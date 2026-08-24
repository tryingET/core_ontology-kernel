#!/usr/bin/env bash
set -euo pipefail

# Execute only a private snapshot copied from the exact checked-in vendored
# ROCS bundle through descriptor-relative, no-follow verification. Never import
# from the mutable source path and never write Python bytecode into either tree.
export PATH="/usr/local/bin:/usr/bin:/bin"
unset PYTHONPATH
script_dir="$(CDPATH='' cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
repo="$(CDPATH='' cd -- "$script_dir/.." && pwd -P)"
artifact="$repo/tools/rocs-cli"
python_bin=""
if command -v python3.12 >/dev/null 2>&1; then
  python_bin="$(command -v python3.12)"
elif command -v uv >/dev/null 2>&1; then
  python_bin="$(uv python find --no-project 3.12 2>/dev/null || true)"
fi
if [[ -z "$python_bin" || ! -x "$python_bin" ]]; then
  echo "ROCS requires an installed Python 3.12 interpreter" >&2
  exit 2
fi
"$python_bin" -I -S -B - <<'PY'
import sys
if sys.version_info[:2] != (3, 12):
    raise SystemExit("ROCS requires Python 3.12.x")
PY
export PYTHONDONTWRITEBYTECODE=1
scratch_root="${TMPDIR:-$(dirname -- "$repo")}"
mkdir -p -- "$scratch_root"
runtime_root="$(mktemp -d "$scratch_root/rocs-verified-runtime.XXXXXX")"
verified_artifact="$runtime_root/bundle"
cleanup() {
  rm -rf -- "$runtime_root"
}
trap cleanup EXIT HUP INT TERM
"$python_bin" -I -S -B "$repo/scripts/verify_vendored_rocs.py" \
  "$artifact" --snapshot-dir "$verified_artifact"
"$python_bin" -I -S -B "$verified_artifact/rocs.py" "$@"
