# One Stage Before (FASA 7312, 1992, Nigel Findley) -- campaign order #16. Downtown / Harbor Island /
# Matthews Beach / Bitter Creek / Vashon Island, August 2053 (p.5 "The year is 2053"; the news handouts
# are dated Friday August 25 2053 and the Kingdome show is "twelve days" out in the prologue).
# Source text: docs/Adventures/text/Shadowrun 2e - Adventure - One Stage Before {FASA7312}.txt (64 pages).
# Editing inconsistencies in the book (recorded on the affected rows):
#   - The Shadows' fourth member is "Ernest Hawkins" (contents, Cast of Shadows p.60) but "Emile Hawkins"
#     in the Legwork table (p.51). Cast-page spelling used.
#   - The failure news handout (p.63) calls the go-gang the "Nightwalkers"; everywhere else it is the
#     Nightstalkers.
#   - Wallace served in the "UCAS Marines" (p.13), the "UCAS army" (p.56) and is "ex-Special Forces" (p.52).
#   - Allenby holds "a majority of Caravan stock" (synopsis p.6) but is its "sole shareholder" (p.50, p.62).
#   - Jetblack "died" "several years ago" (p.30) / "about two years ago" (p.51).
#   - Highstar's Special Operations Team is "seven gunners and a combat mage" (p.33) under a stat heading
#     that reads "Highstar Security Operative (5)" (p.34).
# ASCII only (pre-commit hook).

ADVENTURE = "One Stage Before"
ORDER = 16
SOURCE = "Shadowrun 2e - Adventure - One Stage Before {FASA7312}.pdf, pp. 4-63"
YEAR = "2053 (August)"

SYNOPSIS = """
Seattle has gone crazy over **The Shadows**, the hottest band since Jetblack died: one show at the
Kingdome, sixty-five thousand tickets gone in an hour, ten dead at the ticket offices. Broke and
nursing drinks at the **Blue Flame Tavern**, the runners are collected by two immaculate Highstar
"junior expediters" (**Daniel Maynes** and **Lester Hatton**), handed a 5,000-nuyen credstick for
showing up, and driven in a Rolls Royce Phaeton to **Kobe Terrace Park**, where **Jonathon Teague** of
**Highstar Incorporated** (a Mitsuhama subsidiary) offers 80,000 nuyen to find out who has been sending
death threats to **Lew Allenby**, the irascible dwarf who owns **Caravan Productions** and manages The
Shadows. Start by talking to Allenby, Teague says. Allenby throws them out of his Occidental Avenue
office the moment they mention Teague ("Those vultures?"), and on the way out a chromed giant who calls
himself "just **Wallace**" pumps them about Allenby.

Three hours later a Lone Star patrol opens fire on sight: Allenby is dead at his desk, still jacked in,
and a tip with manufactured evidence names the runners. Teague is "in conference". **Meta**, Teague's
lethal expediter, meets them at **The Mattresses** under the Space Needle to say Allenby is dead and
she wants the killer -- and proves her chrome when the ork **Teddy Boys** shoot up the club (pure
coincidence). Teague finally calls, sets a meet at Highstar's Harbor Island warehouse, and it is a
sniper-and-samurai gauntlet that ends with a swim in Elliott Bay. Then **Tangent**, Allenby's
secretary, phones from hiding: her boss spent his last afternoon reviewing simsense demos, somebody
wiped the demo directory, and The Shadows will be at media producer **Blair Wickingham's** party in
Matthews Beach. At the party the band toasts "absent friends, and those who are no further away than
sunset", Teague's double flees, and go-gangers in grim-reaper colors -- the **Nightstalkers** -- turn
out to be the band's security. Tailing the ganger **Blaze** to a dead firehouse in Bitter Creek, the
runners meet the gang's leader: **Jetblack**, the angst-rock megastar who faked his death, now a
vampire, Allenby's old friend, and the band's secret protector.

Jetblack's password ("Unruly") opens the hidden datastore on Allenby's computer: his diary (Teague
wanted Caravan; over Allenby's dead body), and backups of the deleted demos -- one of them carrying
Killer black IC written by Teague's decker **Himem**, which fried Allenby through his datajack.
Wallace, an FBI contractor with no homicide jurisdiction, supplies the word "Charon", which reveals
the tapped SAN into Highstar's own system: takeover files, Himem's research, and Teague's home address
at **Vashon Heights**. Twenty-five **Hard Corps** guards, dogs, lasers and an earth elemental defend
it. Only a reunion -- convincing Jetblack that The Shadows know what he is and do not care -- buys the
runners twenty Nightstalkers for a diversion. The proof is a notebook computer in Teague's den. Lone
Star recalls the warrants without apology; Highstar and Mitsuhama declare Teague a loose cannon and he
"commits suicide" in a Redmond rooming house within 48 hours; The Shadows pay 100,000 nuyen, and
Jetblack plays one private jam with them -- the first time all five stand on one stage.
"""

TIMELINE = """
- **Prologue (twelve days before the Kingdome show)** -- Allenby hangs up on Teague for the last time;
  Tangent confirms the Kingdome, cancellation insurance and Knight Errant security.
- **Day 1** -- Blue Flame Tavern pickup; Kobe Terrace Park meet (10,000 binder); Caravan offices;
  Wallace outside. Three-plus hours later Lone Star attacks (Allenby is already dead, killed by the
  booby-trapped demo). Meta's call and The Mattresses; the Teddy Boys.
- **Day 1-2** -- Teague's warehouse ambush at Pier 16, Harbor Island; Tangent's call; Wickingham's
  party that evening (Teague's double, Meta's covering fire, the toast).
- **Following days** -- Blaze the tail; the Nightstalkers' firehouse and Jetblack ("Unruly"); Mindfield
  at Caravan (Himem's Black-5 IC and the Highstar Special Ops van in ten minutes); Wallace again
  ("Charon"); the Highstar system and Himem's dogfight; Jetblack refuses, then the Richmond Highlands
  reunion (night only); the assault on Vashon Heights.
- **Friday August 25 2053** -- the News-Intelligencer reports Teague's "suicide" (success) or the
  "Nightwalkers" gang war on Vashon Island (failure). The Kingdome show follows within days.
"""

