---
ont:
  id: "core.ClassCChange"
  type: concept
  labels: ["class-C change"]
  synonyms: []
  description: "A role a proposal plays under the class rules when its change lies within the Holding Owner's reserved scope as those rules list it, or cannot be made reversible."
  relations:
    - type: is_a
      target: core.Proposal
    - type: instance_of
      target: core.UfoCategory.Role
    - type: instance_of
      target: core.DecisionClass
  examples:
    - "A proposal for a new core definition, or to publish under the society's name"
  anti_examples:
    - "A proposal for a reversible change inside one domain and outside the reserved scope (class A)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# class-C change (core.ClassCChange)

## Definition
A role a proposal plays under the class rules when its change lies within the Holding Owner's reserved scope as those rules list it, or cannot be made reversible.

## Typical usage
- One of the three decision classes (`core.DecisionClass`). A classified proposal holds exactly one class at a time, and can move to another, for example when its change is made reversible.
- The reserved scope is the class rules' list (Holding Owner decision, 2026-09-26), for example a core definition or publication under the society's name. The list is governance-kernel's; when it changes, this concept does not.
- The class rules apply the reserved scope first: a change within it is class C however reversible or local it is. ADR-0008 applies the rule to reserved identifiers (§1.6, "class C at every layer") and, until the handover, to every change to a core concept (§4).
- Whether class C needs a consent round or the owner's authorization is governance-kernel's rule, not part of this concept.

## Category
- UFO role (`core.UfoCategory.Role`), played through the classification of the proposal by the class rules; an instance of the high-order type `core.DecisionClass`, and a specialisation of its base type `core.Proposal`. Required: the proposal, the rule that classifies it, who applied it.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- governance-kernel `docs/dev/consent-change-control.md`, "Decision classes and the three records" (class C).
- Holding Owner ruling Q5, 2026-10-01 (AK 6364, evidence 12179).
- Holding Owner ruling, 2026-10-02 (AK 6364, evidence 12302): the base type is `core.Proposal`; a proposal holds class A, B or C under the class rules.
- Decision note: `ontology/decisions/2026-10-02-decision-records-questions.md`.

Admitted: AK task 6364, 2026-10-02
