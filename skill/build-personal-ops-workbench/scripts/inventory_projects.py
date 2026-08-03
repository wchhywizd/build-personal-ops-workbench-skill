#!/usr/bin/env python3
"""Discover project candidates under explicit authorized roots."""

import argparse
import json
import os
from datetime import datetime, timezone
from pathlib import Path


MARKERS = {".git", "AGENTS.md", "README.md", "package.json", "pyproject.toml", "Cargo.toml", "go.mod", "pom.xml"}
EXCLUDES = {".git", ".next", ".cache", ".venv", "venv", "node_modules", "dist", "build", "coverage", "tmp", "temp", "__pycache__", "Library"}


def inspect_project(path, max_files):
    count = 0
    latest_path = None
    latest_mtime = 0.0
    for current, dirs, files in os.walk(path):
        dirs[:] = [name for name in dirs if name not in EXCLUDES and not name.startswith(".cache")]
        for name in files:
            candidate = Path(current, name)
            try:
                stat = candidate.stat()
            except OSError:
                continue
            count += 1
            if stat.st_mtime > latest_mtime:
                latest_mtime = stat.st_mtime
                latest_path = candidate
            if count >= max_files:
                break
        if count >= max_files:
            break
    return {
        "path": str(path.resolve()),
        "name": path.name,
        "file_count_sampled": count,
        "latest_file": str(latest_path.resolve()) if latest_path else None,
        "latest_modified_at": datetime.fromtimestamp(latest_mtime, timezone.utc).isoformat() if latest_mtime else None,
        "markers": sorted(name for name in MARKERS if (path / name).exists()),
    }


def discover(root, max_depth, max_files):
    root = root.resolve()
    if not root.exists() or not root.is_dir():
        raise ValueError(f"Not a directory: {root}")
    projects = []
    seen = set()
    for current, dirs, _ in os.walk(root):
        path = Path(current)
        depth = len(path.relative_to(root).parts)
        dirs[:] = [name for name in dirs if name not in EXCLUDES and not name.startswith(".")]
        if depth > max_depth:
            dirs[:] = []
            continue
        if any((path / marker).exists() for marker in MARKERS):
            resolved = str(path.resolve())
            if resolved not in seen:
                projects.append(inspect_project(path, max_files))
                seen.add(resolved)
            dirs[:] = []
    if not projects:
        projects.append(inspect_project(root, max_files))
    return projects


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("roots", nargs="+", type=Path)
    parser.add_argument("--max-depth", type=int, default=3)
    parser.add_argument("--max-files", type=int, default=10000)
    args = parser.parse_args()
    if args.max_depth < 0 or args.max_files < 1:
        parser.error("max-depth must be >= 0 and max-files must be >= 1")
    projects = []
    for root in args.roots:
        projects.extend(discover(root, args.max_depth, args.max_files))
    unique = {project["path"]: project for project in projects}
    print(json.dumps({"projects": list(unique.values()), "count": len(unique)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
