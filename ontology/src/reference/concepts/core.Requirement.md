---
ont:
  id: "core.Requirement"
  type: concept
  labels: ["requirement"]
  synonyms: ["shall statement"]
  description: "A binding statement: one verifiable 'shall' with an owner, a verification method, a waiver authority and a trace to its parent (or flagged as self-derived)."
  relations: []
  examples:
    - "The item contract shall record the tool version used for each check."
  anti_examples:
    - "S3's 'requirement' (in our own text: goal)"
    - "A wish with no way to verify it"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# requirement (core.Requirement)

## Definition
A binding statement: one verifiable 'shall' with an owner, a verification method, a waiver authority and a trace to its parent (or flagged as self-derived).

## Typical usage
- Requirements become FCOS DoD rows and are checked by verification.

## Common confusions
- S3's requirement → goal; Binner's Anforderung → stakeholder expectation.

## Source and mapping
- Combination strategy §3 spine row 6 (NASA p. 132); Combination strategy §4 requirement row.
- Vocabulary card: requirement [a binding statement].
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
