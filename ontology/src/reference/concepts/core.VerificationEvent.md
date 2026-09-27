---
ont:
  id: "core.VerificationEvent"
  type: concept
  labels: ["verification"]
  synonyms: ["verification event"]
  description: "An event: a check of a claim against evidence under criteria declared in advance; in our records the claim is usually that a product meets a requirement or a DoD row."
  relations:
    - type: instance_of
      target: core.UfoCategory.Event
    - type: uses
      target: core.EvidenceRole
    - type: produces
      target: core.VerificationVerdict
    - type: produces
      target: core.Receipt
  examples:
    - "Recomputing artifact checksums against a retained manifest before tagging"
    - "Running a declared test gate and recording its outcome for a release decision"
  anti_examples:
    - "Restating the claim with more confidence"
    - "A replay check (it shows that a record reproduces, not that the result is right)"
    - "A validation (fitness for purpose, judged by the receiver)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# verification (core.VerificationEvent)

## Definition
An event: a check of a claim against evidence under criteria declared in advance; in our records the claim is usually that a product meets a requirement or a DoD row.

## Typical usage
- For class B and C work the verifier is someone other than the producer.
- A record that says 'verified' names the verification that produced its verdict.

## Common confusions
- Its outcome is a separate concept, the verification verdict; a later verification can supersede a verdict, never an event.
- Not validation: verification asks 'built right?', validation asks 'the right thing?' and is judged by the receiver.

## Category
- UFO event (`core.UfoCategory.Event`). Required: the claim or requirement, the criteria, the evidence used, the verifier.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Split from core.Verification, 'the act and outcome' (decision note below).
- Combination strategy §3 spine row 10 and §4 verification row: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.
- Controlled-vocabulary adjudication, practical consequence amended, item 1: governance-kernel `docs/project/2026-09-26-controlled-vocabulary-adjudication.md`.
- Decision note: `ontology/decisions/2026-09-27-governance-core-splits.md`.

Admitted: AK task 5987, 2026-09-27
