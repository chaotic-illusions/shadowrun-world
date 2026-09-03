"""Idempotent loader that pushes one adventure spec (scripts/adventure_ingest/specs/*.py) into a
running shadowrun-world API, and renders the matching GM prep doc.

Spec module contract (all optional except ADVENTURE):
  ADVENTURE   str   -- the source_adventure tag, e.g. "Silver Angel" (must match ADVENTURE_ORDER
                       in frontend/shared.js so the manage-page filter sorts it into campaign order)
  ORDER       int   -- campaign order number (docs/Adventures/SR_Adventures.xlsx)
  SOURCE      str   -- book / pages
  YEAR        str   -- in-game year
  SYNOPSIS    str   -- markdown, GM-facing plot summary
  TIMELINE    str   -- markdown, optional
  ORGS        list  -- OrganizationCreate dicts + optional keys: summary, allies, enemies (org names)
  LOCATIONS   list  -- LocationCreate dicts + optional keys: summary, controlling_org (org name)
  NPCS        list  -- CharacterCreate dicts + optional keys: role, organization (org name)
  ORG_UPDATES dict  -- {org name: {description_append, notes_append, leadership_add: [...],
                                   allies_add: [names], enemies_add: [names], set: {field: value}}}
  LOC_UPDATES dict  -- {location name: {description_append, notes_append, controlling_org: name,
                                        set: {field: value}}}
  NPC_UPDATES dict  -- {character name: {description_append, background_append, notes_append,
                                         contact_skills_add: [...], organization: name,
                                         set: {field: value}}}
                       `set` overwrites fields verbatim (use for corrections such as a wrong name;
                       never for lore text -- that is what the *_append keys are for). A `set` that
                       renames a row keys the update by the OLD name.
  TAG_EXISTING dict -- {"orgs": [names], "locations": [names], "npcs": [names]}: rows that predate
                       the ingest tooling but belong to this adventure; they get source_adventure
                       stamped when it is still empty.
  MATRIX_HOSTS str  -- markdown: systems worth building later (NOT built by this loader)
  NOT_BUILT   str   -- markdown: flavor names deliberately skipped
  PLAY_NOTES  str   -- markdown: GM hooks / how it plays

Every created row gets is_active=False and source_adventure=ADVENTURE. Re-running is safe:
rows are matched by name (case-insensitive) and appends are skipped when the
"-- <ADVENTURE> --" marker is already present in the target field.
"""
from __future__ import annotations

import json
import urllib.error
import urllib.request

_STRIP_ORG = {"summary", "allies", "enemies"}
_STRIP_LOC = {"summary", "controlling_org"}
_STRIP_NPC = {"role", "organization"}


class Api:
    def __init__(self, base: str, token: str):
        self.base = base.rstrip("/")
        self.token = token

    def _call(self, method: str, path: str, body=None):
        data = json.dumps(body).encode("utf-8") if body is not None else None
        req = urllib.request.Request(self.base + path, data=data, method=method)
        req.add_header("X-Admin-Token", self.token)
        req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                raw = resp.read()
                return json.loads(raw) if raw else None
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", "replace")
            raise RuntimeError(f"{method} {path} -> {e.code}: {detail[:500]}") from None

    def get(self, path):
        return self._call("GET", path)

    def post(self, path, body):
        return self._call("POST", path, body)

    def patch(self, path, body):
        return self._call("PATCH", path, body)


def _marker(adv: str) -> str:
    return f"-- {adv} --"


def _append(existing: str | None, adv: str, text: str) -> str | None:
    """Return the new field value, or None when the marker is already present (no-op)."""
    if not text:
        return None
    if existing and _marker(adv) in existing:
        return None
    block = f"{_marker(adv)}\n{text.strip()}"
    return f"{existing.rstrip()}\n\n{block}" if existing and existing.strip() else block


