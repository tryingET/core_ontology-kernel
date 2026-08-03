---
summary: "Historical v2 four-format experiment design, superseded as the default by uncertainty-focused successor experiments."
read_when:
  - "Evaluating whether Markdown should remain the ontology authoring frontend."
  - "Implementing or reviewing the ontology source architecture experiment."
type: design
status: superseded
---

# Ontology source architecture — comparative experiment

## Post-v2 disposition

This is the historical design that produced `ontology-source-experiment-v2-result.md`; it is not an instruction to rerun the tournament. V2 established 40/40 cross-implementation semantic agreement in its accepted scope, 40/40 source/debug disagreement, and zero protocol-valid selecting observations. It selected no format.

The false dependency between semantic correctness and a complete four-format ergonomic tournament is retired. The controlling successor is `ontology-source-architecture-transcendent-synthesis.md`: preserve the bounded semantic invariant, isolate source/debug identity as the next falsifiable contract, and require new justification before any multi-format cohort. Current Markdown/frontmatter behavior is retained without a superiority claim. Decision 53 authority remains external to semantic content.

The sections below preserve the preregistered v2 design and must be read as experiment history.

## Historical decision question

Which representation gives ontology-kernel the smallest correct authoring and semantic-identity architecture while preserving Git review, independent machine agreement, standards interchange, projection safety, and the accepted separation between semantic content and operational authority?

The experiment compares four hypotheses. It does not presume that a separate strict record language or bespoke IR will win.

## Boundaries and non-authorizations

This packet authorizes only a reversible, isolated experiment after independent review of this design. It does not authorize:

- mutation or migration of ontology-kernel source;
- changes to ROCS production behavior or accepted semantic-release contracts;
- publication, approval, adoption, activation, delivery, or rollback claims;
- changes to AK tasks, decisions, evidence, or lifecycle state;
- adoption or source-authority status for `modeldriven-hu/ontology-diagram-editor`;
- treating generated Markdown, RDF, diagrams, or experimental digests as released ontology truth;
- committing experiment outputs without a later explicit gate.

The semantic fact model may describe content. It must not contain or derive owner approval, publication, currentness, consumer intent, acceptance, activation, use, or influence.

## Reproducible baseline

- Repository: `core/ontology-kernel`
- Git commit: `038151bbe8bca46700a800cc05fa39a87ee89ed7`
- Tracked semantic corpus at that commit: 31 concept definitions and 12 relation definitions.
- Non-semantic directory files: one `README.md` in each definitions directory.
- Inspected dirty-worktree delta excluded from the baseline: untracked `ontology/src/reference/concepts/core.AgentExperience.md`.
- Execution location: a disposable read-only checkout or copied fixture tree plus a managed disk-backed temporary output directory. The operator's dirty working tree is not an experiment workspace.

Before execution, write a fixture manifest containing the commit, exact paths, source byte digests, tool versions, and experiment-protocol digest. Any mismatch fails before compilation.

## Fixture corpus

Use six tracked concepts and three tracked relations:

### Concepts

1. `core.Agent` — relation assertion, examples, anti-examples, System4D, and duplicate definition text.
2. `core.Actor` — taxonomy target and comparison point.
3. `core.Secret` — no relation assertion and security-sensitive guidance.
4. `core.Policy` — policy-oriented meaning and relation behavior.
5. `core.Release` — lifecycle/release vocabulary without conferring release authority.
6. `core.DecisionRecord` — governance vocabulary without conferring AK decision authority.

### Relations

1. `core.rel.is_a` — transitive taxonomy characteristic and label/ID distinction.
2. `core.rel.depends_on` — non-transitive dependency relation.
3. `core.rel.conflicts_with` — symmetric-relation test case.

### Preregistered perturbations

Derive experiment-only copies outside the repository for:

- one frontmatter/prose definition disagreement;
- one deprecated term with `since`, `replaced_by`, and decision reference;
- one label-only rename with stable ID;
- one definition change;
- one edge-target change;
- one ambiguous relation-label reference;
- Unicode composed/decomposed label forms;
- integer, boolean, date-looking, and string typed-literal cases;
- reordered mappings, sequences, and facts;
- one unsupported RDF/OWL construct.

The fixture does not claim these synthetic cases are accepted production ontology semantics. They exist to test candidate contracts.

## Competing variants

Encode the identical preregistered fact set in four independently maintained experiment variants.

### V1 — Hardened Markdown/frontmatter

- Preserve one Markdown file per term.
- Define one closed `ont` record as the normative semantic content.
- Classify the body as explicitly non-normative guidance.
- Reject disagreement when a body section claims to restate a normative field but differs.
- Replace relation-label references with stable relation IDs in the experiment copy.
- Treat top-level System4D and guidance fields according to the preregistered field inventory, not current parser accident.

### V2 — Separate strict records

- Use a closed JSON-compatible textual record, with the exact encoding selected only for the experiment.
- Forbid duplicate keys, aliases, merges, implicit dates, ambiguous scalars, unknown fields, and untyped extensions lexically before ordinary deserialization can erase evidence.
- Keep at most one hand-maintained semantic artifact per term.
- Generate any Markdown view; do not hand-maintain a synchronized sidecar.

