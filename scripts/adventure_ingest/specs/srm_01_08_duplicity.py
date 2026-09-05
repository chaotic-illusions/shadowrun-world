# SRM 01-08 Duplicity (FanPro/WizKids, 2005, SR3) -- campaign order #51. Everett (Griffin
# Biotechnology at the end of 172nd Street off Marine Drive, Dusty's Steak House), southern Tacoma
# near the docks (the Knight Errant simsense black site), Downtown (Dante's Inferno).
# SETTING NOTE: this is a SEATTLE adventure, not a Denver one, and it is Shadowrun Third Edition,
# not SR4. "Duplicity is an adventure in the Rose Croix series", the third and final Mission against
# Griffin Biotech's Everett facility after SRM 00-03 FORCEd RECON and SRM 01-04 The Gambler. Every
# location row is therefore city "Seattle".
# Dating: no in-world date is printed; the campaign year is 2064, matching the rest of Season 1. The
# adventure's internal timeline is Wednesday 17:30 (Lyle Green's first call), Wednesday 22:15 (the
# meet at Dante's Inferno), Thursday 13:20 (the runners captured and taken to Tacoma), Thursday
# 20:10 (the runners realize they are in a simulation), Friday 22:00 (job deadline). The adventure
# opens in media res inside the simulation and flashes back to the meet.
# Book editing inconsistencies, noted on the affected rows:
#   * the deadline is Friday 22:00 in the Timeline, "48 hours (until 9PM Friday)" in Cold Shower,
#     and "within 24 hours" in that scene's What's Up Chummer blurb;
#   * a high-alert shift is 39 guards in the adventure text (1 commander, 2 gate, 4 control room, 2
#     main lobby, 6 per floor, 2 plus a K-9 team per quadrant) and 38 in the player Security Report
#     (3 control room, 4 main lobby, 4 per floor, 4 per quadrant) -- the handout is the pre-alert
#     baseline the runners were given, so both are "true";
#   * the player handout states "No spirits or watchers monitor the building" and a Background Count
#     of 1, while the high-alert adventure text posts a Knight Errant magician in the control room
#     with watchers and low-level spirits combing the site and four K-9 handlers with barghests on
#     constant duty;
#   * the Ares Predator II is 7M Stun with gel in every guard entry and 9M in the shared gear list;
#   * the opening narration says "the tenth time today" twice while Behind the Scenes says "at least
#     five times" and Pushing the Envelope says "the fifth time";
#   * Rebecca Owls-Breath's stat block is OCR-garbled -- Unarmed Combat, Intimidation, Shadowrun
#     Tactics and Enhanced Articulation have all lost their ratings;
#   * the Yamatetsu team is "assigned to the Seattle office" in the cast entry but Moscow-based in
#     the legwork table, which also prints "Yamatetstu";
#   * the aftermath handout reports explosions demolishing "the northern half of the compound" while
#     the mission has Yamatetsu wiring the section under the hilltop, i.e. the underground half;
#   * the standard guard's knowledge list reads "Launch Weapons (Launchers)" where the supervisor and
#     SWAT entries read "Heavy Weapons (Launchers)";
#   * the prototype is cloning and custom-cultured-organ research in Cold Shower, "a bioware
#     prototype" in Debugging, and "standard and cultured bioware" in the legwork table;
#   * the 01-08B recon photo labels the neighbouring property "Brackhaven Estate", where SRM 00-03
#     FORCEd RECON (and this spec) name it the Brackhaus Estate.
# Cross-spec note: SRM 00-03 FORCEd RECON owns the Griffin facility, its grounds neighbours, Rebecca
# Owls-Breath, Dr. Indira Chontel (the 01-08B second-floor map labels her lab and office "Dr.
# Chantel's"), the Knight Errant shift supervisor, Michael Mackie and Mackie Construction; SRM 01-01
# Double Cross owns Rose Croix, Michael Davenport and a second, separate Griffin facility row
# ("Griffin Biotechnology Facility (Everett)"); SRM 00-01 Mission Briefing owns Lyle Green. All are
# appended to here, never re-created. The duplicate Griffin facility rows are flagged below and both
# receive an append.
# Source text: docs/Adventures/text/SRM01-08A_Duplicity.txt (19 pages) and
# docs/Adventures/text/SRM01-08B.txt (play aids, 17 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "SRM 01-08 Duplicity"
ORDER = 51
SOURCE = "SRM01-08A_Duplicity.pdf, pp. 5-19; SRM01-08B.pdf (Play Aids), pp. 2-16"
YEAR = "2064"

SYNOPSIS = """
"Griffin Biotechnology has been a revolving door for shadowrunners." Two Missions have already been
through the Everett facility: **FORCEd RECON**, where runners bluffed guards and worked contacts for
an interior layout, and **The Gambler**, where a team breached it without leaving a trace and lifted
paydata off a standalone terminal. Both were organized by the fixer **Lyle Green** and paid for by
**Rose Croix**. Now news of a prototype has pushed CEO **Walter Broward** into one last daring push.
Griffin has a working system for growing custom cultured organs -- generic marker-free organs that
genetic modification can retag for a specific patient in hours instead of months, success rates
still hovering around fifteen percent -- and it is the research that bought **DocWagon**'s support.
Broward wants it. Failing that, he wants DocWagon not to have it.

The first attempt failed. **Knight Errant**, tired of the traffic through a site it is paid to hold,
took matters into its own hands: it captured the team with a SWAT squad, dosed them with Laes and
depressants, and built an artificial version of the facility to train its elite squads in
anti-runner tactics. The adventure opens inside that simulation, on what feels like the tenth run of
the day -- bypass the monowire, drop over the wall, thirty seconds of open ground, five-four-three-
two-one-go on the hourly three-second backup gap, gun down the two guards in the entrance hall, punch
the basement button. The way out is to reach a secured section or be defeated, or to pull the plug
and eat dumpshock.

Waking up is scene two: ergonomic chairs with massagers, IV bags prepared and not yet administered,
whiteboards reading "Randomize backup cycle" and "Auditory alarm at door opening?", a heavy plasteel
door on a biometric maglock, and a technician making a panicked move for the alarm panel. The site is
an inconspicuous building in southern Tacoma near the docks, taken over in short order -- heavy
sensors outside, light security inside, four bored guards watching an urban brawl game, a SWAT squad
in debriefing, and the runners' own gear sitting in the armory, due to ship to Knight Errant HQ for
inventory in forty-eight hours. Then a text message -- "Call me, LG" -- triggers the flashback to the
seventh level of **Dante's Inferno** on Wednesday night, and the job: 3,000 nuyen plus 3,000 per
table rating each, sixty percent for destruction instead of theft.

The third act is Griffin at high alert, gloves off, with Ares-supplied security throughout, Force 8
wards, walls full of pressurised FAB bacteria, four barghest teams and thirty-nine guards. Rounding a
corner the team meets a second squad in black jumpsuits setting charges: a **Yamatetsu** covert ops
team, the same one from *Strings Attached*, with orders to demolish the underground half of the
building and close the tunnel. Their agenda and the runners' happen to line up. Afterwards, Lyle
buys dinner at **Dusty's**, and KSEA runs the words "terrorist attack".
"""

TIMELINE = """
- **Over the previous quarter** -- Griffin Biotechnology takes a huge influx of cash from DocWagon
  and Ares, breaks through on mapping the motor centers of the brain and on tissue development, and
  builds a state-of-the-art secured facility in Everett. Ares supplies the entire security suite at
  bargain prices; Knight Errant takes the guard contract.
- **SRM 00-03 FORCEd RECON** -- runners tramp across the grass, bluff past guards and hit every
  contact they can think of for a substantial interior layout. Organized by Lyle Green, paid for by
  Rose Croix.
- **SRM 01-04 The Gambler** -- runners breach the facility without leaving traces and steal paydata
  from a standalone terminal, using the key code and passkey of a lead researcher. Again funded by
  Rose Croix.
- **Over a month later, Wednesday 17:30** -- Lyle Green makes initial contact with the team.
- **Wednesday 22:15** -- the meet on the seventh level of Dante's Inferno. 3,000 + (3,000 x TR) each
  for the prototype and all associated research, 60 percent for destroying them instead. 48 hours.
- **Thursday, before 13:20** -- the assault goes in using a stolen car. It fails.
- **Thursday 13:20** -- the runners are captured by a Knight Errant SWAT squad and taken to the
  Tacoma site. Laes and depressants; the simulation begins.
- **Thursday, through the day** -- at least five runs through the simsense reconstruction of Griffin
  at high alert, each ending differently. KE's whiteboards fill up with lessons learned.
- **Thursday 20:10** -- the runners realize they are in a simulation. Adventure begins.
- **Immediately after** -- breaking the sim, the escape from the Tacoma compound, recovering gear
  (and ideally KE uniforms) from the armory, and optionally inserting false data into the Everett
  host from the Tacoma secondary host.
- **Friday** -- the flashback meet is remembered, and the team goes back to Griffin. All security
  measures are at high alert because of the failed attempt. The Yamatetsu team rolls in on its own
  schedule with charges already placed through the ventilation and the FAB delivery panels.
- **Friday 22:00** -- job deadline (the Cold Shower scene says 21:00).
- **After** -- payoff at Dusty's in Everett. KSEA reports a terrorist attack, dozens dead, one wing
  demolished. Knight Errant stock drops a tenth of a point; Griffin plummets seven points. The
  runners' gear was due to ship to Knight Errant HQ for inventory forty-eight hours after capture.
"""

ORGS = []

