---
ont:
  id: "core.MitoLevel.Dispositiv"
  type: concept
  labels: ["dispositiv"]
  synonyms: []
  description: "The third MITO level: the sub-processes (Teilprozesse), owned by the sub-process owner; in AI Society an FCOS coordination item, or an AK task and its claimant."
  relations:
    - type: instance_of
      target: core.MitoLevel
  examples:
    - "An FCOS coordination item and the AK task that carries it"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# dispositiv (core.MitoLevel.Dispositiv)

## Definition
The third MITO level: the sub-processes (Teilprozesse), owned by the sub-process owner; in AI Society an FCOS coordination item, or an AK task and its claimant.

## Source and mapping
- MITO model definition: level table.
- Placement-layers decision: dispositiv = FCOS coordination item; AK task and its claimant.
- MITO model definition: governance-kernel `docs/core/definitions/mito-model.md`.
- Placement-layers decision: org-handbook `docs/decisions/2026-09-26-placement-layers-retired-segment-and-level.md`.

Admitted: AK task 6147, 2026-09-27
