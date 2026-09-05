# SRM 00-03 FORCEd Recon (FanPro/WizKids, 2004, SR3) -- campaign order #41. North Everett (the new
# Griffin Biotechnology research facility off Marine Drive), downtown Everett (Dusty's Steak House,
# Mackie Construction) and downtown Seattle (Huitzilopochtli Plaza, Club Penumbra).
# SETTING NOTE: Seattle, not Denver. The run is in north Everett "near the Salish border", and the
# only Denver reference is historical -- the area "used to belong to the Native Americans before
# the Treaty of Denver". Every location row is city "Seattle".
# Dating: no in-world date; 2064 as for the rest of Season 0. The facility's official opening is
# one week away, the Seattle University field-trip bus runs every Wednesday, and the module's own
# fiction refers back to SRM 00-02 ("Rumor even has it that he hired a group of runners to hit a
# DocWagon manufacturing facility so that Paladin could secure a lucrative supply contract with
# Seattle General").
# Book editing inconsistencies noted on the affected rows: the researcher is "Dr. Indira Chontel"
# on p.3 but the second-floor map key calls her rooms "Dr. Chantel's Private Lab" and "Dr.
# Chantel's Office"; Mackie Construction's owner is "Michael Mackie" in one sentence and "Robert
# Mackie" three sentences later; the aerial recon key labels the Saeder-Krupp executive's estate
# "Brackhaven Estate" while the text names the resident "Hans Brackhaus"; the module refers to
# "Seattle University" and "the various universities in the sprawl" where the world row is the
# University of Seattle; the company is "Griffin Biotechnology", "Griffin Biotechnologies" and
# "Griffin Biotech" in the same paragraphs; the guard write-up says the facility has "two floors
# and one basement level" while the drone-recon section speaks of "the two basement levels"; the
# Knight Errant guard block lists "Launch Weapons (Launchers)" and the shift supervisor "Heavy
# Weapons (Launchers)" for the same role; and the Delivery scenario cross-references a "Forced
# Entry" section that is actually titled Frontal Assault.
# Name collisions: the Club Penumbra bartender is filed as "Tommy (Club Penumbra)" because an
# unrelated Tommy already exists (Brainscan), and Mackie's co-owner is filed as "Vincent Ciarniello
# (Mackie Construction)" to keep him apart from the Everett Mafia don Vince Ciarniello (Mob War!),
# whose name he merely shares -- which is the whole point of the joke.
# Source text: docs/Adventures/text/SRM00-03A_FORCEdRECON.txt (31 pages) and
# docs/Adventures/text/SRM00-03B_FORCEd_RECON.txt (player aids, maps and forms, 19 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "SRM 00-03 FORCEd Recon"
ORDER = 41
SOURCE = "SRM00-03A_FORCEdRECON.pdf, pp. 3-31; SRM00-03B_FORCEd_RECON.pdf (Player Aids), pp. 3-19"
YEAR = "2064"

SYNOPSIS = """
"We have decided to make you an offer." Eight words from **DocWagon** turned **Griffin
Biotechnology** from another struggling small firm into one of the largest biomedical research
outfits in the metroplex. What bought them was **Dr. Indira Chontel**'s breakthrough: remapping the
damaged motor centers of the brain onto healthy tissue, using the signals from good tissue to
compensate for bad. It is a cure for epilepsy and a doorway into a generation of bioware and
cybernetic spin-offs. CEO **Dr. Sumihiro Asikawa** courted the majors and they came -- DocWagon
first with something close to a hundred million nuyen, then Ares Macrotechnology, Seattle
University, even UCAS Department of Defense grants.

The money bought a facility. Griffin quietly purchased every house and street at the end of 172nd
Street off Marine Drive in north Everett, tore them down and let the ground grow over. Armored
trucks brought men who cut a magical circle that a lithe elven woman doused out for them, and then
earth elementals pushed solid granite up out of the ground to make a four-meter wall. **Mackie
Construction** came in behind them with crews of orks and trolls, and the whole compound went up in
weeks. Ares, as a prime investor, handed **Knight Errant** the security contract at a steep
discount and supplied the technical suite at cost. The place is a week from opening: the labs are
being stocked, half the staff are still downtown at the leased offices in **Huitzilopochtli
Plaza**, the guard shifts are at fifty percent, and -- crucially -- the pressure pads, laser grids
and ultrasound arrays are installed but not yet online.

**Dr. Fredericks** of **Paladin Medical Technologies** has read a report from a man he knows only
as "Christof" and does not like it. Griffin is suddenly his only serious competition, and their
downtown offices sit inside an Aztechnology plaza across from the Pyramid, which makes them
effectively unrunnable. The new compound will not be fully operational for a while yet. So he calls
**Lyle Green** -- former child trid star, "Lovely Lyle", the most civilized of his intermediaries
-- and buys reconnaissance to be spent later.

Lyle takes the meet at **Dusty's Steak House** in downtown Everett over a beer, a salad and a real
steak, tells the team about ninjas, and makes them an unusual offer: name your own pay. One
thousand nuyen guaranteed for bringing back anything at all, and after that the fee scales with
what they deliver -- floor plans, cameras, sensors, drones, magical security, guard rosters and
uniforms, Matrix hosts and IC, personnel and badges, terrain. Poor, Fair, Good and Excellent are
worth 500, 1,000, 2,000 and 5,000 nuyen a category, and a perfect job across the board is 28,000.
"If you feel that you are getting in over your heads, you should pull out, and accept whatever
reward you have accomplished. You should not let greed drive you into something foolish."
"""

TIMELINE = """
- **Some years back** -- Griffin Biotechnology struggles along with the other small biomedical
  firms in the sprawl, leasing space in Aztechnology's Huitzilopochtli Plaza downtown.
- **Recently** -- Dr. Indira Chontel's neural remapping work turns into a genuine breakthrough;
  Asikawa courts investors and DocWagon transfers close to 100 million nuyen, followed by Ares
  Macrotechnology, Seattle University and UCAS DoD grants.
- **About two months ago** -- Griffin buys 172nd Street and every property around it in north
  Everett, demolishes the buildings and lets the land grow over. Paladin's man "Christof" watches
  armored trucks deliver a team that cuts a magical circle, an elven woman douse it, and earth
  elementals raise granite walls out of the ground.
- **The following weeks** -- Mackie Construction builds the compound with ork and troll crews and
  dwarven stonework, the elementals moving earth to speed it along. Ares supplies the security
  suite; Knight Errant takes the guard contract at a discount; the university lends thaumaturgic
  staff.
- **Now** -- construction is all but finished (only the security and electrical contractors are
  still on site), the labs are being stocked, staffing is about 50 percent per shift, the sensor
  grids and ultrasound arrays are installed but not connected, and the official opening is a week
  away. Mackie has moved on to designing Tuskers.
- **Day 0, evening** -- Tommy behind the bar at Club Penumbra passes the word, or a street contact
  catches a runner outside China Pete's noodle shack: Dusty's, Everett, six sharp, dress nice, no
  toys.
- **Day 1, 6 PM** -- the meet. Anyone who declines takes 500 nuyen on a beacon-carrying credstick
  and is followed home.
- **Days 1-7** -- legwork and reconnaissance in whatever combination the team chooses: government
  floor plans, Mackie Construction, construction-worker contacts, a drive-by, the delivery ruse,
  the Wednesday student bus, drones, astral scouting, interrogation.
- **Wrap** -- an upscale downtown club, Lyle in party clothes, the report read, the questions
  asked, and payment by category.
"""

