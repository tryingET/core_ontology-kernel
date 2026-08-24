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
evidence_paths:
  - "README.md"
  - "docs/project/vision.md"
  - "docs/ontology-schema.md"
  - "docs/adr/2026-08-03-ontology-markdown-rocs-contract-v1.md"
  - "docs/project/ontology-source-polaris-model.md"
  - "docs/project/ontology-source-identity-purpose-gate.md"
  - "docs/project/2026-08-23-ontology-kernel-release-readiness.md"
  - "docs/project/2026-08-23-ontology-kernel-v0.2.0-release-preparation.md"
  - "RELEASING.md"
  - "ontology/manifest.yaml"
  - "ontology/src/system4d.yaml"
---

# Product Posture

> **Validation state:** This posture was prepared against exact baseline commit
> `76f31bc5d42a77bc2c0fd24c8b30708f907fbd44`, which is also local tag `v0.2.0`.
> Its ontology source tree is `266409404a9570ab4bfe48002f91d1bdef0e5764`; ROCS summary reports
> 37 concepts and 12 relations, while exact-release gate evidence records 11 compiled edges. AK
> records `IW1` and `IW2` done. AK evidence `7484` records the published GitHub Release reporting
> `immutable: true`; evidence `7488` records three bounded consumer pins and acceptance gates. Those
> AK and consumer records remain their owners' authority; this document is a maturity projection.
> Adding this file and the vision changes no ontology source, release tag, consumer pin, activation,
> use, or currentness fact.

## Posture in one sentence

`ontology-kernel` is a released, deterministic, minimal shared semantic kernel with a published
GitHub Release reporting `immutable: true`, a protected `v0.2.0` tag bound to an exact OID, and
bounded validated consumer adoption; it is in stewardship rather than terminal completion, with
whole-holding adoption coverage, System4D baseline currentness, and the parent strategic-frame
disposition still requiring explicit owner evidence or decision.

## Product maturity map

| Area | Current posture | Target posture | Main gap and proof of closure |
|---|---|---|---|
| Shared semantic kernel | Exact-release gate evidence records 37 concepts, 12 relations, and 11 compiled edges. `v0.2.0` added evidence, authority, and planning vocabulary without removing released IDs or edges. | A small, stable cross-company meta-language that grows only from demonstrated shared demand. | No finite kernel proves conceptual completeness. Closure for any new gap requires a named consumer operation, owner review, compatible semantic delta, and exact-corpus validation. |
| Source and validation contract | The repository opts into `ontology-markdown-v1`, profile `kernel-v1`, and an exact vendored ROCS materialization. The strict gate admits the corpus without a sibling checkout. | Deterministic, offline-first authoring and validation with typed failures, stable IDs, explicit deprecation, bounded summaries, and reproducible packs. | Existing proof is operation-qualified conformance, not generic semantic correctness. Future contract/tool changes must preserve that ceiling and pass exact-OID owner gates. |
| Release identity | AK evidence `7484` records GitHub Release `v0.2.0` at sole destination `tryingET/core_ontology-kernel`, Release ID `375502095`, server response `immutable: true`, protected lightweight tag at exact OID `76f31bc5…`, signed attestation, and no assets. | One unambiguous destination and forward-only publication whose semantic delta, exact OID, content, tag protection, server immutability state, and attestation are independently verifiable. | The successful `v0.2.0` procedure does not pre-authorize later releases. Each release needs fresh owner authority, exact-OID gates, setting/readback evidence, and consumer handoff. |
| Consumer adoption | AK evidence `7488` records protected `v0.2.0` pins and acceptance gates for the bounded Softwareco infra, fork, and ontology consumers. AK tasks `4959`–`4964` and `4973` separately record convergence of current Copier defaults and parent baselines. | Every declared consumer resolves a protected release through an explicit path, passes its owner gate, and records its own adoption. | No complete whole-holding consumer inventory, activation census, or use/currentness proof exists. Closure requires an owner-defined inventory and consumer-owned receipts; template defaults alone are not adoption. |
| System4D baseline | `ontology/src/system4d.yaml` defines the shared baseline boundaries, constraints, invariants, lifecycle, risks, and debt. It also retains baseline version `0.1`, an environment-specific self-hosted GitLab edge, a GitLab owner handle, and explicit debt that not all repos enforce policies. | A source-owner-reviewed baseline whose shared facts are current, whose environment-specific facts live at the correct layer, and whose lifecycle/version relationship is explicit. | The `v0.2.0` release did not establish or record those entries as current. Closure requires a separate semantic-owner review and, if needed, a versioned ontology change—not an editorial posture rewrite. |
| Direction and lifecycle | AK-native `SF1` remains active while child waves `IW1` and `IW2` are done and no ready repo task is present. Task `4852` remains pending, actively deferred, and linked as a historical branch-parity anchor; its scope predates the owner decision excluding NAS from `v0.2.0`. | Product posture, AK direction, and live tasks tell the same bounded story without treating a completed release as terminal product completion. | The owner disposition of `SF1` and task `4852` remains unresolved. This document neither selects execution, cancellation, supersession, nor archival. |

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

1. **Fleet scope is bounded.** The three adoptions recorded in AK evidence `7488` and protected
   template defaults do not establish whole-holding adoption, activation, use, or currentness.
2. **System4D currentness is not established.** Environment-specific GitLab, owner, baseline-version,
   and rollout-debt entries survived unchanged into `v0.2.0`; semantic-owner adjudication is still
   required before treating them as current shared facts.
3. **Direction closure is undecided.** Completed work waves prove their accepted outcomes, not
   automatic closure of active `SF1` or cancellation of linked historical tasks.
4. **Conformance is deliberately bounded.** ROCS proves admitted source-contract, schema, and
   reference behavior for named operations; it does not prove universal semantic correctness.
5. **Representation remains supersedable.** No accepted evidence selects a permanent universal
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

## Open maturity questions

These questions identify product-level uncertainty; they are not an executable sequence, queue, or
lifecycle authorization:

- Does the semantic owner affirm the currentness and layer placement of the environment-specific
  entries in `ontology/src/system4d.yaml`, or is a separately versioned ontology change warranted?
- Should active `SF1` remain the durable stewardship frame now that `IW1` and `IW2` are done, or does
  the accountable owner intend a different AK lifecycle disposition?
- Does pending, deferred task `4852` still represent desired branch-parity work after NAS was
  excluded from `v0.2.0`, and what owner action—if any—should reconcile its historical scope?
- Is whole-holding adoption a desired claim? If so, which owner-defined consumer inventory and
  consumer receipts would be sufficient rather than inferring adoption from template defaults?

Until owners answer those questions, new semantic work remains demand-led: add or deprecate meaning
only for named cross-domain operations, and authorize every future release independently.

## Hard rules for status language

- Say **released** only for the exact published Release, protected tag/OID, and verified artifacts.
- Say **adopted** only for a consumer whose owner recorded a pin and passing acceptance evidence.
- Say **current** or **used** only when the relevant owner surface supplies fresh evidence.
- Say **conformant** only with the exact ROCS operation, profile, corpus, and evidence boundary.
- Do not translate `IW1`/`IW2` completion into product completion or `SF1` closure.
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
