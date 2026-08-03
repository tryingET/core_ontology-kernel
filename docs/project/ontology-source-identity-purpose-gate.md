---
summary: "Stage A purpose gate for normalized ontology source identity, recommending not_needed because semantic identity, raw hashes, and separate provenance answer the bounded editor-proposal operation."
read_when:
  - "Considering a normalized source/debug digest or authored-form identity."
  - "Designing a ROCS-to-editor projection or proposal boundary."
type: analysis
status: final
---

# Ontology source identity — Stage A purpose gate

## Disposition

- Gate: Stage A from `ontology-source-architecture-transcendent-synthesis.md`
- Concern: normalized authored-form identity, previously called `source/debug identity`
- Bounded candidate consumer: an ontology maintainer using a future ROCS-to-diagram-editor proposal adapter
- Disposition: **`not_needed` recommended**
- Stage B: **not entered**
- Implementation: **not authorized and unnecessary for this disposition**
- Independent review: **`PASS`**, recorded in `ontology-source-identity-purpose-gate-review.md`

This packet does not establish that no future consumer could need another operation-indexed equivalence. It establishes only that the bounded operation below does not justify normalized authored-form identity and that the reviewed evidence names no other concrete consumer.

## Evidence boundary

Observed from the sealed v2 result:

- two independent implementations agreed on the frozen semantic outputs while disagreeing on all 40 source/debug digests;
- zero actor-cohort observations were protocol-valid selecting evidence;
- no format winner exists; and
- current Markdown/frontmatter remains operational behavior without superiority status.

Derived by the reviewed POLARIS model:

- a digest is a witness for a specified preimage, not a definition of identity;
- a normalization contract adds normative coordination information but no authority;
- an intermediate identity requires a bounded consumer operation, laws, consequences, and distinguishing witnesses; and
- authority/currentness remains external under Decision 53.

This packet supplies contract analysis, not new empirical behavior evidence.

## Concern boundary

### Producer

A candidate ROCS projection path producing a projection receipt with:

- a semantic-contract identifier;
- a base semantic digest;
- exact projection bytes and raw hashes;
- a pinned projection-profile identifier;
- ROCS/tool-version provenance; and
- an explicit loss/editability declaration.

A candidate editor adapter separately records an export receipt containing the exact export bytes/hash, editor version, and originating projection-receipt identity. Both paths are proposed; production ROCS and the editor are not claimed to implement them.

### Consumer

An ontology maintainer reviewing a semantic proposal derived from a pinned diagram-editor export.

The editor and adapter are candidate tools, not adopted or authoritative surfaces.

### Single operation

> Determine whether a diagram-editor export is a reproducible proposal against the same semantic base from which its projection was generated, and recover only the supported semantic delta without interpreting omitted information as deletion.

### Required answer

The operation must answer:

1. Does the proposal target the reviewed semantic base under the same semantic contract?
2. Are the projection bytes exactly those named by the projection receipt, and are the export bytes exactly those named by the linked export receipt?
3. Which projection profile and tool versions produced the view and export?
4. What supported semantic facts were added, removed, or changed?
5. Were non-editable and omitted fact kinds preserved rather than inferred as deleted?
6. Is the result still only a non-authoritative proposal?

### Wrong-answer consequences

- A stale proposal could be applied to a different semantic base.
- A byte-different export could be mistaken for the reviewed artifact.
- Tool/profile drift could make the result irreproducible.
- Omitted facts could be misclassified as deletions.
- Unsupported editor behavior could be approximated silently.
- A valid semantic proposal could be mistaken for approval, release, adoption, activation, use, or currentness.

## Operation-invariant machinery

Stage A compares identity dispositions; it does not pretend that identity mechanisms implement the entire editor operation. Every disposition—`remove`, `raw`, or `normalize`—would still require the same baseline machinery:

- a guarded proposal decoder and typed errors for supported semantic changes;
- loss/editability declarations plus frame and closed-world-absence laws;
- linked projection and export receipts; and
- an authority ceiling with Decision 53 owner facts obtained separately when an action requires them.

The discriminating question is narrower: **does any required answer additionally change under a normalized authored-form relation after bounded semantic identity, raw artifact identity, and separately queryable provenance are available?** The decoder, lens laws, and authority boundary do not count as evidence for or against that extra identity.

## Candidate distinctions

| Distinction | Required treatment | Mechanism |
|---|---|---|
| Exact same bytes vs any byte change | Different exact artifact | Raw byte hash plus immutable retrieval |
| Different bytes with the same bounded semantic facts | Same semantic base, different exact artifact | Semantic digest and raw hashes remain separate |
| Same semantics under different semantic-contract versions | Outside equality until contract relationship is specified | Semantic-contract identifier |
| Same bytes under different projection profiles | Different interpretation context | Projection-profile identifier |
| Same bytes produced by different tool versions | Distinct provenance even when artifact bytes coincide | Separate tool/version provenance |
| Supported semantic edit | Proposal delta | Guarded profile decoder |
| Omitted or non-editable fact kind | Preserve; absence is not deletion | Loss/editability declaration and frame law |
| Approval/currentness difference | Never derived from content identity | Decision 53 owner facts at action time |

