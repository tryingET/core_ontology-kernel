---
summary: "Grand architecture review of Agent Experience across 10,000-, 5,000-, 2,000-, and 1,000-foot views."
read_when:
  - "When designing agent-facing interfaces, machine/compact projections, or recovery contracts"
  - "When deciding whether Agent Experience terminology belongs locally, in Softwareco, or in the core ontology"
  - "When correcting the current core.AgentExperience authority drift"
type: "architecture-review"
review_status: "complete"
architecture_disposition: "revise_before_adr"
---

# Agent Experience — grand architecture review

- AK task: `4651`
- Prior dogfood: AK task `4648`
- Prior semantic review: AK task `4649`
- Candidate: `ontology/src/reference/concepts/core.AgentExperience.md`
- Candidate SHA-256: `297441bf8dbdd14736183488742fcf4b5b36ce5036039bc4935744a3263bbe12`
- Review method: three non-overlapping lenses under Prompt Vault procedure `review-rfc-multi`
- System4D mode: full

## Overall verdict

**Reject the current core-concept direction. Revise the cross-system architecture before any ADR. Proceed with owner-local corrective work.**

The need is real: agents need interfaces that make action discovery, input, outcome, failure, recovery, evidence, freshness, and authority legible. The architectural mistake is treating that need as one new holding-wide ontology noun or one central “AX” runtime.

The target is an **owner-local agent-interaction membrane** implemented by existing owners through their existing CLI, SDK, RPC, Pi-tool, and artifact contracts. “Agent Experience” may remain a local product phrase while its denotation stabilizes. It is not currently a core semantic fact, company ontology fact, engineering-core discipline, or runtime authority layer.

Immediate posture:

- **GO:** correct false authority claims and isolate the rejected candidate from ordinary local core retrieval after explicit owner disposition.
- **GO:** preserve and improve the proven product pattern—durable artifact plus structured and compact projections—without requiring shared vocabulary.
- **HOLD:** repo-ontology insertion until a real local retrieval/validation need exists.
- **NO-GO:** Softwareco/core promotion, bare `AX` propagation, central AX service, template rollout, or Decision 53 claims.

## System4D summary

### Container — boundary

In scope:

- interactions through which an autonomous or semi-autonomous `core.Agent` discovers actions, supplies inputs, interprets outcomes/errors, and decides whether to continue, retry, recover, or escalate;
- the owner contracts and projections that make those interactions deterministic, bounded, authority-aware, and context-efficient;
- vocabulary placement from product-local language through possible company/core promotion.

Out of scope:

- generic machine readability for passive ETL, dashboards, CI, or reporting;
- choosing JSON, Markdown, line protocols, or any other source/transport format as canonical;
- creating a new central agent-facing authority service;
- semantic publication, adoption, activation, currentness, or Decision 53 facts;
- changing the candidate during this review.

### Compass — primary driver

Agents should not need to reverse-engineer prose, ambient state, hidden authority, or ambiguous failure to act safely. Before and after an operation, an agent should be able to answer:

1. Who owns this capability and fact?
2. Which exact resource generation and contract am I using?
3. Is this canonical fact, receipt, projection, advice, or empirical observation?
4. What may the operation change, and what authorization is required?
5. Was execution merely accepted, or were effects durably settled?
6. Is retry safe, forbidden, or dependent on readback/reconciliation?
7. Which evidence proves the result?
8. What was omitted to fit the consumer/context budget?

### Engine — target mechanism

```text
owner capability + owner fact
          |
          v
DISCOVER -> READ/PLAN -> PREFLIGHT -> AUTHORIZE
          -> EXECUTE -> SETTLE -> READ BACK/RECONCILE
          -> RECEIPT -> PROJECT -> OBSERVE
                       |       |
                       |       +-> empirical analysis (DSPx/Oracle)
                       +-> structured machine / compact agent / human views
```

This is a shared contract pattern, not a shared service or shared database.

### Fog — uncertainties and debt

- No independent evidence yet shows that multiple repos mean the same thing by Agent Experience.
- The term may be better as a quality attribute or engineering discipline than an ontology concept.
- No accepted cross-owner metric set exists for agent-interface quality.
- Bare `AX` collides with accessibility terminology.
- `ts-quality` projects nonexistent core authority.
- The rejected untracked candidate currently enters default worktree corpus resolution and ignored local compiled outputs.
- Current owner interfaces have uneven freshness, correlation, settlement, retry, and omission semantics.
- The controlled-vocabulary lifecycle remains proposed rather than accepted policy.

