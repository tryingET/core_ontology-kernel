---
ont:
  id: "core.Handover"
  type: concept
  labels: ["handover"]
  synonyms: ["NASA product transition"]
  description: "Passing a finished product to its receiver, together with what the receiver needs to use it."
  relations:
    - type: instance_of
      target: core.UfoCategory.Event
  examples:
    - "Delivering a finished skill to its users together with its install notes"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# handover (core.Handover)

## Definition
Passing a finished product to its receiver, together with what the receiver needs to use it.

## Common confusions
- Not FCOS 'transition', which is an authority migration.

## Category
- UFO event (`core.UfoCategory.Event`). Required: the product, who hands it over, the receiver.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §4 transition row: NASA product transition → handover.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
