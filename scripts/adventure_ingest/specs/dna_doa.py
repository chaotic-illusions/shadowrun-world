# DNA/DOA (FASA 7301, 1989) -- campaign order #3. Set in the Tacoma district, December 2050.
# Source text: docs/Adventures/text/Shadowrun 1e - DNA-DOA {FASA7301}.txt (62 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "DNA/DOA"
ORDER = 3
SOURCE = "Shadowrun 1e - DNA-DOA {FASA7301}.pdf, pp. 4-62"
YEAR = "2050 (December)"

SYNOPSIS = """
**Biogene Technologies**, a mid-size San Diego genetic-engineering firm, hires the runners through its
Seattle Special Operations man **Jason Walker** (over dinner at the Eye of the Needle, weapons checked
with Cripps the elven maitre d') for a datasteal on **Aztechnology's Tacoma Research Park**: grab the
Metavirus data file and a sample of the viral vector from the underground Beta Section and deliver
them to the container ship *S.S. Misha* at Wharf 114 before dawn. Aztechnology is about to move the
research to Aztlan, so the run is tonight. Pay is 120,000 nuyen for the team, 60,000 up front, plus
a van of AK-97s, chemsuits, C-4 and two canisters of the catalyst that turns the facility's
Plastisteel-7 wall into bubble gum.

Nothing is what it seems. The Metavirus (Dr. **Carol Owens**' work, meant to control the Metagene
for good) has been weaponized by Dr. **Simon Peterhoff** into animal/human force-breeds -- Wolf,
Tiger and Bear Sapiens -- using Orks kidnapped from the Tacoma sewers as raw material. Twenty-four
hours before the run an aerosol, self-mutating Metavirus IV got loose in Beta Section; Aztechnology
sealed Alpha and Beta, threw Owens in a cell on Peterhoff's say-so, and is watching the survivors
eat each other as a "survivability test" through the astral eyes of apprentice mage **William
Blount**. The runners crawl into a charnel house: virus-warped technicians, giant cockroaches, flesh
worms, an infected troll, and Peterhoff himself, insane and living in the ventilation ducts.

Meanwhile the **Hands of Five** -- the Tacoma chapter of the anti-metahuman terror group **Alamos
20,000** -- have a traitor inside Biogene (Walker's assistant **Wendell Holmes**), have kidnapped a
loved one of one of the runners to blackmail the data out of them (the optional traitor subplot), and
have killed the Biogene contact on the *Misha*. At the docks the Alamos ambush collides with a full
Aztechnology Response and Pursuit Team, and the team flees into one of the warehouses where Alamos
burned thousands of metahumans on the Night of Rage eleven years ago -- and finds Ork children.

Their babysitter **Jenny Hernandez** leads them to **Wilhem Park**, a shopping mall buried by the
2017 Tacoma eruptions and now the hidden home of 400 Orks and their families under "mayor" **Allan
Bronston**. Bronston wants the Orks Aztechnology kidnapped from the sewers rescued from Alpha Section,
and Carol Owens -- his old lab colleague, "The Tailor" -- brought to him. The second raid frees the Ork
women and children and Owens, then Bronston confronts Owens over what she let Aztechnology do,
trades the Alamos hostage (his Orks rescued it) and hands over a Biogene safe-house address.

The safe house is a trap: Holmes routed the message to the Hands of Five, who arrive with Martin
Honnicker to take hostages, followed by an Aztechnology team under Jacob Barre. Walker finally shows
with the money: 30,000 for the sample, 30,000 for the file, 50,000 more for Owens. Afterwards
Aztechnology and Alamos 20,000 both want the runners' blood, Biogene keeps them at arm's length, and
nobody sane will hire them for a month or two -- but to those who know, they are the runners who
burned Aztechnology.
"""

TIMELINE = """
- **February 7, 2039** -- the Night of Rage. Humanis rally in Tacoma; the Metroplex Guard "deplaces"
  metahumans to the docks for the liner *Asian Princess*; the warehouses burn; Tacoma's downtown is
  gutted; survivors found Wilhem Park in the sewers. Prologue "Into the Flames", pp.4-6.
- **The morning** (traitor subplot) -- a Hands of Five Mr. Johnson meets the traitor on the monorail
  and hands over a Ronnie Bean homing device; two hired samurai rough up anyone who follows.
- **Evening** -- Holmes collects the team from the CBI; dinner at the Eye of the Needle; Walker's
  briefing; gear van; sewer entry about a kilometer from the facility.
- **Night** -- Beta Section (viral accident 24 hours old). Blount spots them astrally (2D6 <= 4 each
  turn); an Aztech Response Team deploys into the sewers too late.
- **Before dawn** -- Wharf 114: Alamos ambush on the *S.S. Misha*, Aztechnology Response and Pursuit
  Team arrives in force; escape into the Night of Rage warehouse; Jenny; Wilhem Park.
- **Next day** -- Alpha Section raid (systems junction box; guards from the elevator 2D6+2 turns after
  the alarm, +3 every four turns; Wage Mage 3D6+2 turns; Corporate Decker 2D6+2 turns). Bronston
  vs Owens. Biogene safe house in the Puyallup Barrens: Hands of Five, then Aztechnology.
- **Monday, December 12, 2050** -- Seattle News-Intelligencer: Lone Star accuses Aztechnology of
  military maneuvers at the Tacoma docks; an Ares Dragon crashes at the Seattle Pyramid; Owens named
  Biogene head of Biotechnology Research (success) or Aztechnology absorbs Biogene and Tacoma sewer
  deaths are up 300 percent (failure).
"""

