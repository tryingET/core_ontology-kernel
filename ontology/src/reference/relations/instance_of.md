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
  axis_default: "parents"
examples:
  - "core.DataClass.Public instance_of core.DataClassification"
anti_examples:
  - "Using instance_of where taxonomy/subtype is intended (use `is_a`)"
---

## Notes
- Keep semantics crisp.
- Do not overload one relation with multiple meanings (Lucidity).

## Use when
- You are modeling a concrete instance/value of a class-like concept.

## Do not use when
- You mean subtype/category (use `is_a`) or part-whole (use `part_of`).

## Domain / Range
- Domain: instance/value concept
- Range: class-like concept
