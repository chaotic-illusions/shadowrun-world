# Shadows of the Underworld (FASA 7323, 1995) -- an anthology of five unconnected short
# adventures (Excelsior, Two Solitudes, C.O.D., Double Dipping, Dead Run) sharing one backdrop:
# the chaotic, violence-wracked UCAS presidential campaign of summer 2057, following the tainted
# 2056 election. Candidates named in the book: Dunkelzahn (independent, dragon), Kenneth
# Brackhaven (Archconservative, anti-magic/anti-metahuman), General Franklin Yeats (Republican,
# VP Anne Penchyk), Dr. Rozilyn Hernandez (New Century Party), James Booth (Technocratic),
# Arthur Vogel (Democratic, dwarf eco-lawyer). All six get at least a short row; Vogel, Hernandez
# and Booth are poll-blurb texture (p.7) but are built anyway since Super Tuesday! (ORDER 26,
# not yet ingested) needs the same field.
# NOTE: ADVENTURE_ORDER in frontend/shared.js places "Shadows of the Underworld" at position 27
# (immediately after "Super Tuesday!" and before "Predator and Prey"). Dead Run and C.O.D. both
# lean on "Super Tuesday!" (Casualties of War / Carla Brooks / Bug City) as background continuity;
# specs/super_tuesday.py does not exist yet at the time of writing, so Anne Penchyk, the
# Empowerment Coalition, the Secret Hive and the three minor candidates are created fresh here.
# If super_tuesday.py is added later and creates any of the same names, convert this spec's rows
# for them to ORG_UPDATES/NPC_UPDATES so nothing double-creates.
# OCR quality collapses badly on pp. 53-58 and pp. 61-64, 70-98 (columns interleaved/scrambled,
# whole words dropped); content below is reconstructed from legible fragments, not invented.
# Karma tables for C.O.D., Double Dipping and Dead Run and some attribute columns (Carroll, Eichi,
# Cohen) are partly illegible in the scan and are flagged rather than guessed at.
# Source text: docs/Adventures/text/Shadowrun 2e - Adventure - Shadows of the Underworld
# {FASA7323}.txt (98 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "Shadows of the Underworld"
ORDER = 27
SOURCE = "Shadowrun 2e - Adventure - Shadows of the Underworld {FASA7323}.pdf, pp. 1-98"
YEAR = "2057 (Summer)"

SYNOPSIS = """
Five unconnected shadowruns, bound together only by the long, hot summer of the 2057 UCAS
presidential race. In **Excelsior**, a security-consulting meet with **Dunkelzahn**'s New York
staffer **Martha Delaney** turns into a hostage siege atop the Empire State Building when the
**Whole Earth Adventists** -- fanatic fringe of the **Church of the Whole Earth Inc**, convinced
the dragon is a living god -- try to "purify" a room full of yakuza and corp VIPs and blow up the
building's top floors for the cameras. In **Two Solitudes**, a missing-persons job for a
heartbroken Yamatetsu couple leads the runners to their gay mage son **Sho Kojima**, who
conjured a free spirit lover, **Hiro**, out of a botched summoning and fled into Japanese-occupied
San Francisco's Oakland/Berkeley underground -- one jump ahead of Saeder-Krupp watchman **Nils
Hammarand**'s blackmail and his adept killer **Schreck**.

**C.O.D.** sends the runners to babysit a smuggled "art object" that turns out to be a stolen
dragon egg, the centerpiece of a **Human Nation** plot (fronted by MCT manager **Lawrence
Carroll** and funded through yakuza fixer **Isao Yamazaki**) to stage a public dragon rampage in
downtown Seattle and cripple Dunkelzahn's poll numbers -- with the young dragon **Masaru** and
the Human Nation's own **Flaming Sword** paramilitary both bearing down on the delivery. In
**Double Dipping**, a "simple" kidnap-and-ransom for a disguised **Burt Aronson** turns out to be
a Humanis Policlub frame job built around ork socialite **Kinsey Zandras**, meant to spark
metahuman-on-metahuman riots and blackmail her father's shipping line into smuggling guns; the
runners have to out-run the vigilante **New Weathermen**, win over reporter **Gilby Rellets**, and
storm Aronson's own safehouse to clear their names.

**Dead Run** closes the book on the highest stakes: the runners stumble onto the murdered body of
presidential candidate **General Franklin Yeats** and the FBI's **Cohen and O'Rourke** brand them
the killers. The truth is stranger than politics -- Yeats was secretly host to a "good merge"
insect spirit of the **Secret Hive**, remnant of the shattered Universal Brotherhood, and running
mate **Anne Penchyk** is an agent of the mantis-spirit **Empowerment Coalition**, which killed him
(and framed the runners) to keep the Hive from taking the White House by proxy.
"""

TIMELINE = """
- **Summer 2057** -- the UCAS presidential race, coming off the "tainted" election of 2056, turns
  the streets into a proxy war between Humanis/Human Nation-backed metahuman-baiting and pro-
  Dunkelzahn fanaticism. All five adventures play out during this same hot summer, independently.
- **Excelsior**: the Whole Earth Adventists' one-night siege of the Windows on the World
  restaurant and the Empire State Building's top floors, timed to a Dunkelzahn campaign security
  consult.
- **Two Solitudes**: Sho Kojima vanishes from UC Berkeley about a week before the Kojimas hire the
  runners; the search, the underground's trust-test, and the two-front raid on the October 25th
  Alliance safehouse play out over the following days.
- **C.O.D.**: Masaru's egg is stolen, ferried to Seattle by air within a day, held at a Redmond
  firehouse for roughly 48 hours, then delivered into a staged downtown ambush the moment the
  dragon is spotted inbound.
- **Double Dipping**: Kinsey Zandras is snatched during a townhouse party, ransomed within about
  two days, exposed on the newsnets days later, and rescued from Aronson's own safehouse once the
  runners piece together who "Mr. Johnson" really was.
- **Dead Run**: General Yeats is murdered at the Plaza Hotel the same night the runners arrive for
  what they think is a routine meet; days of flight, legwork and a three-way firefight at Eve
  Donovan's Puyallup doss follow before the truth about the Secret Hive comes out.
"""

ORGS = [
    {
        "name": "Church of the Whole Earth Inc",
        "org_type": "mystical fellowship",
        "tier": 2,
        "summary": "Half New Age, half evangelical religious movement founded by Jaelle Lester after she saw Dunkelzahn's first Awakened appearance as a sign from the Goddess",
        "description": (
            "Founded in 2005 by Jaelle Lester, a spiritual seeker who despaired of ever reaching the "
            "Goddess through conventional activism until she watched a silver-and-azure dragon take "
            "wing over the trees and knew it for a sign. The Church built a large, sincere following "
            "over the decades on a message of ecological and spiritual redemption. A fervent minority "
            "of believers, calling themselves the Whole Earth Adventists, has taken Jaelle's revelation "
            "as literal license for violence in Dunkelzahn's name."
        ),
        "leadership": [
            {"name": "Jaelle Lester", "title": "Founder", "notes": "Wrote 'Jaelle Lester's Revelation' (2012) after her vision of Dunkelzahn's first appearance; the Church's foundational text."},
        ],
        "notes": "Excelsior: the Church itself takes no action in the adventure and disavows the Adventists' methods; it is the wellspring the fanatics distorted.",
    },
    {
        "name": "Whole Earth Adventists",
        "org_type": "cult",
        "affiliation_contact_type": "Cult",
        "tier": 1,
        "headquarters": "Mobile cell, New York City",
        "summary": "Violent fringe of the Church of the Whole Earth convinced Dunkelzahn's presidency is a holy mandate worth killing for",
        "description": (
            "A cell of Church of the Whole Earth fanatics who believe Dunkelzahn is destined for the "
            "presidency and that anyone standing in the way -- organized crime, unfeeling "
            "megacorporations -- forfeits the right to live in 'the dragon's utopia'. Dunkelzahn does "
            "not approve of the Adventists and believes them all talk; on the night of Excelsior he is "
            "proven catastrophically wrong."
        ),
        "leadership": [
            {"name": "Arthur Quazach", "title": "Cell leader / 'the voice'", "notes": "Ex-Humanis, broke with them after being forced to help slaughter elf children; joined the Church to atone."},
            {"name": "Alicia Bayone", "title": "Field commander", "notes": "A Mafioso's daughter turned true believer; leads the assault inside the restaurant."},
        ],
        "notes": (
            "Excelsior. About twenty operatives hit the Windows on the World restaurant atop the "
            "Empire State Building during a gathering of yakuza, Saeder-Krupp/Shiawase/Aztechnology "
            "types and Dunkelzahn's security staffer Martha Delaney: 41+ hostages, a dwarf sorcery "
            "adept (Duff 'Fingers' McGillis) scanning for magic, a decker (David 'Pokerface' Ryan) "
            "trying to break Dunkelzahn's Matrix jamming, C-14 charges wired to blow the top ~15 "
            "floors, and a getaway rigger (Mastic Boy) flying a hijacked Dunkelzahn-For-President "
            "advertising blimp off the observation deck. Rank and file (Chunk-Style, Napalm, Noah Kobo "
            "and the rest) run on Kamikaze combat drug (8 boxes on the Condition Monitor, addiction "
            "Essence loss). Two hired street punks with no real Adventist conviction, Blood and Blade, "
            "guard the security center for cred. If exposed, the incident makes Dunkelzahn look "
            "powerless to control his own supporters rather than dangerous -- the opposite of what the "
            "Adventists intended -- and survivors nurse a personal vendetta against the runners "
            "regardless of the outcome."
        ),
        "enemies": ["Humanis Policlub"],
    },
    {
        "name": "October 25th Alliance",
        "org_type": "policlub",
        "affiliation_contact_type": "Resistance movement",
        "tier": 2,
        "headquarters": "People's University, Oakland/Berkeley sprawl",
        "summary": "One of the two largest anti-occupation metahuman-rights groups in Japanese-occupied San Francisco's Oakland/Berkeley underground",
        "description": (
            "Favors political action and social services over pure terrorism, though it does run "
            "'terrorist-style' attacks on Japanacorp targets it judges will not spill innocent blood. "
            "Founded the People's University, whose 'floating' classes (to protect students and "
            "instructors from corporate reprisal) range from basic literacy to demolitions, tactical "
            "magic, decking and rigging -- often taught by sympathetic shadowrunners lodging there for "
            "a while. Its free clinic and food pantries are the university's only fixed addresses. The "
            "Alliance also runs informal law enforcement (people's tribunals) across the sprawl and "
            "treats operations against San Francisco's occupying authorities as no crime at all."
        ),
        "leadership": [
            {"name": "Sharon Greenfeld", "title": "Cell commander", "notes": "Elf, a former San Francisco citizen driven out with other metahumans by the Japanese Imperials."},
            {"name": "The Prof", "title": "Recruiter / street contact", "notes": "Elderly ork, ex-UC Berkeley faculty, vets outsiders at the White Horse Tavern before vouching for them."},
        ],
        "notes": (
            "Two Solitudes: shelters Sho Kojima and his spirit-lover Hiro after Sho steals data from "
            "Yamatetsu and flees Saeder-Krupp blackmail. Tests runners with a 'best jobs' list "
            "(bombing a Yamatetsu warehouse, torching the SF HQ entryway, hijacking a shipment, "
            "ambushing security, or a coordinated Matrix/physical hit) before trusting them to meet "
            "Sho. Publishes Sho's stolen data ('The Little Red Schoolhouse') over the local Matrix, "
            "exposing Yamatetsu's metahuman 'schools' as testing-lab feeder pipelines. Former dropout "
            "student Hal Conway, Sho's old roommate, joined the movement about five months before the "
            "adventure -- unknown to the Kojimas."
        ),
        "enemies": ["Yamatetsu Corporation", "Saeder-Krupp Heavy Industries"],
    },
    {
        "name": "Human Nation",
        "org_type": "policlub",
        "affiliation_contact_type": "Anti-metahuman fraternity",
        "tier": 3,
        "summary": "National anti-metahuman fraternity of powerful individuals backing Kenneth Brackhaven and paying gangs to manufacture street violence",
        "description": (
            "A wide-ranging fraternity of wealthy and powerful humans dedicated to eventually "
            "exterminating metahumanity. In Seattle its effort to swing public opinion behind "
            "Kenneth Brackhaven is run by MCT mid-level manager Lawrence Carroll, who pays "
            "metahuman gangs (through yakuza middlemen, to keep his own hands clean) to commit "
            "public mayhem for the trideo cameras. In response to Dunkelzahn's rising poll numbers, "
            "Carroll escalated to stealing a young dragon's egg and staging a public 'dragon attack' "
            "to discredit dragonkind and Dunkelzahn's candidacy at a stroke (C.O.D.)."
        ),
        "notes": "See the Threats sourcebook for the Human Nation's full national profile (cross-referenced but not detailed in this book).",
        "enemies": ["Dunkelzahn"],
    },
    {
        "name": "Flaming Sword",
        "org_type": "paramilitary",
        "affiliation_contact_type": "Militia",
        "tier": 2,
        "summary": "The Human Nation's paramilitary wing -- started as rich dilettantes playing soldier, now led and trained by hired military professionals",
        "description": (
            "Began as a clique of wealthy elite fantasists who never outgrew playing soldier; now led "
            "and trained by recruited military professionals and augmented with mercenaries and other "
            "highly trained specialists. Fiercely anti-metahuman and anti-magic; squads target obvious "
            "magicians and metahumans first in any fight."
        ),
        "leadership": [
            {"name": "Rob Sewall", "title": "'Captain' (honorary rank)", "notes": "Ex-Humanis Policlub; homicidal anti-metahuman zealot who found a professional home in the Sword."},
        ],
        "notes": "C.O.D.: an eight-sniper squad under Sewall covertly guards the runners and the stolen dragon egg at the Redmond firehouse, then has standing orders to kill Masaru, the egg and the runners together at the final delivery to erase all evidence of the Human Nation's plot.",
    },
    {
        "name": "New Weathermen",
        "org_type": "policlub",
        "affiliation_contact_type": "Metahuman-rights militants",
        "tier": 1,
        "headquarters": "Redmond, Seattle",
        "summary": "Violent metahuman-rights activists who target racist groups and leaders in terrorist attacks -- and who have been watching Burt Aronson for some time",
        "description": (
            "A radical Seattle metahuman-rights cell distinct from Oakland/Berkeley's October 25th "
            "Alliance. Suspects Humanis Policlub organizer Burt Aronson of orchestrating the Kinsey "
            "Zandras kidnapping and confronts the runners -- thirty-six strong -- to find out the "
            "truth before deciding whether to beat a confession out of them or recruit their help."
        ),
        "leadership": [
            {"name": "Derrick", "title": "Cell leader", "notes": "Troll; has taken a personal interest in exposing Aronson."},
        ],
        "notes": "Double Dipping: if convinced the runners were Aronson's dupes, Derrick reveals Aronson's real identity and urges them to rescue Kinsey; if attacked, the Weathermen try to beat 'the traitors' to death.",
        "enemies": ["Humanis Policlub"],
    },
    {
        "name": "Zandras Shipping",
        "org_type": "corporation",
        "tier": 2,
        "headquarters": "Seattle",
        "summary": "One of the most successful metahuman-owned businesses in the Seattle sprawl, with exclusive shipping routes into Salish-Shidhe Council territory",
        "description": (
            "President Malcolm Zandras built one of Seattle's few prominent ork-owned businesses on "
            "shipping routes into Salish-Shidhe land that plenty of bigger companies covet. In-house "
            "security is staffed by ex-runners; trucks run tight, professional escorts. Burt Aronson's "
            "Humanis cell targets the family to blackmail those routes into a weapons-smuggling "
            "pipeline for Humanis sympathizers in Salish-Shidhe territory."
        ),
        "leadership": [
            {"name": "Malcolm Zandras", "title": "President", "notes": "Kinsey's father; targeted for blackmail once his daughter is 'safely' returned."},
            {"name": "Kinsey Zandras", "title": "Heiress", "notes": "BTL-addicted socialite; the kidnap target."},
        ],
        "notes": "Double Dipping. Malcolm offers the runners 2,000 nuyen each for Kinsey's safe return and will not be talked up from it.",
    },
    {
        "name": "The Secret Hive",
        "org_type": "cult",
        "affiliation_contact_type": "Insect-spirit infiltration network",
        "tier": 3,
        "summary": "Insect-spirit remnant of the shattered Universal Brotherhood, infiltrating governments and corporations through 'good merge' hosts indistinguishable from ordinary people",
        "description": (
            "Formerly pulled the strings of the Universal Brotherhood cult; when Knight Errant's small "
            "nuclear device partially destroyed the Chicago Hive (see the novel 'Running Bright'), the "
            "surviving 'good merges' -- insect spirits whose human/metahuman hosts lend them enough "
            "independent intellect to function without a queen's direct guidance -- went underground "
            "and began quietly infiltrating governments across North America. The 2057 special "
            "presidential election was their chance to install a merge-possessed candidate, General "
            "Franklin Yeats, in the White House. The Queen's location and the full extent of the "
            "Hive's infiltration remain unknown."
        ),
        "notes": "Dead Run: Yeats was merged with a wasp spirit years earlier on a Chicago visit; FBI Special Agent Scott Cohen was merged shortly after admiring Yeats during the campaign. Both merges were unusually good -- neither man showed outward signs of possession.",
        "enemies": ["Empowerment Coalition"],
    },
    {
        "name": "Empowerment Coalition",
        "org_type": "spirit cabal",
        "affiliation_contact_type": "Mantis spirit cabal",
        "tier": 2,
        "summary": "A cabal of powerful mantis spirits, smuggled out of the Chicago Containment Zone, dedicated to stopping the Secret Hive -- not out of altruism, but rivalry",
        "description": (
            "First appeared (per the Super Tuesday adventure 'Casualties of War') trapped behind the "
            "Chicago Containment Zone wall; worked with outside contacts to smuggle members out and "
            "install them in, or ally them with, powerful and ambitious human and metahuman women, "
            "Anne Penchyk foremost among them. Despite opposing the Secret Hive, the Coalition has "
            "little regard for the human races and is, like the Hive, ultimately predatory."
        ),
        "leadership": [
            {"name": "Anne Penchyk", "title": "Chief human agent", "notes": "UCAS VP candidate; increasingly consumed by the Coalition's agenda since the events of Casualties of War."},
        ],
        "notes": (
            "Dead Run: orchestrated General Yeats's assassination through Penchyk -- luring him to the "
            "Plaza Hotel under threat of exposing his Hive possession, then having a true-form mantis "
            "kill the wasp spirit while Penchyk killed the human body -- and framed the runners as the "
            "fall guys to keep the Hive's attention off the Coalition's real work of hunting down Hive "
            "operatives one by one. Fixer Eve Donovan, who unwittingly arranged the fatal meet, is not "
            "part of the Coalition's plot and becomes a target herself once she starts asking questions."
        ),
        "enemies": ["The Secret Hive"],
    },
]