# 10,000-foot view — society architecture

## Architectural thesis

Agent Experience is **not another layer in the AI Society stack**. It is a cross-cutting quality concern spanning existing layers:

| Existing layer | Contribution to agent interaction | Must not absorb |
|---|---|---|
| ROCS / ontology owners | controlled meaning and semantic validation | task state, execution effects, empirical judgments |
| AK / `society.v2.db` | canonical task, decision, evidence, lifecycle, and lineage facts | product semantics, Pi runtime, ontology meaning |
| Pi / ASC | execution host, session lifecycle, cancellation, effect settlement, operator visibility | canonical society authority |
| Pi orchestrator | routing, sequencing, escalation, synthesis | lower-plane owner truth |
| Product repos | concrete commands, artifacts, projection contracts, compatibility | society-wide ontology by assertion |
| Engineering-core | reusable cross-language design disciplines and advisory invariants | controlled society vocabulary or execution proof |
| Prompt Vault | reusable transition procedures | runtime task/decision/semantic authority |
| DSPx / Oracle | empirical patterns over receipts and traces | normative permission or semantic promotion |
| Steward/workbench surfaces | human explanation, review, navigation, continuity | canonical state by convenience |

The existing convergence architecture already supplies the required macro-shape:

```text
Authoring / semantic / product sources
                 |
                 v
     owner validation and runtime
                 |
        durable facts + receipts
                 |
        +--------+---------+
        |                  |
 AK operational lineage   product/semantic authority remains with owner
        |                  |
        +--------+---------+
                 v
         Pi execution/coordination
                 |
       machine / compact / human projections
                 |
          empirical observation
```

No “AX platform” belongs between these owners. A central wrapper would become a shadow authority, hide owner-specific failure semantics, and create a second compatibility surface.

## Current-state contradiction

The present workspace demonstrates why the owner split matters:

- the candidate is untracked and core admission was rejected;
- clean committed acceptance contains 31 concepts, 12 relations, and 43 v1 documents;
- the current dirty worktree contains the candidate, so ROCS correctly admits 32 concepts and 44 documents for that exact filesystem corpus;
- ignored `ontology/dist/summary.json` and `id_index.json` therefore expose `core.AgentExperience` locally;
- the build receipt correctly marks that build `authoritative: false` with `authority_mode: local_only`;
- ordinary summary/index consumers do not carry that warning beside each ID;
- `ts-quality/docs/public-contract.md` already cites `core.AgentExperience` as shared authority.

This is not a ROCS parser defect: v1 admits the exact current source directory, independent of Git tracking. It is a **candidate-intake and operator-projection architecture gap**. Candidate files placed in active source roots become part of worktree semantics before governance has accepted them.

## 10,000-foot target state

1. **Authority remains plural and explicit.** Each concern retains its owner; AK binds operational lineage rather than absorbing all facts.
2. **Agent interaction is a quality membrane, not an authority membrane.** It exposes owner truth without replacing it.
3. **Candidate semantics remain outside active source roots.** Review artifacts and isolated review worktrees are used until owner admission.
4. **All projections identify their authority posture.** Local/non-authoritative/candidate state cannot be lost between receipt and summary.
5. **Correction precedes promotion.** False authority references are repaired before any new vocabulary proposal.
6. **Empirical evidence informs but never promotes.** DSPx/Oracle may reveal usability patterns; owners make decisions through AK-governed lifecycle.

# 5,000-foot view — semantic and ownership architecture

## Separate the kinds

The draft collapses six architectural kinds:

| Kind | Architectural meaning | Correct role here |
|---|---|---|
| Agent | autonomous/semi-autonomous actor | existing `core.Agent` |
| Agent-facing interface | boundary used by an agent action loop | product/Pi/API contract |
| Interaction quality | clarity, parsability, provenance, recoverability, efficiency, safety | quality attribute |
| Agent-interface design | practices used to improve that quality | possible engineering discipline |
| Projection/adapter | JSON, RPC, line protocol, compact packet, TUI view | replaceable implementation |
| Controlled concept | stable shared semantic category | possible only after denotation and use converge |

