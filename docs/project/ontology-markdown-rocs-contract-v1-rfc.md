---
summary: "RFC for a bounded current-Markdown contract and reproducible ROCS consumer boundary."
read_when:
  - "When reviewing or implementing ontology-kernel and rocs-cli source-contract alignment."
type: "proposal"
---

# RFC: Ontology Markdown / ROCS contract v1

## Status

Proposal. This RFC does not authorize implementation. The governance path is one cross-repo AK decision covering `core/ontology-kernel` and `core/rocs-cli`, with both semantic-owner and ROCS-owner review tracks. Implementation becomes lawful only after review closes `ready_for_adr`, the cross-repo ADR is recorded, post-ADR plans are attached, and separately scoped AK tasks in each repository are created and claimed. A review outcome or ontology-kernel artifact alone cannot authorize a ROCS release.

## Inputs

- [Problem brief](ontology-markdown-rocs-contract-v1-problem-brief.md)
- [Evidence note](ontology-markdown-rocs-contract-v1-evidence-note.md)
- [POLARIS model](ontology-source-polaris-model.md)
- [Transcendent synthesis](ontology-source-architecture-transcendent-synthesis.md)

## Problem

The semantic owner and its deterministic tool disagree about accepted source shape and reproducible consumption. Validation currently passes documents that another ROCS path rejects, while the kernel has an incomplete shift from a vendored offline gate to an environment-dependent sibling checkout.

## Goals

1. Make the current operational Markdown/frontmatter contract explicit.
2. Align ROCS validator and semantic snapshot admission for that contract.
3. Standardize guidance-field placement with a bounded corpus migration.
4. Restore a reproducible required-class consumer gate.
5. Preserve all prior source-format and authority nonclaims.

## Non-goals

- choosing a permanent source format;
- adding normalized authored-form identity or a production semantic digest;
- adding semantic evaluation, Decision 53 adaptation, or editor integration;
- requiring prose and `ont.description` to be byte-equal;
- changing ontology meanings while relocating equivalent guidance fields.

## Proposed contract

### 1. Ownership and authority ceiling

`ontology-kernel` owns the contract and corpus meaning. ROCS enforces the accepted shape but cannot invent fields or meaning. Validation, builds, digests, Git, and generated artifacts never imply approval, release, adoption, activation, use, or currentness.

### 2. Document envelope

A reference document is UTF-8 Markdown with YAML frontmatter. Allowed top-level frontmatter keys are closed:

- required `ont` mapping;
- optional `system4d` mapping.

Unknown top-level keys fail validation and semantic snapshot admission.

`system4d` is non-normative guidance in v1. Its exact admitted shape is an optional mapping containing exactly `fog`; `fog` contains exactly `risks`, `assumptions`, `exceptions`, and `debt`; each value is a list of strings. It is retained in exact source bytes and raw document identity but omitted from lexical retrieval fields. Consumers that project fields rather than exact source must declare that omission. V1 does not define a semantic digest for `system4d`.

### 3. Normative declaration

`ont` is the normative machine-readable declaration. YAML implicit coercion does not satisfy a string or boolean requirement.

| Field | Concept | Relation | Exact v1 shape |
|---|---|---|---|
| `id` | required | required | non-empty string matching the dotted ROCS ID grammar |
| `type` | required | required | exact string `concept` or `relation`, matching location |
| `labels` | required | required | non-empty list of non-empty strings; relation labels are corpus-wide unique |
| `description` | required | required | non-empty string |
| `status` | optional | optional | exact string `active` or `deprecated`; default `active` |
| `deprecated` | conditional | conditional | required only for deprecated documents; mapping with exactly non-empty string keys `since`, `replaced_by`, `decision`; forbidden for active documents |
| `lint_ignore` | optional | optional | list of non-empty advisory lint-rule ID strings; default `[]` |
| `examples` | optional | optional | list of strings; default `[]`; guidance, not authority |
| `anti_examples` | optional | optional | list of strings; default `[]`; guidance, not authority |
| `synonyms` | optional | forbidden | list of strings; default `[]` |
| `relations` | required | forbidden | list of mappings containing exactly `type` and `target`, both non-empty strings |
| `group` | forbidden | required | non-empty string |
| `characteristics` | forbidden | required | mapping containing exactly boolean `transitive` and `symmetric` |
| `axis_default` | forbidden | required | exact string `parents`, `children`, or `left` |
| `inverse` | forbidden | optional | non-empty relation-label string resolving uniquely and reciprocally |

Unknown `ont` keys and forbidden field/kind combinations fail closed. `deprecated.replaced_by` resolves to an existing same-kind ID. `lint_ignore` cannot suppress envelope, schema, type, unknown-field, identity, relation-resolution, deprecation, snapshot-admission, or placeholder errors; it may suppress only rules explicitly classified as advisory in the ROCS rule registry.

### 4. Guidance placement

`examples` and `anti_examples` are standardized under `ont` for both concepts and relations. Existing relation guidance moves without content changes.

Markdown body sections are human guidance and explanation. `## Definition` may elaborate or translate `ont.description`; exact equality is not required. Any machine consumer requiring the normative definition uses `ont.description`.

### 5. Relation references

V1 retains the observed relation-label edge syntax:

```yaml
relations:
  - type: is_a
    target: core.Actor
```

The `type` value must resolve to exactly one relation label, and relation labels used as references are stable within v1. Missing or ambiguous labels fail closed. Targets resolve by stable concept ID.

Stable relation-ID edge syntax remains a possible future migration, not part of this wave. This avoids a breaking fleet-wide ROCS change without evidence of a current wrong-answer consequence.

### 6. Operation matrix and declared loss

Admission and projection are separate. An operation may validate an admitted field without projecting it.

| Operation | Admission/validation | Projected fields | Explicitly omitted fields | Identity |
|---|---|---|---|---|
| `validate` | full envelope, complete per-kind grammar, references, placeholders across exact source | findings and counts only | all source fields except those named in findings/counts | none |
| `summary` | manifest/layer resolution plus document collection | layer metadata and concept/relation counts | every document field and body | none |
| `build` | same v1 schema/reference checks as `validate` | current generated ID index, counts, and authority-ceiling receipts | guidance, body, and any field absent from the documented generated schemas | generated-artifact byte identity only |
| lexical `discover` | full v1 envelope and per-kind grammar | ID, kind, layer, labels, synonyms, description, relation references, examples, anti-examples | status/deprecation, lint metadata, relation group/characteristics/axis/inverse, `system4d`, body | raw document and corpus-snapshot digests |
| exact/bound `pack` | fresh v1 admission plus snapshot binding | exact selected source bytes and pack metadata | unselected documents only, declared by pack config and document list | raw document, corpus-snapshot, and pack digests |

The implementation and public command documentation must preserve this table or publish a reviewed successor. No omission is permission to reinterpret a field. No row creates semantic equivalence, approval, release, adoption, activation, use, or currentness.

### 7. Error behavior

The validator and semantic snapshot parser must share or behaviorally reproduce the exact grammar above, including:

- closed top-level, per-kind, nested deprecation, characteristics, System4D, and edge keys;
- type/location and field/kind consistency;
- exact YAML scalar and list element types without string coercion;
- defaults and forbidden combinations;
- relation-label uniqueness, inverse reciprocity, and edge resolution;
- concept-target and deprecated-replacement resolution;
- unsuppressible admission/schema/reference errors.

They may expose different envelopes for their named operation, but neither may accept a malformed document that the other rejects. Known projection omissions are governed by the operation matrix rather than represented as unknown-field acceptance.

### 8. Consumer wiring

`ontology-kernel` is a ROCS `required` consumer with a nested `ontology/` root.

- Checked-in `tools/rocs-cli` is the reproducible CI and hook dependency.
- `scripts/ci/full.sh` is the standalone acceptance entry point.
- `.gitlab-ci.yml` must invoke `scripts/ci/full.sh`, not the workspace launcher.
- A workspace launcher may exist only as an explicitly non-authoritative developer convenience and must not be the sole CI dependency.
- Acceptance must include a clean-clone test with no sibling `core/rocs-cli` checkout available.
- Hook generation is verified, while activation of `core.hooksPath` remains an explicit local operator action rather than a convergence side effect.
- `ontology_repo` convergence is forbidden for this layout.

## Options considered

### A. Keep current drift

Rejected. Passing one ROCS path while failing another makes validation claims operation-dependent and opaque.

### B. Make the sibling workspace checkout canonical

Rejected. It breaks standalone/offline consumer verification and makes CI depend on workstation layout.

### C. Require only `ont` and delete `system4d`

Rejected. It would discard existing owner-authored guidance without a demonstrated need.

### D. Treat the entire Markdown body as normative

Rejected. It makes harmless explanation and translation changes alter the machine contract and conflicts with observed relation documentation.

### E. Switch relation edges immediately to relation IDs

Deferred. IDs are architecturally cleaner, but the current unique-label contract is deterministic and no current consumer justifies a breaking fleet-wide migration.

## Implementation consequences

If accepted by the cross-repo decision and ADR:

1. Post-ADR implementation and validation/rollout/rollback plans are attached before code tasks become executable.
2. A scoped `rocs-cli` task adds shared closed-envelope validation, restricts `lint_ignore` to advisory rules, admits the exact optional `system4d` guidance shape in semantic snapshots, admits relation guidance under `ont`, documents operation loss, and adds regression fixtures.
3. After ROCS-owner validation, a scoped release task applies the approved SemVer bump; review readiness and the ontology ADR do not themselves authorize that release.
4. A scoped `ontology-kernel` task relocates relation guidance under `ont`, expands schema documentation, converges as `required`, and explicitly rewires `.gitlab-ci.yml` to `scripts/ci/full.sh`.
5. The kernel vendors the exact released ROCS bundle and verifies its manifest.
6. Clean-worktree and no-sibling-checkout tests verify validator, build, summary/pack, semantic discovery admission, generated gates, and CI wiring.

## Rollback

- Revert the ROCS implementation/release commit.
- Revert the kernel corpus/schema/convergence commit.
- Restore the previously pinned vendored ROCS bundle and CI commands.
- Do not roll back by making CI resolve an unpinned sibling checkout.

## Decision requested

Accept the bounded v1 contract, including required-class vendoring, standardized `ont` guidance placement, optional top-level `system4d` guidance, normative `ont.description`, and retained unique relation-label references.
