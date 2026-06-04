# Deck-Builder (and Matrix-Run) 3-Pane Redesign -- session handoff / TODO

Branch `worldstate-2pane`. Goal: reduce the single-column busy-ness of deck-builder by
adopting the **matrix-designer 3-pane shell** (the `.md3` look/feel). Then give matrix-run
the same treatment. Build a **static prototype first**, then a data-wired **-preview**, then
port to live -- same flow used for world-state / the manage pages. Test on the local :8000
instance (admin token in the user's message; Playwright harness in `D:\Code Projects\_sr_e2e`).

## Decisions locked with the user (2026-06-04)
1. **Order**: deck-builder FIRST (fully, get sign-off), THEN matrix-run.
2. **Flow**: static prototype in `frontend/prototypes/` -> approval -> wired `*-preview.html`
   -> approval -> port to live. (Do NOT touch live `deck-builder.html` until approved.)
3. **Deck-builder shell**: ONE 3-pane shell (no top tab-bar). The current two tabs
   (Cyberdeck Builder / Program Builder) become a **left-pane vertical nav mode switch**.
4. **Pane mapping**: Summary on the LEFT, Inspector on the RIGHT (mirrors matrix-designer).
   Reconciliation of #3 + #4 -> the LEFT pane stacks: section NAV (top) + live SUMMARY/cost
   (below). CENTER = the selected section's controls. RIGHT = inspector for the selected
   item + Saved Builds.

## Reference: the matrix-designer md3 shell (copy its structure + CSS)
- `frontend/matrix-designer.html`: `.md3-tabbar` (top), `.md3-panes` (CSS grid), three
  children: `.md3-side` (left summary, `#md3SummaryMount`), `.md3-center` (workspace),
  `.md3-side` (right inspector, `#mdInspector` with an `.md3-insp-empty` placeholder).
- `frontend/style.css`: `.md3-panes { grid-template-columns: 248px minmax(0,1fr) 360px }`
  (~line 2754) plus the whole `.md3-*` block (panes, side, center, insp, num inputs, chips,
  custom dropdown `.md3-cdd-*`). md3 number inputs use `.md3-num` and `initNumSteppers`.
  md3 input height rules live ~lines 2744-2752. The `.md3` scope keeps it from leaking.
- Inspector pattern: click an item in the center -> render its editor into the right pane
  (`mdInspector.innerHTML = ...`), with an empty-state placeholder otherwise.

## Deck-builder content inventory (live deck-builder.html)
Top: Programmer Profile. Tab bar: "Cyberdeck Builder" (tab 0), "Program / Utility Builder" (tab 1).
- Tab 0 panels: Deck Specification, Persona Programs, Hardware Components, Memory & I/O,
  Accessories, Deck Summary, Component Cost Breakdown, Saved Deck Builds.
- Tab 1 panels: Program Specification, Program Options, Cost & Availability, Construction Time,
  Deck Load Planner, Saved Program Load-outs, Program Library / Compile Jobs,
  Purchased Program Options, Import Summary.

### Proposed 3-pane placement (refine in the prototype)
- LEFT (`.md3-side`):
  - NAV (top): Cyberdeck > [Deck Spec | Persona Programs | Hardware | Memory & I/O | Accessories];
    Program > [Program Builder]. Selecting an entry sets what CENTER edits.
  - SUMMARY (below, sticky): live deck totals (rating/MPCP/etc.), Component Cost Breakdown,
    validity/over-cap warnings. (For Program mode: Cost & Availability + Construction Time.)
- CENTER (`.md3-center`): the selected section's controls only (de-clutters the column).
- RIGHT (`.md3-side` inspector): details/editor for the selected program/component/load slot;
  Saved Deck Builds + Saved Program Load-outs + Program Library live here too (or as a
  right-pane sub-tab). Empty-state placeholder when nothing selected.

## TODO -- Deck-builder (do these in order; check off as completed)
- [ ] D1. Copy `matrix-designer.html`'s md3 shell markup into a new static prototype
      `frontend/prototypes/deck-builder-3pane.html` (placeholder data, no JS wiring yet).
      Reuse `style.css` `.md3-*` classes; do not fork the CSS.
- [ ] D2. Lay out the LEFT nav + summary, CENTER section host, RIGHT inspector with an
      empty-state. Wire ONLY the nav -> center section switching (static content blocks).
- [ ] D3. Map every live panel into a pane (use the inventory above). Confirm nothing is
      dropped: list each live panel -> its new home. Flag anything with no obvious home.
- [ ] D4. **User review of the static prototype** (layout/feel) before any data wiring.
- [ ] D5. Create `frontend/deck-builder-preview.html` = the approved shell wired to the real
      deck-builder JS/data (port the existing logic into the 3-pane DOM; keep behavior).
- [ ] D6. Inspector interactions: click a program/component/slot -> editor in the right pane;
      live summary/cost updates in the left pane. Saved builds load/save still work.
- [ ] D7. Playwright coverage in `_sr_e2e` against :8000 (build a deck, see summary update,
      inspect an item, save/load a build, switch to Program mode). Zero page JS errors.
- [ ] D8. **User review of the wired preview.**
- [ ] D9. Port approved preview into the live `deck-builder.html`.

## TODO -- Matrix-run (Phase 2, after deck-builder sign-off)
- [ ] M1. Decide target layout with the user (likely a 3-pane "run console": left = decker/host
      status, center = event log + actions, right = active IC / trap doors / paydata / hostile
      deckers inspector). Setup screen vs live-run screen handling TBD.
- [ ] M2. Static prototype `frontend/prototypes/matrix-run-3pane.html`.
- [ ] M3. User review -> `frontend/matrix-run-preview.html` wired -> tests -> review -> port.

## Notes / gotchas
- Text hygiene pre-commit hook rejects non-ASCII -- keep all new files ASCII (use --, ->, ...).
- Don't touch live pages until the matching review step is approved.
- Playwright: override baseURL to http://localhost:8000, inject the admin token into
  localStorage via addInitScript (see `_sr_e2e/manage-autosave.spec.js`).
- Related prior work: `docs/matrix-designer-3pane-port-plan.md` (how the md3 shell was built),
  `docs/manage-pages-autosave-plan.md`.
