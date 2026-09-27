---
ont:
  id: "core.Vorgabe"
  type: concept
  labels: ["Vorgabe"]
  synonyms: []
  description: "What Führung sets for the level below: goals, targets and tasks that the lower level plans and carries out."
  relations: []
  examples:
    - "A target and a deadline that the company level receives from the strategic level"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Vorgabe (core.Vorgabe)

## Definition
What Führung sets for the level below: goals, targets and tasks that the lower level plans and carries out.

## Typical usage
- Targets flow down as Vorgaben and actual results flow back as Rückmeldungen; each level compares Soll with Ist.
- The Holding Owner sets the core words as a Vorgabe (ADR-0008 §4).

## Common confusions
- Not direction (AK strategy) and not a directive (a binding rule): a Vorgabe is the MITO flow from Führung downward.

## Source and mapping
- MITO model definition: Führung issues the Vorgabe (B1 pp. 49, 207, 337); levels (B1 pp. 12, 54, 67–68).
- B1 = Binner, *Organisation 4.0 – MITO-Konfigurationsmanagement* (2018); B2 = Binner, *Ganzheitliche Businessmodell-Transformation* (2020); printed pages.
- MITO model definition: governance-kernel `docs/core/definitions/mito-model.md`.

Admitted: AK task 6147, 2026-09-27
