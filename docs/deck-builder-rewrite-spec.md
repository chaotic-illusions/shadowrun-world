# Deck-Builder Preview -- Full Rewrite Spec (for the next agent)

You (the agent reading this) are going to rewrite `frontend/deck-builder-preview.html`
from scratch so that it has **full functional parity** with the live page
`frontend/deck-builder.html`, in the **3-pane md3 shell** the project already uses for
matrix-designer and the previous deck-builder-preview iteration.

The previous preview iteration accumulated cruft across six review rounds. We are throwing
that version away and producing a clean rebuild that:

1. Mirrors every behavior of the live page (no regressions),
2. Lays everything out in the 3-pane md3 shell with **uniform control sizing and no wasted
   whitespace**,
3. Replaces "row stretched to fill space" with content that earns its row.

Read this whole document before you touch a file. Stop and ask on every conflict.

---

## 0. Ground rules (do not skip)

- **Source of truth (read these first):**
  - `frontend/deck-builder.html` -- the live page. **Behavior** comes from here.
  - `frontend/matrix-designer.html` -- the canonical md3 shell. **Shell pattern** comes from here.
  - `frontend/style.css` -- the `.md3-*`, `.sum-row`, `.comp-table`, `.ltg-overlay`,
    `.btn / .btn-red / .btn-sm`, `.infield-num-*` rules. **Reuse, never fork.**
  - `frontend/shared.js` -- `esc`, `apiFetch`, `authHeaders`, `showAlert`, `showConfirm`,
    `initNumSteppers`, polling helpers. **Reuse, never duplicate.**
  - `AGENTS.md` -- check-first/validate-after process. **Mandatory.**
  - `.github/copilot-instructions.md` -- stack/auth/encoding rules.

- **Target file:** `frontend/deck-builder-preview.html`. Replace its contents wholesale.
  Do NOT touch `frontend/deck-builder.html` or `frontend/deck-builder.html`'s callers.

- **Frontend encoding:** ASCII-only literals (`--`, `->`, `...`, `&mdash;`, `&times;`,
  `&yen;`, `&ge;`, `&#9650;`). The pre-commit hook (`tools/check_text_hygiene.py`) will
  reject smart quotes / em dashes / unicode glyphs in source.

- **XSS:** every server- or user-derived value going into `innerHTML` or a template literal
  must be wrapped in `esc()`. Prefer `.textContent` where possible.

- **API calls:** always use `apiFetch` from `shared.js`. Never raw `fetch`.

