---
ont:
  id: "core.DecisionRecord"
  type: concept
  labels: ["DecisionRecord"]
  synonyms: []
  description: "A persistent record of a decision, including context, options, and rationale."
  relations:
    - type: depends_on
      target: core.Decision
    - type: instance_of
      target: core.UfoCategory.Kind
  examples:
    - "ADR-style decision linked from ontology deprecations"
  anti_examples:
    - "An undocumented choice in chat logs"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# DecisionRecord (core.DecisionRecord)

## Definition
A persistent record of a decision, including context, options, and rationale.

## Typical usage
- Used to justify new IDs, deprecations, and relation additions.
- It documents a decision (`core.Decision`): the motivating driver, the alternatives and criteria, the decision, and its consent, authorization and dissent records.

## Common confusions
- Confused with a proposal; decisions are outcomes.

## Category
- UFO kind (`core.UfoCategory.Kind`). Required: the decision and its consent, authorization and dissent records.
- Reference model: `docs/reference-model/governance-core.md`.
