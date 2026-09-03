# Silver Angel (FASA 7102, Shadowrun 1st Edition GM Screen adventure, 1989) -- campaign order #1.
# Source text: docs/Adventures/text/Shadowrun 1e - SilverAngel {FASA7102}.txt (32 pages).
# ASCII only (pre-commit hook). "nuyen" is spelled out instead of the yen glyph.

ADVENTURE = "Silver Angel"
ORDER = 1
SOURCE = "Shadowrun 1e - Silver Angel {FASA7102}.pdf, pp. 3-32"
YEAR = "2050 (early)"

SYNOPSIS = """
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
"""

TIMELINE = """
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
"""

# ---------------------------------------------------------------------------------------------
ORGS = [
    {
        "name": "King's Crimson",
        "org_type": "gang",
        "affiliation_contact_type": "Gang",
        "tier": 2,
        "headquarters": "Seattle (turf not given in source)",
        "summary": "Street gang; honor-debt to Eve Donovan; a member's word is good",
        "description": (
            "A Seattle street gang whose members dress entirely in black -- shoes, pants, shirt, gloves, "
            "long coat -- randomly splattered in red, right down to their black-dyed hair. Word on the "
            "street is that any King's Crimson member who gives his word can be trusted to keep it, "
            "which makes them useful go-betweens for people who need discreet messages carried. "
            "Typical members ride second-hand Yamaha Rapiers, carry Streetline Specials and knives, run "
            "low-light cybereyes and Wired Reflexes 1, and are never far from a simsense player and a "
            "pocketful of chips. Any member can call on 2D6 others when trouble starts."
        ),
        "leadership": [
            {"name": "Alan Corliss", "title": "Leader", "notes": "Owes Eve Donovan an honor-debt."}
        ],
        "notes": (
            "Leader Alan Corliss recently, and inadvertently, ended up owing fixer Eve Donovan an "
            "honor-debt; as a result she can draw on up to twelve gang members as needed. King's "
            "Crimson emissaries deliver Donovan's invitations to Matchstick's and can be used to reach "
            "Haruhiko Blake or Karen Whisper if the runners' own contacts come up dry. "
            "Typical member stats (Silver Angel p.23): B5 Q6 S5 C6 I5 W4, Ess 3.8, Reaction 5(7); "
            "Armed Combat 5, Bike 3, Etiquette (Street) 4, Firearms 4, Stealth 6, Unarmed 5."
        ),
    },
    {
        "name": "The Blood Brothers",
        "org_type": "crime syndicate",
        "tier": 2,
        "headquarters": "Chop shop deep in the Redmond Barrens; meets at the Cerebus Warehouse",
        "summary": "Haruhiko Blake's chop-shop crew; feared organ-and-cyber traders",
        "description": (
            "The crew around Haruhiko \"Blood\" Blake, a disgraced Mitsuhama security director turned "
            "underworld surgeon-broker. The Blood Brothers run a high-grade illegal chop shop hidden deep "
            "in the Barrens: body-part transplants and cyber implants for anyone with the nuyen, with the "
            "correct compatible organ available within a few hours. Nobody asks where the parts come "
            "from. Members are among the most feared individuals in Seattle; the police consider Blake "
            "and his men so many names on the missing-persons list."
        ),
        "leadership": [
            {"name": "Haruhiko Blake", "title": "Boss (\"Blood\")", "notes": "Ex-Head of Security, Cavilard Research Center."}
        ],
        "notes": (
            "Blake keeps the abandoned Cerebus Warehouse on the wharf as his meeting ground and pays the "
            "homeless of the district to report anyone snooping around it. He trades information for "
            "favors (\"marks\" he can call in later), not money. Reaching him takes an Etiquette (Street) "
            "test at TN 9 (+3 unless Mitsuhama, Applied Security, or Cavilard is mentioned); useful "
            "contacts are the Burned-Out Mage, Detective, Fixer, Gang Boss/Member, Squatter, Street Doc, "
            "Mage, Samurai, Shaman, and Yakuza Boss. Blake holds a grudge against both Mitsuhama and "
            "Applied Security Concepts."
        ),
        "enemies": ["Mitsuhama Computer Technologies", "Applied Security Concepts"],
    },
    {
        "name": "Applied Security Concepts",
        "org_type": "security contractor",
        "tier": 2,
        "headquarters": "Seattle",
        "summary": "Failing computer/physical security contractor guarding Cavilard; Lone Star buyout looming",
        "description": (
            "For a long time one of the premier Seattle agencies for installing and guarding computer "
            "systems. ASC has recently fallen on hard times and every indication points to a buyer -- "
            "probably Lone Star Security -- taking the firm over in the near future. ASC supplies all of "
            "the security guards at Mitsuhama's Cavilard Research Center (the Security Director is a "
            "Mitsuhama employee) and holds a data-protection contract that dispatches an ASC decker "
            "whenever a client declares a computer emergency."
        ),
        "notes": (
            "Morale is at an all-time low and the guards are slacking: before any alert, apply +1 to any "
            "Perception or Social test an ASC guard has to make against the runners. Supplies have been "
            "cut back -- guards carry standard gear and cheap body armor (Armor Vest, Browning "
            "Max-Power; on Alert they draw Partial Heavy Armor, helmet, and an FN HAR from the Cavilard "
            "armory). A Minor-League Corporate Decker responds 2D6 turns after an External Alert, a "
            "second 3D6 turns later. Haruhiko Blake claims ASC knew one of its techs was stealing "
            "Cavilard computer time and let it ride for a cut of the profits. White Tiger cracked the ASC "
            "database to learn which guards had monitor duty on the night of the run. Guard shifts at "
            "Cavilard: 5 a.m.-1 p.m., 1-9 p.m., 9 p.m.-5 a.m., eight guards per shift."
        ),
        "allies": ["Mitsuhama Computer Technologies"],
    },
    {
        "name": "Russel Overland Transport",
        "org_type": "corporation",
        "tier": 1,
        "headquarters": "Seattle",
        "summary": "Trucking contractor for Cavilard; leaky Matrix system; runs the biohazard Roadhauler",
        "description": (
            "A Seattle hauling company whose contract with Mitsuhama covers everything from incidental "
            "carting to high-priority secured cargo for the Cavilard Research Center. Some runs are fully "
            "automated vehicles, others carry crews. Its converted Ares Roadhauler (a biohazard-sealed "
            "Roadmaster variant) makes the 2:00 a.m. delivery on the night of the run."
        ),
        "notes": (
            "Russel Overland's Matrix security is so full of holes the term barely applies: an Orange "
            "system with no Red nodes and no node rated above 4 (generate with the Quick Matrix rules). "
            "Its records reveal: six minimally shielded containers of low-grade biohazard (nausea and "
            "fever after a three-day incubation) due at Cavilard at 2:00 a.m.; any schedule change must "
            "be cleared with Mitsuhama; the vehicle is a converted Ares Roadmaster with an Ares Pro-Pilot "
            "II auto-pilot (Skill 2) that can be overridden remotely; three technician/handlers ride "
            "along. Crew are Corporate Wage Slaves in hooded hazard suits that hide the wearer's face. "
            "Cab doors: maglock keypad rating 4; rear cargo door: rating 6. The cab phone dials straight "
            "to the Overland terminal, which notifies Cavilard of any delay."
        ),
        "allies": ["Mitsuhama Computer Technologies"],
    },
    {
        "name": "Seattle Metroplex Guard",
        "org_type": "government",
        "tier": 3,
        "headquarters": "Seattle Metroplex government",
        "summary": "Former National Guard; under-equipped emergency peacekeepers answering to the governor",
        "description": (
            "Seattle's emergency peace-keeping force, formerly the National Guard, renamed under the "
            "political accommodation with the Salish-Shidhe Council. Guardsmen answer directly to the "
            "Metroplex governor. Under-manned and ill-supplied next to corporate armies and professional "
            "security cops, they are nonetheless citizens proud to serve -- and quietly envious of the "
            "heavy hardware the private armies play with. Metroplex choppers sweep the bay at night "
            "looking for debris, human debris included."
        ),
        "notes": (
            "Typical Guardsman (Silver Angel p.27): B4 Q4 S4 C2 I3 W3; Firearms 5, Unarmed 4, Etiquette "
            "(Corporate/Street) 2. Attitude: \"It's our job to keep the peace. But if you want to make "
            "trouble, we can accommodate you there as well.\" Not adventure-specific -- consider "
            "activating immediately as general world texture."
        ),
    },
]

