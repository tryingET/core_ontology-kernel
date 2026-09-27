---
ont:
  id: "core.Claim"
  type: concept
  labels: ["Claim"]
  synonyms: ["assertion"]
  description: "An asserted statement whose truth is not established by the assertion itself."
  relations:
    - type: precedes
      target: core.VerificationEvent
    - type: instance_of
      target: core.UfoCategory.Proposition
  examples:
    - "A predeclared campaign claim that a failure-rate threshold justifies an owner review"
    - "A changelog statement that a release fixes a defect"
  anti_examples:
    - "A measurement result (that is an observation)"
    - "A fact established by prior verification and cited as such"
    - "An AK task claim (that is a task claim, a commitment)"
    - "The claim side of a commitment (a UFO claim)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Claim (core.Claim)

## Definition
An asserted statement whose truth is not established by the assertion itself. A claim is what verification, falsification, or retirement decisions evaluate — never their substitute.

## Typical usage
- Predeclaring, before measurement, exactly what a review window is expected to show.
- Separating the assertion under test from the evidence gathered for or against it.

## Common confusions
- Confused with observation: claims describe expectations or assertions; observations record what actually happened.
- Confused with nonclaims: a well-formed claim states its own boundaries; silence about scope is not a boundary.
- Repeating a claim more loudly or more often does not move it toward verified status.
- Not an AK task claim (core.TaskClaim, a commitment) and not the claim side of a commitment (core.UfoCategory.Claim).

## Category
- UFO proposition (`core.UfoCategory.Proposition`): the asserted content. Required: who asserts it, and its scope.
- Reference model: `docs/reference-model/governance-core.md`.
