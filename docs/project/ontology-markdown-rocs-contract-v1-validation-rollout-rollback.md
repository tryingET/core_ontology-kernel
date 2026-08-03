---
summary: "Validation, rollout, and rollback contract for Decision 110 implementation."
read_when:
  - "When validating, releasing, adopting, or rolling back ontology Markdown / ROCS contract v1."
type: "procedure"
---

# Ontology Markdown / ROCS contract v1 — validation, rollout, rollback

## ROCS validation

Required before package release:

```bash
uv run --frozen python -m unittest discover -s tests -p 'test_*.py' -q
./scripts/ci/full.sh
```

Focused evidence must cover:

- all accepted tracked kernel documents after guidance relocation;
- malformed UTF-8/frontmatter/YAML, duplicate keys, aliases/merges/tags, limits, paths, IDs, lifecycle, references, and placeholders;
- selector-off legacy behavior and selector-on v1 behavior;
- every interpreting command named by the ADR/RFC;
- raw `context.create` custody followed by mandatory downstream admission;
- complete-success versus partial/resource-exhausted conformance claims;
- schema-3 receipt mutation, missing/extra path, source-commit, lock, and digest failures.

## Package rollout

- release only after the ROCS implementation task is complete and evidenced;
- version/tag/lock/source commit must read back consistently;
- verify the produced materialization before handing its receipt to the kernel;
- no remote publication or push is implied by local tag/evidence.

## Kernel acceptance

From a clean detached worktree or clone whose parent has no sibling `core/rocs-cli` checkout and with `ROCS_WORKSPACE_ROOT` unset:

```bash
./scripts/ci/full.sh
```

The gate must verify vendored hashes and exercise validate, build, summary, lint, graph, inverse checks, normalize no-write behavior, unbound pack, development-runtime discover, bound pack, route, and the generated hook. ROCS package tests cover diff and disposable transaction paths.

Also run:

```bash
node ~/ai-society/core/agent-scripts/scripts/docs-list.mjs --docs docs --strict
```

## Rollout stop conditions

Stop before kernel commit if:

- any guidance bytes change beyond YAML nesting/indentation;
- any selector-off ROCS regression appears;
- any operation emits corpus conformance on partial/rejected/resource-exhausted input;
- the gate resolves a sibling checkout;
- receipt source, lock, complete files, or digest do not agree;
- Python/Unicode discovery runtime is incompatible.

## Rollback

Before package release, abandon/revert the candidate ROCS implementation.

After release but before kernel adoption, do not vendor the candidate.

After kernel adoption:

1. revert the kernel adoption/corpus commit;
2. restore the prior complete vendored tree and CI entrypoint;
3. repin to the prior exact materialization receipt;
4. issue a forward corrective ROCS release if the package itself is defective.

Never roll back to an unpinned sibling workspace dependency. Rollback does not alter Decision 53, semantic publication, adoption, activation, or currentness facts.
