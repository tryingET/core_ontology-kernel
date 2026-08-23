---
summary: "Pre-merge v0.2.0 release-preparation candidate for AK task 4881."
read_when:
  - "Reviewing or executing the bounded ontology-kernel v0.2.0 release preparation."
type: evidence
status: candidate
task_id: 4881
---

# Ontology-kernel v0.2.0 release preparation

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

The AK 4881 PR sequence requires an externally supplied, AK-reviewed, 40-hex `CANDIDATE_OID`
and asserts local `HEAD` equals it; `HEAD` does not supply its own authority. The fail-closed
procedure in [`RELEASING.md`](../../RELEASING.md) also proves the assessment base is an ancestor of
live `origin/main`, binds the live merge base and exact three-path PR diff, and requires exact review
ref `refs/heads/release/ontology-kernel-v0.2.0-prep` absent. Only then may later parent execution
make one non-force exact-OID push to the origin URL. Exactly one live
`candidate_oid<TAB>candidate_ref` line must be observed before PR creation. Absence, mismatch,
duplication, lookup failure, or any earlier failure requires revised authority; no silent retry,
rebase, or amend is allowed. This candidate does not execute that publication procedure.

## Post-merge release procedure

After review and merge to `main`, select the full reviewed merge OID, use a clean checkout at that
OID, rerun the strict repository and docs gates, and follow the complete procedure in
`RELEASING.md`. Before tag creation, owner evidence for each destination must record repository
URL, ruleset/control identity, observation time, matching ref/pattern, enforcement, protected
update/deletion operations, bypasses, and owner acceptance. Missing, stale, inaccessible,
ambiguous, or unaccepted evidence fails closed.

Only then may the executor create the annotated `v0.2.0` tag, push exact
`refs/tags/v0.2.0:refs/tags/v0.2.0` refspecs to both named URLs, and assert exactly one live direct
line equals the local annotated tag-object OID and exactly one peeled line equals the release OID.
`verify_commit_handoff.py` remains an additional mandatory OID-only check. Lookup/transport/auth
failure is never tag absence.

Before each release push, its URL is added to a duplicate-checked `attempted` array. On any push
or verification failure, every attempted URL—including an indeterminate failed-push URL—is queried
immediately and classified as exact direct-plus-peeled match, absent, mismatch, or unavailable;
push return code never implies publication state. Stop and preserve those observations and exact
local OIDs. Do not delete or move the tag. Resumption requires fresh owner authority and fresh
protection/current-state checks for exact matches plus protection/absence checks for absent
locations; mismatch or unavailable state remains stopped. Authority may permit only identical-tag
publication to a missing destination or a separately authorized forward corrective release.

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

Before merge, prove the reviewed candidate is not an ancestor of live `origin/main`, close and
verify closure of the AK 4881 PR, and require the live review branch equals the same externally
supplied `CANDIDATE_OID`. Deletion is compare-and-swap only, using
`--force-with-lease="${candidate_ref}:${candidate_oid}"` with the deletion refspec scoped to exact
branch `refs/heads/release/ontology-kernel-v0.2.0-prep`; a fresh query must return `2` absence. The
lease/force never applies to `main` or tags. Any failed proof stops for revised authority; do not
retry, silently rebase/amend, or delete another ref.

After a partial publication, do not delete or move any published tag. Preserve exact observations,
stop, and follow the fresh-authority/protection/absence/current-state recovery rules above.
Preserve AK and Git evidence in every case.

## Nonclaims

This artifact does not claim exact-final-candidate validation, final-OID selection, review, merge,
server protection, tag creation, publication, destination parity, consumer adoption, activation,
use, or AK completion. It grants no permission to mutate remotes, tags, branches, PRs, or AK state.
