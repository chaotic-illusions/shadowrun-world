# Double Exposure (FASA 7319, 1994, Fraser Cane with Nigel D. Findley) -- campaign order #23. Downtown /
# Glow City (Redmond Barrens) / Kent / Auburn / Tacoma, 2055 (p.7 "The year is 2055"; no month is given --
# the prologue's "unusual humidity" and the bus-day "weatherman warned that today is going to be a hot one"
# put it in summer).
# Source text: docs/Adventures/text/Shadowrun 2e - Adventure - Double Exposure {FASA7319}.txt (62 pages).
# Editing inconsistencies in the book (recorded on the affected rows):
#   - Jonathan Tung has Quickness 6 in the hive chase (p.43) but Quickness 3 in the Cast of Shadows (p.57).
#   - Peace Enforcement Officers are Threat/Professional 5/4 at the gate (p.22) and 4/4 in the hive (p.44).
#   - The Hope camp fence is "eight meters high" (p.22); the Faith camp fence is "4-meter-high" (p.39) with
#     Barrier 25 instead of 24 -- otherwise "security at Faith matches Hope".
#   - The timeline calls Ted Wiley an "EPA agent" (p.10); the text says the EPA hired him as a private
#     investigator (p.28), and the Awareness table calls him "Agent Wiley".
#   - Enrico Sanchez transfers to Faith camp "four days before the datasteal" (p.29) but the timeline puts
#     the transfer on Day 7 and the Aztechnology raid on Day 10 (three days).
#   - Juarez says New Dawn Environics is "based in Kent" (p.17); p.33 gives it ten Seattle sites and a large
#     downtown office block as its newest facility, with the Kent plant only one cog.
#   - The New Dawn flesh-form soldiers have Reaction 10 (p.35); the near-identical Faith camp soldiers have
#     Reaction 7 (p.39).
#   - OCR renders Juarez as "Judrez" / "Juerez" throughout; the Cast page spelling (Juarez) is used.
# ASCII only (pre-commit hook).

ADVENTURE = "Double Exposure"
ORDER = 23
SOURCE = "Shadowrun 2e - Adventure - Double Exposure {FASA7319}.pdf, pp. 4-62"
YEAR = "2055 (summer; month not given)"

SYNOPSIS = """
Two cakewalk runs from the team's regular fixer -- hijacking an **Aztechnology** van of cyberlimb spares
on its way from the Pyramid to Tacoma, and lifting a refrigerated case of DNA and blood samples from a
**DocWagon** Jackrabbit between Cherry Street and Auburn -- turn out to have been filmed. Weeks later
**Special Agent Simon Juarez** of the **UCAS FBI** sits down at **McHugh's** on Fourth and Blanchard with
a vid player, two snipers across the street and a "postmortem mail" dead-man switch, and buys the runners
for 30,000 nuyen each: find out why **Renraku Computer Systems** is pouring "enough money to buy small
countries" into **Project Hope**, the charity that is rebuilding Glow City with Seattle's homeless. His
last man inside, **Special Agent Clint Ranger**, vanished from the camps two months ago.

The runners apply at the reeking **Project Hope Enrollment Center** on Seneca Street (**Ms. Montagu**),
ride a sealed bus through the Barrens, are searched and "peace-bonded" by white-suited Peace Enforcement
Officers, and wake at 7 a.m. every day to hoe fields for camp director **Jonathan Tung** in the
impossibly green **Hope Relief Camp**. The camp is a shell: its computer (password "Springs Eternal")
only points at directories in the **Faith Relief Camp** system, its guards move far too fast, and
everybody interesting is a spy -- **Garder Armstrong** (a flesh-form worker ant planted by the
**Universal Brotherhood**), **Ted Wiley** (a private investigator working for the **UCAS EPA**), **Casey
Hughes** (Renraku), **Enrico Sanchez** (Aztechnology) and **Andrew Mitchell** of the Seattle Times, who
is dragged off at breakfast. The **Butchers** ram the electrified fence one night and fifteen gangers die
in under a minute. Wiley's lead is **New Dawn Environics** in Kent, the extraterritorial "saint" that
turns toxic effluent into crystal water and black soil for the camps: behind its songbirds and armed
guards is a 100-by-150-meter effluent pool where bloated human hosts float bound to dog-sized dragonfly
larvae while toxic earth and water spirits force the poison into them.

Everything is one machine. Project Hope, New Dawn and their shell parents belong to the Universal
Brotherhood, and beneath Faith camp's Renraku-funded medical center -- where mercenary docs implant
BTL chips and "subjective time dilation" simsense in unanesthetized enrollees -- an ancient cave maze
holds an **Ant Hive** of more than five hundred spirits and a four-meter **Hive Queen** who shares her
mind and her Willpower with every servant, Tung included. Renraku is quietly paying for the whole hive.
Corporate schedules collide: Aztechnology raids Faith camp on Day 10 to steal Renraku's data, Renraku
"violently pulls out" on Day 11, and both hit teams are cut to pieces by things that only look like
security guards. When the runners reach the basement office, Tung has already purged the central
computer to a portable and is running for the big metal doors; the chase down a slippery mold-lined
tunnel ends halfway up the wall of a 200-meter cocoon cavern with twenty flesh-form soldiers climbing
toward them and true-form ants closing the tunnel behind.

Juarez pays the balance, hands over "the originals" (a lie) and, if told about the hive, has UCAS
soldiers fill the caverns with fuel-air explosive within a day (a methane pocket, says the UCAS
Geological Service). Within a week the camps and the Kent plant are closed "for health reasons",
warrants go out for Project Hope's vanished management and the Seattle chapter's executives, the FBI
starts burning hives under Brotherhood chapter houses across the country, and the Brotherhood is
finished as a force in the UCAS inside two months. Renraku is untouched: the government is saving that
dirt.
"""

TIMELINE = """
- **Weeks before** -- the Aztechnology van (Pyramid to Tacoma, 22:00) and, a few weeks later, the DocWagon
  Jackrabbit (Cherry and 13th to Auburn, 10:00); Juarez's drones film both. Two months earlier Clint
  Ranger entered the camps; four weeks at Hope, three at Tranquility, then the operating table.
- **Day 1** -- Juarez's call and the McHugh's meet (5,000 each to show up; 15,000 each up front).
  The Enrollment Center; the bus leaves three hours after the interview; delousing; Solace House.
- **Day 3** -- the Butchers ram the Hope camp fence at night; fifteen dead in 55 seconds.
- **Day 5 (morning)** -- Ted Wiley rides a New Dawn Environics truck back to Kent (10,000 nuyen to
  whoever creates his diversion).
- **Day 7** -- Enrico Sanchez is transferred to Faith camp; Tung transfers the runners there too if they
  have not arranged it themselves.
- **Day 10** -- Aztechnology's raid on the Faith camp medical facility.
- **Day 11** -- Renraku's "violent" pull-out; the runners' window closes. Tung purges the computer and runs
  for the hive whenever they reach the basement.
- **Day 14** -- the agreed end of the Renraku / Project Hope experiments (never reached).
- **After** -- Juarez pays 15,000 each; the fuel-air strike on the hive within a day (+5,000 each to join);
  camps and the Kent plant closed within a week; the Brotherhood broken in the UCAS within two months.
  Seattle Datafax handouts: "Underground Explosion" (told) or "Barrens Disappearances Up" (not told).
"""

