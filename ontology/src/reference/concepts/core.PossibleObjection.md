---
ont:
  id: "core.PossibleObjection"
  type: concept
  labels: ["possible objection"]
  synonyms: []
  description: "A mode held by a party: an argument it raises against a proposal, existing decision or activity, offered as an objection whether or not it qualifies."
  relations:
    - type: instance_of
      target: core.UfoCategory.Mode
  examples:
    - "A holder in a consent round argues that the change weakens a safety invariant; the round tests whether the argument qualifies"
  anti_examples:
    - "An assumption held but not raised as an objection (that is a concern)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# possible objection (core.PossibleObjection)

## Definition
A mode held by a party: an argument it raises against a proposal, existing decision or activity, offered as an objection whether or not it qualifies.

## Typical usage
- Every argument raised in a consent round is a possible objection. The round tests it as an argument: if it qualifies, it is an objection (`core.Objection`); if it does not, it is not an objection, though it may reveal a concern (`core.Concern`).
- A possible objection that did not qualify never blocks consent and never becomes dissent. It is kept with its test result, and the proposer may still take it up as an amendment.
- A possible objection may be withdrawn before its test (Holding Owner ruling, 2026-10-02, evidence 12346).

## Common confusions
- Not an objection until it qualifies: S3 tests "if arguments qualify as objections" (the page cited below), and a failed argument may rest on a misconception, an assumption or a personal preference.
- Not a concern: a failed argument only might reveal a concern.

## Category
- UFO mode (`core.UfoCategory.Mode`), inhering in the party who raised it and depending on what it argues against. Required: who raised it, the proposal, existing decision or activity, the argument, the test and its result (unless it was withdrawn before the test).
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- S3 practical guide v2026-01-26 (upstream commit 479413d), vault note `~/Documents/Obsidian/Wiki/S3/` `S3 - Test if Arguments Qualify as Objections.md`: "When someone raises a possible objection (an argument for changing something) check that the argument reveals how leaving things unchanged will — or could — lead to consequences you want to avoid, or that it informs you of a worthwhile way to improve how to go about achieving your objectives." v2024-04-18a (af63a1d), cited here until 2026-10-08, ended the sentence at "improve".
- Wording updated to S3 v2026 ("existing decision" for "agreement") on 2026-10-08 (AK 6822, Holding Owner instruction); the test and its outcomes are unchanged.
- Holding Owner ruling Q1, 2026-10-01 (AK 6364, evidence 12130): a failed argument is not an objection.
- Decision note: `ontology/decisions/2026-10-02-decision-records-questions.md`.

Admitted: AK task 6364, 2026-10-02
