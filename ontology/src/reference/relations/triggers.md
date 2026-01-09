---
ont:
  id: "core.rel.triggers"
  type: relation
  labels: ["triggers"]
  description: "X löst Y aus (Trigger → Effect)"
  group: "causality"
  inverse: "triggered_by"
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
