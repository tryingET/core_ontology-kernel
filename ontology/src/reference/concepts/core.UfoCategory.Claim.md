---
ont:
  id: "core.UfoCategory.Claim"
  type: concept
  labels: ["UFO claim"]
  synonyms: []
  description: "The UFO-C category of social moments held by the party a commitment is owed to, paired with that commitment and its propositional content."
  relations:
    - type: instance_of
      target: core.UfoCategory
  examples:
    - "The requester's claim that a claimed task be done"
  anti_examples:
    - "core.Claim, an asserted statement"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# UFO claim (core.UfoCategory.Claim)

## Definition
The UFO-C category of social moments held by the party a commitment is owed to, paired with that commitment and its propositional content.

## Typical usage
- Test question: Towards whom is a commitment owed?
- Governance-core concepts in this category: none yet.

## Common confusions
- Not core.Claim, an asserted statement.

## Source and mapping
- Guizzardi, Falbo, Guizzardi (2008), Grounding Software Domain Ontologies in UFO, IDEAS 2008 (UFO-C), §4. Checked on the page images on 2026-09-27.
- Reference model: `docs/reference-model/governance-core.md`.

Admitted: AK task 5986, 2026-09-27
