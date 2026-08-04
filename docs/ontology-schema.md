---
summary: "Accepted ontology-markdown-v1 source grammar, field ownership, and conformance ceiling."
read_when:
  - "When adding or changing ontology files"
  - "When implementing validators, builders, retrieval, or projections"
---

# Ontology schema (kernel)

This repository opts into `rocs.source_contract: ontology-markdown-v1`.
Markdown/frontmatter remains the current operational frontend; this contract does not declare it a permanent source-format winner.

## Conformance ceiling

ROCS may report only operation-qualified **source-contract/schema/reference conformance** for the exact completely admitted corpus. It does not report broad semantic correctness and cannot create package publication, semantic publication, desired state, consumer adoption, activation, use, currentness, or AK lifecycle facts.

A failed, partial, or resource-exhausted operation emits no corpus-conformance claim.

## File envelope

A definition is a direct regular `*.md` child of:

- `ontology/src/reference/concepts/`
- `ontology/src/reference/relations/`

Exact `README.md` files are narrative and excluded. Subdirectories, symlinks, special files, and other regular files fail closed.

Definition files:

- are at most 1 MiB;
- are strict UTF-8 without BOM;
- begin with exact `---\n` and close frontmatter at the first exact `\n---\n`;
- use one safe YAML document with string keys, maximum depth 32, and at most 10,000 collection items;
- reject duplicate keys, aliases, anchors, merges, explicit tags, additional YAML documents, and `<...>` placeholders.

Within one document, errors follow: resource, envelope, YAML, schema, identity/path, lifecycle/reference, placeholder.

## Identity and paths

`ont.id` matches:

```text
[A-Za-z0-9_-]+(\.[A-Za-z0-9_-]+)+
```

IDs are owner-stable and unique across concept/relation kinds in the resolved corpus.

- concept path: `reference/concepts/<ont.id>.md`
- relation path: `reference/relations/<primary-label>.md`

The primary relation label is `ont.labels[0]`, matches `[A-Za-z0-9_-]+`, and is the stable v1 edge/inverse reference token.

## Field grammar

| Field | Concept | Relation | Shape / owner class |
|---|---|---|---|
| `id` | required | required | dotted string; semantic normative |
| `type` | required | required | exact `concept` / `relation`; semantic normative |
| `labels` | required | required | non-empty list of non-empty strings; semantic normative |
| `description` | required | required | non-empty string; normative concise definition |
| `status` | optional | optional | `active` default or `deprecated`; lifecycle normative |
| `deprecated` | conditional | conditional | exact `since`, `replaced_by`, `decision` strings; lifecycle normative |
| `lint_ignore` | optional | optional | exact `[]` in v1; lint metadata |
| `examples` | optional | optional | string list; retrieval/authoring guidance |
| `anti_examples` | optional | optional | string list; retrieval/authoring guidance |
| `synonyms` | optional | forbidden | string list; semantic normative |
| `relations` | required | forbidden | exact `{type, target}` list; semantic normative |
| `group` | forbidden | required | non-empty string; semantic normative |
| `characteristics` | forbidden | required | exact boolean `transitive`, `symmetric`; semantic normative |
| `axis_default` | forbidden | required | `parents`, `children`, or `left`; presentation only |
| `inverse` | forbidden | optional | unique reciprocal relation label; semantic normative |

Unknown keys and forbidden kind/field combinations fail closed.

### Deprecation

When `status: deprecated`:

- `since` is a valid zero-padded Gregorian `YYYY-MM-DD` date;
- `replaced_by` resolves to a different existing same-kind ID;
- `decision` is an absolute HTTPS URL or normalized repo-relative POSIX path.

`deprecated` is forbidden while active.

### Concept relations

Each edge is exact:

```yaml
relations:
  - type: is_a
    target: core.Actor
```

`type` resolves to exactly one relation label and `target` to an existing concept ID. Stable relation-ID edges are deferred beyond v1.

### Concept System4D guidance

Concepts may contain exact top-level guidance:

```yaml
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
```

Each fog value is a string list. `system4d` is forbidden on relations in v1 and is not a semantic or authority fact.

## Prose

Markdown body sections are human guidance. `## Definition` may elaborate or translate `ont.description`; exact equality is not required. Machine consumers use `ont.description` as the normative concise definition.

## Operational reference

The accepted decision is [Decision 110 ADR](adr/2026-08-03-ontology-markdown-rocs-contract-v1.md). ROCS implementation details live in `core/rocs-cli/docs/project/ontology-markdown-v1.md`.
