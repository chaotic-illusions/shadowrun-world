# SRM 01-07 Keys to the Asylum (FanPro/WizKids, 2005, SR3) -- campaign order #50. Puyallup (Caring
# Gardens, a full city block), with the hiring meet in the back room of Matchstick's jazz club.
# SETTING NOTE: this is a SEATTLE adventure, not a Denver one, and it is Shadowrun Third Edition,
# not SR4. Shadowrun Missions Season 1 is the Rose Croix story arc and runs in the Seattle
# metroplex: the meet is "at Matchstick's jazz club, as detailed in either edition of the Seattle
# Sourcebook", Caring Gardens is "in Puyallup", the metroplex guard and elite officer stat blocks
# are cited from New Seattle pp.113-114, and Neil O'Malley worked fifteen years "as a public defense
# attorney with the city of Seattle". Every location row is therefore city "Seattle".
# Dating: no in-world date is printed. The book is written for SR3, refers to "the way the world
# works in the '60s", and was published in 2005, so the campaign year is 2064 (matching SRM 00-01
# Mission Briefing and SRM 01-01 Double Cross). The adventure runs from a 02:00 phone call and a
# 02:30 meet through a single night, against a 24-hour deadline before Mr. Johnson expects the story
# to break.
# Book editing inconsistencies, noted on the affected rows:
#   * the sim star is "Levine, Shannon" on the Handout 1 patient roster, but the cast text says both
#     her room door and the patient list the runners are given read "Sharon Vine";
#   * Handout 1 lists "Woods, John, Ork, Male" where the cast entry is "Jack Woods, Orc Male";
#   * Mr. Johnson says ten employees were scheduled on duty tonight, while Handout 2 lists a
#     twenty-six-name employee roster;
#   * the book itself warns that "some of the information in these files is deliberately
#     contradictory with information contained in later scenes" and that the Matrix access codes
#     Mr. Johnson supplies are out of date -- these are intentional, not errata;
#   * the Awarding Karma table prints "Stopping Dr. Heffernan from controlling the facility" twice,
#     for 1 point and for 2 points without resorting to violence;
#   * Trey "Boltar" Harris gets a full personality write-up and no stat block at all;
#   * Heffernan's Magic is printed 8(10) and disrupting Mindgloom costs him "2 points of his magic
#     rating. (Reducing it to 6.)";
#   * the book uses "Orc" where the line normally prints ork, and misspells therapy as "therarpy"
#     twice;
#   * the employee roster includes "Adams, Douglas, Elf, Office Manager", an author in-joke.
# Cross-spec note: Rose Croix and Walter Broward (as Michael Davenport) are created by
# specs/srm_01_01_double_cross.py and are appended to here, never re-created; DocWagon, Ares
# Macrotechnology, Lone Star Security, the Universal Brotherhood, Universal Omnitech, Transys
# Neuronet and Matchstick's already exist and are likewise updated. This adventure introduces no new
# organization of its own -- everything in it belongs to Rose Croix -- so ORGS is empty by design.
# Source text: docs/Adventures/text/SRM01-07A_Keys_to_the_Asylum.txt (21 pages) and
# docs/Adventures/text/SRM01-07B.txt (player aids, 11 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "SRM 01-07 Keys to the Asylum"
ORDER = 50
SOURCE = "SRM01-07A_Keys_to_the_Asylum.pdf, pp. 3-21; SRM01-07B.pdf (Player Aids), pp. 2-11"
YEAR = "2064"

SYNOPSIS = """
Rose Croix grew too fast. Racing to compete with DocWagon from a standing start, it cut corners,
and the corner it cut was the background check on **Dr. Alex Heffernan**. He presented a premiere
psychiatrist's curriculum vitae -- senior posts at research hospitals, publications in the best
journals, personal references from executives at Transys Neuronet and Universal Omnitech -- and he
interviewed beautifully. Most of it would have collapsed under a cursory check. Rose Croix never
even did that, because it had just bought a state-owned sanitarium, renamed it **Caring Gardens**,
and needed it turning a profit immediately. Instead of an expert physician they got a corrupted
mage holding the keys to the asylum.

For weeks Heffernan has been running "alternative treatments" on the patients -- adjusted
medications, electroshock, leechings, new magical techniques -- all of it preparation for a ritual.
Tonight he finished it: he summoned the shadow free spirit **Mindgloom**, whose true name he spent
weeks researching, and bound it into a spirit pact. The binding went wrong enough that the magical
feedback knocked the facility's electronics off-line, severed the telecom, the power and the LTG,
and left a Force 4 astral barrier around the grounds and a Background Count of 2 inside them. Then
Heffernan improvised: two guards called into his office and put under Control Actions, most of the
staff and patients rounded up and held under a sustained Mob Mind, and the three-man **High Threat
Response** team Rose Croix sent in taken personally.

At 02:00 each runner's fixer calls: a Mr. Johnson has asked for them by name, 1,000 nuyen just for
turning up, back room of **Matchstick's** in half an hour. The Johnson is **Walter Broward**, CEO of
Rose Croix -- the man they "assassinated" in *Double Cross*, now behind a new face -- and he needs
deniable people because patients may die. Fifteen patients at 200 nuyen a head, ten employees plus
the HTR team at 200 each, 1,000 for the security records, 1,000 for the experimental data, 1,500 for
the opposition alive and interrogable or 500 dead. Twenty-four hours, no media, no Lone Star.

Inside the wall the team walks a dark three-storey hospital full of people who are not what they
appear: a terrified ork repairman barricaded in the boiler room, a man who believes he is possessed
by an insect spirit crawling along the drop ceilings, a sixteen-year-old otaku convulsing at the
mention of her treatment, a burned-out sim star in the DTs, a public defender who thinks he is the
director's right-hand man, two ex-military nurses improvising weapons, a Desert Wars veteran on
patrol with his cyberspur popped, and an OCD engineer clutching a flashlight. Above them, on the
third floor, Heffernan waits with sixteen thralls at his back and three bribes in his mouth.
"""

TIMELINE = """
- **A few months ago** -- Rose Croix buys a state-owned sanitarium, renames it Caring Gardens, tunes
  up the facilities, replaces several employees and refocuses it on high-margin clients: twenty
  beds, high-profile patients with stress-related psychoses or addiction problems.
- **Shortly after** -- Dr. Alex Heffernan is hired as director on a fraudulent CV that nobody
  checks. He spends his first weeks learning the patients, the staff and the systems.
- **The following weeks** -- he starts adjusting medications and introducing alternative treatments:
  electroshock (through Brianne Tillers's datajack), leechings, "new" magical techniques, forced sims
  in which Jack Woods watches his comrades die, submersion in a vat of insects for Kevin Cooper. He
  also spends the time researching Mindgloom's true name.
- **Tonight, about 22:00** -- Heffernan completes the summoning and binds Mindgloom into a spirit
  pact, becoming a fully corrupted mage. The feedback knocks the facility off-line and raises the
  astral barrier.
- **Four hours before the meet** -- routine checks show the telecom, power and Matrix connections all
  severed. An astral sweep by a Rose Croix security mage finds a barrier that is not in the corporate
  plan.
- **Three and a half hours before the meet** -- a three-member HTR team crosses the perimeter and the
  astral barrier. Nothing more is heard from them; Heffernan deals with them personally.
- **Meanwhile inside** -- two guards are called into the office and put under Control Actions with
  Force 5 sustaining foci worn as bandage headbands; they round up most of the staff and patients,
  and Heffernan casts and sustains Mob Mind over them.
- **02:00** -- each runner's fixer calls. Mr. Johnson has asked for them personally; 1,000 nuyen for
  showing up.
- **02:30** -- the meet in Matchstick's back room. Broward's briefing, the goal-based fee schedule,
  the optional loan of the combat mage Trey "Boltar" Harris, badges, security files and out-of-date
  Matrix codes.
- **The rest of the night** -- the grounds, the complex, the Datasteal, and the Director's Office.
  The runners arrive much faster than Heffernan expected.
- **Within 24 hours** -- Broward does not believe he can keep the situation under wraps any longer
  than that.
- **After** -- if Heffernan escapes or is taken prisoner by force, the team has earned an enemy who
  may recur. Defeating Heffernan or Mindgloom counts toward an initiation ordeal.
"""

ORGS = []

