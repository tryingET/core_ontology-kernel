---
ont:
  id: "core.rel.precedes"
  type: relation
  labels: ["precedes"]
  description: "X kommt vor Y (zeitlich/logisch)"
  group: "sequence"
  inverse: "follows"
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
