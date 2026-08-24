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

## `v0.2.0` destination

The complete intended release destination set is exactly one repository:

1. `https://github.com/tryingET/core_ontology-kernel.git`

Owner decision of 2026-08-24 (AK `4911` evidence `7442`): the public
`tryingET/core_ontology-kernel` is the sole destination because it carries the holding naming
schema. The two-destination set recorded at `90106efeb7893ec26093ed359ab647e9bf21c007` — which
also named `https://github.com/tryingET/ontology-kernel.git` — is superseded and must not be
executed. `tryingET/ontology-kernel` remains the private PR/review surface until its owner
separately archives or deletes it; it is not a v0.2.0 destination, and this contract grants no
archival or deletion authority.

NAS is not required for `v0.2.0` and is not a release destination. Do not infer, add, replace, or
skip a destination from configured remote aliases; aliases are convenience only, not authority.

## Completed AK 4881 preparation

AK `4881`'s review-branch sequence is complete and must not be replayed. AK `4890` records PR `#2`
merged to origin `main` at `d50c7ef8127afc7967db6d025287d2c69ea2858e` without creating a tag
or Release. Git preserves the exact pre-correction runbook at merge commit
`d50c7ef8127afc7967db6d025287d2c69ea2858e`; the
[AK 4881 preparation record](docs/project/2026-08-23-ontology-kernel-v0.2.0-release-preparation.md)
summarizes its scope and evidence. Any later branch cleanup or source revert requires separate
authority; neither is release publication.

## `v0.2.0` GitHub immutable-release preflight

GitHub Release immutability, not a direct tag push, is the selected protection transition for this
release. GitHub documents that the associated tag and assets become immutable only when a Release
is **published**; a draft is not protected. GitHub's repository setting applies only to future
releases. The REST and GraphQL Release objects expose the resulting per-release `immutable`
value. The repository-level switch is also observable through
`gh api repos/{owner}/{repo}/immutable-releases` (observed 2026-08-24; it was not known during
AK `4905`). Reading it corroborates a receipt; changing it requires separate owner authority that
this procedure does not grant.

Before creating the draft, all of the following must hold:

1. Select the final reviewed `main` commit as a full OID. In a clean checkout at that exact OID,
   run `ROCS_CI_PROFILE=main-strict ./scripts/ci/full.sh` and strict docs validation. Record the
   exact command receipts and prove the checkout remains clean.
2. Prove `refs/heads/main` at the destination URL resolves to that exact OID. A commit that is
   absent from the destination repository is not a valid release target. Any required
   branch-parity publication needs its own authority and verification before release-draft work.
3. For the exact destination repository, an owner must navigate to **Settings → General →
   Releases**, select **Enable release immutability**, and record a current owner receipt naming
   repository, observed control label/state, actor, UTC time, and evidence location. If the
   setting is unavailable, unchecked, stale, or cannot be evidenced, stop. Do not infer it from
   plan level, ruleset availability, a remote alias, or a draft's `immutable: false` value.
   Corroborate the receipt with a current read-only
   `gh api repos/tryingET/core_ontology-kernel/immutable-releases` returning `enabled: true`.
4. Prove `refs/tags/v0.2.0` and every draft or published Release whose `tag_name` is `v0.2.0` are
   absent at the destination repository. Return code `2` from `git ls-remote --exit-code` means
   ref absence;
   every other nonzero result is an error, not absence. Release-list pagination and authenticated
   visibility of drafts are mandatory.
5. Establish an exclusive publication window: every owner-accepted actor or automation able to
   write tags or Releases is quiescent from the final absence check through post-publication
   verification. GitHub's APIs provide no compare-and-swap binding between the last tag check and
   draft publication. The later publication authority must explicitly accept this residual race;
   a check does not prove that the race is impossible.

Draft preparation and publication are separate effects. Draft authority may create only the
exact single draft below. Later publication authority must name `v0.2.0`, the final full OID, the
exact destination repository URL, the numeric draft ID, the expected title/body digest and empty
asset set, the current setting receipts, residual-race acceptance, and the forward-only recovery
boundary. A branch, draft, setting, prior assessment, or protection observation is not
publication authority.

