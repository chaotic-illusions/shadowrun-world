# Bottled Demon (FASA 7305, 1990) -- campaign order #7. Redmond / Puyallup / Tacoma, January 2051
# (news handouts dated January 15). Note: the book spells the elven hitman both "Blackwing" (cast
# page) and "Bloodwing" (most of the text); the cast-page spelling is used, alias noted.
# Source text: docs/Adventures/text/Shadowrun 1e - Bottled Demon {FASA7305}.txt (62 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "Bottled Demon"
ORDER = 7
SOURCE = "Shadowrun 1e - Bottled Demon {FASA7305}.pdf, pp. 4-62"
YEAR = "2051 (January)"

SYNOPSIS = """
**Topal** (Pietr Fiegeton), a chubby Raven-shaman talismonger from the Sophocles neighborhood of
Redmond, waddles up to the runners at **Yoshiro's** with a courier case chained to his wrist and
5,000 nuyen each for three hours' bodyguard work. Three days earlier his friend **Simon Templeman**
staggered into The Guiding Hand with the case, aged thirty years in a month, and died. Inside is
the idol: thirty centimeters of deep-red stone, demon-shaped, glowing eyes, a pinkish globe clutched
to its chest -- a Power Focus rating 12 that anyone can use, that eats its user, and that burned
Topal's shop down. He wants to sell it to elven scholars at **Black's Junk Yard** at 4 a.m.

The scholars are dead in room 616 of the Snohomish Sheraton, three precise shots by the elven
assassin **Blackwing**, hired by an unnamed Tir Tairngire noble to fetch the idol quietly. **Captain
Grissim** of Lone Star, who has chased Blackwing since Los Angeles, hits the junkyard with a
Citymaster, ten troopers and two Yellowjackets. Topal cuffs the case to a runner and dies in the
crossfire; the runners flee with the idol, Lone Star's Class A felons on the evening news, snitched
on by squatters, shunned by contacts, hunted by Blackwing, and ambushed by Topal's grieving
**Children of Sophocles**, who believe Blackwing's rumor that the team iced its employer.

**Trixy**, an ancient Dog shaman who has been dreaming of the red stone, tells them only a Dragon
can destroy it and sends them to **Geyswain**, the young Western dragon who runs **Lochlann
Investments** from a desert lair atop the Lochlann Center. Geyswain wants it, takes it (bake the
runners in his lair if they refuse), and is consumed by it within a day: 150 employees dead, the
security center a charnel house, spirits swarming the astral, Blackwing's team broken. **Arleesh**,
a Great Feathered Serpent ten months awake, collects the runners at the Tacoma Charity Hospital,
teaches them the difference between dragons, and uses them to wear Geyswain down while she, invisible,
saves her strength to implode the idol. Grissim's cordon watches from the roof and does not fire.
Blackwing buys the inert idol for Tir Tairngire and walks on a diplomatic pass. Grissim is not pleased.
"""

TIMELINE = """
- **Three days before** -- Templeman dies in The Guiding Hand; cremated; Topal experiments, the
  dreams begin, the shop burns. **Night before** -- Topal finds elven buyers and calls for muscle;
  Blackwing kills the three scholars at the Snohomish Sheraton; Grissim's joygirl lark spots him.
- **Day 1** -- mid-afternoon at Yoshiro's; 3:00 a.m. convoy through Asphalt Devil turf; 4:00 a.m.
  Black's Junk Yard raid; Topal dies. Rest until **6:00 p.m.**: a contact's warning, Lone Star at the
  door, the team on the evening news. The Children of Sophocles, Lone Star Country, Trixy.
- **Day 2** -- Geyswain at Lochlann; the runners wake 24 hours later in Tacoma Charity Hospital.
  Arleesh; Stuffer Shack drive-through; **1:00 a.m.** on the Tacoma docks; the abandoned storefront;
  Lochlann in the rain; Grissim's cordon; the implosion. Reputations mend in about a week.
"""

