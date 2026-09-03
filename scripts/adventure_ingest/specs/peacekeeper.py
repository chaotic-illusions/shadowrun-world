# Peacekeeper (Native American Nations Volume One, FASA 7202, 1991) -- campaign order #8.
# Seattle -> Las Vegas (Ute) -> Provo (Ute) -> Council Island, October 2051 (news handouts dated
# Thursday October 26, 2051; the intro's "2052" is the sourcebook's year).
# NOTE: the book's third act calls the city both "Pueblo" and "Provo" (maps, the scribbled address
# and the epilogue say Provo, Ute; the prose says Pueblo). Provo, Ute is used here; alias noted.
# Source text: docs/Adventures/text/Shadowrun 1e - Native American Nations Volume One {FASA7202}.txt
# (viewer pp. 6-70). ASCII only (pre-commit hook).

ADVENTURE = "Peacekeeper"
ORDER = 8
SOURCE = "Shadowrun 1e - Native American Nations Volume One {FASA7202}.pdf, viewer pp. 6-70 (adventure section)"
YEAR = "2051 (October)"

SYNOPSIS = """
Two razorguys the Chinaman calls the Bobsie Twins collect the runners from the **Blue Flame Tavern**
for a meet at the **New Ritz** lounge with 'Mr. Johnson' -- turquoise power tie, Aztechnology watch,
an Aztech expense account -- who is really **Karl Brackhaven**, president of the Humanis Policlub's
Central Seattle chapter. The job: 115,000 nuyen to stop **Jesse John**, 'shaman, assassin,
provocateur', capture if possible, 'beyond salvage' if not. Jesse is a Tsimshian-born Toxic shaman
who hates every tribe on the continent, joined Humanis, went mad two years ago, and split the policlub
with a plan to blow the NAN apart. Brackhaven wants him stopped before Humanis gets blamed for a war.

A road movie follows. The Salish-Shidhe border post stages a fake quarantine so the UCAS **FBI** can
tag the runners' getaway van; Vegas **Diamondbacks** and Humanis goons hit them on the highway; a
Humanis rooftop ambush and a **Renraku** Field Op squad disguised as a squatter meet them in Las
Vegas; at **the Kokomo** they catch Liz, Bob and Sammy planting a data chip that lures their decker
into the **Pueblo Corporate Council's Net**, where Jesse's psycho decker **Ram** springs a trap
built to make Pueblo blame the Sioux Wildcats. Special Agent **Clive Drummond** and Agent **Della
Cooper** spring theirs, and ten Renraku troopers crash it. In Provo the trail runs through an
abandoned wire works into **Provo-Under**, the tunnel home of the **Underground Awakened** ork-and-troll
tribe under **Mary Hawkmoon**, past the Barrelhouse Boys' BTL crew and the paranoid troll **Crunch**,
who believes he is a Sioux Special Forces recruit -- until **Aurora** shoots anti-BTL crusader
**Maureen Westlake** from a rooftop and leaves Crunch's corpse as the 'Sioux sniper'.

Home again, Jesse ('Denny Sam') is on **Council Island** with a stolen Renraku tonal generator wired
into the **Grand Council Lodge's** air ducts to turn a touchy Salish-Shidhe Council session into a
brawl. Disarmed, with cyberlimbs switched off, the runners break from the gallery crowd, dodge Ranger
squads, an invisible Renraku mage and an invisible Agent Cooper, and face a Toxic shaman with Threat
Rating 6 and three Force 6 toxic spirits in the HVAC room at 11:55. The generator has a clearly marked
On/Off switch. The NAN, it turns out, works.
"""

TIMELINE = """
- **Day 1** -- the Blue Flame; the New Ritz meet; visas in an hour; the Salish-Shidhe border post
  (FBI arrive in 90 minutes if the team waits). **Thunder Road** two hours out of Vegas.
- **Vegas** -- rooftop ambush (Metro arrive after 20 combat turns); Ghost Wheel Street; the Renraku
  'squatter'; the Kokomo room 2R; the Pueblo Net run (Pueblo soldiers 10 minutes after a Trace);
  the FBI/Renraku three-way. Jesse leaves by unmarked helijet.
- **Provo** -- Route 666 and the Beasts; the Jones Chain and Wire warehouse; Provo-Under council
  meeting; Crossfire / Smuggler's Blues; the Carlisle; Maureen Westlake's speech (Aurora fires seven
  minutes in). Crunch's diary: officer ten days ago, 'major' six days ago, briefcase three days ago,
  'it's tomorrow' yesterday. Aurora's ticket: Sea-Tac flight next day.
- **Seattle** -- Denny Sam's three-day Council Island Inn reservation; Brackhaven's note ('the S-S
  Council meeting tomorrow'); Council meeting at noon, generator on at 11:55. Handouts dated Thursday
  October 26, 2051 ('a special meeting ... was disrupted yesterday').
"""

