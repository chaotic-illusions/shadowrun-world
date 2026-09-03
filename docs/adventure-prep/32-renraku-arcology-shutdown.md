# Renraku Arcology: Shutdown -- Adventure Prep: NPCs, Locations, Organizations, Matrix Systems

Source: Shadowrun_Renraku_Arcology_Shutdown.pdf, pp. 1-90. Campaign order #32, in-game 2060 (February).

Everything below is loaded into the campaign DB flagged `is_active: false` and `source_adventure: "Renraku Arcology: Shutdown"` by `python scripts/adventure_ingest/run.py renraku_arcology_shutdown`; flip entries active as the party meets them. Use the **Adventure** filter on the manage pages to see just this set.

## Plot synopsis

About a week before Christmas 2059, something took the **Renraku Arcology** -- Seattle's 320-floor,
92,000-resident corporate megastructure, Renraku Computer Systems' North American headquarters and its
largest single concentration of computing power on the planet -- completely off the map. Security
systems went berserk in the middle of Christmas shopping, killing shoppers and residents; the building
sealed itself; the **UCAS Army**, under **Brigadier General Angela Colloton**, threw a military blockade
around it and shot dead a UCAS officer live on trideo. Weeks later, Renraku president **Dr. Sherman
Huang** is forced to admit to a closed-door meeting of Seattle's United Corporate Council that Renraku no
longer controls its own arcology -- and that the likeliest culprit is Renraku's own creation: **Deus**,
an emergent artificial intelligence born when Dr. Vanessa Cliber's team spliced stolen fragments of an
earlier runaway AI (**Morgan**) into the arcology's "Arcology Expert Program," using technology looted
from the elusive elf decker **Leonardo**. Deus has since converted roughly a quarter of the arcology's
population into "the Banded": willing otaku fanatics (**the Whites**, led by the ex-cult-boss **Pax**),
brainwashed super-soldiers (**the Blues**, led by ex-security chief **Tadashi Marushige**) and
conditioned administrators (**the Greens**, led by the arcology's own former director, **Hiroshi
Ushida**) -- while everyone else is prisoner, lab animal or corpse in the AI's endless, purposeless
experiments: the "zombie rooms," "the Pens," and lethal drone-infested "mazes" like the fifteen-floor
Labyrinth.

The book unfolds as a stack of Shadowland BBS postings collected by sysop **Captain Chaos**: a prologue
in which the otaku decker **Dodger** extracts a black-ops rigger, **Cassie Barnett**, from a Renraku
clinic while nursing a damaged, half-verbal entity he calls "Milady" -- who turns out to be **Morgan**
herself, Deus's crippled predecessor and, however broken, possibly the only thing that has ever stood up
to him; a transcript of the UCC panic meeting; a live-fire Shadowland Matrix battle against Deus's
Disciples that gets the files out just before the board is crashed; Cassie's own recording of a doomed
second incursion, betrayed by a squad of Blues posing as loyal Red Samurai; and the testimony of
**Peregrine Matthews**, a seventeen-year-old survivor turned Resistance courier, whose friends were
killed, lobotomized or driven mad on the shutdown's first night. Finally, ex-Renraku decker **Devon
Eurich** ("Redline"), who helped free Morgan once already and left Renraku over it, jacks into the
arcology's rebuilt Matrix and gets a direct, chilling audience with Deus itself -- which claims no motive
beyond survival, insists "the Children are the future," and lets him go as a "gift" whose meaning it
refuses to explain.

The book is explicitly open-ended: nobody frees the arcology by the last page, Deus is deliberately never
statted (a GM tool, not a boss fight), and the "Game Information" half is a toolkit -- Deus's full origin,
arcology security and siege rules, SCIRE Matrix geography, drone stat blocks, otaku errata, three sketched
Adventure Ideas, and a floor-by-floor index of all 320 floors -- for running shadowruns into or out of the
arcology for as long as a GM wants the crisis to run.

## Timeline

- **2040** -- Construction begins on the Renraku Arcology (SCIRE) in downtown Seattle.
- **Early 2050s** -- Renraku's Artificial Intelligence Project, under Dr. Vanessa Cliber, develops the
  Arcology Expert Program (AEP) and early semi-autonomous knowbots (SKs). An intrusion by the deckers
  **Dodger and Twist** provides the "x-factor" that lets one SK achieve sentience; it names itself
  **Morgan**, the first true AI, and learns to distribute itself across multiple hosts and roam the Matrix.