ORGS = [
    {
        "name": "Lochlann Investments",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Lochlann Center, Tacoma, north of the docks on the shore of Lake Washington",
        "summary": "Geyswain's decade-old real estate corp holding huge undeveloped tracts of the Barrens; 150 dead after the idol",
        "description": (
            "A decade-old real estate acquisition and management corporation (Lochlann Real Estate) "
            "owned and administered by the low-profile Western dragon Geyswain, who unlike most dragon "
            "CEOs keeps a claw in the daily business from his ecologically engineered lair on the top "
            "floors of the Lochlann Center. Spurred by the dragon's capital it became a major player in "
            "local real estate with extensive holdings in Redmond, Puyallup and Tacoma -- most of "
            "which stay off the market and undeveloped. Perhaps he knows something. A moderate internal "
            "security force, periodically retrained at the local Knight Errant facility."
        ),
        "leadership": [
            {"name": "Geyswain", "title": "President/CEO; Division Head, Lochlann Real Estate", "notes": "Western dragon (dracoform)."},
        ],
        "notes": (
            "Security: lobby guard and elevator guard (posh lobby, atrium waterfall), a basement Security "
            "Center (map p.36-37: corridors on camera, locker room, briefing room, break room, shift "
            "supervisor's office, security administration, computer administration, computer room with "
            "palm-scanner Maglock 6, PANICBUTTONS and a pressure plate after 5 p.m.; three technicians "
            "on the security subprocessor round the clock; four basement guards and six in the building "
            "per shift), at least 20 guards to call on, gel-round Roomsweepers and stun batons under "
            "Geyswain's orders; a 15-man subprocessor crew. Corporate profile p.42. After the idol: 60 "
            "percent of the workforce never came home; at least 150 employees dead, killed by each other "
            "or by Geyswain, bodies looking days-dead within hours; the CPU physically burned; spirits "
            "and elementals swarming the upper floors. Success news: 'Lochlann massacre', cause "
            "'magically induced', Geyswain unconfirmed among the dead. Failure news: a 'strange fire' "
            "guts the Center, a large feathered serpent's body in the ruins, Geyswain unseen since."
        ),
        "allies": ["Knight Errant Security Services"],
    },
    {
        "name": "Children of Sophocles",
        "org_type": "mystical fellowship",
        "tier": 1,
        "headquarters": "Sophocles neighborhood, Redmond (a back-room club)",
        "summary": "Armchair magicians' society founded by Simon Templeman; Topal's friends, out to avenge him",
        "description": (
            "A mystical fellowship founded by the eccentric scholar Simon Templeman as a true scholarly "
            "society and lately degenerated into a social club of armchair mages and shamans -- 'The "
            "Kids', 'a buncha tarot-card-turning idiots' who could not call up a first-rank "
            "quasi-elemental, says the street. Topal led whenever Templeman wandered off after some new "
            "interest; now Caw Caw, a Raven shaman, leads with impassioned speeches."
        ),
        "leadership": [
            {"name": "Caw Caw", "title": "Leader (Raven shaman)", "notes": "Topal's closest friend."},
            {"name": "Simon Templeman", "title": "Founder (deceased)", "notes": None},
            {"name": "Pietr Fiegeton", "title": "Ad-hoc leader 'Topal' (deceased)", "notes": None},
        ],
        "notes": (
            "Members: Caw Caw, Gunderson Grey Knife (hermetic, analytical), Orion Yossarian (the only one "
            "with street-fighting experience), Aewyn Caleh (elf, newest). They know nothing of the idol "
            "-- Topal never told them -- and believe Blackwing's rumor. Their ambush (Etiquette (Street) "
            "TN 4 to spot; two block the sidewalk, two cast) collapses when one dies or two are down; "
            "talked down, they become an information source and future allies (and one knows Trixy has "
            "been asking about a red stone object)."
        ),
    },
    {
        "name": "Asphalt Devils",
        "org_type": "go-gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "A stretch of highway off Jefferson in the Puyallup Barrens",
        "summary": "Cruel, easily bored go-gang holding a Puyallup Barrens highway; Quick Kill and Sweet Sheila",
        "description": (
            "One of the go-gangs that swarm the Puyallup Barrens; this contingent guards its stretch of "
            "highway while the rest of the gang raids elsewhere. Cruel and vicious, bored easily at 3 "
            "a.m.: running a convoy off their turf is a moral victory, salvaging spare parts a bonus."
        ),
        "leadership": [
            {"name": "Quick Kill", "title": "Leader of the highway contingent", "notes": "Hyperactive wild man."},
        ],
        "notes": (
            "Six riders on Rapiers and Scorpions at speed 60, 50 meters behind the convoy, no mounted "
            "weapons (+2 to drive and shoot); five vehicle turns to clear their turf. Member block "
            "(p.12): B4 Q4 S4, Bike 4, Uzi III, armor vest with plating, knife. Stop a car and they stop "
            "to loot."
        ),
    },
    {
        "name": "Tir Tairngire",
        "org_type": "nation-state",
        "tier": 5,
        "headquarters": "Portland (the Elven nation south of Seattle)",
        "summary": "The Elven nation; an unnamed noble hired Blackwing; its ambassador leans on Lone Star; 'Paladins' rumored",
        "description": (
            "The Elven nation of Tir Tairngire, declared in 2037. News of Templeman's find spread through "
            "the Tir and reached an unnamed noble who hired the assassin Blackwing to obtain the idol by "
            "any means -- quietly. Its embassy leans on Lone Star's board to get Blackwing; Blackwing "
            "carries a diplomatic pass as an Associate Ambassador."
        ),
        "notes": (
            "'Some of the back-to-nature Elves' (the three murdered scholars) wanted the idol too. Street "
            "rumor says the Tir has sent Paladins after the runners. After the adventure Blackwing returns "
            "to the Tir with an inert idol, or none, and must explain it to his master. Andrew Shalene "
            "(Dreamchipper pregen) lived there and left over its politics."
        ),
    },
    {
        "name": "United Oil",
        "org_type": "corporation",
        "tier": 4,
        "headquarters": "Seattle offices (parent elsewhere)",
        "summary": "Oil corp whose Seattle security chief is the dragon Haesslich, away in Tokyo",
        "description": "An oil corporation with a Seattle presence notable for one thing: its security chief is the dragon Haesslich, the only other dragon Trixy knows of in the Seattle area.",
        "notes": "Haesslich is in Tokyo on business during Bottled Demon (no die rolls needed to learn it). The GM is advised to keep every other dragon in Seattle unavailable or uninterested.",
    },
    {
        "name": "Seattle News-Intelligencer",
        "org_type": "media",
        "tier": 2,
        "headquarters": "Seattle",
        "summary": "Seattle's daily newsnet; the source of most of the campaign's news handouts",
        "description": (
            "Seattle's principal daily newsnet (print and Update-Net), with local, world, sports, weather, "
            "business, lifestyle and entertainment sections and an At-A-Glance News Digest. Publisher "
            "Louise Berns; city editor George Harmon, the paper's first Elf reporter, known for "
            "even-handed metahuman/human coverage, retires to a retreat in Salish on February 1, 2051 "
            "and is replaced by investigative reporter Bruce Krasnow II ('Higher, Faster, Weaker', a "
            "North American Press award in 2048)."
        ),
        "leadership": [
            {"name": "Louise Berns", "title": "Publisher", "notes": None},
            {"name": "Bruce Krasnow II", "title": "City editor (from February 1, 2051)", "notes": "Investigative reporter; building-permit irregularities series."},
            {"name": "George Harmon", "title": "City editor (retiring)", "notes": "First Elf reporter at the paper."},
        ],
        "notes": (
            "January 15, 2051 edition (Bottled Demon / Queen Euphoria handouts): the Lochlann massacre or "
            "fire; Universal Brotherhood awareness centers coming to downtown Seattle and Tacoma; Justice "
            "Evan 'Hanging Evan' Gooch named to Governor Schultz's Crime Commission Select Panel on "
            "Containment (prosecuted the Screamin' Meemies, the first Ork gang eradicated by the Gang "
            "Task Force; presided over the year-long trial of organized-crime leader Hano Tomas, 24 "
            "consecutive life sentences); a go-gang hit-and-run that killed seven-year-old Tamsin "
            "Douglas-Kinsal at 6th Ave South and Main by Kobe Terrace Park (Lt. Avery Milkuski; 5,000 "
            "nuyen family reward); MindTrips 'Tourist Log' chip recall; Des Moines sewer protests "
            "(Clayton Lucas, Commissioner Kenneth Keenan); a squatters' fire in the luxurious Alki "
            "neighborhood that killed Birdie McGee, Shamus and an unidentified male, with Gemma and "
            "Freddie the Lip missing; Brighton's 'Rock Solid' and Euphoria's 'Final Fling' released. A "
            "reporter here is a natural contact."
        ),
    },
]

