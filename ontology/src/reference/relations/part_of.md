---
ont:
  id: "core.rel.part_of"
  type: relation
  labels: ["part_of"]
  description: "Teil → Ganzes"
  group: "mereology"
  characteristics:
    transitive: true
    symmetric: false
  axis_default: "parents"
examples:
  - "core.IntegrationEdge part_of core.Service (integration is part of a service boundary)"
anti_examples:
  - "Using part_of when you mean depends_on"
---

## Definition
`X part_of Y` means X is a component/contained part of Y (mereology/containment), not just a dependency.

## Notes
- Keep semantics crisp.
- Do not overload one relation with multiple meanings (Lucidity).

## Use when
- X is a component of Y (mereology / containment).

## Do not use when
- X just interacts with Y (use `uses`) or requires Y (use `depends_on`).

## Domain / Range
- Domain: component concept
- Range: whole concept
