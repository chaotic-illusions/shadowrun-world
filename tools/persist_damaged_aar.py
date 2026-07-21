"""One-off: persist a damaged-exit AAR example so the GM review page shows injury rendering.

Clones run #4's state as a realistic base, injects a rough exit (MPCP damage, permanent persona-
chip burn, heavy biofeedback, a lingering MPCP worm, physical trace located, black-IC flatline),
prints the _build_run_aar payload, and saves it to the DB. Run: python tools/persist_damaged_aar.py
"""
from __future__ import annotations

import asyncio
import datetime
import json
import os
import sqlite3
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.session import async_session
from app.models.matrix_run import MatrixRun
from app.auth.core import hash_token
from app.routers import matrix_runs as mr


def main() -> None:
    c = sqlite3.connect("data/shadowrun.db")
    row = list(c.execute("select decker_json, state_json from matrix_runs where id=4"))[0]
    c.close()
    decker = json.loads(row[0])
    state = json.loads(row[1])

    cm = state["condition_monitor"]
    cm["mpcp_damage"] = 2
    cm["persona_damage"] = {"bod": 0, "evasion": 3, "masking": 0, "sensor": 1}
    cm["persona_chip_damage"] = {"bod": 0, "evasion": 2, "masking": 0, "sensor": 1}
    cm["stun_boxes"] = 6
    cm["physical_boxes"] = 4
    state["mpcp_infections"] = [{"variant": "worm", "rating": 6, "ic_id": "worm_a1"}]
    state["alert_status"] = "active"
    state["security_tally"] = 71
    state["physical_trace_immune"] = False
    state["traces_completed"] = 1
    state["end_reason"] = "black_ic_lethal"

    class _R:
        pass

    r = _R()
    r.id = None
    r.host_id = 3
    r.status = "killed"
    r.decker_json = decker
    r.state_json = state
    r.aar_acknowledged = False
    r.created_at = datetime.datetime.now(datetime.timezone.utc)
    r.updated_at = r.created_at
    print(json.dumps(mr._build_run_aar(r), indent=2, default=str))

    async def go() -> int:
        async with async_session() as db:
            m = MatrixRun(
                host_id=3, decker_json=decker, state_json=state, status="killed",
                owner_token_hash=hash_token("static"), aar_acknowledged=False,
            )
            db.add(m)
            await db.commit()
            await db.refresh(m)
            return m.id

    nid = asyncio.new_event_loop().run_until_complete(go())
    print(f"\n[persist] saved damaged run #{nid}")


if __name__ == "__main__":
    main()