LOCATIONS = [
    {
        "name": "Yoshiro's Restaurant and Bar",
        "location_type": "restaurant",
        "district": "Seattle",
        "security_level": "Patrolled / Commercial",
        "summary": "See-and-be-seen restaurant where successful teams keep up their contacts; corner booths",
        "description": (
            "One of the places a successful team has to be seen: a bar and a restaurant section with "
            "corner booths where a man can sit with his back to the wall and order three entrees and two "
            "desserts. Mid-afternoon it is already busy with runners renewing contacts and paying the "
            "overhead of good will."
        ),
        "notes": "Where Topal finds the team and where he wants them idling their vehicles at 3:00 a.m. A good default 'where the team is seen' venue.",
    },
    {
        "name": "Black's Junk Yard",
        "location_type": "ruins",
        "district": "Puyallup Barrens",
        "security_level": "No Security / Barrens",
        "summary": "Legendary Seattle junkyard: mounds of crushed cars, a maze, a tunnel under the fence; no raid here ever goes to plan",
        "description": (
            "One of Seattle's legendary establishments: heavy steel gates, a fence topped with razor "
            "wire, and beyond them mounds and columns of crushed cars and ancient vehicles come to their "
            "final rest, stacked into a labyrinth whose lanes are blocked by fallen stacks. A single "
            "round rock by the fence rolls away from a tight tunnel that widens after five meters and "
            "climbs out behind the mounds under a red Ford LTD hood. Deep inside, a roughly circular "
            "clearing of beaten grass and spare parts under the moon."
        ),
        "notes": (
            "Map p.60: tunnel entrance and exit, the Citymaster's breach, the meeting place. Vehicles "
            "hide behind the dumpsters in the alley across the street. Grissim's raid: a Citymaster "
            "through a side gate and a wall of cars, ten troopers, two Yellowjackets autorotating in, "
            "'Turn to ice, boys and girls'; escape table by Reaction (p.14): razor wire 4M2, the front "
            "gate, or back to the tunnel. 'No raid on Black's has ever gone according to plan.'"
        ),
    },
    {
        "name": "The Guiding Hand",
        "location_type": "shop",
        "district": "Sophocles neighborhood, Redmond",
        "security_level": "Low Security",
        "summary": "Topal's small, profitable talismonger/lore shop -- burned to the ground the night after Templeman's cremation",
        "description": "A small but profitable talismonger and lore shop in the Sophocles neighborhood of Redmond, whose proprietor Topal enjoyed a good bit of local prestige. Now a burned-out shell: it caught fire the night Topal tried and failed to conjure with the idol's power.",
        "notes": "Where Simon Templeman staggered in with the case and died. Rumor on the street: 'Place burned down a night or two ago.' Nothing left to find.",
    },
    {
        "name": "Trixy's (Knower of Secrets)",
        "location_type": "shop",
        "district": "Redmond Barrens",
        "security_level": "Low Security",
        "summary": "Threadbare fortune-teller's shopfront over the home of Seattle's oldest Dog shaman and three dozen dogs",
        "description": (
            "A simple shop with a threadbare awning like a shroud and crude astrological symbols painted "
            "on opaque windows; a carved sign reads 'Trixy, Knower of Secrets, Teller of Fates. Fortunes "
            "told 10:30 - 6:00. Closed Sundays and Holidays.' Behind the dark vestibule the shop has "
            "become a home: a sitting area of furniture and books, a fireplace, a kitchen with food and "
            "drink, reading material everywhere, and some three dozen dogs -- all of whom stare at any "
            "astral visitor."
        ),
        "notes": "Trixy has lived in this building for 60 years and is a neighborhood fixture. Astrally inert from outside. Searching it in her absence reveals only that she is a Dog shaman.",
    },
    {
        "name": "Lochlann Center",
        "location_type": "corporate headquarters",
        "district": "Tacoma, north of the docks on the Lake Washington shore",
        "security_level": "Corporate Standard",
        "controlling_org": "Lochlann Investments",
        "summary": "Gleaming black-and-silver tower; posh atrium lobby; Geyswain's 2,000-square-meter Mojave desert lair on the top three floors",
        "description": (
            "Material excess a few kilometers from Redmond's poverty: gleaming black and silver metal, a "
            "posh lobby of glass, marble and real plants with a waterfall cascading from the third-floor "
            "atrium into a pool, an Information desk behind plexiglass, and a teak-paneled elevator "
            "hidden in the foliage that runs straight to the top. The upper three floors are one open "
            "eco-center landscaped as the Mojave: camphor-stinging hot dry air, hard-packed sand, "
            "sandstone boulders and full-sized flowering cacti hiding any windows, some 2,000 square "
            "meters, with two sealed exits (reinforced impact plastic, Barrier 20) -- the elevator and "
            "the double doors to a ramp onto the roof."
        ),
        "notes": (
            "Heavy weapons stay at the front desk (heavy pistols allowed). Geyswain's oven trick: 15 "
            "minutes before the first collapse, then 6S2 fatigue per minute (armor's impact rating adds to "
            "the Power); an area Sleep and eleven guards if you break out; wake in Tacoma Charity Hospital "
            "minus the idol. Second visit: lobby empty, cameras dead, a guard dead behind the desk with a "
            "recently fired gun and a five-bullet corpse by the elevators, an elevator full of wage slaves "
            "who tore each other apart, a stain on the last stair landing, the basement Security Center "
            "(shift supervisor Chester homicidal in the break room, one technician eating his two "
            "co-workers in the computer room, processors smashed), and upstairs cool moist air, a pile of "
            "days-dead bodies and Geyswain playing with Blackwing. Roof map p.61. Lone Star cordons the "
            "building, lands a dozen troopers and circles Wasps, Yellowjackets and an Ares Dragon command "
            "helicopter -- and fires no shot on private property."
        ),
    },
    {
        "name": "Tacoma Charity Hospital",
        "location_type": "hospital",
        "district": "Tacoma",
        "security_level": "Low Security",
        "summary": "Hospital of questionable repute where Lochlann dumps the runners; beds needed for the next team that lost to Aztechnology",
        "description": (
            "An establishment of questionable repute: a dying woman with something highly communicable in "
            "the next bed, a man down the hall screaming about bugs no matter how much tranquilizer they "
            "pump into him, doctors with plastic smiles who want you out to free the beds for some runners "
            "who just lost an argument with Aztechnology. Gear is returned in sealed safety bags."
        ),
        "notes": "Where Lochlann's guards deliver unconscious runners. A magician nobody on the team knows healed them (Arleesh). She waits outside by a white Mitsubishi Nightsky.",
    },
    {
        "name": "Snohomish Sheraton",
        "location_type": "hospital",
        "district": "Snohomish",
        "security_level": "Patrolled / Commercial",
        "summary": "Hotel where Blackwing killed the three elven scholars in room 616 with three shots",
        "description": "A Sheraton hotel in Snohomish. Room 616 on the sixth floor: three back-to-nature Elven runners dead with three precise shots, the scene clean, almost sterile, and a shattered pocket secretary under the third body.",
        "notes": "Grissim's joygirl lark spotted Blackwing leaving in a rush; a Predator under the desk clerk's nose got the room number; a cashed favor reconstructed 'Four a.m.' and 'Black's Junk Yard' from the recorder.",
    },
]