LOCATIONS = [
    {
        "name": "Empire State Building",
        "location_type": "landmark / monument",
        "city": "New York",
        "district": "Midtown Manhattan",
        "security_level": "Patrolled / Commercial",
        "summary": "The 2050s' still-prestigious NYC landmark, home to Shiawase/Aztechnology/Ares subsidiary offices and the Windows on the World restaurant; Knight Errant runs the lobby",
        "description": (
            "A dinosaur of a structure that still carries prestige despite its age and the ferrocrete "
            "shoring up 2005-earthquake damage -- Shiawase, Aztechnology and Ares all pack subsidiary "
            "office space into it, and the building bends noticeably in the wind. In the lobby, six "
            "Knight Errant guards run two Rating 8 magnetic anomaly detectors dressed up like a "
            "cyberpunk Christmas tree, plus Rating 3 chem-sniffer wands over every bag; a flat "
            "no-weapons policy means anyone whose cyberware trips a MAD gets slapped in taser "
            "restraints and asked for a SIN on the spot, and anyone carrying a gun with Concealability "
            "2 or less gets four guns pointed back and a very polite suggestion not to start anything. "
            "Steel lockers (Barrier 6, Rating 4 maglocks, one credstick apiece) let well-heeled visitors "
            "check hardware before the high-speed elevator ride up; above the hundredth floor, "
            "maintenance level 100 holds the building's pipes, turbines and fuse boxes, and level 102 "
            "is the antenna-and-satellite-dish roof."
        ),
        "notes": "Excelsior. The Whole Earth Adventists take the building floor by floor: lobby heavies with an Ares MP LMG on a tripod, a fourth-floor security center, a hundredth-floor maintenance level wired with C-14, and the observation deck and roof (101/102) as the final stand and blimp-mooring escape point.",
    },
    {
        "name": "Windows on the World Restaurant",
        "location_type": "restaurant",
        "city": "New York",
        "district": "Empire State Building, Floor 101",
        "security_level": "Patrolled / Commercial",
        "summary": "Posh restaurant licensed to reuse the name of the original after the 2005 earthquake destroyed the World Trade Center; a well-known corp/yakuza hangout and the site of Dunkelzahn's Excelsior meet",
        "description": (
            "Thick carpets, lots of brass, a jazz trio and exotic plants -- probably costing more UCAS "
            "dollars than the average runner dreams about -- with old photos and plaques on the walls "
            "telling the story of the licensing deal that let the original Windows' proprietors reopen "
            "here after the World Trade Center went down in the 2005 quake. Shiawase Atomics execs, "
            "Saeder-Krupp reps and Yamaguchi-gumi yakuza can all be found on any given night without "
            "incident, because none of them bother the others -- the security here is so good it stays "
            "hidden. Off the main dining room, a small windowless meeting room set up for a seminar "
            "(one large table, several chairs) has its own hermetic circle (Rating 4), white-noise "
            "generator and jammer built into the table's centerpiece -- soundproofed enough that the "
            "runners barely feel the door's air-pressure seal close before Martha Delaney starts "
            "talking business."
        ),
        "notes": "Excelsior. Martha Delaney rents the private seminar room to consult the runners about Dunkelzahn's Madison Square Garden rally; the Whole Earth Adventists take the whole restaurant hostage minutes later, herding 41+ hostages into the main dining room.",
        "controlling_org": "Church of the Whole Earth Inc",
    },
    {
        "name": "The Katana",
        "location_type": "restaurant",
        "city": "San Francisco",
        "district": "Presidio",
        "security_level": "Corporate High Security",
        "summary": "Intimate japanacorp-suit hangout just southeast of the Presidio where off-duty Imperial Marines drink alongside corporate salarymen",
        "description": (
            "A small, exclusive club-restaurant in Japanese-occupied San Francisco where the suits from "
            "Sanfran's various japanacorps hang out alongside the occasional off-duty Imperial Marine -- "
            "intimate enough for a discreet meet, if not quite private enough for comfort. A dragon-lady "
            "hostess at the door keeps her painted smile professionally fixed, though it slips visibly "
            "when metahuman or obviously non-Japanese patrons walk in; once she is satisfied a party "
            "belongs to a reservation, she escorts them to a large booth well away from the other tables."
        ),
        "notes": "Two Solitudes. Meet site where Mr. and Mrs. Kojima, desperate and hopelessly out of their element, hire the runners to find their missing son Sho for a flat 10,000 nuyen.",
    },
    {
        "name": "UC Berkeley",
        "location_type": "landmark / monument",
        "city": "Berkeley",
        "district": "Oakland/Berkeley sprawl",
        "security_level": "Low Security",
        "summary": "Corporate-sponsored university where Sho Kojima studied Occult Sciences; his abandoned dorm room is the runners' first real clue",
        "description": (
            "A once-public university now under corporate sponsorship, with a computer Host (Green-4, "
            "Rating 8 all subsystems, Trace-4 IC) holding student records. Sho's third-floor dorm room "
            "is a typical rectangular cubicle -- bunk bed, closet, bureau, desk -- decorated in a "
            "Spartan mix of Japanese touches and 'early magic geek'. Searching it turns up no sign of a "
            "struggle, but several changes of clothes, some chips, a portable chip reader and a couple "
            "of books are missing, along with faint traces of colored chalk dust on the wooden floor -- "
            "the remains of a small hermetic circle, too disturbed to reconstruct. A magician who "
            "assenses the room feels a strong undertone of loneliness stretching back months, "
            "underlaid by a brief, sharp surge of hope and happiness that is only just beginning to fade."
        ),
        "notes": "Two Solitudes. Campus magical rituals are forbidden outside lab rooms, meaning Sho's summoning attempt (which birthed Hiro) was already a serious breach before it went catastrophically wrong.",
    },
    {
        "name": "White Horse Tavern",
        "location_type": "bar",
        "city": "Berkeley",
        "district": "Near UC Berkeley campus",
        "security_level": "Low Security",
        "summary": "Cozy brick tavern a few blocks from campus, dead-drop and vetting site for the October 25th Alliance contact known as the Prof",
        "description": (
            "A nondescript brick building with narrow windows that looks like a holdover from the early "
            "twentieth century; inside, dark wood and brass, freestanding round tables along the "
            "windows and across the hardwood floor, a lunch counter along one side. Mostly college "
            "students eating and talking in small groups; a waitress breezes by with a tray, calling "
            "'sit wherever you want.' A back kitchen and manager's office serve as a screening room -- "
            "the Prof has the runners sent through the kitchen and told to 'find Bobby the cook' rather "
            "than simply waving them over, letting his contacts confirm the visitors' intentions before "
            "he shows himself."
        ),
        "notes": "Two Solitudes. FBI-equivalent-of-the-underground vetting happens here: the Prof tests the runners' honesty, and Hammarand's adept killer Schreck tracks the Prof here looking for Sho.",
        "controlling_org": "October 25th Alliance",
    },
    {
        "name": "October 25th Alliance Safehouse",
        "location_type": "safehouse",
        "city": "Oakland",
        "district": "Near the Gauntlet monorail corridor",
        "security_level": "No Security / Barrens",
        "summary": "Old brownstone crammed with scavenged Matrix gear and a rooftop satellite dish, hideout for Sho Kojima, Hiro and the Alliance cell that shelters them",
        "description": (
            "One of a small ring of intact buildings near the Gauntlet -- the narrow corridor where the "
            "monorail crosses into San Francisco and every passing train draws gunfire from the "
            "burned-out buildings on both sides, a favorite site for attacks against the occupation. "
            "The lower floors and basement have been cleared out and renovated with whatever modern "
            "equipment the underground could scavenge, mostly second-hand and kit-bashed computers and "
            "communications gear, all hooked up to a concealed satellite dish on the roof that links "
            "the brownstone into the greater Free State Matrix."
        ),
        "notes": "Two Solitudes finale: Yamatetsu's assault team and Hammarand's agent Schreck both hit the safehouse the same night, dropping the runners, the Alliance and both corporate factions into a three-way melee.",
        "controlling_org": "October 25th Alliance",
    },
    {
        "name": "Angelic Entertainment",
        "location_type": "corporate facility",
        "city": "Los Angeles",
        "security_level": "Corporate Standard",
        "summary": "Saeder-Krupp shell subsidiary in LA fronting corporate watchman Nils Hammarand's dragon-serving spy network",
        "description": "A media-industry shell corporation Saeder-Krupp uses to operate legally in the California Free State. Officially an entertainment company; in practice it is Hammarand's base for gathering blackmail material on anyone who might inconvenience Lofwyr, reached only through an automated message line that never returns calls from strangers.",
        "notes": "Two Solitudes. Also lists Schreck, Hammarand's adept assassin, as a 'special security associate' on staff. Sho's stolen telecom logs trace one call from his dorm room to Angelic Entertainment's LTG number, the thread that leads the runners to Hammarand.",
        "controlling_org": "Saeder-Krupp Heavy Industries",
    },
    {
        "name": "Eight-Sixteen",
        "location_type": "bar",
        "district": "Snohomish",
        "security_level": "Patrolled / Commercial",
        "summary": "Honest, hardworking-folks nightspot in Snohomish; the meet site where 'Lowery' (Lawrence Carroll in disguise) hires the runners to babysit a stolen dragon egg",
        "description": (
            "A charming little nightspot where honest, hard-working folks toss back soy-beer while the "
            "jukebox plays the latest twang country hits -- not the kind of place the runners are used "
            "to meeting a Johnson. The regulars have a 'Detect Strangers' spell on, it seems: the "
            "moment the runners step through the door, nearly every eye in the place swivels toward "
            "them, not hostile exactly, but nobody is buying a round either. The bartender waves toward "
            "the back with his bar rag -- 'first door on the left, past the kitchen' -- to an "
            "unremarkable cinder-block back room with a well-worn set of chairs and a battered table "
            "that looks, almost convincingly, like real wood."
        ),
        "notes": "C.O.D. Carroll poses as 'Lowery', an art collector needing discreet import handling for his new 'piece'; offers 10,000 nuyen per runner (2,000 up front) to babysit an unopened crate for 48 hours.",
    },
    {
        "name": "Flat City",
        "location_type": "smugglers den",
        "district": "Redmond",
        "security_level": "No Security / Barrens",
        "summary": "Tiny unregistered Redmond airstrip specializing in unscheduled flights -- the drop point for Masaru's stolen egg",
        "description": (
            "A small, dark airfield that goes completely black between flights. When a delivery is "
            "inbound, high-intensity arc lights pop on with a resounding tchonk, illuminating a long "
            "open stretch of pavement just long enough for a rounded Federated-Boeing Komet to swoop in "
            "from the north for a landing; the moment the T-bird stops, the lights cut out again, "
            "leaving only headlights and the plane's running lights until the handoff is done and it "
            "lifts off once more."
        ),
        "notes": "C.O.D. Twiggs's transport team lands here to hand off the stolen dragon egg to the runners, then races off to get distance before Masaru catches up.",
    },
    {
        "name": "Redmond Firehouse Safehouse",
        "location_type": "safehouse",
        "district": "Redmond Barrens ('Hollywood' area)",
        "security_level": "No Security / Barrens",
        "summary": "Converted firehouse (Barrier Rating 12) where the runners guard the stolen dragon egg -- secretly ringed by Flaming Sword snipers",
        "description": (
            "A two-story brick monstrosity that looks as old as Seattle itself but is in fairly good "
            "shape for its age -- an old, sturdy firehouse (Barrier Rating 12) with few windows and "
            "good sightlines. Two massive vehicle bay doors (Barrier 6, chainable from inside) and one "
            "normal-sized door secured with a Level 6 maglock (keyed to the passcode on Carroll's "
            "credsticks) are the only ways in. Inside, the main room is a huge, empty, oil-stained "
            "concrete box: a battered sofa, a cheap card table and chairs, an old trid set and an "
            "antique phone set to intercept incoming calls only -- purpose-built to be a boring place to "
            "spend a couple of days with a dragon egg."
        ),
        "notes": "C.O.D. Eight Flaming Sword snipers hide on the four surrounding rooftops, unseen by the runners; the Red Hot Nukes stage a diversionary dwarf-gang assault while a three-man yakuza strike team tries to steal the egg back through a second-story window.",
    },
    {
        "name": "Masaru's Lair",
        "location_type": "underground bunker",
        "city": "Vancouver",
        "district": "Vancouver Island",
        "security_level": "Low Security",
        "summary": "The young great eastern dragon Masaru's home, cave-collapsed by a runner team hired to steal his egg while he lay unconscious",
        "description": (
            "Masaru's dwelling, somewhere on Vancouver Island -- a place of rest and contemplation for "
            "the young dragon, quiet enough that he was caught completely off guard when a hired runner "
            "team broke in. A specially designed Stun Masaru spell, expensive fetishes, several summoned "
            "elementals, precise timing and a small fortune in Karma put him down long enough for the "
            "attackers to grab the egg and cave in the entrance behind them for extra escape time; "
            "Masaru dug himself free within hours, badly wounding one of his attackers' mages in the "
            "process, and flew straight for Seattle the moment he realized what was missing."
        ),
        "notes": "C.O.D. Masaru tracks the egg the whole way to Seattle by its magical resonance; the lair itself is never revisited in play.",
    },
    {
        "name": "Jefferson Center Building",
        "location_type": "shop",
        "city": "Seattle",
        "district": "Downtown",
        "security_level": "Patrolled / Commercial",
        "summary": "Fictitious 'delivery address' Carroll gave the runners for the dragon egg -- deliberately picked as a busy, highly visible spot for the staged 'dragon attack'",
        "description": (
            "A downtown office address right on the edge of the district, timed by Carroll to hit at "
            "the height of the lunch rush -- crowds of pedestrians, honking traffic, double-parked vans. "
            "No one inside is actually expecting a package; the address exists purely as a stage set, "
            "chosen for the widest possible civilian audience and camera coverage when Masaru arrives to "
            "reclaim his egg."
        ),
        "notes": "C.O.D. climax: Masaru confronts the runners here in human 'salaryman' disguise before Flaming Sword snipers force the fight into the open and the dragon assumes true form, unleashing his Noxious Breath on the crowded street.",
    },
    {
        "name": "Seward Club",
        "location_type": "casino",
        "city": "Seattle",
        "district": "Downtown",
        "security_level": "Patrolled / Commercial",
        "summary": "One of Seattle's finer casinos; Rating 4 MAD wands and chem-sniffers at the door, and the Heffernan Room where Burt Aronson (disguised as an elf) hires the runners to kidnap Kinsey Zandras",
        "description": (
            "An ornate, noisy gaming floor -- card tables running both trideo and 'flesh and deck' "
            "games, craps and dice tables, slot machines lining the walls, VR poker rigs letting "
            "patrons don a helmet and jack in against strangers across the club, a cash bar and buffet "
            "doing brisk business. The dress code reflects the club's status, and on a jumping Saturday "
            "night, casino security in Rating 4 MAD-wand-and-chem-sniffer checkpoints turns away anyone "
            "in obvious armor and slaps restraints on dangerous cyberware. Several plexiglass-walled "
            "private rooms overlook the floor; the Heffernan Room -- a couch or two, a wet bar, a "
            "telecom center, a few trideo slot machines and a private card table -- is where Mr. "
            "Johnson waits."
        ),
        "notes": "Double Dipping meet site. Aronson passes as an elf here, a disguise good enough to fool most runners without a high-success Perception (15) Test.",
    },
    {
        "name": "Kinsey Zandras's Townhouse",
        "location_type": "residential community",
        "city": "Renton",
        "district": "Maplewood",
        "security_level": "Patrolled / Commercial",
        "summary": "Kinsey and roommate Emily Daly's elegant townhouse, guarded by a six-to-twelve-strong private security team and the site of the staged kidnapping",
        "description": (
            "An elegant Renton townhouse behind a green-carpet lawn, its rooms mapped out across a "
            "living area (couches, chairs, a trid center), dining room (a massive faux-oak table "
            "connecting to kitchen, deck and garage), a well-stocked kitchen, a deck packed with party "
            "guests jamming to loud music, a two-car garage housing matching deep-red '57 Eurocar "
            "Westwinds, an upper hallway, a shared bathroom, two bedrooms, a locked storage closet, and "
            "the upstairs 'Party Room' where Kinsey and her friends indulge an illegal BTL habit in "
            "near-catatonic rows on the couches and floor. Four boosted, delarynxed attack dogs bred to "
            "kill patrol the grounds silently; a passive Matrix-linked trideo camera system covers the "
            "perimeter, and roving guard pairs check every arrival without quite managing to check "
            "everyone at a twenty-guest house party."
        ),
        "notes": "Double Dipping. Head of security Jameson, an adept, runs a professional team (Fred, Mandy, Counterweight) that is distracted but not incompetent during Kinsey's party -- the night the runners are meant to snatch her.",
        "controlling_org": "Zandras Shipping",
    },
    {
        "name": "Aronson's Redmond Safehouse",
        "location_type": "safehouse",
        "district": "Redmond, near Fort Lewis",
        "security_level": "No Security / Barrens",
        "summary": "Run-down three-floor brownstone hotel doubling as a Humanis Policlub safehouse, Aronson's records vault, and Kinsey Zandras's prison",
        "description": (
            "A squat, crumbling brownstone hotel in a neighborhood so far gone the runners are "
            "surprised it hasn't been razed already -- a working flophouse on the lower two floors "
            "(a threadbare lobby with a half-drunk 'guest' watching the door, a manager's office papered "
            "with pornography, paying guests including a street samurai on the run from Lone Star), "
            "with an electric-eye sensor at the top of the stairs to the third floor. Aronson's own "
            "floor is packed with bunks, weapons and every record of his operations -- successful jobs, "
            "contacts, blackmail material -- kept as leverage with his own Humanis superiors. Elemental "
            "adept Vander Peterson wards his room here (Background Count 1, candles and lamps casting "
            "shifting shadows) and keeps Kinsey shapechanged into a lizard, leashed to a spike in the "
            "floor and warded against astral detection."
        ),
        "notes": "Double Dipping finale. Aronson's chromed enforcer Kandle, lookout Karl, and squads of Humanis troops guard the building; the incriminating kidnapping data sits on a chip labeled 'Urban Brawl Scores'.",
        "controlling_org": "Humanis Policlub",
    },
    {
        "name": "The Last Drop",
        "location_type": "bar",
        "district": "Redmond",
        "security_level": "Low Security",
        "summary": "Quiet, mostly empty Redmond bar where reporter Gilby Rellets offers the runners a way to clear their names",
        "description": (
            "A little, unremarkable bar the runners duck into to think, mostly empty, which suits them "
            "just fine -- a few brews, a chance to decide on a next move. A skinny elf at a corner table "
            "has clearly been watching them for some time before he gets up, leans on their table and "
            "says quietly, 'I know who you are. I can help you -- but it'll cost you. Mind if I sit "
            "down?'"
        ),
        "notes": "Double Dipping. Aronson's enforcer Shelly and a Humanis hit squad storm the bar mid-interview to silence Gilby (Humanis's most-wanted reporter) and the runners as loose ends -- the ambush lands once the runners are too absorbed in the interview to notice the other patrons have quietly cleared out.",
    },
    {
        "name": "Plaza Hotel",
        "location_type": "hotel",
        "city": "Seattle",
        "district": "Downtown",
        "security_level": "Patrolled / Commercial",
        "summary": "Elegant downtown Seattle hotel three blocks from General Yeats's own hotel -- the site of his murder and the runners' fateful meet",
        "description": (
            "A well-appointed downtown hotel with formally sculpted flower gardens out front, its "
            "elegant facade lit softly at night -- an easy, unremarkable evening stroll from Yeats's own "
            "suite for a man expecting to face down a simple blackmailer alone. The runners arrive to "
            "find the tenth-floor suite quiet: a man in a dark suit lies on the neatly made bed, a large "
            "dark red patch soaking the coverlet, something torn clean through his throat down to the "
            "whitish ridge of the windpipe and the pale gleam of his spine. The face is intact -- "
            "dark-skinned, maybe fifty or sixty -- and unmistakably General Franklin Yeats. No sign of a "
            "struggle; the windows are armored glass and do not open; the only way in or out is the door "
            "the runners just used."
        ),
        "notes": "Dead Run. The runners arrive minutes after Anne Penchyk and a true-form mantis spirit kill Yeats (and the wasp spirit possessing him); FBI agents Cohen and O'Rourke arrive on their heels and brand the runners suspects.",
    },
    {
        "name": "Eve Donovan's Puyallup Doss",
        "location_type": "safehouse",
        "district": "Puyallup, near Hell's Kitchen",
        "security_level": "No Security / Barrens",
        "summary": "Fixer Eve Donovan's hideout in a mostly-abandoned Puyallup apartment building, guarded by King's Crimson gangers, where the Empowerment Coalition tries to silence her",
        "description": (
            "A stone's throw from Hell's Kitchen: fine gray ash lies over everything like dust on a "
            "forgotten place, most of the surrounding buildings filthy, crumbling or half-collapsed, "
            "faint light from the single working street lamp glinting off jagged broken windows. "
            "Donovan's third-floor apartment, reached up cracked concrete steps past shattered lobby "
            "doors and an elevator shaft long since stripped for scrap, is protected by a new maglock "
            "and a small security camera wired into her telecom so she can screen every visitor; two "
            "King's Crimson gang members guard the door at all times, thanks for a debt gang leader "
            "Alan Corliss owes her."
        ),
        "notes": "Dead Run. Anne Penchyk and mantis spirits from the Empowerment Coalition converge on the doss to silence Donovan just as the runners arrive, and FBI agents Cohen and O'Rourke break in mid-confrontation, forcing Cohen to reveal his own Secret Hive possession to survive.",
        "controlling_org": "King's Crimson",
    },
]

