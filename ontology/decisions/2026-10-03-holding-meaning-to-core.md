---
summary: "Decision note for moving the holding's shared meaning from the holdingco company layer to core (AK 6592): core.TemplateTopology is admitted unchanged; core.WorkItemAuthoritySplit is admitted reworded, because the old text described a retired arrangement."
read_when:
  - "When a record, relation or doc uses co.holding.TemplateTopology or co.holding.WorkItemAuthoritySplit"
  - "When deciding whether a meaning belongs in the holdingco company layer or in core"
type: "decision"
---

# The holding's shared meaning goes to core, 2026-10-03

**Decision:** AK task 6592, authorized by the Holding Owner (AK evidence 13029; the rewording, 13099) through the ADR-0008 Core
Vorgabe route (§4, class C). No consent round was held: the Holding Owner holds both affected layers, core and
`holdingco/ontology` (ADR-0008 data file, holders), as for ADR-0008 itself.

**Driver.** The holdingco company layer held two concepts, both about how every company is structured, and no
others. Only holdingco's own repos load that layer (`holdingco/agents`, `holdingco/fcos-control-board`,
`holdingco/infra/template-propagator`), so the companies the concepts govern never saw them. The template gives
every company a company layer, including the holding, but the meaning the holding sets for all companies is
core meaning. Neither concept ever went through ADR-0008's promotion route; both predate it.

| Company concept | Outcome |
|---|---|
| `co.holding.TemplateTopology` | Admitted as `core.TemplateTopology`, meaning unchanged, description translated. |
| `co.holding.WorkItemAuthoritySplit` | Admitted reworded as `core.WorkItemAuthoritySplit`. The old text said a scheduler runs L0 FCOS work items while L1/L2 work items only plan; that scheduler is archived and the work-items files were retired (AK 5805). The kept meaning, at the owner's direction: only an AK task drives execution; direction rows, FCOS rows, plans and generated files never do. |

**Consumers.**
- No consumer uses either identifier in a durable text. `holdingco/fcos-control-board`
  `tests/test_fcos_vocabulary_pilot.py` uses `co.holding.TemplateTopology` as a sample string only.
- The holdingco layer records the removal in its own append-only removed-identifiers list, with
  `core.TemplateTopology` and `core.WorkItemAuthoritySplit` as the replacements, during decision 168's fold (AK 6274). The fold then imports the
  layer without these concepts.

**Rule for later.** ADR-0008 §1 item 7 (2026-10-03): a meaning the holding sets for every company is core's and
goes through the Vorgabe route; the holdingco company layer holds only meaning specific to holdingco's own repos.
