---
ont:
  id: "core.WorkItemAuthoritySplit"
  type: concept
  labels: ["work-item authority split"]
  synonyms: ["operational vs planning split"]
  description: "The separation between the record that drives execution, an AK task, and every planning or derived record about work (direction rows, FCOS coordination rows, plans, generated files), which never drives execution."
  relations:
    - type: is_a
      target: core.Invariant
    - type: depends_on
      target: core.WorkItem
    - type: instance_of
      target: core.UfoCategory.NormativeDescription
  examples:
    - "An agent takes its next step from `ak task ready`, not from a plan document or an FCOS board row."
  anti_examples:
    - "Reading a generated work-items file or an FCOS board row as the queue"
    - "Treating a completed direction node as proof that the work was done"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# work-item authority split (core.WorkItemAuthoritySplit)

## Definition
The separation between the record that drives execution, an AK task, and every planning or derived record about work (direction rows, FCOS coordination rows, plans, generated files), which never drives execution.

## Typical usage
- Deciding which record about a piece of work has effect at runtime.
- Keeping planning and coordination records from being read as the queue.

## Common confusions
- FCOS rows coordinate across repos and cannot be claimed; they are not tasks.
- Direction rows link to tasks; they are not tasks, and a finished node does not prove finished work.
- Work-items JSON files were projections of AK and are retired (AK 5805); none of them was ever the queue.

## Category
- UFO normative description (`core.UfoCategory.NormativeDescription`): an invariant that holds for every company.

## Source and mapping
- Moved from the holdingco company layer, where it was `co.holding.WorkItemAuthoritySplit` (holdingco/ontology `src/reference/concepts/co.holding.WorkItemAuthoritySplit.md`, last changed in `5315a69`). Reworded at the owner's direction (AK evidence 13099): the old text named a scheduler that reads L0 FCOS work items, an arrangement that is archived.
- Decision note: `ontology/decisions/2026-10-03-holding-meaning-to-core.md`.

Admitted: AK task 6592, 2026-10-03