# ---------------------------------------------------------------------------------------------
LOCATIONS = [
    {
        "name": "Cavilard Research Center",
        "location_type": "research lab",
        "district": "Bellevue",
        "security_level": "Corporate High Security",
        "controlling_org": "Mitsuhama Computer Technologies",
        "summary": "MCT R&D plant in a hill off Route 405; the target. Full three-level map + Matrix map in the book",
        "description": (
            "Mitsuhama Computer Technologies' research and development facility east of downtown, just off "
            "Route 405 in the Bellevue district. A modern building set into a gently rising hill in a "
            "former park, surrounded by light woods; heavy cement, chromed steel and smoked-glass facade. "
            "Publicly it does compu-optic systems and biotechnology research and is rumored to be only "
            "moderately secure. It has a landing pad big enough for large passenger helicopters and luxury "
            "VTOL craft -- rarely used, but traffic has picked up sharply in the last two weeks, and the "
            "microtronics industry is buzzing that Mitsuhama has hit a major breakthrough. Guards are "
            "contract staff from Applied Security Concepts; Russel Overland handles all trucking."
        ),
        "notes": (
            "Three levels (Upper: offices, cafeteria, gallery over the lobby; Ground: lobby, maintenance, "
            "CompuTech labs 1-8, loading dock with airlock; Lower: BioTech labs, Security Center, Security "
            "Director's office, Armory, Computer Center, CyberTech wing). Full room key Silver Angel "
            "pp.12-15. Every hallway has cameras at both ends, every room has PANICBUTTONS, offices have "
            "maglock keypads TN 4 (Security Center and Computer Center TN 6, barrier 10). Emergency exits "
            "D/E: plasteel barrier 10, intrusion sensors TN 4 to override, no outside handle. "
            "Eight ASC guards per shift: two at the entrance desk, one outside the Upper Level elevator, "
            "one in the loading dock, one roaming each of Ground and Upper, two in Security Control. "
            "Security Director Jack Drury (Mitsuhama) is in his office at 2 a.m. catching up on paperwork. "
            "Known glitches: Lower Level intrusion sensors are switched OFF because the air conditioning "
            "keeps tripping them, and any Lower Level room connects to any other through the A/C ducts "
            "(except across airlocks); the door latches in the Lower Level south wing (rooms 14-18) open "
            "if you press any two keypad numbers at once. Rumor says the cameras static-out often enough "
            "that nobody worries. Armory: Partial Heavy Armor, helmets, Browning Max-Powers, FN HARs. "
            "The Executive System (Silver Angel, 80 Mp, Scramble 3, in DS-13) is physically isolated; it "
            "can only be linked to the main system from a terminal in the Computer Center (Computer TN 4, "
            "3 successes; failure = External Alert) or jacked directly (4 actions to rig). Explosives sealed "
            "under the Computer Center floor destroy the primary datastores if the Security Center guard "
            "throws the switch (SM-8). CyberTech Supervisor's office holds the only clue: the name Dr. "
            "Denise Parkwood and the codename Silver Angel. CyberTech labs: ~8,000 nuyen of parts to a "
            "patient scavenger. On External Alert the ENS gives all IC +2. Matrix host: see the prep doc "
            "(full node map, Silver Angel p.16)."
        ),
    },
    {
        "name": "Matchstick's",
        "location_type": "nightclub",
        "district": "Seattle Center",
        "security_level": "Patrolled / Commercial",
        "summary": "Members-only basement jazz club near the Needle; Donovan's meeting place (password 'Steward')",
        "description": (
            "A local, low-profile private club in the substreet level of an office building near the "
            "Space Needle. Strictly members-only: you enter as a member or a member's guest, and new "
            "members need a sponsor. A street door leads down a stairway into a comfortably furnished bar "
            "decorated like a jazz joint from over a century ago; it holds 70 to 100 people when full. "
            "The doorman, Saint John, is a former street samurai with a photographic memory and an "
            "imposing presence. He lets guests keep their weapons but makes it clear violence inside will "
            "not be tolerated. A door at the far end of the club and a second flight of stairs lead to a "
            "short corridor ending in a white door -- the private meeting room."
        ),
        "notes": (
            "Eve Donovan runs the Silver Angel briefing from the white-door room; the password at the door "
            "and with the bartender is \"Steward\". Saint John recognizes the runners on sight because "
            "Donovan briefed him. A good recurring neutral-ground venue for fixer meets after the adventure."
        ),
    },
    {
        "name": "The Cutting Edge",
        "location_type": "nightclub",
        "district": "Downtown",
        "security_level": "Low Security",
        "summary": "Sleazy cabaret where Karen Whisper dances as Queen Conchita; the Fuchi Guns shootout",
        "description": (
            "A sleazy downtown cabaret, usually crowded with customers who view strangers with suspicion "
            "and lightly veiled hostility. The owner employs a string of human female dancer-barmaids, "
            "each with some high-tech gimmick to enhance her act; the headliner is Queen Conchita. The "
            "troll bouncer Winslow works the door and the floor. A cluttered four-meter-square storeroom "
            "behind the club opens onto a two-meter-wide, four-meter-long hallway that exits into a "
            "garbage-strewn back alley ten meters long and two wide."
        ),
        "notes": (
            "Karen Whisper's dressing room is here (searching it yields nothing). The Fuchi Guns (Rodrigo, "
            "VanChak, Ventura) come in the front showing holo-pix while Silverthorn covers the alley and "
            "shoots at anyone who opens the rear door. Winslow slows the pursuers; put one street between "
            "you and them and you are clear. Whisper's friend's convenience store, a few blocks from her "
            "apartment, is where the chips are hidden."
        ),
    },
    {
        "name": "Cerebus Warehouse",
        "location_type": "warehouse",
        "district": "Waterfront (abandoned wharf district)",
        "security_level": "No Security / Barrens",
        "controlling_org": "The Blood Brothers",
        "summary": "Derelict container warehouse on the wharf; Blake's meeting ground, riddled with smuggler passages",
        "description": (
            "A cavernous, decaying warehouse in the abandoned section of the wharf district, still bearing "
            "the faded sign of its former owner, Cerebus Shipping. It once handled the big cargo containers "
            "off long-distance freighters, and rusted empties still litter the floor with their chains "
            "dangling from the rafters. Decayed, interconnected offices honeycomb the side walls. The only "
            "light is dim and gray-green, filtered through half-broken skylights; when it rains the roar on "
            "the aluminum roof drowns everything and water drips into a hundred rusty pools. Wharf-rats and "
            "the district's homeless treat it as their sanctuary."
        ),
        "notes": (
            "Abandoned about eight years; formerly a clearing house for incoming drug shipments, so it is "
            "riddled with hiding places and man-sized passages under the metal-plated floor. Haruhiko "
            "Blake and the Blood Brothers keep its unused look deliberately and pay the local homeless to "
            "report snoopers. Blake picks it for meets because the setting and his reputation give him "
            "the negotiating edge; he comes and goes through the passages like magic and lets visitors "
            "wait just long enough to think he is not coming. Read the atmosphere text on pp.31-32."
        ),
    },
    {
        "name": "Blood Brothers Chop Shop",
        "location_type": "chop shop",
        "district": "Redmond Barrens (exact location hidden)",
        "security_level": "No Security / Barrens",
        "controlling_org": "The Blood Brothers",
        "summary": "Blake's hidden high-grade chop shop; parts and cyber for a price, no questions",
        "description": (
            "Somewhere deep in the Barrens, Haruhiko Blake's crew runs a surprisingly high-grade illegal "
            "surgery: body-part transplants and cyber implants for anyone with the nuyen, with a compatible "
            "part available within a few hours. Nobody who matters knows exactly where it is."
        ),
        "notes": (
            "Not mapped in the source. Blake is loyal to himself first and will exploit any situation; a "
            "runner who takes a mark from him may be asked to pay it off here later."
        ),
    },
    {
        "name": "Fuchi Seattle Office Tower",
        "location_type": "corporate headquarters",
        "district": "Downtown",
        "security_level": "Corporate Standard",
        "controlling_org": "Fuchi Industrial Electronics",
        "summary": "Home of the local Fuchi Systems Design division; where the Fuchi Guns meant to bring Whisper",
        "description": (
            "Fuchi Industrial Electronics' Seattle office tower, home to the local Fuchi Systems Design "
            "division. The company men who hunt Karen Whisper are ordered to bring her back here."
        ),
        "notes": (
            "Not mapped in the source; staff-gun Louis Rodrigo works out of the Systems Design division. "
            "A respected Fuchi Mr. Johnson has recently been seen in Seattle recruiting local talent."
        ),
    },
]

