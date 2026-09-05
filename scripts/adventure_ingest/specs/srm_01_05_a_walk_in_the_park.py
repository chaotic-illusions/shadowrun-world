# SRM 01-05 A Walk In The Park (FanPro / WizKids, 2004, Shadowrun Missions Season One, SR3) --
# campaign order #48. Bellevue (the Hillside Student Community), Fort Lewis (the zoological park),
# an upper-class townhouse north of downtown, and a derelict warehouse on the outskirts of Everett's
# dock district. One Saturday, from an eight o'clock meet to a night-time firefight.
# SETTING NOTE / DISCREPANCY WITH THE TASK BRIEF: commissioned as "Denver in the 2060s (SR4 era)";
# the book is Seattle and "For use with Shadowrun, Third Edition". Denver is never mentioned. Every
# location carries city "Seattle".
# ARC NOTE: unlike SRM 01-01 through 01-04 this adventure carries no Campaign Background section and
# is not part of the Rose Croix story arc -- it describes itself only as "an adventure for the
# Shadowrun game system and the Shadowrun Missions campaign setting in particular". Its one link to
# the surrounding chapters is that Mark's mother works as a research biologist for Griffin
# Biotechnology, the company at the centre of SRM 00-03 and SRM 01-04.
# Dating: no in-world date is printed; the whole adventure happens on one Saturday, and its
# backstory is dated only relative to itself (fifteen years since the first sacrifice, thirty since
# the marriage, one year since Santiago found his ex-wife, three since Mark enrolled). YEAR follows
# the campaign at 2064.
# Editing inconsistencies in the book, noted again on the affected rows: the plot synopsis says the
# runners "will notice something strange about the Smiths" at the Sanchez house, where the
# introduction on p.5 says "something strange about the mother" -- there is no Smith anywhere in the
# adventure; the four younger students are rostered as "Mikey, Sara, Sally and Ramie" and then
# described as "Marc, Sara, Sally, Ramie", so the cat-tailed SURGE-ling has two names; "Atzlan
# University" and "back in Atzlan" appear against correct "Aztlan" elsewhere in the same book; the
# four older students are called "middle school aged" although they are 14, 15, 15 and 16; the first
# son is unnamed in the Background section and named Tomas in the prologue fiction; the venue is the
# "Fort Lewis Zoological Park" in the hire scene and the "Fort Lewis Zoo" in Menagerie's write-up;
# the Johnson is "Professor Samantha White" in the scene heading and "Ms. White" everywhere after;
# and the GRAB and Hired Thug stat blocks are the DocWagon Special Ops and Westin-Seattle hotel
# security blocks from SRM 01-01 reprinted with the gear swapped.
# Rows created by earlier specs are updated, never re-created: Manny and Pete/Petra Sprent come from
# specs/srm_00_01_mission_briefing.py, and Griffin Biotechnology from
# specs/srm_00_03_forced_recon.py. The student Sammy is filed as "Sammy (Hillside Student
# Community)" because an unrelated Sammy already exists in the campaign database.
# Source text: docs/Adventures/text/SRM01-05A_A_Walk_in_the_Park.txt (20 pages) and
# docs/Adventures/text/SRM01-05B.txt (player aids -- a warehouse map and the debriefing log; there is
# no screamsheet and there are no contact cards in this one).
# ASCII only (pre-commit hook).

ADVENTURE = "SRM 01-05 A Walk in the Park"
ORDER = 48
SOURCE = "SRM01-05A_A_Walk_in_the_Park.pdf, pp. 3-20; SRM01-05B.pdf (player aids)"
YEAR = "2064 (a single Saturday; no in-world date is printed and the backstory is dated only " \
       "relative to itself -- fifteen years since the first sacrifice)"

SYNOPSIS = """
Fifteen years ago a missed reagent cost **Aztechnology** millions of nuyen, and the corporation
took its recovery out of the man responsible in the only currency that mattered. **Dr. Joselito
Santiago**, chief biochemical engineer on a wonder drug that Ares and Shiawase were racing him for,
was demoted to research assistant, stripped of his perqs, and required to hand over his twelve-
year-old son **Tomas** -- watched by the corporate offices since testing revealed a latent gene for
magical ability, and therefore a valuable candidate for ritual sacrifice in the research teocalli.
Devotion, professional vanity and greed made Santiago agree. He spent his last night on the fold-out
couch because his wife was too distraught to be near, which is why he never learned she was
pregnant. He walked the boy to the temple in the morning, came home with a transfer to Seattle, and
found an empty house.

**Amanda** fled to Seattle, became Sanchez, bore **Mark**, and built a career as a research
biologist at **Griffin Biotechnology**. Santiago spent fifteen years being shunted from place to
place before his skills earned him back some prestige on the Aztechnology Seattle staff -- and then,
a year ago, he was invited to tour Griffin's new Everett facility, caught a glance through a lab
window, and discovered both his ex-wife and a second son he had never known existed. He did not feel
what a father feels. He had cut all ties with family; his family is the corporation. His first son
was sacrificed to correct an error. The second will be sacrificed to correct an injustice.

So on a Saturday morning the fixer **Manny** calls the runners about a bodyguarding job for some
VIPs who want fresh air, and **Professor Samantha White** of the **Hillside Student Community** --
white hair in a bun, no-nonsense, unafraid of shadowrunners -- hires them out of the principal's
office for two thousand nuyen apiece to chaperone eight magically active children to the **Fort
Lewis Zoological Park**. Keep them safe, and keep them from drawing attention: every one of them is
from a family that could be ransomed. It is a day of telekinetic ice cream, shoplifted souvenirs, a
Humanis demonstration at the gates, a reporter with a camera, and a boy whose uncontrolled luck
power makes birds attack whoever stands nearest him.

Then the cages open. **GRAB**, the team Santiago's secret savings hired, planted acid charges on
enclosures the night before and dosed the animals with something that makes them want to use the
gap. While the runners chase rhinos, GRAB moves on Mark -- and **Menagerie**, a toxic nature shaman
who came on an anonymous tip, is watching to see whether anybody hurts an animal.

Whether Mark is taken or not, the trail runs the same way: through the school's file, through a
seedy bar where Santiago's hired muscle drinks, and above all through Amanda's townhouse north of
downtown, where six wireless cameras feed a satellite dish that is aimed at nothing and a hacked
Aztechnology credstick names a woman who stopped existing fifteen years ago. The signal leads to an
old machine-parts warehouse on the edge of Everett's dock district, where a portable generator, a
round altar room behind one-way ballistic plexiglas, an Aztechnology shaman and two thugs per runner
are waiting for the ritual that will summon a blood spirit out of a fifteen-year-old boy.
"""

TIMELINE = """
- **~30 years ago** -- Joselito and Amanda meet at work in Aztlan and marry.
- **~18 years ago** -- Tomas Santiago turns twelve; Aztechnology testing reveals a latent gene
  associated with magical ability, and the corporate offices begin watching him.
- **15 years ago** -- Santiago's missed reagent wrecks the wonder-drug experiment, pushing the
  programme back at least two weeks while Ares and Shiawase race for the same protein chain. He is
  demoted to research assistant and required to give up his son. He spends the night on the couch;
  Amanda, who learned that morning that she is pregnant, says nothing. Next morning he takes Tomas
  to the teocalli. He returns with a Seattle transfer and an empty house.
- **15 years ago, weeks later** -- Amanda reaches Seattle, becomes Sanchez, and gives birth to Mark.
  She goes to work for Griffin Biotechnology.
- **The intervening years** -- Santiago is shunted from place to place until Seattle, where his work
  accelerates a project and wins Aztechnology significant pharmaceutical advances; over the past two
  years he is instrumental in bioware and pharmaceutical breakthroughs and recovers much of his pay
  and prestige.
- **~3 years ago** -- Mark begins to exhibit supernatural strength at puberty. Amanda, unsurprised,
  enrols him at the Hillside Student Community, telling the school he was removed from an abusive
  father's custody.
- **1 year ago** -- Santiago is invited to look over Griffin Biotechnology's new Everett facility,
  glimpses Amanda through a lab window, and learns there is a second son. He begins planning.
- **2 weeks ago** -- a "National Satellite" van spends three hours at the Sanchez townhouse
  installing a dish; six wireless cameras go in with it.
- **The last two weeks** -- Santiago hires two shadowrunner teams: GRAB for the abduction, and a
  crew of street thugs to secure the warehouse. Months earlier he had hired muscle to set the
  hideout up.
- **The night before** -- two GRAB members plant acid devices on animal cages across the zoo and
  inject the animals with a psychotropic aggression drug.
- **Saturday, early morning** -- Manny calls. 8:00 AM at 5027 159th Place SE, Bellevue.
- **Saturday, 9:00 AM to 5:00 PM** -- the zoo trip. Somewhere in it, the cages open and GRAB moves.
- **Saturday, afternoon** -- the school's file on Mark, the street, and the Sanchez townhouse.
- **Saturday, evening** -- the warehouse on the outskirts of Everett's dock district.
"""

