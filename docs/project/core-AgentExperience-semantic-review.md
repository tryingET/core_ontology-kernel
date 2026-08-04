---
summary: "Ontology-owner semantic review of the untracked core.AgentExperience candidate; outcome revise and route, not core admission."
read_when:
  - "When deciding whether Agent Experience belongs in the holding-wide core ontology"
  - "When using or revising AX terminology in a Softwareco repository"
type: "review"
---

# `core.AgentExperience` semantic review

- AK task: `4649`
- Candidate: `ontology/src/reference/concepts/core.AgentExperience.md`
- Candidate SHA-256: `297441bf8dbdd14736183488742fcf4b5b36ce5036039bc4935744a3263bbe12`
- Review outcome: **revise and route**
- Core admission: **not approved**

## Controlling conclusion

Do not commit the candidate as `core.AgentExperience` in its current form. The term identifies a potentially useful concern, but the candidate does not yet fit the kernel's declared holding-shared, minimal, stable, and slow-changing scope. Independent adoption is this review's recommended evidence gate, not an already codified kernel admission rule.

The current text conflates three different things:

1. the interaction quality of surfaces used by an autonomous or semi-autonomous `core.Agent`;
2. generic machine-readable output for passive parsers, CI, and dashboards;
3. implementation guidance about JSON, compact projections, token budgets, authority artifacts, and specific CLI shapes.

Those concerns can interact, but they are not one stable identifying condition for a core concept.

This review recommends incubation in the owning Softwareco surface rather than promotion into the holding-wide kernel. The placement reviewer recommended the Softwareco company overlay immediately. The controlling synthesis instead selects repo-local `ts-quality` incubation as the narrowest current owner because exact normative use was found only there; this is an explicit conservative override, not an established placement rule. A later Softwareco ontology-owner review may promote a revised concept to `co.software.AgentExperience` if broader Softwareco use becomes real. This review recommends broader cross-company evidence before any future `core.AgentExperience` proposal.

This review does not accept, adopt, publish, activate, or make current any ontology term.

## Evidence considered

### Core scope and existing semantics

- The kernel is the holding-wide shared ontology and should change slowly: `README.md`.
- Core concepts must remain minimal and stable; domain concepts belong in overlays: `ontology/src/reference/concepts/README.md`.
- `core.Agent` means an autonomous or semi-autonomous software actor and is a subtype of `core.Actor`.
- Passive artifacts are not actors under `core.Actor`.
- CI/CD workflows already have the distinct `core.Pipeline` concept.
- No existing core UX, DX, Experience, Projection, or Interface concept was found.

### Dogfood evidence

AK task `4648` exercised vendored ROCS 0.3.0 with Python 3.12 without modifying the candidate:

- query `agent experience` on the worktree returned `multiple_candidates`: `core.AgentExperience` first and `core.Agent` second;
- query `AX` uniquely retrieved `core.AgentExperience` in the worktree and returned no candidate in the committed corpus;
- digest-bound pack accepted `core.AgentExperience` as input in the observed worktree snapshot.

These observations establish retrieval behavior only. They do not establish semantic correctness or owner approval.

### Actual term use and placement

Exact tracked occurrences of “Agent Experience” were found in four `softwareco/owned/ts-quality` documentation files: current README/public-contract guidance plus changelog/release history. `ts-quality/docs/public-contract.md` currently says that `core.AgentExperience` is the shared term even though the candidate is not committed or accepted. That statement is a premature projection, not ontology authority.

No independent exact use was found in the inspected Pi extension or pi-mono documentation. The candidate's preserved mtime immediately precedes the first `ts-quality` terminology commit; that chronology is evidence consistent with one product wave, not proof of independent semantic convergence or original file creation time.

A bare `AX` abbreviation also collides with accessibility terminology: engineering-core accessibility guidance uses `UIA/AX/AT-SPI`, where AX denotes an accessibility platform/API family.

Softwareco already has a company ontology overlay at `softwareco/ontology`, whose declared purpose is to extend core with company-domain concepts. The `ts-quality` repository also has a repo-local ontology layer and explicitly says concepts should begin locally when they are not yet broadly shared.

## Semantic blockers

### 1. Unstable ontological kind