ORGS = [
    {
        "name": "UCAS Federal Bureau of Investigation",
        "org_type": "government agency",
        "tier": 5,
        "headquarters": "Washington FDC; Seattle field office",
        "summary": "The Bureau: Drummond's counter-terror team, chromed Fast Response Team troopers, and an Anti-Gang Squad that just leaned on the Ancients",
        "description": (
            "The UCAS federal police. Special Agent Clive Drummond runs its legendary counter-terrorism "
            "team with Agent Della Cooper and a Federal Fast Response Team -- 'the elite of the FBI "
            "combat arm and they know it': dermal plating, wired reflexes, Beretta 70 smartguns, heavy "
            "security armor, an unmarked armored van. The Bureau's Anti-Gang Squad recently tried to lean "
            "on the Ancients and has been attending memorial services since."
        ),
        "leadership": [
            {"name": "Clive Drummond", "title": "Special Agent (counter-terrorism)", "notes": "Hermetic mage; straight arrow."},
            {"name": "Della Cooper", "title": "Agent", "notes": "'The Angel of Death'; hates Humanis."},
        ],
        "notes": (
            "In Peacekeeper the Bureau knows Jesse's plan and his Humanis link, believes the policlub's "
            "leaders back him, has tailed Brackhaven, and concludes the runners are Jesse's backup. It "
            "calls in markers with the Salish-Shidhe Border Patrol to plant a passive location "
            "transponder (4,500 nuyen to the right buyer; inertial reckoning, answers an FBI "
            "interrogation pulse) in a getaway van. Orders: capture with minimum damage while Drummond "
            "lives; execution under Cooper if he dies. Phone the Feds later and it is an invitation to a "
            "trap. Afterwards Drummond and Cooper become contacts, acquaintances or nemeses depending on "
            "the number of body bags with FBI crests."
        ),
        "enemies": ["Humanis Policlub"],
    },
    {
        "name": "Native American Nations (Sovereign Tribal Council)",
        "org_type": "nation-state",
        "tier": 5,
        "headquarters": "Denver (the Sovereign Tribal Council)",
        "summary": "The NAN federation of tribal nations; First Speaker Wilson Gold Eagle; the target of Jesse John's plan",
        "description": (
            "The federation of eight sovereign Native American nations governed by the Sovereign Tribal "
            "Council, opened each session with Wilson Gold Eagle's ritual invocation ('we have come "
            "together to speak and to listen'). Jesse John's plan: stir trouble in several nations so "
            "that each blames another -- Sioux against Pueblo, Ute against Sioux, Cascade Ork against "
            "everyone -- and break the Salish-Shidhe Council on top of it."
        ),
        "leadership": [
            {"name": "Wilson Gold Eagle", "title": "First Speaker, Sovereign Tribal Council", "notes": "'Head honcho of the Native American Nations.'"},
        ],
        "notes": (
            "Aurora smuggled a recorder into a Council session to prove it could be done. Whatever the "
            "runners fail to stop (the Pueblo Net run, Westlake's murder, the Council brawl) sours "
            "relations for a while -- but 'despite the doom predicted by its detractors, the NAN works': "
            "political pressure from the other nations heals the wounds and the federation may emerge "
            "stronger. Keep that hidden from the runners for a while. Tsimshian seceded from the NAN "
            "(Jesse was raised on Hecate Strait in the Queen Charlotte Islands before that)."
        ),
    },
    {
        "name": "Pueblo Corporate Council",
        "org_type": "nation-state",
        "tier": 5,
        "headquarters": "Santa Fe (the Pueblo Corporate Council)",
        "summary": "The corporate-run Pueblo nation: the fully computerized 'Net', the PCC Matrix Defense Force, and a SecForce that looks like an army",
        "description": (
            "A NAN member run like a corporation and computerized to the hilt: every hotel room has an "
            "ISDN jack, and its corner of the Matrix -- 'the Net', capital N audible -- is half a decade "
            "ahead of anything else: black IC as the norm, 'party ice' that calls in IC from other nodes, "
            "SPASIC adaptive architecture that rewires datalines under a decker's feet. The PCC Matrix "
            "Defense Force fields young, keen corporate deckers on Fuchi Cyber-5s. Pueblo Security "
            "Force soldiers arrive ten minutes after a Trace."
        ),
        "notes": (
            "Sore point with the Sioux: Pueblo feels the Sioux government does nothing about (or is in) "
            "the BTL trade. Jesse's Vegas trap is meant to leave Sioux-tagged military code ('Wildcat "
            "MILCOMP SSF-1284') in the Parks Board watchdog subsystem so Pueblo loosens its NAN ties and "
            "edges toward secession. If Ram is also dumped, the PCC finds his untagged copy and smells a "
            "frame. The 'Pueblo sector of Vegas' has PCC security within reach."
        ),
        "enemies": ["Sioux Nation"],
    },
    {
        "name": "Ute Nation",
        "org_type": "nation-state",
        "tier": 5,
        "headquarters": "Salt Lake City; Las Vegas and Provo",
        "summary": "The Ute NAN member: wide-open Las Vegas (Vegas Metro, panzers on the Strip) and Provo with its SecForce and tunnels",
        "description": (
            "A NAN member state whose Las Vegas makes Seattle look like a church picnic: security forces "
            "that look like an army (armor, APCs, gunships), honest citizens packing more hardware than "
            "the runners, and a Ghost Wheel Street where the wealthy business traveler drives a panzer "
            "and deals in mil-spec weaponry. Vegas Metro Police are well trained, non-lethal first, and "
            "professional with prisoners. Provo, by contrast, has no Anglos on the street and a flat, "
            "calculating SecForce stare."
        ),
        "notes": (
            "Jesse's second bombshell: the assassination of Provo anti-BTL crusader Maureen Westlake "
            "framed on a 'Sioux Special Forces' troll. Success turns chilly Ute-Sioux diplomacy into a "
            "cold war. Vegas Metro block (p.23); Provo SecForce trooper block (p.49). The book calls "
            "Provo 'Pueblo' in places; see the spec header."
        ),
        "enemies": ["Sioux Nation"],
    },
    {
        "name": "Sioux Nation",
        "org_type": "nation-state",
        "tier": 5,
        "headquarters": "Cheyenne",
        "summary": "The militarized Sioux NAN member; the Wildcats (Sioux Special Forces); a BTL-exporting underworld; Jesse's chosen scapegoat",
        "description": (
            "The Sioux nation, home of the Wildcats -- the Sioux Special Forces, mountain-lion shoulder "
            "flash -- and of an underworld that recruits 'local representatives' in other nations to "
            "distribute its BTLs. The Cheyenne system holds paydata every Vegas decker dreams about."
        ),
        "notes": (
            "Framed twice by Jesse John: Sioux-tagged intrusion code in the Pueblo Net and a dead troll "
            "in stapled-on Sioux patches on a Provo rooftop. The Sioux underworld's Provo distributors "
            "were the Barrelhouse Boys. Pueblo suspects the Sioux government tolerates or runs the trade."
        ),
        "enemies": ["Pueblo Corporate Council", "Ute Nation"],
    },
    {
        "name": "Cascade Ork",
        "org_type": "tribe",
        "tier": 3,
        "headquarters": "The Cascades (Salish-Shidhe Council)",
        "summary": "Ork-and-troll tribe of the Salish-Shidhe Council under the troll chief Paul Shaggy Mountain; blamed for panzer runs and a Cle Elum uranium mine",
        "description": (
            "A Salish-Shidhe Council tribe of orks and trolls whose chief, the troll Paul Shaggy "
            "Mountain, speaks with the power of a heavy club. On the October 2051 Council agenda: other "
            "tribes accuse the Cascade Orks of aiding and abetting illegal panzer runs, and the "
            "Sinsearach are hopping mad about a Cascade Ork uranium mine near Cle Elum."
        ),
        "leadership": [
            {"name": "Paul Shaggy Mountain", "title": "Chief (troll)", "notes": None},
        ],
        "notes": "Jesse's vision: 'Cascade Ork will be against just about everyone.'",
    },
    {
        "name": "Diamondbacks",
        "org_type": "go-gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Las Vegas, Ute Nation",
        "summary": "Particularly unpleasant Vegas go-gang under 'The Edge'; hired by Humanis hotheads to head the runners off on the highway",
        "description": "A Vegas go-gang that lives for the thrill and will die for it as long as it takes an 'honor guard' along. Eight riders on armed Harley Scorpions; The Edge and her two lieutenants mount Ingram Valiant LMGs on firm points.",
        "leadership": [
            {"name": "The Edge", "title": "Leader", "notes": "Rams her bike into the enemy's grille rather than lose."},
        ],
        "notes": "Member block p.20 (dermal plating 1, hand razors, TMP SMG, armor vest, Bike 5). Knew nothing about Jesse -- 'just hired for a bit of fun' by Humanis goons in a stolen Westwind 2000.",
    },
    {
        "name": "The Beasts",
        "org_type": "go-gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Route 666, between the Ute-Pueblo border and Provo",
        "summary": "Nasty go-gang that claims a stretch of Route 666 and hunts travelers with an ultralight grenadier",
        "description": "Ten riders two-up on five Harley Scorpions ('gunners' behind the drivers with Roomsweepers, one with a monofilament whip) plus a scout in a tiny ultralight who drops six defensive grenades on a convoy before the head-on charge. The highway's scorch marks and craters are their signature.",
        "notes": "Member block p.38: low-light cybereyes, hand razor, Browning Max-Power. They break off and flee away from Provo when losing.",
    },
    {
        "name": "Underground Awakened",
        "org_type": "tribe",
        "tier": 2,
        "headquarters": "Provo-Under, the tunnels beneath Provo, Ute Nation",
        "summary": "Tribe of goblinized orks and trolls living the old ways in the tunnels under Provo; chief Mary Hawkmoon",
        "description": (
            "After the Awakening most goblinized tribe members became tribeless 'lost ones' in the "
            "cities; these orks and trolls banded together instead, took the old sewers and storm drains "
            "under Provo, and built a strong, stable tribe reconciling the old ways with their new bodies. "
            "Council meetings are informal and open, held in a sunlit hydroponic garden room; a Force 6 "
            "city spirit stands sentry. 'Sometimes I think those guys have got it together better than "
            "we do up here.' Street rumor calls them a BTL crime family; the council is trying to stamp "
            "out the couple of rotten apples who are."
        ),
        "leadership": [
            {"name": "Mary Hawkmoon", "title": "Chief (troll; Dog shaman)", "notes": "Daughter of an influential Ute subchief."},
        ],
        "notes": (
            "About 24 present at a council: ten trolls (Troll Bouncer), eleven orks (Ork Mercenary, less "
            "hardware), three ork shamans, plus eight councillors and spectators. Reception depends "
            "entirely on how Joey was treated. They know nothing of Jesse and will not fight him; they "
            "forbid exploration beyond the garden room. Geeking Joey costs Karma and the tribe's goodwill."
        ),
    },
    {
        "name": "Barrelhouse Boys",
        "org_type": "gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "A side room off the Provo-Under tunnels",
        "summary": "Six scared young orks and the troll Crunch running Sioux BTLs in Provo-Under; small fish who set a grenade tripwire",
        "description": (
            "Six orks in their early twenties (Zachery, Rick and four others) and a troll named Crunch "
            "who took a Sioux underworld 'marketing assignment' for the thrill and found themselves "
            "armed when the police clamped down. Crunch swore them to a blood oath to kill anyone who "
            "came sniffing; they are horrified by what their own grenades do and glad to surrender and "
            "confess. Nobody outside the group knows the name."
        ),
        "leadership": [
            {"name": "Crunch", "title": "Enforcer (troll; deceased)", "notes": "Jesse's patsy."},
        ],
        "notes": "Hidden weapons: five Ruger Super Warhawks, one defensive and two offensive grenades, a small stash of light-entertainment BTLs. Crunch's note gives the Carlisle, Center St and 4th West, room 12.",
    },
]