## Draft preparation under separate authority

The release has no uploaded assets; GitHub-generated source archives are not Release assets. Use a
fixed title and body rather than generated notes. Run the following only from the clean exact-OID
checkout and only under a task that authorizes draft creation. It may create an unprotected
lightweight tag while a draft exists, so every returned state must be verified immediately.

```bash
set -euo pipefail

release_oid="${RELEASE_OID:?set the authorized full release commit OID}"
receipt_root="${DRAFT_RECEIPT_DIR:?set a new durable task-owned draft receipt directory}"
draft_authority="${DRAFT_AUTHORITY:?set the exact AK draft authority reference}"
tag_name="v0.2.0"
tag_ref="refs/tags/$tag_name"
repositories=(
  "tryingET/core_ontology-kernel"
)
urls=(
  "https://github.com/tryingET/core_ontology-kernel.git"
)
setting_receipts=(
  "${DESTINATION_IMMUTABILITY_RECEIPT:?set the accepted destination setting receipt}"
)
test "${#repositories[@]}" -eq 1
test "${#urls[@]}" -eq "${#repositories[@]}"
test "${#setting_receipts[@]}" -eq "${#repositories[@]}"
release_title="ontology-kernel v0.2.0"
printf -v release_body \
  'Immutable ontology-kernel v0.2.0 release.\n\nRelease commit: `%s`.\n' \
  "$release_oid"
release_body_sha256=$(printf '%s' "$release_body" | sha256sum | awk '{print $1}')
[[ "$release_body_sha256" =~ ^[0-9a-f]{64}$ ]]
[[ "$release_oid" =~ ^[0-9a-f]{40}$ ]]
test "$(git rev-parse --verify 'HEAD^{commit}')" = "$release_oid"
test ! -e "$receipt_root"
mkdir -m 700 -- "$receipt_root"
created_ids=("")
observation_round=0
printf 'draft_authority=%s setting_receipts=%s body_sha256=%s\n' \
  "$draft_authority" "${setting_receipts[0]}" \
  "$release_body_sha256"

require_push_visibility() {
  local repo=$1 permission
  permission=$(gh api "repos/$repo" --jq '.permissions.push') || return 1
  test "$permission" = true || {
    printf 'authenticated push visibility is not proved for %s\n' "$repo" >&2
    return 1
  }
  return 0
}

require_main_oid() {
  local url=$1 output rc expected
  if output=$(git ls-remote --exit-code "$url" refs/heads/main 2>&1); then
    rc=0
  else
    rc=$?
  fi
  test "$rc" -eq 0 || {
    printf 'main lookup failed at %s, rc=%s: %s\n' "$url" "$rc" "$output" >&2
    return 1
  }
  expected="${release_oid}"$'\t'"refs/heads/main"
  test "$output" = "$expected" || {
    printf 'main mismatch at %s: %s\n' "$url" "$output" >&2
    return 1
  }
  return 0
}

require_tag_absent() {
  local url=$1 output rc
  if output=$(git ls-remote --exit-code "$url" "$tag_ref" "${tag_ref}^{}" 2>&1); then
    rc=0
  else
    rc=$?
  fi
  case "$rc" in
    2) return 0 ;;
    0) printf 'tag already exists at %s: %s\n' "$url" "$output" >&2; return 1 ;;
    *) printf 'tag lookup failed at %s, rc=%s: %s\n' \
         "$url" "$rc" "$output" >&2; return 1 ;;
  esac
}

matching_releases() {
  local repo=$1
  gh api --paginate --slurp "repos/$repo/releases?per_page=100" \
    | jq --arg tag "$tag_name" '[add[] | select(.tag_name == $tag)]' \
    || return 1
  return 0
}

require_release_absent() {
  local repo=$1 matches count
  matches=$(matching_releases "$repo") || return 1
  count=$(jq -er 'length' <<<"$matches") || return 1
  test "$count" -eq 0 || {
    printf 'Release already exists at %s: %s\n' "$repo" "$matches" >&2
    return 1
  }
  return 0
}

verify_draft_tag_state() {
  local url=$1 output rc expected
  if output=$(git ls-remote --exit-code "$url" "$tag_ref" "${tag_ref}^{}" 2>&1); then
    rc=0
  else
    rc=$?
  fi
  case "$rc" in
    2) printf 'draft tag state: url=%s state=absent\n' "$url"; return 0 ;;
    0)
      expected="${release_oid}"$'\t'"${tag_ref}"
      test "$output" = "$expected" || {
        printf 'draft tag mismatch at %s: %s\n' "$url" "$output" >&2
        return 1
      }
      printf 'draft tag state: url=%s state=exact-lightweight oid=%s\n' \
        "$url" "$release_oid"
      return 0
      ;;
    *) printf 'draft tag lookup failed at %s, rc=%s: %s\n' \
         "$url" "$rc" "$output" >&2; return 1 ;;
  esac
}

global_preflight_one() {
  local repo=$1 url=$2
  require_push_visibility "$repo" || return 1
  require_main_oid "$url" || return 1
  require_tag_absent "$url" || return 1
  require_release_absent "$repo" || return 1
  return 0
}

observe_draft_all() {
  local reason=$1 i repo url matches tag_output tag_rc main_output main_rc file
  observation_round=$((observation_round + 1))
  printf 'STOP draft preparation: %s; release_oid=%s\n' \
    "$reason" "$release_oid" >&2
  for i in "${!repositories[@]}"; do
    repo=${repositories[$i]}; url=${urls[$i]}
    file="$receipt_root/observe-$observation_round-$i-releases.json"
    if matches=$(matching_releases "$repo" 2>&1); then
      printf '%s\n' "$matches" > "$file"
      jq -c --arg expected_name "$release_title" --arg expected_body "$release_body" \
        '[.[] | {id,node_id,html_url,tag_name,target_commitish,name,
          name_matches:(.name == $expected_name),
          body_matches:(.body == $expected_body),body_bytes:((.body // "") | utf8bytelength),
          draft,prerelease,immutable,published_at,
          assets:[.assets[]? | {id,name,label,state,size,digest}]}]' "$file" >&2 || true
    else
      printf '%s\n' "$matches" > "$file.error"
      printf 'Release observation unavailable: repo=%s output=%q\n' \
        "$repo" "$matches" >&2
    fi
    if tag_output=$(git ls-remote --exit-code "$url" "$tag_ref" "${tag_ref}^{}" 2>&1); then
      tag_rc=0
    else
      tag_rc=$?
    fi
    printf '%s\n' "$tag_output" > "$receipt_root/observe-$observation_round-$i-tag.txt"
    printf 'tag observation: url=%s rc=%s output=%q\n' \
      "$url" "$tag_rc" "$tag_output" >&2
    if main_output=$(git ls-remote --exit-code "$url" refs/heads/main 2>&1); then
      main_rc=0
    else
      main_rc=$?
    fi
    printf '%s\n' "$main_output" > "$receipt_root/observe-$observation_round-$i-main.txt"
    printf 'main observation: url=%s rc=%s output=%q\n' \
      "$url" "$main_rc" "$main_output" >&2
  done
  return 0
}

create_and_verify_draft() {
  local i=$1 repo=${repositories[$1]} url=${urls[$1]}
  local payload release_id fresh matches count only_id post_rc
  require_push_visibility "$repo" || return 1
  require_main_oid "$url" || return 1
  require_tag_absent "$url" || return 1
  require_release_absent "$repo" || return 1
  payload=$(jq -n \
    --arg tag "$tag_name" --arg target "$release_oid" \
    --arg name "$release_title" --arg body "$release_body" \
    '{tag_name:$tag,target_commitish:$target,name:$name,body:$body,
      draft:true,prerelease:false}') || return 1
  if gh api --method POST "repos/$repo/releases" --input - \
      <<<"$payload" > "$receipt_root/$i.created.json"; then
    post_rc=0
  else
    post_rc=$?
  fi
  test "$post_rc" -eq 0 || return "$post_rc"
  release_id=$(jq -er '.id | select(type == "number" and . > 0)' \
    "$receipt_root/$i.created.json") || return 1
  created_ids[$i]=$release_id
  gh api "repos/$repo/releases/$release_id" \
    > "$receipt_root/$i.fresh.json" || return 1
  fresh=$(cat "$receipt_root/$i.fresh.json") || return 1
  jq -e \
    --argjson id "$release_id" --arg tag "$tag_name" --arg target "$release_oid" \
    --arg name "$release_title" --arg body "$release_body" \
    '.id == $id and .tag_name == $tag and .target_commitish == $target and
     .name == $name and .body == $body and .draft == true and
     .prerelease == false and .immutable == false and (.assets | length) == 0' \
    <<<"$fresh" >/dev/null || return 1
  matches=$(matching_releases "$repo") || return 1
  count=$(jq -er 'length' <<<"$matches") || return 1
  only_id=$(jq -er '.[0].id' <<<"$matches") || return 1
  test "$count" -eq 1 || return 1
  test "$only_id" = "$release_id" || return 1
  verify_draft_tag_state "$url" || return 1
  jq '{id,node_id,html_url,tag_name,target_commitish,name,body,draft,
       prerelease,immutable,assets}' "$receipt_root/$i.fresh.json" \
    | tee "$receipt_root/$i.normalized.json" || return 1
  return 0
}

# Complete the effect-free preflight for the destination repository before the POST.
for i in "${!repositories[@]}"; do
  if global_preflight_one "${repositories[$i]}" "${urls[$i]}"; then
    preflight_rc=0
  else
    preflight_rc=$?
  fi
  if test "$preflight_rc" -ne 0; then
    observe_draft_all "global preflight failed for ${repositories[$i]} (rc=$preflight_rc)"
    exit 1
  fi
done

for i in "${!repositories[@]}"; do
  if create_and_verify_draft "$i"; then
    draft_rc=0
  else
    draft_rc=$?
  fi
  if test "$draft_rc" -ne 0; then
    observe_draft_all "draft call or verification failed for ${repositories[$i]} (rc=$draft_rc)"
    exit 1
  fi
done
printf 'draft_ids=%s receipt_root=%s\n' \
  "${created_ids[0]}" "$receipt_root"
```