# ---------------------------------------------------------------------------------------------
NPCS = [
    {
        "name": "Eve Donovan",
        "role": "Fixer running the Silver Angel job for Ares (alias 'Steward')",
        "archetype": "Fixer",
        "title": "Fixer; front for Ares Macrotechnology on the Silver Angel run",
        "race": "Human",
        "gender": "Female",
        "nationality": "Swiss",
        "connection": 4,
        "description": (
            "Tall and athletic, with midnight-black hair cropped short and deep blue eyes; at the first "
            "meeting she wears loose white pants and a shirt exactly the color of her eyes. Everything "
            "about her speaks of a cultured upbringing -- a well-tailored facade over a violent life that "
            "shows few physical signs. Her left arm and leg are full cyber-replacements with no "
            "enhancements, because she refused them. Business-like during a run without being cold; some "
            "former associates call her a chrome-hearted bitch, which she is not. She listens to the team "
            "but presses them hard to perform flawlessly."
        ),
        "background": (
            "Born in Switzerland before the goblinization, orphaned at ten when a mob crushed her parents "
            "to death, she grew up on the streets of Bern and Stuttgart. She became one of the best "
            "fixers in Seattle -- the slick Coruscutra extraction from under the Euro-Products "
            "Consortium's nose during a Singapore resort weekend is still talked about -- until a run in "
            "Aztlan three years ago, when her helicopter ate a heat-seeker near the Torreon fusion plant. "
            "A long-owed corporate debt bought her rejuvenation in Seattle's blackest chop shops. Street "
            "rumor still has her dead."
        ),
        "notes": (
            "Fanatically loyal to her current employer (Ares Macrotechnology), even ahead of her own "
            "interests; will not reveal the client, and no contact can turn up who it is. Silver Angel is "
            "her comeback -- a clean run puts her back in the top rank. She insists on attending every "
            "meeting, plays devil's advocate, and will gear up and go in with the team if needed. Through "
            "Ares she can get perfect IDs in eight hours, the Pro-Pilot override kit, and a "
            "state-of-the-art comms/surveillance van (all gear rating 4+). Alan Corliss of King's Crimson "
            "owes her an honor-debt (up to twelve gang members). Pays 50,000 nuyen each up front, 35,000 "
            "on completion, 15,000 bonus if unnoticed -- and will fight Ares for the bonus if the team "
            "handled a hairy run well. Stats: B~2 Q4 S2 C6 I5 W5, Ess 1.5, Reaction 4; Negotiation 6, "
            "Etiquette (Street) 5 / (Corporate) 4, Firearms 3, Car 3, Winged Planes 2; Blood Filtration 3, "
            "datajack (100 Mp), datasoft link, display link, telephone; Japanese and Spanish skillsofts 3."
        ),
        "contact_skills": [
            "Fixer: job brokering and team assembly",
            "Ares Macrotechnology resources (IDs in 8 hours, surveillance van, Pro-Pilot override gear)",
            "King's Crimson muscle via Alan Corliss (up to 12 members)",
            "Negotiation 6; Etiquette (Corporate) 4 / (Street) 5",
            "Japanese and Spanish (skillsofts)",
        ],
    },
    {
        "name": "Haruhiko Blake",
        "role": "'Blood' -- ex-Cavilard security chief, boss of the Blood Brothers; sells maps for a favor",
        "archetype": "Crime Boss",
        "title": "\"Blood\", boss of the Blood Brothers; former Head of Security, Cavilard Research Center",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese-American (Mitsuhama corporate)",
        "organization": "The Blood Brothers",
        "connection": 4,
        "description": (
            "Tall and gaunt, hair worn unstylishly long and often done up in multiple braids, black "
            "war-paint his favorite. Both arms are cyber: the right carries a monofilament whip, the left "
            "a smartgun link. Not quite as deadly as his reputation, but he plays the role to the hilt: "
            "intense, crazy, twisted by turns, yet always polite at a meeting. Be rude once and he warns "
            "you; twice and you are on his guano-list."
        ),
        "background": (
            "Born to well-placed Mitsuhama parents at the Wake Island facility and raised entirely inside "
            "the compound, he saw nothing of the real world until his family transferred to San Francisco "
            "(Tokyo West) in his first year of high school. Trading on his parents' pull and his own "
            "prowess he went into security training and rose fast: Head of Security at Cavilard by 30. "
            "Two years ago a Cavilard tech stole computer time to build a simulation game for the Brits "
            "(now number one on the charts); Blake was unjustly implicated and forced out of Mitsuhama "
            "abruptly. He spiralled into the Seattle underworld, which embraced a man of his talents, and "
            "maneuvered his way to the top of a chop shop deep in the Barrens."
        ),
        "notes": (
            "Loyal to himself first, the Blood Brothers a distant second; honors his word but gives it "
            "rarely and exploits every situation. Meets the team at the Cerebus Warehouse on the evening of "
            "Day 2 -- the time cannot be moved -- and lets them sweat before appearing through the floor "
            "passages. Price for his help is a favor he can call in later (a mark), not money. He knows: "
            "the directory of a secondary data line into Cavilard (NA/UCAS-SEA-8206, SAN-3); that the "
            "cameras static-out often; that maglock keypads guard the important doors; that a destruct/purge "
            "system around the main datastores is triggered from the Security Center via a slave module on "
            "the Security Subprocessor. He also has complete, accurate maps of the Center and its Matrix "
            "(no room descriptions). Angry at both Mitsuhama and Applied Security. Stats: B4(6) Q6 S5 C5 "
            "I5 W5, Ess 0.05, Reaction 5(9); Armed Combat 6, Firearms 6, Unarmed 5, Stealth 4, Etiquette "
            "(Corporate/Street) 4. Cyber: cyberarms (monofilament whip / smartgun link), datajack, dermal "
            "armor 1, Wired Reflexes 2. Gear: HK227 SMG smartgun (flechette), Streetline Special in an ankle "
            "holster, lined coat, concussion grenade."
        ),
        "contact_skills": [
            "Illegal transplants and cyber implants within hours (Blood Brothers chop shop)",
            "Cavilard / Mitsuhama insider knowledge and system maps",
            "Barrens underworld muscle and intimidation",
        ],
    },
    {
        "name": "Karen Whisper",
        "role": "'Queen Conchita', dancer at the Cutting Edge; unknowingly holds Neon Fever's Cavilard map",
        "archetype": "Dancer",
        "title": "Barmaid and dancer at the Cutting Edge (stage name Queen Conchita)",
        "race": "Human",
        "gender": "Female",
        "nationality": "Hispanic / Amerindian",
        "connection": 1,
        "description": (
            "Attractive but worn: dark-streaked red hair, startlingly green eyes, slightly above average "
            "height with a dancer's figure. When the runners find her she is wearing her dance costume "
            "under a cheap polycloth robe. Pleasant by nature, but present circumstances make her "
            "paranoid, frightened, and testy; she spooks easily and screams for Winslow if she feels "
            "threatened."
        ),
        "background": (
            "She was the girlfriend of the decker Neon Fever (Frank Gazzara) until Aztechnology had him "
            "killed several months ago after he ran their pyramid. Fleeing their apartment ahead of the "
            "corp she grabbed a handful of his personal effects, including a packet of optical chips she "
            "has never dared examine. She knows Aztechnology killed him and assumes the chips are why. "
            "Since his death she has grown fearful of emotional connections and is quietly glad to be "
            "rid of his mementos."
        ),
        "notes": (
            "Contacts who can locate her (TN 4): Bartender, Club Owner, Decker, Gang Boss/Member, Rocker, "
            "Street Cop, Doc, Mage, Samurai, Shaman. Best approached by a decker name-dropping Neon "
            "Fever's friends. Getting the files: Etiquette TN 9; she denies everything, then relents for "
            "at least 2,500 nuyen. The chips hold a months-old Cavilard system map plus about 6,000 nuyen "
            "of raw data, hidden in a friend's convenience store a few blocks from her apartment. If she "
            "escapes a fight she cannot be found again in time. After the sale she vanishes -- until the "
            "news that Queen Conchita's murdered body turned up in the Barrens (no clues, no suspects). "
            "Stats: B5 Q5 S3 C6 I4 W5, Ess 5.6; Dance 6, Acrobatic Dance 3, Performance Composition 3; "
            "datajack, synthlink; knife, Streetline Special, Mitsubishi Runabout."
        ),
        "contact_skills": ["Neon Fever's chips (Cavilard system map + 6,000 nuyen raw data)"],
    },
    {
        "name": "Jack Drury",
        "role": "Cavilard Security Director; ex-UCAS Marine; the man to bluff past or fight",
        "archetype": "Corporate Security Director",
        "title": "Security Director, Cavilard Research Center",
        "race": "Human",
        "gender": "Male",
        "nationality": "UCAS",
        "organization": "Mitsuhama Computer Technologies",
        "connection": 1,
        "description": (
            "Large and solidly built, he looks like the ex-UCAS Marine he is: military-short hair shot "
            "with gray, a strict taskmaster who wields his authority like a weapon and does not take "
            "kindly to taking orders himself. Gruff and direct, a difficult man to get to know."
        ),
        "background": (
            "A Mitsuhama employee (unlike the contract guards), intensely loyal to the corporation. "
            "Former UCAS Marine."
        ),
        "notes": (
            "At 2 a.m. he is in his office (Lower Level 14) catching up on paperwork; suspicious activity "
            "or unexpected guests draw him to the scene. Only an aggressive fake-Mitsuhama-executive act "
            "can bully him: Negotiation or Etiquette (Corporate) vs his Willpower 5, +2 for any request "
            "touching the Executive System or Computer Center, +4 because ignoring the standing order "
            "(nobody but authorized Cavilard staff touches the Executive System) is harmful; -1 for a "
            "proper ID, -2 more if the computer verifies it (TN 8). Failure makes him hostile. Stats: B5 "
            "Q6 S6 C2 I4 W5, Ess 4, Reaction 5(7); Firearms 7, Unarmed 6, Stealth 5, Car 5, Armed "
            "Combat 4; Wired Reflexes 1; Ares Predator (2 reloads), armed like the guards on Alert."
        ),
    },
    {
        "name": "Callie Firebird",
        "role": "Fuchi's out-of-town covert mage; already inside Cavilard on the night",
        "archetype": "Corporate Mage",
        "title": "Contract mage for Fuchi Industrial Electronics (covert action specialist)",
        "race": "Human",
        "gender": "Female",
        "nationality": "Amerindian",
        "organization": "Fuchi Industrial Electronics",
        "connection": 1,
        "description": (
            "Average height, long dark hair shaved close at the sides, semi-traditional Amerindian "
            "clothing, warpaint when shadowrunning. Her personality runs hot and cold as she wishes -- "
            "a bantering teammate one moment, cool and all-business the next. Trained in avoidance and "
            "deception but prepared to make a lot of noise if she must."
        ),
        "background": (
            "Out-of-town magical talent Fuchi trusts to pull off the Silver Angel datasteal without "
            "attracting notice. Loyal to her employer, though not the self-sacrificing type."
        ),
        "notes": (
            "Her plan: visit the two guards rostered for monitor duty; one she talks into calling in "
            "sick, the other she puts under her See-Me-Not spell (custom: Drain L1, mana, maintainable -- "
            "the subject is distracted whenever shown the chosen image and never remembers it; an alarm "
            "breaks and re-triggers it in a feedback loop). She and White Tiger enter under Invisibility "
            "behind a decoy vehicle of three girls who chat up the desk guards, ride the elevator down with "
            "an unsuspecting guard, and hold the Computer Center with the door shade drawn while she "
            "maintains Detect Life and takes preemptive action against anyone approaching. Stats: B2 Q3 "
            "S1 C2 I5 W3, Ess 6, Magic 6, Reaction 4; Sorcery 6, Conjuring 5, Magical Theory 6, Etiquette "
            "(Corporate) 4, Firearms 3; Astral pool 17. Spells: Mana Bolt 4, Clairvoyance 4, Detect Life 4, "
            "Heal Moderate Wounds 2, Chaos 3, Invisibility 5, Barrier 3, See-Me-Not. Gear: armor jacket, "
            "Enfield AS7 assault shotgun (explosive rounds, laser sight), Fichetti Security 500 (extended "
            "clip), Illusion focus 2, Manipulation focus 3, computer-media hermetic library."
        ),
    },
    {
        "name": "Arthur Farren",
        "role": "'White Tiger', local decker on Fuchi's team; downloads Silver Angel from inside",
        "archetype": "Corporate Decker",
        "title": "\"White Tiger\"; contract decker for Fuchi Industrial Electronics",
        "race": "Human",
        "gender": "Male",
        "organization": "Fuchi Industrial Electronics",
        "connection": 2,
        "description": (
            "A tall, thin young man who speaks only rarely; when he does his voice is surprisingly deep "
            "and expansive. Dislikes physical violence and fights only if his life is threatened."
        ),
        "background": (
            "Local Seattle talent who has worked for Fuchi before, but never on anything this important. "
            "Loyal to the company, not to the point of self-sacrifice."
        ),
        "notes": (
            "Penetrated the Applied Security Concepts database to learn which two guards had monitor duty. "
            "On the night he bypasses the Computer Center lock (apparently unaware of the south-wing "
            "keypad glitch), jacks directly into the Executive System, and is leaving with Silver Angel "
            "when the ENS arrives at 2:18. Stats: B1 Q3 S3 C1 I4 W3, Ess 5.8, Reaction 3; Computer 5, "
            "Computer Theory 4, Etiquette (Corporate) 2; Hacking pool 8. Fuchi-4 cyberdeck with Level 1 "
            "Response Increase; programs Bod 5, Evasion 5, Masking 4, Sensors 6, Attack 5, Smoke 3, Slow 6. "
            "Armor clothing, knife, Streetline Special, Mitsubishi Runabout."
        ),
    },
    {
        "name": "Louis Rodrigo",
        "role": "Fuchi Systems Design staff-gun leading the four 'Fuchi Guns' hunting Whisper",
        "archetype": "Company Man",
        "title": "Staff-gun, Fuchi Systems Design (Seattle); leader of the \"Fuchi Guns\"",
        "race": "Human",
        "gender": "Male",
        "organization": "Fuchi Industrial Electronics",
        "connection": 1,
        "description": (
            "A corporate hard case in the dress of the Japanese-American consortium corps. Leads three "
            "companions through Seattle's bars showing a flat holo-pix of Karen Whisper to the patrons. "
            "Someone on the team may recognize him from a past job (roll 1D6 hours to place the face)."
        ),
        "background": (
            "Rodrigo and his crew were told only to find Karen Whisper and bring her to the Fuchi office "
            "tower -- not why. All four carry forged Ares Macrotechnology / Knight Errant identification; "
            "nothing connects them to Fuchi."
        ),
        "notes": (
            "Stats: B5 Q5 S5 C2 I4 W4, Ess 4, Reaction 4(6); Firearms 5, Unarmed 6, Stealth 5, Armed "
            "Combat 4, Car 4, Etiquette (Corporate) 3; Wired Reflexes 1. Gear: armor clothing, Ruger Super "
            "Warhawk (shoulder holster, 2 reloads), Streetline Special (ankle, 1 reload). Gunfire in the "
            "alley draws him and the others out of the club."
        ),
    },
    {
        "name": "Silverthorn",
        "role": "Elf hitman; the fourth Fuchi Gun, covering the Cutting Edge back alley",
        "archetype": "Hitman",
        "title": "Elf hitman on Fuchi's payroll (the fourth \"Fuchi Gun\")",
        "race": "Elf",
        "gender": "Male",
        "organization": "Fuchi Industrial Electronics",
        "connection": 1,
        "description": (
            "Stands in plain view in the alley behind the Cutting Edge with a clear line on the rear door, "
            "and assumes anyone who exits or even pokes a head out is Karen Whisper trying to escape. He "
            "takes appropriate action."
        ),
        "notes": (
            "Stats: B5 Q6 S5 C2 I4 W4, Ess 2.5, Reaction 5(9); Firearms 5, Stealth 5, Demolitions 4, "
            "Hovercraft 4, Bike 4, Car 4, Unarmed 4, Etiquette (Corporate/Street) 3; smartgun link, Wired "
            "Reflexes 2. Gear: Ares Slivergun with smartgun adapter (shoulder holster, 3 reloads), armor "
            "clothing."
        ),
    },
    {
        "name": "Shen VanChak",
        "role": "Fuchi company man in Rodrigo's crew",
        "archetype": "Company Man",
        "title": "Company man, Fuchi Industrial Electronics (the \"Fuchi Guns\")",
        "race": "Human",
        "gender": "Male",
        "organization": "Fuchi Industrial Electronics",
        "connection": 1,
        "description": "One of Rodrigo's three companions canvassing bars for Karen Whisper; may pass for an Ares/Knight Errant badge on his forged ID.",
        "notes": (
            "Stats: B5 Q4 S5 C2 I4 W4, Ess 4, Reaction 4(6); Unarmed 6, Stealth 5, Armed Combat 4, Car 4, "
            "Firearms 3, Etiquette (Corporate) 3; Wired Reflexes 1. Gear: armor clothing, Browning "
            "Max-Power (shoulder holster, 3 reloads), Streetline Special (ankle, 1 reload)."
        ),
    },
    {
        "name": "Vicki Ventura",
        "role": "Street samurai muscle in the Fuchi Guns",
        "archetype": "Street Samurai",
        "title": "Street samurai working for Fuchi (the \"Fuchi Guns\")",
        "race": "Human",
        "gender": "Female",
        "organization": "Fuchi Industrial Electronics",
        "connection": 1,
        "description": (
            "The heavy in Rodrigo's crew -- chromed to the eyeballs and packing a heavy sidearm, which is "
            "the detail a sharp-eyed runner notices first. Could be mistaken for a Fuchi employee."
        ),
        "notes": (
            "Stats: B6 Q6(7) S6(7) C2 I5 W5, Ess 1, Reaction 5(9); Firearms 5, Unarmed 6, Armed Combat 4, "
            "Stealth 4, Etiquette (Street) 4. Cyber: low-light cybereyes, dermal armor 2, muscle "
            "replacement 1, retractable hand razors, smartgun link, Wired Reflexes 2. Gear: armor jacket, "
            "Uzi III smartgun (hip-slung, 4 reloads), Fichetti Security 500 (lower-back holster, 2 "
            "reloads), two throwing knives."
        ),
    },
    {
        "name": "Winslow",
        "role": "Troll bouncer at the Cutting Edge; devoted to Queen Conchita",
        "archetype": "Bouncer",
        "title": "Bouncer and doorman, the Cutting Edge",
        "race": "Troll",
        "gender": "Male",
        "connection": 1,
        "description": (
            "Older than most trolls -- old enough to remember being human before the goblinization, and "
            "looking at Queen Conchita brings back sweet memories. He has seen plenty of scum come and go "
            "and knows how to deal with it. He admires her, thinks she can do better than this place, and "
            "will do everything he can to give her the chance she deserves. Allergic to sunlight (nuisance)."
        ),
        "notes": (
            "Comes running if Whisper screams; if a fight breaks out she bolts and is lost. When the Fuchi "
            "Guns show up he advises her to slip out the back and then does his best to slow them down. "
            "Force applied to him or the staff yields Whisper's apartment address (which holds no clues). "
            "Stats: B9 Q3 S9 C1 I1 W2, Ess 6, Reaction 2; Unarmed 6, Armed Combat 3, Firearms 2, Etiquette "
            "(Street) 2. No gear."
        ),
    },
    {
        "name": "Saint John",
        "role": "Doorman at Matchstick's; ex-street samurai with a photographic memory",
        "archetype": "Doorman",
        "title": "Doorman, Matchstick's",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": (
            "A former street samurai with a photographic memory and an imposing presence. He recognizes "
            "guests on sight, gives a knowing smile at the name Steward, lets you keep your weapons, and "
            "warns that violence inside the club will not be tolerated."
        ),
        "notes": (
            "No stats in the source. Because he never forgets a face, he is a natural information source "
            "about who has been meeting whom at Matchstick's -- and a natural liability for runners who "
            "want to be forgotten."
        ),
        "contact_skills": ["Never forgets a face -- who has been in and out of Matchstick's"],
    },
    {
        "name": "Alan Corliss",
        "role": "Leader of King's Crimson; owes Eve Donovan an honor-debt",
        "archetype": "Gang Boss",
        "title": "Leader of the King's Crimson street gang",
        "race": "Human",
        "gender": "Male",
        "organization": "King's Crimson",
        "connection": 3,
        "description": "Leader of King's Crimson. Wears the gang's black-splattered-red colors like everyone else; his word, once given, is kept.",
        "background": (
            "Recently and inadvertently ended up owing fixer Eve Donovan an honor-debt. He pays it by "
            "putting up to twelve of his people at her disposal for the Silver Angel job."
        ),
        "notes": (
            "No stats in the source (use the King's Crimson gang member block, Silver Angel p.23). Can be "
            "the route to Haruhiko Blake or Karen Whisper if the runners' own contacts fail."
        ),
        "contact_skills": ["King's Crimson gang muscle and messengers"],
    },
    {
        "name": "Dr. Denise Parkwood",
        "role": "Mitsuhama cybernetics researcher; extracted by Ares from the Philippines the same night",
        "archetype": "Corporate Scientist",
        "title": "Cybernetics researcher, Mitsuhama Computer Technologies",
        "race": "Human",
        "gender": "Female",
        "organization": "Mitsuhama Computer Technologies",
        "connection": 1,
        "description": (
            "Her name, alongside the codename Silver Angel, is the only clue in the CyberTech Supervisor's "
            "office at Cavilard -- an office that clearly belongs to someone else. Whatever Silver Angel "
            "is, it is hers, and Mitsuhama is excited enough about it to run VTOL traffic into Cavilard."
        ),
        "notes": (
            "At 2:00 a.m. on the night of the run an Ares Macrotechnology commando team para-drops into the "
            "Mitsuhama enclave in the Philippines and extracts her. After the adventure she is presumably "
            "an Ares asset; Mitsuhama will want her -- and the runners who stole the duplicate file -- back. "
            "No stats in the source."
        ),
    },
    {
        "name": "Frank Gazzara",
        "role": "'Neon Fever' -- decker killed by Aztechnology; left the Cavilard map behind (deceased)",
        "archetype": "Street Decker",
        "title": "\"Neon Fever\", street decker (deceased)",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": (
            "Deceased before the adventure begins. A Seattle decker who by chance acquired a Cavilard "
            "Research Center system map a few days before his death."
        ),
        "background": (
            "Ran the Aztechnology pyramid a couple of months back and deep-fried his brain doing it; "
            "Aztechnology put out the contract and all but nuked his apartment afterwards. They never "
            "identified his girlfriend Karen Whisper, who fled with his chips."
        ),
        "notes": (
            "Backstory-only. Deckers with a reputation can name-drop his friends to get Whisper talking. "
            "A useful hook: whatever else was on his chips (6,000 nuyen of raw data) is the GM's to define."
        ),
    },
]

