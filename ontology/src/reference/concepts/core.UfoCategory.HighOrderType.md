---
ont:
  id: "core.UfoCategory.HighOrderType"
  type: concept
  labels: ["high-order type"]
  synonyms: []
  description: "The category, from the multi-level theory MLT that UFO incorporates, of types whose instances are themselves types; a high-order type categorises a base type when each of its instances specialises that base type."
  relations:
    - type: instance_of
      target: core.UfoCategory
  examples:
    - "Bird species, whose instances are emperor penguin and American eagle"
    - "Decision class, whose instances are class-A, class-B and class-C change"
  anti_examples:
    - "A supertype of the classes (a high-order type is instantiated by its classes, not specialised by them)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# high-order type (core.UfoCategory.HighOrderType)

## Definition
The category, from the multi-level theory MLT that UFO incorporates, of types whose instances are themselves types; a high-order type categorises a base type when each of its instances specialises that base type.

## Typical usage
- Test question: Are its instances types rather than individuals?
- Governance-core concepts in this category: core.DecisionClass.
- Its instances point to it with instance_of, like any concept to its category; they keep their own UFO category (the decision classes are roles).

## Source and mapping
- V. A. Carvalho, J. P. A. Almeida, C. M. Fonseca, G. Guizzardi (2017), Multi-level ontology-based conceptual modeling, Data & Knowledge Engineering 109.
- C. M. Fonseca, G. Guizzardi, J. P. A. Almeida, T. P. Sales, D. Porello (2022), Incorporating Types of Types in Ontology-Driven Conceptual Modeling, ER 2022, LNCS 13607.
- Not yet checked against the page images; the definition follows the abstracts and the papers' summaries.
- Holding Owner ruling Q5, 2026-10-01 (AK 6364, evidence 12179): a new foundational category.
- Reference model: `docs/reference-model/governance-core.md`.

Admitted: AK task 6364, 2026-10-02
