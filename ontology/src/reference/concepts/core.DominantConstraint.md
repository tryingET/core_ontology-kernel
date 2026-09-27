---
ont:
  id: "core.DominantConstraint"
  type: concept
  labels: ["dominant constraint"]
  synonyms: ["NASA design driver"]
  description: "The requirement or constraint that shapes a design most strongly (NASA's 'design driver')."
  relations: []
  examples:
    - "The size of an agent's context window, which shapes how records are designed"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# dominant constraint (core.DominantConstraint)

## Definition
The requirement or constraint that shapes a design most strongly (NASA's 'design driver').

## Common confusions
- Not a driver (a situation that calls for a response) and not core.Constraint (an ontology axiom).

## Source and mapping
- Combination strategy §4 driver row.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
