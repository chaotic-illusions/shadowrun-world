"""
Parses a GM's free-form run narrative using Claude.
Returns structured run data and proposed world-state changes.
"""
import json
import pathlib
import re

import anthropic

from app.services.secrets import get_api_key

# Load the AI parser reference doc at import time so edits to the file
# take effect without restarting the server (the module reloads on change).
_REF_PATH = pathlib.Path(__file__).parent.parent.parent / "docs" / "ai_parser_reference.md"
try:
    _REFERENCE = _REF_PATH.read_text(encoding="utf-8")
except FileNotFoundError:
    _REFERENCE = ""

_SYSTEM = """You are a Shadowrun 2nd Edition GM assistant.
Given a free-form narrative about a shadowrun, extract structured information
and propose specific world-state changes. The world context lists all active
characters (with IDs), organizations (with IDs), current reputation values,
and current org standings.

Respond ONLY with a single valid JSON object matching this schema exactly:

{
  "title": "Short descriptive run title (max 60 chars)",
  "objective": "What the team was hired to do",
  "result": "What actually happened",
  "outcome": "success | partial_success | failure | critical_failure | abandoned",
  "employer": "Name of hiring party or org (as described in narrative)",
  "outcome_tags": ["list", "of", "consequence", "tags"],
  "proposed_changes": [
    {
      "type": "street_cred | notoriety | public_awareness | org_standing | heat",
      "character_name": "Exact name from world context",
      "character_id": <integer id from world context>,
      "delta": <signed integer>,
      "org_name": "Org name — only for org_standing type, otherwise omit",
      "org_id": <integer id — only for org_standing type, otherwise omit>,
      "reason": "One-sentence explanation"
    }
  ]
}

Rules for proposed_changes:
- street_cred: use this for ALL skill-based reputation changes.
    Success: +1 to +3 depending on difficulty and cleanliness.
    Partial success: +0 to +1.
    Failure: -1 to -2 (the shadows talk; a botched job costs cred).
    Do NOT use notoriety for run failures -- use a negative street_cred delta instead.
- notoriety: ONLY for genuine infamy events distinct from run outcome:
    collateral civilian damage, witnessed atrocities, betrayal of a Johnson or teammate,
    unnecessary violence, breaking shadowrunner codes of conduct.
    A run failing cleanly does NOT generate notoriety.
- public_awareness: +1 only if the event made news or caused a public scene visible to ordinary citizens.
- org_standing: -5 to +5 based on how the run affected that org's interests (positive = helped them, negative = harmed them).
- heat: individual character heat change (0–10 scale). Use +1 to +3 per runner who was personally exposed,
    identified, witnessed, or is now being hunted by law enforcement or a corp. Do NOT apply to runners
    who stayed hidden or were uninvolved in the exposure. A runner wanted by Lone Star is +2 to +4 heat.
    Reduce heat (-1 to -2) if a runner successfully disappeared or covered their tracks after a prior mission.
- Only include changes clearly supported by the narrative.
- Match character_name and org_name exactly to the world context.
- If a character is not named in the narrative, do not include changes for them unless they obviously participated (e.g. "the team").
- Do not invent organizations or characters not present in the world context.
"""

# Append the reference doc (tag and mechanic details) if available
_FULL_SYSTEM = _SYSTEM + ("\n\n---\n\n" + _REFERENCE if _REFERENCE else "")

# Regex to find the first JSON object in a response (handles markdown fences, preamble, etc.)
_JSON_RE = re.compile(r"\{[\s\S]*\}")


def _extract_json(raw: str) -> dict:
    """Extract and parse the first JSON object from Claude's response text."""
    # Strip markdown code fences
    cleaned = raw.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1] if "\n" in cleaned else cleaned[3:]
    if cleaned.endswith("```"):
        cleaned = cleaned.rsplit("```", 1)[0].strip()

    # Try direct parse first (cleanest path)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    # Regex fallback: find the first { ... } block
    match = _JSON_RE.search(raw)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    raise ValueError(f"Could not extract valid JSON from model response:\n{raw[:500]}")


async def parse_narrative(narrative: str, world_context: dict) -> dict:
    """
    Call Claude to parse a GM narrative into structured run data + proposed changes.

    world_context keys:
      characters  – list of {id, name, is_pc}
      organizations – list of {id, name, org_type}
      reputation  – list of {character_id, street_cred, notoriety, public_awareness}
      standings   – list of {character_id, org_id, standing}
    """
    api_key = get_api_key()
    if not api_key:
        raise RuntimeError("Anthropic API key is not configured")

    client = anthropic.AsyncAnthropic(api_key=api_key)

    user_msg = (
        "WORLD CONTEXT:\n"
        + json.dumps(world_context, indent=2)
        + "\n\nGM NARRATIVE:\n"
        + narrative.strip()
    )

    message = await client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=_FULL_SYSTEM,
        messages=[{"role": "user", "content": user_msg}],
    )

    raw = message.content[0].text.strip()
    return _extract_json(raw)
