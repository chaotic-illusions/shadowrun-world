# SRM 01-06 Lost and Found (FanPro/WizKids, 2005, SR3) -- campaign order #49. Puyallup (Al's
# Stuffer Shack at 3rd and West, the Sidhe Devils' burnt-out garage, Tarn's neighborhood), with
# Aztechnology's pyramid and Huitzilopochtli Plaza in Downtown and a Telestrian pickup a mile past
# the Salish border.
# SETTING NOTE: this is a SEATTLE adventure, not a Denver one, and it is Shadowrun Third Edition,
# not SR4. Shadowrun Missions Season 1 (the "Rose Croix story arc", per the 01-06B cover) runs in
# the Seattle metroplex: the Preparing the Adventure section cites New Seattle "for an overview of
# the Seattle Metroplex during the 2060s", every scene is in Puyallup, and the getaway runs for the
# Salish border and Tir Tairngire. The campaign only relocates to Denver in later seasons. Every
# location row is therefore city "Seattle".
# Dating: no in-world date is printed. The book is written for SR3, cites New Seattle and The Sprawl
# Survival Guide for "daily life in the 2060s", and was published in 2005, so the campaign year is
# 2064 (matching SRM 00-01 Mission Briefing and SRM 01-01 Double Cross). The adventure itself runs
# across a single night: the comm rings at 0215, the meet is at 0315, the car must be back by 0500
# (0600 for half pay), the gang rolls at 0530 and the Aztechnology board meets at the testing track
# at 0800.
# Book editing inconsistencies, noted on the affected rows:
#   * the prototype is the "Amanecer 5000" in the Plot Synopsis, the karma table and the vehicle
#     stat block, and the "Amenecer 5000" in Lucien's briefing and in Following the Leader;
#   * the Introduction says New Seattle covers "the downtown area where this scenario takes place",
#     but every scene except the pyramid is in the Puyallup barrens;
#   * Bennett finds and deactivates the car's tracking beacon at Al's, yet Heather later says she
#     knows the car has a tracking device and is not sure why it has not been activated;
#   * the Debugging note reads "They will be unable to turn the car in to either Lucien" -- the
#     sentence is truncated and the second option (the Tir) is missing;
#   * Al Preswick is "a big Orc" and the gangers are "elf posers" with cosmetic surgery, so the
#     book uses Orc where the line normally prints ork;
#   * Lucien's deadline is 0500 with a 0600 grace, but the corporate legwork puts the board meeting
#     at 0800 -- three hours of slack the briefing never mentions;
#   * the 01-06B Player Aids package opens "This is the Player Aids package for the Shadowrun
#     Missions adventure entitled The Gambler", copy-pasted from SRM 01-04;
#   * Lucien's contact card blanks his Body, Quickness, Strength, Essence and Reaction ("?") and
#     drops the mnemonic enhancer that the adventure text gives him.
# Cross-spec note: Aztechnology, Aztlan, Tir Tairngire, Salish-Shidhe Council, Lone Star Security,
# Seattle Mafia and the Ancients already exist and are updated, not re-created; likewise the
# Aztechnology Pyramid and the Salish-Shidhe Border Post.
# Source text: docs/Adventures/text/SRM01-06A_Lost_and_Found.txt (23 pages) and
# docs/Adventures/text/SRM01-06B.txt (player aids, 7 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "SRM 01-06 Lost and Found"
ORDER = 49
SOURCE = "SRM01-06A_Lost_and_Found.pdf, pp. 3-23; SRM01-06B.pdf (Player Aids), pp. 1-7"
YEAR = "2064"

SYNOPSIS = """
At 23:00 an Aztechnology engineer named **Edmundo Castellian** watches the security tape for the
fifth time and understands that he is a dead man. The tape shows him walking through the
underground parking deck, saying hello to the guard, driving out in a car with superconductive black
paint glowing white as the engine idles, and showing his pass on the way past. Billions of nuyen of
Aztechnology money, gone, and whoever took it wore his face perfectly -- no extra wrinkles around
the eyes, the voice pattern an exact match. "With that sort of perfection it could only be magic."
The **Amanecer 5000**, the prototype he is due to unveil to the board of directors at sunrise, is a
multi-billion-nuyen gap in the middle of his work floor, and once it is missed nobody will let him
protest his innocence; security will simply walk him to the lower labs. So he calls the brother he
has not spoken to in years.

The thief is **Jackson Rollo**, Edmundo's own lead assistant, who wore his boss's face out of the
building and means to "recover" the car in the morning and be the hero of the board meeting.
Promotion is a cutthroat business at Aztechnology. To park the car where nobody would look for it he
handed the keys to **Heather**, the elf dog shaman who leads a Puyallup gang of elf posers called
the **Sidhe Devils**, and told her a mole inside Aztech wanted the corporation's newest toy to reach
the right hands. She agreed to take it to **Tir Tairngire**. Rollo never imagined a gang that small
could actually get it across the border in time -- and Heather, once **Bennett** popped the hood
and found the engine, scrapped the plan to strip it and started mapping a route north.

Edmundo's brother **Eduardo "Lucien" Castellian** is a fixer with a bullet scar through his cheek, a
hatred of Aztechnology that goes back to the death of his mother and the taking of his father, and a
life debt to the brother who nursed him back from the alley where an Aztlan death squad left him.
He puts a call on the Shadowlands board at two in the morning, pays a heavy finder's fee, and meets
the runners in a stripped black van outside **Al's Stuffer Shack** at 3rd and West at 03:15: 5,000
nuyen each (1,000 up front) for the car undamaged by 05:00, half that by 06:00, 1,500 more each for
the thief. He is unarmed and unarmored and does not much mind if the team kills him.

Al's security cameras and the ork owner's memory give the team Heather, Bennett and the gang colors.
The garage is a dead three-pump filling station with a collapsed roof, two nervous sentries walking
parallel circuits, three watchers orbiting at forty meters and the glowing car up on the one working
lift. Heather casts Analyze Truth and negotiates: she will sell the car back for 15,000 nuyen, she
will hand it over rather than see her punks tortured by Aztech, and she will die before she lets them
be taken. The moment the runners settle with her -- whichever way -- an amplified voice announces
**Lt. Jose Ramirez of the Aztlan Jaguar Guards**, thirty seconds and then gas grenades, because
Rollo has hedged his bet. The runners can hand the car to Lucien, run it to the Tir with Heather and
her wolf-shaman mentor **Tarn**, or sell it to any AAA that dares and earn Aztechnology as an enemy.
"""

TIMELINE = """
- **23:00, the night before** -- Edmundo Castellian finds the theft on the security tapes, hacks the
  security database to confirm it, and phones his brother Eduardo. The car left the parking deck
  earlier that evening.
- **Earlier that night** -- Rollo, in a hat and coat that beat the cameras, hands Heather the keys in
  Al's Stuffer Shack parking lot and walks out of shot into a waiting cab. Bennett pops the hood,
  finds the Aztechnology GPS beacon, tears it out and drops it in the lot; the two drive off in a car
  glowing like a spotlight.
- **02:15** -- the comm rings. A familiar face with a familiar smile: a job. The team has an hour,
  enough for a few phone calls about Lucien (Legwork).
- **03:15** -- the meet at 3rd and West, Puyallup, outside Al's. Perception (hearing) TN 4 notices
  that the normal night noise of the barrens is missing -- the gangers are sequestered in their
  garage. Briefing, 1,000 nuyen each up front.
- **03:15-05:30** -- Al's Stuffer Shack (cameras, the credstick scanner, the broken beacon in the
  lot), legwork on the Sidhe Devils (Etiquette Street 6, minus 2 with Ancients contacts) and the
  garage blueprints (Computer TN 4+TR, TN 3+TR through city hall; one success in an hour, ten
  minutes off per extra success).
- **05:00** -- Lucien's deadline. Full pay, 5,000 nuyen each.
- **05:30** -- if nobody has interfered, the Sidhe Devils finish mapping their route; Heather calls
  the gang to mount up and they are on the road inside two minutes, with a car that can outrun almost
  anything. Heather is also waiting on a callback that will not come until 05:30.
- **06:00** -- the late deadline. Half pay, 2,500 nuyen each.
- **The moment the garage is resolved** -- the Jaguar Guards announce themselves and give thirty
  seconds before the gas grenades.
- **08:00** -- the Aztechnology board of directors meets at the testing track to see the Amanecer
  unveiled at sunrise. Marketing thought it would be symbolic.
- **After** -- the fixer who set the run up gets quiet thanks from Aztechnology and is bumped from
  connection 1 to 2; teams who sell the car elsewhere collect a Corporate Favor and Enemy:
  Aztechnology.
"""

