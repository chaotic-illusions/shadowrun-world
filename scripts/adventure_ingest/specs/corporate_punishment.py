# Corporate Punishment (FASA 7330, 2000, SR3) -- campaign order #34. An anthology of three unlinked
# adventures: DOUBLE TAKE (Seattle / Portland, Tir Tairngire), SECOND EFFORT (Seattle / Salish-Shidhe,
# north of Vancouver), LEGACY (Boston). None of the three share characters, plot or geography with each
# other; this spec covers all three under one ADVENTURE entry per the book's own packaging.
# Dating: the book gives exactly one explicit year anywhere in its text -- Second Effort's plot synopsis
# says Dunkelzahn's will "may never be fully understood or even revealed to the public of 2060" -- so YEAR
# follows that anchor for all three adventures (no adventure gives a season or month). This is also
# consistent with the existing Blood in the Boardroom spec (campaign order #32), whose Wuxing/Yakashima
# corporate timeline runs through 15 Aug 2059 and dovetails cleanly with this book's portrayal of both
# corps a few months later.
# Continuity: Wuxing, Inc. and Yakashima Technologies already exist as orgs (created by
# blood_in_the_boardroom.py), with Wu Lung-Wai and Hiroshi Yakashima as their existing NPC rows --
# updated here, not re-created. Legacy spells the Wuxing chairman "Wu-Lung Wei"; treated as the same
# person as the existing "Wu Lung-Wai" and flagged as a spelling discrepancy on his row. Kenneth
# Brackhaven and Aithne Oakforest already exist as NPCs (super_tuesday.py, celtic_double_cross.py) and are
# updated, not re-created. Double Take's Count Evan Parris introduces himself as the former shadowrunner
# "Blackwing" and the book explicitly invites the GM to treat him as a returning NPC from earlier
# adventures -- "Blackwing" already exists (bottled_demon.py) as an icy, stylish elven assassin with a Tir
# Tairngire diplomatic pass and an identical physical description; updated as the same character rather
# than re-created, with his new identity noted on that row.
# Editing inconsistencies noted in the affected rows: Second Effort gives Marianna Che's Seattle safehouse
# as apartment 319 at 1303 East 18th Street, then later has her Proteus room posted as "Room 236" on the
# offshore facility's staff board -- both numbers are kept, flagged as the book's own inconsistency. Legacy
# never firmly identifies the fire-sheathed "Master" or the astral "Crone"/"Hag" of the chess-game prologue
# framing device (possibly Hualpa and a free spirit, possibly unconnected flavor text); left as unbuilt
# color rather than guessed at. Some OCR is garbled in weapon/attribute blocks throughout (particularly
# Second Effort's Proteus AG Security Mage and the Ghosts' Fire Support specialist); reference the book
# directly for exact dice.
# Source text: docs/Adventures/text/Shadowrun 3e - Corporate Punishment - B&W No Cover [FASA 7330].txt
# (91 pages of content).
# ASCII only (pre-commit hook).

ADVENTURE = "Corporate Punishment"
ORDER = 34
SOURCE = "Corporate Punishment.pdf (FASA 7330), pp. 4-90"
YEAR = "2060"

SYNOPSIS = """
Corporate Punishment collects three unrelated Shadowrun adventures under one theme: corporations
settling scores through the shadows rather than risk their own hands. **Double Take** drops the runners
into the walled, caste-bound city of Portland inside **Tir Tairngire**. **Count Evan Parris**, an elf who
was once the notorious hired killer **Blackwing** before Prince **Aithne Oakforest** pardoned him for
services rendered, has **Telestrian Industries**' black-ops handler **Moire Ferguson** ("**Banshee**," a
burned-out ex-Seattle runner) hire an outside team to hit a **Universal Omnitech** research lab and steal
its magical-gene-mapping data -- research chasing the ten-million-nuyen prize in **Dunkelzahn**'s will for
explaining the origin of the "magic gene." Posing as the "Green Sleeves" gardening crew, the runners
crack the lab, but Banshee's real assignment was always to frame them (and, through them, **Saeder-
Krupp** and its dragon CEO **Lofwyr**) for the break-in, discrediting Lofwyr on Tir Tairngire's ruling
Council of Princes. The runners become fugitives inside a country they cannot legally leave, hunted at
once by Universal Omnitech's own security team, a Saeder-Krupp squad led by Lofwyr's shapeshifting
"expediter" **Scale**, and a Tir Tairngire special-forces unit called **the Ghosts** sent by Oakforest to
silence Banshee once she's outlived her usefulness. Cornered at Banshee's usual haunt, the biker bar **the
Ivanhoe**, the Ghosts try to kill her too, and she throws in with the runners she betrayed. From there the
adventure is wide open: the runners can hand Telestrian's proof of the frame-up to Saeder-Krupp or
Universal Omnitech to buy their way home, sell the stolen data to the highest bidder, or vanish into
Portland's shadows with Dog's smuggling help -- but no ending lets them leave the Tir without new,
powerful enemies.

**Second Effort** is a spy story told in two acts. **Anthony Munson**, a low-level fixer for the fiercely
anti-metahuman **Yakashima Technologies**, hires the runners over an obscenely expensive dinner at the
neutral-turf restaurant **Colucci's** to smuggle a Yakashima mole -- **Marianna Che**, a Yakashima agent
surgically and behaviorally trained to impersonate a real Proteus researcher of the same name -- into
**Proteus AG**'s brand-new, paranoid North American aquasphere facility on the Salish-Shidhe coast north
of Vancouver. Proteus rotates its staff so relentlessly that even its own scientists don't know their next
posting until they physically enter a guarded Schedule Room; the runners' job is to get the double inside
unseen so she can learn where "she" is supposed to be before the Monday reshuffle. The insertion
succeeds, but at the payoff meet the runners learn Munson has gone rogue: seduced days earlier by the
Yakashima operative "**Kat**" at **Angry Jake's** and freshly defected to the archconservative **Kenneth
Brackhaven**'s **Brackhaven Investments**, Munson stole Marianna's file on his way out the door and now
means to sell her to Proteus (or ransom her back to Yakashima) to buy his new employer's favor.
Yakashima's real handler, **Jonathan Copass**, doubles the runners' fee to go back in -- this time against
a facility on full red alert -- extract Marianna, and get her home to Seattle before Munson's Humanis-
recruited hit squad ambushes them at the border and a second team runs her down again at her own
apartment. However it ends, Proteus quietly closes the loop by planting a body -- the real Marianna Che's,
already weeks dead -- burned in a Downtown Seattle alley and calling it a failed extraction.

**Legacy** sends a non-Boston team east into the Hub on a two-week deadline. The dragon **Hualpa**
lent Dunkelzahn's bequest, the untranslated **Elemental Scrolls of Ak'le'ar**, to the **Dunkelzahn
Institute of Magical Research (DIMR)**, which placed them at **MIT&T** for a joint research project with
**Mitsuhama Computer Technologies**' secretive magical black-ops wing, **Unit 13**. **Wuxing, Inc.**'s
chairman wants the Scrolls badly enough to hire an outside team through the freelance fixer **Denise
Pierce** ("Ms. Johnson"), who flies the runners to Boston under flawless false identities to meet Wuxing's
local cutouts, the courier **Huong** and the Chinatown fixer **Mr. Lee**. Getting into the heavily warded
**Dunkelzahn Magical Research Building** is the easy part; the Scrolls carry hidden tracking devices, and
within minutes of the theft seven different factions -- MIT&T, MCT's Unit 13, the DIMR, MCT's yakuza
muscle, the Triads working for Wuxing, Wuxing's own wujen, and the Boston fixer-legend **Mama** --
are all hunting the runners and the Scrolls through ritual sorcery and street muscle at once. Cornered in
a running three-way firefight, the runners are pulled out by Mama's agent **Scartage** and taken
blindfolded to her lair in an abandoned subway tunnel, where she offers to broker a clean handoff to
whichever faction they choose -- DIMR, MCT, or Wuxing -- in exchange for one look at the Scrolls and an
unspecified favor owed. Whoever gets them, the Scrolls themselves are strange rather than dangerous:
sturdy beyond reason, undated by any test, and prone to calling curious elemental spirits out of the
ether, including two old and immensely powerful ones -- a free air spirit and a bound fire elemental --
that will fight to the death for the Scrolls' safety if anyone actually tries to destroy them.
"""

TIMELINE = """
Double Take (Portland, Tir Tairngire; no date given beyond "the year is roughly Corporate Punishment's
2060"):
- **Day 0** -- Count Parris briefs Banshee at Telestrian's Portland offices; Banshee hires the runners at
  **Matchstick's** in Seattle.
- **Day 1-2** -- flight to Portland, customs, the Rose Branch Inn; gear (and an already-doctored map)
  delivered Friday night by the Portland fixers **Eddy and Zach**.
- **Saturday** -- the "Green Sleeves" gardening-crew infiltration of Universal Omnitech's Faloma district lab
  (Flower and Fire); data stolen, lab wrecked, an escape under fire if the alarm trips.
- **Saturday evening** -- payoff at Pioneer Courthouse Square; Banshee vanishes into the Telestrian
  Habitat; that night TTBC News breaks the runners' mugshots as "Saeder-Krupp operatives."
- **The following days** -- the runners go to ground; Universal Omnitech, Saeder-Krupp's Scale, and the
  Tir Ghosts all hunt them; Banshee is ambushed at the Ivanhoe and joins the runners; open-ended
  resolution with DIMR-- er, with Saeder-Krupp, Telestrian, Universal Omnitech, or independence.

Second Effort (Seattle / Salish-Shidhe coast; one week):
- **Four days before the meet** -- the prologue: "Kat" seduces Anthony Munson at Angry Jake's.
- **Friday** -- Munson (as "Mr. Johnson") hires the runners at Colucci's; they meet the Marianna Che double
  at her ransacked Seattle safehouse apartment and recon the Proteus facility that night or the next.
- **Sunday night into Monday** -- the insertion (The Dropoff); Marianna reaches the Schedule Room and
  cuts the runners loose.
- **Thursday** -- Munson has himself extracted to Brackhaven Investments, taking Marianna's file.
- **Friday** -- Jonathan Copass reveals the betrayal and doubles the runners' pay to extract Marianna.
- **That weekend** -- a second break-in against a red-alert Proteus facility finds it evacuated to Seattle;
  Munson's Humanis-recruited hit squad ambushes the runners at the border on the way back; a final
  extraction from Marianna's apartment building, a three-way chase to Colucci's, and payoff.

Legacy (Boston; two-week window):
- **Day 0** -- Denise Pierce hires the runners in a Redmond junkyard meet (Handshakes); flight to Boston
  the next day.
- **Day 1-2 in Boston** -- Huong delivers the target package; Mr. Lee supplies smuggled gear; legwork on
  MIT&T and the Dunkelzahn Magical Research Building.
- **Within the twelve-day window** -- Getting In (recon) and Getting Out (the theft of the five Scrolls from
  their warded display case).
- **Within minutes to hours of the theft** -- AOD trackers activate; seven factions begin ritual tracking and
  street searches (Swiftly and Brutally Pursued).
- **Same night** -- the runners' hideout is besieged by multiple warring factions at once; Mama's agent
  Scartage extracts them (A Rock and a Hard Place); Mama lays out the endgame options and brokers
  delivery to whichever faction the runners choose (Delivery); the Scrolls change hands and the runners,
  now owing Mama a favor, get out of Boston.
"""

