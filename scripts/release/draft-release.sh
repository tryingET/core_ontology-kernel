#!/usr/bin/env bash
# Draft one immutable ontology-kernel GitHub Release. This is the completed
# v0.2.0 draft block of RELEASING.md with the version as input, derived title
# and body, and the versioning-rule checks; docs/release-procedure.md lists
# every difference. Running it grants nothing: it needs a draft authority.
set -euo pipefail
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../.."

release_oid="${RELEASE_OID:?set the authorized full release commit OID}"
receipt_root="${DRAFT_RECEIPT_DIR:?set a new durable task-owned draft receipt directory}"
draft_authority="${DRAFT_AUTHORITY:?set the exact AK draft authority reference}"
tag_name="${RELEASE_VERSION:?set the authorized release version, such as v0.3.0}"
[[ "$tag_name" =~ ^v(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$ ]]
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
release_title="ontology-kernel $tag_name"
printf -v release_body \
  'Immutable ontology-kernel %s release.\n\nRelease commit: `%s`.\n' \
  "$tag_name" "$release_oid"
release_body_sha256=$(printf '%s' "$release_body" | sha256sum | awk '{print $1}')
[[ "$release_body_sha256" =~ ^[0-9a-f]{64}$ ]]
[[ "$release_oid" =~ ^[0-9a-f]{40}$ ]]
test "$(git rev-parse --verify 'HEAD^{commit}')" = "$release_oid"
# Versioning rule (RELEASING.md): the tag is "v" plus the manifest version, and
# no existing destination tag carries this ontology tree. A tag object missing
# from this checkout fails closed; fetch the destination's tags first.
manifest_version=$(sed -n 's/^  version: "\(.*\)"$/\1/p' ontology/manifest.yaml)
test "v$manifest_version" = "$tag_name" || {
  printf 'manifest version %s does not match %s\n' "$manifest_version" "$tag_name" >&2
  exit 1
}
release_tree=$(git rev-parse --verify 'HEAD:ontology')
remote_tags=$(git ls-remote --tags "${urls[0]}" 'refs/tags/v*')
while read -r tagged_oid tagged_ref; do
  test -n "$tagged_oid" || continue
  tagged_tree=$(git rev-parse --verify "${tagged_oid}^{commit}:ontology") || {
    printf 'fetch tags first: %s (%s) is absent here\n' "$tagged_ref" "$tagged_oid" >&2
    exit 1
  }
  test "$tagged_tree" != "$release_tree" || {
    printf 'ontology tree %s is already tagged by %s\n' "$release_tree" "$tagged_ref" >&2
    exit 1
  }
done <<<"$remote_tags"
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
