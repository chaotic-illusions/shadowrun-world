# SRM 01-01 Double Cross (FanPro / WizKids, 2004, Shadowrun Missions Season One, SR3) --
# campaign order #44. Downtown Seattle (the Westin Seattle), Tacoma, Everett, Snohomish, Bellevue,
# Fort Lewis, Lake Washington.
# SETTING NOTE / DISCREPANCY WITH THE TASK BRIEF: this spec was commissioned as "Denver in the
# 2060s (SR4 era)". The book is neither. Season One of Shadowrun Missions is set in the SEATTLE
# metroplex and is written "For use with Shadowrun, Third Edition"; Denver is never mentioned. The
# recommended sourcebook list names "New Seattle, which provides an overview of the Seattle
# Metroplex during the 2060s, including the downtown area where this scenario takes place." Every
# location therefore carries city "Seattle" (Fort Lewis included -- it is inside the metroplex in
# this campaign's canon and already exists as a Seattle row).
# Dating: the book gives no in-world date anywhere. The only internal anchors are Davenport's
# Temporary Responder Program "that he devised back in 2057" and Garrett Walsh's reference to "the
# way things have been going since the Redmond crash in '59". Published 2004 and set "during the
# 2060s"; the Shadowrun Missions campaign clock ran roughly one in-world year per publication year
# from 2064, so YEAR is given as 2064 with the uncertainty stated.
# Editing inconsistencies in the book, noted again on the affected rows: the hotel security stat
# block arms guards with a "Little Cricket" Taser rated 6S Stun while the Personnel Security
# paragraph rates the same tasers 6M Stun; the Westin write-up gives the address as "Fifth Avenue
# and Steward Street" (the street is Stewart Street, and the handout map's own labels use "Fifth
# Avenue Corner Cafe" and a "5th Avenue Entrance"); the news handout calls Harborview Medical
# Center "Harborview Hospital"; the screamsheet says "all four HTR team members" burned in the
# ambulance while the DocWagon Special Ops stat block is written for six; and Davenport is said to
# have had "his medical data replaced with that of Earl Peabody" yet the whole plan depends on the
# DNA and dental records matching Davenport, which the handout's poster "Skeptic" is given as the
# in-world objection rather than an answer. The scenario also relies on two things the GM is told
# the players must never find (the safehouse bugs, Fox's reports) -- flagged in PLAY_NOTES.
# Rows shared with earlier specs are updated, never re-created: Griffin Biotechnology and its
# Everett research facility come from specs/srm_00_03_forced_recon.py (which also creates Dr. Indira
# Chontel -- see the Dasari/Chontel discrepancy on the Griffin org row); Fox and Dr. Fredericks come from
# specs/srm_00_01_mission_briefing.py and specs/srm_00_02_demolition_run.py, as do Paladin Medical
# Technologies and the Snohomish plant (kept under the SRM 00-02 name "DocWagon Snohomish
# Pharmaceutical Facility"; this book calls it "the Snohomish facility" and "a production facility
# in Snohomish"). This book prints "Dr. Thomas Fredericks" where SRM 00-02 gives only "Dr.
# Fredericks" -- same man, earlier name kept. Shotozumi-rengo and Toju Shotozumi already exist in
# the production database and are updated by exact name.
# Source text: docs/Adventures/text/SRM01-01A_Double_Cross.txt (26 pages) and
# docs/Adventures/text/SRM01-01B.txt (player handouts).
# ASCII only (pre-commit hook).

ADVENTURE = "SRM 01-01 Double Cross"
ORDER = 44
SOURCE = "SRM01-01A_Double_Cross.pdf, pp. 3-26; SRM01-01B.pdf (player handouts)"
YEAR = "2064 (no in-world date is printed; the book is set 'during the 2060s', references the " \
       "Redmond crash of '59 and a Temporary Responder Program devised in 2057)"

SYNOPSIS = """
**Fox**, a Seattle fixer with a taste for cigars and a low opinion of the talent he hires, calls a
team of competent unknowns to a pull-off on the west shore of Lake Washington just after dusk. The
job is wetwork: **Michael Davenport**, Chief Operations Officer of **DocWagon**'s Seattle
franchise, is to be shot or spelled at the podium during the annual shareholders' meeting in the
Grand Ballroom of the **Westin Seattle Hotel**. No explosives, no collateral damage. Ten thousand
nuyen for green runners, more for better ones, plus a fully stocked Tacoma safehouse and gear at a
twenty percent discount. One condition is non-negotiable: Fox comes along.

The reason Fox comes along is that the Johnson is Davenport himself. Two years of shot-down
proposals -- most recently a UCAS military pharmaceuticals contract with **Fort Lewis** as the
testbed, killed by CEO **Garrett Walsh**'s dislike of defense work -- convinced Davenport that
DocWagon's monopoly on metroplex health care makes it fat and cautious, and that the way to get
rich is to compete with it. He has spent months preparing: encrypted caches of customer lists and
security codes hidden across the company (one, an innocuous file named "H", sat in the Snohomish
plant that was blown up weeks ago); his own medical records swapped with those of **Earl Peabody**,
a Fort Lewis car dealer of the same build; a second Peabody clone commissioned and quietly rerouted
out of DocWagon's Tacoma storage facility. Fox reports the runners' plan to him so he can prepare
mundane countermeasures and, if he must, a mage in the audience who will drop illusions the instant
the trigger phrase is spoken. The safehouse is bugged for the same reason.

The runners get five days. They can case the hotel (a soft target with a hard PanicButton: a
magnetic anomaly detector in the guest doors, Rating 5 maglocks on credstick verification, taser-
armed private security in secure clothing, and a Lone Star contract that puts armed response inside
the building in five combat turns), work the **Rabinowitz** wedding reception in the same ballroom
the night before, deck the hotel's Orange-5 host, or get pulled into a Nightsky by an interested
investor -- Mafia don **Vincent "Numbers" Ciarniello**, sokaiya boss **Toju Shotozumi**, Paladin
Medical's **Dr. Thomas Fredericks** or the socialite **Drew Hollingsworth** -- who wants to know
which way DocWagon stock is about to move. If they dawdle, a DocWagon special ops team comes through
the safehouse windows on ropes.

At zero hour Davenport introduces **Dr. Chandra Dasari** of **Griffin Biotechnology**, says "all of
these achievements come with a price -- and not always money", and falls. A second team of runners
in DocWagon High Threat Response colors -- wearing gear taken off murdered **HTR team #27** out of
Renton -- carries him out while Fox screams over the commlink to finish the job. The runners blow
the ambulance; a Trid Phantasm and a greater form city spirit carry the real Davenport away. The
next morning's screamsheet reports five dead, DNA and dental records confirmed, cremation, a
memorial at **Reynolds Eternal Estates** in Bellevue, no surviving relatives. In a few weeks a man
with a new face named **Walter Broward** will introduce himself as Chief Executive Officer of
**Rose Croix**, a new competitor in emergency medical services, and the two-year story arc begins.
"""

TIMELINE = """
- **2057** -- Davenport devises DocWagon's Temporary Responder Program to augment undermanned HTR
  teams. The uniforms and credentials it produces are what the extraction team will wear.
- **'59** -- the Redmond crash; DocWagon shares have climbed steadily ever since, which is exactly
  Walsh's argument for taking no risks.
- **~2 years back** -- Walsh begins refusing Davenport's diversification proposals. The friendship
  strains.
- **Last month (relative to the prologue)** -- Walsh approves the Snohomish pharmaceutical plant;
  supply contracts signed with Seattle General Hospital and the university clinic.
- **A few months back** -- Davenport begins laying the groundwork: hidden encrypted files (including
  "H" in Snohomish), the Peabody records swap, retagged clones, a second Peabody clone commissioned
  "for shipment to the east coast".
- **A few weeks back** -- someone destroys the Snohomish facility; DocWagon loses six months of
  production and has to buy from outside vendors at a premium.
- **Recently** -- Yamatetsu, with AG Chemie of Europe and Paladin Medical Technologies, wins the
  UCAS defense contract Davenport wanted. The contract is the only thing keeping Paladin afloat.
- **Days back** -- someone pokes around the unopened Griffin Biotechnology facility in Everett and
  learns nothing; Knight Errant has the site.
- **Day 0 (evening)** -- Fox meets the team at Lake Washington. Five days to zero hour.
- **Days 1-4** -- the safehouse, the hotel, legwork, the Rabinowitz reception, the optional
  DocWagon raid and the optional limousine interview.
- **Day 4 (the night before)** -- the Rabinowitz-Ginsberg wedding reception fills the Grand Ballroom.
- **Day 5, evening** -- the shareholders' meeting. CEO speech, CFO speech, Davenport's speech,
  Dasari's introduction, the trigger phrase, the hit, the HTR extraction, the ambulance.
- **+30 minutes** -- the safehouse; Fox's phone call confirms Davenport and the medical team dead;
  cigars and certified credsticks.
- **The next morning** -- the KSEA screamsheet. Memorial Saturday, Reynolds Eternal Estates.
- **A few weeks on** -- surgery, a new identity, and Walter Broward of Rose Croix.
"""

