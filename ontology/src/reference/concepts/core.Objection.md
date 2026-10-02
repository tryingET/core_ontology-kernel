---
ont:
  id: "core.Objection"
  type: concept
  labels: ["Objection"]
  synonyms: []
  description: "A possible objection, raised against a proposal in a consent round, that qualified: its argument reveals consequences or risks preferably avoided, or a worthwhile improvement, so it blocks consent until it is integrated or withdrawn."
  relations:
    - type: is_a
      target: core.PossibleObjection
    - type: instance_of
      target: core.UfoCategory.Mode
  examples:
    - "This change weakens a safety invariant; propose an alternative"
  anti_examples:
    - "A preference without impact/risks"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Objection (core.Objection)

## Definition
A possible objection, raised against a proposal in a consent round, that qualified: its argument reveals consequences or risks preferably avoided, or a worthwhile improvement, so it blocks consent until it is integrated or withdrawn.

## Typical usage
- Used to surface risks, missing safeguards, or unclear semantics.
- An objection ends integrated (resolved by any amendment, deferral with an owner and date or monitoring included), withdrawn, or standing. When a decision goes ahead over a standing objection, its resulting action carries out what the objection was raised against (a grant, or a revocation), and the objection is kept as dissent.

## Common confusions
- Confused with disagreement; objections must be actionable and reasoned.
- Confused with a concern: a concern cannot (for now) be backed by reasoning or evidence and never blocks consent.
- An argument that failed the test is a possible objection, not an objection.

## Category
- UFO mode (`core.UfoCategory.Mode`); its argument is its content, not a second category. A subkind of possible objection: whether it qualifies is settled by the argument's content. Required: who holds it, the proposal it objects to, its reasons.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- S3 practical guide, local edition `holdingco/governance-kernel/external/s3-0-practical-guide` (v2024-04-18a, upstream commit af63a1d), `glossary.yaml`, objection (its definition, which `src/making-sense-of-organizations/objection.md` renders): "An objection is an argument – relating to a proposal, existing agreement, or activity being conducted by one or more members of the organization – that reveals consequences or risks that are preferably avoided for the organization, or that demonstrates worthwhile ways to improve."
- S3 also counts arguments against existing agreements and activities. The kernel's objection keeps the extension it had in v0.3.0: it is raised against a proposal and blocks consent (evidence 12211).
- Reworded in place on 2026-10-02 (AK 6364, Holding Owner ruling, evidence 12211): its conditions (it blocks consent; a preference without impact is not one) are unchanged; only `core.PossibleObjection` was added above it. Decision note: `ontology/decisions/2026-10-02-decision-records-questions.md`.