ORGS = [
    {
        "name": "Highstar Incorporated",
        "org_type": "corporation (entertainment; Mitsuhama subsidiary)",
        "tier": 3,
        "headquarters": "Seattle (the Highstar building downtown; address not given); parent: Mitsuhama",
        "summary": "Seattle entertainment corp -- live shows, trid -- that is really a Mitsuhama puppet; Teague's takeover of Caravan runs through it",
        "description": (
            "Apparently a major player in the Seattle entertainment scene (live shows, trideo, 'that kind "
            "of thing'), Highstar is in fact a shell company whose strings are pulled by its parent, "
            "Mitsuhama Computer Technologies; its own accounting datastore says as much. Highstar wants to "
            "increase its control of the music business in the sprawl, and its executive vice-president, "
            "Jonathon Teague, decided The Shadows were the coup that would win him the president's suite. "
            "President Takahashi Yanaga is well entrenched and never appears. The Highstar building has "
            "weapons detectors, chem-sniffers and a lobby packed with security; Teague's home address is "
            "not on file anywhere public. Street legwork (TN 4, TN 3 for media contacts): 'They make "
            "dirigibles, don't they?' -- 'Don't bother looking for drek on Highstar, look at who owns it.'"
        ),
        "leadership": [
            {"name": "Takahashi Yanaga", "title": "President", "notes": "Teague's target; never met."},
            {"name": "Jonathon Teague", "title": "Executive Vice-President", "notes": "Hires the runners as 'Mr. Johnson'; orders Allenby's murder. Dead within 48 hours of exposure."},
            {"name": "Meta", "title": "Personal expediter to Teague", "notes": "Ex-shadowrunner; does not know about the murder."},
            {"name": "Himem", "title": "Decker (research into modified black IC)", "notes": "Built the booby-trapped simsense."},
            {"name": "Daniel Maynes", "title": "Junior expediter / bodyguard", "notes": None},
            {"name": "Lester Hatton", "title": "Junior expediter / bodyguard", "notes": None},
        ],
        "notes": (
            "Security assets seen: junior expediters Daniel and Lester plus seven more of the same type in "
            "the park; a Rolls Royce Phaeton (500K nuyen) with a rigger chauffeur (VCR 2, Beretta 200ST); "
            "a Special Operations Team of seven gunners and a combat mage in a Volkswagen Superkombi III "
            "(ten minutes to Caravan, seven the second time). Highstar Security Operative: B5 Q6 S5 C3 I3 "
            "W4, Ess 3.2, R4(6)+2D6; TR 3/2; Firearms 5, Armed 4, Unarmed 4; Boosted Reflexes 3; medium "
            "security armor 6/5, Samopal vz 88 V assault rifle (laser, gas-vent 2). Highstar Combat Mage "
            "(a woman who joined for the hermetic libraries; takes no risks): B4 Q5 S4 C3 I5 W5, Ess 6, "
            "Magic 6, R5; TR 3/3; Sorcery 3 (Spellcasting 5, Combat 7); Predator II, spell foci Powerball 2 "
            "and Sleep 1; Heal 3, Mana Bolt 6, Powerball 6, Sleep 3, Ram 2. Teague's party wage mage "
            "(Grade 1 initiate, centers by declaiming her spells loudly in Greek): B4 Q4(7) S3 C3 I5 W5, "
            "Magic 7, R6; Sorcery 5 (Spellcasting 7); Chaotic World 3, Mana Bolt 3, Manaball 3, Power "
            "Missile 5, Ram 4. Highstar warehouse: Pier 16, north end of Harbor Island. Ending: Highstar "
            "and Mitsuhama disown Teague as a 'loose cannon', hire hit teams to close the loop, and will "
            "pay a slick team perhaps 20,000 nuyen for bringing the scandal to their attention as a 'public "
            "service' -- blackmail gets only hit teams. If Teague survives, Highstar legally absorbs "
            "Caravan and The Shadows become corporate property. Computer system mapped in the prep doc."
        ),
        "allies": ["Mitsuhama Computer Technologies", "Hard Corps Security Inc."],
        "enemies": ["Caravan Productions", "The Nightstalkers"],
    },
    {
        "name": "Caravan Productions",
        "org_type": "talent management / production company",
        "tier": 2,
        "headquarters": "Suite 500, 2265 Occidental Avenue, south of the Kingdome near the docks",
        "summary": "Lew Allenby's one-man empire: Seattle's premiere management and production company; managed Jetblack, manages The Shadows",
        "description": (
            "Built over twenty years by Lew Allenby into the city's premiere management and production "
            "company and, after signing Jetblack and then The Shadows, one of the biggest entertainment "
            "companies on the West Coast. Wholly owned by Allenby (the synopsis says 'a majority of the "
            "stock'; the Legwork section and the news handout say sole shareholder). Every takeover bid "
            "has died 'stone dead' against him. The office is a suite of platinum discs in a pitted, "
            "pre-2000 ferrocrete building with no cameras and no guards; LTG 1206 (53-2817). With Allenby "
            "dead the company simply stops: bills go unpaid, the security firms disconnect the alarms, and "
            "crime-scene tape hangs on the doors."
        ),
        "leadership": [
            {"name": "Lew Allenby", "title": "President and owner (murdered)", "notes": "Killed by Himem's booby-trapped simsense demo."},
            {"name": "Tangent", "title": "Executive assistant / receptionist", "notes": "Goes underground after an attempt on her life."},
            {"name": "David Graves", "title": "Database clerk", "notes": None},
            {"name": "Gnasher", "title": "Allenby's bodyguard", "notes": "Troll."},
        ],
        "notes": (
            "The Shadows' Kingdome show is Caravan's: 65,000 tickets sold out in one hour, cancellation "
            "insurance placed, Knight Errant hired ('the only ones who can handle something this big'), "
            "transport and limos booked, no second show ('always keep the kids wanting more'). Allenby's "
            "desk computer is not on the Matrix -- officially; Himem hardwired a tap from an LTG line into "
            "it. Passwords: 'Unruly' (the hidden datastore, from Jetblack) and 'Charon' (the hidden SAN to "
            "Highstar, from Wallace). Front door maglock Rating 5, Allenby's office Rating 4. Success "
            "ending: The Shadows go free-agent. Failure: Highstar absorbs Caravan's operations."
        ),
        "allies": ["The Shadows", "Knight Errant Security Services"],
        "enemies": ["Highstar Incorporated"],
    },
    {
        "name": "The Shadows",
        "org_type": "music band (megastar act)",
        "tier": 2,
        "headquarters": "Seattle; between shows they hole up at a musician friend's condo in Richmond Highlands",
        "summary": "The hottest band since Jetblack died: Marli Bremerton, Joey Nightmare, Sid Id, Ernest Hawkins; one sold-out Kingdome show",
        "description": (
            "'The Shadows -- they're It. Wiz. The megastars to end all megastars.' Their newest disk or chip "
            "sells out in two days; T-shirts and posters net more a year than most bands gross in a career. "
            "Marli Bremerton sings and writes and handles the outside world, Joey Nightmare plays lead "
            "synth-guitar, Sid Id and Ernest Hawkins (the Legwork table calls him 'Emile') play synths. "
            "They wear street leathers without armor, look bored at parties, smash their glasses after a "
            "private toast, and are guarded from time to time by a scuzzy biker gang nobody can explain. "
            "Managed by Caravan; Highstar is trying to poach them and 'Allenby would rather chew off his "
            "arm than let them go'."
        ),
        "leadership": [
            {"name": "Marli Bremerton", "title": "Lead singer, main songwriter, spokeswoman", "notes": None},
            {"name": "Joey Nightmare", "title": "Lead synth-guitar", "notes": None},
            {"name": "Sid Id", "title": "Synths, programming, record producer", "notes": None},
            {"name": "Ernest Hawkins", "title": "Synths, backing vocals, light show", "notes": None},
        ],
        "notes": (
            "The band has known about Jetblack's vampirism almost from the start and respected his "
            "disappearance; the toast 'to absent friends, and to those who are no further away than "
            "sunset' is theirs, and it is the key that unlocks his help. The best flacks in the business "
            "keep street monsters away from them -- claiming to know Jetblack earns only ridicule ('He was "
            "playing poker with Elvis, Jim Morrison and Adam Vikk, right?'). Success: 100,000 nuyen 'for "
            "services rendered', two Kingdome tickets each, a private jam session with Jetblack and a "
            "bootleg simsense of it as a memento (worth thousands, at the price of a vampire's trust); "
            "good future contacts who may send work. Failure: Highstar's unwilling property. Members have "
            "TR 2/2, armor clothing and Streetline Special hold-outs."
        ),
        "allies": ["Caravan Productions", "The Nightstalkers"],
        "enemies": ["Highstar Incorporated"],
    },
    {
        "name": "The Nightstalkers",
        "org_type": "go-gang",
        "tier": 2,
        "headquarters": "Deserted fire station, Palatine Avenue North, Bitter Creek (northern Downtown)",
        "summary": "Low-profile biker gang led in secret by the vampire Jetblack; every member carries his bite; moonlights as The Shadows' security",
        "description": (
            "One of the lower-profile go-gangs on Seattle's streets, causing far less mayhem than the "
            "Rusted Stilettos or Crimson Crush. Colors: a cloaked grim reaper riding a chopped Harley. "
            "Their leader never shows his face around town, which makes people think he is hiding a big, "
            "dirty secret -- he is Jetblack, and every ganger wears two puncture scars three centimeters "
            "apart over the carotid, a 'badge of honor' they would die before explaining. They feed him "
            "willingly; he protects them and calls it penance. They frequently provide security for The "
            "Shadows, and 'something real queer about them sets your teeth on edge'. Twenty-plus hard, "
            "competent riders."
        ),
        "leadership": [
            {"name": "Jetblack", "title": "Gang leader (vampire; the 'dead' megastar)", "notes": None},
            {"name": "Blaze", "title": "Young ganger; the tail on the runners", "notes": None},
        ],
        "notes": (
            "Nightstalker (20+): B5 Q6 S4 C3 I4 W4, Ess 6, R5; TR 4/3; Armed 4, Etiquette (Street) 3, "
            "Firearms 5, Stealth 3, Unarmed 4; Browning Ultra-Power (laser), knife, lined coat 4/2; three "
            "carry AK-97s and three Uzi IIIs. Party security uses the Gang Boss archetype with Bike 5 and "
            "Ruger Super Warhawks. Hangout: Fire Station archetype (Sprawl Sites p.23) -- open-plan dorm "
            "upstairs, bikes in the garage; the team walks into a dark, 'deserted' building and twenty "
            "guns come out of hiding. Ten ride escort to the Richmond Highlands reunion; twenty stage the "
            "diversion at Vashon Heights (played off-stage, 'sounds of distant mayhem'). Nightstalkers may "
            "also show up to pull the runners out of the Highstar Special Ops fight. In the failure news "
            "handout Lone Star is interrogating the surviving 'Nightwalkers' (sic). Legwork TN 5 (TN 4 "
            "from a ganger): 'They hang in Bitter Creek.'"
        ),
        "allies": ["The Shadows"],
        "enemies": ["Highstar Incorporated", "Hard Corps Security Inc."],
    },
    {
        "name": "The Teddy Boys",
        "org_type": "mucker gang (ork)",
        "tier": 1,
        "headquarters": "Seattle streets (turf not given); they crash The Mattresses on Denny Way",
        "summary": "Ork vandals in cheap Edwardian velvet and lace who prefer defacing people to property; their attack on The Mattresses is a genuine coincidence",
        "description": (
            "A particularly unpleasant 'mucker' gang, a mob of vandals who exist to frag up the system "
            "they blame for their bleak lives and are happy to die doing it as long as they take an honor "
            "guard along. Aping the Teddy Boys of 1960s London, they wear bad knock-offs of Edwardian "
            "clothing in cheap synthetic velvet and satin, dripping lace. Twenty-four of them overpowered "
            "The Mattresses' elf maitre d' and its security team, taking heavy casualties on the way in; "
            "twelve were still fit to party."
        ),
        "notes": (
            "Teddy Boy: B5 Q4 S5 C1 I2 W4, Ess 6, R2; TR 2/2; Armed 5, Etiquette (Street) 3, Firearms 4, "
            "Unarmed 4; knife, lined coat 4/2, Uzi III. A Moderate wound takes one out; the rest retreat "
            "once two-thirds are down. The attack has NO connection to Allenby, Teague or the run -- a red "
            "herring the GM should not let the players chase too long. Lone Star arrives five minutes "
            "after the first shot. The Mattresses' members hunt down anyone who compromises the club, so "
            "the survivors have a short future."
        ),
    },
    {
        "name": "Hard Corps Security Inc.",
        "org_type": "private security corporation",
        "tier": 3,
        "headquarters": "Seattle (headquarters address not given)",
        "summary": "One of the best and toughest security firms in the plex -- astral, computer, lasers, and gunship back-up inside ten minutes; guards Teague's Vashon Island compound",
        "description": (
            "'Any place protected by Hard Corps might as well be marked Hands Off.' Well-trained, "
            "well-equipped guards; astral and computer security; pressure pads, motion detectors and "
            "perimeter lasers; and the best reputation for back-up in the plex -- within ten minutes of an "
            "alarm you are drowning in Hard Corps gunners, helicopter gunships and Citymasters. Teague's "
            "Vashon Heights compound is their showpiece: twenty-five guards, three troll animal handlers "
            "with attack dogs, a Rating 4 earth elemental, a security computer whose dial-out SAN calls "
            "Hard Corps headquarters by itself."
        ),
        "notes": (
            "Hard Corps Security Guard (25+): B5 Q6 S4 C1 I2 W5, Ess 6, R4; TR 3/3; Armed 4, Etiquette "
            "(Corporate) 3, Firearms 5, Unarmed 4; AK-97 (laser, RC 2, three extra clips), partial heavy "
            "armor 6/4, survival knife, microtransceiver; paid to kill intruders, not to die. Animal "
            "Handler (troll, 3): B7 Q4 S6 C1 I2 W4, R3; TR 2/2; AK-97 SMG; looses the dog and snipes "
            "from cover. Dog (3): B3 Q4x4 S3 W2, attack dice 4, TR 3 -- not paranormal. Riggers (2): B4 "
            "Q6 S3 C2 I5 W4, Ess 4.5, R5(7); TR 3/2; Rotor Craft 4 (Fixed-Rotor 6), Gunnery 3; VCR 1, "
            "low-light/thermo eyes; stay out of small-arms range. Back-up: Northrop PRC-44B Yellowjacket "
            "with Vanquisher minigun in ten minutes; five minutes later a Hughes WK-2 Stallion (seven "
            "guards, door minigun) and a Citymaster (twelve guards, FN-MAG 5 turret). Legwork TN 5 (TN 6 "
            "if you are stupid enough to ask a Hard Corps employee). Repels the assault 'with no "
            "casualties and limited property damage' in the failure handout."
        ),
        "allies": ["Highstar Incorporated"],
        "enemies": ["The Nightstalkers"],
    },
]