LOCATIONS = [
    {
        "name": "Knight Errant Tacoma Compound",
        "location_type": "corporate facility",
        "city": "Seattle",
        "district": "South Tacoma (near the docks)",
        "security_level": "Corporate High Security",
        "controlling_org": "Knight Errant Security Services",
        "summary": "The inconspicuous building where Knight Errant runs captured shadowrunners through a simsense reconstruction of Griffin Biotech to train its own squads -- heavy sensors outside, light security inside",
        "description": (
            "An inconspicuous building in southern Tacoma near the docks, housing a set of highly "
            "illegal tests. Ares has heavy sensor and security equipment set up outside to ensure the "
            "facility's privacy, but the building was taken over in short order and there has not yet "
            "been time to lock down the interior. Beyond the simsense chamber where the runners wake "
            "-- ergonomic chairs with small massagers to prevent pressure points and bedsores, IV bags "
            "of unknown drugs and nutrients prepared but not yet administered, whiteboards covered in "
            "cryptic commentary on the subjects' behaviour, and a heavy plasteel door whose maglock "
            "runs off a biometric interface -- the map shows a storage area, a security office, an "
            "airlock structure, a medical bay, a common area and mess hall, a bathroom, an RRT staging "
            "area, a computer room and the armory. All internal maglocks are rating 5 with biometric "
            "or passkey interfaces; technicians have access to the common areas and labs while "
            "security has carte blanche, and all access attempts are logged and checked weekly."
        ),
        "notes": (
            "Garrison at the moment the runners come round: four standard security guards in the "
            "guardroom watching camera feeds on a cyclic system that switches every three seconds "
            "(pulling a specific feed is a simple action), currently distracted by an urban brawl game "
            "on a secondary monitor and comfortable in the assumption that the Rapid Response team will "
            "handle anything horrible; 1+TR labtechs in the chamber; and 2+TR SWAT team members. If "
            "the runners beat the simulation the SWAT team is in a debriefing from its last mission; if "
            "they dumpshocked out, the team spends five minutes checking the scenario for tampering "
            "before it armors up, and will respond in armored vests rather than full security armor if "
            "an alarm goes before that. There is no on-site magical support -- an astrally projecting "
            "mage arrives three combat rounds after any alarm and summons elementals according to the "
            "threat. Hitting the alarm panel brings guards in just under a minute. Security responds "
            "non-lethally at first with a combination of flash-bangs and gel rounds and switches to "
            "lethal only against deadly force. THE ARMORY is the objective: the runners' own gear is "
            "held there, due to ship to Knight Errant HQ for inventory purposes in forty-eight hours, "
            "along with every optional item on the Griffin equipment list -- and the GM is told to "
            "remind the players of the tactical value of taking KE uniforms, weapons and armor as a "
            "disguise for later. The best-case escape is subduing the techs quietly, using a palm on "
            "the biometric lock and moving down the hallway; the runners are unarmed and unarmored "
            "until the armory, and the book says to throw the book at anyone who forgets it."
        ),
    },
    {
        "name": "Griffin Biotechnology Compound Grounds",
        "location_type": "corporate facility",
        "city": "Seattle",
        "district": "North Everett (172nd Street off Marine Drive)",
        "security_level": "Corporate High Security",
        "controlling_org": "Griffin Biotechnology",
        "summary": "Hillside, pine forest and a 4m elemental-raised granite wall under monowire, seeded with hidden cameras, pressure pads, UV laser grids and ultrasound -- and one exploitable weakness",
        "description": (
            "The facility sits at the end of 172nd Street off Marine Drive, closest exit I-5 206. The "
            "previous owner bought out the surrounding homes and connecting streets, so the whole area "
            "belongs to Griffin; the former buildings have been torn down and grown over. External "
            "physical security is mostly terrain: the facility is built into the side of a hill, the "
            "approach road climbs the side of another, and the surrounding area is thick pine forest "
            "that nothing wider than a two-wheeled motorcycle can maneuver through. A 4-meter stone "
            "wall rings the grounds, granite in large sections because it was raised by earth "
            "elementals out of the natural rock, at Barrier rating 24. The north, south and east walls "
            "are topped with monowire; only the west side, facing the street entrance, is not. High-"
            "powered daylight halogens light the main gate, the main drive, the front of the facility "
            "and the parking area. Beyond the gate and guard shack are the parking areas and a helipad; "
            "the neighbours on the aerial recon photo are Puget Sound, the Brackhaus estate, the Draco "
            "Foundation complex, Universal Omnitech and Ares private property, a Stuffer Shack and BP "
            "gas station, and the Dohner estate."
        ),
        "notes": (
            "Monowire: Perception (10) to notice, 10S damage, wired into the security system so "
            "breaking it breaks a circuit and sets off an alarm; Electronics (5) with insulated cutters "
            "and an electronics toolkit bypasses it. Characters should not be able to steal monowire "
            "from this facility. Cameras at the gate and along the drive are mounted openly on posts; "
            "cameras in the woods and around the rear are hidden inside artificial trees and boulders "
            "(Perception 10, or Perception 6 with thermographic, ultrasound, other non-normal senses or "
            "astral perception, since the fakes have no living aura). All cameras: 120-degree view, "
            "normal spectrum, low light, thermographic, 5x variable zoom, normal-range audio pickups, "
            "black ballistic polymer covers bulletproof to heavy pistol and below. Sensor grids fill "
            "the gaps between rotational camera timers: pressure pads set to respond over 30 kg to "
            "avoid small animals, and UV laser grids strung between artificial trees, both at "
            "Concealability 15 (6 with astral perception or specialized detection). Rating 6 ultrasound "
            "sensors closer to the building pick up invisible intruders but are not operational at this "
            "time. Astral: Background Count 1 through the facility and three meters either side of the "
            "main wall, from the amount of magic used in construction. THE WEAK POINT: all external "
            "sensors, cameras and other devices are connected directly to slave nodes in the security "
            "system, so runners who stealth into the compound can place a dataline tap and hack the "
            "security computer far more easily than decking in from the public SAN -- from inside they "
            "can modify the biometrics database, pull guard schedules and more. Coming over the wall "
            "and through the forest gives the guards and systems time to spot them; being spotted "
            "triggers a silent alarm and gives the garrison ample time to upgrade at the armory and "
            "call Knight Errant for backup. Distractions mostly backfire: the closest team investigates "
            "while the shift supervisor deploys the rest, the goal being containment rather than a "
            "pitched battle, with spirits, elementals and astral scouts arriving within minutes and "
            "support teams shortly after."
        ),
    },
    {
        "name": "Griffin Biotechnology Subterranean Labs (Float Floor)",
        "location_type": "research lab",
        "city": "Seattle",
        "district": "North Everett (172nd Street off Marine Drive)",
        "security_level": "Corporate High Security",
        "controlling_org": "Griffin Biotechnology",
        "summary": "The buried half of Griffin: Beta Clinic, microtech and cyberware prototyping, the main nanotech lab on a vibration-isolated float floor -- and the wing Yamatetsu came to bring down",
        "description": (
            "The basement level, reached by the main stairwell, the lobby doors, the elevators or "
            "either freight elevator. Around the main stairwell are the generators, general supplies "
            "and storage, maintenance, restrooms, secure labs, observation rooms, mechanical "
            "fabrication rooms and a kitchen. Deeper in lie the operating room -- the Beta Clinic -- "
            "with laundry, restrooms and showers, a nurse's station and monitoring, and recovery rooms. "
            "Past those an airlock and bridge lead onto the Float Floor, an inner section that floats "
            "above the foundation and is separated from the walls to minimize vibration and external "
            "effects, holding the microtech labs and cyberware assembly and prototyping and the main "
            "nanotech lab. Every hallway, wall, floor and ceiling on this level is rigged for FAB "
            "dispensers, and all three wings past the main lobby are astrally warded. The most secure "
            "doors down here carry rating 10 retinal-scan maglocks."
        ),
        "notes": (
            "Map note from the play aids: the airlock, the Float Floor, the microtech labs and the main "
            "nanotech lab appear ONLY on Mackie Construction's files -- the construction firm's "
            "drawings are the sole record that the deepest part of the facility exists, which is what "
            "made Mackie a target in SRM 00-03 FORCEd RECON. This level is the objective from both "
            "directions at once: the runners are here for the microbiology lab, the prototype and the "
            "research, while the Yamatetsu covert ops team has secured the back half and placed charges "
            "throughout the ventilation system and within various access panels for the FAB delivery "
            "system in the walls, with orders to demolish the section under the hilltop and close the "
            "tunnel. In the simulation, reaching the Beta Clinic or passing the airlock toward the "
            "nanotech facility counts as completing the scenario requirements and ends the sim on the "
            "runners' terms. Astral security here is at its heaviest: Force 8 opaque wards, walls "
            "collocated with security doors that hold tanks of Fat Bacteria to be pressure-sprayed into "
            "the surrounding walls, floor, ceiling and doors on an astral breach (astral Reaction (8) "
            "to notice while trying to pass through such a wall; travelling by the hallways and normal "
            "entryways never finds them), a second release into the hallways to help security locate "
            "the intruder, and biofiber lining in the inner walls, floors and ceilings of the sensitive "
            "labs."
        ),
    },
    {
        "name": "Wyndham Crossroads",
        "location_type": "hotel",
        "city": "Seattle",
        "security_level": "Patrolled / Commercial",
        "summary": "Where the legwork table says to ask for a Mr. Tamagochi if you want to reach the Yamatetsu covert ops team",
        "description": (
            "The address the shadow community hands over at four or more successes when anyone asks "
            "about the Yamatetsu team: 'Ask for a Mr. Tamagochi at the Wyndham Crossroads.' It is the "
            "only civilian contact point the adventure offers for a unit the corporation does not "
            "normally let anyone approach -- the team is based out of Moscow, only comes to North "
            "America for something big, and is 'so good they don't need Battletac, probably some kind "
            "of magical link'. The earlier entries on the same table are a warning: at zero successes, "
            "'Listen, I'm going to pretend you never asked me that.'"
        ),
        "notes": (
            "Reached through the Yamatetsu Team legwork table (runner contact, any corporate contact, "
            "any Russian contact, data broker, fixer or Mr. Johnson; Local Shadowrun Community, "
            "(Mega)corporate Security or Data Brokerage at TN 4). The practical use is preparation: a "
            "team that does this legwork before the third act knows there is a second squad in the "
            "building and can plan for an alliance instead of a corridor firefight. It is also the "
            "adventure's one lead to the same Yamatetsu operators the runners may have tangled with in "
            "SRM 01-02 Strings Attached, where the street remembers them getting 'tangled up with some "
            "Rastafarian'. The book gives the hotel no description, no floor plan and no scene -- it is "
            "a name, an ask-for, and a door the GM can open."
        ),
    },
]