A non-authoritative architecture statement is:

> An agent-facing interface is a boundary used by a `core.Agent` action loop. Agent-interface quality describes how safely and effectively that loop can discover, invoke, interpret, and recover. Agent-interface design is the discipline used to improve the quality. Machine and compact projections are implementations of the boundary.

This framing is deliberately not an ontology definition.

## Why the current candidate fails

1. **Unstable kind:** it calls the term a design category but treats artifacts, protocols, feedback loops, and individual packets as members.
2. **Wrong agent boundary:** passive parsers, dashboards, and CI consumers are included even when no autonomous/semi-autonomous action loop exists.
3. **Quality versus membership confusion:** verbose JSON is poor interaction design, not a non-member of an interface category.
4. **Implementation leakage:** JSON/compact preferences, token advice, CLI flags, and evidence-packet practice enter the normative definition.
5. **Authority leakage:** durable-artifact placement is prescribed as core semantics even though fact ownership varies by system.
6. **Naming collision:** bare `AX` already denotes accessibility technology in engineering guidance.
7. **Insufficient convergence:** exact current use is concentrated in one `ts-quality` product/documentation wave.

## Placement ladder

### Now: product-local descriptive language

`ts-quality` may keep a full phrase as explicitly local terminology if useful, but it must remove the false core claim. It need not create a repo ontology concept merely to preserve an acronym or document two projection modes.

### Later: repo-local concept, only if earned

A repo ontology entry is justified only when controlled retrieval, validation, or cross-artifact consistency needs a stable local identifier. The successor must choose one kind, anchor to real agent loops, remove bare `AX`, and exclude product implementation policy.

### Later still: Softwareco overlay

A revised `co.software.*` concept becomes plausible after independently maintained Softwareco repos demonstrate the same denotation—not merely copied terminology, templates, or similar JSON flags.

### Holding core: exceptional end state

Core review is warranted only if the concept remains minimal and implementation-neutral across company boundaries. Numeric adoption thresholds in this review are proposed gates, not accepted policy.

## Stable core versus adapter boundary

Stable semantics should describe identifying conditions and relations. Adapters own representation, transport, context budgets, and product compatibility. Therefore:

- do not add JSON, compactness, command names, token budgets, or evidence-storage rules to core;
- do not infer ontology membership from transport shape;
- do not invent `serves`/`designed_for` merely to connect one candidate;
- prefer `relations: []` to a false edge;
- let product and Pi owners version concrete projection contracts;
- promote a discipline to engineering-core only after recurring cross-repo failures and reusable validation exist.

# Decision decomposition and owner assignment

The architecture is not one decision.

1. **Corrective decisions now:** `core/ontology-kernel` owns candidate disposition and clean retrieval; `ts-quality` owns correction of its product terminology. These need bounded owner-local tasks, not a cross-system ADR.
2. **Pilot decision next:** each named pilot owner may authorize a reversible, read-only experimental mapping over its own interfaces. No shared authority or compatibility promise follows.
3. **Candidate shared-discipline decision later:** after two independent pilots, the exact RFC question is: **Should `core/engineering-core` own an advisory, transport-neutral Agent Interaction discipline/profile?** Engineering-core would own reusable design and validation invariants only; owner packages would retain schemas, effect semantics, compatibility, and execution proof.
4. **Possible normative tool-contract decision later still:** if advisory guidance cannot prevent cross-owner wrong answers, a separate decision must assign a component owner for a society-wide tool/event contract profile. The current workspace-root `RFC-tool-contracts-SocietyS3.md` is a draft layer anchor, not by itself a stable component owner. This decision is blocked until that owner and concrete interoperability need are explicit.
5. **Vocabulary decision remains separate:** repo, Softwareco, or core ontology promotion cannot ride inside the interaction-contract RFC.

The current review is therefore decision-grade as a **revise-before-ADR disposition**, not as an ADR-ready shared contract.

# 2,000-foot view — interaction and contract architecture

## Owner-local interaction membrane

Each owner should expose three logically related surfaces through its native transport:

### 1. Capability passport

