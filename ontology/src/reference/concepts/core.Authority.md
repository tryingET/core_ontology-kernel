---
ont:
  id: "core.Authority"
  type: concept
  labels: ["Authority"]
  synonyms: []
  description: "A recognized mandate to decide, attest, or promote within a stated scope."
  relations:
    - type: constrains
      target: core.Verification
    - type: depends_on
      target: core.Policy
  examples:
    - "A maintainer's mandate to merge to main under the lane's main-first policy"
    - "An owner's exclusive authority to accept a bounded proposal or approve a release"
  anti_examples:
    - "Mere ability: tool access or technical capability without a recognized mandate"
    - "Authority claimed from ownership of infrastructure alone"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Authority (core.Authority)

## Definition
A recognized mandate to decide, attest, or promote within a stated scope. Authority is granted by policy, consent, or delegation — it is a property of the relationship between actor and scope, never of the actor's tools or abilities.

## Typical usage
- Naming who may accept evidence, merge changes, cut releases, or promote content — and in which scope the mandate ends.
- Keeping decision surfaces explicit: an action outside a mandate is out of scope even if technically possible.

## Common confusions
- Confused with capability: being able to do X is not being authorized to do X.
- Confused with verification: an authority may attest that a check ran; the attestation does not replace the check.
- Scope is part of the mandate; authority over one repository or surface does not transfer to another.