LOCATIONS = [
    {
        "name": "Caravan Productions Offices",
        "location_type": "corporate facility",
        "district": "Occidental Avenue, south of the Kingdome, near the docks",
        "security_level": "Low Security",
        "controlling_org": "Caravan Productions",
        "summary": "Suite 500 in a pitted pre-2000 ferrocrete building with no cameras or guards; platinum discs, Tangent's desk, Allenby's antique desk and the computer that killed him",
        "description": (
            "An old gray ferroconcrete building from before the turn of the century, pitted and streaked "
            "black by decades of hard rain -- no security cameras, no macroplast booth, no guards, just "
            "corp wannabes in the lobby. Suite 500 is the top (fifth) floor: a surprisingly well-appointed "
            "reception room dotted with platinum discs (most The Shadows', a couple for 'some old novastar "
            "named Jetblack'), Tangent at the desk with David Graves hovering, and Allenby's inner office "
            "-- more awards under track lighting, a huge antique dark-wood desk, and a sophisticated "
            "computer wired by fiber optic to the datajack in the dwarf's head. Address: 2265 Occidental "
            "Avenue; LTG 1206 (53-2817)."
        ),
        "notes": (
            "Visit one: Allenby is 'in conference'; push past Tangent and he throws his soykaf mug, "
            "mentions of Teague make him apoplectic, a key on his computer summons Gnasher. Gunfire here "
            "means PANICBUTTONs and Lone Star. Visit two (Mindfield): deserted, crime-scene tape, maglocks "
            "Rating 5 (suite) and 4 (office), every alarm disconnected for non-payment. The desk system is "
            "Allenby's computer (map in the prep doc): tortoise programs Bod 3, Sensors 2, Analyze 1, "
            "Evaluate 1, Browse 2, Decrypt 2. Tripping the Trace and Report 7 ice brings Himem's Black-5 "
            "IC in five actions and the Highstar Special Ops van in ten minutes. Visit three (Charon): one "
            "Highstar operative left on watch in the outer office; the van now arrives in seven minutes."
        ),
    },
    {
        "name": "Kobe Terrace Park",
        "location_type": "park",
        "district": "Downtown, South Jackson Street just west of the freeway",
        "security_level": "Patrolled / Commercial",
        "summary": "A little oasis of green among the skyrakers by day, a gang killing ground by night; Teague's Mr. Johnson meet",
        "description": (
            "A beautiful spot at South Jackson Street just west of the freeway, a little oasis of green "
            "surrounded by corporate skyrakers -- and, despite the best efforts of Lone Star and corporate "
            "security, a frequent night-time battlefield for downtown gangs. Deserted in daylight, which "
            "is when Teague materializes from behind a tree in a business suit."
        ),
        "notes": (
            "Teague's escort (Daniel and Lester) drops back to give the meet privacy; seven more security "
            "men of the same two types wait in the bushes if the runners try anything. Teague pays a "
            "10,000-nuyen certified credstick binder against 80,000 and will raise the completion fee up "
            "to 50 percent (he never intends to pay). A good recurring neutral-ground meet for corporate "
            "Johnsons who like witnesses to be gangers."
        ),
    },
    {
        "name": "The Mattresses",
        "location_type": "private members club",
        "district": "Denny Way near Seattle Center, under the Space Needle (beside Tam's Under the Needle)",
        "security_level": "Corporate High Security",
        "summary": "Underground members-only club where bigwigs from every corp meet in guaranteed safety -- the members hunt down and kill anyone who causes trouble",
        "description": (
            "A narrow concrete stairway between the building and Tam's leads below street level to a "
            "solid metal door and a hand-sized plaque: 'The Mattresses -- Members and Guests Only'. Inside: "
            "a dark-wood anteroom with burgundy carpet and a dinner-jacketed elf maitre d' behind a podium, "
            "then understated opulence -- leather-topped tables, leather wingbacks, several million nuyen "
            "of art, two dozen affluent corp types who give street trash a single surprised glance. Too "
            "many people need The Mattresses; anyone who compromises its safety dies. Layout: Mid-size "
            "Restaurant archetype (Sprawl Sites p.37)."
        ),
        "notes": (
            "The podium hides a Rating 8 weapon detector (8-dice Perception vs Concealability); guests may "
            "keep one light or medium pistol and one knife, everything else is checked or you wait in the "
            "foyer. State your sponsoring corporation ('we're with Highstar'). Each table has a Rating 7 "
            "white-noise generator; a Rating 6 magical ward covers the room. Security within a minute of "
            "trouble: five Corporate Security Guards (partial heavy armor, stun batons, tasers, Uzi IIIs), "
            "a Company Man, two Wage Mages -- neutralize and expel, not kill. Street (3) or Corporate (2) "
            "legwork confirms it is safe from corporate shootouts. Chairs give Barrier 1 cover, the heavy "
            "tables Barrier 2. Meta's booth is by the kitchen; she leaves by the back door. Lone Star five "
            "minutes after the Teddy Boys' first shot."
        ),
    },
    {
        "name": "Highstar Warehouse (Pier 16, Harbor Island)",
        "location_type": "warehouse",
        "district": "Pier 16, north shore of Harbor Island",
        "security_level": "Low Security",
        "controlling_org": "Highstar Incorporated",
        "summary": "Deserted wharf where Teague's 'meet' is a sniper, samurai and street-mage gauntlet that ends in Elliott Bay",
        "description": (
            "Highstar's warehouse sits on one of the wharves along the north shore of Harbor Island -- "
            "seen one dock, seen them all. No ships alongside, two cranes at the north end, the warehouse "
            "itself, and a single road out at the south end of the wharf. The address is in the public "
            "datanets."
        ),
        "notes": (
            "The ambush (map p.20): two snipers on the warehouse roof and one on the eastern crane; a "
            "street mage (sustained Increase Quickness +4) on the other crane; two street samurai inside "
            "the warehouse; a Leyland-Rover electric transport pulls across the south end and three more "
            "samurai get out. Perception (6): two successes suspect the trap, none means a full turn "
            "surprised. Sniper (3): B4 Q5 S3 C2 I3 W5, R4, 4/3; TR 3/2; Firearms 4 (Sniper Rifles 6, "
            "Walther WA-2100 8), Stealth 4; WA-2100 with low-light scope and silencer; slot and run if "
            "approached. Street Mage: B2 Q5(9) S2 C2 I5 W3, Magic 4, R5(7); TR 3/2; Sorcery 5; Colt "
            "America L36; Fireball 4, Increase Quickness 4, Power Bolt 4. Street Samurai (5): B5 Q5 S5 C1 "
            "I2 W4, Ess 1, R3(9)+4D6; TR 3/2; Wired 3; AK-97 SMG (RC 2), armor jacket. Hired through "
            "untraceable 'channels'. Expect a swim: heavy weapons and the team's vehicles stay behind. "
            "Teague is nowhere near."
        ),
    },
    {
        "name": "Highstar Incorporated Building",
        "location_type": "corporate headquarters",
        "district": "Downtown (address not given)",
        "security_level": "Corporate High Security",
        "controlling_org": "Highstar Incorporated",
        "summary": "Highstar's Seattle offices: weapons detectors, chem-sniffers, a lobby full of guards; Teague is always 'in conference'",
        "description": (
            "The Seattle home of Highstar Incorporated, the entertainment front through which Mitsuhama "
            "reaches into the music business. Teague's office terminal (I/OP-5), the accounting and "
            "personnel departments, and Himem's research lab all hang off the Highstar computer system "
            "(mapped in the prep doc). The book never gives the street address."
        ),
        "notes": (
            "Barging in gets the team no further than the lobby: high-tech weapons detectors, chem-sniffers, "
            "security personnel wall to wall, and no way to learn where Teague lives. After the ambush, "
            "both Highstar's offices and Teague's city home are 'guarded by small armies'. The only "
            "productive entry is through the Matrix, via the tapped SAN from Allenby's computer."
        ),
    },
    {
        "name": "Wickingham's Penthouse (Matthews Beach)",
        "location_type": "penthouse",
        "district": "Matthews Beach (exclusive side)",
        "security_level": "Corporate Standard",
        "summary": "Media producer Blair Wickingham's twelve-storey penthouse party: starlets, producers, The Shadows, Nightstalker doormen, and Teague's double",
        "description": (
            "One of four corner penthouse suites atop a twelve-storey luxury block on the exclusive side of "
            "Matthews Beach. Two armed-and-armored guards in the lobby, black-leathered Nightstalker bikers "
            "at the elevators and the suite door, and inside the young bright lights of Seattle -- sleazy "
            "producers, brain-dead leading men, willing starlets, chipped-out musicians -- perfume, smoking "
            "substances, hors d'oeuvres and champagne, Jetblack's last, most depressing album on the "
            "sound system. Layout: Large Residence archetype (Sprawl Sites p.34)."
        ),
        "notes": (
            "Rating 7 weapon detectors in the lobby doorframe; guests keep one personal-defense weapon, "
            "street trash checks everything. Staff: two lobby guards (Street Cop archetype: stun baton, "
            "Defiance Super Shock taser, Fichetti Security 500, armor jacket), four bikers (Gang Boss "
            "archetype, Bike 5, Ruger Super Warhawk), three undercover interior guards (Corporate Security "
            "Guard: taser, Ares Slivergun, armored clothing), ten serving staff, twenty-five guests (Media "
            "Producer / Club Habitue / Simsense Star archetypes; PR 1 cannon fodder). Play the mistaken "
            "identity ('What band are you with?'). The toast: Perception (4) to realize it is a band "
            "tradition. Teague's double arrives with Daniel, Lester and a wage mage, bolts for the "
            "elevator (four turns), security freezes the second car, twelve flights of fire stairs, the "
            "Phaeton peels out, and Meta in the bushes fires through the glass doors to keep heads down "
            "before leaving on her BMW Blitzen. Lone Star in five minutes (100 turns), Citymaster five "
            "minutes after; the Star would rather arrest than kill here and the team gets one escape "
            "chance en route downtown. Etiquette (Street) 4 identifies the reaper colors as Nightstalkers."
        ),
    },
    {
        "name": "Nightstalkers' Firehouse (Bitter Creek)",
        "location_type": "gang territory",
        "district": "Palatine Avenue North, Bitter Creek (northern Downtown)",
        "security_level": "Low Security",
        "controlling_org": "The Nightstalkers",
        "summary": "Deserted fire station with black-painted windows: bikes in the garage, a dormitory of bedrolls upstairs, Jetblack in the dark",
        "description": (
            "A deserted fire station whose black-painted windows make it look empty until light leaks "
            "around the big garage door and a rider guns out into the street. Fire Station archetype "
            "(Sprawl Sites p.23): the garage full of bikes below, an open-plan dormitory of thin mattresses "
            "and bedrolls above with only the corner washroom walled off. Guests are walked up the back "
            "stairs in total darkness with gun barrels in their kidneys until a cool blue nimbus lights a "
            "slim young man in tailored black leather."
        ),
        "notes": (
            "The gang expects visitors: sneak in and twenty-plus Nightstalkers rise from hiding; watch "
            "from a distance and twenty watch you back ('Make like ice or we'll geek you where you "
            "stand'). Jetblack checks every word with Analyze Truth and digs with Mind Probe; if the team "
            "fights he stuns them with spells and they wake bound upstairs. Level with him (clear our "
            "names, find who killed Allenby, no harm to The Shadows) and he gives the password 'Unruly' "
            "and asks for first shot at the killer. Second visit: he refuses muscle until convinced The "
            "Shadows know his secret, then rides with the team (night only) to Richmond Highlands."
        ),
    },
    {
        "name": "The Shadows' Richmond Highlands Condo",
        "location_type": "residential community",
        "district": "Richmond Highlands",
        "security_level": "Patrolled / Commercial",
        "summary": "Ground-floor condo of a musician friend where The Shadows hide between shows; a guard in a bulletproof booth and no obvious alarms",
        "description": (
            "A ground-floor condo in the Richmond Highlands owned by another musician, a friend of the "
            "band, where The Shadows are hanging out before the Kingdome show: a security guard in a "
            "bulletproof glass booth at the lobby door, no obvious alarm systems, and whatever Jetblack "
            "says to the guard opens the door. Large Residence archetype (Sprawl Sites p.34) if a map is "
            "needed."
        ),
        "notes": (
            "The reunion: Marli Bremerton opens the door ('It is you. I knew you weren't dead'), hugs and "
            "handshakes, a vampire with tears in his eyes -- play it out or send the runners to pour "
            "drinks in another room. The band cannot help ('unless we can really prove Teague killed "
            "Allenby'); the newly happy Jetblack and twenty Nightstalkers can. 'We're gangers, not assault "
            "troops. You do the planning.' Gunning down The Shadows here ends the team's Seattle career."
        ),
    },
    {
        "name": "Teague's Vashon Heights Compound",
        "location_type": "private estate / compound",
        "district": "Vashon Heights, north tip of Vashon Island (waterfront, 1 km from the hydroplane-ferry terminal)",
        "security_level": "Corporate High Security",
        "controlling_org": "Hard Corps Security Inc.",
        "summary": "Teague's three-hectare waterfront fortress: monowire fence, 25 Hard Corps guards, dogs, lasers, pressure pads, an earth elemental, gunships in ten minutes -- and the proof in his den",
        "description": (
            "Vashon Heights is one of the newer luxury enclaves outside the sprawl -- rolling hills and "
            "real trees around the compounds of Seattle's rich industrialists, reached by the high-speed "
            "hydroplane ferry from just south of Lincoln Park. Teague's lot covers almost three hectares "
            "(radius about 100 m) of manicured lawn, copses and two koi ponds, ringed by a six-meter "
            "reinforced fence angled outward with three strands of electrified monowire, one reinforced "
            "south gate that stops a Citymaster, and a ballistic-composite guard shack. The lawn runs to a "
            "two-meter retaining wall and a strand of beach on Puget Sound. The house: concrete exterior "
            "(Barrier 16), ballistic-composite doors (14), interior walls 10, interior doors 4, reinforced "
            "windows 4; a trideo room, boardroom, library, two guest rooms (one is Meta's), a sybarite's "
            "bathroom with sunken jacuzzi, an automated kitchen with a cook, a decadent bedroom, a dining "
            "room fit for a luxury hotel, a living room with polarizing patio doors (Barrier 8), and "
            "Teague's den. Heated garage: a SAAB Dynamit 776TI and Meta's BMW Blitzen 2050."
        ),
        "notes": (
            "Map pp.41-44. Fence: Barrier 24 vs vehicles, 8 vs blades; monowire 4S4 to grab, (Body)S4 at "
            "walking speed, (Body x 2)S4 faster. Seawall hides Rating 8 motion detectors (10 m) -- eight "
            "guards in five turns. Guards: three at the shack, twelve patrolling, five on the waterfront, "
            "five hidden at the house; three troll handlers with dogs (one hidden). Front and rear doors: "
            "Rating 5 maglocks, two-stage lasers, 40-kg pressure pads under the carpet (also the patio "
            "doors). No mage on site; a Force 4 earth elemental defends the house. Shack: Barrier 14, "
            "Rating 6 maglock, a terminal on the security computer (mapped in the prep doc) from which a "
            "decker can shut down most of the house systems; the SAN dials Hard Corps HQ by itself on "
            "active alert. Back-up: Yellowjacket in ten minutes, Stallion and Citymaster five minutes "
            "later. Teague and Meta retreat to the den (Barrier 14 walls, 8 door; hidden security "
            "terminal) and fight to the death; the notebook computer there (Green-2, password Barrier 2) "
            "holds his takeover files and Himem's notes on planting the simsense -- the proof. Loot: "
            "several thousand nuyen of gewgaws in the bedroom and dining room. Ways in: fast-talk the "
            "gate, deck the shack, or a Nightstalker diversion at the gate while the team comes over the "
            "fence or in from the water on Suzuki Watersports. Run it cinematically -- fifty guns, then "
            "seventy; roll only what is aimed at the runners."
        ),
    },
]

