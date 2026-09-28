"""Audit copyable world prose for ingest notes, raw mechanics, and broken text."""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
from collections.abc import Iterator
from dataclasses import asdict, dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DB = ROOT / "data" / "prod-snapshot" / "2026-09-15" / "shadowrun_prod.db"

_FALSE_POSITIVE_RE = re.compile(
    r"(?i)(?:torture-resistance test|Resistance testimony|Honda-GM)"
)
_PATTERNS = {
    "ingest_metadata": re.compile(
        r"(?im)(?:^\s*--.+--|\b(?:Adventure scope removed|ally_ids|enemy_ids|"
        r"stored flat|production row|database row|ingest|loader|schema|"
        r"documentation-only|documentary only|GM-only|player-safe|needs human touch|"
        r"TODO|future context|dated context|bounded source context|source-current|"
        r"are omitted|is omitted)\b|\b(?:the|this|earlier|later|original|published|"
        r"20\d{2}|NAN2|Denver|Aztlan) source(?:book)?\b|\bsource (?:frame|period|"
        r"profile|records?|reports?|text|material|alias|variant|category|shorthand|"
        r"commentary|forms?|options?)\b)"
    ),
    "raw_mechanics": re.compile(
        r"(?i)(?:\bStats?\s*:|\bstat blocks?\b|\bB\d+\s+Q\d+\s+S\d+|"
        r"\b(?:Body|Quickness|Strength|Charisma|Intelligence|Willpower|Essence|"
        r"Reaction|Initiative)\s*[:=]?\s*\d+(?:\(\d+\))?|\bCombat Pool\b|"
        r"\bKarma Pool\b|\bProfessional Rating\b|\bThreat\s*[/ :]\s*\d|"
        r"\b(?:TN\s*\d+|target number\s*\d+|\d+D6|\d+ dice|success test|"
        r"opposed test|resistance test)\b|\b(?:Body|Quickness|Strength|Charisma|"
        r"Intelligence|Willpower|Computer|Etiquette|Perception|Negotiation|Stealth|"
        r"Athletics|Sorcery|Conjuring|Firearms|Biotech|Electronics|Demolitions|"
        r"Gunnery|Unarmed Combat|Armed Combat|Police Procedures|Rifles)\s*"
        r"(?:\(\d+\)|[:=]?\s+\d+)\b|\b(?:Rating|Barrier|MPCP|Attack|Sleaze|"
        r"Masking|Sensor|Armor)\s*[:=]?\s*\d+\b|\b(?:Cyberware|Gear|Spells?|"
        r"Powers?|Weapons?|Armor)\s*:\s*|\b\d+(?:[SLMDF])\d*\s+"
        r"(?:Stun|Physical|damage|per turn))"
    ),
    "page_citation": re.compile(r"(?i)\b(?:p{1,2}\.\s*\d+(?:-\d+)?|page\s+\d+)\b"),
    "editorial_instruction": re.compile(
        r"(?i)\b(?:the|this) book(?! of\b)|\b(?:later|earlier) books?\b|"
        r"\b(?:the|this) module (?:says?|tells?|calls?|flags?|gives?|lists?|"
        r"suggests?|offers?|expects?|allows?|frames?|introduces?|names?|places?|"
        r"provides?|uses?|assumes?|warns?)\b|\bmodule(?:'s)? (?:fiction|text|"
        r"write-up|affair)\b|\b(?:the|this|an) adventure\b|\badventure (?:role|"
        r"scope|ends?|text|assumes?|uses?|calls?|names?|says?)\b|(?<!Honda-)"
        r"\b(?:the )?GM\b|\bgamemaster\b|\bplayer handouts?\b|\bprep doc\b|"
        r"\bPLAY_NOTES\b|\bMATRIX_HOSTS\b|\bsee Matrix systems\b|"
        r"\bsource(?:/OCR)? (?:forms?|aliases?|options?|context|profile|framed|"
        r"dated|material|variant|shorthand)\b|\blegwork\b|\b(?:as printed|"
        r"published stats?|printed stats?|no published stats?|source-attributed|"
        r"in the source|published account)\b"
    ),
    "source_heading": re.compile(
        r"(?i)^(?:Elven Fire|Eye of the Eagle|Wake of the Comet|Peacekeeper news|"
        r"Bottled Demon news|June 8, 2051 news|Corporate profile as published|"
        r"Dunkelzahn campaign background|Renraku Arcology: Shutdown|By 2054, Target|"
        r"Printed local (?:RTG documentation|LTG result)|Availability|"
        r"Brainscan Pushing the Envelope)\b"
    ),
    "malformed_prose": re.compile(
        r"(?m)(?:^[a-z,;:.?)]|\bBy 20\d{2},\s*\.|(?<!\.)\.['\"]?\s*\.(?!\.)|"
        r"\brecords records\b|\b(?:published )?records (?:does|documents|supports|"
        r"presents|spells|identifies|names|places|calls)\b|\.(?:By|In) 20\d{2}|"
        r"\bis a (?:alternate|unusual)\b|\bU\.S\. Of\b|"
        r"^In the 20\d{2} [^\n]* period, The\b|"
        r"\b(?:claims|details|operations|services|ties|facilities|activities|"
        r"relationships|mechanisms|barriers|appointments|restrictions|allegations|"
        r"interests|links|reports|facts|warnings|theories|arrangements) is\b)"
    ),
}


