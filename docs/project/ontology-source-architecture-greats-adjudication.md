---
summary: "Many-of-the-Greats adjudication of the canonical ontology source, semantic IR, release identity, and projection architecture."
read_when:
  - "Reconsidering Markdown/frontmatter as the ontology-kernel source format."
  - "Designing ROCS semantic IR, RDF/OWL interchange, or visual ontology tooling."
type: proposal
status: proposed
---

# Ontology source architecture — Greats adjudication

## Question

What representation should carry authored ontology intent, canonical semantic identity, released meaning, current authority, machine interchange, human explanation, and visual exploration—and which of those responsibilities were incorrectly collapsed into Markdown with YAML front matter?

This is a proposal-stage analysis. It does not authorize a source-format migration, ontology mutation, ROCS implementation, editor adoption, activation, or release.

## Evidence boundary

Observed current state:

- `ontology-kernel` declares Markdown files with YAML front matter as its source schema in `docs/ontology-schema.md`.
- The earliest explicit schema commit, `3c493fe`, states that choice but does not record why Markdown was selected over RDF, a typed record language, or another substrate.
- At Git commit `038151bbe8bca46700a800cc05fa39a87ee89ed7`, the tracked corpus contains 31 concept definitions and 12 relation definitions; directory `README.md` files are not definitions. The inspected dirty working tree resolves through ROCS to 32 concepts because it also contains untracked `core.AgentExperience.md`.
- All 32 dirty-worktree concepts carry top-level `system4d`; all 12 relation definitions carry top-level `examples` and `anti_examples`, although `docs/ontology-schema.md` documents neither placement completely.
- Concept edges currently name relation labels such as `is_a`, rather than stable relation IDs such as `core.rel.is_a`.
- Normative-looking definitions occur in both front matter and Markdown prose; 30 inspected formulations were exact duplicates and 14 differed, so a consumer cannot infer one universal precedence rule safely.
- Current ROCS paths parse or project different subsets of the source. This establishes parser and projection drift; it does not yet establish that a separate source language is necessary.
- `modeldriven-hu/ontology-diagram-editor` consumes RDF/OWL-family files and persists non-authoritative `.odiagram` layout documents; it does not consume ROCS Markdown or edit ontology source.

The historical record supports “Markdown was the initial practical scaffold.” It does not establish “Markdown is the optimal permanent semantic substrate.”

## Mode 1 — Many of the Greats

### School 1: Standards-native knowledge representation

- **Core claim:** canonical ontology meaning belongs in RDF/RDFS/SKOS/OWL, constrained by SHACL where closed-world repository rules are required.
- **Premises:** semantic interoperability requires externally defined denotations; IRIs, classes, properties, inverses, labels, and taxonomy should not depend on one Python parser.
- **Strongest case:** standards permit independent processors, SPARQL, reasoning, and potential visual-tool interoperability. ROCS currently records and custom-validates selected relation characteristics and inverses, but the inspected runtime does not establish general transitive or symmetric reasoning.
- **What it sees that others miss:** a bespoke typed record can be perfectly deterministic while remaining semantically isolated.

### School 2: Git-native literate semantics

- **Core claim:** meaning is authored and reviewed most safely as small, coherent, human-readable text documents; databases and formal graphs should be reproducible projections.
- **Premises:** ontology quality is primarily an authoring, explanation, review, and governance problem; examples, anti-examples, confusion notes, and rationale are semantic safety mechanisms.
- **Strongest case:** one-file-per-term Markdown gives excellent diffs, blame, branching, offline operation, bounded LLM packs, and cohesive review. The kernel is intentionally small and does not yet demonstrate an entailment-heavy workload that justifies OWL-first authoring.
- **What it sees that others miss:** formal triples can preserve axioms while destroying the narrative unit humans and language models need to apply terms correctly.

### School 3: Compiler and typed-IR architecture

- **Core claim:** neither Markdown nor RDF should be privileged as universal truth; both should compile into one closed, canonical semantic IR from which every projection is derived.
- **Premises:** parsing, semantic normalization, identity, validation, and presentation are different phases; one typed boundary prevents graph, pack, validation, discovery, and diagram code from independently interpreting source dictionaries.
- **Strongest case:** a closed IR can use stable IDs, relation IDs, localized text, typed literals, explicit provenance, canonical ordering, semantic digests, and declared projection-loss profiles. Equivalent Markdown and RDF inputs can compile to the same semantic identity.
- **What it sees that others miss:** source serialization is an authoring interface; canonical semantic equivalence is a compiler concern.

### School 4: Content-addressed transactional graph

