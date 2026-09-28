---
ont:
  id: "core.Verification"
  type: concept
  labels: ["Verification"]
  synonyms: []
  description: "The act and outcome of checking a claim against evidence under declared criteria."
  status: deprecated
  deprecated:
    since: "2026-09-27"
    replaced_by: "core.VerificationEvent"
    decision: "ontology/decisions/2026-09-27-governance-core-splits.md"
  relations:
    - type: uses
      target: core.Evidence
    - type: produces
      target: core.Receipt
  examples:
    - "Recomputing artifact checksums against a retained manifest before tagging"
    - "Running a declared test gate and recording its outcome for a release decision"
  anti_examples:
    - "Restating the claim with more confidence"
    - "An authority figure asserting the claim without criteria or evidence"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Verification (core.Verification)

> Deprecated on 2026-09-27 (AK 5987): this concept named two categories. It is split into verification (core.VerificationEvent) and verification verdict (core.VerificationVerdict). Use `core.VerificationEvent` where the main meaning is meant. Decision note: `ontology/decisions/2026-09-27-governance-core-splits.md`.

## Definition
The act and outcome of checking a claim against evidence under declared criteria. The criteria — what would count as support, falsification, or insufficient evidence — are part of the verification, declared before or at check time, not negotiated after the result.

## Typical usage
- Gating releases and promotions on predeclared checks whose outcomes are recorded.
- Turning competing claims into an evaluateable question: which criteria, which evidence, what result.

## Common confusions
- Confused with assertion: without declared criteria and independent evidence, a "verification" is just a restated claim.
- Confused with validation of correctness in general: a verification answers its declared question only; it does not certify safety, quality, or adoption beyond that scope.
- A passed verification is itself an event that should produce a receipt; an unrecorded verification cannot be cited later.
