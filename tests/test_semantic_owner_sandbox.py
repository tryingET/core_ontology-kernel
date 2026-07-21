from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SCRIPT = REPO / "scripts" / "semantic_owner_sandbox.py"
FIXTURES = REPO / "tests" / "fixtures" / "semantic-owner-sandbox"

spec = importlib.util.spec_from_file_location("semantic_owner_sandbox", SCRIPT)
assert spec and spec.loader
sandbox = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = sandbox
spec.loader.exec_module(sandbox)


def load(name: str):
    return json.loads((FIXTURES / name).read_text(encoding="utf-8"))


def tree_snapshot(root: Path) -> dict[str, tuple[int, bytes]]:
    if not root.exists():
        return {}
    return {
        path.relative_to(root).as_posix(): (path.stat().st_mode & 0o777, path.read_bytes())
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


class SemanticOwnerSandboxTests(unittest.TestCase):
    def test_committed_fixtures_regenerate_byte_identically(self) -> None:
        for name, value in sandbox.fixture_values().items():
            self.assertEqual(
                (FIXTURES / name).read_text(encoding="utf-8"),
                sandbox.pretty_json(value),
            )

    def test_all_six_owner_contracts_and_non_authorization_are_explicit(self) -> None:
        store = sandbox.validate_store(load("owner-store.json"))
        self.assertFalse(store["live_acquisition_implemented"])
        self.assertTrue(store["sandbox_only"])
        self.assertEqual(
            {record["role"] for record in store["records"]},
            set(sandbox.ROLE_CONTRACTS),
        )
        for record in store["records"]:
            self.assertEqual(record["issuer"], sandbox.ISSUER)
            self.assertEqual(record["owner_repository"], sandbox.OWNER_REPOSITORY)
            self.assertEqual(record["artifact"]["environment"], "disposable_sandbox")
            self.assertTrue(record["artifact"]["non_authorizing"])
            self.assertFalse(record["artifact"]["production_state_mutated"])
            self.assertTrue(record["artifact"]["namespace"].endswith("sandbox.task-3988"))

    def test_publication_fixture_covers_append_only_withdrawal_and_revocation(self) -> None:
        store = load("owner-store.json")
        record = next(record for record in store["records"] if record["role"] == "publication_state")
        artifact = record["artifact"]
        self.assertEqual([row["status"] for row in artifact["history"]], ["published", "withdrawn", "revoked"])
        self.assertEqual([row["revision"] for row in artifact["history"]], [1, 2, 3])
        self.assertIsNone(artifact["canonical_production_head"])
        self.assertFalse(artifact["publication_authorized"])
        self.assertTrue(artifact["append_only"])
        self.assertTrue(artifact["cas_lineage_complete"])

    def test_receipts_replay_exactly_and_are_read_only_owner_issued(self) -> None:
        store = load("owner-store.json")
        request = load("acquisition-request.json")
        expected = load("expected-receipts.json")
        actual = sandbox.acquire(store, request)
        self.assertEqual(expected, actual)
        sandbox.validate_bundle(expected, store, request)
        self.assertFalse(actual["live_acquisition_implemented"])
        self.assertEqual(len(actual["pins"]), 6)
        self.assertEqual(len(actual["receipts"]), 6)
        for receipt in actual["receipts"]:
            self.assertEqual(receipt["schema"], "semantic-owner-store-read-receipt.v0")
            self.assertEqual(receipt["issuer"], sandbox.ISSUER)
            self.assertEqual(receipt["claim_scope"], "owner_store_read_only")
            self.assertEqual(receipt["store_head_digest"], store["store_head_digest"])

    def test_acquisition_does_not_touch_ontology_or_dist(self) -> None:
        source_before = tree_snapshot(REPO / "ontology" / "src")
        dist_before = tree_snapshot(REPO / "ontology" / "dist")
        sandbox.acquire(load("owner-store.json"), load("acquisition-request.json"))
        self.assertEqual(source_before, tree_snapshot(REPO / "ontology" / "src"))
        self.assertEqual(dist_before, tree_snapshot(REPO / "ontology" / "dist"))

    def test_live_flag_foreign_issuer_and_digest_tampering_fail_closed(self) -> None:
        store = load("owner-store.json")
        live = copy.deepcopy(store)
        live["live_acquisition_implemented"] = True
        with self.assertRaisesRegex(sandbox.SandboxContractError, "live acquisition"):
            sandbox.validate_store(live)
        foreign = copy.deepcopy(store)
        foreign["records"][0]["issuer"]["id"] = "rocs"
        with self.assertRaisesRegex(sandbox.SandboxContractError, "foreign semantic-owner"):
            sandbox.validate_store(foreign)
        tampered = copy.deepcopy(store)
        tampered["records"][1]["artifact"]["classification"] = "compatible"
        with self.assertRaisesRegex(sandbox.SandboxContractError, "artifact digest mismatch"):
            sandbox.validate_store(tampered)

        # Unkeyed fixture digests are integrity checks, not authority. Even a
        # fully rehashed attempt to manufacture production authority must fail
        # the closed role-specific fixture equality check.
        unsafe = copy.deepcopy(store)
        publication = next(record for record in unsafe["records"] if record["role"] == "publication_state")
        publication["artifact"]["canonical_production_head"] = sandbox._fixture_digest("attacker-head")
        publication["artifact"]["publication_authorized"] = True
        publication["artifact"]["artifact_digest"] = sandbox.object_digest(
            "ontology-kernel.semantic-owner-sandbox-artifact.v0", publication["artifact"], "artifact_digest"
        )
        publication["artifact_digest"] = publication["artifact"]["artifact_digest"]
        publication["record_digest"] = sandbox.object_digest(
            "ontology-kernel.semantic-owner-sandbox-record.v0", publication, "record_digest"
        )
        unsafe["store_head_digest"] = sandbox.object_digest(
            "ontology-kernel.semantic-owner-sandbox-store.v0", unsafe, "store_head_digest"
        )
        with self.assertRaisesRegex(sandbox.SandboxContractError, "closed owner-issued"):
            sandbox.acquire(unsafe, load("acquisition-request.json"))

    def test_stale_unknown_and_replayed_receipt_tampering_fail_closed(self) -> None:
        store = load("owner-store.json")
        request = load("acquisition-request.json")
        stale = copy.deepcopy(request)
        stale["action_epoch"] = 0
        with self.assertRaisesRegex(sandbox.SandboxContractError, "stale"):
            sandbox.acquire(store, stale)
        future = copy.deepcopy(request)
        future["action_epoch"] = 2
        with self.assertRaisesRegex(sandbox.SandboxContractError, "closed fixture epoch"):
            sandbox.acquire(store, future)
        boolean_floor = copy.deepcopy(request)
        boolean_floor["required_action_epoch_floor"] = True
        with self.assertRaisesRegex(sandbox.SandboxContractError, "action epoch floor drift"):
            sandbox.acquire(store, boolean_floor)
        unknown = copy.deepcopy(request)
        unknown["roles"] = ["consumer_acceptance"]
        with self.assertRaisesRegex(sandbox.SandboxContractError, "unknown role"):
            sandbox.acquire(store, unknown)
        receipts = load("expected-receipts.json")
        receipts["receipts"][0]["store_revision"] = 2
        with self.assertRaisesRegex(sandbox.SandboxContractError, "does not replay"):
            sandbox.validate_bundle(receipts, store, request)

        # Python considers True equal to 1. Replay must compare canonical,
        # type-aware bytes so booleans cannot impersonate integer currentness.
        for label, path in (
            ("bundle action epoch", ("action_epoch",)),
            ("receipt store revision", ("receipts", 0, "store_revision")),
            ("pin action epoch floor", ("pins", 0, "required_action_epoch_floor")),
        ):
            drift = load("expected-receipts.json")
            target = drift
            for component in path[:-1]:
                target = target[component]
            target[path[-1]] = True
            with self.subTest(label=label), self.assertRaisesRegex(
                sandbox.SandboxContractError, "does not replay"
            ):
                sandbox.validate_bundle(drift, store, request)

    def test_cli_rejects_final_and_intermediate_symlink_escape_and_duplicate_keys(self) -> None:
        with tempfile.TemporaryDirectory() as raw, tempfile.TemporaryDirectory() as outside_raw:
            root = Path(raw)
            outside = Path(outside_raw)
            (outside / "store.json").write_text("{}\n", encoding="utf-8")
            for link in (root / "store.json", root / "linked"):
                link.symlink_to(outside / "store.json" if link.name == "store.json" else outside)
                candidate = link if link.name == "store.json" else link / "store.json"
                result = subprocess.run(
                    [sys.executable, str(SCRIPT), "validate", "--root", str(root), "--store", str(candidate)],
                    cwd=REPO,
                    text=True,
                    capture_output=True,
                    check=False,
                )
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("without following path links", result.stderr)

            duplicate = root / "duplicate.json"
            duplicate.write_text('{"schema":"x","schema":"y"}\n', encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "validate", "--root", str(root), "--store", str(duplicate)],
                cwd=REPO,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("duplicate JSON key", result.stderr)

    def test_cli_has_no_filesystem_output_operation(self) -> None:
        source_before = tree_snapshot(REPO / "ontology" / "src")
        dist_before = tree_snapshot(REPO / "ontology" / "dist")
        result = subprocess.run(
            [
                sys.executable, str(SCRIPT), "acquire", "--root", str(FIXTURES),
                "--store", str(FIXTURES / "owner-store.json"),
                "--request", str(FIXTURES / "acquisition-request.json"),
            ],
            cwd=REPO,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), load("expected-receipts.json"))
        self.assertEqual(source_before, tree_snapshot(REPO / "ontology" / "src"))
        self.assertEqual(dist_before, tree_snapshot(REPO / "ontology" / "dist"))

    def test_fixture_contains_no_key_material_or_production_locator(self) -> None:
        raw = (FIXTURES / "owner-store.json").read_text(encoding="utf-8")
        lowered = raw.lower()
        self.assertNotIn("begin private key", lowered)
        self.assertNotIn('"private_key"', lowered)
        self.assertNotIn('"secret"', lowered)
        self.assertNotIn("https://", lowered)
        self.assertIn("local-sandbox://", lowered)


if __name__ == "__main__":
    unittest.main()
