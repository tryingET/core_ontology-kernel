---
ont:
  id: "core.Variance"
  type: concept
  labels: ["variance"]
  synonyms: ["deviation", "Soll/Ist variance"]
  description: "The difference between plan figures and actual results (Soll/Ist)."
  relations:
    - type: depends_on
      target: core.PlanFigures
  examples:
    - "Planned 20 admissions, actual 3"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# variance (core.Variance)

## Definition
The difference between plan figures and actual results (Soll/Ist).

## Common confusions
- The word 'deviation' is not used; NASA's deviation is prospective relief, not a variance.

## Source and mapping
- Combination strategy §4 deviation row.
- Vocabulary card: variance [plan figures vs actuals].
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
