# Predator and Prey (FASA 7324, 1998) -- an anthology of three unconnected adventures sharing only a
# theme (metahumanity against Awakened predators) and a year: the book's own Introduction states
# "The year is 2059." Campaign order per frontend/shared.js ADVENTURE_ORDER: the array lists
# 'Predator and Prey' at index 27 (0-based) / position 28 (1-based, matching every other spec's
# ORDER = index+1 convention). The brief for this spec said ORDER = 29; that number does not match
# the array (verified by script: Silver Angel=1 ... Missing Blood=25, Super Tuesday!=26, Shadows of
# the Underworld=27, Predator and Prey=28, Missions=29). Using ORDER = 28 here to match the established
# convention and the actual frontend sort position; flagged for the user rather than silently
# following the (apparently mistaken) instruction.
#
# Three adventures, three authors: FORBIDDEN FRUIT (Brian Schoner, pp. 7-27, Amazonia), WILD KINGDOM
# (Jennifer Brandes & Chris Hepler, pp. 29-51, Caribbean/West Africa) and BASER INSTINCTS (Bill Aguiar,
# pp. 52-75, Seattle). Pages 76-97 are the Gamemastering Critters / Critter Powers reference chapters
# (pure crunch -- stat blocks and power definitions for creatures used across all three stories); not
# built as org/location/NPC rows, noted in NOT_BUILT and referenced from the affected rows instead.
#
# Book's own inconsistencies, noted here and on the affected rows: the Wild Kingdom legwork table
# calls the Seattle paranimal supplier "MCT-Parashield" (implying Mitsuhama ownership) while Baser
# Instincts calls it a "small local corp" with no parent named -- ownership is never reconciled.
# Ahmadou Kourouma's wife is named "Massan" in his Cast of Shadows entry (mentioned only in his NPC
# background below, not built as her own row); earlier in the same adventure "Massan" is also the name
# of Gavivi Aidoo's eight-year-old bodyguard, who IS built as his own row -- almost certainly an
# editing accident, not the same person. The Fort Lewis
# database's Host B security-sheaf table has its trigger-step column and event column printed as
# separate lists in the scan (a two-column OCR merge); MATRIX_HOSTS below reconstructs the pairing
# from the step/event counts, which lines up cleanly, but treat it as a best-effort reconstruction.
#
# Source text: docs/Adventures/text/Shadowrun 2e - Adventure - Predator and Prey {FASA7324}.txt
# (10,399 OCR lines / 98 scanned pages). ASCII only (pre-commit hook).

ADVENTURE = "Predator and Prey"
ORDER = 28
SOURCE = "Shadowrun 2e - Adventure - Predator and Prey {FASA7324}.pdf, pp. 4-97"
YEAR = "2059"

SYNOPSIS = """
**Predator and Prey** collects three stand-alone runs, each pitting a team against creatures of the
Awakened world rather than the usual corps and gangers -- the gamemaster can drop any of them into an
existing campaign without touching continuity.

**Forbidden Fruit** sends the runners into Amazonia. **Randall Pape** of the small, ethically-strapped
**Green Globe International** hires them to smuggle three GGI botanists -- elf ecologist **Dr. Eiji
Fukuhara**, human ethnobotanist **Dr. Carl Sanders** and hobgoblin phytogeographer **Dr. Mohammed
Al-Mansour** -- across the closed Amazonian border to harvest the rare Brazilian kiwi, GGI's entry in
the race for one of Dunkelzahn's bequests. Peruvian guide **Roberto "Bicho" Xavier** gets them past the
border post at **Leticia** and into rainforest thick with basilisks, a naga and an Awakened caiman.
Once the fruit is found, the trip curdles into horror: a larval Awakened insect that hatches inside the
kiwis burrows into Sanders and then kills Fukuhara outright, and the survivors barely make it home
before a hold full of spider-beasts breaks loose over the Skytruck at altitude.

**Wild Kingdom** is a long escort run with a hidden cargo. **Phoenix Biotechnologies** hires the team,
through disguised handler **Rachel Liseli**, to guard the **PCS Tangakwunu** on its three-week run from
Miami to the free city of **Sekondi** on Africa's Gold Coast. The "valuable cargo" is really **Dr.
Albert Dicristofaro**, a neurologist extracted from rival JHIH Corporation and now an unwilling slave
bound for PBT's African research arm. Ewe pirates of the **Aidoo Clan**, hired by competitor **Tan Tien
Incorporated**, use trained mami wata to cover a hull breach and snatch Dicristofaro mid-voyage. PBT
contact **Ahmadou Kourouma** sends the runners after him: legwork through Accra and the pirate
shantytown of **Glidji** leads to a heavily-guarded Tan Tien research compound up the Volta River, and
then a jungle chase and a runaway locomotive back to Sekondi, with Dicristofaro's fate -- freedom or a
life of corporate slavery -- left to the runners to decide.

**Baser Instincts** brings the horror home to Seattle. A wave of paranormal-animal attacks has Lone
Star's Paranormal Animal Control Division overwhelmed and Knight Errant circling for the law-enforcement
contract; a fixer secretly working for the Star hires the runners, off the books, to recover an incubus
from the sewers and run down a paranimal dog pack terrorizing the Redmond Barrens. Both leads trace back
to **Parashield, Inc.**, a local watch-animal supplier, and from there to **Reginald Disball**, an animal
handler at the **Fort Lewis Zoological Gardens** who has spent years unknowingly hosting a possessing
astral entity. The trail ends in a running battle through **Woodland Park Zoo** as Disball, no longer in
control of himself, tries to stampede the zoo's elephants and behemoths through the city before the
entity abandons his body and vanishes back to the metaplanes -- leaving "It will hunt again" as its only
clue, and Disball's shattered mind as the only evidence anyone will believe.
"""

TIMELINE = """
- **Forbidden Fruit** (must follow Dunkelzahn's death and the reading of his will, so 2058 or later;
  the book's blanket "2059" is used here). Randall Pape recruits shadowrunners at the Gravity Bar North
  after Amazonia cancels GGI's legal kiwi expedition. A 48-hour prep window, then the Skytruck flight
  to Iquitos, Peru, where guide Bicho swaps the expedition's flashy boat for his own Golfinhao. The
  border crossing at Leticia is delayed a day by a soccer match; a night hike to a kiwi site runs into
  a basilisk, scattering the scientists into a wyrd mantis pair and a naga. A macareu holes the
  Golfinhao on the way downriver; the team hikes cross-country to a working kiwi grove, where a larva
  infests Dr. Sanders that same night. The next morning a second larva kills Dr. Fukuhara outright;
  Bicho and Dr. Al-Mansour nearly kill each other before the border patrol forces a running fight back
  to Iquitos. On the return flight, the hatched spider-beasts break out of the cargo hold.
- **Wild Kingdom** (roughly one month of game time, same year). Dr. Albert Dicristofaro is extracted
  from JHIH Corporation in Baltimore and delivered to Ms. Cairo in Miami, believing he is bound for a
  Bahamas research post; he is locked in a hold cabin bound for Phoenix Biotechnologies' Sekondi
  operation instead. The runners are hired at the Dillman Theater in Seattle and meet the PCS
  Tangakwunu at Miami's Pier 121. Roughly three weeks into the 22-day Miami-Bermuda-Sekondi crossing
  (with a stop in Bermuda to meet fixer Rain), Ewe pirates of the Aidoo Clan use trained mami wata to
  cover a hull breach and extract Dicristofaro off the coast of West Africa. In Sekondi, contact
  Ahmadou Kourouma sends the runners after him; legwork in Accra and the Aidoo shantytown of Glidji
  leads to a Tan Tien Incorporated research compound up the Volta River near Mampong, from which
  anti-slavery activists have just freed Dicristofaro. A jungle chase (enwontzane monkeys, a spying
  anwuma bavole, three waves of Tan Tien mercenaries and a runaway coal locomotive) ends at the
  Sekondi border, where the runners choose to hand Dicristofaro back to PBT or let him go.
- **Baser Instincts** (three nights of escalating incidents, same year). Night one: Lone Star's PAC
  substation 25 fields a dozen-plus paranormal-animal calls across Seattle, including an incubus
  causing traffic deaths and a Saeder-Krupp facility breakout. Night two: heavier Star patrols hold the
  line to two incidents. Night three: PAC calls nearly double and six officers die in what look like
  deliberate ambushes; Knight Errant publicly offers extermination teams. The runners are hired the
  next morning at Woodland Park Zoo by an unnamed fixer (rumored name "Mike") secretly working for the
  Star, and spend the following days clearing the sewer incubus, surviving a dog-pack ambush in the
  Redmond Barrens, breaking into a Parashield, Inc. facility and cross-referencing Parashield's and
  Fort Lewis Zoological Gardens' animal records to identify handler Reginald Disball -- who, confronted
  at the zoo, reveals he has been an unwitting host to a possessing astral entity that tries to
  stampede the zoo's elephants and behemoths through the city before abandoning his body.
"""

