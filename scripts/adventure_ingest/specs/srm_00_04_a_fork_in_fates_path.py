# SRM 00-04 A Fork in Fate's Path (FanPro/WizKids, 2004, SR3, version 1.1) -- campaign order #42.
# Seattle: the Elliot Bay dock district and a converted warehouse sound stage in the Puyallup
# Barrens (Rolando's half), Pier 37 and Joeli Gibson's yacht, a halfway house, Renton (Eddie's
# Coffee Shop) and a recycling warehouse in the Tacoma warehouse district (Joey's half).
# SETTING NOTE: Seattle, not Denver -- Elliot Bay, the Puyallup Barrens, Renton, Tacoma, the Ork
# Underground. Denver is not mentioned at all. Every location row is city "Seattle".
# Dating: no in-world date; 2064 as for the rest of Season 0, and this module cites SOTA:2064
# directly (for Or'zet). The Ares sonic rifle is due to debut to the Defense Department "on the
# 15th"; Joey wants the rescue done inside 48 hours.
# STRUCTURE: this is two mutually exclusive adventures in one book. The team is offered Rolando's
# job first and Joey's minutes later, and may take only one -- majority vote, ties broken by the
# total Karma on each side. Players may swap characters at that point but not create new ones, and
# the module explicitly forbids replaying it to see the other path.
# Book editing inconsistencies noted on the affected rows: the opening fiction names Rolando's two
# ork bodyguards "Betty and Betsy" where SRM 00-01 Mission Briefing named them Betsy and Becky
# Ross; the fixer is "Roland" in two places and "Rolando" everywhere else; "Kirkpatric k" and
# "Gang Bang" (contents) versus "Gang Bangers" (body); the "Shooting Stars" scene has no contents
# entry; the gang chamber is "twenty-one meters (seventy feet) wide by (one hundred) feet long"
# with the metric figure dropped; White-out and Burn-bag are printed with identical stat blocks
# and gear apart from their goggles; and the Or'zet flyer entry garbles a name as "a Unified or
# Universal Brotherhood".
# Name collision: the coffee-shop owner is filed as "Eddie (Eddie's Coffee Shop)" because an
# unrelated Eddie already exists (Wake of the Comet).
# Source text: docs/Adventures/text/SRM00-04A_aforkinfatespath.txt (32 pages) and
# docs/Adventures/text/SRM00-04B_aforkinfatespath.txt (player aids, maps and contact cards).
# ASCII only (pre-commit hook).

ADVENTURE = "SRM 00-04 A Fork in Fate's Path"
ORDER = 42
SOURCE = "SRM00-04A_aforkinfatespath.pdf, pp. 3-32; SRM00-04B_aforkinfatespath.pdf (Player Aids), pp. 3-11"
YEAR = "2064"

SYNOPSIS = """
Two phone calls, twenty minutes apart, and only one of them can be answered.

The first is **Rolando** -- Ray Marcello, the gaudy initiate fixer from the Freeway Park meet --
offering 10,000 nuyen a head, 1,000 up front, no questions asked, job in two hours, bring the
heavy gear. At a party he levitated over a crowd to get a look at **Kevin Kirkpatrick**, a
spike-baby elf with six-inch floppy ears who owns **HotSpot Communications** and makes half the
local trideo in Seattle, wrapped the man's admirers in an illusion, walked him into a corner and
bought his way into a new reality show: *RealRunners!* The "new state-of-the-art entertainment
facility" the runners are hired to test is a warehouse in the **Puyallup Barrens** converted into
a sound stage -- a dungeon crawl with memory-plastic walls, thirty-six devil rats dropping out of
the ceiling, a room full of gangers who have been shown planted evidence that the runners murdered
their friends, and a three-meter anthropomorph combat drone for a finale. Snake shamans stand by
to heal whoever survives. On the way out a Perception test spots an action figure in a storage
room, and a whole marketing plan built around the team's faces. Kirkpatrick is unbothered: "No SIN
means no rights to your image, chummer." The gangers will be digitally repainted as Lone Star
patrolmen and corporate wage slaves, and Rolando's cut of the first episode is a million nuyen.

The second call is **Joey** -- Joeli Gibson, on her yacht at **Pier 37** -- with 500 up front,
1,500 on completion, and only 1,000 for herself because the client is an old friend. **Jessica
Ravenwing**, a teenager in the **Church of the Undying Light** halfway house who does not know who
her father is, has been taken. Her father is **Finger**, an independent weapons designer under
contract to **Ares Macrotechnology**, who developed an attack of conscience about the company field
testing the first production run of Ravener SMGs on homeless people in the Barrens. His director,
**Dr. Hamilton**, spent black-ops money to find the daughter Finger has hidden since she was two
and put her on ice with **The Eliminators** until the SCREECH sonic rifle is finished for its
Defense Department debut on the 15th. A divination failed because she is warded; the mages who
tried were torn apart by something that leaves an astral signature like Psychic Manifestation. The
trail runs through Sister Miriam's shelter, an Or'zet flyer dropped behind a floorboard, a
terrified Halloweener called **Burpie** hiding in his brother's coffee shop in Renton, and an Ares
decker named **Hammer-Slammer** who does not use subtlety. It ends in a **Puget Recycling
Cooperative** warehouse in Tacoma, where six professionals are waiting for a phone call that will
tell them whether to hand the girl over or feed her to the crusher.

Cash and a ruined reputation, or 2,000 nuyen and the gratitude of a very talented weapons
specialist. Fate is fickle; the decision is theirs.
"""

TIMELINE = """
- **Some time back** -- Ares contracts the freelance weapons designer "Finger" for the SCREECH
  sonic rifle program in Seattle. He solves the power coupling problem and has only the wave pulse
  regulator left, and starts asking Dr. Hamilton about the Ravener field trials in the Barrens.
- **Hamilton reports the problem to Dr. Murakami**, who tells him to find the motivation. Black-op
  funds are approved; outside operatives shadow Finger and dig up his past.
- **Three days later** -- Jessica Ravenwing is located in a halfway house in the sprawl and
  confirmed as his daughter. The Eliminators are contracted to take her and keep her on ice.
  Hamilton privately considers both father and daughter expendable afterwards.
- **Recently** -- Jessica is snatched from the Church of the Undying Light shelter; her records are
  professionally wiped from the shelter's system; Burpie, casing the PRC warehouse for a
  Halloweener raid, sees her carried in inside a blue sack and is shot at on his way out.
- **The Johnson hires mages** at the Snake Lodge to find her by divination and ritual tracking.
  The ward defeats them; days later every member of the Lodge is found murdered, the blood flung
  across the walls, ceiling and floor.
- **At a Seattle party** -- Rolando levitates over the crowd, illusion-screens Kevin Kirkpatrick
  away from his admirers, and buys into RealRunners! as an investor and talent scout. He arranges
  for gang members to be murdered and the blame planted on the runners he intends to hire.
- **Day 1, evening** -- Rolando calls: 10,000 nuyen, two hours' notice, heavy gear, southern dock
  district. Minutes later Joey calls: 2,000 nuyen, a rescue, Pier 37 in about twenty minutes. The
  team chooses; the other job closes immediately and Rolando or Joey reacts accordingly.
- **Rolando's path, that night** -- the docks, Stick's van, the Puyallup warehouse, the door, the
  devil rats, the gangers, the combat drone, the healing, the payoff, and the storage room.
- **Joey's path, over the next 48 hours** -- the yacht, the shelter, the Snake Lodge, the Matrix,
  Eddie's Coffee Shop, and the PRC warehouse in Tacoma. Then back to Pier 37, where Finger is
  waiting.
"""

