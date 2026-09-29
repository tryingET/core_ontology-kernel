---
summary: "Change note for ontology-kernel v0.3.0 (AK 6167): the semantic delta against v0.2.0 from rocs diff, the five deprecations, the pre-release corrections, what consumers see, and what the release does not claim."
read_when:
  - "Before repinning a consumer from ontology-kernel v0.2.x or @main to v0.3.0."
  - "When checking what v0.3.0 changed, deprecated or corrected."
type: "reference"
task_id: 6167
---

# ontology-kernel v0.3.0 change note

v0.3.0 carries the owner's core vocabulary. AK 6167 is the release task; the scope is AK evidence 11274, the content freeze is 11275, and the procedure is [docs/release-procedure.md](../release-procedure.md). This note describes the content of the prep PR. The release commit is that PR's merge commit, named in the owner's authorization. A version exists only once the Release is published.

## Content

| Source | What | Merge |
|---|---|---|
| AK 6147, PR #2 | core vocabulary batch 1: 54 concepts (authority, MITO structure, governance, commitment and check words) | `4778bd5` |
| AK 5986, PR #3 | the UFO category layer: `core.UfoCategory` and 12 categories, `instance_of` on the governance core, [reference model](../reference-model/governance-core.md) | `21b5dfd` |
| AK 5987, PR #4 | splits of five overloaded concepts; the old identifiers are deprecated, never deleted | `5669a0b` |
| AK 6167, prep PR | pre-release corrections from the independent inspection (AK 6188) and `ontology/manifest.yaml` version `0.3.0` | this PR |

## Semantic delta against v0.2.0

`rocs diff --baseline '<repo:core/ontology-kernel@v0.2.0>' --resolve-refs --workspace-ref-mode strict` (rocs-cli 0.4.5) exits 2, which is its report of removals:

- **Concepts:** 76 added, none removed. 37 → 113.
- **Relation types:** none added or removed (12).
- **Edges:** 94 added, 2 removed. 11 → 103.
  - Added by type: 68 `instance_of`, 6 `precedes`, 6 `produces`, 5 `depends_on`, 4 `is_a`, 3 `uses`, 1 `part_of`, 1 `constrains`.
  - Removed: `core.Authority constrains core.Verification` and `core.Claim precedes core.Verification`. Both were retargeted to `core.VerificationEvent`, so a consumer that walks these edges sees the successor.
- **Corpus:** `rocs validate` reports `sha256:8da179a6c587ef26775b9c881311963baceec0e7a7d4746d98d5c6f50862d7b8` on the prep branch. The release commit's own digest is recorded at the checks.

Under the versioning rule in [RELEASING.md](../../RELEASING.md), added and deprecated concepts and retargeted edges make this a minor version.

## Deprecations

`rocs diff` does not report status changes, so they are listed here. Each deprecated identifier stays resolvable, with `status: deprecated`, `replaced_by` and a decision note (CORE-INV-002).

| Deprecated | Successors | replaced_by |
|---|---|---|
| `core.Verification` | `core.VerificationEvent`, `core.VerificationVerdict` | `core.VerificationEvent` |
| `core.Consent` | `core.ConsentState`, `core.ConsentRound` | `core.ConsentState` |
| `core.Role` | `core.SocialRole`, `core.Permission` | `core.SocialRole` |
| `core.Capability` | `core.ActorCapability`, `core.Permission` | `core.ActorCapability` |
| `core.Evidence` | `core.EvidenceRole`, `core.RetainedArtefact` | `core.EvidenceRole` |

Decision note: `ontology/decisions/2026-09-27-governance-core-splits.md`.

## Pre-release corrections

The independent inspection (AK 6188) found two problems that would have needed new identifiers after an immutable release. The Holding Owner corrected them in place, because none of these identifiers had been released. Decision note: `ontology/decisions/2026-09-28-v0.3.0-pre-release-corrections.md`.

- **`core.VerificationEvent`:** narrowed to a check that a product meets a requirement or a DoD row. Schema and replay checks are not verifications. `core.VerificationVerdict` follows: a verdict is for the requirement or DoD row checked.
- **`core.ArtefactStatus`:** recategorised from UFO phase to UFO quality, with the values approach, preliminary, baseline and update.
- **Synonyms:** aligned with the ADR-0008 data file.
  - Added: 'group outcome' on `core.ConsentState`, 'NASA concurrence' on `core.ConsentRound`.
  - Qualified: 'PDCA Plan', 'PDCA Do' and 'PDCA Check'.
  - Removed: nine extras.

## Consumers

- **Pinned to v0.2.x:** nothing changes until they repin. After repinning, they see the added concepts, the deprecations and the two retargeted edges; every v0.2.0 identifier still resolves. rocs-cli ≥ 0.4.5 is needed, so that a pin keeps resolving to the v0.3.0 tree after `main` moves.
- **Pinned to `@main`:** they have read this content since 2026-09-27, except for the pre-release corrections. The versioning rule asks them to pin the tag.
- **FCOS layer:** `holdingco/fcos-control-board`, the ADR-0008 pilot, is the first consumer. It passes `rocs validate` against this branch (122 concepts, 12 relations, 106 edges); against v0.2.1 it failed with `ONT008 core.VerificationEvent`. Its repin is AK 6190.
- **ADR-0008 data file:** it still lists 'NASA concurrence' under consent and has no PDCA terms. Its holder aligns it in governance-kernel.

## What this release does not claim

- **Conformance:** `rocs validate` proves source-contract, schema and reference conformance for the exact corpus. It does not prove that the meaning is right; the inspection (AK 6188) is the work-product check of that.
- **`ontology/src/system4d.yaml`** is unchanged since v0.2.0. It still names a GitLab edge (`http://192.168.161.10:8929`) and a GitLab contact, both known to be stale because GitLab is retired (AK 6118). The file sits outside the admitted concept corpus, and changing it needs its own contract.
- **Known findings not fixed in this version** (AK 6188, non-blocking):
  - N3–N11 (evidence 11287–11295): Waiver as a subtype of Relief, the Receipt and RetainedArtefact overlap, a shared UFO example, two sets of objection dispositions, implied edges that are missing, card words in kernel prose, the OperationsMode definition, the deprecated concepts listed under Open, and MITO segment and level fields.
  - The `secret` synonym shared by `core.DataClass.SecretData` and `core.Secret`, present since v0.2.0.
  - The 10 governance-core concepts that the reference model leaves without a category.
- **No adoption claim:** a consumer adopts v0.3.0 only when its own owner records the pin and a passing check.