ORGS = [
    {
        "name": "Project Hope",
        "org_type": "charity / relief-camp operator (Universal Brotherhood front)",
        "tier": 3,
        "headquarters": "Enrollment Center, 3487 Seneca Street, downtown Seattle (LTG 8206 (75-0999)); ten relief camps in the Barrens",
        "summary": "The charity rebuilding Glow City with Seattle's homeless -- a Brotherhood shell that sells enrollees to Renraku's surgeons and feeds the rest to the hive",
        "description": (
            "A recently formed organization that has taken on the seemingly impossible task of restoring "
            "life to the Glow City region of the Redmond Barrens, using the one resource nobody else wants: "
            "Seattle's teeming homeless. Apply at the downtown Enrollment Center, ride the bus, get a shower, "
            "clean clothes, three meals, a bunk, a hoe and a counselor, and within four weeks a transfer to "
            "one of the other nine camps. It keeps no records -- no names, no SINs -- and people vanish in "
            "transit. Publicity is glowing, the media adore it, and 'thousands of corporate and individual "
            "philanthropists' back it, Renraku among them with a public 10,000-nuyen donation. Behind the "
            "bewildering network of subsidiaries and shell corporations it belongs to the Universal "
            "Brotherhood; Renraku pays it enormous sums to run biotech and BTL experiments on the enrollees at "
            "Faith camp, and the Brotherhood diverts most of that money, at the Ant Queen's behest, into "
            "cocoons and larvae. Not technically extraterritorial, but the camps behave like corporate land "
            "and nobody argues with the guards. Motto on the terminals: 'Love Project Hope, and Project Hope "
            "will love you right back.'"
        ),
        "leadership": [
            {"name": "Jonathan Tung", "title": "Director, Hope Relief Camp (and the Queen's link to the camps)", "notes": "Flesh-form worker ant; former Lifeline Education PR manager."},
            {"name": "Ms. Montagu", "title": "Caseworker, Enrollment Center", "notes": "Knows nothing and does not care."},
        ],
        "notes": (
            "Structure: ten camps in the Barrens (Hope, Faith, Tranquility named), more than 2,000 enrollees, "
            "Hope as the training camp (200 people). Two unnamed Project Hope managers share the system "
            "password 'Springs Eternal' with Tung (changed every 48 hours); they know Renraku's reason but not "
            "the Brotherhood's, are not yet embraced by the Queen, and are easy Mind Probe targets (Mr. Johnson "
            "archetype, Willpower 4). Security: Peace Enforcement Officers -- flesh-form ant soldiers (B9 Q8 "
            "S9 C2 I4 W2, R8, +10 Initiative (18+1D6); TR 5/4; Firearms 6, Stealth 6, Security Procedures 3; "
            "AK-97 gas-vent III, Fichetti Security 500, armored suit 8/6 with helmet, low-light/thermo goggles, "
            "commlink); fourteen per camp, a third on duty, radio check every ten minutes, orders to shoot "
            "anyone coming over the fence. Two PEO Shamans per camp (Ant totem; B3 Q5 S4 C2 I5 W5, Magic 6; "
            "Conjuring 6, Sorcery 6; Armor 4, Chaotic World 5, Mana Barrier 4, Mana Bolt 4, Powerball 5, Sleep "
            "5; spell lock Mana Barrier) patrol astrally, off duty noon to 8 p.m. Faith camp adds three Force 4 "
            "fire elementals for Renraku's benefit. Enrollment Center rent-a-cops (4): Ares Viper Slivergun, "
            "taser, stun baton, PANICBUTTON; they call Lone Star. Fences: chain-link, razorwire, reinforced and "
            "electrified, Barrier 24 (25 at Faith) vs vehicles, 14S shock. Gate sweep: Absolute Security "
            "chemsniffer and Encyon Industries metal detector, both Rating 5; lethal cyberware is 'peace "
            "bonded' (Biotech (5), base 4 hours to undo). The enrollment computer checks the Lone Star warrant "
            "database and calls the Star on hits. Awareness Point ladder (Brotherhood): 1 casual PEO "
            "surveillance; 2-4 watched constantly; 5-7 detained a few days; 8-9 captured for the cocoons; 10+ "
            "experimented on, then cocooned. Ending: camps closed within a week 'for health reasons'; FBI "
            "warrants for the entire management team, never served -- the leadership drops out of sight."
        ),
        "allies": ["Universal Brotherhood", "Renraku Computer Systems", "New Dawn Environics", "The Ant Hive (Glow City)"],
        "enemies": ["UCAS Federal Bureau of Investigation", "Aztechnology", "The Butchers"],
    },
    {
        "name": "New Dawn Environics",
        "org_type": "corporation (environmental clean-up; Universal Brotherhood subsidiary)",
        "tier": 3,
        "headquarters": "Large corporate office block, downtown Seattle (address not given); water and soil treatment plant in Kent",
        "summary": "Three-year-old extraterritorial 'saint' of the waste business that turns toxic effluent into pure water and arable soil -- by magic, larvae and human hosts",
        "description": (
            "'At One With Nature.' A three-year-old corporation with more than ten sites in Seattle -- its "
            "newest a large downtown office block -- enough employees to qualify for extraterritoriality, and "
            "about 30 percent of the sprawl's waste-disposal market (Shiawase Envirotech has the rest). "
            "Factories pay it to take toxic effluent off their hands; tanker trucks carry the bilge to Kent; "
            "crystal-pure water and rich black soil come out and go to Project Hope, its largest customer. "
            "Twelve EPA court-order requests have been refused and six months of investigation found nothing "
            "illegal. New Dawn belongs to Universal Brotherhood International, but only a handful of top "
            "executives know it; the Kent plant is an autonomous division and the rest of the company is "
            "clean, staffed by ordinary people who have no idea. New Dawn is willing to kill to protect the "
            "process, and its guards can shoot first on sovereign soil."
        ),
        "notes": (
            "The Kent facility is staffed entirely by insect spirits: six flesh-form soldier ant guards (B10 "
            "Q9 S10 C2 I5 W2, R10, +10 Initiative; TR 5/4; Firearms 6, Stealth 6; AK-97, Fichetti Security "
            "500, armored suit 8/6, goggles; Force 5, aura-masking, NOT covered by the Queen's shared "
            "Willpower; faceted eyes, bony ridges and bristles under the helmets), twenty Force 3 flesh-form "
            "workers (B1 Q9 S5 I1 W1; grotesque, they run and shriek for the soldiers), three Force 4 watcher "
            "spirits on the astral perimeter and three Force 5 true-form soldier ants inside the building. "
            "Legwork (TN 5; city official, company man, reporter, scientist; Shadowland TN 4): saints; 'without "
            "magic it's totally impossible'; 'belongs to some larger corp'; 'New Dawn and Project Hope belong "
            "to the same corp -- both small potatoes, both extraterritorial'. The book's first legwork result "
            "confuses it with a band ('not enough guitars'). The UCAS closes the Kent facility within a week "
            "of the runners' report. EPA Awareness ladder: 1 Wiley watches; 2-4 he warns them and threatens "
            "an arrest he cannot make; 5+ he offers 10,000 nuyen for court-usable data."
        ),
        "allies": ["Universal Brotherhood", "Project Hope", "The Ant Hive (Glow City)"],
        "enemies": ["UCAS Environmental Protection Agency", "Shiawase Corporation"],
    },
    {
        "name": "The Ant Hive (Glow City)",
        "org_type": "insect spirit hive",
        "tier": 3,
        "headquarters": "Natural cave maze beneath the Faith Relief Camp medical center, Glow City, Redmond Barrens",
        "summary": "The Queen's second Seattle hive: 500-plus ant spirits, a 200-meter cocoon cavern, and a telepathic queen who shares her Willpower with every servant",
        "description": (
            "In an ancient maze of natural caverns under Faith camp, funded without its knowledge by Renraku "
            "and fed by Project Hope's endless buses, the Hive Queen is building the hive that will one day "
            "share her 'love' with all of Seattle. Hundreds of enrollees hang in clumps of fifteen-plus pods in "
            "a 200-meter cocoon cavern lit by fluorescent tubes twenty meters up; more than five hundred ant "
            "spirits already live below. The Queen picks her best-bonded flesh-forms -- Tung, the Peace "
            "Enforcement Officers, Garder Armstrong -- for work among humans; the twisted failures guard the "
            "caves. Every servant is in two-way telepathic contact with her (Share Minds) and wrapped in her "
            "Willpower against mind magic (Share Willpower). Unlike Craft's hive in Puyallup this Queen is "
            "fully summoned, awake, and ancient: she killed her shaman long ago."
        ),
        "leadership": [
            {"name": "The Glow City Hive Queen", "title": "Hive Queen (Force 10)", "notes": "See her NPC row."},
            {"name": "Jonathan Tung", "title": "Flesh-form worker; the Queen's link to the camps", "notes": None},
        ],
        "notes": (
            "Bugs rules reprinted pp.47-49: the Queen summons Force-rating workers a day; hosts bond by "
            "Willpower vs twice the spirit's Force (+2 when the Queen summons) -- 0 successes true-form, 5+ a "
            "flesh-form that keeps its shape, memories and gets aura masking. Flesh-form workers: mental "
            "stats of a true-form, physical one below the host, Skill power. Flesh-form soldiers: physical "
            "stats host plus Force, no venom or paralysis, no natural armor. True-Form Soldier Ant (Force 5): "
            "B6 Q10x4 S9 I5 W2, R10, +20 astral / +10 manifest; 9M; Enhanced Senses (Smell), Paralyzing "
            "Touch, Venom; Reduced Sight, Vulnerability (Insecticides). Hive entrance: Barrier 35 metal doors, "
            "Rating 7 maglock, at the end of the medical center's basement corridor; a half-kilometer of "
            "worker-cut then natural tunnel (green mold on the walls, slippery -- Athletics (2) each round at "
            "speed) opens halfway up the cocoon cavern, floor 50 m below on a 45-degree slope. The chase: 20+ "
            "flesh-form soldiers climb from below while two Force 5 true-forms and eight-plus PEOs (TR 4/4) "
            "close the tunnel behind; more than 500 spirits if the team goes deeper. Goal is exposure, not "
            "destruction; 'taking on the 200-plus members of the hive would be suicide'. The UCAS destroys it "
            "with fuel-air explosives within a day of hearing of it (4:34 a.m., roar heard in Tacoma); nothing "
            "survives. The Queen's atypical powers may be unique to her, shared by other atypical queens, or "
            "the new normal -- the book leaves that to the GM."
        ),
        "allies": ["Universal Brotherhood", "Project Hope", "New Dawn Environics"],
        "enemies": ["UCAS Federal Bureau of Investigation", "Renraku Computer Systems", "Aztechnology"],
    },
    {
        "name": "The Butchers",
        "org_type": "thrill-gang",
        "tier": 1,
        "headquarters": "Glow City, Redmond Barrens (turf not given)",
        "summary": "Glow City thrill-gangers who drive a truck through the Hope camp fence on Day 3 and lose fifteen in under a minute",
        "description": (
            "One of the gangs whose insignia is layered over every wall on the road into Glow City, alongside "
            "the Nightstalkers and the Splatters. After eyeing Hope Relief Camp's defenses for a couple of "
            "days they drop a fence section by driving a truck into it -- not knowing it is electrified. The "
            "driver and passengers die in a shower of sparks that wakes the neighborhood, then fifteen "
            "Butchers armed to the teeth march through the gap firing at anything that moves."
        ),
        "notes": (
            "Gang Boss archetype (SRII p.207). Capsule battle p.30: 30 s five PEOs behind cover; 35 s two "
            "punks vanish in a shaman's fireball; 42 s half dead, one PEO hit; 55 s 'Run awaaaay!'; 1:09 the two "
            "behind the truck fireballed; 2:15 ten more PEOs execute the wounded; 4:21 Tung on the "
            "loudspeaker; 34:45 fence as good as new. The point is what it shows the runners about the "
            "guards, not the gang. Timeline: Day 3."
        ),
        "enemies": ["Project Hope"],
    },
    {
        "name": "UCAS Environmental Protection Agency",
        "org_type": "government agency (environmental regulator)",
        "tier": 4,
        "headquarters": "Washington FDC (UCAS federal agency); Seattle-area investigation of New Dawn Environics",
        "summary": "The EPA, six months and twelve refused court orders into New Dawn Environics, now running a private investigator inside Project Hope",
        "description": (
            "The federal environmental regulator. It knows what goes into New Dawn Environics (effluent that "
            "'could eat your hand off') and what comes out (water cleaner than a mountain stream) and that "
            "this is impossible; its paranoid bureaucrats have spent six months and twelve court-order "
            "requests failing to make an extraterritorial corp explain itself. Having exhausted legal "
            "browbeating it hired PI Ted Wiley, who found Project Hope was New Dawn's biggest customer and "
            "enrolled at Hope camp. It may eventually send its own team into the Kent plant -- quite possibly "
            "the runners."
        ),
        "leadership": [
            {"name": "Ted Wiley", "title": "Private investigator under contract", "notes": "Inside Hope Relief Camp; 10,000 nuyen for help getting into New Dawn."},
        ],
        "notes": (
            "Juarez knows other groups are investigating the camps but not which; the EPA is one of them. "
            "Wiley cannot arrest anyone without blowing his cover. Legwork on Project Hope lists 'Government "
            "Agent' among the useful contacts."
        ),
        "enemies": ["New Dawn Environics"],
    },
    {
        "name": "Seattle Times",
        "org_type": "media (newspaper)",
        "tier": 2,
        "headquarters": "Seattle (offices not described)",
        "summary": "The newspaper whose reporter Andrew Mitchell went undercover in Hope Relief Camp and came back a few months later with the edge gone from his stories",
        "description": (
            "A Seattle daily that put reporter Andrew Mitchell into the Hope Relief Camp as an enrollee to "
            "find out what Project Hope really does. He asked the wrong questions at breakfast, three Peace "
            "Enforcement Officers dragged him away, and he returns to the paper months later with his "
            "stories blunted and no appetite for undercover work."
        ),
        "leadership": [
            {"name": "Andrew Mitchell", "title": "Reporter", "notes": "'Andy'; shipped to Faith camp 'for a new slant on life as an insect spirit'."},
        ],
        "notes": (
            "A reporter is one of the book's listed contacts for Juarez, Project Hope, Hope camp and New "
            "Dawn legwork. Runners who survive may recognize Andy's face next to a byline afterwards and wonder "
            "what looks back."
        ),
    },
    {
        "name": "Seattle Datafax",
        "org_type": "media (newsfax; Renraku division)",
        "tier": 2,
        "headquarters": "Seattle; 'A Division of Renraku Computer Systems'",
        "summary": "Renraku-owned newsfax service whose custom editions carry the adventure's closing handouts",
        "description": (
            "A newsfax service published as 'A Division of Renraku Computer Systems', delivered as custom "
            "editions with General, Features and Late Breaking sections keyed by REF numbers. Its coverage of "
            "the Project Hope collapse is careful about Renraku: international investigations of the "
            "Universal Brotherhood, arrests of high-ranking officials expected, and not a word about who paid "
            "for the experiments."
        ),
        "notes": (
            "Handouts 3 and 4 (p.61-62). General: Project Hope ownership and financial revelations lead to "
            "international investigations into Universal Brotherhood activities; 122 dead in a Tibetan train "
            "wreck blamed on a 'mountain-sized' fire elemental; MIT&M's 'self-energetic metamagical foci' "
            "results inconclusive. Features: Northrup's consumer 'air car' milestone; missing-persons cases "
            "rising nationwide; Arthur Garrett on municipalities licensing magic while the 'mystically "
            "advantaged' population rises. Late Breaking (hive destroyed): 'Underground Explosion' -- 4:34 "
            "a.m. under Glow City, roar felt in Tacoma, Eva Leuwendyke of the UCAS Geological Service blames "
            "a methane pocket in a known cave complex, rescue teams sent, no survivors expected. Late Breaking "
            "(hive not reported): 'Barrens Disappearances Up' -- about 110 missing this year in and around "
            "the Redmond Barrens, Governor Schultz cites go-gangs, cyberleggers, paranormal predators and a "
            "possible Mayan Cutter copycat, Lone Star reinforces Redmond but not Glow City. Both editions: "
            "'Running Gunfight Angers Police' -- Lone Star Lieutenant Dan Akkison on a two-and-a-half-hour "
            "running battle from Downtown into the Redmond Barrens with a vanload of shadowrunners, eight "
            "bystanders dead, twenty-seven injured, two of his troopers killed, the runners escaped."
        ),
        "allies": ["Renraku Computer Systems"],
    },
    {
        "name": "Lifeline Education",
        "org_type": "educational institute / cult (Universal Brotherhood front)",
        "tier": 2,
        "headquarters": "Not given (Seattle assumed)",
        "summary": "The controversial 'glorified cult' school where Jonathan Tung learned to turn media hounds away -- Brotherhood-owned through shells",
        "description": (
            "A controversial institute that belongs to the Universal Brotherhood through a complex network of "
            "intermediaries and shell companies. As its public-relations manager Jonathan Tung repeatedly "
            "diverted and dissuaded reporters intent on exposing the school as a glorified cult, which is "
            "exactly why the Brotherhood chose him to run the Project Hope camps."
        ),
        "notes": (
            "Background only (Cast of Shadows p.57); nothing else is said of it. A natural place for a "
            "reporter contact to have first met Tung, and a second Brotherhood front for the FBI's warrants to "
            "reach."
        ),
        "allies": ["Universal Brotherhood"],
    },
]

