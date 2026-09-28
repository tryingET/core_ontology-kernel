# AGENTS.md (Core)

Always start with the compiled bundle, not raw sources.

Preferred (`rocs` is not on PATH; the checked-in launcher verifies and runs the vendored ROCS):
- `./scripts/rocs.sh build --repo .` (produces `ontology/dist/summary.json`)
- `./scripts/rocs.sh summary --repo .`
- `./scripts/rocs.sh pack core.Secret --repo .`

Do not load all concept files into context.

Kernel changes are PR-only at `github.com/tryingET/core_ontology-kernel`. GitHub Actions runs
`ROCS_CI_PROFILE=main-strict ./scripts/ci/full.sh` on every pull request and on `main`. The NAS
GitLab is retired (AK 6118); do not push to a `gitlab-nas` remote.