ORGS = [
    {
        "name": "Rose Croix",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Seattle metroplex (not yet announced during this adventure)",
        "summary": "The new competitor in metroplex emergency medical services, biomedical research and related contracts, founded on stolen DocWagon customer lists and security codes by a dead man",
        "description": (
            "Rose Croix is a new contender in the field of emergency medical services, biomedical "
            "research and related contracts, and the corporate half of the two-year Shadowrun "
            "Missions story arc that bears its name. It does not exist yet when this adventure "
            "begins. Its founder is Michael Davenport, Chief Operations Officer of DocWagon's "
            "Seattle franchise, who spent months seeding encrypted caches of DocWagon customer "
            "lists, security codes and operational data throughout the company he intends to "
            "compete with, then hired two teams of shadowrunners to stage his own assassination so "
            "he could walk away with them. Weeks after the shareholders' meeting, with a new face "
            "and a new identity, he will surface as Walter Broward, Chief Executive Officer. Every "
            "advantage the company opens with -- client lists, response protocols, facility "
            "codes -- was taken out of DocWagon in Davenport's head and on his chips."
        ),
        "leadership": [
            {"name": "Walter Broward", "title": "Chief Executive Officer", "notes": "Michael Davenport with reconstructive surgery and a new identity."},
        ],
        "notes": (
            "SRM 01-01 sets Rose Croix up but never names it to the players; the reveal belongs to "
            "later chapters of the arc. Nothing of the corporation appears on stage in this "
            "adventure except its founder, its funding (Davenport's stolen data plus whatever "
            "backers he has quietly lined up) and the elite extraction team it can already afford: "
            "a rigger, a shaman with a greater form city spirit, mages with Improved Invisibility "
            "anchoring foci, and enough discipline to murder a DocWagon HTR team for its ambulance. "
            "The book deliberately gives that team no statistics -- 'they are as good as you need "
            "them to be' -- and rules that the runners can never capture one or keep any of its "
            "gear. Aftermath: DocWagon Seattle loses its COO, its shareholders read about "
            "terrorism, and a well-informed rival opens for business in the metroplex within weeks. "
            "The runners are the unwitting instrument and, in the shadow gossip on the handout, the "
            "prime suspects."
        ),
        "enemies": ["DocWagon"],
    },
    {
        "name": "Westin International Hotel Corporation",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "The Westin Seattle, Fifth Avenue and Stewart Street, Downtown Seattle",
        "summary": "Hotel chain whose flagship and headquarters is the three-towered Westin Seattle; runs the metroplex's largest meeting-space operation and its own private security staff",
        "description": (
            "The corporation that owns and operates the Westin chain; the Westin Seattle is both "
            "its headquarters and its flagship. Its business is first-class hospitality -- upper-"
            "class guests, permanent residents on the upper floors, three first-class restaurants "
            "and the most meeting-room space of any hotel in the metroplex -- and it protects that "
            "business rather than any secret. A private network links reservations and corporate "
            "data between all Westin properties; the Seattle host has a connector to it visible "
            "from the entry node. Manager Kevin McKeen runs the Seattle house."
        ),
        "leadership": [
            {"name": "Kevin McKeen", "title": "Manager, the Westin Seattle", "notes": None},
        ],
        "notes": (
            "Personnel policy is the security hole and the book says so plainly. Regular staff earn "
            "slightly more than minimum wage, get one multimedia HR presentation a year on how to "
            "handle terrorists, and can be bribed or talked into work details, uniforms and favors; "
            "they are normal humans, orks, dwarfs and elves at racial norms with skills of 3 or "
            "less and no combat skills. Management (mostly human or elf, racial norms +1, skills 4 "
            "or less, no combat skills) has more to lose and resists. The hired security staff -- "
            "trained and licensed by larger firms -- resists bribery better than either and is "
            "trained to read how a person moves for combat training, boosted reflexes or concealed "
            "hardware, then to ask the guest aside for a hand scanner sweep or a pat-down. Stat "
            "block p.25: B5 Q4 S4 C3 I4 W4, Ess 5.0, Reaction 4, Init 4+1d6, Combat Pool 6, Karma "
            "Pool TR-1, Professional Rating 2; Armed Combat (Baton) 2(3), Pistol (Taser) 2(4), "
            "Unarmed 3, Athletics 2, Stealth 5, Etiquette 5, Negotiation 3, Electronics 2, "
            "Computers 1, Biotech 2; Hotel Operational Procedures 4, Security Procedures 4, VIP "
            "Personnel 3; secure clothing (3/0) in hotel uniform or plain clothes; 'Little Cricket' "
            "taser (6S Stun in the stat block, 6M Stun in the text -- book inconsistency); "
            "transceiver Rating 1 with integrated PanicButton (fence value 2,500 nuyen)."
        ),
        "allies": ["Lone Star Security"],
    },
    {
        "name": "Howell, Shultz, and Rabinowitz",
        "org_type": "corporation",
        "tier": 2,
        "headquarters": "Seattle metroplex",
        "summary": "One of the most prestigious corporate law firms in the metroplex; senior partner Levi Rabinowitz's wedding reception fills the Grand Ballroom the night before the hit",
        "description": (
            "One of the most prestigious corporate law firms in the Seattle metroplex. Its senior "
            "partner Levi Rabinowitz has just married Sarah Ginsberg, daughter of the president of "
            "Seattle Federal Savings and Loan, producing one of the biggest weddings -- and one of "
            "the biggest social events -- of the year. The firm's client list is implied rather "
            "than printed: the reception draws presidents and senior officials from megacorps and "
            "large companies, the best of Seattle society, and celebrities from music, trideo and "
            "sport."
        ),
        "leadership": [
            {"name": "Levi Rabinowitz", "title": "Senior partner", "notes": "Groom at the Grand Ballroom reception the night before the shareholders' meeting."},
        ],
        "notes": (
            "Plot use only: the firm exists to justify the Rabinowitz reception, which is the "
            "runners' best chance to walk the Grand Ballroom with the head table already staged "
            "exactly as it will be for DocWagon. Guests bring personal bodyguards (seated together "
            "off to one side) and the family hires private security in evening dress; both carry "
            "light and heavy pistols and other concealable weapons, run on standard archetypes, and "
            "will hand any troublemaker to Lone Star. Some of the guests are DocWagon investors who "
            "will be back the next night, which is a legitimate legwork channel. A firm with this "
            "client list is a standing contact source for corporate paper."
        ),
    },
    {
        "name": "Seattle Federal Savings and Loan",
        "org_type": "corporation",
        "tier": 2,
        "headquarters": "Seattle metroplex",
        "summary": "Metroplex savings and loan whose president, Alan Ginsberg, married his daughter to a senior partner of Howell, Shultz, and Rabinowitz",
        "description": (
            "A Seattle savings and loan of enough standing that its president's daughter's wedding "
            "to a senior corporate lawyer is one of the social events of the year. The book gives "
            "the institution nothing else: it is here as the source of Sarah Ginsberg and of the "
            "money and connections that filled the Grand Ballroom with 500 guests, a live band and "
            "a dance floor the night before the DocWagon shareholders' meeting."
        ),
        "leadership": [
            {"name": "Alan Ginsberg", "title": "President", "notes": "Father of the bride at the Rabinowitz reception."},
        ],
        "notes": (
            "Name-drop with a plot function. A metroplex bank president is a plausible DocWagon "
            "shareholder, a plausible investor in Griffin Biotechnology, and an obvious later "
            "source of financing for anyone building a new medical corporation from nothing -- keep "
            "Ginsberg in reserve for the Rose Croix arc."
        ),
    },
]

LOCATIONS = [
    {
        "name": "The Westin Seattle",
        "location_type": "hotel",
        "city": "Seattle",
        "district": "Downtown (Fifth Avenue and Stewart Street)",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "Westin International Hotel Corporation",
        "summary": "Sixty floors in three towers the locals call the corncobs; headquarters and flagship of Westin International, most meeting space in the metroplex, and the site of the DocWagon hit",
        "description": (
            "One of the finest hotels in Seattle and a common venue for important functions, having "
            "hosted the creme of the city's social scene. Sixty floors in three towers that the "
            "natives have dubbed the corncobs (and less polite things), offering one of the only "
            "unobstructed views of Puget Sound, Lake Union and the downtown core; the upper floors "
            "hold permanent residents living in luxury. Staff in dark blue and gold uniforms hurry "
            "through the public rooms fulfilling guests' whims. Three first-class restaurants -- "
            "Trader Vic's, The Emerald Room and the Elven View -- plus the Lobby Bar and the Fifth "
            "Avenue Corner Cafe. The hotel has the most meeting-room space of any in the metroplex, "
            "spread over three floors: the Grand Level (Grand Ballroom I-III, Grand Foyer, Grand "
            "Crescent, Grand Convention and Registration Offices, Vashon I and II, Banquet Office), "
            "the San Juan Level (Whidbey, Orcas, Blakely, San Juan Foyer), the Mezzanine (Cascade "
            "Ballroom I-II, Cascade Foyer North and South, Glacier Peak, St. Helens, Stuart, Baker, "
            "Adams, Olympic, Stanwood, Emerald City Gallery, Elliott Bay Room, executive offices, "
            "Preferred Guest Desk) and the Lobby (reception, concierge, sundries, shoeshine, the "
            "Fifth Avenue entrance). The Grand Ballroom sits on the fourth floor: 92 by 196 feet, "
            "1,500 seats, a ceiling nearly five metres high, hotel-provided audio and trideo."
        ),
        "notes": (
            "Public data: 'Westin Hotel, Upper-Class Hotel Archetype (60 floors, 3 towers), Fifth "
            "Avenue and Steward Street, Kevin McKeen, Manager, No Racial Bias, LTG# 206 "
            "(52-3587).' (The book prints 'Steward'; the street is Stewart, and the map's own "
            "labels read Fifth Avenue.) PHYSICAL: no walls, fences or wire; plascrete and steel "
            "rebar, Barrier 12; ballistic windows over most of the surface, proof against heavy "
            "pistol calibre and smaller; guest doors the same material, rear and service doors "
            "heavy metal at Barrier 8. TECHNICAL: magnetic anomaly detector (Device Rating 10) in "
            "the main guest door frames for cyberware and firearms -- service entries have none; "
            "hand scanners Rating 5 on security; maglocks Rating 5 with credstick verification "
            "Rating 4, five patterns plus the hotel master, battery backup, front doors seldom "
            "locked; key staff credsticks carry a master code, service staff codes open non-guest "
            "doors; elevators, maglocks, fire control, lighting and HVAC integrated under computer "
            "control; multi-phase power with two hours of emergency lighting. A separately wired "
            "PanicButton network (main desk, maitre d' podiums, bars and other posts, plus personal "
            "transmitters through the guards' transceivers) is contracted to Lone Star: silent "
            "alarm, five combat turns to arrival because the district rates AAA security, contract "
            "pre-approval to take whatever action the threat requires, and authority to enter -- "
            "the hotel is not extraterritorial. Lone Star can also redirect contract guards from "
            "other protected properties nearby. MAGICAL: next to nothing; periodic sweeps, always "
            "before a sensitive event such as this meeting, and a magician on standby for wards and "
            "services -- otherwise guests provide their own watchers, wards and anti-detection "
            "spells, so there is unrelated magic all over the building. Zero Hour: after five "
            "combat turns two Lone Star patrol vehicles plus TR d6 contract guards from nearby "
            "properties arrive; a full Lone Star response team at twelve turns. Hotel and DocWagon "
            "security try to capture, then to herd the runners into the street, and ignore anyone "
            "holding a cover identity who is not shooting. Matrix host in MATRIX_HOSTS."
        ),
    },
    {
        "name": "Fox's Tacoma Safehouse",
        "location_type": "safehouse",
        "city": "Seattle",
        "district": "Northern Tacoma",
        "security_level": "Low Security",
        "summary": "A four-bedroom house indistinguishable from its neighbours, fully stocked, with a ritual attic and a smart-house security system -- and wired end to end with Fox's bugs",
        "description": (
            "A two-storey house in Tacoma's northern section, just like every other house around "
            "it, which is exactly what you want in a safehouse. Four bedrooms, two bathrooms, a "
            "kitchen, a dining room with the hotel ballroom plans spread across the walls, and a "
            "family room with a full telecom entertainment centre. The finished attic above is "
            "large enough for ritual work and has been used routinely for it, particularly for "
            "summoning elementals. The attached two-car garage has room for a few extras. The "
            "refrigerator, pantry, dishes, toiletries and bedding are all stocked, and there are "
            "commlinks laid out for everyone on the team so they can coordinate during the mission. "
            "One of Fox's best safehouses; he is only lending it because the job matters."
        ),
        "notes": (
            "The entertainment and telecom unit is state of the art, carries enough datajacks for "
            "Matrix access, and doubles as the control interface for the whole smart house, "
            "including a Sensors 4 security system and Maglock 6 maglocks on every external door "
            "(the book notes this is higher than normal for a middle-class house here). The entire "
            "house is bugged. Fox knows; the runners must not. The bugs are off when the team first "
            "arrives in case they sweep, go live once everyone has settled in, and go off again the "
            "moment Fox thinks another sweep is coming -- the book instructs the GM that under no "
            "circumstances are the runners to find them. The Ambush! scene lands here: DocWagon "
            "intelligence backtracks the team's legwork (or Davenport tips off Internal Affairs "
            "himself to make the plot look real) and a special ops team comes through the windows "
            "on ropes to take prisoners and floor plans. Optional cruelty: strip out the built-in "
            "security so the runners must supply their own, or have it false-alarm at four in the "
            "morning until they switch it off. Runners return here after the ambulance; Fox waits "
            "half an hour, makes one call, confirms the deaths, hands out cigars and certified "
            "credsticks."
        ),
    },
    {
        "name": "Lake Washington Waterfront Pull-Off",
        "location_type": "meeting site",
        "city": "Seattle",
        "district": "West shore of Lake Washington, just outside downtown",
        "security_level": "Low Security",
        "summary": "The deserted waterfront lay-by just after dusk where Fox lays out the wetwork contract; no cover for eavesdroppers, no room for an ambush",
        "description": (
            "A little pull-off on the waterfront road along the west side of Lake Washington, just "
            "outside downtown, chosen because it is private and open: the road is all but deserted, "
            "the water gives anyone watching from across it nowhere to hide, and the lay-by holds "
            "only a few vehicles, so there is no room to set up an ambush of any kind. Fox arrives "
            "five minutes early in a nondescript Ford Americar, leans on the fender, lights a "
            "cigarette and refuses to talk business until the last runner shows. The nearest bus "
            "station is a quarter mile away, so anyone on public transport walks the last stretch."
        ),
        "notes": (
            "Runners who arrive early to case the spot find nothing, which is the point. Pushing "
            "the envelope: a Lone Star patrol car rounds the bend and an officer strolls over "
            "asking what the gathering is about -- the precinct has had reports of disturbances "
            "down by the lake. Ordinary clothes, no visible hardware and a cool head sends them "
            "away; suspicious behaviour gets licence numbers called in from up the road while they "
            "wait for backup; drawn weapons gets a distress signal and a response team. The scene "
            "is also the table's introduction to itself if the players have not run together "
            "before."
        ),
    },
    {
        "name": "The Kethers Building",
        "location_type": "corporate facility",
        "city": "Seattle",
        "district": "Tacoma (1366 Crescent Boulevard)",
        "security_level": "Corporate High Security",
        "controlling_org": "DocWagon",
        "summary": "DocWagon's Tacoma clone and tissue vault; Davenport's 'deniable assets' rerouted a second Peabody clone out of it, and that clone is the body in the ambulance",
        "description": (
            "The DocWagon Seattle facility that stores the cloned tissue and full-body clones the "
            "franchise maintains for its contract holders, part of the tissue-replacement service "
            "that is one of the three pillars of the standard franchise business alongside "
            "emergency medical care and private clinics. Clones are tagged to their owners; "
            "retagging requires access at the executive level, which Michael Davenport has."
        ),
        "notes": (
            "The heart of the deception. Davenport had his own medical data replaced with Earl "
            "Peabody's and both men's clones retagged, then commissioned a second 'Peabody' clone "
            "on the pretext that the customer wanted a backup shipped to the east coast. As Chief "
            "Operations Officer he routinely worked with the security director on black operations "
            "against Seattle corporations, so he used that same pool of deniable assets to reroute "
            "the clone out of this facility. Dressed in the clothes Davenport wears to the podium "
            "and loaded into a remote-controlled ambulance, it becomes the corpse the DNA and "
            "dental analysis identify as him. A team that investigates the storage records instead "
            "of the hotel can break the whole plot open before zero hour -- the book does not "
            "expect it, so improvise the security. NAMING: Double Cross calls this only "
            "'DocWagon's Tacoma storage facility'; SRM 01-02 Strings Attached names the same site "
            "the Kethers Building at 1366 Crescent Boulevard and details it in full, so the row "
            "carries the later name."
        ),
    },
    {
        "name": "Reynolds Eternal Estates",
        "location_type": "cemetery / memorial park",
        "city": "Seattle",
        "district": "Primrose Boulevard, Bellevue",
        "security_level": "Patrolled / Commercial",
        "summary": "The Bellevue memorial park where DocWagon buries a Fort Lewis car dealer's clone under Michael Davenport's name",
        "description": (
            "A memorial park on Primrose Boulevard in Bellevue. Michael Davenport's remains -- what "
            "the fire left of the clone -- are cremated according to his stated wishes, and the "
            "memorial service is held here on the Saturday after the shareholders' meeting. The "
            "screamsheet notes that Davenport had no remaining relatives or heirs, so the mourners "
            "are DocWagon: Garrett Walsh, the board, Margo Fleming, and whichever shareholders and "
            "metroplex notables think attendance is worth being seen at."
        ),
        "notes": (
            "Not a scene in the book, and all the more useful for it. A memorial with no family, a "
            "cremation that destroys the only physical evidence, and a guest list of every "
            "DocWagon executive in the metroplex is an ideal place to run the aftermath: runners "
            "who suspect the frame can watch who does and does not grieve, and a team that took "
            "the job and is now curious has one afternoon to look at Walsh, Fleming and the board "
            "in the same room. Later chapters of the Rose Croix arc can use the same ground when "
            "Walter Broward's face starts appearing on the trid."
        ),
    },
]