LOCATIONS = [
    {
        "name": "Project Hope Enrollment Center",
        "location_type": "charity enrollment office",
        "district": "3487 Seneca Street, halfway up the hill, Downtown",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "Project Hope",
        "summary": "Small nondescript office where Seattle's homeless queue for the camps: a stench like a convention of body fluids, olfactory-inhibited staff, a Rating 5 metal detector and four polite rent-a-cops",
        "description": (
            "A small, nondescript office building with a large, freshly painted sign; inside, urine, sweat, "
            "vomit and alcohol 'holding a convention', rows of chairs of the most unfortunate-looking slots in "
            "the plex (two working off hangovers, one crashing from a BTL chip), a well-dressed secretary "
            "with a plastic smile and caseworkers in the latest corporate fashion carrying portable computers "
            "-- all wearing olfactory inhibitors. Ms. Montagu's office is down the hall. Rooms: lobby, offices, "
            "lunch room, bathroom. LTG 8206 (75-0999); UCAS 98057. The bus leaves for the Hope Relief Camp "
            "three hours after the interview."
        ),
        "notes": (
            "Rating 5 metal detector on the main doors; the four guards (Ares Viper Slivergun, Defiance Super "
            "Shock taser, stun baton, PANICBUTTON, armor jacket) confiscate weapons and give them back on the "
            "way out. The questionnaire (Handout 2, p.60) asks for name, alias, LTG, birth to the second, "
            "criminal record, cyberware and where it was implanted, five employers, education and friends who "
            "might join; the computer checks Lone Star for warrants (patrol in minutes) and approves criminal "
            "records (+1 Brotherhood Awareness). Nothing here links to the Brotherhood or Renraku; the only "
            "paydata is a complete list of everyone ever sent to the camps (Virtual Realities fast resolution, "
            "base TN 4). Clint Ranger's recruiter was a young woman here who genuinely believes."
        ),
    },
    {
        "name": "Hope Relief Camp",
        "location_type": "relief camp / work camp",
        "district": "Glow City, Redmond Barrens",
        "security_level": "Corporate High Security",
        "controlling_org": "Project Hope",
        "summary": "Project Hope's showpiece training camp: replanted orchards, fresh paint and happy people behind an electrified fence, fourteen flesh-form ant soldiers and two Ant shamans",
        "description": (
            "Huge arched gates, white-uniformed guards, and beyond them a hundred years back in time: trees "
            "and flowers along the sidewalks, freshly painted two-story buildings, apple orchards replanted "
            "in soil trucked in over the Mount St. Helens ash, and 200 people who actually look content. "
            "Buildings (map p.24): Registration Office (Tung's office and, behind it, the central computer "
            "room), Tung's House, Solace House (the runners' quarters -- four twelve-bunk bedrooms, two baths, "
            "communal kitchen and living room, no locks, a bolted-down propaganda terminal), other houses, "
            "Security Building, Recreation Hall, Storage, Orchards, Main Gate. Schedule: 7:00 wake-up (Tung in "
            "person, with guards), 7:15 breakfast, 7:45 assignments, work 8:00-12:30 and 1:00-6:00, dinner, "
            "group counseling 7:15-9:30 in circles of eight, lights out at 10. Water and soil arrive by New "
            "Dawn Environics truck."
        ),
        "notes": (
            "Arrival: an hour's search at the gate (Rating 5 chemsniffer and metal detector; PEO Perception "
            "vs the runner's Dexterity to catch a hidden item; lethal cyber peace-bonded), then a four-hour "
            "chemical delousing that leaves the skin on fire for 24 hours (Willpower (4) not to cry out when "
            "touched). Work: 8S Stun fatigue every evening, Body dice only. Fence: 8 m chain-link with three "
            "strands of razorwire, reinforced and electrified, Barrier 24 vs vehicles, 14S. Fourteen PEOs (a "
            "third on duty; night-vision goggles; check-ins every 10 minutes) plus two Ant shamans (off duty "
            "noon to 8 p.m.) and one PEO wandering the registration building day and night (he initiates a "
            "call every 30 minutes). Leaving is free -- out the gate into the worst part of Seattle and walk "
            "downtown, no buses or cabs. The camp system is mapped in the prep doc (password 'Springs Eternal'; "
            "an innocent crash lets a Computer (4) keystroke logger catch it). Four other agents are inside: "
            "Armstrong, Wiley, Hughes, Sanchez; the reporter Mitchell is dragged off at breakfast. Transfers "
            "to Faith need Tung's digital signature (Computer (5) to forge from another document) or a good "
            "story about carpentry skills. Legwork TN 5: 'Hope you'll get out alive'; 'if you get brought up "
            "for transfer, start worrying'."
        ),
    },
    {
        "name": "Faith Relief Camp",
        "location_type": "relief camp / work camp",
        "district": "Glow City, Redmond Barrens",
        "security_level": "Corporate High Security",
        "controlling_org": "Project Hope",
        "summary": "The run-down camp where the experiments happen: blighted crops, crumbling houses, 75 percent of the enrollees slated for surgery, a medical center over the hive",
        "description": (
            "A startling change from Hope: dull, grim faces, anemic blighted crops, buildings actually "
            "crumbling, because nobody here has time to take care of anything -- everyone is performing "
            "experiments or being one. Same layout as Hope (map p.38: Registration Office, Director's House, "
            "Research Facility, Houses, Security Building, Recreation Hall, Storage, Orchards, Main Gate) "
            "plus the large white medical center near the middle. Nobody gets in without a transfer carrying "
            "Jonathan Tung's digital signature."
        ),
        "notes": (
            "Fence 4 m electric, Barrier 25, 14S. Six Force 5 flesh-form soldier ants at the gates at all times "
            "(B10 Q10 S10 C2 I5 W2, R7, +10 Initiative; TR 5/4; Rating 4 portable chemsniffers and metal "
            "detectors) and 'another dozen or so' on random patrol -- the GM sets the number; three Force 4 "
            "fire elementals (B5 Q18 S2, R6; 4M fire at 8 m, Engulf, Fire Aura, Fire Projection, Guard; "
            "Vulnerability (Water)) as respectable-looking magical security. Corporate raids: Aztechnology "
            "(Day 10) and Renraku (Day 11), a dozen or fewer Bodyguard / Combat Mage / Street Samurai "
            "archetypes each, cut to pieces on the wire and by fire elementals cooking off their grenades; "
            "run it as spectacle, rolling only shots at or from the runners, and use the chaos to hit the "
            "computer. Renraku Awareness 2-4 has PEOs arrest the runners and hold them 'on corp land' up to a "
            "week; 5+ Renraku pulls out one week later and disposes of them."
        ),
    },
    {
        "name": "Faith Relief Camp Medical Center",
        "location_type": "hospital",
        "district": "Center of Faith Relief Camp, Glow City, Redmond Barrens",
        "security_level": "Corporate High Security",
        "controlling_org": "Project Hope",
        "summary": "A Seattle Medical Bureau-approved clinic upstairs; four operating rooms, Renraku's experiment records and the hive's big metal doors in the basement",
        "description": (
            "A large white structure, officially the camp infirmary: a twenty-bed clinic with 2D6 squatter "
            "patients and 1D6 street docs who suspect nothing (or are paid too well to ask). Main floor (map "
            "p.41): entrance and administration, recovery rooms, office, examination rooms, bathroom, the "
            "elevator at the end of the hall. Lower level: preparation room, four sophisticated operating "
            "rooms, recovery, the office holding the Project Hope central computer, and the big metal doors at "
            "the end of the corridor -- the main entrance to the hive. When the runners arrive one theater is "
            "in use, messy experimental surgery with no anesthetic (make the screamer somebody they met)."
        ),
        "notes": (
            "Elevator: keycard plus thumbprint, maglock / cardreader / scanner all Rating 5; any failure sounds "
            "an alarm in the computer room, alerts Tung and brings four PEOs to the elevator in exactly five "
            "minutes, who ride down unless it is disabled. Only high-ranking Project Hope staff carry keycards. "
            "Three mercenary Street Docs run the theater: they know a megacorp pays, not which, and are "
            "afraid of the doors. Upper-floor terminals show the directories but no data; the central "
            "processor is in the basement (prep doc). Tung is here overseeing an operation; alerted, he copies "
            "the files to a portable, purges memory and storage in four Combat Turns and runs through the "
            "doors, leaving them unlocked (Barrier 35, Rating 7 maglock). Computer (3) on the activity log: "
            "purged moments ago. If Tung is already dead, another senior manager with identical stats does "
            "it. Bugging out instead means fighting the four PEOs at the elevator."
        ),
    },
    {
        "name": "Glow City Hive Caverns",
        "location_type": "insect spirit hive",
        "district": "Beneath Faith Relief Camp, Glow City, Redmond Barrens",
        "security_level": "Zero Zone -- Lethal Response",
        "controlling_org": "The Ant Hive (Glow City)",
        "summary": "Half a kilometer of mold-lined tunnel to a 200-meter cocoon cavern -- the chase after Tung, and the place the UCAS fills with fuel-air explosive",
        "description": (
            "Beyond the metal doors a narrow tunnel cut through bedrock drops steeply and turns right; the "
            "walls are furred with repulsive green mold (ant food) and the air smells wrong. Worker-carved "
            "passage merges with a larger natural tunnel that snakes so sharply there is almost never line of "
            "sight, then after about half a kilometer opens more than halfway up the wall of a huge cavern: "
            "200 m long, fluorescent lights on the ceiling 20 m up, the floor 50 m below down a 45-degree "
            "slope, and clumps of cocoons of fifteen or more pods each where the hive turns humans into ants. "
            "Side passages the runners 'just happened to miss' let the true-forms in behind them (map p.43: "
            "big metal door, side passages, cocooning room)."
        ),
        "notes": (
            "Tung runs at Quickness 6 (his Cast entry says 3); matching him means full speed on slick ground, "
            "Athletics (2) each round or lose a round. Shots at him on the way get partial cover, impaired "
            "visibility, running target and running attacker on difficult ground. The runners must climb about "
            "20 m to reach him on the wall, take the portable, and get out as 20+ flesh-form soldiers climb "
            "the last couple of meters below them; two Force 5 true-forms and eight-plus PEOs block the "
            "tunnel at the worst moment. If he cannot be stopped, the strain of summoning distracts the Queen "
            "enough to drop her Willpower shield over him. More than 500 spirits below; a team that goes "
            "deeper gets ants until it runs. Destroyed by UCAS soldiers with fuel-air explosives within a day "
            "of Juarez hearing about it -- the Seattle Datafax reports a methane pocket at 4:34 a.m."
        ),
    },
    {
        "name": "Tranquility Relief Camp",
        "location_type": "relief camp / work camp",
        "district": "Redmond Barrens (exact site not given)",
        "security_level": "Corporate High Security",
        "controlling_org": "Project Hope",
        "summary": "Another interchangeable spot of green in the Barrens; where Clint Ranger did his midnight decking and was taken from his bunk",
        "description": (
            "One of Project Hope's ten camps, indistinguishable from Hope: the same renovated two-story "
            "buildings, the same work, the same four-week turnover. Clint Ranger spent three weeks here after "
            "his month at Hope, twice slipping into the records office to deck the project terminal (a "
            "legitimate charity, thousands of donors, one 10,000-nuyen Renraku gift) before goons with "
            "reinforced plastiform cuffs and a narcoform rag woke him one morning."
        ),
        "notes": (
            "Prologue only (pp.4-6). From here the kidnappers' van drove exactly 9 minutes 18.17 seconds to an "
            "operating room behind pneumatic doors, an ID check and a magical barrier -- almost certainly "
            "Faith camp's medical center. Ranger's fate is the book's opening image: a man and a woman in "
            "lab coats salvaging his cyberware for resale and choosing between an undamped full-sensory BTL "
            "chip and the alpha-test 'RADOC cybernetic modification'."
        ),
    },
    {
        "name": "New Dawn Environics Kent Facility",
        "location_type": "corporate facility",
        "district": "Kent",
        "security_level": "Corporate Extraterritorial",
        "controlling_org": "New Dawn Environics",
        "summary": "Research facility crossed with a park -- songbirds on the guards' AK-97s, a brook under the electric fence, and a 100-by-150-meter effluent pool of larvae and human hosts below",
        "description": (
            "'Just like your standard medium-sized research facility', except that it is also a pastoral park: "
            "forest, a babbling brook, birdsong, a 4-meter chain-link electric fence and armed guards. Compound "
            "(map p.34): the NDE building, parking, the truck entrance, a security building, forested area and "
            "brook. Silver tanker trucks plastered with biohazard warnings roll through the gate and vanish "
            "into a door in the main building's side. Main floor: lobby, research labs and offices full of "
            "industrious flesh-form workers who used to be scientists and secretaries; a locked elevator in the "
            "northeast corner. Lower level: two docking bays and pumping rooms on the west side, and the "
            "effluent pool -- pitch dark, a stench of toxic waste and rotting flesh, a strip of solid ground and "
            "then 100 by 150 meters of popping brown sludge in which naked, bloated, sore-covered hosts float "
            "grafted to hissing dog-sized larvae while a brown shape with spindly arms rises from the middle."
        ),
        "notes": (
            "Getting in: sneaking is near-megacorp difficulty; the easy-not-easy way is a truck from Hope camp "
            "(guards sweep the cab with a Rating 5 chemsniffer and the driver with a Rating 4 metal detector "
            "but never the cargo; GMC 4201 tanker, Handling 3/6, 35/85, B/A 5/3, 37.5 kL; Mechanic-archetype "
            "drivers with Car 3). Fence Barrier 24, gates 20, 8D shock, alarms everywhere. Five guards patrol "
            "the first floor and look into every room every ten minutes; every guard carries an elevator "
            "keycard; two guards and four workers run the docking bays. Astral: three Force 4 watchers on the "
            "perimeter, three Force 5 true-form soldiers inside. The pool: a toxic earth spirit (B8 Q2x2 S8 "
            "W4; Alienation, Concealment, Corrosive Secretions, Fear, Noxious Breath), a toxic water spirit "
            "(B6 Q4x2 S4 W4; Accident, Alienation, Corrosive Secretions, Engulf, Fear, Movement, Search) and "
            "ten dragonfly larvae (B6 Q4x4 S4 I3 W4, R4; 4M; Corrosive Saliva, Enhanced Reactions, Enhanced "
            "Senses (Smell, Hearing, Vibration), Venom; dual beings smarter than a troll), all ordered to attack "
            "anyone in reach. A ceiling siphon draws off the purified water and soil to the outgoing trucks. "
            "The computer system is mapped in the prep doc. Nothing here is required to finish the adventure; "
            "it exists to show the team what it is up against, and a team that has met bugs before may pull "
            "the plug right here."
        ),
    },
    {
        "name": "McHugh's (Fourth and Blanchard)",
        "location_type": "restaurant",
        "district": "Fourth Avenue and Blanchard Street, Downtown",
        "security_level": "Patrolled / Commercial",
        "summary": "Fast-food franchise under the old golden arches: armed guards, macroplast furniture, clear fields of fire -- the one place nobody gets double-crossed; Juarez's meet",
        "description": (
            "If any place exists where it is impossible to double-cross somebody, McHugh's is it: armed "
            "guards, bolted macroplast furniture, clear fields of fire, walls in jarring colors and subtly "
            "disturbing muzak designed to make you bolt your food and leave. Layout (map p.16): food "
            "preparation area, manager's office, storeroom, men's and women's washrooms, marked guard "
            "positions. Yellow tables."
        ),
        "notes": (
            "Juarez's team arrives thirty minutes early: two FBI Snipers across the street (B6 Q5 S5 C2 I3 W4, "
            "Ess 3.4, R4(6); TR 3/3; Firearms 4, Stealth 3; thermographic cybereyes, Wired 1; Ranger Arms SM-3 "
            "with magnification 3 thermo scope and gas-vent III, Uzi III, armored vest with plates 4/3) "
            "listening on his wire and shooting if he sounds in trouble. He lets the runners stew five "
            "minutes, walks in by the main doors and sits down. He will agree to another meeting place only if "
            "it is as safe as McHugh's -- 'not many places are'. Have the runners order some fries."
        ),
    },
    {
        "name": "DocWagon Research and Storage Facility (Cherry and 13th)",
        "location_type": "research lab",
        "district": "Cherry Street and 13th Avenue, Downtown (First Hill)",
        "security_level": "Corporate High Security",
        "controlling_org": "DocWagon",
        "summary": "Heavily guarded DocWagon storage and research building from which a lone Jackrabbit carries DNA and blood samples to Auburn at 10 a.m.",
        "description": (
            "DocWagon's research and storage facilities at Cherry Street and 13th Avenue, where hundreds of "
            "man-hours of DNA sample boards and blood are kept refrigerated. 'Heavily guarded, and only "
            "foolish runners would try to assault' it -- the courier car on the open road is the target."
        ),
        "notes": (
            "Six Feet Under (p.13): at about 10 a.m. a lone Chrysler-Nissan Jackrabbit (Handling 3, 25/75, B/A "
            "1/0, Sig 5; rear modified for a 1-cubic-meter, 40 kg cooled storage box) drives straight to "
            "Response HQ 1 in Auburn. Courier: hireling, TR 1/1, Colt American L36, gives up the keys at the "
            "first gun. Daylight hijack: Lone Star in droves unless it is quick and clean. Fee 8,000 nuyen for "
            "the group. Juarez films everything; the loss 'upsets DocWagon' enough for blackmail to bite."
        ),
    },
    {
        "name": "DocWagon Response HQ 1 (Auburn)",
        "location_type": "corporate facility",
        "district": "Pacific and First Avenues, Auburn",
        "security_level": "Corporate High Security",
        "controlling_org": "DocWagon",
        "summary": "DocWagon's Auburn response headquarters, destination of the sample courier; heavily guarded",
        "description": (
            "One of DocWagon's response headquarters, at Pacific and First Avenues in Auburn, where the "
            "refrigerated sample case was bound. Heavily guarded; not a place to hit."
        ),
        "notes": "Named only as the courier's destination (p.13). Response teams launch from here for the south sprawl.",
    },
    {
        "name": "Glow City (Redmond Barrens)",
        "location_type": "barrens district",
        "district": "Glow City, Redmond Barrens",
        "security_level": "No Security / Barrens",
        "summary": "The most dangerous part of Seattle: burnt-out houses, stripped cars, layered gang tags -- and ten spots of Project Hope green, one of them over a hive",
        "description": (
            "The Glow City region of the Redmond Barrens, deep in the sprawl's blighted east: burnt-out "
            "houses, cars stripped to their frames, street people shambling in rags, walls under so many "
            "layers of spray paint (the Nightstalkers? the Splatters? the Butchers?) that no insignia can be "
            "told from the next. Buses and cabs stopped running here years ago. Project Hope's relief camps "
            "sit inside it behind electrified fences, orchards growing in trucked-in soil over the Mount St. "
            "Helens ash; a large complex of natural caves runs underneath, known to the UCAS Geological "
            "Service."
        ),
        "notes": (
            "The bus from Seneca Street takes well over half an hour and is sealed and unventilated on a hot "
            "day (Body (4) not to be sick). About 110 people have gone missing in and around the Redmond "
            "Barrens this year, 'a normal 30 percent increase'; Lone Star reinforces Redmond generally but "
            "declines to step up in Glow City. The success handout's 'underground explosion' is here. Earlier "
            "books put the Puyallup hive and Dreamchipper's Redmond gang wars nearby; this is the same "
            "Barrens a few years on."
        ),
    },
]

