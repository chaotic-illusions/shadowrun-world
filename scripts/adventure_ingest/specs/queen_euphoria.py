# Queen Euphoria (FASA 7304, 1990) -- campaign order #6. Tacoma / Puyallup / Redmond, January 2051
# (the success handout is a January 15 newsnet). Secret debut of the insect spirits.
# Source text: docs/Adventures/text/Shadowrun 1e - Queen Euphoria {FASA7304].txt (67 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "Queen Euphoria"
ORDER = 6
SOURCE = "Shadowrun 1e - Queen Euphoria {FASA7304].pdf, pp. 4-67"
YEAR = "2051 (January)"

SYNOPSIS = """
Fixer **Ellery Whitecastle** wakes a hung-over runner with a job: meet a Mr. Johnson at Pier 36 on
the Tacoma docks at eleven. The Johnson (a **Ludivenko** exec who never says so, with samurai **Juan
Diablo** riding shotgun) pays 20,000 nuyen each to "detain" the reclusive megasimstar **Euphoria**
for three days so she misses her Friday-to-Sunday appearances promoting **Strice Foods'** runaway
stuffer **Amber Gel** -- treat her like royalty, no harm to the girl. The runners take her from her
21st-floor penthouse at **Pacific Towers** (past bodyguard **Osprey**, his old partner the mage
**Stone**, and four Knight Errant guards) and hole up in a roach-ridden flat at **Royal Meadows
Apartments**, where she nags, craves Amber Gel, and a magician who opens a jar sees a swarm of ants.
Strice's shows flop and riot; Strice hires the Lion shaman **Pride**, who ritual-tracks her by a hair
and kicks the door in on Sunday morning.

What nobody knows: Amber Gel is worker-ant secretion. **Thomas Dorin**, once the runner **Craft**,
came back from a South American fetish run possessed by the Ant totem and has been building a Hive in
the Amber Gel plant off Pioneer Highway, feeding it with Barrens street people, and selling the
"nectar of the gods" through desperate Strice exec **Vincent Burroughs**. When Ludivenko signs
Euphoria to push its clone Blue Bacosoy, Burroughs tells Craft to "take care of" her -- and Craft, who
has been dressing prostitutes as Euphoria in his basement for years, has Soldier ants climb Pacific
Towers, shred the Knight Errant team, and carry her off to be cocooned as his Queen. Her simsense rig
records the whole thing.

**MegaMedia** VP **Robert Carrone** -- who has just had Whitecastle interrogated and firebombed --
hires the runners to find her before Saturday: the unfiltered recording (a BTL-strength nightmare),
Garrety's Bar and Grill and the chitin-scarred missing waiter **Van Willis**, Burroughs' office (a
Soldier spirit comes for him mid-confession), Craft's shop **Magic Crafts** and its blood-soaked
shrine, the Strice computer, and finally a MegaMedia-sanctioned, contract-signed, simsense-recorded
assault on the Hive with a company of Knight Errant outside. Euphoria cannot be saved. Six weeks later
MegaMedia releases *Against the Hive Masters*, starring the runners.
"""

TIMELINE = """
- **Wednesday night** -- Whitecastle's call; Pier 36 at 11 p.m. **Thursday night** -- the kidnapping
  (penthouse, the door, or the road). **Friday 10 a.m.** -- Vernon Gruder and the first credsticks;
  Friday afternoon the Renraku Arcology show flops. **Saturday** -- the coliseum show riots. **Sunday
  9 a.m.** -- Pride's assault; the city cancels the Pyramid-park show; Euphoria released; Diablo pays.
- **Monday** -- Euphoria and Carrone try to squeeze Burroughs; contract clause says no. **Tuesday** --
  Burroughs hears of the Ludivenko/MegaMedia Blue Bacosoy deal and calls Craft; that evening Soldiers
  climb Pacific Towers. Wednesday-Thursday: Killian's guards die in the plant; Craft tells Burroughs
  production has stopped.
- **Second wake-up call** -- Whitecastle (fifteen minutes from death); 11 a.m. at Pacific Towers with
  Carrone; deadline **6 a.m. Saturday** (Ludivenko recording dates). Eight-hourly reports.
- **Five weeks** -- the Queen would emerge. **Six weeks after** -- *Against the Hive Masters*.
"""