ORGS = [
    {
        "name": "Biogene Technologies",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "San Diego, California Free State (Seattle branch downtown)",
        "summary": "Mid-size genetech firm sponsoring the run; guarded by Knight Errant; rises or is absorbed by Aztechnology",
        "description": (
            "A decade-old biotechnology and genetic-engineering company that rose from the ashes of three "
            "San Diego biotech firms that failed in the same period, and reported gross profits of over a "
            "billion nuyen in its last fiscal year. President/CEO Dr. Jarred Leiji. Divisions: Biogene "
            "Research (pure scientific research in biotechnology and genetic engineering, head Randolph "
            "Cooper) and Biogene Pharmaceuticals (medically restricted and consumer pharmaceuticals, head "
            "Kristen Long). Known as an organization quick to recognize its own shortcomings and aggressive "
            "at correcting them. Biogene has no security or military forces of its own; every Biogene "
            "facility is protected by Knight Errant of Detroit."
        ),
        "leadership": [
            {"name": "Dr. Jarred Leiji", "title": "President/CEO", "notes": None},
            {"name": "Randolph Cooper", "title": "Division Head, Biogene Research", "notes": None},
            {"name": "Kristen Long", "title": "Division Head, Biogene Pharmaceuticals", "notes": None},
            {"name": "Jason Walker", "title": "Assistant Director of Special Operations, Seattle branch", "notes": "The runners' Mr. Johnson in DNA/DOA."},
        ],
        "notes": (
            "Sponsor of the DNA/DOA run against Aztechnology's Tacoma Research Park: a simultaneous hit "
            "by the runners on the lab and by a hidden Biogene agent on the backup-file site. Offered "
            "120,000 nuyen (60,000 up front), a gear van, and pre-generated operatives (Johnny Clean, "
            "Louise Frost, Andrew Shalene) at full shares. Walker's assistant Wendell Holmes was an Alamos "
            "20,000 (Hands of Five) informant, which is how the drop on the S.S. Misha was ambushed. "
            "Success ending: Dr. Carol Owens becomes Biogene's head of Biotechnology Research and "
            "Aztechnology/Biogene hostility keeps both busy for a while; Biogene keeps the runners at arm's "
            "length. Failure ending: Aztechnology absorbs Biogene outright."
        ),
        "allies": ["Knight Errant Security Services"],
        "enemies": ["Aztechnology"],
    },
    {
        "name": "Alamos 20,000",
        "org_type": "terrorist organization",
        "tier": 3,
        "headquarters": "Underground, nationwide; Seattle presence through the Tacoma chapter (Hands of Five)",
        "summary": "Violent anti-metahuman terror network behind the Night of Rage; political front is the Humanis Policlub",
        "description": (
            "The infamous anti-metahuman terrorist organization. Its leaders are violently opposed to "
            "genetic mutation of the human race or any other species; on February 7, 2039 -- the Night of "
            "Rage -- Alamos 20,000 corralled and burned thousands of metahumans in the Tacoma dock "
            "warehouses. Recent media investigations have revealed that most Alamos members are Humanis "
            "Policlub members; Humanis' international headquarters in Philadelphia denounces the reports "
            "(\"We wonder just how many mass-murderers or serial killers are registered "
            "Arch-Conservatives\"). Members act hooded, in urban fatigues and combat gear with Alamos "
            "20,000 arm-bands."
        ),
        "notes": (
            "Wanted the Metavirus as a tool to purify the human race: inject fertilized metahuman eggs to "
            "turn them human and wipe out every metahuman species within a generation, then have Humanis "
            "lobby to legalize a variant as a treatment for \"unfortunate genetic damage during "
            "pregnancy\". After DNA/DOA Alamos knows the runners' identities but is driven further "
            "underground in Seattle for a short time; expect vengeance to wind down over a month or two. "
            "Rank and file: Humanis Policlub Member stat block (DNA/DOA p.56), armor clothing, Uzi III or "
            "Remington 750 sporting rifle. The Hands of Five salute is arms crossed over the chest."
        ),
        "allies": ["Humanis Policlub"],
        "enemies": ["Wilhem Park Enclave"],
    },
    {
        "name": "Hands of Five",
        "org_type": "terrorist cell",
        "tier": 2,
        "headquarters": "Tacoma",
        "summary": "Tacoma chapter of Alamos 20,000 under Martin Honnicker; kidnappers, blackmailers, ambushers",
        "description": (
            "The Tacoma chapter of Alamos 20,000, a notorious faction believed responsible for numerous "
            "terrorist acts against metahumans over the years -- some Metroplex Guardsmen were flashing "
            "its crossed-arms salute on the Night of Rage. Led by the charismatic fanatic Martin Honnicker, "
            "who is almost single-handedly responsible for the chapter's success in Seattle; field "
            "leaders Claude Pierce, Terry Carey and Daniel Sinclair."
        ),
        "leadership": [
            {"name": "Martin Honnicker", "title": "Leader", "notes": "Personally responsible for 20+ metahuman deaths in two years."},
            {"name": "Claude Pierce", "title": "Field leader", "notes": "Merc archetype; smart AK-97."},
            {"name": "Terry Carey", "title": "Field leader", "notes": "Merc archetype; Enfield AS7."},
            {"name": "Daniel Sinclair", "title": "Field leader", "notes": "Corporate Security Guard archetype; Uzi III."},
        ],
        "notes": (
            "Learned of the Metavirus and Biogene's plan through Wendell Holmes; too short of time and "
            "ignorant of the facility's location to raid it themselves, so they kidnapped a runner's loved "
            "one (held in a storm-drain maintenance room near Wilhem Park until Bronston's Orks rescued "
            "the hostage), tagged the traitor with a Ronnie Bean, killed the Biogene contact on the S.S. "
            "Misha, and ambushed the drop. Their ambush team was almost certainly wiped out to a man by "
            "the Aztechnology Response Team. Honnicker survives to spring the safe-house trap with two of "
            "the three Misha leaders and three hooded members."
        ),
        "allies": ["Alamos 20,000", "Humanis Policlub"],
        "enemies": ["Wilhem Park Enclave", "Biogene Technologies"],
    },
    {
        "name": "Wilhem Park Enclave",
        "org_type": "community",
        "tier": 2,
        "headquarters": "Wilhem Park, a buried shopping mall under a Tacoma condoplex",
        "summary": "~400 Orks and their human kin living in a buried mall since the Night of Rage; 'mayor' Allan Bronston",
        "description": (
            "The hidden community of Orks who escaped the burning Tacoma warehouses on the Night of Rage "
            "(February 7, 2039) through the sewers and found the shopping mall entombed by the 2017 "
            "Tacoma eruptions. Close to 400 men, women and children, mostly Ork with some human offspring "
            "of the older Orks, governed by a council of elders whose \"mayor\" is Allan Bronston. They "
            "are civilized, literate and family-minded -- they read the same data-faxes and watch the "
            "same Urban Brawl as anyone up top -- and maintain almost no contact with the outside world "
            "beyond keeping informed. Any who reach adulthood may leave on condition they never reveal "
            "the enclave's existence or location."
        ),
        "leadership": [
            {"name": "Allan Bronston", "title": "\"Mayor\" / elder", "notes": "Night of Rage survivor; ex-lab assistant to Carol Owens."},
        ],
        "notes": (
            "Their calm was shattered in the past year by Aztechnology's Tacoma Research Park sending "
            "\"specimen sweeps\" into the sewers for test subjects; a group of two Ork women and four "
            "children was taken just before the viral accident. Aztechnology suspects an underground Ork "
            "colony exists but has not found it; the enclave's great fear is discovery and eviction. "
            "Bronston keeps Ork scouts in the tunnels (they shadowed the runners from the first sewer "
            "entry), can seal passages behind visitors, and can arm friends with about 30 rounds each of "
            "normal ammo up to assault-rifle caliber. Fighting them means at least 20 adult Ork males "
            "(Ork Mercenary archetype). Runners who killed Ork children are held as virtual prisoners "
            "until they redeem themselves."
        ),
        "enemies": ["Aztechnology", "Alamos 20,000", "Hands of Five"],
    },
]