NPCS = [
    {
        "name": "Simon Juarez",
        "role": "FBI special agent who films the runners' crimes and blackmails them into Project Hope; pays well, lies about the originals, never gets his own hands dirty",
        "archetype": "Government Agent",
        "title": "Special Agent, UCAS Federal Bureau of Investigation",
        "race": "Human",
        "gender": "Male",
        "organization": "UCAS Federal Bureau of Investigation",
        "connection": 4,
        "description": (
            "Tall, short-cropped straight black hair, inexpensive black suit and matching tie ('doesn't the "
            "UCAS hand those things out?'), mirrored sunglasses, a little cord hanging from his ear. Crisp, "
            "carefully enunciated syllables that he enjoys every microsecond of; thick fingers tapping a vid "
            "player on a yellow McHugh's table. Arrogant because he believes the trap is airtight. 'I know what "
            "you do, and I know how you do it. But most important, I know what you've done.'"
        ),
        "background": (
            "Ten years enforcing UCAS federal law, most of it repulsive; he would have stayed home in his "
            "father's soya food store if he had known. It took him a decade to climb out of the Bureau's seedy "
            "underbelly to the perfect spot where intermediaries and subcontractors do the dirty work and a "
            "whole database of people can take the blame. Assigned to Project Hope after Clint Ranger "
            "vanished, he chose to blackmail -- er, hire -- disposable help: two fake cakewalk runs through the "
            "team's own fixer, drones and cameras on every move, and a copy of the vids in the 'postmortem "
            "mail' that goes to Aztechnology and DocWagon if his telecom computer reads his obituary or he "
            "misses a check-in."
        ),
        "notes": (
            "Offer: 5,000 each to show up, 30,000 each (15,000 up front) for anything proving what Renraku is "
            "doing with Project Hope, extra for anything else useful to the UCAS, non-negotiable, and never "
            "tell anyone but him. His four leads: the Seneca Street office, the Glow City camps' 'unusually "
            "high security', New Dawn Environics in Kent, and other unknown investigators. Afterwards he pays "
            "the balance, asks if the copy is the only one (they lie), says the vids are the originals (he "
            "lies), swears the team to silence about the hive and sends UCAS soldiers with fuel-air explosives "
            "-- an invitation and 5,000 more each if the team was a big help. He wants leverage on Renraku, not "
            "a court case; loose talk about bugs gets the vids used, then a combat team and 'protective "
            "custody'. Stats: B4 Q6 S4 C4 I5 W4, Ess 2.6, R5(7); TR 4/3; Car 4, Computer 4, Etiquette "
            "(Corporate) 3, (Government) 4, (Street) 4, Firearms 6, Negotiation 6, Psychology 3, Stealth 4; "
            "chipjack with Federal Laws and Regulations chip 5, datajack 50 Mp, smartlink, Wired 1; Ares "
            "Predator (smartlink), armor clothing 3/1, credstick with 100,000 nuyen, micro-transceiver, boosted "
            "ear phone. Legwork TN 6 (fixer, government, reporter): 'He doesn't like to get his hands dirty, "
            "even if keeping clean means letting somebody else get geeked.' Killing him buys the Bureau's "
            "full attention."
        ),
        "contact_skills": ["Federal leverage and deniable government work", "Blackmail he will never quite stop holding"],
    },
    {
        "name": "Jonathan Tung",
        "role": "Charismatic director of the Hope Relief Camp, Project Hope's public face -- a flesh-form worker ant who loves his Queen and thinks the experiments a necessary sacrifice",
        "archetype": "Camp Director / Flesh-Form Ant Spirit",
        "title": "Director, Hope Relief Camp, Project Hope; formerly PR manager, Lifeline Education",
        "race": "Human (flesh-form ant worker)",
        "gender": "Male",
        "organization": "Project Hope",
        "connection": 4,
        "description": (
            "Mid-fifties, dark skin, black hair cropped short, surprisingly muscular and dexterous for his "
            "age; first seen teaching an enrollee to use an autohammer and running over to shake hands. Warm, "
            "caring, friendly, almost too good to be true -- 'I like to think of them as my family' -- with a "
            "speech about a loving community that sends shivers up a cynic's spine. Office hours ten to noon "
            "and four to six; otherwise 'somewhere around the camp, generally making myself useful'. No "
            "physical sign of what he is; masks his aura."
        ),
        "background": (
            "Public-relations manager for Lifeline Education, a Brotherhood-owned institute he defended for "
            "years against reporters calling it a glorified cult, which made him the ideal relief-camp "
            "director. When ant spirits saturated the Universal Brotherhood his public position made it vital "
            "that he be transformed; the bonding went well. More than five years since he first felt the "
            "Queen's overwhelming love, he has devoted his life to sharing it with a mankind that seems less "
            "than willing. Renraku's money is the only way to build the new hive; the experiments sadden his "
            "heart and keep him warm at night as a just cause. He wrote 'Understanding the Hive Mind' (Handout "
            "1): insects are not evil, merely alien; democracy is dated; join the loving embrace."
        ),
        "notes": (
            "Wakes the whole camp at 7 a.m. with a guard escort; questions about Renraku, the Brotherhood or "
            "Clint Ranger set off alarms in his head (+2 Awareness) and he has the guards watch you; his "
            "digital signature authorizes every transfer, and on Day 7 he transfers the runners to Faith as "
            "experiment candidates. Mind Probe meets two Resistance Tests (his Willpower, then the Queen's "
            "10); beat only his and you see the loving family man and a blocked region. At the medical center "
            "he copies the paydata to a portable, purges the system in four turns and runs -- Quickness 6 in "
            "the chase, 3 in the Cast (book inconsistency) -- down the wall of the cocoon cavern with the "
            "computer. Stats: B4 Q3 S3 C6 I3 W3, Ess 6(A), R12, Initiative 22+1D6; TR 6/4; Computer 4, "
            "Etiquette (Corporate) 3, Negotiation 6, Psychology 3; pocket secretary, portable phone. Share Minds "
            "means the Queen sees what he sees. If killed earlier, 'another senior manager with exactly the "
            "same attributes' fills in. The portable holds the medical records, proof of Renraku and of "
            "Brotherhood ownership, and his encrypted essay."
        ),
    },
    {
        "name": "The Glow City Hive Queen",
        "role": "Force 10 ant queen beneath Faith camp who telepathically runs Project Hope and shields every servant with her Willpower",
        "archetype": "Insect Spirit Queen",
        "title": "Hive Queen of the Glow City hive (Force 10; killed her summoner long ago)",
        "race": "Insect spirit (Ant Queen)",
        "gender": "Female",
        "organization": "The Ant Hive (Glow City)",
        "connection": 1,
        "description": (
            "Nearly four meters long, a bloated hybrid of metahuman and ant. An atypical Queen: Force 10, "
            "an extraordinarily high Willpower, and powers no other queen in print has. She is never met on "
            "stage -- the runners feel her through the guards who move too fast, the shamans who follow Ant, "
            "the telepathic alarm that puts twenty soldiers on the cavern wall the moment Tung knows he is "
            "followed."
        ),
        "background": (
            "The conduit of power for the insect shaman who summoned her, whom she killed when he ceased to "
            "be useful; the book assumes he died long ago and gives no summoning rules. Through the Universal "
            "Brotherhood's shell companies she runs Project Hope and the Kent plant, diverting Renraku's "
            "research money into cocoons and larvae and choosing her best-bonded flesh-forms for the jobs "
            "among humans. Her plan is to share her love with the entire population of Seattle."
        ),
        "notes": (
            "Stats: B15 Q16x5 S16 C10 I10 W10, Ess 10(A), R30, Initiative 40/50+1D6 (+20 astral, +10 "
            "manifest); TR (F)/4; melee uses Force for skill dice. Powers: Animal Control (Ants), Compulsion "
            "(pheromones to Force meters, or secreted into food, drink and drugs), Enhanced Senses (Smell), "
            "Fear, Immunity to Normal Weapons, Paralyzing Touch, Share Minds (two-way telepathy with every "
            "subject; subjects relay through her and rarely dare), Share Willpower (add 10 to any subject's "
            "Willpower against mind-affecting spells; failing to overcome it costs +1 Brotherhood Awareness), "
            "Summoning (Force spirits a day), Venom. Weaknesses: Reduced Senses (Sight), Vulnerability "
            "(Insecticides). The New Dawn soldiers are not under her Willpower; Tung, the PEOs and Armstrong "
            "are. The strain of summoning the cavern reinforcements can drop her shield over Tung. Dies "
            "off-stage with everything else when the UCAS fuel-air charges go off. Whether her extra powers "
            "are unique to her, shared by other atypical queens, or the future of all queens is for the GM."
        ),
    },
    {
        "name": "Clint Ranger",
        "role": "FBI special agent who went into the camps as a vagrant, dug orchards for seven weeks, and ended strapped to a table under narcoform (prologue)",
        "archetype": "Government Agent",
        "title": "Special Agent, UCAS FBI (missing, presumed dead or worse)",
        "race": "Human",
        "gender": "Male",
        "organization": "UCAS Federal Bureau of Investigation",
        "connection": 2,
        "description": (
            "A better-than-average government agent by his own estimate, ten years in, cynical enough to "
            "know nobody helps for helping's sake, and easily disguised as one more bum on the Seneca Street "
            "chairs -- until he noticed he was the only man on the bus without lice. Hates heat, hates hard "
            "work in heat, and by the end could take real pride in a porch he had built."
        ),
        "background": (
            "Sent by his director less than two months before the adventure to get inside a Barrens relief "
            "camp and find why Renraku was shoveling nuyen into Project Hope. Four weeks at Hope camp, "
            "three at Tranquility, two midnight decking sessions that found a legitimate charity and one "
            "10,000-nuyen Renraku donation, and three questions he could not answer: where the water and "
            "soil came from, why nobody took his name, and why nobody stayed longer than four weeks. Then the "
            "drek found him: cuffed and chloroformed in his bunk (his lung filters beat the narcoform), a "
            "nine-minute van ride, a ward, an operating room and reinforced plastiform straps that did not "
            "give a millimeter."
        ),
        "notes": (
            "Cyberware named on the surgeons' notepad: cybernetic left eye, respiratory system and right arm, "
            "enhanced left arm and both legs, internal chronometer, a chipslot -- all to be salvaged for "
            "resale before the surgeons implant an undamped full-sensory BTL chip (the alternative was the "
            "alpha-test 'RADOC cybernetic modification'). His fate is never resolved; the GM may put him on "
            "the Faith camp operating table when the runners arrive (one box left on each monitor) or in a "
            "cocoon. Asking about him in Tung's hearing is worth +2 Brotherhood Awareness."
        ),
    },
    {
        "name": "Ms. Montagu",
        "role": "Project Hope caseworker in the latest corporate fashion who processes the runners into Hope Relief Camp without caring who they are",
        "archetype": "Caseworker",
        "title": "Caseworker, Project Hope Enrollment Center",
        "race": "Human",
        "gender": "Female",
        "organization": "Project Hope",
        "connection": 1,
        "description": (
            "Dressed in the latest corporate fashion, holographic ID badge on the jacket, portable computer "
            "in hand, olfactory inhibitor turning the waiting room into roses. 'This tells me that you have "
            "decided to change your lives for the better, and I'm thrilled that Project Hope can help you do "
            "this. If you're illiterate, I can arrange for a voice-recognition unit.'"
        ),
        "notes": (
            "Paid to collect applicant data, raise spirits and route people to the right camp; has no idea what "
            "Project Hope really does and 'couldn't give a flyin' frag'. Her computer checks Lone Star for "
            "warrants and recommends immediate admission to Hope; bus in three hours. Stats: B2 Q3 S2 C4 I4 "
            "W2, R4; TR 1/1; Computer 3, Etiquette (Corporate) 2; olfactory inhibitor, pocket secretary."
        ),
    },
    {
        "name": "Garder Armstrong",
        "role": "The Brotherhood's plant in Hope camp: a friendly long-timer who 'knows the password' -- actually a Force 6 flesh-form worker ant sent to entrap the runners",
        "archetype": "Infiltrator / Flesh-Form Ant Spirit",
        "title": "Universal Brotherhood plant, Hope Relief Camp",
        "race": "Human (flesh-form ant worker)",
        "gender": "Male",
        "organization": "Universal Brotherhood",
        "connection": 2,
        "description": (
            "Looks entirely human and dresses like any other enrollee; claims to have been in the camp a good "
            "while. The friend with access you wish you had: says he overheard two managers five months ago, "
            "learned the system password and has been decking himself easy jobs ever since, and offers to fix "
            "your schedule. Masks his aura and stands under the Queen's Willpower."
        ),
        "notes": (
            "Arrives as soon as the runners have 1 Brotherhood Awareness Point. He does not have the "
            "password -- the managers change schedules for him out of love for the Queen. Ask him to help "
            "break into the database and the team's ulterior motive is proven; failing that, 'real food', "
            "better entertainment, anything to be trusted. When he learns why they are here he reports: +5 "
            "Brotherhood Awareness. Stats: B4 Q4 S3 C3 I4 W4, Ess 6(A), R3, +10 Initiative (13+1D6); TR 3/3; "
            "Computer 3, Etiquette (Corporate) 2, (Street) 4, Firearms 4, Negotiation 4, Stealth 5; Ares "
            "Predator hidden in his quarters, portable phone. Force 6 flesh-form worker."
        ),
    },
    {
        "name": "Ted Wiley",
        "role": "Private investigator on the EPA's payroll, a week into Hope camp, tracking New Dawn's trucks and looking for a diversion",
        "archetype": "Private Investigator",
        "title": "Private investigator under contract to the UCAS Environmental Protection Agency",
        "race": "Human",
        "gender": "Male",
        "organization": "UCAS Environmental Protection Agency",
        "connection": 3,
        "description": (
            "An enrollee like any other who has learned more than he ever wanted about horticulture, "
            "carpentry and brotherly love, and who watches the guards a little too carefully. Wired, chipped, "
            "camera eyes, and no gear at all inside the wire."
        ),
        "background": (
            "Hired when the EPA's court orders ran out; a little digging showed Project Hope was New Dawn "
            "Environics' largest customer and that both seemed to belong to one larger corporation, so he "
            "enrolled where he would not be noticed. A week in he has done a little decking, knows how the "
            "camp system works, who holds the passwords and where the central system is, and has clocked "
            "that the guards react faster than anyone should -- wired, drugged or bioteched, he does not know."
        ),
        "notes": (
            "Timeline: on the morning of Day 5 he means to slip onto a New Dawn truck and ride it back to "
            "Kent; all he lacks is a diversion. At EPA Awareness 4 he offers the runners 10,000 nuyen on his "
            "return for helping him aboard; at 5+ the EPA has him offer 10,000 for any court-usable data. At "
            "2-4 he tells them to stop making noise and threatens an arrest he cannot make without blowing "
            "cover. If the team cannot see the New Dawn connection, he points it out. Stats: B6 Q5 S4 C3 I4 "
            "W5, Ess 3, R5(6); TR 3/4; Computer 3, Etiquette (Corporate) 4, (Street) 4, Firearms 4, Government "
            "Procedures 4, Negotiation 3, Stealth 3; chipjack, cybereyes (camera, low-light), Wired 1. The "
            "timeline calls him an 'EPA agent'."
        ),
        "contact_skills": ["EPA investigations and environmental-crime paperwork", "Who is watching whom inside the camps"],
    },
    {
        "name": "Casey Hughes",
        "role": "Hand-picked Renraku agent living as an enrollee to make sure nobody has gotten wise before the corp pulls its data out early; flags chromed runners for the surgeons",
        "archetype": "Corporate Agent",
        "title": "Renraku Computer Systems field agent, Hope Relief Camp",
        "race": "Human",
        "gender": "Female",
        "organization": "Renraku Computer Systems",
        "connection": 3,
        "description": (
            "Dresses like an enrollee and carries nothing but a concealable Rating 3 metal detector, which "
            "she runs over anyone interesting. Has clout in the corporation and knows it. In her opinion "
            "almost anything the runners do qualifies as suspicious activity."
        ),
        "notes": (
            "Renraku trusts nobody, least of all its partner in crime: she is here to watch the camp through "
            "the pull-out. Cyberware found by her detector gets the owner flagged for experimentation (the "
            "doctors prefer pre-cybered patients) -- +1 Renraku Awareness per chromed runner. She turns the "
            "runners in only if they seriously threaten her mission, and then by arranging their transfer to "
            "Faith for surgery rather than telling Project Hope what she is. Renraku ladder: 1 detection "
            "systems up a rating (the system slows); 2-4 PEOs arrest the team on 'corp land' for up to a "
            "week; 5+ Renraku pulls out one week later and disposes of them. Stats: B4 Q4 S5 C3 I5 W4, Ess "
            "4.7, R5; TR 4/4; Car 4, Computer 3, Etiquette (Corporate) 4, Negotiation 5, Psychology 4; "
            "chipjack, cybereyes (camera), telephone."
        ),
    },
    {
        "name": "Enrico Sanchez",
        "role": "Aztechnology's man in the camps -- longest-serving of all the spies, holds the password, knows Renraku's pull-out hour and runs the Day 10 datasnatch",
        "archetype": "Corporate Agent",
        "title": "Aztechnology agent, Hope then Faith Relief Camp",
        "race": "Human",
        "gender": "Male",
        "organization": "Aztechnology",
        "connection": 3,
        "description": (
            "Quiet, quick and very well prepared: a bug scanner, a boosted earplug phone and a microcamera "
            "where the guards found nothing. Notices chrome on sight and 'just happens' to be nearby when "
            "somebody breaks into something."
        ),
        "background": (
            "Aztechnology has known for some time that Renraku pays Project Hope to experiment on unwilling "
            "subjects and means to steal the results, secure that Renraku cannot sue without hanging itself. "
            "Sanchez has stayed longest and learned most: the system password, the exact day and hour Renraku "
            "leaves, and the honor of orchestrating the theft. Four days before it he decks himself a transfer "
            "to Faith (Day 7 in the timeline) -- and the runners with him if he has recruited them."
        ),
        "notes": (
            "Aztech ladder: 1-4 he tells the runners to keep their investigation quieter; 5+ he offers 30,000 "
            "nuyen to break into Faith camp's medical facility, steal the experimental data and erase every "
            "copy and backup; the top tier (only if Juarez has released his vids) is a 10,000-nuyen bounty "
            "on each runner for two years. His raid on Day 10 is a dozen or fewer Bodyguard / Combat Mage / "
            "Street Samurai archetypes who expect human security guards and are cut to pieces. Stats: B5 Q6 "
            "S4 C3 I6 W5, Ess 4, R6(8); TR 4/4; Car 5, Computer 3, Etiquette (Corporate) 5, Negotiation 4, "
            "Stealth 5; Wired 1; bug scanner 4, earplug phone with booster, microcamera."
        ),
    },
    {
        "name": "Andrew Mitchell",
        "role": "Seattle Times reporter undercover in Hope camp who asks the wrong questions at breakfast and is dragged away by three PEOs -- comes back months later, changed",
        "archetype": "Reporter",
        "title": "Reporter, Seattle Times",
        "race": "Human",
        "gender": "Male",
        "organization": "Seattle Times",
        "connection": 2,
        "description": (
            "A man who joins the runners' breakfast table, shoots the drek for a few minutes and then asks, "
            "'So, have you seen anything strange going on here?' and 'What do any of us really know about "
            "Project Hope?' -- just before three Peace Enforcement Officers storm in and drag him out. 'Andy' "
            "to his paper."
        ),
        "notes": (
            "Tung caught him investigating off-limits areas and ships him to Faith camp 'to get a new slant on "
            "life as an insect spirit'. He somehow escapes the final battle and returns to the newspaper a few "
            "months later with his stories' biting edge gone and no more undercover work; runners may spot his "
            "face beside a byline. The encounter exists to add paranoia, not a rescue plot. No stats given."
        ),
    },
    {
        "name": "Lt. Dan Akkison",
        "role": "Lone Star lieutenant quoted after a two-and-a-half-hour running gunfight from Downtown into the Redmond Barrens killed two of his troopers and eight bystanders",
        "archetype": "Police Officer",
        "title": "Lieutenant, Lone Star Security Services",
        "race": "Human",
        "gender": "Male",
        "organization": "Lone Star Security",
        "connection": 2,
        "description": (
            "'These people are criminals, pure and simple, and I'm tired of society trying to glorify them. "
            "They'd like everyone to believe they're Robin Hood, robbing the rich corps and saving the "
            "downtrodden poor. Truth is, they're just criminal mercs in it for the cash.' Said surveying the "
            "scene where two troopers under his command died."
        ),
        "notes": (
            "Seattle Datafax handouts 3 and 4 (p.61-62): multi-service Lone Star elements chased a vanload of "
            "'so-called shadowrunners' from the Downtown zone deep into the Redmond Barrens; eight innocent "
            "bystanders killed and twenty-seven injured by stray gunfire, magic and vehicles; the runners "
            "escaped. The story runs whatever the team does; if the GM likes, the vanload was them leaving "
            "Faith camp."
        ),
    },
    {
        "name": "Eva Leuwendyke",
        "role": "UCAS Geological Service spokesperson who explains the hive's destruction to the press as a methane pocket in a known cave complex",
        "archetype": "Government Spokesperson",
        "title": "Spokesperson, UCAS Geological Service",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": (
            "'We've known about a large complex of underground caves in the area for quite some time. The "
            "explosion seems to have been caused by a large natural build-up of methane gas; some unsuspecting "
            "spelunker probably lit a cigarette and blew up the gas pocket.'"
        ),
        "notes": (
            "Seattle Datafax Handout 3 only: the 4:34 a.m. 'Underground Explosion' under Glow City, felt as "
            "far as Tacoma, with UCAS rescue teams sent into the caverns that no one expects to find alive. "
            "Whether she knows what she is covering is not said."
        ),
    },
]

