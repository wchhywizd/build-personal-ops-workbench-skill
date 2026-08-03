# UI style options

Offer these three choices during requirements discovery and in the generated workbench. Keep layout, semantics, data, and controls consistent; implement differences through tokens and component material rules.

## Choice cards shown to the user

### 1. 黑曜石控制台 — `obsidian-control`

**感觉：** 深色、克制、精密、电影感。

**适合：** 高频项目管理、数据密集型运营、夜间使用。

**视觉：** 近黑画布、烟熏玻璃、冷白细边、信号绿主强调、立体项目卡组。
**取舍：** 信息密度最高；必须严格控制暗色对比度和模糊范围。

When available, use `build-obsidian-dashboard-ui`. Use one signal-green accent family and small semantic warning/danger colors.

Core tokens:

```css
[data-theme="obsidian-control"] {
  --canvas: #050607;
  --surface-1: #0a0c0f;
  --surface-2: #101318;
  --line: rgba(255,255,255,.09);
  --text-1: #f3f5f7;
  --text-2: #a9afb7;
  --accent: #20c96b;
  --accent-bright: #35f18a;
}
```

### 2. 雾白效率台 — `mist-light`

**感觉：** 明亮、理性、轻盈、低干扰。

**适合：** 白天办公、文档与任务并重、偏好传统效率工具的用户。

**视觉：** 雾白背景、石墨文字、白色工作面、低阴影、清晰分割线、冷静蓝强调。
**取舍：** 扫读最轻松；避免大面积纯白和无层级的“表格软件感”。

Core tokens:

```css
[data-theme="mist-light"] {
  --canvas: #eef1f4;
  --surface-1: #f9fafb;
  --surface-2: #ffffff;
  --line: rgba(18,28,40,.11);
  --text-1: #17202b;
  --text-2: #596574;
  --accent: #3268d6;
  --accent-bright: #4c7ee3;
}
```

Use crisp borders, restrained elevation, and slightly more whitespace than the obsidian theme. Do not add glass blur.

### 3. 暖砂编辑台 — `warm-editorial`

**感觉：** 温暖、沉静、有人味、适合思考。

**适合：** 内容创作、知识管理、决策复盘和长期规划。

**视觉：** 暖砂画布、纸张色工作面、炭黑文字、赤陶/琥珀强调、编辑式标题与细规则线。
**取舍：** 叙事性最强；正文仍使用中性无衬线，避免把工作台做成杂志封面。

Core tokens:

```css
[data-theme="warm-editorial"] {
  --canvas: #e9e2d7;
  --surface-1: #f3eee6;
  --surface-2: #fbf7f0;
  --line: rgba(54,43,34,.14);
  --text-1: #28231f;
  --text-2: #6b6259;
  --accent: #b95636;
  --accent-bright: #cf6b48;
}
```

Use warm shadows, subtle paper-like value separation, and slightly larger section headings. Avoid fake paper textures that reduce legibility.

## Selector requirements

- Display three named cards with a miniature color/material preview and one-sentence use case.
- Use a radio group or equivalent single-select semantics.
- Expose `aria-checked` or native checked state.
- Maintain 44×44 px minimum touch targets.
- Show selection with border, icon, and text—not color alone.
- Apply the selected theme immediately for preview.
- Persist the theme key and restore it before first paint when possible.
- Offer “跟随已确认默认值” when storage is unavailable; do not introduce a fourth visual theme.

## Functional invariants

Across themes, keep identical:

- navigation and information hierarchy;
- record counts and filtering;
- create/update/write-back operations;
- inspector fields and status semantics;
- loading, empty, error, and permission states;
- responsive breakpoints and accessibility behavior.

Theme choice is presentation preference, not a separate product variant.
