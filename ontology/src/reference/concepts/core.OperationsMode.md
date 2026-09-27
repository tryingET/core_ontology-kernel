---
ont:
  id: "core.OperationsMode"
  type: concept
  labels: ["operations mode"]
  synonyms: ["NASA Phase E"]
  description: "Running a system that is live, where each significant change is a parallel initiative beside ongoing operations (NASA's operations-phase doctrine)."
  relations:
    - type: instance_of
      target: core.UfoCategory.Phase
  examples:
    - "Rolling out a new record schema while the society keeps working"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# operations mode (core.OperationsMode)

## Definition
Running a system that is live, where each significant change is a parallel initiative beside ongoing operations (NASA's operations-phase doctrine).

## Typical usage
- AI Society is always in operations mode; significant changes are coordinated through FCOS.

## Category
- UFO phase (`core.UfoCategory.Phase`). Required: the live system.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §3 operating mode (NASA p. 31, App. T); Combination strategy §4 operations row.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
