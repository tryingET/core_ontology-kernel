from __future__ import annotations

import json
import os
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "verify_commit_handoff.py"


class VerifyCommitHandoffTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.local = self.root / "local"
        self.remote = self.root / "remote.git"
        self._git("init", "-q", str(self.local), cwd=self.root)
        self._git("init", "-q", "--bare", str(self.remote), cwd=self.root)
        self._git("config", "user.name", "Handoff Test")
        self._git("config", "user.email", "handoff@example.invalid")
        (self.local / "record.txt").write_text("first\n", encoding="utf-8")
        self._git("add", "record.txt")
        self._git("commit", "-q", "-m", "first")
        self.first = self._git("rev-parse", "HEAD").stdout.strip()
        self._git("branch", "handoff", self.first)
        self._git("tag", "lightweight", self.first)
        self._git("tag", "-a", "annotated", self.first, "-m", "annotated")
        self._git("push", "-q", str(self.remote), "handoff", "lightweight", "annotated")
        self._git("remote", "add", "handoff-origin", str(self.remote))
        (self.local / "record.txt").write_text("second\n", encoding="utf-8")
        self._git("commit", "-q", "-am", "second")
        self.second = self._git("rev-parse", "HEAD").stdout.strip()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _git(self, *args: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["git", *args],
            cwd=cwd or self.local,
            text=True,
            capture_output=True,
            check=True,
        )

    def _verify(
        self,
        ref: str,
        oid: str | None = None,
        remote: str | None = None,
        timeout: int = 5,
        env: dict[str, str] | None = None,
    ) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--repo",
                str(self.local),
                "--remote",
                remote or str(self.remote),
                "--ref",
                ref,
                "--commit",
                oid or self.first,
                "--timeout",
                str(timeout),
            ],
            cwd=REPO,
            text=True,
            capture_output=True,
            check=False,
            env=env,
        )

    def _git_wrapper(self, ls_remote_body: str) -> Path:
        real_git = shutil.which("git")
        self.assertIsNotNone(real_git)
        bin_dir = self.root / "fake-bin"
        bin_dir.mkdir(exist_ok=True)
        wrapper = bin_dir / "git"
        wrapper.write_text(
            "#!/bin/sh\n"
            "has_ls_remote=0\n"
            "has_get_url=0\n"
            "for argument in \"$@\"; do\n"
            "  [ \"$argument\" = ls-remote ] && has_ls_remote=1\n"
            "  [ \"$argument\" = --get-url ] && has_get_url=1\n"
            "done\n"
            "if [ \"$has_ls_remote\" -eq 1 ] && [ \"$has_get_url\" -eq 0 ]; then\n"
            f"{ls_remote_body}\n"
            "fi\n"
            f"exec {shlex.quote(str(real_git))} \"$@\"\n",
            encoding="utf-8",
        )
        wrapper.chmod(0o755)
        return bin_dir

    def assert_error(self, result: subprocess.CompletedProcess[str], exit_code: int, code: str) -> None:
        self.assertEqual(result.returncode, exit_code, result)
        self.assertEqual(json.loads(result.stderr), {"error": code})
        self.assertEqual(result.stdout, "")

    def test_abbreviated_oid_and_unqualified_ref_are_invalid(self) -> None:
        self.assert_error(
            self._verify("refs/heads/handoff", self.first[:12]), 2, "invalid_commit_oid"
        )
        self.assert_error(self._verify("handoff"), 2, "invalid_remote_ref")
        self.assert_error(self._verify("HEAD"), 2, "invalid_remote_ref")

    def test_checkout_is_irrelevant_and_matching_branch_passes(self) -> None:
        self.assertNotEqual(self.first, self.second)
        self.assertEqual(self._git("rev-parse", "HEAD").stdout.strip(), self.second)
        result = self._verify("refs/heads/handoff")
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["commit_oid"], self.first)
        self.assertEqual(payload["remote_ref"], "refs/heads/handoff")
        self.assertEqual(payload["remote_endpoint"], "<redacted>")
        self.assertTrue(payload["verified"])

    def test_matching_lightweight_and_annotated_tags_pass(self) -> None:
        for tag in ("lightweight", "annotated"):
            with self.subTest(tag=tag):
                result = self._verify(f"refs/tags/{tag}")
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(json.loads(result.stdout)["commit_oid"], self.first)

    def test_configured_remote_name_resolves_without_disclosing_endpoint(self) -> None:
        result = self._verify("refs/heads/handoff", remote="handoff-origin")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["remote_endpoint"], "<redacted>")
        self.assertNotIn(str(self.remote), result.stdout + result.stderr)

    def test_configured_remote_rejects_insecure_push_url(self) -> None:
        self._git("remote", "add", "split-origin", str(self.remote))
        self._git(
            "remote",
            "set-url",
            "--push",
            "split-origin",
            "http://oauth2@example.invalid/private.git",
        )
        self.assert_error(
            self._verify("refs/heads/handoff", remote="split-origin"),
            2,
            "insecure_remote_transport",
        )

    def test_missing_mismatched_and_nonlocal_commits_have_distinct_failures(self) -> None:
        self.assert_error(self._verify("refs/heads/missing"), 5, "remote_ref_absent")
        self.assert_error(
            self._verify("refs/heads/handoff", self.second), 6, "remote_oid_mismatch"
        )
        absent_oid = "0" * len(self.first)
        self.assert_error(
            self._verify("refs/heads/handoff", absent_oid), 3, "local_commit_unavailable"
        )

    def test_ambient_git_selection_and_trace_variables_are_ignored(self) -> None:
        ambient_git_dir = self.root / "ambient.git"
        self._git("init", "-q", "--bare", str(ambient_git_dir), cwd=self.root)
        trace = self.root / "git.trace"
        env = os.environ.copy()
        env.update({"GIT_DIR": str(ambient_git_dir), "GIT_TRACE": str(trace)})
        result = self._verify("refs/heads/handoff", env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(trace.exists())

    def test_plaintext_and_embedded_credential_remotes_fail_before_git_transport(self) -> None:
        trace = self.root / "credential.trace"
        env = os.environ.copy()
        env["GIT_TRACE"] = str(trace)
        self.assert_error(
            self._verify(
                "refs/heads/handoff",
                remote="https://user:credential-that-must-not-leak@example.invalid/private.git",
                env=env,
            ),
            2,
            "embedded_remote_credentials",
        )
        self.assert_error(
            self._verify("refs/heads/handoff", remote="http://example.invalid/private.git"),
            2,
            "insecure_remote_transport",
        )
        self.assertFalse(trace.exists())

    def test_effective_url_rewrite_cannot_bypass_transport_policy(self) -> None:
        home = self.root / "home"
        xdg = self.root / "xdg"
        home.mkdir()
        xdg.mkdir()
        (home / ".gitconfig").write_text(
            '[url "http://plain.invalid/"]\n\tinsteadOf = https://safe.invalid/\n',
            encoding="utf-8",
        )
        env = os.environ.copy()
        env.update({"HOME": str(home), "XDG_CONFIG_HOME": str(xdg)})
        self.assert_error(
            self._verify(
                "refs/heads/handoff",
                remote="https://safe.invalid/repository.git",
                env=env,
            ),
            2,
            "insecure_remote_transport",
        )

    def test_remote_helpers_and_unknown_schemes_are_rejected(self) -> None:
        for remote in ("ext::sh -c true", "foo://example.invalid/repository.git"):
            with self.subTest(remote=remote):
                self.assert_error(
                    self._verify("refs/heads/handoff", remote=remote),
                    2,
                    "unsupported_remote_transport",
                )

    def test_unreachable_secure_remote_is_bounded(self) -> None:
        started = time.monotonic()
        result = self._verify(
            "refs/heads/handoff", remote="https://127.0.0.1:9/private.git", timeout=2
        )
        self.assert_error(result, 4, "remote_unavailable")
        self.assertLess(time.monotonic() - started, 5)

    def test_timeout_kills_transport_descendants(self) -> None:
        marker = self.root / "transport-child-finished"
        body = (
            f"    (sleep 2; printf done > {shlex.quote(str(marker))}) &\n"
            "    sleep 30\n"
            "    exit 0"
        )
        bin_dir = self._git_wrapper(body)
        env = os.environ.copy()
        env["PATH"] = f"{bin_dir}{os.pathsep}{env.get('PATH', os.defpath)}"
        result = self._verify("refs/heads/handoff", timeout=1, env=env)
        self.assert_error(result, 4, "remote_unavailable")
        time.sleep(1.3)
        self.assertFalse(marker.exists())

    def test_oversized_remote_output_fails_closed_and_kills_descendants(self) -> None:
        marker = self.root / "oversized-child-finished"
        body = (
            f"    (sleep 1; printf done > {shlex.quote(str(marker))}) &\n"
            "    count=0\n"
            "    while [ \"$count\" -lt 5000 ]; do\n"
            "      printf '0000000000000000000000000000000000000000\\trefs/heads/handoff\\n'\n"
            "      count=$((count + 1))\n"
            "    done\n"
            "    exit 0"
        )
        bin_dir = self._git_wrapper(body)
        env = os.environ.copy()
        env["PATH"] = f"{bin_dir}{os.pathsep}{env.get('PATH', os.defpath)}"
        result = self._verify("refs/heads/handoff", env=env)
        self.assert_error(result, 4, "remote_output_limit")
        time.sleep(1.3)
        self.assertFalse(marker.exists())

    def test_missing_git_is_not_misclassified_as_remote_failure(self) -> None:
        env = os.environ.copy()
        env["PATH"] = ""
        result = self._verify("refs/heads/handoff", env=env)
        self.assert_error(result, 2, "git_unavailable")

    def test_success_output_has_observation_only_authority_ceiling(self) -> None:
        result = self._verify("refs/heads/handoff")
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        ceiling = payload["authority_ceiling"]
        self.assertIn("observation_only", ceiling)
        self.assertIn("no semantic release", ceiling)
        self.assertIn("publication authority", ceiling)
        self.assertIn("adoption", ceiling)
        self.assertIn("AK evidence", ceiling)
        self.assertNotIn(str(self.remote), result.stdout)


if __name__ == "__main__":
    unittest.main()