ORGS = [
    {
        "name": "Griffin Biotechnology",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Huitzilopochtli Plaza, downtown Seattle; new research facility off 172nd Street, north Everett",
        "summary": "Formerly struggling biomedical firm catapulted into the front rank by a neural remapping breakthrough and a flood of investor cash.",
        "description": (
            "Until very recently Griffin Biotechnology was one of the small biomedical firms "
            "scraping along in the Seattle sprawl out of leased offices in Aztechnology's "
            "Huitzilopochtli Plaza, across from the Pyramid, with its security subcontracted "
            "through its Aztechnology landlords. Then Dr. Indira Chontel's work on using the "
            "signals from healthy brain tissue to compensate for the irregular signals of damaged "
            "tissue turned into real progress on epilepsy -- and, more valuably, into a whole "
            "family of bioware and cybernetic spin-off technologies. CEO Dr. Sumihiro Asikawa "
            "courted the majors for the capital to finish the neural research, and DocWagon led a "
            "field that came to include Ares Macrotechnology, Seattle University and UCAS "
            "Department of Defense grants. In the space of a few months Griffin has become one of "
            "the largest biomedical research and technology firms in the metroplex, bought out an "
            "entire neighbourhood in north Everett, and built a state-of-the-art research, "
            "manufacturing and clinical facility on it."
        ),
        "notes": (
            "Leadership: Dr. Sumihiro Asikawa (CEO), Dr. Indira Chontel (lead researcher, with her "
            "own private lab and office on the second floor), Rebecca Owls-Breath (Security "
            "Director -- the only security post not held by Knight Errant). Corporate posture: "
            "Griffin understands industrial espionage and has written policy around it. Staff are "
            "instructed not to resist capture but to cooperate and tell captors enough to keep them "
            "at bay, then report the compromise so the affected systems can be changed. Mid-level "
            "managers and above get Knight Errant resistance training (Interrogation [Resist "
            "Verbal] 1 [3]) and stall, misdirect and wait for rescue; those with a Professional "
            "Rating hold out under torture until wounded commensurately. Damage that heals "
            "naturally is tolerated; anything requiring cyber replacement or expensive healing "
            "earns the corporation's active wrath (Etiquette (Corporate) (4) to know this). Staff "
            "are encouraged onto public transport and car pools, though senior people still drive "
            "private vehicles between downtown and Everett and most carry a PanicButton that can be "
            "tracked by radio direction finding -- kidnap a VIP without isolating their gear and "
            "four Knight Errant response teams with close air support arrive shortly after. Griffin "
            "also paid the metroplex agencies to keep only partial floor plans on file. Recruiting: "
            "heavily at the sprawl's universities, especially Seattle University, for lab support "
            "and research posts in biotechnology, cybertechnology, traditional medicine and "
            "nanotechnology."
        ),
        "allies": ["DocWagon", "Ares Macrotechnology", "Knight Errant Security Services", "Aztechnology"],
        "enemies": ["Paladin Medical Technologies"],
    },
    {
        "name": "Mackie Construction",
        "org_type": "corporation",
        "tier": 2,
        "headquarters": "46th Street SE off Evergreen Way, downtown Everett, Seattle",
        "summary": "Prominent Everett construction firm that built the Griffin compound, wrongly rumored to be a Mafia operation.",
        "description": (
            "A large and very successful construction firm operating mainly in Everett, run by "
            "owner Michael Mackie with Vincent Ciarniello as business manager and financial "
            "officer. About twenty people work there: six architects, four administrative staff, "
            "and eight foremen and contractors specializing in electronics and data wiring, "
            "plumbing, HVAC, security systems and general construction, almost all human and almost "
            "all with minimal cyberware. The one metahuman on staff is Anthony Trenello, the ork "
            "ironworking foreman. The firm is widely rumored to be run by the Mafia, and the rumor "
            "is simply wrong: Ciarniello happens to share a name with Vince 'Numbers' Ciarniello, "
            "Don of the Everett faction of the Seattle Mafia, and the coincidence of a Ciarniello "
            "handling the money has won Mackie a good deal of business it never asked for. Michael "
            "Mackie is not inclined to correct anybody."
        ),
        "notes": (
            "Plot role: Mackie built the Griffin facility and holds the only complete set of plans "
            "in existence -- the full GM map, including the basement float floor, the microtech and "
            "nanotech labs, and the FAB dispensers, all of which appear on Mackie's files and "
            "nowhere else. Getting them is the single most valuable score in the module. The firm "
            "is all but finished with the Griffin project; only the security and electrical "
            "contractors are still on site, and everyone else is gearing up for the next job -- "
            "Tuskers, an ork and troll music venue for downtown Everett. Because of the heavy stone "
            "and steel, Mackie used a great deal of metahuman labor on the Griffin build: orks and "
            "trolls on the structure, dwarves on the underground work and the stone facing. Ork, "
            "troll and dwarf construction contacts will describe the construction and sketch a "
            "rough exterior floor plan at base target 6 (+2 for a human or elf worker, or any "
            "worker not from Everett). Security: two Pinkerton guards overnight; concrete block "
            "walls barrier 16; tinted, mirrored, privacy- and thermal-treated Plexiglas front "
            "(barrier 4, +4 TN to sonic, ultrasound or laser detection against interior targets); "
            "metal and metal-framed Plexiglas exterior doors barrier 8; rating 4 intrusion "
            "detection on windows and doors; rating 8 external maglocks with keycard and passcode "
            "tied to the PanicButton; rating 6 passcode-only maglocks on the two officers' doors "
            "and the computer room; cameras inside and out with low-light and thermographic imaging "
            "watched by a CompuEyes-III smart frame. Magical security is effectively nil -- "
            "Pinkerton supplies a mage case by case, who sends spirits ahead while an armed "
            "response team comes in by helicopter or tilt rotor."
        ),
        "allies": ["Pinkerton Security Services", "Griffin Biotechnology"],
    },
    {
        "name": "Pinkerton Security Services",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "UCAS; Seattle metroplex branch offices",
        "summary": "The oldest security firm in the UCAS, supplying Mackie Construction's night guards, night decker and on-call mage.",
        "description": (
            "Pinkerton Security Services is described in the module simply as the oldest security "
            "firm in the UCAS, and it sells the middle of the market: reliable contract guards, "
            "Matrix monitoring and an armed response capability, at a price a twenty-person "
            "construction firm can afford. For Mackie Construction it provides two guards on a "
            "seven-to-seven night shift, a decker who sweeps the client's system periodically after "
            "hours and reads the log files and security tallies for evidence of intrusion, and a "
            "magician available case by case rather than on station."
        ),
        "notes": (
            "Pinkerton guards (2, both human): B5 Q4 S4 C3 I4 W4, Ess 5.0, Reaction 4, Init 4+1D6, "
            "Combat Pool 6, Karma TR-1, Pro 3/Trained. Armed Combat (Baton) 4 (6), Pistol (Taser) 4 "
            "(6), Unarmed 4, Athletics 2, Stealth 3, Etiquette 3, Negotiation 3, Electronics 2, "
            "Computers 1, Biotech 2; Pinkerton Operational Procedures 4, Security Procedures 4, "
            "Pinkerton Personnel 3, Card Games 4. Datajack. Secure clothing 3/0. Defiance "
            "Super-Shock taser (10S Stun) and an AZ-150 stun baton (8S Stun) -- non-lethal only. "
            "Rating 1 transceiver with rating 2 broadcast encryption. Procedure: one on the "
            "reception desk watching the internal and external cameras, one patrolling the three "
            "floors and resting in the employee lounge or on the leather sofa in the president's "
            "office; they swap at about 1 AM. They will not go outside under any circumstances -- "
            "they call Pinkerton on the radio and Lone Star through the installed PanicButton. "
            "Magical response: a Pinkerton mage sends spirits ahead to assess while preparing a "
            "physical arrival, usually with an armed team by helicopter or tilt rotor."
        ),
        "allies": ["Mackie Construction", "Lone Star Security"],
    },
    {
        "name": "UCAS Department of Defense",
        "org_type": "government agency",
        "tier": 5,
        "headquarters": "Washington FDC, UCAS",
        "summary": "Federal defense department funding Griffin's neural research through grants, alongside DocWagon and Ares.",
        "description": (
            "The defense establishment of the United Canadian and American States, which among its "
            "other activities funds promising civilian research through grant programs. When Dr. "
            "Asikawa went looking for the capital to finish Griffin's neural remapping work, the "
            "Department of Defense was one of the bodies that came to the table -- through various "
            "grants rather than an equity stake, but with the same underlying interest as everyone "
            "else at the table: a technology that repairs damaged motor control has obvious "
            "applications a long way from epilepsy clinics."
        ),
        "notes": (
            "A named investor and nothing more in this module; the runners never touch it. It "
            "matters as context. Griffin's investor list is DocWagon, Ares Macrotechnology, Seattle "
            "University and the UCAS DoD, which is why the facility carries a security posture "
            "wildly out of proportion to a company that was small change a year ago, and why "
            "Paladin's plan is reconnaissance now and a run much later rather than a smash and "
            "grab. A GM extending the campaign has an obvious lever: federal money in a private lab "
            "means federal interest in who has been photographing its walls."
        ),
    },
]

