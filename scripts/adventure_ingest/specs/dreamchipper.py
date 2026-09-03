# Dreamchipper (FASA 7303, 1989) -- campaign order #5. Seattle (Bellevue / Redmond Barrens),
# a Sunday-to-Friday week in 2050 (the news handout is dated Wednesday, August 17, 2050).
# Source text: docs/Adventures/text/Shadowrun 1e - Dreamchipper {FASA7303}.txt (75 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "Dreamchipper"
ORDER = 5
SOURCE = "Shadowrun 1e - Dreamchipper {FASA7303}.pdf, pp. 4-74"
YEAR = "2050 (late summer; news handout dated August 17, 2050)"

SYNOPSIS = """
**Global Technologies**, a small Bellevue skillsoft house, has secretly built three "Global
Dreamchips" -- skillsofts fused with BTL technology that overlay a whole encoded personality on the
user: **Genghis Khan**, **Cleopatra** and **Jack the Ripper**, demo products for the UCAS military.
The night before the adventure a team hired by fixer **Marcus "Face" Cooperman**, "the Historian",
stole all three prototypes with inside help from Global's star decker **Tee Hee**, who then wiped
every copy of the research and hid the only backup on the desktop of **Thomas "Junior" Martelli** --
the founder's goblinized son, who is conspiring with **Booker Pengrave** of **Hollywood Simsense
Entertainment** to bankrupt Global at Friday's board meeting and buy it for a song.

Cooperman paid his crew in stolen chips and everything fell apart. He jacked the Khan chip himself
and is uniting the **Blood Rumblers** and three other go-gangs to conquer the Redmond Barrens;
samurai **Griffin** jacked Jack and is dissecting joygirls and joyboys in the Barrens fog; rigger
**Val Westerfield** jacked Cleo and now, as "Cleo", has Pengrave wrapped around her finger. The
fourth thief, elven mage **Freya Goldenhair**, was left behind bleeding on the sidewalk and is
mending at **Dr. Bob's Quickstitch**, plotting payback.

Global president **Urlan Manes** and his division head **Roxanne Wunter** hire the runners at Reno's
and brief them in the back room of **The Banshee**: recover the chips by 9 a.m. Friday, quietly,
30,000 nuyen per runner per intact chip, and never use them. The trail runs from Tee Hee's desk
contents to the decker bar on Cascade Road and his old professor **Flair**, to Freya, to Junior's
ambush at The Banshee (with the dwarf weapons-check bouncer Gus turned traitor), to Pengrave's
premiere party on Queen Anne Hill, to a car chase to the docks, to the go-gang war council in a
warehouse at Union Hill Road and 208th, and to a night walking the 15-block kill zone as bait for
Jack. Pulling a chip fries its wearer's brain; the runners must decide whether to hand the chips back
(saving Global, and arming the UCAS military) or destroy them and forfeit the fee.
"""

TIMELINE = """
- **Sunday night** -- Reno's (Roxanne), Ferret's tail, 1:00 a.m. at The Banshee with Urlan; Junior
  and two Ork bodyguards crash the meeting; the box of Tee Hee's desk contents.
- **Monday** -- Cascade Road (Breadboard, Orion's), Flair, Tee Hee's one-room flat; Dr. Bob's
  Quickstitch and Freya. Monday night: Roxanne's 11 p.m. meet at The Banshee = Junior's ambush.
- **Tuesday evening** -- HSE premiere party at Pengrave's condo, Queen Anne Hill; Val/Cleo leaves
  in a Mitsubishi Nightsky for the docks and Pengrave's boat.
- **Wednesday night** -- Khan's war council with eight gang leaders at the Union Hill / 208th
  warehouse, then the ride into Redmond.
- **Thursday night** -- the trap for Jack in the 15-block murder zone (nine dead in four nights).
- **Friday 9:00 a.m.** -- chips due in Roxanne's hands; 9:30 board of directors meeting.
- Contacts twice a day; 1D6 4+ = a Redmond street encounter (twelve scripted, p.52).
"""

