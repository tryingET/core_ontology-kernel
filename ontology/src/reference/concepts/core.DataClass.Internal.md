---
ont:
  id: "core.DataClass.Internal"
  type: concept
  labels: ["DataClassInternal"]
  synonyms: ["internal"]
  description: "Data classification: internal to the holding (not public)."
  relations:
    - type: instance_of
      target: "core.DataClassification"
  examples:
    - "Internal runbooks and architecture notes"
  anti_examples:
    - "Customer PII/PHI (treat as restricted)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# DataClass.Internal (core.DataClass.Internal)

## Definition
Data classification: internal to the holding (not public).

