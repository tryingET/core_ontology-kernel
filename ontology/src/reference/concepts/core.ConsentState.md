---
ont:
  id: "core.ConsentState"
  type: concept
  labels: ["consent"]
  synonyms: []
  description: "A situation: a consent round has ended with no objection standing, so the proposal it considered may proceed; it always names that round."
  relations:
    - type: instance_of
      target: core.UfoCategory.Situation
  examples:
    - "No objection stood at the end of the round on a new core word, so the proposal may proceed"
  anti_examples:
    - "Silence without a round"
    - "An owner sign-off (that is an authorization, an act)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# consent (core.ConsentState)

## Definition
A situation: a consent round has ended with no objection standing, so the proposal it considered may proceed; it always names that round.

## Typical usage
- Consent is asked of the holders of the affected domains only, blind and in parallel (owner decision 2, 2026-09-26).

## Common confusions
- Not an act: consent is reached by a round; an authorization is an act by one holder of authority.
- Not a vote: a round tests objections as arguments; it does not count voices.

## Category
- UFO situation (`core.UfoCategory.Situation`). Required: the round, its proposal, every objection with its disposition.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Split from core.Consent, 'a governance state' (decision note below).
- Vocabulary card: consent [a state: a consent round ended with no objection standing].
- Decision note: `ontology/decisions/2026-09-27-governance-core-splits.md`.

Admitted: AK task 5987, 2026-09-27
