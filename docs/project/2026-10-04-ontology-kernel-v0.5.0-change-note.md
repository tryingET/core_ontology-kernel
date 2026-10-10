---
summary: "Change note for the ontology-kernel v0.5.0 candidate (AK 6659): the holding's shared meaning moves to core, the semantic delta against v0.4.0, and the consumer handoffs."
read_when:
  - "Before repinning a consumer from ontology-kernel v0.4.0 to v0.5.0."
  - "When a holdingco layer or record still uses co.holding.TemplateTopology or co.holding.WorkItemAuthoritySplit."
type: "reference"
task_id: 6659
---

# ontology-kernel v0.5.0 change note

AK 6592 moved the meaning the holding sets for every company from the holdingco company layer into core. The
Holding Owner decided it on 2026-10-03 through the ADR-0008 Core Vorgabe route (class C, AK evidence 13029; the
rewording of the second concept, 13099). No consent round was held because the owner holds both affected layers.
The content landed in PR #15 (merge `1687560`) and, as in-place wording, PR #17 (merge `3493a86`). The owner asked on 2026-10-04 to prepare this release (evidence
13568). The content freeze, the version/OID authorization, the draft and the publication remain the owner's
separate acts. The release follows [docs/release-procedure.md](../release-procedure.md).

## Content

- `core.TemplateTopology` (template topology): the binding structure of the template layers L0, L1 and L2, which
  layer holds authority over a change, which generates which, and how drift is found. Moved from
  `co.holding.TemplateTopology`, meaning unchanged, description translated. `is_a core.Policy`.
- `core.WorkItemAuthoritySplit` (work-item authority split): only an AK task drives execution; direction rows,
  FCOS coordination rows, plans and generated files never do. Moved from `co.holding.WorkItemAuthoritySplit` and
  reworded at the owner's direction, because the old text named an archived L0 work-items scheduler.
  `is_a core.Invariant`, `depends_on core.WorkItem`.

The decision note is
[ontology/decisions/2026-10-03-holding-meaning-to-core.md](../../ontology/decisions/2026-10-03-holding-meaning-to-core.md).
ADR-0008 §1 item 7 states the rule (governance-kernel `00035f9`, `0d7603a`).

## In-place wording (AK 6822, PR #17)

PR #17 (merge `3493a86`) landed after the first candidate `28e34e9` and is part of v0.5.0. It rewords four
existing concepts in S3 v2026 terms and adds vault citations; identifiers, relations and edges are unchanged:

- `core.AgreementReview`: an agreement is, in S3 v2026 terms, a policy; the review checks it against evaluation
  criteria and metrics.
- `core.Concern`, `core.PossibleObjection`, `core.Objection`: the object of an objection or concern is "a proposal,
  existing decision or activity" (was "proposal, agreement or activity").

`rocs diff` does not report description changes, so they are listed here. The reference model
`docs/reference-model/governance-core.md` and the AK 6364 decision packet carry the same wording.

## Semantic delta against v0.4.0

`rocs diff --baseline '<repo:core/ontology-kernel@v0.4.0>' --resolve-refs --workspace-root ~/ai-society --json`
(consumer rocs-cli 0.4.6) exits 0:

- Concepts: 2 added, none removed; 124 → 126.
- Relation types: none added or removed; 13.
- Edges: 5 added, none removed; 132 → 137.
  - `core.TemplateTopology` `is_a` `core.Policy`, `instance_of` `core.UfoCategory.NormativeDescription`;
  - `core.WorkItemAuthoritySplit` `is_a` `core.Invariant`, `depends_on` `core.WorkItem`, `instance_of`
    `core.UfoCategory.NormativeDescription`.
- No deprecations.

Added concepts and edges make this a minor version under [RELEASING.md](../../RELEASING.md). This prep sets
`ontology/manifest.yaml` to `0.5.0`.

## Consumers

- Consumers that pin `<repo:core/ontology-kernel@main>` already read both concepts; their own checks pass
  (holdingco/agents and holdingco/fcos-control-board checked on 2026-10-03).
- The holdingco company layer still defines `co.holding.TemplateTopology` and `co.holding.WorkItemAuthoritySplit`
  until decision 168's fold (AK 6274) records both in its removed-identifiers list with the core identifiers as
  replacements. Until then both layers carry the labels; rocs reports no error for that.
- After publication, consumers repin per the standing owner decision AK 6288 (release procedure §6). The v0.4.0
  repin is running as AK 6648.

## What this release does not claim

- It does not retire the holdingco identifiers; decision 168's fold does that.
- It does not change any other core concept, relation type or edge.
- It is not a published Release until the owner's publication authority names the numeric draft.
