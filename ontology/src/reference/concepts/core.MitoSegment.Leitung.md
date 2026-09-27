---
ont:
  id: "core.MitoSegment.Leitung"
  type: concept
  labels: ["Leitung"]
  synonyms: ["Leitung segment", "Management-Leitung", "Act 2"]
  description: "The fifth MITO segment (Act 2): it reviews effectiveness, 'doing the right things', through review, audit, compliance and improvement, and returns the Rückmeldung that feeds the next Führung."
  relations:
    - type: instance_of
      target: core.MitoSegment
    - type: precedes
      target: core.MitoSegment.Fuehrung
    - type: produces
      target: core.Rueckmeldung
  examples:
    - "A review that asks whether the release process still serves the people who use it"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Leitung (core.MitoSegment.Leitung)

## Definition
The fifth MITO segment (Act 2): it reviews effectiveness, 'doing the right things', through review, audit, compliance and improvement, and returns the Rückmeldung that feeds the next Führung.

## Typical usage
- Validation by the receiver and the Leitung review sit here.

## Common confusions
- Not Leistung: MITO has no Leistung segment; B1's two 'Leistungssegment' are most likely misprints for Leitungssegment (the same pages name the segment Leitung).
- Leitung is fact-related and works with hard facts, rules and compliance; its counterpart Führung is person-related.

## Source and mapping
- MITO model definition: segment table; Act 2 = Review in EFQM RADAR (B1 pp. 65, 533–535; B2 pp. 137, 256).
- Findings register B1-1 and B1-2 (org-handbook docs/registers/source-findings.md).
- B1 = Binner, *Organisation 4.0 – MITO-Konfigurationsmanagement* (2018); B2 = Binner, *Ganzheitliche Businessmodell-Transformation* (2020); printed pages.
- MITO model definition: governance-kernel `docs/core/definitions/mito-model.md`.

Admitted: AK task 6147, 2026-09-27
