---
ont:
  id: "core.WorkProductInspection"
  type: concept
  labels: ["work-product inspection"]
  synonyms: []
  description: "A structured examination of a work product by people other than its author, to find defects."
  relations:
    - type: instance_of
      target: core.UfoCategory.Event
  examples:
    - "Two reviewers reading an RFC line by line for defects"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# work-product inspection (core.WorkProductInspection)

## Definition
A structured examination of a work product by people other than its author, to find defects.

## Common confusions
- 'Review' is never bare.

## Category
- UFO event (`core.UfoCategory.Event`). Required: the work product and inspectors other than its author.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §4 review row.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
