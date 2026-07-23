"""VR2 Matrix reconciliation contract -- the machine-checked proof harness.

This test enforces, for every buildable program / option / IC / host mechanic enumerated
in ``tests/matrix_scope_ledger.py``, the five reconciliation requirements:

  (1) PRESENT   -- it exists in the schema / catalog (bijection with the builder + schema).
  (2) REACHABLE -- it has a run-UI config field AND an invoke control (or is a documented
                   backend-only action / open UI gap).
  (3) CORRECT   -- its shared resolver is numerically proven in success AND failure
                   (delegated to test_matrix_numeric_oracle via COVERED_PRIMITIVES).
  (4) ONE SEAM  -- multi-actor mechanics resolve through a single engine primitive; every
                   known exception is a pinned, non-drifting DIVERGENCE.
  (5) GUARDED   -- a new builder entry cannot appear without a ledger row (or an exclusion),
                   and cannot skip the numeric gate.

It deliberately BUILDS ON the existing ``tests/test_coverage_matrix.py`` schema-derived
registries (ACTIONS / UTILITIES / OPTIONS / IC_TYPES) rather than re-deriving them, so the
two contracts cannot silently disagree.

Static frontend checks are literal-token / parsed-catalog searches against the shipped
``frontend/*.html`` (no browser). Numeric correctness is executed in-process by the oracle.
"""

from __future__ import annotations

import inspect
import re
import typing
from pathlib import Path

import app.schemas.matrix_run as schemas
import app.services.matrix_engine as eng
import app.services.matrix_rules as rules
import app.routers.matrix_runs as mr
from app.schemas.matrix_run import ActionType, DeckerUtilities, ProgramOptions

from tests.matrix_scope_ledger import (
    PROGRAMS, OPTIONS, IC, HOST_MECHANICS, EXCLUSIONS, DIVERGENCES,
    UI_REACHABILITY_GAPS,
    all_program_slots, carried_option_fields, toggle_option_keys, active_programs,
    open_divergences, open_ui_gaps,
)
from tests.test_matrix_numeric_oracle import COVERED_PRIMITIVES, PASSIVE_COVERED
from tests.test_coverage_matrix import (
    ACTIONS as COV_ACTIONS, UTILITIES as COV_UTILITIES,
    OPTIONS as COV_OPTIONS, IC_TYPES as COV_IC_TYPES,
)


# --------------------------------------------------------------------------- fixtures
ROOT = Path(__file__).resolve().parents[1]
RUN_UI = (ROOT / "frontend" / "matrix-run.html").read_text(encoding="utf-8")
WORKSHOP = (ROOT / "frontend" / "deck-workshop.html").read_text(encoding="utf-8")
PROGRAM_CATALOG = (ROOT / "frontend" / "matrix-programs.js").read_text(encoding="utf-8")
DESIGNER = (ROOT / "frontend" / "matrix-designer.html").read_text(encoding="utf-8")

ACTION_TYPES = set(typing.get_args(ActionType))


def _js_array(text: str, name: str) -> str:
    """Return the source of the JS array literal ``name = [ ... ]`` (up to the first ``];``)."""
    m = re.search(name + r"\s*=\s*\[", text)
    assert m, f"{name} array literal not found"
    start = m.end() - 1
    end = text.index("];", start)
    return text[start:end]


#: Action keys reachable through the run console (ACTION_CATALOG ``{ v: 'key', ... }``).
CONSOLE_ACTIONS = set(re.findall(r"\bv:\s*'([a-z0-9_]+)'", _js_array(RUN_UI, "ACTION_CATALOG")))
#: Program display names and option ids from the canonical shared catalog.
WORKSHOP_PROGRAMS = set(re.findall(r"display:\s*'([^']+)'", _js_array(PROGRAM_CATALOG, "PROGRAMS")))
WORKSHOP_OPTIONS = set(re.findall(r"id:\s*'([^']+)'", _js_array(PROGRAM_CATALOG, "OPTION_DEFS")))

#: Actions reachable via a dedicated (non-console) run control -> the token that proves it.
DEDICATED_CONTROLS = {
    "logon_to_host": "doLogon",     # >> Log On to Host button + doLogon()
    "graceful_logoff": "/logoff",   # logoff modal POSTs /logoff
}

#: Multi-actor mechanics that MUST resolve through a single shared engine primitive (req 4).
SHARED_SEAM_PRIMITIVES = (
    "cybercombat_attack", "black_attack", "attribute_attack_core",
    "damage_resistance", "shield_parry", "medic_heal", "restore_repair", "maneuver_test",
)

