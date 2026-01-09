---
ont:
  id: "core.rel.is_a"
  type: relation
  labels: ["is_a"]
  description: "Untertyp/Unterklasse → Obertyp/Oberklasse"
  group: "taxonomy"
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
