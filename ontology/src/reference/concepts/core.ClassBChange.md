---
ont:
  id: "core.ClassBChange"
  type: concept
  labels: ["class-B change"]
  synonyms: []
  description: "A role a proposed change plays under the class rules: reversible and touching several domains, including a technical one-way change once it has been made reversible (a verified backup, a written rollback plan, a check that proves the result)."
  relations:
    - type: instance_of
      target: core.UfoCategory.Role
    - type: instance_of
      target: core.DecisionClass
  examples:
    - "A schema migration with a verified paired backup, a rollback plan and a rehearsal"
  anti_examples:
    - "A schema migration that cannot be made reversible (class C)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# class-B change (core.ClassBChange)

## Definition
A role a proposed change plays under the class rules: reversible and touching several domains, including a technical one-way change once it has been made reversible (a verified backup, a written rollback plan, a check that proves the result).

## Typical usage
- One of the three decision classes (`core.DecisionClass`). A change holds exactly one class at a time, and can move to another, for example when it is made reversible.
- Whether class B needs a consent round or the owner's authorization is governance-kernel's rule, not part of this concept.

## Category
- UFO role (`core.UfoCategory.Role`), played through the classification of the change by the class rules; an instance of the high-order type `core.DecisionClass`. Required: the change, the rule that classifies it, who applied it.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- governance-kernel `docs/dev/consent-change-control.md`, "Decision classes and the three records" (class B).
- Holding Owner ruling Q5, 2026-10-01 (AK 6364, evidence 12179).
- Decision note: `ontology/decisions/2026-10-02-decision-records-questions.md`.

Admitted: AK task 6364, 2026-10-02