NPCS = [
    {
        "name": "Dunkelzahn",
        "role": "Independent dragon presidential candidate; unknowingly at the center of two of the book's five plots",
        "archetype": "Great Dragon",
        "title": "UCAS presidential candidate (Independent); running mate Kyle Hackner",
        "race": "Dragon",
        "gender": "Male",
        "connection": 6,
        "description": (
            "A silver-and-azure great dragon whose 2012 first Awakened appearance -- 'the beating of "
            "his silver and azure wings created the freshening air' -- inspired Jaelle Lester to found "
            "the Church of the Whole Earth; forty-five years later he is a serious UCAS presidential "
            "contender, running on 'A New Golden Age'. Never directly on stage in this book, but his "
            "authority is felt in every scene involving his staff or his enemies: he does not approve "
            "of the Whole Earth Adventists' violence and badly underestimates them."
        ),
        "background": "Runs his campaign's New York security consulting through staffer Martha Delaney and keeps a team of skilled deckers watching over his Matrix presence at all times.",
        "notes": (
            "Excelsior: authorizes Delaney to offer the runners up to 100,000 UCAS dollars each to "
            "defuse the Whole Earth Adventists' hostage siege without public bloodshed or exposure; "
            "his agents track down and remember any runner who takes his money and then abandons the "
            "job. C.O.D.: the real target of Lawrence Carroll's dragon-egg plot -- a public Masaru "
            "rampage is meant to tank Dunkelzahn's poll numbers by association. Poll standing in the "
            "book's news blurbs: 22 percent, behind Brackhaven's 24."
        ),
    },
    {
        "name": "Kenneth Brackhaven",
        "role": "Archconservative presidential candidate whose anti-magic, anti-metahuman campaign both the Human Nation and Humanis Policlub are covertly working to elect",
        "archetype": "Politician",
        "title": "UCAS presidential candidate (Archconservative Party); running mate William Ager",
        "race": "Human",
        "gender": "Male",
        "connection": 4,
        "description": (
            "Slogan: 'A Holy War for the Soul of the Nation'. A polished, confident stump speaker -- "
            "'We can take our streets and our schools back from those who are using the weakness and "
            "fear of our so-called leaders against us... together, we can restore to this country the "
            "greatness that has always been, and will always be, its birthright' -- who draws a "
            "deafening trideo-audience roar even through the dampers. Polling ahead of the field at 24 "
            "percent on the strength of fear-mongering about magic and metahumanity."
        ),
        "notes": (
            "C.O.D.: Human Nation operative Lawrence Carroll funds street violence and the dragon-egg "
            "plot specifically to boost Brackhaven's numbers at Dunkelzahn's expense, financed partly "
            "through yakuza contact Isao Yamazaki. Double Dipping: Burt Aronson's Humanis cell runs the "
            "Kinsey Zandras frame-up toward the same end -- discrediting metahumanity broadly enough "
            "that undecided voters break for Brackhaven."
        ),
    },
    {
        "name": "Arthur Vogel",
        "role": "Democratic presidential candidate -- a dwarf eco-lawyer campaigning on environmentalism",
        "archetype": "Politician",
        "title": "UCAS presidential candidate (Democratic Party)",
        "race": "Dwarf",
        "gender": "Male",
        "connection": 2,
        "description": (
            "A dwarf eco-lawyer running with an unnamed troll Eagle shaman as his VP pick -- 'now "
            "there's an image!' says the trideo coverage, adding that the pair are 'smart, savvy, "
            "articulate' rather than the usual crackpot tree-huggers, and 'just might have a shot at "
            "the Big Chair -- assuming no nasty skeletons come popping out of lawyer Vogel's closet.' "
            "Slogan: 'Save the Earth'."
        ),
        "notes": "Excelsior campaign-poll blurb (p.7) only; no direct scene. Trails the frontrunners in early summer polling.",
    },
    {
        "name": "Dr. Rozilyn Hernandez",
        "role": "New Century Party presidential candidate campaigning on a pro-magic, pro-technology platform",
        "archetype": "Politician",
        "title": "UCAS presidential candidate (New Century Party); running mate Ramsay McMulkin",
        "race": "Human",
        "gender": "Female",
        "connection": 2,
        "description": (
            "Billed by the trideo coverage as offering 'better living through electing mage-o-crat Roz "
            "and her gorgeous simstar veep' -- running mate Ramsay McMulkin, dismissed in the same "
            "breath as 'pretty, but can he type?' Slogan: 'Our Magical Future'; courts both 'magical "
            "goombahs and techno-weenies' in one ticket."
        ),
        "notes": "Excelsior campaign-poll blurb (p.7) only; no direct scene.",
    },
    {
        "name": "James Booth",
        "role": "Technocratic Party presidential candidate, a former UCAS vice president running on a status-quo platform",
        "archetype": "Politician",
        "title": "UCAS presidential candidate (Technocratic Party); running mate Brandon Ekimatsu",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": (
            "'Slick Jimmy and his suit' -- a ticket, the trideo blurb sneers, 'only their mothers could "
            "love'; a former vice president trying to trade on incumbency-adjacent status. Slogan: "
            "'The Status Quo'."
        ),
        "notes": "Excelsior campaign-poll blurb (p.7) only; no direct scene. Polling weakest of the six named candidates, roughly tied with Undecided.",
    },
    {
        "name": "Martha Delaney",
        "role": "Dunkelzahn's New York security staffer; hires the runners for the Excelsior meet that turns into a hostage siege",
        "archetype": "Corporate Security",
        "title": "Head of New York security, Dunkelzahn campaign",
        "race": "Human",
        "gender": "Female",
        "age": 38,
        "connection": 3,
        "description": (
            "A tall, commanding African-American woman with a pleasantly low-pitched voice and a "
            "presence that reads as consular even before she opens her mouth: 'Good evening. My name "
            "is Martha Delaney, and this is Percy. We are here on behalf of someone you all probably "
            "know of -- hopefully, you'll ever vote for him.' A former Knight Errant rent-a-cop who "
            "joined Dunkelzahn's staff about a year ago and has grown to respect him deeply as both "
            "dragon and person; two young children make her risk-averse under fire, letting the runners "
            "handle the terrorists directly rather than draw attention to herself."
        ),
        "background": "Has two children, ages four and two; 'retired' into an office job on Dunkelzahn's staff for their sakes and worries constantly what would happen to them if she were killed on the job.",
        "notes": (
            "Excelsior. Stats: Quickness4 Strength4 Charisma4 Intelligence4 Willpower5, Ess2.8, "
            "Reaction4(6), Initiative4(6)+1D6(2D6), Combat Pool6, Threat/Professional3/3; Armed "
            "Combat4, Athletics3, Car3, Computer3, Etiquette(Corporate)6, Etiquette(Street)3, "
            "Firearms5, Negotiation5, Unarmed Combat4; datajack, smartlink, telephone, wired reflexes "
            "1; Zoe 'Retrovision' suit, 5,000-nuyen credsticks (one per runner). Offers 25,000 UCAS "
            "dollars each for security consulting on the Madison Square Garden rally, then 100,000 "
            "each mid-siege (Dunkelzahn's authorization) to defuse the situation; carries a headphone "
            "link straight to Dunkelzahn throughout the crisis."
        ),
    },
    {
        "name": "Percy",
        "role": "Delaney's androgynous personal secretary; the Adventists' first, expendable casualty",
        "archetype": "Corporate Secretary",
        "title": "Personal secretary to Martha Delaney",
        "race": "Human",
        "connection": 1,
        "description": (
            "About 1.7 meters tall, willowy, bright blue eyes, long blond hair pulled back in a "
            "ponytail -- gender left deliberately ambiguous in the text. Greets the runners at the "
            "elevator with placid professionalism: 'Glad you showed up. Are you all here? I've rented "
            "a few lockers in case you'd like to store any, uh, valuables before we go up.'"
        ),
        "notes": "Excelsior. Efficient at logistics (rents the lobby lockers, produces a credstick for the runners), useless in a firefight; use the Corporate Secretary contact archetype for stats. The book explicitly flags Percy as disposable if the GM needs to show the Whole Earth Adventists mean business early.",
    },
    {
        "name": "Alicia Bayone",
        "role": "Whole Earth Adventist field commander -- a Mafioso's daughter turned cold true believer who leads the Windows on the World assault",
        "archetype": "Terrorist",
        "title": "Field commander, Whole Earth Adventists",
        "race": "Human",
        "gender": "Female",
        "age": 28,
        "organization": "Whole Earth Adventists",
        "connection": 2,
        "description": (
            "Tall and muscular, cutting an imposing and attractive figure whose charisma comes purely "
            "from an intimidating manner and a willingness to lead by example -- not from any softness. "
            "'Hands up, slowly,' she snaps through her teeth over the M22A2. 'Throw a spell, move too "
            "fast, and you're chunks, GOT IT?' Later, rallying the hostages: 'Pay attention! We are the "
            "warriors of the Whole Earth Adventists. Comply with our demands and you will live... "
            "Changes will be made, starting now. And they will continue when the great wyrm leads us, "
            "his chosen people, to the future!'"
        ),
        "background": "A Mafioso's daughter gone bad; grew up materially comfortable but emotionally starved, and learned early that violence bought her sympathetic noises and reform schools rather than prison. Channeled what little remains of her vulnerable side into achieving 'spiritual fulfillment' by ushering in the Adventists' Golden Age, unbothered that it requires other people to die.",
        "notes": (
            "Excelsior. B5(6) Q5(7) S4(6) C4 I5(?) W6, Ess1.6, Reaction4(9), Body Index1.6, "
            "Initiative4(9)+1D6(3D6), Combat Pool8, Threat/Professional5/4; Armed Combat3, Athletics4 "
            "(Cardiovascular6), Car2, Demolitions2, Electronics1 (Hot-wiring Vehicles5), Etiquette "
            "(Underworld)5, Etiquette(Street)3, Firearms6, Gunnery3, Leadership4, Unarmed Combat3 "
            "(Kyokushin-kai karate6); cybereyes (flare compensation/low-light/thermographic), plastic "
            "bone lacing, smartlink, retractable hand razors with improved Dikote blades, wired "
            "reflexes 2, muscle augmentation 2. Colt M22A2 with underbarrel grenade launcher and "
            "explosive-ammo clips, Colt Manhunter with silencer, 'Effervescence' armored evening gown "
            "(3/1). Reads Jaelle Lester's Revelation aloud to hostages before the assault escalates; "
            "flees via the hijacked blimp if the fight turns against her."
        ),
    },
    {
        "name": "Duff \"Fingers\" McGillis",
        "role": "Dwarf sorcery adept with the Whole Earth Adventists -- paranoid, magic-sniffing, and the most easily turned of the cell",
        "archetype": "Adept",
        "title": "Magical security, Whole Earth Adventists",
        "race": "Dwarf",
        "gender": "Male",
        "organization": "Whole Earth Adventists",
        "connection": 1,
        "description": (
            "Vain, distrustful even of his own compatriots Alicia and Noah, and quietly convinced "
            "everyone is out to get him -- a paranoia born of near-constant spell-locked Detect Enemies "
            "and Detect Magic use that has curdled into a full personality disorder. Mumbles constantly, "
            "seeming to carry on conversations with thirty different people at once, and speaks "
            "hesitantly because he is always trying to listen to everything being said around him. To "
            "Fingers, paranoia is simply a way of life. Envies Alicia's status within the cell."
        ),
        "notes": (
            "Excelsior (called 'Fingers Martillis' once in the book's own OCR-mangled prose, elsewhere "
            "'Duff McGillis' -- same character). B6 Q3 S5 C3 I5 W6, Ess6, Magic6, Reaction4, "
            "Initiative4+1D6, Combat Pool7, Magic Pool4/6, Threat/Professional4/3; Car2, "
            "Etiquette(Corporate)2, Etiquette(Street)2, Firearms3, Magical Theory5, Sorcery4 "
            "(Spellcasting6), Unarmed Combat3(Judo5); spells Manabolt6, Powerball5, Sleep5, Analyze "
            "Truth4, Detect Enemies5*, Detect Magic6*, Heal4, Chaotic World4, Physical Mask4, Magic "
            "Fingers7, Personal Physical Barrier6 (*spell-locked at listed Force); sapphire nose ring "
            "and earring spell locks, Ares Predator, lined coat (4/2). If the runners suggest Alicia "
            "plans to pin the blame on him, he can be talked into sabotaging the operation."
        ),
    },
    {
        "name": "Arthur Quazach",
        "role": "Whole Earth Adventist cell leader and 'voice' -- ex-Humanis, radicalized after being forced to help slaughter elf children",
        "archetype": "Terrorist Leader",
        "title": "Cell leader, Whole Earth Adventists",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": (
            "Attractive and charismatic, close to six feet tall, graying brown hair and green eyes, "
            "well-dressed with a slight upper-class New England accent. Opens with practiced calm even "
            "after the runners bust in on his operation: 'Hoi. Glad to see you made it out. We never "
            "intended to hurt anyone except the soulless corporate types you usually run into up "
            "there... I was going to tell Alicia to let the innocents go in just a couple of minutes.' "
            "Then, lower, working for a convert: 'I hate having to do this, but you know how it is. "
            "Sometimes things just have to be done to make a point. When Dunkelzahn becomes president, "
            "we're going to see an incredible change in this world... We're showing the world that the "
            "great dragon and the Whole Earth cannot be beaten by the power of money.'"
        ),
        "background": (
            "As a young man was an active member of the Humanis Policlub, where he learned most of "
            "what he knows about fighting and motivating others. Grew steadily disillusioned with the "
            "policlub's bigoted message, and after being forced to join in the slaughter of a group of "
            "elf children underwent a complete change of heart -- broke with Humanis, joined the Church "
            "of the Whole Earth to atone, and turned his zeal toward 'cleansing the world' instead. "
            "Rationalizes that people like his racist, corporate-yes-man father taught him hatred in "
            "the first place, and so all 'innately racist' corporate types must be eliminated so "
            "everyone can live together in harmony -- a search for meaning that has bounced him from "
            "one extremist group to another for most of his adult life."
        ),
        "notes": (
            "Excelsior. B5 Q4 S4 C6 I5 W6, Reaction4, Initiative4+1D6, Combat Pool7, "
            "Threat/Professional4/3; Armed Combat2, Car3, Computer4, Computer Theory4, Etiquette "
            "(Corporate)4, Etiquette(Street)3, Etiquette(Underworld)5, Firearms4, Negotiation5, "
            "Leadership6, Unarmed Combat5; Ares Predator with flechette rounds, form-fitting body "
            "armor (Level3, 4/1), pocket secretary. Runs the fourth-floor security center with decker "
            "David 'Pokerface' Ryan and two hired guards, Blood and Blade. Will let the runners walk "
            "(with a 1,000-nuyen bribe) if they seem sympathetic, or fight to the last if pressed; if "
            "he or the whole cell dies, the bomb still goes off on schedule."
        ),
    },
    {
        "name": "Eden Harper",
        "role": "Freelance demolitions expert hired by the Whole Earth Adventists -- a radiation-scarred ex-shadowrunner racing her own death clock",
        "archetype": "Demolitions Expert",
        "title": "Freelance demolitions specialist",
        "race": "Human",
        "gender": "Female",
        "age": 29,
        "connection": 2,
        "description": (
            "Physically repulsive: dry, flaking skin covered in large untreated tumors, a scalp with "
            "the same wasp-nest look as the rest of her, one arm replaced with dull cyberware after it "
            "withered, the other visibly deteriorating. Speaks in a raspy, mispy stutter, often hard to "
            "understand. When the runners first see her bent over a couple of wires in the maintenance "
            "room she snaps, 'Wh-what the geek-hag do you want?!' -- and flies into a killing rage at "
            "any hint of pity or condescension, fighting to the death against whichever runner triggers "
            "it."
        ),
        "background": (
            "Only twenty-nine but suffers from radiation sickness that makes her look wizened and "
            "ancient -- caught in the periphery of Chicago's Cermak Blast while living nearby. A former "
            "shadowrunner by trade, she used her skills and contacts to escape the city, but the "
            "sickness and the trauma have driven her over the edge; she has perhaps a year left to "
            "live and knows it, which makes her willing to take extreme risks. She cares nothing for "
            "the rightness of any cause or who gets hurt -- the only thing that still makes her happy "
            "is knowing her work causes others the same pain she carries."
        ),
        "notes": (
            "Excelsior. Body3 Quickness5 Strength3 Charisma1 Intelligence5 Willpower8, Ess1, "
            "Reaction5(6), Initiative5(9)+1D6(4D6), Combat Pool8, Threat/Professional4/4; Car3, "
            "Computer4, Demolitions7, Demolitions(B/R)6, Etiquette(Street)3, Firearms5, Stealth6, "
            "Throwing Weapons4, Unarmed Combat3(Cyberimplant5); cyberarm with smartlink and spurs, "
            "cyberears with dampers, cybereyes (flare compensation/low-light/thermographic), datajack "
            "(Level4); armored jacket (5/3), Ingram Smartgun, painkillers, four offensive grenades "
            "(10S). Severe nerve damage gives her Pain Resistance (3 boxes) against surface pain. Arms "
            "the Empire State Building's rooftop bomb in the hundredth-floor maintenance room; a "
            "strong Negotiation roll (TN 11, TN 9 with a bribe or a Dunkelzahn favor) can talk her into "
            "disarming it herself."
        ),
    },
    {
        "name": "Noah Kobo",
        "role": "Whole Earth Adventist gunman who herds hostages alongside Alicia and later guards the maintenance elevator",
        "archetype": "Terrorist",
        "title": "Field operative, Whole Earth Adventists",
        "race": "Human",
        "gender": "Male",
        "organization": "Whole Earth Adventists",
        "connection": 1,
        "description": (
            "Carries an HK submachine gun and covers the right flank alongside Alicia's left when the "
            "cell first reveals itself; herds hostages into the main dining room, then locks down the "
            "maintenance elevator once the building is secure. Harbors real grudges against corps and "
            "yakuza and genuinely believes the purge is doing the world a favor -- not just following "
            "orders."
        ),
        "notes": "Excelsior. Uses generic Adventist terrorist stats (B4/5 Q4/5 S3/5, Firearms 5, Kamikaze-boosted, only eight boxes of Condition Monitor due to the drug's addiction). Reacts instantly if the maintenance elevator is called by anyone unauthorized.",
    },
    {
        "name": "David \"Pokerface\" Ryan",
        "role": "Whole Earth Adventist decker desperately trying to break Dunkelzahn's Matrix jamming during the siege",
        "archetype": "Decker",
        "title": "Decker, Whole Earth Adventists",
        "race": "Human",
        "gender": "Male",
        "organization": "Whole Earth Adventists",
        "connection": 1,
        "description": (
            "Wears a black lined coat with a dragon card crossed out and 'NEVER DEAL WITH A DRAGON' "
            "emblazoned on the back -- irony he is no longer enjoying living out. Concentrating on his "
            "job to the exclusion of everything else, he does not relish killing half as much as his "
            "compatriots, and once Dunkelzahn's own deckers start dumping him from the building's "
            "system with vicious attack programs, he just wants out."
        ),
        "notes": (
            "Excelsior. Essence4(5), Reaction4, Threat/Professional2/2; Athletics2, Car2, Computer5, "
            "Computer(B/R)2, Computer Theory4, Electronics3, Electronics(B/R)2, Etiquette(Matrix)4, "
            "Etiquette(Street)3, Firearms2; datajack (Level4), headware memory (150 Mp), cybereyes(4), "
            "softlink (4 ports). Fuchi Cyber-4 deck (MPCP 4/3/3/3/3, mostly burned by Dunkelzahn's "
            "deckers if he loses), Level4 skillsofts (Firearms, Unarmed Combat, Demolitions), Ruger "
            "Super Warhawk. His Demolitions skillsoft, if recovered, lets any runner with skillwires "
            "disarm the rooftop bomb later."
        ),
    },
    {
        "name": "Mastic Boy",
        "role": "Adventist rigger who flies the hijacked Dunkelzahn-For-President blimp as the cell's planned escape vehicle",
        "archetype": "Rigger",
        "title": "Getaway rigger, Whole Earth Adventists",
        "race": "Human",
        "gender": "Male",
        "organization": "Whole Earth Adventists",
        "connection": 1,
        "description": "A staunch Adventist true believer who genuinely does not want to see his friends hurt -- he holds fire on anyone not actively shooting at his people and avoids civilians in suits or gowns out of caution, not mercy, though he will skip anyone in melee range of his fellow Adventists rather than risk hitting them.",
        "notes": "Excelsior. Uses the Rigger archetype (SRII p.59). Flies a Zeppelinwerke advertising blimp with a popup remote-turret Vindicator minigun (1,000 rounds normal/tracer ammo); the cell's chosen escape method because advert blimps are effectively invisible to anti-aircraft sensors, can swap their advertising to blend with other blimps over downtown New York, and no cop will shoot down a blimp over the city.",
    },
    {
        "name": "Chunk-Style",
        "role": "Whole Earth Adventist ground-floor heavy guarding the Empire State Building lobby, keeps the whole operation's plan written out in his pocket",
        "archetype": "Terrorist",
        "title": "Ground-floor security, Whole Earth Adventists",
        "race": "Human",
        "gender": "Male",
        "organization": "Whole Earth Adventists",
        "connection": 1,
        "description": (
            "A bruiser paired with Napalm on an Ares MP LMG (stenciled 'No Smoking' on its side) mounted "
            "on a tripod behind the lobby's marble security desk, pointed at the exit door. Not "
            "confident he can keep the whole plan straight in his head, he has written it out in simple "
            "words on a sheet of paper he keeps in his pocket: 'Lobby. Lock Doors (Very Important). "
            "Security Central (4th floor). Guards. Check. Roof. Bombs. Check. Restaurant. Check. Com "
            "Call. Final Check. Wait. Deck.'"
        ),
        "notes": "Excelsior. Shares the 'Ground Floor Heavies' stat block with Napalm: B5(6) Q5(6) S5(7) C3 W5(6) Reaction3, Armor6/4, Threat/Professional3/4; Armed Combat2, Athletics3, Car3, Demolitions2(Plastic Explosives4), Etiquette(Street)4, Etiquette(Underworld)5, Firearms5, Gunnery3, Rotorcraft2, Unarmed Combat2(Boxing3); cybereyes (low-light/flare compensation), smartgun links; Securetech armor jackets with helmets, the Ares MP, Ares Predators, a ballistic-cloth duffel bag, micro-transceivers, gear looted off downed Knight Errant guards. Only eight boxes of Condition Monitor from Kamikaze addiction.",
    },
    {
        "name": "Napalm",
        "role": "Whole Earth Adventist ground-floor heavy paired with Chunk-Style on the lobby's tripod-mounted LMG",
        "archetype": "Terrorist",
        "title": "Ground-floor security, Whole Earth Adventists",
        "race": "Human",
        "gender": "Male",
        "organization": "Whole Earth Adventists",
        "connection": 1,
        "description": "The other of the two lobby heavies covering the exit door with the Ares MP; if word reaches them that shadowrunners are loose in the building, both take their dose of Kamikaze and swing the gun toward the stairs.",
        "notes": "Excelsior. Shares the 'Ground Floor Heavies' stat block with Chunk-Style (see that row). Killing both and searching them for the written plan is the fastest way for runners to learn the security center is on the fourth floor and that a bomb is coming.",
    },
    {
        "name": "Blood",
        "role": "Hired street punk who thinks he's a samurai, guards the Adventists' fourth-floor security center",
        "archetype": "Ganger",
        "title": "Hired guard, Whole Earth Adventists",
        "race": "Human",
        "gender": "Male",
        "organization": "Whole Earth Adventists",
        "connection": 1,
        "description": "Paired with Blade at the security-center door, watching the hallway camera for trouble. Not a true believer -- just muscle for hire who thinks the job makes him a samurai -- and will fall for almost any line the runners feed him if they bluster their way in rather than burst in shooting.",
        "notes": "Excelsior. Shares a stat block with Blade: Initiative6+2D6; Armed Combat3(Edged Weapons5), Bike2, Car3, Etiquette(Street)3, Firearms5, Unarmed Combat3; datajack, retractable hand razors, smartgun link, wired reflexes1, cybereyes (low-light/thermographic), cyberears (hearing amplification/sound dampener); armored jacket (5/3), Ingram Smartgun, knife, micro-transceivers, a simsense chip (The Dragon Warrior), steel knuckles, two doses of Kamikaze they refuse to touch.",
    },
    {
        "name": "Blade",
        "role": "Hired street punk paired with Blood, guarding the Adventists' fourth-floor security center",
        "archetype": "Ganger",
        "title": "Hired guard, Whole Earth Adventists",
        "race": "Human",
        "gender": "Male",
        "organization": "Whole Earth Adventists",
        "connection": 1,
        "description": "The other hired 'samurai' watching the security-center door alongside Blood; ready for trouble if the runners bust in with guns blazing, but easy marks for a convincing bluff or a knock and a story.",
        "notes": "Excelsior. Shares Blood's stat block (see that row).",
    },
    {
        "name": "Mr. Heol",
        "role": "Yamaguchi-gumi yakuza hostage singled out by name during Alicia's speech to the Windows on the World crowd",
        "archetype": "Yakuza Boss",
        "title": "Yamaguchi-gumi yakuza representative",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "connection": 1,
        "description": "A dignified-looking Asian man in a designer suit; Alicia steps up to him mid-rant and stares him down: 'Isn't that right, Mister Heol of the Yamaguchi-gumi yakuza?'",
        "notes": "Excelsior. Name-and-affiliation only; no stats given. One of several VIP hostages the Adventists' Fingers scans for magic and strips of foci during the takeover.",
    },
    {
        "name": "Mr. Nocaito",
        "role": "Saeder-Krupp executive hostage singled out by name during Alicia's speech to the Windows on the World crowd",
        "archetype": "Corporate Executive",
        "title": "Saeder-Krupp representative",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": "Another executive-type Alicia calls out by name and stares down as she surveys the hostages: 'And Mister Nocaito of Saeder-Krupp?'",
        "notes": "Excelsior. Name-and-affiliation only; no stats given.",
    },
    {
        "name": "Ms. Reilly",
        "role": "Shiawase Atomics executive hostage singled out by name during Alicia's speech to the Windows on the World crowd",
        "archetype": "Corporate Executive",
        "title": "Shiawase Atomics representative",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": "The third VIP Alicia singles out, shifting her hard stare to a nearby woman: 'And Ms. Reilly of Shiawase Atomics?'",
        "notes": "Excelsior. Name-and-affiliation only; no stats given.",
    },
    {
        "name": "Kyle Hackner",
        "role": "Dunkelzahn's human vice-presidential running mate, who takes on more public appearances after the Excelsior siege damages the campaign's image",
        "archetype": "Politician",
        "title": "UCAS vice-presidential candidate (running with Dunkelzahn)",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": "A philanthropist chosen as Dunkelzahn's running mate specifically to make nervous voters more comfortable with the idea of a dragon president -- billed in the campaign coverage as making 'even nervous voters like the prize'.",
        "notes": "Excelsior aftermath: fronts more of the campaign's public face after the siege reminds voters, forcibly, that Dunkelzahn is 'not a pet of anything that resembles one'; Dunkelzahn himself retreats to human-form-only appearances until other news bumps the incident off the air.",
    },
    {
        "name": "Sho Kojima",
        "role": "Missing UC Berkeley Occult Studies student -- a closeted gay mage whose botched summoning birthed the free spirit Hiro",
        "archetype": "Mage",
        "title": "Occult Studies student, UC Berkeley",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese-American",
        "organization": "October 25th Alliance",
        "connection": 3,
        "description": (
            "A talented, isolated young mage who has hidden his homosexuality from his parents for "
            "years -- illegal for someone of his social standing under Japanese-occupied San "
            "Francisco's 'protected culture' laws, which confine openly gay residents to the "
            "Oakland/Berkeley enclaves. In the prologue, fleeing his dorm with a duffel bag over one "
            "shoulder, he snaps at Hiro with dry gallows humor: 'Yeah? What're you planning on doing, "
            "Hiro? Going out there and flaming the guy? That might attract a little unwanted attention, "
            "don't you think?' His achievements at school -- straight-A's, faculty praise -- mask deep "
            "inner turmoil his classmates never see past 'bright but bookish, shy and difficult to get "
            "to know.'"
        ),
        "background": (
            "Discovered visiting clandestine gay establishments by Saeder-Krupp watchman Nils "
            "Hammarand, who blackmailed him into stealing his accountant father's access codes to "
            "Yamatetsu's secret spreadsheets. Rather than hand the data over, Sho tried to conjure an "
            "elemental to kill Hammarand; it escaped his control and became the free spirit Hiro, who "
            "fell in love with him. They fled together into the Oakland/Berkeley underground under the "
            "October 25th Alliance's protection."
        ),
        "notes": (
            "Two Solitudes. Body3 Quickness3 Strength2 Intelligence4 Willpower4 Charisma5, Ess5, "
            "Reaction4, Magic5, Initiative5+1D6, Threat/Professional2/2; Conjuring4, Enchanting2, "
            "Etiquette(Corporate)2, Magical Theory4, Sorcery4, Unarmed Combat (rating garbled in the "
            "scan); datajack, headware memory (80 Mp); armor clothing (2/0), Yamatetsu Ronin laptop "
            "computer (250 Mp), Hermetic Library (Rating2) on optical chips; spells Analyze Magic, "
            "Treat3, Mask3, Lighter2. Remains with the Alliance and Hiro at the adventure's end rather "
            "than return home; asks the runners to tell his parents he is safe."
        ),
    },
    {
        "name": "Hiro",
        "role": "Free spirit born from Sho Kojima's botched summoning -- fiercely loyal, fire-natured, and devoted to protecting his summoner",
        "archetype": "Free Spirit",
        "title": "Hana (animus spirit); Sho Kojima's partner",
        "race": "Free Spirit",
        "gender": "Male",
        "organization": "October 25th Alliance",
        "connection": 1,
        "description": (
            "A hana, a rare type of animus spirit whose form and personality sprang directly from Sho's "
            "innermost desires. His laugh is 'a beautiful sound, rich and deep'; his face and form "
            "shimmer 'like a dampened watercolor' when he shapeshifts to help Sho escape pursuit -- "
            "'I go first,' he tells Sho in the prologue. 'Our friend follows me. Then I pull another "
            "presto-change-o, leave him chasing his tail. Meanwhile, you slip out and find a safe "
            "hiding place across the Bridge. I'll catch up... and then we're home free.' Newly awakened "
            "to a world of sensation and emotion he never suspected, passionate and protective but "
            "poorly versed in mundane human values -- a poor planner despite his power."
        ),
        "notes": (
            "Two Solitudes. Force5, Spirit Energy2; powers Engulf, Flame Aura, Flame Projection, Guard, "
            "Human Form, Immunity to Normal Weapons, Manifestation, Movement, Wealth; weakness "
            "Vulnerability (Water). Sets warning fires ('LEAVE SHO KOJIMA ALONE') rather than attack "
            "outright when trying to scare the runners off; fights to the death at the safehouse "
            "climax. Can reward cooperative runners with several thousand nuyen in gems via his Wealth "
            "power."
        ),
    },
    {
        "name": "Nils Hammarand",
        "role": "Saeder-Krupp corporate watchman working for Lofwyr, who blackmailed Sho Kojima and set his adept killer Schreck on the trail",
        "archetype": "Corporate Watchman",
        "title": "Watchman, Angelic Entertainment (Saeder-Krupp)",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "Runs a network of informants across the California Free State from a Los Angeles shell-corp "
            "office, hunting exploitable weaknesses in anyone who might inconvenience the great dragon "
            "Lofwyr. Short-tempered and contemptuous of subordinates who fail him: 'What do you mean, "
            "you lost him?' he snarls into his datajack over a lost tail on Sho. 'Wet-behind-the-ears "
            "suitboy whelp, knows as much about the real world as a baby rabbit... and he gives you the "
            "slip? Explain to me how this happens. On second thought, don't. I don't want to hear it... "
            "You find that kid or you'll live just long enough to regret it.' Instantly straightens up "
            "and smooths his hair when his own boss appears in the doorway."
        ),
        "background": "Discovered Sho Kojima's sexuality through his informant network and blackmailed him into corporate espionage against Yamatetsu, hoping the score would be big enough to catch Lofwyr's attention and earn a European posting.",
        "notes": "Two Solitudes. Sends his agent Schreck after the runners and the Prof once his automated message line is used; takes note of the runners for potential future use (a job offer or a set-up, depending on how badly they cost him).",
    },
    {
        "name": "Kojima Sr.",
        "role": "Sho's father, a trusted Yamatetsu North America middle manager desperate to find his missing son",
        "archetype": "Corporate Manager",
        "title": "Middle manager, Yamatetsu North America",
        "race": "Human",
        "gender": "Male",
        "organization": "Yamatetsu Corporation",
        "connection": 2,
        "description": (
            "A dignified, out-of-his-depth corporate man who has never dealt with shadowrunners before; "
            "greets the team with a smooth, heavily accented voice -- 'Thank you for being so prompt. "
            "Please sit down' -- and covers his silent, tearful wife's hand with his own. 'I am a loyal "
            "employee. I trust that my company will do all it can, but I fear for my son. I wish to "
            "employ you to find him, discreetly. I can offer you the sum of 10,000 nuyen for his safe "
            "return, or information that leads to it.'"
        ),
        "background": "Middle manager with Yamatetsu North America; his wife is originally from Osaka. Has access, through Sho's forced theft of his passcodes, to spreadsheets Yamatetsu never lets show up in its corporate reports.",
        "notes": "Two Solitudes. Offers a flat 10,000 nuyen -- his idea of a fair opening offer, having learned negotiation mostly from trid shows -- and will not be moved off it. Later scapegoated as the internal 'hero' who exposed a rogue manager's schools scandal once Yamatetsu spins the fallout from the Little Red Schoolhouse leak; gets a promotion out of it.",
    },
    {
        "name": "Schreck",
        "role": "Nils Hammarand's principal agent -- a physical adept assassin who claims to feed on his victims' fear",
        "archetype": "Physical Adept",
        "title": "'Special security associate', Angelic Entertainment (Saeder-Krupp)",
        "race": "Human",
        "gender": "Male",
        "nationality": "German",
        "connection": 3,
        "description": "A giant of a man, orks-scale muscle wrapped in dark leather studded with chrome spikes and chains, chiseled features, a wild mane of white hair, a slight German accent. Follows the Twisted Way, and claims an empathic ability to draw strength and pleasure from the pain and fear of his victims.",
        "background": "Mentally unstable by almost anyone's definition -- his magical path is focused solely on improving his ability as a killer. If he were not working for Saeder-Krupp he would probably be a serial killer; as it is, his work for Hammarand gives him ample opportunity to indulge his addiction to inflicting pain on others.",
        "notes": (
            "Two Solitudes. B6(9) S6(10) Q4 I4 W5 C2, Initiate Grade4; Improved Unarmed Combat 2, "
            "Killing Hands (geas: only at night), Strength Boost +4 (geas: only while a victim is "
            "frightened or in pain), Empathic Sense, Pain Resistance 3; quickened Enhance Aim, Personal "
            "Spell Barrier and Increase Reflexes from a Saeder-Krupp mage. A shrewd professional, not a "
            "loose cannon -- withdraws and regroups rather than dying for the job."
        ),
    },
    {
        "name": "The Prof",
        "role": "Elderly ork ex-UC Berkeley professor who vets outsiders for the October 25th Alliance at the White Horse Tavern",
        "archetype": "Contact",
        "title": "Street contact, October 25th Alliance",
        "race": "Ork",
        "gender": "Male",
        "organization": "October 25th Alliance",
        "connection": 2,
        "description": "White-haired, beady-eyed, careful; approaches the runners' table unbidden with a simple 'Good evening. Mind if I join you?' Lost his faculty post to 'budget cuts' when corporate sponsors took over the school and found a second calling recruiting for the underground.",
        "background": "The title dates back to his days as a member of the UC Berkeley faculty before he goblinized; when corporate sponsors took over the school shortly after, his job was among the first sacrificed, and he ended up joining the October 25th Alliance.",
        "notes": "Two Solitudes. Uses a Deckhand-Technician-style archetype modified for an ork. Tests the runners' sincerity before arranging their meeting with Sho; grateful (and cooperative) if they save him from Schreck in the tavern's back alley.",
    },
    {
        "name": "Sharon Greenfeld",
        "role": "Elf commander of the October 25th Alliance cell sheltering Sho Kojima and Hiro",
        "archetype": "Mage",
        "title": "Cell commander, October 25th Alliance",
        "race": "Elf",
        "gender": "Female",
        "organization": "October 25th Alliance",
        "connection": 2,
        "description": "A former San Francisco citizen driven into the Oakland/Berkeley enclaves along with other metahumans by the occupying Japanese Imperials; questions captured runners about their identities and purpose herself before deciding whether to let them near Sho.",
        "notes": "Two Solitudes. Uses the Former Wage Mage archetype with elven racial modifiers. Grants a supervised meeting with Sho if convinced of the runners' honesty, but will not let them use force to persuade him to go with them; fights to defend the safehouse in the finale.",
    },
    {
        "name": "Hal Conway",
        "role": "Sho Kojima's former dorm roommate, who dropped out of UC Berkeley and joined the underground five months before the adventure",
        "archetype": "Student Dropout",
        "title": "Former roommate of Sho Kojima; October 25th Alliance",
        "race": "Human",
        "gender": "Male",
        "organization": "October 25th Alliance",
        "connection": 1,
        "description": "College records list him as also enrolled in Occult Studies before he dropped out five months before Sho's disappearance -- a fact unknown to the university, the Kojimas, or, at first, the runners.",
        "background": "Left UC Berkeley to join the underground establishment known as the People's University; his trail is deliberately hard to follow, and street word puts him solidly inside the October 25th Alliance's orbit by the time the runners come looking.",
        "notes": "Two Solitudes. Never directly encountered; known only through legwork (Street Etiquette TN 4 table) that points the runners toward the White Horse Tavern and the Prof.",
    },
    {
        "name": "Lawrence Carroll",
        "role": "MCT mid-level manager and Human Nation operative posing as art collector 'Lowery' to run the C.O.D. dragon-egg plot",
        "archetype": "Corporate Manager",
        "title": "Mid-level manager, Mitsuhama Computer Technologies; Human Nation operative",
        "race": "Human",
        "gender": "Male",
        "organization": "Human Nation",
        "connection": 3,
        "description": (
            "Gaunt, forty-ish, graying brown hair, pale blue eyes -- dressed down to blend into a "
            "working-class Snohomish bar except for hideously expensive boots that give him away as a "
            "corper trying to pass for a local. Boastful and a little too pleased with himself around "
            "his yakuza contact: 'The stupid trogs don't realize they're digging their own graves,' he "
            "chuckles, before bragging that 'we've gotten hold of something that's gonna bring a dragon "
            "to town, mad enough to shake the walls down... and when he does, the stupid worm is gonna "
            "send Dunkelzahn's campaign right down the drekker where it belongs.' As 'Lowery' he plays "
            "friendly and straightforward, offering to buy drinks, but makes clear from the first "
            "meeting that he is the boss and won't take any drek from the runners."
        ),
        "background": (
            "Grew up working his father's electronics store; witnessed a metahuman-driven 'Night of "
            "Rage'-style riot as a child, and while others moved on, Carroll's fear curdled into a "
            "lasting desire for revenge. Came to believe humans were destined to inherit the world and "
            "that he was cleverer and more cunning than most, and vowed to rid it of metahumanity -- a "
            "vow he now pursues through his day job's cover as a Mitsuhama Computer Technologies "
            "manager and his real work funding Human Nation violence."
        ),
        "notes": (
            "C.O.D. Stat block badly garbled by OCR; legible fragments give Etiquette(Corporate)4, "
            "Negotiation5, and a Remington Roomsweeper heavy pistol. Pays 10,000 nuyen per runner "
            "(2,000 up front, negotiable up with successful Negotiation), truthfully claims the package "
            "holds no bombs, drugs, BTLs or weapons, and never intends any of the guarding runners to "
            "survive the finale."
        ),
    },
    {
        "name": "Isao Yamazaki",
        "role": "Yakuza fixer and Human Nation middleman who arranges gangs to watch Seattle's smuggling routes and later scrambles to recover the stolen dragon egg",
        "archetype": "Yakuza Fixer",
        "title": "Fixer, Yakuza (Watada-rengo)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Yakuza (Watada-rengo)",
        "connection": 3,
        "description": (
            "Middle-aged, composed, precise; smiles faintly at Carroll's boasting, 'his white teeth "
            "barely visible between thin, papery lips.' Privately finds dealing with fanatics like "
            "Carroll distasteful even while taking their money -- 'One would think the violence would "
            "have died down by now -- the gangs must have a strong motivation indeed to continue their "
            "destruction at such a pace' -- and haggles over the price of continued funding with "
            "unshakeable calm: 'I believe that a twenty percent increase in funding would be sufficient "
            "for the next month, Mr. Carroll. After that, who can say?'"
        ),
        "notes": "C.O.D. Learns midway through Carroll's boasting that the 'dragon incident' plot is real, and, well aware that 'even oyabuns fear the anger of great dragons,' immediately tries to recover the egg to avoid Masaru's wrath -- hiring the 405 Hellhounds to trail the runners and later sending a three-operative strike team (Eichi, Sato, Reiko) to steal it back.",
    },
    {
        "name": "Masaru",
        "role": "Young great eastern dragon whose stolen egg drives the entire C.O.D. plot",
        "archetype": "Great Dragon",
        "title": "Great eastern dragon, Vancouver Island",
        "race": "Dragon",
        "gender": "Male",
        "connection": 2,
        "description": (
            "A young dragon confronted downtown in human 'salaryman' form, agitated and barely holding "
            "his fury in check -- alert runners sense the dragon's true nature and barely controlled "
            "rage before he ever transforms. His egg -- a new life, spiritual solace, proof of his "
            "adulthood, 'flesh of his flesh' -- is stolen from his caved-in Vancouver Island lair while "
            "he lies unconscious from a specially engineered Stun Masaru spell."
        ),
        "notes": (
            "C.O.D. B20 Q10x3 S40(12 human) C8(6) I8 W10, Ess11, Reaction9, Initiative9+7D6, "
            "Threat/Professional6(7 when defending the egg)/4, attacks +3 Reach/15D damage; Sorcery9; "
            "Hardened Armor, Enhanced Senses (low-light/thermal/wide-band hearing), Human Form, Noxious "
            "Breath; spells Barrier, Powerball, Ram, Analyze Truth, Heal, Mana Barrier, all Force 10. "
            "Gives the runners one chance to surrender the egg peacefully before Flaming Sword snipers "
            "force the confrontation into open combat and he assumes true form."
        ),
    },
    {
        "name": "Rob Sewall",
        "role": "'Captain' of the Flaming Sword squad secretly guarding -- and under orders to eventually kill -- the runners and the stolen dragon egg",
        "archetype": "Paramilitary Leader",
        "title": "'Captain', Flaming Sword",
        "race": "Human",
        "gender": "Male",
        "organization": "Flaming Sword",
        "connection": 3,
        "description": "A walking poster child for the Flaming Sword -- has always enjoyed beating anyone weaker than him, and learned early that his brutality earned him praise and rewards whenever the target was 'socially undesirable' metahumans. Politics do not much interest him; to Sewall, metahumans deserve to get stomped on simply for not being 'like him and his friends'.",
        "background": "Formerly a member of the Humanis Policlub; found a real home in the Flaming Sword, the paramilitary arm of the Human Nation, where the honorary rank of 'Captain' lets him play soldier while obeying orders that usually let him kill metahumans. A homicidal psychopath, but not a stupid one -- willing to hold his fire in the interest of advancing the anti-metahuman cause.",
        "notes": (
            "C.O.D. B5 Q5(6) S5(6) C3 I3 W5, Ess3.25, Reaction4(6), Initiative4(6)+2D6; Athletics4, "
            "Car4, Firearms6, Leadership3, Stealth6, Unarmed Combat5; boosted reflexes2, muscle "
            "replacement1, smartlink; Colt Manhunter with smartgun link, Walther WA-2100 sniper rifle "
            "with smartgun link, secure Ultra-Vest(4/3), portable phone, signal locator(5) tuned to the "
            "tracker hidden in the egg case. Leads eight snipers hidden on rooftops around the Redmond "
            "firehouse, each carrying explosive ammunition saved for the confrontation with Masaru. "
            "Under standing orders to destroy Masaru, the egg and the runners together at the final "
            "delivery to erase all evidence of the Human Nation's plot."
        ),
    },
    {
        "name": "Twiggs",
        "role": "Elf street samurai leading the transport team that steals Masaru's egg and hands it off to the runners",
        "archetype": "Street Samurai",
        "title": "Team leader, egg-theft transport crew",
        "race": "Elf",
        "gender": "Male",
        "connection": 1,
        "description": "Brusque and all business, gives nothing away about the job or the client: 'Sorry, chummers, but if Mr. Johnson wanted you to know, he would've told ya.' Wants distance from the egg the moment it's handed off, anxious to get his badly wounded team mage medical attention before Masaru can catch up with them.",
        "notes": "C.O.D. Uses the Elf Street Samurai archetype with Intelligence 5 (Reaction 6/10, Initiative 10+3D6); his team includes an elven hitman, a troll street samurai, a rigger, and the wounded mage. Flies out immediately after the handoff.",
    },
    {
        "name": "Eichi",
        "role": "Yakuza strike team leader sent to steal Masaru's egg back from the runners' safehouse",
        "archetype": "Physical Adept",
        "title": "Team leader, yakuza egg-recovery strike team",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Yakuza (Watada-rengo)",
        "connection": 2,
        "description": "A skilled physical adept swordsman who deals with his team's mistakes harshly but earns their respect for it, and in turn defers to their judgment in areas where their expertise exceeds his own. Gives nothing away if captured and interrogated.",
        "notes": "C.O.D. Magic9, Initiate Grade3; page's stat columns are badly garbled by OCR damage that mixes his block with the Flaming Sword org write-up -- treat exact attribute numbers as uncertain. Uses Improved Ability (Armed Combat) and Increased Reflexes, and fights with a katana.",
    },
    {
        "name": "Sato",
        "role": "Yakuza mage on the egg-recovery strike team, protects the egg with conjured elementals",
        "archetype": "Mage",
        "title": "Team mage, yakuza egg-recovery strike team",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Yakuza (Watada-rengo)",
        "connection": 1,
        "description": "Keeps a Force 5 air elemental and a Force 5 earth elemental standing by at all times, feeling strongly about redeeming the theft of the dragon's egg; the earth elemental physically carries the egg once recovered while the air elemental stands guard over it.",
        "notes": "C.O.D. Conjuring4, Sorcery6, Initiate Grade1; spells Mana Dart, Combat Sense, Detect Enemies, Detect Life, Increase Reflexes (quickened), Treat, Chaos, Improved Invisibility, Mask, Magic Fingers, Shadow; form-fitting body armor, Power Focus (1) ring, an SMG with sound suppressor.",
    },
    {
        "name": "Reiko",
        "role": "Female cybered soldier on the yakuza egg-recovery strike team, conscious of the extra scrutiny her gender draws in the organization",
        "archetype": "Street Samurai",
        "title": "Soldier, yakuza egg-recovery strike team",
        "race": "Human",
        "gender": "Female",
        "nationality": "Japanese",
        "organization": "Yakuza (Watada-rengo)",
        "connection": 1,
        "description": "Plays strictly by the book, well aware of the extra scrutiny her gender draws in a male-dominated organization, but will go out of her way to prove her ability if she thinks a mission is going soft on her account.",
        "notes": "C.O.D. B4 Q6(9) S4(5) C4 I6 W4, Ess1.58, Reaction6(10); Armed Combat5, Athletics4, Biotech4, Car6, Firearms6, Stealth5, Unarmed Combat5; alpha-grade cybereyes (electronic magnification/flare compensation/low-light/thermographic), muscle replacement, retractable spurs, smartlink, wired reflexes2. Ares Predator II with smartgun link, Ingram Smartgun with smartgun link, Toyota Elite.",
    },
    {
        "name": "Burt Aronson",
        "role": "Seattle Humanis Policlub organizer who disguises himself as an elf 'Mr. Johnson' to hire runner teams as frame-up patsies",
        "archetype": "Con Man",
        "title": "Chapter organizer, Humanis Policlub (Seattle)",
        "race": "Human",
        "gender": "Male",
        "age": 39,
        "organization": "Humanis Policlub",
        "connection": 4,
        "description": (
            "Tall and slender, passing convincingly for a slightly-burlier-than-average elf; wears "
            "whitish-blond hair at collarbone length, usually in a braid or ponytail, and moves "
            "gracefully with a flair for style, corporate or street. Highly intelligent but "
            "fundamentally cold and unfeeling underneath a warmth he can project convincingly when it "
            "serves him -- extremely sensitive people find him creepy without ever quite being able to "
            "say why. If pressed on the family-dispute cover story, he stonewalls smoothly: 'family "
            "business is family business, not your business -- or else.'"
        ),
        "background": "Radicalized by an ork-caused tragedy in his youth (the book's own 'Night of Rage' framing); rose to run Seattle's local Humanis operations and has spent years pitting different metahuman factions against each other and against humans, culminating in the Kinsey Zandras kidnapping.",
        "notes": (
            "Double Dipping. B4 Q5 S5 C6 I5 W6, Ess5.4; cybereyes, datajack, smartlink; Beretta 101T. "
            "Hires the runners to kidnap Kinsey Zandras, disguised as an elf; leaks the security "
            "footage himself to spark metahuman-on-metahuman riots, then uses the kidnapping to "
            "blackmail Malcolm Zandras's shipping routes for gun-running into Salish-Shidhe territory. "
            "Records every operation on a chip labeled 'Urban Brawl Scores' as leverage with his own "
            "superiors."
        ),
    },
    {
        "name": "Kinsey Zandras",
        "role": "BTL-addicted ork socialite kidnapped as bait for Burt Aronson's frame-up scheme",
        "archetype": "Socialite",
        "title": "Daughter of Malcolm Zandras, president of Zandras Shipping",
        "race": "Ork",
        "gender": "Female",
        "organization": "Zandras Shipping",
        "connection": 2,
        "description": "Wealthy, reckless, seriously addicted to illegal BTL chips -- a habit her father's security team works hard to keep others from exploiting. When 'chipped up' on a Neal the Ork Barbarian recording, dressed in synth-leather trousers and a fur halter top, she is savage, pumped up, flailing her arms and taking names, ready to fight any interruption with genuine ferocity.",
        "notes": "Double Dipping. B6 Q4 S5 C5 I4 W5, Ess5.8, Threat/Professional (1/4)/1(2) depending on BTL state; Etiquette(Corporate)4, Etiquette(Street)3, Firearms2, Negotiation4, Unarmed Combat3; datajack. Held by Aronson shapechanged into a lizard and warded in his lieutenant Vander Peterson's room; a Stun or Physical hit snaps her out of her BTL delusion.",
    },
    {
        "name": "Malcolm Zandras",
        "role": "President of Zandras Shipping and Kinsey's father -- Burt Aronson's real blackmail target",
        "archetype": "Corporate Executive",
        "title": "President, Zandras Shipping",
        "race": "Ork",
        "gender": "Male",
        "organization": "Zandras Shipping",
        "connection": 3,
        "description": "Built one of Seattle's most successful metahuman-owned businesses on exclusive Salish-Shidhe shipping routes that plenty of bigger companies covet.",
        "background": "Aronson's real target: kidnapping Kinsey is meant to blackmail Zandras into letting Humanis smuggle weapons along his shipping routes into Salish-Shidhe territory.",
        "notes": "Double Dipping. Offers the runners a flat 2,000 nuyen each for Kinsey's safe return, non-negotiable.",
    },
    {
        "name": "Emily Daly",
        "role": "Kinsey Zandras's ork housemate and best friend, co-host of the party the kidnapping is staged during",
        "archetype": "Socialite",
        "title": "Kinsey Zandras's housemate",
        "race": "Ork",
        "gender": "Female",
        "connection": 1,
        "description": "Another well-off young ork; spends the party on the back deck listening to music with friends, unaware of what is about to happen to her roommate. If the runners return after the party has broken up, she is downstairs cleaning up bottles and paper plates with a couple of friends.",
        "notes": "Double Dipping. Present but not directly involved in the snatch; a natural source for the runners to case Kinsey's routine.",
    },
    {
        "name": "Jameson",
        "role": "Adept head of the Zandras household security team -- a street veteran turned legitimate professional",
        "archetype": "Adept",
        "title": "Head of security, Zandras household",
        "race": "Human",
        "gender": "Male",
        "organization": "Zandras Shipping",
        "connection": 2,
        "description": "A former street operator now running Kinsey's protection detail, all business at all times; runs a running commentary on his transceiver to the rest of the guard team, coordinating them like the professional he is, and thinks fast on his feet when trouble starts.",
        "notes": "Double Dipping. Magic6, Willpower5(8); combat spell focus, spell locks (Increase Reflexes +2, Increase Willpower +3); spells include Slay Elf, Slay Human, Spirit Bolt, Stun Bolt, Stunblast, Increase Reflexes, Increase Willpower, Treat, Confusion, Improved Invisibility, Personal Bullet Barrier, Personal Spell Barrier. Notices out-of-place questions about the 'Party Room' and tips off the rest of the team.",
    },
    {
        "name": "Fred (Zandras Guard)",
        "role": "Heavily cybered ork member of the Zandras security team -- a loose cannon who loves full-auto noise and is unexpectedly shy around partygoers",
        "archetype": "Security Guard",
        "title": "Security, Zandras household",
        "race": "Ork",
        "gender": "Male",
        "organization": "Zandras Shipping",
        "connection": 1,
        "description": "Belligerently proud of his rough-neighborhood roots; the most heavily cybered guard on the team, prefers full-auto HK227 bursts because he likes the noise. Unexpectedly shy around attractive women, which makes guarding some of Kinsey's party girls awkward for him -- but he does his best to keep them safe regardless. Considers human partner Mandy his best friend, privately thinking of her as 'different' from other humans.",
        "notes": "Double Dipping. B8(11) Q4(13) S8(10) C2 I4 W4, Ess.1, Reaction4(13); Firearms5(Submachine Guns7), Stealth4, Throwing Weapons4, Unarmed Combat5(Retractable Spurs8); dermal plating3, reaction enhancer+3, smartlink II, wired reflexes2; muscle augmentation3, enhanced articulation, reflex recorder (SMGs); armor jacket(5/3), Colt Manhunter, HK227 with gas-vent IV, flash grenades. Acts before calling for backup, showing off for the rich kids at the party.",
    },
    {
        "name": "Mandy",
        "role": "Human close-combat specialist on the Zandras security team, keeps her over-wired partner Fred from getting too reckless",
        "archetype": "Security Guard",
        "title": "Security, Zandras household",
        "race": "Human",
        "gender": "Female",
        "organization": "Zandras Shipping",
        "connection": 1,
        "description": "Short, stocky and powerfully built; a tough, loyal fighter who wields her katana with deadly precision and has been Fred's partner and buddy for years -- keeping him from getting too crazy is practically her second job.",
        "notes": "Double Dipping. B6 Q6(9) S5(8) C5 I5 W6, Ess5.1, Reaction5(10), Body Index5.75; Armed Combat4(5)(Katana7[8]), Etiquette(Street)4, Firearms6, Stealth4, Throwing Weapons4; reaction enhancer+3; muscle augmentation3, orthoskin3, reflex recorder(Armed Combat), synaptic accelerator2; armor jacket(5/3), Colt Manhunter with explosive ammo and laser sight, three flash grenades, forearm guards, katana with Dikote.",
    },
    {
        "name": "Counterweight",
        "role": "Young ork rookie on the Zandras security team who idolizes teammate Fred",
        "archetype": "Security Guard",
        "title": "Security, Zandras household",
        "race": "Ork",
        "gender": "Male",
        "organization": "Zandras Shipping",
        "connection": 1,
        "description": "A recent recruit from Fred's own rough neighborhood, recommended for the job by Fred himself; makes up for a lack of street experience with enthusiasm, right down to installing cyberware similar to Fred's. Bored at his post on a stool near the top of the stairs, he happily chats with anyone who approaches -- an easy in for social runners -- and hasn't yet heard Kinsey scream under the influence of her Neal the Ork Barbarian chip.",
        "notes": "Double Dipping. B6 Q4 S8 C3 I4 W4, Ess3.2, Reaction4(8); Armed Combat4(Spurs6), Firearms5, Stealth3; retractable spurs, smartlink, wired reflexes1; armor jacket(5/3), Ares Predator, HK227.",
    },
    {
        "name": "Derrick",
        "role": "Troll leader of a New Weathermen cell who confronts the runners to find out the truth about Burt Aronson",
        "archetype": "Street Samurai",
        "title": "Cell leader, New Weathermen",
        "race": "Troll",
        "gender": "Male",
        "organization": "New Weathermen",
        "connection": 2,
        "description": (
            "Cold and flat-voiced when the confrontation opens, flanked by two elves and backed by "
            "thirty-plus more Weathermen pouring out of the dark: 'You've been asking a lot of "
            "questions about the Zandras kidnapping. We'd like to know why. You give us the whole truth "
            "and we just might let you walk away -- maybe. But you can't lie. I can smell lies. You "
            "play any kind of stupid game with us, we'll break every bone in your motherfragging "
            "bodies. Do we have an understanding here?' Once satisfied of the runners' innocence, turns "
            "instantly candid: 'Aronson's no elf. He's a fragging racist pinkskin. He's in with Humanis "
            "real deep.'"
        ),
        "background": "Has taken a personal interest in Burt Aronson for some time, suspecting him of orchestrating the Kinsey Zandras kidnapping based on rumor and pattern-matching against Aronson's known tactics.",
        "notes": "Double Dipping. Uses the Street Samurai archetype modified for a troll. Brings thirty-six New Weathermen to the confrontation; if convinced of the runners' innocence, reveals Aronson's real identity and urges them to rescue Kinsey.",
    },
    {
        "name": "Gilby Rellets",
        "role": "Elf investigative reporter who trades the runners a way to clear their names for their exclusive story",
        "archetype": "Reporter",
        "title": "Metahuman-beat reporter, Underground News",
        "race": "Elf",
        "gender": "Male",
        "connection": 3,
        "description": (
            "Skinny, scruffy, intense; approaches the runners' table at the Last Drop after watching "
            "them for ten minutes: 'Listen up, chum. You don't know me, but you will. I know you've "
            "been asking around about the Zandras snatch, and I've got a hunch that you've got a story "
            "to tell...' and later, direct: 'I know who you are. I can help you -- but it'll cost you. "
            "Mind if I sit down?' Loves his job and believes it can genuinely help metahumanity."
        ),
        "background": "Has spent years working the metahuman beat for the Underground News bureau, building a considerable arsenal of contacts and influence within the metahuman community; the Zandras kidnapping and its fallout have him on the story around the clock, and it has made him an unofficial 'voice of metahumanity' in Seattle.",
        "notes": (
            "Double Dipping. B3 Q5 S3 C6 I6 W5, Ess3.4; Athletics3, Computer4, Etiquette(Street)4, "
            "Firearms3, Negotiation4, Reporting5, Stealth(Urban)4; cyberears (recorder), cybereyes "
            "(camera/low-light/thermographic), chipjack, datajack, headware memory(100 Mp); armor "
            "clothing, Beretta 101T, pocket secretary. Offers the runners anonymity and Aronson's "
            "safehouse location in exchange for their story and any evidence of Humanis involvement; "
            "marked for death by Aronson's enforcer Shelly once she recognizes him."
        ),
        "contact_skills": ["Seattle metahuman-rights journalism and street sources"],
    },
    {
        "name": "Shelly",
        "role": "Burt Aronson's cybered enforcer, sent to silence Gilby Rellets and the runners as loose ends",
        "archetype": "Enforcer",
        "title": "Enforcer, Humanis Policlub (Seattle)",
        "race": "Human",
        "gender": "Female",
        "organization": "Humanis Policlub",
        "connection": 2,
        "description": "Aronson's go-to muscle for tying off loose ends; recognizes Gilby Rellets the instant she and her squad storm the Last Drop and personally marks him for death as Humanis's most-wanted reporter.",
        "notes": "Double Dipping. B5(8) Q5 S4 C2 I5 W5, Ess2, Reaction5(7); Armed Combat6, Firearms6, Stealth4; dermal armor4, smartlink, wired reflexes1; armor jacket(5/3), Colt Cobra with APDS ammo, Colt Manhunter. Karl's girlfriend -- if she dies, he will personally hunt whoever killed her.",
    },
    {
        "name": "Karl (Humanis Lookout)",
        "role": "Burt Aronson's cybered lookout at the safehouse hotel front desk -- Shelly's boyfriend",
        "archetype": "Enforcer",
        "title": "Lookout, Aronson's Redmond safehouse",
        "race": "Human",
        "gender": "Male",
        "organization": "Humanis Policlub",
        "connection": 1,
        "description": "Poses as a half-drunk barfly slumped in a hotel lobby chair, clutching a liquor bottle in a sagging stupor unless spoken to, while watching every arrival closely and unobtrusively.",
        "notes": "Double Dipping. B5(8) Q5 S4 C2 I4 W4, Ess1.6, Reaction4(6); Armed Combat5, Firearms6, Stealth4; dermal armor3, smartlink, wired reflexes1; Colt Cobra with APDS ammo, Colt Manhunter, lined coat, monofilament whip, transceiver. Alerts Aronson the moment the runners head upstairs; wants the runners dead if he learns they killed Shelly.",
    },
    {
        "name": "Kandle",
        "role": "Burt Aronson's chromed-to-the-max cyberwarrior enforcer, unshakably loyal to the death",
        "archetype": "Cyberwarrior",
        "title": "Chief enforcer, Humanis Policlub (Seattle)",
        "race": "Human",
        "gender": "Male",
        "organization": "Humanis Policlub",
        "connection": 2,
        "description": "So cybered and bioware-laden that he can barely keep himself together physically -- his body is 'so crammed full of parts not his own' the strain shows -- and unshakably devoted to Aronson regardless, ready to fight to the death on his say-so.",
        "notes": "Double Dipping. B6(8) Q6(12) S6(10) C2 I4 W6, Ess2 (mostly beta-grade), Reaction6(13), Body Index6; Armed Combat6, Athletics4, Firearms8, Stealth5, Unarmed Combat6; bone lacing (titanium), cybereyes (flare compensation/low-light/thermographic), move-by-wire system2, retractable spurs, smartlink II, image compensator2; enhanced articulation, muscle augmentation4, orthoskin2. Colt M22A2 with integral grenade launcher (mini concussion and flash grenades), Colt Manhunter, katana with Dikote, transceiver.",
    },
    {
        "name": "Vander Peterson",
        "role": "Burt Aronson's resident elemental adept mage, wards his room and keeps Kinsey Zandras shapechanged and bound",
        "archetype": "Elemental Adept",
        "title": "Resident mage, Humanis Policlub (Seattle)",
        "race": "Human",
        "gender": "Male",
        "organization": "Humanis Policlub",
        "connection": 2,
        "description": "An elemental adept with an affinity for earth, devoted to expanding his own power as much as keeping Aronson satisfied; lives and works in a candlelit room he has attuned specifically to his craft, shadows shifting across the walls as he concentrates.",
        "notes": (
            "Double Dipping. B4(5) Q4 S5 C4 I5 W4, Ess5, Magic6, Initiate Grade1; Conjuring6, Firearms4, "
            "Magical Theory4, Sorcery6; special centering skill Reciting Poetry (Edgar Allan Poe)4; "
            "elemental spell focus3, fetish focus3, spell locks (Personal Bullet Barrier4, Shadow3), "
            "Colt Cobra; spells Acid Bomb4(6)*, Acid Stream5, Barrier5(7), Bind5, Ice Sheet3, Mob "
            "Mood6, Personal Bullet Barrier4, Shapechange4 (*expendable fetish doubles Force). Anchors "
            "an Acid Bomb spell and a Bind spell in his own room's floor tiles, keeps a Background "
            "Count of 1 running, and conjures two Force 5 earth elementals for defense. Holds Kinsey "
            "shapechanged into a small lizard, leashed and warded against astral detection -- the "
            "spell collapses if he is knocked out before its sustaining period ends."
        ),
    },
    {
        "name": "Secret Service Agent Harris",
        "role": "General Yeats's Secret Service agent -- the last person he speaks to before slipping out alone to meet his killer",
        "archetype": "Secret Service Agent",
        "title": "Secret Service detail, General Franklin Yeats",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": (
            "Answers Yeats's summons with crisp professionalism -- 'Agent Harris. What can I do for "
            "you, sir?' -- and holds a soldier's 'at ease' stance even as his instincts flag something "
            "wrong. Pushes back, carefully, when Yeats orders him to keep the rest of the detail out of "
            "it: 'Sir, I can't...' -- and is cut off with 'You're not supposed to think. You're here to "
            "follow my orders and those of our superiors. We cannot risk exposure.' Nods and obeys."
        ),
        "notes": "Dead Run prologue only. Dismissed from the room before Yeats leaves alone for the Plaza Hotel; no stats given, one scene, never encountered by the runners.",
    },
    {
        "name": "General Franklin Yeats",
        "role": "Republican presidential candidate, secretly host to a Secret Hive wasp spirit -- murdered at the Plaza Hotel to open Dead Run",
        "archetype": "Politician",
        "title": "UCAS presidential candidate (Republican Party); running mate Anne Penchyk",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "A hawkish general-turned-candidate, slogan 'Rebuild America'; believed himself strong-"
            "willed enough to keep his campaign clean while secretly merged with an insect spirit for "
            "years without any outward sign. Found dead on his hotel bed, throat torn open to the "
            "windpipe -- his face intact, dark-skinned, looking maybe fifty or sixty. Alive, in the "
            "prologue, he dismisses the threat calmly to Agent Harris: 'Someone knows... enough to "
            "raise questions -- not enough to prove anything. But questions are the last thing we need "
            "in the middle of a presidential campaign... I'll handle it myself. My caller wants a "
            "face-to-face meeting at the Plaza Hotel -- tonight.'"
        ),
        "background": "Merged with a Secret Hive wasp spirit on a visit to Chicago before the Bug City crisis; the possession was exceptionally good, giving the spirit access to enough of Yeats's memory and personality to convincingly run for president as part of the Hive's plan to occupy the office by proxy.",
        "notes": "Dead Run. Lured to a private meeting at the Plaza Hotel by what he believes is a simple blackmailer -- his own running mate Anne Penchyk, an Empowerment Coalition agent. Killed there (his wasp-spirit host by a true-form mantis, his human body by Penchyk) minutes before the runners arrive for an unrelated meet and are framed for the murder.",
    },
    {
        "name": "Anne Penchyk",
        "role": "Ork vice-presidential candidate and Empowerment Coalition agent who orchestrated General Yeats's assassination",
        "archetype": "Politician",
        "title": "UCAS vice-presidential candidate (running with General Yeats)",
        "race": "Ork",
        "gender": "Female",
        "organization": "Empowerment Coalition",
        "connection": 4,
        "description": "Built a career on refusing to take no for an answer -- rebuilt her life and a marketing-consulting firm from scratch after an unexpected goblinization in her twenties, then became a genuine, respected voice for metahuman rights in Congress. Colleagues and staff have started noticing her grow cold and distant as the campaign wears on, chalking it up to strain rather than to what is really consuming her attention.",
        "background": (
            "Served multiple terms as a UCAS Representative for Wisconsin on metahuman-rights issues; "
            "met and became close friends with General Yeats over military-integration policy, and he "
            "tapped her as his running mate. Events of Casualties of War (the Super Tuesday adventure "
            "set) drew her into the Empowerment Coalition's orbit, and she has grown steadily colder "
            "and more consumed by the mantis spirits' agenda ever since -- while remaining, underneath "
            "it, still her own person."
        ),
        "notes": (
            "Dead Run. B6 Q3 S4 C4 I4 W4, Ess5, Reaction3; Administration4, Car2, Etiquette(Corporate)6, "
            "Etiquette(Media)4, Etiquette(Political)?, Leadership(Political)4, Marketing6, Negotiation6; "
            "chipjack, datajack, display link, headware memory(50 Mp). Lures Yeats to the fatal meeting, "
            "kills his human body once a true-form mantis kills the wasp spirit possessing him, and lets "
            "the runners take the fall for the murder to protect the Coalition's ongoing campaign against "
            "the Secret Hive. Whether she survives the Puyallup confrontation and clears the runners' "
            "names, or dies there, is left to the table."
        ),
    },
    {
        "name": "Scott Cohen",
        "role": "FBI special agent hunting the runners for Yeats's murder -- unknowingly himself a Secret Hive wasp-spirit host",
        "archetype": "FBI Agent",
        "title": "Special Agent, UCAS Federal Bureau of Investigation",
        "race": "Human",
        "gender": "Male",
        "organization": "UCAS Federal Bureau of Investigation",
        "connection": 3,
        "description": "An experienced, capable, well-regarded agent who came to know and admire General Yeats during the campaign's D.C. policy briefings -- which made him an ideal, unsuspecting target for Hive infiltration. Shows no outward sign of possession beyond a slight tendency toward moodiness and occasional trouble sleeping.",
        "background": "Merged with a wasp spirit by the Secret Hive shortly after Yeats noticed his admiration; the merge was excellent enough that Cohen shows almost no sign of it and returns to duty with no memory of the event.",
        "notes": (
            "Dead Run. B5 Q5(6) S5 C4 I5 W5, Initiative5(7)+1D6, Threat/Professional4/4; Armed Combat5, "
            "Car3, Etiquette(Corporate)3, Etiquette(Government)3, Firearms5, Unarmed Combat5; Browning "
            "Max-Power heavy pistol, lined coat, FBI identification. Reveals his true insect nature to "
            "fight for survival once the Empowerment Coalition's mantis spirits corner him at Eve "
            "Donovan's doss -- the moment that exposes the whole Secret Hive plot to his partner "
            "O'Rourke, if he lives to explain it, or to the runners if he doesn't."
        ),
    },
    {
        "name": "Meagan O'Rourke",
        "role": "FBI special agent and occult-trained mage, Cohen's partner, unaware her partner is a Secret Hive host",
        "archetype": "Mage",
        "title": "Special Agent, UCAS Federal Bureau of Investigation",
        "race": "Human",
        "gender": "Female",
        "nationality": "Irish",
        "organization": "UCAS Federal Bureau of Investigation",
        "connection": 3,
        "description": "Holds a master's degree in Occult Sciences from Georgetown; dynamic, driven, expects the same relentless work ethic from everyone around her, with a quick Irish temper that masks real dedication to the job.",
        "background": "Partnered with Cohen for about a year; their early friction gave way to a solid working friendship. Has no cause to suspect him of anything, though his caution around her has grown as the campaign wears on.",
        "notes": (
            "Dead Run. B3 Q4 S4 C5 I6 W5, Magic6(8), Initiate Grade1, Reaction5; Conjuring6, Sorcery6, "
            "Etiquette(Government)4, Etiquette(Street)6, Firearms5, Investigation?, Magical Theory4, "
            "Unarmed Combat3; spells Redirect5, Sleep4, Astral Sense3*, Clairvoyance3*, Mind Probe4, "
            "Heal4, Preserve5*, Stabilize3*, Improved Invisibility4, Bind5, Light3, Magic Fingers3, "
            "Seal4, Thunderclap5 (*fetish-required); datajack, display link, data management SPU, "
            "headware memory(50 Mp); Browning Max-Power, FBI identification, lined coat, portable "
            "phone, crystal-ball clairvoyance fetish, carved-ash health-spell fetish (Rating4 focus), "
            "silver-and-garnet power focus (Rating2) ring. Uses astral perception and elementals to "
            "hunt the runners; may end up heading the UCAS government's internal Secret Hive cleanup "
            "team if the truth comes out."
        ),
    },
]