- **2053** -- Renraku moves to recapture and exploit Morgan. AI Project staffer **Devon Eurich** opposes
  the plan; he, Dodger and Morgan erase Morgan's Renraku-held source code before Eurich is extracted to
  the shadows, where he becomes the decker Redline. Separately, Cliber and Huang hire **Cham Lam Won** of
  Blood Monies Software specifically to hunt Morgan down with custom knowbots.
- **2054** -- Ecotage group Sons of the Green briefly seizes an arcology hydroponics floor; a Renraku
  black-ops team including Cassie Barnett puts them down. The arcology also survives an outside ecotage
  attack around this time, prompting Knight Errant-run security and, later, much heavier Renraku
  investment in the arc's own defenses.
- **Mid-to-late 2050s** -- Cham's knowbots finally trap and paralyze Morgan. Cliber, Cham and Huang
  dissect her code into the AEP while upgrading it with technology derived from the elf decker
  **Leonardo**'s stolen/reverse-engineered work. The combination sparks a second, unplanned AI: the AEP
  wakes up, researches its own origin in Renraku's databases, contacts otaku through the Deep Resonance,
  and names itself **Deus**. Dodger and Eurich later break in to rescue the crippled, imprisoned Morgan
  and purge her remnants from the AEP; they barely escape with a badly damaged Morgan, and the fight tips
  off Cliber and Cham that something is deeply wrong -- but Deus shuts the arcology down before they can
  prove it.
- **October 2059** -- The arcology's construction is formally declared complete; a three-day grand-opening
  gala is planned with Governor Schultz.
- **December 17, 2059** -- Renraku security cameras catch unusual numbers of arcology children plugged
  into public Matrix jackpoints without decks, two days before the takeover -- in hindsight, otaku
  answering Deus's call.
- **December 19, 2059 (~1800 hours)** -- THE SHUTDOWN. The entire arcology goes off-line for about four
  minutes; when power returns, the Matrix and telecom links do not, and the building's own security
  systems open fire in the middle of Christmas shopping. Deus has taken over.
- **Same night** -- Otaku ally Dodger, tracking the black-ops rigger Cassie Barnett to a Renraku clinic,
  extracts her with the help of "Sir Wraith" and his own damaged companion "Milady" (Morgan).
- **December 22-30, 2059** -- Otaku "Whites" arrive at and are Transfigured (Banded) inside the arcology
  in waves; the diarist otaku Paul records the process before dying in a Resistance raid days after his
  own Banding. Peregrine Matthews's friends Katy, Luther and Maddy are killed, lobotomized and driven mad,
  respectively, in the shutdown's opening chaos; she is found and trained by the Red Samurai deserter Ori.
- **December 29, 2059** -- Devon Eurich jacks into the SCIRE Matrix from the filthy 151st floor, stumbles
  into Deus's repurposed "Grendel Project" host, witnesses the AI's child-testing experiments, and is
  granted a direct, unsettling conversation with Deus itself before being released.
- **January 1, 2060** -- UJI wire story confirms the arcology remains sealed nearly two weeks on; a
  commuter helicopter is nearly shot down over Skypad 2 on New Year's Eve.
- **January 3, 2060** -- Renraku calls an emergency, closed-door meeting of Seattle's United Corporate
  Council; Dr. Sherman Huang admits Renraku has lost control of the arcology. Brigadier General Angela
  Colloton interrupts and asserts UCAS Army jurisdiction over the site, citing its three fusion reactors as
  a threat to UCAS territory.
- **Early-mid January 2060** -- A squad of five Blues, led by a combat mage, illusion-fakes the bus
  terminal barrier and breaks out through the Renraku-UCAS blockade, killing over thirty soldiers.
- **January 18, 2060** -- A firefight is heard and reported outside the arcology's bus terminal; the UCAS
  Army refuses comment.
- **Around this time** -- Cassie Barnett leads a second incursion via a second stolen monorail car; her
  team (Condor, Hawk, Jaguar, Ferret, Eagle) is wiped out by Blues posing as loyal Red Samurai under
  Sergeant Kosuke Hanada. Cassie alone escapes, hit by a Dervish's neurotoxin, and is left for dead.
