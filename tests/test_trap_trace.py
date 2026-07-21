"""Trap IC + Trace IC completion effects -- run-engine coverage (Tier 3).

Validates the RAW Trace / Trap behaviour wired into app.routers.matrix_runs:

  * Trace "Effects on Completion" (vr2_rules.md L588-591): finishing a Location
    Cycle records the completion in ``state['traces_completed']``, which then
    (a) lowers every PROACTIVE IC's Attack-Test target number by 1 and
    (b) accelerates every later security-tally increase by +1 -- per completed
    Trace, cumulatively. (Recording the jackpoint address is narrative only.)

  * Trap IC (vr2_rules.md L686-692): a white/gray Trap IC crashed in cybercombat
    springs its hidden IC; a Trap TRACE crashed during its hunt cycle is DEFUSED
    (its hidden IC never triggers), and the hidden IC instead springs only when the
    Location Cycle completes successfully.

  * ``_bump_security_tally`` is the single choke point that applies the
    +1-per-completed-Trace acceleration to genuine tally INCREASES (never to
    refunds), so the acceleration can never be silently skipped.

These drive the real helpers / the real ``_advance_npc_pass`` app-as-GM loop
(no per-test rules re-implementation).
"""
from __future__ import annotations

import pytest

from app.services import matrix_engine as eng
from app.routers import matrix_runs as mr


class _RunStub:
    status = "active"


def _crash_state():
    """Minimal state for the crash-resolution helpers (tally + sheaf + event log)."""
    return {
        "security_tally": 0, "alert_status": "none",
        "active_ic": [], "lurking_ic": [], "sheaf": [],
        "host_security_code": "Green", "host_security_value": 6,
        "host_acifs": [8, 10, 9, 9, 8], "current_turn": 1, "event_log": [],
    }


def _npc_state(sec="Green", sv=6):
    """Minimal PC-side state for the ``_advance_npc_pass`` app-as-GM loop."""
    return {
        "host_security_code": sec, "host_security_value": sv,
        "current_pass": 1, "security_tally": 0,
        "active_ic": [], "enemy_deckers": [], "event_log": [], "sheaf": [],
        "has_legitimate_status": True,
        "condition_monitor": {"persona_boxes": 0, "physical_boxes": 0, "stun_boxes": 0,
                              "mpcp_damage": 0,
                              "persona_damage": {"bod": 0, "evasion": 0, "masking": 0, "sensor": 0}},
        "program_damage": {},
    }


def _pc_decker(deck_mode="cool"):
    # cool deck keeps a gray Killer off the hot-deck-only simsense branch.
    return {"bod": 6, "evasion": 6, "masking": 6, "sensor": 6, "mpcp": 6,
            "intelligence": 5, "body": 5, "willpower": 4, "hardening": 0,
            "deck_mode": deck_mode, "computer_skill": 6, "utilities": {"armor": 0}}


# -- _completed_trace_count + _bump_security_tally (unit) -----------------------

class TestTallyAcceleration:
    """vr2 Trace 'Tally acceleration' (L591): each completed Trace adds +1 to every SUBSEQUENT
    tally increase. The counter floors at 0 and refunds are never accelerated."""

    def test_completed_trace_count_reads_and_floors(self):
        assert mr._completed_trace_count({}) == 0
        assert mr._completed_trace_count({"traces_completed": 3}) == 3
        assert mr._completed_trace_count({"traces_completed": None}) == 0
        assert mr._completed_trace_count({"traces_completed": -2}) == 0

    def test_no_completed_trace_adds_base(self):
        st = _crash_state()
        applied = mr._bump_security_tally(st, 4)
        assert applied == 4 and st["security_tally"] == 4

    def test_positive_increase_is_accelerated(self):
        st = _crash_state(); st["traces_completed"] = 2
        applied = mr._bump_security_tally(st, 3)          # 3 + 2 completed traces
        assert applied == 5 and st["security_tally"] == 5

    def test_refund_is_not_accelerated(self):
        st = _crash_state(); st["security_tally"] = 6; st["traces_completed"] = 2
        applied = mr._bump_security_tally(st, -4)         # a decrease passes through untouched
        assert applied == -4 and st["security_tally"] == 2

    def test_tally_floors_at_zero(self):
        st = _crash_state(); st["security_tally"] = 1; st["traces_completed"] = 5
        mr._bump_security_tally(st, -9)
        assert st["security_tally"] == 0


# -- Trap IC: reveal-on-crash vs defuse-on-crash --------------------------------

