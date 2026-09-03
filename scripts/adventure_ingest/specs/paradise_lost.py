# Paradise Lost (FASA 7317, 1994, Tom Wong & Nigel Findley) -- campaign order #21. Seattle (one dinner
# at La Maison d'Indochine in Bellevue) then the Independent Kingdom of Hawai'i: Honolulu, Makai Island
# off Molokai, and ALOHA's caves in Waimea Canyon on Kauai. The book is set in 2055 (p.7 "The year is
# 2055", back cover, and the Punchbowl entry "As of 2055"); the Kingdom of Hawai'i sourcebook section
# carries Shadowland comments dated December 2054, and Cameron's diary dates the raid planning to
# "1-14-54" / "1-18-54" -- read here as January 2055 (the raid happened "two weeks ago" when the runners
# are hired), so the adventure runs in February 2055. Kinu's legwork text also says "The ALOHA of 2054".
# Source text: docs/Adventures/text/7317-paradise-lost.txt (82 pages).
# Editing inconsistencies in the book (recorded on the affected rows):
#   - The year confusion above (2055 vs 2054 diary dates and Shadowland stamps).
#   - Bounder "entered the University of Washington" and was expelled on goblinizing (p.15), but the
#     success news handout says Sasha Griczuk "boasts a degree in economics from WSU" (p.64).
#   - Mark Koyashi is an "accountant" (p.23), an "account executive" (p.28) and an "account supervisor"
#     (p.27) at 2M.
#   - The Hughes Airstar 2050 "seats six" (p.29) but its stat block gives "Twin + 9 bucket seats" (p.39).
#   - The ALOHA HQ map labels the perimeter lodge "Eagle Shaman's Medicine Lodge"; the text says three
#     Nene (Goose) shamans (p.40).
#   - The Computer Room holds "three Fuchi Cyber-6 decks with Response Increase 2" (p.45); the deck stat
#     block says "Response Increase (1)" (p.46).
#   - Stack's attribute line was dropped in layout; his skills/gear sit under Kala's block (p.27).
#   - The HNPF unit at the luau is "Special Forces" (p.22); the sourcebook calls it the "Special Response
#     Team" of physical adepts (p.77).
#   - Mary Falls is 33 in the prologue and "in her mid-30s" at the meet.
# ASCII only (pre-commit hook); Hawai'i is written with a plain apostrophe.

ADVENTURE = "Paradise Lost"
ORDER = 21
SOURCE = "7317-paradise-lost.pdf, pp. 4-78 (adventure pp. 4-58, GM information pp. 59-64, Kingdom of Hawai'i pp. 65-78)"
YEAR = "2055 (February)"

SYNOPSIS = """
In late 2051 a mediocre elven decker called **Hackpool** survived a megacorp's field test of new black
IC because a worn-out antique REX signal modifier on his deck short-circuited the biofeedback loop. He
sold the idea to **Mary Falls, Inc. (MFI)**, a mid-size Seattle processed-food company looking to
diversify; MFI named it the **AFD (Anti-Flatlining Device)**, lost one test decker and then Hackpool
himself learning that a working REX does nothing, and **Mary Falls** -- sole owner, a hidden mage of
terrifying power -- took the project to **Molokai Microtronics (2M)** in Hawai'i to keep it away from
the megacorps. 2M built a working prototype in six months, decided MFI could never market it, and
quietly sold it to **Mitsuhama Computer Technologies**. An MCT undercover team massacred the MFI/2M
progress meeting in 2M's Honolulu boardroom while a second team hit the lab on Makai Island off
Molokai, took every prototype and file, purged the lab computer, and killed all but one scientist.

The lab team's leader, **Robbie "Kinu" Kurosawa**, was a double agent for **ALOHA** (Army for the
Liberation of Hawai'i), and ALOHA's leader -- the feathered serpent **Naheka**, a vassal of the great
dragon Ryumyo -- rose out of the sea and drowned the MCT boat crews, keeping the prototypes, the data
and the scientist (whom he mind-sifted and ate). Kinu told MCT a kraken did it. MCT's search boats have
found nothing and the corp is watching Kinu closely; 2M has told MFI it will "handle" the investigation.

Mary Falls plays her own Mr. Johnson at **La Maison d'Indochine** in Bellevue (10,000 nuyen each up
front, 50,000 on completion, negotiable), hands the team ten **Polson Corporation** cover identities
and a 5,000-nuyen credstick apiece, and flies them to **Awalani Airport**. Their bellboy at the
**Honolulu Hilton**, **Daniel Kapaa** -- MFI's only operative in the islands and a Grade 3 initiate
posing as a street fixer -- greets them "from Auntie June", hands out Streetline Specials and a loaned
Fuchi Cyber-4, and books them a tourist day that ends at the **Kona Kalaa Luau**, where the elf
**Serena Day** of the Anglo gang **Haoles Don't Surf** throws them a satchel (a copied 2M passcard and a
floor plan) while four gang enforcers run her down for freelancing.

Inside 2M's 31st-floor offices the runners find VP **Ahmed Virani** jacked in late with his dwarf
bodyguard, monowire across the research-room door, and an ALOHA squad (**Mark Koyashi**, **Kala**,
**Stack**, the Gecko shaman **Kanaka**) checking whether the dead account supervisor **Janet Kaniko**
hid AFD data at a second lab. Koyashi talks; the research subsystem gives up Makai Island. At Makai
the team watches three Japanese MCT soldiers about to execute Kinu ("You've lost the company's trust"),
rescues him, flees ten wired commandos and four Swordsman gunboats, and is saved by the kraken that
really does live there. Kinu, burned by both masters, sells his knowledge of Waimea Canyon for a
200,000-nuyen stake. (If they miss all that, an ALOHA hit squad -- **Toshi** and the paranoid rigger
**Cameron** -- attacks their car in Honolulu and Cameron's "Insurance" chip carries a map of the canyon.)

Daniel flies the team into **Waimea Canyon** in a Hughes Airstar. ALOHA's caves hold about fifty
people: ork guards and adepts, three Nene shamans in a hilltop lodge, the house manager **Audrey
Wilkes**, accountant **Merill Toyoda** and her Awakened cat, five deckers including the veteran **John
Kalakaua** and his prodigy daughter **Lili** testing the AFD on a Fuchi Cyber-7, senior mages **Cassidy
Kane**, **Walker**, **Apapane** and **Akialoa**, and, behind brass doors and a Force 5 barrier, Naheka's
lair with two more prototypes and the "Honeydew" back-up chip. Then a thirty-meter feathered serpent
lands in the cavern. Fighting is suicide; running needs Daniel's helicopter; negotiating gets ALOHA a
50 percent joint venture with MFI and the runners their lives. Escape with the AFD and Mary Falls opens
an electronics division under Bounder and mails the decker five AFDs -- and Naheka never forgets.
"""

TIMELINE = """
- **Late fall 2051** -- Hackpool survives black IC; MFI founds the AFD project. A test decker dies; a
  year later Hackpool dies. Mary Falls partners with 2M; six months to a prototype.
- **January 2055** (Cameron's diary, "1-14" and "1-18") -- ALOHA learns 2M is selling out to MCT and
  that MCT will hit the offices and the Makai lab; Koyashi is "in place". The raids follow; Naheka
  drowns the MCT boat crews. MCT search boats find nothing.
- **Two weeks after the raid (Day 0)** -- e-mail / Egmond's envelope; dinner at La Maison d'Indochine
  the next night at 20:00; limo to Sea-Tac.
- **Day 1** -- Awalani at dawn; the Hilton; Daniel Kapaa; the tourist day; the luau and Serena Day;
  the 2M break-in and the ALOHA squad that night.
- **Day 2-3** -- Daniel needs one day for the Otter (Makai Island, Kinu, the kraken) or two for the
  Airstar. ALOHA's Revenge on the streets if the team is stuck.
- **Day 4-6** -- Waimea Canyon: the caves, the Special Research Area, Naheka's lair, Enter the Dragon.
- **Seven days after arrival** -- deadline: Naheka sells the AFD to Fuchi for 10 million nuyen.
- **Aftermath** -- AFDs sell wildly for three or four months until AFD-defeating black IC hits the
  street; the Seattle Datafax carries MFI's new electronics division (success) or its layoffs (failure).
"""

