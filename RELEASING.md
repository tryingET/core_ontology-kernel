# Releasing `ontology-kernel`

Goal: stable, reproducible meaning.

Rules:
- All dependent manifests must pin the kernel by a release tag governed as immutable; the full
  commit OID remains the durable handoff identity (avoid `@main`).
- Cross-owner Git handoffs must name a full commit OID and an exact `refs/heads/*` or
  `refs/tags/*` transport ref. Verify that live observation from the receiving checkout:
  ```bash
  python3 scripts/verify_commit_handoff.py \
    --repo . --remote <explicit-remote> --ref <fully-qualified-ref> \
    --commit <full-commit-oid>
  ```
  The ref and remote are transport inputs, not authority. The verifier permits SSH, HTTPS
  without embedded credentials, and local paths used by tests; it rejects plaintext HTTP/Git
  transport. A successful observation does not establish semantic release, publication
  authority, adoption, or AK evidence.
- Kernel changes are MR-only; no silent redefines.
- Meaning change = new `ont.id` + mark old one deprecated + decision reference.

Release steps:
1) Merge approved MRs to `main`.
2) Select the full merge commit OID explicitly and verify this checkout is at that exact commit:
   ```bash
   release_oid=<full-commit-oid>
   test "$(git rev-parse --verify 'HEAD^{commit}')" = "$release_oid"
   ```
3) Run the repository gate: `ROCS_CI_PROFILE=main-strict ./scripts/ci/full.sh`.
4) Create `vX.Y.Z` at `"$release_oid"` (SemVer; breaking meaning changes bump MAJOR).
5) Push the exact tag refspec to each intended remote; do not use an ambient `git push`.
6) Run `scripts/verify_commit_handoff.py` for the live `refs/tags/vX.Y.Z` on each remote.

