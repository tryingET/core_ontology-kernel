---
ont:
  id: "core.ReplayCheck"
  type: concept
  labels: ["replay check"]
  synonyms: ["replay"]
  description: "An integrity re-run: a recorded, deterministic operation is repeated and its result compared with the recorded one."
  relations:
    - type: instance_of
      target: core.UfoCategory.Event
  examples:
    - "Re-running a recorded build and comparing its output digest with the recorded one"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# replay check (core.ReplayCheck)

## Definition
An integrity re-run: a recorded, deterministic operation is repeated and its result compared with the recorded one.

## Common confusions
- Not verification against requirements: a replay check shows that the record reproduces, not that the result is right.

## Category
- UFO event (`core.UfoCategory.Event`). Required: the recorded operation and its recorded result.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §4 verification row: replay → replay check; Combination strategy §1 principle 6.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
