"""
Parses a GM's free-form run summary using Claude.
Returns structured run data and proposed world-state changes for the GM to review.

The instructions live in docs/ai_parser_reference.md. Claude answers in a fixed JSON schema
(structured outputs), and check_result() then drops anything that names an ID outside the
world context or a character who was not on the run, and marks evidence quotes it cannot find
in the summary.
"""
import json
import os
import pathlib
import re

import anthropic

from app.data.consequence_tags import SINGLE_TAG_RULES
from app.services.secrets import get_api_key

_REF_PATH = pathlib.Path(__file__).parent.parent.parent / "docs" / "ai_parser_reference.md"
try:
    _REFERENCE = _REF_PATH.read_text(encoding="utf-8")
except FileNotFoundError:
    _REFERENCE = ""

_SYSTEM = (
    "You record Shadowrun runs for a GM's campaign tracker. The user message holds the world "
    "context (JSON) and the GM's run summary. Follow the reference below exactly and answer "
    "with the JSON record only.\n\n---\n\n" + _REFERENCE
)

DEFAULT_MODEL = "claude-opus-5"
OUTCOMES = ["success", "partial_success", "failure", "critical_failure", "abandoned"]
CHANGE_TYPES = ["street_cred", "notoriety", "public_awareness", "org_standing", "heat"]
EXPOSURE_TAGS = [
    "witnesses", "collateral_damage", "public_scene", "media_attention", "casualties", "wetwork",
    "assassination", "magic_use", "vehicle_chase", "data_theft", "extraction", "bribery",
    "false_flag", "stealth",
]
CONSEQUENCE_TAGS = sorted(SINGLE_TAG_RULES)

_ID_LIST = {"type": "array", "items": {"type": "integer"}}
RECORD_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "objective": {"type": "string"},
        "result": {"type": "string"},
        "outcome": {"type": "string", "enum": OUTCOMES},
        "employer": {"type": "string"},
        "outcome_tags": {"type": "array", "items": {"type": "string", "enum": EXPOSURE_TAGS}},
        "consequence_tags": {"type": "array", "items": {"type": "string", "enum": CONSEQUENCE_TAGS}},
        "location_ids": _ID_LIST,
        "org_ids": _ID_LIST,
        "proposed_changes": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {"type": "string", "enum": CHANGE_TYPES},
                    "character_id": {"type": "integer"},
                    "delta": {"type": "integer"},
                    "org_id": {"anyOf": [{"type": "integer"}, {"type": "null"}]},
                    "reason": {"type": "string"},
                    "evidence": {"type": "string"},
                },
                "required": ["type", "character_id", "delta", "org_id", "reason", "evidence"],
                "additionalProperties": False,
            },
        },
        "questions": {"type": "array", "items": {"type": "string"}},
    },
    "required": [
        "title", "objective", "result", "outcome", "employer", "outcome_tags", "consequence_tags",
        "location_ids", "org_ids", "proposed_changes", "questions",
    ],
    "additionalProperties": False,
}


def _squash(text: str) -> str:
    """Lower-case and collapse whitespace and quote styles so quotes compare loosely."""
    text = text.lower().replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", text).strip()


def check_result(result: dict, world_context: dict, narrative: str) -> dict:
    """Keep only what the world context supports; fill names from the context, not the model.

    Adds ``dropped`` (why each rejected change was removed) and, on each kept change,
    ``evidence_found`` (whether its quote appears in the summary).
    """
    participants = {p["id"]: p["name"] for p in world_context.get("participants", [])}
    orgs = {o["id"]: o["name"] for o in world_context.get("organizations", [])}
    locations = {loc["id"] for loc in world_context.get("locations", [])}
    summary = _squash(narrative)

    kept, dropped = [], []
    for change in result.get("proposed_changes") or []:
        who = change.get("character_id")
        label = f"{change.get('type')} {change.get('delta')} for character {who}"
        if change.get("type") not in CHANGE_TYPES:
            dropped.append(f"{label}: unknown change type")
            continue
        if who not in participants:
            dropped.append(f"{label}: not a runner on this run")
            continue
        if not change.get("delta"):
            dropped.append(f"{label}: no change")
            continue
        if change["type"] == "org_standing":
            if change.get("org_id") not in orgs:
                dropped.append(f"{label}: organization {change.get('org_id')} is not in the world context")
                continue
            change["org_name"] = orgs[change["org_id"]]
        else:
            change["org_id"] = None
            change.pop("org_name", None)
        change["character_name"] = participants[who]
        evidence = _squash(change.get("evidence") or "")
        change["evidence_found"] = bool(evidence) and evidence in summary
        kept.append(change)

    result["proposed_changes"] = kept
    result["dropped"] = dropped
    result["location_ids"] = [i for i in result.get("location_ids") or [] if i in locations]
    result["org_ids"] = [i for i in result.get("org_ids") or [] if i in orgs]
    # One stored tag list: exposure tags drive heat, consequence tags drive the consequence engine.
    exposure = [t for t in result.get("outcome_tags") or [] if t in EXPOSURE_TAGS]
    consequence = [t for t in result.pop("consequence_tags", None) or [] if t in SINGLE_TAG_RULES]
    result["outcome_tags"] = list(dict.fromkeys(exposure + consequence))
    result["questions"] = [q for q in result.get("questions") or [] if q.strip()]
    return result


async def parse_narrative(narrative: str, world_context: dict) -> dict:
    """Ask Claude for a run record, then check it against the world context."""
    api_key = get_api_key()
    if not api_key:
        raise RuntimeError("Anthropic API key is not configured")

    client = anthropic.AsyncAnthropic(api_key=api_key)
    model = os.getenv("CLAUDE_MODEL", DEFAULT_MODEL)
    request = dict(
        model=model,
        max_tokens=16000,
        # The reference is identical on every call, so cache it.
        system=[{"type": "text", "text": _SYSTEM, "cache_control": {"type": "ephemeral"}}],
        messages=[{
            "role": "user",
            "content": (
                "WORLD CONTEXT:\n" + json.dumps(world_context, indent=2, sort_keys=True)
                + "\n\nGM RUN SUMMARY:\n" + narrative.strip()
            ),
        }],
        thinking={"type": "adaptive"},
        output_config={"effort": "high", "format": {"type": "json_schema", "schema": RECORD_SCHEMA}},
    )
    # Run summaries describe violent crime; on a safety decline, let the API retry on its
    # fallback model instead of failing the parse.
    if model.startswith(("claude-opus-5", "claude-fable-5")):
        message = await client.beta.messages.create(
            **request, betas=["server-side-fallback-2026-07-01"], fallbacks="default",
        )
    else:
        message = await client.messages.create(**request)

    if message.stop_reason == "refusal":
        raise RuntimeError("Claude declined to parse this summary; log the run manually")
    if message.stop_reason == "max_tokens":
        raise RuntimeError("The parse ran out of room; shorten the summary and try again")
    text = next((block.text for block in message.content if block.type == "text"), "")
    try:
        result = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Claude returned malformed JSON: {text[:300]}") from exc
    return check_result(result, world_context, narrative)