LOCATIONS = [
    {
        "name": "Blue Flame Tavern",
        "location_type": "bar",
        "district": "Seattle",
        "security_level": "Low Security",
        "summary": "Dark runners' tavern where the booths hold hulking chrome and the Chinaman waters your drinks; Bobsie Twins find the team here",
        "description": (
            "A dark tavern that vibrates with barely repressed violence: cramped booths along the side "
            "wall full of hard, angular, glinting shapes, eyes glowing or reflecting the washed-out neon "
            "of the beer sign, the subliminal hiss of a spur sliding out of its sheath. Nothing ever "
            "changes at the Blue Flame. The team has a regular booth; there is a back door."
        ),
        "notes": "'First round on the house' means he shortchanges you later or waters the second round. Where the Bobsie Twins deliver Brackhaven's invitation.",
    },
    {
        "name": "The New Ritz Hotel",
        "location_type": "hotel",
        "district": "Fourth and Blanchard, downtown Seattle",
        "security_level": "Corporate High Security",
        "summary": "Third incarnation of the Ritz: sumptuous exec hotel with an Edwardian-club lounge, weapons checked at the door, a controllable venue for the right price",
        "description": (
            "The first Ritz was Old World charm in the early 20th century; the name passed to a flophouse "
            "on the bad end of Denny Way that burned in 2040, and the New Ritz rose as a haven for "
            "high-level corporate execs -- cutting-edge labor-saving tech behind old-fashioned comfort, "
            "impeccable staff. The lounge is an Edwardian gentlemen's club: Afghan rugs, dark oak tables, "
            "burgundy wingbacks, bookcases, a working fireplace, and hidden tech -- a Rating 7 white-noise "
            "generator at every table and a Rating 6 ward over the room. Almost empty at these prices."
        ),
        "notes": (
            "The maitre d' with the almost-real European accent is a Street Mage (fighter) standing in an "
            "electronic-scanner alcove (7 dice vs Concealability); weapons are checked, refuseniks wait "
            "in the foyer. Security team within a minute: five corporate guards (partial heavy armor, "
            "stun batons, tasers, Uzi IIIs), a Company Man, two wage mages -- neutralize and expel. For "
            "1,000 nuyen the maitre d' logs a bill to an Aztechnology expense account and 'guest services' "
            "erase any record you were there. Messages for 'Mr. Johnson' at the front desk."
        ),
    },
    {
        "name": "Salish-Shidhe Border Post (Seattle crossing)",
        "location_type": "government building",
        "district": "Seattle / Salish-Shidhe border",
        "security_level": "Corporate High Security",
        "controlling_org": "Salish-Shidhe Council",
        "summary": "Humorless Border Patrol blockhouse with a crash-proof gate; four officers outside, more inside, Rangers and a Citymaster when the Feds ask",
        "description": (
            "A blockhouse and closed crash-proof gate (Body 6) where four lightly armed Border Patrol "
            "officers stand outside and at least four more wait inside, armed to the teeth and bored. "
            "Map p.17: parking lots on both sides, barrier control booth, reception desk, guard room, "
            "storage (customs forms in quadruplicate, coffee filters), and a spartan waiting room with a "
            "torn vinyl sofa, one lockable door and one unlocked back window with a visibly broken alarm."
        ),
        "notes": (
            "Peacekeeper's 'viral infection quarantine' scam: eight Salish-Shidhe Rangers and two Ranger "
            "combat mages in the guard room, a Citymaster (coaxial LMG, explosive rounds; maglock and "
            "password ignition, TN 8 via rigger port) behind the post, and a conveniently unlocked van "
            "with a passive FBI transponder by the window. Fight here and every Council paramilitary comes "
            "after you on sight; kill a guard and the order is 'shoot first and get fingerprints off the "
            "corpses'. Border Patrol officer block p.17; Ranger and Ranger mage blocks p.18."
        ),
    },
    {
        "name": "The Kokomo",
        "location_type": "hotel",
        "city": "Las Vegas, Ute Nation",
        "district": "South end of Ghost Wheel Street, north Vegas",
        "security_level": "Low Security",
        "summary": "Five-storey Mediterranean apartment hotel (one Michelin star: you won't get geeked in the foyer) where Jesse interviewed deckers; room 2R",
        "description": (
            "A five-storey apartment hotel of eye-pleasing Mediterranean design where Ghost Wheel Street's "
            "top-drawer hotels give way to coffee shops and rates by the day, week or month: pygmy palms "
            "flanking the door, red tile steps, soft carpet, a rickety-looking fire escape that is "
            "actually solid and silent. Desk clerk Eric cleans his nails with a staple remover."
        ),
        "notes": (
            "Jesse ('Mr. John') interviewed deckers here, geeked one applicant for asking too many "
            "questions, hired Ram, gave him the data key, and told Eric that 'the guys' would collect "
            "what he left in 2R. Room 2R (map p.29): Liz plants the chip in the desk drawer while Bob and "
            "Sammy tidy; Liz's backpack holds one tonal generator (must be destroyed here); a note gives "
            "'Jesse -- Provo-Under, 10127 N. 11th Street, Provo, Ute'. A gray, cold astral stain runs "
            "across the lobby to the stairs -- Jesse's spoor. Thorin rents a Fuchi Cyber-4 with four "
            "hitcher jacks for 200 nuyen an hour if the team lacks a deck."
        ),
    },
    {
        "name": "Jones Chain and Wire (10127 N. 11th Street)",
        "location_type": "ruins",
        "city": "Provo, Ute Nation",
        "district": "Old light-industrial and warehouse district",
        "security_level": "No Security / Barrens",
        "summary": "Dilapidated, deserted wire works whose supervisor's desk slides aside onto the stairway into Provo-Under",
        "description": (
            "Wide dirty streets, grimy buildings, truck traffic around the clock, and one warehouse a "
            "little more dilapidated than the rest under a crooked 'Jones Chain and Wire' sign. Chain "
            "and wire-extruding machinery still bolted to the cement, spools everywhere, rust and dust, "
            "two rows of steel girders, a windowed supervisor's office. No alarms, doors unlocked, nothing "
            "alive but rats -- and a faint trace of Jesse's spiritual taint."
        ),
        "notes": "Map p.40. Joey the ork climbs in through no usual door; trigger-happy runners shoot at him. The manager's desk sits on a raised platform that slides on silent runners to reveal the stairs. The address on the Kokomo note, dated two days on.",
    },
    {
        "name": "Provo-Under",
        "location_type": "subterranean community",
        "city": "Provo, Ute Nation",
        "district": "Beneath the city (old sewers, storm drains, lifting stations and pump houses)",
        "security_level": "Low Security",
        "controlling_org": "Underground Awakened",
        "summary": "The Underground Awakened's tunnel home: scrubbed dry corridors, dim ceiling lights, a sunlit hydroponic garden council room 25 meters square",
        "description": (
            "Twentieth-century sewers and storm drains closed off as civil engineering improved, now a "
            "warm, dry home. The tunnels from the wire works are scrubbed and lit, sloping deeper "
            "underground, with fresh air and the scent of flowers from the west. The garden room is 25 "
            "meters square and nearly ten high, bright as sunlight and a riot of color like an "
            "Impressionist park -- a hydroponic garden that scrubs the air, where Mary Hawkmoon holds "
            "open council meetings. A curious Force 6 city spirit of congealed garbage with mismatched "
            "eyes watches the entrance."
        ),
        "notes": (
            "Called 'Pueblo-Under' in much of the book. The Barrelhouse Boys' tripwire grenade and "
            "cross-tunnel ambush (map p.43) or their unguarded hideout (map p.45) lie down other tunnels; "
            "the council forbids exploring further. 'What a wizzer place to vanish.'"
        ),
    },
    {
        "name": "The Carlisle",
        "location_type": "hotel",
        "city": "Provo, Ute Nation",
        "district": "Center Street and Fourth West (low-rent district)",
        "security_level": "No Security / Barrens",
        "summary": "Half a step up from a flophouse; Crunch's room 12, papered with mercenary posters, with troll blood under the bed",
        "description": (
            "A few notches below the Kokomo: rats and roaches after dark, nobody at the desk, the "
            "service bell stolen, a fire-plan map in the lobby for the edification of firefighters and hit "
            "men. Room 12, second floor, off a rancid hallway: metal bed, formica table, rickety chair, "
            "cracked plaster papered with cut-out pictures of mercs and pros under a poster of the "
            "simsense anti-hero 'The Sniper'; a closet of XXL army-surplus fatigues with clumsily "
            "stapled Sioux unit flashes and a magazine photo of a mountain lion glued on as a Wildcats "
            "patch."
        ),
        "notes": (
            "Under the pillow: Crunch's unsecured pocket-secretary diary (last five entries above; "
            "Psychology TN 3 diagnoses paranoid schizophrenia, homicidal tendencies, a strong Oedipal "
            "complex). Perception TN 6: the bed has been moved; beneath it, more blood than a human "
            "holds -- troll blood, and the troll did not walk away. Westlake's speech is a few blocks away."
        ),
    },
    {
        "name": "Grand Council Lodge (Council Island)",
        "location_type": "government building",
        "district": "Council Island, Seattle",
        "security_level": "Corporate Extraterritorial",
        "controlling_org": "Salish-Shidhe Council",
        "summary": "Huge longhouse-styled council building on Council Island; circular council table, a second-floor gallery up one narrow stair, and the HVAC room where Jesse hides",
        "description": (
            "A huge, apparently wooden building in the style of a Northwest longhouse on a vast scale; "
            "inside it is laid out like any corporate headquarters. A high-ceilinged lobby hung with local "
            "native art, a council chamber dominated by a huge circular table for the tribal "
            "representatives, and a large spectator gallery one floor up reached by a single narrow "
            "stairway (30 people at a time) -- the architect's mistake that funnels every visitor and "
            "councillor past two edgy Rangers. Off the gallery corridor: three boardroom-style meeting "
            "rooms, a telecom room, an unlocked storage room, and the HVAC Control Room with its "
            "computers and large overhead ducts (simple maglocks; corridors 1-4 sealed with complex ones)."
        ),
        "notes": (
            "Map p.53. Island security for the October 2051 session: ten Council Island Police (HK227s, "
            "full heavy armor), eight Metroplex Guards (AK-98s), six Rangers and two Ranger mages, an "
            "Enfield AS7 and a bipod Panther cannon, four Yellowjackets with twin LMGs, four SAM teams; "
            "credsticks checked, persons scanned (9 dice vs Concealability), cyberlimbs disabled for the "
            "visit (Biotech B/R TN 4 to re-enable). 'One catfood-worth' of troops in the lobby and "
            "halls. Jesse's spoor leads from the stairs to the HVAC room, where a tonal generator in a "
            "main duct goes on at 11:55 for a noon session: +1 to all target numbers, every temper on a "
            "hair trigger (white-noise generator rating dice vs TN 6; Willpower 8 per turn to block; or "
            "the clearly marked On/Off switch). Ranger pursuit squads of four plus a mage every 20 turns; "
            "an invisible Renraku Field Op mage and an invisible Agent Cooper tag along. Success news: a "
            "'faulty sensor' fire alarm, a heat-pump bearing that 'sounded like gunshots'. The Council "
            "normally meets in Bellingham."
        ),
    },
    {
        "name": "Council Island Inn",
        "location_type": "hotel",
        "district": "Council Island, Seattle",
        "security_level": "Corporate Standard",
        "controlling_org": "Salish-Shidhe Council",
        "summary": "The hotel on Council Island; a credstick-confirmed three-day reservation for 'Denny Sam' that will never be claimed",
        "description": "The inn on Council Island, Seattle's Salish-Shidhe enclave, where Jesse John booked three days under the alias Denny Sam and told Aurora to take a room and wait for his call.",
        "notes": "Contact tables p.51: no major Seattle hotel holds a booking for Jesse John or Ben Johnson; the Inn holds Denny Sam's, confirmed by credstick and held safe from cancellation. He never shows.",
    },
]

