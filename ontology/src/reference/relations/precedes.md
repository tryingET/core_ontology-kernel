---
ont:
  id: "core.rel.precedes"
  type: relation
  labels: ["precedes"]
  description: "X kommt vor Y (zeitlich/logisch)"
  group: "sequence"
  characteristics:
    transitive: false
    symmetric: false
  axis_default: "left"
examples:
  - "core.Policy precedes core.Release (policy approval happens before release)"
anti_examples:
  - "Using precedes for dependency (use `depends_on`)"
---

## Notes
- Keep semantics crisp.
- Do not overload one relation with multiple meanings (Lucidity).

## Use when
- Ordering matters (time or logical sequence) between X and Y.

## Do not use when
- You mean part-of containment or a hard requirement (use `part_of` / `depends_on`).

## Domain / Range
- Domain: earlier step/event/state concept
- Range: later step/event/state concept
