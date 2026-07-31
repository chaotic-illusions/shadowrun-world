"""Generate an exhaustive Event Log catalog with RENDERED admin + player examples.

Static, AST-based extraction so coverage is GUARANTEED: it finds every ``_append_event(...)``
call site in ``app/routers/matrix_runs.py`` and, for each one, records the enclosing function,
the guarding ``if`` condition, the event ``type`` (resolving ``**event_base`` spreads and
``_append_event(state, ev)`` dynamics), and the payload keys.

For each event it then produces a REPRESENTATIVE, concrete example (no ``{variables}``):

  * ADMIN  -- the real f-string template evaluated against one fixed "sample world"
              (a stock host + decker + a stock IC/Worm, listed under SAMPLE below).
  * PLAYER -- that same event run through the ACTUAL serializer redaction pipeline
              (``_redact_system_action_event`` -> ``_redact_event_tally`` -> ``_redact_event_ic``),
              so what the player sees is computed, not guessed.

Outputs:
  * docs/event-log-catalog.md   -- readable, grouped by event type.
  * docs/event-log-catalog.csv  -- one row per event with a blank ``notes`` column, so the
                                   catalog can be reviewed/annotated in Excel and fed back.

Notes on fidelity (the sample world is fixed, so numbers are illustrative, not from a live run):
  * Player lines are the real redaction output. For host-system-test events the player line is a
    GENERIC rebuild ("<Action> -- SUCCESS (Net Successes: N).") -- the effective Target Number is
    shown only after Analyze Host reveals that subsystem, so the sample world leaves it hidden.
  * The IC identity used for the player redaction is taken from the first "Type-Rating" token in
    the rendered admin line (so "Killer-5" collapses to "Killer" at detection level 2, etc.).

Run:  python tools/gen_event_catalog.py
"""
from __future__ import annotations

import ast
import builtins as _builtins
import collections
import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from app.routers import matrix_runs as mr  # noqa: E402

SRC = ROOT / "app" / "routers" / "matrix_runs.py"
_SUFFIX = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--suffix=")), "")
OUT_MD = ROOT / "docs" / f"event-log-catalog{_SUFFIX}.md"
OUT_CSV = ROOT / "docs" / f"event-log-catalog{_SUFFIX}.csv"
# Reviewer notes round-trip: preserve from the OUTPUT file itself once it exists (so annotating a
# derived catalog like -final and re-running keeps those notes); seed from the base CSV the first
# time a new derived file is created.
NOTES_SRC = OUT_CSV if OUT_CSV.exists() else ROOT / "docs" / "event-log-catalog.csv"


# ============================================================ sample rendering
# A "Smart" value fills any variable/key a template touches that the curated SAMPLE below does not
# provide, so EVERY template renders without a KeyError/NameError. Numeric-looking names resolve to
# a small int; everything else to a short string.
_NUM_HINTS = (
    "success", "rating", "tn", "net", "box", "pool", "count", "damage", "size", "remaining",
    "turn", "init", "level", "tally", "hit", "mpcp", "depth", "round", "increase", "total",
    "ones", "value", "margin", "reduction", "dice", "credit", "point", "factor", "index",
    "number", "amount", "hp", "boxes", "successes", "rem",
)