ORGS = [
    {
        "name": "Telestrian Industries",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Telestrian Habitat, Portland, Tir Tairngire",
        "summary": "Tir Tairngire corp fronting a Council of Princes power play: hires shadowrunners to steal Universal Omnitech's magic-gene research and frames Saeder-Krupp for it",
        "description": (
            "A Tir Tairngire corporation with deep family ties to Prince Aithne Oakforest, who owns a "
            "significant stake and has 'the authority and motivation to operate through the corp.' On the "
            "surface Telestrian pursues its own genetic-research programs; underneath, Oakforest uses it "
            "as deniable cover for black operations against his rival on the Council of Princes, the dragon "
            "Lofwyr of Saeder-Krupp. All corporate business in Tir Tairngire is by law five percent "
            "government-owned, which suits Oakforest's arrangement perfectly."
        ),
        "leadership": [
            {"name": "Aithne Oakforest", "title": "Prince, Tir Tairngire (unofficial patron)", "notes": "Directs the frame-up through Count Parris; does not appear as a Telestrian employee of record."},
        ],
        "notes": (
            "Double Take: orders the Universal Omnitech datasteal via its handler Moire Ferguson "
            "('Banshee'), plants forged evidence naming the runners 'known Saeder-Krupp operatives,' then "
            "moves to silence Banshee (and the runners) once the frame lands, using a borrowed unit of Tir "
            "Ghosts. The Telestrian Habitat arcology in Portland is its Tir headquarters and Banshee's base. "
            "If exposed, Telestrian will retract its media story rather than let the blackmail stand, but "
            "hunts down anyone who pushes it too hard."
        ),
        "enemies": ["Saeder-Krupp Heavy Industries", "Universal Omnitech"],
    },
    {
        "name": "Universal Omnitech",
        "org_type": "corporation (biotechnology)",
        "tier": 3,
        "headquarters": "Faloma district, Portland, Tir Tairngire",
        "summary": "Biotech corp whose Portland R&D lab -- close to explaining the 'magus factor' -- gets robbed and wrecked, then used as the excuse to smear Saeder-Krupp",
        "description": (
            "An aggressive biotech acquirer that received 120 million nuyen from Dunkelzahn's will and has "
            "since bought up smaller gene-mapping firms across the Pacific Prosperity Group, chasing the "
            "ten-million-nuyen bounty the will offers for explaining the genetic basis of magical ability. Its "
            "Portland facility -- three stand-alone buildings behind a sculpted hedge, only one of them "
            "actually in use -- houses the lab that made the breakthrough Telestrian wants."
        ),
        "notes": (
            "Double Take: standard weekend security is a bored gatehouse guard, two floor patrols, an "
            "on-call (unmanned) security rigger, and a Force 6 bound water elemental; a six-member "
            "response team (one hermetic security mage, five samurai) plus a five-samurai-and-a-physical-"
            "adept second wave from a neighboring building respond to any alarm within a few Combat "
            "Turns. Its Matrix host is decked as an undersea castle (fish for data, sharks for IC, deckers as "
            "mermaids). After the theft, Universal Omnitech believes the leaked evidence naming Saeder-"
            "Krupp and pursues the corp through the Corporate Court with real teeth, sending its own street "
            "team (equal to the lab's own security guards) after the runners in parallel with Saeder-Krupp "
            "and the Ghosts. Will trade captured runners' freedom for Banshee's identity, but still turns them "
            "over to the Tir military tribunal afterward."
        ),
        "enemies": ["Saeder-Krupp Heavy Industries", "Telestrian Industries"],
    },
    {
        "name": "The Ghosts",
        "org_type": "special forces unit (Tir Tairngire)",
        "tier": 4,
        "headquarters": "Tir Tairngire (on loan to Prince Aithne Oakforest for Double Take)",
        "summary": "Elite Tir Tairngire black-ops squad on loan to Prince Oakforest; ordered to hunt the runners and, once she's outlived her use, assassinate Telestrian's own handler Banshee",
        "description": (
            "Tir Tairngire's secret special-forces unit for counter-insurgency, hostage rescue and deniable "
            "black ops, run on two loyalties only: the Tir and each other. Well-trained, highly intelligent and "
            "frighteningly efficient, they are the country's answer to a shadowrunner problem, and they "
            "favor shadowrunner teams as training targets. Count Evan Parris hand-picked the unit assigned "
            "to Double Take, using Prince Oakforest's personal authority."
        ),
        "notes": (
            "Double Take: a six-person unit (Sergeant/unit leader, Fire Support and Demolitions Specialist, "
            "two Tactical Support Specialists, a Small Arms Specialist, a Magical Support Specialist), all "
            "elves, Grade 3-4 adepts and initiates, in Medium Security Armor with ruthenium-coated coats. "
            "Ordered to keep Banshee under surveillance and kill her once the runners are dealt with; a "
            "second squad hunts the runners directly, tracking them by the blood samples taken at customs "
            "via ritual sorcery if street methods fail. Ambushes Banshee at the Ivanhoe once she tries to meet "
            "the runners, forcing her to fight alongside the team she was sent to betray. Has home-field "
            "advantage over every other faction hunting the runners in Portland."
        ),
        "allies": ["Telestrian Industries"],
    },
    {
        "name": "Proteus AG",
        "org_type": "corporation (bioware / genetics)",
        "tier": 4,
        "headquarters": "Germany; North American facility on the Salish-Shidhe coast, ~70 km north of Vancouver",
        "summary": "Ultra-paranoid German AA bioware corp that builds offshore 'aquasphere' arkoblocks and rotates staff so obsessively that even its own scientists don't know next week's posting",
        "description": (
            "A mystery corporation that grew to AA stature 'right in Saeder-Krupp's backyard' by building "
            "arkoblocks -- offshore underwater arcologies -- for Japanese corporations; it has completed "
            "nine worldwide (five North Sea, two off Japan, one in the South Pacific near Fiji, one off South "
            "America, and its newest off Salish-Shidhe). It entered Dunkelzahn's aquasphere-prize "
            "competition and lost on a technicality -- its spheres sit above sea level rather than fully "
            "submerged. Its own staff rotate teams and postings on a whim; no employee learns a new "
            "assignment except by physically entering a Schedule Room fed a single-use burn chip over a "
            "satellite uplink isolated from the Matrix. Eco-groups consider Proteus target number one for "
            "toxic dumping and mass sealife kills, and are in open, unresolved 'warfare' with it."
        ),
        "notes": (
            "Second Effort: North American land facility is a black polished-glass box (Barrier 8) behind a "
            "monowire fence, glare-trap lighting, ultrasonic jammers and cameras, two pop-up sentry "
            "turrets, and a rotating four-guard perimeter patrol; a tram tunnel (Barrier 24) connects it to the "
            "offshore aquasphere ~1 km out, itself defended by Assault Cannons, anti-vehicle missile racks, "
            "a VTOL gunship, patrol boats and multiple water/air elementals, with ~50 security staff and its "
            "own Matrix deckers rated Superior/Professional. Onshore Matrix is Red-7 (ACIFS "
            "14/13/14/12/14), offshore Red-9 (13/13/16/18/15), sculpted as an aquarium with shark IC. "
            "Yakashima's mole Marianna Che is inserted here to learn her cover identity's real work "
            "assignment; when the facility later goes to red alert it evacuates all non-security staff to a "
            "Seattle apartment complex rather than risk them. Proteus quietly closes out the Marianna Che "
            "affair by planting the real (already dead) Marianna's body, burned, in a Seattle alley."
        ),
        "enemies": ["Yakashima Technologies"],
    },
    {
        "name": "Brackhaven Investments",
        "org_type": "corporation (investment firm)",
        "tier": 2,
        "headquarters": "Seattle",
        "summary": "Kenneth Brackhaven's openly anti-metahuman investment firm; recruits defecting corporate suits (and Humanis Policlub muscle) as freelance Johnsons and enforcers",
        "description": (
            "The investment firm of Kenneth Brackhaven, who nearly won the UCAS presidency on an "
            "archconservative, anti-metahuman platform before Dunkelzahn spoiled it. Brackhaven has since "
            "grown rich funding companies that quietly (or not so quietly) share his politics, and has become "
            "one of Seattle's wealthiest and best-known individuals by softening his public stance without "
            "changing his private one. Because open bigotry makes it hard to staff a corporation, Brackhaven "
            "tricks and poaches disgruntled suits from rival corps into 'creating their own extractions' -- "
            "hiring shadowrunners to check up on dissatisfied executives and nudge them toward defecting."
        ),
        "notes": (
            "Second Effort: recruits Anthony Munson away from Yakashima mid-adventure after 'Kat' softens "
            "him up at Angry Jake's; Munson steals Marianna Che's file on the way out to curry favor with his "
            "new employer. Brackhaven's muscle is pulled from the ranks of the Humanis Policlub -- an "
            "ambush squad (sniper, Raven-totem shaman, six thugs, three vehicle riggers) hits the runners at "
            "the Salish-Shidhe border once Munson learns they've extracted Marianna, and Munson himself "
            "leads a second attempt at her Seattle apartment building. Brackhaven Investments never "
            "appears directly; Munson is its only on-page representative."
        ),
        "allies": ["Humanis Policlub"],
        "enemies": ["Yakashima Technologies"],
    },
    {
        "name": "Boston Triads",
        "org_type": "criminal syndicate (Triad alliance)",
        "tier": 2,
        "headquarters": "Chinatown, Boston",
        "summary": "The Yellow Lotus and the Mutual Prosperity League, Boston's two rival Triad houses, holding an unprecedented truce brokered by Wuxing to serve the corp's Legacy heist",
        "description": (
            "Boston's underworld belongs to the Mafia; the Triads are localized entirely to Chinatown and a "
            "few Wuxing-controlled blocks, running BTL, prostitution and gambling there and nowhere else "
            "by long-standing mutual restraint with the Families. The city's two houses, the Yellow Lotus and "
            "the Mutual Prosperity League, have fought each other for years -- until recently, when street "
            "rumor notices League muscle guarding a Yellow Lotus opium shipment. Word on the street "
            "places the truce squarely at the feet of Wuxing, Inc., which wanted a unified, discreet local arm "
            "for its Legacy operation."
        ),
        "notes": (
            "Legacy: acts as Wuxing's Boston cutout, fronted publicly by the fixer Mr. Lee, who arms the "
            "runners and later hunts them (using DNA samples lifted from their hotel room) once the Scrolls "
            "are stolen. Generic operative block: B5 Q5 S5 C3 I3 W4, Threat 2/3; Clubs 4, Edged Weapons 4, "
            "Pistol 4, Unarmed Combat 5; Ares Predator, sap, knife, Armored Vest with Plates [4/3]. Yakuza "
            "muscle (MCT's, hunting on the other side of the same theft) uses the same statline with swapped "
            "knowledge skills. Chinatown residents treat Triad members as folk heroes and will not give them "
            "up to police or outsiders."
        ),
        "allies": ["Wuxing, Inc."],
    },
    {
        "name": "Mitsuhama Unit 13",
        "org_type": "corporate black-ops magical research division",
        "tier": 4,
        "headquarters": "Mitsuhama Computer Technologies North American HQ (Boston area)",
        "summary": "MCT's secretive magical research and security wing, run in Legacy by the mage-agents Shotozumi and Karonage under a local commander known only as 'Sensei'",
        "description": (
            "A shadowy corner of Mitsuhama Computer Technologies devoted to magical research and "
            "black operations, so secretive that 'no one would be able to point out a member if they saw one "
            "on the street.' Very few outside MCT have seen Unit 13 operate, and fewer still have lived to "
            "talk about it; the Legacy heist puts them more visibly in the field than the street rumor mill has "
            "ever seen them."
        ),
        "notes": (
            "Legacy: co-funds and staffs the MIT&T/DIMR study of the Elemental Scrolls of Ak'le'ar alongside "
            "the university and the Dunkelzahn Institute of Magical Research; provides four guards, a "
            "security mage (Jason Winters) and, once the Scrolls are stolen, leads the pursuit through two "
            "initiate field agents, Shotozumi and Karonage, both Grade 3, backed by a large pool of trained "
            "MCT security operatives. Each pursuing squad is led by one of the two mages; if both are killed, "
            "the local commander 'Sensei' -- a Grade 5 initiate with a great-form elemental of every type on "
            "call -- takes the field personally and hunts without mercy. Runs its own hidden ritual-sorcery lab "
            "in the Boston area, using a scrap of the Scrolls for tracking."
        ),
        "allies": ["Mitsuhama Computer Technologies", "Dunkelzahn Institute of Magical Research"],
    },
    {
        "name": "Dunkelzahn Institute of Magical Research",
        "org_type": "magical research institute",
        "tier": 3,
        "headquarters": "Western Cambridge, Boston, off the Fresh Pond Parkway",
        "summary": "The dragon Dunkelzahn's premier magical-research foundation; holds the Elemental Scrolls of Ak'le'ar on loan from Hualpa and partners with MIT&T and MCT's Unit 13 to study them",
        "description": (
            "Established by Dunkelzahn's will, the DIMR has become the world's foremost cutting-edge "
            "magical research body, with access to many of the world's most powerful magical items and "
            "sorcerers and the clout to make corporations, universities and even the Atlantean Foundation "
            "cooperate under one roof. The dragon Hualpa entrusted it with the Elemental Scrolls of Ak'le'ar, "
            "and the DIMR arranged for a two-week joint study at MIT&T's Thaumaturgy department with "
            "Mitsuhama's Unit 13 as co-funder and second security provider."
        ),
        "notes": (
            "Legacy: keeps DIMR security shaman Daniel Gammemnos on-site at the MIT&T research "
            "building; begins its own ritual-sorcery search for the stolen Scrolls within ten minutes of "
            "discovering the theft, using a retained scrap of Scroll material. Not the most dangerous of the "
            "seven pursuing factions -- 'not as tough as the special operative that the Draco Foundation "
            "uses' -- but treats returned Scrolls warmly, paying the runners and asking (without threat) who "
            "hired them originally. May call on the Draco Foundation's own shadowops team, Assets Inc., if "
            "the GM wants a harder edge. Loses the Scrolls to theft on this book's watch, which the DIMR "
            "understandably would rather not have publicized."
        ),
        "allies": ["Mitsuhama Unit 13"],
    },
]

