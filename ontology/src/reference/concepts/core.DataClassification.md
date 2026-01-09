---
ont:
  id: "core.DataClassification"
  type: concept
  labels: ["DataClassification"]
  synonyms: []
  description: "Klassifikation von Daten (public/internal/restricted/secret)."
  relations: []
  examples:
    - "A repo declares docs as internal, and secrets as secret"
  anti_examples:
    - "Ein Dateiname"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# DataClassification (core.DataClassification)

## Definition
Klassifikation von Daten (public/internal/restricted/secret).

## Typical usage
- Used to decide what can be included in prompts and which repos need stricter controls.

## Common confusions
- Confused with a filename or folder name (classification is about content).

## Canonical classes
- `core.DataClass.Public`
- `core.DataClass.Internal`
- `core.DataClass.Restricted`
- `core.DataClass.SecretData`
