---
ont:
  id: "core.Assumption"
  type: concept
  labels: ["Assumption"]
  synonyms: []
  description: "Unbewiesene Annahme; muss validierbar gemacht werden."
  relations: []
  examples:
    - "Assume CI runner can reach GitLab base URL"
  anti_examples:
    - "Ein Fakt (bewiesen)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Assumption (core.Assumption)

## Definition
Unbewiesene Annahme; muss validierbar gemacht werden.

## Typical usage
- Tracked in registers; validated during rollout and incident reviews.

## Common confusions
- Confused with a decision (assumptions are provisional).
