---
ont:
  id: "core.StakeholderExpectation"
  type: concept
  labels: ["stakeholder expectation"]
  synonyms: ["Binner Anforderung"]
  description: "What a stakeholder expects of a product or process, before it is turned into goals and requirements (Binner's Anforderung)."
  relations:
    - type: instance_of
      target: core.UfoCategory.Mode
  examples:
    - "The owner expects to see every pending decision on one page"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# stakeholder expectation (core.StakeholderExpectation)

## Definition
What a stakeholder expects of a product or process, before it is turned into goals and requirements (Binner's Anforderung).

## Common confusions
- Not a requirement: an expectation is not yet a verifiable 'shall' with an owner.

## Category
- UFO mode (`core.UfoCategory.Mode`). Required: the stakeholder who holds it.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §4 requirement row: Binner's Anforderung → stakeholder expectation; NASA stakeholder expectations.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