ORGS = [
    {
        "name": "HotSpot Communications",
        "org_type": "media",
        "tier": 2,
        "headquarters": "Seattle; production sound stage in a converted Puyallup Barrens warehouse",
        "summary": "Small Seattle trideo film firm behind Eye on Seattle and the reality show RealRunners!",
        "description": (
            "A small trideo film firm in Seattle, owned and mainly produced by Kevin Kirkpatrick, "
            "who has spent about fifty years slowly building it into an empire. HotSpot makes a lot "
            "of the local trideo: Eye on Seattle, Good Morning, Seattle, and Puget Sound Nightlife "
            "among them. Its next project is RealRunners!, a reality show built around the elusive "
            "figures the public sees on the reality cop shows and blames for half the damage done "
            "to government and corporate property -- a show Kirkpatrick expects to skyrocket in the "
            "ratings and earn him millions of cred and reputation. He pitches it as an honest look "
            "behind the scenes from the runners' point of view, to settle whether they are the "
            "Robin Hoods some people believe or the public enemies others say. It is nothing of the "
            "kind."
        ),
        "notes": (
            "How RealRunners! actually works: hire real shadowrunners to walk a lethal course in a "
            "converted warehouse, film everything from concealed cameras, then use digital "
            "manipulation to repaint the opposition -- gang members Rolando had murdered and framed "
            "the runners for -- as Lone Star patrol officers and innocent corporate wage slaves. "
            "Whether the runners were actually monsters is immaterial; public perception is what "
            "counts. Rolando bought in as a major investor and talent scout and stands to make a "
            "million nuyen from the first episode. Because the runners are SINless they have no "
            "legal claim to their own images, and the marketing plan already in prototype -- "
            "posters, action figures, comics, lunch boxes, toy weapons modelled on the team -- is "
            "entirely legal. Assets: a rigger, Stick, on 1,000 nuyen a night; three Snake shamans "
            "on retainer as a medical team; four anthropomorph combat drones; Sony production kit "
            "worth 25,000 nuyen fenced, a Sony TridMaster 4000 (14,000 fenced), and the Sony "
            "TrideoMax digital manipulation suite (Spoof 5 / Read-Write 2). Aftermath: destroy the "
            "footage and the plan and the runners stay anonymous; leave it and they become minor "
            "celebrities, which cuts both ways."
        ),
        "allies": ["Seattle Mafia"],
    },
    {
        "name": "The Eliminators",
        "org_type": "shadowrunner team",
        "tier": 3,
        "headquarters": "Seattle; operates out of rented facilities such as the PRC warehouse in Tacoma",
        "summary": "Infamous professional runner team specializing in wetwork and extractions, and in keeping people on ice.",
        "description": (
            "A crack team of shadowrunners who have worked the Seattle shadows for years doing the "
            "jobs nobody else likes to touch: wetwork and high-profile extractions. They excel at "
            "making people disappear and keeping them on ice until a Johnson needs them again. "
            "Their leader is a former corporate security director who knows all the tricks, and the "
            "roster runs to former special ops, former Lone Star SWAT and others who understand "
            "their targets' routines and get the job done. Six members: White-out, Shredder, "
            "Eraser, Burn-bag, Degauss and Vaporize, all professional rating 4 and all "
            "extensively augmented."
        ),
        "notes": (
            "Street legwork on the name, Etiquette (8): 0 successes gets a joke about a cleaning "
            "company on Denny Street ('they'll get any stain out of a carpet in 30 minutes or "
            "less'); 1 that they are runners in Seattle who ELIMINATE problems; 2 the wetwork and "
            "extraction specialty; 3 the leader's corp-security background and the special ops and "
            "Lone Star SWAT alumni. Hired by Ares through Dr. Hamilton's black-ops budget to take "
            "Jessica Ravenwing and hold her until Finger delivers SCREECH. Method: rent a facility "
            "whose owner is compensated to suspend operations, install their own cameras, stock a "
            "week of supplies, ward the room the charge is held in, and wait for the telecom call "
            "that says hand her over or get rid of her. When it is the latter they use the site's "
            "industrial machinery -- at the PRC warehouse, the metal crusher, with the body going "
            "out on the next load to the smelters. Deployment at the warehouse: two on the "
            "catwalks, two in the upstairs office on the monitors, two patrolling the floor, with "
            "one going down to check the girl occasionally. Almost certainly also responsible for "
            "the massacre at the Snake Lodge, though the astral signature there resembles Psychic "
            "Manifestation and matches nothing in their known roster -- an unexplained loose end."
        ),
        "enemies": ["Halloweeners"],
    },
    {
        "name": "Puget Recycling Cooperative",
        "org_type": "corporation",
        "tier": 1,
        "headquarters": "Warehouse district, Tacoma, Seattle",
        "summary": "Small Tacoma metal recycler whose warehouse the Eliminators rent as a holding site and body disposal.",
        "description": (
            "PRC is a small recycling business specializing in metals: it separates material by "
            "type and crushes it into cubes like those from a car crusher, which are trucked to a "
            "smelting facility deeper in Tacoma. Most of its work comes from the shipyards and the "
            "occasional construction job. It has recently secured a contract with Lone Star to "
            "destroy small arms recovered from the street and released after processing, because "
            "evidence lockers are only so large -- though the guns themselves are too small to "
            "crush and go straight to the smelters rather than to this yard, a detail the "
            "Halloweeners got wrong. The company logo is a three-prong recycle symbol in royal "
            "gold, dark blue and metallic grey around the letters PRC, and it appears on the "
            "uniforms, the containers and the trucks -- but never on the outside of the warehouse."
        ),
        "notes": (
            "The nasty part: PRC is 'compensated' to suspend operations whenever the Eliminators "
            "want the warehouse, which they use as a holding site and, when the order comes, as a "
            "disposal site -- the victim goes into the crusher and out with the next load to the "
            "smelters. Runners who tip off Lone Star, a news service or another public body about "
            "PRC's arrangement and what has happened at the warehouse earn a point of team Karma: "
            "within days Lone Star impounds the site, finds evidence of previous activities that "
            "substantiates the story, and brings PRC officials to justice. The Halloweeners had "
            "been planning to hit the place for SMGs and assault rifles they believed were being "
            "destroyed there -- guns already marked destroyed, so Lone Star would no longer hold "
            "the ballistics records. Burpie was casing it for that raid when he saw the girl "
            "brought in."
        ),
        "allies": ["The Eliminators"],
    },
    {
        "name": "Church of the Undying Light",
        "org_type": "church",
        "tier": 1,
        "headquarters": "Seattle",
        "summary": "Seattle church running a halfway house shelter where Jessica Ravenwing was living when she was taken.",
        "description": (
            "A Seattle church whose visible work in the module is a halfway house for young people "
            "with nowhere else to go. It is run day to day by Sister Miriam, who keeps the place "
            "going on donations and the labor of the residents themselves -- Jessica Ravenwing "
            "helped out with the chores, and Sister Miriam is now looking for another little helper "
            "because the electrical outlets and the roof leaks are not going to fix themselves. "
            "Money is short enough that she bakes cookies for the donation drives herself."
        ),
        "notes": (
            "The shelter is where Finger placed his daughter and where the Eliminators took her "
            "from. Its computer records had every trace of the girl professionally wiped -- nothing "
            "else touched or mangled, which a Computer (4) test identifies as a professional job. "
            "The house has essentially no security, physical or Matrix, though Hammer-Slammer has a "
            "tracer sitting on it. Sister Miriam will cooperate with anyone investigating the "
            "abduction without any donation at all, though the module attaches a point of team "
            "Karma to characters who come back afterwards and spend a week doing the repairs, "
            "annotated on their calendars. Other residents saw the abduction and their accounts "
            "vary wildly -- the children are an imaginative lot who want to impress real "
            "shadowrunners and will happily name state-of-the-art gear they never saw."
        ),
    },
    {
        "name": "Snake Lodge",
        "org_type": "mystical fellowship",
        "tier": 1,
        "headquarters": "Seattle (former habitat, now a crime scene)",
        "summary": "Small, highly regarded divination and enhancement service, murdered to a man for looking for Jessica Ravenwing.",
        "description": (
            "The Snake Lodge was a small but highly useful divination and enhancer service in "
            "Seattle with a solid reputation among people who needed something found. Quiet "
            "inquiries with any appropriate contact (TN 4) establish what they did and what "
            "happened to them: hired by Finger to locate his daughter by divination and ritual "
            "tracking, they failed -- she is warded -- and then every member of the group met an "
            "untimely end. Lone Star's file records no signs of entry and no reported disturbance "
            "in the area, and yet all of them were brutally murdered, their blood flung along the "
            "walls, the ceiling and the floor, almost as if some rabid beast had attacked. The Star "
            "has no leads."
        ),
        "notes": (
            "The lodge doubles as a crime scene and a clue cache. Normal Perception (5): 1 success "
            "sees where they died from the pooled blood; 2 finds bits of blood and bone -- whatever "
            "did it was thorough; 3 turns up a tiny lock of Jessica Ravenwing's hair in a plastic "
            "case hidden in the dust; 5 finds a single-page Or'zet flyer dropped behind a "
            "floorboard with 'Ravenwing' and an elaborate series of numbers handwritten in the "
            "margin -- an encoded address that a mapsoft of greater Seattle plus a Decrypt program "
            "resolves at TN 6 into a warehouse in Tacoma. Astral Perception (4): 3 successes reads "
            "a style of magic that is definitely neither shamanic nor hermetic and that no runner "
            "has encountered before; 5 identifies the signature of the attack as closely related to "
            "Psychic Manifestation. The module never explains who or what killed them, which makes "
            "the Lodge the single best unresolved hook in Season 0."
        ),
        "enemies": ["The Eliminators", "Ares Macrotechnology"],
    },
]

