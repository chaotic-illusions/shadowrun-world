# Manage Pages -- Auto-Save Redesign (session handoff)

Branch `worldstate-2pane`. Apply the world-state **auto-save** behavior (debounced save,
no Save/Cancel buttons) to the four CRUD admin pages. **No 2-pane** here -- the user
confirmed the existing single-modal layout stays exactly as-is; only the save mechanic changes.

## Goal (user)
- Auto-save replaces the modal's **Save** + **Cancel** buttons with a quiet status line.
- A brand-new record is **created (POST) as soon as the required field(s) are valid**, then
  every later edit silently **PATCH**es. Keep the **Delete** (and Unclaim) buttons + close x.
- Keep the existing fade-in/out modal transitions and the existing layout untouched.
- Build/dial-in on `*-preview.html` copies before replacing any live page.

## Shared infrastructure (additive -- safe for live pages, which don't call it)
- `frontend/shared.js` -> `makeManageAutoSave(cfg)`: debounce + status line + create-then-PATCH.
  cfg = `{ overlayId, statusId, foot(), idleMsg, active(), valid(), editingId(), commit(isCreate) }`.
  Listens for `input`/`change` bubbling inside `#overlayId`; `arm()` on modal open, `disarm()` on close.
- `frontend/style.css` -> `.ws-save-status` (+ `.saving/.error/.idle` color states).

## Per-page wiring pattern (what each preview does)
1. Footer: remove the green Save/Submit button + the ghost Cancel button; keep Delete (+ Unclaim).
2. Split the old save fn into `xPayload()` (pure payload) + `commitX(isCreate)` (POST/PATCH,
   no modal close, no full reload). On create: set `editingId`, show Delete, flip the title.
   Silent list refresh = update the local array + `applyFilter()` (poll is paused while open).
3. `openModal` -> `xAutoSave.arm()`; `closeModal` -> `xAutoSave.disarm()`.
4. Custom controls that write a value WITHOUT a native input/change event need a manual
   `xAutoSave.schedule()` nudge (guarded `typeof` since some run at load -> declare the autosaver
   with `var`, not `const`, to avoid the temporal-dead-zone throw).

## Required-for-create field(s) per page (from app/schemas/*.py)
- RTG: **code + region** (both non-null in `RTGCreate` -- the live page never enforced region!).
- Location / Organization / Character: **name** only (NPC also needs **title**, client-side rule).

## TODOs
- [x] Shared `makeManageAutoSave()` in shared.js + `.ws-save-status` CSS in style.css.
- [x] `manage-rtgs-preview.html` -- valid = code+region; tested.
- [x] `manage-locations-preview.html` -- valid = name; tested.
- [x] `manage-characters-preview.html` -- PC/NPC modes, reputation side-save + schema-drift guard
      preserved, contact-links unlock on create, connection-picker has a manual `schedule()` hook,
      NPC title gating; tested. (`charAutoSave` declared `var`.)
- [x] `manage-organizations-preview.html` -- nested leadership/telecom/host tables, tier dots +
      removeRow have manual `schedule()` hooks, relationship/reveal checkboxes via native change,
      `commitOrg` deliberately does NOT call renderOrgChecks (would reset in-progress checkboxes);
      tested. (`orgAutoSave` declared `var`.)
- [x] Playwright coverage: `_sr_e2e/manage-autosave.spec.js` (4 specs, all green on :8000) --
      create-on-first-valid, silent PATCH on edit, API-verified persistence, delete, NPC gating,
      org tier-dot hook, zero page JS errors.
- [x] UI tweaks (round 2, on the previews + global CSS):
      - **Table headers not-bold globally**: added `font-weight: normal` to `.manage-table th` and
        `.lead-table th` in style.css (they computed to 700; now 400 everywhere -- affects live too,
        as requested). Covers every column header on the touched manage pages + their modal tables.
      - **Org Matrix-host row** (manage-organizations-preview): security VALUE swapped from a
        `<select>` to an `<input type=number min=2 max=14>` (gets the shared in-field stepper via
        `initNumSteppers`); RTG `<select>` now shows **code-only when collapsed**, full "code -- region"
        when open (`setupRtgDisplay`, mirrored from world-state); RTG column shrunk to 96px and the
        freed width given to Description. Verified host persists `san_access_rating` "Color-N".
      - **RTG modal** (manage-rtgs-preview): security VALUE `<select>` -> `<input type=number>` spinner;
        openModal sets `.value` instead of building options. Persists "Color-N".
      - Tests: `_sr_e2e/manage-uitweaks.spec.js` (3 specs) + the original 4 -- all 7 green.
- [x] UI tweaks (round 3, previews + global CSS):
      - **Spinner/select height match**: in `.lead-table` (org modal tables), selects kept the taller
        base `9px` padding while inputs/number-spinners used `6px` -> 35px vs 28px. Added
        `.lead-table td select { padding:6px 22px 6px 8px; font-size:var(--fs-md); background-position:right 7px center }`
        so every control in the host/telecom rows is a uniform 28px. (RTG modal already matched at 35/35.)
      - **Org host columns**: RTG `<select>` widened 96->128px so `NA/UCAS-SEA` shows fully without the
        arrow overlapping; fixed columns set to `width:1px;white-space:nowrap` and Description to
        `width:100%` so the slack collapses into Description; `padding-right:18px` on the security cell
        adds separation before Visibility.
      - **Characters reputation**: Street Cred / Notoriety / Public Awareness / Heat now share one row
        via a new `.grid4` (added to style.css); removed the heat side-label (`#f-heat-label`, guarded in
        updateRepPreview -- heat tier still shows in the Rep preview line) and the per-field sub-captions.
      - Regression: all 7 specs (`manage-autosave` + `manage-uitweaks`) still green.
- [ ] **User review of the four previews on http://localhost:8000/ui/manage-*-preview.html.**
- [ ] After approval: port each preview's changes onto its live page (the shared.js/style.css
      infra is already in place, so promotion = apply the per-page edits to the live files).

## Test setup
`_sr_e2e/manage-autosave.spec.js`, baseURL overridden to `http://localhost:8000`, admin token
injected into localStorage via `addInitScript`. Run: `cd _sr_e2e && npx playwright test
manage-autosave.spec.js --workers=1`. The tests create + delete their own throwaway records
(names/codes prefixed `ZZ`).

## Notes / gotchas
- `apiFetch` (shared.js) already sets `Content-Type` when a body is present -- commit fns omit it.
- Status span is injected once by `arm()` (idempotent); for org/loc edit-of-existing, `arm()` is
  re-called after the async populate so the status reflects the loaded (valid) form.
