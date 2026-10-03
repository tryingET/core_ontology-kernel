---
ont:
  id: "core.ClassBChange"
  type: concept
  labels: ["class-B change"]
  synonyms: []
  description: "A role a proposal plays under the class rules when its change is reversible, touches several domains and lies outside the Holding Owner's reserved scope, including a technical one-way change once it has been made reversible (a verified backup, a written rollback plan, a check that proves the result)."
  relations:
    - type: is_a
      target: core.Proposal
    - type: instance_of
      target: core.UfoCategory.Role
    - type: instance_of
      target: core.DecisionClass
  examples:
    - "A proposal for a schema migration made reversible first: a verified backup, a written rollback plan, and a check that proves the result"
  anti_examples:
    - "A proposal for a schema migration that cannot be made reversible (class C)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# class-B change (core.ClassBChange)

## Definition
A role a proposal plays under the class rules when its change is reversible, touches several domains and lies outside the Holding Owner's reserved scope, including a technical one-way change once it has been made reversible (a verified backup, a written rollback plan, a check that proves the result).

## Typical usage
- One of the three decision classes (`core.DecisionClass`). A classified proposal holds exactly one class at a time, and can move to another, for example when its change is made reversible.
- Whether class B needs a consent round or the owner's authorization is governance-kernel's rule, not part of this concept.

## Category
- UFO role (`core.UfoCategory.Role`), played through the classification of the proposal by the class rules; an instance of the high-order type `core.DecisionClass`, and a specialisation of its base type `core.Proposal`. Required: the proposal, the rule that classifies it, who applied it.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- governance-kernel `docs/dev/consent-change-control.md`, "Decision classes and the three records" (class B).
- Holding Owner ruling Q5, 2026-10-01 (AK 6364, evidence 12179).
- Holding Owner ruling, 2026-10-02 (AK 6364, evidence 12302): the base type is `core.Proposal`; a proposal holds class A, B or C under the class rules.
- Decision note: `ontology/decisions/2026-10-02-decision-records-questions.md`.

Admitted: AK task 6364, 2026-10-02
