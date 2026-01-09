---
ont:
  id: "core.Risk"
  type: concept
  labels: ["Risk"]
  synonyms: []
  description: "Eine aktive Unsicherheit mit möglichem Schaden."
  relations: []
  examples:
    - "Prompt injection via repo files"
  anti_examples:
    - "Eine reine Annahme ohne Impact"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Risk (core.Risk)

## Definition
Eine aktive Unsicherheit mit möglichem Schaden.

## Typical usage
- Tracked in registers; mitigations inform policies and tooling.

## Common confusions
- Confused with an incident (realized failure) rather than a potential.
