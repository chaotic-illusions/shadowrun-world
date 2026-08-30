# DONE: Active/Inactive Toggles (Locations, Organizations)

**Status: implemented 2026-08-30.** This file is kept as a record of what was
built and why; the checklist below is marked up with what actually happened
(a few decisions differ from the original proposal — noted inline).

Prompted by prepping the *Mercurial* adventure: Locations and Organizations need
to support "exists in the world but hasn't been discovered/introduced yet,"
the same way NPCs/Contacts already support "exists but is currently inactive."

## Current state (confirmed by reading the code, 2026-08-30)

The "good" pattern already in use, which we want everything to match:

> **A boolean column + an immediate, scoped `PATCH` fired from a single inline
> control (button or checkbox), with no modal and no full-form round trip.**

Concrete examples of the good pattern today:
- **Characters (PCs/NPCs)** — `Character.is_active` (`app/models/character.py:128`).
  UI: `.card-active-btn` on each card in `frontend/world-state.js`
  (`toggleCharActive()`, line 555) — one click, `PATCH /characters/{id}`
  with just `{is_active: !isActive}`.
- **Contacts** — `Contact.is_active` (`app/models/contact.py:24`). Same
  one-click card button pattern, `toggleContactActive()` (`world-state.js:565`).
- **Matrix Hosts** — `MatrixHost.is_visible_to_players`
  (`app/models/matrix_host.py:30`). UI: inline checkbox in the registry table
  (`frontend/matrix-designer.html`, `mhSetVisible()`, line 1686) and a detail-view
  button (`toggleHostVisibility()`, line 1275). Both PATCH immediately.
  **This one is already fine — no changes needed here**, per explicit ask.

### Organizations — has the column, UI is the problem
- `Organization.is_active` already exists (`app/models/organization.py:35`,
  default `True`), and the schema (`app/schemas/organization.py`) already
  carries it through Create/Update/Read.
- The UI toggle lives *inside* the big edit modal in
  `frontend/manage-organizations.html` (`#is_active` checkbox, "Operational
  Status", lines ~145-154).
- `updateStatus()` (line 341) only updates the on-screen label — it does
  **not** persist anything by itself. Persisting the flag requires clicking
  through the entire org form (Core Identity, Intel Profile, Command
  Structure, Political Relationships, Runner Affiliation, RTG/LTG network
  editor) and hitting **"Submit to Database"**, which PATCHes the whole
  organization payload (`submitForm()`, line 863) just to flip one boolean.
- There's no quick in-row toggle in the org table itself.

### Locations — no flag exists at all
- `Location` model (`app/models/location.py`) has no `is_active`,
  `is_visible`, or "discovered" concept whatsoever.
- Locations are all-or-nothing: they exist, or an admin hard-deletes them
  (`frontend/manage-locations.html`, `DELETE /{id}`). There is currently no
  way to pre-create a location and keep it hidden from players until it's
  discovered in play.

## Work done

### 1. Organizations — UI-only fix (no schema/migration needed)
- [x] Added an inline `chk-reveal` checkbox toggle directly in the
      organizations table row (`manage-organizations.html`), replacing the
      old plain "ACTIVE"/"INACTIVE" text label. `toggleOrgRow()` PATCHes
      just `{is_active}` immediately — no modal.
- [x] Added the matching one-click `.card-active-btn` + inactive overlay to
      the org card in World State (`buildOrgCard()` / `toggleOrgActive()` in
      `world-state.js`), matching the Character/Contact card pattern exactly.
- [x] Left the "Operational Status" checkbox inside the big edit modal as-is
      (secondary control) — matches how Characters keep both a card button
      *and* a modal checkbox.
- [x] **Went further than "confirm" — added real server-side enforcement.**
      `GET /organizations/` and `GET /organizations/{id}` now hide inactive
      orgs from non-admins at the query level (404 on direct fetch), mirroring
      the existing Character privacy pattern (`_is_privileged_view`). Before
      this, `is_active` only ever controlled client-side rendering — any
      player could see "hidden" orgs via devtools/network tab. Also fixed a
      pre-existing bug: World State's org section filtered out inactive orgs
      **even for admins**, so a GM had no way to see/re-toggle a deactivated
      org from that page at all.

### 2. Locations — new field
- [x] Added `is_active` (bool, **default `True`**, not `False` as originally
      proposed) to `Location` model. Reasoning: this matches the
      Character/Organization convention (new records start active), and the
      migration backfills existing rows to `True` via `server_default` so
      nothing that was already visible gets silently hidden. New
      *prep-only* content (like the Mercurial locations) is created with
      `is_active: false` explicitly at insert time instead of relying on a
      different default.
      - Named `is_active`, not `is_discovered` — kept consistent with
        Character/Contact/Organization rather than matching Matrix Host's
        `is_visible_to_players`, so three of the four toggleable entity
        types share one field name and one PATCH shape.
- [x] Alembic migration: `alembic/versions/a3f5c92e0d17_add_location_is_active.py`.
- [x] Startup-guard `_ensure_location_is_active_column()` added to
      `app/main.py` per the project's documented convention (AGENTS.md §4) —
      this DB was already behind on other pending migrations, so the guard
      is what actually patched the live schema in practice.
- [x] Added to `app/schemas/location.py` (Base/Create/Update/Read/Summary).
- [x] Added the same inline `chk-reveal` toggle to `manage-locations.html`'s
      table rows, plus a Status filter dropdown matching Organizations'.
- [x] Added the card-button + overlay treatment to the location card in
      World State (`buildLocCard()` / `toggleLocActive()`).
- [x] **Server-side enforcement added here too** — `GET /locations/` and
      `GET /locations/{id}` now 404/exclude inactive locations for
      non-admins, same as Organizations above.
- [x] GM workflow confirmed and used: all 7 new Mercurial locations were
      bulk-loaded as `is_active: false` via a one-off script against the
      live API, ready to flip active as the party discovers each one.

### 3. Consistency pass
- [x] Decided during implementation (see Locations note above): went with
      unified `is_active` naming across Character/Contact/Organization/
      Location. Matrix Host keeps its own `is_visible_to_players` name
      untouched, since it was explicitly out of scope and already works well.

## Verification
- Full test suite: `1827 passed` (was 1818; +9 from the code-review follow-up
  below).
- Manually verified end-to-end against the live dev DB with a throwaway
  player token: player list/detail requests correctly exclude/404 inactive
  orgs and locations; admin requests see everything; the PATCH toggle
  flips visibility immediately in both directions.
- `/full-code-review` run against this diff (two independent audits +
  manual verification) found two real gaps beyond the toggle work itself:
  1. `GET /adventure-logs/{id}` doesn't redact concealed location/org names
     in `locations_involved`/`orgs_involved` — reviewed and **accepted as a
     non-issue**: adventure logs are post-run summaries, so anything logged
     already happened in play and isn't a real spoiler risk.
  2. `GET /matrix-hosts/ltg-catalog` had no `is_active`/visibility filtering
     at all, so a concealed org's name/address would leak the moment a
     Matrix host got attached to it — **fixed** in
     `app/routers/matrix_hosts.py::ltg_catalog`, mirroring
     `organizations._serialize_org`'s existing redaction. Regression tests
     added to `tests/test_host_security_visibility.py`.
  3. No automated regression tests existed for the new Location/Organization
     gating (only manual curl checks) — **fixed**, added to
     `tests/test_world_visibility.py` mirroring the existing Character
     pattern.

## Explicitly out of scope
- Matrix Host visibility toggle — already works well, don't touch it.
- Nuyen enforcement, Essence/Body Index enforcement — unrelated, tracked
  separately (see memory).
