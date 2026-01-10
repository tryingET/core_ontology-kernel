---
ont:
  id: "core.rel.produces"
  type: relation
  labels: ["produces"]
  description: "X erzeugt/führt zu Y (Outcome/Result)"
  group: "outcome"
  characteristics:
    transitive: false
    symmetric: false
  axis_default: "children"
examples:
  - "core.Pipeline produces core.Release"
anti_examples:
  - "Using produces for ordering without outcome (use `precedes`)"
---

## Definition
`X produces Y` means X yields/creates Y as an outcome (artifact/state/result), not merely an ordering.

## Notes
- Keep semantics crisp.
- Do not overload one relation with multiple meanings (Lucidity).

## Use when
- X yields/creates Y as an outcome/artifact/state.

## Do not use when
- You mean dependency without a produced artifact/state (use `depends_on`).

## Domain / Range
- Domain: producer process/system
- Range: produced artifact/state
