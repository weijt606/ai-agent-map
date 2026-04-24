# LiteLLM

[![ZH](https://img.shields.io/badge/ZH-%E4%B8%AD%E6%96%87-dc2626?style=for-the-badge&labelColor=991b1b)](../zh/agents/litellm.md)
[![EN](https://img.shields.io/badge/EN-CURRENT-2563eb?style=for-the-badge&labelColor=1d4ed8)](litellm.md)
[![Home](https://img.shields.io/badge/HOME-README-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

One-line take: LiteLLM is an open-source AI gateway that lets you call 100+ LLM APIs through a unified OpenAI-compatible interface with load balancing, budgets, and cost tracking.

## Quick Read

| Item | Conclusion |
| --- | --- |
| Vendor | BerriAI, Inc. |
| Route | LLM API gateway and proxy |
| Open source | Yes, MIT |
| Best for | Teams running multiple LLM providers who want a single API interface with routing, budgets, and observability |
| Main cost | Self-hosted infra (Docker, Redis, PostgreSQL); latency under heavy concurrency |
| Official website | https://www.litellm.ai |
| GitHub repo | https://github.com/BerriAI/litellm |

## When To Pick It

- You call multiple LLM providers and want a single OpenAI-compatible interface.
- You need per-key and per-team budget controls with real-time cost tracking.
- You want load balancing, rate limiting, fallbacks, and retries across providers.
- You need observability — export to Langfuse, Prometheus, OpenTelemetry.
- You want virtual API keys for team management.

## When Not To Pick It

- You only use one LLM provider. The gateway adds complexity for no benefit.
- You need high-throughput production with minimal latency — Python GIL limits concurrency.
- You want zero operational overhead. Running LiteLLM in HA is nontrivial.
- You need enterprise governance (SSO, granular RBAC) without paying for Enterprise.

## Capability Shape

| Dimension | Assessment | Notes |
| --- | --- | --- |
| Unified LLM API | Very strong | 100+ providers in OpenAI-compatible format |
| Load balancing | Strong | Across providers with fallbacks and retries |
| Budget controls | Strong | Per-key and per-team spend limits |
| Cost tracking | Strong | Real-time with export to observability tools |
| Rate limiting | Strong | RPM and TPM controls |
| High-throughput | Medium | Python GIL limits under heavy concurrency |
| Enterprise features | Medium | SSO and advanced RBAC require paid tier |

## Operating Cost

Complexity is Medium to High. The software is free (MIT), but you own the infrastructure — Docker host, Redis for state, PostgreSQL for logging. HA deployment requires careful planning. The payoff is centralized LLM management across your entire organization.

## Bottom Line

LiteLLM is the infrastructure layer for teams that run multiple LLM providers. It does not build agents — it unifies the model access that agents depend on.
