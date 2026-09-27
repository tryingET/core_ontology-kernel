---
ont:
  id: "core.UfoCategory.Role"
  type: concept
  labels: ["UFO role"]
  synonyms: []
  description: "The UFO category of anti-rigid types that apply to an instance only through a relation, which belongs to the role's definition."
  relations:
    - type: instance_of
      target: core.UfoCategory
  examples:
    - "A reviewer within a review assignment"
  anti_examples:
    - "core.Role, the kernel's older role-or-permission concept, which AK 5987 splits"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# UFO role (core.UfoCategory.Role)

## Definition
The UFO category of anti-rigid types that apply to an instance only through a relation, which belongs to the role's definition.

## Typical usage
- Test question: Which relation makes the instance play it?
- Governance-core concepts in this category: none yet.

## Common confusions
- Not core.Role, the kernel's older role-or-permission concept, which AK 5987 splits.

## Source and mapping
- Guizzardi et al. (2022), UFO: Unified Foundational Ontology, Applied Ontology 17(1), pp. 173–174. Checked on the page images on 2026-09-27.
- Reference model: `docs/reference-model/governance-core.md`.

Admitted: AK task 5986, 2026-09-27
