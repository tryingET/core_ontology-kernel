---
summary: "Cross-owner closeout of the accepted Agent interaction direction through candidate isolation, authority correction, two read-only projection pilots, independent review, and rollback dogfood."
read_when:
  - "When deciding whether the Agent interaction pilots satisfied rollout gate G3"
  - "When considering a future engineering-core Agent Interaction discipline RFC"
  - "When checking the disposition of core.AgentExperience or ts-quality AX terminology"
type: "dogfood-closeout"
review_status: "complete"
architecture_disposition: "bounded_corrections_and_pilots_complete_g3_gate_hold"
---

# Agent interaction direction — implementation and dogfood closeout

- Architecture review: [`agent-experience-grand-architecture-review.md`](agent-experience-grand-architecture-review.md)
- Semantic review: [`core-AgentExperience-semantic-review.md`](core-AgentExperience-semantic-review.md)
- Core candidate disposition: AK task `4654`
- `ts-quality` correction and P1: AK task `4655`
- Agent Kernel P2: AK task `4656`
- Cross-owner closeout: AK task `4657`
- Independent closeout review: `dispatch-1785838172411` — PASS after G1A evidence, G3 hold, rollback attachment, and close-check remediation

## Verdict

**The bounded corrections and named pilot executions are implemented and dogfooded. G3 canary exit remains on hold because the full accepted read-effect, authorization, and redaction matrix is not closed.**

Completed:

1. the rejected `core.AgentExperience` candidate is preserved outside the active ROCS source root;
2. ordinary core retrieval is back to the admitted 31-concept, 12-relation, 43-document corpus;
3. active `ts-quality` guidance no longer projects nonexistent core authority or bare `AX` as canonical terminology;
4. `ts-quality` now uses explicit product-local structured JSON and command-specific machine-protocol terminology;
5. P1 and P2 produced executable read-only fixtures, exact owner joins, compactness measurements, omission/expansion evidence, independent review, AK evidence, and rollback proof;
6. task `4654` now carries AK evidence `6554`-`6556` and is done;
7. dogfood failures changed the implementations before closure rather than being explained away.

Not completed or authorized:

- no society-wide interaction contract;
- no engineering-core discipline/profile;
- no repo, Softwareco, or core ontology successor;
- no mutation settlement/retry pilot;
- no G3 canary exit or accepted gate variance;
- no complete read-effect, caller-authorization, or cross-owner redaction matrix;
- no Pi/template propagation;
- no package release, installed AK replacement, or remote publication.

# Gate disposition

| Gate | Result | Evidence ceiling |
|---|---|---|
| G1A — candidate/retrieval separation | Pass | exact archive digest, source absence, 31/12/43 ROCS corpus, negative pack, container full gate, independent review |
| G1B — `ts-quality` authority correction | Pass | active contract/docs correction, repo verification, independent review |
| G2 — local vocabulary decision | Pass | retire umbrella/bare acronym from active guidance; no repo ontology insertion |
| G3 — named reversible read-only pilots | **Hold after pilot execution** | executable P1/P2 evidence and rollback exist, but accepted read-effect, caller-authorization, and redaction canary-exit checks remain incomplete |
| G4 — Softwareco proposal | Hold | independent product convergence not established |
| G5 — core proposal | No-go | cross-company minimal implementation-neutral semantics not established |

The two named experiments completed their implementation/dogfood slices, but that is not a G3 pass. The accepted architecture ties canary exit to the applicable acceptance matrix. Command-intent evidence, source-subset checks, and explicit caveats do not substitute for unclosed read-effect, caller-authorization, or cross-owner redaction proof. Their labels, protocols, dimensions, and measurements remain local experimental evidence.

# G1A — ontology candidate disposition

## Observed mutation

The exact bytes formerly at:

```text
ontology/src/reference/concepts/core.AgentExperience.md
```

are preserved at:

```text
docs/project/rejected-candidates/core.AgentExperience.md.candidate
```

The archive SHA-256 remains:

```text
297441bf8dbdd14736183488742fcf4b5b36ce5036039bc4935744a3263bbe12
```

