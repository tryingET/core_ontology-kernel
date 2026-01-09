---
ont:
  id: "core.DataClass.SecretData"
  type: concept
  labels: ["DataClassSecret"]
  synonyms: ["secret"]
  description: "Data classification: secret; disclosure is severe (not the same as core.Secret)."
  relations:
    - type: instance_of
      target: "core.DataClassification"
  examples:
    - "Secret material stored outside git and excluded from prompts"
  anti_examples:
    - "Internal docs without sensitive content"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# DataClass.SecretData (core.DataClass.SecretData)

## Definition
Data classification: secret; disclosure is severe (not the same as core.Secret).