LOCATIONS = [
    {
        "name": "Aztechnology Tacoma Research Park",
        "location_type": "research lab",
        "district": "Tacoma",
        "security_level": "Corporate Extraterritorial",
        "controlling_org": "Aztechnology",
        "summary": "12-building corporate campus with a 20 m pyramid; Metavirus labs (Alpha/Beta) underground behind a Plastisteel-7 wall",
        "description": (
            "A twelve-building industrial park, every building twelve stories high, laid out in concentric "
            "circles facing inward on a landscaped open area dominated by a 20-meter replica of an Aztec "
            "pyramid. The adjacent parking lot holds 8,000 vehicles. Publicly the site of microtronic, "
            "computer and biological research; considered very securely protected, with many sublevels "
            "below ground. Rumor in the science community says it does bioweapon research and that the "
            "two best minds in genetic engineering, Dr. Carol Owens and Dr. Simon Peterhoff, work there "
            "and do not get along. Aztechnology executives recently flew up from Aztlan to the Seattle "
            "Pyramid and shuttled here."
        ),
        "notes": (
            "The Metagene Project's Alpha and Beta Sections are underground, ringed by a 30 cm "
            "Plastisteel-7 wall (Barrier 35; Biogene's aerosol catalyst turns a 4x4 m patch to bubble gum "
            "for an hour) a meter or so from the abandoned Tacoma sewers; ventilation ducts run just inside. "
            "Beta Section (map pp.20-26): entrance hall with sealed Alpha access door, auditorium (giant "
            "cockroaches), lounge, meeting room (Dr. Perkins, Tiger variant; his green pass opens the "
            "Biotech pressure door), analysis room (three virus-rotted technicians), hallway with flesh "
            "worms and two half-eaten guards, observation area (infected troll in cell D; 20 Mp chip with "
            "Data File One), guard office (three terrified guards), holding-cell corridor, "
            "analysis/experimentation area (Peterhoff, two infected Ork guards, the data store holding "
            "the 150 Mp Metavirus file -- Electronics 3 to wire a deck to it), examination room, and the "
            "vault (Maglock 6, Barrier 10: six dishes of Viral Strain I plus 30,000 nuyen of data chips). "
            "Random encounters: Tiger/Wolf/Bear Sapiens, giant millipedes. Alpha Section (map pp.33-38): "
            "guard quarters, storeroom, stainless-steel hallway with cameras every 10 m, auditorium, "
            "meeting room (elite bodyguard with attack dog), dog kennel office, Sanchez's office, guard "
            "lounge, two isolation labs (Maglock 7) with suicide/gunshot victims, examination room, dead "
            "elevator, Main Security (Samuel Silver, two guards, three technicians; monitors; Beta door "
            "control behind Maglock 5 that trips biohazard klaxons), detention cells (Ork women and "
            "children in 14, Owens in 16). Doors Maglock 4 unless noted. A systems junction box in the "
            "wall kills Alpha's security and elevator controls (Electronics 5 to do it silently). "
            "Reinforcements: five guards by elevator 2D6+2 turns after the alarm, three more every four "
            "turns, a Wage Mage astrally 3D6+2 turns, a Corporate Decker 2D6+2 turns. Astral: three Rating "
            "8 Earth Elementals underground, pairs of Rating 8 Fire and Air Elementals above, doubling "
            "after four turns; William Blount surveys Beta astrally. Matrix: see the prep doc."
        ),
    },
    {
        "name": "Old Tacoma Sewers",
        "location_type": "sewer system",
        "district": "Tacoma",
        "security_level": "No Security / Barrens",
        "summary": "Abandoned 30 years; ghouls, squatters, sewer Orks, gangs, the odd vampire; the way into the Research Park",
        "description": (
            "The old Tacoma sewer network, abandoned about 30 years ago when a new storm system replaced "
            "it. Still catches run-off and overflow, but mostly it collects debris -- natural, human and "
            "otherwise. Damp walls of evil muck, dry stretches and knee-deep stretches, a smell like many "
            "things have died down here. Or will. Pitch black without a light (low-light eyes do not help). "
            "Cave-ins make the route less direct than any map; manholes to the street at half of all "
            "intersections."
        ),
        "notes": (
            "Encounter check per section (2D6, 9+), then 3D6 on the Sewer Encounter Table: rabid cat or "
            "dog, bats, 1-6 ghouls, street gangers (leader may be a samurai or mage), squatters (with a "
            "concealed street archetype now and then), harmless sewer-dwelling Orks (no connection to "
            "Wilhem Park), dwarfs, ghosts, rats, a vampire on 18. Skin contact produces rashes over 80% of "
            "the body 1D6 days after the adventure -- let the players blame the Aztech labs. Entry point: "
            "a rusted grating behind the buildings of a Tacoma industrial park about a kilometer from the "
            "facility. Wilhem Park's Orks keep their own, cleaner, forgotten section swept and watched, "
            "with a false cave-in as the door."
        ),
    },
    {
        "name": "Wilhem Park",
        "location_type": "subterranean community",
        "district": "Tacoma",
        "security_level": "Low Security",
        "controlling_org": "Wilhem Park Enclave",
        "summary": "Shopping mall buried by the 2017 eruptions, now a gas-lit Ork town of 400 under a condoplex",
        "description": (
            "A former enclosed shopping mall buried under ash and rubble by the Tacoma volcano eruptions of "
            "2017, written off as a total loss and entombed with a modern block of condoplexes built "
            "directly above. Reached through a hidden opening in a collapsed tunnel. Inside, dozens of "
            "small gas lamps flicker over Ork children playing in a still-working multi-level waterfall; "
            "the upper level's rows of stores are homes and hydroponic farms, the lower level has a "
            "restaurant where Orks and humans cook enormous meals together, and a bookstore with "
            "preserved volumes where the elders tell the story of the night Tacoma burned."
        ),
        "notes": (
            "Not self-supporting: small meat animals bred in a former department store on nutri-grain "
            "from the hydroponics; light from gas lines illicitly tapped into a nearby main. Two known "
            "entrances -- the false cave-in and the Night of Rage warehouse -- plus escape tunnels "
            "Bronston can seal. The enclave will hustle visitors out by another route the moment a scout "
            "reports masked gunmen (Alamos, tracking the Ronnie Bean) in the tunnels. If Owens is kept "
            "here as penance she teaches the Ork children."
        ),
    },
    {
        "name": "Night of Rage Warehouses",
        "location_type": "ruins",
        "district": "Tacoma (docks)",
        "security_level": "No Security / Barrens",
        "controlling_org": "Wilhem Park Enclave",
        "summary": "Burned-out metahuman holding pens from 2039; a hidden, forbidden back door to Wilhem Park",
        "description": (
            "The row of old, burned-out warehouses along the Tacoma docks where Alamos 20,000 corralled and "
            "burned thousands of metahumans on the Night of Rage, February 7, 2039. Blackened by flame and "
            "age, rusted doors, collapsed wall sections. Long abandoned."
        ),
        "notes": (
            "One of them is a rarely used, hidden entranceway to the Wilhem Park tunnels and a favorite "
            "forbidden play area for Ork children (two are watching the dockside firefight from a window "
            "when the runners crash in). Whether the team shoots those children sets the tone for the rest "
            "of the adventure. Jenny Hernandez comes out of the tunnel mouth to fetch them. The drainage "
            "tunnel Allan Bronston fell through in 2039 is under one of these floors."
        ),
    },
    {
        "name": "Tacoma Docks (Wharf 114)",
        "location_type": "transportation hub",
        "district": "Tacoma",
        "security_level": "Patrolled / Commercial",
        "summary": "Container wharf; the S.S. Misha drop point; the Alamos-vs-Aztechnology battleground",
        "description": (
            "The Tacoma container docks, security gates and all. Wharf 114 is where the rusty old container "
            "ship S.S. Misha ties up, a stone's throw from the burned-out Night of Rage warehouses."
        ),
        "notes": (
            "Biogene bought the gates open and the guards absent for the night. Alamos 20,000 took the Misha, "
            "killed the tall thin black-haired Elf contact (pass-phrase: \"Is the sky still blue?\" / \"It "
            "hasn't been since I was a child\") and replaced him with a lookalike who does not know the "
            "phrases. Claude Pierce, Terry Carey, Daniel Sinclair and 1D6+2 Alamos members wait on deck; "
            "then Captain H.C. Strum's Aztechnology Response and Pursuit Team arrives by the dozen vehicle "
            "and helicopter and opens fire on everyone, and vanloads of Alamos supporters pile in. About a "
            "million nuyen of damage; Lone Star publicly calls it military maneuvers."
        ),
    },
    {
        "name": "The Corporate Bums and Indigents Club",
        "location_type": "bar",
        "district": "Seattle (runner turf)",
        "security_level": "Low Security",
        "summary": "'The CBI' -- the runners' hangout where Holmes finds them",
        "description": (
            "Informally known as The CBI. A shadowrunner hangout where a nervous sarariman can walk up to "
            "your table with an invitation to a private dinner from Mr. Johnson -- no heavy weapons, please."
        ),
        "notes": "Where DNA/DOA begins. Good default 'where the team drinks' if the campaign needs one.",
    },
    {
        "name": "Biogene Safe House (Puyallup)",
        "location_type": "safehouse",
        "district": "Puyallup Barrens (edge)",
        "security_level": "No Security / Barrens",
        "controlling_org": "Biogene Technologies",
        "summary": "A house a few streets from a sewer sump; the Not-So-Safe House where Alamos and Aztechnology converge",
        "description": (
            "A house a few streets from a sump on the edge of the Puyallup Barrens, through ruined buildings "
            "and abandoned lots. A living area on the first floor with several small side rooms."
        ),
        "notes": (
            "Bronston's message to Biogene went through Wendell Holmes, so the Hands of Five (Honnicker, "
            "two of the Misha leaders, three hooded members) are deployed in the side rooms waiting for a "
            "hostage, and Holmes himself waves from the window as a familiar face. Then Jacob Barre and "
            "Eduardo Eman arrive in two up-armored Ford Americars with six troopers. Optionally Walker "
            "rides to the rescue with six Knight Errant troopers. Burned after the adventure."
        ),
    },
]

