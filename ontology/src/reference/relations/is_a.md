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
  axis_default: "parents"
examples:
  - "core.Agent is_a core.Actor"
anti_examples:
  - "Using is_a for instances/values (use `instance_of`)"
---

## Notes
- Keep semantics crisp.
- Do not overload one relation with multiple meanings (Lucidity).

## Use when
- X is a subtype/specialization of Y (inherits meaning/constraints).

## Do not use when
- You mean instance/value membership (use `instance_of`) or part-whole (use `part_of`).

## Domain / Range
- Domain: subtype concept
- Range: supertype concept
