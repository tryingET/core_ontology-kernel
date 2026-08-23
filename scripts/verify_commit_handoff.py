#!/usr/bin/env python3
"""Observe whether one exact remote ref currently reports a local commit OID."""

from __future__ import annotations

import argparse
import json
import os
import re
import selectors
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path
from urllib.parse import urlsplit

EXIT_INVALID_INPUT = 2
EXIT_LOCAL_OBJECT = 3
EXIT_REMOTE_UNAVAILABLE = 4
EXIT_REF_ABSENT = 5
EXIT_OID_MISMATCH = 6
DEFAULT_TIMEOUT_SECONDS = 15
MAX_TIMEOUT_SECONDS = 300
MAX_GIT_OUTPUT_BYTES = 64 * 1024
OID_LENGTHS = {"sha1": 40, "sha256": 64}
ENV_PASSTHROUGH = (
    "HOME",
    "PATH",
    "XDG_CONFIG_HOME",
    "SSH_AUTH_SOCK",
    "SSL_CERT_FILE",
    "SSL_CERT_DIR",
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "ALL_PROXY",
    "NO_PROXY",
    "http_proxy",
    "https_proxy",
    "all_proxy",
    "no_proxy",
)
INSECURE_REMOTE_SCHEMES = {"ftp", "git", "http"}


class HandoffError(Exception):
    def __init__(self, exit_code: int, code: str) -> None:
        super().__init__(code)
        self.exit_code = exit_code
        self.code = code


def _git_environment() -> dict[str, str]:
    env = {
        key: value
        for key in ENV_PASSTHROUGH
        if (value := os.environ.get(key)) is not None
    }
    env.setdefault("PATH", os.defpath)
    env.update(
        {
            "GIT_TERMINAL_PROMPT": "0",
            "GIT_ASKPASS": "/bin/false",
            "LC_ALL": "C",
            "LANG": "C",
        }
    )
    return env


