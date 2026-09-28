---
ont:
  id: "core.Capability"
  type: concept
  labels: ["Capability"]
  synonyms: []
  description: "Eine Fähigkeit/Permission, die Aktionen erlaubt."
  status: deprecated
  deprecated:
    since: "2026-09-27"
    replaced_by: "core.ActorCapability"
    decision: "ontology/decisions/2026-09-27-governance-core-splits.md"
  relations: []
  examples:
    - "Agent can open a Merge Request"
  anti_examples:
    - "Ein Ziel (Outcome)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Capability (core.Capability)

> Deprecated on 2026-09-27 (AK 5987): this concept named two categories. It is split into capability (core.ActorCapability) and permission (core.Permission). Use `core.ActorCapability` where the main meaning is meant. Decision note: `ontology/decisions/2026-09-27-governance-core-splits.md`.

## Definition
Eine Fähigkeit/Permission, die Aktionen erlaubt.

## Typical usage
- Used in agent profiles and access control discussions.

## Common confusions
- Confused with implementation details (a script is not a capability).
