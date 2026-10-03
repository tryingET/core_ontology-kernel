#!/usr/bin/env python3
"""Verify and optionally snapshot the vendored ROCS bundle before import.

The checked-in lock digest is the trust anchor. Source traversal is anchored to
no-follow directory descriptors. A requested runtime snapshot is populated from
opened regular-file descriptors while those exact bytes are hashed; callers then
execute only the private verified snapshot, not the mutable source path.
"""

from __future__ import annotations

import argparse
import errno
import hashlib
import json
import os
from dataclasses import dataclass
from pathlib import Path
import re
import shutil
import stat
import sys
from typing import Mapping

TRUSTED_LOCK_DIGEST = "1a05dc91dd1546921861851f4f16cf3dc24af00bcf3b962a72283a37a4b68564"
LOCK_NAME = "VENDORED_HASHES.json"
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
DIAGNOSTIC_LIMIT = 20
_REQUIRED_FLAGS = ("O_DIRECTORY", "O_NOFOLLOW")
if any(not hasattr(os, name) for name in _REQUIRED_FLAGS):
    raise RuntimeError("vendored ROCS verification requires O_DIRECTORY and O_NOFOLLOW")
_DIRECTORY_FLAGS = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | getattr(os, "O_CLOEXEC", 0)
_FILE_FLAGS = (
    os.O_RDONLY | os.O_NOFOLLOW | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NONBLOCK", 0)
)


class BundleVerificationError(RuntimeError):
    """The bundle cannot be admitted without executing its bytes."""


class InvalidFileTypeError(BundleVerificationError):
    """A path raced to, or was observed as, a forbidden filesystem type."""


@dataclass(frozen=True)
class InventoryDiff:
    unexpected: tuple[str, ...]
    missing: tuple[str, ...]
    mismatched: tuple[str, ...]
    invalid_types: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not (self.unexpected or self.missing or self.mismatched or self.invalid_types)


def _sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _read_all(fd: int, label: str) -> bytes:
    chunks: list[bytes] = []
    while True:
        try:
            chunk = os.read(fd, 1024 * 1024)
        except OSError as exc:
            raise BundleVerificationError(f"unable to read {label}: {exc}") from exc
        if not chunk:
            return b"".join(chunks)
        chunks.append(chunk)


def _open_directory_tree(root_arg: str | os.PathLike[str]) -> tuple[int, Path]:
    absolute = Path(os.path.abspath(os.fspath(root_arg)))
    parts = absolute.parts
    if not parts or parts[0] != os.sep:
        raise BundleVerificationError("bundle path must resolve to an absolute local path")
    try:
        fd = os.open(os.sep, _DIRECTORY_FLAGS)
    except OSError as exc:
        raise BundleVerificationError(f"unable to open filesystem root: {exc}") from exc
    try:
        for part in parts[1:]:
            try:
                next_fd = os.open(part, _DIRECTORY_FLAGS, dir_fd=fd)
            except OSError as exc:
                if exc.errno in (errno.ELOOP, errno.ENOTDIR):
                    reason = "symlink or non-directory path component"
                else:
                    reason = str(exc)
                raise BundleVerificationError(
                    f"bundle path is not a no-follow directory tree at {part!r}: {reason}"
                ) from exc
            os.close(fd)
            fd = next_fd
        return fd, absolute
    except BaseException:
        os.close(fd)
        raise


def _open_regular_at(directory_fd: int, name: str, relative: str) -> tuple[int, os.stat_result]:
    try:
        fd = os.open(name, _FILE_FLAGS, dir_fd=directory_fd)
    except OSError as exc:
        if exc.errno == errno.ELOOP:
            raise InvalidFileTypeError(
                f"unable to open regular file {relative}: symlink"
            ) from exc
        raise BundleVerificationError(f"unable to open regular file {relative}: {exc}") from exc
    try:
        metadata = os.fstat(fd)
        if not stat.S_ISREG(metadata.st_mode):
            raise InvalidFileTypeError(f"expected regular file: {relative}")
        return fd, metadata
    except BaseException:
        os.close(fd)
        raise


