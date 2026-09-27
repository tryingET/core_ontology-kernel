---
ont:
  id: "core.Directive"
  type: concept
  labels: ["directive"]
  synonyms: []
  description: "A binding rule in text, such as an AK decision or a 'must' in AGENTS.md; it can be tailored only by relief."
  relations:
    - type: is_a
      target: core.Policy
    - type: instance_of
      target: core.UfoCategory.NormativeDescription
  examples:
    - "'Never use /tmp for worktrees' in the workspace AGENTS.md"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# directive (core.Directive)

## Definition
A binding rule in text, such as an AK decision or a 'must' in AGENTS.md; it can be tailored only by relief.

## Common confusions
- Not direction (AK strategy) and not guidance (Prompt Vault advice, freely customizable).

## Category
- UFO normative description (`core.UfoCategory.NormativeDescription`). Required: whom it binds and its owner; tailoring only by relief.
- Reference model: `docs/reference-model/governance-core.md`.

## Source and mapping
- Combination strategy §4 directive row; Combination strategy §3 planning artefacts.
- Vocabulary card: directive [a binding rule].
- Combination strategy: governance-kernel `docs/project/2026-09-26-mito-s3-nasa-combination-strategy.md`.

Admitted: AK task 6147, 2026-09-27
