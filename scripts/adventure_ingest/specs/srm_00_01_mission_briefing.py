# SRM 00-01 Mission Briefing (FanPro/WizKids, 2004, SR3) -- campaign order #39. Downtown Seattle
# (Freeway Park, the Seattle Trade and Convention Center, THE Sports Bar), with the dead fixer's
# levelled headquarters back in Redmond.
# SETTING NOTE: this is a SEATTLE adventure, not a Denver one. Shadowrun Missions Season 0 runs in
# the Seattle metroplex ("Freeway Park in Downtown Seattle", "one of Seattle's fixers", New Seattle
# cited as the area reference); the campaign only relocates to Denver in later seasons. Every
# location row is therefore city "Seattle".
# Dating: the book gives no in-world date. It is written for SR3, cites SOTA:2064, describes the
# Renraku Arcology shutdown and the "slow, vicious fight for recovery" as recent history, and was
# published in 2004, so 2064 is the campaign year. The run itself takes place over a single Monday
# lunchtime: the hire call comes mid-morning, muster is 1130, the meet runs 1200-1300, the bomb is
# timed for 1255.
# Book editing inconsistencies noted on the affected rows: the dead fixer is "the fixer who had once
# reigned over this section of the sprawl" and is called "he or she" in the intro but "her little
# black book" in the Legwork table; Rolando's adventure text gives him three remaining elementals
# (Water 1, Earth 2) after two materialize but only lists five in total by implication; the
# adventure text calls the reporter's surname only in the handout ("Sprent") and swaps gender by
# table; Rolando's real name ("Ray Marcello") appears only on the contact card, never in the
# adventure text. Snoop's Intelligence is printed as "2/4".
# Name collision: the ganger "Crawler" is disambiguated as "Crawler (Halloweeners)" because an
# unrelated Crawler (Tartarus Ring lieutenant, Mob War!) already exists in the world.
# Source text: docs/Adventures/text/SRM00-01A_missionbriefing.txt (29 pages) and
# docs/Adventures/text/SRM00-01B_missionbriefing.txt (player aids, 21 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "SRM 00-01 Mission Briefing"
ORDER = 39
SOURCE = "SRM00-01A_missionbriefing.pdf, pp. 3-29; SRM00-01B_missionbriefing.pdf (Player Aids), pp. 3-21"
YEAR = "2064"

SYNOPSIS = """
Weeks ago somebody dropped a three-storey building in **Redmond** on top of one of the best fixers
in the Seattle metroplex. Shadowrunners digging the rubble pulled out a cyberdeck, an armored
storage unit and a fireproof box holding a will dated only weeks before. Two days of cracking the
encryption later they had the whole empire in their hands: contacts, runners for hire, markers,
access codes, blueprints, recon photos, and enough compromising material to blackmail half of
Seattle's political and corporate establishment. Releasing it would start another shadow war, so
they followed the will's own instructions -- divide and conquer. Invitations went out to a dozen of
the more honorable fixers in the sprawl.

The meet is at high noon on a Monday in the **Maynard Pavilion**, an enclosed hire-able pavilion
inside **Freeway Park**, the deck of greenery built over the I-5 canyon next to the **Seattle Trade
and Convention Center** in Downtown. One hour of uninterrupted bargaining is all it takes. Because
even honorable fixers do not trust each other, each attending fixer nominated one guard who is new
to the Seattle scene and has no stake in the outcome -- that is the runners. **Trotter**, a bland
ex-runner who worked for the dead fixer, hands them 1,000 nuyen each in the Combat Biker room of
**THE Sports Bar** at 1130, promises 1,500 more at 1300, and tells them nothing: external security
only, nobody enters after the doors close, no attention drawn. Downtown is AAA and the convention
next door is the **Confederation of Security Providers** trade show -- the largest single gathering
of cops, feds and corporate security on the continent, all of them eating lunch in the park.

What nobody says out loud is that one of the fixers who refused the invitation sees the meet as a
chance to thin the herd. He bribed one of the organizing runners for the details and loaded five
kilos of liquid Compound XII into the fluid reservoir of a Chrysler-Nissan Caretaker gardening
drone -- the one the park's resident Mouse shaman **Scarper** calls "Hugh". At 1254 Hugh rolls to
the pavilion wall; at 1255 it goes off for 26D with a mere -1 per meter of falloff. Hugh has not
watered anything all morning, has no maintenance record in the park host, and smells faintly of
chemicals. Scarper will tell anyone polite enough to listen that he is worried about Hugh.

Around that hour: the fixer **Rolando** (Ray Marcello), a boorish initiate hermetic in gold chains,
arrives late with two ork bodyguards and intends to walk in anyway; a pair of Kamikaze-crazed
**Halloweeners** ride in off Seneca with stolen flamethrowers; a free field spirit in the shape of
a skateboarding girl plays Accident on whoever amuses her; a cyber-beagle from the trade show
records everything; a Wuxing drone demo comes down the I-5 canyon with the guns pointed at the
team; the reporter **Pete/Petra Sprent** offers 5,000 nuyen for an interview and knows about the
bomb; and a green FBI agent, **Barnaby Mason**, is watching from the vending machines. Play it
quiet and every fixer in the pavilion offers to be a contact.
"""

TIMELINE = """
- **Weeks before** -- the fixer's Redmond headquarters is levelled in a shadow war; runners recover
  the deck, the storage unit and the will (dated weeks earlier).
- **Two days later** -- the encryption falls; the will's list of honorable fixers is used to send
  out invitations.
- **A week after that** -- the fixers agree to terms: Freeway Park, one hour, one nominated outside
  guard each. A refused invitee bribes an organizing runner for the details.
- **Two days before the meet** -- the gardening drone "Hugh" goes in for "service" and comes back
  wrong; the bomb is fitted to its fluid reservoir.
- **Meet day, mid-morning (Monday)** -- each runner gets the call, two hours' notice, 2,500 nuyen.
- **1130** -- muster under the Everett Jets poster in the Combat Biker room of THE Sports Bar;
  Trotter pays 1,000 nuyen each and briefs them.
- **1145-1200** -- the runners get about fifteen minutes to walk the park; the fixers arrive in
  separate groups, one obvious bodyguard apiece.
- **1200** -- the pavilion doors close. Rating 6 ward, two force 3 watchers, a force 6 air elemental
  inside; the summoning magician sits in a cafe 300 meters away.
- **1200-1300** -- Rolando's arrival, the Halloweener firebomb run, the field spirit, Snoop, the
  Wuxing fly-by, the reporter, the fed, Deborah Figgis's allergy attack -- in whatever order the GM
  needs them.
- **1254** -- Hugh drives directly at a pavilion wall.
- **1255** -- detonation, 26D, -1 per meter, unless the drone has been shut down.
- **1300** -- contract over. Balance paid, 500 nuyen bonus if the hour was clean; each runner may
  take one fixer contact plus one other contact.
"""

ORGS = [
    {
        "name": "Confederation of Security Providers",
        "org_type": "trade association",
        "tier": 4,
        "headquarters": "Rotating; convening at the Seattle Trade and Convention Center, Downtown Seattle",
        "summary": "Continental trade body of police, federal and corporate security providers, holding its annual show next door to the meet.",
        "description": (
            "The Confederation of Security Providers is the industry body that runs the security "
            "trade show booked into the Seattle Trade and Convention Center for the week of the "
            "fixers' meet. Banners over the entrance advertise it to the whole of Downtown. Every "
            "vendor of note takes a booth -- Lone Star, Knight Errant, the FBI, the drone shops, "
            "the surveillance houses -- which makes it, in the words of one street source, "
            "'pretty much everybody who's anybody in the field... probably the biggest single "
            "gathering of cops, feds, and private security in the continent.' Its members spill "
            "out into Freeway Park at lunchtime in neatly tailored and very obviously armored "
            "suits, and its exhibitors treat the park as an extension of the show floor: a "
            "cybernetically wired beagle is turned loose in it as a live surveillance demo, and "
            "Wuxing runs an armed VTOL drone flight down the I-5 canyon into the hall as an "
            "attack demonstration."
        ),
        "notes": (
            "Plot role: the reason Downtown is thick with professional security on the day of the "
            "meet, and the reason two of the optional encounters (Cyber Snoop, Fly By) exist. Any "
            "runner who starts trouble in the park is doing it in front of several hundred trained "
            "security professionals eating lunch; if the team chases the field spirit and looks "
            "like it is menacing a child, some of the bystanders who intervene are conference "
            "delegates. Legwork (Corporate / Law enforcement or security contact, or Arms Dealer, "
            "TN 4-6): 3 successes gets the roster of attendees, 4+ gets 'they're going to be "
            "trying out some new covert surveillance kit around the local area as part of the "
            "show.' The park's Matrix host is run out of the Convention Center."
        ),
        "allies": ["Lone Star Security", "Knight Errant Security Services", "UCAS Federal Bureau of Investigation", "Wuxing, Inc."],
    },
    {
        "name": "Puget Sound Sports Fishing Club",
        "org_type": "social club",
        "tier": 1,
        "headquarters": "Puget Sound waterfront, Seattle",
        "summary": "Respectable anglers' club whose small lapel pin is the one non-magical thing Rolando wears.",
        "description": (
            "A perfectly ordinary recreational fishing club working the Sound out of the Seattle "
            "marinas -- charter days, tournaments, a members' bar and a small enameled lapel pin. "
            "Of all the fetishes, foci, ornate medallions and gaudy paraphernalia hanging off the "
            "fixer Rolando, the club pin is the only piece with no magical function whatsoever. He "
            "wears it because he genuinely loves the water: he carries Motorboat 3, Sport Fishing "
            "3 and Ocean Fish 4 alongside his Sorcery and his Mafia Background."
        ),
        "notes": (
            "Plot role: a lever. A runner who spots the pin (or who has any waterfront, boating or "
            "fishing knowledge) has the single non-confrontational hook into Rolando that exists in "
            "the adventure -- getting his attention is the hard part of the Negotiation (Fast "
            "Talking) (4) or Etiquette (Street) (4) test that opens the persuasion route, and a "
            "conversation about the Sound will do it where a threat will not. Joeli Gibson, who "
            "lives on her yacht in Puget Sound, is the other NPC likely to know the membership."
        ),
    },
]