# ----------------------------------------------------------------------------------------------
ORGS = [
    {
        "name": "Global Technologies",
        "org_type": "corporation",
        "tier": 2,
        "headquarters": "Bellevue, Seattle (single office building)",
        "summary": "Small skillsoft/simsense house (127 staff) behind the Colt L36-Mark VII and the illegal Global Dreamchips",
        "description": (
            "A rather grandiose name for a small Bellevue skillsoft company of 127 employees, mostly "
            "deckers, founded 15 years ago by Thomas Martelli Sr. and Urlan Manes and run from an "
            "apartment before it became a corporation. Years of lackluster products ended when a wave "
            "of University of Seattle graduates joined; its Colt L36-Mark VII is now the premier "
            "hand-gun skillsoft in Seattle. Divisions: Back Door Technologies (military, commercial "
            "and private skillsofts and memory modules; head Roxanne Wunter) and Martelli "
            "Entertainment (entertainment simsense; head Thomas Martelli Jr.), a once-separate company "
            "nearly bankrupted by Hollywood Simsense and reacquired three years ago. Global keeps no "
            "military assets; its guards, security deckers and mages are hired from Knight Errant as "
            "needed. Its building has a blue neon sign, Armorlite acrylic doors and a fourth-floor "
            "think tank."
        ),
        "leadership": [
            {"name": "Urlan Manes", "title": "President/CEO", "notes": "Inherited most of Martelli Sr.'s stock two years ago."},
            {"name": "Roxanne Wunter", "title": "Division Head, Back Door Technologies", "notes": "Urlan's right hand; number two at Global."},
            {"name": "Thomas Martelli Jr.", "title": "Division President, Martelli Entertainment", "notes": "'Junior'. Conspiring with HSE to take the company."},
            {"name": "Thomas Martelli Sr.", "title": "Co-founder (deceased, two years ago)", "notes": None},
        ],
        "notes": (
            "Financially over-extended: no dividend in four quarters, a high-powered loan to finish the "
            "new product, history if it does not score major cash by quarter's end. The 'Back Door' "
            "think tank's Global Dreamchips (BTL + skillsoft personality overlays: Jack the Ripper, "
            "Cleopatra, Genghis Khan) are illegal even as prototypes; Ares passed on the pitch, so Urlan "
            "took it to the UCAS military. Tee Hee wiped all the research data; the only backup is on "
            "Junior's desktop (I/OP-6). Board of directors meeting Friday 9:30 a.m. -- Junior's speech "
            "demanding Urlan's head for gross financial mismanagement is on his pocket secretary. "
            "Success ending: a record dividend of 113.34 nuyen per share. Failure: HSE names Booker "
            "Pengrave VP to oversee the acquisition. Matrix system map in the prep doc (p.54); the "
            "number on Roxanne's card (567-3272) is an unlisted SAN routed straight to her."
        ),
        "allies": ["Knight Errant Security Services"],
        "enemies": ["Hollywood Simsense Entertainment"],
    },
    {
        "name": "Hollywood Simsense Entertainment",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Hollywood, California Free State; UCAS division in Seattle",
        "summary": "Major producer of cheap, gory, porny simsense; own heavily armed security; premiere parties; suspected BTL maker",
        "description": (
            "A major producer of simsense players and chips. The Hollywood parent (President/CEO Yuri "
            "Tellenkov) makes educational disks under its Modern Life Simsense division (head Albert "
            "Yellowjacket), while the Seattle production and distribution company -- HSE UCAS, division "
            "head Joshua Bulter -- turns out numerous new entertainment chips every month, most of them "
            "pornographic or gory, beyond the reach of the Japanese Imperial State censorship boards in "
            "California. With its own Seattle studios and factories it does a booming business in the "
            "seediest products on the market. HSE maintains a large, heavily armed security force and "
            "special operatives who run large-scale operations in the Seattle area, plus a modest fleet "
            "of land and air patrol craft with considerable firepower. Famous for its premieres and "
            "parties; on the front page of the scream sheets at least once a week."
        ),
        "leadership": [
            {"name": "Yuri Tellenkov", "title": "President/CEO", "notes": None},
            {"name": "Joshua Bulter", "title": "Division Head, HSE UCAS (Seattle)", "notes": None},
            {"name": "Albert Yellowjacket", "title": "Division Head, Modern Life Simsense", "notes": None},
            {"name": "Booker Pengrave", "title": "Department head, rising 'Golden Boy'", "notes": "Running the Global acquisition scheme; VP if it works."},
        ],
        "notes": (
            "A corporate shakeup some months ago removed almost 20 percent of top management and left "
            "the company stronger, expanding into Quebec and the CAS. Raided five times in six months by "
            "Knight Errant and Lone Star on suspicion of producing BTLs -- all five raids found nothing. "
            "Its Seattle strategy is 'expansion and diversification': it wants Global Technologies' "
            "skillsoft division and used Junior Martelli and fixer Cooperman to steal the Dreamchips. "
            "Freya Goldenhair ran several snatch-and-dash jobs for HSE and torched something there last "
            "December over a grudge with Pengrave; Griffin was on their payroll at the same time; Flair "
            "was just 'retained' through a middleman to work on the Dreamchip processor. Party security: "
            "a street mage, a street samurai and two street cops at the door, four wage mages patrolling "
            "astrally."
        ),
        "enemies": ["Global Technologies"],
    },
    {
        "name": "Blood Rumblers",
        "org_type": "go-gang",
        "affiliation_contact_type": "Gang",
        "tier": 2,
        "headquarters": "InterCity 9 (Redmond)",
        "summary": "Go-gang that controls InterCity 9; taken over by 'Khan' (Cooperman) for a war on all of Redmond",
        "description": (
            "A Redmond go-gang that holds InterCity 9. Fixer Marcus Cooperman was long their primary "
            "fixer -- the bikers told him what they wanted and he jumped -- until he jacked the Genghis "
            "Khan chip, took over as 'Khan', and started giving the orders. Under Khan the Rumblers are "
            "spray-painting 'Blood Rules' over rival colors, shooting up the Red Hot Nukes' bar with a "
            "light machine gun from a moving bike, ambushing Crimson Crush enforcers, and riding openly "
            "through Crimson Crush turf."
        ),
        "leadership": [
            {"name": "Marcus Cooperman", "title": "'Khan' -- warlord (while the chip lasts)", "notes": "Dies when the chip is pulled."},
        ],
        "notes": (
            "Khan has persuaded the leaders of the Red Rovers, Eye-Fivers and Spike Wheels that combined "
            "they can control the whole Redmond Barrens, not just a stretch of highway. War council "
            "Wednesday night at the warehouse near Union Hill Road and 208th Avenue, then the horde "
            "sweeps into Redmond. Gang leader block (p.48): B5(6) Q4 S5 C2 I4 W4, Ess 2.55, Reaction "
            "4(6); Leadership 6, Bike 5; low-light cybereyes, dermal plating 1, radio, Wired Reflexes 1; "
            "armor jacket, FN-HAR and Ares Predator with smartlinks, Harley Scorpion, DocWagon. Leaders "
            "test morale (1D6, flee on a 1, -1 per leader down) once Khan falls; one running out "
            "screaming 'It's a set-up!' turns the horde on itself."
        ),
        "allies": ["Red Rovers", "Eye-Fivers", "Spike Wheels"],
        "enemies": ["Crimson Crush", "Brain Eaters", "Red Hot Nukes", "Rusted Stilettos"],
    },
    {
        "name": "Red Rovers",
        "org_type": "go-gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Redmond highways",
        "summary": "Go-gang in Khan's pact; seen riding with Blood Rumblers chasing a car of Rusted Stiletto trolls",
        "description": "A Redmond go-gang, one of the three (with the Eye-Fivers and Spike Wheels) whose leaders 'Khan' persuaded to join the Blood Rumblers' war on the Barrens. Now something you don't see every day: Red Rovers riding with Blood Rumblers.",
        "notes": "Uses the gang leader block on Dreamchipper p.48. The pact dissolves in gunfire if the war council goes wrong.",
        "allies": ["Blood Rumblers"],
    },
    {
        "name": "Eye-Fivers",
        "org_type": "go-gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Interstate 5 corridor",
        "summary": "Go-gang in Khan's pact",
        "description": "A go-gang named for its stretch of Interstate 5, one of the three that joined 'Khan's' combined horde against the gangs of Redmond.",
        "notes": "Uses the gang leader block on Dreamchipper p.48.",
        "allies": ["Blood Rumblers"],
    },
    {
        "name": "Spike Wheels",
        "org_type": "go-gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Redmond highways",
        "summary": "Go-gang in Khan's pact",
        "description": "A go-gang, one of the three that joined 'Khan's' combined horde. Chrome and steel steeds readied in the blasted lots around the Union Hill warehouse for a thunder ride into the heart of the Barrens.",
        "notes": "Uses the gang leader block on Dreamchipper p.48.",
        "allies": ["Blood Rumblers"],
    },
    {
        "name": "Brain Eaters",
        "org_type": "gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Redmond Barrens",
        "summary": "Redmond street gang whose wall symbol the Blood Rumblers paint over with 'Blood Rules'",
        "description": "A Redmond Barrens street gang. Its gang symbol normally adorns walls in its turf -- until the Blood Rumblers spray 'Blood Rules' over it.",
        "notes": "One of the local gangs in the path of Khan's horde. No stats given; use the Street Gang Member archetype.",
        "enemies": ["Blood Rumblers"],
    },
    {
        "name": "Red Hot Nukes",
        "org_type": "gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Redmond Barrens (a favorite bar with no front window any more)",
        "summary": "Dwarf street gang ('those midgets') whose hangout the Rumblers shoot up",
        "description": "A dwarven street gang of the Redmond Barrens. A Blood Rumbler on a bike sprayed flechettes from a light machine gun through the front window of their favorite hangout; the Nukes are not going to like it.",
        "notes": "No stats given; use the Street Gang Member archetype with dwarf modifiers. Likely to want revenge on the Rumblers -- or on whoever the runners point them at.",
        "enemies": ["Blood Rumblers"],
    },
    {
        "name": "Trogs",
        "org_type": "gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Seattle streets",
        "summary": "Ork and troll street gang; Ferret's few 'friends'",
        "description": "An Ork and Troll street gang. Not many people like the snitch Ferret, but he has a few 'friends' among the Trogs who could make life rough for anyone who hurts him.",
        "notes": "Use the Street Gang Member archetype with ork/troll modifiers. Ferret is a small fish; the Trogs only matter if the runners kill him and word gets out.",
    },
    {
        "name": "Blood Runners",
        "org_type": "go-gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Seattle south side",
        "summary": "South-side go-gang once led by Quetzel Allar",
        "description": "A south-side Seattle go-gang. Quetzel Allar joined it off the street after the food riots of 2040, rose to undisputed leader by 19, and was forced out of the leadership late last year.",
        "notes": "Not to be confused with the Blood Rumblers of Redmond. Julius Strouther first met Quetzel while she ran with the Blood Runners.",
    },
    {
        "name": "University of Seattle",
        "org_type": "university",
        "tier": 2,
        "headquarters": "University of Seattle campus, Seattle",
        "summary": "'US' -- where Tee Hee, Junior, Julius Strouther studied and Flair taught Matrix geometry",
        "description": (
            "Seattle's university. Its graduating class of '48 produced Tee Hee, the brightest and most "
            "sought-after decker in the city; Dr. Norris Hendrix ('Flair') pioneered Matrix geometry "
            "here before his coma and dismissal; Julius Strouther was a brilliant, driveless student; "
            "Thomas Martelli Jr. studied business and was expelled three weeks before graduation for "
            "mauling a professor."
        ),
        "notes": "Corporate recruiters (Aztechnology among them) hunt the graduating deckers. Flair is bitter at the university; Tee Hee still wanders the campus when he forgets to pay his rent.",
    },
]