ORGS = [
    {
        "name": "Green Globe International",
        "org_type": "corporation",
        "tier": 1,
        "headquarters": "Seattle, UCAS",
        "summary": "Small, principled botanical research corp chasing a Dunkelzahn bequest with a Brazilian-kiwi cultivation bid",
        "description": (
            "A minor Seattle botanical research firm -- 'a small fish in a pond full of sharks' by its "
            "own partner's admission -- trying to win the 10-million-nuyen bequest offered to the first "
            "party to cultivate the rare Brazilian kiwi (actinidia amazonensis) outside its native "
            "Amazonian range (Portfolio of a Dragon: Dunkelzahn's Secrets, p. 32). GGI had a legal "
            "expedition arranged with the Amazonian government, which reneged at the last minute citing "
            "environmental concerns; GGI suspects the real reason is that Amazonia wants to monopolize "
            "the plant's biomedical potential itself. Rather than write off ten months and half a "
            "million nuyen of preparation, executive Randall Pape quietly arranges a shadow crossing "
            "instead, over the objections of his more scrupulous partner."
        ),
        "leadership": [
            {"name": "Randall Pape", "title": "Executive (expedition sponsor)", "notes": "Ex-Shiawase Envirotech; hires the shadow team and briefs them as 'Mr. Johnson'."},
            {"name": "Edwin Danforth", "title": "Partner", "notes": "Dwarf; objects to the shadow crossing on principle and insists on not knowing the details."},
        ],
        "notes": (
            "Forbidden Fruit. Fields a three-scientist expedition (Fukuhara, Sanders, Al-Mansour) plus "
            "hired runners and Peruvian guide Bicho. Pays 100,000 nuyen for the run (20,000 up front, "
            "negotiable +25%, +10,000 if a rigger pilots the Skytruck); final payment and future work "
            "scale with what the team brings home -- full kiwis and at least one living scientist means "
            "full pay and possible repeat business, no kiwis and no scientists means Pape spreads word "
            "the runners are incompetent or worse. Uses a Hawker-Ridley Skytruck (Handling 5, Speed "
            "135/320, Body 9) for transport, refitted for up to 20 passengers with a rear cargo hatch."
        ),
    },
    {
        "name": "Phoenix Biotechnologies",
        "org_type": "corporation",
        "tier": 3,
        "summary": "Neurological-research corp running a slave-labor pipeline of extracted specialists to its West African research arm",
        "description": (
            "A biotech corporation competing with JHIH Corporation and Tan Tien Incorporated in "
            "neurological research, with a research arm on Africa's Gold Coast at the free city of "
            "Sekondi. PBT's Sekondi contact Ahmadou Kourouma treats acquiring skilled researchers as an "
            "ordinary business practice; the corp routinely extracts specialists under false pretenses "
            "(a promised transfer, a promised lab) and delivers them to Sekondi as forced labor instead. "
            "PBT hired shadowrunners as ship security for one such delivery -- Dr. Albert Dicristofaro, "
            "extracted from JHIH -- specifically because the crew needed to be unaware that the 'cargo' "
            "was a person."
        ),
        "leadership": [
            {"name": "Rachel Liseli", "title": "Resources adjustment developer", "notes": "Hires the runners in Seattle under a disguised appearance and the cover name 'Raether'."},
            {"name": "Ahmadou Kourouma", "title": "Sekondi contact", "notes": "Runs the drop-off, the retrieval contract and the runners' pay in PBT stock."},
        ],
        "notes": (
            "Wild Kingdom. Owns/operates the PCS Tangakwunu (Pueblo Corporate Ship, Merchantman-class); "
            "pays in PBT stock (21.3 nuyen/share at hiring, rising to 28.8 within 1D6+2 months if "
            "Dicristofaro is returned). Kourouma becomes a Rating 4 Enemy in Sekondi (Rating 2 in North "
            "America) if the runners free Dicristofaro instead of returning him. Enemies: JHIH "
            "Corporation, Tan Tien Incorporated."
        ),
        "enemies": ["JHIH Corporation", "Tan Tien Incorporated"],
    },
    {
        "name": "JHIH Corporation",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Baltimore, UCAS",
        "summary": "Baltimore neurological-research corp whose star researcher was extracted (unwillingly, as it turned out) by rival Phoenix Biotechnologies",
        "description": (
            "A Baltimore-based competitor to Phoenix Biotechnologies in comparative neurology. Employed "
            "Dr. Albert Dicristofaro on brain-structure research (human, metahuman and animal sensory "
            "processing) until a PBT recruiter talked him into an extraction he came to regret. JHIH "
            "never appears directly in Wild Kingdom beyond this backstory."
        ),
        "notes": "Wild Kingdom (backstory only). Enemy of Phoenix Biotechnologies over the Dicristofaro extraction.",
        "enemies": ["Phoenix Biotechnologies"],
    },
    {
        "name": "Tan Tien Incorporated",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Beijing (home office); Gold Coast division near Mampong, Asante Nation",
        "summary": "Chinese cybernetics/neurology corp developing an animal-Matrix interface, running a heavily-defended paranimal-security compound on the Volta River",
        "description": (
            "A rival to Phoenix Biotechnologies and JHIH in brain-computer interface research, working "
            "toward a working interface between a semi-intelligent creature (dolphin, satyr) and the "
            "Matrix -- a project that would also net a Draco Foundation award. On learning through "
            "corporate spies that PBT was shipping Dr. Dicristofaro to Africa, Tan Tien hired Ewe "
            "pirates of the Aidoo Clan to snatch him during the crossing. The corp employs no magicians "
            "(company policy) and relies instead on camera- and sonic-implanted paranimals -- ekyelebenle "
            "spitting mambas, gomatia chameleons, asonwu pack-monkeys -- controlled by a security rigger "
            "at its Volta River compound near Mampong."
        ),
        "notes": (
            "Wild Kingdom. Compound layout, guard and mercenary stats, and the Tan Tien Research "
            "Computer host are detailed under the Tan Tien Compound location and MATRIX_HOSTS. Holds a "
            "grudge against the runners regardless of outcome but has little reach in North America "
            "(operations limited to Africa and Asia)."
        ),
        "enemies": ["Phoenix Biotechnologies"],
    },
    {
        "name": "Aidoo Clan",
        "org_type": "pirate gang",
        "tier": 1,
        "headquarters": "Glidji (shantytown, east of Accra, Asante Nation)",
        "summary": "Poor Ewe pirate clan, led by patriarch Gavivi Aidoo, hired by Tan Tien to snatch Dicristofaro using trained mami wata",
        "description": (
            "A kin-network of Ewe pirates working the waters south of Accra, patriarch Gavivi Aidoo at "
            "its head with four wives and several children. The Aidoo train mami wata (Awakened, "
            "alcohol-dependent sea lions/mermaids) to fight with spearguns and to board ships, and used "
            "twenty-five of them to cover a Tan Tien-hired dive team cutting into the PCS Tangakwunu's "
            "hull to extract Dr. Dicristofaro. Tan Tien lent the clan a mini-submarine for the job. Poor "
            "even by Glidji standards, Gavivi trades information for cash, food, medicine or work "
            "without much hesitation -- African runners expect their secrets sold after a job, unlike "
            "Seattle's shadows."
        ),
        "notes": (
            "Wild Kingdom. Gavivi's eight-year-old son Ayete and fellow eight-year-old bodyguard Massan "
            "(same name as Ahmadou Kourouma's wife elsewhere in the adventure -- see header note) flank "
            "him at meetings; his thirteen-year-old daughter Acossiova can be intercepted leaving Glidji "
            "for Accra. All three are built as short NPC rows."
        ),
        "enemies": ["Phoenix Biotechnologies"],
    },
    {
        "name": "Parashield, Inc.",
        "org_type": "corporation",
        "tier": 2,
        "headquarters": "Seattle, UCAS (office/warehouse park owned by Ares Macrotechnology)",
        "summary": "Regional paranormal watch-animal supplier whose stock unknowingly seeded Reginald Disball's Seattle attack spree",
        "description": (
            "A local corp specializing in the sale, training and care of paranormal watch animals, "
            "supplying mid-sized firms and even a few megacorps around Seattle. Every animal behind the "
            "book's wave of attacks -- the afanc in the sewers, the tattooed dogs in the Redmond "
            "Barrens -- traces back to a Parashield purchase from the Fort Lewis Zoological Gardens' "
            "breeding program, and from there to trainer Reginald Disball. Parashield's Seattle database "
            "was cut off from the Matrix (one-way SANs only) after a rogue-decker breach some months "
            "back. The Wild Kingdom legwork table names a 'MCT-Parashield' doing biotech work in West "
            "Africa; Baser Instincts calls Parashield an independent local corp with no parent named -- "
            "the book never reconciles whether these are the same company (see header note)."
        ),
        "notes": (
            "Baser Instincts. Sales/service center detailed under its own location row, including hell "
            "hounds, a barghest and two talis cats bred for enhanced powers, and the Parashield Database "
            "host (see MATRIX_HOSTS). Gets a wave of investment interest after the Disball incident from "
            "corps wanting to replicate his apparent animal-control abilities, without knowing an astral "
            "entity was the real cause."
        ),
    },
    {
        "name": "Asante Nation",
        "org_type": "nation-state",
        "tier": 5,
        "headquarters": "Kumasi",
        "summary": "West African kingdom in a decades-long war with the Fanti; the Ewe live largely as its poor or its pirates",
        "description": (
            "An Asante-and-Twi-run ethno-nation on the Gold Coast, in a long-running war with the "
            "neighboring Fanti that has left most Asante harbors blockaded by Fanti pirates. Well-armed "
            "Asante police patrol Accra and other cities with markedly uneven enforcement, favoring "
            "ethnicity over consistent law. The Ewe, largely excluded from Asante government and "
            "business, live poor or turn pirate -- the Aidoo Clan among them. The free city of Sekondi "
            "sits within reach of Asante territory but governs itself independently as a corporate haven."
        ),
        "notes": "Wild Kingdom. Setting for the Accra and Glidji legwork and the Tan Tien compound near Mampong.",
    },
]