- owner and stable operation identifier;
- supported contract versions;
- read/plan/write and effect classes;
- authority prerequisites;
- projection modes;
- schema/help locator;
- limits, omissions, and support maturity.

### 2. Interaction result

- exact resource and invocation identity;
- outcome and owner-native error code;
- accepted versus settled state;
- effect certainty;
- retry/readback/recovery posture;
- evidence reference.

### 3. Evidence receipt

- exact operation and attempt;
- declared and observed effects;
- pre/post resource coordinates;
- validations and artifacts;
- omissions/redactions;
- unresolved or indeterminate state.

These are logical slots, not a mandatory universal JSON schema. Owners may use CLI envelopes, files, RPC, SDK objects, Pi events, or DB records.

## Minimum interaction contract

Every material operation should convey, directly or through joined owner-native artifacts:

1. owner and stable operation identifier;
2. contract/schema version and locator;
3. runtime/package identity where relevant;
4. owner-native resource identity;
5. snapshot, generation, digest, or `as_of` freshness coordinate;
6. logical request/operation identity, attempt identity, and any owner-declared idempotency/replay key;
7. artifact role: source fact, projection, receipt, advice, empirical observation, or candidate artifact;
8. owning authority and exact source coordinate;
9. authority claim and scope: what the artifact is canonical or non-authoritative for;
10. admission/lifecycle state: for example candidate, admitted, deprecated, or unknown;
11. distribution/locality scope: local, repo, company, holding, or owner-native equivalent;
12. declared effect class;
13. effect certainty: `confirmed_no_effects`, `committed`, `partial`, `indeterminate`, or unknown;
14. stable outcome/error and failure phase;
15. retry/readback/reconciliation instruction;
16. evidence/receipt references and integrity joins;
17. truncation, omission, and expansion path;
18. authorization and redaction posture.

Artifact role, owning authority, admission, locality, and provenance are orthogonal dimensions; they must not be collapsed into one enum. The labels above are architecture dimensions, not accepted controlled vocabulary. Each pilot must define an owner-native mapping and the legal combinations it supports.

## Projection architecture

```text
                 exact owner snapshot
                         |
           +-------------+-------------+
           |             |             |
     machine view    compact view    human view
  deterministic/full bounded subset explanatory
           |             |             |
           +-------------+-------------+
                         |
                 same identity joins
```

Rules:

- owner fact remains canonical;
- all views bind the same resource generation;
- compact claims are a subset of machine/owner claims;
- omission is explicit, countable, and expandable;
- compact views prioritize owner, resource, status, blocker, effect posture, one next action, and evidence reference;
- large payloads remain behind explicit expansion/artifact references;
- machine output is versioned and deterministic, not prose-scraped;
- ambient cwd, “latest,” session, or default DB does not silently select mutation targets;
- representation format is not semantic identity;
- receipts prove provenance/execution only within their declared ceiling.

## Failure and retry architecture

| Effect certainty | Agent behavior |
|---|---|
| `confirmed_no_effects` | retry may be permitted with the same logical request and a new attempt identity |
| `committed` | do not re-execute blindly; read back canonical state. An idempotent replay may return the prior result only when the owner contract defines key scope, retention, duplicate-response, and conflict semantics |
| `partial` | owner reconciliation or compensation required; reversibility is not assumed |
| `indeterminate` / unknown | never retry blindly; read back or escalate |

A boolean `retryable` is insufficient. Logical request, operation, attempt, and idempotency identities are distinct. Transport success, command acceptance, subprocess exit, Pi tool completion, owner settlement, and evidence attachment are different facts. External effects may lack one atomic commit boundary; owners must declare settlement, compensability, and reconciliation rather than imply exactly-once execution.

## Context-budget architecture

Token efficiency is valuable but subordinate to safety:

- compact output should remove repetition before removing state;
- include exactly one bounded next action when one is legal;
- preserve effect/freshness/authority/evidence fields even in compact form;
- use explicit `no_packet_needed`, abstention, unknown, and omitted states;
- carry references instead of embedding sensitive or large evidence;
- never claim compact equivalence without tests against the machine/owner view.

## Testable acceptance matrix

The pattern is ready for broader reuse only after each pilot preregisters a semantic mapping profile: material operations/effect classes, acceptable freshness coordinates, resource-generation equality, request/operation/attempt joins, field-level claim comparison, omission/expansion rules, authorization, redaction, and owner-declared idempotency/settlement guarantees.