ORGS = [
    {
        "name": "Strice Foods",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Birmingham, Alabama, CAS; Seattle offices on the 10th-11th floors of Soykyo Office Plaza",
        "summary": "Minor international food corp (Faucet Flavors) whose Amber Gel stuffer is secretly ant-spirit secretion",
        "description": (
            "A minor player in the international food business, best known for the Faucet Flavors line "
            "of nutrisoy flavoring agents (its largest division, head Zachary Fynche). Also REAL Foods "
            "(hydroponic organic vegetables, head Jack Tauber) and Modern Masterpieces (mass-market "
            "stuffers: Best O'Da Bunch, Crackle Cakes, Zap Softies, and the runaway sensation Amber "
            "Gel; head Vincent Burroughs). President/CEO Deloris Stanton. Amber Gel is test-marketed "
            "only in Seattle, sells faster than it can be made, and its ingredients, process, and even "
            "the location of its plant are secrets from Strice's own board. Knight Errant handles the "
            "important security; a small internal force under Security Director Henry Killian handles "
            "the rest."
        ),
        "leadership": [
            {"name": "Deloris Stanton", "title": "President/CEO", "notes": None},
            {"name": "Zachary Fynche", "title": "Division Head, Faucet Flavors", "notes": None},
            {"name": "Jack Tauber", "title": "Division Head, REAL Foods", "notes": None},
            {"name": "Vincent Burroughs", "title": "Division Head, Modern Masterpieces (Amber Gel)", "notes": "Craft's front. Marked for death by the Hive."},
            {"name": "Henry Killian", "title": "Security Director (deceased)", "notes": "Killed with his men by Soldier ants inside the Amber Gel plant."},
        ],
        "notes": (
            "Amber Gel = worker-ant secretion plus thickeners, blue coloring and low-grade nutrisoy "
            "(the only things the purchase orders show delivered to the plant); not addictive, just "
            "craved. Paid MegaMedia 1,280,000 nuyen for Euphoria's three appearances, hired Knight "
            "Errant to guard her, then hired Pride to get her back. Computer system on SAN 2206 "
            "(312-1752), changes weekly; Trace results print at Burroughs' desk (map in the prep doc). "
            "Success ending: Strice withdraws Amber Gel from the market and denies MegaMedia's "
            "'military operation' against its plant. Its Board would demote Burroughs if it knew "
            "production had stopped -- but he is the only one who knows the secrets."
        ),
        "allies": ["Knight Errant Security Services"],
        "enemies": ["Ludivenko", "MegaMedia Entertainment"],
    },
    {
        "name": "Ludivenko",
        "org_type": "corporation",
        "tier": 4,
        "headquarters": "Seattle operations (parent elsewhere; not given)",
        "summary": "Stuffer giant (Ludivenko Lovelies) that hires the runners to kidnap Euphoria and launches Blue Bacosoy",
        "description": (
            "A major stuffer manufacturer with a world share of the market -- the Ludivenko Lovelies "
            "Soya-Sloppies dispensers in every Stuffer Shack are theirs. Amber Gel hit them the only place "
            "corporations get hurt, at the bank, so Ludivenko's Seattle operations hired a shadowrun team "
            "through fixer Ellery Whitecastle to make Euphoria miss her Strice promotions, then cut a "
            "deal with MegaMedia for her to endorse their Amber Gel clone, Blue Bacosoy, instead."
        ),
        "notes": (
            "The Mr. Johnson (Negotiation 6; a night-blue Toyota Elite with a Company Man chauffeur) never "
            "names the corp. Payment: 20,000 each, half at the Redmond flat via wage-slave courier Vernon "
            "Gruder, half from Juan Diablo (wristphone 5-5-CHROME) after Euphoria is released. Rented "
            "flat 812 at Royal Meadows under 'John Smith' and stocked it with dehydrated food and "
            "women's clothing. MegaMedia found out and, instead of retaliating, took the Blue Bacosoy "
            "contract -- and Ludivenko handed over Whitecastle's and the runners' names. Any Seattle "
            "runner can guess Ludivenko is behind the first kidnapping (Legwork p.60)."
        ),
        "enemies": ["Strice Foods"],
    },
    {
        "name": "MegaMedia Entertainment",
        "org_type": "corporation",
        "tier": 4,
        "headquarters": "Seattle, UCAS (the MegaMedia building near the Aztechnology Pyramid)",
        "summary": "One of the 'Big Six' simsense/trideo giants; Euphoria's studio; reeling from Honey Brighton's defection",
        "description": (
            "One of the Big Six international simsense/trideo production and distribution corporations, "
            "headquartered in Seattle. President/CEO William Welsh; divisions MegaMedia Productions "
            "(simsense and trideo production, head Andrea Stueban) and MegaMedia International "
            "(distribution, head Nick Nathan). Owes its success to an uncanny knack for finding and "
            "grooming unknowns: Cindy Cyclone, Ted Morgan, David and Helen Variable, Honey Brighton, "
            "Euphoria. The recent defection of Brighton and her famed producer Witt Lipton to Chicago's "
            "Brilliant Genesis has analysts speculating about internal problems; another blow like it "
            "could be fatal. Recently dropped Lone Star for Knight Errant on all facility and personal "
            "security."
        ),
        "leadership": [
            {"name": "William Welsh", "title": "President/CEO", "notes": None},
            {"name": "Andrea Stueban", "title": "Division Head, MegaMedia Productions", "notes": None},
            {"name": "Nick Nathan", "title": "Division Head, MegaMedia International", "notes": None},
            {"name": "Robert Carrone", "title": "Vice President (Euphoria's career)", "notes": "Formerly her manager."},
            {"name": "Angela Lane", "title": "Spokesperson", "notes": None},
        ],
        "notes": (
            "The Brighton defection will cost billions; every half-nuyen corp in the biz now sees "
            "MegaMedia as fair game. Aztechnology is suing MegaMedia over the helicopter that crashed "
            "near the Pyramid the night Brighton got out, with Lone Star named co-defendant (the Ares "
            "Dragon in the DNA/DOA news handout). MegaMedia had Whitecastle interrogated and firebombed, "
            "hires the runners under threat, runs the Hive assault as an 'official corporate action' "
            "under the Corporate Interaction Act of 2038 (contract overseen by August Dorn, Independent "
            "Contract Overseer; bonded Russel Overland transport; Knight Errant company on standby), "
            "hides simsense recorders in the loaned armor, and releases 'Against the Hive Masters' six "
            "weeks later. Euphoria retires. Loaned gear must be returned."
        ),
        "allies": ["Knight Errant Security Services"],
        "enemies": ["Brilliant Genesis"],
    },
    {
        "name": "Brilliant Genesis",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Chicago",
        "summary": "Chicago simsense studio that poached Honey Brighton and producer Witt Lipton from MegaMedia",
        "description": "MegaMedia's Chicago-based simsense rival, which recently extracted megastar Honey Brighton and her famed producer Witt Lipton -- the defection that has MegaMedia security-conscious and its finances bleeding.",
        "notes": "Off-stage in Queen Euphoria; the reason MegaMedia cannot afford to lose Euphoria and the reason Osprey's job got harder.",
        "enemies": ["MegaMedia Entertainment"],
    },
    {
        "name": "The Ant Hive (Puyallup)",
        "org_type": "insect spirit hive",
        "tier": 3,
        "headquarters": "Lower level of the Amber Gel production facility, south of Puyallup off Pioneer Highway",
        "summary": "Craft's Ant Spirit hive: Workers, Soldiers, nearly a hundred cocooned Barrens victims, and a cocooned Queen -- Euphoria",
        "description": (
            "Something loose in the world that should not be. Under the influence of a still-unsummoned "
            "Queen Ant Spirit, the shaman Craft has been building a Hive in the belly of the Amber Gel "
            "plant: Worker Ant Spirits (cowardly, screeching, sacrificing themselves for the cocoons) and "
            "Soldier Ant Spirits (fearless, cunning fighting machines with thousands of years of "
            "tactics), in True Form (man-sized pristine ants that manifest from astral space, armor equal "
            "to double Force against ranged weapons) and Flesh Form (Barrens street people possessed and "
            "warped -- chitin 'scars', hands that aren't hands, clicking laughter). Nearly a hundred "
            "people who vanished from the Barrens in recent weeks hang in amber cocoons, beyond salvation. "
            "The street calls it a fanatic cult that kidnaps street people."
        ),
        "leadership": [
            {"name": "Thomas Dorin", "title": "Hive shaman (\"Craft\")", "notes": "The Ants' shaman; they seek him out to start over if the Hive falls."},
        ],
        "notes": (
            "No hive-mind yet (the Queen is not fully summoned), so sentries can be killed quietly. "
            "Garrison (pp.43-46): two Flesh Form Soldiers (F3) on the roof; two Flesh Form Workers (F1) "
            "upstairs to raise the alarm; lower level rooms 3/14/15 hold 15 Flesh Form Workers and five "
            "Flesh Form Soldiers (one F5); the Hive Room holds scores of cocoons, the remaining Workers "
            "and Soldiers, Craft, and two True Form Soldiers (F5) held in reserve; astral scouts meet "
            "pairs of True Form Soldiers (F5). GM rule of thumb: at least five Flesh Form Soldiers per "
            "True Form; Force 3 more common than 5; only a handful of True Form Workers. Stat blocks "
            "pp.38, 47-52. Melee against a manifest spirit uses Willpower, not weapon skill; "
            "vulnerability: insecticides. The cocooned Queen (Force 5, Dual Being, cannot defend "
            "herself) is vulnerable to astral combat; opening her cocoon without banishing her kills "
            "Euphoria's body; banishing her first leaves a mindless, half-transformed body. If the Queen "
            "is banished the survivors go looking for Craft. Karma: destroy the Hive 5, destroy Queen "
            "Euphoria 3. 'The ferocity of this encounter will set the tone for many adventures to come.'"
        ),
        "enemies": ["MegaMedia Entertainment", "Knight Errant Security Services"],
    },
    {
        "name": "Universal Brotherhood",
        "org_type": "charity / policlub",
        "tier": 4,
        "headquarters": "Seattle chapter (national organization)",
        "summary": "Fast-growing charitable brotherhood announcing three more Barrens missions (January 2051 news)",
        "description": (
            "A charitable, quasi-religious brotherhood expanding rapidly into the Seattle sprawl. In "
            "January 2051 it announced plans for three more missions in the Barrens, offering food, "
            "shelter and belonging to the SINless."
        ),
        "notes": (
            "Recorded here from the Queen Euphoria success handout (Seattle News-Intelligencer, January "
            "15). Nothing in this adventure connects it to the Ant Hive; treat it as world texture until "
            "Missing Blood (campaign #25) reveals more."
        ),
    },
]

