---
ont:
  id: "core.Relief"
  type: concept
  labels: ["relief"]
  synonyms: ["NASA relief"]
  description: "Release from a binding rule, granted by the rule's owner and recorded in a ledger; it can be prospective or retrospective."
  relations:
    - type: is_a
      target: core.Exception
  examples:
    - "The owner of a coding rule exempts one legacy module, recorded in the relief ledger"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# relief (core.Relief)

## Definition
Release from a binding rule, granted by the rule's owner and recorded in a ledger; it can be prospective or retrospective.

## Common confusions
- Not customization: how a practice is done may be changed without approval; relief from a binding rule needs the rule owner.

## Source and mapping
- Combination strategy §3 (commitment; NASA p. 34); Combination strategy §4 deviation row.
- Vocabulary card: relief [release from a rule, by the rule's owner].
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
