#!/usr/bin/env python3
"""Append the current README heat table to history.json's windows section.

README.md is the single source of truth for the editorial weekly top 10; this
script parses its heat table (date, snapshot window, first ranked block) and
appends the result as a new window in scripts/history.json. Re-running on the
same date overwrites that window (idempotent). validate.py cross-checks the
latest window against the README afterwards, so a divergence can never ship.

Exact star counts are taken from the same-date raw snapshot when available
(fetch-stars.py --write runs first in the publish flow); the README's
0.1k-rounded values are the fallback.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
README = os.path.join(ROOT, "README.md")
HISTORY = os.path.join(HERE, "history.json")

DATE_RE = re.compile(r"Last updated:\*\*\s*(\d{4}-\d{2}-\d{2})")
WINDOW_RE = re.compile(r"Snapshot window:\*\*\s*(\d{4}-\d{2}-\d{2})\s*→\s*(\d{4}-\d{2}-\d{2})")
RANK_ROW_RE = re.compile(r"^\|\s*#(\d+)")
SLUG_RE = re.compile(r"https://github\.com/([\w.-]+/[\w.-]+)")
STARS_RE = re.compile(r"^([\d.]+)k$")
GAIN_RE = re.compile(r"^~?\+([\d,]+)$")


def parse_readme():
    with open(README, encoding="utf-8") as fh:
        text = fh.read()
    m = DATE_RE.search(text)
    if not m:
        sys.exit("ERROR: no 'Last updated' date in README.md")
    date = m.group(1)
    w = WINDOW_RE.search(text)
    window = (w.group(1), w.group(2)) if w else (None, None)

    entries, in_block = [], False
    for line in text.splitlines():
        rm = RANK_ROW_RE.match(line)
        if not rm:
            if in_block:
                break
            continue
        in_block = True
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            sys.exit(f"ERROR: malformed heat row: {line}")
        rank = int(rm.group(1))
        sm = SLUG_RE.search(cells[1])
        if not sm:
            sys.exit(f"ERROR: no github.com link in heat row #{rank}: {cells[1]}")
        slug = sm.group(1).lower()
        st = STARS_RE.match(cells[2])
        if not st:
            sys.exit(f"ERROR: unparseable stars '{cells[2]}' in heat row #{rank}")
        stars = int(round(float(st.group(1)) * 1000))
        gm = GAIN_RE.match(cells[3].replace("&nbsp;", ""))
        if not gm:
            sys.exit(f"ERROR: unparseable gain '{cells[3]}' in heat row #{rank}")
        gain = int(gm.group(1).replace(",", ""))
        entries.append({"rank": rank, "slug": slug, "stars": stars, "gain": gain})

    if [e["rank"] for e in entries] != list(range(1, len(entries) + 1)):
        sys.exit(f"ERROR: heat table ranks not consecutive: {[e['rank'] for e in entries]}")
    if not entries:
        sys.exit("ERROR: no heat table rows found in README.md")
    return date, window, entries


def main():
    date, (start, end), entries = parse_readme()
    with open(HISTORY, encoding="utf-8") as fh:
        hist = json.load(fh)

    note = "stars approximate"
    raw_same_day = next((r for r in hist.get("raw", []) if r.get("date") == date), None)
    if raw_same_day:
        exact = 0
        for e in entries:
            info = raw_same_day["stars"].get(e["slug"])
            if info and isinstance(info.get("stars"), int):
                e["stars"] = info["stars"]
                exact += 1
        if exact == len(entries):
            note = ""

    windows = [w for w in hist["windows"] if w["date"] != date]
    if windows and date < windows[-1]["date"]:
        sys.exit(f"ERROR: README date {date} is older than the latest history window {windows[-1]['date']}")
    windows.append({
        "date": date,
        "window_start": start,
        "window_end": end,
        "source_commit": "",
        "depth": len(entries),
        "note": note,
        "entries": entries,
    })
    hist["windows"] = windows
    with open(HISTORY, "w", encoding="utf-8") as fh:
        json.dump(hist, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    print(f"history.json: window {date} recorded ({len(entries)} entries, {len(windows)} windows total)")


if __name__ == "__main__":
    main()