def _validated_expected(raw: object) -> dict[str, str]:
    if not isinstance(raw, dict):
        raise BundleVerificationError("lock field 'files' must be an object")
    expected: dict[str, str] = {}
    for path, digest in raw.items():
        if not isinstance(path, str) or not path or path.startswith("/") or "\\" in path:
            raise BundleVerificationError("lock contains an invalid relative path")
        parts = Path(path).parts
        if any(part in ("", ".", "..") for part in parts):
            raise BundleVerificationError(f"lock contains a non-normalized path: {path!r}")
        if path == LOCK_NAME:
            raise BundleVerificationError(f"lock must not inventory itself: {path}")
        if not isinstance(digest, str) or not SHA256_RE.fullmatch(digest):
            raise BundleVerificationError(f"lock contains an invalid SHA-256 for {path}")
        expected[path] = digest
    return expected


def load_expected(root_fd: int, trusted_lock_digest: str) -> tuple[dict[str, str], bytes, int]:
    lock_fd, metadata = _open_regular_at(root_fd, LOCK_NAME, LOCK_NAME)
    try:
        lock_bytes = _read_all(lock_fd, LOCK_NAME)
    finally:
        os.close(lock_fd)
    if _sha256_bytes(lock_bytes) != trusted_lock_digest:
        raise BundleVerificationError("lock digest does not match the checked-in trust anchor")
    try:
        payload = json.loads(lock_bytes)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise BundleVerificationError(f"lock is not valid UTF-8 JSON: {exc}") from exc
    if not isinstance(payload, dict) or "files" not in payload:
        raise BundleVerificationError("lock must be an object containing 'files'")
    return _validated_expected(payload["files"]), lock_bytes, stat.S_IMODE(metadata.st_mode)


def _write_private_file(path: Path, raw: bytes, mode: int) -> None:
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW | getattr(os, "O_CLOEXEC", 0)
    fd = os.open(path, flags, mode)
    try:
        view = memoryview(raw)
        while view:
            written = os.write(fd, view)
            if written <= 0:
                raise BundleVerificationError(f"short write while materializing {path}")
            view = view[written:]
        os.fsync(fd)
    finally:
        os.close(fd)


def inventory(
    root_fd: int, destination: Path | None = None
) -> tuple[dict[str, str], tuple[str, ...]]:
    actual: dict[str, str] = {}
    invalid: list[str] = []

    def visit(directory_fd: int, prefix: str, destination_dir: Path | None) -> None:
        try:
            with os.scandir(directory_fd) as scanner:
                entries = sorted(scanner, key=lambda entry: entry.name)
        except OSError as exc:
            raise BundleVerificationError(f"unable to scan bundle directory {prefix or '.'}: {exc}") from exc
        for entry in entries:
            relative = f"{prefix}/{entry.name}" if prefix else entry.name
            try:
                metadata = entry.stat(follow_symlinks=False)
            except OSError as exc:
                raise BundleVerificationError(f"unable to inspect {relative}: {exc}") from exc
            mode = metadata.st_mode
            if stat.S_ISLNK(mode):
                invalid.append(relative)
                continue
            if stat.S_ISDIR(mode):
                try:
                    child_fd = os.open(entry.name, _DIRECTORY_FLAGS, dir_fd=directory_fd)
                except OSError as exc:
                    if exc.errno in (errno.ELOOP, errno.ENOTDIR):
                        invalid.append(relative)
                        continue
                    raise BundleVerificationError(
                        f"unable to open bundle directory {relative}: {exc}"
                    ) from exc
                child_destination = None
                if destination_dir is not None:
                    child_destination = destination_dir / entry.name
                    child_destination.mkdir(mode=0o700)
                try:
                    visit(child_fd, relative, child_destination)
                finally:
                    os.close(child_fd)
                continue
            if stat.S_ISREG(mode):
                if relative == LOCK_NAME:
                    continue
                try:
                    file_fd, opened_metadata = _open_regular_at(directory_fd, entry.name, relative)
                except InvalidFileTypeError:
                    invalid.append(relative)
                    continue
                try:
                    raw = _read_all(file_fd, relative)
                finally:
                    os.close(file_fd)
                actual[relative] = _sha256_bytes(raw)
                if destination_dir is not None:
                    _write_private_file(
                        destination_dir / entry.name, raw, stat.S_IMODE(opened_metadata.st_mode)
                    )
                continue
            invalid.append(relative)

    visit(root_fd, "", destination)
    return actual, tuple(sorted(invalid))


