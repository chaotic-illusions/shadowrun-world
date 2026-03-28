"""
Parses a GM's free-form run narrative using Claude.
Returns structured run data and proposed world-state changes.
"""
import os
import json
import anthropic

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
  "payout": "Payment e.g. \\u00a510,000 per runner, or null",
  "outcome_tags": ["list", "of", "consequence", "tags"],
  "proposed_changes": [
    {
      "type": "nuyen | street_cred | notoriety | public_awareness | org_standing",
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
- nuyen: total per-character payment (positive) or expense (negative). Use the payout figure if stated.
- street_cred: +1 to +3 for a clean success; less for partial; 0 or negative for failure.
- notoriety: +1 to +3 when runners were witnessed, caught on camera, left collateral damage, or acted outside shadowrunner norms.
- public_awareness: +1 only if the event made news or caused a public scene.
- org_standing: -5 to +5 based on how the run affected that org's interests (positive = helped them, negative = harmed them).
- Only include changes clearly supported by the narrative.
- Match character_name and org_name exactly to the world context.
- If a character is not named in the narrative, do not include changes for them unless they obviously participated (e.g. "the team").
- Clamp nuyen changes to reasonable SR2 values (street runs: \\u00a55k-\\u00a550k per runner).
- Do not invent organizations or characters not present in the world context.
"""


def parse_narrative(narrative: str, world_context: dict) -> dict:
    """
    Call Claude to parse a GM narrative into structured run data + proposed changes.

    world_context keys:
      characters  – list of {id, name, is_pc, nuyen}
      organizations – list of {id, name, org_type}
      reputation  – list of {character_id, street_cred, notoriety, public_awareness}
      standings   – list of {character_id, org_id, standing}
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY is not configured")

    client = anthropic.Anthropic(api_key=api_key)

    user_msg = (
        "WORLD CONTEXT:\n"
        + json.dumps(world_context, indent=2)
        + "\n\nGM NARRATIVE:\n"
        + narrative.strip()
    )

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=_SYSTEM,
        messages=[{"role": "user", "content": user_msg}],
    )

    raw = message.content[0].text.strip()
    # Strip markdown code fences if the model wrapped the JSON
    if raw.startswith("```"):
        raw = raw.split("\n", 1)[1]
    if raw.endswith("```"):
        raw = raw.rsplit("```", 1)[0].strip()

    return json.loads(raw)