_MODULES = {"mr": mr, "eng": eng, "rules": rules}


def _assert_symbol(dotted: str, *, schema: bool = False) -> None:
    head, _, tail = dotted.partition(".")
    if schema:
        cls = getattr(schemas, head, None)
        assert cls is not None, f"schema class {head!r} missing"
        assert tail in cls.model_fields, f"{dotted} is not a field on {head}"
        return
    module = _MODULES.get(head)
    assert module is not None, f"unknown module prefix in {dotted!r}"
    assert hasattr(module, tail), f"{dotted} does not exist"


def _invoke_present(inv: dict) -> bool:
    kind, key = inv["kind"], inv["key"]
    if kind == "console":
        return key in CONSOLE_ACTIONS
    if kind == "enemy_opt":
        # The enemy-decker "Attack" menu is built at runtime from _strikeOptionsHtml(), filtered to
        # carried programs; its static source of truth is the option array entry ['<key>', '<label>'].
        return f"['{key}', " in RUN_UI
    if kind in ("endpoint", "raw"):
        return key in RUN_UI
    raise AssertionError(f"unknown invoke kind {kind!r}")


def _expected_unreachable_actions() -> set[str]:
    """Actions with no run-UI control that the ledger DOCUMENTS: open backend-only
    divergences + open UI-reachability gaps. Derived from the ledger so a fix/ruling must
    update the ledger to change what the reachability test tolerates."""
    unreachable = set(open_ui_gaps())  # e.g. purge_hog while its gap stays open
    for d in open_divergences():
        if d["id"] == "logon_to_ltg_unsurfaced":
            unreachable.add("logon_to_ltg")
    return unreachable


# ============================================================ REQ 1 -- PRESENT
def test_req1_programs_are_exactly_the_schema_utilities():
    assert all_program_slots() == set(DeckerUtilities.model_fields)
    assert all_program_slots() == COV_UTILITIES          # build on the existing contract


def test_req1_carried_options_are_exactly_the_schema_option_fields():
    assert carried_option_fields() == set(ProgramOptions.model_fields)
    assert carried_option_fields() == COV_OPTIONS


def test_req1_ic_is_exactly_the_catalog():
    assert set(IC) == set(rules.IC_CATALOG)
    assert set(IC) == COV_IC_TYPES


def test_req1_ledger_mirrors_the_workshop_builder():
    # Every buildable program/option in deck-workshop.html has a ledger row and vice versa,
    # so a NEW workshop entry cannot appear without a ledger row (or an EXCLUSIONS entry).
    assert WORKSHOP_PROGRAMS == set(PROGRAMS)
    # Compare only the TOGGLE options: intrinsic carried fields (e.g. the Attack damage level) are
    # ledger rows but not OPTION_DEFS toggles, so they are excluded from the 1:1 workshop mirror.
    assert WORKSHOP_OPTIONS == toggle_option_keys()


def test_req1_program_and_ic_resolvers_exist_in_engine():
    for name, p in PROGRAMS.items():
        if p["resolver"] != "passive":
            assert hasattr(eng, p["resolver"]), f"{name}: engine has no resolver {p['resolver']!r}"
    for name, entry in IC.items():
        assert hasattr(eng, entry["resolver"]), f"IC {name}: engine has no {entry['resolver']!r}"


def test_req1_host_mechanic_symbols_exist():
    for key, m in HOST_MECHANICS.items():
        _assert_symbol(m["schema"], schema=True)
        _assert_symbol(m["handler"])
        _assert_symbol(m["endpoint"])


# ============================================================ REQ 2 -- REACHABLE
def test_req2_every_program_config_field_is_in_run_ui():
    for name, p in PROGRAMS.items():
        assert p["cfg"] in RUN_UI, f"{name}: config field {p['cfg']} missing from matrix-run.html"


def test_req2_every_active_program_invoke_control_is_reachable():
    for name, p in active_programs().items():
        for inv in p["invoke"]:
            assert _invoke_present(inv), f"{name}: invoke control {inv} not reachable in run UI"


