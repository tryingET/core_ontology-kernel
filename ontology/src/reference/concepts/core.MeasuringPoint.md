---
ont:
  id: "core.MeasuringPoint"
  type: concept
  labels: ["measuring point"]
  synonyms: ["Binner Gates"]
  description: "A defined point in a process where a metric is measured and compared with its plan figure; it measures and does not decide."
  relations:
    - type: uses
      target: core.Metric
  examples:
    - "Counting reopened tasks at the close step and comparing the count with its plan figure"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# measuring point (core.MeasuringPoint)

## Definition
A defined point in a process where a metric is measured and compared with its plan figure; it measures and does not decide.

## Typical usage
- Measuring points feed the Output segment; a threshold names the action it triggers.

## Common confusions
- Not a decision gate: a measuring point measures, a decision gate is an act of a named authority. Merging the two was one of proposal rev 2's errors.

## Source and mapping
- Combination strategy §3 and §4: Binner's 'Gates' → measuring point (B1 p. 244).
- B1 = Binner, *Organisation 4.0 – MITO-Konfigurationsmanagement* (2018); B2 = Binner, *Ganzheitliche Businessmodell-Transformation* (2020); printed pages.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