- **Conflict protocol:** when ANY of the following happens, **stop and ask the user**
  before proceeding:
  - A function from the live page has no obvious home in the new layout.
  - Two design rules conflict (e.g. "34px height" vs "fit the Tortoise option without
    clipping the chevron").
  - A panel cannot be made dense without dropping information.
  - The user-supplied "row filler" policy is unclear for a specific row.
  - A live behavior looks like a bug and you're tempted to "fix" it during the port.
    (Port the bug; flag it separately.)

- **No comments on copied code.** When you copy a function body verbatim, do not add new
  doc comments. One-line `// WHY` comments are fine for genuinely non-obvious decisions.

---

## 1. Mission summary

Rewrite `frontend/deck-builder-preview.html` so that:

- The DOM is structured into the **3-pane md3 shell** (left summary / center workspace /
  right inspector), with the live tab bar replaced by a **left-rail mode switch**
  (Cyberdeck / Program).
- **Every** element id from the live page is preserved (see ID-preservation strategy in
  Section 6). The inline `<script>` from live is copied **verbatim** as the starting
  point, then minimally adapted only for selectors that move panes (e.g. the mode-switch
  shim).
- **All controls share a uniform 34px height** (inputs, selects, buttons -- both `.btn`
  and the inline action buttons rendered into generated tables).
- **No row stretches to fill space.** Where the live page has a half-empty row, you either
  pack another logical control into it or shorten the row so it doesn't span the column.
  See Section 4 for the filler policy and the row-by-row table you must produce as part of
  the deliverable.
- Behavior parity is verified by the existing playwright suite (`_sr_e2e/`), plus a quick
  manual pass against the inventory in Section 3.

---

## 2. Shell structure (copy this exactly)

The new page uses the matrix-designer md3 shell. The skeleton below is **mandatory**;
class names and the outer ids (`md3SummaryMount`, `centerCol`, `mdInspector`, etc.) come
from `style.css` and must not be renamed.

```html
<main id="deckMain">
  <div class="md3">

    <!-- (Optional) top tabbar slot. Leave empty; we don't use host tabs here. -->
    <div class="md3-tabbar"></div>

    <div class="md3-panes">

      <!-- LEFT: profile gate (always interactive) + mode switch + live summary -->
      <aside class="md3-side">
        <div class="pane">
          <div class="pane-hd">Builder</div>
          <div class="pane-bd" id="md3SummaryMount">

            <!-- A1 Programmer Profile gate (stays OUTSIDE the lock) -->
            <section id="profileGateCard"> ... </section>

            <!-- Mode switch (replaces live tabBtn0 / tabBtn1) -->
            <div class="db-navgroup">Builder Mode</div>
            <nav class="db-modeswitch">
              <button id="mode-deck"    class="db-mode on"
                      onclick="setMode('deck')"><span class="db-ind">&gt;</span> Cyberdeck</button>
              <button id="mode-program" class="db-mode"
                      onclick="setMode('program')"><span class="db-ind">&gt;</span> Program / Utility</button>
            </nav>

            <!-- Live summary -- ONE block, mode-switched -->
            <div id="leftSummaryDeck">
              <div id="validityBadge" class="validity-badge"></div>
              <div class="md3-summary">
                <div class="md3-summary-hd">Deck Summary</div>
                <div id="deckSumGrid"></div>
              </div>
              <button class="btn btn-sm" onclick="showDeckReview()">&gt;&gt; Review Build</button>
            </div>
            <div id="leftSummaryProgram" style="display:none">
              <!-- Mirror of the program-side summary card title; details live in the inspector -->
            </div>

          </div>
        </div>
      </aside>

      <!-- CENTER: workspace per mode -->
      <section class="md3-center deck-builder-app deck-builder-locked" id="centerCol">

        <div id="centerDeck">
          <div id="deckEmptyState"> ... "Pick or start a deck" empty-state ... </div>
          <div id="deckFormView" style="display:none">
            <!-- A3 panels: Deck Spec / Persona / Hardware / Memory & I/O / Accessories -->
          </div>
          <!-- Saved Deck Builds live in the INSPECTOR (Section 5), not here. -->
          <!-- Component Cost Breakdown lives in an overlay (#deckReviewOverlay), not here. -->
        </div>

        <div id="centerProgram" style="display:none">
          <!-- A5 program spec + A11 load planner + A14 saved load-outs + A10 library/jobs -->
        </div>

      </section>

      <!-- RIGHT: inspector -->
      <aside class="md3-side deck-builder-app deck-builder-locked" id="inspectorCol">
        <div class="pane">
          <div class="pane-hd">Inspector</div>
          <div class="pane-bd" id="mdInspector">

            <div id="inspDeck">
              <!-- Click-to-inspect detail (BEMS / Hardening / RI / MPCP) -->
              <div id="compDetail" class="comp-detail-box">
                <div class="md3-insp-empty">
                  Click a deck component (MPCP / B / E / M / S / Hardening / Response Increase)
                  to see its rules and live contribution.
                </div>
              </div>
              <!-- A13 Saved Deck Builds (rendered into #savedDecksList) -->
              <div class="md3-summary">
                <div class="md3-summary-hd">Saved Deck Builds</div>
                <div id="savedDecksList"></div>
              </div>
            </div>

            <div id="inspProgram" style="display:none">
              <!-- A6: utilSummaryPanel (utilCard + Cost &amp; Availability + Construction Time)
                   + utilEmpty placeholder.  Move the existing elements; keep their ids. -->
              <div id="utilEmpty" class="md3-insp-empty">
                Select a utility type to see its card, cost, and construction time here.
              </div>
              <div id="utilSummaryPanel" style="display:none">
                <!-- utilCard / utilCostGrid / buildTimeMeta / buildTimeGrid -->
              </div>
            </div>

          </div>
        </div>
      </aside>

    </div>

    <!-- A4 Component Cost Breakdown + Construction Task (overlay) -->
    <div id="deckReviewOverlay" class="ltg-overlay"> ... </div>

    <!-- A9 Purchased import modal -->
    <div id="purchasedImportModal"> ... </div>

    <!-- A12 Deck-selection modal -->
    <div id="deckSelectionModal"> ... </div>

    <!-- A12 Alert modal -->
    <div id="deckAlertModal"> ... </div>

    <!-- A2 Interrupt overlay -->
    <div id="deckInterruptOverlay"> ... </div>

  </div>
</main>
```

**Locking:** the live page toggles `#deckBuilderApp` between
`deck-builder-locked` / `deck-builder-unlocked`. In the new shell, the equivalent is to
toggle the lock class on **every** element with class `.deck-builder-app`
(`#centerCol` AND `#inspectorCol`). The profile gate stays outside that lock so the user
can always change programmer. Implement the toggle with `querySelectorAll('.deck-builder-app')`.

**Mode switch shim:** keep `switchTab(idx)` defined as a thin shim that calls
`setMode(idx === 0 ? 'deck' : 'program')`. The live page's `editSourceProject()` calls
`switchTab(1)`, and we don't want to chase that change through the copied JS.

---

## 3. Functional inventory you must preserve

This is the **complete** list of behaviors from the live page. Treat it as a checklist.
Every single function must end up wired in the new file (most via copy-paste; a few need
selector adjustments). When you finish, you will produce a parity table (Section 9).

### 3.1 Module-scope state to keep verbatim

| Name | Kind | Initial | Role |
|---|---|---|---|
| `UTILITIES` | const | array | Utility/program master table |
| `OPTION_DEFS` | const | array | Program option definitions |
| `OPTION_EXCLUSIONS` | const | object | Per-utility option exclusions |
| `OFFENSIVE_ONLY_OPTIONS` | const | `["chaser","penetration","targeting"]` | |
| `loadPlannerItems` | let | `[]` | Current load-planner items |
| `deckProgrammerCaps` | let | `{mpcpMax:50,utilMax:50}` | Programmer-derived caps |
| `PROGRAMMER_PROFILE_STORE` | const | `"sr2_deck_programmer_profile_v1"` | profile key |
| `STORAGE_PRACTICAL_MAX` | const | `65535` | offline-storage cap |
| `YEAR_OFFSET` | const | `24` | Fastjack timestamp |
| `selectedProgrammerSkillSet` | let | `null` | |
| `editingSourceProjectId` | let | `""` | upgrade-edit baseline |
| `purchasedImportDraft` | let | `null` | |
| `remoteDeckState` | let | `null` | server-side state |
| `remoteDeckStateLoadedForCharacterId` | let | `""` | |
| `remoteDeckStateSaveTimer` | let | `null` | |
| `loadPlannerFilter` | let | `"all"` | |
| `loadPlannerDense` | let | `false` | |
| `activeDeckBuildName` | let | `""` | |
| `pendingDeckSelectionAction` | let | `null` | |
| `DECK_STORE` | const | `"sr2_decks_v1"` | |
| `LOADOUT_STORE` | const | `"sr2_loadouts_v1"` | |
| `PROGRAM_STORE` | const | `"sr2_programs_v1"` | (legacy) |
| `SOURCE_STORE` | const | `"sr2_program_sources_v1"` | |
| `COMPILE_JOB_STORE` | const | `"sr2_compile_jobs_v1"` | |
| `COMPILED_STORE` | const | `"sr2_compiled_programs_v1"` | |
| `PROGRAM_MIGRATION_STORE` | const | `"sr2_program_migration_v1"` | |
| `PROGRAM_RECONCILE_STORE` | const | `"sr2_program_reconcile_v1"` | |

### 3.2 Functions, grouped by section

**Helpers / shell:** `$`, `ni`, `cb`, `fmtN`, `fmtY`, `pfFactor`, `clampInt`,
`randomHex12`, `fastjackStamp`, `setInterruptOverlay`, `acknowledgeInterrupt`,
`getProgrammerScopedStoreKey`, `getUtilityOptionExclusions`.

**Programmer Profile (A1):** `getSavedProgrammerProfile`, `getActiveProgrammerId`,
`hasActiveDeckSkill`, `getSelectedProgrammerSkillSet`, `computeProgrammerCapsFromSkillSet`,
`computeProgrammerCaps`, `getCurrentMpcpCap`, `getCurrentUtilCap`,
`getDominantProgrammingSkill`, `getUtilityRatingCap`, `updateUtilityRatingCapUI`,
`canAddUpgradeOptionsFromVersion`, `getUpgradeRatingFloorForUtil`,
`applyUpgradeRatingFloor`, `applyProgrammerCaps`, `loadProgrammerCharacters`,
`updateProgrammerProfilePreview`, `activateDeckBuilder`, `editProgrammerProfile`,
`initProgrammerProfile`.

**Cyberdeck calc (A3 + A4):** `calcDeck`.

**Program / Utility builder (A5 + A6 + A7):** `buildUtilDropdown`, `onUtilTypeChange`,
`onOptionRatingInput`, `onNumericOptionToggle`, `syncOptionRatingCaps`, `getOptVal`,
`computeUtilityFootprint`, `getProgramModsLabel`, `getProgramTypeKey`,
`getProgramTypeLabelFromKey`, `computeProgramEconomics`, `computeProgramFootprintFromState`,
`getCurrentProgramSnapshot`, `getProgrammingTargetNumber`, `getProgrammingSuccessesCap`,
`syncProgrammingSuccessInputBounds`, `getProgrammingSuccesses`, `getPlannedCompileDays`,
`rollProgrammingTask`, `calcUtil`.

**Purchased import (A9):** `populateUtilityDropdownLikeBuilder`,
`getPurchasedImportDefaults`, `getPurchasedImportFootprintState`,
`getPurchasedStreetPrice`, `syncPurchasedImportDraftFromModal`,
`renderPurchasedImportOptions`, `onPurchaseOptionRatingInput`,
`onPurchaseNumericOptionToggle`, `onPurchasedImportTypeChange`,
`onPurchasedImportRatingChanged`, `onPurchasedImportOptionChanged`,
`openPurchasedImportModal`, `closePurchasedImportModal`, `refreshPurchaseImportPreview`,
`submitPurchasedProgramImport`.

**Source / upgrade / compile-job (A8):** `setProgramEditState`, `cancelProgramEdit`,
`parseLegacyMods`, `applyProgramOptionState`, `editSourceProject`,
`ensureSourceFromCompiledArtifact`, `startUpgradeFromCompiled`, `validateSourceUpgrade`,
`buildSourceVersionFromSnapshot`, `getFunctionalProgramSignature`,
`findEquivalentCompiledArtifact`, `findEquivalentQueuedCompile`, `getSourceDisplayName`,
`saveCurrentProgram`, `compileSourceProject`, `finalizeCompileJob`,
`adjustCompileJobDays`, `deleteCompileJob`, `migrateLegacyProgramsIfNeeded`,
`buildSourceVersionFromArtifact`, `reconcileProgramSourcesIfNeeded`,
`renderSavedPrograms`, `renderLibraryGroup`.

**Load planner (A11):** `addToLoadPlanner`, `addProgramToLoadPlanner`,
`finalizeLoadPlannerChange`, `addCompiledProgramToLoad`, `deleteCompiledProgram`,
`recalcLoadPlannerWithWarnings`, `computeLoadUsage`, `getProgramIdentityKey`,
`isOneShotProgram`, `targetIsActive`, `targetHasStorage`, `aggregateLoadPlannerEntries`,
`setLoadPlannerFilter`, `toggleLoadPlannerDense`, `_buildLoadItemFromEntry`,
`addEntryToActive`, `addEntryToStorage`, `removeEntryFromActive`,
`removeEntryFromStorage`, `getLoadedSleazeRating`, `renderLoadPlanner`.

**Persistence (A15):** `_emptyDeckBuilderState`, `_deckStoreContainer`,
`_readLegacyLocalStore`, `_collectLegacyDeckBuilderState`, `_hasAnyStoreData`,
`_isStoreValueEmpty`, `saveDeckBuilderStateToServer`, `scheduleDeckBuilderStateSave`,
`loadDeckBuilderStateFromServer`, `_loadStore`, `_saveStore`.

**Saved decks (A13):** `saveDeckBuild`, `loadDeckBuild`, `deleteDeckBuild`,
`renderSavedDecks`, `getActiveDeckBuild`.

**Saved load-outs (A14):** `saveLoadout`, `loadLoadout`, `deleteLoadout`,
`clearLoadPlanner`, `renderSavedLoadouts`.

**Modals (A12):** `openDeckAlertModal`, `closeDeckAlertModal`, `showAlert`,
`openDeckSelectionForLoad`, `cancelDeckSelectionForLoad`, `confirmDeckSelectionForLoad`,
`ensureDeckSelectedForLoad`.

**Shell shims you ADD (do not exist in live):**
- `setMode(mode)` -- toggle `#centerDeck`/`#centerProgram`,
  `#inspDeck`/`#inspProgram`, `#leftSummaryDeck`/`#leftSummaryProgram`, and the
  `.db-mode.on` class on the mode-switch buttons. Closes the review overlay on leaving
  deck mode.
- `switchTab(idx)` -- thin shim -> `setMode(idx === 0 ? 'deck' : 'program')`.
- `showDeckReview()` / `closeDeckReview()` -- toggle `.open` on `#deckReviewOverlay`,
  re-render the cost table by re-running `calcDeck()`.
- `setDeckFormVisible(bool)` -- toggle `#deckFormView` vs `#deckEmptyState`.
- `newDeckBuild()` -- reset the deck form + load planner, show form.
- `inspectDeckComponent(key)` -- render rules + live numbers for MPCP / B / E / M / S /
  Hardening / Response Increase into `#compDetail`. Source data: `window._deckRows`
  (already populated by `calcDeck`).

The shims must NOT touch any storage; they're purely presentational glue.

### 3.3 DOMContentLoaded init order (mandatory, do not reorder)

1. `await bootstrapAuth()`
2. `await initProgrammerProfile()`
3. `buildUtilDropdown()`
4. `onUtilTypeChange()`
5. `syncProgrammingSuccessInputBounds()`
6. `calcDeck()`
7. `renderLoadPlanner()`
8. `renderSavedDecks()`
9. `renderSavedLoadouts()`
10. `renderSavedPrograms()`
11. `refreshPurchaseImportPreview()`
12. `initNumSteppers($('centerDeck'))` and `initNumSteppers($('centerProgram'))`
13. `setMode('deck')` (default; or whichever mode the previous session ended on if you
    persist that -- otherwise just 'deck').

### 3.4 Inline event-handler map (must match live exactly)

Copy the inline `onclick` / `oninput` / `onchange` strings from
`frontend/deck-builder.html` verbatim onto the equivalent elements. Concretely:

- Deck form fields (`deckName`, `deckType`, `mpcp`, `pBod`, `pEvasion`, `pMasking`,
  `pSensor`, `hardening`, `respIncrease`, `iccm`, `realityFilter`, `activeMem`,
  `ioSpeed`, `offlineStorage`, `deckCasing`, `satlink`, `hitcherJack`) all call
  `calcDeck()` on input/change.
- `utilType` -> `onUtilTypeChange()`, `utilRating` -> `calcUtil()`, `attackDmg` ->
  `calcUtil()`, `programSuccessesInput` -> `calcUtil()`.
- All generated buttons in the saved-decks / saved-loadouts / library / planner /
  compile-jobs lists keep their existing handler names. The renderers
  (`renderSavedDecks`, `renderSavedLoadouts`, `renderSavedPrograms`,
  `renderLoadPlanner`) produce these `<button>` tags themselves; do not edit them.

### 3.5 Input constraints to preserve

Exact attributes from live:

| id | type | min | max | step | value |
|---|---|---|---|---|---|
| `mpcp` | number | 1 | 50 | -- | -- |
| `pBod` `pEvasion` `pMasking` `pSensor` | number | 1 | 50 | -- | -- |
| `hardening` | number | 0 | 10 | -- | 0 |
| `respIncrease` | number | 0 | 3 | -- | 0 |
| `activeMem` | number | 100 | 100 | 10 | -- |
| `ioSpeed` | number | 10 | 10 | 10 | -- |
| `offlineStorage` | number | 0 | 65535 | 10 | -- |
| `utilRating` | number | 1 | 50 | -- | -- |
| `programSuccessesInput` | number | 1 | 50 | -- | 1 |
| `purchaseProgramRating` | number | 1 | 20 | -- | 1 |

`calcDeck()` mutates `min`/`max` at runtime; preserve that behavior.

---

## 4. Sizing, density, and the "no stretched rows" rule

The visual delta is the whole point. The agent before you let labels and fields stretch to
fill columns; we are not doing that this time.

### 4.1 Uniform control sizing (mandatory)

Add ONE page-local CSS block that pins control sizing for every text/number/select/button
inside the deck-builder panes:

```css
/* Uniform 34px control height across the deck-builder */
#deckMain input[type=text],
#deckMain input[type=number],
#deckMain input[type=password],
#deckMain select,
#deckMain .btn,
#deckMain button:not(.infield-num-btn):not(.md3-cdd-btn):not(.db-mode) {
  height: 34px;
  box-sizing: border-box;
  line-height: 1;
}

/* Checkboxes get their own consistent size */
#deckMain input[type=checkbox] { width: 16px; height: 16px; margin: 0; vertical-align: middle; }

/* Mode-switch buttons are vertical and may be taller; exempt them above */
```

The exceptions list is intentional:
- `.infield-num-btn` is the up/down stepper carat from `initNumSteppers`; it lives inside
  a 34px wrapper and would otherwise blow it out.
- `.md3-cdd-btn` is the custom-dropdown trigger; matrix-designer already styles it at
  34-35px via the global `.md3 input[type=number]` rule -- leave it alone.
- `.db-mode` (the left-rail mode switch) is a navigational button, not a form control.

### 4.2 No row stretches to fill space

The live page has several wide rows where a single short field (e.g. MPCP at 60px) sits
beside a giant empty span. In the new layout:

**Rule:** every row's controls must collectively earn the row's width. If the natural
controls don't fill the row, do ONE of these (pick per row, document your choice):

1. **Pack a related control onto the same row.** E.g. on the Deck Spec row, the live page
   has `Deck Name | Deck Type | MPCP` on three separate rows; combine them into one row
   `[Deck Name flex:1] [Deck Type max-content] [MPCP 84px]`.
2. **Shrink the row to its content** with `width: max-content` or `display: inline-flex;
   gap: 10px;` so the column isn't visually under-filled.
3. **Inline a tip / live readout** that's tied to the field (e.g. the `mpcpCapTip` text
   sits to the right of the MPCP field, not below it). The tip is content; it's not a
   layout filler.