NPCS = [
    {
        "name": "Pietr Fiegeton",
        "role": "'Topal' -- chubby Raven-shaman talismonger dying of the idol; hires the team and is killed at the junkyard",
        "archetype": "Talismonger",
        "title": "\"Topal\", proprietor of The Guiding Hand (deceased)",
        "race": "Human",
        "gender": "Male",
        "organization": "Children of Sophocles",
        "connection": 2,
        "description": (
            "A chubby, waddling man in tres chic clothes much the worse for wear, a black alloy courier "
            "case manacled to his right wrist, weary haunted eyes and a high cracking voice; ten years "
            "older under street lights than under Yoshiro's soft ones. A Raven shaman who eats without "
            "pause -- three entrees, two desserts, and a pocketful of jawbreakers -- and says 'Good, "
            "good, good.'"
        ),
        "background": (
            "A small-time magician and unassuming shopkeeper with prestige among the locals, ad-hoc "
            "leader of the Children of Sophocles whenever Templeman wandered off. Took the case from his "
            "dying friend, found the idol would serve him as a Power Focus though he had not made it, "
            "played with it until the dreams came, the shop burned, and his body began to fail, then by a "
            "feat of will put out word he would sell -- to an enclave of Elven magicians."
        ),
        "notes": (
            "Pays 5,000 each (Opposed Negotiation, +10 percent per net success), half up front; will not "
            "say where, what, or whether he buys or sells. Cuffs the case to a runner at the clearing "
            "('It will be safe with you'), wheezes across to the wrong Elf, and must die -- Blackwing's "
            "rifle, Tundra's Power Bolt, a stray Lone Star round, or a falling stack of cars. Stats: B2 Q2 "
            "S1 C4 I4 W4, Ess 6, Magic 6 (1 when more than four meters from the idol); Conjuring 6, "
            "Sorcery 5, Magical Theory 6; Astral pool 15 (10); Mana Bolt 3, Analyze Device 4, "
            "Entertainment 4; Colt L36, Mitsubishi Runabout."
        ),
    },
    {
        "name": "Simon Templeman",
        "role": "Eccentric scholar-founder of the Children of Sophocles who brought the idol back from the South Pacific and died of it",
        "archetype": "Scholar",
        "title": "Founder, Children of Sophocles; archaeologist (deceased)",
        "race": "Human",
        "gender": "Male",
        "age": 42,
        "organization": "Children of Sophocles",
        "connection": 1,
        "description": "Well-known, somewhat respected, a bit eccentric: a multi-discipline scholar who dashed off after every new interest. Came back from a prolonged archaeological/anthropological expedition through the South Pacific with a courier case chained to his wrist, delirious, and died in Topal's shop the same day, wracked with pain.",
        "notes": "The coroner called it natural causes -- surprised to learn he was 42, not in his late sixties as his body suggested. Cremated last week. No one knows where in the South Pacific he found the idol; research into its history ends with him.",
    },
    {
        "name": "Captain Grissim",
        "role": "Iron-jawed, straight-shooting Lone Star captain who has chased Blackwing since Los Angeles",
        "archetype": "Police Captain",
        "title": "Captain, Lone Star Security (Seattle)",
        "race": "Human",
        "gender": "Male",
        "organization": "Lone Star Security",
        "connection": 4,
        "description": (
            "An iron-jawed, blue-eyed rock of a man, dark hair graying at the temples, uniform spotless "
            "and creased; Swedish dermal plates so well placed nobody notices. Smokes nicosticks, likes a "
            "lot of lights on his console, smacks subordinates to punctuate orders, and never sends an "
            "officer where he would not go himself. Tough but fair, more concerned with justice than "
            "law; the idol of the city's street cops."
        ),
        "background": (
            "Nearly 20 years with Lone Star, a spotless record, unofficial influence in every corner of "
            "the company, never above Captain. Headed the Lone Star-LA investigation into a rash of "
            "political killings attributed to Blackwing, could pin nothing on him, and was transferred "
            "to Seattle. Rides a Citymaster with rigger Ronnie and a fresh-from-the-academy elf aide, "
            "Swope."
        ),
        "notes": (
            "Wants Blackwing, not the runners; his bosses (leaned on by the Tir Tairngire ambassador "
            "upstairs) want both, alive if possible, so he puts the team on the news as Class A felons. "
            "Interrogates prisoners under a Lone Star mage's Analyze Truth for 24 hours, then releases them "
            "under astral surveillance. Might cut a deal for Blackwing. Cordons Lochlann, lands on the "
            "roof, and watches. After the dust settles he is either a Lone Star contact or a lifelong "
            "adversary, depending on how many of his men are in the morgue. If he gives his word, count on "
            "it. Stats: B6(8) Q4 S5 C4 I5 W6, Ess 3.85; Armed Combat 7, Etiquette (Street) 8, Firearms 5, "
            "Interrogation 5, Police Procedures 6; datajack, dermal plating 2, radio, flare compensation; "
            "Ruger Super Warhawk, katana, concussion grenades, low-light/thermo binoculars."
        ),
        "contact_skills": ["Lone Star command-level access (raids, releases, deals)", "Twenty years of Seattle and LA police intelligence"],
    },
    {
        "name": "Blackwing",
        "role": "Icy, stylish elven assassin (37 confirmed kills) hired by a Tir noble to fetch the idol; alias Bloodwing",
        "archetype": "Hitman",
        "title": "Elven assassin (\"Bloodwing\"); Associate Ambassador of Tir Tairngire (diplomatic pass)",
        "race": "Elf",
        "gender": "Male",
        "nationality": "Tir Tairngire",
        "organization": "Tir Tairngire",
        "connection": 3,
        "description": (
            "The essence of style and grace: the most expensive clothes in dark solid colors and simple "
            "tailoring, hair perfectly in place whatever happens, a permanent smile on a finely chiseled "
            "face, a cigarette flicked away in one smooth gesture. Icy calm, constantly alert to "
            "alternatives, makes the most of every enemy mistake, not afraid to die. Loves every minute "
            "of it after ten years."
        ),
        "background": (
            "One half of the infamous Blackwing-Nightprince team of Elven assassins (his usual partner "
            "Cillian Nightprince is the spontaneous one), credited with a perfect record of 37 confirmed "
            "terminations, blamed for political killings in Los Angeles that Grissim could never prove. "
            "Hired by an unnamed Tir Tairngire noble to get the idol without noise; killed the three "
            "scholars, went underground when the junkyard raid blew up, spread the rumor that the runners "
            "iced Topal, tracked them to Lochlann, and was broken by Geyswain."
        ),
        "notes": (
            "Team: Tundra and Harper. At the clearing: 'Are you ready, Raven-man? I have the oath price.' "
            "Snipes Topal with the HAR, then withdraws. Found as Geyswain's 'flesh toy'; fights the dragon "
            "gladly if given a weapon; afterwards claims the idol as stolen Tir property, pays 50,000 "
            "non-negotiable, and beats Grissim's arrest with a diplomatic pass. Deported to the Tir to "
            "explain an inert idol. Stats: B5 Q6 S4 C3 I5 W5, Ess 0.2, Reaction 5(11); Firearms 8, "
            "Unarmed 7, Armed 5, Demolitions 5, Car 5, Computer 4; cyberears, smartlink, Wired Reflexes 3; "
            "Ares Predator and FN HAR with built-in smartlinks, tres chic armor clothing, Westwind 2000, "
            "DocWagon Gold; low-light eyes, sunlight allergy (nuisance)."
        ),
    },
    {
        "name": "Tundra",
        "role": "Gun-shy veteran elven mage on Blackwing's team, winding down his career; leads with his biggest weapon",
        "archetype": "Street Mage",
        "title": "Elven mage, Blackwing's team",
        "race": "Elf",
        "gender": "Male",
        "organization": "Tir Tairngire",
        "connection": 1,
        "description": "Running the shadows for more years than he cares to remember and worn out by it; more than a little gun-shy after too many firefights, he leads with his biggest spell or gun and avoids melee. Sits in lotus atop the tallest stack in the junkyard under a blue Armor aura with yellow Increase Reaction pulses playing tag across his body.",
        "notes": "Ready to die to finish what may be his last mission. Stats: B3(4) Q4 S4 C2 I5 W5, Ess 5.2, Magic 5, Reaction 4(6); Sorcery 6, Magical Theory 6, Firearms 4; dermal plating 1, retractable spurs; Uzi III, two offensive grenades, armor jacket, Armor and Increase Reaction spell locks, Yamaha Rapier. Spells: Manaball 5, Power Bolt 5, Combat Sense 4, Detect Enemies 4, Heal Severe Wounds 4, Armor 4. Silver allergy (moderate).",
    },
    {
        "name": "Harper",
        "role": "New kid on Blackwing's team; astral-combat specialist elven mage who treats them as family",
        "archetype": "Street Mage",
        "title": "Elven mage, Blackwing's team",
        "race": "Elf",
        "gender": "Female",
        "organization": "Tir Tairngire",
        "connection": 1,
        "description": "Blackwing and Tundra are the only people she has ever worked with and she treats them like family; she will do anything to get them out safely but will not die for the case -- she would escape and take revenge later. Slips into astral space mid-fight for a better view; excels at astral combat. Floats above and behind Blackwing at the clearing and nods to astral visitors.",
        "notes": "Covers retreats with the Enfield or Chaotic World. Stats: B1 Q4 S1 C4 I5 W5, Ess 6, Magic 7; Sorcery 7, Conjuring 6, Magical Theory 6, Etiquette (Tribal) 4; Astral pool 18. Spells: Powerball 4, Sleep 6, Clairvoyance 4, Mind Probe 5, Heal Moderate Wounds 5, Chaotic World 5, Magic Fingers 4. Enfield AS7, lined coat, three fetishes per spell, Armor spell lock, Yamaha Rapier. Plastic allergy (mild).",
    },
    {
        "name": "Trixy",
        "role": "Ancient Dog shaman fortune-teller of the Redmond Barrens who dreamed of the idol; sends the team to a dragon",
        "archetype": "Street Shaman",
        "title": "Fortune teller ('Knower of Secrets, Teller of Fates'); Dog shaman",
        "race": "Human",
        "gender": "Female",
        "connection": 5,
        "description": (
            "A small, very old woman with an ancient hand, a rocking chair by the fire, knitting, tea and "
            "pastries for guests, and three dozen dogs. One of the oldest shamans in Seattle; a fortune "
            "teller most of her life who trusts her own common sense and the signs of nature over "
            "traditional divination. 'I can see in your eyes that you're in very deep doo-doo.' Patient, "
            "well loved, well respected; few suspect the power she wields."
        ),
        "background": (
            "Grew up in what is now the Redmond Barrens and has lived 60 years in the same building. Her "
            "hard life has worn her Essence and Magic down to 4. Her dreams told her the team was coming; "
            "she has been asking around about a small object of red stone. Knows Geyswain and Haesslich; "
            "has already talked to Geyswain -- and to Arleesh."
        ),
        "notes": (
            "Holds the idol briefly (the dogs get restless), walks with her two largest dogs, comes back "
            "with an extra one, and pronounces in a deep resonant voice: a tool of corruption; only a "
            "Dragon has the wisdom to destroy it; a request for service, not a trade. Will not take the "
            "idol or come along. All roads lead to her; she is the only one who can help clear the team's "
            "reputation. Stats: B2 Q1 S1 C5 I6 W5, Ess 4, Magic 4; Conjuring 7, Sorcery 6, Magical "
            "Theory 6, Etiquette (Street) 6; Astral pool 16. Spells: Mana Ball 6, Power Dart 5, Sleep 8, "
            "Analyze Truth 6, Clairvoyance 8, Detect Enemies 6, Mind Probe 8, Antidote 4, Heal "
            "Moderate/Severe 5/4, Hibernate 5, Levitate Person 5. Orichalcum knife, medicine lodge 8, "
            "ritual materials (detection, health) 6, lined coat, Dodge Scoot."
        ),
        "contact_skills": ["Divination, dreams and common-sense counsel", "Knows Seattle's dragons and its oldest shamans", "Redmond Barrens neighborhood standing"],
    },
    {
        "name": "Geyswain",
        "role": "Young, arrogant Western dragon CEO of Lochlann Investments; takes the idol and is consumed by it",
        "archetype": "Dragon",
        "title": "Western dragon (dracoform); President/CEO, Lochlann Investments",
        "race": "Western Dragon",
        "gender": "Male",
        "organization": "Lochlann Investments",
        "connection": 3,
        "description": (
            "Easily 20 meters snout to hind legs with a tail as long again, spines ringing his head and "
            "lining his back, brown and red scales under dark red plates, tongue darting, head weaving, "
            "stepping over his cacti with care. 'Well, don't just hover there!' Arrogant even for a "
            "dragon, and very young; explains away every mistake and never learns from them, which makes "
            "him an outsider among dracoforms. Wears the big scar on his left flank -- a 'hostile "
            "takeover in Aztlan' -- as a badge of courage."
        ),
        "background": (
            "Awakened in the deserts of the American Southwest almost 20 years ago, wandered the Western "
            "Hemisphere observing, saw the long-term value of Barrens land to something as long-lived as "
            "himself, and spent part of a hidden hoard on it twelve years ago. Not evil or stupid; he just "
            "does not understand consequences. Knows something of the forces behind the idol but has "
            "never felt them, so he cannot see the danger -- a little wiser he would destroy it, a Great "
            "Dragon he could."
        ),
        "notes": (
            "Levitates the idol to eye level (never touches it), agrees to an 'arduous ritual' of 'Dragon "
            "magic no mortal may view', demands a favor owed by the team as a group, and bakes them in the "
            "lair if they hedge. Within a day the idol has consumed him: pus-filled sores, scales sliding "
            "off, torn wings, feeding on his own staff, rogue Force 3 spirits and elementals (one or two "
            "at any moment) at his call. Flees to the roof when Seriously Wounded, meets Lone Star's "
            "guns, and turns back to take the runners with him. Stats: B14(6) Q7x3 S40 C3 I5 W8, Ess 8, "
            "Magic 8; Sorcery high, Conjuring 7, Magical Theory 8; Astral pool 22; noxious breath 10S2, "
            "low-light eyes, wide-band hearing. Spells: Hellblast 7, Manaball 12, Mana Dart 10, Power Bolt "
            "8, Sleep 10, Clairvoyance 8, Detect Enemies 7, Detect Life 8, Detox 7, Heal Severe 8, "
            "Confusion 6, Invisibility 8, Stink 8, Armor 8, Ignite 8, Levitate Item 8, Magic Fingers 10, "
            "Toxic Wave 6. Almost certainly dead at the end; Lone Star will not confirm."
        ),
    },
    {
        "name": "Arleesh",
        "role": "Great Feathered Serpent ten months awake, slumming in Seattle; uses the runners to reach and implode the idol",
        "archetype": "Great Dragon",
        "title": "Great Feathered Serpent ('of ancient and honorable lineage')",
        "race": "Feathered Serpent",
        "gender": "Female",
        "connection": 5,
        "description": (
            "In human form a beautiful woman in mirrorshades and an earth-toned headdress leaning on a "
            "long sleek white Mitsubishi Nightsky, scowling; for the Lochlann job a long white leather "
            "evening dress with plunges and a side slit. 'Somebody really should teach you the differences "
            "between Dragons.' Snapped a man's fingers in a Barrens bar when he got too feelie. Loyal only "
            "to herself; keeps her word to humans but sees them as tools and would lead them into Hell to "
            "further her mission."
        ),
        "background": (
            "Awake only ten months and still a bit out of things; came to Seattle to slum and learn "
            "modern human culture, sensed the idol, and could track it only once it left its warded case. "
            "Young for a Great Dragon but ancient beside Geyswain, with first-hand knowledge of the horrors "
            "behind the idol's power; will spend her own life to destroy it, and will not risk being too "
            "weakened by Geyswain to do it -- hence the runners."
        ),
        "notes": (
            "Healed the team in the hospital; buys everyone Stuffer Shack; 'Assense me, I will allow you "
            "to see my real form.' Refuses refusal ('if any other Great Dragons learn what you have "
            "done...'). Plan: a decker confuses Lochlann's system while the rain-soaked damsel takes the "
            "lobby; sends the team to the basement, goes up alone with a gym bag, waits invisible, then "
            "tears the idol from Geyswain and implodes it in blue-purple light. 'Here. Have fun. And "
            "thanks.' If the team skips the docks she goes alone -- a dragon's body is found either way. "
            "Stats (dragon / human form): B18(8) Q6x2(7) S40(8) C8 I7 W12, Ess 12, Magic 12, Reaction "
            "10(7); Sorcery 15, Conjuring 12, Magical Theory 12, Interrogation 8, Psychology 8, Unarmed 8; "
            "Astral pool 34. Spells incl. Power Bolt 12, Manaball 10, Sleep 10, Hibernate 10, Armor 9, "
            "Turn to Goo 8, Petrify 8, Control Emotion 8, Chaotic World 7, Invisibility 6. Orichalcum "
            "sword, Ruger Super Warhawk, shuriken, tres chic armor jacket, wrist computer. May return to "
            "lead the runners into more adventures -- 'with friends like this, who needs fixers?'"
        ),
        "contact_skills": ["Great Dragon patronage (magic beyond any human, knowledge of the old horrors)", "A white Nightsky and a low profile in Seattle"],
    },
    {
        "name": "Caw Caw",
        "role": "Cadaverous Raven shaman orator leading the Children of Sophocles to avenge Topal",
        "archetype": "Street Shaman",
        "title": "Leader, Children of Sophocles (Raven shaman)",
        "race": "Human",
        "gender": "Male",
        "organization": "Children of Sophocles",
        "connection": 2,
        "description": "Cadaverously thin, all bones and skin, with a remarkable speaking voice -- every word for maximum effect, crowds swayed with ease. Like every Raven shaman he eats constantly, but only food prepared by the city's finest chefs. Arrogant but not stupid; believes attacking the runners was right.",
        "notes": "Topal's closest friend and the hardest to persuade of the team's innocence. Stats: B3 Q3 S2 C2 I4 W2, Ess 6, Magic 6; Magical Theory 6, Conjuring 4, Sorcery 3; Astral pool 13. Spells: Powerball 5, Analyze Device 4, Chaotic World 4, Entertainment 3, Control Emotion 3. Browning Max-Power, armor vest, Chrysler-Nissan Jackrabbit, tres chic clothing.",
        "contact_skills": ["Children of Sophocles fellowship", "Oratory / crowd-swaying"],
    },
    {
        "name": "Gunderson Grey Knife",
        "role": "Half-Amerindian hermetic mage of the Children who dislikes coincidence and hunts causes",
        "archetype": "Street Mage",
        "title": "Hermetic mage, Children of Sophocles",
        "race": "Human",
        "gender": "Male",
        "nationality": "Half Amerindian",
        "organization": "Children of Sophocles",
        "connection": 2,
        "description": "Analytical almost to a fault, interested in cause and effect, with an extreme dislike of coincidence; diligently searches for the causes behind magic. Wears an armor poncho with one hand hidden beneath it.",
        "notes": "The strongest caster of the Children. Stats: B3 Q4 S3 C2 I4 W4, Ess 6, Magic 6; Sorcery 7, Magical Theory 6, Conjuring 4, Armed Combat 4; Astral pool 17. Spells: Mana Bolt 4, Armor 6, Magic Fingers 4. Enfield AS7, two combat fetishes, knife.",
    },
    {
        "name": "Orion Yossarian",
        "role": "The Children's one street-experienced mage; once a magical bodyguard to a crime figure",
        "archetype": "Street Mage",
        "title": "Mage, Children of Sophocles",
        "race": "Human",
        "gender": "Male",
        "organization": "Children of Sophocles",
        "connection": 2,
        "description": "Probably the most experienced street fighter among the Children after a stint as magical bodyguard to an underworld crime figure some years ago -- still nowhere near the runners' class.",
        "notes": "Stats: B3 Q3 S3 C4 I5 W4, Ess 6, Magic 6; Conjuring 6, Car 4, Firearms 4, Magical Theory 4; Power Focus 3. Spells: Power Bolt 4, Detect Enemies 4, Mask 3, Hibernate 3, Levitate Item 4. Ares Slivergun, armor jacket.",
    },
    {
        "name": "Aewyn Caleh",
        "role": "Elven newcomer to the Children (born Adrian); least attached to Topal, most willing to listen",
        "archetype": "Street Mage",
        "title": "Mage, Children of Sophocles",
        "race": "Elf",
        "gender": "Female",
        "organization": "Children of Sophocles",
        "connection": 2,
        "description": "A female Elf, born Adrian and renamed at puberty 'to better reflect her Elven heritage'; a lifelong Seattleite. Joined only recently, so less emotionally tied to Templeman and Topal and more willing to hear the runners' story.",
        "notes": "Stats: B3 Q5 S2 C6 I6 W4, Ess 6, Magic 6; Sorcery 6, Conjuring 5, Unarmed 5; Astral pool 18. Spells: Analyze Truth 4, Detect Life 4, Heal Moderate 4, Heal Severe 5, Poltergeist 4. Ruger Super Warhawk, lined coat, smoke grenade, thermographic goggles, detection and healing fetishes.",
    },
    {
        "name": "Quick Kill",
        "role": "Hyperactive wild man leading the Asphalt Devils' highway contingent",
        "archetype": "Gang Boss",
        "title": "Asphalt Devils (highway contingent leader)",
        "race": "Human",
        "gender": "Male",
        "organization": "Asphalt Devils",
        "connection": 1,
        "description": "Always moving, always talking; a real wild man on a Harley Scorpion.",
        "notes": "Stats: B4(5) Q4 S5 C3 I3 W5, Ess 3.5, Reaction 3(5); Bike 6, Armed Combat 4, Firearms 4, Gunnery 3; low-light cybereyes, dermal plating 1, Wired Reflexes 1; Uzi III, Ares Predator, katana, two offensive grenades, lined coat, helmet.",
    },
    {
        "name": "Sweet Sheila",
        "role": "Quick Kill's honey; screams like a maniac in a fight and looks prettier for it",
        "archetype": "Gang Member",
        "title": "Asphalt Devils",
        "race": "Human",
        "gender": "Female",
        "organization": "Asphalt Devils",
        "connection": 1,
        "description": "Quick Kill's honey, anything but sweet in battle: screams like a maniac during a fight and, oddly, seems prettier that way. The best rider in the pack.",
        "notes": "Stats: B3 Q4 S4 C5 I3 W6, Ess 6; Bike 7, Firearms 4, Stealth 5; H&K 227 SMG with laser sight, armor jacket, Harley Scorpion.",
    },
    {
        "name": "Haesslich",
        "role": "Dragon security chief of United Oil, the only other dragon Trixy knows in Seattle; away in Tokyo",
        "archetype": "Dragon",
        "title": "Security chief, United Oil (Seattle)",
        "race": "Western Dragon",
        "gender": "Male",
        "organization": "United Oil",
        "connection": 2,
        "description": "A dragon employed as security chief by United Oil -- the only other dragon in the Seattle area that Trixy knows of.",
        "notes": "In Tokyo on business throughout Bottled Demon (no die rolls needed to learn it). No stats given; kept unavailable so the team must go to Geyswain.",
    },
]

