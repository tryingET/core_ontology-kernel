---
summary: "Observed corpus, ROCS behavior, and consumer-convergence evidence for the ontology Markdown / ROCS contract decision."
read_when:
  - "When reviewing the ontology Markdown / ROCS contract v1 proposal."
type: "reference"
---

# Ontology Markdown / ROCS contract v1 — evidence note

## Corpus observation

A bounded local audit of tracked reference documents at the proposal baseline found:

- 32 concepts and 12 relations;
- every concept stores `examples` and `anti_examples` under `ont`;
- every relation stores `examples` and `anti_examples` at top level;
- all 32 concepts carry top-level `system4d.fog` guidance; relations do not;
- five concept edges use unique relation labels (`instance_of`, `is_a`) rather than relation IDs;
- two concept `## Definition` sections differ textually from `ont.description`;
- all 12 relation `## Definition` sections elaborate beyond or differ from `ont.description`.

These are shape observations, not evidence that one representation is semantically superior.

## ROCS observation

Current `rocs validate --repo . --strict-placeholders` and `rocs build --repo .` succeed against the kernel through the workspace launcher.

The validator allows concept `ont.examples` / `ont.anti_examples`, excludes those fields from the relation `ont` allowlist, resolves relation edges through a unique-label index, and does not validate top-level frontmatter keys.

The semantic snapshot parser is stricter: it requires frontmatter to contain exactly `ont`. A direct `capture_corpus` attempt against the kernel fails with:

```text
SnapshotError invalid_ontology ontology front matter is invalid
```

This means general validation success does not currently imply semantic discovery compatibility.

## Consumer-convergence observation

ROCS `converge` dry-runs report:

- class `required`: restore/publish `tools/rocs-cli`, `ontology/manifest.yaml`, `ontology/src/system4d.yaml`, `scripts/ci/full.sh`, and pre-push hook surfaces;
- class `optional`: no changes and therefore no enforced local acceptance gate;
- class `ontology_repo`: target root-level `manifest.yaml` and `src/system4d.yaml`, which conflicts with this repository's nested `ontology/` layout.

Therefore `required` is the only class matching both the repository layout and mandatory ontology validation.

## Current worktree observation

Before this decision, the kernel worktree contained an incomplete migration:

- tracked `tools/rocs-cli/**` deleted;
- `.gitlab-ci.yml` changed to invoke an untracked workspace-resolving `scripts/rocs.sh`;
- unrelated untracked `ontology/src/reference/concepts/core.AgentExperience.md` present.

The first two are in-scope evidence. The unrelated concept remains outside this decision and execution scope.

## Prior bounded evidence

The source-format experiment and POLARIS synthesis establish only that:

- current Markdown/frontmatter remains operational because no replacement won;
- raw byte identity, bounded semantic identity, and authority/currentness are distinct;
- normalized authored-form identity is not needed for the reviewed operation;
- the pinned editor is at most a conditional read-only visualization consumer.

They do not authorize a source-format migration or a universal production semantic IR.
