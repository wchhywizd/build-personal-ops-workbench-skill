---
name: build-personal-ops-workbench
description: Discover requirements from user interviews and authorized work sources, offer three selectable UI styles, inventory projects, model a MECE personal operating system, create a Feishu Base, DingTalk AI Table, or local data backend, build a polished daily workbench, seed it with real evidence, and verify it end to end. Use when a user asks to build or rebuild a personal dashboard, cross-project workbench, daily operating console, project cockpit, task-and-decision hub, or wants Codex to analyze authorized Feishu, Lark, DingTalk, local files, chats, group messages, reports, meetings, email, calendar, or other work sources before producing such a system.
---

# Build Personal Ops Workbench

Turn scattered work signals into a daily operating loop: **collect evidence → identify projects and commitments → prioritize → act → record outcomes → review decisions**. Build a working product backed by traceable data, not a decorative dashboard.

## Introduce the skill before discovery

Start every new engagement with this short explanation, adapted to the user:

> 这个 Skill 会先确认你的工作目标和资料授权，再从你允许的本地项目、飞书、钉钉或其他渠道提取项目、任务、资产、活动与决策，生成可日常使用的工作台和数据底座，并用真实数据完成端到端验收。默认只读分析；安装工具、写入数据和发送消息都需要单独授权。

Then ask the first-round questions in one concise turn:

1. **你期望的功能是什么？** 这个工作台每天必须帮你完成哪些动作？请给出最重要的 3–5 项功能或结果。
2. **是否需要我通过钉钉、飞书或其他渠道的资料直接分析并产出？** 可选本地项目、聊天记录、群消息、日报/周报、文档、任务、日历、会议纪要、邮件或其他来源；也可以选择只使用你手动提供的材料。
3. **谁使用、数据放哪里？** 个人还是团队使用；希望存入飞书多维表格、钉钉 AI 表格、本地数据库或其他系统。
4. **你偏好哪种 UI 风格？** 展示 [references/ui-style-options.md](references/ui-style-options.md) 中的三张风格卡：黑曜石控制台、雾白效率台、暖砂编辑台。用户可选择默认风格；生成的工作台仍须提供三风格切换入口。

Use a structured input tool when available. Otherwise ask in plain language. Do not ask every detailed question before the user chooses a source.

## Run the workflow

### 1. Gate requirements and authority

Read [references/intake-and-consent.md](references/intake-and-consent.md). Ask only the follow-ups relevant to the user's selected sources and output.

Separate authority into three explicit gates:

- **Read gate:** inspect named sources, identities, organizations, groups, and time ranges.
- **Install gate:** install or update a CLI, plugin, or dependency.
- **Write gate:** create tables, seed records, update live data, send messages, or change permissions.

Never infer one gate from another. Reading a chat does not authorize posting to it. Creating a workbench does not authorize deleting or overwriting existing data.

Record the agreed scope as `intake.json`. Run:

```bash
python scripts/intake_gate.py intake.json
```

Do not build until `analysis_ready` is true. Do not mutate a live backend until `write_ready` is true.

### 2. Acquire evidence from selected sources

Read [references/source-connectors.md](references/source-connectors.md) only for the selected connectors.

Use this order:

1. Prefer an already available app, MCP tool, or CLI.
2. Check authentication and exact command capabilities using read-only discovery.
3. If missing, explain what the connector unlocks and ask permission to install it.
4. Query only the authorized identities, organizations, groups, content types, and time range.
5. Preserve provenance; retain derived summaries instead of raw private content unless the user explicitly requests raw retention.

For local project discovery, run only against roots the user placed in scope:

```bash
python scripts/inventory_projects.py /authorized/root/one /authorized/root/two
```

Normalize each evidence item with `source`, `source_id`, `captured_at`, `time`, `project_hint`, `summary`, `confidence`, and `privacy_class`.

### 3. Infer needs without inventing results

Distinguish:

- explicit user requirements;
- observed recurring actions;
- inferred needs requiring confirmation;
- activity signals that do not prove outcomes;
- stale, duplicated, or low-confidence evidence.

Return a compact discovery brief before implementation:

1. real problem;
2. minimum daily loop;
3. proposed 3–5 core functions;
4. features to defer;
5. true signals and false-signal risks;
6. source coverage and evidence gaps;
7. decisions requiring confirmation.

