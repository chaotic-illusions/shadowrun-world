"""skill_concentration_lists

After chargen a skill can carry any number of Concentrations and Specializations, each bought
with Good Karma (SR2 p.190), so a stored skill's single ``conc``/``spec`` pair becomes two lists:

    {"name", "rating", "concs": [{"name", "rating"}], "specs": [{"name", "rating", "conc"}]}

``rating`` is the general skill after the chargen split, and a Specialization's ``conc`` names
the Concentration it falls under ("" when it was bought straight off the general skill).

Chargen used to store the unsplit Skill Points with no ``concRating``; the play sheet split them
on first load. A skill still in that state is split here the same way (SR2 p.70: general -1 and
Concentration +1, or general -2, Concentration at the original rating and Specialization +2).
The saved chargen wizard state keeps its own single conc/spec shape and is left alone.

Revision ID: d8a3f0b6c215
Revises: c5f8b2d04e37
Create Date: 2026-10-04 00:00:00.000000
"""
import json
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "d8a3f0b6c215"
down_revision: Union[str, None] = "c5f8b2d04e37"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

_LEGACY_KEYS = ("conc", "concRating", "spec", "specRating")


def _to_lists(skill: dict) -> dict:
    conc = (skill.pop("conc", "") or "").strip()
    spec = (skill.pop("spec", "") or "").strip()
    conc_rating = skill.pop("concRating", None)
    spec_rating = skill.pop("specRating", None)
    rating = int(skill.get("rating") or 0)
    if conc and conc_rating is None:
        conc_rating, rating = rating + 1, rating - 1
    if spec and spec_rating is None:
        points = rating + 1
        rating, conc_rating, spec_rating = points - 2, points, points + 2
    skill["rating"] = rating
    skill["concs"] = [{"name": conc, "rating": int(conc_rating)}] if conc else []
    skill["specs"] = [{"name": spec, "rating": int(spec_rating), "conc": conc}] if spec else []
    return skill


def _to_legacy(skill: dict) -> dict:
    concs = skill.pop("concs", None) or []
    specs = skill.pop("specs", None) or []
    conc, spec = (concs[0] if concs else {}), (specs[0] if specs else {})
    skill["conc"] = conc.get("name", "")
    skill["spec"] = spec.get("name", "")
    if conc:
        skill["concRating"] = conc.get("rating")
    if spec:
        skill["specRating"] = spec.get("rating")
    return skill


def _rewrite(convert, applies) -> None:
    bind = op.get_bind()
    for char_id, raw in bind.execute(sa.text("SELECT id, skills FROM characters")).fetchall():
        try:
            skills = json.loads(raw) if isinstance(raw, str) else raw
        except ValueError:
            continue
        if not isinstance(skills, list):
            continue
        hits = [s for s in skills if isinstance(s, dict) and applies(s)]
        if not hits:
            continue
        for s in hits:
            convert(s)
        bind.execute(sa.text("UPDATE characters SET skills = :v WHERE id = :id"),
                     {"v": json.dumps(skills), "id": char_id})


def upgrade() -> None:
    _rewrite(_to_lists, lambda s: "concs" not in s or any(k in s for k in _LEGACY_KEYS))


def downgrade() -> None:
    # Only the first Concentration and Specialization fit the old shape; any others are dropped.
    _rewrite(_to_legacy, lambda s: "concs" in s or "specs" in s)
