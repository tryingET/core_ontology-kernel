---
summary: "Decision note for the ontology questions from AK's decision records (AK 6364, 2026-10-02): possible objection and concern, when dissent exists, decision as an intention created by a deliberation, refusal and revocation, the decision class as a high-order type over three class roles, when a permission ends, and the in-place readings of core.Objection, core.ConsentRound, core.Dissent, core.Permission and core.DecisionRecord."
read_when:
  - "When a record, schema or layer uses core.Objection, core.PossibleObjection, core.Concern, core.Dissent, core.Decision, core.Deliberation, core.Authorization, core.Refusal, core.Revocation, core.Permission, core.DecisionClass or a class role"
  - "When a consumer keyed an argument that failed the objection test to core.Objection, or a revocation to core.Authorization"
type: "decision"
---

# Ontology questions from AK's decision records, 2026-10-02

**Decision.** The Holding Owner ruled on AK 6364's questions on 2026-10-01 and 2026-10-02. The
rulings are AK evidence 12130 (Q1, Q2), 12179 (Q3 to Q6), 12209 (in-place readings; prepare the
version), 12211 (`core.Objection` in place), 12302 (the class roles' base type is `core.Proposal`; the owner's
wording of `core.Decision`) and 12346 (after the consent round). This note records the change drafted
from them.
- **Class.** C: every question touches a reserved identifier or the core word *decision* (ADR-0008
  §1.5, §1.6, §4).
- **Driver.** AK 5991's decision records needed closed vocabularies, and AK routed the questions it
  may not answer itself. Packet: `docs/project/2026-10-01-ak6364-decision-records-ontology-questions.md`.
- **Consent.** Reserved identifiers and foundational categories go to the Holding Owner after the
  stewardship consent round (ADR-0008 §4). The stewardship roles are not held yet, and during the
  pilot the owner answers consent rounds for the FCOS layer (§6), so every holder asked is the
  Holding Owner. The FCOS pilot and AK sessions were invited as objection sources (packet §6;
  round evidence 12306). Both replied; each possible objection was tested, and the owner ruled on
  the points the tests left open (see "Consent round" below).
- **Authorization.** Pending. The Holding Owner authorizes the final content before the PR is opened.
- **Dissent.** None recorded; dissent exists only once a decision has gone ahead.
- **Conformance receipt.** The corpus digest at the commit that is authorized (to be filled).
- **Review date.** 2027-04-01 (proposed).

## What changed

| Identifier | Change |
|---|---|
| `core.PossibleObjection` | new, UFO mode: an argument raised against a proposal, agreement or activity, offered as an objection whether or not it qualifies |
| `core.Objection` | reworded in place: a possible objection, raised against a proposal in a consent round, that qualified; `is_a core.PossibleObjection` (a subkind) |
| `core.Concern` | new, UFO mode: S3's concern; it never blocks consent and never becomes dissent |
| `core.ConsentRound` | reworded in place: each *possible* objection is tested; each objection ends integrated, withdrawn or standing; a possible objection may be withdrawn before its test, and one that fails is kept with its test result (evidence 12346) |
| `core.Dissent` | typical usage extended in place: before a decision goes ahead, a standing objection is escalated, not yet dissent; edge `depends_on core.Decision` |
| `core.Decision` | new, UFO mode: the intention a deliberation creates (Core Ontology on Decision Making); the Holding Owner's wording, adopted 2026-10-02 (evidence 12302), including "doing nothing included" |
| `core.Deliberation` | new, UFO event: `produces core.Decision` |
| `core.DecisionGate` | edge `is_a core.Deliberation` |
| `core.DecisionRecord` | edge `depends_on core.Decision`; one record may document several decisions in order (evidence 12346) |
| `core.Authorization` | edges `manifests core.Decision`, `precedes core.Revocation` |
| `core.Refusal` | new, UFO event: the holder of the authority refuses a permission asked for |
| `core.Revocation` | new, UFO event: ends permissions or a delegated authority; one concept for both |
| `core.Permission` | typical usage extended in place: its scope may say when it ends; a review date ends nothing |
| `core.ClassAChange`, `core.ClassBChange`, `core.ClassCChange` | new, UFO roles: the class a proposal holds under the class rules; each `is_a core.Proposal` (evidence 12302); the reserved scope is class C first, and A and B lie outside it |
| `core.DecisionClass` | new, high-order type: disjointly categorizes `core.Proposal`, and a classified proposal holds exactly one class role (evidence 12346); its instances are the three class roles |
| `core.UfoCategory.HighOrderType` | new foundational category (MLT), a sibling of the UFO categories |
| relation `manifests` | new relation type (UFO-B manifestation) |
| `core.ConsentTier` | unchanged: it is the path tier, not the decision class; its category stays open |