NPCS = [
    {
        "name": "Jonathon Teague",
        "role": "Highstar's Machiavellian executive VP posing as 'a junior expediter'; hires the runners to frame them for Allenby's murder",
        "archetype": "Corporate Executive",
        "title": "Executive Vice-President, Highstar Incorporated (the 'Mr. Johnson')",
        "race": "Human",
        "gender": "Male",
        "organization": "Highstar Incorporated",
        "connection": 4,
        "description": (
            "A good-looking, hard-faced man who always dresses impeccably, with a gold stud shaped like a "
            "nuyen sign in his left ear and a smooth, well-modulated voice that says 'um, terminate the "
            "flow of events, as it were'. 'Junior expediter, you might say. I make things happen.' Keen "
            "business sense coupled to an instinct for whose back to stab at any given moment."
        ),
        "background": (
            "Born to a rich and influential Seattle family, best education money could buy, vice-president "
            "before thirty, executive VP of Highstar five years later, and immediately looking for a coup "
            "big enough to ease President Takahashi Yanaga out of his chair. The Shadows were it: if he "
            "brought them into the Highstar stable, Mitsuhama might reward him with Yanaga's position. "
            "Allenby refused every offer. So Teague hired a street samurai (Meta) to guard his back, a "
            "decker (Himem) to kill Allenby with a booby-trapped simsense demo, a Lone Star tip and "
            "manufactured evidence to hang it on a team of deniable runners, and shadow muscle to make "
            "sure the runners never argued. 'What good is the word of known shadowrunners against a "
            "corporate executive?'"
        ),
        "notes": (
            "Never intends to pay (offers 80,000 and will 'agree' to +50 percent). 'In conference' after "
            "the first meet; uses a double with his real bodyguards at Wickingham's party; his city home "
            "and office are guarded by small armies; only the Highstar personnel datastore or Jetblack "
            "gives up Vashon Heights. Put a price on the runners' heads -- every fixer meet is a potential "
            "setup. Stats: B3 Q5 S3 C5 I6 W5, Ess 3.8, R5; TR 2/3; Armed 2, Computer Theory 5, Etiquette "
            "(Corporate) 8, (Street) 5, (Music Business) 6, Firearms 4, Negotiation 6, Psychology 8, "
            "Unarmed 2; datajack 200 Mp; Ares Viper Slivergun (laser), armor clothing 3/0. Fights to the "
            "death in the den beside Meta; Jetblack may feed on him. If he survives the raid, Highstar and "
            "Mitsuhama have him dead within 48 hours: 'Executive Suicide', body in a Redmond rooming "
            "house (News-Intelligencer, August 25 2053)."
        ),
    },
    {
        "name": "Lew Allenby",
        "role": "Irascible dwarf owner of Caravan Productions, manager of Jetblack and The Shadows; murdered at his desk by a booby-trapped simsense",
        "archetype": "Talent Manager",
        "title": "President and sole shareholder, Caravan Productions (deceased)",
        "race": "Dwarf",
        "gender": "Male",
        "organization": "Caravan Productions",
        "connection": 4,
        "description": (
            "Balding and ugly, thick black hair and an unruly black beard, a wrinkled leathery face and "
            "cold flint-hard eyes; a datajack cable running to the computer on an antique desk under walls "
            "of platinum discs. 'And just who the frag are you?' Easily angered, gifted with interpersonal "
            "skills he frequently chooses not to use; throws his soykaf mug at whoever annoys him most, "
            "punches dents in the wall, and says he does not 'work with street punks'. A phenomenal "
            "businessman and an unbelievable jerk -- 'everything he touches turns to gold'."
        ),
        "background": (
            "Born on Seattle's meanest streets with two ways out, gang or band, he chose the band: a "
            "marginal career in the sprawl's small underground clubs until he found his business skills "
            "outran his talent. Twenty years of management built Caravan Productions into the city's "
            "premiere company; signing Jetblack and then The Shadows made it one of the biggest on the "
            "West Coast. Teague's takeover offer was 'attractive'; Allenby's answer was that Highstar "
            "would get Caravan over his dead body. A 'diary junkie' who recorded everything he thought in "
            "a private, hardware-hidden computer node; paranoid enough to keep his demo chips backed up "
            "there too, which is what convicts his killer."
        ),
        "notes": (
            "Dead within hours of the runners' visit: found by Tangent at his desk, still jacked in, no "
            "sign of violence -- Killer 4 black IC hidden in a simsense demo, delivered straight through "
            "his datajack. Death threats, and a car bomb three days earlier he wrote off as 'a fragging "
            "smoke charge' (both presumably Teague's groundwork). Stats: B4 Q3 S5 C4 I6 W6, Ess 3.8, R4; "
            "TR 2/3; Etiquette (Corporate) 6, (Street) 6, (Music Business) 8, Negotiation 5, Psychology "
            "6, Computer Theory 3; datajack 200 Mp; armor clothing. His diary (100+ Mp, five hours to "
            "read) is the motive; Jetblack believes he died without learning his old friend's secret."
        ),
    },
    {
        "name": "Darryl Wallace",
        "role": "'Just Wallace' / 'Ripper' -- chromed ex-Special Forces FBI contractor investigating Caravan; feeds the runners the word 'Charon'",
        "archetype": "Street Samurai",
        "title": "FBI contractor (not on the payroll); ex-UCAS military, Desert Wars veteran",
        "race": "Human",
        "gender": "Male",
        "organization": "UCAS Federal Bureau of Investigation",
        "connection": 4,
        "description": (
            "A big figure, definitely human but bulky enough to pass for troll when it suits him, in a "
            "black duster and dark street clothes, empty hands held out from his sides, a wry half-smile "
            "as if he can read your caution off your mind. Chromed to the max and moves like a jungle "
            "cat; 'death on two legs' when he is ticked off, but he would rather talk his way out of "
            "trouble. 'Hoi, chummers. Got a minute to shoot the drek?'"
        ),
        "background": (
            "Played in a band in New York with considerable success before enlisting; served several "
            "Desert Wars tours (the book variously says UCAS Marines, UCAS army and Special Forces) and "
            "resigned his commission. Now a shadowrunner the Feds hire from time to time, which keeps his "
            "FBI connections nearly impossible to dig up (legwork TN 8, TN 6 with federal contacts). His "
            "current job for a task force on corruption and collusion in an entertainment industry that "
            "is 98 percent megacorp-owned: check the (false) payola rumors around Allenby. He noticed the "
            "runners leaving Allenby's office and wondered what a respectable promoter wanted with street "
            "drek like them."
        ),
        "notes": (
            "Cover story: ex-army looking for an 'expediter' job with Allenby; sticks to it no matter what "
            "and walks away rather than fight (if killed, the FBI has 'clones' to replace him). After "
            "Mindfield he levels: Highstar killed Allenby, homicide is outside his jurisdiction, FIIGMO, "
            "but dirt on Highstar or something unpleasant done to Teague and he will pull strings to clear "
            "the murder rap. 'You found the door that wasn't there. The word of the day is Charon.' Can "
            "supply four low-grade ork mercs (Ork Mercenary archetype) for a deniable raid if pitched "
            "right (Etiquette Street/Law Enforcement 6). Holding him hostage brings an FBI Fast Response "
            "Team. Stats: B6(7) Q6 S5(6) C4 I5 W6, Ess 0.2, R6(8)+2D6; TR 6/4; Armed 6, Etiquette "
            "(Corporate) 3, (Street) 4, Firearms (Cyberweapons) 8 (Heavy Pistol 10), Negotiation 2, "
            "Psychology 4, Stealth 6, Unarmed 6; Boosted Reflexes 3, both arms cyberlimbs with increased "
            "strength, retractable spurs and implanted Ares Predators, cybereyes (flare, thermographic), "
            "dermal plating 1; lined coat, survival knife. Afterwards drops out of sight with a cryptic "
            "note of congratulations; keeps the team on file -- an excellent future Mr. Johnson."
        ),
        "contact_skills": ["Federal (FBI) strings, quietly pulled", "Deniable muscle and entertainment-industry background"],
    },
    {
        "name": "Meta",
        "role": "Teague's personal expediter -- an ex-shadowrunner 'hatchetwoman' in haute couture and silver gloves who does not know about the murder",
        "archetype": "Street Samurai",
        "title": "Personal expediter to Jonathon Teague, Highstar Incorporated",
        "race": "Human",
        "gender": "Female",
        "organization": "Highstar Incorporated",
        "connection": 3,
        "description": (
            "Tall, perfectly groomed, the height of corp haute couture -- except for mirrored wraparound "
            "sunglasses (over Zeiss cybereyes) and skin-tight silver gloves of mylar woven with metal that "
            "leave no fingerprints and carry the smartgun pad in her palm. A strong, assured voice that "
            "leaves no gap for questions. When the Teddy Boys come through the door her HK227 is simply "
            "in her hand. 'Isn't it obvious? If anybody learns about my edge, I won't be much use to my "
            "boss... or to you.'"
        ),
        "background": (
            "Held a drek-hot rep as a shadowrunner until about three years ago, when Teague offered a "
            "steady job paying more nuyen than a lifetime on the street; she 'sold out' and calls herself "
            "his 'personal expediter'. Takes pride in her corp status and wants to help her boss; learned "
            "through her own channels that he had hired runners, and has no inkling of his darker schemes "
            "-- Analyze Truth confirms every word she says at The Mattresses."
        ),
        "notes": (
            "Meets the team at The Mattresses on her own initiative to keep them working ('bring Allenby's "
            "killers to me'), sprints out the back door after the shootout, hands over Teague's card (LTG "
            "2206 (12-3582)). Covers the double's escape at the party with a few rounds through the lobby "
            "glass and leaves on her BMW Blitzen 2050 (hardpoint Ares MP LMG). Lives in the guest room at "
            "Vashon Heights and dies there beside Teague if it comes to that. Stats: B6 Q6 S5 C4 I4 W5, "
            "Ess 0.2, R5(11)+4D6; TR 6/4; Armed 5, Bike 6, Etiquette (Corporate) 4, (Street) 4, Firearms "
            "6, Negotiation 3, Psychology 2, Stealth 5, Unarmed 5; low-light cybereyes (thermographic, "
            "flare), hand razors, smartgun link, Wired Reflexes 3; armor jacket 5/3, HK227 S (smartlink, "
            "RC 2, two spare clips), survival knife, phone. GM fudges: she comes through the Teddy Boys "
            "unscratched."
        ),
    },
    {
        "name": "Jetblack",
        "role": "Angst-rock megastar who faked his death, became a vampire, and now secretly leads the Nightstalkers; Allenby's old friend, The Shadows' hidden protector",
        "archetype": "Rock Star / Vampire",
        "title": "Leader of the Nightstalkers; 'dead' founder of angst-rock; vampire (HMVV), Grade 0 initiate",
        "race": "Human (vampire)",
        "gender": "Male",
        "organization": "The Nightstalkers",
        "connection": 4,
        "description": (
            "A sensitive-looking youth apparently in his early twenties: tall, slim and slight, glossy "
            "black hair to his shoulders framing a pale, high-cheekboned, almost elven face, tailored "
            "black leather, noticeably enlarged eyeteeth, and the voice of a professional performer with "
            "an edge under the calm. First seen inside a cool blue magical nimbus in a pitch-dark "
            "dormitory. His slight build hides massive vampiric strength. Emotionally insecure to the "
            "point of paranoia about his secret; visibly happy for the first time when The Shadows "
            "embrace him."
        ),
        "background": (
            "From the same mean streets as Allenby, but his songwriting and performing far outweighed his "
            "business sense: a major Seattle star at eighteen when he signed with Caravan, then one of "
            "the first megastars -- Maria Mercurial, Concrete Dreams and The Shadows followed. He "
            "personally started the 'angst-rock' movement ('One Step Ahead of Death'; neurotics and "
            "manic-depressives love him) and his music was the sound of a man terrified of his own "
            "mortality. A fan who was a vampire offered the 'dark gift'; Jetblack took it to cheat death, "
            "realized too late what eternity would cost -- vampire killers, fans following him into the "
            "same mistake -- and chose the honorable course: faked his death in 'random street violence' "
            "(Lone Star found a badly trashed body) and went underground. 'Jetblack Lives!' is "
            "spraypainted all over town. Since then he has studied magic in the vague hope of reversing "
            "his condition. He let The Shadows know he was alive but never told them what he had become; "
            "they knew almost from the start."
        ),
        "notes": (
            "Feeds only on the willing Nightstalkers (never more than they can spare, never kills, never "
            "makes new vampires) and on unwilling victims only if they have tried to kill him -- Teague, "
            "for instance. Checks every statement with Analyze Truth, digs with Mind Probe, stuns rather "
            "than kills. Gives 'Unruly' to a team that levels with him; wants first shot at Allenby's "
            "killer; refuses muscle until convinced the band will not despise him, then brings ten riders "
            "to the reunion and twenty to Vashon Heights (night only). Stats: B2 Q3(x5) S12 C6 I4 W2, Ess "
            "10, Magic 7, R3, Init 5(11)+4D6; Armed 3, Etiquette (Corporate) 1, (Music Business) 2, "
            "(Street) 4, Firearms 3, Sorcery 6, Unarmed 2, Instrumental Music 6, Musical Composition 7, "
            "Singing 7. Vampire powers: Enhanced Physical Attributes, Enhanced Senses (hearing, smell), "
            "Essence Drain, Immunity (age, pathogens, poison), Infection, Mist Form, Regeneration, "
            "Thermographic Vision. Weaknesses: Allergy (sunlight, severe), Induced Dormancy (lack of "
            "air), Essence Loss, Vulnerability (wood). Spells: Sleep 3, Analyze Truth 4, Mind Probe 5, "
            "Increase Quickness +4 3, Chaotic World 2, Entertainment 5, Mana Barter 4. Gear: Browning "
            "Max-Power (laser, two spare clips), knife, lined coat. If he dies in the assault The Shadows "
            "mourn him as his own choice; if he lives he is an excellent contact and joins the band for one "
            "private jam -- all five on one stage for the first time -- with a simsense memento for the "
            "runners."
        ),
        "contact_skills": ["The Nightstalkers' muscle and eyes on the street", "Seattle music-business history and The Shadows"],
    },
    {
        "name": "Marli Bremerton",
        "role": "The Shadows' lead singer and main songwriter; the band's face to the world and the one who opens the door for Jetblack",
        "archetype": "Rock Star",
        "title": "Lead singer and songwriter, The Shadows",
        "race": "Human",
        "gender": "Female",
        "organization": "The Shadows",
        "connection": 3,
        "description": (
            "Tall, slender and beautiful, long dark hair, a voice 'too loud for a human throat' when she "
            "raises a glass across a crowded penthouse. Serious and direct with the runners; warm and "
            "quick to smile with an old friend. By consensus she handles most of the band's dealings with "
            "the outside world."
        ),
        "notes": (
            "Gives the toast at Wickingham's party; at the Richmond Highlands condo she looks Jetblack up "
            "and down and says 'It is you. I knew you weren't dead.' Knows nothing of the takeover ('we "
            "sure don't want to slave for Highstar') and can offer no help but money afterwards. Stats: "
            "B2 Q4 S3 C6 I4 W4, Ess 6, R4, 3/0; TR 2/2; Etiquette (Corporate) 3, (Music Business) 4, "
            "(Street) 5, Firearms 2, Musical Composition 6, Singing 7; voice modulation with increased "
            "volume, tonal shift and playback; armor clothing, Streetline Special hold-out."
        ),
        "contact_skills": ["Megastar access and music-business favors"],
    },
    {
        "name": "Joey Nightmare",
        "role": "The Shadows' lead synth-guitarist, cosmetically modified to look like a cross between a devil and an ape; a soft-spoken nice guy",
        "archetype": "Rock Star",
        "title": "Lead synth-guitar, The Shadows",
        "race": "Human",
        "gender": "Male",
        "organization": "The Shadows",
        "connection": 2,
        "description": "Heavy cosmetic modification makes him look like something between a devil and an ape; underneath he is soft-spoken and nice. Plays the 'synth-axe'.",
        "notes": "Stats: B4 Q3 S3 C5 I3 W2, Ess 3.8, R3, 3/0; TR 2/2; Etiquette (Street) 6, Firearms 3, Instrumental Music 7, Musical Composition 3; datajack 100 Mp, instrument control link; armor clothing, Streetline Special.",
    },
    {
        "name": "Sid Id",
        "role": "The Shadows' elven synth player, programmer and record producer; waist-length blond hair, gray eyes, rarely makes sense when he speaks",
        "archetype": "Rock Star",
        "title": "Synths and programming; producer of The Shadows' sessions",
        "race": "Elf",
        "gender": "Male",
        "organization": "The Shadows",
        "connection": 2,
        "description": "An elf with waist-length blond hair and gray eyes who rarely speaks, and makes little sense when he does. A terrific synth player and programmer; produces the band's recordings.",
        "notes": "Stats: B3 Q6 S1 C1 I2 W6, Ess 3.8, R3, 3/0; TR 2/2; Electronics 8, Electronics (B/R) 6, Instrumental Music 8, Unarmed 4; datajack 100 Mp, instrument control link; armor clothing, Streetline Special. The best electronics man in the book after Himem -- a possible favor for a friendly team.",
    },
    {
        "name": "Ernest Hawkins",
        "role": "The Shadows' second synth player, backing vocalist and light-show designer; lemur-eyed, sloth-slow, coaxes music out of trashed instruments",
        "archetype": "Rock Star",
        "title": "Synths, backing vocals and stage lighting, The Shadows",
        "race": "Human",
        "gender": "Male",
        "organization": "The Shadows",
        "connection": 2,
        "description": "Short and slight, close-cropped sandy hair and large soft eyes that make him look like a lemur; moves as slowly as a tree sloth unless something can be gained by moving fast. Knows nothing about synthesizer technology but has a gift for squeezing incredible performances out of the most trashed instruments.",
        "notes": "The Legwork table (p.51) calls him 'Emile Hawkins'; the Cast of Shadows and contents say Ernest. Stats: B2 Q5 S2 C4 I3 W4, Ess 3.8, R4, 3/0; TR 2/2; Armed 5, Etiquette (Corporate) 2, (Street) 5, Firearms 4, Instrumental Music 8; datajack 100 Mp, instrument control link; armor clothing, Streetline Special.",
    },
    {
        "name": "Tangent",
        "role": "Allenby's golden-haired assistant who knows the runners did not kill him, survives a hit, and hands them Wickingham's invitations before leaving town",
        "archetype": "Executive Assistant",
        "title": "Executive assistant / receptionist, Caravan Productions",
        "race": "Human",
        "gender": "Female",
        "organization": "Caravan Productions",
        "connection": 2,
        "description": (
            "Young, beautiful and ambitious, a mane of golden hair and impossibly blue eyes that look at "
            "strangers a little nervously ('Uh... yes? Can I help you?'). Comes across as an airhead and "
            "is nothing of the kind: intelligent, a good judge of character, and loyal to a crusty old "
            "curmudgeon she believes has a heart of gold. Nobody gets past her on the phone."
        ),
        "notes": (
            "Found Allenby dead at his desk; found the demo directory wiped; could not open his "
            "password-locked backup. Told Lone Star the runners left him alive and was not believed; "
            "someone then tried to kill her at home (GM invents the flashy details) and she is staying "
            "with friends, planning to leave Seattle. Phones the team with the first solid lead, describes "
            "Wallace perfectly, gave him nothing, and couriers Wickingham's party invitations. Asked "
            "about Jetblack: TN 3 and one automatic success. Stats: B3 Q4 S3 C6 I5 W4, Ess 4.7, R4; TR "
            "0/2; Computer 4, Etiquette (Corporate) 3, (Street) 3, Music Business 4; datajack 100 Mp, "
            "display link. Her own street network found the runners' number."
        ),
        "contact_skills": ["Seattle music-business gossip and who manages whom"],
    },
    {
        "name": "David Graves",
        "role": "Caravan's shy database clerk, a musician wannabe frightened of most things, runners included",
        "archetype": "Corporate Wage Slave",
        "title": "Database clerk, Caravan Productions",
        "race": "Human",
        "gender": "Male",
        "organization": "Caravan Productions",
        "connection": 1,
        "description": "A young man in inexpensive copies of high corp fashion with a datajack glittering in his forehead, who backs away from the reception desk when the runners walk in. Figures working in the business is one way to break in as a performer.",
        "notes": "Stats: B3 Q3 S2 C3 I3 W2, Ess 2.7, R3; TR 0/1; Computer 4, Etiquette (Corporate) 3, (Street) 1, Music Business 2; datajack 300 Mp, display link. Out of a job once Caravan folds.",
    },
    {
        "name": "Gnasher",
        "role": "Allenby's well-spoken troll bodyguard who escorts unwanted visitors out -- as hard as necessary",
        "archetype": "Bodyguard",
        "title": "Personal bodyguard to Lew Allenby, Caravan Productions",
        "race": "Troll",
        "gender": "Male",
        "organization": "Caravan Productions",
        "connection": 1,
        "description": "Better-spoken than most troll bodyguards the runners have met; calmly asks the team to leave, and if push comes to shove, shoves as hard as it takes. Summoned by a key on Allenby's computer.",
        "notes": "His appearance is the cue to leave, not a target; shooting him means PANICBUTTONs and Lone Star scooping up 'psychopathic murderers'. Stats: B11 Q5(7) S9(11) C3 I3 W4, Ess 1, R4(8)+3D6, 4/2; TR 5/3; Armed 4, Etiquette (Street) 3, Firearms 5, Unarmed 4; Muscle Replacement 2, Wired Reflexes 2; lined coat, Colt Manhunter (laser), survival knife.",
    },
    {
        "name": "Daniel Maynes",
        "role": "Highstar 'junior expediter' -- Teague's immaculate, inhumanly calm talker and knife-thrower; also the bodyguard who covers the double",
        "archetype": "Company Man",
        "title": "Junior expediter and bodyguard, Highstar Incorporated (personally loyal to Teague)",
        "race": "Human",
        "gender": "Male",
        "organization": "Highstar Incorporated",
        "connection": 2,
        "description": "Tall and slender, always perfectly groomed and exquisitely dressed, with a reputation for being constantly cool and inhumanly calm -- the perfect corporate expediter. Pins the Pig's coiffure to the Blue Flame's wall with a thrown knife without looking. 'Our employer will make that clear in time.'",
        "notes": "Stats: B6(7) Q4 S5 C5 I4 W5, Ess 2.5, R4(8)+3D6, 4/2; TR 5/3; Armed 5, Etiquette (Corporate) 5, (Street) 2, Firearms 5, Negotiation 5, Psychology 3, Stealth 2, Unarmed 3; Dermal Plating 1, Wired Reflexes 2; Browning Ultra-Power (laser), lined coat, survival knife. Knows neither the job nor the meet's purpose. Holds the penthouse doorway with Lester while the double escapes; briefed the double with the runners' pictures.",
    },
    {
        "name": "Lester Hatton",
        "role": "Highstar 'junior expediter' -- Daniel's stockier partner who takes center stage when the hard option is the only option",
        "archetype": "Company Man",
        "title": "Junior expediter and bodyguard, Highstar Incorporated (personally loyal to Teague)",
        "race": "Human",
        "gender": "Male",
        "organization": "Highstar Incorporated",
        "connection": 2,
        "description": "Slightly shorter and stockier than Daniel, sharing his partner's control and cool. Defers to Daniel with people and logic problems; when things get rough, Lester takes over.",
        "notes": "Stats: B6 Q5 S6 C6 I3 W5, R4(10)+4D6, 4/2; TR 5/3; Armed 6, Etiquette (Corporate) 4, (Street) 2, Firearms 6, Negotiation 1, Stealth 3, Unarmed 5; Dermal Plating 1, Smartlink, Wired Reflexes 3; Browning Ultra-Power (external smartlink), lined coat, survival knife, two throwing knives. Rides in back with the runners in the Phaeton.",
    },
    {
        "name": "Himem",
        "role": "Teague's 23-year-old wunderkind decker who murders by simsense: booby-trapped chips, modified Black-5 IC, and an ego that will not cut and run",
        "archetype": "Decker",
        "title": "Corporate decker, Highstar Incorporated (black-IC research)",
        "race": "Human",
        "gender": "Male",
        "age": 23,
        "organization": "Highstar Incorporated",
        "connection": 3,
        "description": (
            "An unpleasant young man, twenty-three years young, who can whip up nasty ice and hold his own "
            "in a decker dogfight. Matrix icon: a Three Musketeers-vintage fop wielding an epee that glows "
            "with the red light of a CO2 laser. Typically egotistical -- arrogance keeps him from "
            "recognizing a losing position; he would rather die than jack out."
        ),
        "background": (
            "Spent months working out how to kill people by electronics: a simsense recording carrying "
            "black IC that fires whenever it plays -- through a datajack it kills like any Killer program, "
            "faster on an amateur; through trodes it only hurts. Teague let him experiment on Allenby. "
            "Using Highstar's resources he hardwired a tap from an LTG line into Caravan's computer "
            "(a concealed SAN), planted the rigged demo, then deleted it and every other demo -- not "
            "knowing Allenby's hidden datastore had already backed them up."
        ),
        "notes": (
            "Watches Allenby's system through Trace and Report 7 ice; five actions after a report reaches "
            "SAN-1 he sends two copies of modified semi-autonomous Black-5 IC (one to CPU-1, one to DS-1) "
            "and dispatches the Highstar Special Ops van. In the Highstar system he fights toe-to-toe. "
            "Stats: B2 Q6 S2 C1 I6 W3, Ess 5.5, R6 (12 in the Matrix, +3D6); TR 4/3; Hacking Pool 12; "
            "Computer 4 (Software 6, Matrix Programming 8), Computer Theory 6, Computer (B/R) 5, "
            "Electronics 5. Fairlight Excalibur (MPCP 12, Hardening 5, Memory 500, Storage 1,000, Load "
            "100, I/O 50, increased response 3); Bod 6, Evasion 4, Masking 3, Sensors 6, Attack 7, "
            "Browse 3, Deception 3. His research (DS-4): 100 Mp on modified black IC worth 50,000 nuyen "
            "complete; 150 Mp of encrypted booby-trap notes (Intelligence 8, 24 hours) worth 200,000 -- "
            "less 10 percent a week. Dumping him is only a dump: he is alive and well and living in "
            "Seattle, burning with shame, plotting revenge on the team at the worst possible moment."
        ),
    },
    {
        "name": "Takahashi Yanaga",
        "role": "Highstar's well-entrenched president, whose chair Teague is trying to take; never appears",
        "archetype": "Corporate Executive",
        "title": "President, Highstar Incorporated",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Highstar Incorporated",
        "connection": 3,
        "description": "The well-entrenched president of Highstar, whom Teague could only oust with a major coup for the corp. Off-stage throughout; the man who signs off on the smear campaign and the hit teams once Teague is exposed.",
        "notes": "No stats. A natural face for Highstar/Mitsuhama if the runners try the 'public service' approach (20,000-nuyen retainer) -- or the blackmail approach (hit teams).",
    },
    {
        "name": "Blaze",
        "role": "Young elven Nightstalker on a Yamaha Rapier, new to the surveillance game, who leads the runners home to Jetblack",
        "archetype": "Ganger",
        "title": "Nightstalker go-ganger (up-and-coming)",
        "race": "Elf",
        "gender": "Male",
        "organization": "The Nightstalkers",
        "connection": 1,
        "description": "A leather-clad elf idling his Yamaha Rapier a few blocks back, ogling a passing blonde and pretending he was not watching you. Proud of his colors; the high collar hides two puncture wounds over his carotid, a 'badge of honor' he will die before explaining.",
        "notes": "Shadows the team on the gang boss's orders and never imagines being followed back. Captured, he admits the gang's name and offers to take the team to his leader (privately expecting his mates to cut them up); will not give the leader's name. Stats: B4 Q5 S3 C3 I3 W4, Ess 6, R4, 4/2; TR 4/4; Armed 3, Etiquette (Street) 3, Firearms 4, Stealth 2, Unarmed 3; Browning Ultra-Power (laser), knife, lined coat.",
    },
    {
        "name": "Blair Wickingham",
        "role": "Hot media producer with big-network connections whose Matthews Beach penthouse party is where The Shadows can be met",
        "archetype": "Media Producer",
        "title": "Media producer (connected to one of the big entertainment networks)",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": "A hot media producer with connections to one of the big entertainment networks; throws invitation-only parties in his Matthews Beach penthouse for rising stars, big names and sycophants, and sent Allenby a stack of invitations. Little else is known of him -- Tangent knows only the network connection.",
        "notes": "Not seen on-stage; his party is trashed by Teague's bodyguards and the Nightstalkers, and Lone Star would love to hang the damage on the runners. Media Producer archetype if stats are needed.",
    },
    {
        "name": "The Pig",
        "role": "115 kilos of ork fat, muscle and bad temper, heeled like a walking armory; Blue Flame regular pinned to the wall by Daniel's knife",
        "archetype": "Ork Thug",
        "title": "Regular at the Blue Flame Tavern",
        "race": "Ork",
        "gender": "Male",
        "connection": 1,
        "description": "Bloodshot eyes, an oily coiffure, a nasty smile when he sees shaikujin in gold watches walk into the Flame -- until a thrown knife sprouts from the wall a centimeter above his head, precisely on the centerline of his skull, and he takes a sudden interest in the tabletop graffiti.",
        "notes": "One-scene color; no stats. Handy as the Flame's resident bully for later nights.",
    },
    {
        "name": "Dr. Silvus Nyberg",
        "role": "University of Seattle physicist whose quantum-physics-and-metaphysics lab blew out a wing of the science building (August 2053 news)",
        "archetype": "Scientist",
        "title": "Professor of quantum physics, University of Seattle",
        "race": "Human",
        "gender": "Male",
        "organization": "University of Seattle",
        "connection": 2,
        "description": "Noted for his work in quantum physics and related metaphysical principles. An explosion originating in his labs leveled a large section of the main science building's physics wing late one August night in 2053; no injuries; neither he nor the University would comment on the cause.",
        "notes": "News-handout name (Seattle News-Intelligencer, August 25 2053, both endings). A hook: what does a quantum physicist studying 'metaphysical principles' blow up, and who wanted it?",
    },
    {
        "name": "Kyle Arigharu",
        "role": "Fuchi spokesperson who announced the Symbolic Processor AI milestone with fireworks (August 2053 news)",
        "archetype": "Corporate Spokesperson",
        "title": "Spokesperson, Fuchi Industrial Electronics (Seattle)",
        "race": "Human",
        "gender": "Male",
        "organization": "Fuchi Industrial Electronics",
        "connection": 2,
        "description": "The Fuchi voice behind the fireworks over the Seattle tower: the top-secret Symbolic Processor project, cornerstone of Fuchi's artificial-intelligence research, has passed a milestone -- but Fuchi 'does not anticipate bringing an AI system online at any time in the foreseeable future'.",
        "notes": "News-handout name (August 25 2053). The business world had expected Renraku to make the next AI breakthrough.",
    },
]