LOCATIONS = [
    {
        "name": "Caring Gardens",
        "location_type": "hospital",
        "city": "Seattle",
        "district": "Puyallup",
        "security_level": "Corporate Standard",
        "summary": "The twenty-bed Rose Croix psychiatric clinic in Puyallup -- a dark, powerless three-storey complex whose director has most of its patients and staff under a sustained Mob Mind",
        "description": (
            "A fairly compact three-storey building taking up a full city block in Puyallup, formerly "
            "a state-owned sanitarium and, until a few months ago, a federally subsidized place. Rose "
            "Croix bought it, renamed it Caring Gardens, tuned up the facilities and replaced several "
            "employees; it now caters to high-profile patients with stress-related psychoses or "
            "addiction problems, and because it targets high-margin clients it is only a twenty-bed "
            "facility with fifteen patients currently enrolled. There is a single entrance at the "
            "front and a loading dock at the back, and tonight neither is locked and no lights are on "
            "anywhere inside. The ground floor holds a reception area, patient rooms, an exercise "
            "room, a meeting room, the medical exam room, a kitchen and a receiving area off the "
            "loading dock, with an elevator for moving materials and patients between floors. The "
            "second floor is a nurses' station and more patient rooms off a stairwell landing. The "
            "third floor is patient rooms, a library and the Director's Office. Every room not "
            "otherwise noted is empty of people and full of the ordinary things -- cooking utensils "
            "in the kitchen, books in the library, beds in the patient rooms."
        ),
        "notes": (
            "Maps in the 01-07B player aids: basement, ground floor, second floor, third floor. Two "
            "guards patrol inside, both under a Force 5 Control Actions held by Force 5 sustaining "
            "foci worn as bandage headbands, ordered to subdue anyone they meet and bring them to the "
            "Doctor for evaluation; run them on the metroplex guard stats (New Seattle p.113) with "
            "Defiant Super Shocks (10S Stun). Free one and he will happily escort patients out or "
            "guard them somewhere the runners choose, and will reveal that Heffernan has a fortified "
            "room with prisoners on the third floor -- but no amount of negotiation or bribery will "
            "get him to go back up there. Encounter placement: Ben Wilson in the basement boiler "
            "room, Kevin Cooper lurking in the basement storage, Brianne Tillers in the computer "
            "room, Neil O'Malley at reception with a guard shortly after, Shannon Levine in a "
            "ground-floor patient room, Mindgloom on the first floor if the team has an initiate, "
            "Aaron Marik on the second-floor stairwell landing, Gary and Samantha Templeton at the "
            "second-floor nurses' station, Jack Woods stalking the second-floor halls, and Heffernan "
            "in the third-floor Director's Office. Rose Croix badges from Mr. Johnson reassure "
            "confused patients and employees. Background Count 2 applies throughout, and every "
            "magically active character except Heffernan and Mindgloom has to deal with it. Street "
            "legwork (any street contact, TN 5): a pretty place in Puyallup, a nuthouse for rich "
            "folks, formerly federally subsidized with a lot of name changes and layoffs in the past "
            "few weeks, and at four successes a passer-by who saw all the lights go out at once "
            "earlier tonight and heard crazy noises. Corporate legwork (TN 4): an asylum Rose-Croix "
            "just bought, contracted to several AAs and AAAs -- Ares in particular -- doing cutting "
            "edge psychiatric treatment involving magical work, under a newly appointed drek-hot "
            "academic named Heffernan."
        ),
    },
    {
        "name": "Caring Gardens Grounds",
        "location_type": "hospital",
        "city": "Seattle",
        "district": "Puyallup",
        "security_level": "Corporate Standard",
        "summary": "Beautiful walled gardens with a Force 4 astral barrier of wailing bodies across the gate, a Background Count of 2 of despair, and an abandoned HTR ambulance in the drive",
        "description": (
            "From the roadside a six-foot stone wall runs around the block, topped by monowire that is "
            "angled into the facility and clearly labelled -- the goal is to keep patients from "
            "getting out, not to stop people breaking in. Trees show over the wall but hide the "
            "hospital itself, and a few lampposts are visible inside, none of them lit. There is one "
            "conventional entrance: a wrought-iron gate proclaiming 'Caring Gardens' beside a security "
            "booth that is dark and empty tonight, its door standing open. Inside the wall the grounds "
            "are genuinely beautiful and pristinely maintained -- paths winding through well-kept "
            "flowerbeds and old trees, around a small pond, past park benches and picnic tables, with "
            "unlit lampposts every ten meters along the paths. In astral space that beauty is marred "
            "by a sense of dramatic sorrow and dread. A Rose-Croix HTR ambulance sits abandoned in "
            "front of the drive."
        ),
        "notes": (
            "The gate is closed and locked with no power to it or to the booth, so Mr. Johnson's "
            "access code does not work: Electronics (6) to hack the lock, or beat the gate's Barrier "
            "rating of 16. In the booth's drawer is a pocket secretary loaded with word puzzles, music "
            "and vid shows, a cheat sheet for checking delivery schedules and appointments, and a list "
            "of office extensions -- the booth phone is dead and the extensions are 'not in service' "
            "from a cell phone. The HTR vehicle is an Ares Roadmaster with a water cannon, locked "
            "tight with its security system active; inside is a good assortment of basic biotech gear "
            "(medkits, patches), and its security camera is still rolling on a constant uplink to "
            "Rose-Croix dispatch -- anything the team takes or damages comes out of their pay. The "
            "first encounter is the astral barrier at the wall: Force 4, manifesting as a hazy wall of "
            "human and metahuman bodies moaning and wailing in torment, which is simply a "
            "characteristic of the magician who made it; the forms cannot be interacted with. Bringing "
            "magically active foci through it, or entering astral combat with it, alerts both "
            "Heffernan and Mindgloom, though neither acts yet. Magically active characters who do not "
            "think to check get an Int (3) test to remember it from the briefing. Past the barrier, "
            "Magic (10) reveals a Background Count of 2 (MitS pp.83-86) of deep despair, pain and "
            "general hopelessness. Perception (5) finds security cameras at irregular intervals around "
            "the grounds; Electronics (3) shows they are not currently active. The parking lot holds "
            "Heffernan's car and the Caring Gardens mini-bus, which he will load with patients and "
            "employees if the runners let him leave."
        ),
    },
    {
        "name": "Caring Gardens Basement",
        "location_type": "data center",
        "city": "Seattle",
        "district": "Puyallup",
        "security_level": "Corporate Standard",
        "summary": "Boiler room, dead generator, the server room behind a Barrier 13 door, fenceable medical supplies, and a storage space full of terrifying therapeutic equipment",
        "description": (
            "The bottom level of the complex and the Datasteal site. The boiler room also houses the "
            "building's HVAC plant and a back-up generator which is now out of fuel; it is where the "
            "night repairman barricaded himself in with a monkey wrench when the noises started "
            "upstairs. The computer room holds the facility's servers behind a Barrier rating 13 door "
            "with a rating 4 maglock. An enclosed storage area holds fenceable medical supplies with a "
            "street value of TR x 6,000 nuyen. The remainder of the basement is a horribly disorganized "
            "storage space, crates and assorted pieces of terrifying 'therapeutic' equipment scattered "
            "around, which is exactly the kind of place a man who believes he is possessed by an insect "
            "spirit chooses to lurk."
        ),
        "notes": (
            "If the team has no decker, the power is out to every computer system in the building and "
            "the storage components have to come out physically: Electronics (B/R) (8), base time one "
            "hour reduced as normal by extra successes. The resulting unit is big, heavy and awkward at "
            "around 80 kilos, and adds +6 to any stealth, dodge or athletics test while carried -- the "
            "book advises the GM to keep asking who is carrying it. If the team does have a decker, the "
            "network and all computer systems are still up on emergency back-up power and he must hack "
            "the Caring Gardens office host (see MATRIX_HOSTS); Mr. Johnson's codes are out of date. "
            "The fenceable supplies are a deliberate temptation: remind the players that they are "
            "working for the company that owns the facility and that stealing from it would be "
            "unprofessional. Ben Wilson is behind the boiler room door; Brianne Tillers is in the "
            "computer room and, if the team has no decker, the GM is strongly encouraged to include "
            "her; Kevin Cooper is among the crates."
        ),
    },
    {
        "name": "The Director's Office, Caring Gardens",
        "location_type": "corporate facility",
        "city": "Seattle",
        "district": "Puyallup",
        "security_level": "Corporate Standard",
        "summary": "Art, a wooden desk, real paper tomes, an open window over the gardens, and a corrupted mage standing in front of sixteen glazed-eyed thralls",
        "description": (
            "Third floor, behind a door labelled 'Alex Heffernan, Director'. The office is beautifully "
            "furnished with a charming array of art, what looks like a wooden desk, real paper tomes, "
            "and a beautiful view out of the open window onto the Caring Gardens grounds. All of that "
            "is secondary to the man in the lab coat standing in front of the desk and the sixteen "
            "others standing slightly behind him -- the ones in the back have a consistent glazed look "
            "on their faces. A faint glow is visible around the man in the front, and as the runners "
            "focus on him he says, 'Ahh, so good of you to finally come to join the party.'"
        ),
        "notes": (
            "The sixteen behind Heffernan are nine patients, two kitchen staff, two facility night "
            "guards and the three missing HTR team members -- and the book advises specifically "
            "mentioning those heavily armed, heavily armored NPCs to the players. Unless the team "
            "opens fire immediately he will talk. Beyond the negotiation, the room's features matter "
            "in two ways: the guards elsewhere in the building describe it as a fortified room with "
            "prisoners and will not come back up here, and the open window is Heffernan's exit -- when "
            "things start to go poorly he jumps out of it and uses Levitate to get away. The rest of "
            "the third floor is empty patient rooms and a library. Reaching this door ends the "
            "exploration scene and begins the finale."
        ),
    },
    {
        "name": "The Place of Fear (Mindgloom's Asylum)",
        "location_type": "metaplane",
        "city": "Seattle",
        "security_level": "Zero Zone -- Lethal Response",
        "summary": "The metaplanar Place of Fear as a Victorian-era insane asylum, where an initiate can quest for Mindgloom's true name past a Dweller and an alienist",
        "description": (
            "The metaplanar destination of the optional astral quest for Mindgloom's true name, run as "
            "a visit to the Place of Fear in the form of a Victorian-era insane asylum -- the same "
            "period and the same institution the spirit itself wears when it materializes as a stooped "
            "old man in late-Victorian garb carrying a black medical bag. After overcoming the Dweller "
            "on the Threshold, the key test of willpower is not a fight at all: the quester must "
            "persuade an alienist, a Victorian psychologist, that he has in fact recovered from his "
            "recent bout of insanity. From there the way opens to the Citadel and to Mindgloom's true "
            "name."
        ),
        "notes": (
            "Requires an initiate full magician who has first assensed Mindgloom and identified him as "
            "a hearth spirit. Quest Rating 7; duration 7D6 hours (MitS pp.92-95 for the quest, p.114 "
            "for true names). This is a real-time problem as much as a magical one: Broward's deadline "
            "is twenty-four hours and the quest can eat most of it. The payoff is decisive -- banish, "
            "disrupt or bind Mindgloom and Dr. Heffernan loses all of his potency and two points of "
            "Magic. The mirror also holds: defeat Heffernan first and Mindgloom loses all his Spirit "
            "Energy and leaves the physical plane willingly."
        ),
    },
]