LOCATIONS = [
    {
        "name": "Gravity Bar North",
        "location_type": "nightclub",
        "security_level": "Patrolled / Commercial",
        "summary": "Quieter northern branch of the Gravity Bar chain, popular for private Johnson meets",
        "description": (
            "A calmer counterpart to the chain's downtown location, doing brisk business with the "
            "shadow crowd -- at least three separate 'Johnson parties' are being seated and sorted on "
            "any given night. Private back rooms let a Johnson do business with a waitress closing the "
            "door behind her."
        ),
        "notes": "Forbidden Fruit. Randall Pape hires the runners here for the Green Globe International run.",
    },
    {
        "name": "Sea-Tac Airport Hangar 8",
        "location_type": "air freight hangar",
        "district": "Sea-Tac Airport, north side",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "Green Globe International",
        "summary": "Private freight hangar where GGI loads its Hawker-Ridley Skytruck for the run to Peru",
        "description": (
            "A private air-freight hangar on the north side of Sea-Tac, leased by GGI for the "
            "expedition. Ground crew load crates of scientific gear and a motorboat under Dr. Fukuhara's "
            "watchful eye while dwarf rigger/mechanic Melissa preps the Skytruck."
        ),
        "notes": "Forbidden Fruit. Departure and return point; Pape provides falsified passports here.",
    },
    {
        "name": "Iquitos",
        "location_type": "transportation hub",
        "city": "Peru",
        "summary": "Riverside Peruvian city with no roads in, just the airport and the Amazon -- Bicho's home base and the expedition's staging point",
        "description": (
            "A city that, from the air, looks impossible: no roads lead to it, just the airport runway "
            "and the huge shining curve of the Amazon River, everything else jungle. Bicho keeps his boat "
            "docked here and knows the harbor, the traffic (mostly motorcycles, which recognize and dodge "
            "his ancient Landrover on sight) and the airport guards well enough to bribe them to watch the "
            "expedition's hangar. The team's outbound and return flights both pass through here."
        ),
        "notes": "Forbidden Fruit. Staging and return point; Bicho's boat, the Golfinhao, is docked here between runs.",
    },
    {
        "name": "Leticia",
        "location_type": "border outpost",
        "city": "Amazonia",
        "district": "Peru/Amazonia border, on the Amazon River",
        "controlling_org": "Amazonia",
        "summary": "Fortified river-border checkpoint into Amazonia: gun towers, a fast patrol boat and a standing Jaguar shaman",
        "description": (
            "A jumble of flimsy wood-and-tin buildings that exists to keep the border guards company, "
            "dominated by two machine-gun towers, a satellite-linked military building and a well-armed "
            "GMC Riverine patrol boat -- 'if this place is a town, then you're Lofwyr.' Guards check "
            "passports and search boats for people (not contraband) with bored efficiency: a routine "
            "search ends with a curt 'The border is closed for the rest of today. You are welcome to "
            "sleep in town or on your boat. I will keep your passports until the morning' -- not "
            "suspicion, just a soccer match against Aztlan the whole post wants to watch. Push the guards "
            "and the mood flips fast: nine on-duty and ten off-duty guards plus a Jaguar shaman (Analyze "
            "Truth, river/jungle spirit conjuring) respond hard and fast to any real trouble."
        ),
        "notes": (
            "Forbidden Fruit. The border closes for a day so guards and villagers can watch an "
            "Amazonia-Aztlan soccer match, forcing the expedition's overnight jungle jaunt for kiwis. "
            "Nine on-duty Border Guards (Firearms 5, Colt Manhunters, tower LMGs and a Mag-3/thermographic "
            "sniper rifle) plus the patrol boat's two LMGs and turret assault cannon; generic squad, not "
            "built as NPC rows. Amazonia pays a 5,000-nuyen bounty per wyrd mantis killed."
        ),
    },
    {
        "name": "Dillman Theater",
        "location_type": "movie theater",
        "security_level": "Patrolled / Commercial",
        "summary": "Old-style flatscreen theater used for the Phoenix Biotechnologies hiring meet",
        "description": (
            "A single-screen, old-style flatscreen movie house downtown. Rachel Liseli books a private "
            "showing under the name 'Raether' to meet the runners, her bodyguard Cheveyo covering her "
            "from the projection booth with a silenced, smartlinked Remington 950."
        ),
        "notes": "Wild Kingdom. Meet site for the Phoenix Biotechnologies escort contract.",
    },
    {
        "name": "Pier 121, Miami",
        "location_type": "commercial district",
        "city": "Miami, CAS",
        "summary": "Miami dock where the runners board the PCS Tangakwunu and meet PBT handler Cairo",
        "description": (
            "A working pier in Miami harbor, hot enough that 'the harbor smells like baking asphalt "
            "instead of diesel fumes.' PBT arranges ground transport from the airport straight to the "
            "gangplank, where Cairo and her bodyguards wait to check the team aboard the Tangakwunu."
        ),
        "notes": "Wild Kingdom. Named only as the embarkation point; not detailed beyond the boarding scene.",
    },
    {
        "name": "Bermuda",
        "location_type": "transportation hub",
        "city": "Bermuda",
        "summary": "Mid-voyage stop where fixer Rain loads supplementary PBT cargo aboard the Tangakwunu",
        "description": (
            "A beautiful, espionage-riddled stopover roughly a third of the way to Sekondi, where fixer "
            "Rain meets the ship to load surgical equipment, MRI scanners, refrigeration units and "
            "Caribbean-creature tissue samples, and to collect the second stage of the runners' payment "
            "in PBT stock. Rain wants the transfer done and the ship gone before it attracts attention."
        ),
        "notes": "Wild Kingdom. Rain's base of operations; not otherwise detailed beyond the resupply scene.",
    },
    {
        "name": "Sekondi",
        "location_type": "free city",
        "city": "Gold Coast, West Africa",
        "security_level": "Corporate Extraterritorial",
        "summary": "West African free city where dozens of megacorps buy protection and business under a shared truce, governed by twin Ga leaders",
        "description": (
            "A modern city of white-concrete high-rises on the Gold Coast, formed when the Asante Nation "
            "pressured the Ga people to assimilate or leave; the Ga took the old city of Sekondi and "
            "traded corporations land free of law for security and money. Every corp based there has "
            "agreed to keep Sekondi's streets quiet -- trouble that starts within the walls is punished "
            "by the best joint military response the city can muster, though a running gun battle right "
            "up to the gates is tolerated. Ninety-five percent of residents are African; nearly every "
            "Caucasian, Native American or Asian face belongs to a corporate uniform."
        ),
        "notes": (
            "Wild Kingdom. Phoenix Biotechnologies' drop-off point and Ahmadou Kourouma's base; runners "
            "are housed in a PBT-owned shadowrunner suite (six rooms, no vidphones, real phones only) "
            "pending cargo inventory. Legwork here (Sekondi background, mami wata, biotech corps, Tan "
            "Tien) is summarized in this spec's notes rather than reproduced verbatim."
        ),
    },
    {
        "name": "Accra",
        "location_type": "commercial district",
        "city": "Asante Nation",
        "summary": "Older, dirtier port city under uneven Asante policing; the runners' trail to the Aidoo pirates starts here",
        "description": (
            "A big port city that resembles Sekondi in its wealthier quarters but is older and less "
            "clean, with primitive facilities in the poorer districts. Well-armed Asante police patrol "
            "everywhere, but enforcement runs on ethnic favoritism rather than consistent law; runners "
            "who stick to back streets and sleazy areas are generally left alone."
        ),
        "notes": (
            "Wild Kingdom. Twi pirate informant Awotwi Tetteh approaches the runners here and points them "
            "to Gavivi Aidoo's clan in Glidji."
        ),
    },
    {
        "name": "Glidji",
        "location_type": "squatter camp",
        "city": "Asante Nation",
        "district": "shantytown east of Accra",
        "security_level": "No Security / Barrens",
        "controlling_org": "Aidoo Clan",
        "summary": "Shantytown home of the Aidoo pirate clan, entirely loyal to patriarch Gavivi Aidoo",
        "description": (
            "A small shantytown east of Accra where Gavivi Aidoo's entire pirate clan lives, poor even "
            "by local standards. Every resident is part of Aidoo's kin-network -- friendly to outsiders "
            "but close-mouthed, and quick to report interested strangers to Gavivi."
        ),
        "notes": (
            "Wild Kingdom. Gavivi trades information (Tan Tien's Volta River facility near Mampong) for "
            "cash, food, medicine or work. Hostile approaches bring twenty-three armed residents running."
        ),
    },
    {
        "name": "Tan Tien Compound",
        "location_type": "corporate facility",
        "city": "Asante Nation",
        "district": "Volta River, near Mampong",
        "security_level": "Corporate High Security",
        "controlling_org": "Tan Tien Incorporated",
        "summary": "Razor-wired brain-computer-interface research compound defended by camera- and sonic-implanted paranimals",
        "description": (
            "A seven-kilometer walk from the Volta River through jungle, ringed by a six-meter "
            "razor-wired, electrified fence with a remote gate. Inside: an eight-meter concrete pit "
            "holding two troops of asonwu pack-monkeys released via remote ladder; a four-story security "
            "tower with a smartlinked assault cannon and heavy machine gun on a rotating track, staffed "
            "by a security rigger and two guards; a vehicle lot, fuel depot and repair garage; wage-slave "
            "and executive living quarters (sixty wageslaves and thirty researchers, eleven of them "
            "abductees like Dicristofaro); an exercise yard patrolled by ekyelebenle (Awakened green "
            "mambas); and a main office/lobby with gomatia (giant chameleons, Adaptive Coloration) that "
            "snare astral forms, magic-users and anyone smelling of gunpowder. The research building "
            "houses the compound's main computer and a basement of caged satyrs and datajacked lab rats "
            "kept for DNA research."
        ),
        "notes": (
            "Wild Kingdom. Tan Tien employs no magicians and relies entirely on paranimal security fed "
            "through a security rigger's display; all animals carry implanted cameras and sonic "
            "control/frenzy cyberware. Twelve guards (Wired Reflexes 1, Smartlink 1, Louh Fu assault "
            "rifles) staff the tower and lobby; the Tan Tien Research Computer host is detailed under "
            "MATRIX_HOSTS. Fenced value beyond Dicristofaro: four GMC-Nissan hovertrucks (~25,000 nuyen "
            "each fenced), the security rigger's deck and animal sonic cybernetics (~21,000 nuyen for one "
            "of each undamaged), trained gomatia/ekyelebenle (~2,500 nuyen each), a hovertruck of "
            "antivenin and medical supplies (~20,000 nuyen)."
        ),
    },
    {
        "name": "PCS Tangakwunu",
        "location_type": "ship",
        "city": "Atlantic Ocean",
        "district": "Miami-Bermuda-Sekondi crossing",
        "controlling_org": "Phoenix Biotechnologies",
        "summary": "Pueblo Corporate Ship (Merchantman-class) secretly carrying an enslaved neurologist to PBT's Sekondi research arm",
        "description": (
            "A newly-minted, two-hundred-meter black Merchantman-class freighter flying Pueblo Corporate "
            "Council colors, chartered by Phoenix Biotechnologies for the 22-day run from Miami to "
            "Sekondi via Bermuda. Two tripod-mounted medium machine guns sit in the conning tower; eight "
            "hidden tracking signals let PBT find the ship if needed. Dr. Dicristofaro is held in a "
            "soundproof, Barrier-16 cabin near the engine room behind a Rating-5 astral ward, marked on "
            "the manifest as 'biological samples.'"
        ),
        "notes": (
            "Wild Kingdom. Handling 5, Speed 10, Hull 8, Accommodations 25, Cargo 270,000 CF. Ewe pirates "
            "hired by Tan Tien breach the hull with a monofilament saw from a mini-submarine while mami "
            "wata storm the deck as cover; the ship makes it to Sekondi regardless, riding lower and "
            "slower. A run of optional Bermuda Triangle/Caribbean encounters (megalodons, a Nomad spirit, "
            "sea drakes, ghost sailors, sea-spirit illusions) is available but not built as content here."
        ),
    },
    {
        "name": "Woodland Park Zoo",
        "location_type": "zoo",
        "security_level": "Patrolled / Commercial",
        "summary": "Seattle's public zoo, meet site for the Baser Instincts Johnson and the setting of its climactic battle",
        "description": (
            "A landscaped city zoo whose insect house serves as a quiet meet spot (crowds instinctively "
            "avoid it) and whose primate area, small mammal exhibit and Large Animal section (elephant "
            "and behemoth pens, including a baby juggernaut) become a running battlefield when Reginald "
            "Disball, possessed by an astral entity, tries to release the zoo's largest animals into the "
            "surrounding district."
        ),
        "notes": (
            "Baser Instincts. Three attack waves (primates, then small mammals/birdmen, then the Large "
            "Animal area) cover Disball's run to the behemoth pens; bystander fire risk and body count "
            "affect the runners' standing with the zoo and animal-rights groups afterward. A 10,000-nuyen "
            "bonus and minor celebrity await a team that clears the incident without killing more than a "
            "handful of animals."
        ),
    },
    {
        "name": "Parashield Sales & Service Center",
        "location_type": "corporate facility",
        "security_level": "Corporate Standard",
        "controlling_org": "Parashield, Inc.",
        "summary": "Parashield's Seattle sales office, veterinary clinic and animal containment area, in an Ares Macrotechnology-owned office park",
        "description": (
            "A two-story, windowless-ground-floor plascrete building in an Ares Macrotechnology office "
            "warehouse park, patrolled by Knight Errant on 45-minute cycles (Ares does not include "
            "top-tier security in the rent). The ground floor splits between an animal containment/"
            "exhibition area, a veterinary clinic and storage; sales offices and the company database "
            "occupy the second floor. Two hell hounds with Flame Aura, a specially-bred barghest and two "
            "synergistic talis cats guard the building."
        ),
        "notes": (
            "Baser Instincts. Holds full sales, shipping and medical records tying the attacking animals "
            "to Fort Lewis Zoological Gardens and, ultimately, to Reginald Disball. The Parashield "
            "Database host is detailed under MATRIX_HOSTS."
        ),
    },
    {
        "name": "Fort Lewis Zoological Gardens",
        "location_type": "zoo",
        "district": "Fort Lewis",
        "summary": "Military-adjacent zoo with an uncannily successful paranimal breeding program -- and Reginald Disball on staff",
        "description": (
            "The best zoo on the coast for paranimals outside rumored Tir Tairngire private collections, "
            "run in cooperation with the neighboring Fort Lewis military base; its breeding program's "
            "success is unexplained even by its own staff. Landscaped to look like real habitats, with "
            "speaker-piped jungle sound and a mix of real and plastic underbrush. Animal handler Reginald "
            "Disball lives on zoo grounds for late-night emergencies."
        ),
        "notes": (
            "Baser Instincts. Zoo records rent space on UCAS military host #26530 (see MATRIX_HOSTS, "
            "Fort Lewis Zoological Gardens system); Parashield holds the access password as the zoo's "
            "sales agent. Fort Lewis soldiers can carry weapons through zoo grounds without much scrutiny."
        ),
    },
    {
        "name": "Hollywood Hospital",
        "location_type": "hospital",
        "district": "Redmond Barrens, Hollywood",
        "security_level": "No Security / Barrens",
        "summary": "Barrens charity hospital that treated a spike of dog-bite patients from Disball's paranimal pack",
        "description": (
            "A charity hospital serving the Hollywood area of the Redmond Barrens, reporting an unusually "
            "high number of dog-bite patients in the days before the runners are hired -- doctors here "
            "are the first to connect the wounds to a single roaming pack rather than scattered strays, "
            "making the hospital a natural legwork stop before the runners go looking for the animals "
            "themselves. Its proximity is also the only reason the local Brain Eaters gang didn't lose "
            "more people when the same pack mauled them."
        ),
        "notes": "Baser Instincts. Named only as a legwork source; not detailed beyond that.",
    },
    {
        "name": "Blackstone's Zoo",
        "location_type": "zoo",
        "district": "Snohomish",
        "summary": "Private Snohomish zoo that lost several dogs on loan from Fort Lewis, unwittingly seeding the Barrens dog pack",
        "description": (
            "A private Snohomish zoo that reported several dogs missing from its kennels shortly before "
            "the Barrens attacks started. A newsfax check turns up the loss; a call to the zoo confirms "
            "the missing animals were on loan from the Fort Lewis Zoological Gardens breeding program, "
            "and Seattle's animal-license database ties them to Reginald Disball by name -- one more "
            "thread in the chain that leads the runners to him."
        ),
        "notes": "Baser Instincts. Named only as a legwork source; not detailed beyond that.",
    },
]

