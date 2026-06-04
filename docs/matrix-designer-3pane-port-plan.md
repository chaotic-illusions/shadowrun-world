# Matrix Designer 3-Pane Port -- Line-by-Line Audit Plan

## [x] BATCH 12 (COMPLETE, 2026-06-03) -- readability/contrast pass (style.css, scoped .md3), green
User: important labels/buttons were too dim/small; dim grey should be explanation text only. All in style.css.
- [x] **Ghost buttons** (Create Custom Host / Cancel / + Add / + Add Step) -- `.md3 .btn-ghost` now bright
  text (`--text-bright`) + green outline (was `--text-dim` on `#222`).
- [x] **Sheaf-inspector palette labels** (White/Gray/Black IC, Composite) -- `.md3-pal-lbl` bumped to
  `--fs-sm`, bold, steel-blue `--md3-label` (was `--fs-xxs` dim grey).
- [x] **Trigger row** -- new `.md3-trigger-lbl` (matches the input's `--fs-sm`, not the tiny uppercase
  section label); dropped the `>=`; stepper now ATTACHED via `.md3 #mdInspector .infield-num-wrap:has(.md3-num){width:72px}`
  (the `.md3-num` width is class-based so initNumSteppers couldn't size the wrap -- pinned in CSS). Verified wrapW=72, ctrls flush.
- [x] **Inspector section labels** -- `.md3-insp-label` bumped `--fs-xxs`->`--fs-xs` + bold.
- [x] **Smallest text floor** -- scoped token bump `.md3 { --fs-xxs:0.62rem; --fs-xs:0.68rem }` so tiny
  tips/badges (e.g. the Generate-Sheaf hint) are readable. Other pages unaffected.
- [x] **Step Count label** -- de-inlined: replaced inline `font-size:.58rem;color:--text-dim` with a new
  reusable `.md3 .md3-field-lbl` (steel-blue, readable) -- the pattern to promote app-wide later.
- [x] Playwright green (only the intermittent favicon 404). Screenshots confirm all four areas.
NOTE (answer to user's meta-Q): all style changes live in **style.css** under `.md3`, NOT inline. The HTML
still carries a backlog of inline `style=` attrs from earlier phases; future work = promote `.md3` rules to
an app-wide baseline + strip inline styles. `.md3-field-lbl` is the first step of that de-inlining.

## [x] BATCH 11 (COMPLETE, 2026-06-03) -- Trace-tree removal + center-aligned tabs + legacy audit, green
- [x] **Removed the Trace IC decision tree entirely** (user: the run side already resolves trace success;
  just add a Trace IC and let the run handle it). Deleted `step.trace_branch` rendering, `_stepTraceBranch*`/
  `_traceIcCount`/`_traceBranchCount`/`_hasEarlierTraceIc`/`_stepTraceBranchSection`/`renderTraceBranchHTML`/
  `_branchAddOptions`, the inspectStep section, the click-handler branch, and all `.trace-branch-*` CSS. Legacy
  `trace_branch` data is stripped on load. (Note: the legacy file ALSO had this feature -- its removal is a
  deliberate scope cut, not a regression.)
- [x] **Tabs aligned to the center pane** via a `.md3-tabbar` grid that mirrors `.md3-panes`
  (`248px / 1fr / 360px`), strip placed in column 2 -- measured stripLeft/Right == centerLeft/Right (286/1102).
- [x] **Always one tab**: the current host is shown as tab 1 (`_syncCurrentHostTab`, called from `onHostChange`
  + `createHost`); the lone root tab has no close button; following adds more. Pulse retained.
- [x] **Legacy functional audit** (live vs `matrix-designer.legacy.html`): function-name diff (155 legacy /
  236 live) -- only trace-branch (intentionally removed) + renamed paydata helper differ; API endpoints
  identical; save-payload fields identical incl. `trap_doors_json`; all key feature fns present; LTG-security
  sync present (inline). **No functional gaps** beyond the deliberate Trace-tree removal.
- [x] Playwright green, ISSUES 0 (spec section 11 now asserts the Trace tree is gone; 11e asserts always-one-tab
  + no-close lone tab + center-pane behavior + step restore).

## [x] BATCH 10 (COMPLETE, 2026-06-03) -- user visual-feedback pass, Playwright green (ISSUES 0)
Six items from a hands-on review. Spec `_sr_e2e/md3-shell.spec.js` updated; chip-height + button verified by measurement ([22,22,22]; Follow btn bg transparent / text+border cyan).
- [x] **1. Uniform chip height** -- `.md3 .sheaf-events { align-items: stretch }` so every chip in a step matches the tallest (e.g. a chip carrying an EXP/option badge). No magic numbers.
- [x] **2. Follow button** -- `.btn-follow` is now outlined cyan (transparent bg, cyan border + text), matching the prototype `.btn-cyan` (was solid blue / black text).
- [x] **3. Host tabs more striking + state preserved** -- active tab gets a cyan top-accent + glow; a freshly-followed tab plays a `@keyframes md3-tab-flash` (`.htab.justadded`); follow banner is a cyan-railed callout. **State:** each tab stores its `wizardStep` (`_saveCurrentTabStep`/`_restoreTabStep`); following stashes the source step and returning restores it (no more snap-back to Step 2).
- [x] **4. Combined hover** -- the trigger badge and step card open the same (step) inspector, so they now highlight **together** on hover (`:has()`-guarded so a chip/branch hover doesn't co-light the trigger) and on selection (`.sheaf-step:has(.trigger-badge.md3-sel)`).
- [x] **5. Trace Branch -> step-level, gated** (reverses Batch 9 K's "branch on the Trace IC event"). Branch now lives on `step.trace_branch`, offered from the **step inspector** of a step that comes AFTER a Trace IC fires, capped 1:1 to the number of Trace ICs in the sheaf (`_traceIcCount`/`_traceBranchCount`/`_hasEarlierTraceIc` + `_stepTraceBranchSection`/`_stepAddTraceBranch`/`_stepTraceBranchAdd`/`_stepTraceBranchDel`/`_stepRemoveTraceBranch`). Sheaf shows it read-only; clicking the block opens that step's inspector. Removed the IC-editor branch hook (`_renderIcTraceBranch`/`_icTraceBranchInner`/`_trace*`).
- [x] Playwright green, ISSUES 0 (new spec section 11 = step-level gated branch incl. cap + block-click->step; 11e adds the source-step-restore assertion).

## [x] BATCH 9 (COMPLETE, 2026-06-03) -- polish + Trace-branch redesign + tabbed Follow, Playwright green
Spec: `_sr_e2e/md3-shell.spec.js` (baseURL :8771, `/ui/matrix-designer.html`). All 12 items done + verified.
- [x] **A.** Removed the `[x]` (event-remove-btn) from sheaf IC chips -- removal lives in the IC inspector.
- [x] **B.** Boundary box per sheaf IC chip (`.sheaf-event` 1px border + inline per-category `border-color`).
- [x] **C.** `--md3-label:#5aa8d0` (style.css 2871) drives summary `.k`/`.sum-thr-label`, inspector `.md3-insp-label`, trigger `.t-lbl`.
- [x] **D.** Data-bomb uniqueness: `_rebuildTargetDropdowns` excludes devices already carrying a Data Bomb (no alert).
- [x] **E.** Scramble variant driven by target -- `onScrTargetChange` shows Poison only for `Files - entire`, else Exploding only; target list is the variant-independent exploding superset.
- [x] **F.** Trap-door/slave inspector uses `.follow-card` (Hidden: Yes -- until Analyzed; dest card; Follow inside). No confirm popup (`_inspFollowTrapDoor` is non-destructive -- edits auto-save).
- [x] **G.** `#saveStatus` text removed (element gone; `_setSaveStatus` no-ops). Auto-save is silent. Spec asserts `noStatusEl`.
- [x] **H.** Review **RUN-READY** Status pulses (`.md3 .rev-cell .v.good` -> `@keyframes md3-runready-pulse` 2s).
- [x] **I.** Sheaf trigger badge = "Trigger" + big colored number (`.trigger-badge b`, `--green`, `--fs-2xl`).
- [x] **J.** Whole `.sheaf-step` clickable -> `inspectStep`; precedence chip -> trace-block -> step (global handler ~3120).
- [x] **K.** Trace-branch lives on the **Trace IC event** (`ev.trace_branch`), edited from the IC editor (`_renderIcTraceBranch`/`#icTraceBranch`); sheaf shows it read-only (`renderTraceBranchHTML`, clickable -> owning Trace IC). Dead step-level branch code already gone.
- [x] **L.** Tabbed trap-door Follow -- in-app host tabs (`#hostTabs`/`#followMsg`, prototype `.hosttabs`/`.htab`/`.followmsg`). `_inspFollowTrapDoor` opens the dest as a new tab (`_hostTabs`, `via`=source piece); `switchHostTab`/`closeHostTab` drive `currentHost` via `onHostChange` (auto-save makes it safe); strip shows only at >=2 tabs; closing the active tab returns to source. `_followPending` flag tells `onHostChange` a load is a follow (keeps the chain) vs a plain dropdown pick (resets to a single root tab).
- [x] Playwright green (all 12 spec sections pass; only a benign favicon-style 404 logged). Memory `project_matrix_designer_3pane_port.md` updated.

**Where I stopped:** BATCH 9 complete. Nothing committed yet (all 3-pane port work is still uncommitted in `frontend/matrix-designer.html` + `frontend/style.css`).



**Notes file:** `docs/matrix-designer-3pane-port-plan.md`
**Branch:** `matrix2-designer-3pane` (off `matrix2`). **Backup:** `frontend/matrix-designer.legacy.html`. Nothing committed.
**Template (source of truth):** `frontend/prototypes/host-builder-terminal.html` (969 lines)
**Live target:** `frontend/matrix-designer.html` (+ scoped CSS in `frontend/style.css` "SECTION 25b")
**Method the user wants:** walk the TEMPLATE top-to-bottom. For each piece: if it's missing or different in live, adjust live to match -- **without losing live functionality** (live has more real mechanics than the mock).

---

## [x] PHASE 6 (2026-06-02) -- PROTOTYPE-FAITHFUL CONTENT PORT (corrected method), Playwright green
User feedback: stop bolting inspectors onto the old layout -- **make live LOOK like the prototype and
relocate live's data into the prototype's representation**; call out anything with no prototype home.
Walked the prototype section by section and ported the look + representation (all `.md3`-scoped CSS):
- **Files** -> `.pd-row` (* key / name / `.lock` defense badge(s) / Mp) + `.pd-counters` (Bombs/Scramble/
  Worm). Per-file edit is in the inspector; inline clutter removed. Header -> "Host Files, Devices & Passive IC".
- **Named pieces** -> `.tag-pc` pills. Slave pill = name + `[TRAP DOOR]` flag -> **inspectSlaveDevice**
  (rename / Trap Door toggle / destination / Follow / remove).
- **Trap doors** (USER RULING: inspector) -> **retired Step 5**, renumbered wizard 7->6 steps; trap-door
  source = slave device, dest+Follow in the inspector.
- **Review** -> `.review-grid`/`.rev-cell` (... Status: RUN-READY). **Identity** -> LTG select moved in.
  **Alert-Triggers** -> `.alertpanel`/`.ap-row`.
- USER RULING (passive IC): the detailed subsystem/device Data Bomb/Scramble/Worm editors STAY in the
  Files section under the counters (header broadened to reflect it).
- Call-outs left (minor/decided): topbar label-color switcher (skip), multi-tab `hosttabs` (Follow =
  host-switch instead), Intrusion Difficulty preset kept (drives Quick-Fill). Spec updated to 6 steps +
  new sections; screenshots md3-paydata/-subsystems/-review/-identity/-sheaf-alert.png.

## [x] REFACTOR COMPLETE (2026-06-02, Phase 5) -- all gap #1 + audit items done, Playwright green (0 page errors)
Click-to-inspect now covers **every** sheaf element: event chips, alert chips, **paydata rows**,
**trap-door entries**, and **trace-branch chips**. New inspectors: `inspectPaydata` (size / Key / Data
Bomb / Scramble -- **retired the two `prompt()` editors**, `editPaydataDefense` is now a one-line shim),
`inspectTrapDoor` (destination + **Follow** = host-switch via `onHostChange`), `inspectBranchEvent`
(read-only branch-event detail). Flavor text present (IC editor `#icEditTip` + alert/branch/paydata
inspectors). Field/layout parity verified (SV in-field steppers via shared.js global `initNumSteppers`,
ACIFS Quick-Fill, all Security fields, single bottom Save bar). Spec `md3-shell.spec.js` extended to
sections 8-12 (chip/alert/paydata/trapdoor/branch click-to-inspect + a global "no prompt() ever" guard).
**Deliberately NOT built (out of this refactor's scope, additive features, would need their own design):**
multi-tab host chrome (`hosttabs` -- Follow already switches the host, which is the substantive behavior);
the template's in-inspector add-event *palette* (live's always-visible center add-event row is the single
source of truth -- duplicating it would fork the add logic). Identity/LTG remain separate steps (live).

## (!) Known gap the user hit first (was done FIRST)
**STATUS (2026-06-02, Phase 4): the sheaf-chip part is DONE + Playwright-verified.** A delegated
`document.addEventListener('click', ...)` now opens the Inspector when you click anywhere on a sheaf
**event chip body** (not just the pencil) -- routed by type via `inspectEvent(si,ei)` to the existing
`editIcEvent`/`inspectTrap`/`inspectBouncer`/`inspectConstruct`/`inspectParty`. **Alert chips** now
open a new read-only `inspectAlert(kind,si)` (flavor + "also on this step" list + note that alerts are
placed via the Alert Triggers panel). All chips carry `data-si`/`data-ei` (alerts also `data-alert`),
get `cursor:pointer`, and highlight with `.md3-sel`. Spec `md3-shell.spec.js` section 8 asserts this.
**STILL TODO in this gap:** `inspectPaydata` (paydata row), `inspectTrapDoor` (slave trap-door device),
trace-branch chip click. `inspectStep` (trigger) is effectively satisfied -- live's trigger is already
an inline `<input>` in the step header.

Original notes (template lines ~830-856): the global handler also covered a **trigger badge**, a
**paydata row**, a **trap-door device tag**, a **trace-branch chip**, and a **Composite palette chip**.
In live, the small **edit-pencil** buttons (`event-edit-btn`) also still open the inspector (unchanged).

**Action:** add a delegated click handler (or per-element onclick) so selecting any sheaf element shows it in `#mdInspector`, and add the missing inspectors:
- `inspectStep(si)` -- click the trigger badge -> edit trigger (min/max by neighbours) + list events + delete step. (Live has the data inline already in `renderStepHTML`; move it to the inspector.)
- `inspectAlert(kind, si)` -- click an alert pill -> show alert flavor + "also on this step" + add-IC palette.
- `inspectPaydata(name/idx)` -- click a paydata row -> size (Mp), key-file toggle, file-level Scramble/Data Bomb. **Preserve live's inline-rename + Generate.**
- `inspectTrapDoor(deviceKey)` -- click a `[TRAP DOOR]` slave device -> destination + **Follow** action (Follow itself is deferred, see below).
- Make the whole **event chip** clickable (not just the pencil) -> route by type to the existing `inspectIC`(relocated modal)/`inspectConstruct`/`inspectParty`/`inspectTrap`/`inspectBouncer`.
- Add a `.md3-sel` selected-highlight on whatever is open (helper `_markSelectedEvent` already exists; generalise it).

---

## Current state (done this session, all Playwright-verified, 0 JS errors)
- **Phase 1** 3-pane shell; **Phase 2** sheaf chip-timeline + IC editor relocated into `#mdInspector` (replaces `#icEditOverlay`); **Phase 3** Trap/Bouncer/Construct/Party EDIT in inspector (prompts retired); **3.5** composite CREATE routes through inspector; **3.6** ONE-step-at-a-time (left nav drives it; scroll-spy removed), single sticky left pane, Host Summary rebuilt to template fields, Create-Custom-Host is a button.
- See memory `project_matrix_designer_3pane_port.md`, `project_ui_conventions.md`.

---

## Test harness (bring this up first each session)
- Serve + test from an **isolated** server (the page auto-creates an admin token on first load, which breaks any bootstrap key -- so PRE-MINT a real token):
  ```powershell
  # 1. fresh isolated server (serves /ui/ live from frontend/ AND the API)
  $env:DATABASE_URL='sqlite+aiosqlite:///./data/_md3_test.db'; $env:BOOTSTRAP_ADMIN_KEY='e2etest'
  & ".venv\Scripts\python.exe" -m uvicorn app.main:app --host 127.0.0.1 --port 8771   # run in background
  # 2. mint a real admin token ONCE (bootstrap key works only until an admin token exists)
  #    POST /auth/tokens  {"label":"md3test","is_admin":true}  header X-Admin-Token: e2etest  -> save .token
  ```
- Token already saved at `D:\Code Projects\_sr_e2e\token-md3.txt`; spec `md3-shell.spec.js` + `md3.config.js` (baseURL :8771). Run: `cd "D:\Code Projects\_sr_e2e"; npx playwright test --config md3.config.js`. Page is at **`/ui/matrix-designer.html`** (NOT root).
- Kill stale server: `Get-NetTCPConnection -LocalPort 8771 -State Listen | %{ Stop-Process -Id $_.OwningProcess -Force }`

---

## Line-by-line audit checklist (template section -> live -> action)
Walk `host-builder-terminal.html` in order. `[ ]` = to verify/fix.

### CSS / tokens (template `:root`, lines 21-287)
- [ ] Confirm every template token maps to a `style.css` var (most do). Differences are cosmetic; align spacing/scale only where the live page looks off.

### Topbar (template 291-307)
- [ ] **Label-color switcher** (Steel/Dim Green/Copper/Slate) -- NOT in live. Decision pending (we chose steel-cyan). Likely SKIP unless the user wants it.
- [ ] **hosttabs / followMsg** (trap-door Follow tabs) -- NOT in live. DEFERRED (see Follow below).

### Left pane (template 318-348: Build Steps nav + summary-card)
- [x] Checkbox tick nav -- DONE. [x] Summary fields -- DONE (Name/Security/Owner/ACIFS/Paydata/Passive IC/Sheaf Steps/3 threshold pills).
- [ ] Verify nav tick semantics vs live (`done` = step < current). Template shows discrete done/active/pending -- OK.

### Center -- Identity (template 369-381)
- [ ] Template = Host Selection select + "+ Create Custom Host" button + LTG address select, in ONE block. Live splits Identity (Step 1: selection+create) and LTG (Step 2). DONE-ish; consider moving LTG address into Step 1 to match, or leave (functionality intact).

### Center -- Security Profile (template 383-394)
- [ ] Host Name / Security Code / Security Value / Owner Type. Live Step 2 has these (+ tips). Verify field parity, in-field steppers on SV.

### Center -- ACIFS (template 396-421)
- [ ] 5 cells + Quick-Fill; Access named pieces; Slave named devices (with `[TRAP DOOR]` flag). Live Step 3 has all + more (difficulty preset). Verify Slave device trap-door flag toggle still works and surfaces in the trap-door inspector.

### Center -- Hosted Files & Passive IC (template 423-441)
- [ ] Paydata rows (star=key, lock badge=protection, Mp), Generate Paydata, counters (Data Bombs/Scramble/Worm). Live Step 4 has full editors (variants, targets). KEEP live functionality; just adopt the template's row look + click-to-inspect.

### Center -- Security Sheaf (template 443-459)
- [ ] Alert-Triggers panel (Passive/Active/Shutdown selects) -- live has `#alertPlacementPanel`. [x] Sheaf timeline -- DONE.
- [ ] Make chips/alerts/trigger clickable into inspector (the FIRST gap above).

### Center -- Review & Save (template 461-475)
- [ ] review-grid + Save BELOW summary. Live Step 7 `renderReview`. Verify layout matches (Save button placement).

### Right pane -- Inspector (template 204-238 CSS, 665-827 JS)
- [ ] inspectIC [x](relocated modal) / inspectComposite [x](construct/party/trap/bouncer). MISSING: inspectStep, inspectAlert, inspectPaydata, inspectTrapDoor (see gap #1).
- [ ] Template inspector also shows **flavor text** (IC_FLAVOR) and an **add-event palette** gated by alert context -- live IC editor (relocated modal) does NOT. Consider adding flavor + palette to inspectors (nice-to-have).

### Trap-door "Follow" + host tabs (template 259-265, 800-811, 947-957) -- DEFERRED FEATURE
- [ ] Clicking a trap-door device -> inspector with destination + **Follow ->** which opens that host in an in-app tab (`hosttabs`) and swaps the center to the destination host. Net-new navigation; design before building.

### Misc still on prompts (NOT in template, live-only) -- retire later
- [ ] Data Bomb / Scramble rating editing in the Files block still uses `prompt()` (live lines ~1635-1649). Out of template scope but should become inspector/inline to match the "no prompts" direction.

---

## Guardrails (do not break -- see `project_ui_conventions`)
- No paydata price field. IC labels `Name-Rating`. Alert colors amber/red/purple persistent top-border. Security-code color-matched (Black=purple). No invented mechanics -- verify against `vr2_rules.md`. In-field number steppers fill the field.
- All new CSS stays scoped under `.md3`. Preserve every existing element ID + handler (the live JS is ~3,200 lines and ID-driven).

## Order of attack -- ALL DONE
1. ~~**Inspector click-to-select** (gap #1)~~ -- DONE (sheaf chips + alert chips, Phase 4).
2. ~~inspectAlert~~ / ~~inspectPaydata~~ / ~~inspectTrapDoor~~ / ~~trace-branch chip click~~ -- DONE (Phase 5).
   ~~inspectStep~~ N/A (trigger is an inline input).
3. ~~Field/layout parity~~ -- verified present (steppers/Quick-Fill/fields/Save bar); no rebuild needed.
4. ~~Inspector flavor~~ DONE. Add-event palette -- declined (center add-row is the single source).
5. Trap-door Follow -- DONE as host-switch. Multi-tab `hosttabs` chrome -- out of scope (additive feature).
6. ~~Retire Data Bomb/Scramble prompts~~ -- DONE (folded into inspectPaydata).
3. Field/layout parity pass (Identity/Security/ACIFS/Files/Review) per checklist.
4. Inspector flavor text + add-event palette.
5. Trap-door Follow + host tabs.
6. Retire Data Bomb/Scramble prompts.
Re-run `md3-shell.spec.js` after each; extend it with selection assertions.
