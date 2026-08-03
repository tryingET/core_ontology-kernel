---
summary: "POLARIS reasoning model and applied solution for separating ontology representation, semantic identity, projections, proposals, and owner-issued authority."
read_when:
  - "Deciding the relationship among ontology-kernel, ROCS, and ontology diagram tooling."
  - "Testing whether a new ontology identity, projection, or source format is justified."
type: analysis
status: proposed
---

# Ontology source architecture — POLARIS model

## Status and evidence boundary

No artifact can honestly prove that only a superintelligence could have developed it. POLARIS instead targets the useful part of that request: reason across information theory, compiler architecture, bidirectional transformations, governance, and experimental epistemology without collapsing their distinct kinds of truth.

This analysis applies the Prompt Vault `first-principles`, `telescopic`, `simplification`, `nexus`, `recursion-engine`, and `knowledge-crystallization` procedures. Their dispatch posture was `text_ok`. The model is grounded in:

- `ontology-source-experiment-v2-result.md`;
- `ontology-source-architecture-transcendent-synthesis.md`;
- `ontology-source-implicit-explicit-audit.md`;
- `ontology-source-architecture-greats-adjudication.md`; and
- the historical `ontology-source-architecture-comparative-experiment.md`.

It does not authorize a production semantic IR, source migration, ROCS change, ontology mutation, editor adoption, Decision 53 mutation, publication, activation, release, or source-format RFC/ADR.

## The mistake behind the original question

“What is the canonical format?” asks one object to answer several non-isomorphic questions:

1. Which exact bytes were authored?
2. Which semantic facts do those bytes denote under a contract?
3. Which facts are visible in a projection?
4. Which change is a tool proposing?
5. Which owner has approved, released, desired, adopted, activated, or used something?
6. Which owner-issued fact is current at action time?

A single canonical artifact cannot answer all six without silently absorbing other owners or confusing identity with authority. The architecture must therefore be **polycanonical**: canonicality belongs to a relation and an owner, not to one universal file.

## POLARIS

POLARIS is a seven-part reasoning model:

- **P — Polycanonical relations:** identify the relation before naming a canonical artifact.
- **O — Operation-indexed sufficiency:** add a distinction only for a named operation whose answer changes because of it.
- **L — Loss-declared lenses:** every projection and reverse path declares preserved, omitted, unsupported, and editable information.
- **A — Authority orthogonality:** semantic transformations have an authority ceiling and cannot mint owner facts.
- **R — Recursive proof generation:** generate tests from contracts, contracts from consumer operations, and adversarial cases from both.
- **I — Information accounting:** given a complete preimage, pinned function, and version, a digest is a derived witness; the governing equivalence contract adds coordination information, while neither can confer authority.
- **S — Sequential falsification:** test the first unsupported edge, stop on failure, and never fund a larger comparison to answer a smaller uncertainty.

The unit of architecture is not a format. It is a **proof-carrying relation**.

## Formal model

Let:

- \(b\) be exact authored bytes;
- \(p\) be separately stored path and provenance;
- \(K\) be a versioned semantic contract;
- \(C_K(b)\) produce normalized semantic facts \(F_K\) or typed error \(E_K\);
- \(canon_K(F_K)\) produce canonical semantic bytes;
- \(\pi_i(F_K)\) produce projection \(V_i\) plus a loss declaration;
- \(\delta_i(F_K,V'_i)\) produce a non-authoritative semantic proposal;
- \(A_o(t)\) be facts issued by owner \(o\), observed at time \(t\); and
- \(q\) be one named consumer operation.

### Distinct relations

**Byte identity**

\[
x \equiv_b y \iff bytes(x)=bytes(y)
\]

A raw digest is a compact operational witness for this relation under a stated collision assumption.

**Semantic identity**

\[
x \equiv_{s,K} y \iff canon_K(C_K(x))=canon_K(C_K(y))
\]

This relation exists only within the admitted domain of \(K\). Agreement on fixtures does not establish a global relation.

**Candidate normalized authored-form identity**

\[
x \equiv_{n,q} y \iff N_q(x,p_x)=N_q(y,p_y)
\]

This relation does not exist merely because a digest field was named. It requires a consumer, an equivalence contract, a preimage grammar, and evidence.

**Authority and currentness**

\[
Effective(q,t)=Policy(q,F_K,\{A_o(t)\})
\]

Authority/currentness is not another digest relation. Semantic content is one input to an action-time join with independently obtained owner facts.

## Five deductions

### 1. Digest non-creation

Given the complete preimage \((b,p)\), a pinned deterministic function, and its version, a digest is a derived witness: it adds no new source facts, proves no meaning, and confers no authority. The equivalence contract does add normative coordination information about which distinctions matter; bytes alone are insufficient when path or provenance participates. The 40/40 v2 source/debug disagreement is therefore evidence of an unspecified relation and preimage, not of a missing hash algorithm.

### 2. Nested intermediate-identity necessity

For a candidate relation intended to sit strictly between byte and semantic identity over a bounded admitted domain, path and provenance are excluded from the relation and all of the following are required:

1. **Lower refinement law:** byte equality universally implies normalized equality in the admitted domain.
2. **Upper refinement law:** normalized equality universally implies semantic equality under \(K\):

   \[
   \equiv_b \subseteq \equiv_{n,q} \subseteq \equiv_{s,K}
   \]
3. **Positive strictness witness:** two byte-different artifacts must be treated as the same by operation \(q\).
4. **Negative strictness witness:** two semantically identical artifacts must be treated as different by \(q\).
5. **Consequence:** a wrong classification causes a named failure.
6. **Coordination proof:** a shared relation reduces cross-producer ambiguity, replicated logic, or operational risk enough to earn its contract cost.

If path, provenance, or another discriminator makes the relation non-nested, it must be named as a separate operation-indexed equivalence with its own inputs and laws, not as an intermediate source identity. Given the complete preimage, pinned function, and version, the resulting digest adds no new source facts; the contract earns its cost only by providing shared normative coordination.

Absence of strictness witnesses establishes collapse only under a complete pair oracle for the admitted domain. With incomplete coverage, their absence establishes only that the proposed relation has not been justified.

### 3. Projection non-invertibility

If \(\pi_i\) is non-injective or declares loss for a fact kind, its output does not in general determine omitted information. Consequently, absence in an editor export may mean deletion only when the profile proves complete coverage and closed-world absence semantics for that fact kind.

### 4. Authority non-lift

Assign every transformation an authority ceiling. Compilation, validation, hashing, projection, editor export, and proposal decoding remain at `semantic_content` or `proposal`. No composition of those operations may yield `approved`, `released`, `desired`, `adopted`, `activated`, `used`, or `current`.

### 5. Evidence non-transfer

Represent an evidence item as:

\[
e=\langle claim,domain,operation,protocol,observer,validity\rangle
\]

Evidence may support a narrower claim inside the same axes. It cannot move laterally from semantic correctness to ergonomics, from RDF library round-trip to editor behavior, from byte identity to release, or from diagnostic output to architecture selection.

## Applying POLARIS to v2

| Frozen observation | Supported conclusion | Forbidden lift |
|---|---|---|
| A and B agreed on 40/40 accepted semantic streams/digests, the applicable malformed corpus, and 80/80 RDF directions. | The frozen mapping was independently realizable for the tested domain. | Global equivalence, production IR readiness, or format preference. |
| A and B disagreed on 40/40 source/debug digests. | The relation and preimage were under-specified. | A requirement for normalized authored identity or canonicality of either algorithm. |
| Zero cohort observations were protocol-valid. | No selecting evidence exists. | Winner, ranking, tie, elimination, or ergonomic conclusion. |
| V3 had 0/14 diagnostic errors and V4 had 14/14. | Candidate hypotheses about discoverability and conflict workflow. | Selection evidence. |

POLARIS therefore reproduces the lawful v2 disposition: retain current Markdown/frontmatter operationally, select no format, and preserve only bounded evidence for a format-neutral semantic boundary.

## Stage A application and reviewed result

This model first screened the candidate operations below. The complete bounded packet is `ontology-source-identity-purpose-gate.md`, and its independent PASS record is `ontology-source-identity-purpose-gate-review.md`:

| Consumer operation | Required mechanism | Normalized authored identity? |
|---|---|---|
| Reproduce exact input or export | Raw byte digest plus immutable retrieval/provenance | No |
| Detect semantic base staleness | Semantic contract identifier plus semantic digest | No |
| Review a semantic change | Canonical semantic diff plus exact source diff | No |
| Invalidate parse/build cache | Raw digest plus compiler/contract version | No |
| Deduplicate equivalent meaning | Semantic identity within contract \(K\) | No |
| Preserve formatting during rewrite | Original bytes plus a bounded patch/edit script | No |
| Explain which tool produced an artifact | Separate provenance and tool/profile versions | No |
| Determine approval, release, adoption, use, or currentness | Owner-issued Decision 53 facts observed at action time | Forbidden |
| Import an editor change | Base semantic digest, exact export hashes, profile, and proposal delta | No |

A concrete candidate within that screen is a ROCS projection-bundle producer serving an ontology maintainer through an editor adapter. The operation is to reject a stale semantic base, recover the proposed supported-fact delta, and reproduce the exact export. A wrong answer could apply a proposal to the wrong base, misstate the semantic delta, or make the export irreproducible. Semantic contract/digest, raw export hashes, and separate profile/tool provenance answer those questions without a normalized authored-form relation.

The bounded Stage A packet subsequently separated identity-sensitive answers from operation-invariant decoder/lens/receipt machinery, compared `remove`, `raw`, and `normalize`, and passed independent design review. Its scoped disposition is **`not_needed`**; source-identity protocol authoring closes without Stage B or a normalized digest.

This is not proof about undocumented future consumers or owner-issued acceptance of a production architecture. A future consumer may reopen Stage A only under the complete rule in `ontology-source-architecture-transcendent-synthesis.md`: name the producer, consumer, and operation; provide exact distinctions, required answers, and wrong-answer consequences; show why semantic identity, raw identity, and separate provenance fail for the identity-sensitive answers; and supply the appropriate nested or non-nested laws, witness pairs, and coordination benefit. Absence of witnesses outside a complete pair oracle is not proof that no such relation could ever exist.

## Applied solution architecture

```text
ontology-kernel
  current authored Markdown/frontmatter
  exact source bytes + raw receipts
            |
            | compile under versioned semantic contract
            v
ROCS candidate semantic boundary
  normalized facts + typed errors + semantic digest
            |
            +--------------------------+
            |                          |
            | validate/explain/pack    | loss-declared projection
            |                          v
            |                 editor projection bundle
            |                 RDF/OWL profile + base digest
            |                          |
            |                          v
            |                 ontology-diagram-editor
            |                 visual work + .odiagram layout
            |                          |
            |                          v
            +<---------------- semantic proposal delta
                               never a source write

Decision 53 owner facts -------------------> action-time policy join
(separate authority/currentness plane)       never compiler output
```

This is a candidate boundary model, not an assertion that production ROCS already implements it.

### `ontology-kernel`

- Owns reviewed authored ontology intent.
- Retains current Markdown/frontmatter until separate valid evidence justifies change.
- Does not treat Git state or semantic validity as release, adoption, activation, use, or currentness.
- May support replaceable frontends later, but source replaceability is not required for the boundary to be useful.

### ROCS

- Is the natural executor of the versioned semantic contract: compile, validate, explain, pack, project, and decode proposals.
- Emits typed failures rather than silently dropping unsupported fields.
- Carries semantic contract identity and declares projection loss.
- Does not manufacture Decision 53 authority facts.
- Has no established need for a normalized source/debug digest within the candidate operations screened here.

These are proposed responsibilities; production changes require their own decision and evidence.

### Ontology diagram editor

If separately tested and authorized, an editor could serve as a replaceable projection consumer and proposal UI under these candidate responsibilities:

- consume only a pinned, closed RDF/OWL projection profile;
- keep `.odiagram` layout separate from semantic facts;
- return an exact export and layout receipt plus a proposed semantic delta; and
- never write ontology source directly or become source or lifecycle authority.

## The editor boundary is a guarded asymmetric lens

For semantic contract \(K\) and projection profile \(P\), let:

```text
get_K,P(F)                         -> (receipt, V) | typed error
propose_K,P(F, receipt, V')        -> Δ | typed error
apply_K(F, Δ)                      -> F' | typed error
```

`receipt` binds the base semantic digest, semantic-contract identity, projection-profile identity, exact projection bytes, and tool version. Source rendering is deliberately outside the lens.

A bounded editor profile must prove:

1. **Receipt precondition**

   `propose` fails closed unless all three relations hold:

   ```text
   receipt.base_semantic_digest = digest_K(F)
   receipt.semantic_contract_id = K
   receipt.projection_profile_id = P
   ```

2. **No-op law**

   For a valid receipt and unchanged valid export:

   ```text
   propose_K,P(F, receipt, V) = empty
   ```

3. **Supported-edit and frame laws**

   For an export containing only supported edits:

   ```text
   Δ  = propose_K,P(F, receipt, V')
   F' = apply_K(F, Δ)

   editable_P(F')    = decode_editable_K,P(V')
   noneditable_P(F') = noneditable_P(F)
   ```

   Omission is not deletion outside fact kinds with proved complete coverage and closed-world absence semantics.

4. **Unsupported-construct law**

   Unsupported RDF/OWL constructs or edits outside \(P\) produce typed errors rather than approximations.

5. **Authority-ceiling law**

   Output status is `non_authoritative_proposal`; no editor field can elevate it.

6. **Loss-transparency law**

   The bundle lists included, omitted, unsupported, and editable fact kinds separately.

A source round-trip law such as `render(compile(source)) = source` is neither required nor generally desirable. Compilation may intentionally forget ordering, prose, comments, and presentation.

## Proof-carrying boundary packet

Every producer-consumer edge should eventually be described by one packet:

```text
producer
consumer
named operation
contract/profile version
admitted inputs
canonical output relation
preserved information
omitted information
unsupported information
editable information
identity witnesses
typed errors and precedence
authority ceiling
fixtures and independent oracle
tool versions
proof receipt
```

The packet is more durable than a format choice because it states exactly which capability is being claimed.

## Smallest falsifiable successor

Do not rerun the four-format tournament and do not implement a normalized source digest.

If the ontology owner wants visual change proposals, the smallest useful experiment is one isolated **editor guarded-lens probe**:

1. Pin one editor revision and one minimal RDF/OWL profile.
2. Freeze a tiny semantic fixture and its base semantic digest.
3. Generate one loss-declared editor bundle.
4. Test exactly four cases:
   - open/export without semantic change;
   - one supported semantic edit;
   - one unsupported or omitted fact-kind edit;
   - one proposal against a stale base.
5. Decode only to a `non_authoritative_proposal` delta.
6. Independently score the six lens requirements.
7. Stop on the first mismatch; do not repair the frozen oracle in place.

Passing would support only that pinned profile and those operations. It would not select a source format, authorize editor adoption, prove full ontology coverage, or open a source-format RFC/ADR.

If no owner names the visual proposal operation, perform no experiment. The correct move is subtraction.

## Prompt Vault synthesis

- **First principles:** yielded relation-specific axioms rather than inherited format assumptions.
- **Telescopic:** connected the micro-level 40/40 digest divergence to the macro-level collapse of identity kinds.
- **Simplification:** proposes removing normalized source identity, direct editor-to-source writes, and the universal-format objective from the candidate architecture.
- **Nexus:** identified the proof-carrying producer-consumer boundary as the one intervention that improves compilers, projections, editor safety, and future experiments simultaneously.
- **Recursion engine:** turns each contract into laws, each law into adversarial fixtures, and each failure into a narrower contract revision.
- **Knowledge crystallization:** preserves the reusable rule: architecture claims are proved relations indexed by consumer operation, not properties inherited from a file format.

## Final answer

The recommended candidate relationship is not Markdown versus RDF versus objects. It is:

- **Markdown/frontmatter remains the observed current authoring frontend without superiority status.**
- **ROCS would, only if later authorized, execute a format-neutral semantic contract whose evidence remains bounded to the frozen v2 scope until expanded.**
- **A diagram editor could, only if separately tested and authorized, act as a loss-declared, digest-bound proposal surface behind a guarded asymmetric lens.**
- **Raw byte identity, bounded semantic identity, and owner-issued authority/currentness remain separate.**
- **For the independently reviewed bounded consumer, normalized source/debug identity is `not_needed`; Stage B and normalized-digest implementation do not follow.**
- **Future evidence should target one producer-consumer capability at a time; no tournament or migration proceeds by default.**
