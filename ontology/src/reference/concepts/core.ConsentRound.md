---
ont:
  id: "core.ConsentRound"
  type: concept
  labels: ["consent round"]
  synonyms: ["NASA concurrence"]
  description: "An event: the holders of the affected domains are asked, blind and in parallel, whether they object to a proposal; each objection is tested as an argument and ends integrated, withdrawn or standing."
  relations:
    - type: instance_of
      target: core.UfoCategory.Event
    - type: produces
      target: core.ConsentState
  examples:
    - "The round that asked the holders of the affected layers about a new core word"
  anti_examples:
    - "A vote"
    - "An owner deciding alone (that is an authorization)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# consent round (core.ConsentRound)

## Definition
An event: the holders of the affected domains are asked, blind and in parallel, whether they object to a proposal; each objection is tested as an argument and ends integrated, withdrawn or standing.

## Category
- UFO event (`core.UfoCategory.Event`). Required: the proposal, the holders asked, each objection and its disposition, the end date.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Owner decision 2 of 2026-09-26 (combination strategy §9).
- ADR-0008 §8, records by class.
- Synonym 'NASA concurrence': a signature, an act, so it maps to the round, not to the state (Holding Owner, 2026-09-28; AK 6167): `ontology/decisions/2026-09-28-v0.3.0-pre-release-corrections.md`.
- Decision note: `ontology/decisions/2026-09-27-governance-core-splits.md`.

Admitted: AK task 5987, 2026-09-27
