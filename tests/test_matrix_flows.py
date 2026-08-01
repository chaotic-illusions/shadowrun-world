"""FLOW / CHAIN correctness tests -- "if A then B then C then D".

The fuzz oracle (test_matrix_correctness_fuzz) checks per-action rule arithmetic; this suite checks
the multi-step CHAINS a decker actually experiences: do a command, verify the exact expected
consequence AND what becomes available/unavailable next, then continue the chain. Dice are made
DETERMINISTIC by scripting the engine's test result (``eng.system_test`` / decrypt / defuse), so a
step's outcome (success with N net successes, or a failure) is chosen, not random -- that is what lets
us assert "I got 3 successes, so I can reveal exactly 3 subsystems".

Every step also checks the admin view is a superset of the player view (the admin can do everything
the player can, with more event-log detail). Grounded in vr2_rules.md + the verified rule notes.
"""

from __future__ import annotations

import pytest
from fastapi import HTTPException

from app.routers import matrix_runs as mr
from app.services import matrix_engine as eng
from app.schemas.matrix_run import (
    RunActionInput, RunAreaAttackInput, RunAttackInput, RunDefendInput, RunEnemyAttackInput,
    RunEnemyScanInput, RunLogoffInput, RunRevealHostRatingsInput, RunScrambleAttackInput,
    RunSuppressInput, RunTrapDoorInput,
)
from tests.test_matrix_visibility_fuzz import (
    _HostNS, _StubRun, _FakeDB, _capable_decker, _call, _LOOP,
)

AUTH_ADMIN = {"is_admin": True, "is_user": False, "user_token": None}
AUTH_PLAYER = {"is_admin": False, "is_user": True, "user_token": "flow"}


def _scripted_system_test(decker_succ: int, host_succ: int = 0):
    """A drop-in for ``eng.system_test`` that yields a CHOSEN outcome (decker vs host successes) with
    an honest roll shape, so a flow step's result is deterministic."""
    def fn(*, decker_pool, subsystem_rating, security_value, det_factor, extra_tn_modifier=0):
        dtn = max(2, subsystem_rating + extra_tn_modifier)
        ds = max(0, min(max(1, decker_pool), decker_succ))
        hs = max(0, min(max(1, security_value), host_succ))
        return {
            "success": (ds - hs >= 0) and ds > 0,
            "decker_roll": {"pool": max(1, decker_pool), "tn": dtn,
                            "dice": [max(dtn, 2)] * ds + [1] * (max(1, decker_pool) - ds),
                            "successes": ds, "ones": 0},
            "host_roll": {"pool": max(1, security_value), "tn": max(1, det_factor),
                          "dice": [max(det_factor, 1)] * hs + [1] * (max(1, security_value) - hs),
                          "successes": hs, "ones": 0},
            "decker_net_successes": ds - hs,
            "tally_increase": hs,
        }
    return fn


class Flow:
    """Drives the REAL run endpoints with deterministic test outcomes, and exposes the admin/player
    serializations so a flow can assert the exact state after each step."""

    def __init__(self, monkeypatch, cfg, trap_doors=None, seed=1234):
        eng.random.seed(seed)
        mr.random.seed(seed)
        self.mp = monkeypatch
        self.host = _HostNS(cfg, trap_doors)
        self.decker = _capable_decker()
        self.run = _StubRun(self.decker, mr._initial_state(self.decker, self.host))

        async def _get_run(db, run_id):
            return self.run

        async def _get_host(db, host_id):
            return self.host

        monkeypatch.setattr(mr, "_get_run_or_404", _get_run)
        monkeypatch.setattr(mr, "_get_host_or_404", _get_host)
        monkeypatch.setattr(mr, "_assert_run_access", lambda r, a: None)

    def act(self, action_type, decker_succ=3, host_succ=0, **body_kw):
        """Perform one action with a chosen outcome. Extra kwargs feed RunActionInput."""
        self.mp.setattr(eng, "system_test", _scripted_system_test(decker_succ, host_succ))
        body = RunActionInput(action_type=action_type, utility_rating=6, hacking_pool_dice=0,
                              **body_kw)
        _call(mr.perform_action(run_id=1, body=body, auth=AUTH_ADMIN, db=_FakeDB()))
        return self

    def act_rejected(self, action_type, decker_succ=3, host_succ=0, **body_kw):
        """Perform an action that the rules should REFUSE, asserting a 4xx rejection and returning it.
        The run state is left unchanged (the guard fires before any mutation)."""
        self.mp.setattr(eng, "system_test", _scripted_system_test(decker_succ, host_succ))
        body = RunActionInput(action_type=action_type, utility_rating=6, hacking_pool_dice=0,
                              **body_kw)
        with pytest.raises(HTTPException) as ei:
            _LOOP.run_until_complete(
                mr.perform_action(run_id=1, body=body, auth=AUTH_ADMIN, db=_FakeDB()))
        assert 400 <= ei.value.status_code < 500, f"expected a 4xx rejection, got {ei.value.status_code}"
        return ei.value

    def reveal(self, subsystems):
        _call(mr.reveal_host_ratings(run_id=1, body=RunRevealHostRatingsInput(subsystems=subsystems),
                                     auth=AUTH_ADMIN, db=_FakeDB()))
        return self

    def new_turn(self):
        """End the current pass / turn -- refreshes the action budget + Hacking Pool."""
        _call(mr.new_turn(run_id=1, auth=AUTH_ADMIN, db=_FakeDB()))
        return self

    def force_decrypt(self, decrypted: bool):
        """Script the next Decrypt File outcome (eng.scramble_decrypt_test)."""
        def fn(*, decker_pool, scramble_rating, decrypt_utility=0):
            tn = max(2, scramble_rating - decrypt_utility)
            s = 2 if decrypted else 0
            return {"roll": {"pool": max(1, decker_pool), "tn": tn,
                             "dice": [max(tn, 2)] * s + [1] * (max(1, decker_pool) - s),
                             "successes": s, "ones": 0},
                    "tn": tn, "decrypted": bool(decrypted)}
        self.mp.setattr(eng, "scramble_decrypt_test", fn)
        return self

    def force_scramble_failure(self, *, destroyed: bool, key_lost: bool = False):
        """Script the Poison-Scramble failed-decrypt consequence (eng.scramble_failure_consequence)."""
        def fn(*, variant, is_key, scramble_rating=6, decker_computer_skill=6):
            return {"data_destroyed": bool(destroyed), "key_data_lost": bool(key_lost),
                    "message": ("Poison IC erased the protected data." if destroyed
                                else "Decrypt failed -- the Poison Scramble holds; the data survives."),
                    "poison_roll": {"pool": scramble_rating, "tn": max(2, decker_computer_skill),
                                    "dice": [], "successes": 1 if destroyed else 0, "ones": 0}}
        self.mp.setattr(eng, "scramble_failure_consequence", fn)
        return self

    def force_defuse(self, defused: bool, detonated: bool = False):
        """Script a Defuse Data Bomb outcome. The handler ignores a bare `defused` flag -- it
        recomputes the result from df["roll"]["successes"] vs a LIVE opposed host roll -- so a
        successful defuse needs both a winning decker roll AND a neutralized host roll."""
        succ = 4 if (defused and not detonated) else 0

        def fn(*, decker_pool, subsystem_rating, defuse_utility=0, **_kw):
            tn = max(2, subsystem_rating - defuse_utility)
            return {"roll": {"pool": max(1, decker_pool), "tn": tn,
                             "dice": [max(tn, 2)] * succ + [1] * max(0, max(1, decker_pool) - succ),
                             "successes": succ, "ones": 0},
                    "tn": tn, "defused": bool(defused), "detonated": bool(detonated)}
        self.mp.setattr(eng, "data_bomb_defuse", fn)
        if defused and not detonated:
            self.mp.setattr(eng, "roll_dice",
                            lambda pool, tn: {"pool": pool, "tn": tn, "dice": [],
                                              "successes": 0, "ones": 0})
        return self

    def force_attack(self, boxes: int, atk_succ: int = 4, resist_succ: int = 0):
        """Script the next cybercombat resolution (eng.cybercombat_attack) to land `boxes` on the
        target -- 10+ crashes an IC. Attack/resist success counts feed the rendered event only."""
        def fn(*_a, **_k):
            return {
                "attack_roll": {"pool": 6, "tn": 4, "dice": [], "successes": atk_succ, "ones": 0},
                "resistance": {
                    "resist_roll": {"pool": 6, "tn": 4, "dice": [], "successes": resist_succ,
                                    "ones": 0},
                    "final_damage_level": "M", "boxes": int(boxes),
                },
            }
        self.mp.setattr(eng, "cybercombat_attack", fn)
        return self

    def attack_ic(self, ic_id: str, hacking_pool_dice: int = 0):
        """Drive the decker's cybercombat Attack endpoint against an active IC."""
        body = RunAttackInput(target_ic_id=ic_id, hacking_pool_dice=hacking_pool_dice)
        _call(mr.attack_ic(run_id=1, body=body, auth=AUTH_ADMIN, db=_FakeDB()))
        return self

    def crash_scramble(self, scramble_ref: str, boxes: int, atk_succ: int = 4, resist_succ: int = 0):
        """Crash a DISCOVERED Scramble IC in cybercombat (scripted damage)."""
        self.force_attack(boxes, atk_succ, resist_succ)
        _call(mr.crash_scramble(run_id=1, body=RunScrambleAttackInput(scramble_ref=scramble_ref),
                                auth=AUTH_ADMIN, db=_FakeDB()))
        return self

    def force_maneuver(self, won: bool, net: int = 2):
        """Script the next combat maneuver (eng.maneuver_test): win by `net`, or lose to the opponent."""
        m, o, ns = (net, 0, net) if won else (0, 2, -2)

        def fn(**_k):
            return {"maneuvering_roll": {"pool": 6, "tn": 4, "dice": [], "successes": m, "ones": 0},
                    "opposing_roll": {"pool": 6, "tn": 4, "dice": [], "successes": o, "ones": 0},
                    "net_successes": ns, "success": bool(won)}
        self.mp.setattr(eng, "maneuver_test", fn)
        return self

    def force_steamroller(self, crashed: bool, boxes: int = 10):
        """Script the next Steamroller strike (eng.steamroller_attack)."""
        def fn(**_k):
            return {"crashed": bool(crashed),
                    "to_hit_roll": {"pool": 6, "tn": 4, "dice": [], "successes": 4, "ones": 0},
                    "total_boxes": boxes, "boxes": boxes, "damage_level": "M", "tar_cm": 10}
        self.mp.setattr(eng, "steamroller_attack", fn)
        return self

    def force_slow(self, won: bool, net: int = 2, actions_lost: int = 10):
        """Script a Slow strike: land the to-hit (eng.roll_dice) and the opposed eng.slow_test."""
        self.mp.setattr(eng, "roll_dice",
                        lambda pool, tn: {"pool": pool, "tn": tn, "dice": [],
                                          "successes": 4 if won else 0, "ones": 0})

        def st(*, decker_pool, slow_rating, ic_dice):
            return {"net_successes": net if won else 0,
                    "actions_lost": actions_lost if won else 0,
                    "decker_roll": {"successes": 4 if won else 0, "ones": 0},
                    "ic_roll": {"successes": 0 if won else 2, "ones": 0}}
        self.mp.setattr(eng, "slow_test", st)
        return self

    def suppress(self, ic_id: str, release: bool = False):
        """Suppress (spend 1 DF to refund tally) or release a crashed-IC / data-bomb entry."""
        _call(mr.suppress_ic(run_id=1, body=RunSuppressInput(ic_id=ic_id, release=release),
                             auth=AUTH_ADMIN, db=_FakeDB()))
        return self

    def force_roll(self, successes: int):
        """Force eng.roll_dice to a fixed success count (for single-roll endpoints: scan, medic...)."""
        self.mp.setattr(eng, "roll_dice",
                        lambda pool, tn: {"pool": pool, "tn": tn, "dice": [],
                                          "successes": successes, "ones": 0})
        return self

    def force_disinfect(self, destroyed: bool):
        """Script the Disinfect System Test (eng.disinfect_test)."""
        def fn(*, decker_pool, subsystem_rating, disinfect_utility, security_value, det_factor):
            s = 3 if destroyed else 0
            return {"success": bool(destroyed), "worm_destroyed": bool(destroyed),
                    "decker_net_successes": 2 if destroyed else -1, "tn": 4,
                    "decker_roll": {"successes": s, "ones": 0}, "host_roll": {"successes": 0, "ones": 0},
                    "tally_increase": 0, "roll": {"successes": s, "ones": 0}}
        self.mp.setattr(eng, "disinfect_test", fn)
        return self

    def attack_enemy(self, enemy_id: str, boxes: int, program: str = "attack"):
        """Drive the strike-back-at-an-enemy-decker endpoint (scripted damage)."""
        self.force_attack(boxes)
        _call(mr.attack_enemy_decker(run_id=1, body=RunEnemyAttackInput(enemy_id=enemy_id, program=program),
                                     auth=AUTH_ADMIN, db=_FakeDB()))
        return self

    def scan_enemy(self, enemy_id: str, successes: int = 3):
        """Drive the Scan Icon endpoint vs a revealed enemy decker (scripted roll)."""
        self.force_roll(successes)
        _call(mr.scan_enemy_decker(run_id=1, body=RunEnemyScanInput(enemy_id=enemy_id),
                                   auth=AUTH_ADMIN, db=_FakeDB()))
        return self

    def area_attack(self, target_ids, boxes: int = 10):
        """Drive the Area-burst Attack endpoint against several icons (scripted per-target damage).
        Area rolls ONE attack (eng.roll_dice) then resists each target (eng.damage_resistance)."""
        self.mp.setattr(eng, "roll_dice",
                        lambda pool, tn: {"pool": pool, "tn": tn, "dice": [10] * 8,
                                          "successes": 8, "ones": 0})
        self.mp.setattr(eng, "damage_resistance",
                        lambda **_k: {"boxes": boxes, "final_damage_level": "M",
                                      "resist_roll": {"pool": 1, "tn": 2, "dice": [], "successes": 0, "ones": 0}})
        _call(mr.area_attack(run_id=1, body=RunAreaAttackInput(target_ids=list(target_ids)),
                             auth=AUTH_ADMIN, db=_FakeDB()))
        return self

    def force_purge_hog(self, purged: bool):
        """Script the Hog purge test (eng.hog_purge_test)."""
        self.mp.setattr(eng, "hog_purge_test",
                        lambda **_k: {"purged": bool(purged), "tn": 4,
                                      "roll": {"successes": 3 if purged else 0, "ones": 0}})
        return self

    def force_locate_decker(self, located: bool):
        """Script the opposed PC-locate-decker test (eng.pc_locate_decker_test)."""
        self.mp.setattr(eng, "pc_locate_decker_test",
                        lambda **_k: {"located": bool(located),
                                      "roll": {"successes": 3 if located else 0, "ones": 0}})
        return self

    def defend(self, hacking_pool_dice: int = 0):
        """Drive the interactive per-attack defense endpoint (resolves state['pending_defense'])."""
        _call(mr.defend(run_id=1, body=RunDefendInput(hacking_pool_dice=hacking_pool_dice),
                        auth=AUTH_ADMIN, db=_FakeDB()))
        return self

    def logoff(self, decker_succ: int = 3, host_succ: int = 0, hacking_pool_dice: int = 0):
        """Drive the Graceful Logoff endpoint with a scripted Access Test outcome."""
        self.mp.setattr(eng, "system_test", _scripted_system_test(decker_succ, host_succ))
        _call(mr.graceful_logoff(run_id=1, body=RunLogoffInput(hacking_pool_dice=hacking_pool_dice),
                                 auth=AUTH_ADMIN, db=_FakeDB()))
        return self

    def jack_out(self):
        """Drive the emergency jack-out endpoint."""
        _call(mr.jack_out(run_id=1, auth=AUTH_ADMIN, db=_FakeDB()))
        return self

    def enter_trap_door(self, td_id: str, decker_succ: int = 3, host_succ: int = 0):
        """Drive the trap-door transit endpoint (its logoff Access Test is scripted)."""
        self.mp.setattr(eng, "system_test", _scripted_system_test(decker_succ, host_succ))
        _call(mr.trap_door_action(run_id=1, td_id=td_id, body=RunTrapDoorInput(action="enter"),
                                  auth=AUTH_ADMIN, db=_FakeDB()))
        return self

    def player(self) -> dict:
        return mr._serialize_run(self.run, AUTH_PLAYER).get("state_json", {}) or {}

    def admin(self) -> dict:
        return mr._serialize_run(self.run, AUTH_ADMIN).get("state_json", {}) or {}


