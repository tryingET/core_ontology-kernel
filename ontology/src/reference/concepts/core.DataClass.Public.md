---
ont:
  id: "core.DataClass.Public"
  type: concept
  labels: ["DataClassPublic"]
  synonyms: ["public"]
  description: "Data classification: safe to share publicly."
  relations:
    - type: instance_of
      target: "core.DataClassification"
  examples:
    - "Open-source compatible metadata"
  anti_examples:
    - "Credentials or internal incident notes"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# DataClass.Public (core.DataClass.Public)

## Definition
Data classification: safe to share publicly.