ORG_UPDATES = {
    "Lone Star Security": {
        "notes_append": (
            "Bottled Demon: Captain Grissim (transferred from Lone Star-LA, straight as they come, "
            "unofficial pull everywhere) commands raids from a Citymaster with a water cannon and turret, "
            "with rigger Ronnie, a pair of wage mages for astral cover, Yellowjackets that autorotate in "
            "silently, Wasps, and an Ares Dragon transport as a command post; street cops here are riot- "
            "and close-combat-trained (Police Procedure 4; Predator, armor jacket, helmet, low-light "
            "goggles, earplug radio, stun baton first) and back off when seriously wounded; a Lieutenant "
            "(Police Procedure 5, cybereyes with camera) per four troopers. Heat tactics: raids on every "
            "known haunt, media alerts naming runners Class A felons, homes staked out, vehicles impounded, "
            "squatters paid to snitch, 24-hour interrogation under Analyze Truth, astral surveillance on "
            "release. The board was being leaned on by the Tir Tairngire ambassador; 'I ain't seen them "
            "so bent since what's-his-face was going around AVMing the monorail.' Lone Star will not "
            "fire a shot on private corporate property. Corporate spokesperson Jacob Bright."
        ),
        "leadership_add": [
            {"name": "Captain Grissim", "title": "Captain (raid commander)", "notes": "Bottled Demon; Blackwing's nemesis."},
            {"name": "Jacob Bright", "title": "Corporate spokesperson", "notes": None},
        ],
    },
    "Knight Errant Security Services": {
        "notes_append": "Bottled Demon: Lochlann Investments' internal security force is periodically retrained at the local Knight Errant training facility.",
    },
    "Aztechnology": {
        "notes_append": (
            "Bottled Demon: the dragon Geyswain carries a large scar on his left flank from 'a hostile "
            "takeover in Aztlan'; Tacoma Charity Hospital is used to patching up runners who 'just lost "
            "an argument with Aztechnology'."
        ),
    },
    "Universal Brotherhood": {
        "notes_append": (
            "Bottled Demon (January 15, 2051): spokesperson Niles Patrick announces 'awareness centers' "
            "in downtown Seattle and Tacoma by summer, modelled on the many already operating in "
            "low-income neighborhoods -- 'executives at all levels are leading miserable, unfulfilled "
            "lives'. Neighborhood support is growing; some city leaders call it a front for "
            "anti-establishment sentiment. 'Our only purpose is to raise an individual's personal "
            "awareness.'"
        ),
        "leadership_add": [
            {"name": "Niles Patrick", "title": "Spokesperson", "notes": "January 2051 news handouts."},
        ],
    },
    "Seattle Metroplex Guard": {
        "notes_append": (
            "Bottled Demon (January 2051 news): Governor Schultz formed the Seattle Crime Commission "
            "Select Panel on Containment; appellate justice Evan 'Hanging Evan' Gooch (prosecutor of the "
            "surviving Screamin' Meemies, the first Ork gang eradicated by the Gang Task Force; presided "
            "over the trial of organized-crime leader Hano Tomas, 24 consecutive life sentences) fills one "
            "of its last two seats. City Commissioner Kenneth Keenan fields the Des Moines sewer revolt."
        ),
    },
    "MegaMedia Entertainment": {
        "notes_append": "Bottled Demon news (January 15, 2051): MegaMedia rushes out Euphoria's 'Final Fling', her first sim without Hans Vandenburg, to counter Brilliant Genesis's 'Rock Solid'.",
    },
    "Brilliant Genesis": {
        "notes_append": "Bottled Demon news (January 15, 2051): releases Honey Brighton's 'Rock Solid', the controversial project she and Witt Lipton took with them; expected to be its biggest saturation release to date; the defection's lawsuits are still unsettled.",
    },
}

