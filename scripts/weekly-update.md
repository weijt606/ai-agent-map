# Weekly update playbook (every Wednesday)

This is the standing instruction set for the automated weekly refresh of
ai-agent-map. The scheduled agent (and any human doing the update by hand)
follows these steps in order. **The hard rule: nothing is pushed unless the full
validation check passes.**

## Scope of a weekly update

Three things change every week, not just the rank:

1. **Rank** — refresh the 7-day gain heat ranking in all four index files.
2. **热点 / hot topics** — update the narrative bullets and "Market events" to
   reflect what actually drove the window (breakouts, rebrands, cool-downs).
3. **新的收录 / new inclusions** — scan GitHub for newly-trending agent repos.
   Add a profile if a project clears the in-scope bar; otherwise add it to the
   watchlist bullet and note it for next week.

Plus one **conditional** pass: the selection surfaces (capability matrix,
cost & benchmarks, memory approaches) are refreshed only when the window's
changes actually touch them — see step 5.

## Steps

1. **Fetch the data.**
   ```
   export GITHUB_TOKEN=$(gh auth token)   # required in practice: 42+ tracked repos vs 60 req/hr unauthenticated
   scripts/weekly-update.sh check
   ```
   This prints each tracked repo with its current stars, the previous snapshot
   value, and the 7-day gain. The snapshot window is the previous `snapshot.json`
   `updated` date → today.

2. **Refresh the rank** in all four heat tables. Keep them in lockstep:
   - `README.md` — "Recent Heat Ranking"
   - `zh/README.md` — "近期热度排名"
   - `agents/README.md` — "Recent Heat Snapshot"
   - `zh/agents/README.md` — "近期热门快照"

   Rules: top 10 by gain; rank-change arrows (↑/↓/new) vs last week; stars
   rounded to 0.1k; update the `Last updated` date and `Snapshot window` line in
   every table to the same date. Update the "continuing to grow" / off-table
   bullet and the OpenClaw line.

   The rankings/ boards, the history file, and the trend charts are regenerated
   automatically by `publish` — do **not** hand-edit anything between
   `<!-- auto:... -->` markers in rankings/ files or the SVGs in assets/. Do give
   the editorial prose in rankings/ (the trend read-out, section intros) a quick
   look in case the story has moved on.

3. **Update hot topics.** Rewrite the narrative bullets under each table and add
   a dated "Market events" entry for anything structural (a breakout, a rebrand,
   an acquisition, a wave re-broadening/cooling). EN and zh must say the same
   thing.

4. **Scan for new inclusions.** Search for recently-created trending repos, e.g.:
   ```
   curl -s "https://api.github.com/search/repositories?q=coding+agent+cli+created:>YYYY-MM-DD&sort=stars&order=desc&per_page=8"
   ```
   (also try `ai+agent+terminal`, `claude+skills`). For any genuinely new
   in-scope agent surface, write a bilingual profile (`agents/<name>.md` +
   `zh/agents/<name>.md`), add its slug to `scripts/tracked-repos.txt`, and wire
   it into the route/coverage tables per the file checklist in project memory.
   If nothing clears the bar, add the best candidates to the watchlist bullet and
   record them for next week.

   **Every slug added to `tracked-repos.txt` needs a matching entry in
   `scripts/catalog.json`** (display name, category agent/infra/skill, vertical,
   infra group, profile path, scope) — `render-rankings.py` fails hard on a
   tracked repo with no metadata.

5. **Sync the selection surfaces (conditional — skip when nothing applies).**
   These pages are hand-maintained; they only change when the window produced a
   matching event:
   - **New in-scope profile** → add a scored row to `capabilities/matrix.md` ×2
     in its route group (●/◐/○/— per the legend), and mention it in the group's
     "Standouts" line if it changes the story.
   - **New profile with memory as a headline feature** → wire it into the right
     section of `comparisons/memory-approaches.md` ×2.
   - **Model-layer event** (new model/tier, price change, new benchmark number
     recorded in market-events) → refresh the affected rows in
     `comparisons/cost-and-benchmarks.md` ×2, including the "as of" month in
     its note line.
   - Keep the rule from the profiles: only numbers already established
     elsewhere in the map (vendor profiles, market-events) go into
     cost-and-benchmarks — never invent a figure during a routine refresh.

6. **Publish (gated).**
   ```
   scripts/weekly-update.sh publish "Refresh weekly heat ranking (YYYY-MM-DD): <headline>"
   ```
   This stamps the snapshot (+ appends the full fetch to `history.json` raw),
   records the README heat table as the week's history window, regenerates the
   rankings/ tables and both trend SVGs, then runs `scripts/validate.py`. If
   validation fails, nothing is committed or pushed — the regenerated files stay
   in the working tree; fix the errors and re-run. Every generation step is
   idempotent for the same date.

## What validation checks (`scripts/validate.py`)

- Internal markdown links resolve to real files.
- Bilingual parity: every EN doc under agents/ comparisons/ use-cases/ rankings/
  has a zh mirror and vice versa.
- All dated files (four heat tables + six rankings docs) share one
  `Last updated` date.
- Every ranked table block is consecutive #1..#N; the four heat tables must
  open with exactly #1..#10.
- `history.json` cross-check: the latest window matches the README heat table
  row for row (slug / stars / gain), window dates strictly increase, every slug
  has a catalog.json entry, and both trend SVGs carry the latest window date.
- No leftover TODO/FIXME/PLACEHOLDER markers (warning only).

## Commit message convention

`Refresh weekly heat ranking (YYYY-MM-DD): <one-line headline>` — matching the
existing git history. Do **not** add a Claude co-author trailer.