NPCS = [
    {
        "name": "Jason Walker",
        "role": "Biogene's Seattle Special Ops man; the runners' by-the-book Mr. Johnson",
        "archetype": "Mr. Johnson",
        "title": "Assistant Director of Special Operations, Biogene Technologies (Seattle)",
        "race": "Human",
        "gender": "Male",
        "organization": "Biogene Technologies",
        "connection": 3,
        "description": (
            "An experienced contact agent who until now has run only low-level industrial espionage and "
            "surveillance shadowruns; this run is his entry into the big leagues. Careful to do everything "
            "by the book, which sometimes makes him look like a neophyte. Never lies to the runners, never "
            "names himself, Holmes, or Biogene -- but his information about the Aztechnology facility is "
            "dangerously out of date."
        ),
        "background": (
            "Judges a team by how they handle themselves in the car and at the Eye of the Needle, and sets "
            "the fee accordingly. Does not suspect his assistant Holmes is an Alamos traitor; when he "
            "learns it he feels hurt, betrayed, and angry enough to kill."
        ),
        "notes": (
            "Refusing him means \"This is Johnson. Dispatch Team Two\" and the offer is gone. Pays the "
            "balance at the safe house: 30,000 for the intact sample (5,000 damaged), 30,000 for the file, "
            "50,000 for Owens; more only through Negotiation. Afterwards wants nothing to do with the "
            "runners and tells them to leave town. (The cast list spells him John Walker.) Stats: B3 Q3 S2 "
            "C4 I6 W5, Ess 3.8; Etiquette (Corporate) 8, Psychology 8, Negotiation 6, Computer Theory 5, "
            "Firearms 2; datajack with 200 Mp; armor vest, Beretta 101T with laser sight."
        ),
        "contact_skills": ["Biogene corporate jobs and payment", "Knight Errant strike team (through Biogene)"],
    },
    {
        "name": "Wendell Holmes",
        "role": "Walker's assistant and the Alamos 20,000 informant inside Biogene",
        "archetype": "Corporate Wage Slave",
        "title": "Assistant to Jason Walker, Biogene Technologies (Seattle); Hands of Five informant",
        "race": "Human",
        "gender": "Male",
        "organization": "Biogene Technologies",
        "connection": 1,
        "description": (
            "A nervous-looking sarariman with large round eyes that dart from the mirror to the road when "
            "he drives. Likes to think he is only reluctantly a traitor -- that the Hands of Five are "
            "forcing him by threatening to expose his ties. Almost believes it."
        ),
        "background": (
            "Drifted into the Hands of Five through a former girlfriend's Humanis rallies; exposure to "
            "Martin Honnicker sealed it. Naive enough to imagine his betrayal will not end in violence."
        ),
        "notes": (
            "Collects the team from the CBI, drives the gear van to the sewer grating, and is gone (keys in "
            "the sun visor) when they come out. Routes Bronston's message to the Hands, then waits at the "
            "safe house as the familiar face in the window. If he survives, Walker wants him dead; Knight "
            "Errant troopers take him into custody if they are present. Stats: B2 Q2 S4 C2 I3 W1, Ess "
            "4.8; Computer 3, Etiquette (Corporate) 4, Japanese 2; datajack, 100 Mp memory; armor vest."
        ),
    },
    {
        "name": "Dr. Carol Owens",
        "role": "'The Tailor' -- designer of the Metavirus; imprisoned by Aztechnology; Biogene's prize",
        "archetype": "Corporate Scientist",
        "title": "Metagene Project Coordinator, Aztechnology Tacoma facility (later Biogene head of Biotechnology Research)",
        "race": "Human",
        "gender": "Female",
        "organization": "Aztechnology",
        "connection": 2,
        "description": (
            "A haggard, frail-looking woman in the tattered remains of a lab coat when found in detention "
            "cell 16 (\"I won't fall for any of your stupid tricks, Peterhoff!\"). A brilliant bioengineer "
            "with Intelligence 7 and Genetic Engineering 8 who suffers from not always seeing the "
            "consequences of her work."
        ),
        "background": (
            "Received her doctorate in bioengineering while working at a small Seattle genetics lab where "
            "Allan Bronston was her assistant; her theory of the Metagene's origin and its control was "
            "meant to save the next generation of \"lost children\" from goblinization. When a South "
            "American currency devaluation bankrupted the lab she took Aztechnology's long-standing offer "
            "over Bronston's pleas. She forced herself to stay blind to her employer until Peterhoff was "
            "put on the project; her protests got Jorge Sanchez sent in to intimidate her team, and after "
            "the viral accident Peterhoff's ravings got her locked up."
        ),
        "notes": (
            "Will not leave Alpha without the viral sample (she knows the Alpha/Beta door code; using it "
            "trips the alarms). Accepts Biogene's offer because she believes its people are trustworthy. "
            "Bronston's confrontation (\"Would you like me to rattle off the mapping codes for the Metagene "
            "spiral, Carol?\") is the emotional climax; if he stays unconvinced he keeps her at Wilhem Park "
            "as penance, teaching Ork children. Her extract of the master file (Handout p.61) supports her "
            "version. Stats: B2 Q3 S2 C4 I7 W4, Ess 4.6; Biology 6, Biotech 4, Genetic Engineering 8, "
            "Computer 3; datajack, 100 Mp headware memory with display link."
        ),
        "contact_skills": ["World-class genetic engineering / Metagene research"],
    },
    {
        "name": "Dr. Simon Peterhoff",
        "role": "Metagene Applications director gone insane; breeds Wolf/Tiger/Bear Sapiens from kidnapped Orks",
        "archetype": "Corporate Scientist",
        "title": "Metagene Applications Project Director, Aztechnology Tacoma facility",
        "race": "Human",
        "gender": "Male",
        "organization": "Aztechnology",
        "connection": 1,
        "description": (
            "Found cowering in an observation cell or dodging madly through the debris toward the nearest "
            "ventilation duct, which has become his favorite way around Beta Section because the loose "
            "critters have not discovered it. Babbles incessantly, switching from incomprehensible biotech "
            "speak to the baby-talk he uses on his creations. Utterly insane."
        ),
        "background": (
            "Brought in by Aztechnology to develop alternatives to Owens' Metagene virus; his gene-splicing "
            "force-breeds (Wolf Sapiens WS104, Tiger Sapiens TS64, Bear Sapiens BS261) used Orks kidnapped "
            "from the Tacoma sewers as raw genetic material, with funding from Emilio K. in Weapons. Ran "
            "Alpha and Beta like his private facility; called Owens \"The Tailor\" and got her jailed by "
            "blaming the accident on her."
        ),
        "notes": (
            "Believes the accident was a terrorist plot by Owens. Knows the spill was an aerosol-vectored, "
            "self-mutating Metavirus IV variant but not that the virus is now long dead. Two virus-infected "
            "Ork guards act as his personal guard and defend him at any cost. Aztechnology no longer cares "
            "about him -- his part of the work is done. Stats: B2 Q3 S2 C2 I7 W1, Ess 5.8; Biology 5, "
            "Biotech 5, Genetic Engineering 7; datajack."
        ),
    },
    {
        "name": "Allan Bronston",
        "role": "'Mayor' of Wilhem Park; Night of Rage survivor; Owens' former lab assistant",
        "archetype": "Community Leader",
        "title": "\"Mayor\" and elder of the Wilhem Park Ork enclave",
        "race": "Ork",
        "gender": "Male",
        "age": 28,
        "organization": "Wilhem Park Enclave",
        "connection": 4,
        "description": (
            "A hulking Ork of 28 whose hair is already graying and whose face shows the wrinkling of a "
            "human of sixty. He tells the enclave's young the story of the night Tacoma burned from a "
            "large chair in the buried bookstore. Proud: \"Not afraid. Different, but never, never afraid.\""
        ),
        "background": (
            "Goblinized as a boy; on February 7, 2039 his family was dragged from their Tacoma home by "
            "chemsuited inspectors and the Metroplex Guard, marched to the docks for the liner Asian "
            "Princess, and split up in the warehouse that burned. He fell through a floor grate into a "
            "drainage tunnel, shot the guard who found him, and never saw his family again. One of the "
            "first Orks in the buried mall, he found The Metahuman Connection in the ruined bookstore, "
            "left to work as a lab assistant under Carol Owens, absorbed a full bio-education in a few "
            "years, and returned to Wilhem Park when the lab went bankrupt and Aztechnology took only "
            "Owens."
        ),
        "notes": (
            "Friendly if the runners spared the Ork children, hostile (and holding them prisoner) if not; "
            "either way he uses them to raid Alpha Section for the kidnapped Orks and for Owens, whom he "
            "wants to confront personally. Hides that his Orks are watching the Hands of Five hostage; "
            "rescues it during the Alpha raid as a bargaining chip. Fears both discovery and Aztechnology's "
            "retribution; still hopes the virus can save his people. Stats: B6 Q5 S6 C2 I3 W5, Ess 5.8; "
            "Biology 3, Genetic Engineering 2, Leadership 4, Throwing Weapons 5; datajack; Beretta 101T "
            "with exploding bullets, four throwing knives, 100 Mp pocket computer."
        ),
        "contact_skills": [
            "Wilhem Park enclave: shelter, guides through the Tacoma sewers, Ork muscle",
            "Basic genetics / biology (lab-trained)",
            "Message relay to Biogene",
        ],
    },
    {
        "name": "Jenny Hernandez",
        "role": "Human metahuman-rights activist who babysits Wilhem Park's children and guides the team in",
        "archetype": "Political Activist",
        "title": "Metahuman-rights activist living in Wilhem Park",
        "race": "Human",
        "gender": "Female",
        "organization": "Wilhem Park Enclave",
        "connection": 2,
        "description": (
            "A human who lives among the Orks of Wilhem Park and minds their children. Bursts out of the "
            "hidden tunnel in the Night of Rage warehouse to retrieve two straying Ork kids -- cursing "
            "violently if the runners have shot them. Says little on the walk down: \"You'll have to ask "
            "Allan.\""
        ),
        "notes": "No stats in the source (use the Squatter or Political Activist profile). Promises to guide the team out of the sewers and takes them to Wilhem Park instead.",
    },
    {
        "name": "Martin Honnicker",
        "role": "Charismatic fanatic leading the Hands of Five; 20+ metahuman deaths",
        "archetype": "Terrorist Leader",
        "title": "Leader of the Hands of Five (Alamos 20,000, Tacoma)",
        "race": "Human",
        "gender": "Male",
        "organization": "Hands of Five",
        "connection": 1,
        "description": (
            "A tall, lanky man whose long face is framed by a mop of dark hair, so charismatic that he is "
            "almost single-handedly responsible for the Hands of Five's success in Seattle. Speaks to "
            "metahumans only in a derisive, condescending manner."
        ),
        "background": (
            "A true fanatic, personally responsible for more than 20 metahuman deaths in the last two years. "
            "Attributes his hatred to the unsubstantiated belief that an Elven biker gang murdered his baby "
            "sister; a perceptive psychologist would call it a repressed, desperate wish to be metahuman."
        ),
        "notes": (
            "At the safe house he sincerely tries to keep things non-violent -- if the team is mostly "
            "non-Awakened humans -- and takes hostages rather than lives, but resorts to force when he must. "
            "His death would be an enormous blow to the organization. Stats: B3 Q3 S4 C6 I4 W4, Ess 3.8, "
            "Reaction 3(5); Etiquette (Street) 5, Firearms 5, Leadership 4, Persuasion 4; smartgun link, "
            "Wired Reflexes 1; AK-97 with smartgun link (3 clips), lined coat."
        ),
    },
    {
        "name": "Claude Pierce",
        "role": "Alamos-Tacoma field leader at the Misha ambush",
        "archetype": "Mercenary",
        "title": "Field leader, Hands of Five",
        "race": "Human",
        "gender": "Male",
        "organization": "Hands of Five",
        "connection": 1,
        "description": "Masked, in urban fatigues with an Alamos 20,000 arm-band, on the deck of the S.S. Misha.",
        "notes": "Merc archetype. Smart AK-97 (6 clips), smart Fichetti Security 500 (2 clips), armor clothing. Likely killed by the Aztechnology Response Team; the GM picks which two of the three Misha leaders survive to the safe house.",
    },
    {
        "name": "Terry Carey",
        "role": "Alamos-Tacoma field leader at the Misha ambush",
        "archetype": "Mercenary",
        "title": "Field leader, Hands of Five",
        "race": "Human",
        "gender": "Male",
        "organization": "Hands of Five",
        "connection": 1,
        "description": "Masked, in urban fatigues with an Alamos 20,000 arm-band, on the deck of the S.S. Misha.",
        "notes": "Merc archetype, no smartgun link. Enfield AS7 (2 clips), Beretta 101T (3 clips), armor clothing.",
    },
    {
        "name": "Daniel Sinclair",
        "role": "Alamos-Tacoma field leader at the Misha ambush",
        "archetype": "Corporate Security Guard",
        "title": "Field leader, Hands of Five",
        "race": "Human",
        "gender": "Male",
        "organization": "Hands of Five",
        "connection": 1,
        "description": "Masked, in urban fatigues with an Alamos 20,000 arm-band, on the deck of the S.S. Misha.",
        "notes": "Corporate Security Guard archetype. Uzi III SMG (4 clips), Ruger Super Warhawk (12 extra rounds), armor clothing.",
    },
    {
        "name": "Jorge Sanchez",
        "role": "Aztechnology 'personal efficiency expert' -- a globe-trotting enforcer who hates germs",
        "archetype": "Corporate Fixer",
        "title": "Personal efficiency expert, Aztechnology",
        "race": "Human",
        "gender": "Male",
        "organization": "Aztechnology",
        "connection": 1,
        "description": (
            "A tall, dark-skinned man in an easily 2,000-nuyen suit. A personal efficiency expert: he pays "
            "you a personal call, you get efficient. Travels armed, though the jar of bullets on his "
            "mantelpiece has not grown in recent years. Enjoys work that takes him all over the globe."
        ),
        "background": (
            "Sent by suborbital and helicopter to resolve the Peterhoff/Owens personality conflict with a "
            "ready smile, soothing words, and nice precise talk about corporate responsibility. Then came "
            "the viral spill, and he discovered how much he hates germs. Furious at being sealed into Alpha "
            "Section and terrified of contamination; ordered Owens into detention on Peterhoff's word."
        ),
        "notes": (
            "In office 7 with Evelyn Franklin and an elite bodyguard (Merc archetype, Ares Predator). "
            "Demands to know who intruders are; a plausible excuse works (a wild-but-plausible one earns "
            "1 Karma), otherwise he draws and fires. Stats: B4 Q4 S3 C4 I3 W3, Ess 2.3, Reaction 3(7); "
            "Firearms 6, Unarmed 6, Stealth 4, Etiquette (Corporate) 4, Computer 3, Car 3, Aircraft 2; "
            "datajack, smartgun link, Wired Reflexes 2; Ares Predator w/ smartlink (2 reloads), armor "
            "vest, two Trauma Patch 5, white noise generator."
        ),
    },
    {
        "name": "Evelyn Franklin",
        "role": "Sanchez's assistant, a powerful hermetic mage with a Power Focus who watches her boss",
        "archetype": "Corporate Mage",
        "title": "Special assistant to Jorge Sanchez, Aztechnology",
        "race": "Human",
        "gender": "Female",
        "organization": "Aztechnology",
        "connection": 1,
        "description": (
            "An attractive red-haired woman thumbing through a magazine in Sanchez's office. A careful "
            "observer: she knows who to watch and how long to watch them, and right now she is watching "
            "her boss. Travels the world with him, enjoying the same contacts with the rich and powerful. "
            "Plays classical piano."
        ),
        "notes": (
            "Unconcerned about the contamination because she is sure her Cure Deadly Disease spell will "
            "handle it (it will not). Attacks alongside Sanchez. Stats: B2 Q3 S1 C4 I6 W5, Ess 6, Magic "
            "6 (9 with focus); Sorcery 6, Conjuring 6, Magical Theory 6, Etiquette (Corporate) 5; Astral "
            "pool 21. Gear: armor vest, bracelet (3-point Power Focus), ruby ring (2-point Powerball spell "
            "focus). Spells: Power Dart 5, Powerball 8, Analyze Truth 4, Antidote Serious Toxin 3, Cure "
            "Deadly Disease 3, Treat Severe Wounds 3, Entertainment 2."
        ),
    },
    {
        "name": "Samuel Silver",
        "role": "Long-time Aztechnology security mage who dreams of blending magic with bioengineering",
        "archetype": "Corporate Mage",
        "title": "Security mage, Aztechnology Tacoma Research Park",
        "race": "Human",
        "gender": "Male",
        "organization": "Aztechnology",
        "connection": 1,
        "description": (
            "A tall, dark-skinned man with slicked-back hair, in Main Security with two guards and three "
            "technicians. A dedicated professional who will guard the facility at any cost."
        ),
        "background": (
            "A long-time Aztechnology security mage recently transferred to Tacoma. Semi-professionally "
            "interested in biology since adolescence, he dreams of blending magic with bioengineering; "
            "Peterhoff ignores him, Owens listens sympathetically but lacks the magical theory to follow."
        ),
        "notes": (
            "Stats: B2 Q4 S2 C2 I6 W4, Ess 6, Magic 6, Reaction 5; Sorcery 7, Magical Theory 7, Conjuring "
            "5, Etiquette (Corporate) 5, Firearms 3, Biology 1; Astral pool 19. Gear: armor vest, Beretta "
            "101T, Rating 3 Power Focus. Spells: Mana Bolt 7, Power Bolt 5, Sleep 3, Heal Moderate Wounds "
            "3, Chaos 3. A survivor could become an unlikely contact for a team with a magician."
        ),
    },
    {
        "name": "William Blount",
        "role": "Apprentice hermetic mage astrally spying on Beta Section for Aztechnology",
        "archetype": "Corporate Mage",
        "title": "Field observer, Aztechnology parazoological research division",
        "race": "Human",
        "gender": "Male",
        "organization": "Aztechnology",
        "connection": 1,
        "description": (
            "Grew up on an Iowa farm, earned a master's in parazoological magical studies from the "
            "University of San Diego, and was recruited by Aztechnology just before graduating. Six months "
            "into the parazoology division when Tacoma called for a skilled field observer; leaped at it."
        ),
        "notes": (
            "Has spent eight hours astrally surveying Beta Section (2D6 <= 4 each turn to spot the team). "
            "Ill-suited to combat; sent back to harass a player magician astrally, targeting spirits then "
            "magic items. Cannot command the Rating 8 security elementals (not his). Stats: B2 Q2 S2 C1 I6 "
            "W5, Ess 6, Magic 6; Sorcery 5, Magical Theory 3, Parazoology 2, Psychology 2, Etiquette "
            "(Corporate) 3; Astral pool 17. Spells: Power Dart 2, Detect Life 2, Detect Life Form 3, Treat "
            "Light Wounds 2, Invisibility 1, Barrier 4."
        ),
    },
    {
        "name": "Jacob Barre",
        "role": "Aztechnology corporate enforcer who has never failed to retrieve a wayward employee",
        "archetype": "Company Man",
        "title": "Corporate enforcer, Aztechnology",
        "race": "Human",
        "gender": "Male",
        "organization": "Aztechnology",
        "connection": 1,
        "description": (
            "Aztechnology's specialist in wayward employees; takes great pride in never having failed to "
            "retrieve one. Under orders to take back the viral sample, the data file and Dr. Owens -- or "
            "see that nobody else gets them. Unconcerned with hostages, fanatics, or runners."
        ),
        "notes": (
            "Leads the safe-house strike: two Ford Americars (Body 3, Armor 1), Eman and two troopers with "
            "him, four more troopers in the second car. Fetches the assault cannon from the car only if "
            "his side is losing. Stats: B5(6) Q5(6) S6 C2 I4 W5, Ess 2.8, Reaction 5(7); Firearms 7, "
            "Unarmed 6, Gunnery 4, Car 4, Etiquette (Corporate) 4, Stealth 3; muscle replacement 1, "
            "smartgun link, Wired Reflexes 1; FN-HAR w/ smartlink (4 clips), Ruger Super Warhawk "
            "(exploding bullets), assault cannon (10 shots), partial heavy armor."
        ),
    },
    {
        "name": "Eduardo Eman",
        "role": "Street mage newly gone corporate; coarse, confrontational, Mana Bolt 7",
        "archetype": "Corporate Mage",
        "title": "Company mage, Aztechnology (newcomer)",
        "race": "Human",
        "gender": "Male",
        "organization": "Aztechnology",
        "connection": 1,
        "description": (
            "Promising street talent recently converted to the corporate line; a street veteran, much "
            "coarser than Barre and less inclined to subtlety. Confrontational in attitude and manner, but "
            "listens to Barre and takes his orders."
        ),
        "notes": (
            "Stats: B3 Q3 S2 C2 I5 W5, Ess 6, Magic 6, Reaction 4; Sorcery 6, Conjuring 6, Magical Theory "
            "5, Etiquette (Street) 5, Firearms 4; Astral pool 17. Gear: armor clothing, reusable fetishes "
            "for Mana Bolt, Uzi II SMG with laser sight. Spells: Mana Bolt 7, Powerball 5, Heal Moderate "
            "Wounds 3, Mask 3."
        ),
    },
    {
        "name": "Captain H.C. Strum",
        "role": "Commander of the Aztechnology Response and Pursuit Team that levels the Tacoma wharf",
        "archetype": "Company Man",
        "title": "Commanding Officer, Aztechnology Response and Pursuit Team (Tacoma)",
        "race": "Human",
        "gender": "Male",
        "organization": "Aztechnology",
        "connection": 1,
        "description": "Commands the dozens of armed and transport vehicles and helicopters that converge on Wharf 114 and open fire on everything on the Misha's deck.",
        "notes": (
            "Company Man archetype. Smart FN HAR (gas-vent 2, 4 clips), smart Browning Max-Power (3 "
            "clips), partial heavy armor, helmet. Second in command Lieutenant Carl Hollis (HK227 SMG, "
            "Browning Max-Power, partial heavy armor). Troopers: Aztechnology Security Guard block, HK227s, "
            "armor clothing, helmets. The team is meant to be an insurmountable foe that herds the runners "
            "into the warehouses."
        ),
    },
    {
        "name": "Cripps",
        "role": "Elven maitre d' of the Eye of the Needle; his podium hides more electronics than an office",
        "archetype": "Club Owner",
        "title": "Maitre d', Eye of the Needle restaurant (Space Needle)",
        "race": "Elf",
        "gender": "Male",
        "connection": 2,
        "description": (
            "The formal, black-clad, almost effeminate Elven maitre d' of the Eye of the Needle. His "
            "innocent-looking podium and light probably contain more electronics than a medium-sized "
            "office, and the hidden eyes watching will not tolerate violence. A fount of information that "
            "dries up after he tells you his name."
        ),
        "notes": (
            "Asks guests nicely to check any weapon the foyer sensors detect (8-dice Perception vs "
            "Concealability); arguing brings a warning, then the Needle's security team within a minute. "
            "Walker's bribes ensure Cripps and the surveillance \"forget\" who dined. Knows every "
            "high-powered mage in Seattle by sight."
        ),
        "contact_skills": ["Who dines at the Eye of the Needle (discreetly, for a price)"],
    },
    {
        "name": "Johnny Clean",
        "role": "Ex-UCAS White Lion street samurai for hire: 'Speak softly and carry a big fraggin' gun'",
        "archetype": "Street Samurai",
        "title": "Street samurai (freelance; offered by Biogene)",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "Few samurai on the streets have a rep as mean as Mr. Clean's, and fortunately he has one of "
            "the more stable personalities in the business. Prefers intimidation to force whenever "
            "possible. Motto: \"Speak softly and carry a big fraggin' gun.\""
        ),
        "background": (
            "Son of a former US Army general who stayed with the UCAS after the CAS secession and retired a "
            "two-star. A military brat, veteran of the UCAS White Lion elite unit, forced out by a "
            "personality clash with a ranking officer. Still close to elements of the UCAS military and "
            "occasionally runs shadowy special missions for them. Living and working in Seattle."
        ),
        "notes": (
            "One of three pre-generated operatives Biogene offers the team at a full share. Stats: B6(7) "
            "Q4(5) S6(7) C2 I5 W5, Ess 0, Reaction 4(8); Firearms 6, Unarmed 6, Armed 5, Stealth 4, "
            "Etiquette (Street) 4; dermal plating 1, low-light eyes, muscle replacement 1, retractable "
            "spur, smartgun link, Wired Reflexes 2; Ares Predator (exploding, smartlink), Enfield AS7 "
            "(smartlink), armor jacket, airfoil concussion and defensive grenades, thermographic goggles, "
            "wrist phone."
        ),
        "contact_skills": ["Heavy muscle and intimidation", "UCAS military back-channel"],
    },
    {
        "name": "Louise Frost",
        "role": "Half-Salish street samurai, ex-Sisters Sinister, freelance; supports her father in the Barrens",
        "archetype": "Street Samurai",
        "title": "Street samurai (freelance; offered by Biogene)",
        "race": "Human",
        "gender": "Female",
        "nationality": "Half-blood Salish",
        "connection": 3,
        "description": "A freelance samurai with a strong enough rep to make a good living; sword specialist (Armed Combat (Sword) 6), Etiquette (Street) 6.",
        "background": (
            "Moved to Seattle with her father at four so she could rise above their poverty; an "
            "uncompensated on-the-job injury put them in a run-down Redmond Barrens tenement instead. Ran "
            "with the all-female gang Sisters Sinister from 15 until a political fracture split it; went "
            "freelance on her rep. Still supports her father, who lives in the same Barrens apartment."
        ),
        "notes": (
            "Biogene operative option. Stats: B3(4) Q4(5) S2(3) C5 I5 W5, Ess 1.8, Reaction 5(7); "
            "Firearms 5, Unarmed 5, Stealth (Urban) 3, Bike 2; thermographic cybereyes, dermal plating 1, "
            "muscle replacement 1, smartgun link, Wired Reflexes 1; AK-97 SMG w/ smartlink, armor jacket, "
            "defensive airfoil grenades, Trauma Patches."
        ),
        "contact_skills": ["Redmond Barrens street connections", "Sisters Sinister alumni"],
    },
    {
        "name": "Andrew Shalene",
        "role": "Elf hermetic mage and jackless decker who lives for the rush; daylight allergy",
        "archetype": "Mage",
        "title": "Mage / decker (freelance; offered by Biogene)",
        "race": "Elf",
        "gender": "Male",
        "connection": 2,
        "description": (
            "Always first into the dark hole, through the door, or into the odd-looking processor -- he lives "
            "for the rush and so far has not paid for it. Physically repulsed by cyberware: no datajack, so "
            "he decks slow through a Sony CTY-360 terminal rig. Nuisance allergy to daylight."
        ),
        "background": (
            "Born to a wealthy Spokane family sheltered by his father's job at a Shiawase-linked computer "
            "firm in Seattle. Left in 2037 to join his \"Elven brothers\" in the new Tir Tairngire and met "
            "abuse from the back-to-nature Elves instead; learned the hermetic arts there from Tanner, an "
            "older human mage exiled from Los Angeles. Politics pushed them out; Tanner went home, Shalene "
            "went to Denver and learned decking."
        ),
        "notes": (
            "Biogene operative option. Stats: B2 Q4 S3 C1 I4 W2, Ess 6, Magic 6; Computer 4, Sorcery 4, "
            "Magical Theory 3, Conjuring 2, Firearms 3; Astral pool 14, Hacking pool 8. Gear: Beretta "
            "101T, Gold DocWagon contract, lined coat, Sony CTY-360 (Bod 4, Evasion/Masking 5, Sensors 3, "
            "Attack 3, Sleaze 4, Smoke 4, 200 Mp storage), two 1-point spell foci. Contacts: Bartender, "
            "Mr. Johnson."
        ),
        "contact_skills": ["Hermetic magic", "Decking (slow, jackless)", "Tir Tairngire experience"],
    },
]

