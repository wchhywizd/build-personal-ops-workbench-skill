# Implementation playbook

## Architecture selection

Prefer the smallest architecture that completes the confirmed loop:

```text
authorized sources → evidence normalization → MECE backend → local/service API → workbench UI → write-back confirmation
```

Preserve an existing application stack. For a new personal local tool, a zero- or low-dependency service and static frontend are acceptable when they improve reliability and auditability.

## Backend rules

### Feishu Base

Read `lark-shared` and `lark-base`. Verify identity and target. Create one new Base with five tables by default. Use a dry run when supported. Store only Base and table IDs in configuration; never store access tokens or app secrets.

### DingTalk AI Table

Read the installed `dws` skill and `aitable` references. Discover leaf schema and help before assembling commands. Use JSON output, batches no larger than 30 records, and a dedicated new Base/table set unless the user identifies an existing target.

### Local storage

Use SQLite when information must remain local or connectors are unavailable. Keep migrations explicit and seed data traceable. Offer export/import rather than silently syncing external systems.

## UI rules

Use an operational information hierarchy:

1. health and global actions;
2. KPIs backed by real records;
3. today's commitments;
4. prioritized project context;
5. activity evidence;
6. selected-object inspector.

Read `ui-style-options.md` and implement the three themes through semantic CSS/design tokens rather than three separate pages. Use `build-obsidian-dashboard-ui` when available for the black obsidian theme. Keep signal color for actionable objects, not every card.

Provide a labeled selector with three preview swatches in first-run setup or settings. It must be keyboard operable, expose selected state with text/icon in addition to color, persist the preference using local storage or the user's settings record, and fall back to the confirmed default. Never store work data in local storage merely to support theme selection.

Support:

- responsive navigation and inspector drawers;
- compact but readable data rows;
- semantic status labels, not color alone;
- keyboard-accessible primary flows;
- reduced motion and transparency;
- visible source mode: live, fixture, stale, or failed.
- functional parity across all three theme choices.

## Seed rules

Populate each module from authorized evidence. Use confidence labels:

- high: explicit structured record or direct statement;
- medium: consistent inference from multiple sources;
- low: weak activity heuristic requiring review.

Keep empty projects visible when their existence matters. Mark them empty rather than inventing work.

## Test modes

Maintain two modes when possible:

- `fixture`: deterministic browser and API regression without external mutation;
- `live`: real connector read and dedicated smoke-record write/read-back.

Test local logic first, browser flows second, live backend third, and live UI integration last. Use dedicated record IDs so smoke tests are idempotent.

## Delivery boundary

Explicitly state whether the result is local-only, remotely hosted, team-shared, scheduled, or manually refreshed. Do not imply a local service will survive restart unless a startup mechanism was created and tested.
