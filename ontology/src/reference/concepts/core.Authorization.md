---
ont:
  id: "core.Authorization"
  type: concept
  labels: ["authorization"]
  synonyms: ["sign-off", "owner sign-off", "approval"]
  description: "An act: a sign-off by someone holding the authority, which grants a permission to a grantee within a stated scope."
  relations:
    - type: depends_on
      target: core.Authority
    - type: manifests
      target: core.Decision
    - type: precedes
      target: core.Revocation
    - type: instance_of
      target: core.UfoCategory.Event
  examples:
    - "The Holding Owner authorizes a class-C change; the record names act, grantor, grantee, scope and basis."
  anti_examples:
    - "A consent round that ended with no objection standing (that is consent, a state)"
    - "An agent approving its own change"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# authorization (core.Authorization)

## Definition
An act: a sign-off by someone holding the authority, which grants a permission to a grantee within a stated scope.

## Typical usage
- Class-C decisions carry an authorization record: act, grantor, grantee, scope and basis.
- An authorization is a decision-resulting action: it carries out the decision of the holder of the authority. A refusal declines and a revocation ends what was granted; both are acts of their own (AK 6364).

## Common confusions
- Confused with consent: consent is a state a round reaches; authorization is one act by a holder of authority.
- Confused with authority: authority is the mandate; an authorization is one use of it.

## Category
- UFO event (`core.UfoCategory.Event`). Required: grantor (holding the authority), grantee, scope, basis; it founds a permission.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §4: approval / concurrence / consent are three acts; owner sign-off → authorization.
- Vocabulary card: authorization [an act: a sign-off that grants a permission].
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