LOCATIONS = [
    {
        "name": "Freeway Park",
        "location_type": "park",
        "city": "Seattle",
        "district": "Downtown",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "Lone Star Security",
        "summary": "Green deck built over the I-5 canyon beside the Convention Center; the run's whole battlefield.",
        "description": (
            "One of the few green spots in the heart of Downtown, spread over several city blocks "
            "on a deck built above the I-5 -- the busiest road in the metroplex -- so that the "
            "traffic noise arrives strangely muted and the park sits as an oasis of relative calm. "
            "Towering buildings surround it on every side and provide countless vantage points; "
            "the monstrous bulk of the Renraku Arcology looms over everything. Large plascrete "
            "planters three quarters of a meter high (barrier 16) are filled with earth, flower "
            "beds and shrubs up to a further one and a half meters (barrier 2) and small four- to "
            "five-meter trees (foliage 2, trunks 6), so sightlines are short and cover is "
            "everywhere. Interactive audio-visual units (barrier 4, half a meter above the planter "
            "rim) spring to life when anyone comes within a meter, reciting facts about the plants, "
            "Downtown landmarks and events at the Convention Center. Benches, rubbish bins and "
            "vending machines fill the gaps. Microphones and speakers are rigged throughout, LAVs "
            "and executive choppers and drones cross overhead, and advertising blimps run trid "
            "constantly. At lunchtime it fills with wage slaves, tourists, meta-variants, SURGE "
            "cases, hip teens in skintight lurid colors and armored suits from the security trade "
            "show next door. The Seattle Trade and Convention Center is adjacent; Seneca Street "
            "runs in on one side and University Street on another."
        ),
        "notes": (
            "Map: SRM00-01P p.4 ('Freeway Park & Surrounds') and p.5 ('Maynard Pavilion & "
            "Surrounds'). Physical security: three two-officer patrols of probationary Lone Star "
            "guards (B4 Q3 S4 C3 I3 W3, Init 3+1D6, Karma/Pro 1/2, Unarmed 3, Clubs 2 [Stun Baton "
            "4], Pistols 2 [Ruger Thunderbolt 4], armor jacket, AZ-150 stun baton, Ruger "
            "Thunderbolt with gel and regular, commlink) -- aware of trouble one turn after it "
            "starts, on the scene in 1D6 turns, real Lone Star support in a further 2D6. Magical: "
            "a Lone Star mage on astral patrol crosses the park roughly every 15 minutes, spotting "
            "suspicious magic on a 1 on 1D6; combat, manipulation and dangerous illusions bring a "
            "mage with elementals in 1D6 turns. Electronic: cameras and sensors everywhere feeding "
            "the park host, not constantly monitored (pattern-recognition alerts only) -- a few "
            "dead cameras raise nothing, and the team can black out the pavilion's coverage for the "
            "hour. Access to the host is Electronics B/R (4), base time 30 seconds, to open an "
            "interactive unit, then Electronics (4) to fit a dataline tap; the same tests shut "
            "individual devices down. Uncovered suspicious action is recorded on a 1-2 on 1D6. "
            "Resident: Scarper the Mouse shaman, and a free field spirit that materializes as a "
            "skateboarding girl of about 1.5 meters in sneakers, brown pants, green halter top and "
            "yellow cap and amuses itself with Accident; an astral barrier or another spirit's "
            "Guard power blocks it, and it flees anyone who chases it. Gardening drones work the "
            "park; one of them, 'Hugh', is the bomb."
        ),
    },
    {
        "name": "Maynard Pavilion",
        "location_type": "pavilion",
        "city": "Seattle",
        "district": "Downtown (Freeway Park)",
        "security_level": "Patrolled / Commercial",
        "summary": "Hireable pavilion in an enclosed corner of Freeway Park; the fixers' meet happens inside it.",
        "description": (
            "A small single-storey building with a gabled roof, ten meters by five and about five "
            "meters high, standing in an isolated enclosed grotto of Freeway Park reached by a "
            "single entry walkway (there is an interactive unit at the mouth of it). The walls look "
            "like wood but are synthetic and much stronger than they look; each wall has a central "
            "double door and the long walls carry two flanking single doors besides, all of them "
            "French doors of one-way armored glass so that those inside can watch the park while "
            "the park cannot watch them. Walls and doors are barrier rating 8. Normally the "
            "pavilion is a shady spot open to the public, but it can be hired for private "
            "functions, which is what has been done today. The grotto is walled off by hedges and "
            "planters that will not stop a determined body and will certainly not stop bullets."
        ),
        "notes": (
            "Magical security laid on for the meet: a rating 6 ward, two force 3 watchers acting as "
            "guard dogs inside, and a single force 6 air elemental. The summoning magician is "
            "sitting in a cafe about 300 meters away and responds astrally as needed -- use the "
            "Lone Star magician stats, New Seattle p.114. Internal security is somebody else's "
            "problem; the runners have the outside only, from 1200 to 1300, with nobody admitted "
            "after the doors shut unless someone inside says so. The building has several flammable "
            "components: a Halloweener flamethrower sweep will set it alight (blankets, buckets or "
            "magic put it out, but the meeting breaks up early if it is not dealt with at once). "
            "Hugh the gardening drone drives at one of these walls at 1254. If Rolando gets in, the "
            "runners hear a subdued conversation, silence, then a loud one-sided argument before he "
            "storms out; enhanced hearing catches that his presence was neither requested nor "
            "allowed and that the assembled fixers will lean on him if he persists."
        ),
    },
    {
        "name": "Seattle Trade and Convention Center",
        "location_type": "convention center",
        "city": "Seattle",
        "district": "Downtown",
        "security_level": "Corporate Standard",
        "controlling_org": "Confederation of Security Providers",
        "summary": "Convention hall adjoining Freeway Park, hosting the Confederation of Security Providers show.",
        "description": (
            "The metroplex's trade and convention hall, sitting immediately alongside Freeway Park "
            "in the middle of Downtown, usually booked out for one big gathering or another. Inside "
            "it is a rabbit warren -- street wisdom holds that if you have heat on you, you duck in "
            "there and lose yourself in the crowd. This week the banners advertise the Confederation "
            "of Security Providers trade show, which turns the surrounding blocks into the densest "
            "concentration of police, federal agents and corporate security on the continent. "
            "Exhibitors use the park outside to stage live demonstrations, and the complex's rigged "
            "control system also runs the park's cameras and sensors."
        ),
        "notes": (
            "The park's Matrix host is run from here (see Matrix systems). Vendors are actively "
            "trying to outdo each other, which a smart runner can play off -- and which is why "
            "Snoop the cyber-beagle is loose in the park and why three armed Wuxing Azure Cloud "
            "VTOLs come down the I-5 canyon and into the hall on a mock attack run against dummy "
            "targets (flight plan registered with Lone Star; a minor bureaucrat routed it over the "
            "park to give the patrons a thrill). Legwork (Corporate or Law enforcement contact TN "
            "4, any Downtown contact TN 6): 4+ successes gets 'they'll be showing off some wiz "
            "stuff at the show. Probably using the park to stage some of the displays.'"
        ),
    },
    {
        "name": "THE Sports Bar",
        "location_type": "bar",
        "city": "Seattle",
        "district": "Downtown (University Street and Terry Avenue)",
        "security_level": "Patrolled / Commercial",
        "summary": "Family-style sports bar on University and Terry where Trotter briefs and pays the team; rumored Mafia money.",
        "description": (
            "Commonly considered the best sports bar of its type in Seattle, THE Sports Bar stands "
            "on the corner of University Street and Terry Avenue, a short walk from Freeway Park. "
            "It is a family-style restaurant and bar split into two rooms, each dedicated to a "
            "different sport depending on the season; the runners are told to meet under the "
            "Everett Jets poster in the Combat Biker room at 1130. It is common knowledge in the "
            "shadow community that rumors persistently link THE Sports Bar to the Mafia, which is "
            "reason enough for anyone drinking there to keep a cool head and a civil tongue."
        ),
        "notes": (
            "The Hire scene. For most of the team this is the first time they have met each other, "
            "which can be a tense and highly charged affair; give them a few minutes before Trotter "
            "joins them. He pays 1,000 nuyen each on the spot against 2,500 total. Haggling: "
            "Negotiation Test per SR3 p.93 against Negotiation 7 / Intelligence 6, each net success "
            "shifting the fee 250 nuyen either way; remind them that a normal bodyguarding job pays "
            "about 200 nuyen a head. A very nasty attitude drops the base to 2,000 nuyen. Starting "
            "a brawl in a Mafia bar is its own reward."
        ),
    },
    {
        "name": "Scarper's Bower",
        "location_type": "squatter camp",
        "city": "Seattle",
        "district": "Downtown (Freeway Park)",
        "security_level": "Patrolled / Commercial",
        "summary": "The overgrown corner of Freeway Park the Mouse shaman Scarper has made into a home the authorities tolerate.",
        "description": (
            "Tucked into a corner near the Maynard Pavilion, a bower -- a small 'room' formed by "
            "the overhanging branches of the park's trees -- that the elderly Mouse shaman Scarper "
            "has made his own. It is a cluttered space, but it is a cluttered space with its own "
            "special order: Scarper is a chronic neatness freak and very house proud, and between "
            "his spells and his affinity with the local spirits he lives a good deal more "
            "comfortably in it than a homeless drunk has any right to. The authorities leave him "
            "alone because in his own way he keeps the park clean and safe; in effect he is its "
            "unpaid attendant."
        ),
        "notes": (
            "Contact card: 'Places to Meet: Freeway Park only. Contact: In Person Only.' Scarper "
            "lives here by choice because it is where he feels closest to Mouse. Runners who move "
            "park furniture around will find him following behind putting it back, often without "
            "their noticing until later; runners who wreck the park earn the field spirit's "
            "attention and his open disapproval. The bower is the natural place for any private "
            "conversation with him, and for the first-aid and healing he provides if the bomb goes "
            "off."
        ),
    },
]