class Smart:
    __slots__ = ("hint",)

    def __init__(self, hint: str = "") -> None:
        self.hint = str(hint)

    def _v(self):
        h = self.hint.lower()
        return 3 if any(t in h for t in _NUM_HINTS) else (f"<{self.hint}>" if self.hint else "<?>")

    def __format__(self, spec):
        try:
            return format(self._v(), spec)
        except Exception:
            return str(self._v())

    def __str__(self):
        return str(self._v())

    def __int__(self):
        v = self._v()
        return v if isinstance(v, int) else 3

    __index__ = __int__

    def __float__(self):
        return float(int(self))

    def __getitem__(self, k):
        return _key_sample(k)

    def get(self, k, default=None):
        if default is not None:
            return default
        return _key_sample(k)

    def __getattr__(self, name):
        if name.startswith("__"):
            raise AttributeError(name)
        if name in _STR_METHODS:
            return lambda *a, **k: self._apply_str(name, a, k)
        if name in _KEY_SAMPLES:
            return _key_sample(name)
        return Smart(name)

    def _apply_str(self, name, a, k):
        base = self._v()
        base = base if isinstance(base, str) else str(base)
        try:
            return getattr(base, name)(*a, **k)
        except Exception:
            return base

    def __call__(self, *a, **k):
        return Smart(self.hint)

    def __iter__(self):
        return iter(())

    def __len__(self):
        return 0

    def __bool__(self):
        return True

    def __contains__(self, x):
        return False

    def __add__(self, o):
        return (int(self) + o) if isinstance(o, (int, float)) else (str(self) + str(o))

    def __radd__(self, o):
        return (o + int(self)) if isinstance(o, (int, float)) else (str(o) + str(self))

    def __sub__(self, o):
        return int(self) - (o if isinstance(o, (int, float)) else 0)

    def __rsub__(self, o):
        return (o if isinstance(o, (int, float)) else 0) - int(self)

    def __mul__(self, o):
        return int(self) * (o if isinstance(o, (int, float)) else 1)

    __rmul__ = __mul__

    def __floordiv__(self, o):
        return int(self) // (o if isinstance(o, int) and o else 1)

    def __rfloordiv__(self, o):
        return (o if isinstance(o, int) else 3) // max(1, int(self))

    def __mod__(self, o):
        return int(self)

    def __eq__(self, o):
        return self._v() == o

    def __ne__(self, o):
        return self._v() != o

    def __lt__(self, o):
        return int(self) < o if isinstance(o, (int, float)) else False

    def __gt__(self, o):
        return int(self) > o if isinstance(o, (int, float)) else False

    def __le__(self, o):
        return int(self) <= o if isinstance(o, (int, float)) else False

    def __ge__(self, o):
        return int(self) >= o if isinstance(o, (int, float)) else False

    def __hash__(self):
        return hash(self.hint)


# Sample values for common dict KEYS, so `x['type']` / `x.get('name')` render sensibly even when
# `x` is an uncurated Smart. Strings that would otherwise leak as <marker>.
_KEY_SAMPLES = {
    "type": "Killer", "name": "Payroll DB", "label": "Payroll DB", "rating": 5, "id": "ic_1",
    "subsystem": "files", "variant": "poison", "code": "Green", "status": "active",
    "device": "Datastore", "outcome": "mpcp_infected", "handle": "Razor", "tier": "veteran",
    "intent": "hunt", "display": "Attack", "key": "attack", "successes": 3, "tn": 4, "pool": 6,
    "final_damage_level": "M", "damage_level": "M", "address": "NA/UCAS-SEA-1234",
    "computer_skill": 6, "file": "Payroll DB", "boxes": 2, "mpcp": 6, "target": "Datastore",
    "storage_used_mp": 90, "tar_cm": 2, "ic_type": "Killer", "security_code": "Green",
    "io_speed": 10, "sensor": 4, "evasion": 5, "masking": 5, "fate": "burned",
}
_STR_METHODS = {
    "upper", "lower", "title", "capitalize", "strip", "lstrip", "rstrip", "replace", "split",
    "rsplit", "startswith", "endswith", "join", "format", "zfill", "ljust", "rjust",
}


def _key_sample(k):
    if isinstance(k, str) and k in _KEY_SAMPLES:
        return _KEY_SAMPLES[k]
    return Smart(k if isinstance(k, str) else "")


class SmartDict(dict):
    def __missing__(self, key):
        return _key_sample(key)

    def get(self, key, default=None):
        if key in self:
            return self[key]
        return default if default is not None else _key_sample(key)


