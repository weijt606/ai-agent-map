# ZCode

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/zcode.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](zcode.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: ZCode is Zhipu's desktop agentic development environment — a GUI task surface rather than an editor, tuned around GLM-5.3, with long-horizon "Goal" tasks you can steer from WeChat, Feishu, or Telegram while you are away from the machine.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Zhipu / Z.ai |
| Route | Direct execution (desktop GUI, not a terminal CLI and not an editor plugin) |
| Open source | No — the client is proprietary; the GLM model line is separately open-weighted |
| Best for | GLM-first teams who want long-running coding tasks with a visible task surface and remote check-ins |
| Main cost | Paid subscription tiers; the strongest capabilities are tied to Zhipu's own models |
| Current version | 3.11.2 |
| Official site | https://zcode.z.ai |

## Why This Entry Exists

This map had a real hole on the Chinese vendor side: it profiles [Kimi Code](kimi-code.md), [MiMoCode](mimocode.md), [CodeWhale](codewhale.md), [CoStrict](costrict.md), and [Open Code Review](open-code-review.md), all of which are terminal or CI shaped, and none of which is the tool a GLM-first team actually opens. ZCode is that tool, and it is a different shape from everything above: a **desktop application whose primary object is a task, not a file**.

That distinction is why it sits on the direct-execution route rather than with [Cursor](cursor.md) and [Windsurf](windsurf.md). The editor-centric route is for products where the editor stays the centre of gravity. In ZCode the centre is a goal you hand over and check on.

## When To Pick It

- You are already on **GLM**. The product's stated design point is deep integration with GLM-5.3, plus GLM-5.3-Flash for screenshot and image understanding.
- Your tasks are **long-horizon**. The "Goal" feature exists specifically to hold a multi-step objective across a long run rather than a single prompt-and-diff exchange.
- You want to **check in from your phone**. Remote invocation through WeChat, Feishu, or Telegram is a first-class feature, not an integration afterthought — a genuinely different operating model from a terminal agent that dies with your SSH session.
- You want a GUI over agent work without adopting an editor's whole opinion about your workflow.
- You want Linux desktop coverage: `.deb`, `.rpm`, and `.AppImage` builds exist alongside macOS (Apple Silicon and Intel) and Windows (x64 and ARM64).

## When Not To Pick It

- **You want to read the code.** The client is closed. If open source is the requirement on this route, [Kimi Code](kimi-code.md) and [CodeWhale](codewhale.md) are the comparable Chinese-vendor options.
- You are a terminal-first developer. This is a desktop app; a CLI loop is a different ergonomic bet — see the [terminal coding CLI comparison](../comparisons/coding-cli-agents.md).
- You do not run GLM. The tool accepts other backends (see below), but the tuning, the pricing, and the vendor's attention are on their own model line.
- You need an established governance story. This is a young product on a fast release cadence — 3.11.2 at the time of writing.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Long-horizon execution | Strong | "Goal" is the product's headline primitive for multi-step objectives |
| Remote operation | Very strong | Drive and monitor runs from WeChat, Feishu, or Telegram |
| Multimodal input | Strong | GLM-5.3-Flash handles screenshots and image analysis |
| Multi-agent | Strong | Positioned around several agents collaborating on one objective |
| Platform coverage | Strong | macOS (both architectures), Windows (x64/ARM64), Linux (beta) |
| Model freedom | Medium | GLM-first by design; other providers reported to work through your own key |
| Open source | None | Proprietary client |

**Sourcing note.** The official site documents GLM-5.3 and GLM-5.3-Flash. Third-party walkthroughs report that ZCode also accepts your own key for Anthropic, OpenRouter, and OpenAI-compatible endpoints (including pointing it at DeepSeek's Anthropic-compatible URL), and earlier coverage of the 3.0 release described it as a visual front end for Claude Code, Codex, and Gemini. That capability is **not** stated on the current official page, so this map records it as reported rather than confirmed — verify against the version you install before building a multi-vendor plan on it.

## Relationship To The Model Layer

ZCode is the product; GLM is the model. This map does not yet profile the open-weights model tier that GLM belongs to, which is a separate gap it is tracking. What matters for selection here: the reason to choose ZCode over a vendor-neutral harness is the tuning between the client and Zhipu's own models, so a team that wants model portability above all should weigh a harness from the [harness route](../comparisons/agent-harness-frameworks.md) instead.

## Bottom Line

ZCode is the most complete answer to "what does a GLM-first developer actually run", and its remote-invocation and long-horizon-goal design are genuinely different from the terminal loops this map is mostly made of. The trade is the usual one for this shape: you get an integrated product and you give up reading the source, and the deepest capability is tied to one vendor's models.