ORGS = [
    {
        "name": "Mary Falls, Inc. (MFI)",
        "org_type": "corporation (processed food; new electronics division)",
        "tier": 3,
        "headquarters": "Seattle (address not given); shell companies including Polson Corporation",
        "summary": "Mid-size Seattle food manufacturer wholly owned by Mary Falls, secretly developing the Anti-Flatlining Device; hires the runners",
        "description": (
            "'Don't they make music trids?' -- MFI is a mid-size Seattle company that makes processed food "
            "and is 'looking to diversify its business profile'. Mary Falls bought the bankrupt original "
            "out of receivership and resurrected it; she is sole owner and president, with a fleet of "
            "limos, several computers, sizable credit, a corporate security staff of trolls and orks "
            "under Bounder, and a web of holding companies and shells (Polson Corporation among them). "
            "Since late 2051 it has poured millions into the AFD, the Anti-Flatlining Device that dumps a "
            "decker from a system before black IC can kill him. No data on the AFD exists anywhere in the "
            "Matrix. Its only asset in Hawai'i is Daniel Kapaa."
        ),
        "leadership": [
            {"name": "Mary Falls", "title": "President and sole owner", "notes": "Plays her own Mr. Johnson; a Magic 8 mage nobody knows about."},
            {"name": "Bounder", "title": "Chief of security", "notes": "Troll; heads the new electronics division in the success ending (as Sasha Griczuk)."},
            {"name": "Daniel Kapaa", "title": "Personal expediter; sole operative in Hawai'i", "notes": "Bellboy at the Honolulu Hilton; Grade 3 initiate."},
            {"name": "Hackpool", "title": "Head of AFD research (deceased)", "notes": "Killed by black IC testing a preliminary model."},
        ],
        "notes": (
            "Pay: 10,000 nuyen each up front, 50,000 each on completion; Negotiation (Willpower) moves it "
            "10,000 per net success either way. Gear in Hawai'i up to 10,000 nuyen per runner (kept on "
            "success), no single extra item over 500, extras capped at 5,000 total. MFI traveler's "
            "insurance patches up a beaten team. Security seen at La Maison: four troll guards (B9 Q2 S9 "
            "C2 I3 W3 E5.5 R2; TR 4/3; smartlink, dermal plating 1, armor jacket) and four ork guards (B7 "
            "Q4 S8 C2 I3 W3 E5 R3; TR 3/3; smartlink, armor jacket). Endings: success -- new electronics "
            "division under Sasha Griczuk, AFDs sell for four months, five AFDs mailed to the team's "
            "decker, Mary sings the team's praises in Seattle and Honolulu; joint venture with ALOHA -- "
            "both sides honor it and hunt anyone who talks; failure -- 20 layoffs, 'restructuring'. "
            "Refusing the job costs reputation; talking about it later gets the team geeked by MFI and "
            "ALOHA together."
        ),
        "allies": ["Polson Corporation", "Hard Corps Security Inc.", "DocWagon"],
        "enemies": ["Mitsuhama Computer Technologies", "Molokai Microtronics (2M)"],
    },
    {
        "name": "Polson Corporation",
        "org_type": "shell company (investment funds; MFI front)",
        "tier": 2,
        "headquarters": "Seattle (paper company); parent: Mary Falls, Inc. through several layers of holding companies",
        "summary": "One of MFI's many shell companies; supplies the runners' cover identities as fund managers and their families on a Honolulu holiday",
        "description": (
            "A shell that MFI controls through several layers of holding companies, real enough to have "
            "an investment-fund business, a personnel director and a security chief on paper. Mary Falls "
            "issues ten Polson identities: Ralph/Rita Carlson (fund manager, pension fixed-income), "
            "Lauren/Robert Carlson (assistant fund manager, foreign exchange), Juan/Juanita Beyer "
            "(security chief; suits an ork or troll), Colin/Colleen Scheckter (director of personnel), "
            "Huang Li-Chen/Robert Huang (speculative-investments fund manager), Steven/Stephanie Honing "
            "(VP Marketing), Wilma/William Honing (freelance holographic artist and homemaker) and "
            "Wesley/Leslie Honing (student, 16-25; a goblinized child for an ork or troll)."
        ),
        "notes": (
            "The dwarf chauffeur waits at Awalani under a 'Polson Corporation' sign; the Hilton clerk takes "
            "the fake IDs without a blink. ALOHA later knows the 'investment fund managers on vacation' are "
            "more than that. Credsticks are coded to the aliases (5,000 nuyen certified each)."
        ),
        "allies": ["Mary Falls, Inc. (MFI)"],
    },
    {
        "name": "Molokai Microtronics (2M)",
        "org_type": "corporation (contract research)",
        "tier": 3,
        "headquarters": "31st floor of a 50-storey downtown Honolulu skyraker; second office in Hong Kong; secret labs across the islands",
        "summary": "Mid-size Hawai'ian research firm that built the AFD for MFI, then sold it to Mitsuhama and let MCT butcher its own staff for 'assets expended'",
        "description": (
            "'A piddly bunch of research geeks who bulldrek about being bigger guns than they are' -- 2M "
            "does the boring contract research megacorps will not touch and good work for small corps "
            "without labs of their own, and makes 'pretty nuyen for a weeny little corp'. Logo: a gold and "
            "a silver M overlapping in an azure circle. Offices in Honolulu and Hong Kong (President Ted "
            "Dackson and VP Marketing Phillip Savage live in the latter); lab locations are secret even "
            "from most employees and travel only by courier ('mosquitoes') and a stand-alone research "
            "subsystem. Top management doubted MFI could market the AFD, sold the prototype to Mitsuhama, "
            "took compensation for the staff MCT killed, and promised MFI it would run the investigation. "
            "Legwork TN 9: 'got fragged in a major way a couple of weeks ago -- a megacorp nailed them'."
        ),
        "leadership": [
            {"name": "Ted Dackson", "title": "President", "notes": "Mostly in Hong Kong or entertaining clients."},
            {"name": "Phillip Savage", "title": "Vice-President, Marketing", "notes": "Ex-pro Urban Brawler; Dackson's son-in-law."},
            {"name": "Ahmed Virani", "title": "Vice-President, Accounts Management", "notes": "Working late the night of the break-in."},
            {"name": "Derek Hanna", "title": "Vice-President, Accounting and Finance; financial controller", "notes": "Oldest executive; the central computer sits in his office."},
            {"name": "Leslie Chao", "title": "Vice-President, Personnel and Payroll", "notes": "New."},
            {"name": "Janet Kaniko", "title": "Account supervisor, AFD project (deceased)", "notes": "Killed in the boardroom massacre."},
            {"name": "Mark Koyashi", "title": "Account supervisor (ALOHA mole)", "notes": None},
            {"name": "Alan Jenkins", "title": "Account executive", "notes": "His copied passcard gets the runners in."},
        ],
        "notes": (
            "Head-office security is the landlord's (Honolulu Offices Inc.) plus 2M's own stand-alone "
            "subsystems -- see the office location row and the prep-doc Matrix maps (2M Main System, 2M "
            "Research Lab Subsystem, building system). The AFD lab was on Makai Island, a dot off Molokai; "
            "MCT purged its computer and 2M abandoned it. The paranoid survivors 'will sleep at the office "
            "for the next month'. Serena Day: 'Some Seattle corp made a deal with 2M, paying Molokai to "
            "grease some of their labcoats' -- inside information that is half right."
        ),
        "allies": ["Mitsuhama Computer Technologies", "Honolulu Offices Inc."],
        "enemies": ["ALOHA (Army for the Liberation of Hawai'i)", "Mary Falls, Inc. (MFI)"],
    },
    {
        "name": "ALOHA (Army for the Liberation of Hawai'i)",
        "org_type": "terrorist / secessionist army",
        "tier": 3,
        "headquarters": "Two natural caves behind a rock outcrop 300 m up the wall of Waimea Canyon, Kauai (being abandoned after the run)",
        "summary": "Militant Polynesian nationalists led in secret by the feathered serpent Naheka; ~50 in the canyon, ~200 field agents in corporate jobs; stole the AFD from MCT",
        "description": (
            "The original ALOHA bombed U.S. military bases (two dozen car bombs, 2011-2013, 150 'legitimate' "
            "dead and twice that collateral), fought the Civil Defense Force as guerrillas and helped win "
            "secession; whether today's ALOHA is the same organization 'remains in doubt', but it runs the "
            "same kind of attacks against megacorporate assets. Stated goals: rid Hawai'i of all "
            "non-Polynesian influence and reunite Polynesia into a single empire -- 'twisted morons who "
            "want to wipe out anything that ain't native Hawai'ian' (Serena Day). Kinu: 'a shell of the "
            "organization it was' -- about 50 members at the Waimea Canyon caves and 200 or so field "
            "operatives across the islands and the mainland, many in corporate management jobs (Mark "
            "Koyashi at 2M, Kinu inside MCT). Plenty of mages and deckers, mostly naturalists who regard "
            "heavy cyberware as a 'perversion' of the body's essence. Members greet you with 'Aloha from "
            "ALOHA! E make loa, haole!' and die rather than talk. Only the innermost circle knows the "
            "'brilliant man with fantastic magical power' who leads them is a feathered serpent."
        ),
        "leadership": [
            {"name": "Naheka", "title": "Leader (feathered serpent; vassal of Ryumyo)", "notes": None},
            {"name": "Akialoa", "title": "Leader of the ALOHA mages", "notes": None},
            {"name": "Cassidy Kane", "title": "Most experienced mage; trains the apprentices", "notes": None},
            {"name": "John Kalakaua", "title": "Veteran decker", "notes": None},
            {"name": "Lili Kalakaua", "title": "Prodigy decker; keeper of the AFD back-up", "notes": None},
            {"name": "Audrey Wilkes", "title": "House manager", "notes": "Master passcard to everything but Naheka's cave."},
            {"name": "Merill Toyoda", "title": "Accountant and financial manager", "notes": None},
            {"name": "Robbie \"Kinu\" Kurosawa", "title": "Top espionage operative (burned)", "notes": None},
        ],
        "notes": (
            "Foiled an attack on Awalani Airport's cargo depot (van of RVX-12 explosive) the day the "
            "runners land; plans in progress to kidnap the synthrock group Blitzkrieg on their Honolulu "
            "tour date (Cameron's chip). Muscle: ork guards (B?/Q3 S4 R3; TR 4/3; Armed 5, Climbing 4, "
            "Firearms 5; Predator, sword, armor vest, wrist phone); physical adepts (B5 Q5 S5 C3 I3 W3 M6; "
            "Init 4+2D6; TR 4/4; Unarmed 8, Firearms 6, Athletics 6; Predator, katana, Killing Hands 5S); "
            "field teams like Toshi's (Uzi IIIs, armor vests, TR 3/3); three Nene shamans (Sleep 7, Mana "
            "Bolt 5, Powerball 5; +3 dice mountain spirits, +2 TN off Hawai'ian ground); four apprentice "
            "mages (Sorcery 5; Chaos 5, Heal 4, Mana Barrier 5, Mana Bolt 4, Power Dart 4); senior mages "
            "(Sorcery 6, Conjuring 5; Acid Stream 6, Flamethrower 5, Heal 6, Mana Barrier 6, Mask 6, Mind "
            "Probe 3, Power Dart 6, Stunball 5); five deckers with Fuchi Cyber-6s. Legwork TN 8 in "
            "Honolulu: 'crazy terrorist group... they got people working everywhere'; 'some psycho mage, "
            "calls himself Naheka' (naheka = snake). Endings: a joint venture with MFI honored to the "
            "letter; or Naheka sells the AFD to Fuchi for 10 million and gets a few dozen AFDs for his "
            "deckers; or, with Naheka dead, ALOHA is crippled until Ryumyo appoints another vassal. Naheka "
            "is already moving operations out of Waimea Canyon."
        ),
        "allies": ["Na Kama'aina"],
        "enemies": ["Mitsuhama Computer Technologies", "Molokai Microtronics (2M)", "Haoles Don't Surf", "Hawai'ian National Police Force (HNPF)", "Kingdom of Hawai'i"],
    },
    {
        "name": "Haoles Don't Surf",
        "org_type": "gang (Anglo protection / information network)",
        "tier": 2,
        "headquarters": "Honolulu night spots (turf not given); recognizable by a ponytail with shaved sides",
        "summary": "Tough Anglo gang that grew from protecting white-run businesses into a night-spot cartel and an underground information network; opposes ALOHA",
        "description": (
            "Named from native slang for white people, the Haoles started as a protection group for "
            "Anglo-run businesses when anti-white sentiment grew in the islands; now they control many "
            "popular night spots and run an efficient underground information network. Non-white members "
            "exist but Caucasian humans and metahumans hold the power. They oppose ALOHA and work to thwart "
            "it, but the bosses refused Daniel Kapaa's request for 2M information rather than draw the "
            "attention of whoever ordered the massacre. Vicious street gladiators with a deserved "
            "reputation; they flee when losing."
        ),
        "leadership": [
            {"name": "Serena Day", "title": "One of the gang's best operatives (marked for death for freelancing)", "notes": None},
            {"name": "Kristo", "title": "Enforcer (ork)", "notes": "Leads the four sent after Serena."},
        ],
        "notes": (
            "Enforcers at the luau: Kristo (B7 Q4 S7 C2 I4 W2 R4; TR 4/3; Armed 4, Firearms 5) and Marcus, "
            "Tor and Stefano (B3 Q3 S4 C3 I3 W4 R3; TR 3/2; Armed 4, Firearms 3), all with armor vests, "
            "Colt American L36s in concealable holsters and saps. Five Combat Turns to save Serena; "
            "otherwise she is driven somewhere secluded and never seen again. If the gang beats the team, "
            "it strips them and leaves them bleeding in the street -- and Daniel fires them."
        ),
        "enemies": ["ALOHA (Army for the Liberation of Hawai'i)"],
    },
    {
        "name": "Hawai'ian National Police Force (HNPF)",
        "org_type": "national police force (Na Maka'i)",
        "tier": 4,
        "headquarters": "Honolulu; jurisdiction across the Kingdom and nominally 50 km out to sea",
        "summary": "Hawai'i's community-policing national force -- kahuna cops, six-month neighborhood tours, and a Special Response Team made entirely of physical adepts",
        "description": (
            "Na Maka'i is a national police force, not a contractor like Lone Star. Officers serve "
            "six-month tours in one neighborhood, defuse trouble before it starts and draw the big guns "
            "only as a last resort -- but they 'fight smarter and harder than the average Lone Star cop'. "
            "Many officers are kahunas of modest power. The Special Response Team (the luau text calls "
            "them Special Forces) is all physical adepts trained in special weapons and tactics. ALOHA's "
            "hit men sit near the top of the Most Wanted list; a plausible story ('They just started "
            "shooting!') gets the runners waved on. Cross-trains with the army (Pu'ali Koa)."
        ),
        "notes": (
            "HNPF Special Forces (10) reach the Kona Kalaa Luau from Waikiki in one minute: B4 Q6 S5 C3 I3 "
            "W3 E6 M6 R4; TR 3/3; Athletics 3, Firearms 5, Stealth 4, Unarmed 5; Killing Hands 5M; Ares "
            "Predator, armor clothing 4/2, Defiance Super Shock taser -- hands and tasers first, pistols "
            "only if it gets tough. Awalani arrivals are the HNPF's problem, not the airport's."
        ),
        "allies": ["Kingdom of Hawai'i", "Royal Hawai'ian Armed Forces"],
        "enemies": ["ALOHA (Army for the Liberation of Hawai'i)"],
    },
    {
        "name": "Kingdom of Hawai'i",
        "org_type": "nation (constitutional monarchy)",
        "tier": 5,
        "headquarters": "Iolani Palace and the Legislative Building, King Street, downtown Honolulu",
        "summary": "Independent since August 22 2017 under King Kamehameha IV (Danforth Ho); now ruled by his son Kamehameha V -- a megacorporate free port that lives on tourism and trade",
        "description": (
            "Eight islands (Ni'ihau, Kauai, Oahu, Molokai, Lanai, Maui, Kaho'olawe, Hawai'i), 4.1 million "
            "people (54 percent human, 22 ork, 11 troll, 8 elf, 4 dwarf), 3.2 million of them on Oahu, "
            "RTG PA/HI, per-capita income 20,000 nuyen, 64 percent corporate-affiliated. Na Kama'aina "
            "found a Kamehameha I bloodline in the Ho family; Danforth Ho went underground as 'rightful "
            "ruler in exile', cut deals with Yamatetsu, Ares and the yakuza, and on the day of the Great "
            "Ghost Dance loosed kahunas and Great Form spirits on the Civil Defense Force, marched on the "
            "capital and declared sovereignty as Kamehameha IV (August 22 2017). A U.S. task force turned "
            "back -- rumor says a salvo of Ares 'Thor shots' off the flagship's bow. The ali'i and his "
            "appointed officials share power with an elected legislature (three-quarters majorities to "
            "block each other; a royal override forces the whole chamber to resign). The price of "
            "independence: megacorps enjoy 'more latitude than almost anywhere else in the world', which "
            "is also the buffer against UCAS repatriation and Japan's designs through CalFree. English "
            "official, Japanese second, Hawai'ian rising; write it with the apostrophe or slot off every "
            "kama'aina in earshot."
        ),
        "leadership": [
            {"name": "King Kamehameha V (Gordon Ho)", "title": "Ali'i (king) since 2045", "notes": "Born 2020; Harvard economics postgraduate."},
            {"name": "Ke-one-poko", "title": "Chief advisor (kahuna)", "notes": "Believed a Nene shaman; also advised Kamehameha IV."},
            {"name": "Danforth Ho (King Kamehameha IV)", "title": "First ali'i, 2017-2045 (deceased)", "notes": None},
        ],
        "notes": (
            "Free customs on arrival (Awalani only accepts flights from airports with rigid security); "
            "departures are scrutinized hard. Prices 105 percent of Seattle, black market as low as 90. "
            "Nuyen is the currency; nativists want a Tongan pa'anga standard. Hurricanes every four years "
            "(Kauai and Ni'ihau worst). Population by descent (2050): Asian 58.4, Anglo 30, Polynesian "
            "9.5, Hispanic 2.1 percent; under 10 percent can claim a quarter Hawai'ian ancestry. Orks and "
            "trolls are unusually common and unusually accepted; prejudice runs against elves instead. "
            "Native totems: Honu (Turtle), Kohola (Whale), Mo'o (Gecko), Nene (Goose); of the mainland "
            "totems kama'aina follow only Cat, Dog, Rat and Shark. Awakened natives: the nene, the mo'o, "
            "the gray whale, and a kraken in the waters off Molokai. Kaho'olawe is a bombing range and "
            "Ni'ihau a patrolled 'primitive preserve' whose guard boats sink intruders without asking. "
            "Legislative factions: the old Na Kama'aina lions, now publicly denouncing ALOHA's violence "
            "while flirting with its pan-Polynesian cause."
        ),
        "allies": ["Yamatetsu Corporation", "Ares Macrotechnology", "Hawai'ian Yakuza", "Royal Hawai'ian Armed Forces", "Hawai'ian National Police Force (HNPF)"],
        "enemies": ["ALOHA (Army for the Liberation of Hawai'i)"],
    },
    {
        "name": "Royal Hawai'ian Armed Forces",
        "org_type": "national military (air force, army Pu'ali Koa, navy, covert Na Kiu)",
        "tier": 4,
        "headquarters": "Kaiao Field (former Hickam AFB) west of Honolulu; Pearl Harbor Naval Shipyard; Space City on Haleakala",
        "summary": "Defense-only combined-arms military built on inherited U.S. hypersonic spy-plane tech, old hulls with new guts, and a covert branch nobody can describe",
        "description": (
            "Tailor-made to repel attack by air or sea and 'virtually incapable' of operating far beyond "
            "the islands; no defense against space-based attack. The small, lethal air force flies from "
            "Kaiao Field on inherited pulse-detonation spy-plane research; the army (Pu'ali Koa) resembles "
            "the old National Guard and cross-trains with the HNPF; the navy's hulls were on the Pearl "
            "Harbor slipways at secession and look thirty years old, but everything inside is cutting "
            "edge and 5 percent of the fleet is always in dock for refits. The covert Na Kiu exist -- "
            "number, training and missions unknown. It bombs Kaho'olawe most days, sinks boats around "
            "Ni'ihau, and runs 'black' research at Space City and the Kahuku Point zero zone where "
            "'speculating too much can be hazardous to the health' (rumor: magical experiments in the "
            "Haleakala crater)."
        ),
        "notes": (
            "The HNPF cedes its 50-km maritime jurisdiction to the navy in practice. The Honolulu newscast "
            "has MCT denying that its own military forces are training in Hawai'ian waters -- the "
            "Swordsman flotilla off Makai Island says otherwise."
        ),
        "allies": ["Kingdom of Hawai'i", "Hawai'ian National Police Force (HNPF)"],
    },
    {
        "name": "Na Kama'aina",
        "org_type": "political movement (Hawai'ian / pan-Polynesian nationalists)",
        "tier": 3,
        "headquarters": "Honolulu; legislative seats and a resurgent street movement across the islands",
        "summary": "'The Land Children' -- the 1990s secessionist movement that found and crowned Danforth Ho, then lost him; reborn with the cry 'Polynesia for Polynesians'",
        "description": (
            "Founded in the 1990s to lobby for an independent kingdom, distanced itself from ALOHA's "
            "bombs in 2013, was crushed alongside it by the Civil Defense Force in 2014, went underground, "
            "traced Kamehameha I's bloodline to the Ho family and made Danforth Ho its ali'i in exile -- "
            "then watched him cut corporate and yakuza deals behind its back and shut it out of the new "
            "government. It fought back at the ballot box as the anti-corporate faction of the legislature. "
            "Today's Na Kama'aina has resurfaced as a social force preaching a United Polynesia, an "
            "ethnically pure homeland with Hawai'i at its center (the folktales say the islands are the "
            "peaks of a sunken continent that will rise again); its young militants learn Hawai'ian and "
            "take names like Ka-wena-'ula-a-Hiiaka-i-ka-poli-o-Pele-ka-wahine-'ai-ho-nua. It claims it can "
            "win without bloodshed; ALOHA and the other splinters disagree."
        ),
        "notes": (
            "Useful as the political face of the same anger that fills ALOHA's caves: sympathizers in the "
            "legislature, kahunas, traditionalists living in the mountains below the poverty line by "
            "choice. Any information about ALOHA in the sourcebook section is common knowledge among them."
        ),
        "allies": ["ALOHA (Army for the Liberation of Hawai'i)"],
    },
    {
        "name": "Honolulu Offices Inc.",
        "org_type": "commercial landlord / building security",
        "tier": 2,
        "headquarters": "Fifth-floor office of the 50-storey downtown Honolulu skyraker that houses Molokai Microtronics",
        "summary": "Landlord of 2M's skyraker; runs the building's off-Matrix security CPU with a guard jacked in and ten-plus armed guards ten minutes away",
        "description": (
            "Provides centralized building security to many tenants (2M, several consulting firms) from a "
            "CPU in its fifth-floor office that also runs the lights, sprinklers and air conditioning and "
            "is kept off the Matrix. Molokai's monthly payment buys pressure sensors, maglocks, alarms, "
            "cardreaders and a thumbprint scanner on the main doors. A guard is jacked into the CPU at all "
            "times and can tell which floor a tampering decker is working from."
        ),
        "notes": (
            "Security Guards (10+) from headquarters within ten minutes of the call: B4 Q4 S4 C2 I4 W4; TR "
            "3/3; Armed 4, Firearms 4, Unarmed 3; Ares Predator, armor clothing 4/2, low-light goggles, "
            "portable phone, stun baton. A GM lifeline: they can be sent in against the ALOHA squad instead "
            "of the runners. Building system mapped in the prep doc."
        ),
        "allies": ["Molokai Microtronics (2M)"],
    },
    {
        "name": "Hawai'ian Yakuza",
        "org_type": "organized crime (yakuza, Hawai'i branch)",
        "tier": 4,
        "headquarters": "Honolulu's Japanese districts (no oyabun or office named)",
        "summary": "The only organized crime in the Kingdom: protects the Japanese population, skims the black market, and is the liaison every corp hiring locals must pay",
        "description": (
            "Organized crime in the Kingdom of Hawai'i belongs exclusively to the yakuza. Traditional "
            "protectors of the common folk in Japan, the Hawai'ian branch collects protection money in "
            "Japanese neighborhoods and actually delivers -- shielding Japanese interests against the "
            "kama'aina. The bulk of its money is skimmed from the islands' black market. Any corporation "
            "employing Hawai'ian residents rather than importing enclave workers learns that a yakuza "
            "liaison is the only way to keep a project running; those that refuse suffer a staggering "
            "number of accidents, never quite enough to justify a corporate army. Danforth Ho negotiated "
            "with them in early 2017 (over Na Kama'aina's objections) and on Secession Day the yakuza "
            "fielded a civilian army that cut government communications across the islands."
        ),
        "notes": (
            "Not encountered in the adventure; the obvious next door for a team that needs Honolulu "
            "contacts, gear or a way off the islands unofficially. Distinct from the Seattle Watada-rengo "
            "row."
        ),
        "allies": ["Kingdom of Hawai'i"],
    },
    {
        "name": "Ork Rights Committee",
        "org_type": "metahuman-rights activist group",
        "tier": 2,
        "headquarters": "Seattle; a storefront distribution point in the Redmond Barrens",
        "summary": "Ork and troll underclass advocacy group whose Redmond Barrens storefront was shot up by masked gunmen (six dead); its rising star is the activist Preacher",
        "description": (
            "Seattle Datafax (February 2055): masked gunmen opened fire on the Committee's storefront "
            "distribution point in the Redmond Barrens; six dead including a four-year-old boy; Alamos "
            "20,000 blamed; the intended target believed to be Preacher (John Picarille), who has risen "
            "from an open Seattle Council meeting two years ago to a national position as spokesman for "
            "the ork and troll underclass. 'But who is Preacher, and what does he really stand for?'"
        ),
        "leadership": [
            {"name": "Preacher", "title": "Ork-activist leader and spokesman (a.k.a. John Picarille)", "notes": None},
        ],
        "notes": "News-handout organization; a Seattle hook for the team's return.",
        "enemies": ["Alamos 20,000"],
    },
]

