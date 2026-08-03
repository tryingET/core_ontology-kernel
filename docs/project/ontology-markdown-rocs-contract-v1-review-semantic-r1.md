---
summary: "Decision 110 semantic-owner and authority review attempt r1; outcome revise_rfc."
read_when:
  - "When auditing the first formal review of ontology Markdown / ROCS contract v1."
type: "review"
---

# Decision 110 — semantic-owner and authority review r1

## Immutable review binding

- reviewed commit: `56d044687ffb2815ef2e79f0d7b077c9b0123036`
- reviewed artifact: `docs/project/ontology-markdown-rocs-contract-v1-rfc.md`
- Git blob: `26960ac5a4c815907cdf32ad2e5ffab946d7760e`
- blob SHA-256: `ce1c2d3237ad47f8b046bd56833bf5776e41f45b083f58f2ec8193ac348f0ed1`
- review execution: `dispatch-1785796750506`
- track: semantic owner and authority

This review attempt is immutable for the exact binding above. Corrections require a new RFC revision and review attempt.

## Findings

### High — tracked and dirty corpus baselines were conflated

The evidence note reported 32 concepts as tracked. The reviewed commit contains 31 tracked concept documents and 12 tracked relation documents; the dirty worktree contains an additional untracked `core.AgentExperience.md`. Counts, migrations, and clean-clone acceptance must bind to the committed tree and report dirty observations separately.

### High — the closed frontmatter grammar was incomplete

The RFC did not specify delimiters, BOM/line-ending behavior, duplicate mapping keys, aliases, merge keys, tags, recursive/shared nodes, resource limits, or typed error precedence. Current ROCS validator and semantic snapshot paths parse these differently, so the RFC could not guarantee admission parity.

### High — identity, path, and lifecycle invariants were incomplete

The RFC did not close global/cross-kind ID uniqueness, concept/relation path and filename grammar, normalized path collisions, deprecation date/reference syntax, or the owner/version of suppressible advisory rules.

### High — operation identity and projection wording was ambiguous

Raw document, corpus-snapshot, and pack digest names were used without normatively binding the existing semantic-discovery v0 preimages and algorithms. The discovery row also conflated internal scoring inputs with emitted candidate fields.

### Medium — the authority ceiling needed a normative Decision 53 reference

The local nonclaim list was directionally correct but incomplete. It must incorporate the accepted Decision 53 ADR by reference and explicitly exclude desired state, semantic publication/withdrawal/revocation, consumer consent, activation/deactivation/rollback, and AK lineage facts. It must distinguish an executable ROCS package release from semantic release publication.

## Outcome

`revise_rfc`

## Legal next move

Correct the committed evidence baseline and RFC grammar/identity/projection/authority defects, commit a new RFC revision, then run new formal review attempts on both required tracks. No ADR or implementation task is legal from r1.
