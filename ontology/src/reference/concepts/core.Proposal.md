---
ont:
  id: "core.Proposal"
  type: concept
  labels: ["Proposal"]
  synonyms: []
  description: "A concrete change request with rationale, scope, and acceptance criteria."
  relations:
    - type: instance_of
      target: core.UfoCategory.Kind
  examples:
    - "Add a new kernel relation with clear semantics and tests"
  anti_examples:
    - "A vague idea without a decision path"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Proposal (core.Proposal)

## Definition
A concrete change request with rationale, scope, and acceptance criteria.

## Typical usage
- Used as the entry point for governance-driven change.

## Common confusions
- Confused with a decision; proposals can be rejected or revised.

## Category
- UFO kind (`core.UfoCategory.Kind`). Required: proposer, change, rationale, scope, acceptance criteria.
- Reference model: `docs/reference-model/governance-core.md`.