4. **Add a logical secondary control** (e.g. a small "reset to cap" button next to a
   numeric field that has a cap).

**Forbidden fillers:** decorative dividers, blank cells, `&nbsp;`, "ghost" labels, fixed
spacers wider than 16px.

### 4.3 Row plan you must produce as a deliverable

Before writing HTML, produce a short table in this spec file (append to Section 11) listing
every row in `#deckFormView` and `#centerProgram` and the chosen filler strategy. This is
for the user to review. Example shape:

```
| Pane | Section | Row | Controls (live) | Plan (new) | Filler strategy |
|---|---|---|---|---|---|
| centerDeck | Deck Spec | 1 | deckName / deckType / mpcp on 3 rows | 1 row: name (flex:1) + type (max-content) + mpcp (84px) | Pack 3 fields onto 1 row |
| centerDeck | Persona Programs | 1 | personaBar (full-width meter) | unchanged | Bar is content, not filler |
| centerDeck | Hardware | 1 | hardening / respIncrease / iccm / realityFilter | 1 row: 2 number boxes + 2 checkboxes inline | Pack |
| centerDeck | Memory & I/O | 1 | activeMem / ioSpeed / offlineStorage on 3 rows | 1 row of 3 .db-membox cells | Pack into equal-width boxes |
| centerDeck | Accessories | 1 | deckCasing / satlink / hitcherJack | 1 row, select + 2 checkboxes inline | Pack |
| centerProgram | Program Spec | 1 | utilType / utilRating / attackDmg | 1 row | Pack |
| centerProgram | Program Options | -- | dynamic | grid, 2 columns at desktop | Pack |
| centerProgram | Load Planner add-row | 1 | loadLabelInput / loadTargetInput / "Add to Load" | 1 row | Pack |
| centerProgram | Load Planner filters | 1 | All / Active / Storage-Only / One-Shot / Dense | 1 row of pill buttons | Pack |
| centerProgram | Saved Load-outs | 1 | loadSaveName / "Save" / "Clear" | 1 row | Pack |
| centerProgram | Library + Compile Jobs | 1 | "Import Purchased" button + libraryLoadSnapshot | 1 row | Pack (snapshot is a chip) |
... etc.
```

