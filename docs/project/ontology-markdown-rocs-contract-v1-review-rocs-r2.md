---
summary: "Decision 110 ROCS implementation and migration review attempt r2; outcome revise_rfc."
read_when:
  - "When auditing Decision 110 review lineage."
type: "review"
---

# Decision 110 — ROCS implementation and migration review r2

## Binding

- ontology-kernel commit: `e6cf6c7bb44be99b3ec42f0a49052cbc198ec9bb`
- RFC blob: `94132c664d4e8483984439ae20436995ac1f2887`
- RFC SHA-256: `364fafbb8711684e1a4866b294d600774497d7ea36503c3ff4b769ac9ae8dadf`
- ROCS observation: `aff1ddcadf328a0f117e68a4743643ed28a7df3b`
- execution: `dispatch-1785797779146-1`

## Findings

1. **High:** the vendored runtime copies ambient dependency trees, so an exact version does not yet identify canonical bundle bytes; rollback must be consumer repin or forward correction rather than release reversal.
2. **High:** the proposal lacks an opt-in contract selector, breaking-version policy, complete source-reading command scope, ref-layer boundary, and explicit unbound-versus-bound pack behavior.
3. **High:** no executable kernel profile/runtime matrix exists for no-sibling semantic discovery; the current manifest has no profile and current CI uses Python 3.11 while discovery v0 requires Python 3.12 / Unicode 15.0.0.

The tracked 31-concept / 12-relation corpus otherwise conforms after the declared relation-guidance migration.

## Outcome

`revise_rfc`

## Legal next move

Define canonical bundle/release/rollback identity, opt-in compatibility and complete command scope, and the kernel profile/runtime/no-sibling acceptance matrix. Then rerun both tracks and synthesis. No ADR, convergence, or release is legal from r2.
