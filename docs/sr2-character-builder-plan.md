# SR2 Character Builder ("Runner Dossier Intake") -- Plan

> Status: **Design in progress.** No implementation started against the real app yet.
> The builder now lives at `frontend/character-builder.html`
> (branch `SR2-char-builder`). All raw reference data pulled for this feature --
> shadowrun2e.com's catalogue/builder JS files and the full Rigger 2 vehicle
> table -- is committed under `docs/reference-data/`, so implementation work
> doesn't depend on re-fetching from the internet. This doc is the running
> decision log -- update it as choices get made instead of re-deriving them from
> chat scrollback.
>
> **2026-08-14**: `tools/check_text_hygiene.py` was corrected -- it's meant to
> catch mojibake (double-encoding corruption), not ban all non-ASCII text.
> Fixed to only flag genuine corruption markers/invalid UTF-8/BOM; legitimate
> Unicode (nuyen signs, accented names like "Tiburon", typographic punctuation)
> is allowed again. The reference-data files and this doc had been over-eagerly
> ASCII-flattened to pass the old stricter check; reference data was restored
> from pristine copies, and this doc's own prose is left as plain ASCII (cheap,
> low-value to restore -- it's internal documentation, not rendered game data).

## Implementation status

Real-app implementation is underway on branch `SR2-char-builder`:

- **Increment 1 (backend data-model foundation) -- done 2026-08-12.** Promoted the
  SR2 sheet onto real `Character` columns (six attributes, essence, body index,
  magic rating/type/tradition/totem, nuyen, karma pool + good karma, ordinal
  lifestyle level) with catalog-heavy chargen lists (priorities/skills/spells/
  adept_powers/gear) kept as JSON. Alembic migration `d7e4b2a9c150` + a
  `_ensure_character_sheet_columns` startup guard; existing PCs get defaults
  (two-tier, no backfill for now).
- **Increment 2 (catalog data + book toggle) -- done 2026-08-12.** The reference
  JS was converted to committed JSON under `app/data/catalog/` by
  `tools/build_catalog.py` (a build-time tool using `json5` to tolerate the JS
  literal syntax; the runtime loader uses stdlib `json`). Chose JSON + a small
  loader package (`app/data/catalog/__init__.py`) over hand-written `.py`
  literals given the ~1,240-item volume -- still "static data under `app/data/`"
  per S7, just not `.py`. Item counts: weapons 530, armor 35, cyberware 208,
  gear 212, spells **217** (the source file's header says 219 but only contains
  217 objects -- a source miscount, not a conversion loss), adept powers 37,
  vehicles 169. The 208-item cyberware pull is split into two catalogs by cost
  type: **cyberware** 186 (Essence cost) and **bioware** 22 (Body Index cost,
  `bio: true`). The per-campaign book toggle lives on
  `CampaignState.enabled_books` (migration `e2b7c4a91f30` + startup guard); SR2 is
  always implicit, `FAN` expands to `BSW`+`RG`, and `VR2` gear is intentionally
  never enable-able. Endpoints: `GET/PUT /catalog/books`, `GET /catalog/rules`,
  `GET /catalog/{name}` (book-filtered).
- **Increment 3 (frontend wizard + deck integration) -- done 2026-08-12.** The real,
  API-wired `frontend/character-builder.html` replaces the mockup: it loads
  `/catalog/rules` + the item catalogs, shops weapons/armor/cyberware/bioware/
  gear/vehicles + spells/adept-powers (book-filtered), and commits via a new
  `POST /characters/dossier` (player-owned or admin-unclaimed full sheet). Nav
  link injected via `shared.js`. **Cyberware grades** are in: Standard/Alpha
  selectable, Beta (career-only) and Delta (GM-only) gated, with the essence
  (ceil to 0.05) + nuyen multipliers and SSC/CYB book-gating; the admin-only
  `Character.delta_grade_approved` flag (migration `f3a8d0c21e64`) plus
  server-side rejection of Beta/Delta from players and a GM checkbox in
  `manage-characters.html`. **Deck integration (Option B)**: the wizard commits
  first, maps the Computer skill onto deck-eligibility, seeds the chargen deck
  budget + MPCP cap, then hands off to the Deck Workshop, which gained a small,
  self-contained **chargen mode** (URL-driven) that hard-enforces the MPCP cap
  (`floor(Computer x 1.5)`, max 8) and the nuyen budget without changing its
  normal behavior. Validated with Playwright DOM smokes
  (`tests/test_character_builder_dom.py`).