If a row can't be packed without crowding, use option 2 (shrink) and note it.

### 4.4 Existing styling primitives you may reuse

These are already in `style.css` or in the previous preview's page-local block. Reuse them
verbatim; do not invent parallel classes.

- `.md3-panes`, `.md3-side`, `.md3-center`, `.md3-tabbar`, `.md3-summary`, `.sum-row`,
  `.md3-insp-empty`, `.md3-num`, `.md3-cdd-*`, `.infield-num-*`
- `.btn`, `.btn-sm`, `.btn-red`
- `.comp-table`, `.ltg-overlay`
- `.sum-row .k / .v` for left-summary rows
- (Page-local) `.db-navgroup`, `.db-spec-row`, `.db-type-select`, `.db-bems`, `.db-mini`,
  `.db-memrow`, `.db-membox`, `.db-fade`, `.db-flash`, `.db-disabled`,
  `.db-mode`, `.db-ind`
- (Page-local) `.lp-remove-btn` -- use `.btn .btn-red .btn-sm` instead for full
  consistency; only fall back to `.lp-remove-btn` if `.btn-red` doesn't fit a generated
  table row.

Delete buttons across the page render as `<button class="btn btn-red btn-sm">x</button>`
(text "x", not a glyph -- ASCII).

---

## 5. Pane mapping (where every live panel lives now)