ORGS = [
    {
        "name": "Hillside Student Community",
        "org_type": "private school",
        "tier": 2,
        "headquarters": "5027 159th Place SE, Bellevue, Seattle metroplex",
        "summary": "The metroplex's top private school for magically gifted children whose families do not work for the megacorps -- a former boarding school for the wealthy that hired specialists the moment magic returned",
        "description": (
            "A private school for gifted students in the Seattle area. It used to be a traditional "
            "boarding school for the wealthy and was one of the first to hire on specialists when "
            "magic returned to the world, which made it the top school for children who possess "
            "the magic genomes and can develop talents or abilities but whose families do not work "
            "for the megacorporations. Students board; the school takes them in at elementary age "
            "and keeps them into their late teens, and it runs Academic Improvement Plans that "
            "cover social development as seriously as academic progress. Its intake ranges from "
            "children of some of the richest and most influential families in the metroplex to a "
            "girl living on a scholarship funded by a security firm that wants to use her stealth "
            "abilities to test detection equipment. Run by Professor Samantha White out of a "
            "principal's office that looks exactly like a principal's office."
        ),
        "leadership": [
            {"name": "Professor Samantha White", "title": "Principal", "notes": "Hires the runners herself; archetypal school administrator, unafraid of shadowrunners."},
        ],
        "notes": (
            "The school's problem is the one that hires the runners: every student is from a family "
            "that could be subject to ransom, and every student is magically active and mostly "
            "unable to control it, so the two requirements -- bodyguards and chaperones -- are the "
            "same job. It has no discretionary funds for freelance protection (2,000 nuyen base per "
            "escort, scaling to 7,500 for prime runners, with up to 20 percent up front and a "
            "negotiation limit that never doubles the base) and no access to weapons or supplies "
            "whatever. Its safeguarding practice is real: doctors examined Mark for signs of the "
            "physical abuse his mother reported and found none, the school keeps what it believes "
            "about a student's background confidential even from the people it has hired to protect "
            "them, and it will only share Mark's file after the abduction attempt. Its judgement "
            "under pressure is good -- Ms. White suggests the runners keep watching the children "
            "until the situation is resolved rather than sending them back, and accepts their "
            "professional opinion if they disagree. Its judgement of children is worse: told to go "
            "home, the students will try to escape and investigate the kidnapping themselves. Eight "
            "students go on the trip -- Freddy, Winona, Sammy and Mark, aged 14 to 16 with moderate "
            "powers, and Mikey (Marc), Sara, Sally and Ramie, elementary aged with minor ones."
        ),
    },
    {
        "name": "GRAB",
        "org_type": "shadowrunner team",
        "tier": 3,
        "headquarters": "Seattle metroplex; no base given",
        "summary": "A six-strong professional shadowrunner team hired with a disgraced scientist's secret savings to abduct one boy out of a crowded zoo, and organised enough to have planned for every way it could go wrong",
        "description": (
            "A shadowrunning team of six, wired and cybered to a uniform standard and working as "
            "one -- the adventure's own summary is that 'in all situations, GRAB will work as a "
            "well organized team that has planed out every possible situation'. Their plan for the "
            "zoo is a professional's plan: two of them spent the night before planting devices on "
            "animal cages across the park that release a super acid capable of instantly dissolving "
            "both steel and plexiglas, and injecting the animals with a psychotropic drug to "
            "enhance their natural aggressiveness so that they would actually use the opening. On "
            "the day the rest of them are simply park visitors in ordinary clothes, waiting."
        ),
        "notes": (
            "Member block p.20 (six of them): B5 Q6 S6 C3 I5 W5, Ess 0.9, Magic 0, Reaction 5(10), "
            "Init 5+1d6 [10+3d6], Combat Pool 9, Karma Pool TR, Professional Rating 4/Professional; "
            "smartlink, hearing damper modification, datajack, cybereyes (flare compensation, "
            "rangefinder, thermographic), headware radio with Comlink-IV and Crypto-3, Wired "
            "Reflexes 2; Assault Rifles 3, Pistols 5, Unarmed 3, Armed Combat (Club) 2 (4), "
            "Throwing 4, Launch Weapons (Launchers) 2 (4), SMG 5, Athletics 3, Stealth 4, Etiquette "
            "2, Intimidation 4, Interrogation 4, Electronics 3; Shadowrunner Tactics 3; armoured "
            "vest (5/3); Ares Predator II heavy pistol (7M Stun, gel) and two flash-bang grenades "
            "(12S Stun, flash). Note the loadout: gel rounds and flash-bangs, because this is a "
            "snatch in a public park and they are not being paid for bodies. TACTICS: trigger the "
            "cages, let the runners go and be heroes, and take Mark while nobody is watching the "
            "children; if a runner stays with him, subdue that runner quietly without alerting the "
            "rest; if the distraction fails altogether, attack the team as a second distraction "
            "while another member walks Mark to the exit. OPSEC: Santiago deliberately told them "
            "only to take the boy, and arranged to page them the delivery address on special pagers "
            "once a hired pedestrian's mini-camcorder showed him the snatch had worked -- so a "
            "captured GRAB member never receives the page and has nothing to give up. They are paid "
            "off at the warehouse and leave before the finale. DISCREPANCY: the block is the "
            "DocWagon Special Ops Team from SRM 01-01 reprinted with different armour, weapons and "
            "knowledge skills."
        ),
    },
]

