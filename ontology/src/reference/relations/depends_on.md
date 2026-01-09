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
  axis_default: "<parents|children|left|right|previous|next>"
examples:
  - "<positive example>"
anti_examples:
  - "<common misuse example>"
---

## Notes
- Keep semantics crisp.
- Do not overload one relation with multiple meanings (Lucidity).