LOCATIONS = [
    {
        "name": "HotSpot Communications Studio A",
        "location_type": "corporate facility",
        "city": "Seattle",
        "district": "Puyallup Barrens",
        "security_level": "Corporate High Security",
        "controlling_org": "HotSpot Communications",
        "summary": "Abandoned Barrens warehouse converted into the RealRunners! dungeon set, with a lethal course beneath it.",
        "description": (
            "From the outside it is nothing: a featureless warehouse about forty meters long by "
            "thirty wide with six-meter aluminium walls, standing on flat open ground inside a "
            "chain link fence closed with an old-fashioned padlock, in the middle of the Puyallup "
            "Barrens. No security, no workers, nothing -- just the moon, the wind whistling through "
            "the walls and the creak of the siding, which is precisely what makes a careful team "
            "nervous. Smack in the middle of the empty floor a set of archaic stone steps descends "
            "six meters to a sunken ornate wooden door four meters tall, and past it a narrow "
            "corridor barely wide enough for two (one, for a large troll), then a great stone "
            "chamber twenty-one meters wide hung with a red velvet curtain, then a vehicle-sized "
            "door at the far end. Beyond the concealed exit is a brightly lit hallway of production "
            "and workshop rooms sloping up to double doors that open on the street a block from "
            "where the team was dropped off."
        ),
        "notes": (
            "Maps: SRM00-04B pp.4-6 (Studio A - 'Real Runners!', the entry warehouse, and the great "
            "stone room). Key areas: main entry with astral barriers, main corridor, hall control "
            "room, rat rooms, bathroom, trideo processing (Area H), control rooms, storage (Area J), "
            "the sloped exit hallway (Area F). ENTRY: one beam carries a hidden rating 8 ultrasound "
            "detector disguised as a support, another a passive IR motion detector primarily meant "
            "to register the team entering the building; both are backups if the corridor trap is "
            "bypassed. The wooden door has a complex mechanical lock -- Lockpicking, Security "
            "Systems B/R or any hand-crafting knowledge at TN 7, with +4 for modern-technology "
            "skills because the mechanism is simple in technology and complex in mechanics; barrier "
            "15 against brute force, -1 per extra person ramming, and two strong characters can "
            "always break it for 10S Impact each. ASTRAL: scouts move freely in and around the "
            "warehouse and can find the stair, but cannot pass through the floor; going outside and "
            "down through the earth eventually meets a 'living wall'; below ground every wall is "
            "warded. CORRIDOR: the walls are memory plastic that changes shape on an electrical "
            "charge -- Chemistry or Security Systems (8), or Perception (10), to work that out; a "
            "hidden camera sits at the far end (Perception (10)) and three watchers hover barely "
            "perceptible (Astral Perception (5)), instructed to materialize so the operator behind "
            "the wall knows where the runners are even if they are invisible. Destroy all three "
            "before they report and the trap never fires. THE RAT TRAP: a loud click gives one free "
            "combat phase, then the stone goes transparent, the floor panels drop to bare metal "
            "latticework and 36 devil rats pour from the walls, floor and ceiling. THE CHAMBER: "
            "real stone, feels chilling astrally, no other exit until the curtain drops -- manually, "
            "from the control booth, once enough runners are inside. THE FINALE: an anthropomorph "
            "combat drone through the vehicle door; Perception (6) finds the cameras, TN 10 the "
            "concealed side door with its rating 5 electronic lock and hidden palm reader. Area H "
            "holds the Sony processing kit -- Computer (5) with a threshold of 3 (Hacking Pool "
            "allowed) deletes or extracts all footage of the team, and a threshold of 5 purges "
            "every record of their weapons, suspected cyberware and spells. Area J is the marketing "
            "storage room: prototype posters, action figures, comics, lunch boxes and toy weapons "
            "modelled on the runners, spotted on a Perception (8) through a door left slightly ajar. "
            "On a later return only technicians are present (no combat ability, they capitulate to "
            "any show of force); the drones are confined to the outside and Areas F and J and "
            "cannot follow through single-hung doors."
        ),
    },
    {
        "name": "Pier 37",
        "location_type": "transportation hub",
        "city": "Seattle",
        "district": "Waterfront",
        "security_level": "Patrolled / Commercial",
        "summary": "The pier where Joeli Gibson berths her yacht; the meet and the wrap for the rescue half of the adventure.",
        "description": (
            "A working pier on the Seattle waterfront where the fixer Joeli Gibson keeps her private "
            "yacht tied up when she is in town, which is not often -- she generally stays aboard, "
            "out on Puget Sound. The meet happens in the yacht's saloon, where Joey sits in a plush "
            "leather armchair with her legs straddled over the edge and nods at each runner as they "
            "come in. It is also where the adventure ends: the team brings Jessica Ravenwing back "
            "here, Finger is waiting, and once the business is done Joey asks everyone off, "
            "disengages from the pier and rigs in to take her passengers out into the Sound and "
            "somewhere else entirely."
        ),
        "notes": (
            "The whole Cruisin' With Joey half opens and closes here. Joey's terms: 500 nuyen each "
            "up front, 1,500 on completion, non-negotiable, and she is only taking 1,000 for "
            "herself to cover expenses because the client is an old friend -- 'I do have to make "
            "ends meet.' She cannot pass messages back to the Johnson during the run. Bonus at the "
            "wrap: if Jessica is unharmed and unmarked -- wounds healed, clothes mended, no trace "
            "-- Finger pays an extra 500 nuyen each and puts himself at the team's disposal through "
            "Joey for weapon modifications, custom weapons or fencing. Anyone crass enough to "
            "follow the yacht out by drone or astrally should be stopped short by something "
            "unrelated: a Lone Star reconnaissance drone interrogating their responder chip, a free "
            "spirit stopping an astral traveller for questions."
        ),
    },
    {
        "name": "Church of the Undying Light Halfway House",
        "location_type": "residential community",
        "city": "Seattle",
        "district": "Seattle metroplex",
        "security_level": "Low Security",
        "controlling_org": "Church of the Undying Light",
        "summary": "Run-down church shelter where Jessica Ravenwing lived and from which the Eliminators took her.",
        "description": (
            "A halfway house shelter run by the Church of the Undying Light, housing young people "
            "with nowhere else to go and kept running on donations and their labor. Sister Miriam "
            "is generally in the kitchen -- baking cookies for a donation drive when the runners "
            "arrive -- and the building needs work she cannot keep up with: electrical outlets, "
            "leaks in the roof, the general upkeep that Jessica used to help with. The residents' "
            "quarters are plain, and a resident's possessions fit in a box."
        ),
        "notes": (
            "Jessica's last known location, and where the thugs took her from. Sister Miriam "
            "cooperates in any reasonable way with anyone investigating the abduction, without "
            "needing a donation, and will give the team access to Jessica's room and her box: "
            "strands of hair in a hairbrush and other DNA samples, a locket, a small doll, an old "
            "blanket from when she was young -- enough for ritual sorcery, though the ward at the "
            "warehouse defeats it. Nobody in the area got a good look at the abductors and the "
            "children's accounts vary wildly in number and description; some of them follow "
            "state-of-the-art gear closely enough to name equipment they never saw, purely to "
            "impress real shadowrunners. The shelter's computer records have every trace of the "
            "girl professionally wiped with nothing else touched (Computer (4) to identify a "
            "professional job); security is effectively nil, but Hammer-Slammer has a tracer "
            "sitting on the system. Team Karma: 1 point for characters who state they will return "
            "after the run, annotate a week on their calendars, and spend it doing Sister Miriam's "
            "repairs."
        ),
    },
    {
        "name": "Eddie's Coffee Shop",
        "location_type": "restaurant",
        "city": "Seattle",
        "district": "Renton",
        "security_level": "No Security / Barrens",
        "summary": "Greasy-spoon coffee shop in Renton run by an ex-Halloweener, hiding his terrified younger brother in the back office.",
        "description": (
            "A hole-in-the-wall in Renton serving simple sandwiches, donuts and coffee to a rough "
            "clientele -- definitely no Starbucks, though the soycaf is hot and fairly good for a "
            "greasy spoon. A little bell rings over the front door, and about a dozen grizzled, "
            "unshaven, mostly human customers look up at anyone who comes through it as though a "
            "sewer spirit had just been summoned to torment them. The man behind the counter has a "
            "cigar and a long scar down his left cheek, and his welcome is: 'Hey, the street's free "
            "but a cup of coffee is five nuyen -- drink or scram!'"
        ),
        "notes": (
            "Where Burpie is hiding. Eddie owns the place, is an ex-Halloweener, and is Burpie's "
            "older brother. He hates everyone equally and verbally abuses anyone who looks out of "
            "place, with a particular dislike of metahumans of any type and pretty-boy face "
            "characters. Former Halloweeners are known and treated as family; a character with "
            "Charisma 3 or less who looks like a fighter and has a Halloweener contact is welcome "
            "too; anyone else with proper street etiquette is merely tolerated. More than three "
            "runners in the shop at once makes him immediately wary -- they are obviously the team "
            "Burpie warned him about. Gain his trust (200 nuyen goes a long way) and he takes them "
            "to the back office. Fail, and Eddie plus four of the patrons try to thump the team and "
            "take their gear, credsticks and clothing to the local fence. If the runners make a "
            "good impression, Eddie and Burpie can raise the Halloweeners to hit the PRC warehouse "
            "as a diversion, or to come and get the team out if it all goes wrong."
        ),
    },
    {
        "name": "PRC Tacoma Warehouse",
        "location_type": "corporate facility",
        "city": "Seattle",
        "district": "Tacoma warehouse district",
        "security_level": "Corporate Standard",
        "controlling_org": "Puget Recycling Cooperative",
        "summary": "Recycling warehouse rented by the Eliminators as a holding site; Jessica is tied up in the women's showers.",
        "description": (
            "A long cracked sidewalk runs from the street to a yard behind a three-meter chain "
            "fence with dark blue slats woven top to bottom on all four sides. Each corner of the "
            "fence anchors to a concrete tower five meters high and two across, and strong halogen "
            "lamps behind well-shielded Plexiglas on top of the platforms bathe the yard in light "
            "and leave almost no shadow -- it is hard not to conclude it was designed that way. "
            "Even the containers are stacked in tight piles with nothing that cannot be seen from "
            "the towers. The gate carries a heavy chain and an ordinary key padlock. Fifty-five "
            "gallon steel drums stand just inside the fence, with occasional piles of debris "
            "grouped by material across a dirt yard broken by concrete slabs where nothing grows. "
            "The warehouse itself is featureless, forty meters by twenty, recently painted dark "
            "blue and already scoured by the acid rain, with no graffiti anywhere: truck-sized "
            "sliding doors at the front and a man-sized door in the side."
        ),
        "notes": (
            "Map: SRM00-04B p.7 -- front personal entry, sliding vehicle door, stairs up to the "
            "second-floor office, ladder to catwalks, catwalks over the whole floor, main warehouse "
            "and recycling debris, sorting hoppers, conveyor and lift ramp, repair pitch with "
            "tools, women's and men's locker rooms, compactor and generators, forklift and fuel "
            "tank with a crane above. Inside: catwalks on the upper level overlook everything; a "
            "single metal staircase at the front winds up to a lit office; heavy processing "
            "machinery and the crusher fill the back left corner with dark blue containers ringed "
            "around it; a truck and a light service area sit further down; two locker rooms hold "
            "bathrooms and showers. Four cameras are just visible in the upper shadows -- the "
            "Eliminators installed extras of their own, though Burpie bypassed them by luck. The "
            "sliding doors are six inches of reinforced steel running on wheeled steel tracks. "
            "Jessica is tied to a chair in the women's shower; the entire bathroom and shower area "
            "is warded against scrying, which is why the divination failed. Deployment: two "
            "Eliminators on the catwalks (Shredder sniping from a corner), two in the office "
            "watching the monitors (White-out among them), two patrolling the floor and the "
            "machines, with one going down to check on the girl now and then. They are waiting for "
            "a telecom call telling them to hand her over or put her in the crusher, and they have "
            "supplies to sit here a week. If the whole team is taken, they wake tied up with "
            "cyberware neutralized and mages in masks, and can try to escape -- possibly with "
            "Burpie and Eddie bringing the Halloweeners in."
        ),
    },
    {
        "name": "The Snake Lodge",
        "location_type": "ruins",
        "city": "Seattle",
        "district": "Seattle metroplex",
        "security_level": "Low Security",
        "controlling_org": "Snake Lodge",
        "summary": "Former habitat of a divination fellowship, now an unexplained massacre scene holding two vital clues.",
        "description": (
            "The former habitat of the Snake Lodge, a small divination and enhancement service with "
            "a good quiet reputation, and now a room Lone Star has processed and abandoned. The "
            "bodies are gone but the pooled blood still marks where each of them died, and the "
            "blood was flung along the walls, the ceiling and the floor as though a rabid beast had "
            "been let loose in the room. There were no signs of entry and no reported disturbance "
            "in the area. Astrally the whole place tastes distinctly wrong -- a style of magic that "
            "is definitely neither shamanic nor hermetic, and that nobody the runners are likely to "
            "ask has met before."
        ),
        "notes": (
            "Joey directs the team here if they want to know who cast the failed divination; quiet "
            "inquiries with an appropriate contact at TN 4 establish the Lodge's reputation and its "
            "fate. Normal Perception (5), taking the best result: 1 the pooled blood; 2 bits of "
            "blood and bone, thoroughly done; 3 a tiny lock of Jessica Ravenwing's hair in a "
            "plastic case hidden in the dust; 5 an Or'zet flyer dropped behind a floorboard, with "
            "'Ravenwing' and an elaborate series of numbers in the margin. Cryptography or any "
            "Computer skill identifies the numbers as an encoded address; a greater-Seattle mapsoft "
            "plus a Decrypt program at TN 6 resolves it to the Tacoma warehouse. Astral Perception "
            "(4): 3 successes for the unfamiliar magical style, 5 to place the attack's signature "
            "as closely related to Psychic Manifestation. The flyer itself needs Or'zet (TN 5) and "
            "is a separate plot entirely -- see the Ork Underground. Nothing in the module says who "
            "killed them."
        ),
    },
]