ORG_UPDATES = {
    "Humanis Policlub": {
        "notes_append": (
            "Shadows of the Underworld -- Double Dipping: Seattle chapter organizer Burt Aronson (disguised "
            "as an elf) orchestrates the Kinsey Zandras kidnapping to spark metahuman-on-metahuman riots "
            "toward Kenneth Brackhaven's benefit and to blackmail Zandras Shipping's Salish-Shidhe routes "
            "into a weapons-smuggling pipeline. His safehouse doubles as a records vault of Humanis "
            "operations (evidence label: 'Urban Brawl Scores'), kept as leverage with his own superiors."
        ),
        "leadership_add": [{"name": "Burt Aronson", "title": "Chapter organizer, Seattle", "notes": "Disguises himself as an elf; runs the Kinsey Zandras frame-up."}],
        "enemies_add": ["New Weathermen", "October 25th Alliance"],
    },
    "Yamatetsu Corporation": {
        "notes_append": (
            "Shadows of the Underworld -- Two Solitudes: North America (San Francisco) branch employee Sho "
            "Kojima steals internal spreadsheets, later published by the October 25th Alliance as 'The "
            "Little Red Schoolhouse' -- proof that Yamatetsu's touted metahuman-friendly 'schools' are "
            "actually feeder pipelines to Central Valley testing labs. Corporate response blames a rogue "
            "mid-level manager, promotes Sho's father as the internal 'hero' who exposed it, and funnels "
            "PR nuyen into Oakland to blunt the fallout."
        ),
        "enemies_add": ["October 25th Alliance"],
    },
    "Saeder-Krupp Heavy Industries": {
        "notes_append": (
            "Shadows of the Underworld -- Two Solitudes: corporate watchman Nils Hammarand runs a "
            "blackmail-and-espionage network for Lofwyr out of the Angelic Entertainment shell subsidiary "
            "in Los Angeles, backed by physical adept assassin Schreck. Blackmailed Yamatetsu employee "
            "Sho Kojima into corporate espionage, indirectly triggering the birth of the free spirit Hiro "
            "and the Little Red Schoolhouse scandal."
        ),
    },
    "Mitsuhama Computer Technologies": {
        "notes_append": (
            "Shadows of the Underworld -- C.O.D.: mid-level manager Lawrence Carroll moonlights as a Human "
            "Nation operative, using his corporate cover to fund metahuman gang violence and orchestrate "
            "the theft of a young dragon's egg in a plot to publicly discredit Dunkelzahn's presidential "
            "campaign."
        ),
    },
    "405 Hellhounds": {
        "notes_append": (
            "Shadows of the Underworld -- C.O.D.: hired by yakuza fixer Isao Yamazaki to trail the stolen "
            "dragon egg's Seattle delivery without engaging; concealed their colors and dropped back "
            "rather than risk damaging the cargo."
        ),
    },
    "Red Hot Nukes": {
        "notes_append": (
            "Shadows of the Underworld -- C.O.D.: about two dozen dwarf gangers hired as a decoy assault on "
            "the runners' Redmond firehouse safehouse, drawing fire while a yakuza strike team tried to "
            "steal the dragon egg back through a rear window."
        ),
    },
    "Yakuza (Watada-rengo)": {
        "notes_append": (
            "Shadows of the Underworld -- C.O.D.: fixer Isao Yamazaki serves as Lawrence Carroll's Human "
            "Nation middleman, contracting gangs and a professional strike team (Eichi, Sato, Reiko) in a "
            "failed bid to recover Masaru's stolen egg and salvage the organization's standing with the "
            "dragon before violence engulfs downtown Seattle."
        ),
        "leadership_add": [{"name": "Isao Yamazaki", "title": "Fixer / Human Nation middleman", "notes": "Arranges gang and strike-team contracts; scrambles to recover the stolen dragon egg."}],
    },
    "King's Crimson": {
        "notes_append": (
            "Shadows of the Underworld -- Dead Run: leader Alan Corliss's honor-debt to fixer Eve Donovan "
            "means two gang members guard her Puyallup doss at all times; they escort the runners to a "
            "meeting that turns into a three-way confrontation with the Empowerment Coalition and the FBI."
        ),
    },
    "UCAS Federal Bureau of Investigation": {
        "notes_append": (
            "Shadows of the Underworld -- Dead Run: Special Agents Scott Cohen and Meagan O'Rourke hunt "
            "the runners for General Yeats's assassination. Cohen is revealed, mid-investigation, to be an "
            "unwitting Secret Hive wasp-spirit host; depending on how the case resolves, the Bureau (and "
            "the wider UCAS government) may quietly begin rooting out Hive infiltrators, potentially with "
            "O'Rourke leading the internal cleanup."
        ),
    },
    "Universal Brotherhood": {
        "notes_append": (
            "Shadows of the Underworld -- Dead Run: revealed as having been, in its day, a puppet of the "
            "insect-spirit Secret Hive; when Knight Errant's small nuclear device partially destroyed the "
            "Chicago Hive (see the novel 'Running Bright'), the shattered Brotherhood's surviving 'good "
            "merge' spirits went underground and began infiltrating governments directly, culminating in "
            "General Yeats's Hive-possessed presidential run."
        ),
    },
    "Salish-Shidhe Council": {
        "notes_append": (
            "Shadows of the Underworld -- Double Dipping: Humanis Policlub organizer Burt Aronson targets "
            "Zandras Shipping's exclusive Salish-Shidhe shipping routes as a weapons-smuggling pipeline "
            "for Humanis sympathizers within Council territory; the plot is foiled if the runners break "
            "the blackmail before it takes hold."
        ),
    },
}

