# DNA/DOA -- Adventure Prep: NPCs, Locations, Organizations, Matrix Systems

Source: Shadowrun 1e - DNA-DOA {FASA7301}.pdf, pp. 4-62. Campaign order #3, in-game 2050 (December).

Everything below is loaded into the campaign DB flagged `is_active: false` and `source_adventure: "DNA/DOA"` by `python scripts/adventure_ingest/run.py dna_doa`; flip entries active as the party meets them. Use the **Adventure** filter on the manage pages to see just this set.

## Plot synopsis

**Biogene Technologies**, a mid-size San Diego genetic-engineering firm, hires the runners through its
Seattle Special Operations man **Jason Walker** (over dinner at the Eye of the Needle, weapons checked
with Cripps the elven maitre d') for a datasteal on **Aztechnology's Tacoma Research Park**: grab the
Metavirus data file and a sample of the viral vector from the underground Beta Section and deliver
them to the container ship *S.S. Misha* at Wharf 114 before dawn. Aztechnology is about to move the
research to Aztlan, so the run is tonight. Pay is 120,000 nuyen for the team, 60,000 up front, plus
a van of AK-97s, chemsuits, C-4 and two canisters of the catalyst that turns the facility's
Plastisteel-7 wall into bubble gum.

Nothing is what it seems. The Metavirus (Dr. **Carol Owens**' work, meant to control the Metagene
for good) has been weaponized by Dr. **Simon Peterhoff** into animal/human force-breeds -- Wolf,
Tiger and Bear Sapiens -- using Orks kidnapped from the Tacoma sewers as raw material. Twenty-four
hours before the run an aerosol, self-mutating Metavirus IV got loose in Beta Section; Aztechnology
sealed Alpha and Beta, threw Owens in a cell on Peterhoff's say-so, and is watching the survivors
eat each other as a "survivability test" through the astral eyes of apprentice mage **William
Blount**. The runners crawl into a charnel house: virus-warped technicians, giant cockroaches, flesh
worms, an infected troll, and Peterhoff himself, insane and living in the ventilation ducts.

Meanwhile the **Hands of Five** -- the Tacoma chapter of the anti-metahuman terror group **Alamos
20,000** -- have a traitor inside Biogene (Walker's assistant **Wendell Holmes**), have kidnapped a
loved one of one of the runners to blackmail the data out of them (the optional traitor subplot), and
have killed the Biogene contact on the *Misha*. At the docks the Alamos ambush collides with a full
Aztechnology Response and Pursuit Team, and the team flees into one of the warehouses where Alamos
burned thousands of metahumans on the Night of Rage eleven years ago -- and finds Ork children.

Their babysitter **Jenny Hernandez** leads them to **Wilhem Park**, a shopping mall buried by the
2017 Tacoma eruptions and now the hidden home of 400 Orks and their families under "mayor" **Allan
Bronston**. Bronston wants the Orks Aztechnology kidnapped from the sewers rescued from Alpha Section,
and Carol Owens -- his old lab colleague, "The Tailor" -- brought to him. The second raid frees the Ork
women and children and Owens, then Bronston confronts Owens over what she let Aztechnology do,
trades the Alamos hostage (his Orks rescued it) and hands over a Biogene safe-house address.

The safe house is a trap: Holmes routed the message to the Hands of Five, who arrive with Martin
Honnicker to take hostages, followed by an Aztechnology team under Jacob Barre. Walker finally shows
with the money: 30,000 for the sample, 30,000 for the file, 50,000 more for Owens. Afterwards
Aztechnology and Alamos 20,000 both want the runners' blood, Biogene keeps them at arm's length, and
nobody sane will hire them for a month or two -- but to those who know, they are the runners who
burned Aztechnology.

## Timeline

- **February 7, 2039** -- the Night of Rage. Humanis rally in Tacoma; the Metroplex Guard "deplaces"
  metahumans to the docks for the liner *Asian Princess*; the warehouses burn; Tacoma's downtown is
  gutted; survivors found Wilhem Park in the sewers. Prologue "Into the Flames", pp.4-6.
- **The morning** (traitor subplot) -- a Hands of Five Mr. Johnson meets the traitor on the monorail
  and hands over a Ronnie Bean homing device; two hired samurai rough up anyone who follows.
- **Evening** -- Holmes collects the team from the CBI; dinner at the Eye of the Needle; Walker's
  briefing; gear van; sewer entry about a kilometer from the facility.
- **Night** -- Beta Section (viral accident 24 hours old). Blount spots them astrally (2D6 <= 4 each
  turn); an Aztech Response Team deploys into the sewers too late.
- **Before dawn** -- Wharf 114: Alamos ambush on the *S.S. Misha*, Aztechnology Response and Pursuit
  Team arrives in force; escape into the Night of Rage warehouse; Jenny; Wilhem Park.
- **Next day** -- Alpha Section raid (systems junction box; guards from the elevator 2D6+2 turns after
  the alarm, +3 every four turns; Wage Mage 3D6+2 turns; Corporate Decker 2D6+2 turns). Bronston
  vs Owens. Biogene safe house in the Puyallup Barrens: Hands of Five, then Aztechnology.
- **Monday, December 12, 2050** -- Seattle News-Intelligencer: Lone Star accuses Aztechnology of
  military maneuvers at the Tacoma docks; an Ares Dragon crashes at the Seattle Pyramid; Owens named
  Biogene head of Biotechnology Research (success) or Aztechnology absorbs Biogene and Tacoma sewer
  deaths are up 300 percent (failure).

## NPCs (Persons of Interest)

| Name | Role | Org |
|---|---|---|
| Jason Walker | Biogene's Seattle Special Ops man; the runners' by-the-book Mr. Johnson | Biogene Technologies |
| Wendell Holmes | Walker's assistant and the Alamos 20,000 informant inside Biogene | Biogene Technologies |
| Dr. Carol Owens | 'The Tailor' -- designer of the Metavirus; imprisoned by Aztechnology; Biogene's prize | Aztechnology |
| Dr. Simon Peterhoff | Metagene Applications director gone insane; breeds Wolf/Tiger/Bear Sapiens from kidnapped Orks | Aztechnology |
| Allan Bronston | 'Mayor' of Wilhem Park; Night of Rage survivor; Owens' former lab assistant | Wilhem Park Enclave |
| Jenny Hernandez | Human metahuman-rights activist who babysits Wilhem Park's children and guides the team in | Wilhem Park Enclave |
| Martin Honnicker | Charismatic fanatic leading the Hands of Five; 20+ metahuman deaths | Hands of Five |
| Claude Pierce | Alamos-Tacoma field leader at the Misha ambush | Hands of Five |
| Terry Carey | Alamos-Tacoma field leader at the Misha ambush | Hands of Five |
| Daniel Sinclair | Alamos-Tacoma field leader at the Misha ambush | Hands of Five |
| Jorge Sanchez | Aztechnology 'personal efficiency expert' -- a globe-trotting enforcer who hates germs | Aztechnology |
| Evelyn Franklin | Sanchez's assistant, a powerful hermetic mage with a Power Focus who watches her boss | Aztechnology |
| Samuel Silver | Long-time Aztechnology security mage who dreams of blending magic with bioengineering | Aztechnology |
| William Blount | Apprentice hermetic mage astrally spying on Beta Section for Aztechnology | Aztechnology |
| Jacob Barre | Aztechnology corporate enforcer who has never failed to retrieve a wayward employee | Aztechnology |
| Eduardo Eman | Street mage newly gone corporate; coarse, confrontational, Mana Bolt 7 | Aztechnology |
| Captain H.C. Strum | Commander of the Aztechnology Response and Pursuit Team that levels the Tacoma wharf | Aztechnology |
| Cripps | Elven maitre d' of the Eye of the Needle; his podium hides more electronics than an office | independent |
| Johnny Clean | Ex-UCAS White Lion street samurai for hire: 'Speak softly and carry a big fraggin' gun' | independent |
| Louise Frost | Half-Salish street samurai, ex-Sisters Sinister, freelance; supports her father in the Barrens | independent |
| Andrew Shalene | Elf hermetic mage and jackless decker who lives for the rush; daylight allergy | independent |

## Locations

| Name | Type | District | Notes |
|---|---|---|---|
| Aztechnology Tacoma Research Park | research lab | Tacoma | 12-building corporate campus with a 20 m pyramid; Metavirus labs (Alpha/Beta) underground behind a Plastisteel-7 wall |
| Old Tacoma Sewers | sewer system | Tacoma | Abandoned 30 years; ghouls, squatters, sewer Orks, gangs, the odd vampire; the way into the Research Park |
| Wilhem Park | subterranean community | Tacoma | Shopping mall buried by the 2017 eruptions, now a gas-lit Ork town of 400 under a condoplex |
| Night of Rage Warehouses | ruins | Tacoma (docks) | Burned-out metahuman holding pens from 2039; a hidden, forbidden back door to Wilhem Park |
| Tacoma Docks (Wharf 114) | transportation hub | Tacoma | Container wharf; the S.S. Misha drop point; the Alamos-vs-Aztechnology battleground |
| The Corporate Bums and Indigents Club | bar | Seattle (runner turf) | 'The CBI' -- the runners' hangout where Holmes finds them |
| Biogene Safe House (Puyallup) | safehouse | Puyallup Barrens (edge) | A house a few streets from a sewer sump; the Not-So-Safe House where Alamos and Aztechnology converge |

## Organizations (new)

| Name | Type | Tier | Notes |
|---|---|---|---|
| Biogene Technologies | corporation | 3 | Mid-size genetech firm sponsoring the run; guarded by Knight Errant; rises or is absorbed by Aztechnology |
| Alamos 20,000 | terrorist organization | 3 | Violent anti-metahuman terror network behind the Night of Rage; political front is the Humanis Policlub |
| Hands of Five | terrorist cell | 2 | Tacoma chapter of Alamos 20,000 under Martin Honnicker; kidnappers, blackmailers, ambushers |
| Wilhem Park Enclave | community | 2 | ~400 Orks and their human kin living in a buried mall since the Night of Rage; 'mayor' Allan Bronston |

## Existing organizations updated (sourced appends, nothing overwritten)

- **Aztechnology** -- profile; GM notes; leadership: Juan Atzcapotzalco, Salvador Ramierez, Dr. William Espinata; enemies: Biogene Technologies, Wilhem Park Enclave
- **Knight Errant Security Services** -- GM notes
- **Lone Star Security** -- GM notes
- **Humanis Policlub** -- GM notes; allies: Alamos 20,000, Hands of Five
- **Seattle Metroplex Guard** -- GM notes

## Existing locations / NPCs updated

- location: **The Space Needle**
- location: **Aztechnology Pyramid**

## Matrix systems -- to build in the Matrix designer (NOT built yet)

**1. Aztechnology Tacoma -- Alpha Section system** (map DNA/DOA p.34; SR1 color-rating notation).
Isolated from the outside; reachable only from terminals inside Alpha (I/OP-1 meeting room, I/OP-2
Sanchez's office, I/OP-3 Main Security, plus the guard-quarters keyboard). A Corporate Decker defends
it 2D6+2 turns after security is alerted. Worth building as the adventure's one live host.

| Node | Function | Rating / IC |
|---|---|---|
| SAN-1 | Link to the main Aztechnology Seattle system only | Red-8, Barrier 6 |
| SAN-2 | Link to the (crashed) Beta Section system -- leads nowhere | Blue-6 |
| CPU-1 | Alpha and Beta central processor | Orange-7, Barrier 7, Trace and Burn 5 |
| DS-10 | General data storage | Green-6, Access 4 |
| SPU-1 | Section environmental systems | Green-4 -> DS-1 seasonal defaults / usage records (Blue-2) |
| SPU-2 | Research and analysis systems | Orange-3, Access 5 -> DS-2 general records (Green-4), DS-3 specific project records (Orange-2, Access 3) **copy of the Metavirus datafile handout only** |
| SPU-3 | Sectional administration | Orange-4, Access 5 -> DS-4 personnel (Green-3, Access 2), DS-5 general (Green-3, Access 2), DS-6 restricted files (Orange-5, Access 5, Trace and Burn 5), I/OP-1 meeting-room terminal (Green-4, Access 4) |
| SPU-4 | Local security sub-processor: hallway cameras every 10 m and every maglock keypad in Alpha (and Beta, were it working) | Orange-5, Barrier 5, Blaster 5 -> DS-7 security files (Green-4, Access 4), I/OP-2 office terminal (Green-3, Access 3), I/OP-3 Main Security terminal (Green-3, Access 3) |
| SPU-5 | Secondary research sub-processor | Orange-3, Access 4 -> DS-8 backup files (Green-5, Access 2), DS-9 archive files (Green-3, Access 2) |

**2. Beta Section system** -- crashed. Physical damage killed it as a whole; the data storage unit in
the Analysis/Experimentation Area (Beta 10) still runs off a cyberdeck after an Electronics (3) test
to wire it in, and holds the 150 Mp Metavirus master file with its safeguards inoperative. Model as
a single unguarded datastore, not a host. The 20 Mp chip in Beta 7 (Data File One) is a file.

**3. Aztechnology Seattle Pyramid main system** -- 38+ security levels, Level 30 Black IC test bed;
explicitly "NO ONE has ever done it and lived." Do not build for this adventure; keep as the
legendary ceiling of the Seattle Matrix (already noted on the Aztechnology org and Pyramid location).

**4. Biogene's backup-site hit** -- offscreen; a hidden Biogene agent wipes Aztechnology's backup
copies during the run. Nothing to build.

## Flavor / not built

- **Dr. Perkins** (Tiger-Sapiens variant), the infected troll, technicians and Ork guards, Wolf/Tiger/Bear Sapiens, giant cockroaches, flesh worms, millipedes -- creature stat blocks (pp.21-25), kept in the Research Park notes.
- **Lt. Carl Hollis** (Strum's second) -- folded into Strum's notes. **The elite bodyguards and attack dogs** in Alpha -- archetypes.
- **Dr. William Espinata, Emilio K. (Weapons), Juan Atzcapotzalco, Salvador Ramierez** -- leadership entries on Aztechnology, not NPC rows.
- **Governor Allenson (2039), the liner Asian Princess, the United Corporation Council** -- Night of Rage history, in the org notes.
- **Elyse Sunberg** (Seattle Corporate Council spokesperson), **Detective Lucas Niles** (Lone Star), **Ehran the Scribe**, **Dick Steubens** (Seahawks GM), **Nat "Hercules" Brandy / Ann Ransom** -- news-handout names; Niles is on the Lone Star notes.
- **Tanner** (Shalene's mentor, L.A.), **Sisters Sinister** (Frost's old gang), the traitor's kidnapped loved one, the Hands of Five monorail Mr. Johnson and his two hired samurai, the Seneca Street station -- backstory / one-scene devices.
- **Wharf 114 / S.S. Misha** -- one location row (Tacoma Docks); the ship is not a separate entry.
- **Ronnie Bean** homing device and the **Plastisteel-7 catalyst** -- gear, described in the notes.

## GM play notes

- The traitor subplot is optional and must be set up privately with one player before the session;
  without it, Holmes does all the betraying. Either way the Misha ambush is where the blackmail comes
  out.
- Legwork is nearly impossible: street contacts know nothing (roll and ignore); a corporate contact
  needs Etiquette (Corporate) 8, a science contact Knowledge 9 or Etiquette (Science) 6. Public data
  on the Research Park carries a decker's graffiti.
- Whether the team shoots the Ork children in the warehouse decides Bronston's whole attitude.
  Karma: sample 2, file 1, Owens 2, kidnapped Orks 1, killing Ork children -2.
- Beta Section is a sensory gauntlet, not the climax; keep the party alive for Alpha and the safe house.
- Aftermath: Aztechnology and Alamos want blood for a month or two; Biogene keeps its distance; only the
  lunatic fringe offers work. Then the rep upswing: these are the runners who burned Aztechnology.
- Loose ends: whatever Silver Angel was in the last adventure, the Metavirus is the same kind of
  time bomb; Owens at Biogene (or at Wilhem Park); Peterhoff if he lived; Honnicker if he lived; the
  Sapiens loose in the Tacoma sewers (failure ending news).

