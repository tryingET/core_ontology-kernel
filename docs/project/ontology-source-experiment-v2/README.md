---
summary: "Frozen v2 protocol bundle for the four-way ontology source architecture comparison."
read_when:
  - "Implementing, reviewing, or replaying the ontology source architecture experiment."
  - "Interpreting ontology source experiment results or winner/no-winner disposition."
type: design
status: proposed
---

# Ontology source experiment protocol v2

## Status

This bundle freezes the executable choices left open by `../ontology-source-architecture-comparative-experiment.md`. It remains proposed until an independent rereview returns no blocking defect.

No artifact in this directory is ontology truth, a production ROCS contract, a semantic release, an authority fact, or permission to migrate source.

Protocol revision v2 intentionally retains nested experimental source-format identifiers ending in `.v0` (`rocs-source-experiment.v0`, `rocs-semantic-object-experiment.v0`, and the bounded RDF v0 profile). Those identify unchanged candidate encodings; the surrounding execution protocol, accepted inputs, scoring, evidence rules, and command allowlist are v2.

Protocol v2 differs from rejected v1 only by making the actor command contract internally executable: it explicitly permits the exact unscored warm-up validation, scored variant validation, and V4 atomic authoring argv/redirection forms. No semantic fixture, oracle, architecture, metric, or winner rule changed.

## Frozen bundle

| Artifact | Purpose |
|---|---|
| `protocol-manifest.v2.json` | SHA-256 inventory and aggregate digest of every other frozen protocol artifact. |
| `field-inventory.v2.json` | Exhaustive classification and normalization of observed and synthetic fields. |
| `baseline-manifest.v2.json` | Exact Git tree, fixture paths, Git blobs, and SHA-256 source-byte digests. |
| `fixture-files.v2.json` and `fixtures/` | Exact frozen V1–V4 baseline source bytes and their SHA-256 manifest. |
| `accepted-inputs-manifest.v2.json` and `accepted-inputs/` | Forty byte-exact source packets: every golden case for every variant. |
| `task-fixtures.v2.json` | Exact T1–T6 prompts, starting overlays, branch bytes, digests, and expected golden cases. |
| `golden-cases.v2.json` | Exact accepted-case canonical fact streams and semantic digests. |
| `malformed-cases.v2.json` | Exact adversarial payloads, applicability, errors, and precedence. |
| `variant-contracts.v2.md` | Frozen V1–V4 syntax, topology, dependency, and maintained/generated boundaries. |
| `decision-rule.v2.json` | Mechanical correctness, complexity, dominance, tie, and no-winner rules. |
| `complexity-measurement.v2.json` | Exact median, LOC, contract-byte, dependency, error, and surface algorithms. |
| `evidence-manifest-contract.v2.json` | Exact retained-evidence and operator-status byte verification contract. |
| `actor-materials/` | Frozen actor/reviewer instructions, tools, validation help, warm-up, blind mapping, and normalization. |
| `runbook.v2.md` | Independent implementation, ergonomics, isolation, evidence, and cleanup protocol. |

Before implementation, compute SHA-256 for every bundle artifact in lexical path order and record the resulting manifest as the `protocol_digest`. Any content change creates a new protocol revision and invalidates prior runs.

## Canonical fact stream

A canonical fact is a JSON array. The stream is formed as follows:

1. Every Unicode string is normalized to NFC.
2. Numbers are forbidden in protocol v2 semantic facts; booleans are JSON `true` or `false`; missing optional values are represented by absence of a fact, not `null`.
3. Each fact is serialized as UTF-8 JSON with no insignificant whitespace, no ASCII-only escaping, and only JSON-required escaping.
4. Fact arrays are sorted by unsigned UTF-8 byte order of their serialized lines.
5. Duplicate serialized facts are an error; they are not deduplicated silently.
6. Lines are joined with LF and the stream ends with exactly one LF.
7. `semantic_digest = sha256(canonical_fact_stream_bytes)` in lowercase hexadecimal.

Allowed protocol v2 fact shapes are closed:

```text
["term", term_id, "concept" | "relation"]
["label", term_id, "und", lexical_form]
["synonym", term_id, "und", lexical_form]
["definition", term_id, "und", lexical_form]
["assertion", assertion_id, subject_id, relation_id, object_id]
["relation_group", relation_id, group_id]
["relation_characteristic", relation_id, "transitive" | "symmetric", boolean]
["inverse", relation_id, inverse_relation_id]
["lifecycle", term_id, "active"]
["lifecycle", term_id, "deprecated", since_text, replacement_id, decision_ref]
```

