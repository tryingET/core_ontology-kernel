---
ont:
  id: "core.AgreementReview"
  type: concept
  labels: ["agreement review"]
  synonyms: []
  description: "A scheduled review of an agreement against its evaluation criteria, ending in keep, evolve or drop (S3)."
  relations:
    - type: instance_of
      target: core.UfoCategory.Event
  examples:
    - "Reviewing a domain agreement on its review date: keep, evolve or drop"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# agreement review (core.AgreementReview)

## Definition
A scheduled review of an agreement against its evaluation criteria, ending in keep, evolve or drop (S3).

## Common confusions
- 'Review' is never bare.

## Category
- UFO event (`core.UfoCategory.Event`). Required: the agreement, its evaluation criteria, the review date.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §4 review row; Combination strategy §5 (S3 keep / evolve / drop).
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