LOCATIONS = [
    {
        "name": "La Maison d'Indochine",
        "location_type": "restaurant",
        "district": "Bellevue",
        "security_level": "Corporate High Security",
        "summary": "Deluxe French-Vietnamese restaurant where corporate top dogs do business in safety: MAD staircase, twelve hidden guards, armed elven quartet, Hard Corps astral cover",
        "description": (
            "Pink awnings and bright lights outside; inside, small and elegant -- golden chandeliers from a "
            "14-foot ceiling, live palms and bamboo in lapis lazuli pots, a holographic stage of Southeast "
            "Asian scenery, an elven string quartet playing something sparkling and baroque, and a "
            "drop-dead-gorgeous maitre d' with long black curls at a Fuchi P100. Six tables and four "
            "private booths (5A-5D) behind three-meter panels, each booth issuing a PANICBUTTON wristband; "
            "booths 5A and 5C have trap doors to the private rooms below, worked only from the security "
            "computer. Extremely thick cement walls. Downstairs: two private guest rooms (Rating 5 "
            "maglock, Rating 4 passcard reader, PANICBUTTON), storeroom, and proprietor Jeremy Ngok's "
            "office, bedroom and living room (Rating 6 maglock, Rating 7 passcard reader). Kitchen of a "
            "chef, two cooks and two prep cooks; three waiters and three busboys. Legwork TN 4: 'Some "
            "fancy restaurant in Bellevue. Supposed to be a corp hangout' -- dinner costs more than you "
            "make in a month. Map p.13."
        ),
        "notes": (
            "Dress code: 200 nuyen per point of Body and Etiquette (Corporate) (6) or you look wrong; ask "
            "for the Smithson table; 50 nuyen into the maitre d's slot if she stalls. Front stairs are a "
            "Rating 9 magnetic-anomaly detector (Concealability 10); guards step out of wall panels and "
            "demand weapons, then stun and call Lone Star (six cops in five minutes). Security Guards (12, "
            "six per monitoring room, ten respond): B4 Q4(5) S4(5) C3 I3 W3 E4.5 R3; TR 3/3; Firearms 5, "
            "Electronics (Maglocks) 2; muscle replacement 1, smartlink; Predator with gel rounds, armor "
            "jacket, stun baton -- stun fast, rarely pursue outside, hand culprits to Lone Star. Elven "
            "Musicians (4): B4 Q6 S3 C6 I4 W4 E5.8 R5; TR 3/3; Firearms (Pistols) 4, Unarmed 5; synthlink; "
            "armor vest, Fichetti Security 500 gel, Kazuki 300 violin synthesizer -- play helpless, then "
            "flank. Maitre d': Computer 3, Etiquette (Corporate) 5, Japanese 4; datajack. Back stairs from "
            "the alley: Rating 6 maglock plus Rating 5 retinal scan (Bounder's pattern is on file for the "
            "night). Astral: Hard Corps contract -- a Force 4 watcher, then an astral mage (Sorcery 6, "
            "Conjuring 5, Rating 2 katana weapon focus) and two Force 4 air elementals. Eight MFI guards "
            "wait in the rented room below Mary's booth. A scene here ends the offer; captured runners "
            "get two months from Lone Star. Team Karma +1 for avoiding conflict."
        ),
    },
    {
        "name": "Awalani Airport",
        "location_type": "transportation hub",
        "district": "Just west of Honolulu, on the old Honolulu International and half of Hickam AFB",
        "security_level": "Patrolled / Commercial",
        "city": "Honolulu",
        "controlling_org": "Kingdom of Hawai'i",
        "summary": "'Sky Harbor' -- the Kingdom's only suborbital-capable airport; no security on arrival, hard scrutiny on departure; ALOHA's foiled bomb van",
        "description": (
            "The major international airport of the Kingdom, the only one that handles suborbital and "
            "semiballistic flights, with scheduled service to North America and the Far East. Aloha Air "
            "and Moku'aina Air fly commuters (Federated-Boeing Commuters, Cessna C750s, Hughes Airstars at "
            "a premium) to the outer islands; Lio Lawe Ukana ('Pack Horse') Air Transport moves cargo by "
            "LZ-2049 SHAPELY airship. Broad palm-lined streets glow gold in the early-morning sun on the "
            "drive into town. A trideo in the lounges replays the day's news: a routine traffic stop on "
            "the cargo-depot access road stopped a rental van packed with RVX-12 -- ALOHA blamed."
        ),
        "notes": (
            "No arrivals check ('a corporate tourist haven... contraband brought in is the Hawai'ian "
            "police's problem'); departures are screened intensely, so plan the exit. The Polson chauffeur "
            "is a snoring dwarf in a screaming Hawai'ian shirt under a 'Polson Corporation' sign (Dwarf "
            "Technician, Etiquette (Corporate) 4, Car 5, Unarmed 3; Toyota Elite). ALOHA's decker Jan is "
            "surfing the airport's systems from Waimea Canyon. Suborbital to Seattle: 2,500 nuyen."
        ),
    },
    {
        "name": "Honolulu Hilton",
        "location_type": "hotel",
        "district": "Waikiki (the book never names the district; the luau is just outside the grounds)",
        "security_level": "Patrolled / Commercial",
        "city": "Honolulu",
        "summary": "Luxury hotel where MFI books the team a prepaid week; Daniel Kapaa's bellboy cover, Kintaro's Lounge, a marina, and a rooftop heliport",
        "description": (
            "Everyone smiles and bends over backwards for guests they take for high rollers. The deluxe "
            "suite is booked for a week, paid in advance; Kintaro's Lounge downstairs serves a Japanese "
            "brunch; the day tour bus leaves from the door; the hotel marina moors the Otter; the roof "
            "heliport takes the Hughes Airstar. The scrawny tanned bellboy who insists on unpacking your "
            "bags is Daniel Kapaa, whose side business in illegal and semi-legal goods for wealthy guests "
            "is an open secret the bell captain takes a cut of."
        ),
        "notes": (
            "Gear arrives in boxes marked 'Special Delivery -- Candy's Toys' with car and bike keys and a "
            "note from 'Auntie June'; the parking attendant brings the Ford Americar and two Yamaha "
            "Rapiers round. Daniel waits in the suite from midnight to 2 a.m. after the 2M job. ALOHA "
            "traces the team here and gets the rental's plate. Attacking Daniel ends the run."
        ),
    },
    {
        "name": "Kona Kalaa Luau",
        "location_type": "restaurant",
        "district": "Just outside the Honolulu Hilton grounds",
        "security_level": "Patrolled / Commercial",
        "city": "Honolulu",
        "summary": "Tourist luau with a weapons check, a magically illustrated hula of Pele rising from Mauna Loa, an open bar -- and Serena Day running for her life",
        "description": (
            "An outdoor stage under the moon where costumed dancers tell the story of the goddess Pele's "
            "rise from Mauna Loa while magically generated images of a volcanic eruption climb into the "
            "sky, realistic enough to make you flinch; then a sumptuous banquet and an open bar. Mandatory "
            "security check at the gate."
        ),
        "notes": (
            "Nothing heavier than a Streetline Special: weapons of Concealability 7 or better pass. "
            "Trouble brings ten HNPF Special Forces adepts from Waikiki in one minute (stats on the HNPF "
            "row). Serena Day sprints across the grounds with Kristo, Marcus, Tor and Stefano behind her "
            "and throws the team a leather satchel (Alan Jenkins' copied passcard, the 2M floor plan). "
            "Five turns to intervene."
        ),
    },
    {
        "name": "Molokai Microtronics Offices (Honolulu)",
        "location_type": "corporate facility",
        "district": "Downtown Honolulu, 31st floor of a 50-storey skyraker near the nighttime hub",
        "security_level": "Corporate High Security",
        "city": "Honolulu",
        "controlling_org": "Molokai Microtronics (2M)",
        "summary": "2M's head office: passcard elevators, thumbprint doors, laser grids, nerve gas on the central computer, a research subsystem that knows where the labs are, and an ALOHA squad in the dark",
        "description": (
            "A dark monolith over a deserted street. The passcard (Alan Jenkins') opens the front door and "
            "an elevator that stops only at 31. Reception (terminal on 2M's Matrix-connected central "
            "network), tall oak main doors with the gold-and-silver M logo (Barrier 6, Rating 4 thumbprint "
            "scanner), executive offices with windows round the outside, junior cubbyholes inside; lights "
            "stay on in the inner hall, reception, accounting and secretarial areas. Rooms: presentation "
            "room (stand-alone computers; maglock/cardreader/thumbprint 4), accounting cubicles, account "
            "supervisors' offices (Rating 5 keypad, Rating 6 pressure sensors, seven-digit code), "
            "secretarial area, the boardroom where the massacre happened (repanelled, new teak table), "
            "President Dackson's bare office, Phillip Savage's art-and-trophy office (Rating 5 keypad, "
            "infrared laser grid, 5S then 5L -- thermographic vision sees the beams in the dust), Ahmed "
            "Virani's tasteful office, Leslie Chao's undecorated one, and Derek Hanna's, which houses the "
            "central computer: Rating 7 keypad with Anti-tamper 2, nine-digit code, 10S lasers, and a "
            "Rating 5 retinal scanner in the terminal screen that releases Green Ring 3 nerve gas (8S; "
            "survivors +5 to all TNs for an hour) on a stranger's eye. The Research Room (14) holds two "
            "terminals on the stand-alone research subsystem. Map p.24, Handout 4."
        ),
        "notes": (
            "Landlord security (Honolulu Offices Inc.) is off-Matrix; a guard jacked into the fifth-floor "
            "CPU can place a tampering decker's floor and ten-plus guards arrive in ten minutes; 2M's own "
            "subsystems only report to it. Breaking the main doors alarms everyone. The night of the "
            "break-in: Virani jacked into his Fuchi Cyber-6 behind drawn curtains, Rosenkrantz outside "
            "his door; in the research room Koyashi, Kala, Stack and Kanaka under Invisibility, most of "
            "the room's security disabled, monowire across the doorway a meter up (Perception (6), (8) in "
            "combat; 11S running, 9S walking, 7S grabbing). Retinal scanner can be shut off only from "
            "inside the 2M system (I/O port). The research subsystem's DS-2 names Makai Island with map "
            "coordinates; it cannot tell you the lab is empty. Systems mapped in the prep doc."
        ),
    },
    {
        "name": "Makai Island Lab (2M)",
        "location_type": "research lab",
        "district": "A tiny island off Molokai; small coves, jungle, and the MCT search party's boats",
        "security_level": "Corporate High Security",
        "city": "Makai Island (off Molokai)",
        "controlling_org": "Molokai Microtronics (2M)",
        "summary": "The isolated lab where 2M built the AFD -- raided, purged and abandoned; now crawling with Mitsuhama commandos, watcher spirits and a kraken offshore",
        "description": (
            "A dot of land off the larger island of Molokai, thick with life that blazes in astral space "
            "except for one dark concrete-and-steel spot. Reached from the Hilton marina by night in the "
            "Otter on stolen coordinates; a searchlight boat passes, and something large swells the water "
            "behind it. The lab itself is gone as far as the runners are concerned: MCT stole every "
            "prototype, downloaded the files, purged the computer and killed the staff, and 2M abandoned "
            "it. 'The island offers nothing except death at the hands of MCT's professional commandos.'"
        ),
        "notes": (
            "Astral scouts meet three tiger-sized watcher spirits (Threat 5, 5M) bound by MCT's combat "
            "mage. On the beach three Japanese MCT soldiers (wired 1, AK-97s with laser and thermo scope; "
            "TR 3/3) are about to shoot Kinu; one burst is planned, more brings a ten-man Mitsuhama "
            "Assault Team (B5 Q4(6) S4(6) I4 W4 R4(8), Init 8+3D6; TR 5/4; Ares FN-HAR, armor jacket), the "
            "combat mage (Sorcery 5, Conjuring 5; Chaos 5, Mana Bolt 4, Power Dart 4) and four "
            "Zemlya-Poltava Swordsman boats (Handling 5, Speed 30/90, Body 3; pilot with Boat 5 plus four "
            "wired crew, AK-97s) -- one 100 m off the cove, three at 600 m; restricted terrain, +2. The "
            "runners should not win the fight. The Otter (Handling 2, Speed 22/67, Body 2, Signature 4; "
            "pop-up MMG turret, rear arc) is slower; the kraken (B12/3 Q5x3 S20 W6 R7, 12D +2 Reach, "
            "Pestilence) comes to bright lights -- flares, illusions or a nature spirit steer it into the "
            "Swordsmen; it eats one or two boats and MCT stops interfering for the rest of the run."
        ),
    },
    {
        "name": "ALOHA Headquarters (Waimea Canyon)",
        "location_type": "underground bunker",
        "district": "Waimea Canyon, 300 m above the floor and 300 m below the rim, behind a rock outcrop",
        "security_level": "Zero Zone -- Lethal Response",
        "city": "Waimea Canyon, Kauai",
        "controlling_org": "ALOHA (Army for the Liberation of Hawai'i)",
        "summary": "Two shored-up natural caves (Barrier 16 walls, 14 doors) housing fifty terrorists, a Nene medicine lodge, a hermetic library, the AFD research area, and Naheka's masked lair",
        "description": (
            "Kauai from the air is a verdant circle round dark mountains; the Airstar drops past Mount "
            "Waialeale into red-orange rock and brilliant green. A camouflage-netted landing pad 50 m from "
            "a four-meter hole in the canyon wall (Perception (3); transponder beacons the team lacks; "
            "Rotor Craft at Handling +3 or crash at 100 m/turn; or rappel upslope and climb, Climbing (4) "
            "per 50 m, falls 20 m a round at (distance/10)M). Upper level: entry room with a Rating 5 palm "
            "scanner (fifty members on file, Anti-tamper 4) that opens hidden panels; Audrey Wilkes' "
            "office; guest rooms; entertainment lounge with a concert stage; dining room; the elven "
            "musicians' practice room; cooks' and cleaners' quarters; kitchen and a storeroom good for "
            "months; gym; guards' quarters 13A-D; Merill Toyoda's office (Rating 5 maglock) and "
            "cat-guarded quarters; showers. Lower level (earth floor): technicians', deckers' and the "
            "Kalakauas' quarters (voice 5, thumbprint 4, retinal 6, maglock 7 -- all stand-alone); "
            "apprentice mages, chemists and adept guards; the conference room where kidnappings are "
            "planned (Rating 5 maglocks, hidden cameras); the Computer Room (Rating 6 maglocks, 7 to the "
            "research area; central computer and three Fuchi Cyber-6s); the Special Research Area (Rating "
            "7 maglock, cameras; AFD prototype on a Fuchi Cyber-7); chem lab; magic practice area padded "
            "with gym mats; a hermetic library (Conjuring 6, Magical Theory 6); senior mages' rooms "
            "(Rating 6 maglocks) and Akialoa's den; ornate brass double doors bearing a feathered serpent, "
            "two adepts who never leave them; and Naheka's lair -- a barren cavern masked as mountainside "
            "behind a Force 5 anchored mana barrier kept by a bound Force 4 earth elemental, opening into a "
            "carpeted suite of trid screens and simsense goggles (no bed; Lili's playroom, really), two "
            "terminals and two AFD prototypes. Maps pp.40-48."
        ),
        "notes": (
            "Perimeter: three Nene shamans meditating in a Rating 4 medicine lodge on top of the outcrop "
            "(the map calls it an Eagle shaman's lodge) -- two attack, one alerts; two watcher spirits "
            "warn Naheka first. Daniel casts Vehicle Mask for the approach if nobody else can, and "
            "baby-sits the copter. Six ork guards with wrist phones, two adepts asleep in 13D who feign "
            "sleep, two at Naheka's doors; alarms send every guard to the last reported position. By day "
            "everyone is at work (Lili jacked into the Cyber-7 with John, Wong and Chan watching; Cassidy "
            "Kane lecturing four apprentices; Walker, Apapane and Akialoa in the library; Jan, Kira and "
            "Flash decking; chemists in the lab; cooks cooking; two guards in the gym, unarmed). By night "
            "two guards patrol, two deckers work, a chemist and an apprentice watch trid, Naheka sleeps "
            "in serpent form. Interrogation (Willpower) ladder: cooks and shamans know rooms; adepts, "
            "chemists and guards know security; Wilkes, Toyoda and junior mages that Naheka is a powerful "
            "mage; Wong, Chan and Kalakaua the Special Research Area and that back-ups exist; senior mages "
            "that Naheka is a feathered serpent; only Lili the 'Honeydew' chip carrier. The back-up chip "
            "hides among trid chips (Intelligence (8), base 20 minutes; Red-5, Access 6, Scramble 7). "
            "Naheka's barrier was built to conceal, not resist: Daniel punches through it in the Airstar. "
            "Karma: find HQ +6, prototype +5, back-ups +8, deal +12, defeat or escape with the AFD +20. "
            "After the run all the cops will find is a pair of deserted caves."
        ),
    },
    {
        "name": "Waikiki",
        "location_type": "commercial district",
        "district": "Kapiolani Park and Diamond Head east, Kapiolani Boulevard west, the H1 north",
        "security_level": "Patrolled / Commercial",
        "city": "Honolulu",
        "summary": "The tourist district: five-star hotels, post-modern towers, ritzy clubs, restaurants that run credit checks, 1,000-nuyen rooms at the Outrigger Ala Moana and the Royal Hawai'ian",
        "description": (
            "A wonderland of five-star hotels, breathtaking post-modern architecture, ritzy nightclubs and "
            "restaurants that run a credit check before accepting a reservation. Virtually all the "
            "vacationers are high-level corporate executives; the population is dense but transient, "
            "'residents' being tourists in 1,000-nuyen-a-night rooms. Waikiki Beach is a stop on every "
            "tour bus; the HNPF Special Forces stage from here."
        ),
        "notes": (
            "Honolulu contacts: an evening on the town and a Charisma (10) Test finds a fixer in a karaoke "
            "bar who works the Waikiki Beach area; every 500-nuyen bribe lowers the legwork TN by one. "
            "Rachel Hong's restaurant is presumably here."
        ),
    },
    {
        "name": "Downtown Honolulu",
        "location_type": "commercial district",
        "district": "Financial district round Nuuanu Avenue and Beretania Street; King Street to the east",
        "security_level": "Corporate Standard",
        "city": "Honolulu",
        "summary": "Megacorp-logoed skyrakers round Nuuanu and Beretania, the Iolani Palace and Legislative Building on King Street, and 2M's tower near the nighttime hub",
        "description": (
            "Towering skyrakers each bearing a major megacorporation's logo. Greater Honolulu runs from "
            "Diamond Head west past Pearl Harbor and up the finger valleys of the Ko'olau range, swallowing "
            "Pearl City, Waipahu and Ewa Beach: 2,978,000 people (57 percent human, 22 ork, 12 elf, 9 "
            "troll), per-capita 31,000 nuyen, 1 percent below the poverty line, felony rate 7 per 1,000, "
            "33 hospitals. Fewer slums than Seattle and nothing like the Redmond Barrens or Hell's "
            "Kitchen. Most traffic rides the AutoGuide grid (autopilots lose one level on it); the big "
            "yellow Bus circles all of Oahu in four hours from the Ala Moana center."
        ),
        "notes": (
            "Honolulu's shadow community is smaller than Seattle's -- hard to enter or leave unofficially, "
            "nowhere to run -- but busier per runner and with faster turnover; fixers work only through "
            "people they know and trust, brag sheets be damned. ALOHA's Honda-GM 3220 ZX hit on the "
            "runners' Americar happens on these one-way streets (Toshi, Cameron, two gunners; Cameron's "
            "'Insurance' chip)."
        ),
    },
    {
        "name": "Ala Moana Shopping Center",
        "location_type": "mall",
        "district": "Waikiki edge; hub of The Bus",
        "security_level": "Patrolled / Commercial",
        "city": "Honolulu",
        "summary": "Five-floor shopping center where The Bus begins its four-hour circuit of Oahu -- and where eight-year-old Ellie Liluokalani fried two would-be kidnappers with her first mana bolt",
        "description": (
            "A five-storey shopping center and the tourist's boarding point for The Bus. Twenty-odd years "
            "ago two go-gang members tried to abduct a corporate executives' eight-year-old daughter here; "
            "hysterical with fear, she released a mana bolt that killed them both. The child became Mary "
            "Falls."
        ),
        "notes": "Flavor and back-story only; the Outrigger Ala Moana hotel stands nearby.",
    },
    {
        "name": "Iolani Palace and Legislative Building",
        "location_type": "government building",
        "district": "King Street, a short distance east of downtown's corporate core",
        "security_level": "Corporate High Security",
        "city": "Honolulu",
        "controlling_org": "Kingdom of Hawai'i",
        "summary": "Seat of the ali'i and the elected legislature; the capital next to the palace is where Danforth Ho's mob installed him as Kamehameha IV on Secession Day",
        "description": (
            "The Iolani Palace of the old monarchy and the Legislative Building, home to the elected branch "
            "of the government, both on King Street. On August 22 2017 hundreds of Na Kama'aina and "
            "thousands of civilians followed Danforth Ho into the capital building beside the palace, "
            "displaced the state officials and declared sovereignty."
        ),
        "notes": "Not visited in the adventure; the natural stage for any political follow-up in the Kingdom.",
    },
    {
        "name": "Punchbowl (Puowaina)",
        "location_type": "landmark / monument",
        "district": "Extinct crater above Greater Honolulu",
        "security_level": "Low Security",
        "city": "Honolulu",
        "summary": "'Hill of Sacrifices' -- old ritual site, former military cemetery emptied back to UCAS, public park by 2055, and by rumor a place of magical rituals after dark",
        "description": (
            "Once the site of human sacrifices and other great rituals of the Hawai'ian religion, then a "
            "20th-century military cemetery; after secession the government exhumed the dead and shipped "
            "them to UCAS with honors. As of 2055 it is a public park overlooking the sprawl. Secession "
            "Day stories tell of unnatural storms rolling down over Honolulu from this crater."
        ),
        "notes": "Rumor says mysterious magical rituals are held here after nightfall -- a natural kahuna or ALOHA meeting ground.",
    },
    {
        "name": "Diamond Head",
        "location_type": "landmark / monument",
        "district": "East of the city by Kapiolani Park",
        "security_level": "Low Security",
        "city": "Honolulu",
        "summary": "The holo-postcard crater at Waikiki's eastern end; a brisk forty-minute walk from Kapiolani Park to a view of the whole sprawl",
        "description": (
            "An extinct volcanic crater, subject of countless holo postcards, forming Waikiki's eastern "
            "boundary with Kapiolani Park. Forty minutes' brisk walk from the park reaches a vantage point "
            "over all of Greater Honolulu. Secession Day rumor puts 'activity' in the crater in August 2017."
        ),
        "notes": "Scenery for the tourist day; a quiet meet spot with one road out.",
    },
    {
        "name": "Kaiao Field (former Hickam AFB)",
        "location_type": "military installation",
        "district": "West of Honolulu, beside Awalani Airport",
        "security_level": "Zero Zone -- Lethal Response",
        "city": "Honolulu",
        "controlling_org": "Royal Hawai'ian Armed Forces",
        "summary": "Home of the Kingdom's small, lethal air force and the inherited U.S. hypersonic spy-plane research",
        "description": (
            "Formerly Hickam Air Force Base, half of whose land went to Awalani Airport. The Royal "
            "Hawai'ian Air Force flies from here on the 'large amounts of state-of-the-art technology' "
            "the islands inherited from America's pulse-detonation hypersonic spy-plane program."
        ),
        "notes": "Not visited; noted for the security climate around Awalani.",
    },
    {
        "name": "Pearl Harbor Naval Base",
        "location_type": "military installation",
        "district": "West of downtown Honolulu",
        "security_level": "Zero Zone -- Lethal Response",
        "city": "Honolulu",
        "controlling_org": "Royal Hawai'ian Armed Forces",
        "summary": "The Kingdom's navy and shipyard: thirty-year-old hulls with cutting-edge systems; the U.S. Pacific fleet's old home; 'something huge' near the Arizona Memorial in 2017",
        "description": (
            "America's primary central-Pacific naval and air base for a century, vital after the pullout "
            "from Okinawa and the Philippines and host after 2009 to relocated aerospace research. Half the "
            "Pacific fleet sailed from here in July 2017 and never came back. The Kingdom's naval vessels "
            "were on the shipyard slipways at secession; 5 percent of the fleet is always in dock for "
            "refits. Secession Day witnesses speak of something huge surfacing momentarily near the USS "
            "Arizona Memorial."
        ),
        "notes": "Not visited; the navy in practice holds the 50-km maritime jurisdiction.",
    },
    {
        "name": "Kahuku Point Research Site",
        "location_type": "military installation",
        "district": "North coast of Oahu",
        "security_level": "Zero Zone -- Lethal Response",
        "city": "Kahuku, Oahu",
        "controlling_org": "Royal Hawai'ian Armed Forces",
        "summary": "The 'mysterious research site' -- a U.S. military zero zone for 'less savory projects' inherited whole by the Kingdom",
        "description": (
            "When the U.S. moved sensitive research off disputed mainland ground after the Lone Eagle "
            "incident, it put its aerospace projects at Pearl Harbor and its 'less savory' ones in a "
            "military zero zone near Kahuku Point. The Hawai'ian government keeps the same security "
            "America did; the average citizen knows nothing, and 'speculating about them too much can be "
            "hazardous to the health'."
        ),
        "notes": "Pure hook -- black projects with no book detail.",
    },
    {
        "name": "Space City (Haleakala)",
        "location_type": "military installation",
        "district": "Summit of Mount Haleakala",
        "security_level": "Zero Zone -- Lethal Response",
        "city": "Maui",
        "controlling_org": "Royal Hawai'ian Armed Forces",
        "summary": "The old SDI 'Star Wars' facility atop Haleakala, grown huge after 2000 and inherited by the Kingdom; rumors of magical experiments in the crater",
        "description": (
            "A major player in the 1980s Star Wars program that grew considerably larger after the turn "
            "of the century despite the program's official end. The crater below erupted on November 15 "
            "2017, a magical 'echo' of the Great Ghost Dance three months earlier. Best-known of the "
            "inherited facilities and as closed as ever; a few people speculate the government is running "
            "magical experiments in the crater to supplement the armed forces."
        ),
        "notes": "Not visited. Secession Day rumor lists 'activity in the Haleakala crater'.",
    },
    {
        "name": "Kaho'olawe Bombing Range",
        "location_type": "military installation",
        "district": "The whole island, off-limits",
        "security_level": "Zero Zone -- Lethal Response",
        "city": "Kaho'olawe",
        "controlling_org": "Royal Hawai'ian Armed Forces",
        "summary": "Testing ground and bombing range of the Royal Hawai'ian Armed Forces -- somebody is blowing the drek out of it most days and nights",
        "description": "Off-limits, and for good reason: on any given day or night there is a good chance the military is out there blowing the drek out of it.",
        "notes": "No airport, no civilians; a place to lose a body or a boat.",
    },
    {
        "name": "Ni'ihau Preserve",
        "location_type": "restricted preserve",
        "district": "The whole island; restricted waters and airspace",
        "security_level": "Zero Zone -- Lethal Response",
        "city": "Ni'ihau",
        "controlling_org": "Royal Hawai'ian Armed Forces",
        "summary": "Officially a preserve for a colony of 'traditional' aboriginal Hawai'ians in grass huts; in practice patrolled by a military that sinks any boat or plane without asking for ID",
        "description": (
            "In theory a preserve for a small colony of aboriginal Hawai'ians who have not bought into the "
            "19th century, let alone the 21st, living in grass huts on fish they net and spear. In "
            "practice the Royal Hawai'ian Armed Forces patrol the surrounding water and sink or splash "
            "anything entering the restricted space. No airport. 'Explain to me why...'"
        ),
        "notes": "Untouched hook: what is really on Ni'ihau? Northernmost island, hurricane-prone.",
    },
    {
        "name": "Wailea Ruins",
        "location_type": "ruins",
        "district": "South Maui, buried by the 2017 Haleakala eruption",
        "security_level": "No Security / Barrens",
        "city": "Maui",
        "summary": "'The Pompeii of the Pacific' -- the resort town buried when Haleakala erupted on November 15 2017",
        "description": (
            "The town of Wailea on Maui was buried by the eruption of Haleakala on November 15 2017, three "
            "months after the Great Ghost Dance and, analysts now believe, a magical echo of it. Weather "
            "patterns changed across the islands at the same time."
        ),
        "notes": "Not visited; Kinu grew up a gang leader somewhere on Maui in the shadow of it.",
    },
]

