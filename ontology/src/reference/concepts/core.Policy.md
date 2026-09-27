---
ont:
  id: "core.Policy"
  type: concept
  labels: ["Policy"]
  synonyms: []
  description: "Eine formalisierte Regel, die Verhalten einschränkt oder überprüft."
  relations:
    - type: instance_of
      target: core.UfoCategory.NormativeDescription
  examples:
    - "CODEOWNERS-required approval for protected paths"
  anti_examples:
    - "Eine vage Guideline ohne Prüfbarkeit"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Policy (core.Policy)

## Definition
Eine formalisierte Regel, die Verhalten einschränkt oder überprüft.

## Typical usage
- Used for enforceable rules with explicit scope and checks.

## Common confusions
- Confused with informal guidelines that cannot be validated.

## Category
- UFO normative description (`core.UfoCategory.NormativeDescription`). Required: whom it binds and its owner.
- Reference model: `docs/reference-model/governance-core.md`.