The archive directory explicitly states that candidates are not admitted semantics and that filesystem restoration is not ontology admission.

Owner commit:

```text
fb22aee3fc718d3875baec060886074b41c7e90a
```

## Retrieval dogfood

A Python 3.12, network-disabled container ran the complete owner gate successfully:

```bash
docker run --rm --network none \
  --user "$(id -u):$(id -g)" \
  -e HOME=/tmp/home -e TMPDIR=/tmp \
  -v "$PWD:/work" -w /work \
  ghcr.io/astral-sh/uv:python3.12-bookworm \
  bash scripts/ci/full.sh
```

Observed corpus:

- concepts: `31`;
- relations: `12`;
- source-contract documents: `43`;
- corpus digest: `sha256:2c3a7bc524f3178ac94b2b82aa080c83dd1c07b98a3e01203ab46e9038f8b8db`;
- `core.AgentExperience` absent from `ontology/dist/summary.json` and `id_index.json`;
- direct `pack core.AgentExperience` exits `2` as unknown;
- candidate archive remains byte-identical.

The host's Python 3.14 runtime cannot execute semantic discovery because that protocol intentionally requires Python 3.12/Unicode 15.0.0. The accepted container gate passed; host incompatibility was not reported as semantic or parser success.

Independent reviewer `dispatch-1785836911076`: **PASS**.

AK evidence: `6554` validation, `6555` dogfood, `6556` independent review. Task `4654` is done.

# G1B and G2 — `ts-quality` authority and vocabulary

Active product guidance now says:

- supported command-specific `--json` surfaces are structured JSON projections;
- supported command-specific `--machine` surfaces are versioned compact machine protocols;
- there is no general `--compact` flag;
- these are product-local interface descriptions;
- passive machine consumption is not agent-facing by definition;
- no accepted `core.AgentExperience` or bare `AX` concept is claimed.

Historical changelog, dated adoption, release, and projection records remain historical rather than being rewritten.

No repo ontology entry was added. This is the selected low-risk G2 path: retire the umbrella term from active contract language and retain explicit projection names.

Owner commit:

```text
8330a333cf2b03b8eb1c51b72ef7afbce6c9fda2
```

Validation:

- `node --test test/agent-interaction-retention-projection-pilot.test.mjs` — pass;
- `npm run verify` — pass;
- strict docs validation — pass;
- JSON parsing and `git diff --check` — pass.

Independent reviewer `dispatch-1785836911075` first returned **REVISE** because active docs implied an unsupported general `--compact` flag and the first subset check was circular. The implementation then removed the false flag description, independently parsed compact records, mapped them back to source leaves, and derived omissions/fallbacks. Re-review: **PASS**.

AK evidence: `6537` validation, `6539` dogfood, `6540` independent review. Task `4655` is done.

# P1 — `ts-quality` retention-plan projection

## Mapping

Source owner object:

```text
ArtifactRetentionPlan
```

Derived views from one in-process object:

1. full `structured_owner_plan`;
2. `TSQ_RETENTION_PLAN_V1` compact line protocol.

The pilot independently parses the compact protocol, compares every projected claim with the source model after the protocol's safe-text transform, computes exhaustive leaf omissions, records fallback derivations, compares against the existing owner renderer, and exposes `/structured_owner_plan` as expansion.

## Dogfood result

Fixture: `fixtures/minimal-external-adoption`.

- source plan SHA-256: `40ad922baa4bf9376face56fefa85fa1529d4c5f7563b162a6abe38b0617e223`;
- fixture tree before/after SHA-256: `b338b43c0a571f0ce27c7abbc6789b2c7b0a6f39cb7a25e62446fdd5a4e271a8`;
- source structured bytes: `1894`;
- compact protocol bytes: `1492`;
- reduction: `402` bytes;
- ratio: `0.7878`;
- keep entries: `9`;
- ignore entries: `6`;
- omissions: `/schemaVersion`, `/surface`;
- fallback derivations: none in the observed fixture;
- receipt SHA-256: `f2b58a9594035c02606de67bdaa557f706ebf6e75ecb40bb0ea394f81070bc51`.

