#!/usr/bin/env python3
from __future__ import annotations

from contextlib import redirect_stderr
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "verify_vendored_rocs.py"
SPEC = importlib.util.spec_from_file_location("verify_vendored_rocs", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def make_bundle(root: Path, files: dict[str, bytes]) -> str:
    expected: dict[str, str] = {}
    for relative, raw in files.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        expected[relative] = hashlib.sha256(raw).hexdigest()
    lock = json.dumps({"files": expected}, sort_keys=True, separators=(",", ":")).encode()
    (root / MODULE.LOCK_NAME).write_bytes(lock)
    return hashlib.sha256(lock).hexdigest()


class InventoryDiffTests(unittest.TestCase):
    def test_compare_classifies_every_drift_kind(self) -> None:
        expected = {"kept.py": "a" * 64, "missing.py": "b" * 64, "changed.py": "c" * 64}
        actual = {
            "kept.py": "a" * 64,
            "changed.py": "d" * 64,
            "pkg/__pycache__/ambient.pyc": "e" * 64,
        }
        diff = MODULE.compare(expected, actual, ("linked.py",))
        self.assertFalse(diff.ok)
        self.assertEqual(diff.unexpected, ("pkg/__pycache__/ambient.pyc",))
        self.assertEqual(diff.missing, ("missing.py",))
        self.assertEqual(diff.mismatched, ("changed.py",))
        self.assertEqual(diff.invalid_types, ("linked.py",))

    def test_clean_bundle_materializes_exact_private_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw) / "bundle"
            root.mkdir()
            digest = make_bundle(root, {"rocs.py": b"print('ok')\n", "src/pkg.py": b"VALUE = 1\n"})
            snapshot = Path(raw) / "snapshot"
            diff = MODULE.verify_bundle(root, trusted_lock_digest=digest, snapshot_dir=snapshot)
            self.assertTrue(diff.ok)
            self.assertEqual((snapshot / "rocs.py").read_bytes(), b"print('ok')\n")
            self.assertEqual((snapshot / "src/pkg.py").read_bytes(), b"VALUE = 1\n")
            self.assertTrue((snapshot / MODULE.LOCK_NAME).is_file())

    def test_bundle_root_and_ancestor_symlinks_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            base = Path(raw)
            real_parent = base / "real-parent"
            root = real_parent / "bundle"
            root.mkdir(parents=True)
            digest = make_bundle(root, {"rocs.py": b"pass\n"})
            root_link = base / "bundle-link"
            root_link.symlink_to(root, target_is_directory=True)
            with self.assertRaises(MODULE.BundleVerificationError):
                MODULE.verify_bundle(root_link, trusted_lock_digest=digest)
            parent_link = base / "parent-link"
            parent_link.symlink_to(real_parent, target_is_directory=True)
            with self.assertRaises(MODULE.BundleVerificationError):
                MODULE.verify_bundle(parent_link / "bundle", trusted_lock_digest=digest)

    def test_lock_symlink_is_rejected_before_target_read(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            base = Path(raw)
            root = base / "bundle"
            root.mkdir()
            external = base / "external-lock"
            external.write_bytes(b"not json and must not be read")
            (root / MODULE.LOCK_NAME).symlink_to(external)
            root_fd, _ = MODULE._open_directory_tree(root)
            try:
                with self.assertRaises(MODULE.BundleVerificationError) as caught:
                    MODULE.load_expected(root_fd, hashlib.sha256(external.read_bytes()).hexdigest())
            finally:
                os.close(root_fd)
            self.assertIn("unable to open regular file", str(caught.exception))

    def test_nested_symlink_and_fifo_are_invalid_without_traversal(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            base = Path(raw)
            root = base / "bundle"
            root.mkdir()
            digest = make_bundle(root, {})
            external = base / "external"
            external.mkdir()
            (external / "canary.py").write_bytes(b"never hash me")
            (root / "linked-dir").symlink_to(external, target_is_directory=True)
            os.mkfifo(root / "special")
            diff = MODULE.verify_bundle(root, trusted_lock_digest=digest)
            self.assertEqual(diff.invalid_types, ("linked-dir", "special"))
            self.assertFalse(diff.ok)

    def test_missing_mismatch_and_unexpected_are_reported(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw) / "bundle"
            root.mkdir()
            digest = make_bundle(root, {"missing.py": b"expected\n", "changed.py": b"before\n"})
            (root / "missing.py").unlink()
            (root / "changed.py").write_bytes(b"after\n")
            (root / "ambient.pyc").write_bytes(b"cache\n")
            diff = MODULE.verify_bundle(root, trusted_lock_digest=digest)
            self.assertEqual(diff.missing, ("missing.py",))
            self.assertEqual(diff.mismatched, ("changed.py",))
            self.assertEqual(diff.unexpected, ("ambient.pyc",))

    def test_trust_anchor_and_lock_shapes_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw) / "bundle"
            root.mkdir()
            digest = make_bundle(root, {})
            with self.assertRaises(MODULE.BundleVerificationError):
                MODULE.verify_bundle(root, trusted_lock_digest="0" * 64)
            self.assertTrue(MODULE.verify_bundle(root, trusted_lock_digest=digest).ok)
        with self.assertRaises(MODULE.BundleVerificationError):
            MODULE._validated_expected({"../escape.py": "a" * 64})
        with self.assertRaises(MODULE.BundleVerificationError):
            MODULE._validated_expected({"bad.py": "not-a-digest"})
        with self.assertRaises(MODULE.BundleVerificationError):
            MODULE._validated_expected({MODULE.LOCK_NAME: "a" * 64})

    def test_cli_diagnostics_are_bounded_and_truthful(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw) / "bundle"
            root.mkdir()
            digest = make_bundle(root, {})
            for index in range(25):
                (root / f"unexpected-{index:02d}.py").write_bytes(b"x")
            stderr = io.StringIO()
            with redirect_stderr(stderr):
                result = MODULE.main(["verify", str(root)], trusted_lock_digest=digest)
            output = stderr.getvalue()
            self.assertEqual(result, 1)
            self.assertIn("unexpected regular files: 25", output)
            self.assertIn("... 5 more", output)
            self.assertNotIn("lock invalid", output)


if __name__ == "__main__":
    unittest.main()