# --------------------------------------------------------------------------- helpers
def _host_cfg(**over):
    cfg = {
        "security_code": "Green", "security_value": 4,
        "acifs": [3, 4, 5, 6, 7], "sheaf": [],
        "paydata": [], "scrambles": [], "data_bombs": [], "slave_pieces": [],
    }
    cfg.update(over)
    return cfg


def _assert_admin_superset(flow: Flow, ctx: str):
    """The admin sees everything the player sees, and at least as much event-log detail."""
    p, a = flow.player(), flow.admin()
    for key in ("located_paydata", "active_ic", "enemy_deckers"):
        pid = {(e.get("id") or e.get("name")) for e in (p.get(key) or []) if isinstance(e, dict)}
        aid = {(e.get("id") or e.get("name")) for e in (a.get(key) or []) if isinstance(e, dict)}
        assert pid <= aid, f"[{ctx}] admin {key} missing what the player sees: {pid - aid}"
    assert len(a.get("event_log") or []) >= len(p.get("event_log") or []), (
        f"[{ctx}] admin event log has fewer entries than the player's")
    if p.get("host_ratings_revealed"):
        for k in p["host_ratings_revealed"]:
            assert k in (a.get("host_ratings_revealed") or {}), (
                f"[{ctx}] admin missing host rating {k} the player can see")


def _last_action_event(state, action_type):
    for ev in reversed(state.get("event_log") or []):
        if isinstance(ev, dict) and ev.get("action") == action_type:
            return ev
    return None


def _last_event_of_type(state, ev_type):
    """The most recent event by its `type` tag. Handler side-effect events (defuse, invalidate,
    data-bomb detonation, ...) are `type`-tagged, unlike the single primary `action` event."""
    for ev in reversed(state.get("event_log") or []):
        if isinstance(ev, dict) and ev.get("type") == ev_type:
            return ev
    return None


# =============================================================================
# DEPTH-FIRST branch tree. Start at the root (Logon) and walk each branch -- success AND failure --
# to its conclusion before rolling up to the next decision. Each node asserts the exact rendered
# outcome for BOTH branches, so "a success looks like a success and a failure looks like a failure".
#
# LEVEL 0 -- LOGON: the entry step. You get on the host, or you do not.
# =============================================================================
def test_logon_success_puts_the_decker_on_the_host(monkeypatch):
    flow = Flow(monkeypatch, _host_cfg())
    flow.act("logon_to_host", subsystem="access", decker_succ=3, host_succ=0)
    p = flow.player()
    assert p.get("logon_complete") is True, "a successful logon must put the decker on the host"
    ev = _last_action_event(p, "logon_to_host")
    assert ev is not None and ev.get("success") is True, "logon success must render a SUCCESS event"
    assert flow.run.status == "active", "a successful logon keeps the run active (on the host)"
    _assert_admin_superset(flow, "logon success")


def test_logon_failure_keeps_the_decker_out(monkeypatch):
    flow = Flow(monkeypatch, _host_cfg())
    flow.act("logon_to_host", subsystem="access", decker_succ=0, host_succ=1)   # decker whiffs
    p = flow.player()
    assert not p.get("logon_complete"), "a failed logon must NOT put the decker on the host"
    ev = _last_action_event(p, "logon_to_host")
    assert ev is not None and ev.get("success") is False, "logon failure must render a FAILED event"
    assert flow.run.status == "active", "a failed logon must not end the run"
    # Host actions stay blocked until a successful logon (the decker is not on the host yet).
    flow.act_rejected("analyze_host", subsystem="control")
    assert not flow.player().get("logon_complete")