NPCS = [
    {
        "name": "Mr. Tamagochi",
        "role": "The name the shadows give for reaching the Yamatetsu covert ops team -- ask for him at the Wyndham Crossroads",
        "archetype": "Corporate Handler",
        "title": "Yamatetsu contact, Wyndham Crossroads",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Yamatetsu Corporation",
        "connection": 4,
        "description": (
            "A name at the end of a legwork table and nothing more: the answer that comes back at four "
            "or more successes when a runner asks about the six operators in black jumpsuits. Everyone "
            "who knows anything about the team knows better than to talk -- at zero successes the "
            "response is 'Listen, I'm going to pretend you never asked me that' -- so a contact willing "
            "to hand over a name and an address is handing over something the corporation would rather "
            "keep quiet. Whether Tamagochi is the team's handler, its cover identity in the metroplex "
            "or simply the man who answers the phone, the book never says."
        ),
        "background": (
            "He sits behind a team that Yamatetsu keeps for missions the company cannot afford to trust "
            "to shadowrunners: five combat support personnel and a mage, extremely loyal, trained so "
            "tightly together that they look Battletac-linked when they are not, based out of Moscow "
            "and brought to North America only for something big. Legwork places them 'assigned to the "
            "Seattle office' in the cast entry and Moscow-based in the table -- both may be true of a "
            "unit on temporary assignment. Their previous outing in the metroplex was SRM 01-02 Strings "
            "Attached, remembered on the street only as work where they 'tangled up with some "
            "Rastafarian'."
        ),
        "notes": (
            "No statistics, no description and no scene -- he is a name, an address and a door. Plot "
            "use: the only handle the adventure offers on the Yamatetsu team before the runners walk "
            "into them mid-corridor with charges half-laid. A team that follows this lead can arrive at "
            "the Office Politics encounter expecting a negotiation rather than an ambush, which is the "
            "difference between a short-term alliance and a firefight that costs both squads the "
            "building. Give him whatever weight the table needs: a corporate cut-out who will take a "
            "message, or a handler with the authority to bless a joint operation. The Wyndham "
            "Crossroads is likewise unstatted."
        ),
        "contact_skills": [
            "Yamatetsu covert operations in the metroplex",
            "Corporate introductions to deniable units",
        ],
    },
    {
        "name": "Knight Errant Security Guard (Griffin Biotechnology)",
        "role": "The average two-year veteran on the Griffin detail -- professional, wired, all but immune to fast talk, bribes or intimidation",
        "archetype": "Corporate Security Guard",
        "title": "Security guard, Knight Errant detail, Griffin Biotechnology Everett facility",
        "organization": "Knight Errant Security Services",
        "connection": 2,
        "description": (
            "The standard body in the standard grey armor with the KE logo the runners meet at every "
            "turn of the third act. Guards on external posts wear light security armor with matching "
            "helmets and low-light amplifiers; guards inside wear only secure ultra-vests and secure "
            "clothing -- their Knight Errant uniforms -- and carry a stun baton, a pistol and a "
            "flashlight. All the equipment is Ares brand, of course. They are confident in their "
            "ability to handle any situation and know they are backed up by elite warriors and powerful "
            "mages; they use military tactics and strategy and will fight until told to pull out or "
            "stand down by a recognized authority."
        ),
        "background": (
            "Griffin hires out its entire guard force to Knight Errant, which fills every security "
            "function at the facility except the Security Director's post, held by a Griffin employee. "
            "Every guard serving here has been with the company at least two years and has combat "
            "experience; most have seen action against shadowrunners at other major facilities. Four "
            "shift teams -- Alpha, Bravo, Charlie and Delta -- rotate four days on, one off, four swing "
            "shifts (15:00-23:00), one off, four mid shifts (23:00-07:00), then three days off; the "
            "shift on three-day break can be recalled as reinforcements during heightened security, "
            "which it currently is."
        ),
        "notes": (
            "Stats: B5 Q6 S6 C3 I5 W5, Ess 0.9, Reaction 5(9), Init 5+1D6 [9+3D6], Karma TR, Combat "
            "Pool 8, Pro 3/Trained. Cyber: smartlink, hearing damper, datajack, cybereyes (flare "
            "compensation, rangefinder, thermographic), headware radio with Commlink-IV and Crypto-3, "
            "Wired Reflexes 2. Assault Rifles 3, Pistols 5, Unarmed 3, Armed Combat (Club) 2(4), "
            "Throwing Weapons 4, Launch Weapons (Launchers) 2(4), SMG 5, Athletics 3, Stealth 4, "
            "Etiquette 2, Intimidation 4, Interrogation 4, Electronics 3; KE Operational Procedures 4, "
            "Security Procedures 4, Shadowrunner Tactics 3. Light security armor with helmet 7/6; Ares "
            "Predator II (7M Stun, gel -- the shared gear list prints 9M), Ares Ravener SMG (7M APDS, "
            "same as HK-227), AZ-150 stun baton (8S Stun), two flash-bang grenades (12S Stun, flash), "
            "security passcard, flashlight. +4 to any target number for fast talk, bribery or "
            "intimidation. Roaming guards patrol in pairs in assigned areas and report by radio every "
            "ten minutes, sometimes checking in through a camera's audio-visual pickup instead, which "
            "doubles as a test of the pattern recognition software; 15-minute breaks every three hours, "
            "staggered meal breaks splitting the lunch hour, shift change covering the half hour around "
            "the hour. On an alarm all internal guards report to the armory and refit into light "
            "security armor and heavier weapons as directed: Ares Alpha assault rifles, Ares MP-LMG, "
            "Ares Raptor rocket launchers, with APDS standard in rifles and heavier weapons. High-alert "
            "shift strength is 39: one shift commander and corporate liaison, two at the main gate, "
            "four in the control room, two in the main lobby, six on each of the three levels, and two "
            "plus a K-9 team in each of four exterior quadrants."
        ),
    },
    {
        "name": "Knight Errant K-9 Handler (Griffin Biotechnology)",
        "role": "A standard guard with a barghest on the leash -- four handler teams on constant duty for the duration of the alert",
        "archetype": "Corporate Security Guard",
        "title": "K-9 handler, Knight Errant detail, Griffin Biotechnology Everett facility",
        "organization": "Knight Errant Security Services",
        "connection": 2,
        "description": (
            "One of the four handlers Knight Errant stabled at the facility when the alert went up, "
            "walking an exterior quadrant with two ordinary guards and one very unordinary animal. In "
            "the simulation the barghests travel with their handlers, which is how the runners already "
            "know they are out there. He looks and fights exactly like every other guard on the "
            "detail; the difference is that he is the reason astral concealment and physical stealth "
            "both stop working in his quadrant at the same time."
        ),
        "background": (
            "Knight Errant provides magical security for the building and grounds under its contract "
            "with Griffin. Because of the current heightened state of alert it has stabled four K-9 "
            "handlers with barghests on constant duty, on top of the magician posted in the control "
            "room with watchers and low-level spirits combing the site inside and out. The player-issue "
            "Security Report, written before the alert, tells the runners flatly that no spirits or "
            "watchers monitor the building -- one of several places where the briefing they carry is "
            "out of date."
        ),
        "notes": (
            "Stats as the standard Knight Errant security guard (B5 Q6 S6 C3 I5 W5, Ess 0.9, Reaction "
            "5(9), Init 5+1D6 [9+3D6], Combat Pool 8, Pro 3/Trained, light security armor 7/6, Ares "
            "Predator II, Ares Ravener SMG, AZ-150 stun baton, two flash-bangs) with the addition of "
            "Animal Handling 4. Deployment: one K-9 team plus two guards in each of the four exterior "
            "quadrants during a high-alert shift. The handler is what turns the barghest from a hazard "
            "into a weapon -- it has been trained to follow his commands including the use of its "
            "powers, which is why it carries a Professional Rating at all."
        ),
    },
    {
        "name": "Barghest (Knight Errant K-9)",
        "role": "Dual-natured black mastiff with sonar, Fear and a Paralyzing Howl, walking the Griffin perimeter with its handler",
        "archetype": "Paracritter",
        "title": "Trained barghest, Knight Errant K-9 detail, Griffin Biotechnology",
        "race": "Barghest",
        "organization": "Knight Errant Security Services",
        "connection": 1,
        "description": (
            "An oversized solid black mastiff. Its short fur lies flat on its body, creating the "
            "impression that its hide is naked, with spines protruding the length of its back. Its eyes "
            "shine red and its teeth glow slightly in the dark because of luminescent bacteria in its "
            "saliva. It is a dual natured being and can use its senses and its powers on the astral "
            "plane, which makes it the single most effective counter on the grounds to an astrally "
            "projecting or magically concealed intruder."
        ),
        "background": (
            "Four barghests with their handlers were stabled at the Everett facility on constant duty "
            "when Knight Errant raised the alert level after the runners' failed first attempt. Each "
            "has been trained to follow the commands of its handler, including the use of its powers -- "
            "which is why the book assigns it a Professional Rating in the first place. In the simsense "
            "reconstruction at the Tacoma site the barghests travel with their K-9 handlers, so the "
            "runners have already met them a dozen times in a place where dying did not count."
        ),
        "notes": (
            "Stats: B7 Q6x4 S5 C- I3/6 W3, Ess 6Z, Reaction 6, Init 6+2D6, Pro 3/Trained. Attacks 9S. "
            "Powers: Enhanced Senses (Sonar), Fear, Paralyzing Howl. The howl requires an opposed "
            "Essence (Willpower) test; one net success results in paralysis. Dual natured, so it "
            "perceives and attacks on the astral plane as well as the physical -- invisibility, "
            "concealment and astral projection are all far less useful in its quadrant. Deployed one "
            "per exterior quadrant with a handler and two guards throughout the high-alert shift."
        ),
    },
    {
        "name": "Knight Errant Security Mage (Griffin Biotechnology)",
        "role": "Grade 3 initiate posted in the Griffin control room with quickened reflexes, three elementals and three watchers combing the site",
        "archetype": "Corporate Mage",
        "title": "Security magician, Knight Errant detail, Griffin Biotechnology Everett facility",
        "organization": "Knight Errant Security Services",
        "connection": 3,
        "description": (
            "The magician Knight Errant posted on site for the duration of the alert, working out of "
            "the control room in full heavy security armor with an EnviroSeal and fire resistance, an "
            "Ares Alpha across his knees and a pocket secretary in his hand. He does not patrol. He "
            "sits at the center of the sensor picture with watchers and low-level spirits combing the "
            "facility inside and out for evidence of astral intrusion, spell use or other unauthorized "
            "magical activity, and when something happens he sends elementals to it and, if the "
            "supervisor needs a picture, materializes in front of him to deliver the latest "
            "intelligence in person."
        ),
        "background": (
            "Griffin's own astral defences are architectural -- Force 8 wards, walls full of pressurised "
            "Fat Bacteria, biofiber linings, a residual Background Count of 1 from the magic used in "
            "construction. What the corporation contracted Knight Errant for is the active half: "
            "magical security for the building and its grounds. The player-issue Security Report, "
            "written before the alert, still tells the runners that no spirits or watchers monitor the "
            "building, and a team that plans its astral approach on that document walks into a "
            "magician who has been waiting for exactly that."
        ),
        "notes": (
            "Stats: B4 Q6(8) S3 C5 I6 W6 Magic 9, Ess 6.0, Reaction 6, Init 6+1D6 (6+4D6), Combat Pool "
            "6, Spell Pool 8, Karma 4, Pro 3/Trained. Athletics 6, Sorcery 6 (Astral Combat 9), "
            "Etiquette 3 (Corporate 5), Pistols 7, Assault Rifles 6, Stealth 6, Conjuring 6, Unarmed 6; "
            "Security Procedures 5, Tactics 4, Magical Threats 4, English 5, Japanese 3, German 3. "
            "Initiate Grade 3: Quickening, Invoking, Shielding, with Increased Reflexes 3 and Increased "
            "Quickness 2 already quickened. Spells: Manabolt 5, Powerbolt 5, Stunball 5, Improved "
            "Invisibility 6, Trid Spectacle 6, Transform 5, Shapechange 5, Chaotic World 6, Heal 6, "
            "Silence 5, Oxygenate 4. Full heavy security armor with helmet 8/7, EnviroSeal, fire "
            "resistant (-4 to the Power of fire-based attacks); Ares Alpha Combat Gun (8M, smartlinked, "
            "grenade link, Recoil 2, APDS) with offensive air-timed mini-grenades (10S). Gear: pocket "
            "secretary, Rating 3 medkit. Bound spirits: Earth Elemental Force 2 (5 services), Earth "
            "Elemental Force 4 (3 services), Fire Elemental Force 4 (2 services), and three Force 1 "
            "watchers. On a disturbance the spirits split -- some to the incoming threat, some to hold "
            "the fort and guard the inner perimeter."
        ),
    },
    {
        "name": "Knight Errant SWAT Trooper",
        "role": "The elite squad that captured the runners in the first place and is being trained on them at the Tacoma site",
        "archetype": "Corporate Security Specialist",
        "title": "SWAT operator, Knight Errant Security Services",
        "organization": "Knight Errant Security Services",
        "connection": 3,
        "description": (
            "Full heavy security armor with helmet, EnviroSeal and fire resistance, an Ares Alpha with "
            "a grenade link and air-timed mini-grenades, alpha-grade wire through every limb. These are "
            "the people who took the runners alive on Thursday afternoon rather than killing them, "
            "because a live shadowrunner is a training asset. At the Tacoma compound they are either in "
            "a debriefing from that last mission or five minutes away from being fully kitted, "
            "depending on how the team got out of the simulation -- and if an alarm goes before those "
            "five minutes are up they come in armored vests instead."
        ),
        "background": (
            "Knight Errant has grown tired of the repeated attempts, some of them successful, to breach "
            "the security at the Everett firm, and took matters into its own hands: it created an "
            "artificial version of the facility to train its elite squad members in specific anti-runner "
            "tactics, and it needed subjects. The whiteboards in the simsense chamber record what the "
            "squads have been learning from the runners -- 'Randomize backup cycle', 'Auditory alarm at "
            "door opening?' -- which is to say the team's own tricks are being written into the "
            "procedures they will face on Friday night."
        ),
        "notes": (
            "Stats: B5 Q6(8) S6(8) C4 I4 W5, Ess 0.4, Reaction 6(11), Init 11+3D6, Karma TR+2, Combat "
            "Pool 8, Pro 4/Professional. Cyber (all alpha): smartlink, cyberears (hearing damper and "
            "amplification), datajack, cybereyes (flare compensation, rangefinder, thermographic), "
            "headware radio with Commlink-IV and Crypto-3, Wired Reflexes 2, Muscle Replacement 2. "
            "Bioware: enhanced articulation, orthoskin 3, trauma damper. Assault Rifles 7, Pistols 5, "
            "Unarmed 4, Armed Combat (Club) 2(4), Throwing 4, Heavy Weapons (Launchers) 2(4), SMG 5, "
            "Athletics 3, Stealth 4, Etiquette 2, Intimidation 4, Interrogation 4, Electronics 3, "
            "Leadership 4; KE Operational Procedures 6, Security Procedures 6, Shadowrunner Tactics 5. "
            "Full heavy security armor with helmet 8/7, EnviroSeal, fire resistant; Ares Alpha Combat "
            "Gun (8M, smartlinked, grenade link, Recoil 2, APDS) with offensive air-timed mini-grenades "
            "(10S). 2+TR present at the Tacoma compound. The shift supervisor at Griffin uses the same "
            "attribute line at Pro 3 with light security armor. Shared armory list for KE at either "
            "site: light security armor with helmet, Ares Predator II, Ares Ravener SMG, Ares Alpha, "
            "Ares MP-LMG (7S APDS), Ares Raptor rocket launcher (as the Aztech Lasher), Zapper static "
            "discharge rocket (16D blast -10/m, scatter 2D6, fence 1,250 nuyen), anti-vehicle rocket "
            "(16D blast -8/m, scatter 2D6, fence 1,000 nuyen), APDS in pistol, SMG and rifle calibres, "
            "and flash-bang grenades."
        ),
    },
    {
        "name": "Knight Errant Labtech (Tacoma Simsense Site)",
        "role": "The technicians running the illegal simsense training programme -- brainy pushovers between the runners and the alarm panel",
        "archetype": "Technician",
        "title": "Simsense research technician, Knight Errant Tacoma compound",
        "organization": "Knight Errant Security Services",
        "connection": 1,
        "description": (
            "White coats around a room full of ergonomic chairs, small machines and prepared IV drips, "
            "administering to bodies that are not supposed to be awake yet. When the runners come round "
            "they jerk back from the moving forms -- they had not expected the simulation to end this "
            "quickly -- and for a beat or two they simply stand there stunned, long enough for the smell "
            "of fear to reach anyone with enhanced scent as a sudden salty outbreak of sweat and panic. "
            "Then one of them makes a panicked move for the alarm panel. The polite version, for a team "
            "that beat the sim properly, is a technician saying 'Please converse amongst yourselves "
            "quietly, the training program will recommence in ten minutes.'"
        ),
        "background": (
            "Staff on a set of highly illegal tests in an anonymous Tacoma building, running captured "
            "shadowrunners through a simsense reconstruction of Griffin Biotech so Knight Errant squads "
            "can learn anti-runner tactics. Because shadowrunners have such highly variable resistance "
            "to drugs and toxins, the level of sedation is difficult to gauge; the techs expect the team "
            "to come out groggy and disoriented from the disconnection between mind and body and from "
            "the mixture of Laes and depressants in their bloodstream. The depressants have worn off. "
            "If the techs notice the characters do not seem groggy, they immediately call security to "
            "subdue them so they can be properly tranquilized."
        ),
        "notes": (
            "Stats: B2 Q3 S3 C6 I4 W2, Ess 5.3, Reaction 4, Init 4+1D6, Karma 1, Pro 2. Cyber: datajack "
            "and 150 Mp of memory. Computers 6, Electronics 6, Etiquette 3, Biotech 3; Computer "
            "Background 6, Physics 3. Number present is 1+TR, adjustable for the combat worthiness of "
            "the group. While quite brainy, they should be a pushover -- the security forces at the "
            "other end of that alarm panel are a very different story for a group of unarmed and "
            "unarmored shadowrunners, arriving in just under a minute. Best case is subduing them with "
            "a minimal amount of noise and using a palm on the biometric maglock. Their whiteboards are "
            "the runners' intelligence: cryptic commentary on the team's actions to date, including "
            "'Randomize backup cycle' and 'Auditory alarm at door opening?'"
        ),
    },
    {
        "name": "Yamatetsu Covert Ops Operative",
        "role": "One of five combat operators in black jumpsuits wiring Griffin's underground half to blow -- willing to ally, willing to double-cross",
        "archetype": "Corporate Wetwork Operative",
        "title": "Covert operations specialist, Yamatetsu Corporation (Seattle assignment)",
        "gender": "Male",
        "nationality": "Russian",
        "organization": "Yamatetsu Corporation",
        "connection": 4,
        "description": (
            "A team cloaked head to toe in black jumpsuits and armored vests, moving as one, in the "
            "middle of setting explosive charges when the runners round the corner -- and already in "
            "firing positions with SMGs at the ready by the time anyone speaks, because they heard the "
            "runners at the same moment the runners heard them. They have been trained to work together "
            "so tightly that it sometimes seems they are using a Battletac unit when they are not. They "
            "are quick to use any tactical opportunity they can spot, and so will not hesitate to work "
            "with the runners as long as their goals do not conflict."
        ),
        "background": (
            "Six of them -- five combat support personnel and one mage. They are extremely loyal to "
            "Yamatetsu and have been assigned to the Seattle office to undertake various sensitive "
            "missions; sometimes the company cannot even afford to trust something to shadowrunners. "
            "Legwork puts them out of Moscow, coming to North America only for something big, and "
            "remembers their last local job -- SRM 01-02 Strings Attached -- as work where they got "
            "'tangled up with some Rastafarian'. Their orders here have nothing to do with the "
            "prototype: demolish the half of the building currently underground and close the tunnel. "
            "They have already secured the back half and placed charges throughout the ventilation "
            "system and within various access panels for the FAB delivery system in the walls."
        ),
        "notes": (
            "Stats: B5 Q7(8) S6(7) C5 I5 W4, Ess 1.75, Reaction 6(12), Init 8+1D6 (12+3D6), Combat Pool "
            "8, Karma 3, Pro 4/Professional. Athletics 6, Biotech 3, Car 5, Etiquette 3 (Corporate 5), "
            "Pistols 7, Small Unit Tactics 4, SMG 6, Stealth 6, Throwing 6, Unarmed 6; Security "
            "Procedures 5, Tactics 4, Russian 5, Japanese 3, English 3. Cyber (all alpha): cybereyes "
            "(display link, flare compensation, low light), Muscle Replacement 1, Reaction Enhancers 2, "
            "Wired Reflexes 2 with trigger. Armor 7/4: black combat clothing (as a camo suit, 5/3) plus "
            "tactical vest (3/1) plus helmet (+1/+1). Weapons: HK-227s (7M), Narcojet pistol (6D Stun), "
            "flashpak. Gear: pocket secretary, Rating 3 medkit. In play: willing to form a short-term "
            "alliance, and if the runners are hostile and will not negotiate they will take every "
            "action to defend themselves. Choices made in Strings Attached may colour the reaction. "
            "Pushing the Envelope: if the runners have seemed unchallenged so far, the Yamatetsu team "
            "may double-cross them and take the prototype for their own upper management -- such a boon "
            "would improve the elite team's standing inside the corporation. Debugging note: right now "
            "the agendas line up, Yamatetsu shutting down Griffin's nanotechnology developments while "
            "the runners steal a bioware prototype."
        ),
    },
    {
        "name": "Yamatetsu Covert Ops Mage",
        "role": "Arcane support for the demolition team -- grade 3 initiate with anchoring, four elementals and a gold ring that keeps the squad invisible",
        "archetype": "Corporate Mage",
        "title": "Covert operations magician, Yamatetsu Corporation (Seattle assignment)",
        "gender": "Male",
        "nationality": "Russian",
        "organization": "Yamatetsu Corporation",
        "connection": 4,
        "description": (
            "The sixth member of the black-jumpsuited team, dressed identically to the other five and "
            "carrying the same HK-227 and narcojet pistol, distinguishable only by a gold ring. His job "
            "is not the fight: most of his time is spent covering the movements of the team so that "
            "they can move like shadows to their intended target and get out without being seen. He is "
            "ready to counter any magical threat and to provide the extra punch necessary in a fight, "
            "which is what he is doing if the runners open the conversation with gunfire instead of "
            "words."
        ),
        "background": (
            "Attached to a six-person unit Yamatetsu keeps for the work it cannot trust to "
            "shadowrunners, apparently good enough that the street believes they must be linked by "
            "magic rather than by a Battletac. Anchoring rather than Invoking is his third metamagic, "
            "which is the practical difference between him and his Knight Errant counterpart across the "
            "building: the gold ring carries an anchored Improved Invisibility, which is how six armed "
            "operators reached the underground level of a facility at maximum alert and had time to "
            "wire the ventilation and the FAB access panels before anyone noticed."
        ),
        "notes": (
            "Stats: B4 Q6(8) S3 C5 I6 W5 Magic 9, Ess 6, Reaction 6.0, Init 6+1D6 (6+4D6), Combat Pool "
            "6, Spell Pool 8, Karma 4, Pro 4/Professional. Athletics 6, Biotech 3, Sorcery 8, Etiquette "
            "3 (Corporate 5), Pistols 7, Small Unit Tactics 4, SMG 6, Stealth 6, Conjuring 6, Unarmed 6; "
            "Security Procedures 5, Tactics 4, Magical Threats 4, Russian 5, Japanese 3, English 3. "
            "Initiate Grade 3: Quickening, Anchoring, Shielding, with Increased Reflexes 3 and Increased "
            "Quickness 2 quickened. Spells: Manabolt 5, Powerbolt 5, Stunball 5, Improved Invisibility "
            "6, Trid Spectacle 6, Transform 5, Shapechange 5, Chaotic World 6, Heal 6, Silence 5, "
            "Oxygenate 4. Armor 7/4 as the rest of the team; HK-227s, narcojet pistol, flashpak, pocket "
            "secretary, Rating 3 medkit, gold ring with anchored Improved Invisibility. Bound spirits: "
            "Earth Elemental Force 5 (3 services), Earth Elemental Force 6 (2 services), Earth Elemental "
            "Force 6 (2 services), Fire Elemental Force 4 (4 services). Note that his Sorcery is 8 "
            "against the Knight Errant security mage's 6, and that between them these two are the "
            "adventure's only real magical opposition."
        ),
    },
]

