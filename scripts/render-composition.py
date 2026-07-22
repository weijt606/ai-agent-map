#!/usr/bin/env python3
"""Render the weekly top-10 composition chart (stacked bars by category).

Reads scripts/history.json (`windows`) and scripts/catalog.json (per-slug
category: agent | infra | skill) and writes assets/heat-composition-en.svg +
assets/heat-composition-zh.svg. This is the quantitative view of the story the
weekly bullets tell in prose: how many of the top-10 gain seats each layer
holds per window (the "skills wave" line is the amber band).

Pure stdlib; self-contained light-surface SVGs (same design constants as
render-trend.py) so they stay readable on GitHub in both modes. Idempotent for
the same history file.

Usage:
    python3 scripts/render-composition.py            # both languages
    python3 scripts/render-composition.py --lang en
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

# Same surface/ink constants as render-trend.py; category colors reuse the
# validated palette (amber = the skills wave, blue = agents, gray = infra).
INK = "#0b0b0b"
INK_SOFT = "#52514e"
GRID = "#e1e0d9"
SURFACE = "#fcfcfb"
BORDER = "rgba(11,11,11,0.10)"
CAT_COLORS = {"agent": "#2a78d6", "infra": "#898781", "skill": "#eda100"}
CAT_ORDER = ["agent", "infra", "skill"]  # stack bottom -> top; skill on top

TEXT = {
    "en": {
        "title": "Who holds the weekly top 10 — seats by layer",
        "subtitle": "Last updated {date} · one bar per weekly window · amber = the skills wave",
        "cats": {"agent": "agent", "infra": "infra", "skill": "skill"},
        "latest_head": "latest window:",
        "latest": "skill {skill} · agent {agent} · infra {infra}",
        "footnote": "Table depth grew over time: top 5–8 before 2026-05-23, top 10 since — shorter early bars reflect that, not fewer projects.",
    },
    "zh": {
        "title": "每周 Top 10 由谁占据——按层分席位",
        "subtitle": "最后更新 {date} · 每根柱是一个每周窗口 · 琥珀色 = skills 浪潮",
        "cats": {"agent": "agent", "infra": "infra", "skill": "skill"},
        "latest_head": "最新窗口：",
        "latest": "skill {skill} 席 · agent {agent} · infra {infra}",
        "footnote": "榜单深度随时间加深：2026-05-23 之前是 top 5–8，此后是 top 10——早期柱子矮是这个原因，不是项目变少。",
    },
}


def load():
    with open(HISTORY, encoding="utf-8") as fh:
        windows = json.load(fh)["windows"]
    with open(CATALOG, encoding="utf-8") as fh:
        catalog = json.load(fh)
    cats = {k: v.get("category") for k, v in catalog.items() if isinstance(v, dict)}
    return windows, cats


def counts_for(window, cats):
    c = {k: 0 for k in CAT_ORDER}
    for e in window["entries"]:
        cat = cats.get(e["slug"].lower(), "agent")
        c[cat if cat in c else "agent"] += 1
    return c


def render(lang, windows, cats):
    t = TEXT[lang]
    n = len(windows)
    width = 920
    margin_l, margin_r, margin_t, margin_b = 46, 250, 66, 56
    plot_w = width - margin_l - margin_r
    plot_h = 200
    height = margin_t + plot_h + margin_b
    max_seats = 10
    bar_gap = 10
    bar_w = max(8, (plot_w - bar_gap * (n - 1)) / n)

    latest = windows[-1]
    latest_counts = counts_for(latest, cats)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" font-family="system-ui, -apple-system, sans-serif">',
        f'<rect width="{width}" height="{height}" rx="10" fill="{SURFACE}" stroke="{BORDER}"/>',
        f'<text x="{margin_l}" y="26" font-size="16" font-weight="700" fill="{INK}">{escape(t["title"])}</text>',
        f'<text x="{margin_l}" y="44" font-size="11" fill="{INK_SOFT}">'
        f'{escape(t["subtitle"].format(date=latest["date"]))}</text>',
    ]

    # horizontal gridlines every 2 seats
    for s in range(0, max_seats + 1, 2):
        y = margin_t + plot_h - plot_h * s / max_seats
        parts.append(f'<line x1="{margin_l}" y1="{y:.1f}" x2="{margin_l + plot_w}" y2="{y:.1f}" '
                     f'stroke="{GRID}" stroke-width="1"/>')
        parts.append(f'<text x="{margin_l - 8}" y="{y + 3.5:.1f}" font-size="10" fill="{INK_SOFT}" '
                     f'text-anchor="end">{s}</text>')

    # bars
    for i, w in enumerate(windows):
        x = margin_l + i * (bar_w + bar_gap)
        c = counts_for(w, cats)
        y_cursor = margin_t + plot_h
        for cat in CAT_ORDER:
            seats = c[cat]
            if not seats:
                continue
            h = plot_h * seats / max_seats
            y_cursor -= h
            parts.append(f'<rect x="{x:.1f}" y="{y_cursor:.1f}" width="{bar_w:.1f}" height="{h:.1f}" '
                         f'fill="{CAT_COLORS[cat]}" rx="1.5"/>')
            if seats >= 2 and bar_w >= 24:
                parts.append(f'<text x="{x + bar_w / 2:.1f}" y="{y_cursor + h / 2 + 3.5:.1f}" font-size="10" '
                             f'font-weight="600" fill="#ffffff" text-anchor="middle">{seats}</text>')
        # x label (MM-DD), every bar while sparse; thin to every 2nd beyond 20 windows
        if n <= 20 or i % 2 == (n - 1) % 2:
            parts.append(f'<text x="{x + bar_w / 2:.1f}" y="{margin_t + plot_h + 16}" font-size="9.5" '
                         f'fill="{INK_SOFT}" text-anchor="middle">{w["date"][5:]}</text>')

    # legend + latest read-out on the right
    lx = margin_l + plot_w + 24
    ly = margin_t + 8
    for cat in reversed(CAT_ORDER):
        parts.append(f'<rect x="{lx}" y="{ly - 9}" width="12" height="12" rx="2" fill="{CAT_COLORS[cat]}"/>')
        parts.append(f'<text x="{lx + 18}" y="{ly + 1.5}" font-size="11.5" fill="{INK}">{escape(t["cats"][cat])}</text>')
        ly += 22
    parts.append(f'<text x="{lx}" y="{ly + 10}" font-size="10.5" fill="{INK_SOFT}">'
                 f'{escape(t["latest_head"])}</text>')
    parts.append(f'<text x="{lx}" y="{ly + 26}" font-size="10.5" font-weight="600" fill="{INK}">'
                 f'{escape(t["latest"].format(**latest_counts))}</text>')

    parts.append(f'<text x="{margin_l}" y="{height - 14}" font-size="10" fill="{INK_SOFT}">'
                 f'{escape(t["footnote"])}</text>')
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", choices=["en", "zh"], help="render one language only")
    args = ap.parse_args()
    windows, cats = load()
    os.makedirs(ASSETS, exist_ok=True)
    for lang in ([args.lang] if args.lang else ["en", "zh"]):
        out = os.path.join(ASSETS, f"heat-composition-{lang}.svg")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(render(lang, windows, cats))
        print(f"wrote {os.path.relpath(out, ROOT)} ({len(windows)} windows)")


if __name__ == "__main__":
    main()