LOCATIONS = [
    {
        "name": "Reno's",
        "location_type": "nightclub",
        "district": "Downtown",
        "security_level": "Patrolled / Commercial",
        "summary": "The downtown club where runners go to get hired; no heavy hardware past the Ork doorman",
        "description": (
            "In the heart of Downtown Seattle, the place to make contacts with prospective employers: "
            "rockerboys whipping the crowd, deep throbbing bass and synth-guitar over 16 MaxMaster "
            "speakers, a dance floor that is a madhouse an hour before the place is jumping. A "
            "mangled-handed Ork doorman takes crumpled nuyen at the door and checks IDs against "
            "bluffing juves; a Troll bouncer clears them out by the armload. Every runner in Seattle has "
            "the same idea, so style is all."
        ),
        "notes": (
            "Any weapon with Concealability under 8 or armor other than leather bars a character and "
            "draws a Lone Star patrol. Roxanne Wunter recruits here (Sunday night) with her samurai "
            "bodyguard at the bar; she walks three blocks to a Global-logo helicopter afterwards. "
            "Ferret watches from the shadows."
        ),
    },
    {
        "name": "The Banshee",
        "location_type": "bar",
        "district": "Redmond Barrens",
        "security_level": "Low Security",
        "summary": "Quiet, private business bar: weapons check, gate, white-noise tables, a soundproof back room with a hermetic circle",
        "description": (
            "An unremarkable brick front with a broken neon sign ('Ba sh e'), a heavy steel door and no "
            "windows. Inside, a narrow hall with a weapons-check window (a gritty dwarf racks the heavy "
            "gear; handguns stay with you) and a steel-mesh gate operated from the other side. Not an "
            "'in' place but quiet and private: a wet tile floor, stale beer, canned last-year hits from "
            "decaying speakers to cover conversations, big padded-vinyl tables with a white-noise "
            "generator bolted to each, scantily clad waitresses, three bouncers and Tinker the head "
            "barman. Behind a Troll-guarded door is the nicer back bar (polished redwood, better stock, "
            "soundproofed, rating-5 noise generators), and off it a rentable back room with a legless "
            "vinyl couch, a poker table, a rating-10 white-noise generator and a rating-7 hermetic "
            "circle. Owner Martin Jacazziman is out of town."
        ),
        "notes": (
            "Fixers and low-level execs use it to get away from the office; heavy hitters on occasion. "
            "Front room: rating-3 noise generators (lip readers beat them). Bar map p.36: weapons "
            "storage (Gus), entrance hall (one razor-armed bouncer locked in with the clients), locked "
            "office (Jacazziman's mahogany desk, 150 Mp computer of tax records, Ares Predator in the "
            "bottom drawer), tap room, back bar with a Defiance T-250 under the counter, Uzi IIIs "
            "holstered at each end of the front bar. Staff: Tinker (acting manager), Gus (dwarf, weapons "
            "check -- Junior's traitor), Mackie (troll, back-bar door), two human bouncers, three "
            "waitresses. Junior's Monday-night ambush kills both human bouncers; the team trashes the "
            "bar. Urlan rents the back room by the minute for the briefing."
        ),
    },
    {
        "name": "Breadboard Quaff and Stuff",
        "location_type": "bar",
        "district": "Cascade Road, Redmond/Bellevue border",
        "security_level": "Low Security",
        "summary": "Decker hangout tavern serving soyjack breakfasts; Flair's regular haunt; strangers without datajacks get stared at",
        "description": (
            "A small tavern on Cascade Road, a side street in a residential neighborhood near the "
            "Redmond/Bellevue border, three doors from Orion's Organic Grocery. Busy at breakfast in solid "
            "and liquid forms: a single bar the length of the room, a cook flipping soyjacks and frying "
            "synth-eggs, a mountain of a woman with twin datajacks behind her ear pouring soykaf ('Well "
            "boys, what'll it be?'). Regulars whisper and point at newcomers, especially ones without "
            "datajacks. Its disposable lighters have circuit diagrams worked into the body."
        ),
        "notes": (
            "Etiquette (Street) or Interrogation TN 5 about Flair; a 50-nuyen donation adds a success. "
            "Nobody remembers Tee Hee ('the Kid who's been staying with Flair'). Flair has not been seen "
            "awake before noon in three years; the proprietor will point him out when he comes in for "
            "food for two."
        ),
    },
    {
        "name": "Orion's Organic Grocery",
        "location_type": "convenience store",
        "district": "Cascade Road, Redmond/Bellevue border",
        "security_level": "Low Security",
        "summary": "Mom-and-pop grocer with caged registers and a pungent organic corner; 'Orion's Special Blend' herb tea",
        "description": (
            "A mom-and-pop grocery on Cascade Road: a buzzer at the single door, two caged and locked "
            "checkout registers, four aisles of canned goods and a small organic section whose barrage of "
            "smells gives the shop its name. A small gray-haired lady shuffles up from the back: 'Hello, "
            "hello, hello. How can I help you today?'"
        ),
        "notes": "TN 4 to ask after Flair. Its 'Orion's Special Blend' tea in Tee Hee's desk is the clue that points here.",
    },
    {
        "name": "Dr. Bob's Quickstitch",
        "location_type": "hospital",
        "district": "Fourth (Redmond)",
        "security_level": "Patrolled / Commercial",
        "summary": "Seattle's institution for quick, quiet repair work; barely trained medics, neuro-stun panic rooms, 100 nuyen per ten minutes",
        "description": (
            "Something of an institution in Seattle: Quickstitch teams of barely trained medics work "
            "long hours for little pay on the front line of the city's constant fighting and have an "
            "excellent reputation among runners for quick and quiet repairs. Disinfectant hangs heavy "
            "(no ultrasonic disinfectors here), dilapidated furniture and tasteless wall hangings in the "
            "waiting room, a harried nurse behind plexiglass, a number server, squatters hoping for the "
            "free service handed out at the end of the day, and a row of six private rooms at the back."
        ),
        "notes": (
            "Staff: head doctor Wilmoth, three doctors, six nurses, two aides; five guards (three mercs, "
            "a street mage, a street samurai). Every room has a hidden panic button that locks the door "
            "and floods it with Neuro-Stun VIII. Nothing happens if you take a number; a credstick in the "
            "slot opens negotiations at 10 nuyen a question (Etiquette (Street)/Interrogation TN 5; four "
            "successes brings a doctor in ten minutes). Dr. Wilmoth: 100 nuyen per ten minutes flat plus "
            "500-1,200 per answer (menu p.30). Freya Goldenhair is in room 6 behind a magical barrier "
            "and listens to the negotiation astrally."
        ),
    },
    {
        "name": "Global Technologies Building",
        "location_type": "corporate facility",
        "district": "Bellevue",
        "security_level": "Corporate Standard",
        "controlling_org": "Global Technologies",
        "summary": "Blue neon sign, Armorlite doors, marble lobby, fourth-floor think tank; Knight Errant rent-a-cops",
        "description": (
            "Global's only office: a blue neon sign over Armorlite acrylic doors, a polished marble lobby "
            "with a guard station, elevators and stairs, and the Back Door 'think tank' on the fourth "
            "floor where the Dreamchips were kept. Guards in Lone Star-style uniforms are Knight Errant "
            "hires. A parking lot across the street with a row of dumpsters."
        ),
        "notes": (
            "The prologue heist ('Trashed', pp.4-6): Val's Airstar lands in the intersection, Freya "
            "sleeps the lobby guard, Griffin kills two Knight Errant guards, a dwarf sergeant with thermal "
            "eyes shoots Freya on the stairs, and Cooperman flies off leaving her in a dumpster. The "
            "Matrix map (p.54) is in the prep doc; SM-8 is a self-destruct. Junior's desktop (I/OP-6) "
            "holds the only Dreamchip research backup (500 Mp)."
        ),
    },
    {
        "name": "Pengrave's Condo (Queen Anne Hill)",
        "location_type": "penthouse",
        "district": "Queen Anne Hill",
        "security_level": "Corporate Standard",
        "controlling_org": "Hollywood Simsense Entertainment",
        "summary": "16th-floor condo where HSE throws its premiere party; pool, lobby of the elite, real food",
        "description": (
            "A tower on Queen Anne Hill bathed in twin searchlights for the HSE premiere: revelers on the "
            "front steps, the powerful holding court in the lobby, military types in the heated pool, "
            "little groups gossiping on the grounds, and on the 16th floor a mirrored strobe-and-laser "
            "entryway opening into a living room full of dancers, a kitchen of real food (chicken, tuna, "
            "turkey, real coffee), simsense players in the bedroom running HSE's bloody new release, and "
            "a picture window over the bay through whispers of fog."
        ),
        "notes": (
            "Invitations (from Junior's body, Flair's flat, or 100 nuyen each on the street) get you in as "
            "honored guests; otherwise carry liquor for a dwarf with a lap computer and take the stairs. "
            "Security patrol at the door (mage, samurai, two street cops) and four wage mages astrally; "
            "nothing bigger than a hold-out. Eavesdropping table p.39 (2D6 per half hour). Pengrave and "
            "'Cleo' leave in a rented black Mitsubishi Nightsky for the docks and his Aztech Nightrunner."
        ),
    },
    {
        "name": "The Lion's Den Warehouse",
        "location_type": "safehouse",
        "district": "Union Hill Road and 208th Avenue (Redmond outskirts)",
        "security_level": "No Security / Barrens",
        "controlling_org": "Blood Rumblers",
        "summary": "Cooperman's abandoned warehouse base amid blasted lots; Khan's war council; manhole to the sewers",
        "description": (
            "An old, long-unused warehouse in the middle of a lot of nothing near Union Hill Road and "
            "208th Avenue, its ceiling a maze of girders and lights. Bare manager's office with a hole "
            "knocked into the warehouse, a receiving clerk's office with the remains of a small fire and "
            "a meal, a scarred reception counter, and an entrance hall blocked by tipped-over vending "
            "machines that a person can crawl under unseen. Outside: blasted vacant lots crawling with "
            "go-gangers on chrome and steel steeds."
        ),
        "notes": (
            "Cooperman's base since the Global run (Val landed the Airstar on the tarmac here). A manhole "
            "near the north wall (Intelligence TN 4 to spot) is his escape hatch into sewers big enough "
            "to run crouched, ending two miles away. Wednesday night: Khan on a box haranguing eight gang "
            "leaders; four Stealth-4 tests to get through the hordes (Negotiation TN 8, or 6 in gang "
            "colors); 1D6 bikers arrive eight turns after shooting starts. Pulling Khan's chip kills "
            "Cooperman."
        ),
    },
    {
        "name": "Seattle Waterfront Docks (marina)",
        "location_type": "transportation hub",
        "district": "Waterfront",
        "security_level": "Patrolled / Commercial",
        "summary": "Marina and piers where Pengrave keeps his Aztech Nightrunner; the end of the Nightsky chase",
        "description": "The Seattle waterfront's marina area and piers, where a rented Mitsubishi Nightsky can pull up and its passengers walk down to a private boat.",
        "notes": (
            "Chase table 'Fish and Chip' p.41 (TN 4). The loyal driver (Car 5) tries to shake and then "
            "sideswipe pursuers. Pengrave runs down the pier leaving Val hobbled by gown and heels; "
            "captured, he bargains Griffin, then Cooperman, then nuyen, then anything but Val."
        ),
    },
    {
        "name": "The Kingdome",
        "location_type": "landmark / monument",
        "district": "Downtown",
        "security_level": "Patrolled / Commercial",
        "summary": "Seattle's stadium: urban brawl games, pro biker shows",
        "description": "Seattle's domed stadium. Urban brawl games draw the crowds (Tee Hee had tickets to last week's); bikers perform as pros here; the Mariners' fans storm the outer bunkers when they win.",
        "notes": "General world texture from the Dreamchipper clues and news handouts. The Cobras train 'on The Island'; the 'Ratchet Squad' were all but wiped out in the Olympic Mountains.",
    },
]

