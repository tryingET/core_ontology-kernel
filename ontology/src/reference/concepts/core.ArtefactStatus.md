---
ont:
  id: "core.ArtefactStatus"
  type: concept
  labels: ["artefact status"]
  synonyms: ["NASA document states"]
  description: "The state of a document or other artefact: approach, preliminary, baseline or update (NASA's document states)."
  relations:
    - type: instance_of
      target: core.UfoCategory.Quality
  examples:
    - "Preliminary: the value a design document holds while it is still being worked out"
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
- UFO quality (`core.UfoCategory.Quality`). Required: the artefact, its value on the scale approach, preliminary, baseline, update.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §4 maturity row.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.
- Recategorised from UFO phase to UFO quality before its first release (Holding Owner, 2026-09-28; AK 6167, inspection finding evidence 11284): `ontology/decisions/2026-09-28-v0.3.0-pre-release-corrections.md`.

Admitted: AK task 6147, 2026-09-27