| Live piece (live id / panel) | New home | Mode | Notes |
|---|---|---|---|
| A0 tab bar (`tabBtn0`/`tabBtn1`) | LEFT rail mode switch (`#mode-deck`/`#mode-program`) | both | Keep `switchTab(idx)` shim |
| A1 Programmer Profile gate | LEFT pane top, OUTSIDE `.deck-builder-app` lock | both | |
| A2 Interrupt overlay | full-screen overlay, unchanged | both | |
| A3 Deck Spec / Persona / Hardware / Memory / Accessories | CENTER `#deckFormView` | Deck | One panel per section, packed rows per Section 4 |
| A4 validity badge (`#validityBadge`) | LEFT `#leftSummaryDeck` | Deck | |
| A4 deck summary grid (`#deckSumGrid`, 13 rows) | LEFT `#leftSummaryDeck` (`.md3-summary` / `.sum-row`) | Deck | |
| A4 persona bar (`#personaBar`) | CENTER Persona Programs panel | Deck | Stays where `calcDeck` writes it |
| A4 component cost breakdown (`#costTable`/`#costBody`) | OVERLAY `#deckReviewOverlay` | Deck | Toggled by `showDeckReview()`/`closeDeckReview()` |
| A5 Program Spec + Options | CENTER `#centerProgram` | Program | |
| A6 utility card / Cost & Avail / Construction Time (`#utilSummaryPanel`, `#utilEmpty`) | RIGHT `#inspProgram` | Program | Including `#utilCard`, `#utilCostGrid`, `#buildTimeMeta`, `#buildTimeGrid` |
| A7 programming roll (GM-only) | CENTER (inside Program Spec) | Program | |
| A8 compile/source machinery | unchanged (no UI of its own) | Program | |
| A9 Purchased import modal (`#purchasedImportModal`) | unchanged (modal) | Program | |
| A10 Program library / Compile jobs (`#savedProgramsList`, `#libraryLoadSnapshot`) | CENTER `#centerProgram` (below program form) | Program | |
| A11 Load Planner (`#loadPlannerArea` + add-row controls) | CENTER `#centerProgram` (above library) | Program | Always visible; live page nested it inside `#utilSummaryPanel` |
| A12 Deck-selection modal (`#deckSelectionModal`) | unchanged | both | |
| A12 Alert modal (`#deckAlertModal`) | unchanged | both | |
| A13 Saved Deck Builds (`#savedDecksList`) + name input (`#deckSaveName`) | RIGHT `#inspDeck` | Deck | If you keep autosave from the previous preview's R5, drop `#deckSaveName`; otherwise keep the input above the list. Default for this rewrite: KEEP the manual Save UI -- autosave decisions are out of scope unless the user asks. |
| A14 Saved Program Load-outs (`#savedLoadoutsList`) | CENTER `#centerProgram` | Program | |
| A15 persistence | unchanged | both | Keep all store keys + element ids |