ORG_UPDATES = {
    "Griffin Biotechnology": {
        "notes_append": (
            "SRM 01-08 Duplicity: the third and final Mission against the Everett facility, and the one "
            "that ends the company's quarter. Griffin is a new company that received a huge influx of "
            "cash from DocWagon and Ares; the money bought breakthrough research in mapping the motor "
            "centers of the brain and in tissue development, and numerous bioware and cybernetic "
            "spin-off technologies have been born from the work done at the new secured facility. THE "
            "PROTOTYPE: an unstable advancement in cloning research. Griffin has working prototypes of a "
            "system to very quickly grow custom cultured organs -- established technology grows "
            "'marker-free' generic organs, then when a patient needs a rapid transplant a genetic "
            "sample is taken and genetic modification techniques retag the generic organ with the "
            "appropriate markers for that patient. In theory the technique produces custom organs in "
            "hours instead of months. The research is at a functional stage for several organs but is "
            "not yet optimized: success rates hover around fifteen percent. This is the research that "
            "bought DocWagon's support, which is why Rose Croix wants it or wants it gone. Legwork "
            "(street doc, any corporate contact, any Everett contact, data broker, fixer or Mr. "
            "Johnson; Biotech, (Mega)corporate Security, Data Brokerage or Everett Corporations at TN "
            "4): a biotech firm with a new facility in Everett that every shadowrunner worth his salt "
            "has been through; security drones on patrol but no rigger on duty; no mages on duty but "
            "some spirits, and Yamatetsu has just brought in a team from Russia probably en route to "
            "Griffin; and at four or more, they are working on a major breakthrough in standard and "
            "cultured bioware. The Security Director's post is the one security function Knight Errant "
            "does not fill -- it is held by a Griffin employee, Rebecca Owls-Breath. Staff are "
            "scientists, lab technicians, administrative personnel, computer technicians, janitorial "
            "staff and maintenance; none except the Security Director has any combat or defense skills; "
            "normal workers are loyal and resist bribes unless overly generous, and if captured or "
            "detained they are instructed not to resist or endanger themselves but to cooperate and "
            "tell their captors enough to keep them at bay, then submit to a debriefing afterwards so "
            "changes can be made. AFTERMATH: Griffin Biotechnology plummets seven points on the news "
            "and sits in a tenuous position while it establishes how much damage was done to its "
            "microbiology and nanotechnology research labs."
        ),
        "enemies_add": ["Rose Croix"],
    },
    "Rose Croix": {
        "notes_append": (
            "SRM 01-08 Duplicity: the last daring push before the IPO. Walter Broward funded all three "
            "Griffin runs through the fixer Lyle Green -- FORCEd RECON for the layout 'in case the "
            "facility became important later', The Gambler for the standalone paydata, and now this. "
            "News of the prototype has forced his hand: he wants the Griffin prototype and the research "
            "that bought DocWagon's support, and if he cannot have it he wants to ensure it does not "
            "end up in DocWagon's hands, so he has arranged for a team to steal or destroy it. Unlike "
            "the previous two visits the runners are allowed to take the gloves off and make as much "
            "noise as they feel is necessary; property damage and the death of personnel are "
            "inconsequential. His timing is unknowingly synchronized with a Yamatetsu strike on the same "
            "building. Terms through Green: 3,000 + (3,000 x TR) per runner for bringing in the "
            "prototype and research, 1,800 + (1,800 x TR) for destroying them, half for delivering only "
            "one of the two. Aftermath, from the shadow gossip on the handout: 'Word has it that this is "
            "meant to be the nail in the coffin for Griffin Biotechnology before Rose Croix has their "
            "IPO' and 'What I'm really interested in is whether Broward got what he wanted -- this "
            "smacks of his heavy handed approach to running and business.' The noise is exactly the "
            "kind of attention that sets up SRM 01-09."
        ),
        "enemies_add": ["Griffin Biotechnology"],
    },
    "Knight Errant Security Services": {
        "notes_append": (
            "SRM 01-08 Duplicity: Knight Errant holds the Griffin Biotechnology guard contract and fills "
            "every security function at the Everett facility except the Security Director's post. Four "
            "shift teams -- Alpha, Bravo, Charlie and Delta -- work four days on, one off, four swing "
            "shifts (15:00-23:00) on, one off, four mid shifts (23:00-07:00), then three days off; the "
            "team on three-day break can be recalled during heightened security. A high-alert shift is "
            "39 guards: one shift commander and corporate liaison, two at the main gate, four in the "
            "control room, two in the main lobby, six on each of the three levels, and two guards plus "
            "one K-9 team in each of four exterior quadrants -- the player-issue Security Report gives "
            "the pre-alert baseline of 38 with a different distribution. Guards arrive in a combination "
            "of private vehicles and Ares Citymaster troop transports; the shift commander has an Ares "
            "corporate Ford Americar. THE ILLEGAL PART: Knight Errant has grown tired of the repeated "
            "attempts, some of them successful, to breach the Everett firm's security, and took matters "
            "into its own hands -- it captured a runner team with a SWAT squad, dosed them with Laes and "
            "depressants, and built an artificial simsense version of the facility at an inconspicuous "
            "building in southern Tacoma to train its elite squad members in specific anti-runner "
            "tactics. Captured runners are the training subjects; their gear is held in the site armory "
            "and shipped to Knight Errant HQ for inventory after forty-eight hours. Aftermath: KE stock "
            "drops a tenth of a point on the Griffin bombing, a minor tremor parent company Ares "
            "assures investors will be resolved before the end of the day, and all security personnel "
            "form up behind 'the Grey Wall of Silence common after tragedy strikes areas defended by the "
            "national leader in advanced commercial security'."
        ),
    },
    "Ares Macrotechnology": {
        "notes_append": (
            "SRM 01-08 Duplicity: Ares is one of the prime backers of Griffin's research breakthroughs "
            "alongside DocWagon, and supplied the entire security suite for the Everett facility at "
            "bargain prices. Every piece of Knight Errant equipment on site is Ares brand: light and "
            "heavy security armor, the Predator II, the Ravener SMG (the HK-227 by another name), the "
            "Alpha Combat Gun, the MP-LMG, the Raptor rocket launcher, the Citymaster troop transports "
            "and the corporate Ford Americar the shift commander drives. Ares also wrote both smart "
            "frames guarding the facility's networks: OperateIT (Rating 20, 1,416 Mp, fence 22,500 "
            "nuyen), which analyzes and routes every data packet on the communications network, and the "
            "Overwatch-VI smart core (Rating 20, 1,850 Mp, fence 25,000 nuyen), which watches every "
            "camera and sensor feed for changes and for looping or splicing. Ares owns Knight Errant, "
            "and holds private property adjoining the Griffin grounds on the aerial recon photo. The "
            "aftermath handout has 'volunteer efforts from the awakened members of Ares' Knight Errant "
            "security' digging through the salvage."
        ),
    },
    "DocWagon": {
        "notes_append": (
            "SRM 01-08 Duplicity: DocWagon is one of the two corporations whose cash built the Everett "
            "facility, and the reason Rose Croix wants the prototype destroyed if it cannot be stolen. "
            "The custom cultured-organ research -- generic marker-free organs retagged for a specific "
            "patient in hours rather than months -- is precisely what an emergency medical corporation "
            "with an emptied organ vault needs, and it is 'the research that bought the support of "
            "DocWagon'. When the facility burns, DocWagon emergency response vehicles fill the airspace "
            "over Everett and its ambulances fill the roads. The series of hits on Griffin has been "
            "irritating DocWagon, one of the firm's main investors, and Rose Croix has been linked to "
            "them -- which is what pushes DocWagon into ending the Seattle market war in SRM 01-09."
        ),
    },
    "Yamatetsu Corporation": {
        "notes_append": (
            "SRM 01-08 Duplicity: Yamatetsu runs its own strike on Griffin Biotechnology on the same "
            "night as Rose Croix, entirely by coincidence. The instrument is a six-person covert ops "
            "team -- five combat support personnel and one mage -- extremely loyal, assigned to the "
            "Seattle office for missions the company cannot even afford to trust to shadowrunners, and "
            "trained so tightly together that they look Battletac-linked when they are not. The same "
            "team appeared in SRM 01-02 Strings Attached, and choices made there colour how they treat "
            "the runners here. Their orders: demolish the half of the building that is currently "
            "underground and close the tunnel -- shutting down Griffin's nanotechnology developments. "
            "By the time the runners meet them they have secured the back half and placed charges "
            "throughout the ventilation system and within the FAB delivery system's wall access panels. "
            "Legwork (runner, corporate, Russian, data broker, fixer or Johnson contacts at TN 4): "
            "nobody wants to discuss them at zero successes; based out of Moscow, only in North America "
            "for something big; they did some work here a while back and tangled with some Rastafarian; "
            "so good they do not need Battletac; and at four, ask for a Mr. Tamagochi at the Wyndham "
            "Crossroads. Aftermath, from the handout: 'Did anyone notice the distinct absence of "
            "Yamatetsu -- their import team was crawling all over that facility for the last week and "
            "they weren't even a blip on the radar.'"
        ),
        "enemies_add": ["Griffin Biotechnology"],
    },
    "Mackie Construction": {
        "notes_append": (
            "SRM 01-08 Duplicity: the play aids confirm what made Mackie a target in SRM 00-03 FORCEd "
            "RECON. The basement floor plan carries the note that areas 15 through 18 -- the airlock and "
            "bridge to the Float Floor, the Float Floor itself, the microtech labs and cyberware "
            "assembly and prototyping, and the main nanotech lab -- appear ONLY on Mackie Construction "
            "files. The construction firm's drawings are the sole record that the deepest and most "
            "valuable part of Griffin Biotechnology exists at all, including the fact that the inner "
            "section floats above the foundation and is separated from the walls to minimize vibration "
            "and external effects, and that every hallway, wall, floor and ceiling on the level is "
            "rigged for FAB dispensers."
        ),
    },
    "Draco Foundation": {
        "notes_append": (
            "SRM 01-08 Duplicity: the Draco Foundation's Everett complex is item 3 on the aerial "
            "reconnaissance photo in the play aids, one of the properties adjoining the Griffin "
            "Biotechnology grounds along Marine Drive, between the Brackhaus estate and Universal "
            "Omnitech's private property. It takes no part in the adventure -- but a runner team "
            "approaching Griffin through the pine forest, or exfiltrating after an explosion that "
            "levels a wing, is moving across a very well-observed stretch of Everett coastline."
        ),
    },
    "Universal Omnitech": {
        "notes_append": (
            "SRM 01-08 Duplicity: Universal Omnitech private property is item 4 on the aerial "
            "reconnaissance photo, adjoining the Griffin Biotechnology grounds along Marine Drive "
            "between the Draco Foundation complex and Ares private property. Its presence in the "
            "neighbourhood is texture rather than plot -- but it puts a second biotechnology "
            "megacorporation next door to a firm about to be levelled over cloned-organ research, and "
            "the yellow property line on the photo is the only thing separating them."
        ),
    },
}

