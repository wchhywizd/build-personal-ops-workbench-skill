# Build Personal Ops Workbench

让 AI 先理解你的工作，再为你生成真正可日常使用的个人工作台。

<img src="poster/build-personal-ops-workbench-poster.png" width="720" alt="Build Personal Ops Workbench 宣传长图" />

这个 Skill 会完成完整闭环：需求问询、多渠道资料授权、项目扫描、MECE 建模、飞书/钉钉/本地数据底座、三套 UI 风格、真实数据填充与端到端验收。

## 核心能力

- 先问需求：确认期望功能、日常闭环、使用人和数据位置。
- 多源分析：按授权读取飞书、钉钉、本地项目、聊天、群消息、周报、文档、任务、会议、邮件等信息。
- 三重权限门禁：读取、安装连接器、写回数据分别授权。
- MECE 五域模型：项目、任务、资产、活动、决策。
- 三套可切换 UI：黑曜石控制台、雾白效率台、暖砂编辑台。
- 真实数据底座：支持飞书多维表格、钉钉 AI 表格或本地 SQLite。
- 端到端验收：数据、功能、集成、体验、安全五域测试，真实写入后必须回读确认。

## Codex 安装

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo wchhywizd/build-personal-ops-workbench-skill \
  --path skill/build-personal-ops-workbench
```

安装后，在新任务中使用：

```text
使用 $build-personal-ops-workbench，先问询我的工作目标和资料授权，再分析我允许的飞书、钉钉或本地项目，为我生成有真实数据底座并通过端到端测试的个人工作台。
```

## 其他支持 SKILL.md 的 AI

把下面这段话发送给目标 AI：

```text
请从 https://github.com/wchhywizd/build-personal-ops-workbench-skill/tree/main/skill/build-personal-ops-workbench 安装这个 Skill 到你的技能目录。完整读取 SKILL.md，并保留 references、scripts 和 agents 目录。安装后不要立即扫描资料：先执行需求问询，分别获得读取、安装连接器和写回数据的授权，再开始生成工作台。
```

也可以手动克隆，将 `skill/build-personal-ops-workbench` 整个目录复制到目标 AI 的 Skills 目录。

## 使用边界

- 不会默认扫描整个个人目录、组织或邮箱。
- 不会默认保存原始私人聊天内容。
- 不会把文件数量、消息数量或活跃度伪装成业务成果。
- 不会因获得读取授权而自动安装工具、写数据或发送消息。

## 包结构

```text
skill/build-personal-ops-workbench/
├── SKILL.md
├── agents/openai.yaml
├── references/
└── scripts/
```

宣传长图位于 `poster/build-personal-ops-workbench-poster.png`。