**Click-to-inspect (right pane in Deck mode):**
- Clicks on the **label** OR the **input** for MPCP / pBod / pEvasion / pMasking / pSensor
  / hardening / respIncrease call `inspectDeckComponent('mpcp' | 'bod' | 'evasion' |
  'masking' | 'sensor' | 'hardening' | 'respIncrease')`.
- `inspectDeckComponent` renders rules text (a static `DECK_COMPONENT_INFO` map you ship
  in the page) plus live size/subtotal/cook/install pulled from `window._deckRows` (which
  `calcDeck` already populates -- verify by reading the live `calcDeck`).
- The empty state is the `.md3-insp-empty` placeholder shown initially.

---

## 6. Element-ID preservation strategy

Persistence in this app is element-id-driven. The simplest correct rewrite keeps every
existing id. Concretely:

- **Do not rename any element id from Section 3.** Copy them into the new shell exactly.
- The new ids you ADD must NOT collide. The minimal additions are:
  `centerCol`, `inspectorCol`, `centerDeck`, `centerProgram`, `deckFormView`,
  `deckEmptyState`, `leftSummaryDeck`, `leftSummaryProgram`, `inspDeck`, `inspProgram`,
  `compDetail`, `deckReviewOverlay`, `mode-deck`, `mode-program`, plus any page-local
  internals you need.
- If you must rename an id, you must update every JS reference to it in the copied script.
  Don't do this unless the user explicitly approves.

`getElementById` returns null silently in JS, so renames that miss a reference will look
like dead controls at runtime. Spot-check by `grep_search` for every id used in inline
handlers after you finish wiring.

---

## 7. Persistence + locking + auth (do not break these)

- `apiFetch` from `shared.js` is the only allowed HTTP entry point. Token headers come
  from `authHeaders()`. Do not write a parallel fetcher.
- The character `deck-builder-state` is fetched/PUT via `loadDeckBuilderStateFromServer`
  and `saveDeckBuilderStateToServer`. Don't change their bodies. They are debounced 250ms.
- `localStorage` keys are programmer-scoped via `getProgrammerScopedStoreKey(baseKey)`.
  Don't bypass that helper.
- The lock state toggles between `deck-builder-locked` / `deck-builder-unlocked` on every
  element with class `.deck-builder-app`. In the new file that's `#centerCol` and
  `#inspectorCol`.
- The profile gate (`#profileGateCard`) must remain interactive while locked.

---

## 8. Phased build plan

Work in this order. Stop after each phase and verify before moving on.

### Phase 0 -- Read

Read live `deck-builder.html` end-to-end. Read `matrix-designer.html`'s shell. Read the
`.md3-*` and `.sum-row` blocks in `style.css`. Read `AGENTS.md`. Do NOT touch any file yet.

### Phase 1 -- Skeleton

Replace `frontend/deck-builder-preview.html` with the shell from Section 2 (HTML only, no
JS yet, no field panels yet). Add the page-local `<style>` block from Section 4. Verify
the file parses (`node --check` on the extracted `<script>`, see Section 9). Page should
load and show the profile gate + empty Builder pane + empty Inspector pane.

### Phase 2 -- Wire script

Copy the inline `<script>` from `frontend/deck-builder.html` **verbatim** into the new
file. Add the shell shims from Section 3.2: `setMode`, `switchTab` (shim),
`showDeckReview`, `closeDeckReview`, `setDeckFormVisible`, `newDeckBuild`,
`inspectDeckComponent`, plus the `DECK_COMPONENT_INFO` map. Append the DOMContentLoaded
init block from Section 3.3. At this point the page won't render anything in the panes
yet, but importing it shouldn't throw -- if the script references a missing id, the
function will simply no-op on that id.