NPCS = [
    {
        "name": "Trotter",
        "role": "Bland ex-runner Face who worked for the dead fixer; arranges the meet, hires and pays the team",
        "archetype": "Face",
        "title": "Middleman and chair for the estate meet",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "A bland-looking human man who gives no name but 'Trotter' and volunteers nothing he "
            "does not have to. He walks into the Combat Biker room of THE Sports Bar, finds a table "
            "of strangers who have never met each other, counts out 1,000 nuyen apiece, and answers "
            "questions in flat, complete, uninformative sentences. He will freely admit that he "
            "knows little beyond what he needs to know to get the runners primed for the job, and "
            "he means it as reassurance rather than apology."
        ),
        "background": (
            "A former shadowrunner who went to work for the fixer who was killed in Redmond, in the "
            "role the book calls 'a Face'. When the will was cracked he became the middleman: he "
            "set the base requirement that anyone who wants to bid for the dead fixer's assets must "
            "attend the meet in person, at a set time and place, and he chairs the bargaining "
            "inside the Maynard Pavilion. He negotiated the guard arrangement -- each attending "
            "fixer nominates one runner who is new to the Seattle scene and has no stake in the "
            "outcome -- which is the only reason the player characters are in the park at all."
        ),
        "notes": (
            "No stat block is given; run him as a competent Face. Answers he will give: external "
            "security only, from 1200 to 1300 exactly; nobody enters the pavilion after the doors "
            "close unless someone inside says otherwise; internal security is handled by another "
            "group; disturbances are to be dealt with quickly and quietly, surveillance attempts "
            "stopped, the integrity of the meeting maintained; the parties chose neutral guards "
            "through friends of friends; force is the runners' call but Downtown is AAA-rated; the "
            "likeliest physical threat is gangers; resources are whatever they brought. Pays the "
            "balance at 1300 unless the team was grossly negligent, plus 500 nuyen each if the hour "
            "was genuinely clean. He is the obvious suspect for the bribe that leaked the meet to "
            "the bomber, and the book never says he was not."
        ),
        "contact_skills": ["Shadow work for the late fixer's estate", "Introductions to the Seattle fixer community"],
    },
    {
        "name": "Rolando",
        "role": "Gaudy initiate hermetic fixer, uninvited and late, who intends to walk into the meet regardless",
        "archetype": "Fixer",
        "title": "\"Rolando\" -- independent fixer and talismonger's friend; real name Ray Marcello",
        "race": "Human",
        "gender": "Male",
        "connection": 4,
        "description": (
            "Mediterranean-looking, extensively remodelled by cosmetic surgery, with a few implants "
            "on open display and so much jewelry that he throws flashes and scintillations of light "
            "as he strides. A gold medallion on a gold chain swings at his neck. He has all the "
            "accent, all the clothes and none of the class -- most people assume he has watched too "
            "many repeats of Godfather IX. Boorish, tactless, self-interested and utterly certain of "
            "his right to be wherever he is standing: he will argue every point the runners make "
            "while insulting everyone at every opportunity. Among the fetishes and paraphernalia, "
            "one small pin is not magical at all -- it marks him as a member of the Puget Sound "
            "Sports Fishing Club."
        ),
        "background": (
            "The contact cards give his real name as Ray Marcello, which never appears in the "
            "adventure text. An initiate of grade 3 who always Masks himself as an ordinary "
            "magician and Masks two of his foci besides, he trades in magical gear and knows "
            "Seattle's best talismongers, carries Mafia Background 3 alongside Corporate Background "
            "4, and fishes the Sound in his spare time. He was not invited to the estate meet -- "
            "his presence was neither requested nor allowed -- but he refuses to miss out on the "
            "dealing and arrives after the doors have already shut."
        ),
        "notes": (
            "Stats: B3 Q4 S3 C5 I5 W6, Ess 5.6, Bio 0.5, Magic 8(9), Reaction 4, Init 4+4D6, "
            "Combat Pool 7, Spell Pool 6, Karma/Pro 6/2. Conjuring 5, Cyber-Implant Combat 4, "
            "Etiquette 5 (Corp 7), Interrogation 5, Negotiation 6, Sorcery 5, Sport Fishing 3, "
            "Stealth 4. Spells: Armor 5, Control Thoughts 4, Detect Enemies (Ext) 3, Fireball 5, "
            "Heal 6, Improved Invisibility 4, Increase Reflexes +3 2, Influence 4, Levitate 2, "
            "Manaball 4, Mindprobe 4, Stun Bolt 4. Metamagic (grade 3): Anchoring, Masking, "
            "Shielding -- always 4 dice on Shielding for himself plus Betsy and Becky. Cyber: "
            "datajack, alpha retractable hand blade (rating 2 masked weapon focus). Bio: clean "
            "metabolism, skin pigmentation, trauma damper. Ceska vz/120 silenced, armor clothing "
            "3/0, armband sustaining focus (Increase Reflexes +3), rating 3 manipulation spell "
            "focus medallion, rating 4 expendable foci. Tactics: sustains Detect Enemies, astrally "
            "perceives, and ambushes any projecting magician with the masked hand blade in astral "
            "melee. If a fight starts he holds an action to self-cast Armor and never attacks "
            "directly; he runs for the doors under cover of the fight; at Moderate physical damage "
            "a force 5 fire and a force 5 air elemental materialize, the air one carrying him out. "
            "Three more force 5 elementals (one Water, two Earth) are available for Pushing the "
            "Envelope, and he can Levitate over the melee into the pavilion. Talk him down with "
            "Negotiation (Fast Talking) (4) or Etiquette (Street) (4) to get his attention, then a "
            "(6) test after a real argument; or beat him with deployment (opposed Intelligence, "
            "modified by how well the team is set up) or Intimidation. He leaves with insults and "
            "grudging admiration -- and is available as a contact afterwards."
        ),
        "contact_skills": ["Acquiring magical gear and foci", "Seattle's best talismongers", "Mafia and street gossip"],
    },
    {
        "name": "Betsy Ross",
        "role": "Ork bodyguard sister to Becky; Rolando's muscle at the pavilion door",
        "archetype": "Bodyguard",
        "title": "Bodyguard to Rolando",
        "race": "Ork",
        "gender": "Female",
        "connection": 2,
        "description": (
            "Attractive for an ork, with coffee-colored skin, dark hair and dark eyes, dressed with "
            "her sister in tight dark green faux-leather pants and a secure jacket that show off an "
            "athletic, muscular build. She has worked for Rolando long enough to have learned to "
            "keep her mouth shut and follow orders quickly, efficiently and quietly. Off duty she "
            "and Becky head for the nearest nightclub or bar, particularly if one of their favorite "
            "boy bands is playing; on duty, if there are attractive men on the runner team -- ork "
            "men especially -- and no violence has started yet, she will find time for a wink."
        ),
        "background": (
            "One of two sisters working together as Rolando's bodyguards. Their knowledge skills "
            "give away where they came up: Gang Identification 4, Gang Territory 4, Ork Underground "
            "Night Clubs 6, and Boy Bands 6."
        ),
        "notes": (
            "Stats (identical for both sisters): B8(10) Q3 S6 C3 I4 W5, Ess 0.29, Reaction 7, Init "
            "7+3D6, Combat Pool 7, Karma/Pro 2/3. Athletics 4, Clubs 5, Pistols 4, SMG 5, Stealth "
            "4, Unarmed 5, Biotech 2 (First Aid 4). Cyber: alpha Wired Reflexes 2 with reflex "
            "trigger, titanium bone lacing (unarmed (STR+4)M), cybereyes with low-light, thermo, "
            "electronic mag 3 and flare comp, smartlink-2. Secure jacket 5/3 (6/4 with the lacing). "
            "Stun baton and a sound-suppressed HK227-S. Patches: 2 trauma, 2 tranq 10, 1 antidote "
            "8, 1 stim 6. Tactics: she and Becky step in front and slightly to either side of "
            "Rolando and march; they draw only if the runners draw; they cover his retreat if he is "
            "wounded. They are professionals, not fanatics -- a fight here is a job, not a grudge."
        ),
        "contact_skills": ["Ork Underground nightclubs", "Gang turf and gang identification"],
    },
    {
        "name": "Becky Ross",
        "role": "Ork bodyguard sister to Betsy; Rolando's muscle at the pavilion door",
        "archetype": "Bodyguard",
        "title": "Bodyguard to Rolando",
        "race": "Ork",
        "gender": "Female",
        "connection": 2,
        "description": (
            "The other Ross sister, and to a stranger indistinguishable from Betsy: coffee-colored "
            "skin, dark hair and eyes, tight dark green faux-leather pants and a secure jacket over "
            "an athlete's build. Silent on the job, cheerfully social off it. Between them the "
            "sisters have learned to say nothing at all while Rolando does the talking, and to move "
            "the instant he stops."
        ),
        "background": (
            "Sister to Betsy and hired with her; the pair have been with Rolando long enough that "
            "he trusts them to walk him into a hostile meet with no more instruction than a nod. "
            "Ork Underground nightclubs, gang turf and boy bands make up most of what she knows "
            "outside the job."
        ),
        "notes": (
            "Stats: identical to Betsy Ross -- B8(10) Q3 S6 C3 I4 W5, Ess 0.29, Reaction 7, Init "
            "7+3D6, Combat Pool 7, Karma/Pro 2/3, alpha Wired Reflexes 2, titanium bone lacing, "
            "cybereyes, smartlink-2, secure jacket 6/4 with the lacing, stun baton, suppressed "
            "HK227-S, patch kit. The pair are meant to be handled together; splitting them is the "
            "cleanest way for a clever team to take the confrontation apart without a shot. Note "
            "that both are professional rating 3 against starting characters -- a stand-up fight "
            "with them is not a foregone conclusion."
        ),
        "contact_skills": ["Ork Underground nightclubs", "Gang turf and gang identification"],
    },
    {
        "name": "Scarper",
        "role": "Elderly Mouse shaman, ex-runner and unpaid keeper of Freeway Park; the adventure's safety net and clue-giver",
        "archetype": "Shaman",
        "title": "\"Scarper\" -- Mouse shaman of Freeway Park (real name unknown)",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "A short thin fellow with tufts of balding grey hair, eyes darting nervously here and "
            "there, almost always quivering, torn between curiosity and flight, with a smile "
            "forever trying to reach his lips. His clothes are out of fashion and a little strange "
            "but clean and well kept. He seems little more than a homeless drunk -- and he is a "
            "drunk -- yet he functions perfectly well. He nervously approaches the runners to ask "
            "who they are and what they are doing, follows behind tidying up whatever they "
            "rearrange, and drops sardonic one-liners at the worst moments: after the dust settles "
            "from a fight, 'I wonder if you're going to get paid now?'"
        ),
        "background": (
            "Once a shadowrunner himself. He lives in Freeway Park by choice, because that is where "
            "he feels closest to Mouse, and between his spells and his affinity with the local "
            "spirits he lives comfortably enough in his bower. The local authorities allow him free "
            "access and do not bother him: he keeps the place safe and clean in his own way, an "
            "unpaid park attendant. As a former runner he still knows the tricks of the trade and "
            "is happy to help out any 'youngsters' he takes a shine to; his casual side comments "
            "usually carry a grain of real wisdom."
        ),
        "notes": (
            "Stats: B3 Q3 S2 C6 I5 W6, Ess 6, Magic 8, Reaction 4, Init 4+1D6, Astral 2, Astral "
            "Combat 8, Combat 4, Spell 6, Karma/Pro 5/3. Aura Reading 6, Biotech 3, Conjuring 8, "
            "Etiquette 4 (Street 6), Interrogation 4, Negotiation 4, Sorcery 8, Stealth 8. Totem "
            "Mouse (SR3 p.164): +2 detection/health, +2 hearth/field spirits, -2 combat spells. "
            "Spells include Antidote 6, Armor 5, Barrier 6, Clairvoyance (Ext) 5, Control Actions 6, "
            "Control Thoughts 6, Create Food 3, Detox 6, Heal 4, Improved Invisibility 5, Mana "
            "Static 5, Mind Probe 6, Silence 4, Stealth 5, Treat 6. Initiate grade 2: Masking, "
            "Shielding. Long coat 4/2. CLUE ROUTE: Etiquette (Street) (4) has him confide that he "
            "is worried about 'Hugh'; Interrogation (4) establishes Hugh is one of the gardening "
            "robots and has not been the same since his service a couple of days ago -- which "
            "points straight at the bomb. He also advises on the field spirit (an astral barrier, "
            "even a weak one, or another spirit's Guard power, blocks Accident; banishing only as a "
            "last resort) and comments acidly on unsubtle violence. He rarely fights, supporting "
            "others instead, and steps in to keep the peace in what he considers his home. If the "
            "bomb goes off he can be assumed to survive and provide first aid and healing."
        ),
        "contact_skills": ["Magical instruction", "Downtown Seattle street history", "Healing and first aid"],
    },
    {
        "name": "Fox",
        "role": "Archetypal Seattle fixer at the meet; treats runners as expendable tools but deals fairly",
        "archetype": "Fixer",
        "title": "\"Fox\" -- independent fixer (real name unknown)",
        "race": "Human",
        "gender": "Male",
        "connection": 4,
        "description": (
            "A standard grey business suit of the kind mid-level sararimen wear; only the confident "
            "swagger and the penchant for cigars mark him out as something other than corporate. "
            "When Fox responds to a situation he is always in control. He treats his talent like "
            "scum and makes no secret of it -- his role is to facilitate the hiring of 'expendable "
            "assets', and that is how he feels about most of them. One must take care of one's "
            "tools lest they get broken, but beyond that Fox cares only about his own reputation."
        ),
        "background": (
            "Fox's background is unknown, almost as if he were a shadowrunner himself, although the "
            "way he treats his runners argues against it. He is a very accomplished fixer with a "
            "phenomenal success rate over the years, respected by the corporate world because he "
            "always seems to find the right people for the right job, and known in the shadows as "
            "fair in his dealings and able to source almost any hard-to-obtain item."
        ),
        "notes": (
            "Contact card: I6 W5 C3 (rest unknown), Init unknown, Karma/Pro 8/3. Etiquette 6 "
            "(Street 8), Negotiation 9. Corporate Rumors 4, Fences 6, Gear Value 8, Shadowrunners "
            "6, Black Market Goods 5, Organized Crime 4. Two datajacks; pocket secretary. Uses: "
            "jobs and cred, information, gear, additional contacts. Meets anywhere he likes -- "
            "bars, clubs, coffee shops, crowded corners where surveillance is next to impossible. "
            "Phone and email; always available. Specialties: none, because Fox is the archetype -- "
            "shadow assets, equipment or solutions to problems. Preferred runners: all of them, as "
            "long as they have talent and can do the job. Awarded as a contact to whichever runner "
            "played the hour hardest and most professionally."
        ),
        "contact_skills": ["Jobs and cred", "Hard-to-obtain gear", "Black market goods and fences", "Organized crime"],
    },
    {
        "name": "Joeli Gibson",
        "role": "Dwarf fixer at the meet; smuggler networks, hardware and drones, lives on her yacht in Puget Sound",
        "archetype": "Fixer",
        "title": "\"Joey\" -- independent fixer, smuggling and hardware",
        "race": "Dwarf",
        "gender": "Female",
        "nationality": "Fijian",
        "connection": 4,
        "description": (
            "A quiet, undemonstrative dwarf woman, so undemonstrative that people who do not know "
            "her mistake it for coldness. She keeps an extensive trid and simsense collection and "
            "never misses a Seattle trid festival. She does business over the water: bars and "
            "restaurants near the waterfront, the piers, or aboard her own yacht, where she "
            "generally stays."
        ),
        "background": (
            "Born and raised in Fiji, and a successful Seattle fixer for a few years now. Her "
            "contact base runs through the smugglers and the city's nautical circles, and she knows "
            "the fences and the suppliers of serious technical hardware better than anyone else at "
            "the meet. Anyone wanting to move, buy or sell hardware talks to Joeli."
        ),
        "notes": (
            "Contact card: I4 W5 C2, Karma/Pro 12/4 (the highest professional rating of the six "
            "fixers). Etiquette 4 (Street 6)(Mercenary 8)(Smugglers 8), Negotiation 8. Smugglers 3, "
            "Fences 4, Gear Value 4, Shadowrunners 4, Mercenary Groups 5, Puget Sound 8, Smuggler "
            "Networks 6, Acquiring Vehicles/Drones and Support Gear 6. Vehicle control rig; private "
            "yacht. Uses: jobs and cred, information, gear, additional contacts, smuggling. Phone "
            "and email, always available, though she is usually out on the Sound. Preferred "
            "runners: riggers and 'geek' types -- award her to the team's rigger."
        ),
        "contact_skills": ["Smuggler networks", "Acquiring vehicles, drones and support gear", "Mercenary groups", "Puget Sound waters"],
    },
    {
        "name": "Lyle Green",
        "role": "Young ex-simstar fixer at the meet; connector, media and high-society specialist",
        "archetype": "Fixer",
        "title": "Independent fixer, entertainment and high society",
        "race": "Human",
        "gender": "Male",
        "age": 22,
        "connection": 4,
        "description": (
            "A handsome, charming young man in his early twenties and a sharp dresser, cool, witty "
            "and confident, with a relaxed manner bordering on arrogance that he carries off "
            "through sheer good humor, charm and chutzpah. He does business in private corners of "
            "the city's hottest nightspots and is always on the lookout for new talent and "
            "associates, naturally drawn to the young and the beautiful."
        ),
        "background": (
            "Lyle was a child simsense star: a meteoric rise to nova-stardom followed very quickly "
            "by burnout, breakdown and a return to anonymity. He handles the bread-and-butter of "
            "fixing -- gear and information -- competently, but what he actually excels at is "
            "making friends and linking them to other talent. He remains extremely well connected "
            "in the media and entertainment industries and always seems to have invitations to the "
            "right events and the hippest parties, which makes him the man to know for anyone "
            "looking for a way inside the world of celebrity and high society."
        ),
        "notes": (
            "Contact card: I6 W6 C7, Karma/Pro 7/3. Etiquette 6 (Corporate 8), Negotiation 6. "
            "Corporate Rumors 6, Fences 4, Entertainment Industry 8, Shadowrunners 4, Seattle "
            "Glitterati 5, Seattle Nightlife 6. No cyberware or bioware listed. Uses: jobs and "
            "cred, information, gear, additional contacts. Meets in nightclubs or at private "
            "parties; phone only; available noon to 4 AM. Preferred runners: faces and 'smooth' "
            "types -- award him to whoever talked the team out of trouble."
        ),
        "contact_skills": ["Entertainment industry", "Seattle glitterati and nightlife", "Corporate rumors", "Introductions to other talent"],
    },
    {
        "name": "Manny",
        "role": "Sociable mid-tier fixer at the meet; magical and street knowledge, expert on the city's unwritten history",
        "archetype": "Fixer",
        "title": "\"Manny\" -- independent fixer, magic and the street (real name unknown)",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "An easy smile, a sharp wit and a real gift for conversation: Manny is the sort of man "
            "people relax around and enjoy sharing a joke and a drink with. After a while some of "
            "them get uncomfortable, as a sardonic and frankly sarcastic edge starts to show "
            "through. He enjoys jokes of all kinds and his humor can be very black indeed."
        ),
        "background": (
            "Over the years Manny has used his charisma and social talents to build friendships and "
            "contacts across Seattle and a solid shadow reputation as a reliable fixer and an "
            "information miner and trader. He is not up in the lofty heights of Seattle's top "
            "fixers but he is good at what he does: he knows experienced, proven runners, has many "
            "contacts on the street and in the city's magical circles, keeps a few in the tribal "
            "and corporate worlds, and is known as an expert on Seattle's unwritten street history."
        ),
        "notes": (
            "Contact card: I4 W4 C5, Karma/Pro 6/3. Etiquette 4 (Street 6)(Tribal 5)(Magic 6), "
            "Negotiation 6, Sorcery 2, Conjuring 2 -- a trace of talent of his own. Corporate "
            "Rumors 3, Fences 4, Gear Value 4, Shadowrunners 4, Policlubs 5, Seattle History 6, "
            "Magic Background 6, Talismongers 4. No implants. Uses: jobs and cred, information, "
            "gear, additional contacts; phone and email, always available. Preferred runners: "
            "magicians and street folk -- award him to the team's shaman or mage."
        ),
        "contact_skills": ["Magical knowledge and talismongers", "Seattle street history", "Acquiring magical gear and spells", "Tribal contacts"],
    },
    {
        "name": "Michelle Rampling",
        "role": "Elf fixer at the meet hiding behind a piano teacher's life; data brokerage and the Seattle Matrix",
        "archetype": "Fixer",
        "title": "Independent fixer and data broker; piano instructor",
        "race": "Elf",
        "gender": "Female",
        "nationality": "French",
        "connection": 3,
        "description": (
            "A bland-looking, soft-spoken woman with an extreme aversion to violence, who to all "
            "outward appearances is an unassuming piano teacher and nothing more. That is precisely "
            "why she has survived: she seems nothing like a successful, if low-end, fixer. Her "
            "first love is genuinely music."
        ),
        "background": (
            "Born and raised in a quiet middle-class suburb of Marseilles, Michelle has lived in "
            "Seattle since 2046 and has found a comfortable niche in the shadows. She keeps her "
            "hand in information brokerage for her own reasons. Her contacts are mostly ordinary "
            "people from ordinary walks of life, plus some influential music personalities; she "
            "maintains a constant Matrix presence and, while no decker herself, knows a great many "
            "of them and is quite the data broker. Many of her overseas friends were clients of her "
            "old legal business."
        ),
        "notes": (
            "Contact card: I4 W5 C4, Karma/Pro 4/2 -- the lowest of the six fixers. Etiquette 6 "
            "(Corporate 8), Negotiation 6, Computer 4. Entertainment Industry 5 (Music 8), Fences 3 "
            "(Paydata 6), Passcodes 3, Shadowrunners 4, Matrix Deckers 5, Seattle Matrix 8. "
            "Datajack. Uses: jobs and cred, information, gear, additional contacts; phone, email, "
            "Matrix, or her residence; always available, but remember she has a real life as a "
            "piano instructor. Preferred runners: deckers and 'quiet' types -- the obvious contact "
            "reward for the team's decker, and the natural fence for the park host's paydata."
        ),
        "contact_skills": ["Data brokerage and paydata fencing", "Seattle Matrix and deckers", "Music industry", "Acquiring Matrix hardware and software"],
    },
    {
        "name": "Willis Daltree",
        "role": "Old ork fixer of the Ork Underground at the meet; low-key, broad, loyal contact base",
        "archetype": "Fixer",
        "title": "\"Willy\" -- independent fixer of the Seattle Ork Underground",
        "race": "Ork",
        "gender": "Male",
        "connection": 3,
        "description": (
            "White-haired and gravel-voiced, an old ork whose cataracts have left him partially "
            "blind -- he distrusts surgery and has refused both treatment and cyber replacements. "
            "Less perceptive people read him as a rather sad figure, because his line of work looks "
            "small time. Those who know him know he covers all the bases and has yet to screw up "
            "badly."
        ),
        "background": (
            "Born to British immigrant parents who came hoping to start a new life in the then "
            "United States; instead their children were born orks and their new home was embroiled "
            "in a war against its indigenous people. Somehow the family got by. For over twenty "
            "years Willis has fixed in the Ork Underground, careful to keep his activities low key "
            "and to stay out of anything overly ambitious. He does not have a high-powered contact "
            "base, does not set up big-time jobs and cannot get the really cutting-edge gear -- but "
            "his contact base, small fry as it is, is very broad and very loyal, and there is not "
            "much going down in the Underground that he does not know about. He is a popular figure "
            "there and, through an extensive family, related to a great many of its inhabitants. "
            "Many ork and troll shadowrunners got their first job through Willis and have not "
            "forgotten it."
        ),
        "notes": (
            "Contact card: I4 W5 C3 (5 versus Ork Underground members), Karma/Pro 10/3. Etiquette 6 "
            "(Street 8), Negotiation 9. Corporate Rumors 3, Fences 4, Gear Value 6, Shadowrunners "
            "4, Policlubs 5, Seattle Underground 8. No cyberware or bioware. Overseas contacts in "
            "England and Germany. Uses: jobs and cred, information, gear, additional contacts; "
            "phone and email. Preferred runners: metahumans, orks and trolls in particular, and "
            "'straight shooters' -- award him to the team's ork or troll."
        ),
        "contact_skills": ["Seattle Ork Underground", "Low-end but very loyal street contacts", "Metahuman affairs and policlubs", "Acquiring inexpensive gear"],
    },
    {
        "name": "Pete/Petra Sprent",
        "role": "Beautiful investigative reporter chasing the meet; 5,000 nuyen for an interview, and knows the bomb rumor",
        "archetype": "Reporter",
        "title": "Investigative reporter",
        "race": "Human",
        "gender": "Male or female (GM's choice)",
        "age": 25,
        "connection": 3,
        "description": (
            "Mid-twenties and extraordinarily good looking, dressed in the latest casual fashion in "
            "a way that only enhances it -- and entirely aware of the effect, which is used quite "
            "deliberately to follow leads and chase stories. Affable, friendly and seriously "
            "charming, but also very smart, suspicious and tenacious, and quick to identify the "
            "runner most likely to be swayed. Circulates through the park talking to one group "
            "after another, working steadily closer to the pavilion."
        ),
        "background": (
            "It has been a while since Sprent had a good scoop and the rep needs feeding in a "
            "cut-throat industry. Rumors of the fixers' meet reached the newsroom, along with a "
            "whisper that it is going down somewhere in Freeway Park at this time -- and, more "
            "dangerously, a rumor that there is a bomb at it."
        ),
        "notes": (
            "The book prints identical Peter and Petra cards and tells the GM to pick the gender "
            "that best foils the team; this row covers both. Stats: B4 Q4 S3 C7 I6 W5, Ess 5.8, "
            "Bio 1.4, Reaction 5, Init 5+1D6, Combat Pool 7, Karma/Pro 3/2. Etiquette 6, "
            "Interrogation 4 (Verbal 6), Negotiation 5, Computer 3 (Search Ops 5), Winged Aircraft "
            "5, Pistols 3, English 7, Japanese 5, Chinese 4, Salish 4, Russian 2. Bad Puns 6, VIP "
            "Who's Who 6, Interview Techniques 4. Datajack; clean metabolism, mnemonic enhancer 3, "
            "tailored pheromones 2 (+2 dice on all social and Charisma tests). SA Puzzler with gel, "
            "armor clothing 3/0, pocket secretary. Play: 5,000 nuyen interview budget, opening much "
            "lower; brushed off, Sprent shadows the team for the rest of the run and reappears "
            "after every incident. Will trade the bomb rumor, but bargains hard and says nothing "
            "until an interview is agreed. Can also fill gaps in the Legwork table. Killing the "
            "reporter in a park full of security professionals ends badly; capturing needs a "
            "Negotiation (Fast Talking) test on any witness. Any runner who gives an interview "
            "earns cutting remarks from their contacts -- and possibly Sprent as a contact."
        ),
        "contact_skills": ["Media information and news archives", "VIP who's who", "Street sources"],
    },
    {
        "name": "Barnaby Mason",
        "role": "Ambitious junior FBI agent working the meet off the books, hoping to recruit a source",
        "archetype": "Federal Agent",
        "title": "Special Agent, UCAS Federal Bureau of Investigation",
        "race": "Human",
        "gender": "Male",
        "organization": "UCAS Federal Bureau of Investigation",
        "connection": 3,
        "description": (
            "Just another tourist looking around the park -- except that the guy by the food "
            "vending machine has looked the team's way a few too many times, and he is running "
            "textbook surveillance while doing it. Mason is new to his position and wants to go "
            "places. He has no interest whatsoever in a fight and will withdraw if one looks "
            "likely, but he is entirely willing to negotiate with anyone who seems reasonable."
        ),
        "background": (
            "An ambitious junior agent who heard about the meeting through his own contacts, "
            "without specifics, and decided to look into it himself in a somewhat unofficial "
            "capacity -- without notifying anyone else in the Bureau. His interest is in "
            "establishing sources for an ever-growing contact network that he hopes will let him "
            "close cases faster than his fellow agents and make him look good in the bureau. He "
            "routinely learns what is happening in the metroplex before official notice comes down "
            "through channels."
        ),
        "notes": (
            "Stats: B3 Q4 S3 C5 I5 W4, Ess 5.4, Reaction 4, Init 4+1D6, Combat Pool 6, Karma/Pro "
            "3/3. Unarmed 3, Pistols 4, Etiquette 4 (Street 5), Negotiation 4, Interrogation 3, "
            "Intimidation 2, Stealth 3, Biotech 2, Car 2. Corp Background 3, Criminal "
            "Organizations 3, Forensics 3, Law 3, Police Procedures 3, Spanish 3, Street "
            "Background 4. Datajack, smartlink-2, armor jacket 5/3, Ares Predator III with gel and "
            "regular, wristphone, plasteel restraints (barrier 15). Spotting him: Perception (6) "
            "with Stealth complementary; Police Procedures (4) or equivalent then identifies the "
            "surveillance technique as law enforcement. Deal with him fairly and he can be taken as "
            "a contact -- he trades information on the metroplex, criminal organizations, and what "
            "the Feds or Lone Star are working on, and can quietly lose a small indiscretion from a "
            "file, provided the runner brings something of comparable value. Pushed harder, he will "
            "ID the team, ask pointed questions about their gear, and call for backup."
        ),
        "contact_skills": ["Federal and Lone Star case information", "Police and government file access", "Criminal organizations"],
    },
    {
        "name": "Snoop",
        "role": "Cybernetically wired beagle turned loose in the park as a live surveillance demo for the trade show",
        "archetype": "Surveillance Animal",
        "title": "Cyber-beagle exhibit, Confederation of Security Providers show",
        "race": "Beagle",
        "gender": "Male",
        "organization": "Confederation of Security Providers",
        "connection": 1,
        "description": (
            "A small beagle trotting around the park unattended, apt to start chewing playfully on "
            "an ankle or to sit down abruptly and watch whatever is going on. Perception (6) with "
            "one success spots the listening bud in his ear and the cable running to his collar; "
            "two or more successes reveal that his eyes are not natural. Astral perception makes "
            "the whole package obvious at a glance. The implants have left him with a chronic "
            "chewing compulsion -- table legs, cushions, boots, gun stocks, anything."
        ),
        "background": (
            "An exhibit from the security conference, released into Freeway Park as a live "
            "demonstration of his surveillance abilities. He is wired for sight and sound and "
            "everything he sees and hears is relayed to a display screen at a booth inside the "
            "Convention Center."
        ),
        "notes": (
            "Stats: B1 Q4(x4) S1 I2/4 W3, Ess 4.64, Reaction 4, Init 4+1D6, Combat Pool 4; attack "
            "3L, -1 reach (Intelligence is printed '2/4' in the book). All beta-grade cyberware: "
            "chemical analyzer and gas spectrometer, cybereyes (flare comp, low-light, opticam, "
            "thermographic), datajack, hearing amplification, hearing dampener, high and low "
            "frequency hearing, recorder, select sound filter 5. Collar: cell phone, ear-buds, "
            "micro-transceiver 2, signal encryption 4, 400 Mp storage, tracking signal AOD 4. Play: "
            "any time a runner does something notable, roll 1D6 -- on a 1 Snoop has recorded it, "
            "which may bring park security down on them. Stealing him is hard (he is recording and "
            "transmitting) and cruel: without his special dietary supplements he turns vicious and "
            "eventually dies of implant rejection."
        ),
    },
    {
        "name": "Crawler (Halloweeners)",
        "role": "Human Halloweener recruit on Kamikaze, burning his way across the park with a stolen flamethrower",
        "archetype": "Ganger",
        "title": "Halloweeners recruit",
        "race": "Human",
        "gender": "Male",
        "organization": "Halloweeners",
        "connection": 1,
        "description": (
            "Black boots, black pants, black shirt and a black jacket blazoned with a fiery jack "
            "o'lantern, orange bandannas knotted around arms, legs and neck, and a Halloween devil "
            "mask over the face. He rides in off Seneca hooting and yelling, wide-eyed, crazed and "
            "frantic on Kamikaze, and hits whatever catches his drugged fancy with a spray of "
            "burning fuel while taunting and laughing at anyone who shoots back."
        ),
        "background": (
            "A new recruit to the Halloweeners, one of the most violent gangs in the metroplex, out "
            "with Toss to build gang rep by committing the outrageous, psychotic sort of act the "
            "Halloweeners are known for. Legwork on the park (4+ successes) turns up the rumor "
            "beforehand: 'the Halloweeners have been planning to use the place for a demonstration "
            "... a hollerin' run through the park just to show they ain't scared of the cops.'"
        ),
        "notes": (
            "Stats Kamikaze-boosted (base in brackets): B6(5) Q5(4) S8(6) C3 I4 W6(5), Ess 5.5, "
            "Reaction 4, Init 4+3D6 (4+2D6), Combat Pool 7(6), Karma/Pro 2/3. Athletics 3, Bike 4, "
            "Bike B/R 2, Clubs 3, Edged 2, Pistols 3, Spray Weapons 4, Unarmed 4, Whips 2, "
            "Intimidation 2 (Physical 4). Boosted Reflexes 1. Knife, Colt American L36, "
            "flamethrower [Flame, SS, 8M, 10-shot tank, shotgun-spread rules, damage reduced by "
            "Impact armor], armor jacket 5/3, Mitsuhama Blaze racing bike. Kamikaze also gives pain "
            "resistance for the first four boxes. Tactics: sweeps of three or four shots each, "
            "aiming for visible runners, the hedge and the pavilion itself, then out into the city "
            "before the Star arrives -- and back again if not stopped, focusing on the pavilion. "
            "Firing the flamethrower from a moving bike is +2 and costs the next action to a "
            "Handling test. Emptied, they use pistols; forced to melee, knives. They do not back "
            "down until seriously wounded or until Lone Star appears (1 minute after the first "
            "attack). Etiquette can bait them away; Intimidation and Negotiation both work even "
            "drugged."
        ),
    },
    {
        "name": "Toss",
        "role": "Elf Halloweener recruit riding with Crawler; the second flamethrower",
        "archetype": "Ganger",
        "title": "Halloweeners recruit",
        "race": "Elf",
        "gender": "Male",
        "organization": "Halloweeners",
        "connection": 1,
        "description": (
            "Dressed identically to Crawler -- black leathers with the fiery jack o'lantern, orange "
            "bandannas, a devil mask -- and riding the same model of Mitsuhama Blaze. Faster and "
            "smarter than his partner and no less crazed on Kamikaze; he yelps, taunts and laughs "
            "through the whole rampage and prefers to stay on the bike, sweeping in and out of "
            "range rather than standing to fight."
        ),
        "background": (
            "Another new recruit trying to build rep with the Halloweeners. The pair stole the "
            "flamethrowers for the demonstration run; the gang chose Freeway Park precisely because "
            "it is the sort of place gangers are not supposed to touch."
        ),
        "notes": (
            "Stats Kamikaze-boosted (base in brackets): B4(3) Q6(5) S5(3) C6 I5 W6(5), Ess 6, "
            "Reaction 5, Init 5+2D6 (5+1D6), Combat Pool 8(7), Karma/Pro 2/3. Athletics 3, Bike 3, "
            "Clubs 3, Edged 2, Pistols 3, Spray Weapons 4, Unarmed 4, Etiquette 2 (Street 4), "
            "Intimidation 2 (Physical 4). No cyberware. Knife, Colt American L36, flamethrower [8M, "
            "10-shot tank], armor jacket 5/3, Mitsuhama Blaze racing bike. Pushing the envelope: "
            "add offensive grenades [SS, 10S, -1/m] thrown at pursuing vehicles, or have the Lone "
            "Star patrol arrive and start shooting at everyone including the runners. Aftermath: "
            "the Star knows the Halloweeners and is not much interested in citizens defending "
            "themselves -- unless illegal weapons were used visibly, which needs Etiquette "
            "(Corporate) (6) or Negotiation (Fast Talking) (6), rising to TN 8 if the park host was "
            "not penetrated and the cameras got it. Hurting bystanders with illegal gear is not "
            "forgivable at all."
        ),
    },
    {
        "name": "Deborah Figgis",
        "role": "Seattle local going into anaphylactic shock in the middle of the runners' perimeter",
        "archetype": "Civilian",
        "title": "Freeway Park lunchtime visitor",
        "race": "Human",
        "gender": "Female",
        "nationality": "UCAS",
        "connection": 1,
        "description": (
            "An ordinary local Seattleite enjoying the park at lunchtime, who suddenly rushes at a "
            "nervous stranger and starts pawing frantically at him. She looks for all the world "
            "like a madwoman attacking a passer-by. In fact she is in a panic, unable to speak and "
            "barely able to breathe, trying to get help from the first person she can reach."
        ),
        "background": (
            "Deborah has a Severe allergy to mushrooms and has been foolish enough to eat "
            "something containing them."
        ),
        "notes": (
            "Runs the optional 'Watch What You Eat' encounter, staged at whatever boundary line the "
            "team has drawn. She reaches Ranjit Devi at a Moderate wound (5 boxes) and takes a "
            "further Light wound every 10 turns (ingestion, not the usual per minute). Perception "
            "(5), with Biotech and Medicine complementary, sees that she is in real trouble. "
            "Treatment: make her vomit with Biotech (5), or build an antidote from a medkit with "
            "Biotech (4); healing magic also works; then first aid per SR3 p.129. Etiquette "
            "(Corporate) (4) gets the guards or a bystander to call a paramedic without awkward "
            "questions. Left alone she collapses, draws a useless crowd, and the crowd draws the "
            "authorities; a DocWagon standard response unit arrives in 5 minutes. If the team has "
            "no medic at all, the scene still works as a reason to make them talk to ordinary "
            "people, and a passer-by shouting 'let me through, I'm a doctor' will bail them out "
            "while drafting one runner as an assistant."
        ),
    },
    {
        "name": "Ranjit Devi",
        "role": "Nervous Indian tourist mistaken for an assailant when Deborah Figgis collapses on him",
        "archetype": "Civilian",
        "title": "Tourist from Calcutta",
        "race": "Human",
        "gender": "Male",
        "nationality": "Indian",
        "connection": 1,
        "description": (
            "A nervous-looking Indian tourist from Calcutta walking past the runners' boundary line "
            "when a strange woman throws herself at him and starts clawing at his clothes. "
            "Convinced he is being attacked, he panics and bats ineffectually at her, which from a "
            "distance looks exactly like a man beating a woman in a public park in front of several "
            "hundred off-duty security professionals."
        ),
        "background": (
            "A visitor to Seattle with no connection to the meet, the fixers, or anything else in "
            "the adventure -- pure bad luck and bad timing."
        ),
        "notes": (
            "The misdirection half of the 'Watch What You Eat' encounter: the scene reads as an "
            "assault until somebody makes the Perception (5) test and realizes Deborah is dying, "
            "not attacking. Left to run, the scuffle becomes a circus and pulls the park patrol "
            "straight through the runners' cordon at exactly the wrong moment. He does not fight, "
            "speaks no more Cityspeak than a tourist needs, and will be extremely grateful, and "
            "extremely talkative to any reporter, if the runners sort it out."
        ),
    },
]

