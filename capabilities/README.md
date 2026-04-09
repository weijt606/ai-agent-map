# Capabilities

[![中文](https://img.shields.io/badge/中文-查看中文版-9ca3af?style=flat-square)](../zh/capabilities/README.md)
[![English](https://img.shields.io/badge/English-Current%20Page-1f6feb?style=flat-square)](README.md)

This directory is not a feature dump. It is a shared vocabulary.

The point is to keep profile pages speaking the same language, otherwise it becomes too easy to say “both support it” when the actual strength difference is large.

## Current Priority Dimensions

| Dimension | What it really means here | Typical question |
| --- | --- | --- |
| Tool use | Whether the system can actually call tools or APIs | Does it just talk, or can it really act? |
| Code execution | Whether it can run commands, tests, and scripts in a real environment | Does it only suggest changes, or can it execute them? |
| Memory | Whether it can preserve or retrieve useful context across time | Does it still know anything next session? |
| Orchestration | Whether it coordinates workflow instead of just answering prompts | Does it help move work forward? |
| Multi-agent | Whether it supports delegation, subagents, or parallel work | Is it one worker or several? |
| Human approval | Whether there are explicit review and interrupt points | Can you stop the risky actions? |
| Scheduling | Whether work can run on time or event triggers | Can it work in the background on a schedule? |
| Delivery surfaces | Where the system meets the operator | Terminal, editor, web, Slack, Telegram, device? |
| Deployment control | How much control the team has over the runtime boundary | Managed, self-hosted, local-first, framework-only? |

## How To Use These Dimensions

1. Mark the dimensions that are mandatory for your workflow.
2. Decide whether each one is a core strength or just incidental support.
3. Check the cost attached to that dimension: security, approvals, secrets, runtime burden, and operator overhead.