NPCS = [
    {
        "name": "Urlan Manes",
        "role": "Ute president of Global Technologies; the runners' employer; decker, hard but fair",
        "archetype": "Corporate Executive",
        "title": "President/CEO, Global Technologies",
        "race": "Human",
        "gender": "Male",
        "nationality": "Ute (Native American)",
        "organization": "Global Technologies",
        "connection": 3,
        "description": (
            "A huge Indian in a fringed leather jacket, breeches and loincloth, a bead-and-feather bone "
            "vest over a massive bare chest, and thick-soled moccasins beaded with a snake trapped under "
            "his left sole and a green bird taking flight up his right calf. Always wears some Indian "
            "apparel to remind others of his heritage. Constantly in control of his emotions, his face a "
            "blank mask; courteous and polite even in the face of hostility. 'Son of Isheer Many-Manes.'"
        ),
        "background": (
            "A full-blooded Ute interested in computers since he could reach a keyboard; raised in what "
            "used to be Utah, schooled at UCLA, in Seattle ever since his first job. Founded Global with "
            "his best friend Thomas Martelli Sr. 15 years ago and led the skillsoft division; inherited "
            "most of Martelli's shares and the CEO chair two years ago, which set Junior against him. "
            "Once broke Junior's arm in a tussle. Loyal to his employees to a fault -- firing anyone is "
            "traumatic -- and grooming Tee Hee like a son."
        ),
        "notes": (
            "Offers 30,000 nuyen per runner (up to four) per intact chip, adjusted by the team's conduct "
            "(-1,000 rude to Roxanne, -1,000 asked directions, -2,000 no Ferret info, -5,000 bar fight; "
            "+1,000 hesitant-but-interested, +1,500 Ferret's number), Opposed Negotiation at 500 per net "
            "success, 1,000 per chip destroyed if the team wins a success, 2,000 advance each, 5,000 "
            "bonus for Tee Hee's safe return. Will not say what the chips are (illegal even as "
            "prototypes; prison if it leaks). Absent until payment; work through Roxanne. Stats: B6 Q3 "
            "S5 C4 I5 W4, Ess 4; Computer 5, Computer Theory 7, Negotiation 5, Leadership 4, Etiquette "
            "(Corporate) 5, Firearms 4; Hacking pool 9; datajack, 100 Mp headware, program carrier; "
            "Ruger Super Warhawk (explosive), lined coat, Toyota Elite, Aztech Nightrunner boat. Rumor: "
            "he and Roxanne have a thing."
        ),
        "contact_skills": ["Global Technologies resources and skillsoft expertise", "Corporate and tribal contacts (City Official, Tribal Chief, Mr. Johnson)"],
    },
    {
        "name": "Roxanne Wunter",
        "role": "Global's Back Door division head and the runners' handler; stylish, curt, carries a torch for Urlan",
        "archetype": "Corporate Executive",
        "title": "Division Head, Back Door Technologies, Global Technologies",
        "race": "Human",
        "gender": "Female",
        "organization": "Global Technologies",
        "connection": 3,
        "description": (
            "Easy to look at: a military-cut corporate suit, lots of flashy jewelry (her earring alone "
            "cost more than most runners make in six months), every strand of hair in place. A stylish, "
            "slightly compulsive dresser who keeps a fully stocked closet at work. Commands silent "
            "authority and has not had to shout in years; curt, efficient and businesslike, and sullen "
            "and angry when her cultured image slips. Drinks a foaming blue concoction."
        ),
        "background": (
            "Born on the east side of Los Angeles to a family poverty still grips; a rabble-rouser with "
            "good grades, honors scholarship at Berkeley, then Seattle: security manager at Back Door "
            "Systems and, by Thomas Martelli Sr.'s last official act, division head. Some say she moved "
            "up too fast; none say it to her face. Loyal to the company and to Urlan, for whom she carries "
            "a torch he is unaware of."
        ),
        "notes": (
            "Recruits at Reno's as 'uh... Johnson'; her plastic business card number 567-3272 is an "
            "unlisted Global SAN routed straight to her. Won't discuss anything on the phone. Fights "
            "alongside the team at The Banshee and takes reasonable orders from the team leader; if she "
            "dies, she dies ('If she's a goner, waste her'). Retrieves the Dreamchip backup from Junior's "
            "desktop herself if told. Stats: B2 Q5 S2 C6 I5 W5, Ess 5.6; Etiquette (Corporate/Street) 5, "
            "Negotiation 4, Computer 3, Firearms 3; Hacking pool 8; datajack, retractable razors; Colt L36 "
            "(AP rounds), armor clothing, Eurocar Westwind 2000, pocket secretary."
        ),
        "contact_skills": ["Global Technologies jobs and payment", "Skillsoft industry intel"],
    },
    {
        "name": "Thomas Martelli Jr.",
        "role": "'Junior' -- goblinized son of Global's founder; vicious Ork exec plotting the HSE takeover",
        "archetype": "Corporate Executive",
        "title": "\"Junior\", Division President, Martelli Entertainment (Global Technologies)",
        "race": "Ork",
        "gender": "Male",
        "organization": "Global Technologies",
        "connection": 2,
        "description": (
            "Easily six and a half feet and built like a linebacker, ugly even for an Ork: knobby dermal "
            "plates make his warty skin stick up at odd angles, enormous ears hung with earrings, a "
            "pencil-sized 'Orkish toothpick' always in his mouth. Three-piece suit and walking cape for "
            "'company' business, biker leathers with chrome chains and spikes otherwise. Laughs like a "
            "dying hyena. Starts fights by accusing people of staring at him -- and he is usually right."
        ),
        "background": (
            "Popular and promising until he goblinized at 13; grew up rough and mean, weeks at a time in "
            "the Ork Underground, then surprised everyone by studying business at the University of "
            "Seattle -- expelled three weeks before graduation for mauling a professor. His father hired "
            "him at Martelli Entertainment, where he clawed his way to president, and then willed most "
            "of Global's stock to Urlan Manes, dated just after the goblinization. Bitter ever since "
            "Global swallowed Martelli."
        ),
        "notes": (
            "Recruited Tee Hee with a credstick and a souped-up Fairlight Excalibur; brought in Pengrave "
            "and Cooperman; hides the Dreamchip research backup on his desktop; hires Ferret and other "
            "independents to shadow Urlan's staff (his private line is 567-2384). Crashes the Banshee "
            "briefing with two suited Ork bodyguards, then ambushes it Monday night with three "
            "go-gang-leathered bodyguards, three Ork mercs in the back room, Gus the turncoat dwarf, and "
            "two offensive grenades; breaks for his Westwind when down to two metas. Loyal only to money, "
            "Junior, and his Harley. His pocket secretary is the jackpot: the whole conspiracy, 'Val is "
            "running Cleo, and Griffin's messed up with Jack the Ripper', his board speech, and his Global "
            "access codes. Stats: B6(9) Q4 S8(9) C1 I3 W3, Ess 0.3, Reaction 3(7); Armed Combat 5; "
            "cyberarm (smartlink, spur, +1 Str), dermal plating 3, Wired Reflexes 2; armored vest with "
            "plates, Browning Max-Power and Enfield AS7 smartguns, monofilament whip, Westwind 2000, "
            "Harley Scorpion with two AK-97s on firmpoints; DocWagon Gold. Allergies: iron, sunlight."
        ),
    },
    {
        "name": "Tee Hee",
        "role": "Global's giggling genius decker; the thieves' inside man; hiding in Flair's flat",
        "archetype": "Corporate Decker",
        "title": "Decker, Back Door think tank, Global Technologies (turned inside man)",
        "race": "Human",
        "gender": "Male",
        "organization": "Global Technologies",
        "connection": 2,
        "description": (
            "Sides of the head shaved, the rest a severely spiked neon-blue mohawk; wardrobe changes "
            "weekly (neo-Hunnish one week, subdued Amerindian the next), expensive accessories mixed with "
            "junk. Constantly dazed, glassy-eyed, slack-grinned -- animated only about computers. In the "
            "Matrix his fingers fly, he rocks to an unheard rhythm and giggles near-constantly, hence the "
            "name. Naive, forgets everything (including his rent, and the way to the store)."
        ),
        "background": (
            "Best and brightest of the University of Seattle class of '48, disliked as an intellectual "
            "snob, recruited by every major corp; turned down an outstanding Aztechnology offer and "
            "signed with Global after one office visit. Drove the Colt L36-Mark VII. Loyal to the Matrix "
            "and computers and nothing else; people and companies matter only as far as they keep him "
            "jacked in and interested."
        ),
        "notes": (
            "Evicted two weeks ago; sleeping on the floor of Flair's flat jacked in. Milkin' Tee (p.27, "
            "Negotiation 2 / Interrogation 3, pick one): the heist, Junior's recruitment, that the chips "
            "are unstable personality chips ('leave them in too long and you can lose yourself forever'), "
            "and that the only R&D backup is on Junior's desktop. Can draw a Global system map if "
            "convinced (and will ask Urlan why later). Killed by Junior's boys if left unescorted -- Flair's "
            "flat is torched before Knight Errant arrives. Stats: B3 Q4 S2 C4 I6 W2, Ess 3.6; Computer "
            "9, Computer B/R 6, Computer Theory 6; Hacking pool 14; datajack, 200 Mp headware, program "
            "carrier; Cyber-6 deck (Level 2 Response Increase): Bod 6, Evasion 8, Masking 6, Sensors 8, "
            "Attack 4; Beretta 101T, armor clothing."
        ),
        "contact_skills": ["Elite decking and skillsoft design", "Global Technologies system knowledge"],
    },
    {
        "name": "Dr. Norris Hendrix",
        "role": "'Flair' -- fallen Matrix-geometry professor and old-school decker sheltering Tee Hee",
        "archetype": "Street Decker",
        "title": "\"Flair\", former University of Seattle professor of Matrix geometry",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "A small, gray-haired man who looks like an ancient student: jeans, engineer boots, a "
            "University of Seattle sweatshirt, long hair in a ponytail, a bright blue rucksack over one "
            "shoulder. A man of style and knowledge, crotchety when cornered, never awake before noon. "
            "Lives in a one-room third-floor flat done over in Late-American Decker -- stacks of disks, "
            "trade journals and printouts, a hot plate, a cyberdeck and a mug that says 'Flair'."
        ),
        "background": (
            "One of the great minds of Matrix geometry and one of the original shadowrunners, making and "
            "breaking the best IC of his day as Flair, until massive neural feedback on an independent "
            "run against an up-and-coming Aztechnology put him in a coma for two years. Woke to find "
            "technology had passed him; the university let him go after a year; bitter at life and at "
            "US, he runs the shadows to eat. Now looking for a final score to retire on -- HSE just "
            "'retained' him through a middleman (to work on the Dreamchip processor, though he does not "
            "know it yet) and he has been flashing the advance and a pair of party tickets downtown."
        ),
        "notes": (
            "The only man who ever held Tee Hee's attention; wants the boy kept alive and argues against "
            "turning him over. Etiquette (Street) TN 4 then Psychology TN 4 to befriend; Negotiation or "
            "Interrogation TN 5 to crack. Stats: B2 Q3 S1 C4 I5 W5, Ess 4.6; Computer 9, Computer Theory "
            "8, Electronics 5; Hacking pool 13; Fuchi Cyber-7 with Level 3 Response Increase (Bod 10, "
            "Evasion 8, Masking 8, Sensors 10, Analyze 7, Attack 7, Browse 8, Deception 8, Decrypt 10, "
            "Relocate 10, Shield 10, Slow 7); Beretta 101T, armored sweatshirt, used Yamaha Rapier. His "
            "computer is not connected to the Matrix. Not seen again after the fire if Tee Hee dies."
        ),
        "contact_skills": ["Old-school decking and IC theory", "University of Seattle alumni network", "Breadboard regulars"],
    },
    {
        "name": "Marcus Cooperman",
        "role": "'Face' / 'the Historian' -- fixer to the go-gangs, now 'Khan' of the Blood Rumblers on a degrading chip",
        "archetype": "Fixer",
        "title": "\"Face\", \"the Historian\"; fixer; self-styled Khan of the Blood Rumblers",
        "race": "Human",
        "gender": "Male",
        "nationality": "Texan",
        "organization": "Blood Rumblers",
        "connection": 5,
        "description": (
            "Only five-foot-four, a fashion follower always in the current fad, dark hair short and "
            "slicked back, a slow Texas drawl that cracks when he gets excited. A gravelly voice on a "
            "headset with all the warmth of grinding metal. Obsessed with power he could not say what "
            "he would do with; egocentric, will not be shown up; a self-styled history expert -- "
            "especially medieval, especially Genghis Khan -- who punctuates every point with an "
            "anecdote. His cybereyes and ears record constantly for posterity, the records kept in "
            "several secure locations. Never seen without bodyguards."
        ),
        "background": (
            "Born rich in Texas; both parents goblinized in 2021 -- his father died in the change and his "
            "mother lingered three years on machines his father's will forbade him to switch off, until "
            "they all 'mysteriously' failed at once. Lost the rest of the fortune in ten years, fled his "
            "creditors, and sprang up in the Seattle Barrens as an information broker with an uncanny ear "
            "to the street; contacts with every go-gang and most of the syndicates, favors owed by the "
            "powerful. The Global run was a departure: he had to have the Khan module."
        ),
        "notes": (
            "Paid his crew in stolen chips and kept Khan; 'Now I am the Khan. Now I build my empire.' "
            "The patchwork Khan chip is degrading fast in a weak-willed user; by Wednesday he has lost "
            "his grip on reality, standing on a box in the Lion's Den shouting orders. Leave a message at "
            "any Seattle hot spot and he finds you -- except he has returned no calls for weeks. Removing "
            "his chip discharges a lethal jolt into his brain. Stats: B2 Q3 S3 C4 I6 W3, Ess 2.2, Reaction "
            "4(6); Etiquette (Corporate/Street) 8, Negotiation 6, Military Theory (Mongol Hordes), "
            "Sociology (History) 4, Computer 4; cybereyes with camera, cyberears with recorder, toxin "
            "filter 4, Wired Reflexes 1; Fichetti Security 500, Uzi III, smoke grenades, lined coat, "
            "Harley Scorpion. Khan chip adds Leadership 8, Etiquette (Tribal) 7, Military Theory 6."
        ),
        "contact_skills": ["Go-gang and syndicate fixer (Blood Rumblers especially)", "Information broker with an ear to the street", "History buff"],
    },
    {
        "name": "Freya Goldenhair",
        "role": "Elven mage abandoned on the Global run; healing at Dr. Bob's and out for Cooperman's blood",
        "archetype": "Street Mage",
        "title": "Elven mage (freelance, Sinsearach)",
        "race": "Elf",
        "gender": "Female",
        "age": 43,
        "connection": 4,
        "description": (
            "Looks about twenty: long thick hair of honey gold, brown eyes, a perpetual grin, full "
            "layered gowns with loose sleeves, gold chains of every length accentuating figure, face and "
            "hands; thick moccasins on a run, matching slippers otherwise. Easy to like, slow to anger "
            "and slower to forgive; gives strangers the benefit of the doubt until they earn distrust; "
            "puts the mission and her partners before her own safety. Swears by the Blessed Lady. Mild "
            "allergy to plastic."
        ),
        "background": (
            "Forty-three, loves the woods and spends what time she can with her people at Sinsearach; "
            "runs the shadows for the thrill. Highly sought and expensive -- only fixers with the best "
            "connections can reach her -- with several unscathed snatch-and-dash jobs for Hollywood "
            "Simsense until the shakeup, and a payback 'light show' at HSE last December over Pengrave. "
            "Shot in the shoulder on the Global stairs, barriered the door, held the lobby, and watched "
            "Face wave from the rising chopper. 'It's not over, Face. You're mine now.'"
        ),
        "notes": (
            "Room 6 at Dr. Bob's behind a magical barrier; eavesdrops astrally on the team's talk with "
            "Wilmoth and docks half his take from her bill. The only source who connects Pengrave, "
            "Griffin, HSE, Cooperman and Val (answers p.31). May join a polite team for the run -- start "
            "her with a moderate wound; a rude team gets its information anyway and a lesson in manners "
            "later. Stats: B3 Q5 S2 C7 I6 W5, Ess 6, Magic 6; Sorcery 6, Conjuring 5, Athletics 5, "
            "Negotiation 4, Etiquette (Street) 4; Astral pool 18. Spells: Barrier 4, Clairvoyance 4, "
            "Control Thoughts 5, Heal Moderate Wounds 4, Invisibility 6, Mask 4, Power Bolt 5, Sleep 5. "
            "Gear (not at the clinic): Colt L36 (explosive), reusable Barrier fetish (calfskin glove) and "
            "Power Bolt fetish (ivory wand), Eurocar Westwind 2000, DocWagon Gold, tres chic clothes."
        ),
        "contact_skills": ["Hermetic magic for hire (expensive)", "Sinsearach elven contacts", "HSE dirt"],
    },
    {
        "name": "Griffin",
        "role": "Corporate razor running the Jack the Ripper chip -- the Redmond fog killer",
        "archetype": "Street Samurai",
        "title": "Corporate bodyguard / samurai; 'Jack' while the chip is in",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": (
            "Not a big man. Stylized dark corporate suits in muted reds and grays, black T-shirts and real "
            "leather wingtips, all tailor-made to mirror his current employer; a dark red walking cape "
            "and gloves in the fog. Glossy black cybereyes that glow pale yellow in high humidity. "
            "Well-read, restrained, hates loud noises (always a silencer, never a grenade), radiates the "
            "air that events are beneath his concern -- except in the Barrens, where he turns edgy and "
            "mean. As Jack: friendly and outgoing by day, a raving madman at night, talking constantly, "
            "razors out, roaring with laughter at every wound. 'Die. Die, tramp.'"
        ),
        "background": (
            "Born and raised in the Puyallup Barrens and sworn to rise out of it; a steady if "
            "unspectacular career as a corporate goon for most of Seattle's corps, bodyguarding by "
            "preference, an occasional run. Modest downtown apartment and safe spots in the better parts "
            "of town; avoids the Barrens. Worked for HSE around the time Freya did and came out of the "
            "shakeup better than ever. Killed the two Knight Errant guards in Global's lobby, then took "
            "the Jack chip as payment from Cooperman -- and stormed off in his Westwind when Face's "
            "outlaws got the drop on him."
        ),
        "notes": (
            "Nine prostitutes in four nights, throats slashed and bodies dissected, all in a 15-block "
            "area of Redmond; a joygirl heard him call himself Jack. Hunt him with bait (Stranger in "
            "the Night, p.49): he uses only his razors, never retreats, attacks whoever wounded him, and "
            "fights at reduced wound penalties. Pulling the chip leaves him permanently catatonic. Stats: "
            "B6 Q6(8) S6(8) C1 I5 W4, Ess 0.1, Reaction 5(9); Armed Combat (Edged) 6, Stealth 6, Firearms "
            "4, Interrogation 4; chipjack, thermographic/flare-comp cybereyes, muscle replacement 2, "
            "retractable hand razors, Skillwire 3, Wired Reflexes 2; stylish armor clothing; in the "
            "Westwind a block away: armor jacket, Browning Max-Power, Enfield AS7, H&K S variant SMG, "
            "smart goggles, DocWagon Gold. Jack chip adds Stealth 9, Etiquette 7, Psychology 6."
        ),
    },
    {
        "name": "Valerie Westerfield",
        "role": "'Val' -- broke freelance rigger with a run-down Airstar; 'Cleo' while the chip is in",
        "archetype": "Rigger",
        "title": "Freelance rigger (Hughes Airstar); 'Cleo' on the chip",
        "race": "Human",
        "gender": "Female",
        "age": 23,
        "connection": 3,
        "description": (
            "An attractive woman who hides it in baggy pants and a thick leather jacket or grease-stained "
            "coveralls, thick black hair cut short so it won't interfere with flying. As Cleo: long silk "
            "gowns slit to show her best feature, Pengrave's jewelry everywhere, gliding like a queen "
            "among peasants and choosing her escort with an outstretched hand. Cleo is witty, charming, "
            "hungry for political and economic power, and answers only to Cleo or Cleopatra."
        ),
        "background": (
            "Got her wish to be a rigger on her 16th birthday; shuttles from San Francisco to L.A., then "
            "a sudden move to Seattle she will not explain, and corp after corp with glowing references. "
            "Went independent six months ago with a run-down Hughes Airstar and takes every run she can "
            "to keep it flying. Flew the Global heist and got paid in the Cleo chip; jacked it out of "
            "curiosity at a private field on the south side."
        ),
        "notes": (
            "Cleo's plan: manipulate Pengrave into the VP chair, then take Global and HSE, then the "
            "simsense market, then the world. Fights to keep the chip (sedate or KO her); without it she "
            "remembers nothing since the heist and cheerfully sells out Cooperman: the Union Hill "
            "warehouse, 'Now I am the Khan', and a 200-nuyen-a-head lift there in the Airstar. Stats: B4 "
            "Q6 S3 C5 I5 W5, Ess 0.35, Reaction 5(7); Rotor Craft 5, Gunnery 6, Car 5, Electronics 5, "
            "Firearms 4; low-light cybereyes, high-frequency cyberears, datajack, retractable razors, "
            "vehicle control rig 2, Wired Reflexes 1; Ares Slivergun, Hughes Airstar with adaption rig, "
            "Yamaha Rapier. Cleo chip adds Etiquette (Corporate) 8, Leadership 6, Negotiation 6, "
            "Psychology (Seduction) 8."
        ),
        "contact_skills": ["Helicopter rigger for hire (Hughes Airstar)", "Rotorcraft repair"],
    },
    {
        "name": "Booker Pengrave",
        "role": "HSE's Golden Boy running the Global takeover; besotted with 'Cleo'; cyberarm with a built-in Predator",
        "archetype": "Corporate Executive",
        "title": "Department head, Hollywood Simsense Entertainment (Seattle)",
        "race": "Human",
        "gender": "Male",
        "organization": "Hollywood Simsense Entertainment",
        "connection": 3,
        "description": (
            "Plain: short hair, no distinguishing features, simple conservative clothes. Having the time "
            "of his life -- wheeling and dealing is in his blood; very animated, takes over conversations "
            "and cannot be shut up. 'Not much to look at, is he? Still, he sure knows how to party.'"
        ),
        "background": (
            "The right man in the right spot during HSE's shakeup: seized the initiative in his "
            "department, ended up running it, and became the Golden Boy. Not afraid to use muscle. "
            "Devised the Global scheme with Junior -- steal the prototypes, collapse Global at the board "
            "meeting, buy it for a song, keep the skillsoft tech, install Junior over simsense -- and "
            "hired Cooperman. A vice president's chair if it works. Fell under Cleo's spell in two days."
        ),
        "notes": (
            "Pretends not to know the runners at his party; calls security if pushed; boards a private "
            "elevator. Flees down the pier leaving Val; captured, trades Griffin, then Cooperman, then "
            "nuyen, then anything but Val, and delivers. His pocket secretary (on the boat or in the car) "
            "holds the Cooperman meeting details. Stats: B6 Q2 S3 C5 I4 W3, Ess 3.4; Etiquette "
            "(Corporate) 7, Psychology (Group) 4, Firearms 4, Stealth 4; blood filter 4, cyberarm with "
            "built-in Ares Predator and retractable razors, cyberears with recorder, datajack; Ares "
            "Predator, lined coat, Aztech Nightrunner at the dock, DocWagon Standard, contacts up to a "
            "Tribal Chief."
        ),
    },
    {
        "name": "Ferret",
        "role": "Gutter snitch and perfect tail; hired by Junior to watch Roxanne",
        "archetype": "Info Broker",
        "title": "Street snitch / tail for hire",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": (
            "A man of few if any redeeming qualities: shabby, unshaven, pox-marked, twisted features, "
            "long hair in a single dirty tail, greasy black synth-leathers. Inconspicuous and sneaky, he "
            "blends perfectly into Seattle's dirty underbelly and runs the moment he is approached, "
            "over terrain that will put pursuers on the pavement."
        ),
        "notes": (
            "Hired by phone for 100 nuyen to follow 'the blonde' from Reno's (and to The Banshee) and "
            "report by wrist phone. Interrogation TN 7 to spill; two successes gets Junior's private "
            "number, 567-2384. Junior plans to eliminate him afterwards. Stats: B2 Q6 S2 C1 I5 W3, Ess "
            "6, Reaction 5; Stealth (Urban) 6, Armed Combat 4, Unarmed 4, Etiquette (Street) 4; knife, "
            "Streetline Special, low-light binoculars, wrist phone. Friends in the Trogs."
        ),
        "contact_skills": ["Tailing and street surveillance", "Gutter gossip"],
    },
    {
        "name": "Gus",
        "role": "The Banshee's disagreeable dwarf weapons-check bouncer, turned by Junior",
        "archetype": "Bouncer",
        "title": "Weapons-check bouncer, The Banshee (turncoat)",
        "race": "Dwarf",
        "gender": "Male",
        "connection": 1,
        "description": "A gritty, very disagreeable dwarf who racks patrons' heavy gear behind the armor-glass window and gives the thumbs-up to open the gate. Mean to begin with, he has long chafed under his co-workers' remarks.",
        "notes": (
            "Junior's ace in the hole: on the wrist-phone signal he steps out with a sawed-off T-250 (10 "
            "spare shells) and shoots the gate bouncer, opens the door for Junior's boys, and goes for the "
            "men at the front bar, planning to loot the office afterwards. Fights to the death. Bouncer "
            "block: B5 Q4 S5 C1 I2 W2; Firearms 4, Armed 4; hand razors; armor clothing, Browning "
            "Max-Power."
        ),
    },
    {
        "name": "Mackie",
        "role": "Troll bouncer on The Banshee's back-bar door",
        "archetype": "Bouncer",
        "title": "Bouncer, The Banshee (back bar)",
        "race": "Troll",
        "gender": "Male",
        "connection": 1,
        "description": "The Troll who guards the door to The Banshee's back bar and ushers referred clients through. Does his duty -- nothing more, nothing less.",
        "notes": "Troll Bouncer stats plus a Browning Max-Power and an armored jacket. Rushes the nearest Ork when Junior hits; a little surprised by Gus, and does not much mind that the two humans got wasted.",
    },
    {
        "name": "Tinker",
        "role": "Head barman and acting manager of The Banshee",
        "archetype": "Bartender",
        "title": "Head barman / acting manager, The Banshee",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": "Rubs the wet bar with an even wetter rag, points to the back door with exaggerated slowness, and disassembles the audio controls when a processor blows. Runs the place while owner Martin Jacazziman is out of town.",
        "notes": "Bartender stats (SR1 p.163). Uzi IIIs holstered at each end of his bar. Helps fight off Junior's ambush -- if the runners fire first the staff may take them for the assassins.",
        "contact_skills": ["The Banshee's back room and its clientele"],
    },
    {
        "name": "Dr. Wilmoth",
        "role": "Head doctor at Dr. Bob's Quickstitch; sells information by the question; Freya's old friend",
        "archetype": "Street Doc",
        "title": "Head doctor, Dr. Bob's Quickstitch",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": "A mumbling street doc with a small, very well furnished office, a metal desk, a knee against the panic button, and a flat fee of 100 nuyen per ten minutes or any part thereof, not subject to negotiation. Anything he does or says costs extra.",
        "background": "A long-standing contact of Freya Goldenhair; the two trust and help each other. Spent eight hours mending the sorcerer and pronounced it a complete success.",
        "notes": "Street Doc stats (SR1 p.171). Answer menu p.30 (500-1,200 nuyen each); will only take the team to Freya once they leave their weapons in his office and promise no violence. Freya deducts half his take from her bill.",
        "contact_skills": ["Quick, quiet medical repair (Dr. Bob's Quickstitch)", "Who has been patched up lately (for a fee)"],
    },
    {
        "name": "Martin Jacazziman",
        "role": "Absentee owner of The Banshee",
        "archetype": "Club Owner",
        "title": "Owner, The Banshee",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": "Runs The Banshee from a small bare office with a mahogany desk, a 150 Mp computer buried in tax printouts, a love seat, and an Ares Predator in a chamois holster in the bottom drawer. Out of town for the whole adventure.",
        "notes": "Comes home to a trashed bar and two dead bouncers. Gus planned to loot his office.",
    },
    {
        "name": "Thomas Martelli Sr.",
        "role": "Co-founder of Global Technologies (deceased two years ago); willed the company to his best friend, not his son",
        "archetype": "Corporate Executive",
        "title": "Co-founder, Global Technologies (deceased)",
        "race": "Human",
        "gender": "Male",
        "organization": "Global Technologies",
        "connection": 1,
        "description": "Deceased. Built Global from an apartment operation into a small corporation with his best friend Urlan Manes, stealing most of the thunder; founded Martelli Entertainment to give his goblinized son a job.",
        "background": "Cared for Junior constantly after the goblinization at 13 and hired him despite the expulsion; his last official act promoted Roxanne Wunter; his will, dated just after Junior's change, left most of his stock to Urlan.",
        "notes": "Backstory only. The will is the wound the whole adventure turns on.",
    },
    {
        "name": "Quetzel Allar",
        "role": "Ex-leader of the Blood Runners go-gang turned freelance team leader; runs for the action",
        "archetype": "Street Samurai",
        "title": "Freelance runner / field leader (pregenerated)",
        "race": "Human",
        "gender": "Female",
        "age": 24,
        "connection": 3,
        "description": (
            "Tall and thin with a runner's build, blond hair in a single long braid, outrageous makeup to "
            "call attention to her ice-blue cybereyes. Quiet and reserved, a watcher who lets others lead "
            "the unimportant moments and issues orders without thought in a crisis. A mother hen to her "
            "team."
        ),
        "background": (
            "Born on the outskirts of Seattle in 2026; her middle-class parents were wiped out by the "
            "Crash of '29, her father killed in the 2040 food riots, her mother vanished a year later. "
            "Joined the Blood Runners off the street, undisputed leader by 19 running the south side, "
            "invested her loot, and was forced out late last year with a permanent middle lifestyle and "
            "numerous street contacts. Runs because she lives for it."
        ),
        "notes": (
            "Pregenerated PC usable as an NPC runner. Stats: B4 Q5 S3(4) C3 I5 W4, Ess 1.1, Reaction "
            "5(9); Firearms 5, Armed 4, Car 4, Leadership 3, Military Theory 3; right cyberarm with spur, "
            "Ares Slivergun and +1 Str, cybereyes (thermo, low-light, flare), datajack, smartlink, Wired "
            "Reflexes 2; FN HAR (scope, smartlink, gas-vent 3), Viper Slivergun, armored jacket, medkit, "
            "Westwind 2000, DocWagon Platinum."
        ),
        "contact_skills": ["Team leadership and heavy firepower", "South-side gang contacts (ex-Blood Runners)"],
    },
    {
        "name": "Evenstar",
        "role": "Political-activist rocker and songwriter who runs the shadows to pay the bills",
        "archetype": "Rocker",
        "title": "Rocker / runner (pregenerated)",
        "race": "Human",
        "gender": "Female",
        "connection": 2,
        "description": (
            "No flashy image: mini-skirts, moderately spiked leather jackets, red hair heavily styled, "
            "makeup rarely -- her voice must be of the common people. Moody, bright and glittery one "
            "moment and depressed the next; loud and overbearing in a hot debate; at her best with a cause "
            "to fight. 'The most good for the most people.'"
        ),
        "background": (
            "Born in the wrong century -- a pioneer of the music business a hundred years late. More "
            "writer than performer, with limited success peddling songs to other groups. Her second run, "
            "against Mitsuhama, turned from cakewalk to nightmare; only she and Julius Strouther got out."
        ),
        "notes": (
            "Pregenerated PC. Stats: B2 Q5 S1 C5 I5 W5, Ess 3.2, Reaction 5(7); Firearms 4, Bike 4, "
            "Psychology 4, Etiquette (Corporate/Street) 4, Musical Composition 6, Singing 3; datajack, "
            "hand razors, synthesizer link, voice modulator, Wired Reflexes 1; Enfield AS7, Ruger Super "
            "Warhawk, Harley Scorpion with concealed Uzi II, bug scanner, dataline tap, micro camcorder, "
            "synth-keyboard, tracking signals, DocWagon Gold. Contacts: Fixer, Media Promoter, Metahuman "
            "Rights Activist."
        ),
        "contact_skills": ["Songwriting and the rocker scene", "Activist / media contacts", "Surveillance gear"],
    },
    {
        "name": "Julius Strouther",
        "role": "Dwarf decker in pinstripes; first dwarf child born at Memorial Hospital (2018); Quetzel's old partner",
        "archetype": "Decker",
        "title": "Decker / runner (pregenerated)",
        "race": "Dwarf",
        "gender": "Male",
        "age": 32,
        "connection": 3,
        "description": (
            "A stylish, conservative dresser -- three-piece pinstripes in muted blues and grays, the tie "
            "his only splash of color -- who spends hours grooming beard and moustache (little on top to "
            "worry about). Cynical and grim on a run, patient because dwarves live long; off duty he "
            "drinks huge amounts with no visible effect. A fanatical team player who will risk his life "
            "for a partner."
        ),
        "background": (
            "A celebrity from birth in 2018 as the first child born at Memorial Hospital with the dwarfish "
            "form of UGE. Brilliant but driveless at the University of Seattle; refused lucrative offers, "
            "started his own computer business, and lost it to a mysterious midnight fire -- so took to "
            "the streets. Five years working with Quetzel since her Blood Runners days; survived the "
            "disastrous Mitsuhama run with Evenstar."
        ),
        "notes": (
            "Pregenerated PC. Stats: B3 Q2 S4 C2 I4 W5, Ess 3.6; Computer 5, Computer B/R 4, Firearms 4; "
            "Hacking pool 8; air filter 6, cyberears, datajack, 50 Mp headware, program carrier, "
            "smartlink; Fuchi Cyber-4 (Bod 6, Evasion 6, Masking 6, Sensors 6, Attack 6, Browse 5, Sleaze "
            "5, Smoke 4); H&K 227 smartgun, Walther Palm Pistol, armor vest with plates, electronics "
            "toolkit. Thermographic eyes, disease resistance, mild sunlight allergy."
        ),
        "contact_skills": ["Decking and computer repair", "Memorial Hospital / dwarf community minor celebrity"],
    },
    {
        "name": "Agarosi Tawtain",
        "role": "Coyote shaman stowaway; jack-of-all-trades runner in neon rainbow spikes; 'what will be will be'",
        "archetype": "Street Shaman",
        "title": "Coyote shaman / runner (pregenerated)",
        "race": "Human",
        "gender": "Male",
        "age": 21,
        "connection": 2,
        "description": (
            "Physically nondescript -- black hair, brown eyes -- so he wears the most outrageous neon "
            "blues and greens he can find and dyes his spiked hair in a rainbow for a run. Red is his lucky "
            "color; his teammates gauge the danger of a job by how much of it he wears. Calm, "
            "good-natured, no remorse for the past: 'Life's but a grand illusion.'"
        ),
        "background": (
            "Arrived in Seattle a few months ago as a stowaway on a cargo ship (a well-known story) and "
            "sleeps in doorways, alleys and missions; secretive about everything before that. At 21 already "
            "a name on the street: snatch-and-dash to headhunting. Has worked with Quetzel and looks after "
            "their mutual interests."
        ),
        "notes": (
            "Pregenerated PC. Stats: B3 Q3 S2 C3 I5 W4, Ess 6, Magic 6; Sorcery 5, Conjuring 4, Magic "
            "Theory 3, Etiquette (Street) 4; Astral pool 16; totem Coyote. Spells: Analyze Device 3, "
            "Detect Enemies 3, Heal Moderate Wounds 4, Mask 2, Power Bolt 4, Sleep 4. Gear: Browning "
            "Max-Power, armor jacket, medicine lodge materials 4, reusable healing fetish (rabbit's ear), "
            "tabletop computer, Yamaha Rapier. No contacts."
        ),
        "contact_skills": ["Coyote shamanism (healing, analysis)", "Odd jobs and stowaway street-craft"],
    },
]