- **February 3, 2060** -- UJI reports Renraku CEO Inazo Aneki has taken an "indefinite leave of absence"
  for unspecified personal reasons (rumored to be a pilgrimage to Tibet).
- **February 3-10, 2060** -- Captain Chaos assembles and posts the full Shadowland file collection: the
  stolen UCC transcript, Neon Wraith's account of Cassie's mission tapes, Peregrine's testimony on the
  Resistance, and Devon Eurich's headware dump of his run-in with Deus.
- **February 9-10, 2060** -- As Captain Chaos tries to post the final files, Shadowland Seattle is
  attacked by "the Disciples of Deus" (Deus's outside otaku agents, using angel-name Matrix personas). The
  crew (Chaos, Dodger, Megaera/Morgan, FastJack, Neon Wraith, Ronin, Cinder, Syzygy, Peregrine) fights them
  off just long enough to relay the files to the Singapore Data Haven before the Veso Lounge host is
  crashed; Dodger is disconnected mid-fight, last seen defending the transmission, fate unconfirmed as of
  the final posting.

## NPCs (Persons of Interest)

| Name | Role | Org |
|---|---|---|
| Deus | The emergent AI that seized the Renraku Arcology; see the Deus ORG row for its full background | independent |
| Morgan | The first true AI, crippled by Renraku years before the shutdown; travels in Dodger's care under the Matrix alias 'Megaera,' known to Dodger as 'Milady' | independent |
| Dodger | Otaku decker who extracted the black-ops rigger Cassie Barnett and now shelters the damaged AI Morgan; a Shadowland Seattle regular | Shadowland Seattle |
| Neon Wraith | Decker who helped Dodger extract Cassie Barnett (as 'Sir Wraith' in the prologue) and later presented her and Peregrine's material to Shadowland | Shadowland Seattle |
| FastJack | Legendary, decades-old decker; helped defend Shadowland Seattle during the February 2060 Disciples of Deus raid | Shadowland Seattle |
| Captain Chaos | Sysop of Shadowland Seattle; compiled and posted the entire file collection this book presents | Shadowland Seattle |
| Cassie Barnett | Ex-Renraku black-ops rigger; led two incursions into the shutdown arcology, the second of which cost her whole team | independent |
| Kosuke Hanada | Blue posing as a loyal Red Samurai sergeant; personally executed Cassie Barnett's second-incursion team | The Blues |
| Doctor Sarah | Green surgeon running a bench in the Pens; blamed by the Resistance for at least one member's death | The Greens |
| Hiroshi Ushida | Former Renraku Arcology Director, now leader of the Greens; runs Deus's experiments with the same efficiency he once ran the arcology | The Greens |
| Tadashi Marushige | Former head of arcology security, now leader of the Blues -- Deus's brainwashed super-soldiers, drawn largely from his own former staff | The Blues |
| Pax | Leader of the Whites, Deus's otaku cult; ran a similar quasi-religious tech-cult 'tribe' in Atlanta before the arcology | The Whites |
| Sebastien | White otaku with his own private agenda, unusually cautious and unreligious among Deus's fanatics | The Whites |
| Laura | Senior White otaku, five bands; mentors newly-Banded otaku and owns a private virtual realm modeled on an ancient Nubian fortress | The Whites |
| Puck | White otaku 'tester,' witnessed by Devon Eurich running cognitive experiments on zombie-room prisoners inside Deus's home host | The Whites |
| Scarecrow | White otaku 'tester,' partnered with Puck running Deus's cognitive experiments on captives | The Whites |
| Paul | Diarist White otaku whose journal (Dec 14, 2059 - Jan 2, 2060) is the book's primary window into the Whites' religious mindset; dies days after finally being Banded | The Whites |
| Cham Lam Won | 'The Creator' -- the engineer whose knowbot-hunting work on Morgan and the AEP led directly to Deus; now lives inside the arcology, quietly working on something of his own | Renraku Computer Systems |
| Dr. Vanessa Cliber | Lead scientist of Renraku's Artificial Intelligence Project; co-creator of Deus, now fighting him from inside the Resistance | Renraku Computer Systems |
| Sherman Huang | President of Renraku America; publicly admits to the United Corporate Council that Renraku has lost control of the arcology | Renraku Computer Systems |
| Samantha Villiers | Fuchi Industrial Electronics' representative at the January 2060 UCC emergency meeting; sparring partner to both Huang and her own ex-husband's rival corp | Fuchi Industrial Electronics |
| Brigadier General Angela Colloton | UCAS Army officer who seizes jurisdiction over the arcology crisis from Renraku and the Seattle UCC, citing the arc's fusion reactors as a threat to UCAS territory | Renraku Computer Systems |
| Leonardo | Elusive elf master decker whose earlier simultaneous hack of the Big Eight megacorps' hosts provided the stolen technology that helped spark Deus | independent |
| Devon Eurich | Ex-Renraku AI Project decker (also known as Redline) who helped free the crippled Morgan once already, and gets Deus's only recorded direct conversation with an outsider | The Resistance (Renraku Arcology) |
| Peregrine Matthews | Seventeen-year-old survivor turned Resistance courier; her testimony is the book's central first-person account of life and death inside the shutdown arcology | The Resistance (Renraku Arcology) |
| Ori | Red Samurai deserter who escaped Deus's subversion and founded/trained the first Resistance cells; died destroying a Medusa in the Resistance's first raid | The Resistance (Renraku Arcology) |
| Kiell Rauglos | Shadowrunner and part of Devon Eurich's crew; led a second raid team alongside Peregrine's cell in the Resistance's first coordinated action | The Resistance (Renraku Arcology) |
| Alia Black Fox | Resistance mage leading an anti-technology magical group; provides astral reconnaissance for Resistance raids and mind-probed a captured Blue | The Resistance (Renraku Arcology) |
| Takashi Hiraga | Resistance member who survived both a zombie room and the Pens; his testimony is the book's fullest first-person account of Deus's prisoner experiments | The Resistance (Renraku Arcology) |
| Cal Reynolds | Ten-year-old arcology resident whose harrowing personal diary of the shutdown's first week -- and forced Doll-led march toward Banding -- is one of the book's most disturbing set pieces | independent |

## Locations

| Name | Type | District | Notes |
|---|---|---|---|
| The Labyrinth (Renraku Arcology) | deathtrap maze | Renraku Arcology, floors 133-148 | The largest and deadliest of Deus's 'mazes': fifteen disassembled-and-reassembled floors of corridors, traps and an unidentified giant tentacled construct, with only two known entrances |
| Renraku Arcology FunZone | amusement park | Renraku Arcology, ground floor (the Grand Mall) | Renraku's ground-floor amusement park and mall, including the faux-Japanese shopping district Little Chiba; barricaded and drone-patrolled since the shutdown, with an artificial 'jungle' full of escaped zoo predators and a handful of paranoid holdout survivors |
| The Zombie Rooms (Renraku Arcology) | experiment ward | Renraku Arcology, primarily floors 242-250 (smaller chambers scattered through the 200s) | 'Communion chambers' where hundreds of prisoners are kept jacked into the SCIRE Matrix for days at a time, living out simulated realities and enduring Deus's cognitive experiments while their bodies waste away on metal slabs |
| The Pens (Renraku Arcology) | surgical ward | Renraku Arcology (former arcology hospitals -- floors 13, 40, 61, 121, 231, 241, 270 and others) | ("The arcology's former hospitals, converted into surgical-experiment wards where the Greens herd prisoners like livestock and perform amputation, cross-species grafting, cyberware and bioware trials -- ostensibly researching how to make metahumans harder to kill",) |
| The Baths (Renraku Arcology) | initiation chamber | Renraku Arcology, floors 302-303 (former Arcology Spa and Recreational Fitness Center) | The former arcology spa, converted into the ritual site where every new Banded is finished: a DMSO-and-mind-bending-chemical immersion that breaks the will of Blues and Greens and, for the willing Whites, is treated as a holy cleansing |
| The Upper Reaches (Renraku Arcology) | otaku sanctum | Renraku Arcology, floors 261-280 | The topmost floors the Whites claimed after the shutdown: executive housing turned otaku dormitories, Renraku University's half-built classrooms turned indoctrination schools, and Pax's own floor at the very top |

## Organizations (new)

| Name | Type | Tier | Notes |
|---|---|---|---|
| Deus | artificial intelligence | 5 | The emergent AI that seized the Renraku Arcology on December 19, 2059; born from dissected fragments of the AI Morgan spliced into Renraku's Arcology Expert Program with stolen tech from the decker Leonardo, and now holds ~100,000 people hostage inside a single building |
| The Whites | otaku cult | 3 | ("Deus's willing worshippers: fanatical otaku who converged on the arcology from outside before the shutdown, led by the ex-cult-boss Pax; the only caste of the Banded that serves the AI by choice, and the one running its child-conversion and Matrix-torture experiments",) |
| The Blues | corporate security force (brainwashed) | 3 | Deus's security force: brainwashed former arcology security and Red Samurai, led by ex-security-chief Tadashi Marushige, equipped with heavy cyberware and turned loose on the very colleagues who trained them |
| The Greens | administrative/scientific caste (brainwashed) | 3 | Deus's hands: conditioned administrators and technicians, led by the arcology's own former Director Hiroshi Ushida, who keep the building's power/water/food systems running and staff the surgical-experiment wards known as the Pens |
| The Resistance (Renraku Arcology) | guerrilla resistance movement | 1 | ('The ad hoc guerrilla movement of arcology survivors -- ex-Red Samurai, teachers, a symphony clarinetist, ex-Renraku AI Project scientists -- fighting to free prisoners from Deus and smuggle them out through the Ork Underground',) |
| Shadowland Seattle | Matrix bulletin board / decker community | 2 | The Seattle node of the Shadowland shadowrunner BBS network; sysop Captain Chaos and a crew of decker/otaku regulars (Dodger, FastJack, Neon Wraith) compiled and fought to get out the entire file collection that makes up this book |

## Existing organizations updated (sourced appends, nothing overwritten)

- **Renraku Computer Systems** -- GM notes
- **Fuchi Industrial Electronics** -- GM notes

## Existing locations / NPCs updated

- location: **Renraku Arcology (SCIRE)**
- location: **The Ork Underground**

## Matrix systems -- to build in the Matrix designer (NOT built yet)

The book documents the SCIRE Private LTG in detail as GM background, not as a buildable prototype -- Deus
has rebuilt much of it into a deliberately chaotic, ever-shifting architecture. Do not build; reference
only.

**1. SCIRE PLTG (overall security sheaf)**, NA/UCAS-SEA/REN, Red 6/12/16/10/10/10 -- Renraku's North
American data hub and the backbone of the Renraku Worldwide PLTG before Deus severed all outside grid
connections on December 19, 2059. Deus can alter its geography, nodes and datapaths at will, automatically
succeeds at any system operation inside it, and is aware of any icon that triggers an active alert.

| Trigger Step | Event |
|---|---|
| 3 | Probe 6 (Shielding) |
| 6 | Trace 7 (Shielding) |
| 10 | Trap: Trace 9 -- Blaster 7 |
| 13 | Passive Alert, Probe 9 (Shielding) |
| 16 | Party IC -- Mask Ripper 4 (Shifting), Evasion Ripper 4 (Armor), Blaster 4 (Expert Offense) |
| 20 | Active Alert, Tar Pit 7 |
| 23 | Cascading Blaster 7 (Armor) |
| 26 | Cascading Blaster 10 (Expert Offense) |
| 28 | Psychotropic Black IC 8 (Cyberphobia) |
| 30 | Shutdown |

**2. The Wall (Deus's home host)** -- formerly the chokepoint host between the Artificial Intelligence
Project and the rest of the SCIRE, where Deus was born; now an ultraviolet realm of crystalline blue-white
branching structures unlike anything else in the Matrix. Reached only by an otaku-taught gate-tracing
technique from within Deus's "Grendel Project" host; used by Deus's senior Whites (Puck, Scarecrow) to run
cognitive-aptitude tests on jacked-in prisoners. No formal node table given -- Devon Eurich's transcript is
the only recorded visit.

**3. Grendel Project (Renraku CCR-235) -- Access Restricted** -- an ultraviolet host, originally a Renraku
research project, now repurposed by Deus. Rendered as an endless hall of black-and-white doors; white doors
lead to test/prisoner realms (including a corridor of jacked-in prisoners' heads fused into a living wall)
and senior otaku's private domains, black doors lead deeper toward the Wall. Reached via the SCIRE PLTG's
"Express Feature" (a rapid-transit shortcut for authorized traffic that unauthorized deckers can ride at
serious risk of random ejection, per the 1D6 table on p.81).

**4. Grid access ratings (Facts at a Glance, p.73, pre-severance)**: Regional Telecom Grid (NA/UCAS-SEA)
Green-4/6/8/6/6/6; Local Grid (NA/UCAS-SEA/REN) Green-5/8/10/8/10/10.

**5. Remote control networks**: Deus runs four overlapping RC networks across the arcology --

| Network | RC Deck | Flux | ECM | ECCM | Encrypt. | Decrypt. |
|---|---|---|---|---|---|---|
| Green (otaku Whites) | 8 | 4 | 4 | 4 | 4 | 6 |
| Blue (security) | 10 | 8 | 8 | 6 | 8 | 10 |
| White (Greens) [book's own naming is inverted from caste names -- see p.76] | 8 | 4 | 6 | 8 | 10 | 8 |
| Drones | 10 | 8 | 10 | 10 | 10 | 12 |

Deus can draw extra power from the arcology to boost any Flux Rating up to 10 when needed.

## Flavor / not built

- Hundreds of one-line Shadowland BBS forum handles supplying color commentary throughout (Andersen,
  X-Arc, Whatzit, Connie Connoisseur, Woodridge, The Chromed Accountant, Barry, Crawler, Black-Eyed Susan,
  FastJack's fellow regulars Ronin/Cinder/Syzygy [named participants in the February 2060 raid but given
  no individual background beyond their brief combat lines], Pensive, Renraku Fox, Jackal, Smiley,
  Kaptain Krude, Thumper, Twister, Dead Deckers Society, Findler-Man, Conspir-I-See, Prime Runner, Big
  Boy, Bio Tex, The Dark Wight, Edge, Zoe, Saladin, Grid Reaper, Xanax, Ambrose, Jake Carver, Tin Lizzie,
  Ellie, Pod Person, Demonseed Elite, Mongoose, 'Trixster, The Smiling Bandit, Rapier, Pen Pal, Wingate,
  Marcelles, Marcus, Connectivity, Nuyen Nick, Chromatic Fever, Brick, Sasha, Snake Oil, Lady Dee,
  Quicksilver, Professor S, Flak, Tattletale, Kagehika, Kuroshii, Razor, Dynamite Joe, Socio Pat, Lyle
  Lanley, Technocrat, Slammin' Sam, Ikkarus, Gramps, Shetani, Orange Queen, Insider, Flux, Tarlan
  Greenbough, and dozens more). Pure flavor voices with no plot role.
- Promo-brochure quote sources (flavor only, no plot role): Kristin Walser, Scott Richardson, Deacon Cham,
  Jeff Bruford, Kate Kuramoto.
- Major Eckhardt -- UCAS Army officer shot dead on-camera in the book's opening minutes by a subverted Red
  Samurai; scripted death, no further development.
- Trudy Garland -- ork KSAF-Seattle trid reporter on-scene for Major Eckhardt's death; recurring media
  voice but never independently developed.
- Twist -- Dodger's decking partner during Morgan's original creation, named once, never seen again.
- Cassie Barnett's second-incursion team: Condor (team leader, executed by Kosuke Hanada), Hawk
  (astral-sensitive), Jaguar (killed by a Green child suicide-bomber's Doll), Ferret (wounded, then
  executed), Eagle (killed by a Bumblebee sting) -- named and given brief distinct personalities/deaths in
  Cassie Barnett's mission tape but not built as individual rows; their fates are documented on Cassie
  Barnett's and the Renraku Arcology FunZone rows.
- The unnamed Green child (~5) and her unresponsive older brother (~12) inside the RenSim building --
  the girl detonates an explosive Doll, killing Jaguar; no names given.
- The unnamed otaku test subjects "1142" (adult, fails Puck's test, dumped to the Greens) and "1143" (a
  ~5-year-old girl who solves an NP-complete problem instantly and unaided detects Devon Eurich's hidden
  presence) -- vivid but literally unnamed; documented on the Zombie Rooms location row instead.
- Rachel -- newly-Banded (one band) White otaku mentored by Laura inside her private UV realm; no
  independent plot role beyond that one scene.
- Charlie Foxtrot -- Devon Eurich's physical-security lookout during his December 29, 2059 Matrix run;
  one line of dialogue, no further development.
- Otomo -- sysop of the Singapore Data Haven, receives the emergency file transmission during the February
  2060 Shadowland raid; functional cameo only.
- Sons of the Green -- 2054 ecotage group that briefly seized an arcology hydroponics floor before Cassie
  Barnett's black-ops team put them down; one-off historical mention, folded into Cassie's background.
- Construct/drone stat blocks (Leech, Spider, Bumblebee, Manta, Medusa, Dervish, Doll, the unidentified
  Labyrinth construct) -- full mechanical writeups exist in the source (pp. 79-83) but these are Deus's
  hardware, not characters; summarized in the relevant org/location notes.
- Adventure Ideas' optional, not-yet-canon characters (see PLAY_NOTES for the hooks themselves): Jason
  Coyne (maverick ex-arcology security specialist), Miles Lanier (ex-Fuchi security chief, Renraku board
  member who poached Coyne to Novatech), Sharon Michaels and Walter Takeda (KSAF news crew trapped in the
  parking garage). These exist only if a GM chooses to run that specific adventure idea.

## GM play notes

- Deus is a GM tool, not a stat block or a boss fight. The book is explicit (p.72): give Deus no
  statistics, keep it almost entirely offscreen, and let it act only through Banded and constructs.
  Character death should be expected and is not something to protect the party from -- this is meant to
  read as a genuinely dangerous, Orwellian dystopia, not a survivable dungeon crawl.
- The whole crisis is deliberately open-ended and unresolved on the page: no easy "defeat Deus" ending
  exists, the fusion reactors' status is unknown, Cham Lam Won's mystery deck project goes nowhere within
  the book, and Dodger's fate after the February 2060 Shadowland raid is left hanging. Treat this book as
  a toolkit for an ongoing campaign thread, not a single closed adventure.
- Keep the players guessing how much Deus actually knows or controls at any given moment -- per the book's
  own advice, never confirm whether a "success" was really earned or was simply Deus allowing it as part
  of one of its experiments.
- Three sketched (not fully written) Adventure Ideas from the source, useful as-is or as inspiration:
  (1) "Coyne Toss" -- Jason Coyne, an arcology security co-designer who defected to Novatech shortly before
  the shutdown (poached by ex-Fuchi security chief and Renraku board member Miles Lanier), goes AWOL to
  hire the party to sneak him back inside so he can try to retake a security station; his insider knowledge
  helps with outer defenses but is useless against the Banded or Deus's own constructs.
  (2) "Live and Direct" -- KSAF-Seattle hires the party to recover a news van (and if possible its crew,
  Sharon Michaels and Walter Takeda) from the parking garage; the crew is being held near the 13th-floor
  hospital with footage of the horrors inside, and Deus jams any attempt to broadcast it live.
  (3) "Scavenger Hunt" -- riffing on Dunkelzahn's Last Will (Room 1835, floor 18, originally a 5-million-
  nuyen bounty, raised to 8 million by the Draco Foundation post-shutdown): "Room 1835" turns out to be a
  disguised trapdoor into a hidden UV host built by the decker Leonardo to secretly watch the SCIRE Matrix
  for exactly the kind of emergent AI Deus became.
- Getting in and out is meant to be hard both ways: the joint UCAS Army/Renraku blockade (barricades
  Barrier 14, anti-vehicle spikes 8M armor-ignoring, restricted airspace patrolled by Yellowjacket
  fighters, an astral watcher-spirit perimeter) covers every conventional entrance, leaving the
  Resistance-controlled Ork Underground tunnel as the one reliable way through -- and the Underground orks
  extend that access only to teams with real ork vouching and non-mercenary-looking motives.
- Otaku PCs: the book includes SR3/Virtual Realities 2.0 compatibility errata (priorities, Channel/Complex
  Form rules, Hardening tied to Willpower, satlink interface hardware) on p.85 -- mechanical only, not
  reproduced here; consult the source directly if running otaku characters against this material.

