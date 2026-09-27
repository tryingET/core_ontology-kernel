---
ont:
  id: "core.Operations"
  type: concept
  labels: ["operations"]
  synonyms: []
  description: "Doing the work, as distinct from governing it (S3)."
  relations:
    - type: instance_of
      target: core.UfoCategory.Event
  examples:
    - "Running the daily work of a domain"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# operations (core.Operations)

## Definition
Doing the work, as distinct from governing it (S3).

## Common confusions
- MITO operativ is a level and stays German; NASA Phase E is operations mode.

## Category
- UFO event (`core.UfoCategory.Event`). Required: the domain whose work it is.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §4 operations row.
- Vocabulary card: operations [doing the work].
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
