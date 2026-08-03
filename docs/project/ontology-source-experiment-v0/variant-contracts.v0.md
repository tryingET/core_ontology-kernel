---
summary: "Frozen syntax, topology, and maintained/generated boundaries for ontology experiment variants V1 through V4."
read_when:
  - "Implementing or reviewing any ontology source experiment variant."
type: reference
status: proposed
---

# Variant contracts v0

## Common constraints

All variants represent the same field inventory and target the same golden fact oracle. They must:

- keep one hand-maintained semantic input action per term change;
- reject unknown semantic fields;
- preserve guidance and layout only through declared non-semantic channels;
- emit the closed fact stream from `README.md`;
- emit variant-specific source/debug digest and projection-loss metadata;
- reject authority/currentness fields;
- run without network access;
- use only dependencies locked before implementation freeze;
- write only within the assigned writable variant root and evidence root.

A compiler may not reinterpret another variant's output.

## V1 — Hardened Markdown/frontmatter

### Source topology

```text
concepts/<stable-term-id>.md
relations/<stable-relation-id>.md
```

Within the protocol bundle, exact V1 bytes use a terminal `.fixture` storage suffix so repository documentation tooling does not interpret them as live docs. The fixture materializer strips only that final suffix before compiler or actor use; resulting source names end in `.md`.

One Markdown file is the sole hand-maintained semantic source per term. Front matter is YAML 1.2 core-schema syntax restricted further as follows:

- exact `---\n` opening and closing delimiters;
- UTF-8 without BOM;
- mappings and sequences only;
- duplicate keys rejected lexically;
- anchors, aliases, tags, directives, and merge keys forbidden;
- all text scalars double-quoted except closed enum keys/values explicitly allowed by the field inventory;
- dates remain quoted strings;
- booleans are exactly `true` or `false`;
- unknown top-level keys rejected except `ont`, `system4d`, and relation guidance keys `examples`, `anti_examples`;
- unknown `ont` keys rejected.

The experiment fixture mechanically rewrites baseline concept edge `type` labels and relation `inverse` labels through the frozen three-entry map before freeze. After freeze, stable relation IDs are required.

### Body boundary

The body is non-normative guidance. Only the exact marker defined in `README.md` creates a restatement assertion. The marked paragraph must match `ont.description`; mismatch is `E_RESTATEMENT_CONFLICT`.

### Maintained/generated boundary

- maintained: one `.md` source per term;
- generated: canonical facts, digests, cards, RDF, graph JSON, diagrams, indexes;
- no sidecar is hand-maintained.

### Allowed parser dependency

One locked YAML 1.2 parser per implementation, preceded by an implementation-owned lexical scanner. Parser defaults do not override the closed lexical rules.

## V2 — Strict JSON records

### Source topology

```text
concepts/<stable-term-id>.json
relations/<stable-relation-id>.json
```

One JSON file is the sole hand-maintained semantic source per term. Encoding is strict UTF-8 JSON:

- RFC 8259 object syntax;
- UTF-8 without BOM;
- duplicate keys rejected lexically before object construction;
- no comments or trailing commas;
- JSON strings for all text/date/reference values;
- JSON booleans only for characteristics;
- exact top-level object keys: `schema`, `ont`, optional `guidance`, optional `system4d`;
- `schema` is exactly `rocs-source-experiment.v0`;
- `ont` follows `field-inventory.v0.json`;
- `guidance` contains `examples`, `anti_examples`, and optional ordered `sections` only;
- unknown fields rejected.

Concept assertion shape is exactly:

```json
{"relation_id":"core.rel.is_a","target_id":"core.Actor"}
```

Relation inverse is a stable `relation_id` string. Ordering of object keys is nonsemantic; labels, synonyms, and assertions have set semantics; guidance sections have sequence semantics.

### Maintained/generated boundary

- maintained: one `.json` source per term;
- generated: Markdown and every other projection;
- no Markdown sidecar is hand-maintained.

### Allowed parser dependency

Only the runtime's standard JSON parser after an implementation-owned duplicate-key lexical check.

## V3 — RDF/Turtle plus SHACL

### Source topology

```text
ontology.ttl
shapes.ttl
GUIDANCE.md
```

`ontology.ttl` is the sole hand-maintained source for semantic facts and typed nonsemantic guidance in the bounded fixture. `shapes.ttl` is protocol-owned and identical for all actors; actors do not edit it. `GUIDANCE.md` is generated from nonsemantic RDF predicates and is not a second maintained surface.

### IRI mapping

Stable IDs map bijectively:

```text
https://ontology.ai-society.invalid/id/<stable-id>
```

`<stable-id>` is the exact NFC ROCS ID. ASCII letters, digits, `.`, `_`, `-`, and `~` remain literal; all other UTF-8 bytes are uppercase percent-encoded. Reverse mapping rejects noncanonical encodings.

Vocabulary base:

```text
https://ontology.ai-society.invalid/schema/
```

Closed predicates/classes:

