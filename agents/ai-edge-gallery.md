# AI Edge Gallery

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/ai-edge-gallery.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](ai-edge-gallery.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: AI Edge Gallery is better understood as an on-device local assistant sandbox than as a mainstream coding agent.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Google AI Edge |
| Route | On-device local assistant sandbox |
| Open source | Yes |
| Best for | Trying local mobile models, agent skills, multimodal inputs, and private on-device actions |
| Main cost | It is mainly a mobile edge-runtime sandbox, so it is off the direct path for coding automation |
| Official website | https://ai.google.dev/edge |
| GitHub repo | https://github.com/google-ai-edge/gallery |

## When To Pick It

- You want to test what local on-device assistants can do on a phone or tablet right now.
- You care about privacy, offline execution, and mobile actions more than cloud orchestration.
- You want a practical sandbox for model choice, prompts, agent skills, and edge-device trade-offs.

## When Not To Pick It

- You want repo-local coding automation or issue-to-PR execution.
- You need a desktop-first orchestration platform with rich developer workflow controls.
- You want a finished enterprise agent surface rather than an experimental edge app.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| On-device execution | Very strong | Local inference on mobile hardware is the center of the story |
| Model sandboxing | Very strong | Useful for trying multiple local models on real hardware |
| Agent skills / actions | Medium | Present and interesting, but not the only reason to use it |
| Privacy / offline usage | Very strong | A major reason to look at it |
| Coding automation | Weak | This is not where it is strongest |

## Operating Cost

Complexity is Low. It is easier to try than most self-hosted runtimes, but your real constraints become device compatibility, memory limits, and the fact that this is more of an edge experimentation surface than a full workflow platform.

## Bottom Line

If your question is "what can a local mobile assistant do entirely on-device right now," AI Edge Gallery is worth exploring. If your question is "which coding agent should my team adopt," it is usually not the first stop.