def _SD(d):
    return SmartDict({k: (_SD(v) if isinstance(v, dict) else v) for k, v in d.items()})


# One fixed "sample world": Orange host (Security Value 6), MPCP-6 decker (Hardening 2), a stock
# Killer-5 / Worm-4 on the Files subsystem (rating 8 -> a TN-3 utility test). Curated so common
# templates render coherent numbers; anything unlisted falls to Smart.
_ROLL = _SD({"pool": 6, "tn": 4, "successes": 3, "ones": 1, "dice": [6, 5, 4, 3, 2, 1],
             "net_successes": 3})
_HOSTROLL = _SD({"pool": 6, "tn": 7, "successes": 1, "ones": 2, "dice": [7, 3, 2, 2, 1, 1]})
SAMPLE = {
    "rating": 5, "subsystem": "files", "tid": "", "remaining": 2, "locate_turns": 3, "trace_tn": 4,
    "acting_type": "Killer", "acting_rating": 5, "effect_type": "Killer", "effect_rating": 5,
    "hunt_successes": 3, "net_successes": 3, "boxes": 2, "mpcp_hit": 1, "new_init": 12, "count": 2,
    "surface_type": "Trace", "surface_rating": 5, "hidden_type": "Killer", "hidden_rating": 5,
    "h_type": "Killer", "h_rating": 5, "sec_code": "Orange", "meat_boxes": 2, "persona_boxes": 3,
    "stun_boxes": 2, "sparky_final": "M", "sparky_boxes": 2, "final_dmg": "M", "b_roll": _ROLL,
    "final_damage_level": "M", "damage": "M", "subsystem_rating": 8, "already_located": 1,
    "worm": _SD({"rating": 4, "id": "ic_1", "type": "Worm", "subsystem": "files"}),
    "ic": _SD({"type": "Killer", "rating": 5, "id": "ic_1", "status": "active", "boxes": 2,
               "initiative": 12, "subsystem": "files"}),
    "res": _SD({"tn": 3, "roll": _ROLL, "decker_roll": _ROLL, "host_roll": _HOSTROLL,
                "success": True, "decker_net_successes": 3, "tally_increase": 1,
                "worm_destroyed": True}),
    "wr": _SD({"roll": _SD({"pool": 6, "successes": 3, "tn": 6}), "tn": 6, "net_successes": 2,
               "mpcp_infected": True}),
    "decker": _SD({"mpcp": 6, "hardening": 2, "computer_skill": 6, "utilities": _SD({}),
                   "sensor": 4, "evasion": 5}),
    "state": _SD({"security_tally": 5, "current_turn": 2, "current_pass": 1,
                  "condition_monitor": _SD({"persona_boxes": 3, "stun_boxes": 2,
                                            "physical_boxes": 0, "mpcp_damage": 0}),
                  "host_security_value": 6, "host_security_code": "Orange",
                  "initiative_passes": 2}),
    "attack": _SD({"attack_roll": _ROLL, "resistance": _SD({"resist_roll": _ROLL}),
                   "icon": _SD({"final_damage_level": "M"}), "meat": _SD({"final_damage_level": "M"})}),
    "black": _SD({"attack_roll": _ROLL, "icon": _SD({"final_damage_level": "M"}),
                  "meat": _SD({"final_damage_level": "M"})}),
    "hunt": _SD({"hit": True, "roll": _ROLL}),
    "sparky_body": _SD({"successes": 2}),
    "test": _SD({"success": True, "decker_net_successes": 3, "tn": 4, "decker_roll": _ROLL,
                 "tally_increase": 1}),
    "probe": _SD({"tally_increase": 2, "roll": _ROLL}),
    "det": _SD({"tally_increase": 1}),
}
SAMPLE.update({
    # string locals
    "handle": "Razor", "label": "Attack", "icon_label": "Payroll DB", "utility_name": "Attack",
    "btarget": "Datastore", "dmg_kind": "physical", "meat_kind": "physical", "clamp_note": "",
    "skulk_note": "", "_payload": "", "_where": "on the Files subsystem", "_vlabel": "Worm",
    "pretty": "Attack", "_atk_letter": "M", "src": "Killer", "program": "attack",
    "stored": "attack", "file": "Payroll DB", "name": "Razor", "attr": "Bod",
    "attribute": "Bod", "attr_key": "bod", "util": "Attack", "utility": "Attack", "key": "attack",
    "context": "the operation", "note": "", "headline": "Data bomb on Files", "tail": "",
    "comp_note": "", "dmg_part": "", "child_name": "Frame", "parent_name": "Killer",
    "reveals": "Files 8",
    # numeric locals
    "eff": 5, "power": 6, "applied": 1, "succ": 3, "decker_succ": 3, "host_succ": 1, "frag": 2,
    "meat_val": 2, "computer_skill": 6, "hardening": 2, "decoy_succ": 2, "decoy_staged": 1,
    "d6": 4, "passes": 2, "floor": 0, "wound": "light", "healed": 2, "left": 2, "full": 0,
    "storage_used_mp": 90, "now": 0, "atk_succ": 3, "def_succ": 3, "shield_succ": 3, "shock": 2,
    "overflow_after": 1, "n_delete": 1, "tar_cm": 2, "crashed_n": 1, "flushed": 1,
    "man_succ": 3, "opp_succ": 2,
    # more string locals
    "disp": "Attack", "head": "Data bomb", "detail": "", "suffix": "", "actor": "Razor",
    "action_label": "Analyze Subsystem", "result_detail": "", "target_ref": "Razor",
    "names": "Payroll DB", "security_code": "Green", "player_label": "Razor", "weakest": "attack",
    "target_file": "Payroll DB", "_rlabel": "Worm", "source_piece": "Datastore", "bod": "Bod",
    "ic_type": "Killer", "address": "NA/UCAS-SEA-1234", "io_speed": 10, "fate": "burned",
    # containers
    "enemy": _SD({"handle": "Razor", "tier": "veteran", "intent": "hunt"}),
})
SAMPLE.update({
    # conditional-suffix note vars -> empty so the base sentence renders cleanly
    "tally_note": "", "mpcp_note": "", "floor_note": "",
    "frag": "Attack -3 (CRASHED)",
    "fate": "the hostile decker's icon crashes -- dumped and out of the run.",
    "body": _SD({"program": "attack", "action_type": "attack", "subsystem": "files",
                 "target_file": "Payroll DB", "edit_mode": "erase", "note": "",
                 "suppress_trace": False}),
})


