---
ont:
  id: "core.UfoCategory.Kind"
  type: concept
  labels: ["UFO kind"]
  synonyms: []
  description: "The UFO category of rigid types that give their instances identity and persistence; an instance cannot stop being one."
  relations:
    - type: instance_of
      target: core.UfoCategory
  examples:
    - "A receipt; a decision record"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# UFO kind (core.UfoCategory.Kind)

## Definition
The UFO category of rigid types that give their instances identity and persistence; an instance cannot stop being one.

## Typical usage
- Test question: Could an instance stop being one and still exist?
- Governance-core concepts in this category: core.DecisionRecord, core.Dissent, core.Proposal, core.Receipt, core.RetainedArtefact.

## Source and mapping
- Guizzardi et al. (2022), UFO: Unified Foundational Ontology, Applied Ontology 17(1), p. 173. Checked on the page images on 2026-09-27.
- Reference model: `docs/reference-model/governance-core.md`.

Admitted: AK task 5986, 2026-09-27
