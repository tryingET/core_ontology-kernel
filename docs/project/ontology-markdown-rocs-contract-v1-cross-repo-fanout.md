---
summary: "Coordination-only owner-repo task fanout for Decision 110."
read_when:
  - "When materializing or auditing Decision 110 execution tasks."
type: "coordination"
fanout_mode: "coordination_only"
---

# Decision 110 — cross-repo fanout

## Boundary

This pack decomposes one accepted cross-repo decision into owner-local AK tasks. It is coordination only. AK tasks remain execution authority; each repository owns its commits and validation.

## Owner sequence

1. ROCS implementation and tests.
2. ROCS package-owner release, dependent on implementation evidence.
3. Ontology-kernel adoption, dependent on the exact released materialization.

## Machine-readable fan-out manifest

```yaml
fanout_manifest:
  schema_version: 1
  mode: coordination_only
  tasks:
    - task_key: rocs_source_contract_v1
      repo: /home/tryinget/ai-society/core/rocs-cli
      title: "Decision 110: implement ontology-markdown-v1 conformance"
      description: |
        Implement the accepted opt-in source parser/dispatcher, operation-qualified
        source-contract conformance, raw context.create custody boundary, schema-3
        exact materialization receipts, and complete legacy/v1 tests. Do not release
        or claim semantic publication/adoption in this task.

    - task_key: rocs_package_0_3_0
      repo: /home/tryinget/ai-society/core/rocs-cli
      title: "Decision 110: release rocs-cli 0.3.0 after conformance evidence"
      description: |
        After the implementation task passes all owner gates, apply the separately
        authorized package release, update the lock, commit/tag the exact release,
        and produce the exact materialization receipt for ontology-kernel. This is
        package-owner work, not semantic publication or consumer adoption.

    - task_key: ontology_kernel_adoption
      repo: /home/tryinget/ai-society/core/ontology-kernel
      title: "Decision 110: adopt ontology-markdown-v1 and vendored ROCS 0.3.0"
      description: |
        After the ROCS release task, relocate relation guidance without content
        change, update schema docs and manifest/profile/request fixtures, converge
        as required, vendor the exact receipt and bytes, rewire CI, and prove the
        clean no-sibling gate. Keep untracked core.AgentExperience.md out of scope.
```

## Exact post-ADR materialization protocol

Run only after the ADR, implementation plan, validation/rollout/rollback, and this fanout are committed and attached to Decision 110.

### 1. Dry-run and materialize

```bash
ak decision materialize-fanout 110 \
  --artifact-ref docs/project/ontology-markdown-rocs-contract-v1-cross-repo-fanout.md \
  --dry-run -F json

ak decision materialize-fanout 110 \
  --artifact-ref docs/project/ontology-markdown-rocs-contract-v1-cross-repo-fanout.md \
  -F json > "$TMPDIR/decision-110-fanout.json"

A=$(jq -r '.tasks[] | select(.task_key=="rocs_source_contract_v1") | .task_id' "$TMPDIR/decision-110-fanout.json")
B=$(jq -r '.tasks[] | select(.task_key=="rocs_package_0_3_0") | .task_id' "$TMPDIR/decision-110-fanout.json")
C=$(jq -r '.tasks[] | select(.task_key=="ontology_kernel_adoption") | .task_id' "$TMPDIR/decision-110-fanout.json")
```

### 2. Set exact scopes

```bash
ak task scope set "$A" \
  --allowed 'src/rocs_cli/**' --allowed 'tests/**' --allowed 'README.md' --allowed 'docs/project/**' \
  --required 'src/rocs_cli/source_contract.py' --required 'tests/test_source_contract_v1.py' \
  --forbidden 'pyproject.toml' --forbidden 'uv.lock'

ak task scope set "$B" \
  --allowed 'pyproject.toml' --allowed 'uv.lock' --allowed 'src/rocs_cli/__init__.py' --allowed 'docs/project/**' \
  --required 'pyproject.toml' --required 'uv.lock' --required 'src/rocs_cli/__init__.py' \
  --forbidden 'src/rocs_cli/source_contract.py'

ak task scope set "$C" \
  --allowed '.gitlab-ci.yml' --allowed '.githooks/**' --allowed 'scripts/ci/full.sh' --allowed 'scripts/rocs.sh' \
  --allowed 'tools/rocs-cli/**' --allowed 'ontology/manifest.yaml' \
  --allowed 'ontology/src/reference/relations/*.md' --allowed 'docs/ontology-schema.md' --allowed 'tests/fixtures/**' \
  --required '.gitlab-ci.yml' --required 'scripts/ci/full.sh' \
  --required 'tools/rocs-cli/VENDORED_HASHES.json' --required 'ontology/manifest.yaml' --required 'docs/ontology-schema.md' \
  --forbidden 'ontology/src/reference/concepts/core.AgentExperience.md'
```