class Loader:
    def __init__(self, api: Api, spec, dry: bool = False, log=print):
        self.api, self.spec, self.dry, self.log = api, spec, dry, log
        self.adv = spec.ADVENTURE
        self.orgs = {}
        self.locs = {}
        self.chars = {}
        self.report = {"created": [], "updated": [], "skipped": [], "warnings": []}

    # -- helpers -------------------------------------------------------------------------------
    def _refresh(self):
        self.orgs = {o["name"].lower(): o for o in self.api.get("/organizations/")}
        self.locs = {l["name"].lower(): l for l in self.api.get("/locations/")}
        self.chars = {c["name"].lower(): c for c in self.api.get("/characters/")}

    def _org_id(self, name: str | None) -> int | None:
        if not name:
            return None
        o = self.orgs.get(name.lower())
        if not o:
            self.report["warnings"].append(f"org not found: {name}")
            return None
        return o["id"]

    def _do(self, kind: str, verb: str, path: str, body: dict, name: str):
        if self.dry:
            self.log(f"  [dry] {verb} {path} {name}")
            return None
        row = self.api.post(path, body) if verb == "POST" else self.api.patch(path, body)
        self.report["created" if verb == "POST" else "updated"].append(f"{kind}: {name}")
        self.log(f"  {verb} {kind} {name}" + (f" -> id {row.get('id')}" if isinstance(row, dict) else ""))
        return row

    # -- phases --------------------------------------------------------------------------------
    def run(self):
        self._refresh()
        self.log(f"== {self.adv}: loading against {self.api.base}")
        self._create_orgs()
        self._refresh()
        self._org_relations()
        self._create_locations()
        self._create_npcs()
        self._update_orgs()
        self._update_locations()
        self._update_npcs()
        self._tag_existing()
        return self.report

    def _tag_existing(self):
        tags = getattr(self.spec, "TAG_EXISTING", {}) or {}
        for key, rows, path, kind in (
            ("orgs", self.orgs, "/organizations/", "org"),
            ("locations", self.locs, "/locations/", "location"),
            ("npcs", self.chars, "/characters/", "npc"),
        ):
            for name in tags.get(key, []):
                row = rows.get(name.lower())
                if not row:
                    self.report["warnings"].append(f"TAG_EXISTING {kind} not found: {name}")
                    continue
                if row.get("source_adventure"):
                    continue
                self._do(f"{kind}-tag", "PATCH", f"{path}{row['id']}", {"source_adventure": self.adv}, name)

    def _create_orgs(self):
        for o in getattr(self.spec, "ORGS", []):
            if o["name"].lower() in self.orgs:
                self.report["skipped"].append(f"org exists: {o['name']}")
                continue
            body = {k: v for k, v in o.items() if k not in _STRIP_ORG}
            body.setdefault("is_active", False)
            body["source_adventure"] = self.adv
            self._do("org", "POST", "/organizations/", body, o["name"])

    def _org_relations(self):
        for o in getattr(self.spec, "ORGS", []):
            row = self.orgs.get(o["name"].lower())
            if not row or row.get("source_adventure") != self.adv:
                continue
            patch = {}
            for key, field in (("allies", "ally_ids"), ("enemies", "enemy_ids")):
                ids = [i for i in (self._org_id(n) for n in o.get(key, [])) if i]
                merged = sorted(set(row.get(field) or []) | set(ids))
                if merged != sorted(row.get(field) or []):
                    patch[field] = merged
            if patch:
                self._do("org-relations", "PATCH", f"/organizations/{row['id']}", patch, o["name"])

    def _create_locations(self):
        for l in getattr(self.spec, "LOCATIONS", []):
            if l["name"].lower() in self.locs:
                self.report["skipped"].append(f"location exists: {l['name']}")
                continue
            body = {k: v for k, v in l.items() if k not in _STRIP_LOC}
            body["controlling_org_id"] = self._org_id(l.get("controlling_org"))
            body.setdefault("city", "Seattle")
            body.setdefault("is_active", False)
            body["source_adventure"] = self.adv
            row = self._do("location", "POST", "/locations/", body, l["name"])
            if row:
                self.locs[l["name"].lower()] = row

    def _create_npcs(self):
        for c in getattr(self.spec, "NPCS", []):
            if c["name"].lower() in self.chars:
                self.report["skipped"].append(f"npc exists: {c['name']}")
                continue
            body = {k: v for k, v in c.items() if k not in _STRIP_NPC}
            org = c.get("organization")
            body["organization_id"] = self._org_id(org)
            body.setdefault("is_independent", body["organization_id"] is None and org is None)
            body["is_pc"] = False
            body.setdefault("is_active", False)
            body.setdefault("race", "Human")
            body.setdefault("connection", 1)
            body["source_adventure"] = self.adv
            row = self._do("npc", "POST", "/characters/", body, c["name"])
            if row:
                self.chars[c["name"].lower()] = row

    def _update_orgs(self):
        for name, upd in getattr(self.spec, "ORG_UPDATES", {}).items():
            row = self.orgs.get(name.lower())
            if not row:
                self.report["warnings"].append(f"ORG_UPDATES target not found: {name}")
                continue
            patch = {}
            for field in ("description", "notes"):
                new = _append(row.get(field), self.adv, upd.get(f"{field}_append", ""))
                if new is not None:
                    patch[field] = new
            adds = upd.get("leadership_add") or []
            if adds:
                have = {(e.get("name") or "").lower() for e in (row.get("leadership") or [])}
                fresh = [e for e in adds if e["name"].lower() not in have]
                if fresh:
                    patch["leadership"] = list(row.get("leadership") or []) + [
                        {"name": e["name"], "title": e.get("title"), "notes": e.get("notes")} for e in fresh
                    ]
            for key, field in (("allies_add", "ally_ids"), ("enemies_add", "enemy_ids")):
                ids = [i for i in (self._org_id(n) for n in upd.get(key, [])) if i]
                merged = sorted(set(row.get(field) or []) | set(ids))
                if merged != sorted(row.get(field) or []):
                    patch[field] = merged
            patch.update({k: v for k, v in (upd.get("set") or {}).items() if row.get(k) != v})
            if patch:
                self._do("org-update", "PATCH", f"/organizations/{row['id']}", patch, name)
                if "name" in patch:
                    self.orgs[patch["name"].lower()] = {**row, **patch}
            else:
                self.report["skipped"].append(f"org already updated: {name}")

    def _update_locations(self):
        for name, upd in getattr(self.spec, "LOC_UPDATES", {}).items():
            row = self.locs.get(name.lower())
            if not row:
                self.report["warnings"].append(f"LOC_UPDATES target not found: {name}")
                continue
            patch = {}
            for field in ("description", "notes"):
                new = _append(row.get(field), self.adv, upd.get(f"{field}_append", ""))
                if new is not None:
                    patch[field] = new
            if upd.get("controlling_org"):
                oid = self._org_id(upd["controlling_org"])
                if oid and row.get("controlling_org_id") != oid:
                    patch["controlling_org_id"] = oid
            patch.update({k: v for k, v in (upd.get("set") or {}).items() if row.get(k) != v})
            if patch:
                self._do("location-update", "PATCH", f"/locations/{row['id']}", patch, name)
                if "name" in patch:
                    self.locs[patch["name"].lower()] = {**row, **patch}
            else:
                self.report["skipped"].append(f"location already updated: {name}")

    def _update_npcs(self):
        for name, upd in getattr(self.spec, "NPC_UPDATES", {}).items():
            row = self.chars.get(name.lower())
            if not row:
                self.report["warnings"].append(f"NPC_UPDATES target not found: {name}")
                continue
            patch = {}
            for field in ("description", "background", "notes"):
                new = _append(row.get(field), self.adv, upd.get(f"{field}_append", ""))
                if new is not None:
                    patch[field] = new
            adds = [s for s in (upd.get("contact_skills_add") or []) if s not in (row.get("contact_skills") or [])]
            if adds:
                patch["contact_skills"] = list(row.get("contact_skills") or []) + adds
            if "organization" in upd:
                oid = self._org_id(upd["organization"]) if upd["organization"] else None
                if row.get("organization_id") != oid:
                    patch["organization_id"] = oid
                    patch["is_independent"] = oid is None and upd["organization"] is None
            patch.update({k: v for k, v in (upd.get("set") or {}).items() if row.get(k) != v})
            if patch:
                self._do("npc-update", "PATCH", f"/characters/{row['id']}", patch, name)
                if "name" in patch:
                    self.chars[patch["name"].lower()] = {**row, **patch}
            else:
                self.report["skipped"].append(f"npc already updated: {name}")