### Phase 3 -- Center: Deck mode

Build `#centerDeck` -> `#deckFormView` with the five panels (Deck Spec / Persona /
Hardware / Memory & I/O / Accessories), packed per the row plan in Section 4.3. Wire every
input's id and event handler from Section 3.4. Verify: change MPCP and watch the left
summary update; change persona values and watch the persona bar update.

### Phase 4 -- Left: summary + mode switch

Confirm `#deckSumGrid` renders the 13-row summary and the validity badge updates. Confirm
the mode switch toggles `centerDeck`/`centerProgram` and `inspDeck`/`inspProgram`.

### Phase 5 -- Right: inspector (Deck mode)

Build `#compDetail` empty-state + the Saved Deck Builds section. Wire
`inspectDeckComponent` to MPCP / B / E / M / S / Hardening / RI clicks (on BOTH label and
input). Verify a click swaps the empty-state with rules + live numbers.

### Phase 6 -- Overlay: Review Build

Build `#deckReviewOverlay` containing the cost table (`#costTable` + `#costBody`) and a
"<< Back" close button. Wire `showDeckReview()` to add `.open` + re-run `calcDeck()`.
Verify clicking the button opens the overlay with the 8-col cost table populated.

### Phase 7 -- Center: Program mode

Build `#centerProgram` with: Program Spec + Options + GM-only programming roll, then Load
Planner (add-row, filters, dense, the consolidated table), then Saved Load-outs (name +
Save + Clear + the list), then Library / Compile Jobs (`#libraryLoadSnapshot` +
`#savedProgramsList` + the "Import Purchased" button). Wire all handlers verbatim.

### Phase 8 -- Right: inspector (Program mode)

Build `#inspProgram` with `#utilEmpty` + `#utilSummaryPanel` containing `#utilCard`
(title/sub/stat-row/note), `#utilCostGrid`, `#buildTimeMeta`, `#buildTimeGrid`. Verify
that selecting a utility renders the card and that Cost & Availability + Construction Time
populate.

### Phase 9 -- Modals + overlay

Build `#purchasedImportModal`, `#deckSelectionModal`, `#deckAlertModal`,
`#deckInterruptOverlay`. Wire their open/close handlers. Verify each opens, populates, and
closes.

### Phase 10 -- Verify (Section 9)

Run the validation checklist. Stop and ask for review.

---

## 9. Validation

Before declaring "done", you MUST run all of these and they must pass:

```pwsh
# 1. Syntax of the inline JS (extract the <script> block; pipe into node --check)
#    Quick check: grep_search for any obviously broken template-string interpolation.
node --check  <(extracted-script.js)

# 2. ASCII / encoding (the pre-commit hook will run this too)
py tools\check_text_hygiene.py

# 3. Backend smoke (does not exercise the new page but proves you didn't break imports)
python -c "import app.main"
python -m pytest -q
```

Then load the page in the browser at `http://localhost:8000/ui/deck-builder-preview.html`
and execute this scripted smoke pass (mirror the existing playwright spec at
`_sr_e2e/deck-preview-smoke.spec.js` if it still exists; otherwise do it by hand):

