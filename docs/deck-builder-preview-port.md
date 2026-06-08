# Deck-Builder -> 3-Pane Port: functionality inventory + mapping (progress tracker)

Working file: `frontend/deck-builder-preview.html` (copy of live `deck-builder.html`).
Approved layout: `frontend/prototypes/deck-builder-3pane.html` (v2).
Live page is the source of truth and must NOT be touched until the preview is signed off.

Goal: move the visual layout to the 3-pane md3 shell WITHOUT breaking any behavior.
Method: catalogue every piece of functionality (Part A), decide its new home (Part B),
flag anything that does not obviously fit and ASK before porting (Part C), then port in
stages with a checklist (Part D). ASCII only (text-hygiene hook): use -- -> ... not unicode.

--------------------------------------------------------------------------------
## PART A -- COMPLETE FUNCTIONALITY INVENTORY (live deck-builder.html)
--------------------------------------------------------------------------------

### A0. Page shell / global
- Header + nav (standard). Page title + page-sub ("PROGRAMMER: <name>").
- `#pageAlert` element exists but alerts now route through a modal (see A12).
- `#deckBuilderApp` wraps the whole tool; toggles `deck-builder-locked` /
  `deck-builder-unlocked` based on whether a programmer profile is active.
- Tab bar: `tabBtn0` "Cyberdeck Builder" / `tabBtn1` "Program / Utility Builder"
  -> `switchTab(idx)` toggles `tabPanel0` / `tabPanel1`.
- Init (`DOMContentLoaded`): bootstrapAuth -> initProgrammerProfile -> buildUtilDropdown
  -> onUtilTypeChange -> syncProgrammingSuccessInputBounds -> calcDeck -> renderLoadPlanner
  -> renderSavedDecks -> renderSavedLoadouts -> renderSavedPrograms -> refreshPurchaseImportPreview.

### A1. Programmer Profile gate (pre-app)
- Card `#profileGateCard`: prompt tip, `#profileStatus`.
- Form area `#profileFormArea`: `#programmerCharacter` select (PCs with active
  computer/software/matrix skills), `#profileDerived` (MPCP cap | Utility cap | dominant),
  `#activateProfileBtn`.
- Summary area `#profileSummaryArea`: `#profileSummaryText`, `#profileSummaryCaps`,
  "Change Programmer" button.
- Functions: loadProgrammerCharacters, updateProgrammerProfilePreview, activateDeckBuilder,
  editProgrammerProfile, initProgrammerProfile, hasActiveDeckSkill,
  getSelectedProgrammerSkillSet, computeProgrammerCaps(FromSkillSet),
  getDominantProgrammingSkill, applyProgrammerCaps.
- Caps drive: MPCP max (floor(highestSkill x1.5), <=50), Utility max (highestSkill, <=50),
  Black Hammer/Killjoy cap (util/2), programming-successes cap (Computer B/R rating).
- Profile persisted to localStorage `sr2_deck_programmer_profile_v1`; gates server state load.

### A2. Interrupt overlay (security flavor)
- `#deckInterruptOverlay` "-- Fastjack" screen shown when a runner-token user has no
  claimed eligible PC. Functions: setInterruptOverlay, acknowledgeInterrupt (nav back),
  randomHex12, fastjackStamp.

### A3. Cyberdeck Builder inputs (TAB 0 left)
- Deck Specification: `deckName`, `deckType` (hot/cool/tortoise), `mpcp` + `#mpcpCapTip`.
- Persona Programs: `pBod`, `pEvasion`, `pMasking`, `pSensor`; live `#personaBar`
  (sum vs MPCP x3 cap). Persona ratings capped at MPCP.
- Hardware Components: `hardening` (+dynamic `#hardeningLabel` max floor(MPCP/2)),
  `respIncrease` (+dynamic `#respIncreaseLabel` max min(floor(MPCP/4),3)),
  `iccm` checkbox, `realityFilter` checkbox.
- Memory & I/O: `activeMem` (max MPCP x100), `ioSpeed` (max MPCP x Sensor x10),
  `offlineStorage` (cap 65535) -- each with dynamic label + tip.
- Accessories: `deckCasing` select (0/1/2/3), `satlink` checkbox, `hitcherJack` checkbox.

### A4. Cyberdeck calculation -- calcDeck()
- Recomputes/clamps all dynamic caps + labels/tips.
- Constraint check -> errors[]; persona-cap accounts for Reality Filter (-1 MPCP).
- `#validityBadge`: ok / err state with message.
- `#personaBar`: persona sum vs cap (warn/ok).
- Component cost rows (each: size/OCC/PLC-DTC/other/subtotal/cook/install):
  MPCP core, 4 persona programs, ASIST (hot/cold; none for tortoise), Reality Filter NOTE
  row, Hardening, ICCM, Response Increase, Active Memory (OMC), I/O Speed, Offline Storage,
  Deck Casing, Satlink, Hitcher. 10% package discount when all core present.
- Cost table rendered to `#costBody` (8 cols) + TOTAL + discount + FINAL rows.
- Deck summary `#deckSumGrid` (13 items): MPCP, Deck Type, Persona B/E/M/S,
  Persona Sum/Cap, Hardening, Response Increase (incl RF +1), Active Memory, I/O Speed,
  Matrix Reaction, Initiative (xD6+react), Hacking Pool, Detection Factor
  (Masking + loaded Sleaze), Total Cost. Uses programmer Intel/Quickness + loaded Sleaze.
- Shows/hides `#deckSummaryPanel` + `#costBreakdownPanel`; calls renderLoadPlanner.