LOCATIONS = [
    {
        "name": "Universal Omnitech Portland Facility",
        "location_type": "corporate facility",
        "district": "Faloma district",
        "city": "Portland",
        "security_level": "Corporate Standard",
        "controlling_org": "Universal Omnitech",
        "summary": "Six-story tiered biotech R&D building north of downtown Portland, hit by the Green Sleeves gardening-crew datasteal in Double Take",
        "description": (
            "One of three stand-alone office buildings Universal Omnitech owns on a hedge-ringed lot in "
            "Faloma, only the largest of which it actually uses (the rest are rented out to small local "
            "businesses). The main building steps back like a pyramid every two floors, with rooftop "
            "gardens over floors Three and Five, four ground-floor entrances including two single-vehicle "
            "docking garages, two main elevators, a service elevator and two stairwells. The fifth floor -- "
            "the runners' target -- holds a corridor of glass-walled gardens, cubicle offices, the lab "
            "director's and assistant director's offices, and the Research and Development lab itself, with a "
            "separate unlabeled closet housing the lab's off-Matrix datastore hardware."
        ),
        "notes": (
            "Barrier Rating 12 plascrete vehicle barrier under the perimeter hedge; camera-equipped "
            "lampposts every 10 m. Weekend staffing is thin and the gatehouse guard barely checks the "
            "Green Sleeves cover story. Fifth-floor doors (director's/assistant director's offices, the lab, the "
            "datastore closet) run Rating 4-5 maglocks; a single Force 6 bound water elemental patrols "
            "astrally. On alarm, a six-person response team (mage + five samurai) arrives within a few "
            "Combat Turns and a five-samurai-plus-adept second wave from a neighboring building follows "
            "about two minutes later. The datastore module can be physically unplugged and carried off in "
            "place of a Matrix download."
        ),
    },
    {
        "name": "Pioneer Courthouse Square",
        "location_type": "landmark / monument",
        "district": "Downtown",
        "city": "Portland",
        "security_level": "Patrolled / Commercial",
        "summary": "Full-city-block downtown Portland plaza where Banshee pays off the runners after the Universal Omnitech run -- and where the frame-up news breaks that same night",
        "description": (
            "A gorgeous, full-block park ringed by free-standing Greek pillars on one side and a waterfall "
            "and amphitheater steps on the other, surrounded by shopping centers, corporate offices and "
            "government buildings. Elven couples stroll it on pleasant evenings, making it an easy place for "
            "a nervous meeting to look unremarkable."
        ),
        "notes": (
            "Double Take: Banshee waits on the amphitheater steps near the waterfall, pays the runners "
            "and takes the stolen data, then leaves quickly, distancing herself before triggering the "
            "'anonymous tip' that frames them as Saeder-Krupp operatives. She keeps two Force 5 air "
            "elementals on call and two elven snipers posted on nearby rooftops covering her exit; if the "
            "runners follow her, she checks for a tail before driving to a parking garage and on to the "
            "Telestrian Habitat."
        ),
    },
    {
        "name": "Rose Branch Inn",
        "location_type": "hotel",
        "district": "Downtown",
        "city": "Portland",
        "security_level": "Patrolled / Commercial",
        "summary": "Downtown Portland hotel where the runners wait out their gear delivery before the Universal Omnitech run, uneasily aware of Tir Tairngire's caste hierarchy in the bellhops' attitude",
        "description": (
            "A well-appointed downtown hotel that puts the runners squarely in 'elf territory' for the first "
            "time -- check-in is fast, the rooms comfortable, but the staff's deference clearly correlates with "
            "the caste of the guest, and outsiders like the runners rate accordingly. The runners spend a day "
            "and a half here waiting for Banshee's people to deliver their gear."
        ),
        "notes": "Double Take: Eddy and Zach deliver the team's cyberdeck, weapons, armor and the Green Sleeves cover gear here late Friday night, along with a business card and an offer of local fixer services.",
    },
    {
        "name": "The Ivanhoe",
        "location_type": "bar",
        "district": "Portland shadows (turf not given)",
        "city": "Portland",
        "security_level": "Low Security",
        "summary": "Dingy biker bar and motel that is Dog's main hangout and Banshee's favorite watering hole -- the site of the Tir Ghosts' assassination attempt on her in Peek-a-Boo",
        "description": (
            "One of the dingiest motels the runners have seen: a back parking lot full of parked "
            "motorcycles, a tough crowd of gangers and bikers partying outside, and a troll bouncer at the "
            "rear entrance to the bar itself. Banshee drinks here to drown her guilt after setting the runners "
            "up, on good terms with a number of the crime boss Dog's people; Dog treats it as his personal "
            "turf and headquarters."
        ),
        "notes": (
            "Double Take: the Tir Ghosts stake out the Ivanhoe waiting for Banshee to appear, a laser-sighted "
            "shot to her forehead is the ambush's opening tell; four Ghosts attack here (two more may be "
            "hunting the runners elsewhere), using ruthenium-coated stealth to close for melee while a "
            "sniper/mage pair holds cover on nearby rooftops or behind parked vehicles. Bikers dive for "
            "cover but will fight any Ghost they can actually see. Dog can arrange a guarded meeting with "
            "Banshee in one of the Ivanhoe's warded rooms if approached correctly."
        ),
    },
    {
        "name": "Telestrian Habitat",
        "location_type": "corporate arcology",
        "district": "Portland",
        "city": "Portland",
        "security_level": "Corporate High Security",
        "controlling_org": "Telestrian Industries",
        "summary": "Telestrian Industries' Portland arcology headquarters; Banshee's base, the stolen data's resting place, and Count Parris's likely location if the runners go after him",
        "description": (
            "Telestrian Industries' corporate arcology in Portland, where Banshee drops off the stolen "
            "Universal Omnitech data with her superiors and keeps her personal office. Security is alert but "
            "not paranoid toward staff moving normally; Banshee, using her own access codes and intimate "
            "knowledge of the layout, can walk visitors through with minimal attention as long as they aren't "
            "obviously armed or acting suspicious."
        ),
        "notes": (
            "Double Take: if the runners and Banshee break in together within an hour or two of the Ghost "
            "ambush, they can retrieve her personal operation files from her office and the stolen datastore "
            "unit from the tech lab (a clerk there initially refuses to release it -- 'not authorized' -- forcing "
            "improvisation). Count Evan Parris may be present and is a plausible secondary extraction "
            "target. Security response escalates fast once any alarm trips inside the arcology."
        ),
    },
    {
        "name": "Proteus AG North American Facility",
        "location_type": "corporate facility",
        "district": "Salish-Shidhe coast, ~70 km north of Vancouver",
        "city": "Vancouver",
        "security_level": "Corporate High Security",
        "controlling_org": "Proteus AG",
        "summary": "Black, polished-glass onshore facility and its connected offshore aquasphere -- the Second Effort insertion and extraction target, twice broken into by the same team",
        "description": (
            "A four-meter-tall building of black, highly polished, highly reflective armored glass (Barrier 8) "
            "hidden in a forest clearing off an unmarked exit, nearly invisible at night and blinding in direct "
            "sun. A two-meter chain-link-and-monowire fence with buried high-intensity light boxes rings "
            "the site; a jammer pole and four ultrasonic-capable cameras cover the grounds, and two pop-up "
            "sentry turrets with Ultimax MMGs watch the north and south corridors. Inside: a lobby built "
            "purely for show, a security office, a Chemical Defense room with HAZMAT gear and spray "
            "weapons, executive offices that look unused because they are, and -- one level underground, "
            "unmapped -- the Schedule Room's computer, key to the whole plot. A second underground "
            "level houses the tram station connecting to the offshore aquasphere roughly a kilometer out to "
            "sea, itself a multi-level undersea complex of labs, staff housing and executive quarters guarded "
            "by dozens of security personnel, elementals, Assault Cannons and patrol boats."
        ),
        "notes": (
            "Second Effort: standard patrol is a four-guard rotation on a predictable ~30-minute gap; a "
            "Force 6 water elemental sits offshore and a Force 6 barrier wards Room 2 (the security office). "
            "After the runners' first break-in trips the alarm, Proteus evacuates all non-security staff "
            "(including Marianna) to Seattle, doubles guards, adds great-form water and air spirits, and "
            "clears a wider tree line -- the runners' second infiltration finds the whole site an empty, heavily "
            "upgraded shell. The offshore aquasphere is reachable by the tram tunnel (Barrier 24, 5-minute "
            "ride) or, far more dangerously, by sea or air against Assault Cannons, anti-vehicle missiles, a "
            "VTOL gunship and patrol boats. Onshore Matrix Red-7 (14/13/14/12/14); offshore Red-9 "
            "(13/13/16/18/15), sculpted as an aquarium with shark IC."
        ),
    },
    {
        "name": "Colucci's",
        "location_type": "restaurant",
        "district": "Downtown",
        "security_level": "Patrolled / Commercial",
        "summary": "Neutral-turf Italian restaurant where Anthony Munson hires the runners over an outrageously expensive dinner, and where Jonathan Copass pays them off after the extraction",
        "description": (
            "An Italian restaurant lined with red leather booths, dark-suited made men and underdressed "
            "joygirls, its front door guarded by a Rating 8 MAD scanner and the hostess's massive doorman "
            "'Tiny.' No weapons are allowed past the door -- they're checked with Tiny and returned on the "
            "way out -- and despite the clientele, Colucci's is explicitly independent, not run by any crime "
            "family; the handshake agreement to keep it neutral ground is honored by every major syndicate "
            "in the city. The hostess is a Grade-1 physical adept initiate working security."
        ),
        "notes": (
            "Second Effort: site of both the initial hire (Anthony Munson as 'Mr. Johnson,' offering "
            "200,000 nuyen for the Proteus insertion) and the Friday follow-up meet where his real boss, "
            "Jonathan Copass, reveals Munson's defection and doubles the fee for Marianna's extraction. "
            "Final payoff after the extraction also happens here; Copass can arrive within half an hour of a "
            "call and Colucci's neutral-ground reputation is enough to make pursuing Lone Star and Proteus "
            "units back off rather than start a fight on the premises."
        ),
    },
    {
        "name": "Angry Jake's",
        "location_type": "nightclub",
        "district": "Seattle (district not given)",
        "security_level": "Patrolled / Commercial",
        "summary": "Seattle club where the Yakashima operative 'Kat' seduces and begins compromising Anthony Munson in the prologue vignette that sets up his mid-adventure betrayal",
        "description": (
            "An ordinary Seattle club with a troll bouncer wanding patrons for weapons at the door -- Kat "
            "hands over a Fichetti Needler on the way in -- and a bar where the 'beautiful people' watch and "
            "are watched. Nothing distinguishes it on the page beyond being the stage for Kat's careful, "
            "pheromone-assisted seduction of Anthony Munson."
        ),
        "notes": "Second Effort: single-scene setting for the First Impressions prologue; not revisited elsewhere in the text.",
    },
    {
        "name": "Marianna Che's Apartment (1303 East 18th Street)",
        "location_type": "apartment complex",
        "district": "Downtown Seattle",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "Proteus AG",
        "summary": "Posh, anonymously-owned Seattle apartment building where Yakashima's Marianna Che double preps for and later hides out from her insertion -- secretly leased by Proteus for its North American staff",
        "description": (
            "An unexpectedly luxurious building for a shadowrun meet: a keypad-and-camera lobby with no "
            "visible egress but a single elevator, plush carpeted hallways with real-wood doors and gold "
            "numerals, and a synthesized voice that walks visitors to their floor. Apartment 319, on the "
            "third floor, is the Marianna double's cover residence -- in disarray both times the runners visit, "
            "as she frantically searches for things the real Marianna would know like the back of her hand. "
            "The building's true owner is impossible to trace publicly; it is in fact leased anonymously by "
            "Proteus AG for its North American employees, with the lease nearly up now that the Salish-"
            "Shidhe facility is running."
        ),
        "notes": (
            "Second Effort: site of the runners' first meeting with Marianna (The Package) and, days later, "
            "the tense final extraction (Extraction Done Easy) once Proteus staff flood back into the building "
            "for new assignments and Munson's people close in. Marianna's own record posts her assigned "
            "Proteus quarters as 'Room 236' on the offshore staff board -- a different number than her "
            "Seattle apartment 319, and the book never reconciles the two; both are kept here as the book's "
            "own inconsistency."
        ),
    },
    {
        "name": "Dunkelzahn Magical Research Building",
        "location_type": "research lab",
        "district": "MIT&T campus, Cambridge",
        "city": "Boston",
        "security_level": "Corporate Standard",
        "summary": "Three-story ivy-covered MIT&T research building holding the Elemental Scrolls of Ak'le'ar in a warded display case -- the Legacy heist's target, tenanted by half a dozen megacorps and a dragon-topped statue out front",
        "description": (
            "A three-story brick building with ivy-covered walls, external wrought-iron fire escapes and a "
            "statue of Dunkelzahn out front, standing out sharply from the rest of campus. Corridors run 2 m "
            "wide with 3-4 m ceilings; the building houses corporate research offices for MCT, "
            "Aztechnology, Yamatetsu, Renraku, Saeder-Krupp, the Atlantean Foundation, Manadyne, Knight "
            "Errant, Novatech and Mass General Hospital alongside DIMR offices, a hermetic library, "
            "graduate-student and faculty offices, classrooms/lecture hall, and giant third-floor 'Circle Labs' "
            "for ritual work. The building's entire exterior carries a Rating 4 Polarized Ward (opaque from "
            "outside); many individual labs and offices carry their own alarm wards (Force 4-6). The Scroll "
            "Lab itself, unlabeled and unmarked, holds the five Scrolls in a locked glass display case behind "
            "a Rating 7 alarm ward and a Force 12 masking ward (Force 8 to pierce)."
        ),
        "notes": (
            "Legacy: two MIT&T guards plus regular campus patrol, four MCT guards and a security mage "
            "(Jason Winters), and the DIMR's own security shaman (Daniel Gammemnos) rotate coverage; "
            "guardian vines (Force 3) grow on the walls and Force 3 watchers patrol the halls. Layered Matrix "
            "access: public campus net (Blue-6/6/8/6/8/8), campus PLTG (Green-8/9/8/6/9/9+), campus "
            "security net (Orange-8/11/10/7/12/12, with a secret DIMR-MCT backdoor), and the Scroll Lab's "
            "own isolated computers (Orange-7/10/10/8/9/8). The five Scrolls each carry a hidden Rating 5 "
            "AOD tracker (staggered activation, unknown to MIT&T security) that begins broadcasting within "
            "five minutes of the theft unless all five are found and disabled."
        ),
    },
    {
        "name": "Mama's Sanctuary",
        "location_type": "underground bunker",
        "district": "Abandoned subway tunnels/catacombs beneath Boston",
        "city": "Boston",
        "security_level": "No Security / Barrens",
        "summary": "Mama's hidden lair deep in Boston's abandoned subway system, reached blindfolded, where the fixer-legend shelters the runners and brokers the Scrolls' final delivery",
        "description": (
            "A large, square room deep within a maze of abandoned subway tunnels and old catacombs "
            "beneath Boston, reachable only through a disorienting blindfolded walk of many minutes -- the "
            "runners never learn its exact location. Mama receives visitors here from a soft chair she rises "
            "from only with effort, leaning on a thick walking stick, surrounded by a constant traffic of "
            "retainers reporting in and receiving new assignments."
        ),
        "notes": (
            "Legacy: cell phones and GPS are dead here except through Mama's own private repeater "
            "network; if the lights go out, a character could be dead within a minute. Mama's people will die "
            "to protect her and intercept any direct threat instantly. This is where she lays out the runners' "
            "five options for the stolen Scrolls (return them, deliver to Wuxing, keep them, give them to a "
            "trusted third party, or sell to the highest bidder) and later brokers the actual handoff meet, "
            "though she is never present at the exchange itself -- only one of her people watches from a "
            "distance."
        ),
    },
]

