---
ont:
  id: "core.ArtefactStatus"
  type: concept
  labels: ["artefact status"]
  synonyms: ["NASA document states"]
  description: "The state of a document or other artefact: approach, preliminary, baseline or update (NASA's document states)."
  relations:
    - type: instance_of
      target: core.UfoCategory.Phase
  examples:
    - "A document in preliminary status"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# artefact status (core.ArtefactStatus)

## Definition
The state of a document or other artefact: approach, preliminary, baseline or update (NASA's document states).

## Common confusions
- Not maturity (MITO process maturity).

## Category
- UFO phase (`core.UfoCategory.Phase`). Required: the artefact; approach, preliminary, baseline and update partition its life.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §4 maturity row.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
