---
ont:
  id: "core.AuditEvent"
  type: concept
  labels: ["AuditEvent"]
  synonyms: []
  description: "Nachvollziehbares Ereignis (wer tat was wann warum)."
  relations:
    - type: instance_of
      target: core.UfoCategory.Event
  examples:
    - "Merge Request merged (who/what/when/why)"
  anti_examples:
    - "Ein unstrukturierter Log-Text"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# AuditEvent (core.AuditEvent)

## Definition
Nachvollziehbares Ereignis (wer tat was wann warum).

## Typical usage
- Used to link changes to governance decisions and approvals.

## Common confusions
- Confused with unstructured log lines that lack actor/intent.

## Category
- UFO event (`core.UfoCategory.Event`). Required: who, what, when, why.
- Reference model: `docs/reference-model/governance-core.md`.
