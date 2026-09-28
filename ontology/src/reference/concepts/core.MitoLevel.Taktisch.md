---
ont:
  id: "core.MitoLevel.Taktisch"
  type: concept
  labels: ["taktisch"]
  synonyms: []
  description: "The second MITO level: the main processes (Hauptprozesse), owned by the main-process owner; in AI Society a repo or domain owner."
  relations:
    - type: instance_of
      target: core.MitoLevel
  examples:
    - "A repo owner steering the main process of one repository"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# taktisch (core.MitoLevel.Taktisch)

## Definition
The second MITO level: the main processes (Hauptprozesse), owned by the main-process owner; in AI Society a repo or domain owner.

## Source and mapping
- MITO model definition: level table.
- Placement-layers decision: taktisch = repo or domain owner (human or steward agent).
- MITO model definition: governance-kernel `docs/core/definitions/mito-model.md`.
- Placement-layers decision: org-handbook `docs/decisions/2026-09-26-placement-layers-retired-segment-and-level.md`.

Admitted: AK task 6147, 2026-09-27
