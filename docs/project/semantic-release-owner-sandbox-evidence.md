---
summary: "Task 3988 evidence for Decision 53 semantic-owner sandbox contracts and independently replayable owner-store read receipts."
read_when:
  - "Reviewing or integrating the Decision 53 semantic-owner sandbox slice."
type: "evidence"
status: "candidate_evidence"
---
# Decision 53 Semantic-Owner Sandbox Evidence

## Authority and scope

- AK task: `3988`
- AK decision: `53`
- Candidate base: `78fd2212189ceeab844f7e737a521fd6d17c90ea`
- Owner repository: `core/ontology-kernel`
- Accepted ADR: `/home/tryinget/ai-society/core/rocs-cli/docs/adr/2026-07-13-semantic-release-and-single-canary-adoption.md`
- Accepted plans: `semantic-release-implementation-plan.md`, `semantic-release-validation-rollout-rollback.md`, and `semantic-release-cross-repo-fanout.md` in `core/rocs-cli/docs/project/`

This evidence covers only the I3 disposable semantic-owner sandbox. It is not a semantic release, live acquisition capability, owner approval for production, production publication, or consumer adoption. AK task/evidence completion remains with the controller.

## Implemented contract

`scripts/semantic_owner_sandbox.py` deterministically produces and validates:

1. namespace policy and owner predicate;
2. compatibility decision;
3. lifecycle decision with deprecation, removal, and permanent tombstone posture;
4. fixture-only trust rotation and revocation state with no key material;
5. non-authorizing sandbox release approval;
6. append-only sandbox publication, withdrawal, and revocation history whose production head is explicitly absent.

Every artifact is bound to the `ai-society.core.sandbox.task-3988` namespace, `disposable_sandbox` environment, ontology-kernel repository identity, and `semantic_owner` issuer. Every artifact says `non_authorizing=true` and `production_state_mutated=false`.

The fixture acquisition path emits protocol-v0 `semantic-owner-acquisition-capability-pin.v0` and `semantic-owner-store-read-receipt.v0` objects. Receipts bind the exact store head, revision, trust-revocation head, role, fact digest, acquisition contract/distribution, closed fixture epoch, and capability pin. The CLI has no filesystem-output operation: generate/acquire emit JSON to stdout, while validate/replay only read through a required root and no-follow descriptor walk.

The closed invariant remains:

```text
live_acquisition_implemented=false
```

## Committed fixture inventory

| Path | SHA-256 |
|---|---|
| `tests/fixtures/semantic-owner-sandbox/acquisition-request.json` | `88ad6d9f15d156ab3de785ecd4ddb88833ef346a71aa8e7748fd859d1fd5339e` |
| `tests/fixtures/semantic-owner-sandbox/owner-store.json` | `829fa5b83a5aa0c703fddc4b86a63e19b69693218981f2c26953999c45ab1fb8` |
| `tests/fixtures/semantic-owner-sandbox/expected-receipts.json` | `3f528dbdc9d8f222ceffaf623c18ec80d178582a5c5a05ad9cf9f39a52d0db07` |

The fixtures regenerate byte-identically from the checked-in script. The store has six owner roles, six capability pins, and six read receipts.

## Validation evidence

Observed in the isolated candidate worktree on 2026-07-17:

| Command | Observed result |
|---|---|
| `./scripts/rocs.sh contracts` | exit `0`; schema-3 command/effect contract emitted before unfamiliar ROCS use |
| `./scripts/rocs.sh validate --repo .` | exit `0`; `rocs validate: OK` |
| `python3 -I -B -m unittest discover -s tests -p 'test_*.py' -v` | exit `0`; 10 focused tests passed |
| `./scripts/ci/full.sh` | exit `0`; ROCS validation and all 10 tests passed |
| `python3 -m py_compile scripts/semantic_owner_sandbox.py tests/test_semantic_owner_sandbox.py` | exit `0` |
| `git diff --cached --check` | exit `0` on the exact independently reviewed stage |

The focused tests prove deterministic regeneration, complete six-role coverage, ontology-kernel-only issuance, sandbox/non-authorization flags, append-only publication-state fixtures, exact receipt replay, rejection of live acquisition, foreign issuers, stale/future/unknown requests, digest/replay tampering, fully rehashed production-authority drift, duplicate JSON keys, and final/intermediate symlink escape. They also exercise the stdout-only CLI and compare `ontology/src` and `ontology/dist` before and after acquisition.

### Sanitized disposable dogfood