NPCS = [
    {
        "name": "Mary Falls",
        "role": "Owner of MFI and the runners' Mr. Johnson; born Ellie Liluokalani in Honolulu, a corporate-raised mage prodigy who ran away to build her own company",
        "archetype": "Corporate Executive / Hermetic Mage",
        "title": "President and sole owner, Mary Falls, Inc. (the 'Mr. Johnson')",
        "race": "Human",
        "gender": "Female",
        "nationality": "Kingdom of Hawai'i (Honolulu-born); lives in Seattle",
        "age": 34,
        "organization": "Mary Falls, Inc. (MFI)",
        "connection": 5,
        "description": (
            "A woman in her mid-30s in blue-and-gray corporate chic, brown hair sleeked into a severe "
            "chignon, round black-rimmed spectacles, a sharp catlike face -- 'if she lost the glasses and "
            "let her hair down she might look quite attractive'. Says little through a sumptuous dinner, "
            "then: 'Let's get down to business.' Types faster than unaugmented eyes can read; nature gave "
            "her what others buy as cyberware. Refuses to name herself or her company at the meet and "
            "drives a tough bargain. Trusts nobody."
        ),
        "background": (
            "Born Ellie Liluokalani to two corporate executives in Honolulu; her magic manifested at eight "
            "when two go-gangers tried to snatch her at the Ala Moana shopping center and she fried them "
            "with a mana bolt. The corporation sequestered her for twelve years of forced training toward a "
            "'devastatingly powerful wage mage' while her parents' status rose. She used the skills to "
            "vanish, took the first suborbital to Seattle, sold her talents until she could buy the assets "
            "of a bankrupt food manufacturer called Mary Falls, Inc., and took its name as her own. "
            "Genius runs in the Falls family 'once a generation' -- at 33 she owns a powerful mid-size "
            "corporation. Three years and millions of nuyen into the AFD, somebody stole it, and she "
            "trusts 2M less than anyone."
        ),
        "notes": (
            "Nobody in the adventure knows she is a mage; her one flaw is a paranoid fear of astral attack "
            "that keeps her from using foci. Stats: B3 Q6 S2 C5 I8 W7 E6 M8 R7; Init 7+1D6; TR 6/4; "
            "Computer 5, Conjuring 7, Cooking 3, Corporate Management 5, Economics 5, Etiquette "
            "(Corporate) 6, (Street) 5, Firearms 3, Interrogation 4, Leadership 6, Magical Theory 6, "
            "Marketing 6, Negotiation 7, Sorcery 7. Spells: Fireball 6, Manaball 6, Mana Bolt 7, Analyze "
            "Magic 7, Detect Enemies 5, Mind Probe 6, Antidote 4, Cure Disease 4, Increase Attribute +1, "
            "Increase Cybered Attribute +1, Treat 7, Improved Invisibility 5, Mask 6, Overstimulation 5, "
            "Armor 5, Barrier 6, Shapechange 5, Vehicle Mask 6. Gear: Ares Predator with laser sight, "
            "armor clothing 3/2, DocWagon Super-Platinum, wrist phone. Pays well and 'sings the team's "
            "praises' after success; if they refuse she trashes their reputation; if they talk afterward "
            "she has them killed. Honors a joint venture with Naheka. Sends the decker five AFDs."
        ),
        "contact_skills": ["Corporate money, cover identities and gear on demand", "Seattle food-industry and shell-company web"],
    },
    {
        "name": "Bounder",
        "role": "Troll chief of MFI security, born Sasha Griczuk -- a goblinized university prodigy whom Mary Falls gave a second life; heads the new electronics division in the success ending",
        "archetype": "Security Chief",
        "title": "Chief of security, Mary Falls, Inc.; later head of MFI's electronics division",
        "race": "Troll",
        "gender": "Male",
        "nationality": "UCAS (Seattle)",
        "age": 25,
        "organization": "Mary Falls, Inc. (MFI)",
        "connection": 3,
        "description": (
            "A large troll in his mid-20s, charming and still sharp-witted 'for a troll', a natural leader "
            "the rest of MFI security look up to. Unflagging loyalty to Mary Falls. Fights with a +1 reach."
        ),
        "background": (
            "Born human, the child of respected scientists Pavel and Eileen Griczuk; big for his age, bright "
            "and articulate, graduated high school at 15 and entered the University of Washington the next "
            "year. Six months later he goblinized; the change dulled his mind, the university expelled him "
            "and his parents disowned him. Odd jobs, then bouncing and bodyguarding under the name "
            "Bounder, until Mary Falls hired him for a business trip through NAN territory and offered "
            "him the security chief's job. The success news handout says Sasha Griczuk 'boasts a degree "
            "in economics from WSU' -- the book contradicts itself."
        ),
        "notes": (
            "His retinal pattern is temporarily on file at La Maison's back door. Stats: B11(12) Q4 S10 C3 "
            "I5 W3 E3.5 R4(6); Init 6+2D6; TR 6/4; Armed 3, Athletics 6, Economics 5, Etiquette (Corporate) "
            "4, (Street) 5, Firearms 6, Interrogation 6, Negotiation 4, Unarmed 7; dermal armor 1, "
            "smartlink, wired reflexes 1; smartlinked Ares Predator and Uzi III, armor vest 5/3, stun "
            "baton, DocWagon Platinum. The immaculate pinstriped troll who may hand-deliver the invitation "
            "is Egmond, not Bounder."
        ),
        "contact_skills": ["MFI corporate security and hiring", "Bouncer / bodyguard circuit"],
    },
    {
        "name": "Daniel Kapaa",
        "role": "MFI's only man in Hawai'i -- a wiz-kid street mage and Grade 3 initiate hiding as a bellboy-fixer at the Honolulu Hilton; 'Greetings from Auntie June'",
        "archetype": "Fixer / Street Mage",
        "title": "Personal expediter to Mary Falls; bellboy at the Honolulu Hilton",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "Mary Falls, Inc. (MFI)",
        "connection": 4,
        "description": (
            "A scrawny, tanned youth who insists on unpacking your bags, then looks you in the eye: "
            "'Greetings from Auntie June.' Gets on people's nerves, plays the simple guy hired for a "
            "simple job ('An A-F-what?'), grumbles about every request as if it came out of his hide, and "
            "delivers. 'If I told you, I'd have to kill you.' Refuses to discuss his magic -- 'a trick of "
            "the trade'."
        ),
        "background": (
            "Met Mary Falls when she first arrived in Seattle; she hired him as personal expediter when she "
            "bought MFI and sent him to Honolulu to watch the 2M joint venture. He built a reputation as a "
            "good fixer by doing nothing but watch, so nobody suspects the MFI link; the bell captain "
            "thinks he only runs illegal goods for rich guests and takes a cut. Prefers to help from a "
            "distance, but likes Mary enough to fly the team into Waimea Canyon himself."
        ),
        "notes": (
            "Supplies Streetline Specials, a loaned Fuchi Cyber-4 (Response Increase 1, 250/1,000 Mp; "
            "Attack 4, Bod 5, Decrypt 3, Evaluate 5 on AFD data only, Evasion 3, Masking 6, Medic 4, "
            "Mirrors 4, Sensors 4, Sleaze 4), a Ford Americar and two Yamaha Rapiers (maybe a Honda-GM "
            "3220 ZX), four easy gear requests then +1 Availability each, the Otter in a day or the "
            "Airstar in two. Casts Vehicle Mask on the approach, baby-sits the copter, then tails Naheka "
            "and blasts through the lair barrier with the Airstar's door open -- and will not risk himself "
            "for runners who picked a fight with a dragon. Wary of Kinu, then arms him. Hands over the "
            "bank passcodes for the fee. Stats: B2(4) Q4 S3 C5 I5 W5 E5.6 M7(9) R4; TR 5/4; Grade 3; Bike "
            "3, Car 4, Conjuring 4, Equipment Acquisition 6, Etiquette (Corporate) 6, (Street) 5, Firearms "
            "2, Magical Theory 4, Motorboat 3, Negotiation 6, Rotorcraft 3, Sorcery 7, Stealth 5, Unarmed "
            "5, Winged Planes 3. Spells: Fireball 6, Manaball 5, Mana Bolt 8, Clairvoyance 5, Detect "
            "Enemies 4, Heal 5, Treat 5, Improved Invisibility 5, Physical Mask 5, Trid Entertainment 5, "
            "Vehicle Mask 6, Armor 4. Gear: armor jacket, HK227 with laser, Power Focus 2, Spell Lock "
            "(Armor, usually off). Fires the team after a week of failure."
        ),
        "contact_skills": ["Honolulu fixer: weapons, vehicles, boats, helicopters inside a budget", "Vehicle Mask and a helicopter when it counts"],
    },
    {
        "name": "Egmond",
        "role": "Immaculately pinstriped troll bouncer who moonlights as a discreet courier; delivers Mary Falls' invitation to runners without a telecom",
        "archetype": "Troll Bouncer",
        "title": "Bouncer at a popular Seattle night spot; occasional courier",
        "race": "Troll",
        "gender": "Male",
        "nationality": "UCAS (Seattle)",
        "connection": 2,
        "description": (
            "A large troll in a pinstripe suit, deep gravelly voice, greets you by street handle, hands over "
            "a plain white envelope, bows as elegantly as a troll can and vanishes into the sidewalk crowd. "
            "'I'm sorry, but I don't know. I'm only a messenger.'"
        ),
        "notes": (
            "Hired by an MFI corporate guard he cannot identify. Troll Bouncer contact (SRII p.213) with "
            "Charisma 3, Etiquette (Street) 4 and (Corporate) 4; Beretta 101T in a jacket holster, stylish "
            "armor clothing. A reusable Seattle go-between for well-paying customers."
        ),
        "contact_skills": ["Discreet deliveries for well-paying customers"],
    },
    {
        "name": "Jeremy Ngok",
        "role": "Proprietor of La Maison d'Indochine, Bellevue's securest corporate dining room; keeps private quarters under the restaurant",
        "archetype": "Restaurateur",
        "title": "Proprietor, La Maison d'Indochine",
        "race": "Human",
        "gender": "Male",
        "nationality": "UCAS (Seattle)",
        "connection": 3,
        "description": (
            "Runs a French-Vietnamese restaurant whose reputation among corporate top dogs is safety; posts "
            "twelve guards behind the decor and pays Hard Corps for astral cover. Works late on promotions "
            "in a neat office behind a Rating 6 maglock and a Rating 7 passcard reader that only his card "
            "opens, sleeps downstairs when he chooses not to go home, and 'discreetly entertains company' "
            "there."
        ),
        "notes": "Bartender archetype with Restaurant Management 5. Rents the lower-level private rooms by the evening -- MFI has one tonight. A man who knows who dined with whom.",
        "contact_skills": ["Who is meeting whom over dinner in Bellevue"],
    },
    {
        "name": "Hackpool",
        "role": "The mediocre elven decker whose burnt-out REX modifier survived megacorp black IC, founding MFI's AFD project; died testing it (deceased)",
        "archetype": "Decker",
        "title": "Head of AFD research, Mary Falls, Inc. (deceased, c. 2053)",
        "race": "Elf",
        "gender": "Male",
        "nationality": "UCAS (Seattle)",
        "organization": "Mary Falls, Inc. (MFI)",
        "connection": 1,
        "description": "A luckless, unremarkable Seattle decker with a second-rate deck and no elegant defense utilities -- until the antique REX signal modifier he bought at a pawnshop saved his life.",
        "background": (
            "Late fall 2051: an unguarded golden globe icon, a gaping maw of bloody teeth, and a slammed "
            "return to a body that should have been dead; the REX had short-circuited the biofeedback "
            "loop and slagged itself. Its maker had been bankrupt twenty years. Through a Mr. Johnson he "
            "reached MFI, which hired him to head the research team. A working REX killed a test decker; "
            "more than a year later Hackpool himself succumbed to black IC testing a preliminary AFD."
        ),
        "notes": "Deceased; the reason Mary Falls' name is on every AFD. The megacorp whose IC he tripped was never identified.",
    },
    {
        "name": "Preacher",
        "role": "Ork-activist leader (a.k.a. John Picarille), national spokesman for the ork and troll underclass; believed target of the Redmond Barrens storefront shooting",
        "archetype": "Activist",
        "title": "Ork-rights activist; spokesman, Ork Rights Committee",
        "race": "Ork",
        "gender": "Male",
        "nationality": "UCAS (Seattle)",
        "organization": "Ork Rights Committee",
        "connection": 3,
        "description": "Since his first public appearance at an open Seattle Council meeting two years ago he has risen to a highly visible national position. 'But who is Preacher, and what does he really stand for?'",
        "notes": "Seattle Datafax, February 2055: masked gunmen (Alamos 20,000 blamed) hit the Committee's Redmond Barrens storefront, six dead including a four-year-old; authorities believe Preacher was the target. News-handout figure only.",
    },
    {
        "name": "Robbie \"Kinu\" Kurosawa",
        "role": "Maui gang lord turned ALOHA spy inside Mitsuhama; led the MCT lab raid, handed the AFD to Naheka, and is now marked for death by both masters",
        "archetype": "Espionage Operative / Street Samurai",
        "title": "ALOHA espionage operative; MCT undercover assault leader (burned)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i (three-quarters Polynesian)",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 4,
        "description": (
            "Over six feet, strong and lean, 'looks like a Hawai'ian god' despite the Japanese surname; first "
            "seen in jungle camo lighting a cigarette in a starlit clearing while a man raises an AK-97 "
            "('I was just about to ask if you'd like a last cigarette'). A gutter rat to the bottom of his "
            "shriveled soul, a real survivor, and lately a believer."
        ),
        "background": (
            "Prominent gang leader on Maui in his youth, recruited by both ALOHA and Mitsuhama and "
            "opportunist enough to join both; over the years he fed Naheka valuable information and "
            "gradually came to believe. He led MCT's assault on the Makai lab, tipped Naheka, watched the "
            "serpent drown his own team, and told MCT a kraken did it. Then MCT sent him back to Makai to "
            "'search for evidence' with three soldiers ordered to kill him, and ALOHA changed its "
            "communication protocol without telling him. Betrayed twice, he wants a new life -- and part "
            "of him wants to even the score with Naheka."
        ),
        "notes": (
            "Offers 20,000 nuyen for a ride to Honolulu; level with him about MFI and he tells all "
            "(ALOHA legwork, the raid, his role). Believes Naheka is a powerful mage, never a serpent; "
            "has never been inside the HQ but knows it is in Waimea Canyon; will guide the team there "
            "for a 200,000-nuyen stake (negotiable) and opens the palm scanner. Talks the team off Makai "
            "('an angry corporate assault team awaits'), mans the Otter's rear gun. Stats: B6(8) Q6 S7 C5 "
            "I5 W3 E2.7 R5(7); Init 7+2D6; TR 6/4; Athletics 6, Etiquette (Corporate) 3, (Street) 5, "
            "Firearms 6, Gunnery 6, Interrogation 5, Leadership 5, Military Theory 4, Motorboat 4, "
            "Stealth 5, Unarmed 7; cybereyes (low-light, normal appearance), dermal plating 2, fingertip "
            "compartment with a monofilament whip, wired reflexes 1; Daniel gives him an AK-97 and a "
            "knife. Afterwards a Honolulu contact with no home to go to."
        ),
        "contact_skills": ["ALOHA's structure, field agents and Waimea Canyon", "Mitsuhama's Hawai'ian operations", "Maui gang connections"],
    },
    {
        "name": "Naheka",
        "role": "Feathered serpent, vassal of the great dragon Ryumyo, secret leader of ALOHA; has the AFD prototypes and sees (meta)humans as resources to be expended",
        "archetype": "Feathered Serpent (dracoform)",
        "title": "Leader of ALOHA; vassal of the Great Dragon Ryumyo",
        "race": "Feathered serpent",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 5,
        "description": (
            "Almost thirty meters of brilliant-colored feathered serpent with rows upon rows of swordlike "
            "teeth, landing in his cavern on a sudden gale; in human form a 'brilliant man with fantastic "
            "magical power' whom his followers revere. Beneath the beauty a cold, uncaring heart -- he "
            "mind-sifts the captured 2M scientist to an empty shell, crushes him in his coils and "
            "swallows him. Patient as only a dracoform is; strikes quickly and cleanly when he must. "
            "Naheka means snake."
        ),
        "background": (
            "Soon after independence Ryumyo ordered him to take over ALOHA and keep up the fight for "
            "Polynesian sovereignty; he does not care who rules Hawai'i but maintains the pressure on the "
            "government at his master's bidding, and every act somehow furthers Ryumyo's goals. Duping "
            "MFI, 2M and 'the powerful and hated Mitsuhama' at once pleased him greatly. His interest in "
            "the AFD is strictly money to fund ALOHA."
        ),
        "notes": (
            "Sleeps in serpent form in a cavern masked as mountainside behind a Force 5 anchored barrier "
            "(concealment, not defense). Fight him and die; run and he waits outside the caves; negotiate "
            "and he gladly deals: 50 percent of AFD net sales through a joint venture with MFI (+/-1 "
            "percent per net Negotiation success), the team's silence on pain of a vengeance 'no place in "
            "the world can hide you from' (he cares little; he is already leaving Waimea Canyon), then "
            "shapechanges to human and drafts the letter of agreement to MFI's e-mail. Robbed, he hunts "
            "the runners as an ongoing nemesis. Stats: B12(8) Q7x2 (x4 flying) S32 C6 I6 W8 E10 M8 R7; "
            "Init 7+2D6; 12D +2 Reach; TR 7/4; Conjuring 6, Etiquette (Tribal) 6, Interrogation 6, "
            "Leadership 5, Magical Theory 6, Negotiation 6, Psychology 5, Sorcery 8. Spells: Manablast 6, "
            "Sleep 7, Analyze Truth 5, Mind Probe 8, Mask 5, Overstimulation 7, Mana Barrier 8. Enhanced "
            "Senses (low-light, thermal, wide-band hearing), Hardened Armor. Failing a deal, sells the AFD "
            "to Fuchi for 10 million nuyen. If killed, Ryumyo finds another vassal."
        ),
    },
    {
        "name": "Serena Day",
        "role": "Tall blond elf, one of the Haoles' best operatives; freelanced 2M intel to Daniel Kapaa, was marked for death, and throws the runners the satchel at the luau",
        "archetype": "Information Broker",
        "title": "Operative, Haoles Don't Surf (on the run)",
        "race": "Elf",
        "gender": "Female",
        "nationality": "Kingdom of Hawai'i",
        "organization": "Haoles Don't Surf",
        "connection": 3,
        "description": (
            "Tall, blond, ponytail with shaved sides like the men chasing her, sprinting across the luau "
            "grounds to toss a small leather satchel your way. Once paid, a fount of 'deathless prose': "
            "'2M's a piddly bunch of research geeks...' 'Say, you guys don't work for that corp, do you? "
            "Got any job openings for a resourceful, attractive, talented elf?'"
        ),
        "background": (
            "Her bosses refused Daniel's request for 2M information; she went solo for the money. She "
            "copied the passcard of her former lover Alan Jenkins when the affair soured, and gave it to "
            "the runners knowing 2M's logs would hang the break-in on him. Won't sell out her chummers "
            "in the gang: 'It ain't got nothin' to do with 2M.'"
        ),
        "notes": (
            "Rescued within five turns, she sells everything for 2,500 nuyen (a suborbital seat to "
            "Seattle) and hopes for shelter in Tir Tairngire: 2M's size and habits, the raid's inside "
            "help and 'major support', a Seattle corp paying 2M to grease labcoats, the off-Matrix lab "
            "computer marked on the plan, the mosquito couriers, the guard rigged into building security "
            "and the ten-minute response, ALOHA's spies. Begs a ride to the airport. Unrescued, she "
            "vanishes. Stats: B3 Q5 S2 C6 I5 W4 E6 R5; TR 3/3; Electronics 4, Etiquette (Corporate) 3, "
            "(Street) 6, Negotiation (Fast Talk) 6, Unarmed 4; knife, Streetline Special."
        ),
        "contact_skills": ["Honolulu underground information network", "2M and the Anglo night-spot scene"],
    },
    {
        "name": "Kristo",
        "role": "Ork enforcer of Haoles Don't Surf who leads the four sent to 'terminate Serena Day's membership'",
        "archetype": "Gang Enforcer",
        "title": "Enforcer, Haoles Don't Surf",
        "race": "Ork",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "Haoles Don't Surf",
        "connection": 1,
        "description": "Ponytail with shaved sides, armor vest under the tropical shirt, a vicious street gladiator who flees when the fight turns.",
        "notes": "B7 Q4 S7 C2 I4 W2 E6 R4; TR 4/3; Armed 4, Etiquette (Street) 4, Firearms 5, Unarmed 3; armor vest 2/1, Colt American L36 in a concealable holster, sap (9M Stun). Catches Serena outside the grounds unless stopped.",
    },
    {
        "name": "Marcus",
        "role": "Human enforcer of Haoles Don't Surf hunting Serena Day at the Kona Kalaa Luau",
        "archetype": "Ganger",
        "title": "Enforcer, Haoles Don't Surf",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "Haoles Don't Surf",
        "connection": 1,
        "description": "One of the three human bruisers with the gang's ponytail-and-shaved-sides cut who chase the elf across the luau.",
        "notes": "B3 Q3 S4 C3 I3 W4 E6 R3; TR 3/2; Armed 4, Etiquette (Street) 4, Firearms 3; armor vest, Colt American L36, sap. Fights hard, runs when losing.",
    },
    {
        "name": "Tor",
        "role": "Human enforcer of Haoles Don't Surf hunting Serena Day at the Kona Kalaa Luau",
        "archetype": "Ganger",
        "title": "Enforcer, Haoles Don't Surf",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "Haoles Don't Surf",
        "connection": 1,
        "description": "Second of Kristo's three human enforcers.",
        "notes": "Same block as Marcus: B3 Q3 S4 C3 I3 W4 E6 R3; TR 3/2; armor vest, Colt American L36, sap.",
    },
    {
        "name": "Stefano",
        "role": "Human enforcer of Haoles Don't Surf hunting Serena Day at the Kona Kalaa Luau",
        "archetype": "Ganger",
        "title": "Enforcer, Haoles Don't Surf",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "Haoles Don't Surf",
        "connection": 1,
        "description": "Third of Kristo's three human enforcers.",
        "notes": "Same block as Marcus: B3 Q3 S4 C3 I3 W4 E6 R3; TR 3/2; armor vest, Colt American L36, sap.",
    },
    {
        "name": "Alan Jenkins",
        "role": "2M account executive and Serena Day's ex-lover whose copied passcard the runners use -- 2M's logs will blame him for the break-in",
        "archetype": "Corporate Account Executive",
        "title": "Account executive, Molokai Microtronics",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "Molokai Microtronics (2M)",
        "connection": 2,
        "description": "Never met. A 31st-floor account man who let a Haole elf close enough to copy his passcard; his thumbprint is what the main-door scanner expects.",
        "notes": "The card opens the front door and the elevator to 31 only. Serena copied it as leverage when the relationship soured and gave it away to buy him 'a drekload of trouble'. A ruined man looking for whoever used his name -- a loose end.",
    },
    {
        "name": "Ted Dackson",
        "role": "President of Molokai Microtronics, mostly in Hong Kong entertaining clients; part of the 'top corpboys' who sold the AFD to Mitsuhama and took compensation for the dead",
        "archetype": "Corporate Executive",
        "title": "President, Molokai Microtronics",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "Molokai Microtronics (2M)",
        "connection": 3,
        "description": "Keeps a spartan Honolulu office (oak desk, ergonomic chair, terminal) he rarely uses; works out of the Hong Kong office or entertains new clients with his son-in-law Phillip Savage.",
        "notes": "His diary sits in DS-11 of the 2M main system (Orange-6). Not present during the break-in. 'The top brass here didn't seem too upset.'",
    },
    {
        "name": "Phillip Savage",
        "role": "2M's Vice-President of Marketing -- an ex-professional Urban Brawl star who married President Dackson's daughter, a former fan",
        "archetype": "Corporate Executive / ex-Urban Brawler",
        "title": "Vice-President, Marketing, Molokai Microtronics",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "Molokai Microtronics (2M)",
        "connection": 3,
        "description": "An office crowded with artwork and a shelf of Urban Brawl trophies; owes his job to the tenacity that made him famous and to his marriage. Travels with Dackson.",
        "notes": "Installed his own Rating 5 keypad and an infrared laser grid across the whole office (seven-digit code; 5S discharge, 5L for three turns while recharging; visible with thermographic vision in the dust). Terminal I/OP-32 (Green-5). Absent during the break-in.",
    },
    {
        "name": "Ahmed Virani",
        "role": "2M's Vice-President of Accounts Management, working late jacked into the company system the night of the break-in; a coward who guides captors through the security and dreams of revenge",
        "archetype": "Corporate Executive / Decker",
        "title": "Vice-President, Accounts Management, Molokai Microtronics",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "Molokai Microtronics (2M)",
        "connection": 3,
        "description": "Tasteful holographic prints and exotic plants; curtains drawn, security off, jacked into a Fuchi Cyber-6 with all the passcodes and no extra utilities. Avoids combat; quails at the thought of it.",
        "notes": (
            "Stats: B3 Q3 S3 I5 W5 E5.8 R4(6); Matrix Init 6+2D6; TR 2/1; Computer 5, Corporate Accounting "
            "6, Etiquette (Corporate) 7, Negotiation 4; datajack; Fuchi Cyber-6 (Persona 6, Hardening 3, "
            "Bod 7, Masking 4, Sensors 5). A decker in the 2M system may rouse his curiosity. Captured, "
            "he opens every room but his fellow seniors' offices and consoles himself with fantasies of "
            "tracking the team down later -- a future enemy with a corporate budget."
        ),
    },
    {
        "name": "Rosenkrantz",
        "role": "Ahmed Virani's dwarf bodyguard in a tailored armored-cloth suit, watching the dark 31st-floor hallway",
        "archetype": "Bodyguard",
        "title": "Bodyguard to Ahmed Virani, Molokai Microtronics",
        "race": "Dwarf",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "Molokai Microtronics (2M)",
        "connection": 1,
        "description": "Stylishly dressed, keeps a sharp eye on the office door and the area nearby; at any sign of movement where there should be none he blends into the shadows and investigates, never straying far from Ahmed.",
        "notes": "Bodyguard archetype (SRII p.49) with Threat/Professional Rating 5/4 in place of dice pools; uses Stealth. The invisibility spell got the ALOHA team past him.",
    },
    {
        "name": "Leslie Chao",
        "role": "2M's new Vice-President of Personnel and Payroll, whose office she has not yet decorated",
        "archetype": "Corporate Executive",
        "title": "Vice-President, Personnel and Payroll, Molokai Microtronics",
        "race": "Human",
        "gender": "Female",
        "nationality": "Kingdom of Hawai'i",
        "organization": "Molokai Microtronics (2M)",
        "connection": 2,
        "description": "The newest senior suit; a bare office behind the standard Rating 4 door security.",
        "notes": "Her terminal (I/OP-31, Orange-6) reaches DS-7 office personnel and DS-8 lab personnel and mosquito couriers. Presumably replaced someone killed in the boardroom.",
    },
    {
        "name": "Derek Hanna",
        "role": "2M's financial controller and oldest executive; the company's central computer sits in his laser-gridded, nerve-gassed office",
        "archetype": "Corporate Executive",
        "title": "Vice-President, Accounting and Finance; financial controller, Molokai Microtronics",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "Molokai Microtronics (2M)",
        "connection": 3,
        "description": "The old man of the executive floor, custodian of the central computer and the nine-digit code.",
        "notes": "Office: Rating 7 keypad with Anti-tamper 2, 10S infrared lasers, terminal retinal scanner Rating 5 that vents Green Ring 3 nerve gas (8S) on strangers. Terminal I/OP-34 (Red-4). Knows where the money from Mitsuhama went.",
    },
    {
        "name": "Janet Kaniko",
        "role": "2M's account supervisor for the AFD project, killed in the boardroom massacre; rumored to have hidden AFD data at a second lab (she had not) -- deceased",
        "archetype": "Corporate Account Supervisor",
        "title": "Account supervisor, AFD project, Molokai Microtronics (deceased)",
        "race": "Human",
        "gender": "Female",
        "nationality": "Kingdom of Hawai'i",
        "organization": "Molokai Microtronics (2M)",
        "connection": 1,
        "description": "Dead two weeks before the runners arrive, shot with everyone else at the MFI/2M progress meeting.",
        "notes": "The rumor about her hidden back-up is what brings the ALOHA squad to the research room the same night as the runners; Koyashi is hunting for her password by terminal light. One of DS-4 to DS-23 was hers.",
    },
    {
        "name": "Mark Koyashi",
        "role": "ALOHA's mole at 2M -- an account supervisor who leaked the AFD project and lab, and the only captured ALOHA member who talks",
        "archetype": "Corporate Mole",
        "title": "Account supervisor, Molokai Microtronics; ALOHA field agent",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 2,
        "description": "An account man, not a warrior: plays tough, then folds. 'Naheka wouldn't tell me anything like that.' Brightens about his leader: 'A brilliant man, with fantastic magical power. He'll give Hawai'i back to us natives.' Has only ever seen Naheka in human form.",
        "background": "Fed ALOHA the AFD details and the lab location; then 'an assault team from I don't know where destroyed the lab and made a hit on this office'. Knows ALOHA could not have fielded that force and still ended up with the AFD. The book calls him accountant, account executive and account supervisor.",
        "notes": "Stats: B2 Q3 S2 C5 I5 E6 R4; TR 2/2; Electronics (B/R) 3, Engineering 4, Etiquette (Corporate) 4, Negotiation 5; pocket secretary. Reveals the HQ location only on pain of death, and nothing more -- he expects more forgiveness from ALOHA than mercy from the runners.",
        "contact_skills": ["2M's accounts and research bookkeeping"],
    },
    {
        "name": "Kala",
        "role": "Ork ALOHA fighter who keeps watch on the 2M hallway through a gap in the curtain",
        "archetype": "Terrorist Soldier",
        "title": "ALOHA operative (2M break-in team)",
        "race": "Ork",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 1,
        "description": "Big, quiet, watching the hall while Koyashi works by terminal light. Says nothing under interrogation even on pain of death.",
        "notes": "B8 Q3 S7 C1 I3 W3 E6.5 R3; TR 3/4; Armed 3, Etiquette (Street) 3, Firearms 4, Unarmed 4; smartlink; smartlinked Ares Predator, armor vest 2/1. Lightly armed for a deserted office.",
    },
    {
        "name": "Stack",
        "role": "Well-armed ALOHA street samurai who strung the monowire across the 2M research-room door",
        "archetype": "Street Samurai",
        "title": "ALOHA operative (2M break-in team)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 1,
        "description": "The squad's gun; his 'nasty surprise' is a strand of monowire a meter off the floor on the hallway side of the door. Blindly loyal.",
        "notes": "Attribute line lost in the book's layout; skills Electronics (B/R) 5, Firearms 6, Unarmed 4; datajack, smartlink, 100 Mp; Ares Viper Slivergun with flechette, armor vest, low-light goggles. Monowire: Perception (6) to spot, 11S/9S/7S running/walking/grabbing.",
    },
    {
        "name": "Kanaka",
        "role": "ALOHA's Gecko (Mo'o) shaman who walked the squad past Rosenkrantz under Invisibility",
        "archetype": "Shaman (Gecko)",
        "title": "ALOHA shaman (2M break-in team)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 2,
        "description": "A prankster's totem in a terrorist's service: fast, adaptable, impossible to pin down, and apt to assume his friends can slip trouble as easily as he does. Refuses to speak if captured.",
        "notes": "Q5 S4 C4 I3 W5 M6; TR 3/4; Armed 3, Athletics 3, Conjuring 3, Etiquette (Street) 3, Firearms 3, Sorcery 4, Stealth 4; Analyze Device 4, Analyze Truth 3, Chaos 5, Heal 4, Invisibility 6, Manaball 3; knife. Gecko: +2 dice manipulation/illusion, +1 die vs poison, -1 die combat spells.",
    },
]