### A5. Program / Utility Builder inputs (TAB 1 left)
- `utilType` select (grouped Operational/Special/Offensive/Defensive) via buildUtilDropdown.
- `#utilBrief` description box.
- `utilRating` + `#utilCapTip` (cap from programmer; BH/Killjoy halved).
- `attackDmgField`/`attackDmg` (only for Attack: Light/Mod/Serious/Deadly multiplier).
- GM-only: `programSuccessesInput` + "Roll Programming Task" -> programmingRollResult.
- Buttons: `saveProgramBtn` (Compile Program / Compile Upgrade), `cancelProgramEditBtn`,
  `#programEditState` (upgrade baseline banner).
- Program Options `#optionsArea` (dynamic): Variable Value Options (area/dinab/skulk with
  enable-checkbox + number), Toggle Options (chaser/oneshot/optimization/penetration/
  squeeze/targeting/limit), Limit target radios (decker/ic). Per-utility exclusions.
- Functions: onUtilTypeChange, onOptionRatingInput, onNumericOptionToggle,
  syncOptionRatingCaps, getOptVal, computeUtilityFootprint, getProgramModsLabel,
  applyProgramOptionState, initNumSteppers.

### A6. Program calculation -- calcUtil()
- Footprint via computeUtilityFootprint (eff rating, base/design/actual size, mods).
- Prog card: `#utilCardTitle`, `#utilCardSub` (cat badge + multiplier + Attack dmg),
  `#utilStatRow` (Base/Design/Actual size), `#utilNote`.
- Cost & Availability `#utilCostGrid`: buy cost (or upgrade delta), street price (SI x),
  availability badge, street index, cost/Mp tier, limit target, eff rating.
- Construction Time `#buildTimeMeta` + `#buildTimeGrid`: base/delta construction time,
  programming TN, applied successes, planned compile time.
- `#utilSummaryPanel` shown / `#utilEmpty` hidden when valid.

### A7. Programming task roll (GM-only)
- rollProgrammingTask: Computer B/R dice vs TN=base rating, sets successes, recalcs.
- getProgrammingTargetNumber, getProgrammingSuccessesCap, syncProgrammingSuccessInputBounds,
  getProgrammingSuccesses, getPlannedCompileDays.

### A8. Compile / source / version system (the heavy backend)
- Snapshot: getCurrentProgramSnapshot, computeProgramEconomics, getProgramTypeKey,
  getProgramTypeLabelFromKey, getSourceDisplayName, buildSourceVersionFromSnapshot.
- Save/compile: saveCurrentProgram (new source v1 OR upgrade vN+1), compileSourceProject
  (queues a job), finalizeCompileJob (job -> compiled artifact), adjustCompileJobDays
  (ADMIN: -1d / Finish), deleteCompileJob.
- Upgrade flow: editSourceProject, startUpgradeFromCompiled, ensureSourceFromCompiledArtifact,
  validateSourceUpgrade, canAddUpgradeOptionsFromVersion, getUpgradeRatingFloorForUtil,
  applyUpgradeRatingFloor, setProgramEditState, cancelProgramEdit.
- Dupe guards: getFunctionalProgramSignature, findEquivalentCompiledArtifact,
  findEquivalentQueuedCompile.
- Migration/reconcile: migrateLegacyProgramsIfNeeded, reconcileProgramSourcesIfNeeded,
  buildSourceVersionFromArtifact, parseLegacyMods.

### A9. Purchased program import (modal)
- `#purchasedImportModal`: purchaseProgramType, purchaseProgramRating,
  purchaseAttackDmgField/purchaseAttackDmg, purchaseUtilBrief, `#purchaseOptionsArea`,
  `#purchaseImportNamePreview`, `#purchaseImportSummaryGrid`, Import/Cancel.
- Functions: getPurchasedImportDefaults, getPurchasedImportFootprintState,
  getPurchasedStreetPrice, syncPurchasedImportDraftFromModal, renderPurchasedImportOptions,
  onPurchaseOptionRatingInput, onPurchaseNumericOptionToggle, onPurchasedImportTypeChange,
  onPurchasedImportRatingChanged, onPurchasedImportOptionChanged, openPurchasedImportModal,
  closePurchasedImportModal, refreshPurchaseImportPreview, submitPurchasedProgramImport,
  populateUtilityDropdownLikeBuilder, computeProgramFootprintFromState.

### A10. Program Library / Compile Jobs -- renderSavedPrograms()
- Triggered by Import Purchased Program button (`openPurchasedImportModal`).
- `#libraryLoadSnapshot` (mirror of load usage bars).
- `#savedProgramsList`: Built library (collapsible per type, A/S/Upgrade/[x]),
  Purchased library (collapsible per type, A/S/[x]), Compile Jobs table
  (status, days left, ADMIN -1d/Finish, [x]).
- Add to load: addCompiledProgramToLoad, deleteCompiledProgram.

### A11. Deck Load Planner -- renderLoadPlanner()
- Add row: `loadLabelInput`, `loadTargetInput` (active/storage), "Add to Load".
- `#loadPlannerArea`: Active/Storage memory bars, filter buttons (all/active/storage_only/
  oneshot), Dense toggle, consolidated program table (Program/Size/Storage/Active/Usage/ops),
  +S/-S/+A/-A ops.
- Save load-out: `loadSaveName`, "Save Load-out", "Clear".
- Functions: addToLoadPlanner, addProgramToLoadPlanner, aggregateLoadPlannerEntries,
  computeLoadUsage, getProgramIdentityKey, isOneShotProgram, targetIsActive,
  targetHasStorage, setLoadPlannerFilter, toggleLoadPlannerDense, addEntryToActive,
  addEntryToStorage, removeEntryFromActive, removeEntryFromStorage, recalcLoadPlannerWithWarnings,
  getLoadedSleazeRating (feeds Detection Factor in A4).

### A12. Deck selection gating + alert/notice modals
- `#deckSelectionModal`: must pick a saved deck build before adding programs to memory.
  Functions: openDeckSelectionForLoad, cancelDeckSelectionForLoad, confirmDeckSelectionForLoad,
  ensureDeckSelectedForLoad, getActiveDeckBuild.
