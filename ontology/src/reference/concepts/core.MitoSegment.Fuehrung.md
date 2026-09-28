---
ont:
  id: "core.MitoSegment.Fuehrung"
  type: concept
  labels: ["Führung"]
  synonyms: ["Management-Führung", "Act 1"]
  description: "The first MITO segment (Act 1): it sets requirements, strategy, goals, tasks, responsibilities and interfaces, and issues the Vorgabe for the level below."
  relations:
    - type: instance_of
      target: core.MitoSegment
    - type: precedes
      target: core.MitoSegment.Input
    - type: produces
      target: core.Vorgabe
  examples:
    - "Setting the goals, responsibilities and interfaces of a new company domain"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Führung (core.MitoSegment.Fuehrung)

## Definition
The first MITO segment (Act 1): it sets requirements, strategy, goals, tasks, responsibilities and interfaces, and issues the Vorgabe for the level below.

## Typical usage
- Goal-setting, policy and planning of the management system sit here, not in Input.

## Common confusions
- Confused with Input: Binner faults ISO's PDCA mapping for putting goal-setting into Plan (B1 p. 372).
- Führung is person-related and works with soft facts; its counterpart Leitung is fact-related (B1 pp. 49, 207, 337).

## Source and mapping
- MITO model definition: segment table (B1 pp. 57–59); Act 1 = Result in EFQM RADAR (B1 pp. 38, 65).
- B1 = Binner, *Organisation 4.0 – MITO-Konfigurationsmanagement* (2018); B2 = Binner, *Ganzheitliche Businessmodell-Transformation* (2020); printed pages.
- MITO model definition: governance-kernel `docs/core/definitions/mito-model.md`.

Admitted: AK task 6147, 2026-09-27
