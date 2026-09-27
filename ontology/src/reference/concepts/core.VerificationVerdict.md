---
ont:
  id: "core.VerificationVerdict"
  type: concept
  labels: ["verification verdict"]
  synonyms: ["verification outcome"]
  description: "The outcome of a verification (pass, fail or insufficient evidence) for the claim it checked under its criteria; a later verification can supersede it."
  relations:
    - type: instance_of
      target: core.UfoCategory.Situation
  examples:
    - "Fail: two DoD rows are unmet, from the check run on the release candidate"
  anti_examples:
    - "The check itself (that is a verification)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# verification verdict (core.VerificationVerdict)

## Definition
The outcome of a verification (pass, fail or insufficient evidence) for the claim it checked under its criteria; a later verification can supersede it.

## Common confusions
- A verdict without the verification that produced it cannot be cited.

## Category
- UFO situation (`core.UfoCategory.Situation`). Required: the verification that produced it, the claim, the criteria.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Split from core.Verification, 'the act and outcome' (decision note below).
- Decision note: `ontology/decisions/2026-09-27-governance-core-splits.md`.

Admitted: AK task 5987, 2026-09-27