Wrong-answer consequence checked: a compact retention view must not reclassify reusable, generated, ambient, coverage, witness-receipt, or private-key paths relative to the owner plan. Observed claim mapping passed. The retention plan remains advisory; repository policy and run artifacts retain authority.

# P2 — AK exact-generation task inspection

## Mapping

Source owner read:

```bash
ak task show <id> --machine
```

The sidecar invokes exactly one owner read, retains its complete structured envelope, and derives experimental `AK_TASK_COMPACT_PILOT_V1` text from the same task payload.

Preserved fields:

- source surface/schema;
- task id and `entity_version`;
- repo, title, lifecycle status, priority;
- claimant and lease;
- dependencies;
- exact current task scope, including distinction between `null` and explicit empty scope.

Unknown future scope properties fail closed. Omitted task fields are explicit and the receipt records both the exact source command and owner-default expansion.

## Dogfood result

Live subject: task `4656`, entity version `2` at read time.

- structured owner snapshot: `969` canonical JSON bytes;
- compact line-protocol payload: `633` bytes;
- line-protocol reduction: `336` bytes;
- ratio: `0.6533`;
- enclosing compact-projection evidence object: `1404` bytes;
- source snapshot SHA-256: `199a2d895e8c8114814ca10ba09268cd06b82a5c7fd32db32583326377692bec`;
- receipt SHA-256: `4325eec894d08ab9211f685ee84c0a462d4dbe943d085f6b0b18b107d084271c`.

The size claim applies only to consumer-facing line-protocol text. The evidence object and full receipt are intentionally larger.

## Falsification and correction

The first P2 implementation produced a descriptive JSON object of `1286` bytes from a `969`-byte source—a 32.71% expansion. Dogfood falsified its compactness claim.

After conversion to a compact protocol, independent review found four more defects:

1. read-only command selection was overstated as confirmed zero effects;
2. `null` scope and future scope fields were not represented safely;
3. text-size measurements were mislabeled as whole-projection measurements;
4. expansion hard-coded `ak` instead of preserving an alternate source executable.

All four were corrected. Final posture is `read_only_command_intent_effects_not_empirically_proven`.

Owner commit:

```text
846f3d6b1c77ad9611b440f1d6d90673c21f6be0
```

Validation:

- deterministic fake-AK single-read/negative-path check — pass;
- `./scripts/validate.sh --quiet-success fast` — pass;
- strict project-doc validation — pass;
- `git diff --check` — pass.

Independent reviewer `dispatch-1785836911075-1`: **PASS** after correction.

AK evidence: `6541` validation, `6542` dogfood, `6543` independent review. Task `4656` is done.

# AK close-check note

Tasks `4654`, `4655`, and `4656` are canonically `done`, but their advisory `close-check` views remain `ready_to_close=false`. Their completion results used structured field names instead of reproducing each done-contract outcome and validation sentence verbatim, so the current exact-string close-check does not recognize the otherwise recorded proof.

This is an advisory-result-shape gap, not silently claimed readiness. Evidence `6559`, `6560`, and `6561` explicitly records why the corresponding validation, dogfood, independent-review evidence, commits, and task results satisfy the factual contracts while the exact-string advisory remains false. Before task `4657` completes, it must record passing evidence with the exact `validation`, `dogfood`, and final `independent_review` classes, then place both contract outcome sentences and the independent-review validation sentence explicitly in its completion result so its own final close-check can become true.

# Cross-owner comparison

## Stable shared dimensions observed

Both pilots converged on these transport-neutral dimensions:

1. owner-native structured source remains present and authoritative within its declared ceiling;
2. compact output is derived, never separately authored as fact;
3. one source generation feeds each observed pair;
4. compact claims are checked against source claims;
5. omissions are explicit;
6. an expansion path returns to the owner view;
7. the pilot invokes only a read-oriented owner surface;
8. rollback removes the adapter without altering owner-native output.

These are observed common dimensions, not accepted controlled vocabulary or a universal envelope.

## Lawful owner-specific differences

