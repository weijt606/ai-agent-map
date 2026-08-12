#!/usr/bin/env python3
"""Fetch current GitHub star counts for every repo in tracked-repos.txt.

Reads the previous snapshot from scripts/snapshot.json (if present), fetches the
current star count for each tracked slug via the public GitHub API, and prints a
gain table sorted by 7-day gain. With --write it also rewrites snapshot.json so
the next run can compute deltas, and appends the full snapshot (stars + gain per
repo) to the `raw` section of scripts/history.json, which feeds the category
rankings under rankings/. Same-date re-runs overwrite the raw entry (idempotent).

Read mode vs write mode, and why the cache exists
-------------------------------------------------
The weekly flow is: `check` (read mode) prints the numbers you hand-write into
the heat tables, then `publish` (--write) stamps them. When --write re-fetched
independently, stars moved between the two calls and the stamped snapshot no
longer matched the hand-written tables — a drift of 2-37 stars that recurred
every week and forced a manual reconciliation pass afterwards.

So read mode now records what it saw in scripts/.fetch-cache.json, and --write
reuses that same-day cache instead of re-fetching. Same numbers in the tables
and in the snapshot, by construction.

- Slugs added to tracked-repos.txt between the two calls (the playbook's
  "pending pickup" step does exactly this) are simply not in the cache, so they
  are fetched individually and merged in — the rest is still reused.
- A cache from an earlier date is ignored as stale.
- --refetch forces a fresh fetch and bypasses the cache entirely.

Used both for the manual weekly refresh and by the automated Wednesday routine.
Auth: set GITHUB_TOKEN in the environment to lift the 60 req/hr unauthenticated
limit (the script works without it for <60 repos).
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(HERE, "tracked-repos.txt")
SNAPSHOT = os.path.join(HERE, "snapshot.json")
HISTORY = os.path.join(HERE, "history.json")
CACHE = os.path.join(HERE, ".fetch-cache.json")


def slugs():
    out = []
    with open(MANIFEST) as fh:
        for line in fh:
            line = line.split("#", 1)[0].strip()
            if line:
                out.append(line.split()[0])
    return out


def fetch(slug):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{slug}",
        headers={"Accept": "application/vnd.github+json",
                 "User-Agent": "ai-agent-map-bot"},
    )
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        req.add_header("Authorization", f"Bearer {tok}")
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                d = json.load(r)
                return {
                    "full_name": d.get("full_name", slug),
                    "stars": d.get("stargazers_count"),
                }
        except urllib.error.HTTPError as e:
            if e.code == 403 and attempt < 2:  # rate limit, back off
                time.sleep(5)
                continue
            return {"full_name": slug, "stars": None, "error": str(e)}
        except Exception as e:  # noqa: BLE001
            return {"full_name": slug, "stars": None, "error": str(e)}
    return {"full_name": slug, "stars": None, "error": "retries exhausted"}


def load_cache(today):
    """Return {key: {full_name, stars}} from a same-day cache, else {}.

    A cache from any other date is stale and ignored; an unreadable or
    malformed cache is treated as absent rather than fatal, since the only
    cost of missing it is a re-fetch.
    """
    if not os.path.exists(CACHE):
        return {}, None
    try:
        with open(CACHE, encoding="utf-8") as fh:
            blob = json.load(fh)
    except (OSError, json.JSONDecodeError):
        return {}, None
    if blob.get("date") != today:
        return {}, None
    repos = blob.get("repos")
    if not isinstance(repos, dict):
        return {}, None
    return repos, blob.get("fetched_at")


def save_cache(today, current):
    """Record this fetch so a later --write can reuse it verbatim."""
    blob = {
        "_comment": "Written by fetch-stars.py read mode; reused by --write on "
                    "the same date so the stamped snapshot matches the numbers "
                    "the heat tables were written from. Safe to delete.",
        "date": today,
        "fetched_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "repos": current,
    }
    try:
        with open(CACHE, "w", encoding="utf-8") as fh:
            json.dump(blob, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
    except OSError as e:  # non-fatal: the fetch itself already succeeded
        print(f"note: could not write {CACHE}: {e}", file=sys.stderr)


def main():
    write = "--write" in sys.argv
    refetch = "--refetch" in sys.argv
    today = time.strftime("%Y-%m-%d")
    prev = {}
    if os.path.exists(SNAPSHOT):
        with open(SNAPSHOT) as fh:
            blob = json.load(fh)
            prev = {k: v for k, v in blob.get("repos", {}).items()}

    # --write reuses the fetch that read mode already recorded today, so the
    # stamped snapshot cannot drift from the hand-written heat tables.
    cached, fetched_at = ({}, None) if refetch else load_cache(today)
    reuse = bool(cached) and write
    # Status goes to stderr so publish can silence the gain table but still
    # surface which fetch it stamped.
    if write:
        if refetch:
            print("--refetch: ignoring any cached fetch, hitting the API fresh.",
                  file=sys.stderr)
        elif reuse:
            print(f"reusing the check fetch from {fetched_at} "
                  f"({len(cached)} repos cached) — no re-fetch, so no drift.",
                  file=sys.stderr)
        else:
            print("WARNING: no same-day check cache found, fetching fresh.\n"
                  "         Stars may have moved since you wrote the heat tables;\n"
                  "         reconcile the tables against the stamped snapshot after.",
                  file=sys.stderr)

    rows = []
    current = {}
    refetched = 0
    for slug in slugs():
        key = slug.lower()
        hit = cached.get(key) if reuse else None
        if hit and isinstance(hit.get("stars"), int):
            info = {"full_name": hit.get("full_name", slug), "stars": hit["stars"]}
        else:
            info = fetch(slug)
            if reuse:
                refetched += 1
        stars = info["stars"]
        prev_stars = prev.get(key, {}).get("stars") if isinstance(prev.get(key), dict) else prev.get(key)
        gain = (stars - prev_stars) if (stars is not None and isinstance(prev_stars, (int, float))) else None
        rows.append((slug, stars, prev_stars, gain, info.get("error")))
        if stars is not None:
            current[key] = {"full_name": info["full_name"], "stars": stars}

    rows.sort(key=lambda r: (r[3] is None, -(r[3] or 0)))
    print(f"{'repo':40} {'stars':>10} {'prev':>10} {'gain':>10}")
    print("-" * 74)
    for slug, stars, prev_stars, gain, err in rows:
        s = f"{stars:,}" if isinstance(stars, int) else "ERR"
        p = f"{prev_stars:,}" if isinstance(prev_stars, (int, float)) else "-"
        g = f"{gain:+,}" if isinstance(gain, (int, float)) else "-"
        line = f"{slug:40} {s:>10} {p:>10} {g:>10}"
        if err:
            line += f"  ({err})"
        print(line)

    if reuse and refetched:
        print(f"{refetched} slug(s) were not in the cache (added to "
              f"tracked-repos.txt after the check run) and were fetched now.",
              file=sys.stderr)

    if not write:
        save_cache(today, current)

    if write:
        append_raw(today, rows)
        out = {"updated": today, "repos": current}
        with open(SNAPSHOT, "w") as fh:
            json.dump(out, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(f"\nwrote {SNAPSHOT} ({len(current)} repos)")


def append_raw(date, rows):
    """Append today's full snapshot to history.json's raw section.

    Runs BEFORE snapshot.json is overwritten so gains are relative to the
    previous snapshot. Fails hard: a publish must not proceed with a broken
    or missing history file.
    """
    try:
        with open(HISTORY, encoding="utf-8") as fh:
            hist = json.load(fh)
    except (OSError, json.JSONDecodeError) as e:
        print(f"ERROR: cannot read {HISTORY}: {e}", file=sys.stderr)
        sys.exit(1)
    stars = {}
    for slug, cur, _prev, gain, err in rows:
        if cur is None:
            continue
        stars[slug.lower()] = {"stars": cur, "gain": gain}
    entry = {"date": date, "stars": stars}
    raw = [r for r in hist.setdefault("raw", []) if r.get("date") != date]
    raw.append(entry)
    hist["raw"] = raw
    with open(HISTORY, "w", encoding="utf-8") as fh:
        json.dump(hist, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    print(f"appended raw snapshot for {date} to history.json ({len(stars)} repos)")


if __name__ == "__main__":
    main()
