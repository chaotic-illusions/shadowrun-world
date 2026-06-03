# World State -- 2-Pane Redesign (session handoff)

Branch `worldstate-2pane` (off `matrix2-designer-3pane`). Sandbox = **frontend/world-state-preview.html**
(a full copy of world-state.html + dock CSS; loads the real style.css + world-state.js, so dossiers
populate with live data). Iterate here; port into the live world-state.html once approved.
Isolated test server on :8771 serves `/ui/`. Update this file + check items off after EACH step.

## Goal (user)
Upgrade the preview's CSS-only docked-modal into a real **persistent 2-pane**:
1. Right pane **always visible** so the main content never shifts when something is selected.
2. Right pane **wider** (the dossiers/edit modals are wide; the current 560px smushes them).
3. Pane **top sits under the nav bar** (header), not overlapping it; full height minus header, with a gap.
4. Pane is a **rounded-corner holder** (border + radius).
5. **Idle state** when nothing is selected: animated rotating phrases ("... awaiting input",
   "... scanning Matrix", + a random pool of others), with a terminal-style blink/typing feel.

## Design
- The five dossier/edit overlays are docked into the pane box: `#npcOverlay`, `#editOverlay`,
  `#orgEditOverlay`, `#locEditOverlay`, `#charEditOverlay`. Utility overlays stay centered modals:
  `#srConfirmOverlay`, `#srAlertOverlay`, `#standingEditorOverlay`, `#srPromptOverlay`.
- A persistent `<aside id="wsPane">` holder is always in the layout (fixed, right of the centered
  content column, under the header, rounded). `#wsIdle` lives inside it and is hidden via
  `body:has(#npcOverlay.open) ... { display:none }` (explicit list -- NOT all .ltg-overlay, so the
  utility modals don't blank the idle text). The docked overlays sit on the same box as `#wsPane`.
- Reserve space permanently: main is always shifted left by half (pane+gap) so the content+pane pair
  stays centered and NOTHING moves when a dossier opens (vs the preview, which only shifts on open).
- Header height is measured into `--ws-hdr-h` (JS, on load + resize) so the pane top tracks the nav.
- Responsive: below the side-by-side threshold, fall back to a right-docked pane (no main shift) /
  stack, so cards stay usable.

## TODOs
- [x] 1. Added the persistent `#wsPane` holder + `#wsIdle` markup (after `</main>`).
- [x] 2. Pane always visible, UNDER the header (`top: var(--ws-hdr-h) + gap`, `bottom: gap`),
      rounded holder (border + radius:14px), width **660px**. `--ws-hdr-h` measured via JS on
      resize + `load` + `document.fonts.ready` (the webfont grows the nav after first paint, so the
      initial read was stale at 55 vs the real 71 -- now re-synced after fonts load).
- [x] 3. Permanent space reservation: `main { transform: translateX(-(pane+gap)/2) }` ALWAYS, so the
      content+pane pair stays centered and nothing moves when a dossier opens.
- [x] 4. Docked the 5 overlays (`#npcOverlay/#editOverlay/#orgEditOverlay/#locEditOverlay/
      #charEditOverlay`) onto the pane box (verified `modalLeft == paneLeft == 1242`, width 660,
      rounded, under header). Idle hidden via explicit `body:has(#...Overlay.open) #wsIdle`.
- [x] 5. Idle animation: `#wsIdleText` rotates a phrase pool every ~3.4s (fade), blinking `_` cursor
      (`wsBlink`) + scanning `...` dots (`wsScan`). Pool in the inline script (10 phrases, random start).
- [x] 6. Responsive: `<=1940px` right-docks the pane + pads main (no shift); `<=1200px` hides the
      holder and restores centered modals.
- [~] 7. Visual pass DONE for idle + a docked overlay (orgEdit) at 1920px -- pane under nav, 660px,
      rounded, idle centered, dossier docks aligned, no JS errors, main not shifted. STILL TODO:
      open each REAL dossier (org/location/contact/npc) with data (test DB had 0 records) + a
      close->idle-returns check + narrow-screen screenshot. Screenshots: _sr_e2e/ws-idle.png, ws-docked.png.
- [ ] 8. (LATER, after approval) Port the approved 2-pane into the live world-state.html.

## Status / notes
- Foundation COMPLETE in the preview sandbox and visually confirmed (ws-idle.png / ws-docked.png).
  Pane = persistent, 660px, rounded, under the nav; dossiers dock in; idle rotates; main never shifts.
- Remaining: finish #7 (real-data dossier open + close-returns-to-idle + narrow screenshot), tune
  width/phrasing to taste, then #8 port to live world-state.html. The :8771 test DB is empty for
  orgs/locations/contacts, so seed or test against a populated DB to exercise real dossiers.
