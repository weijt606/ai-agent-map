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

## Steps

1. **Fetch the data.**
   ```
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

5. **Publish (gated).**
   ```
   scripts/weekly-update.sh publish "Refresh weekly heat ranking (YYYY-MM-DD): <headline>"
   ```
   This runs `scripts/validate.py` first. If validation fails, it aborts and
   pushes nothing — fix the errors and re-run. If it passes, it stamps the new
   snapshot, commits, and pushes.

## What validation checks (`scripts/validate.py`)

- Internal markdown links resolve to real files.
- Bilingual parity: every EN doc under agents/ comparisons/ use-cases/ has a zh
  mirror and vice versa.
- All four heat tables share one `Last updated` date.
- Each heat table has ranks #1..#10 with no duplicates.
- No leftover TODO/FIXME/PLACEHOLDER markers (warning only).

## Commit message convention

`Refresh weekly heat ranking (YYYY-MM-DD): <one-line headline>` — matching the
existing git history. Do **not** add a Claude co-author trailer.