NPCS = [
    {
        "name": "Randall Pape",
        "role": "Green Globe International executive who arranges the shadow border crossing for the Amazonia kiwi run",
        "archetype": "Corporate Executive",
        "title": "Executive, Green Globe International",
        "race": "Human",
        "gender": "Male",
        "organization": "Green Globe International",
        "connection": 3,
        "description": (
            "A tall, calm, pragmatic man, ex-Shiawase Envirotech, who sees the shadow crossing as simple "
            "necessity rather than a moral compromise -- and keeps his more principled partner "
            "deliberately in the dark about it. Amiable but businesslike at the meet, sipping soykaf while "
            "he sizes up the room: 'Thank you for coming. I represent a local agricultural company that's "
            "trying to obtain plant samples from the jungles of Amazonia ... would a hundred thousand "
            "nuyen divided among you be enough to buy your services for a week?' Deflects questions about "
            "the cargo with practiced vagueness -- 'I can assure you that it isn't poisonous, carnivorous "
            "or hazardous in any way' -- and lets the scientists handle specifics once the plane is in "
            "the air."
        ),
        "background": (
            "Left Shiawase Envirotech to help found Green Globe International. When Amazonia reneges on "
            "GGI's legal expedition permit with the Dunkelzahn bequest deadline looming, he pitches his "
            "more scrupulous partner on a shadow alternative over the office intercom: 'Just because I no "
            "longer work for Shiawase doesn't mean I've lost all my contacts. I know an individual who can "
            "help us arrange for a, shall we say, less official border crossing.' When Danforth balks, "
            "Pape lays out the calculus flatly -- 'We're a small fish in a pond full of sharks, and the "
            "only reason we haven't been snapped up yet is that we haven't produced anything worth taking "
            "over' -- and gets his reluctant blessing to proceed, promising, 'You won't regret this, "
            "Edwin. It's the same expedition -- just with a few different guides.'"
        ),
        "notes": (
            "No stat block given in the book; roleplay as a professional Mr. Johnson. Offers 100,000 "
            "nuyen (20,000 up front), negotiable up 25%, +10,000 nuyen if a rigger pilots the Skytruck. "
            "Pays out per outcome: full kiwis + a living scientist = full pay + possible future work; "
            "fruit but no scientists = 25% of the balance; nothing credible = no pay and a bad reputation "
            "put about."
        ),
    },
    {
        "name": "Edwin Danforth",
        "role": "GGI's principled dwarf partner, who refuses to know the details of the shadow crossing he approved",
        "archetype": "Corporate Executive",
        "title": "Partner, Green Globe International",
        "race": "Dwarf",
        "gender": "Male",
        "organization": "Green Globe International",
        "connection": 1,
        "description": (
            "A small, hot-tempered dwarf who storms into his partner's office and hurls his simulated-"
            "leather briefcase at the couch when he learns Amazonia has killed the legal expedition: "
            "'Those bastards ... They let us spend ten months and half a million nuyen planning this "
            "expedition, never voicing a word of complaint, and now that we've got everyone lined up and "
            "paid in advance, now they tell us they're unwilling to let us upset the delicate ecological "
            "balance of the region.' Genuinely proud that GGI has 'avoided the corruption and crime the "
            "megas are full of' and has built its reputation on 'doing honest business' -- proud enough "
            "that he refuses point-blank when Pape first raises hiring shadowrunners: 'I don't like that "
            "kind of thing, Randall.'"
        ),
        "background": (
            "Co-founder and partner at Green Globe International alongside Randall Pape; the more "
            "principled half of the partnership, and the one who has to be talked into compromising his "
            "principles rather than lose ten months and half a million nuyen of preparation. Gives his "
            "reluctant blessing to the shadow crossing on one condition: 'Just do your dirty work and "
            "leave me out of it.'"
        ),
        "notes": "Forbidden Fruit. Appears only in the opening Seattle office scene; never meets the runners. No stat block given.",
    },
    {
        "name": "Dr. Eiji Fukuhara",
        "role": "GGI's elf ecologist and self-appointed expedition leader, killed by kiwi-borne insect larvae",
        "archetype": "Scientist",
        "title": "Ecologist, Green Globe International expedition",
        "race": "Elf",
        "gender": "Male",
        "nationality": "Japanese descent (UCAS)",
        "organization": "Green Globe International",
        "connection": 2,
        "description": (
            "A slender elf of Japanese descent, University of Pittsburgh graduate, who proposed the "
            "expedition and treats every obstacle -- hostile patrols, incoming gunfire -- as just another "
            "scientific problem to work around. Opens the in-flight briefing by pulling down a viewscreen "
            "and running through slides: 'If I could have everyone's attention for a few moments? Thank "
            "you. I'd like to take this opportunity to familiarize everyone with the objectives of our "
            "expedition and to answer any questions you may have,' and lectures for forty-five minutes on "
            "actinidia amazonensis and its alkaloid-rich soil chemistry without noticing eyes glazing "
            "over. Focused to the point of stubbornness and, after years in the lab, prone to forgetting "
            "that normal people don't follow his jargon; when the vines finally turn up, his only reaction "
            "is quiet triumph: 'Gentlemen, I give you actinidia amazonensis.'"
        ),
        "background": "Proposed the Brazilian-kiwi expedition to Green Globe International and considers himself its driving force and de facto leader from the moment the plane leaves Sea-Tac.",
        "notes": (
            "Forbidden Fruit. B3 Q3 S2 C3 I6 W5, Ess 3.65, R4; Biology 6 (Ecology 8), Computer 4, "
            "Etiquette (Corp) 3, Japanese 6, Leadership 3; Datajack, retinal display link, 600 Mp FIFF "
            "memory. Gear: medikit, Nav-Dat GPS, survival kit, wrist computer. Killed late in the run when "
            "spider-beast larvae hatch out of the kiwis he is carrying and burrow into him overnight; he "
            "never wakes."
        ),
    },
    {
        "name": "Dr. Mohammed Al-Mansour",
        "role": "GGI's hobgoblin phytogeographer, a Syrian refugee and the expedition's only armed scientist",
        "archetype": "Scientist",
        "title": "Phytogeographer, Green Globe International expedition",
        "race": "Hobgoblin",
        "gender": "Male",
        "nationality": "Syrian (emigre to UCAS)",
        "organization": "Green Globe International",
        "connection": 2,
        "description": (
            "A sour-faced, solitary hobgoblin -- olive skin, beady eyes, pointed teeth, a build like 'a "
            "cross between an ugly elf and a skinny ork' -- who gives newcomers a flat 'Good morning' with "
            "no sign he thinks the morning is good at all. Polite but deeply suspicious of humans; his "
            "military background and self-defense training make him the expedition's only armed "
            "scientist, and his solitary, watchful manner makes him an obvious suspect once things go "
            "wrong. Genuinely lights up only once, sat-maps in hand: 'I found a place only a few klicks "
            "from here. And we can walk there!'"
        ),
        "background": (
            "Fled a fundamentalist regime that seized power in his native Syria, hoping emigration to the "
            "UCAS would end the persecution of metahumans -- only to be viciously beaten by human-"
            "supremacist thugs about a week after he arrived. Took a job with Green Globe International "
            "and moved to Seattle, but still carries the chip on his shoulder from the beating and keeps "
            "his distance from everyone but his work."
        ),
        "notes": (
            "Forbidden Fruit. B4 Q3 S4 C1 I5 W4, Ess 4.8, R4; Arabic 6, Biology 5, Computer 3, Etiquette "
            "(Corp) 2, Firearms 4, Physical Sciences 4 (Geology 6), Stealth 2, Unarmed Combat 4; Datajack, "
            "100 Mp memory. Gear: Narcoject Rifle, Walther PB-120 with 100 rounds, medikit, GPS, survival "
            "kit. Nearly kills Bicho in a fear-and-suspicion-fueled fight after Fukuhara's death; survives "
            "the return trip if the runners intervene."
        ),
    },
    {
        "name": "Dr. Carl Sanders",
        "role": "GGI's gregarious, cyberware-free ethnobotanist, infested by an insect larva that drives him to self-mutilate",
        "archetype": "Scientist",
        "title": "Ethnobotanist, Green Globe International expedition",
        "race": "Human",
        "gender": "Male",
        "organization": "Green Globe International",
        "connection": 2,
        "description": (
            "A likable, down-to-earth University of Washington graduate who disdains cyberware and "
            "prefers real fieldwork to simsense reconstructions -- a maverick reputation he rather enjoys. "
            "An excellent storyteller who can while away hours on his college days and past expeditions, "
            "with a sly twinkle in his eye whenever he delivers the expedition's standing rule: no one "
            "eats the kiwis, on account of the local legends about them being hallucinogenic -- a rule he "
            "looks like he plans to break himself the moment no one's watching. When asked about border "
            "patrols and paranormal animals he can only blink and pass the question back to the runners: "
            "'That's your department, isn't it?'"
        ),
        "notes": (
            "Forbidden Fruit. B3 Q2 S2 C5 I6 W5, Ess 6, R4; Biology 6 (Botany 8), Biotech 3, Car 2, "
            "Computer 3, Etiquette (Corp) 3, Motorboat 3, Negotiation 4, Sociology 5 (Anthropology 7), "
            "Spanish 4. Gear: medikit, GPS, survival kit, wrist computer. A larva hatched from a kiwi he "
            "was examining burrows into his arm overnight, its hallucinogenic secretions driving him to "
            "hack at himself with Bicho's borrowed machete; survives if subdued, but stays disoriented and "
            "unable to explain what happened for the rest of the trip."
        ),
    },
    {
        "name": "Roberto \"Bicho\" Xavier",
        "role": "Ex-Brazilian-army guide out of Iquitos who gets the expedition across the Amazonia border and back",
        "archetype": "Guide",
        "title": "Independent guide, Iquitos, Peru",
        "race": "Human",
        "gender": "Male",
        "nationality": "Brazilian",
        "connection": 3,
        "description": (
            "A gaunt, deeply tanned, fiftyish veteran with dark sunglasses and a toothy grin, who greets "
            "the expedition at the foot of the Skytruck's stairs with a wave and a chummy 'Oi, "
            "chummeros ... I've taken care of customs for now, but the sooner we get unpacked and on our "
            "way, the less attention we attract, hmm?' Practical to the point of ruthlessness -- he vetoes "
            "the expedition's brand-new boat on sight ('You think you can get a new, expensive boat like "
            "this across the border? You might as well paint ILLEGAL FOREIGN RESEARCH on the side in big "
            "orange letters') and talks the scientists out of armor with the same blunt logic ('What good "
            "will it do you? None, against a snakebite, or a basilisk's eyes, or a caiman -- they don't "
            "eat you until after they've drowned you'). Distrusts and dislikes metahumans, though he "
            "usually hides it well; hates Amazonia's government and its paranormal wildlife in equal "
            "measure, and his temper finally cracks once the kiwis start costing him everything: 'Damn "
            "you and your stupid fruit, you troga! You've ruined me, do you realize that?!'"
        ),
        "background": (
            "A Brazilian army sergeant stationed at Fonte Boa when dragons and metahumans first attacked "
            "Brazil in 2033; his squad was ordered downriver to protect Manaus and was decimated by "
            "hit-and-run paranimal attacks within two days, and Bicho alone survived the week-long retreat "
            "to the Peruvian border. Settled in Iquitos, making a meager living guiding tourists -- and "
            "quieter expeditions -- into the rainforest he came to know all too well."
        ),
        "notes": (
            "Forbidden Fruit. B5 Q4 S4 C3 I4 W5, Ess 5.5, R4; Armed Combat 4, Boats (B/R) 3, Car 3, "
            "Etiquette (Street) 3, Firearms 5, Leadership 3, Motorboat 4, Negotiation 3, Portuguese 6, "
            "Spanish 5, Stealth 4 (Wilderness 6), Unarmed Combat 4; Boosted Reflexes 1. Gear: Defiance "
            "T-250 shotgun, Ruger Super Warhawk, machete, survival knife, thermographic goggles. Owns and "
            "pilots the Golfinhao (Handling 4, Speed 15, Body 6, Armor 3). Nearly kills Dr. Al-Mansour in "
            "a fear-driven fight after Fukuhara's death; potential contact for future Amazonia work."
        ),
    },
    {
        "name": "Melissa",
        "role": "Dwarf rigger/mechanic who preps and can fly GGI's Skytruck to Peru",
        "archetype": "Rigger",
        "title": "Freelance rigger/mechanic",
        "race": "Dwarf",
        "gender": "Female",
        "connection": 2,
        "description": (
            "A blunt, competent dwarf in bib overalls that look like she's never taken them off, a "
            "flashlight hanging out of her mouth like a cigar. Grunts a hello and lays out the terms flat: "
            "'I ain't hired to tell you how to fly this thing or to tell you what to do with it once it's "
            "in the air. But I'll tell ya this -- I personally worked on this flying ceegar, and I can "
            "guarantee that if you don't screw up, this baby can fly just about anywhere.'"
        ),
        "background": "Runs a freelance vehicle maintenance yard near Fort Lewis in Seattle; hired to prep and, if no runner rigger wants the job, fly Green Globe International's Skytruck to Peru and back.",
        "notes": (
            "Forbidden Fruit. Use the Dwarf Technician statistics (SRII p. 206) with gender swapped, two "
            "vehicle skills at Rating 5 and two at Rating 4; no remote-operation skills. Flies the team's "
            "Skytruck to Iquitos and back if no runner rigger takes the job (she does not accompany the "
            "expedition into Amazonia). Potential contact through roleplay."
        ),
    },
    {
        "name": "Albert Dicristofaro",
        "role": "JHIH neurologist extracted under false pretenses and shipped to Africa as forced labor for Phoenix Biotechnologies",
        "archetype": "Scientist",
        "title": "Neurologist (comparative brain structure)",
        "race": "Human",
        "gender": "Male",
        "nationality": "UCAS (Anglo)",
        "organization": "Phoenix Biotechnologies",
        "connection": 1,
        "description": (
            "A short, pudgy, balding Anglo man with brown hair and blue eyes, normally quiet, fussy and "
            "compulsively neat, reduced to hysteria and terror once he realizes his 'promotion' is a "
            "one-way trip into corporate slavery. Naive enough at first to gush about his 'celebration' -- "
            "'I think making it here alive calls for a party. I've never been shot at before. I swear, "
            "when we were diving for the car, a bullet--' -- and then, the instant he understands his "
            "cabin door has locked him in, desperate enough to hurl himself at cold-rolled steel bare-"
            "handed: 'WAIT!' Alternates for the rest of the adventure between demanding his rights, "
            "pleading for help and shocked disbelief at the danger around him."
        ),
        "background": (
            "Worked at JHIH Corporation in Baltimore on comparative neurology -- the differences in how "
            "human, metahuman and animal brains process sensory data -- until a Phoenix Biotechnologies "
            "recruiter offered him better pay, direct access to his results and a Bahamas lab post. He "
            "agreed to an extraction on a whim; ended up locked in a soundproof cabin bound for Sekondi "
            "instead."
        ),
        "notes": (
            "Wild Kingdom. B2 Q1 S2 C3 I6 W4, Ess 4.8, R4; Biology 6 (Medicine 8, Neurology 10), Biotech "
            "4 (Organ Culture 6, Brain 8), Cybertechnology 5, Electronics 4, Etiquette (Corp) 3, Physical "
            "Sciences 3, Psychology 4; Datajack, 300 Mp FIFF headware memory. Weighs 101 kilos, which "
            "matters for the jungle chase (carrying him is 'no picnic'). The runners' central moral "
            "decision: return him to PBT for pay, or free him and strand themselves in Africa."
        ),
    },
    {
        "name": "Rachel Liseli",
        "role": "Disguised PBT handler who hires the runners for the Tangakwunu escort under the cover name 'Raether'",
        "archetype": "Corporate Handler",
        "title": "Resources adjustment developer, Phoenix Biotechnologies",
        "race": "Human",
        "gender": "Female",
        "nationality": "Zuni Native American (disguised as Indian for the meet)",
        "organization": "Phoenix Biotechnologies",
        "connection": 3,
        "description": (
            "Young, enthusiastic and thoroughly a product of management training, munching popcorn with "
            "silver-ringed fingers in an empty theater. Opens with brisk professionalism -- 'I've heard "
            "you can pull off bodyguard and escort services, and aren't afraid of a serious time "
            "commitment or travel. We need professional freelancers to escort an ocean liner of valuable "
            "cargo through the Caribbean League and well beyond' -- and hypes the job as a challenge as "
            "much as a paycheck once the runners show interest. Wears melanin-adjustment drugs and hair "
            "extensions at the meet to appear Indian rather than her true Zuni complexion -- a precaution "
            "against JHIH spies, not an attempt to mislead the runners specifically; she looks different "
            "if they meet her again."
        ),
        "notes": (
            "Wild Kingdom. Use the Mr. Johnson statistics (SRII p. 210) plus a video recorder and "
            "low-light cybereyes. Pays in PBT stock across three stages (500 shares up front, 2,500 more "
            "in Bermuda, 4,000 at delivery); can push cash-equivalent offers up 50% under negotiation. "
            "Genuinely unaware that Dicristofaro is aboard the ship as cargo."
        ),
        "contact_skills": ["Phoenix Biotechnologies hiring and logistics"],
    },
    {
        "name": "Cheveyo",
        "role": "Rachel Liseli's bodyguard, covering her from the projection booth during the Dillman Theater meet",
        "archetype": "Bodyguard",
        "title": "Bodyguard to Rachel Liseli",
        "connection": 1,
        "description": (
            "A silent presence in the Dillman Theater's projection booth, ready to drop an offending "
            "runner with a silenced, smartlinked Remington 950 the instant Liseli signals trouble."
        ),
        "notes": "Wild Kingdom. Use the Bodyguard statistics (SRII p. 49). No further characterization given.",
    },
    {
        "name": "Cairo",
        "role": "PBT handler who receives Dicristofaro and pays off his extraction team at the Miami docks",
        "archetype": "Corporate Handler",
        "title": "PBT handler, Miami pickup",
        "organization": "Phoenix Biotechnologies",
        "connection": 2,
        "description": (
            "A tanned corporate employee in white, an enormous sun hat and dark glasses, backed by three "
            "armed elven bodyguards (one greased in sunblock 'like heavily armed bacon fat'). Cool and "
            "procedural at the handoff: 'Dr. Albert Dicristofaro, this is the end of your running. "
            "Welcome to extraterritorial corporate property,' followed by a cellular scan ('Excuse the "
            "precaution, but we need a cellular scan') and a clipped 'Very well. Our agreement is "
            "fulfilled. Good evening' once the extraction team is paid off. Warms up only slightly to walk "
            "Dicristofaro aboard: 'Welcome aboard the PCS Tangakwunu and to Phoenix Biotechnologies, "
            "Albert. I think getting away from Baltimore calls for a little celebration, don't you?' -- "
            "and delivers the Bahamas-to-Sekondi switch with the same bland corporate delicacy: "
            "'Regrettably, the Bahamas fell through. Our cerebral specialists there were downsized to "
            "maximize our competitive value ... We took the liberty of transferring you to our Sekondi "
            "operation.'"
        ),
        "notes": "Wild Kingdom. Prologue only; no stat block given, does not interact with the player-character team.",
    },
    {
        "name": "Rain",
        "role": "Retired shadowrunner turned Bermuda fixer, PBT's contact for the Tangakwunu's mid-voyage resupply",
        "archetype": "Fixer",
        "title": "Fixer, Bermuda",
        "race": "Elf",
        "gender": "Male",
        "nationality": "Anglo",
        "connection": 3,
        "description": (
            "An elegant, black-haired elf who retired from active running to broker deals out of "
            "Bermuda. Unfriendly but strictly professional -- wants the cargo transfer done cleanly and "
            "the runners out of Bermuda before they attract trouble."
        ),
        "background": "A former shadowrunner who settled in Bermuda and now fixes for Phoenix Biotechnologies among other clients, handling mid-voyage resupply for ships like the Tangakwunu.",
        "notes": "Wild Kingdom. No stat block given. Loads supplementary cargo (medical gear, tissue samples) aboard the Tangakwunu.",
        "contact_skills": ["Bermuda fixing and PBT logistics"],
    },
    {
        "name": "Ahmadou Kourouma",
        "role": "PBT's Sekondi contact, who reveals Dicristofaro missing and sends the runners after him",
        "archetype": "Corporate Fixer",
        "title": "Sekondi contact, Phoenix Biotechnologies",
        "race": "Human",
        "gender": "Male",
        "nationality": "Anyi (former Cote d'Ivoire)",
        "organization": "Phoenix Biotechnologies",
        "connection": 3,
        "description": (
            "A heavy man with dark-chocolate skin, close-cut hair and a thick beard, with a nervous habit "
            "of smiling too much. Strides down the dock with an armed khaki-clad escort wheeling what "
            "looks like a battered laundry cart and bellows a greeting in Twi before switching to a "
            "clipped 'What do you want, English?' Delivers the bad news with cold professionalism: 'I'm "
            "afraid our business is not quite completed. A certain bit of valuable cargo that you were "
            "paid to protect is missing ... So you so-called professionals will need to retrieve him if "
            "you hope ever to see your homes again.' Sees corporate slavery as simply business and "
            "dismisses moral arguments against it; retains a residual dislike of orks and trolls from his "
            "childhood, though he sets it aside professionally, and takes visible pride in showing off "
            "Sekondi to outsiders."
        ),
        "background": (
            "Grew up poor in Anyi territory in the former Cote d'Ivoire under constant fear of King "
            "Gissale's anti-human purges. Phoenix Biotechnologies got him out and educated him, buying "
            "absolute loyalty; he loves both his wives, Massan and Tsotso, and will not risk their "
            "position."
        ),
        "notes": (
            "Wild Kingdom. B3 Q4 S4 C3 I5 W4, Ess 5.8, R4; Asante 5, Biotech 3, Car 2, Computer 3, "
            "English 5, Etiquette (Corp) 6, Etiquette (Tribal) 5, Firearms 3, French 7, Negotiation 4, "
            "Twi-Fanti 2; Datajack (Level 2). Pays the retrieval bounty (5,000-10,000 nuyen for proof, "
            "plus buys any Tan Tien loot) and offers equipment at Seattle book value. Becomes a Rating 4 "
            "Enemy in Sekondi (Rating 2 in North America) if Dicristofaro is freed instead of returned."
        ),
        "contact_skills": ["Phoenix Biotechnologies Sekondi operations"],
    },
    {
        "name": "Awotwi Tetteh",
        "role": "Twi pirate informant in Accra who points the runners toward the Aidoo Clan",
        "archetype": "Informant",
        "title": "Twi pirate, Accra",
        "race": "Human",
        "nationality": "Twi",
        "connection": 2,
        "description": (
            "A short, light-skinned man in dated 2030s-style clothes, speaking only Twi-Fanti; approaches "
            "the runners in an Accra bar after a few brush-offs from more close-mouthed locals and offers "
            "to buy a drink for anyone who understands him. Dances around his real grievance until "
            "someone mentions Ewe pirates, then negotiates hard for a favor before he'll talk."
        ),
        "background": (
            "A Twi pirate whose crew lost several jobs and a boatload of his people to the Aidoo clan of "
            "Ewe pirates. Wants revenge -- his first ask is that the runners slaughter as many Aidoo as "
            "they can -- but settles for asking them to hurt the clan's profitable Tan Tien contract "
            "instead once it's clear most runners find outright massacre repugnant."
        ),
        "notes": "Wild Kingdom. No stat block given. Reveals Gavivi Aidoo's boat location off Glidji in exchange for a favor.",
    },
    {
        "name": "Gavivi Aidoo",
        "role": "Patriarch of the Ewe pirate clan hired by Tan Tien to snatch Dicristofaro with trained mami wata",
        "archetype": "Pirate Leader",
        "title": "Patriarch, Aidoo Clan",
        "race": "Human",
        "nationality": "Ewe",
        "organization": "Aidoo Clan",
        "connection": 2,
        "description": (
            "A poor pirate patriarch supporting four wives and their children, pragmatic about selling "
            "secrets once a job is done -- unlike Seattle's shadows, African runners expect it, which is "
            "why local corporate security runs so lethal. Never meets outsiders alone: he sends his "
            "eight-year-old son Ayete to fetch interested parties, and a same-age bodyguard flanks him at "
            "the sit-down, both boys ready to fight if trouble starts."
        ),
        "background": (
            "Patriarch of the Aidoo Clan, always looking for new ways to support his family; recently "
            "took a Tan Tien Incorporated contract -- a loaned mini-submarine and trained mami wata in "
            "exchange for snatching Dr. Dicristofaro off the PCS Tangakwunu -- and pulled it off clean."
        ),
        "notes": (
            "Wild Kingdom. No stat block given; flanked at meetings by his son Ayete and bodyguard Massan "
            "(see their rows for stats). Trades information for cash, food, medicine or work; reveals the "
            "Tan Tien compound's location near Mampong for the right price."
        ),
    },
    {
        "name": "Badu",
        "role": "Ork anti-slavery escort protecting Dicristofaro on the run to Burkina Faso",
        "archetype": "Escort",
        "title": "Anti-slavery escort",
        "race": "Ork",
        "gender": "Male",
        "connection": 1,
        "description": (
            "A former pirate turned anti-slavery activist, moderately chromed, working with two "
            "companions to smuggle freed slaves like Dicristofaro north to sanctuary in Burkina Faso."
        ),
        "background": "Left pirating for anti-slavery work; runs escorts north out of Tan Tien territory with Kofi and the shaman Yao.",
        "notes": (
            "Wild Kingdom. Shares a stat block with Kofi: B5/6 Q5 S6/7 C2 I5 W5, R5, Armor 4/3; Armed "
            "Combat 4, Athletics 5, Biotech (First Aid) 1(4), Firearms 6, Motorboat 4, Stealth (Rural) "
            "5(7), Unarmed Combat 5; Boosted Reflexes 1, Smartgun Link. Gear: Paau pistol with Hi-Ex ammo "
            "(10 rounds left), armored vest, machete, offensive grenades. Fights to keep Dicristofaro free "
            "if the runners try to retake him; if the runners let him go, refuses to let them follow to "
            "Burkina Faso for fear they are spies."
        ),
    },
    {
        "name": "Kofi",
        "role": "Ork anti-slavery escort protecting Dicristofaro on the run to Burkina Faso",
        "archetype": "Escort",
        "title": "Anti-slavery escort",
        "race": "Ork",
        "gender": "Male",
        "connection": 1,
        "description": "Badu's companion; a former pirate turned anti-slavery activist, working the same escort run.",
        "notes": "Wild Kingdom. Shares Badu's stat block (see Badu's notes).",
    },
    {
        "name": "Yao",
        "role": "Ork Nau (Crocodile-ancestor) shaman leading Dicristofaro's anti-slavery escort team",
        "archetype": "Shaman",
        "title": "Nau shaman, anti-slavery escort",
        "race": "Ork",
        "gender": "Male",
        "connection": 2,
        "description": (
            "A Nau (Crocodile-ancestor) shaman escorting freed slaves like Dicristofaro toward Burkina "
            "Faso; goes berserk against the nearest living target if badly injured and fails a Willpower "
            "(3) Test."
        ),
        "background": "Leads Badu and Kofi's anti-slavery escort cell, using Nau totem magic to help freed captives like Dicristofaro slip Tan Tien's pursuit.",
        "notes": (
            "Wild Kingdom. B6/5 Q5 S4 C4 I6 W6, R4; Conjuring (Ancestor Spirits) 4(6), Firearms 3, "
            "Magical Theory (Shamanic) 2(4), Sorcery 5, Stealth (Wilderness) 5(7), Unarmed Combat 3. "
            "Spells: Bullet Barrier 5, Chaos 5, Heal 4, Invisibility 5, Mana Bolt 6, Urban Renewal 4. Gear: "
            "Ruger Super Warhawk with laser sight and Hi-Ex ammo, machete, four gold-teeth fetishes "
            "(reusable, Invisibility). Totem bonuses: +2 combat spells, +1 illusion, +1 sea/river spirit "
            "conjuring, +2 ancestor spirit conjuring."
        ),
    },
    {
        "name": "Mr. Johnson (\"Mike\")",
        "role": "Unnamed fixer secretly working for Lone Star, who hires the runners to run down the Seattle paranimal attacks off the books",
        "archetype": "Fixer",
        "title": "Fixer (Lone Star-linked; name unconfirmed)",
        "race": "Human",
        "gender": "Male",
        "connection": 4,
        "description": (
            "Never gives his name -- street rumor guesses 'Mike' -- and dresses and carries himself like a "
            "cop despite the deliberately casual clothes: dark hair cut unfashionably short, sunglasses "
            "hiding his eyes, no obvious cyberware, shined shoes, and a hand that keeps drifting to a "
            "sidearm that isn't there. Opens the meet in the zoo's insect house with a throwaway line about "
            "the exhibit's declining attendance, then gets straight to business: 'I represent the family "
            "of a victim of one of the recent paranormal animal attacks -- I'm sure you've heard about "
            "them ... The leads in question are slim, but they present the best hope of determining who is "
            "behind the attacks.' Blunt to the point of rudeness -- 'There's the offer. Take it or leave "
            "it' -- but honest with his 'temporary employees' about the odds; will not send runners on a "
            "suicide job without telling them so."
        ),
        "background": (
            "A low-profile Seattle fixer who works only at odd intervals, almost exclusively organizing "
            "runs for law-enforcement and government clients -- linked by rumor to the Veil, ConsOps, the "
            "CIA, Lone Star and Ares, with no confirmed employer. Dress and bearing suggest a military "
            "tour of duty."
        ),
        "notes": (
            "Baser Instincts. B4 Q3 S3 C2 I4 W4, Ess 1.5, R3(5); Armed Combat 2(Club 4), Car 4, Computer "
            "4(Software 6), Etiquette 3(Street 7), Firearms 5(Pistol 7), Negotiation 5(Bargaining 8), "
            "Psychology 3, Stealth 3(Urban 5), Unarmed Combat 2(Subduing 4), Vectored Thrust 4; Chipjack, "
            "Datajack, radio receiver, telephone, voice modulator, Wired Reflexes 1. Gear: Ares Predator "
            "with Smartlink, police baton, concussion mini-grenades, armor clothing, lined coat, Gold "
            "DocWagon contract. Meets the runners in the Woodland Park Zoo insect house, offers 20,000-"
            "30,000 nuyen plus a records whitewash and new SINs; almost certainly Lone Star itself hiring "
            "off the books to solve the crisis before Knight Errant capitalizes on it."
        ),
    },
    {
        "name": "Reginald Disball",
        "role": "Fort Lewis animal handler, unknowingly possessed for years by an astral entity that has been staging the Seattle attacks through him",
        "archetype": "Animal Handler",
        "title": "Animal handler, Fort Lewis Zoological Gardens",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": (
            "Average height, underweight, a fringe of white hair around a balding dome and days of "
            "stubble. Under possession, giving a zoo-crowd presentation, he sounds nervous at first -- "
            "'The recent animal attacks are an aberration. Most of these animals are more afraid of you "
            "than you are of them ... Only someone completely without conscience would use animals in "
            "such a way. I've spent my whole life learning how to take care of these magnificent "
            "creatures -- and what's happening now, the way some lunatic is sacrificing them for some "
            "unfathomable agenda, makes me sick!' -- before his voice steadies into something colder: "
            "'Well, I've been sick for long enough. It's time to do something about it! ... I knew you "
            "were coming. My friends told me. I had hoped to accomplish more, but it's time to end this "
            "... I was going to release the juggernaut and the behemoths later to destroy this filthy "
            "city, but I've changed my mind. You can leave now, and live a little longer. Otherwise ... "
            "so be it.'"
        ),
        "background": (
            "Always got along better with animals than people, and lacked the firmness a good handler "
            "needs -- gentleness, not force, was all he ever wanted to give them -- which should have "
            "capped his career at Fort Lewis Zoological Gardens. At an environmental policlub meeting "
            "years ago, a new member struck up a conversation and, over diner coffee, revealed itself as "
            "a being from the astral planes trapped in the physical world, needing regular contact with "
            "paranimals to keep up its strength and lacking the time to build a legitimate cover to get "
            "near Fort Lewis's collection. In exchange for hosting it, it would help Disball work with the "
            "animals -- and for years the bargain held, quietly making him one of the zoo's best handlers, "
            "the entity's occasional favors disguised as ordinary work requests. Then it seized full "
            "control and began orchestrating the citywide attack wave through him. The remnant of Disball "
            "that remains believes the entity is hunting something and considers its actions regrettable "
            "but necessary; he no longer has the power to stop it."
        ),
        "notes": (
            "Baser Instincts. Unpossessed: B3 Q3 S3 C4 I3 W3, Ess 5.2, R3; Athletics 2, Biology 3 "
            "(Parazoology 4), Firearms 4(Pistol 6), Melee Weapons 4, Psychology 2(Animal 4), Stealth 4, "
            "Unarmed Combat 4; Animal Empathy edge; Chipjack, Datajack, Pathogenic Defense 2. Possessed "
            "(bracketed, treat as Superhuman): B9 Q9 S9 C10 I10 W10, R6, Threat/Professional 6/4. Gear: "
            "Ares Squirt (DMSO/tranq), AZ-150 stun baton, animal handling gear. Dies (or is left catatonic "
            "and amnesiac) when the entity abandons him at the climax, gurgling only 'It will hunt again.'"
        ),
    },
    {
        "name": "The Astral Entity",
        "role": "Unidentified possessing spirit hunting through Reginald Disball and Seattle's paranormal animals",
        "archetype": "Possessing Spirit",
        "race": "Spirit",
        "title": "Astral entity (possessing Reginald Disball)",
        "description": (
            "Never manifests physically -- if forced to, it flees straight to the metaplanes instead. "
            "Speaks only through Disball's stolen mouth, and only once, at the very end, in a body already "
            "dying: 'It will hunt again.' Uses Aura Masking to erase every animal's astral 'fingerprint,' "
            "binds spirits to guard its trail and has already cost Lone Star three mages who tried to "
            "track it astrally -- the astral plane is its home ground, and it uses that advantage without "
            "mercy."
        ),
        "background": (
            "Approached Reginald Disball at an environmental policlub meeting some years before the "
            "adventure, offering him company and, unspoken, a slow foothold. It needs regular contact "
            "with paranimals to sustain itself and had no legitimate way to get close to Fort Lewis "
            "Zoological Gardens' collection; Disball, in exchange for letting it share his body, got "
            "an animal handler's touch he never had on his own. The entity held to the bargain for years, "
            "quietly boosting his career, before seizing full control and staging a three-night wave of "
            "attacks across Seattle for a purpose the book never explains. When cornered at Woodland Park "
            "Zoo it stages its own cover story -- forging a diary that frames Disball as a lone toxic "
            "shaman -- and abandons his body the moment the runners defeat him, leaving no proof beyond "
            "a magically active witness's glimpse of something leaving on the wind."
        ),
        "notes": (
            "Baser Instincts. Force Rating 10, Spirit Power 6; Mental Attributes equal Force Rating. "
            "Powers: Animal Command (controls up to 10 animals as drones simultaneously, opposed Force vs. "
            "Willpower), Aura Masking, Dispelling, Human Form, Possession, Sorcery (nearly all illusion "
            "spells). Abandons Disball once he is defeated or dying, leaving only the line 'It will hunt "
            "again'; framed Disball's diary as a cover story before departing. A loose thread the "
            "gamemaster can bring back as a recurring campaign Threat."
        ),
    },
    {
        "name": "Fred",
        "role": "Shiawase Envirotech technician assisting the secret Lone Star Johnson's paranimal capture operation",
        "archetype": "Technician",
        "title": "Technician, Shiawase Envirotech",
        "gender": "Male",
        "organization": "Shiawase Corporation",
        "connection": 1,
        "description": (
            "An arrogant, jargon-happy field biologist in grubby sewer-worker overalls who treats the "
            "runners as hired hands while chattering with his (unnamed) partner about mRNA strands and "
            "incubus retro-virus theory ('The F-series of mono-nucleotide tests won't work until you get "
            "the proper viral cutters, you moron!'). Snaps into brisk professionalism the instant the "
            "runners show up -- 'Ah. I believe you gentlemen have something for me?' -- and walks them "
            "through the gear with the same clinical calm: 'You'll find two Ares Squirts in each box with "
            "a DMSO/trang load. Don't splash any of it on yourselves unless you really want a nap. Nail "
            "any part of the critter with this stuff and it should go to sleep.' Genuinely delighted "
            "whenever a captured critter turns up, muttering things like 'can't wait to get this baby in "
            "the lab.'"
        ),
        "notes": (
            "Baser Instincts. No stat block given. Issues the team's Ares Squirts (DMSO/tranq load) and "
            "antidote slap patches, and collects captured animals at both the sewer entrance and the "
            "Redmond Barrens pickup."
        ),
    },
    {
        "name": "Sergeant Victor Crocker",
        "role": "Night commander of Lone Star's Paranormal Animal Control substation 25 during the three-night attack wave",
        "archetype": "Police Officer",
        "title": "Night shift commander, PAC Substation 25, Lone Star Security",
        "race": "Human",
        "gender": "Male",
        "organization": "Lone Star Security",
        "connection": 1,
        "description": (
            "Runs the graveyard shift out of PAC substation 25 nursing cups of 'rotgut soykaf' between "
            "escalating calls, dry and weary with his receptionist: 'What's the tally today?' ... "
            "'Surprise, surprise. Stick it in the corp file with all the others.' By the third and worst "
            "night he is out of officers, out of favors and visibly rattled -- 'This thing spins any "
            "further out of control and I'm going to need more than a few favors' -- but never lets the "
            "strain show past dark humor: told Shore Patrol has 'a situation', his only reply is 'Just "
            "tell them to shoot it. Assuming those incompetents can hit it.'"
        ),
        "notes": (
            "Baser Instincts cold open (frame narration only -- never meets the player characters). Fields "
            "reports of devil rat swarms, an incubus causing traffic deaths, a Saeder-Krupp Facility 3 "
            "breakout (a piasma and two cockatrices), a rockworm-collapsed building and a loup-garou "
            "incident, all in one shift, with PAC stretched to nothing and the lieutenant unreachable. No "
            "stat block given."
        ),
    },
    {
        "name": "William Louden",
        "role": "Head of Lone Star Seattle, publicly on the defensive as the paranormal-animal crisis and Knight Errant's needling escalate",
        "archetype": "Corporate Executive",
        "title": "Head of Lone Star Security, Seattle",
        "organization": "Lone Star Security",
        "connection": 1,
        "description": (
            "Appears only at a press conference gone sideways, promising extra patrols to stop the "
            "mayhem and find out who is behind it -- a promise that curdles the instant a reporter asks "
            "whether he plans to pull officers off the organized-crime beat, and the conference collapses "
            "into shouted questions about the Star's failures, DPI witch hunts and why 'whoever was "
            "presumably behind it all' has made no demands."
        ),
        "notes": "Baser Instincts (press-conference mention only). No stat block given; never appears on-scene.",
    },
    {
        "name": "Ayete",
        "role": "Gavivi Aidoo's eight-year-old son, sent to fetch or flank interested outsiders at Glidji",
        "archetype": "Child",
        "title": "Son and messenger, Aidoo Clan",
        "race": "Human",
        "gender": "Male",
        "nationality": "Ewe",
        "organization": "Aidoo Clan",
        "connection": 1,
        "age": 8,
        "description": (
            "An eight-year-old sent by his father to fetch the runners for a meeting once word reaches "
            "Gavivi that they are asking around Glidji; flanks him at the sit-down alongside a same-age "
            "guard, both boys ready to fight if trouble starts."
        ),
        "notes": (
            "Wild Kingdom. Shares a stat block with Massan (see her row): B2 Q4x4 S1 C3 I3 W5, R6; Armed "
            "Combat (clubs) 2(4), Athletics 3, Etiquette (Tribal) 3, Firearms 4(B/R 2), Motorboat 3, "
            "Stealth 4, Unarmed Combat 3. Gear: old kevlar curtain worn as a poncho (2/1), an archaic Colt "
            "9mm carbine recognizable as a submachine gun only on a Firearms (6) Test, four cowrie shells."
        ),
    },
    {
        "name": "Massan",
        "role": "Gavivi Aidoo's other eight-year-old bodyguard, flanking him alongside Ayete",
        "archetype": "Child",
        "title": "Bodyguard, Aidoo Clan",
        "race": "Human",
        "gender": "Male",
        "nationality": "Ewe",
        "organization": "Aidoo Clan",
        "connection": 1,
        "age": 8,
        "description": (
            "Another eight-year-old, flanking Gavivi Aidoo opposite Ayete at meetings, ready to fight if "
            "there is trouble. Shares his name with Ahmadou Kourouma's wife elsewhere in the same "
            "adventure -- almost certainly an editing accident rather than the same person (see header "
            "note)."
        ),
        "notes": "Wild Kingdom. Shares Ayete's stat block (see Ayete's row).",
    },
    {
        "name": "Acossiova",
        "role": "Gavivi Aidoo's thirteen-year-old daughter, intercepted leaving Glidji for Accra and pressed for information",
        "archetype": "Child",
        "title": "Daughter, Aidoo Clan",
        "race": "Human",
        "gender": "Female",
        "nationality": "Ewe",
        "organization": "Aidoo Clan",
        "connection": 1,
        "age": 13,
        "description": (
            "Sullen and guarded with strangers, ready to fight if accosted alone but backs down at the "
            "sight of multiple opponents. Tells what she knows, in Ewe, only under threat or bribe, and "
            "breaks into curses if pushed past that."
        ),
        "background": (
            "Knows that Tan Tien Incorporated contacted her father about snatching a man from a hidden "
            "room on a boat, and that he took the mami wata and a loaned submarine upriver to Mampong "
            "afterward -- but not how Tan Tien learned Dicristofaro was aboard, and nothing more."
        ),
        "notes": "Wild Kingdom. Uses Ayete's stat block if a fight breaks out. No further detail given.",
    },
]