| Dimension | P1 — `ts-quality` | P2 — AK |
|---|---|---|
| Owner fact kind | advisory artifact-retention plan | canonical task-state read |
| Freshness/generation | one in-process plan + source digest | task id + `entity_version` + machine-envelope read |
| Compact transport | existing public `TSQ_RETENTION_PLAN_V1` | experimental `AK_TASK_COMPACT_PILOT_V1` |
| Scope semantics | keep/ignore/warning entries | task allowed/required/forbidden scope |
| Omission risk | misclassifying commit/ignore posture | acting on stale/wrong task or missing scope/evidence |
| Effect claim | plan builder is read-oriented; tree unchanged in fixture | read-only command intent; zero effects not empirically claimed |
| Authority | advisory owner plan | AK active DB task truth via owner read |

The pilots therefore support a shared pattern, not one shared schema.

# Rollback dogfood

A disposable scratch archive removed every pilot-only file from both owner commits.

P1 rollback:

- rebuilt `ts-quality` without the pilot sidecar/test/note;
- ran owner `retention --machine` from current and rolled-back trees against the same target;
- outputs were byte-identical;
- owner output SHA-256: `770c17c702cbd855685bd668e98440f353e2a16654fe09e6165193d86b5ba163`.

P2 rollback:

- removed the P2 sidecar/check/note from a scratch archive;
- read task `4656` through the owner command from current and rolled-back working directories;
- canonical `.payload.task` values were byte-identical;
- owner task-payload SHA-256: `fc7f22e0b7b8dc58884e761fbc3c543a994cf4c4c36120e94d047bd6b245426b`.

Rollback receipt:

- local path: `$TMPDIR/agent-interaction-rollback-4657.json`;
- SHA-256: `ea946895678386a88108787efc8c9ce3debb599f1c7b438dba207c5f12243b48`;
- AK evidence: `6557` on task `4657`;
- runtime identity recorded in AK: Node `v26.1.0`, npm `11.14.1`, AK `0.1.0+git.0734099401717015399e0f6ce19ef4c182f0fd0a`, binary SHA-256 `7070fca9626d7f9bc3d58ca8ce075bccfe998820b87f39accae1d788bf65f876`;
- P2 rollback-time task generation: entity version `3`.

This proves pilot-file removal did not change the named owner reads in the observed snapshots. It does not prove public compatibility or authorize promotion.

# Remaining falsifiers and stop conditions

Broader reuse must stop or return to owner-local guidance if:

- another owner cannot map the shared dimensions without semantic coercion;
- compact output drops authority, freshness/generation, effect posture, scope, recovery, or evidence needed for its wrong-answer consequence;
- authorization or redaction differs between full and compact views;
- runtime identity cannot be bound strongly enough for the consequence level;
- mutation pilots cannot distinguish committed, partial, indeterminate, and confirmed-no-effect outcomes;
- adapters begin replacing owner-native reads or accumulating shadow authority;
- adoption comes from copied templates rather than independent owner need.

The read-only pilots did not close empirical no-authority-mutation proof for every owner read, caller-specific authorization, or cross-owner redaction conformance. They also did not exercise mutation settlement, retry/idempotency, or compensation. The first three keep G3 on hold; all remain blockers for any normative shared tool/event contract.

# Recommendation after dogfood

The next architecture question remains deliberately narrow:

> Should `core/engineering-core` own an advisory, transport-neutral Agent Interaction discipline/profile based on independently reviewed P1/P2 evidence?

This closeout does **not** answer yes. P1/P2 show enough convergence to make that future RFC question concrete, but G3 is not closed and the evidence is not enough to bypass owner review or accept a discipline now. Any such work requires completion or explicit accepted disposition of the G3 matrix plus a separately authorized engineering-core decision/task, and must retain the owner-specific differences above.

Vocabulary promotion remains a separate no-go until independent semantic use exists.

## Explicit nonclaims

This closeout does not:

- revive or accept `core.AgentExperience`;
- accept a repo or Softwareco successor concept;
- establish `AX` as canonical terminology;
- accept a society-wide interaction schema, protocol, service, registry, or authority layer;
- prove mutation safety, retry safety, settlement, authorization, or redaction parity;
- alter Decision 53 publication/adoption/activation facts;
- publish packages, push commits, or propagate templates.
