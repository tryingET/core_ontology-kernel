---
ont:
  id: "core.Validation"
  type: concept
  labels: ["validation"]
  synonyms: []
  description: "A check of fitness for purpose: the receiver judges the result against the effectiveness metric ('the right thing')."
  relations:
    - type: uses
      target: core.Metric
    - type: instance_of
      target: core.UfoCategory.Event
  examples:
    - "The receiving domain confirms that a new record schema lets it do its job"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# validation (core.Validation)

## Definition
A check of fitness for purpose: the receiver judges the result against the effectiveness metric ('the right thing').

## Typical usage
- Done by the consuming domain or the owner, never by the producer; it sits in Leitung.

## Common confusions
- Not verification (conformance to a requirement, 'built right').
- Schema validation → schema check; FCOS 'validation tiers' → test tiers.

## Category
- UFO event (`core.UfoCategory.Event`). Required: the receiver who judges, the effectiveness metric, the product.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §3 spine row 11 (NASA p. 204); Combination strategy §4 validation row; NASA p. 196.
- Vocabulary card: validation [fitness for purpose, judged by the receiver].
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