ORGS = [
    {
        "name": "Sidhe Devils",
        "org_type": "go-gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "A burnt-out three-pump gas station in the Puyallup barrens",
        "summary": "A small Puyallup gang of elf posers -- five to seven surgically elf-ified humans behind a real elf dog shaman -- who accidentally end up holding a multi-billion-nuyen Aztechnology prototype",
        "description": (
            "'A small gang of elf posers in Puyallup.' Five to seven members, usually five guys and "
            "two girls, all of them humans who have paid for cosmetic surgery to give themselves a "
            "more elf-like appearance, riding stolen and stripped Harley-Davidson Scorpions in synth "
            "leathers. They hang around the more rundown parts of Puyallup, leave the locals alone "
            "for the most part, and stick to petty vandalism and theft; even Al Preswick, who does "
            "not think highly of them, allows that as gangers go they are not all that bad. They "
            "carry nothing heavier than pistols by reputation -- in fact AK-97 smartguns -- and "
            "their base is a burnt-out garage whose address any decent street contact can give up. "
            "What lifts them out of the ordinary is their leadership: a genuine elf, the dog shaman "
            "Heather, who sees Tir Tairngire through rose-colored glasses and keeps trying to make "
            "the elven nation acknowledge her existence, and her boyfriend Bennett, a real mechanic "
            "with real skills. The gang is loyal to her and she is fiercely loyal back."
        ),
        "leadership": [
            {"name": "Heather", "title": "Leader; dog shaman and talismonger", "notes": "The only real elf in the gang; would rather die than see her punks taken by Aztechnology."},
            {"name": "Bennett", "title": "Heather's boyfriend and the gang's wrench", "notes": "Found and killed the car's GPS beacon; recognized what the engine was."},
        ],
        "notes": (
            "Typical ganger (5 guys, 2 girls): B4 Q4 S3 C3 I2 W3, Ess 5.0, Reaction 5, Init 3+2D6, "
            "Combat Pool 4, Karma 1, Pro 1/Average. AK-97 SMG smartgun (6M) with smartlink and 2 "
            "clips, synth leathers 0/1, Boosted Reflexes 1, cosmetic surgery for the ears and face. "
            "Bike/Harley Scorpions 4/6, Bike B/R 2, Stealth 3, Unarmed 4, SMG/AK-97 3/5. Their bikes "
            "are stolen, stripped, in poor repair and would fence for 5,000 nuyen for the lot. "
            "Legwork: Etiquette (Street) 6, reduced by 2 with Ancients contacts, six items deep -- "
            "gang, turf, size and leadership, weapons and the garage address, Heather's altruism and "
            "her attempts to get the Tir's attention, and finally that she is a dog shaman. In play "
            "the sentries are punks who have not been blooded, with no shoot-first instinct, and "
            "will take a non-threatening visitor to Heather. If more than half of them go down, or "
            "Heather and Bennett go down, the rest flee -- but Heather and Bennett will not go down "
            "at all if they believe Aztechnology is taking them alive. Aftermath: if the runners help "
            "her escape, Heather takes the whole weight of Aztechnology's enmity herself and tells "
            "everyone but a select few that the Sidhe Devils overpowered the runners and got away "
            "clean."
        ),
        "enemies": ["Aztechnology"],
    },
    {
        "name": "Aztlan Jaguar Guards",
        "org_type": "military unit",
        "tier": 5,
        "headquarters": "Aztlan and Aztechnology extraterritorial holdings; in Seattle, Huitzilopochtli Plaza",
        "summary": "Aztlan's elite troops, called in by Jackson Rollo to take the prototype back from a gang of teenagers -- gas first, then rifle fire on anyone who leaves cover",
        "description": (
            "The Jaguar Guards are Aztlan's elite soldiers, and Aztechnology can put a squad of them "
            "on a Seattle street at five in the morning on a phone call from a mid-level assistant "
            "with the right story. They arrive without warning, surround the objective, and announce "
            "themselves through an amplifier: 'This is Lt. Jose Ramirez of the Aztlan Jaguar Guards. "
            "We have the garage surrounded. We have reason to believe that you have a piece of stolen "
            "corporate equipment inside with you. Please throw down your weapons and exit with your "
            "hands up. You have 30 seconds before we attack.' They cannot be bribed. They can, just "
            "possibly, be dazzled with corporate politics or talked into a phone conversation with "
            "somebody who outranks the man who called them, but a firefight is the likely result."
        ),
        "leadership": [
            {"name": "Lt. Jose Ramirez", "title": "Lieutenant commanding the recovery squad", "notes": "Tipped off by Jackson Rollo; gives thirty seconds and then opens with gas."},
        ],
        "notes": (
            "Troopers (2+TR): B5 Q6 S6 C3 I5 W6, Ess 1, Reaction 5(9), Init 9+3D6, Combat Pool 8, "
            "Karma 2, Pro 4/Veteran. Ares Alpha assault rifle (8M), Neurostun VIII grenades (6S "
            "Stun), medium security armor 6/5, Smartlink 2, Wired Reflexes 2, datajack, 2 clips, 8 "
            "grenades, low-light vision. Armed Combat 4, Demolitions 3, Etiquette (Corporate) 3, "
            "Assault Rifles 6, Stealth 4. Combat shaman (only if TR is above 2): B3 Q4 S2 C1 I5 W5 "
            "Magic 6, Ess 6, Reaction 4, Init 4+1D6, Combat Pool 7(9), Spell Pool 8, Karma 2, Pro "
            "4/Veteran; Browning Max Power (9M), armor jacket 5/3, two Force 2 sustaining foci "
            "(Armor 4 successes, Combat Sense 4 successes); Conjuring 3, Etiquette (Corporate) 4, "
            "Pistols 3, Sorcery 6, Stealth 4; Armor 4, Mana Bolt 4, Combat Sense 4, Stun Ball 5. The "
            "shaman allocates all available sorcery dice to spell defense unless the GM decides "
            "otherwise. Tactics: gas grenades into the garage first, then pick off anyone who leaves "
            "the cover of the building. For a full effect the GM may add an Ares Citymaster and a "
            "rigger. If the runners surrender the car to them the run is effectively over -- the "
            "team is taken prisoner to Huitzilopochtli Plaza for a grand inquisition by Aztech "
            "security and earns roleplaying karma only."
        ),
        "allies": ["Aztechnology", "Aztlan"],
    },
]