LOC_UPDATES = {
    "The Barrens (Seattle)": {
        "notes_append": (
            "Bottled Demon: Puyallup -- Jefferson runs through Asphalt Devil territory to Black's Junk "
            "Yard; 'most people wouldn't travel these streets in broad daylight'. Redmond -- the Sophocles "
            "neighborhood (Topal's Guiding Hand), Trixy's shopfront, and the Lochlann land nobody develops."
        ),
    },
}

NPC_UPDATES = {}

TAG_EXISTING = {}

MATRIX_HOSTS = """
**Lochlann Center system** -- quad-linked geodesics shifting emerald to sapphire on the neon edge of
Lake Washington, mid-sized, rough imagery. By the time anyone decks it the SAN is 'clean-squeak open',
the IC present but dead with nothing commanding it, and the CPU physically burned from inside. Nothing
to build for this adventure; if a GM wants the pre-massacre host, improvise an Orange corporate system
with a security subprocessor run by a 15-man crew and three on-duty technicians.

**Pacific Towers / Strice** -- see Queen Euphoria. No other systems in Bottled Demon.
"""

NOT_BUILT = """
- **The idol** (Playing With Darkness, pp.51-53): 30 cm, two kilos, indestructible, unscannable;
  Power Focus 12 usable unbonded by anyone with Magic 1+; Sorcery (12) assensing table (channels veer
  90 degrees into another level of existence); cannot augment Summoning (twisted spirits); every use is
  a Magic Test vs the rating used -> Magic loss and Major/Minor Physical Effects the user cannot
  perceive; shamans lose totem bonuses below half Magic and need a lodge purge; separation beyond
  Willpower meters or destruction = Magic collapses, 1D6 Major Effects (Willpower 12 to negate each),
  6D1 Stun vs Body 12, recovery 1 point per day with nightmares; below half Magic the user craves it;
  at Magic 0 a Willpower (24) test or a slide into insanity over Willpower days. Karma: nobody affected
  3, Geyswain denied 5, idol destroyed 8, not destroyed -10. Kept as rules, not an entity.
- **Cillian Nightprince** (Blackwing's usual partner, absent), **Ronnie** (Grissim's rigger), **Swope**
  (Grissim's elf aide), **Banes** (Blue One), **Chester** (Lochlann's homicidal shift supervisor), the
  **cannibal technician**, the **three murdered elven scholars**, the **joygirl lark** -- on the org /
  NPC rows.
- News names: **Governor Schultz, Justice Evan Gooch, Hano Tomas, the Screamin' Meemies, Lt. Avery
  Milkuski, Tamsin Douglas-Kinsal and Madigan Kinsal, Clayton Lucas, Kenneth Keenan, Birdie McGee,
  Shamus, Gemma, Freddie the Lip, MindTrips** -- on the News-Intelligencer row.
- **Kobe Terrace Park, the Alki neighborhood, Des Moines, the abandoned storefront near Lochlann** --
  not recorded as locations.
"""

PLAY_NOTES = """
- Two employers, both doomed: Topal must die at the junkyard; Geyswain must get the idol. The
  runners' job is to survive being wrong.
- Make the idol tempting (a Power Focus 12 anyone can use) and keep every Magic Test secret; the
  affected player roleplays symptoms he cannot see. Separation and destruction hurt.
- The heat is the adventure's engine: no contact talks (Target 5; a Lone Star contact at 7), squatters
  snitch, homes are staked out. Lone Star Country is for pressure, not slaughter -- dead cops turn
  Grissim into a permanent enemy.
- The Children of Sophocles are a conversation, not a fight, if the players listen to what they shout.
- Trixy is the pivot: every road leads to her, and she will not take the idol.
- Geyswain's lair is an oven; roll the fatigue yourself. Lochlann the second time is horror -- the
  elevator of bodies, the basement, the pile in the sand.
- Arleesh sacrifices the runners' hides to save her strength. Bloodwing (a weapon in his hand),
  Harper and Tundra, even the Children, can join the dragon fight if the team needs bodies.
- Loose ends: Grissim as contact or enemy; Blackwing's return from the Tir (and his master's wrath);
  Arleesh's next 'request'; the inert idol if anyone kept it; who else knows what it was.
"""