def test_logon_retry_after_a_new_pass_succeeds(monkeypatch):
    # A failed logon still spends the action economy (RAW: a failed action costs the action), so a
    # retry needs a fresh pass. End Turn, then the retried logon gets the decker on.
    flow = Flow(monkeypatch, _host_cfg())
    flow.act("logon_to_host", subsystem="access", decker_succ=0, host_succ=1)   # fail
    assert not flow.player().get("logon_complete")
    flow.new_turn()                                                             # refresh the budget
    flow.act("logon_to_host", subsystem="access", decker_succ=3, host_succ=0)   # retry -> succeed
    assert flow.player().get("logon_complete") is True, "a retried logon after End Turn should succeed"
    _assert_admin_superset(flow, "logon retry after new pass")


def test_host_action_before_logon_is_refused(monkeypatch):
    flow = Flow(monkeypatch, _host_cfg())
    exc = flow.act_rejected("analyze_host", subsystem="control")
    assert exc.status_code == 400, "a host action before logon must be refused with 400"
    assert not flow.player().get("logon_complete")


# =============================================================================
# FLOW: Analyze Host -> reveal is gated by successes (your example).
#   - 0 successes  -> nothing revealed, no picker.
#   - N (< hidden) -> bank exactly N credits, reveal nothing yet, THEN pick N subsystems.
#   - >= hidden    -> reveal everything at once, no picker.
# =============================================================================
def test_flow_analyze_host_zero_successes_reveals_nothing(monkeypatch):
    flow = Flow(monkeypatch, _host_cfg())
    flow.act("logon_to_host", subsystem="access", decker_succ=3)
    flow.act("analyze_host", subsystem="control", decker_succ=0)
    p = flow.player()
    assert not (p.get("host_ratings_revealed") or {}), "a 0-success Analyze Host revealed a rating"
    assert not p.get("host_analyze_pending"), "a 0-success Analyze Host offered a reveal pick"
    _assert_admin_superset(flow, "analyze_host 0-succ")


def test_flow_analyze_host_partial_banks_then_pick_reveals_exactly_that_many(monkeypatch):
    flow = Flow(monkeypatch, _host_cfg())            # 5 hidden ACIFS
    flow.act("logon_to_host", subsystem="access", decker_succ=3)
    flow.act("analyze_host", subsystem="control", decker_succ=3)   # 3 < 5 -> bank 3
    p = flow.player()
    assert not (p.get("host_ratings_revealed") or {}), "partial Analyze Host revealed before the pick"
    pending = p.get("host_analyze_pending")
    assert pending and int(pending.get("credits", 0)) == 3, (
        f"3 successes should bank exactly 3 reveal credits, got {pending!r}")

    flow.reveal(["access", "control", "index"])       # spend the 3 credits
    p = flow.player()
    revealed = p.get("host_ratings_revealed") or {}
    assert set(revealed) == {"access", "control", "index"}, f"picked reveal mismatch: {revealed}"
    assert not p.get("host_analyze_pending"), "pending credits not cleared after revealing"
    _assert_admin_superset(flow, "analyze_host partial+reveal")


def test_flow_analyze_host_full_reveals_all_without_a_pick(monkeypatch):
    flow = Flow(monkeypatch, _host_cfg())            # 5 ACIFS + Security Rating = 6 hidden items
    flow.act("logon_to_host", subsystem="access", decker_succ=3)
    flow.act("analyze_host", subsystem="control", decker_succ=6)   # >= 6 hidden -> reveal all
    p = flow.player()
    assert set(p.get("host_ratings_revealed") or {}) == {"access", "control", "index", "files", "slave"}, (
        "6 successes should reveal all five ACIFS ratings at once")
    assert p.get("host_security_revealed") is True, "6 successes should also reveal the Security Rating"
    assert not p.get("host_analyze_pending"), "a full Analyze Host still offered a pick"
    _assert_admin_superset(flow, "analyze_host full")


# =============================================================================
# FLOW: Locate File -> the key file appears ENCRYPTED with its size hidden; Analyze Icon reveals the
# size + discovers the covering Scramble (the file stays encrypted until a later Decrypt). Your
# example: "do the key data points appear as they should -- not encrypted until I analyze the icon".
# =============================================================================
KEYFILE_ID = "pd0"
KEYFILE_NAME = "Payroll DB"


def _paydata_host_cfg():
    return _host_cfg(
        paydata=[{"id": KEYFILE_ID, "name": KEYFILE_NAME, "density": 90, "is_key": True, "defense": 0}],
        scrambles=[{"target_key": f"files::file::{KEYFILE_NAME}", "rating": 6, "variant": "poison"}],
    )


def _located(state, file_id):
    for p in (state.get("located_paydata") or []):
        if isinstance(p, dict) and p.get("id") == file_id:
            return p
    return None


def _scramble_discovered(state) -> bool:
    return bool(state.get("discovered_scrambles"))


def test_flow_locate_file_then_analyze_icon_progressive_disclosure(monkeypatch):
    flow = Flow(monkeypatch, _paydata_host_cfg())
    flow.act("logon_to_host", subsystem="access", decker_succ=3)

    # Step 1 -- Locate File surfaces the key file with its size hidden; the covering Scramble is NOT
    # yet known to the player (encryption is disclosed only by an Analyze Icon or a blind Download).
    flow.act("locate_file", subsystem="index", target_file=KEYFILE_NAME, decker_succ=3)
    p = flow.player()
    f = _located(p, KEYFILE_ID)
    assert f is not None, "Locate File did not surface the key file to the player"
    assert f.get("encrypted") is not True, "encryption must not be pre-leaked before it is discovered"
    assert f.get("size_mp") is None, "the file size must stay hidden until Analyze Icon"
    assert f.get("analyzed") is False, "the file must not be analyzed yet"
    assert not _scramble_discovered(p), "the Scramble must not be discovered before Analyze Icon"
    # The admin sees the real size from the start AND still knows a lock is hidden there (GM marker),
    # but its ACTION gate is uniform with the player -- it too blind-downloads until discovery.
    a = _located(flow.admin(), KEYFILE_ID)
    assert a and a.get("size_mp") == 90, "the admin should see the real size immediately"
    assert a.get("encrypted") is not True, "the encryption action gate is uniform (admin blind-downloads too)"
    assert a.get("scrambled") is True, "the admin still SEES the hidden Scramble via the GM marker"
    _assert_admin_superset(flow, "post-locate")

    # Step 2 -- Analyze Icon reveals the real size and discovers the covering Scramble; the file now
    # reads ENCRYPTED to the player (it stays encrypted until a later Decrypt clears the Scramble).
    flow.act("analyze_icon", subsystem="control", target_file=f"files::{KEYFILE_ID}", decker_succ=3)
    p = flow.player()
    f = _located(p, KEYFILE_ID)
    assert f.get("analyzed") is True, "Analyze Icon must mark the file analyzed"
    assert f.get("size_mp") == 90, "Analyze Icon must reveal the real file size to the player"
    assert f.get("encrypted") is True, "the file now reads encrypted to the player (until Decrypt)"
    assert _scramble_discovered(p), "Analyze Icon must surface the covering Scramble to the player"
    _assert_admin_superset(flow, "post-analyze-icon")


# =============================================================================
# LEVEL 1+ -- FILE ACQUISITION TREE (depth-first). From logged on: Locate File, then walk the file:
#   plain file      -> Download (success/fail) + Edit (erase/modify).
#   encrypted file  -> Download REFUSED (Scramble lock) -> Analyze Icon (reveal size + discover
#                      Scramble, success/fail) -> Decrypt File (success -> unlock; Poison fail ->
#                      data may be wiped) -> Download.
# Action economy note: Locate File is Complex (2 AP), so a New Turn refreshes the budget before the
# next action; Analyze Icon is Free, Download / Edit / Decrypt are Simple (1 AP).
# =============================================================================
PLAIN_ID, PLAIN_NAME = "memo", "Memo"
ENC_ID, ENC_NAME = "pd0", "Payroll DB"


def _files_host_cfg():
    return _host_cfg(
        paydata=[
            {"id": PLAIN_ID, "name": PLAIN_NAME, "density": 40, "is_key": True, "defense": 0},
            {"id": ENC_ID, "name": ENC_NAME, "density": 90, "is_key": True, "defense": 0},
        ],
        scrambles=[{"target_key": f"files::file::{ENC_NAME}", "rating": 6, "variant": "poison"}],
    )


def _logged_on_files(monkeypatch):
    flow = Flow(monkeypatch, _files_host_cfg())
    flow.act("logon_to_host", subsystem="access", decker_succ=3)
    return flow


def _raw_paydata(flow, file_id):
    for p in (flow.run.state_json.get("paydata") or []):
        if isinstance(p, dict) and p.get("id") == file_id:
            return p
    return {}


# -- Locate File: found vs not-found --
def test_locate_file_success_finds_the_key_files(monkeypatch):
    flow = _logged_on_files(monkeypatch)
    flow.act("locate_file", subsystem="index", target_file=ENC_NAME, decker_succ=3)
    p = flow.player()
    assert _located(p, PLAIN_ID) is not None, "Locate File should find the plain key file"
    assert _located(p, ENC_ID) is not None, "Locate File should find the encrypted key file"
    _assert_admin_superset(flow, "locate_file success")


def test_locate_file_failure_finds_nothing(monkeypatch):
    flow = _logged_on_files(monkeypatch)
    flow.act("locate_file", subsystem="index", target_file=ENC_NAME, decker_succ=0, host_succ=1)
    assert not (flow.player().get("located_paydata") or []), "a failed Locate File locates nothing"


# -- Plain file branch: Download (success/fail), Edit (erase/modify) --
def test_plain_file_download_success_grabs_it_and_charges_storage(monkeypatch):
    flow = _logged_on_files(monkeypatch)
    flow.act("locate_file", subsystem="index", decker_succ=3).new_turn()
    flow.act("download_data", subsystem="files", target_file=PLAIN_NAME, decker_succ=3)
    p = flow.player()
    assert _located(p, PLAIN_ID).get("downloaded") is True, "a successful Download marks it downloaded"
    assert any(d.get("id") == PLAIN_ID for d in p.get("downloaded_files") or []), "not in the ledger"
    assert (p.get("storage_used_mp") or 0) > 0, "Download must charge deck storage"
    _assert_admin_superset(flow, "plain download success")