LOC_UPDATES = {}

NPC_UPDATES = {
    "Eve Donovan": {
        "notes_append": (
            "Shadows of the Underworld -- Dead Run: unwittingly sets up the fatal Plaza Hotel meet between "
            "General Yeats and Anne Penchyk on behalf of the Empowerment Coalition, then goes to ground at "
            "her Puyallup doss (a third-floor walk-up guarded by King's Crimson, a new maglock and a "
            "telecom-linked camera she installed herself) once she realizes she was used. The Coalition's "
            "mantis spirits try to silence her as a loose end; the runners' arrival, and the FBI's raid "
            "moments later, turn the confrontation into a three-way fight that exposes Special Agent Scott "
            "Cohen's own Secret Hive possession."
        ),
    },
    "Alan Corliss": {
        "notes_append": (
            "Shadows of the Underworld -- Dead Run: still pays off his honor-debt to Eve Donovan by keeping "
            "King's Crimson members on her door around the clock; personally arranges the runners' meeting "
            "with her when they come looking for answers about General Yeats's murder."
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
Only one Matrix system in the book is built out in any detail:

**UC Berkeley student records** (Two Solitudes, p.32-33). Host is Green-4 with Rating 8 across all
subsystems, running Trace-4 IC. Holds Sho Kojima's academic file (straight-A student, glowing
professor comments) but nothing about his disappearance or his sexuality.

Everything else is name-only or explicitly out of scope: the Empire State Building's building
security system and Matrix log (Excelsior, referenced but never given host stats), the Whole Earth
Adventists' jammed comms (Dunkelzahn's own deckers do the jamming off-page), Pokerface's burned
Fuchi Cyber-4 deck, the Zandras townhouse's Matrix-linked but unrated camera system (Double
Dipping), and Aronson's evidence chip ('Urban Brawl Scores', no host -- just a datachip a team
decker can crack in minutes).
"""

NOT_BUILT = """
- **David Ryan's ("Pokerface's") burned cyberdeck** and **Twiggs's transport-team hitman, troll
  samurai, rigger and wounded mage** -- generic archetype fill-ins with no names of their own,
  summarized on Pokerface's and Twiggs's own rows.