Owner-local tests must then prove:

1. advertised capabilities map to supported owner contracts;
2. read/plan paths perform no undeclared authority mutation;
3. machine and compact views bind the same generation under the preregistered owner mapping;
4. compact claims are a mechanically checked subset of owner/machine claims, with omitted fields accounted for;
5. changed preconditions fail stale/conflict rather than executing silently;
6. failure injection across every declared settlement boundary yields the correct effect certainty;
7. indeterminate effects cannot be mechanically retried;
8. owner-declared idempotent replay returns the prior result or a defined conflict without duplicating effects; non-idempotent operations reject replay;
9. receipts bind resource, logical request, attempt, effects, validation, and artifacts with verified join integrity;
10. projections expose truncation/omission and an authorized expansion path;
11. authorization-classification tests prove compact/human views reveal no more than the caller-authorized machine view;
12. redaction tests prevent prompt/path/stderr/secret leakage and preserve redaction monotonicity across projections;
13. empirical export cannot mutate or impersonate normative authority.

Passing local tests proves only that owner's mapping. Cross-owner conformance requires fixture-level agreement on the shared dimensions and explicit documentation of lawful owner-specific differences.

# 1,000-foot view — concrete disposition and rollout

## Current facts

- `core.AgentExperience` remains untracked and uncommitted.
- Its semantic review concluded `revise_and_route`; core admission is not approved.
- AK evidence records exist for dogfood (`6501`, `6502`) and semantic review (`6507`, `6508`).
- `ts-quality` active docs claim nonexistent core authority.
- Bare `AX` is ambiguous.
- Local ignored compiled output includes the candidate because it is present in the active source directory.
- Clean committed CI and no-sibling acceptance exclude it.

## Options

| Option | Assessment |
|---|---|
| A. Commit current candidate to core | Reject |
| B. Insert current/revised concept into Softwareco now | Premature |
| C. Correct authority drift, then optionally incubate full phrase locally | Recommended |
| D. Retire umbrella term and use explicit projection names | Valid low-risk fallback |
| E. Build a central AX gateway/runtime | Reject |
| F. Extract an engineering-core discipline immediately | Hold until recurring evidence and validation exist |

## Owner-local sequence

### Phase 0 — freeze

- no new `core.AgentExperience` references;
- no bare `AX` propagation;
- no company/core/engineering/Pi/template promotion;
- no interpretation of ROCS retrieval as semantic approval.

### Phase 1A — restore core candidate/retrieval separation

Owner: `core/ontology-kernel`.

1. Confirm candidate checksum and provenance.
2. Obtain explicit owner disposition for the untracked file.
3. Preserve it outside active source resolution, delete it, or move it to an explicitly reviewed owner artifact—never by convenience.
4. Clean/regenerate ignored compiled output from the committed corpus.
5. Prove ordinary summary/query/pack exposes 31 concepts, 12 relations, 43 documents, and no `core.AgentExperience`.
6. Keep the committed semantic and architecture reviews as review evidence.

**Gate G1A:** active core retrieval is truthful and the candidate's disposition is explicit.

### Phase 1B — correct `ts-quality` authority drift

Owner: `softwareco/owned/ts-quality`.

1. Remove the claim that `core.AgentExperience` is accepted shared semantics.
2. Use explicit projection names or label the full phrase as local/incubating.
3. Remove or locally qualify bare `AX`.
4. Preserve changelog/release history as history.
5. Do not bundle command behavior changes.
6. Run repo-owned docs and contract validation.

**Gate G1B:** active guidance claims no nonexistent core authority.

Phases 1A and 1B are separate owner-local tasks and may execute independently.

### Phase 2 — local vocabulary decision

Owner: `ts-quality`.

Choose either:

- retire the umbrella term; or
- incubate it as descriptive product language.

Create a repo ontology concept only if a concrete retrieval/validation need survives review. Use the revision contract from `core-AgentExperience-semantic-review.md`.

**Gate G2:** owner review accepts one kind, boundary, name, and actual local need.

### Phase 3 — named reversible interaction-pattern pilots

Pilot the owner-local interaction membrane—not the ontology term—through two read-only, owner-authorized experiments:

1. **P1 — `ts-quality` retention-plan projection:** derive an experimental structured view and compact view from the same owner-produced retention plan. Wrong-answer consequence: an agent commits ephemeral/sensitive output or omits required reusable evidence. Owner: `ts-quality`.
2. **P2 — AK task inspection projection:** derive an experimental compact view from the same task/entity version as AK's owner JSON/machine read. Wrong-answer consequence: an agent acts on the wrong task, stale lifecycle state, wrong scope, or missing evidence. Owner: `agent-kernel`.

Pilot ceiling:

- no write operation, owner API replacement, accepted compatibility promise, template propagation, or vocabulary promotion;
- prototypes are sidecars/adapters over exact owner outputs and preserve owner identifiers;
- existing output remains unchanged;
- each run records runtime identity, fixtures, claim mapping, omission set, context cost, wrong-answer checks, and task evidence.

Compatibility and rollback:

- prototype profiles carry explicit experimental versions and negotiate no unsupported version;
- canary entry requires owner-approved fixtures and non-production subjects;
- canary exit requires the acceptance matrix, independent review, and no authority/freshness/effect regression;
- downgrade means removing the sidecar/profile while retaining owner-native output;
- receipts from a withdrawn profile remain historical experiment evidence and do not establish current conformance;
- any consumer that cannot fall back to owner-native output blocks the pilot.

Measure correct projection selection, freshness/authority recognition, recovery/evidence closure, context cost, omission failures, and false confidence. Mutation settlement remains a later owner-specific experiment after read-only semantics converge.

**Gate G3:** both named pilots produce executable fixtures, AK task evidence, stable shared dimensions, documented owner-specific differences, and successful rollback.

### Phase 4 — learning and empirical closure

- KES may crystallize the proven anti-pattern: consumer docs must not project candidate ontology IDs as shared authority, and dirty local builds must not be mistaken for committed semantics.
- DSPx/Oracle may analyze repeated failures, objections, retries, context loss, and recovery patterns.
- Neither KES nor Oracle promotes vocabulary or activates policy.

### Phase 5 — optional Softwareco proposal

Owner: `softwareco/ontology`.

A company proposal is warranted only after independently maintained Softwareco products converge on one denotation. Review must separate the semantic concept from the interaction-membrane engineering pattern.

**Gate G4:** accepted company decision, migration, validation, rollback, and owner-local canary.

### Phase 6 — exceptional core proposal

Owner: `core/ontology-kernel`.

Only if cross-company use converges on minimal, implementation-neutral semantics should a new RFC enter review. It would concern a revised successor, not the rejected candidate.

**Gate G5:** decision lifecycle closes through review synthesis, ADR, versioned release, consumer canary, and rollback proof.

### Phase 7 — propagation last

Order:

1. source product pilot;
2. independent canary;
3. company ontology if accepted;
4. engineering-core only for reusable discipline;
5. Pi-specific guidance through Pi owners;
6. templates last.

Never propagate from an untracked candidate, dirty compiled bundle, review memo, or proposed lifecycle RFC.

## Rollback and stop conditions

Stop and return to local language if:

- two adopters mean different things;
- passive machine consumption remains conflated with agent action loops;
- bare `AX` ambiguity persists;
- the term adds no retrieval/validation value;
- compact views omit authority, effect, freshness, or recovery information;
- adapters become a shadow authority service;
- tests cannot distinguish committed, partial, and indeterminate effects;
- promotion depends on copied/template-generated usage rather than independent adoption.

Rollback is owner-local:

- product terminology can return to explicit projection names;
- repo/company ontology can deprecate a successor with migration guidance;
- projection adapters can be versioned or removed without changing source authority;
- a core release, if one ever exists, requires forward-compatible deprecation or a reviewed repin—never silent history rewrite.

# Three-lens architecture review

## Lens 1 — core architecture and semantics

**Strengths**

- The stack already separates semantics, runtime, execution, product, guidance, and empirical analysis.
- Core/company/repo ontology layering supports incubation without premature promotion.
- The semantic review already rejects the incoherent current candidate.

**Risks**

- active-source candidate leakage into local compiled retrieval;
- reverse promotion from consumer docs into claimed core authority;
- concept/discipline/quality/interface collapse.

**Must fix**

