---
summary: "Evidence-bound ontology-kernel product posture after immutable v0.5.0: the holding's shared meaning moved into core, exact release checks, and consumer adoption routed to its owners."
read_when:
  - "When deciding where ontology-kernel stands relative to its durable vision."
  - "When selecting or reviewing a semantic, stewardship, release, or adoption maturity move."
  - "When checking whether release completion is being confused with product completion."
type: "reference"
as_of: "2026-10-10"
last_validated: "2026-10-10"
evidence_baseline_commit: "60790d43ba0f4cfea946df9b07865b877432a7dd"
evidence_ids:
  - "7484"
  - "7488"
  - "11274"
  - "11275"
  - "11307"
  - "11332"
  - "11336"
  - "11417"
  - "11418"
  - "11440"
  - "11441"
  - "11545"
  - "11546"
  - "11548"
  - "11549"
  - "12507"
  - "12766"
  - "12852"
  - "12853"
  - "12859"
  - "12860"
  - "13029"
  - "13099"
  - "14974"
  - "14985"
  - "14986"
  - "14990"
  - "14993"
  - "14995"
evidence_paths:
  - "README.md"
  - "RELEASING.md"
  - "docs/release-procedure.md"
  - "docs/project/vision.md"
  - "docs/project/2026-09-28-ontology-kernel-v0.3.0-change-note.md"
  - "docs/project/2026-10-03-ontology-kernel-v0.4.0-change-note.md"
  - "docs/project/2026-10-04-ontology-kernel-v0.5.0-change-note.md"
  - "docs/reference-model/governance-core.md"
  - "ontology/decisions/2026-09-27-governance-core-splits.md"
  - "ontology/decisions/2026-09-28-v0.3.0-pre-release-corrections.md"
  - "ontology/decisions/2026-10-02-decision-records-questions.md"
  - "ontology/decisions/2026-10-03-holding-meaning-to-core.md"
  - "ontology/manifest.yaml"
  - "ontology/src/system4d.yaml"
  - ".github/workflows/validate.yml"
---

# Product Posture

> **Validation state:**
> - **Release commit:** `60790d43ba0f4cfea946df9b07865b877432a7dd`, protected tag `v0.5.0`, ontology tree `80e050c0de548aef3519e8a11ddf9aaf65eaf920`. Exact-commit checks in a fresh clone (14974) report 126 concepts, 13 relation types and 137 edges; full CI, strict docs and strict ROCS validation pass; corpus digest `sha256:fcd758d0988f178d1d29cbe45912563d8b638698df81cde3947e17e3f5482b04`.
> - **Release:** evidence 14995 records Release `409031456`, published `2026-10-10T15:27:30Z`, `immutable: true`, tag `v0.5.0` on the release OID, `gh release verify` passing, no assets. The owner authorized version, OID and draft (14985) and, separately, publication of the numeric draft (14993); 14986 records the immutability setting read. Earlier receipts: v0.2.0 7484, v0.3.0 11546, v0.4.0 12853.
> - **Adoption:** consumers that pin `<repo:core/ontology-kernel@main>` already read v0.5.0's content; pinned consumers repin through standing AK 6288, carried for v0.5.0 by AK 6936 (template default, company refreshes, FCOS, teachingco). Agent Kernel's first-consumer route (6453) is unchanged by this refresh.
> - **Authority:** these records remain their owners' authority; this document is a maturity projection. It changes no ontology source, tag, pin, activation, use or currentness fact.

This refresh covers the v0.5.0 semantic release and its checks. Other stewardship and overlay observations retain their cited receipt dates; no new consumer census or strategic-frame disposition is claimed.

## Posture in one sentence

`ontology-kernel` is a deterministic shared semantic kernel with four immutable, version-addressed GitHub Releases. v0.5.0 moves the meaning the holding sets for every company (template topology, work-item authority split) from the holdingco company layer into core and rewords four consent concepts in S3 v2026 terms. Its exact commit passes native and consumer checks; consumer adoption now follows the first-consumer route and standing owner decision 6288. Release completion does not establish consumer adoption, resolve the System4D limitations or hand over stewardship.

## Product maturity map

