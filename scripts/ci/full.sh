#!/usr/bin/env bash
set -euo pipefail
# Sanitize lookup before invoking even basic helper commands.
export PATH="/usr/local/bin:/usr/bin:/bin"
unset PYTHONPATH
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
repo="$(cd -- "$script_dir/../.." && pwd -P)"
if [[ -n "${ROCS_REPO:-}" ]]; then
  supplied_repo="$(cd -- "$ROCS_REPO" 2>/dev/null && pwd -P)" || {
    echo "ROCS_REPO does not resolve to this checkout" >&2
    exit 2
  }
  if [[ "$supplied_repo" != "$repo" ]]; then
    echo "ROCS_REPO must identify this checkout: $repo" >&2
    exit 2
  fi
fi
export ROCS_REPO="$repo"
artifact="$repo/tools/rocs-cli"
python_bin=""
if command -v python3.12 >/dev/null 2>&1; then
  python_bin="$(command -v python3.12)"
elif command -v uv >/dev/null 2>&1; then
  python_bin="$(uv python find --no-project 3.12 2>/dev/null || true)"
fi
if [[ -z "$python_bin" || ! -x "$python_bin" ]]; then
  echo "ROCS validation requires an installed Python 3.12 interpreter" >&2
  exit 2
fi
"$python_bin" -I -S -B - <<'PY'
import sys
if sys.version_info[:2] != (3, 12):
    raise SystemExit("ROCS validation requires Python 3.12.x")
PY
export ROCS_WORKSPACE_ROOT="${ROCS_WORKSPACE_ROOT:-$repo}"
export PYTHONDONTWRITEBYTECODE=1

# Keep the cross-owner handoff observation contract executable in the full gate.
"$python_bin" -I -S -B "$repo/tests/test_verify_commit_handoff.py"

# Verify with the standard library before importing or executing any bundled byte.
"$python_bin" -I -S -B - "$artifact" <<'PY'
import hashlib, json, os, stat, sys
from pathlib import Path
root = Path(sys.argv[1]).resolve(strict=True)
lock = root / "VENDORED_HASHES.json"
trusted_lock_digest = "c7bf413cc0edb5fec30eb5aadfa5bc2f30c366a36b8aa392936be821a5912ad7"
try:
    lock_bytes = lock.read_bytes()
    if hashlib.sha256(lock_bytes).hexdigest() != trusted_lock_digest:
        raise ValueError("lock digest does not match generated trust anchor")
    payload = json.loads(lock_bytes)
    expected = payload["files"]
except Exception as exc:
    raise SystemExit(f"ROCS bundled runtime lock invalid: {exc}")
actual = {}
for path in sorted(root.rglob("*")):
    if path == lock:
        continue
    mode = path.lstat().st_mode
    if stat.S_ISLNK(mode) or (not stat.S_ISREG(mode) and not stat.S_ISDIR(mode)):
        raise SystemExit(f"ROCS bundled runtime has invalid file type: {path.relative_to(root)}")
    if stat.S_ISREG(mode):
        actual[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
if actual != expected:
    raise SystemExit("ROCS bundled runtime verification failed closed")
PY
rocs=("$python_bin" -I -S -B "$artifact/rocs.py")
profile="${ROCS_CI_PROFILE:-local-dev}"
case "$profile" in
  local-dev) resolve=(--only path) ;;
  main-strict|branch-ci) resolve=(--resolve-refs --workspace-ref-mode strict) ;;
  *) echo "unknown ROCS_CI_PROFILE: $profile" >&2; exit 2 ;;
esac
"${rocs[@]}" cleanup --repo "$repo"
"${rocs[@]}" validate --repo "$repo" --json "${resolve[@]}"
"${rocs[@]}" build --repo "$repo" --json "${resolve[@]}"
"${rocs[@]}" vendored-check --vendored-dir "$artifact"
"${rocs[@]}" summary --repo "$repo" --profile kernel-v1 --json "${resolve[@]}"
"${rocs[@]}" lint --repo "$repo" --profile kernel-v1 --json "${resolve[@]}"
"${rocs[@]}" graph --repo "$repo" --profile kernel-v1 --json "${resolve[@]}"
"${rocs[@]}" check-inverses --repo "$repo" --profile kernel-v1 --json "${resolve[@]}"
"${rocs[@]}" normalize --repo "$repo" --profile kernel-v1
"${rocs[@]}" pack core.Agent --repo "$repo" --profile kernel-v1 --json "${resolve[@]}"

scratch_root="${TMPDIR:-$(dirname -- "$repo")}"
mkdir -p "$scratch_root"
gate_tmp="$(mktemp -d "$scratch_root/rocs-kernel-gate.XXXXXX")"
trap 'rm -rf -- "$gate_tmp"' EXIT
# Raw SHA-256 of the exact verified VENDORED_HASHES.json bytes. This is only
# non-authoritative prepared-runtime invocation metadata.
manifest_digest="sha256:c7bf413cc0edb5fec30eb5aadfa5bc2f30c366a36b8aa392936be821a5912ad7"
"${rocs[@]}" discover \
  --repo "$repo" \
  --request-file "$repo/tests/fixtures/semantic-discovery-request.v0.json" \
  --tool-kind development_runtime \
  --tool-manifest-digest "$manifest_digest" \
  --json --no-index-cache --no-env-file \
  > "$gate_tmp/discover.json"
