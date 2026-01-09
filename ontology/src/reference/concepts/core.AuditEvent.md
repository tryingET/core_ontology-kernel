---
ont:
  id: "core.AuditEvent"
  type: concept
  labels: ["AuditEvent"]
  synonyms: []
  description: "Nachvollziehbares Ereignis (wer tat was wann warum)."
  relations: []
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