### 3. Set done contracts and guardrails

```bash
ak task contract set-done "$A" --completion-kind implementation_verified \
  --outcome 'one shared opt-in parser/dispatcher serves every interpreting command' \
  --outcome 'legacy selector-off behavior remains covered' \
  --outcome 'schema-3 materialization receipt and operation-qualified conformance are tested' \
  --validation "uv run --frozen python -m unittest discover -s tests -p 'test_*.py' -q" \
  --validation './scripts/ci/full.sh' \
  --evidence-class command --evidence-class artifact --expect-version 0
ak task contract set-guardrails "$A" \
  --invariant 'maximum claim is operation-qualified source-contract/schema/reference conformance' \
  --invariant 'context.create remains raw custody and downstream interpretation re-admits' \
  --anti-goal 'no package release, semantic publication, Decision 53 adapter, or source-format selection' \
  --rollback-boundary 'revert implementation commit before package release' --expect-version 0

ak task contract set-done "$B" --completion-kind package_release \
  --outcome 'version and lock read back as 0.3.0' \
  --outcome 'immutable package commit/tag and exact materialization receipt are produced' \
  --validation 'uv run --frozen python -m rocs_cli release plan --version 0.3.0' \
  --validation "uv run --frozen python -m unittest discover -s tests -p 'test_*.py' -q" \
  --evidence-class command --evidence-class artifact --expect-version 0
ak task contract set-guardrails "$B" \
  --invariant 'package release is not semantic publication or consumer adoption' \
  --constraint 'begin only after task A is complete' \
  --anti-goal 'do not rewrite a published tag or claim canonical cross-builder bytes' \
  --rollback-boundary 'forward corrective release after publication' --expect-version 0

ak task contract set-done "$C" --completion-kind consumer_adoption_verified \
  --outcome 'relation guidance relocates without list-item or prose changes' \
  --outcome 'kernel opts in through kernel-v1 and pins the exact ROCS materialization' \
  --outcome 'CI and generated gate pass without a sibling ROCS checkout' \
  --validation './scripts/ci/full.sh' \
  --validation 'node ~/ai-society/core/agent-scripts/scripts/docs-list.mjs --docs docs --strict' \
  --evidence-class command --evidence-class artifact --expect-version 0
ak task contract set-guardrails "$C" \
  --invariant 'untracked core.AgentExperience.md remains untouched and uncommitted' \
  --invariant 'Decision 53 and source-format nonclaims remain unchanged' \
  --constraint 'begin only after task B is complete' \
  --anti-goal 'no sibling-workspace CI dependency, relation-ID migration, evaluator, or editor integration' \
  --rollback-boundary 'revert adoption commit and restore the prior complete vendored pin' --expect-version 0
```

### 4. Add dependencies and links

```bash
ak task add-deps "$B" --deps "$A"
ak task add-deps "$C" --deps "$B"

ak decision link-task 110 "$A" --role post_adr_execution
ak decision link-task 110 "$B" --role post_adr_execution
ak decision link-task 110 "$C" --role post_adr_execution

ak direction link-task -r /home/tryinget/ai-society/core/rocs-cli IW7 "$A" --role execution_task
ak direction link-task -r /home/tryinget/ai-society/core/rocs-cli IW7 "$B" --role execution_task
ak direction link-task -r /home/tryinget/ai-society/core/ontology-kernel IW1 "$C" --role execution_task
```

### 5. Complete decision gating

```bash
ak decision advance 110 --state adr_recorded \
  --adr-ref docs/adr/2026-08-03-ontology-markdown-rocs-contract-v1.md \
  --actor pi-session-019fc622
ak decision advance 110 --state tasks_reevaluation_pending --actor pi-session-019fc622
ak decision reevaluate-task 110 "$A" --status still_valid --note 'owner-local ROCS implementation required by accepted ADR'
ak decision reevaluate-task 110 "$B" --status still_valid --note 'separate package-owner release remains required after implementation'
ak decision reevaluate-task 110 "$C" --status still_valid --note 'kernel adoption remains required after exact package materialization'
ak decision advance 110 --state unblocked --actor pi-session-019fc622
```

Read back Decision 110, all three tasks' scopes/contracts/guardrails/dependencies, and both direction graphs before claiming task A. Claim and complete in A → B → C order; never claim a dependent task early.