class SmartLocals(dict):
    def __missing__(self, key):
        if hasattr(mr, key):
            return getattr(mr, key)
        if hasattr(_builtins, key):
            return getattr(_builtins, key)
        return Smart(key)


def render_admin(desc_src: str) -> tuple[str, str | None]:
    """Evaluate a description f-string template against the sample world. Returns (text, error)."""
    try:
        code = compile(desc_src, "<template>", "eval")
        ns = SmartLocals(SAMPLE)
        val = eval(code, {"__builtins__": _builtins.__dict__}, ns)  # noqa: S307 (trusted source)
        return " ".join(str(val).split()), None
    except Exception as exc:  # noqa: BLE001
        return f"[could not render: {desc_src}]", f"{type(exc).__name__}: {exc}"


# ------------------------------------------------------------ player redaction
_REDACT_STATE = SmartDict({
    "host_ratings_revealed": {},      # nothing Analyzed yet -> most-redacted player view
    "host_security_value": 6, "host_security_code": "Orange",
    "security_tally": 5, "analyzed_subsystems": [],
})


def _ic_ident(text: str) -> tuple[str, int]:
    """The IC identity for the player redaction, taken from the first 'Type-Rating' token in the
    rendered admin line (so 'Killer-5' collapses to 'Killer' at level 2)."""
    for m in re.finditer(r"\b([A-Z][A-Za-z]+)-(\d{1,2})\b", text or ""):
        word = m.group(1)
        if word not in ("Disinfect", "Analyze", "Decrypt", "Defuse", "Relocate", "Slow",
                        "Steamroller", "TN", "Mp", "MPCP", "AP", "DF"):
            return word, int(m.group(2))
    return "Killer", 5