`assertion_id` is exactly:

```text
assert:<subject_id>:<relation_id>:<object_id>
```

The protocol v2 semantic fact stream excludes guidance, System4D, layout, source provenance, owner authority, and current-head facts. Those remain available to source/debug and projection-loss reports where required.

## Identity distinctions

The experiment uses four distinct identities:

| Identity | Meaning | Label-only rename behavior |
|---|---|---|
| `term_id` | Stable entity identity, e.g. `core.Agent`. | Preserved. |
| `semantic_digest` | Digest of all selected semantic-content facts. | Changes because labels are selected semantic facts. |
| `source_debug_digest` | Variant-specific authored bytes and provenance. | Changes. |
| authority/currentness identity | Owner-issued state outside semantic content. | Not derivable from any source variant or semantic digest. |

The earlier phrase “label-only rename preserves semantic identity” is replaced by the precise requirement: a label rename preserves `term_id` but changes `semantic_digest` in protocol v2.

## Exact field decisions

The machine-readable inventory is controlling. Its main consequences are:

- `ont.labels`, `ont.synonyms`, and `ont.description` participate in semantic digest.
- concept relation assertions participate after relation labels are resolved through the frozen legacy-label map and normalized to stable relation IDs;
- `ont.group`, `ont.characteristics.transitive`, `ont.characteristics.symmetric`, and `ont.inverse` participate;
- `ont.axis_default` is layout/presentation and does not participate;
- examples and anti-examples are non-normative guidance and do not participate;
- all `system4d` content is non-normative guidance in protocol v2 and does not participate;
- Markdown body content is non-normative guidance unless an exact restatement marker is present;
- `ont.lint_ignore`, source path, source revision, and source byte digest are source/debug provenance and do not participate;
- approval, publication, desired state, currentness, acceptance, activation, use, delivery, influence, owner-store heads, and AK facts are forbidden in semantic source.

There are no `if selected` fields in protocol v2.

## Legacy relation-label map

Only the following mappings are available to the V1 baseline fixture adapter:

```text
is_a          -> core.rel.is_a
depends_on    -> core.rel.depends_on
conflicts_with -> core.rel.conflicts_with
```

V1 authoring tasks must write stable IDs. Use of any relation label outside the frozen baseline adapter fails with `E_RELATION_ID_REQUIRED`.

## Authority ownership

Lifecycle stages do not map positionally to the six participating owners. Use this table instead:

| Fact or operation | Owning/issuing surface | ROCS role |
|---|---|---|
| authored semantic bytes | ontology/semantic owner repository | parse and validate deterministically |
| semantic release approval/publication/withdrawal | semantic owner | verify owner-issued inputs; do not self-approve |
| desired consumer state | consumer owner | verify input shape/joins only |
| acceptance/activation/deactivation/rollback policy | consumer owner | materialize only under valid owner inputs |
| task, decision, evidence, revocation/supersession lineage | AK | verify references; do not issue AK facts |
| delivery/suppression/failure attestation | Pi | no authority transfer |
| accepted recovery execution | independently pinned recovery controller | validate protocol effects where applicable |
| empirical influence analysis | DSPx/Oracle | no normative authority |

The experiment tests rejection of semantic content that claims any authority-bearing field.

## Frozen accepted cases

`golden-cases.v2.json` contains these exact cases:

1. `baseline`;
2. `add_term`;
3. `label_rename`;
4. `definition_change`;
5. `edge_wrong`;
6. `deprecation`;
7. `merge_label_and_guidance`;
8. `unicode_nfc`;
9. `unicode_nfd_equivalent`;
10. `source_reorder_equivalent`.

Every accepted case carries the complete canonical stream and expected digest. Implementations are scored independently against that oracle before A↔B comparison.

Expected relationships are also frozen:

- baseline and source reorder: equal `term_id` set and equal semantic digest;
- Unicode NFC and NFD: equal semantic digest after NFC normalization;
- label rename: equal `term_id` set and different semantic digest from baseline;
- add, definition, wrong-edge, deprecation, and merge-label changes: different semantic digest from baseline;
- guidance-only additions do not alter semantic digest, while the T6 label change does.

## Frozen malformed cases

`malformed-cases.v2.json` controls applicability. An implementation cannot choose `not_applicable`. Every applicable payload has:

- exact UTF-8 source bytes embedded as text;
- source SHA-256;
- variant and entrypoint;
- expected accept/reject disposition;
- expected typed error;
- expected precedence if more than one defect exists.

Closed error vocabulary:

| Error | Meaning |
|---|---|
| `E_DUPLICATE_KEY` | A JSON/YAML mapping key repeats before deserialization. |
| `E_YAML_ALIAS_FORBIDDEN` | YAML alias, anchor, or merge syntax occurs. |
| `E_AMBIGUOUS_SCALAR` | YAML scalar relies on implicit non-string typing where text is required. |
| `E_UNKNOWN_FIELD` | Closed source/profile contains an undeclared field or predicate. |
| `E_TYPE` | Declared field has the wrong primitive/container type. |
| `E_UNICODE_COLLISION` | Distinct source values normalize to one prohibited duplicate. |
| `E_DUPLICATE_ID` | Corpus defines one stable ID more than once. |
| `E_RELATION_ID_REQUIRED` | An authored assertion uses a label rather than a stable relation ID. |
| `E_RESTATEMENT_CONFLICT` | Marked Markdown restatement differs from normative definition after NFC and LF normalization. |
| `E_UNSUPPORTED_RDF` | RDF/OWL construct is outside the closed v0 profile. |
| `E_AUTHORITY_FIELD_FORBIDDEN` | Semantic source contains an authority/currentness field or predicate. |
| `E_PROJECTION_FALSE_COMPLETENESS` | Projection claims completeness while omitting selected semantic facts. |

When multiple errors exist, implementations must return the lexically first error code in this table's controlling numeric precedence from `malformed-cases.v2.json`; no parser-native accident decides the result.

## V1 Markdown restatement rule

Markdown body text is guidance by default. A normative restatement check is activated only by this exact marker on the line immediately following a `## Definition` heading:

```markdown
<!-- rocs:restates ont.description -->
```

The next non-empty paragraph, continuing until the next heading or blank line, must equal `ont.description` after NFC normalization and CRLF-to-LF normalization. Absence of the marker creates no restatement claim. A mismatch fails with `E_RESTATEMENT_CONFLICT`.

## Winner/no-winner rule

Correctness is conjunctive. A variant with one applicable correctness failure is excluded.

For correctness-passing variants, calculate the exact complexity vector defined in `decision-rule.v2.json`:

```text
(
  hand_maintained_semantic_surfaces_per_term,
  authoring_task_errors,
  median_paired_task_seconds,
  new_production_semantic_loc,
  custom_normative_contract_bytes,
  added_direct_runtime_dependencies
)
```

Lower is better. Dominance is Pareto dominance: no worse in every measured dimension and strictly better in at least one. Raw LOC is never used alone.

Mechanical disposition:

1. No correctness-passing variant -> `no_winner_retain_current`.
2. Exactly one correctness-passing variant -> it is the technical winner only if ergonomics evidence is sufficient; otherwise `no_winner_retain_current`.
3. Multiple passing variants with exactly one Pareto-undominated variant -> that variant wins only if ergonomics evidence is sufficient.
4. Multiple Pareto-undominated variants including V1 -> `no_winner_retain_current`; retain V1 operationally because migration burden is unearned, not because V1 is proven superior.
5. Multiple Pareto-undominated variants excluding V1 -> `no_winner_incomparable`.
6. Missing or insufficient selecting evidence -> `no_winner_insufficient_evidence`.

Only one mechanically demonstrated winner can advance to architecture RFC consideration. Retaining current behavior is not an ADR approval of Markdown's permanence.

## Ergonomics evidence

Protocol v2 uses eight fresh stateless Pi sessions running `openai-codex/gpt-5.6-sol` under the same checked-in tool/instruction surface. Each actor performs the six selecting authoring tasks for all four variants under the Latin-square order in `runbook.v2.md`. The remaining projection and rejection tasks are correctness tests, not ergonomics samples.

The 10% median rule is removed. Selection uses paired results and the fixed complexity vector. If the exact model/provider or eight-session cohort is unavailable, ergonomics is `insufficient_evidence`, and no non-status-quo source migration winner may be claimed.

## Reversibility

Execution uses:

1. one immutable clean baseline checkout at the bound commit;
2. four separate writable per-variant fixture copies under managed disk-backed temporary storage;
3. one retained evidence root outside disposable copies;
4. no writes to the operator's dirty checkout.

Before any compiler code runs, retain the protocol digest, baseline manifest, baseline checkout Git status, and SHA-256 source-tree manifest. Before deleting disposable variant copies, copy all receipts, streams, digests, patches, timings, logs, and failure payloads into the retained evidence root and verify its manifest.

## Next legal move

Request independent rereview of this bundle and the corrected parent documents. Do not start canonicalizer or variant implementation until the rereview returns `PASS` and `execution ready` with no blocking protocol defect.