NPCS = [
    {
        "name": "Dr. Alex Heffernan",
        "role": "The fraudulent director of Caring Gardens -- a con artist and corrupted hermetic mage holding the staff and patients under a sustained Mob Mind",
        "archetype": "Corrupted Mage",
        "title": "Director, Caring Gardens (Rose Croix); corrupted hermetic magician",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "A man in a lab coat with a faint glow visible around him, standing easily in a beautifully "
            "furnished office in front of sixteen glazed-eyed thralls, greeting an armed intrusion the "
            "way a host greets latecomers: 'Ahh, so good of you to finally come to join the party.' He "
            "is a terribly slick con artist first and a very skilled magician second, and both show. He "
            "explains in the most persuasive way he can that he really has no argument with the "
            "runners, that this is an inconvenient situation for all of them, and that he assumes his "
            "body is worth a fair bit of nuyen to them -- and then starts offering ways out that cost "
            "him nothing. He would prefer to keep his body and his thralls intact."
        ),
        "background": (
            "He is not a doctor by any stretch of the imagination. He presented himself to Rose Croix "
            "as a premiere psychiatrist with a background in innovative drug and thaumaturgical "
            "therapies -- senior positions at several research hospitals, publications in premiere "
            "journals, personal references from executives at both Transys Neuronet and Universal "
            "Omnitech. Most of it would not have survived a cursory check, and Rose Croix, racing to "
            "compete with DocWagon and needing its new sanitarium profitable at once, never even did "
            "that; the hiring was considered a major coup. He spent his first weeks learning the "
            "patients, the staff and the systems of a facility that had been an honest place which "
            "truly cared about its patients. Then he began manipulating things: a few adjusted "
            "medications, then alternative treatments -- electroshock, leechings, 'new' magical "
            "techniques. All of it was preparation for the ritual he finished tonight, summoning a "
            "shadow free spirit and binding it into a spirit pact to complete his own transformation "
            "into a fully corrupted mage. The binding went imperfectly, the feedback knocked the "
            "institute's electronics off-line, and that only accelerated his plans."
        ),
        "notes": (
            "Stats: B3 Q3 S2 C6 I6 W6 Magic 8(10), Ess 6.0, Reaction 4, Init 4+1D6. Potency 2; "
            "Initiate Grade 1+TR; Pro 3; Combat Pool 7, Astral Pool 9, Spell Pool 10. Biotech 4, "
            "Pistols 5, Sorcery 7, Conjuring 8, Etiquette (Corp) 5(7), Negotiation (Con) 7(9); Pop "
            "Psych 4, Megacorporate Politics 5, Spirits 4. Metamagic: Masking, with Reflecting and "
            "Quickening. Force 6 sustaining focus currently holding Armor 6; Secure Ultra Vest 3/2. "
            "Spells: Mob Mind 6, Control Actions 5, Stun Ball 5, Stun Bolt 6, Alter Memory 4, Heal 4, "
            "Armor 6, Control Emotion 5, Levitate 4, Phantasm 5. The Background Count of 2 counts as a "
            "Power Site 2 for him because it is aspected to match his corruption; sustaining the Mob "
            "Mind gives him +2 to all target numbers for the encounter. His three bribes: teaching any "
            "willing mage the ways he came into his power (any PC who agrees and follows through is "
            "eliminated from the campaign and becomes an NPC); the wiles of his patients; and a nasty "
            "secret about Rose Croix worth about 20,000 nuyen on the street -- video of a run against "
            "DocWagon's tissue banks plus audio of a Rose-Croix Mr. Johnson setting it up through a "
            "street fixer, which SRM 01-02 Strings Attached players will recognize themselves in, and "
            "which fences to a DocWagon or media contact for 10,000. He can also be talked in: an "
            "opposed Negotiations test, helped by promises of immunity, a generous bribe of cash or "
            "equipment, or magical teaching. Tactics if it goes badly: patients and employees into "
            "melee first, then Control Actions on the team's most combat-capable character to turn him "
            "on his own team, with Mindgloom supporting if available; then out of the window on "
            "Levitate. He keeps every bargain he makes, takes his car and loads the mini-bus with a "
            "selection of patients and employees, and leaves the facility to the runners. Escaped or "
            "taken prisoner by force, he is an enemy who may recur in a future mission -- note it on "
            "the Event Log. Legwork: medical contact (4), academic (6) or corporate (8) -- Rose-Croix "
            "just hired him and made it sound like a coup; nobody has seen anything he published; "
            "searches against the references in the press release return no matches; he does not even "
            "appear to hold accreditations."
        ),
    },
    {
        "name": "Mindgloom",
        "role": "Shadow free hearth spirit, newly arrived and feeding on the despair of a whole asylum; Heffernan's pact partner and the reason the lights went out",
        "archetype": "Free Spirit",
        "title": "Shadow free hearth spirit; Caring Gardens is his domain",
        "gender": "Male",
        "connection": 4,
        "description": (
            "In his physical form Mindgloom appears as a stooped old man dressed in late Victorian-era "
            "garb, carrying a black medical bag, with a bit of a confused expression on his face. The "
            "confusion is genuine: he is newly arrived in the physical world, he does not understand "
            "why these people are not feeling the despair he is used to encountering in this building, "
            "and he wants to know why they are taking one of his meals away with them. Two of the "
            "patients have already tried to describe him to the runners without knowing what he is -- "
            "Neil O'Malley is not sure about this new psychologist whose techniques and style of dress "
            "seem very dated, and Aaron Marik simply calls him Victorian and scary."
        ),
        "background": (
            "Mindgloom's arrival triggered tonight's entire series of events. Dr. Heffernan spent a few "
            "weeks of research identifying his true name, then summoned him and bound him into a "
            "spirit pact (MitS p.124). Caring Gardens has been a buffet ever since -- he feeds off the "
            "despair and confusion of metahumans, and in the first few hours of his time here he has "
            "feasted and rapidly raised his Spirit Energy. He is naive, content with his situation, and "
            "has not yet encountered anyone working against him; Heffernan dealt with the HTR team "
            "personally, and Mindgloom has not bothered trying to feed off the employees who are still "
            "in the complex under their own free will."
        ),
        "notes": (
            "Stats: B8(10) Q9(11)x3 S5(7) C7(9) I7(9) W7(9) Ess 7(9)A Reaction 8(10); Init 27(29)+1D6 "
            "astral, 16+1D6 physical; Combat Pool 9, Astral Pool 8, Pro 4. Force 5; Spirit Energy 2(4) "
            "because Caring Gardens is his domain. Unarmed Combat 5, Negotiation 3. Powers: Accident, "
            "Concealment, Confusion, Dispelling, Human Form, Guard, Materialization, Search. Armor "
            "14(18); melee damage 3+2(4)M. At exceptionally high table ratings raise his Force (and "
            "then his attributes) to 3+TR. OPTIONAL: run this encounter only if there are one or more "
            "full magicians among the runners; defeating him needs a capable conjurer and may involve "
            "an astral quest. He materializes after the players have met at least one patient. Well "
            "played fast talk may persuade him to go back and check with Dr. Heffernan before "
            "attacking. The two are mechanically linked: kill Heffernan first and Mindgloom loses all "
            "Spirit Energy and willingly leaves the physical plane; banish, disrupt or bind Mindgloom "
            "and Heffernan loses all potency and 2 points of Magic. Disrupting him counts as defeating "
            "him for initiation-ordeal purposes; if both he and Heffernan escape safely, nobody gets "
            "the ordeal credit. True name via astral quest: assense him first to establish that he was "
            "a hearth spirit, then Quest Rating 7, 7D6 hours, the Place of Fear as a Victorian asylum."
        ),
    },
    {
        "name": "Trey \"Boltar\" Harris",
        "role": "Rose Croix corporate combat mage, loaned to the team only if it has no full magician of its own -- and insufferable about it",
        "archetype": "Corporate Mage",
        "title": "Combat mage, Rose Croix Corporation",
        "race": "Human",
        "gender": "Male",
        "organization": "Rose Croix",
        "connection": 3,
        "description": (
            "The epitome of the cocky flyboy: a corporate wage mage who has proven himself "
            "combat-capable and never stops implying it. An elitist, arrogant, womanizing bastard who "
            "sold his soul to a corporation, has been thoroughly pampered every step of the way, and "
            "fully expects the pampering to continue even when he is working with people who are not "
            "from his corporation. In his mind the runners have two strikes before the run starts: "
            "they are streetscum-guttertrash, and they are all mundanes -- in Trey's world anyone who "
            "is not a full magician is a mundane. He will make it eminently clear that he is here "
            "because he has to be, not because he wants to be, and will voice the opinion often that "
            "the whole situation would have gone much better handled in house, while happily ignoring "
            "the counter-arguments of any streetscum."
        ),
        "background": (
            "Mr. Johnson keeps him waiting outside the meeting room at Matchstick's and calls him in "
            "only if the team's primary concern is that it has no magical support; if the team already "
            "has one or more spellcasters, he is never offered and never appears. He is the sharp "
            "contrast the book builds him for: contemptuous of the runners and genuinely, deeply "
            "concerned about everyone at the Caring Gardens facility, because they are either corporate "
            "family or clients. Around any other NPC he behaves, reluctantly, like a professional."
        ),
        "notes": (
            "NO STAT BLOCK -- the book gives him a full personality write-up and the cast section ends "
            "without printing a single attribute, skill or spell. Build him as a Rose Croix combat mage "
            "scaled to the table, or borrow the Knight Errant security mage line if you need numbers "
            "in a hurry. Play value: he is a running friction generator inside a scenario that "
            "otherwise has no interpersonal conflict on the runners' side of the line, and he is a "
            "corporate witness to whatever the team does to Rose Croix property and Rose Croix "
            "clients. He is also the group's insurance policy against Heffernan, since a team with no "
            "full magician can neither meet Mindgloom nor reliably strip the doctor's sustained "
            "spells."
        ),
        "contact_skills": [
            "Rose Croix corporate magical security",
            "Combat sorcery",
        ],
    },
    {
        "name": "Ben Wilson",
        "role": "Caring Gardens night repairman, barricaded in the boiler room with a monkey wrench and no intention of leaving it",
        "archetype": "Technician",
        "title": "Night maintenance, Caring Gardens (Benjamin Wilson on the employee roster)",
        "race": "Ork",
        "gender": "Male",
        "organization": "Rose Croix",
        "connection": 1,
        "description": (
            "A big ork maintenance man who was on duty when the power went out and went straight into "
            "the boiler room to work out what had failed. After a while spent establishing that nothing "
            "worked at all, he started hearing strange noises from the upper floors, grabbed a handy "
            "monkey wrench and barricaded himself in. He knows something awfully weird is going on, he "
            "is not fond of being trapped in a building full of 'nut jobs', and he has no idea how far "
            "the problem goes. He is not a particularly brave man, nor a particularly wise one, and "
            "the book is blunt about it: keep in mind that he is a coward -- but if he has the "
            "opportunity to get the jump on a lone runner, he will take it."
        ),
        "background": (
            "One of the two maintenance staff on the Caring Gardens employee roster. The phones are out "
            "and he does not have his cell phone with him, so he has not been anxious to investigate "
            "too far. He has the skills to help repair the facility, and would be more than happy to, "
            "but a full repair means restringing power lines from the telephone poles along the street "
            "to the building and he does not have the equipment for that -- if the runners can somehow "
            "get the electric company out here, he is their man."
        ),
        "notes": (
            "Stats: B5 Q4 S5 C2 I3 W3, Ess 6.0, Reaction 3, Init 3+1D6. Unarmed Combat 2, Electronics "
            "4, Electronics (B/R) 4, HVAC 3. Encountered on entering the basement boiler room, which "
            "also houses the HVAC plant and the dry back-up generator. He will be very apprehensive on "
            "first contact -- use best judgment on his reaction. Getting him to leave the hidey-hole "
            "takes a heck of a job of persuading, or a promise to take him out of the facility "
            "immediately once he is convinced it is safer outside than in. He is worth 200 nuyen per "
            "runner extracted, like every other employee, and he is the one person in the building who "
            "could plausibly help restore power if the team solves the outside half of the problem."
        ),
        "contact_skills": [
            "Building systems and HVAC repair",
        ],
    },
    {
        "name": "Kevin Cooper",
        "role": "Patient who believes he is possessed by an insect spirit -- stalks the team along the drop ceilings and fake-casts at them",
        "archetype": "Patient",
        "title": "Patient, Caring Gardens; former Universal Brotherhood activist",
        "race": "Human",
        "gender": "Male",
        "age": 28,
        "connection": 1,
        "description": (
            "A human male in his late twenties in patient scrubs that are dirty and torn in places, "
            "wearing a pair of faceted goggles and a pair of floppy wire antennae. He has developed a "
            "pathological fear of light and of cleanliness, and spends most of his time crawling around "
            "behind or under furniture, lurking in dark hallways and closets, or climbing over "
            "furniture and along the drop ceilings. When he talks he frequently inserts weird chittering "
            "noises. He approaches the runners from a dark hall, hanging upside down from the ceiling, "
            "chittering as he comes, and when noticed he drops down and starts gesturing as though "
            "casting a spell."
        ),
        "background": (
            "Kevin was a dedicated activist with the Universal Brotherhood a number of years ago, a "
            "true believer in their cause. He only discovered their corruption when it came out in the "
            "media, and he did not take the information well; at that point his mind snapped. Since "
            "then he has been shuffled between quite a few mental care facilities by wealthy parents "
            "who still hope he can be cured. He has deluded himself into believing that he is possessed "
            "by an insect spirit. He is not possessed, and he is not awakened -- but because he "
            "believes it he has developed a variety of psychoses that force him to act as he thinks an "
            "insect spirit would."
        ),
        "notes": (
            "Stats: B2 Q2 S2 C2 I3 W2, Ess 6.0, Reaction 2, Init 2+1D6. Negotiation 2, Etiquette (Corp) "
            "4, Instruction 2, Universal Brotherhood 4. Noticing his approach requires one success on a "
            "Stealth (Sneaking) (2) test. Give awakened characters a quick Sorcery (2) test as he "
            "'casts': success reveals he is not actually manipulating any energies, which will "
            "hopefully stop the gun-happy runners from shooting a rescue objective. If they do not "
            "attack, he finishes the gesture, shouts 'Beware the bugs!' and runs for the nearest "
            "closet. Restrained and interrogated he knows there is at least one staffer hiding in the "
            "boiler room and has heard strange noises from the second floor but has not wanted to check. "
            "Asked about his treatments or about Dr. Heffernan he panics; calmed, he delivers a horribly "
            "jumbled tale about being repeatedly submerged in a vat full of insects."
        ),
    },
    {
        "name": "Brianne Tillers",
        "role": "Sixteen-year-old fading otaku in the computer room -- crude, unfiltered, and the team's way into the Caring Gardens network",
        "archetype": "Otaku",
        "title": "Patient, Caring Gardens; otaku",
        "race": "Human",
        "gender": "Female",
        "age": 16,
        "connection": 2,
        "description": (
            "A sixteen-year-old girl who grew up in the confrontational world of the Matrix and is "
            "quickly discovering that she has none of the social skills required in the world outside "
            "it. She is unbelievably coarse, crude and direct, and to make things even more "
            "embarrassing she finds herself compelled to shout things out at odd times in a near "
            "uncontrollable manner -- as if there were no filter between her brain and her mouth. She "
            "will be more than happy to help the players extract whatever data is available, and she "
            "may be a bit of a nuisance in the process."
        ),
        "background": (
            "An otaku whose skills are fading rapidly, and who as those skills fade is finding it "
            "harder and harder to deal with a physical world that is trapping her. She is not very "
            "familiar with the physical complex at all but was intimately familiar with the Caring "
            "Gardens network system. Her treatment at Heffernan's hands was extensive electroshock "
            "therapy with the charges delivered directly through her datajack, throughout which she was "
            "told that the Matrix was a figment of her imagination."
        ),
        "notes": (
            "Stats: B1 Q1 S1 C4 I7 W3, Ess 5.8, Reaction 4, Init 4+1D6. Cyberware: datajack, internal "
            "ASIST converter. Computers 7. If the team has a decker she is an optional encounter; if it "
            "does not, the GM is strongly encouraged to include her, because she is the alternative to "
            "hauling an 80-kilo storage unit around a hostile building. Asked about Dr. Heffernan or "
            "the treatments she has received, she goes into convulsions; calming her takes First Aid "
            "(4) with two successes, after which she explains what was done to her. She is a patient "
            "and therefore a 200-nuyen-per-runner extraction objective, and she is a live hook well "
            "past this adventure: a fading otaku with Computers 7 who owes a runner team her rescue."
        ),
        "contact_skills": [
            "Matrix intuition and host navigation",
            "The Caring Gardens network",
        ],
    },
    {
        "name": "Shannon Levine",
        "role": "Burned-out sim star admitted under the name Sharon Vine, a month into addiction treatment and deep in the DTs",
        "archetype": "Simsense Star",
        "title": "Patient, Caring Gardens, registered as \"Sharon Vine\"; former primetime sim star",
        "race": "Human",
        "gender": "Female",
        "connection": 2,
        "description": (
            "Two years ago she was on top of the world: her own primetime network sim, endorsement "
            "deals worth meganuyen, paparazzi chasing her everywhere. Now she is rather out of it. The "
            "real world seems far too surreal for her chip-riddled senses; she has no idea why the "
            "lights are out or what the strange noises in the building are, and what she does know is "
            "that she needs some strong experience, preferably with an adrenaline fix in hand. As soon "
            "as things stop going the way they would in a sim, she becomes terribly confused."
        ),
        "background": (
            "Perhaps having too much too easily was the problem. At the top of the world she started "
            "chipping -- innocently enough, a chip at a party to make her a little more social and the "
            "media a little less invasive, a weekend jacked in to forget the world. As time passed she "
            "needed stronger and stronger chips: first Cal-hots, then full BTLs. Her body began to "
            "degrade and her network ratings with it, and from there it was a short step to last year's "
            "star. A month ago she checked herself into Caring Gardens, using most of her remaining "
            "assets to pay for addiction treatment. She is still going through the DTs, and there does "
            "not seem to be anyone around to help."
        ),
        "notes": (
            "Stats: B2 Q3 S2 C6 I3 W2, Ess 3.2, Reaction 3, Init 3+1D6. Etiquette (Corp) 5, Negotiation "
            "4, Pop Music 4, Pop Sims. Cyberware: Full-X cyberware simrig, Simlink (Rating 5), datajack. "
            "Found in a ground-floor patient room. When the team meets her, have them immediately make a "
            "Pop Culture (3) test: the door to her room and the patient list they were given both read "
            "'Sharon Vine', but one success reveals the well-known sim star Shannon Levine, remembered "
            "from her NERPS commercials and her role as the wicked sister on 'Housemates'. Note the "
            "book's own inconsistency -- Handout 1's patient roster lists her as 'Levine, Shannon' "
            "rather than under the alias the text says appears on the list. She is a 200-nuyen "
            "extraction objective and the most publicity-sensitive body in the building, which matters "
            "given that Mr. Johnson's overriding instruction is no media."
        ),
        "contact_skills": [
            "Seattle simsense and trid industry",
        ],
    },
    {
        "name": "Neil O'Malley",
        "role": "Patient who believes he is a psychiatrist and Dr. Heffernan's right-hand man; as likely to lead the team astray as to help",
        "archetype": "Patient",
        "title": "Patient, Caring Gardens; former Seattle public defender",
        "race": "Elf",
        "gender": "Male",
        "connection": 1,
        "description": (
            "A tall elf in a business suit and a lab coat with a non-functional Rose-Croix "
            "identification card, who asks to see the runners' identification and readily accepts "
            "whatever they provide. He identifies himself as one of the clinic's psychiatrists and as "
            "Dr. Heffernan's right-hand man, and once he has seen ID he asks why they are here and then "
            "attempts to take charge of the situation. He offers psychiatric and psychological advice "
            "to the characters throughout, throwing out constant buzzwords and dropping assorted medical "
            "terms, never using them correctly and often mispronouncing them. He is physically incapable "
            "of knowing when to be quiet."
        ),
        "background": (
            "Neil worked as a public defense attorney with the city of Seattle for fifteen years, during "
            "which he handled a great many cases where innocents did time for crimes they had not "
            "committed. Some say that is just the way the world works in the '60s; Neil was not cut out "
            "to deal with it. After one of his clients went to the chair for a crime he knew she could "
            "not have committed, his brain simply snapped."
        ),
        "notes": (
            "Stats: B3 Q3 S2 C5 I3 W3, Ess 6.0, Reaction 3, Init 3+1D6. Etiquette (Corp) 4, Negotiation "
            "4, Pop Psych 3. His Rose-Croix ID is a fake -- a Forgery (2) test reveals it quickly, as "
            "will any attempt to use it. In truth there is very little he can do: he knows the layout of "
            "the facility and he will recognize, and be recognized by, any of the patients and "
            "employees, but he is terribly unfocused and out of touch and is every bit as likely to lead "
            "the team in the wrong direction as to help them. Asked about the crisis he explains that "
            "the problems are due to a city-wide power outage and reassures everyone that it is a "
            "routine problem which should be resolved shortly, and he is anxious to accompany the "
            "runners around the facility to make sure the guards have been doing their jobs and the "
            "patients are all secured and reassured. Two things make him worth keeping: he is the "
            "preferred victim for Jack Woods's headlock ambush, and he makes an offhand mention that he "
            "is not sure about this new psychologist whose techniques and style of dress seem very "
            "dated -- which is the team's first warning about Mindgloom."
        ),
    },
    {
        "name": "Gary Templeton",
        "role": "Night-shift nurse and ex-UCAS military; found securing supplies and improvising weapons at the second-floor nurses' station",
        "archetype": "Medic",
        "title": "Night-shift nurse, Caring Gardens; married to Samantha Templeton",
        "race": "Human",
        "gender": "Male",
        "organization": "Rose Croix",
        "connection": 2,
        "description": (
            "One half of a married pair of night-shift nurses who locked themselves into an unused "
            "patient room as soon as things started getting crazy and stayed low and quiet. When the "
            "runners find him he is at the second-floor nurses' station securing medical supplies and "
            "improvising weapons. Unless approached violently he is very relieved to see help arrive; "
            "if attacked he defends himself to the best of his ability, which is considerably better "
            "than a nurse's ability usually is. He asks straight away whether any firearms are "
            "available and explains, or demonstrates, what he can do with one."
        ),
        "background": (
            "Gary and Samantha met while in the UCAS military and took the jobs at Caring Gardens after "
            "retiring. They are dedicated medical workers with a background that leaves them "
            "particularly capable in exactly this situation: very concerned about each other's safety, "
            "and also about their patients. Neither is comfortable with the treatments the new director "
            "has implemented -- patients do not seem to be progressing properly, and some of his shock "
            "therapy methods seem downright primitive."
        ),
        "notes": (
            "Stats (identical for both Templetons): B4 Q4 S5 C3 I4 W3, Ess 6.0, Reaction 4, Init 4+1D6. "
            "Biotech 4, Unarmed Combat 3, SMG 3, Stealth 4. Gear: Rating 4 medkit. If the team is "
            "reasonably persuasive, the pair will come along and help take down whatever madness is on "
            "the second floor -- the only competent, willing, armed allies available inside the "
            "building. If any of the NPC patients are with the team when they are met, both nurses can "
            "calm and medicate them; if any runner is injured, both will do their best to help. Each is "
            "a 200-nuyen-per-runner extraction objective, and rescuing at least three of the detailed "
            "staff or patients is worth a karma point."
        ),
        "contact_skills": [
            "Emergency biotech and field medicine",
            "Caring Gardens staff and routine",
        ],
    },
    {
        "name": "Samantha Templeton",
        "role": "Night-shift nurse and ex-UCAS military; Gary's wife and the other half of the only competent allies in the building",
        "archetype": "Medic",
        "title": "Night-shift nurse, Caring Gardens; married to Gary Templeton",
        "race": "Human",
        "gender": "Female",
        "organization": "Rose Croix",
        "connection": 2,
        "description": (
            "The other half of the Caring Gardens night nursing shift: a retired UCAS soldier turned "
            "nurse who rode out the first hours of the crisis locked in an unused patient room with her "
            "husband and is now stripping the nurses' station for anything useful. She is relieved rather "
            "than frightened when armed strangers turn up, provided they do not open with violence, and "
            "her first practical question is the same as Gary's: is there a gun going spare? She is "
            "visibly more worried about her husband than about herself, and about the patients than "
            "about either of them."
        ),
        "background": (
            "She and Gary met while in the UCAS military and took the Caring Gardens jobs after "
            "retiring. Both are dedicated medical workers who have been quietly unhappy with the new "
            "director for weeks: patients are not progressing properly under his regime, and some of "
            "his 'shock therapy' methods seem downright primitive to people who have seen real field "
            "medicine."
        ),
        "notes": (
            "Stats as Gary Templeton: B4 Q4 S5 C3 I4 W3, Ess 6.0, Reaction 4, Init 4+1D6; Biotech 4, "
            "Unarmed Combat 3, SMG 3, Stealth 4; Rating 4 medkit. The book gives the couple one shared "
            "stat block and one shared write-up, so play them as a unit that reacts to threats against "
            "each other. Their practical value to the team: two extra guns if the runners will arm "
            "them, a mobile medkit, and the only people in the building who can settle a panicking "
            "patient without a spell. Their testimony about the director's methods is also the "
            "clearest inside confirmation the team gets that Heffernan is the problem before they reach "
            "the third floor."
        ),
        "contact_skills": [
            "Emergency biotech and field medicine",
            "Caring Gardens staff and routine",
        ],
    },
    {
        "name": "Jack Woods",
        "role": "Desert Wars veteran patient whose cyberware inhibitors died with the power -- on patrol, spur popped, wired reflexes hot",
        "archetype": "Street Samurai",
        "title": "Patient, Caring Gardens (John Woods on the roster); Desert Wars veteran, Ares",
        "race": "Ork",
        "gender": "Male",
        "connection": 2,
        "description": (
            "An ork in white patient scrubs with a sergeant's chevrons drawn on the upper arm in "
            "marker, cyberspur popped and reflexes engaged, working his way through a darkened hospital "
            "on what he firmly believes is a recon mission during the wars. He appears out of the "
            "shadows, takes one of the other patients the team is escorting in a headlock with the spur "
            "at their throat, and shouts 'Password: Ragnarok.' He will take pretty much anything the "
            "runners say as a counter-password, after which he unhands his prisoner and walks over with "
            "a swagger in his step. He is very gung-ho with a can-do attitude, explains that he is the "
            "only survivor from his platoon on this recon, and asks to hook up with theirs to finish "
            "the job -- and to borrow a gun, preferably one with a smartgun link."
        ),
        "background": (
            "Jack is a Desert Wars veteran who served with Ares. All of the cybernetic implants made "
            "him a physical master of the battlefield; sadly his mind did not cope nearly as well with "
            "the stresses of ongoing warfare, and he is now dissociative. Having spent a fortune on his "
            "cybernetics, Ares sent him to Caring Gardens for treatment, trying to recoup its "
            "investment. Rose Croix normally keeps his cyberware inactive using inhibitors. Since the "
            "power went out, the inhibitors have stopped working."
        ),
        "notes": (
            "Stats: B4 Q4(6) S6(8) C2 I3 W3, Ess 0.2, Reaction 3(7), Init 3(7)+3D6. Cyberware: "
            "cyberspur, Wired Reflexes 2, Muscle Replacement 2, smartgun link, cybereyes with low-light "
            "and flare compensation. Cyber Implant Combat 6, Pistols 4, SMG 6, Etiquette (Military) 3, "
            "Stealth 2. OPTIONAL encounter, second floor; he ambushes another patient the team is "
            "escorting, preferably Neil O'Malley. If the team does not want his help he follows them "
            "anyway, and the only way to lose him is to lock him in a patient room. Let him come along "
            "unarmed and he nags continuously for a weapon; arm him and it becomes obvious he has no "
            "fire discipline at all and will shoot at pretty much anything that moves. He knows the "
            "layout but has only just begun his recon, thinks some of the other prisoners here have "
            "been moved -- he heard screaming and gunshots earlier -- and does not know where they were "
            "taken. Asked about the doctor, he calls him 'Major Heffernan, a hardass' and complains "
            "about all the suicide missions over the last few weeks: constant sims in which he was "
            "forced to watch his comrades at arms die horribly. Roster note: Handout 1 lists him as "
            "'Woods, John', while the cast entry names him Jack."
        ),
    },
    {
        "name": "Aaron Marik",
        "role": "OCD engineer terrified of dirt and darkness, reassembling a very powerful flashlight and unwilling to leave the team's side",
        "archetype": "Engineer",
        "title": "Patient, Caring Gardens; former Ares vehicle and mass-transit engineer",
        "race": "Dwarf",
        "gender": "Male",
        "connection": 2,
        "description": (
            "A dwarf found frantically reassembling an extremely powerful flashlight by the light of "
            "one of the emergency lamps. He is thrilled to see the runners and desperately wants them "
            "to protect him; he will follow them and will not leave them alone, and he insists on "
            "helping with his newly working flashlight and a packet of cleaning wipes. His obsessive "
            "compulsive disorder manifests as a constant need to clean, organize and straighten, "
            "compounded by phobias of dirt and of darkness severe enough to cause near-paralysis at "
            "extreme exposure to either -- which is a serious problem in a filthy, unlit building."
        ),
        "background": (
            "Aaron was a key engineer with Ares, working on vehicle design and mass transit systems. He "
            "was involved in the design and construction of a monorail system in Madrid last year; the "
            "early phases went very well, but shortly after the trains began running with full loads "
            "several thousand people were killed when a high-speed train jumped the tracks and "
            "barrelled through the business district. Investigations pointed to a critical but minor "
            "design flaw in Aaron's blueprints. The incredible guilt and self-doubt drove him over the "
            "edge."
        ),
        "notes": (
            "Stats: B4 Q2 S4 C2 I6 W2, Ess 5.8, Reaction 4, Init 4+1D6. Cyberware: datajack. "
            "Electronics 6, Electronics (B/R) 6, Car (B/R) 8, Civil Engineering 5. OPTIONAL encounter, "
            "second-floor stairwell landing. He is the second patient to describe Mindgloom without "
            "knowing what he is, calling the new doctor who arrived tonight Victorian and scary. In "
            "play he is a liability with useful hands: an Electronics 6 / Electronics B/R 6 engineer "
            "glued to the team in a building whose systems are all dead, who cannot be left in the dark "
            "and cannot be persuaded to stop tidying. He is a 200-nuyen extraction objective and one of "
            "the detailed NPCs who counts toward the rescue-three karma point."
        ),
        "contact_skills": [
            "Vehicle design and civil engineering",
            "Electronics repair",
        ],
    },
    {
        "name": "Caring Gardens Night Guard (thralled)",
        "role": "Facility guard under a Force 5 Control Actions, ordered to subdue anyone he meets and bring them to the Doctor for evaluation",
        "archetype": "Corporate Security Guard",
        "title": "Night guard, Caring Gardens (Rose Croix); under Dr. Heffernan's control",
        "gender": "Male",
        "organization": "Rose Croix",
        "connection": 1,
        "description": (
            "One of two Caring Gardens night guards Heffernan called into his office and put under a "
            "spell before he sent them out to round up the staff and the patients. They still walk the "
            "building on something that looks like a patrol, still carry their Defiant Super Shocks, "
            "and still wear what looks like a bandage tied around the head like a headband -- which is "
            "the Force 5 sustaining focus holding the spell in place. They subdue rather than kill, and "
            "everything they take gets carried up to the third floor for the Doctor's evaluation."
        ),
        "background": (
            "Ordinary metroplex-grade security staff on a night shift at a twenty-bed clinic. Heffernan "
            "started with them because they were the two people in the building who could physically "
            "round up everybody else; they did exactly that, after which he cast Mob Mind over the "
            "collected staff and patients and has sustained it since. Freed, they turn out to be "
            "perfectly cooperative people who have been used as tools all night."
        ),
        "notes": (
            "Use the metroplex guard statistics (New Seattle p.113), armed with Defiant Super Shocks "
            "(10S Stun). Both are under a Force 5 Control Actions cast by Dr. Heffernan and kept up by "
            "Force 5 sustaining foci disguised as bandage headbands. Two are on patrol inside the "
            "complex: the book suggests running into one shortly after the team meets Neil O'Malley, "
            "and the other at whatever moment is most inconvenient. Break the spell locks and a guard "
            "will volunteer to escort patients out or stand watch over them anywhere in the facility "
            "the runners suggest, and will tell them that Heffernan has a fortified room with a number "
            "of prisoners on the third floor -- but no amount of negotiation or bribery will get him to "
            "go up there again. Two more thralled guards stand behind Heffernan in the Director's "
            "Office at the finale. Each is an employee worth 200 nuyen per runner if extracted alive."
        ),
    },
    {
        "name": "Caring Gardens Patient (thralled)",
        "role": "One of the nine patients standing glazed-eyed behind Heffernan under a sustained Mob Mind, sent into melee with improvised clubs",
        "archetype": "Patient",
        "title": "Patient, Caring Gardens; held under Mob Mind",
        "connection": 1,
        "description": (
            "One of nine patients standing slightly behind the man in the lab coat with a consistent "
            "glazed look on their faces. They are the people the runners were paid 200 nuyen a head to "
            "carry out of this building alive, and when the negotiation fails they are what comes at "
            "the team first, swinging whatever they picked up on the way through the wards. They have "
            "no skills, no gear and no chance, and killing them is both a mission failure and a "
            "deliberate moral trap the book sets from the moment Mr. Johnson names his price list."
        ),
        "background": (
            "High-profile clients with stress-related psychoses or addiction problems, admitted to a "
            "high-margin twenty-bed clinic and rounded up by two mind-controlled guards on the night "
            "their director finished his ritual. Heffernan cast a single Mob Mind over the collected "
            "group and has sustained it ever since -- which is why his target numbers are all at +2 "
            "throughout the final encounter."
        ),
        "notes": (
            "Patients (9): B2 Q2 S2 C4 I3 W2, Ess 6, Reaction 2. Key skills: none. Gear: none. Key "
            "weapons: improvised clubs (3M Stun). Kitchen help (2), the other unarmoured civilians in "
            "the room: B4 Q2 S3 C3 I2 W3, Ess 6, Reaction 2, cleavers (3L). Heffernan sends this group "
            "into melee first, then uses Control Actions on the runners' best fighter while they are "
            "occupied. The karma table rewards stopping him without resorting to violence at 2 points "
            "against 1 for stopping him at all, and every patient and employee killed is money off the "
            "team's pay as well as a body Rose Croix has to explain. Nine of the fifteen enrolled "
            "patients are here; the other six -- Cooper, Tillers, Levine, O'Malley, Woods and Marik -- "
            "are loose in the building with their own write-ups."
        ),
    },
    {
        "name": "Rose Croix HTR Team Member",
        "role": "One of three High Threat Response operators sent in three and a half hours ago and never heard from again; now standing behind Heffernan",
        "archetype": "Corporate Security Specialist",
        "title": "High Threat Response team member, Rose Croix",
        "organization": "Rose Croix",
        "connection": 2,
        "description": (
            "Heavily armed and heavily armored professionals in Rose Croix colours, standing in a "
            "director's office with the same glazed expression as the patients around them. Their "
            "ambulance is still parked in the drive outside with its camera uplinking to dispatch and "
            "its doors locked. The book advises the GM to make a point of mentioning them to the "
            "players when the runners open the office door, because these three are the reason "
            "everybody in the room should think twice: a corporate HTR team went into this building "
            "before them and this is what is left of it."
        ),
        "background": (
            "Rose Croix sent the team in three and a half hours before the runners were hired, after "
            "routine checks showed the telecom, power and Matrix connections severed and an astral "
            "sweep found a barrier that was not in the corporate plan. They crossed the perimeter and "
            "the astral barrier and were not heard from again. Dr. Heffernan dealt with them "
            "personally -- which is also why Mindgloom, who has not been fed any of them, has still not "
            "encountered anyone working against him."
        ),
        "notes": (
            "Use the Elite Officer statistics (New Seattle p.114); key weapons Enfield AS-7 (8S) with "
            "smartlink. Three of them, held under the same sustained Mob Mind as the patients and "
            "staff. Mr. Johnson counts them among the employees to be recovered at 200 nuyen per runner "
            "each, and they are by far the most dangerous bodies in the finale if the fight goes hot -- "
            "a team that opens up on the crowd is shooting at armoured professionals standing in front "
            "of unarmoured patients. Their survival is also the difference between an embarrassment and "
            "a disaster for a corporation whose CEO has told the runners that losing an employee is "
            "much less of a public relations problem than losing a client."
        ),
    },
]

