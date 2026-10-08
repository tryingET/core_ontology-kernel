---
ont:
  id: "core.Concern"
  type: concept
  labels: ["concern"]
  synonyms: []
  description: "A mode held by a party: an assumption about a proposal, existing decision or activity that cannot, for now at least, be backed up by reasoning or enough evidence to qualify as an objection to those who are considering it; it never blocks consent."
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
A mode held by a party: an assumption about a proposal, existing decision or activity that cannot, for now at least, be backed up by reasoning or enough evidence to qualify as an objection to those who are considering it; it never blocks consent.

## Typical usage
- Consent records keep concerns beside objections (ADR-0008 §8). Concerns lead to amendments, evaluation criteria or review dates; they never prevent a proposal from being accepted.
- A concern never becomes dissent.

## Common confusions
- Not an objection: "Concerns don’t prevent proposals from being accepted; only objections do" (S3 v2026, `S3 - Objections.md`, section "Concerns").
- Not every failed possible objection: a failed argument might reveal a concern, or be only a preference.

## Category
- UFO mode (`core.UfoCategory.Mode`). Required: who holds it, the proposal, existing decision or activity, the assumption.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- S3 practical guide v2026-01-26 (upstream commit 479413d), vault notes `~/Documents/Obsidian/Wiki/S3/` `S3 - Glossary.md` (Concern): "An assumption that cannot (for now at least) be backed up by reasoning or enough evidence to qualify as an objection to those who are considering it." The entry is unchanged since v2024-04-18a (af63a1d), which this concept cited until 2026-10-08.
- Same edition, `S3 - Objections.md`, section "Concerns" (v2024: "Concerns don't prevent proposals becoming agreements, only objections do").
- Wording updated to S3 v2026 ("existing decision" for "agreement") on 2026-10-08 (AK 6822, Holding Owner instruction); it never blocks consent, as before.
- Holding Owner ruling Q1, 2026-10-01 (AK 6364, evidence 12130), which admitted `core.Concern`.
- Decision note: `ontology/decisions/2026-10-02-decision-records-questions.md`.

Admitted: AK task 6364, 2026-10-02