def _sample_event_value(key: str, admin_text: str, success: bool):
    k = key.lower()
    if key == "host_system_test":
        return True
    if key == "success":
        return success
    if key == "action_label":
        return admin_text.split(" -- ")[0].strip() if " -- " in admin_text else "System Test"
    if key in ("is_key", "all_located", "physical_trace_immune", "is_trap_reveal", "destroyed",
               "tampered", "revealed", "console_access"):
        return True
    if key in ("ic_id", "actor_id", "target_id", "scramble_ref", "bomb_id"):
        return "ic_1"
    if key == "ic_type":
        return _ic_ident(admin_text)[0]
    if key == "construct_components":
        return [{"type": "Killer", "rating": 5}, {"type": "Blaster", "rating": 6}]
    if key == "outcome":
        return "mpcp_infected"
    if key == "trace_phase":
        return "hunting"
    if key == "attribute_target":
        return "bod"
    if key in ("subsystem",):
        return "files"
    if key == "action":
        return "system_test"
    if k.endswith("_roll") or k == "roll":
        return {"pool": 6, "tn": 4, "successes": 3, "dice": [6, 5, 4, 3, 2, 1], "ones": 1}
    if key in ("cluster_size", "count"):
        return 2
    if any(t in k for t in ("success", "tn", "net", "box", "tally", "rating", "margin",
                            "reduction", "hit", "damage", "boxes", "amount", "increase")):
        return 3 if success else -1
    if k.endswith("_id"):
        return "ic_1"
    return "sample"


def render_player(etype: str, keys: list[str], literals: dict, gm_only, admin_text: str) -> str:
    if gm_only not in (None, "False"):
        return "(admin-only -- not shown to players)"
    success = not re.search(r"\bFAIL", admin_text or "", re.I)
    ev = {"type": etype, "description": admin_text}
    for k in keys:
        if k == "**spread**":
            continue
        ev[k] = literals[k] if k in literals else _sample_event_value(k, admin_text, success)
    ic_type, ic_rating = _ic_ident(admin_text)
    if any(k in ev for k in ("ic_id", "actor_id", "target_id")) or "ic_type" in keys:
        ev.setdefault("ic_id", "ic_1")
        if "ic_type" in ev:
            ev["ic_type"] = ic_type
    disclosures = {"ic_1": {"level": 2, "type": ic_type, "rating": ic_rating}}
    try:
        e = mr._redact_system_action_event(dict(ev), _REDACT_STATE)
        e = mr._redact_event_tally(e)
        e = mr._redact_event_ic(e, disclosures)
        return " ".join(str(e.get("description", "")).split())
    except Exception as exc:  # noqa: BLE001
        return f"[player-render error: {type(exc).__name__}: {exc}]"


# ============================================================ AST extraction
def _const_str(node):
    return node.value if isinstance(node, ast.Constant) and isinstance(node.value, str) else None


def _const_any(node):
    return node.value if isinstance(node, ast.Constant) else None


def _unparse(node):
    try:
        return ast.unparse(node)
    except Exception:
        return "<unparseable>"


def _short(text, limit=180):
    text = " ".join(text.split())
    return text if len(text) <= limit else text[: limit - 3] + "..."


class _Parents(ast.NodeVisitor):
    def __init__(self):
        self.parent = {}

    def generic_visit(self, node):
        for child in ast.iter_child_nodes(node):
            self.parent[child] = node
        super().generic_visit(node)


