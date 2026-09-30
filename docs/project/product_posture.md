---
summary: "Evidence-bound ontology-kernel product posture after the published v0.3.0 release: the owner's core vocabulary and UFO category layer, two immutable Releases, and the first ADR-0008 consumer pinned."
read_when:
  - "When deciding where ontology-kernel stands relative to its durable vision."
  - "When selecting or reviewing a semantic, stewardship, release, or adoption maturity move."
  - "When checking whether release completion is being confused with product completion."
type: "reference"
as_of: "2026-09-30"
last_validated: "2026-09-30"
evidence_baseline_commit: "a6d38f56dd9b91e0a03b96444385402aecf1b9b0"
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
evidence_paths:
  - "README.md"
  - "RELEASING.md"
  - "docs/release-procedure.md"
  - "docs/project/vision.md"
  - "docs/project/2026-09-28-ontology-kernel-v0.3.0-change-note.md"
  - "docs/reference-model/governance-core.md"
  - "ontology/decisions/2026-09-27-governance-core-splits.md"
  - "ontology/decisions/2026-09-28-v0.3.0-pre-release-corrections.md"
  - "ontology/manifest.yaml"
  - "ontology/src/system4d.yaml"
  - ".github/workflows/validate.yml"
---

# Product Posture

> **Validation state:**
> - **Baseline:** exact commit `a6d38f56dd9b91e0a03b96444385402aecf1b9b0`, which is tag `v0.3.0`. Its ontology tree is `05ce7edb7a7b220d075206ca217df85e517e6a78`. ROCS reports 113 concepts, 12 relation types and 103 edges, and the corpus digest is `sha256:5dae5a62f0382fab72f39bda4e68b6f3fd1b5b5cd6a68e14a54b502ca0a1a5dd`.
> - **Release:** AK evidence 11546 records GitHub Release `399375883` reporting `immutable: true`, a verified signed release attestation, and no assets. Evidence 7484 still records the v0.2.0 Release.
> - **Adoption:** evidence 11548 records the FCOS layer pinned to v0.3.0 with passing checks.
> - **Authority:** these records remain their owners' authority; this document is a maturity projection. It changes no ontology source, tag, pin, activation, use or currentness fact.

## Posture in one sentence

`ontology-kernel` is a deterministic shared semantic kernel with two immutable, version-addressed GitHub Releases. v0.3.0 carries the Holding Owner's core vocabulary and a UFO category layer for the governance core, it was checked independently before release, and its first ADR-0008 consumer is pinned. It remains in active stewardship: most consumers still pin `@main`, System4D keeps known-stale entries, and the stewardship roles that would take over the core layer do not exist yet.

## Product maturity map

