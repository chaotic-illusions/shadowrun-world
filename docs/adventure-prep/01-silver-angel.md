# Silver Angel -- Adventure Prep: NPCs, Locations, Organizations, Matrix Systems

Source: Shadowrun 1e - Silver Angel {FASA7102}.pdf, pp. 3-32. Campaign order #1, in-game 2050 (early).

Everything below is loaded into the campaign DB flagged `is_active: false` and `source_adventure: "Silver Angel"` by `python scripts/adventure_ingest/run.py silver_angel`; flip entries active as the party meets them. Use the **Adventure** filter on the manage pages to see just this set.

## Plot synopsis

Eve Donovan, a once-great Seattle fixer clawing her way back after a near-fatal helicopter crash in
Aztlan, is quietly working for **Ares Macrotechnology**. She assembles the runners at the members-only
club **Matchstick's** (password "Steward") for a datasteal: pull the file codenamed **Silver Angel**
out of the physically isolated Executive System at **Cavilard Research Center**, Mitsuhama's R&D plant
in Bellevue. Pay is 50,000 nuyen each up front, 35,000 on completion, and a 15,000 bonus per head if
nobody notices. The run must go down at exactly 2:00 a.m. on Day 3 -- because half a world away an
Ares commando team is extracting Dr. Denise Parkwood from Mitsuhama's Philippines enclave at the same
minute.

Day 1 is legwork. Two leads matter: **Karen Whisper** (stage name Queen Conchita), a dancer at the sleazy
**Cutting Edge** cabaret whose dead decker boyfriend Neon Fever left her a months-old Cavilard system
map she does not know she has; and **Haruhiko "Blood" Blake**, Cavilard's disgraced ex-security
director, now running a chop-shop crew called the **Blood Brothers** out of the Barrens, who meets the
team at the derelict **Cerebus Warehouse** on the wharf and trades complete maps for a future favor.

**Fuchi Industrial Electronics** wants the file too. Four Fuchi "company men" led by Louis Rodrigo
canvass the bars for Whisper with holo-pix and forged Knight Errant IDs, and a two-person Fuchi team
(mage **Callie Firebird** and decker **White Tiger**) is already inside Cavilard on the night, having
put the Security Center guard under a See-Me-Not spell.

The run itself can go the Flashy Way (bluff the front desk as Applied Security or Russel Overland
inspectors), the Violent Way (assault; guards hit PANICBUTTONS, Mitsuhama mercs arrive by Stallion
helicopter), the Quiet Way (emergency exits, with a decker owning the sensor and camera slave modules)
or the Subtle Way (hijack the Russel Overland Roadhauler and its biohazard barrels). At 2:15 a.m.
Mitsuhama Kyoto learns of the Parkwood snatch and at 2:18 the Emergency Notification Signal puts every
Mitsuhama facility -- and every IC in Cavilard -- on External Alert.

Afterwards Mitsuhama will work out Ares was behind the double extraction, but two teams in the
building buys everyone time to disappear. Queen Conchita's body turns up in the Barrens. What Silver
Angel actually is (a faster optical chip? a mind/machine interface? a mole-hunting fake?) is the GM's
call, and should come back to bite the runners later.

## Timeline

- **Day 1** -- Matchstick's briefing; legwork through contacts (TN 4). Fuchi Guns are asking the same
  questions; contacts mention "others have been asking" on 1+ successes.
- **Day 1-2** -- The Cutting Edge: Karen Whisper, Winslow, and the Fuchi Guns encounter (Silverthorn in
  the alley). Whisper sells the chips (2,500+ nuyen) and vanishes.
- **Day 2, evening** -- Blake's meet at the Cerebus Warehouse, about 24 hours before the run. Fixed time.
- **Day 3, 2:00 a.m.** -- The run. Ares extracts Dr. Parkwood in the Philippines at the same moment.
  Russel Overland's biohazard delivery is also scheduled for 2:00 a.m.
