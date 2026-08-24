# ontology-kernel (Holding shared)

This repository contains the **Core (shared) ontology** and **System4D baseline** for the whole holding.

## Product direction

- [Vision](docs/project/vision.md) — durable purpose, intended experience, and hard scope.
- [Product posture](docs/project/product_posture.md) — current maturity, evidence boundaries, and
  stewardship decisions.
- [Ontology schema](docs/ontology-schema.md) — accepted source grammar and conformance ceiling.
- [Release procedure](RELEASING.md) — protected tag/OID and publication contract.

## Local operator path

Use the checked-in wrapper so the exact vendored ROCS bundle is verified before import and Python
bytecode is not written into it:

```bash
./scripts/rocs.sh contracts
./scripts/rocs.sh summary --repo .
ROCS_CI_PROFILE=main-strict ./scripts/ci/full.sh
```

The strict gate inventories every vendored file. Ignored `__pycache__` or bytecode under
`tools/rocs-cli/` is contamination, not harmless cache state; the verifier reports exact unexpected
paths and fails before importing bundled code.

## SOP references
For process docs and SOPs that need ontology concepts, follow the reference block convention:
`holdingco/org-handbook/docs/org/processes/ontology-references.md`.

## Repo hygiene
If a file named `NUL` appears in the repo root, delete it and do not commit it (typically a stray Windows artifact).

- `ontology/src/system4d.yaml` — baseline constraints/boundaries/risks
- `ontology/src/reference/` — core concepts/relations definitions (minimal + stable)
- `ontology/dist/` — generated artifacts (created by tooling)

This repo should change slowly and be versioned with tags.