LOCATIONS = [
    {
        "name": "Griffin Biotechnology Everett Research Facility",
        "location_type": "research lab",
        "city": "Seattle",
        "district": "North Everett (172nd Street off Marine Drive)",
        "security_level": "Corporate High Security",
        "controlling_org": "Griffin Biotechnology",
        "summary": "New hillside research, nanotech and clinical compound behind an elemental-raised granite wall; the target of the entire run.",
        "description": (
            "At the end of 172nd Street, which turns east off Marine Drive and rises over a small "
            "hill, closest exit 206 off the I-5, in a stretch of north Everett near the Salish "
            "border that was Native American land before the Treaty of Denver and was never "
            "overbuilt. Griffin bought every surrounding home and connecting street, tore the "
            "buildings down and let the ground grow over, so the whole area is theirs. The compound "
            "is built into the side of one hill and approached up the side of another, ringed by "
            "thick pine forest that nothing wider than a two-wheeler can pass through. A four-meter "
            "wall stands three meters back from the road, large sections of it solid granite pushed "
            "up out of the earth by elementals rather than laid by hand -- a Perception (5) test "
            "notices that it is not built so much as grown, and it rates barrier 24. Monowire runs "
            "along the top of the back and south walls (Perception (10), 10S). A heavy steel gate "
            "(barrier 18) just wide enough for a transport truck closes the opening, with a "
            "separate man-gate set into it (Perception (6)), a visitor intercom pedestal at car and "
            "truck height wired to the main computer, two wide-angle thermographic cameras "
            "(Perception (5)) in bulletproof shells, and a four-meter-square guard shack behind the "
            "wall built for four guards and currently holding two. The building itself is natural "
            "cut stone (barrier 16) and heavy opaque Plexiglas (barrier 8) with a polycarbonate "
            "vibration-damping coat; inside, drywall partitions (barrier 4) except in the labs and "
            "clean rooms, which are plascrete with rebar (barrier 8), and fire doors (barrier 6) at "
            "every hall end and major intersection. High-powered daylight halogens light the gate, "
            "the drive, the frontage and the parking area; inside is ordinary fluorescent light."
        ),
        "notes": (
            "Maps: compound, first floor, second floor and basement, SRM00-03B pp.8-13, with player "
            "and GM versions. FIRST FLOOR: main entrance, front lobby with stairs and main "
            "elevators, restrooms, basic labs, loading dock, snack machines, break area, "
            "administrative offices, demonstration labs, conference room/auditorium, two freight "
            "elevators, radiology labs, tissue culture labs, plus the main electrical closet, the "
            "security center, the Security Director's office, the armory and sprinkler control. "
            "SECOND FLOOR: glass lobby and elevators, a hallway running into the hillside, two "
            "conference rooms, bio labs, computer center and administrator's office, Dr. Chontel's "
            "private lab and office (the map key spells it 'Chantel'), senior doctors' offices, "
            "restrooms, the director's office, medical equipment storage, secure labs, telecom and "
            "electrical closets. BASEMENT: main stairwell, generators, general storage, "
            "maintenance, restrooms, secure labs, observation rooms, mechanical fabrication rooms, "
            "kitchen, a beta-clinic operating room, laundry, showers, a nurse's station and "
            "monitoring, recovery rooms -- and past an airlock and bridge, a float floor that hangs "
            "clear of the foundation and walls to kill vibration, carrying the microtech and "
            "cyberware prototyping labs and the main nanotech lab. Areas 15-18 of the basement "
            "appear ONLY on Mackie Construction's files. TECHNICAL: external maglocks (card reader "
            "plus numeric keypad, rating 8) active 7 PM to 8 AM; internal offices and low-security "
            "areas keycard rating 6; labs and high-security areas card plus keypad rating 8; "
            "subterranean labs, armory and sensitive rooms add retinal scan at rating 10. Cameras "
            "everywhere with 120-degree arcs, normal, low-light and thermographic vision, 5x "
            "variable zoom and normal-range audio pickup, in ballistic polymer covers proof against "
            "heavy pistol calibre; interior units rotate in 120-degree increments for full coverage "
            "and sit in unobtrusive black ceiling globes (Perception (5)); exterior units hide "
            "inside artificial trees and boulders (Perception (10), or (6) with thermographic "
            "vision, ultrasound or astral perception, since the fakes have no living aura). Sensor "
            "grids of pressure pads (triggering above 30 kg) and invisible UV laser grids strung "
            "between artificial trees, concealability 15 (6 astrally). Ultrasound sensors rating 6 "
            "close in. MAD and chemical sniffers at rating 10 in the door frames and hallway at the "
            "main entrance and the high-security areas, and around the HVAC intakes, scanning for "
            "weapons, cyberware, explosives, gunpowder and dangerous chemicals both in and out. "
            "THE CRITICAL GAP: the sensor grids and the ultrasound arrays are installed but NOT YET "
            "ONLINE. Only the cameras are live, security must monitor them manually, and the "
            "pattern-recognition software takes -4. A runner may well find a pressure pad and only "
            "then realize it is dead. HVAC: two systems, the secondary serving the labs fitted with "
            "an Airwall UV-and-filter sterilizer (SOTA63 p.83); both have choke points and fans "
            "that stop anything bigger than Body 1, and carry the same MAD and chemical sensors as "
            "the doors. POWER: three-phase with redundant crossovers, five minutes of UPS on "
            "computers, security, lab equipment and emergency lighting, then six hours of auxiliary "
            "generator -- enough to shut down or defend in an orderly way. MAGIC: no staff "
            "magicians, no watchers, no bound spirits. A residual Background Count of 1 pervades "
            "the whole interior and three meters either side of the wall from the construction "
            "magic. Force 8 opaque wards cover the labs and research areas; all three wings of the "
            "basement are warded past the main lobby. Certain walls are solid in astral space and "
            "sit collocated with security doors -- they hold pressurized Fat Bacteria tanks that "
            "spray the walls, floor, ceiling and doors on an astral breach, with a second "
            "fluorescing release into the hallways to help the guards find the intruder; an astral "
            "Reaction (8) test finds them, but only for a traveller who tries to pass through a "
            "wall rather than using the halls. Knight Errant sweeps the grounds with one handler "
            "and a barghest on one day of the week (roll 1D6, 1 = Monday, 6 = Saturday, never "
            "Sunday); a KE contact will sell the next patrol date for a minimum 2,000 nuyen bribe. "
            "On alert, four handlers and beasts plus an on-site mage with watchers and low-level "
            "spirits, and alerts last three days."
        ),
    },
    {
        "name": "Mackie Construction Offices",
        "location_type": "corporate facility",
        "city": "Seattle",
        "district": "Downtown Everett (46th Street SE off Evergreen Way)",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "Mackie Construction",
        "summary": "Three-storey block on 46th and Evergreen holding the only complete set of plans for the Griffin compound.",
        "description": (
            "A three-storey concrete block building on 46th Street SE just off Evergreen Way, close "
            "to Exit 192 off the I-5, built over a private home some time in the 2020s. The street "
            "frontage is large-pane Plexiglas, tinted and mirrored to throw back the sunlight, with "
            "big Plexiglas double doors centered on the first floor; the sides and rear have "
            "smaller windows in white-painted cement block. A large brown dumpster sits in the "
            "three-meter rear alley. The parking lot on the right holds about twenty-five cars "
            "under four tall lamp posts and is shared with the Starbucks on the north corner of "
            "46th and Evergreen; a row of pines on the left screens off a two-storey private home. "
            "Across the street on the south corner is a small strip mall with a hair salon, a "
            "Korean market and a cellular phone store."
        ),
        "notes": (
            "The single richest target in the module: Mackie holds the full GM map of the Griffin "
            "facility, including the basement float floor, the microtech and nanotech labs and the "
            "FAB dispensers, none of which appear on any government copy. The Matrix host is "
            "Orange-8/12/12/10/12/12 with the Griffin files encrypted behind Probe-12/Scramble-12 "
            "(see Matrix systems); everything else -- cameras, personnel files, schedules, contact "
            "lists -- runs against the normal rating. Staffing: about twenty by day; two Pinkerton "
            "guards from 7 PM to 7 AM, swapping desk and patrol duties around 1 AM, who will not "
            "step outside and instead radio Pinkerton and hit the PanicButton to Lone Star. The "
            "surroundings are deliberate GM material: the module suggests making the Korean market "
            "a Seoulpa ring front or running a protection racket through the block if the team "
            "needs distracting, challenging or misdirecting. Only the security and electrical "
            "contractors are still working the Griffin job; the rest of the firm is gearing up for "
            "Tuskers."
        ),
    },
    {
        "name": "Dusty's Steak House",
        "location_type": "restaurant",
        "city": "Seattle",
        "district": "Downtown Everett",
        "security_level": "Patrolled / Commercial",
        "summary": "One of the most upscale restaurants in the metroplex, where Lyle Green takes the meet over real steak.",
        "description": (
            "The smell of the oak wood fires nearly lifts a visitor by the nose and drags them "
            "inside. Dusty's is one of the most upscale establishments in Everett and in the "
            "metroplex as a whole -- real steak, from actual cows, with loaves of steaming hot "
            "bread -- and it is a highly unusual place to hold a shadow meet, because people in "
            "that line of business do not fit the surroundings. Large solid oak tables, "
            "leather-lined booths, attentive waitresses, and enough simsense stars, sports figures "
            "and VIPs at the other tables that the runners will recognize faces. The dress code and "
            "the door are enforced: anyone carrying a weapon or dressed wrong does not get in and "
            "has to be briefed by their teammates afterwards."
        ),
        "notes": (
            "The meet scene. Lyle Green sits with a pilsner and the remains of a large salad and "
            "waits; the steak arrives as the last runner does. Refreshments are pointedly on "
            "separate checks -- 'You may help yourself to the bread, if you wish' -- and the "
            "message is that the runners have not earned this room yet. Play up the other diners. "
            "Anyone who declines the job gets a certified credstick with 500 nuyen and a polite "
            "farewell; two large men who have had nothing but beer and bread get up and leave at "
            "the same time to make sure they stay quiet. If they talk anyway, the module is blunt: "
            "the character is removed from play, messily, unless they immediately ditch the "
            "credstick, which carries a locator beacon. For inexperienced players, substitute "
            "Deadly wounds and a lesson."
        ),
    },
    {
        "name": "Huitzilopochtli Plaza",
        "location_type": "commercial district",
        "city": "Seattle",
        "district": "Downtown",
        "security_level": "Corporate High Security",
        "controlling_org": "Aztechnology",
        "summary": "Aztechnology-owned plaza across from the Pyramid where Griffin still leases its downtown offices.",
        "description": (
            "A commercial plaza owned and operated by Aztechnology in downtown Seattle, standing "
            "across from the Aztechnology Pyramid itself. Griffin Biotechnology leases its "
            "corporate offices here and, as a tenant, subcontracts all of its security needs "
            "through its landlords -- which means running against Griffin's downtown operation "
            "means running against Aztechnology on Aztechnology's ground, in the shadow of the "
            "Pyramid. Most of Griffin's scientists and lab technicians are still working out of "
            "these offices while the Everett facility is stocked."
        ),
        "notes": (
            "The reason the adventure exists in the form it does. Paladin cannot buy a run against "
            "the downtown offices at any sane price -- 'It was difficult to hire even shadowrunners "
            "to attempt runs against such a target' -- so the new Everett compound, not yet fully "
            "operational, is the soft target. The old downtown network is still live and still "
            "holds the delivery schedules for the Everett move; a decker who can get at it (through "
            "Aztechnology security) has an alternative route to the one piece of information that "
            "makes the delivery-truck ruse workable. Senior staff commute between here and Everett "
            "in private vehicles, which is where they are easiest to intercept."
        ),
    },
    {
        "name": "Marine Drive Stuffer Shack and BP Gas Station",
        "location_type": "convenience store",
        "city": "Seattle",
        "district": "North Everett (Marine Drive)",
        "security_level": "Low Security",
        "summary": "Stuffer Shack and gas station a mile south of the Griffin gate; where Knight Errant dumps the people it drugs.",
        "description": (
            "A Stuffer Shack with a BP gas station attached, about a mile south of the end of 172nd "
            "Street on Marine Drive -- the nearest thing to a public amenity in a stretch of wooded "
            "Everett given over to estates, corporate think tanks and research compounds. It is "
            "item 6 on the aerial reconnaissance photograph, and it is where the Griffin gate "
            "guards tell anyone who stops with a problem to go, since they have standing orders not "
            "to involve themselves in a car accident, a flat tire, a medical emergency or anything "
            "else outside the wall."
        ),
        "notes": (
            "The module's designated soft landing. Runners hosed down with Gamma-Scopolamine by the "
            "black-van removal team, or captured after a botched approach, wake up in this parking "
            "lot -- stripped of anything illegal, security-grade, military-grade or used for "
            "surveillance, with ordinary vehicles towed there and anything armed or unusually "
            "modified confiscated to a Knight Errant facility instead. A runner captured after a "
            "frontal assault and interrogated is released here in nothing but their underwear. It "
            "is also the obvious staging point for a team watching the road, and the only place "
            "nearby to buy anything at all."
        ),
    },
    {
        "name": "Brackhaus Estate",
        "location_type": "penthouse",
        "city": "Seattle",
        "district": "North Everett (Marine Drive)",
        "security_level": "Corporate High Security",
        "summary": "Private estate of the Saeder-Krupp executive Hans Brackhaus, two properties down from the Griffin compound.",
        "description": (
            "One of the large private estates that replaced the old homes along the wooded stretch "
            "of Marine Drive in north Everett, and the residence of Hans Brackhaus, described by "
            "the module as a high-level executive of Saeder-Krupp. It is item 2 on the aerial "
            "reconnaissance photograph handed out after a successful high-altitude drone flight, "
            "sitting between Puget Sound and the Draco Foundation complex. Nothing else about it is "
            "described, which given the identity of the man reputed to use that name is probably "
            "for the best."
        ),
        "notes": (
            "The aerial photo key labels it 'Brackhaven Estate' while the text names the resident "
            "'Hans Brackhaus' -- flagged here as a book inconsistency, and worth keeping distinct "
            "from Seattle's Brackhaven political family. Play use: a team that wants an observation "
            "post overlooking Griffin will find that every neighbouring property belongs to "
            "somebody with the resources to object, and this is the one they should be most "
            "frightened of. Hans Brackhaus is a name long associated in the shadows with Lofwyr's "
            "personal business, which no Season 0 runner has any reason to know and every GM has "
            "reason to remember."
        ),
    },
    {
        "name": "Draco Foundation Everett Complex",
        "location_type": "corporate facility",
        "city": "Seattle",
        "district": "North Everett (Marine Drive)",
        "security_level": "Corporate High Security",
        "controlling_org": "Draco Foundation",
        "summary": "Draco Foundation facility on the same wooded stretch of Marine Drive, and an easy vehicle to hijack by mistake.",
        "description": (
            "A Draco Foundation complex among the estates and research facilities on Marine Drive "
            "in north Everett, item 3 on the aerial reconnaissance photograph. Like everything else "
            "in this part of the sprawl it sits behind trees on land that was never crowded, and "
            "like everything else in this part of the sprawl its traffic uses the same handful of "
            "highway exits as the Griffin compound."
        ),
        "notes": (
            "The specific hazard the module calls out: a team that decides to hijack 'a delivery "
            "truck' coming off the nearest exit rather than identifying a scheduled Griffin "
            "delivery may well stop a Draco Foundation vehicle, and many transports in this area "
            "run with security escorts. Any Griffin delivery carrying lab equipment or bio-material "
            "is certainly escorted too. Otherwise a neighbour and a piece of scene-setting -- and a "
            "reminder to the GM that this stretch of Everett is not a place to have a firefight."
        ),
    },
    {
        "name": "Tuskers",
        "location_type": "nightclub",
        "city": "Seattle",
        "district": "Downtown Everett",
        "security_level": "Patrolled / Commercial",
        "summary": "Ork and troll music venue under construction by Mackie, the firm's next project after the Griffin compound.",
        "description": (
            "A new nightclub being built for downtown Everett that will showcase ork and troll "
            "musical talent -- part of the wave of ork bands rediscovering (or marketing) their "
            "ancient heritage that has Club Penumbra's crowd arguing about whether orks have a "
            "Fourth World of their own the way the elves and the great dragons do. Most of Mackie "
            "Construction has already moved off the finished Griffin job and onto this one."
        ),
        "notes": (
            "Not visited in the module; it exists as the reason most of Mackie's staff are no "
            "longer thinking about Griffin, and as an obvious future venue for a campaign set in "
            "Everett. A team that wants to reach Mackie's people socially rather than breaking into "
            "the offices will find the foremen -- Anthony Trenello in particular, who works the "
            "meta labor and the union reps -- easier to meet on the Tuskers site than anywhere "
            "else."
        ),
    },
    {
        "name": "Dohner Estate",
        "location_type": "penthouse",
        "city": "Seattle",
        "district": "North Everett (Marine Drive)",
        "security_level": "Corporate Standard",
        "summary": "Private estate marked on the Griffin aerial reconnaissance photo; nothing else is said about it.",
        "description": (
            "Item 7 on the aerial reconnaissance photograph of the Griffin compound and its "
            "surroundings: another of the large private estates along Marine Drive in north "
            "Everett, on land that used to belong to the Native American nations before the Treaty "
            "of Denver and was never overbuilt. The module names it and says nothing else about it."
        ),
        "notes": (
            "A blank on the map and therefore useful. It is one of the properties adjoining the "
            "Griffin wall, which makes it a candidate for an observation post, an approach route "
            "through the pines, or -- if a GM wants it -- an owner with an opinion about the "
            "corporation that just bought and demolished the neighbourhood. Nothing in the module "
            "constrains what a GM makes of it."
        ),
    },
]

