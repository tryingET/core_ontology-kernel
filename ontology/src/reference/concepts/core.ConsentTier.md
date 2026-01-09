---
ont:
  id: "core.ConsentTier"
  type: concept
  labels: ["ConsentTier"]
  synonyms: []
  description: "A governance tier defining who must consent for a change."
  relations: []
  examples:
    - "Kernel tier requires holding owners; project tier requires project owners"
  anti_examples:
    - "Implicit authority with no written rule"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# ConsentTier (core.ConsentTier)

## Definition
A governance tier defining who must consent for a change.

## Typical usage
- Used to avoid accidental escalation and clarify review authority.

## Common confusions
- Confused with roles; tiers describe approval boundaries, not individuals.

