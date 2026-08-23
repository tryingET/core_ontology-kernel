---
summary: "Exact-OID assessment of ontology-kernel readiness for its next immutable release after v0.1.0."
read_when:
  - "Selecting the next ontology-kernel release version or release OID."
  - "Publishing ontology-kernel tags or handing a release to consumers."
type: evidence
status: final
task_id: 4880
---

# Ontology-kernel immutable release readiness

## Assessment result

| Field | Result |
|---|---|
| Assessed candidate | `e5efc3b8a818ac4f592d0b369d7e1bf718057f0e` |
| Latest observed release tag | `v0.1.0` |
| Released commit | `3c493fecc8dbdb890e23684816b6325f1ad8463d` |
| Semantic delta | Additive: 9 concepts, 1 relation, and 6 assertions; no removed or deprecated IDs or assertions |
| Recommended next version | Provisional semantic-surface recommendation: **`v0.2.0`**, subject to repository-compatibility review, release authorization, and final-OID selection |
| Release readiness | **Not ready to tag or publish yet** |

The candidate passes the repository's strict gate in a clean detached checkout at the exact
assessed OID. The ontology-meaning delta supports a provisional MINOR recommendation: it adds
stable public IDs and assertions without removing IDs or changing the machine-normative identity
and characteristics of existing terms. Because one Git tag covers the whole repository, the
release owner must separately accept the source-contract and tooling compatibility posture before
turning that semantic-surface recommendation into a release version.

This assessment does **not** authorize a release. No task inspected here authorizes creating or
pushing a tag, the final release OID has not been selected, release-version metadata remains
unresolved, and the intended remote set and immutable-tag controls are not explicit. If NAS is an
intended release remote, secure transport remains blocked by AK `4861`; AK `4852` covers branch
parity only and grants no tag-publication authority.

## Authority and scope

- Execution authority: AK task `4880`.
- Direction: `AK.V5.SF01.WW02`, “Secure publication and immutable release readiness.”
- Owner release contract: [`RELEASING.md`](../../RELEASING.md).
- Source-contract decision: [Decision 110 ADR](../adr/2026-08-03-ontology-markdown-rocs-contract-v1.md).
- Branch-parity anchor: AK `4852`, blocked by holdingco GitLab owner task `4861`; neither task authorizes a release tag.
- Mutation ceiling: this task may add only this assessment. It may not change ontology source,
  manifests, scripts, tests, branches, remotes, or tags.

Git observations below establish repository transport facts only. They do not establish semantic
release authority, publication authority, consumer adoption, activation, use, or currentness.
ROCS observations establish operation-qualified source-contract/schema/reference conformance for
the exact admitted corpus; they do not establish a generic semantic-correctness verdict.

## Exact endpoint binding

| Identity | Exact value | Observation |
|---|---|---|
| Tag ref | `refs/tags/v0.1.0` | Sole observed release tag |
| Annotated tag object | `7da7f6e916d3f5f6f65fa1a11c3b8eb400d22e5c` | Observed locally and on `origin` |
| Tag's released commit | `3c493fecc8dbdb890e23684816b6325f1ad8463d` | `v0.1.0^{commit}` |
| Released ontology source tree | `8acdab1c89a9ab9553e8430115c9e289a65c9885` | `<released-commit>:ontology/src` |
| Assessed candidate commit | `e5efc3b8a818ac4f592d0b369d7e1bf718057f0e` | `HEAD`, local `main`, `origin/main`, and `github/main` agreed at assessment time |
| Candidate ontology source tree | `266409404a9570ab4bfe48002f91d1bdef0e5764` | `<candidate-commit>:ontology/src` |
| Commit relationship | Released commit is the merge base; candidate is 46 commits ahead | No history rewrite in the compared range |

“Latest” means the sole release tag visible in this checkout and the queried public remote. The
server-side immutability/protection configuration for that tag was not inspected. The tag is
annotated but unsigned; current repository policy does not state whether signatures are required.

