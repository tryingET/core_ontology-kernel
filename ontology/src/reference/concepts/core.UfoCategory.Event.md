---
ont:
  id: "core.UfoCategory.Event"
  type: concept
  labels: ["UFO event"]
  synonyms: []
  description: "The UFO category of occurrences that unfold in time and cannot change once they have happened; an event takes reality from a pre-state situation to a post-state situation."
  relations:
    - type: instance_of
      target: core.UfoCategory
  examples:
    - "A review; a handover"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# UFO event (core.UfoCategory.Event)

## Definition
The UFO category of occurrences that unfold in time and cannot change once they have happened; an event takes reality from a pre-state situation to a post-state situation.

## Typical usage
- Test question: Can it change after it happened?
- Governance-core concepts in this category: core.AgreementReview, core.AuditEvent, core.Authorization, core.ConformanceAudit, core.ConsentRound, core.DecisionGate, core.Handover, core.LeitungReview, core.Operations, core.ProcessAudit, core.ReadinessReview, core.ReplayCheck, core.RoleReview, core.SchemaCheck, core.Validation, core.VerificationEvent, core.WorkProductInspection.

## Source and mapping
- Guizzardi et al. (2022), UFO: Unified Foundational Ontology, Applied Ontology 17(1), pp. 171, 174; Guizzardi, Falbo, Guizzardi (2008), Grounding Software Domain Ontologies in UFO, IDEAS 2008 (UFO-C), §3. Checked on the page images on 2026-09-27.
- Reference model: `docs/reference-model/governance-core.md`.

Admitted: AK task 5986, 2026-09-27
