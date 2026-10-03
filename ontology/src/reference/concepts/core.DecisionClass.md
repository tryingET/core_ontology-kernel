---
ont:
  id: "core.DecisionClass"
  type: concept
  labels: ["decision class"]
  synonyms: []
  description: "A high-order type that disjointly categorizes core.Proposal: each of its instances, the class roles class-A change, class-B change and class-C change, is a proper specialisation of core.Proposal; a proposal holds at most one of them at a time, and exactly one once the class rules have been applied to it."
  relations:
    - type: instance_of
      target: core.UfoCategory.HighOrderType
    - type: is_a
      target: core.UfoCategory.Role
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
A high-order type that disjointly categorizes core.Proposal: each of its instances, the class roles class-A change, class-B change and class-C change, is a proper specialisation of core.Proposal; a proposal holds at most one of them at a time, and exactly one once the class rules have been applied to it.

## Typical usage
- The instances are `core.ClassAChange`, `core.ClassBChange` and `core.ClassCChange`; each is a role, because a change holds it through its classification by the class rules and can move between classes.
- Its base type is `core.Proposal` (Holding Owner ruling, 2026-10-02, evidence 12302): each class role `is_a core.Proposal`, and a proposal holds class A, B or C under the class rules.
- A proposal holds its class once a named party has applied the class rules to it. Until then it is unclassified, and no decision on it may go ahead (Holding Owner ruling, 2026-10-02, evidence 12346). So every classified proposal holds exactly one class role; an unclassified one holds none.
- The authorization part of a decision record says "not required" when the class needs no owner authorization.

## Common confusions
- Not `core.ConsentTier`: consent tiers classify paths by who must consent (Core, Org, Project); decision classes classify proposals (Holding Owner's question of 2026-09-30, AK evidence 11507).
- Not an autonomy level: that concept, for later, describes how far an agent may decide; it belongs to the agent's delegated capacity.
- Not a quality: a class is assigned by applying rules, not measured on a scale intrinsic to the change.

## Category
- High-order type (`core.UfoCategory.HighOrderType`), disjointly categorizing `core.Proposal`. Required: its base type (`core.Proposal`), its instances (the three class roles), the rules that assign them.
- It specialises `core.UfoCategory.Role`, the category of its instances (Fonseca et al. 2022, §4.4; Holding Owner ruling 12461). The three class roles classify proposals; DecisionClass classifies those role types. HighOrderType identifies that its instances are types.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- governance-kernel `docs/dev/consent-change-control.md`, "Decision classes and the three records"; authorization-vs-consent adjudication §6 (class C narrowed by the Holding Owner, 2026-09-26).
- V. A. Carvalho, J. P. A. Almeida, C. M. Fonseca, G. Guizzardi (2017), Multi-level ontology-based conceptual modeling, Data & Knowledge Engineering 109, pp. 3–24: "t partitions t’ iff t categorizes t’ and each instance of t’ is instance of exactly one instance of t"; under disjoint categorization each instance of t’ is an instance of at most one instance of t.
- C. M. Fonseca, G. Guizzardi, J. P. A. Almeida, T. P. Sales, D. Porello (2022), Incorporating Types of Types in Ontology-Driven Conceptual Modeling, ER 2022, LNCS 13607, pp. 18–34: a type categorizes a base type "iff every instance of the former is a proper specialization of the latter".
- Holding Owner ruling Q5, 2026-10-01 (AK 6364, evidence 12179).
- Holding Owner ruling, 2026-10-02 (AK 6364, evidence 12302): the base type is `core.Proposal`.
- Holding Owner ruling, 2026-10-02 (AK 6364, evidence 12346): a proposal may be unclassified, and then no decision on it may go ahead.
- Holding Owner ruling, 2026-10-03 (AK 6364, evidence 12461): `is_a core.UfoCategory.Role`, retaining HighOrderType.
- Decision note: `ontology/decisions/2026-10-02-decision-records-questions.md`.

Admitted: AK task 6364, 2026-10-02
