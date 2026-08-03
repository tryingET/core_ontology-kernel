---
summary: "Post-v2 direction: keep bounded semantic agreement, close normalized source identity as not_needed for the reviewed consumer, and test only named capabilities."
read_when:
  - "Designing the successor to ontology source experiment v2."
  - "Interpreting what v2 established without selecting a source format."
type: design
status: proposed
---

# Ontology source architecture — transcendent synthesis

## Direction

Stop asking which container is canonical. The evidence supports no format choice. It supports separating relations that the tournament treated as one problem:

```text
authored bytes --raw hash--> byte identity
      |
      +--compile--> semantic facts --semantic digest--> semantic identity

normalized authored-form identity --> absent unless a consumer proves it is needed
approval/currentness/activation --> owner-issued Decision 53 facts, never content output
```

This changes experiment architecture, not production architecture. Markdown/frontmatter remains current behavior because no replacement won, not because Markdown was proved superior.

## Evidence ledger

| Verified observation | What survives | What does not follow |
|---|---|---|
| A and B agreed on 40/40 semantic streams and digests across V1–V4. | The frozen semantic mapping was independently realizable for the tested packets. | Global equivalence, a production IR, or format preference. |
| A and B disagreed on 40/40 source/debug digests. | The source/debug relation and preimage were under-specified. | That a normalized source identity is needed or that either implementation is canonical. |
| Zero cohort observations were protocol-valid. | No selecting ergonomic evidence exists. | A winner, ranking, tie, or elimination. |
| V3 had 0/14 diagnostic errors; V4 had 14/14. | Discoverability and conflict workflow are hypotheses worth isolating if later needed. | Comparative quality or selection evidence. |
| Pinned editor v1.6.0 reads RDF/OWL, but its node/edge actions change only `.odiagram` presentation state. | A conditional semantically read-only visualization role is technically plausible. | A semantic edit, semantic proposal delta, or reverse semantic lens. |
| The editor has no native contract/profile/base-digest or loss receipt and accepts unresolved ontology references with known prefixes. | External freshness, loss, path-confinement, and reference-validation controls would be required. | Direct governed integration or fail-closed behavior. |
| The ontology dependency reloaded after semantic change without bound-receipt rejection. | The view can refresh from changed source. | Stale-base protection or reproducible proposal review. |

No source-format RFC/ADR may open from these observations.

## Architecture consequence

The durable candidate is a boundary, not a format: replaceable authored serializations may compile to independently testable semantic facts and loss-declared projections. V2 supports that boundary only over its frozen scope. It does not authorize a production IR, migration, ROCS change, ontology mutation, editor adoption, publication, activation, or release.

Four identities must remain non-interchangeable:

1. **Byte identity:** exact authored bytes, served by an ordinary raw-byte digest.
2. **Semantic identity:** normalized facts, served only by a specified and validated semantic contract.
3. **Authored-form identity:** a possible relation across byte differences; the reviewed bounded consumer did not need it, so it is not a current architecture requirement.
4. **Authority/currentness:** owner-issued facts governed by Decision 53. No digest or semantic projection creates released, desired, adopted, used, approved, current, or activated state.

The phrase `source/debug digest` is therefore suspended as an architecture requirement. It may return only with one meaning, one consumer, and evidence that byte identity plus semantic identity and separate provenance cannot serve that consumer.

The pinned editor probe narrows the editor consequence. The implementation cannot occupy the semantic-proposal boundary previously used as a hypothetical candidate consumer. It can at most consume an adapter-produced RDF/OWL projection for visualization while writing separate `.odiagram` presentation state. This is a capability classification, not an adoption decision.

## Source-identity successor disposition

Stage A is complete in `ontology-source-identity-purpose-gate.md`; its independent record is `ontology-source-identity-purpose-gate-review.md`.

The bounded candidate consumer was an ontology maintainer using a future ROCS-to-diagram-editor proposal adapter. The operation was to verify a reproducible proposal against the same semantic base, recover only supported semantic changes, preserve omitted/non-editable facts, and retain a non-authoritative ceiling. The packet separated operation-invariant decoder/lens/receipt machinery from the identity question.