LOCATIONS = [
    {
        "name": "Hillside Student Community",
        "location_type": "private school",
        "city": "Seattle",
        "district": "Bellevue (5027 159th Place SE)",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "Hillside Student Community",
        "summary": "The Bellevue boarding school for magically gifted children where the runners are hired out of the principal's office at eight o'clock on a Saturday morning",
        "description": (
            "A private boarding school at 5027 159th Place SE in Bellevue, originally built for the "
            "wealthy and now the metroplex's leading school for magically gifted children outside "
            "the megacorporations. Runners arriving for the meet are directed, exactly as any "
            "visitor would be, to the principal's office -- and the book tells the GM to have fun "
            "with everything that entails. Professor Samantha White receives them there: white hair "
            "in a bun, an aura of authority, no experience of shadowrunners and no fear of them "
            "either, working from the advice of trusted associates that this is how you protect "
            "children on a day out. A school bus takes the party to Fort Lewis at nine."
        ),
        "notes": (
            "The hire scene, and the fallback for the whole adventure -- if the runners will not "
            "go and speak to Mark's mother, Ms. White calls and asks them to, so that Amanda hears "
            "what happened from them rather than from the news. Terms and the pay table are on the "
            "Hillside Student Community org row. The school will give the runners the Sanchez "
            "address and, after the abduction attempt, the file it has been keeping confidential: "
            "Mark arrived about three years ago, his mother reported that he was being abused by "
            "his father and had been removed from the father's custody when she left, she noticed "
            "supernatural strength and knew he had the genetic markers, and school doctors could "
            "find no signs of physical abuse at all. Returning the students here after the zoo is "
            "harder than it sounds: they want to help solve the mystery, and if refused they will "
            "try to escape and investigate on their own. Ms. White has already decided the runners "
            "are the safest place for them until it is over."
        ),
    },
    {
        "name": "Fort Lewis Zoological Park",
        "location_type": "zoo",
        "city": "Seattle",
        "district": "Fort Lewis",
        "security_level": "Patrolled / Commercial",
        "summary": "The zoo where eight magically active children spend a Saturday, and where a shadowrunner team dissolves the cages to cover an abduction",
        "description": (
            "A zoological park in Fort Lewis, popular enough with off-duty military personnel that "
            "there are always soldiers on leave in the crowd. Paranormal animals are showcased "
            "alongside the ordinary ones and are held in proper containment. The book deliberately "
            "supplies no map and tells the GM to draw one or print a real zoo's visitor brochure "
            "instead, which is the right instinct for a scene that is mostly comedy: gift shops, "
            "ice cream, cages, restrooms to get lost in, and enough distance between exhibits for "
            "eight children and their bodyguards to end up spread across half the park before "
            "anything goes wrong."
        ),
        "notes": (
            "SECURITY: the zoo already provides substantial protection and rates AA with Lone Star; "
            "the entrance carries sophisticated weapons detectors at MAD Rating 6, which is Ms. "
            "White's polite way of telling the team not to bring anything heavy. ZOO ENCOUNTERS "
            "(pick and choose): Sammy telekinetically torments animals, passers-by and babies; "
            "Humanis Policlub demonstrators at the gates surround a SURGE-affected or metahuman "
            "student and tell the 'freak' to leave; a Perception (6) spots the reporter Peter (or "
            "Petra) Sprent following the group; Winona slips into a gift shop or asks for the "
            "bathroom and comes back with things she did not have before (Perception (8)); and "
            "Freddy's uncontrolled Accident power afflicts whichever runner is nearest with a "
            "string of unfortunate events, which stops when he moves away. Pushing the envelope: "
            "have the children annoy someone who matters -- two Mafia members using the park as "
            "neutral public ground, a megacorporate figure, a politician -- so that the runners have "
            "to keep it quiet. THE ABDUCTION: GRAB's devices dissolve cages across the park (the "
            "GM picks the animals -- lions, black rhinoceros, a herd of zebras, badgers, emus, or "
            "for experienced tables cockatrices, wyrd mantis or a piasma), the students insist on "
            "helping, and GRAB moves on Mark while nobody is counting heads. Park personnel arrive "
            "with narcojet rifles and pistols at increased chemical strength for large animals -- "
            "10D Stun against a metahuman; taken during the encounter a weapon holds one round, and "
            "recovered afterwards none. Menagerie is somewhere in the crowd watching how the "
            "children and the runners treat the animals."
        ),
    },
    {
        "name": "The Sanchez Townhouse",
        "location_type": "apartment complex",
        "city": "Seattle",
        "district": "North of downtown",
        "security_level": "Corporate Standard",
        "summary": "Amanda Sanchez's upper-class townhouse, wired end to end with six hidden cameras feeding a roof dish that points at nothing -- and holding the photograph of a son who no longer exists",
        "description": (
            "An upper-class townhouse north of downtown in an A-level security area: a standard "
            "two-bedroom, two-and-a-half bath unit with the bedrooms upstairs, bought with a "
            "research biologist's salary and kept for two people. Amanda is not home when the "
            "runners arrive. What is in it is fifteen years of a life carefully assembled around a "
            "hole -- a photograph in her bedroom of herself, an adult Latino man and a Latino boy of "
            "about twelve who looks like Mark and is not Mark, and, kept rather than destroyed, the "
            "documents of the woman she stopped being."
        ),
        "notes": (
            "ENTRY: maglock Rating (4 + TR) with biometric sensors appropriate to the difficulty. "
            "If the team fails it, have the lock jam rather than alarm and let Amanda come home "
            "early -- she will tell them everything herself, by trickery, intimidation or plain "
            "asking. FINDS: the photograph; a graduation certificate from Atzlan University, a "
            "doctorate in biology in Amanda's name; and an Aztechnology identification credstick "
            "reading Amanda Santiago -- Computer (8) to hack, revealing her marriage to Joselito "
            "Santiago about thirty years ago in Aztlan and no records active after fifteen years "
            "ago. Perception (8) finds up to six wireless mini-camcorders through the house. THE "
            "DISH: the telecom satellite dish on the roof is a signal repeater carrying the camera "
            "feed to Santiago. It is aimed the wrong way -- not towards Texas, where the North "
            "American geosynchronous cable satellites orbit, but the opposite direction. Perception "
            "(4) notices the misaim, or a plain Perception test if they already know to look for a "
            "repeater, with Electronics (4) as a complementary test. The house telecoms work "
            "perfectly and Amanda subscribes to no satellite service at all -- her standard Matrix "
            "connection bill is on the counter. Intelligence or Electronics (5) traces the "
            "transmission to Santiago's hideout in Everett, which is the adventure's critical "
            "clue. THE NEIGHBOUR: Ed Griswald, watching through his curtains, will say that nobody "
            "but the woman and the boy has been to the house in over a week, and that the last "
            "visitors were a National Satellite telecom van two weeks ago whose 'cable guys' spent "
            "three hours on the roof. Amanda knows nothing about the dish or the cameras."
        ),
    },
    {
        "name": "Santiago's Warehouse",
        "location_type": "smugglers den",
        "city": "Seattle",
        "district": "Outskirts of Everett's dock district",
        "security_level": "Low Security",
        "summary": "An old machine-parts warehouse with a chain-link fence, a portable generator and a round altar room behind one-way ballistic plexiglas, isolated enough to finish a blood ritual in",
        "description": (
            "An old truck shipping and machine parts distributing facility on the outskirts of "
            "Everett's dock district, relatively isolated -- Santiago's whole plan is to be left "
            "alone long enough. Sturdy fabricated concrete, built twenty years ago, behind a locked "
            "chain link fence with a single BMW parked inside the gate. Inside it is cluttered with "
            "old boxes of machine parts and drums of dirty machine lubricant; there is a broken-down "
            "electric fork-lift, a dusty office, a reception area, a bathroom and a conference "
            "room, large pallet racks lining the walls, and wooden rafters going every which way "
            "overhead with exposed dirty nails in them. There is no electricity in the building; "
            "Santiago has installed a portable generator system for what he needs. And in the "
            "middle of the floor stands a round building -- the altar room -- surrounded by one-way "
            "bullet-resistant plexiglas windows at Barrier Rating 6, with a speaker mounted "
            "outside, and every trapping the ritual requires already in place."
        ),
        "notes": (
            "Set up with Santiago's untouched offshore savings, months ago, by street muscle he "
            "hired for the purpose -- who can be found in a seedy bar and will give up the address "
            "to persuasion, interrogation or bribery, along with the fact that he has hired two "
            "shadowrunner teams in the last fortnight. It is also his listening post: the wireless "
            "cameras in the Sanchez townhouse and the mini-camcorder carried by a hired pedestrian "
            "at the zoo both report here. THE FINALE: if Santiago has Mark the ritual is already "
            "starting and he warns the runners off over the outside speaker; if Mark was never "
            "taken, Santiago is out at a table with one of the thugs planning a second attempt, "
            "which the book offers as a deliberate reward for stopping the abduction. Roughly two "
            "hired thugs per player character are hidden through the building and spring out if the "
            "warning is ignored, putting the whole team into hand-to-hand at once (Surprise tests "
            "as normal). Sneaking in: both the thugs and Santiago get Perception tests, and the "
            "thugs have installed ultrasound motion sensors throughout at Rating 4. A Magic Theory "
            "or Sorcery test identifies what the altar room is for. The book's instruction is "
            "explicit -- this is meant to be a climactic battle and should be challenging, but the "
            "players should win it, with no more than a quarter of the team incapacitated -- and "
            "equally explicit that 'there is every chance that Mark may be accidentally killed "
            "during this scene. That is not necessarily a bad thing!'"
        ),
    },
]