ORG_UPDATES = {
    "Amazonia": {
        "notes_append": (
            "Predator and Prey (Forbidden Fruit, 2059): refuses Green Globe International's legal permit "
            "to sample the Brazilian kiwi (actinidia amazonensis), officially over ecological concerns; "
            "GGI suspects Amazonia wants to monopolize the plant's biomedical potential instead. Its "
            "regrowth magic gives the rainforest itself a Background Count of 1 against urban and "
            "hermetic astral operations (jungle-totem shamans instead get -1), makes nature spirits "
            "easier to conjure at +1 to +3 Force, and lets those spirits refuse orders that would harm "
            "the forest or its creatures (opposed Willpower Test against the summoner). Polices its "
            "Peruvian river border at Leticia with gun towers, a fast patrol boat and a standing Jaguar "
            "shaman; pays a 5,000-nuyen bounty per wyrd mantis killed, and fines captured trespassers "
            "1,000 to 5,000 nuyen depending on what they were caught doing (killing a protected naga is "
            "the worst of it)."
        ),
    },
    "Lone Star Security": {
        "notes_append": (
            "Predator and Prey (Baser Instincts, 2059): a three-night wave of paranormal-animal attacks "
            "overwhelms the Paranormal Animal Control Division -- a piasma loose downtown, a hell hound "
            "and cockatrices escaped from a Saeder-Krupp facility, six PAC officers killed in what look "
            "like deliberate ambushes. PAC substation 25's night commander, Sergeant Victor Crocker, "
            "fields the worst of it (frame narration only -- never meets the runners). Star Seattle chief "
            "William Louden publicly promises more patrols after Knight Errant offers to loan "
            "extermination teams. Lone Star secretly hires the runners off the books, "
            "through an unnamed fixer ('Mr. Johnson (\"Mike\")'), to solve the crisis quietly rather than "
            "let Knight Errant capitalize on it -- new SINs and a records whitewash are the real payment."
        ),
    },
    "Knight Errant Security Services": {
        "notes_append": (
            "Predator and Prey (Baser Instincts, 2059): offers Seattle extermination teams during the "
            "paranimal attack wave, explicitly angling to embarrass Lone Star and take its law-enforcement "
            "contract. KE also patrols (on 45-minute cycles) the Ares Macrotechnology office park housing "
            "Parashield, Inc.'s facility, and can send a CityMaster of 12 officers plus 4 Combat Mage "
            "archetypes as backup if a break-in there escalates."
        ),
    },
    "Saeder-Krupp Heavy Industries": {
        "notes_append": (
            "Predator and Prey (Baser Instincts, 2059): loses a hell hound from a facility on Stewart "
            "Street and a piasma plus two cockatrices (killed handlers, escaped) from 'Facility 3' during "
            "the paranimal attack wave; invokes corporate rights to shut down further Lone Star "
            "investigation both times. Unrelated to Reginald Disball's own animal-control campaign -- just "
            "bad timing."
        ),
    },
    "Ares Macrotechnology": {
        "notes_append": (
            "Predator and Prey (Baser Instincts, 2059): owns the office/warehouse park where Parashield, "
            "Inc. leases its Seattle sales and service center; Ares does not include top-tier security in "
            "the rent, leaving Knight Errant's 45-minute patrol cycles as the only site security."
        ),
    },
    "Mitsuhama Computer Technologies": {
        "notes_append": (
            "Predator and Prey: the Wild Kingdom legwork table (West Africa biotech corps) names 'MCT-"
            "Parashield' alongside Phoenix Biotechnologies and Tan Tien Incorporated as doing paranimal "
            "biotech work on the Gold Coast -- implying MCT owns or partners with Parashield, Inc. Baser "
            "Instincts, set the same year, calls Parashield 'a small local corp' with no parent named. The "
            "book never reconciles the two; flagged rather than resolved."
        ),
    },
    "Shiawase Corporation": {
        "notes_append": (
            "Predator and Prey: a Shiawase Envirotech team (led by a technician named Fred, plus an "
            "unnamed partner) works two encounters of Baser Instincts (2059) for the secret Lone Star "
            "Johnson, tranquilizing and collecting captured paranimals with DMSO/tranq-loaded Ares "
            "Squirts. Separately, Forbidden Fruit's Johnson, Randall Pape of Green Globe International, "
            "is a former Shiawase Envirotech employee."
        ),
    },
    "Brain Eaters": {
        "notes_append": (
            "Predator and Prey (Baser Instincts, 2059): this mostly-human Redmond Barrens gang, based out "
            "by Hollywood, is mauled by Reginald Disball's paranimal dog pack and cedes a piece of its "
            "turf as a result -- lucky to be only a couple of blocks from Hollywood Hospital, or losses "
            "would have been worse."
        ),
    },
    "Pueblo Corporate Council": {
        "notes_append": (
            "Predator and Prey (Wild Kingdom, 2059): the PCS Tangakwunu sails under Pueblo Corporate "
            "Council registry (the crew jokes about a landlocked country flying a ship), chartered by "
            "Phoenix Biotechnologies to carry Dr. Albert Dicristofaro's escort team -- and, unknown to the "
            "PCC, Dicristofaro himself as forced cargo -- to Sekondi."
        ),
    },
}

