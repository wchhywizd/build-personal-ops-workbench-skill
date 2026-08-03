# MECE model and testing

## Canonical data model

### Projects

Required: `id`, `name`, `goal`, `owner`, `status`, `priority`, `milestone`, `next_action`, `evidence`, `confidence`, `source`.

Use for durable operating objects. Do not use projects as folders for every topic.

### Tasks

Required: `id`, `name`, `project_id`, `owner`, `status`, `priority`, `is_today`, `due_at`, `next_action`, `acceptance`, `evidence`, `source`.

A task is a commitment with an observable completion condition. A message or file update is not automatically a task.

### Assets

Required: `id`, `name`, `project_id`, `type`, `location`, `status`, `modified_at`, `reuse_value`, `source`.

An asset must have potential reuse or delivery value. Ignore cache and generated noise.

### Activities

Required: `id`, `title`, `project_id`, `type`, `time`, `summary`, `confidence`, `source`, `source_id`.

Activity proves that something occurred, not that it produced impact.

### Decisions

Required: `id`, `name`, `project_id`, `type`, `status`, `priority`, `facts`, `recommendation`, `result`, `source`.

Use for choices, risks, hypotheses, approvals, and confirmed outcomes. Do not duplicate routine task statuses.

## Signal rules

Prefer:

- explicit commitment over conversational intent;
- delivered artifact over file count;
- read-back state over API success response;
- dated decision over inferred preference;
- owner-confirmed milestone over recent activity;
- multiple consistent sources over one ambiguous message.

Label inference and confidence. Keep conflicting evidence instead of silently choosing a preferred story.

## MECE acceptance matrix

### 1. Data integrity

- unique stable IDs;
- every visible module populated or explicitly empty;
- source IDs and confidence retained;
- select, multiselect, date, boolean, and text round-trip correctly;
- synchronization is idempotent;
- stale and duplicate records are handled deterministically.

### 2. Functional behavior

- overview loads;
- navigation reaches every module;
- global search filters and clears;
- filters are correct;
- detail inspector matches the selected record;
- create and update flows validate input;
- synchronization provides visible feedback;
- source links open the intended system.

### 3. Integration

- browser reads through the service from the live backend;
- writes travel browser → service → connector → backend;
- created or updated records are read back;
- eventual consistency uses bounded polling;
- connector identity and target container are verified.

### 4. Experience

- 1440, 1024, 768, and 375 widths do not overlap or overflow;
- mobile controls are at least 44×44 px;
- keyboard and focus behavior work;
- reduced motion/transparency preserve comprehension;
- loading, empty, success, error, disabled, selected, and hover states are visible;
- screenshots are visually inspected, not only generated.
- all three themes can be selected with mouse, keyboard, and touch;
- the selected theme survives reload and preserves every business control;
- representative desktop and mobile screenshots are inspected for each theme.

### 5. Safety and resilience

- invalid input yields actionable errors;
- missing scopes do not cause partial silent results;
- source failures are attributed;
- no credentials appear in files, logs, screenshots, or reports;
- write tests use dedicated records or containers;
- destructive and outward-facing operations require explicit confirmation.

## Acceptance report shape

For each test include:

| ID | Domain | Scenario | Expected | Evidence | Result |
|---|---|---|---|---|---|

Finish with record counts, bugs found and fixed, known boundaries, and deferred risks. A passing test suite without visual inspection or live read-back is not end-to-end acceptance.
