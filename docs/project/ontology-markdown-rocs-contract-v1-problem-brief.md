---
summary: "Problem brief for aligning ontology-kernel's current Markdown contract with its ROCS consumer boundary."
read_when:
  - "When deciding how ontology-kernel and rocs-cli should divide schema and enforcement ownership."
type: "reference"
---

# Ontology Markdown / ROCS contract v1 — problem brief

## Trigger

`ontology-kernel` and `core/rocs-cli` have a real integration boundary but no single accepted contract for the Markdown/frontmatter shape currently in production.

The result is three kinds of drift:

1. `docs/ontology-schema.md` under-documents fields used by the tracked corpus.
2. ROCS validation, semantic snapshot parsing, and pack/discovery projections accept different shapes.
3. The kernel's partially edited consumer wiring deletes the vendored ROCS bundle and makes CI resolve a sibling workspace checkout, while ROCS required-class convergence specifies a standalone vendored gate.

## Why this is architecture-significant

The concern changes a shared schema/interface across two repositories and affects reproducible validation. It is therefore Tier 1 even though it does not select a new ontology source format.

## Owner boundary

- `ontology-kernel` owns authored ontology meaning and its accepted source contract.
- `rocs-cli` owns deterministic, offline enforcement and consumer convergence mechanics.
- Decision 53 owners retain approval, release, adoption, activation, use, and currentness authority.
- Git state, validation, document digests, and projections cannot mint those authority facts.

## Required outcome

Accept or reject one bounded contract that:

- retains current Markdown/frontmatter operationally without claiming format superiority;
- makes normative fields, guidance fields, reference semantics, and parser errors explicit;
- makes current ontology-kernel documents consumable by the agreed ROCS operations;
- preserves reproducible standalone CI through a pinned ROCS bundle;
- avoids normalized authored identity, a semantic evaluator, and editor integration.

## Non-goals

- selecting Markdown, RDF, objects, or another universal source format;
- productionizing the frozen v2 experimental semantic mapping wholesale;
- changing Decision 53 or implementing Decisions 106/107;
- adopting the probed diagram editor;
- treating build success as publication, adoption, or currentness.
