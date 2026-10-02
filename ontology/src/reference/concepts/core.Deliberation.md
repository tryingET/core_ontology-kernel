---
ont:
  id: "core.Deliberation"
  type: concept
  labels: ["deliberation"]
  synonyms: []
  description: "An act: a decider weighs alternatives against criteria and preferences and so creates a decision."
  relations:
    - type: produces
      target: core.Decision
    - type: instance_of
      target: core.UfoCategory.Event
  examples:
    - "The owner weighs migrating now against waiting for the next rotation and decides to wait"
    - "A readiness review deciding against criteria set in advance (a decision gate)"
  anti_examples:
    - "The decision it creates (that is an intention, core.Decision)"
    - "The sign-off that carries the decision out (that is an authorization)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# deliberation (core.Deliberation)

## Definition
An act: a decider weighs alternatives against criteria and preferences and so creates a decision.

## Typical usage
- A decision gate is a deliberation by a named authority against criteria set in advance (`core.DecisionGate is_a core.Deliberation`).
- Criteria are the quality or mode types the decider weighs (for example cost or reversibility), not mental moments.

## Category
- UFO event (`core.UfoCategory.Event`), an action of its agent. Required: the agent, the motivating intention, the alternatives, the criteria, the decision created.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- R. Guizzardi, B. G. Carneiro, D. Porello, G. Guizzardi (2020), A Core Ontology on Decision Making, ONTOBRAS 2020, CEUR-WS 2728, §3: "due to a certain (motivating) INTENTION, an AGENT performs a DELIBERATION, which, in turn, creates a new INTENTION termed a DECISION".
- Holding Owner ruling Q3, 2026-10-01 (AK 6364, evidence 12179).
- Decision note: `ontology/decisions/2026-10-02-decision-records-questions.md`.

Admitted: AK task 6364, 2026-10-02
