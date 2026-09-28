---
ont:
  id: "core.MitoLevel.Operativ"
  type: concept
  labels: ["operativ"]
  synonyms: []
  description: "The lowest MITO level: the work-system processes (Arbeitssystemprozesse), done by the process staff; in AI Society an agent session executing a claimed task."
  relations:
    - type: instance_of
      target: core.MitoLevel
  examples:
    - "An agent session executing its claimed task"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# operativ (core.MitoLevel.Operativ)

## Definition
The lowest MITO level: the work-system processes (Arbeitssystemprozesse), done by the process staff; in AI Society an agent session executing a claimed task.

## Common confusions
- Not operations (doing the work, S3) and not operations mode (NASA Phase E); the level name stays German.

## Source and mapping
- MITO model definition: level table.
- Placement-layers decision: operativ = agent session executing a claimed task.
- Combination strategy §4: MITO operativ stays German.
- MITO model definition: governance-kernel `docs/core/definitions/mito-model.md`.
- Placement-layers decision: org-handbook `docs/decisions/2026-09-26-placement-layers-retired-segment-and-level.md`.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
