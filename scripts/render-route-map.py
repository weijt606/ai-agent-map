#!/usr/bin/env python3
"""Render the route ecosystem map as committed SVG assets.

The visual form of the home page's "The First Cut Of The Map" table: 12 routes
as cards, grouped into four bands by what the user is really deciding, each
card naming its flagship projects. Writes assets/route-map-en.svg +
assets/route-map-zh.svg with the same design constants as the other charts.

Data lives in ROUTE GROUPS below and is the single source for this chart —
when a route gains or loses a profile, update the names/counts here and rerun
(the weekly playbook's conditional step covers this). Card "+N" counts must
keep summing to the home page's total profile count.

Usage:
    python3 scripts/render-route-map.py            # both languages
    python3 scripts/render-route-map.py --lang en
"""
import argparse
import os
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
ASSETS = os.path.join(ROOT, "assets")

INK = "#0b0b0b"
INK_SOFT = "#52514e"
SURFACE = "#fcfcfb"
CARD = "#ffffff"
BORDER = "rgba(11,11,11,0.10)"
CARD_BORDER = "rgba(11,11,11,0.12)"

# group: (label_en, label_zh, color, routes)
# route: (name_en, name_zh, [shown projects], total_profiles)
GROUPS = [
    ("Use an agent on your code", "让 agent 直接上手你的代码", "#2a78d6", [
        ("Direct execution", "直接执行", ["Claude Code", "Codex", "Aider", "Kimi Code"], 8),
        ("Editor-centric AI workflow", "编辑器中心", ["Cursor", "Windsurf", "Continue"], 3),
        ("Review-first automation", "评审优先自动化", ["Cline", "GitHub Copilot"], 4),
        ("Workflow / orchestration layer", "工作流编排层", ["oh-my-claudecode", "oh-my-codex", "Ruflo"], 3),
        ("Managed background path", "管理式后台路径", ["Claude Managed Agents"], 1),
    ]),
    ("Own the loop", "自己掌控循环", "#eb6834", [
        ("Agent harness framework", "Agent harness 框架", ["Pi", "jcode", "OpenHands"], 6),
        ("Self-hosted / local runtime", "自托管 / 本地 runtime", ["Hermes Agent", "OpenClaw", "Goose"], 6),
        ("General-purpose autonomous agent", "通用自主 agent", ["AutoGPT", "Agent Zero", "BabyAGI"], 6),
    ]),
    ("Build your own", "自建与基础设施", "#1baf7a", [
        ("Build-your-own system", "自建系统", ["LangChain", "LangGraph", "CrewAI"], 8),
        ("Runtime and tools", "运行时 & 工具", ["n8n", "MemGPT", "CodeGraph"], 7),
    ]),
    ("The model & skill layer", "模型与技能层", "#4a3aa7", [
        ("Frontier agentic model", "前沿 agentic 模型", ["Claude Fable 5", "GPT-5.5"], 2),
        ("Agentic skills framework", "Agentic skills 框架", ["Superpowers"], 1),
    ]),
]

TEXT = {
    "en": {
        "title": "The AI Agent Map — the first cut: 12 routes, {total} profiles",
        "subtitle": "Four decisions, twelve routes. Full tables with links follow below.",
        "more": "+{n} more",
    },
    "zh": {
        "title": "AI Agent 选型地图——先摊开：12 条路线、{total} 个 profile",
        "subtitle": "四类决策、十二条路线。带链接的完整表格见下文。",
        "more": "等 {n} 个",
    },
}

WIDTH = 920
MARGIN = 26
COLS = 3
CARD_GAP = 12
CARD_H = 58
GROUP_HEAD_H = 30
GROUP_GAP = 16
TITLE_H = 58


def total_profiles():
    return sum(r[3] for _, _, _, routes in GROUPS for r in routes)


def render(lang):
    t = TEXT[lang]
    card_w = (WIDTH - 2 * MARGIN - (COLS - 1) * CARD_GAP) / COLS
    # measure height
    y = TITLE_H
    for _, _, _, routes in GROUPS:
        rows = -(-len(routes) // COLS)
        y += GROUP_HEAD_H + rows * (CARD_H + CARD_GAP) - CARD_GAP + GROUP_GAP
    height = y + MARGIN - GROUP_GAP + 8

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height:.0f}" '
        f'viewBox="0 0 {WIDTH} {height:.0f}" font-family="system-ui, -apple-system, sans-serif">',
        f'<rect width="{WIDTH}" height="{height:.0f}" rx="10" fill="{SURFACE}" stroke="{BORDER}"/>',
        f'<text x="{MARGIN}" y="28" font-size="17" font-weight="700" fill="{INK}">'
        f'{escape(t["title"].format(total=total_profiles()))}</text>',
        f'<text x="{MARGIN}" y="46" font-size="11" fill="{INK_SOFT}">{escape(t["subtitle"])}</text>',
    ]

    y = TITLE_H
    for label_en, label_zh, color, routes in GROUPS:
        label = label_en if lang == "en" else label_zh
        parts.append(f'<circle cx="{MARGIN + 5}" cy="{y + 11}" r="5" fill="{color}"/>')
        parts.append(f'<text x="{MARGIN + 18}" y="{y + 15}" font-size="12.5" font-weight="700" '
                     f'fill="{INK}">{escape(label)}</text>')
        y += GROUP_HEAD_H
        for i, (name_en, name_zh, projects, total) in enumerate(routes):
            col, row = i % COLS, i // COLS
            x = MARGIN + col * (card_w + CARD_GAP)
            cy = y + row * (CARD_H + CARD_GAP)
            name = name_en if lang == "en" else name_zh
            parts.append(f'<rect x="{x:.1f}" y="{cy:.1f}" width="{card_w:.1f}" height="{CARD_H}" rx="7" '
                         f'fill="{CARD}" stroke="{CARD_BORDER}"/>')
            parts.append(f'<rect x="{x:.1f}" y="{cy:.1f}" width="3.5" height="{CARD_H}" rx="1.75" fill="{color}"/>')
            parts.append(f'<text x="{x + 13:.1f}" y="{cy + 22:.1f}" font-size="12" font-weight="600" '
                         f'fill="{INK}">{escape(name)}</text>')
            shown = ", ".join(projects)
            extra = total - len(projects)
            if extra > 0:
                shown += " · " + t["more"].format(n=extra)
            parts.append(f'<text x="{x + 13:.1f}" y="{cy + 41:.1f}" font-size="10.5" '
                         f'fill="{INK_SOFT}">{escape(shown)}</text>')
        rows = -(-len(routes) // COLS)
        y += rows * (CARD_H + CARD_GAP) - CARD_GAP + GROUP_GAP

    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", choices=["en", "zh"], help="render one language only")
    args = ap.parse_args()
    os.makedirs(ASSETS, exist_ok=True)
    for lang in ([args.lang] if args.lang else ["en", "zh"]):
        out = os.path.join(ASSETS, f"route-map-{lang}.svg")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(render(lang))
        print(f"wrote {os.path.relpath(out, ROOT)} ({total_profiles()} profiles)")


if __name__ == "__main__":
    main()