NPCS = [
    {
        "name": "Banshee",
        "role": "Moire Ferguson, ex-Seattle shadowrunner turned Telestrian Industries black-ops handler; hires the runners to hit Universal Omnitech, then frames them for it -- and becomes a fugitive herself",
        "archetype": "Corporate Fixer",
        "title": "Corporate handler, Telestrian Industries; former Seattle shadowrunner ('Banshee')",
        "race": "Elf",
        "gender": "Female",
        "age": 26,
        "organization": "Telestrian Industries",
        "connection": 4,
        "description": (
            "Twenty-six years old, blue-black hair in a short straight bob, dark blue eyes, fair "
            "complexion, somewhat aloof with a sad air but tough enough that few try to run roughshod "
            "over her. Presents as 'Ms. Johnson' -- a fluid British accent, snug synthleather and a "
            "sleeveless zippered vest that clash deliberately with her polished manner -- to hide her Telestrian "
            "affiliation from the runners she hires."
        ),
        "background": (
            "Born Moire Ferguson in Native American country; orphaned at fifteen the same day her magical "
            "abilities manifested, she fled into the shadows with an elf friend named Molly and resurfaced "
            "in Seattle five years later, running the shadows there as 'Banshee' until Molly was murdered. "
            "Grief-stricken, she fled to Tir Tairngire drawn by its promise of elven freedom from prejudice, "
            "only to find the same bigotry dressed up differently. Telestrian Industries recruited her "
            "aggressively, fast-tracked her to Grade 3 initiate, and slowly buried her under bureaucratic "
            "betrayals of runner teams she has come to despise doing."
        ),
        "notes": (
            "Full SR3 mage stats: B4 Q6 S3 C6 I6 W6 E6 M6 R9; Sorcery 6, Conjuring 5, Aura Reading 5; "
            "spells include Manabolt 6, Mind Probe 5, Fireball 5, Powerball 4; Grade 3 initiate (Centering, "
            "Masking, Reflecting). Hires the runners at Matchstick's for 100,000-110,000 nuyen to hit "
            "Universal Omnitech, then frames them (and Saeder-Krupp) for the theft on Telestrian's orders. "
            "Her own superiors, wary of her growing disillusionment, secretly order the Tir Ghosts to "
            "assassinate her once the runners are dealt with; ambushed with them at the Ivanhoe, she joins "
            "forces with the team she betrayed and can guide them into the Telestrian Habitat using her own "
            "access codes."
        ),
        "contact_skills": ["Tir Tairngire corporate and government circles", "Portland shadow-community back channels"],
    },
    {
        "name": "Count Evan Parris",
        "role": "Prince Aithne Oakforest's black-ops handler and Banshee's controller -- formerly the world-famous assassin and shadowrunner 'Blackwing,' pardoned into Tir nobility",
        "archetype": "Fixer",
        "title": "Count, Tir Tairngire; black-operations coordinator for Prince Aithne Oakforest",
        "race": "Elf",
        "gender": "Male",
        "organization": "Tir Tairngire",
        "connection": 6,
        "description": (
            "Husband, father, and scholar by his new public face: the essence of style and grace, calm and "
            "collected no matter the situation, fearing little, including death. A private man who never "
            "speaks of his past, though he retains the flash of his younger, deadlier days and loathes every "
            "dracoform and anyone who serves one."
        ),
        "background": (
            "Ten years before Double Take, Parris was the world-famous assassin and shadowrunner "
            "Blackwing, backed by a Tir royal patron; when he failed to secure an important magical relic for "
            "that patron, the Council of Princes sentenced him to death for treason. He fled into the shadows "
            "and sold his services to the highest bidder until, through quick action and incredible luck, he "
            "placed the far more powerful Prince Aithne Oakforest in his debt. Oakforest overturned the "
            "death sentence, and Blackwing rebuilt himself as Count Evan Parris, leaving the old name behind."
        ),
        "notes": (
            "No fixed statistics; treat as Superhuman -- a cold killer unsurpassed with firearms, delta-grade "
            "cyberware including Wired Reflexes 3 and two synthetic cyberarms, not Awakened. Directs "
            "Banshee's Double Take frame-up on Oakforest's authority and hand-picks the Ghost unit sent "
            "after Banshee and the runners; may be present in the Telestrian Habitat and is a plausible "
            "secondary extraction target if the runners go after Telestrian directly. Corporate Punishment: "
            "'the player characters may have met Count Parris as Blackwing in previous adventures' -- this "
            "row updates the existing Blackwing NPC rather than duplicating him; see that row for his "
            "earlier appearance and identical physical description."
        ),
        "contact_skills": ["Unrestricted access to Tir Tairngire's higher circles"],
    },
    {
        "name": "Eddy and Zach",
        "role": "Inseparable ork brothers, Portland's freelance shadow couriers and fixers -- deliver the runners' gear, offer tour-guide services, and can lead the runners to Dog and Banshee",
        "archetype": "Fixer",
        "title": "Freelance couriers and fixers, Portland",
        "race": "Ork",
        "gender": "Male",
        "connection": 2,
        "description": (
            "Similar in size and stature but easy to tell apart: Eddy is noticeably scruffier and does "
            "nearly all the talking, even for questions directed at Zach; Zach is unnaturally quiet but always "
            "first to start a task, often half-finished before Eddy stops negotiating the fee. Bound by intense "
            "mutual loyalty -- either will viciously attack anyone who threatens the other."
        ),
        "background": (
            "Grew up together on Portland's streets, recognized early that Tir society's caste system left "
            "orks no room to rise, and turned to the shadows for better odds. Careful never to tie themselves "
            "too closely to any one power base or patron, they take almost any job that pays and doesn't "
            "make lasting enemies -- hired for Double Take through the troll crime boss Dog, an old friend of "
            "Banshee's, without either brother knowing who they really work for."
        ),
        "notes": (
            "Combined stats (one block covers both): B6 Q5 S(-) C(-) I(-) W(-), Athletics 3, Bike 3, Car 3, "
            "Computer 5, Demolitions 4, Intimidation 3, Negotiation 4, Pistols 4, Unarmed Combat 6; "
            "Remington Roomsweeper, Armor Jacket [5/3]; Karma Pool/Professional Rating 3/3. Deliver the "
            "team's cyberdeck, weapons, armor and Green Sleeves cover gear at the Rose Branch Inn; offer "
            "info-brokering (20 percent markup) and Portland tour-guide services; recognize Banshee's photo "
            "from the Ivanhoe bar but not her name. Will not join a run directly but take peripheral tasks "
            "(scouting, spotting, diversions); if hired to find Banshee, get a call from Dog almost immediately."
        ),
        "contact_skills": ["Portland fixers and shadowspots", "Underworld politics, Tir corporations and Tir politics"],
    },
    {
        "name": "Dog",
        "role": "Aging troll crime boss and ex-go-gang leader who runs one of Portland's two big independent underworld operations -- an old friend of Banshee's who can smuggle the runners out of the Tir",
        "archetype": "Crime Boss",
        "title": "Independent crime boss, Portland",
        "race": "Troll",
        "gender": "Male",
        "connection": 3,
        "description": (
            "A vicious fragger by reputation who used to lead one of Portland's more infamous go-gangs "
            "before building an independent criminal operation to rival the city's other major player, the "
            "dwarf Kate 'the Kat' Mustaffah. Keeps the fireworks between them minimal by mutual, unspoken "
            "agreement rather than any real friendship."
        ),
        "background": (
            "Rose from Portland go-gang leadership to running an underworld operation big enough to "
            "compete with Mustaffah's docks-and-BTL trade, without the elf manpower or subtlety that keeps "
            "the major syndicates out of Portland entirely. Hired the couriers Eddy and Zach to deliver the "
            "runners' Double Take gear without telling them who they really worked for, and has been Banshee's "
            "friend since her own days running the shadows."
        ),
        "notes": (
            "Double Take: hangout and headquarters is the Ivanhoe biker bar/motel. Sends polite but "
            "forceful ork armbreakers to bring the runners in for a talk if they start asking questions about "
            "Banshee around Portland; can arrange a guarded meeting between them and Banshee in a "
            "warded Ivanhoe room. Once Banshee is compromised and sides with the runners, he can arrange "
            "smuggling out of the Tir -- for a price, and a riskier crossing the less the runners can pay."
        ),
        "contact_skills": ["Portland underworld, smuggling routes out of Tir Tairngire"],
    },
    {
        "name": "Kate \"the Kat\" Mustaffah",
        "role": "Dwarf ex-European-arms-trader who runs Portland's strongest independent criminal operation -- Dog's rival, controlling the docks and most of the city's BTL trade",
        "archetype": "Crime Boss",
        "title": "Independent crime boss, Portland",
        "race": "Dwarf",
        "gender": "Female",
        "nationality": "European",
        "connection": 3,
        "description": "A dwarf with a background in the European arms trade who built the strongest independent criminal operation in Portland, with direct control over the docks and the bulk of the city's BTL trade -- Dog's biggest and only serious competitor.",
        "notes": "Double Take: name-drop as Portland's other major crime figure in the city-briefing material; never appears on-page directly, but the runners are likely to hear of her while working Dog's turf.",
    },
    {
        "name": "Scale",
        "role": "Lofwyr's mysterious shapeshifting 'expediter,' sent to find out who framed Saeder-Krupp for Double Take -- and to make the runners pay off a personal debt to the dragon for it",
        "archetype": "Fixer",
        "title": "Personal expediter to Lofwyr, Saeder-Krupp Heavy Industries",
        "race": "Unknown",
        "gender": "Unknown",
        "organization": "Saeder-Krupp Heavy Industries",
        "connection": 5,
        "description": (
            "An entity of uncertain nature -- some say an ally spirit, others a lesser dragon, others "
            "something else entirely -- who appears to the runners as a slick, composed figure whose "
            "masking cannot be pierced by any means the runners are likely to bring. Portrays himself as a "
            "simple emissary sent to learn what Lofwyr needs to know and to 'request' suitable reparations "
            "for the insult of being framed."
        ),
        "notes": (
            "Double Take: takes orders directly from Lofwyr and should be feared on that basis alone; his "
            "hand-picked team includes at least one initiate and two top-tier cyber/bio specialists (build all as "
            "Superior, treat Scale himself as Ultimate). Leads Saeder-Krupp's Portland pursuit squad, "
            "avoiding a fight where possible but forcing the runners to surrender at a disadvantage rather "
            "than killing them outright; releases captured runners on condition they deliver Banshee, the "
            "stolen data and proof of Telestrian's plot, and personally makes sure they understand the debt "
            "they now owe Lofwyr for their lives. May intervene against the Ghosts at the Ivanhoe if the "
            "runners are losing badly, then extract them to a Saeder-Krupp warehouse for a personal audience."
        ),
        "contact_skills": ["Direct line to Lofwyr's household"],
    },
    {
        "name": "Anthony Munson",
        "role": "Yakashima Technologies fixer who hires the runners as 'Mr. Johnson' to insert a spy into Proteus AG -- then defects to Brackhaven Investments mid-job and turns hunter",
        "archetype": "Corporate Fixer",
        "title": "Corporate fixer, Yakashima Technologies (later: Brackhaven Investments)",
        "race": "Human",
        "gender": "Male",
        "age": 30,
        "organization": "Yakashima Technologies",
        "connection": 3,
        "description": (
            "Four hundred pounds and just under six feet, brown hair in a crewcut going gray at the "
            "temples, a fondness for Vashon Island suits worn with the jacket off and suspenders showing. A "
            "Mafioso wannabe rather than a made man -- his taste for rich Italian food and occasional dealings "
            "with the Family let him hold business meetings at Colucci's without actually belonging to it."
        ),
        "background": (
            "A shrewd negotiator passed over for promotion at Yakashima once the corp brought in an "
            "outsider to 'professionalize the Johnsons,' Munson devised the Marianna Che insertion into "
            "Proteus AG as his ticket up -- then, four days after hiring the runners, let himself be seduced "
            "and turned by the operative 'Kat' at Angry Jake's. He defects to Kenneth Brackhaven's "
            "Brackhaven Investments on the strength of stolen files on Marianna, meaning to sell or ransom "
            "her for his new employer's favor."
        ),
        "notes": (
            "Full stats: B5 Q2 S5 C4 I6 W4 E5.8; Etiquette (Corporate 8, Mafia 7), Negotiation 6, Pistol 4; "
            "Walther Palm Pistol, Fine Armored Clothing [3/0], datajack. Hires the runners at Colucci's for "
            "200,000 nuyen (negotiable to 250,000) to insert Marianna into Proteus; after his defection, sets "
            "a Humanis-recruited ambush at the Salish-Shidhe border (sniper, shaman, six thugs, three riggers) "
            "and personally leads a second confrontation at Marianna's Seattle apartment building. If he dies, "
            "Jonathan Copass is relieved but Marianna still needs pulling out, since Munson may already have "
            "shared her file with Brackhaven's people."
        ),
        "contact_skills": ["Yakashima corporate hiring channels"],
    },
    {
        "name": "Marianna Che",
        "role": "Yakashima Technologies mole trained for months to become a real Proteus AG researcher, inserted to learn her cover identity's next assignment -- and later extracted when Munson's betrayal exposes her",
        "archetype": "Corporate Spy",
        "title": "Undercover operative, Yakashima Technologies (posing as a Proteus AG researcher)",
        "race": "Human",
        "gender": "Female",
        "nationality": "Chinese-European",
        "organization": "Yakashima Technologies",
        "connection": 2,
        "description": (
            "Matches the real Marianna Che's Chinese-European looks, but wears her hair short and "
            "dyed blond, slicked back and tucked behind her ears, with a datajack gleaming at one temple. "
            "Trained so thoroughly in her cover that she has genuinely begun to believe she is Marianna, "
            "which shows in her frustration hunting for 'her own' things in an apartment she should know "
            "cold -- and in her occasional slips back into shadowrunner instincts."
        ),
        "background": (
            "The ultimate mole: trained for months to lie, cheat and steal while projecting total loyalty, "
            "loyal only to Yakashima. Because Proteus rotates its staff constantly and even its own scientists "
            "don't know next week's posting, she is inserted mid-transfer -- before even the real Marianna "
            "learned her own new assignment -- leaving her needing to reach the facility's Schedule Room "
            "before Monday's reshuffle or blow her own cover."
        ),
        "notes": (
            "Full stats: B4 Q5 S3 C5 I7(9) W5 E21; Biotech 5, Computer 5, Stealth 8, Negotiation 4 (Fast "
            "Talk 8); Browning Max-Power with silencer and laser sight, Cerebral Booster 2, Encephalon 2, "
            "Wired Reflexes 1. Reaches the Schedule Room successfully and learns her cover posting ('Salish "
            "Facility 236'); when Munson's betrayal endangers her, the runners must extract her twice -- once "
            "from an evacuated, red-alert Proteus facility (she's actually been shipped to a Seattle apartment "
            "complex) and once from that same apartment building as security closes in. Becomes a Level 2 "
            "contact if the runners get her out alive; Proteus publicly closes the loop afterward with the real "
            "Marianna's already-weeks-dead body, burned in a Seattle alley."
        ),
        "contact_skills": ["Proteus AG internal operations (as long as her cover holds)"],
    },
    {
        "name": "Jonathan Copass",
        "role": "Anthony Munson's actual Yakashima superior -- reveals Munson's betrayal at the Friday payoff and doubles the runners' fee to extract Marianna Che before Munson can sell her out",
        "archetype": "Corporate Fixer",
        "title": "Johnson manager, Yakashima Technologies",
        "race": "Human",
        "gender": "Male",
        "connection": 4,
        "description": (
            "A six-and-a-half-foot-tall African American man with black hair and purple cybereyes, "
            "dressed in a black Armante suit and patent leather shoes -- a level of corporate polish the "
            "runners don't usually see face to face. Uncomfortable dealing with shadowrunners directly (that's "
            "normally Munson's job), he doesn't lie to them, just visibly dislikes having to come down to "
            "their level."
        ),
        "background": (
            "Imported from the East Coast to 'professionalize the Johnsons' at Yakashima, a promotion that "
            "cost Anthony Munson his own shot at the role and pushed him toward defection. Now Copass "
            "has to clean up his subordinate's mess personally or take the blame for it himself."
        ),
        "notes": (
            "Full stats: B4 Q4 S3 C6 I5 W4 E3.2; Etiquette (Corporate 5), Negotiation 4, Leadership 3, "
            "Pistols 1; Fechetti Security 500a, Armored suit [3/0], cybereyes with camera/retinal clock and "
            "headware memory recorder. Pays the runners for the successful insertion (five black credsticks), "
            "then reveals Munson's defection to Brackhaven Investments and offers double pay (up to "
            "400,000 nuyen, free bioware, and the Ford Bison) to extract Marianna. Will point runners toward "
            "killing Munson as a loose end if the negotiation sours; offers corp protection or Yakashima "
            "employment to runners who succeed."
        ),
        "contact_skills": ["Yakashima Johnson-management circles"],
    },
    {
        "name": "Kat",
        "role": "Yakashima operative who seduces and begins turning Anthony Munson in a single honeytrap scene, setting up his later defection to Brackhaven Investments",
        "archetype": "Corporate Spy",
        "title": "Undercover operative (alias 'Jana'), Yakashima Technologies",
        "race": "Human",
        "gender": "Female",
        "nationality": "American (Southern accent)",
        "organization": "Yakashima Technologies",
        "connection": 1,
        "description": (
            "Works a room in a short Armante dress and tailored pheromones, staging a spilled-drink "
            "meet-cute with practiced precision; drops her cover voice-modulator once out of earshot to "
            "reveal a soft, natural Southern drawl. Carries a chemical breath-analyzer and a palm recorder "
            "disguised as ordinary accessories."
        ),
        "background": "Introduces herself to Anthony Munson as 'Jana' at Angry Jake's and works him for several minutes of practiced small talk and pheromone-assisted flirtation before reporting success to her handler by phone -- the opening move in compromising Munson days before he defects to Brackhaven Investments.",
        "notes": "Second Effort: appears only in the First Impressions prologue vignette; no combat stats given. Her exact role -- freelance honeytrap for hire, or a Yakashima loyalty test/compromise operation run against its own fixer -- is left ambiguous by the book; treat as the latter given how directly her work feeds Munson's later defection.",
        "contact_skills": ["Honeytrap tradecraft"],
    },
    {
        "name": "Denise Pierce",
        "role": "Freelance fixer working as 'Ms. Johnson' for Wuxing, Inc. -- hires the runners in a Redmond junkyard meet to steal the Elemental Scrolls of Ak'le'ar from MIT&T, sight unseen",
        "archetype": "Fixer",
        "title": "Freelance fixer (alias 'Ms. Johnson')",
        "race": "Human",
        "gender": "Female",
        "connection": 4,
        "description": (
            "A professional through and through: composed, efficient, plays a British-accented "
            "'Ms. Johnson' persona over her own voice, and completes the entire hiring meet -- terms, "
            "advance, false identities, travel arrangements -- inside a single sitting in an abandoned Redmond "
            "warehouse without wasted words."
        ),
        "background": (
            "Hired by Wuxing to find a Seattle team professional, discreet and very good -- reputation-vetted "
            "before the meet even happens. Knows almost nothing about the actual job beyond its two-week "
            "window, its unspecified magical target, and that the Boston contact is Triad-connected; she "
            "deliberately isn't told who the item's owner is or that a dragon is involved."
        ),
        "notes": (
            "Full stats: B3 Q4 S3 C5 I5 W5 E5.8; Etiquette 6, Negotiation 6, Pistol 4; Fichetti Security 500, "
            "Fine Armored Clothing [3/0], datajack, image-linked cybereyes. Offers 150,000-200,000 nuyen "
            "(5,000/runner advance, negotiable to 10,000), first-class flights, Hotel Edmonton reservations, "
            "flawless false identities, and an unstated 1,000,000-nuyen equipment budget the runners never "
            "learn about. Backed at the meet by her dwarf mage bodyguard Donald Blake and driver Jeremy "
            "Spence. Will not negotiate a bidding war once the runners are ready to deliver the Scrolls."
        ),
        "contact_skills": ["Pacific Rim fixer network", "Wuxing intermediary channels"],
    },
    {
        "name": "Donald Blake",
        "role": "Denise Pierce's dwarf mage bodyguard, hidden and ready at the Handshakes meet with a fire and earth elemental on call",
        "archetype": "Bodyguard",
        "title": "Bodyguard/mage, retained by Denise Pierce",
        "race": "Dwarf",
        "gender": "Male",
        "connection": 1,
        "description": "Waits out of sight during Denise Pierce's meet with the runners, ready to act only if she's threatened; keeps a fire and an earth elemental on call and treats both as protectors rather than combatants unless the meeting turns violent.",
        "notes": (
            "Full stats: B5 Q5 S5 C5 I5 W7 E6; Conjuring 6, Sorcery 6, SMG 5; HK-227, Armored Jacket "
            "[5/3]; Earth Elemental (Force 5, Services 3), Fire Elemental (Force 4, Services 2); Grade 2 "
            "initiate (Centering, Shielding). Legacy: never appears again after Handshakes; if the meet turns "
            "violent, a fire elemental could ignite a gas line in the meeting building's basement."
        ),
    },
    {
        "name": "Jeremy Spence",
        "role": "Denise Pierce's human driver, waiting outside the Handshakes meet",
        "archetype": "Bodyguard",
        "title": "Driver/bodyguard, retained by Denise Pierce",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": "Stays with the car outside the meeting building unless called in or he hears gunfire; a competent, unremarkable professional driver-bodyguard.",
        "notes": "Full stats: B4 Q4 S4 C3 I4 W3; Car 5, Etiquette 3, Pistol 4; Ares Predator, Fine Armored Clothing [3/0]. Legacy: never appears again after Handshakes.",
    },
    {
        "name": "Huong",
        "role": "Wuxing's Boston courier -- delivers the campus map, security briefing and false ID cards for the Legacy heist, and knows deliberately little about the job itself",
        "archetype": "Fixer",
        "title": "Courier and messenger, Wuxing, Inc. (Boston)",
        "race": "Asian (nationality not specified)",
        "gender": "Male",
        "connection": 1,
        "description": (
            "A well-built man with long black hair pulled into a ponytail, dressed in a loose white shirt "
            "over dark pants, carrying a single large briefcase. Waits patiently at the runners' hotel door and "
            "makes a point of knowing as little as possible about the business of his fellow citizens in the "
            "shadows."
        ),
        "background": "A courier and messenger with wide but arm's-length contacts across Boston's shadow community; killing him would annoy several people for no gain, since he genuinely carries no information worth extracting by force.",
        "notes": (
            "Legacy: average-human-plus stats (Intelligence and Charisma +1), Athletics 3, Unarmed Combat "
            "5, Etiquette (Street) 2(4), Boston Area 5, Underworld (Triads) 2(4), Street Rumormill 5, "
            "semi-trained professional rating; unarmed. Delivers the MIT&T campus map and floor plan, a "
            "security summary, a physical description of 'the Scrolls of the Elements' (the cover name; true "
            "name Ak'le'ar withheld), contact numbers, a city guide, and forged MIT&T ID cards."
        ),
        "contact_skills": ["Wide arm's-length contacts across Boston's shadow community"],
    },
    {
        "name": "Mr. Lee",
        "role": "Wuxing's Chinatown fixer and Triad-connected gear supplier for Legacy -- later leads the Triad search for the runners once the Scrolls are stolen, using DNA lifted from their hotel room",
        "archetype": "Fixer",
        "title": "Fixer and procurer, Boston Chinatown",
        "race": "Human",
        "gender": "Male",
        "nationality": "Chinese",
        "connection": 4,
        "description": (
            "Elegant and unhurried, in a sharp white suit with a colored shirt and dark sunglasses, hair "
            "short and black, his clothing and shoes both clearly expensive. Meets the runners in a "
            "spotlessly clean alley behind two of his men, an ork bodyguard standing silently nearby."
        ),
        "background": (
            "A fixer and procurer of many talents with deep, semi-open Triad connections that street rumor "
            "can never quite confirm outright -- 'works for himself and the highest bidder,' with solid ties to "
            "a certain megacorp based out of Hong Kong. Supplies the runners' Legacy gear in two black "
            "cases and later, once the Scrolls go missing, has his staff quietly lift DNA samples from the "
            "runners' hotel room to hunt them down for Wuxing."
        ),
        "notes": (
            "Full stats: B3 Q4 S3 C5 I6 W6 E4.8; Negotiation 6, Intimidation 5, Interrogation 4, Pistol 5, "
            "Unarmed Combat 5; Knife [5M], Armored Clothing [3/0], cybereyes (Image Link, Low-Light, "
            "Opticam), datajack. Ork bodyguard: B8(12) Q5 S7 C2 I5 W4, Browning Max-Power, Combat "
            "Knife, Armored Jacket [6/4], Titanium Bone Lacing, Wired Reflexes 2. Begins the Triad search for "
            "the runners only once they call Ms. Johnson; congratulates the team afterward if they deliver the "
            "Scrolls to Wuxing, returns their stolen DNA samples as a goodwill gesture, and offers transport "
            "home."
        ),
        "contact_skills": ["Boston Triads (Yellow Lotus and Mutual Prosperity League)", "Chinatown gear and information"],
    },
    {
        "name": "Mama",
        "role": "Boston's enigmatic, legendary information broker and fixer of fixers -- extracts the runners from a multi-faction firefight and brokers the Elemental Scrolls' final delivery in exchange for a look at them and a favor owed",
        "archetype": "Fixer",
        "title": "Information broker and fixer, Boston (identity and true nature unconfirmed)",
        "race": "Unknown",
        "gender": "Female",
        "connection": 6,
        "description": (
            "Physically unimposing -- less than average height, far less than healthy weight, seemingly "
            "made of skin and bones, face withered and ancient, eyes speaking from shallow dark pits. "
            "Speaks softly, clears her throat often, and cackles at moments calculated to unnerve. An astral "
            "look finds no magical pattern and no known metahuman aura signature at all; her eyes, looked "
            "into directly, seem to stare back from an abyss."
        ),
        "background": (
            "Street rumor makes her everything from a thousand-year vampire to a magician's spirit too "
            "ornery to stay in the grave; she confirms none of it. What is certain is her reach -- retainers "
            "constantly moving through her abandoned-subway domain reporting and receiving assignments, "
            "and information on nearly everything and everyone in the Hub, whether she wants it known or not."
        ),
        "notes": (
            "No combat stats given; treat as untouchable in her own domain. Legacy: her agent Scartage "
            "extracts the runners from a multi-faction firefight around their hideout and brings them "
            "blindfolded to her sanctuary; she disarms the Scrolls' AOD trackers, lays out five options for "
            "their disposition (return to DIMR/MIT&T/MCT, deliver to Wuxing, keep them, give to a trusted "
            "third party, or sell to the highest bidder -- warning that the Triads work for Wuxing and the "
            "Yakuza work for MCT, so two of any 'highest bidders' are already-hostile factions), and later "
            "brokers the actual handoff without attending it herself. Her price: first look at the Scrolls and an "
            "unspecified future favor, collected months later."
        ),
        "contact_skills": ["Everything and everyone in the Hub"],
    },
    {
        "name": "Scartage",
        "role": "Mama's grubby, unarmed dwarf agent who finds the runners first during the multi-faction firefight and leads them to Mama's sanctuary -- twin brother of her bodyguard Stinger",
        "archetype": "Fixer",
        "title": "Street agent, working for Mama",
        "race": "Dwarf",
        "gender": "Male",
        "connection": 1,
        "description": "A dirty, homeless-looking dwarf who appears out of nowhere in the middle of a firefight, hands visibly empty, and calmly offers the only way out: 'Yo, chummers -- if you wanna live, follow me.' Convincing and honest in manner, unarmed and mundane.",
        "background": "One of Mama's many street-level agents; identical in appearance to her bodyguard Stinger, though the two are never in the same place at once.",
        "notes": "Legacy: uses generic average-dwarf critter stats, no weapons or special gear. If the runners kill or refuse him, another (interchangeable) agent takes his place; killing several in a row earns Mama's genuine anger.",
    },
    {
        "name": "Stinger",
        "role": "Mama's chief bodyguard in Legacy -- a dangerous, heavily cybered professional and twin brother of her street agent Scartage",
        "archetype": "Bodyguard",
        "title": "Chief bodyguard, retained by Mama",
        "race": "Dwarf",
        "gender": "Male",
        "connection": 2,
        "description": (
            "Years running in the big leagues bought Stinger cutting-edge cybernetics that have left him "
            "colder and more callous than most, and considerably more dangerous -- a trade he made "
            "willingly. A stalwart professional to have on your side and a genuinely dangerous man to have "
            "against you."
        ),
        "notes": (
            "Full stats: B5(7) Q6 S7(9) C3 I6 W5 E0.02; Pistols 6, SMG 6 (Ingram Smartgun 7), Unarmed "
            "Combat 4, Stealth 6; paired Ingram Smartguns (silenced), Ares Predator (silenced), retractable "
            "cyber spurs, Wired Reflexes 2, two obvious cyberarms with built-in smartlink and Strength "
            "Enhancement 3. Legacy: guards Mama's sanctuary; identical to his twin Scartage in appearance "
            "but the two never appear together."
        ),
    },
    {
        "name": "Daniel Gammemnos",
        "role": "DIMR security shaman posted to the MIT&T research building -- part of the Legacy building's day-to-day defense and one of seven factions hunting the runners once the Scrolls are stolen",
        "archetype": "Security Mage",
        "title": "Security shaman, Dunkelzahn Institute of Magical Research",
        "race": "Human",
        "gender": "Male",
        "organization": "Dunkelzahn Institute of Magical Research",
        "connection": 2,
        "description": "A Fire-bringer totem shaman who carries a golden phoenix pendant as his spirit focus and a bundle of self-grown olive leaves as an expendable focus, sharing rotating shifts with MCT's security mage Jason Winters and swapping notes on any astral events between them.",
        "background": "Stationed by the DIMR as one of the research building's two on-duty security magicians for the duration of the Elemental Scrolls' study period.",
        "notes": (
            "Full stats: B4 Q5 S4 C5 I6 W6 E6 M8; Sorcery 7, Conjuring 6; Fire-bringer totem (+2 detection/"
            "manipulation and spirits of man, -1 illusion); spells include Bind 6, Detect Enemies 6, Flamethrower "
            "5, Powerball 5; Grade 2 initiate (Centering, Shielding); Beretta 101T, Armored Jacket [5/3]. "
            "Legacy: begins his own ritual-sorcery search using a scrap of the Scrolls within ten minutes of "
            "discovering the theft, alongside MIT&T's own researchers."
        ),
    },
    {
        "name": "Jason Winters",
        "role": "MCT security mage stationed at the MIT&T research building -- reviews astral activity in shift-overlap with DIMR's Daniel Gammemnos and joins the Legacy pursuit once the Scrolls are stolen",
        "archetype": "Security Mage",
        "title": "Security mage, Mitsuhama Computer Technologies",
        "race": "Human",
        "gender": "Male",
        "organization": "Mitsuhama Computer Technologies",
        "connection": 2,
        "description": "Carries a silver bracelet as his sustaining focus and a quartz crystal pendant as an expendable focus; keeps two watcher spirits on patrol that report back to him directly if they spot trouble or an obvious stranger near the research building.",
        "notes": (
            "Full stats: B3 Q5 S4 C4 I5 W6 E6 M6; Sorcery 6, Conjuring 6; spells include Bind 6, Improved "
            "Invisibility 5, Physical Mask 4, Powerbolt 5, Stunball 5; elementals of each element (Force 4, "
            "Services 2) on call; HK-227-S, Beretta 101T, Armored Jacket [5/3]. Legacy: one of MCT's two "
            "on-site security mages guarding the Scroll research; joins the pursuit once the theft is "
            "discovered."
        ),
    },
    {
        "name": "Shotozumi",
        "role": "Militant field mage of MCT's black-ops Unit 13, leading a Legacy pursuit squad against the runners in preference to any wheeling-and-dealing",
        "archetype": "Corporate Mage",
        "title": "Field agent/mage, Mitsuhama Unit 13",
        "race": "Human",
        "gender": "Female",
        "organization": "Mitsuhama Unit 13",
        "connection": 3,
        "description": "A slight but physically powerful Japanese woman in a standard security uniform marked only by a silver ring, her anchored spell focus; the more militant of Unit 13's two field agents, preferring the straightforward strike to her partner Karonage's political maneuvering.",
        "notes": (
            "Full stats: B5 Q4 S5 C4 I5 W6 E5.04 M8; Sorcery 7, Conjuring 5, Centering (Kata) 6; spells "
            "include Lightning Bolt 6, Manabolt 6, Powerball 5; Grade 3 initiate (Anchoring, Centering, "
            "Shielding); Ceska Black Scorpion, Combat Knife, Armored Jacket [5/3]. Legacy: if she and "
            "Karonage are both killed and the runners are found again, Unit 13's local leader 'Sensei' -- a "
            "Grade 5 initiate with a great-form elemental of every type on call -- takes the field personally."
        ),
    },
    {
        "name": "Karonage",
        "role": "Manipulative, politically-minded field mage of MCT's black-ops Unit 13, running a Legacy pursuit squad in parallel with the more militant Shotozumi",
        "archetype": "Corporate Mage",
        "title": "Field agent/mage, Mitsuhama Unit 13",
        "race": "Elf",
        "gender": "Male",
        "nationality": "Mediterranean",
        "organization": "Mitsuhama Unit 13",
        "connection": 3,
        "description": "Tall and thin, frail-featured with long fingers, manipulative and conniving; treats subordinates with exactly the respect they've earned and not an iota more, playing favorites who live in relative luxury against those who earn the worst assignments and walk the razor's edge of his whims.",
        "notes": (
            "Full stats: B3 Q6 S2 C7 I6 W6 E5.2 M8; Sorcery 6, Conjuring 7, Centering (Zazen) 6; spells "
            "include Bind 6, Fireball 5, Mind Probe 5, Influence 5; Grade 3 initiate (Anchoring, Centering, "
            "Shielding); Beretta 101T, Combat Knife, Armored Jacket [5/3]. Legacy: leads one of Unit 13's two "
            "field pursuit squads alongside Shotozumi; if he and Shotozumi both fall, 'Sensei' takes over the "
            "hunt directly."
        ),
    },
    {
        "name": "Sensei",
        "role": "Unit 13's mysterious local Boston commander, a Grade 5 initiate who joins the Legacy hunt personally and without mercy if both his field mages are killed",
        "archetype": "Corporate Mage",
        "title": "Local commander, Mitsuhama Unit 13 (Boston)",
        "race": "Human",
        "gender": "Male",
        "organization": "Mitsuhama Unit 13",
        "connection": 4,
        "description": "Carries himself like a marine officer, capable of dressing down subordinates as sharply as any drill sergeant; educated, sees himself as a modern samurai, polite and brief with most people but merciless without remorse when the situation calls for it. His own people call him only 'sensei.'",
        "notes": (
            "Full stats: B4 Q5 S5 C5 I6 W6 E5.something M9 (partial OCR); Sorcery 7, Conjuring 8, "
            "Centering (Zazen) 6; spells include Bind 6, Fireball 5, Mind Probe 6, Powerball 5, Shapechange 4; "
            "Grade 5 initiate (Anchoring, Centering, Invoking, Masking, Shielding) with great-form elementals "
            "(Force 5, Services 3) of every type on call. Legacy: only enters the field personally if both "
            "Shotozumi and Karonage are killed and the runners are found again; when he does, he is "
            "'nothing short of ruthless.'"
        ),
    },
]

