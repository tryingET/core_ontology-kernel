---
ont:
  id: "core.Refusal"
  type: concept
  labels: ["refusal"]
  synonyms: ["declined authorization"]
  description: "An act: the holder of the authority refuses a permission that was asked for; the proposal returns to its driver."
  relations:
    - type: depends_on
      target: core.Authority
    - type: manifests
      target: core.Decision
    - type: instance_of
      target: core.UfoCategory.Event
  examples:
    - "The Holding Owner declines a class-C change; the proposal goes back to its driver to be amended, deferred or dropped"
  anti_examples:
    - "An agent concluding 'no' on its own (agents escalate; only the holder of the authority refuses)"
    - "Ending a permission granted earlier (that is a revocation)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# refusal (core.Refusal)

## Definition
An act: the holder of the authority refuses a permission that was asked for; the proposal returns to its driver.

## Typical usage
- The authorization part of a decision record holds a grant, a refusal, or "not required" (which follows from the decision class).
- A refusal leaves no dissent: the decision did not go ahead.

## Common confusions
- Not an authorization: an authorization grants a permission; a refusal founds none.

## Category
- UFO event (`core.UfoCategory.Event`), a decision-resulting action. Required: the refuser, the party refused, what was asked for, the basis.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Authorization-vs-consent adjudication, clash 5: the owner may decline authorization, and the proposal then returns to its driver; governance-kernel `docs/project/2026-09-26-authorization-vs-consent-adjudication.md`.
- Holding Owner ruling Q4, 2026-10-01 (AK 6364, evidence 12179).
- Decision note: `ontology/decisions/2026-10-02-decision-records-questions.md`.

Admitted: AK task 6364, 2026-10-02
