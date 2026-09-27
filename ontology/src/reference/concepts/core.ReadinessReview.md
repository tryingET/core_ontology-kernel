---
ont:
  id: "core.ReadinessReview"
  type: concept
  labels: ["readiness review"]
  synonyms: []
  description: "A decision gate that checks, against criteria set in advance, whether an item is ready for its next step."
  relations:
    - type: is_a
      target: core.DecisionGate
  examples:
    - "Checking, against criteria set in advance, that a migration may start"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# readiness review (core.ReadinessReview)

## Definition
A decision gate that checks, against criteria set in advance, whether an item is ready for its next step.

## Common confusions
- 'Review' is never bare.

## Source and mapping
- Combination strategy §4 review row; Combination strategy §5: one of four review archetypes kept from NASA.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
