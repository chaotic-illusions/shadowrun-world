#!/usr/bin/env python3
"""Fail on mojibake, UTF-8 BOM, invalid UTF-8, or any non-ASCII source text."""

from __future__ import annotations

import argparse
import codecs
import subprocess
import sys
from pathlib import Path

TEXT_EXTENSIONS = {
    ".py",
    ".md",
    ".html",
    ".js",
    ".css",
    ".json",
    ".yml",
    ".yaml",
    ".ini",
    ".txt",
    ".bat",
    ".sh",
    ".mako",
    ".ps1",
    ".toml",
}

EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "node_modules",
    "chat-session-resources",
    "workspaceStorage",
    "__pycache__",
}

MOJIBAKE_MARKERS = ("\u00e2", "\u00c3", "\u00c2", "\ufffd")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check source text files for encoding hygiene issues."
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root (default: current directory).",
    )
    parser.add_argument(
        "--staged",
        action="store_true",
        help="Only check staged files (for pre-commit).",
    )
    return parser.parse_args()


def _rel(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def get_staged_files(root: Path) -> list[Path]:
    proc = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        return []

    files: list[Path] = []
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        p = root / line
        if p.is_file() and p.suffix.lower() in TEXT_EXTENSIONS:
            files.append(p)
    return files


def iter_repo_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue

        rel_parts = set(p.relative_to(root).parts)
        if rel_parts.intersection(EXCLUDED_DIRS):
            continue

        if p.suffix.lower() in TEXT_EXTENSIONS:
            files.append(p)

    return files


def check_file(path: Path) -> list[str]:
    issues: list[str] = []
    data = path.read_bytes()

    if data.startswith(codecs.BOM_UTF8):
        issues.append("UTF-8 BOM detected")

    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        issues.append(
            f"invalid UTF-8 at byte {exc.start}: expected UTF-8 without legacy encoding"
        )
        return issues

    for marker in MOJIBAKE_MARKERS:
        if marker in text:
            issues.append(f"mojibake marker found: {marker}")

    non_ascii = sorted({ch for ch in text if ord(ch) > 127})
    if non_ascii:
        sample = ", ".join(f"U+{ord(ch):04X}" for ch in non_ascii[:8])
        if len(non_ascii) > 8:
            sample += ", ..."
        issues.append(f"non-ASCII characters present: {sample}")

    return issues


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()

    files = get_staged_files(root) if args.staged else iter_repo_files(root)
    if args.staged and not files:
        print("Text hygiene check: no staged text files.")
        return 0

    failures: list[tuple[Path, list[str]]] = []
    for path in files:
        issues = check_file(path)
        if issues:
            failures.append((path, issues))

    if not failures:
        print(f"Text hygiene check passed ({len(files)} files scanned).")
        return 0

    print(f"Text hygiene check failed in {len(failures)} file(s):")
    for path, issues in failures:
        rel = _rel(path, root)
        print(f"- {rel}")
        for issue in issues:
            print(f"  - {issue}")

    print("Fix encoding/content issues before committing.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
