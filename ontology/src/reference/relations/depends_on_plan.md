---
ont:
  id: "core.rel.depends_on_plan"
  type: relation
  labels: ["depends_on_plan"]
  description: "X should be done after Y to reduce risk / unblock progress (planning dependency)."
  group: "planning"
  characteristics:
    transitive: false
    symmetric: false
  axis_default: "parents"
examples:
  - "core.WorkItem depends_on_plan core.WorkItem (issue A depends on issue B)"
  - "core.Milestone depends_on_plan core.Milestone (milestone ordering dependency)"
anti_examples:
  - "Using depends_on_plan for runtime/build requirements (use `core.rel.depends_on`)"
---

## Definition
`X depends_on_plan Y` means Y should be completed first so X can be executed with lower risk / higher clarity.

## Notes
- Planning dependency only (work sequencing), not runtime/build/operational requirements.
- Keep semantics crisp; prefer `core.rel.precedes` for pure ordering without an "unblocks" implication.

## Use when
- You want to express "do Y first, then X" in a planning/tracking context (issues, milestones, programs).

## Do not use when
- X requires Y to function correctly at runtime/build time (use `core.rel.depends_on`).

## Domain / Range
- Domain: planning element (`core.WorkItem`, `core.Milestone`, `core.Program`)
- Range: prerequisite planning element (`core.WorkItem`, `core.Milestone`, `core.Program`)