def _enclosing_function(parent, node):
    cur = parent.get(node)
    while cur is not None:
        if isinstance(cur, (ast.FunctionDef, ast.AsyncFunctionDef)):
            return cur
        cur = parent.get(cur)
    return None


def _guarding_condition(parent, node):
    child, cur = node, parent.get(node)
    while cur is not None:
        if isinstance(cur, ast.If):
            in_orelse = any(_contains(n, child) for n in cur.orelse)
            return f"{'else of' if in_orelse else 'when'} `{_short(_unparse(cur.test))}`"
        child, cur = cur, parent.get(cur)
    return "always (no local guard)"


def _contains(root, target):
    return any(n is target for n in ast.walk(root))


def _dict_assigns(func):
    """Dict-literal assignments (name -> Dict) plus EVERY name assignment (name -> [(lineno, node)])
    for simple + annotated assigns, so a `description: desc` name resolves to the NEAREST preceding
    `desc = ...` (branch-local), not an arbitrary later reassignment elsewhere in the function."""
    dicts = {}
    name_assigns = collections.defaultdict(list)
    for n in ast.walk(func):
        name = val = None
        if isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name):
            name, val = n.targets[0].id, n.value
        elif isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name) and n.value is not None:
            name, val = n.target.id, n.value
        elif isinstance(n, ast.Assign) and len(n.targets) == 1 and isinstance(n.targets[0], ast.Tuple):
            # Tuple-unpack (e.g. `changed, description = f(...)`): record each bound name against the
            # (unresolvable) RHS so nearest-assign sees it -- the resolver then marks such a
            # function-return description dynamic instead of grabbing a sibling branch's assignment.
            for elt in n.targets[0].elts:
                if isinstance(elt, ast.Name):
                    name_assigns[elt.id].append((getattr(n, "lineno", 0), n.value))
            continue
        if name is None:
            continue
        name_assigns[name].append((getattr(n, "lineno", 0), val))
        if isinstance(val, ast.Dict):
            dicts[name] = val
    return dicts, name_assigns


def _nearest_assign(name_assigns, name, before_line):
    """Value node assigned to `name` NEAREST above `before_line` (branch-local), else the last."""
    cands = name_assigns.get(name) or []
    before = [(ln, v) for ln, v in cands if ln < before_line]
    if before:
        return max(before, key=lambda t: t[0])[1]
    return cands[-1][1] if cands else None


def _subscript_str_assigns(func, name):
    """{key: value_node} for `name["key"] = value` assignments in a function (built-up payloads)."""
    out = {}
    for n in ast.walk(func):
        if (isinstance(n, ast.Assign) and len(n.targets) == 1
                and isinstance(n.targets[0], ast.Subscript)
                and isinstance(n.targets[0].value, ast.Name)
                and n.targets[0].value.id == name):
            k = _const_str(n.targets[0].slice)
            if k is not None:
                out[k] = n.value
    return out


def _resolve_flat(arg, dict_assigns, func):
    """Ordered {key: value_node} for an event payload: a dict literal, or a NAME built from a dict
    literal and/or `name["key"] = value` assignments. None when nothing is statically resolvable."""
    if isinstance(arg, ast.Dict):
        return _flatten(arg, dict_assigns)
    if isinstance(arg, ast.Name):
        flat = {}
        if arg.id in dict_assigns:
            flat.update(_flatten(dict_assigns[arg.id], dict_assigns))
        if func is not None:
            flat.update(_subscript_str_assigns(func, arg.id))
        return flat or None
    return None


def _flatten(d, dict_assigns, seen=()):
    """Ordered {key: value_node}, expanding **event_base spreads (later keys win)."""
    out = {}
    for k, v in zip(d.keys, d.values):
        if k is None:  # ** spread
            if isinstance(v, ast.Name) and v.id in dict_assigns and v.id not in seen:
                out.update(_flatten(dict_assigns[v.id], dict_assigns, seen + (v.id,)))
        else:
            ks = _const_str(k)
            if ks is not None:
                out[ks] = v
    return out


