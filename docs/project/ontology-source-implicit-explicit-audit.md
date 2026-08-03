---
summary: "Implicit-explicit DSL audit and formalization threshold for ontology authoring, semantic identity, projections, and authority boundaries."
read_when:
  - "Revising the ontology source architecture adjudication."
  - "Designing the comparative source-format experiment or semantic IR contract."
type: analysis
status: proposed
---

# Ontology source architecture — implicit/explicit audit

## Scope and evidence

This audit applies the Prompt Vault `implicit-explicit` procedure and its companion `formalization-threshold` procedure to the current ontology source architecture.

Observed evidence is bounded to:

- ontology-kernel at Git commit `038151bbe8bca46700a800cc05fa39a87ee89ed7`;
- the inspected dirty working tree, which adds untracked `core.AgentExperience.md`;
- `docs/ontology-schema.md`;
- current ROCS summary/build behavior;
- the Greats adjudication and its independent synthesis review;
- accepted Decision 53 authority boundaries as cited by that review.

This is an analysis artifact. It does not authorize schema implementation, ontology migration, ontology mutation, publication, activation, or editor adoption.

## IMPLICIT DSLs FOUND

- **Ontology record shape:** concept/relation authoring -> ontology maintainers, ROCS, reviewers, and consumers -> undocumented fields can be accepted, dropped, or interpreted differently.
- **Normative meaning split:** front matter versus Markdown body -> authors, reviewers, and LLM consumers -> two formulations can disagree without a machine-detectable winner.
- **Relation reference language:** relation labels in concept edges versus stable relation IDs in relation definitions -> authors and graph consumers -> renames or label collisions can silently change or break denotation.
- **System4D attachment:** top-level `system4d` blocks outside the documented `ont` schema -> ontology authors and ROCS -> a field can be operationally accepted without a declared role in semantic identity.
- **Relation guidance attachment:** top-level `examples` and `anti_examples` plus prose sections -> ontology authors and projection consumers -> guidance can be duplicated, omitted, or classified inconsistently.
- **Canonicalization language:** ordering, normalization, typed literals, Unicode, defaults, and digest participation -> compiler implementers and release consumers -> two conforming-looking implementations can assign different identity.
- **Projection-loss language:** Markdown, cards, RDF/OWL, graphs, indexes, and diagrams -> humans, LLMs, and tools -> a partial view can be mistaken for complete or authoritative meaning.
- **RDF interoperability profile:** ROCS IDs to IRIs and the supported RDF/OWL/SHACL subset -> external tools and the ontology diagram editor -> syntactic import can be mistaken for semantic round-trip compatibility.
- **Corpus baseline language:** “current ontology” versus Git tree versus dirty working tree -> experimenters and reviewers -> results can be irreproducible while appearing precise.
- **Authority join language:** authored, released, desired, adopted, and used facts -> semantic owner, ROCS, AK, consumer owner, Pi, and recovery controller -> semantic content can appear to confer approval or currentness.
- **Visual-edit proposal language:** `.odiagram` layout and diagram edits -> visual users and ontology maintainers -> a presentation change can be mistaken for an ontology mutation or accepted proposal.

## CLASSIFICATION

| DSL | Current State | Should Be | Why |
|---|---|---|---|
| Ontology record shape | convention / partially formal | formal | Repeated machine consumption and silent field drift justify one closed validated contract. |
| Normative meaning split | implicit | formal | Competing definitions are costly, silent, and difficult to detect reliably in review. |
| Relation reference language | convention | formal | Stable relation identity must not depend on mutable labels. |
| System4D attachment | implicit | convention before formalization | Its participation in semantic identity is unresolved; freezing it now would encode an unreviewed commitment. |
| Relation examples and anti-examples | convention | explicit convention, then formal if normative | Their safety value is clear, but whether they are semantic identity or guidance must be decided first. |
| Canonicalization and digest rules | implicit | formal | Independent compilation is impossible without an executable canonicalization contract. |
| Projection-loss declarations | implicit | formal | Undeclared omission creates operator and LLM misuse without obvious parser failures. |
| RDF/OWL/SHACL profile | implicit | explicit convention during experiment | The supported profile is still volatile; the experiment must test it before it becomes a permanent contract. |
| Corpus/fixture identity | implicit | formal | Reproducibility requires an exact tree and fixture manifest, not “current corpus.” |
| Authority joins | formal elsewhere, inaccurately summarized here | formal by reference | Reuse accepted Decision 53 facts; do not create a competing semantic-authority DSL. |
| Visual edit/proposal boundary | convention | explicit convention | The editor is initially a non-authoritative projection/proposal surface, not a source owner. |
| Candidate strict source syntax | proposal | convention during experiment | YAML subset, JSON, RDF, and object forms are still competing hypotheses. |

## FORMALIZATION CANDIDATES

Ranked by damage on violation:

1. Authority/content separation and owner-issued currentness inputs.
2. Complete normative-field and semantic-identity inventory.
3. Canonical semantic fact model, normalization, and semantic-digest algorithm; normalized source identity remains conditional on a demonstrated consumer.
4. Stable relation-ID references.
5. Corpus fixture manifest and malformed-input corpus.
6. Projection completeness/loss declarations.
7. Normative definition versus non-normative guidance boundary.
8. RDF ID-to-IRI mapping and supported profile.
9. Visual proposal/import boundary.
10. Candidate source serialization syntax.

## CANDIDATES

Scores use `0` (low), `1` (medium), and `2` (high). High volatility increases the raw score but invokes the template override: keep the candidate as an explicit convention until it stabilizes.

| DSL | Domain | Repetition | Damage | Detection | Onboarding | Tooling | Volatility | Total |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Authority/content boundary | cross-owner lifecycle | 2 | 2 | 2 | 2 | 2 | 0 | 10 |
| Normative-field inventory | semantic identity | 2 | 2 | 2 | 2 | 2 | 1 | 11 |
| Canonical semantic fact/digest contract | compilation and release | 2 | 2 | 2 | 2 | 2 | 1 | 11 |
| Stable relation references | ontology graph | 2 | 2 | 1 | 1 | 2 | 0 | 8 |
| Fixture/corpus manifest | experimentation | 1 | 2 | 2 | 1 | 2 | 0 | 8 |
| Projection-loss contract | generated views | 2 | 2 | 2 | 2 | 2 | 1 | 11 |
| Definition/guidance boundary | authoring and review | 2 | 2 | 2 | 2 | 2 | 2 | 12 |
| System4D semantic participation | ontology extension | 2 | 2 | 2 | 2 | 2 | 2 | 12 |
| RDF/OWL profile and IRI mapping | interchange | 1 | 2 | 2 | 2 | 2 | 2 | 11 |
| Visual proposal boundary | diagram tooling | 1 | 1 | 2 | 1 | 1 | 1 | 7 |
| Strict source serialization | authoring frontend | 2 | 1 | 1 | 2 | 2 | 2 | 10 |

## DECISION

- **Keep implicit:** visual layout aesthetics that do not alter semantic proposals; prose style inside explicitly non-normative guidance.
- **Keep as convention:** System4D semantic participation, RDF/OWL profile, visual proposal workflow, and candidate strict source serialization until comparative evidence resolves them.
- **Formalize now:** authority/content separation by reference to Decision 53; exact fixture identity; normative-field inventory; canonical semantic fact/digest contract; stable relation references; malformed-input behavior; projection-loss declarations; and the definition/guidance conflict policy. A normalized source/debug identity is excluded unless a concrete consumer first demonstrates the need.

The high raw scores for System4D, RDF mapping, and source syntax do not override their instability. Their violations are dangerous, but prematurely freezing the wrong semantics would be more expensive than using explicit experiment conventions.

## FIRST FORMALIZATION STEP

- **Authority/content boundary:** correct the adjudication so semantic IR is only a semantic-content input and owner-issued lifecycle/currentness facts remain independent inputs.
- **Normative-field inventory:** preregister every candidate field and classify it as semantic identity, source provenance, non-normative guidance, layout, or authority-external.
- **Canonical semantic fact/digest contract:** publish a small golden fact set and require two independent canonicalizers to agree. This does not formalize a normalized source/debug digest; that separate relation requires a concrete consumer first.
- **Stable relation references:** use relation IDs in the golden fact model and explicitly test label-only renames.
- **Fixture/corpus manifest:** bind the experiment to one commit, exact source paths, and explicit synthetic perturbations.
- **Projection-loss contract:** require every generated view to declare complete, lossless, or partial status and list omissions.
- **Definition/guidance boundary:** include a deliberate prose/frontmatter conflict and require deterministic failure rather than silent precedence.
- **System4D participation:** record both include-in-identity and guidance-only hypotheses; do not choose before the experiment inventory review.
- **RDF profile:** define only the minimal profile needed for round-trip tests and fail closed on unsupported constructs.
- **Visual proposal boundary:** treat `.odiagram` and visual edits as digest-bound, non-authoritative proposals.
- **Strict source serialization:** encode it as one experiment variant, not as the presumed migration target.

## WHY NOW

The architecture debate is not primarily Markdown versus RDF versus YAML. The hidden language is the mapping from authored bytes to normative facts, semantic identity, projections, and owner-issued authority. V2 subsequently showed independent agreement on the tested semantic mapping (40/40) but disagreement on every source/debug digest (40/40), while producing no valid selecting cohort. The highest-leverage move is therefore no longer another closed four-format comparison. It is to retire one cross-format contract uncertainty at a time. For source/debug identity, the first uncertainty is whether any consumer needs a normalized identity beyond semantic identity and raw byte hashing; only then may a reviewable micro-experiment be authored, as specified in `ontology-source-architecture-transcendent-synthesis.md`. This keeps Decision 53 authority inputs separate and does not select a serialization.