NPCS += [
    {
        "name": "Toshi",
        "role": "Grinning ork in a tropical shirt who leans out of a black Honda-GM with an Uzi: 'Aloha from ALOHA! E make loa, haole!'",
        "archetype": "Terrorist Gunman",
        "title": "ALOHA hit-squad gunner",
        "race": "Ork",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 1,
        "description": "Drek-eating grin, tropical shirt, submachine gun. Gets one free shot.",
        "notes": "B8 Q4 S6 C2 I2 W3 E3 R6; TR 4/3; Etiquette (Street) 4, Firearms 5, Unarmed 2; armor vest, Uzi III with two spare clips. Near the top of the HNPF's Most Wanted list; the cops forget the runners exist once they see who died.",
    },
    {
        "name": "Cameron",
        "role": "Paranoid sociopath rigger who drives ALOHA's hit squad and carries an 'Insurance' chip -- a map of Waimea Canyon, a diary of the AFD job, and a plan to kidnap Blitzkrieg",
        "archetype": "Rigger",
        "title": "ALOHA hit-squad driver",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 1,
        "description": "Drives the Honda-GM 3220 ZX Turbo rigged, rams rather than shoots, packs a Colt he never draws. His diary is an unpleasant guided tour through a twisted mind: death, destruction, destiny, and 'motherfragging rich haole slots'.",
        "background": "Kept out of everything by 'slotting high-ups', he built a bargaining chip for the day he wanted out of ALOHA and never finished it. 'Wish I could go; hosing down a corp office sounds wiz.'",
        "notes": (
            "B4 Q4 S3 C1 I5 W3 E4 R4; rigging Init 6+2D6; TR 3/3; Car 4, Car (B/R) 5, Computer 3, "
            "Electronics 4, Firearms 3; VCR 1; Colt American L36. The chip (Rating 6 scramble): 'Canyon' "
            "(rough map with the HQ entrance), 'Life Insurance' (diary; entries 1-14 and 1-18 name MFI, "
            "2M, Mitsuhama's plan and 'one of our ops on 2M lab hit squad'), 'Blitzkrieg' (a plan in "
            "progress to kidnap the European synthrock group on their Honolulu date -- major paydata "
            "unrelated to the run)."
        ),
    },
    {
        "name": "Audrey Wilkes",
        "role": "ALOHA's house manager who rules the canyon's kitchen and cleaning staff with an iron (cyber)hand; many years with the cause, trusted by Naheka",
        "archetype": "House Manager",
        "title": "House manager, ALOHA headquarters",
        "race": "Human",
        "gender": "Female",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 2,
        "description": "Found poring over supply inventories on a stand-alone tabletop computer; a cyberhand with a built-in phone, recording cyberears, a datajack.",
        "notes": "B1 Q3 S2 C2 I3 W3; TR 2/1; Accounting 4, Computer 3, Etiquette (ALOHA) 4, Firearms 3, Negotiation 3, Office Procedures 3; datajack 200 Mp; Colt American L36. Master passcard to everything except Naheka's cave. Interrogated, she knows the general security and that Naheka is a powerful mage.",
    },
    {
        "name": "Kehlani",
        "role": "Elven cyber-rock musician resident at ALOHA HQ; jams so loud she never hears the raid",
        "archetype": "Musician",
        "title": "Resident musician, ALOHA headquarters",
        "race": "Elf",
        "gender": "Female",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 1,
        "description": "Half of the duo that plays after-hours concerts for the hard-working terrorists; decked into her instruments in a practice room full of acoustic and computer-controlled gear, oblivious unless physically attacked.",
        "notes": "Media Producer contact with Computer 4, Unarmed 3, Instrumental Music 4, datajack (Essence 5.8). Knows the rooms; nothing about the AFD.",
    },
    {
        "name": "Karla",
        "role": "Elven cyber-rock musician resident at ALOHA HQ, Kehlani's partner",
        "archetype": "Musician",
        "title": "Resident musician, ALOHA headquarters",
        "race": "Elf",
        "gender": "Female",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 1,
        "description": "Shares two pleasantly decorated rooms with Kehlani, one to live in and one to practice in.",
        "notes": "Same block as Kehlani (Media Producer contact, Instrumental Music 4, datajack).",
    },
    {
        "name": "Merill Toyoda",
        "role": "ALOHA's accountant and financial manager, keeper of a red-plush, Egyptian-themed room full of ceramic cats and one very real Awakened one",
        "archetype": "Accountant",
        "title": "Accountant and financial manager, ALOHA",
        "race": "Human",
        "gender": "Female",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 2,
        "description": "Hard at work on complex calculations behind a Rating 5 maglock; low-light cybereyes, a datajack, a telephone. Her quarters need no lock -- her cat guards them.",
        "notes": "B2 S2 C2 I5 W4 E4.3 R4; TR 2/2; Accounting 6, Car 4, Climbing 3, Computer 3, Etiquette (Corporate) 4; tortoise computer. Terminal I/OP-4 on the main system only. The cat: B3 Q5x4 S2 W4 R5, Init 5+2D6, 6M claws, powers Fear and Electrical Projection (6M). Knows the security; thinks Naheka is a mage.",
    },
    {
        "name": "Peter Wong",
        "role": "ALOHA computer technician who maintains the caves' data and telecom gear, rewrites programs, runs the conference-room cameras and assists the deckers",
        "archetype": "Computer Technician",
        "title": "Computer technician, ALOHA headquarters",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 2,
        "description": "Tastefully furnished quarters; watching Lili test the AFD when the runners arrive. Transmits messages to ALOHA members across the islands and beyond from the Computer Room.",
        "notes": "B3 Q5 S2 C3 I5 W4 E5.5 R5; TR 2/2; Accounting 5, Computer 6, Computer (B/R) 5, Computer Theory 6, Electronics 5, Electronics (B/R) 5, Etiquette (Matrix) 6, Unarmed 5; datajack; passcards for the Computer Room and Special Research Area. Knows the AFD staff work in the research area and that back-ups exist 'somewhere'.",
    },
    {
        "name": "Peter Chan",
        "role": "ALOHA computer technician, Peter Wong's partner in keeping the caves' systems running",
        "archetype": "Computer Technician",
        "title": "Computer technician, ALOHA headquarters",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 2,
        "description": "The other half of 'Wong and Chan'; same rooms, same work, same passcards.",
        "notes": "Identical block to Peter Wong (Computer 6, Computer Theory 6, Electronics 5, Etiquette (Matrix) 6; datajack). Same interrogation tier.",
    },
    {
        "name": "Jan",
        "role": "Junior ALOHA decker caught surfing Awalani Airport's systems from the Computer Room",
        "archetype": "Decker",
        "title": "Junior decker, ALOHA",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 1,
        "description": "A young man jacked in and far away when the runners come through the door; Kira stands by to pull his plug.",
        "notes": "Junior decker block: B3 Q4 S2 C3 I5 W3 E5.8 R4; Matrix Init 8+3D6; TR 3/3; Computer 6, Computer (B/R) 6, Electronics 5, Firearms 3, Unarmed 3; Colt American L36, wrist radio; Fuchi Cyber-6 (MPCP 8, Hardening 4, 100/500; Bod 7, Evasion 5, Masking 6, Sensors 6; Attack 5, Browse 6, Decrypt 4, Medic 3, Mirrors 5, Sleaze 5; Response Increase 1 -- the room text says 2). Passcards for the Computer Room and research area.",
    },
    {
        "name": "Kira",
        "role": "Junior ALOHA decker standing ready to jack Jan out; caps off a couple of rounds and flees when trouble arrives",
        "archetype": "Decker",
        "title": "Junior decker, ALOHA",
        "race": "Human",
        "gender": "Female",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 1,
        "description": "The one on her feet in the Computer Room, and the first to react.",
        "notes": "Same block as Jan (Computer 6, Fuchi Cyber-6, Colt American L36). Fires two rounds, then runs -- and raises the alarm.",
    },
    {
        "name": "Flash",
        "role": "Junior ALOHA decker jacked into the central system watching the cameras on the research area, chem lab and magic practice area",
        "archetype": "Decker",
        "title": "Junior decker, ALOHA (security monitor)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 1,
        "description": "Gathering and analyzing camera feeds from inside the system; anything odd on a screen and he alerts the guards.",
        "notes": "Same block as Jan. He is the reason the Special Research Area cannot be entered quietly on camera; kill the cameras (SM-1, Red-4) or him first.",
    },
    {
        "name": "John Kalakaua",
        "role": "ALOHA's veteran decker, father of the prodigy Lili, who keeps his first deck -- an obsolete Radio Shack PD-50 -- in solitary splendor behind four locks",
        "archetype": "Decker",
        "title": "Veteran decker, ALOHA",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 3,
        "description": "A spacious, spartan suite behind a Rating 5 voice lock, Rating 4 thumbprint, Rating 6 retinal scan and Rating 7 maglock, all stand-alone. Watches his daughter's final AFD tests with quiet pride.",
        "background": "Raised Lili in the decking trade in Waimea Canyon; groomed her from childhood as a super-decker. Where her mother is, the book does not say.",
        "notes": "B4 Q4 S3 C2 I5 W5 E5.8 R4; TR 4/4; datajack; Athletics 5, Computer 7, Computer Theory 8, Etiquette (Matrix) 5, Firearms 4, Unarmed 4; Fichetti Security 500; passcards. Interrogated: knows the AFD is in the Special Research Area and that Naheka keeps back-ups and spare prototypes 'somewhere'.",
        "contact_skills": ["Matrix operations and datasteals across the Hawai'ian RTG"],
    },
    {
        "name": "Lili Kalakaua",
        "role": "Eighteen-year-old prodigy decker raised in Waimea Canyon as ALOHA's super-decker; testing the AFD on a Fuchi Cyber-7 and the only person who knows where the 'Honeydew' back-up is",
        "archetype": "Decker (prodigy)",
        "title": "Decker, ALOHA; AFD test pilot",
        "race": "Human",
        "gender": "Female",
        "nationality": "Kingdom of Hawai'i",
        "age": 18,
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 3,
        "description": "Jacked into a brand-new Fuchi Cyber-7 with the AFD attached while her father, Wong and Chan look on. Elegant quarters with the same four-lock security as John's. Often visits Naheka's suite to use the trid screens and simsense goggles he installed mostly for her.",
        "background": "A child prodigy who has spent virtually her whole life in the canyon being groomed for this. Naheka's fondness for her is the closest thing to warmth the serpent shows.",
        "notes": (
            "B3 Q5 S4 C5 I6 W6 E5.8 R5; Matrix Init 9+3D6; TR 5/4; datajack; Climbing 5, Computer 8, "
            "Computer Theory 8, Etiquette (Matrix) 5, Firearms 5, Unarmed 5; Fichetti Security 500; Fuchi "
            "Cyber-7 (MPCP 10, Hardening 4, 200/2,000; Bod 7, Evasion 8, Masking 8, Sensors 7; Armor 4, "
            "Attack 7, Browse 6, Deception 4, Mirrors 5, Restore 5, Sleaze 5, Slow 6; Response Increase 2, "
            "AFD). Persuaded or forced, she names the chip carrier 'Honeydew' in Naheka's lair. Top of the "
            "interrogation ladder. A superb future asset or enemy for any decker."
        ),
        "contact_skills": ["AFD design and testing", "ALOHA's research subsystem"],
    },
    {
        "name": "Cassidy Kane",
        "role": "ALOHA's most experienced mage, lecturing four apprentices on conjuring in the padded practice area when the runners arrive",
        "archetype": "Hermetic Mage",
        "title": "Senior mage and instructor, ALOHA",
        "race": "Human",
        "gender": "Female",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 3,
        "description": "Teaching the finer points of conjuring among gym mats, holographic displays and trid screens; carries a Rating 2 power focus and a passcard to her own room.",
        "notes": "B3 Q3 S3 C3 I6 W4 E3 M3(5) R4; TR 5/3; Climbing 3, Conjuring 6, Magical Theory 6, Negotiation 4, Sorcery 6; Power Focus 2. Spells: Acid Stream 6, Analyze Magic 5, Chaos 5, Cure Disease 6, Flamethrower 5, Heal 6, Increase Reflexes +1, Mana Barrier 6, Mana Bolt 4, Mask 6, Mind Probe 3, Power Dart 6, Stunball 5. Senior-mage interrogation tier: knows Naheka is a feathered serpent. Her Essence 3 and Magic 3(5) go unexplained.",
    },
    {
        "name": "Walker",
        "role": "Senior ALOHA mage researching in the hermetic library",
        "archetype": "Hermetic Mage",
        "title": "Senior mage, ALOHA",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 2,
        "description": "One of three seniors among the printed books, chip readers and CD-ROMs of a library that doubles as Conjuring 6 and Magical Theory 6 references. Comfortable quarters behind a Rating 6 maglock.",
        "notes": "Senior Mage block: B3 Q4 S3 C4 I6 W5 E6 M6 R5; TR 4/3; Climbing 4, Conjuring 5, Magical Theory 6, Negotiation 4, Sorcery 6; same spell list as Cassidy Kane. Knows Naheka's true nature.",
    },
    {
        "name": "Apapane",
        "role": "Senior ALOHA mage researching in the hermetic library; named for a Hawai'ian honeycreeper",
        "archetype": "Hermetic Mage",
        "title": "Senior mage, ALOHA",
        "race": "Human",
        "gender": "Female",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 2,
        "description": "A militant who took a traditional name, as the young kama'aina do. In the library with Walker and Akialoa.",
        "notes": "Senior Mage block (Sorcery 6, Conjuring 5; Acid Stream 6, Flamethrower 5, Heal 6, Mana Barrier 6, Mask 6, Power Dart 6, Stunball 5). Knows Naheka is a feathered serpent. Gender is the ingest's guess.",
    },
    {
        "name": "Akialoa",
        "role": "Leader of the ALOHA mages, with a den of two huge trid screens as the perk of rank; named for an extinct Hawai'ian bird",
        "archetype": "Hermetic Mage",
        "title": "Leader of the ALOHA mages",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "ALOHA (Army for the Liberation of Hawai'i)",
        "connection": 3,
        "description": "Enjoys a spacious, cluttered den of entertainment paraphernalia beside the senior quarters; found in the library with Walker and Apapane.",
        "notes": "Senior Mage block (B3 Q4 S3 C4 I6 W5 M6; Sorcery 6). Second only to Naheka in the magical hierarchy; with Naheka gone, the man who would try to hold ALOHA together. Gender is the ingest's guess.",
    },
    {
        "name": "Yoshi Akimoto",
        "role": "Mitsuhama press-liaison officer in Hawai'i who denies that MCT military forces are training in Hawai'ian waters and threatens the Maui Screamer with libel",
        "archetype": "Corporate Spokesman",
        "title": "Press liaison office, Mitsuhama Computer Technologies (Hawai'i)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Mitsuhama Computer Technologies",
        "connection": 2,
        "description": "'A few cargo vessels entering Hawai'ian waters to engage in normal shipping procedures becomes an act of aggression in the minds of foolish people with overactive imaginations.' Declines to say whether MCT will sue.",
        "notes": "Honolulu newscast handout. The 'cargo vessels' are the Swordsman flotilla searching for the AFD off Makai Island. A face for any MCT follow-up in the islands.",
    },
    {
        "name": "King Kamehameha V (Gordon Ho)",
        "role": "Ali'i of the Kingdom of Hawai'i since 2045; Danforth Ho's son, half Hawai'ian, Harvard economist, an excellent judge of people",
        "archetype": "Monarch",
        "title": "Ali'i (King) of the Kingdom of Hawai'i",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "age": 35,
        "organization": "Kingdom of Hawai'i",
        "connection": 6,
        "description": "Born Gordon Ho in 2020, ascended at 25; only half his ancestry is Hawai'ian but the bloodline runs straight to Kamehameha I. Postgraduate degree in economics from Harvard. Enjoys enough popular support that unseating him would cost every legislative incumbent his seat.",
        "notes": "Regards the kahuna Ke-one-poko as friend, mentor and political advisor. Keeps the megacorporate latitude his father promised because it is also the shield against UCAS and Japan. Not encountered; the top of the Kingdom's org chart.",
    },
    {
        "name": "Ke-one-poko",
        "role": "Aging, powerful kahuna, chief advisor to two kings; believed a Nene shaman though he has never named his totem",
        "archetype": "Kahuna (Shaman)",
        "title": "Chief advisor to the Ali'i",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "Kingdom of Hawai'i",
        "connection": 5,
        "description": "'The short sand.' Tradition says the ali'i's chief advisor must be a kahuna; he served Kamehameha IV and now his son as friend and mentor.",
        "notes": "No stats. If ALOHA's three Nene shamans answer to any tradition, it is his; a possible back-channel between the palace and the canyon.",
    },
    {
        "name": "Danforth Ho (King Kamehameha IV)",
        "role": "Maui management consultant found by Na Kama'aina to be Kamehameha I's heir; declared Hawai'ian sovereignty on August 22 2017 and ruled until 2045 (deceased)",
        "archetype": "Monarch (historical)",
        "title": "First Ali'i of the independent Kingdom of Hawai'i, 2017-2045 (deceased)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Kingdom of Hawai'i",
        "organization": "Kingdom of Hawai'i",
        "connection": 1,
        "description": "Twenty-four when Na Kama'aina came for him, owner of a profitable consulting firm, less than a quarter Hawai'ian; a labor-relations man with an instinct for brokering alliances who became a strong, charismatic king 'who did not take kindly to orders from anyone'.",
        "background": "Went underground as 'rightful ruler in exile' in 2015-16, cut corporate deals (Yamatetsu above all, Ares too) and a yakuza deal behind Na Kama'aina's back, and on the day of the Great Ghost Dance unleashed kahunas, Great Form spirits, the yakuza's civilian army and corporate security on the Civil Defense Force. Marched on the capital; ruled well and justly; no evidence of foul play in his death.",
        "notes": "Historical; the Secession Day mysteries (dragons, storms from Punchbowl, something huge at the Arizona Memorial, purged records) are his era's unexplained drek.",
    },
    {
        "name": "Orren Debare",
        "role": "California Free State trade representative visiting Honolulu to expand trade agreements; his last visit ended in scandal with Rachel Hong",
        "archetype": "Diplomat",
        "title": "Trade Representative, California Free State",
        "race": "Human",
        "gender": "Male",
        "nationality": "California Free State",
        "connection": 3,
        "description": "Arrives the day after the runners; the 11:00 news promises an in-depth report on the trade talks -- and a look at Ms. Hong's latest sim.",
        "notes": "Newscast handout. Japan angles to control Hawai'i through its client state CalFree, which makes his talks more than trade.",
    },
    {
        "name": "Rachel Hong",
        "role": "Famous Honolulu restaurateur and star of adult simsense; the 'minor scandal' of Orren Debare's last visit",
        "archetype": "Simsense Star / Restaurateur",
        "title": "Restaurateur and adult-simsense star",
        "race": "Human",
        "gender": "Female",
        "nationality": "Kingdom of Hawai'i",
        "connection": 3,
        "description": "Two careers, one headline. Her latest sim gets airtime beside the CalFree trade talks.",
        "notes": "Newscast handout; her restaurant is never named. A Honolulu contact with a corporate clientele and a diplomat's phone number.",
    },
]