LOCATIONS = [
    {
        "name": "Al's Stuffer Shack",
        "location_type": "convenience store",
        "city": "Seattle",
        "district": "Puyallup",
        "security_level": "No Security / Barrens",
        "summary": "The Puyallup Stuffer Shack at 3rd and West where Rollo handed over the keys, where Lucien holds the meet, and whose cameras and credstick scanner hold everything the team needs to start",
        "description": (
            "A five-meter neon sign of a fat man shoving a pie into his mouth dimly lights the corner "
            "of West and Third in Puyallup. All but one of the streetlights are dark, victims of "
            "vandalism, stray gunfire and neglect, and the blue light of the sign blends with the "
            "shadows from the working streetlamp to make the place seem darker than its unlit "
            "surroundings. The building itself is a typical fast food joint with a drive-through, the "
            "majority of its walls bulletproof Plexiglas at Barrier rating 4, its doors the same "
            "Plexiglas sealed with rating 3 maglocks. It is obviously closed for the night; the only "
            "light inside comes from behind the closed kitchen door, where the owner is still working. "
            "Security cameras inside cover the restaurant and the parking lot. The lot is where the "
            "corporate suit handed a set of keys to an elf ganger, where Bennett popped a hood, and "
            "where the black van waits under the one working streetlamp."
        ),
        "notes": (
            "Perception (4) spots the cameras; Electronics (3) reviews the footage. The important part "
            "of the tape: Heather accepting keys from a corporate suit who then walks out of frame, "
            "Bennett popping the hood and rummaging briefly, and the two driving off in the glowing "
            "car. Stills of the car, Bennett and Heather can be pulled easily once found; Rollo cannot "
            "be identified at all, because his hat and coat beat every angle. Asking Al or an Area "
            "Knowledge / Gang Identification (5) test identifies the colors as Sidhe Devils. The suit's "
            "personal information is still in Al's rating 3 credstick scanner, which the runners must "
            "find a way to hack without Al noticing. Perception (6) in the parking lot turns up a "
            "six-inch-square piece of broken electronics stamped with the Aztechnology logo; "
            "Electronics (4) identifies it as a GPS locator beacon, forcibly removed and clearly dead. "
            "Running the car's plates gives Edmundo Castellian and an address in Huitzilopochtli Plaza. "
            "Pushing the envelope, either the local Mafia handles Al's security -- Capo Maurice "
            "'Butcher' Bigio's limo and bodyguards pull into the drive-through, because he has a thing "
            "for Al's soyburgers, and they will be very disappointed if the runners have hurt someone "
            "under their protection -- or Al keeps the grill running for any Lone Star officer who "
            "feels like stopping by. If nobody on the team has Electronics they must get Al's help or "
            "carry the security data to another contact, which burns time this scenario cannot spare."
        ),
    },
    {
        "name": "The Sidhe Devils' Garage",
        "location_type": "gang territory",
        "city": "Seattle",
        "district": "Puyallup",
        "security_level": "No Security / Barrens",
        "controlling_org": "Sidhe Devils",
        "summary": "The burnt-out three-pump filling station where the gang has the Amanecer up on the one working lift, guarded by two green sentries and three watchers",
        "description": (
            "A simple three-pump garage left over from the 1950s. The pumps are dry, most of the "
            "equipment has long since rusted out and the place is in bad repair, but it still keeps "
            "most of the rain off. It is a cashier box and office connected to a repair bay: the "
            "office is 7m by 7m by 2m with a 2m by 2m non-working bathroom in the northeast corner "
            "and an empty window frame where the whole southern wall should be; the garage is 12m by "
            "12m by 10m and shares half of the eastern wall with the office. The garage doors are "
            "missing entirely and the roof has collapsed across a 2m by 4m stretch along the western "
            "wall. One of the car lifts has been jury-rigged back into service, and the Amanecer hangs "
            "on it, its driver-side window open, Aztechnology logos all over the interior and none at "
            "all on the outside. The gang's Harley-Davidson Scorpions are parked out front. Everyone "
            "inside is tense and frightened."
        ),
        "notes": (
            "Layout in play: a woman stands in the office near the open window frame; two men patrol "
            "the north and south sides on parallel routes, so if they fail to meet at the ends of the "
            "building they know something is wrong and raise the alarm; the rest of the gang is in the "
            "bay with Heather and Bennett. Heather keeps three watchers circling forty meters out from "
            "the center of the garage. The ceiling is fragile -- anyone over 60 kg standing on it goes "
            "through; a Reaction test at TN 6 catches a wall if they are within reach (TN 4 if the "
            "player said they were expecting it), and landing in the middle of the roof allows no test "
            "at all because there is nothing there that would hold. Blueprints can be pulled before the "
            "assault: Computer TN 4+TR, or TN 3+TR through a contact in city hall, one success in an "
            "hour and ten minutes off per additional success (Handout). Heather's original plan was to "
            "let Bennett strip the car and leave the unsellable remains for Rollo to find; Bennett "
            "found the engine instead, and the gang now spends until 05:30 mapping the fastest and "
            "safest route to Tir Tairngire. At 05:30 Heather calls them to mount up and they are gone "
            "within two minutes. The moment the runners settle matters here -- deal or firefight -- the "
            "Jaguar Guards announce themselves outside."
        ),
    },
    {
        "name": "Huitzilopochtli Plaza",
        "location_type": "residential community",
        "city": "Seattle",
        "district": "Downtown",
        "security_level": "Corporate Extraterritorial",
        "controlling_org": "Aztechnology",
        "summary": "The heavily guarded Aztlan-soil community outside the Aztechnology pyramid where Edmundo Castellian keeps an apartment he is not in tonight",
        "description": (
            "The Aztechnology residential enclave immediately outside the pyramid in Downtown Seattle, "
            "and the registered address of the Amanecer 5000's owner of record, Edmundo Castellian. It "
            "is considered Aztlan land. The book is blunt about what that means for a team that thinks "
            "of leaning on the frightened engineer at home: it is a heavily guarded Aztechnology "
            "community and breaking in on the fly will be next to impossible. It is also where the "
            "Jaguar Guards take prisoners for questioning."
        ),
        "notes": (
            "Edmundo is not in his apartment; he is inside the pyramid trying to invent a cover story "
            "and buy time in case the runners are late or fail. Running the car's license plate is what "
            "sends the team here, and confronting Lucien about the address is what gets them the story "
            "of their Johnson's parents' deaths and his brother's kidnapping and rediscovery. If the "
            "team cooperates with the Jaguar Guards and hands over the car, this is where they are "
            "brought: a grand inquisition run by Aztech security, for as long as the GM finds "
            "appropriate."
        ),
    },
    {
        "name": "Aztechnology Prototype Vehicle Facility (Seattle)",
        "location_type": "research lab",
        "city": "Seattle",
        "district": "Downtown",
        "security_level": "Corporate Extraterritorial",
        "controlling_org": "Aztechnology",
        "summary": "The plant where the Amanecer 5000 was built and stolen -- an underground parking deck, a work floor with a multi-billion-nuyen gap in the middle, and the lower labs nobody comes back from",
        "description": (
            "The Aztechnology facility where Edmundo Castellian's team built the Amanecer 5000. An "
            "underground parking deck with a guard on the barrier gives onto the work floor, which "
            "Edmundo's office overlooks through a window -- on the night of the theft there is a "
            "multi-billion-nuyen gap right in the middle of it where the car ought to be. Below are "
            "the lower labs, which is where corporate security takes people who have cost the company "
            "money: in Edmundo's imagination a voice proclaiming its innocence over the sound of saws "
            "entering warm flesh, and a hope that he might grab a gun from one of the guards and shoot "
            "himself before the elevator arrives."
        ),
        "notes": (
            "The theft as it happened: Rollo, wearing Edmundo's face, entered through the parking deck, "
            "greeted the guard, and drove the car out past the barrier a few minutes later. The plan "
            "was ruined only because Edmundo pulled an all-nighter before the unveiling and the guard "
            "said 'Welcome Back Mr. Castellian' on his way in. Edmundo spent the next hour hacking into "
            "the facility's own security database instead of weeping, magnified every frame he could "
            "find, and could not fault the impersonation: no extra wrinkles around the eyes, a perfect "
            "voice-pattern match. The building never appears on stage -- there is no scene here -- but "
            "it is the crime scene, the source of the security footage Edmundo is sitting on, and the "
            "reason the runners are working to a sunrise deadline."
        ),
    },
    {
        "name": "Aztechnology Seattle Testing Track",
        "location_type": "corporate facility",
        "city": "Seattle",
        "security_level": "Corporate Extraterritorial",
        "controlling_org": "Aztechnology",
        "summary": "Where the Aztechnology board of directors gathers at 08:00 to watch a glowing car they may not have",
        "description": (
            "The Aztechnology test track where the board of directors is due at 08:00 to see the "
            "Amanecer 5000 unveiled. One of the marketing people thought it would be clever: the car is "
            "called 'the dawn', it is launching on a new engine, so show it at sunrise -- symbolic, "
            "impactful. Edmundo's own assessment is a bunch of sleepy investors and board members "
            "wondering why they were dragged out of bed at the crack of dawn to watch a glowing car."
        ),
        "notes": (
            "Reached only through the corporate legwork table (Etiquette: Corporate Contacts, TN 4): a "
            "prototype was heisted off Aztechnology, it runs on some kind of new engine, the Azzies are "
            "sinking money into alternate fuels, and there is a Board of Directors meeting at 08:00 at "
            "their testing track, just a few hours off. That last item is the runners' clue that "
            "Lucien's 05:00 deadline has three hours of slack in it, and is the closest thing the "
            "adventure has to an editing inconsistency in the timing."
        ),
    },
    {
        "name": "Tarn's Home (Puyallup)",
        "location_type": "residential community",
        "city": "Seattle",
        "district": "Puyallup",
        "security_level": "Low Security",
        "summary": "The wolf shaman's house in a better part of Puyallup -- Heather's first stop with the car, and the one neighborhood in this adventure where Lone Star answers a call",
        "description": (
            "Heather's mentor Tarn lives in a better part of Puyallup, and the book makes a point of "
            "the difference: unlike the dead streets around Al's and the burnt-out garage, this is a "
            "neighborhood where Lone Star will respond to trouble. It is the first stop on the optional "
            "run for the border. Tarn makes his calls from here to contacts inside the Tir, who arrange "
            "for a GMC Banshee from Telestrian Industries to meet the party a mile outside the Salish "
            "border at specific coordinates."
        ),
        "notes": (
            "Used only in the optional Following the Leader scene, which is explicitly a time-filler "
            "for teams who sided with the Sidhe Devils and have session left to burn. Tarn also has a "
            "contact among the Salish border guards if the runners have no crossing plan of their own. "
            "If the players decide to mix things up with Tarn here, assume he is a grade 2+TR initiate "
            "and remember whose neighborhood they are shooting up."
        ),
    },
    {
        "name": "Telestrian Pickup Point (Salish Border)",
        "location_type": "smugglers den",
        "city": "Seattle",
        "district": "Salish-Shidhe border country",
        "security_level": "Low Security",
        "controlling_org": "Telestrian Industries",
        "summary": "Specific coordinates a mile past the Salish border where a Tir Banshee collects the car, the shamans and the gang",
        "description": (
            "A set of coordinates in Salish-Shidhe country, one mile beyond the border, where Tarn's "
            "contacts inside the Tir have arranged for a GMC Banshee from Telestrian Industries to "
            "come down and collect Tarn, Heather, the Amanecer and the Sidhe Devils. The convoy that "
            "arrives is a two-door two-seater glowing like a spotlight with a column of Harley-Davidson "
            "Scorpions whooping along behind it, which is not a discreet way to approach an "
            "international frontier."
        ),
        "notes": (
            "Getting here is the optional escort. If the runners have contacts or a plan for crossing "
            "the Salish border, use them; otherwise Tarn's border-guard contact opens the way. The GM "
            "is told to assume the Salish border guards are elite troops armed at least as well as the "
            "Jaguar Guards, with reinforcements in Yellowjackets able to respond to a skirmish within "
            "minutes. An incidental fight on the road -- gangers, Lone Star, Salish Border Patrol -- can "
            "be dropped in if there is time, keeping in mind that it is about six in the morning. If an "
            "ambush hits while they are in the car, Heather runs first: she orders the gangers to hold "
            "the pursuers off behind her while she and Tarn accelerate away, since the Amanecer only "
            "seats two."
        ),
    },
]

