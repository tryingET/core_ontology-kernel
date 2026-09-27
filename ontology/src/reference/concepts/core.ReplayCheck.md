---
ont:
  id: "core.ReplayCheck"
  type: concept
  labels: ["replay check"]
  synonyms: ["replay"]
  description: "An integrity re-run: a recorded, deterministic operation is repeated and its result compared with the recorded one."
  relations: []
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

## Source and mapping
- Combination strategy §4 verification row: replay → replay check; Combination strategy §1 principle 6.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