1. Activate a Static-or-similar PC as programmer.
2. Click "New Deck" (or whatever you've labelled the empty-state action), fill MPCP=6,
   set B/E/M/S to 1/2/3/4. Verify the left summary shows 13 rows and the validity badge
   shows "VALID BUILD".
3. Click "Review Build" -- verify the cost overlay opens with the 8-column table and a
   total row. Close it.
4. Click MPCP input -- verify the inspector shows the MPCP rules + live contribution.
5. Save a build "Smoke Rig". Reload. Verify "Smoke Rig" appears in Saved Deck Builds and
   loads cleanly.
6. Switch to Program mode. Pick Attack-6. Verify the right inspector shows the program
   card + Cost & Availability + Construction Time.
7. Click "Add to Load" -- verify the deck-selection modal opens, confirm with "Smoke Rig",
   verify a row appears in the load planner.
8. Open Import Purchased Program; import a Browse-3. Verify it shows up in the Purchased
   library section.
9. Roll the programming task (GM only). Verify a result appears.
10. Switch back to Deck mode. Verify the Review overlay is closed (auto-closes on mode
    leave) and the deck form is intact.

If any step fails, fix and re-verify before reporting back.

---

## 10. What to report back when you finish

A short message containing:

1. **Files changed** (just `frontend/deck-builder-preview.html`, ideally).
2. **Row plan table** (the one from Section 4.3, filled in for every row).
3. **Any deviations** from this spec (and why).
4. **List of conflicts you stopped to ask about** and their resolutions.
5. **Verification output**: paste the final exit-status of the four commands in Section 9
   and a one-line summary of the manual smoke pass.
6. **Known gaps**: any live behavior you weren't able to port and why.

Do not write a separate change-log doc. Do not "fix" anything you noticed in passing
unless it's the spec.

---

## 11. ROW PLAN (you fill this in -- the user reviews it)

Append your row-by-row layout decisions here before writing HTML. Empty template:

| Pane | Section | Row | Controls (live) | Plan (new) | Filler strategy |
|---|---|---|---|---|---|
| centerDeck | Deck Spec | 1 | deckName / deckType / mpcp on 3 separate rows | 1 row: name (flex:1) + type (max-content) + mpcp (84px); MPCP label is click-to-inspect; cap/brain tips sit below | Pack 3 fields onto 1 row (`.db-spec-row`) |
| centerDeck | Persona Programs | 1 | B/E/M/S in a 2x2 grid + persona bar | 1 inline row of four 72px boxes (`.db-bems`/`.db-mini`), persona bar below | Pack onto one row; bar is content |
| centerDeck | Hardware | 1 | hardening / respIncrease (2-col) + ICCM + RF stacked | hardening+respIncrease inline (`.db-spec-row`), then ICCM and RF as full-width `.chk-row`s (each click-to-inspect) | Pack the number pair; checkboxes are content rows |
| centerDeck | Memory & I/O | 1 | activeMem / ioSpeed (2-col) + offlineStorage own row | 1 row of three equal `.db-membox` cells (each label+input click-to-inspect) | Pack into equal-width boxes |
| centerDeck | Accessories | 1 | casing select + satlink + hitcher | casing select (content width, click-to-inspect) + 2 `.chk-row`s | Shrink select to content; checkboxes are content rows |
| centerProgram | Program Spec | 1 | utilType + brief / utilRating + cap tip / attackDmg (cond) / compile buttons | Stacked fields kept; each is legitimate content (select+brief, rating+cap, conditional attack); compile/cancel buttons inline | Shrink-to-content; the brief/cap tips are content, not filler |
| centerProgram | Program Options | -- | dynamic option grid | `.opt-grid` (2-col desktop) for variable + toggle options | Pack via grid |
| centerProgram | GM programming roll | 1 | successes input + Roll button | inline flex row (input min 160px + button) | Pack |
| centerProgram | Load Planner add-row | 1 | label / target select / Add button | one `.add-load-row` flex row | Pack |
| centerProgram | Load Planner filters | 1 | All / Active / Storage-Only / One-Shot / Dense | one `.lp-controls-row` of pill buttons | Pack |
| centerProgram | Load Planner table | -- | consolidated table | unchanged consolidated table (+S/-S/+A/-A ops) | Content |
| centerProgram | Saved Load-outs | 1 | name / Save / Clear + list | inline row (name flex:1 + Save + Clear) + table | Pack |
| centerProgram | Library / Compile Jobs | 1 | Import button + snapshot + list | button row + snapshot chip + grouped artifact tables | Pack (snapshot is a chip) |
| centerProgram | Fabrication Queue | -- | (not in live) deck builds + program compiles | content table (phase / days-left / admin ops) | Content |
| inspector(Deck) | Saved Deck Builds | 1 | name input + Save + list | inline row (name flex:1 + Save) + table (Load / Delete) | Pack |

> Note: this rewrite evolved the existing 3-pane preview in place (user chose to carry forward its Build-It/Buy-It + GM-approval + Fabrication-queue workflow, which only exists in the preview). The packing above was already largely present; the deltas applied were explicit Save (drop form autosave), memory-snap OFF (match live), uniform 34px control height incl. buttons, and extended click-to-inspect (ICCM / Reality Filter / Active Mem / I/O / Storage / Casing / Satlink / Hitcher).

---

## 12. Pre-flagged ambiguities (you MUST ask the user about these before assuming)

These are the things this spec deliberately doesn't decide. Ask once, batch the answers,
then proceed.

1. **Autosave vs explicit Save** for deck builds. The previous preview switched to a
   600ms-debounced autosave (`scheduleDeckAutosave`) and removed `#deckSaveName`. This
   rewrite defaults to **explicit Save** (matches live). Confirm with the user.
2. **Click-anywhere-to-inspect** scope. Spec says MPCP / B / E / M / S / Hardening / RI.
   The user may want ICCM / Reality Filter / Active Memory / I/O / Storage / Casing /
   Satlink / Hitcher too. Ask.
3. **Construction Task panel** (V7 in the prior round). The previous preview added an
   aggregate Cook/Install roll inside the Review overlay. This spec **does not** include
   it -- ask whether to port it. If yes, expose only `getDeckBrDice`, `getDeckSuccesses`,
   `computeDeckConstruction`, `renderConstructionTask`, `rollDeckConstruction` (port from
   the previous preview verbatim); don't reinvent.
4. **Validity flash** ("INVALID BUILD" red pulse from T3). Default ON. Confirm.
5. **Disabling B/E/M/S until MPCP >= 1** (U1). Default ON. Confirm.
6. **Empty-state on programmer change** (T5). Default ON. Confirm.
7. **Delete buttons as text "x"** (`.btn .btn-red .btn-sm`) everywhere, or keep the live
   page's `[x]` text-glyph buttons? Default: `.btn .btn-red .btn-sm` with content `x`.
8. **No load confirmation dialogs** (V8). Default ON (silent load). Confirm.
9. **The mode the page starts in.** Default: always 'deck'. Alt: remember last mode in
   localStorage. Confirm.
10. **Memory-field snap-to-multiple-of-10** (V4). The live page doesn't do this; the
    previous preview did (1s debounced snap). Default OFF (match live). Confirm.

---

## 13. Don'ts (anti-checklist)

- Don't touch `frontend/deck-builder.html`.
- Don't rename element ids without approval.
- Don't introduce a parallel HTTP helper, alert helper, escape helper, or auth helper.
- Don't paste unicode glyphs (`,`, `,`, `,`, smart quotes, etc.).
- Don't add docstrings or change-log comments to copied code.
- Don't refactor while porting. Port first; flag refactors in your final report.
- Don't add "improvements" that weren't asked for (no toast notifications, no keyboard
  shortcuts, no theme switcher, no analytics).
- Don't add CSS to `style.css`. All page-local CSS goes in a `<style>` block inside the
  new file.
- Don't commit or push. The user runs git themselves.

---

End of spec.
