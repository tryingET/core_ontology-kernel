---
ont:
  id: "core.Invariant"
  type: concept
  labels: ["Invariant"]
  synonyms: []
  description: "Golden Rule: wenn gebrochen → Konsistenz/Daten korrupt."
  relations: []
  examples:
    - "Concept IDs are stable; meaning changes create a new ID"
  anti_examples:
    - "Eine Präferenz, die man ignorieren kann"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Invariant (core.Invariant)

## Definition
Golden Rule: wenn gebrochen → Konsistenz/Daten korrupt.

## Typical usage
- Used as non-negotiable rules enforced by policy/validation.

## Common confusions
- Confused with optional best practices.
