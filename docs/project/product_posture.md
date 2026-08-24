---
summary: "Evidence-bound ontology-kernel product posture after the published v0.2.0 release and bounded consumer convergence."
read_when:
  - "When deciding where ontology-kernel stands relative to its durable vision."
  - "When selecting or reviewing a semantic, stewardship, release, or adoption maturity move."
  - "When checking whether release completion is being confused with product completion."
type: "reference"
as_of: "2026-08-24"
last_validated: "2026-08-24"
evidence_baseline_commit: "76f31bc5d42a77bc2c0fd24c8b30708f907fbd44"
evidence_ids:
  - "7471"
  - "7484"
  - "7488"
  - "7603"
  - "7632"
  - "7633"
  - "7634"
  - "7635"
evidence_paths:
  - "README.md"
  - "docs/project/vision.md"
  - "docs/project/2026-08-24-ontology-kernel-stewardship-greats-adjudication.md"
  - "docs/ontology-schema.md"
  - "docs/adr/2026-08-03-ontology-markdown-rocs-contract-v1.md"
  - "docs/project/ontology-source-polaris-model.md"
  - "docs/project/ontology-source-identity-purpose-gate.md"
  - "docs/project/2026-08-23-ontology-kernel-release-readiness.md"
  - "docs/project/2026-08-23-ontology-kernel-v0.2.0-release-preparation.md"
  - "RELEASING.md"
  - "ontology/manifest.yaml"
  - "ontology/src/system4d.yaml"
  - "scripts/rocs.sh"
  - "scripts/verify_vendored_rocs.py"
---

# Product Posture

> **Validation state:** This posture was prepared against exact baseline commit
> `76f31bc5d42a77bc2c0fd24c8b30708f907fbd44`, which is also local tag `v0.2.0`.
> Its ontology source tree is `266409404a9570ab4bfe48002f91d1bdef0e5764`; ROCS summary reports
> 37 concepts and 12 relations, while exact-release gate evidence records 11 compiled edges. AK
> records `IW1` and `IW2` done while `IW3` remains active at explicit close-or-continue gate
> task `5010`; completed implementation outcomes and lifecycle closure remain distinct. `SF1`
> remains active stewardship. AK evidence `7484` records the published GitHub Release reporting
> `immutable: true`; evidence `7488` records three
> bounded consumer pins and acceptance gates. Task `4852` remains blocked by dependency `4861` and
> active deferral `241`; evidence `7632` records a scope-currentness audit and recommended resume
> checks but does not install a new task guardrail. Those records remain their owners' authority;
> this document is a maturity projection. This posture changes no ontology source, release tag,
> consumer pin, activation, use, or currentness fact.

## Posture in one sentence

`ontology-kernel` is a released, deterministic, minimal shared semantic kernel with a published
GitHub Release reporting `immutable: true`, a protected `v0.2.0` tag bound to an exact OID, and
exactly bounded validated consumer adoption; it is in active stewardship rather than terminal
completion, with System4D uncertainty explicitly bounded, historical NAS scope currently blocked by
its AK dependency and deferral, and the normal local ROCS path repaired without changing ontology
meaning.

## Product maturity map

