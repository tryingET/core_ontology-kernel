---
ont:
  id: "core.rel.depends_on"
  type: relation
  labels: ["depends_on"]
  description: "X benötigt Y, um korrekt zu funktionieren"
  group: "dependency"
  characteristics:
    transitive: false
    symmetric: false
  axis_default: "parents"
examples:
  - "core.Service depends_on core.IntegrationEdge (service needs an external integration)"
anti_examples:
  - "Using depends_on for mere 'uses' relationships"
---

## Notes
- Keep semantics crisp.
- Do not overload one relation with multiple meanings (Lucidity).

## Use when
- X requires Y to function correctly (runtime, build, or operational requirement).

## Do not use when
- X just uses Y optionally or incidentally (use `uses`), or X is a part of Y (use `part_of`).

## Domain / Range
- Domain: any system element (`core.Service`, `core.Pipeline`, `core.Repo`)
- Range: required element (`core.Service`, `core.IntegrationEdge`, `core.Policy`, etc)
