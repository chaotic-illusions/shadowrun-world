"""refund_removed_cyberware

Chipjack and Display Link were dropped from the cyberware catalog (a Smartlink needs no Display
Link; the Softlink replaced the Chipjack). A character who already bought one still paid Essence
and nuyen for it, so take the item off every sheet and give both back:

- Essence and nuyen are refunded at the grade the item was bought at, the same way the app charges
  them (Essence x grade multiplier, rounded up to 0.01, minimum 0.05; nuyen x grade multiplier).
- The saved chargen wizard state loses the items too. An unfinished draft gets no refund on its
  columns: the builder recomputes Essence and nuyen from the gear list when it is resumed.
- Magic Rating is left alone; a GM adjusts it by hand if an awakened character regains Essence.

Revision ID: c5f8b2d04e37
Revises: b4e7a1c93d26
Create Date: 2026-10-02 00:00:00.000000
"""
import json
import math
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "c5f8b2d04e37"
down_revision: Union[str, None] = "b4e7a1c93d26"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# name -> (Essence, nuyen) as the catalog listed them, for a line that doesn't carry its own.
REMOVED = {"Chipjack": (0.2, 1000), "Display Link": (0.1, 1000)}
# grade -> (Essence multiplier, nuyen multiplier); play-sheet.html ESS_GRADE_MULT.
GRADES = {"Standard": (1.0, 1), "Alpha": (0.8, 3), "Beta": (0.6, 7), "Delta": (0.5, 10)}
STARTING_ESSENCE = 6.0


def _strip(gear) -> tuple[float, int]:
    """Remove the dropped items from ``gear["cyber"]`` in place; return (Essence, nuyen) to refund."""
    cyber = gear.get("cyber") if isinstance(gear, dict) else None
    if not isinstance(cyber, list):
        return 0.0, 0
    essence, nuyen, kept = 0.0, 0, []
    for line in cyber:
        if not isinstance(line, dict) or line.get("n") not in REMOVED:
            kept.append(line)
            continue
        base_ess, base_cost = REMOVED[line["n"]]
        ess_mult, cost_mult = GRADES.get(line.get("grade") or "Standard", GRADES["Standard"])
        base_ess = float(line.get("baseEss") or base_ess)
        essence += max(0.05, math.ceil(base_ess * ess_mult * 100 - 1e-9) / 100)
        nuyen += int(round(float(line.get("baseCost") or base_cost) * cost_mult))
    gear["cyber"] = kept
    return essence, nuyen


def upgrade() -> None:
    bind = op.get_bind()
    rows = bind.execute(sa.text(
        "SELECT id, gear, chargen_state, essence, nuyen, is_draft FROM characters"
    )).fetchall()
    for char_id, gear_raw, state_raw, essence, nuyen, is_draft in rows:
        try:
            gear = json.loads(gear_raw) if isinstance(gear_raw, str) else gear_raw
            state = json.loads(state_raw) if isinstance(state_raw, str) else state_raw
        except ValueError:
            continue
        ess_back, nuyen_back = _strip(gear)
        if ess_back:
            values = {"gear": json.dumps(gear), "id": char_id}
            sql = "UPDATE characters SET gear = :gear"
            if not is_draft:
                values["essence"] = min(STARTING_ESSENCE, round((essence or 0) + ess_back, 2))
                values["nuyen"] = (nuyen or 0) + nuyen_back
                sql += ", essence = :essence, nuyen = :nuyen"
            bind.execute(sa.text(sql + " WHERE id = :id"), values)
        if isinstance(state, dict) and _strip(state.get("gear"))[0]:
            bind.execute(sa.text("UPDATE characters SET chargen_state = :v WHERE id = :id"),
                         {"v": json.dumps(state), "id": char_id})


def downgrade() -> None:
    # Which characters owned the items isn't recorded, and the catalog no longer sells them.
    pass
