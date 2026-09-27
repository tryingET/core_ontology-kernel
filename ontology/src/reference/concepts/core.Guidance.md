---
ont:
  id: "core.Guidance"
  type: concept
  labels: ["guidance"]
  synonyms: []
  description: "Advice in text that may be customized freely, such as a Prompt Vault procedure; it binds no one."
  relations:
    - type: instance_of
      target: core.UfoCategory.NormativeDescription
  examples:
    - "A Prompt Vault procedure for writing a letter to an author"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# guidance (core.Guidance)

## Definition
Advice in text that may be customized freely, such as a Prompt Vault procedure; it binds no one.

## Common confusions
- Not a directive: departing from guidance needs no relief.

## Category
- UFO normative description (`core.UfoCategory.NormativeDescription`). Required: its owner; it binds no one.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §4 directive row.
- Vocabulary card: guidance [Prompt Vault advice].
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