NPCS = [
    {
        "name": "Kevin Kirkpatrick",
        "role": "Spike-baby elf media mogul behind HotSpot Communications and RealRunners!; the Johnson for Rolando's half",
        "archetype": "Media Mogul",
        "title": "Owner and principal producer, HotSpot Communications",
        "race": "Elf",
        "gender": "Male",
        "organization": "HotSpot Communications",
        "connection": 4,
        "description": (
            "Very short for an elf, only about 1.5 meters, with the largest and longest ears anyone "
            "at the table has ever seen -- almost six inches, floppy, comic. The module's own "
            "comparison is the twin brother of Ross Perot with pointed ears. He is extremely "
            "sensitive about his appearance, and a GM should watch the players closely: anyone who "
            "makes fun of his looks will be repaid severely later. For the moment he is all smiles "
            "and hugs, because they are about to make him a great deal of money. He arrives fifteen "
            "minutes late in a large black Mitsubishi Nightsky with numerous hidden weapon ports "
            "and a very heavy astral presence, and lets a two-meter elf driver open the door for "
            "him."
        ),
        "background": (
            "One of the precursor elves from the Age Before -- a spike baby, born an elf in the "
            "early 1990s -- who endured ridicule and prejudice over his ears and mannerisms long "
            "before there was any explanation for them, and who is doomed by a genetic abnormality "
            "and a highly persistent curse to look a complete freak. When magic returned he "
            "embraced it and can perform small prestidigitations himself; large mental illusions of "
            "the kind Rolando used on him at the party are well out of his range, which is exactly "
            "why he found the demonstration intriguing rather than offensive. He has spent some "
            "fifty years building HotSpot Communications into a small empire producing Eye on "
            "Seattle, Good Morning, Seattle and Puget Sound Nightlife, and now wants the show that "
            "makes him millions."
        ),
        "notes": (
            "No stat block; he is a producer, not a combatant, and he has staff for that. Terms: "
            "10,000 nuyen each, non-negotiable -- he will honor whatever Rolando agreed as an "
            "advance but will not raise the total no matter how well the team negotiates, and he "
            "pays on the spot. His pitch: 'I am testing a new state-of-the-art entertainment "
            "facility... I want to pay each of you 10,000 to go in and take down anything you find "
            "there. There will be tests of cunning, courage and combat.' He gives no layout and "
            "answers as little as possible to keep the test authentic, with one exception -- he "
            "will happily discuss firepower, because the bigger and more explosive it is the better "
            "for him. He promises a full medical team of specialist mages standing by, and delivers "
            "(three Snake shamans who heal everything, by GM fiat if necessary). Confronted about "
            "the marketing plan: 'No SIN means no rights to your image, chummer. Shame you found "
            "out about it, since I could really have used you guys for future events... unless of "
            "course you plan on leaving peacefully. You guys don't strike me as the leaving "
            "peacefully type though...' If it comes to a fight he has no intention of letting them "
            "leave alive: the shamans buff and hide him and get him out to a safehouse while the "
            "drones handle the rest."
        ),
        "contact_skills": ["Seattle trideo and media production", "Celebrity and high-society access"],
    },
    {
        "name": "Stick",
        "role": "Rigger paid 1,000 nuyen to drive the runners to the RealRunners! set and not ask questions",
        "archetype": "Rigger",
        "title": "Freelance driver for HotSpot Communications",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": (
            "The man behind the wheel of a large unmarked black van, who knows where the runners "
            "are supposed to go and nothing else he is willing to say. If they have brought more "
            "gear than fits in the van he will drive slowly enough for them to follow. He stops at "
            "the fence, points, and says: 'The entrance is inside the warehouse boys. Good luck.' "
            "He is still waiting when they come out, a block over from where he dropped them, and "
            "will take them wherever they specify."
        ),
        "background": (
            "A freelance rigger who was paid 1,000 nuyen to drive a bunch of shadowrunners from "
            "point A to point B in a van Mr. Johnson provided. That is genuinely the extent of his "
            "involvement, and he took the job the way any rigger takes a night's work."
        ),
        "notes": (
            "No stat block. He will not volunteer anything, but Mind Probe gets what he actually "
            "thinks: something really weird is going on, this is definitely not a normal "
            "shadowrun, and he does not trust Rolando as far as he could throw him. That is the "
            "cheapest early warning the module offers, and a team with a mind-reading mage can have "
            "it before they ever go down the stairs. He is also the module's soft nudge if the "
            "runners stall outside the warehouse -- he will mention that Kirkpatrick is expecting "
            "them to report back soon."
        ),
        "contact_skills": ["Driving and vehicle work", "Odd jobs in the Puyallup Barrens"],
    },
    {
        "name": "Jessica Ravenwing",
        "role": "Teenage kidnap victim held to force her father to finish an Ares weapons project; does not know who he is",
        "archetype": "Civilian",
        "title": "Resident, Church of the Undying Light halfway house",
        "race": "Human",
        "gender": "Female",
        "nationality": "Native American",
        "connection": 1,
        "description": (
            "An attractive Native American girl with jet black hair, seen by Burpie being carried "
            "into the warehouse in a large blue sack, bound and gagged, and half dragged into the "
            "women's locker room by two large men. When the runners find her she is tied to a chair "
            "in the shower area of a warded bathroom. At the shelter she was the one who helped "
            "Sister Miriam with the chores, and Sister Miriam liked her a great deal and has been "
            "struggling with the upkeep since she disappeared."
        ),
        "background": (
            "Ravenwing is the surname her father gave her to keep their connection secret, and she "
            "has not known him since she was two years old -- as an independent contractor who does "
            "not trust corporations, he separated himself from her deliberately against exactly the "
            "possibility that has now occurred. She grew up in the sprawl and ended up in the "
            "Church of the Undying Light's halfway house. Her belongings fit in a box: a hairbrush, "
            "a locket, a small doll, an old blanket from when she was young."
        ),
        "notes": (
            "No stat block; she is the objective, not a combatant. Held in the women's shower at "
            "the PRC warehouse, tied to a chair, in an area warded specifically to defeat scrying "
            "-- which is why Finger's divination failed and, indirectly, why the Snake Lodge is "
            "dead. The Eliminators are waiting on a telecom call that will tell them either to hand "
            "her over or to put her in the crusher and send her out with the next load to the "
            "smelters. Team Karma: 2 points for saving her without injury. At the wrap, if she is "
            "unharmed and unmarked -- healed, clothes mended, no trace of harm -- Finger pays a 500 "
            "nuyen bonus per runner and makes his services permanently available. She is never told "
            "on screen who her father is; what the runners choose to say to her is left entirely "
            "open."
        ),
    },
    {
        "name": "Finger (Ravenwing)",
        "role": "Independent weapons designer under Ares contract whose conscience got his daughter kidnapped; the module's Johnson",
        "archetype": "Weapons Designer",
        "title": "\"Finger\" -- freelance weapons specialist, lead engineer on the Ares SCREECH program",
        "race": "Human",
        "gender": "Male",
        "nationality": "Native American",
        "connection": 4,
        "description": (
            "A tall and muscular Native American man waiting on Joey's yacht at the end of the run. "
            "He introduces himself only as Finger and explains that he has tired of the recent "
            "practices he has learned of at Ares; he will not go into it further, and he will not "
            "answer many questions. In the lab he is quieter and sharper than his employers expect: "
            "'The SCREECH will be ready soon -- I've solved the power problem by modifying the "
            "power coupling to the battery unit. The emitter should have enough power from a "
            "standard MK-III battery for over a dozen uses. I just need to clean up the wave pulse "
            "regulator.' And then, in a low voice, the question that started all of this."
        ),
        "background": (
            "A highly watched contract employee -- an independent contractor for hire, currently "
            "Ares Macrotechnology's lead engineer on a sonic disruptor rifle called SCREECH, due to "
            "debut to the Defense Department on the 15th. He asked Dr. Hamilton whether it was true "
            "that Ares had been field-testing the initial production run of the new Ravener SMGs on "
            "homeless people in the Barrens, and was told his employers were paying a substantial "
            "rate for his services, not his politics. Because he does not trust corporations he has "
            "kept his daughter Jessica at arm's length since she was two, under a name of his own "
            "choosing; her existence was supposed to be the one thing they could not use. He now "
            "suspects his preparations were not enough. He could get himself out easily; he hires "
            "the runners so that Jessica is clear of the blast when he does, and there is a window "
            "of opportunity that closes in about 48 hours."
        ),
        "notes": (
            "No stat block; he appears only in the fiction and at the wrap. Employer's view: "
            "Hamilton considers both Finger and his daughter expendable once SCREECH is finished. "
            "Reward for a clean rescue: 500 nuyen bonus each on top of the 2,000, plus a standing "
            "offer -- call him through Joey and he will do weapon modifications, build special "
            "weapons, or fence goods. That contact is the whole point of taking the low-paying job, "
            "and is worth considerably more over a campaign than Rolando's 10,000 nuyen. He is also "
            "the reason the Snake Lodge is dead: he hired them to find Jessica by divination and "
            "ritual tracking, they failed against the ward, and then someone killed all of them."
        ),
        "contact_skills": ["Weapon modification and custom weapon construction", "Fencing", "Ares weapons projects"],
    },
    {
        "name": "Dr. Hamilton",
        "role": "Ares project manager on SCREECH who ordered Jessica Ravenwing kidnapped to keep her father working",
        "archetype": "Corporate Scientist",
        "title": "Project director, SCREECH sonic disruptor program, Ares Macrotechnology",
        "race": "Human",
        "gender": "Male",
        "organization": "Ares Macrotechnology",
        "connection": 3,
        "description": (
            "The man who walks into the research lab to check on progress and scowls when he gets a "
            "question instead of an answer: 'Our field trials are none of your concern -- I believe "
            "the question I asked you dealt with your progress on the sonic rifle!' A middle "
            "manager with a schedule, a deadline and a superior who does not want to hear about "
            "problems. Standing in front of Dr. Murakami's large oak desk enduring the old man's "
            "stare, he manages only: 'Yes sir' -- and then has to work out what that actually "
            "means."
        ),
        "background": (
            "Hamilton runs the SCREECH program and reports to Dr. Murakami. When his lead engineer "
            "-- the freelancer he brought in himself -- developed what he called an attack of "
            "conscience about the Ravener field trials in the Barrens, he took the problem upstairs "
            "and was told to find the motivation. With Murakami's blessing, black-ops funds were "
            "approved: outside operatives shadowed Finger and dug up his past, and in three days "
            "they had Jessica Ravenwing in a halfway house and confirmation that she was the "
            "engineer's daughter. Hamilton contracted The Eliminators to take her and keep her "
            "safely on ice until the project was done. His private conclusion afterwards: 'perhaps "
            "they were both expendable.'"
        ),
        "notes": (
            "No stat block; never met on screen, and the runners are unlikely to learn his name at "
            "all -- a Lone Star or Ares contact who is prepared to talk will name the Eliminators "
            "and 'Finger' and go no further. He is what makes this a corporate crime rather than a "
            "gang snatch, and the obvious target of any follow-up. Note the deadline that drives "
            "everything: SCREECH must debut to the Defense Department on the 15th, which is why "
            "there is a window and why Joey wants the job done in 48 hours."
        ),
    },
    {
        "name": "Dr. Murakami",
        "role": "Hamilton's superior at Ares, who approved the black-ops funds without ever saying what for",
        "archetype": "Corporate Executive",
        "title": "Senior director, Ares Macrotechnology weapons research, Seattle",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Ares Macrotechnology",
        "connection": 4,
        "description": (
            "An old man behind a large oak desk who lets a subordinate stand and endure his stare "
            "while he decides how much to say. What he says is nine words: 'I suggest you take "
            "matters to ensure that he does finish, and on time. Find the motivation.' Nothing in "
            "that sentence describes a kidnapping, which is exactly the point."
        ),
        "background": (
            "Murakami is the level of Ares management at which SCREECH is a schedule rather than a "
            "weapon and the lead engineer is a resource rather than a man. He approved the funds "
            "for the black operation that found Jessica Ravenwing, and he gave the order that led "
            "to her abduction in a form that commits him to nothing. He has no on-screen "
            "appearance beyond that one exchange."
        ),
        "notes": (
            "No stat block; pure background, and the module's structural echo of Dr. Fredericks "
            "giving Brian Wallace a deniable instruction in SRM 00-02. He matters for a GM "
            "extending the plot: Finger is about to walk out of Ares with everything he knows about "
            "SCREECH and about the Ravener field trials in the Barrens, and the person who has to "
            "explain that to the Defense Department on the 15th is Murakami."
        ),
    },
    {
        "name": "Sister Miriam",
        "role": "Runs the Church of the Undying Light halfway house; cooperative, overworked, and fond of Jessica",
        "archetype": "Cleric",
        "title": "Sister, Church of the Undying Light; warden of the halfway house",
        "race": "Human",
        "gender": "Female",
        "organization": "Church of the Undying Light",
        "connection": 2,
        "description": (
            "Found baking cookies for a donation drive when the runners arrive. She has worked with "
            "a great many people before, and she really liked Jessica, who used to help out with "
            "the chores around the house -- now that she is gone Sister Miriam has to find another "
            "little helper. Showing the team to Jessica's room and her things, she talks about the "
            "repairs the house needs: the electrical outlets, the leaks in the roof, how much "
            "harder the upkeep gets each day without girls like Jessica around."
        ),
        "background": (
            "Nothing more is given about her than the shelter and the work. She asks nobody for a "
            "donation to earn her cooperation -- mentioning that they are investigating Jessica's "
            "abduction is enough -- and she gives the runners full access to the girl's quarters "
            "and her box of belongings without hesitation."
        ),
        "notes": (
            "No stat block. Practical value: access to Jessica's room and her box, which contains "
            "hair in a hairbrush and other DNA samples plus a locket, a doll and an old blanket "
            "-- ritual sorcery material, though the warehouse ward defeats it. She can also point "
            "the team at the other residents, whose accounts are wildly imaginative and almost "
            "worthless. The module attaches a point of team Karma to characters who state they will "
            "return after the run, annotate a week on their calendars and actually spend it fixing "
            "her outlets and her roof -- one of the few unambiguously kind things a Season 0 "
            "character can be rewarded for."
        ),
        "contact_skills": ["Street kids and the shelter network", "Local word of mouth"],
    },
    {
        "name": "Burpie",
        "role": "Halloweener who saw Jessica carried into the warehouse and is now hiding in his brother's coffee shop",
        "archetype": "Ganger",
        "title": "Halloweeners member, in hiding",
        "race": "Human",
        "gender": "Male",
        "organization": "Halloweeners",
        "connection": 2,
        "description": (
            "A little high strung, and with reason: he knows he is in well over his head after "
            "seeing something he should not have seen, and he knows it is only a matter of time "
            "before somebody comes looking to shut him up permanently. He has been sitting in the "
            "back office of his brother's coffee shop in Renton waiting for it to happen. Handled "
            "badly he bolts; handled well he talks freely, and he can draw the warehouse layout and "
            "mark where he was watching from."
        ),
        "background": (
            "Burpie was casing the PRC warehouse for a possible Halloweener hit. The gang believed "
            "Lone Star's contract with PRC meant confiscated SMGs and assault rifles were being "
            "melted down there -- guns already marked destroyed, so the Star would no longer hold "
            "the ballistics records. It was a bad tip; the small arms go straight to the smelters. "
            "While he was hiding on the catwalks a group of large men came in carrying a big blue "
            "sack, closed the doors behind them, dumped it on the ground and opened it to reveal an "
            "attractive Native American girl with jet black hair, bound and gagged. Two of them "
            "dragged her into the women's locker room; when they came out without her a third went "
            "in, and Burpie heard chanting. He decided it was time to leave, knocked over a bin of "
            "parts slated for recycling, and made the door as gunfire opened up behind him -- he "
            "felt splinters off the door framing hit his back. He reached his bike and got away, "
            "and is fairly sure he was not identified, though they may have seen his gang colors."
        ),
        "notes": (
            "No stat block. Joey has already done the footwork that names him, and the Matrix "
            "paydata table produces him at 6 successes for an extra 100 nuyen; finding him at the "
            "coffee shop takes gang or street contacts. Everything he gives up is in his background "
            "plus the warehouse layout and the position he watched from. If the team makes a good "
            "impression on him, he and Eddie can raise the Halloweeners to hit the warehouse as a "
            "diversion, or to come and pull the team out afterwards -- the single most useful thing "
            "a face can achieve in this half of the adventure. If they blow the encounter he slips "
            "away and they need another route to the warehouse (the encoded address on the Or'zet "
            "flyer, or ritual sorcery)."
        ),
        "contact_skills": ["Halloweeners gang business", "Tacoma warehouse district"],
    },
    {
        "name": "Eddie (Eddie's Coffee Shop)",
        "role": "Ex-Halloweener coffee shop owner in Renton sheltering his younger brother Burpie",
        "archetype": "Business Owner",
        "title": "Owner, Eddie's Coffee Shop, Renton; former Halloweener",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": (
            "A man with a cigar and a long scar down his left cheek who greets new customers with "
            "'Hey, the street's free but a cup of coffee is five nuyen -- drink or scram!' He hates "
            "everyone equally and verbally abuses anyone who comes in looking out of place, with a "
            "distinct dislike of metahumans of any metatype and of pretty-boy face types. The "
            "module's own summary: nothing has the social graces of a former "
            "Halloweener-turned-coffee-shop-owner."
        ),
        "background": (
            "A former Halloweener who got out and bought a greasy spoon in Renton, and who has "
            "enough problems of his own with the local authorities without his little brother "
            "bringing a corporate hit team down on the place. Burpie is his younger brother and has "
            "been hiding in the back office; Eddie is watching out for him and is not inclined to "
            "hand him to strangers."
        ),
        "notes": (
            "Filed under a disambiguated name -- an unrelated Eddie already exists (Wake of the "
            "Comet). No stat block; run him and four patrons as ordinary tough humans if it comes "
            "to a brawl. Getting past him: anyone who is a former Halloweener is known and treated "
            "as family; a character with Charisma 3 or less who looks like a fighter and has a "
            "Halloweener contact is also welcome; anyone else with proper street etiquette is "
            "tolerated. More than three runners in the shop at once makes him wary at once -- "
            "obviously the team Burpie told him about. Gain his trust and 200 nuyen goes a long way, "
            "and he shows them the back office. Fail and Eddie plus four patrons try to thump the "
            "team and strip them of gear, credsticks and clothing for the local fence. Handled "
            "well, he and Burpie can bring the Halloweeners in on the warehouse."
        ),
        "contact_skills": ["Renton street scene", "Halloweeners, past and present"],
    },
    {
        "name": "Hammer-Slammer",
        "role": "Ares decker watching the Matrix for anyone asking about Jessica Ravenwing, with no interest in subtlety",
        "archetype": "Decker",
        "title": "Contract decker, Ares Macrotechnology (Seattle)",
        "race": "Human",
        "gender": "Male",
        "organization": "Ares Macrotechnology",
        "connection": 3,
        "description": (
            "Encountered only in the Matrix, and only by people who went looking where they were "
            "told not to. Joey's warning is explicit: Ares has a very good decker by the name of "
            "Hammer-Slammer out there making sure people do not ask too many questions, and "
            "searching could be dangerous. His tactics do not use much subtlety -- he goes for "
            "blood, tries to establish name, identity and location, and puts Black IC on the deck "
            "of anyone who cannot get away."
        ),
        "background": (
            "Part of the same black-ops budget that found Jessica in the first place. He has smart "
            "frames and tracers sitting on the three places anyone hunting her would naturally go: "
            "the Ares site, the girl's SIN records, and the shelter's system. Anyone entering one "
            "of those areas rolls an opposed Sleaze test against his Sensors at rating 9, and if "
            "they are detected he comes after them personally."
        ),
        "notes": (
            "Matrix stats: B3 Q5 S2 C2 I6 W4, Ess 2.5, Reaction 5, Init 9+3D6 (12+4D6 on pure DNI), "
            "Hacking Pool 4 (9), Karma 2, Task 2, Pro 3/Trained. Computer 6 (Decking 8, Programming "
            "7), Etiquette 3 (Corporate 4, Matrix 5). Attack-8 and Black IC (Killer 8S). Datajack, "
            "Encephalon 2, Math SPU 3. Renraku Kraftwerk-8 (MPCP-8, Hardening 4, Response Increase "
            "2) with rating 4-8 programs. He is only ever met in the Matrix, so nothing else is "
            "needed. Handling a decker CONTACT sent to do the team's dirty work: they run into him "
            "automatically -- if the contact is a generic template or a Level 1 contact, roll two "
            "quick contests at rating 6 against rating 9, TN 4; win and the team gets useful "
            "information, lose and they lose the contact to cybercombat and a deck full of Black "
            "IC. The safe route is the Computer (5) paydata table: 2 successes names the "
            "Eliminators, 4 places one of them in Tacoma by the warehouse district and docks, 6 "
            "(plus 100 nuyen) points at a Halloweener called Burpie."
        ),
        "contact_skills": ["Ares Matrix security", "Tracing and intrusion countermeasures"],
    },
    {
        "name": "White-out",
        "role": "Leader of the Eliminators; former corporate security specialist running the warehouse from the office",
        "archetype": "Shadowrunner",
        "title": "Team leader, The Eliminators",
        "race": "Human",
        "gender": "Male",
        "organization": "The Eliminators",
        "connection": 4,
        "description": (
            "A former corporate security director who knows all the tricks, and who runs the "
            "operation the way he used to run the other side of it: from the upstairs office, "
            "watching the camera feeds, with the rest of the team dispersed to cover every approach "
            "and a sniper on the catwalk. Alphaware throughout, an armor jacket, a Colt M-23 and an "
            "Ingram Valiant, and low-light goggles. Street rumor knows him only as the leader who "
            "used to be a corp security man."
        ),
        "background": (
            "The Eliminators have worked the Seattle shadows for years on wetwork and high-profile "
            "extractions, taking the jobs nobody else likes to touch, and White-out assembled a "
            "roster from people who know their targets' routines: former special ops, former Lone "
            "Star SWAT, former counter-intelligence. Their trademark is not the snatch, it is the "
            "keeping -- a rented site whose owner is compensated to close, their own cameras, a "
            "week of supplies, a warded room, and the patience to wait for a phone call."
        ),
        "notes": (
            "Stats: B6(7) Q4(6) S5(7) C4 I5 W4, Ess 0.42, Reaction 4(8), Init 8+3D6, Combat Pool 7, "
            "Karma 4, Pro 4/Professional. Athletics 5, Assault Rifles 5, Heavy Weapons 5, Unarmed "
            "5, Stealth 4, Edged Weapons 3 (Knife 5), Intimidation 3, Etiquette 3 (Corporate 5, "
            "Street 4). Cyber, all alphaware: plastic bone lacing, cybereyes (thermo, flare comp), "
            "muscle replacement 2, Smartlink II, Wired Reflexes 2. Armor jacket 5/3. Colt M-23 "
            "assault rifle (8M), Ingram Valiant LMG (7S), survival knife (9L). Survival kit, "
            "low-light goggles, microtransceiver with encryption 4. Normally stationed in the "
            "office watching the cameras. Note the module prints Burn-bag's block identically -- "
            "the two differ only in their goggles and their background."
        ),
    },
    {
        "name": "Shredder",
        "role": "Eliminators sniper on the catwalks; former Lone Star SWAT",
        "archetype": "Shadowrunner",
        "title": "The Eliminators; former Lone Star SWAT",
        "race": "Ork",
        "gender": "Male",
        "organization": "The Eliminators",
        "connection": 3,
        "description": (
            "An ork who used to kick doors for Lone Star SWAT and now shoots people from a corner "
            "of the catwalks with a Ranger-Arms SM-3. Small Unit Tactics 6 and Stealth 4 "
            "(Sneaking 6) say what he brought with him from the Star; the synaptic accelerator and "
            "the reaction enhancers say what the Eliminators paid to add."
        ),
        "background": (
            "Former Lone Star SWAT, and the reason the module warns runners to be careful which "
            "Star contacts they trust: the ties between Ares and Lone Star run both ways, and some "
            "of the people who used to serve warrants are now serving Johnsons. He handles the "
            "long-range work and the tactical planning for the team's static positions."
        ),
        "notes": (
            "Stats: B6 Q5 S7 C3 I4 W5, Ess 4.96, Reaction 4(6), Init 6+3D6, Combat Pool 7, Karma 4, "
            "Pro 4/Professional. Athletics 6, Rifles 7, Pistols 4, Clubs 4, Demolitions 2, Small "
            "Unit Tactics 6, Stealth 4 (Sneaking 6), Unarmed 5. Cyber, all alphaware: cybereyes "
            "(electronic magnification 3, low light, thermo), Smartlink II, reaction enhancers 2. "
            "Bioware: synaptic accelerator. Armor jacket 5/3. Colt Manhunter (9M), Ranger-Arms SM-3 "
            "sniper rifle (14S). Microtransceiver with encryption 4. Usually stationed on the upper "
            "catwalks near a corner as the overwatch -- a 14S rifle in a lit yard with almost no "
            "shadow is the single deadliest thing about the warehouse approach, and dealing with "
            "him first is what separates a clean rescue from a firefight."
        ),
    },
    {
        "name": "Eraser",
        "role": "Eliminators covert operations specialist and talker; the team's face and infiltrator",
        "archetype": "Shadowrunner",
        "title": "The Eliminators; former covert operations specialist",
        "race": "Elf",
        "gender": "Male",
        "organization": "The Eliminators",
        "connection": 3,
        "description": (
            "The one Eliminator built for getting in rather than shooting his way through: an elf "
            "with Etiquette 5 (Government 7), Negotiations 5 (Fast Talking 7), Stealth 6, and "
            "alphaware cybereyes and cyberears that record everything he sees and hears. He carries "
            "an Ares Predator III and a stun baton and would much rather use neither."
        ),
        "background": (
            "A former covert operations specialist, and the member of the team whose old trade most "
            "obviously explains how the Eliminators arrange the things around their jobs -- the "
            "rented warehouse, the compensated owner, the professionally wiped shelter records, the "
            "witnesses who never quite saw anything. Nothing else about his history is given."
        ),
        "notes": (
            "Stats: B3 Q5 S3 C6 I4 W3, Ess 3.22, Reaction 4, Init 5+1D6 (2D6), Hacking Pool 6, Pro "
            "4/Professional. Athletics 6, Clubs 3 (Stun Baton 5), Etiquette 5 (Government 7), "
            "Negotiations 5 (Fast Talking 7), Pistols 4, Stealth 6, Unarmed 4 (Kick Attacks 6). "
            "Cyber: boosted reflexes 1, alpha cyberears (hearing dampener, amplification, "
            "recorder), alpha cybereyes (camera, flare comp, low light, thermo), alpha headware "
            "radio (rating 6, encryption 4), alpha Smartlink II. Armor jacket 5/3, Ares Predator "
            "III (9M), no other gear. He has the lowest Body on the team and the highest social "
            "skills; a party that opens with talking rather than shooting will be talking to him, "
            "and he is better at it than they are."
        ),
    },
    {
        "name": "Burn-bag",
        "role": "Eliminators heavy weapons man; former UCAS Army Green Beret",
        "archetype": "Shadowrunner",
        "title": "The Eliminators; former UCAS Army Green Beret",
        "race": "Human",
        "gender": "Male",
        "organization": "The Eliminators",
        "connection": 3,
        "description": (
            "The team's other assault rifle and light machine gun, cybered to the same specification "
            "as White-out -- plastic bone lacing, muscle replacement, Wired Reflexes 2, thermo "
            "cybereyes -- and equipped identically apart from the ultrasound goggles he carries in "
            "place of low-light. A Green Beret who took the shadows' pay rise."
        ),
        "background": (
            "Former UCAS Army Special Forces. Between him, White-out's corporate security "
            "background, Shredder's Lone Star SWAT service and Eraser's covert operations career, "
            "the Eliminators' reputation for knowing their targets' routines is entirely earned: "
            "every one of them learned the trade from the side that writes the procedures."
        ),
        "notes": (
            "Stats (printed identically to White-out): B6(7) Q4(6) S5(7) C4 I5 W4, Ess 0.42, "
            "Reaction 4(8), Init 8+3D6, Combat Pool 7, Karma 4, Pro 4/Professional. Athletics 5, "
            "Assault Rifles 5, Heavy Weapons 5, Unarmed 5, Stealth 4, Edged Weapons 3 (Knife 5), "
            "Intimidation 3, Etiquette 3 (Corporate 5, Street 4). Cyber, all alphaware: plastic "
            "bone lacing, cybereyes (thermo, flare comp), muscle replacement 2, Smartlink II, Wired "
            "Reflexes 2. Armor jacket 5/3, Colt M-23 (8M), Ingram Valiant LMG (7S), survival knife "
            "(9L), survival kit, ULTRASOUND goggles (the one difference from White-out), "
            "microtransceiver with encryption 4. Ultrasound goggles matter: an invisible or "
            "concealed runner who has planned around thermographic and low-light vision has not "
            "planned around him."
        ),
    },
    {
        "name": "Degauss",
        "role": "Eliminators decker turned close-combat cyberarm fighter; carrying no deck on this job",
        "archetype": "Shadowrunner",
        "title": "The Eliminators; former corporate security decker",
        "race": "Ork",
        "gender": "Male",
        "organization": "The Eliminators",
        "connection": 3,
        "description": (
            "An ork with an obvious cyberarm carrying a Smartlink II, strength enhancement and "
            "cyberspurs, who fights at Cyber Implant Combat 5 (Spurs 7) and reaches for an Ares "
            "Predator III only when he has to. On this job he is not a decker at all -- he left the "
            "cyberdeck behind, because the warehouse job is a stakeout with a phone call at the end "
            "of it."
        ),
        "background": (
            "A former corporate security decker, which is presumably how the Eliminators managed a "
            "wipe of the shelter's records so clean that only the girl's data was touched. On the "
            "warehouse detail he is muscle."
        ),
        "notes": (
            "Stats: B6 Q4 S5(7) C2 I5 W5, Ess 1.54, Reaction 4(6), Init 4+1D6 (6+2D6), Combat Pool "
            "7, Karma 4, Pro 4/Professional. Cyber Implant Combat 5 (Spurs 7), Pistols 5, Stealth "
            "4, Unarmed 4. Cyber: alpha headware radio (rating 5, encryption 4), obvious cyberlimb "
            "arm with Smartlink II, strength enhancement 2 and cyberspurs, alpha Wired Reflexes 1 "
            "with reflex trigger. Armor jacket 5/3, Ares Predator III (9M), microtransceiver with "
            "encryption 4. The module states explicitly that he does NOT have his cyberdeck with "
            "him and is not encountered in the Matrix during this adventure, so no Matrix stats are "
            "needed -- which also means the warehouse has no live decker defending it."
        ),
    },
    {
        "name": "Vaporize",
        "role": "Eliminators hermetic magician; wards the holding room and opens fights with Decrease Charisma",
        "archetype": "Mage",
        "title": "The Eliminators; former counter-intelligence magician",
        "race": "Human",
        "gender": "Male",
        "organization": "The Eliminators",
        "connection": 4,
        "description": (
            "A hermetic magician and grade 1 initiate with Shielding, in an armor jacket, who is "
            "the reason the divination failed and the reason Burpie heard chanting from the "
            "women's locker room after the girl was carried in. He opens against a team by trying "
            "to neutralize whichever runners are least charismatic with Decrease Charisma, then "
            "goes to Chaotic World and his elementals."
        ),
        "background": (
            "A former counter-intelligence magician. Between his ward on the shower area and the "
            "Snake Lodge's failure to find Jessica by divination or ritual tracking, he is the "
            "single most important member of the team to the plot -- and the most obvious suspect "
            "for what happened to the Lodge, except that the astral signature there resembles "
            "Psychic Manifestation, which is neither shamanic nor hermetic."
        ),
        "notes": (
            "Stats: B4 Q5 S3 C5 I5 W6, Ess 6, Magic 7 (Initiate Grade 1), Reaction 5, Init 5+1D6, "
            "Spellcasting Pool 6, Pro 4/Professional. Metamagic: Shielding. Sorcery 6, Conjuring 6. "
            "Spells: Chaotic World 7, Heal 6, Improved Invisibility 6, Increase Reflexes +2 5, "
            "Stealth 6, Decrease Charisma 7. Armor jacket 5/3, microtransceiver with encryption 4. "
            "On call: a Force 4 fire elemental with 3 services, a Force 5 earth elemental with 3 "
            "services and a Force 6 air elemental with 2 services. Tactics: Decrease Charisma "
            "first on the non-charismatic runners, then Chaotic World, elementals, and Improved "
            "Invisibility to break contact. The ward covers the entire bathroom and shower area and "
            "is what defeats every attempt to locate Jessica at range."
        ),
    },
]

