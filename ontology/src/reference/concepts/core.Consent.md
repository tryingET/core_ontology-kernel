---
ont:
  id: "core.Consent"
  type: concept
  labels: ["Consent"]
  synonyms: []
  description: "A governance state: proceed unless a reasoned objection remains."
  status: deprecated
  deprecated:
    since: "2026-09-27"
    replaced_by: "core.ConsentState"
    decision: "ontology/decisions/2026-09-27-governance-core-splits.md"
  relations: []
  examples:
    - "Proposal accepted after objections resolved"
  anti_examples:
    - "Silence without an objection window"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Consent (core.Consent)

> Deprecated on 2026-09-27 (AK 5987): the word stood both for a state and for the round that reaches it, and this concept did not name its round. It is split into consent (core.ConsentState) and consent round (core.ConsentRound). Use `core.ConsentState` where the main meaning is meant. Decision note: `ontology/decisions/2026-09-27-governance-core-splits.md`.

## Definition
A governance state: proceed unless a reasoned objection remains.

## Typical usage
- Used to gate changes in org/kernel context (proposal → objections → consent → MR).

## Common confusions
- Confused with unanimity; consent allows disagreement if objections are resolved.

