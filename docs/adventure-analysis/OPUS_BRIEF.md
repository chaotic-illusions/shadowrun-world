# Brief: Adventure Structure Deep-Dive (hand-off for an Opus session)

## Goal

Produce a writer's guide to how the 52 published Shadowrun adventures in this campaign are built, so the
campaign owner can write original adventures using the published material as a structural model. The
deliverable is not another summary of each plot. It is an analysis of STRUCTURE: how the books open, how
they are divided into acts and scenes, what beats recur, how many people and places each needs, how
opposition escalates, how twists are seeded, how they end and pay out. The final product must let someone
sit down with a blank page and a checklist and draft a Shadowrun adventure that feels like one of these.

Everything the analysis needs is already in this repository. Do not re-ingest the PDFs.

## Inputs (all in the repo)

1. `docs/adventure-prep/NN-<slug>.md` -- one prep document per adventure (52 files, numbered in campaign
   order). Each has: SYNOPSIS, TIMELINE (bulleted beats), the created NPC / location / org rows with
   their descriptions and notes, MATRIX_HOSTS, NOT_BUILT, PLAY_NOTES. These are the primary source for
   the analysis and are usually sufficient on their own.
2. `scripts/adventure_ingest/specs/<slug>.py` -- the same content as structured Python (NPCS,
   LOCATIONS, ORGS lists and *_UPDATES dicts). Useful for counting and for scripted extraction.
3. `docs/Adventures/text/*.txt` -- the OCR'd full text of every book (gitignored, present on the owner's
   machine only). Consult only when a prep doc is silent on something structural: the book's own act and
   scene headings, GM-advice sidebars, "Picking up the pieces" / awards sections, the "Cast of shadows"
   ordering, handouts. Read in chunks (the files are 100 KB to 1 MB); never read a whole book into context.
4. `docs/adventure-analysis/baseline-counts.md` -- an auto-generated table of rows created per adventure
   plus timeline-beat counts. Use it as the quantitative starting point; do not recompute it by hand.
5. `frontend/shared.js` ADVENTURE_ORDER -- the canonical campaign order and titles.

Corpus notes that affect the analysis:
- Editions: #1-#12 and #15, #25 are SR1 (FASA 1989-1992); #13-#31 are SR2; #32-#38 are SR3 (FASA / FanPro);
  #39-#52 are Shadowrun Missions (SRM) Season 0 and Season 1, SR3, all Seattle 2064, written to a
  4-hour convention slot with a fixed scene format. Treat SRM as its own structural family.
- Anthologies rather than single adventures: #29 Missions (four short runs), #31 Blood in the Boardroom
  (a corporate-war sourcebook with adventure seeds, not a scripted adventure), #24 Harlequin's Back
  (a linked series of metaplanar quests). #9 Harlequin is a campaign of eight linked runs.
  #32 Renraku Arcology: Shutdown and #38 System Failure are event sourcebooks with embedded adventure
  hooks. Analyse each of these as what it is, and say so in its card.
- Earlier books are canon in this campaign; the analysis is descriptive, not a canon ruling.

## Deliverables

Write three files into `docs/adventure-analysis/`:

### A. `cards/NN-<slug>.md` -- one structure card per adventure (52 files)

Fixed field list; keep each card to roughly one to two pages. Use "n/a" rather than omitting a field.

