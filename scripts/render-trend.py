#!/usr/bin/env python3
"""Render the weekly heat-ranking bump chart as committed SVG assets.

Reads scripts/history.json (the `windows` list) and scripts/catalog.json
(display names) and writes assets/heat-trend-en.svg + assets/heat-trend-zh.svg.
Pure stdlib; the SVGs are self-contained (own light background) so they stay
readable on GitHub in both light and dark mode.

Usage:
    python3 scripts/render-trend.py          # both languages, last 26 windows
    python3 scripts/render-trend.py --all    # render every window
    python3 scripts/render-trend.py --lang en

Colors follow the entity, never the rank: the slug->color map below is fixed
so a re-render never repaints a project. Eight CVD-validated categorical hues
go to the long-tenured headline projects; every other entrant folds into two
neutral grays and is identified by the right-edge labels and the legend.
"""
import argparse
import json
import os
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
HISTORY = os.path.join(HERE, "history.json")
CATALOG = os.path.join(HERE, "catalog.json")
ASSETS = os.path.join(ROOT, "assets")

MAX_WINDOWS_DEFAULT = 26

# Fixed entity colors (validated: scripts/validate_palette.js, light surface).
COLORS = {
    "mattpocock/skills": "#2a78d6",
    "addyosmani/agent-skills": "#1baf7a",
    "obra/superpowers": "#eda100",
    "nousresearch/hermes-agent": "#008300",
    "anthropics/skills": "#4a3aa7",
    "colbymchenry/codegraph": "#e34948",
    "earendil-works/pi": "#e87ba4",
    "openai/codex": "#eb6834",
}
GRAYS = ["#898781", "#b8b6ae"]

INK = "#0b0b0b"
INK_SOFT = "#52514e"
GRID = "#e1e0d9"
SURFACE = "#fcfcfb"
BORDER = "rgba(11,11,11,0.10)"

TEXT = {
    "en": {
        "title": "Weekly heat top 10 — ranked by 7-day star gain",
        "subtitle": "Last updated {date} · window {start} → {end}",
        "subtitle_nowin": "Last updated {date}",
        "footnote": "Table depth grew over time: top 5–8 before 2026-05-23, top 10 since. Gaps mean the project was off the board that week.",
        "gray_note": "gray = shorter-lived entrants",
    },
    "zh": {
        "title": "每周热度 Top 10 —— 按 7 天 star 增量排名",
        "subtitle": "最后更新 {date} · 窗口 {start} → {end}",
        "subtitle_nowin": "最后更新 {date}",
        "footnote": "榜单深度随时间扩大：2026-05-23 之前为 top 5–8，此后为 top 10。折线中断表示该周未上榜。",
        "gray_note": "灰色 = 短暂上榜项目",
    },
}

MARGIN_LEFT = 40
MARGIN_RIGHT = 190
TOP = 56
ROW_H = 36
COL_STEP = 72
MAX_RANK = 10
DATE_AXIS_H = 26
FOOTNOTE_H = 18
LEGEND_ROW_H = 20
LEGEND_PAD = 10


def text_width(s, size=11):
    """Rough width estimate: CJK glyphs ~= 1em, latin ~= 0.56em."""
    w = 0.0
    for ch in s:
        w += size if ord(ch) > 0x2E7F else size * 0.56
    return w


def display_name(catalog, slug, lang):
    meta = catalog.get(slug, {})
    name = meta.get("display", slug)
    if lang == "zh":
        name = meta.get("display_zh", name)
    return name


def color_for(slug, gray_index):
    if slug in COLORS:
        return COLORS[slug], False
    return GRAYS[gray_index % len(GRAYS)], True


