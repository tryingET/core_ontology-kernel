---
ont:
  id: "core.ConformanceAudit"
  type: concept
  labels: ["conformance audit"]
  synonyms: []
  description: "An audit that the product as built matches its requirements and its documentation (NASA's functional and physical configuration audits); in AI Society often done by replay."
  relations:
    - type: instance_of
      target: core.UfoCategory.Event
  examples:
    - "Replaying a release's recorded checks to confirm it matches its requirements"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# conformance audit (core.ConformanceAudit)

## Definition
An audit that the product as built matches its requirements and its documentation (NASA's functional and physical configuration audits); in AI Society often done by replay.

## Common confusions
- Not a process audit (how a process is carried out).

## Category
- UFO event (`core.UfoCategory.Event`). Required: the product, its requirements and documentation.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §4 review row: conformance audit (NASA FCA/PCA; replay).
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
