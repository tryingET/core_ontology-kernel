---
ont:
  id: "core.Evidence"
  type: concept
  labels: ["Evidence"]
  synonyms: []
  description: "Digest-bound, provenance-bearing material offered in support of a claim."
  status: deprecated
  deprecated:
    since: "2026-09-27"
    replaced_by: "core.EvidenceRole"
    decision: "ontology/decisions/2026-09-27-governance-core-splits.md"
  relations:
    - type: depends_on
      target: core.Observation
  examples:
    - "A retained release-evidence archive with checksum, subject revision, and capture time"
    - "A test-run log referenced by digest from a review record"
  anti_examples:
    - "An assertion repeated without a checkable source"
    - "A screenshot of a dashboard with no window, scope, or digest"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Evidence (core.Evidence)

> Deprecated on 2026-09-27 (AK 5987): this concept named two categories. It is split into evidence (core.EvidenceRole) and retained artefact (core.RetainedArtefact). Use `core.EvidenceRole` where the main meaning is meant. Decision note: `ontology/decisions/2026-09-27-governance-core-splits.md`.

## Definition
Digest-bound, provenance-bearing material offered in support of a claim. Evidence carries what was captured, where it came from, when, and how its bytes can be re-verified — it does not carry the conclusion.

## Typical usage
- Attaching re-verifiable artifacts (digests, revisions, capture windows) to reviews, releases, and custody records.
- Keeping the authority ceiling explicit: valid evidence supports review; it never by itself establishes correctness, safety, or adoption.

## Common confusions
- Confused with proof: evidence supports or falsifies claims under declared criteria; it does not settle them.
- Confused with observation: observations are the captured measurements; evidence is the bounded, re-verifiable packaging of them for a specific support role.
- Confused with authority: who offers evidence and who may accept it are authority questions, not properties of the evidence itself.
