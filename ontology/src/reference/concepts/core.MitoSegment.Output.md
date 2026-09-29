---
ont:
  id: "core.MitoSegment.Output"
  type: concept
  labels: ["Output segment"]
  synonyms: ["Output", "PDCA Check"]
  description: "The fourth MITO segment (PDCA Check): it measures results against the plan figures and factual goals, that is efficiency, 'doing the things right'."
  relations:
    - type: instance_of
      target: core.MitoSegment
    - type: precedes
      target: core.MitoSegment.Leitung
  examples:
    - "Comparing this month's measured cycle time with its plan figure"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Output segment (core.MitoSegment.Output)

## Definition
The fourth MITO segment (PDCA Check): it measures results against the plan figures and factual goals, that is efficiency, 'doing the things right'.

## Typical usage
- Measuring points and verification feed this segment.

## Common confusions
- Output checks efficiency; Leitung checks effectiveness (B1 pp. 33, 221–222, 553).
- Not output in the data-flow sense; use the qualified label.

## Source and mapping
- MITO model definition: segment table and 'Two checks'.
- MITO model definition: governance-kernel `docs/core/definitions/mito-model.md`.

Admitted: AK task 6147, 2026-09-27