NPCS = [
    {
        "name": "Eduardo \"Lucien\" Castellian",
        "role": "The Mr. Johnson -- an Aztlan-born fixer who hates Aztechnology and is spending his brother's blood money to save his brother's life",
        "archetype": "Fixer",
        "title": "\"Lucien\" -- independent fixer, Seattle; brother of Edmundo Castellian",
        "race": "Human",
        "gender": "Male",
        "nationality": "Aztlan",
        "connection": 2,
        "description": (
            "A human male of Aztlan descent in a black duster over a black t-shirt and jeans, with "
            "mid-back-length black hair pulled into a ponytail. A bullet-hole scar mars his right "
            "cheek; the exit wound is in the back of his neck near the spinal cord, hidden by the "
            "hair. He speaks with only the slightest trace of a Spanish accent, has dark eyes, and "
            "carries the patient, unflappably calm demeanor of a man who has accepted that he may be "
            "waiting for his own death. At the meet he is unarmed and unarmored out of a fatalist "
            "melancholy about helping his brother and thereby helping Aztechnology; he has no qualms "
            "about injury, death or dying at the hands of the runners. Very open about not being in "
            "it for the money."
        ),
        "background": (
            "His father was taken when Lucien was eight, during an Aztechnology experimental-subject "
            "acquisition drive that he and his mother escaped. At fifteen, during the suppression of a "
            "rebel insurgency, he watched his mother shot, was shot in the mouth himself and left for "
            "dead; his brother Edmundo nursed him back to health. Aztechnology took Edmundo in another "
            "acquisition drive five years later. Since then Lucien has carried a growing hatred of "
            "Aztech and will do anything he can to see it injured, even in the smallest way -- he "
            "specializes in hooder-style jobs and runs against the corporation. The one exception is "
            "Edmundo: Lucien still feels he owes a life debt for the nursing, even to a brother who "
            "has gone over to the dark side, and neither of them has ever tested how far that debt can "
            "be pushed. They fell out when Edmundo took the Aztechnology job and have only recently "
            "started speaking again, though Lucien quietly keeps an eye on his brother's activities "
            "without his brother knowing. He took his running name from Alexandre Dumas's The Corsican "
            "Brothers, casting himself as the bandit brother, even though he and Edmundo are not twins."
        ),
        "notes": (
            "Stats: B2 Q4 S2 C4 I6 W6, Ess 5.84, Reaction 5. Pistols 6, Negotiation 6, Etiquette "
            "(Matrix) 2/4, Etiquette (Street) 2/4. Cyber: datajack (back of the neck). Bioware: "
            "mnemonic enhancer. Talents: data acquisition, bypassing security. Gear: Ares Predator, "
            "black Leyland-Rover Trans Electric Minibus (R3R p.171, no plates, stripped, no seating in "
            "the back). Treat him at the meet as having no dodge pool and no armor. Terms: 5,000 nuyen "
            "each for the undamaged car by 05:00, 2,500 if it arrives by 06:00, 1,000 each in advance "
            "subject to negotiation, 1,500 each more for capturing the thief; he provides a picture of "
            "the car and the last GPS fix, which is why the meet is at Al's. He will not say what "
            "happens to the thief -- 'that's not their concern' -- and seems almost disappointed if he "
            "has to deal with Heather himself. Legwork (Etiquette: Street 4): an Aztlan immigrant "
            "fixer; known hatred of Aztechnology; the scar came from an Aztlan death squad that shot "
            "him and left him for dead; Lucien is a running name he picked because of his family; he "
            "specializes in hooder jobs and runs against Aztech. Nothing about his brother or the "
            "Johnson behind him is available. Characters gain Lucien as a contact if they turn the "
            "undamaged car in as agreed. Contact card: Independent Fixer, human male, uses charity "
            "cases and runs against Aztechnology, meets in barrens bars and quiet back alleys, phone "
            "contact, usually available."
        ),
        "contact_skills": [
            "Runs against Aztechnology and charity cases",
            "Data acquisition and bypassing security",
            "Shadowlands board postings and rush hiring",
        ],
    },
    {
        "name": "Edmundo Castellian",
        "role": "The Aztechnology engineer framed for stealing his own prototype, footing the bill for the run with what his brother calls blood money",
        "archetype": "Corporate Scientist",
        "title": "Prototype vehicle engineer, Aztechnology (Seattle); Jackson Rollo's superior",
        "race": "Human",
        "gender": "Male",
        "nationality": "Aztlan",
        "connection": 2,
        "description": (
            "An engineer, not a criminal -- a man who works on electronics and theories and has spent "
            "the last hour watching the same security tape over and over in an office overlooking a "
            "work floor with a car-shaped hole in it. 'I am so screwed,' said out loud to an empty "
            "room. His hand shakes so badly that he punches his brother's number in wrong three times "
            "before it connects, and he swallows the lump in his throat and prays to whoever is "
            "listening that Eduardo still gives a damn. Underneath the panic is the other Castellian "
            "temper: when he finds out who did this, he will make sure that person wishes he had never "
            "been born. Oh, how they would pay."
        ),
        "background": (
            "Taken by Aztechnology in an experimental-subject acquisition drive five years after his "
            "mother was shot and his brother left for dead -- the story Lucien will tell the runners if "
            "they confront him about the Huitzilopochtli Plaza address on the car's registration. He "
            "ended up an Aztechnology employee rather than an Aztechnology experiment, which is a "
            "distinction his brother finds hard to forgive; the two fell out over it and have only "
            "lately begun speaking again. Tonight the Amanecer 5000 is his responsibility, his neck, "
            "and most importantly his face on the tape taking the car. He knows perfectly well that "
            "once the theft is discovered he will not be given a chance to proclaim his innocence; he "
            "will simply be taken by security to the lower labs, and that will be it."
        ),
        "notes": (
            "No stat block; he never appears on stage. He is in the pyramid all night, inventing ways "
            "to cover the loss and buy time in case the runners are late or fail -- which is why "
            "breaking into his Huitzilopochtli Plaza apartment achieves nothing except attracting "
            "Aztechnology. He is the registered owner of the stolen car, so running the plates leads "
            "to him. He is also the source of the money: he is footing the entire bill, and Lucien is "
            "not remotely worried about burning through what he regards as his brother's blood money "
            "from Aztechnology. The one thing he does right is the all-nighter -- without it the "
            "guard's 'Welcome Back Mr. Castellian' would never have tipped him off and he would have "
            "spent the hour weeping instead of hacking the security database. He does not know where "
            "the car is and dares not activate it in case whoever has it notices it being looked for."
        ),
    },
    {
        "name": "Jackson Rollo",
        "role": "Edmundo's lead assistant -- the thief who wore his boss's face, parked the car with a gang, and tipped the Jaguar Guards to make himself the hero",
        "archetype": "Corporate Mage",
        "title": "Lead assistant to Edmundo Castellian, Aztechnology (Seattle)",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": (
            "A corporate suit who beat every camera in a Stuffer Shack parking lot by wearing a hat and "
            "a coat, and who beat every camera in an Aztechnology facility by wearing his boss's face. "
            "On the security tape he is Edmundo Castellian down to the wrinkles around the eyes and the "
            "voice pattern; in the parking lot he is a suit handing keys to an elf girl and getting "
            "into a waiting cab. The runners never get a good look at him and never get an image: none "
            "of the cameras caught his face. What they get instead is the shape of the man -- somebody "
            "willing to steal billions of nuyen of his own employer's property, frame his immediate "
            "superior for it, and then call in an elite military unit on a gang of teenagers, all to "
            "look good at an 08:00 board meeting."
        ),
        "background": (
            "Earning promotions is a cutthroat business at Aztechnology, and Rollo did a very good job "
            "of making it look as though Edmundo took the car. Magic was the tool -- the impersonation "
            "is too perfect to be an actor -- and the plan was never actually to keep the Amanecer. He "
            "handed it to the Sidhe Devils with a story about a mole inside Aztech who wanted the "
            "corporation's newest toy to get into the right hands, expecting a small gang to sit on it "
            "in a garage until he could recover it in the morning with some flair. He never thought "
            "they might be able to get it inside the Tir border in time. When it becomes clear that a "
            "complication -- the runners, or Heather's drive north -- might cost him the car, he hedges "
            "his bet and tips off a squad of Jaguar Guards."
        ),
        "notes": (
            "No stat block and no image; the book keeps him offstage. He is worth 1,500 nuyen each as "
            "a bonus if the runners can capture the thief, which requires working out who he is from "
            "the credstick record in Al's scanner, Heather's account of the handover, and the fact that "
            "somebody at the facility could wear Edmundo's face. He deactivated nothing himself: "
            "Bennett found and tore out the GPS beacon at Al's, which is why the car's last fix is the "
            "Stuffer Shack lot. His move in the third act is Jaguars Come Stalking, triggered the "
            "moment the runners settle matters with the Sidhe Devils. Aftermath: if the car goes back "
            "to Aztechnology, the contact who set the run up gets the credit and the gratitude, and "
            "Rollo does not."
        ),
    },
    {
        "name": "Heather",
        "role": "Elf dog shaman leading the Sidhe Devils, holding a stolen prototype she means to gift to Tir Tairngire; a contact who owes fetishes if the runners help her escape",
        "archetype": "Shaman",
        "title": "Leader of the Sidhe Devils; dog shaman and talismonger",
        "race": "Elf",
        "gender": "Female",
        "connection": 2,
        "description": (
            "The only genuine elf in a gang of surgically elf-ified humans, in leathers, with an Ares "
            "Predator and a Harley-Davidson Scorpion, described on the street simply as 'an elf girl "
            "ganger, quite a looker'. She is reasonable and hard to move: an accomplished dog shaman "
            "who is very difficult to dissuade from a task once she has set her mind to it, and an "
            "altruist who has been seen trying to get Tir Tairngire to acknowledge her existence. She "
            "meets strangers with Analyze Truth up and the first question straight: do they work for "
            "Aztechnology? She can be pushed, but only so far -- even under threat of death she will "
            "insist that her gang members go free, and she would rather die than see them all suffer "
            "Aztech's torture."
        ),
        "background": (
            "She sees Tir Tairngire through rose-colored glasses and aspires to join the elven nation, "
            "though it refuses to have her; the gang of posers around her is a kind of answer to that. "
            "She took the car from a corp suit at Al's Stuffer Shack, agreeing to hold it for a few "
            "hours, and only decided to take her own initiative once she realized what it was worth; "
            "Bennett found the unusual engine and she saw a chance to buy credibility with the Tir at "
            "last. She knows the car has a tracking device and cannot understand why it has not been "
            "activated -- the book's own loose thread, since Bennett had already torn the beacon out at "
            "Al's. She has some leads to get her to the border but is waiting on a callback that will "
            "not come until 05:30."
        ),
        "notes": (
            "Stats: B2 Q4 S1 C6 I5 W6 Magic 6, Ess 6, Reaction 4, Init 4+1D6, Combat Pool 7, Spell "
            "Pool 5, Karma 2, Pro 2/semi-trained. Leathers 0/2; Ares Predator, Harley-Davidson "
            "Scorpion, Force 2 expendable healing fetish. Pistols 3, Aura Reading 5, Conjuring 6, "
            "Sorcery 6, Etiquette 4, Gang Identification 3; talismongering. Spells: Armor 5, Detect "
            "Enemies 4, Influence 3, Powerbolt 4, Manabolt 5, Physical Mask 3, Analyze Truth 5, Treat "
            "5, Compel Truth 5. Three watchers patrol a forty-meter circle around the garage. "
            "Negotiations: she will sell the car back starting at 15,000 nuyen subject to the usual "
            "negotiation, since anything that hurts Aztech suits her; a team claiming to work for "
            "Aztechnology can bluff her into cooperating, and a team that can obviously overpower the "
            "gang can force her, but she will surrender herself rather than her people. She has three "
            "expendable rating 2 health fetishes to offer as a bribe. If the runners side with her she "
            "hands those over at once and promises three more Force 2 expendable fetishes of the "
            "player's choice once she is safe -- one at a time, two weeks each, arriving after the "
            "second week's activities; note the recipients on the Mission Record. Players gain Heather "
            "as a contact if they help her escape to Tir Tairngire with the car. Turning her in "
            "requires incapacitating her first. Killing her whole gang for the Jaguars costs a karma "
            "point."
        ),
        "contact_skills": [
            "Talismongering -- expendable fetishes to order",
            "Puyallup gang scene and Sidhe Devils turf",
            "Tir Tairngire sympathizers and border rumor",
        ],
    },
    {
        "name": "Bennett",
        "role": "Heather's boyfriend and the Sidhe Devils' mechanic -- the one who found the beacon, opened the hood and realized what the gang had stolen",
        "archetype": "Ganger",
        "title": "Second of the Sidhe Devils; the gang's mechanic and rider",
        "race": "Human",
        "gender": "Male",
        "organization": "Sidhe Devils",
        "connection": 1,
        "description": (
            "One of the cosmetically elf-ified humans in the gang, and the only one with a skill worth "
            "anything: an actual mechanic with low-light vision, a datajack, boosted reflexes and an "
            "AK-97 smartgun, who rides a Scorpion better than anyone else in the Sidhe Devils. On the "
            "security tape from Al's he is the figure who pops the hood of a glowing car and rummages "
            "under it for a few seconds before getting in. He is intimidating rather than talkative, "
            "and like Heather he will not go down without a fight if he thinks Aztechnology is taking "
            "him alive."
        ),
        "background": (
            "Heather's boyfriend and the practical half of the gang's leadership. The original plan for "
            "the Amanecer was his job -- strip it and leave whatever could not be sold in pieces for "
            "the suit to find. He tore the Aztechnology GPS beacon out in the Stuffer Shack parking lot "
            "and left it broken on the ground before they drove off, which is why the last fix Lucien "
            "can give the runners is Al's. Then he got the hood open properly at the garage, saw what "
            "the engine actually was, and the chop-shop plan died on the spot. He plans to leave his "
            "own bike behind on the ride north; the Amanecer only seats two, and one of those seats is "
            "not his."
        ),
        "notes": (
            "Stats: B5 Q7 S3 C5 I4 W5, Ess 4.8, Reaction 5, Init 5+2D6, Combat Pool 8, Karma 1, Pro "
            "2/Semi-trained. Leathers 0/2; AK-97 SMG smartgun (6M), smartlink, datajack, 2 clips, "
            "Boosted Reflexes 1, low-light vision. Intimidation 3, Bike/Harley Scorpions 5/7, Bike B/R "
            "6, Electronics 5, Stealth 3, Unarmed Combat 6, SMG/AK-97 4/6. Legwork names him as "
            "Heather's boyfriend at three successes on the Sidhe Devils table. In the Direct Approach "
            "he and Heather are the two the rest of the gang watches: drop either of them, or more "
            "than half the gang, and the remaining punks run. He is the reason the Amanecer is intact "
            "and drivable when the runners find it, and the reason it is not still transmitting."
        ),
    },
    {
        "name": "Al Preswick",
        "role": "Owner of Al's Stuffer Shack -- bluster, a baseball bat, a security system and everything the team needs to find the gang",
        "archetype": "Shopkeeper",
        "title": "Owner, Al's Stuffer Shack (3rd and West, Puyallup)",
        "race": "Ork",
        "gender": "Male",
        "age": 38,
        "connection": 1,
        "description": (
            "A big ork in his late thirties -- bald, out of shape, with a serious beer gut -- who comes "
            "out of the back of the kitchen in a stained white apron carrying an old baseball bat when "
            "somebody makes a ruckus at his sealed front door at three in the morning. The book's "
            "direction is explicit: give him your best Brooklyn accent and play him full of bluster. He "
            "is confrontational toward the runners and has absolutely no combat skills to back it up. "
            "Offer him any sort of bribe, or any amount of flattery at all, and he becomes cooperative "
            "very quickly; return his attitude and he will not willingly help with anything."
        ),
        "background": (
            "He has been running a fast-food franchise in the Puyallup barrens long enough to know the "
            "local gangs by their colors and to keep the grill going after close. He has seen Heather "
            "and Bennett around, knows of the Sidhe Devils, and does not think highly of them, though "
            "he allows that as gangers go they are not all that bad. He watched them take the car "
            "earlier that night and thought it looked like a more complicated sort of job than they "
            "would normally be involved in. He remembers the car and the driver but has never seen the "
            "man before and knows nothing about him. He has no idea where the gang's hideout is."
        ),
        "notes": (
            "No stat block. His assets are the ones that matter: interior and parking-lot cameras "
            "(Perception 4 to spot, Electronics 3 to review), a rating 3 credstick scanner still "
            "holding the suit's personal information, rating 3 maglocks on Plexiglas doors, and his own "
            "memory of the handover -- he will happily describe how brightly the car was glowing when "
            "it drove off. Asking him, or an Area Knowledge / Gang Identification (5) test, names the "
            "Sidhe Devils. Two optional complications hang off him: he may run his security through the "
            "local Mafia, so a scene at his shop brings Capo Maurice 'Butcher' Bigio's limo and "
            "bodyguards to the drive-through buzzer, disappointed to find someone under their "
            "protection has been hurt; or he may, despite the address, be on friendly terms with Lone "
            "Star, keeping the grill running and handing out free soyburgers to any cop who stops by. "
            "If nobody on the team has Electronics, they need Al's cooperation to get through the "
            "footage at all."
        ),
        "contact_skills": [
            "Puyallup street and gang gossip",
            "Late-night soyburgers and a working security system",
        ],
    },
    {
        "name": "Lt. Jose Ramirez",
        "role": "Jaguar Guard lieutenant who surrounds the garage on Rollo's tip and gives everyone inside thirty seconds",
        "archetype": "Military Officer",
        "title": "Lieutenant, Aztlan Jaguar Guards",
        "race": "Human",
        "gender": "Male",
        "nationality": "Aztlan",
        "organization": "Aztlan Jaguar Guards",
        "connection": 3,
        "description": (
            "A voice through an electronic amplifier in the dark outside a garage, at the exact moment "
            "the runners think the job is finished: 'This is Lt. Jose Ramirez of the Aztlan Jaguar "
            "Guards. We have the garage surrounded. We have reason to believe that you have a piece of "
            "stolen corporate equipment inside with you. Please throw down your weapons and exit with "
            "your hands up. You have 30 seconds before we attack.' He is professional, entirely "
            "unbribable, and running an elite squad against what he has been told is a corporate theft. "
            "He is not told, and does not know, that the man who called it in is the thief."
        ),
        "background": (
            "Rollo discovered that a complication -- the runners, or Heather's drive for the Tir -- "
            "might prevent him from recovering the car in time to be the hero of the morning's board "
            "meeting, so he hedged his bets and tipped a squad of Jaguar Guards to its location. "
            "Ramirez's squad is the result: elite Aztlan troops deployed into the Puyallup barrens "
            "before dawn on a mid-level assistant's word, to take a prototype back from teenagers."
        ),
        "notes": (
            "No individual stat block; run him on the Jaguar Guard trooper line (B5 Q6 S6 C3 I5 W6, "
            "Ess 1, Reaction 5(9), Init 9+3D6, Combat Pool 8, Karma 2, Pro 4/Veteran; Ares Alpha 8M, "
            "Neurostun VIII 6S Stun, medium security armor 6/5, Wired Reflexes 2, Smartlink 2). "
            "Triggered the moment matters are resolved with the Sidhe Devils. Tactics: gas grenades "
            "into the garage first, then pick off runners as they leave cover; the combat shaman, if "
            "the table rating merits one, spends everything on spell defense. Negotiation is unlikely "
            "but the GM is told to be flexible -- corporate politics or a phone call to Lucien might "
            "work; money will not. Standing back and letting the Jaguars slaughter the gangers costs "
            "the team a karma point. If the team surrenders the car, Ramirez's people take them "
            "prisoner and deliver them to the plaza for questioning."
        ),
    },
    {
        "name": "Tarn",
        "role": "Heather's mentor -- an elf wolf shaman with real contacts inside the Tir, and the reason the escort scene has an ending",
        "archetype": "Shaman",
        "title": "Wolf shaman; Heather's teacher",
        "race": "Elf",
        "gender": "Male",
        "connection": 3,
        "description": (
            "An elf wolf shaman living in a better part of Puyallup than any of his student's gang "
            "could afford -- the sort of neighborhood where Lone Star still answers calls. He is the "
            "one adult in Heather's life with actual standing: where she has been trying for years to "
            "get Tir Tairngire to notice she exists, Tarn simply makes a call and a Telestrian Banshee "
            "is dispatched to a set of coordinates across a national border. He has a contact among the "
            "Salish border guards as well."
        ),
        "background": (
            "Heather's mentor and the first place she takes the car, before she takes it anywhere else. "
            "His connections inside the Tir arrange the pickup a mile past the Salish border and the "
            "protective custody that follows. He rides out with the column and, being one of the two "
            "people in the Amanecer's two seats, is the other half of the escape if an ambush hits on "
            "the road."
        ),
        "notes": (
            "No stat block; the book says to assume he is a level 2+TR initiate if the players decide "
            "it is a good idea to mix things up with him. He appears only in the optional Following the "
            "Leader scene. Plot use: he is the bridge between a Puyallup poser gang and a real Tir "
            "corporation, the fallback for a team with no way across the Salish border, and a standing "
            "contact for anyone who escorts Heather all the way. Note that his neighborhood is not the "
            "barrens -- trouble there brings Lone Star, which is precisely the sort of attention a team "
            "hauling a glowing stolen prototype cannot afford."
        ),
        "contact_skills": [
            "Contacts inside Tir Tairngire",
            "A contact among the Salish border guards",
            "Shamanic instruction",
        ],
    },
    {
        "name": "Maurice \"Butcher\" Bigio",
        "role": "Mafia capo with a weakness for Al's soyburgers, and an optional very bad complication for a team making a scene at a protected business",
        "archetype": "Crime Boss",
        "title": "Capo, Seattle Mafia (New Seattle p.98)",
        "race": "Human",
        "gender": "Male",
        "organization": "Seattle Mafia",
        "connection": 4,
        "description": (
            "A Seattle Mafia capo who turns up in the drive-through of a closed Stuffer Shack in the "
            "Puyallup barrens at three in the morning because he has a thing for Al's soyburgers. The "
            "runners meet him, if they meet him at all, as a limousine and a set of bodyguards on a "
            "security monitor after the drive-through buzzer goes off in the middle of whatever they "
            "are doing to Al or his systems. He is not there for them and does not want trouble; he is "
            "there for the food, and he will be very disappointed to discover that somebody has hurt a "
            "man under his protection."
        ),
        "background": (
            "Statted in New Seattle (p.98) rather than in this adventure. The optional hook is that Al "
            "manages his security through the local Mafia rather than through anybody legitimate -- a "
            "sensible arrangement for a franchise in a district where Lone Star is a rumor -- which "
            "makes a small fast-food operator into a protected interest and any runner who leans too "
            "hard on him into a problem for the organization."
        ),
        "notes": (
            "Optional Pushing the Envelope complication only; use the New Seattle stat block. The "
            "trigger is the runners making a scene at Al's -- breaking in, roughing him up, tearing "
            "into his security system in front of him. Consequences are left to the GM, but the framing "
            "is clear: the team has hours to find a car and has just acquired the attention of "
            "organized crime while doing legwork. The alternative hook the book offers for the same "
            "scene is Lone Star rather than the Mafia, so only one of the two should be in play."
        ),
        "contact_skills": [
            "Seattle Mafia protection rackets in the south metroplex",
        ],
    },
]