ORG_UPDATES = {
    "Halloweeners": {
        "notes_append": (
            "SRM 00-01 Mission Briefing: two new recruits, Crawler (human) and Toss (elf), ride "
            "stolen flamethrowers into Freeway Park in Downtown at lunchtime, high on Kamikaze, "
            "purely to build rep -- the gang has been planning a 'demonstration' run through the "
            "park to show it is not scared of the cops, and street legwork picks the rumor up "
            "beforehand on 4+ successes. Recruit stats: Karma/Pro 2/3, Spray Weapons 4, armor "
            "jacket, Colt American L36, knife, Mitsuhama Blaze racing bike, flamethrower [8M, "
            "10-shot tank]. Both wear black leathers with a fiery jack o'lantern, orange bandannas "
            "and Halloween devil masks. Lone Star knows the gang well enough that officers are not "
            "much interested in citizens who defend themselves against them."
        ),
    },
    "Lone Star Security": {
        "notes_append": (
            "SRM 00-01 Mission Briefing: Freeway Park in Downtown is policed on the cheap. Three "
            "two-officer patrols of probationary officers -- inexperienced, demoted or unambitious, "
            "not fully authorized police -- walk the park (B4 Q3 S4 C3 I3 W3, Karma/Pro 1/2, stun "
            "baton, Ruger Thunderbolt with gel, armor jacket, commlink). They notice trouble one "
            "turn after it starts, arrive in 1D6 turns, and can call real Lone Star support in a "
            "further 2D6. A Lone Star mage crosses the park astrally about every 15 minutes and "
            "spots suspicious magic on a 1 on 1D6; combat, manipulation and dangerous illusions "
            "bring a mage with elementals in 1D6 turns. Talking the Star out of an incident is "
            "Etiquette (Corporate) or Negotiation (Fast Talking) at TN 4 with no evidence, TN 6 "
            "with witnesses, TN 8 if the park cameras recorded illegal gear. Injuring bystanders "
            "with illegal weapons cannot be talked away. Lone Star also has a booth at the "
            "Confederation of Security Providers trade show next door."
        ),
    },
    "UCAS Federal Bureau of Investigation": {
        "notes_append": (
            "SRM 00-01 Mission Briefing: the Bureau has a booth at the Confederation of Security "
            "Providers show in the Seattle Trade and Convention Center. Special Agent Barnaby "
            "Mason, an ambitious junior agent, works the fixers' meet in Freeway Park entirely off "
            "the books -- without notifying anyone else in the Bureau -- hoping to recruit a shadow "
            "source. He can trade file access and word of what the Feds and Lone Star are working "
            "on, and can quietly lose a minor indiscretion, in exchange for information of "
            "comparable value."
        ),
        "leadership_add": [
            {"name": "Barnaby Mason", "title": "Special Agent, Seattle", "notes": "Junior, ambitious, building an unofficial contact network; Karma/Pro 3/3."},
        ],
    },
    "Wuxing, Inc.": {
        "notes_append": (
            "SRM 00-01 Mission Briefing: Wuxing's Seattle branch runs an attack demonstration for "
            "the Confederation of Security Providers show, flying a wing of three Azure Cloud VTOL "
            "drones down the I-5 canyon, low over Freeway Park, and into the Convention Center to "
            "shoot up dummy targets. The flight plan is registered with Lone Star; a minor "
            "bureaucrat routed it over the park to give the patrons a thrill, which means the guns "
            "come in lined up on the runners. Azure Cloud: Handling 3, Speed 210, Accel 12, Body 2, "
            "Armor 3, Sig 6, Pilot 3, Sensor 2, Init 6+3D6, IVIS pool 4, Adaptation 3, Clearsight 3 "
            "and Sharpshooter 3 autosofts, robotic reflexes 2, one firmpoint LMG [BF/FA, 5S Stun, "
            "gel, half recoil from the turret], BattleTac IVIS receiver. They are in robot mode and "
            "ignore everyone unless fired on; attacked, they Sensor Lock on 8 dice versus the "
            "shooter's Signature and answer with two 3-round bursts at 8D Stun on 7 dice, breaking "
            "off at Medium or Serious damage. Destroy one and Wuxing sends a heavily armed "
            "retrieval team within 1D6 minutes, suppresses the whole incident to avoid the "
            "embarrassment -- and the humiliated Wuxing manager who organized the demo becomes a "
            "minor enemy."
        ),
    },
    "Seattle Mafia": {
        "notes_append": (
            "SRM 00-01 Mission Briefing: it is common knowledge in the shadow community that rumors "
            "persistently link THE Sports Bar, on the corner of University Street and Terry Avenue "
            "in Downtown, to the Mafia. Trotter picks it as the muster point for the runners "
            "precisely because it is a place where nobody starts anything. The fixer Rolando (Ray "
            "Marcello) carries Mafia Background 3 and dresses like a trid stereotype of the "
            "organization without, so far as anyone can establish, actually belonging to it."
        ),
    },
    "Knight Errant Security Services": {
        "notes_append": (
            "SRM 00-01 Mission Briefing: Knight Errant exhibits alongside Lone Star and the FBI at "
            "the Confederation of Security Providers show in the Seattle Trade and Convention "
            "Center, Downtown. Street legwork (2 successes) names all three; 3 successes adds that "
            "the vendors will be trying to outdo each other, which a smart operator can play off."
        ),
    },
    "DocWagon": {
        "notes_append": (
            "SRM 00-01 Mission Briefing: if Deborah Figgis's anaphylactic collapse in Freeway Park "
            "is left unattended, a DocWagon standard response unit arrives on scene in five "
            "minutes -- which is five minutes of paramedics, questions and attention in the middle "
            "of the runners' cordon during the meet hour."
        ),
    },
}

