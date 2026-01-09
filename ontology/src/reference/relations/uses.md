---
ont:
  id: "core.rel.uses"
  type: relation
  labels: ["uses"]
  description: "X nutzt Y (Implementations-/Betriebsbezug)"
  group: "usage"
  characteristics:
    transitive: false
    symmetric: false
  axis_default: "children"
examples:
  - "core.Service uses core.IntegrationEdge"
anti_examples:
  - "Using uses for mandatory requirement (use `depends_on`)"
---

## Notes
- Keep semantics crisp.
- Do not overload one relation with multiple meanings (Lucidity).

## Use when
- X uses Y as part of its implementation/operation (not necessarily required).

## Do not use when
- You mean a strict requirement (use `depends_on`) or containment (use `part_of`).

## Domain / Range
- Domain: user system/process
- Range: used system/component
