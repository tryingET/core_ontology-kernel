---
summary: "Pinned ontology-diagram-editor probe: semantic proposal capability fails; only externally guarded read-only visualization remains conditionally feasible."
read_when:
  - "Deciding the role of modeldriven-hu/ontology-diagram-editor in ontology-kernel architecture."
  - "Considering an editor semantic proposal path or read-only visualization adapter."
type: evidence
status: final
---

# Ontology editor guarded-lens probe v0 — result

## Disposition

- Upstream: `modeldriven-hu/ontology-diagram-editor` v1.6.0
- Commit: `039b8d9cbe4be1552c0efd29e3ffd5afa2904a6d`
- Semantic proposal lens: **`fail`**
- Conditional role: **semantically read-only visualization consumer behind an external guarded adapter**
- Current integration/adoption: **not authorized**
- Source-format consequence: **none**
- Decision 53 consequence: **none**

“Read-only” refers to ontology semantics. The editor mutates `.odiagram` layout, materialization, styling, notes, and export state.

## Verification

The upstream pin passed:

- `npm ci` with zero reported audit vulnerabilities;
- `npm run compile`;
- `npm run compile-tests`; and
- 56 targeted upstream ontology-model, materialization, and `.odiagram` tests under Mocha's TDD interface.

The bounded probe receipt is `ontology-editor-guarded-lens-probe-v0/probe-receipt.json` with SHA-256:

```text
56845f861ecf41fe320d449f5b1c8079cb2890d0a3839965d41baeb262b24420
```

Independent tester dispatch `dispatch-1785768927089` rebuilt the pinned source into a fresh output root and reproduced byte-identical probe output and receipt. Independent architecture review dispatch `dispatch-1785768927098` selected only the conditional read-only visualization role.

## Observations

| Case | Observed result | Correct interpretation |
|---|---|---|
| C1 — no-op | Generated `.odiagram` parse/stringify was byte-stable; ontology bytes were unchanged. | Narrow data-layer support for separate presentation persistence, not full VS Code UI proof. |
| C2 — materialized edge | Adding the existing `rdfs:subClassOf` relationship changed `.odiagram` state while ontology bytes and loaded facts remained unchanged. | The action visualizes an existing fact; it is not a semantic edit and emits no semantic proposal. |
| C3 — unresolved reference | `.odiagram` accepted and round-tripped `ex:Missing` when the prefix was declared, although the entity was absent from the loaded ontology. | Native persistence validates reference syntax/prefixes, not existence against the semantic projection. |
| C4 — changed dependency | The referenced ontology reloaded from two to three classes while `.odiagram` remained unchanged. | Dependency refresh exists, but no semantic-contract/profile/base-digest binding or stale-base rejection exists. |

The receipt's source hashes are raw-byte digests, not semantic digests under a versioned semantic contract. It contains no included/omitted/unsupported/editable loss declaration and is not an editor-issued receipt.

## Pinned source findings

At the reviewed commit:

- `src/ui/model-tree/ontology-loader.ts` reads referenced RDF files and projects quads into model-tree items.
- `src/diagram-editor/use-cases/create-edge-use-case.ts` creates nodes and edges inside `OntologyDiagramDocument` from already-loaded ontology items.
- `src/diagram-editor/document-repository.ts` persists the `.odiagram` document, not ontology source.
- The contributed and internal command surfaces contain presentation/materialization operations but no ontology-fact create/update/delete or semantic-delta export.
- `.odiagram` passthrough fields can carry arbitrary JSON-compatible metadata, but upstream does not generate or enforce semantic-contract, projection-profile, loss, or freshness fields.
- `OntologyFileReference` accepts non-empty paths, and the loader resolves them relative to the diagram. It does not itself confine `../` or absolute paths to an adapter-owned projection directory.

These findings are bounded to the pinned source and exercised fixture. They do not claim that every future editor version lacks these capabilities.

## Why the semantic proposal lens fails

The proposed guarded lens required:

```text
get_K,P(F)                  -> bound projection receipt + view
propose_K,P(F, receipt, V') -> semantic delta or typed error
apply_K(F, delta)           -> verified fact set
```

The pinned editor supplies the first operation only as an unbound RDF read plus visual projection. It supplies no semantic `propose` operation, no native bound receipt, and no reverse semantic path. Unresolved semantic references and changed dependencies do not fail closed under those missing contracts.

This is capability absence, not a defective semantic-delta algorithm. Repeating semantic-edit cases against the same pin is unjustified.

## Supported candidate role

A future external adapter may test a strictly read-only visualization operation. It must:

1. generate immutable RDF/OWL projection bytes under a pinned profile;
2. issue an external receipt binding semantic contract, base semantic digest, raw projection hash, profile, exact loss declaration, adapter version, and editor commit;
3. declare semantic editability as `none`;
4. confine ontology references to an adapter-owned projection directory;
5. validate every `.odiagram` ontology reference against the pinned projection;
6. reject changed projection bytes or a stale semantic base;
7. classify all `.odiagram` changes as presentation state only; and
8. obtain separate owner authorization before adoption.

Passing such a protocol would support only read-only visualization for the pinned profile. It would not create semantic proposals, select a source format, mutate ontology-kernel, or mint approval/currentness.

## Stop decision

No further editor experiment is justified now. No owner-approved value case for read-only visualization has been established, and the proposed semantic-proposal capability does not exist at the pin.

The next action is therefore to correct the architecture synthesis, preserve this evidence, and stop. A new protocol begins only if an owner later names a concrete read-only visual exploration operation.

## Limits

- No full VS Code canvas/open-save UI session was run.
- No broad RDF/OWL loss profile was measured.
- C3 tested an unresolved reference, not every unsupported or omitted RDF/OWL construct.
- The original receipt did not bind compiled `out/**` artifact hashes, although independent recompilation reproduced the result.
- No dependency-path confinement or untrusted-`.odiagram` security test was implemented.
