# Intake and consent

## Purpose

Discover enough context to build the right operating loop while minimizing questions and protecting private work data.

## Progressive questionnaire

### Round 1: mandatory outcome questions

Ask together:

1. What should the workbench help the user accomplish every day?
2. Which 3–5 functions are essential for version one?
3. Should the skill directly analyze authorized DingTalk, Feishu/Lark, local projects, or other sources, or use only materials supplied in the conversation?
4. Who will use it and where should data be stored?
5. Which of the three UI directions should be the initial default: black obsidian, mist-light, or warm editorial? Explain that the finished UI includes all three choices.

If the user gives a broad request such as “analyze everything,” explain that a source and time boundary is still required.

### Round 2: selected-source questions

Ask only for selected sources.

| Dimension | Question |
|---|---|
| Identity | Which account/profile and organization should be used? |
| Objects | Which groups, projects, folders, docs, task lists, calendars, mailboxes, or report templates? |
| Time | What date range represents current work: 7, 30, 90 days, current quarter, or custom? |
| Content | Chats, group messages, reports, docs, tasks, meetings, email, calendar, approvals, files, or all selected? |
| People | Personal-only, direct team, named collaborators, or organization-wide? |
| Privacy | Which topics, people, groups, keywords, or folders are excluded? |
| Retention | Derived facts only, excerpts, or authorized raw copies? Default to derived facts only. |
| Confidence | Should inferred requirements require confirmation before build? Default to confirm material inferences. |

### Round 3: implementation questions

Ask only choices that materially change the product:

- new or existing backend;
- personal or team access;
- read-only dashboard or write-back operations;
- local-only or remotely hosted;
- desired visual style or supplied reference;
- default UI style and whether organization branding should override only logo/type, not the three-theme structure;
- refresh cadence and whether automation is in scope.

## Authority ledger

Represent each permission independently:

```json
{
  "read": {
    "authorized": true,
    "sources": ["feishu"],
    "scope": ["named groups", "weekly reports"],
    "time_range": "last 30 days"
  },
  "install": {
    "authorized": false,
    "tools": []
  },
  "write": {
    "authorized": true,
    "targets": ["new Feishu Base only"]
  }
}
```

Do not treat general approval as authorization for destructive or outward-facing actions.

## Intake file

Use this shape for `intake.json`:

```json
{
  "expected_outcomes": ["Know today's highest-value actions"],
  "core_functions": ["project overview", "task write-back", "decision queue"],
  "daily_loop": "scan, choose, act, record, review",
  "users": ["personal"],
  "sources": [
    {
      "type": "feishu",
      "scope": ["named groups", "weekly reports"],
      "time_range": "last 30 days",
      "read_authorized": true,
      "retention": "derived-only"
    }
  ],
  "storage": { "type": "feishu-base", "target": "new" },
  "ui_style": { "default": "obsidian-control", "enable_switcher": true },
  "install_authorized": false,
  "writeback_authorized": true,
  "privacy_redlines": ["exclude HR and compensation groups"]
}
```

Run `scripts/intake_gate.py` and address missing items before acquisition or build.

## Discovery brief template

```markdown
### Real problem
...

### Minimum daily loop
...

### V1 functions
1. ...

### Defer
- ...

### Source coverage
- Confirmed: ...
- Inferred: ...
- Missing: ...

### Authority boundary
- Read: ...
- Install: ...
- Write: ...
```