LOC_UPDATES = {
    "Renraku Arcology (SCIRE)": {
        "notes_append": (
            "SRM 00-01 Mission Briefing: by 2064 the arcology still dominates the skyline over "
            "Freeway Park -- 'what dominates your senses, what never leaves your attention, is the "
            "monstrous Renraku Arcology looming overhead. After what happened in that place, what "
            "might be watching through those thousands of windows...' The shutdown, the siege and "
            "the slow, vicious fight for recovery are recent enough history that street stories "
            "about the building are still half unbelievable, and the shadow of it is used in the "
            "adventure purely as atmosphere pressing on a team of brand-new runners."
        ),
    },
    "The Ork Underground": {
        "notes_append": (
            "SRM 00-01 Mission Briefing: the fixer Willis 'Willy' Daltree has worked the "
            "Underground for over twenty years, low key by deliberate policy -- no big jobs, no "
            "cutting-edge gear, but a very broad and very loyal small-fry contact base and Seattle "
            "Underground 8. He is a popular figure, related through an extensive family to a great "
            "many of its inhabitants, and many ork and troll shadowrunners got their first job "
            "through him. Betsy and Becky Ross, Rolando's ork bodyguards, spend their off hours in "
            "the Underground's nightclubs (Ork Underground Night Clubs 6)."
        ),
    },
}

