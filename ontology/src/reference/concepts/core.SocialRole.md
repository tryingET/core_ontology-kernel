---
ont:
  id: "core.SocialRole"
  type: concept
  labels: ["role"]
  synonyms: ["social role"]
  description: "A role someone plays within a relation defined by a rule, such as maintainer of a repository, reviewer of a proposal or steward of a domain; it names that relation and grants its permissions through it."
  relations:
    - type: instance_of
      target: core.UfoCategory.Role
  examples:
    - "Maintainer of a GitLab repository"
    - "Reviewer in a review assignment"
  anti_examples:
    - "A person or an agent (that is an actor)"
    - "A permission on its own (that is a permission)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# role (core.SocialRole)

## Definition
A role someone plays within a relation defined by a rule, such as maintainer of a repository, reviewer of a proposal or steward of a domain; it names that relation and grants its permissions through it.

## Common confusions
- People and agents both play roles (in UFO a role mixin); one player can hold several roles, so count roles, players and assignments separately.

## Category
- UFO role (`core.UfoCategory.Role`). Required: the player, the relation that makes it true, the rule that defines it.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Split from core.Role, 'Rolle/Berechtigung' (decision note below).
- Decision note: `ontology/decisions/2026-09-27-governance-core-splits.md`.

Admitted: AK task 5987, 2026-09-27