NPCS = [
    {
        "name": "Dr. Sumihiro Asikawa",
        "role": "CEO of Griffin Biotechnology, who turned Chontel's breakthrough into a hundred million nuyen of investment",
        "archetype": "Corporate Executive",
        "title": "Chief Executive Officer, Griffin Biotechnology",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Griffin Biotechnology",
        "connection": 4,
        "description": (
            "The man who heard eight words -- 'We have decided to make you an offer' -- and built a "
            "corporation out of them. Asikawa is not described physically in the module; what it "
            "shows is his method. Handed a genuine breakthrough by his lead researcher, he did not "
            "sell it, he courted: he went to the major players one after another looking for "
            "investment partners rather than a buyer, and kept enough of them interested at once "
            "that DocWagon had to lead a field rather than dictate to a supplicant."
        ),
        "background": (
            "Asikawa ran Griffin Biotechnology as one of the small firms struggling along in the "
            "Seattle sprawl out of leased space in Aztechnology's Huitzilopochtli Plaza. When Dr. "
            "Indira Chontel's neural remapping work matured he went looking for the capital to "
            "finish it and found DocWagon, Ares Macrotechnology, Seattle University and UCAS "
            "Department of Defense grants. The money bought land in north Everett, a facility "
            "designed around research, nanotech manufacturing and a clinic where test subjects "
            "could be monitored, and -- because Ares was a prime investor -- a Knight Errant "
            "security contract at a heavily discounted rate. Griffin has gone from struggling to "
            "one of the largest biomedical research and technology firms in the metroplex in "
            "months."
        ),
        "notes": (
            "No stat block; he never appears on screen and the runners are extremely unlikely to "
            "meet him. He matters as the explanation for the shape of the target: this is a small "
            "company wearing a megacorporation's security, bought with other people's money, "
            "staffed at fifty percent, with half its systems still unplugged. Everything the team "
            "finds is best understood as somebody spending an investor's budget faster than the "
            "organization can absorb it. Senior staff, Asikawa included, visit the new facility "
            "from time to time to oversee the move -- which puts him on the road between downtown "
            "and Everett in a private vehicle, protected but not invulnerable, for a GM who wants "
            "the module to escalate."
        ),
        "contact_skills": ["Biomedical corporate finance", "Seattle investor circles"],
    },
    {
        "name": "Dr. Indira Chontel",
        "role": "Griffin's lead researcher, whose neural remapping breakthrough is the reason for everything in this adventure",
        "archetype": "Scientist",
        "title": "Lead researcher, neural remapping, Griffin Biotechnology",
        "race": "Human",
        "gender": "Female",
        "organization": "Griffin Biotechnology",
        "connection": 3,
        "description": (
            "The module gives Dr. Chontel no physical description at all -- only her work and her "
            "footprint on the building. She has a private laboratory and a private office of her "
            "own on the second floor of the new facility, next to the bio labs and the senior "
            "doctors' offices, which in a compound this new says everything about her standing. "
            "The second-floor map key spells her name 'Dr. Chantel', one of the module's small "
            "editing slips."
        ),
        "background": (
            "With Dr. Chontel's help Griffin Biotech made dramatic progress in the treatment of "
            "epilepsy: using the signals from healthy brain tissue to compensate for the irregular "
            "signals of damaged tissue, remapping the damaged sections of the brain's motor centers "
            "onto healthy ones. The epilepsy application is what the press release will say. What "
            "brought DocWagon, Ares and the Department of Defense to the table is the family of "
            "bioware and cybernetic spin-off technologies that follows from it. DocWagon's roughly "
            "hundred-million-nuyen investment buys the rights after development, probably a year of "
            "final research and testing away."
        ),
        "notes": (
            "No stat block; not met during play unless a GM puts her there. She is the reason the "
            "adventure exists and the obvious target of the follow-up run Paladin is paying to make "
            "possible -- Fredericks is buying reconnaissance now precisely so that someone can "
            "appropriate her work later. Her private lab and office are on the warded second floor; "
            "the really sensitive work (the microtech, cyberware prototyping and main nanotech labs "
            "on the basement float floor) appears only on Mackie Construction's plans. Most of the "
            "scientists including, presumably, Chontel are still working downtown at Huitzilopochtli "
            "Plaza and only visit Everett to see their new space, which makes the commute the one "
            "place a determined team can reach her."
        ),
        "contact_skills": ["Neural remapping and epilepsy research", "Bioware and cybernetic spin-off technology"],
    },
    {
        "name": "Rebecca Owls-Breath",
        "role": "Griffin's Security Director, the only security post not held by Knight Errant, and a walking delta-grade weapon",
        "archetype": "Corporate Security Director",
        "title": "Security Director, Griffin Biotechnology Everett facility",
        "race": "Human",
        "gender": "Female",
        "organization": "Griffin Biotechnology",
        "connection": 4,
        "description": (
            "Griffin contracts every security function at the Everett facility to Knight Errant "
            "except this one: the Security Director is a Griffin employee, and she is carrying "
            "roughly a quarter of a million nuyen of delta-grade hardware inside her skin. Wired "
            "Reflexes 3, a reaction enhancer, muscle replacement, dermal plating, an encephalon, a "
            "tactical computer and an encrypted headware radio, on 0.6 Essence, behind an armor "
            "jacket and an Enfield AS-7. She currently drives an Ares-issued Ford Americar. Her "
            "knowledge skills are Security Procedures 6 and Shadowrun Tactics 5, and she has "
            "clearly been hired by people who expected shadowrunners."
        ),
        "background": (
            "Nothing of her history is given, and the name suggests a good deal the module does not "
            "say. What it does establish is her professionalism under pressure. Captured and "
            "questioned, she will cooperate exactly as Griffin policy demands: she will describe "
            "the guard routines, the computer systems and the internal and external security "
            "measures in full, and hand-draw seventy-five percent of the building from memory. Ask "
            "her for her password or passcode and she gives a duress code that trips a silent "
            "alarm. Only magical interrogation gets the real one."
        ),
        "notes": (
            "Stats: B4(6) Q5(6) S5(6) C4 I4(7) W5, Ess 0.6, Reaction 5(11), Init 5(11)+1D6 (4D6), "
            "Combat Pool 9, Karma TR+4, Pro 4/Professional. Assault Rifles 5, Shotguns 5, Unarmed "
            "6, Athletics 3, Stealth 4, Etiquette 2, Intimidation 4, Electronics 3, Computers 3, "
            "Biotech 3; Security Procedures 6, Shadowrun Tactics 5. ALL cyberware delta grade: "
            "smartlink, hearing damper, datajack, Wired Reflexes 3, reaction enhancer +2, muscle "
            "replacement 1, dermal plating 2, encephalon 2, headware radio with Comlink-IV and "
            "Crypto-3, tactical computer 1. Bioware: cerebral booster 2, enhanced articulation. "
            "Armor jacket 5/3, Enfield AS-7 with internal smartgun and four clips of slug. PLAY: "
            "she is the biggest prize and the biggest risk in the module. Her real password plus "
            "access to the main or security network yields one hundred percent of the floor plans "
            "-- the single largest payout available. Getting it means magical interrogation, "
            "because the duress code is what she gives up voluntarily and it sounds a silent alarm "
            "the moment it is used. She also personally interrogates any 'student' caught with "
            "contraband on the field trip, alongside the shift supervisor. In a straight fight with "
            "starting characters she wins."
        ),
        "contact_skills": ["Corporate security procedures", "Shadowrunner tactics"],
    },
    {
        "name": "Michael Mackie",
        "role": "Owner of Mackie Construction; very happy and very wealthy, and content to let the Mafia rumor run",
        "archetype": "Business Owner",
        "title": "Owner, Mackie Construction",
        "race": "Human",
        "gender": "Male",
        "organization": "Mackie Construction",
        "connection": 3,
        "description": (
            "The module describes him in one clause -- the firm's prominence and success 'makes "
            "Michael Mackie, the owner, very happy and very wealthy' -- and then leaves him alone. "
            "He runs a twenty-person firm out of a converted three-storey block on 46th and "
            "Evergreen with a leather sofa in the president's office that the night guard sleeps "
            "on, and he has just delivered a state-of-the-art corporate research compound in a few "
            "weeks flat with elemental assistance and metahuman crews."
        ),
        "background": (
            "Mackie Construction is widely rumored to be a Mafia operation. It is not. His business "
            "manager and financial officer, Vincent Ciarniello, simply happens to share a name with "
            "Vince 'Numbers' Ciarniello, Don of the Everett faction of the Seattle Mafia, and "
            "having a Ciarniello signing the cheques has brought the firm a steady trickle of "
            "clients who assume they know what they are buying. Mackie has never gone out of his "
            "way to correct anyone. The module calls him 'Robert Mackie' three sentences after "
            "naming him Michael, one of its small editing slips."
        ),
        "notes": (
            "No stat block. He is the gatekeeper for the module's biggest score: Mackie "
            "Construction holds the only complete plans of the Griffin facility in existence, "
            "including the basement float floor, the nanotech and microtech labs, and the FAB "
            "dispenser runs, none of which appear on any government copy. Those files sit on an "
            "Orange-8/12/12/10/12/12 host behind Probe-12/Scramble-12 IC. There is no reason a team "
            "cannot approach him socially instead -- he is a proud, wealthy, talkative contractor "
            "whose firm has just pulled off something impressive and is moving on to a nightclub, "
            "and the module offers no rule against a face simply admiring his work at length."
        ),
        "contact_skills": ["Everett construction industry", "Building plans and permits"],
    },
    {
        "name": "Vincent Ciarniello (Mackie Construction)",
        "role": "Mackie's business manager and part owner; the accidental source of the firm's Mafia reputation",
        "archetype": "Business Manager",
        "title": "Business manager and financial officer, Mackie Construction; co-owner",
        "race": "Human",
        "gender": "Male",
        "nationality": "UCAS",
        "organization": "Mackie Construction",
        "connection": 2,
        "description": (
            "One of the two major owners of Mackie Construction and the man who handles its money. "
            "The module gives him no description beyond his job and his name -- and his name is the "
            "point. He is not a mobster, he is an accountant with the wrong surname, and the "
            "coincidence has been quietly good for business for years."
        ),
        "background": (
            "Vincent Ciarniello shares a name with Vince 'Numbers' Ciarniello, Don of the Everett "
            "faction of the Seattle Mafia. That he is also the firm's business manager and "
            "financial officer -- the Ciarniello who does the numbers, at a construction company, "
            "in Everett -- does not help. People hire Mackie Construction because they think they "
            "know who they are dealing with, and the firm is very prominent and very successful in "
            "part because of it. The rumor is simply incorrect."
        ),
        "notes": (
            "Filed under a disambiguated name to keep him apart from the genuine Everett don Vince "
            "Ciarniello of the Ciarniello Family (Mob War!), who is a different man. No stat block. "
            "Play value: a team that investigates the Mafia rumor is chasing a red herring the "
            "module planted deliberately, and the time they burn on it is time not spent on the "
            "Griffin wall. A team that leans on him expecting a mobster will get an extremely "
            "frightened financial officer -- and, if they push it far enough that the real "
            "Ciarniellos hear their own name being thrown around Everett, a problem that outlasts "
            "the run."
        ),
        "contact_skills": ["Construction contracts and finance", "Everett business gossip"],
    },
    {
        "name": "Anthony Trenello",
        "role": "Mackie's ork ironworking foreman; the way in to the metahuman crews who actually built the Griffin compound",
        "archetype": "Foreman",
        "title": "Foreman, ironworking crews, Mackie Construction",
        "race": "Ork",
        "gender": "Male",
        "nationality": "UCAS",
        "organization": "Mackie Construction",
        "connection": 3,
        "description": (
            "The only metahuman on Mackie Construction's staff, an ork who has worked his way up "
            "through the firm on hard work and dedication, and -- being of Italian descent -- one "
            "more reason the Mafia rumor refuses to die. He runs the ironworking crews: girders, "
            "structural supports, the work that needs people strong enough to carry and place steel "
            "I-beams, which means hiring orks and trolls. He is well respected by the workers and "
            "works closely with the union representatives to keep meta problems off the site before "
            "they start."
        ),
        "background": (
            "Trenello was picked for the foreman's job precisely because the company needed "
            "somebody who could interface between an almost entirely human office and the "
            "metahuman labor the heavy work requires. He did the Griffin build with ork and troll "
            "crews on the structure and dwarven crews on the underground work and the stone facing "
            "of the front exterior -- which means his people, collectively, know how that building "
            "goes together better than anybody outside the security office."
        ),
        "notes": (
            "No stat block. The module names him specifically as the NPC that meta runners or "
            "runners with metahuman construction contacts will interact with, whether they are "
            "chasing information or posing as construction workers. Construction details and a "
            "rough hand-drawn exterior floor plan are available from ork, troll or dwarf "
            "construction-worker contacts at base target 6 with normal modifiers; a human or elf "
            "worker, or any worker not from the Everett area, adds +2 as a friend of a friend. "
            "Trenello himself is the shortest route to those crews, and he is currently splitting "
            "his attention between the last of Griffin and the start of the Tuskers job, where he "
            "is much easier to meet than in the office."
        ),
        "contact_skills": ["Metahuman construction crews", "Union representatives in Everett", "How the Griffin compound is built"],
    },
    {
        "name": "Tommy (Club Penumbra)",
        "role": "Elf bartender at Club Penumbra who passes Lyle Green's message to connected runners",
        "archetype": "Bartender",
        "title": "Bartender, Club Penumbra",
        "race": "Elf",
        "gender": "Male",
        "connection": 2,
        "description": (
            "An elf with a sense of flair who has really fit into the Penumbra scene, working the "
            "bar on a night when the place is hopping, the line outside is as long as ever, and "
            "everyone is arguing about the new wave of ork bands supposedly rediscovering their "
            "ancient heritage. His dry martinis are, in the words of one satisfied customer, simply "
            "excellent, and show a true understanding and artistry of mixology. He spots a regular "
            "at the rail, works his way over and greets them by name."
        ),
        "background": (
            "Tommy is the sort of bartender a fixer uses as a message drop: he knows the high "
            "society crowd by face, he can be tipped, and he passes things along accurately. When "
            "Lyle Green needs to reach a runner who moves in Penumbra's circles, he stops by "
            "earlier in the evening and leaves the word with Tommy -- 'Lovely Lyle. He said that if "
            "I saw you, I should tell you that he's got something interesting lined up.'"
        ),
        "notes": (
            "Filed as 'Tommy (Club Penumbra)' to keep him apart from the unrelated Tommy already in "
            "the world (Brainscan). No stat block. He delivers Player Handout 1: Dusty's Steak "
            "House up in Everett, tomorrow night, six sharp, dress nice and do not bring any toys, "
            "it is a classy place. The tip he gets is explicitly part drinks and part information, "
            "which is the module quietly teaching new players how a message drop works. Runners who "
            "do not travel in those circles get Player Handout 2 instead, from a street contact "
            "outside China Pete's."
        ),
        "contact_skills": ["Club Penumbra and the Seattle nightlife scene", "Messages and gossip from the high society crowd"],
    },
    {
        "name": "Hans Brackhaus",
        "role": "Saeder-Krupp executive whose private estate adjoins the Griffin compound",
        "archetype": "Corporate Executive",
        "title": "High-level executive, Saeder-Krupp Heavy Industries",
        "race": "Human",
        "gender": "Male",
        "nationality": "German",
        "organization": "Saeder-Krupp Heavy Industries",
        "connection": 5,
        "description": (
            "The module says only that runners curious enough to look at Griffin's neighbours will "
            "discover 'the private estate of Hans Brackhaus, a high level executive for "
            "Saeder-Krupp' among the residents of this stretch of Marine Drive. He is never seen "
            "and never described. The aerial reconnaissance key labels the property 'Brackhaven "
            "Estate', which is an editing slip rather than a second family."
        ),
        "background": (
            "Nothing is given, and nothing needs to be for a Season 0 table. The name has a long "
            "history in the shadows as the identity a certain German dragon wears when he wants to "
            "conduct business face to face, which is not something any starting runner has reason "
            "to know -- but a GM handing out that aerial photograph should know exactly what has "
            "just been drawn on the map three properties from the runners' target."
        ),
        "notes": (
            "No stat block; a neighbour and an atmosphere. Practical use: he is the reason a team "
            "should think very hard before setting up an observation post, launching a drone, or "
            "hijacking a truck anywhere along this stretch of Marine Drive, and the reason a GM has "
            "a perfectly legitimate escalation available if they do it badly. Treat any contact "
            "with the estate as a separate adventure, not an encounter."
        ),
        "contact_skills": ["Saeder-Krupp business", "Very high-level corporate introductions"],
    },
    {
        "name": "China Pete",
        "role": "Noodle-shack proprietor whose corner is where unconnected runners pick up the job",
        "archetype": "Street Vendor",
        "title": "Proprietor, China Pete's noodle shack",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": (
            "A wizened old man behind the counter of a little noodle shack on the corner, doling "
            "out bowls of steaming noodles and broth to the dozen or so people crowded around it. "
            "The smell is not all that great; the noodles are quite tasty, especially on a chilly "
            "morning. The shack is cheap enough that a runner between jobs with an empty fridge and "
            "the last of a certified credstick can eat there without thinking about it."
        ),
        "background": (
            "China Pete's is the sort of fixture a neighbourhood is organized around: everybody "
            "eats there, everybody can be found there, and a contact looking for a runner with "
            "downtime knows exactly which corner to check. The alley beside it is where the runner "
            "in Player Handout 2 backs off to get a look at the person tailing them, and where that "
            "person turns out to be a friend."
        ),
        "notes": (
            "No stat block, and he says nothing in the text -- he is the setting for Player Handout "
            "2, the version of the hook for characters who do not have Lyle Green as a contact and "
            "do not get into Club Penumbra. The contact who finds them there relays it badly and at "
            "length: Lyle Green, weirdly the same name as the kid from that '40s trid show "
            "'Daddy's Little Helper'; Dusty's up in Everett, tonight at six; a little rich for my "
            "blood but I hear they have real steak, from cows. Worth keeping as a location-flavored "
            "NPC for any Everett or downtown campaign -- a cheap, crowded, reliable place to be "
            "found."
        ),
        "contact_skills": ["Neighbourhood word of mouth", "Cheap food at any hour"],
    },
    {
        "name": "Knight Errant Shift Supervisor (Griffin Everett)",
        "role": "The shift commander and corporate liaison running Griffin's guard force from the control room",
        "archetype": "Corporate Security Officer",
        "title": "Shift commander and corporate liaison, Knight Errant detail, Griffin Everett facility",
        "race": "Human",
        "gender": "Male",
        "organization": "Knight Errant Security Services",
        "connection": 3,
        "description": (
            "Unnamed. One per shift, wearing either light security armor with helmet or the "
            "internal secure-clothing uniform, carrying nothing heavier than an Ares Predator II "
            "with gel and a stun baton, because his job is not to shoot people -- it is to deploy "
            "the twenty-seven who will. Orthoskin, muscle replacement, wired reflexes and a trauma "
            "damper under Leadership 4 and Shadowrunner Tactics 5. He drives an Ares corporate Ford "
            "Americar with armor 5 and a communications suite, made exclusively for Ares."
        ),
        "background": (
            "Knight Errant guards at this site have all been with the company at least two years, "
            "have combat experience, and most have seen action against shadowrunners at other major "
            "facilities. The supervisor is the most experienced of them, doubling as corporate "
            "liaison to Griffin. His standing procedure against a diversion is the reason the "
            "module warns that distractions will mostly frustrate the team: he sends the nearest "
            "team to look, brings the area sensors to bear, deploys some of his people to the "
            "OPPOSITE side of the disturbance on principle, and then does exactly what the runners "
            "are doing -- stands back and watches through the sensors, feeding what he learns to "
            "the Knight Errant units already rolling."
        ),
        "notes": (
            "Stats: B5 Q6[8] S6[8] C4 I4 W5, Ess 0.9, Reaction 6(11), Init 11+3D6, Combat Pool 8, "
            "Karma TR+2, Pro 4/Professional. Assault Rifles 7, Pistols 5, SMG 5, Throwing 4, Heavy "
            "Weapons (Launchers) 2 (4), Armed Combat (Club) 2 (4), Unarmed 4, Athletics 3, Stealth "
            "4, Intimidation 4, Interrogation 4, Electronics 3, Leadership 4; KE Operational "
            "Procedures 6, Security Procedures 6, Shadowrunner Tactics 5. Cyber: smartlink, "
            "cyberears (damper/amplification), datajack, cybereyes (flare comp, rangefinder, "
            "thermographic), headware radio with Comlink-IV and Crypto-3, Wired Reflexes 2, muscle "
            "replacement 2. Bio: enhanced articulation, orthoskin 3, trauma damper. Light security "
            "armor with helmet 7/6 or secure clothing with ultra vest 5/1. Ares Predator II (7M "
            "Stun, gel), AZ-150 stun baton, security passcard, flashlight. PLAY: he sounds the "
            "silent alarm, orders the internal guards to the armory, calls Knight Errant for "
            "backup, receives the astral mage who materializes in the control room to brief him, "
            "and interrogates anyone pulled off the student bus with contraband alongside Rebecca "
            "Owls-Breath. His goal in a breach is containment, not a pitched battle: keep the "
            "intruders fighting, redeploy, and wait for the response teams."
        ),
    },
]

