#!/usr/bin/env python3
"""Full repository integrity check — the gate that must pass before any push.

Checks, in order:
  1. Internal markdown links resolve to a real file (relative links only;
     http(s)/anchors/mailto are skipped).
  2. Bilingual parity: every EN doc under agents/, comparisons/, use-cases/ has
     a matching mirror under zh/<same path>, and vice versa.
  3. Heat tables across the four index files agree on one "Last updated" date.
  4. Each heat table has 10 ranked rows (#1..#10) with no duplicate ranks.
  5. No leftover TODO/PLACEHOLDER/FIXME markers in tracked markdown.

Exit code 0 = clean, 1 = at least one failure. Run from the repo root.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MIRRORED_DIRS = ["agents", "comparisons", "use-cases"]
HEAT_FILES = ["README.md", "zh/README.md", "agents/README.md", "zh/agents/README.md"]

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


def check_heat():
    dates = {}
    for rel in HEAT_FILES:
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
        ranks = [int(RANK_RE.match(ln).group(1)) for ln in lines if RANK_RE.match(ln)]
        ranks = ranks[:10] if len(ranks) >= 10 else ranks
        if sorted(ranks) != list(range(1, 11)):
            errors.append(f"[heat] {rel}: expected ranks #1..#10, got {ranks}")
    if len(set(dates.values())) > 1:
        errors.append(f"[heat] 'Last updated' dates disagree across files: {dates}")


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
    check_heat()
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
