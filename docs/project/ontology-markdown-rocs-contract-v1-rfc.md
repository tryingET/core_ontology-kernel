---
summary: "RFC for a bounded current-Markdown contract and reproducible ROCS consumer boundary."
read_when:
  - "When reviewing or implementing ontology-kernel and rocs-cli source-contract alignment."
type: "proposal"
---

# RFC: Ontology Markdown / ROCS contract v1

## Status

Revised proposal after [semantic-owner review r1](ontology-markdown-rocs-contract-v1-review-semantic-r1.md) and the controlling [review synthesis r2](ontology-markdown-rocs-contract-v1-review-synthesis-r2.md). This RFC does not authorize implementation.

The governance path is one cross-repo AK decision covering `core/ontology-kernel` and `core/rocs-cli`, with semantic-owner and ROCS-owner review tracks. Implementation becomes lawful only after a complete review set closes `ready_for_adr`, the cross-repo ADR is recorded, post-ADR plans are attached, and separately scoped AK tasks in each repository are created and claimed. Review readiness or an ontology-kernel artifact alone cannot authorize a ROCS package release.

## Inputs

- [Problem brief](ontology-markdown-rocs-contract-v1-problem-brief.md)
- [Evidence note](ontology-markdown-rocs-contract-v1-evidence-note.md)
- [POLARIS model](ontology-source-polaris-model.md)
- [Transcendent synthesis](ontology-source-architecture-transcendent-synthesis.md)
- `core/rocs-cli/docs/project/semantic-discovery-protocol-v0.md`
- `core/rocs-cli/docs/adr/2026-07-13-semantic-release-and-single-canary-adoption.md` (Decision 53)

## Problem

The semantic owner and its deterministic tool disagree about accepted source shape and reproducible consumption. Validation currently passes documents that semantic snapshot admission rejects, while the kernel has an incomplete shift from a vendored offline gate to an environment-dependent sibling checkout.

## Goals

1. Make the current operational Markdown/frontmatter contract executable and explicit.
2. Align ROCS validator and semantic snapshot admission.
3. Standardize guidance-field placement with a meaning-preserving migration.
4. Restore a reproducible required-class consumer gate.
5. Preserve source-format and authority nonclaims.

## Non-goals

- choosing Markdown or any other permanent source format;
- normalized authored-form identity or a production semantic digest;
- semantic evaluation, Decision 53 adaptation, or editor integration;
- byte equality between prose and `ont.description`;
- changing ontology meaning while relocating equivalent guidance;
- changing the accepted semantic-discovery v0 protocol.

This is a supersedable contract for the observed current frontend, not evidence of Markdown superiority.

## Proposed contract

### 1. Ownership and authority ceiling

`ontology-kernel` owns authored meaning and this source contract. ROCS enforces accepted structure without inventing meaning.

Decision 53 remains normative for authority separation. This contract issues no facts for semantic publication, withdrawal, revocation, desired state, consumer intent or acceptance, adoption, activation, deactivation, rollback, use, currentness, or AK decision/task/evidence lineage. Git state, validation, builds, raw digests, generated artifacts, and this decision cannot issue those facts.

The SemVer release described here is an executable `rocs-cli` package release for deterministic tooling. It is not Decision 53 semantic-release publication or consumer adoption.

### 2. File and YAML profile

A v1 reference document obeys this closed envelope:

1. Maximum file size is 1 MiB.
2. Bytes are strict UTF-8 with no BOM.
3. Byte zero begins exact `---\n`; the first later exact `\n---\n` ends frontmatter. CRLF delimiters, a missing delimiter, or another YAML document marker fail.
4. The remaining UTF-8 bytes are the Markdown body and may be empty.
5. Frontmatter uses the safe YAML subset below:
   - root and all nested mappings have string keys;
   - values are only mappings, lists, strings, and booleans admitted by the field grammar;
   - duplicate keys, anchors, aliases, merge keys, explicit tags, recursive/shared nodes, and multiple documents are forbidden;
   - maximum collection depth is 32 and maximum mapping-key plus sequence-item count is 10,000 per document.
6. Allowed top-level keys are exact:
   - concepts: required `ont`, optional `system4d`;
   - relations: required `ont` only.
7. Strict source admission rejects placeholder tokens matching `<[^>]+>` anywhere in the exact document.

ROCS validator and semantic snapshot paths must use one parser or behaviorally identical independent parsers for this profile. A caller-selected lower operation budget may return `resource_exhausted`; it does not redefine which source bytes are schema-valid.