@dataclass(frozen=True)
class Finding:
    kind: str
    row_id: int
    name: str
    path: str
    patterns: tuple[str, ...]
    text: str


def _scan_text(
    kind: str,
    row_id: int,
    name: str,
    path: str,
    text: str | None,
) -> Iterator[Finding]:
    if not text:
        return
    for paragraph in re.split(r"\n\s*\n", text):
        masked = _FALSE_POSITIVE_RE.sub("", paragraph)
        matches = tuple(key for key, pattern in _PATTERNS.items() if pattern.search(masked))
        if matches:
            yield Finding(kind, row_id, name, path, matches, paragraph)


def _scan_nested(
    kind: str,
    row_id: int,
    name: str,
    path: str,
    value: object,
) -> Iterator[Finding]:
    if isinstance(value, dict):
        for key, nested in value.items():
            nested_path = f"{path}.{key}"
            if key in {"description", "notes"} and isinstance(nested, str):
                yield from _scan_text(kind, row_id, name, nested_path, nested)
            elif key in {"leadership", "ltgs"}:
                yield from _scan_nested(kind, row_id, name, nested_path, nested)
    elif isinstance(value, list):
        for index, nested in enumerate(value):
            yield from _scan_nested(kind, row_id, name, f"{path}[{index}]", nested)


def audit_database(database_path: Path) -> list[Finding]:
    findings: list[Finding] = []
    with sqlite3.connect(database_path) as database:
        database.row_factory = sqlite3.Row
        tables = (
            ("organizations", "organization", "name", ("description", "headquarters", "notes"), ""),
            ("locations", "location", "name", ("description", "notes"), ""),
            (
                "characters", "character", "name", ("description", "background", "notes"),
                "WHERE is_pc = 0",
            ),
            ("rtgs", "rtg", "code", ("notes",), ""),
            ("matrix_hosts", "matrix_host", "name", ("notes",), ""),
            (
                "adventure_logs", "adventure_log", "title",
                ("objective", "result", "payout", "casualties", "employer", "gm_notes"),
                "",
            ),
            (
                "contacts", "contact", "name", ("description", "notes"),
                "WHERE owner_id IS NULL OR owner_id NOT IN "
                "(SELECT id FROM characters WHERE is_pc = 1)",
            ),
            (
                "reputations", "reputation", "id", ("notes",),
                "WHERE character_id NOT IN (SELECT id FROM characters WHERE is_pc = 1)",
            ),
            (
                "org_standings", "org_standing", "id", ("notes",),
                "WHERE character_id NOT IN (SELECT id FROM characters WHERE is_pc = 1)",
            ),
        )
        for table, kind, name_column, fields, where_clause in tables:
            for row in database.execute(f'SELECT * FROM "{table}" {where_clause}'):
                name = str(row[name_column])
                for field in fields:
                    findings.extend(_scan_text(kind, row["id"], name, field, row[field]))

        for row in database.execute(
            "SELECT id, name, leadership, divisions, ltgs FROM organizations"
        ):
            for field in ("leadership", "divisions", "ltgs"):
                value = json.loads(row[field] or "[]")
                findings.extend(
                    _scan_nested("organization", row["id"], row["name"], field, value)
                )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    findings = audit_database(args.db)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(
            json.dumps([asdict(finding) for finding in findings], indent=2, ensure_ascii=True)
            + "\n",
            encoding="utf-8",
            newline="\n",
        )
    print(f"Copyable-text findings: {len(findings)}")
    for finding in findings:
        print(
            f"{finding.kind} {finding.row_id} {finding.name} {finding.path} "
            f"[{', '.join(finding.patterns)}]"
        )
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())