LOCATIONS = [
    {
        "name": "Pier 36 (Tacoma Docks)",
        "location_type": "transportation hub",
        "district": "Tacoma docks (disreputable end)",
        "security_level": "No Security / Barrens",
        "summary": "Lonely hundred-meter wooden pier where Ludivenko's Johnson holds the meet; Lone Star doesn't patrol here",
        "description": (
            "A heavy wooden pier stretching a hundred meters into the bay among the disreputable and "
            "dangerous stretches of the Tacoma docks, deserted by nine at night. One incandescent street "
            "lamp on a frazzled cable sways in the wind, throwing shadows up and down the planking over "
            "the crashing waves. Across the road, derelict warehouses -- empty near the pier, squatters, "
            "gang hideouts and illegal goods further along. Few ships use these docks; Lone Star does "
            "not bother to patrol."
        ),
        "notes": "A samurai on a Harley Scorpion (Ingram MG, armor plate) sweeps the area first and phones the night-blue Toyota Elite in. A good recurring 'neutral' meet for corporate Johnsons who want no witnesses.",
    },
    {
        "name": "Royal Meadows Apartments",
        "location_type": "apartment complex",
        "district": "Redmond Barrens (edge)",
        "security_level": "No Security / Barrens",
        "summary": "18-storey corporate tenement, no meadows, nothing royal; the rented hideout flat 812; landlord Crucius Bunter",
        "description": (
            "Eighteen storeys of steel frame and cinderblock polished up with plastic windows, rusted "
            "iron sculptures and three decades of pollution, a few blocks into the Barrens and easily "
            "mistaken for one of its slum tenements. Wage slaves and street people stream through the "
            "main doors; a dwarf reads the fax behind the manager's window; security is one Ork asleep "
            "by the elevators; the stairwells belong to the vermin. Flat 812: a coffin-sized bathroom "
            "with filters never changed, two doubles pushed together, low-grade plastic furniture, a "
            "closet kitchenette, stale air, and resident insects that eye you speculatively."
        ),
        "notes": (
            "Rented for the month as 'John Smith' by Ludivenko, stocked with dehydrated food (surprisingly "
            "tasty if prepared right) and plastic-wrapped women's clothing for Euphoria. No effective "
            "security checks. One chair breaks, the freezer is dead, the hot tap does not work; a small "
            "bribe gets Crucius to fix things. Pride's crew blows the door in Sunday at 9 a.m.; Bunter "
            "will have questions about the room damage."
        ),
    },
    {
        "name": "Pacific Towers",
        "location_type": "penthouse",
        "district": "Ward Street, over Rosemont Beach",
        "security_level": "Corporate Standard",
        "summary": "Black tapering 25-storey condo spike for corporate execs; Euphoria's 21st-floor penthouse; scene of both kidnappings",
        "description": (
            "A great ebony spike over Rosemont Beach: black polymer sides, plastic-enclosed balconies, 25 "
            "storeys each smaller than the last, two parking sublevels. The lobby is gray marble and "
            "colorful rugs, oil paintings, a holographic cathedral vault, a circular marble-and-gold "
            "security desk, three thumbprint-locked elevators, a residents' bar, meeting and lecture "
            "rooms, an expensive clothing-and-electronics store with a courier who delivers to your door, "
            "a garden courtyard, sauna, and a pool open all hours with a tanning lamp at every lounger. "
            "Three or four condos per floor; the top five floors are one penthouse each. Corporate "
            "executives own or lease most of it and the staff respect privacy. No magical security."
        ),
        "notes": (
            "Staff: lobby guard round the clock (barely trained; Armor Vest, Ceska Black Scorpion, an "
            "Enfield AS7 behind the desk, PANICBUTTON -> four Lone Star officers in five minutes unless "
            "cancelled by calling 2206 (312-1876) with code J87), a bellboy/courier, and by day a "
            "maintenance man, bartender, lifeguard and two clerks. Visitors are video-verified by the "
            "resident; elevators are thumbprint-locked and floor-programmed (Electronics 5, five minutes, "
            "to bypass); cameras on the ground floor and in every lift. Building computer is NOT on the "
            "Matrix (lobby terminal only): I/OP-1 Green-3, SM-1 cameras Orange-3, SM-2 lighting/elevators "
            "Orange-3, DS-1 (visitor records, the cancel code) Green-3, CPU Orange-4. Euphoria's "
            "penthouse (map p.18): entrance hall with a Knight Errant guard, credstick-locked double doors "
            "(Barrier 5, Electronics 4), foyer with Monet prints, living room with real and holographic "
            "sculpture and an entertainment wall, her private recording studio (professional simsense "
            "recorder, sensory-calibration desk of sandpaper and lemon juice), a jungle greenhouse balcony "
            "(impact plastic, Barrier 6, rain-and-animal soundtrack, holographic views), workout room "
            "with hot tub, automated kitchen, dining room, Osprey's English-motif bedroom with a "
            "Napoleonic cavalry sword, Stone's spare room, the master bedroom with a full-figure "
            "holographic mirror and a hidden wardrobe. After the Hive attack: a chair and cold soykaf in "
            "the hall, three guards shredded across the living room, holes in the ceiling, a lump of "
            "brown hive-slime by the couch, the balcony shell torn open, the recording still running. "
            "When she travels: Osprey and Stone in a Mitsubishi Nightsky driven by Knight Errant, two "
            "more in a Ford Americar ahead, a Knight Errant Wasp three minutes away by radio."
        ),
    },
    {
        "name": "Soykyo Office Plaza",
        "location_type": "corporate facility",
        "district": "Downtown",
        "security_level": "Corporate Standard",
        "controlling_org": "Strice Foods",
        "summary": "Downtown office tower; Strice Foods' Seattle offices on floors 10-11; Burroughs' corner office",
        "description": (
            "A crowded downtown office building whose tenth and eleventh floors hold all of Strice Foods' "
            "Seattle central offices. Vincent Burroughs' corner office on the tenth floor has two views "
            "of the city, plush furniture, a well-stocked bar, and a huge desk with the terminal and "
            "printer that receive the Strice system's Trace printouts."
        ),
        "notes": (
            "Guns blazing brings a large Lone Star force at once. Eleventh-floor receptionist: Etiquette "
            "(Corporate) TN 5; Burroughs' secretary: TN 6 for an appointment in eight hours divided by "
            "successes (four = immediately); +2 per extra character talking, -1 in business suits, +4 "
            "with assault rifles. Burroughs' desk terminal is I/OP-1 of the Strice system. His secretary "
            "knows the plant's Puyallup address and Craft's paycheck address near St James Lake, and can "
            "clear the runners if the Soldier kills him."
        ),
    },
    {
        "name": "Garrety's Bar and Grill",
        "location_type": "bar",
        "district": "Downtown",
        "security_level": "Patrolled / Commercial",
        "summary": "Safe 'street-edge' pub where corp types slum; staff T-shirts; missing waiter Van Willis",
        "description": (
            "Near enough to the real action to have a glimmer of street edge, far enough to be safe -- the "
            "kind of place corp types go slumming for the aura of a street bar. A bar, a dance floor, "
            "tables and booths, credstick sim machines and arcade games in a corner, grilled food and a "
            "well-stocked bar, waiters and waitresses in Garrety's Bar and Grill T-shirts. Clientele: "
            "lower-level sararimen and the middle class. A Troll bouncer at night."
        ),
        "notes": (
            "Owner and chief bartender Bill Garrety saw waiter Van Willis dragged down a manhole behind "
            "the bar a month ago and will not say a word -- he has heard the rumors about the cult "
            "kidnapping street people. Waitress Wendy Phillips will talk when Garrety is out of earshot "
            "(or catch the runners leaving): she saw Willis two weeks ago outside a shop called 'Magic "
            "Crafts', face covered in what looked like scars. A bar brawl here gets the runners beaten "
            "senseless, and they deserve it."
        ),
    },
    {
        "name": "Magic Crafts",
        "location_type": "shop",
        "district": "Redmond Barrens, near St James Lake",
        "security_level": "No Security / Barrens",
        "controlling_org": "The Ant Hive (Puyallup)",
        "summary": "Craft's shuttered talismonger shop and basement shrine to Euphoria; a Flesh Form Worker guards the door",
        "description": (
            "Thomas Dorin's old talismonger shop on a desolate Barrens street near St James Lake, closed "
            "for months but recently 'renovated', with scary-looking dudes hanging around. Front and "
            "alley doors (Barrier 5), the alley lock recently used. The shop floor holds about 2,500 nuyen "
            "of fetish material and dust. Downstairs is where Craft lived and still escapes to be human "
            "for a while: trideo, LiveSound audio, a simsense player and a stack of chips that are mostly "
            "Euphoria sims, a crude map of the Amber Gel plant with its location, microwave fixings and "
            "heaps of empty Amber Gel jars, a bathroom that erupts roaches, and a bedroom that reeks of "
            "dried blood."
        ),
        "notes": (
            "Van Willis (Flesh Form Worker, Force 1, three weeks possessed, chitin under bulky clothes, "
            "still in his torn Garrety's T-shirt) stands in the doorway as a scare tactic; he cannot "
            "fight. Astrally his aura is a huge ant. The bedroom walls are papered with blood-spattered "
            "photos and illustrations of Euphoria; the closet holds copies of her sim costumes and wigs "
            "in her hairstyle. Craft has lured women here for years, mostly prostitutes, dressed them as "
            "the star and acted out his fantasies -- at least one died here, the last about a week before "
            "he took Euphoria. Attack Ant Spirits may show up; this is an instructional fight, not a "
            "final one. Strice's paychecks to Craft were sent to this address."
        ),
    },
    {
        "name": "Amber Gel Production Facility",
        "location_type": "corporate facility",
        "district": "South of Puyallup, off Pioneer Highway",
        "security_level": "Corporate Standard",
        "controlling_org": "The Ant Hive (Puyallup)",
        "summary": "Strice's secret plant: dusty conventional food machinery upstairs, the Ant Hive in the dark lower level",
        "description": (
            "Strice Foods' hidden Amber Gel plant on a fenced compound off Pioneer Highway south of "
            "Puyallup. Upstairs: a loading dock where Strice trucks find the drums already waiting each "
            "morning and only ever see Craft, dusty and poorly maintained conventional food-production "
            "equipment, a small block of abandoned offices, a working freight elevator with a damaged "
            "panel, an unlit stairway to roof and basement, green-tinted high windows, power on. "
            "Downstairs: no light, stale air sweet and pungent, no ordinary insects or rodents at all, "
            "weak walls (Barrier 3), crates of raw soy, worker rooms, the mixing vats and drums, and the "
            "Hive Room -- scores of dark amber cocoons with human shapes writhing inside."
        ),
        "notes": (
            "Map pp.43-45. Sentries on the roof; Workers upstairs flee to raise the alarm; Soldiers use "
            "the thin walls, the dark and their knowledge of the ground. Play up decay, skittering, "
            "water dripping on metal, the inhuman wails of the Flesh Form Workers. Strice's autopiloted "
            "trucks report here via the SM node; a Trace from the plant's own small system prints at "
            "Burroughs' desk. MegaMedia's command truck waits within spitting distance with a company of "
            "Knight Errant and a KE executive observer; afterwards MegaMedia or Strice analyze the "
            "cocoons for economic value, then destroy them. Killian's Strice guards died here."
        ),
    },
]