Corpus membership is closed. Under each selected layer source root, `reference/concepts/README.md` and `reference/relations/README.md` are optional narrative files and are excluded. Every other direct-child `*.md` file in those two directories is a reference document and must pass this contract. Subdirectories, symlinks, and other regular files in those directories fail admission; no malformed definition may escape by classification.

### 3. Identity and path grammar

- `ont.id` is a string matching `[A-Za-z0-9_-]+(\.[A-Za-z0-9_-]+)+`.
- IDs are owner-stable and holding-wide unique by ontology policy. ROCS enforces uniqueness across concepts and relations in the complete resolved corpus available to the operation.
- A concept path is exactly `reference/concepts/<ont.id>.md`, relative to its layer source root.
- A relation path is exactly `reference/relations/<primary-label>.md`, where `primary-label` is the first entry of `ont.labels`. Primary relation labels are stable, unique path tokens matching `[A-Za-z0-9_-]+`, and are the labels used by relation references.
- Logical paths are NFC-normalized POSIX paths with no empty, `.`, `..`, backslash, absolute, symlink, or normalization-collision form.
- `ont.type` exactly matches both path class and document kind.

### 4. Per-kind field grammar

YAML implicit coercion does not satisfy a string or boolean requirement.

| Field | Concept | Relation | Exact v1 shape |
|---|---|---|---|
| `id` | required | required | identity grammar above |
| `type` | required | required | exact `concept` or `relation` |
| `labels` | required | required | non-empty list of non-empty strings; relation labels corpus-wide unique |
| `description` | required | required | non-empty string; normative concise definition |
| `status` | optional | optional | exact `active` or `deprecated`; default `active` |
| `deprecated` | conditional | conditional | required only when deprecated; exact non-empty string keys `since`, `replaced_by`, `decision`; forbidden when active |
| `lint_ignore` | optional | optional | exact empty list in v1; non-empty suppression is not admitted |
| `examples` | optional | optional | list of strings; default `[]`; retrieval/authoring guidance only |
| `anti_examples` | optional | optional | list of strings; default `[]`; retrieval/authoring guidance only |
| `synonyms` | optional | forbidden | list of strings; default `[]` |
| `relations` | required | forbidden | list of exact `{type, target}` mappings with non-empty string values |
| `group` | forbidden | required | non-empty string |
| `characteristics` | forbidden | required | exact mapping of boolean `transitive` and `symmetric` |
| `axis_default` | forbidden | required | exact `parents`, `children`, or `left` |
| `inverse` | forbidden | optional | non-empty relation-label string resolving uniquely and reciprocally |

Every admitted field has one owner classification:

| Classification | Fields/surfaces | Change and projection rule |
|---|---|---|
| semantic normative | `id`, `type`, `labels`, `description`, `synonyms`, `relations`, `group`, `characteristics`, `inverse` | changes authored meaning or semantic reference behavior; projections must preserve or explicitly omit |
| lifecycle normative | `status`, `deprecated` | changes semantic-owner lifecycle declaration but never Decision 53 publication/adoption/currentness; projections must preserve or explicitly omit |
| retrieval/authoring guidance | `examples`, `anti_examples`, `system4d`, Markdown body | may affect retrieval or human interpretation; never overrides semantic fields; omission must be explicit |
| presentation | `axis_default` | affects default visualization/layout only; no semantic consequence; omission must be explicit |
| lint metadata | `lint_ignore` | v1 admits only `[]`; carries no meaning or authority |

`labels` include the primary relation path/reference token; changing that token requires an explicit reference and filename migration. This classification is normative for v1 and does not inherit broader conclusions from the source-format experiments.

Additional invariants:

- `deprecated.since` is a valid zero-padded Gregorian date `YYYY-MM-DD`.
- `deprecated.replaced_by` resolves to an existing same-kind ID and is not self.
- `deprecated.decision` is either an absolute `https://` URL or a normalized repo-relative POSIX path without traversal.
- unknown keys and forbidden field/kind combinations fail closed.
- v1 has no suppressible source-admission, schema, reference, placeholder, or lifecycle rule.

Optional concept `system4d` is non-normative guidance with exact shape:

```yaml
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
```

`system4d` contains exactly `fog`; `fog` contains exactly those four keys; every value is a list of strings. Exact source and raw document identity retain it, while lexical discovery omits it as declared below. V1 defines no semantic digest for it.

### 5. Guidance and prose

`examples` and `anti_examples` live under `ont` for both kinds. Existing relation guidance moves there without text changes.

Markdown body sections are human explanation. `## Definition` may elaborate or translate `ont.description`; exact equality is not required. Machine consumers use `ont.description` as the normative concise definition.