- **2:06** Mitsuhama Chiba HQ hears of the Parkwood extraction. **2:15** decision to issue the ENS.
  **2:18** ENS arrives at Cavilard: all IC +2, guards gear up and sweep room by room.
- **After an External Alert**: five mercs + a wage mage by Hughes WK-2 Stallion in 3D6+5 minutes; eight
  more mercs in two Chrysler-Nissan Patrol-1s 3D6 minutes later; an Applied Security decker in 2D6
  turns and a second 3D6 turns after that.

## NPCs (Persons of Interest)

| Name | Role | Org |
|---|---|---|
| Eve Donovan | Fixer running the Silver Angel job for Ares (alias 'Steward') | independent |
| Haruhiko Blake | 'Blood' -- ex-Cavilard security chief, boss of the Blood Brothers; sells maps for a favor | The Blood Brothers |
| Karen Whisper | 'Queen Conchita', dancer at the Cutting Edge; unknowingly holds Neon Fever's Cavilard map | independent |
| Jack Drury | Cavilard Security Director; ex-UCAS Marine; the man to bluff past or fight | Mitsuhama Computer Technologies |
| Callie Firebird | Fuchi's out-of-town covert mage; already inside Cavilard on the night | Fuchi Industrial Electronics |
| Arthur Farren | 'White Tiger', local decker on Fuchi's team; downloads Silver Angel from inside | Fuchi Industrial Electronics |
| Louis Rodrigo | Fuchi Systems Design staff-gun leading the four 'Fuchi Guns' hunting Whisper | Fuchi Industrial Electronics |
| Silverthorn | Elf hitman; the fourth Fuchi Gun, covering the Cutting Edge back alley | Fuchi Industrial Electronics |
| Shen VanChak | Fuchi company man in Rodrigo's crew | Fuchi Industrial Electronics |
| Vicki Ventura | Street samurai muscle in the Fuchi Guns | Fuchi Industrial Electronics |
| Winslow | Troll bouncer at the Cutting Edge; devoted to Queen Conchita | independent |
| Saint John | Doorman at Matchstick's; ex-street samurai with a photographic memory | independent |
| Alan Corliss | Leader of King's Crimson; owes Eve Donovan an honor-debt | King's Crimson |
| Dr. Denise Parkwood | Mitsuhama cybernetics researcher; extracted by Ares from the Philippines the same night | Mitsuhama Computer Technologies |
| Frank Gazzara | 'Neon Fever' -- decker killed by Aztechnology; left the Cavilard map behind (deceased) | independent |

## Locations

| Name | Type | District | Notes |
|---|---|---|---|
| Cavilard Research Center | research lab | Bellevue | MCT R&D plant in a hill off Route 405; the target. Full three-level map + Matrix map in the book |
| Matchstick's | nightclub | Seattle Center | Members-only basement jazz club near the Needle; Donovan's meeting place (password 'Steward') |
| The Cutting Edge | nightclub | Downtown | Sleazy cabaret where Karen Whisper dances as Queen Conchita; the Fuchi Guns shootout |
| Cerebus Warehouse | warehouse | Waterfront (abandoned wharf district) | Derelict container warehouse on the wharf; Blake's meeting ground, riddled with smuggler passages |
| Blood Brothers Chop Shop | chop shop | Redmond Barrens (exact location hidden) | Blake's hidden high-grade chop shop; parts and cyber for a price, no questions |
| Fuchi Seattle Office Tower | corporate headquarters | Downtown | Home of the local Fuchi Systems Design division; where the Fuchi Guns meant to bring Whisper |

## Organizations (new)

| Name | Type | Tier | Notes |
|---|---|---|---|
| King's Crimson | gang | 2 | Street gang; honor-debt to Eve Donovan; a member's word is good |
| The Blood Brothers | crime syndicate | 2 | Haruhiko Blake's chop-shop crew; feared organ-and-cyber traders |
| Applied Security Concepts | security contractor | 2 | Failing computer/physical security contractor guarding Cavilard; Lone Star buyout looming |
| Russel Overland Transport | corporation | 1 | Trucking contractor for Cavilard; leaky Matrix system; runs the biohazard Roadhauler |
| Seattle Metroplex Guard | government | 3 | Former National Guard; under-equipped emergency peacekeepers answering to the governor |

