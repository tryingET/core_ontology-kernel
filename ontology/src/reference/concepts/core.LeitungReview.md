---
ont:
  id: "core.LeitungReview"
  type: concept
  labels: ["Leitung review"]
  synonyms: []
  description: "A review in the Leitung segment of whether a process or system does the right things (effectiveness); its findings return to Führung as Rückmeldung."
  relations:
    - type: produces
      target: core.Rueckmeldung
    - type: instance_of
      target: core.UfoCategory.Event
  examples:
    - "The monthly bootstrap Leitung review of the vocabulary loop"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Leitung review (core.LeitungReview)

## Definition
A review in the Leitung segment of whether a process or system does the right things (effectiveness); its findings return to Führung as Rückmeldung.

## Typical usage
- The bootstrap Leitung review of the vocabulary loop (ADR-0008 §11).

## Common confusions
- 'Review' is never bare.

## Category
- UFO event (`core.UfoCategory.Event`). Required: the process or system reviewed, the effectiveness question.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §4 review row; MITO model definition (Leitung: review, audit, compliance, improvement).
- MITO model definition: governance-kernel `docs/core/definitions/mito-model.md`.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