NPCS = [
    {
        "name": "Jesse John",
        "role": "Tsimshian-born Toxic shaman who hates every tribe; Humanis defector plotting to shatter the NAN; aliases Ben Johnson, Denny Sam",
        "archetype": "Toxic Shaman",
        "title": "Toxic shaman; agent-provocateur (formerly Humanis Policlub)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Tsimshian (renounced)",
        "connection": 3,
        "description": (
            "Rail-thin, eyes of cold steel, sleek black hair pulled back severely into a ponytail tied "
            "with a fine silver chain; black leather vest dusty with age over an open-necked gray shirt, "
            "tight black jeans in rattlesnake-skin boots, silver toecaps, buckle and wristband; feather, "
            "leather and wood fetishes at his belt; long razor-sharp natural fingernails that gouge "
            "upholstery. No visible weapons. When he casts, his face lengthens toward a snout and his "
            "eyes go red. Laughs like something chilling; spits on carpets; 'I do not run from such as "
            "them.'"
        ),
        "background": (
            "Raised in Tsimshian tradition on Hecate Strait in the Queen Charlotte Islands before "
            "Tsimshian left the NAN; a troubled boy who killed a man at fourteen for no reason and ran to "
            "Seattle before the elders could discipline him the old way. His rabid hatred of all tribal "
            "life got him invited into the Humanis Policlub despite his face; surrounded by shared hate "
            "he grew violent and unstable and crossed into madness two years ago. Took Rat as his totem "
            "and perverted it into Toxic shamanism -- 'I use some of their skills, but only the more "
            "easily to destroy them.' His plan split the policlub; Brackhaven cut him loose; the "
            "hotheads followed him."
        ),
        "notes": (
            "Plan: (1) Vegas -- lure the runners' decker into the Pueblo Net with Sioux-tagged code; (2) "
            "Provo -- have Aurora kill Maureen Westlake and leave Crunch as a 'Wildcat' sniper; (3) "
            "Council Island -- a Renraku tonal generator in the Grand Council Lodge ducts. Stole two "
            "prototype generators from Renraku's 'Shop', liquefied a Renraku guard with Turn to Goo, "
            "argues with people who are not in the room, hides behind toxic spirits, and travels by "
            "unmarked helijet. Stats: B3 Q5 S2 C1 I5 W5, Ess 6, Magic 6; Sorcery 6, Conjuring 6, "
            "Enchantment 5, Stealth 4, Armed Combat 4; Threat Rating 6 (+1 per goal achieved). Spells: "
            "Death Touch 3, Fire Bolt 5, Fireblast 4, Mana Bolt 4, Manablast 3, Power Missile 4, "
            "Stunblast 2, Urban Renewal 2, Clairvoyance (extended) 5, Chaotic World 2, Overstimulation 5, "
            "Clout 3, Levitate Item 2, Turn to Goo 4. Orichalcum knife 3, Colt L36, lodge materials 2, "
            "stimulant patches. Final fight: two Force 6 toxic water spirits, one Force 6 toxic earth "
            "spirit. If he escapes he leaves Seattle for the next phase and comes for the runners later, "
            "stronger."
        ),
    },
    {
        "name": "Aurora",
        "role": "Big, cybered Humanis hardcase and rifle assassin backing Jesse; thinks the policlub has gone criminally soft",
        "archetype": "Street Samurai",
        "title": "Humanis Policlub hardliner; Jesse John's muscle",
        "race": "Human",
        "gender": "Female",
        "connection": 2,
        "description": (
            "A big, powerfully built woman with short-cropped dark hair and piercing dark eyes; Zeiss "
            "optics, spurs that snap out of her left forearm by reflex, a Colt Manhunter at her hip. A "
            "true believer who will fight to the death -- and who shivers at Jesse's laugh and shies from "
            "his touch. 'What are you planning, Jesse?'"
        ),
        "background": (
            "Smuggled a recorder into a NAN Sovereign Tribal Council session for Jesse to prove it could "
            "be done; watched him turn a Renraku soldier into red-gray sludge; leads 'the true heart' of "
            "Humanis he flatters as future leaders."
        ),
        "notes": (
            "Provo: hunkers below a rooftop cornice with a Ranger Arms SM-3 (APDS, smartlink) and "
            "Crunch's corpse (one bullet in the throat), fires seven minutes into Westlake's speech "
            "('drills Maureen clean between her baby blues'), shoves the troll up for SecForce to shoot, "
            "and leaves the rifle. Carries a Sea-Tac ticket for the next day; was to wait at the Council "
            "Island Inn. If SecForce would take her alive, Jesse's toxic earth spirit kills her. Under "
            "interrogation she gives the whole Ute operation, Jesse's Seattle plan in outline, and 'a new "
            "kind of bomb from Renraku'. Stats: B5 Q3(5) S6 C2 I4 W4, Ess ~0.7; Firearms (Rifles) 5, "
            "Armed Combat 5, Unarmed 4; low-light/flare cybereyes, dermal plating 2, spurs, smartlink, "
            "Wired Reflexes 2; Defiance T-250 short, armor vest with plates."
        ),
    },
    {
        "name": "Karl Brackhaven",
        "role": "Handsome, smooth Humanis Central Seattle chapter president and ex-Aztech exec posing as an Aztechnology Mr. Johnson",
        "archetype": "Policlub Leader",
        "title": "President, Humanis Policlub Central Seattle chapter (formerly a low-level Aztechnology executive)",
        "race": "Human",
        "gender": "Male",
        "organization": "Humanis Policlub",
        "connection": 4,
        "description": (
            "Early 40s, off the cover of a megacorp annual report: conservative suit, this season's "
            "power color (bright turquoise) in tie and ear-stud, a wristwatch worth a small yacht with the "
            "Aztechnology logo worked subtly into its face (Perception TN 5), a corporator's perfect "
            "teeth, bonhomie oozing. 'Sincerity's the key; once you can fake that, you're in.' Truly "
            "believes in the Humanis cause and never lets the fanaticism show."
        ),
        "background": (
            "Well educated in history and psychology; knows from precedent that Humanis must not go too "
            "far -- if the policlub is caught starting a war among the NAN it loses the limited popular "
            "sympathy it has built. A low-level Aztechnology exec before making the chapter his career, "
            "which is why the corporator act is so convincing. Called 'a moderate, whatever that means "
            "for a Humanis type'; the lunatic fringe think he has lost his cojones."
        ),
        "notes": (
            "Offers 115,000 nuyen for Jesse's neutralization, 20,000 down (his assessment of the team "
            "since the Bobsie Twins first approached them adjusts the price); promises backup that never "
            "comes; supplies a van and Salish-Shidhe visas (200 nuyen each, negotiable to zero); leaves "
            "messages at the Ritz. Sends 'Our agreement is still in force...' when the team stalls in "
            "Seattle. Pays up on success; always surrounded by heavy guard afterwards. Stats: B4 Q3 S3 C6 "
            "I6 W3, Ess 5.8; Etiquette (Corporate) 6, Psychology 7, History 5, Negotiation 5, Firearms 4; "
            "datajack 300 Mp; Colt L36, pocket secretary, wristphone."
        ),
        "contact_skills": ["Humanis Policlub politics and membership", "Corporate-Johnson theater (Ritz, Aztech cover)", "Salish-Shidhe visas and travel passes"],
    },
    {
        "name": "The Bobsie Twins",
        "role": "Two chromed born losers, Brackhaven's 'personal expediters'; loyal to whoever provides raw meat, booze, women and the occasional elf",
        "archetype": "Street Samurai",
        "title": "Humanis Policlub muscle (Bobsie One and Bobsie Two)",
        "race": "Human",
        "gender": "Male",
        "organization": "Humanis Policlub",
        "connection": 1,
        "description": (
            "Big men with close-cropped hair who look nothing alike and feel exactly the same -- the "
            "sameness of sararimen from one corporation. One stops a safe half-meter away with a voice "
            "like twenty klicks of bad road; Two stands close cover a meter back and a meter right, "
            "perfect overlapping arcs of fire. Barely enough brains between them to know which way to "
            "shoot; supercilious to metahumans and Amerindians; hand over a 2,000-nuyen credstick as "
            "'a token of my boss' earnest... whatever that means.'"
        ),
        "notes": "Each: B6(8) Q3(5) S6(8) C1 I1 W3, Ess 0; Unarmed 6, Firearms 4, Armed 4; cybereyes with flare comp, dermal plating 2, muscle replacement 2, spurs, smartlink, Wired Reflexes 2; silenced Ingram Smartgun, survival knife, Harley Scorpion. Would love to slot with the runners but have a job to do.",
    },
    {
        "name": "The Chinaman",
        "role": "Toothless, thin-voiced barkeep of the Blue Flame; free first rounds mean watered second ones",
        "archetype": "Bartender",
        "title": "Barkeep, Blue Flame Tavern",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": "A good-natured, toothless grin, a thin strongly accented voice, 'Hoi, chummers,' and 'ha?' at the end of every line. Pours your usuals without asking, warns you who came looking ('Bobsie Twins. Said they be back later'), offers the back door, and mutters 'Your funeral' when you stay.",
        "notes": "Knows what the team pulled last week. Watches the room from his haven behind the bar. No stats given (Bartender contact).",
        "contact_skills": ["Who has been asking for you at the Blue Flame"],
    },
    {
        "name": "Clive Drummond",
        "role": "FBI counter-terror legend who looks like an ineffectual favorite uncle; incorruptible, fair, and convinced the runners work for Humanis",
        "archetype": "Federal Agent",
        "title": "Special Agent, UCAS FBI (counter-terrorism team leader)",
        "race": "Human",
        "gender": "Male",
        "organization": "UCAS Federal Bureau of Investigation",
        "connection": 5,
        "description": (
            "Middle-aged, balding, soft around the edges, a kindly face with a troubled, perplexed look; "
            "speaks softly and only when he has something important to say. In FBI armor only when a "
            "situation may go volatile. 'The great equalizer': a fair shake for the side of the angels, a "
            "9mm migraine for the other side. Knows the book inside out and when to throw it away; gives "
            "a dog the first bite, just one."
        ),
        "background": "A Bureau legend who has defused more explosive situations than anyone can count, usually with surprisingly little bloodshed -- and has wiped terrorists out completely when circumstances dictated. Leads his own anti-terrorist squad; a hermetic mage of modest talent.",
        "notes": (
            "Arrives at the border post in 90 minutes; interrogates about Humanis, concludes the team "
            "was set up (Cooper disagrees) and puts them on ice in Seattle until Jesse is dealt with. "
            "Later ambushes them on a Vegas street from a parked Westwind with 13 FRT troopers in two "
            "vans; wants them alive while he lives. Stats: B3 Q4 S4 C5 I5 W5, Ess 1.8, Magic 3; "
            "Leadership 6, Etiquette (Street) 6, Interrogation 5, Negotiation 5, Firearms 5, Armed "
            "Combat 5, Sorcery 1; datajack 300 Mp, radio, smartlink; Ingram Smartgun, partial heavy "
            "armor; Analyze Device 2, Clairvoyance 1, Detect Enemies 1. Possible future contact."
        ),
        "contact_skills": ["Federal counter-terrorism intelligence", "A fair hearing from the Bureau"],
    },
    {
        "name": "Della Cooper",
        "role": "'The Angel of Death' -- Drummond's hard-option partner, a better mage with a sharper street edge, who shoots Humanis members first",
        "archetype": "Federal Agent",
        "title": "Agent, UCAS FBI (Drummond's team)",
        "race": "Human",
        "gender": "Female",
        "organization": "UCAS Federal Bureau of Investigation",
        "connection": 4,
        "description": "Early 30s, hard as steel and sharp as a knife; incorruptible, and certain she would not have been called in if the situation were ambiguous. Good shot, bad attitude, great bod, wicked temper. A miniaturized bullhorn strapped to her throat: 'Make like ice, boys and girls. Now.'",
        "background": "Fell deeply in love with an elf named Derek Rosebower, who died in a drive-by committed by a Humanis Policlub member -- a deranged individual, the policlub said, rightly; Cooper blames the club and joined the Bureau to hunt it. Drummond keeps her enthusiasm in check; without him she geeks Humanis on sight.",
        "notes": (
            "If Drummond dies the arrest becomes an execution. Tags invisible along the Ranger squad in "
            "the Grand Council Lodge with her heart set on executing the 'Humanis scum' who played her; "
            "afterwards lets the team go if the FBI morgue is empty, and watches them. Stats: B5 Q3 S4 C2 "
            "I4 W4, Ess 1.1, Magic 2; Armed Combat 6, Firearms 5, Leadership 5, Sorcery 2; datajack, "
            "low-light/flare cybereyes, retractable razors, smartlink, radio; Ares Predator, FN HAR, "
            "full heavy armor, grenades; Invisibility 2, Power Bolt 1, Detect Enemies 1."
        ),
    },
    {
        "name": "Ram",
        "role": "Denver decker-for-hire, brain-damaged sociopath from running the Pueblo Net naked; Jesse's hired Fairlight artist",
        "archetype": "Decker",
        "title": "Decker-for-hire (Denver)",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "Early 30s, a nasty piece of work, high-strung and 'a certified psycho' who geeked the joygirl "
            "he lived with for using his razor and is more likely to kill you if you look at him first. "
            "Matrix icon: a huge black-furred humanoid with glaring red eyes, fangs and a neon-red laser "
            "katana. 'So you've come to get me, huh? Then come on. Let's play.'"
        ),
        "background": "Honed his skills as a kid running the Pueblo Corporate Council Net naked; black IC left his intellect intact and his personality warped -- other people are tools or obstacles. First-class reputation out of Denver; young deckers want to be him. Almost as formidable outside the Matrix.",
        "notes": (
            "Hired at the Kokomo with a data key for SAN 0010AF and a 1 Mp 'key' that rewires SPU-5 from "
            "CPU-1 to SPU-6; his access utility lacks the Sioux tag. Runs mirrors to SPU-5, trips the "
            "alarm on purpose, attacks for three turns, smokes out to CPU-1 and flips the architecture. "
            "Stats: B2 Q3 S2 C1 I5 W3, Ess 1.8; Computer 6, Computer Theory 4, Electronics 4, Armed 3, "
            "Firearms 3; Hacking pool 11; Fairlight Excalibur with Response Increase 2; Attack 6, Bod 6, "
            "Evasion 6, Masking 6, Sensors 6, Mirrors 5, Smoke 5, Shield 4, Medic 2; Uzi III, shuriken. "
            "Karma 2 if killed or dumped."
        ),
    },
    {
        "name": "Liz",
        "role": "Petite blonde Humanis hardliner who looks like a harmless airhead until she gives orders; carries a tonal generator she will shoot rather than surrender",
        "archetype": "Policlub Operative",
        "title": "Humanis Policlub (Jesse John's faction)",
        "race": "Human",
        "gender": "Female",
        "organization": "Humanis Policlub",
        "connection": 1,
        "description": "The intellectual of her cell: a petite blonde with a fine body (all hers) and the snap of command the moment she opens her mouth. 'Life's a bitch, so I might as well be one.' 'Can it! Aurora's righteous.'",
        "notes": "Plants the data chip in Kokomo 2R and carries one of Jesse's two stolen tonal generators to a meet; puts a round into it herself if magic or trickery threatens. Suspects the chip is a trap; knows Jesse hired Ram. Stats: Uzi III with smartlink, armor vest; Leadership 2, Negotiation 3, Firearms 4. Fights to the death once it starts.",
    },
    {
        "name": "Bob",
        "role": "Humanis goon big and ugly enough to pass for a troll in dim light -- never say so; sworn to back Jesse with his life",
        "archetype": "Policlub Thug",
        "title": "Humanis Policlub (Jesse John's faction)",
        "race": "Human",
        "gender": "Male",
        "organization": "Humanis Policlub",
        "connection": 1,
        "description": "A non-Awakened human and fragging proud of it, mistaken for a troll in bad light (the surest way onto his bad side). Heard Jesse screaming at an empty room on guard duty and nearly got fried opening the door: 'He's losin' it. And that Aurora...'",
        "notes": "Stats: B6(8) Q3(7) S6(10) C2 I3 W3; Unarmed 5, Firearms 4, Armed 4, Stealth 3; muscle replacement 4, smartlink; Uzi III, armored vest. Knows nothing about the chip; Jesse contacts him, never the reverse.",
    },
    {
        "name": "Sammy",
        "role": "Steroid-bulged Humanis goon slightly less intelligent than a vending machine, with an instinct for violence",
        "archetype": "Policlub Thug",
        "title": "Humanis Policlub (Jesse John's faction)",
        "race": "Human",
        "gender": "Male",
        "organization": "Humanis Policlub",
        "connection": 1,
        "description": "Like Bob but more so: his muscle bulges have bulges. A long-time steroid abuser with limited faculties and an instinctive skill for violence. 'He's getting flaky. You've seen him, Bob.'",
        "notes": "Stats: B6(7) Q2(6) S6(10) C1 I1 W2, Ess 2.5; Unarmed 6, Firearms 5, Armed 5; right cyberarm with smartlink and increased strength, dermal plating 1, muscle replacement 4; Uzi III, armored vest. Would never think to run and warn Jesse.",
    },
    {
        "name": "Eric",
        "role": "Room-temperature-IQ desk clerk of the Kokomo who cleans his nails with a staple remover",
        "archetype": "Desk Clerk",
        "title": "Desk clerk, the Kokomo (Las Vegas)",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": "A bored career desk clerk, unable to handle anything more challenging, who watches armed strangers creep up his stairs with total disinterest. 'If you're after the job, you're too late. The man left... Or did you want a room?'",
        "notes": "Keeps the register behind the desk and a holdout pistol under it (used only when danger is obvious even to him). Won't give room numbers after the interviews -- intimidate or trick him. Remembers Jesse's instruction that 'the guys' can collect what was left in 2R.",
    },
    {
        "name": "Thorin",
        "role": "Unabashed technology fan in Vegas who rents a dead client's Fuchi Cyber-4 by the hour",
        "archetype": "Deck Technician",
        "title": "Cyberdeck repair tech (Las Vegas)",
        "race": "Dwarf",
        "gender": "Male",
        "connection": 2,
        "description": "Friendly to anyone who shares his appreciation of well-designed technology. Was repairing a Fuchi Cyber-4 with four hitcher jacks when its owner got herself geeked before she could pick it up; rents it to a like-minded friend for 200 nuyen an hour.",
        "notes": "No programs, but knows shadow sources for them. Race not stated in the book; the name suggests a dwarf.",
        "contact_skills": ["Cyberdeck rental and repair in Vegas", "Shadow program sources"],
    },
    {
        "name": "Joey",
        "role": "Smart-talking thirteen-year-old ork of the Underground Awakened with an adult's body and a kid's mouth; the team's guide into Provo-Under",
        "archetype": "Street Kid",
        "title": "Underground Awakened (tribe member, early teens)",
        "race": "Ork",
        "gender": "Male",
        "age": 13,
        "organization": "Underground Awakened",
        "connection": 1,
        "description": "The kind of twerpy kid who should be kept from society until 21, in a body that reached maturity early. Climbs into the wire works through no usual door, dives behind a filing cabinet screaming 'don't kill me!' when the runners shoot, and, if asked, guides them down: 'Hey, guys, look who I've brought.' Everything he knows about the tribe is filtered through thirteen.",
        "notes": "Stats: B2 Q5 S2 C3 I3 W3, Ess 6; Etiquette (Tribal) 4, (Street) 3; a smartlink he has no gun for. Gear: Urban Brawl trading cards, a 'Neil the Ork Barbarian' action figure, a well-viewed page from Playork. Karma -1 if he dies; the tribe's welcome depends on him.",
    },
    {
        "name": "Mary Hawkmoon",
        "role": "Troll Dog shaman chief of the Underground Awakened; a Ute subchief's daughter who builds consensus and protects her new tribe implacably",
        "archetype": "Tribal Chief",
        "title": "Chief, Underground Awakened (Dog shaman)",
        "race": "Troll",
        "gender": "Female",
        "organization": "Underground Awakened",
        "connection": 4,
        "description": "Big and ugly, a typical troll, with the manner of a kindly, strong-minded young woman. Chosen chief for her gift at orchestrating consensus among factions; holds open council in the hydroponic garden she loves. Lives by the tribe's rules and the nation's, and reacts strongly to suggestions the tribe deals BTL.",
        "background": "Daughter of an influential Ute subchief; goblinization made staying impossible. Has dedicated her life to protecting and strengthening the Underground Awakened and is the implacable enemy of anyone who harms it.",
        "notes": "Knows nothing of Jesse; has heard rumors of a small unsanctioned BTL group and will not name names on hearsay; refuses to fight Jesse (no evidence of a crime) but lends Joey as a guide and, if she hears Zachery confess, lets the team visit his partners. Stats: Conjuring 6, Etiquette (Tribal) 6, Sorcery 4, Firearms 4, Enchantment 3; Magic 4; Detect Enemies 3, Mana Bolt 4, Powerball 5, Power Bolt 3; knife, lodge materials, detection fetish. Summoned the Force 6 city spirit sentry.",
        "contact_skills": ["Underground Awakened tribe and Provo-Under", "Ute tribal politics (her father's circle)"],
    },
    {
        "name": "Zachery",
        "role": "Small, sneaky, abjectly cowardly ork of the Barrelhouse Boys who runs to warn his crew and confesses everything when caught",
        "archetype": "Gang Member",
        "title": "Barrelhouse Boys (BTL runner)",
        "race": "Ork",
        "gender": "Male",
        "age": 25,
        "organization": "Barrelhouse Boys",
        "connection": 1,
        "description": "About 25, small and sneaky; pushes through the council crowd toward a tunnel the moment the runners mention Jesse. Fights only until threatened with real hurt, then surrenders and begs; keeps his head down through the ambush; blurts out where Crunch is if nobody asks, to fierce looks from his friends.",
        "notes": "Stats: B2 Q4 S2 C1 I2 W2; Unarmed 4, Stealth 2; armor vest, Colt L36, knife. Leads the team to the hideout if captured.",
    },
    {
        "name": "Crunch",
        "role": "Paranoid, homicidal troll enforcer of the Barrelhouse Boys who believed a 'Sioux Special Forces major' recruited him; murdered and framed as Westlake's sniper",
        "archetype": "Gang Enforcer",
        "title": "Barrelhouse Boys (deceased)",
        "race": "Troll",
        "gender": "Male",
        "organization": "Barrelhouse Boys",
        "connection": 1,
        "description": "As hard as the other Boys pretend to be; kept them in the BTL trade by intimidation, then started talking crazy. His room at the Carlisle is a shrine to 'The Sniper' and hard men; his fatigues carry stapled-on Sioux flashes and a glued magazine mountain lion for the Wildcats. 'Frag the Boys, they're nothing. I'm in the Sioux army now.'",
        "background": "Jesse, posing as a Sioux Special Forces major, courted him for ten days -- vital assignment, 'are you a good rifle shot?', a briefcase 'big surprise for anybody I don't like', questions about Maureen Westlake, the promise that the Sioux BTL traffic would be his -- and then shot him in the throat in room 12 and moved the bed over the blood.",
        "notes": "His diary (unsecured pocket secretary; a copy planted on his corpse) reads as a paranoid schizophrenic with homicidal tendencies and an Oedipal complex (Psychology TN 3). Found dead on the rooftop beside Aurora's SM-3, dressed in camo, riddled by SecForce.",
    },
    {
        "name": "Maureen Westlake",
        "role": "Middle-aged mundane Provo politician waging a neighborhood war on corruption and the BTL trade; Jesse's assassination target",
        "archetype": "Politician",
        "title": "Anti-BTL political crusader (Provo, Ute Nation)",
        "race": "Human",
        "gender": "Female",
        "connection": 4,
        "description": "A mundane with a great deal of political power and the energy of someone half her age, spent on a personal war against governmental corruption and the BTL trade. An amazing orator whose traveling road show fills bad intersections and always gets a standing ovation. 'If the people of a neighborhood resist, there can be no BTL business in that neighborhood. Never underestimate the power of the people.'",
        "notes": "The BTL czars leave her alone -- she would hurt them more as a martyr. Speaks about 15 minutes from a stage-and-PA rig at a barricaded intersection near the Carlisle with 22 SecForce troopers on crowd control; travels with armed goons she keeps off the stage. Aurora's shot comes seven minutes in. Karma 2 if she lives; a cold war with the Sioux if she dies.",
        "contact_skills": ["Provo grassroots politics", "Anti-BTL community networks"],
    },
]