### V3 — RDF/Turtle plus SHACL

- Use stable IRIs under one preregistered ROCS ID-to-IRI mapping.
- Define the minimal supported RDF/RDFS/SKOS/OWL profile and closed SHACL constraints.
- Reject unsupported constructs rather than silently approximating them.
- Keep narrative guidance in explicitly classified predicates or a non-semantic linked view.
- Test through two independent RDF libraries.

### V4 — Immutable semantic objects plus head manifest

- Store one immutable canonical semantic object per term plus one immutable relation/assertion representation.
- Bind the fixture through a content-addressed manifest/head.
- Keep semantic object identity separate from current authorization.
- Do not recreate Decision 53 authority facts inside the object graph.
- Measure merge and authoring behavior rather than assuming transactional identity makes a good authoring frontend.

## Frozen protocol bundle

Protocols v0 and v1 were independently rejected as execution-indeterminate; their dispositions are recorded in `ontology-source-experiment-v0-review.md` and `ontology-source-experiment-v1-review.md`. The corrected executable candidate is frozen under `ontology-source-experiment-v2/`:

- `field-inventory.v2.json` classifies every observed and synthetic field without conditional selection;
- baseline, fixture, accepted-input, and task manifests bind exact V1–V4 bytes for all 10 golden cases and T1–T6 starts/branches;
- `golden-cases.v2.json` and `malformed-cases.v2.json` bind exact accepted outputs and adversarial inputs;
- `variant-contracts.v2.md` freezes syntax, RDF profile/IRI mapping, SHACL scope, object topology, and maintained/generated surfaces;
- `complexity-measurement.v2.json` and `decision-rule.v2.json` make measurement and winner/no-winner disposition mechanical;
- `actor-materials/` freezes actor/reviewer inputs, exact legal commands, warm-up, blind mapping, and normalization;
- `evidence-manifest-contract.v2.json` and `runbook.v2.md` bind independent implementation, cohort, timing, evidence, worktree preservation, and cleanup.

Protocol v2 makes labels, synonyms, definitions, stable-ID assertions, relation group/characteristics/inverse, and lifecycle semantic. Guidance, System4D, axis/layout, provenance, and authority remain outside the semantic digest. A label rename preserves stable `term_id` but changes the semantic-content digest. Changing any frozen artifact after implementation begins invalidates the run and requires a new protocol revision.

The golden model is experiment truth only. It is not released ontology truth or an accepted production IR.

## Independent implementation rule

Build two canonicalizers with no shared canonicalization implementation and no shared in-memory model library:

- implementation A: Python;
- implementation B: Node/TypeScript or another independently selected runtime.

They may share only the frozen written protocol, exact fixture bytes, and golden oracle. Separate fresh executors build A and B in isolated roots. Each implementation revision and dependency lock is frozen before either implementation or output becomes visible to the comparator or other executor. They must not import one another, reuse generated code, call a shared canonicalization service, or consume the other implementation's output as input truth. After both locks, a third executor scores A and B independently against the oracle before comparing A↔B.

For each variant, both implementations emit:

- canonical fact stream;
- semantic digest;
- source/debug digest;
- loss/conflict report;
- bounded typed errors for rejected fixtures;
- projection metadata declaring `lossless`, `semantically_complete`, or `partial`, plus exact omissions.

## Required tasks

Run the following tasks in counterbalanced order for every variant:

1. add a term with one edge, examples, anti-examples, and guidance;
2. deprecate a term with replacement and decision reference;
3. rename a label without changing stable identity;
4. correct a normative definition;
5. correct a taxonomy edge;
6. resolve a deliberately created merge conflict;
7. generate a compact semantic card;
8. generate RDF and round-trip it through two independent libraries;
9. produce graph JSON and a digest-bound editor import bundle;
10. attempt to insert an authority fact into semantic content and verify rejection.

The diagram-editor probe is syntactic and workflow evidence only. `.odiagram` remains a non-authoritative layout artifact, and visual semantic changes remain proposals requiring normal source-owner review.

## Malformed and adversarial corpus

`ontology-source-experiment-v2/malformed-cases.v2.json` is controlling. It embeds exact UTF-8 payloads and SHA-256 digests for duplicate keys, YAML aliases/merges, ambiguous scalars, unknown fields, wrong primitive types, Unicode collisions, duplicate IDs, label-based relation references, marked prose conflicts, unsupported OWL, forbidden authority fields, false projection completeness, and multi-error precedence.

Applicability and `not_applicable` are frozen per variant; implementations cannot choose them. Parser crashes, untyped failures, hangs, silent coercion, or the wrong precedence fail the case.

## Preregistered metrics and thresholds

Correctness gates are conjunctive: one failure rejects that variant for architecture selection in this protocol revision.