ORG_UPDATES = {
    "Aztechnology": {
        "description_append": (
            "Corporate profile as published in 2050: home office Mexico City, Aztlan; President/CEO Juan "
            "Atzcapotzalco; Northwest Division (diversified products from armaments to electronics) under "
            "division head Salvador Ramierez. Many experts believe Aztechnology is the real power behind "
            "the government of Aztlan. It grew from a motley collection of South and Central American "
            "resource and technopirate companies in the early days of the Awakening; much of its early "
            "growth came from employing magically active staff and from ruthless industrial espionage and "
            "sabotage. The founder and his son are both said to be accomplished magicians. Maintains "
            "extensive paramilitary forces; the Northwest Division keeps elements of the Third Aztlan "
            "Legion as backup to its security teams. (Note: the source names the CEO Juan Atzcapotzalco; "
            "the existing profile lists Flavia de la Rosa.)"
        ),
        "notes_append": (
            "The Tacoma Research Park runs the Metagene Project (Dr. William Espinata, Supervisor of "
            "Genetic Systems, recently transferred from Europe; coordinator Dr. Carol Owens; applications "
            "director Dr. Simon Peterhoff, funded by \"Emilio K. in Weapons\"): a viral vector that grafts "
            "traits into a fertilized egg -- ultimately a way to manufacture metahuman subspecies. "
            "Peterhoff's Wolf/Tiger/Bear Sapiens force-breeds used Orks swept from the Tacoma sewers. "
            "The Metavirus IV accident, Alpha/Beta lockdown, and \"survivability test\" are Aztechnology's "
            "dirty secret; the research was about to move to Aztlan. The Tacoma park has no telecom "
            "connection of its own -- it works through the Seattle Pyramid's main system, 38+ security "
            "levels including the quasi-mythical Level 30 where prototype Black IC is tested; no one has "
            "run it and lived. Magical security: Rating 8 Earth/Fire/Air Elementals that strafe then attack "
            "astral intruders. After DNA/DOA Aztechnology does not know who burned them but is doing its "
            "damnedest to find out; an Ares Dragon crashed on the Seattle Pyramid grounds the same night "
            "(news handout). Enforcers Jacob Barre and Jorge Sanchez, mages Samuel Silver, Evelyn Franklin, "
            "Eduardo Eman, William Blount, and Captain H.C. Strum's Response and Pursuit Team are on file."
        ),
        "leadership_add": [
            {"name": "Juan Atzcapotzalco", "title": "President/CEO", "notes": "DNA/DOA corporate profile (2050)."},
            {"name": "Salvador Ramierez", "title": "Division Head, Aztechnology Northwest Division", "notes": "DNA/DOA corporate profile (2050)."},
            {"name": "Dr. William Espinata", "title": "Supervisor of Genetic Systems", "notes": "Recipient of the Metavirus project memos; transferred from Europe."},
        ],
        "enemies_add": ["Biogene Technologies", "Wilhem Park Enclave"],
    },
    "Knight Errant Security Services": {
        "notes_append": (
            "Holds the security contract for every Biogene Technologies facility (Biogene has no forces of "
            "its own). A Biogene/Knight Errant strike team of six troopers under Jason Walker is the "
            "optional cavalry at the DNA/DOA safe house."
        ),
    },
    "Lone Star Security": {
        "notes_append": (
            "December 2050: Lone Star publicly accused Aztechnology of staging military maneuvers with a "
            "company-sized unit, attack helicopters and urban assault vehicles at the Tacoma docks and "
            "petitioned the Seattle Corporate Council (spokesperson Elyse Sunberg); Aztechnology blamed "
            "Lone Star for the roughly one million nuyen in damage. Lone Star only stopped the Night of "
            "Rage violence in 2039 after the United Corporation Council intervened. Detective Lucas Niles "
            "tracks sewer-dweller deaths in Tacoma (up 300 percent if the Metavirus creatures got loose)."
        ),
    },
    "Humanis Policlub": {
        "notes_append": (
            "International headquarters in Philadelphia. Recent media investigations revealed that most "
            "Alamos 20,000 members are Humanis members; Humanis denounced the reports. The massive "
            "Humanis rally in Tacoma on February 7, 2039 (\"guardians of human purity\") was the spark of "
            "the Night of Rage. Alamos intended to use Humanis as the political front to legalize a "
            "Metavirus \"treatment\" for metahuman pregnancies. Wendell Holmes was recruited through "
            "Humanis rallies."
        ),
        "allies_add": ["Alamos 20,000", "Hands of Five"],
    },
    "Seattle Metroplex Guard": {
        "notes_append": (
            "On the Night of Rage (February 7, 2039) the Metroplex Guard enforced Governor Allenson's "
            "\"deplacement\" order: riot vehicles with water cannon and machine guns, thirty cops in riot "
            "gear per block, transport convoys to the Tacoma docks and the liner Asian Princess, surveillance "
            "drones over the warehouses. Some Guardsmen exchanged the Hands of Five salute. Older Orks "
            "remember."
        ),
    },
}