| Area | Current posture | Target posture | Main gap and proof of closure |
|---|---|---|---|
| Shared semantic kernel | Exact-release gate evidence records 37 concepts, 12 relations, and 11 compiled edges. `v0.2.0` added evidence, authority, and planning vocabulary without removing released IDs or edges. | A small, stable cross-company meta-language that grows only from demonstrated shared demand. | No finite kernel proves conceptual completeness. Closure for any new gap requires a named consumer operation, owner review, compatible semantic delta, and exact-corpus validation. |
| Source and validation contract | The repository opts into `ontology-markdown-v1`, profile `kernel-v1`, and an exact vendored ROCS materialization. The strict gate admits the corpus without a sibling checkout. | Deterministic, offline-first authoring and validation with typed failures, stable IDs, explicit deprecation, bounded summaries, and reproducible packs. | Existing proof is operation-qualified conformance, not generic semantic correctness. Future contract/tool changes must preserve that ceiling and pass exact-OID owner gates. |
| Release identity | AK evidence `7484` records GitHub Release `v0.2.0` at sole destination `tryingET/core_ontology-kernel`, Release ID `375502095`, server response `immutable: true`, protected lightweight tag at exact OID `76f31bc5…`, signed attestation, and no assets. | One unambiguous destination and forward-only publication whose semantic delta, exact OID, content, tag protection, server immutability state, and attestation are independently verifiable. | The successful `v0.2.0` procedure does not pre-authorize later releases. Each release needs fresh owner authority, exact-OID gates, setting/readback evidence, and consumer handoff. |
| Consumer adoption | AK evidence `7488` records protected `v0.2.0` pins and acceptance gates for the bounded Softwareco infra, fork, and ontology consumers. Evidence `7635` records 64 declaration lines but explicitly classifies them as inventory—not adoption, activation, use, currentness, or live-repo status. | Every consumer that chooses the kernel resolves a protected release through an explicit path, passes its owner gate, and records its own adoption. | Whole-holding adoption is not a current product claim or provider-owned migration target. A future fleet claim requires an owner-defined registry and consumer receipts; template defaults and manifest declarations alone are not adoption. |
| System4D baseline | `ontology/src/system4d.yaml` defines shared baseline guidance but also retains baseline version `0.1`, an environment-specific GitLab edge and owner handle, rollout state, workflow particulars, and enforcement debt. The file is outside the admitted concept/relation corpus. | A source-owner-reviewed boundary that separates durable shared guidance from operational overlays without treating either as currentness or authority. | Reviewed IW3 analysis recommends keeping the bytes unchanged and treating environment-specific entries as unproved currentness. Any split, deletion, owner/endpoint update, or version change requires a separate semantic-owner contract and consumer-impact review; this posture does not authorize it. |
| Direction and lifecycle | AK-native `SF1` remains the active stewardship frame. `IW1` and `IW2` are done. Accepted implementation outcomes from tasks `4996`–`4998` have landed, but `IW3` remains active at close-or-continue gate task `5010`: closeout status has missing domain rows, and generic proceed authorizes neither closure nor invented owner facts. Task `4852` remains pending with dependency `4861` and active deferral `241`. Evidence `7632` records that fresh owner intent, secure reachable transport, and current-ref scope should precede any resume; it did not re-scope the task. | Durable stewardship uses finite waves only for real work, closes them through truthful evidence and explicit lifecycle choice, and permits quiet SF-level discovery between waves. | `IW3` is not done until closeout readiness, an explicit close selection, and a lawful apply receipt exist. `SF1` lifecycle remains separate and AK-owned. General NAS replication intent remains an owner question; task execution is blocked by the recorded dependency and deferral. |
| Local operator truth | The checked-in wrapper verifies the exact vendored ROCS bundle before import, copies opened bytes into a private snapshot, executes only that snapshot, and suppresses bytecode. CI shares the verifier, reports classified drift, and passes in the normal checkout after verified ignored-bytecode cleanup. Completed `v0.2.0` release guidance is explicitly non-replayable. | Git-clean and bundle-clean states are distinguishable, the standard local path stays bytecode-free, and historical mutation procedures cannot masquerade as current work. | Accidental direct imports outside the wrapper can still create cache files; strict equality intentionally fails and names the cleanup boundary rather than ignoring executable ambient bytes. |

## What is strong now

- The public semantic surface is small enough to inspect and retrieve in bounded packs.
- IDs, lifecycle fields, references, source grammar, and conformance ceilings are explicit.
- The validator path is deterministic and self-contained for the released kernel corpus.
- Semantic content, exact bytes, projections, provenance, release, adoption, and authority are kept
  separate rather than collapsed into Git or generated-artifact status.
- The published Release, protected tag, and bounded consumer pins establish a reproducible adoption
  path for the consumers actually tested.
- The frozen v2 source-format experiment selected no winner; current Markdown remains an operational
  frontend. Normalized authored-form identity was not needed for the reviewed bounded consumer and
  therefore was not implemented.

## Current gaps and accepted limitations

1. **Fleet scope is deliberately bounded.** The three adoptions recorded in AK evidence `7488` and
   protected template defaults do not establish whole-holding adoption, activation, use, or
   currentness. Existing mutable declarations are consumer-owner candidates, not a kernel-owned
   migration queue.
2. **System4D remains a mixed guidance artifact.** Environment-specific endpoint, owner,
   baseline-version, rollout, and workflow entries are not established as current. The reviewed IW3
   recommendation is containment and explicit nonclaim, not an unreviewed semantic rewrite.