| Measure | Threshold |
|---|---|
| Semantic loss | Zero undeclared omissions or additions. |
| Independent canonicalization | 100% semantic-digest agreement across the two implementations. |
| Adversarial rejection | 100% correct rejection of applicable malformed and authority-leakage cases. |
| Identity behavior | Label-only rename preserves `term_id` but changes the semantic digest; definition, edge, lifecycle, and add-term cases match all frozen relationships. |
| Ordering behavior | Reordering non-semantic mappings/facts preserves semantic identity in 100% of fixtures. |
| RDF round-trip | 100% preservation of the supported fact set through two independent RDF libraries. |
| Projection honesty | 100% correct completeness/loss classification and omission listing. |
| Authority separation | 100% rejection of attempts to derive or encode owner approval/currentness as semantic-content output. |
| Maintained semantic surfaces | No more than one hand-maintained semantic artifact per term. |
| Reversibility | Zero mutation of the bound source checkout; identical source-tree digest and Git status before and after. |
| Authoring cohort | All 192 paired observations from eight exact-model stateless actors complete under the frozen counterbalance. |
| Merge resolution | No semantic fact loss, unintended change, protected-surface edit, or timeout. |

The former 10% timing threshold and subjective phrases such as “superior enough” are removed. `complexity-measurement.v2.json` and `decision-rule.v2.json` define a fixed six-dimensional complexity vector and Pareto comparison. Eight actors each run six tasks across four variants; missing observations or model substitution produce `no_winner_insufficient_evidence`.

## Selection and falsification rules

Correctness is conjunctive. Exclude every variant with one failed applicable gate. For the remainder, apply the frozen Pareto rule and disposition table mechanically:

- one uniquely undominated variant with sufficient evidence may advance;
- unresolved comparisons containing V1 retain current behavior without declaring Markdown permanently superior;
- multiple undominated non-V1 variants are `no_winner_incomparable`;
- missing selecting evidence is `no_winner_insufficient_evidence`;
- no correctness-passing variant is `no_winner_retain_current`.

Do not average failures or select the least-bad architecture. Only `winner:V1|V2|V3|V4` may support architecture RFC consideration. Every `no_winner_*` disposition retains current production behavior and routes to a revised experiment or bounded hardening proposal.

## Execution phases

1. **Protocol review:** independently review this packet, the audit, corrected adjudication, and complete `ontology-source-experiment-v2/` bundle.
2. **Freeze verification:** compute the aggregate protocol digest; verify frozen field, baseline, fixture, oracle, error, variant, decision, and runbook artifacts before code.
3. **Isolate:** create one immutable clean baseline, four writable fixture copies, two mutually hidden implementation roots, and one retained evidence root.
4. **Implement:** build and lock A and B independently without changing production ROCS or ontology source; expose neither implementation until both locks exist.
5. **Correctness:** score A and B separately against valid and malformed oracles, then compare them; run identity, ordering, authority, projection, and RDF round-trip suites.
6. **Ergonomics:** run the complete 192-observation counterbalanced cohort and blinded review exactly as frozen.
7. **Projection probe:** generate loss-declared cards, RDF, graph JSON, and a non-authoritative editor bundle.
8. **Evidence retention:** copy and hash every required receipt, output, failure, timing, patch, review, and complexity measurement into the retained evidence root.
9. **Reversibility and cleanup:** verify immutable baseline and operator-worktree preservation, then delete only disposable owned copies after the evidence-root manifest passes.
10. **Results:** apply the mechanical disposition table and preserve failures and `insufficient_evidence` without suppression.
11. **Architecture iteration:** only after the complete results packet exists, run the governed transcendent iteration over that evidence.
12. **Decision membrane:** open an architecture RFC/decision only for a demonstrated winner; otherwise retain current behavior.

## Required evidence packet

The experiment results must include:

- protocol and fixture-manifest digests;
- exact implementation revisions and dependency locks;
- canonical fact streams and both digest outputs;
- malformed-case matrix;
- projection loss reports;
- RDF dual-library round-trip receipts;
- authoring/review prompts, ordering, durations, errors, and reviewer judgments;
- implementation-complexity inventory;
- before/after source-tree digest and Git status;
- explicit winner, no-winner, or insufficient-evidence disposition;
- all failed thresholds without suppression.

## Stop conditions

Stop without architecture selection if:

- the field inventory changes after implementations begin;
- either canonicalizer has consumed the other's output or implementation;
- a correctness failure is waived;
- the dirty operator workspace would be mutated;
- an authority fact is collapsed into semantic content;
- experiment output is presented as released or adopted ontology truth;
- the editor requires source-authority privileges for the bounded probe;
- the evidence sample is too small to support a claimed ergonomic winner.

## Next legal move

Do not rerun this protocol by default. The next move is bounded protocol authoring for the source-identity question in `ontology-source-architecture-transcendent-synthesis.md`: establish a concrete purpose and author exact fixtures, oracle, preimage grammar, algorithm, and errors only if an extra normalized identity is needed. Independent design review follows a complete packet. Its pass condition can establish only a candidate source/debug identity contract. RFC/ADR work remains blocked until separate valid evidence demonstrates a source-format winner.