NPC_UPDATES = {}

TAG_EXISTING = {}

MATRIX_HOSTS = """
### Freeway Park host (run from the Seattle Trade and Convention Center)

Green-5/10/8/8/9/8. Feeds every camera, sensor, microphone, speaker, sprinkler and interactive
display in the park, plus the park maintenance schedules (including the service record that does
*not* show a maintenance call for "Hugh"). Access from the park side: Electronics B/R (4), base
time 30 seconds, to open an interactive unit's casing, then Electronics (4) to fit a dataline tap;
the same pair of tests shuts an individual camera or sensor down. Camera feeds are not monitored
constantly -- automated pattern recognition triggers the alerts, and a few dead cameras are
expected, so the pavilion's coverage can be blacked out for the hour without an alarm. Uncovered
suspicious activity is recorded on a 1-2 on 1D6.

| Step | Event |
| --- | --- |
| 5 | Probe-6 |
| 10 | Probe-8 |
| 15 | Scout-7 |
| 20 | Trace-7 |
| 25 | Passive Alert; security deckers (inferior) |
| 30 | Ripper (bind-rip)-7 |
| 35 | Trace-7 with trap Blaster-4 |
| 40 | Blaster-7 |
| 45 | Active Alert |
| 50 | Construct-8 (Killer-10, Probe-6) |
| 55 | Blaster-9 |
| 60 | Sparky-11 |
| 65 | Shutdown |

Paydata: 3 points (100 Mp, 70 Mp, 40 Mp). Michelle Rampling (Fences 3 (Paydata 6), Seattle Matrix
8) is the obvious buyer. Note the campaign cap: no single character walks away with more than
about 5,000 nuyen from this run, paydata included.

The park is also a known playground for young hackers who break in to make mischief -- sprinklers
firing unexpectedly, the park speakers turned up loud and badly -- which the GM can use as cover
noise or as a complication in the middle of the meet hour.
"""