- **The seven-plus generic Whole Earth Adventist terrorists** (human/elf/ork/troll Kamikaze-boosted
  stat block, Excelsior p.14-15) beyond the named cell members (Alicia, Fingers, Arthur, Noah,
  Chunk-Style, Napalm, Blood, Blade) -- unnamed mooks.
- **The Red Hot Nukes gang members, the Flaming Sword sniper squad and the Humanis Troops squads**
  (Double Dipping, C.O.D.) -- generic shared stat blocks with no individual names, summarized on
  their org rows.
- **The Republican, New Century and Technocratic Party staff** beyond the candidates themselves,
  **UCAS Secret Service** as an institution, and assorted trideo news anchors/reporters quoted
  across the book's handout-style prose -- pure atmosphere.
- **Sarah, Fred and Mandy's unnamed party-guest contacts, Kinsey's unnamed BTL companions in the
  Party Room, and the Alliance's unnamed 'floating' class instructors** -- nameless texture on the
  location rows.
"""

PLAY_NOTES = """
- The five adventures are genuinely standalone -- run any of them in any order, or run just one.
  Only loose continuity threads: Dead Run assumes (but does not require) the players' table has run
  "Super Tuesday!"'s "Casualties of War" and met Anne Penchyk and the mantis spirits there; if not,
  everything needed is recapped in Dead Run itself.
