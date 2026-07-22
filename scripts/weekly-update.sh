#!/usr/bin/env bash
# Weekly-update helper for ai-agent-map.
#
#   scripts/weekly-update.sh check
#       Fetch current stars and print the gain table vs the last snapshot.
#       Read-only — does NOT touch snapshot.json or any doc. Use this to drive
#       the editorial heat-table refresh.
#
#   scripts/weekly-update.sh publish "<commit message>"
#       The push gate. Stamps the snapshot (+ history raw), records the README
#       heat table into history, regenerates the rankings tables and both trend
#       SVGs, THEN runs the full validation check. ONLY if validation passes is
#       anything committed and pushed. On failure the regenerated files stay in
#       the working tree for inspection, but nothing is committed or pushed.
#
# The publish path enforces the rule: a push happens only after the full
# integrity check passes. Generation runs before validation because validate.py
# cross-checks the generated artifacts (history window vs README, SVG freshness).
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

    echo "==> Stamping snapshot + history raw…"
    python3 scripts/fetch-stars.py --write >/dev/null

    echo "==> Recording README heat table into history…"
    python3 scripts/append-history.py

    echo "==> Regenerating rankings tables…"
    python3 scripts/render-rankings.py

    echo "==> Rerendering trend charts…"
    python3 scripts/render-trend.py

    echo "==> Rerendering composition charts…"
    python3 scripts/render-composition.py

    echo "==> Running full validation (gate)…"
    if ! python3 scripts/validate.py; then
      echo "==> Validation FAILED — aborting, nothing committed or pushed." >&2
      echo "==> Regenerated files are left in the working tree for inspection." >&2
      exit 1
    fi

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
