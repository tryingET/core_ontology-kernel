---
ont:
  id: "core.Exception"
  type: concept
  labels: ["Exception"]
  synonyms: []
  description: "Bewusste Ausnahme von einer Regel (mit Begründung und Scope)."
  relations:
    - type: instance_of
      target: core.UfoCategory.Situation
  examples:
    - "Incident hotfix bypass approved with scope and end date"
  anti_examples:
    - "Ein Bug (ungewollt)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Exception (core.Exception)

## Definition
Bewusste Ausnahme von einer Regel (mit Begründung und Scope).

## Typical usage
- Used for governance-approved rule bypasses with explicit scope and justification.

## Common confusions
- Confused with an accidental failure (bug/incident).

## Category
- UFO situation (`core.UfoCategory.Situation`). Required: the rule, the scope, the justification.
- Reference model: `docs/reference-model/governance-core.md`.