ORG_UPDATES = {
    "Mitsuhama Computer Technologies": {
        "notes_append": (
            "Paradise Lost (February 2055): bought the AFD prototype from Molokai Microtronics for a hefty "
            "fee, then by prearranged plan sent an undercover assault team to massacre the MFI/2M meeting "
            "in 2M's Honolulu boardroom while a second team (led by its own double agent Robbie 'Kinu' "
            "Kurosawa) stripped the Makai Island lab, purged its computer and killed all but one "
            "scientist -- and paid 2M for 'assets expended'. Naheka drowned the boat crews; MCT believed "
            "Kinu's kraken story just long enough to send search boats, then ordered him shot on Makai. "
            "Its search party: a ten-man Mitsuhama Assault Team (B5 Q4(6) S4(6) I4 W4 R4(8), Init 8+3D6; "
            "TR 5/4; muscle replacement 2, wired 1; Ares FN-HAR with laser, gas vent II and thermo scope, "
            "armor jacket), three executioners (wired 1, AK-97s), a combat mage with three tiger-sized "
            "watcher spirits, and four Zemlya-Poltava Swordsman boats (pilot plus four wired crew each). "
            "After the kraken eats a boat or two MCT no longer knows what happened and stays out of the "
            "rest of the run. Press liaison Yoshi Akimoto publicly denies MCT military training in "
            "Hawai'ian waters. Naheka counts 'the powerful and hated Mitsuhama' among those he duped."
        ),
        "leadership_add": [
            {"name": "Yoshi Akimoto", "title": "Press liaison office (Hawai'i)", "notes": "Paradise Lost news handout."},
        ],
        "enemies_add": ["ALOHA (Army for the Liberation of Hawai'i)", "Mary Falls, Inc. (MFI)"],
    },
    "Fuchi Industrial Electronics": {
        "notes_append": (
            "Paradise Lost: if the runners fail, Naheka sells the AFD to Fuchi for 10 million nuyen; "
            "Fuchi floods the market with AFDs, builds AFD-defeating black IC in three months (a month "
            "later every corp has reverse-engineered it), makes a second fortune on the countermeasure, "
            "and supplies ALOHA a few dozen units -- deckers who trust their new AFD die. On success the "
            "corps still ship AFD-killing ice, but it takes four months. Seattle Datafax: Fuchi's new "
            "PCD3500 non-linear processor, design-team leader Dr. Anne Devren. Fuchi Cyber-4/6/7 decks "
            "and the P100 tabletop are everywhere in the book."
        ),
    },
    "Lone Star Security": {
        "notes_append": (
            "Paradise Lost: La Maison d'Indochine in Bellevue calls the Star when its MAD stairs or its "
            "PANICBUTTONs trip -- a six-trooper patrol in five minutes (B4 Q4 S4 C2 I3 W3 E6 R3; TR 3/3; "
            "Police Procedures 4; Ares Predator, armor jacket 5/3, sap); stunned troublemakers are handed "
            "over and jailed for two months. Honolulu's HNPF is a national force, not a contractor, and "
            "'fights smarter and harder than the average Lone Star cop'."
        ),
    },
    "Hard Corps Security Inc.": {
        "notes_append": (
            "Paradise Lost: holds La Maison d'Indochine's astral-protection contract in Bellevue -- a "
            "Force 4 watcher spirit patrols the restaurant and reports to Hard Corps headquarters; the "
            "response is an astrally projecting mage (B? Q5 S4 C4 I5 W4 E6 R10 astral; TR 4/3; Sorcery 6, "
            "Conjuring 5; Rating 2 katana weapon focus, spell defense, casts nothing) with two Force 4 air "
            "elementals (Engulf, Noxious Breath, Psychokinesis) that never manifest. 'Grade-A astral "
            "security.'"
        ),
        "allies_add": ["Mary Falls, Inc. (MFI)"],
    },
    "Yamatetsu Corporation": {
        "notes_append": (
            "Paradise Lost (Kingdom of Hawai'i sourcebook): Danforth Ho's strongest corporate connection "
            "in the secession years, 'connections which still exist today'; Yamatetsu led the contingent "
            "of majors that pressured Washington into recognizing Hawai'i in 2017. The Kingdom repaid the "
            "corps with more latitude than they enjoy almost anywhere else in the world."
        ),
        "allies_add": ["Kingdom of Hawai'i"],
    },
    "Ares Macrotechnology": {
        "notes_append": (
            "Paradise Lost (Kingdom of Hawai'i sourcebook, Shadowland rumor): in August 2017 Ares had just "
            "taken over the Freedom space station (later Zurich-Orbital) and was the only party with "
            "assets in orbit when a salvo of Project Thor 'smart crowbars' hit the ocean a couple of "
            "hundred meters off the flagship of the U.S. task force steaming back to Hawai'i -- it "
            "turned for San Diego. Danforth Ho had 'held a few serious meetings' with Ares."
        ),
        "allies_add": ["Kingdom of Hawai'i"],
    },
    "Tir Tairngire": {
        "notes_append": (
            "Paradise Lost: Serena Day, a Haoles Don't Surf elf marked for death in Honolulu, plans to "
            "buy a 2,500-nuyen suborbital to Seattle and 'find shelter in Tir Tairngire'. Hawai'i's "
            "knee-jerk prejudice runs against elves rather than orks and trolls."
        ),
    },
    "Renraku Computer Systems": {
        "notes_append": (
            "Paradise Lost: the Seattle Datafax news handouts are 'A Service of Renraku Computer Systems, "
            "Custom Edition' (February 2055): Aztlan civil war, Senator Dennelly's black-magic inquiry, "
            "Universal Brotherhood attacks, Project Hope in the Barrens, Fuchi's PCD3500, the Nashville "
            "snake, the Ork Rights Committee shooting, and MFI's new electronics division or layoffs."
        ),
    },
    "Universal Brotherhood": {
        "notes_append": (
            "Paradise Lost (Seattle Datafax, February 2055): 'Terrorist attacks against Universal "
            "Brotherhood chapter houses continue in North America. Authorities cannot pinpoint the source "
            "of this aggression and seem unable to prevent further attacks.'"
        ),
    },
    "Alamos 20,000": {
        "notes_append": (
            "Paradise Lost (Seattle Datafax, February 2055): blamed for masked gunmen shooting up the Ork "
            "Rights Committee's storefront distribution point in the Redmond Barrens -- six dead, one a "
            "four-year-old boy; the believed target was the rising ork-activist leader Preacher (John "
            "Picarille)."
        ),
        "enemies_add": ["Ork Rights Committee"],
    },
    "Aztlan": {
        "notes_append": (
            "Paradise Lost (Seattle Datafax, February 2055): 'Aztlan civil war heats up. Seventy dead in "
            "fighting near Culiacan as a result of government weather magic creating a flash flood "
            "through rebel positions.'"
        ),
    },
    "UCAS Federal Bureau of Investigation": {
        "notes_append": (
            "Paradise Lost (Seattle Datafax, February 2055): investigating UCAS Senator Moe Dennelly, who "
            "denies participation in black-magic rituals involving the deaths of four Kansas teenagers."
        ),
    },
    "DocWagon": {
        "notes_append": (
            "Paradise Lost: Mary Falls carries a Super-Platinum contract, her security chief Bounder a "
            "Platinum one. No word on DocWagon coverage in the Kingdom of Hawai'i; MFI's traveler's "
            "insurance patches up the team there."
        ),
    },
}

