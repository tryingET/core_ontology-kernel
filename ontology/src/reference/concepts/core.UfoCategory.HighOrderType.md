---
ont:
  id: "core.UfoCategory.HighOrderType"
  type: concept
  labels: ["high-order type"]
  synonyms: []
  description: "The category, from the multi-level theory MLT that UFO incorporates, of domain types whose instances are themselves domain types; such a type categorises a base type when each of its instances is a proper specialisation of that base type."
  relations:
    - type: instance_of
      target: core.UfoCategory
  examples:
    - "Species, whose instances include the types Emperor Penguin and Dog (Fonseca et al. 2022, Fig. 3)"
    - "Person Role, which categorises Person; its instances include Manager and Researcher (Carvalho et al. 2017, Fig. 5)"
    - "core.DecisionClass, whose instances are the three class roles"
  anti_examples:
    - "A supertype of the types it classifies (Species classifies Emperor Penguin; it does not generalise it)"
    - "core.UfoCategory and its categories (they classify the kernel's concepts, not domain types)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# high-order type (core.UfoCategory.HighOrderType)

## Definition
The category, from the multi-level theory MLT that UFO incorporates, of domain types whose instances are themselves domain types; such a type categorises a base type when each of its instances is a proper specialisation of that base type.

## Typical usage
- Test question: Are its instances domain types rather than individuals?
- A concept's UFO category is the target of its instance_of edge under core.UfoCategory.
- Governance-core concepts in this category: core.DecisionClass. It is the instance of this category; the class roles are instances of core.DecisionClass. They point to core.DecisionClass with instance_of as well, but their UFO category is core.UfoCategory.Role.
- The kernel adds high-order type as a sibling of the other categories under core.UfoCategory. In OntoUML with high-order types, a high-order type instead specialises the UFO category of its instances (Fonseca et al. 2022, §4.4): core.DecisionClass would specialise UFO Role.

## Source and mapping
- V. A. Carvalho, J. P. A. Almeida, C. M. Fonseca, G. Guizzardi (2017), Multi-level ontology-based conceptual modeling, Data & Knowledge Engineering 109, pp. 3–24: categorization ("a type t categorizes a type t’ iff all instances of t are proper specializations of t’"), partitions, and Fig. 5 (Person Role).
- C. M. Fonseca, G. Guizzardi, J. P. A. Almeida, T. P. Sales, D. Porello (2022), Incorporating Types of Types in Ontology-Driven Conceptual Modeling, ER 2022, LNCS 13607, pp. 18–34: high-order types, axiom a7 (categorizes), Fig. 3 (Species), §4.4 (rules involving UFO classes).
- Checked on 2026-10-02 against the text of the authors' copies (NEMO, UFES), not the page images.
- Holding Owner ruling Q5, 2026-10-01 (AK 6364, evidence 12179): a new foundational category.
- Reference model: `docs/reference-model/governance-core.md`.

Admitted: AK task 6364, 2026-10-02