- Excelsior and Dead Run both put a version of "prove your innocence to armed federal agents while
  the real culprit has diplomatic-grade cover" in front of the players; play the pressure but keep
  both winnable -- neither adventure wants a TPK, per its own Debugging notes.
- C.O.D. and Double Dipping share a structure: an ostensibly simple job (babysit a package / snatch
  a rich kid) that is actually bait in someone else's political scheme, with a hidden third faction
  (Flaming Sword snipers / Humanis enforcers) watching the runners the whole time. Telegraph that
  the "simple" job is being professionally overwatched before the reveal -- Sewall's snipers and
  Aronson's tracking transmitter are both meant to be findable with careful play.
- Every adventure's antagonist org ties back to the same summer's presidential race: Whole Earth
  Adventists (pro-Dunkelzahn fanaticism), Human Nation/Flaming Sword and Humanis Policlub/New
  Weathermen (anti-metahuman backlash, both pro-Brackhaven), and the Secret Hive/Empowerment
  Coalition (a hidden insect-spirit proxy war for the Republican ticket). Use that thread to tie the
  book into an ongoing campaign even if you only run one or two of the five.
- Dead Run's reveal works best played close to the vest: let Cohen's possession surface only when
  he is physically cornered, and let O'Rourke's reaction (horror, then reassessment) do the dramatic
  work rather than an info-dump.
