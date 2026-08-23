---
summary: "Pre-merge v0.2.0 release-preparation candidate for AK task 4881."
read_when:
  - "Reviewing or executing the bounded ontology-kernel v0.2.0 release preparation."
type: evidence
status: candidate
task_id: 4881
---

# Ontology-kernel v0.2.0 release preparation

## Later procedure correction

AK `4890` later recorded GitHub PR `#2` merged at
`d50c7ef8127afc7967db6d025287d2c69ea2858e` without a tag or Release. AK `4905` then found that
the tag-first procedure preserved in pre-correction merge commit
`d50c7ef8127afc7967db6d025287d2c69ea2858e` could not satisfy its own pre-creation protection
gate for the private origin, where repository rulesets were unavailable. The current canonical
[`RELEASING.md`](../../RELEASING.md) supersedes that flow with owner-evidenced GitHub Release
immutability, separately authorized draft preparation, separately authorized publication, and
post-publication attestation plus exact tag/OID verification.

This note does not retroactively turn this historical AK `4881` candidate into release authority,
select a final release OID, or claim that either repository setting is enabled. The correction
itself changes the eventual release OID and must merge and pass exact-OID gates before any draft is
prepared.

## Scope and exact anchors

AK task `4881` authorizes only a pre-merge candidate changing the manifest version, release
procedure, and this record. The exact candidate base is
`3e6c9f39c8cecc5feb509ead2022361d3c5f3ec1`. The exact corpus assessed by AK task `4880` is
`e5efc3b8a818ac4f592d0b369d7e1bf718057f0e`; its assessment was committed in the candidate base.
The final release OID is intentionally unset until this candidate is reviewed and merged to
`main`.

This preparation changes `rocs.version` from `0.1.0` to `0.2.0` and makes no ontology meaning or
source change. At the base and in this candidate, `ontology/src` has Git tree OID
`266409404a9570ab4bfe48002f91d1bdef0e5764`.

## Decisions and pre-merge posture

- Version: `v0.2.0`, matching manifest `rocs.version: "0.2.0"`.
- Complete destination set: exactly `https://github.com/tryingET/ontology-kernel.git` and
  `https://github.com/tryingET/core_ontology-kernel.git`.
- NAS is not required for `v0.2.0` and is excluded. Remote aliases are not authority.
- OIDs are durable content identities. Tag refs are described only as currently protected against
  update/deletion under time-bounded, recorded, owner-accepted controls—not permanently immutable.
- This is not a final release OID, release authorization, tag, publication, or readiness/adoption
  claim.

At candidate commit `e3951cce8137a94fdcb7dccb80ff18c2cf6da57d`, the AK `4881` PR
sequence required an externally supplied, AK-reviewed, 40-hex `CANDIDATE_OID` and asserted local
`HEAD` equaled it; `HEAD` did not supply its own authority. The pre-correction runbook preserved at
merge commit `d50c7ef8127afc7967db6d025287d2c69ea2858e` proved the assessment base was an ancestor
of live `origin/main`, bound the live merge base and exact three-path PR diff, and required exact
review ref `refs/heads/release/ontology-kernel-v0.2.0-prep` absent before one non-force exact-OID
push. Exactly one live `candidate_oid<TAB>candidate_ref` line had to be observed before PR
creation. AK `4890` records that sequence completed; the current `RELEASING.md` intentionally does
not retain it as executable current guidance.

## Post-merge release procedure

After this correction is reviewed and merged to `main`, select that resulting full OID, use a clean
checkout at the exact commit, rerun the strict repository and docs gates, and follow
`RELEASING.md`. Before any draft, both exact GitHub `main` refs must equal the release OID and an
owner must record current **Enable release immutability** receipts from each repository's
**Settings → General → Releases** control. The repository switch was not exposed by the supported
REST/GraphQL surfaces observed in AK `4905`; it must not be inferred from ruleset capability or
from a draft's expected `immutable: false` value.

A draft-preparation task may then create exactly one fixed-title, fixed-body, empty-asset draft for
`v0.2.0` at each destination. It must record both numeric draft IDs, exact body digest, full target
OID, and whether GitHub left the draft tag absent or created the expected unprotected lightweight
ref. Draft preparation is not publication. A separate publication task must bind those exact
drafts, fresh setting receipts, publication order, an exclusive writer window, and explicit
acceptance of the non-atomic check/publish race.

Publication changes each exact draft to published state through GitHub's Release API; it does not
create or push a local annotated tag. Success requires a fresh Release response with `draft:
false`, `immutable: true`, the authorized numeric ID/content/target and no assets; one live
lightweight `refs/tags/v0.2.0` line equal to the full release OID; a successful
`verify_commit_handoff.py` check; and a successful `gh release verify v0.2.0` signed-attestation
check at **both** repositories.

On any draft or publication command failure, query both numeric Release IDs, authenticated
matching-Release lists, both `main` refs, and both tag refs; do not infer state from return code or
retry a mutation mechanically. Bounded read-only polling may resolve propagation delay without
repeating publication. A verified immutable Release may remain while fresh authority permits
publishing the already prepared exact draft at the other repository. A nonimmutable, mismatched,
changed, or cryptographically invalid published state requires a forward corrective release. Never
move or delete a published tag, and do not publish the second destination after the first fails
verification.

## Preliminary implementation-time validation

These are implementation-time checks, not authoritative receipts for the exact final amended
commit. Earlier candidate-worktree runs of
`ROCS_CI_PROFILE=main-strict ./scripts/ci/full.sh` and
`node ~/ai-society/core/agent-scripts/scripts/docs-list.mjs --docs docs --strict` exited `0` on
2026-08-23; their bounded logs were recorded during implementation. This artifact is part of the
bytes that determine the commit OID, so it cannot honestly contain an exact-final-candidate receipt
that names that OID. After the final amend, the parent must run both gates against the exact commit
and record authoritative command/OID/results receipts in AK. No result in this section substitutes
for that post-commit AK evidence.

## Rollback

The original pre-merge rollback is historical: AK `4890` records the candidate merged, so PR
closure or review-branch deletion cannot roll back `main`. Any source rollback now requires a
separate reviewed revert while preserving AK and Git history; it would change the prospective
release OID and invalidate every prior exact-OID gate or draft.

A draft remains unprotected and is not safe to delete or edit merely because publication has not
occurred. Preserve exact draft/tag observations and obtain separate cleanup authority. After any
publication attempt, do not delete or move a published tag or Release. Preserve exact observations
and follow the forward-only recovery rules in `RELEASING.md`; GitHub documents that an immutable
Release's tag name cannot be reused even if the Release is deleted.

## Nonclaims

The original AK `4881` evidence made no exact-final-candidate, final-OID, server-protection, tag,
publication, destination-parity, adoption, activation, or use claim. The later note records AK
`4890`'s merge fact but does not itself establish release readiness or grant mutation authority.
This artifact grants no permission to mutate remotes, tags, Releases, settings, branches, PRs, or
AK state.