None of these distinctions requires an intermediate normalized authored-form relation.

## Disposition comparison

### `remove`

Interpretation: do not define normalized authored-form identity. Use distinct mechanisms for distinct questions:

- semantic contract plus semantic digest for bounded semantic-base identity;
- raw hashes for exact artifact identity;
- separate provenance for path, profile, and tool context;
- a guarded proposal decoder for supported semantic changes; and
- Decision 53 owner facts for authority/currentness.

Result: together with the operation-invariant machinery above, answers every required question without a new equivalence relation.

### `raw`

Interpretation: retain raw hashing and separate provenance alongside bounded semantic identity, but add no normalization algorithm.

Result: together with the invariant machinery, this is operationally the same identity architecture needed by the bounded consumer. `raw` is therefore an implementation description of the `remove` disposition, not evidence for a third identity.

### `normalize`

Interpretation: define an equivalence relation between byte and semantic identity, or a non-nested operation-indexed relation involving provenance.

To earn this disposition, the consumer would need at least one answer that changes under the normalized relation but cannot be answered cleanly by the mechanisms above. No such answer is present.

Potential normalization categories do not supply the missing purpose:

- line-ending or Unicode normalization changes an exact-byte question into a new policy question;
- map or fact reordering is already handled by bounded semantic identity when semantic order is irrelevant;
- comments, guidance, and layout require explicit classification, not an unlabeled source digest;
- path and provenance are clearer as separately queryable facts;
- cross-serialization equivalence is a semantic-contract question; and
- release/currentness is forbidden from content-derived identity.

Result: introduces contract, versioning, implementation, collision, fixture, migration, and debugging costs without a named additional answer.

## Decision rule application

| Requirement | Result |
|---|---|
| Named producer and consumer | Bounded candidate supplied |
| One operation | Supplied |
| Required answers | Supplied |
| Wrong-answer consequences | Supplied |
| Why semantic identity alone fails | It cannot identify exact bytes, provenance, or authority |
| Why raw identity alone fails | It cannot identify bounded semantic equality |
| Why separate provenance alone fails | It does not identify bytes or semantics |
| Why the three identity/provenance mechanisms together fail | **They do not fail for the identity-sensitive subquestions; invariant decoder, lens, receipt, and authority machinery handles the non-identity subquestions across every disposition** |
| Positive/negative witnesses for a nested intermediate relation | Not supplied because no required answer demands them |
| Coordination benefit exceeding contract cost | Not demonstrated |

Mechanical outcome for this bounded consumer: **`not_needed`**.

## Architecture consequence

Remove normalized `source/debug identity` from the candidate relationship among ontology-kernel, ROCS, and diagram tooling. Preserve three explicit channels:

```text
exact artifact channel    = raw bytes + raw digest + retrieval receipt
semantic channel          = semantic contract + bounded semantic facts/digest
context channel           = path/profile/tool provenance stored separately

authority/currentness     = independent Decision 53 owner facts

invariant operation layer = guarded decoder + typed errors + loss/frame laws
                            + linked projection/export receipts
```

Do not implement a normalized digest, canonical preimage grammar, pair oracle, or independent normalizers. Stage B exists only for a future `normalize` disposition and is not entered here.

## Owner and authority handoff

| Field | Binding |
|---|---|
| Source owner | ontology-kernel semantic/source owner |
| Native fact | authored bytes and accepted semantic content |
| AK fact | none created; future decision/task state remains AK-owned if authorized |
| Projection boundary | RDF/OWL/editor artifacts are loss-declared, digest-bound views or proposals |
| Mutation gate | separate owner approval plus repo/AK workflow before production or ontology mutation |
| Non-authorizations | no migration, ROCS change, editor adoption, ontology mutation, publication, activation, release, or source-format decision |
| Validation surface | independent review of this packet; any later editor capability uses a frozen guarded-lens protocol |

Decision 53 authority/currentness fields cannot enter semantic or source-identity preimages.

## Landing and next move

- Authority landing: `docs_only`
- Direction impact: `none`; this applies the existing transcendent synthesis rather than changing its source-format disposition
- Runtime/schema change needed now: `no`
- AK mutation needed now: `no`
- Prompt Vault mutation needed now: `no`
- Knowledge landing: `docs_only`

Independent design review passed. Source-identity protocol authoring closes at `not_needed`; no Stage B implementation follows. If an owner separately requests the visual-proposal capability, the next artifact is the smallest guarded-lens experiment protocol. Otherwise stop. Any later capability cannot inherit authority from this disposition or select a source format.