ORG_UPDATES = {
    "Knight Errant Security Services": {
        "notes_append": (
            "Dreamchipper: supplies Global Technologies' guards, security deckers and mages as needed; "
            "three rent-a-cops (Sergeant, a dwarf with thermal eyes; Barnes; Thomas) were on Global's "
            "fourth floor the night of the heist and two died to Griffin's razors. Knight Errant sends a "
            "heavily armed pickup squad for Tee Hee if Urlan is called. Has raided Hollywood Simsense "
            "for BTL production."
        ),
    },
    "Lone Star Security": {
        "notes_append": (
            "Dreamchipper: patrols are few and far between in the Redmond Barrens until nine dissected "
            "prostitutes in four nights force them in -- beefed-up patrols, Wasp helicopters with "
            "searchlights, street samurai rousted and their razors swabbed with chemlab kits, and a lid "
            "on the media; five patrol cars in five minutes 'must be a new donut shop'. Street slang: "
            "'Hey Starry, your constellation is showing' = your Lone Star backup is too close. Pulls "
            "over anyone carrying more than a sidearm near Reno's. Has raided HSE for BTLs."
        ),
    },
    "Aztechnology": {
        "notes_append": (
            "Dreamchipper: made Tee Hee an outstanding graduate offer that he turned down for Global, "
            "and years ago an independent run against an 'up and coming Aztechnology' put Dr. Norris "
            "Hendrix ('Flair') into a two-year coma. Junior Martelli's cape-and-suit Ork bodyguards "
            "carry Ares Sliverguns; Urlan Manes and Pengrave both keep Aztech Nightrunner boats."
        ),
    },
    "Ares Macrotechnology": {
        "notes_append": (
            "Dreamchipper: Global Technologies pitched its 'breakthrough' personality skillchip to Ares "
            "first; Ares passed -- it was too hot -- and Global took the show to the UCAS military."
        ),
    },
    "Crimson Crush": {
        "notes_append": (
            "Dreamchipper: Blood Rumblers ride openly through Crimson Crush territory, and nine of them "
            "ambush a group of Crimson Crush enforcers in the street -- prelims to Khan's war for all of "
            "Redmond. The Crush are the biggest of the local gangs in the horde's path."
        ),
        "enemies_add": ["Blood Rumblers"],
    },
    "Rusted Stilettos": {
        "notes_append": (
            "Dreamchipper: a car full of Rusted Stiletto trolls seen fleeing a mixed pack of Red Rovers "
            "and Blood Rumblers during the run-up to Khan's war on Redmond."
        ),
        "enemies_add": ["Blood Rumblers"],
    },
    "Mitsuhama Computer Technologies": {
        "notes_append": (
            "Dreamchipper: a recent shadowrun against Mitsuhama turned from cakewalk to nightmare; only "
            "Evenstar and Julius Strouther walked away."
        ),
    },
}