# ---------------------------------------------------------------------------------------------
ORG_UPDATES = {
    "Mitsuhama Computer Technologies": {
        "description_append": (
            "Corporate profile as published in 2050: home office Kyoto; President/CEO Toshiro Mitsuhama. "
            "Principal North American division MCT North America (data processors, computer interface and "
            "control devices) under division head Tamatsu Sakura. Despite several successful court "
            "battles the company's name remains linked to known Yakuza gang leaders -- street rumor flatly "
            "calls it a Yakuza front. Sharp and aggressive; pushes competitors hard in the market and in "
            "the labs. Relies on company personnel for internal security but makes extensive use of hired "
            "individuals and firms for special operations. Its computer systems are guarded by the "
            "blackest of IC."
        ),
        "notes_append": (
            "Owns the Cavilard Research Center in Bellevue (compu-optics and biotech on paper; actually a "
            "cybernetics / mind-machine interface program under Dr. Denise Parkwood, file codename Silver "
            "Angel). Guards there are contracted from Applied Security Concepts; only Security Director "
            "Jack Drury is MCT staff. MCT raises corporate children at compounds like the Wake Island "
            "facility and keeps an enclave in the Philippines. The Emergency Notification Signal (ENS) "
            "from Chiba HQ puts every facility and every IC on External Alert (+2 to IC ratings) and "
            "triggers armed sweeps. Response package for an alerted Seattle facility: five mercs and a "
            "wage mage by Hughes WK-2 Stallion in 3D6+5 minutes, eight more mercs in two Chrysler-Nissan "
            "Patrol-1s 3D6 minutes later (stat blocks Silver Angel p.23). Two years ago a Cavilard tech "
            "stole computer time to build a simulation game for the Brits; MCT scragged Security Director "
            "Haruhiko Blake for it, creating a very well-informed enemy. Renraku installed Cavilard's "
            "Matrix security, including a prototype Black Hole node that killed two MCT deckers and was "
            "pulled. After Silver Angel, MCT works out that Ares ran the double extraction (Parkwood plus "
            "the file) and will hunt for whoever left clues behind."
        ),
        "leadership_add": [
            {"name": "Tamatsu Sakura", "title": "Division Head, MCT North America", "notes": "Silver Angel corporate profile (2050)."},
        ],
        "enemies_add": ["Ares Macrotechnology"],
    },
    "Ares Macrotechnology": {
        "description_append": (
            "Corporate profile as published in 2050: home office Detroit, Michigan, UCAS; President/CEO "
            "Damien Knight. Principal divisions: Knight Errant Security (division head Roger Soaring Owl; "
            "private and corporate security, physical and electronic) and Ares Arms (division head Guido "
            "Cantarelli; military and police equipment from small arms to top-line Ares vehicles). Ares "
            "Arms' extensive military assets are believed to be available to Knight Errant as needed. "
            "Knight takes a direct hand in Knight Errant's day-to-day operations. Rumor links his "
            "meteoric rise to financial killings made during the Computer Crash of '29; the first reliable "
            "records show him mounting a hostile takeover of Ares from Swedish data havens and sitting in "
            "the Director's chair within 24 hours of his first stock purchase."
        ),
        "notes_append": (
            "The unseen employer behind Eve Donovan's Silver Angel datasteal, run through her as a "
            "cut-out; the same night an Ares commando team para-drops into Mitsuhama's Philippines "
            "enclave to extract Dr. Denise Parkwood. Ares supplied Donovan's IDs, a Pro-Pilot II remote "
            "override kit, and a rating-4 comms/surveillance van, and pays 50,000 + 35,000 nuyen per "
            "runner plus a 15,000 discretion bonus. Days before the run Damien Knight was seen in Seattle "
            "dining at the exclusive Eye of the Needle with rising simsense starlet Jenny Chimes. Fuchi's "
            "field agents carry forged Ares / Knight Errant ID cards."
        ),
        "leadership_add": [
            {"name": "Roger Soaring Owl", "title": "Division Head, Knight Errant Security", "notes": "Silver Angel corporate profile (2050)."},
            {"name": "Guido Cantarelli", "title": "Division Head, Ares Arms", "notes": "Silver Angel corporate profile (2050)."},
        ],
        "enemies_add": ["Mitsuhama Computer Technologies"],
    },
    "Fuchi Industrial Electronics": {
        "description_append": (
            "Corporate profile as published in 2050: home office Tokyo; President/CEO Richard Villiers. "
            "Principal division Fuchi System Design (research, design and production of advanced "
            "technology for corporate, military and industrial use) under division head Samantha "
            "Villiers. Owned and operated by a consortium of three clans -- the Yamana and Nakatomi "
            "families of Japan and the Villiers family of New York -- whose relations are less than "
            "cordial but efficiently business-like. The first ASIST simulated-senses technology created "
            "an instant boom that let Fuchi withstand a billion-dollar patent suit from ESP Systems of "
            "Chicago; the company pioneered cyberdeck technology and remains on its cutting edge. "
            "(Note: the source names the Japanese clans Yamana and Nakatomi; the existing profile above "
            "says Shigeda/Nakamura.)"
        ),
        "notes_append": (
            "Fuchi has no Seattle military force, but non-Seattle divisions build military equipment and "
            "it fielded a crack company at the Winter '49 Tunisian Corporate Wargames. Current rumors: an "
            "aborted assassination attempt on Samantha Villiers, and a respected Fuchi Mr. Johnson seen in "
            "Seattle recruiting or coordinating local talent. Fuchi knows about Silver Angel and wants it: "
            "it fields a two-person team (mage Callie Firebird and decker Arthur \"White Tiger\" Farren) "
            "inside Cavilard, and four \"company men\" (Louis Rodrigo, Silverthorn, Shen VanChak, Vicki "
            "Ventura) out of the Fuchi Seattle office tower hunting Karen Whisper with forged Ares/Knight "
            "Errant IDs. Fuchi also knows a rival is on the same trail but not who."
        ),
        "leadership_add": [
            {"name": "Samantha Villiers", "title": "Division Head, Fuchi System Design", "notes": "Target of a rumored aborted assassination attempt (Silver Angel, 2050)."},
        ],
        "enemies_add": ["Mitsuhama Computer Technologies"],
    },
    "Renraku Computer Systems": {
        "notes_append": (
            "Renraku installed the computer security at Mitsuhama's Cavilard Research Center. It tried to "
            "field a prototype \"Black Hole\" security node there -- looks like a regular node, but do "
            "anything inside it and it viruses your MPCP, hamstrings your programs, traces you home and "
            "wastes you -- but the technology was not ready: after two Mitsuhama deckers were lost the "
            "system was removed entirely. Street deckers still believe it is in there. Problems with the "
            "Arcology have made Renraku hypersensitive about internal security; lean on a Renraku contact "
            "too hard and bells start ringing."
        ),
    },
    "Lone Star Security": {
        "notes_append": (
            "The likely buyer of Applied Security Concepts, the failing Seattle computer/physical security "
            "contractor that guards Mitsuhama's Cavilard Research Center."
        ),
    },
    "Aztechnology": {
        "notes_append": (
            "Put out the contract on street decker Frank \"Neon Fever\" Gazzara after he ran the "
            "Aztechnology pyramid; his place was all but nuked afterwards. Aztech never identified his "
            "girlfriend Karen Whisper, who fled with his chips. Three years ago fixer Eve Donovan's "
            "helicopter ate a heat-seeker near the Torreon fusion plant in Aztlan."
        ),
    },
    "Knight Errant Security Services": {
        "notes_append": (
            "Forged Ares Macrotechnology / Knight Errant identification cards are in circulation: Fuchi's "
            "field agents used them while hunting Karen Whisper in Seattle."
        ),
    },
}

