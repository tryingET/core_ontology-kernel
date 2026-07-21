#!/usr/bin/env python3
"""Decision 53 semantic-owner sandbox record and read-receipt fixture tool.

This module is deliberately fixture-only.  It cannot read a live owner store,
use keys, mutate ontology sources, or advance a publication head.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import stat
import sys
import unicodedata
from pathlib import Path
from typing import Any

MAX_BYTES = 1_048_576
MAX_DEPTH = 32
MAX_SAFE_INTEGER = 9_007_199_254_740_991
LIVE_ACQUISITION_IMPLEMENTED = False
STORE_SCHEMA = "ontology-kernel.semantic-owner-sandbox-store.v0"
BUNDLE_SCHEMA = "ontology-kernel.semantic-owner-sandbox-receipt-bundle.v0"
OWNER_REPOSITORY = {
    "canonical_locator": "local://core/ontology-kernel",
    "identity_revision": 1,
    "owner": "semantic-owner",
    "repository_id": "ontology-kernel",
}
ISSUER = {"id": "semantic-owner", "kind": "semantic_owner"}
STORE_ID = "semantic-owner-sandbox-task-3988"
STORE_LOCATOR = "local-sandbox://core/ontology-kernel/task-3988#owner-store"
REQUIRED_ACTION_EPOCH_FLOOR = 1

ROLE_CONTRACTS = {
    "namespace_policy": (
        "semantic_lifecycle",
        "semantic-authority-semantic-lifecycle-fact.v0",
        "ontology-kernel.semantic-namespace-read-sandbox.v0",
    ),
    "compatibility_decision": (
        "semantic_lifecycle",
        "semantic-authority-semantic-lifecycle-fact.v0",
        "ontology-kernel.semantic-compatibility-read-sandbox.v0",
    ),
    "lifecycle_decision": (
        "semantic_lifecycle",
        "semantic-authority-semantic-lifecycle-fact.v0",
        "ontology-kernel.semantic-lifecycle-read-sandbox.v0",
    ),
    "trust_state": (
        "semantic_trust",
        "semantic-authority-semantic-trust-fact.v0",
        "ontology-kernel.semantic-trust-read-sandbox.v0",
    ),
    "release_approval": (
        "semantic_vote",
        "semantic-authority-semantic-vote-fact.v0",
        "ontology-kernel.semantic-approval-read-sandbox.v0",
    ),
    "publication_state": (
        "semantic_publication",
        "semantic-authority-semantic-publication-fact.v0",
        "ontology-kernel.semantic-publication-read-sandbox.v0",
    ),
}


class SandboxContractError(ValueError):
    """A fixture violates the closed sandbox contract."""


def _reject_value(value: Any, path: str = "") -> None:
    if value is None or type(value) is bool:
        return
    if type(value) is str:
        if unicodedata.normalize("NFC", value) != value:
            raise SandboxContractError(f"non-NFC string at {path or '/'}")
        if any(0xD800 <= ord(ch) <= 0xDFFF for ch in value):
            raise SandboxContractError(f"surrogate scalar at {path or '/'}")
        return
    if type(value) is int:
        if not 0 <= value <= MAX_SAFE_INTEGER:
            raise SandboxContractError(f"integer outside safe range at {path or '/'}")
        return
    if type(value) is float:
        raise SandboxContractError(f"floating-point value at {path or '/'}")
    if type(value) is list:
        for index, child in enumerate(value):
            _reject_value(child, f"{path}/{index}")
        return
    if type(value) is dict:
        for key, child in value.items():
            if type(key) is not str:
                raise SandboxContractError(f"non-string key at {path or '/'}")
            _reject_value(key, path)
            _reject_value(child, f"{path}/{key}")
        return
    raise SandboxContractError(f"unsupported JSON value at {path or '/'}")


def _depth(value: Any) -> int:
    if type(value) is dict:
        return 1 + max((_depth(item) for item in value.values()), default=0)
    if type(value) is list:
        return 1 + max((_depth(item) for item in value), default=0)
    return 0


def canonical_bytes(value: Any) -> bytes:
    """Return deterministic integer-only RFC-8785-profile bytes."""
    _reject_value(value)

    def encode(item: Any) -> str:
        if item is None:
            return "null"
        if item is True:
            return "true"
        if item is False:
            return "false"
        if type(item) is int:
            return str(item)
        if type(item) is str:
            return json.dumps(item, ensure_ascii=False, allow_nan=False, separators=(",", ":"))
        if type(item) is list:
            return "[" + ",".join(encode(child) for child in item) + "]"
        keys = sorted(item, key=lambda key: key.encode("utf-16-be"))
        return "{" + ",".join(f"{encode(key)}:{encode(item[key])}" for key in keys) + "}"

    return encode(value).encode("utf-8")


def digest(domain: str, value: Any) -> str:
    return "sha256:" + hashlib.sha256(domain.encode("ascii") + b"\0" + canonical_bytes(value)).hexdigest()


def object_digest(domain: str, value: dict[str, Any], field: str) -> str:
    preimage = copy.deepcopy(value)
    if field not in preimage:
        raise SandboxContractError(f"missing digest field {field}")
    preimage.pop(field)
    return digest(domain, preimage)


def _fixture_digest(label: str) -> str:
    return "sha256:" + hashlib.sha256(("task-3988-sandbox:" + label).encode("ascii")).hexdigest()


def _artifact(schema: str, body: dict[str, Any]) -> dict[str, Any]:
    value = {
        "schema": schema,
        "environment": "disposable_sandbox",
        "namespace": "ai-society.core.sandbox.task-3988",
        "issuer": copy.deepcopy(ISSUER),
        "owner_repository": copy.deepcopy(OWNER_REPOSITORY),
        "non_authorizing": True,
        "production_state_mutated": False,
        **body,
        "artifact_digest": "sha256:" + "0" * 64,
    }
    value["artifact_digest"] = object_digest(
        "ontology-kernel.semantic-owner-sandbox-artifact.v0", value, "artifact_digest"
    )
    return value


def build_store() -> dict[str, Any]:
    """Construct all owner-issued semantic facts in a disposable namespace."""
    artifacts = {
        "namespace_policy": _artifact(
            "ontology-kernel.semantic-namespace-policy-sandbox.v0",
            {
                "namespace_revision": 1,
                "allowed_id_prefix": "sandbox.task-3988.",
                "canonical_namespace_unchanged": True,
                "owner_predicate": {
                    "kind": "threshold",
                    "eligible_owner_ids": ["sandbox-owner-a", "sandbox-owner-b", "sandbox-owner-c"],
                    "minimum_distinct_approvals": 2,
                },
            },
        ),
        "compatibility_decision": _artifact(
            "ontology-kernel.semantic-compatibility-decision-sandbox.v0",
            {
                "decision_revision": 1,
                "candidate_id": "sandbox.task-3988.Example",
                "classification": "conditionally_compatible",
                "required_semver_effect": "minor",
                "minimum_deprecation_releases": 2,
                "identifier_reuse_override_forbidden": True,
                "evidence_digest": _fixture_digest("compatibility-evidence"),
            },
        ),
        "lifecycle_decision": _artifact(
            "ontology-kernel.semantic-lifecycle-decision-sandbox.v0",
            {
                "decision_revision": 1,
                "semantic_id": "sandbox.task-3988.Legacy",
                "history": [
                    {"revision": 1, "state": "active", "predecessor_digest": None},
                    {"revision": 2, "state": "deprecated", "predecessor_digest": _fixture_digest("lifecycle-active")},
                    {"revision": 4, "state": "removed", "predecessor_digest": _fixture_digest("lifecycle-deprecated")},
                ],
                "tombstone_permanent": True,
                "identifier_reuse_allowed": False,
            },
        ),
        "trust_state": _artifact(
            "ontology-kernel.semantic-trust-state-sandbox.v0",
            {
                "trust_revision": 2,
                "fixture_key_material_present": False,
                "active_root": {
                    "root_id": "sandbox-root",
                    "revision": 2,
                    "key_ids": ["sandbox-non-signing-key-a", "sandbox-non-signing-key-b"],
                    "prior_root_digest": _fixture_digest("trust-root-revision-1"),
                },
                "rotation": {
                    "old_root_digest": _fixture_digest("trust-root-revision-1"),
                    "new_root_digest": _fixture_digest("trust-root-revision-2"),
                    "approved": True,
                },
                "revocations": [
                    {
                        "revision": 1,
                        "target_kind": "fixture_key_id",
                        "target_digest": _fixture_digest("sandbox-revoked-key"),
                        "reason_digest": _fixture_digest("sandbox-revocation-reason"),
                    }
                ],
                "revocation_fail_closed": True,
            },
        ),
        "release_approval": _artifact(
            "ontology-kernel.semantic-release-approval-sandbox.v0",
            {
                "approval_revision": 1,
                "action": "validate_sandbox_release_candidate_only",
                "candidate_capsule_digest": _fixture_digest("sandbox-capsule"),
                "compatibility_decision_digest": _fixture_digest("sandbox-compatibility-decision"),
                "votes": [
                    {"owner_id": "sandbox-owner-a", "proof_kind": "deterministic_fixture_digest", "proof_digest": _fixture_digest("vote-a")},
                    {"owner_id": "sandbox-owner-b", "proof_kind": "deterministic_fixture_digest", "proof_digest": _fixture_digest("vote-b")},
                ],
                "threshold_satisfied": True,
                "publication_authorized": False,
            },
        ),
        "publication_state": _artifact(
            "ontology-kernel.semantic-publication-state-sandbox.v0",
            {
                "ledger_revision": 3,
                "canonical_production_head": None,
                "sandbox_head_digest": _fixture_digest("sandbox-publication-revoked"),
                "history": [
                    {"revision": 1, "status": "published", "prior_record_digest": None, "record_digest": _fixture_digest("sandbox-publication-published")},
                    {"revision": 2, "status": "withdrawn", "prior_record_digest": _fixture_digest("sandbox-publication-published"), "record_digest": _fixture_digest("sandbox-publication-withdrawn")},
                    {"revision": 3, "status": "revoked", "prior_record_digest": _fixture_digest("sandbox-publication-withdrawn"), "record_digest": _fixture_digest("sandbox-publication-revoked")},
                ],
                "cas_lineage_complete": True,
                "append_only": True,
                "publication_authorized": False,
            },
        ),
    }
    records = []
    for role in ROLE_CONTRACTS:
        category, fact_schema, contract = ROLE_CONTRACTS[role]
        artifact = artifacts[role]
        record = {
            "role": role,
            "category": category,
            "issuer": copy.deepcopy(ISSUER),
            "owner_repository": copy.deepcopy(OWNER_REPOSITORY),
            "acquisition_contract": contract,
            "fact_schema": fact_schema,
            "artifact": artifact,
            "artifact_digest": artifact["artifact_digest"],
            "record_digest": "sha256:" + "0" * 64,
        }
        record["record_digest"] = object_digest(
            "ontology-kernel.semantic-owner-sandbox-record.v0", record, "record_digest"
        )
        records.append(record)
    store = {
        "schema": STORE_SCHEMA,
        "sandbox_only": True,
        "live_acquisition_implemented": LIVE_ACQUISITION_IMPLEMENTED,
        "owner_repository": copy.deepcopy(OWNER_REPOSITORY),
        "issuer": copy.deepcopy(ISSUER),
        "store_id": STORE_ID,
        "canonical_store_locator": STORE_LOCATOR,
        "store_revision": 1,
        "records": records,
        "store_head_digest": "sha256:" + "0" * 64,
    }
    store["store_head_digest"] = object_digest(
        "ontology-kernel.semantic-owner-sandbox-store.v0", store, "store_head_digest"
    )
    return store


def build_request() -> dict[str, Any]:
    return {
        "schema": "ontology-kernel.semantic-owner-sandbox-read-request.v0",
        "action_epoch": 1,
        "required_action_epoch_floor": REQUIRED_ACTION_EPOCH_FLOOR,
        "roles": list(ROLE_CONTRACTS),
    }


def _expect_keys(value: dict[str, Any], expected: set[str], path: str) -> None:
    if set(value) != expected:
        missing = sorted(expected - set(value))
        extra = sorted(set(value) - expected)
        raise SandboxContractError(f"closed fields mismatch at {path}: missing={missing}, extra={extra}")


def validate_store(store: Any) -> dict[str, Any]:
    _reject_value(store)
    if _depth(store) > MAX_DEPTH or type(store) is not dict:
        raise SandboxContractError("store must be a bounded object")
    _expect_keys(store, {
        "schema", "sandbox_only", "live_acquisition_implemented", "owner_repository", "issuer",
        "store_id", "canonical_store_locator", "store_revision", "records", "store_head_digest",
    }, "/")
    if store["schema"] != STORE_SCHEMA or store["sandbox_only"] is not True:
        raise SandboxContractError("store is not the task-3988 sandbox contract")
    if store["live_acquisition_implemented"] is not False:
        raise SandboxContractError("live acquisition must remain false")
    if store["owner_repository"] != OWNER_REPOSITORY or store["issuer"] != ISSUER:
        raise SandboxContractError("semantic-owner facts must be issued only by ontology-kernel")
    if store["store_id"] != STORE_ID or store["canonical_store_locator"] != STORE_LOCATOR:
        raise SandboxContractError("sandbox store identity drift")
    if type(store["store_revision"]) is not int or store["store_revision"] < 1:
        raise SandboxContractError("invalid store revision")
    records = store["records"]
    if type(records) is not list or len(records) != len(ROLE_CONTRACTS):
        raise SandboxContractError("store must contain exactly one record per owner role")
    seen = set()
    for index, record in enumerate(records):
        path = f"/records/{index}"
        if type(record) is not dict:
            raise SandboxContractError(f"record is not an object at {path}")
        _expect_keys(record, {
            "role", "category", "issuer", "owner_repository", "acquisition_contract",
            "fact_schema", "artifact", "artifact_digest", "record_digest",
        }, path)
        role = record["role"]
        if role not in ROLE_CONTRACTS or role in seen:
            raise SandboxContractError(f"unknown or duplicate role at {path}")
        seen.add(role)
        category, fact_schema, contract = ROLE_CONTRACTS[role]
        if (record["category"], record["fact_schema"], record["acquisition_contract"]) != (category, fact_schema, contract):
            raise SandboxContractError(f"role contract drift at {path}")
        if record["issuer"] != ISSUER or record["owner_repository"] != OWNER_REPOSITORY:
            raise SandboxContractError(f"foreign semantic-owner issuer at {path}")
        artifact = record["artifact"]
        if type(artifact) is not dict:
            raise SandboxContractError(f"artifact is not an object at {path}")
        required_artifact = {
            "environment": "disposable_sandbox",
            "namespace": "ai-society.core.sandbox.task-3988",
            "issuer": ISSUER,
            "owner_repository": OWNER_REPOSITORY,
            "non_authorizing": True,
            "production_state_mutated": False,
        }
        if any(artifact.get(key) != value for key, value in required_artifact.items()):
            raise SandboxContractError(f"artifact escaped sandbox at {path}")
        expected_artifact_digest = object_digest(
            "ontology-kernel.semantic-owner-sandbox-artifact.v0", artifact, "artifact_digest"
        )
        if artifact.get("artifact_digest") != expected_artifact_digest or record["artifact_digest"] != expected_artifact_digest:
            raise SandboxContractError(f"artifact digest mismatch at {path}")
        if record["record_digest"] != object_digest(
            "ontology-kernel.semantic-owner-sandbox-record.v0", record, "record_digest"
        ):
            raise SandboxContractError(f"record digest mismatch at {path}")
    if seen != set(ROLE_CONTRACTS):
        raise SandboxContractError("owner role coverage is incomplete")
    if store["store_head_digest"] != object_digest(
        "ontology-kernel.semantic-owner-sandbox-store.v0", store, "store_head_digest"
    ):
        raise SandboxContractError("store head digest mismatch")
    # This is a closed fixture contract, not a generic owner-store validator.
    # Exact equality prevents a caller from adding self-consistent production
    # authority fields and merely recomputing the unkeyed fixture digests.
    if canonical_bytes(store) != canonical_bytes(build_store()):
        raise SandboxContractError("store differs from the closed owner-issued sandbox fixture")
    return store


def validate_request(request: Any) -> dict[str, Any]:
    if type(request) is not dict:
        raise SandboxContractError("request must be an object")
    _expect_keys(request, {"schema", "action_epoch", "required_action_epoch_floor", "roles"}, "/request")
    if request["schema"] != "ontology-kernel.semantic-owner-sandbox-read-request.v0":
        raise SandboxContractError("request schema drift")
    if (
        type(request["required_action_epoch_floor"]) is not int
        or request["required_action_epoch_floor"] != REQUIRED_ACTION_EPOCH_FLOOR
    ):
        raise SandboxContractError("request action epoch floor drift")
    if type(request["action_epoch"]) is not int or request["action_epoch"] < REQUIRED_ACTION_EPOCH_FLOOR:
        raise SandboxContractError("stale request action epoch")
    roles = request["roles"]
    if type(roles) is not list or not roles or len(roles) != len(set(roles)):
        raise SandboxContractError("request roles must be nonempty and unique")
    if any(type(role) is not str or role not in ROLE_CONTRACTS for role in roles):
        raise SandboxContractError("request contains an unknown role")
    if canonical_bytes(request) != canonical_bytes(build_request()):
        raise SandboxContractError("request differs from the closed fixture epoch and role set")
    return request


def _capability_parts(record: dict[str, Any]) -> tuple[str, str, str]:
    contract_digest = digest("semantic-release.raw-blob.v0", record["acquisition_contract"])
    distribution_digest = digest(
        "semantic-release.raw-blob.v0",
        f"sandbox-distribution:{record['acquisition_contract']}:{OWNER_REPOSITORY['repository_id']}",
    )
    capability = {
        "owner_surface": "semantic_owner",
        "owner_repository": copy.deepcopy(OWNER_REPOSITORY),
        "acquisition_contract": record["acquisition_contract"],
        "acquisition_contract_digest": contract_digest,
        "acquisition_distribution_digest": distribution_digest,
    }
    capability_digest = digest("semantic-release.owner-acquisition-capability.v0", capability)
    return contract_digest, distribution_digest, capability_digest


def _pin_and_receipt(store: dict[str, Any], request: dict[str, Any], record: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any]]:
    role = record["role"]
    category = record["category"]
    fact_value = {"kind": "digest", "value": record["artifact_digest"]}
    fact = {"fact_schema": record["fact_schema"], "fact_value": fact_value}
    fact_digest = digest("semantic-release.authority-fact.v0", fact)
    contract_digest, distribution_digest, capability_digest = _capability_parts(record)
    common = {
        "role": role,
        "category": category,
        "owner_repository": copy.deepcopy(OWNER_REPOSITORY),
        "acquisition_contract": record["acquisition_contract"],
        "acquisition_contract_digest": contract_digest,
        "acquisition_distribution_digest": distribution_digest,
        "store_id": store["store_id"],
        "canonical_store_locator": store["canonical_store_locator"],
        "store_head_digest": store["store_head_digest"],
        "store_revision": store["store_revision"],
        "revocation_head_digest": next(
            item["artifact_digest"] for item in store["records"] if item["role"] == "trust_state"
        ),
        "fact_schema": record["fact_schema"],
        "fact_value": fact_value,
        "fact_digest": fact_digest,
        "required_action_epoch_floor": request["required_action_epoch_floor"],
        "acquisition_capability_digest": capability_digest,
    }
    freshness = {
        key: common[key]
        for key in (
            "role", "category", "owner_repository", "acquisition_contract",
            "acquisition_contract_digest", "acquisition_distribution_digest", "store_id",
            "canonical_store_locator", "store_head_digest", "store_revision",
            "revocation_head_digest", "fact_schema", "fact_digest", "required_action_epoch_floor",
        )
    }
    freshness["owner_surface"] = "semantic_owner"
    freshness["owner_id"] = "semantic-owner"
    freshness["action_epoch"] = request["action_epoch"]
    freshness_digest = digest("semantic-release.owner-store-freshness-cas.v0", freshness)
    pin = {
        "schema": "semantic-owner-acquisition-capability-pin.v0",
        "capability_pin_id": f"sandbox-pin:task-3988:{role}",
        **common,
        "owner_surface": "semantic_owner",
        "owner_id": "semantic-owner",
        "freshness_cas_token_digest": freshness_digest,
        "capability_pin_digest": "sha256:" + "0" * 64,
    }
    pin["capability_pin_digest"] = object_digest(
        "semantic-release.owner-acquisition-capability-pin.v0", pin, "capability_pin_digest"
    )
    receipt = {
        "schema": "semantic-owner-store-read-receipt.v0",
        "observation_id": f"sandbox-receipt:task-3988:{role}",
        **common,
        "issuer": copy.deepcopy(ISSUER),
        "claim_scope": "owner_store_read_only",
        "capability_pin_id": pin["capability_pin_id"],
        "capability_pin_digest": pin["capability_pin_digest"],
        "freshness_cas_token_digest": freshness_digest,
        "action_epoch": request["action_epoch"],
        "owner_store_read_receipt_digest": "sha256:" + "0" * 64,
    }
    receipt["owner_store_read_receipt_digest"] = object_digest(
        "semantic-release.owner-store-read-receipt.v0", receipt, "owner_store_read_receipt_digest"
    )
    return pin, receipt


def acquire(store: Any, request: Any) -> dict[str, Any]:
    checked_store = validate_store(store)
    checked_request = validate_request(request)
    by_role = {record["role"]: record for record in checked_store["records"]}
    pins, receipts = [], []
    for role in checked_request["roles"]:
        pin, receipt = _pin_and_receipt(checked_store, checked_request, by_role[role])
        pins.append(pin)
        receipts.append(receipt)
    bundle = {
        "schema": BUNDLE_SCHEMA,
        "sandbox_only": True,
        "live_acquisition_implemented": False,
        "owner_repository": copy.deepcopy(OWNER_REPOSITORY),
        "store_head_digest": checked_store["store_head_digest"],
        "action_epoch": checked_request["action_epoch"],
        "pins": pins,
        "receipts": receipts,
        "bundle_digest": "sha256:" + "0" * 64,
    }
    bundle["bundle_digest"] = object_digest(
        "ontology-kernel.semantic-owner-sandbox-receipt-bundle.v0", bundle, "bundle_digest"
    )
    return bundle


def validate_bundle(bundle: Any, store: Any, request: Any) -> dict[str, Any]:
    _reject_value(bundle)
    if type(bundle) is not dict or _depth(bundle) > MAX_DEPTH:
        raise SandboxContractError("receipt bundle must be a bounded object")
    expected = acquire(store, request)
    # Canonical byte equality is deliberately type-aware. Python object
    # equality treats True == 1, which would otherwise permit boolean drift in
    # action epochs, store revisions, or other integer receipt fields.
    if canonical_bytes(bundle) != canonical_bytes(expected):
        raise SandboxContractError("receipt bundle does not replay from the owner store and request")
    return expected


def pretty_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, allow_nan=False, indent=2, sort_keys=True) + "\n"


def fixture_values() -> dict[str, Any]:
    store = build_store()
    request = build_request()
    return {
        "owner-store.json": store,
        "acquisition-request.json": request,
        "expected-receipts.json": acquire(store, request),
    }


def _checked_root(root: Path) -> Path:
    lexical = Path(os.path.abspath(root))
    try:
        info = lexical.lstat()
    except OSError as exc:
        raise SandboxContractError(f"cannot stat declared root: {lexical}") from exc
    if stat.S_ISLNK(info.st_mode) or not stat.S_ISDIR(info.st_mode):
        raise SandboxContractError(f"declared root must be a real directory: {lexical}")
    try:
        resolved = lexical.resolve(strict=True)
    except OSError as exc:
        raise SandboxContractError(f"cannot resolve declared root: {lexical}") from exc
    if resolved != lexical:
        raise SandboxContractError(f"declared root contains a symlink component: {lexical}")
    return lexical


def _read_bounded_file(path: Path, root: Path) -> bytes:
    root = _checked_root(root)
    lexical = Path(os.path.abspath(path))
    try:
        relative = lexical.relative_to(root)
    except ValueError as exc:
        raise SandboxContractError(f"input escapes declared root: {lexical}") from exc
    if not relative.parts:
        raise SandboxContractError("input path names the root directory")
    directory_flags = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_NOFOLLOW", 0)
    file_flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0)
    descriptors: list[int] = []
    try:
        current = os.open(root, directory_flags)
        descriptors.append(current)
        for component in relative.parts[:-1]:
            current = os.open(component, directory_flags, dir_fd=current)
            descriptors.append(current)
        descriptor = os.open(relative.parts[-1], file_flags, dir_fd=current)
        descriptors.append(descriptor)
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            raise SandboxContractError(f"input must be a regular no-follow file: {lexical}")
        chunks, total = [], 0
        while True:
            chunk = os.read(descriptor, min(65_536, MAX_BYTES + 1 - total))
            if not chunk:
                break
            chunks.append(chunk)
            total += len(chunk)
            if total > MAX_BYTES:
                raise SandboxContractError(f"input exceeds {MAX_BYTES} bytes: {lexical}")
        return b"".join(chunks)
    except SandboxContractError:
        raise
    except OSError as exc:
        raise SandboxContractError(f"cannot read input without following path links: {lexical}") from exc
    finally:
        for descriptor in reversed(descriptors):
            try:
                os.close(descriptor)
            except OSError:
                pass


def _load_json(path: Path, *, root: Path) -> Any:
    raw = _read_bounded_file(path, root)
    try:
        text = raw.decode("utf-8", "strict")
    except UnicodeDecodeError as exc:
        raise SandboxContractError(f"input is not UTF-8: {path}") from exc

    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        result = {}
        for key, value in items:
            if key in result:
                raise SandboxContractError(f"duplicate JSON key in {path}: {key}")
            result[key] = value
        return result

    try:
        value = json.loads(
            text,
            object_pairs_hook=pairs,
            parse_float=lambda token: (_ for _ in ()).throw(SandboxContractError(f"float token in {path}: {token}")),
            parse_constant=lambda token: (_ for _ in ()).throw(SandboxContractError(f"constant token in {path}: {token}")),
        )
    except json.JSONDecodeError as exc:
        raise SandboxContractError(f"invalid JSON input: {path}") from exc
    _reject_value(value)
    if _depth(value) > MAX_DEPTH:
        raise SandboxContractError(f"input exceeds depth limit: {path}")
    return value


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    generate = sub.add_parser("generate", help="emit a deterministic fixture value to stdout")
    generate.add_argument(
        "--kind", required=True,
        choices=("owner-store.json", "acquisition-request.json", "expected-receipts.json", "package"),
    )
    validate = sub.add_parser("validate", help="validate one closed sandbox owner store")
    validate.add_argument("--store", type=Path, required=True)
    validate.add_argument("--root", type=Path, required=True)
    acquire_parser = sub.add_parser("acquire", help="emit replayed read-only fixture receipts to stdout")
    acquire_parser.add_argument("--store", type=Path, required=True)
    acquire_parser.add_argument("--request", type=Path, required=True)
    acquire_parser.add_argument("--root", type=Path, required=True)
    replay = sub.add_parser("replay", help="verify a committed receipt bundle")
    replay.add_argument("--store", type=Path, required=True)
    replay.add_argument("--request", type=Path, required=True)
    replay.add_argument("--receipts", type=Path, required=True)
    replay.add_argument("--root", type=Path, required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.command == "generate":
            values = fixture_values()
            value = values if args.kind == "package" else values[args.kind]
            sys.stdout.write(pretty_json(value))
            return 0
        store = _load_json(args.store, root=args.root)
        if args.command == "validate":
            validate_store(store)
            print("semantic-owner sandbox store: OK")
            return 0
        request = _load_json(args.request, root=args.root)
        if args.command == "acquire":
            sys.stdout.write(pretty_json(acquire(store, request)))
            return 0
        receipts = _load_json(args.receipts, root=args.root)
        validate_bundle(receipts, store, request)
        print("semantic-owner sandbox receipt replay: OK")
        return 0
    except (OSError, SandboxContractError) as exc:
        print(f"semantic-owner sandbox: ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
