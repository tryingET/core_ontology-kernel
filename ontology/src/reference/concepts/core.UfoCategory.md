---
ont:
  id: "core.UfoCategory"
  type: concept
  labels: ["UFO category"]
  synonyms: []
  description: "A foundational category of the Unified Foundational Ontology (UFO): what kind of entity a governance-core concept names. The concept points to its category with an instance_of edge."
  relations: []
  examples:
    - "core.Authorization instance_of core.UfoCategory.Event"
  anti_examples:
    - "core.Authorization is_a core.UfoCategory.Event (categories are meta-types, not supertypes)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# UFO category (core.UfoCategory)

## Definition
A foundational category of the Unified Foundational Ontology (UFO): what kind of entity a governance-core concept names. The concept points to its category with an instance_of edge.

## Typical usage
- Only the governance core carries categories (Holding Owner D22 and D23, 2026-09-26).
- One meaning and one category per identifier: a concept that names two categories is split (AK 5987).
- The reference model `docs/reference-model/governance-core.md` gives each categorised concept its required parties and a diagnostic question.

## Common confusions
- A category is not a supertype: UFO counts types as instances of meta-types, so the edge is instance_of, never is_a (UFO2022, axioms a1–a4).
- MITO segment and level say where a thing acts and who owns it; the category says what kind of thing it is. They are independent.

## Source and mapping
- Guizzardi et al. (2022), UFO: Unified Foundational Ontology, Applied Ontology 17(1).
- Guizzardi, Falbo, Guizzardi (2008), Grounding Software Domain Ontologies in UFO, IDEAS 2008 (UFO-C).
- Controlled-vocabulary adjudication, addendum (school 7): governance-kernel `docs/project/2026-09-26-controlled-vocabulary-adjudication.md`.

Admitted: AK task 5986, 2026-09-27