NPCS = [
    {
        "name": "Dr. Joselito Santiago",
        "role": "The Aztechnology biochemist who gave one son to the corporation to save his career and has spent a year planning to give it the second",
        "archetype": "Corporate Scientist",
        "title": "Biochemist, Aztechnology Seattle; formerly chief biochemical engineer, Mexico City",
        "race": "Human",
        "gender": "Male",
        "nationality": "Aztlaner",
        "organization": "Aztechnology",
        "connection": 3,
        "description": (
            "A man who has spent fifteen years climbing back and has arrived somewhere worse than "
            "where he started. Beaten, he does not resist -- he resigns himself to defeat and will "
            "wait to fight another day -- and it is obvious by then that he has slipped past into "
            "the realm of madness. He explains himself readily and without shame: he has worked "
            "hard to regain favour with Aztechnology, and Mark holds the key to his redemption, "
            "because a boy who possesses the genes for magical expression can be sacrificed and the "
            "power harnessed by a shaman to summon a powerful blood spirit. His own accounting of "
            "the two killings is the coldest line in the book: his first son was sacrificed to "
            "correct an error, and his second would be sacrificed to correct an injustice."
        ),
        "background": (
            "Fifteen years ago he was chief biochemical engineer on an Aztechnology wonder drug "
            "built around a protein chain he had discovered himself, with Ares and Shiawase racing "
            "for the same key and a project manager pushing for early release. A missed reagent in "
            "his calculations wrecked the experiment, cost the corporation millions in research, "
            "public affairs and advertising, and pushed the programme back at least two weeks. The "
            "project manager and the vice president of biotechnology demoted him to research "
            "assistant and demanded a price paid in blood: his son Tomas, watched by the corporate "
            "offices since his twelfth birthday because testing showed a latent gene associated "
            "with magical ability, and therefore a valuable candidate for ritual sacrifice to power "
            "the more obscure procedures rumoured to take place in the research teocalli. Devotion, "
            "professional vanity and greed made him agree. He spent his last night at home on the "
            "fold-out couch because his wife was distraught, and so never learned she was pregnant. "
            "He took the boy to the temple at sunrise, came home to a transfer order and an empty "
            "house, and spent fifteen years being shunted from place to place before Seattle gave "
            "him a team where his skills accelerated a project and won the corporation significant "
            "pharmaceutical advances -- and with it, over the past two years, much of his pay and "
            "prestige. A year ago he was invited to look over Griffin Biotechnology's new Everett "
            "facility, caught a glance through a lab window, and discovered both the ex-wife he had "
            "never approached and the existence of a second son. He felt jubilation. He had cut all "
            "ties with family; his family is the corporation."
        ),
        "notes": (
            "Stats p.20: B3 Q4 S3 C4 I4 W6, Ess 4.9, Reaction 4, Init 4+1d6, Combat Pool 9, Karma "
            "Pool TR, Professional Rating 1/Unskilled; smartlink, datajack, head memory; Unarmed "
            "Combat 2, Etiquette 4, Computer 2, Electronics 3, Biotech 4; Biotechnology 8, "
            "Chemistry 8; no armour, no weapons. He is not a fighter and is not meant to survive as "
            "one -- the Professional Rating says Unskilled. Most of his public assets were frozen, "
            "but several secret savings were untouched and he has spent them: on GRAB, on an "
            "Aztechnology shaman who can perform the blood magic, on street muscle to set up the "
            "warehouse months ago, on a second team of thugs to guard it, on six wireless cameras "
            "and a repeater dish in his ex-wife's house, and on a pedestrian with a mini-camcorder "
            "at the zoo. His operational security is better than his sanity: GRAB were told only to "
            "take the boy and would be paged the delivery address afterwards, so a captured member "
            "knows nothing. AFTERMATH, which the book hands entirely to the table: do the runners "
            "let Santiago go, free to try this again? Do they help relocate Amanda and Mark? Do "
            "they kill the Azzie shaman or let him go?"
        ),
        "contact_skills": ["Aztechnology Seattle pharmaceutical research", "Biotechnology and chemistry"],
    },
    {
        "name": "Amanda Sanchez",
        "role": "Mark's mother -- formerly Amanda Santiago, Aztechnology doctor of biology, who fled Mexico City with an unborn son and a secret she has kept for fifteen years",
        "archetype": "Corporate Scientist",
        "title": "Research biologist, Griffin Biotechnology; born Amanda Santiago",
        "race": "Human",
        "gender": "Female",
        "nationality": "Aztlaner",
        "organization": "Griffin Biotechnology",
        "connection": 3,
        "description": (
            "A research biologist with a doctorate, a good salary, an upper-class townhouse north "
            "of downtown and a son at a private school -- a life built carefully enough that the "
            "only crack in it is a photograph she could not bring herself to throw away and a "
            "credstick in a dead woman's name. She is not home when the runners break in. Faced "
            "with them she tells the whole story without much prompting: her husband's utter "
            "devotion to Aztechnology, what it cost their first-born son, and why she left the next "
            "morning without telling him she was pregnant. Mark has never been given more than the "
            "one reason she can bear to say aloud -- that she was afraid his father would abuse "
            "him -- and asking about brothers or sisters makes her break down in sobs."
        ),
        "background": (
            "She met Joselito at work in Aztlan almost thirty years ago and married him about "
            "thirty years ago; she took a doctorate in biology from Atzlan University and worked as "
            "a biologist in her own right. When he came home fifteen years ago and told her what "
            "the corporation had demanded, she burst into tears and fled the room, and he assumed "
            "it was for Tomas alone; she had learned that morning that she was pregnant again, and "
            "took the secret with her when she left the next day. She fled to Seattle, changed her "
            "identity to Sanchez, gave birth to Mark, and went to work for a local biotechnology "
            "research and development firm -- Griffin Biotechnology -- where she worked her way up "
            "the corporate ladder to a comfortable living. The note she left made quite clear what "
            "she thought of a man who would sacrifice his own son to save his job, and she has "
            "broken off all contact and heard nothing from him since. When Mark entered puberty and "
            "began exhibiting extraordinary abilities she was not surprised: her first son had been "
            "a powerful latent, which is precisely why Aztechnology wanted him. She used her "
            "position and her money to enrol Mark at the Hillside Student Community, telling the "
            "school he had been removed from an abusive father's custody."
        ),
        "notes": (
            "No statistics; she is a scene, not a fight. Talking to her is the key clue of the "
            "adventure, and if the runners do not go, Ms. White phones and asks them to -- Amanda "
            "should hear what happened to Mark from them before she sees it on the news. She knows "
            "nothing about the six cameras in her house or the repeater on her roof, which is what "
            "makes her dangerous to be near: Santiago has been watching her and her son for weeks. "
            "The debugging path is generous -- a jammed maglock and an early homecoming produce the "
            "same information a burglary would, minus the surveillance gear. She is also the "
            "adventure's one connection to the rest of Season One: a Griffin Biotechnology research "
            "biologist, which is how Santiago found her in the first place, on a tour of the same "
            "Everett compound the runners robbed in SRM 01-04. The unresolved question after the "
            "warehouse is hers: Santiago knows where she lives, and will wait to fight another day."
        ),
        "contact_skills": ["Griffin Biotechnology research staff", "Biology and biotechnology"],
    },
    {
        "name": "Mark Sanchez",
        "role": "The fifteen-year-old physical adept the whole adventure is about -- the son Santiago never knew he had, and the sacrifice he intends to make of him",
        "archetype": "Physical Adept",
        "title": "Student, Hillside Student Community",
        "race": "Human",
        "gender": "Male",
        "age": 15,
        "organization": "Hillside Student Community",
        "connection": 2,
        "description": (
            "A seemingly withdrawn fifteen-year-old with uncanny strength. Quiet -- he will not "
            "speak unless spoken to -- and entirely cooperative: he does what he is told and causes "
            "the runners no trouble at all, which in a party of eight magically active children "
            "makes him easy to lose track of. That is exactly what GRAB is counting on."
        ),
        "background": (
            "Born in Seattle weeks after his mother fled Mexico City. He knows nothing about his "
            "father or what happened before she left -- only that there is something horrible "
            "between his parents, because she never talks about him, and that asking about brothers "
            "or sisters once made her break down in sobs. The only reason he has been given for the "
            "flight is that his mother was afraid his father would abuse him. He came to the "
            "Hillside Student Community about three years ago, when his mother noticed he was "
            "developing supernatural strength and knew he carried the genetic markers for Awakened "
            "powers. The school believes he was abused and has been trying to help him come to "
            "terms with it; its doctors found no physical signs of anything. He is developing as a "
            "physical adept and is mostly quiet and withdrawn from the other students."
        ),
        "notes": (
            "Stats p.19: B5 Q5 S6 C3 I5 W5, Ess 6, Reaction 5, Init 1d6, Karma Pool 3, Professional "
            "Rating 2; Etiquette 2 (Corporate 4), Athletics 5; Standard Education 4; Attribute Boost "
            "(Strength) 6, Increased Athletics 3. The plot does not depend on keeping him: 'the "
            "abduction of Mark is not critical to the adventure', and stopping it is worth 2 Karma "
            "against 1 for rescuing him afterwards. The debriefing log records whether he was "
            "kidnapped and whether he was rescued or killed, and the book is blunt that he may well "
            "be killed accidentally in the final firefight and that this is 'not necessarily a bad "
            "thing'. What none of the adults will tell him, and what the runners are left holding, "
            "is the whole of it: that he had a brother, that his father killed him for a promotion, "
            "and that his father has spent a year planning to do the same to him."
        ),
    },
    {
        "name": "Tomas Santiago",
        "role": "Santiago's first son, given to Aztechnology's teocalli at twelve to pay for his father's mistake",
        "archetype": "Sacrifice",
        "title": "Son of Joselito and Amanda Santiago (deceased)",
        "race": "Human",
        "gender": "Male",
        "age": 12,
        "connection": 1,
        "description": (
            "A boy of about twelve in a photograph in his mother's bedroom, standing with her and "
            "an adult Latino man. He looks like Mark and is not Mark, and working that out is the "
            "moment the adventure turns. In the one image his father kept of him he is simply "
            "standing there with big brown eyes, 'as if he could see the entire universe at once' "
            "-- the one sight of his son that Joselito would remember."
        ),
        "background": (
            "Aztechnology's corporate offices began watching him at twelve, when testing revealed he "
            "possessed a latent gene known to be involved with magical ability. He never "
            "demonstrated any ability or power that would have interested the thaumaturgy division, "
            "but latent ability alone made him a valuable and powerful candidate for ritual "
            "sacrifice to power some of the more obscure procedures rumoured to take place in the "
            "secret confines of the corporation's research teocalli. When his father's error cost "
            "the corporation millions, the price of recovery was set at the boy's life. His father "
            "agreed, spent one last night in the house, and walked him to the temple at sunrise "
            "under the smog above Mexico City."
        ),
        "notes": (
            "No statistics; dead fifteen years before the adventure opens. He is a row because he "
            "is the reason for every other row: the photograph in Amanda's bedroom is the physical "
            "clue that breaks the case, his existence is what she has never been able to tell Mark, "
            "and his sacrifice is the precedent Santiago is following. NAMING: he is named Tomas "
            "only in the Blood Ties prologue; the Background section calls him just 'his first born "
            "and only son'. Note also what his existence establishes about Aztechnology in this "
            "campaign -- that the corporation tests employees' children for latent magical genes, "
            "keeps a watching file on those who have them, and calls them in as payment."
        ),
    },
    {
        "name": "Professor Samantha White",
        "role": "Principal of the Hillside Student Community and the runners' Johnson -- a school administrator hiring shadowrunners because trusted associates told her to",
        "archetype": "Educator",
        "title": "Principal, Hillside Student Community",
        "race": "Human",
        "gender": "Female",
        "organization": "Hillside Student Community",
        "connection": 3,
        "description": (
            "The archetypal school administrator, and the book means it as a compliment. White hair "
            "done up in a bun, definitely no-nonsense, projecting an aura of authority across a "
            "principal's desk at eight o'clock on a Saturday morning. She is definitely not used to "
            "dealing with shadowrunners and she does not fear them either; she only knows that "
            "trusted associates have told her this is the best way to protect the students on their "
            "trip, and she proceeds on that basis with complete composure."
        ),
        "background": (
            "She runs a school that used to be a boarding school for the wealthy and became, when "
            "magic returned, the top school in the metroplex for gifted children whose families do "
            "not work for the megacorporations. That means her students are simultaneously "
            "magically active, largely unable to control it, and drawn from families rich enough to "
            "be worth ransoming -- so a reward field trip to the zoo is a security problem she has "
            "no budget for. She hires the runners as bodyguards and chaperones in the same breath, "
            "briefs them on each child's powers, personality and description, and refuses to go any "
            "further than that, because more in-depth personal information is confidential."
        ),
        "notes": (
            "No statistics. TERMS: 2,000 nuyen base per escort for green runners with a 2,200 limit, "
            "rising through 2,200/2,500, 2,500/4,000, 4,000/5,000 and 5,000/7,500 to 7,500/10,000 "
            "for prime; payment on completion, up to 20 percent up front if negotiated; the school "
            "has no access to weapons or other supplies. If the team balks at the pay, the argument "
            "is reputation, not money -- these are the children of some of the richest and most "
            "influential families in Seattle that do not work for the megacorps -- and a runner who "
            "still refuses is simply out of the adventure. Her judgement carries the middle of the "
            "adventure: she phones the runners to ask them to break the news to Amanda Sanchez "
            "before the trid does, and she would rather the children stayed with the team than "
            "came back to school while a kidnapper is still at large, though she will defer if the "
            "runners insist. NAMING: 'Professor Samantha White' in the scene heading, 'Ms. White' "
            "everywhere afterwards, and the book notes with some amusement that White 'turns out to "
            "be her real name'."
        ),
        "contact_skills": ["The Awakened-child education circuit in the metroplex", "Wealthy non-corporate Seattle families"],
    },
    {
        "name": "Menagerie",
        "role": "A toxic nature shaman and animal-rights extremist who came to the zoo on an anonymous tip and will attack anyone who harms an animal, whatever the reason",
        "archetype": "Toxic Shaman",
        "title": "Animal rights activist and shadowrunner",
        "race": "Human",
        "gender": "Female",
        "connection": 3,
        "description": (
            "A well-known animal rights activist and shadowrunner, somewhere in a Saturday crowd at "
            "the zoo, watching a school party carefully to see how they react to and treat the "
            "animals. She makes no move and no announcement until somebody does something to an "
            "animal, at which point she attacks in one of her various animal forms. The line she "
            "draws is not the one a reasonable person would draw: freeing the animals does not "
            "count against GRAB, because she is not sure they did it, while stunning a rampaging "
            "rhinoceros to stop it trampling a bystander does count, and is enough to bring her "
            "down on the runner who did it."
        ),
        "background": (
            "A nature shaman who has taken an extremist path when it comes to protecting and "
            "preserving animals, and has gone toxic on it. She is at the Fort Lewis Zoo today "
            "because of an anonymous tip that a group of 'special children' from the school was "
            "coming, and she wants to be certain they pose no threat to the animals -- which is "
            "either an unrelated coincidence or the same rumour mill that carried the news to "
            "Humanis Policlub. The book does not say who tipped her."
        ),
        "notes": (
            "Stats p.20: B3 Q4 S3 C3 I6 W5, Ess 6, Reaction 5, Init 1d6, Karma Pool 8, Professional "
            "Rating 3; Sorcery 6, Conjuring 6; Paranormal Animals 6, Zoology 6; Magic Rating 6, "
            "non-initiate, toxic rating 1; Chaotic World 6, Manabolt 5, Calm Animal 6, Shapechange "
            "6. Note what that spell list means for the scene: she can end the animal stampede "
            "single-handed with Calm Animal and will not, because the animals are not the ones she "
            "considers dangerous. She is the trap inside the rescue -- the Karma award for stopping "
            "the stampede without damaging the animals is worth a point, and Menagerie is what "
            "happens to a team that takes the efficient route instead. Left alive she is a "
            "recurring hazard for any run that touches animals, a genuine expert on paranormal "
            "critters, and a shadowrunner in her own right who now knows the team's faces."
        ),
        "contact_skills": ["Paranormal animals and zoology", "Animal rights networks and eco-activist cells"],
    },
    {
        "name": "Freddy \"Red\"",
        "role": "Sixteen-year-old student whose uncanny luck comes with a side effect that makes everyone dislike him -- and whose Accident power afflicts whichever runner stands nearest",
        "archetype": "Awakened Student",
        "title": "Student, Hillside Student Community",
        "race": "Human",
        "gender": "Male",
        "age": 16,
        "organization": "Hillside Student Community",
        "connection": 1,
        "description": (
            "A quiet sixteen-year-old boy with no friends. The book's assessment is unsparing: 'It "
            "seems he is just not a very likable person.' On the rare occasion a new student takes "
            "to being Freddy's friend, that poor student is affected by his magical powers, and the "
            "friendship does not last. He has been at the school three years and his Academic "
            "Improvement Plan still calls for gains in social development that have yet to make "
            "adequate progress."
        ),
        "background": (
            "The school is not sure of the specific nature of his powers. What it knows is that he "
            "can affect luck and is himself lucky to an uncanny degree, and it believes his main "
            "power is exactly that -- being very lucky -- with the side effect of causing people not "
            "to like him. He has somehow gained the spirit power Accident and has no ability to "
            "control it, which means the misfortune simply happens to whoever is nearby, "
            "indefinitely, for as long as he is there."
        ),
        "notes": (
            "Stats p.17: B2 Q3 S2 C1 I4 W5, Ess 6, Reaction 3, Init 1d6, Karma Pool 2, Professional "
            "Rating 1; Fencing 3, Etiquette 1 (High Society 2), Negotiation 2; Standard Education "
            "4; Accident, as per the spirit power. Run the Unlucky Day encounter without dice: pick "
            "a runner and give them a series of unfortunate events -- a slip and a fall, bird "
            "droppings on the head, an unprovoked attack by a bird -- and end it when Freddy moves "
            "away. The temptation the scene creates is worth playing for: the runner will work out "
            "the pattern and want the boy kept at a distance, which is precisely how a fifteen-year "
            "history of nobody liking Freddy gets made, one reasonable decision at a time. Charisma "
            "1 and a Fencing skill are the whole of his character sheet and most of his character."
        ),
    },
    {
        "name": "Winona",
        "role": "Fourteen-year-old elf who can wrap herself in shadow and silence, and steals compulsively because she used to have to",
        "archetype": "Awakened Student",
        "title": "Student, Hillside Student Community (security-firm scholarship)",
        "race": "Elf",
        "gender": "Female",
        "age": 14,
        "organization": "Hillside Student Community",
        "connection": 1,
        "description": (
            "A cute fourteen-year-old elven girl, half Latina, who can envelop herself in shadow "
            "and silence and move like a panther. She knows she is cute and uses it: caught "
            "stealing, she has learned to look her way out of serious trouble, and it works often "
            "enough to be a strategy. Her Etiquette specialisation is Street, which in a school full "
            "of the children of the metroplex's richest families says everything about where she "
            "came from."
        ),
        "background": (
            "Winona spent much of her life living on the streets before coming to the school, and "
            "on the streets stealing was how she survived. She understands perfectly well that "
            "stealing is wrong; the compulsion to take things that do not belong to her is "
            "psychological and it has outlasted the need. Her powers feed it, and it feeds them. She "
            "is at the Hillside Student Community on a scholarship funded by a security firm that "
            "wants to use her abilities to test detection equipment -- which is to say that the one "
            "child in the party who is not from a wealthy family is there because a corporation "
            "found a use for her."
        ),
        "notes": (
            "Stats p.18: B2 Q6 S2 C4 I5 W4, Ess 6, Reaction 5, Init 1d6, Karma Pool 3, Professional "
            "Rating 1; Etiquette 4 (Street 5), Stealth 5; Standard Education 5; Stealth 3, Magic "
            "Fingers 2, Shadow 3; various trinkets stolen from others. Zoo encounter: she slips into "
            "a gift shop for souvenirs, or asks to use the bathroom and uses being left alone to go "
            "wherever she likes -- Perception (8) notices she has a few extra things she did not "
            "have before. A team that handles this by taking the trinkets back and saying nothing "
            "has understood the assignment better than one that reports her. Her scholarship is a "
            "standing hook: the security firm paying for her education has plans for a fourteen-"
            "year-old who can walk through detection systems."
        ),
    },
    {
        "name": "Sammy (Hillside Student Community)",
        "role": "Fifteen-year-old psychokinetic in a wheelchair, the school's natural leader and the author of every scheme in it, who likes tormenting animals",
        "archetype": "Awakened Student",
        "title": "Student, Hillside Student Community",
        "race": "Human",
        "gender": "Male",
        "age": 15,
        "organization": "Hillside Student Community",
        "connection": 1,
        "description": (
            "Fifteen, bound to an electric wheelchair since birth, and already possessed of "
            "psychokinetic powers strong enough that the teachers and scientists at the school "
            "expect him to become a very powerful sorcerer. A natural leader among his peers whom "
            "many look to as a friend, and simultaneously the class clown who does not listen in "
            "lessons and is behind every plan to cause chaos on the premises -- if students are in "
            "trouble at the school, Sammy hatched it. Deep down a good boy with mischievous "
            "tendencies. He is currently working on using his powers to walk like other boys and "
            "girls his age."
        ),
        "background": (
            "The powers arrived early in puberty and arrived strong. Sammy has grown up with the "
            "one thing that separates a wheelchair user from everyone else being answerable by "
            "will, and has not yet solved it -- but he has solved every smaller problem in between, "
            "which is where the mischief comes from. The book's summary of his favourite pastime is "
            "matter-of-fact and slightly appalling: 'Like other boys his age, he likes to torment "
            "animals. Tormenting animals is extremely fun when you have invisible psychokinetic "
            "powers!'"
        ),
        "notes": (
            "Stats p.18: B1 Q2 S1 C4 I6 W6, Ess 5, Reaction 4, Init 1d6, Karma Pool 5, Professional "
            "Rating 1; Etiquette 3 (High Society 4), Negotiation 3 (Fast Talk 5); Standard Education "
            "5; Levitation 4, Magic Fingers 4, Clout 3, Physical Barrier 3; electric wheelchair. Zoo "
            "encounter (Don't Poke the Monkey): he uses telekinesis to poke unsuspecting animals, "
            "people or babies, trip a passer-by, or push someone's ice cream cone into their face. "
            "Note the collision the adventure builds and never points out -- Sammy's favourite game "
            "is tormenting animals, and Menagerie is in the crowd waiting for exactly that, though "
            "as written she only reacts to real harm. Physical Barrier 3 and Fast Talk 5 also make "
            "him the single most useful child in the party during the stampede, if a runner thinks "
            "to ask him."
        ),
    },
    {
        "name": "Marc (Mikey)",
        "role": "Elementary-aged student and obvious SURGE-ling with a long cat-like tail; the roster and the description give him two different names",
        "archetype": "Awakened Student",
        "title": "Student, Hillside Student Community",
        "race": "Human",
        "gender": "Male",
        "organization": "Hillside Student Community",
        "connection": 1,
        "description": (
            "An obvious SURGE-ling with a long cat-like tail, and one of the four elementary-aged "
            "children on the trip -- typical rambunctious primary-school kids with only minor "
            "magical powers. The tail is the point of him as far as the adventure is concerned: he "
            "is visibly, unmistakably not baseline human in a public park, which is exactly what the "
            "Humanis Policlub demonstrators at the gate are looking for."
        ),
        "background": (
            "SURGE-affected from birth or early childhood and enrolled at the Hillside Student "
            "Community with the rest of the metroplex's gifted children. The book gives him no "
            "history beyond the tail; what it gives him instead is a role, as one of the two "
            "obviously non-human children the runners are responsible for keeping out of an "
            "argument."
        ),
        "notes": (
            "Shared elementary block p.19: B1 Q3 S1 C3 I3 W2, Ess 6, Reaction 3, Init 1d6, Karma "
            "Pool 1, Professional Rating 1; no active skills; Standard Education 2. NAMING "
            "DISCREPANCY: the roster lists the four younger students as 'Mikey, Sara, Sally and "
            "Ramie' and then the descriptions cover 'Marc, Sara, Sally, Ramie' -- the cat-tailed "
            "child has both names in the same two pages and the book never reconciles them. Plot "
            "use: the Humanis encounter needs a SURGE-affected or metahuman student for the "
            "demonstrators to surround and call a freak, and he and Ramie are the obvious "
            "candidates. The demonstrators are unarmed normals who will happily brawl and will be "
            "as loud as possible about defenceless people being beaten up; the challenge is "
            "defusing it quietly with an eight-year-old in the middle."
        ),
    },
    {
        "name": "Sara",
        "role": "Elementary-aged student, identical twin to Sally, who can periodically cast Detect Emotions",
        "archetype": "Awakened Student",
        "title": "Student, Hillside Student Community",
        "race": "Human",
        "gender": "Female",
        "organization": "Hillside Student Community",
        "connection": 1,
        "description": (
            "One half of a pair of identical twins who like nothing better than playing games with "
            "adults who get confused about which of them is which -- a game the runners are going "
            "to be playing all day while counting heads in a crowded zoo. The quieter of the two, "
            "and the one who notices things: she has the periodic ability to cast Detect Emotions."
        ),
        "background": (
            "Elementary-aged, at the school with the other minor talents, and one of a pair whose "
            "connection nobody at the school has formally established. She and Sally often finish "
            "each other's sentences and know what the other is thinking, which the staff have "
            "written down as an apparent emotional link and left at that."
        ),
        "notes": (
            "Shared elementary block p.19: B1 Q3 S1 C3 I3 W2, Ess 6, Reaction 3, Init 1d6, Karma "
            "Pool 1, Professional Rating 1; Standard Education 2; Detect Emotions 2, periodically. "
            "Two things a GM should use her for. First, the twins swapping places is the cheapest "
            "possible way to make a headcount go wrong at the exact moment GRAB moves on Mark. "
            "Second, a small child who periodically reads emotions is in a crowd of park visitors "
            "of whom six are a professional abduction team waiting for a signal -- if the runners "
            "ever think to ask her whether anyone feels wrong, she can answer."
        ),
    },
    {
        "name": "Sally",
        "role": "Elementary-aged student, the more outgoing twin, known to cast Control Emotions",
        "archetype": "Awakened Student",
        "title": "Student, Hillside Student Community",
        "race": "Human",
        "gender": "Female",
        "organization": "Hillside Student Community",
        "connection": 1,
        "description": (
            "Slightly more outgoing than her identical twin sister Sara, and the one more likely to "
            "start the which-of-us-is-which game with an adult. Where Sara reads emotions, Sally has "
            "been known to change them -- which in a small child with minor powers and no training "
            "is a rather larger thing than the school's write-up makes it sound."
        ),
        "background": (
            "Elementary-aged, with the same unofficial emotional link to Sara that the staff have "
            "noted without explaining: they finish each other's sentences and know what the other "
            "is thinking. Both are at the school for minor powers rather than the moderate ones "
            "that the older four have, and both are along on the zoo trip as a reward."
        ),
        "notes": (
            "Shared elementary block p.19: B1 Q3 S1 C3 I3 W2, Ess 6, Reaction 3, Init 1d6, Karma "
            "Pool 1, Professional Rating 1; Standard Education 2; has been known to cast Control "
            "Emotions 3. That is a manipulation spell in the hands of an unsupervised primary-school "
            "child, and it is the single most likely way for the day to go wrong without any help "
            "from GRAB -- a Humanis demonstrator, a zoo employee or a bodyguard whose mood suddenly "
            "changes for no reason. It is also, in the hands of a GM who wants to reward the "
            "runners for building trust with the children, a genuine asset during the Humanis "
            "confrontation."
        ),
    },
    {
        "name": "Ramie",
        "role": "Elementary-aged student with solid grey pupil-less eyes who slips into astral perception without meaning to",
        "archetype": "Awakened Student",
        "title": "Student, Hillside Student Community",
        "race": "Human",
        "gender": "Male",
        "organization": "Hillside Student Community",
        "connection": 1,
        "description": (
            "A sweet young boy with strange eyes -- solid grey with no apparent pupil. The book "
            "calls them quite beautiful and notes in the same breath that they also mark him as an "
            "obvious SURGE-ling, which is the whole of a SURGE child's experience in one sentence. "
            "He often slips into astral perception, without deciding to and without being able to "
            "explain it afterwards."
        ),
        "background": (
            "Elementary-aged and at the school for minor powers. Nothing else of his history is "
            "given, but the two facts he has are load-bearing: he is visibly not baseline, and he "
            "sees the astral without being asked to. In a party of eight children in a public park "
            "he is both the most likely target for a Humanis demonstrator and the only person "
            "present who might notice a toxic shaman standing in the crowd."
        ),
        "notes": (
            "Shared elementary block p.19: B1 Q3 S1 C3 I3 W2, Ess 6, Reaction 3, Init 1d6, Karma "
            "Pool 1, Professional Rating 1; Standard Education 2; often slips into astral "
            "perception. The adventure never uses this and a GM absolutely should: Menagerie's aura "
            "is toxic, GRAB are heavily cybered, and a small boy who keeps drifting onto the astral "
            "in the middle of a crowded zoo is the party's early warning system if anyone listens "
            "to him. He is also, with Marc, the child the Humanis demonstrators pick out, and the "
            "one whose eyes make him impossible to disguise on the way out if the runners ever need "
            "to move the children quietly."
        ),
    },
    {
        "name": "Ed Griswald",
        "role": "The Sanchez family's nosey neighbour -- a work-from-home web developer with a fetish for the glorified life of shadowrunners, who saw the satellite van",
        "archetype": "Civilian",
        "title": "Web page developer; neighbour of Amanda Sanchez",
        "race": "Human",
        "gender": "Male",
        "age": 32,
        "connection": 2,
        "description": (
            "In his early thirties, works at home as a web page developer, and has been watching "
            "the runners through his curtains since the moment they arrived. He has a particular "
            "fetish for the glorified life of shadowrunners, which means that a team who would "
            "normally expect a neighbour to call Lone Star instead gets a delighted witness who "
            "wants to talk to them."
        ),
        "background": (
            "Lives next door to Amanda Sanchez in an A-level security block north of downtown, "
            "spends his working day at home with a view of the street, and pays attention to it. "
            "The book gives him no more history than that, which is exactly enough: the value of Ed "
            "Griswald is that he has been at the window every day for two weeks."
        ),
        "notes": (
            "No statistics. Questioned, he says that nobody other than the woman and the boy has "
            "been to the house in over a week, and that the last visitor was a National Satellite "
            "telecom company van parked outside -- the cable guys installed a satellite system on "
            "the roof and were there about three hours, two weeks ago, and nobody has come or gone "
            "since. That is the entire solution to the townhouse handed over for the price of "
            "talking to him: a dish Amanda never ordered, installed by a company she does not "
            "subscribe to, in the same fortnight the cameras went in. He is the reward for the team "
            "that knocks on doors instead of picking locks, and the one witness who can put a "
            "timeline on Santiago's surveillance."
        ),
        "contact_skills": ["Who comes and goes on his street", "Web development"],
    },
]