LOC_UPDATES = {
    "The Space Needle": {
        "notes_append": (
            "The Eye of the Needle restaurant at the very peak: eatery of choice for high-powered mages, "
            "reached from an underground garage near the old World's Fair grounds (90-degree ramp turn, "
            "Banshee-proof grates, vehicle sensors and coded keys), through plastisteel doors and a "
            "pressurized lift to a cream-carpeted foyer where Cripps, the Elven maitre d', checks weapons "
            "the foyer sensors find, then a silver-and-black elevator to intimate private dining areas "
            "with a Rating 10 white-noise generator and a Rating 8 hermetic circle built into the decor. "
            "Corporate neutral ground. Security team within one minute of any disturbance: eight guards "
            "in partial heavy armor with clubs, tasers and Uzi IIIs, a company man, a street mage and a "
            "wage mage, who neutralize rather than kill; doors seal and elevators lock down first. Biogene's "
            "Jason Walker hires runners here (DNA/DOA)."
        ),
    },
    "Aztechnology Pyramid": {
        "notes_append": (
            "The Tacoma Research Park has no telecom connection of its own and routes through the Pyramid's "
            "main system: 38+ security levels including the quasi-mythical Level 30 where prototype Black "
            "IC is tested. No one has run it and lived to tell. Aztlan executives visiting the Tacoma "
            "Metagene project stay here; an Ares Dragon transport helicopter crashed on the grounds "
            "shortly after 1:00 a.m. the night of the DNA/DOA run, last seen near the Mega-Media building."
        ),
    },
}