LOC_UPDATES = {
    "Griffin Biotechnology Everett Research Facility": {
        "notes_append": (
            "SRM 01-08 Duplicity -- HIGH ALERT. Over a month after the last successful penetration, and "
            "because of the runners' own failed attempt, every security measure is running at high "
            "alert status. Internal physical security: fire doors (Barrier 6) at the end of each hall "
            "and at every major intersection; external walls of natural cut stone (Barrier 16) and "
            "heavy Plexiglas (Barrier 8); opaque windows with a polycarbonate coating that adds +4 to "
            "all target numbers for laser microphones and other sonic intrusion devices; internal walls "
            "of normal drywall (Barrier 4) except in labs, clean rooms and other sensitive areas, where "
            "they are plascrete with reinforced rebar (Barrier 8). Two HVAC systems -- the main one for "
            "common areas, halls and offices, the secondary for labs and sensitive areas, fitted with "
            "an Airwall system (SOTA63 p.83) that sterilizes the airflow with UV light and special "
            "filters. Both have choke points and filtration fans preventing anything larger than Body 1 "
            "from using them as an entryway (small animals such as squirrels may fit through certain "
            "areas), and both carry the same MAD and chemical sensors as the doors. Power: three-phase "
            "with redundant crossover circuits, battery UPS covering all computer systems, internal "
            "security, laboratory equipment and emergency lighting for five minutes, and auxiliary "
            "generators good for six hours on essential systems -- a window for systematic shutdown "
            "and/or defense. Maglocks: external card reader plus numeric keypad, both Rating 8, active "
            "during non-business hours 19:00-08:00 and governed by access rosters; internal offices and "
            "low security areas Rating 6 keycard only; labs and high security areas Rating 8; the most "
            "secure areas including the subterranean labs and armory add retinal scan at Rating 10. "
            "Cameras inside are mounted in unobtrusive black ceiling globes (Perception 5 to spot) and "
            "rotate at major intersections and common areas for a full 360-degree view in 120-degree "
            "increments. Astral: Force 8 opaque wards on labs and research areas, walls collocated with "
            "security doors holding pressurised Fat Bacteria tanks for an astral breach (astral Reaction "
            "(8) to find while trying to pass through one), a second fluorescing release into the "
            "hallways to help security locate the intruder, and biofiber lining in the inner walls, "
            "floors and ceilings of sensitive work areas. Knight Errant provides the magical security: "
            "four K-9 handlers with barghests on constant duty and a magician posted in the control "
            "room with watchers and low-level spirits combing the facility inside and out. FLOOR PLANS "
            "(play aids): First floor -- main entrance, front lobby with stairs and main elevators, "
            "restrooms, basic labs, loading dock, snack machines, break area, administrative offices, "
            "demonstration labs, conference room and auditorium, two freight elevators, radiology labs, "
            "tissue culture labs, plus the main electrical closet, the security center, the Security "
            "Director's office, the armory and sprinkler control. Second floor -- main stairs with "
            "glass lobby and elevators, the first-floor hallway running into the hillside, two "
            "conference rooms, bio labs, computer center and administrator's office, Dr. Chantel's "
            "private lab and office (Dr. Indira Chontel), senior doctors' offices, restrooms, the "
            "Director's office, a bio lab, medical equipment storage, secure labs, telecom and "
            "electrical closets. Basement -- see the separate Float Floor row. Entry points: only the "
            "front doors, the loading dock and the emergency exits; two are guarded and the third is "
            "alarmed. AFTERMATH: explosions rip through the compound, demolishing one wing completely "
            "and blocking all routes for rescue teams; dozens of support personnel and security forces "
            "are killed; KSEA calls it a terrorist act and cites 'a combination of military grade "
            "firepower and eldritch flame'."
        ),
    },
    "Griffin Biotechnology Facility (Everett)": {
        "notes_append": (
            "SRM 01-08 Duplicity: NOTE -- this row and 'Griffin Biotechnology Everett Research Facility' "
            "(created by SRM 00-03 FORCEd RECON) are the same building under two names, a duplication "
            "introduced across specs rather than by the books. The full high-alert security write-up, "
            "the floor plans and the aftermath are appended to the FORCEd RECON row. In brief: this is "
            "the third and final Mission against the site. Griffin has working prototypes of a system "
            "for growing custom cultured organs -- the research that bought DocWagon's support -- and "
            "Rose Croix sends a team to steal it or destroy it. The facility is at high alert after the "
            "runners' own failed first attempt, thirty-nine guards to a shift, four barghest teams, a "
            "Knight Errant magician in the control room, and a Yamatetsu covert ops team already "
            "underground wiring the nanotech wing to blow. It does not survive the night intact."
        ),
    },
    "Dusty's Steak House": {
        "notes_append": (
            "SRM 01-08 Duplicity: the payoff scene, and a deliberate callback for anyone who played "
            "SRM 00-03 FORCEd RECON. Lyle Green asks the team to meet him at his favourite restaurant "
            "in Everett; the upscale steakhouse is closed, but the Maitre D is waiting behind a small "
            "podium and escorts them back to the table where 'Lovely Lyle' is sitting. A large smile "
            "spreads across his face as the insulated case changes hands: 'Please, sit down. It's my "
            "treat today.' The scent of fresh bread the runners had been studiously ignoring fills "
            "their senses and they realize it has been a long time since they had non-soy food, with "
            "supple leather under them and solid real oak under their hands. Lyle has heard about the "
            "demolition of the Griffin facility, credits it to the runners at his table, decides they "
            "exceeded his expectations in 'destroying any research data' by leveling the place, and is "
            "somewhat generous about it -- an expense he passes on to his employer. Debugging note: the "
            "restaurant being closed will not stop the Maitre D commenting on the attire and odor of "
            "shadowrunners who come straight from the run, particularly if they have gunshot wounds."
        ),
    },
    "Dante's Inferno": {
        "notes_append": (
            "SRM 01-08 Duplicity: the Wednesday 22:15 meet, on the seventh level. The pulsing bass "
            "resonates through the body even as the sea of body fragrance and perfume mixes with "
            "alcohol into the intoxicating tide of the mob mentality; everyone gyrates in time to the "
            "beat, primal and unchoreographed yet unified by the dance. Lyle Green waits pressed into a "
            "booth at the back, where the throng of people and the intense electromagnetic interference "
            "created by the sound equipment make even a shouted conversation almost impossible to "
            "overhear. 'I'm glad you're here. We need to talk about heading back into the lion's den.' "
            "The runners do not play this scene in sequence -- they play it as a flashback in the third "
            "scene of the adventure, triggered by a text message reading 'Call me, LG' after the Laes "
            "wears off."
        ),
    },
    "Brackhaus Estate": {
        "notes_append": (
            "SRM 01-08 Duplicity: item 2 on the aerial reconnaissance photograph in the play aids, one "
            "of the properties adjoining the Griffin Biotechnology grounds along Marine Drive, between "
            "Puget Sound and the Draco Foundation complex. NOTE: the photo caption reads 'Brackhaven "
            "Estate' where SRM 00-03 FORCEd RECON names the property for its owner, Hans Brackhaus -- "
            "one of the book's small inconsistencies, and an unusually loaded one given who "
            "Brackhaus is."
        ),
    },
    "Dohner Estate": {
        "notes_append": (
            "SRM 01-08 Duplicity: item 7 on the aerial reconnaissance photograph in the play aids, "
            "adjoining the Griffin Biotechnology grounds along Marine Drive between the Stuffer Shack "
            "and BP gas station and Griffin's own entry and guard shack. The yellow line on the photo "
            "marks the property border and the stone wall. It takes no part in the adventure, but it is "
            "the nearest civilian property to the entrance of a facility that is about to have "
            "explosions rip through it."
        ),
    },
    "Draco Foundation Everett Complex": {
        "notes_append": (
            "SRM 01-08 Duplicity: item 3 on the aerial reconnaissance photograph in the play aids, "
            "adjoining the Griffin Biotechnology grounds along Marine Drive between the Brackhaus "
            "estate and Universal Omnitech's private property. Named on the photo and nowhere else in "
            "the adventure -- but it means the Foundation has a complex within sight of a biotech firm "
            "that gets levelled in a night the media calls a terrorist attack."
        ),
    },
    "Marine Drive Stuffer Shack and BP Gas Station": {
        "notes_append": (
            "SRM 01-08 Duplicity: item 6 on the aerial reconnaissance photograph in the play aids, on "
            "Marine Drive between Ares private property and the Dohner estate, the last ordinary "
            "commercial premises before the turn onto 172nd Street. The closest exit from I-5 is Exit "
            "206. For a team staging an approach, it is the only place on the recon photo where a "
            "vehicle can sit without belonging to a megacorporation or a private estate."
        ),
    },
    "Mackie Construction Offices": {
        "notes_append": (
            "SRM 01-08 Duplicity: the play aids retroactively justify SRM 00-03 FORCEd RECON's interest "
            "in this office. The Griffin basement floor plan notes that areas 15 through 18 -- the "
            "airlock and bridge, the Float Floor, the microtech and cyberware prototyping labs, and the "
            "main nanotech lab -- appear ONLY on Mackie Construction files. Whatever the runners took "
            "out of here in the earlier Mission is the sole documentary evidence that the deepest part "
            "of Griffin Biotechnology exists, and the Yamatetsu team wiring that level tonight got "
            "there by one route or another."
        ),
    },
}