LOC_UPDATES = {
    "The Barrens (Seattle)": {
        "notes_append": (
            "Paradise Lost (Seattle Datafax, February 2055): 'Project Hope brings new life to Seattle's "
            "Barrens' -- manager Jonathon Tung interviewed; and the Ork Rights Committee's Redmond "
            "storefront shooting (six dead, Alamos 20,000 blamed). Honolulu, by contrast, has 'nothing "
            "that even comes close to the squalor of the Redmond Barrens or Hell's Kitchen'."
        ),
    },
}

NPC_UPDATES = {}

TAG_EXISTING = {}

MATRIX_HOSTS = """
All Hawai'ian systems sit on the PA/HI regional grid; a decker who is not on the premises crosses a
Green-4 SAN to reach the LTG and must find the LTG number by the standard rules. No data on the AFD
exists anywhere in the Matrix.

**1. 2M Main System** (map p.60-61) -- Molokai Microtronics' Honolulu head office, Matrix-connected.
Virani (Fuchi Cyber-6, all passcodes) is jacked in the night of the break-in and avoids combat. The
retinal scanner on Derek Hanna's central terminal can only be shut off from inside, via its I/O port.

| Node | Function | Rating / IC |
|---|---|---|
| SAN | Matrix access | Orange-4, Access 4, Trace and Report 4 |
| CPU | Central processor | Red-5, Trace and Report 6, Black-5 |
| SPU-1 | Accounting subprocessor | Orange-5, Access 6, Trace and Dump 5 |
| I/OP-1 | President's terminal | Orange-5, Access 6, Blaster 6 |
| I/OP-34 | VP Accounting's terminal (Hanna; central computer, retinal scanner) | Red-4, Access 6, Trace and Burn 5 |
| DS-1 | Financial records | Red-5, Access 6, Barrier 7, Trace and Burn 4 |
| DS-2 | Monetary accounts | Red-6, Access 7, Black-5 |
| DS-11 | President's diary | Orange-6, Access 5, Barrier 5, Trace and Report 5 |
| SPU-2 | Client accounts subprocessor | Orange-5, Access 6, Trace and Dump 5 |
| I/OP-22 to 24 | Account supervisors' terminals | Orange-5, Access 6, Killer 5 |
| I/OP-25 | VP Accounts Management's terminal (Virani) | Orange-6, Access 6, Trace and Burn 5 |
| DS-3 to 5 | Account data, mainly client correspondence | Orange-4, Access 5, Trace and Report 5 |
| SPU-3 | Marketing subprocessor | Orange-4, Access 5, Trace and Report 5 |
| I/OP-32 | VP Marketing's terminal (Savage) | Green-5, Access 4, Trace and Dump 4 |
| I/OP-33 | Boardroom terminal | Green-5, Access 5 |
| DS-9 and 10 | Marketing lists and proposals | Orange-5, Access 5, Barrier 5, Trace and Report 5 |
| SM | Boardroom display screens | Orange-4 |
| SPU-4 | Personnel subprocessor | Orange-5, Access 5, Trace and Dump 5 |
| I/OP-31 | VP Personnel's terminal (Chao) | Orange-6, Access 6, Trace and Burn 5 |
| DS-7 | Office personnel records | Orange-5, Access 5, Barrier 5 |
| DS-8 | Lab personnel and mosquito couriers | Red-5, Access 5, Barrier 6, Trace and Burn 5 |
| SPU-5 | Correspondence subprocessor | Green-5, Access 5 |
| I/OP-26 to 29 | Secretaries' terminals | Green-5, Access 5 |
| I/OP-30 | Reception terminal | Green-5, Access 5 |
| DS-6 | Correspondence | Orange-4, Barrier 4 |
| SPU-6 | Account managers' subprocessor | (no rating given) |
| I/OP-2 to 21 | Junior account managers' terminals | Orange-4, Access 6 |

**2. 2M Research Lab Subsystem** (map p.26-27) -- stand-alone, reachable only from the two terminals in
the Research Room (14). The runners' Evaluate 5 works only on AFD data. Most of the room's physical
security is already down, disabled by Koyashi.

| Node | Function | Rating / IC |
|---|---|---|
| CPU | Research CPU | Red-4 |
| SPU-1 | Manages datastores 1-3 | Orange-4, Access 4 |
| DS-1 | All research accounts, each account's manager and lab code | Red-5, Access 6, Black-5, Scramble 4 |
| DS-2 | Locations and descriptions of every lab -- the AFD lab on Makai Island off Molokai, with map coordinates (cannot reveal that MCT purged it) | Red-6, Access 6, Barrier 6, Black-5 |
| DS-3 | Mosquito couriers' contacts | Red-5, Access 6, Barrier 4, Black-4 |
| I/OP-1 and 2 | Research Room terminals | Green-6, Access 5, Blaster 5 |
| SPU-2 | Manages datastores 4-23 | Orange-4, Access 4 |
| DS-4 to 23 | One per account manager / supervisor: project descriptions and lab correspondence | Red-4, Access 6, Blaster 5, Scramble 5 |

**3. Honolulu Offices Inc. building system, 31st-floor subsystem** (map p.23) -- the landlord's
off-Matrix security CPU in its fifth-floor office; also lights, sprinklers and air conditioning. A guard
is jacked in at all times and can place a tampering decker's floor; ten-plus guards in ten minutes.
2M's own subsystems (laser grids, keypads, pressure sensors, the retinal scanner) report to it but are
not controlled by it.

| Node | Function | Rating / IC |
|---|---|---|
| CPU | Building central processor | Red-5, Barrier 6, Trace and Burn 6 |
| SPU-31 | 31st-floor subprocessor | Orange-5, Access 6, Barrier 5, Killer 4 |
| SM-1 | All maglocks, cardreaders and print scanners on 31 | Orange-4, Access 4, Barrier 4, Blaster 4 |
| SM-2 | Lights, 31st floor | Green-3, Access 4, Barrier 4 |
| SM-3 | Heat / air conditioning, 31st floor | Green-3, Access 4, Barrier 4 |
| SM-4 | Smoke detectors, 31st floor | Green-3, Access 4, Barrier 4 |

**4. ALOHA Main System** (map p.61) -- Waimea Canyon, Matrix-connected through two SANs. Flash is
jacked in watching cameras; Jan and Kira are out on the airport's systems. Three Fuchi Cyber-6 decks
in the Computer Room.

| Node | Function | Rating / IC |
|---|---|---|
| SAN-1 | Normal correspondence | Green-5, Access 5 |
| SAN-2 | Financial correspondence | Orange-6, Access 6, Trace and Burn 6 |
| CPU | Central processor | Red-5, Access 7, Black-4 |
| SPU-1 | Correspondence subprocessor | Orange-5, Access 6, Killer 5 |
| DS-1 | Correspondence files | Orange-5, Barrier 5 |
| SPU-2 | Security and building maintenance | Red-4, Access 7, Trace and Burn 6 |
| I/OP-1 to 3 | Computer Room terminals | Orange-5, Access 6, Blaster 5 |
| SM-1 | Security cameras (research area, chem lab, magic practice area, conference room) | Red-4, Barrier 6, Trace and Report 5 |
| SM-2 | Security maglocks and attached devices | Red-5, Access 7, Black-4 |
| SM-3 | Lights | Orange-5, Barrier 5 |
| SM-4 | Heat / air conditioning | Orange-5, Barrier 5 |
| SPU-3 | Accounting and finance | Orange-5, Access 6 |
| I/OP-4 | Accountant's terminal (Toyoda) | Orange-4, Access 5 |
| DS-2 | Bookkeeping and financial records | Orange-5, Barrier 5, Scramble 5 |
| DS-3 | Cash accounts | Red-5, Access 7, Black-5 |
| SPU-4 | Personnel and miscellaneous | Orange-5, Access 6, Trace and Report 6 |
| I/OP-5 | Conference room terminal | Orange-5 |
| I/OP-6 | Special research terminal (main-system side) | Orange-5 |
| DS-4 | Contacts and personnel information -- the field-agent list | Red-5, Access 7, Barrier 7, Black-5 |
| SM-5 | Conference room display screens | Orange-5 |

Not mapped: the Kalakauas' four stand-alone door locks, Audrey Wilkes' inventory computer, the chem
lab's analysis computer, and the senior mages' tabletop computers.

**5. ALOHA Research Subsystem** (map p.47) -- autonomous; reachable only from the Special Research Area
or Naheka's suite. Complete AFD details.

| Node | Function | Rating / IC |
|---|---|---|
| CPU | Research CPU | Red-5, Access 6, Barrier 6 |
| I/OP-1 | Research terminal | Orange-4, Access 5, Barrier 5, Blaster 5 |
| DS-1 | AFD design specifications | Red-5, Access 6, Black-6 |
| DS-2 | Results of the ongoing AFD evaluation | Red-5, Access 6, Black-6 |

**6. Naheka's personal computer and the back-up chip** (p.48) -- a stand-alone terminal in the lair suite
beside two AFD prototypes; the back-up optical chip (carrier "Honeydew", among shelves of trid chips)
must be uploaded to it to separate the AFD data from the other project back-ups, faking or bypassing
every passcode; the AFD data is protected by the equivalent of Red-5, Access 6, Scramble 7. Cameron's
"Insurance" chip (Rating 6 scramble equivalent) is read by slotting it into any cyberdeck. Neither is a
host.

**7. La Maison d'Indochine security computer** -- no map; controls the booth trap doors and takes the
PANICBUTTON alarms from the two monitoring rooms.
"""

