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
- A deliberation creates a decision (`core.Deliberation produces core.Decision`). The decision is manifested in a decision-resulting action: an authorization, a refusal or a revocation (`manifests`). A decision record documents it.
- "The decision that went ahead" over a standing objection is a decision whose resulting action happened while the objection stood; that is what dissent keeps.

## Common confusions
- Not an act: the act of deciding is the deliberation, and the act that carries the decision out is a decision-resulting action.
- Not the AK decision row: AK's decision row has a workflow state and maps to a decision record.

## Category
- UFO mode (`core.UfoCategory.Mode`): an intention, a mental moment of its bearer. Required: the decider (its bearer), the goal it commits to, the deliberation that created it, the alternatives and criteria weighed.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- R. Guizzardi, B. G. Carneiro, D. Porello, G. Guizzardi (2020), A Core Ontology on Decision Making, ONTOBRAS 2020, CEUR-WS 2728, pp. 9–21, §3: "a DECISION is an INTENTION created by a DELIBERATION"; it "can eventually manifest in the performing of another ACTION termed a DECISION RESULTING ACTION".
- Core word *decision*, defined by the Holding Owner (ADR-0008 §1.5): ruling Q3, 2026-10-01 (AK 6364, evidence 12179).
- Decision note: `ontology/decisions/2026-10-02-decision-records-questions.md`.

Admitted: AK task 6364, 2026-10-02
