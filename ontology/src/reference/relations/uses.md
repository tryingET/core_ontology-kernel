---
ont:
  id: "core.rel.uses"
  type: relation
  labels: ["uses"]
  description: "X nutzt Y (Implementations-/Betriebsbezug)"
  group: "usage"
  inverse: "used_by"
  characteristics:
    transitive: false
    symmetric: false
  axis_default: "<parents|children|left|right|previous|next>"
examples:
  - "<positive example>"
anti_examples:
  - "<common misuse example>"
---

## Notes
- Keep semantics crisp.
- Do not overload one relation with multiple meanings (Lucidity).
