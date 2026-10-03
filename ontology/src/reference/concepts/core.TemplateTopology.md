---
ont:
  id: "core.TemplateTopology"
  type: concept
  labels: ["template topology"]
  synonyms: ["L0-L1-L2 topology", "template stack"]
  description: "The binding structure of the template layers L0, L1 and L2: L0 holds the canonical templates, L1 individualises them for one company, L2 runs them in execution repos; it fixes which layer holds authority over a change, which layer generates which, and how drift between them is found."
  relations:
    - type: is_a
      target: core.Policy
    - type: instance_of
      target: core.UfoCategory.NormativeDescription
  examples:
    - "A template fix belongs in L0 and reaches L1 and L2 through a propagation wave, not through edits in each L2 repo."
  anti_examples:
    - "Editing an L2 repo directly to stand in for a missing L0 or L1 change"
    - "The ontology layers core, company and repo (a different structure)"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# template topology (core.TemplateTopology)

## Definition
The binding structure of the template layers L0, L1 and L2: L0 holds the canonical templates, L1 individualises them for one company, L2 runs them in execution repos. It fixes which layer holds authority over a change, which layer generates which, and how drift between them is found.

## Typical usage
- Deciding at which template layer a change must be made.
- Keeping generated artefacts from being treated as the canonical source.

## Common confusions
- "L1 is optional": no, L1 is the company's translation layer.
- "L2 may override L0 contracts": no, L2 is specific to its execution.
- The template layers are not the ontology layers (core, company, repo): every company has both, and they are separate structures.

## Category
- UFO normative description (`core.UfoCategory.NormativeDescription`), like its parent `core.Policy`.

## Source and mapping
- Moved from the holdingco company layer, where it was `co.holding.TemplateTopology` (holdingco/ontology `src/reference/concepts/co.holding.TemplateTopology.md`, last changed in `5315a69`). The meaning is unchanged; the description is translated from German.
- Why core: the holding sets this structure for every company, but only holdingco's repos loaded the holdingco layer, so the companies it governs never saw it.
- Decision note: `ontology/decisions/2026-10-03-holding-meaning-to-core.md`.

Admitted: AK task 6592, 2026-10-03