NPC_UPDATES = {
    "Lyle Green": {
        "notes_append": (
            "SRM 01-08 Duplicity: 'Lovely Lyle', the fixer and Mr. Johnson for all three Griffin runs, "
            "fronting for Rose Croix. Initial contact Wednesday 17:30; the meet Wednesday 22:15 on the "
            "seventh level of Dante's Inferno, pressed into a back booth where the crowd and the sound "
            "rig's electromagnetic interference make even a shouted conversation almost impossible to "
            "overhear: 'I'm glad you're here. We need to talk about heading back into the lion's den.' "
            "When the runners surface from the Tacoma compound with their memories still fogged by "
            "Laes, it is his text -- 'Call me, LG' -- that triggers the landslide of memory. TERMS: "
            "3,000 + (3,000 x TR) per team member to steal the prototype and all associated research; "
            "60 percent of that (1,800 + 1,800 x TR) if they can only destroy them; half if they "
            "deliver or destroy just one of the two. Forty-eight hours from the meet. He supplies a "
            "floor plan and security details of the facility, having been told that some of the runners "
            "have already been to the site once and that those should suffice to get them to the lab, "
            "and warns that the information predates their capture. For a team with no decker he can "
            "provide a stand-alone module with a smart-frame/agent: a black box with two connectors, a "
            "green cable carrying an agent loaded with browse utilities to grab the data, and a red "
            "cable that injects a cascading worm to corrupt and destroy everything on the host. He "
            "heard about the demolition before the team reached him, credits it to them, and is "
            "somewhat generous about it -- an expense he passes on to his employer. Payoff at Dusty's "
            "Steak House in Everett: 'Please, sit down. It's my treat today.'"
        ),
        "contact_skills_add": [
            "Rose Croix contracts and corporate sabotage work",
            "Stand-alone agent and worm modules for teams without a decker",
        ],
    },
    "Michael Davenport": {
        "notes_append": (
            "SRM 01-08 Duplicity: as Walter Broward, CEO of Rose Croix, he never appears on stage -- "
            "everything runs through the fixer Lyle Green -- but the whole adventure is his. He paid "
            "for SRM 00-03 FORCEd RECON to map the Griffin facility 'in case it became important "
            "later', paid for SRM 01-04 The Gambler to lift paydata from a standalone terminal without "
            "leaving traces, and now, with news of a prototype out, makes one last daring push: he "
            "wants the prototype and the research that bought DocWagon's support, and if he cannot have "
            "it he wants to ensure DocWagon does not. Unlike the previous two visits the gloves come "
            "off -- property damage and the death of personnel are explicitly inconsequential. His "
            "timing is unknowingly synchronized with a Yamatetsu strike on the same building on the "
            "same night. The shadow gossip afterwards reads him accurately: 'What I'm really interested "
            "in is whether Broward got what he wanted -- this smacks of his heavy handed approach to "
            "running and business. Don't get me wrong the nuyen is great, but sometimes the trouble "
            "isn't worth it.' And: 'Word has it that this is meant to be the nail in the coffin for "
            "Griffin Biotechnology before Rose Croix has their IPO.' The noise is what finally brings "
            "DocWagon down on him in SRM 01-09."
        ),
    },
    "Rebecca Owls-Breath": {
        "notes_append": (
            "SRM 01-08 Duplicity: Security Director of Griffin Biotechnology through the facility's "
            "worst night, and the one security post Knight Errant does not fill. She drives an "
            "Ares-issued Ford Americar, the same model given to the Knight Errant shift commander. "
            "STATS as printed here (the OCR of the book drops several ratings): B4(6) Q5(6) S5(6) C4 "
            "I4(6) W5, Ess 0.5, Reaction 5(14), Init 5(14)+1D6 (4D6), Karma TR+4, Combat Pool 9, Pro "
            "4/Professional. All cyberware DELTA grade: smartlink, hearing damper modification, "
            "datajack, Wired Reflexes 3, reaction enhancer, Muscle Replacement 1, dermal plating, "
            "encephalon 2, headware radio with Commlink-IV and Crypto-3, tactical computer 1. Bioware: "
            "cerebral booster 2, enhanced articulation. Skills: Assault Rifles 5, Shotguns 5, Unarmed "
            "Combat (rating garbled), Athletics 3, Stealth 4, Etiquette 2, Intimidation (garbled), "
            "Electronics 3, Computers 3, Biotech 3; Security Procedures 6, Shadowrun Tactics (garbled). "
            "Armor jacket 5/3. Enfield AS-7 shotgun (Conc 3, Ammo 10(c), SA/BF, 8S) with internal "
            "smartgun system and four clips of slug ammunition, 2,000 nuyen value. AFTERMATH: she is "
            "the only person Knight Errant puts on the record, telling KSEA that Knight Errant is "
            "following up on every lead it has and confirming that several individuals did attempt to "
            "breach the facility in the pre-dawn hours prior to the attack but were turned over to "
            "local law enforcement officials for prosecution -- a statement she is in no position to "
            "know is false, since those individuals were in a Knight Errant simsense rig in Tacoma. All "
            "other security personnel form up behind 'the Grey Wall of Silence'."
        ),
    },
    "Dr. Indira Chontel": {
        "notes_append": (
            "SRM 01-08 Duplicity: the Griffin second-floor map in the play aids gives her a private lab "
            "(room 6) and her own office (room 7), the only researcher on any of the three floor plans "
            "to be named -- the map labels both 'Dr. Chantel's', spelling her surname differently from "
            "SRM 00-03 FORCEd RECON. Her rooms sit between the computer center and administrator's "
            "office on one side and the senior doctors' offices on the other, on the floor where the "
            "hallway runs into the hillside. She takes no part in the adventure's scenes and is not "
            "mentioned in the text at all, but the microbiology lab the runners are sent to raid and "
            "the tissue culture and radiology labs on the first floor are the working end of the "
            "research she leads -- and one wing of the building does not survive the night."
        ),
    },
    "Knight Errant Shift Supervisor (Griffin Everett)": {
        "notes_append": (
            "SRM 01-08 Duplicity: the shift commander and corporate liaison, one per shift, running a "
            "39-guard high-alert roster from the control room. STATS: B5 Q6(8) S6(8) C4 I4 W5, Ess 0.4, "
            "Reaction 6(11), Init 11+3D6, Karma TR+2, Combat Pool 8, Pro 3/Trained. Cyber (all alpha): "
            "smartlink, cyberears with hearing damper and amplification, datajack, cybereyes (flare "
            "compensation, rangefinder, thermographic), headware radio with Commlink-IV and Crypto-3, "
            "Wired Reflexes 2, Muscle Replacement 2. Bioware: enhanced articulation, orthoskin 3, "
            "trauma damper. Assault Rifles 7, Pistols 5, Unarmed 4, Armed Combat (Club) 2(4), Throwing "
            "4, Heavy Weapons (Launchers) 2(4), SMG 5, Athletics 3, Stealth 4, Etiquette 2, "
            "Intimidation 4, Interrogation 4, Electronics 3, Leadership 4; KE Operational Procedures 6, "
            "Security Procedures 6, Shadowrunner Tactics 5. Light security armor with helmet 7/6; Ares "
            "Predator II (7M Stun, gel), AZ-150 stun baton (8S Stun), Ares Ravener SMG (7M APDS), "
            "security passcard, flashlight. He drives an Ares corporate Ford Americar. DOCTRINE: when a "
            "ruckus is caused on the grounds he sends the closest team to investigate while bringing the "
            "area's sensors into play, announces the disturbance as appropriate and deploys the rest as "
            "required. Protecting the facility and containing the breach is the goal, not engaging "
            "unknown foes in a pitched battle -- he will do exactly what the runners are doing, staying "
            "back and observing via sensors, the first wave of guards and other sources, then use that "
            "picture to formulate a defense and feed it to the Knight Errant forces en route. An astral "
            "mage or two scouts and materializes in front of him with the latest intelligence. Once the "
            "support teams arrive the facility locks down and the goal becomes containment: keep the "
            "runners fighting, redeploy, wait for backup. A team that grabs what it came for and leaves "
            "stands a good chance of getting away; a team that holds ground or pushes deeper will "
            "probably be captured, injured or killed."
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
Six systems, in two clusters. Neither Tacoma host is sculpted, and because the decker is coming in
from an internal jackpoint at that site the security is toned down.

### Knight Errant Tacoma -- primary host

Orange-7/14/15/12/13/13. Controls all security measures and negotiates the connection to the outside
world through a vanishing SAN and one-way data flows.

| Step | Event |
| --- | --- |
| 4 | Probe-5 |
| 8 | Probe-7 |
| 12 | Passive Alert, Trace-9 |
| 16 | Blaster-8 |
| 20 | Active Alert |
| 24 | Shutdown |

### Knight Errant Tacoma -- secondary data host

Green-5/9/9/8/9/9.

| Trigger Step | Event |
| --- | --- |
| 3 | Probe-4 |
| 7 | Tar Baby-6 |
| 12 | Probe-6, Tar Pit-6, Passive Alert |
| 18 | Probe-6, Killer-6 |
| 25 | Tar Pit-6, Tar Pit-6, Killer-6 |
| 30 | Shutdown |

Paydata: **Personnel Files (250 Mp)**, protected with scramble-6 -- the current listing of all Knight
Errant personnel at the Griffin Biotech facility including training profiles and serial numbers,
annotated with the gear assigned on a standard basis and the additional gear each guard is qualified
to use. Worth 7,500 nuyen to the right fixer or fence. This host is also where a team decker can
insert false data for transmission to the Everett host -- which, combined with stolen KE uniforms
from the armory, is the book's suggested alternative to fighting through Griffin's front gate. If
the facility alert is triggered by an alarm panel or by security hearing the fray, both Tacoma hosts
go to active alert.

### Griffin Biotechnology -- communications network

Green-8/8/14/10/15/11. No paydata. The only system directly connected to the Matrix, via a standard
SAN. Houses the public corporate site, email and telecom connections, and the pattern recognition
and control software that analyzes and routes data packets by content. All inbound streams are
inspected; telecom signals pass to their recipients on the main network, email is retained in data
storage. Any traffic trying to pass through to the main network via the internal SAN is analyzed for
viruses, smart frames, persona programs and other illegal datastreams -- a decker must evade the
program's Sensor rating and then the node's Access rating.

| Trigger Step | Event |
| --- | --- |
| 5 | Probe-8 |
| 10 | Probe-10, Tar Baby-10 |
| 15 | Tar Pit-10, Passive Alert |
| 20 | Mark-Rip-12, Tar Pit-12 |
| 24 | Sparky-12, Active Alert |
| 28 | Shutdown |

**OperateIT (application smart frame, programmed by Ares).** Smart Core Rating 20, Size 1,416 Mp.
B 5, E 0, M 0, S 15, R 20, I 3D6. Programs: Analyze 6, Commlink 6, Read/Write 6. Options: DINAB-8.
Fence value 22,500 nuyen. Uses Analyze to detect anomalies (deckers, illegal programs) in any data
packet travelling in or through the system; uses Read/Write to send error and alarm messages to the
security consoles and to delete or edit files with illegal attachments or viruses; Commlink routes
all telecom traffic and inspects the signal for monitoring or tampering.

### Griffin Biotechnology -- logistics network

Green-8/8/15/8/8/15. No paydata. Same trigger table as the communications network. The facility's
nerve center for non-security automation: housekeeping and gardening drones, HVAC control, lighting,
elevator control, fire suppression, sprinklers and the PANICBUTTON system. Its link to the
communications network is one-way outbound and dedicated to PANICBUTTON reaching the Matrix to
notify the authorities -- and it runs on a dead man's switch, constantly transmitting status update
packets. Shutting down either the communications or the logistics network cuts that feed and
immediately triggers an alarm, unless a clever decker can somehow spoof the outbound data. The
security network has override control over most of this network's functions.

### Griffin Biotechnology -- main network

Orange-10/12/15/12/12/15. Handles all processing for the labs, offices and research areas. Not
connected to the Matrix directly, though research data and reports can be routed through the
communications network -- reaching it from outside means decking through two SANs, the second of
which only admits communications packets and standard packets directly requested by an internal
user. Deckers can obtain data files, all in the biomedical field, worth up to a combined maximum of
**100,000 nuyen**.

| Trigger Step | Event |
| --- | --- |
| 3 | Probe-8 |
| 6 | Probe-10, Tar Baby-10 |
| 10 | Tar Pit-10, Passive Alert |
| 13 | Mark-Rip-12, Tar Pit-12 |
| 17 | Sparky-12, Active Alert |
| 20 | Shutdown |

### Griffin Biotechnology -- security network

Red-8/15/12/10/12/15. No paydata. Controls all security-specific hardware inside and out and can
override the logistics network. This is the system the external dataline tap reaches -- from inside
it, runners can modify the biometrics database, pull guard schedules and more.

| Trigger Step | Event |
| --- | --- |
| 3 | Probe-8 |
| 5 | Probe-10, Tar Baby-10 |
| 8 | Tar Pit-10, Passive Alert |
| 10 | Mark-Rip-12, Tar Pit-12 |
| 12 | Sparky-12, Active Alert |
| 15 | Shutdown |

**Overwatch-VI Smart Core (programmed by Ares).** Rating 20, Size 1,850 Mp. B 5, E 0, M 0, S 15,
R 20, I 6D6. Programs: Analyze 10, Read/Write 5. Options: DINAB-8. Fence value 25,000 nuyen. Monitors
input from Matrix-wired cameras and sensors for differences from normal states, using its Analyze
rating as a Perception test with filters for waving branches, fans and similar false readings. On a
disparity it reroutes the camera's video feed to a primary monitor at a security station, creates a
log entry and sends a visual, audio and/or text alert. The same rating checks for attempts to modify
a camera's or sensor's signal, control or time code, which is what prevents looping and splicing.
Meant for a mainframe; a character who downloads it gets object code only, which cannot be modified,
but can be sold at the listed price.
"""

NOT_BUILT = """
- **The Shadowland posters on the aftermath handout** -- **Iblis**, **ConspiracyTheorist**,
  **Skeptic**, **HammerJack**, **Wingless Falcon**, **Deacon Blues** and **Spider**, arguing about
  whether Broward got what he wanted, why anyone would flatten a cash cow every runner in the
  metroplex had been through, and whether this is a smear campaign that will make Knight Errant and
  Lone Star harder on minor infringements. Handles on a board, not characters.
- **The Dusty's Maitre D** -- unnamed, waits behind a small podium in a closed restaurant and will
  comment on the attire, odor and gunshot wounds of anyone who comes straight from the run. Folded
  into the Dusty's Steak House update.
- **The Griffin shift commander and corporate liaison as an individual** -- the post is filled by
  the Knight Errant Shift Supervisor row created by SRM 00-03 FORCEd RECON and appended to here.
- **The four guards in the Tacoma guardroom, the astrally projecting mage who answers a Tacoma
  alarm, and the Rapid Response Team the guards are relying on** -- posts and stat-block references
  rather than people; folded into the Knight Errant Tacoma Compound notes.
- **The technician in the van** at Griffin -- there is none in this adventure; the equivalent role
  belongs to SRM 01-09.
- **KSEA** -- the news outlet carrying the "Innocents Slaughtered as Griffin Biotechnology Struck by
  Terrorist Attack" story; a byline-free masthead.
- **The stolen car** used for the failed first assault, and the runners' vehicles, which are "in a
  safe location of the players choosing" while they are in the simulation.
- **Ares, Enfield, HK, Leyland-Rover, GMC, Ford** -- manufacturer name-drops on gear and vehicles.
- **Universal Omnitech and Ares private property, Puget Sound** on the aerial recon photo -- captured
  in the org updates and the compound grounds notes.
"""

PLAY_NOTES = """
- The structure is unusual and the book flags it: the adventure begins in media res, inside a
  simulation, with the run already failed. Scenes one and two (Waking Up, Getting out of bed) are
  paced differently from a normal Mission, and scene three (Cold Shower) is a flashback to the meet
  the players never got to play. After that it proceeds traditionally.
- Ending the simulation properly -- reaching the Beta Clinic or passing the airlock toward the
  nanotech facility, or being defeated with everyone captured, knocked out or killed -- gives the
  better payoff: a chance to interact with the facility at high alert without the danger of horrific
  death, and an exit from the host with minimal personal damage. Jacking out is a Willpower test at
  TN 8 and 5S Stun to soak; otaku with the Neurofilter echo and deckers running ICCM on a cranial
  cyberdeck get TN 6 and 3M Stun. It is not advised but is offered for players who know the Matrix
  rules and want the shortcut.
- Anyone with Simsense Vertigo runs at full negatives inside the simulation, which is a strong hint
  that something is not right. A memory test at TN 6 recalls flashes of a lab and of the team
  debriefing each other after failing the mission.
- The sadistic option the book prints and then disclaims: do not mention that this is the fifth run
  through the encounter, and reveal what is going on only after inducing a total party kill. "Neither
  the campaign director nor the author assume any responsibility for what players might do to any GM
  who would pull such a nefarious stunt."
- The runners are unarmed and unarmored until the armory. Emphasize it. Security responds
  non-lethally at first with flash-bangs and gel and goes lethal only against deadly force.
- Minimal legwork by design -- three Missions have already covered this facility, and players get the
  same security briefings issued in FORCEd RECON and The Gambler. If a player has extra information
  in hard copy or from memory, let them use it.
- The high-alert assault is written as potentially a high-mortality encounter. Push the players to
  understand how deadly it is. Distractions mostly backfire: Knight Errant investigates with the
  nearest team, deploys the rest for containment rather than a pitched battle, and gets spirits,
  astral scouts and support teams on scene within minutes. The book's own suggestion for a team that
  did not take uniforms and insert false security data into the Tacoma host is a go-gang assaulting
  the front gate, or individuals spread along the perimeter with launch weapons.
- The Yamatetsu encounter is the pressure valve: either a godsend for a beaten and battered team or
  another batch of stiff opposition. Their agendas line up right now. Play the standoff -- both squads
  had already assumed firing positions before anyone spoke.
- Karma: retrieving or destroying the prototype 1, retrieving or destroying the research 1, escaping
  the lab without heavy casualties or alerting security 1; maximum 3 team plus 3 individual. The book
  notes explicitly that this mission has a great impact throughout corporate Seattle and that the
  runners' business ethics should be awarded in consequence.
- Debugging for a team that refuses to go back: emphasize the reputation hit for turning down a job
  mid-run and remind them they know the facility better now. If they still refuse, pack up -- no
  karma and a hit to their reputation score.
- Debriefing Log boxes: the prototype was extracted / destroyed / remained secure; the research data
  was extracted / destroyed / remained secure; Griffin Biotechnology was BOOM! / stealthfully
  infiltrated / unharmed in any way.
"""

# Load-time fix: SRM 01-01 folded its own Griffin location into the FORCEd RECON row before load, so the
# second Griffin target below never exists in production; the full write-up already goes to the 00-03 row.
LOC_UPDATES.pop("Griffin Biotechnology Facility (Everett)", None)
