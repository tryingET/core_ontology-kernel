---
ont:
  id: "core.SchemaCheck"
  type: concept
  labels: ["schema check"]
  synonyms: ["schema validation"]
  description: "A check that a record or file conforms to its schema."
  relations: []
  examples:
    - "Checking a concept file against the ontology-markdown-v1 grammar"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# schema check (core.SchemaCheck)

## Definition
A check that a record or file conforms to its schema.

## Common confusions
- Not validation (fitness for purpose) and not verification against a requirement: a passing schema check proves conformance to the schema only.

## Source and mapping
- Combination strategy §4 validation row: schema validation → schema check.
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