Ask for confirmation only when a choice materially changes scope, storage, privacy, or architecture. Otherwise state reasonable assumptions and continue.

### 4. Build the MECE operating model

Read [references/mece-model-and-testing.md](references/mece-model-and-testing.md). Use these default domains unless evidence justifies another decomposition:

| Domain | Answers | Excludes |
|---|---|---|
| Projects | What is being operated? | Individual actions and event logs |
| Tasks | What is committed next? | Passive observations |
| Assets | What can be reused? | Mere file activity |
| Activities | What happened and when? | Unverified outcome claims |
| Decisions | What requires or records judgment? | Routine task execution |

Every project should have a goal, current evidence, owner, status, priority, milestone, and next action. Keep evidence traceable to its source.

### 5. Create the data backend

Read [references/implementation-playbook.md](references/implementation-playbook.md).

Select the backend from the confirmed requirement:

- Feishu/Lark → use `lark-base` and `lark-shared` instructions.
- DingTalk → use the installed `dws` skill and its `aitable` instructions.
- Local/private → use SQLite or project-native storage.
- Existing enterprise system → preserve its schema and API conventions.

Perform a dry run when supported. Create new containers instead of altering unrelated tables. Store IDs and non-secret configuration separately; never persist tokens, App Secrets, cookies, or raw credentials in source files.

Seed every visible module with authorized existing data. Mark inferred fields and low-confidence items; do not fabricate plausible-looking metrics.

### 6. Build the daily workbench

Preserve the detected stack. If no suitable app exists, build the smallest runnable frontend and local service that completes the daily loop.

Read [references/ui-style-options.md](references/ui-style-options.md). Implement all three tokenized UI themes and use the user's choice as the default. Provide an accessible theme selector during first run or in settings, persist only the theme preference locally, and keep information architecture and functionality identical across themes.

When the default is `obsidian-control` and the skill is available, use `build-obsidian-dashboard-ui` for the visual implementation. Keep the product operational:

- overview with actionable signals;
- project portfolio and context inspector;
- task creation and status write-back;
- reusable asset inventory;
- activity evidence timeline;
- decision queue;
- global search and filters;
- visible source health and synchronization feedback.

Do not add chat, calendar, analytics, automation, or AI panels unless they close a confirmed user loop.

### 7. Verify end to end with MECE coverage

Test five non-overlapping quality domains:

1. **Data integrity:** schema, counts, provenance, normalization, idempotency.
2. **Functional behavior:** read, search, filter, inspect, create, update, synchronize, link-out.
3. **Integration:** browser → local API → live backend → read-back confirmation.
4. **Experience:** desktop/mobile layout, keyboard, touch targets, focus, reduced motion, error feedback.
5. **Safety and resilience:** invalid input, missing permissions, eventual consistency, partial source failure, no secret leakage.

Do not declare a live write successful only because an API returned success. Read it back with bounded polling when the platform is eventually consistent.

Visually inspect representative desktop and mobile screenshots. Fix discovered issues and rerun affected tests. Produce an acceptance matrix with test IDs, evidence, result, known boundaries, and bugs fixed.

Test each UI theme for selection, persistence after reload, readable contrast, responsive layout, and functional parity. A theme may change tokens, materials, density within defined limits, and motion treatment; it must not hide or change business capabilities.

### 8. Deliver a reusable system

Hand off:

- running workbench URL and start command;
- backend URL and table/domain map;
- source inventory and authorization boundary;
- populated record counts;
- acceptance report and screenshots;
- open risks, empty-signal areas, and deferred features;
- update/sync instructions;
- reusable skill or project assets created.

State the long-term narrative: personal information hub → cross-project operating system → evidence-driven agent execution. Keep future expansion tied to verified recurring needs.

## Safety rules

- Never scan broad home directories, organizations, groups, or mailboxes without explicit scope.
- Never retain raw private chats by default; prefer source-linked derived facts.
- Never send, delete, recall, invite, change permissions, or overwrite live data without explicit authority.
- Never claim messages, files, commits, or meeting attendance prove business impact.
- Never expose tokens or credentials in code, logs, screenshots, reports, or generated test fixtures.
- Never silently install or update connector software.
