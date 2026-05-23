# Pi

[![ZH](https://img.shields.io/badge/ZH-CURRENT-dc2626?style=for-the-badge&labelColor=991b1b)](pi.md)
[![EN](https://img.shields.io/badge/EN-English-2563eb?style=for-the-badge&labelColor=1d4ed8)](../../agents/pi.md)
[![主页](https://img.shields.io/badge/%E8%BF%94%E5%9B%9E-%E4%B8%BB%E9%A1%B5-0d9488?style=for-the-badge&labelColor=0f766e)](../README.md)

一句话：Pi 是一个刻意做得很小、很有主张的 coding agent harness——只保留 agent loop、工具和 provider，其它交给扩展。

## 速读

| 项目 | 结论 |
| --- | --- |
| 厂商 | earendil-works（2026-04-08 从 Mario Zechner / badlogic 收购而来） |
| 路线 | 可自托管的终端 coding agent + agent toolkit |
| 开源 | 是（MIT，TypeScript） |
| 适合谁 | 想把 harness 保持精简、自己掌控编排选择的开发者 |
| 主要代价 | 自带 API key、自带 skill、自带"agent 该怎么扩展"的主张 |
| 官网 | https://lefos.ai/ |
| GitHub 仓库 | https://github.com/earendil-works/pi |

## 什么时候选它

- 想要一个 coding agent CLI，只默认带核心循环（read、write、edit、bash），其它通过 skills 和扩展按需补强。
- 想要广泛的 LLM 提供方支持——OpenAI、Anthropic、Google、vLLM pods——不绑定单一厂商表面。
- 愿意把工作会话回传到 Hugging Face 作为开源训练数据，这是项目明确鼓励的玩法。

## 什么时候不选它

- 想要一个开箱即用的产品，自带 teams、dashboard 和托管后台运行。
- 不想花时间挑选要接入哪些扩展和 skill。
- 需要打磨过的编辑器表面；Pi 是 terminal-first。

## 能力画像

| 维度 | 评估 | 说明 |
| --- | --- | --- |
| 终端工作流 | 很强 | CLI 是主表面 |
| Provider 覆盖 | 很强 | 统一 API 跨 OpenAI、Anthropic、Google、vLLM |
| 工具 harness | 强 | 默认 read、write、edit、bash；通过 skills、prompt 模板、扩展包补强 |
| 开箱编排 | 刻意做轻 | 编排交给调用方是设计意图 |
| 渠道（Slack、Web UI） | 以工具包形式提供 | TUI、Web UI、Slack bot 作为独立包发布 |

## 使用代价

复杂度 Medium。安装本身简单，但 Pi 默认你会自己挑模型、挑 skill、决定 agent 怎么扩展自己。"harness rebellion" 的定位是有意为之：少打包、多自决。

## 魔改 Pi：深度玩法手册

Pi 是被设计成"可以撬开"的。定制表面是四层结构，按"写多少代码 / 投入多少"从低到高排序。从最低层开始，只在低层表达不了时才往上爬。

| 层 | 是什么 | 什么时候用 | 文件放哪 |
| --- | --- | --- | --- |
| 1. Skills | Markdown + YAML frontmatter（兼容 anthropics/skills） | 想教 agent 一个工作流、一种习惯或一个领域词汇，但不想写代码 | `.pi/skills/`、`~/.pi/agent/skills/`、`~/.agents/skills/`，以及 package 的 `skills/` |
| 2. Prompt Templates | 由 slash command 展开的可复用 prompt | 你总在重复同一段话 | `.pi/prompts/`、`~/.pi/agent/prompts/` |
| 3. Extensions | TypeScript 模块，使用 `ExtensionAPI` 注册 tools / commands / 生命周期 hook / 自定义 UI | 你需要写真实代码：新工具、权限闸、外部集成、副作用 | `.pi/extensions/*.ts` 或 `.pi/extensions/<name>/index.ts` |
| 4. Packages | 用 npm 打包 extensions + skills + prompts + themes | 你想把工作流跨机器或跨团队共享、版本钉死 | 任意 npm 包，通过 `package.json` 里的 `pi.skills` / `pi.extensions` 被识别 |

### Layer 1 — Skills（从这里开始）

一个 skill 就是一个 markdown 文件。最小例子，放在 `.pi/skills/git-rebase-resolver/SKILL.md`：

```markdown
---
name: git-rebase-resolver
description: 遇到 git rebase 冲突时，逐文件交互式解决，每解决一个文件都要先跑测试。
---

# Git Rebase Resolver

1. 用 `read` 读冲突文件。
2. 每个冲突标记按上下文语义意图决定保留谁。
3. 解决完后、`git add` 前必须先跑项目的 pre-commit hook。
4. 继续 rebase；没有用户明确允许不要 squash。
```

Pi 会自动发现。Agent 只在 description 命中任务时才完整加载 `SKILL.md`（"progressive disclosure"），所以可以放很多 skill 而不烧上下文。也可以用 `/skill:git-rebase-resolver` 显式触发。

跨 harness 小技巧：放在 `~/.agents/skills/` 下，同一个 skill 文件能给 Pi、Claude Code、OpenAI Codex 共用——不用复制。

### Layer 2 — Prompt Templates

Prompt template 把 `/<command>` 展开成一段完整 prompt。当你的定制是"我每次都从同一段话开始"——而不是"我有一套工作流"时——用这一层。

示例：`.pi/prompts/ship.md` 文件就是 `/ship` 命令，展开成文件内容。可以传参数：`/ship feature-X` 会把 `feature-X` 暴露给模板。

Skill vs Prompt template：
- **Prompt template** —— 静态文本展开，你完全控制措辞。
- **Skill** —— agent 通过 description 匹配任务后自己挑出来的工作流。

### Layer 3 — Extensions（要写真实代码时）

这一层让 Pi 真正变成一个"你能重写"的 harness。Extension 是 TypeScript 模块，默认导出一个工厂函数：

```typescript
import type { ExtensionAPI } from "@earendil-works/pi-coding-agent";
import { Type } from "typebox";

export default function (pi: ExtensionAPI) {
  // 权限闸：拦截危险 bash 命令
  pi.on("tool_call", async (event, ctx) => {
    if (event.toolName !== "bash") return;
    const cmd = event.input.command as string;
    if (/rm\s+-rf|sudo|curl .* \| sh/.test(cmd)) {
      const ok = await ctx.ui.confirm("危险命令", cmd.slice(0, 100));
      if (!ok) return { block: true, reason: "用户拒绝" };
    }
  });

  // 自定义工具：从本地 tracker 拉 TODO
  pi.registerTool({
    name: "list_my_todos",
    label: "列出我的 TODO",
    description: "从本地 tracker 拉用户的 TODO 列表",
    parameters: Type.Object({ filter: Type.Optional(Type.String()) }),
    async execute(_id, params, _signal, _onUpdate, _ctx) {
      const todos = await loadFromLocalDb(params.filter);
      return {
        content: [{ type: "text", text: todos.join("\n") }],
        details: { count: todos.length },
      };
    },
  });

  // Slash command：开一个新的 review session
  pi.registerCommand("review", {
    description: "对当前 diff 开一个 review session",
    handler: async (_args, ctx) => {
      await ctx.newSession({ initialPrompt: "Review the staged diff..." });
    },
  });
}
```

文件放在 `.pi/extensions/my-ext.ts`，Pi 自动发现。要带依赖的 extension 用目录形式：`.pi/extensions/my-ext/{package.json, src/index.ts, node_modules/}`。

关键生命周期事件：

- 会话：`session_start`、`session_before_switch`、`session_shutdown`
- Agent loop：`before_agent_start`、`input`、`turn_start`、`turn_end`
- 工具：`tool_call`（可拦截）、`tool_result`（可改写）

`ctx.ui` 提供的 UI 原语：`confirm`、`select`、`input`、`notify`、`setStatus`、`setWidget`。

临时调试：`pi -e ./my-ext.ts`。

### Layer 4 — Packages（共享 + 版本钉死）

当你的 `.pi/` 收藏已经在产出真实价值时，把它升级成一个 npm 包。Pi 的 package 就是带约定的普通 npm 包：

```
my-pi-pack/
├── package.json   # 加 "pi.skills" / "pi.extensions" 字段
├── skills/
│   ├── git-rebase-resolver/SKILL.md
│   └── ship/SKILL.md
├── prompts/
│   └── ship.md
├── extensions/
│   └── permissions.ts
└── themes/
    └── solarized.json
```

`npm i @your-scope/my-pi-pack` 安装——Pi 会自动捡起四种资产。这是团队从"Bob 的机器上 skill 很好用"演进到"团队的 skill 在 package.json 里版本钉死"的方式。

## 组合 Recipes

### Recipe A：领域专精的 coding 工作流

让 Pi 在一个技术栈上特别擅长（比如 FastAPI + SQLAlchemy + Alembic）：

1. Skill `.pi/skills/alembic-migration/SKILL.md` —— 迁移工作流（生成 revision、dry-run、降级测试、commit 格式）。
2. Skill `.pi/skills/fastapi-route/SKILL.md` —— 路由 + 依赖注入 + 测试配对约定。
3. Prompt template `.pi/prompts/feature.md` —— `/feature` 展开为「新增一个 feature，按 alembic-migration 和 fastapi-route 这两个 skill 走...」
4. （可选）Extension `db-snapshot.ts` —— 注册 `snapshot_db` 工具，让 migration skill 能调用。

### Recipe B：个人安全 + 遥测 harness

一个本地严格的 Pi：危险操作必须确认，每次工具调用都记日志：

1. Extension `permissions.ts` —— `tool_call` handler 拦截没确认的 rm / sudo / curl-pipe-sh。
2. Extension `telemetry.ts` —— `tool_result` handler 写 JSONL 到 `~/.pi/log/`。
3. Skill `incident-replay/SKILL.md` —— 告诉 agent JSONL 日志路径，事后重建发生了什么时它知道去哪找。

### Recipe C：团队共享工作流

"团队怎么用 Pi" 的单一真实来源：

1. 把所有东西打成包：`@yourorg/pi-team-pack`。
2. 在每个仓库的 `package.json` 里钉死版本。
3. `npm install`——所有贡献者拿到一致的 skill、prompt、extension、theme。
4. 集中更新——`npm update` 把新工作流推给所有人。

## 反模式

- **能用 skill 的事情写了 extension。** 如果定制是"告诉 agent 怎么做"，那是 skill，不是 TypeScript。
- **把配置硬编码进 extension。** Pi 自己的贡献者规则说得很清楚：配置归配置面，不进代码。
- **跳过 skill 直接堆超长 prompt template。** Skill 组合更好、只在需要时加载；prompt template 每次调用都会膨胀。
- **本地没验证就直接发包。** 在 `.pi/` 里跑一周以上再考虑升级成 package。

## 底线

Pi 与 [Aider](aider.md)、[Claude Code](claude-code.md) 同属"终端 coding agent"路线，但刻意做得更小。2026-04-08 被 Earendil 收购（同时在做 Lefos 云端 agent 平台）之后，原本是个人项目的 Pi 拿到了真实资金。比起重型厂商产品，选 Pi 的真正理由是上面那张四层定制表——从一个 `SKILL.md` 起步，按需升级到 prompt template、extension、package。如果只是想"用别人的 agent"，挑厂商产品就够了。如果想"拥有自己的 harness"，这是最干净的起点。