- restore candidate/admitted corpus separation;
- correct the consumer's false core reference;
- retain stable-core versus adapter boundary.

**Evidence quality:** high for current state and owner boundaries; insufficient for shared vocabulary promotion.

## Lens 2 — runtime interface and projection architecture

**Strengths**

- AK machine reads, ROCS contracts, ASC settlement, Pi transports, and `ts-quality` artifact/projection discipline provide proven ingredients.

**Risks**

- fragmented correlation and mutation settlement;
- compact-output omission;
- ambient selection and stale resource execution;
- adapter centralization into shadow authority.

**Must fix before shared architecture**

- define owner-local capability/result/receipt slots;
- prove freshness, effect certainty, retry, omission, and evidence joins;
- pilot through existing owner transports.

**Evidence quality:** medium-high for existing primitives; insufficient for a universal normalized envelope or central service.

## Lens 3 — governance, rollout, and adoption

**Strengths**

- AK tasks/evidence, owner-local repos, decision lifecycle, KES, and Oracle have explicit distinct roles.
- The current error is reversible without changing runtime behavior.

**Risks**

- review guidance mistaken for accepted promotion policy;
- historical occurrences mistaken for independent adoption;
- templates spreading an ungoverned term;
- cross-repo cleanup absorbing unrelated dirty changes.

**Must fix**

- execute corrections as separate owner-local tasks;
- require explicit candidate disposition;
- attach evidence through AK;
- treat proposed adoption thresholds as proposals until accepted.

**Evidence quality:** high for corrective work; low for company/core promotion.

# Cross-cutting contradictions

1. **Candidate versus corpus:** untracked does not mean excluded; filesystem admission and governance admission are different.
2. **Retrieval versus authority:** successful discovery/pack proves operational retrieval, not accepted meaning.
3. **Structured versus agent:** machine-readable does not imply agent-facing.
4. **Compact versus complete:** token efficiency can improve usability while increasing omission risk.
5. **Shared pattern versus shared noun:** multiple systems may need the same interaction invariants without needing one ontology concept or one envelope.
6. **Local evidence versus broad promotion:** one product wave can validate a local pattern but not holding-wide semantics.
7. **Current versus target:** the stack has strong fragments, but no accepted society-wide interaction-membrane contract.

# Must fix before an ADR

- Keep the exact candidate shared decision narrow: whether `core/engineering-core` should own an advisory Agent Interaction discipline/profile after P1/P2 evidence.
- Keep any future normative society tool/event contract behind a separate owner-assignment and interoperability decision.
- Complete named P1/P2 pilots with explicit wrong-answer consequences and experimental authority ceilings.
- Freeze the shared semantic dimensions while explicitly allowing owner-native representation and mappings.
- Define freshness, artifact role, owning authority, admission/locality, effect certainty, identity joins, evidence, omission, authorization, and redaction semantics.
- Define idempotency, replay, settlement, compensation, and reconciliation without assuming exactly-once effects.
- Keep vocabulary promotion in a separate owner decision.
- Provide compatibility, canary, downgrade, receipt-retention, and consumer rollback behavior.
- Demonstrate executable conformance rather than static confidence.

# Final recommendation

**Request another architecture/RFC revision round for any shared contract. Reject the current core ontology direction. Approve bounded owner-local corrections now.**

Why:

1. the stack needs a reusable interaction pattern, not another authority layer;
2. current vocabulary evidence is local and semantically unstable;
3. existing systems already contain most required contract primitives;
4. the immediate authority drift and candidate-retrieval gap are independently correctable;
5. pilots should prove the shared contract before ontology, engineering-core, Pi, or template propagation.

## Explicit nonclaims

This review does not:

- accept or modify `core.AgentExperience`;
- accept `co.software.AgentExperience` or a repo-local successor;
- create a new AX service, runtime, schema, registry, or authority layer;
- change the ontology source format;
- alter Decision 53 facts;
- approve an engineering-core discipline;
- mutate `ts-quality`, Softwareco ontology, Pi, Prompt Vault, KES, or DSPx;
- prove field adoption from dogfood, term counts, or local generated output;
- accept a society-wide interaction contract;
- authorize P1/P2 pilot execution or template adoption;
- prove that current owner interfaces already satisfy the proposed dimensions.
