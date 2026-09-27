---
ont:
  id: "core.Action"
  type: concept
  labels: ["action"]
  synonyms: ["Binner Maßnahme"]
  description: "A step chosen to reach a goal, with an owner and a date (Binner's Maßnahme); in AI Society it is carried out as AK tasks."
  relations: []
  examples:
    - "Put the decided words into the ontology kernel, with an owner and a date"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# action (core.Action)

## Definition
A step chosen to reach a goal, with an owner and a date (Binner's Maßnahme); in AI Society it is carried out as AK tasks.

## Typical usage
- The cascade need → goal → action → metric → to-do gives every action an owner and a date.

## Common confusions
- 'Measure' is never bare: a Maßnahme is an action, a Kennzahl is a metric.

## Source and mapping
- Combination strategy §3 spine row 9; Combination strategy §4 measure row; Combination strategy §5 cascade.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
