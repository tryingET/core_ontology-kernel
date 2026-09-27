---
ont:
  id: "core.TechnologyReadiness"
  type: concept
  labels: ["technology readiness"]
  synonyms: ["TRL"]
  description: "How far a technology has been demonstrated, rated as a technology readiness level (TRL)."
  relations:
    - type: instance_of
      target: core.UfoCategory.Quality
  examples:
    - "A technology demonstrated in a relevant environment (TRL 6)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# technology readiness (core.TechnologyReadiness)

## Definition
How far a technology has been demonstrated, rated as a technology readiness level (TRL).

## Common confusions
- Not maturity (MITO) and not readiness (preflight or readiness review).

## Category
- UFO quality (`core.UfoCategory.Quality`). Required: the technology, the TRL scale, the environment it was shown in.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §4 maturity row.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
