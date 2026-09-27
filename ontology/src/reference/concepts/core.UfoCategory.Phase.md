---
ont:
  id: "core.UfoCategory.Phase"
  type: concept
  labels: ["UFO phase"]
  synonyms: []
  description: "The UFO category of anti-rigid types that apply to an instance through an intrinsic change it can go through; the phases of a kind partition it."
  relations:
    - type: instance_of
      target: core.UfoCategory
  examples:
    - "A system in operations mode"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# UFO phase (core.UfoCategory.Phase)

## Definition
The UFO category of anti-rigid types that apply to an instance through an intrinsic change it can go through; the phases of a kind partition it.

## Typical usage
- Test question: Does the instance enter it by changing itself, with no other party involved?
- Governance-core concepts in this category: core.ArtefactStatus, core.OperationsMode.

## Source and mapping
- Guizzardi et al. (2022), UFO: Unified Foundational Ontology, Applied Ontology 17(1), p. 173. Checked on the page images on 2026-09-27.
- Reference model: `docs/reference-model/governance-core.md`.

Admitted: AK task 5986, 2026-09-27