ORG_UPDATES = {
    "Humanis Policlub": {
        "notes_append": (
            "Peacekeeper (October 2051): the policlub has split. President Karl Brackhaven's Central "
            "Seattle chapter ('cool heads do belong to the policlub') officially cut loose the Toxic "
            "shaman Jesse John and his plan to blow the NAN apart; the young members, borderline psychos "
            "and hotheads -- Aurora, Liz, Bob, Sammy, goons in Vegas -- back him with everything they "
            "have (the book compares it to the IRA / Provos / INLA splits). Brackhaven hires runners "
            "under an Aztechnology cover to stop him, because a Humanis-linked NAN war would kill the "
            "limited sympathy the club has built. Humanis members know it as an 'oreo' problem: 'An "
            "Indian? In the Humanis Policlub?' Humanis goon block p.21 (club, Roomsweeper, AK-97). The "
            "club is 'influential and widespread enough to make lives hell on earth' for runners who "
            "skip with a down payment. Agent Della Cooper of the FBI hunts its members on sight."
        ),
        "leadership_add": [
            {"name": "Karl Brackhaven", "title": "President, Central Seattle chapter", "notes": "'A moderate'; ex-Aztechnology."},
        ],
        "enemies_add": ["UCAS Federal Bureau of Investigation"],
    },
    "Salish-Shidhe Council": {
        "notes_append": (
            "Peacekeeper (October 2051): Border Patrol officers (Predator II smartguns, armor jackets; "
            "'main goal in life is to say he did his job') and the Salish-Shidhe Rangers ('lean, mean "
            "fighting machine'; heavy security armor, Beretta 70 smartguns, spurs, a Citymaster with a "
            "coaxial LMG loaded explosive; Ranger combat mages with Powerball 5) guard the crossings and "
            "answer favors for the UCAS FBI. The Council normally meets in Bellingham; to show goodwill "
            "it held a special open session on Council Island, Seattle, chaired by Jon Moses, with the "
            "Metroplex Guard and Rangers reinforcing the Council Island Police. Agenda: tribes accusing "
            "the Cascade Orks of abetting illegal panzer runs; the Sinsearach furious over a Cascade Ork "
            "uranium mine near Cle Elum; the Nootka demanding cuts to industry around Prince George; a "
            "UCAS rep complaining about dirty cargo shipped through the Port of Seattle. Jesse John's "
            "tonal generator nearly turned it into an Urban Brawl game; the success handout reports a "
            "'false alarm', an accord on several key issues, and three representatives sent to the NAN "
            "Sovereign Tribal Council ('the beginning of an era of closer cooperation' -- Harold Gray "
            "Bear). A Ranger shaman with Analyze Truth clears the runners; they are escorted off the "
            "island and told never to return."
        ),
        "leadership_add": [
            {"name": "Jon Moses", "title": "Chair of the October 2051 Council Island session", "notes": None},
            {"name": "Harold Gray Bear", "title": "Council spokesman (NAN cooperation)", "notes": None},
        ],
    },
    "Renraku Computer Systems": {
        "notes_append": (
            "Peacekeeper (October 2051): Renraku Seattle's new top-secret department 'The Shop' (a "
            "sonics expert poached from MCT; 'the effect of harmonics on animals... and not only "
            "animals' -- emotion control) built two prototype tonal generators, both stolen by Jesse "
            "John; four security guards died retaking them (two by an exploded door, one shot, one "
            "turned to goo). Renraku blames the runners, and squads of Field Operatives (partial heavy "
            "armor, HK227s, Wired Reflexes 2, radio; a combat mage with Hellblast 5 and Mask 3) shadow "
            "them from Vegas to Council Island, ready to interrogate in a deserted warehouse and geek "
            "afterwards. A Field Op mage tries to snatch the generator from the Lodge; keeping it brings "
            "'increasingly determined attempts' to get it back. Same week's news: Ken Shaker, a Renraku "
            "coolant technician missing from the Arcology since late November 2050, was dumped "
            "unconscious on the Downtown Lone Star precinct steps and shot dead inside it by an "
            "assault-rifle gunman."
        ),
    },
    "Lone Star Security": {
        "notes_append": (
            "Peacekeeper news (October 26, 2051): an unidentified gunman walked into the Seattle Downtown "
            "precinct with an assault rifle and killed Officer Lucas Kidd and Ken Shaker, the missing "
            "Renraku technician Kidd was trying to protect. Commander Sam McMillin, on the Universal "
            "Brotherhood bombing: 'This terrorism against the Brotherhood must end.' Lone Star passes "
            "the FBI's opinion of the runners along; phoning either is an invitation to a trap."
        ),
        "leadership_add": [
            {"name": "Sam McMillin", "title": "Commander", "notes": "Public face on the October 2051 Brotherhood bombing."},
        ],
    },
    "Universal Brotherhood": {
        "notes_append": (
            "Peacekeeper news (October 26, 2051): a bomb killed five at the Universal Brotherhood "
            "Chapterhouse in Tacoma early that morning; a black Westwind 2000 was seen outside just "
            "before the blast; Lone Star Commander Sam McMillin called it terrorism against 'a fine, "
            "upstanding group'; the Brotherhood could not be reached for comment."
        ),
    },
    "Aztechnology": {
        "notes_append": (
            "Peacekeeper: Karl Brackhaven, president of the Humanis Central Seattle chapter, was a "
            "low-level Aztechnology exec and still plays an Aztech Mr. Johnson to perfection -- logo "
            "watch, a bribed maitre d' logging his Ritz bill to an Aztechnology expense account -- "
            "counting on the corp's reputation to keep hired runners honest."
        ),
    },
    "Seattle Metroplex Guard": {
        "notes_append": (
            "Peacekeeper (October 2051): eight Metroplex Guards with AK-98s reinforce the Council Island "
            "Police for the Salish-Shidhe Council's special session; a UCAS representative attends to "
            "complain about dirty cargo through the Port of Seattle. News the same week: a 5.5 quake in "
            "the San Francisco bay area; nine Laubenstein paintings stolen from the Laubenstein Plaza "
            "Hotel lobby gallery; the Seattle Shakespeare Festival plans Macbeth, Coriolanus and The "
            "Tempest with live magic in the Kingdome next summer (Mariners manager Sludge Whittaker "
            "objects); Urban Brawl season opens with the Sprawl Scummers defending; explosions at the "
            "Brando Memorial Cemetery leave a vampire, a dzoo-noo-qua, four banshees, ghouls and "
            "dismembered members of the Church of the Whole Earth Inc."
        ),
    },
    "Seattle News-Intelligencer": {
        "notes_append": (
            "October 26, 2051 Update-Net (Peacekeeper handouts): bylines M. Perneta (cemetery bodies), "
            "N. Findley ('NAN Breakup Imminent?' quoting Jeanine Hormsley of the Annacis Institute and "
            "Alexis Potter of UW International Relations; or 'False Alarm at Grand Council Lodge'), L. "
            "Erickson (Downtown police slaying), D. Fister (Brotherhood blast). Eurocar stock soars on "
            "rumors of a cheaper Westwind-class car; corporate mages form a professional body."
        ),
    },
}

