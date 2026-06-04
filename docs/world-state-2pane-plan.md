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
- [x] 7b. Round-2 user feedback addressed + verified (Playwright _sr_e2e/ws2pane.spec.js, real
      populated org via stubbed /auth/verify + /organizations/ since the :8770/:8771 DBs are empty
      AND token.txt is stale/401):
      (a) WIDER: --dock-w 660->780; org editor (8-col matrix-host table) now fits with NO horizontal
          scroll -- forced overflow-x:hidden on docked bodies + table-layout:fixed + width:100%
          min-width:0 inputs so the tables reflow/squish instead of scrolling. Measured body
          scrollWidth==clientWidth (overflow 0) at both 2200px (centered) and 1700px (right-dock).
          Centering breakpoint moved 1940->2040 for the wider pane.
      (b) ROUNDED: docked .ltg-modal/.edit-modal/.edit-modal-mini got `overflow:hidden` so the
          head/body backgrounds no longer clip the holder's 14px radius. Confirmed radius 14px +
          overflow hidden; screenshots ws2-org-wide.png / ws2-org-narrow.png show clean corners.
      (c) SWAP: inline glue now wraps openNpc/openOrg/openLoc/openCharEditModal to close the other
          four docked overlays first, so clicking a different card updates the pane in place (no
          close needed). Verified: open 901 then 902 -> title swaps to Halloweeners, exactly 1
          docked overlay open. Also fixed editOverlay selector (.edit-modal-mini, not .ltg-modal)
          in the dock + narrow media query.
      NOTE re-test setup: served file is correct on BOTH :8770 and :8771; use Playwright baseURL
      (:8770) and STUB /auth/verify + the 6 loadAll endpoints -- token.txt no longer authenticates.
- [ ] 8. (LATER, after approval) Port the approved 2-pane into the live world-state.html.

## Status / notes
- Foundation COMPLETE in the preview sandbox and visually confirmed (ws-idle.png / ws-docked.png).
  Pane = persistent, 660px, rounded, under the nav; dossiers dock in; idle rotates; main never shifts.
- Remaining: finish #7 (real-data dossier open + close-returns-to-idle + narrow screenshot), tune
  width/phrasing to taste, then #8 port to live world-state.html. The :8771 test DB is empty for
  orgs/locations/contacts, so seed or test against a populated DB to exercise real dossiers.