ORG_UPDATES = {
    "Tir Tairngire": {
        "notes_append": (
            "Corporate Punishment (Double Take): Portland is the country's only border-zone city open to "
            "non-citizens, run under modified martial law by a military tribunal and the well-armed Tir "
            "Peace Force; visitors submit to blood tests and cyberware deactivation at Customs. Rigid caste "
            "structure (gentry/'Squire', chivalry/'Sir', nobles, counts, dukes, then royalty at Royal Hill); "
            "discrimination against non-elves is masked as status rather than stated outright. Foreign-owned "
            "companies cannot operate directly inside the Tir; Aztechnology and Saeder-Krupp are both "
            "specifically banned, the latter because its dragon CEO Lofwyr sits on the Council of Princes -- a "
            "perceived conflict of interest the whole adventure exploits. Prince Aithne Oakforest uses "
            "Telestrian Industries as deniable cover to frame Lofwyr for a Universal Omnitech theft, hiring "
            "outside shadowrunners through his agent Count Evan Parris (formerly the assassin Blackwing) "
            "and Telestrian's handler Banshee, then deploying a borrowed unit of the Tir's elite black-ops "
            "Ghosts to clean up loose ends including Banshee herself."
        ),
    },
    "Saeder-Krupp Heavy Industries": {
        "notes_append": (
            "Corporate Punishment (Double Take): banned outright from operating inside Tir Tairngire "
            "because CEO Lofwyr sits on the Tir Council of Princes -- a standing conflict of interest Prince "
            "Aithne Oakforest exploits by framing Saeder-Krupp for a Universal Omnitech datasteal actually "
            "run by his own agent, Count Evan Parris, through Telestrian Industries. Lofwyr responds by "
            "sending his personal 'expediter,' the mysterious entity Scale, and a hand-picked squad from "
            "Saeder-Krupp Prime to hunt the framed runners in Portland, extract the truth of who set them "
            "up, and collect proof clearing the corp before the Corporate Court."
        ),
    },
    "Humanis Policlub": {
        "notes_append": (
            "Corporate Punishment (Second Effort): supplies the muscle -- a sniper, a Raven-totem shaman, "
            "six thugs and three vehicle riggers -- for Brackhaven Investments' ambush of a runner team at "
            "the Salish-Shidhe border, hired through Kenneth Brackhaven's defected Yakashima fixer Anthony "
            "Munson."
        ),
    },
    "Knight Errant Security Services": {
        "notes_append": (
            "Corporate Punishment (Legacy): holds Boston's citywide security enforcement contract, "
            "supplemented locally by the corp Minuteman and neighborhood watches; runs city gridguide "
            "traffic in partnership with Novatech. Serves as the final-resort backup if MIT&T and Mitsuhama "
            "security both fail to contain an incident at the Dunkelzahn Magical Research Building, and "
            "leases office space there like several other megacorps studying alongside the DIMR."
        ),
    },
    "Wuxing, Inc.": {
        "notes_append": (
            "Corporate Punishment (Legacy, 2060): Wu Lung-Wai wants Dunkelzahn's bequest to Hualpa, the "
            "untranslated Elemental Scrolls of Ak'le'ar, badly enough to hire an outside Seattle team through "
            "the freelance fixer Denise Pierce while the Scrolls sit at MIT&T for a two-week DIMR/Mitsuhama "
            "study. Wuxing's Boston presence runs through the courier Huong and the Chinatown fixer Mr. "
            "Lee, and the corp has brokered an unprecedented truce between Boston's two rival Triad houses "
            "(the Yellow Lotus and the Mutual Prosperity League) to serve as a unified, discreet local arm for "
            "the operation. Once the Scrolls are stolen, Wuxing's own initiated wujen join the ritual-sorcery "
            "hunt for them alongside the Triads. DISCREPANCY: this book spells the chairman's name "
            "'Wu-Lung Wei'; treated here as the same person as the existing 'Wu Lung-Wai' row."
        ),
    },
    "Yakashima Technologies": {
        "notes_append": (
            "Corporate Punishment (Second Effort, 2060): fixer Anthony Munson runs a mole, the trained "
            "double Marianna Che, into Proteus AG's new Salish-Shidhe research facility to learn its rotating "
            "staff schedules, hiring an outside runner team to insert her undetected. The operation nearly "
            "unravels when Munson himself is turned mid-job by an operative ('Kat') working the Yakashima "
            "angle and defects to Brackhaven Investments with Marianna's file; Yakashima's real Johnson "
            "manager, Jonathan Copass, has to hire the same runners a second time to extract her before "
            "Munson can sell her out."
        ),
    },
}