### 6. Relation references

V1 retains the observed relation-label edge syntax:

```yaml
relations:
  - type: is_a
    target: core.Actor
```

`type` resolves to exactly one relation label. Labels used as references are stable within v1; missing, ambiguous, or renamed-without-migration labels fail. `target` resolves by concept ID.

Stable relation-ID edges remain a possible future migration. No current wrong-answer consequence justifies a breaking fleet-wide change in this wave.

### 7. Opt-in and compatibility boundary

V1 is activated per layer by exact manifest declaration:

```yaml
rocs:
  source_contract: ontology-markdown-v1
```

A layer without that selector retains the pre-v1 ROCS source behavior. The selector is read from the manifest adjacent to that layer's `src` root, so mixed resolved views dispatch each layer through its declared contract before cross-layer identity/reference checks. This wave opts in only `ontology-kernel`; it does not silently change other consumers or ref layers.

Every command that opens reference documents must use the same per-layer contract dispatcher. The affected public set is `validate`, `build`, `summary`, `lint`, `diff`, `graph`, `check-inverses`, `normalize`, `pack`, bound `pack`, and `discover`, plus any internal helper they call. `rules` may describe rules without opening documents; `explain` must use the dispatcher when it opens a document.

Unbound interactive `pack` remains supported and emits its existing human/JSON shape after v1 admission. Bound `pack` remains the semantic-discovery-v0 snapshot-bound protocol operation. The RFC does not merge their identities or output contracts. Because the new grammar is opt-in, the tooling release is a minor `0.3.0` capability addition; any future default-on or legacy-removal change requires a new breaking-policy decision.

### 8. Operation projection and identity

The raw identities below normatively reuse `semantic-discovery-protocol-v0`: SHA-256 over exact raw document bytes, and RFC 8785/JCS object digests with the protocol's digest-omitted pseudotypes. Corpus-snapshot and bound-pack preimages, field sets, algorithm IDs, ordering, and error envelopes remain those of that protocol. They are raw/protocol identities, not semantic equivalence or authority.

| Operation | Required admission | Internal field use | Emitted projection | Declared omission |
|---|---|---|---|---|
| `validate` | complete v1 grammar and references | all admitted structure; exact bytes for placeholders | findings and counts | source fields not named by a finding/count |
| `summary` | complete v1 grammar and references | IDs, kinds, layers | layers and counts | all document fields and body |
| `build` | complete v1 grammar and references | fields required by documented generated schemas | ID index, summary/counts, authority-ceiling receipts | guidance, body, and fields absent from generated schemas |
| lexical `discover` | complete v1 grammar and references | ID, labels, synonyms, description, relation references, examples, anti-examples | protocol candidate identity, score, matched query tokens, bounded field/rule evidence, raw document digest | source field values, status/deprecation, lint metadata, relation metadata, `system4d`, body |
| unbound `pack` | complete v1 admission | selected exact source text and traversal metadata | existing interactive text/JSON pack shape | unselected documents according to pack configuration |
| bound `pack` | fresh complete v1 admission and semantic-discovery-v0 snapshot binding | exact selected source bytes | closed semantic-discovery-v0 pack protocol | only unselected documents, explicit in config/document list |

Lexical source values are scoring inputs, not automatic prompt injection. Full source content appears only through explicit exact/bound pack output. A known omission cannot be reinterpreted as absence or permission to invent meaning.

### 9. Error precedence

For one operation, the first applicable class wins:

1. file-size/resource limit;
2. UTF-8/BOM/frontmatter envelope;
3. forbidden YAML construct, duplicate key, or YAML parse;
4. top-level and per-kind schema/type/unknown-field;
5. ID/type/path/uniqueness;
6. deprecation, inverse, relation-label, and target reference;
7. placeholder.

Validator findings may use operation-specific rule IDs, while semantic discovery uses its closed error envelope. Both must classify the same source as accepted or rejected when run with sufficient operation budgets.

### 10. Reproducible tooling release and rollback

The canonical `rocs-cli` tooling release identity is the tuple:

```text
SemVer + immutable Git commit + pyproject SHA-256 + uv.lock SHA-256
+ VENDORED_HASHES schema/version + bundle_manifest_digest
```

The release is built from a clean tagged commit under Python 3.12 / Unicode 15.0.0 with `uv sync --frozen`; runtime dependency trees come only from that lock-resolved environment. `VENDORED_HASHES.json` records the source commit, lock digest, every included path digest, and `bundle_manifest_digest`, defined as SHA-256 over RFC 8785/JCS bytes of the sorted path-to-digest mapping plus release identity fields, excluding only `bundle_manifest_digest`. Two isolated builds from the same commit and lock must be byte-identical before release acceptance.

