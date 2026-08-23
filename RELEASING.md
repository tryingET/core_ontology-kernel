# Releasing `ontology-kernel`

Goal: stable, reproducible meaning.

## Release contract

- OIDs are durable content identities. Release tag refs must be protected against update and
  deletion under current, recorded, owner-accepted server controls; do not describe a Git ref as
  permanently immutable.
- All dependent manifests must pin the protected release tag; the full commit OID remains the
  durable handoff identity (avoid `@main`).
- Cross-owner Git handoffs must name a full commit OID and an exact `refs/heads/*` or
  `refs/tags/*` transport ref. Verify the live observation from the receiving checkout:
  ```bash
  set -euo pipefail
  python3 scripts/verify_commit_handoff.py \
    --repo . --remote "${REMOTE_URL:?set exact remote URL}" \
    --ref "${HANDOFF_REF:?set fully qualified ref}" \
    --commit "${HANDOFF_COMMIT:?set full commit OID}"
  ```
  The ref and remote URL are transport inputs, not authority. Remote aliases are not authority.
  The verifier permits SSH, HTTPS without embedded credentials, and local paths used by tests; it
  rejects plaintext HTTP/Git transport. A successful observation does not establish semantic
  release, publication authority, adoption, or AK evidence.
- Kernel changes are PR-only; no silent redefines.
- Meaning change = new `ont.id` + mark old one deprecated + decision reference.

## `v0.2.0` destinations

The complete intended release destination set is exactly:

1. `https://github.com/tryingET/ontology-kernel.git`
2. `https://github.com/tryingET/core_ontology-kernel.git`

NAS is not required for `v0.2.0` and is not a release destination. Do not infer, add, replace, or
skip a destination from configured remote aliases; aliases are convenience only, not authority.

## AK 4881 PR sequencing and review-branch publication

Do not publish the review branch or open the AK 4881 PR until AK supplies the reviewed full
`CANDIDATE_OID`. Run this once from its exact checkout. It binds local `HEAD` to that external
identity, proves the assessment base is in live `origin/main`, binds the live merge base and exact
three-path PR surface, proves the exact review ref absent, makes one non-force exact-OID push, and
then verifies the live review ref before PR creation:

```bash
set -euo pipefail

origin_url="https://github.com/tryingET/ontology-kernel.git"
assessment_base="3e6c9f39c8cecc5feb509ead2022361d3c5f3ec1"
candidate_ref="refs/heads/release/ontology-kernel-v0.2.0-prep"
candidate_oid="${CANDIDATE_OID:?AK must supply the reviewed full candidate OID}"
[[ "$candidate_oid" =~ ^[0-9a-f]{40}$ ]]
test "$(git rev-parse --verify 'HEAD^{commit}')" = "$candidate_oid"

if main_output=$(git ls-remote --exit-code "$origin_url" refs/heads/main 2>&1); then
  main_rc=0
else
  main_rc=$?
fi
case "$main_rc" in
  0) ;;
  2) printf 'live refs/heads/main is absent\n' >&2; exit 1 ;;
  *) printf 'live main lookup failed (transport/auth), rc=%s: %s\n' \
       "$main_rc" "$main_output" >&2; exit 1 ;;
esac
mapfile -t main_lines <<<"$main_output"
test "${#main_lines[@]}" -eq 1
IFS=$'\t' read -r live_main_oid live_main_ref extra <<<"${main_lines[0]}"
test "$live_main_ref" = refs/heads/main
test -z "${extra:-}"
[[ "$live_main_oid" =~ ^[0-9a-f]{40}$ ]]
expected_main_line="${live_main_oid}"$'\t'"refs/heads/main"
test "${main_lines[0]}" = "$expected_main_line"

git fetch --no-tags --no-write-fetch-head "$origin_url" "$live_main_oid"
git cat-file -e "${live_main_oid}^{commit}"
git merge-base --is-ancestor "$assessment_base" "$live_main_oid"
live_merge_base=$(git merge-base "$live_main_oid" "$candidate_oid")
test "$live_merge_base" = "$assessment_base"

expected_paths=(
  "RELEASING.md"
  "docs/project/2026-08-23-ontology-kernel-v0.2.0-release-preparation.md"
  "ontology/manifest.yaml"
)
diff_output=$(git diff --name-only "$live_main_oid...$candidate_oid")
mapfile -t actual_paths <<<"$diff_output"
test "${#actual_paths[@]}" -eq "${#expected_paths[@]}"
for i in "${!expected_paths[@]}"; do
  test "${actual_paths[$i]}" = "${expected_paths[$i]}"
done

if branch_output=$(git ls-remote --exit-code "$origin_url" "$candidate_ref" 2>&1); then
  branch_rc=0
else
  branch_rc=$?
fi
case "$branch_rc" in
  2) ;;
  0) printf 'review branch already exists: %s\n' "$branch_output" >&2; exit 1 ;;
  *) printf 'review branch absence lookup failed, rc=%s: %s\n' \
       "$branch_rc" "$branch_output" >&2; exit 1 ;;
esac

if git push "$origin_url" "${candidate_oid}:${candidate_ref}"; then
  push_rc=0
else
  push_rc=$?
fi
if live_branch_output=$(git ls-remote --exit-code "$origin_url" "$candidate_ref" 2>&1); then
  live_branch_rc=0
else
  live_branch_rc=$?
fi
case "$live_branch_rc" in
  0) ;;
  2) printf 'review branch absent after push attempt\n' >&2; exit 1 ;;
  *) printf 'review branch verification unavailable, rc=%s: %s\n' \
       "$live_branch_rc" "$live_branch_output" >&2; exit 1 ;;
esac
test "$push_rc" -eq 0
mapfile -t live_branch_lines <<<"$live_branch_output"
test "${#live_branch_lines[@]}" -eq 1
expected_branch_line="${candidate_oid}"$'\t'"${candidate_ref}"
test "${live_branch_lines[0]}" = "$expected_branch_line"
```