ORG_UPDATES = {
    "Mitsuhama Computer Technologies": {
        "notes_append": (
            "One Stage Before (August 2053): Highstar Incorporated, 'a big noise on the Seattle "
            "entertainment scene', is a Mitsuhama puppet company -- its accounting datastore shows a "
            "shell -- through which Mitsuhama is increasing its grip on the sprawl's music business. "
            "Highstar's executive VP Jonathon Teague murdered Lew Allenby of Caravan Productions to "
            "capture The Shadows and win the president's chair; if he had stolen Highstar's Rolls Royce "
            "Phaeton the operation would have been 'bumped up the line' to Mitsuhama. Once exposed, "
            "Highstar and Mitsuhama declared Teague a deranged renegade and 'loose cannon', mounted a "
            "smear campaign, and had him dead ('suicide') inside 48 hours behind plausible deniability. "
            "Blackmailing the corps over it earns hit teams; offering the proof as a 'public service' "
            "earns a 20,000-nuyen retainer. Did Mitsuhama know what Teague was doing? Unprovable."
        ),
        "allies_add": ["Highstar Incorporated"],
    },
    "Lone Star Security": {
        "notes_append": (
            "One Stage Before (August 2053): an anonymous tip plus manufactured evidence from Highstar "
            "had Lone Star issue warrants for the runners for Allenby's murder with the Rules of "
            "Apprehension waived -- dead or alive, and dead is easier. First contact is a Chrysler-Nissan "
            "Patrol-One with four helmeted officers (one a combat mage) opening fire from behind the car "
            "in the rain; a General Products COP with two more troopers at 15 turns, a second Patrol-One "
            "at 30, a SWAT Citymaster five minutes later. Trooper: B4 Q4 S4 C2 I3, R3; TR 3/2; Firearms "
            "3, Police Procedures 4; armor jacket, Beretta Model 70 SMG (laser, silencer), one CMDT combat "
            "gun per car. Combat Mage: B4 Q4 S3 C2 I4 W5, Magic 4; TR 4/3; Sorcery 4; Combat Sense 3, "
            "Manaball 4, Powerball 3. Patrol-One: H4/8, 60/180, B/A 3/2, gas-sealed firing ports. Five "
            "minutes to any PANICBUTTON. Later prefers to arrest (prisoners can be shot escaping); the "
            "team gets one escape chance on the way to the Lone Star building downtown. Proof of Teague's "
            "guilt gets the warrants recalled -- no apology, no restitution, and no brownie points. Lone "
            "Star also 'found' Jetblack's badly trashed body two years ago and never patrols Kobe Terrace "
            "Park hard enough to stop the night-time gang wars."
        ),
        "enemies_add": ["The Teddy Boys"],
    },
    "Knight Errant Security Services": {
        "notes_append": (
            "One Stage Before (August 2053): booked by Caravan Productions (through Allenby's assistant "
            "Tangent) for The Shadows' sold-out Kingdome show -- 'the only ones who can handle something "
            "this big' -- 'Knight Errant again'."
        ),
        "allies_add": ["Caravan Productions"],
    },
    "Fuchi Industrial Electronics": {
        "notes_append": (
            "One Stage Before (news handout, August 25 2053): 'Fireworks over Fuchi' -- a spectacular "
            "display over Fuchi Industrial Electronics announced a milestone in the top-secret Symbolic "
            "Processor project, cornerstone of Fuchi's artificial-intelligence research and commonly "
            "believed a failure until now. Spokesperson Kyle Arigharu: no AI system will come online in "
            "the foreseeable future. The business world had expected Renraku to get there first."
        ),
    },
    "Renraku Computer Systems": {
        "notes_append": (
            "One Stage Before (news handout, August 25 2053): the business world 'looked to Renraku "
            "Computer Systems to make the next AI breakthrough' -- and Fuchi's Symbolic Processor "
            "announcement beat them to the headline."
        ),
    },
    "Universal Brotherhood": {
        "notes_append": (
            "One Stage Before (news handout, August 25 2053): described as 'Seattle-based'; its soup "
            "kitchen was the current tenant of the St. Louis Moolah Temple, the Shriners' old landmark "
            "headquarters, when the building burned in a five-alarm fire preceded by an unexplained "
            "explosion (Bi-Star Police arson investigation)."
        ),
    },
    "University of Seattle": {
        "notes_append": (
            "One Stage Before (news handout, August 25 2053): 'Blast rocks Seattle U.' -- an explosion "
            "originating in the labs of Dr. Silvus Nyberg (quantum physics and related metaphysical "
            "principles) leveled a large section of the main science building's physics wing late at "
            "night; no injuries; no comment from Nyberg or the University."
        ),
    },
    "Tir Tairngire": {
        "notes_append": (
            "One Stage Before (news handout, August 25 2053): North American Basketball Association "
            "Commissioner Herb Bass again denied Portland's petition to host a team in the proposed 2055 "
            "expansion ('we all know what a disaster Portland hoops turned out to be'); Portland Sports "
            "Committee spokesperson Kevin Welch called it a cover-up of anti-elf prejudice."
        ),
    },
    "Seattle News-Intelligencer": {
        "notes_append": (
            "One Stage Before: Update-Net of Friday August 25 2053 (11:00, Local Seattle Stories). "
            "Headlines: Hurricane Ethelbert wrecks the DC-New York corridor, martial law; a mysterious "
            "blue slime several hundred kilometers across, first seen in the Pacific in May, washes up "
            "on New Zealand; All-Salish Nations Bank cuts hours and suspends international wire "
            "transfers amid failure rumors; seven insurers review cyberinsurance (individual policies "
            "next year); the 'Garden of Eden' fashion look; musicologist Sonora Quigley on 'Louie Louie'; "
            "NABA denies Portland again. Stories: the St. Louis Moolah Temple fire (Universal Brotherhood "
            "soup kitchen); 'Executive Suicide' -- Jonathon Teague of Highstar found dead in a Redmond "
            "rooming house amid evidence of illegal takeover attempts on Caravan (success ending) or "
            "'Gang War on Vashon Island' -- the 'Nightwalkers' repelled by Hard Corps (failure ending); "
            "Fuchi's Symbolic Processor fireworks; the blast at the University of Seattle; an ork-and-troll "
            "attack on Crusader Security's Chicago offices after metahuman deaths at the Byrne Projects."
        ),
    },
    "Rusted Stilettos": {
        "notes_append": (
            "One Stage Before: named with Crimson Crush as the 'more famous brethren' whose mayhem the "
            "low-profile Nightstalkers go-gang never matches."
        ),
    },
    "Crimson Crush": {
        "notes_append": (
            "One Stage Before: named with the Rusted Stilettos as the 'more famous brethren' whose mayhem "
            "the low-profile Nightstalkers go-gang never matches."
        ),
    },
    "Salish-Shidhe Council": {
        "notes_append": (
            "One Stage Before (news handout, August 25 2053): 'amid rumors of imminent failure, All-Salish "
            "Nations Bank has drastically reduced banking hours and suspended international wire "
            "transfers' pending a government auditors' report -- the book does not say which government; "
            "recorded here as the likeliest Salish institution."
        ),
    },
    "UCAS Federal Bureau of Investigation": {
        "notes_append": (
            "One Stage Before (August 2053): a special FBI task force investigates corruption and "
            "collusion in an entertainment industry 98 percent owned by a few megacorps; it hired "
            "contractor Darryl 'Ripper' Wallace (ex-Special Forces, ex-New York musician) to check false "
            "payola rumors around Lew Allenby of Caravan Productions. Caravan came up clean and the Bureau "
            "has no homicide jurisdiction -- FIIGMO, 'frag it, I got my orders' -- but Wallace wants "
            "Teague and Highstar down and will pull strings to clear runners who deliver. Wallace's "
            "superior is in Washington, DC; the Bureau keeps 'clones' to replace a dead contractor and an "
            "FBI Fast Response Team for anyone who holds one hostage."
        ),
        "leadership_add": [
            {"name": "Darryl Wallace", "title": "Contractor (entertainment-industry task force)", "notes": "'Just Wallace'; not on the official payroll."},
        ],
    },
}

