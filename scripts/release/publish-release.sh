#!/usr/bin/env bash
# Publish one drafted ontology-kernel Release and verify it is immutable. This
# is the completed v0.2.0 publication block of RELEASING.md with the version as
# input, derived title and body, and added checks that fail closed;
# docs/release-procedure.md lists every difference. Running it grants nothing:
# it needs a separate publication authority that names the draft ID.
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.."

release_oid="${RELEASE_OID:?set the separately authorized full release commit OID}"
draft_receipt_root="${DRAFT_RECEIPT_DIR:?set the durable draft receipt directory}"
receipt_root="${PUBLICATION_RECEIPT_DIR:?set a new publication-session receipt directory}"
publication_authority="${PUBLICATION_AUTHORITY:?set the exact AK publication authority reference}"
tag_name="${RELEASE_VERSION:?set the authorized release version, such as v0.3.0}"
[[ "$tag_name" =~ ^v(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$ ]] || {
  printf 'RELEASE_VERSION must be vMAJOR.MINOR.PATCH, got %s\n' "$tag_name" >&2
  exit 1
}
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
release_title="ontology-kernel $tag_name"
printf -v release_body \
  'Immutable ontology-kernel %s release.\n\nRelease commit: `%s`.\n' \
  "$tag_name" "$release_oid"
release_body_sha256=$(printf '%s' "$release_body" | sha256sum | awk '{print $1}')
[[ "$release_body_sha256" =~ ^[0-9a-f]{64}$ ]]
[[ "$release_oid" =~ ^[0-9a-f]{40}$ ]]
test "$(git rev-parse --verify 'HEAD^{commit}')" = "$release_oid"
# Versioning rule (RELEASING.md), read from the release commit, not the working
# tree: the tag is "v" plus the manifest version.
manifest_version=$(git show "$release_oid:ontology/manifest.yaml" \
  | sed -n 's/^  version: "\(.*\)"$/\1/p')
test "v$manifest_version" = "$tag_name" || {
  printf 'manifest version %s does not match %s\n' "$manifest_version" "$tag_name" >&2
  exit 1
}
# A clean checkout, and receipt directories given as absolute paths, because
# this script runs from the checkout root.
test -z "$(git status --porcelain)" || {
  printf 'the release checkout is not clean\n' >&2
  exit 1
}
[[ "$draft_receipt_root" == /* && "$receipt_root" == /* ]] || {
  printf 'DRAFT_RECEIPT_DIR and PUBLICATION_RECEIPT_DIR must be absolute paths\n' >&2
  exit 1
}
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
