# Agent Evaluation Framework

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-9ca3af?style=for-the-badge)](../zh/agents/evaluation-framework.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-1f6feb?style=for-the-badge)](evaluation-framework.md)
[![Home](https://img.shields.io/badge/HOME-README-24292f?style=for-the-badge)](../README.md)

This framework is not for assigning a total score.

It exists so that different profiles can be compared side by side instead of each one drifting into a totally different writing style.

## Required Fields

| Field | What it should answer |
| --- | --- |
| `name` | What the project is actually called and who owns it |
| `category` | Whether it is mainly an executor, automation system, multi-agent system, or platform |
| `capabilities` | Where its real strength boundary sits |
| `best use cases` | What kinds of problems should start here |
| `not suitable for` | What kinds of problems should not start here |
| `complexity level` | How heavy it is to operate in practice |
| `real-world usage notes` | The biggest practical caveats, costs, or operator responsibilities |

## Recommended Fields

| Field | Why it helps |
| --- | --- |
| `open_source` | Clarifies whether the project is open, closed, or mixed |
| `homepage` / `repo` | Points readers to the official source |
| `verification` | Notes ambiguity in naming or positioning |
| `delivery model` | Tells readers whether the system is managed, self-hosted, local-first, or framework-only |
| `last_reviewed` | Signals how recent the verification is |

## Category Definitions

| Category | Meaning here |
| --- | --- |
| `execution` | You hand it a task and it does work directly |
| `automation` | It behaves more like workflow, scheduling, task queue, approval, or orchestration system |
| `multi-agent` | It explicitly supports delegation, subagents, or parallel collaboration |
| `platform` | It is mainly infrastructure for building, routing, hosting, or operating agents |

## Complexity Definitions

| Level | Meaning here |
| --- | --- |
| `low` | Small teams or individuals can get value quickly with little setup |
| `medium` | Reasonable to start, but still requires workflow, permission, or environment management |
| `high` | Requires meaningful systems design, infra ownership, security work, or observability |

## Writing Rules

- Write task outcomes before architecture language.
- Always state anti-fit, not just fit.
- Do not confuse feature support with primary strength.
- Capture operator cost: approvals, environment setup, secrets, review burden, maintenance.
- If public information is incomplete, say so directly.

## Suggested Page Structure

```md
# Agent Name

One-line positioning.

## Quick Read

## When To Pick It

## When Not To Pick It

## Capability Shape

## Operating Cost

## Bottom Line
```

## What This Framework Avoids On Purpose

- No total score.
- No vague leaderboard.
- No false equivalence between research prototypes and production tools.
- No popularity-based ranking disguised as evaluation.