NPCS = [
    {
        "name": "Michael Davenport",
        "role": "Chief Operations Officer of DocWagon Seattle and the true Mr. Johnson -- he hired both teams, faked his own death and walks away as Walter Broward of Rose Croix",
        "archetype": "Corporate Executive",
        "title": "Chief Operations Officer, DocWagon Seattle franchise; afterwards Walter Broward, CEO of Rose Croix",
        "race": "Human",
        "gender": "Male",
        "connection": 4,
        "description": (
            "A distinguished human male with a strong voice that carries over a ballroom of fifteen "
            "hundred without amplification, comfortable at a podium and expert at the corporate "
            "warmth that makes shareholders feel spoken to. In private he is the man who flings a "
            "datapad against his office wall hard enough to shatter it into a hundred pieces the "
            "moment the door closes. His measure of a proposal is two numbers: 'The numbers were "
            "excellent, the risk was small.' To Walsh's face: 'C'mon Garrett, take a chance -- this "
            "is worth millions for god's sake!' On the night, shot and bleeding for the crowd, he "
            "shoves the women away from him and shouts at them to run -- heroism as stagecraft, "
            "played so nobody gets close enough to notice the wounds are dressed."
        ),
        "background": (
            "Davenport and Garrett Walsh were friends early on; two years of refused proposals "
            "strained it past repair. Davenport looks forward -- new markets, drug manufacture, "
            "bioware development, spin-offs from products DocWagon already makes -- and measures "
            "himself in the size of the retirement he is building. He devised the Temporary "
            "Responder Program in 2057 to augment undermanned HTR teams. His last proposal was a "
            "UCAS military pharmaceuticals contract with Fort Lewis as testbed and control centre, "
            "worth millions over four years and biddable directly because DocWagon runs on "
            "franchises with no home office to consult; Walsh killed it on principle. Walsh's own "
            "phrase -- 'we have a virtual monopoly on health care here in the metroplex' -- gave "
            "him the answer: the monopoly is the reason DocWagon will not take risks, so compete "
            "with it. Months of groundwork followed: encrypted caches of customer lists and "
            "security codes hidden through the company, the Peabody records swap and clone "
            "retagging, a second Peabody clone rerouted out of Tacoma storage, and two runner teams "
            "hired for one performance. As COO he had long run deniable black operations against "
            "other Seattle corporations with the security director; he used the same pool."
        ),
        "notes": (
            "No statistics are printed for Davenport -- he never fights and cannot die in this "
            "adventure. Mechanics of the fake: Fox relays the runners' plan and any change to it, "
            "so Davenport counters it by mundane means wherever possible, keeping magical detection "
            "clean; where magic is unavoidable, a shadowrunner mage seeded in the audience knows "
            "the trigger phrase and casts sustained illusions and protection only segments before "
            "the attack. If the runners approach the stage, a panicked would-be hero's stray shot "
            "'hits' him to make the wound convincing. The extraction team keeps him alive through "
            "any real damage. He also arranges to be discovered: if he thinks DocWagon will not "
            "believe the assassination, he has someone loyal tip off Internal Affairs, which "
            "produces the safehouse ambush. Aftermath: declared dead, cremated, no relatives or "
            "heirs; weeks of reconstructive surgery (street gossip says the Carib League) and he "
            "returns as Walter Broward, CEO of Rose Croix. He is the arc villain and, for a team "
            "that ever works out what it did, the most dangerous man it has ever been paid by."
        ),
        "contact_skills": ["DocWagon Seattle operations, clinics and HTR dispatch", "Corporate black operations and deniable assets in the metroplex"],
    },
    {
        "name": "Garrett Walsh",
        "role": "Chief Executive Officer of DocWagon Seattle -- the cautious boss whose refusals set the whole plot in motion, and who eulogises the man who robbed him",
        "archetype": "Corporate Executive",
        "title": "Chief Executive Officer, DocWagon Seattle franchise",
        "race": "Human",
        "gender": "Male",
        "organization": "DocWagon",
        "connection": 4,
        "description": (
            "Works from behind a desk with quarterly projections hanging in xenon mist between "
            "holoprojectors, and comes around it to greet a visitor rather than making them stand. "
            "Opens with 'OK, Michael, what do you have for me today?' and delivers bad news slowly "
            "enough that you hear it coming: 'Interesting, very interesting. Well, Michael, you've "
            "certainly done your homework... But...' Conservative by conviction rather than "
            "timidity -- 'you know my position on defense contracts as it is, and we do have a "
            "public image to uphold, whether you agree with it or not.' Patient with Davenport's "
            "outbursts; lets him walk out of the office without a word."
        ),
        "background": (
            "Friends with Davenport early on, boss and obstacle later. Walsh runs the Seattle "
            "franchise on the standard business -- emergency medical care, private clinics, tissue "
            "replacement for contract holders -- and on the argument that DocWagon's virtual "
            "monopoly on metroplex health care plus steadily rising shares since the Redmond crash "
            "of '59 means there is nothing to gain by gambling. He is not a blanket obstructionist "
            "and says so: he approved the Snohomish production facility a month earlier and the "
            "Griffin Biotechnology purchase is 'looking promising as well'. What he will not do is "
            "defense work, whatever the margin, and he will not spend the company's public image on "
            "it."
        ),
        "notes": (
            "No statistics; Walsh never appears on stage in the adventure. He gives the first of "
            "the three speeches at the shareholders' meeting -- 'his vision for changes in the "
            "coming year' -- and introduces the head table before the CFO and then Davenport, so "
            "he is in the room and in the line of fire when the runners open up. Aftermath: he is "
            "the quoted mourner on the KSEA screamsheet ('The loss of Michael Davenport is one that "
            "will be felt throughout the company. He was a devoted employee and close personal "
            "friend...'). Street gossip on the same handout claims Walsh had been trying to rein "
            "Davenport in and was about to ask him to step down as COO, which if true means "
            "Davenport jumped days before he was pushed. Walsh will spend the Rose Croix arc "
            "watching a new competitor turn up knowing everything about his company."
        ),
        "contact_skills": ["DocWagon Seattle corporate policy and board politics"],
    },
    {
        "name": "Dr. Chandra Dasari",
        "role": "Griffin Biotechnology's lead neurology researcher, presented to the shareholders under bodyguard moments before the shooting starts",
        "archetype": "Corporate Scientist",
        "title": "Lead researcher in neurology, Griffin Biotechnology",
        "race": "Human",
        "gender": "Female",
        "nationality": "Indian",
        "organization": "Griffin Biotechnology",
        "connection": 3,
        "description": (
            "A mousy woman of Indian descent who stands up at one of the round tables near the "
            "stage when Davenport calls her name, waves once to fifteen hundred applauding "
            "shareholders and sits down again as fast as courtesy allows. Her two 'dates' are "
            "obviously bodyguards, and the tension coming off them while she is on her feet is "
            "almost tangible -- the clearest signal in the room of how much DocWagon values her."
        ),
        "background": (
            "One of the leading authorities on neurology and a pioneer in her field. Her research "
            "redirects healthy brain tissue to compensate for damaged tissue, which promises "
            "treatment for certain types of epilepsy and, more valuably to a medical corporation, "
            "new knowledge of how motor skills work and of how those areas of the brain integrate "
            "with cultured tissue and cybernetic systems. She came to DocWagon with the small "
            "Seattle firm Griffin Biotechnology earlier in the quarter; DocWagon and co-investors "
            "bought the firm and funded a new Everett facility for her, and she is close to human "
            "trials. Davenport was to announce her and her programme at the shareholders' meeting, "
            "and does."
        ),
        "notes": (
            "No statistics. Dasari's introduction is the runners' cue -- the trigger phrase follows "
            "two sentences later. Her bodyguards will draw and cover her but, like every personal "
            "bodyguard in the room, will not fire on the runners unless someone threatens them or "
            "their charge. Aftermath: a scientist whose corporate patron has just lost the "
            "executive who championed her, with an unopened lab, unstarted human trials, and a "
            "brand-new medical corporation about to appear in the metroplex looking for exactly her "
            "expertise. The book leaves her alive and available; the Rose Croix arc gives an "
            "obvious reason to come back for her."
        ),
        "contact_skills": ["Neurology, cultured neural tissue and cybernetic integration research"],
    },
    {
        "name": "Margo Fleming",
        "role": "DocWagon Seattle's Vice President of Marketing and Davenport's personal assistant -- the one person who runs toward him when he falls",
        "archetype": "Corporate Executive",
        "title": "Vice President of Marketing, DocWagon Seattle; Michael Davenport's personal assistant",
        "race": "Human",
        "gender": "Female",
        "organization": "DocWagon",
        "connection": 3,
        "description": (
            "Seated at the head table with the officers of the franchise. When the shooting starts "
            "and most of the table dives for cover, Fleming is the one who rushes to Davenport's "
            "side to attend to him -- and gets shoved away and shouted at for her trouble, because "
            "the last thing Davenport can afford is somebody competent looking closely at his "
            "wounds."
        ),
        "background": (
            "Marketing officer and personal assistant to the COO, which in a franchise this size "
            "means she has handled his public face, his itinerary and the presentation of the "
            "Griffin partnership. The book gives her no history beyond her title and her one "
            "action, but her position makes her the person most likely to have noticed the months "
            "of quiet preparation Davenport made before his death -- and the person the runners can "
            "most usefully find afterwards."
        ),
        "notes": (
            "No statistics. Sole scene: the head table at zero hour, where she and Davenport's "
            "personal assistant are pushed aside first by him and then physically by the incoming "
            "HTR team. If the runners are approaching the stage she is between them and the target. "
            "Aftermath hook: she is a DocWagon insider with a dead boss, a grievance and access to "
            "his files -- the natural first contact for anyone in the Rose Croix arc who wants to "
            "prove what happened, and a natural early recruit for Walter Broward if he decides he "
            "needs someone inside his old company."
        ),
        "contact_skills": ["DocWagon Seattle marketing, executive itineraries and press handling"],
    },
    {
        "name": "Kevin McKeen",
        "role": "Manager of the Westin Seattle -- the man whose staff can be bribed, whose maglocks are Rating 5 and whose PanicButton brings Lone Star in five turns",
        "archetype": "Corporate Manager",
        "title": "Manager, the Westin Seattle",
        "race": "Human",
        "gender": "Male",
        "organization": "Westin International Hotel Corporation",
        "connection": 2,
        "description": (
            "A name on the hotel's public data entry rather than a character the book puts on "
            "stage: 'Westin Hotel, Upper-Class Hotel Archetype (60 floors, 3 towers), Fifth Avenue "
            "and Steward Street, Kevin McKeen, Manager, No Racial Bias.' He runs the flagship and "
            "headquarters of Westin International, which means he answers to the corporation for a "
            "building full of megacorp presidents, permanent residents and the biggest wedding of "
            "the year, and he is the executive who will be explaining a firefight in his Grand "
            "Ballroom."
        ),
        "background": (
            "Manager of a hotel that hosts the creme of Seattle society and the most meeting-room "
            "space in the metroplex. His policy decisions are all over the scenario: hired security "
            "trained and licensed by larger firms rather than an in-house force; a magical sweep "
            "commissioned before any sensitive event; a magician kept on standby for guests who "
            "need wards; a Lone Star PanicButton contract with pre-approved authority to act; and "
            "an underpaid, barely trained service staff kept loyal by the fact that it is a steady "
            "job in a nice place to work."
        ),
        "notes": (
            "No statistics. McKeen is the escalation the GM reaches for when the runners are "
            "conspicuous rather than violent: the guest asked politely to step aside for the hand "
            "scanner, the difficult patron invited to leave during a Matrix shutdown ('the Westin "
            "has no shortage of patrons, and they know who they should not anger, who is important, "
            "and who is... not'), the decision to raise security for six hours after an alert. He "
            "is also the obvious target for a bribe or a blackmail: he is management, which the "
            "book says resists such tactics, but he alone can put a name on the catering roster "
            "without touching the Matrix host at all."
        ),
        "contact_skills": ["Westin Seattle staffing, event bookings and floor access"],
    },
    {
        "name": "Vincent \"Numbers\" Ciarniello",
        "role": "The longest-serving Mafia don in Seattle -- an accountant at heart who plays the market and wants advance warning of what is about to happen to DocWagon stock",
        "archetype": "Crime Boss",
        "title": "Don, Seattle Mafia",
        "race": "Human",
        "gender": "Male",
        "organization": "Seattle Mafia",
        "connection": 5,
        "description": (
            "Arrives as a black Mitsubishi Nightsky that seems to swallow the surrounding light, "
            "with a rear door that opens by itself and a low voice from inside: 'Get in, we need to "
            "talk...' Inside is a richly appointed limousine, a seat facing the don, and two large "
            "ork bodyguards cybered to the gills on either side of the guest. He has been a don "
            "longer than anyone else in the city and is a smart man, but at heart he is an "
            "accountant, and he enjoys the stock market most when he knows what is coming."
        ),
        "background": (
            "The senior don of the Seattle Mafia by tenure. His interest in Double Cross is "
            "financial rather than territorial: word has reached the street that a major run is "
            "about to be made against DocWagon, one that could move the share price, and Ciarniello "
            "wants to know which way before the market does. The introduction is always made "
            "'through the grapevine', which leaves the runners free to wonder which of their own "
            "contacts sold them."
        ),
        "notes": (
            "No statistics. He is the Insider Trading host matched to runners with Mafia contacts. "
            "Cooperative, respectful answers -- true or not -- earn thanks, a drop at the next free "
            "parking spot and possibly a 1,000 nuyen gratuity; the runner with the best Etiquette "
            "should do the talking. Refusing the invitation gets a second, gentler warning about "
            "not making a scene, then operatives on the sidewalk who stick the runner with "
            "gamma-scopolamine or a rooftop round of the same while two heavies bundle them through "
            "the door -- the interview then happens under a truth drug, and there is no gratuity "
            "for the impolite. Aftermath: whatever the runners say, a Mafia don now knows their "
            "faces and that they were involved in the DocWagon killing."
        ),
        "contact_skills": ["Seattle Mafia business and market interests", "Corporate stock movements and who is about to move them"],
    },
    {
        "name": "Drew Hollingsworth",
        "role": "Wealthy socialite and adventurer with an uncanny nose for corporate trouble; senses that DocWagon's management is about to change and wants to know how",
        "archetype": "Socialite",
        "title": "Socialite, adventurer and investor",
        "race": "Human",
        "gender": "Male",
        "connection": 4,
        "description": (
            "A wealthy socialite and adventurer known around the metroplex as a shrewd "
            "businessman -- one who always seems able to smell trouble brewing in a company before "
            "anyone else does. He is convinced something is about to change the management of "
            "DocWagon and has arranged, in the usual black Nightsky with the usual ork bodyguards, "
            "to ask the people who would know. Charming about it; the coercion is only for people "
            "who decline."
        ),
        "background": (
            "The book raises and immediately half-closes the interesting possibility: it could be "
            "that Hollingsworth has some magical talent for precognition, but if so it is an innate "
            "ability and he does not detect as magical. Nothing else of his history is given -- no "
            "corporation, no syndicate, no source of the fortune -- which leaves a rich, "
            "well-connected man with an unexplained gift and a habit of turning up just before "
            "things happen."
        ),
        "notes": (
            "No statistics. The Insider Trading host matched to runners with high-society contacts; "
            "same mechanics and the same 1,000 nuyen gratuity. Of the four he is the most useful to "
            "keep: a socialite with an unexplained talent for sensing corporate upheaval is a "
            "recurring contact, a recurring warning system and, if the GM wants him to be, "
            "something considerably stranger. He is also the one host who cannot be traced to an "
            "organisation afterwards, so runners who talk to him have no idea who they talked to."
        ),
        "contact_skills": ["Seattle high society and its gossip", "Investor sentiment and impending corporate upheaval"],
    },
    {
        "name": "Levi Rabinowitz",
        "role": "Senior partner of Howell, Shultz, and Rabinowitz, whose wedding reception fills the Grand Ballroom the night before the hit",
        "archetype": "Corporate Lawyer",
        "title": "Senior partner, Howell, Shultz, and Rabinowitz",
        "race": "Human",
        "gender": "Male",
        "organization": "Howell, Shultz, and Rabinowitz",
        "connection": 3,
        "description": (
            "The groom, and at his own reception the man everyone wants a word with. The book uses "
            "him mainly as a hazard: a family member latches onto any runner who has talked their "
            "way in as a guest and starts hunting for a shared past, ending in a bellowed 'HEY "
            "LEVI, COME SAY HELLO TO ONE OF YOUR COLLEGE BUDDIES!!' across a room of five hundred "
            "people the runner very much did not want to be looked at by."
        ),
        "background": (
            "A senior partner at one of the most prestigious corporate law firms in the metroplex, "
            "newly married to Sarah Ginsberg, daughter of the president of Seattle Federal Savings "
            "and Loan. The match of a top corporate lawyer to a banking family produced one of the "
            "biggest weddings of the year: 500 guests, a live band, a dance floor, megacorp "
            "presidents and senior officials, the best of Seattle society and celebrities from "
            "music, trideo and sport, in a Grand Ballroom laid out exactly as DocWagon will have it "
            "the next night."
        ),
        "notes": (
            "No statistics. The Rabinowitz Reception is a casing opportunity dressed as a social "
            "trap. Runners posing as hotel staff get treated as invisible people by guests who "
            "expect servants to be invisible -- fetching drinks, absorbing complaints, being made "
            "to spill a tray over a simsense starlet's new dress. Runners who wrangle an invitation "
            "get the run of the hall and the shared-past interrogation above. Bodyguards sit "
            "together off to one side, hired security stands unobtrusively around the walls, and "
            "all of them carry concealable light and heavy pistols; violence here brings hotel "
            "security, the wedding's own guards and Lone Star down at once. Some guests are "
            "DocWagon investors who will return the following night, which is a legitimate legwork "
            "channel."
        ),
        "contact_skills": ["Corporate law and metroplex contract paper", "Seattle high society"],
    },
    {
        "name": "Sarah Rabinowitz",
        "role": "The bride -- Sarah Ginsberg of the Seattle Federal Savings and Loan family, married to Levi Rabinowitz the night before the shareholders' meeting",
        "archetype": "Socialite",
        "title": "Daughter of Alan Ginsberg, president of Seattle Federal Savings and Loan",
        "race": "Human",
        "gender": "Female",
        "organization": "Seattle Federal Savings and Loan",
        "connection": 2,
        "description": (
            "The bride at the biggest wedding of the year and the reason half of Seattle's money is "
            "standing in the Grand Ballroom the night before the DocWagon meeting. The book gives "
            "her the marriage and nothing else, but the guest list is her family's as much as her "
            "husband's -- banking on one side of the room and corporate law on the other."
        ),
        "background": (
            "Daughter of Alan Ginsberg, president of Seattle Federal Savings and Loan, married to "
            "Levi Rabinowitz, senior partner at Howell, Shultz, and Rabinowitz. The result is one "
            "of the biggest weddings and one of the biggest social events of the year, supported by "
            "about 500 guests with a live band and a dance floor."
        ),
        "notes": (
            "No statistics and no lines. She is here because the campaign is generous with named "
            "people and because a bride is the one person at the reception whom every guest will "
            "stop and speak to, which makes her a hazard to a runner working the room in a waiter's "
            "jacket and an asset to a runner who has talked their way in as a guest. The wedding "
            "party's own hired security answers to her family."
        ),
    },
    {
        "name": "Alan Ginsberg",
        "role": "President of Seattle Federal Savings and Loan and father of the bride",
        "archetype": "Corporate Executive",
        "title": "President, Seattle Federal Savings and Loan",
        "race": "Human",
        "gender": "Male",
        "organization": "Seattle Federal Savings and Loan",
        "connection": 3,
        "description": (
            "The father of the bride at the Rabinowitz reception, and the reason there are bank "
            "presidents and their bodyguards among the megacorp officials in the Grand Ballroom. "
            "The book never puts him on stage; he is a name attached to a fortune and a guest list."
        ),
        "background": (
            "President of Seattle Federal Savings and Loan. His daughter Sarah's marriage to a "
            "senior partner of Howell, Shultz, and Rabinowitz joined a banking family to one of the "
            "metroplex's most prestigious corporate law firms, which is why the reception drew "
            "presidents and senior officials from megacorps and large companies as well as society "
            "and celebrities."
        ),
        "notes": (
            "No statistics. Plot use is entirely indirect: he explains the calibre of the guests "
            "the runners are casing the room among, and he is a plausible DocWagon shareholder who "
            "will be back the following night. For the arc, a metroplex banking president with a "
            "new son-in-law in corporate law is exactly the sort of person a man building a medical "
            "corporation out of nothing needs to know -- keep him for later."
        ),
        "contact_skills": ["Metroplex banking and commercial lending"],
    },
    {
        "name": "Earl Peabody",
        "role": "Fort Lewis car dealer of Davenport's build whose medical records, clone tags and second clone were quietly appropriated to provide a corpse",
        "archetype": "Businessman",
        "title": "Owner of a successful car dealership in Fort Lewis",
        "race": "Human",
        "gender": "Male",
        "description": (
            "The owner of a very successful car dealership in Fort Lewis, whose only qualification "
            "for a role in this plot is that he has the same physical build and general "
            "characteristics as Michael Davenport. He almost certainly has no idea that his medical "
            "file has been swapped, his clone retagged, and a second clone commissioned in his name "
            "and shipped out of DocWagon's Tacoma storage on a pretext."
        ),
        "background": (
            "A DocWagon contract holder prosperous enough to keep a full-body clone in storage -- "
            "the tissue-replacement service is one of the three pillars of the franchise business. "
            "A week before the shareholders' meeting Davenport had his own medical data replaced "
            "with Peabody's and both men's clones retagged, then ordered a second 'Peabody' clone "
            "on the story that the customer wanted a backup shipped to the east coast. That second "
            "clone is dressed as Davenport and put in the ambulance."
        ),
        "notes": (
            "No statistics and no scene. Peabody is the loose thread the book leaves lying in the "
            "open: DNA analysis and dental records 'confirmed the identities of those found in the "
            "vehicle', which they could only do because Davenport's records are now Peabody's and "
            "vice versa. That means Earl Peabody's medical file currently identifies him as a dead "
            "man, and any team, insurer, coroner or Lone Star investigator who compares the "
            "DocWagon storage records against the autopsy has the whole conspiracy. A car dealer in "
            "Fort Lewis who suddenly cannot get medical service, or who is quietly killed to close "
            "the gap, is a ready-made opening for a later chapter of the arc."
        ),
    },
    {
        "name": "Kyle Matthews",
        "role": "Dwarf paramedic and support gunner of DocWagon HTR team #27 out of Renton -- murdered so his team's ambulance and gear could be used for the extraction",
        "archetype": "Paramedic",
        "title": "Paramedic and support gunner, DocWagon High Threat Response team #27 (Renton)",
        "race": "Dwarf",
        "gender": "Male",
        "organization": "DocWagon",
        "connection": 2,
        "description": (
            "Known on the boards through his friend Penny Ante as 'a damn good paramedic and "
            "support gunner to boot' -- and, crucially, a dwarf. None of the witnesses at the "
            "Westin remember seeing a dwarf among the HTR team that came onto the stage to recover "
            "Davenport's body, which is the single hardest piece of evidence in the adventure that "
            "the rescuers were not DocWagon at all."
        ),
        "background": (
            "Grew up with the poster who calls herself Penny Ante and has not missed meeting her "
            "during his down time since he started shift work with the HTR teams two years ago. "
            "They talked just before his last duty cycle and made plans for after his release. That "
            "meeting was three days ago and he never came. DocWagon HTR team #27 out of Renton "
            "never reported back from its last night of detail; the investigation had not reached "
            "upper management by the time of the shareholders' meeting, and it was only after the "
            "reports were filed that a duty officer noticed the names."
        ),
        "notes": (
            "No statistics; Matthews is dead before the adventure opens. The extraction team "
            "neutralised HTR team #27 to obtain a genuine DocWagon ambulance, uniforms and "
            "equipment -- Davenport reasoned that having the real crew's bodies inside would add to "
            "the authenticity, and arranged that their corporate bracelets would not register in "
            "the dispatch system until he wanted them to. The screamsheet reports 'the charred "
            "remains of all four HTR team members and Michael Davenport' recovered and identified "
            "(the book's DocWagon Special Ops stat block is written for six -- a printing "
            "inconsistency). Matthews is the campaign's built-in loose end and the reason the "
            "street does not believe the official story: a team that wants to know what it really "
            "did should start with him."
        ),
    },
    {
        "name": "Yolanda",
        "role": "Garrett Walsh's executive assistant -- the last friendly face Davenport passes on the way to the meeting that decides everything",
        "archetype": "Corporate Aide",
        "title": "Executive assistant to the CEO, DocWagon Seattle",
        "race": "Elf",
        "gender": "Female",
        "organization": "DocWagon",
        "connection": 2,
        "description": (
            "Sits outside Garrett Walsh's office and greets Davenport with a beaming smile and "
            "sparkling violet eyes as she waves him through into the inner office; he salutes her "
            "with a wave of the hand as he passes. Half a page later he is smashing a datapad "
            "against his own wall, and she is the only person in the building who saw him go in "
            "whole."
        ),
        "background": (
            "Executive assistant to the CEO of DocWagon's Seattle franchise, which means she "
            "controls the diary of the one man in the metroplex whose signature Davenport needed "
            "and could not get. The book gives her one sentence and no surname; the violet eyes are "
            "the only physical detail printed, and are the reason this row records her as an elf."
        ),
        "notes": (
            "No statistics; a prologue-only appearance. Kept as a row because she is a named person "
            "with a place, and because a CEO's executive assistant is one of the most valuable "
            "low-level contacts in a corporate building: she knows who saw Walsh, when, and how "
            "they looked coming out. Anyone reconstructing Davenport's last months inside DocWagon "
            "goes through Yolanda's calendar."
        ),
        "contact_skills": ["DocWagon Seattle executive schedules and who met whom"],
    },
]