NPCS = [
    {
        "name": "Thomas Dorin",
        "role": "'Craft' -- ex-runner and talismonger, Coyote shaman turned Ant shaman; Euphoria-obsessed founder of the Hive",
        "archetype": "Street Shaman",
        "title": "\"Craft\"; Ant shaman of the Puyallup Hive; proprietor of Magic Crafts",
        "race": "Human",
        "gender": "Male",
        "organization": "The Ant Hive (Puyallup)",
        "connection": 3,
        "description": (
            "Once ripped, muscular and flashily dressed; now a filthy, unkempt man with long tangled blond "
            "hair, clothes stained brown with regurgitated hive food, and a sickly sweet smell on his "
            "breath. Handsome, were he younger and cleaner. Wide swings: trickster and traitor as a "
            "Coyote shaman, respectable and friendly as a merchant, crazed with power under the Ant "
            "totem. 'Don't be afraid, everything will be all right. Now isn't that a silly thing to say?'"
        ),
        "background": (
            "Son of wage slaves, raised on Seattle's streets; learned shamanic magic from a crazed old "
            "Coyote squatter in exchange for food. Ran the shadows as Craft (named for his cunning "
            "solutions) with a razorguy and another wiz until he skimmed and double-crossed his partners "
            "and employers once too often and was blacklisted; opened Magic Crafts on the proceeds. Bored, "
            "he took fixer Solomon Daniels' run to buy fetishes cheap from two South American jungle "
            "villages, was shot down by the supply corp's fighter, walked eight delirious days under a "
            "totem howling death, collapsed on a vine-covered four-meter stone pyramid, and was remade on "
            "the astral plane by warrior ants who devoured his Coyote and offered him power -- and her. "
            "'She would be his Queen.'"
        ),
        "notes": (
            "Sold Amber Gel through Burroughs for nuyen and secrecy; halted production when the Queen "
            "ordered the Hive to build her cocoon; dispatched a True Form Soldier (F3) to kill Burroughs; "
            "kidnapped Euphoria personally with a Worker and several Soldiers. In the Hive Room he holds "
            "two True Form Soldiers (F5) in reserve, maintains astral perception, aids the Soldiers with "
            "magic, engages only if the Queen is threatened, and flees only when defeat is certain -- to "
            "start over. Stats: B4 Q3 S3 C5 I5 W6, Ess 6, Magic 6; Sorcery 6, Conjuring 5, Magic Theory "
            "6, Negotiation 4, Stealth (Urban) 4; Astral pool 15. Spells: Mana Bolt 5, Sleep 5 (focus 2), "
            "Mask 6, Stimulation 4, Armor 6, Levitate Person 4. Ares Predator, real leather. Totem: Ant."
        ),
    },
    {
        "name": "Euphoria",
        "role": "Amanda Lockhart -- reclusive megasimstar, spoiled child, Amber Gel addict; kidnapped twice, cocooned as the Ant Queen",
        "archetype": "Simsense Star",
        "title": "Simsense megastar (MegaMedia); born Amanda Lockhart",
        "race": "Human",
        "gender": "Female",
        "age": 21,
        "organization": "MegaMedia Entertainment",
        "connection": 2,
        "description": (
            "Dazzling without surgery or make-up: light brown hair (it has been every color), brown eyes "
            "still the original organic models, a silk wardrobe and a Long Coat in public. Twenty-one and "
            "still a little girl -- arrogant, spoiled, a nag by day two ('I'm supposed to sleep in that "
            "bed? It's full of bugs!'), frightened and docile when threatened, contemptuous of the fans "
            "who mill about 'like cattle idolizing me because they can't face their own pathetic lives'. "
            "Something of a recluse; has never made a public appearance."
        ),
        "background": (
            "Daughter of two trideo actors who pushed her from child trideo into simsense extras. Her "
            "break came when she switched to agent Robert Carrone: a series of low-budget erotic sims "
            "that estranged her parents and made her a star, then six full-budget sims, four with "
            "co-star Hans Vandenburg (who is fit to be tied over her). Debuted in 2048 with 'Shotgun "
            "Blues'. Next project: 'Jungle Huntress', to shoot on location in the Aztlan jungles. "
            "Craves Amber Gel; violence in scripts bothers her."
        ),
        "notes": (
            "Stats: B2 Q4 S2 C6 I4 W2, Ess 5; Simsense Acting 6, Electronics (simsense) 3; datajack, "
            "Sense Link with internal transmitter -- which is why her abduction was recorded, unfiltered, "
            "at BTL intensity. Cannot be located magically once cocooned (the Queen shrouds her aura); "
            "Mind Probe yields a headache of alien thoughts. There is no way to save her: open the cocoon "
            "and she dies; banish the Queen first and a mindless, half-transformed body survives. Ending: "
            "MegaMedia announces her 'retirement' after 'Against the Hive Masters' (formerly Jungle "
            "Princess), over budget and unfinished; the Euphoriacs fan club (Lou Buckminster) wails."
        ),
    },
    {
        "name": "Robert Carrone",
        "role": "Euphoria's manager turned MegaMedia VP; honest dealer, ruthless corp man; hires and threatens the runners",
        "archetype": "Corporate Executive",
        "title": "Vice President, MegaMedia Entertainment (in charge of Euphoria's career)",
        "race": "Human",
        "gender": "Male",
        "organization": "MegaMedia Entertainment",
        "connection": 4,
        "description": (
            "Tall and lanky in a gray business suit, red hair in a conservative corporate style, opaque "
            "sunglasses on a thin hawk-like nose, brooding over a drink. Calm and collected; uses every "
            "ruthless trick in the corporate world to keep what is his, yet has a street reputation for "
            "a fair shake. 'Anyone want a drink? You'll need it.'"
        ),
        "background": (
            "A born and bred corp man: a video director's go-fer at nine, in the right place to turn "
            "Amanda Lockhart into Euphoria, set for life when MegaMedia acquired her contract. Refuses to "
            "give up his other acts though she takes all his time; his heart will stress out without a "
            "Chiba organ. Worries about Osprey as a financial leech; delayed Jungle Huntress over jungle "
            "security."
        ),
        "notes": (
            "Had Whitecastle interrogated and killed; offers 20,000 each (half if after 6 a.m. Saturday), "
            "then 75,000 each for the Hive assault as an official corporate action with a contract that "
            "signs away every reproduction right (handout p.65). Demands reports every eight hours, "
            "total secrecy, and the loaned gear back; waives the gag only for Knight Errant. Records the "
            "rescue through hidden simsense gear in the armor (Electronics B/R TN 12 to find). Stats: B3 "
            "Q4 S2 C3 I4 W3, Ess 5.4; Etiquette (Corporate) 6, (Media) 5, Negotiation 5, Firearms 3; "
            "datajack, display link, 30 Mp headware; armor clothing, Ceska vz/120, pocket secretary."
        ),
        "contact_skills": ["MegaMedia simsense industry access and jobs", "Talent management"],
    },
    {
        "name": "Vincent Burroughs",
        "role": "Obese, desperate Strice exec fronting Amber Gel for Craft; marked for death by a Soldier ant",
        "archetype": "Corporate Executive",
        "title": "Division Head, Modern Masterpieces, Strice Foods (Amber Gel)",
        "race": "Human",
        "gender": "Male",
        "age": 51,
        "organization": "Strice Foods",
        "connection": 2,
        "description": (
            "Obese, 51, pinstripe suits and lots of jewelry, neatly combed conservative gray hair, a face "
            "that could use the cosmetic surgery it has never had. Casual and pleasant about combat-bike "
            "teams ('How about those Timberwolves?') until anyone mentions Euphoria or Amber Gel; on the "
            "verge of a nervous breakdown."
        ),
        "background": (
            "Unknown in the business world until Amber Gel. With Modern Masterpieces' sales slow and his "
            "job in doubt, a man named Craft walked in with a stuffer that would make Strice king of the "
            "industry and showed him how it was made -- 'like honey'. Burroughs went ahead anyway, "
            "supplied the raw materials, and watched his value rise; nobody upstairs asked where it came "
            "from. Told Craft to 'take care of' Euphoria when Ludivenko signed her for Blue Bacosoy."
        ),
        "notes": (
            "Etiquette (Corporate) / Interrogation / Negotiation TN 6 (-2 with the abduction recording) "
            "to break him: 1 success gets 'Craft', 2+ the whole story. Mid-confession a True Form Soldier "
            "(F3) materializes to kill him (Perception TN 9); it ignores the runners and flees once he "
            "is dead. Alive, he gives the plant's address and 10,000 nuyen to learn why production "
            "stopped. Sent Security Director Henry Killian and his guards into the forbidden sections; "
            "they were massacred. Stats: B3 Q2 S2 C4 I4 W2, Ess 4.8; Negotiation 4, Etiquette "
            "(Corporate) 4, Interrogation 3; datajack, 100 Mp. Lives in a lightly secured condo."
        ),
    },
    {
        "name": "Michael Adams",
        "role": "'Osprey' -- Euphoria's English ex-runner bodyguard, a cultured mercenary loyal to MegaMedia's credstick",
        "archetype": "Bodyguard",
        "title": "\"Osprey\", personal bodyguard to Euphoria (retained by MegaMedia)",
        "race": "Human",
        "gender": "Male",
        "nationality": "English",
        "organization": "MegaMedia Entertainment",
        "connection": 3,
        "description": (
            "Taller than average, slender but muscular, dirty blond hair and pale blue eyes, no visible "
            "modifications so as not to mar the glamour of the stars he guards. A veneer of culture and "
            "gentility -- coat of arms of his 'supposed ancestors', posters of London and Stonehenge, a "
            "Napoleonic cavalry sword -- over mercenary ruthlessness. Charges a high price. Still slums "
            "for fun when off duty."
        ),
        "background": (
            "Born in England, moved to Seattle when his father joined Renraku, grew up as much on the "
            "streets as in the corporate shelter. When a rival corp extracted both his parents, he spent "
            "Renraku's support money on cyber and went samurai-for-hire, running with Stone and a team "
            "that is otherwise all dead. Gave it up for secure work; good looks brought bodyguard jobs "
            "and, for a year and a half, Euphoria -- defusing bombs and holding off gangs of fans who "
            "want to become her. No special friendship with her; babysits her for MegaMedia, which she "
            "resents."
        ),
        "notes": (
            "Orders the Knight Errant team to repel invaders while he secures Euphoria, then joins in; "
            "interrogates captured runners. Not present at the second kidnapping (MegaMedia was still "
            "looking for his replacement). Stats: B5 Q5 S4 C5 I4 W5, Ess 0.3, Reaction 5(9); Firearms 7, "
            "Armed Combat 5, Unarmed 5, Stealth 5, Etiquette (Media/Street) 4, Negotiation 4; two "
            "chipjacks, datasoft link, thermographic/flare retinal mods, retractable razors, Skillwire 6 "
            "(Car, Demolitions, French, Interrogation, Japanese, Monofilament Whip softs), smartlink, "
            "Wired Reflexes 2; armor jacket, Colt Manhunter, FN HAR (explosive), monofilament whip, BMW "
            "330LS."
        ),
        "contact_skills": ["Celebrity bodyguarding and star security", "Fan-cult and kidnap threats to stars"],
    },
    {
        "name": "Alexander Cross",
        "role": "'Stone' -- retired runner mage and library hermetic consultant guarding Euphoria for his old partner Osprey",
        "archetype": "Street Mage",
        "title": "\"Stone\", hermetic mage (retired runner; lore-shop owner)",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "Tall and slightly overweight after a few calm years, curly brown hair and heavy sideburns; "
            "quiet and stoic -- hence Stone -- and a bit more noble-hearted than his associate Osprey. "
            "Rich in fetishes and ritual material back when he ran; always had an Elemental or two at "
            "his call."
        ),
        "background": (
            "Seattle street kid (sarariman father, corporate-secretary mother) who ran with gangs, then "
            "surprised his parents by majoring in magic at UCLA and selling his skills as a runner "
            "alongside Osprey. Retired shortly after Osprey did, worked as a hermetic consultant in a "
            "public library, and now owns a lore shop someone else runs while he takes 'a few days off "
            "with old associates'."
        ),
        "notes": (
            "Will stand by Euphoria. Stats: B4 Q2 S3 C4 I5 W6, Ess 6, Magic 6; Sorcery 7, Magical Theory "
            "8, Conjuring 5, Armed Combat (Clubs) 4; Astral pool 18. Spells: Mana Bolt 5, Powerball 5, "
            "Sleep 6, Detect Enemies 3, Increase Strength +2, Treat Severe Wounds 5, Armor 8, Control "
            "Thoughts 5, Petrify 6 (manipulations need his six expendable fetishes). Bound: Fire "
            "Elemental F5 on Euphoria for Spell Defense, Fire Elemental F4 for combat spells, Earth "
            "Elemental F5 to sustain Armor. Armor clothing, silenced Browning Max-Power, staff."
        ),
        "contact_skills": ["Hermetic magic and lore (lore shop)", "Elemental conjuring"],
    },
    {
        "name": "Shaka Jubowei",
        "role": "'Pride' -- two-meter African Lion shaman and globe-trotting bounty hunter hired by Strice to find Euphoria",
        "archetype": "Bounty Hunter",
        "title": "\"Pride\", shaman and bounty hunter (freelance, global)",
        "race": "Human",
        "gender": "Male",
        "nationality": "African",
        "connection": 3,
        "description": (
            "Almost two meters and muscular, very black skin, long stringy hair growing down the back of "
            "his neck, cat-like vertical pupils, real leather clothing of African design. Behaves like an "
            "aristocrat, always cunning, savage when angered; gives no quarter. Roars like a beast and "
            "charges. Lion: vain, lives well, demands respect and loyalty, works from surprise and ambush "
            "and lets others do the work until needed."
        ),
        "background": (
            "Named for Shaka Zulu; learned Sixth World magic from African shamans keeping ancient "
            "traditions, then left to make a name in the modern world and discovered that ability plus "
            "savagery sells. A globally active runner specializing in bounty hunting."
        ),
        "notes": (
            "Hired by Burroughs; ritual-tracked Euphoria with strands of her hair from the penthouse and "
            "hits the flat Sunday 9 a.m. with four Strice guards (armor vest with plates, Seco LD 120, "
            "stun batons for Euphoria, Uzi III) -- told no one where she was. Stats: B6 Q5 S6 C4 I4 W6, "
            "Ess 6, Magic 6; Sorcery (Ritual) 6, Thrown Weapon (Spear) 6, Unarmed 5, Stealth 5, "
            "Magical Theory 5, Etiquette (Tribal) 4, Negotiation 4; Astral pool 14. Spells: Power "
            "Missile 5, Fireball 5, Detect Enemies 3, Mind Probe 6, Detox Deadly Toxin 5, Entertainment "
            "3. Gear: Browning Ultra-Power (firepower ammo, laser), spear, survival knife, plastic "
            "restraints, medicine lodge materials 4. Totem Lion (+2 combat spells, +2 prairie spirits, "
            "-1 health spells). Survivors of his raid have made an enemy who does not forgive."
        ),
        "contact_skills": ["Ritual tracking and bounty hunting (worldwide)", "African shamanic tradition"],
    },
    {
        "name": "Ellery Whitecastle",
        "role": "Phone-only fixer in a smoking jacket who brokers the Ludivenko job; interrogated and firebombed by MegaMedia",
        "archetype": "Fixer",
        "title": "Fixer (deceased -- firebombed by MegaMedia)",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "An expensive suit, slicked-back black hair and green cybereyes on a wristphone screen; a "
            "smoking jacket and a nervously fidgeted pipe the second time. Moderately successful, dresses "
            "in style, lives in comfort, does almost all business by phone and rarely appears in person. "
            "'Greetings, chummer. I've got a job for you and your pals.'"
        ),
        "notes": (
            "Hired by Ludivenko (he suspects, never confirmed) to set up the Pier 36 meet; his fee depends "
            "on the team showing up. Would pick a team that had handled a big-name star before "
            "(Mercurial). After the second disappearance MegaMedia's 'representatives' lean on him; "
            "Carrone has him interrogated and killed fifteen minutes before the runners' meeting -- a "
            "firebomb at his residence, body identified by dental records. Fixer contact stats (SR1 p.167)."
        ),
    },
    {
        "name": "Juan Diablo",
        "role": "Latin razorguy on a gun-mounted Harley Scorpion; Ludivenko's fixer-of-the-week and paymaster (5-5-CHROME)",
        "archetype": "Street Samurai",
        "title": "Street samurai on Ludivenko's payroll",
        "race": "Human",
        "gender": "Male",
        "nationality": "Latin American",
        "organization": "Ludivenko",
        "connection": 2,
        "description": (
            "A gang punk turned samurai on Ludivenko's nuyen: Latin looks, black leather, mirrored shades "
            "over blazing red cybereyes, a plated-up Harley Scorpion urban combat bike with an Ingram "
            "machine gun. Sweeps the pier before the Johnson arrives, crosses his arms on the seat, and "
            "hands out his wristphone number: '5-5-Chrome'."
        ),
        "notes": "Street Samurai stats plus Gunnery 4; Uzi III with shock pads and smartgun adapter, armored vest with plates, the bike's weapons. Backs up the Company Man chauffeur if the meet turns violent; delivers the second half of the fee on uncertified credsticks once Euphoria is free.",
        "contact_skills": ["Line to Ludivenko's Seattle operations", "Muscle on a combat bike"],
    },
    {
        "name": "Vernon Gruder",
        "role": "Overexcited Ludivenko interoffice courier playing spy; delivers the first credsticks; a rabid Euphoria fan",
        "archetype": "Corporate Wage Slave",
        "title": "Interoffice courier, Ludivenko",
        "race": "Human",
        "gender": "Male",
        "organization": "Ludivenko",
        "connection": 1,
        "description": (
            "A short man in an overcoat and a hat several sizes too large who whispers 'Jack Sprat could "
            "eat no fat' at the door, scans the hall for tails, announces loudly that he is here to check "
            "the plumbing, then reads 'Mr. Johnson' off a scrap of paper. Assumes everything said to him "
            "is code and hears two or three meanings in 'want some soykaf?'."
        ),
        "notes": "Totally harmless. Interrogation/Etiquette (Corporate) TN 3 (TN 2 if threatened) gets everything under Ludivenko in the Legwork section. Shown Euphoria he fawns uncontrollably. Mistreating him gets back to Mr. Johnson.",
    },
    {
        "name": "Crucius Bunter",
        "role": "Irritable, overworked dwarf landlord of Royal Meadows Apartments",
        "archetype": "Landlord",
        "title": "Manager / landlord, Royal Meadows Apartments",
        "race": "Dwarf",
        "gender": "Male",
        "age": 35,
        "connection": 1,
        "description": "About thirty-five, face pockmarked by disease, behind the manager's window most hours with the morning fax. Irritable and overworked, responsible for maintenance he has long given up on; complaints get a mumble or a tale of woe.",
        "notes": "Nuyen talks: a small bribe gets repairs, about 100 nuyen calms him if annoyed. Will have questions about the damage after Pride's raid.",
    },
    {
        "name": "Bill Garrety",
        "role": "Owner-bartender of Garrety's who saw his waiter dragged into the sewers and will never say so",
        "archetype": "Bartender",
        "title": "Owner and chief bartender, Garrety's Bar and Grill",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": "A big, beefy man behind the bar talking with customers. Not especially brave; figures a waiter is not worth getting on the bad side of some fanatic cult.",
        "notes": "Bartender stats. Witnessed Van Willis dragged through a manhole out back a month ago; admits only that Willis fits the description and disappeared. Has heard the rumors about the cult taking street people.",
        "contact_skills": ["Downtown pub gossip (for those he trusts)"],
    },
    {
        "name": "Wendy Phillips",
        "role": "Garrety's waitress who saw the missing Van Willis two weeks ago, 'scarred', outside Magic Crafts",
        "archetype": "Waitress",
        "title": "Waitress, Garrety's Bar and Grill",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": "Worked Van Willis's shift and liked the slow, nice kid. Thinks Garrety knows more than he admits and does not blame him. Will talk when he is not nearby, or catch the runners on the way out.",
        "notes": "Drunk and off at the wrong rail stop two weeks ago, she saw Willis under dead streetlights in front of a shop called 'Magic Crafts'; he ran when she called him. She thought the scars were a cult initiation; they are chitin.",
    },
    {
        "name": "Van Willis",
        "role": "Missing Garrety's waiter, now a Flesh Form Worker ant in a torn logo T-shirt guarding Craft's door",
        "archetype": "Waiter",
        "title": "Former waiter, Garrety's Bar and Grill; Flesh Form Worker (Force 1)",
        "race": "Human",
        "gender": "Male",
        "organization": "The Ant Hive (Puyallup)",
        "connection": 1,
        "description": (
            "A nice kid, a little slow, who would not win the mental Olympics. Kidnapped from behind the "
            "bar a month ago while emptying trash; three weeks into possession his skin is 'scarred' with "
            "chitin under heavy bulky clothing, something wrong with his eyes, still wearing the tattered "
            "Garrety's T-shirt he was taken in. He just stands there, looking mean."
        ),
        "notes": "Seen on Euphoria's abduction recording (short black hair, dirty torn jeans, the T-shirt). Flesh Form Worker F1: cannot fight; enhanced smell, reduced sight. His aura is a huge ant. Beyond saving.",
    },
    {
        "name": "Warden",
        "role": "Elven armorer of some repute in a warehouse near the Tacoma docks; if you can pay, he can get it",
        "archetype": "Armorer",
        "title": "Armorer (freelance, MegaMedia's outfitter for the Hive raid)",
        "race": "Elf",
        "gender": "Male",
        "connection": 4,
        "description": "An Elven armorer of some repute working out of a small warehouse near the Tacoma docks. Etiquette (Street) TN 3 to know him: if you want it and can pay for it, he can get it. 'Going hunting, I hear. What you need?'",
        "notes": (
            "Outfits MegaMedia's assault: medium security armor with helmet (7/7; HUD, low-light, "
            "thermographic, signal locator, smartlink, tracking signal, transceiver -- and MegaMedia's "
            "hidden simsense recorders), grenades, a smart primary/secondary/backup weapon with launcher "
            "and IPE mini-grenades, stimulant and trauma patches; everything in the core book and the "
            "Street Samurai Catalog except medium/heavy machine guns and the MP-Laser, Harley Scorpions "
            "or Honda Vikings, even a minigun on a gyro-mount. Track carried weight. Everything goes back."
        ),
        "contact_skills": ["Heavy weapons and military gear on demand (for a price)"],
    },
    {
        "name": "Hans Vandenburg",
        "role": "Euphoria's male co-star in four sims; fit to be tied over their falling-out",
        "archetype": "Simsense Star",
        "title": "Simsense star, MegaMedia",
        "race": "Human",
        "gender": "Male",
        "organization": "MegaMedia Entertainment",
        "connection": 2,
        "description": "The male co-star through whose eyes half of Euphoria's fans have been to her fabulous places. Rumored to have had a real falling-out with her -- 'he's fit to be tied, which I also hear is what he likes best'.",
        "notes": "Industry insiders blame Euphoria's retirement on conflict with him; MegaMedia denies it ('Sure she bugs him occasionally, but she does that to everyone'). No stats.",
    },
    {
        "name": "Solomon Daniels",
        "role": "Craft's fixer who sent him into the jungle after cheap fetishes",
        "archetype": "Fixer",
        "title": "Fixer and magical-supply middleman",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": "Supplied Magic Crafts with fetishes and magical goods, then discovered his own corporate supplier's source: shamans in two South American jungle villages selling for almost nothing. Hired Dorin to fly down and buy them out from under the corp.",
        "notes": "Backstory only; never appears. Does not know what came back from the jungle. A talismonger-trade fixer who could be a future contact -- or the next person the Hive's shaman calls.",
        "contact_skills": ["Talismonger supply chain and fetish sourcing"],
    },
    {
        "name": "The Earl",
        "role": "Metal-toothed bartender who serves neon sake and rents coffins to pass out in",
        "archetype": "Bartender",
        "title": "Bartender (bar unnamed)",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": "A bartender with metal teeth who calls himself The Earl and pours neon sake late into the night; his place rents coffins with lights on voice command and a speaker that squawks check-out time.",
        "notes": "One-scene color from the opening wake-up call. Handy default for 'where the team drank last night'.",
    },
    {
        "name": "Clockwork",
        "role": "Orange-spiked bartender with a Beethoven medallion vidscreen looping an old violent English film; serves 'Rippers'",
        "archetype": "Bartender",
        "title": "Bartender (bar unnamed)",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": "A large man with bright orange hair in a short spike and a big medallion with a tiny vidscreen that constantly plays some violent English film from the last century and shouts something about Beethoven. Serves 'Rippers'; lets you sleep it off in his storage room. 'Have a good nap, mate?'",
        "notes": "One-scene color from the second wake-up call.",
    },
]