ORG_UPDATES = {
    "Rose Croix": {
        "notes_append": (
            "SRM 01-07 Keys to the Asylum: the arc's first self-inflicted wound. Racing to compete "
            "directly with DocWagon from a standing start, Rose Croix cut corners, and its human "
            "resources department is about to discover that the background check it never ran on Dr. "
            "Alex Heffernan is its biggest mistake to date. R-C had just purchased a state-owned "
            "sanitarium in Puyallup, renamed it Caring Gardens and needed it profitable at once, so a "
            "premiere psychiatrist with references from Transys Neuronet and Universal Omnitech "
            "executives was hired as director on a CV that would not have survived a cursory check. He "
            "was a fraud and a corrupted mage. Corporate assets on show: a High Threat Response "
            "division with armoured ambulances (an Ares Roadmaster with a water cannon, biotech gear "
            "inside, camera uplinked to Rose-Croix dispatch), in-house security mages who run astral "
            "sweeps of company facilities, corporate combat mages such as Trey 'Boltar' Harris who can "
            "be loaned to a runner team, employee ID badges, and a CEO who negotiates personally at "
            "0230 in the back room of a jazz club with two guards in full security armour outside the "
            "door. Street legwork (any street contact, TN 4): a company with a new ambulance logo, the "
            "outfit trying to muscle in on DocWagon, hiring runners for all kinds of work lately, and "
            "something just went down at one of their facilities. Corporate legwork (TN 4): a new-ish "
            "startup doing ambulance work that HR departments are considering switching medical plans "
            "to, which has come to the forefront of the Seattle scene mighty quick -- 'I'm not sure "
            "I'd want to get in bed with something rocketing that fast' -- and which may have some "
            "unsavory ties. Those ties are real: Heffernan holds video of a Rose Croix run against "
            "DocWagon's tissue banks and audio of a Rose-Croix Mr. Johnson arranging it through a "
            "street fixer, worth about 20,000 nuyen and fenceable for 10,000 to a DocWagon or media "
            "contact. R-C's requirement here is deniability -- it needs culpable deniability if "
            "patients die, the situation resolved inside 24 hours, and minimal press exposure."
        ),
        "leadership_add": [
            {"name": "Dr. Alex Heffernan", "title": "Director, Caring Gardens", "notes": "A fraud with no accreditation; a corrupted hermetic mage who took the facility for himself."},
        ],
        "enemies_add": ["DocWagon"],
    },
    "DocWagon": {
        "notes_append": (
            "SRM 01-07 Keys to the Asylum: DocWagon is the reason Caring Gardens exists in the state it "
            "does. Rose Croix was 'forced to cut corners when they decided to start up and immediately "
            "compete with DocWagon', and the skipped background check that put a corrupted mage in "
            "charge of an asylum is a direct consequence. Street legwork identifies Rose Croix simply "
            "as 'the company trying to muscle in on DocWagon'. The blackmail material Dr. Heffernan "
            "offers the runners is a Rose Croix run against DocWagon's tissue banks -- video of the run "
            "plus audio of a Rose-Croix Mr. Johnson setting it up through a street fixer (the events of "
            "SRM 01-02 Strings Attached) -- with a street value of about 20,000 nuyen, which fences to "
            "a DocWagon or media contact for 10,000. Selling it to DocWagon puts a weapon in the hands "
            "of the corporation Rose Croix is trying to destroy, two adventures before that fight "
            "reaches its conclusion."
        ),
    },
    "Universal Brotherhood": {
        "notes_append": (
            "SRM 01-07 Keys to the Asylum: the Brotherhood's collapse is still producing casualties in "
            "2064. Kevin Cooper, a patient at Caring Gardens, was a dedicated Universal Brotherhood "
            "activist and a true believer in the cause; he only learned of their corruption when it "
            "broke in the media and did not take the information well. His mind snapped, and wealthy "
            "parents have shuffled him between mental care facilities ever since. He has since deluded "
            "himself into believing that he is possessed by an insect spirit -- he is neither possessed "
            "nor awakened, but the belief has generated a set of psychoses that make him act as he "
            "thinks an insect spirit would: fear of light and cleanliness, faceted goggles, wire "
            "antennae, chittering speech, and a habit of crawling along drop ceilings. He retains "
            "Universal Brotherhood 4 as a knowledge skill."
        ),
    },
    "Ares Macrotechnology": {
        "notes_append": (
            "SRM 01-07 Keys to the Asylum: Ares appears twice as an employer paying for the wreckage of "
            "its own people. Jack Woods is a Desert Wars veteran who served with Ares; the corporation "
            "spent a fortune on the cybernetics that made him a physical master of the battlefield, and "
            "when his mind failed to keep up it sent him to Caring Gardens for treatment specifically "
            "to recoup that investment. Aaron Marik was a key Ares engineer on vehicle design and mass "
            "transit who worked on a Madrid monorail; several thousand people died when a full "
            "high-speed train jumped the tracks through the business district and the inquiry blamed a "
            "minor flaw in his blueprints. Corporate legwork also notes that a few AAs and AAAs hold "
            "contracts with Caring Gardens, 'Ares in particular'."
        ),
    },
    "Lone Star Security": {
        "notes_append": (
            "SRM 01-07 Keys to the Asylum: Lone Star is a failure condition rather than an opponent. Mr. "
            "Johnson's standing instruction is that media attention would be a major problem and that "
            "if Lone Star became involved such attention would be inevitable -- so the whole run is "
            "built around resolving an armed magical crisis at a Puyallup hospital quietly enough that "
            "no police report is ever filed. Rose Croix does not believe it can keep the situation under "
            "wraps for more than 24 hours."
        ),
    },
    "Universal Omnitech": {
        "notes_append": (
            "SRM 01-07 Keys to the Asylum: Universal Omnitech is named, without its knowledge, in the "
            "fraudulent curriculum vitae that got Dr. Alex Heffernan appointed director of Caring "
            "Gardens. His personal references included executives from both Universal Omnitech and "
            "Transys Neuronet, alongside claimed senior positions at several research hospitals and "
            "publications in premiere journals. Most of the references would have held up to a cursory "
            "check; Rose Croix never made one. Academic and medical legwork on Heffernan turns up no "
            "published work and no matches at all when his name is searched against the references in "
            "the Rose Croix press release."
        ),
    },
    "Transys Neuronet": {
        "notes_append": (
            "SRM 01-07 Keys to the Asylum: Transys Neuronet is one of the two megacorporations whose "
            "executives Dr. Alex Heffernan claimed as personal references on the fraudulent CV that won "
            "him the directorship of Caring Gardens -- the other being Universal Omnitech. The "
            "references are exactly the kind that survive a name-check and collapse under a phone call, "
            "which is precisely the check Rose Croix skipped. Searching his name against the references "
            "quoted in the hiring press release returns no matches whatsoever."
        ),
    },
}