The candidate calls Agent Experience a “design category” covering interfaces, artifacts, protocols, and feedback loops. Its examples then treat individual output artifacts and packets as instances. These are different category boundaries.

The verbose-JSON anti-example is also still an agent-facing artifact under the candidate's own definition; it is a poor implementation, not a non-member. Anti-examples must distinguish category membership rather than quality.

### 2. “Agent” includes passive consumers

Parsers, dashboards, and CI systems are not necessarily autonomous or semi-autonomous actors. Machine readability alone does not make a surface part of Agent Experience under the existing `core.Agent` meaning.

Deterministic adapters and model-oriented projections may share one interaction boundary only when they mediate how an actual agent receives state, discovers or invokes actions, interprets results, or recovers from failure.

### 3. Normative definition contains implementation policy

The definition and examples prescribe durable-artifact placement, JSON versus compact projections, token economy, named command shapes, and evidence-closure packets. These belong to engineering/process or product-owner guidance, not to a minimal identifying definition in the core ontology.

Pi owns Pi-specific operator-workbench behavior. Engineering-core may own reusable cross-language design discipline. Product repositories own their concrete CLI projection contracts.

### 4. Abbreviation and evidence are not stable enough

`AX` is duplicated as a label/synonym and is ambiguous with accessibility usage. Exact adoption is currently concentrated in one Softwareco product family, with no cross-company convergence.

## Non-blocking relation assessment

`relations: []` is acceptable for review and is not a semantic blocker. `AgentExperience is_a Agent` would be false because an experience or design discipline is not an actor. `part_of`, `uses`, and `instance_of` would also misstate the relationship. A new `serves` or `designed_for` relation must not be invented merely to connect this candidate.

An empty relation list is preferable to a false edge. It neither resolves nor worsens the separate boundary and placement blockers.

## Review-recommended revision contract before any broader proposal

A successor proposal should:

1. choose one ontological kind, such as the interaction quality or design discipline of surfaces serving a `core.Agent` action loop;
2. anchor “agent” to `core.Agent`, treating parsers/adapters as in scope only when they participate in that agent interaction;
3. make passive reporting, ETL, dashboard, and non-agent machine consumption explicit non-members;
4. remove JSON/compact preferences, named flags, token advice, and authority-storage rules from the normative definition;
5. use examples that are actual instances and anti-examples that are genuine non-members;
6. remove bare `AX` unless an owner resolves the accessibility collision and demonstrates stable qualified usage;
7. leave relations empty unless a separately reviewed relation expresses the intended semantics truthfully;
8. under this review's recommended gate, demonstrate independent active use beyond one product wave before promotion from repo-local to company or holding scope.

A possible direction—not an accepted definition—is:

> Agent Experience is the interaction quality of system surfaces through which an autonomous or semi-autonomous software agent discovers actions, supplies inputs, interprets results and errors, and determines whether to continue, retry, recover, or escalate.

Representation format is not definitional.

## Source-owner routing

| Concern | Owning surface |
|---|---|
| Current terminology and CLI projection behavior | `softwareco/owned/ts-quality` |
| Provisional semantic incubation | `ts-quality` repo ontology |
| Possible multi-repo Softwareco promotion | `softwareco/ontology` after company-owner review |
| Reusable engineering guidance | `core/engineering-core` |
| Pi-specific workbench/runtime guidance | Pi / pi-extensions owner surfaces |
| Holding-wide semantic promotion | `core/ontology-kernel` after ontology-owner approval and this review's recommended cross-company evidence |

The false `core.AgentExperience` reference in `ts-quality/docs/public-contract.md` should be corrected only through a separately scoped task in that owner repository. This review does not authorize that mutation.

## Review synthesis

Independent ontology-semantic review returned **REVISE**: the concept may fill a gap, but its kind, agent boundary, examples, and normative guidance must change.

Independent placement review returned **REJECT/ROUTE** for the core location and recommended immediate placement in the Softwareco company overlay, with engineering/Pi guidance separated, `AX` resolved, and broader evidence required before core promotion.

The controlling synthesis accepts the rejection of core placement but conservatively overrides immediate company-overlay placement: exact normative use is currently concentrated in `ts-quality`, whose repo ontology explicitly supports local incubation before broader promotion.

Controlling synthesis: **revise and route to repo-local incubation; do not admit to core**.