The tag is immutable. Rollback is a consumer repin to a previously accepted exact bundle/manifest or a forward corrective release; neither a published version nor tag is rewritten or represented as retracted by reverting a source commit.

### 11. Consumer wiring and executable acceptance

`ontology-kernel` is a ROCS `required` consumer with nested `ontology/` layout. Its manifest adds:

```yaml
rocs:
  layer: core
  source_contract: ontology-markdown-v1
  profiles:
    default: kernel-v1
    kernel-v1:
      include_layers: [core]
```

- Checked-in `tools/rocs-cli` is the reproducible CI/hook dependency.
- `scripts/ci/full.sh` is the standalone acceptance entry point.
- `.gitlab-ci.yml` uses Python 3.12 and invokes `scripts/ci/full.sh`, not a workspace launcher.
- A checked-in semantic-discovery-v0 request fixture uses profile `kernel-v1` and development-snapshot identity.
- The gate derives the adopted-runtime tool-manifest digest from the verified vendored manifest, runs discovery with `--json --no-index-cache --no-env-file`, and uses the returned corpus/document digests to exercise bound pack; it separately exercises unbound pack.
- Acceptance runs from a clean detached worktree or clone whose parent contains no sibling `core/rocs-cli` checkout and with `ROCS_WORKSPACE_ROOT` unset.
- The matrix covers `vendored-check`, `validate`, `build`, `summary`, `lint`, `graph`, `check-inverses`, `normalize` dry-run/no-write behavior, unbound pack, discover, bound pack, generated hook, and CI script. `diff` is covered by ROCS package tests using two v1 fixtures because it requires two corpus states.
- Hook generation is verified; `core.hooksPath` activation remains an explicit local operator action.
- `ontology_repo` convergence is forbidden for this nested layout.

## Options considered

- **Keep current drift:** rejected; one ROCS path passing while another rejects is opaque.
- **Make sibling checkout canonical:** rejected; it breaks standalone/offline reproducibility.
- **Delete `system4d`:** rejected; it discards owner-authored guidance without need.
- **Treat body as normative:** rejected; explanation and translation would change the machine contract.
- **Switch edges to relation IDs now:** deferred; current unique-label resolution is deterministic and a fleet break is unjustified.
- **Allow general YAML:** rejected; parser divergence and expansion hazards defeat closed admission.
- **Allow non-empty `lint_ignore`:** deferred until a separately reviewed, versioned advisory-rule registry exists.
- **Change all ROCS consumers at once:** rejected; the manifest selector makes adoption explicit and preserves legacy behavior elsewhere.
- **Treat ambient vendoring as a release identity:** rejected; self-consistency is not reproducibility.

## Implementation consequences

If accepted by the cross-repo decision and ADR:

1. Attach implementation and validation/rollout/rollback plans.
2. Create and claim a scoped `rocs-cli` task to implement the opt-in shared parser/grammar dispatcher across every affected operation, validator/snapshot parity, deterministic bundle identity, operation-loss documentation, and adversarial/legacy-compatibility fixtures.
3. After ROCS-owner validation and isolated double-build proof, create and claim a separate release task for tooling release `0.3.0`, update the lock, commit, tag the exact source commit, and preserve the release manifest evidence.
4. Create and claim a scoped `ontology-kernel` task to relocate relation guidance, add the selector/profile/request fixture, update schema docs, converge as `required`, rewire CI to Python 3.12 and the generated gate, and remove the workspace launcher from acceptance.
5. Vendor the exact released bundle and verify its source commit, lock, file hashes, and bundle-manifest digest.
6. Prove the executable acceptance matrix in a clean no-sibling environment.

## Rollback

- Before publication, abandon/revert the candidate implementation normally.
- After an immutable tooling release exists, do not rewrite its commit or tag; issue a forward corrective release if package bytes are defective.
- Revert the kernel schema/corpus/selector/convergence commit and repin its complete vendored tree to the previously accepted exact manifest.
- Restore the prior CI commands only with that previous vendored pin.
- Never use an unpinned sibling checkout as rollback.

## Decision requested

Accept this bounded, supersedable v1 contract: required-class vendoring; exact current-frontmatter grammar; relation guidance under `ont`; concept-only non-normative `system4d.fog`; normative `ont.description`; retained unique relation-label references; protocol-bound raw identities; and Decision 53 authority separation.