Independent design review passed, and a separate red team found no documented current cache, debugging, merge, provenance, editor, reproducible-build, cross-serialization, or formatting-preservation operation that needed normalized authored-form identity. Semantic contract/digest, raw artifact hashes, and separately queryable provenance answer the identity-sensitive questions. The mechanical outcome is **`not_needed`**. Stage B is not entered, and no normalized digest or implementation follows.

The later capability probe does not reopen that identity result. It changes another axis: the pinned editor cannot realize the hypothetical proposal operation. The reviewed purpose-gate packet and its digest-bound review remain unchanged as historical Stage A evidence.

### Reopening rule

A future consumer may reopen Stage A only by naming an operation whose answer changes under an extra equivalence relation and supplying:

- its producer and consumer;
- exact input distinctions and required answers;
- wrong-answer consequences;
- the failure of semantic identity, raw identity, and separate provenance for those identity-sensitive answers;
- nested or non-nested equivalence laws and concrete witness pairs; and
- a coordination benefit exceeding the contract cost.

A valid future `normalize` disposition would then require Stage B to freeze literal fixture bytes, a complete pair oracle, expected semantic relationships, canonical preimage grammar and encoding, digest algorithm, path/provenance participation, bounded errors, Decision 53 field rejection, two isolated implementations, and independent scoring. Categories such as line endings, Unicode, reordering, comments, guidance, path, provenance, cross-serialization equivalence, and schema version remain candidate discriminators—not permission to execute.

## Dispositions

- **`not_needed`:** remove normalized source/debug identity from architecture claims.
- **`pass`:** both implementations achieve 100% oracle, preimage-byte, and digest agreement with no authority field admitted; only the preregistered relation is supported.
- **`fail`:** any mismatch or unclassified required distinction leaves the relation unresolved and returns to protocol revision.

None selects V1, V2, V3, or V4.

## Complexity rule

Every added surface bears its own proof burden. No actor cohort, timing study, counterbalance, editor probe, RDF round-trip, projection suite, merge exercise, source migration, or production change enters the source-identity protocol unless its named uncertainty requires it. Decision 53 authority machinery cannot enter at all; authority questions route to their owners.

A future format comparison may begin only for one named, decision-relevant capability that a format-neutral contract cannot settle. It must use the smallest sequential falsification that can distinguish the candidates. V3/V4 diagnostics may generate its hypothesis but may not score it. A four-format tournament requires fresh justification.

## Gates

1. **Completed — source-identity purpose gate:** independent review passed with `not_needed`; Stage B was not entered, and normalized-digest implementation remains closed for this bounded disposition.
2. **Dormant — source-identity reopening:** only a new consumer satisfying the existing reopening rule may restart Stage A.
3. **Completed/failed — pinned semantic-proposal capability:** editor v1.6.0 exposes no semantic-edit or proposal-delta surface. The guarded proposal-lens path stops at capability discovery.
4. **Conditional — read-only visualization adapter:** may begin only for an owner-named visual operation and would require external freshness/loss receipts, semantic-reference validation, confined dependency paths, UI-level evidence, and separate adoption authorization.
5. **RFC/ADR:** remains blocked until independent protocol-valid evidence demonstrates a source-format winner.

## Residual debt

- No normalized authored-form identity purpose or preimage is established; the reviewed bounded consumer closed `not_needed`, while undocumented future consumers remain outside the claim.
- Semantic agreement covers only v2's 40 accepted packets and malformed corpus, not the full ontology or production ROCS.
- System4D, guidance, provenance, and future-extension participation remain contract questions.
- No valid ergonomics, review-cost, merge-cost, or onboarding comparison exists.
- V3 discoverability and V4 workflow remain diagnostic-only.
- The pinned editor cannot realize the reviewed hypothetical semantic-proposal operation.
- The probe receipt contains raw byte hashes, not a contract-bound semantic digest, and contains no included/omitted/unsupported/editable loss declaration.
- C1 tested generated-file parse/stringify, not a complete VS Code open/save workflow; C3 tested an unresolved reference, not the original unsupported RDF fact-kind case.
- No external adapter, reference-validation gate, dependency-path confinement, untrusted-`.odiagram` policy, or owner-approved read-only value case exists.
- Projection, editor, and release contracts cannot inherit experimental hashes or authority. Any future visualization receipt must be newly produced under its own semantic contract and profile.