NOT_BUILT = """
- **The dead fixer** -- never named. The intro calls the fixer "he or she" and the Legwork table
  says "a local fixer got popped and now one of her buddies is selling off her little black book",
  so the book leans female without committing; the headquarters was a three-storey building in
  Redmond, now a lot full of concrete and rebar. Captured in the synopsis and Trotter's background.
- **The rival fixer who planted the bomb** -- never named either. He refused the invitation, bribed
  one of the organizing shadowrunners for the details, and expects to seize the data cheaply once
  the competition is dead. A deliberate loose end for later Missions play.
- **The unnamed summoning magician** in a cafe 300 meters from the pavilion, holding the rating 6
  ward, two force 3 watchers and the force 6 air elemental; run him with the Lone Star magician
  stats from New Seattle p.114. Folded into the Maynard Pavilion notes.
- **"Hugh"** -- the Chrysler-Nissan Caretaker gardening drone carrying the bomb (Hand 4/4, Speed 10,
  Body 1, Pilot 1, gardening autosoft 3, 5-liter liquid tanks). A machine, not a person; kept in the
  Freeway Park notes and the synopsis. Base value 3,500 nuyen if defused and stolen.
- **The free field spirit of Freeway Park** -- unnamed, materializes as a 1.5-meter girl with a
  skateboard and plays Accident on whoever amuses it. Kept in the Freeway Park notes.
- **The other five or six fixers at the meet** -- the will listed almost a dozen and only six get
  contact cards; the rest arrive, each with one obvious bodyguard, and are never described.
- **Chrysler-Nissan, Ares Macrotechnology, Mitsuhama, Ruger, Colt, Ceska, Heckler & Koch, Defiance**
  -- manufacturer name-drops on gear only.
- **The Everett Jets** (the poster in THE Sports Bar's Combat Biker room) -- team name-drop.
- **The frustrated park technician, the annoying busybody, the wanted fugitive** -- Pushing the
  Envelope hooks with no names or stats.
"""

