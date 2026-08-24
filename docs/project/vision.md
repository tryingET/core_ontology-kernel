---
summary: "Durable product direction for ontology-kernel as AI Society's minimal, stable shared semantic kernel."
read_when:
  - "When deciding whether a concept, relation, System4D baseline, or source-contract change belongs in ontology-kernel."
  - "When evaluating long-term direction beyond a release, implementation wave, or consumer migration."
type: "reference"
---

# Vision

## Purpose

Every AI Society company and repository can refer to a small set of stable, versioned concepts,
relations, and baseline constraints without importing an enterprise knowledge graph or confusing
semantic content with operational authority.

`ontology-kernel` is the slow-moving shared semantic floor. It provides the minimal cross-company
meta-language needed to describe actors, authority, evidence, policy, risk, work, releases, and
other concerns that genuinely cross domain boundaries. Company and repository overlays own their
specialized meaning.

## Intended experience

1. A maintainer starts from a named consumer need and decides whether the meaning is truly shared
   or belongs in a company or repository overlay.
2. The maintainer authors reviewed semantic intent through the currently accepted source contract,
   preserving stable IDs and using explicit deprecation rather than silent redefinition.
3. ROCS admits, validates, builds, explains, and packs the exact corpus deterministically from
   local inputs. Its claims remain operation-qualified source-contract, schema, and reference
   conformance—not generic semantic correctness.
4. Reviewers can distinguish semantic changes from prose guidance, presentation, tooling,
   projections, release mechanics, and owner-issued lifecycle facts.
5. A release owner can classify the semantic delta, select an exact OID, and publish one protected,
   version-addressed release without treating a branch, transport alias, or passing gate as release
   authority.
6. A consumer pins a protected release, resolves it from an explicit workspace or published
   artifact, runs its own acceptance gate, and records adoption through its own owner surface.
7. Agents and humans retrieve bounded summaries and packs instead of loading the whole ontology.
   Projections declare their losses and never acquire more authority than the semantic source.
8. When evidence is insufficient, the system preserves uncertainty and stops before inventing a
   format winner, semantic fact, approval, adoption, activation, use, or currentness claim.

## Product principles

- **Minimal shared floor.** Add only meaning that must be shared across domains; specialized
  semantics stay in overlays.
- **Stable identity before convenience.** IDs survive code and file refactors. Breaking meaning
  changes use deprecation, replacement, and an explicit decision trail.
- **Slow, reviewable evolution.** Kernel changes are demand-led, independently reviewed, and
  versioned according to their semantic surface.
- **Deterministic local proof.** Validation, build, retrieval, and handoff work from explicit local
  inputs without hidden remote fallback.
- **Relation-specific canonicality.** Authored bytes, bounded semantic identity, projections,
  proposals, provenance, and owner authority remain distinct relations rather than being collapsed
  into one supposedly universal artifact.
- **Authority stays orthogonal.** Semantic content and compiler output cannot mint task, decision,
  release, adoption, activation, use, or currentness facts owned elsewhere.
- **Bounded context by default.** Summaries and packs should answer a named operation with minimal
  noise; unlimited graph expansion is an anti-goal.
- **Truthful nonclaims.** A passing parser, gate, experiment, or release proves only its declared
  operation and evidence boundary.

## Hard scope boundaries

`ontology-kernel` does not:

- become an enterprise knowledge graph for every company or product;
- absorb domain-specific vocabulary that belongs in company or repository overlays;
- become a task, decision, planning, policy-enforcement, or evidence-ledger authority;
- own the ROCS product or package lifecycle, even when it pins or vendors an exact ROCS
  materialization for reproducible validation;
- declare Markdown, RDF, an editor, or another representation the permanent universal source
  format without a separately justified consumer operation and accepted decision;
- infer release, adoption, activation, use, or currentness from Git state, semantic validity, or
  generated artifacts; or
- authorize indiscriminate source loading or unbounded neighbor expansion into agent context.

## Success condition

The kernel succeeds when cross-company systems can use the same small vocabulary with stable
meaning; maintainers can change it through explicit, reproducible, reviewable contracts; consumers
can pin and validate exact releases without hidden workspace memory; and every semantic,
projection, release, adoption, and authority claim remains attached to its proper owner and proof.

Success is a continuing stewardship posture, not terminal feature completion. This vision states
durable direction; it does not by itself prove release readiness, fleet adoption, activation, use,
currentness, or completion of an AK strategic frame.