ORG_UPDATES = {
    "Knight Errant Security Services": {
        "notes_append": (
            "Queen Euphoria: Strice Foods contracted a four-man Knight Errant team (Group Three training "
            "level -- a cut above corporate guards, not elite: Ares Predator II, H&K MP-5TX, airfoil IPE "
            "concussion grenades, armor jackets) to guard Euphoria around the clock under Osprey, with a "
            "Nightsky driver, a Ford Americar lead car and a Northrup PRC-42D Wasp (LMG, Armorflex) three "
            "minutes away by radio. MegaMedia switched from Lone Star to Knight Errant for all security, "
            "extended the Strice contract, and lost the team to Ant Soldiers at Pacific Towers -- shredded, "
            "'explained' by MegaMedia. Knight Errant investigates the abduction with Lone Star. Nearly a "
            "full company surrounds the Amber Gel plant during MegaMedia's raid, with a Knight Errant "
            "executive observing from the command vehicle who offers 1,000 nuyen per runner for a full "
            "report on the Hive -- a hook for later."
        ),
        "allies_add": ["MegaMedia Entertainment", "Strice Foods"],
    },
    "Lone Star Security": {
        "notes_append": (
            "Queen Euphoria (January 2051): the city contract is up for renewal, negotiations begin next "
            "week (news handout). Lone Star confiscated over 20,000 BTL chips breaking one of the city's "
            "largest smuggling rings. Named co-defendant in Aztechnology's suit over the helicopter that "
            "crashed near the Pyramid the night Honey Brighton got out. Recently dropped by MegaMedia in "
            "favor of Knight Errant. Pacific Towers' PANICBUTTON brings four officers (Browning "
            "Max-Power, stun baton, armor vest) in five minutes; investigates Euphoria's first kidnapping "
            "as 'a fan cult gang rather than professionals'; does not patrol Pier 36."
        ),
    },
    "Aztechnology": {
        "notes_append": (
            "Queen Euphoria: suing the drek out of MegaMedia over the helicopter that crashed near the "
            "Seattle Pyramid the night simstar Honey Brighton was extracted to Brilliant Genesis (the "
            "Ares Dragon crash of the DNA/DOA news handout), Lone Star co-defendant. Strice's Sunday "
            "Amber Gel show was booked for a park near the Pyramid and cancelled by the city to prevent "
            "riots. Euphoria's next sim, Jungle Huntress, was to shoot on location in the Aztlan jungles. "
            "Aztech-Mex products aside, Aztechnology's Stuffer Shacks dispense Ludivenko Lovelies."
        ),
    },
    "Renraku Computer Systems": {
        "notes_append": (
            "Queen Euphoria: Strice's first Amber Gel promotion, Friday afternoon at the Renraku Arcology, "
            "went ahead without Euphoria -- meager attendance, a restless, angry crowd, a public "
            "embarrassment for Strice. Michael 'Osprey' Adams grew up a Renraku corporate kid until a "
            "rival corp extracted both his parents."
        ),
    },
    "Russel Overland Transport": {
        "notes_append": (
            "Queen Euphoria: MegaMedia moves its Hive assault team in a bonded, sealed transport vehicle "
            "crewed by Russel Overland staff drivers -- not MegaMedia employees -- who can testify that "
            "they picked the runners up in one corporate territory and set them down beside another "
            "without anyone leaving the vehicle. Bonded 'deniable transit' is a service Overland sells."
        ),
    },
    "Seattle Metroplex Guard": {
        "notes_append": (
            "Queen Euphoria: city government cancels the third Amber Gel show (a park near the "
            "Aztechnology Pyramid) to prevent riots after the coliseum show ends in rioting; city "
            "officials warn that travel into all tribal lands may be further restricted (January 2051)."
        ),
    },
}

