---
ont:
  id: "core.Configuration"
  type: concept
  labels: ["configuration"]
  synonyms: ["configuration control", "Binner Konfigurationsmanagement (B2 sense)"]
  description: "Control of controlled items: each item has a named change authority, and every change goes through it (NASA configuration control)."
  relations: []
  examples:
    - "Keeping the AK schema under a named change authority"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# configuration (core.Configuration)

## Definition
Control of controlled items: each item has a named change authority, and every change goes through it (NASA configuration control).

## Typical usage
- A register of controlled items (core docs, domain descriptions, interface agreements, schemas, runtime contracts), each with its change authority.

## Common confusions
- Binner's 2018 Konfigurationsmanagement is organisation design.

## Source and mapping
- Combination strategy §3 (commitment); Combination strategy §4 configuration row.
- Vocabulary card: configuration [control of controlled items].
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