LOCATIONS.insert(7, {
    "name": "Council Island",
    "location_type": "government building",
    "district": "Council Island, Lake Washington, Seattle",
    "security_level": "Corporate Extraterritorial",
    "controlling_org": "Salish-Shidhe Council",
    "summary": "The Salish-Shidhe enclave in Lake Washington: tribal land inside the metroplex, reached by ferry or I-90 through the Council's red tape",
    "description": (
        "Seattle's Salish-Shidhe enclave, an island of tribal land in Lake Washington governed by the "
        "Council and policed by the Council Island Police (Seattle Sourcebook pp.59-62). Visitors need "
        "the same visas and travel passes as the nation proper; access is by guarded ferry docks or the "
        "I-90 road crossing. Home to the Grand Council Lodge and the Council Island Inn."
    ),
    "notes": (
        "Peacekeeper (October 2051): host of the Salish-Shidhe Council's special open session. Every "
        "visitor's credstick is checked and person scanned; obvious cyberlimbs are disabled for the "
        "stay or the visitor turned away. Council Island Police, Metroplex Guard, Rangers, four "
        "Yellowjackets and four SAM teams -- 'the big leagues'; start anything and they hose you down. "
        "The Inn holds a reservation for 'Denny Sam'. Council security hangs up on runners' warnings."
    ),
})