ORG_UPDATES = {
    "Draco Foundation": {
        "notes_append": (
            "SRM 00-03 FORCEd Recon: the Draco Foundation maintains a complex on the wooded stretch "
            "of Marine Drive in north Everett, three properties from Griffin Biotechnology's new "
            "research compound (item 3 on the adventure's aerial reconnaissance photograph). This "
            "part of the sprawl belonged to the Native American nations before the Treaty of Denver "
            "and was never overbuilt; what homes there were have given way to large estates, "
            "corporate think tanks and research facilities, the Foundation's among them. The "
            "practical hazard the module calls out: runners who decide to hijack 'a delivery truck' "
            "coming off the nearest I-5 exit rather than identifying a specific scheduled Griffin "
            "delivery stand a real chance of stopping a Draco Foundation vehicle instead -- and "
            "many transports along this road travel with security escorts."
        ),
    },
    "Knight Errant Security Services": {
        "notes_append": (
            "SRM 00-03 FORCEd Recon: Knight Errant holds the security contract for Griffin "
            "Biotechnology's new north Everett research facility, taken at a heavily discounted "
            "rate because Ares Macrotechnology is one of Griffin's prime investors. KE covers every "
            "security function there except the Security Director's post, which Griffin keeps "
            "in-house. Structure: three eight-hour shifts starting 0700, four teams on rotation "
            "(Alpha, Bravo, Charlie, Delta -- four days on, one off, four swings, one off, four "
            "mids, three off, with the resting team as the recall pool). At the current fifty "
            "percent manning each shift is 28 guards: one shift commander/corporate liaison, two on "
            "the main gate, three in the control room, two in the main lobby, four on each of the "
            "two floors and the basement, and two patrolling each of the four exterior quadrants. "
            "External kit is Ares throughout: light security armor and helmet (7/6) with low-light, "
            "AZ-150 stun baton, Ares Predator II with gel, Ares Ravener SMG, two flash-bangs. "
            "Internal guards wear secure ultra-vest and secure clothing (5/1) with a pistol, baton "
            "and flashlight and refit at the armory on any alarm. Guards radio in every ten minutes "
            "and sometimes report through camera audio-visual pickups, which doubles as a test of "
            "the pattern-recognition software; fifteen-minute breaks every three hours, split "
            "lunches, and a shift change covering the half hour around the hour. They arrive by "
            "private car and Ares Citymaster; the supervisor drives an Ares-exclusive Ford Americar "
            "(armor 5, comms suite). Standard guard: B5 Q6 S6 C3 I5 W5, Ess 0.9, Reaction 5(10), "
            "Init 5+1D6 [10+3D6], Combat Pool 9, Pro 4/Professional, Wired Reflexes 2, smartlink, "
            "cybereyes, encrypted headware radio; two years' service minimum and most have fought "
            "shadowrunners elsewhere. They use military tactics, fight until a recognized authority "
            "stands them down, and are all but immune to fast talk, bribery and intimidation (+4 "
            "TN). Armory upgrades: Ares Alpha with APDS and air-timed mini-grenades, Ares MP-LMG "
            "with APDS, Ares Raptor rocket launcher, Zapper static discharge rockets, anti-vehicle "
            "rockets. Rapid response team: as the supervisor's block, in full heavy security armor "
            "(8/7) with EnviroSeal and fire resistance, carrying Ares Alphas. The removal team runs "
            "a nondescript black van approaching at random from north or south and hoses "
            "intruders with Gamma-Scopolamine from Ares Cascade rifles, shooting anyone still "
            "standing; the drugged wake up in the Marine Drive Stuffer Shack lot minus their "
            "illegal, security, military and surveillance gear. Paranormal patrol: one handler with "
            "Animal Handling 4 and a barghest (B7 Q6x4 S5 I3/6 W3, Init 6+2D6, 9S attack, dual "
            "natured, Enhanced Senses (sonar), Fear, Paralyzing Howl -- opposed Essence vs "
            "Willpower, one net success paralyzes) sweeps the grounds one day a week (1D6, 1 = "
            "Monday, never Sunday); on alert, four handlers and beasts plus a posted mage with "
            "watchers and low-level spirits, and alerts run three days. A frontal assault brings "
            "1D6 of each type of elemental at Force 4 with orders to subdue anyone without a "
            "Griffin badge, directed by a mage in astral space. KE also provides the resistance "
            "training that gives Griffin's mid-level managers and above Interrogation [Resist "
            "Verbal] 1 [3], and puts two undercover agents on the weekly Seattle University field "
            "trip bus. Getting anything out of a KE contact about a client contract is base target "
            "10 with +4 for a non-employee; the next barghest patrol date costs a minimum 2,000 "
            "nuyen bribe."
        ),
        "allies_add": ["Griffin Biotechnology", "Ares Macrotechnology"],
    },
    "DocWagon": {
        "notes_append": (
            "SRM 00-03 FORCEd Recon: DocWagon led the investment round that transformed Griffin "
            "Biotechnology, transferring close to 100 million nuyen from its main corporate office "
            "-- the opening line of the module's fiction, 'We have decided to make you an offer', "
            "is DocWagon's. The deal buys the rights to Dr. Indira Chontel's neural remapping work "
            "after development, probably a year of final research and testing away, at what should "
            "be a tidy profit on the initial outlay. Lyle Green's read is that DocWagon is "
            "committing no security or defense resources to the Everett facility beyond a liaison "
            "officer overseeing development; the guns belong to Knight Errant and the money behind "
            "them to Ares."
        ),
        "allies_add": ["Griffin Biotechnology"],
    },
    "Ares Macrotechnology": {
        "notes_append": (
            "SRM 00-03 FORCEd Recon: Ares is one of the prime investors in Griffin Biotechnology's "
            "neural remapping research, and has spent that position aggressively. It steered the "
            "security contract for Griffin's new north Everett facility to Knight Errant at a "
            "heavily discounted rate to protect its own interest, and supplied the entire technical "
            "security suite at bargain prices -- cameras, maglocks, sensor grids, MAD and chemical "
            "sniffers, and the Overwatch-VI and OperateIT smart frames, both programmed by Ares. "
            "The Knight Errant detail is equipped Ares brand throughout, down to the shift "
            "supervisor's Ares-exclusive Ford Americar. Ares also owns a private property along the "
            "same stretch of Marine Drive (item 5 on the aerial reconnaissance photograph)."
        ),
        "allies_add": ["Griffin Biotechnology", "Knight Errant Security Services"],
    },
    "Aztechnology": {
        "notes_append": (
            "SRM 00-03 FORCEd Recon: Aztechnology owns and operates Huitzilopochtli Plaza in "
            "downtown Seattle, across from the Pyramid, where Griffin Biotechnology leases its "
            "corporate offices -- and, as landlord, subcontracts all of Griffin's downtown security "
            "needs. That arrangement is precisely why Paladin cannot buy a run against Griffin's "
            "original premises at any reasonable price and has to settle for reconnaissance of the "
            "half-finished Everett compound instead. The delivery schedules for the Everett move "
            "sit on the old downtown network, behind Aztechnology security."
        ),
    },
    "Paladin Medical Technologies": {
        "notes_append": (
            "SRM 00-03 FORCEd Recon: another profitable quarter for Paladin, and shrewd business "
            "moves in the last few years have kept it growing -- but the shadows know that much of "
            "that success is down to Dr. Fredericks being unafraid to hire shadowrunners to "
            "retrieve prototypes, research data and special shipments. The module states the rumor "
            "outright: 'Rumor even has it that he hired a group of runners to hit a DocWagon "
            "manufacturing facility so that Paladin could secure a lucrative supply contract with "
            "Seattle General' -- the events of SRM 00-02 Demolition Run, now circulating as street "
            "talk. Griffin Biotechnology's sudden funding and the state-of-the-art facility it "
            "built in weeks make Griffin Paladin's only serious competition in the sprawl. "
            "Fredericks receives a report on the construction from a man he knows only as "
            "'Christof' and then hires through Lyle Green -- one of an extensive list of "
            "intermediaries -- for reconnaissance to be used later, not an immediate run. Pay is "
            "results-based: 1,000 nuyen guaranteed per runner, then 500 / 1,000 / 2,000 / 5,000 "
            "nuyen per information category for Poor / Fair / Good / Excellent, up to a theoretical "
            "28,000 for the team."
        ),
        "enemies_add": ["Griffin Biotechnology"],
    },
    "University of Seattle": {
        "notes_append": (
            "SRM 00-03 FORCEd Recon (the module writes 'Seattle University'): the university is one "
            "of the investors in Griffin Biotechnology's neural research and loaned out its "
            "thaumaturgic staff to assist in the construction of the new Everett compound -- the "
            "magical circle and the earth elementals that raised the granite walls. Griffin is now "
            "recruiting heavily there, inviting every graduate student in biotechnology, "
            "cybertechnology, traditional medicine and nanotechnology to apply for lab support and "
            "research posts. A tour bus leaves the campus every Wednesday carrying students, "
            "teachers and escorts on a field trip to the new facility ahead of the official "
            "opening, with two undercover Knight Errant agents aboard. Students are searched for "
            "cameras and recording devices as they step off the bus, pass through the front-door "
            "detection system, and must present student data on their identification credsticks "
            "proving graduate enrollment in one of those programs. Anyone who passes for a graduate "
            "student sees roughly seventy-five percent of the facility -- everything but the most "
            "secure labs, the security center and the armory."
        ),
    },
    "Universal Omnitech": {
        "notes_append": (
            "SRM 00-03 FORCEd Recon: Universal Omnitech maintains a corporate retreat on private "
            "property along the wooded stretch of Marine Drive in north Everett, two doors from "
            "Griffin Biotechnology's new compound (item 4 on the aerial reconnaissance "
            "photograph). Runners nosing around Griffin from a neighbouring property will find "
            "themselves on somebody's land whichever way they turn."
        ),
    },
    "Saeder-Krupp Heavy Industries": {
        "notes_append": (
            "SRM 00-03 FORCEd Recon: the private estate of Hans Brackhaus, described by the module "
            "as a high-level Saeder-Krupp executive, stands on Marine Drive in north Everett two "
            "properties from the Griffin compound (item 2 on the aerial reconnaissance photo, where "
            "the key misspells it 'Brackhaven Estate'). Nothing else is said about him or it, which "
            "given the reputation of that particular name is quite enough."
        ),
    },
    "Lone Star Security": {
        "notes_append": (
            "SRM 00-03 FORCEd Recon: Lone Star is one of the agencies holding a partial copy of the "
            "Griffin Everett facility's floor plans -- Griffin paid the metroplex's public services "
            "to keep only the parts relevant to each agency's responsibility. The Lone Star copy "
            "shows the basic halls and common areas plus the control room, standard security "
            "features and the armory, and can be prised out of a contact with a Negotiation (10) "
            "test and about 500 nuyen. Lone Star is also the endpoint of the PanicButton systems at "
            "Mackie Construction, where the Pinkerton night guards will call the Star rather than "
            "step outside."
        ),
    },
    "Ciarniello Family": {
        "notes_append": (
            "SRM 00-03 FORCEd Recon: the Everett construction firm Mackie Construction is widely "
            "rumored to be a Mafia operation. It is not. One of its two major owners, its business "
            "manager and financial officer, is a Vincent Ciarniello who simply happens to share a "
            "name with Don Vince 'Numbers' Ciarniello -- and having a Ciarniello handling the money "
            "at an Everett firm has been quietly profitable for Mackie for years. The module flags "
            "this explicitly as a coincidence and a red herring; whether the real Family enjoys "
            "having its name used as free advertising is left open, and is a ready-made hook for a "
            "GM whose runners start asking loud questions about it around Everett."
        ),
    },
    "Transys Neuronet": {
        "notes_append": (
            "SRM 00-03 FORCEd Recon: the CompuEyes-III camera-monitoring smart frame running on "
            "Mackie Construction's Matrix host was programmed by Transys Neuronet. Smart core "
            "rating 15, size 1,512 Mp, B5 E4 M0 S12 R15, Init 1D6; Analyze 6, Read/Write 3, Armor "
            "3, Medic 3, DINAB-3; fence value 18,000 nuyen. It compares camera frames using its "
            "Analyze rating as a Perception test (filtering out branches, fans and similar false "
            "positives), reroutes any anomaly to a primary monitor at the security station, logs "
            "it and sends a visual, audio or text alert, and uses the same rating to catch attempts "
            "to modify a camera's signal, control or time code -- which is what defeats looping and "
            "splicing. The Armor and Medic programs exist only to protect it from active attack and "
            "viruses. Object code only: it can be downloaded and sold or used, but not modified."
        ),
    },
}

