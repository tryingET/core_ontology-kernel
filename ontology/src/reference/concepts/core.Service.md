---
ont:
  id: "core.Service"
  type: concept
  labels: ["Service"]
  synonyms: []
  description: "Deploybares Systemteil mit definierten Interfaces."
  relations: []
  examples:
    - "Self-hosted GitLab service"
  anti_examples:
    - "Eine Klasse im Code"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Service (core.Service)

## Definition
Deploybares Systemteil mit definierten Interfaces.

## Typical usage
- Used to model deployed systems with SLOs, owners, and incidents.

## Common confusions
- Confused with libraries or scripts that are not deployed services.