class TestTrapCrashResolution:
    """vr2 Trap IC (L686-692): a white/gray Trap IC crashed in cybercombat springs its hidden IC;
    a Trap TRACE crashed during its hunt cycle is DEFUSED instead. ``_apply_ic_crash`` is the shared
    Attack/Area crash resolver, so both call sites inherit this."""

    def test_white_trap_springs_hidden_ic_on_crash(self):
        state = _crash_state()
        ic = {"id": "k1", "type": "Killer", "rating": 6, "status": "active",
              "trap_hidden": {"type": "Blaster", "rating": 6}}
        state["active_ic"] = [ic]
        mr._apply_ic_crash(state, ic, "Green", 0)
        assert ic["status"] == "crashed"
        hidden = [i for i in state["active_ic"] if i["type"] == "Blaster"]
        assert hidden and hidden[0]["status"] == "active"
        assert any(e.get("is_trap_reveal") for e in state["event_log"])

    def test_trap_trace_crashed_in_cybercombat_is_defused(self):
        state = _crash_state()
        ic = {"id": "tr1", "type": "Trace", "rating": 6, "status": "active",
              "trap_hidden": {"type": "Killer", "rating": 6}}
        state["active_ic"] = [ic]
        mr._apply_ic_crash(state, ic, "Green", 0)
        assert ic["status"] == "crashed"
        # Defused: the hidden IC never spawns and no trap-reveal event fires.
        assert all(i["id"] == "tr1" for i in state["active_ic"])
        assert not any(e.get("is_trap_reveal") for e in state["event_log"])

    def test_completed_trace_accelerates_crash_tally(self):
        state = _crash_state(); state["traces_completed"] = 1
        ic = {"id": "k1", "type": "Killer", "rating": 6, "status": "active"}
        state["active_ic"] = [ic]
        mr._apply_ic_crash(state, ic, "Green", 0)         # base +6, +1 acceleration -> +7
        assert state["security_tally"] == 7
        ev = [e for e in state["event_log"] if e["type"] == "ic_crashed"][-1]
        assert ev["tally_increase"] == 7


# -- Trace cycle: hunt -> locate -> completion (via the real app-as-GM loop) ----

