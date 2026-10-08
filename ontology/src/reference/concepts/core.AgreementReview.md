---
ont:
  id: "core.AgreementReview"
  type: concept
  labels: ["agreement review"]
  synonyms: ["policy review"]
  description: "A scheduled review of an agreement (in S3 v2026 terms, a policy) against its evaluation criteria and metrics, ending in keep, evolve or drop."
  relations:
    - type: instance_of
      target: core.UfoCategory.Event
  examples:
    - "Reviewing a domain agreement on its review date: keep, evolve or drop"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# agreement review (core.AgreementReview)

## Definition
A scheduled review of an agreement (in S3 v2026 terms, a policy) against its evaluation criteria and metrics, ending in keep, evolve or drop.

## Common confusions
- 'Review' is never bare.

## Category
- UFO event (`core.UfoCategory.Event`). Required: the agreement (policy), its evaluation criteria or metrics, the review date.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §4 review row; Combination strategy §5 (keep / evolve / drop).
- S3 practical guide v2026-01-26, vault note `~/Documents/Obsidian/Wiki/S3/S3 - Evaluate and Evolve Policies.md`: v2026 renamed agreements to policies, and its figure draws only "Drop/Archive" and "Evolve"; "keep" survives in the text ("whether there are any objections to keeping it as it is"). The three outcomes are therefore the AI-society choice, not v2026 S3 text (combination strategy update, 2026-10-08, AK 6822).
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