def compare(
    expected: Mapping[str, str], actual: Mapping[str, str], invalid_types: tuple[str, ...] = ()
) -> InventoryDiff:
    expected_paths = set(expected)
    actual_paths = set(actual)
    return InventoryDiff(
        unexpected=tuple(sorted(actual_paths - expected_paths)),
        missing=tuple(sorted(expected_paths - actual_paths)),
        mismatched=tuple(
            sorted(path for path in expected_paths & actual_paths if expected[path] != actual[path])
        ),
        invalid_types=tuple(sorted(invalid_types)),
    )


def verify_bundle(
    root_arg: str | os.PathLike[str],
    *,
    trusted_lock_digest: str = TRUSTED_LOCK_DIGEST,
    snapshot_dir: str | os.PathLike[str] | None = None,
) -> InventoryDiff:
    root_fd, _ = _open_directory_tree(root_arg)
    destination: Path | None = None
    created_destination = False
    try:
        expected, lock_bytes, lock_mode = load_expected(root_fd, trusted_lock_digest)
        if snapshot_dir is not None:
            destination = Path(snapshot_dir)
            if destination.exists() or destination.is_symlink():
                raise BundleVerificationError(f"snapshot destination must not exist: {destination}")
            destination.mkdir(mode=0o700, parents=False)
            created_destination = True
            _write_private_file(destination / LOCK_NAME, lock_bytes, lock_mode)
        actual, invalid = inventory(root_fd, destination)
        diff = compare(expected, actual, invalid)
        if not diff.ok and created_destination and destination is not None:
            shutil.rmtree(destination)
            created_destination = False
        return diff
    except BaseException:
        if created_destination and destination is not None:
            shutil.rmtree(destination)
        raise
    finally:
        os.close(root_fd)


def _emit_category(label: str, paths: tuple[str, ...]) -> None:
    if not paths:
        return
    print(f"- {label}: {len(paths)}", file=sys.stderr)
    for path in paths[:DIAGNOSTIC_LIMIT]:
        print(f"  {path}", file=sys.stderr)
    if len(paths) > DIAGNOSTIC_LIMIT:
        print(f"  ... {len(paths) - DIAGNOSTIC_LIMIT} more", file=sys.stderr)


def main(argv: list[str], *, trusted_lock_digest: str = TRUSTED_LOCK_DIGEST) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bundle_dir")
    parser.add_argument("--snapshot-dir")
    try:
        args = parser.parse_args(argv[1:])
        diff = verify_bundle(
            args.bundle_dir,
            trusted_lock_digest=trusted_lock_digest,
            snapshot_dir=args.snapshot_dir,
        )
    except KeyboardInterrupt:
        print("ROCS bundled runtime verification interrupted", file=sys.stderr)
        return 130
    except (BundleVerificationError, OSError) as exc:
        print(f"ROCS bundled runtime verification error: {exc}", file=sys.stderr)
        return 1
    if not diff.ok:
        print("ROCS bundled runtime verification failed closed", file=sys.stderr)
        _emit_category("unexpected regular files", diff.unexpected)
        _emit_category("missing regular files", diff.missing)
        _emit_category("hash mismatches", diff.mismatched)
        _emit_category("invalid file types", diff.invalid_types)
        if diff.unexpected and all(
            "/__pycache__/" in f"/{path}" and path.endswith((".pyc", ".pyo"))
            for path in diff.unexpected
        ):
            print(
                "generated Python bytecode contaminated the vendored bundle; remove only the "
                "reported ignored __pycache__ directories, then use scripts/rocs.sh",
                file=sys.stderr,
            )
        return 1
    print("ROCS bundled runtime verification: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
