---
ont:
  id: "core.rel.conflicts_with"
  type: relation
  labels: ["conflicts_with"]
  description: "X steht im Konflikt/Widerspruch zu Y"
  group: "opposition"
  inverse: "conflicts_with"
  characteristics:
    transitive: false
    symmetric: true
  axis_default: "<parents|children|left|right|previous|next>"
examples:
  - "<positive example>"
anti_examples:
  - "<common misuse example>"
---

## Notes
- Keep semantics crisp.
- Do not overload one relation with multiple meanings (Lucidity).
