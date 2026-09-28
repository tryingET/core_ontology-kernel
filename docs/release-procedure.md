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
- the Holding Owner's authorization naming the version and the full release commit OID. Kernel
  versions are the owner's until the stewardship handover, and the stewards' by consent (class B)
  after it. Publishing on GitHub stays the owner's either way (class C, ADR-0008 §4);
- a draft authority;
- a separate publication authority that names the numeric draft ID.

The draft and publication authorities are the Holding Owner's. No session issues one to itself,
and a branch, a passing check or a script run is never one.

The release contract and the versioning rule are in [RELEASING.md](../RELEASING.md). The v0.2.0
preflight, draft, publication and recovery contracts there apply to every later release with the
version substituted. The scripts replace only their command blocks, and the last section lists
every difference. The only destination is `https://github.com/tryingET/core_ontology-kernel.git`.
Remote aliases are not destinations.

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
     `rocs diff` exits 2 when it reports removed concepts, relations or edges. That exit is the
     report, not a failure: the change note carries the removals.
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
- Every consumer layer that the release task names must pass `rocs validate` against the release
  commit.
- The hosted `validate` workflow corroborates the commit. It does not replace these local checks.

Record the commands, exit codes and the corpus digest on the release task.

## 3. Destination and settings

- `git ls-remote --exit-code https://github.com/tryingET/core_ontology-kernel.git
  refs/heads/main` must return the release OID.
- The owner records a current receipt that **Settings → General → Releases → Enable release
  immutability** is on: repository, control state, actor, UTC time and where it is recorded.
- Before the draft, a current read of
  `gh api repos/tryingET/core_ontology-kernel/immutable-releases` must return `enabled: true`.
  - Any other answer stops the release, a 403 included. On 2026-09-28 the workstation's
    fine-grained token got a 403, so the read needs a token with read access to the repository's
    administration settings, such as the owner's own.
  - A draft always reads `immutable: false`, so no draft readback can stand in for this read.
- Every actor or automation that can write tags or Releases stays quiet from the draft's absence
  checks through the post-publication verification. GitHub offers no compare-and-swap between a
  check and a publish, so the publication authority must accept that residual race.

## 4. Draft

Run under the draft authority only, from the clean checkout. Fetch the destination's tags first,
because the versioning check fails closed on a tag commit this clone lacks. Receipt directories are
absolute paths outside the checkout.

```bash
git fetch --tags https://github.com/tryingET/core_ontology-kernel.git
RELEASE_VERSION=vX.Y.Z RELEASE_OID=<full OID> DRAFT_RECEIPT_DIR=<new absolute directory> \
DRAFT_AUTHORITY=<AK reference> DESTINATION_IMMUTABILITY_RECEIPT=<owner receipt reference> \
  scripts/release/draft-release.sh
```

A dry run of either script without authority must put a read-only `gh` guard first on `PATH`: a
shim that refuses every call except `gh api` reads. A dry run is only safe when it cannot write,
whatever the checkout looks like. On 2026-09-28 a guardless dry run created a draft Release (AK
evidence 11307, removed under the operator's authority, 11332).

The script then:
- checks the versioning rule against the release commit, a clean checkout and an absolute receipt
  path;
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
PUBLICATION_RECEIPT_DIR=<new absolute directory> PUBLICATION_AUTHORITY=<AK reference> \
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
  byte. A malformed version stops the script with a message;
- both scripts read `ontology/manifest.yaml` from the release commit, not the working tree, and
  check that its `version` equals the version without `v`;
- both scripts require a clean checkout and absolute receipt directories;
- the draft script also checks two things against every destination `v*` tag:
  - the version is new and above all of them, which keeps the hard-coded `make_latest=true` right;
  - `ontology/` differs from each tagged commit in more than `ontology/manifest.yaml`.

  The publication script skips both checks, because by then the draft may already have created
  the new tag.

Check that list against the preserved blocks:

```bash
block() { awk -v n="$1" '/^```bash/{c++; if(c==n){p=1; next}} /^```$/{p=0} p' RELEASING.md; }
diff <(block 1) scripts/release/draft-release.sh
diff <(block 2) scripts/release/publish-release.sh
```
