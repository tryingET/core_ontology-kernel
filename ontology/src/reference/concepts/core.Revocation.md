---
ont:
  id: "core.Revocation"
  type: concept
  labels: ["revocation"]
  synonyms: []
  description: "An act: the holder of the authority ends one or more permissions, or a delegated authority, that earlier acts founded; those acts stay on record."
  relations:
    - type: depends_on
      target: core.Authority
    - type: manifests
      target: core.Decision
    - type: instance_of
      target: core.UfoCategory.Event
  examples:
    - "The Holding Owner withdraws a grant after the risk changed; the grant and its dissent stay on record"
    - "The Holding Owner ends a steward's delegation"
  anti_examples:
    - "Refusing a permission that was never granted (that is a refusal)"
    - "A permission that ends at the time its authorization stated (it ends without a revocation)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# revocation (core.Revocation)

## Definition
An act: the holder of the authority ends one or more permissions, or a delegated authority, that earlier acts founded; those acts stay on record.

## Typical usage
- A revocation is a new event: the authorization it ends is not changed or deleted.
- An agreement review that ends in *drop* is followed by a revocation; the review itself ends nothing.

## Common confusions
- Not a refusal: a refusal declines what was asked for; a revocation ends what was granted.

## Category
- UFO event (`core.UfoCategory.Event`), a decision-resulting action. Required: the authorizations or delegation it ends, the revoker, the basis.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Reference model, `core.Authorization` row: "a revocation is a new event".
- Holding Owner ruling Q4, 2026-10-01 (AK 6364, evidence 12179): one concept covers ending a permission and ending a delegated authority.
- Decision note: `ontology/decisions/2026-10-02-decision-records-questions.md`.

Admitted: AK task 6364, 2026-10-02