ORG_UPDATES = {
    "DocWagon": {
        "notes_append": (
            "SRM 01-01 Double Cross (Seattle, 2060s): DocWagon Seattle is an individual franchise "
            "with no home office to answer to, free to bid on contracts itself, and holds what its "
            "own CEO calls 'a virtual monopoly on health care here in the metroplex' -- neither "
            "megacorps nor small firms seriously contest the market, because DocWagon's volume and "
            "low overhead undercut them all. The standard franchise business is emergency medical "
            "care, private clinics and tissue replacement (full-body clones in storage) for "
            "contract holders; shares have risen steadily since the Redmond crash of '59. "
            "Officers: CEO Garrett Walsh, COO Michael Davenport, a CFO (unnamed), VP of Marketing "
            "Margo Fleming. Davenport devised the Temporary Responder Program in 2057 to augment "
            "undermanned High Threat Response teams -- the extraction team in this adventure wears "
            "TRP-pattern uniforms and equipment. As COO, Davenport routinely ran deniable "
            "black operations and datasteals against other Seattle corporations with the security "
            "director, and used that same pool of assets against his own employer. Facilities in "
            "play: the destroyed Snohomish production plant (supply contracts with Seattle General "
            "Hospital and the university clinic), the Tacoma clone-storage facility, and Griffin "
            "Biotechnology's unopened Everett lab (Knight Errant contract). HTR team #27 out of "
            "Renton was murdered for its ambulance and gear and never reported back from its last "
            "night of detail; corporate bracelets can be kept from registering in the dispatch "
            "system by an executive who wants a delay. DocWagon intelligence and 'independent "
            "contractors' backtrack shadowrunner legwork well enough to raid a safehouse. "
            "DocWagon Special Ops stat block p.26: B5 Q6 S6 C3 I5 W5, Ess 0.9, Reaction 5(10), "
            "Init 5+1d6 [10+3d6], Combat Pool 9, Karma Pool TR, Professional Rating 4; smartlink, "
            "hearing damper, datajack, cybereyes (flare compensation, rangefinder, thermographic), "
            "headware radio with Comlink-IV and Crypto-3, Wired Reflexes 2; Assault Rifles 3, "
            "Pistols 5, Unarmed 3, Armed Combat (Club) 2(4), Throwing 4, Launch Weapons "
            "(Launchers) 2(4), SMG 5, Athletics 3, Stealth 4, Etiquette 2, Intimidation 4, "
            "Interrogation 4, Electronics 3; DocWagon Operational Procedures 4, Security "
            "Procedures 4, Shadowrunner Tactics 3; light security armour with helmet (7/6); Ares "
            "Predator II (7M Stun, gel), Ares ELD-AR (10S, gamma-scopolamine rounds), AZ-150 stun "
            "baton (8S Stun), two flash-bang grenades (12S Stun, flash). Aftermath: the COO is "
            "dead on paper, cremated with no relatives or heirs, and the man who stole the "
            "company's customer lists and security codes is about to open a competitor."
        ),
        "leadership_add": [
            {"name": "Garrett Walsh", "title": "Chief Executive Officer, DocWagon Seattle", "notes": "Conservative; refuses defense contracts; approved Snohomish and Griffin."},
            {"name": "Michael Davenport", "title": "Chief Operations Officer, DocWagon Seattle", "notes": "Faked his own death at the 2060s shareholders' meeting; becomes Walter Broward of Rose Croix."},
            {"name": "Margo Fleming", "title": "Vice President of Marketing; personal assistant to the COO", "notes": "Rushes to Davenport when he falls."},
        ],
        "enemies_add": ["Rose Croix", "Paladin Medical Technologies"],
        "allies_add": ["Griffin Biotechnology", "Knight Errant Security Services"],
    },
    "Lone Star Security": {
        "notes_append": (
            "SRM 01-01 Double Cross (Seattle, 2060s): the Westin Seattle carries a separately wired "
            "PanicButton contract with Lone Star covering the main desk, restaurant maitre d' "
            "podiums, bars and other posts, plus personal transmitters triggered through hotel "
            "security's transceivers. It is a silent alarm; response arrives in five combat turns "
            "because downtown rates AAA security, and the contract grants Lone Star pre-approval to "
            "take whatever action the threat requires. Lone Star can also reroute contract guards "
            "from other stores, hotels and protected properties in the area -- at the shareholders' "
            "meeting, two patrol vehicles plus TR d6 redirected contract guards arrive after five "
            "combat turns and a full response team after twelve. The hotel is not extraterritorial, "
            "so Lone Star enters and works the ground without waiting to be invited. Elsewhere: a "
            "patrol car checks out reported disturbances on the Lake Washington waterfront road and "
            "will run licence plates on anyone who behaves oddly; the crime hotline in the "
            "screamsheet is LTG 206 5-CRIME (52-7463); and Lone Star closes the Davenport "
            "assassination with no leads and no information, which is exactly how Davenport wanted "
            "it. Runners caught inside the hotel are handed to Lone Star by hotel, wedding and "
            "DocWagon security alike."
        ),
    },
    "Knight Errant Security Services": {
        "notes_append": (
            "SRM 01-01 Double Cross (Seattle, 2060s): Knight Errant holds the security contract on "
            "Griffin Biotechnology's new, not-yet-opened research facility in Everett, built with "
            "DocWagon capital for Dr. Chandra Dasari's neurology programme. Someone infiltrated the "
            "site days before the adventure and, the prologue notes, 'learned very little about the "
            "research being conducted on DocWagon's behalf' -- the book credits Knight Errant's "
            "presence with that failure. The intruders are never identified."
        ),
    },
    "Yamatetsu Corporation": {
        "notes_append": (
            "SRM 01-01 Double Cross (Seattle, 2060s): Yamatetsu, in cooperation with AG Chemie of "
            "Europe and the Seattle biotech firm Paladin Medical Technologies, won the UCAS "
            "military pharmaceuticals contract that DocWagon's COO Michael Davenport had spent two "
            "weeks preparing to bid for -- drugs to enhance combat troops and chemical compounds "
            "for use against paranormals, with Fort Lewis chosen as testbed and control centre and "
            "millions of nuyen over four years at stake. The partnership is 'making money hand over "
            "fist', and the contract is the only thing keeping Paladin afloat. Losing this bid, "
            "because his CEO would not touch defense work, is the immediate cause of everything "
            "Davenport does in this adventure."
        ),
        "allies_add": ["Paladin Medical Technologies"],
    },
    "Seattle Mafia": {
        "notes_append": (
            "SRM 01-01 Double Cross (Seattle, 2060s): Vincent 'Numbers' Ciarniello has been a don "
            "longer than anyone else in the city -- a smart man but an accountant at heart, who "
            "enjoys playing the stock market most when he has information ahead of an important "
            "market fluctuation. He travels in a black Mitsubishi Nightsky with heavily cybered ork "
            "bodyguards, hears about shadowruns 'through the grapevine', and picks runners up off "
            "the street to ask what is about to happen to a share price. Politeness earns a 1,000 "
            "nuyen gratuity and a lift; refusal earns a gamma-scopolamine dart from a passer-by or "
            "a rooftop sniper and an interview under a truth agent."
        ),
        "leadership_add": [
            {"name": "Vincent \"Numbers\" Ciarniello", "title": "Don (longest-serving in Seattle)", "notes": "Accountant by temperament; trades on advance knowledge of corporate upheaval."},
        ],
    },
    "Yakuza (Watada-rengo)": {
        "notes_append": (
            "SRM 01-01 Double Cross (Seattle, 2060s) DISCREPANCY / cross-reference: a decade on "
            "from the earlier books, Shadowrun Missions Season One names the Seattle syndicate the "
            "Shotozumi-rengo, with a sokaiya branch under the oyabun's cousin Toju Shotozumi "
            "handling all dealings with local corporations and businesses -- deciding which stocks "
            "to buy and which corporations to apply leverage to. The Watada-rengo is never "
            "mentioned. Earlier canon stands as written; the Shotozumi-rengo is recorded as its own "
            "row for the later period rather than rewriting this one."
        ),
        "allies_add": ["Shotozumi-rengo"],
    },
    "Griffin Biotechnology": {
        "description_append": (
            "SRM 01-01 Double Cross: Double Cross gives the corporation's origin story from "
            "DocWagon's side. 'Earlier this quarter, we were approached by a small biotechnology "
            "research and development firm here in Seattle. After examining their operations and "
            "current progress in certain projects, we decided to join with a few other investors "
            "in purchasing the firm and lending the capital needed to construct a new "
            "state-of-the-art facility to continue their research.' The lead researcher named in "
            "this book is Dr. Chandra Dasari, 'one of the leading authorities on neurology and a "
            "pioneer in her field', whose work redirects healthy brain tissue to compensate for "
            "damaged tissue -- promising treatment for certain types of epilepsy and, more "
            "valuably to a medical corporation, new knowledge of how motor skills work and of how "
            "those areas of the brain integrate with cultured tissue and cybernetic systems. She "
            "is close to beginning human trials."
        ),
        "notes_append": (
            "SRM 01-01 Double Cross: Griffin is the one diversification DocWagon CEO Garrett Walsh "
            "approved and the proposal he sat on longest, which Michael Davenport resented on both "
            "counts. Davenport was to announce the partnership and the doctor at the annual "
            "shareholders' meeting, and does -- the introduction of Dr. Dasari is the cue two "
            "sentences before the trigger phrase the runners are waiting for, and the presence of "
            "a guarded VIP scientist in the front rows is why the Westin commissions a magical "
            "sweep before the event. DocWagon assigns her two bodyguards, who attend the meeting "
            "as her 'dates' and whose tension while she stands to wave is visible across the room. "
            "The Everett facility had not opened yet, and when somebody infiltrated it days before "
            "the adventure they learned very little about the research being conducted on "
            "DocWagon's behalf -- Knight Errant was already in place. The intruders are never "
            "identified. DISCREPANCY: this book's lead neurology researcher is Dr. Chandra Dasari; "
            "SRM 00-03 FORCEd Recon and SRM 01-04 The Gambler give the identical research, the "
            "identical role and the identical shareholders'-meeting announcement to Dr. Indira "
            "Chontel. Both rows are kept and cross-referenced rather than merged."
        ),
        "leadership_add": [
            {"name": "Dr. Chandra Dasari", "title": "Lead researcher (neurology)", "notes": "Named in SRM 01-01 only; about to begin human trials. See the Dr. Indira Chontel discrepancy."},
        ],
        "allies_add": ["DocWagon", "Knight Errant Security Services"],
    },
    "Paladin Medical Technologies": {
        "description_append": (
            "SRM 01-01 Double Cross: by the time of the DocWagon shareholders' meeting Paladin has "
            "found its way out of the contract famine that drove the Snohomish job -- in "
            "partnership with Yamatetsu and AG Chemie of Europe it has won the UCAS military "
            "pharmaceuticals contract that DocWagon's COO Michael Davenport spent two weeks "
            "preparing to bid for, with Fort Lewis as the testbed and control centre. The "
            "partnership is 'making money hand over fist'. Davenport's sources add the sting: that "
            "contract is the only thing keeping Paladin afloat. The book still calls Paladin 'a "
            "leader in biotechnology products here in Seattle' and notes that DocWagon is "
            "simultaneously its major customer and its competitor on some levels."
        ),
        "notes_append": (
            "SRM 01-01 Double Cross: Dr. Fredericks is one of the four possible hosts of the "
            "Insider Trading scene -- the one matched to runners with corporate contacts. He picks "
            "a runner up in a black Mitsubishi Nightsky, seats them between heavily cybered ork "
            "bodyguards and asks what is about to happen to DocWagon; cooperative and polite "
            "answers (true or not) earn thanks, a drop at the next free parking spot and possibly a "
            "1,000 nuyen gratuity, while refusal earns a gamma-scopolamine dart from a passer-by or "
            "a rooftop sniper and an interview under a truth agent with no gratuity at the end. "
            "Continuity note for the GM: the players have no way to know it, but SRM 00-02 "
            "established that Paladin's own deniable contractors levelled DocWagon's Snohomish "
            "plant. In 01-01 that destruction is reported only as something that happened 'a few "
            "weeks ago', it has cost DocWagon six months of production and forced it back to "
            "outside vendors at raised prices -- Paladin among them -- and nobody in the adventure "
            "names a culprit. A corporation living on a single defense contract is also the most "
            "obvious early acquisition target for the new medical corporation about to appear."
        ),
        "allies_add": ["Yamatetsu Corporation"],
        "enemies_add": ["DocWagon"],
    },
    "Shotozumi-rengo": {
        "notes_append": (
            "SRM 01-01 Double Cross (Seattle, 2060s): the adventure touches one arm of the "
            "syndicate, the sokaiya -- the branch that handles the yakuza's dealings with local "
            "corporations and businesses -- under Toju Shotozumi, the oyabun's cousin. Sokaiya work "
            "is deciding which stocks to buy and which corporations to apply leverage to for the "
            "highest profit, so an assassination that will move DocWagon's share price is directly "
            "its business. Toju hears about the run 'through the grapevine', travels in a black "
            "Mitsubishi Nightsky with heavily cybered ork bodyguards, and picks runners up off the "
            "street for an interview: courtesy earns a 1,000 nuyen gratuity and a lift, refusal "
            "earns gamma-scopolamine from a passer-by or a rooftop sniper and questioning under a "
            "truth agent. Of the four Insider Trading hosts the sokaiya is the one most able to act "
            "on what it learns -- it can buy into DocWagon before the news breaks and into Rose "
            "Croix afterwards. DISCREPANCY / cross-reference: the campaign's earlier Seattle yakuza "
            "row is Yakuza (Watada-rengo), which this book never mentions; both rows are kept and "
            "cross-referenced rather than reconciled."
        ),
        "leadership_add": [
            {"name": "Toju Shotozumi", "title": "Head of the sokaiya; cousin of the oyabun", "notes": "Strong business skills; buys into and applies leverage to metroplex corporations."},
        ],
    },
    "Seattle Metroplex Guard": {
        "notes_append": (
            "SRM 01-01 Double Cross (Seattle, 2060s): the Metroplex Guard is the second escalation "
            "behind Lone Star for the Westin Seattle. If runners walk into a downtown "
            "AAA-security hotel 'dressed like something out of the Desert Wars, carrying half an "
            "armory', the book calls in Lone Star special response teams and, depending on how much "
            "hardware is on display, the Metroplex Guard as well."
        ),
    },
}