LOC_UPDATES = {
    "Club Penumbra": {
        "notes_append": (
            "SRM 00-03 FORCEd Recon: the opening scene for any runner connected enough to get in. "
            "It takes a special person to get past the door, the line outside is as long as ever, "
            "and on this night the crowd is arguing about the new wave of ork bands supposedly "
            "rediscovering their ancient heritage -- marketing huey, or a Fourth World of their own "
            "like the elves and the great dragons claim? Tommy, an elf with a sense of flair whose "
            "dry martinis show real artistry, works the bar and passes on Lyle Green's message: "
            "Dusty's Steak House in Everett, tomorrow night, six sharp, dress nice, no toys. The "
            "tip he takes is part for the drinks and part for the information."
        ),
    },
    "Aztechnology Pyramid": {
        "notes_append": (
            "SRM 00-03 FORCEd Recon: Huitzilopochtli Plaza, owned and operated by Aztechnology, "
            "stands across from the Pyramid, and Griffin Biotechnology leases its downtown "
            "corporate offices there with its security subcontracted through its landlords. Being "
            "in the Pyramid's shadow is exactly why Paladin cannot buy a run against Griffin's "
            "original premises -- 'It was difficult to hire even shadowrunners to attempt runs "
            "against such a target.'"
        ),
    },
}