ORG_UPDATES = {
    "Universal Brotherhood": {
        "notes_append": (
            "Double Exposure (2055): the mask comes off. Through a bewildering network of subsidiaries and "
            "shell corporations the Brotherhood owns Project Hope (ten relief camps in the Barrens), New Dawn "
            "Environics (the extraterritorial waste-to-water corp in Kent; the NDE computer names the parent "
            "as 'Universal Brotherhood International') and Lifeline Education (a 'glorified cult' school). "
            "Ant spirits have 'saturated' the organization: at the Hive Queen's behest it diverts most of the "
            "money Renraku pays Project Hope for medical experiments into building a hive of 500-plus spirits "
            "under Faith Relief Camp, and it plants flesh-form workers such as Garder Armstrong and camp "
            "director Jonathan Tung wherever the public looks. Ending: the UCAS government learns the "
            "bug connection but dares not say so; it issues warrants for executives of the Seattle chapter "
            "for tax evasion and corruption (Project Hope as a criminal tax-write-off sham), saturates the "
            "media, and the FBI and other agencies raid the hives beneath many Brotherhood chapter houses -- "
            "reported as 'a spate of unmotivated terrorist violence against the troubled Universal "
            "Brotherhood'. Within a couple of months it is destroyed as a major force in the UCAS and goes "
            "underground elsewhere; 'subsequent events in Chicago' follow. NOTE: the Queen Euphoria note above "
            "defers the bug link to Missing Blood (#25); in campaign order this book (#23) exposes it first, "
            "though only to the government and the runners."
        ),
        "leadership_add": [
            {"name": "Jonathan Tung", "title": "Director, Hope Relief Camp (Project Hope front)", "notes": "Flesh-form ant worker; former Lifeline Education PR manager."},
            {"name": "Garder Armstrong", "title": "Plant inside Hope Relief Camp", "notes": "Force 6 flesh-form worker."},
        ],
        "allies_add": ["Project Hope", "New Dawn Environics", "The Ant Hive (Glow City)", "Lifeline Education"],
        "enemies_add": ["UCAS Federal Bureau of Investigation"],
    },
    "Renraku Computer Systems": {
        "notes_append": (
            "Double Exposure (2055): to close the R&D gap with its competitors Renraku started several "
            "biotech projects needing large numbers of subjects and funneled 'enough money to buy small "
            "countries' into Project Hope -- publicly a 10,000-nuyen donation -- to run them on easily "
            "forgotten homeless enrollees at Faith Relief Camp: BTL chips, illegal simsense, non-elective "
            "cyberlimb modification, prototype bioware, and a nearly perfected 'subjective time dilation' "
            "simsense that makes two real days feel like 200 years in hell. It demanded intense security at "
            "the camp, never learned that its partner was the Universal Brotherhood or that its money was "
            "building an ant hive, and, trusting nobody, planned to pull out three days early (Day 11) with a "
            "team to 'steal' the data and destroy the evidence; the team is cut to pieces by flesh-form "
            "guards. Agent Casey Hughes watched the camp. The UCAS FBI (Juarez) now holds the records as "
            "leverage and 'declines to come down hard on Renraku', saving the dirt for a far-reaching plan. "
            "Seattle Datafax, which reports the collapse without naming Renraku, is 'A Division of Renraku "
            "Computer Systems'. Awareness ladder: 1 detection systems +1 rating; 2-4 PEOs hold the runners on "
            "corp land for a week; 5+ pull-out a week later and the runners arrested, killed or experimented "
            "on."
        ),
        "leadership_add": [
            {"name": "Casey Hughes", "title": "Field agent (Project Hope oversight)", "notes": "Hand-picked; has clout."},
        ],
        "allies_add": ["Project Hope", "Seattle Datafax"],
    },
    "Aztechnology": {
        "notes_append": (
            "Double Exposure (2055): the first set-up run hijacks an Aztechnology van of cyberlimb spare parts "
            "leaving the Seattle pyramid at 22:00 for a research facility just south of the Tacoma city "
            "center -- 40 minutes down I-5, lightly guarded because Aztech believed the transfer secret "
            "(Driver: VCR 1, Uzi III; three guards with AK-97s behind gunports; armored truck Handling 4, "
            "30/120, B/A 4/12). Inter-corp etiquette means Aztech ignores minor damage until someone tells it "
            "who to blame -- which is Juarez's threat. Aztechnology has known for some time that Renraku pays "
            "Project Hope for illegal experiments and means to steal the results (Renraku cannot sue without "
            "hanging itself): agent Enrico Sanchez runs the Day 10 raid on Faith camp's medical center, which "
            "the flesh-form guards destroy. Aztech ladder: 1-4 Sanchez warns the runners to be quieter; 5+ "
            "offers 30,000 nuyen to steal and erase the data; if Juarez releases his vids, a 10,000-nuyen "
            "bounty on each runner for two years."
        ),
        "leadership_add": [
            {"name": "Enrico Sanchez", "title": "Field agent, Project Hope camps", "notes": "Orchestrates the Faith camp datasnatch."},
        ],
        "enemies_add": ["Project Hope"],
    },
    "DocWagon": {
        "notes_append": (
            "Double Exposure (2055): the second set-up run. DocWagon moves DNA sample boards and several pints "
            "of blood in a refrigerated 1-cubic-meter case from its research and storage facility at Cherry "
            "Street and 13th Avenue to Response HQ 1 at Pacific and First Avenues in Auburn, in a lone "
            "Chrysler-Nissan Jackrabbit at about 10 a.m. driven by a TR 1/1 hireling with a Colt American L36 "
            "who hands over the keys. Both buildings are heavily guarded. Hundreds of man-hours of samples "
            "lost; DocWagon 'will take the news very seriously' -- Juarez's other blackmail lever."
        ),
    },
    "UCAS Federal Bureau of Investigation": {
        "notes_append": (
            "Double Exposure (2055): the Bureau had an inkling of Renraku's use of Project Hope and saw a "
            "chance at tremendous leverage -- threaten to hand Renraku's methods to a few choice competitors "
            "-- so it sent Special Agent Clint Ranger into the camps as a vagrant; he disappeared within two "
            "months. Special Agent Simon Juarez then filmed a shadowrunner team on two set-up runs and "
            "blackmailed them in (30,000 nuyen each, snipers at the meet, postmortem mail). Outcome: the "
            "government learns of the bug connection and will not admit it; the FBI issues warrants for "
            "Project Hope's whole management (never served) and Seattle Brotherhood executives, a crack UCAS "
            "team destroys the Glow City hive with fuel-air explosives within a day, and FBI strike teams "
            "hunt hives beneath Brotherhood chapter houses across the country under cover of the 'heat wave'. "
            "Renraku is left alone -- the dirt is being saved. Juarez keeps copies of the vids and a combat "
            "team for 'protective custody' of anyone who talks."
        ),
        "leadership_add": [
            {"name": "Simon Juarez", "title": "Special Agent (Project Hope investigation)", "notes": "Blackmails the runners; keeps the vids."},
            {"name": "Clint Ranger", "title": "Special Agent (missing)", "notes": "Vanished from Tranquility Relief Camp."},
        ],
        "enemies_add": ["Universal Brotherhood", "Project Hope", "The Ant Hive (Glow City)"],
    },
    "Lone Star Security": {
        "notes_append": (
            "Double Exposure (2055): Project Hope's enrollment computer queries the Lone Star warrant "
            "database on every applicant and calls the nearest patrol on a hit -- troopers in force within "
            "minutes; the Enrollment Center's rent-a-cops also call the Star. A daylight hijack of the "
            "DocWagon Jackrabbit brings 'Lone Star troopers in droves'. Seattle Datafax handouts: Lieutenant "
            "Dan Akkison's two-and-a-half-hour running battle with a vanload of shadowrunners from Downtown "
            "deep into the Redmond Barrens (eight bystanders dead, twenty-seven injured, two troopers killed, "
            "runners escaped -- 'criminal mercs in it for the cash'); and, if the hive is never reported, Lone "
            "Star increases security in Redmond as a whole but declines to step up enforcement in Glow City "
            "despite about 110 disappearances this year."
        ),
        "leadership_add": [
            {"name": "Dan Akkison", "title": "Lieutenant", "notes": "Quoted in the Seattle Datafax after the running gunfight."},
        ],
    },
    "Shiawase Corporation": {
        "notes_append": (
            "Double Exposure (2055): Shiawase Envirotech holds about 70 percent of the Seattle sprawl's "
            "waste-disposal market; the other 30 percent belongs to the three-year-old, extraterritorial New "
            "Dawn Environics, which hopes its impossible toxic-effluent-to-drinking-water process in Kent will "
            "take a great deal more. Envirotech has an obvious interest in whatever exposes New Dawn."
        ),
        "enemies_add": ["New Dawn Environics"],
    },
    "The Ant Hive (Puyallup)": {
        "notes_append": (
            "Double Exposure (2055): the book recommends Queen Euphoria (and Missing Blood) for the mentality "
            "of the Hive Queen. A second, far larger hive -- 500-plus spirits under a fully summoned Force 10 "
            "Queen -- is found beneath Project Hope's Faith Relief Camp in Glow City, funded by Renraku via "
            "the Universal Brotherhood. The trideo 'Against the Hive Masters' made from Euphoria's abduction "
            "has destroyed the credibility of anyone who talks about bugs in public: 'Yeah, right. I saw that "
            "simsense, too. The Hive That Ate Tokyo, wasn't it?'"
        ),
    },
    "The Nightstalkers": {
        "notes_append": (
            "Double Exposure (2055): their insignia is among the layers of spray paint on the walls of Glow "
            "City on the road to Hope Relief Camp, with the Splatters and the Butchers -- so far from Bitter "
            "Creek that the runners cannot tell whose turf they are in."
        ),
    },
}

