# AGENTS.md (Core)

Always start with the compiled bundle, not raw sources.

Preferred:
- `rocs build --repo .` (produces `ontology/dist/summary.json`)
- `rocs summary --repo .`
- `rocs pack core.Secret --repo .`

Do not load all concept files into context.

GitLab (NAS):
- API (issues/MRs/etc): `gl-nas -- <gitlab-cli args...>`
- Git (clone/fetch/push): `gl-nas-git -- <git args...>`
- Reference: `holdingco/governance-kernel/docs/dev/gitlab-access.md`
