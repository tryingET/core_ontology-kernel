---
summary: "Release procedure for ontology-kernel versions after v0.2.0: the authorities each release needs, the checks at the exact commit, and the draft and publication scripts derived from the completed v0.2.0 commands."
read_when:
  - "Before preparing, drafting or publishing any ontology-kernel release after v0.2.0."
  - "When checking a proposed kernel tag against the versioning rule."
  - "When checking scripts/release/ against the v0.2.0 commands in RELEASING.md."
type: "reference"
---

# Release procedure after v0.2.0

This document grants nothing. Each release needs these records in AK:
- the task that carries it;
- the Holding Owner's authorization naming the version and the full release commit OID. Until the
  stewardship handover, kernel versions are the owner's, and publishing on GitHub is class C
  (ADR-0008 §4);
- a draft authority;
- a separate publication authority that names the numeric draft ID.

The release contract and the versioning rule are in [RELEASING.md](../RELEASING.md). The only
destination is `https://github.com/tryingET/core_ontology-kernel.git`. Remote aliases are not
destinations.

## 1. Content

1. The holder of the core layer declares a content freeze on `main`, recorded as evidence on the
   release task. While it holds, `ontology/` changes only through the release's own PRs.
2. A prep PR sets `ontology/manifest.yaml` `version` to the version without the leading `v`. It
   also adds a change note, `docs/project/<date>-ontology-kernel-<version>-change-note.md`, with:
   - the output of `rocs diff` against the previous Release:
     ```bash
     uv --project ~/ai-society/core/rocs-cli run --frozen rocs diff --repo . \
       --baseline '<repo:core/ontology-kernel@<previous-version>>' \
       --resolve-refs --workspace-root ~/ai-society --json
     ```
   - every deprecation with its successors and decision note, because `rocs diff` does not report
     status changes;
   - what the release does not claim.
3. The prep PR's merge commit on `main` is the release commit candidate.

## 2. Checks at the exact commit

Run these in a fresh clone checked out at the full OID, not in the shared workspace checkout:

```bash
set -euo pipefail
test "$(git rev-parse --verify 'HEAD^{commit}')" = "${RELEASE_OID:?}"
env -u ROCS_REPO -u ROCS_WORKSPACE_ROOT -u ROCS_WORKSPACE_REF_MODE \
  ROCS_CI_PROFILE=main-strict ./scripts/ci/full.sh
node ~/ai-society/core/agent-scripts/scripts/docs-list.mjs --docs docs --strict
uv --project ~/ai-society/core/rocs-cli run --frozen rocs validate --repo . --json \
  --resolve-refs --workspace-ref-mode strict
test -z "$(git status --porcelain)"
```

- `full.sh` runs the vendored ROCS. The workspace rocs-cli is what consumers run, so both must pass.
- Every consumer layer that the release task names must validate against the release commit.
- The hosted `validate` workflow corroborates the commit. It does not replace these local checks.

Record the commands, exit codes and the corpus digest on the release task.

## 3. Destination and settings

- `git ls-remote --exit-code https://github.com/tryingET/core_ontology-kernel.git
  refs/heads/main` must return the release OID.
- The owner records a current receipt that **Settings → General → Releases → Enable release
  immutability** is on: repository, control state, actor, UTC time and where it is recorded.
  - When the token can read it, corroborate the receipt with
    `gh api repos/tryingET/core_ontology-kernel/immutable-releases` returning `enabled: true`.
  - On 2026-09-28 that call returned 403. When it does, the owner receipt stands alone and the
    draft and published readbacks prove the rest.
- Every actor or automation that can write tags or Releases stays quiet from the draft's absence
  checks through the post-publication verification. GitHub offers no compare-and-swap between a
  check and a publish, so the publication authority must accept that residual race.

## 4. Draft

Run under the draft authority only, from the clean checkout. Fetch the destination's tags first,
because the versioning check fails closed on a tag object this clone lacks.

```bash
git fetch --tags https://github.com/tryingET/core_ontology-kernel.git
RELEASE_VERSION=vX.Y.Z RELEASE_OID=<full OID> DRAFT_RECEIPT_DIR=<new durable directory> \
DRAFT_AUTHORITY=<AK reference> DESTINATION_IMMUTABILITY_RECEIPT=<owner receipt reference> \
  scripts/release/draft-release.sh
```

The script then:
- checks the versioning rule;
- checks push permission, that destination `main` equals the release OID, and that the tag and
  every Release for it are absent;
- creates exactly one draft with a fixed title and body and no assets;
- keeps the raw and normalized responses in the receipt directory.

A failed call is effect-indeterminate. Read the destination's state and never retry mechanically;
RELEASING.md's draft contract applies.

## 5. Publication

The publication authority names:
- the version, the full OID and the destination URL;
- the numeric draft ID;
- the expected title and body digest, and the empty asset set;
- the setting receipts and the acceptance of the residual race;
- the forward-only recovery boundary.

Then:

```bash
RELEASE_VERSION=vX.Y.Z RELEASE_OID=<full OID> DRAFT_RECEIPT_DIR=<draft receipt directory> \
PUBLICATION_RECEIPT_DIR=<new directory> PUBLICATION_AUTHORITY=<AK reference> \
DESTINATION_DRAFT_ID=<numeric id> DESTINATION_IMMUTABILITY_RECEIPT=<owner receipt reference> \
  scripts/release/publish-release.sh
```

The script:
- verifies the draft again and publishes it once;
- verifies `immutable: true`, the exact tag and OID, the commit handoff observation, and
  `gh release verify`.

If anything fails, follow RELEASING.md's preserved partial-publication and forward-recovery
contract, with the version substituted. Never move, delete or re-create a published tag.

## 6. After publication

- Record the Release ID, `immutable: true`, the tag and the OID on the release task.
- Consumers repin through their own tasks, the named first consumer first (ADR-0008 §7: admit
  above, cut the version, consumers repin, deprecate below).
- Refresh `docs/project/product_posture.md`.
- The holder of the core layer lifts the content freeze.

## How the scripts relate to the v0.2.0 commands

`scripts/release/draft-release.sh` and `scripts/release/publish-release.sh` start from the two
command blocks in RELEASING.md. Those blocks are byte-identical to the text executed at the
immutable tag `v0.2.0`. These are the only changes:

- a shebang and a header comment;
- the script changes to its own checkout's root first;
- the version comes from `RELEASE_VERSION` in the form `vMAJOR.MINOR.PATCH`, and the title and body
  derive from it. With `RELEASE_VERSION=v0.2.0` they reproduce the v0.2.0 title and body byte for
  byte;
- both scripts check that `ontology/manifest.yaml` `version` equals the version without `v`;
- the draft script also checks that no destination tag carries the release commit's `ontology/`
  tree. The publication script skips this check, because by then the draft may already have
  created the new tag.

Check that list against the preserved blocks:

```bash
block() { awk -v n="$1" '/^```bash/{c++; if(c==n){p=1; next}} /^```$/{p=0} p' RELEASING.md; }
diff <(block 1) scripts/release/draft-release.sh
diff <(block 2) scripts/release/publish-release.sh
```
