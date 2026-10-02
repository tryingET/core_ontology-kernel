---
ont:
  id: "core.Concern"
  type: concept
  labels: ["concern"]
  synonyms: []
  description: "A mode held by a party: an assumption about a proposal, agreement or activity that cannot, for now at least, be backed up by reasoning or enough evidence to qualify as an objection to those who are considering it; it never blocks consent."
  relations:
    - type: instance_of
      target: core.UfoCategory.Mode
  examples:
    - "A holder suspects the new review date is too far away but cannot show a risk; the round keeps it as a concern and adds an evaluation criterion"
  anti_examples:
    - "An argument showing a risk preferably avoided (that is an objection)"
    - "An objection that stood when a decision went ahead (that is kept as dissent)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# concern (core.Concern)

## Definition
A mode held by a party: an assumption about a proposal, agreement or activity that cannot, for now at least, be backed up by reasoning or enough evidence to qualify as an objection to those who are considering it; it never blocks consent.

## Typical usage
- Consent records keep concerns beside objections (ADR-0008 §8). Concerns lead to amendments, evaluation criteria or review dates; they never prevent a proposal from becoming an agreement.
- A concern never becomes dissent.

## Common confusions
- Not an objection: "Concerns don't prevent proposals becoming agreements, only objections do" (S3).
- Not every failed possible objection: a failed argument might reveal a concern, or be only a preference.

## Category
- UFO mode (`core.UfoCategory.Mode`). Required: who holds it, the proposal, agreement or activity, the assumption.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- S3 glossary, concern: "An assumption that cannot (for now at least) be backed up by reasoning or enough evidence to qualify as an objection to those who are considering it."
- S3 practical guide, "Objections" (section "Concerns").
- Holding Owner rulings Q1 and Q7, 2026-10-01 (AK 6364, evidence 12130).
- Decision note: `ontology/decisions/2026-10-02-decision-records-questions.md`.

Admitted: AK task 6364, 2026-10-02