LOC_UPDATES = {
    "Blue Flame Tavern": {
        "notes_append": (
            "One Stage Before (August 2053): the runners' 'regular table' when they are tap city; the "
            "Chinaman behind the bar rearranging grime on a mug and refusing to meet their eye because "
            "his information network already knows they are broke. Two Highstar suits in gold watches "
            "and diamond earstuds walk in, pin the ork regular 'the Pig' to the wall with a thrown knife, "
            "and drop a 5,000-nuyen credstick on the table: a Rolls Royce Phaeton is idling at the curb."
        ),
    },
    "The Kingdome": {
        "notes_append": (
            "One Stage Before (August 2053): venue for The Shadows' single Seattle show -- 65,000 tickets "
            "(hundreds counterfeit) sold out in one hour, ten dead and fourteen missing at ticket offices "
            "across the plex, 250 nuyen a scalped nosebleed seat and a thousand or two for a good one. "
            "Booked by Caravan Productions with cancellation insurance, Knight Errant security, and no "
            "second show. The success ending gives the runners two tickets each."
        ),
    },
    "The Space Needle": {
        "notes_append": (
            "One Stage Before: The Mattresses, the corps' members-only neutral-ground club, is directly "
            "beneath it -- a stairway below street level on Denny Way beside Tam's Under the Needle."
        ),
    },
}

