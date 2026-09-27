---
ont:
  id: "core.Role"
  type: concept
  labels: ["Role"]
  synonyms: []
  description: "Eine Rolle/Berechtigung, die Fähigkeiten bündelt."
  status: deprecated
  deprecated:
    since: "2026-09-27"
    replaced_by: "core.SocialRole"
    decision: "ontology/decisions/2026-09-27-governance-core-splits.md"
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

> Deprecated on 2026-09-27 (AK 5987): this concept named two categories. It is split into role (core.SocialRole) and permission (core.Permission). Use `core.SocialRole` where the main meaning is meant. Decision note: `ontology/decisions/2026-09-27-governance-core-splits.md`.

## Definition
Eine Rolle/Berechtigung, die Fähigkeiten bündelt.

## Typical usage
- Used to define who can approve, merge, and change protected paths.

## Common confusions
- Confused with a person (`core.Actor`) rather than an assignable responsibility.
