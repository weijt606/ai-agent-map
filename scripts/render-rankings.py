#!/usr/bin/env python3
"""Regenerate the machine-maintained tables in the rankings/ documents.

Reads scripts/catalog.json (category / vertical / group metadata) and the
latest raw snapshot in scripts/history.json (exact stars + weekly gain), then
rewrites every block between <!-- auto:NAME --> and <!-- /auto:NAME --> markers
in the six rankings files, plus each file's "Last updated" line. Editorial
prose outside the markers is never touched — and the marked blocks must never
be edited by hand.

Boards are sorted by current total stars (the stock view), complementing the
gain-sorted heat tables on the home page. The "Last updated" date written here
is the heat date parsed from README.md, so all dated files stay in lockstep.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CATALOG = os.path.join(HERE, "catalog.json")
HISTORY = os.path.join(HERE, "history.json")

HEAT_DATE_RE = re.compile(r"Last updated:\*\*\s*(\d{4}-\d{2}-\d{2})")
DATE_LINE_RE = re.compile(r"((?:Last updated|最后更新)[:：]\*\*\s*)\d{4}-\d{2}-\d{2}")

FILES = {
    "en": ["rankings/README.md", "rankings/agent-verticals.md", "rankings/skill-verticals.md"],
    "zh": ["zh/rankings/README.md", "zh/rankings/agent-verticals.md", "zh/rankings/skill-verticals.md"],
}

VERTICAL_LABELS = {
    "en": {"coding": "Coding", "general": "General assistant", "finance": "Finance",
           "collections": "Curated collections", "research": "Academic & scientific",
           "methodology": "Methodology"},
    "zh": {"coding": "编程开发", "general": "通用助理", "finance": "金融",
           "collections": "通用技能集", "research": "学术科研",
           "methodology": "方法论"},
}
GROUP_LABELS = {
    "en": {"framework": "Framework", "orchestration": "Orchestration",
           "memory-context": "Memory & context", "gateway-runtime": "Gateway & runtime",
           "workflow": "Workflow"},
    "zh": {"framework": "框架", "orchestration": "编排",
           "memory-context": "记忆与上下文", "gateway-runtime": "网关与执行",
           "workflow": "工作流"},
}
HEADERS = {
    "en": {
        "board:agent": "| Rank | Project | Vertical | Stars | Weekly gain | Map status |\n| --- | --- | --- | --- | --- | --- |",
        "board:infra": "| Rank | Project | Group | Stars | Weekly gain | Map status |\n| --- | --- | --- | --- | --- | --- |",
        "board:skill": "| Rank | Project | Focus | Stars | Weekly gain | Map status |\n| --- | --- | --- | --- | --- | --- |",
        "vertical": "| Rank | Project | Stars | Weekly gain | Map status |\n| --- | --- | --- | --- | --- |",
    },
    "zh": {
        "board:agent": "| 排名 | 项目 | 垂类 | Stars | 本周增量 | 状态 |\n| --- | --- | --- | --- | --- | --- |",
        "board:infra": "| 排名 | 项目 | 分组 | Stars | 本周增量 | 状态 |\n| --- | --- | --- | --- | --- | --- |",
        "board:skill": "| 排名 | 项目 | 方向 | Stars | 本周增量 | 状态 |\n| --- | --- | --- | --- | --- | --- |",
        "vertical": "| 排名 | 项目 | Stars | 本周增量 | 状态 |\n| --- | --- | --- | --- | --- |",
    },
}
STATUS = {
    "en": {"in": "In scope · [profile]({profile})", "watchlist": "Watchlist", "out": "Out of scope"},
    "zh": {"in": "已收录 · [profile]({profile})", "watchlist": "候补", "out": "不收录"},
}

MARKER_RE = re.compile(r"(<!-- auto:([\w:-]+) -->\n).*?(<!-- /auto:\2 -->)", re.DOTALL)


def fmt_stars(n):
    return f"{n / 1000:.1f}k"


def fmt_gain(g):
    return f"+{g:,}" if isinstance(g, int) else "—"


def load_inputs():
    with open(CATALOG, encoding="utf-8") as fh:
        catalog = {k: v for k, v in json.load(fh).items() if not k.startswith("_")}
    with open(HISTORY, encoding="utf-8") as fh:
        hist = json.load(fh)
    if not hist.get("raw"):
        sys.exit("ERROR: history.json has no raw snapshots — run fetch-stars.py --write first")
    latest_raw = hist["raw"][-1]["stars"]
    with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as fh:
        m = HEAT_DATE_RE.search(fh.read())
    if not m:
        sys.exit("ERROR: no 'Last updated' date in README.md")
    return catalog, latest_raw, m.group(1)


def rows_for(catalog, raw, category, vertical=None, group_col=None, lang="en"):
    rows = []
    for slug, meta in catalog.items():
        if not meta.get("tracked", True) or meta["category"] != category:
            continue
        if vertical is not None and meta.get("vertical") != vertical:
            continue
        info = raw.get(slug)
        if not info:
            sys.exit(f"ERROR: tracked repo {slug} missing from the latest raw snapshot")
        rows.append((slug, meta, info["stars"], info.get("gain")))
    rows.sort(key=lambda r: -r[2])

    out = []
    for i, (slug, meta, stars, gain) in enumerate(rows, 1):
        name = meta.get("display_zh", meta["display"]) if lang == "zh" else meta["display"]
        link = f"[{name}](https://github.com/{slug})"
        status_tpl = STATUS[lang][meta["scope"]]
        profile = f"../{meta['profile']}" if meta.get("profile") else None
        status = status_tpl.format(profile=profile) if profile and meta["scope"] == "in" else \
            STATUS[lang][meta["scope"]].replace(" · [profile]({profile})", "")
        cells = [f"#{i}", link]
        if vertical is None:
            if group_col:
                cells.append(GROUP_LABELS[lang].get(meta.get("group"), "—"))
            else:
                cells.append(VERTICAL_LABELS[lang].get(meta.get("vertical"), "—"))
        cells += [fmt_stars(stars), fmt_gain(gain), status]
        out.append("| " + " | ".join(cells) + " |")
    return "\n".join(out)


def block_content(name, catalog, raw, lang):
    if name.startswith("board:"):
        category = name.split(":", 1)[1]
        header = HEADERS[lang][name]
        body = rows_for(catalog, raw, category, group_col=(category == "infra"), lang=lang)
    elif name.startswith("vertical:"):
        _, category, vertical = name.split(":")
        header = HEADERS[lang]["vertical"]
        body = rows_for(catalog, raw, category, vertical=vertical, lang=lang)
    else:
        sys.exit(f"ERROR: unknown auto block '{name}'")
    if not body:
        sys.exit(f"ERROR: auto block '{name}' produced no rows")
    return header + "\n" + body


def main():
    catalog, raw, heat_date = load_inputs()
    for lang, files in FILES.items():
        for rel in files:
            path = os.path.join(ROOT, rel)
            if not os.path.exists(path):
                sys.exit(f"ERROR: {rel} does not exist")
            with open(path, encoding="utf-8") as fh:
                text = fh.read()

            def repl(m, lang=lang):
                return m.group(1) + block_content(m.group(2), catalog, raw, lang) + "\n" + m.group(3)

            new, n = MARKER_RE.subn(repl, text)
            new = DATE_LINE_RE.sub(lambda m: m.group(1) + heat_date, new)
            if n == 0:
                sys.exit(f"ERROR: no auto blocks found in {rel}")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new)
            print(f"rendered {rel} ({n} blocks)")


if __name__ == "__main__":
    main()