ORG_UPDATES = {
    "Aztechnology": {
        "notes_append": (
            "SRM 01-06 Lost and Found: an Aztechnology prototype vehicle plant in Seattle loses the "
            "Amanecer 5000, a multi-billion-nuyen alternate-fuel prototype, hours before it is due to "
            "be unveiled to the board of directors at the corporate testing track at sunrise. The thief "
            "is the project lead's own assistant, Jackson Rollo, who used magic to wear his superior's "
            "face past the parking-deck guard -- promotion is a cutthroat business at Aztechnology, and "
            "the frame-up was meant to end with Edmundo Castellian in the lower labs. Corporate legwork "
            "(Etiquette: Corporate, TN 4) turns up the theft, the new engine, the fact that the Azzies "
            "are sinking money into alternate fuels, and the 08:00 board meeting at the testing track. "
            "Staff attitude is set by what happens to failures: Castellian's assumption is that once "
            "the loss is discovered he will simply be walked to the lower labs by security, and he "
            "hopes he can grab a guard's gun first. Aftermath: the corporation is quietly grateful to "
            "whichever fixer arranged the recovery and bumps a connection 1 contact to connection 2 (2 "
            "and above are unaffected); a team that instead sells the car to another AAA earns "
            "Enemy: Aztechnology -- the next dealing with the corporation goes badly, after which the "
            "status is rescinded. Any AAA will gladly take the car; nothing below AAA will risk "
            "Aztech's ire. Aztechnology also employs the Aztlan Jaguar Guards as a recovery asset "
            "inside the metroplex on a phone call, and holds Huitzilopochtli Plaza outside the pyramid "
            "as Aztlan soil."
        ),
        "enemies_add": ["Sidhe Devils"],
    },
    "Aztlan": {
        "notes_append": (
            "SRM 01-06 Lost and Found: Aztlan's reach into the Seattle metroplex is on display twice. "
            "Huitzilopochtli Plaza, the residential community outside the Aztechnology pyramid, is "
            "considered Aztlan land and is heavily enough guarded that breaking in on the fly is next "
            "to impossible. And a squad of Aztlan Jaguar Guards -- elite national troops -- deploys "
            "into the Puyallup barrens before dawn to recover corporate property on the word of a "
            "mid-level Aztechnology assistant. The adventure's Mr. Johnson is an Aztlan emigrant whose "
            "father was taken in an Aztechnology experimental-subject acquisition drive and whose "
            "mother was shot during the suppression of a rebel insurgency; the same suppression put a "
            "bullet through his cheek and left him for dead at fifteen."
        ),
    },
    "Tir Tairngire": {
        "notes_append": (
            "SRM 01-06 Lost and Found: the Tir is the object of a Puyallup elf-poser gang's devotion "
            "and refuses to have anything to do with her. Heather, the real elf leading the Sidhe "
            "Devils, sees Tir Tairngire through rose-colored glasses and has been trying for years to "
            "get the elven nation to acknowledge her existence; she decides that delivering a stolen "
            "Aztechnology prototype will finally buy her credibility. Her mentor Tarn, a wolf shaman, "
            "does have contacts inside the Tir, and they respond: a GMC Banshee from Telestrian "
            "Industries is dispatched to coordinates one mile outside the Salish border to collect the "
            "car, the shamans and the gangers, who are taken into protective custody until their story "
            "can be verified. Delivering the Amanecer 5000 to Tir Tairngire is worth two karma to the "
            "runners, against one for handing it back."
        ),
        "allies_add": ["Telestrian Industries"],
    },
    "Salish-Shidhe Council": {
        "notes_append": (
            "SRM 01-06 Lost and Found: the Salish border is the last obstacle on the optional run for "
            "Tir Tairngire. The book tells the GM to assume the border guards are elite troops armed at "
            "least as well as Aztlan's Jaguar Guards, with additional guards in Yellowjackets able to "
            "respond to a skirmish within minutes. The wolf shaman Tarn has a contact among the border "
            "guards and can open a crossing if the runners have no plan of their own; the Telestrian "
            "pickup point is a mile beyond the line. An incidental road fight with the Salish Border "
            "Patrol is offered as a time-filler for teams with session left over."
        ),
    },
    "Lone Star Security": {
        "notes_append": (
            "SRM 01-06 Lost and Found: Lone Star's absence is the point. The corner of 3rd and West in "
            "Puyallup is dark, silent and unpoliced at three in the morning -- all but one streetlight "
            "gone to vandalism, stray gunfire and neglect -- and nothing that happens at Al's Stuffer "
            "Shack or the Sidhe Devils' garage draws a response. The one place in the adventure where "
            "the Star does answer is the better part of Puyallup where the shaman Tarn lives, which "
            "makes it the wrong neighborhood for a firefight. Optional hook: Al Preswick may keep his "
            "grill running and hand out complimentary soyburgers to any officer who stops by, giving a "
            "barrens franchise a friend with a badge; the alternative version of the same hook gives "
            "him Mafia protection instead."
        ),
    },
    "Seattle Mafia": {
        "notes_append": (
            "SRM 01-06 Lost and Found: optional complication -- Al Preswick manages the security of his "
            "Puyallup Stuffer Shack through the local Mafia. If the runners make a scene there, the "
            "drive-through buzzer goes off in the middle of it: Capo Maurice 'Butcher' Bigio (New "
            "Seattle p.98) has a thing for Al's soyburgers, and that is his limousine and his "
            "bodyguards on the security monitor. They will be extremely disappointed to learn that the "
            "team has hurt someone under their protection."
        ),
        "leadership_add": [
            {"name": "Maurice \"Butcher\" Bigio", "title": "Capo", "notes": "Statted in New Seattle p.98; protects Al's Stuffer Shack in Puyallup and eats there after hours."},
        ],
    },
    "Telestrian Industries": {
        "notes_append": (
            "SRM 01-06 Lost and Found: Telestrian is the hand Tir Tairngire extends to a Puyallup "
            "elf-poser gang holding a stolen Aztechnology prototype. When the wolf shaman Tarn calls "
            "his contacts inside the Tir on Heather's behalf, they arrange for a GMC Banshee from "
            "Telestrian Industries to collect the party at specific coordinates one mile outside the "
            "Salish border. The crew take Tarn, Heather, the Amanecer 5000 and the surviving Sidhe "
            "Devils into protective custody until their story can be verified; Heather thanks the "
            "runners at the landing zone and explains that she does not know when she will be able to "
            "leave and does not want to be responsible for them as well. No statistics are given for "
            "the crew -- the book tells the GM only to use best judgment if the players decide to mix "
            "it up with them. Plot use: an operating corporate arm of the Tir inside the metroplex, "
            "and the reason a stolen alternate-fuel prototype is flown out rather than confiscated at "
            "the Salish line. Delivering the car this way is worth two karma against one for handing "
            "it back to Aztechnology."
        ),
        "allies_add": ["Tir Tairngire"],
    },
    "Ancients": {
        "notes_append": (
            "SRM 01-06 Lost and Found: contacts within the Ancients reduce the target number for street "
            "legwork on the Sidhe Devils by 2 (from Etiquette: Street 6 to 4). The Ancients are the "
            "reference point against which a gang of surgically elf-ified human posers in Puyallup gets "
            "measured, and the obvious source for anyone in the metroplex who wants to know what a real "
            "elf gang thinks of one."
        ),
    },
}

