---
ont:
  id: "core.ConsentRound"
  type: concept
  labels: ["consent round"]
  synonyms: ["NASA concurrence"]
  description: "An event: the holders of the affected domains are asked, blind and in parallel, whether they object to a proposal; each possible objection is tested as an argument, and each that qualifies as an objection ends integrated, withdrawn or standing."
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
An event: the holders of the affected domains are asked, blind and in parallel, whether they object to a proposal; each possible objection is tested as an argument, and each that qualifies as an objection ends integrated, withdrawn or standing.

## Typical usage
- A possible objection may be withdrawn before its test. One that fails the test is kept with its test result: it never blocks consent and never becomes dissent, though the proposer may still take it up as an amendment (Holding Owner ruling, 2026-10-02, evidence 12346).

## Category
- UFO event (`core.UfoCategory.Event`). Required: the proposal, the holders asked, each possible objection with its test result or its withdrawal before the test, each objection with its disposition, the end date.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Owner decision 2 of 2026-09-26 (combination strategy §9).
- ADR-0008 §8, records by class.
- Synonym 'NASA concurrence': a signature, an act, so it maps to the round, not to the state (Holding Owner, 2026-09-28; AK 6167): `ontology/decisions/2026-09-28-v0.3.0-pre-release-corrections.md`.
- Decision note: `ontology/decisions/2026-09-27-governance-core-splits.md`.
- Reworded in place on 2026-10-02 (AK 6364, evidence 12209): "each possible objection is tested". Only an objection takes an end state; how a possible objection ends before or after failing its test is the Holding Owner's ruling of the same day (evidence 12346), after the consent round on this change. Decision note: `ontology/decisions/2026-10-02-decision-records-questions.md`.

Admitted: AK task 5987, 2026-09-27
