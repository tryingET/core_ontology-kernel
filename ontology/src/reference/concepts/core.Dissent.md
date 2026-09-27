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

## Common confusions
- Confused with an objection: an objection blocks consent until it is addressed; dissent is what stays on record when a decision goes ahead over one.

## Source and mapping
- Combination strategy §4 and §5: recorded disagreement → dissent; NASA's decision report records dissent.
- Vocabulary card: dissent [a record of a disagreement, kept with the decision].
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
