---
ont:
  id: "core.MitoSegment.Transformation"
  type: concept
  labels: ["Transformation segment"]
  synonyms: ["Transformation", "Do"]
  description: "The third MITO segment (Do): the core value-creating work, steered by the process owners."
  relations:
    - type: instance_of
      target: core.MitoSegment
    - type: precedes
      target: core.MitoSegment.Output
  examples:
    - "An agent session carrying out a claimed AK task"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Transformation segment (core.MitoSegment.Transformation)

## Definition
The third MITO segment (Do): the core value-creating work, steered by the process owners.

## Typical usage
- Actions are carried out here; in AI Society the work happens in AK tasks.

## Common confusions
- Not a data transformation; use the qualified label.

## Source and mapping
- MITO model definition: segment table (B1 pp. 57–59); Combination strategy §3 spine row 9.
- B1 = Binner, *Organisation 4.0 – MITO-Konfigurationsmanagement* (2018); B2 = Binner, *Ganzheitliche Businessmodell-Transformation* (2020); printed pages.
- MITO model definition: governance-kernel `docs/core/definitions/mito-model.md`.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
