---
ont:
  id: "core.Permission"
  type: concept
  labels: ["permission"]
  synonyms: []
  description: "What a party may do within a stated scope, granted by an authorization or by a rule; a role can bundle several permissions."
  relations:
    - type: instance_of
      target: core.UfoCategory.Mode
  examples:
    - "Permission to merge to the protected main branch, held by maintainers"
  anti_examples:
    - "Being able to do it (that is a capability)"
    - "The mandate to grant permissions (that is authority)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# permission (core.Permission)

## Definition
What a party may do within a stated scope, granted by an authorization or by a rule; a role can bundle several permissions.

## Typical usage
- Its scope may say when it ends; it then ends without a revocation. An agreement review date does not end it.
- A revocation ends a permission before then.

## Category
- UFO mode (`core.UfoCategory.Mode`). Required: the holder, what it allows, the scope, the authorization or rule that grants it.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Split from core.Role and core.Capability, which both mixed permission in (decision note below).
- UFO-L permission (Griffo, Almeida, Guizzardi 2018), via the research note behind the adjudication's school 7.
- Decision note: `ontology/decisions/2026-09-27-governance-core-splits.md`.
- Typical usage added in place on 2026-10-02 (AK 6364, evidence 12179 and 12209); its meaning is unchanged. Decision note: `ontology/decisions/2026-10-02-decision-records-questions.md`.

Admitted: AK task 5987, 2026-09-27
