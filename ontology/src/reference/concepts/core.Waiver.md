---
ont:
  id: "core.Waiver"
  type: concept
  labels: ["waiver"]
  synonyms: []
  description: "Relief from meeting a requirement that leaves the commitment unchanged: the item is released, and the requirement stays as agreed."
  relations:
    - type: is_a
      target: core.Relief
    - type: instance_of
      target: core.UfoCategory.Situation
  examples:
    - "A requirement's waiver authority releases one release from a test requirement; the requirement stays"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# waiver (core.Waiver)

## Definition
Relief from meeting a requirement that leaves the commitment unchanged: the item is released, and the requirement stays as agreed.

## Typical usage
- Granted by the requirement's waiver authority; waivers expire.

## Common confusions
- Not a change: changing the commitment goes through change control.
- NASA calls a waiver both 'a documented agreement' (handbook p. 149) and 'a documented authorization' (glossary p. 196); in AI Society it is granted, not agreed.

## Category
- UFO situation (`core.UfoCategory.Situation`). Required: the requirement, its waiver authority, scope, expiry.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §3, §4, §5 (waiver ≠ change).
- Findings register N-1.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