```
# NN. <Title> (<edition>, <publisher>, <year published>, in-world <YEAR>)

**Type:** scripted adventure | linked campaign | anthology | event sourcebook | convention mission
**Length:** page count of the adventure proper (exclude appendices), estimated sessions to play
**Premise (one sentence):**
**Hook / Johnson:** who hires the runners, how the meet is staged, what is offered, what is concealed
**The real job vs the stated job:** the twist, if any, and on which page/beat it is revealed to players
**Structure:** number of acts/chapters/scenes as the BOOK divides them (name them); linear, branching,
  or hub-and-spoke; whether scenes are timed (SRM) or free-form
**Beat list:** numbered, one line each, in play order -- opening, legwork, complications, set-pieces,
  climax, resolution. Mark each beat with tags: [meet] [legwork] [infiltration] [combat] [social]
  [chase] [matrix] [astral] [betrayal] [moral-choice] [reveal] [climax] [aftermath]
**Opposition ladder:** the antagonist forces in order of escalation (street gang -> corp security ->
  named heavy -> big bad), and whether the big bad is fought, negotiated with, or escaped
**Cast size:** NPCs with speaking roles / NPCs with stat blocks / named-only (from baseline-counts plus
  the prep doc); the 3-5 NPCs the plot cannot run without and their functions (Johnson, target,
  betrayer, ally, wildcard)
**Locations:** count and the 3-5 set-piece locations with a phrase on what the scene there does
**Factions:** orgs in play and which side each is on
**Information economy:** what the players must learn, from whom, and the intended legwork paths
  (contacts, matrix, astral, street); what is deliberately hidden until the climax
**Failure handling:** what the book says happens if the runners fail, refuse, or go off-script;
  sidebars titled "If the runners...", "Debugging", "Picking up the pieces"
**Payout and karma:** stated nuyen, karma awards, and what non-cash rewards (contacts, rep, enemies)
**Themes and tone:** 2-4 short phrases (e.g. corporate betrayal, body horror, elven politics, noir)
**Recurring devices used:** from the device list in C (fill in as the list grows)
**Reusable template value:** one paragraph on what a homebrew writer should steal from this book
**Discrepancies / editing notes:** anything the prep doc flagged about the book's own inconsistencies
```

### B. `SYNTHESIS.md` -- the cross-corpus analysis

Sections, in this order:
1. **Corpus overview** -- table by edition/family: count, median page length, median acts, median cast,
   median locations, typical payout, typical session count. Draw on baseline-counts.md.
2. **The standard skeleton** -- the act structure the majority of scripted adventures share, described
   as a numbered sequence of beats with the percentage of adventures that use each beat. Name the
   variants (e.g. the "double Johnson" opening, the "midpoint betrayal", the "hostage climax") and cite
   the adventures that exemplify each by number.
3. **Structural families** -- cluster the 52 into families (e.g. extraction, investigation/mystery,
   protection/bodyguard, heist/data-steal, wilderness/travel, political, metaplanar/magical, convention
   mission, campaign/anthology). For each family: defining beats, typical act count, typical cast and
   location count, best exemplar, weakest exemplar and why.
4. **Recurring devices** -- a catalogue of 20-40 named devices with a one-line definition and the
   adventures that use each: the Johnson who lies, the target who wants to be extracted, the double-cross
   at the handoff, the ticking clock, the moral choice with no clean answer, the dragon behind the
   curtain, the innocent bystander, the map handout, the news-feed handout, the tailing scene, the
   Matrix run as parallel track, the astral clue, the mid-run second job offer, the "runners are the
   patsies" reveal, the Lone Star response timer, the chase, the safehouse raid, the finale at a public
   event, etc. Derive from the cards; do not invent devices no book uses.
5. **Cast and place patterns** -- what roles a cast always contains (Johnson, fixer, target, rival team,
   local colour, heavy, big bad), how many of each, how NPCs are introduced and reused; how many
   locations a run needs and what kinds (meet, legwork stop, set-piece, safehouse, climax); how the
   books stage security levels.
6. **Information and legwork design** -- how the books ration clues across contact, Matrix, astral and
   street channels; how they handle player failure to find a clue; how much is written for the GM vs
   handed to players.
7. **Escalation and climax design** -- how threat ramps across acts; the ratio of combat to social to
   stealth climaxes; how books make the final scene decisive without railroading.
8. **Payout, karma and consequences** -- ranges by era; what the books consistently reward and punish;
   how aftermath sections seed sequels.
9. **What changed across editions** -- SR1 vs SR2 vs SR3 vs SRM: page economy, scene formatting,
   handouts, GM advice, tone.
