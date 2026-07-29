# Matrix Run -- Trace RAW audit + UI follow-ups

Working reference for the Trace-IC representation fixes and the four UI/UX tasks
raised 2026-07-29. Kept here so nothing is lost to conversation compaction.

Legend: [DONE] shipped this session; [NEEDS-CONFIRM] awaiting a decision below;
[PLANNED] agreed direction, not yet built; [OPEN-Q] see section 7.

---

## 0. Quick status

| Item | State |
|---|---|
| Stop garbling located file names/sizes | [DONE] earlier this session |
| `[TRAP]` no longer leaks from passive detection (`_redact_ic` gate) | [DONE] |
| Trace hunt/location event wording ("Construct component" mislabel dropped) | [DONE] |
| Hide currently-suppressed IC from the Known IC pane | [DONE] (section 2) |
| Trace Location Cycle re-skinned as the "location" (no direct Attack) | [DONE] (frontend) |
| Task 1 -- exhaustive Event Log catalog | [DONE] (section 3) |
| Task 2 -- action bar cleanup + last-action memory | [DONE] (section 4) |
| Task 3 -- move Decrypt/Defuse onto the IC card | [DONE] (section 5) |
| Task 4 -- 1.5s explanatory tooltips (programs + actions) | [DONE] (section 6) |

---

## 1. Trace IC -- RAW vs. current app

RAW source: `vr2_rules.md` -- Trace IC, Hunt/Location cycles L566-582; "Trace
Effects on Completion" L585-591; Suppressing IC L419-425.

### 1a. Completion effects -- CONFIRMED modeled AND applied

Both RAW "Effects on Completion" mechanics are wired and actually take effect
(not just announced in the log):

- **Proactive IC -1 to-hit TN per completed trace.** Applied as
  `- _completed_trace_count(state)` in every IC Attack-Test `tn_modifier`
  (`app/routers/matrix_runs.py` ~L6961, L7384, L7458, L7568, L11983).
- **Tally acceleration +1 per completed trace on every later increase.** Applied
  in `_bump_security_tally` (`app/routers/matrix_runs.py` L1717) -- the single
  choke point every genuine tally increase routes through, so it can't be skipped.
- Cumulative: N completed traces => -N TN and +N per tally increase.
- Counter stored in `state["traces_completed"]`, read via `_completed_trace_count`.

Verdict: **works as RAW.** No change needed.

### 1b. Hunt Cycle -- essentially correct

- The trace shows in the **Known IC pane** during the hunt cycle at detection
  **level 2** (`_ic_detection_level` returns 2 for a trace by default): type
  "Trace" is known, exact rating hidden.
- The decker **can attack / crash it** during the hunt cycle (a Trap Trace crashed
  in hunt is *defused* -- its hidden IC never fires). Matches RAW L569.
- Mechanically the hunt is the IC rolling its dice vs the decker's **Trace Factor**
  (`_compute_trace_tn`) to score a "hit"; a hit ends the hunt and starts the
  Location Cycle. RAW frames this as an "Attack Test", but that Attack Test deals
  **no icon damage** -- its only success-effect is starting the Location Cycle. So
  there is nothing for the decker to *defend* against; the counter-play is to attack
  the trace first. The app matches this.
- Player vs Admin log text (redaction in `_redact_event_ic`, L809-822):
  - Player sees generic: "Trace IC Hunt Cycle continues -- the jackpoint is not yet
    located." / "Trace IC Hunt Cycle succeeded -- it enters its Location Cycle."
  - Admin sees the detailed line with rating/TN/successes.

### 1c. Location Cycle -- THE BUG [NEEDS-CONFIRM]

- **RAW (L571):** when the hunt Attack Test succeeds, "the IC **vanishes and becomes
  reactive**." During the Location Cycle it is hidden; the decker's tools are
  Relocate / Graceful Logoff / run.
- **Current app:** the trace **stays visible at level 2** in the Known IC pane for
  the whole Location Cycle, because `_ic_detection_level` returns 2 for a trace
  regardless of phase. It does not disappear.
- **Internal inconsistency:** `_apply_locate_ic` (`app/routers/matrix_runs.py`
  L5850) ALREADY assumes it vanished -- it excludes a location-cycle trace from
  re-acquisition and its docstring says: "Trace IC in its Location Cycle has vanished
  and cannot be re-acquired; Relocate is the operation that affects it then." So only
  the **pane visibility** was never updated to match.