NPC_UPDATES = {
    "Lyle Green": {
        "background_append": (
            "SRM 00-03 FORCEd Recon: 'Lovely Lyle' is Dr. Fredericks' preferred intermediary out of "
            "Paladin Medical Technologies' extensive list -- he has produced results before, at "
            "reasonable fees, and is far more pleasant and civilized to deal with than most in his "
            "line of work. The trid show that made him is named here: 'Daddy's Little Helper', a "
            "'40s series about a boy helping his father run their store."
        ),
        "notes_append": (
            "SRM 00-03 FORCEd Recon: Lyle runs this job personally. He reaches connected runners "
            "through Tommy behind the bar at Club Penumbra and everyone else through a street "
            "contact, and takes the meet at Dusty's Steak House in downtown Everett at six -- dress "
            "code enforced, no weapons past the door, drinks and food on separate checks. He opens "
            "with a lecture on ninjas as intelligence gatherers rather than assassins and closes "
            "with a genuinely unusual offer: name your own pay. 1,000 nuyen guaranteed per runner "
            "for bringing back anything at all, then per-category fees of 500 / 1,000 / 2,000 / "
            "5,000 nuyen for Poor / Fair / Good / Excellent across floor plans, images, security "
            "plans and other information, up to a theoretical 28,000 for the team; he expects an "
            "average team to earn about 5,000. The fees are non-negotiable, but he will front 2,500 "
            "nuyen of expenses, rising to 5,000 if at least one runner at the table has him as a "
            "fixer (+500 per success on a standard Negotiation test). His advice is explicitly "
            "protective: 'If you feel that you are getting in over your heads, you should pull out, "
            "and accept whatever reward you have accomplished. You should not let greed drive you "
            "into something foolish.' He will also source gear as a separate transaction, with a 10 "
            "percent discount or an extra success on Availability time (runner's choice) for those "
            "who have him as a fixer. Turn the job down at the table and he thanks you, hands over "
            "a certified credstick with 500 nuyen -- carrying a locator beacon -- and has two large "
            "men follow you out to make sure you stay quiet. Wrap-up is at another upscale downtown "
            "club with Lyle in party clothes, reading the report and asking what the team wants to "
            "add before he pays."
        ),
        "contact_skills_add": ["Results-based intelligence contracts", "Fronting expense money"],
    },
    "Dr. Fredericks": {
        "notes_append": (
            "SRM 00-03 FORCEd Recon: a profitable quarter, and the module confirms what SRM 00-02 "
            "implied -- much of Paladin's success comes from Fredericks being unafraid to hire "
            "shadowrunners to retrieve prototypes, research data and special shipments, and the "
            "street now carries the rumor that he had a DocWagon manufacturing facility destroyed "
            "to win the Seattle General supply contract. His new problem is Griffin Biotechnology: "
            "undisclosed investors a couple of months ago, and a state-of-the-art Everett facility "
            "built in weeks. A man he knows only as 'Christof' delivers a disturbing report -- "
            "armored trucks, a magical circle doused by a lithe elven woman, earth elementals "
            "raising rock walls out of the ground, ork and troll crews, Mackie Construction logos. "
            "Griffin's downtown offices in Aztechnology's Huitzilopochtli Plaza are effectively "
            "unrunnable, so Fredericks consults his extensive list of intermediaries, settles on "
            "Lyle Green, and buys reconnaissance of the half-finished compound to make a profitable "
            "run possible later. He does not appear on screen."
        ),
    },
    "Vince Ciarniello": {
        "notes_append": (
            "SRM 00-03 FORCEd Recon: the Don's name is doing work he never asked it to. The Everett "
            "construction firm Mackie Construction employs a Vincent Ciarniello as business manager "
            "and financial officer and part owner, and the coincidence -- a Ciarniello handling the "
            "money at a prominent Everett company -- has convinced much of the sprawl that Mackie "
            "is a Mafia front. The module states flatly that the rumor is incorrect and that the "
            "two men are unrelated, and uses it as a red herring to burn a curious team's time."
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
Griffin's systems are deliberately compartmentalized: each computer system is dedicated to one
role and does not normally connect to the others, so shutting one down for maintenance or against
an intrusion leaves the rest running. Only the communications network touches the Matrix directly.
A system architecture overview ("Prepared by Ares Macrotechnology, Matrix Services Division,
COMPANY CONFIDENTIAL") is one of the player handouts, SRM00-03B p.7.

### Griffin communications network -- Green-8/8/14/10/15/11

The corporate web presence, email and telecom, plus pattern recognition and routing software that
inspects every inbound data stream. Telecom is passed to recipients on the main network; email is
held in storage and read from the main network. Any traffic trying to cross the internal SAN to
the main network is analyzed for viruses, smart frames, persona programs and other illegal
streams: a decker must beat the smart frame's Sensor rating and then the node's Access rating.
No paydata.

| Step | Event |
| --- | --- |
| 5 | Probe-8 |
| 10 | Probe-10, Tar Baby-10 |
| 15 | Tar Pit-10, Passive Alert |
| 20 | Mark-Rip-12, Tar Pit-12 |
| 24 | Sparky-12, Active Alert |
| 28 | Shutdown |

**OperateIT** (smart frame, programmed by Ares): core rating 20, 1,416 Mp, B5 E0 M0 S15 R20,
Init 3D6; Analyze 6, Commlink 6, Read/Write 6, DINAB-8; fence 22,500 nuyen. Analyze detects
deckers and illegal programs in transiting packets; Read/Write sends error and alarm messages to
the security consoles and deletes or edits files with illegal attachments; Commlink routes telecom
traffic and inspects it for monitoring or tampering.

### Griffin logistics network -- Green-8/8/15/8/8/15

The facility's nerve center for everything non-security: housekeeping and gardening drones, HVAC,
lighting, elevators, fire suppression, sprinklers and the PanicButton system. No paydata. Its only
link to the communications network is a one-way outbound feed dedicated to PanicButton -- and that
feed runs on a deadman's switch, transmitting constant status packets to the Matrix. Shut down
either the communications or the logistics network and the feed dies and the alarm fires at once,
unless a clever decker can spoof the outbound data. The security network can override most of this
network's functions.

| Step | Event |
| --- | --- |
| 5 | Probe-8 |
| 10 | Probe-10, Tar Baby-10 |
| 15 | Tar Pit-10, Passive Alert |
| 20 | Mark-Rip-12, Tar Pit-12 |
| 24 | Sparky-12, Active Alert |
| 28 | Shutdown |

### Griffin main network -- Orange-10/12/15/12/12/15

Labs, offices and research processing. Not connected to the Matrix directly; reaching it from
outside means decking through two SANs, the second of which only passes telecom, email and data
packets directly requested by an internal user. Most of the valuable research data is not online
yet, but files common to all R&D remain: paydata in the biomedical field to a combined maximum of
50,000 nuyen. This network also holds the delivery schedule that makes the delivery-truck ruse
possible, and the access data files that would have to be edited for a forged passkey to work.

| Step | Event |
| --- | --- |
| 3 | Probe-8 |
| 6 | Probe-10, Tar Baby-10 |
| 10 | Tar Pit-10, Passive Alert |
| 13 | Mark-Rip-12, Tar Pit-12 |
| 17 | Sparky-12, Active Alert |
| 20 | Shutdown |

### Griffin security network -- Red-8/15/12/10/12/15

All security hardware inside and out, with override authority over the logistics network. No
paydata -- but Rebecca Owls-Breath's real password plus access here or to the main network yields
one hundred percent of the floor plans, the largest single payout in the adventure.

| Step | Event |
| --- | --- |
| 3 | Probe-8 |
| 5 | Probe-10, Tar Baby-10 |
| 8 | Tar Pit-10, Passive Alert |
| 10 | Mark-Rip-12, Tar Pit-12 |
| 12 | Sparky-12, Active Alert |
| 15 | Shutdown |

**Overwatch-VI** (smart frame, programmed by Ares): core rating 20, 1,850 Mp, B5 E0 M0 S15 R20,
Init 6D6; Analyze 10, Read/Write 5, DINAB-8; fence 25,000 nuyen. Compares camera and sensor states
using Analyze as a Perception test, filtering ordinary movement; reroutes anomalies to a primary
monitor, logs them and alerts the security station; and uses the same rating to catch signal,
control or time-code tampering, defeating loops and splices. Remember the -4 penalty while the
sensor grids remain unconnected -- the software is working with cameras alone.

### Mackie Construction -- Orange-8/12/12/10/12/12

The bulk of Mackie's business lives in CAD data and specifications, so the firm has paid for the
best security it can afford. An IT staffer monitors by day; a Pinkerton decker sweeps the system,
the log files and the security tallies by night. The Griffin facility files are highly encrypted
and sit behind the strongest IC in the system: reaching them directly means beating
Probe-12/Scramble-12. Paydata to a maximum of 25,000 nuyen. Camera control, personnel files,
schedules and contact lists all run against the ordinary system rating.

| Step | Event |
| --- | --- |
| 3 | Probe-8 |
| 6 | Probe-10, Tar Baby-10 |
| 10 | Tar Pit-10, Passive Alert |
| 13 | Mark-Rip-12, Tar Pit-12 |
| 17 | Sparky-12, Active Alert |
| 20 | Shutdown |

**CompuEyes-III** (smart frame, programmed by Transys Neuronet): core rating 15, 1,512 Mp,
B5 E4 M0 S12 R15, Init 1D6; Analyze 6, Read/Write 3, Armor 3, Medic 3, DINAB-3; fence 18,000
nuyen. Camera monitoring and anti-tamper, as above; Armor and Medic protect it from active attack
and viruses. Object code only -- downloadable, sellable, usable, not modifiable.
"""

NOT_BUILT = """
- **"Christof"** -- the operative whose surveillance report on the Griffin construction lands on
  Fredericks' desk and starts the adventure. Fredericks knows him by no other name; he never
  appears. A standing hook.
- **The lithe elven woman** who doused out the magical circle at the start of the Griffin build,
  and the men who cut it -- unnamed, seen only in Christof's report.
- **The Griffin guard force** (28 per shift at current manning) and the **Knight Errant K-9
  handlers, barghests, rapid response teams and armory** -- stat blocks folded into the Knight
  Errant org notes and the facility notes; only the shift supervisor gets a row.
- **The two undercover Knight Errant agents** on the weekly Seattle University field-trip bus.
- **The DocWagon liaison officer** Lyle Green believes is overseeing development at the facility.
- **Griffin's administrative, computer, janitorial and maintenance staff** -- unnamed, but each
  group has a defined disclosure profile under interrogation; kept in the Griffin org notes.
- **Mackie Construction's six architects, four administrators and eight foremen** other than
  Anthony Trenello, and the day-shift IT staffer.
- **The two Pinkerton night guards** and the on-call **Pinkerton magician and armed response team**
  -- stat block folded into the Pinkerton org row.
- **The street contact** who delivers Player Handout 2 outside China Pete's, and the **two large
  men** who follow anyone who turns the job down out of Dusty's.
- **The Starbucks, the hair salon, the Korean market and the cellphone store** around Mackie
  Construction -- scenery the module offers as red-herring material (a Seoulpa front, a protection
  racket) rather than built places.
- **"Daddy's Little Helper"** (Lyle Green's '40s trid show), the new wave of ork heritage bands,
  the Airwall system, Ares Citymaster, Ares Cascade, Ares Alpha, Ares Ravener, Ares Raptor,
  Enfield, Defiance -- name-drops on gear and culture.
- **City Hall, the Fire Department, Public Works, the power company and the FCC** as floor-plan
  sources -- procedures rather than organizations; kept in the play notes and the facility notes.
"""

PLAY_NOTES = """
- This is an intelligence-gathering module with no single correct solution and no fixed pay. The
  team names its own price by what it brings back, so the GM's real job is bookkeeping: use the GM
  checklist (SRM00-03B p.5) against the players' Mission Log, and remember that each box is worth
  500, 1,000, 2,000 or 5,000 nuyen for Poor, Fair, Good or Excellent. 28,000 is the theoretical
  ceiling; about 5,000 is a normal night's work.
- The central secret is that the compound is half-finished. The pressure pads, laser grids and
  ultrasound arrays are installed but not connected, only the cameras are live, the guards are at
  fifty percent, and the pattern-recognition software is running at -4. The players do not know
  this. Let them discover a dead pressure pad and sweat over what it means.
- Floor plans come in layers and the layers stack: City Hall gives halls, common areas and the
  outdoor features; Lone Star adds the control room, security features and armory; the fire
  department adds sprinklers and extinguishers; Public Works adds restrooms, sewer access and the
  water supply station; the power company adds the electrical and telecom closets and the backup
  power; the FCC has no plans but will sell the licensed operating frequencies. Every two sources
  raises the category by one. Each costs about 500 nuyen and a Negotiation (10) test with the
  usual contact modifiers. Mackie Construction alone holds the complete GM map.
- Every approach in the Gathering Intelligence chapter has a designed outcome, and most of the
  aggressive ones are designed to fail instructively. The drive-by gets a stony stare and then a
  black van with Gamma-Scopolamine. The frontal assault gets six guards at the doors and 1D6 of
  each elemental at Force 4. The smooth talk gets nothing because there are no scheduled visitors
  and no surprise inspections. The distraction gets a professional response that deliberately
  reinforces the far side. What works is patience: the student bus, a hijacked scheduled delivery,
  a stationary microdrone, a slow astral sweep, and talking to construction workers.
- Astral recon is the only route to a full interior map short of Mackie -- but warn the players
  through the fiction, not the rules. Background Count 1, opaque Force 8 wards, and walls that are
  solid in astral space because they are packed with FAB tanks that will spray the corridor and
  paint the intruder. An astral Reaction (8) finds the tanks, but only if you try to pass through a
  wall rather than using the halls.
- Interrogation is legitimate and Griffin has planned for it: staff cooperate by policy and hand
  over their access codes and their area's plans. The trap is Rebecca Owls-Breath's duress code.
  Killing captives is the one thing that turns a reconnaissance job into a vendetta -- Etiquette
  (Corporate) (4) tells any runner that damage which heals naturally is tolerated and anything
  needing cyber replacement or expensive magic is not.
- Karma is entirely the GM's judgment, up to three points for the team: did they plan, did they
  stick to the plan, did they have contingencies, did they avoid strong-arm tactics, did they use
  their contacts well, were their methods interesting? One for a poor job, two for average, three
  for good, plus personal awards, with six the maximum any character can earn.
- Two threads for later: Paladin is buying this map to use it, so a return run against Griffin is
  the obvious sequel; and the aerial photograph puts the Draco Foundation, Universal Omnitech, Ares
  and Hans Brackhaus's estate on the same road as the target, any of which can be escalated into a
  campaign of its own.
"""