LOC_UPDATES = {
    "The Barrens (Seattle)": {
        "notes_append": (
            "Dreamchipper (Redmond): Lone Star patrols few and far between, gangs control the streets, "
            "the news-nets steer clear until a murder spree and a gang war get too big to ignore. Street "
            "encounters p.52: Blood Rumblers in Crimson Crush turf, 'Blood Rules' sprayed over the Brain "
            "Eaters' symbol, joyboys mourning Simon 'all cut up in that alley', Red Rovers riding with "
            "Rumblers chasing Rusted Stiletto trolls, a light machine gun through the Red Hot Nukes' bar "
            "window, a chop-shop meat wagon collecting a young dwarf girl, five Lone Star cars in five "
            "minutes, an ambush blocking the street, empty joygirl corners, 'Khan Rules' on a gang wall, "
            "a Wasp searchlight and a razor swab, and a body laid open on the cold stone. Working girls "
            "and boys of the district are terrorized; the Redmond/Bellevue border (Cascade Road) is the "
            "decker fringe. 'It's not like when that werewolf was prowling the streets last year.'"
        ),
    },
}

NPC_UPDATES = {}

TAG_EXISTING = {}

MATRIX_HOSTS = """
**1. Global Technologies main system** (map p.54; SR1 color-rating notation). Two unlisted SANs:
#3282 (SAN-1, the normal directory number) and #3272 (SAN-2, Roxanne's card -- calls through it route
straight to her). Only part of the whole Global Matrix is mapped: the Martelli Entertainment and
chip-factory sub-processors are left to the GM. Worth building as the adventure's showcase host.

| Node | Function | Rating / IC |
|---|---|---|
| SAN-1 / SAN-2 | Directory #3282 / #3272, unlisted | Green-2, Access 4, Trace and Report 3 |
| SPU-1 | Data routing | Green-3, Barrier 5, Tar Baby 4 |
| SPU-2 | Building systems | Red-3, Access 4, Blaster 4 -> I/OP-1 building controls (Orange-2, Blaster 4, Trace and Dump 3); SM-1 heating/AC, SM-2 elevators, SM-3 electrical (each Green-2, Access 3, Blaster 4) |
| SPU-3 | Security | Red-4, Access 7, Black IC 3 -> I/OP-2 terminals (Orange-4, Blaster 4, Trace and Burn 4); DS-1 records (Orange-4, Scramble 3, Tar Baby 4); SM-4 cameras, SM-5 sensors, SM-6 interior maglocks, SM-7 front-door maglock (each Orange-3, Access 3, Blaster 4) |
| SPU-4 | Personnel | Red-3, Barrier 5, Killer 4 -> I/OP-3 (Orange-2, Blaster 4, Trace and Dump 3); DS-2 records (Orange-2, Barrier 4, Scramble 3) |
| SPU-5 | Data routing | Green-3, Barrier 3, Tar Baby 4 |
| SPU-6 | Back Door think tank | Red-5, Killer 5, Trace and Burn 4 -> I/OP-4 (Red-3, Blaster 4, Trace and Dump 4); DS-3 records (Red-3, Killer 5, Tar Pit 4); **SM-8 self-destruct** (Red-4, Barrier 4, Black IC 5) |
| SPU-7 | Administration | Red-3, Barrier 5, Killer 4 -> I/OP-5 (Orange-3, Blaster 4, Trace and Dump 4); DS-4 records/files (Orange-3, Scramble 3, Blaster 4, Trace and Dump 4) -- fragments of the wiped research: the names Jack, Cleo, Khan |
| SPU-8 | Executive file system | Red-4, Barrier 4, Blaster 5 -> I/OP-6 terminals (Orange-3, Access 4, Trace and Dump 4) **Junior's desktop: the only Dreamchip R&D backup, 500 Mp**; DS-5 records (Orange-3, Scramble 3, Blaster 4, Trace and Dump 4); DS-6 Roxanne's files (Orange-3, Scramble 4, Blaster 3, Tar Pit 4); DS-12 Junior's files (Orange-3, Scramble 4, Blaster 3, Tar Baby 4) -- his pocket-secretary evidence; DS-13 Urlan's files (Red-4, Scramble 4, Black IC 3). DS-6/12/13 each hold a 50 Mp executive summary of the chips |
| SPU-9 | Accounting | Red-3, Barrier 4, Killer 4 -> I/OP-7 (Orange-3, Access 4, Trace and Dump 4); DS-7 records (Orange-3, Scramble 3, Barrier 4, Killer 4) -- ten 10 Mp skillsoft files at 1,000 nuyen each |
| SPU-10 | Research and development | Red-5, Blaster 4, Tar Pit 4 -> I/OP-8 (Orange-3, Blaster 4, Trace and Dump 4); DS-8 records (Orange-3, Scramble 3, Blaster 4, Tar Baby 4); DS-9 project file (Orange-3, Blaster 4, Scramble 3, Tar Baby 4) -- ten 10 Mp files at 1,000 each |
| SPU-11 | Chip maker | Red-4, Access 5, Trace and Burn 4 -> I/OP-9 processor controls (Red-4, Access 5, Trace and Burn 4); SM-10 chip processor (Orange-3, Access 3, Blaster 4); DS-14 'Dreamchipper' personalities (Red-5, Barrier 4, Black IC 4); DS-15 files (Red-3, Barrier 3, Scramble 4, Blaster 4) -- ten 10 Mp files at 1,000 each |
| CPU | | Red-5, Killer 5, Trace and Dump 4 |
| SM-9 | Telephone routing | Green-2, Barrier 2, Access 3 |
| DS-10 / DS-11 | Backup files / backup records | Orange-3, Barrier 3, Scramble 3 |

**2. The LTG company ('one of Ma Bell's babies')** -- to trace 567-2384 to Thomas Martelli: three
resisted tests (Masking, Browse, Decrypt) against Security/IC 8 needing 3 net successes each; any
failure fires Trace and Dump 8 and eight LTG-company men (Company Man, Street Samurai, five
Corporate Security Guards, Street Mage) arrive in five minutes. Model as an abstract Red-8 utility
host if a decker insists; otherwise a rules note.

**3. Flair's computer** -- not connected to the Matrix; nothing of value. **Junior's desktop** is a
terminal on Global's system (I/OP-6), not a separate host. **The Banshee's office computer** --
150 Mp of tax records, no host.
"""

