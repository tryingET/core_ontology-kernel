---
ont:
  id: "core.rel.produces"
  type: relation
  labels: ["produces"]
  description: "X erzeugt/führt zu Y (Outcome/Result)"
  group: "outcome"
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
