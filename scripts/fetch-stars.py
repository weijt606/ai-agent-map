#!/usr/bin/env python3
"""Fetch current GitHub star counts for every repo in tracked-repos.txt.

Reads the previous snapshot from scripts/snapshot.json (if present), fetches the
current star count for each tracked slug via the public GitHub API, and prints a
gain table sorted by 7-day gain. With --write it also rewrites snapshot.json so
the next run can compute deltas.

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


def main():
    write = "--write" in sys.argv
    prev = {}
    if os.path.exists(SNAPSHOT):
        with open(SNAPSHOT) as fh:
            blob = json.load(fh)
            prev = {k: v for k, v in blob.get("repos", {}).items()}

    rows = []
    current = {}
    for slug in slugs():
        info = fetch(slug)
        stars = info["stars"]
        key = slug.lower()
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
        g = f"+{gain:,}" if isinstance(gain, (int, float)) else "-"
        line = f"{slug:40} {s:>10} {p:>10} {g:>10}"
        if err:
            line += f"  ({err})"
        print(line)

    if write:
        out = {"updated": time.strftime("%Y-%m-%d"), "repos": current}
        with open(SNAPSHOT, "w") as fh:
            json.dump(out, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(f"\nwrote {SNAPSHOT} ({len(current)} repos)")


if __name__ == "__main__":
    main()
