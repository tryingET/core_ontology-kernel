---
ont:
  id: "core.Decision"
  type: concept
  labels: ["decision"]
  synonyms: []
  description: "A mode: the intention a decider forms by deliberating, whose content is the alternative chosen (doing nothing included) and which the decider commits to bring about."
  relations:
    - type: instance_of
      target: core.UfoCategory.Mode
  examples:
    - "The Holding Owner's intention, formed by weighing the options, that the schema migration goes ahead; the owner's authorization then carries it out"
  anti_examples:
    - "The deliberation that formed it (that is an act, core.Deliberation)"
    - "The sign-off that carries it out (that is an authorization, a decision-resulting action)"
    - "The record that documents it (that is a decision record)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# decision (core.Decision)

## Definition
A mode: the intention a decider forms by deliberating, whose content is the alternative chosen (doing nothing included) and which the decider commits to bring about.

## Typical usage
- A deliberation creates a decision (`core.Deliberation produces core.Decision`). A decision-resulting action manifests it (`manifests`); in the governance core, authorizations, refusals and revocations are such actions, though not the only ones. A decision record documents it.
- "The decision that went ahead" over a standing objection is a decision whose resulting action carries out what the objection was raised against: an authorization that grants it, or a revocation that ends a permission. That is what dissent keeps. A refusal never produces dissent: the proposal did not go ahead.

## Common confusions
- Not an act: the act of deciding is the deliberation, and the act that carries the decision out is a decision-resulting action.
- Not the AK decision row: AK's decision row has a workflow state and maps to a decision record.

## Category
- UFO mode (`core.UfoCategory.Mode`): an intention, a mental moment of its bearer. Required: the decider (its bearer), the goal it commits to, the deliberation that created it, the alternatives and criteria weighed.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- R. Guizzardi, B. G. Carneiro, D. Porello, G. Guizzardi (2020), A Core Ontology on Decision Making, ONTOBRAS 2020, CEUR-WS 2728, pp. 9–21, §3: "a DECISION is an INTENTION created by a DELIBERATION"; it "can eventually manifest in the performing of another ACTION termed a DECISION RESULTING ACTION".
- The Holding Owner's wording, adopted 2026-10-02 (evidence 12302), after ruling Q3 (AK 6364, evidence 12179). *Decision* is a reserved core word, and its definition is the Holding Owner's (ADR-0008 §1.5).
- "Doing nothing included" is the owner's addition to the paper's analysis. In decision analysis "do nothing" is always an alternative: the combination strategy adopts alternatives including "do nothing" (§5; §3 cites NASA, N p. 168), governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.
- Decision note: `ontology/decisions/2026-10-02-decision-records-questions.md`.

Admitted: AK task 6364, 2026-10-02
