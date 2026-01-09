---
ont:
  id: "core.rel.constrains"
  type: relation
  labels: ["constrains"]
  description: "Axiom/Constraint begrenzt oder gilt für X"
  group: "constraint"
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