## Semantic delta

A current ROCS 0.3.0 build was run against disposable exact-OID worktrees for both endpoints.
This uses one parser for the comparison; the reported `summary.json.version` is the ROCS tool
version, not the ontology-kernel release version.

| Corpus | Concepts | Relations | Profile |
|---|---:|---:|---|
| `v0.1.0` released commit | 28 | 11 | Legacy/default |
| Assessed candidate | 37 | 12 | `kernel-v1` |
| Delta | **+9** | **+1** | Source contract adopted |

### Added IDs

| Slice | Added IDs | Classification |
|---|---|---|
| Planning | `core.Milestone`, `core.Program`, `core.WorkItem`, `core.rel.depends_on_plan` | Additive planning vocabulary; the new relation is explicitly distinct from runtime/build `core.rel.depends_on` |
| Evidence and authority | `core.Observation`, `core.Evidence`, `core.Claim`, `core.Verification`, `core.Receipt`, `core.Authority` | Additive, implementation-independent evidence-chain and scoped-mandate vocabulary |

### Added assertions

The compiled graph grows from 5 to 11 edges. These six assertions are additive; none removes or
replaces a released assertion:

| Added assertion | Classification |
|---|---|
| `core.Authority core.rel.constrains core.Verification` | A scoped mandate bounds what may be verified or promoted |
| `core.Authority core.rel.depends_on core.Policy` | Recognized authority requires an applicable policy |
| `core.Claim core.rel.precedes core.Verification` | A claim exists before it is checked |
| `core.Evidence core.rel.depends_on core.Observation` | Evidence is grounded in a bounded observation |
| `core.Verification core.rel.uses core.Evidence` | Verification checks against evidence |
| `core.Verification core.rel.produces core.Receipt` | Verification yields a custody/lineage receipt |

No concept or relation ID was removed or deprecated. No existing concept file changed between the
released and assessed ontology source trees.

All 11 existing relation documents changed as part of Decision 110's source-contract migration:
examples and anti-examples moved under `ont`, and explicit definition prose was added. Their IDs,
types, labels, concise descriptions, relation groups, inverses, transitivity, symmetry, and axes
remain unchanged. The Decision 110 ADR classifies this as guidance relocation intended to preserve
meaning and keeps body prose as guidance.

`core.rel.constrains` also adds `core.Authority` to its prose Domain/Range guidance. This is an
additive explanation for the new `core.Authority constrains core.Verification` assertion; it does
not change the existing relation's machine-normative frontmatter. A release reviewer should still
confirm this classification rather than infer it solely from file shape.

### SemVer classification

Provisional semantic-surface recommendation: **`v0.2.0`**.

- the ten new stable IDs and six assertions expand the public semantic surface;
- no released ID, assertion, lifecycle state, concise definition, or relation characteristic was
  removed or incompatibly redefined;
- a patch would understate the additive semantic API;
- the repository contract reserves MAJOR for breaking meaning changes.

For this recommendation, the public semantic surface means ontology IDs, their machine-normative
frontmatter, and compiled assertions. The Git tag also distributes the source grammar, profile,
vendored validator, and repository gate. The known consumer boundary now requires ROCS behavior
that understands `ontology-markdown-v1` and profile `kernel-v1`; this assessment did not test a
fleet of older consumers. A release owner must therefore accept that source/tool compatibility
posture—or choose another version—before authorizing the repository-level tag.

The manifest still contains `rocs.version: "0.1.0"`. The repository does not currently state
whether that field must equal the Git release tag. Before selecting a final release OID, the owner
must either update it under a separately scoped task or explicitly document why it is independent
of the kernel release version. This assessment does neither.

## Non-semantic repository delta

The 46-commit range also includes substantial contract, validation, and evidence work:

- adoption of `ontology-markdown-v1` and profile `kernel-v1`;
- an expanded schema/conformance contract;
- vendored ROCS 0.3.0 and its integrity manifest;
- the strict self-contained repository gate;
- OID-only cross-owner handoff verification;
- semantic-owner sandbox and source-architecture evidence, all with explicit non-authority ceilings.

These changes improve reproducibility and validation but do not themselves authorize a semantic
release or prove downstream adoption. They are part of the tagged repository compatibility
surface even though they are not changes to ontology meaning; the provisional `v0.2.0`
classification therefore requires explicit owner acceptance of that boundary.

## Validation receipts

### Strict candidate gate

The exact owner command was run in a clean detached worktree at
`e5efc3b8a818ac4f592d0b369d7e1bf718057f0e`:

```bash
ROCS_CI_PROFILE=main-strict ./scripts/ci/full.sh
```

Observed result: **exit 0**.

- before and after `HEAD`: `e5efc3b8a818ac4f592d0b369d7e1bf718057f0e`;
- before and after status SHA-256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
  (empty tracked/untracked status);
- corpus: 37 concepts, 12 relations, 11 edges;
- source contract: `ontology-markdown-v1`;
- admitted documents: 49;
- corpus digest: `sha256:8a5bb9f3620791d2b5eb2e2f93fbeaa763c72e99060e39fdc777bcae952a14d0`;
- validate, build, vendored integrity, summary, lint, graph, inverse check, normalize, bounded pack,
  discovery, bound pack, synthetic routing, and generated-hook probe all passed.

AK evidence `7279` retains the bounded command receipt: start `2026-08-23T16:35:49Z`, end
`2026-08-23T16:35:58Z`, exit `0`, 5,447 output bytes, and output digest
`sha256:1c9dc0fd812bc13b1383bb6319e4ff30456804b09e939931e46fc9d24ed1d41a`.
The disposable full transcript was removed after hashing; the durable AK receipt contains the
command, exact OID, pre/post hashes, corpus identity, and bounded result facts.

The operator checkout contained 113 ignored Python cache files under the vendored runtime during
assessment. The strict bundle verifier rejects unexpected files, so a direct gate there would fail
before cleanup even though Git reports a clean tracked worktree. The passing receipt above used a
clean exact-OID checkout. Any release execution must do the same or perform owner-approved cleanup
before the gate; ignored contamination must never be mistaken for a source failure or silently
excluded from the integrity check.

A read-only exploration subagent also invoked ROCS `graph` in the operator checkout and overwrote
an ignored generated `ontology/dist/graph.json`. No pre-task hash exists for that ignored file, so
this assessment does not claim byte-preservation for all ignored runtime artifacts. Git-visible
scope remains exact—only this assessment is changed—and the canonical ontology source, manifest,
scripts, tests, branches, remotes, and tags remain unchanged. All acceptance gates used disposable
worktrees to avoid relying on the operator checkout's ignored state.

### Released-corpus comparison

A disposable detached worktree at
`3c493fecc8dbdb890e23684816b6325f1ad8463d` was built with the same bounded ROCS parser. It
reported 28 concepts and 11 relations. Set comparison against the candidate produced exactly the
ten added IDs listed above and no removed ID.

### Documentation and independent review

- Strict documentation validation passed at `2026-08-23T16:36:08Z` with exit `0`; AK evidence
  `7280` records output digest
  `sha256:c2d75dee5b2e0b58655c587a58e79b397ba87d78dc78075cc1098d6a1527f78d`.
- Independent review `dispatch-1787502400475` first returned `REVISE`, then accepted the corrected
  artifact with no blocker, high, or medium finding. AK evidence `7281` binds the accepted reviewed
  bytes (`sha256:40c63a4008a4b0a4f6fb2bfd96c10b66ad114dec644e21788bc3cd3e147a393a`)
  and records `ACCEPT` for all three task review questions.

## Publication and remote state

Observed read-only remote state at assessment time:

