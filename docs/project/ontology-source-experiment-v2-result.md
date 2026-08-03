---
summary: "Closed result of ontology source experiment v2: semantic correctness passed, selecting cohort invalid, and no architecture winner."
read_when:
  - "Interpreting ontology source experiment evidence or deciding whether an architecture RFC may open."
  - "Designing a successor ontology authoring experiment or transcendent architecture iteration."
type: evidence
status: final
---

# Ontology source experiment v2 — result

## Disposition

- Protocol: `225e21b0eb05008ee2d36fb6d81fdc8c6dc77865c5d00c1300eff8192d991c3c`
- Evidence-tree digest: `54aa3651d1a96557c94b6a0df057d2b87da1be8d45dbd776b0fdbcf56b030f3a`
- Mechanical disposition: **`no_winner_insufficient_evidence`**
- RFC/ADR gate: **blocked**
- Production consequence: retain current Markdown/frontmatter behavior.

This result does not establish that Markdown is architecturally superior or permanent. It establishes that protocol v2 did not obtain lawful selecting evidence.

## Verified correctness evidence

Two independent implementations were built and locked without cross-inspection:

- Python A: `35d1eb4b3089ff8b735053724ecdf72d36ff21bd`
- Node/TypeScript B: `3842ee5305811661e431fcabcc9b56fa32fcd340`

Generation-3 comparison passed:

| Gate | Result |
|---|---:|
| Accepted source packets against golden oracle | 40 / 40 |
| Applicable malformed/error-precedence entries | 37 / 37 |
| Cross-implementation RDF directions | 80 / 80 |
| Projection completeness/loss metadata | pass |
| A/B wrapper validation | pass |
| A/B V4 author agreement and rollback | pass |
| Technical eligibility before ergonomics | V1, V2, V3, V4 |

The independent implementations initially exposed and then corrected two real defects before the cohort restarted:

1. V4 `changed_semantic_facts` needed the full canonical symmetric difference rather than additions only.
2. V3 missing `status` needed the frozen default `active` rather than rejection.

Those failed attempts and old locks are retained as superseded evidence, not counted as passing behavior.

## Non-gating semantic debt discovered

A and B produced different source/debug digests for all 40 accepted packets while agreeing on every semantic stream and semantic digest.

This did not violate a selecting correctness gate, but it proves that the source/debug digest preimage remains under-specified. A future production IR or release contract must not adopt either algorithm by convenience.

## Why the selecting cohort is invalid

Protocol v2 required:

- eight exact-model stateless Pi actors;
- 192 paired observations;
- one task prompt at a time;
- frozen command/tool policy;
- complete timing and blinded review evidence.

Observed:

- all eight replacement sessions used `openai-codex/gpt-5.6-sol`;
- all eight passed the unscored warm-up;
- 56 host-timed observation receipts were produced;
- the host interrupted round 8, leaving 136 observations missing;
- persistent sessions had received the interrupted prompt, so replay would not be the same observation;
- the supervisor supplied the actor instructions but not the contents of the frozen bash allowlist;
- all eight sessions therefore used prohibited commands; 37 prohibited bash calls were detected;
- zero observations qualify as protocol-valid selecting evidence.

The missing-observation rule and command-policy failure independently force `no_winner_insufficient_evidence`.

## Diagnostic-only actor signal

The 56 host receipts are retained for debugging but excluded from Pareto selection:

| Variant | Receipts | Diagnostic errors | Selection use |
|---|---:|---:|---|
| V1 hardened Markdown | 14 | 2 | forbidden |
| V2 strict JSON records | 14 | 2 | forbidden |
| V3 RDF/Turtle + SHACL | 14 | 0 | forbidden |
| V4 immutable objects + head | 14 | 14 | forbidden |

These counts are not architecture evidence. In particular:

- V1/V2 deprecation errors may reflect missing author-facing schema help rather than format quality;
- V4 errors expose that its authoring command and conflict workflow were not discoverable from the supplied actor surface;
- V3's zero diagnostic errors is interesting but cannot support selection after protocol violations and missing observations.

## Static complexity evidence

The deterministic source-LOC receipt recorded:

| Variant | A+B common-plus-variant LOC | Frozen contract bytes | Direct runtime dependencies |
|---|---:|---:|---:|
| V1 | 1457 | 2595 | 0 |
| V2 | 1200 | 2052 | 0 |
| V3 | 1576 | 6878 | 0 |
| V4 | 1391 | 2728 | 0 |

Hand-maintained surfaces, selecting error counts, full paired medians, and Pareto dominance remain unset because the cohort is invalid.

## Reversibility proof

Before evidence sealing:

- the immutable baseline Git status matched its preflight bytes;
- the baseline source-tree manifest matched byte-for-byte;
- the operator dirty-checkout porcelain-v1-z byte stream matched preflight exactly;
- the controller lineage was preserved in a verified Git bundle;
- 3,127 retained evidence files were independently hashed;
- Node independently verified evidence-tree digest `54aa3651d1a96557c94b6a0df057d2b87da1be8d45dbd776b0fdbcf56b030f3a`.

The local retained evidence root is under managed `TMPDIR` as `ontology-source-experiment-v2-225e21b0/evidence/`. It is execution evidence, not AK, ROCS, ontology, publication, or release authority.

## Successor constraints, without inherited tournament scaffolding

The next bounded work is not an actor cohort and does not inherit the tournament's allowlist, session-recovery, editor, projection, or four-variant machinery. It must first establish the source/debug digest's purpose: name a concrete consumer and show why semantic identity plus raw source-byte hashing is insufficient; then either author one independently testable normalized algorithm or remove normalized source/debug identity from architecture claims.

Only a future experiment that actually uses model actors, comparative onboarding, or V4 conflict tasks must correct the corresponding v2 failures before review:

- deliver and mechanically enforce the exact model-visible command allowlist;
- define interruption, replacement, timing, and contamination rules;
- supply equal bounded author-facing schema and command help;
- define lawful V4 conflict resolution without direct protected-head edits.

No successor may treat a 192-observation four-format tournament as the default. Retire one contract uncertainty at a time and require fresh justification for every added cohort, format, projection, or authority surface.

## Decision boundary

No source-format RFC/ADR may open from protocol v2. No ontology migration, production ROCS change, diagram-editor adoption, activation, publication, or release is authorized.

The governed transcendent iteration is recorded in `ontology-source-architecture-transcendent-synthesis.md`. Its next lawful step is bounded protocol authoring: establish a concrete source-identity purpose and, only if needed, supply exact fixtures, oracle, preimage grammar, algorithm, and errors. Independent design review follows only when that packet is complete. Any resulting micro-experiment cannot select a source format; an architecture RFC/ADR remains blocked.
