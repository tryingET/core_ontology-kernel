---
ont:
  id: "core.VerificationEvent"
  type: concept
  labels: ["verification"]
  synonyms: []
  description: "An event: a check, against evidence and under criteria declared in advance, that a product meets a requirement or a DoD row."
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
    - "Checking a delivered change against each row of its DoD and recording the outcome"
    - "Running a declared test gate and recording its outcome for a release decision"
  anti_examples:
    - "Restating the claim with more confidence"
    - "A replay check (it shows that a record reproduces, not that the result is right)"
    - "A schema check (it proves conformance to a schema, not to a requirement)"
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
An event: a check, against evidence and under criteria declared in advance, that a product meets a requirement or a DoD row.

## Typical usage
- For class B and C work the verifier is someone other than the producer.
- A record that says 'verified' names the verification that produced its verdict.

## Common confusions
- Its outcome is a separate concept, the verification verdict; a later verification can supersede a verdict, never an event.
- Not validation: verification asks 'built right?', validation asks 'the right thing?' and is judged by the receiver.
- Not every check: a schema check or a replay check checks something other than a requirement or a DoD row.

## Category
- UFO event (`core.UfoCategory.Event`). Required: the product, the requirement or DoD row, the criteria, the evidence used, the verifier.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Split from core.Verification, 'the act and outcome' (decision note below).
- Combination strategy §3 spine row 10 and §4 verification row: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.
- Controlled-vocabulary adjudication, practical consequence amended, item 1: governance-kernel `docs/project/2026-09-26-controlled-vocabulary-adjudication.md`.
- Decision note: `ontology/decisions/2026-09-27-governance-core-splits.md`.
- Narrowed to the decided sense before its first release (Holding Owner, 2026-09-28; AK 6167, inspection finding evidence 11283): `ontology/decisions/2026-09-28-v0.3.0-pre-release-corrections.md`.

Admitted: AK task 5987, 2026-09-27
