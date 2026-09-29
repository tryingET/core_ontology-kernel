---
ont:
  id: "core.MitoSegment.Input"
  type: concept
  labels: ["Input segment"]
  synonyms: ["Input", "plan", "PDCA Plan"]
  description: "The second MITO segment (PDCA Plan): it provides resources, competence and information, plans the processes, and fixes the plan figures that Output measures against."
  relations:
    - type: instance_of
      target: core.MitoSegment
    - type: precedes
      target: core.MitoSegment.Transformation
  examples:
    - "Allocating resources and fixing the plan figures for the next release"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Input segment (core.MitoSegment.Input)

## Definition
The second MITO segment (PDCA Plan): it provides resources, competence and information, plans the processes, and fixes the plan figures that Output measures against.

## Typical usage
- In our own text, bare 'plan' means this segment; NASA's plans are named by their kind (for example 'verification plan').

## Common confusions
- Input is not goal-setting; goals belong to Führung (B1 p. 372).
- Not input in the data-flow sense; use the qualified label.

## Source and mapping
- MITO model definition: segment table (B1 pp. 57–59, 372).
- Combination strategy §4: plan = the MITO Input/Plan segment.
- B1 = Binner, *Organisation 4.0 – MITO-Konfigurationsmanagement* (2018); B2 = Binner, *Ganzheitliche Businessmodell-Transformation* (2020); printed pages.
- MITO model definition: governance-kernel `docs/core/definitions/mito-model.md`.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