LOC_UPDATES = {
    "Renraku Arcology (SCIRE)": {
        "notes_append": (
            "Queen Euphoria: venue for Strice Foods' first Amber Gel promotion (Friday afternoon), a flop "
            "without its star -- meager, restless, angry crowd handed one-play simsense chips of Euphoria "
            "tasting Amber Gel."
        ),
    },
    "The Barrens (Seattle)": {
        "notes_append": (
            "Queen Euphoria: nearly a hundred Barrens street people vanished in a few weeks, taken through "
            "manholes for Craft's Hive; the street blames 'some cult' ('at first I thought it was a hoax "
            "like that barghest scare last year'). Royal Meadows Apartments sits on the Redmond edge; "
            "Magic Crafts is up in Redmond by St James Lake; the Amber Gel plant is south of Puyallup off "
            "Pioneer Highway."
        ),
    },
}

NPC_UPDATES = {}

TAG_EXISTING = {}

MATRIX_HOSTS = """
**1. Strice Foods main system** (map p.34; SAN number 2206 (312-1752), changes weekly; Etiquette
(Street) 8 / (Corporate) 6 / (Matrix) 5 or a decker contact with 3+ successes to get it). A low-cost
system with no wiz-bang icons. External Alert = complete shutdown within two minutes; Trace results
print automatically at Burroughs' desk and go to Lone Star. Worth building as a modest paydata host.

| Node | Function | Rating / IC |
|---|---|---|
| SAN | Crystal wall and gate with the Strice logo | Red-5, Access 5 |
| SPU-1 | Polygon | Orange-3, Trace and Dump 3 (a shifting ball of light) |
| SPU-2 | Polygon | Orange-3, Killer 4 (a sparkling orange diamond) |
| I/OP-1 | Burroughs' terminal, 10th floor Soykyo Office Plaza (white pyramid) | Green-3, Access 3 |
| I/OP-2 | Departmental desktop terminals (orange pyramids) | Green-2, Access 2 |
| SM | Autopiloted delivery trucks (a Strice truck icon; turret = Blaster). Warns of stuck autopilots; holds the Amber Gel plant's Puyallup address | Orange-4, Blaster 3 |
| CPU | Octagonal room with shimmering walls | Orange-4, Barrier 3, Tar Pit 4 (a mouth that swallows, belches and poisons utilities) |
| DS-1 | Maze of corridors blazing with data: purchase orders (only jars, blue coloring and low-grade nutrisoy go to the plant); MegaMedia's 1,280,000-nuyen fee; Knight Errant and promo expenditures. Four 70 Mp files, 28,000 nuyen | Orange-3, Barrier 4 |
| DS-2 | Library of tunnels and rooms: accounts receivable, three 80 Mp files, 60,000 nuyen | Orange-5, Scramble 3 |
| DS-3 | Rectangular room: Seattle retailers and distributors, two 40 Mp files, 4,000 nuyen | Green-3 |

The GM may seed extra clues here (Craft's shop rent, a Burroughs/Craft meeting memo) if the team stalls.

**2. Pacific Towers building computer** -- not on the Matrix; only the lobby security terminal. I/OP-1
Green-3 Access 3; SM-1 cameras Orange-3 Barrier 3; SM-2 general lighting/heating and the elevators
(open doors, send a car anywhere) Orange-3 Access 4; DS-1 visitor and maintenance records plus the
PANICBUTTON cancel number 2206 (312-1876) and code J87, Green-3; CPU Orange-4 Barrier 3. Build only as a
tiny on-site host for the kidnapping.

**3. Amber Gel facility computer** -- mentioned (a decker can find the name 'Craft' by decking it) but
unmapped; the Trace goes to Burroughs' printer. Improvise a small Orange system if needed.
"""

