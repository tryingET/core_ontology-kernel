---
ont:
  id: "core.MitoLevel"
  type: concept
  labels: ["level"]
  synonyms: ["MITO level"]
  description: "One of the four process levels of Binner's enterprise architecture (strategisch, taktisch, dispositiv, operativ), each with its own owner; the MITO loop runs on every level."
  relations: []
  examples:
    - "A doc whose front matter records mito_level: dispositiv"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# level (core.MitoLevel)

## Definition
One of the four process levels of Binner's enterprise architecture (strategisch, taktisch, dispositiv, operativ), each with its own owner; the MITO loop runs on every level.

## Typical usage
- Docs record their level in front matter as mito_level.
- Targets flow down and actual results flow up; each level compares Soll with Ist.

## Common confusions
- Not a NASA product layer, not an architecture layer (Layer-N), not a ROCS ontology layer.

## Source and mapping
- MITO model definition: Enterprise-Architektur-Ebenenmodell (B1 pp. 12, 54, 67–68; B2 p. 148).
- Placement-layers decision: the AI Society mapping of the four levels.
- B1 = Binner, *Organisation 4.0 – MITO-Konfigurationsmanagement* (2018); B2 = Binner, *Ganzheitliche Businessmodell-Transformation* (2020); printed pages.
- MITO model definition: governance-kernel `docs/core/definitions/mito-model.md`.
- Placement-layers decision: org-handbook `docs/decisions/2026-09-26-placement-layers-retired-segment-and-level.md`.

Admitted: AK task 6147, 2026-09-27
