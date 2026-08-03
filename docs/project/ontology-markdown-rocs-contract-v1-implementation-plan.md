---
summary: "Post-ADR implementation plan for Decision 110 across rocs-cli and ontology-kernel."
read_when:
  - "When executing Decision 110 owner-local tasks."
type: "procedure"
---

# Ontology Markdown / ROCS contract v1 — implementation plan

## Governing decision

- AK Decision 110
- [ADR](../adr/2026-08-03-ontology-markdown-rocs-contract-v1.md)
- [Cross-repo fanout](ontology-markdown-rocs-contract-v1-cross-repo-fanout.md)

## Wave A — ROCS implementation

Owner: `core/rocs-cli`.

1. Add one shared v1 frontmatter/document parser with the accepted byte, YAML, path, field, and error rules.
2. Add per-layer `source_contract` resolution and route every interpreting source-reading operation through the dispatcher.
3. Keep `context.create` raw-capture-only and add tests proving it emits no conformance claim.
4. Align validator, summary/build, semantic snapshot, discover/route, both pack modes, and transaction fixtures.
5. Add operation-qualified conformance output rules: complete success only; no corpus claim on partial/resource-exhausted failure.
6. Add schema-3 exact materialization receipts with Git SHA-1 `source_commit`, lock digest, complete file hashes, and JCS receipt digest.
7. Preserve legacy behavior for layers without the selector.
8. Run the complete ROCS test and CI gates.

## Wave B — ROCS package release

Owner: `core/rocs-cli`, separate task after Wave A evidence.

1. Apply version `0.3.0` through the repo release command.
2. Update and verify `uv.lock`.
3. Commit and tag the exact package-owner release under the existing release contract.
4. Produce and verify the exact materialization consumed by the kernel.

This task proves a package release and one exact bundle. It does not prove semantic publication, consumer adoption, or canonical cross-builder bytes.

## Wave C — ontology-kernel adoption

Owner: `core/ontology-kernel`; depends on Wave B.

1. Move relation `examples` and `anti_examples` under `ont` without changing list contents or prose.
2. Update `docs/ontology-schema.md` to the accepted v1 grammar and verdict ceiling.
3. Add `rocs.source_contract: ontology-markdown-v1`, profile `kernel-v1`, and the checked-in discovery request fixture.
4. Converge as class `required` and vendor the exact ROCS 0.3.0 materialization.
5. Rewire `.gitlab-ci.yml` to Python 3.12 and `scripts/ci/full.sh`; remove the workspace launcher from acceptance.
6. Run clean no-sibling acceptance and commit only the scoped migration/adoption paths.

## Out of scope

- the untracked `core.AgentExperience.md` concept;
- source-format selection, relation-ID migration, semantic evaluator, Decision 53 adapter, or editor integration;
- package publication/adoption/currentness claims beyond the package-owner evidence actually produced.
