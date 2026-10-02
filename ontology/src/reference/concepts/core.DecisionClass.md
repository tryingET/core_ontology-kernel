---
ont:
  id: "core.DecisionClass"
  type: concept
  labels: ["decision class"]
  synonyms: []
  description: "A high-order type that categorises proposed changes: its instances are the class roles class-A change, class-B change and class-C change, and a change holds exactly one of them at a time."
  relations:
    - type: instance_of
      target: core.UfoCategory.HighOrderType
  examples:
    - "Class C is the decision class of a new core definition"
  anti_examples:
    - "core.ConsentTier (a tier of paths by who must consent: Core, Org, Project)"
    - "An agent's autonomy level (how far an agent may decide without the owner; a property of its delegated capacity)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# decision class (core.DecisionClass)

## Definition
A high-order type that categorises proposed changes: its instances are the class roles class-A change, class-B change and class-C change, and a change holds exactly one of them at a time.

## Typical usage
- The instances are `core.ClassAChange`, `core.ClassBChange` and `core.ClassCChange`; each is a role, because a change holds it through its classification by the class rules and can move between classes.
- The authorization part of a decision record says "not required" when the class needs no owner authorization.

## Common confusions
- Not `core.ConsentTier`: consent tiers classify paths by who must consent (Core, Org, Project); decision classes classify proposed changes (Holding Owner's question of 2026-09-30, AK evidence 11507).
- Not an autonomy level: that concept, for later, describes how far an agent may decide; it belongs to the agent's delegated capacity.
- Not a quality: a class is assigned by applying rules, not measured on a scale intrinsic to the change.

## Category
- High-order type (`core.UfoCategory.HighOrderType`), categorising proposed changes. Required: its instances (the three class roles), the rules that assign them.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- governance-kernel `docs/dev/consent-change-control.md`, "Decision classes and the three records"; authorization-vs-consent adjudication §6 (class C narrowed by the Holding Owner, 2026-09-26).
- V. A. Carvalho, J. P. A. Almeida, C. M. Fonseca, G. Guizzardi (2017), Multi-level ontology-based conceptual modeling, Data & Knowledge Engineering 109; C. M. Fonseca et al. (2022), Incorporating Types of Types in Ontology-Driven Conceptual Modeling, ER 2022, LNCS 13607 (the powertype pattern: a high-order type categorises a base type).
- Holding Owner ruling Q5, 2026-10-01 (AK 6364, evidence 12179).
- Decision note: `ontology/decisions/2026-10-02-decision-records-questions.md`.

Admitted: AK task 6364, 2026-10-02
