---
ont:
  id: "core.Metric"
  type: concept
  labels: ["metric"]
  synonyms: ["Binner Kennzahl", "NASA MOE", "NASA MOP"]
  description: "A defined, measurable quantity with a calculation rule, compared with a target to show how well a goal or requirement is met (Binner's Kennzahl; NASA's measures of effectiveness and performance)."
  relations: []
  examples:
    - "Share of AK tasks closed with evidence, per month, target 100 %"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# metric (core.Metric)

## Definition
A defined, measurable quantity with a calculation rule, compared with a target to show how well a goal or requirement is met (Binner's Kennzahl; NASA's measures of effectiveness and performance).

## Typical usage
- An objective carries an effectiveness metric, judged at validation; a requirement carries a performance metric, checked at verification.

## Common confusions
- 'Measure' is never bare.
- Say which kind: an effectiveness metric (NASA MOE) or a performance metric (NASA MOP); NASA itself mixes the two (handbook p. 69 vs glossary p. 205).

## Source and mapping
- Combination strategy §3 spine rows 3 and 6; Combination strategy §4 measure row.
- Findings register N-4.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
