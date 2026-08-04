---
summary: "Quarantined ontology candidate bytes retained outside the active ROCS source corpus after owner rejection."
read_when:
  - "When investigating why a reviewed ontology candidate is absent from active ROCS retrieval"
  - "When verifying the disposition of core.AgentExperience"
type: "reference"
---

# Rejected ontology candidates

This directory preserves exact candidate bytes for audit and review without placing them under the active `ontology/src/` source root.

Files here are **not admitted ontology**, are not ROCS source documents, and must not be cited as current core semantics. A successful read or checksum of a file here proves only custody of the reviewed candidate bytes.

## `core.AgentExperience.md.candidate`

- Disposition: rejected for core admission; routed to owner-local terminology and read-only projection pilots.
- Original active-source-relative path: `ontology/src/reference/concepts/core.AgentExperience.md`.
- Preserved SHA-256: `297441bf8dbdd14736183488742fcf4b5b36ce5036039bc4935744a3263bbe12`.
- Semantic review: [`../2026-08-04-core-AgentExperience-semantic-review.md`](../2026-08-04-core-AgentExperience-semantic-review.md).
- Grand architecture review: [`../2026-08-04-agent-experience-grand-architecture-review.md`](../2026-08-04-agent-experience-grand-architecture-review.md).
- Custody action: AK task `4654`.

Restoring this file into `ontology/src/` would make it part of that exact filesystem corpus. Such a restoration is not admission and requires a new ontology-owner decision.
