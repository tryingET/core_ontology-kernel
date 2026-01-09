---
ont:
  id: "core.Role"
  type: concept
  labels: ["Role"]
  synonyms: []
  description: "Eine Rolle/Berechtigung, die Fähigkeiten bündelt."
  relations: []
  examples:
    - "Owner / Maintainer role in GitLab"
  anti_examples:
    - "Eine Person selbst (das ist Actor)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Role (core.Role)

## Definition
Eine Rolle/Berechtigung, die Fähigkeiten bündelt.

## Typical usage
- Used to define who can approve, merge, and change protected paths.

## Common confusions
- Confused with a person (`core.Actor`) rather than an assignable responsibility.