read -r snapshot_digest document_digest < <(
  "$python_bin" -I -S -B - "$gate_tmp/discover.json" <<'PY'
import json, sys
payload = json.load(open(sys.argv[1], encoding="utf-8"))
candidates = payload.get("candidates")
if payload.get("retrieval") != "multiple_candidates" or payload.get("truncated") is not False:
    raise SystemExit("expected complete multiple-candidate discovery")
if not isinstance(candidates, list) or len(candidates) != 2:
    raise SystemExit("expected exactly two discovery candidates")
identities = [(candidate.get("ont_id"), candidate.get("kind")) for candidate in candidates]
expected = {("core.Agent", "concept"), ("core.Authority", "concept")}
if len(set(identities)) != len(identities) or set(identities) != expected:
    raise SystemExit("expected exact core.Agent and core.Authority discovery candidates")
candidate = next(candidate for candidate in candidates if candidate.get("ont_id") == "core.Agent")
print(payload["corpus_snapshot_digest"], candidate["document_digest"])
PY
)
"${rocs[@]}" pack core.Agent \
  --repo "$repo" --profile kernel-v1 --json \
  --expected-snapshot-digest "$snapshot_digest" \
  --expected-document-digest "$document_digest" \
  --no-index-cache --no-env-file \
  > "$gate_tmp/bound-pack.json"

# Exercise semantic routing only with conspicuously synthetic, disposable
# policy/provenance authority. This creates no kernel or Decision 53 fact.
command -v /usr/bin/git >/dev/null 2>&1 || {
  echo "ROCS route acceptance requires /usr/bin/git" >&2
  exit 2
}
owner_root="$gate_tmp/synthetic-owner"
policy_root="$gate_tmp/synthetic-policy"
mkdir -p "$owner_root" "$policy_root"
printf '%s\n' 'conspicuously synthetic kernel route authority' > "$owner_root/authority.txt"
printf '%s\n' 'conspicuously synthetic kernel route provenance' > "$owner_root/record.txt"
git_env=(
  env -i PATH=/usr/bin:/bin HOME=/nonexistent LANG=C LC_ALL=C
  GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null
  GIT_AUTHOR_NAME='Synthetic kernel gate' GIT_AUTHOR_EMAIL=kernel-gate@example.invalid
  GIT_COMMITTER_NAME='Synthetic kernel gate' GIT_COMMITTER_EMAIL=kernel-gate@example.invalid
  GIT_AUTHOR_DATE=2026-08-01T00:00:00Z GIT_COMMITTER_DATE=2026-08-01T00:00:00Z
)
"${git_env[@]}" /usr/bin/git -C "$owner_root" init -q
"${git_env[@]}" /usr/bin/git -C "$owner_root" add authority.txt record.txt
"${git_env[@]}" /usr/bin/git -C "$owner_root" commit -q -m 'synthetic route authority'
owner_revision="$("${git_env[@]}" /usr/bin/git -C "$owner_root" rev-parse HEAD)"
"$python_bin" -I -S -B - \
  "$artifact" "$owner_root" "$owner_revision" "$policy_root" <<'PY'
import hashlib, json, sys
from pathlib import Path
artifact, owner, revision, policy_root = map(Path, sys.argv[1:])
sys.path.insert(0, str(artifact / "src"))
from rocs_cli.semantic_router_protocol import jcs_bytes, object_digest

def digest(raw: bytes) -> str:
    return "sha256:" + hashlib.sha256(raw).hexdigest()

