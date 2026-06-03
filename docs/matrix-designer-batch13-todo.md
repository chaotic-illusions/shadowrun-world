# Matrix Designer -- Batch 13 TODO (session handoff)

Live work on branch `matrix2-designer-3pane` (uncommitted). Test harness: `_sr_e2e/md3-shell.spec.js`
via `md3.config.js` (server on :8771, page at `/ui/matrix-designer.html`). Update this file after EACH step.

## Tasks
- [x] **1. Host-select dropdown not fully populating** -- INVESTIGATED: not a fixable ancestor-CSS cause.
  - Ruled OUT a CSS trigger: walked the full ancestor chain of `#hostSelect`
    (`body > main > .md3-panes(grid) > .md3-center > #wStep1.wstep.active > .mx-panel > .mx-field > flex div`).
    None carry `transform`/`filter`/`backdrop-filter`/`will-change`/`perspective`/`contain`/`zoom` in the
    normal builder state. (The only `filter:` on `<main>` is gated behind the transient
    `body.deck-interrupt-active` overlay class -- not active during host selection.)
  - Ruled OUT letter-spacing on `option`/`select` (base `select` rule + `#hostSelect` have none).
  - Remaining contributors are inherent to the **native popup**: (a) the list is built from multiple
    `<optgroup>`s (Configured Hosts + one per org across the whole LTG catalog) -> a tall popup whose
    off-screen rows Chromium lazy-paints blank until scrolled; (b) the font is a swap-loaded webfont
    (`Share Tech Mono` via Google Fonts `@import ... display=swap`), which native popups snapshot before
    the swap lands. Neither is reliably fixable with CSS on the native `<select>`.
  - CONCLUSION (per the "don't guess" guidance): this is the native Chromium select-popup bug. The real
    fix is a **custom dropdown** (renders our own option list in-DOM so CSS/fonts apply and rows paint
    eagerly) -- tracked as a separate task, NOT attempted here.
- [x] **2. Remove auto-forward to Step 2** -- `onHostChange` now calls `gotoStep(1)` (stays on Identity,
  still refreshes nav/sheaf). `createHost` keeps its `gotoStep(2)` (creating a host still advances).
- [x] **3. Remove the `ID # // <SC>-<SV>` label** -- deleted `#hostMeta` element + all 3 assignments
  (onHostChange load, onHostChange !id branch, post-save refresh). Summary pane still shows the data.
- [x] **4. Trap IC chip "trap" badge** -- added `<span class="ic-trap-badge">trap</span>` (magenta #ff5599,
  dashed border) to the trap_ic chip, matching the construct/party/bouncer badge style. CSS at style.css.
- [x] **5. Focus newly-added IC in the inspector** -- `_stepAddIc` + `_stepAddComposite` now call
  `inspectEvent(si, ei)` on the new event (opens IC editor / composite editor) instead of `inspectStep(si)`.
  (The center add-row `commitAddEvent` already did this via `_addAndInspect`.)