NOT_BUILT = """
- **Ludivenko's Mr. Johnson** ('real name unimportant'; Mr. Johnson contact, Negotiation 6) and his
  **Company Man chauffeur** (lined coat, silenced Browning Max-Power, explosive ammo) -- on the
  Ludivenko org row.
- **Henry Killian** (Strice Security Director, killed in the plant) and **the Strice Boys** guard block
  -- on the Strice / Pride rows. **Pacific Towers guards, courier and staff**, **Knight Errant guards**
  -- stat blocks on the location and org rows.
- **Honey Brighton, Witt Lipton, Cindy Cyclone, Ted Morgan, David and Helen Variable** (MegaMedia
  stars), **William Welsh, Andrea Stueban, Nick Nathan, Angela Lane**, **Deloris Stanton, Zachary
  Fynche, Jack Tauber** -- leadership entries / notes, not NPC rows.
- **August Dorn** (Independent Contract Overseer under the Corporate Interaction Act of 2038),
  **Lou Buckminster** and the **Euphoriacs** fan club, **Nik Elliot** (industry analyst), **'Mauler'
  Tate** of the Screamers, **the Revenants** (European policlub that bombed a Werner-Voss shuttle) --
  news-handout names.
- **The old Coyote squatter** who taught Dorin, the **jungle shamans and the old man with beady eyes**,
  the **supply corp's silver-and-blue jet**, the **stone pyramid** in the South American jungle --
  prologue backstory on Dorin's row.
- **The Queen Ant Spirit** (Force 5, cocooned) and all Ant Spirit stat blocks -- on the Hive org row.
- **The south-end coliseum** (Saturday riot) and **the park near the Pyramid** (cancelled Sunday show).
"""