ORG_UPDATES = {
    "Ares Macrotechnology": {
        "notes_append": (
            "SRM 00-04 A Fork in Fate's Path: Ares runs a Seattle weapons testing program with two "
            "ugly features. The first is field trials -- the initial production run of the new "
            "Ravener SMGs was tested on homeless people in the Barrens, which the company's own "
            "lead engineer heard about and objected to. The second is the SCREECH sonic disruptor "
            "rifle, due to debut to the UCAS Defense Department on the 15th, whose freelance lead "
            "engineer 'Finger' had solved the power coupling problem and had only the wave pulse "
            "regulator left when he started asking questions. Project director Dr. Hamilton, told "
            "by his superior Dr. Murakami to 'find the motivation', spent approved black-ops funds "
            "on outside operatives who shadowed the engineer and dug up his past, located his "
            "hidden daughter Jessica Ravenwing in a halfway house within three days, and contracted "
            "the shadowrunner team The Eliminators to abduct her and keep her on ice until the "
            "project was delivered. Hamilton privately considers both father and daughter "
            "expendable afterwards. Ares also fields a contract decker, Hammer-Slammer, with smart "
            "frames and tracers on the corporate site, the girl's SIN records and the shelter's "
            "system, who traces and attacks anyone who comes looking. Because of the close ties "
            "between Ares and Lone Star, there is a 1 in 3 chance that any Lone Star or Ares "
            "contact asked about the girl, the shelter, Hammer-Slammer or the Eliminators is tapped "
            "-- a tapped Level 1 contact gives nothing and is dismissed or transferred by Internal "
            "Affairs, effectively neutralized for the run."
        ),
        "enemies_add": ["Snake Lodge"],
    },
    "Lone Star Security": {
        "notes_append": (
            "SRM 00-04 A Fork in Fate's Path: two threads. First, the Star has contracted the Puget "
            "Recycling Cooperative to destroy small arms recovered from the street and released "
            "after processing, because evidence lockers are only so large -- the Halloweeners got "
            "the impression the guns were being melted at PRC's Tacoma warehouse and planned to "
            "raid it for SMGs and assault rifles already marked destroyed (and therefore no longer "
            "on file for ballistics), but the small arms actually go straight to the smelters. "
            "Second, the close ties between Ares and Lone Star make Star contacts unsafe for this "
            "run: 1 in 3 are tapped, and Lone Star/Corporate Relations is on alert for any query "
            "about Ares employees. Lone Star also investigated the Snake Lodge massacre -- no signs "
            "of entry, no reported disturbance, every member brutally murdered with blood flung "
            "across the walls, ceiling and floor, no leads. Tipped off about PRC and the "
            "Eliminators, the Star impounds the warehouse within days, finds corroborating evidence "
            "of previous activities and prosecutes PRC officials."
        ),
    },
    "Halloweeners": {
        "notes_append": (
            "SRM 00-04 A Fork in Fate's Path: the gang planned to hit the Puget Recycling "
            "Cooperative warehouse in Tacoma, believing that Lone Star's confiscated small arms "
            "were being melted down there and could be recovered and repaired without any "
            "ballistics record surviving. The tip was wrong -- the guns go straight to the smelters "
            "-- and the member sent to case the place, 'Burpie', instead saw the Eliminators carry "
            "a bound and gagged girl in inside a blue sack, was shot at, and has been hiding in his "
            "older brother Eddie's coffee shop in Renton ever since, expecting to be silenced. "
            "Eddie is himself a former Halloweener; ex-members are treated as family in his shop. "
            "Handled well, the brothers will raise the gang to hit the warehouse as a diversion for "
            "the runners, or to pull them out afterwards."
        ),
        "enemies_add": ["The Eliminators"],
    },
    "DocWagon": {
        "notes_append": (
            "SRM 00-04 A Fork in Fate's Path: the party chatter Rolando finds so boring is about "
            "the latest terrorist attacks against DocWagon -- and Rolando, listening, concludes "
            "that they are not terrorism at all but the opening of some kind of shadow war being "
            "waged against the medical conglomerate. His read is commercial rather than moral: once "
            "the conflict reaches critical mass DocWagon will have to respond without drawing "
            "public notice, and that means hiring shadowrunners, which means work for a fixer. A "
            "deliberate campaign seed left standing at the end of Season 0."
        ),
    },
    "Humanis Policlub": {
        "notes_append": (
            "SRM 00-04 A Fork in Fate's Path: an Or'zet-language flyer dropped behind a floorboard "
            "at the Snake Lodge calls for uniting the Ork Underground and rising up against its "
            "oppressors and the Humanis Policlub, and carries a password granting entry to a new "
            "secret part of the Underground where a militant policlub for orks and trolls is "
            "forming. Ork or troll characters who read it (Or'zet, TN 5) may opt to join that "
            "organization after the adventure. Neither the group nor its leadership is named."
        ),
    },
}