def main() -> None:
    tree = ast.parse(SRC.read_text(encoding="utf-8"))
    parents = _Parents()
    parents.visit(tree)

    records, admin_errs, player_errs = [], 0, 0
    for node in ast.walk(tree):
        if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == "_append_event"):
            continue
        func = _enclosing_function(parents.parent, node)
        fname = func.name if func else "<module>"
        cond = _guarding_condition(parents.parent, node)
        line = node.lineno
        dict_assigns, name_assigns = _dict_assigns(func) if func else ({}, {})

        arg = node.args[1] if len(node.args) >= 2 else None
        flat = _resolve_flat(arg, dict_assigns, func) if arg is not None else None
        if not flat:
            records.append({"type": "(dynamic)", "func": fname, "line": line, "cond": cond,
                            "keys": [], "gm_only": None, "template": _unparse(arg) if arg else "?",
                            "admin": f"(payload built dynamically in `{fname}` -- see source)",
                            "player": "--"})
            continue
        etype = _const_str(flat.get("type")) or (
            f"(expr){_unparse(flat['type'])}" if "type" in flat else "(untyped)")
        desc_node = flat.get("description")
        # description may be a bare name (e.g. `desc` / `msg`) reassigned per branch -- resolve it to
        # the assignment NEAREST above this _append_event call, so each event renders its own branch.
        if isinstance(desc_node, ast.Name):
            resolved = _nearest_assign(name_assigns, desc_node.id, line)
            if resolved is not None:
                desc_node = resolved
        # description built by a function return (e.g. `_, description = f(...)`): not statically
        # renderable -- mark it dynamic rather than misattributing a sibling branch's assignment.
        if isinstance(desc_node, ast.Call):
            note = f"(dynamic -- description returned by {_unparse(desc_node.func)}())"
            keys = [k for k in flat if k not in ("type", "description")]
            gm_only = _unparse(flat["gm_only"]) if "gm_only" in flat else None
            records.append({"type": etype, "func": fname, "line": line, "cond": cond, "keys": keys,
                            "gm_only": gm_only, "template": _unparse(desc_node),
                            "admin": note, "player": note})
            continue
        # ...or `some_local_dict[level]` (graduated notices) -- render a representative branch.
        if (isinstance(desc_node, ast.Subscript) and isinstance(desc_node.value, ast.Name)
                and desc_node.value.id in dict_assigns):
            dvals = dict_assigns[desc_node.value.id].values
            if dvals:
                desc_node = dvals[min(1, len(dvals) - 1)]
        desc_src = _unparse(desc_node) if desc_node is not None else "'(no description)'"
        literals = {k: _const_any(v) for k, v in flat.items()
                    if k not in ("type", "description") and _const_any(v) is not None}
        keys = [k for k in flat if k not in ("type", "description")]

        admin, aerr = render_admin(desc_src)
        gm_only = _unparse(flat["gm_only"]) if "gm_only" in flat else None
        player = render_player(etype, keys, literals, gm_only, admin)
        if aerr:
            admin_errs += 1
        if player.startswith("[player-render error"):
            player_errs += 1
        records.append({"type": etype, "func": fname, "line": line, "cond": cond, "keys": keys,
                        "gm_only": gm_only, "template": desc_src, "admin": admin, "player": player})

    by_type = collections.defaultdict(list)
    for r in records:
        by_type[r["type"]].append(r)

    leaks = collections.Counter()
    for r in records:
        for tok in re.findall(r"<([^<>]+)>", r["admin"]):
            leaks[tok] += 1

    _write_md(records, by_type)
    _write_csv(records)
    print(f"Wrote {OUT_MD.relative_to(ROOT)} + {OUT_CSV.relative_to(ROOT)} -- "
          f"{len(records)} sites, {len([t for t in by_type if not t.startswith('(')])} types. "
          f"(admin render fallbacks: {admin_errs}, player render errors: {player_errs})")
    if leaks:
        top = ", ".join(f"{tok}x{n}" for tok, n in leaks.most_common(30))
        print(f"Unsampled markers ({sum(leaks.values())} total, {len(leaks)} distinct): {top}")