NPC_UPDATES = {}

MATRIX_HOSTS = """
**1. Aztechnology Tacoma -- Alpha Section system** (map DNA/DOA p.34; SR1 color-rating notation).
Isolated from the outside; reachable only from terminals inside Alpha (I/OP-1 meeting room, I/OP-2
Sanchez's office, I/OP-3 Main Security, plus the guard-quarters keyboard). A Corporate Decker defends
it 2D6+2 turns after security is alerted. Worth building as the adventure's one live host.

| Node | Function | Rating / IC |
|---|---|---|
| SAN-1 | Link to the main Aztechnology Seattle system only | Red-8, Barrier 6 |
| SAN-2 | Link to the (crashed) Beta Section system -- leads nowhere | Blue-6 |
| CPU-1 | Alpha and Beta central processor | Orange-7, Barrier 7, Trace and Burn 5 |
| DS-10 | General data storage | Green-6, Access 4 |
| SPU-1 | Section environmental systems | Green-4 -> DS-1 seasonal defaults / usage records (Blue-2) |
| SPU-2 | Research and analysis systems | Orange-3, Access 5 -> DS-2 general records (Green-4), DS-3 specific project records (Orange-2, Access 3) **copy of the Metavirus datafile handout only** |
| SPU-3 | Sectional administration | Orange-4, Access 5 -> DS-4 personnel (Green-3, Access 2), DS-5 general (Green-3, Access 2), DS-6 restricted files (Orange-5, Access 5, Trace and Burn 5), I/OP-1 meeting-room terminal (Green-4, Access 4) |
| SPU-4 | Local security sub-processor: hallway cameras every 10 m and every maglock keypad in Alpha (and Beta, were it working) | Orange-5, Barrier 5, Blaster 5 -> DS-7 security files (Green-4, Access 4), I/OP-2 office terminal (Green-3, Access 3), I/OP-3 Main Security terminal (Green-3, Access 3) |
| SPU-5 | Secondary research sub-processor | Orange-3, Access 4 -> DS-8 backup files (Green-5, Access 2), DS-9 archive files (Green-3, Access 2) |

**2. Beta Section system** -- crashed. Physical damage killed it as a whole; the data storage unit in
the Analysis/Experimentation Area (Beta 10) still runs off a cyberdeck after an Electronics (3) test
to wire it in, and holds the 150 Mp Metavirus master file with its safeguards inoperative. Model as
a single unguarded datastore, not a host. The 20 Mp chip in Beta 7 (Data File One) is a file.

**3. Aztechnology Seattle Pyramid main system** -- 38+ security levels, Level 30 Black IC test bed;
explicitly "NO ONE has ever done it and lived." Do not build for this adventure; keep as the
legendary ceiling of the Seattle Matrix (already noted on the Aztechnology org and Pyramid location).

**4. Biogene's backup-site hit** -- offscreen; a hidden Biogene agent wipes Aztechnology's backup
copies during the run. Nothing to build.
"""