LOC_UPDATES = {
    "The Barrens (Seattle)": {
        "notes_append": (
            "Predator and Prey (Baser Instincts, 2059): Reginald Disball, possessed by an astral entity, "
            "ambushes the runners with up to ten paranimal dogs (hell hounds, a barghest, a Gabriel hound "
            "posing as a mugging victim, and rarer beasts up to a martichoras, a piasma or a saber-tooth "
            "cat) in a four-block stretch near Hollywood. The Brain Eaters gang cedes turf here after a "
            "mauling by the same pack; Hollywood Hospital reports the resulting spike in dog-bite cases."
        ),
    },
}

NPC_UPDATES = {}

TAG_EXISTING = {}

MATRIX_HOSTS = """
Three systems get full SRII host stats and security sheaves; noted here for a GM who wants to run them,
not built as sr-world DB records.

**Tan Tien Research Computer** (Wild Kingdom, Tan Tien Compound) -- Red-5/11/8/8/10/8, air-gapped from
the Matrix. Ten 125-Mp paydata files (2D6x2,000 nuyen each); intrusion triggers transfer of the files to
Tan Tien's Beijing home office and deletes the local copies.

| Step | Event |
|---|---|
| 4 | Satlink to Tan Tien-Beijing opens, 50 Mp bandwidth |
| 6 | Probe-8 |
| 10 | Passive Alert: Killer-6 |
| 14 | Download/deletion via satlink begins |
| 18 | Blaster-8 |
| 22 | Expert Construct/Offense +2 (Armor), Tar Baby-5, Sparky-7 |
| 27 | Black IC-9 (Armor) |
| 30 | Shutdown |

**Parashield Database** (Baser Instincts, Parashield Sales & Service Center) -- Orange-8/11/12/14/14/11,
one-way SANs only since a rogue-decker breach cut it off from the Matrix. Paydata 2 (2D6x15 Mp).

| Step | Event |
|---|---|
| 3 | Warning suggests re-entering password, Probe-7 |
| 7 | Explosive Scramble activates in all files |
| 10 | Passive Alert |
| 13 | Jammer-6 |
| 16 | Jam-Rip 7 |
| 19 | Tapeworms placed in all files |
| 21 | Active Alert (Hard Corps arrives in 2 minutes) |
| 24 | Shutdown (needs Parashield management codes to restart) |

**Fort Lewis Zoological Gardens system** (Baser Instincts) -- rented space on UCAS military host #26530;
Parashield holds the access password as the zoo's sales agent. Host A is the public-relations gateway
(low security, not detailed in the text). Host B is the overwatch/security chokepoint: Red-9/12/13/16/17/16.
Host C is the zoo database itself: Red-9/10/11/13/13/11, Paydata 3 (2D6x10 Mp). One continuous security
sheaf covers the whole system -- switching hosts does not reset the countdown. A resolved trace on Host C
pulls in a government decker and alerts Hard Corps/Parashield security, who reach the Parashield facility
within two minutes. (Host B's step/event pairing below is reconstructed from a two-column OCR merge in
the scan -- the step numbers and event count line up cleanly, but treat it as best-effort.)

| Host | Step | Event |
|---|---|---|
| B | 3 | Probe-8 |
| B | 7 | Trap Trace 10 (Killer-8) |
| B | 10 | Passive Alert |
| B | 12 | Probe-9 (both Probes attempt to raise the sheaf) |
| B | 13 | Expert Construct (Armor) |
| B | 17 | Trace-8, Marker-6 |
| B | 24 | Expert Construct (Armor, +1 Attack, -1 Defense), Ripper-Bod 7, Blaster-8 |
| B | 27 | Active Alert: government decker arrives next turn |
| B | 30 | Lethal Black IC-8, Cascading Psychotropic Black IC-9 (Judas), Shutdown |
| C | 2 | Passive Alert, Probe-7 |
| C | 5 | Trace-8 |
| C | 9 | Construct (Shield), Killer-7, Tar Baby-7 |
| C | 11 | Active Alert: government decker summoned next turn |
| C | 14 | Cascading Psychotropic Black IC-9 (toward Fort Lewis Zoo) |
| C | 17 | Party IC: Bind-rip 5, Acid-rip 5, Jam-rip 5, Mark-rip 5 |
| C | 21 | Shutdown |
"""

