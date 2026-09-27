---
ont:
  id: "core.CarriedObligation"
  type: concept
  labels: ["carried obligation"]
  synonyms: ["NASA lien"]
  description: "An open obligation carried forward on a decision to proceed, with an owner and a date; never on a close."
  relations:
    - type: instance_of
      target: core.UfoCategory.Commitment
  examples:
    - "Proceed with the migration, carrying the obligation to backfill its evidence by a set date"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# carried obligation (core.CarriedObligation)

## Definition
An open obligation carried forward on a decision to proceed, with an owner and a date; never on a close.

## Common confusions
- Work left after a close becomes a successor item, not a carried obligation. The word 'lien' is not used.

## Category
- UFO commitment (`core.UfoCategory.Commitment`). Required: who owes it, to whom, the proceed decision, owner and date.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §3 (NASA 'lien', NASA p. 17); Combination strategy §4 lien row.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