The reference model (`docs/reference-model/governance-core.md`) gains the category row, a row per new
concept, the single end-state question for `core.Objection` (inspector finding N6, AK 6218), the
decision-making and MLT papers in its sources, and a corrected reason in the open row for
`core.ConsentTier`.

## Rulings of 2026-10-02 (evidence 12302)

- **The class roles' base type is `core.Proposal`.** A proposal holds class A, B or C under the class
  rules: each class role `is_a core.Proposal`, and `core.DecisionClass` categorizes `core.Proposal`
  (disjointly, after the ruling of evidence 12346 below).
- **`core.Decision`'s wording is the Holding Owner's.** The owner adopted the drafted text verbatim as
  the definition of the reserved word *decision*. "Doing nothing included" is the owner's addition to
  the paper's analysis: in decision analysis "do nothing" is always an alternative (combination
  strategy §5).

## Consent round (evidence 12306)

The AK coordinator and an FCOS session opened for the round (the pilot role was vacant) raised possible objections, blind and in parallel
(evidence 12310). A tester who was neither the objector nor the proposer checked each argument
against the files (evidence 12312 for AK, 12313 for FCOS).
- **Integrated** (qualified, no ruling needed):
  - AK's schema-47 keys: AK amends migration 47 before its live apply (Consumers).
  - The `core.PossibleObjection` anti-example now names an assumption *not raised* as an objection.
  - FCOS F1: `not_after` is the end its grant states (Consumers).
  - FCOS F2: FCOS adopts forward, in new record versions (Consumers).
  - FCOS F3: dissent also when a revocation goes ahead (`core.Decision`, `core.Objection`).
  - FCOS F4: the reserved scope is class C first (`core.ClassAChange`, `core.ClassBChange`,
    `core.ClassCChange`).