LOC_UPDATES = {
    "Aztechnology Pyramid": {
        "notes_append": (
            "SRM 01-06 Lost and Found: the pyramid is where Edmundo Castellian spends the night of the "
            "theft, trying to invent a cover story and buy time in case the runners are late or fail, "
            "which is why he is not at his apartment in Huitzilopochtli Plaza when the team runs the "
            "stolen car's plates and turns up his address. The plaza outside the pyramid is Aztlan "
            "land, heavily guarded, and effectively impossible to break into on the fly."
        ),
    },
    "Salish-Shidhe Border Post (Seattle crossing)": {
        "notes_append": (
            "SRM 01-06 Lost and Found: the crossing the optional escort scene has to beat. Heather's "
            "convoy -- a two-seat prototype glowing white-blue and visible at 150 meters, trailed by a "
            "column of Harley-Davidson Scorpions -- runs for coordinates a mile past the line, where a "
            "Telestrian Industries GMC Banshee is waiting. The book tells the GM to treat the border "
            "guards as elite troops armed at least as well as the Aztlan Jaguar Guards, with "
            "reinforcements in Yellowjackets minutes away. The wolf shaman Tarn has a contact among the "
            "guards and can arrange passage if the runners have no route of their own."
        ),
    },
}

NPC_UPDATES = {}

