#!/usr/bin/env python3
"""Validate workbench intake and report analysis/write readiness."""

import argparse
import json
from pathlib import Path


EXTERNAL_SOURCES = {"feishu", "lark", "dingtalk", "slack", "teams", "notion", "google-drive", "email", "calendar"}
UI_STYLES = {"obsidian-control", "mist-light", "warm-editorial"}


def nonempty_list(value):
    return isinstance(value, list) and any(str(item).strip() for item in value)


def validate(data):
    missing = []
    warnings = []

    if not nonempty_list(data.get("expected_outcomes")):
        missing.append("expected_outcomes: at least one desired outcome")
    if not nonempty_list(data.get("core_functions")):
        missing.append("core_functions: 3-5 version-one functions")
    if not str(data.get("daily_loop", "")).strip():
        missing.append("daily_loop: the user's recurring operating loop")
    if not nonempty_list(data.get("users")):
        missing.append("users: personal or named team audience")

    sources = data.get("sources")
    if not isinstance(sources, list) or not sources:
        missing.append("sources: at least manual, local, or one authorized connector")
        sources = []

    for index, source in enumerate(sources):
        label = f"sources[{index}]"
        source_type = str(source.get("type", "")).strip().lower()
        if not source_type:
            missing.append(f"{label}.type")
            continue
        if source_type in EXTERNAL_SOURCES:
            if not source.get("read_authorized", False):
                missing.append(f"{label}.read_authorized")
            if not nonempty_list(source.get("scope")):
                missing.append(f"{label}.scope: named objects or bounded category")
            if not str(source.get("time_range", "")).strip():
                missing.append(f"{label}.time_range")
            if not str(source.get("retention", "")).strip():
                warnings.append(f"{label}.retention defaults to derived-only")
        if source_type == "local" and not nonempty_list(source.get("scope")):
            missing.append(f"{label}.scope: explicit root paths")

    storage = data.get("storage")
    if not isinstance(storage, dict) or not str(storage.get("type", "")).strip():
        missing.append("storage.type")

    ui_style = data.get("ui_style")
    if not isinstance(ui_style, dict) or ui_style.get("default") not in UI_STYLES:
        missing.append("ui_style.default: obsidian-control, mist-light, or warm-editorial")
    elif ui_style.get("enable_switcher") is not True:
        missing.append("ui_style.enable_switcher: must be true so the generated UI offers all three styles")

    analysis_ready = not missing
    external_storage = isinstance(storage, dict) and storage.get("type") not in {None, "local", "sqlite", "fixture"}
    write_ready = analysis_ready and (not external_storage or data.get("writeback_authorized") is True)
    if analysis_ready and external_storage and not write_ready:
        warnings.append("writeback_authorized is required before creating or seeding the external backend")
    if data.get("install_authorized") is not True:
        warnings.append("connector installation is not authorized; use installed tools or ask before installing")

    return {
        "ok": analysis_ready,
        "analysis_ready": analysis_ready,
        "write_ready": write_ready,
        "missing": missing,
        "warnings": warnings,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("intake", type=Path)
    args = parser.parse_args()
    data = json.loads(args.intake.read_text(encoding="utf-8"))
    result = validate(data)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["analysis_ready"] else 2)


if __name__ == "__main__":
    main()
