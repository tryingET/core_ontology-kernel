---
ont:
  id: "core.Dissent"
  type: concept
  labels: ["dissent"]
  synonyms: ["recorded disagreement"]
  description: "A record of a disagreement with a decision, kept with the decision: who objected, on what grounds, and why the decision went ahead."
  relations:
    - type: part_of
      target: core.DecisionRecord
    - type: depends_on
      target: core.Decision
    - type: instance_of
      target: core.UfoCategory.Kind
  examples:
    - "An objection still standing when the owner authorized the change anyway, kept in the decision record."
  anti_examples:
    - "An objection resolved before consent (it leaves no dissent)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# dissent (core.Dissent)

## Definition
A record of a disagreement with a decision, kept with the decision: who objected, on what grounds, and why the decision went ahead.

## Typical usage
- Every class-B and class-C decision records its dissent, or 'none'.
- Before a decision goes ahead, a standing objection is escalated, not yet dissent; a concern or a possible objection that did not qualify never becomes dissent.

## Common confusions
- Confused with an objection: an objection blocks consent until it is addressed; dissent is what stays on record when a decision goes ahead over one.

## Category
- UFO kind (`core.UfoCategory.Kind`). Required: the objection it keeps and the decision that went ahead over it.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §4 and §5: recorded disagreement → dissent; NASA's decision report records dissent.
- Vocabulary card: dissent [a record of a disagreement, kept with the decision].
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.
- Typical usage extended in place on 2026-10-02 (AK 6364, evidence 12130 and 12209); its meaning is unchanged. Decision note: `ontology/decisions/2026-10-02-decision-records-questions.md`.

Admitted: AK task 6147, 2026-09-27
