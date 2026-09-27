---
ont:
  id: "core.UfoCategory.Quality"
  type: concept
  labels: ["UFO quality"]
  synonyms: []
  description: "The UFO category of moments whose values lie in a quality structure, so that a target is a region of that structure."
  relations:
    - type: instance_of
      target: core.UfoCategory
  examples:
    - "A metric; a technology readiness level"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# UFO quality (core.UfoCategory.Quality)

## Definition
The UFO category of moments whose values lie in a quality structure, so that a target is a region of that structure.

## Typical usage
- Test question: On which scale is it measured, and what value counts as met?
- Governance-core concepts in this category: core.Metric, core.TechnologyReadiness.

## Source and mapping
- Guizzardi et al. (2022), UFO: Unified Foundational Ontology, Applied Ontology 17(1), p. 172. Checked on the page images on 2026-09-27.
- Reference model: `docs/reference-model/governance-core.md`.

Admitted: AK task 5986, 2026-09-27