LOC_UPDATES = {}

NPC_UPDATES = {}

TAG_EXISTING = {}

MATRIX_HOSTS = """
**Pueblo Corporate Council Net -- Parks Board accounting watchdog subsystem** (map p.33). Every
node is half a decade ahead of the rest of the Matrix; whole Net is Orange or Red with IC rolls at +2;
black IC is the norm; 'party ice' calls IC in from other nodes; SPASIC adaptive architecture changes
datalines. Worth building as a showpiece host, with the adaptive-dataline trick as a scripted event.

| Node | Function | Rating / IC |
|---|---|---|
| SAN 0010AF | Entry from the rest of the Net; black fortress, crenelated battlements, gargoyle IC; the Sioux-tagged 'pennant' utility (8 Mp) turns it white and lowers the drawbridge | Red-5, Access 8 |
| CPU-1 | Watchdog functions | Orange-7, Barrier 7, Killer 5 |
| SPU-1 | File integrity monitor | Orange-5, Barrier 3, Trace and Burn 4 |
| DS-1 | General ledger account structure | Blue-3 |
| SPU-2 | Numerical co-processor | Orange-4, Barrier 2, Trace 3 |
| DS-3 | Real-time performance database | Blue-2 |
| SPU-3 | Traffic management co-processor | Orange-6, Barrier 4, Trace and Report 4 |
| SPU-4 | Supervisory coordinator | Orange-5, Barrier 3, Trace and Dump 5 |
| DS-2 | Inter-watchdog protocol data | Orange-1, Scramble 4 |
| SAN-2 | To another watchdog subsystem | Red-5, Barrier 5, Blaster 5 |
| SPU-5 | Adaptive overload co-processor; dataline to CPU-1 until Ram's 1 Mp key flips it to SPU-6 | Red-6, Barrier 4 |
| SPU-6 | Supervisory coordinator ('not a nice place to be') | Orange-5, Barrier 4, Trace and Dump 5 |
| SAN-3 | From an accounting subsystem; the PCC deckers' entry (Ms. Pac-Man ghost icons) | Red-5, Barrier 5 |
| CPU-2 | Reports watchdog results upward; limited expert system monitoring CPU-1 | Orange-7, Barrier 7 |
| DS-4 | Rule base for CPU-2 | Orange-4, Scramble 5, Tar Pit 5 |
| I/OP-1 | Read-only operator monitor terminal, rarely used | Blue-2, Access 3 |
| SPU-7 | Traffic management co-processor | Red-5, Barrier 4 |
| DS-5 | Security codes for the mid-level supervisory subsystem | Red-4, Scramble 7, Tar Pit 6, Black Ice 3 |
| I/OP-2 | Printer: hourly traffic reports to/from SAN-4 | Blue-2 |
| SAN-4 | To a mid-level supervisory subsystem | Red-5, Barrier 8, Party Ice 3 |

Script: Ram appears in the SAN, runs mirrors to SPU-5 via SPU-1/CPU-1, touches the barrier to raise the
alarm, fights three turns, smokes out to CPU-1 and flips the architecture; two PCC Matrix Defense Force
deckers (Fuchi Cyber-5, Hacking 11, Attack 6) enter via SAN-3 the turn after and try to dump intruders
so Trace IC can hand their location to PCC soldiers (10 minutes). Leftover tagged code = Pueblo blames
the Sioux.

**Lochlann / other systems** -- none. The Kokomo, Carlisle and Council Island Inn have no mapped hosts.
"""