authority_raw = (owner / "authority.txt").read_bytes()
record_raw = (owner / "record.txt").read_bytes()
revision_text = revision.as_posix()
record_common = {
    "author": "synthetic-kernel-gate",
    "b0_exposure": "confirmed",
    "contamination_scan_receipt": "sha256:" + "a" * 64,
    "created_at": "2026-08-01T00:00:00Z",
    "development_case_ids": ["SYNTHETIC_KERNEL_GATE"],
    "kind": "token",
    "review_ref": "synthetic-kernel-gate-review",
    "source_content_digest": digest(record_raw),
    "source_owner_repo": "synthetic-kernel-gate-owner",
    "source_path": "record.txt",
    "source_revision": revision_text,
}
provenance = {
    "schema": "semantic-routing-provenance.v0",
    "policy_id": "synthetic-kernel-gate",
    "policy_owner_repo": "synthetic-kernel-gate-owner",
    "policy_revision": revision_text,
    "policy_path": "authority.txt",
    "policy_source_content_digest": digest(authority_raw),
    "records": [
        {**record_common, "clause_id": "concept.agent", "group_id": "group.agent", "value": "agent"},
        {**record_common, "clause_id": "domain.authority", "group_id": "group.authority", "value": "authority"},
    ],
}
provenance["provenance_manifest_digest"] = object_digest("provenance_manifest", provenance)
policy = {
    "schema": "semantic-routing-policy.v0",
    "policy_id": "synthetic-kernel-gate",
    "unicode_data": "15.0.0",
    "normalization": "nfkc-casefold-ws-v0",
    "tokenization": "unicode-ln-sequence-v0",
    "authority": {
        "owner_repo": "synthetic-kernel-gate-owner",
        "revision": revision_text,
        "path": "authority.txt",
        "source_content_digest": digest(authority_raw),
        "review_ref": "synthetic-kernel-gate-review",
    },
    "provenance_manifest_digest": provenance["provenance_manifest_digest"],
    "domain": {
        "domain_id": "synthetic-kernel-gate-domain",
        "admit_any": [{"clause_id": "domain.authority", "all_of": [{"group_id": "group.authority", "any_of": [{"kind": "token", "value": "authority"}]}]}],
        "exclude_any": [],
    },
    "concepts": [{
        "ont_id": "core.Agent",
        "support_any": [{"clause_id": "concept.agent", "all_of": [{"group_id": "group.agent", "any_of": [{"kind": "token", "value": "agent"}]}]}],
        "exclude_any": [],
    }],
    "joint_routes": [],
}
policy["routing_policy_digest"] = object_digest("routing_policy", policy)
request = {
    "schema": "semantic-route-request.v0",
    "query": "agent authority",
    "identity_selector": {"kind": "development_snapshot"},
    "profile": "kernel-v1",
    "router_algorithm": "rocs-symbolic-router-v0",
    "candidate_algorithm": "rocs-lexical-v0",
    "expected_routing_policy_digest": policy["routing_policy_digest"],
    "expected_provenance_manifest_digest": provenance["provenance_manifest_digest"],
    "discovery_limits": {"query_bytes": 16384, "corpus_files": 5000, "corpus_bytes": 33554432, "file_bytes": 1048576, "parser_depth": 32, "collection_items": 10000, "candidates": 12, "result_bytes": 65536},
    "route_limits": {"policy_bytes": 1048576, "provenance_bytes": 8388608, "concepts": 1000, "clauses": 4096, "groups_per_clause": 8, "alternatives_per_group": 16, "total_alternatives": 16384, "normalized_alternative_bytes": 524288, "joint_routes": 1000, "evidence_entries": 2048, "witnesses": 8192, "matching_work": 2000000, "result_bytes": 262144, "parser_depth": 32, "collection_items": 20000},
}
(policy_root / "policy.json").write_bytes(jcs_bytes(policy))
(policy_root / "provenance.json").write_bytes(jcs_bytes(provenance))
(policy_root / "request.json").write_bytes(jcs_bytes(request))
PY
"${rocs[@]}" route \
  --repo "$repo" \
  --policy-owner-repo-id synthetic-kernel-gate-owner \
  --policy-owner-repo-root "$owner_root" \
  --routing-policy-root "$policy_root" \
  --routing-policy policy.json \
  --routing-provenance provenance.json \
  --request-json - \
  --tool-kind development_runtime \
  --tool-manifest-digest "$manifest_digest" \
  --json --no-index-cache --no-env-file \
  < "$policy_root/request.json" > "$gate_tmp/route.json"
"$python_bin" -I -S -B - "$gate_tmp/route.json" <<'PY'
import json, sys
payload = json.load(open(sys.argv[1], encoding="utf-8"))
if payload.get("admission", {}).get("state") != "admitted":
    raise SystemExit("expected synthetic route admission")
routing = payload.get("routing", {})
if routing.get("state") != "single" or routing.get("selected_ont_ids") != ["core.Agent"]:
    raise SystemExit("expected synthetic route to select only core.Agent")
PY

# Exercise the generated hook against a disposable probe entrypoint. Hook
# activation in the real checkout remains an explicit operator action.
hook_root="$gate_tmp/hook-probe"
mkdir -p "$hook_root/.githooks" "$hook_root/scripts/ci"
cp "$repo/.githooks/pre-push" "$hook_root/.githooks/pre-push"
cat > "$hook_root/scripts/ci/full.sh" <<'SH'
#!/bin/sh
set -eu
[ "$PWD" = "$HOOK_PROBE_ROOT" ]
[ "$ROCS_REPO" = "$HOOK_PROBE_ROOT" ]
[ "$ROCS_CI_PROFILE" = "local-dev" ]
printf '%s\n' generated-hook-ok > "$HOOK_PROBE_RECEIPT"
SH
chmod +x "$hook_root/scripts/ci/full.sh"
env -u ROCS_REPO -u ROCS_CI_PROFILE \
  HOOK_PROBE_ROOT="$hook_root" HOOK_PROBE_RECEIPT="$gate_tmp/hook.receipt" \
  "$hook_root/.githooks/pre-push"
grep -Fx 'generated-hook-ok' "$gate_tmp/hook.receipt" >/dev/null
