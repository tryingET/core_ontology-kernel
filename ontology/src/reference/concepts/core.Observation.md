---
ont:
  id: "core.Observation"
  type: concept
  labels: ["Observation"]
  synonyms: []
  description: "A recorded measurement of actual behavior within a stated scope and time window."
  relations: []
  examples:
    - "Telemetry event counts captured over a declared 7-day window"
    - "A timestamped command transcript retained as a session artifact"
  anti_examples:
    - "Intended or designed behavior presented as if it had been measured"
    - "An interpretation or trend derived from data (that is an inference, not the observation)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# Observation (core.Observation)

## Definition
A recorded measurement of actual behavior within a stated scope and time window. An observation is the raw, bounded capture — not its interpretation.

## Typical usage
- Citing the concrete capture (what, where, when, how many) that downstream evidence and claims must reference.
- Separating "what was seen" from "what it means" in review and campaign records.

## Common confusions
- Confused with interpretation: averages, trends, and root causes are inferences about observations, not observations.
- Confused with evidence: an observation becomes evidence only when captured with provenance and offered in support of a claim.
- Missing events are not zero observations; absence of capture is a coverage limitation, not a measurement.