- **Ruled by the Holding Owner** (evidence 12346), each the recommended option:
  - A possible objection may be withdrawn before its test. One that fails is kept with its test
    result; the proposer may still take it up as an amendment (AK's ConsentRound point).
  - A proposal is unclassified until a named party applies the class rules, and no decision on it
    may go ahead; so `core.DecisionClass` disjointly categorizes `core.Proposal` (AK's
    classification point).
  - One decision record may document several decisions in order (AK's decision-case point).
  - AK amends migration 47 rather than shipping 48.
- **Not qualified, or concerns only** (each goes to its owner as a follow-up): an end date on AK
  grants (already AK's, Q6); 6366's classification record; a home for concerns in AK; revocation of
  several permissions in one act; AK pinning the ontology version; 6368's fields; "Not the AK decision
  row" (a preference); FCOS C1, which FCOS entity plays `core.Proposal`.
- **Disclosed.** `core.Deliberation` names its agent "a decider"; the packet draft read "an agent".
  The change keeps a CI discovery gate under its cap (ontology-kernel 6448); neither word was ruled.

## Open points

- **`core.DecisionGate`'s diagnostic question.** "Does it create or change a permission or commitment?
  If not, it is a check, not a decision gate." Under `is_a core.Deliberation` a decision gate creates
  a decision, an intention; the permission comes from the authorization that manifests it. The
  question is left unchanged; the owner decides whether the question or the edge moves.
- **Sibling category.** The kernel adds high-order type beside the UFO categories. In OntoUML with
  high-order types, a high-order type specialises the UFO category of its instances (Fonseca et al.
  2022, §4.4), so `core.DecisionClass` would specialise UFO Role.

## In-place readings

CORE-INV-002 says a meaning change takes a new identifier. These five identifiers were released in
v0.3.0. The owner read the changes as keeping each concept's meaning (evidence 12209, 12211), so the
identifiers stay; the two extensions ruled after the consent round (evidence 12346) are named in the
authorization request:
- **`core.Objection`.** Its conditions are unchanged: it blocks consent, and "a preference without
  impact" is not one. An argument that fails the S3 test never blocked consent, so it was never an
  objection under the kernel's own definition. Adding `core.PossibleObjection` above it leaves its
  extension as it was (evidence 12211, after the owner asked for Guizzardi's view on type identity).
- **`core.ConsentRound`.** "Each possible objection is tested" names what the round already did: it
  tested arguments before knowing whether they qualified. Only an objection ends integrated or
  standing; a possible objection may end withdrawn before its test, and one that fails takes no end
  state (evidence 12346). This narrows v0.3.0's text, where every tested argument took an end state.
- **`core.DecisionRecord`.** One record may document several decisions in order (evidence 12346); its
  Required line now names each of them. A record of one decision is the case with one entry, so every
  v0.3.0 record still reads as before.
- **`core.Dissent`.** The added line restates its diagnostic: dissent does not exist without a decision
  that went ahead (ruling Q2).
- **`core.Permission`.** "Within a stated scope" already allowed a scope with an end; the line says so
  and separates the end from the agreement review date.

## Consumers

- **agent-kernel (AK 5991 records).**
  - `decision_objections` rows key to `core.PossibleObjection`; a qualified one is a
    `core.Objection`.
  - `act` keys to `core.Authorization`, `core.Refusal` or `core.Revocation`.
  - Concerns gain a home.
  - Grants may carry an optional end (Q6).
  - The AK decision row is a decision case, mapped to `core.DecisionRecord`.
  - Migration 47 is amended with these keys and a disposition grid matched to the final
    `core.ConsentRound` text before any database holds it (evidence 12346; AK 6471). AK 6367,
    the live apply, waits for it. After that, the append-only CHECK constants mean a forward
    migration, never a rewrite.
  - AK 6366 waits on `core.DecisionClass`, not on `core.ConsentTier`.
- **FCOS pilot.**
  - FCOS adopts this forward, in new record versions. Version-1 records, signed facts and archived
    inputs stay as they are and keep their version-1 validators.
  - Arguments judged `not_valid` are possible objections that did not qualify; in new records they
    leave the `dissent` list.
  - New revocation records take `core.Revocation`.
  - `not_after` is the end its grant states (`core.Permission`), enforced as now. An agreement review
    falls due before it and ends nothing.
  - `decision_class` (design D11) maps to `core.DecisionClass`. Which FCOS entity plays
    `core.Proposal` is FCOS's to state (consent-round concern C1).
- **governance-kernel (class C).**
  - The ADR-0008 data file reserves the new identifiers, and adds *possible objection*, *concern*,
    *refusal*, *revocation* and *decision class* to `core_words`.
  - consent-change-control and the ADR-0008 §4 and §8 wording read "escalated objection" before a
    decision, and "dissent" after one.
  - human-on-the-loop-consent reads `declined` as a refusal.
  - The vocabulary card's authorization / consent / dissent line follows these words.
- **org-handbook.** The consent-tier SOPs stay on `core.ConsentTier`; class wording follows the decision
  class.
- **Company and repo layers.** pi-extensions and the other layers repin to the version that carries
  this note (ADR-0008 §7; standing repin decision, AK 6288).
