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
  axis_default: "left"
examples:
  - "core.Debt similar_to core.Exception (both represent intentional deviation from ideal state)"
anti_examples:
  - "Using similar_to for subtype (use `is_a`) or containment (use `part_of`)"
---

## Definition
`X similar_to Y` means X and Y are analogous/adjacent concepts without implying subtype, part, or instance semantics.

## Notes
- Keep semantics crisp.
- Do not overload one relation with multiple meanings (Lucidity).

## Use when
- Two concepts are adjacent/analogous, but neither is a subtype/part/instance of the other.

## Do not use when
- You can express a stronger relation like `is_a`, `part_of`, or `depends_on`.

## Domain / Range
- Domain: concept
- Range: concept