| Area | Current posture | Target posture | Main gap and proof of closure |
|---|---|---|---|
| Shared semantic kernel | 113 concepts, 12 relation types, 103 edges. v0.3.0 added 76 concepts: the authority, MITO structure, governance, commitment and check words (AK 6147), and `core.UfoCategory` with 12 categories (AK 5986). It deprecated five overloaded concepts with named successors (AK 5987). No released identifier was removed. | A small, stable cross-company meta-language that grows from demonstrated shared demand and the owner's Vorgabe route (ADR-0008). | Ten governance-core concepts still carry no category, and the non-blocking inspection findings are open (AK 6218). Closure needs owner decisions and a later version. |
| Source and validation contract | `ontology-markdown-v1`, profile `kernel-v1`, vendored ROCS 0.3.0; the workspace rocs-cli 0.4.5 also passes. GitHub Actions runs main-strict `full.sh` on every PR and on `main`. | Deterministic, offline-first validation with hosted corroboration. | The grammar request for a retired status, several successors and cross-layer mappings is AK 6087. Conformance stays a schema and reference claim, not proof that meaning is right. |
| Release identity | v0.2.0 (`76f31bc`) and v0.3.0 (`a6d38f5`) are immutable Releases at the one destination. The versioning rule ties a version to one `ontology/` tree, and `docs/release-procedure.md` with `scripts/release/` carries every release after v0.2.0. v0.1.0 and v0.2.1 are tags without Releases, and no tag ruleset exists. | Every version is an immutable Release bound to an exact OID, cut only when the ontology tree changes. | v0.2.1's tree equals v0.2.0's; it is recorded as the exception, and its consumers move to v0.3.0 (AK 6220). A `v*` tag ruleset is an owner setting that has not been made. |
| Consumer adoption | The FCOS layer pins v0.3.0 (evidence 11548). Two bounded v0.2.0 adoptions (evidence 7488) remain, and softwareco/ontology moved to v0.2.1. About 60 live manifests pin `@main`, including three company layers and two company copier templates. The L0 template and softwareco/copier default to v0.2.1. | Every consumer pins a protected release and records its own adoption. | AK 6220 moves the company layers and template defaults. Repo manifests follow through template propagation, not a kernel-owned mass repin. Consumers need rocs-cli ≥ 0.4.5. |
| System4D baseline | `ontology/src/system4d.yaml` is unchanged since v0.2.0. Its GitLab edge (`http://192.168.161.10:8929`) and GitLab contact are now known to be stale, because GitLab is retired (AK 6118). The file sits outside the admitted corpus. | A source-owner-reviewed boundary between shared guidance and operational overlays. | A change needs its own contract and a version. The v0.3.0 change note states the staleness as a nonclaim. |
| Direction and lifecycle | AK records SF1 as active stewardship, with route-wait task 5030 pending. The v0.3.0 content came through the owner's class-C route under ADR-0008 (AK 6147, 5986, 5987), and the release through AK 6167, outside any implementation wave. The NAS tasks 4852 and 4861 were closed as superseded. | Stewardship through bounded tasks or waves with truthful evidence. The ADR-0008 stewardship roles take over the core layer after the handover. | Whether this work reframes SF1 is AK-owned (5030). The stewardship roles are AK 5985. Until the handover the Holding Owner holds the core layer. |
| Local operator truth | The verified private-snapshot launcher is unchanged. Release dry runs need a read-only `gh` guard: a guardless dry run created an unauthorized draft on 2026-09-28, which was removed under the owner's authority (evidence 11307, 11332). The draft script tolerates Release-list lag on read-back. | Historical procedures cannot masquerade as current work, and dry runs cannot write. | A dry-run switch that stops before any POST or PATCH, whatever PATH holds, is idea R2 in AK 6218. |

## What is strong now

- The owner's controlled vocabulary lives in the kernel as retrievable concepts with preferred labels, mapped source synonyms and an `Admitted:` line. It is no longer only a hand-written card.
- The governance core states each concept's UFO category and required relata in a textual reference model.
- Meaning changes stay explicit. The five splits keep their old identifiers as deprecated tombstones with a decision note. The owner's pre-release corrections were recorded as a class-C decision before the first release.
- Content was checked by an independent work-product inspection (AK 6188), and the release procedure by two independent checks (AK 6191, 6199), before anything became immutable.
- Both Releases are immutable, attested and bound to exact OIDs. Hosted CI now corroborates every change.

## Current gaps and accepted limitations

1. **Most consumers still read `@main`.** Only FCOS pins v0.3.0. AK 6220 carries the company layers and template defaults.
2. **Categories and findings are open.** Ten governance-core concepts have no category, and the non-blocking inspection findings are listed in AK 6218.
3. **System4D is a mixed guidance artifact with known-stale GitLab entries.** They are not changed without a separate contract.
4. **Stewardship roles do not exist yet** (AK 5985). Every change to a core concept stays class C, with the Holding Owner as holder.
5. **Tooling follow-ups:** the ROCS drift checks and lookup (AK 5988), the vocabulary card generated from the kernel (AK 6088) and the grammar request (AK 6087) are outside this repository or still open.
6. **Conformance is deliberately bounded:** ROCS proves source-contract, schema and reference behaviour for named operations, not universal semantic correctness.

## Target product experience

1. A maintainer can decide quickly whether proposed meaning belongs in the kernel or an overlay, and whether it is a core word under ADR-0008, with stable-ID and deprecation consequences made explicit.
2. A reviewer can inspect the exact semantic delta (`rocs diff` plus deprecations) separately from guidance, tooling, release and authority changes.
3. A release owner can publish one immutable, version-addressed Release bound to an exact OID through the checked procedure. Each effect needs its own authority.
4. A consumer can pin, resolve, validate, summarize and pack a release from explicit inputs and record its own adoption.
5. An agent can retrieve only the concepts and relations its operation needs, with source, category, provenance and authority ceilings visible.

## Current stewardship dispositions

- **Future versions:** follow the versioning rule in `RELEASING.md` and `docs/release-procedure.md`. Changes outside `ontology/` get no version.
- **v0.2.0 and v0.3.0:** complete, and their procedures are not replayed. Every later release needs fresh owner authority and its own AK task.
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
