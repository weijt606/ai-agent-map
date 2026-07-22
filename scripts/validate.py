#!/usr/bin/env python3
"""Full repository integrity check — the gate that must pass before any push.

Checks, in order:
  1. Internal markdown links resolve to a real file (relative links only;
     http(s)/anchors/mailto are skipped).
  2. Bilingual parity: every EN doc under agents/, comparisons/, use-cases/,
     rankings/ has a matching mirror under zh/<same path>, and vice versa.
  3. All dated files (four heat READMEs + six rankings docs) agree on one
     "Last updated" date.
  4. Ranked tables are well-formed: consecutive rank rows form a block, and
     every block must run #1..#N with no gaps or duplicates. The four heat
     READMEs must additionally open with an exactly-#1..#10 block.
  5. scripts/history.json cross-check: the latest window matches the README
     heat table row for row (slug, stars to 0.1k tolerance, gain), window
     dates strictly increase, ranks run 1..depth, every slug has a
     scripts/catalog.json entry, and both trend SVGs carry the latest date.
  6. No leftover TODO/PLACEHOLDER/FIXME markers in tracked markdown
     (warning only).

Exit code 0 = clean, 1 = at least one failure. Run from the repo root.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIRRORED_DIRS = ["agents", "comparisons", "use-cases", "rankings"]
HEAT_FILES = ["README.md", "zh/README.md", "agents/README.md", "zh/agents/README.md"]
RANKINGS_FILES = [
    "rankings/README.md", "rankings/agent-verticals.md", "rankings/skill-verticals.md",
    "zh/rankings/README.md", "zh/rankings/agent-verticals.md", "zh/rankings/skill-verticals.md",
]
TREND_SVGS = [
    "assets/heat-trend-en.svg", "assets/heat-trend-zh.svg",
    "assets/heat-composition-en.svg", "assets/heat-composition-zh.svg",
]
HISTORY = os.path.join(ROOT, "scripts", "history.json")
CATALOG = os.path.join(ROOT, "scripts", "catalog.json")

errors = []
warnings = []


def md_files(base):
    for dirpath, _dirs, files in os.walk(base):
        if "/.git" in dirpath:
            continue
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(dirpath, f)


LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def check_links():
    for path in md_files(ROOT):
        rel = os.path.relpath(path, ROOT)
        if rel.startswith(".git"):
            continue
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        for target in LINK_RE.findall(text):
            target = target.strip()
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = target.split("#", 1)[0].strip()
            if not target:
                continue
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            resolved = os.path.normpath(os.path.join(os.path.dirname(path), target))
            if not os.path.exists(resolved):
                errors.append(f"[link] {rel}: broken link -> {target}")


def check_parity():
    for d in MIRRORED_DIRS:
        en_dir = os.path.join(ROOT, d)
        zh_dir = os.path.join(ROOT, "zh", d)
        if not os.path.isdir(en_dir):
            continue
        en = {os.path.relpath(p, en_dir) for p in md_files(en_dir)}
        zh = {os.path.relpath(p, zh_dir) for p in md_files(zh_dir)} if os.path.isdir(zh_dir) else set()
        for missing in sorted(en - zh):
            errors.append(f"[parity] zh/{d}/{missing} missing (EN exists)")
        for extra in sorted(zh - en):
            errors.append(f"[parity] {d}/{extra} missing (zh exists)")


DATE_RE = re.compile(r"(?:Last updated|最后更新)[:：*]*\s*(\d{4}-\d{2}-\d{2})")
RANK_RE = re.compile(r"^\|\s*#(\d+)")


def rank_blocks(lines):
    """Group adjacent ranked table rows into blocks; any other line breaks a block."""
    block = []
    for ln in lines:
        m = RANK_RE.match(ln)
        if m:
            block.append(int(m.group(1)))
        elif block:
            yield block
            block = []
    if block:
        yield block


def check_heat():
    dates = {}
    for rel in HEAT_FILES + RANKINGS_FILES:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            errors.append(f"[heat] missing file {rel}")
            continue
        with open(path, encoding="utf-8") as fh:
            lines = fh.readlines()
        m = DATE_RE.search("".join(lines))
        if not m:
            errors.append(f"[heat] {rel}: no 'Last updated' date found")
        else:
            dates[rel] = m.group(1)
        blocks = list(rank_blocks(lines))
        for i, b in enumerate(blocks, 1):
            if b != list(range(1, len(b) + 1)):
                errors.append(f"[rank] {rel}: table {i} is not consecutive #1..#N: {b}")
        if rel in HEAT_FILES and (not blocks or len(blocks[0]) != 10):
            got = len(blocks[0]) if blocks else 0
            errors.append(f"[heat] {rel}: first heat table must have exactly ranks #1..#10, got {got} rows")
    if len(set(dates.values())) > 1:
        errors.append(f"[heat] 'Last updated' dates disagree across files: {dates}")
    return next(iter(dates.values()), None)


SLUG_RE = re.compile(r"https://github\.com/([\w.-]+/[\w.-]+)")
STARS_K_RE = re.compile(r"^([\d.]+)k$")
GAIN_CELL_RE = re.compile(r"^~?\+([\d,]+)$")


def readme_top10():
    """Parse the first ranked block of README.md into (slug, stars, gain) rows."""
    rows = []
    with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as fh:
        in_block = False
        for line in fh:
            if not RANK_RE.match(line):
                if in_block:
                    break
                continue
            in_block = True
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 4:
                errors.append(f"[history] malformed README heat row: {line.strip()[:60]}")
                return []
            sm = SLUG_RE.search(cells[1])
            st = STARS_K_RE.match(cells[2])
            gm = GAIN_CELL_RE.match(cells[3].replace("&nbsp;", ""))
            if not (sm and st and gm):
                errors.append(f"[history] unparseable README heat row: {line.strip()[:60]}")
                return []
            rows.append((sm.group(1).lower(), int(round(float(st.group(1)) * 1000)),
                         int(gm.group(1).replace(",", ""))))
    return rows


def check_history(heat_date):
    try:
        with open(HISTORY, encoding="utf-8") as fh:
            hist = json.load(fh)
        with open(CATALOG, encoding="utf-8") as fh:
            catalog = json.load(fh)
    except (OSError, json.JSONDecodeError) as e:
        errors.append(f"[history] cannot read history/catalog: {e}")
        return

    windows = hist.get("windows", [])
    if not windows:
        errors.append("[history] history.json has no windows")
        return

    prev = None
    for w in windows:
        if prev is not None and w["date"] <= prev:
            errors.append(f"[history] window dates not strictly increasing at {w['date']}")
        prev = w["date"]
        ranks = [e["rank"] for e in w["entries"]]
        if ranks != list(range(1, w.get("depth", len(ranks)) + 1)):
            errors.append(f"[history] window {w['date']}: ranks are not 1..depth: {ranks}")
        for e in w["entries"]:
            if e["slug"] not in catalog:
                errors.append(f"[history] window {w['date']}: slug {e['slug']} missing from catalog.json")

    latest = windows[-1]
    if heat_date and latest["date"] != heat_date:
        errors.append(f"[history] latest window date {latest['date']} != heat 'Last updated' {heat_date}")

    rows = readme_top10()
    if rows:
        if len(rows) != len(latest["entries"]):
            errors.append(f"[history] README has {len(rows)} heat rows but latest window has {len(latest['entries'])}")
        for (slug, stars, gain), entry in zip(rows, latest["entries"]):
            if slug != entry["slug"]:
                errors.append(f"[history] rank #{entry['rank']}: README slug {slug} != history {entry['slug']}")
                continue
            if abs(entry["stars"] - stars) >= 100:
                errors.append(f"[history] {slug}: README stars ~{stars} vs history {entry['stars']} (beyond 0.1k tolerance)")
            if entry["gain"] != gain:
                errors.append(f"[history] {slug}: README gain {gain} != history {entry['gain']}")

    for rel in TREND_SVGS:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            errors.append(f"[svg] missing {rel}")
            continue
        with open(path, encoding="utf-8") as fh:
            if latest["date"] not in fh.read():
                errors.append(f"[svg] {rel} is stale: does not mention latest window date {latest['date']} — rerun render-trend.py")


PLACEHOLDER_RE = re.compile(r"\b(TODO|FIXME|PLACEHOLDER|XXX|TBD)\b")


def check_placeholders():
    for path in md_files(ROOT):
        rel = os.path.relpath(path, ROOT)
        with open(path, encoding="utf-8") as fh:
            for i, line in enumerate(fh, 1):
                if PLACEHOLDER_RE.search(line):
                    warnings.append(f"[placeholder] {rel}:{i}: {line.strip()[:80]}")


def main():
    check_links()
    check_parity()
    heat_date = check_heat()
    check_history(heat_date)
    check_placeholders()

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"FAIL  {e}")

    if errors:
        print(f"\n✗ validation failed: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"\n✓ validation passed ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
