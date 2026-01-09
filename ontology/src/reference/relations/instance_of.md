---
ont:
  id: "core.rel.instance_of"
  type: relation
  labels: ["instance_of"]
  description: "Instanz → Klasse"
  group: "classification"
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