LOC_UPDATES = {
    "Griffin Biotechnology Everett Research Facility": {
        "notes_append": (
            "SRM 01-01 Double Cross: at the time of the shareholders' meeting the compound has "
            "still not opened. It was built with the capital DocWagon and its co-investors put "
            "into Griffin Biotechnology when they bought the firm, to house Dr. Chandra Dasari's "
            "neurology programme, and the announcement at the meeting is meant to put it on the "
            "metroplex map. Days before the adventure somebody poked around the site and, because "
            "it had not opened and Knight Errant Security Services already held the contract, "
            "'learned very little about the research being conducted on DocWagon's behalf'. The "
            "intruders are never identified, which leaves an unresolved thread the GM can hang on "
            "Paladin Medical Technologies, on Rose Croix's backers, or on a third party. There is "
            "no scene here in Double Cross -- the facility is prologue texture only, and the "
            "obvious next target for anyone following the arc's opening move."
        ),
    },
    "DocWagon Snohomish Pharmaceutical Facility": {
        "notes_append": (
            "SRM 01-01 Double Cross (a few weeks later): the aftermath of the demolition, seen from "
            "inside DocWagon. The franchise is set back six months in lost profits and production "
            "and has to buy from outside vendors who have sensed that their usefulness has been "
            "restored and raised their prices accordingly -- Paladin Medical Technologies among "
            "them. Nobody in 01-01 names a culprit; the destruction is reported only as something "
            "that happened. Background the earlier module did not give: Garrett Walsh approved this "
            "plant a month before the events of 01-01's prologue and it was almost finished, "
            "intended to make common drugs and medical supplies locally instead of shipping them "
            "from elsewhere in the UCAS, supplying DocWagon's own network and selling the overage "
            "under signed contracts to Seattle General Hospital and the university clinic; finance "
            "projected it paid off inside eighteen months, with half a million nuyen a year saved "
            "on medkits and tranq patches alone. It was also one of Michael Davenport's hidden "
            "caches: a file named simply 'H', tucked into the system where a standard inspection "
            "would not find it and encrypted heavily enough that breaking it would take years, "
            "openable only by his own biometric data plus a secret passcode. The book never says "
            "what became of the file, which leaves DocWagon's customer lists and security codes "
            "somewhere in the wreckage as a live thread. Named as 'the Snohomish facility' and 'a "
            "production facility in Snohomish' in this book -- the same site under the SRM 00-02 "
            "name."
        ),
    },
    "Harborview Medical Center": {
        "notes_append": (
            "SRM 01-01 Double Cross (Seattle, 2060s): the DocWagon ambulance carrying the "
            "'mortally wounded' Michael Davenport pulls away from the Westin Seattle bound for "
            "Harborview, and is destroyed by the runners a few blocks out. (The KSEA screamsheet "
            "calls it 'Harborview Hospital' -- book inconsistency; it is the same facility.) Fox "
            "spurs the team on precisely with the line that if the HTR team reaches a hospital they "
            "may revive the target, which makes Harborview the reason the runners commit the crime "
            "that makes the deception stick."
        ),
    },
    "Seattle General Hospital": {
        "notes_append": (
            "SRM 01-01 Double Cross (Seattle, 2060s): DocWagon Seattle signed contracts with "
            "Seattle General and with the university clinic to supply them with the "
            "pharmaceuticals produced in overage at its new Snohomish plant. The plant was "
            "destroyed a few weeks before the adventure, so those supply contracts are now unmet "
            "and DocWagon is buying from outside vendors at raised prices."
        ),
    },
    "Fort Lewis": {
        "notes_append": (
            "SRM 01-01 Double Cross (Seattle, 2060s): the UCAS military selected Fort Lewis, inside "
            "the Seattle metroplex, as the testbed and control centre for the corporations winning "
            "its new combat-technology contracts -- pharmaceuticals to enhance troops in the field "
            "without a trained magician present, and chemical compounds for use against "
            "paranormals such as the revolutionary gamma-scopolamine. DocWagon's COO Michael "
            "Davenport built a bid around it and was refused; Yamatetsu, AG Chemie of Europe and "
            "Paladin Medical Technologies won it instead. Fort Lewis is also home to the very "
            "successful car dealership of Earl Peabody, the DocWagon contract holder of Davenport's "
            "build whose medical records and clones were appropriated to supply a corpse."
        ),
    },
}

