---
ont:
  id: "core.DataClass.Restricted"
  type: concept
  labels: ["DataClassRestricted"]
  synonyms: ["restricted"]
  description: "Data classification: restricted access; high leakage impact."
  relations:
    - type: instance_of
      target: "core.DataClassification"
  examples:
    - "Financial details; health-related information; private keys in secure stores"
  anti_examples:
    - "Public documentation"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# DataClass.Restricted (core.DataClass.Restricted)

## Definition
Data classification: restricted access; high leakage impact.