"""


# --- auto-converted: rows also created by super_tuesday.py become appends ---
_DUP_ORGS=['Human Nation']
ORGS=[o for o in ORGS if o['name'] not in _DUP_ORGS]
_DUP_NPCS=['Dunkelzahn', 'Kenneth Brackhaven', 'Arthur Vogel', 'Dr. Rozilyn Hernandez', 'James Booth', 'General Franklin Yeats', 'Anne Penchyk']
NPCS=[n for n in NPCS if n['name'] not in _DUP_NPCS]
_DUP_LOCS=[]
LOCATIONS=[l for l in LOCATIONS if l['name'] not in _DUP_LOCS]
ORG_UPDATES.update({'Human Nation': {'enemies_add': ['Dunkelzahn'],
                  'notes_append': 'Shadows of the Underworld: A wide-ranging fraternity of wealthy '
                                  'and powerful humans dedicated to eventually exterminating '
                                  'metahumanity. In Seattle its effort to swing public opinion '
                                  'behind Kenneth Brackhaven is run by MCT mid-level manager '
                                  'Lawrence Carroll, who pays metahuman gangs (through yakuza '
                                  'middlemen, to keep his own hands clean) to commit public mayhem '
                                  "for the trideo cameras. In response to Dunkelzahn's rising poll "
                                  "numbers, Carroll escalated to stealing a young dragon's egg and "
                                  "staging a public 'dragon attack' to discredit dragonkind and "
                                  "Dunkelzahn's candidacy at a stroke (C.O.D.). See the Threats "
                                  "sourcebook for the Human Nation's full national profile "
                                  '(cross-referenced but not detailed in this book).'}})
NPC_UPDATES.update({'Anne Penchyk': {'notes_append': 'Shadows of the Underworld: Built a career on refusing to take '
                                  'no for an answer -- rebuilt her life and a marketing-consulting '
                                  'firm from scratch after an unexpected goblinization in her '
                                  'twenties, then became a genuine, respected voice for metahuman '
                                  'rights in Congress. Colleagues and staff have started noticing '
                                  'her grow cold and distant as the campaign wears on, chalking it '
                                  'up to strain rather than to what is really consuming her '
                                  'attention. Served multiple terms as a UCAS Representative for '
                                  'Wisconsin on metahuman-rights issues; met and became close '
                                  'friends with General Yeats over military-integration policy, '
                                  'and he tapped her as his running mate. Events of Casualties of '
                                  'War (the Super Tuesday adventure set) drew her into the '
                                  "Empowerment Coalition's orbit, and she has grown steadily "
                                  "colder and more consumed by the mantis spirits' agenda ever "
                                  'since -- while remaining, underneath it, still her own person. '
                                  'Dead Run. B6 Q3 S4 C4 I4 W4, Ess5, Reaction3; Administration4, '
                                  'Car2, Etiquette(Corporate)6, Etiquette(Media)4, '
                                  'Etiquette(Political)?, Leadership(Political)4, Marketing6, '
                                  'Negotiation6; chipjack, datajack, display link, headware '
                                  'memory(50 Mp). Lures Yeats to the fatal meeting, kills his '
                                  'human body once a true-form mantis kills the wasp spirit '
                                  'possessing him, and lets the runners take the fall for the '
                                  "murder to protect the Coalition's ongoing campaign against the "
                                  'Secret Hive. Whether she survives the Puyallup confrontation '
                                  "and clears the runners' names, or dies there, is left to the "
                                  'table.'},
 'Arthur Vogel': {'notes_append': 'Shadows of the Underworld: A dwarf eco-lawyer running with an '
                                  "unnamed troll Eagle shaman as his VP pick -- 'now there's an "
                                  "image!' says the trideo coverage, adding that the pair are "
                                  "'smart, savvy, articulate' rather than the usual crackpot "
                                  "tree-huggers, and 'just might have a shot at the Big Chair -- "
                                  "assuming no nasty skeletons come popping out of lawyer Vogel's "
                                  "closet.' Slogan: 'Save the Earth'. Excelsior campaign-poll "
                                  'blurb (p.7) only; no direct scene. Trails the frontrunners in '
                                  'early summer polling.'},
 'Dr. Rozilyn Hernandez': {'notes_append': 'Shadows of the Underworld: Billed by the trideo '
                                           "coverage as offering 'better living through electing "
                                           "mage-o-crat Roz and her gorgeous simstar veep' -- "
                                           'running mate Ramsay McMulkin, dismissed in the same '
                                           "breath as 'pretty, but can he type?' Slogan: 'Our "
                                           "Magical Future'; courts both 'magical goombahs and "
                                           "techno-weenies' in one ticket. Excelsior campaign-poll "
                                           'blurb (p.7) only; no direct scene.'},
 'Dunkelzahn': {'notes_append': 'Shadows of the Underworld: A silver-and-azure great dragon whose '
                                "2012 first Awakened appearance -- 'the beating of his silver and "
                                "azure wings created the freshening air' -- inspired Jaelle Lester "
                                'to found the Church of the Whole Earth; forty-five years later he '
                                "is a serious UCAS presidential contender, running on 'A New "
                                "Golden Age'. Never directly on stage in this book, but his "
                                'authority is felt in every scene involving his staff or his '
                                "enemies: he does not approve of the Whole Earth Adventists' "
                                "violence and badly underestimates them. Runs his campaign's New "
                                'York security consulting through staffer Martha Delaney and keeps '
                                'a team of skilled deckers watching over his Matrix presence at '
                                'all times. Excelsior: authorizes Delaney to offer the runners up '
                                'to 100,000 UCAS dollars each to defuse the Whole Earth '
                                "Adventists' hostage siege without public bloodshed or exposure; "
                                'his agents track down and remember any runner who takes his money '
                                'and then abandons the job. C.O.D.: the real target of Lawrence '
                                "Carroll's dragon-egg plot -- a public Masaru rampage is meant to "
                                "tank Dunkelzahn's poll numbers by association. Poll standing in "
                                "the book's news blurbs: 22 percent, behind Brackhaven's 24."},
 'General Franklin Yeats': {'notes_append': 'Shadows of the Underworld: A hawkish '
                                            "general-turned-candidate, slogan 'Rebuild America'; "
                                            'believed himself strong-willed enough to keep his '
                                            'campaign clean while secretly merged with an insect '
                                            'spirit for years without any outward sign. Found dead '
                                            'on his hotel bed, throat torn open to the windpipe -- '
                                            'his face intact, dark-skinned, looking maybe fifty or '
                                            'sixty. Alive, in the prologue, he dismisses the '
                                            "threat calmly to Agent Harris: 'Someone knows... "
                                            'enough to raise questions -- not enough to prove '
                                            'anything. But questions are the last thing we need in '
                                            "the middle of a presidential campaign... I'll handle "
                                            'it myself. My caller wants a face-to-face meeting at '
                                            "the Plaza Hotel -- tonight.' Merged with a Secret "
                                            'Hive wasp spirit on a visit to Chicago before the Bug '
                                            'City crisis; the possession was exceptionally good, '
                                            "giving the spirit access to enough of Yeats's memory "
                                            'and personality to convincingly run for president as '
                                            "part of the Hive's plan to occupy the office by "
                                            'proxy. Dead Run. Lured to a private meeting at the '
                                            'Plaza Hotel by what he believes is a simple '
                                            'blackmailer -- his own running mate Anne Penchyk, an '
                                            'Empowerment Coalition agent. Killed there (his '
                                            'wasp-spirit host by a true-form mantis, his human '
                                            'body by Penchyk) minutes before the runners arrive '
                                            'for an unrelated meet and are framed for the murder.'},
 'James Booth': {'notes_append': "Shadows of the Underworld: 'Slick Jimmy and his suit' -- a "
                                 "ticket, the trideo blurb sneers, 'only their mothers could "
                                 "love'; a former vice president trying to trade on "
                                 "incumbency-adjacent status. Slogan: 'The Status Quo'. Excelsior "
                                 'campaign-poll blurb (p.7) only; no direct scene. Polling weakest '
                                 'of the six named candidates, roughly tied with Undecided.'},
 'Kenneth Brackhaven': {'notes_append': "Shadows of the Underworld: Slogan: 'A Holy War for the "
                                        "Soul of the Nation'. A polished, confident stump speaker "
                                        "-- 'We can take our streets and our schools back from "
                                        'those who are using the weakness and fear of our '
                                        'so-called leaders against us... together, we can restore '
                                        'to this country the greatness that has always been, and '
                                        "will always be, its birthright' -- who draws a deafening "
                                        'trideo-audience roar even through the dampers. Polling '
                                        'ahead of the field at 24 percent on the strength of '
                                        'fear-mongering about magic and metahumanity. C.O.D.: '
                                        'Human Nation operative Lawrence Carroll funds street '
                                        'violence and the dragon-egg plot specifically to boost '
                                        "Brackhaven's numbers at Dunkelzahn's expense, financed "
                                        'partly through yakuza contact Isao Yamazaki. Double '
                                        "Dipping: Burt Aronson's Humanis cell runs the Kinsey "
                                        'Zandras frame-up toward the same end -- discrediting '
                                        'metahumanity broadly enough that undecided voters break '
                                        'for Brackhaven.'}})
LOC_UPDATES.update({})