PLAY_NOTES = """
- Two runs in one: a light-hearted celebrity 'detention' (bugs in the flat, Vernon Gruder, Euphoria
  nagging) that curdles into horror. Let the magician's Amber Gel vision and the abduction recording
  do the turn.
- The abduction recording is a BTL-strength experience played at full sensitivity; the player relives
  it physically. Electronics B/R 4 (four hours) restores the inhibitors; Electronics 5 (30 minutes)
  copies it to a chip -- the copy is blackmail against Burroughs (-2 TN).
- Nothing magical finds Euphoria after the Hive takes her. No street contact knows anything about the
  second kidnapping. The trail is: recording -> Garrety's / Burroughs -> Magic Crafts / the plant.
- Carrone insists on eight-hourly reports and the contract; refusing the contract means no raid.
  Keep track of loaned gear -- Knight Errant enforces its return.
- Fighting spirits: Willpower instead of weapon skill in melee, double-Force 'armor' vs ranged, Force
  3 Soldiers common, Force 5 rare; insecticide is a Vulnerability.
- Euphoria is beyond rescue. Do not let the players think otherwise until they open the cocoon.
- Karma: first kidnapping 5, Hive destroyed 5, Queen Euphoria destroyed 3.
- Loose ends: Craft if he escaped (the Ants seek him out); the Knight Errant executive who wants a
  report; MegaMedia's sim starring the runners; a Lion shaman with a grudge; Amber Gel withdrawn and
  a hundred families in the Barrens still missing someone; the Universal Brotherhood opening missions.
"""
