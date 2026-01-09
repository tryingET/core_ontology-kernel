---
ont:
  id: "core.rel.part_of"
  type: relation
  labels: ["part_of"]
  description: "Teil → Ganzes"
  group: "mereology"
  inverse: "has_part"
  characteristics:
    transitive: true
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