def _anchor(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def _write_md(records, by_type):
    L = []
    a = L.append
    a("# Event Log Catalog (auto-generated -- rendered examples)\n")
    a("> Generated by `tools/gen_event_catalog.py` from `app/routers/matrix_runs.py`. Do not")
    a("> hand-edit -- re-run the generator. Every `_append_event` site is enumerated, so coverage")
    a("> is complete by construction. A companion `event-log-catalog.csv` has the same rows plus a")
    a("> blank `notes` column for review in Excel.\n")
    a(f"- Event emit sites: **{len(records)}**")
    a(f"- Distinct event types: **{len([t for t in by_type if not t.startswith('(')])}**\n")
    a("## How to read this\n")
    a("Each event shows a concrete **Admin** line (the real template rendered against one fixed")
    a("sample world) and the **Player** line (that event run through the actual serializer")
    a("redaction). Sample world: an Orange host (Security Value 6), an MPCP-6 decker (Hardening 2),")
    a("a stock **Killer-5** / **Worm-4** on the **Files** subsystem (rating 8). Numbers are")
    a("illustrative, not from a live run.\n")
    a("Player-view rules the redaction applies: `gm_only` events are dropped entirely; host system")
    a("tests are rebuilt generically (`<Action> -- SUCCESS (Net Successes: N).`) with the Target")
    a("Number shown only after Analyze Host reveals that subsystem (hidden here); the running")
    a("security tally + host successes are stripped; and IC identity collapses to the decker's")
    a("detection level (here **level 2** -- type known, rating hidden).\n")
    a("## Index\n")
    for t in sorted(by_type, key=lambda s: (s.startswith("("), s)):
        a(f"- [`{t}`](#{_anchor(t)}) ({len(by_type[t])})")
    a("")
    for t in sorted(by_type, key=lambda s: (s.startswith("("), s)):
        a(f"\n## `{t}`\n")
        for r in sorted(by_type[t], key=lambda x: x["line"]):
            gm = "  **[ADMIN-ONLY]**" if r["gm_only"] not in (None, "False") else ""
            a(f"- **`{r['func']}`** (line {r['line']}) -- fires {r['cond']}.{gm}")
            a(f"  - Admin:  {r['admin']}")
            a(f"  - Player: {r['player']}")
        a("")
    OUT_MD.write_text("\n".join(L) + "\n", encoding="utf-8")


def _write_csv(records):
    cols = ["type", "function", "line", "condition", "gm_only", "admin_example",
            "player_example", "payload_keys", "template", "notes"]
    # Preserve any reviewer notes already in the CSV (match by type + function + line) so a
    # regeneration NEVER wipes annotations.
    prior_notes = {}
    if NOTES_SRC.exists():
        try:
            with NOTES_SRC.open(encoding="utf-8-sig", newline="") as fh:
                for row in csv.DictReader(fh):
                    note = (row.get("notes") or "").strip()
                    if note:
                        prior_notes[(row.get("type", ""), row.get("function", ""),
                                     str(row.get("line", "")))] = row["notes"]
        except Exception:
            pass
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(cols)
        for r in sorted(records, key=lambda x: (x["type"].startswith("("), x["type"], x["line"])):
            w.writerow([
                r["type"], r["func"], r["line"], r["cond"].replace("`", ""),
                (r["gm_only"] if r["gm_only"] not in (None, "False") else ""),
                r["admin"], r["player"], ", ".join(r["keys"]), r["template"],
                prior_notes.get((r["type"], r["func"], str(r["line"])), ""),
            ])
    if prior_notes:
        print(f"Preserved {len(prior_notes)} reviewer note(s) from the existing CSV.")


if __name__ == "__main__":
    main()