NPC_UPDATES = {
    "The Chinaman": {
        "notes_append": (
            "One Stage Before (August 2053): behind the Blue Flame's bar when Highstar's expediters come "
            "for the runners; his information-gathering network 'would put the FBI and the CIA to shame' "
            "and he already knows the team is broke, so no free round. A natural source for legwork on "
            "Caravan, Highstar, the Nightstalkers and Hard Corps."
        ),
    },
    "Maria Mercurial": {
        "notes_append": (
            "One Stage Before: Jetblack's biography names Maria Mercurial among the first megastars who "
            "followed him ('Maria Mercurial, Concrete Dreams, and The Shadows'); Allenby considers The "
            "Shadows' Kingdome show bigger than anything she ever played in Seattle."
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
**1. Allenby's computer / Caravan Productions system** (map p.32). Officially NOT on the Matrix; the
only way in is physical (Allenby's desk, datajack or keyboard as a tortoise). Himem hardwired a tap
from an LTG line, giving it a concealed SAN into Highstar. Two hidden datalines, each revealed only by
a password spoken as a system command: "Unruly" (CPU-1 to DS-2) and "Charon" (CPU-1 to SAN-1).
Tortoise utilities on the box: Bod 3, Sensors 2, Analyze 1, Evaluate 1, Browse 2, Decrypt 2.

| Node | Function | Rating / IC |
|---|---|---|
| CPU-1 | System CPU | Orange-3, Blaster 3, Trace and Report 7 (report vanishes down the hidden line to SAN-1 after 1 turn; destroy it first) |
| SPU-1 | Graphics / numeric co-processor array | Green-2, Access 2 |
| DS-1 | Primary datastore: Caravan business records; the demo directory Himem wiped | Orange-3, Scramble 2, Blaster 3, Trace and Report 7 (report goes to CPU-1 then SAN-1; 2 turns to kill it) |
| DS-2 | Concealed datastore ("Unruly"): daily bit-for-bit backups of DS-1, Allenby's diary (100+ Mp, five hours; keywords Shadows / Nightstalkers / Jetblack / Teague), and six backed-up simsense demos (~4 min each) -- one is the booby trap | Orange-3, Scramble 2, Blaster 3 |
| I/OP-1 | Keyboard and terminal | Green-2, Access 2 |
| I/OP-2 | Datajack connection | Green-2, Access 2 |
| SAN-1 | Hidden SAN ("Charon"); second dataline onward to Highstar SAN-1 | Orange-3 |

Notes: Perception (4) on meeting the Trace and Report 7 ice reveals it was added to the original
security. Playing the rigged demo = combat with Killer 4 black IC in an Orange-3 node: from a cyberdeck,
normal; jacked straight into Allenby's box, only its tortoise utilities; through a trode rig, no
fighting back, Willpower (4) to jack out, reduced damage. Five actions after a successful trace Himem
drops two modified semi-autonomous Black-5 IC into SAN-1, one to CPU-1 and one to DS-1; they leave when
the decker is down or out, and only white IC remains afterward. Perception (4) on seeing black IC
emerge from the CPU "wall" reveals a second hidden dataline. Physical response: Highstar Special Ops in
10 minutes (7 on the second run).

**2. Highstar Incorporated corporate system** (map p.36-37). Reached from Allenby's SAN-1; SAN-2 is the
public Matrix door. Highstar is a shell company and DS-1 says so. Himem defends it in person and will
not retreat.

| Node | Function | Rating / IC |
|---|---|---|
| SAN-1 | Link from Allenby's system | Orange-3 |
| SAN-2 | Matrix access | Orange-4, Killer 3, Tar Pit 3 |
| CPU-1 | Main CPU | Orange-3, Tar Baby 4, Barrier 5 |
| SPU-1 | Newly installed; manages the Highstar-Caravan link | Red-3, Blaster 4, Trace and Burn 4 |
| SPU-2 | Accounting processor | Orange-3, Barrier 4 |
| DS-1 | Basic accounting: reveals Highstar is a shell | Orange-3, Barrier 3, Scramble 3 |
| I/OP-1 to 3 | Accounting terminals and datajacks | Green-3, Barrier 2 |
| SPU-3 | "Executive" SPU, almost exclusively Teague's | Red-3, Barrier 4, Killer 3 |
| DS-3 | Teague's Caravan takeover files plus a PI report on Allenby's blackmail vulnerability; motive not proof; 25 Mp, 10,000 nuyen to the right buyer | Red-2, Barrier 3, Scramble 3, Black-4 |
| I/OP-5 | Teague's office terminal | Red-2, Barrier 4 |
| CPU-2 | Back-up CPU; mainly supports Himem's research in SPU-6 | Orange-3, Tar Baby 4, Barrier 5 |
| SPU-4 | Traffic between CPU-1 and CPU-2 | Orange-3, Barrier 3 |
| SPU-5 | Personnel | Orange-4, Barrier 4, Trace and Burn 3, Killer 3 |
| DS-2 | Personnel data, including Teague's home address (Vashon Heights, north tip of Vashon Island) | Red-2, Barrier 3, Scramble 3, Blaster 3 |
| I/OP-4 | Personnel terminal | Orange-3, Barrier 3 |
| SPU-6 | Himem's research processor | Red-4, Barrier 4, Trace and Burn 3, Tar Pit 3, Trace and Report 8, Killer (Black-4) |
| DS-4 | Himem's modified-black-IC research (100 Mp, 50,000 nuyen as a set, 1,000 per 10 percent) and encrypted booby-trapped-simsense notes (Intelligence (8), 24 hours; 150 Mp, 200,000 nuyen; 2,000 per 10 percent); value drops 10 percent a week | Red-4, Barrier 4, Scramble 4, Trace and Report 8, Black-5 |
| I/OP-6 | Datajack in Himem's research lab | Red-3, Barrier 5 |
| SPU-7 | Manages SAN-2; monitors all Matrix traffic | Orange-4, Barrier 6, Tar Baby 3 |

Notes: an external alert or a successful Trace and Report brings Himem (Fairlight Excalibur, Attack 7,
Hacking Pool 12) into the system toe-to-toe and the Special Ops van back to Caravan in seven minutes.
Fencing the paydata is a trap -- Teague has told the shadows the team pays more dead.

**3. Teague's compound security computer** (map p.43). Not on the public Matrix: SAN-1 is
dial-out-only and calls Hard Corps headquarters on active alert. Entry is the guard-shack terminal
(I/OP-1) or the concealed terminal in Teague's den. Beating it shuts down most of the house systems.

| Node | Function | Rating / IC |
|---|---|---|
| CPU-1 | Controls the entire system | Orange-4, Barrier 4, Blaster 4 |
| SPU-1 | CPU to SAN-1 communications | Orange-2, Barrier 3 |
| SPU-2 | Seawall motion detectors | Orange-4, Barrier 3 |
| SPU-3 | House lasers and pressure pads | Orange-4, Barrier 3, Blaster 3 |
| SAN-1 | Dial-out-only; auto-calls Hard Corps HQ | Orange-4, Barrier 3 |
| I/OP-1 | Guard-shack terminal | Orange-4, Barrier 4, Blaster 3 |
| I/OP-2 | Terminal in Teague's study | Orange-4, Barrier 3 |
| SM-1 | Seawall motion-detector system (Rating 8, 10 m) | Orange-4, Barrier 4, Blaster 2 |
| SM-2 | Two-phase laser system on the house perimeter (doors, windows, patio) | Orange-4, Barrier 4, Blaster 2 |
| SM-3 | Pressure-pad system in the main hallways (40 kg) | Orange-4, Barrier 4, Blaster 2 |

**4. Teague's notebook computer** (den, p.44-45) -- a stand-alone portable, Green-2, password security
equivalent to Barrier 2; jack in with the right interface hardware or run it as a tortoise. Contains
the takeover files and Himem's installation notes: the proof. Not worth a host of its own.
"""

NOT_BUILT = """
- **Teague's double** (only knows his original is in hiding; briefed with the runners' pictures),
  **the Phaeton driver / rigger** (VCR 2, Car 4 / Phaeton 8, Beretta 200ST), **Teague's Greek-declaiming
  wage mage**, **the Highstar combat mage**, **Highstar Security Operatives**, **the seven park
  guards** -- stat blocks on the Highstar org row.
- **Teague's cook** (Pedestrian archetype, butcher knife, hides under the sink), **Hard Corps guards,
  troll animal handlers, dogs and riggers**, the **Force 4 earth elemental** -- on the Hard Corps and
  compound rows.
- **The Mattresses' elf maitre d'** and its security team; **Wickingham's lobby guards, interior guards,
  serving staff and twenty-five guests**; **Lone Star troopers, combat mages and SWAT** -- on the
  location and Lone Star rows.
- **The ambush team** at Pier 16 (three snipers, a street mage, five street samurai) -- on the
  warehouse row; hired through untraceable "channels".
- **Tam's Under the Needle** (the business beside The Mattresses' stairway; nothing else is said of it),
  **Teague's city home** (address never given, "guarded by a small army"), **the Redmond rooming house**
  where Teague's body turns up, **the hydroplane-ferry terminal** on Vashon Island and its mainland dock
  south of Lincoln Park, **the Lone Star building downtown**.
- **Concrete Dreams** (the only megastar act Allenby never managed), **Adam Vikk**, **Elvis** and **Jim
  Morrison** -- name-drops. **The vampire fan** who infected Jetblack; **the friend who modified
  Allenby's hardware**.
- News-handout names: **Herb Bass** (NABA commissioner), **Kevin Welch** (Portland Sports Committee),
  **Sonora Quigley** (musicologist), **the Moolah Shriners** and the **Moolah Temple** (St. Louis),
  **Bi-Star Police**, **All-Salish Nations Bank**, **Crusader Security** (Chicago) and the **Byrne
  Projects** riot, **Hurricane Ethelbert**, the **Pacific blue slime**. Reporters' bylines are FASA staff
  jokes (N. Findley, C. Kubasik).
- **Sprawl Sites archetypes** used for maps: Mid-size Restaurant (The Mattresses), Large Residence
  (Wickingham's penthouse; the Richmond Highlands condo), Fire Station (the Nightstalkers).
"""

PLAY_NOTES = """
- A decision-tree frame-up: the runners are Class A murderers by the end of Day 1 and every phone call
  leads to trouble. Keep Teague alive and unreachable until the end (the double at the party), and keep
  the Highstar building impregnable -- the only way in is Matrix, via Allenby's tapped SAN.
- Needs a decker and a mage. Three Matrix runs escalate: Allenby's box (tortoise-capable), Highstar
  (Himem in person), the compound security computer (shuts down lasers and pressure pads).
- The Teddy Boys are a genuine coincidence; do not let the players build a theory on them. Wallace is
  odd on purpose -- "let them wonder who the frag that guy was."
- The toast is the key to the climax: "to those who are no further away than sunset" means The Shadows
  know Jetblack is a vampire. Intelligence (4) to recall it if the players are stuck. Jetblack meets at
  night only.
- Fencing Highstar paydata is suicide while Teague's bounty stands: every fixer meet becomes an ambush
  of escalating lethality until the team takes Teague down.
- The final assault is a movie: 50-70 guns on the grounds, but only shots aimed at the runners get
  rolled; the Nightstalker diversion happens off-stage. Get in and out before the Yellowjacket (10 min)
  and the Stallion / Citymaster (15 min).
- Karma: dump Himem 1; evidence in the Highstar system 1; find the booby-trapped simsense 1; the
  Jetblack / Shadows reunion 3; defeat Teague yourselves 2 OR let his corp eliminate him 1; the proof in
  the notebook 3.
- Payoff: Teague never pays. The Shadows pay 100,000 nuyen plus two Kingdome tickets each; Highstar /
  Mitsuhama may pay a 20,000 "public service" retainer; blackmail = hit teams. Lone Star recalls the
  warrants without apology.
- Loose ends: Himem alive and humiliated; Wallace as a future Johnson; Jetblack and The Shadows as
  contacts (and a bootleg jam-session simsense the team must not sell); Meta if she survived; Hard
  Corps' opinion of whoever hit their showpiece; Tangent gone from Seattle; a hundred-thousand-nuyen
  band with no manager.
"""