A failed draft call is effect-indeterminate. Query the destination repository immediately; do
not infer absence from the command's return code and do not retry mechanically. The procedure retains raw and
normalized responses in the caller-supplied durable receipt directory; do not delete it until the
bounded receipts have been exported to AK. Preserve each numeric draft ID, fresh response, tag
observation, exact body bytes/digest, and command receipt. Do not publish, delete, or edit a draft
or its tag without revised authority.

## Publication and immutable verification under later authority

The publisher must receive the numeric draft ID through AK, not discover and self-authorize it.
Immediately before the publish transition, revalidate the destination `main` ref and the
destination: it must still be an exact empty-asset draft with an absent or exact lightweight tag.
Bind fresh owner setting-receipt references as explicit inputs. The publication invocation must
use a new no-clobber receipt directory, separate from the retained draft directory. Any drift
stops the sequence.

```bash
set -euo pipefail

release_oid="${RELEASE_OID:?set the separately authorized full release commit OID}"
draft_receipt_root="${DRAFT_RECEIPT_DIR:?set the durable draft receipt directory}"
receipt_root="${PUBLICATION_RECEIPT_DIR:?set a new publication-session receipt directory}"
publication_authority="${PUBLICATION_AUTHORITY:?set the exact AK publication authority reference}"
tag_name="v0.2.0"
tag_ref="refs/tags/$tag_name"
repositories=(
  "tryingET/core_ontology-kernel"
)
urls=(
  "https://github.com/tryingET/core_ontology-kernel.git"
)
draft_ids=(
  "${DESTINATION_DRAFT_ID:?set the authorized destination draft ID}"
)
setting_receipts=(
  "${DESTINATION_IMMUTABILITY_RECEIPT:?set the accepted destination setting receipt}"
)
test "${#repositories[@]}" -eq 1
test "${#urls[@]}" -eq "${#repositories[@]}"
test "${#draft_ids[@]}" -eq "${#repositories[@]}"
test "${#setting_receipts[@]}" -eq "${#repositories[@]}"
release_title="ontology-kernel v0.2.0"
printf -v release_body \
  'Immutable ontology-kernel v0.2.0 release.\n\nRelease commit: `%s`.\n' \
  "$release_oid"
release_body_sha256=$(printf '%s' "$release_body" | sha256sum | awk '{print $1}')
[[ "$release_body_sha256" =~ ^[0-9a-f]{64}$ ]]
[[ "$release_oid" =~ ^[0-9a-f]{40}$ ]]
test "$(git rev-parse --verify 'HEAD^{commit}')" = "$release_oid"
test -d "$draft_receipt_root" || exit 1
test -r "$draft_receipt_root" || exit 1
test ! -e "$receipt_root" || exit 1
mkdir -m 700 -- "$receipt_root"
command -v timeout >/dev/null || exit 1
verify_sequence=0
observation_round=0
read_deadline_epoch=0
readonly VERIFY_TRANSIENT=10 VERIFY_MISMATCH=20
printf 'publication_authority=%s setting_receipts=%s body_sha256=%s draft_receipts=%s publication_receipts=%s\n' \
  "$publication_authority" "${setting_receipts[0]}" \
  "$release_body_sha256" "$draft_receipt_root" "$receipt_root"

run_read() {
  local now remaining limit=30
  if (( read_deadline_epoch > 0 )); then
    printf -v now '%(%s)T' -1
    remaining=$((read_deadline_epoch - now))
    (( remaining > 0 )) || return 124
    if (( remaining < limit )); then limit=$remaining; fi
  fi
  timeout --signal=KILL "$limit" "$@"
}

require_push_visibility() {
  local repo=$1 permission rc
  if permission=$(run_read gh api "repos/$repo" --jq '.permissions.push'); then
    rc=0
  else
    rc=$?
  fi
  test "$rc" -eq 0 || return "$VERIFY_TRANSIENT"
  test "$permission" = true || return "$VERIFY_MISMATCH"
  return 0
}

require_main_oid() {
  local url=$1 output rc expected
  if output=$(run_read git ls-remote --exit-code "$url" refs/heads/main 2>&1); then
    rc=0
  else
    rc=$?
  fi
  test "$rc" -eq 0 || return "$VERIFY_TRANSIENT"
  expected="${release_oid}"$'\t'"refs/heads/main"
  test "$output" = "$expected" || return "$VERIFY_MISMATCH"
  return 0
}

matching_releases() {
  local repo=$1
  if run_read gh api --paginate --slurp "repos/$repo/releases?per_page=100" \
      | jq --arg tag "$tag_name" '[add[] | select(.tag_name == $tag)]'; then
    return 0
  fi
  return "$VERIFY_TRANSIENT"
}

verify_draft_tag_state() {
  local url=$1 output rc expected
  if output=$(run_read git ls-remote --exit-code \
      "$url" "$tag_ref" "${tag_ref}^{}" 2>&1); then
    rc=0
  else
    rc=$?
  fi
  case "$rc" in
    2) return 0 ;;
    0)
      expected="${release_oid}"$'\t'"${tag_ref}"
      test "$output" = "$expected" || return "$VERIFY_MISMATCH"
      return 0
      ;;
    *) return "$VERIFY_TRANSIENT" ;;
  esac
}

verify_draft() {
  local i=$1 repo=${repositories[$1]} url=${urls[$1]} id=${draft_ids[$1]}
  local fresh matches count only_id file
  [[ "$id" =~ ^[1-9][0-9]*$ ]] || return 1
  require_push_visibility "$repo" || return 1
  require_main_oid "$url" || return 1
  verify_sequence=$((verify_sequence + 1))
  file="$receipt_root/verify-$verify_sequence-$i-draft.json"
  run_read gh api "repos/$repo/releases/$id" > "$file" || return 1
  fresh=$(cat "$file") || return 1
  jq -e \
    --argjson id "$id" --arg tag "$tag_name" --arg target "$release_oid" \
    --arg name "$release_title" --arg body "$release_body" \
    '.id == $id and .tag_name == $tag and .target_commitish == $target and
     .name == $name and .body == $body and .draft == true and
     .prerelease == false and .immutable == false and (.assets | length) == 0' \
    <<<"$fresh" >/dev/null || return 1
  matches=$(matching_releases "$repo") || return 1
  count=$(jq -er 'length' <<<"$matches") || return 1
  only_id=$(jq -er '.[0].id' <<<"$matches") || return 1
  test "$count" -eq 1 || return 1
  test "$only_id" = "$id" || return 1
  verify_draft_tag_state "$url" || return 1
  return 0
}

verify_published_once() {
  local i=$1 repo=${repositories[$1]} url=${urls[$1]} id=${draft_ids[$1]}
  local fresh matches count only_id output rc expected file
  local attestation_out attestation_err attestation_rc
  [[ "$id" =~ ^[1-9][0-9]*$ ]] || return "$VERIFY_MISMATCH"
  if require_push_visibility "$repo"; then rc=0; else rc=$?; fi
  test "$rc" -eq 0 || return "$rc"
  if require_main_oid "$url"; then rc=0; else rc=$?; fi
  test "$rc" -eq 0 || return "$rc"
  verify_sequence=$((verify_sequence + 1))
  file="$receipt_root/verify-$verify_sequence-$i-published.json"
  run_read gh api "repos/$repo/releases/$id" > "$file" \
    || return "$VERIFY_TRANSIENT"
  fresh=$(cat "$file") || return "$VERIFY_MISMATCH"
  jq -e \
    --argjson id "$id" --arg tag "$tag_name" --arg target "$release_oid" \
    --arg name "$release_title" --arg body "$release_body" \
    '.id == $id and .tag_name == $tag and .target_commitish == $target and
     .name == $name and .body == $body and .draft == false and
     .prerelease == false and .immutable == true and (.assets | length) == 0 and
     (.published_at | type == "string")' <<<"$fresh" >/dev/null \
    || return "$VERIFY_MISMATCH"
  if matches=$(matching_releases "$repo"); then rc=0; else rc=$?; fi
  test "$rc" -eq 0 || return "$rc"
  count=$(jq -er 'length' <<<"$matches") || return "$VERIFY_MISMATCH"
  only_id=$(jq -er '.[0].id' <<<"$matches") || return "$VERIFY_MISMATCH"
  test "$count" -eq 1 || return "$VERIFY_MISMATCH"
  test "$only_id" = "$id" || return "$VERIFY_MISMATCH"
  if output=$(run_read git ls-remote --exit-code \
      "$url" "$tag_ref" "${tag_ref}^{}" 2>&1); then
    rc=0
  else
    rc=$?
  fi
  test "$rc" -eq 0 || return "$VERIFY_TRANSIENT"
  expected="${release_oid}"$'\t'"${tag_ref}"
  test "$output" = "$expected" || return "$VERIFY_MISMATCH"
  run_read python3 scripts/verify_commit_handoff.py \
    --repo . --remote "$url" --ref "$tag_ref" --commit "$release_oid" \
    || return "$VERIFY_TRANSIENT"
  attestation_out="$receipt_root/verify-$verify_sequence-$i-attestation.json"
  attestation_err="$receipt_root/verify-$verify_sequence-$i-attestation.stderr"
  if run_read gh release verify "$tag_name" -R "$repo" --format json \
      > "$attestation_out" 2> "$attestation_err"; then
    attestation_rc=0
  else
    attestation_rc=$?
  fi
  printf '%s\n' "$attestation_rc" \
    > "$receipt_root/verify-$verify_sequence-$i-attestation.rc"
  test "$attestation_rc" -eq 0 || return "$VERIFY_TRANSIENT"
  jq '{id,node_id,html_url,tag_name,target_commitish,name,body,draft,
       prerelease,immutable,published_at,assets}' <<<"$fresh" \
    > "$receipt_root/verify-$verify_sequence-$i-normalized.json" \
    || return "$VERIFY_MISMATCH"
  return 0
}

verify_published_eventually() {
  local i=$1 attempt=0 rc now remaining sleep_for
  local saved_deadline=$read_deadline_epoch poll_deadline
  printf -v now '%(%s)T' -1
  poll_deadline=$((now + 120))
  read_deadline_epoch=$poll_deadline
  while true; do
    printf -v now '%(%s)T' -1
    remaining=$((poll_deadline - now))
    if (( remaining <= 0 )); then
      read_deadline_epoch=$saved_deadline
      return "$VERIFY_TRANSIENT"
    fi
    attempt=$((attempt + 1))
    if verify_published_once "$i"; then
      printf 'published verification complete: repo=%s attempts=%s\n' \
        "${repositories[$i]}" "$attempt"
      read_deadline_epoch=$saved_deadline
      return 0
    else
      rc=$?
    fi
    if test "$rc" -eq "$VERIFY_MISMATCH"; then
      read_deadline_epoch=$saved_deadline
      return "$VERIFY_MISMATCH"
    fi
    printf -v now '%(%s)T' -1
    remaining=$((poll_deadline - now))
    if (( remaining <= 0 )); then
      read_deadline_epoch=$saved_deadline
      return "$VERIFY_TRANSIENT"
    fi
    sleep_for=5
    if (( remaining < sleep_for )); then sleep_for=$remaining; fi
    sleep "$sleep_for" || {
      read_deadline_epoch=$saved_deadline
      return "$VERIFY_TRANSIENT"
    }
  done
}

observe_all() {
  local reason=$1 i repo url id release_json matches tag_output tag_rc
  local main_output main_rc release_file matches_file now
  local saved_deadline=$read_deadline_epoch
  observation_round=$((observation_round + 1))
  printf -v now '%(%s)T' -1
  read_deadline_epoch=$((now + 60))
  printf 'STOP publication: %s; release_oid=%s\n' "$reason" "$release_oid" >&2
  for i in "${!repositories[@]}"; do
    repo=${repositories[$i]}; url=${urls[$i]}; id=${draft_ids[$i]}
    release_file="$receipt_root/observe-$observation_round-$i-release.json"
    if release_json=$(run_read gh api "repos/$repo/releases/$id" 2>&1); then
      printf '%s\n' "$release_json" > "$release_file"
      jq -c --arg expected_name "$release_title" --arg expected_body "$release_body" \
        '{id,node_id,html_url,tag_name,target_commitish,name,
          name_matches:(.name == $expected_name),
          body_matches:(.body == $expected_body),body_bytes:((.body // "") | utf8bytelength),
          draft,prerelease,immutable,published_at,
          assets:[.assets[]? | {id,name,label,state,size,digest}]}' \
        "$release_file" >&2 || true
    else
      printf '%s\n' "$release_json" > "$release_file.error"
      printf 'Release observation unavailable: repo=%s output=%q\n' \
        "$repo" "$release_json" >&2
    fi
    matches_file="$receipt_root/observe-$observation_round-$i-matches.json"
    if matches=$(matching_releases "$repo" 2>&1); then
      printf '%s\n' "$matches" > "$matches_file"
      jq -c --arg expected_name "$release_title" --arg expected_body "$release_body" \
        '[.[] | {id,node_id,html_url,tag_name,target_commitish,name,
          name_matches:(.name == $expected_name),
          body_matches:(.body == $expected_body),body_bytes:((.body // "") | utf8bytelength),
          draft,prerelease,immutable,published_at,
          assets:[.assets[]? | {id,name,label,state,size,digest}]}]' \
        "$matches_file" >&2 || true
    else
      printf '%s\n' "$matches" > "$matches_file.error"
    fi
    if tag_output=$(run_read git ls-remote --exit-code \
        "$url" "$tag_ref" "${tag_ref}^{}" 2>&1); then
      tag_rc=0
    else
      tag_rc=$?
    fi
    printf '%s\n' "$tag_output" > "$receipt_root/observe-$observation_round-$i-tag.txt"
    printf 'tag observation: url=%s rc=%s output=%q\n' \
      "$url" "$tag_rc" "$tag_output" >&2
    if main_output=$(run_read git ls-remote --exit-code \
        "$url" refs/heads/main 2>&1); then
      main_rc=0
    else
      main_rc=$?
    fi
    printf '%s\n' "$main_output" > "$receipt_root/observe-$observation_round-$i-main.txt"
    printf 'main observation: url=%s rc=%s output=%q setting_receipt=%s\n' \
      "$url" "$main_rc" "$main_output" "${setting_receipts[$i]}" >&2
  done
  read_deadline_epoch=$saved_deadline
  return 0
}

verify_state_before_step() {
  local step=$1 j
  for j in "${!repositories[@]}"; do
    if (( j < step )); then
      verify_published_once "$j" || return 1
    else
      verify_draft "$j" || return 1
    fi
  done
  return 0
}

for i in "${!repositories[@]}"; do
  if verify_state_before_step "$i"; then
    state_rc=0
  else
    state_rc=$?
  fi
  if test "$state_rc" -ne 0; then
    observe_all "pre-publication state check failed before ${repositories[$i]} (rc=$state_rc)"
    exit 1
  fi

  repo=${repositories[$i]}; id=${draft_ids[$i]}
  if gh api --method PATCH "repos/$repo/releases/$id" \
      -F draft=false -f make_latest=true \
      > "$receipt_root/publish-$i-response.json"; then
    publish_rc=0
  else
    publish_rc=$?
  fi
  if test "$publish_rc" -ne 0; then
    observe_all "publish call failed or was indeterminate for $repo (rc=$publish_rc)"
    exit 1
  fi
  if verify_published_once "$i"; then
    initial_verify_rc=0
  else
    initial_verify_rc=$?
  fi
  if test "$initial_verify_rc" -ne 0; then
    observe_all "initial post-PATCH verification failed for $repo (rc=$initial_verify_rc)"
    if test "$initial_verify_rc" -eq "$VERIFY_MISMATCH"; then
      exit 1
    fi
    if verify_published_eventually "$i"; then
      verify_rc=0
    else
      verify_rc=$?
    fi
    if test "$verify_rc" -ne 0; then
      observe_all "bounded read-only verification failed for $repo (rc=$verify_rc)"
      exit 1
    fi
  fi
done

# Final read-only proof after the irreversible transition.
for i in "${!repositories[@]}"; do
  if verify_published_once "$i"; then
    final_rc=0
  else
    final_rc=$?
  fi
  if test "$final_rc" -ne 0; then
    observe_all "final cross-destination verification failed for ${repositories[$i]}"
    exit 1
  fi
done
```