def test_plain_file_download_failure_leaves_it_ungrabbed(monkeypatch):
    flow = _logged_on_files(monkeypatch)
    flow.act("locate_file", subsystem="index", decker_succ=3).new_turn()
    flow.act("download_data", subsystem="files", target_file=PLAIN_NAME, decker_succ=0, host_succ=1)
    p = flow.player()
    assert not _located(p, PLAIN_ID).get("downloaded"), "a failed Download must not grab the file"
    assert not (p.get("downloaded_files") or []), "a failed Download must not add a ledger entry"


def test_plain_file_edit_erase_destroys_it(monkeypatch):
    flow = _logged_on_files(monkeypatch)
    flow.act("locate_file", subsystem="index", decker_succ=3).new_turn()
    flow.act("edit_file", subsystem="files", target_file=PLAIN_NAME, edit_mode="erase", decker_succ=3)
    assert _raw_paydata(flow, PLAIN_ID).get("destroyed") is True, "Erase must destroy the file"


def test_plain_file_edit_modify_tampers_it(monkeypatch):
    flow = _logged_on_files(monkeypatch)
    flow.act("locate_file", subsystem="index", decker_succ=3).new_turn()
    flow.act("edit_file", subsystem="files", target_file=PLAIN_NAME, edit_mode="modify", decker_succ=3)
    assert _raw_paydata(flow, PLAIN_ID).get("tampered") is True, "Modify must tamper (file stays)"
    assert not _raw_paydata(flow, PLAIN_ID).get("destroyed"), "Modify must NOT destroy the file"


# -- Encrypted file branch: blind Download ATTEMPT reveals the Scramble -> Analyze Icon -> Decrypt --
def test_encrypted_file_download_attempt_reveals_the_scramble(monkeypatch):
    flow = _logged_on_files(monkeypatch)
    flow.act("locate_file", subsystem="index", decker_succ=3).new_turn()
    # Before the attempt the player does not yet know the located file is encrypted.
    assert _located(flow.player(), ENC_ID).get("encrypted") is not True, "encryption is not pre-leaked"
    # A blind Download attempt cannot read the encrypted data, but the attempt DISCOVERS the Scramble.
    flow.act("download_data", subsystem="files", target_file=ENC_NAME, decker_succ=3)
    p = flow.player()
    assert not _located(p, ENC_ID).get("downloaded"), "encrypted data cannot actually be downloaded"
    assert _located(p, ENC_ID).get("encrypted") is True, "the attempt reveals the encryption to the player"
    assert _scramble_discovered(p), "the covering Scramble is now discovered (offer Decrypt on the file card)"
    # The event names the REAL file (its name), not its internal id / scramble target key.
    ev = next((e for e in reversed(p.get("event_log") or [])
               if e.get("type") == "file_access_encrypted"), None)
    assert ev and ENC_NAME in (ev.get("description") or ""), "the event must name the real file"
    assert "File:" not in (ev.get("description") or ""), "the event must not show the raw target key"


def test_admin_sees_hidden_scramble_but_keeps_the_players_blind_download(monkeypatch):
    # Runner/admin "sees more" (a GM 'scrambled' marker on a still-undiscovered lock) but keeps the
    # SAME action gate as the player -- it too blind-downloads until the Scramble is discovered.
    flow = _logged_on_files(monkeypatch)
    flow.act("locate_file", subsystem="index", decker_succ=3)
    a = _located(flow.admin(), ENC_ID)
    assert a.get("encrypted") is not True, "admin action gate is uniform -- not the encrypted branch yet"
    assert a.get("scrambled") is True, "admin still SEES the hidden Scramble via the GM marker"
    assert "scramble_ref" not in a, "no Decrypt target until discovery -- admin blind-downloads like the player"


def test_encrypted_file_download_attempt_on_an_exploding_scramble_detonates(monkeypatch):
    # Grabbing a file blind instead of Analyzing it first is the risk: an undefused Exploding
    # Scramble's linked data bomb goes off on the download attempt.
    flow = _logged_on(monkeypatch, _exploding_host_cfg())
    flow.act("locate_file", subsystem="index", decker_succ=3).new_turn()
    flow.act("download_data", subsystem="files", target_file=EXP_NAME, decker_succ=3)
    assert _detonated(flow.player()), "a blind Download of an Exploding Scramble file detonates its bomb"
    assert not _located(flow.player(), EXP_ID).get("downloaded"), "the encrypted file is still not grabbed"


def test_encrypted_file_analyze_icon_failure_reveals_nothing(monkeypatch):
    flow = _logged_on_files(monkeypatch)
    flow.act("locate_file", subsystem="index", decker_succ=3).new_turn()
    flow.act("analyze_icon", subsystem="control", target_file=f"files::{ENC_ID}", decker_succ=0, host_succ=1)
    p = flow.player()
    f = _located(p, ENC_ID)
    assert not f.get("analyzed"), "a failed Analyze Icon must not analyze the file"
    assert f.get("size_mp") is None, "a failed Analyze Icon must not reveal the size"
    assert not _scramble_discovered(p), "a failed Analyze Icon must not discover the Scramble"


def test_encrypted_file_decrypt_success_unlocks_download(monkeypatch):
    flow = _logged_on_files(monkeypatch)
    flow.act("locate_file", subsystem="index", decker_succ=3).new_turn()
    flow.act("analyze_icon", subsystem="control", target_file=f"files::{ENC_ID}", decker_succ=3)
    flow.force_decrypt(True).act("decrypt_file", subsystem="files",
                                 target_file=f"files::file::{ENC_ID}")
    f = _located(flow.player(), ENC_ID)
    assert f.get("encrypted") is False, "a successful Decrypt clears the Scramble"
    # ...and the file is now downloadable.
    flow.act("download_data", subsystem="files", target_file=ENC_NAME, decker_succ=3)
    assert _located(flow.player(), ENC_ID).get("downloaded") is True, "after Decrypt the file downloads"
    _assert_admin_superset(flow, "decrypt+download")


def test_encrypted_file_decrypt_poison_failure_can_wipe_the_data(monkeypatch):
    flow = _logged_on_files(monkeypatch)
    flow.act("locate_file", subsystem="index", decker_succ=3).new_turn()
    flow.act("analyze_icon", subsystem="control", target_file=f"files::{ENC_ID}", decker_succ=3)
    flow.force_decrypt(False).force_scramble_failure(destroyed=True, key_lost=True).act(
        "decrypt_file", subsystem="files", target_file=f"files::file::{ENC_ID}")
    assert _raw_paydata(flow, ENC_ID).get("destroyed") is True, (
        "a failed Poison Decrypt (poison test succeeds) must erase the protected data")


def test_encrypted_file_decrypt_poison_failure_can_leave_data_intact(monkeypatch):
    flow = _logged_on_files(monkeypatch)
    flow.act("locate_file", subsystem="index", decker_succ=3).new_turn()
    flow.act("analyze_icon", subsystem="control", target_file=f"files::{ENC_ID}", decker_succ=3)
    flow.force_decrypt(False).force_scramble_failure(destroyed=False).act(
        "decrypt_file", subsystem="files", target_file=f"files::file::{ENC_ID}")
    f = _raw_paydata(flow, ENC_ID)
    assert not f.get("destroyed"), "a failed Poison Decrypt whose poison test fails must NOT wipe the data"
    assert _file_scramble_still_present(flow, ENC_ID), "a failed Decrypt leaves the Scramble in place"


def _file_scramble_still_present(flow, file_id) -> bool:
    return any(s.get("target_key") == f"files::file::{file_id}"
               for s in (flow.run.state_json.get("scrambles") or []))


# -- Exploding Scramble: its linked data bomb detonates on ANY decrypt unless the bomb is defused --
EXP_ID, EXP_NAME = "expf", "Secret"


def _exploding_host_cfg():
    return _host_cfg(
        paydata=[{"id": EXP_ID, "name": EXP_NAME, "density": 40, "is_key": True, "defense": 0}],
        scrambles=[{"target_key": f"files::file::{EXP_NAME}", "rating": 6, "variant": "exploding"}],
        data_bombs=[{"target": f"files::{EXP_NAME}", "rating": 5}],
    )


def _only_scramble_key(flow):
    return flow.run.state_json["scrambles"][0]["target_key"]


def _any_scramble_present(flow) -> bool:
    return bool(flow.run.state_json.get("scrambles"))


def test_exploding_scramble_decrypt_without_defusing_detonates(monkeypatch):
    flow = _logged_on(monkeypatch, _exploding_host_cfg())
    flow.act("locate_file", subsystem="index", decker_succ=3)                                  # 2 AP -> 0
    flow.act("analyze_icon", subsystem="control", target_file=f"files::{EXP_ID}", decker_succ=3)  # Free: discover
    flow.new_turn()
    flow.force_decrypt(True).act("decrypt_file", subsystem="files", target_file=_only_scramble_key(flow))
    assert _detonated(flow.player()), (
        "decrypting an UNDEFUSED Exploding Scramble detonates its linked data bomb")


def test_exploding_scramble_decrypt_is_safe_after_defusing_the_bomb(monkeypatch):
    flow = _logged_on(monkeypatch, _exploding_host_cfg())
    flow.act("locate_file", subsystem="index", decker_succ=3)                                  # 2 AP -> 0
    flow.act("analyze_icon", subsystem="control", target_file=f"files::{EXP_ID}", decker_succ=3)  # Free: discover both
    flow.new_turn()
    flow.force_defuse(True).act("defuse_data_bomb", subsystem="files", target_file=EXP_NAME)   # Complex 2 -> 0
    flow.new_turn()
    flow.force_decrypt(True).act("decrypt_file", subsystem="files", target_file=_only_scramble_key(flow))
    assert not _detonated(flow.player()), "defusing the linked bomb FIRST makes the decrypt safe"
    assert not _any_scramble_present(flow), "a successful Decrypt still clears the Scramble"


