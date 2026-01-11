---
ont:
  id: "core.WorkItem"
  type: concept
  labels: ["WorkItem"]
  synonyms: ["Work Item"]
  description: "A trackable unit of work with scope, owner(s), status, and exit criteria (planning primitive)."
  relations: []
  examples:
    - "A GitLab issue representing one mergeable slice"
    - "A milestone wrapper that groups issues"
  anti_examples:
    - "A vague aspiration with no acceptance criteria"
system4d:
  fog:
    risks: []
    assumptions: []
    exceptions: []
    debt: []
---

# WorkItem (core.WorkItem)

## Definition
A trackable unit of work with scope, owner(s), status, and exit criteria.

## Typical usage
- Planning primitive for proposals, slices, milestones, and programs.

## Common confusions
- Confused with runtime dependency (`core.rel.depends_on`). Planning dependencies use `core.rel.depends_on_plan`.