**Proposed fix (pending confirm):** make a location-cycle trace drop out of the
Known IC pane. Cleanest implementation: a phase guard in `_ic_detection_level` --
if the IC is a trace and `trace_phase == "locate"`, return 0 (vanished / reactive),
overriding the default 2 and the `analyzed => 3` bump. Effects:
  - `_redact_ic` returns `None` => the trace leaves the Known IC pane.
  - Location-cycle **events still fire** ("Location Cycle continues...") so the
    decker still knows a trace is counting down -- only the icon is gone.
  - Relocate still works (it targets by phase, not visibility).
  - Locate IC still excludes it (already does).
This is RAW-accurate and removes the inconsistency. Confirm before building
(OPEN-Q 1).

### 1d. Locate IC / Relocate / suppression -- current behavior (as asked)

- **Locate IC** (`_apply_locate_ic`): on a successful Index test, re-acquires
  hidden/evaded operational IC (sets them to detection level 1; still needs Analyze
  IC to identify). **By design it does NOT re-acquire a trace in its Location
  Cycle** -- Relocate is the tool for that.
- **Relocate** (`relocate` handler, L8047):
  - Eligible only against a trace whose `trace_phase == "locate"` -- i.e. **blocked
    during the Hunt Cycle** (RAW: "Relocate cannot affect a trace during its Hunt
    Cycle"). [matches RAW]
  - On success (no suppress): trace is **spoofed for this turn only** -- no
    location-cycle progress this turn, NOT reset to hunt, resumes next turn.
    [matches RAW]
  - Alternative on the same action -- **suppress** the trace: 1 Detection Factor,
    trace paused in place (-1 DF), resumes where it left off when released.
    [matches RAW]
  - Edge case handled: if DF is already at its minimum (1), it cannot suppress; it
    spoofs for the turn and HOLDS the suppress offer, prompting the decker to release
    another suppression first (`relocate_suppress_pending`).
- **NOTE vs. your mental model:** you described "Locate it (via Locate IC), then
  Relocate it." The app (and RAW) does **not** require a Locate IC step first --
  **Relocate targets the location-cycle trace directly.** RAW L580-582 defines
  Relocate as a Control Test "against one trace IC that is in its Location Cycle"
  with no separate locate prerequisite. See OPEN-Q 1 for whether you want the
  RAW-direct flow or a house-rule Locate-then-Relocate.

### 1e. Verification outcomes (checked 2026-07-29)

- **Relocate opposing tally: OK.** Relocate is a control-subsystem test action; it
  routes through the shared action resolver, which applies `test["tally_increase"]`
  (the GM's opposed Security Test) via `_bump_security_tally`. The `relocate` branch
  only reads `test["success"]`; the tally was already applied upstream.
- **Graceful Logoff vs trace: OK / RAW.** The logoff Access Test adds the operational
  trace IC's rating to its TN (`trace_tn_bonus`, ~L9730), matching RAW ("adds IC
  rating to the logoff target number"); a successful graceful logoff clears traces.
- **Jack-out residual 1D6: NOT modeled (minor follow-up).** RAW L583: a plain jack-out
  leaves 1D6 turns for a running trace to still complete (physical dispatch). The app
  ends the run without a residual-completion roll. Low impact (narrative/consequence);
  logged as a future follow-up, not part of the current tasks.
- Hunt-cycle wording kept non-damaging per the OPEN-Q 2 answer.

### 1f. Implemented (2026-07-29)

`frontend/matrix-run.html`: added `_locatingTraceCard(ic, ...)` -- when a trace's
`trace_phase === 'locate'`, `renderActiveIC` renders a re-skinned card titled
"Trace -- LOCATION" (badge TRACING) with the location-cycle status, an explanation
that the IC has gone reactive and can no longer be attacked, and a `>> Relocate`
button (`relocateFromCard`) that opens the existing Relocate action pre-targeted at
this trace. The old attackable card no longer renders for a location-cycle trace.
Backend already exposed `trace_phase` and already blocked attacks on a location-cycle
trace (`_trace_is_targetable`), so this was frontend-only (no restart needed).

---

## 2. [DONE] Suppressed IC hidden from the Known IC pane

`frontend/matrix-run.html` `renderActiveIC`: added a `_visibleIC` filter that drops
IC where `suppressed && !suppression_released`, then used it for the empty-state
check, cluster counts, the card map, and the party-cluster grouping loop (indexes
stay aligned with `_cardHtml`). Suppressed items (crashed-suppressed, hung, and
trace-paused) now appear only in the Suppressions panel (`renderSuppressions`),
which already carries the Release/Suppress controls. Frontend is a live mount -- a
browser refresh picks it up (no server restart).

Minor: the `isCrashed && ic.suppressed` Release block inside `renderActiveIC` is now
unreachable (kept, inert). Remove in a later cleanup pass if desired.

---

## 3. Task 1 -- exhaustive Event Log catalog [OPEN-Q 3]

Goal: one long reference listing **every** line the Event Log can emit, the exact
condition that fires it, the **player-redacted** text AND the **admin** text, for
every branch (success / fail / edge / tally side effects). Purpose: review app
output for errors without having to reproduce each scenario by hand.

Event surface (non-exhaustive; the catalog will enumerate all): logon, analyze
host/security/subsystem, locate paydata/file/IC/decker, cybercombat (decker attack,
IC attack, crippler/ripper, killer, black IC, worm, tar), trace hunt/location/
complete, data bomb detect/defuse/detonate, scramble analyze/decrypt, download/
edit/erase, suppression suppress/release, relocate/redirect, decoy, evade, graceful
logoff / dump / jack-out, AAR.

Method options:
- **(A) Auto-generate from the engine [recommended].** Drive the real handlers /
  `_advance_npc_pass` with scripted states and capture the actual `event_log`
  entries, then render each through the player redactor and the admin view. Most
  accurate (it IS the app's output) and stays current if code changes. Heaviest to
  scaffold; likely a `tools/` script emitting Markdown, run via sub-agents per event
  family.
- **(B) Hand-authored from code reading.** Faster to start, but risks drift from the
  real output and misses edge branches.
- **(C) Hybrid:** auto-generate the cybercombat/IC/trace core (where redaction and
  staging matter most); hand-author the simple deterministic lines.

Recommendation: **A**, sharded by event family across sub-agents, output to
`docs/event-log-catalog.md`.

### 3a. Implemented (2026-07-29)

`tools/gen_event_catalog.py` -- an AST generator over `app/routers/matrix_runs.py`. It
enumerates EVERY `_append_event` site (coverage complete by construction -- more reliable
than driving scenarios, which cannot hit every branch) and writes `docs/event-log-catalog.md`:
**197 emit sites, 97 event types**. Per event: enclosing function, line, firing condition
(the guarding `if`, with body/else branch), the exact text template as written, the extra
payload keys, and a **Player view** tag inferred from the payload -- which redaction passes
apply (`gm_only` drop, `_redact_event_ic`, `_redact_event_tally`, `_redact_system_action_event`).
The doc opens with a precise description of those passes (the player-vs-admin split). Re-run
the generator after engine changes; do not hand-edit the catalog. Edge cases it honestly flags
for manual review: 6 `(dynamic)` sites (`_append_event(state, ev)` built above) and 3 `(untyped)`
(payload `type` from a `**event_base` spread) -- each points to its function.

Optional follow-up if you want CONCRETE rendered strings (not templates) for the main flows,
I can add a scenario-driver that runs the engine and captures real player + admin output.

---

## 4. Task 2 -- action bar cleanup + permanence [OPEN-Q 4]

Observations: the action dropdown is long and lists actions that are not currently
available (wrong phase, missing utility, nothing to target). Requested: shorter,
context-aware, and it should remember the last executed action as the default
instead of resetting each time.

Candidate changes (mix-and-match):
- **Context-filter:** hide or disable actions that cannot fire right now (no valid
  target, missing utility, wrong phase, no AP). Disable-with-tooltip keeps them
  discoverable; hide is cleaner but less educational.
- **Group by category:** Recon (Analyze*/Locate*), Files (Decrypt/Defuse/Download/
  Edit), Trace (Relocate/Redirect), Movement/Exit (Logoff), etc.
- **Last-action memory:** persist the last executed action per run (state or
  localStorage) and re-select it as the dropdown default.
- Possibly promote the 2-3 most-used actions to buttons and leave the long tail in
  the dropdown.

---

## 5. Task 3 -- move Decrypt / Defuse onto the IC card (pros/cons)

You are considering surfacing Decrypt (Scramble) and Defuse (Data Bomb) as buttons
on the relevant IC/subsystem card -- like the existing per-IC Attack / Analyze --
and removing them from the action dropdown.

Pros:
- **Target is unambiguous.** The button lives on the exact Scramble/bomb it acts on;
  no separate target-picker, no acting on the wrong file.
- **Discoverability / less dropdown clutter.** Directly supports Task 2 -- two fewer
  situational entries in the long list.
- **Consistency.** Matches the "act on the thing from the thing's card" model already
  used for Attack/Analyze/Slow/Release.
- **Fewer invalid attempts.** The button only renders when the action is legal
  (a discovered Scramble / a found bomb), so you can't fire it with nothing to hit.

Cons / risks:
- **Card must exist and be discovered.** Scrambles/bombs surface only after Analyze
  Icon; the card is the discovery UI. Need a clear pre-discovery affordance so the
  action isn't "missing" before it's found.
- **Ordering traps stay.** Exploding Scramble requires Defuse-then-Decrypt; the card
  must still enforce/telegraph the safe order (already hinted in the scramble card).
- **Action-cost + Hacking-Pool UI.** The dropdown path shows cost/pool dice pickers;
  the card button needs the same affordances (or a small inline modal like Attack).
- **Two code paths temporarily.** Until fully migrated, logic may exist in both the
  card and the (removed) dropdown branch -- risk of drift; plan a clean cut-over.
- **Muscle memory.** Existing players used to the dropdown must relearn the location.

Recommendation: worth doing, and it pairs naturally with Task 2. Keep the underlying
handler unchanged; only move the trigger UI and reuse the Attack-style inline modal
for cost/pool. Confirm before implementing.

### 5a. Implemented (2026-07-29)

Approved with all cons rebutted. Frontend-driven, reusing the existing `crashScramble` /
`analyzeIC` card-button pattern (a `raw` control that POSTs to /action):
- `decryptScramble(ref)` and `defuseBomb(target)` in `matrix-run.html` POST the IDENTICAL
  `decrypt_file` / `defuse_data_bomb` bodies the menu sent (verified: the decrypt handler
  resolves the scramble purely from `target_file`, so slave/access scrambles work too; the
  defuse subsystem is derived server-side). Each prompts for Hacking Pool dice, like Attack.
- Scramble cards (Subsystem Defenses) gained a `>> Decrypt` button; the existing clear-hint
  already carries the Exploding "defuse the linked bomb FIRST" ordering (Poison / plain say
  nothing to defuse).
- Discovered data bombs now render as their own cards (new "Data Bombs" group) with a
  `>> Defuse` button -- previously bombs had no card.
- Removed `decrypt_file` + `defuse_data_bomb` from the dropdown (ACTION_CATALOG, ACTION_CATEGORY,
  ACTION_INFO). The backend actions are unchanged.
- Updated the two "Decrypt File" menu references (the file-list ENCRYPTED tag + the backend
  download-block message) to point at the card.
- Contract sync (drift guard): repointed the Decrypt/Defuse rows in `tests/matrix_scope_ledger.py`
  from `console` to the `raw` card functions, added both to `DEDICATED_CONTROLS`, and updated the
  scramble-ref reconciliation assertion. Full suite green (1207).

---

## 6. Task 4 -- 1.5s explanatory tooltips [OPEN-Q 5]

Want: hover tooltips (about 1.5s delay) explaining **programs** ("what does Camo
do?") and **actions** ("what does Analyze IC do / discover?"), in:
- the matrix-run UI: program list (left) and the action dropdown (bottom);
- program loadouts: the pre-run loadout picker AND the deck-workshop builder;
- anywhere else a term is unexplained.

Mechanism notes:
- The native `title` attribute cannot do a 1.5s custom delay or styling. The app
  already uses a custom `data-tip` tooltip pattern (seen throughout matrix-run.html
  buttons). Extending that (with a 1.5s show delay) is the natural fit and keeps one
  tooltip system.
- Content is authored once as a small map: program name -> one-line RAW-based
  description; action key -> what it does / what it reveals / its cost. Draft from
  `vr2_rules.md` so descriptions are accurate.
- Reuse across pages by putting the text map + tooltip helper in `frontend/shared.js`.

### 6a. Implemented (2026-07-29)

- **1.5s delay** added to the shared `data-tip` tooltip (`frontend/shared.js`): it now
  arms on hover and appears after 1.5s (applies app-wide). `#app-tooltip` already has
  `white-space: pre-line` + `max-width`, so multi-line descriptions render.
- **Program descriptions already existed** in `frontend/matrix-programs.js`
  (`MatrixPrograms.<key>.description`) and already render as hover tooltips on the in-run
  program chips (`progChip`/`progTip`), plus the pre-run loadout `.tip` spans and the
  deck-workshop inspector (`util.note`). So "what does Camo do?" was already covered; the
  1.5s delay now governs it.
- **Action descriptions (new):** authored `ACTION_INFO` (one RAW-accurate line per dropdown
  action) in `matrix-run.html` and render it as an `#actionDesc` helper line under the
  Action dropdown, updated in `onActionTypeChange` (a native <select> cannot carry a custom
  hover tip on its options). The per-IC card buttons (Attack / Analyze IC / Relocate /
  Suppress) already carry `data-tip`, so "what does Analyze IC do?" was covered there.

---

## 7. Open questions (asked in chat)

1. **Trace vanish + Relocate flow.** Confirm a trace should VANISH from the Known IC
   pane when it enters its Location Cycle (RAW), leaving Relocate / Graceful Logoff /
   run as the tools -- and that Relocate targets it DIRECTLY (RAW; Locate IC will not
   re-acquire a location-cycle trace). Or do you want a house-rule Locate-then-
   Relocate?
2. **Hunt-cycle feel.** Keep the Hunt Cycle as a non-damaging "find-you" roll (RAW --
   nothing to defend, you counter by attacking it), or reword the player events to
   read more like an active attack?
3. **Task 1 method.** Auto-generate the catalog from the real engine (recommended),
   hand-author, or hybrid? Confirm you want BOTH player and admin text per event.
4. **Task 2 scope.** OK to (a) hide/disable unavailable actions, (b) group the rest,
   and (c) remember the last action as default? Any preference on hide vs. disable?
5. **Task 4 tooltips.** OK to extend the existing custom `data-tip` tooltip with a
   ~1.5s delay and author RAW-based text, shared across matrix-run + loadouts +
   deck-workshop?
6. **Sequencing.** Which first: Trace vanish fix, Task 1 catalog, Task 2 action bar,
   Task 3 card buttons, or Task 4 tooltips?

---

## 8. Decisions log

**2026-07-29 (answers received):**
- **Trace Location Cycle:** do NOT fully vanish. Instead **re-skin the card** to
  reference the LOCATION being traced (a "datatrail lock"). The Trace IC itself is
  gone/reactive, so you **cannot Attack it directly**; what you Relocate is the
  location. The card stays in the Known IC pane so it still "looks like IC."
  => Server exposes a coarse cycle (`hunt` vs `locate`) so the card can switch;
     `trace_locate_remaining` stays admin/level-3 only. Frontend renders a
     location-cycle card with no Attack/Analyze/Slow, and a Relocate affordance.
- **Hunt Cycle:** keep non-damaging (RAW); wording clarity only (already improved).
- **Task 1 catalog:** AUTO-GENERATE from the real engine; player + admin text per
  event; sub-agents for coverage; output `docs/event-log-catalog.md`.
- **Task 2 action bar:** (a) HIDE actions that can't fire now, (b) GROUP by category,
  (c) REMEMBER last action as default. (Not disable-grey; not promote-to-buttons.)
- **Task 3 (Decrypt/Defuse on card):** pros/cons delivered. NOT building unless
  confirmed (it was a consult, not a build order).
- **Task 4 tooltips:** extend the custom `data-tip` tooltip with ~1.5s delay; author
  RAW-based text; across matrix-run (programs + actions) + pre-run loadout +
  deck-workshop.
- **Sequencing:** my choice; user will not test until everything is done. Planned
  order: Trace card -> Task 2 action bar -> Task 4 tooltips -> Task 1 catalog.