ORG_UPDATES = {
    "Aztechnology": {
        "notes_append": (
            "SRM 01-05 A Walk In The Park (Seattle and, in flashback, Mexico City): the corporation "
            "as an employer, in the bluntest terms the campaign has used. Fifteen years ago Dr. "
            "Joselito Santiago was chief biochemical engineer on an Aztechnology wonder drug built "
            "around a protein chain he had discovered, with Ares and Shiawase racing for the same "
            "key, the corporation pushing for early release, and public mistrust already running "
            "after the first clinical trials were conducted on metahumans. A missed reagent in his "
            "calculations wrecked the experiment, cost millions in research, public affairs and "
            "advertising, and pushed the programme back at least two weeks. The project manager and "
            "the vice president of biotechnology demoted him to research assistant, stripped his "
            "perqs -- and required the sacrifice of his twelve-year-old son. THE PRACTICE: the "
            "corporate offices had been keeping an eye on the boy since his twelfth birthday, when "
            "testing revealed he possessed a latent gene known to be involved with magical ability. "
            "He never demonstrated any power that would have attracted the thaumaturgy division, "
            "but even latent ability made him 'a valuable and powerful candidate for ritual "
            "sacrifice to power some of the more obscure procedures that were rumored to take place "
            "in the secret confines of the corporation's research teocalli'. So: Aztechnology tests "
            "its employees' children for latent magical genes, keeps a file on those who have them, "
            "and calls them in as payment for failure. Santiago walked his son to the teocalli at "
            "sunrise and was transferred to Seattle. Over the last two years he has been "
            "instrumental in recent breakthroughs in bioware and pharmaceuticals on the "
            "Aztechnology Seattle staff and has recovered much of his pay and prestige. He now "
            "believes a second sacrifice will restore him fully, has hired an Aztechnology shaman "
            "capable of the blood magic rituals, and intends to summon a powerful blood spirit from "
            "his son's death and return to Aztlan a hero. Whether the corporation actually asked "
            "for any of this, or knows about it, the book never says -- Santiago's assets were "
            "frozen and he is paying for it out of secret savings, which suggests he is doing it on "
            "spec. The runners end the adventure holding a captured Azzie blood shaman and the "
            "choice of what to do with him."
        ),
        "leadership_add": [
            {"name": "Dr. Joselito Santiago", "title": "Biochemist, Aztechnology Seattle", "notes": "Formerly chief biochemical engineer, Mexico City; sacrificed his first son to the teocalli."},
        ],
    },
    "Aztlan": {
        "notes_append": (
            "SRM 01-05 A Walk In The Park (backstory, Mexico City): the Santiago marriage, the "
            "Atzlan University doctorate in biology that Amanda Santiago took there, and the "
            "corporate teocalli where their first son was sacrificed all sit in Aztlan, thirty and "
            "fifteen years back respectively. Amanda's Aztechnology identification credstick, "
            "hackable at Computer (8), records the marriage about thirty years ago in Aztlan and no "
            "records active after fifteen years ago -- which is what a woman who walked out of the "
            "country with an unborn child and a new surname looks like in a database. Joselito's "
            "ambition throughout the adventure is stated as returning to Aztlan a hero. NOTE: the "
            "book prints 'Atzlan University' and 'back in Atzlan' against correct spellings "
            "elsewhere in the same text."
        ),
    },
    "Griffin Biotechnology": {
        "notes_append": (
            "SRM 01-05 A Walk In The Park (Seattle, 2064): Griffin is described from the outside "
            "here, by a rival megacorp's biochemist -- 'one of the biomedical firms in the Seattle "
            "sprawl, not one of the megas, but an independent outfit that did cutting research and "
            "development of biotechnology for some of the larger corps and the big megacorps like "
            "Shiawase and Yamatetsu'. More importantly, this adventure gives the company a named "
            "employee who matters: Amanda Sanchez, a research biologist who has worked her way up "
            "the corporate ladder there since arriving in Seattle fifteen years ago, is in fact "
            "Amanda Santiago, formerly of Aztechnology in Aztlan, living under a changed identity "
            "with a son she has never told anyone about. Griffin 'knew nothing of his connection to "
            "the woman known as Amanda Sanchez'. The security hole that starts the adventure is a "
            "courtesy: Dr. Joselito Santiago of Aztechnology Seattle was INVITED to look over "
            "Griffin's new Everett facility about a year ago, and used the tour to catch a glance "
            "into a lab and confirm that his ex-wife worked there. Everything that follows -- a "
            "year of surveillance, an abduction at a zoo and a blood ritual in a warehouse -- comes "
            "out of a visitor pass. For a GM running the season in order, this is a fourth "
            "independent party that has walked information out of the Everett compound, after "
            "Paladin's reconnaissance runs, its datasteal, and whoever probed the site before it "
            "opened."
        ),
        "leadership_add": [
            {"name": "Amanda Sanchez", "title": "Research biologist", "notes": "Formerly Amanda Santiago of Aztechnology; living under a changed identity."},
        ],
    },
    "Humanis Policlub": {
        "notes_append": (
            "SRM 01-05 A Walk In The Park (Fort Lewis, 2064): hearing a rumour that a group of "
            "gifted youngsters from the Hillside Student Community is visiting the zoo, Humanis "
            "members stage a demonstration outside the gates, and some of them decide to start "
            "trouble -- several surround one of the SURGE-affected or metahuman students and tell "
            "the 'freak' to leave the zoo. They are ordinary people (3 in all attributes and "
            "abilities), carry no weapons, and are perfectly willing to get into a brawl; if a "
            "fight starts they will be as loud as possible so that it looks like shadowrunners "
            "beating up defenceless normal people. The scene is written as a test of whether the "
            "team can defuse something quietly with a child in the middle of it, not as a combat. "
            "Note how the rumour reached them at all: a school field trip is not secret, and Ms. "
            "White's whole reason for hiring bodyguards is that these children are worth taking."
        ),
    },
    "Lone Star Security": {
        "notes_append": (
            "SRM 01-05 A Walk In The Park (Fort Lewis, 2064): the Fort Lewis Zoological Park rates "
            "AA with Lone Star and provides substantial security of its own, and the entrance "
            "carries sophisticated weapons detectors at MAD Rating 6 -- which is why the runners' "
            "own fixer tells them not to bring anything heavy. Park personnel rather than Lone Star "
            "handle the animal breakout, arriving with narcojet rifles and pistols loaded at "
            "increased chemical strength for large animals such as rhinoceroses (10D Stun against a "
            "metahuman). The adventure never actually brings Lone Star onto the ground, which is "
            "worth noticing: a mass cage failure, a running firefight and an attempted child "
            "abduction in an AA-rated public park would ordinarily end with the entire team in "
            "custody, and a GM who wants consequences has them ready-made."
        ),
    },
    "Shiawase Corporation": {
        "notes_append": (
            "SRM 01-05 A Walk In The Park (backstory and Seattle, 2064): two mentions worth "
            "keeping. Fifteen years ago, rumour had it that both Ares and Shiawase were close to "
            "discovering the key to the same wonder drug Aztechnology was racing to bring to "
            "market, which is why Dr. Santiago's project manager was pressuring his team for "
            "results and why a two-week slip was worth a child's life. And in the present, Griffin "
            "Biotechnology is described as an independent outfit doing cutting research and "
            "development 'for some of the larger corps and the big megacorps like Shiawase and "
            "Yamatetsu' -- which places Shiawase among the clients of the company at the centre of "
            "Season One."
        ),
    },
    "Yamatetsu Corporation": {
        "notes_append": (
            "SRM 01-05 A Walk In The Park (Seattle, 2064): Griffin Biotechnology, the independent "
            "biomedical R and D firm at the centre of Season One, does cutting research and "
            "development 'for some of the larger corps and the big megacorps like Shiawase and "
            "Yamatetsu'. Coming after SRM 01-02, where a Yamatetsu covert ops team went into "
            "DocWagon's vault after a glowing tissue sample, and SRM 01-04, where Griffin's neural "
            "research was stolen out from under DocWagon and Ares, that makes Yamatetsu a paying "
            "customer of the company whose secrets everyone else in the season is stealing."
        ),
    },
    "Ares Macrotechnology": {
        "notes_append": (
            "SRM 01-05 A Walk In The Park (backstory, ~2049): rumour had it that both Ares and "
            "Shiawase were close to discovering the key to the protein chain behind Aztechnology's "
            "wonder drug, which is why Dr. Santiago's project manager was pressuring his team to be "
            "first to market -- and therefore why a two-week delay caused by one missed reagent was "
            "settled with a human sacrifice. A useful measure of what the pharmaceutical race "
            "between the megacorporations is actually worth to the people running it."
        ),
    },
}