def _kill_process_group(process: subprocess.Popen[bytes]) -> None:
    try:
        os.killpg(process.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    except PermissionError:
        process.kill()
    try:
        process.wait(timeout=1)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait()


def _run_git(
    repo: Path,
    arguments: list[str],
    timeout: int,
    *,
    execution_error: tuple[int, str] = (EXIT_INVALID_INPUT, "git_unavailable"),
    output_error: tuple[int, str] = (EXIT_INVALID_INPUT, "git_output_limit"),
) -> subprocess.CompletedProcess[str]:
    env = _git_environment()
    git_binary = shutil.which("git", path=env["PATH"])
    if git_binary is None:
        raise HandoffError(*execution_error)
    command = [git_binary, "-C", str(repo), *arguments]
    try:
        process = subprocess.Popen(
            command,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            env=env,
            start_new_session=True,
        )
    except OSError as exc:
        raise HandoffError(*execution_error) from exc

    output = bytearray()
    deadline = time.monotonic() + timeout
    selector = selectors.DefaultSelector()
    assert process.stdout is not None
    selector.register(process.stdout, selectors.EVENT_READ)
    try:
        while process.poll() is None or selector.get_map():
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise HandoffError(*execution_error)
            for key, _ in selector.select(min(remaining, 0.1)):
                chunk = os.read(key.fd, min(8192, MAX_GIT_OUTPUT_BYTES + 1 - len(output)))
                if not chunk:
                    selector.unregister(key.fileobj)
                    continue
                output.extend(chunk)
                if len(output) > MAX_GIT_OUTPUT_BYTES:
                    raise HandoffError(*output_error)
        return subprocess.CompletedProcess(
            command,
            process.returncode,
            output.decode("utf-8", errors="replace"),
            "",
        )
    except HandoffError:
        _kill_process_group(process)
        raise
    finally:
        selector.close()
        process.stdout.close()


def _local_git(repo: Path, arguments: list[str], timeout: int = DEFAULT_TIMEOUT_SECONDS) -> str:
    result = _run_git(repo, arguments, timeout)
    if result.returncode != 0:
        raise HandoffError(EXIT_INVALID_INPUT, "invalid_repository")
    return result.stdout.strip()


def _validate_ref(repo: Path, ref: str) -> None:
    if not (ref.startswith("refs/heads/") or ref.startswith("refs/tags/")):
        raise HandoffError(EXIT_INVALID_INPUT, "invalid_remote_ref")
    if any(ord(character) < 32 or ord(character) == 127 for character in ref):
        raise HandoffError(EXIT_INVALID_INPUT, "invalid_remote_ref")
    result = _run_git(repo, ["check-ref-format", ref], DEFAULT_TIMEOUT_SECONDS)
    if result.returncode != 0:
        raise HandoffError(EXIT_INVALID_INPUT, "invalid_remote_ref")


def _configured_remote_names(repo: Path) -> set[str]:
    result = _run_git(repo, ["remote"], DEFAULT_TIMEOUT_SECONDS)
    if result.returncode != 0:
        raise HandoffError(EXIT_INVALID_INPUT, "invalid_repository")
    return {line for line in result.stdout.splitlines() if line}


def _configured_remote_urls(repo: Path, remote: str) -> list[str]:
    fetch = _run_git(repo, ["remote", "get-url", "--all", "--", remote], DEFAULT_TIMEOUT_SECONDS)
    push = _run_git(
        repo,
        ["remote", "get-url", "--push", "--all", "--", remote],
        DEFAULT_TIMEOUT_SECONDS,
    )
    if fetch.returncode != 0 or push.returncode != 0:
        raise HandoffError(EXIT_INVALID_INPUT, "invalid_remote")
    urls = [line for output in (fetch.stdout, push.stdout) for line in output.splitlines() if line]
    if not urls:
        raise HandoffError(EXIT_INVALID_INPUT, "invalid_remote")
    return list(dict.fromkeys(urls))


def _validate_transport_endpoint(repo: Path, endpoint: str) -> None:
    scheme_match = re.match(r"^([A-Za-z][A-Za-z0-9+.-]*)://", endpoint)
    if scheme_match is not None:
        scheme = scheme_match.group(1).lower()
        if scheme in INSECURE_REMOTE_SCHEMES:
            raise HandoffError(EXIT_INVALID_INPUT, "insecure_remote_transport")
        if scheme not in {"file", "https", "ssh"}:
            raise HandoffError(EXIT_INVALID_INPUT, "unsupported_remote_transport")
        try:
            parsed = urlsplit(endpoint)
            if parsed.password is not None or parsed.query or parsed.fragment:
                raise HandoffError(EXIT_INVALID_INPUT, "embedded_remote_credentials")
            if scheme == "https":
                if parsed.hostname is None or parsed.username is not None:
                    raise HandoffError(EXIT_INVALID_INPUT, "embedded_remote_credentials")
                parsed.port
                return
            if scheme == "ssh":
                if parsed.hostname is None:
                    raise HandoffError(EXIT_INVALID_INPUT, "invalid_remote")
                parsed.port
                return
            if parsed.hostname not in (None, "", "localhost") or not Path(parsed.path).is_absolute():
                raise HandoffError(EXIT_INVALID_INPUT, "unsupported_remote_transport")
            if not Path(parsed.path).exists():
                raise HandoffError(EXIT_INVALID_INPUT, "invalid_remote")
            return
        except ValueError as exc:
            raise HandoffError(EXIT_INVALID_INPUT, "invalid_remote") from exc
    if "::" in endpoint:
        raise HandoffError(EXIT_INVALID_INPUT, "unsupported_remote_transport")
    if re.fullmatch(
        r"(?:[A-Za-z0-9._-]+@)?(?:\[[0-9A-Fa-f:]+\]|[A-Za-z0-9.-]+):[^\s:]+",
        endpoint,
    ):
        return
    local_path = Path(endpoint)
    if not local_path.is_absolute():
        local_path = repo / local_path
    if not local_path.exists():
        raise HandoffError(EXIT_INVALID_INPUT, "unsupported_remote_transport")


def _validate_remote_transport(repo: Path, remote: str) -> None:
    if remote in _configured_remote_names(repo):
        endpoints = _configured_remote_urls(repo, remote)
    else:
        endpoints = [remote]
        _validate_transport_endpoint(repo, remote)
    effective = _run_git(
        repo,
        ["ls-remote", "--get-url", "--", remote],
        DEFAULT_TIMEOUT_SECONDS,
    )
    effective_urls = [line for line in effective.stdout.splitlines() if line]
    if effective.returncode != 0 or len(effective_urls) != 1:
        raise HandoffError(EXIT_INVALID_INPUT, "invalid_remote")
    for endpoint in [*endpoints, effective_urls[0]]:
        _validate_transport_endpoint(repo, endpoint)


def verify(repo: Path, remote: str, ref: str, oid: str, timeout: int) -> dict[str, object]:
    if timeout < 1 or timeout > MAX_TIMEOUT_SECONDS:
        raise HandoffError(EXIT_INVALID_INPUT, "invalid_timeout")
    if not remote or remote.startswith("-") or any(ord(c) < 32 or ord(c) == 127 for c in remote):
        raise HandoffError(EXIT_INVALID_INPUT, "invalid_remote")

    object_format = _local_git(repo, ["rev-parse", "--show-object-format=storage"])
    oid_length = OID_LENGTHS.get(object_format)
    if oid_length is None:
        raise HandoffError(EXIT_INVALID_INPUT, "unsupported_object_format")
    if re.fullmatch(rf"[0-9a-f]{{{oid_length}}}", oid) is None:
        raise HandoffError(EXIT_INVALID_INPUT, "invalid_commit_oid")
    _validate_ref(repo, ref)
    _validate_remote_transport(repo, remote)

    object_type = _run_git(repo, ["cat-file", "-t", oid], DEFAULT_TIMEOUT_SECONDS)
    if object_type.returncode != 0 or object_type.stdout.strip() != "commit":
        raise HandoffError(EXIT_LOCAL_OBJECT, "local_commit_unavailable")

    patterns = [ref]
    peeled_ref = ref + "^{}"
    if ref.startswith("refs/tags/"):
        patterns.append(peeled_ref)
    result = _run_git(
        repo,
        ["ls-remote", "--", remote, *patterns],
        timeout,
        execution_error=(EXIT_REMOTE_UNAVAILABLE, "remote_unavailable"),
        output_error=(EXIT_REMOTE_UNAVAILABLE, "remote_output_limit"),
    )
    if result.returncode != 0:
        raise HandoffError(EXIT_REMOTE_UNAVAILABLE, "remote_unavailable")

    observations: dict[str, set[str]] = {}
    for line in result.stdout.splitlines():
        fields = line.split("\t")
        if len(fields) == 2 and fields[1] in (ref, peeled_ref):
            observations.setdefault(fields[1], set()).add(fields[0])
    direct = observations.get(ref, set())
    if not direct:
        raise HandoffError(EXIT_REF_ABSENT, "remote_ref_absent")
    peeled = observations.get(peeled_ref, set())
    observed = peeled if ref.startswith("refs/tags/") and peeled else direct
    if len(direct) != 1 or len(observed) != 1 or oid not in observed:
        raise HandoffError(EXIT_OID_MISMATCH, "remote_oid_mismatch")

    return {
        "authority_ceiling": (
            "observation_only: no semantic release, publication authority, adoption, or AK evidence"
        ),
        "commit_oid": oid,
        "object_format": object_format,
        "remote_endpoint": "<redacted>",
        "remote_ref": ref,
        "schema": "ontology-kernel.commit-handoff-observation.v1",
        "verified": True,
    }


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    parser.add_argument("--remote", required=True)
    parser.add_argument("--ref", required=True)
    parser.add_argument("--commit", required=True)
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    return parser


def main() -> int:
    args = _parser().parse_args()
    try:
        payload = verify(args.repo, args.remote, args.ref, args.commit, args.timeout)
    except HandoffError as exc:
        print(json.dumps({"error": exc.code}, sort_keys=True, separators=(",", ":")), file=sys.stderr)
        return exc.exit_code
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