NOT_BUILT = """
- **Dr. Perkins** (Tiger-Sapiens variant), the infected troll, technicians and Ork guards, Wolf/Tiger/Bear Sapiens, giant cockroaches, flesh worms, millipedes -- creature stat blocks (pp.21-25), kept in the Research Park notes.
- **Lt. Carl Hollis** (Strum's second) -- folded into Strum's notes. **The elite bodyguards and attack dogs** in Alpha -- archetypes.
- **Dr. William Espinata, Emilio K. (Weapons), Juan Atzcapotzalco, Salvador Ramierez** -- leadership entries on Aztechnology, not NPC rows.
- **Governor Allenson (2039), the liner Asian Princess, the United Corporation Council** -- Night of Rage history, in the org notes.
- **Elyse Sunberg** (Seattle Corporate Council spokesperson), **Detective Lucas Niles** (Lone Star), **Ehran the Scribe**, **Dick Steubens** (Seahawks GM), **Nat "Hercules" Brandy / Ann Ransom** -- news-handout names; Niles is on the Lone Star notes.
- **Tanner** (Shalene's mentor, L.A.), **Sisters Sinister** (Frost's old gang), the traitor's kidnapped loved one, the Hands of Five monorail Mr. Johnson and his two hired samurai, the Seneca Street station -- backstory / one-scene devices.
- **Wharf 114 / S.S. Misha** -- one location row (Tacoma Docks); the ship is not a separate entry.
- **Ronnie Bean** homing device and the **Plastisteel-7 catalyst** -- gear, described in the notes.
"""

PLAY_NOTES = """
- The traitor subplot is optional and must be set up privately with one player before the session;
  without it, Holmes does all the betraying. Either way the Misha ambush is where the blackmail comes
  out.
- Legwork is nearly impossible: street contacts know nothing (roll and ignore); a corporate contact
  needs Etiquette (Corporate) 8, a science contact Knowledge 9 or Etiquette (Science) 6. Public data
  on the Research Park carries a decker's graffiti.
- Whether the team shoots the Ork children in the warehouse decides Bronston's whole attitude.
  Karma: sample 2, file 1, Owens 2, kidnapped Orks 1, killing Ork children -2.
- Beta Section is a sensory gauntlet, not the climax; keep the party alive for Alpha and the safe house.
- Aftermath: Aztechnology and Alamos want blood for a month or two; Biogene keeps its distance; only the
  lunatic fringe offers work. Then the rep upswing: these are the runners who burned Aztechnology.
- Loose ends: whatever Silver Angel was in the last adventure, the Metavirus is the same kind of
  time bomb; Owens at Biogene (or at Wilhem Park); Peterhoff if he lived; Honnicker if he lived; the
  Sapiens loose in the Tacoma sewers (failure ending news).
"""