NOT_BUILT = """
- Lone Star PAC substation 25's unnamed night receptionist (Baser Instincts cold open) -- appears only
  as Sergeant Crocker's foil, never named.
- **Forbidden Fruit's unnamed Border Guards (19)** at Leticia and their **Jaguar Shaman**, and the
  **GMC Riverine Patrol Boat** crew -- generic Threat-rated squads, stat summaries on the Leticia row.
- **Wild Kingdom's unnamed shadowrunner extraction team** (a troll, a cigar-smoking human gunman with
  "metal eyes," and others) that pulled Dicristofaro out of JHIH in the prologue -- not this adventure's
  player characters, never named.
- **Tan Tien's security rigger** (use the Rigger Archetype, SRII p. 59), its **twelve guards** (stats on
  the Tan Tien Compound row) and its **thirty-nine mercenaries** across the locomotive chase (Ares HVAR
  assault rifles, phosphorous grenades) -- generic Threat-rated squads, not named individuals.
- **Fred's unnamed Shiawase Envirotech partner** (Baser Instincts) -- appears only alongside Fred, no
  name given.
- **The four unnamed Fort Lewis zoo handlers** who arrive mid-battle to sedate wandering animals, and
  the **Knight Errant office-park patrol** (Street Cop stats) at Parashield, Inc. -- generic squads.
- Flavor/campaign-hook mentions with no built presence: **Amalgamated Studios** (LA, produces the
  in-universe "Predator and Prey" sim series the afanc was bound for -- a title joke on the book itself),
  the **Draco Foundation** award Tan Tien is chasing, the **DIMR** and **Atlantean Foundation** as
  alternate-campaign employers, **People for the Ethical Treatment of Paranormal Animals**, Aztechnology's
  **Medicarro** medical-care division and Universal Omnitech's **DeBeers** diamond division in West
  Africa.
- Unnamed wilderness encounter sites: the Amazonian kiwi grove and campsite, the naga's ravine, the
  basilisk's clearing, the wyrd mantis pair's territory -- one-scene locations folded into the Leticia
  row and Forbidden Fruit's synopsis/timeline.
- The **Gamemastering Critters** and **Critter Powers** reference chapters (pp. 76-97): full stat blocks
  and power write-ups for every creature used across all three adventures (aardwolf, afanc, agropelter,
  anwuma bavole, asonwu, barghest, basilisk, behemoth, birdman, devil rat, ekyelebenle, enwontzane,
  gomatia, incubus, juggernaut, macareu, mami wata, martichoras, naga, piasma, saber-tooth cat,
  shadowhound, spider-beast, talis cat, thunderbird, troglodyte, wyrd mantis, wyvern/griffin and more)
  -- pure crunch, not org/location/NPC content; referenced by name from the affected rows instead.
"""

