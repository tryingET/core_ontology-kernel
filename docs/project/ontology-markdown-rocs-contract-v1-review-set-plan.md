---
summary: "Frozen review plan for the ontology Markdown / ROCS contract v1 RFC."
read_when:
  - "When executing or auditing the RFC review."
type: "procedure"
---

# Ontology Markdown / ROCS contract v1 — review-set plan

## Reviewed artifact

`docs/project/ontology-markdown-rocs-contract-v1-rfc.md` at the exact committed revision cited by each review attempt.

## Required tracks

1. **Semantic-owner and authority track**
   - Does the RFC preserve ontology-kernel ownership and Decision 53 separation?
   - Does it avoid lifting bounded experimental evidence into a universal semantic contract?
   - Are normative versus guidance fields explicit and internally coherent?

2. **ROCS implementation and migration track**
   - Can the proposal be implemented deterministically and offline-first?
   - Does required-class convergence preserve standalone consumer verification?
   - Are validation, snapshot, tests, release, rollout, and rollback complete enough?

## Review outputs

Each immutable review memo must include:

- exact RFC commit and blob SHA-256;
- findings ranked by severity;
- explicit outcome: `ready_for_adr`, `revise_rfc`, or `reject_current_direction`;
- explicit legal next move.

A synthesis must cite both track memos and emit the controlling outcome. Any material blocker forces `revise_rfc` or `reject_current_direction`.

## Synthesis rule

Designated synthesizer with strict blocker closure. Agreement is not enough: every material finding must be resolved or explicitly shown non-blocking before `ready_for_adr`.
