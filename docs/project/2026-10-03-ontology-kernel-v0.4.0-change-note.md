---
summary: "Change note for the ontology-kernel v0.4.0 candidate (AK 6364): decision-record vocabulary, the decision class, in-place readings, the semantic delta against v0.3.0, and consumer handoffs."
read_when:
  - "Before repinning a consumer from ontology-kernel v0.3.0 to v0.4.0."
  - "When checking the decision-record vocabulary and its consumer handoffs."
type: "reference"
task_id: 6364
---

# ontology-kernel v0.4.0 change note

AK 6364 carries the ontology questions from AK 5991's decision records. This is the local v0.4.0
preparation candidate. Consent round 12306 closed early under the owner's ruling 12461, with no
objection standing (receipt 12462). Final content authorization and the PR are pending.
The release follows [docs/release-procedure.md](../release-procedure.md).

## Content

- The raised argument is `core.PossibleObjection`. If it qualifies, it is a `core.Objection`; a
  failed argument may reveal a `core.Concern`, which never blocks consent.
- A `core.Decision` is the intention a deliberation creates. `core.Deliberation` is the act of
  deciding. Authorization, refusal and revocation manifest the decision.
- `core.Refusal` and `core.Revocation` have their own identifiers. Revocation covers permissions
  and delegated authority.
- `core.DecisionClass` classifies the three class roles, each a subtype of `core.Proposal`.
  Reserved scope is class C first. A classified proposal holds exactly one role; an unclassified
  proposal holds none, and no decision on it may go ahead. `core.ConsentTier` remains the path tier.
- DecisionClass specialises UFO Role because its instances are role types. HighOrderType identifies
  that its instances are types (ruling 12461).
- A decision gate remains a deliberation. Its diagnostic names the decision formed against
  criteria set in advance (ruling 12461).
- A possible objection may be withdrawn before its test. A failed test remains on record without
  an objection end state. A qualified objection ends integrated, withdrawn or standing.
- Dissent exists after a decision goes ahead over a standing objection, including a revocation.
- One decision record may document several decisions in order, each with its own deliberation
  and resulting action, if any.
- A permission may end at a time its authorization states. An agreement review date ends nothing.

The decision note is [ontology/decisions/2026-10-02-decision-records-questions.md](../../ontology/decisions/2026-10-02-decision-records-questions.md).

## Semantic delta against v0.3.0

`rocs diff --baseline '<repo:core/ontology-kernel@v0.3.0>' --resolve-refs --workspace-ref-mode strict`
(consumer rocs-cli 0.4.6) exits 0:

- Concepts: 11 added, none removed; 113 → 124.
- Relation types: `core.rel.manifests` added, none removed; 12 → 13.
- Edges: 29 added, none removed; 103 → 132.
  - By type: 14 `instance_of`, 6 `is_a`, 4 `depends_on`, 3 `manifests`, 1 `produces`, 1 `precedes`.
- Candidate corpus digest: `sha256:67d55411209af6c4d77a58f6ecaa0826d2d6ca318dbe32deea1c433f12f3d06d`.

New concepts: `core.PossibleObjection`, `core.Concern`, `core.Decision`, `core.Deliberation`,
`core.Refusal`, `core.Revocation`, `core.DecisionClass`, `core.ClassAChange`, `core.ClassBChange`,
`core.ClassCChange` and `core.UfoCategory.HighOrderType`.

Added concepts, a relation type and edges make this a minor version under
[RELEASING.md](../../RELEASING.md). This prep sets `ontology/manifest.yaml` to `0.4.0`.
`ontology/dist` is generated and ignored by git; it is rebuilt by the acceptance check.

## In-place readings and deprecations

No new deprecation is proposed. The owner has ruled on in-place readings for `core.Objection`,
`core.ConsentRound`, `core.Dissent` and `core.Permission` (evidence 12209 and 12211). Final
authorization must explicitly cover the narrowing of ConsentRound's end-state text and the
extension of DecisionRecord's Required line to each decision in order (ruling 12346).
Deliberation's wording “a decider” and the proposed 2027-04-01 review date are also disclosed in
the final authorization request.

The five v0.3.0 deprecations remain resolvable with their existing successors and decision references:

| Deprecated | Successors | replaced_by |
|---|---|---|
| `core.Verification` | `core.VerificationEvent`, `core.VerificationVerdict` | `core.VerificationEvent` |
| `core.Consent` | `core.ConsentState`, `core.ConsentRound` | `core.ConsentState` |
| `core.Role` | `core.SocialRole`, `core.Permission` | `core.SocialRole` |
| `core.Capability` | `core.ActorCapability`, `core.Permission` | `core.ActorCapability` |
| `core.Evidence` | `core.EvidenceRole`, `core.RetainedArtefact` | `core.EvidenceRole` |

Decision note: [2026-09-27-governance-core-splits.md](../../ontology/decisions/2026-09-27-governance-core-splits.md).

## Consumers

- Agent Kernel: AK 6471 amends dormant migration 47 and its disposition grid before AK 6367's live
  apply. Raised arguments key to `core.PossibleObjection`; acts key to Authorization, Refusal or
  Revocation. AK 6453 carries the ontology pin and checks that its constants resolve. AK 6366
  carries classification and outcome checks; AK 6368 carries decision-record fields.
- FCOS: adoption is forward, in new record versions. Existing version-1 records, signed facts and
  archived inputs retain their validators. In new records, failed possible objections are kept
  with their test result and have no dissent entry. `not_after` is the end the grant states.
  Which FCOS entity plays `core.Proposal` remains its owner's concern from the consent round.
- Governance-kernel: its owner reserves the new identifiers and core words and distinguishes
  escalated objections before a decision from dissent after it.
- Org-handbook: consent-tier SOPs keep `core.ConsentTier`; decision-class wording follows the new
  class concepts.
- Company and repo layers: repin under ADR-0008 §7 and the standing decision AK 6288 after the
  version is published, with each consumer's own check and adoption evidence.

## Checks and limits

The exact candidate commit, acceptance commands and results are recorded on AK 6364.
The fidelity check accounts for all twelve findings against `1204635` (evidence 12396); the two
remaining semantic points are now ruled in 12461. Conformance receipts check the source contract,
schema and references; the owner and work-product inspection judge meaning.

Publication authority and consumer adoption remain their own records. The remaining consumer
concerns need authoritative handoffs before 6364 completes; the preparation checkpoint records
those handoffs and any remaining permission.

