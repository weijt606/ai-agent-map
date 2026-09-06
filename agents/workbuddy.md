# WorkBuddy

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/workbuddy.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](workbuddy.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: WorkBuddy is Tencent's desktop office agent — the same "hand it a goal, it drives your files and apps" pattern this map tracks for code, pointed at documents, spreadsheets, and slide decks instead, and by mid-2026 the highest-traffic product of its kind in China.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Tencent (from the CodeBuddy family) |
| Route | General-purpose autonomous agent — office and knowledge work rather than repositories |
| Open source | No |
| Best for | Non-engineering work an agent can finish end to end: reports, decks, spreadsheets, research |
| Main cost | Credit-based commercial product; closed source, and it reads and writes your local files |
| Surfaces | Desktop client (Windows / macOS), web, WeChat mini-program, enterprise portal |
| Official site | https://copilot.tencent.com/work/ |

## Why This Entry Exists

This map is a coding-agent map by centre of gravity, not by rule — it already profiles [OpenHuman](openhuman.md) for personal-data life integration and [n8n](n8n.md) for workflow automation. WorkBuddy is included for a narrower reason: it is the clearest evidence that **the agent pattern this map documents has escaped the repository**, and it did so first at scale in China.

Tencent positions it as an all-scenario AI office workstation covering daily work, code development, and creative design — an intelligent colleague that decomposes and executes rather than suggesting. Read against the rest of this directory, the loop is familiar: natural-language goal, autonomous decomposition, tool calls, self-verification, a deliverable you can accept or reject. Only the tools changed.

## When To Pick It

- The work is **office-shaped**: Word, Excel, PowerPoint, PDFs, images — read, write, merge, convert — and you want a finished artefact rather than advice.
- You want **parallel agents** on one project without assembling a harness yourself.
- You want **prebuilt domain roles**. Tencent ships 100+ specialists across recruitment, research, frontend, legal, and marketing.
- You need it to keep working when you close the laptop: cloud-hosted tasks run around the clock, and you can drive it from a phone through Tencent's own messaging surfaces.
- You are inside the Chinese enterprise stack already — WeCom, QQ, Feishu, DingTalk integrations are the intended operating environment.

## When Not To Pick It

- **You are choosing a coding agent.** For repositories, everything else on this map is a better starting point — including Tencent's own CodeBuddy, which this map does not yet profile.
- **You care about reading what it does.** Closed source, running with authorized access to local files, is a materially different governance position from the open harnesses here. That is a real trade, not a formality — see [observability and evals](../comparisons/observability-and-evals.md) for what you lose when the log is not yours.
- You need it outside mainland Chinese platforms. The integrations, the model choices, and the support are built for that market.
- You want model transparency: the product surfaces let you switch between several large models, but which one runs a given step is not something the product page pins down.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Office artefact generation | Very strong | The product's core claim: finished documents, spreadsheets, and decks |
| Task decomposition | Strong | Autonomous multi-step planning with self-verification |
| Multi-agent | Strong | Parallel agents on one project |
| Local file operations | Strong | Reads and writes within directories you authorize |
| Remote / mobile control | Strong | Bound through WeCom, QQ, Feishu, or DingTalk; phone-side control of the desktop |
| Model choice | Medium | Multiple large models selectable; the mapping to steps is not published |
| Open source / auditability | None | Proprietary |

## Market Position

By June 2026, roughly three months after its March 9 2026 launch, WorkBuddy was reported at **20.97M monthly visits — more than the second and third place products combined** in China's desktop AI office category, against a category total of over 60M across 17 tracked products. Alibaba consolidated three of its own agent products into a single office offering in July, and ByteDance pushed Doubao into the same space. Those are secondary-source market figures, recorded here as a trend rather than as vendor-verified numbers.

The selection point is not the traffic. It is that **office agents are now a contested vendor category in their own right**, on the same loop, with none of the openness that the coding side of this map takes for granted.

## Bottom Line

WorkBuddy earns its place here as the boundary case: an agent whose loop this map recognizes, whose surface it does not usually cover, and whose governance story is the opposite of the open harnesses next to it. Pick it if the work is documents and you are in its ecosystem. Do not pick it if you would want to audit what it did with your files afterwards.