TAG_EXISTING = {}

MATRIX_HOSTS = """
There is no decking scene in this adventure -- the Matrix work is short, opportunistic and mostly
happens on other people's small systems. Four systems are worth building if the GM wants them.

### Al's Stuffer Shack security system

A franchise fast-food package: interior cameras covering the restaurant, exterior cameras covering
the parking lot, rating 3 maglocks on the Plexiglas doors, and a separate rating 3 credstick scanner
at the counter. No host rating is printed. Access in play is by Electronics (3) to review the
footage, or Perception (4) to spot the cameras in the first place; the scanner has to be hacked
without Al Preswick noticing, and it still holds the personal information of the corporate suit who
handed the car keys over earlier that night. The footage cannot be made to give up Jackson Rollo's
face -- the hat and coat beat every angle -- but yields stills of the car, Bennett and Heather.

### The Aztechnology facility security database

Never entered by the runners; the theft footage the whole plot hangs on comes from Edmundo
Castellian hacking his own building's security database in the hour after he realizes what has
happened. It holds the parking-deck entry, the greeting from the guard, the drive-out and the pass
check -- and survives magnification at every level Edmundo can apply, with no extra wrinkles around
the eyes and a perfect voice-pattern match. Treat it as a corporate security host at whatever rating
the campaign uses for Aztechnology; a team that decked it directly would short-circuit the entire
adventure.

### Seattle city hall permit and blueprint archive

The source of the garage blueprints (Handout). Computer test at TN 4+TR, dropping to TN 3+TR for a
contact inside city hall. One success retrieves the blueprints in an hour; each additional success
cuts ten minutes off the retrieval time. No IC or alert structure is given -- this is legwork, not
an intrusion.

### The Shadowlands board

Lucien puts the call for a rush team out on Shadowlands at about two in the morning and agrees to
pay a heavy finder's fee for any reliable runners who can be produced on that notice. The deckers
who take the call are the ones who contact the player characters, which is why the adventure's
reward table hands the credit -- and an increase from connection 1 to connection 2 -- to the contact
who arranged the run rather than to the team.

### The Amanecer 5000's GPS beacon

An Aztechnology-stamped locator beacon, roughly six inches square, torn out of the car by Bennett in
Al's parking lot and left broken on the ground; Perception (6) finds it, Electronics (4) identifies
it. Its last transmitted fix is the reason Lucien holds the meet at the Stuffer Shack. Note the
book's own contradiction: Heather believes the car still carries a live tracking device and cannot
work out why it has not been activated.
"""

