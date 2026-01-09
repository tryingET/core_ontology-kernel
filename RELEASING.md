# Releasing `ontology-kernel`

Goal: stable, reproducible meaning.

Rules:
- All dependent manifests must pin the kernel by tag (avoid `@main`).
- Kernel changes are MR-only; no silent redefines.
- Meaning change = new `ont.id` + mark old one deprecated + decision reference.

Release steps:
1) Merge approved MRs to `main`.
2) Run validation: `rocs validate --repo . --strict-placeholders`
3) Tag: `vX.Y.Z` (SemVer; breaking meaning changes bump MAJOR).
4) Push tag.

