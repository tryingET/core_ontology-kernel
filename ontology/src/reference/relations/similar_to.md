---
ont:
  id: "core.rel.similar_to"
  type: relation
  labels: ["similar_to"]
  description: "X ist ähnlich/benachbart zu Y (keine Subtyp- oder Teil-Beziehung)"
  group: "similarity"
  inverse: "similar_to"
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