NPC_UPDATES = {
    "Fox": {
        "description_append": (
            "SRM 01-01 Double Cross: on this job the swagger comes with a cigarette he drops and "
            "grinds out with his toe as the runners walk up to the Lake Washington lay-by, and with "
            "cigars passed around afterwards, which for Fox counts as effusive praise. 'Thank you "
            "all for coming. I hope that you'll be as receptive to my offer. As you can probably "
            "guess, our need for privacy indicates a somewhat delicate mission... So, the "
            "assignment is some wetwork -- does anyone have a problem with that?' To a runner who "
            "refuses on principle he is entirely gracious: 'That's quite all right -- I admire your "
            "convictions and of course will honor your wishes.'"
        ),
        "background_append": (
            "SRM 01-01 Double Cross: Fox tells this team himself that he ran the shadows for years "
            "before 'retiring' into fixing, and that he can cover decking, driving and small-arms "
            "support on a run -- the closest the campaign comes to confirming the rumour about his "
            "past. He owns at least one first-rate Tacoma safehouse, which he lends only when the "
            "job matters."
        ),
        "notes_append": (
            "SRM 01-01 Double Cross: Fox brokers the wetwork contract on DocWagon COO Michael "
            "Davenport for a Johnson who is in fact Davenport himself. Terms: 10,000 nuyen base for "
            "green runners (limit 12,000), 12,000/15,000 streetwise, 15,000/20,000 professional, "
            "20,000/25,000 veteran, 25,000/35,000 elite, 30,000/40,000 prime; up to 20 percent in "
            "advance if negotiated; a 20 percent discount on standard gear whose Availability fits "
            "a two-day window (no cyberware, bioware, milspec or magical goods beyond fetishes and "
            "conjuring materials); captured hardware fenced afterwards at 20 percent of book, which "
            "can beat street price where the Street Index is under 1. He also supplies a stocked "
            "safehouse, wider contact access and temporary IDs. The non-negotiable condition is "
            "that he comes along, and the reason is that he is paid to report the runners' plan -- "
            "and any change to it -- to the Johnson after giving it his 'seal of approval'. He "
            "bugged the safehouse for the same purpose (bugs off on arrival in case of a sweep, "
            "live once the team settles, off again the moment he suspects another sweep; the book "
            "instructs the GM that the runners never find them). He avoids mages carrying Mind "
            "Probe or Analyze Truth; if he thinks he is being probed he stops talking and "
            "concentrates on singing 'Row Your Boat' inside his head, adding the Table Rating to "
            "his Willpower to resist. A mage who gets through learns only that he passes plans "
            "along -- he does not know why, and honestly does not believe the team is being crossed. "
            "At zero hour he screams over the shared commlinks that the HTR team must not reach a "
            "hospital, herding the runners out to destroy the ambulance. Afterwards he waits half "
            "an hour at the safehouse, makes one call, confirms the deaths, and hands out cigars "
            "and certified credsticks. Runners who behaved professionally, took command, made him "
            "look good and caused no unnecessary collateral damage can take Fox as a new contact."
        ),
        "contact_skills_add": [
            "Safehouses and temporary identities",
            "Corporate rumors and shadow gossip on metroplex executives",
        ],
    },
    "Dr. Fredericks": {
        "description_append": (
            "SRM 01-01 Double Cross: a year or so on, still 'known as a ruthless businessman' who "
            "will stop at nothing to take Paladin into the top echelon of Seattle's medical field, "
            "but no longer screaming at his executives -- he conducts his own interviews now, from "
            "a blacked-out Mitsubishi Nightsky with a pair of heavily cybered ork bodyguards, which "
            "tells the runners most of what they need to know about how a biotech CEO living on one "
            "contract does business in this city."
        ),
        "background_append": (
            "SRM 01-01 Double Cross: Fredericks took Paladin into partnership with Yamatetsu and AG "
            "Chemie of Europe on the UCAS military pharmaceuticals contract that DocWagon's COO "
            "Michael Davenport had spent two weeks preparing to bid for, and the three partners are "
            "making money hand over fist. Davenport's sources say that contract is the only thing "
            "keeping Paladin afloat, so the contract famine that made him order a rival's plant "
            "levelled has been survived rather than solved."
        ),
        "notes_append": (
            "SRM 01-01 Double Cross: printed here as 'Dr. Thomas Fredericks' (SRM 00-02 gives only "
            "'Dr. Fredericks'); the same man, so this row keeps the earlier name. He is the Insider "
            "Trading host matched to runners with corporate contacts -- the black Nightsky, the ork "
            "bodyguards, a 1,000 nuyen gratuity for polite and cooperative answers, "
            "gamma-scopolamine and a truth-drug interview for anyone who declines the invitation. "
            "He wants to know what is about to happen to DocWagon, being simultaneously its major "
            "supplier and its competitor. The players cannot know it, but he is also the man who "
            "ordered the destruction of DocWagon's Snohomish plant a few weeks earlier -- the event "
            "that put DocWagon back on outside vendors like Paladin at raised prices, and the one "
            "thread in this adventure that leads straight back to a named villain."
        ),
        "contact_skills_add": [
            "Seattle biotechnology and medical-supply markets",
            "UCAS military pharmaceuticals contracting",
        ],
    },
    "Toju Shotozumi": {
        "description_append": (
            "SRM 01-01 Double Cross: meets the runners the way all four Insider Trading hosts do -- "
            "a black Mitsubishi Nightsky that seems to swallow the surrounding light, a rear door "
            "that opens by itself, a low voice saying 'Get in, we need to talk...' and a seat "
            "between two large ork bodyguards cybered to the gills -- but the questions come from a "
            "man with strong business skills who must decide which stocks the syndicate buys and "
            "which corporations it leans on. Courtesy matters more with him than with any of the "
            "other three."
        ),
        "background_append": (
            "SRM 01-01 Double Cross: the oyabun's cousin, placed in charge of the sokaiya -- the "
            "branch of the Shotozumi-rengo that handles the yakuza's dealings with local "
            "corporations and businesses. Sokaiya work is shareholder pressure and market "
            "manipulation dressed as investment, so advance knowledge of an assassination at a "
            "shareholders' meeting converts directly into profit. He heard about the runners' "
            "involvement 'through the grapevine', which leaves them free to wonder which of their "
            "own contacts sold them."
        ),
        "notes_append": (
            "SRM 01-01 Double Cross: no statistics. The Insider Trading host matched to runners "
            "with yakuza contacts; mechanics identical to the other three (1,000 nuyen and a "
            "courteous drop-off for cooperation, a gamma-scopolamine dart and questioning under a "
            "truth agent for refusal -- the runner with the best Etiquette should do the talking). "
            "Of the four he is the one whose organisation can most readily act on what it learns: "
            "the sokaiya can buy into DocWagon before the news breaks and into Rose Croix after it. "
            "A team that impresses him has a genuine yakuza patron for the rest of the arc; a team "
            "that insults him has the Shotozumi-rengo's attention, which is worse."
        ),
        "contact_skills_add": [
            "Shotozumi-rengo sokaiya operations",
            "Corporate leverage, shareholder pressure and stock positions in the metroplex",
        ],
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
One mapped system. The book gives it in SR3 Matrix notation (security code / subsystem ratings and
a trigger-step table) rather than as a node map, so it is reproduced as printed.

**Westin-Seattle Hotel Computer Network** (p.19). Standard Matrix iconology throughout -- from the
entry node the whole system is visible with nothing hidden or unusual: the hotel control systems
(elevators, lighting, and the rest) on one side, the data files on the other, and in the distance a
connector to the private Westin International network that carries reservations and corporate data
between all Westin properties.

Security code: **Orange-5/9/9/8/9/9**

| Trigger step | Event |
|---|---|
| 3 | Probe-4 |
| 7 | Tar Baby-6 |
| 12 | Probe-6, Tar Pit-6, Passive Alert |
| 18 | Probe-6, Killer-6 |
| 25 | Tar Pit-6, Tar Pit-6, Killer-6 |
| 30 | Shutdown |

| File | Size | Contents and protection |
|---|---|---|
| Current Reservations | 2500 Mp | Every active reservation for the next four months: guest names, contact information, arrival and departure dates and times. Scramble-4 |
| Guest List | 2500 Mp | The current registry: names, addresses, phone numbers, current billing, and annotations on VIPs and their preferred services and meals. PAYDATA, 5,000-7,500 nuyen to the right fixer or fence. Scramble-6 |
| Duty Roster | 100 Mp | Every member of staff, position, pay rate and credstick ID code. Must be modified by anyone posing as hotel staff |
| Catering | 1500 Mp | Ballroom event schedules and special instructions, current and six months out: the Rabinowitz reception and the DocWagon shareholders' meeting, who runs each event, what security is being provided, menu, table set-up. No guest name lists -- those belong to each event's own coordinator |
| Inventory | 2000 Mp | Every material good in the hotel, from kitchen pots to the painting in room 1610 |
| Supplies | 1200 Mp | Consumables: linen, cleaning supplies, the little shampoo bottles |
| Contracts | 1800 Mp | All current hotel work contracts -- delivery, trideo, elevator licences, liquor licences. Scramble-4 |
| Logs | 3000 Mp | Four months of department logs, checklists and day-to-day paperwork; compressed and shipped to corporate for archiving every six months |
| Larder | 1500 Mp | Current foodstuffs and liquor for the restaurants and bars, plus recipes and purchasing schedules |
| Register | 1000 Mp | Pointers to actual funds -- 22,720 nuyen transferable to credsticks. Scramble-6 |

Consequences: an active alert raises hotel security for six hours; a full shutdown additionally
takes the system down for at least two hours, during which the hotel takes no reservations and
checks nobody out. Elevators, maglocks, fire control, lighting and HVAC are all under computer
control and therefore reachable from the control side of this host.

**Not mapped**: the private Westin International inter-property network behind the connector;
DocWagon Seattle's corporate system (where Davenport's encrypted caches are hidden, including the
file "H" that was in the Snohomish plant -- his biometrics plus a secret passcode, otherwise years
to break); the DocWagon dispatch system, where an executive can keep HTR corporate bracelets from
registering; and the safehouse smart-house system (Sensors 4, Maglock 6, and Fox's bugs).
"""

NOT_BUILT = """
- **Trader Vic's**, **The Emerald Room** and **the Elven View** (the Westin's three first-class
  restaurants), the **Lobby Bar** and the **Fifth Avenue Corner Cafe**, and the named function rooms
  from the handout maps (**Vashon I-II**, **Whidbey**, **Orcas**, **Blakely**, **Cascade Ballroom**,
  **Glacier Peak**, **St. Helens**, **Stuart**, **Baker**, **Adams**, **Olympic**, **Stanwood**,
  **Emerald City Gallery**, **Elliott Bay Room**) -- all folded into the Westin Seattle row.
- **The Grand Ballroom** itself -- the adventure's climax happens in it, but it is a room in the
  hotel, described in full on the hotel row rather than given a location of its own.
- **AG Chemie of Europe** -- the European partner on the defense contract, a pure name-drop; recorded
  on the Yamatetsu and Paladin rows.
- **The university clinic** that contracted for Snohomish overage -- unnamed; on the Snohomish row.
- **The unnamed CFO** of DocWagon Seattle (second speaker at the meeting), the **Master of
  Ceremonies**, the **DocWagon security director** who ran Davenport's black operations, and
  **Davenport's decker** who hid and encrypted the caches -- unnamed roles, on the DocWagon and
  Davenport rows.
- **The extraction team** (the shaman with the greater form city spirit, the rigger, the mages with
  Improved Invisibility anchoring foci) and **the shadowrunner mage in the audience** -- deliberately
  statless in the book, uncapturable by design; on the Rose Croix row.
- **Dr. Dasari's two bodyguards**, the **personal bodyguards** and **contracted private security** at
  the Rabinowitz reception, **Westin hotel security** and the **DocWagon special ops team** -- stat
  blocks and behaviour on the Westin International, Howell Shultz and Rabinowitz, and DocWagon rows.
- The Shadowland posters on the handout -- **Hondo**, **The Chromed Accountant**, **Skeptic**,
  **Penny Ante**, **Sweet Gypsy Rose** and **Deacon Blues** -- board handles with no face and no
  location; their claims are recorded on the Davenport and Kyle Matthews rows. Penny Ante (Matthews's
  childhood friend) and Deacon Blues (who names HTR team #27) are the two worth promoting to real
  NPCs if a GM wants the loose end chased.
- The **simsense starlet** whose dress gets a tray of drinks, the **boisterous old friend** of the An
  Old Friend scene, and the **wedding relative** hunting for a shared college past -- roles the GM
  casts to fit the table, not fixed people.
- **Howell** and **Shultz** (the other two named partners of the law firm) -- on the firm's row.
"""

PLAY_NOTES = """
- This is a Shadowrun Missions convention scenario, so it is written for a table of strangers with
  a four-hour clock. Two structural things follow: the main line (Crossed) is five scenes long, and
  the Crossed Again section is a pile of optional scenes to spend spare time on. Pick from Crossed
  Again by what the table lacks, not in printed order.
- The whole adventure is a rail with one honest purpose: the runners must succeed, and their success
  must be someone else's plan. The book states outright that they will never find the safehouse
  bugs, never catch Fox reporting, never capture an extraction-team member, and that the ambulance
  explodes no matter what they hit it with. If your table hates being handled, the fix is not to
  break the plot but to let them work out afterwards that they were used -- the handout's Shadowland
  thread is written to hand them exactly that.
- Fox's presence on the run is non-negotiable and players will push back. Sell it as value: an extra
  gun, a driver, a decker, contact access, temporary IDs and a 20 percent gear discount. He is 'as
  good as you need him to be'.
- Mind-affecting magic is the one real threat to the deception. Fox avoids mages with Mind Probe or
  Analyze Truth on their sheet, and if he thinks he is being probed he stops talking and adds the
  Table Rating to his Willpower while singing 'Row Your Boat'. If a mage gets through anyway, they
  learn he reports the team's plans and nothing more -- he genuinely does not know why, and does not
  believe the team is being crossed.
- Payment scales with Table Rating: 10,000/12,000 green up to 30,000/40,000 prime, 20 percent
  available up front, gear at a 20 percent discount, captured hardware fenced at 20 percent of book
  (which can beat street price where the Street Index is under 1).
- The White Doves scene exists so a character who will not do wetwork is rewarded rather than
  benched: the player runs a second character (an established one, or an SR3 archetype -- never a
  freshly generated one), the pacifist keeps the Karma including a bonus point, the surrogate keeps
  the money. At a multi-table event, ask whether the player would rather move tables, and never push
  a table below four players to do it.
- Zero Hour wants miniatures or markers. The runners get one free combat turn on the trigger phrase
  before initiative. Hotel and DocWagon security try to capture, then to herd them into the street
  for Lone Star; anyone maintaining a cover identity and not shooting is ignored. Personal
  bodyguards only fire if their charge is threatened. Five turns brings two patrol cars and TR d6
  contract guards, twelve brings a Lone Star response team.
- Do not let a runner reach Davenport's body. If one closes, a panicking would-be hero's stray shot
  'hits' him, and he shoves Fleming and his assistant away shouting at them to run -- staged so that
  nobody examines him. Prefer mundane countermeasures over magic so a watching mage sees nothing;
  where magic is needed, the planted mage casts in the segments around the attack.
- Insider Trading can be run more than once with different runners: Ciarniello for Mafia contacts,
  Toju for yakuza, Fredericks for corporate, Hollingsworth for high society. Easy way for faces,
  hard way (gamma-scopolamine and a truth-drug interview) for everyone else.
- Ambush! is the pacing valve. Use it when the team over-plans. If they are all captured, Fox
  escapes, hires a rescue team, and they resume the run with a hardened target and less time --
  which is a better outcome than a TPK and the book says so.
- Karma: 1 for the 'elimination', 1 for no unnecessary collateral damage or dead innocents, up to 3
  individual, maximum 5 (6 with White Doves). Runners who behaved professionally, took command and
  made Fox look good can take Fox as a contact.
- Arc hooks to plant now: Peabody's swapped medical records; the missing dwarf Kyle Matthews; who
  actually blew up Snohomish; the file "H"; Dasari and her unopened lab; and Margo Fleming, who was
  close enough to Davenport to have noticed the preparations. Every one of them pays off better if
  the team first believes it did a clean job.
"""