- **Unified nuyen pool + draft round-trip -- done 2026-08-12.** Superseded the
  Option-A deck carve-out with a fully-tracked single pool: the deck is built
  *before* the final commit so its actual spend folds back into the gear budget
  (reserve 200k, spend 150k, the 50k returns for gear; the 10:1 conversion of
  anything left runs only at Commit). The wizard persists a hidden **draft PC**
  (`Character.is_draft`, migration `a1c9e7b3f52d`, excluded from every character
  list) so the Deck Workshop can attach; the player builds against the live
  remaining budget; the actual spend is read back from
  `deck_builder_state.chargen.spent`; Commit **finalizes that same row** via
  `POST /characters/{id}/finalize-dossier` (drafts refresh mid-build via
  `.../dossier-draft`). Known gap: abandoned drafts orphan (players can't delete;
  localStorage reuse limits it to one per session), and the order-route deck spend
  is approximated by the build parts cost.
- **Chargen deck is buy-only -- done 2026-08-12.** At character creation the Deck
  Workshop's chargen mode hides the bench-build path entirely: you craft the deck
  spec and **buy** it at street price (the existing "Order from fixer" a-la-carte
  route), then buy programs with ratings/options. The running spend is recomputed
  from the actual purchases (each bought deck's `acq.priceFinal` + each bought
  program's `buyCost`), the budget gate projects the running total, and that spend
  is what folds back into the wizard's unified pool. A preset "off-the-shelf SR2
  deck" quick-pick list is a deliberate later add on top of this.
- **Stock-deck quick-pick -- done 2026-08-12.** The seven SR2 core stock decks
  (`docs/reference-data/sr2-cyberdecks-vr2.json`) are baked into
  `frontend/matrix-decks.js` and surfaced in the Deck Workshop's chargen mode as a
  "Quick-pick a stock deck" selector above the a-la-carte spec. Picking one is the
  "easy option": it fixes the whole spec at the model's stats and **buys it at the
  printed book price** (not the a-la-carte street price); the buyer's only choice is
  the persona split (MPCP x 3), from which I/O derives
  (`ceil(MPCP x Sensor x 5 / 10) x 10`). No Reality Filter, no other edits -- the
  rest of the spec is locked. The a-la-carte route stays for anyone building custom.

## TODO -- gear database

**Resolved 2026-08-12**: shadowrun2e.com's catalogue pages aren't just rendered
book text -- they're backed by structured, per-item, source-cited data files
(`weapons-data.js`, `armor-data.js`, `cyberware-data.js`, `gear-data.js`,
`spells-data.js`, `adept-powers-data.js`), same as `builder-data.js` was. Pulled
all of them into the scratchpad and inventoried them below. This is dramatically
more than the four books originally named -- every catalogue turned out to be
compiled from more sourcebooks than expected. Full breakdown:

| Catalogue | Items | Sourcebook codes present |
|---|---:|---|
| Weapons | 530 | `SR2` (91), `SSC` Street Samurai Catalog (58), `FOF` Fields of Fire (38), `BSW` Blackhand's Street Weapons 2057 -- **fan-made, not FASA** (343) |
| Armor | 35 | `SR2` (13), `SSC` (15), `FOF` (7) |
| Cyberware + bioware | 208 | `SR2` (61), `SSC` (43), `CYB` Cybertechnology (77), `SHADOW` Shadowtech (27) |
| Gear (incl. vehicles/drones/decks/programs) | 212 | `SR2` (113), `RIG2` Rigger 2, FASA7906 (40), `VR2` Virtual Realities 2.0 (35), `RG` Running Gear -- **fan-made** (24) |
| Spells | 219 | `SR2` (80), `GRIM` Grimoire 2nd Ed (76), `AWK` Awakenings (61) |
| Adept Powers | 37 | `SR2` (9), `GRIM` (6), `AWK` (22) |

Every item already carries its `src` (book) code and page number -- this is exactly
the field the per-campaign book-toggle needs (S7).

- [x] ~~Full skill list~~ -- already fully covered by `builder-data.js`'s
      `SR2_SKILLS` (the complete ~34-skill list w/ concentrations), pulled in an
      earlier session. The mockup's ~26-skill sample was just a mockup trim, not a
      real gap -- no additional sourcing needed here.
- [x] ~~Cyberware / bioware~~ -- pulled (`cyberware-data.js`, 208 items, SR2 +
      SSC + Cybertechnology + Shadowtech). Also resolved the Essence-vs-Body-Index
      question -- see S3.
- [x] ~~Weapons / armor / general gear~~ -- pulled (SR2 + SSC + Fields of Fire +
      the two fan works above).
- [x] ~~Vehicles / rigger gear naming mismatch~~ -- resolved, then simplified
      further: originally both Rigger 2 and the actual Rigger Black Book were
      going to get separate book slots, but once the full Rigger 2 vehicle table
      was transcribed (below) it turned out to already cover every vehicle
      needed -- **the Rigger Black Book slot was dropped entirely, not just left
      empty.** See S7.
- [x] ~~Rigger 2 master vehicle list~~ -- **done 2026-08-13.** User supplied the
      Rigger 2 sourcebook PDF (`vdoc.pub_rigger-2-a-shadowrun-sourcebook.pdf`,
      scanned/no text layer -- rendered to page images with PyMuPDF, cross-checked
      with Tesseract OCR, both installed ad hoc for this task). Transcribed the
      complete "Vehicle List" appendix (pp.148-166): **169 catalog entries** (135
      vehicles + 34 drones, each trim/variant as its own row) covering every
      vehicle in the book, A-Z. Saved as `rigger2_vehicles.json` in the scratchpad
      -- not yet moved into `app/data/`.

      Critically, **every entry carries the book's own `Reference:` field**
      (which book the vehicle *originally* debuted in -- R2/RBB1/SRII/CS/FF/
      NAGRL/LS/Aztlan), confirming Rigger 2 is a compiled, ruleset-unified
      restatement of vehicles from across the whole SR2 line, not just its own
      original content. Breakdown by reference: RBB1 81, SRII 31, R2 21, FF 9,
      Aztlan 6, NAGRL 6, LS 6, SRII+RBB1 (dual-sourced) 4.

      **This settles the Option A vs. Option B redesign-vs-conversion question
      from earlier** (S below, dated 2026-08-11/12): comparing the same vehicle
      across books (Eurocar Westwind 2000, Mitsubishi Runabout, Volkswagen
      Elektro) showed Rigger 2 **redesigns each vehicle from its own Point Value
      / chassis-template system** (p.147/170 of the book) rather than converting
      old stats by formula -- cost and a couple of flavor stats often carry over,
      but core performance stats (Handling, Body, etc.) are frequently
      re-balanced. Conclusion: **use this table as the authoritative, single-
      ruleset vehicle catalog going forward** -- it supersedes the smaller partial
      `RIG2`-tagged subset (20 items) already sitting in `gear-data.js`, which was
      evidently just an incomplete sample of this same table. No manual RBB-to-R2
      conversion formula is needed for any vehicle that appears in this table.

      **Data quality**: every entry spot-checked by the user against 12 flagged
      unusual/hard-to-read rows (paired stats, parenthetical alt-values, tiny
      micro-walker drones) -- all 12 confirmed correct, two got clarifying notes
      folded in (Aguilar-EX's parenthetical = short-term electric drive mode;
      Microskimmer II's split Sig = normal/underwater, per the user's inference).
      Also caught and fixed a modeling error: blank stat cells were initially
      encoded as JSON `null`, conflating "book prints em-dash (not applicable)"
      with "genuinely unread" -- fixed to preserve the book's own `"--"` notation
      instead, once it became clear virtually every flagged case was Pilot-on-
      manned-vehicles or Autonav-on-drones (i.e., a real "--" in print, not a gap).

      **Decided 2026-08-13: Rigger Black Book is not needed at all.** Since this
      table already covers every vehicle, transcribing RBB separately would be
      pure duplicate effort -- dropped from the book list entirely (not left as
      an empty slot). `frontend/vehicle-data-entry.html` (the manual entry tool
      built for that transcription work) has been deleted, its job done. File
      lives at `docs/reference-data/rigger2-vehicles.json` now, alongside the
      shadowrun2e.com pulls, rather than in the session scratchpad.
- [x] ~~Cyberware grades~~ -- **resolved 2026-08-12, confirmed against the user's
      physical books** (not Shadowtech, which doesn't have it -- Alpha/Beta are in
      **Street Samurai Catalog**, Delta is in **Cybertechnology**; both already on
      the finalized book list in S7, so no new sourcebook is needed). Confirmed
      table:

      | Grade | Essence multiplier | Nuyen multiplier | Source |
      |---|---|---|---|
      | Standard | 1.0x | 1x | -- |
      | Alphaware | 0.8x (-20%) | 2x | SSC |
      | Betaware | 0.6x (-40%) | 7x | SSC |
      | Deltaware | 0.5x (-50%) | 10x | CYB |

      Note the Betaware nuyen multiplier is **7x** per the actual SSC text -- a web
      search during the investigation phase had surfaced 4x as "the SR3 number,"
      but that's third-hand fan-wiki trivia about a different, out-of-scope
      sourcebook (possibly *Man & Machine: Cyberware*), not this project's actual
      source. SSC's printed 7x is authoritative here; the 4x figure should be
      disregarded for this app.

      **Essence rounding rule**: essence floor of 0.05; round up (not to nearest)
      when applying a grade multiplier, to 2 decimal places.

      **Explicitly out of scope**: SSC also has per-grade damage-resistance
      ratings -- the user's call is not to model that in the character builder.

      **Data-model implication**: grade is a *purchase-time modifier* applied to
      any cyberware line item, not per-item catalog data -- so it isn't a new
      `book` tag on individual entries. Once the SSC toggle is on, Alpha/Beta
      become available as a grade choice on any cyberware purchase; once CYB is
      on, Delta becomes available too. The grade multiplier table itself lives
      once, applied generically, rather than being baked into every catalogue
      item's stats.

      **Chargen availability by grade -- resolved 2026-08-12**: manufacturing and
      access differ sharply by grade (per the user's books) and that gates when
      each grade is actually choosable, independent of whether its book is toggled
      on:
        - **Standard & Alphaware**: mass-produced, available at most shadow
          clinics. **Selectable in the chargen wizard's Asset Manifest step.**
        - **Betaware**: usually custom-made; obtainable in play at most shadow
          clinics, but **not offered as a chargen option**. It becomes available
          through career-play nuyen spending after the dossier is committed -- the
          same "manage nuyen through the app on an ongoing basis" territory
          already flagged for Lifestyle upkeep and Deck Workshop Option B (S3, S5).
          Whatever ends up handling ongoing post-chargen nuyen spend is where
          Betaware purchases belong, not the wizard itself.
        - **Deltaware**: always custom-made, corp-clinic-only, and narratively
          gated -- "the corp has to want the character there." **Not a normal
          purchase option anywhere**, chargen or otherwise; no price-driven shop
          entry makes sense for it. This is a GM-granted/GM-authorized action --
          likely belongs alongside the admin-only editing capability
          `manage-characters.html` already has (S3's "NPC creation stays
          separate" note), not the player-facing economy.
- [x] ~~Book-inclusion decisions~~ -- resolved, see S7 for the finalized book list.
- [x] ~~Rigger Black Book transcription~~ -- **dropped, not needed 2026-08-13.**
      This item went through a full arc worth remembering the shape of, in case a
      similar dual-book situation comes up again: (1) originally scoped as
      additive to Rigger 2's partial 20-item subset; (2) a fidelity policy was
      set to preserve RBB's native units (meters/Combat Turn, no Accel/Load/
      Avail/Index) rather than convert them; (3) that policy was reversed the
      same day once the user clarified the real goal was one consistent,
      comparable shop-list ruleset, not fidelity to two incompatible unit
      systems; (4) attempting to empirically derive an RBB->R2 conversion formula
      from a single shared vehicle became moot once the *complete* Rigger 2
      vehicle table was transcribed directly from the book and turned out to
      already cover every vehicle needed. Net result: no RBB transcription, no
      conversion formula, no second book slot -- see the Rigger 2 entry above.
- [ ] **Supplemental rules text** (`rigging-mechanics.html`, `combat-mechanics.html`)
      -- these are procedural rules (vehicle mods, called shots, etc.), not catalog
      items, so they don't feed the same book-toggle pipeline. Still worth a pass
      for citations once the catalogue shape is locked in.

## 1. What this is

An in-universe reframing of shadowrun2e.com's SR2 priority-based character builder:
players fill out a **case dossier**, not "build an RPG character." Steps are
relabeled accordingly (see S4). Reference implementation reverse-engineered from
`builder.js` / `builder-data.js` on shadowrun2e.com -- a 7-step wizard (Priorities,
Metatype, Attributes, Magic, Skills, Resources, Finish & Export) with a live budget
sidebar, archetype quick-start kits, searchable shop pickers, and PDF export.

## 2. Decisions confirmed so far

| Decision | Detail |
|---|---|
| Framing | "Runner Dossier Intake" -- matches the app's existing "New Dossier" language in `manage-characters.html`. |
| Wizard chrome | Reuse `matrix-designer.html`'s `.md3` 3-pane layout (sticky left step rail / center step pane / right budget-meter sidebar) rather than inventing new chrome. |
| Gear sourcing | Player-provided data from **SR2 core, Shadowtech, Street Samurai Catalog, Cybertechnology, Grimoire, Awakenings, Rigger 2** -- cyberware, bioware, vehicles, weapons, armor, gear, spells, adept powers. Rigger Black Book turned out unnecessary once the full Rigger 2 vehicle table was in hand -- see the TODO section. Hand-off format: plain text/tables, or a PDF for a Claude session to transcribe directly, shaped into data files matching the reference site's `weapons-data.js` / `armor-data.js` / `cyberware-data.js`. |
| Cyberdecks & programs | **Not bought during chargen** in the baseline plan -- deferred to the existing Deck Workshop tool, post-commit. See S5 for the live-budget alternative under consideration. |
| Aspected Magician / Mystic Adept | **Excluded** -- not in SR2 core, so not in this app. |
| Qualities / Edges / Flaws | **Excluded** -- not in SR2 core. |
| Starting Karma Pool / Good Karma | Per RAW: Karma Pool 1, Good Karma 0 at chargen. |
| Unspent Resources -> cash | Confirmed: convert at **10:1** per SR2 p.46. |
| Totems | Full 15-totem list to be supplied by the user (mockup samples 6). |
| Data model direction | **Promote core sheet fields to real `Character` columns** -- all 6 attributes (today only Body/Quickness/Intelligence/Willpower exist), Essence, Nuyen, Karma -- rather than leaving them buried in a JSON blob. Reasoning: other tools (initiative tracker, matrix run) will want to query these directly. Catalog-heavy, list-shaped data (full gear/spell/power lists) stays JSON. This **supersedes** the `MATRIX VITAL STATISTICS` block in `manage-characters.html`'s admin form for any character built through the wizard -- that block only covers a strict subset of the full sheet. |

## 3. Still open -- needs your call before/while building

- **Existing PCs migration**: characters already created via the old lightweight
  admin form will be thinner than wizard-built ones. Backfill them manually, re-run
  them through the wizard, or accept a two-tier population indefinitely?
- **NPC creation stays separate**: the admin form in `manage-characters.html` can't
  go away -- GMs hand-enter NPCs that never go through a PC priority wizard. Wizard
  becomes a *second* creation path feeding the same `characters` table, not a
  replacement. Worth confirming this split is fine as-is.
- **Bioware essence mechanics -- resolved 2026-08-12**: `cyberware-data.js`'s header
  answers this directly (cited to Shadowtech pp.6-7): bioware uses a separate
  **Body Index** (cap = natural Body Rating), not Essence, and normally costs no
  Essence at all. Magicians/adepts only check for Magic loss after "drastic
  invasive surgery" (total Body Cost over 1.5) or any neural bioware. **Sheet needs
  a second resource track** (Body Index alongside Essence) -- flagged for the data
  model.
- **Foci**: dropped from the mockup entirely (nuyen + Force-Point bonding cost,
  SR2 p.137). Reference tool has them; needs to go back in for magician/adept builds.
- **Native language rule**: also dropped from the mockup. SR2 p.45/74: native
  language free at Intelligence + 2; Street lifestyle adds a free local dialect at
  half Intelligence. Needs porting in.
- **Concentration/Specialization mechanical effect**: mockup only records a free-text
  Concentration. SR2 p.70's actual tiering (general skill -1/-2, concentration +1,
  specialization +2) affects dice pools elsewhere in the app (combat, tests) -- decide
  whether the builder needs to compute this or just record it as reference text.
- **Lifestyle payment -- resolved 2026-08-11, needs design**: confirmed Lifestyle
  does cost nuyen, and it shouldn't be a one-time chargen deduction -- the user wants
  it tracked as ongoing upkeep, auto-charged off the campaign clock. This app
  already has exactly that pattern: `app/models/campaign.py`'s `CampaignState`
  (1 tick = 1 day, advanced only by the Downtime control) is the single source of
  truth for time, and heat / public-awareness / org-standing decay are all computed
  *lazily* from ticks elapsed since a last-stamped value -- no cron job, just
  recomputed on read. Lifestyle upkeep should follow the same shape: stash a
  `lifestyle_paid_through_tick` (or equivalent) alongside the lifestyle tier on the
  character, and lazily deduct `monthly_cost x elapsed_months` from a nuyen balance
  whenever it's read or whenever Downtime advances the clock.
  **This implies nuyen becomes a genuine persistent, spendable balance on
  `Character`** -- not just a chargen-time budget that's forgotten after intake --
  which is a bigger scope decision than the character builder alone (it's the first
  piece of "manage nuyen through the app on an ongoing basis," which the user is
  actively considering per the Deck Workshop discussion in S5). Treat as a related
  but separate follow-on initiative: chargen just needs to set the *initial*
  lifestyle tier + starting nuyen balance correctly; the ongoing tick-deduction
  engine is its own piece of work, probably shared with wherever else nuyen gets
  spent post-chargen (Deck Workshop Option B, if that's the direction taken).
- **Rigger chargen specifics**: VCR essence-by-level, jumped-in bonuses -- currently
  vehicles are just generic gear-shop items in the mockup. Likely needs its own
  mini-section now that the full Rigger 2 vehicle catalog (169 entries,
  `docs/reference-data/rigger2-vehicles.json`) is available to shop from.
- **Cyberware grades** (Standard/Alpha/Beta/Delta): flagged earlier, still unconfirmed
  whether your campaign uses them (Shadowtech territory).

## 4. Wizard steps (current mapping)

| # | In-universe label | Reference-tool step | Notes |
|---|---|---|---|
| 1 | Case Priorities | Priorities | Priority letter grid A-E + archetype "standard dossier template" kits. |
| 2 | Subject Classification | Metatype | Only unlocked past Human if Race priority = A. |
| 3 | Physiological Baseline | Attributes | Point-buy + racial mods/caps. |
| 4 | Arcane Profile | Magic | Full Mage / Adept / Mundane gated by Magic priority + race; tradition/totem for shamans. |
| 5 | Trained Capabilities | Skills | Skill point-buy; needs native-language rule + concentration/specialization added back (S3). |
| 6 | Asset Manifest | Resources | Weapons/armor/cyber/gear shopping + contacts. Deck handling is the open question in S5. |
| 7 | Case File Summary | Finish & Export | Identity fields, derived-stat summary, 10:1 starting-cash conversion, commit action. |

## 5. Deck Builder integration -- two options on the table

**Option A -- Reserve & defer (current mockup behavior).** Chargen doesn't touch deck
stats at all. Asset Manifest gets a "Deck Build Reserve" nuyen field; that amount is
excluded from gear spending *and* from the 10:1 conversion, and carries over 1:1 as
the Deck Workshop's starting budget once the dossier is committed. Simple, but it's a
**house-rule carve-out** -- RAW's 10:1 conversion assumes the deck is bought at
intake, so this deliberately avoids penalizing a decker for deferring the purchase.

**Option B -- Embed Deck Workshop live in chargen (raised 2026-08-11, not yet built
even in the mockup).** Launch the real Deck Workshop from inside the Asset Manifest
step, spending directly against the same Resources nuyen budget as everything else.
Whatever's left over still converts 10:1, RAW-clean -- no house rule needed. Requires:

- **Shared, hard nuyen cap.** Deck Workshop would need a "budget mode": told the
  remaining chargen nuyen, refusing purchases that would exceed it, and reporting
  final spend back to the wizard's budget meter live. Today's Deck Workshop is a
  free-form tool with no evidence of an enforced spending ceiling -- this would be
  new capability there, not just in the character builder.
- **Chargen-only rating ceiling.** SR2 RAW has no MPCP/rating cap at chargen beyond
  nuyen and Availability/Street Index (which this app's Resources step already
  ignores at chargen per its own copy). Letting nuyen alone gate deck rating means a
  Resources-A decker could plausibly start with a near-top-end deck -- almost
  certainly not what you want for a starting character. This needs an explicit house
  cap (e.g., mirror the chargen skill-rating cap of 6 for MPCP, or pick a flat
  number) -- flagging as a number **you** need to set, not something derivable from
  the book.
- **Sequencing problem**: Deck Workshop's existing state (`deck_builder_state`) is
  keyed to a real, already-persisted `Character.id`. During chargen the character
  doesn't exist as a saved row yet -- it's still an in-progress draft. Two ways
  through: (a) persist a draft `Character` row early (before the Finish step) so
  Deck Workshop has a real id to attach to, finalizing/patching it at commit; or
  (b) teach Deck Workshop to operate against an ephemeral, non-persisted budget
  context instead of always requiring a character id. (a) is the smaller change but
  means "character creation" starts writing to the DB before the dossier is
  actually committed -- worth being deliberate about that instead of backing into it.
- Programs have no fixed SR2 price (object code, GM-set) -- the shared-budget cap
  needs to work against editable/typed-in costs, not just catalog lookups.

**Deck build-vs-buy, checked 2026-08-14**: the reference tool's chargen only
supports *buying* a stock deck -- a flat dropdown over 8 SR2-core off-the-shelf
models (Radio Shack PCD-100 through Fairlight Excalibur, fixed MSRP, p.173).
The real per-attribute deck-construction formulas (MPCP/persona
ratings/memory/Response Increase/Hardening, each individually costed, SR2
p.172-173) exist in `SR2_MATRIX` but are **dead data** -- defined, cited, and
never referenced anywhere in `builder.js`. The one non-SR2-core catalog entry,
"SuzyQ's Cyberdeck" (VR2, 732,238Y), isn't a real stock model at all -- its own
description calls it "the book's worked construction example," i.e. VR2's
demonstration of what the build formulas produce, sitting in the gear dropdown
as if purchasable. For reference, a same-MPCP comparison: Fuchi Cyber-6
(MPCP 8, stock, 334,500Y) vs. SuzyQ's (MPCP 8, custom-built, 732,238Y before a
10% complete-build discount) -- roughly 2x cost for a fully persona-loaded
build vs. bare stock hardware. If Deck Workshop (wherever real deck purchases
end up living, per Option A above) wants an actual build-your-own-deck mode
rather than just a stock catalog, the formulas are ready to use -- they'd just
be new functionality, not a port of anything the reference tool actually does.
**Recommendation**: don't decide yet -- Option B is real feature work on Deck Workshop
itself (budget mode + rating ceiling + the persistence-sequencing question), not
something to bolt on inside the character-builder mockup. Worth scoping as its own
follow-up once the rest of chargen is real, rather than blocking on it now. Option A
ships sooner and is fully reversible (nothing stops a later migration to Option B).

**Stock SR2-core decks adapted for this app's rules -- resolved 2026-08-14.**
Confirmed via the actual matrix engine code (`app/services/matrix_engine.py`,
`app/routers/matrix_runs.py`, `frontend/deck-workshop.html`), not assumption:

- MPCP, Hardening, Active Memory, and Storage from the book plug straight in --
  no conflict with anything the engine already does.
- **Persona ratings are assigned by the buyer at purchase time**, not printed on
  the deck -- a pool of MPCP x 3 points split across Bod/Evasion/Masking/Sensor.
  This isn't a new feature; the app's `DeckerStats` schema already requires all
  four individually, capped exactly this way (SR2 p.174).
- **Load is dropped entirely** -- no representation anywhere in `app/`; the
  engine already gates capacity via Active Memory + per-program Mp cost, which
  covers the same ground. Not worth new plumbing for a redundant second stat.
- **I/O is dropped from the book's printed value and replaced with a house
  rule**, since the book's small I/O rating and the app's `io_speed` (Mp per
  Combat Turn, matching VR2's own scale -- SuzyQ's is 480, not a small number)
  are simply different scales with no derivable conversion. The app already
  hard-caps `io_speed <= MPCP x Sensor x 10` (`matrix_runs.py:6485`). Decided:
  stock decks ship at **half that ceiling** (`MPCP x Sensor x 5`), leaving
  headroom for upgrades. Consequence: I/O isn't a fixed per-deck stat anymore --
  it's computed once the buyer's Sensor rating is known.
  **Rounding confirmed 2026-08-15**: `MPCP x Sensor x 5` isn't always a
  multiple of 10 (the app's other `io_speed` requirement) -- only when
  `MPCP x Sensor` is even. When it's odd, **round up** to the nearest 10
  (e.g. MPCP 3 + Sensor 3 -> raw 45 -> stock I/O 50).
- **Deck upgrades post-purchase are already a real, built feature** -- not
  something to design from scratch. `deck-workshop.html` already has both a
  skill-based self-build path (`computeProgrammerCaps()`, max designable MPCP =
  highest of Computer/Software/Matrix Programming skill x 1.5, cited `// vr2
  "MPCP"`) and a sourced/paid upgrade path (`_deckPurchaseTriggers`,
  `validateSourceUpgrade()`, gating certain persona-chip upgrades behind
  needing source code). Chargen just needs to set the starting deck; upgrading
  it later is already handled.
- SuzyQ's Cyberdeck (VR2, the fully-loaded custom-build example) is **not**
  adapted alongside the stock decks -- it's already VR2-native and stays as-is
  in `gear-data.js`.

Full adapted stock-deck catalog (7 decks, all fields above applied, with the
reasoning repeated inline as `_meta`) is in
`docs/reference-data/sr2-cyberdecks-vr2.json`.

## 6. Reference data already captured (from shadowrun2e.com's `builder-data.js`)

Priority table, metatype mods/maxes/vision, 15 totems w/ geasa, foci costs (nuyen +
Force-Point bonding), matrix persona/program structure (kept for reference only --
see S5, actual deck stats stay in Deck Workshop), skill list w/ concentrations,
archetype quick-start kits. Plus the full catalogue pull in the TODO section above
(weapons/armor/cyberware+bioware/gear/spells/adept powers, ~1,241 items total),
plus the complete Rigger 2 vehicle table (169 entries, transcribed directly from
the book -- not shadowrun2e.com). All of it committed under `docs/reference-data/`.

## 7. Book-toggle design (per-campaign sourcebook selection)

The user wants **SR2 core always on**, with everything else (Fields of Fire,
Street Samurai Catalog, Shadowtech, etc.) individually enable-able -- so a GM can
keep a leaner or more expansive item pool per campaign. The pulled data already
carries exactly the field this needs: every item has a `src` book code and page
number (see the TODO table for the full code list).

Proposed shape (not yet built):
- **Storage**: static Python data modules under `app/data/` (one per catalogue --
  `weapons_catalog.py`, `armor_catalog.py`, etc. -- or one combined module),
  mirroring the existing `app/data/consequence_tags.py` precedent rather than
  going through the `seed.py`/API JSON route (that path is for world-state
  entities like orgs/locations, not static reference data). Each item keeps its
  `src` code and page cite.
- **Enabled-books setting**: likely a small addition to `CampaignState` (already
  the single-row source of truth for campaign-wide settings, per S3's lifestyle
  note) -- a set/list of enabled book codes, `SR2` always implicitly included and
  not togglable off.
- **Filtering**: the character builder's shop pickers (and any other UI that
  lists gear) filter every catalogue query by `src in enabled_books`. One filter,
  reused everywhere, rather than each picker re-implementing it.

**Book-inclusion decisions -- resolved 2026-08-12:**

1. **Fan-made content (`BSW`, `RG`)**: gets its own **separate "Fan Content" toggle**,
   distinct from the official-book list, **default OFF**. Not treated as a regular
   book, so a GM turning on official expansions never silently pulls in
   non-canon material.
2. **Rigger books -- down to one slot, resolved 2026-08-13**: `RIG2` (Rigger 2,
   FASA7906) is the only rigger-book toggle. Originally a second `RBB` slot was
   planned for the actual 1st-edition Rigger Black Book, but once the *complete*
   Rigger 2 "Vehicle List" appendix was transcribed from the book (169 entries,
   `docs/reference-data/rigger2-vehicles.json` -- supersedes the smaller partial
   `RIG2` subset in `gear-data.js`), it covered every vehicle needed. RBB adds
   nothing on top and was dropped rather than left as an always-empty slot.
3. **Cybertechnology, Grimoire 2nd Ed, Awakenings**: included as regular toggles --
   data's already pulled and cited.
4. **Virtual Realities 2.0 -- excluded from the character builder's book list.**
   Checked what the 35 `VR2`-tagged `gear-data.js` entries actually are: one
   cyberdeck (`SuzyQ's Cyberdeck`) and 34 Matrix programs -- nothing else.
   That's 100% Deck Workshop territory, which is already out of scope for chargen
   (S2/S5), and the live app's matrix programs are already sourced separately via
   `frontend/matrix-programs.js`, not this pull. There is currently nothing in the
   `VR2` tag relevant to the character builder's own Asset Manifest catalogue, so
   it's dropped rather than added as an always-empty toggle. Revisit only if a
   future VR2 pull turns up non-deck/program content.

**Finalized book list for the character builder** (SR2 always on):
`SSC` (Street Samurai Catalog) - `FOF` (Fields of Fire) - `SHADOW` (Shadowtech) -
`CYB` (Cybertechnology) - `GRIM` (Grimoire 2nd Ed) - `AWK` (Awakenings) -
`RIG2` (Rigger 2) - plus a separate `FAN` toggle covering `BSW` + `RG`, default
off. No Rigger Black Book slot -- see point 2 above.