```text
rdf:type
rdfs:label
skos:definition
skos:altLabel
owl:TransitiveProperty
owl:SymmetricProperty
owl:inverseOf
rocs:Concept
rocs:Relation
rocs:relationGroup
rocs:transitive
rocs:symmetric
rocs:status
rocs:deprecatedSince
rocs:replacedBy
rocs:decisionRef
rocs:example
rocs:antiExample
rocs:guidanceMarkdown
rocs:system4dJson
rocs:axisDefault
```

Concept assertions use the stable relation IRI directly as predicate. `rdfs:label`, `skos:definition`, and `skos:altLabel` must use language tag `und`. Relation groups and lifecycle text use `xsd:string`; deprecated dates use `xsd:date` but canonicalize to the exact lexical `YYYY-MM-DD` text in facts. `rocs:transitive` and `rocs:symmetric` are required explicit `xsd:boolean` source facts; a generated OWL projection additionally emits the matching OWL property class when true. `rocs:example`, `rocs:antiExample`, `rocs:guidanceMarkdown`, `rocs:system4dJson`, and `rocs:axisDefault` are closed nonsemantic source predicates excluded from the semantic digest but included in source/debug and projection-loss reports.

### Supported profile

- RDF 1.1 named IRIs and literals only;
- no blank nodes;
- no RDF-star;
- no lists/containers;
- no imports;
- no punning outside a relation IRI being both `rocs:Relation` and RDF property;
- only the listed OWL property characteristic classes and `owl:inverseOf`;
- closed SHACL node/property shapes;
- duplicate identical triples rejected as `E_DUPLICATE_KEY` for experiment parity rather than silently set-collapsed;
- every unlisted predicate/class or OWL construct fails with `E_UNSUPPORTED_RDF` or `E_UNKNOWN_FIELD` according to the malformed manifest.

Guidance, System4D JSON, and axis defaults may be encoded only through their listed nonsemantic predicates. Diagram layout remains external. Authority facts are forbidden. Semantic compilation ignores the nonsemantic predicate values while source/debug and loss reports preserve their presence.

### Maintained/generated boundary

- maintained: one bounded `ontology.ttl` semantic dataset;
- protocol-owned: `shapes.ttl`;
- generated: guidance Markdown and other projections.

The surface count is normalized per changed term as one semantic dataset edit, while merge-conflict and diff metrics record shared-file contention explicitly.

### Allowed dependencies

Each implementation chooses one locked RDF 1.1 parser and one locked SHACL validator before code freeze. A and B must use different RDF parser implementations. Network and remote context/import resolution are forbidden.

## V4 — Immutable semantic objects plus generated head

### Source topology

```text
objects/sha256/<first-two>/<remaining-hex>.json
head.json
```

The authoring interface is a local offline command receiving exactly one strict JSON term payload on stdin. The command validates it, writes one immutable canonical object at its content digest, and atomically regenerates `head.json`. Actors do not hand-edit object filenames or `head.json`.

Object payload schema is:

```json
{
  "schema":"rocs-semantic-object-experiment.v0",
  "term": {"...":"same closed semantic fields as V2"},
  "guidance": {"examples":[],"anti_examples":[],"system4d":null},
  "presentation": {"axis_default":null}
}
```

The object digest is SHA-256 over RFC 8785 JCS bytes of the complete payload, including guidance. Object identity is therefore a source/debug identity, not the semantic digest.

`head.json` is generated in RFC 8785 JCS form:

```json
{
  "schema":"rocs-semantic-head-experiment.v0",
  "terms":{"core.Agent":"<64-lowercase-hex>","...":"..."}
}
```

The head is content-addressed for reproducibility but carries no approval/currentness authority. The filename `head.json` means fixture selection only.

Assertions remain inside the subject term object and use stable relation IDs. The compiler loads only objects named by the generated head, verifies each object digest, and emits the common facts.

### Maintained/generated boundary

- one author input action: strict JSON payload on stdin;
- immutable object: generated from that action and retained as semantic source history;
- head manifest: generated atomically, never hand-maintained;
- all projections: generated.

If the author must manually repair both object and head, the task is scored as an error and the variant violates the one-action constraint.

### Allowed dependencies

Runtime standard JSON plus one locked RFC 8785 implementation, or an independently implemented JCS encoder covered by the golden byte fixtures. No object database or network service is allowed.

## Projection obligations

Every variant emits metadata with:

```json
{
  "status":"lossless|semantically_complete|partial",
  "semantic_digest":"<hex>",
  "included_fact_kinds":["..."],
  "omitted_semantic_fact_kinds":["..."],
  "omitted_guidance_paths":["..."],
  "authority":"non_authoritative_projection"
}
```

- canonical fact stream: `lossless`;
- RDF within the supported profile: `semantically_complete`;
- generated Markdown: `semantically_complete` plus guidance inclusion/omission list;
- compact card: `partial` with exact omitted fact kinds/term IDs;
- graph JSON: `partial` unless it includes definitions, labels, lifecycle, and relation characteristics;
- editor bundle and `.odiagram`: `partial`, digest-bound, non-authoritative.

A completeness claim inconsistent with emitted facts fails `E_PROJECTION_FALSE_COMPLETENESS`.