LOC_UPDATES = {
    "Fort Lewis": {
        "notes_append": (
            "SRM 01-05 A Walk In The Park (Seattle, 2064): Fort Lewis has a zoological park, and it "
            "is a genuine civilian attraction -- popular enough with off-duty personnel that there "
            "are always military visitors on leave in the crowd, showcasing paranormal animals "
            "alongside ordinary ones, and rated AA with Lone Star with MAD Rating 6 weapons "
            "detectors at the entrance. It is the destination a Bellevue private school picks for a "
            "reward field trip, which says something about how Fort Lewis reads to civilian Seattle: "
            "a safe day out. It is also where a professional shadowrunner team chose to dissolve a "
            "dozen animal cages with super acid in order to cover an abduction, on the reasoning "
            "that heavy security at the gate does nothing about a threat that is already inside."
        ),
    },
}

NPC_UPDATES = {
    "Manny": {
        "description_append": (
            "SRM 01-05 A Walk In The Park: the voice on the comm early on a Saturday morning, "
            "apologetic and completely unbothered about it. 'Sorry to get you so early, but I've "
            "got a line on a job that needs some professional attention. Based on your past "
            "performance, I've decided you're the one for the job. I've dug up a couple of others "
            "based on their reps as well. As I mentioned, it's a sensitive mission -- bodyguarding "
            "a group of VIPs that want to get out into the public and enjoy some fresh air.' He "
            "closes with the one piece of advice that actually matters: 'I wouldn't recommend "
            "anything heavy -- remember that you'll be working out in the public!'"
        ),
        "notes_append": (
            "SRM 01-05 A Walk In The Park: Manny brokers the Hillside Student Community job, "
            "sending the team to 5027 159th Place SE in Bellevue for eight o'clock sharp to meet "
            "their Johnson, Ms. White. Runners who already have him as a contact get the call by "
            "name and on the strength of their past performance; anyone else gets the same call "
            "with 'a mutual acquaintance recommended you'. Note the shape of the business he is "
            "doing here -- a private school principal with no discretionary budget, hiring "
            "shadowrunners as bodyguards for children on the advice of trusted associates, at 2,000 "
            "nuyen a head. Manny is the fixer who takes that call and finds people who will do it "
            "properly, and his warning about not bringing anything heavy is the only briefing the "
            "team gets before walking into a zoo with MAD Rating 6 detectors on the gate."
        ),
        "contact_skills_add": ["Bodyguard and protection work"],
    },
    "Pete/Petra Sprent": {
        "description_append": (
            "SRM 01-05 A Walk In The Park: at the zoo, a man (or woman) in typical street clothes "
            "watching the children and the shadowrunners -- Perception (6) to notice, after which "
            "the reporter simply keeps following the group and watching what they do, waiting for "
            "something newsworthy to happen. The book's own comment is the relevant warning to the "
            "table: 'Hopefully no one with an itchy trigger finger will attack the reporter before "
            "knowing his intent.'"
        ),
        "notes_append": (
            "SRM 01-05 A Walk In The Park: Sprent has stumbled on the story by accident -- a party "
            "of magically gifted children from an exclusive private school being escorted round the "
            "Fort Lewis zoo by obvious shadowrunners -- and is following it in the hope that it "
            "becomes news. It does. Use the male Peter version if the table has both a Pete and a "
            "Petra contact; use whichever version a player already has otherwise. Two consequences "
            "the adventure leaves open: a reporter with footage of eight named, ransomable children "
            "and their bodyguards is a security disaster for the Hillside Student Community "
            "regardless of what happens next, and if the cages open while Sprent is still filming, "
            "he has the abduction attempt on record."
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
No Matrix systems are mapped or rated in this adventure -- there is no decking scene, no host and no
security sheaf anywhere in it. What there is instead is a surveillance chain, which is worth setting
out because tracing it is the adventure's critical clue:

| Element | Detail |
|---|---|
| **Six wireless mini-camcorders** | Hidden through the Sanchez townhouse. Perception (8) to find them |
| **The roof "telecom satellite dish"** | Not a telecom dish at all but a signal repeater, taking the camera broadcast and relaying it to Santiago. Aimed the wrong way -- away from Texas, where the North American geosynchronous cable satellites orbit. Perception (4) to notice the misaim, or a plain Perception test if the runners already know to look for a repeater, with Electronics (4) as a complementary test |
| **The give-away** | The house telecoms work perfectly, and Amanda Sanchez subscribes to no satellite service whatsoever -- she takes telecom over a standard Matrix connection whose bill is sitting on the counter |
| **The trace** | Intelligence or Electronics (5) follows the transmission to its target: Santiago's warehouse hideout in Everett |
| **The installers** | A "National Satellite" telecom company van, two weeks ago, three hours on the roof -- the last visitors the neighbour Ed Griswald saw |
| **The zoo feed** | Santiago also hired an ordinary-looking pedestrian to stand in the park with a mini-camcorder trained on the action, transmitting to the same warehouse, so that he would know the moment GRAB took Mark and could page them the delivery address |

**Not built**: the warehouse's receiving end (a portable generator system and whatever Santiago
watches it on), and the special pagers GRAB carry, which are the deliberate air gap in the plan --
the address only ever goes out after the snatch succeeds, so a GRAB member captured at the zoo has
nothing to give up.
"""

NOT_BUILT = """
- **The Aztechnology shaman** hired to perform the blood magic rituals and channel Mark's power --
  never named, never statted, and standing in the altar room at the climax. The runners' choice of
  what to do with him is one of the three questions the book closes on; recorded on the Santiago and
  Aztechnology rows.
- **The hired thugs** guarding the warehouse (roughly two per player character) -- stat block p.20:
  B5 Q4 S5 C3 I4 W4, Ess 5.0, Reaction 4, Init 4+1d6, Combat Pool 6, Karma Pool TR-1, Professional
  Rating 2/Trained; no cyberware; Armed Combat (Baton) 2 (3), Pistol (Taser) 2 (4), Unarmed 3,
  Athletics 2, Stealth 5, Etiquette 5, Negotiation 3, Electronics 2, Computers 1, Biotech 2;
  Security Procedures 4; secure clothing (3/0); AZ-150 stun baton (8S Stun); transceiver Rating 1.
  Tough but limited, new to the streets, no tactics, attack until killed, full of bluff and random
  insults meant to inflame and taunt. (The block is the Westin-Seattle hotel security block from
  SRM 01-01 with the taser swapped for a baton.)
- **The street muscle** Santiago hired months ago to set the warehouse up, findable in an unnamed
  seedy bar and willing to sell the address to persuasion, interrogation or bribery -- on the
  warehouse row.
- **The pedestrian with the mini-camcorder** at the zoo, and the **"National Satellite" cable
  crew** who spent three hours on Amanda's roof -- unnamed instruments, on the MATRIX_HOSTS
  surveillance chain.
- **The Humanis Policlub demonstrators** (all normal humans, 3 in every attribute and ability, no
  weapons) and the **zoo personnel** with narcojet rifles -- on the Humanis Policlub and Fort Lewis
  Zoological Park rows.
- **The released animals** -- the GM picks them; the book suggests lions, black rhinoceros, a herd
  of zebras, badgers or emus, and for experienced tables cockatrices, wyrd mantis or a piasma or
  two.
- **The Aztechnology project manager** and the **vice president of biotechnology** who demoted
  Santiago and named the price, and the **security firm** paying Winona's scholarship so it can use
  her to test detection equipment -- unnamed, and all three are excellent hooks.
- **The blood spirit** the ritual is intended to summon -- never summoned, described only in
  Santiago's confession.
"""

PLAY_NOTES = """
- The shape of this one is a comedy that turns into a horror story. The zoo section is explicitly
  written for roleplaying and comedy and the book warns it will take the lion's share of the slot;
  the finale is a blood sacrifice in a warehouse. Let the first half be as silly as the table wants
  -- the switch lands harder for it.
- If time runs short, end the adventure with the prevented abduction at the zoo. The Parent Trap
  needs at least ninety minutes remaining, and the book says so.
- Do not use a hex map at the zoo. Draw one or print a real zoo's visitor brochure; the encounters
  work better when the party is spread over a park nobody has mapped precisely.
- Pick two or three zoo encounters, not all five: Sammy's telekinesis, the Humanis demonstration,
  Sprent the reporter, Winona shoplifting, Freddy's uncontrollable bad luck. The Humanis scene is
  the one worth spending time on, because it is a fight the runners must not win.
- The abduction is not the mission. "The abduction of Mark is not critical to the adventure" --
  stopping it is worth 2 Karma, rescuing him afterwards is worth 1, and either way the investigation
  runs the same. Do not fudge the snatch in either direction.
- GRAB are professionals with gel rounds and flash-bangs and a plan for every branch: distraction
  first, quiet subdual of anyone standing near Mark second, open assault as a second distraction
  only if the first fails. They are also compartmentalised on purpose, so interrogating a captured
  member yields nothing but the fact that they were told to grab the boy and wait for a page.
- Menagerie is the trap in the rescue. A runner who stuns a rampaging rhinoceros to save a bystander
  has, by her lights, attacked an animal, and she will attack them for it in animal form. The Karma
  award for stopping the stampede without harming the animals is the signpost; put it in front of
  the players early by having someone else try force first.
- The investigation has three doors and the book only really wants one of them used. The school's
  file is free, the street muscle in the seedy bar is functional and the text admits it "will
  probably not be as fun", and Amanda Sanchez's townhouse is the good one. Steer there, and if the
  runners will not go, have Ms. White phone and ask them to break the news to Mark's mother before
  the trid does.
- At the townhouse, be generous with the clue chain: photograph, Atzlan University doctorate,
  Aztechnology credstick in the name Amanda Santiago (Computer (8)), six cameras (Perception (8)),
  and a roof dish aimed at nothing (Perception (4), Electronics (4) complementary) that traces
  (Intelligence or Electronics (5)) straight to Everett. If they fail the maglock, jam it rather
  than alarm it and bring Amanda home early -- she tells them everything herself.
- The finale should be won. Two thugs per character, ultrasound motion sensors at Rating 4, an altar
  room behind Barrier 6 one-way plexiglas, and a scientist with Professional Rating 1 who does not
  fight. The instruction is that the players win with no more than a quarter of the team down. If
  Mark was never abducted, Santiago is caught out in the open planning his next attempt, which is
  the reward for the earlier success.
- Mark can die here, and the book says that is not necessarily a bad thing. Do not protect him
  harder than the players do.
- Karma: 2 for stopping the abduction at the zoo OR 1 for stopping the sacrifice; 1 for ending the
  animal stampede without damaging the animals; up to 3 individual; maximum 6. The debriefing log
  records kidnapped/not, rescued/killed, and animals restrained without excessive force yes/no.
- The three questions the book hands the table and does not answer: do they let Santiago go, free
  to try again; do they help relocate Amanda and Mark; do they kill the Azzie shaman or let him go.
  Santiago knows where Amanda lives, has money left, and 'will wait to fight another day'. Whatever
  the players choose should come back.
"""
