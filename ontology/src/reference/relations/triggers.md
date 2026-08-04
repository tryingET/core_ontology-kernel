---
ont:
  id: "core.rel.triggers"
  type: relation
  labels: ["triggers"]
  description: "X löst Y aus (Trigger → Effect)"
  group: "causality"
  characteristics:
    transitive: false
    symmetric: false
  axis_default: "children"
  examples:
    - "core.AuditEvent triggers core.Policy (audit event causes a policy review)"
  anti_examples:
    - "Using triggers for deterministic outputs (use `produces`)"
---

## Definition
`X triggers Y` means X causes Y to start/occur (trigger → effect); prefer `produces` for guaranteed outputs.

## Notes
- Keep semantics crisp.
- Do not overload one relation with multiple meanings (Lucidity).

## Use when
- X causes Y to start/occur (trigger → effect).

## Do not use when
- You mean a guaranteed output (use `produces`) or a hard requirement (use `depends_on`).

## Domain / Range
- Domain: triggering event/condition
- Range: triggered process/event/state