PLAY_NOTES = """
- All three adventures are fully independent -- share only the 2059 setting and the predator/prey theme
  -- and can be slotted anywhere in an existing campaign, run in any order, or split across sessions.
- Forbidden Fruit is a slow-burn horror reveal: play the first half (border tension, basilisk, naga,
  macareu) as a fairly normal exotic-locale run, then pivot hard once Sanders is infested. Nobody should
  suspect the kiwis themselves until the spider-beasts hatch on the flight home -- keep Fukuhara's and
  Sanders's warnings about not eating the fruit as red herrings pointing at the wrong threat.
- Wild Kingdom's real hook is the runners' own ignorance: they are guarding what they believe is cargo,
  and the twenty-two-day crossing (with optional Bermuda Triangle/Caribbean encounters, not built here)
  is meant to build boredom before the mami wata assault breaks it. The Dicristofaro decision at the
  climax (return him to slavery for pay, or free him and get stranded/blacklisted) has no "right" answer
  in the text -- let the runners live with whichever they pick.
- Baser Instincts should feel like a mystery, not a monster hunt: the runners are working for Lone Star
  without confirmation of it, chasing animals that are visibly *not* acting like animals (no barking,
  choreographed attacks, abandoning wounded pack-mates). Withhold the astral-entity reveal until Disball's
  zoo confrontation; even then, give the players only a glimpse (one magically active character, one
  instant) so the "lone madman" cover story the Star settles on afterward feels plausible rather than a
  cheat.
- The astral entity survives the adventure and is designed as a reusable campaign Threat -- "It will hunt
  again" is meant literally. Consider seeding a follow-up where the same possession trick turns up in
  another city, or through a different host entirely.
- Tan Tien's compound (Wild Kingdom) and Parashield's facility (Baser Instincts) both reward a
  stealth-and-legwork approach far more than a firefight: Tan Tien's paranimals hunt by smell and can be
  thrown off with strong-smelling cover and a favorable wind/temperature, while Parashield's hell hounds
  are effectively immune to physical weapons (Flame Aura + Immunity to Normal Weapons) and need lasers or
  concussive force instead.
- Karma tables are given per adventure in the source (Forbidden Fruit p. 27; Wild Kingdom p. 51 --
  mutually exclusive points for freeing vs. returning Dicristofaro; Baser Instincts p. 71) rather than
  reproduced here; use the source page references when awarding.
"""
