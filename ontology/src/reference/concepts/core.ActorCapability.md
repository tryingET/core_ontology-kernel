---
ont:
  id: "core.ActorCapability"
  type: concept
  labels: ["capability"]
  synonyms: ["ability"]
  description: "What an actor or system is able to do, whether or not it is permitted to."
  relations:
    - type: instance_of
      target: core.UfoCategory.Mode
  examples:
    - "An agent can open a merge request"
  anti_examples:
    - "Permission to do it (that is a permission)"
    - "A goal (an outcome)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# capability (core.ActorCapability)

## Definition
What an actor or system is able to do, whether or not it is permitted to.

## Common confusions
- A script is not a capability; the capability is what the actor can do with it.

## Category
- UFO mode (`core.UfoCategory.Mode`). Required: the actor or system, what it can do.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Split from core.Capability, 'Fähigkeit/Permission' (decision note below).
- Decision note: `ontology/decisions/2026-09-27-governance-core-splits.md`.

Admitted: AK task 5987, 2026-09-27
