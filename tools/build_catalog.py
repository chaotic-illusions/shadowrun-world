"""Convert the shadowrun2e.com reference JS data + the Rigger 2 vehicle table
into clean JSON catalogs under ``app/data/catalog/``.

The source files under ``docs/reference-data/`` are JS (``window.NAME = <value>;``)
using JS object-literal syntax (unquoted keys, ``//`` and ``/* */`` comments,
trailing commas). This is a *build-time* tool: it depends on ``json5`` (a dev
helper, not a runtime dependency) to tolerate that syntax, and emits stdlib-JSON
that the app loads with plain ``json`` at runtime.

Run from the repo root:

    python tools/build_catalog.py

The generated JSON is committed; re-run only when the reference data changes.
"""
from __future__ import annotations

import json
from pathlib import Path

import json5

ROOT = Path(__file__).resolve().parent.parent
REF_DIR = ROOT / "docs" / "reference-data"
SRC_DIR = REF_DIR / "shadowrun2e-com"
OUT_DIR = ROOT / "app" / "data" / "catalog"

# Single-array reference files: source file -> (window global, output catalog).
ITEM_FILES = {
    "weapons-data.js": ("WEAPONS", "weapons"),
    "armor-data.js": ("ARMOR", "armor"),
    "cyberware-data.js": ("CYBERWARE", "cyberware"),
    "gear-data.js": ("GEAR", "gear"),
    "spells-data.js": ("SR2_SPELLS", "spells"),
    "adept-powers-data.js": ("ADEPT_POWERS", "adept_powers"),
}

# window.SR2_<NAME> assignments in builder-data.js -> output key.
BUILDER_FILE = "builder-data.js"


def _extract_balanced(text: str, start: int) -> tuple[int, int]:
    """Return (start, end) of the balanced ``{...}`` / ``[...]`` beginning at
    ``start``, respecting string literals and JS comments so braces inside them
    are not counted."""
    open_ch = text[start]
    close_ch = {"{": "}", "[": "]"}[open_ch]
    depth = 0
    i = start
    n = len(text)
    in_str: str | None = None
    while i < n:
        c = text[i]
        if in_str is not None:
            if c == "\\":
                i += 2
                continue
            if c == in_str:
                in_str = None
            i += 1
            continue
        if c in "\"'":
            in_str = c
            i += 1
            continue
        pair = text[i : i + 2]
        if pair == "//":
            nl = text.find("\n", i)
            i = n if nl == -1 else nl
            continue
        if pair == "/*":
            end = text.find("*/", i)
            i = n if end == -1 else end + 2
            continue
        if c == open_ch:
            depth += 1
        elif c == close_ch:
            depth -= 1
            if depth == 0:
                return start, i + 1
        i += 1
    raise ValueError(f"unbalanced {open_ch!r} starting at offset {start}")


def _value_after(text: str, marker: str):
    """Parse the JS value assigned right after ``marker`` (e.g. ``window.X =``)."""
    idx = text.index("=", text.index(marker) + len(marker)) + 1
    while text[idx] in " \t\r\n":
        idx += 1
    start, end = _extract_balanced(text, idx)
    return json5.loads(text[start:end])


def _parse_item_file(path: Path, global_name: str) -> list:
    text = path.read_text(encoding="utf-8")
    data = _value_after(text, f"window.{global_name}")
    if not isinstance(data, list):
        raise TypeError(f"{path.name}: expected a list for {global_name}")
    return data


def _parse_builder(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    # SR2_PDFMAP is the reference site's own PDF-export field map: it lives in an
    # IIFE and references JS variables (not a static literal), and our app does
    # not use that PDF, so it is skipped.
    skip = {"pdfmap"}
    out: dict = {}
    search = 0
    needle = "window.SR2_"
    while True:
        pos = text.find(needle, search)
        if pos == -1:
            break
        eq = text.index("=", pos)
        name = text[pos + len("window.") : eq].strip()  # e.g. SR2_PRIORITY
        key = name[len("SR2_") :].lower()  # priority
        start = eq + 1
        while text[start] in " \t\r\n":
            start += 1
        if text[start] in "{[":
            vstart, vend = _extract_balanced(text, start)
            search = vend
            if key not in skip:
                out[key] = json5.loads(text[vstart:vend])
        else:  # scalar/string assignment (none expected, but handle defensively)
            semi = text.index(";", start)
            search = semi + 1
            if key not in skip:
                out[key] = json5.loads(text[start:semi])
    return out


def _dump_array(path: Path, items: list) -> None:
    lines = ["["]
    for i, item in enumerate(items):
        suffix = "," if i < len(items) - 1 else ""
        lines.append(json.dumps(item, ensure_ascii=False) + suffix)
    lines.append("]")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    summary = []

    for filename, (global_name, out_name) in ITEM_FILES.items():
        items = _parse_item_file(SRC_DIR / filename, global_name)
        if out_name == "cyberware":
            # Bioware costs Body Index, not Essence (bio == true), so it becomes its
            # own catalog while the essence-costed cyberware keeps this file.
            bioware = [it for it in items if it.get("bio")]
            cyberware = [it for it in items if not it.get("bio")]
            _dump_array(OUT_DIR / "cyberware.json", cyberware)
            _dump_array(OUT_DIR / "bioware.json", bioware)
            summary.append(("cyberware", len(cyberware)))
            summary.append(("bioware", len(bioware)))
            continue
        _dump_array(OUT_DIR / f"{out_name}.json", items)
        summary.append((out_name, len(items)))

    # Vehicles already ship as clean JSON transcribed from the Rigger 2 book.
    vehicles = json.loads((REF_DIR / "rigger2-vehicles.json").read_text(encoding="utf-8"))
    _dump_array(OUT_DIR / "vehicles.json", vehicles)
    summary.append(("vehicles", len(vehicles)))

    builder = _parse_builder(SRC_DIR / BUILDER_FILE)
    (OUT_DIR / "builder.json").write_text(
        json.dumps(builder, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    summary.append(("builder(rules)", len(builder)))

    width = max(len(name) for name, _ in summary)
    for name, count in summary:
        print(f"  {name.ljust(width)}  {count}")
    print(f"Wrote {len(summary)} catalog file(s) to {OUT_DIR.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