10. **Common weaknesses** -- structural problems that recur (railroads, unearned betrayals, single-path
    legwork, unwinnable climaxes) so a homebrew writer can avoid them.

### C. `TEMPLATE.md` -- the writer's template

A fill-in document for drafting an original adventure in the published style, derived entirely from A
and B. Contents:
- A one-page **skeleton** with the standard beats as headed blanks, each with a one-line prompt and the
  typical page budget.
- A **planning checklist** (hook, twist, three legwork paths, opposition ladder, three set-pieces,
  failure branches, payout, aftermath hooks) with target counts (cast, locations, orgs) taken from the
  medians, and the range to stay within.
- **Family variants**: for each structural family in B.3, the beats to add or swap.
- A **device menu**: the B.4 catalogue as a pick-list with a note on when each works.
- **Worked example**: one published adventure re-expressed in the template, chosen because it is the
  cleanest exemplar of the standard skeleton (state which and why).
- **Two-page SRM variant** for writing a timed 4-hour convention-style mission.

## Method

Work in three passes and write files as you go so a pause loses nothing.

1. **Cards (pass 1).** One card per adventure from its prep doc. Use one sub-agent per 4-6 adventures,
   grouped by campaign order so each agent sees a coherent era; give each agent the card field list
   verbatim, the corpus notes above, and the instruction to consult the OCR text only for act/scene
   headings, GM sidebars and awards sections when the prep doc lacks them. Each sub-agent writes its
   cards directly to `cards/` and reports the beat tags and devices it used. Read a sample card from
   each agent before accepting its batch; send back cards that summarise plot instead of structure.
2. **Synthesis (pass 2).** Read all 52 cards (they are short; this fits in one context) and write
   SYNTHESIS.md. Compute the percentages and medians with a small script over the cards' beat tags
   rather than by eye; keep the script in `docs/adventure-analysis/tools/`.
3. **Template (pass 3).** Write TEMPLATE.md from the synthesis. Then test it: pick one adventure not
   used as the worked example, fill the template from its card, and check nothing important about that
   adventure fails to fit. Note any misfit in a "Limits of the template" section.

Regenerate baseline-counts.md if the specs change:
```
python docs/adventure-analysis/tools/baseline_counts.py
```

## Quality bar

- Structure, not plot. A card that reads like a synopsis is wrong. Every beat line should say what the
  beat DOES for the adventure (introduces the twist, forces a choice, ramps threat) not just what happens.
- Cite by adventure number everywhere in SYNTHESIS.md so claims are checkable against cards.
- Counts come from baseline-counts.md or a script, never from memory.
- Honest about the outliers: the anthologies, the sourcebooks and the SRM family distort medians; report
  them separately where it matters.
- ASCII only in every file (the repo's pre-commit hook rejects non-ASCII): write `--` and "nuyen",
  no curly quotes, no accents, no ellipsis characters.
- Keep the cards uniform; the synthesis script depends on the field names and the bracketed beat tags.

## Budget guidance

The prep docs total roughly 1.5 MB of markdown. A sub-agent handling 5 adventures will read about
150 KB and should finish in 150-300k tokens; ten such agents plus the synthesis pass is the expected
cost. Use Opus for the cards (the structural judgement is the hard part) and for the synthesis; the
counting script and the template's mechanical sections need no model at all. Commit after each pass:

```
git add docs/adventure-analysis && git commit -m "Adventure structure analysis: <pass>"
```

## Definitions (use these consistently)

- **Act / chapter:** the book's own top-level division. **Scene:** a headed encounter within an act
  (SRM books number these). **Beat:** a unit of story movement, one line in the beat list; a scene may
  contain several beats, and a beat may span scenes (e.g. a tail that runs across two locations).
- **Legwork:** any player-driven information gathering between the meet and the first set-piece.
- **Set-piece:** a scene the book maps and stats in detail expecting it to be played out.
- **Twist:** information that changes what the job IS. **Complication:** something that changes how
  hard the job is without changing what it is.
- **Opposition ladder:** the antagonist forces in the order the book expects the players to meet them.
