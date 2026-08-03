---
summary: "Frozen bounded probe for the semantic-proposal and read-only projection capabilities of ontology-diagram-editor v1.6.0."
read_when:
  - "Reproducing the ontology diagram editor capability probe."
  - "Considering a ROCS projection adapter or ontology editor integration."
type: procedure
status: final
---

# Ontology editor guarded-lens probe v0

## Purpose

Test the first unsupported edge in the proposed ontology-diagram-editor relationship:

> Does pinned `modeldriven-hu/ontology-diagram-editor` expose the semantic edit, proposal, reference-validation, and freshness surfaces required by the POLARIS guarded proposal lens?

This probe does not test source-format superiority, production ROCS, full ontology coverage, editor adoption, or Decision 53 authority/currentness.

## Pin

- Repository: `https://github.com/modeldriven-hu/ontology-diagram-editor.git`
- Commit: `039b8d9cbe4be1552c0efd29e3ffd5afa2904a6d`
- Package version: `1.6.0`
- Probe script SHA-256: `54e176ad5e458061a9faba99c1470d05f97cca465468e55795d5f0b1102991a0`
- Probe receipt SHA-256: `56845f861ecf41fe320d449f5b1c8079cb2890d0a3839965d41baeb262b24420`

## Cases

1. **C1 — no-op persistence:** parse and serialize a generated `.odiagram`; verify ontology bytes remain unchanged.
2. **C2 — candidate supported semantic edit:** materialize an existing subclass relationship as a diagram edge; determine whether a semantic delta exists.
3. **C3 — unresolved reference:** persist a diagram node whose ontology reference does not exist in the loaded ontology; determine whether it fails closed.
4. **C4 — stale base:** change the referenced ontology and reload it through the unchanged diagram; determine whether a bound stale-base check exists.

The cases are capability probes, not a complete UI acceptance suite. In particular, C2 discovers whether the selected action is a semantic edit at all.

## Reproduction

Use managed scratch storage and do not mutate ontology-kernel or the upstream repository:

```bash
upstream="$TMPDIR/ontology-diagram-editor-upstream"
runtime="$TMPDIR/ontology-editor-guarded-lens-v0/runtime"

git clone https://github.com/modeldriven-hu/ontology-diagram-editor.git "$upstream"
git -C "$upstream" checkout --detach 039b8d9cbe4be1552c0efd29e3ffd5afa2904a6d
(
  cd "$upstream"
  npm ci
  npm run compile
  npm run compile-tests
)

EDITOR_ROOT="$upstream" \
  node docs/project/ontology-editor-guarded-lens-probe-v0/probe.js "$runtime"
```

The original bounded run also executed:

```bash
./node_modules/.bin/mocha --ui tdd \
  out/test/ontology-model.test.js \
  out/test/ontology-materialization-use-cases.test.js \
  out/test/odiagram.test.js
```

Result: 56 passing upstream data/model tests.

## Disposition rule

- **Semantic proposal lens passes** only if the pinned editor exposes a real semantic-edit operation, emits a semantic proposal, fails closed on unresolved references, and enforces a bound stale base.
- **Read-only visualization remains feasible** if ontology facts can be loaded and visualized without changing source, but it still requires a separately tested external adapter for immutable projection bytes, loss/freshness receipts, reference validation, and confined paths.
- Any missing conjunct fails the semantic-proposal capability without repair or reinterpretation.

## Artifacts

- `probe.js` — executable bounded probe.
- `probe-receipt.json` — observed fixture hashes, case outcomes, and disposition.
- `../ontology-editor-guarded-lens-probe-v0-result.md` — evidence interpretation, independent reproduction, and architecture consequence.