A disposable `/tmp/d53-3988-dogfood.*` root received only the sandbox script and the three fixtures. Under `env -i`, fixed system `PATH`, isolated Python (`-I -B`), empty disposable `HOME`, and `PYTHONNOUSERSITE=1`:

- receipt replay passed;
- fresh fixture values emitted to stdout passed;
- shell-captured values for all three fixtures matched the committed fixtures byte-for-byte with `cmp`;
- the tool itself created no file and the disposable root contained no unexpected file;
- the root was removed after the run.

Observed result: `sanitized dogfood: PASS (read-only replay plus byte-identical stdout generation; temp root removed)`.

### ROCS Decision 53 compatibility dogfood

The accepted post-task-3986 ROCS runtime at `/home/tryinget/ai-society/core/rocs-cli` validated every emitted pin and read receipt with `rocs_cli.semantic_release_protocol.validate_object`.

Observed result: `ROCS Decision 53 runtime compatibility: PASS (12 pin/receipt objects)`.

This compatibility run validates schema and recursive digest compatibility; it does not promote the fixtures into current owner authority.

Fixture currentness is deliberately closed to the exact committed store head, store revision `1`, trust-revocation artifact digest, action epoch `1`, and complete six-role request. Both older and newer epochs or any self-consistent store drift fail the fixture validator. This is deterministic sandbox currentness only; live/action-time owner currentness remains deferred behind G1 with `live_acquisition_implemented=false`.

## Non-mutation and baseline evidence

Before and after focused tests, full gate, and dogfood:

- `ontology/src` tree digest: `d2249a7f7b00ea81cc13499c239063e9c228939a8d14c4ee425f186c774640c2` across 46 files;
- `ontology/dist` tree digest: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` across 0 files;
- `uv.lock`: absent at the candidate base and not created;
- no network locator, private key, secret, production key, production publication head, or live acquisition path is present in the fixtures;
- no `tools/rocs-cli/**`, `.gitlab-ci.yml`, canonical ontology source, AK state, production store, or parent-worktree file was changed.

## Independent review

A read-only independent reviewer inspected the exact staged diff and adversarially exercised it. The first passes identified and blocked acceptance on self-consistent production-authority drift, intermediate symlink escape/output mutation, and JSON boolean-versus-integer currentness drift. The implementation then closed each role/store/request to type-aware canonical fixture equality, replaced output paths with stdout-only emission, added descriptor-relative no-follow reads for every path component, and added regression tests.

Final rereview outcome: **PASS**, dispatch lineage `dispatch-1784300690898`.

1. All semantic-owner facts are issued only by ontology-kernel within the closed sandbox fixture; issuer and owner-repository drift fail validation.
2. Canonical ontology and production publication state are untouched; no staged canonical/forbidden path exists and the CLI has no filesystem-output operation.
3. Receipts replay independently and fail closed on issuer, deterministic sandbox currentness/type, path, digest, store, and fully rehashed production-authority drift.

The reviewer explicitly limited this result to deterministic sandbox currentness, not live or production authority. Reviewer execution did not mutate the candidate worktree. The exact commit is recorded in the candidate report after the commit gate.

### Controller adversarial follow-up

Post-peer inspection found one additional Python-specific replay hazard: ordinary object equality treats `True == 1`, so a digest-valid expected bundle with boolean drift in integer currentness fields could compare equal. The candidate now validates bounded I-JSON and compares canonical type-aware bytes during bundle replay. Regression coverage replaces the bundle action epoch, a receipt store revision, and a pin action-epoch floor with booleans; all three must fail replay. A fresh independent rereview of this correction is required before AK closure.

The sandbox script is intentionally a single disposable-copy tool and exceeds the workspace's 500-LOC readability preference. Treat this as a candidate-scoped exception for I3 portability only: split it before any proposal for live acquisition or production owner-store use. The current exception grants no live or production authority.

## Rollback and integration caveats

Rollback is a revert of the single bounded candidate commit. The fixture tool has no live or production state to compensate. Preserve AK history and all parent concurrent work.

The dirty parent currently has untracked `scripts/`, a modified `.gitlab-ci.yml`, a new `core.AgentExperience` concept, and deleted `tools/rocs-cli/**`. This candidate did not inspect, overwrite, or absorb that work. Because this slice adds `scripts/rocs.sh` and `scripts/ci/full.sh` against base `78fd221`, the controller must reconcile those paths and the parent's planned ROCS-tool deletion before cherry-pick. The wrappers are task-local acceptance plumbing, not authority to restore deleted vendored files.

Legal next action: controller inspection/cherry-pick only after parent-path reconciliation. Live acquisition, production publication, and AK completion remain separately owned and gated.
