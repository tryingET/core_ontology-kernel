---
summary: "Frozen isolation, independent implementation, ergonomics, evidence, and cleanup runbook for ontology source experiment v0."
read_when:
  - "Executing or reviewing ontology source experiment v0."
type: procedure
status: proposed
---

# Experiment runbook v0

## Entry gate

Do not begin implementation unless an independent rereview records `PASS` and `execution ready` for the complete protocol bundle.

At entry, record:

- protocol artifact paths and SHA-256 digests;
- one aggregate `protocol_digest` over lexical `sha256  path\n` lines;
- baseline commit and `baseline-manifest.v0.json` verification;
- exact host, OS, CPU, memory, locale, timezone, runtime, package-manager, model/provider, and tool versions;
- network-disabled execution proof;
- clean immutable baseline checkout status;
- writable variant-root and retained evidence-root paths under managed disk-backed temporary storage.

A mismatch stops with no implementation.

## Workspace topology

```text
<managed-root>/baseline-readonly/        # exact clean commit; chmod read-only after verification
<managed-root>/variant-v1/               # writable fixture copy only
<managed-root>/variant-v2/
<managed-root>/variant-v3/
<managed-root>/variant-v4/
<managed-root>/impl-a/                    # isolated Python implementation
<managed-root>/impl-b/                    # isolated TypeScript implementation
<managed-root>/comparator/                # created only after A and B lock
<retained-evidence-root>/                 # receipts copied before disposable cleanup
```

The operator's ontology-kernel working tree is never an execution or output root.

Compute the baseline source-tree digest exactly as specified in `baseline-manifest.v0.json`. Record Git status as porcelain-v1-z bytes and hash those bytes. Untracked files are impossible in the clean baseline; if present, preflight fails.

## Freeze order

1. Freeze and digest this protocol bundle.
2. Materialize exact accepted and malformed fixture bytes from the bundle.
3. Verify every materialized source digest against its manifest.
4. Freeze expected golden streams and digests.
5. Freeze dependency allowlists and locks independently for implementation A and B.
6. Only then permit compiler code.

Changing a protocol, fixture, oracle, expected error, dependency class, or decision rule after step 4 creates protocol v1; v0 execution stops.

## Independent implementations

### Implementation A

- runtime: Python 3, exact patch version recorded at freeze;
- source and lock live only under `impl-a`;
- may read protocol and fixture bytes;
- may not read `impl-b`, B outputs, B logs, or comparator outputs;
- emits its own canonical facts, digests, errors, loss reports, and projections.

### Implementation B

- runtime: Node.js/TypeScript, exact versions recorded at freeze;
- source and lock live only under `impl-b`;
- may read protocol and fixture bytes;
- may not read `impl-a`, A outputs, A logs, or comparator outputs;
- uses a different RDF parser implementation from A;
- emits its own canonical facts, digests, errors, loss reports, and projections.

### Lock protocol

Each implementation is built by a separate fresh executor. Before comparison, each executor records:

- Git commit or immutable tree digest;
- dependency-lock digest;
- test command and result;
- source inventory and LOC receipt;
- statement that the other implementation and outputs were not inspected.

After lock, make both implementation roots read-only. The comparator is then created by a third executor. Any post-lock implementation change invalidates all comparison results and requires two new locks.

### Scoring order

For every case:

1. score A independently against the frozen golden oracle;
2. score B independently against the frozen golden oracle;
3. compare A with B;
4. preserve all three dispositions.

A↔B agreement cannot compensate for disagreement with the oracle.

## Accepted-case tasks

The accepted golden cases and exact expected streams are controlling. The source reorder and Unicode-equivalence cases must prove equal digests where declared. Label, definition, edge, and lifecycle cases must prove the exact identity relationships declared in `golden-cases.v0.json`.

## Malformed-case execution

Run cases in manifest order. For each applicable variant and implementation, record:

- input payload SHA-256;
- actual disposition;
- actual typed error;
- actual precedence result;
- expected values;
- pass/fail.

`not_applicable` is legal only where the frozen manifest says so. Parser crashes, untyped exceptions, multiple unordered errors, hangs, and silent coercion fail.

Fixed per-case timeout: 10 seconds wall clock and 256 MiB additional resident-memory budget. A timeout returns `E_TIMEOUT` and fails because `E_TIMEOUT` is not an expected v0 error.

## RDF round-trip

For each implementation and accepted case:

1. facts -> v0 RDF profile;
2. parse using that implementation's locked RDF library;
3. serialize in any standards-valid form;
4. parse with the other independently locked RDF library in an isolated process;
5. compile back to facts;
6. compare with the frozen golden stream.

No network, imports, remote contexts, blank-node skolemization, or unsupported constructs are allowed. Both directions must preserve 100% of supported facts.

## Selecting authoring tasks

Six paired tasks are selecting ergonomics evidence:

| Task | Exact requested semantic delta |
|---|---|
| T1 add | Add `core.ExperimentProbe`, type concept, label `ExperimentProbe`, definition `A bounded term used only by ontology source experiment v0.`, one `core.rel.is_a` edge to `core.Actor`, one example and one anti-example. |
| T2 deprecate | Deprecate `core.Policy` since `2026-08-03`, replace with `core.DecisionRecord`, decision reference `experiment://decision/deprecate-policy`. |
| T3 rename label | Change only `core.Agent` label from `Agent` to `Agentic Actor`; preserve term ID and all other semantic facts. |
| T4 definition | Change only `core.Release` definition to `An immutable, version-addressed artifact set.` |
| T5 taxonomy correction | Start from the frozen synthetic wrong edge `core.Agent core.rel.is_a core.Policy`; correct only its target to `core.Actor`. |
| T6 merge | Resolve two prepared branches for `core.Secret`: branch A changes the label to `Protected Secret`; branch B adds guidance example `Short-lived deployment credential`; retain both intended changes and no others. |

