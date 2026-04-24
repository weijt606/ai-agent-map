# LiteLLM

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](litellm.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/litellm.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：LiteLLM 是开源 AI 网关，用统一的 OpenAI 兼容接口调用 100+ LLM API，带负载均衡、预算控制和成本追踪。

## 一眼判断

| 项目 | 结论 |
| --- | --- |
| 厂商 | BerriAI, Inc. |
| 路线 | LLM API 网关和代理 |
| 是否开源 | 是，MIT |
| 最适合 | 同时用多家 LLM provider、想统一接口加路由、预算和可观测性的团队 |
| 主要代价 | 自托管基础设施（Docker、Redis、PostgreSQL）；高并发下延迟受限 |
| 官网 | https://www.litellm.ai |
| GitHub 仓库 | https://github.com/BerriAI/litellm |

## 什么时候选它

- 你调用多家 LLM provider，想要一个统一的 OpenAI 兼容接口。
- 你需要按 key 和按团队的预算控制，实时成本追踪。
- 你想要跨 provider 的负载均衡、限流、fallback 和重试。
- 你需要可观测性——导出到 Langfuse、Prometheus、OpenTelemetry。

## 什么时候别选

- 你只用一家 LLM provider。网关只会增加复杂度而没有收益。
- 你需要高吞吐、低延迟的生产环境——Python GIL 限制并发。
- 你想要零运维。LiteLLM 的高可用部署不简单。
- 你需要企业治理（SSO、细粒度 RBAC）又不想付费 Enterprise。

## 能力侧写

| 维度 | 判断 | 备注 |
| --- | --- | --- |
| 统一 LLM API | 很强 | 100+ provider，OpenAI 兼容格式 |
| 负载均衡 | 强 | 跨 provider，支持 fallback 和重试 |
| 预算控制 | 强 | 按 key 和按团队的花费限制 |
| 成本追踪 | 强 | 实时，可导出到可观测工具 |
| 限流 | 强 | RPM 和 TPM 控制 |
| 高吞吐 | 中 | Python GIL 在高并发下受限 |
| 企业功能 | 中 | SSO 和高级 RBAC 需要付费 |

## 使用代价

复杂度 Medium 到 High。软件免费（MIT），但你需要自己管基础设施——Docker 主机、Redis 做状态管理、PostgreSQL 做日志。高可用部署需要仔细规划。回报是在整个组织内集中管理 LLM 访问。

## 最后一句

LiteLLM 是用多家 LLM provider 的团队的基础设施层。它不搭 agent——它统一了 agent 所依赖的模型访问。
