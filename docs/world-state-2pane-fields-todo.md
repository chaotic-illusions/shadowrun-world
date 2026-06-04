# World State 2-Pane -- Field/Layout Refinements (batch 2)

Branch `worldstate-2pane`. Sandbox = **frontend/world-state-preview.html** (CSS in `<style id="ws-2pane">`
+ glue in the inline `<script>` near `</body>`). `world-state.js`/`world-state.html` stay UNTOUCHED
(live unaffected); all behavior is added by wrapping the global builder/opener fns in the preview's
inline script and scoped CSS. Verify with Playwright in `D:\Code Projects\_sr_e2e\ws2pane.spec.js`
(stub `/auth/verify` + the 6 loadAll endpoints; spin a transient server then tear it down -- no
lingering test envs). Mark each item [x] when done.

## Global (ALL right-pane modals: npc / editOverlay / org / loc / char)
- [x] A. Textareas auto-grow to fit content (no inner scrollbar, no resize grip); pane scrolls.
      JS `autoGrow`/`growAll` (run on open via the opener wrapper + on `input`), CSS `resize:none;
      overflow:hidden`. Verified: long description grew to fit, no overflow, resize disabled.
- [x] B. Political Relationships (`.chk-list`) `max-height:none; overflow:visible` -- grows to data.

## Organizations
- [x] C. Command Structure: Name 23% (~+22px), Notes 32% (-15px), Title/Role = rest (widest).
      Measured Name 170 / Title 290 / Notes 236.

## Telecom Numbers
- [x] D. Number + Description set to the Visibility dropdown's height (38px) + text size (--fs-lg).

## Matrix Hosts
- [x] 1. Uniform 36px height across all line-1 + line-2 controls (verified heights equal).
- [x] 2. RTG shows CODE-only when closed, full `CODE -- Region` when open (focus/blur text swap);
      field shrunk to ~code width. Verified closed text == value.
- [x] 3. ID Code placeholder `-`.
- [x] 4. Description height matches the other controls (same 36px rule).
- [x] 5. Security Value -> number spinner (`initNumSteppers`, 2-14), Security Code stays a dropdown.
- [x] 6. Reveal + Delete wrapped in `.host-ctrls`, stacked, group centered vs the box (verified ~0).
- [x] 7. Each host is now a bordered BOX (amber-tinted) with spacing -- clear separation (supersedes
      the dim line, which is removed).
- [x] 8. Field labels bumped to --fs-sm in both Telecom + Matrix Hosts, non-bold, no glow.
- [x] 9. Telecom header labels: font-weight 400, no text-shadow, larger -- crisp now.
- [x] 10. CHOSEN layout applied: Description up to line 1; Visibility + Security on line 2; both lines
      boxed; Reveal/Delete outside the box on the right, centered. LTG/ID Code shrunk; freed space went
      to a wide Description on line 1.

## Batch 2b (follow-up requests)
- [x] E. Matrix-host box tint changed from amber to steel / muted-cyan (`border #2b5b66`, bg
      `rgba(0,200,255,.04)`) to match the matrix-designer Matrix theme.
- [x] F. Org editor AUTO-SAVE: removed the Save/Cancel footer buttons; edits now debounce-save (1s)
      via a silent PATCH with a quiet status line ("Saving... / All changes saved OK / Save failed"),
      mirroring the matrix-designer pattern. Reuses world-state's payload getters (shared globals);
      does NOT reuse saveOrgEdit() (that closes the pane + loadAll on success). Skips while name is
      empty; runner (read-only) view unaffected. NOTE: app-wide rollout to the loc/char edit modals
      is the same pattern but each needs its own silent-save payload -- not yet done (org only so far).

## Decisions
- #10 layout (CHOSEN): Description moves UP to line 1 (with RTG/LTG/ID Code); Visibility + Security
  Code/Value go to line 2. Wrap those two field-lines in a BOX. Reveal + Delete sit OUTSIDE the box,
  on the right, vertically centered against the box. (Implemented by restructuring each host row in
  the preview's oeAddHost wrapper: move the 6 field cells into a `.host-box` grid, leave reveal/delete
  as flex siblings centered against it.)
- Command Structure (C): going with 10 off Title + 10 off Notes, +20 to Name.
- ID Code (#3): placeholder `-` (value stays blank).
- Labels (#8): telecom th + host field labels unified at --fs-sm (0.7rem), non-bold, no glow (also #9).
- Separator (#7): the per-host box (border + gap) now provides the separation; the old dim bottom
  line is removed in favor of clear boxed rows.
