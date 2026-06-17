#!/usr/bin/env bash
# Weekly-update helper for ai-agent-map.
#
#   scripts/weekly-update.sh check
#       Fetch current stars and print the gain table vs the last snapshot.
#       Read-only — does NOT touch snapshot.json or any doc. Use this to drive
#       the editorial heat-table refresh.
#
#   scripts/weekly-update.sh publish "<commit message>"
#       The push gate. Runs the full validation check; ONLY if it passes does it
#       stamp the snapshot, stage everything, commit, and push. If validation
#       fails, nothing is committed or pushed and the script exits non-zero.
#
# The publish path enforces the rule: a push happens only after the full
# integrity check passes.
set -euo pipefail
cd "$(dirname "$0")/.."

cmd="${1:-check}"

case "$cmd" in
  check)
    exec python3 scripts/fetch-stars.py
    ;;

  publish)
    msg="${2:-}"
    if [ -z "$msg" ]; then
      echo "usage: weekly-update.sh publish \"<commit message>\"" >&2
      exit 2
    fi

    echo "==> Running full validation (gate)…"
    if ! python3 scripts/validate.py; then
      echo "==> Validation FAILED — aborting, nothing committed or pushed." >&2
      exit 1
    fi

    echo "==> Validation passed. Stamping snapshot…"
    python3 scripts/fetch-stars.py --write >/dev/null

    if git diff --quiet && git diff --cached --quiet; then
      echo "==> No changes to commit. Done."
      exit 0
    fi

    branch="$(git rev-parse --abbrev-ref HEAD)"
    echo "==> Committing on '$branch'…"
    git add -A
    git commit -m "$msg"

    echo "==> Pushing…"
    git push origin "$branch"
    echo "==> Published."
    ;;

  *)
    echo "usage: weekly-update.sh {check|publish}" >&2
    exit 2
    ;;
esac