class TestTraceCycle:
    """vr2 Trace IC (L560-591): a Hunt-Cycle hit opens the Location Cycle; when the cycle counts out
    the trace COMPLETES -- recorded in ``state['traces_completed']`` with a 'report' event. A Trap
    Trace springs its hidden IC on completion (only)."""

    def _drive_once(self, state, decker=None):
        decker = decker or _pc_decker()
        eff = mr._get_decker_effective(decker, state)
        mr._advance_npc_pass(state, decker, _RunStub(), eff=eff,
                             sec_code="Green", sec_value=6, det_factor=4)

    def test_hunt_hit_opens_location_cycle(self, monkeypatch):
        monkeypatch.setattr(eng, "trace_hunt_cycle_attack",
                            lambda sv, tn: {"hit": True, "roll": {"successes": 2}})
        state = _npc_state()
        state["active_ic"] = [{"id": "tr1", "type": "Trace", "rating": 5, "status": "active",
                               "initiative": 10, "trace_phase": "hunt"}]
        self._drive_once(state)
        ic = state["active_ic"][0]
        assert ic["trace_phase"] == "locate"
        assert ic["trace_locate_remaining"] == max(1, 10 // 2)   # 5 turns to trace
        assert state.get("traces_completed", 0) == 0             # not complete yet

    def test_location_cycle_completion_records_trace(self):
        state = _npc_state()
        state["active_ic"] = [{"id": "tr1", "type": "Trace", "rating": 5, "status": "active",
                               "initiative": 10, "trace_phase": "locate",
                               "trace_locate_remaining": 1}]
        self._drive_once(state)
        ic = state["active_ic"][0]
        assert ic["trace_phase"] == "triggered" and ic["status"] == "triggered"
        assert state["traces_completed"] == 1
        rep = [e for e in state["event_log"] if e.get("trace_action") == "report"]
        assert rep and rep[-1]["traces_completed"] == 1
        assert len(state["active_ic"]) == 1                      # plain trace: no hidden IC

    def test_trap_trace_springs_hidden_ic_on_completion(self):
        state = _npc_state()
        state["active_ic"] = [{"id": "tr1", "type": "Trace", "rating": 5, "status": "active",
                               "initiative": 10, "trace_phase": "locate",
                               "trace_locate_remaining": 1,
                               "trap_hidden": {"type": "Killer", "rating": 6}}]
        self._drive_once(state)
        assert state["traces_completed"] == 1
        hidden = [ic for ic in state["active_ic"] if ic["type"] == "Killer"]
        assert hidden, "a Trap Trace must spring its hidden IC when the Location Cycle completes"
        assert any(e.get("is_trap_reveal") for e in state["event_log"])


# -- Trace completion: -1 to every proactive IC to-hit --------------------------

class TestProactiveIcToHitBonus:
    """vr2 Trace 'IC-targeting bonus' (L590): a completed Trace lowers every proactive IC's
    Attack-Test target number by 1. The three proactive attack sites all feed the engine core the
    same ``tn_modifier - _completed_trace_count(state)``; this captures the standard cybercombat
    site to prove the wiring (each completed Trace subtracts exactly 1)."""

    _CANNED = {"attack_roll": {"successes": 0, "ones": 0},
               "resistance": {"final_damage_level": "None", "boxes": 0,
                              "resist_roll": {"successes": 0}}}

    def _capture_tn_modifier(self, monkeypatch, traces_completed):
        captured = {}

        def _spy(**kw):
            captured.update(kw)
            return self._CANNED

        monkeypatch.setattr(eng, "cybercombat_attack", _spy)
        state = _npc_state()
        state["traces_completed"] = traces_completed
        state["active_ic"] = [{"id": "k1", "type": "Killer", "rating": 6, "status": "active",
                               "initiative": 10}]
        decker = _pc_decker(deck_mode="cool")
        eff = mr._get_decker_effective(decker, state)
        mr._advance_npc_pass(state, decker, _RunStub(), eff=eff,
                             sec_code="Green", sec_value=6, det_factor=4)
        return captured["tn_modifier"]

    def test_each_completed_trace_lowers_ic_to_hit_by_one(self, monkeypatch):
        base = self._capture_tn_modifier(monkeypatch, traces_completed=0)
        with_two = self._capture_tn_modifier(monkeypatch, traces_completed=2)
        assert with_two == base - 2


# -- Simsense overload: hot-deck == pure-DNI wiring -----------------------------

class TestSimsenseHotDniWiring:
    """vr2 Simsense Overload: a hot deck taking white/gray IC damage rolls Willpower vs a TN that
    RISES +2 for a pure-DNI interface. This app has no manual-controls axis, so a hot deck IS pure
    DNI -- the same convention behind the +1D6 hot-DNI initiative die -- so ``_advance_npc_pass``
    must pass ``hot_dnil_only=True`` to eng.simsense_check. Cool / tortoise decks are immune and
    never reach the branch. Spies on the engine primitive to prove the run-loop wiring."""

    _HIT = {"attack_roll": {"successes": 2, "ones": 0},
            "resistance": {"final_damage_level": "Moderate", "boxes": 3,
                           "resist_roll": {"successes": 1}}}

    def _capture_simsense(self, monkeypatch, deck_mode):
        captured = {}

        def _sim_spy(**kw):
            captured.update(kw)
            return {"immune": False, "tn": 5, "stun_taken": False, "roll": {"successes": 1}}

        # A gray Killer lands a fixed Moderate hit; spy on the simsense primitive it feeds.
        monkeypatch.setattr(eng, "cybercombat_attack", lambda **kw: self._HIT)
        monkeypatch.setattr(eng, "simsense_check", _sim_spy)
        state = _npc_state()
        state["active_ic"] = [{"id": "k1", "type": "Killer", "rating": 6, "status": "active",
                               "initiative": 10}]
        decker = _pc_decker(deck_mode=deck_mode)
        eff = mr._get_decker_effective(decker, state)
        mr._advance_npc_pass(state, decker, _RunStub(), eff=eff,
                             sec_code="Green", sec_value=6, det_factor=4)
        return captured

    def test_hot_deck_passes_pure_dni_flag(self, monkeypatch):
        cap = self._capture_simsense(monkeypatch, deck_mode="hot")
        assert cap.get("hot_dnil_only") is True          # hot == pure DNI in this app
        assert cap.get("deck_mode") == "hot"
        assert cap.get("damage_level") == "Moderate"     # from the gray Killer's hit

    def test_cool_deck_never_reaches_simsense(self, monkeypatch):
        cap = self._capture_simsense(monkeypatch, deck_mode="cool")
        assert cap == {}                                 # guard skips the call entirely