| Remote | Candidate `refs/heads/main` | `refs/tags/v0.1.0` | Pre-authorization candidate-tag state |
|---|---|---|---|
| `origin` | Exact candidate OID | Present; peels to released OID | Not created (expected) |
| `github` | Exact candidate OID | Absent | Not created (expected) |
| `gitlab-nas` | Not safely observable as current candidate | Not safely established | Not created/unestablished |

The configured NAS fetch uses SSH, but its push URL uses plaintext HTTP with an OAuth-style
username. The owner verifier returns `insecure_remote_transport`. If NAS is selected as an intended
release remote, AK `4861` must first close with owner proof of authenticated SSH or TLS HTTPS and a
supported route. AK `4852` remains deferred behind it but authorizes only the two branch refs
recorded in that task—not a release tag. The current URL must not be used, and no credential should
be placed in plaintext transport.

`RELEASING.md` says to push an exact tag refspec to “each intended remote” but does not enumerate
that set. The two configured GitHub remotes already differ in tag population. Release execution
therefore needs an explicit intended-remote list and evidence of tag immutability/protection for
each destination rather than inferring policy from remote names.

## Readiness matrix

| Requirement | Status | Evidence or blocker |
|---|---|---|
| Exact candidate assessed | Pass | Full OID and source tree bound above |
| Semantic delta classified | Pass | +9 concepts, +1 relation, +6 assertions; no removals |
| Proposed SemVer | Provisional semantic-surface recommendation | `v0.2.0`; repository compatibility and owner approval remain open |
| Strict gate at assessed OID | Pass | Clean detached exact-OID receipt |
| Source-contract conformance | Pass | Complete for 49-document corpus |
| Release execution authority | **Blocked** | AK `4880` authorizes assessment only |
| Final release OID | **Blocked** | Must follow owner disposition and any version-metadata change |
| Version metadata disposition | **Blocked** | Manifest remains `0.1.0` |
| Intended remotes and immutable-tag controls | **Blocked** | Not explicitly enumerated/proven |
| Secure NAS release transport | **Conditionally blocked** | AK `4861` if NAS is an intended release remote; AK `4852` is branch parity only |
| Candidate release tag | Not created (expected) | A separate task must authorize creation and exact destinations |
| Consumer pins and validation | Not assessed | Must be separate consumer-owner work |

## Consumer-pin implications

A consumer must not pin `main` or infer a release from branch presence. After a release owner
selects and publishes an immutable tag, each consumer owner should:

1. pin the exact `vX.Y.Z` tag required by `RELEASING.md`;
2. record and verify the tag's peeled full commit OID;
3. run its own owner-declared ROCS/CI acceptance gate;
4. record adoption in its own AK authority surface.

No consumer inventory was performed by this repo-local task. Publication, handoff verification,
and this assessment do not establish any consumer's adoption or currentness.

## Minimum next legal sequence

1. Obtain owner disposition on this assessment and the proposed `v0.2.0` classification.
2. Create a separately scoped release task or decision that names the version, final full commit
   OID, allowed metadata changes, intended remotes, immutable-tag controls, and rollback boundary.
3. Resolve the manifest-version question and re-run the strict gate plus independent review at the
   resulting exact release OID in a clean checkout.
4. If NAS is an intended release remote, resolve AK `4861`. Complete AK `4852` separately for its
   exact branch-parity refspecs; do not treat it as tag authority.
5. Under the separate release authority, create the exact annotated tag at the selected OID, push
   explicit tag refspecs to every explicitly intended remote, and verify each live tag ref and
   peeled commit.
6. Hand adoption to consumer owners; do not close their work from ontology-kernel publication.

## Rollback and nonclaims

This task adds one assessment document only. Rollback is a revert of that document's commit while
preserving AK history and all Git refs. No tag, branch, remote, ontology source, manifest, release,
publication, adoption, activation, use, or currentness fact is created by this assessment.
