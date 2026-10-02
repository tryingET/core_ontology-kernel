---
summary: "Decision note for the ontology questions from AK's decision records (AK 6364, 2026-10-02): possible objection and concern, when dissent exists, decision as an intention created by a deliberation, refusal and revocation, the decision class as a high-order type over three class roles, when a permission ends, and the in-place readings of core.Objection, core.ConsentRound, core.Dissent and core.Permission."
read_when:
  - "When a record, schema or layer uses core.Objection, core.PossibleObjection, core.Concern, core.Dissent, core.Decision, core.Deliberation, core.Authorization, core.Refusal, core.Revocation, core.Permission, core.DecisionClass or a class role"
  - "When a consumer keyed an argument that failed the objection test to core.Objection, or a revocation to core.Authorization"
type: "decision"
---

# Ontology questions from AK's decision records, 2026-10-02

**Decision.** The Holding Owner decided AK 6364 on 2026-10-01 and 2026-10-02. The rulings are AK
evidence 12130 (Q1, Q2), 12179 (Q3 to Q6), 12209 (in-place readings; prepare the version) and 12211
(`core.Objection` in place).
- **Class.** C: every question touches a reserved identifier or the core word *decision* (ADR-0008
  §1.5, §1.6, §4).
- **Driver.** AK 5991's decision records needed closed vocabularies, and AK routed the questions it
  may not answer itself. Packet: `docs/project/2026-10-01-ak6364-decision-records-ontology-questions.md`.
- **Consent.** Reserved identifiers and foundational categories go to the Holding Owner after the
  stewardship consent round (ADR-0008 §4). The stewardship roles are not held yet, and during the
  pilot the owner answers consent rounds for the FCOS layer (§6), so every holder asked is the
  Holding Owner. The FCOS pilot session and the AK session are objection sources, not holders.
- **Dissent.** None.

## What changed

| Identifier | Change |
|---|---|
| `core.PossibleObjection` | new, UFO mode: an argument raised against a proposal, agreement or activity, offered as an objection before it is tested |
| `core.Objection` | reworded in place: a possible objection that qualified; `is_a core.PossibleObjection` (a subkind) |
| `core.Concern` | new, UFO mode: S3's concern; it never blocks consent and never becomes dissent |
| `core.ConsentRound` | reworded in place: each *possible* objection is tested; each objection ends integrated, withdrawn or standing |
| `core.Dissent` | typical usage extended in place: before a decision goes ahead, a standing objection is escalated, not yet dissent; edge `depends_on core.Decision` |
| `core.Decision` | new, UFO mode: the intention a deliberation creates (Core Ontology on Decision Making) |
| `core.Deliberation` | new, UFO event: `produces core.Decision` |
| `core.DecisionGate` | edge `is_a core.Deliberation` |
| `core.DecisionRecord` | edge `depends_on core.Decision` |
| `core.Authorization` | edges `manifests core.Decision`, `precedes core.Revocation`; typical-usage line |
| `core.Refusal` | new, UFO event: the holder of the authority refuses a permission asked for |
| `core.Revocation` | new, UFO event: ends permissions or a delegated authority; one concept for both |
| `core.Permission` | typical usage extended in place: its scope may say when it ends; a review date ends nothing |
| `core.ClassAChange`, `core.ClassBChange`, `core.ClassCChange` | new, UFO roles: the class a proposed change holds under the class rules |
| `core.DecisionClass` | new, high-order type: its instances are the three class roles |
| `core.UfoCategory.HighOrderType` | new foundational category (MLT) |
| relation `manifests` | new relation type (UFO-B manifestation) |
| `core.ConsentTier` | unchanged: it is the path tier, not the decision class; its category stays open |

The reference model (`docs/reference-model/governance-core.md`) gains the category row, a row per new
concept, the single end-state question for `core.Objection` (inspector finding N6, AK 6218), and a
corrected reason in the open row for `core.ConsentTier`.

## In-place readings

CORE-INV-002 says a meaning change takes a new identifier. These four identifiers were released in
v0.3.0. The owner read each change as keeping the concept's meaning, so the identifiers stay:
- **`core.Objection`.** Its conditions are unchanged: it blocks consent, and "a preference without
  impact" is not one. An argument that fails the S3 test never blocked consent, so it was never an
  objection under the kernel's own definition. Adding `core.PossibleObjection` above it leaves its
  extension as it was (evidence 12211, after the owner asked for Guizzardi's view on type identity).
- **`core.ConsentRound`.** "Each possible objection is tested" names what the round already did: it
  tested arguments before knowing whether they qualified.
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
  - The AK decision row is a decision case, mapped to `core.DecisionRecord`.
  - The append-only CHECK constants mean a forward migration, never a rewrite.
  - AK 6366 waits on `core.DecisionClass`, not on `core.ConsentTier`.
- **FCOS pilot.**
  - Arguments judged `not_valid` are possible objections that did not qualify, and they leave the
    `dissent` list.
  - Revocation facts take `core.Revocation`.
  - `not_after` is named either an end of the permission or a review date.
  - `decision_class` (design D11) maps to `core.DecisionClass`.
- **governance-kernel (class C).**
  - The ADR-0008 data file reserves the new identifiers, and adds *possible objection*, *concern*,
    *refusal*, *revocation* and *decision class* to `core_words`.
  - consent-change-control and the ADR-0008 §4 and §8 wording read "escalated objection" before a
    decision, and "dissent" after one.
  - human-on-the-loop-consent reads `declined` as a refusal.
- **Company and repo layers.** pi-extensions and the other layers repin to the version that carries
  this note (ADR-0008 §7; standing repin decision, AK 6288).