NOT_BUILT = """
- **The Amanecer 5000** -- the prototype itself, a machine rather than a character. Hand 2/7, Speed
  380 (limited to 80 in city driving), Accel 21, Body 3, Armor 0, Sig 2, Auto 0, Sensor 2, Cargo 5,
  Load 50, Seating 2, Entry 2, Fuel EC, Econ 24 km/l. A bronze-steel alloy body coated in dikote that
  acts as a superconductor over titanium-steel wheels dikoted as insulators; the engine's excess
  current runs through the outer frame and makes the car glow whitish-blue whenever it is running,
  obvious from 150 meters. Current cracks water vapor as it goes, feeding hydrogen back into the fuel
  canister and shunting the oxygen into the cabin. The voltage is high but the resistance too high to
  hurt anyone -- touching it is a carpet-and-doorknob shock. The windows are synthetic diamond,
  specially tinted so as not to disrupt conductivity, and act as one-way mirrors. It has not been
  fully speed-rated, so the top of the engine is unknown. Kept in the garage and facility notes.
- **The parking-deck guard** who says "Welcome Back Mr. Castellian" -- unnamed, and the only reason
  the frame-up failed. Folded into the Aztechnology Prototype Vehicle Facility notes.
- **The Aztechnology marketing man** who scheduled a sunrise unveiling because the car is called "the
  dawn" -- quoted, never named. Folded into the testing track notes.
- **The Telestrian Banshee crew** -- competent, faceless, and given no statistics; they take everyone
  into protective custody until the story checks out. Folded into the Telestrian Industries notes.
- **The Salish border guards and the Yellowjacket reinforcements** -- an instruction to the GM
  ("elite troops armed at least as well as the Jaguar guards") rather than a cast entry. Folded into
  the Salish-Shidhe Council and border post updates.
- **The cab driver** who collects the suit outside Al's after the handover -- one line in the street
  legwork table.
- **Leyland-Rover, Harley-Davidson, Ares, GMC, Chrysler-Nissan** -- manufacturer name-drops on gear
  and vehicles only.
- **The Shadowlands deckers** who answered Lucien's call and passed the job to the runners -- the
  book deliberately leaves them as the players' own existing contacts, and explicitly warns the GM
  not to use the standard SRM NPCs (Fox, Joey and company) for the introductory contact.
"""

PLAY_NOTES = """
- Three and a half hours of play in a four-to-five hour slot, with 15-20 minutes at the end for
  Debriefing Logs. Everything runs on one clock: 02:15 the call, 03:15 the meet, 05:00 full pay,
  05:30 the gang leaves, 06:00 half pay. Keep close track of elapsed time -- the whole adventure is
  built on the deadline, and the Debugging notes warn repeatedly that legwork detours (especially a
  team with no Electronics skill carrying Al's security data elsewhere) will eat the window.
- The opening is atmosphere, not threat: the barrens around 3rd and West are near-silent because the
  gang is sequestered in its garage, and a Perception (hearing) TN 4 test tells the players that the
  normal night noises are missing. Lucien did not stage it. If you play music, horror-movie
  background is suggested. Let the team be weirded out before they spot each other.
- The Jaguar Guards trigger on resolution, not on a clock. Whatever way the garage ends -- a purchase
  at 15,000 nuyen, a bluff, a threat, a massacre, an alliance -- Lt. Ramirez's amplified voice comes
  a moment later. If the gang is alive and friendly they fight alongside the runners; if not, it is a
  three-way firefight. The Jaguars are elite: do not try to kill the party, but scale up if the table
  can take it, and for a full effect give them an Ares Citymaster and a rigger.
- The moral choices are the point and the karma table says so: taking the car from the Sidhe Devils
  without violence is worth a point, standing by while the Jaguar Guards slaughter the gangers costs
  one, delivering the car to Lucien is worth one and delivering it to Tir Tairngire is worth two.
  Maximum six good karma including three for roleplaying.
- Heather is written to be negotiable in every direction and immovable on one point: her people go
  free. She casts Analyze Truth as a matter of course, so lying to her is a contest, not a
  formality. A team that presents itself as Aztechnology can extort her; a team that is obviously
  stronger can force her; neither gets her gang.
- Following the Leader is optional and explicitly a time-filler. Run it only if the team sided with
  Heather and there is session left. Remember the Amanecer is a two-door two-seater -- Heather and
  Tarn ride in it and everyone else is on a Scorpion.
- Selling the car elsewhere is allowed but expensive: any AAA will take it, nothing smaller will
  risk Aztechnology, and the team collects both the "A Corporate Favor" and the "Enemy:
  Aztechnology" handouts. Note them on the Mission Record Sheets. Any shadowrunner should know the
  car is far too flashy to keep.
- If the players refuse the job at the van, hand them their event log and end the session -- the
  book's own Debugging instruction.
"""

# Load-time fix: Huitzilopochtli Plaza already exists in production (home-grown row), so append instead
# of creating.
_dup = [l for l in LOCATIONS if l["name"] == "Huitzilopochtli Plaza"]
if _dup:
    _l = _dup[0]
    LOCATIONS = [l for l in LOCATIONS if l["name"] != "Huitzilopochtli Plaza"]
    LOC_UPDATES["Huitzilopochtli Plaza"] = {
        "description_append": f"{ADVENTURE}: " + (_l.get("description") or _l.get("summary") or ""),
        "notes_append": f"{ADVENTURE}: " + (_l.get("notes") or ""),
    }