NOT_BUILT = """
- **Ryumyo**, the Great Dragon whose vassal Naheka is (name-drop only; would replace him with another
  vassal); **Pele**, goddess of the luau's hula; **Queen Liliuokalani**, **Sanford B. Dole**, **Father
  Damien**, **Kamehameha I and III**, **Captain Cook** -- sourcebook history.
- **The La Maison maitre d'** (Computer 3, Etiquette (Corporate) 5, Japanese 4, datajack; stats on the
  location row), her **waiters, busboys, chef and cooks**, the **twelve security guards**, the **elven
  string quartet**, the **six Lone Star cops** and the **Hard Corps astral mage, watcher and air
  elementals** -- on the La Maison, Lone Star and Hard Corps rows. **MFI's four troll and four ork
  guards**, the **MFI corporate guard** who hired Egmond, **Pavel and Eileen Griczuk** (Bounder's
  parents).
- **The Polson chauffeur** (snoring dwarf, Toyota Elite) and the **Hilton bell captain**; **Kintaro's
  Lounge**, the **Dole Pineapple Plant**, the **National Museum**, **Macadamia Studios** (trideo
  filming) -- the tourist itinerary; the **Outrigger Ala Moana** and **Royal Hawai'ian** hotels; the
  **Hilton marina and roof heliport**; **Seattle-Tacoma International Airport** (limo ride only; a row
  is being created by the Ivy and Chrome ingest).
- **Honolulu Offices' fifth-floor guard and ten security guards**, **the three MCT executioners,
  ten-man assault team, combat mage, three tiger watchers, four Swordsman pilots and sixteen crew**,
  **the kraken** -- on the Makai Island and Mitsuhama rows. **2M's Hong Kong office**, **2M's mosquito
  couriers**, **the surviving 2M scientist** Naheka ate, **Dackson's daughter** (Savage's wife).
- **ALOHA's two unnamed hit-squad gunners**, **three Nene shamans**, **six ork guards**, **four
  physical adepts**, **four apprentice mages**, **three chemists**, **four cooks**, **cleaning crew**,
  **Merill Toyoda's Awakened cat**, **the Force 4 earth elemental** and **two watcher spirits** -- on
  the ALOHA and headquarters rows. **Blitzkrieg**, the European synthrock group ALOHA plans to kidnap.
- **Aloha Air**, **Moku'aina Air**, **Lio Lawe Ukana Air Transport**, **The Bus** and the **AutoGuide**
  grid, the **Maui Screamer** datafax, **California Free State**, **Na Kiu** (folded into the armed
  forces), the **Civil Defense Force** (2014-2017), the **Ho family**, **Waimea Canyon**, **Mount
  Waialeale**, **Mauna Kea**, the outer-island airports (**Hanamaulu**, **Hoolehua**, **Lanai City**,
  **Kahului**, **Mahana**, **Hana**, **Hilo**, **Ke-Ahole**, **Kamuela**), **Dillingham AFB**, **Kaneohe
  Bay MCAS**, **Schofield Barracks**, **Pearl City**, **Waipahu**, **Ewa Beach**, the **Ko'olau range**,
  **Kapiolani Park**.
- Shadowland posters on the Kingdom of Hawai'i upload (December 2054): **Holly**, **Nene**, **Woppler
  the Weatherman**, **Lace**, **Magnum** (and his red Ferrari 308 Mondiale), **Bomba**, **Blaze**,
  **Sydney**, **Ringer**, **McHugh**, **Nit**, **Auntie Social**, **Grace**, **Trashcan Man**,
  **Lucinda**.
- News-handout names: **Jonathon Tung** (Project Hope manager), **Dr. Anne Devren** (Fuchi PCD3500
  design lead), **Senator Moe Dennelly**, the **200-foot Nashville snake**, the **Kansas teenagers**.
- Rules reprints (weapon detectors, chem-sniffer table, keypad tampering, Success Tables) and the four
  new totems (**Honu**, **Kohola**, **Mo'o**, **Nene**) -- see the Kingdom row's notes for the totem
  list.
"""

PLAY_NOTES = """
- Tone: warm sun, beautiful people and breathtaking scenery slammed against the brutality of 2M,
  Mitsuhama and ALOHA; Naheka is the motif -- beauty over a cold heart that spends people like cred.
  Getting sidetracked can get a runner killed; the team has about seven days in Hawai'i before Naheka
  sells to Fuchi.
- The team travels light: everything usual stays in Seattle, airport arrivals are unscreened, Daniel
  supplies up to 10,000 nuyen of SRII gear per runner (four requests easy, +1 Availability after) and a
  loaned Fuchi Cyber-4. Five to eight runners, at least one skilled decker, ideally a topnotch rigger
  (the Otter chase, the canyon landing), and a mage with illusion and manipulation spells.
- Decision tree: luau (Serena) -> 2M offices (Koyashi, the research subsystem) -> Makai Island (Kinu,
  the kraken) -> Waimea Canyon. ALOHA's Revenge (Toshi and Cameron's chip) is the last-resort clue
  drop if the team never learns where the canyon HQ is; without chip or Kinu they are fired after a
  week.
- Run the big fights like an action movie: only a few of the bad guys get a clean shot at any one
  time; Makai Island is a fight the runners must not win -- Kinu says retreat, the kraken saves them.
  Adjust Threat Ratings, but not so far that the story stops being credible.
- Interrogation in the caves is an opposed Interrogation (Willpower) test against the Knowledge
  Category Table; only Lili knows "Honeydew". Deckers reach the AFD data only from the Special Research
  Area or Naheka's suite.
- Enter the Dragon: fighting Naheka is death, running is nearly death (three Athletics (6) / Quickness
  (8) tests, then Strength (6) or Athletics (4) with 2 successes to board the Airstar), negotiating is
  the intended ending -- 50 percent of net sales to ALOHA, silence for their lives. Daniel will not die
  for runners who chose the fight.
- Karma: avoid conflict at La Maison +1; find the HQ +6; the prototype +5; the back-ups +8; a deal
  with Naheka +12; defeat or escape Naheka with the AFD +20; double the standard individual awards for
  guts and smarts.
- Payoff: 10,000 each up front, 50,000 each on completion (haggled 10,000 per net success either way),
  5,000 certified per alias, leftover gear kept, five AFDs for the decker weeks later; Serena's intel
  costs 2,500, Kinu's guidance 200,000 (or he pays 20,000 for a boat ride). Cameron's "Blitzkrieg"
  file is major paydata.
- Loose ends: Naheka's vengeance if robbed; Kinu with nowhere to go; Alan Jenkins' ruined name; Ahmed
  Virani's revenge fantasies; MCT's unanswered questions; an AFD market that dies in three or four
  months; ALOHA's kidnapping plan for Blitzkrieg; MFI and ALOHA as joint-venture partners who will
  kill anyone who talks.
"""