- `#deckAlertModal`: generic SYSTEM NOTICE / ERROR. Functions: openDeckAlertModal,
  closeDeckAlertModal, showAlert.

### A13. Saved Cyberdeck builds
- `deckSaveName` + Save; `#savedDecksList` (table: Name/MPCP/Saved/Load/[x]).
- Functions: saveDeckBuild, loadDeckBuild, deleteDeckBuild, renderSavedDecks.

### A14. Saved Program load-outs
- `#savedLoadoutsList` (table: Name/Programs/Saved/Load/[x]).
- Functions: saveLoadout, loadLoadout, deleteLoadout, clearLoadPlanner, renderSavedLoadouts.

### A15. Persistence (server + localStorage)
- Stores: DECK_STORE, LOADOUT_STORE, PROGRAM_STORE(legacy), SOURCE_STORE,
  COMPILE_JOB_STORE, COMPILED_STORE, migration/reconcile flags;
  programmer-scoped keys; server `PUT/GET /characters/{id}/deck-builder-state`.
- Functions: _loadStore, _saveStore, save/loadDeckBuilderStateFromServer,
  scheduleDeckBuilderStateSave, _deckStoreContainer, _collectLegacyDeckBuilderState, etc.
- IMPORTANT: these are ID-driven (read/write by element id). Porting must KEEP the same
  element IDs, or update every reference. Strategy: keep IDs identical; only move the
  DOM nodes into the new panes and restyle.

--------------------------------------------------------------------------------
## PART B -- PROPOSED MAPPING TO THE 3-PANE MOCKUP
--------------------------------------------------------------------------------

Legend: LEFT = left rail, CENTER = center column, INSP = right inspector.
Mode = which mode-switch state shows it (Deck / Program / both).

