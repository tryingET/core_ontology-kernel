---
ont:
  id: "core.Secret"
  type: concept
  labels: ["Secret"]
  synonyms: []
  description: "Credential/Token/Key; darf nicht geleakt werden."
  relations: []
  examples:
    - "PAT_GITLAB token in a local .env"
  anti_examples:
    - "Ein öffentliches API-Endpoint"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Secret (core.Secret)

## Definition
Credential/Token/Key; darf nicht geleakt werden.

## Typical usage
- Used in policies and CI checks (secret scanning; no-leak constraints).

## Common confusions
- Confused with public identifiers (URLs, group names).