# -- prep doc ------------------------------------------------------------------------------------
def render_doc(spec) -> str:
    adv = spec.ADVENTURE
    lines = [f"# {adv} -- Adventure Prep: NPCs, Locations, Organizations, Matrix Systems", ""]
    lines.append(f"Source: {getattr(spec, 'SOURCE', '?')}. Campaign order #{getattr(spec, 'ORDER', '?')}, "
                 f"in-game {getattr(spec, 'YEAR', '?')}.")
    lines.append("")
    lines.append(f"Everything below is loaded into the campaign DB flagged `is_active: false` and "
                 f"`source_adventure: \"{adv}\"` by `python scripts/adventure_ingest/run.py "
                 f"{getattr(spec, 'SLUG', '<slug>')}`; flip entries active as the party meets them. "
                 f"Use the **Adventure** filter on the manage pages to see just this set.")
    lines.append("")
    if getattr(spec, "SYNOPSIS", ""):
        lines += ["## Plot synopsis", "", spec.SYNOPSIS.strip(), ""]
    if getattr(spec, "TIMELINE", ""):
        lines += ["## Timeline", "", spec.TIMELINE.strip(), ""]

    npcs = getattr(spec, "NPCS", [])
    if npcs:
        lines += ["## NPCs (Persons of Interest)", "", "| Name | Role | Org |", "|---|---|---|"]
        for c in npcs:
            lines.append(f"| {c['name']} | {c.get('role') or c.get('title') or ''} | {c.get('organization') or 'independent'} |")
        lines.append("")
    locs = getattr(spec, "LOCATIONS", [])
    if locs:
        lines += ["## Locations", "", "| Name | Type | District | Notes |", "|---|---|---|---|"]
        for l in locs:
            lines.append(f"| {l['name']} | {l.get('location_type') or ''} | {l.get('district') or ''} | {l.get('summary') or ''} |")
        lines.append("")
    orgs = getattr(spec, "ORGS", [])
    if orgs:
        lines += ["## Organizations (new)", "", "| Name | Type | Tier | Notes |", "|---|---|---|---|"]
        for o in orgs:
            lines.append(f"| {o['name']} | {o.get('org_type') or ''} | {o.get('tier', 1)} | {o.get('summary') or ''} |")
        lines.append("")
    upd = getattr(spec, "ORG_UPDATES", {})
    if upd:
        lines += ["## Existing organizations updated (sourced appends, nothing overwritten)", ""]
        for name, u in upd.items():
            bits = []
            if u.get("description_append"):
                bits.append("profile")
            if u.get("notes_append"):
                bits.append("GM notes")
            if u.get("leadership_add"):
                bits.append("leadership: " + ", ".join(e["name"] for e in u["leadership_add"]))
            if u.get("allies_add"):
                bits.append("allies: " + ", ".join(u["allies_add"]))
            if u.get("enemies_add"):
                bits.append("enemies: " + ", ".join(u["enemies_add"]))
            lines.append(f"- **{name}** -- {'; '.join(bits)}")
        lines.append("")
    lupd = getattr(spec, "LOC_UPDATES", {})
    nupd = getattr(spec, "NPC_UPDATES", {})
    if lupd or nupd:
        lines += ["## Existing locations / NPCs updated", ""]
        for name, u in lupd.items():
            extra = f" (corrected: {', '.join(u['set'])})" if u.get("set") else ""
            lines.append(f"- location: **{name}**{extra}")
        for name, u in nupd.items():
            extra = f" (corrected: {', '.join(u['set'])})" if u.get("set") else ""
            lines.append(f"- NPC: **{name}**{extra}")
        lines.append("")
    tags = getattr(spec, "TAG_EXISTING", {}) or {}
    if any(tags.values()):
        lines += ["## Pre-existing rows tagged to this adventure", ""]
        for key in ("orgs", "locations", "npcs"):
            if tags.get(key):
                lines.append(f"- {key}: " + ", ".join(tags[key]))
        lines.append("")
    if getattr(spec, "MATRIX_HOSTS", ""):
        lines += ["## Matrix systems -- to build in the Matrix designer (NOT built yet)", "", spec.MATRIX_HOSTS.strip(), ""]
    if getattr(spec, "NOT_BUILT", ""):
        lines += ["## Flavor / not built", "", spec.NOT_BUILT.strip(), ""]
    if getattr(spec, "PLAY_NOTES", ""):
        lines += ["## GM play notes", "", spec.PLAY_NOTES.strip(), ""]
    return "\n".join(lines) + "\n"
