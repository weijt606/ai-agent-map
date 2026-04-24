# Semantic Kernel

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/semantic-kernel.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](semantic-kernel.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: Semantic Kernel is Microsoft's open-source SDK for building AI-orchestrated applications — the natural choice for .NET and Azure-aligned teams.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | Microsoft |
| Route | Enterprise AI orchestration SDK |
| Open source | Yes, MIT |
| Best for | .NET, Python, or Java teams that want typed, enterprise-grade AI orchestration with Azure alignment |
| Main cost | Strongest in the Microsoft ecosystem; Python community and third-party integrations are smaller than LangChain |
| Official website | https://learn.microsoft.com/semantic-kernel |
| GitHub repo | https://github.com/microsoft/semantic-kernel |

## When To Pick It

- Your stack is .NET, C#, or Java, and you want first-class AI orchestration in your language.
- You are building on Azure OpenAI and want native, well-maintained connectors.
- You need a plugin system — modular function groups (prompt-based or native code) that compose and reuse.
- You want auto-generated multi-step execution plans from user goals via Planners.
- You need built-in agent framework with multi-agent patterns, tool use, and conversation management.

## When Not To Pick It

- Your stack is Python-first and you need the broadest community ecosystem. LangChain is larger there.
- You need deep support for niche or non-Microsoft model providers out of the box.
- You want a visual no-code builder.
- You want a finished coding agent, not an orchestration SDK.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| AI orchestration | Very strong | Core strength — chains LLM calls with native code |
| Plugin system | Very strong | Modular, composable, reusable function groups |
| Planners | Strong | Auto-generate multi-step plans from goals |
| Agent framework | Strong | Multi-agent, tool use, conversation management |
| Memory / RAG | Medium | Vector store connectors for Azure AI Search, Qdrant, Chroma |
| Language support | Very strong | C#/.NET (most mature), Python, Java |
| Azure alignment | Very strong | Native Azure OpenAI integration |
| Non-Microsoft providers | Medium | Supported but less deep than LangChain |

## Operating Cost

Complexity is Medium. Well-documented, enterprise-grade, and strongly typed. The SDK is free (MIT). If you are already in the Microsoft ecosystem, integration is smooth. If you are not, you may find LangChain's broader community and third-party integrations more practical.

## Bottom Line

Semantic Kernel is the LangChain of the Microsoft world — typed, enterprise-grade, and Azure-native. If your team writes C# or Java, it is the obvious first choice for AI orchestration.