NOT_BUILT = """
- **Tsimshian** (seceded NAN nation; Jesse's birthplace), **Sinsearach** and **Nootka** tribes (Council
  agenda), **Council Island Police**, **Pueblo Security Force / Matrix Defense Force**, **Vegas Metro
  Police**, **Salish-Shidhe Rangers and Border Patrol** -- on the nation / Council rows.
- **The Ritz maitre d'** (Street Mage), **Border Patrol officers**, **the Renraku 'squatter' and Field
  Op mage**, **the Humanis razorguy in Vegas**, **PCC corporate deckers**, **Rick and the other
  Barrelhouse Boys**, **the ultralight Beast** -- stat blocks noted on org / location rows.
- **Derek Rosebower** (Cooper's dead lover), **Wilson Gold Eagle / Paul Shaggy Mountain / Jon Moses /
  Harold Gray Bear** (leadership entries), **Sam McMillin, Lucas Kidd, Ken Shaker** (Lone Star /
  Renraku notes), **Jeanine Hormsley, Alexis Potter, Sludge Whittaker, Sprawl Scummers, Church of the
  Whole Earth Inc., Laubenstein Plaza Hotel, Brando Memorial Cemetery** -- news texture on the
  Metroplex Guard / News-Intelligencer rows.
- **The tonal generator** (Electronics TN 5 / 10 damaged; repair TN 15): a modulator producing
  harmonics that amplify emotion, especially anger; skull-bone conduction defeats earplugs. Kept as
  rules, not an entity. Karma: Ram dumped 2, Westlake lives 2, generator off 2, Renraku denied 1,
  Jesse taken 2, Aurora taken 1, Drummond killed -2, Joey killed -1.
- **Route 666, Ghost Wheel Street, the Provo intersection, Hecate Strait** -- described on the org /
  location rows.
"""

PLAY_NOTES = """
- A road movie (Midnight Run): keep the convoy moving and every faction misreading the runners --
  Humanis hotheads want them dead, the FBI and Renraku both think they are Jesse's backup, the
  Rangers shoot first. Nobody is on their side; the Chinaman was right about the back door.
- Brackhaven's persona should hold: the watch, the expense account, the Ritz. Let the team find out
  who paid them only through legwork (Target 6 with a photo) and let them decide about the money.
- The Pueblo Net is a trap with a scripted flip; make the decker feel the aesthetics ('the Matrix of
  your dreams') before the drawbridge closes behind him. Dumping Ram matters politically.
- Provo is a roleplaying stretch: strangers in a town with no Anglos; Joey and Mary Hawkmoon reward
  manners. Read Crunch's diary aloud.
- Westlake's speech is a clock (seven minutes); Aurora will not miss; the toxic earth spirit hunts
  anything astral and follows through walls.
- Council Island strips the team of guns and cyberlimbs. The generator has an On/Off switch: the
  win condition is reaching it, not killing Jesse. Feed in Rangers, the Renraku mage and Cooper as
  needed on either side.
- Aftermath: enemies for life among the FBI, Humanis, Renraku, the Rangers, the CIP and two nations'
  SecForces; Jesse at large if he escapes; and the reassurance -- hidden from the players for a while
  -- that the NAN works.
"""