LOC_UPDATES = {
    "The Barrens (Seattle)": {
        "notes_append": (
            "Double Exposure (2055): Project Hope runs ten relief camps in the Redmond Barrens' Glow City "
            "(Hope, Faith and Tranquility named), busing in the homeless from Seneca Street to replant apple "
            "orchards over the Mount St. Helens ash behind electrified fences; nobody stays four weeks and "
            "people vanish in transfer. New Dawn Environics trucks the water and soil in from Kent. Under "
            "Faith camp an ancient cave maze holds an ant hive of 500-plus spirits, destroyed at the end with "
            "fuel-air explosives (a 'methane pocket', says the UCAS Geological Service). About 110 people have "
            "disappeared in and around the Redmond Barrens this year. See the Glow City (Redmond Barrens) row."
        ),
    },
    "Aztechnology Pyramid": {
        "notes_append": (
            "Double Exposure (2055): at exactly 10 p.m. a gray, nondescript armored van of cyberlimb spare "
            "parts leaves the pyramid, takes I-5 south and reaches a research facility just south of the "
            "Tacoma city center forty minutes later, lightly guarded because Aztech thinks nobody knows -- "
            "the runners' first set-up run, filmed by Juarez's drones. A bungled hit brings Aztech troopers."
        ),
    },
    "Aztechnology Tacoma Research Park": {
        "notes_append": (
            "Double Exposure (2055): the likeliest destination of the cyberlimb-parts van from the pyramid "
            "('one of their research facilities ... just south of the Tacoma city center', p.12); the book "
            "never names the site, so treat the link as the GM's choice. Cargo: standard spare parts for "
            "cybernetic limbs, no intact arms or reflex boosters, worth 5,000 nuyen to the fixer's buyer."
        ),
    },
}

