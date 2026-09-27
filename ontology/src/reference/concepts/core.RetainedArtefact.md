---
ont:
  id: "core.RetainedArtefact"
  type: concept
  labels: ["retained artefact"]
  synonyms: []
  description: "Material kept with its content digest and its provenance (what was captured, where it came from, when), so that its bytes can be re-verified."
  relations:
    - type: instance_of
      target: core.UfoCategory.Kind
    - type: depends_on
      target: core.Observation
  examples:
    - "A release-evidence archive with checksum, subject revision and capture time"
  anti_examples:
    - "A screenshot of a dashboard with no window, scope or digest"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# retained artefact (core.RetainedArtefact)

## Definition
Material kept with its content digest and its provenance (what was captured, where it came from, when), so that its bytes can be re-verified.

## Category
- UFO kind (`core.UfoCategory.Kind`). Required: the content digest, the source, the capture time.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Split from core.Evidence, 'digest-bound, provenance-bearing material' (decision note below).
- Decision note: `ontology/decisions/2026-09-27-governance-core-splits.md`.

Admitted: AK task 5987, 2026-09-27