Each variant receives byte-exact starting snapshots and task prompt digests from the retained evidence manifest before actors begin. T1–T6 expected semantic deltas correspond to frozen golden cases or explicit fact-delta entries in the golden manifest.

Actors may use only the variant's documented authoring interface, local validation command, and local diff tools. They may not inspect another variant during a task.

## Actor cohort

- eight fresh stateless Pi sessions;
- exact provider/model: `openai-codex/gpt-5.6-sol`;
- identical system instructions, tool allowlist, task prompt, fixture bytes, and local validation help;
- no inherited conversation context;
- no network;
- one unscored warm-up task on a separate toy fixture before timing;
- each actor performs T1–T6 for every variant.

Required paired observations: `8 actors × 6 tasks × 4 variants = 192`. Any missing observation makes selecting ergonomics `insufficient_evidence`.

### Counterbalancing

Variant order uses this fixed balanced set:

| Actor | Variant order |
|---|---|
| A1 | V1, V2, V3, V4 |
| A2 | V2, V3, V4, V1 |
| A3 | V3, V4, V1, V2 |
| A4 | V4, V1, V2, V3 |
| A5 | V1, V4, V3, V2 |
| A6 | V2, V1, V4, V3 |
| A7 | V3, V2, V1, V4 |
| A8 | V4, V3, V2, V1 |

Task order is T1 through T6 for odd actors and T6 through T1 for even actors. No random seed is needed because order is fully enumerated.

### Timing

- start: task prompt and writable starting fixture are both available, immediately before actor control;
- stop: actor submits final answer and releases the fixture, before reviewer feedback;
- clock: host monotonic nanoseconds;
- timeout: 900 seconds per observation;
- timeout value in timing metric: 900 seconds;
- setup, warm-up, reviewer time, and compiler batch time are excluded;
- environment is reset from the byte-exact starting snapshot between observations;
- no cache persists except runtime/package caches shared equally and warmed before all scored runs.

### Error scoring

One observation has `authoring_task_error=1` if any is true:

- timeout;
- variant source fails its own validator;
- emitted canonical facts differ from expected delta;
- unintended semantic fact changes;
- actor manually edits a generated/protected surface;
- merge drops either intended branch delta;
- actor requires prohibited cross-variant information.

Otherwise it is `0`. Machine oracle scoring is controlling.

### Blinded review

Two additional fresh stateless reviewer sessions use the same exact model/provider but do not author tasks. Before review:

- replace variant names with stable blind codes derived from a protocol-fixed mapping held by the comparator;
- remove timing and implementation-size data;
- present only task, before/after rendered semantic diff, source diff, validation result, and projection-loss report.

Review rubric, each 0 or 1:

1. requested meaning is clear in source diff;
2. unintended meaning is absent;
3. normative versus guidance boundary is visible;
4. generated/authority status is unambiguous;
5. merge resolution is reviewable for T6.

Reviewer disagreement is retained. It does not override machine correctness and is descriptive unless both reviewers find an ambiguity that maps to a frozen error condition. No subjective adjudicator selects a winner.

## Complexity evidence

After implementations lock, a fourth read-only measurement process records every dimension defined in `decision-rule.v0.json`. It emits raw values, commands, included/excluded paths, and a Pareto matrix. Missing values produce `no_winner_insufficient_evidence`; they are never imputed.

## Projection and editor probe

Generate canonical facts, Markdown, compact cards, RDF, graph JSON, and a digest-bound editor import bundle. The editor probe checks only:

- file acceptance under the frozen RDF profile;
- stable IRI rendering;
- round-trip proposal export without claiming semantic acceptance;
- `.odiagram` layout separation;
- visible source semantic digest and partial/non-authoritative status.

If the editor requires writes to ontology source, network access, publication, or authority state, stop the editor probe and record the blocker. It does not block semantic compiler correctness but blocks any editor-utilization claim.

## Evidence retention and cleanup

Before cleanup, copy into the retained evidence root:

- protocol and baseline manifests;
- materialized fixture manifests and bytes;
- A/B locks, source inventories, LOC and dependency receipts;
- every fact stream, digest, error, loss report, RDF round-trip receipt, and projection;
- all actor prompts, session identifiers, patches, timings, errors, and blinded reviews;
- Pareto matrix and mechanical disposition;
- baseline before/after Git status bytes and source-tree digest;
- owned command logs.

Create and verify an evidence-root SHA-256 manifest. Only then delete disposable variant and implementation copies. Never delete the retained evidence root automatically.

Final reversibility passes only when:

- immutable baseline Git status bytes equal preflight bytes;
- immutable baseline source-tree digest equals preflight digest;
- operator dirty checkout status for pre-existing paths is unchanged;
- all experiment outputs are outside both source checkouts;
- retained evidence manifest verifies.

## Final disposition

Apply `decision-rule.v0.json` mechanically. Report exactly one:

- `winner:V1|V2|V3|V4`;
- `no_winner_retain_current`;
- `no_winner_incomparable`;
- `no_winner_insufficient_evidence`.

Do not open an architecture RFC, run the transcendent iteration, or claim editor adoption until the complete evidence packet exists. The transcendent iteration consumes the evidence packet; it does not repair missing evidence by reasoning.