NOT_BUILT = """
- **Junior's Ork bodyguards** (p.34: B8(9) Q5 S6, dermal plate, smartlinked Uzi III, combat knife,
  armored leather; sunlight and plastic allergies), **the three Ork mercs** in the back room, **the
  eight gang leaders**, **Dr. Bob's staff and guards**, **The Banshee's bouncers, bartenders,
  waitresses and patrons**, **HSE party security** -- stat blocks on the org/location rows.
- **The Breadboard's proprietor**, **Orion's gray-haired lady**, **the dwarf with the lap computer**
  at the party, **the Nightsky driver** (Car 5), **Harry** (mind-blasted), **Simon** and **Raymond**
  (joyboys), the **Knight Errant sergeant, Barnes and Thomas** -- one-scene color.
- **Yuri Tellenkov, Joshua Bulter, Albert Yellowjacket** -- HSE leadership entries, not NPC rows.
- **Isheer Many-Manes** (Urlan's father), **Sinsearach** (Freya's haven), **Memorial Hospital**,
  **Cal State / Berkeley / UCLA** -- background references.
- News-handout names (Wednesday, August 17, 2050): investment banker **Dick C. Bloom**; runners **Ted
  Lechowitz, C. R. Greene, Nancy McCabe Flowers** (named in the business pages as corporate raiders);
  **Billy Rogers** (Mariners), **George Seifried** (Cobras coach), **Tom 'Dealer' Cain**, **Jackie
  Cutter**, the **Ratchet Squad**; the 'werewolf prowling the streets last year'.
- **The Global Dreamchips** themselves (rules pp.63-64: Willpower TN 8 to pull one before it takes
  over; 1D6 >= Intelligence when removed = -1 Intelligence permanently; Cleo / Khan / Jack skill lists)
  -- rules, referenced on the Global org row.
"""

PLAY_NOTES = """
- The runners must not learn what the chips are before the run starts; Tee Hee, Junior's secretary,
  the Global datastores, or Dream Analysis (Computer B/R TN 5 or Analyze Device TN 8) reveal it.
- Price is set by conduct (see Urlan) -- track the Reno's meeting, the Ferret chase and the bar fight.
- Junior should not die before the adventure is under way; his Banshee ambush is where he can.
- Freya is the linchpin of the mystery and a possible replacement character; do not let her win the
  fights for the team.
- Pulling a chip: Cooperman dies (lethal capacitor discharge), Griffin goes catatonic, Val forgets
  the week. Using a chip forfeits karma and hands the character to the GM.
- The endgame choice: return the chips (save Global, arm the UCAS military, get paid) or destroy
  them (1,000 per chip if negotiated, nothing otherwise). Karma per the book's guidelines.
- Loose ends: Flair on HSE's payroll to rebuild the chips; the Blood Rumblers' horde without a Khan;
  a catatonic Griffin in a DocWagon Gold bed; Pengrave's VP chair or disgrace; Roxanne and Urlan.
"""