- [x] Re-run Playwright -- **ISSUES 0, 1 passed**. Had to update the spec's step 7 / 7b: they still
  asserted the OLD "palette add stays in the step inspector" flow, which task 5 deliberately changed
  (palette add now focuses the new event's editor). New assertions: `paletteAdd.focusedEditor`
  (construct editor opens, title "Construct") and `icAdd.focusedEditor` (`#icEditRating` present).

## Tasks (follow-up pass)
- [x] **6. Trap IC pieces wear the trap colour** -- both surface + hidden pieces (dots + text) now render in
  the trap magenta `#ff5599` (like a Party's components all share the party cyan), instead of their
  individual IC-category colours. `renderEventHTML` trap_ic branch: `trapColor='#ff5599'`. Verified by a
  one-off check: `Probe-5` / `Killer-6` both `rgb(255,85,153)`, dots magenta.
- [x] **7. Drop the `[R]`/`[P]` IC-mode label inside Trap chips** -- removed the `[R]` span from the trap_ic
  chip (the surface-IC reactive tag); the `trap` badge already conveys it. Verified `hasRP:false`.
- [x] **8. Composite editors auto-save (no Save/Cancel)** -- Trap / Bouncer / Construct / Party inspectors are
  now REAL-TIME like the plain-IC and paydata inspectors. New `_inspCommitComposite` (soft commit of the
  draft -> event, in-range numbers only, no blocking alerts) + `_inspApplyComposite` (wired to each numeric/
  text field's `oninput` + the expert/surface selects, applies without re-render so the field keeps focus);
  `_inspReRender` now live-commits + auto-saves before redrawing (covers toggles / selects / add-remove
  component). Save/Cancel rows replaced by a red **Remove <type>** button (`_inspRemoveComposite`). Deleted
  the dead `_inspSaveConstruct/Party/Trap/Bouncer`, `_inspCancel`, `_inspCloseCustom`, and the `_inspCtx.isNew`
  discard path. Spec PHASE3 rewired: edits dispatch `input` (no Save), asserts `noSaveCancel`+`hasRemove`
  per composite and that threat=1 / trapHidRtg=8 / bouncerSv=11 land live. Playwright **ISSUES 0**.
- [x] **9. Trap IC option tags coloured + slash-separated on the HIDDEN IC** -- the hidden IC's options
  fold into its label slash-joined in the trap magenta (e.g. `Lethal-8/Armor/Shielding/Cascade`), like a
  Party's per-component defenses, so it's clear the options belong to the hidden IC (the surface IC carries
  none). Dropped the separate `.ic-opt-badge` chips for trap. Verified live: surface `Probe-5`, hidden
  `Lethal-8/Armor/Shielding/Cascade`, both `rgb(255,85,153)`.
- [x] **10. Custom in-DOM host dropdown -- BUILT** (replaces the native `<select>` blank-rows popup). Kept
  the native `<select id="hostSelect">` as the hidden data model (`renderHostDropdown` + every `.value`
  read/write + `onHostChange` untouched). New `.md3-cdd` button + `#hostSelectPanel` listbox built fresh
  from the select's optgroup/option tree on open; `_pickHostOption` writes `select.value` + dispatches
  `change` (-> onHostChange) + closes; keyboard nav (Up/Down/Home/End/Enter/Esc) + single-key type-ahead +
  outside-click close; `refreshHostSelect` syncs the button label (called from `renderHostDropdown` and after
  each programmatic `.value=`). CSS under `.md3` in style.css. Spec section 3b asserts native hidden, label
  sync, grouped rows render, current marked, pick sets value + fires change + closes. Playwright **ISSUES 0**;
  screenshot `_sr_e2e/md3-host-dropdown.png`.

- [x] **11. Custom dropdown applied to ALL designer selects** (user: "can that be a style for all
  dropdowns?"). Not pure CSS -- a native `<select>` popup can't be reskinned -- so the task-10 component was
  generalized into a reusable enhancer: `enhanceSelect(sel)` hides the native select (kept as data model),
  copies its layout-only inline styles (width/flex/margin/font-size) to a `.md3-cdd` wrapper, and builds the
  button + listbox; `initCustomDropdowns()` enhances all current `.md3 select`s and a MutationObserver
  auto-upgrades any injected later (inspector/editor selects rebuilt via innerHTML). State keyed on the
  element (`sel._cdd = {wrap,btn,label,panel,placeholder}`); generic `cddOpen/Close/Toggle/Sync/_cddPick/
  _cddKey`. `refreshHostSelect` is now a 1-line shim to `cddSync($('hostSelect'))` (host integration sites
  unchanged). Opt-out hook: `data-native` on a select. Scope: designer only (`.md3`); coverage: every select.
  CSS font-size inherits so compact rows stay compact; disabled selects render a disabled button. Spec 3b
  asserts hostSelect + a 2nd static select (secCode) are both enhanced; verified 10/10 selects on the
  Security step + both Trap-editor selects enhanced (screenshots md3-dd-security/-trap.png). Playwright **ISSUES 0**.

- [x] **12. Consistent text-input height across the designer** (user: named-piece text fields were shorter
  than the Intrusion Difficulty dropdown / ACIFS). Root cause: the Access/Slave/paydata add inputs +
  notes textarea had inline `font-size:.7rem;padding:4px 6px` (~23px) while the dropdown is ~30px. Fix:
  new `.md3 input[type=text]/[type=date]/textarea { font-size: var(--fs-md); padding: 7px 10px; }` (==
  the custom-dropdown button height) + `.md3 #mdInspector input[type=text]` override (beats the compact
  `#mdInspector input` rule); removed the inline font-size/padding from newAccessPiece/newSlavePiece/pdName/
  newHostNotes. Left untouched ON PURPOSE: **number inputs** (`.infield-num-wrap` reserves `padding-right:28px`
  for the +/- stepper -- a `padding` shorthand would overlap them; ACIFS/secValue are the user's "nice"
  reference) and the **inline-rename micro-inputs** (`inlineRenameSubPiece`, contextual in-row edits). After:
  named pieces 23->30px == difficulty dropdown (30), ACIFS 27. Playwright **ISSUES 0**.

- [x] **13. Step 4/5 control-height consistency + caret + Review-clear** (user pass):
  - Buttons that sit on an input row now match the 30px control height via a new `.md3 .md3-ctrl-btn
    { min-height: 30px; box-sizing: border-box; }` class, added to the paydata Add/Generate, the Data
    Bomb/Scramble/Worm card `+ Add` buttons, and the sheaf `+ Add Step` (removed the inline `padding:3px 9px`
    from the paydata pair). Were 19-23px.
  - Card "Rtg" number inputs were 23px (`.md3 .ic-card-add input` forced `.7rem/4px 6px`) -> dropped that
    font-size/padding; new `.md3 input[type=number] { font-size: var(--fs-md); padding-top/bottom: 7px; }`
    (vertical-only, so `.infield-num-wrap`'s reserved `padding-right:28px` for the +/- stepper is preserved)
    -> 30px. Same rule normalizes secValue/ACIFS; inspector compact numbers keep their higher-specificity
    `#mdInspector input` rule. stepCountOverride: removed its inline `padding:5px 6px;font-size:.78rem` (kept
    width:92px + center) -> 30px.
  - Caret: every dropdown already carried the `.md3-cdd-caret` (v) -- verified `_cdd` on all selects, vis=true
    on active steps (the apparent "missing" ones were just inactive/hidden steps). Bumped the caret to .82rem
    for clarity on wide controls.
  - Review-only flavor: `_showReviewFlavor` sets `_inspReviewFlavor=true`; `gotoStep` clears the inspector
    (`inspectorReset()`) when leaving the Review step so Sable's note shows only there. Spec asserts it.
  Playwright **ISSUES 0**; all step-4/5 controls measure 30px.

## Custom in-DOM dropdown -- (BUILT in task 10, generalized to all selects in task 11)
Moderate, self-contained -- ~1 focused session. Lowest-risk path: keep the existing hidden
`<select id="hostSelect">` as the data model (so `renderHostDropdown`, all `hostSelect.value` reads/writes,
and `onHostChange` keep working untouched) and build a custom visual layer over it: a button showing the
current pick + an in-DOM panel that mirrors the select's `<optgroup>`/`<option>` tree, writes back to
`select.value` and dispatches `change` on pick. ~150-250 lines JS + ~40-60 lines `.md3` CSS. Work items:
render/open/close, click-select, outside-click close, keyboard nav (Up/Down/Enter/Esc) + type-ahead, refresh on
open (or after `renderHostDropdown`), and a Playwright section (open -> groups render -> pick -> value+change
propagate -> keyboard). Main risks: keyboard/a11y parity and ensuring every existing `.value=`/`renderHostDropdown`
path repaints the custom view. This fixes the bug because the list is in-DOM (no native popup).

## Status / notes
- DONE -- tasks 2-10 implemented + verified; task 1 investigated & concluded (its fix = the custom dropdown,
  now built in task 10). Playwright green (0 issues) throughout. Spec `_sr_e2e/md3-shell.spec.js` updated for
  the task-5 focus-new-event behavior, the task-8 real-time composites, and the task-10 dropdown (section 3b).
- COMMITTED to branch `matrix2-designer-3pane`: tasks 6-10 (trap colour/options, real-time composites, custom
  dropdown) landed with the frontend files + this doc. Note the commit also carries the broader uncommitted
  3-pane port (the file had never been committed since the port began). The `_sr_e2e/` harness is not a git
  repo, so the spec changes live only on disk.
- Text-hygiene hook (tools/check_text_hygiene.py): the repo enforces ASCII-only source. JS-string glyphs in
  matrix-designer.html were converted to `\uXXXX` escapes (same rendered output); markdown glyphs to ASCII.