- **Core claim:** canonical truth is not a file format but immutable semantic objects plus owner-authorized transitions, receipts, and current heads.
- **Premises:** paths are locators, digests prove bytes rather than permission, and authentic historical objects may still be revoked or stale.
- **Strongest case:** content-addressed objects, CAS heads, typed transactions, and narrow receipts distinguish authored, built, approved, published, accepted, activated, delivered, and rolled-back facts without rewriting history or collapsing owners.
- **What it sees that others miss:** Git or a typed IR can identify meaning but cannot by itself establish lawful currentness, adoption, or action-time authority.

### School 5: Human and superintelligent-LLM interaction safety

- **Core claim:** one semantic fact must appear once authoritatively, while every audience receives a purpose-built, provenance-visible projection.
- **Premises:** duplicated definitions create model ambiguity; raw verbose documents waste context; visual diagrams invite false authority; generated artifacts become dangerous when freshness and omission are invisible.
- **Strongest case:** humans need validated forms and semantic diffs, harnessed LLMs need compact cards with explicit omissions and digests, programs need closed canonical JSON, and visual users need source-bound diagrams. Every surface must say whether it is authoritative, stale, partial, or non-authorizing.
- **What it sees that others miss:** technically correct representations still fail when operators or models cannot tell source from view, fact from prose, or validation from approval.

## Mode 2 — Confrontation

### Standards-native vs Git-native

- **Fundamental contradiction:** whether externally standardized formal semantics or locally cohesive authoring units should dominate the source representation.
- **Standards explains better:** interoperability, formal property semantics, query ecosystems, and independent implementations.
- **Git-native explains better:** review, rationale, anti-examples, bounded retrieval, and low-friction correction.
- **Residual tension:** OWL open-world semantics do not implement ROCS closed-world policy, while Markdown conventions do not give external tools shared denotations.

### Typed IR vs format canonicality

- **Fundamental contradiction:** whether canonical meaning should inherit the accidental syntax of its authoring format.
- **IR explains better:** semantic equivalence across serialization, stable relation identity, deterministic projections, and one validator/compiler boundary.
- **Format-first schools explain better:** direct inspectability and avoiding an invisible generated layer that silently becomes authority.
- **Residual tension:** the IR must be inspectable, independently implemented, and reproducibly generated or it becomes an opaque compiler oracle.

### Transactional graph vs source files

- **Fundamental contradiction:** whether authored meaning and lawful current state are one kind of canonical truth.
- **Transactional graph explains better:** publication, currentness, revocation, concurrency, replay, adoption, and rollback.
- **Source files explain better:** authoring, branching, merge, local review, and reconstruction.
- **Residual tension:** moving authoring into a graph store would absorb Git’s strengths; pretending Git establishes current authority would erase owner-state distinctions.

### Human/LLM safety vs duplicated convenience

- **Fundamental contradiction:** whether redundant prose and metadata help readers or create competing truth.
- **Safety school explains better:** one normative semantic field plus generated audience views prevents ambiguity and staleness.
- **Literate school explains better:** explanation cannot be reduced to machine fields without losing judgment.
- **Residual tension:** narrative remains necessary, but it must be explicitly non-normative or typed as a distinct governed field rather than silently restating definitions.

## Mode 3 — Integration or decision

- **Original hypothesis:** contextual dominance plus a falsifiable four-format comparison. Separation by responsibility was retained; the winning authoring and identity substrate was not selected.
- **Post-v2 adjudication:** the comparison established independent semantic agreement for all 40 accepted packets but no format winner: source/debug identity disagreed 40/40 and the selecting cohort had zero protocol-valid observations. The controlling direction is now `ontology-source-architecture-transcendent-synthesis.md`: preserve the tested format-neutral semantic boundary, separate source identity and Decision 53 authority, and retire one uncertainty per smallest falsifiable experiment. A four-format tournament is no longer the default.

### Original experimental model

V2 tested four candidate frontends against one preregistered semantic fact contract:

```text
Hardened Markdown | strict records | RDF/SHACL | immutable objects + manifest
                              ↓ independent compile + validate
                Candidate canonical semantic fact boundary
                              ↓ deterministic, loss-declared projection
                    Markdown | cards | RDF | graph | diagram | indexes

Independent authority inputs and lifecycle:
authored → released → desired → adopted → used
Ownership is contextual, not positional; use the Decision 53 ownership table.
```

The diagram is a hypothesis under test, not an accepted architecture. The fact boundary may become a production IR only if independent implementations and comparative evidence justify it.

#### 1. Authoring record

Evaluate a strict one-record-per-term textual source language, provisionally `rocs-source.v1`, as one candidate alongside hardened Markdown/frontmatter, RDF/SHACL, and immutable semantic objects:

- strict JSON in experiment V2, compared against hardened YAML frontmatter in V1;
- duplicate keys, aliases, merge keys, implicit dates, and ambiguous scalars forbidden;
- exact top-level schema and schema version;
- one normative definition;
- labels, synonyms, examples, anti-examples, lifecycle, and System4D fields typed consistently;
- relation assertions reference stable relation IDs, never labels;
- optional narrative guidance is explicitly non-normative.

If this candidate wins, Markdown may become a generated human projection. If hardened Markdown satisfies the same semantic contract with equal or lower complexity, Markdown remains the authoring frontend and only its normative/non-normative boundary is hardened.

#### 2. Canonical semantic IR generation

Two isolated experiment compilers independently map every candidate source into a closed canonical fact stream containing:

- terms and assertions with stable IDs;
- normalized localized text and typed literals;
- relation characteristics and lifecycle state;
- source provenance;
- separate semantic-equivalence and source/debug digests;
- specified canonical ordering;
- no implicit blank nodes or untyped extension fields.

The candidate IR is the sole **semantic-content** input to validation, pack, discovery, graph, diff, RDF, and diagram projections. Authority-bearing release or transaction operations additionally require independently acquired owner-issued facts and current-head observations. No semantic projection may manufacture those facts.

#### 3. Projections

- **Generated Markdown:** readable concept pages and review documentation.
- **Compact semantic cards:** bounded LLM context with explicit omissions and provenance.
- **RDF/OWL/SHACL:** standards interchange and explicitly scoped formal reasoning; unsupported constructs fail closed.
- **Graph/diagram:** presentation views bound to the IR digest; visual changes are non-authoritative proposals.
- **Indexes/databases:** disposable acceleration surfaces reproducible from an accepted generation.

Every projection declares whether it is lossless, semantically complete, or intentionally partial. Generated artifacts add no meaning.

#### 4. Authority plane

Git/source-tree identity proves authored bytes. A candidate semantic digest proves normalized semantic identity only if the experiment validates its contract. Neither proves approval, publication, currentness, desire, adoption, activation, use, delivery, or influence. Preserve accepted Decision 53's non-collapsible lifecycle—`authored → released → desired → adopted → used`—and its contextual owner split. Semantic owner, ROCS, AK, consumer owner, Pi, and recovery controller issue or verify only their owned facts; owner-store observations and current heads are external authority inputs, never IR projections.

### Why this hypothesis deserves testing

- Every candidate can preserve Git review while separating source bytes from semantic equivalence.
- Hardened Markdown may fix the observed defects without a second source language.
- RDF/SHACL may provide independent processor agreement with less bespoke machinery than a custom IR.
- Immutable objects may clarify identity while still losing to files on authoring and merge ergonomics.
- Purpose-built human, program, visual, and LLM projections remain valuable regardless of which frontend wins, provided their loss and authority status are explicit.

### What remains unresolved

1. Complete normative-field inventory, including System4D, examples, anti-examples, lifecycle, and relation characteristics.
2. Exact boundary between normative definition fields and non-normative narrative guidance, including disagreement behavior.
3. Semantic normalization, typed literals, Unicode, ordering, defaults, and the semantic-digest preimage; any normalized source/debug preimage is a separate, conditional contract.
4. Stable ROCS ID-to-IRI mapping and the supported RDF/OWL/SHACL profile.
5. Projection completeness, loss declarations, and supported round-trip guarantees.
6. Whether semantic provenance participates in equivalence or only a separate source/debug digest.
7. Independent compiler strategy, malformed-input corpus, and conformance fixture ownership.
8. Authoring, review, and merge cost across all four candidates.
9. Migration compatibility, which is irrelevant until a candidate wins.
10. Production authority/currentness, which remains governed separately by accepted Decision 53.

## Practical consequence

Do not rewrite the ontology, adopt the visual editor as authority, or rerun the four-format protocol by default. Retain current Markdown/frontmatter production behavior without calling it superior. Treat V2's 40/40 semantic agreement as bounded support for a serialization-independent semantic-content contract, not a production IR. Treat the 40/40 source/debug disagreement as evidence of underspecification, not evidence that a normalized source identity must exist. First establish its consumer and purpose; remove it from claims if semantic identity plus raw byte hashing is sufficient. The invalid cohort supplies no ranking; V3/V4 counts may form hypotheses only.

## Decision gate

The next legal artifact is a bounded source-identity protocol in `ontology-source-architecture-transcendent-synthesis.md`, beginning with purpose and alternatives and containing exact reviewable artifacts if normalization is still needed. Independent design review follows protocol completion; neither step is a source-format RFC/ADR. A passing micro-experiment may support a source/debug contract decision only; it cannot select a source format. Format comparison resumes only for a named unmet capability under a newly reviewed, minimally sufficient rule. Migration, production ROCS changes, ontology mutation, editor adoption, activation, publication, and release remain unauthorized.
