---
ont:
  id: "core.Pipeline"
  type: concept
  labels: ["Pipeline"]
  synonyms: []
  description: "CI/CD Workflow, der Artefakte baut/prüft/deployed."
  relations: []
  examples:
    - "GitLab CI validate job"
  anti_examples:
    - "Ein manueller Schritt ohne Automatisierung"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Pipeline (core.Pipeline)

## Definition
CI/CD Workflow, der Artefakte baut/prüft/deployed.

## Typical usage
- Used to describe automated checks that gate changes.

## Common confusions
- Confused with a manual checklist.