# -- Decompress: expand a SQUEEZED program in active memory (no test); files are NOT decompressable --
def test_decompress_expands_a_squeezed_program(monkeypatch):
    flow = _logged_on(monkeypatch)
    # A squeezed program parks in active memory (half footprint), unusable until decompressed.
    flow.run.state_json["squeezed_active"] = [{"name": "sleaze", "rating": 6, "size": 20}]
    flow.run.state_json["active_memory_cap"] = 0   # untracked -> no memory gate for this case
    flow.act("decompress_file", subsystem="files", target_program="sleaze")
    assert not flow.run.state_json.get("squeezed_active"), "decompress clears the squeezed holding area"
    assert flow.run.decker_json.get("utilities", {}).get("sleaze") == 6, "the program is now usable"
    ev = _last_event_of_type(flow.player(), "program_decompressed")
    assert ev is not None and ev.get("outcome") == "ok", "decompress must render as ok"


def test_decompress_with_no_squeezed_program_is_a_clean_noop(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.act("decompress_file", subsystem="files", target_program="nonexistent")
    ev = _last_event_of_type(flow.player(), "program_decompressed")
    assert ev is not None and ev.get("outcome") == "no_target", "no squeezed program -> a no-op event"


# =============================================================================
# LEVEL 1 -- RECON / STATUS ACTIONS (from logged on). Each: success renders its reveal, failure
# renders nothing (or the blocked branch). All single-action, so no New Turn is needed.
# =============================================================================
def _logged_on(monkeypatch, cfg=None, trap_doors=None):
    flow = Flow(monkeypatch, cfg or _host_cfg(), trap_doors=trap_doors)
    flow.act("logon_to_host", subsystem="access", decker_succ=3)
    return flow


def _inject_ic(flow, ic_type="Killer", rating=6, ic_id="ic1", **extra):
    ic = {"id": ic_id, "type": ic_type, "rating": rating, "status": "active",
          "detection_level": 3, "category": "proactive", "boxes": 0, "intruding": False}
    ic.update(extra)
    flow.run.state_json.setdefault("active_ic", []).append(ic)
    return ic


# -- Analyze Security: success snapshots tally/alert; failure reveals nothing --
def test_analyze_security_success_snapshots_tally_and_alert(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.act("analyze_security", subsystem="access", decker_succ=3)
    p = flow.player()
    sk = p.get("security_known")
    assert sk is not None, "a successful Analyze Security must snapshot the security state"
    assert "tally" in sk and "alert" in sk, "the snapshot must carry the tally + alert"


def test_analyze_security_failure_reveals_nothing(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.act("analyze_security", subsystem="access", decker_succ=0, host_succ=1)
    assert not flow.player().get("security_known"), "a failed Analyze Security reveals no security state"


# -- Analyze Subsystem: Access reveals LTG; Files discovers a node Scramble; failure blocks --
def test_analyze_subsystem_access_reveals_ltg(monkeypatch):
    flow = _logged_on(monkeypatch)          # _HostNS carries an ltg_address
    flow.act("analyze_subsystem", subsystem="access", decker_succ=3)
    p = flow.player()
    assert p.get("host_ltg_revealed") is True, "Analyze Subsystem (Access) must reveal LTG status"
    assert "host_has_ltg" in p, "the host_has_ltg flag must surface once Access is analyzed"


def test_analyze_subsystem_access_failure_leaves_ltg_hidden(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.act("analyze_subsystem", subsystem="access", decker_succ=0, host_succ=1)
    assert not flow.player().get("host_ltg_revealed"), "a failed Access analyze leaves LTG hidden"


def test_analyze_subsystem_files_discovers_a_node_scramble(monkeypatch):
    cfg = _host_cfg(scrambles=[{"target_key": "files::entire", "rating": 6, "variant": "poison"}])
    flow = _logged_on(monkeypatch, cfg)
    flow.act("analyze_subsystem", subsystem="files", decker_succ=3)
    assert flow.player().get("discovered_scrambles"), (
        "Analyze Subsystem (Files) must discover a node-level (files::entire) Scramble")


def test_analyze_subsystem_discovers_a_trap_door(monkeypatch):
    flow = _logged_on(monkeypatch, trap_doors=[
        {"id": "td1", "source_piece": "maglock", "subsystem": "access",
         "destination_host_id": None, "destination_ltg": "", "destination_label": "??"}])
    flow.act("analyze_subsystem", subsystem="access", decker_succ=3)
    assert flow.player().get("discovered_trap_doors"), (
        "Analyze Subsystem must surface a concealed trap door on that subsystem")


# -- Validate Passcode: success grants Legitimate; failure does not --
def test_validate_passcode_success_grants_legitimate(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.act("validate_passcode", subsystem="access", decker_succ=3)
    assert flow.player().get("has_legitimate_status") is True, "a successful Validate grants Legitimate"


def test_validate_passcode_failure_grants_nothing(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.act("validate_passcode", subsystem="access", decker_succ=0, host_succ=1)
    assert not flow.player().get("has_legitimate_status"), "a failed Validate grants no Legitimate status"


# -- Invalidate Passcode: whole-system flips everything; a single IC flips that one --
def test_invalidate_passcode_all_flips_the_whole_table(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.act("invalidate_passcode", subsystem="access", target_ic_id="__all__", decker_succ=3)
    ev = _last_event_of_type(flow.player(), "invalidate_passcode")
    assert ev is not None and ev.get("success") is True and ev.get("whole_list") is True, (
        "Invalidate (entire system) must erase the whole passcode table")


def test_invalidate_passcode_single_flips_that_ic_to_intruding(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="ic1", intruding=False)
    flow.act("invalidate_passcode", subsystem="access", target_ic_id="ic1", decker_succ=3)
    ev = _last_event_of_type(flow.player(), "invalidate_passcode")
    assert ev is not None and ev.get("success") is True and ev.get("flipped"), (
        "Invalidate on one IC must flip that IC's passcode")


# -- Redirect Datatrail: first succeeds; a second on the same host is refused --
def test_redirect_datatrail_success_then_second_is_refused(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.act("redirect_datatrail", subsystem="control", decker_succ=3)
    assert flow.player().get("redirects_placed") == 1, "a successful Redirect places the datatrail redirect"
    exc = flow.act_rejected("redirect_datatrail", subsystem="control")
    assert "redirect" in str(exc.detail).lower(), "a second Redirect on the same host must be refused"


# -- Crash Host: success starts the shutdown countdown (turns = ceil(10 / successes)) --
def test_crash_host_success_starts_countdown(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.act("crash_host", subsystem="control", decker_succ=3)   # ceil(10/3) = 4 turns
    cd = flow.player().get("crash_host_countdown")
    assert cd is not None and cd.get("turns_remaining") == 4, (
        "Crash Host must start a countdown of ceil(10/successes) turns")


def test_crash_host_failure_starts_no_countdown(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.act("crash_host", subsystem="control", decker_succ=0, host_succ=1)
    assert not flow.player().get("crash_host_countdown"), "a failed Crash Host starts no countdown"


# -- Decoy: success projects a decoy carrying the decker's successes --
def test_decoy_success_projects_a_decoy(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.act("decoy", subsystem="control", decker_succ=3)
    assert flow.player().get("decoy_successes") == 3, "a successful Decoy records its successes"


# -- Relocate: spoof / suppress a Trace IC while it runs its location cycle --
def test_relocate_spoofs_a_tracing_ic(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="tr1", ic_type="Trace", rating=6, trace_phase="locate")
    flow.act("relocate", subsystem="control", target_ic_id="tr1", decker_succ=3)
    assert _active_ic(flow, "tr1").get("trace_spoofed_turn") is not None, (
        "Relocate spoofs the tracing IC for this turn")


def test_relocate_with_suppress_pauses_the_trace(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="tr1", ic_type="Trace", rating=6, trace_phase="locate")
    flow.act("relocate", subsystem="control", target_ic_id="tr1", suppress_trace=True, decker_succ=3)
    ic = _active_ic(flow, "tr1")
    assert ic.get("suppressed") is True or ic.get("relocate_suppress_pending") is True, (
        "Relocate + suppress pauses the trace (-1 DF) or holds it at the DF minimum")


def test_relocate_with_no_tracing_ic_reports_none(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="k1", ic_type="Killer", rating=6)      # not a trace IC
    flow.act("relocate", subsystem="control", target_ic_id="k1", decker_succ=3)
    ev = _last_event_of_type(flow.admin(), "relocate")
    assert ev is not None and "no trace" in (ev.get("description") or "").lower(), (
        "Relocate with no tracing IC reports nothing to spoof")


# -- Locate Paydata: net-gated. net>0 locates that many random files; a tie/loss locates none --
def _paydata_sweep_cfg():
    return _host_cfg(paydata=[
        {"id": "pdA", "name": "Loot A", "density": 20, "is_key": False},
        {"id": "pdB", "name": "Loot B", "density": 30, "is_key": False},
        {"id": "pdC", "name": "Loot C", "density": 40, "is_key": False},
    ])


def test_locate_paydata_net_two_locates_two_files(monkeypatch):
    flow = _logged_on(monkeypatch, _paydata_sweep_cfg())
    flow.act("locate_paydata", subsystem="index", decker_succ=2, host_succ=0)   # net 2
    located = [p for p in (flow.player().get("located_paydata") or [])]
    assert len(located) == 2, "each net success on Locate Paydata should reveal one file (net 2 -> 2)"


def test_locate_paydata_tie_locates_nothing(monkeypatch):
    flow = _logged_on(monkeypatch, _paydata_sweep_cfg())
    flow.act("locate_paydata", subsystem="index", decker_succ=2, host_succ=2)   # net 0 -> effect-gated fail
    assert not (flow.player().get("located_paydata") or []), (
        "Locate Paydata is effect-gated: a net-zero tie locates nothing")


# -- Null Operation: a no-test idle that always resolves without error --
def test_null_operation_is_a_clean_idle(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.act("null_operation", subsystem="access", decker_succ=3)
    assert flow.run.status == "active", "Null Operation just idles -- the run stays active"


# =============================================================================
# LEVEL 1 -- IC RECON (from logged on, with an IC on the host):
#   Analyze IC identifies an IC (or reveals a discovered Scramble's rating); Locate IC surfaces a
#   hidden IC; Locate Decker re-acquires an evaded hostile decker (clear branch here).
# =============================================================================
def test_analyze_ic_identifies_an_active_ic(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="ic1", ic_type="Killer", rating=6)   # detection_level 3 -> analyzable
    flow.act("analyze_ic", subsystem="control", target_ic_id="ic1", decker_succ=3)
    assert _active_ic(flow, "ic1").get("analyzed") is True, "Analyze IC marks the IC identified"
    ev = _last_event_of_type(flow.player(), "ic_analyzed")
    assert ev is not None and ev.get("ic_rating") == 6, "the reveal must carry the IC's rating"


def test_analyze_ic_failure_identifies_nothing(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="ic1", rating=6)
    flow.act("analyze_ic", subsystem="control", target_ic_id="ic1", decker_succ=0, host_succ=1)
    assert not _active_ic(flow, "ic1").get("analyzed"), "a failed Analyze IC reveals nothing"


def test_analyze_ic_on_a_discovered_scramble_reveals_its_rating(monkeypatch):
    cfg = _host_cfg(scrambles=[{"target_key": "files::entire", "rating": 6, "variant": "poison"}])
    flow = _logged_on(monkeypatch, cfg)
    flow.act("analyze_subsystem", subsystem="files", decker_succ=3)    # Simple -> discover node scramble
    flow.act("analyze_ic", subsystem="control", target_ic_id="files::entire", decker_succ=3)  # Free
    assert flow.run.state_json["scrambles"][0].get("rating_revealed") is True, (
        "Analyze IC on a discovered Scramble reveals its Rating (the Decrypt TN)")


def test_locate_ic_success_finds_a_hidden_ic(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="lurk1", detection_level=0)          # hidden (level 0)
    flow.act("locate_ic", subsystem="index", target_ic_id="lurk1", decker_succ=3)
    assert _active_ic(flow, "lurk1").get("located") is True, "Locate IC surfaces the hidden IC"
    ev = _last_event_of_type(flow.admin(), "ic_relocate")
    assert ev is not None and ev.get("outcome") == "located", "success must render as located"


def test_locate_ic_failure_leaves_it_hidden(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="lurk1", detection_level=0)
    flow.act("locate_ic", subsystem="index", target_ic_id="lurk1", decker_succ=0, host_succ=1)
    assert not _active_ic(flow, "lurk1").get("located"), "a failed Locate IC leaves it hidden"
    ev = _last_event_of_type(flow.admin(), "ic_relocate")
    assert ev is not None and ev.get("outcome") == "fail"


def test_locate_ic_with_nothing_hidden_reports_none(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="vis1", detection_level=3)          # already visible
    flow.act("locate_ic", subsystem="index", target_ic_id="vis1", decker_succ=3)
    ev = _last_event_of_type(flow.admin(), "ic_relocate")
    assert ev is not None and ev.get("outcome") == "none", "no hidden IC -> nothing to locate"


def test_locate_decker_with_no_evaded_decker_reports_clear(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.act("locate_decker", subsystem="index", decker_succ=3)
    ev = _last_event_of_type(flow.admin(), "enemy_decker")
    assert ev is not None and ev.get("outcome") == "scan_clear", (
        "Locate Decker with no evaded hostile reports a clear sweep")


# =============================================================================
# LEVEL 2 -- DATA BOMB CHAIN (depth-first). A key file is booby-trapped. From logged on:
#   Locate File -> Analyze Icon discovers the bomb -> Defuse (success disarms / botch detonates),
#   OR access it undefused: a successful Download trips the bomb; a failed Download does not.
# Bomb target is "files::<name>" so Analyze Icon, the access trigger, and Defuse all resolve it.
# =============================================================================
BOMB_ID, BOMB_NAME = "vault", "Vault"


def _bomb_host_cfg():
    return _host_cfg(
        paydata=[{"id": BOMB_ID, "name": BOMB_NAME, "density": 40, "is_key": True, "defense": 0}],
        data_bombs=[{"target": f"files::{BOMB_NAME}", "rating": 5}],
    )


def _raw_bombs(flow):
    return [b for b in (flow.run.state_json.get("data_bombs") or []) if isinstance(b, dict)]


def _detonated(state) -> bool:
    return any(e.get("type") == "data_bomb" and e.get("outcome") == "detonated"
               for e in (state.get("event_log") or []))


def _discover_bomb(monkeypatch):
    """Logged-on decker who has Located the file and Analyzed its Icon (bomb now discovered)."""
    flow = _logged_on(monkeypatch, _bomb_host_cfg())
    flow.act("locate_file", subsystem="index", decker_succ=3)          # Complex -> budget spent
    flow.act("analyze_icon", subsystem="control", target_file=f"files::{BOMB_NAME}", decker_succ=3)
    return flow


def test_analyze_icon_on_a_bombed_file_discovers_the_bomb(monkeypatch):
    flow = _discover_bomb(monkeypatch)
    assert flow.player().get("discovered_data_bombs"), "Analyze Icon must surface the armed data bomb"
    assert _last_event_of_type(flow.player(), "data_bomb_found") is not None, "a found event must fire"
    _assert_admin_superset(flow, "bomb discovered")


def test_defuse_success_disarms_the_bomb(monkeypatch):
    flow = _discover_bomb(monkeypatch)
    flow.new_turn()                                                    # refresh budget for Defuse
    flow.force_defuse(True).act("defuse_data_bomb", subsystem="files", target_file=BOMB_NAME)
    assert not _raw_bombs(flow), "a successful Defuse must remove the armed bomb"
    ev = _last_event_of_type(flow.player(), "data_bomb")
    assert ev is not None and ev.get("outcome") == "defused", "the Defuse must render as defused"
    assert not flow.player().get("discovered_data_bombs"), "the disarmed bomb leaves the player's list"


def test_defuse_botch_detonates_the_bomb(monkeypatch):
    flow = _discover_bomb(monkeypatch)
    flow.new_turn()
    flow.force_defuse(False, detonated=True).act(
        "defuse_data_bomb", subsystem="files", target_file=BOMB_NAME)
    assert _detonated(flow.player()), "an all-1s botched Defuse must detonate the bomb"
    assert not _raw_bombs(flow), "the detonated bomb is spent (one-shot)"


def test_download_a_bombed_file_without_defusing_detonates_it(monkeypatch):
    flow = _logged_on(monkeypatch, _bomb_host_cfg())
    flow.act("locate_file", subsystem="index", decker_succ=3).new_turn()
    flow.act("download_data", subsystem="files", target_file=BOMB_NAME, decker_succ=3)
    assert _located(flow.player(), BOMB_ID).get("downloaded") is True, (
        "the decker still GETS the file on a successful access...")
    assert _detonated(flow.player()), "...and the undefused bomb detonates on that access"
    assert not _raw_bombs(flow), "the access-tripped bomb is spent"


def test_failed_download_of_a_bombed_file_does_not_detonate(monkeypatch):
    flow = _logged_on(monkeypatch, _bomb_host_cfg())
    flow.act("locate_file", subsystem="index", decker_succ=3).new_turn()
    flow.act("download_data", subsystem="files", target_file=BOMB_NAME, decker_succ=0, host_succ=1)
    assert not _detonated(flow.player()), "a FAILED access must NOT trip the data bomb"
    assert _raw_bombs(flow), "the bomb stays armed after a failed access"


# =============================================================================
# LEVEL 2 -- CYBERCOMBAT (depth-first). From logged on, with an active IC on the host:
#   Attack -> wounds short of a crash / all resisted / 10+ boxes crashes it (tally += rating).
#   Crashing a TRAP IC springs its concealed hidden IC.
# =============================================================================
def _active_ic(flow, ic_id):
    for ic in (flow.run.state_json.get("active_ic") or []):
        if isinstance(ic, dict) and ic.get("id") == ic_id:
            return ic
    return None


def test_attack_ic_deals_damage_short_of_a_crash(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="ic1", rating=6)
    flow.force_attack(boxes=6).attack_ic("ic1")
    ic = _active_ic(flow, "ic1")
    assert ic["boxes"] == 6 and ic["status"] == "active", "6 boxes wounds the IC without crashing it"
    assert _last_event_of_type(flow.player(), "decker_attack") is not None, "a hit must render"


def test_attack_ic_that_resists_takes_no_damage(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="ic1", rating=6)
    flow.force_attack(boxes=0).attack_ic("ic1")
    assert _active_ic(flow, "ic1")["boxes"] == 0, "a fully resisted attack deals no boxes"
    assert _active_ic(flow, "ic1")["status"] == "active", "a resisted IC is still up"


def test_attack_ic_crash_bumps_the_tally_by_its_rating(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="ic1", rating=6)
    tally_before = flow.admin().get("security_tally", 0)
    flow.force_attack(boxes=10).attack_ic("ic1")            # 10 boxes -> crash
    assert _active_ic(flow, "ic1")["status"] == "crashed", "10+ boxes crashes the IC"
    ev = _last_event_of_type(flow.admin(), "ic_crashed")
    assert ev is not None and ev.get("tally_increase") == 6, "a crash adds the IC's rating to the tally"
    assert flow.admin().get("security_tally", 0) == tally_before + 6, "the tally must actually rise"


def test_crashing_a_trap_ic_springs_the_hidden_ic(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="trap1", rating=6, trap_hidden={"type": "Blaster", "rating": 6})
    before = len(flow.run.state_json.get("active_ic") or [])
    flow.force_attack(boxes=10).attack_ic("trap1")
    assert _active_ic(flow, "trap1")["status"] == "crashed", "the trap IC itself crashes"
    assert len(flow.run.state_json.get("active_ic") or []) == before + 1, "the hidden IC is spawned"
    ev = _last_event_of_type(flow.admin(), "ic_activation")
    assert ev is not None and ev.get("is_trap_reveal") is True, "the spring must render as a trap reveal"


# -- Crash a Scramble IC in combat (instead of Decrypting it) --
def _poison_node_cfg():
    return _host_cfg(
        paydata=[{"id": "f1", "name": "File", "density": 40, "is_key": True, "defense": 0}],
        scrambles=[{"target_key": "files::entire", "rating": 6, "variant": "poison"}])


def test_crash_a_poison_scramble_in_combat(monkeypatch):
    flow = _logged_on(monkeypatch, _poison_node_cfg())
    flow.act("analyze_subsystem", subsystem="files", decker_succ=3)     # discover the node Scramble
    flow.crash_scramble("files::entire", boxes=10)
    assert not _any_scramble_present(flow), "crashing the Scramble removes it"
    ev = _last_event_of_type(flow.admin(), "scramble_crashed")
    assert ev is not None and ev.get("tally_increase") == 6, "crashing a Scramble adds its rating to the tally"


def test_attack_a_poison_scramble_without_crashing_it(monkeypatch):
    flow = _logged_on(monkeypatch, _poison_node_cfg())
    flow.act("analyze_subsystem", subsystem="files", decker_succ=3)
    flow.crash_scramble("files::entire", boxes=6)                       # 6 < 10 -> not crashed
    assert _any_scramble_present(flow), "a non-crashing attack leaves the Scramble up"
    ev = _last_event_of_type(flow.player(), "scramble_attack")
    assert ev is not None and ev.get("boxes") == 6, "the partial hit renders its boxes"


def test_crash_an_exploding_scramble_detonates_its_bomb(monkeypatch):
    flow = _logged_on(monkeypatch, _exploding_host_cfg())
    flow.act("locate_file", subsystem="index", decker_succ=3)
    flow.act("analyze_icon", subsystem="control", target_file=f"files::{EXP_ID}", decker_succ=3)
    flow.new_turn()
    flow.crash_scramble(_only_scramble_key(flow), boxes=10)
    assert _detonated(flow.player()), "crashing an undefused Exploding Scramble detonates its bomb"


# -- Combat maneuvers: Evade Detection / Parry / Position Attack --
def test_evade_detection_success_hides_from_the_ic(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="ic1", rating=6)
    flow.force_maneuver(won=True, net=2).act("evade_detection", subsystem="control", maneuver_target="ic1")
    assert _active_ic(flow, "ic1").get("evaded") is True, "a won Evade hides the PC from that IC"


def test_evade_detection_failure_stays_tracked(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="ic1", rating=6)
    flow.force_maneuver(won=False).act("evade_detection", subsystem="control", maneuver_target="ic1")
    assert not _active_ic(flow, "ic1").get("evaded"), "a failed Evade leaves the IC tracking you"


def test_parry_attack_success_banks_a_parry_bonus(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="ic1", rating=6)
    flow.force_maneuver(won=True, net=2).act("parry_attack", subsystem="control", maneuver_target="ic1")
    assert (flow.run.state_json.get("pc_parry") or {}).get("bonus") == 2, "a won Parry banks a +TN penalty"


def test_position_attack_success_banks_a_power_advantage(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="ic1", rating=6)
    flow.force_maneuver(won=True, net=2).act("position_attack", subsystem="control",
                                             maneuver_target="ic1", position_choice="power")
    assert (flow.run.state_json.get("pc_position") or {}).get("power_bonus") == 2, (
        "a won Position (power) banks a Power bonus for the next attack")


# -- Steamroller: the dedicated anti-tar weapon (vs lurking Tar Baby / Tar Pit IC) --
def _inject_lurking_ic(flow, ic_type="Tar Baby", rating=6, ic_id="tar1", **extra):
    ic = {"id": ic_id, "type": ic_type, "rating": rating, "status": "lurking", "boxes": 0}
    ic.update(extra)
    flow.run.state_json.setdefault("lurking_ic", []).append(ic)
    return ic


def test_steamroller_crashes_a_tar_ic(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_lurking_ic(flow, ic_type="Tar Baby", ic_id="tar1")
    flow.force_steamroller(crashed=True).act("steamroller", subsystem="control", target_ic_id="tar1")
    assert not any(ic.get("id") == "tar1" for ic in flow.run.state_json.get("lurking_ic") or []), (
        "a Steamroller crash removes the tar IC")
    ev = _last_event_of_type(flow.player(), "tar_steamrolled")
    assert ev is not None and ev.get("destroyed") is True, "the crash must render as destroyed"


def test_steamroller_hit_short_of_a_crash_wounds_the_tar(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_lurking_ic(flow, ic_type="Tar Baby", ic_id="tar1")
    flow.force_steamroller(crashed=False, boxes=6).act("steamroller", subsystem="control", target_ic_id="tar1")
    assert any(ic.get("id") == "tar1" for ic in flow.run.state_json.get("lurking_ic") or []), (
        "a non-crashing Steamroller strike leaves the tar lurking")
    ev = _last_event_of_type(flow.admin(), "tar_steamrolled")
    assert ev is not None and ev.get("destroyed") is False


def test_steamroller_on_a_non_tar_ic_is_refused(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_lurking_ic(flow, ic_type="Killer", ic_id="k1")   # lurking, but not a tar
    with pytest.raises(HTTPException) as ei:
        _LOOP.run_until_complete(mr.perform_action(
            run_id=1, body=RunActionInput(action_type="steamroller", subsystem="control",
                                          utility_rating=6, hacking_pool_dice=0, target_ic_id="k1"),
            auth=AUTH_ADMIN, db=_FakeDB()))
    assert ei.value.status_code == 400, "Steamroller can only target tar IC"


# -- Slow: reduce a proactive IC's action economy (hang it) --
def test_slow_hangs_a_proactive_ic(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="k1", ic_type="Killer", rating=6)
    flow.force_slow(won=True).act("slow", subsystem="control", target_ic_id="k1")
    assert _active_ic(flow, "k1").get("actions_lost", 0) >= 1, "a won Slow strips the IC's actions"
    ev = _last_event_of_type(flow.player(), "ic_slowed")
    assert ev is not None and ev.get("outcome") in ("hung", "slowed"), "the Slow must render its result"


def test_slow_with_no_eligible_ic_reports_no_target(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.force_slow(won=True).act("slow", subsystem="control")
    ev = _last_event_of_type(flow.player(), "ic_slowed")
    assert ev is not None and ev.get("outcome") == "no_target", "no eligible IC -> no target"


# -- Suppress / Release: the Detection-Factor ledger for a fresh crash --
def test_suppress_a_crashed_ic_refunds_its_tally(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="ic1", rating=6)
    flow.force_attack(boxes=10).attack_ic("ic1")     # crash -> tally += 6 (suppression pending)
    crashed_tally = flow.admin().get("security_tally", 0)
    flow.suppress("ic1", release=False)              # absorb 1 DF to refund the crash tally
    assert flow.admin().get("security_tally", 0) < crashed_tally, "suppressing refunds the crash tally"


def test_release_a_suppressed_crash_readds_the_tally(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="ic1", rating=6)
    flow.force_attack(boxes=10).attack_ic("ic1")
    flow.suppress("ic1", release=False)
    low = flow.admin().get("security_tally", 0)
    flow.suppress("ic1", release=True)               # release -> re-add the crashed IC's tally
    assert flow.admin().get("security_tally", 0) > low, "releasing re-adds the crashed IC's tally"


# =============================================================================
# LEVEL 3 -- ACCESS / MOVEMENT: leave the host (Graceful Logoff / emergency Jack Out) or dive
# deeper (enter a discovered Trap Door -> the host is suspended on the run's stack).
# =============================================================================
def _inject_trap_door(flow, td_id="td1", destination_host_id=1, discovered=True, subsystem="access"):
    door = {"id": td_id, "source_piece": "maglock", "subsystem": subsystem,
            "destination_host_id": destination_host_id, "destination_ltg": "",
            "destination_label": "??", "discovered": discovered}
    flow.run.state_json.setdefault("trap_doors", []).append(door)
    return door


def test_graceful_logoff_success_ends_the_run_escaped(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.logoff(decker_succ=3, host_succ=0)
    assert flow.run.status == "escaped", "a successful Graceful Logoff ends the run (escaped)"
    assert _last_event_of_type(flow.player(), "logoff_success") is not None, "success must render"


def test_graceful_logoff_failure_keeps_the_decker_on_the_host(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.logoff(decker_succ=0, host_succ=1)
    assert flow.run.status == "active", "a failed Graceful Logoff leaves the decker on the host"
    assert _last_event_of_type(flow.player(), "logoff_fail") is not None, "failure must render"


def test_jack_out_ends_the_run_escaped(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.jack_out()
    assert flow.run.status == "escaped", "an emergency Jack Out (no Black IC) ends the run"
    assert _last_event_of_type(flow.player(), "jack_out") is not None, "the jack-out must render"


def test_enter_a_discovered_trap_door_suspends_the_current_host(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_trap_door(flow, td_id="td1", destination_host_id=1)
    depth_before = len(flow.run.state_json.get("host_stack") or [])
    flow.enter_trap_door("td1", decker_succ=3)
    assert len(flow.run.state_json.get("host_stack") or []) == depth_before + 1, (
        "entering a trap door suspends the parent host onto the run's stack")
    assert _last_event_of_type(flow.admin(), "trap_door_entered") is not None, "the transit must render"


def test_enter_trap_door_aborts_when_the_logoff_fails(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_trap_door(flow, td_id="td1", destination_host_id=1)
    flow.enter_trap_door("td1", decker_succ=0, host_succ=1)
    assert not (flow.run.state_json.get("host_stack") or []), (
        "a failed logoff aborts the transit -- still on the current host")


def test_enter_an_undiscovered_trap_door_is_refused(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_trap_door(flow, td_id="td1", destination_host_id=1, discovered=False)
    with pytest.raises(HTTPException) as ei:
        _LOOP.run_until_complete(mr.trap_door_action(
            run_id=1, td_id="td1", body=RunTrapDoorInput(action="enter"),
            auth=AUTH_ADMIN, db=_FakeDB()))
    assert ei.value.status_code == 400 and "discovered" in str(ei.value.detail).lower(), (
        "an undiscovered trap door cannot be entered")


# =============================================================================
# LEVEL 4 -- HOSTILE DECKERS: strike back at / scan a revealed enemy decker.
# =============================================================================
def _inject_enemy_decker(flow, enemy_id="ed1", **over):
    e = {"id": enemy_id, "name": "Ripper", "status": "active", "revealed": True,
         "mpcp": 6, "bod": 6, "evasion": 6, "masking": 6, "sensor": 6, "boxes": 0,
         "utilities": {"sleaze": 0}, "scan_reveal": 0}
    e.update(over)
    flow.run.state_json.setdefault("enemy_deckers", []).append(e)
    return e


def _enemy(flow, enemy_id):
    for e in flow.run.state_json.get("enemy_deckers") or []:
        if isinstance(e, dict) and e.get("id") == enemy_id:
            return e
    return {}


def test_attack_an_enemy_decker_crashes_its_icon(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_enemy_decker(flow, enemy_id="ed1")
    flow.attack_enemy("ed1", boxes=10)
    assert _enemy(flow, "ed1").get("status") == "crashed", "crashing an enemy decker's icon dumps it"


def test_attack_an_enemy_decker_that_resists_survives(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_enemy_decker(flow, enemy_id="ed1")
    flow.attack_enemy("ed1", boxes=0)
    assert _enemy(flow, "ed1").get("status") == "active", "a fully resisted strike leaves the icon up"


def test_scan_an_enemy_decker_reveals_its_ratings(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_enemy_decker(flow, enemy_id="ed1")
    flow.scan_enemy("ed1", successes=3)
    assert _enemy(flow, "ed1").get("scan_reveal", 0) >= 1, "a successful Scan reveals hidden ratings"
    ev = _last_event_of_type(flow.admin(), "icon_scanned")
    assert ev is not None and ev.get("success") is True, "the scan must render as a reveal"


# =============================================================================
# LEVEL 4 -- DECK / PROGRAM MANAGEMENT: Medic (heal the icon).
# =============================================================================
def test_medic_on_an_undamaged_icon_heals_nothing(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.act("medic", subsystem="control")
    ev = _last_event_of_type(flow.player(), "medic_heal")
    assert ev is not None and ev.get("healed") == 0, "an undamaged icon has nothing to heal"


def test_medic_heals_persona_damage(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.run.state_json.setdefault("condition_monitor", {})["persona_boxes"] = 5
    flow.force_roll(3).act("medic", subsystem="control")
    ev = _last_event_of_type(flow.player(), "medic_heal")
    assert ev is not None and ev.get("healed", 0) >= 1, "Medic heals persona boxes on a successful test"


def test_restore_with_no_damage_repairs_nothing(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.act("restore", subsystem="control")
    ev = _last_event_of_type(flow.player(), "restore_repair")
    assert ev is not None and ev.get("repaired") == 0, "no temporary attribute damage -> nothing to repair"


def test_restore_repairs_a_crippled_attribute(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.run.state_json.setdefault("condition_monitor", {})["persona_damage"] = {"bod": 3}
    flow.force_roll(4).act("restore", subsystem="control", target_program="bod")
    ev = _last_event_of_type(flow.player(), "restore_repair")
    assert ev is not None and ev.get("repaired", 0) >= 1, "Restore repairs temporary attribute damage"


def test_disinfect_destroys_a_worm(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_lurking_ic(flow, ic_type="Worm", ic_id="w1", subsystem="files")
    flow.force_disinfect(destroyed=True).act("disinfect", subsystem="files", target_ic_id="w1")
    assert not any(ic.get("id") == "w1" for ic in flow.run.state_json.get("lurking_ic") or []), (
        "a successful Disinfect removes the worm")
    ev = _last_event_of_type(flow.player(), "worm_disinfected")
    assert ev is not None and ev.get("destroyed") is True


def test_disinfect_a_clean_subsystem_finds_no_worm(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.force_disinfect(destroyed=False).act("disinfect", subsystem="files")
    ev = _last_event_of_type(flow.player(), "worm_disinfected")
    assert ev is not None and ev.get("destroyed") is False, "a clean subsystem finds no worm"


# -- Swap Memory / Unload Program: no-test active-memory bookkeeping --
def test_swap_memory_resolves_and_logs(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.act("swap_memory", subsystem="control", target_program="sleaze")
    assert _last_event_of_type(flow.player(), "swap_memory") is not None, "Swap Memory logs its result"


def test_unload_program_frees_active_memory(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.act("unload_program", subsystem="control", target_program="analyze")
    assert _last_event_of_type(flow.player(), "swap_memory") is not None, "Unload Program logs a swap event"


# -- Purge Hog: remove an offensive-virus infection --
def test_purge_hog_removes_the_infection(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.run.state_json["hog_infections"] = [{"id": "h1", "target_id": "pc", "rating": 4}]
    flow.force_purge_hog(True).act("purge_hog", subsystem="control", target_program="h1")
    assert not (flow.run.state_json.get("hog_infections") or []), "a successful purge removes the Hog"
    assert _last_event_of_type(flow.player(), "purge_hog") is not None, "the purge must render"


def test_purge_hog_with_no_infection_is_a_clean_noop(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.act("purge_hog", subsystem="control")
    ev = _last_event_of_type(flow.player(), "purge_hog")
    assert ev is not None and "No Hog" in (ev.get("description") or ""), "no Hog -> clean no-op"


# -- DINAB: run one program autonomously for the Free action --
def test_dinab_runs_an_operational_program_autonomously(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.run.decker_json.setdefault("program_options", {})["analyze"] = {"dinab": 6}
    flow.act("dinab", subsystem="control", target_program="analyze", decker_succ=3)
    ev = _last_event_of_type(flow.player(), "dinab_op")
    assert ev is not None and ev.get("success") is True, "DINAB runs an operational program autonomously"


def test_dinab_without_a_dinab_equipped_program_is_refused(monkeypatch):
    flow = _logged_on(monkeypatch)
    with pytest.raises(HTTPException) as ei:
        _LOOP.run_until_complete(mr.perform_action(
            run_id=1, body=RunActionInput(action_type="dinab", subsystem="control",
                                          utility_rating=6, hacking_pool_dice=0, target_program="analyze"),
            auth=AUTH_ADMIN, db=_FakeDB()))
    assert ei.value.status_code == 400, "DINAB needs a DINAB-equipped program"


# -- Area Attack: one burst against a cluster (needs the Attack utility's Area option) --
def test_area_attack_crashes_a_cluster_of_ic(monkeypatch):
    flow = _logged_on(monkeypatch)
    flow.run.decker_json.setdefault("program_options", {})["attack"] = {"area": 4}
    _inject_ic(flow, ic_id="a", rating=6)
    _inject_ic(flow, ic_id="b", rating=6)
    flow.area_attack(["a", "b"], boxes=10)
    assert _active_ic(flow, "a")["status"] == "crashed" and _active_ic(flow, "b")["status"] == "crashed", (
        "an Area burst crashes each target in the cluster")


def test_area_attack_without_the_area_option_is_refused(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="a", rating=6)
    with pytest.raises(HTTPException) as ei:
        _LOOP.run_until_complete(mr.area_attack(
            run_id=1, body=RunAreaAttackInput(target_ids=["a"]), auth=AUTH_ADMIN, db=_FakeDB()))
    assert ei.value.status_code == 400, "Area Attack needs the Attack utility's Area option"


# -- Locate Decker: re-acquire an EVADED hostile decker (the re-acquire branch) --
def test_locate_decker_reacquires_an_evaded_decker(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_enemy_decker(flow, enemy_id="ed1", evaded=True, evade_dir="hid_from_pc")
    flow.force_locate_decker(True).act("locate_decker", subsystem="index", decker_succ=3)
    ev = _last_event_of_type(flow.admin(), "enemy_decker")
    assert ev is not None and ev.get("outcome") == "scan_hit", "a won opposed test re-acquires the decker"


def test_locate_decker_index_failure_cannot_reacquire(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_enemy_decker(flow, enemy_id="ed1", evaded=True, evade_dir="hid_from_pc")
    flow.act("locate_decker", subsystem="index", decker_succ=0, host_succ=1)
    ev = _last_event_of_type(flow.admin(), "enemy_decker")
    assert ev is not None and ev.get("outcome") == "scan_fail", "a failed Index test cannot re-acquire"


# =============================================================================
# LEVEL 4 -- COMBAT GUARD BRANCHES + interactive defense.
# =============================================================================
def test_attack_while_your_icon_is_crashed_is_refused(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="ic1", rating=6)
    flow.run.state_json["icon_crashed"] = True
    with pytest.raises(HTTPException) as ei:
        _LOOP.run_until_complete(mr.attack_ic(
            run_id=1, body=RunAttackInput(target_ic_id="ic1"), auth=AUTH_ADMIN, db=_FakeDB()))
    assert ei.value.status_code == 400, "a Black-IC-crashed icon can only jack out"


def test_attack_a_trace_ic_in_its_locate_cycle_is_refused(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="tr1", ic_type="Trace", rating=6, trace_phase="locate")
    with pytest.raises(HTTPException) as ei:
        _LOOP.run_until_complete(mr.attack_ic(
            run_id=1, body=RunAttackInput(target_ic_id="tr1"), auth=AUTH_ADMIN, db=_FakeDB()))
    assert ei.value.status_code == 400, "a trace IC vanished into its location cycle can't be attacked"


def test_defend_with_no_pending_strike_is_refused(monkeypatch):
    flow = _logged_on(monkeypatch)
    with pytest.raises(HTTPException) as ei:
        _LOOP.run_until_complete(mr.defend(
            run_id=1, body=RunDefendInput(hacking_pool_dice=0), auth=AUTH_ADMIN, db=_FakeDB()))
    assert ei.value.status_code == 400, "no defense pending -> refused"


def test_defend_resolves_a_pending_ic_strike(monkeypatch):
    flow = _logged_on(monkeypatch)
    _inject_ic(flow, ic_id="ic1", rating=4)
    flow.run.state_json["pending_defense"] = {
        "ic_id": "ic1",
        "to_hit_roll": {"pool": 4, "tn": 4, "dice": [4, 4], "successes": 2, "ones": 0},
        "ctx": {"ic_attack_pool": 4, "ic_target_status": "intruding", "ic_category": "white",
                "sec_code": "Green", "sec_value": 4, "atk_power_delta": 0, "atk_tn_delta": 0,
                "cluster_penalty": 0, "effect_type": None, "effect_rating": None},
        "acting_init": 20, "acting_count": None,
    }
    flow.defend(hacking_pool_dice=0)
    assert flow.run.state_json.get("pending_defense") is None, (
        "resolving the parked strike clears the pending-defense prompt")