LOC_UPDATES = {
    "Matchstick's": {
        "notes_append": (
            "SRM 01-07 Keys to the Asylum: the 0230 hiring meet. By the time the runners arrive the jazz "
            "club has already closed down for the night; knocking (or trying to break in) brings an "
            "annoyed-looking ork bouncer who recognizes them on sight, lets them in and directs them "
            "immediately to the back room, saying Mr. Johnson should be along shortly. He does not "
            "bother with weapon checks or harass them unduly -- he has been provided with their "
            "pictures in advance and instructed simply to let them in. The back room is dominated by a "
            "large, well-worn conference table, with a telecom and Matrix jacks against one wall and a "
            "fresh pot of soykaf and some snacks set out. Mr. Johnson is Walter Broward, CEO of Rose "
            "Croix, who arrives with two guards in full security armour waiting outside the door and a "
            "briefcase of certified credsticks. The club is detailed in either edition of the Seattle "
            "Sourcebook."
        ),
    },
}

NPC_UPDATES = {
    "Michael Davenport": {
        "notes_append": (
            "SRM 01-07 Keys to the Asylum: as Walter Broward, CEO of Rose Croix, he is the Mr. Johnson "
            "in person -- and the runners are the team that 'assassinated' him in SRM 01-01 Double "
            "Cross. Since then he has started Rose Croix and undergone extensive cosmetic surgery; he "
            "remembers that they were a capable team, has followed the street cred they have developed "
            "since, and asks for them by name at two in the morning. He arrives at the back room of "
            "Matchstick's as 'a suit that screams meganuyen' with two guards in full security armour "
            "waiting outside the door and eyes as world-weary as the joygirls on the way to the club, "
            "slides a certified 1,000-nuyen credstick to each runner before he says a word, and opens "
            "with 'Thanks for coming on such short notice. I'll make this as brief as possible.' The "
            "briefing is deliberately vague until they agree: an incident at one of his corporation's "
            "facilities, at least partly magical, primarily a rescue and recovery mission, lives in the "
            "balance, potentially a tremendous embarrassment, media involvement completely "
            "unacceptable, a few casualties possibly inevitable but to be kept to an absolute minimum. "
            "Goal-based fee schedule: 200 nuyen per runner per patient extracted (fifteen enrolled), "
            "200 per employee (ten on duty plus the three-member HTR team), 1,000 for the security "
            "records, 1,000 for the experimental data, 1,500 for the opposition alive and interrogable "
            "or 500 identified but dead or gravely injured -- up to 8,500 each. Negotiation is opposed "
            "against his Negotiation 9, each net success raising one mission category by 50 nuyen. He "
            "offers an ambulance service to move the rescued, Rose Croix ID badges, security files and "
            "Matrix access codes (out of date, though he does not know it), the loan of a combat mage "
            "if the team has no full magician, and his telecom number. He is terribly uneducated about "
            "magical issues and cannot answer questions about them, and he is not aware that the files "
            "he hands over are deliberately contradicted by what the team will find. Aftermath: his "
            "reaction is proportionate to the run -- a smoking crater gets a reluctant payout, a clean "
            "extraction gets a thrilled one."
        ),
        "contact_skills_add": [
            "Rose Croix corporate resources -- HTR ambulances, combat mages, facility access",
        ],
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
### Caring Gardens office host

Orange-7/14/15/12/13/13. Not sculpted. Because the decker is coming in from an internal jackpoint,
the security is toned down; there is no outside route at all, because the LTG connection to the
complex has been severed and there is no Matrix access to the facility from anywhere else.

| Step | Event |
| --- | --- |
| 4 | Probe-5 |
| 8 | Probe-7 |
| 12 | Passive Alert, Trace-9 |
| 16 | Blaster-8 |
| 20 | Active Alert |
| 24 | Shutdown |

Paydata and objectives: the security records and the experimental records are each protected with
Scramble-7 IC and are 150 Mp apiece once downloaded. Each is worth 1,000 nuyen per runner from Mr.
Johnson. The security records may show who or what is responsible for tonight's incident; the
experimental records are the patient files from the facility's thaumaturgical psychiatric testing
programme, which Rose Croix regards as quite valuable. All of the internal security systems are
currently reporting dead feeds. The Matrix access codes Mr. Johnson supplies are sadly out of date --
unless time is running really short, the decker has to hack in.

If the team has no decker, none of this applies: the power is out to every computer in the building
and the physical storage components must be pulled out of the basement server with an Electronics
(B/R) (8) test at a base time of one hour, producing an 80-kilo unit that adds +6 to stealth, dodge
and athletics tests while it is carried. Brianne Tillers, the sixteen-year-old otaku in the computer
room, is the intended alternative and the GM is strongly encouraged to include her in that case.

### Rose Croix dispatch uplink (HTR vehicle)

Not a host to be decked so much as a live camera on the runners. The abandoned Rose-Croix HTR
ambulance in the drive is locked with its security system active, but its security camera is still
rolling and maintaining a constant uplink to Rose-Croix dispatch. Anything the team takes from the
vehicle or damages on it is deducted from their compensation -- and everything they do in front of
it is being watched by their employer.
"""

NOT_BUILT = """
- **The Caring Gardens patient roster (Handout 1)** -- fifteen names with race, gender, weight and
  height and nothing else. Six are detailed in the cast and have rows: Kevin Cooper, Shannon Levine
  (listed as Levine, Shannon, though the text says the list reads Sharon Vine), Aaron Marik, Neil
  O'Malley, Brianne Tillers and John/Jack Woods. The other nine appear only as roster lines with no
  scene, no description and no role, and are folded into the thralled-patient row: **James Bacher**
  (human), **Michelle Bass** (human), **Erika Coburn** (ork), **Linda Deutcher** (dwarf), **Natalie
  Harrison** (ork), **Jennifer Jacobs** (elf), **Frank Masters** (human), **Gordon McCarthy** (ork)
  and **Mark Stephens** (human).
- **The Caring Gardens employee roster (Handout 2)** -- twenty-six names with race, gender and post.
  Three are detailed and have rows: Alex Heffernan (Director), Gary and Samantha Templeton (Nurses)
  and Benjamin Wilson (Maintenance). The rest are roster lines only: office manager **Douglas Adams**
  (elf -- an author in-joke); guards **George Avery** (troll), **Tyrone Baker** (ork), **Thomas
  Cooney** (ork), **Nicholas Gonzalez** (ork), **Anthony Jones**, **Dirk Kline** (dwarf), **Crystal
  Madison**, **Judy Miller** (troll), **Mary Norton**, **Kimberly Stein**, **Elizabeth Tyler** and
  **Edwin Williams** (ork); nurses **Alice Frey** (ork), **Jill Knight**, **William Modic** (ork),
  **Shawn Pruitt** (elf), **Chris Pulley** and **Phyllis Sykes** (ork); cooks **Susan Hendricks**
  (dwarf) and **Michael Hong**; and maintenance **Gabrielle Martinez** (ork). Note the book's own
  contradiction: Mr. Johnson says ten employees were scheduled on duty tonight.
- **The two facility night guards and the three HTR team members** -- given as stat-block references
  (New Seattle p.113 metroplex guard and p.114 elite officer) rather than as individuals; captured in
  the thralled-guard and HTR-team rows.
- **The ork bouncer at Matchstick's** -- unnamed, has the runners' pictures, waves them through
  without a weapons check. Folded into the Matchstick's update.
- **The alienist and the Dweller on the Threshold** in the Place of Fear -- metaplanar figures rather
  than characters, with no names or statistics. Folded into the Place of Fear notes.
- **The runners' own fixers** -- the book says to use the standard SRM fixers from Mission Briefing
  and lets each player's existing contact make the 0200 call, reacting incredulously, dismayed or
  proud that Mr. Johnson asked for them by name.
- **Ares, Defiant, Enfield** -- manufacturer name-drops on gear only.
"""

PLAY_NOTES = """
- The book's own warning up front: this adventure focuses more on NPCs than most Shadowrun Missions
  adventures, and the GM should thoroughly read the Cast of Shadows before running it. Almost every
  encounter in the building is a person who has to be talked to, calmed, carried or worked around,
  and almost none of them are what they first appear.
- The money makes the morality mechanical. Patients are 200 nuyen per runner each and there are
  fifteen; employees are 200 each and there are ten plus three HTR; the data is 1,000 and 1,000;
  Heffernan alive and interrogable is 1,500 against 500 dead. A team that shoots its way through the
  finale is shooting its own payslip. The karma table doubles down: stopping Heffernan is worth 1
  point, stopping him without resorting to violence is worth 2, and rescuing at least three of the
  detailed NPC staff or patients is worth another.
- Trey "Boltar" Harris exists only for magic-poor teams and should not be offered otherwise. If the
  team has one or more spellcasters, do not offer the combat mage at all. Note that he has no stat
  block anywhere in the book.
- Mindgloom is optional and gated: run him only if there are one or more full magicians among the
  runners, and only after the players have met at least one patient. The two-way link between him
  and Heffernan is the scenario's real mechanism -- take one down and the other collapses -- so
  decide early which order your table is likely to reach them in.
- Deliberate misinformation is baked in. The security files Mr. Johnson hands over are contradicted
  by what the team finds, and his Matrix codes no longer work; he does not know either. He is also
  useless on magical questions. Do not let a player's frustration with him read as a GM error.
- Timing pressure is soft but real: twenty-four hours before Rose Croix expects the story to break,
  and no Lone Star, no media, ever. An astral quest for Mindgloom's true name takes 7D6 hours out of
  that budget.
- The Debugging line for the meet is worth remembering: if anyone hedges, point out that it has been
  a slow week, that Mr. Johnson asked for them specifically so refusing looks bad, and that if their
  own fixer is setting them up they are already screwed.
- Any PC who accepts Heffernan's offer of magical teaching and follows through is eliminated from the
  campaign and becomes an NPC at the end of the adventure. Say this out loud before a player commits.
- Debriefing Log boxes: Dr. Heffernan was captured / killed / escaped; Caring Gardens datafiles were
  recovered / lost; the patients and employees were rescued / most survived / killed; Initiation
  Ordeal Credit yes / no.
"""
