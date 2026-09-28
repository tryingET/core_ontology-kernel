---
summary: "Decision note for the governance-core splits of 2026-09-27 (AK 5987): each overloaded kernel concept, its successors with their UFO categories, the successor named in replaced_by, and what consumers change."
read_when:
  - "When a record, relation or doc still uses core.Verification, core.Consent, core.Role, core.Capability or core.Evidence"
type: "decision"
---

# Governance-core splits, 2026-09-27

**Decision:** AK task 5987, authorized by the Holding Owner (AK evidence 11150; ADR-0008 §4, class C, because core.Consent and core.Role are reserved identifiers). Driver: each concept below named two categories at once (for consent, the word named both a state and the round that reaches it), which UFO calls construct overload and which lets two parties agree on a word while meaning different things (controlled-vocabulary adjudication, school 7).

Under CORE-INV-002 the old identifiers are deprecated, never deleted, and every meaning gets a new identifier. ontology-markdown-v1 allows one `replaced_by`; it names the successor that keeps the main meaning, and this note lists every successor (ADR-0008 §7).

| Deprecated | Successors | replaced_by |
|---|---|---|
| `core.Verification` | verification (core.VerificationEvent) and verification verdict (core.VerificationVerdict) | `core.VerificationEvent` |
| `core.Consent` | consent (core.ConsentState) and consent round (core.ConsentRound) | `core.ConsentState` |
| `core.Role` | role (core.SocialRole) and permission (core.Permission) | `core.SocialRole` |
| `core.Capability` | capability (core.ActorCapability) and permission (core.Permission) | `core.ActorCapability` |
| `core.Evidence` | evidence (core.EvidenceRole) and retained artefact (core.RetainedArtefact) | `core.EvidenceRole` |

- **core.Verification**, "the act and outcome": the check is an event; its verdict is a situation a later check can supersede.
- **core.Consent**, "a governance state": consent is the situation a round reaches; the round is an event with its own record.
- **core.Role** and **core.Capability**, both "role/permission" or "ability/permission": a role is played within a relation; a permission is what a party may do (UFO-L); a capability is what it can do.
- **core.Evidence**: evidence is a role a record plays for one claim; the digest-bound, provenance-bearing record is a retained artefact.
- **core.Claim** is not split: it is the asserted content (a UFO proposition) and now says it is neither an AK task claim nor a UFO claim; the synonym "assertion" is added.

**Consumers:**
- The FCOS layer's `fcos.TestTiers` narrows core.Verification and should point to core.VerificationEvent; that is the FCOS pilot holder's change.
- Kernel edges moved in this change: core.Claim precedes core.VerificationEvent; core.Authority constrains core.VerificationEvent.
- Prose in other repos keeps working, because the preferred words (verification, consent, role, capability, evidence) did not change; only their identifiers did.
- Consumers pinned to kernel v0.2.0 see no change until they repin.
