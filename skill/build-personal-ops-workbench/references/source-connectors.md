# Source connectors

Use only the sections selected during intake. Connector behavior and commands can drift; verify the installed version and leaf help before executing business queries.

## Universal connector sequence

1. Detect an installed app, MCP tool, or CLI.
2. Inspect version, authentication, and available read commands.
3. If absent, explain benefits and request install authorization.
4. Use official/current installation documentation; do not guess package names.
5. Authenticate interactively without exposing credentials.
6. Preview scope and expected record volume.
7. Read in bounded pages or batches.
8. Normalize evidence and record provenance.
9. Keep raw content ephemeral unless raw retention was authorized.

## DingTalk

Prefer the available `dws` skill and CLI. Read its complete `SKILL.md`, then load only the relevant product references.

### Setup and discovery

```bash
command -v dws
dws version
dws profile list --format json
dws schema chat --compact
dws schema report --compact
dws schema doc --compact
```

If `dws` is missing, ask whether to install it. Search current official installation guidance and request approval for the exact command. After installation, authenticate and let the user choose the profile when an organization has multiple accounts.

Use `--format json` for business commands. For shortcuts, inspect:

```bash
dws shortcut list --service chat --format json
dws chat +<shortcut> --help
```

Do not guess a chat, group, user, template, document, or organization ID. Resolve it through read-only search/list commands.

### Useful evidence families

- `chat`: named group messages, direct messages, mentions, saved messages;
- `report`: daily and weekly reports, submissions, templates;
- `doc` and `wiki`: plans, SOPs, decisions, specifications;
- `todo`: commitments and completion status;
- `calendar` and `minutes`: meetings, summaries, actions, participants;
- `mail`: decisions and commitments not present in chat;
- `aitable`: existing structured project or operational data.

Use bounded history reads for analysis. Use `dws event consume ... --flatten` only for explicitly requested real-time monitoring; do not poll chat history as an event substitute.

## Feishu / Lark

Prefer the available Feishu/Lark app tools. Otherwise use `lark-cli` and its embedded skills.

### Setup and discovery

```bash
command -v lark-cli
lark-cli auth status
lark-cli skills list
lark-cli skills read lark-shared
```

If missing, ask whether to install it. Look up the current official installation method rather than assuming a package name. Do not run `lark-cli update` silently when an update notice appears.

Load the selected embedded skill before use:

```bash
lark-cli skills read lark-im
lark-cli skills read lark-doc
lark-cli skills read lark-base
lark-cli skills read lark-calendar
lark-cli skills read lark-task
lark-cli skills read lark-vc
lark-cli skills read lark-minutes
lark-cli skills read lark-mail
```

Use the skill's current help and dry-run behavior. Relevant evidence families:

- `lark-im`: group and direct message history;
- `lark-doc`, `lark-wiki`, `lark-drive`: plans, SOPs, project documents;
- `lark-task`: assigned and personal commitments;
- `lark-calendar`, `lark-vc`, `lark-minutes`: schedule, meeting facts, summaries, actions;
- `lark-mail`: decisions and commitments;
- `lark-base`, `lark-sheets`: structured operational data.

Do not expand user identity scopes or request additional OAuth scopes without explaining why they are required.

## Local projects and files

Require explicit root paths. Do not default to `$HOME`, `/`, or broad cloud-sync roots.

Use `scripts/inventory_projects.py` for first-pass discovery, then read the highest-signal files:

- `AGENTS.md`, `README*`, `PROJECTS*`, `OPERATING_SYSTEM*`;
- specifications, plans, decisions, test reports, and recent summaries;
- package manifests and source structure for implementation facts;
- recent file metadata as activity evidence only.

Ignore caches, dependencies, build output, browser profiles, secrets, and binary collections. Never print `.env`, tokens, cookies, SSH material, keychains, or credential stores.

## Other channels

Support Notion, Google Drive, Slack, Teams, Outlook, Jira, GitHub, email exports, calendars, databases, and user-supplied archives when available.

Prefer an installed connector or official API. Ask the same scope, time, privacy, retention, install, and write questions. If no connector exists, accept user-provided exports and state freshness limitations.

## Evidence normalization

Store derived records using a shape like:

```json
{
  "source": "feishu-im",
  "source_id": "opaque-source-id",
  "captured_at": "2026-08-03T12:00:00Z",
  "time": "2026-08-02T09:30:00Z",
  "project_hint": "workbench",
  "summary": "Owner committed to complete mobile QA this week",
  "confidence": "high",
  "privacy_class": "internal-derived",
  "evidence_type": "commitment"
}
```

Do not store full message text when a derived fact and source link are sufficient.