NPC_UPDATES = {
    "Governor Schultz": {
        "notes_append": (
            "Double Exposure (2055, Seattle Datafax Handout 4, if the hive is never reported): asked about "
            "roughly 110 disappearances in and around the Redmond Barrens this year, the Governor called it a "
            "normal 30 percent increase -- 'go-gangs, cyberleggers, paranormal predators ... the crime rate "
            "alone might account for it' -- and, since so many of the missing are homeless, said the office is "
            "looking into a copycat serial killer 'similar to the Mayan Cutter'. 'There is, however, no cause "
            "for alarm.'"
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
The book gives no node tables at all -- every system is resolved with a single Computer Test or the
Virtual Realities fast-resolution rules, and none of them is on the public Matrix. Build them in the
designer only if the group wants a full run; otherwise the tests below are the whole rule set.

**1. Project Hope Enrollment Center database** (Seneca Street). Reached from the office terminals or by
breaking in after hours. Contains nothing about the Brotherhood or Renraku; the only paydata is a
complete list of everyone ever sent to the camps. Virtual Realities Fast Resolution System, Base TN 4.
A leased-line mail gateway (all e-mail encoded, nothing sensitive ever passed) links it to the camp
systems -- the only wire in or out.

**2. Hope Relief Camp central system** (room behind Tung's office, registration building). Not connected
to the outside world. Every terminal in camp is linked but only three reach the central system: one in
Tung's office, two in the registration work area; the propaganda terminals in the houses cannot. No IC.
Password "Springs Eternal" (Tung and two managers only; changed every 48 hours and valid in every camp
system for that long). Decking without it: Computer (9), base time 2 hours, Hacking Pool dice up to
Computer skill, retries double the TN, failure has no consequence. Contents: many references to Renraku
but no numbers -- pointers to directories in the Faith camp system. An innocent crash reboots every
terminal; for two minutes the house terminal is open, then a manager types the password: Computer (4) to
have thought of a keystroke logger. Also Tung's digital signature on transfer authorizations (Computer
(5) to forge from another document).

**3. Faith Relief Camp medical center central processor** (basement office). Same architecture and
password subsystem; 'barely robust enough to support netrunning'. Upper-floor research and diagnostic
terminals show the directories but cannot open the data; the dirt is only readable in the basement.
Contents: records of every experiment (Biotech (4) to read the jargon: BTL chips, illegal simsense,
non-elective cyberlimb modification, Renraku's 'subjective time dilation' simsense), incontrovertible
proof of Renraku's involvement, and proof that Project Hope belongs to the Universal Brotherhood. Tung
copies it all to a portable and purges memory and storage in four Combat Turns when alerted; Computer (3)
on the activity log shows the purge happened moments ago.

**4. Tung's portable computer** (recovered in the cocoon cavern). Encrypted under the same password
subsystem: "Springs Eternal" opens it; otherwise Computer (9), unlimited retries. Also holds Tung's
heavily encrypted essay 'Understanding the Hive Mind' (Handout 1) -- decoding takes plenty of time or a
paid specialist, at the GM's discretion.

**5. New Dawn Environics Kent system** (every lab and office terminal; central system; not on the
Matrix). One Computer Test per category, Hacking Pool dice divided among them and expended, retries
double the TN, +2 to the next category per failure, resolved in order: Treatment Process TN 6 (lab notes
that explain the larvae, the hosts and the toxic spirits); "Bug City" TN 4 (the facility is entirely
staffed by insect spirits); Divisional Autonomy TN 6 (an autonomous division; NDE belongs to Universal
Brotherhood International, known to a handful of top execs; the rest of NDE is clean -- accuse the wrong
people and the team's credibility dies); Faith Camp Experiments TN 4 (a directory listing of the Faith
files, no data).

**6. Juarez's telecom computer** ('postmortem mail'). Scans news reports and obituaries and watches for
his check-in; on his death or a missed date it mails the surveillance vids to Aztechnology and
DocWagon. Location unknown to the runners. Note: 2D6-hour Matrix legwork and one Shadowland request
(Etiquette (Matrix) (4) to find the echo station; 8 dice, base 36 hours) are available per pp.53-54.
"""

NOT_BUILT = """
- **The team's fixer** (unnamed, nervous, 'special medicine'; has no idea Juarez is a Fed -- 'he'd catch
  the next flight to the Caymans'), **the fixer's buyer** for the cyber parts, **the Aztech driver and three
  guards**, **the DocWagon courier**, **the FBI snipers** -- stat blocks on the Aztechnology, DocWagon and
  McHugh's rows.
- **Juarez's and Ranger's director** (never named), **the young woman at the enrollment office** who
  recruited Ranger, **the Enrollment Center secretary and rent-a-cops**, **the two Project Hope managers**
  who share the password (Mr. Johnson archetype, Willpower 4; not yet embraced), **the camp counselors**,
  **the man and woman in white lab coats** and **the troll orderly** of the prologue operating room,
  **Faith camp's three mercenary Street Docs and the clinic staff and patients**, **the Peace Enforcement
  Officers and Ant shamans**, **New Dawn's tanker drivers, guards, workers, watchers and true-forms**, the
  **dragonfly larvae** and the **toxic earth and water spirits** -- on the org and location rows.
- **The Splatters** (a gang tag on a Glow City wall, nothing more), **the Hive shaman** who summoned the
  Queen (dead long ago), **the Renraku and Aztechnology raid teams** (Day 10-11), **the UCAS soldiers**
  who blow the hive.
- **New Dawn's downtown office block** and its other nine Seattle sites (no addresses), **the seven other
  relief camps** (unnamed), **Solace House** (inside the Hope camp row), **the research facility south of
  Tacoma** (see the Tacoma Research Park update).
- Corporate name-drops: **Shiawase Envirotech** (on the Shiawase row), **Universal Brotherhood
  International** (on the Brotherhood row), **Seattle Medical Bureau** (inspected the clinic), **UCAS
  Geological Service** (Eva Leuwendyke's employer), **Absolute Security** and **Encyon Industries** (gate
  detectors), **Ranger Arms** (the SM-3), **MIT&M**, **Northrup** (the 'air car'), **Mayan Cutter** (a
  serial killer the Governor cites), **Arthur Garrett** (Datafax commentator on magic licensing).
- **'Good Morning Seattle'** and Seattle's 650 vid channels; **'The Hive That Ate Tokyo'** and **'Against
  the Hive Masters'** (simsense that ruined the bug story's credibility); **The Tibetan train wreck** and
  its mountain-sized fire elemental; **the Chicago events** the epilogue promises.
- Rules reprints (pp.47-52): insect-spirit bonding, weapon and chemical detection, Awareness Points --
  summarized on the org rows, not entities.
"""

PLAY_NOTES = """
- Three sessions in one book: run Digging Their Own Graves and Six Feet Under weeks apart in real time,
  between other adventures, photocopied so nobody sees the source; drop a 'bystander drone' into the
  scenery once and never again. The players must not suspect a set-up until McHugh's.
- The team cannot refuse Juarez; play the hopelessness and the anger. Some tables need only a hint of
  blackmail, some need the sledgehammer, ex-government characters need none -- an option is to pitch
  without the vids and only show them if the team balks.
- After the camp gates it is free-form: keep four running Awareness Point totals (Brotherhood, EPA,
  Renraku, Aztechnology) and let the tables decide who notices what. Cyberware alone earns a point from
  two factions; conspiring within earshot of guards two; getting caught in a secure area four.
- Every interesting enrollee is a spy. Mix Armstrong, Wiley, Hughes, Sanchez and Mitchell in with
  nobodies so nobody is obviously important; Armstrong is the trap, Wiley the ally, Sanchez the alternate
  employer, Hughes the one who sends chromed runners to the surgeons.
- Clues that the guards are bugs come in order: reaction speed and fireballs at the Butchers' raid, a
  dual-being's reaction to an astral scout, no cyber-scarring on the aura, then New Dawn's pool. Let a
  team that has met bugs before recognize the pattern -- and possibly quit at Kent.
- The mind-magic rule: two Resistance Tests (host, then the Queen's Willpower 10) against every mental
  spell on Tung, the PEOs or Armstrong; New Dawn's soldiers are exempt. Failing the Queen's test tells her.
- Timing the climax: the runners should reach the basement office just as Tung finishes the purge and
  the doors slam; make the chase impossible to win by shooting until the cavern wall; twenty soldiers
  from below, true-forms and eight PEOs behind. Goal is exposure -- 'taking on the 200-plus members of the
  hive would be suicide' -- but the team gets 5 Karma for trying to hurt it on the way out.
- Karma: team 20 for completing; +5 for damaging the hive before escaping; individual awards at double
  the usual rate, because the pay is low for the risk.
- Money: 1,000 each plus 5,000 to the group (Aztech van); 8,000 to the group (DocWagon); 5,000 each to
  show up and 30,000 each from Juarez; Wiley's 10,000 and Aztechnology's 30,000 are alternatives; 5,000
  each to join the fuel-air raid. Juarez keeps copies of everything.
- Loose ends: Juarez as an occasional, hated Johnson with a hold on the team; a Renraku that knows
  nothing yet and a UCAS that knows everything; Sanchez and Aztechnology; Andy Mitchell's byline; the
  Universal Brotherhood going underground with its remaining hives; Tung's essay, to worry about for a
  long time to come.
"""
