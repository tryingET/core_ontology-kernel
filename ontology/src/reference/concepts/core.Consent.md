---
ont:
  id: "core.Consent"
  type: concept
  labels: ["Consent"]
  synonyms: []
  description: "A governance state: proceed unless a reasoned objection remains."
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

## Definition
A governance state: proceed unless a reasoned objection remains.

## Typical usage
- Used to gate changes in org/kernel context (proposal → objections → consent → MR).

## Common confusions
- Confused with unanimity; consent allows disagreement if objections are resolved.

