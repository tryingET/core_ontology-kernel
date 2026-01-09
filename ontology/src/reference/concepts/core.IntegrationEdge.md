---
ont:
  id: "core.IntegrationEdge"
  type: concept
  labels: ["IntegrationEdge"]
  synonyms: []
  description: "Integration/Schnittstelle zwischen Systemen (höchster Bug-Risk)."
  relations: []
  examples:
    - "Service ↔ GitLab API over HTTPS"
  anti_examples:
    - "Eine interne Funktionssignatur"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# IntegrationEdge (core.IntegrationEdge)

## Definition
Integration/Schnittstelle zwischen Systemen (höchster Bug-Risk).

## Typical usage
- Used to enumerate external dependencies and contracts at system boundaries.

## Common confusions
- Confused with internal function calls inside one system boundary.
