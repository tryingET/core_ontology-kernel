---
ont:
  id: "core.rel.manifests"
  type: relation
  labels: ["manifests"]
  description: "X manifests Y: the event X realises the disposition or intention Y (UFO-B manifestation)"
  group: "causality"
  characteristics:
    transitive: false
    symmetric: false
  axis_default: "left"
  examples:
    - "core.Authorization manifests core.Decision (the sign-off carries the owner's decision out)"
  anti_examples:
    - "Using manifests for creation (use `produces`: a deliberation produces a decision)"
---

## Definition
`X manifests Y` means the event X realises Y, a disposition or an intention of its bearer; in the decision-making ontology a decision-resulting action manifests the decision.

## Notes
- Keep semantics crisp.
- Do not overload one relation with multiple meanings (Lucidity).

## Use when
- X is an event and Y the mode (an intention, a disposition) it carries out.

## Do not use when
- X creates Y (use `produces`) or merely needs Y (use `depends_on`).

## Domain / Range
- Domain: event concept
- Range: mode concept (intention or disposition)

## Source
- R. Guizzardi, B. G. Carneiro, D. Porello, G. Guizzardi (2020), A Core Ontology on Decision Making, ONTOBRAS 2020, CEUR-WS 2728, §3 (a decision's relation to its resulting action is a manifestation).
- Holding Owner ruling Q3, 2026-10-01 (AK 6364, evidence 12179).

Admitted: AK task 6364, 2026-10-02