LOC_UPDATES = {
    "The Ork Underground": {
        "notes_append": (
            "SRM 00-04 A Fork in Fate's Path: a single-page flyer written in Or'zet turns up behind "
            "a floorboard at the murdered Snake Lodge, with the name 'Ravenwing' and an encoded "
            "address handwritten in the margin. Read at Or'zet TN 5 it yields, by degrees: that it "
            "concerns the Ork Underground (1 success); something about a brotherhood in the "
            "Underground and killing mankind (2); and at 3 successes the whole of it -- a call to "
            "unite the Ork Underground and rise against its oppressors and the Humanis Policlub, "
            "plus a password granting entry to a new secret part of the Underground where a "
            "militant policlub for orks and trolls is forming. Ork or troll characters may opt to "
            "join it after the adventure. The module names neither the group nor its leaders and "
            "never explains how the flyer came to be at the Lodge, which makes it the most "
            "deliberate loose thread in Season 0."
        ),
    },
}

NPC_UPDATES = {
    "Rolando": {
        "background_append": (
            "SRM 00-04 A Fork in Fate's Path: Rolando got his start mostly through 'family' "
            "connections and to this day handles the more disreputable jobs in the shadows of "
            "Seattle; his ego is exceeded only by his greed for money and power. He has long "
            "dreamed of appearing in a trideo feature, particularly a remake of the gangster films "
            "of the late 20th and early 21st centuries. At a Seattle party -- with his two ork "
            "bodyguards trailing him in matching Heracles designer cocktail dresses fitted to "
            "conceal thigh holsters -- he levitated over the crowd to see who was at the center of "
            "it, recognized the HotSpot Communications owner Kevin Kirkpatrick by his short frame "
            "and oversized ears, and wove an illusion over the surrounding group so that they went "
            "on hearing Kirkpatrick talk while he walked the man into a corner. He proposed a "
            "partnership on the spot, both as an investor hoping for profits on the back end and as "
            "the fixer who knows exactly which runners he can dupe into doing the show."
        ),
        "notes_append": (
            "SRM 00-04 A Fork in Fate's Path: Rolando makes the first of the module's two competing "
            "offers -- 10,000 nuyen each, 1,000 up front, no questions asked, job in two hours, "
            "'bring your gear, your heavy gear' -- and the greeting varies by history: cold call "
            "for runners who never met him, a pointed 'no hard feelings, eh chummer?' for those who "
            "blocked him at Freeway Park, and 'I thought of you first!' for anyone who took him as "
            "a contact in SRM 00-01. Negotiation adds 1,000 nuyen to the advance per net success to "
            "a maximum of 5,000; the 10,000 total is fixed. What he sells is the team itself: he "
            "bought into RealRunners! as a major investor, stands to make a million nuyen from the "
            "first episode, and arranged for gang members to be murdered through his underworld "
            "contacts and the blame planted on the runners so that the gang would ambush them on "
            "camera. Because the runners are SINless he can sell their images and experiences with "
            "no legal recourse available to them. Turned down for Joey's job, he calls back "
            "screaming: 'YOU USELESS FRAGGERS! YOU'LL NEVER WORK IN THIS TOWN AGAIN! I SWEAR BY MY "
            "ALMIGHTY POWER FOCUS THAT EACH AND EVERY ONE OF YOU WILL HAVE HIS HEAD ON A PIKE "
            "BEFORE I'M THROUGH WITH YOU!' Joeli Gibson's assessment, from a run they did together "
            "once: a dangerous guy, always talking about his power focus and how big it is and how "
            "powerful it is, and the whole thing was pretty ridiculous."
        ),
    },
    "Joeli Gibson": {
        "notes_append": (
            "SRM 00-04 A Fork in Fate's Path: Joey makes the second and better offer, from a plush "
            "leather armchair aboard her yacht at Pier 37 -- 500 nuyen each up front and 1,500 on "
            "completion, non-negotiable, with only 1,000 for herself to cover expenses because the "
            "client is an old friend she would help for nothing if she could afford to. She warns "
            "the team off Rolando outright ('I always got a really bad feeling about him... I did a "
            "run with him once a while ago; it was pretty ridiculous'), admits she has used the "
            "trusted-fixer setup herself in the past and is not using it now, and hands over "
            "everything she has: do not run Matrix searches because of the Ares decker "
            "Hammer-Slammer; the girl was last seen at the Church of the Undying Light halfway "
            "house; a divination failed and the mages who tried it were murdered; Ares and Lone "
            "Star are close, so only ask Star contacts you genuinely trust; a Halloweener called "
            "Burpie may have seen something; get it done inside 48 hours because the Johnson has a "
            "window. Asked whether killing is acceptable, she would prefer they did not -- she has "
            "a thing about the taking of innocent life -- but she is not stupid: 'Sometimes it's "
            "just part of the job chummer.' Her closing line is the reason to take her jobs: 'I "
            "have a pretty long memory and I take care of people who take care of me.'"
        ),
        "contact_skills_add": ["Introductions to independent weapons specialists"],
    },
    "Betsy Ross": {
        "notes_append": (
            "SRM 00-04 A Fork in Fate's Path: still working for Rolando and, at a Seattle society "
            "party, ecstatic about it -- she and her sister bought matching Heracles designer "
            "cocktail dresses for the evening, fitted for their over-large frames with a little "
            "extra sway here and there to conceal the weapons holstered on their upper thighs. She "
            "takes Rolando's champagne flute when he decides to levitate over the crowd, and the "
            "pair watch his back while he pushes into the circle around Kevin Kirkpatrick. "
            "DISCREPANCY: this module's fiction calls the two bodyguards 'Betty and Betsy'; SRM "
            "00-01 Mission Briefing names them Betsy and Becky Ross, and that earlier naming is "
            "treated as canon here."
        ),
    },
    "Becky Ross": {
        "notes_append": (
            "SRM 00-04 A Fork in Fate's Path: still on Rolando's payroll and out with her sister in "
            "a matching Heracles cocktail dress at the party where he buys into RealRunners! "
            "DISCREPANCY: the module's opening fiction names Rolando's two female ork bodyguards "
            "'Betty and Betsy', which does not match the Betsy and Becky Ross of SRM 00-01 Mission "
            "Briefing; the earlier naming is treated as canon and this row is the same character."
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
Neither half of this adventure builds a host in the usual sense; the Matrix appears as a hazard
and as a legwork table.

### Ares watch net (Rolando's half: nothing; Joey's half: everything)

There is no host to crack. Instead, Hammer-Slammer has smart frames and tracers sitting on three
places anyone hunting Jessica Ravenwing will naturally go:

| Watched node | Effect |
| --- | --- |
| The Ares corporate site | Opposed Sleaze vs Sensors rating 9 |
| Jessica Ravenwing's SIN records | Opposed Sleaze vs Sensors rating 9 |
| The Church of the Undying Light shelter system | Opposed Sleaze vs Sensors rating 9 |

Detection means Hammer-Slammer comes personally, tries to establish name, identity and location,
and puts Black IC (Killer 8S) on the intruder's deck. A decker CONTACT sent in the team's place
meets him automatically: a generic template or Level 1 contact rolls two quick contests, rating 6
against rating 9 at TN 4 -- win for useful information, lose and the contact is gone.

The safe path is the quick-resolution legwork run (Mr. Johnson's Little Black Book), a Computer
(5) test:

| Successes | Result |
| --- | --- |
| 0 | Nothing useful -- but no mauling either |
| 2 | Ares has hired a runner team called the Eliminators, wetwork and extraction specialists |
| 4 | One of the Eliminators has been spotted in Tacoma by the warehouse district and the docks |
| 6 | (plus 100 nuyen) A Halloweener called "Burpie" may know something |

The shelter's own system is trivial to search and holds one fact: every trace of the girl has been
professionally wiped, with nothing else touched or mangled (Computer (4) to recognize the hand of
a professional).

### HotSpot Communications Studio A -- production systems (Area H)

Not a security host either, but the only Matrix objective in Rolando's half. The trideo processing
suite sits in Area H, past the concealed door and up the sloped exit hallway. A Computer (5) test
with a threshold of 3 (Hacking Pool may be used) locates and deletes -- or extracts, if the team
would rather keep it -- all footage of the runners in the warehouse. A threshold of 5 or better
also purges every record the production kept on them: weapons used, suspected cyberware, spells
cast.

Hardware worth taking: the Sony production equipment (fence 25,000 nuyen); the Sony TridMaster
4000, purpose-built to process digital video and computer-generated animation and explicitly NOT a
cyberdeck (fence 14,000 nuyen); and the Sony TrideoMax digital manipulation suite, equivalent to a
Spoof 5 / Read-Write 2 program and usable to manipulate live camera feeds or recordings -- treated
as a rating 5, multiplier 2 program needing 50 Mp of active memory plus 10 Mp per minute of
manipulated footage (retail 10,000 nuyen, fence only 500, no source code).
"""

NOT_BUILT = """
- **The 36 devil rats** of the corridor trap, the **three watchers** that mark the runners for the
  trap operator, and the **man on the switch** behind the wall -- creature and set-piece stats kept
  in the Studio A location notes.
- **The anthropomorph combat drones** (one for the finale, four more if it comes to a fight later)
  -- B15 Q6x5 S15 I4/8 R5, Init 5+2D6, hardened plating 9/9, Ingram Valiant LMG 7S, Spur 15M,
  immune to mana and Stun, not riggable, self-destructing for 10D at -2/m one full combat turn
  after exceeding a Deadly wound. Machines, kept in the play notes.
- **The three Snake shamans** retained by HotSpot as the medical team and as Kirkpatrick's escape
  -- Grade 1 initiates with Shielding, Chaotic World 8, Heal 8, Treat 8, Trid Phantasm 8, Improved
  Invisibility 6, Stealth 8, Increase Willpower 8, +2 dice for detection, health and illusion
  spells, +2 for conjuring city spirits, -1 for anything cast in combat, and a Force 6 city spirit
  with 2 services on standby.
- **The gangers** (14, 21 or 28 by table rating) whom Rolando had framed for the murder of their
  own, and the **murdered gang members**, the **planted evidence** and the **located witnesses**
  -- all unnamed; the gang itself is never named.
- **Kirkpatrick's two-meter elf driver** and the **HotSpot technicians** working on the marketing
  prototypes, the damaged drones and the final edit.
- **The outside operatives** Ares hired to shadow Finger and dig up his past, and the **large men**
  Burpie saw carry the blue sack -- presumed Eliminators, never confirmed.
- **Whatever killed the Snake Lodge** -- no name, no stats, no explanation; an astral signature
  "closely related to Psychic Manifestation" and a style of magic that is neither shamanic nor
  hermetic. The module's largest deliberate loose end.
- **The militant ork and troll policlub** forming in a new secret part of the Ork Underground,
  named on the Or'zet flyer only as a brotherhood; its password is on the flyer and ork or troll
  characters may join after the adventure.
- **The Mitsubishi Nightsky**, Heracles cocktail dresses, Sony TridMaster 4000 and TrideoMax,
  Renraku Kraftwerk-8, Ingram Valiant, Ranger-Arms SM-3, Colt M-23, Colt Manhunter, Ares Predator
  III, Browning Max-Power, Colt American L36 -- gear and brand name-drops.
- **Eye on Seattle, Good Morning, Seattle** and **Puget Sound Nightlife** -- HotSpot's existing
  shows, kept in the org row.
- **The Table Rating chart** (TR 1 Green through 6 Prime Runner by average career Good Karma),
  reprinted here and used to scale the ganger encounter and the drones.
"""

PLAY_NOTES = """
- Run the choice properly. Both offers arrive within minutes, the team may take only ONE, the
  decision is by majority with ties broken by the higher total Karma on each side, and the moment
  they commit the other job closes. Do not run both halves at one table, and do not let anyone
  replay the module to see the other path. Players who dissent may swap to a different existing
  Missions character or a standard template (with character amnesty applying) but may not build
  someone new on the spot.
- The whole module is a lesson about what a job costs. Rolando's half pays five times as much and
  ends with the team's faces on lunch boxes and their Notoriety up; Joey's half pays 2,000 nuyen
  and ends with a weapons designer who owes them a favor for the rest of their careers. Neither is
  the "right" answer -- but make sure the players feel the trade after the fact.
- Rolando's half is a set-piece crawl, not a puzzle: the door, the rats, the gangers, the drone.
  The Grand Finale is explicitly cinematic. Use GM fiat rather than the dice, let the drone drop
  at least one character, ignore magic-loss and cyberware-damage tests because this is a controlled
  shoot, and leave one runner standing for the heroic last blow. The drone ignores anyone who takes
  a Deadly wound and then stays down. For Veteran tables and up, use real dice and real
  consequences.
- The three watchers in the corridor are the one place skill beats scripting: destroy all three
  before they report and the rat trap never fires. Reward that.
- Perception (8) on the way out is the hinge of the whole half. Miss the storage room and the team
  walks away as minor celebrities: +10 Street Cred, +2 Notoriety for anyone who used lethal force
  on the "innocents", +1 for merely associating with those who did. Find it and the choice is
  theirs -- purge Area H (Computer (5), threshold 3 for the footage, 5 for every record of their
  gear and spells) or start a fight with Kirkpatrick they are not equipped to win. Coming back
  later is the sensible answer: no Kirkpatrick, no shamans, no Rolando, just technicians who
  surrender and drones that cannot follow through a single-hung door.
- Joey's half is a legwork adventure with a hard assault at the end, and it has three independent
  routes to the warehouse -- Burpie at Eddie's, the encoded Or'zet flyer at the Snake Lodge, and
  ritual sorcery from the hairbrush (which the ward will defeat, so it is the route that teaches a
  lesson). Make sure the team has at least one of them by the halfway mark, about two hours in.
- Warn them off the Matrix through Joey, then let Hammer-Slammer be real if they ignore her. Same
  for Lone Star contacts: roll the 1 in 3, and if a Level 1 contact is tapped, take the contact
  away for the rest of the run rather than killing them.
- Eddie's Coffee Shop is a social encounter with a fight attached. Three or more visible runners
  makes him wary immediately; 200 nuyen and street manners get them the back office; failure gets
  Eddie and four patrons trying to strip them. Play the metahuman and pretty-boy prejudice
  honestly -- it is the module's point that the wrong face in the doorway costs the team a lead.
- The warehouse yard is deliberately lit to leave nowhere to hide, and Shredder is on the catwalk
  with a 14S sniper rifle. Six professional-rating-4 opponents will kill a starting team in a
  stand-up fight; the intended answers are the man-door, a Halloweener diversion arranged through
  Burpie and Eddie, and getting Jessica out rather than clearing the building.
- Karma. Rolando's half: 2 for stopping or destroying Kirkpatrick's plan, 1 for completing the
  mission. Joey's half: 2 for saving Jessica without injury, 1 for actually going back and doing a
  week of repairs at Sister Miriam's shelter, 1 for defeating all the Eliminators, 1 for tipping
  off Lone Star or the media about PRC and the crusher. Individual Karma is capped at 3 either way.
"""
