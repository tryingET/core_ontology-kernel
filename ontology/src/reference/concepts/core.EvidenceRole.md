---
ont:
  id: "core.EvidenceRole"
  type: concept
  labels: ["evidence"]
  synonyms: []
  description: "The role a record plays when it is offered in support of, or against, a claim; the same record can be evidence for one claim and not for another."
  relations:
    - type: instance_of
      target: core.UfoCategory.Role
    - type: depends_on
      target: core.RetainedArtefact
  examples:
    - "A test-run log referenced by digest from a review record"
  anti_examples:
    - "An assertion repeated without a checkable source"
    - "A retained archive that no claim cites (a retained artefact, not yet evidence)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# evidence (core.EvidenceRole)

## Definition
The role a record plays when it is offered in support of, or against, a claim; the same record can be evidence for one claim and not for another.

## Common confusions
- Confused with proof: evidence supports or falsifies a claim under declared criteria; it does not settle it.
- Played by records of different kinds (in UFO a role mixin).

## Category
- UFO role (`core.UfoCategory.Role`). Required: the record, the claim it is offered for or against, who offered it.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Split from core.Evidence, which mixed the role with the record category (decision note below).
- Decision note: `ontology/decisions/2026-09-27-governance-core-splits.md`.

Admitted: AK task 5987, 2026-09-27