| Area | Current posture | Target posture | Main gap and proof of closure |
|---|---|---|---|
| Shared semantic kernel | 126 concepts, 13 relation types, 137 edges. v0.5.0 adds 2 concepts and 5 edges against v0.4.0 and rewords four concepts, with no removals (owner's Core Vorgabe route, AK 6592; ADR-0008 §1 item 7). v0.4.0 added 11 concepts, one relation type and 29 edges against v0.3.0. Content and the closed consent round are authorized under AK 6364; the change note carries the exact delta and decision note. The five v0.3.0 deprecations retain their identifiers and successors. | A small, stable cross-company meta-language that grows from demonstrated shared demand and the owner's Vorgabe route (ADR-0008). | The v0.3.0 category and inspection findings (AK 6218) need their own owner dispositions; the v0.4.0 release does not establish their closure. |
| Source and validation contract | `ontology-markdown-v1`, profile `kernel-v1`, vendored and consumer ROCS 0.4.6. Exact-commit native strict CI, consumer schema/reference checks and strict docs pass. CI now checks routing with a growing corpus without changing native discovery's 12-candidate cap (AK 6448). GitHub Actions corroborates every PR and `main`. | Deterministic, offline-first validation with hosted corroboration. | The grammar request for a retired status, several successors and cross-layer mappings is AK 6087. Conformance stays a schema and reference claim, not proof that meaning is right. |
| Release identity | v0.2.0 (`76f31bc`), v0.3.0 (`a6d38f5`), v0.4.0 (`763d70a`) and v0.5.0 (`60790d4`) are immutable Releases at the sole destination. The versioning rule ties a version to one `ontology/` tree; the reviewed procedure separates draft creation from numeric-ID publication authorization. v0.1.0 and v0.2.1 remain tags without Releases. | Every version is an immutable Release bound to an exact OID, cut only when the ontology tree changes. | v0.2.1's tree equals v0.2.0's and remains the recorded exception. Repository rulesets were absent at the publication checks; tag protection for v0.4.0 comes from the immutable Release. |
| Consumer adoption | Agent Kernel's candidate-layer check passes, with canonical files unchanged. Its canonical pin and ONTOLOGY constant checks belong to first-consumer task 6453. Earlier consumer adoption receipts retain their own dates; this release provides no fresh census of current pins. | Every consumer pins a protected release and records its own adoption. | After the first consumer, standing AK 6288 sends template defaults, company refreshes and eligible repo-layer repins through template-propagator and each target's checks. Failing or uncommittable targets get owner-bound AK tasks. |
| System4D baseline | `ontology/src/system4d.yaml` is unchanged since v0.2.0. Its GitLab edge (`http://192.168.161.10:8929`) and GitLab contact are now known to be stale, because GitLab is retired (AK 6118). The file sits outside the admitted corpus. | A source-owner-reviewed boundary between shared guidance and operational overlays. | A change needs its own contract and a version. The v0.3.0 change note states the staleness as a nonclaim. |
| Direction and lifecycle | The 2026-09-30 posture recorded SF1 as active stewardship and task 5030 as pending. Current direction is read from AK. v0.4.0 content came through the owner's ADR-0008 route under AK 6364, with release task 6538. Neither receipt closes or reframes SF1. | Stewardship through bounded tasks or waves with truthful evidence. The ADR-0008 stewardship roles take over the core layer after the handover. | Strategic-frame disposition and the stewardship handover remain AK-owned (5030, 5985). Until a recorded handover, the Holding Owner holds the core layer. |
| Local operator truth | The verified private-snapshot launcher is unchanged. Release dry runs need a read-only `gh` guard: a guardless dry run created an unauthorized draft on 2026-09-28, which was removed under the owner's authority (evidence 11307, 11332). The draft script tolerates Release-list lag on read-back. | Historical procedures cannot masquerade as current work, and dry runs cannot write. | A dry-run switch that stops before any POST or PATCH, whatever PATH holds, is idea R2 in AK 6218. |

## What is strong now

- The owner's controlled vocabulary lives in the kernel as retrievable concepts with preferred labels, mapped source synonyms and an `Admitted:` line. It is no longer only a hand-written card.
- The governance core states each concept's UFO category and required relata in a textual reference model.
- Meaning changes stay explicit. The five splits keep their old identifiers as deprecated tombstones with a decision note. The owner's pre-release corrections were recorded as a class-C decision before the first release.
- Content was checked by an independent work-product inspection (AK 6188), and the release procedure by two independent checks (AK 6191, 6199), before anything became immutable.
- All four Releases are immutable, attested and bound to exact OIDs. Hosted CI corroborates every change.
- v0.4.0 preserves the authorized corpus through the consent round, CI correction, draft and publication; native and consumer checks cover the exact release commit.
- v0.5.0 shows the release path recovering from a moved `main`: when PR #17 landed after the first candidate, a change-note PR produced a new candidate, the owner re-authorized that exact OID, and the draft script's main-equals-OID check held. Hold a content freeze from the prep merge to publication.

## Current gaps and accepted limitations

1. **Canonical v0.4.0 adoption needs consumer-owner receipts.** Candidate conformance is not an adoption receipt. Agent Kernel is the named first consumer; standing AK 6288 governs the later pin propagation.
2. **Category and inspection disposition is separate.** The v0.3.0 inspection identified ten uncategorized governance-core concepts and non-blocking findings (AK 6218). This refresh does not re-audit or close that work.
3. **System4D is a mixed guidance artifact with known-stale GitLab entries.** They are not changed without a separate contract.
4. **Stewardship handover needs its own authority** (AK 5985). The v0.4.0 receipts grant no handover; the Holding Owner's class-C route remains the release's content authority.
5. **Tooling follow-ups retain their source owners:** ROCS drift checks and lookup (AK 5988), the generated vocabulary card (AK 6088) and the grammar request (AK 6087). This release is not their completion evidence.
6. **Conformance is deliberately bounded:** ROCS proves source-contract, schema and reference behaviour for named operations, not universal semantic correctness.

## Target product experience

1. A maintainer can decide quickly whether proposed meaning belongs in the kernel or an overlay, and whether it is a core word under ADR-0008, with stable-ID and deprecation consequences made explicit.
2. A reviewer can inspect the exact semantic delta (`rocs diff` plus deprecations) separately from guidance, tooling, release and authority changes.
3. A release owner can publish one immutable, version-addressed Release bound to an exact OID through the checked procedure. Each effect needs its own authority.
4. A consumer can pin, resolve, validate, summarize and pack a release from explicit inputs and record its own adoption.
5. An agent can retrieve only the concepts and relations its operation needs, with source, category, provenance and authority ceilings visible.

## Current stewardship dispositions

- **Future versions:** follow the versioning rule in `RELEASING.md` and `docs/release-procedure.md`. Changes outside `ontology/` get no version.
- **v0.2.0, v0.3.0, v0.4.0 and v0.5.0:** published and verified; their effects are not replayed. Every later release needs fresh owner authority and its own AK task.
- **The 2026-08-24 stewardship adjudication** still holds for fail-closed ROCS execution, archival fidelity, System4D bytes and bounded adoption claims. Its premise of quiet, demand-led growth was overtaken by the owner's ADR-0008 route. Its NAS question was closed by GitLab's retirement.
- **Adoption claims** stay exactly bounded to consumer-owner receipts.

## Hard rules for status language

- Say **released** only for the exact published Release, protected tag/OID, and verified artifacts.
- Say **adopted** only for a consumer whose owner recorded a pin and passing acceptance evidence.
- Say **current** or **used** only when the relevant owner surface supplies fresh evidence.
- Say **conformant** only with the exact ROCS operation, profile, corpus, and evidence boundary.
- Do not translate completion of any finite task or wave into product completion or `SF1` closure.
- Do not use this file as a roadmap, queue, task mirror, release log, or semantic authority.

## Authority and freshness

- Durable product direction: `docs/project/vision.md`
- Product maturity bridge: this file
- Authored semantic and System4D source: `ontology/src/`, held by the Holding Owner until the ADR-0008 handover
- Core word list, holders and reserved identifiers: governance-kernel `docs/dev/decisions/0008-vocabulary-loop.data.yaml`
- Source grammar and conformance ceiling: `docs/ontology-schema.md` and Decision 110 ADR
- Compiled/generated projections: `ontology/dist/`; reproducible evidence, not authored authority
- ROCS implementation and package lifecycle: `core/rocs-cli`
- Release procedure and exact release evidence: `RELEASING.md`, `docs/release-procedure.md`, GitHub Release state, and AK evidence
- Live tasks, direction, decisions, and execution evidence: Agent Kernel
- Consumer adoption, activation, use, and currentness: each consumer's owner surface

Refresh this document when a semantic release, source-contract boundary, System4D adjudication,
material consumer-adoption boundary, or AK strategic-frame posture changes. A passing check or one
completed task is not sufficient reason to rewrite product maturity.
