# Reference data pulled from shadowrun2e.com

Raw JS data files pulled from the unofficial fan site shadowrun2e.com's SR2
character builder (`character-builder.html` and its scripts), for use as
source material when building this app's own character-builder gear/rules
data. Pulled 2026-08-11/12 -- see `docs/sr2-character-builder-plan.md` for the
full decision log (book-inclusion choices, cyberware grades, etc.) that came
out of reviewing this data.

Not yet wired into the app -- these are staging/reference inputs, not the
final `app/data/` catalog modules. Kept here (rather than only in a session
scratchpad) so implementation work isn't blocked on re-fetching from the site,
including on machines with limited/no internet access.

## Files

| File | Contents | Item count |
|---|---|---|
| `builder-data.js` | Priority table, metatypes, 15 totems, foci, matrix persona/program structure (reference only -- actual deck stats stay in Deck Workshop), full skill list w/ concentrations, languages, contact archetypes, archetype starter kits, chargen constants | -- |
| `builder.js` | The reference site's chargen wizard engine (steps, rendering, budget calculations) -- read as a design reference for our own wizard, not reused directly | -- |
| `weapons-data.js` | Weapons | 530 (SR2 91, SSC 58, FOF 38, BSW++ 343) |
| `armor-data.js` | Armor | 35 (SR2 13, SSC 15, FOF 7) |
| `cyberware-data.js` | Cyberware + bioware | 208 (SR2 61, SSC 43, Cybertechnology 77, Shadowtech 27) |
| `gear-data.js` | General gear, vehicles/drones, decks/programs | 212 (SR2 113, Rigger 2 40, VR2 35, RG++ 24) |
| `spells-data.js` | Spells | 219 (SR2 80, Grimoire 76, Awakenings 61) |
| `adept-powers-data.js` | Adept powers | 37 (SR2 9, Grimoire 6, Awakenings 22) |

++ `BSW` (Blackhand's Street Weapons 2057) and `RG` (Running Gear) are
fan-made, not official FASA books -- see the plan doc's "Fan Content" toggle
decision (off by default).

Every item in every file carries its own `src`/book code and page citation --
that's the field the per-campaign book-toggle system (plan doc S7) filters on.

**Superseded**: the `RIG2`-tagged vehicle subset in `gear-data.js` (20 items)
is a partial sample of the same table now fully captured in
`../rigger2-vehicles.json` (169 items, transcribed directly from the user's
physical Rigger 2 book, not from this site). Prefer that file for vehicles.