Only that exact non-force push is permitted; do not retry it automatically. Create the PR only
after every assertion passes. Absent, mismatched, duplicate, or unavailable live output stops the
sequence. Any earlier failure also stops for revised authority: do not silently rebase or amend,
because that would change the AK-reviewed candidate identity.

## `v0.2.0` fail-closed preflight

After the reviewed candidate has merged to `main`, but before creating a tag:

1. Select and record the reviewed `main` merge commit as a full OID. In a clean checkout of that
   exact commit, run `ROCS_CI_PROFILE=main-strict ./scripts/ci/full.sh` and strict docs validation.
2. Obtain current owner evidence for **each** destination showing that a GitHub ruleset, protected
   tag rule, or equivalent server control currently prevents update and deletion of exact ref
   `refs/tags/v0.2.0`. Record repository URL, ruleset/control identity, observation time,
   matching ref or pattern, enforcement status, protected operations, bypass actors, and explicit
   owner acceptance of every bypass or exception. If evidence is absent, stale, inaccessible,
   ambiguous, or unaccepted, stop before tag creation.
3. Confirm release authority names `v0.2.0`, the selected full release OID, and exactly the two
   destination URLs above. A branch, alias, prior tag, or protection setting is not authority.
4. Run the absence checks in the execution block below. Return code `2` means the requested ref is
   absent; any other nonzero code is a lookup/transport/authentication failure and must not be
   treated as absence. If the tag exists anywhere, stop and reconcile its tag-object and peeled
   commit OIDs; never move or overwrite it.

## `v0.2.0` execution and verification

Only after the reviewed `main` merge and the complete owner-evidence preflight, run this as one
Bash procedure:

```bash
set -euo pipefail

tag_ref="refs/tags/v0.2.0"
release_oid="${RELEASE_OID:?set RELEASE_OID to the full reviewed main merge commit OID}"
destinations=(
  "https://github.com/tryingET/ontology-kernel.git"
  "https://github.com/tryingET/core_ontology-kernel.git"
)
attempted=()
declare -A seen_destinations=()
for url in "${destinations[@]}"; do
  if [[ -n "${seen_destinations[$url]+present}" ]]; then
    printf 'duplicate release destination: %s\n' "$url" >&2
    exit 1
  fi
  seen_destinations["$url"]=1
done

require_remote_absent() {
  local url=$1 output rc
  if output=$(git ls-remote --exit-code "$url" "$tag_ref" "${tag_ref}^{}" 2>&1); then
    rc=0
  else
    rc=$?
  fi
  case "$rc" in
    2) return 0 ;;
    0) printf 'tag already exists at %s: %s\n' "$url" "$output" >&2; return 1 ;;
    *) printf 'tag lookup failed (transport/auth) at %s, rc=%s: %s\n' \
         "$url" "$rc" "$output" >&2; return 1 ;;
  esac
}

verify_live_tag() {
  local url=$1 output rc line expected_direct expected_peeled
  local direct_count=0 peeled_count=0
  local -a lines
  if output=$(git ls-remote --exit-code "$url" "$tag_ref" "${tag_ref}^{}" 2>&1); then
    rc=0
  else
    rc=$?
  fi
  case "$rc" in
    0) ;;
    2) printf 'published tag is absent at %s\n' "$url" >&2; return 1 ;;
    *) printf 'published tag lookup failed (transport/auth) at %s, rc=%s: %s\n' \
         "$url" "$rc" "$output" >&2; return 1 ;;
  esac

  mapfile -t lines <<<"$output"
  expected_direct="${tag_oid}"$'\t'"${tag_ref}"
  expected_peeled="${release_oid}"$'\t'"${tag_ref}^{}"
  test "${#lines[@]}" -eq 2 || return 1
  for line in "${lines[@]}"; do
    case "$line" in
      "$expected_direct") direct_count=$((direct_count + 1)) ;;
      "$expected_peeled") peeled_count=$((peeled_count + 1)) ;;
      *) printf 'unexpected live tag line at %s: %s\n' "$url" "$line" >&2; return 1 ;;
    esac
  done
  test "$direct_count" -eq 1 || return 1
  test "$peeled_count" -eq 1 || return 1
  printf 'live tag verified: url=%s tag_oid=%s release_oid=%s\n' \
    "$url" "$tag_oid" "$release_oid"
  python3 scripts/verify_commit_handoff.py \
    --repo . --remote "$url" --ref "$tag_ref" --commit "$release_oid"
}

observe_attempted_tag() {
  local url=$1 output rc line expected_direct expected_peeled
  local direct_count=0 peeled_count=0 mismatch=0
  local -a lines
  if output=$(git ls-remote --exit-code "$url" "$tag_ref" "${tag_ref}^{}" 2>&1); then
    rc=0
  else
    rc=$?
  fi
  case "$rc" in
    2)
      printf 'attempted destination: url=%s state=absent\n' "$url" >&2
      return 0
      ;;
    0) ;;
    *)
      printf 'attempted destination: url=%s state=unavailable rc=%s output=%q\n' \
        "$url" "$rc" "$output" >&2
      return 0
      ;;
  esac

  mapfile -t lines <<<"$output"
  expected_direct="${tag_oid}"$'\t'"${tag_ref}"
  expected_peeled="${release_oid}"$'\t'"${tag_ref}^{}"
  if [[ "${#lines[@]}" -ne 2 ]]; then
    mismatch=1
  else
    for line in "${lines[@]}"; do
      case "$line" in
        "$expected_direct") direct_count=$((direct_count + 1)) ;;
        "$expected_peeled") peeled_count=$((peeled_count + 1)) ;;
        *) mismatch=1 ;;
      esac
    done
    if [[ "$direct_count" -ne 1 || "$peeled_count" -ne 1 ]]; then
      mismatch=1
    fi
  fi
  if [[ "$mismatch" -eq 0 ]]; then
    printf 'attempted destination: url=%s state=exact-match tag_oid=%s release_oid=%s\n' \
      "$url" "$tag_oid" "$release_oid" >&2
  else
    printf 'attempted destination: url=%s state=mismatch output=%q\n' \
      "$url" "$output" >&2
  fi
  return 0
}

partial_stop() {
  local reason=$1 failed_url=$2 url
  printf 'STOP publication: %s; failed destination=%s; tag_oid=%s; release_oid=%s\n' \
    "$reason" "$failed_url" "$tag_oid" "$release_oid" >&2
  for url in "${attempted[@]}"; do
    observe_attempted_tag "$url"
  done
  return 0
}

test "$(git rev-parse --verify 'HEAD^{commit}')" = "$release_oid"
if git show-ref --verify --quiet "$tag_ref"; then
  local_tag_rc=0
else
  local_tag_rc=$?
fi
case "$local_tag_rc" in
  1) ;;
  0) printf 'local tag already exists: %s\n' "$tag_ref" >&2; exit 1 ;;
  *) printf 'local tag lookup failed, rc=%s\n' "$local_tag_rc" >&2; exit 1 ;;
esac
for url in "${destinations[@]}"; do
  require_remote_absent "$url"
done

git tag -a v0.2.0 "$release_oid" -m 'ontology-kernel v0.2.0'
tag_oid=$(git rev-parse --verify "${tag_ref}^{tag}")
test "$(git rev-parse --verify "${tag_ref}^{commit}")" = "$release_oid"

for url in "${destinations[@]}"; do
  attempted+=("$url")
  if git push "$url" "${tag_ref}:${tag_ref}"; then
    push_rc=0
  else
    push_rc=$?
  fi
  if test "$push_rc" -ne 0; then
    partial_stop "exact tag push failed with rc=$push_rc" "$url"
    exit 1
  fi

  if verify_live_tag "$url"; then
    verify_rc=0
  else
    verify_rc=$?
  fi
  if test "$verify_rc" -ne 0; then
    partial_stop "post-push live verification failed with rc=$verify_rc" "$url"
    exit 1
  fi
done
```

