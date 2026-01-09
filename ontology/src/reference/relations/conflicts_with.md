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
  axis_default: "left"
examples:
  - "core.Policy conflicts_with core.Policy (two rules cannot both hold for the same scope)"
anti_examples:
  - "Using conflicts_with to express similarity (use `similar_to`)"
---

## Notes
- Keep semantics crisp.
- Do not overload one relation with multiple meanings (Lucidity).

## Use when
- Two statements/constraints cannot both be satisfied in the same scope.

## Do not use when
- You mean tradeoff/choice history (track in decisions) or simple difference without contradiction.

## Domain / Range
- Domain: policies/constraints/invariants
- Range: policies/constraints/invariants
