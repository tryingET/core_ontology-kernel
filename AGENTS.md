# AGENTS.md (Core)

Always start with the compiled bundle, not raw sources.

Preferred:
- `rocs build --repo .` (produces `ontology/dist/summary.json`)
- `rocs summary --repo .`
- `rocs pack core.Secret --repo .`

Do not load all concept files into context.
