"""
Consequence engine: given a set of outcome tags from an adventure log,
returns narrative consequence suggestions ordered by severity.

Matching rules:
- Single-tag rules fire when the tag is present in the active set.
- Compound rules fire when ALL tags in the rule's key set are a subset of the active set.
- Compound rules appear before single-tag rules in output (more specific = higher priority).
- Duplicate suggestion text is suppressed.
"""
from typing import Any
from app.data.consequence_tags import SINGLE_TAG_RULES, COMPOUND_TAG_RULES

SEVERITY_ORDER = {
    "severe": 0,
    "significant": 1,
    "moderate": 2,
    "variable": 3,
    "low": 4,
    "positive": 5,
}


def suggest(tags: list[str]) -> list[dict[str, Any]]:
    """
    Return a list of consequence suggestion dicts for the given tags.
    Each dict: {source_tags, severity, suggestion}
    """
    if not tags:
        return []

    active = set(tags)
    results: list[dict[str, Any]] = []
    seen_text: set[str] = set()

    # Compound rules first (most specific)
    matched_compounds = [
        (key, rule)
        for key, rule in COMPOUND_TAG_RULES.items()
        if key.issubset(active)
    ]
    # Sort compound rules by size descending (most specific first)
    matched_compounds.sort(key=lambda x: -len(x[0]))

    for key, rule in matched_compounds:
        for suggestion in rule["suggestions"]:
            if suggestion not in seen_text:
                seen_text.add(suggestion)
                results.append({
                    "source_tags": sorted(key),
                    "severity": rule["severity"],
                    "suggestion": suggestion,
                })

    # Single-tag rules
    for tag in tags:
        rule = SINGLE_TAG_RULES.get(tag)
        if not rule:
            continue
        for suggestion in rule["suggestions"]:
            if suggestion not in seen_text:
                seen_text.add(suggestion)
                results.append({
                    "source_tags": [tag],
                    "severity": rule["severity"],
                    "suggestion": suggestion,
                })

    results.sort(key=lambda x: SEVERITY_ORDER.get(x["severity"], 3))
    return results