Do not create a local tag, push a tag refspec, use `git push --tags`, generate release notes, add an
asset, or publish from a remote alias. `gh release verify` validates GitHub's signed release
attestation; it supplements, and does not replace, the exact live tag/OID and per-release
`immutable: true` checks.

## Partial publication and forward-only recovery

A publish command can fail after taking effect. On any command or verification failure, query
the numeric Release ID, authenticated matching-Release list, the `main` ref, and the exact tag
ref immediately, as `observe_all` does. Classify the destination as draft/absent-tag,
draft/exact-tag, published-and-exact-immutable, published-but-nonimmutable-or-mismatched, or
unavailable. Never infer state from a PATCH return code and never retry publication
mechanically. The procedure may poll only read surfaces for at most 120 seconds in five-second
intervals; it never repeats the PATCH.

Resume only under fresh owner authority after fresh setting receipts and exact state
observations. If the immutable Release and tag are exact but a read surface or attestation was
temporarily unavailable, fresh authority may permit read-only reverification; it must not
republish. A published nonimmutable or mismatched Release, changed content, unexpected asset,
tag drift, or cryptographically invalid attestation requires a separately authorized forward
corrective release. Do not move, delete, recreate, or force a published tag. Deleting an
immutable Release is not rollback: GitHub documents that its tag name cannot be reused even
after deletion.

## Historical AK 4881 rollback boundary

The AK `4881` pre-merge rollback is no longer available because AK `4890` records its candidate
merged. Do not close the merged PR or treat review-branch deletion as a rollback. A source rollback
now requires a separately reviewed revert; it changes the prospective release OID and invalidates
all earlier exact-OID validation or draft receipts. Never rewrite `main`, a tag, or AK history.