LOC_UPDATES = {
    "The Space Needle": {
        "notes_append": (
            "The exclusive restaurant here is known as the Eye of the Needle: Damien Knight of Ares caused "
            "a stir dining there with simsense starlet Jenny Chimes days before the Silver Angel run. "
            "Matchstick's, the members-only basement club Eve Donovan uses for meets, is in an office "
            "building nearby."
        ),
    },
}

NPC_UPDATES = {}

# ---------------------------------------------------------------------------------------------
MATRIX_HOSTS = """
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
"""

NOT_BUILT = """
- **Jenny Chimes**, rising simsense starlet seen dining with Damien Knight -- name-drop only (in Ares notes).
- **Toshiro Mitsuhama, Richard Villiers, Damien Knight** -- already on their orgs' leadership lists; not NPC records.
- **Cerebus Shipping** -- defunct former owner of the warehouse; folded into the location.
- **Euro-Products Consortium / the Coruscutra extraction** -- Donovan's past glory, kept as flavor in her background.
- **Mitsuhama Wake Island facility, Philippines enclave, Torreon fusion plant (Aztlan)** -- off-map backstory, noted on the org/NPC records instead.
- **Whisper's friend's convenience store and her apartment** -- unnamed, no clues; not recorded.
- **Cavilard Center Guard, Mitsuhama Combat Team (Merc / Wage Mage), Roadhauler crew, ASC corporate decker** -- generic stat blocks (Silver Angel pp.23, 31); noted on the org records.
- **Contacts chapter archetypes** (Club Owner, Corporate Decker, Corporate Official, Media Producer, Corporate Wage Slave, Metroplex Guardsman, Technician, pp.24-27) -- contact archetypes with quotes and stats, not individuals; candidates for the contact-archetype catalog rather than NPC rows.
- **See-Me-Not spell and the Ares Roadhauler** vehicle stats (p.31) -- recorded in Firebird's and Russel Overland's notes.
"""

PLAY_NOTES = """
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
"""