3. **NAS parity intent is unresolved and currently blocked.** Task `4852` remains pending behind
   dependency `4861` and active deferral `241`. Evidence `7632` records recommended current-scope
   checks; it is not itself an enforcing re-scope or prohibition.
4. **IW3 closure is deliberately gated.** Tasks `4996`–`4998` have accepted outcomes, but AK closeout
   readiness still reports missing domain rows and requires an explicit close-or-continue choice.
   Task `5010` holds that route; neither generic proceed nor a documentation claim can close the wave.
5. **Conformance is deliberately bounded.** ROCS proves admitted source-contract, schema, and
   reference behavior for named operations; it does not prove universal semantic correctness.
6. **Representation remains supersedable.** No accepted evidence selects a permanent universal
   source format or a semantic-editing diagram tool.

## Target product experience

1. A maintainer can decide quickly whether proposed meaning belongs in the shared kernel or an
   overlay, with stable-ID and deprecation consequences made explicit.
2. A reviewer can inspect the exact semantic delta separately from guidance, tooling, release, and
   authority changes.
3. A release owner can publish one protected, version-addressed GitHub Release bound to an exact
   OID and hand consumers an OID-bound contract without relying on remote aliases or mutable branches.
4. A consumer can pin, resolve, validate, summarize, and pack the release from explicit inputs and
   record adoption through its own authority surface.
5. An agent can retrieve only the concepts and relations needed for its operation, with source,
   projection loss, provenance, and authority ceilings visible.

## Current stewardship dispositions

The reviewed [Many-of-the-Greats analysis](2026-08-24-ontology-kernel-stewardship-greats-adjudication.md)
uses contextual dominance to explain—not replace—the current owner surfaces:

- System4D bytes are unchanged. Environment-specific currentness remains unproved; any migration
  requires a separate semantic-owner contract and consumer-impact review.
- AK records `SF1` as active stewardship, `IW1` and `IW2` done, and `IW3` active at close-or-continue
  gate task `5010`. The wave's accepted outcomes do not substitute for closeout readiness, explicit
  operator choice, or a lifecycle apply receipt. `SF1` closure remains a separate AK-owned question.
- Task `4852` remains pending behind dependency `4861` and deferral `241`. Evidence `7632` records
  recommended owner, transport, and current-scope checks but installs no new task guardrail.
- Adoption claims remain exactly bounded to consumer-owner receipts. Evidence `7635` is a declaration
  inventory, not authority for a provider-owned mass migration.
- Evidence `7633` records exact vendored-bundle equality plus a deterministic private-snapshot
  operator path; permissive cache admission was rejected.
- Every future semantic release remains separately authorized exact-OID work; the completed
  `v0.2.0` commands are historical and non-replayable.

New semantic work remains demand-led: add or deprecate meaning only for named cross-domain
operations, and authorize every future release independently.

## Hard rules for status language

- Say **released** only for the exact published Release, protected tag/OID, and verified artifacts.
- Say **adopted** only for a consumer whose owner recorded a pin and passing acceptance evidence.
- Say **current** or **used** only when the relevant owner surface supplies fresh evidence.
- Say **conformant** only with the exact ROCS operation, profile, corpus, and evidence boundary.
- Do not translate completion of any finite implementation wave into product completion or `SF1` closure.
- Do not use this file as a roadmap, queue, task mirror, release log, or semantic authority.

## Authority and freshness

- Durable product direction: `docs/project/vision.md`
- Product maturity bridge: this file
- Authored semantic and System4D source: `ontology/src/`, under ontology owner review
- Source grammar and conformance ceiling: `docs/ontology-schema.md` and Decision 110 ADR
- Compiled/generated projections: `ontology/dist/`; reproducible evidence, not authored authority
- ROCS implementation and package lifecycle: `core/rocs-cli`
- Release procedure and exact release evidence: `RELEASING.md`, GitHub Release state, and AK evidence
- Live tasks, direction, decisions, and execution evidence: Agent Kernel
- Consumer adoption, activation, use, and currentness: each consumer's owner surface

Refresh this document when a semantic release, source-contract boundary, System4D adjudication,
material consumer-adoption boundary, or AK strategic-frame posture changes. A passing gate or one
completed task is not sufficient reason to rewrite product maturity.
