---
ont:
  id: "core.ClassCChange"
  type: concept
  labels: ["class-C change"]
  synonyms: []
  description: "A role a proposed change plays under the class rules: within the Holding Owner's reserved scope as those rules list it, or anything that cannot be made reversible."
  relations:
    - type: instance_of
      target: core.UfoCategory.Role
    - type: instance_of
      target: core.DecisionClass
  examples:
    - "A new core definition; publishing under the society's name"
  anti_examples:
    - "A reversible change inside one domain (class A)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# class-C change (core.ClassCChange)

## Definition
A role a proposed change plays under the class rules: within the Holding Owner's reserved scope as those rules list it, or anything that cannot be made reversible.

## Typical usage
- One of the three decision classes (`core.DecisionClass`). A change holds exactly one class at a time, and can move to another, for example when it is made reversible.
- The reserved scope is the class rules' list (Holding Owner decision, 2026-09-26), for example a core definition or publication under the society's name. The list is governance-kernel's; when it changes, this concept does not.
- Whether class C needs a consent round or the owner's authorization is governance-kernel's rule, not part of this concept.

## Category
- UFO role (`core.UfoCategory.Role`), played through the classification of the change by the class rules; an instance of the high-order type `core.DecisionClass`. Required: the change, the rule that classifies it, who applied it.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- governance-kernel `docs/dev/consent-change-control.md`, "Decision classes and the three records" (class C).
- Holding Owner ruling Q5, 2026-10-01 (AK 6364, evidence 12179).
- Decision note: `ontology/decisions/2026-10-02-decision-records-questions.md`.

Admitted: AK task 6364, 2026-10-02
