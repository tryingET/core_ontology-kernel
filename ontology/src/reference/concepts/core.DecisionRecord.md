---
ont:
  id: "core.DecisionRecord"
  type: concept
  labels: ["DecisionRecord"]
  synonyms: []
  description: "A persistent record of a decision, including context, options, and rationale."
  relations:
    - type: depends_on
      target: core.Decision
    - type: instance_of
      target: core.UfoCategory.Kind
  examples:
    - "ADR-style decision linked from ontology deprecations"
  anti_examples:
    - "An undocumented choice in chat logs"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# DecisionRecord (core.DecisionRecord)

## Definition
A persistent record of a decision, including context, options, and rationale.

## Typical usage
- Used to justify new IDs, deprecations, and relation additions.
- One record may document several decisions taken in order on one case, for example a refusal, a grant after amendment and a later revocation; each keeps its own deliberation and its resulting action, if any (Holding Owner ruling, 2026-10-02, AK 6364, evidence 12346).

## Common confusions
- Confused with a proposal; decisions are outcomes.

## Category
- UFO kind (`core.UfoCategory.Kind`). Required: each decision it documents, in order, with its consent, authorization and dissent records.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Extended in place on 2026-10-02 (AK 6364, evidence 12346): one record may document several decisions in order; the Required line names each of them. Decision note: `ontology/decisions/2026-10-02-decision-records-questions.md`.
