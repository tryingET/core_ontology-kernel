# ontology-kernel (Holding shared)

This repository contains the **Core (shared) ontology** and **System4D baseline** for the whole holding.

## SOP references
For process docs and SOPs that need ontology concepts, follow the reference block convention:
`holdingco/org-handbook/docs/org/processes/ontology-references.md`.

## Repo hygiene
If a file named `NUL` appears in the repo root, delete it and do not commit it (typically a stray Windows artifact).

- `ontology/src/system4d.yaml` — baseline constraints/boundaries/risks
- `ontology/src/reference/` — core concepts/relations definitions (minimal + stable)
- `ontology/dist/` — generated artifacts (created by tooling)

This repo should change slowly and be versioned with tags.