Do not use `git push --tags`, an ambient push, a force push, or an alias. Success requires exactly
one live direct tag line equal to local annotated `tag_oid`, exactly one peeled line equal to
`release_oid`, and a successful OID-only handoff check at both exact URLs.

## Partial publication

Every destination is added to `attempted` before its push. If any push or live verification fails,
the procedure stops and immediately queries every attempted URL—including a failed-push URL—and
records exactly one state: exact direct-plus-peeled match, absent, mismatch, or unavailable. It
never infers publication state from push return code. Preserve the exact local OIDs and these fresh
observations as owner evidence. Do not delete, move, recreate, or force the tag.

Before resuming, obtain fresh owner authority. Re-observe ruleset identity, time, enforcement,
protected operations, and bypasses at both destinations; verify already-published refs still have
exactly the recorded tag-object and peeled OIDs; and prove the ref is absent at every unpublished
destination, distinguishing absence from lookup failure. Authority may then permit publication of
the **same tag object** to the missing destination, or separately authorize a forward corrective
release. It may not rewrite the published tag.

## Pre-merge rollback of the AK 4881 candidate

Rollback requires separate owner authority. Query and fetch live `refs/heads/main` from the origin
URL, then run `git merge-base --is-ancestor <reviewed-candidate-oid> <live-main-oid>`. Only return
code `1` proves not merged; `0` means merged and every other code is an error. Stop unless
not-merged status is proved. Close the AK 4881 PR through the owner-approved GitHub mechanism and
verify its live state is `closed`.

Only after those proofs, run this deletion block with the same AK-reviewed `CANDIDATE_OID`. It
requires the live review ref to equal that OID, uses compare-and-swap deletion scoped to that ref,
and then requires a fresh lookup to return `2` (absent):

```bash
set -euo pipefail

origin_url="https://github.com/tryingET/ontology-kernel.git"
candidate_ref="refs/heads/release/ontology-kernel-v0.2.0-prep"
candidate_oid="${CANDIDATE_OID:?AK must supply the reviewed full candidate OID}"
[[ "$candidate_oid" =~ ^[0-9a-f]{40}$ ]]
expected_branch_line="${candidate_oid}"$'\t'"${candidate_ref}"

if before_output=$(git ls-remote --exit-code "$origin_url" "$candidate_ref" 2>&1); then
  before_rc=0
else
  before_rc=$?
fi
case "$before_rc" in
  0) ;;
  2) printf 'review branch already absent; do not issue deletion\n' >&2; exit 1 ;;
  *) printf 'review branch lookup unavailable, rc=%s: %s\n' \
       "$before_rc" "$before_output" >&2; exit 1 ;;
esac
mapfile -t before_lines <<<"$before_output"
test "${#before_lines[@]}" -eq 1
test "${before_lines[0]}" = "$expected_branch_line"

if git push --force-with-lease="${candidate_ref}:${candidate_oid}" \
    "$origin_url" ":${candidate_ref}"; then
  delete_rc=0
else
  delete_rc=$?
fi
if after_output=$(git ls-remote --exit-code "$origin_url" "$candidate_ref" 2>&1); then
  after_rc=0
else
  after_rc=$?
fi
case "$after_rc" in
  2) ;;
  0) printf 'review branch still present after deletion attempt: %s\n' \
       "$after_output" >&2; exit 1 ;;
  *) printf 'post-deletion lookup unavailable, rc=%s: %s\n' \
       "$after_rc" "$after_output" >&2; exit 1 ;;
esac
test "$delete_rc" -eq 0
```

Do not retry automatically. The lease/force is permitted only for compare-and-swap deletion of
that exact review branch. Never apply a lease, force, deletion, or rewrite to `main`, any tag,
another branch, or AK history. If live lookup, not-merged status, PR closure, branch identity,
delete result, or confirmed absence cannot be proved, stop for revised authority.
