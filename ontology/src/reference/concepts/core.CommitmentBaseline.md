---
ont:
  id: "core.CommitmentBaseline"
  type: concept
  labels: ["commitment baseline"]
  synonyms: []
  description: "An agreed set of commitments under change control: it changes only through its named change authority."
  relations: []
  examples:
    - "The agreed requirements of a release, changed only through their change authority"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# commitment baseline (core.CommitmentBaseline)

## Definition
An agreed set of commitments under change control: it changes only through its named change authority.

## Common confusions
- 'Baseline' is never bare: plan figures (MITO Soll) and the FCOS freshness baseline are different things.

## Source and mapping
- Combination strategy §3 (commitment); Combination strategy §4 baseline row.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