LOC_UPDATES = {
    "Matchstick's": {
        "notes_append": (
            "Corporate Punishment (Double Take): Banshee, working as Telestrian Industries' handler, hires "
            "the runners here to travel to Portland and hit Universal Omnitech -- the meet that opens the "
            "entire frame-up against Saeder-Krupp."
        ),
    },
}

NPC_UPDATES = {
    "Blackwing": {
        "background_append": (
            "Corporate Punishment (Double Take, 2060): now goes by Count Evan Parris in Tir Tairngire high "
            "society, having rebuilt himself as a black-operations coordinator for Prince Aithne Oakforest "
            "after Oakforest overturned an earlier death sentence against him. Married with a family, and "
            "still 'the essence of style and grace' the earlier description gives him. Runs the Double Take "
            "frame-up of Saeder-Krupp through Telestrian Industries' handler Banshee and hand-picks the Tir "
            "Ghost unit sent after her and the hired runners. The book itself invites this exact continuity: "
            "'the player characters may have met Count Parris as Blackwing in previous adventures.'"
        ),
        "notes_append": "Corporate Punishment: no fixed stats given as Count Parris -- treat as Superhuman, delta-grade cyberware (Wired Reflexes 3, two synthetic cyberarms), not Awakened, unsurpassed with firearms, loathes dracoforms.",
    },
    "Aithne Oakforest": {
        "notes_append": (
            "Corporate Punishment (Double Take, 2060): uses Telestrian Industries as deniable cover to frame "
            "Saeder-Krupp's Lofwyr for a Universal Omnitech theft, working through his agent Count Evan "
            "Parris and Telestrian's handler Banshee, then deploys a borrowed Tir Ghost unit to eliminate "
            "loose ends including Banshee herself. Never appears on-page directly."
        ),
    },
    "Kenneth Brackhaven": {
        "background_append": (
            "Corporate Punishment (Second Effort, 2060): by this point running Brackhaven Investments, an "
            "openly anti-metahuman investment firm; publicly softened his rhetoric for business while "
            "privately unchanged, having grown into one of Seattle's wealthiest and best-known figures. "
            "Recruits dissatisfied corporate suits away from rival corps -- his fixer Anthony Munson, freshly "
            "turned from Yakashima Technologies, is his only on-page representative here; Brackhaven's "
            "muscle is drawn from Humanis Policlub ranks and he never appears in person."
        ),
    },
    "Wu Lung-Wai": {
        "background_append": (
            "Corporate Punishment (Legacy, 2060, spelled 'Wu-Lung Wei' in that book -- same person): wants "
            "Dunkelzahn's bequest to Hualpa, the untranslated Elemental Scrolls of Ak'le'ar, badly enough to "
            "hire an outside Seattle runner team through the freelance fixer Denise Pierce while the Scrolls sit "
            "on loan at MIT&T for a DIMR/Mitsuhama study. May be the robed, meter-long-mustached figure "
            "observing (never named on-page) if the runners deliver the Scrolls to Wuxing's Boston cutouts."
        ),
    },
    "Hiroshi Yakashima": {
        "notes_append": (
            "Corporate Punishment (Second Effort, 2060): his corp's aggressive bioresearch-acquisition drive "
            "leads directly to the Proteus AG espionage plot -- fixer Anthony Munson runs a trained double, "
            "Marianna Che, into Proteus's new Salish-Shidhe facility on Yakashima's orders, hiring outside "
            "runners for both the insertion and, when Munson himself defects mid-job, the extraction."
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
**1. Universal Omnitech Portland lab host** (Double Take, p.24) -- sculpted as an undersea theme: data
transfers are schools of fish, nodes are coral reefs or sunken ships, the core is a huge undersea castle;
unmodified decker icons appear as mermaids/mermen, Smoke as ink clouds, Sleaze as a shell-shaped
armband, Attack as a trident. IC appears as sea creatures.

| Node | Function | Rating / IC |
|---|---|---|
| Fifth-floor terminals | Any cubicle workstation; decker jacks in from anywhere on the floor | -- |
| Datastore (sunken ship) | 3,000+ Mp of magical-metagene research data, found via Locate File | -- |
| Security link | Not connected to the building's rigged physical-security system | -- |

**2. Proteus AG onshore/offshore network** (Second Effort, p.46) -- sculpted as an enormous aquarium:
datastores are treasure chests on the aquarium floor, the security node is a deep-sea diver, IC are gray or
white sharks; Proteus deckers appear in black diving suits with harpoon guns and are rated Superior/
Professional.

| System | ACIFS | Notes |
|---|---|---|
| Onshore land facility | Red-7: 14/13/14/12/14 | Access via the code Marianna provides, past a public choke-point area |
| Offshore aquasphere | Red-9: 13/13/16/18/15 | Connected to onshore via the security office; tougher of the two |

**3. MIT&T campus Matrix** (Legacy, p.69) -- layered public/private/security architecture.

| Network | ACIFS | Notes |
|---|---|---|
| Public campus net (by school) | Blue-6/6/8/6/8/8 | Architecture, Engineering, Humanities, Sloan, Science, Thaumaturgy, Liberal Arts, plus Admin |
| Campus PLTG (student/faculty/researcher) | Green-8/9/8/6/9/9+ | Classified research, hermetic libraries, student/faculty work |
| Campus security net | Orange-8/11/10/7/12/12 | Accessible from the private network; secret DIMR-MCT backdoor for monitoring |
| Scroll Lab computers | Orange-7/10/10/8/9/8 | Secured, offline when the runners arrive; holds research and digital Scroll scans |

Matrix security campus-wide is trace-and-analyze (nonlethal): a caught hacker is kicked and police are
notified; trace IC runs one rating higher than expected, higher still in secured labs.
"""

NOT_BUILT = """
- Cinanestial (Tir Tairngire airline), Morningstar Field (Portland airport) -- procedural color only.
- The Mill and the Edge (Portland shadow hangouts, name-dropped alongside the Ivanhoe) -- never visited on-page.
- Kate Mulligan and "Ross" (TTBC News reporter/anchor, Double Take) -- generic newscast color.
- The unnamed Colucci's hostess (Grade 1 physical adept) and "Tiny" the doorman -- generic archetypes, folded into Colucci's location notes.
- Green Sleeves, Inc. and Taylor Enterprises -- front-company cover identities used for the two insertions, not real orgs.
- MIT&T's other corporate tenants at the Dunkelzahn Magical Research Building (Aztechnology, Yamatetsu, Renraku, Saeder-Krupp, Atlantean Foundation, Manadyne, Novatech, Mass General Hospital, UCAS Army) -- pure background color, folded into that location's notes.
- Assets Inc. (Draco Foundation's shadowops team, Legacy) -- name-dropped by Mama and in Shadowlore only.
- The three unnamed background observers at the Legacy Delivery meets (the robed Chinese man with the meter-long mustache, the Japanese man in charcoal with an unlit cigarette, the Hispanic man with shimmering eyes) -- all confirmed astrally mundane, none named on-page.
- Wind Walker and "the Crone"/"the Hag" (Legacy's Kings and Pawns prologue framing device) -- ambiguous astral figures in a stylized chess-game vignette, never tied concretely to the plot; left as unbuilt texture rather than guessed at.
- Generic security/pursuit squads statted at length in the book (MIT&T campus guards, MCT building guards, Proteus AG Security, MCT Security Operatives, DIMR Security Force, Triad/Yakuza operatives, Brackhaven's sniper/shaman/thugs/riggers, the Tir Ghosts' individual squad slots, Universal Omnitech's samurai/mage/rigger/physical-adept templates) -- folded as stat-block color into the relevant ORG notes rather than built as NPCs.
"""

PLAY_NOTES = """
- The three adventures are fully independent; run any one alone or in any order without continuity cost.
- Double Take is explicitly open-ended and hard: no single "win" ending exists, and every resolution leaves
  the runners with at least one new powerful enemy. Decide before the session which faction(s) will get
  the runners first if the players stall, per the book's own Debugging guidance.
- Second Effort runs on a tight real-world timeline (hire Friday, insert by Monday, confirmation the
  following Friday, extraction that same weekend) -- keep the countdown visible to the players.
- Legacy's seven pursuing factions (MIT&T, MCT's Unit 13, the DIMR, the Yakuza, the Triads, Wuxing, and
  Mama) do not all need full combat writeups in play; the book explicitly expects the GM to use as many or
  as few as the scene calls for, with Mama arriving last to pull the runners out once things get dangerous.
- The Elemental Scrolls of Ak'le'ar are narrative MacGuffins, not power-ups: they grant no abilities to
  anyone who possesses them, resist nearly all damage (Armor/Mystic Armor 20, Body 13), and periodically
  attract curious (not hostile) elemental spirits -- except for two specific, very old and very powerful
  guardian spirits (a free air spirit and a bound great-form fire elemental) that manifest and fight to the
  death only if the Scrolls are in genuine physical danger.
- Kenneth Brackhaven, Aithne Oakforest, Wu Lung-Wai (spelled "Wu-Lung Wei" here) and Hiroshi Yakashima
  are all continuity from earlier books in this campaign (Super Tuesday, Celtic Double-Cross, Blood in the
  Boardroom) -- use their existing established personalities and history, not fresh reads of this book alone.
"""