def test_req2_every_action_type_is_reachable_or_documented():
    expected_unreachable = _expected_unreachable_actions()
    for action in ACTION_TYPES:
        reachable = action in CONSOLE_ACTIONS
        if not reachable and action in DEDICATED_CONTROLS:
            assert DEDICATED_CONTROLS[action] in RUN_UI, f"{action}: dedicated control token missing"
            reachable = True
        if not reachable:
            assert action in expected_unreachable, (
                f"ActionType {action!r} has no run-UI control and is not a documented "
                f"backend-only action or an open UI-reachability gap"
            )
    # The documented-unreachable set must never contain something that IS console-reachable.
    for action in expected_unreachable:
        assert action not in CONSOLE_ACTIONS, f"{action!r} is listed unreachable but IS in ACTION_CATALOG"


def test_req2_action_registry_matches_existing_coverage_contract():
    assert ACTION_TYPES == COV_ACTIONS
    assert CONSOLE_ACTIONS <= ACTION_TYPES        # no console key outside the schema Literal


# ============================================================ REQ 4 -- ONE SHARED SEAM
def test_req4_shared_seam_primitives_are_single_callables():
    for prim in SHARED_SEAM_PRIMITIVES:
        assert callable(getattr(eng, prim, None)), f"shared resolver {prim} missing/not callable"


def test_req4_divergences_are_pinned_and_nondrifting():
    """Each OPEN divergence's evidence is asserted still-present, so 'no gaps' cannot be faked by
    deleting the divergent code. When a divergence is RULED ON, update DIVERGENCES status (and,
    if fixed, the code) -- which will correctly flip the matching assertion below."""
    open_ids = {d["id"] for d in open_divergences()}

    if "dinab_attack_ic_bypass" in open_ids:
        src = inspect.getsource(mr._dinab_attack_ic)
        assert "cybercombat_attack" not in src            # still bypasses the shared seam
        assert "stage_damage" in src or "roll_dice" in src  # ... by hand-rolling

    if "area_attack_cybercombat_bypass" in open_ids:
        src = inspect.getsource(mr.area_attack)
        assert "cybercombat_attack" not in src            # still hand-rolls multi-target damage
        assert hasattr(mr, "_enemy_shield_parry")         # the enemy parry it skips still exists

    if "bouncer_inert" in open_ids:
        assert 'value="bouncer"' in DESIGNER              # designer still builds a Bouncer
        assert "new_security_code" in DESIGNER            # ... carrying the upgrade payload
        assert "new_security_code" not in schemas.SheafEvent.model_fields  # dropped at the schema
        assert "bouncer" not in inspect.getsource(mr._activate_sheaf_step)  # no run handler

    if "logon_to_ltg_unsurfaced" in open_ids:
        assert "logon_to_ltg" in ACTION_TYPES
        assert "logon_to_ltg" not in CONSOLE_ACTIONS
        assert "logon_to_ltg" not in DEDICATED_CONTROLS


# ============================================================ REQ 5 -- GUARDED
def test_req5_every_program_has_a_numeric_proof():
    for name, p in PROGRAMS.items():
        if p["resolver"] == "passive":
            assert name in PASSIVE_COVERED, f"passive program {name} has no numeric proof"
        else:
            assert p["resolver"] in COVERED_PRIMITIVES, (
                f"{name}: resolver {p['resolver']!r} has no executed oracle row"
            )


def test_req5_every_ic_has_a_numeric_proof():
    for name, entry in IC.items():
        assert entry["resolver"] in COVERED_PRIMITIVES, (
            f"IC {name}: resolver {entry['resolver']!r} has no executed oracle row"
        )


def test_req5_scope_and_exclusions_are_disjoint():
    inscope = set(PROGRAMS) | set(OPTIONS) | set(IC)
    assert inscope.isdisjoint(set(EXCLUSIONS)), "an in-scope item is also listed as excluded"


def test_req5_excluded_items_are_truly_absent_from_the_builder():
    # The exclusions are provable: each excluded program/option is genuinely NOT buildable.
    assert "sensitive" not in {o.lower() for o in WORKSHOP_OPTIONS}
    for absent in ("Browse", "Commlink", "Spoof", "Locate File", "Track"):
        assert absent not in WORKSHOP_PROGRAMS, f"{absent} is excluded but present in the workshop"


def test_req5_ui_gap_keys_are_real_action_types():
    for key in UI_REACHABILITY_GAPS:
        assert key in ACTION_TYPES, f"UI-reachability gap {key!r} is not an ActionType"


def test_req5_divergence_ids_unique_and_status_valid():
    ids = [d["id"] for d in DIVERGENCES]
    assert len(ids) == len(set(ids)), "duplicate divergence id"
    for d in DIVERGENCES:
        assert d["status"] in {"open", "accepted", "fixed"}, f"{d['id']}: bad status {d['status']!r}"
