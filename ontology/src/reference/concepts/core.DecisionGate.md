---
ont:
  id: "core.DecisionGate"
  type: concept
  labels: ["decision gate"]
  synonyms: []
  description: "An act: a named authority decides, against criteria set in advance, whether work may proceed."
  relations:
    - type: is_a
      target: core.Deliberation
    - type: depends_on
      target: core.Authority
    - type: instance_of
      target: core.UfoCategory.Event
  examples:
    - "A readiness review before an authority migration."
  anti_examples:
    - "A measuring point (it measures, it does not decide)"
    - "`fcos gates` (health checks)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# decision gate (core.DecisionGate)

## Definition
An act: a named authority decides, against criteria set in advance, whether work may proceed.

## Common confusions
- Never bare 'gate'. Binner's 'Gates' are measuring points; `fcos gates` are health checks; FCOS close is a close gate (FCOS layer).

## Category
- UFO event (`core.UfoCategory.Event`). Required: the named decider, the criteria set in advance, the work at stake.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §4 gate row.
- Vocabulary card: decision gate [an act: a named authority decides against criteria set in advance].
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