## Existing organizations updated (sourced appends, nothing overwritten)

- **Mitsuhama Computer Technologies** -- profile; GM notes; leadership: Tamatsu Sakura; enemies: Ares Macrotechnology
- **Ares Macrotechnology** -- profile; GM notes; leadership: Roger Soaring Owl, Guido Cantarelli; enemies: Mitsuhama Computer Technologies
- **Fuchi Industrial Electronics** -- profile; GM notes; leadership: Samantha Villiers; enemies: Mitsuhama Computer Technologies
- **Renraku Computer Systems** -- GM notes
- **Lone Star Security** -- GM notes
- **Aztechnology** -- GM notes
- **Knight Errant Security Services** -- GM notes

## Existing locations / NPCs updated

- location: **The Space Needle**

## Matrix systems -- to build in the Matrix designer (NOT built yet)

**1. Cavilard Research Center main system** -- the adventure's target; the book gives a complete node
map (Silver Angel p.16). SR1 notation: color-rating (Green/Orange/Red-N) then IC. Worth building in full.

| Node | Function | Rating / IC |
|---|---|---|
| SAN-1, SAN-2 | Directory #5206, unlisted | Red-3, Access 5, Blaster 4 |
| SAN-3 | Directory NA/UCAS-SEA-8206, unlisted private line (Blake's secondary data line) | Orange-4 |
| CPU | Central processor | Red-4, Access 4, Trace 4 |
| SPU-1, SPU-10, SPU-11 | Data routing only | Green-3, no IC |
| SPU-2 | Building systems | Orange-3, Access 4 -> SM-1 Heating/AC, SM-2 Power, SM-3 Elevators (Green-3, no IC), SM-4 Airlock controls (Orange-3, Access) |
| SPU-3 | Personnel | Orange-3, Access 4 -> DS-2 Records (Orange-3, Scramble 3), I/OP-2 Terminals (Orange-2, Access 3) |
| SPU-4 | Accounting | Orange-3, Access 3 -> DS-3 Records (Orange-3, Scramble 3), I/OP-3 (Orange-2, Access 3) |
| SPU-5 | Administration | Red-3, Access 4, Blaster 3 -> DS-4 Records (Orange-3, Scramble 4), I/OP-4 (Orange-3, Access 4) |
| SPU-6 | CompuTech | Red-3, Access 3 -> DS-5 Records (Orange-4, Barrier 3), DS-6 Files (Orange-4, Barrier 3, Killer 3), I/OP-5 (Orange-4, Barrier 3) |
| SPU-7 | BioTech | Red-3, Access 3 -> DS-7 Records (Orange-4, Barrier 3), DS-8 Files (Orange-4, Barrier 3, Killer 3), I/OP-6 (Orange-4, Barrier 3) |
| SPU-8 | CyberTech | Red-4, Access 5, Tar Baby 4 -> DS-9 Records (Red-3, Access 5, Blaster 3), DS-10 Files (Red-3, Access 5, Blaster 3), I/OP-7 (Orange-4, Access 5) |
| SPU-9 | Security | Red-4, Access 4, Killer 5 -> DS-11 Records/Files (Orange-4, Access 3), I/OP-8 (Orange-3, Access 3), SM-5 Security Cameras (Orange-3, Access 3), SM-6 Sensors / PANICBUTTONS (Orange-3, Access 3), SM-7 Maglock Control (Orange-3, Access 4), SM-8 Executive Datastore Destruct (Red-2, Barrier 4), SM-9 ID Card Verification (Orange-3, Access 3) |
| SPU-12 | Executive System (isolated; linked only via SM-10 / the Computer Center terminal) | Red-4, Access 5, Trace 5 -> DS-12 Records/Files (Red-2, Barrier 3, Black 3), DS-13 Records/Files (Red-2, Barrier 3, Black 3) **Silver Angel lives here: 80 Mp, Scramble 3**, I/OP-9 Terminal (Orange-4, Barrier 3), SM-10 Main System Connect (Orange-4, Barrier 3) |
| DS-1 | Basic records, nothing of value | Green-3, no IC |
| DS-14, DS-15 | Back-up files and records | Orange-4, Barrier 2 |
| I/OP-1 | Terminal controlling the slave modules | Orange-2 |
| SM-11 | Telephone routing (no effect on data lines) | Orange-3, Barrier 2 |

Play notes for the builder: controlling SM-6 silences the PANICBUTTONS, SM-5 blinds the cameras, SM-9
lets a lurking decker approve forged IDs, SM-11 cuts the guards' phone, SM-8 is the datastore
destruct. On External Alert (any time after 2:18 a.m.) every IC is +2. The book says "no more than
Red-3 or 4" per street rumor and the Black Hole node is gone (but let the rumor stand).

**2. Russel Overland Transport** -- no map. Quick-generate: Orange system, no Red nodes, no node above
Security 4. Paydata: cargo manifest (six low-grade biohazard containers, 2:00 a.m. delivery), vehicle
spec (converted Ares Roadmaster, Pro-Pilot II remote override), crew list (three handlers).

**3. Applied Security Concepts database** -- no map or ratings given; White Tiger cracked it for the
Cavilard guard roster. Build only if the players go for the same trick; a modest Orange host with
personnel records (guard shifts, rosters) fits.

Not worth building: the Executive System terminal link is a physical action, the ID verification is a
slave module on the main system, and Neon Fever's chips are a data file, not a host.

## Flavor / not built

- **Jenny Chimes**, rising simsense starlet seen dining with Damien Knight -- name-drop only (in Ares notes).
- **Toshiro Mitsuhama, Richard Villiers, Damien Knight** -- already on their orgs' leadership lists; not NPC records.
- **Cerebus Shipping** -- defunct former owner of the warehouse; folded into the location.
- **Euro-Products Consortium / the Coruscutra extraction** -- Donovan's past glory, kept as flavor in her background.
- **Mitsuhama Wake Island facility, Philippines enclave, Torreon fusion plant (Aztlan)** -- off-map backstory, noted on the org/NPC records instead.
- **Whisper's friend's convenience store and her apartment** -- unnamed, no clues; not recorded.
- **Cavilard Center Guard, Mitsuhama Combat Team (Merc / Wage Mage), Roadhauler crew, ASC corporate decker** -- generic stat blocks (Silver Angel pp.23, 31); noted on the org records.
- **Contacts chapter archetypes** (Club Owner, Corporate Decker, Corporate Official, Media Producer, Corporate Wage Slave, Metroplex Guardsman, Technician, pp.24-27) -- contact archetypes with quotes and stats, not individuals; candidates for the contact-archetype catalog rather than NPC rows.
- **See-Me-Not spell and the Ares Roadhauler** vehicle stats (p.31) -- recorded in Firebird's and Russel Overland's notes.

## GM play notes

- Legwork is a contact-driven Success Test at TN 4 per topic; the book gives dialogue per success level
  (pp.28-31) for Cavilard general / physical / computer, Applied Security, Renraku, Russel Overland, and
  Eve Donovan herself. Any contact with 3+ years in the shadows can speak to Donovan's history.
- Every contact meeting: a secret Etiquette test for the NPC at TN 4 -- on a success they mention that
  "others have been asking the same questions" (the Fuchi Guns). Salt the day with Perception tests and
  a being-followed vibe.
- The Silver Angel file: 80 Mp, encoded data and formulae, nothing a runner can read. Decide what it is
  and make it come back around. Mitsuhama will eventually deduce Ares; the runners' loose ends are what
  it hunts.
- Loose ends to keep: Blake's mark on the team; Queen Conchita's murder (who did it?); Saint John's
  memory; the Fuchi team surviving with its own copy; Drury's grudge if he was humiliated.

