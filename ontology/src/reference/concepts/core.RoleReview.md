---
ont:
  id: "core.RoleReview"
  type: concept
  labels: ["role review"]
  synonyms: []
  description: "A review of how someone performs a role, by the people they work with (S3 peer review)."
  relations:
    - type: instance_of
      target: core.UfoCategory.Event
  examples:
    - "Colleagues giving feedback to the holder of a steward role"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# role review (core.RoleReview)

## Definition
A review of how someone performs a role, by the people they work with (S3 peer review).

## Common confusions
- 'Review' is never bare.

## Category
- UFO event (`core.UfoCategory.Event`). Required: the role, its holder, the reviewers.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §4 review row: role review (S3 peer review).
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