PLAY_NOTES = """
- This is the campaign's demo scenario: it must run in as little as two hours, with the optional
  Case Studies dropped in only when there is time. Leave 15-20 minutes at the end for Debriefing
  Logs. Only one event has a fixed clock -- the bomb at 1255 -- so everything else can be reordered
  freely to suit the table.
- Every field of expertise is deliberately covered (combat, negotiation, magic, rigging, Matrix) and
  several Case Studies exist to let one archetype shine: The Drunken Shaman for magicians, Cyber
  Snoop and Fly By for riggers and deckers, Here's the News and The Nosey Fed for faces, Watch What
  You Eat for a medic. Pick by team composition. Do not run more than two or three at once.
- The core lesson is restraint. Downtown is AAA, the convention next door is full of cops and
  corporate security eating lunch, and the correct answer to almost every provocation is the quiet
  one. If the team is spoiling for a fight, stage the demonstration the book suggests: an unrelated
  NPC across the park draws a weapon and is instantly gunned down by the guards (with gel rounds,
  though nobody watching can tell).
- Scarper is the safety net and the clue line. Etiquette (Street) (4) plus Interrogation (4) gets
  "Hugh" out of him; he also advises on the field spirit, comments on unsubtle work, and can
  miraculously survive the blast to heal the wounded. Do not overplay him -- let the runners do the
  work.
- The bomb clues are layered: Scarper's worry; no maintenance record in the host; a Perception (6)
  after half an hour notices Hugh has watered nothing; a Perception (10) within a meter catches the
  chemical smell; and at 1254 the drone simply drives at the wall. Disarming is Electronics B/R (6)
  over a base minute to get inside (failure detonates it), then Electronics (4) to kill the timer.
  Draining the tank without disabling the safeguard detonates it at half volume for 18D.
- Rolando is a set-piece in three modes -- confrontation, persuasion or smarts. Reward the team that
  makes him leave without a shot fired; he departs with insults and grudging admiration and is
  available as a contact.
- Payoff: balance of 2,500 nuyen each, plus 500 if the hour was genuinely clean, plus scavenged
  gear and paydata, capped at about 5,000 nuyen per character. Karma: 1 for finding the bomb, 1 for
  disarming it, 1 for an uninterrupted meeting, 1 for not being publicly identified as a
  shadowrunner, -1 for unnecessary public violence; 7 maximum with roleplaying awards.
- Contacts are the real reward and the campaign's on-ramp: each character may take at most one
  fixer (Fox, Joeli Gibson, Lyle Green, Manny, Michelle Rampling, Willis Daltree, or Rolando) plus
  one other (Scarper, Barnaby Mason, Pete/Petra Sprent). Match the fixer to how the player actually
  played the hour -- that choice is what carries forward into the rest of the season.
"""
