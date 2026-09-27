---
ont:
  id: "core.PlanFigures"
  type: concept
  labels: ["plan figures"]
  synonyms: ["MITO Soll"]
  description: "The planned values, fixed in the Input segment, that Output measures actual results against (MITO Soll)."
  relations: []
  examples:
    - "A planned median of two days from task claim to close"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# plan figures (core.PlanFigures)

## Definition
The planned values, fixed in the Input segment, that Output measures actual results against (MITO Soll).

## Typical usage
- A few tracked parameters with a planned profile (NASA's technical performance measures).

## Common confusions
- 'Baseline' is never bare: plan figures are neither a commitment baseline nor the FCOS freshness baseline.

## Source and mapping
- MITO model definition: Input fixes the plan figures that Output measures against; Combination strategy §3 spine row 7; Combination strategy §4 baseline row.
- MITO model definition: governance-kernel `docs/core/definitions/mito-model.md`.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
