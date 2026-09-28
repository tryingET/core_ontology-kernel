---
ont:
  id: "core.TaskClaim"
  type: concept
  labels: ["task claim"]
  synonyms: []
  description: "An agent's commitment to the requester, made by claiming an AK task, to do the work within the lease; the agent releases it when it stops."
  relations:
    - type: instance_of
      target: core.UfoCategory.Commitment
  examples:
    - "An agent claims an AK task and holds the lease until it completes or releases the task"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# task claim (core.TaskClaim)

## Definition
An agent's commitment to the requester, made by claiming an AK task, to do the work within the lease; the agent releases it when it stops.

## Common confusions
- Not core.Claim (an asserted statement).
- A lease that runs out is a broken commitment, not a release.

## Category
- UFO commitment (`core.UfoCategory.Commitment`). Required: the agent (its session), the requester, the task, the lease; paired with the requester's claim.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Vocabulary card: task claim (AK) [your commitment to the requester for the lease].
- Controlled-vocabulary adjudication, addendum (UFO-C commitment; the requester's side vs the agent's side); owner decision D24.
- Controlled-vocabulary adjudication: governance-kernel `docs/project/2026-09-26-controlled-vocabulary-adjudication.md`.

Admitted: AK task 6147, 2026-09-27
