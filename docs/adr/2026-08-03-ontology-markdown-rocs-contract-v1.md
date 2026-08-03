---
summary: "Accept the bounded ontology Markdown v1 source contract and required ROCS consumer boundary."
read_when:
  - "When implementing or changing ontology-kernel source admission or its ROCS dependency."
type: "decision"
status: "accepted"
decision_id: 110
---

# ADR: Ontology Markdown / ROCS contract v1

## Decision

Accept the exact RFC revision at ontology-kernel commit `70f692978cf7957be9bc44bb136399e47f4172ac`, blob `9c21495dcb116bc5e39f8bc44c0369136fc1f2f8`, SHA-256 `d0c8704b3a7fabe1aeeede763e990295f0e164dae7b75a5f2b15aec671ae5ef5`.

The controlling review is [r5 synthesis](../project/ontology-markdown-rocs-contract-v1-review-synthesis-r5.md), outcome `ready_for_adr`.

## Accepted boundaries

1. `ontology-kernel` owns field meaning and the opt-in `ontology-markdown-v1` source grammar.
2. ROCS evaluates only operation-qualified source-contract/schema/reference conformance. It does not emit a generic semantic verdict or broad semantic-correctness claim.
3. Implementation uses one shared parser/dispatcher path for v1 documents; duplicate admission implementations are not accepted.
4. `ont` is the normative declaration. Relation examples move under `ont`; concept-only `system4d.fog`, examples, anti-examples, and body prose remain guidance; `axis_default` remains presentation.
5. V1 retains unique relation-label references. Relation-ID migration is deferred.
6. `context.create` remains raw UTF-8 capture/custody. Any downstream interpretation must re-admit bytes through the selected source contract.
7. `rocs-cli` package release remains package-owner work. The kernel pins one exact vendored materialization receipt and bytes; it does not claim canonical bytes across builders.
8. A complete successful operation may claim conformance only for its exact admitted corpus and operation. Partial, rejected, or resource-exhausted operations emit no corpus-conformance claim.
9. Decision 53, package publication, consumer adoption, activation, currentness, and AK lifecycle remain separate owner facts.
10. The accepted 40-hex `source_commit` means the repository's current Git SHA-1 object ID. Algorithm agility requires a successor receipt schema.

## Consumer decision

`ontology-kernel` is a ROCS `required` consumer with nested `ontology/` layout. CI uses the checked-in vendored bundle through `scripts/ci/full.sh`, not a sibling workspace checkout.

## Cross-repo execution

Decision 110 is `cross_repo`. Execution decomposes through the attached coordination-only fanout into owner-local tasks and commits in:

- `core/rocs-cli` — parser/dispatcher, materialization receipt, tests, then separate package release;
- `core/ontology-kernel` — source migration, manifest/profile, vendoring, CI and clean no-sibling acceptance.

A repo-scoped decision must never link a foreign-repo task. This ADR does not make the coordination artifact a second task authority.

## Consequences

- Current Markdown remains operational and supersedable; no source-format winner is declared.
- Existing consumers remain on legacy behavior unless their layer explicitly opts in.
- ROCS 0.3.0 is a later package-owner execution task, not an effect of recording this ADR.
- Corpus guidance relocation is intended to preserve meaning; any additional content change requires separate review.
- Rollback is consumer repin/revert or a forward corrective package release, never an unpinned sibling checkout.