| Live piece (A#)                         | New home                         | Mode    |
|-----------------------------------------|----------------------------------|---------|
| A0 tab bar                              | REMOVED -> LEFT mode switch       | both    |
| A1 Programmer Profile gate              | ??? (see C1)                      | both    |
| A2 Interrupt overlay                    | unchanged (full-screen overlay)  | both    |
| A3 Deck Spec/Persona/Hardware/Mem/Acc  | CENTER (stacked panels)          | Deck    |
| A4 validity badge + persona bar         | LEFT summary (badge + bar)       | Deck    |
| A4 deck summary grid (13 items)         | LEFT summary                     | Deck    |
| A4 component cost table (8 col)         | ??? (see C2)                     | Deck    |
| A5 Program spec + options              | CENTER (stacked panels)          | Program |
| A6 prog card                            | INSP (program card)              | Program |
| A6 Cost & Availability                  | INSP                             | Program |
| A6 Construction Time                    | INSP                             | Program |
| A7 programming roll (gm)                | CENTER (in Program spec)         | Program |
| A8 compile/source/version (logic)       | unchanged (no UI of its own)     | Program |
| A9 Purchased import modal               | unchanged (modal)                | Program |
| A10 Program Library / Compile Jobs      | ??? (see C3)                     | Program |
| A11 Load Planner                        | ??? (see C4)                     | Program |
| A12 deck-selection + alert modals       | unchanged (modals)               | both    |
| A13 Saved Deck Builds                   | INSP                             | Deck    |
| A14 Saved Program Load-outs             | ??? (see C3/C4)                  | Program |
| A15 persistence                         | unchanged (keep element IDs)     | both    |

--------------------------------------------------------------------------------
## PART C -- OPEN QUESTIONS (things that do not cleanly fit) -- ASK BEFORE PORTING
--------------------------------------------------------------------------------

C1. Programmer Profile gate (A1). ANSWER: move into the LEFT rail (top of the left pane,
    above the mode switch; stays interactive while the rest is gated; collapses to the
    compact summary once activated).

C2. Component Cost Breakdown table (A4). ANSWER: lives in the CENTER pane, shown ON DEMAND
    via a "Review Build / Cost Breakdown" button in the left rail. Center (Deck mode) has
    two sub-views: the build form (default) and the cost-breakdown review (full wide table,
    with a "<< Back to Build" control).

C3. Program Library / Compile Jobs (A10) + Saved Load-outs (A14). ANSWER: CENTER, below
    the program form.

C4. Load Planner (A11). ANSWER: CENTER, co-located with the Library (same place as C3).

RESULTING INSPECTOR ROLE:
- Deck mode: empty-state + click-to-inspect component detail (TODO enhancement) +
  Saved Deck Builds.
- Program mode: computed program card + Cost & Availability + Construction Time
  (the program output; #utilSummaryPanel / #utilEmpty).
Note: Load Planner + Saved Load-outs were nested INSIDE #utilSummaryPanel in the live page
(hidden until a utility was selected). Moving them to CENTER makes them always visible in
Program mode -- a minor, non-breaking behavior improvement.

--------------------------------------------------------------------------------
## PART D -- PORT CHECKLIST (fill in after C answered)
--------------------------------------------------------------------------------
- [x] D-shell: added `.md3` + `.md3-panes` (LEFT/CENTER/INSP). Lock now toggles ALL
      `.deck-builder-app` elements (left builder block + #centerCol + #inspectorCol) via
      querySelectorAll in activateDeckBuilder / editProgrammerProfile. Profile gate sits
      OUTSIDE the lock so it stays interactive.
- [x] D-left: mode switch (#mode-deck / #mode-program -> setMode) replaces tab bar.
      switchTab(idx) kept as a shim -> setMode (editSourceProject still works).
- [x] D-summary(left): validity badge + deck summary grid in LEFT (Deck mode);
      leftSummaryProgram note (Program mode). personaBar stayed in the center Persona
      panel (where calcDeck writes it) -- harmless, zero-risk.
- [x] D-center-deck: A3 panels in CENTER #deckFormView; cost breakdown in CENTER
      #deckReviewView (toggled by showDeckReview / showDeckForm; "Review Build" button left,
      "<< Back to Build" in review).
- [x] D-center-program: A5 spec+options + A11 load planner + A14 saved load-outs +
      A10 library/compile jobs all in CENTER #centerProgram.
- [x] D-insp-deck: empty-state + Saved Deck Builds (deckSaveName/savedDecksList).
      (TODO enhancement: click-to-inspect per-component detail -- not yet wired.)
- [x] D-insp-program: #utilSummaryPanel (prog card + Cost&Avail + Construction Time) +
      #utilEmpty.
- [x] D-modals: A9 purchased-import, A12 deck-selection + alert, interrupt overlay left intact.
- [x] D-static-checks: tag balance OK (div 132/132, aside 2/2, section 1/1); inline script
      parses with 0 syntax errors; all 11 moved IDs appear exactly once; no leftover
      tab/db-layout refs.
- [x] D-verify (LIVE): PASSED on :8000 with the real admin token (saved as
      _sr_e2e/token-8000.txt). deck-preview-load.spec.js (shell/JS) and
      deck-preview-smoke.spec.js (full flow) both green, 0 page errors:
      activate (Static // Decker) -> VALID BUILD + 13 summary items (left) -> Review Build
      shows 12 cost rows + Back restores form -> Save -> "Smoke Rig" in saved list ->
      mode switch -> Program (Attack-6) -> inspector card + 6 cost items -> deck-selection
      modal -> Use Deck -> load planner +1 row. Screenshots: preview-deck-review.png,
      preview-program.png, preview-load.png in _sr_e2e.
      Note: alert/notice modal must be Acknowledged between actions (existing behavior, not
      a regression).
- [x] FOLLOW-UP: wire deck-mode click-to-inspect per-component detail (D-insp-deck enhancement).
      DONE via R8 + V2/V3 (labels AND number inputs call inspectDeckComponent for
      MPCP/B/E/M/S/Hardening/Response Increase -> #compDetail).

--------------------------------------------------------------------------------
## ROUND 2 -- DECK-BUILDER REFINEMENTS (user review 2026-06-04)
--------------------------------------------------------------------------------
Scope: DECK builder only this round (Program builder feedback comes later).

- [x] R1. Mode switch: glyphs removed; active mode shows a green left bar (inset box-shadow)
      + a green ">" indicator (.db-ind). Inactive ">" is transparent.
- [x] R2. Deck Summary: calcDeck now renders #deckSumGrid as <div class="sum-row"><span k><span v>
      rows (matrix-designer style; .sum-row already scoped to #md3SummaryMount). 13 rows verified.
- [x] R3. Review Build: now a fade-in #deckReviewOverlay (.ltg-overlay) holding the cost table;
      showDeckReview() calcDeck()+adds .open, closeDeckReview() removes it; backdrop + "x Close"
      both close. setMode away from deck closes it.
- [x] R4. Compact number fields: inline widths (mpcp 84 / hardening+RI 72 / mem 96 / storage 110 /
      BEMS 100%) + initNumSteppers($('centerDeck')) on init. B/E/M/S in one .db-bems row.
- [x] R5. Auto-save: scheduleDeckAutosave() (600ms debounce) called at end of calcDeck (and the
      invalid-MPCP early return); autosaveDeckBuild() upserts under Deck Name keyed by
      activeDeckBuildName; status line #deckAutosaveStatus. Manual deckSaveName input + Save
      button removed. loadDeckBuild/newDeckBuild set _skipDeckAutosave to avoid churn.
- [x] R6. Deletes red: .lp-remove-btn restyled to a red bordered button (covers program/loadout/
      library lists); saved-decks delete is now <button class="btn btn-red btn-sm">Delete</button>.
      FOLLOW-UP (program round): unify the remaining [x] glyphs to "Delete" text for full parity.
- [x] R7. "New Deck" button in the left toolbar -> newDeckBuild() resets the form + load planner.
- [x] R8. Click-to-inspect: labels for MPCP / B / E / M / S / Hardening / Response Increase call
      inspectDeckComponent(); renders rules (DECK_COMPONENT_INFO) + live size/subtotal/cook/install
      from window._deckRows into #compDetail. Verified (BOD detail).

VERIFY (R1-R8): deck-preview-smoke.spec.js updated + PASSES 0 issues on :8000 (token-8000.txt).
Screenshots refreshed: preview-deck-review.png (overlay), preview-program.png.

PROGRAM-BUILDER feedback: DEFERRED to a later round (user has "lots more comments").

--------------------------------------------------------------------------------
## ROUND 3 -- DECK-BUILDER REFINEMENTS (user review 2026-06-04, batch 2)
--------------------------------------------------------------------------------
- [x] T1. Programmer dropdown option text = c.name only (archetype dropped);
      profileSummaryText = name only ("Programmer:" prefix removed). Verified: "Static".
- [x] T2. Added <div class="db-navgroup">Builder Mode</div> above the mode switch.
- [x] T3. calcDeck validity: run-ready = no cap errors AND all four persona programs >= 1.
      Otherwise badge gets class .db-flash (slow red pulse, 1.4s) and reads "INVALID BUILD"
      (constraint list, or "set all four persona programs"). Verified: only-MPCP flashes
      INVALID; full persona -> VALID. (matrix-run defaults B/E/M/S to 1 when loading a deck;
      validateLoadoutRules covers program rules only, so persona-complete is the deck gate.)
- [x] T4. All deck-builder deletes now <button class="btn btn-red btn-sm">x</button>
      (matches the manage-organizations red-X). Covers decks, load-outs, compiled programs,
      compile jobs. No .lp-remove-btn usages remain.
- [x] T5. Center starts on #deckEmptyState (form hidden) until newDeckBuild()/loadDeckBuild()
      call setDeckFormVisible(true); changing programmer resets to empty. Verified.

VERIFY (T1-T5): deck-preview-smoke.spec.js updated + PASSES 0 issues on :8000.

--------------------------------------------------------------------------------
## ROUND 4 -- DECK-BUILDER REFINEMENTS (user review 2026-06-04, batch 3)
--------------------------------------------------------------------------------
- [x] U1. syncPersonaInputs(): B/E/M/S min=1, max=MPCP, value clamped to MPCP; disabled +
      greyed (.db-disabled, pointer-events off so steppers die too) until MPCP >= 1. Called
      at top of calcDeck. Verified (disabled w/o MPCP; max=6 after).
- [x] U2. B/E/M/S inputs width 72px (was 100%); .db-mini flex:0 0 auto, gap 14px.
- [x] U3. Deck Spec is one .db-spec-row: Deck Name (flex:1) + Deck Type (.db-type-select,
      width:max-content -> fits the Tortoise option + arrow) + MPCP (84px). MPCP tips moved below.
- [x] U4. Hardware row gap bumped to 28px.
- [x] U5. .db-memrow with three .db-membox cells (Active Memory, Mp / I/O Speed, Mp/turn /
      Deck Storage, Mp); descriptors "Multiples of 10. max <#>" / "Multiple of 10. max <#>" /
      "Max: 65,535". calcDeck updated to set the new static headers + descriptor tips.
- [x] U6. Left New Deck button removed (center empty-state keeps one). setDeckFormVisible(true)
      replays a .db-fade (dbFadeIn keyframe, opacity+translateY .3s) on reveal.
- [x] U7. .db-navgroup now cyan, bold, larger (fs-sm), with a bottom rule + soft glow.
- [x] U8. #mdInspector .md3-summary gets a top border + spacing; compDetail separated.

VERIFY (U1-U8): smoke PASSES 0 issues; screenshot preview-deck-form.png reviewed (spec one-line,
type not clipped, narrow B/E/M/S, boxed memory row, cyan headers, separated inspector).

--------------------------------------------------------------------------------
## ROUND 5 -- DECK-BUILDER REFINEMENTS (user review 2026-06-04, batch 4)
--------------------------------------------------------------------------------
- [x] V1. Uniform field heights across the page; match the Deck Type select's height for all
      text/number/select fields. (CSS: #deckMain input[type=text|number],select { height:34px;
      box-sizing:border-box }. Verified: all 12 deck fields render at 34px.)
- [x] V2. B/E/M/S: clicking anywhere on the field (label OR number input) opens its inspector.
      (onclick=inspectDeckComponent(..) on BOTH the label and the <input>. Verified: clicking
      the #pEvasion input opens the Evasion detail.)
- [x] V3. Same click-anywhere-to-inspect for Hardening and Response Increase. (Verified:
      clicking the #hardening and #respIncrease inputs opens their detail.)
- [x] V4. Memory / I/O / Storage: allow free typing, then debounce ~1s and snap to the nearest
      VALID value (clamp to [min, MPCP-derived max]; round to a multiple of 10). All 3 fields.
      (onMemInput -> calcDeck live preview + 1000ms _memSnapTimers -> snapMemoryField;
      memFieldBounds gives per-field [min,max]. Verified: activeMem 137->140, 99999->600(clamp),
      ioSpeed 47->50.)
- [x] V5. Inspector: put the BEMS/Hardening/RI detail in a box with a modified background to
      separate it from Saved Deck Builds. (#mdInspector #compDetail border + bg #0c130c, rendered
      ABOVE Saved Deck Builds. Verified: boxed, tinted, above.)
- [x] V6. Review modal: column headers should NOT be bold. (#deckReviewOverlay .comp-table th
      { font-weight:normal }. Verified: all 8 header weights = 400.)
- [x] V7. Cook/Install Task roll. DESIGN DECISIONS (user, 2026-06-04):
        * Granularity = AGGREGATE: one cook roll + one install roll for the whole deck,
          TN = MPCP, dice = Computer B/R. actual = ceil(rollable base / successes) + misc base.
        * Misc components (Deck Casing, Satlink, Hitcher, I/O Speed, Offline Storage, ICCM,
          Reality Filter) = NO roll; their base cook/install pass through unchanged.
        * Storage = successes + computed times: build.cookInstall = { cookSuccesses,
          instSuccesses, baseCook, baseInst, rollCook, rollInst, miscCook, miscInst,
          actualCook, actualInst, tn, dice, rolledAt }.
      BUILT: rollable rows tagged `roll:true` (MPCP, persona B/E/M/S, ASIST, Hardening,
        Response Increase, Active Memory); others pass through. New Construction Task panel in
        the Review overlay (#deckConstructionPanel): meta line (dice/TN), sum-grid (Base Cook,
        Base Install, Cook(N succ), Install(N succ)), + GM-only auto-roll & successes overrides.
        Functions: getDeckBrDice, getDeckSuccesses, computeDeckConstruction, renderConstructionTask
        (called at end of calcDeck -> window._deckConstruction), rollDeckConstruction. Persisted
        via _currentDeckBuild + saveDeckBuild (cookInstall); restored in loadDeckBuild; reset in
        newDeckBuild. VR2 mechanic mirrors the existing program roll (rollProgrammingTask).
      VERIFIED: base (succ=1 -> actual==base, TN=MPCP=6, rollCook=78), admin override
        (cook succ=2 -> ceil(78/2)+0=39), and cookInstall snapshot persisted on the build.
- [x] V8. Remove the popup confirmation when loading a deck/load-out. (No confirm() calls remain;
      loadDeckBuild/loadLoadout load silently. Verified: no native dialog fires on load.)

VERIFY (V1-V8): _sr_e2e/deck-preview-round5.spec.js PASSES 0 issues on :8000 (token-8000.txt) --
covers V1 heights, V2/V3 input-click inspect, V4 snap (137->140, 99999->600 clamp, 47->50),
V5 boxed/above, V6 non-bold headers, V7 construction (base/override/persist), V8 no load dialog.
deck-preview-smoke.spec.js still green (0 issues, no regression). Screenshot preview-round5.png.

PROGRAM BUILDER: still deferred -- likely needs MORE panes (many targets to track). Revisit.

CLEANUP (done 2026-06-04): deleted fully-completed checkpoint docs
matrix-designer-batch13-todo.md + world-state-2pane-fields-todo.md (all tasks [x]; in git
history). Left non-checkbox reference/report docs (ai_parser_reference, refactor-notes,
matrix2-* reports) and docs with open items.
CLEANUP (2026-06-04, batch 5): deleted docs/matrix-designer-3pane-port-plan.md -- the
matrix-designer 3-pane port is COMPLETE and live (see memory project_matrix_designer_3pane_port);
its remaining audit checkboxes were stale (prompt() editors retired + Follow=host-switch already
shipped). Kept deck-builder-3pane-plan.md (its matrix-run M1-M3 section is still pending).

--------------------------------------------------------------------------------
## ROUND 6 -- DECK-BUILDER REFINEMENTS (user review 2026-06-04, batch 5)
--------------------------------------------------------------------------------
- [x] W1. A little more vertical space after the Hardening/Response Increase number spinners,
      before the ICCM Biofeedback Filter row. (Hardware .db-spec-row margin-bottom:18px. Verified.)
- [x] W2. Response Increase Max -- user asked "why min(floor(MPCP/4), 3)?". ANSWER: floor(MPCP/4)
      is the MPCP-derived limit; the hard 3 is the hardware ceiling -- Response Increase only comes
      in levels 1-3 (consistent app-wide: matrix-run 0-3, prototype max 3). Formula KEPT. User
      themselves rewrote the inspector text to: "Max (MPCP /4) rounded down. A deck cannot support
      more than 3 levels of Response Increase." (left as-is -- authoritative). Verified.
- [x] W3. Memory / I/O / Storage: dropped the ~1s debounce snap; enforce on BLUR instead
      (onblur=snapMemoryField; oninput=onMemInput just does live calcDeck, no timer; removed
      _memSnapTimers). Verified: snaps on blur (137->140, 99999->600, 47->50); stays as-typed mid-type.
- [x] W4. Cook/Install in the Review pane: Base + Actual now plain calculated LABEL lines --
      "Base Cook: <n> days" / "Base Install: <n> days" / "Actual Cook: <n> days" /
      "Actual Install: <n> days" (.db-construct-line; renderConstructionTask). No successes count
      shown. Actual==Base when no successes entered. Verified.
- [x] W5. Rule of 6 (exploding dice): added rollExplodingD6() + rollDicePool(dice,tn) -- a 6 is
      re-rolled and ADDED, repeating, so a chained 6 beats TN>6. Fixed BOTH the deck construction
      roll and rollProgrammingTask (both had the flat-d6 bug -> any TN>6 was unbeatable, e.g. MPCP
      12 construction always scored 0). Backend roll_dice already correct (explodes when tn>6).
      DOCUMENTED in repo AGENTS.md (section 3, "Dice rolls -- Rule of 6"). Verified: dice exceed 6,
      TN-8 pool scores successes.
- [x] W6. Deck build job tracking (deck-builder side done; run-side chip damage deferred).
      DESIGN ANSWERS (user, 2026-06-04):
        * Kick-off = a "Start Build" button in the Construction Task panel (Review overlay),
          using the current Actual Cook / Actual Install as the two phase durations.
        * Queue = ONE unified Fabrication Queue (deck builds + program compiles) shown in BOTH
          Deck and Program mode. GM -1d/Finish ticks operate on every in-progress job.
        * Sequencing = cook BEFORE install, never parallel. One job, two phases:
          phase 'cook' (daysRemaining=actualCook) -> at 0 switch to 'install'
          (daysRemaining=actualInst) -> at 0 finalize.
        * On finish = mark the saved deck build FABRICATED (status badge), store an as-built
          snapshot (ratings + total nuyen + total build days + fabricatedAt). Deck stays editable.
      EXPANDED REQUIREMENTS (user):
        * UPGRADE delta: like programs, editing/improving a fabricated deck builds only the
          DIFFERENCE in time + nuyen between the as-built (source) ratings and the new
          (destination) ratings. Re-Start-Build on a fabricated deck queues a delta job; on
          finish, the as-built snapshot advances to the new ratings.
        * CHIP DAMAGE: if a run's IC permanently lowers deck stats (chip burn), that reduction
          must persist into the fabricated artifact (as-built snapshot stat reductions). NOTE:
          applying damage happens on the matrix-run side -> cross-page integration; the artifact
          carries a `statDamage`/effective-rating field so the run can write to it.
      BUILD PLAN: (1) unified queue + kick-off + cook->install sequencing + mark fabricated
      [core, this round]; (2) upgrade-delta on re-build [this round if stable]; (3) run-side chip
      damage wiring [DEFERRED -- needs matrix-run design; artifact field reserved now].
      NOTE: file is being co-edited live by the user -- re-read regions right before each edit.
      STATUS (2026-06-04): (1) + (2) BUILT & VERIFIED; (3) reserved-only (see below).
      BUILT:
        * "Start Build" button + #deckBuildStatus in the Construction Task panel. startDeckBuild()
          snapshots ratings + finalCost + actualCook/actualInst onto a deck job (kind:'deck' in
          COMPILE_JOB_STORE), phase 'cook' first.
        * Unified Fabrication Queue: renderFabricationQueue() writes deck jobs + program compiles
          to every .fab-queue-mount (one in #centerDeck = #fabQueueDeck, one in #centerProgram =
          #fabQueueProgram). renderSavedPrograms no longer renders its own Compile Jobs block.
        * Sequencing: adjustCompileJobDays branches to adjustDeckJobDays for deck jobs -- cook
          drains, flips to install at 0, finalizes at install 0. GM -1d / Finish work on all jobs.
        * finalizeDeckJob() marks the saved build fabricated + stores fabricatedSnapshot; FABRICATED
          badge in Saved Deck Builds. autosaveDeckBuild preserves fabricated/snapshot across rebuilds.
        * Upgrade-delta: re-Start-Build on a fabricated deck computes cook/install/nuyen DELTA vs
          the snapshot (isUpgrade job); blocks if no rating raised. On finish the snapshot advances.
        * statDamage:{} reserved on the snapshot for (3).
      VERIFIED: _sr_e2e/deck-preview-w6.spec.js (0 issues) -- kick-off (cook 78 / install 56),
        both queue mounts, cook->install flip, fabricate + snapshot + badge, autosave preserves
        fabricated, upgrade MPCP 6->7 = delta cook 4 / install 3. Full preview suite (smoke +
        round5 + round6 + w6) all green.
      DEFERRED (3) chip damage: needs matrix-run side to write stat reductions into the fabricated
        deck's snapshot (statDamage / effective ratings) when chip-burning IC hits during a run.
        Cross-page; design + matrix-run wiring is a separate task. Artifact field is ready.

--------------------------------------------------------------------------------
## ROUND 7 -- DECK-BUILDER REFINEMENTS (user review 2026-06-04, batch 6)
--------------------------------------------------------------------------------
- [x] X1. Rounding language in DESCRIPTIONS/UI text. Reworded all user-facing "floor(x)"/"ceil(x)"
      to "<formula>, rounded down/up": deck-builder-preview (mpcpCapTip, construct meta, Hardening
      info), matrix-run (Hacking Pool, Reaction tips), matrix-designer (IC-cap alert), host-builder
      prototype (Max IC rating). Code Math.floor/ceil left as-is. NOTE: live deck-builder.html left
      under the preview-freeze -- it inherits the reworded text when the preview ports.
- [x] X2. Cook/Install roll = PLAYER rolls Computer B/R (rule of 6) via rollDeckConstruction();
      the result LOCKS onto build.constructionRoll (not editable). Start Build is gated on a locked
      roll (updateDeckBuildStatus enables/disables #rollConstructionBtn / #startDeckBuildBtn). The
      old editable successes inputs were removed; GM "Reset Roll" (resetConstructionRoll) re-rolls.
      The roll is consumed (cleared) when Start Build queues the job. constructionRoll persists
      across autosave. Verified (round7 gating + round5 V7 successes math).
- [x] X3. Built vs bought + naming:
        * Right pane renamed "Saved Deck Builds" -> "Saved Deck Designs" (+ copy updated).
        * Tags in renderSavedDecks: fabricated -> green "Built" badge; purchased -> cyan "Purchased"
          badge (no Built tag). GM-only "Purchase (GM)" button -> purchaseDeckDesign() sets
          build.purchased (no job, no Built tag, runnable now). Flag preserved across autosave.
        * matrix-run.html: renderDeckAndLoadoutSelectors filters the deck dropdown to
          (fabricated || purchased); fabricated options carry a " [Built]" tag, purchased do not.
      Verified (round7 purchase/tags + matrix-run-deckfilter.spec.js).
- [x] X4. Construction panel now shows the UPGRADE delta. computeDeckConstruction subtracts the
      as-built snapshot's base breakdown (rollCook/rollInst/miscCook/miscInst, now stored on the
      snapshot) so a fabricated deck shows delta cook/install; header + labels switch to "Upgrade".
      Start Build uses the delta. FIXES the 233/240 bug (that was the full rebuild). Verified:
      MPCP 6->7 upgrade shows delta cook 4 vs full base 82.
VERIFY (X1-X4): _sr_e2e/deck-preview-round7.spec.js + matrix-run-deckfilter.spec.js PASS 0 issues;
full preview suite (smoke + round5 + round6 + w6 + round7) + matrix-run filter all green serially.

--------------------------------------------------------------------------------
## ROUND 8 -- BUILD/BUY APPROVAL FLOW (user review 2026-06-05)
--------------------------------------------------------------------------------
Big model change: the in-app dice roll goes away; EVERYTHING is gated by GM approval.
- [x] Y1. Player roll removed. In the Review overlay the player now picks Build It or Buy It
      (Purchase). No successes/roll UI for players. (Removed rollDeckConstruction,
      setConstructionRollManual, resetConstructionRoll, getActiveConstructionRoll, old
      startDeckBuild + the roll/manual/Start buttons + #deckConstructionRoll element.)
- [x] Y2. Build/Buy submit a request onto the deck record: build.request =
      {kind:'build'|'purchase', ...}. Build requests snapshot the construction breakdown
      (rollCook/rollInst/miscCook/miscInst + FULL breakdown + target ratings + finalCost) so the
      GM panel recomputes times without re-deriving rows. requestDeckBuild / requestDeckPurchase /
      withdrawDeckRequest. Pending preserved across autosave; closes the review overlay on submit.
- [x] Y3. GM Pending Approvals panel at the TOP of #centerCol (class gm-only, admin only, both
      modes). renderPendingApprovals lists each request; BUILD rows have Cook/Install success
      number fields that LIVE-recompute actual cook/install (recomputeApprovalTimes ->
      computeApprovalTimes) + Start Build (approveDeckBuild -> queues the cook->install fab job
      from the request snapshot) + Reject. PURCHASE rows have Authorize Purchase
      (authorizeDeckPurchase -> sets purchased, available now) + Reject. Index-keyed element ids
      (window._pendingApprovalList) to avoid escaping deck names. Count badge on the header.
      NOTE: restored the real-time actual-time calc the user said was lost (now in the GM panel).
- [x] Y4. Inspector simplified to Name (+ availability badge: Built/Purchased/Pending) / MPCP /
      Load / Delete. Removed the Saved-date column and the inline Purchase (GM) button
      (purchaseDeckDesign retired -- purchase now goes through the approval queue). Delete kept on
      BOTH views per the user (lets players trash experiments).
- [x] Y5. Left CTA restyled (.db-review-cta: green, glowing, ctaPulse) + retext ">> REVIEW &
      SUBMIT // Build . Buy . Cost".
- [x] Y6. Column headers forced non-bold globally: #deckMain table th { font-weight:normal }.
- [~] Y7. Global "pending approvals" indicator -- MOCKUP ONLY per user ("show me first before
      making it live"): frontend/prototypes/admin-approval-indicator-mockup.html shows a sticky
      amber banner (persists on every page until the queue clears) + a page-load popup, with state
      toggles. NOT wired to real data / shared.js yet. Awaiting sign-off before implementing live.
KNOWN LIMITATION: deck stores are programmer-scoped, so the in-page GM queue shows the ACTIVE
      programmer's requests. A true cross-programmer/global count (for the banner) needs server-side
      aggregation -- flagged in the mockup notes for the data-model pass.
PROGRAMS: same Build/Buy-then-approve treatment is DEFERRED to the program-builder refactor round.
VERIFY (Y1-Y7): static only so far -- inline script parses (0 errors), 13 new/changed funcs each
      defined once, div tags balanced (276/276), mockup script parses. E2E specs NOT yet updated
      (round7 spec still asserts the OLD roll UI and must be rewritten for the approval flow).

## PROGRESS LOG
- 2026-06-04: Read full live page; wrote this inventory + mapping. Created deck-builder-preview.html
  (copy, title marked "(preview)"). Awaiting answers to C1-C4 before porting.
- 2026-06-04 (cont.): C1-C4 answered (see Part C). Ported the 3-pane shell into
  deck-builder-preview.html: head <style> helpers; <main> rebuilt as md3 LEFT/CENTER/INSP;
  added setMode/showDeckReview/showDeckForm + switchTab shim; lock now toggles all
  .deck-builder-app regions. Static checks PASS (tags balanced, script syntax clean, IDs
  unique, no orphan refs; :8000 serves the edited file -- 6/6 markers).
  e2e smoke specs written in _sr_e2e: deck-preview-load.spec.js (no-flow shell/JS check)
  and deck-preview-smoke.spec.js (full flow). BLOCKED on live verification: _sr_e2e/token.txt
  is the :8770 token and returns 401 against :8000 (page redirects to /ui/ login before mount).
  NEXT: get a valid :8000 admin token (or point specs at the right instance), then run the
  full flow; then wire the deferred deck-mode click-to-inspect component detail (D-insp-deck).
- 2026-06-04 (Round 5): Found V1-V6 + V8 already implemented in the working tree from a prior
  session; verified each with a new focused spec (deck-preview-round5.spec.js) -- all pass.
  Then built V7 (cook/install construction roll) per the user's three design answers:
  AGGREGATE roll (TN=MPCP, dice=Computer B/R), NO roll for accessories (base passes through),
  store successes+computed times on build.cookInstall. Tagged rollable rows, added the
  Construction Task panel to the Review overlay + roll/override/persist plumbing. Round-5 spec
  extended with V7 (base/override/persist) and smoke re-run: both green, 0 issues.
  Whole Round 5 (V1-V8) now [x]. Preview still untracked (live page untouched per sign-off rule).
  REMAINING: Program-builder refinements (deferred -- may need more panes); D-insp-deck note now
  effectively done via R8/V2/V3 click-to-inspect.
- 2026-06-04 (Round 6, W1-W6): Docs cleanup -- deleted docs/matrix-designer-3pane-port-plan.md
  (port complete & live). W1 spacing, W2 RI-text clarify (user rewrote it themselves; kept), W3
  memory enforce-on-blur (dropped debounce), W4 Base/Actual cook+install LABELS, W5 rule-of-6
  exploding dice (rollExplodingD6/rollDicePool; fixed deck-construction + rollProgrammingTask;
  documented in AGENTS.md s3) -- all verified via deck-preview-round6.spec.js (0 issues).
  W6 deck fabrication jobs (user answers: kick-off in Construction panel, unified queue both
  modes, cook->install sequential, mark fabricated + as-built snapshot, upgrade-delta): BUILT &
  VERIFIED via deck-preview-w6.spec.js (0 issues). Run-side chip-damage persistence DEFERRED
  (matrix-run cross-page; statDamage field reserved). NOTE: user co-edited the file live this
  round (RI text, memory tips/min vars) -- re-read regions before edits. Preview still untracked.
  NEXT: chip-damage matrix-run wiring (design first); Program-builder refinements still deferred.
- 2026-06-04 (Round 7, X1-X4): X1 rounding-language sweep (deck-builder-preview, matrix-run,
  matrix-designer, host-builder prototype; live deck-builder.html deferred to the port). X2
  player-rolls-Computer-B/R-and-locks (constructionRoll on the build; Start Build gated; editable
  successes inputs removed; GM Reset Roll). X3 "Saved Deck Designs" rename + Built/Purchased tags
  + GM purchaseDeckDesign + matrix-run runnable-only deck dropdown with [Built] tag. X4 upgrade
  DELTA shown in the construction panel (was showing the full rebuild -> the 233/240 report) by
  storing the full cook/install breakdown on the as-built snapshot and subtracting it. All verified
  via new deck-preview-round7.spec.js + matrix-run-deckfilter.spec.js (0 issues) and the full
  preview suite green. NOTE: user co-editing the file live again (RI text, memory min vars) --
  re-read before edits. Preview still untracked; live deck-builder.html untouched.