def build_svg(windows, catalog, lang):
    t = TEXT[lang]
    n = len(windows)
    plot_w = (n - 1) * COL_STEP if n > 1 else COL_STEP
    width = MARGIN_LEFT + plot_w + MARGIN_RIGHT
    plot_h = MAX_RANK * ROW_H

    def x(i):
        return MARGIN_LEFT + i * COL_STEP

    def y(rank):
        return TOP + (rank - 0.5) * ROW_H

    # Presence map: slug -> {window index: rank}
    presence = {}
    for i, w in enumerate(windows):
        for e in w["entries"]:
            presence.setdefault(e["slug"], {})[i] = e["rank"]

    # Stable order: first appearance, then slug — keeps gray alternation and
    # legend order identical across re-renders.
    order = sorted(presence, key=lambda s: (min(presence[s]), s))
    gray_slugs = [s for s in order if s not in COLORS]
    gray_idx = {s: i for i, s in enumerate(gray_slugs)}

    parts = []
    parts.append(f'<text x="{MARGIN_LEFT}" y="24" font-size="15" font-weight="600" fill="{INK}">{escape(t["title"])}</text>')
    last = windows[-1]
    if last.get("window_start") and last.get("window_end"):
        subtitle = t["subtitle"].format(date=last["date"], start=last["window_start"], end=last["window_end"])
    else:
        subtitle = t["subtitle_nowin"].format(date=last["date"])
    parts.append(f'<text x="{MARGIN_LEFT}" y="42" font-size="12" fill="{INK_SOFT}">{escape(subtitle)}</text>')

    # Grid: one recessive horizontal line per rank + rank labels.
    for r in range(1, MAX_RANK + 1):
        yy = y(r)
        parts.append(f'<line x1="{MARGIN_LEFT}" y1="{yy:.1f}" x2="{MARGIN_LEFT + plot_w}" y2="{yy:.1f}" stroke="{GRID}" stroke-width="1"/>')
        parts.append(f'<text x="{MARGIN_LEFT - 8}" y="{yy + 4:.1f}" font-size="11" fill="{INK_SOFT}" text-anchor="end">#{r}</text>')

    # Date axis: label every column, or every other when crowded.
    label_step = 1 if n < 18 else 2
    axis_y = TOP + plot_h + DATE_AXIS_H - 8
    prev_year = None
    for i, w in enumerate(windows):
        if i % label_step and i != n - 1:
            continue
        yr, mo, dy = w["date"].split("-")
        label = f"{mo}-{dy}"
        if prev_year is None or yr != prev_year:
            label = w["date"]
            prev_year = yr
        parts.append(f'<text x="{x(i)}" y="{axis_y}" font-size="11" fill="{INK_SOFT}" text-anchor="middle">{escape(label)}</text>')

    # Series: split each project's on-board windows into consecutive runs.
    for slug in order:
        pts = presence[slug]
        color, _is_gray = color_for(slug, gray_idx.get(slug, 0))
        runs, run = [], []
        for i in range(n):
            if i in pts:
                run.append(i)
            elif run:
                runs.append(run)
                run = []
        if run:
            runs.append(run)
        for run in runs:
            if len(run) > 1:
                coords = " ".join(f"{x(i)},{y(pts[i]):.1f}" for i in run)
                parts.append(f'<polyline points="{coords}" fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
            for i in run:
                parts.append(f'<circle cx="{x(i)}" cy="{y(pts[i]):.1f}" r="4" fill="{color}" stroke="{SURFACE}" stroke-width="2"/>')

    # Right edge: direct labels for everything on the latest board.
    for e in last["entries"]:
        color, _ = color_for(e["slug"], gray_idx.get(e["slug"], 0))
        name = display_name(catalog, e["slug"], lang)
        parts.append(f'<text x="{MARGIN_LEFT + plot_w + 12}" y="{y(e["rank"]) + 4:.1f}" font-size="11" fill="{INK}">{escape(name)}</text>')
        parts.append(f'<rect x="{MARGIN_LEFT + plot_w + 2}" y="{y(e["rank"]) - 3:.1f}" width="6" height="6" fill="{color}"/>')

    # Legend: every project that ever charted, wrapped to the SVG width.
    legend_top = TOP + plot_h + DATE_AXIS_H + LEGEND_PAD
    lx, ly = MARGIN_LEFT, legend_top
    legend_right = width - 16
    for slug in order:
        color, _ = color_for(slug, gray_idx.get(slug, 0))
        name = display_name(catalog, slug, lang)
        item_w = 16 + text_width(name) + 14
        if lx + item_w > legend_right and lx > MARGIN_LEFT:
            lx = MARGIN_LEFT
            ly += LEGEND_ROW_H
        parts.append(f'<rect x="{lx}" y="{ly - 8}" width="10" height="10" fill="{color}"/>')
        parts.append(f'<text x="{lx + 15}" y="{ly + 1}" font-size="11" fill="{INK_SOFT}">{escape(name)}</text>')
        lx += item_w
    # gray meaning note as the last legend item
    note = t["gray_note"]
    item_w = text_width(note) + 14
    if lx + item_w > legend_right and lx > MARGIN_LEFT:
        lx = MARGIN_LEFT
        ly += LEGEND_ROW_H
    parts.append(f'<text x="{lx}" y="{ly + 1}" font-size="11" font-style="italic" fill="{INK_SOFT}">{escape(note)}</text>')

    footnote_y = ly + LEGEND_ROW_H + 4
    parts.append(f'<text x="{MARGIN_LEFT}" y="{footnote_y}" font-size="11" fill="{INK_SOFT}">{escape(t["footnote"])}</text>')

    height = footnote_y + FOOTNOTE_H
    head = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" font-family="system-ui, -apple-system, sans-serif">'
        f'<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" fill="{SURFACE}" stroke="{BORDER}" rx="6"/>'
    )
    return head + "".join(parts) + "</svg>"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", choices=["en", "zh"], help="render one language only")
    ap.add_argument("--all", action="store_true", help="render every window, not just the last %d" % MAX_WINDOWS_DEFAULT)
    args = ap.parse_args()

    with open(HISTORY, encoding="utf-8") as fh:
        windows = json.load(fh)["windows"]
    with open(CATALOG, encoding="utf-8") as fh:
        catalog = json.load(fh)
    if not windows:
        raise SystemExit("history.json has no windows")
    if not args.all:
        windows = windows[-MAX_WINDOWS_DEFAULT:]

    for lang in [args.lang] if args.lang else ["en", "zh"]:
        out = os.path.join(ASSETS, f"heat-trend-{lang}.svg")
        svg = build_svg(windows, catalog, lang)
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(svg + "\n")
        print(f"wrote {os.path.relpath(out, ROOT)} ({len(windows)} windows)")


if __name__ == "__main__":
    main()
