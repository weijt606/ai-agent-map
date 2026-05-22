# SWE-agent

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/swe-agent.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](swe-agent.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: SWE-agent is the original research harness behind SWE-bench — Princeton + Stanford's reference design for "give an LLM a tool interface and let it fix real GitHub issues."

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Princeton + Stanford NLP (John Yang, Carlos Jimenez, Kilian Lieret et al.) |
| Route | Agent harness framework — research reference |
| Open source | Yes (MIT, Python) |
| Best for | Researchers and engineers who want a hackable, single-YAML-config harness whose output ships to SWE-bench |
| Main cost | Most upstream development effort has shifted to [mini-swe-agent](mini-swe-agent.md); SWE-agent is now the heavier historical reference |
| GitHub repo | https://github.com/SWE-agent/SWE-agent |

## When To Pick It

- You are doing SWE-bench / SWE-bench-Verified research and want the harness that produced the original numbers.
- You want a hackable single-YAML configuration where the entire prompting strategy, tool set, and command surface are in one file.
- You need EnIGMA-style extensions for offensive cybersecurity / CTF tasks — SWE-agent is the canonical base for that.
- You want the most-cited open-source harness when you need to defend a methodological choice.

## When Not To Pick It

- You want the leanest possible harness — [mini-swe-agent](mini-swe-agent.md) is now the successor line from the same team, and the upstream README explicitly says most current development effort is on mini-swe-agent.
- You want a finished product with a polished UI. SWE-agent is a research tool, not a developer product.
- You need broad provider coverage and rich tool ecosystem out of the box — [OpenHarness](openharness.md) and [Pi](pi.md) provide more for everyday use.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Research reproducibility | Very strong | The canonical SWE-bench harness reference |
| Configuration surface | Very strong | Single YAML controls prompting strategy, tools, and agent behavior |
| Multi-purpose use | Strong | GitHub-issue fixing, CTF (EnIGMA), coding competition |
| Provider flexibility | Strong | Works with any LM provider |
| Upstream maintenance | Slowing | Active development has largely moved to mini-swe-agent |

## Operating Cost

Complexity is Medium. The single-YAML design makes experiments cheap to vary, but the codebase is heavier than mini-swe-agent and the documentation is research-grade. You are not paying for polish — you are paying for the reference implementation.

## Bottom Line

SWE-agent is what an agent harness looks like when it was designed first as a research artifact, not a developer product. If you are publishing SWE-bench numbers, doing cybersecurity-agent research, or want to defend a baseline methodology, this is the canonical starting point. If you want a leaner working harness for day-to-day use, follow the upstream's own recommendation and look at [mini-swe-agent](mini-swe-agent.md).
