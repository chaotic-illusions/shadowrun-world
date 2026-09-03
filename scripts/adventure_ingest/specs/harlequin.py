# Harlequin (FASA 7306, 1990; OCR text is the SR2 printing) -- campaign order #9. Eight mini-adventures
# meant to be interspersed with other runs: Seattle (Bellevue, Downtown, Puyallup, Auburn, Tacoma),
# Bavaria, Amazonia, Columbia (Missouri) and Mount Saint Helens. In-world spring 2051: the intro
# boilerplate still says "the year is 2050", but the APN pamphlet is dated "Seattle, 2051" ("earlier
# this year"), the YET legwork excerpt is "Seattle Political Database, March 2051", and the Sylvan /
# APN / Who's Who excerpts are August-October 2050 editions.
# Editing inconsistencies in the book, recorded in the affected notes:
#   - Sylvan's First Senior Editor is "Brand Gylgalad" on p.16 and "Elrand Gylgalad" at I/O 30 and file 6-003.
#   - Morlock's second meet is at "Tower 801" (p.20) although the first is the Laubenstein Plaza penthouse.
#   - Trey is "no more than 18" in the meet text and "16" in the cast list; Charlie's envelope becomes a
#     "videodisc" in the Karma table.
#   - The YET hall has "Force 8 Wards" on the admin offices and Ehran's suite (p.58) but a "Force 10 Ward"
#     on the suite in the map key (p.60).
#   - Ehran's plantation is "Fonte do Sul" and "Fonte do Sol"; Anson Helm is also "Helms"; Columbia is in
#     the "OCAS" and the safe house was cleared by "OCAS agents" (both UCAS).
#   - Jane Foster's spell lock is in her RIGHT thigh in Future (p.122) and her LEFT thigh in Present (p.128-129).
#   - The APN has "about 300 members" (p.22) and "an active membership of 200" (legwork, p.143); Fierelle is
#     missing from the registered council of six.
#   - Tarislar's ashfall is "35 years ago" from 2017 (would be 2052); treated as loose prose.
# Source text: docs/Adventures/text/SR2-Harlequin.txt (153 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "Harlequin"
ORDER = 9
SOURCE = "SR2-Harlequin.pdf (FASA 7306), pp. 5-150"
YEAR = "2051 (spring)"

SYNOPSIS = """
Two immortal elves are playing the Great Game. **Harlequin** -- painted face, hundred-year-old guitar,
quicksilver moods -- lost his left ear to **Ehran the Scribe** in a rapier duel on a Paris bridge
centuries ago, and has invoked *chal'han che*, the honor-only form of the ritual of symbolic
destruction: prove power over seven aspects of the target's life (Physical, Hates, Past, Loves,
Spiritual, Future, Present) through pawns who do not know they are pawns. The runners are the pawns.
Each job takes something from Ehran and leaves behind the token of the last one.

**Physical** -- Dwarf fixer **J.P. Morlock** (Laubenstein Plaza penthouse, four Ork thugs as an
entrance exam) pays for Ehran's handwritten *Mankind Revealed* from **Sylvia Green's** safe at
**Sylvan Information** in Bellevue, plus a bunny-shaped virus that erases every copy and paints a
Renaissance rapier on every terminal. File 8-007 holds generations of genealogy with one block
deleted: Ehran's daughter. **Hates** -- fixer **Charlie Tarrow** (Takuri's) wants the six core
members of the **Association Para-Nobilis** -- elf-poser fanatics under **Xeric the Mad** in an old
fire garage in the Renraku Arcology's shadow -- shut down, their six false left ear-tips collected,
and an envelope (the manuscript's title page) left in Xeric's lap; **Harriet Taylor** in the Public
Works archive and her reporter daughter **Kerry** point the way. **Past** -- a French elven Ms.
Johnson at **After** sends the team by Luftlande transorbital (EUD hijack), bullet train and putsch
to **Schloss Munchmaussen** in Bavaria to lift the *Pandemonicus Faustus* from a rheumatic Troll
**Baron** who thinks the refrigerated valise of ear-tips is a bomb, while **Goldi** the Director of
Tourism hides Fire Elementals in the library fireplace. **Loves** -- through **Sandii** and a
gold-toothed "Lee Gorbin" (Harlequin?), the runners rob the **Young Elven Technologists'** own
system for the back-door passcodes their deckers seed into Sylvan's client software, plant one copy
and the tome's frontispiece in Ehran's private suite, and run a siphon program in **Dassurn
Securities'** Liquidations SPU -- as the APN blows the wall in.

**Counterstroke** -- Ehran answers. **Ariel**, an ancient Free Air Elemental bound by her true
name, turns a legitimate NatVat extraction at **Grantleigh Park** into a corporate-police trap,
"rescues" the team in a gas-sealed CIA van, and hands them to **Bonecrack**, his brain-damaged
Troll brother **Iggy**, the sneering **Lancelot Windtree** and the giggling torturer **Doctor What**
in a mothballed UCAS safe house on a sea cliff. **Spiritual** -- honest fixer **Anson Helm**
(Lear Platinum, 150,000 nuyen each) inserts them by stealth VTOL into Amazonia, ten days up the
Amazon with **Captain Colon**, 650 km up the Jutai with **Graeme Greene**, past friendly
Amahuacas and Ehran's Jivaro headhunters, to steal an orchid from **Fonte do Sul**, Ehran's
plantation, and flee in a militarized Stallion through a Storm Spirit. **Future** -- a brusque
Johnson at the Tacoma Style sends them to Columbia, Missouri to kidnap **Jane "Frosty" Foster**,
CommTech secretary, hidden by the **Pretenders** go-gang and a fake nun's all-girl **Flames**; the
flower is left in her flat. **Present** -- Harlequin himself, atop the ruined Southwind towers in
Tarislar, uses the spell lock Ehran grew into his daughter's thigh to fire fireworks at Ehran;
Ehran's booby-trap rebounds, the lock shatters Jane's leg, Mount Saint Helens vents, and Harlequin
sends the team into **Althain** -- marble halls, munchkin stewards, a vivisected wyvern, a chained
young dragon, a fake corpse -- where Ehran walks in alive with two rapiers, the Tir Tairngire High
Prince's **Bratach Gheal** arrive, and Harlequin takes Ehran's left ear. "We are now merely even."
"""

TIMELINE = """
- The segments are meant to be run separately, interleaved with unrelated adventures, in the order
  Physical, Hates, Past, Loves, Counterstroke, Spiritual, Future, Present. Internal clocks only:
- **Physical** -- one week to deliver the manuscript. Sylvan guards 7 a.m.-7 p.m.; staff gone by 4;
  barghests loose in the park after sundown.
- **Hates** -- no deadline; APN meets Thursday nights; a YET samurai pulled the floor plans two weeks
  ago; Sceptre's crew died five months ago; the APN hits Kerry's townhouse the night the runners visit.
- **Past** -- Luftlande Flight 613 leaves at 6 a.m., the only Berlin flight for days; Berlin -> Munich ->
  a day of border checks -> Munchmaussen; a two-day hike or a tram ride to the schloss.
- **Loves** -- Thursday-night YET party; the run must happen by Friday night; Ehran arrives Saturday;
  Dassurn audits its branches Monday morning.
- **Counterstroke** -- Marquis walks at sunset; hourly torture sessions, six hours between rounds;
  captors leave and the cell opens by timer a day after Doctor What has his ten successes; free
  teammates get the government's hint after about 24 hours of legwork.
- **Spiritual** -- flight out two days after the Sea-Tac meet; ten days upriver on the Esperanca (24
  hours in Manaus); five hours by Marsh Rose; 4.5 days by raft; half a day on foot.
- **Future** -- phone call, meet at the Tacoma Style at 8 p.m., the 12:05 Delta to Kansas City, dawn at
  Columbia Regional; Ehran's guns tried for Jane three days earlier.
- **Present** -- 24 hours of waiting, then dawn at Southwind; Mount Saint Helens vents eight minutes
  after the ritual; Mankind Revealed is delayed six months; a holocard from Phoenix a month later.
"""

ORGS = [
    {
        "name": "Sylvan Information",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Eastern Bellevue, Seattle (own landscaped park)",
        "summary": "Elven hypermedia publisher with exclusive rights to Ehran the Scribe; its deckers are YET members seeding back doors",
        "description": (
            "Seattle Corporate Record (amended October 2050): home office Seattle, UCAS; President/CEO "
            "Malachi Morgan; multi-media and hypermedia publications plus industrial software. Known in "
            "the trade as an 'Elven house' -- it publishes Elven authors and designers almost "
            "exclusively and holds publication rights to every work by Ehran the Scribe, its cash cow "
            "(it plans to publish his lecture material 'the way Campbell's was in the nineties'). A "
            "whole section of hotshot deckers codes financial and database software for some of the "
            "biggest corps in the UCAS; that is where the nuyen is really made. Also styled 'Sylvan "
            "Information Systems' in the Matrix chapter. The Young Elven Technologists funnel recruits "
            "here, and no fewer than two dozen YET deckers on the payroll leave imperceptible back doors "
            "in the packages Sylvan installs for its clients."
        ),
        "leadership": [
            {"name": "Malachi Morgan", "title": "President and CEO", "notes": "Safe holds half a million nuyen and the combinations to the other five safes."},
            {"name": "Ngon Dinh Sum", "title": "Vice President and Director", "notes": None},
            {"name": "Brand Gylgalad", "title": "First Senior Editor (Elf)", "notes": "Also spelled 'Elrand Gylgalad' on the system map and in file 6-003."},
            {"name": "Mark Fathom", "title": "Second Senior Editor", "notes": None},
            {"name": "Sylvia Green", "title": "Third Senior Editor (Elf)", "notes": "Ehran's editor; the handwritten Mankind Revealed sits in her safe (5L, 8R, 18L)."},
            {"name": "Mei Lei Fujiwara", "title": "Fourth Senior Editor", "notes": None},
        ],
        "notes": (
            "Harlequin's Physical target. Currently converting Ehran's Mankind Revealed to hypermedia; "
            "after the virus, publication is delayed six months ('Ehran is ill'). In-house security is "
            "four unarmored rent-a-cops with AZ-150 stun batons (7 a.m.-7 p.m.), PANICBUTTONs that bring a "
            "carload of Lone Star in three minutes, a live-in caretaker/kennelmaster (Street Cop stats) "
            "with four barghests loose in the park at night, a 3 m electrified fence (5M4) and a Sony-Cray "
            "10000 in a refrigerated basement (Maglock 5). Its computer system (SAN 9206 (24-1209)) is a "
            "sculpted primeval forest -- see the Matrix section; file 8-007 (Restricted, 240 Mp) is "
            "generations of genealogical and biomedical surveillance on dozens of families since 1834 "
            "with one deleted block: a Midwest female in her late twenties, i.e. Jane Foster. Ehran "
            "'controls' Sylvan through the YET (DS-16 references). Files on the six executives (6-001 to "
            "6-006) link to safe combinations (9-201 to 9-206)."
        ),
        "allies": ["Young Elven Technologists"],
    },
    {
        "name": "Young Elven Technologists",
        "org_type": "policlub",
        "tier": 3,
        "headquarters": "Fire Station 118, Puyallup Barrens, Seattle",
        "summary": "Ehran the Scribe's influential Elven policlub of deckers; modern-world Elves who despise the 'Elven ideal'; enemies of the APN",
        "description": (
            "Seattle Political Database (March 2051): headquarters Seattle, UCAS; leader John Winter; "
            "officers Nick Francis (Indoctrination), Patricia Stein (Recruitment), Alex Manke (Security). "
            "An influential Metahuman policlub in the Puyallup Barrens whose major benefactor and "
            "chairman, Ehran the Scribe, underwrites most expenses through his North American lecture "
            "tours and writes all its literature. The YET hold that Homo nobilis can prosper in the "
            "modern world without eons-old stereotypes, and combat the Association Para-Nobilis 'through "
            "logical, reasoned debate' -- and, when pushed, superior firepower. Around three years old; "
            "some core members came out of a Metahuman gang formed after the Night of Rage. Open to "
            "non-Elves at Ehran's insistence, to some members' disgust. Recruits deckers hard at the "
            "University and on the decker BBSs, then funnels them to a multimedia house in the Barrens "
            "(Sylvan Information), where they write financial software with back doors the policlub "
            "uses to siphon funds when necessary."
        ),
        "leadership": [
            {"name": "Ehran the Scribe", "title": "Chairman and benefactor", "notes": "Keeps a private suite at the hall; visits about monthly with an entourage."},
            {"name": "John Winter", "title": "Leader (registered)", "notes": "Named only in the legwork excerpt."},
            {"name": "Nick Francis", "title": "Indoctrination", "notes": None},
            {"name": "Patricia Stein", "title": "Recruitment", "notes": None},
            {"name": "Alex Manke", "title": "Security", "notes": "Elven Street Samurai; holds the armory passkey; hired three Troll samurai for the party."},
        ],
        "notes": (
            "Meets in an old pre-Awakening fire station bought from the city (Fire Station 118); throws "
            "recruiting parties with real food, a mini-mono musician and simsense, doorman with a "
            "Detek-It hand wand, three hired Troll Street Samurai with Ares MP-LMGs, and a strike force of "
            "six Elven poser bruisers and two Elven Hitmen. Six guards early evening, three after 11 p.m. "
            "Armory (Barrier 24): 4 HK227, 4 Ares MP LMG, 6 Ares Predator, 9 armor jackets. Computer "
            "room of 40 workstations with 2D6 Elven Deckers jacked in; system SAN-0 LTG 4206 (47-2551), "
            "Ehran's private line 4206 (47-1378) -- see Matrix section. Only the admin offices and "
            "Ehran's suite are warded (Force 8 on p.58, Force 10 on p.60). Harlequin frames the club for "
            "computer piracy via Dassurn; the APN then blows a 4 m hole in the south wall with ten "
            "MP-5TX gunmen; both Elven groups end up hunting the runners together. YET Muscle contact "
            "(four security brutes) closes on a traced decker in 1D6 minutes. After Harlequin, Ehran "
            "forbids any retaliation against the pawns; relations are neutral but reserved."
        ),
        "allies": ["Sylvan Information"],
        "enemies": ["Association Para-Nobilis"],
    },
    {
        "name": "Association Para-Nobilis",
        "org_type": "policlub",
        "tier": 2,
        "headquarters": "Old city fire garage in the Renraku Arcology's shadow, near Post and University, Downtown Seattle",
        "summary": "Radical 'back-to-nature' Elven policlub of surgically altered human posers who murder Elves with swords and bows; Xeric's Council of Elders",
        "description": (
            "Seattle Political Database (August 2050): leader Aaron Mitchel (aka Xeric); a governing "
            "council of six (Xeric, Allair, Erendahl, Thiran, Blaine Deathedge registered; Fierelle "
            "unlisted); about 200 active members in Seattle (the text says 300), none elsewhere. Founded "
            "in 2040 by Leo Ridgeworth 'to protect Homo nobilis' after the riots of 2039 killed 4,739 "
            "Elves. Ridgeworth died in a suspicious monorail accident in 2043; his secretary Aaron "
            "Mitchell trained the 27 members as soldiers and waged a covert war that killed most of the "
            "APN's enemies and all but six of its members -- the survivors became the Council of Elders "
            "and Mitchell became Xeric. Rebuilt by recruitment; most members only attend the Thursday "
            "meetings ('The Role of Elves in Modern Society', 'The Humanis Threat', 'Thwarting Misguided "
            "Metahumans') and pass out literature in Seattle's lower schools. The inner circle live and "
            "breathe the ancient Elven stories, push a return-to-nature ideal, and murder Elves who "
            "reject it with archaic weapons. And they ain't real Elves: the core are posers with "
            "cosmetic surgery and false ear tips. Some corp backing (unnamed)."
        ),
        "leadership": [
            {"name": "Leo Ridgeworth", "title": "Founder (deceased 2043)", "notes": "Monorail accident nobody could prove was murder."},
            {"name": "Aaron Mitchell", "title": "Leader, 'Xeric the Mad'", "notes": "See NPC row."},
            {"name": "Fierelle the Red", "title": "Council of Elders (senior to Xeric)", "notes": "Wavering."},
            {"name": "Allair Shadowdeath", "title": "Council of Elders; alarm and BTL chip maker", "notes": None},
            {"name": "Blaine Deathedge", "title": "Council of Elders; enforcer", "notes": None},
            {"name": "Thiran", "title": "Council of Elders; Weapons Master", "notes": None},
            {"name": "Erendahl", "title": "Council of Elders; raid leader", "notes": None},
        ],
        "notes": (
            "Standard weapon the Ares Crusader machine pistol; four posers awake and armed at all times; "
            "silent white alarm buttons (Xeric phones the admissions office to confirm before raising the "
            "alert); Lone Star in 2D6 minutes if heavy weapons fire. Headquarters map pp.26-30: ground-floor "
            "meeting garage with fake Elven weapons and Tolkien murals, 13-bed bunkroom with Crusaders in "
            "every other footlocker, Plan Room (Maglock 10, explosive-rigged) of contingency plans to wipe "
            "out every high-tech Elf group in the area, a basement archery range, an armory with no "
            "ammunition, an ammo room (retina scan: Thiran or Erendahl) with three HEP missiles and twelve "
            "explosive arrows that blow up in the archer's face, and a horse surgically altered into a "
            "unicorn. 19 members live in; two dozen cycles chained outside; they ride Honda Vikings. "
            "Killed Sceptre Productions' four-person video crew five months ago; lost people to a YET "
            "attack and 'are bucking for blood'. Charlie Tarrow's client pays 3,000 nuyen per false left "
            "ear tip. Remnants later assault the YET hall with ten MP-5TX gunmen in lined coats. "
            "Members: Elf Poser-Gang Member (Sprawl Sites p.110); fringe: Pedestrian."
        ),
        "enemies": ["Young Elven Technologists", "Sceptre Productions"],
    },
    {
        "name": "Sceptre Productions",
        "org_type": "media corporation",
        "tier": 2,
        "headquarters": "Seattle (owns a corp-sector townhouse used by Kerry Taylor)",
        "summary": "Media outfit that lost a four-person video crew to the APN near the Aztechnology pyramid; bankrolling Kerry Taylor's expose",
        "description": (
            "A Seattle media production outfit that sent a four-person crew to monitor the Association "
            "Para-Nobilis after rumors that its members were murdering Elves. The crew's bodies, buried "
            "in a meter of ceracrete, were found by chance the night after a bloodbath in an Elf-owned "
            "computer club, when a still-functioning wristphone led DocWagon to them. Three days later "
            "freelance reporter Kerry Taylor -- whose significant other led the crew -- quit her job and "
            "volunteered to expose the APN for Sceptre. City records list Sceptre as owner of the "
            "two-storey corp-sector townhouse (about 30,000 nuyen a month) she lives in."
        ),
        "notes": (
            "One of only two groups on the street that will dare oppose the APN (the other is the YET). "
            "Calling Sceptre gets a woman who says only that a crew was lost near the Aztechnology "
            "pyramid five months ago -- 'No comment' -- unless the runners mention Harriet Taylor's tip "
            "or Charlie Tarrow's photos, whereupon she invites them to the townhouse that evening."
        ),
        "enemies": ["Association Para-Nobilis"],
    },
    {
        "name": "Natural Vat Foods",
        "org_type": "corporation",
        "tier": 4,
        "headquarters": "Seattle operations in the Auburn District (medium-security NatVat condo complex)",
        "summary": "'NatVat' food corp whose corporate police spring Ariel's trap on the runners at Grantleigh Park",
        "description": (
            "Natural Vat Foods, NatVat on the street: a food corporation with a medium-security "
            "employee condo complex in the heavily wooded parkland of Seattle's Auburn District. Its "
            "Corporate Police (officers: Former Company Man; grunts: Corporate Security Guard) wear "
            "Partial Heavy Armor (6/4) and carry AK-97s, smartlinked for officers and laser-sighted for "
            "grunts, with Chrysler-Nissan Patrol-1s hidden in garages and a PRC-44b Yellowjacket with a "
            "chin autocannon on alert."
        ),
        "notes": (
            "Ariel, using Ehran's network and posing as UCAS intelligence, sold the security director "
            "'evidence' that clerk Shirley Marquis would hand the company's network passcodes to a "
            "shadowrun team. The director planned a massive stopper: four plainclothes in the plaza, two "
            "seven-man heavy squads (one Ingram Valiant on a gyro-mount each), three Patrol-1s to block "
            "the streets, the Yellowjacket five turns out. Prisoners are stabilized, stripped, gassed and "
            "handed to Ariel's people 'under federal jurisdiction'. The actual extraction job was "
            "legitimate; NatVat later breaks off negotiations to release captured runners."
        ),
    },
    {
        "name": "Eagle's Union of Destiny",
        "org_type": "policlub",
        "tier": 2,
        "headquarters": "Germany (pro-imperial)",
        "summary": "Pro-imperial German policlub whose agents mistake the runners for French assets and stage a zero-g 'hijack' on Luftlande 613",
        "description": (
            "A pro-imperial German policlub, the EUD, which monitors the French-aligned Ms. Johnson's "
            "meetings in Seattle and treats anyone she hires as an enemy of Germany. Its four agents on "
            "Luftlande Flight 613 -- Klaus, Fritz and Mikki (Gang Member stats with spurs) and the decker "
            "Hildi -- pose as two affectionate clean-cut couples, set off a smoke-impaction bomb at "
            "apogee, deactivate every passenger's shaped-charge restraint bracelet, and plan to execute "
            "the runners and plant evidence that they were the hijackers."
        ),
        "notes": (
            "'Mistakes happen. Go figure.' Their only weapons are spurs; they count on surprise and on "
            "victims too afraid to trigger their own bracelets. Zero-g rules p.38. Potential allies for "
            "the runners aboard: an Eskimo shaman in sealskins, three elderly Japanese 'businessmen' who "
            "are Former Company Man freelancers, and the green-haired Sky Marshal."
        ),
    },
    {
        "name": "Barony of Munchmaussen",
        "org_type": "petty nobility / micro-state",
        "tier": 2,
        "headquarters": "Schloss Munchmaussen, above the village of Munchmaussen, eastern Bavaria",
        "summary": "Single-valley Bavarian domain of a paranoid, rheumatic Troll baron; tram, spy drones, missiles, secret police and a mage tourism director",
        "description": (
            "A tiny domain of one valley on the eastern fringe of Bavaria, ruled from a mountaintop "
            "schloss by Baron (Graf) Munchmaussen, an eccentric Troll obsessed with medieval German "
            "history and his theory of a Dark Ages 'mini-Awakening' that put Trolls in Bavaria. Once a "
            "Riviera-to-Alps jetsetter, now a recluse crippled by rheumatism, crafty as a fox, who has "
            "stayed out of the politics that keep the rest of Germany in turmoil and keeps a tight rein on "
            "his subjects. Bureaucrats in the town hall and castle keep dossiers on every resident; "
            "hidden cameras watch hotels, shops, streets and the youth hostel; his guards routinely shoot "
            "down unknown aircraft, including the spy drone his neighbour Graf Eisenstein sends every week."
        ),
        "leadership": [
            {"name": "Baron Munchmaussen", "title": "Graf; ruler of the valley", "notes": "See NPC row."},
            {"name": "Goldi Schonbosom", "title": "Director of Tourism; secretly chief of intelligence and the baron's mage", "notes": None},
            {"name": "Graf Eisenstein", "title": "Neighbouring baron (rival)", "notes": "Sends a weekly spy drone; shot down every time."},
        ],
        "notes": (
            "Village cops use Detective stats; castle guards a mix of Former Company Man, Merc and Ork "
            "Mercenary (five at the gatehouse plus five asleep, four at the security checkpoint, two in "
            "the drone tower, ten off-duty in barracks, two rounds hourly, four in the keep's security "
            "center). Everybody speaks Bavarian dialect (+2 TN from ordinary German). When suspicious "
            "the baron toys with intruders: guards 'play dead' and cooperate so he can learn what they "
            "want. Neighbouring baronies are brigand states: train soldiers extort passengers (Merc with "
            "Steyr AUG-CSL) and rival 'liberators' in a Krupp Komet panzer stage a putsch. All Bavarian "
            "RTGs are Green-3; the town hall and castle systems are mapped in the Matrix section."
        ),
        "enemies": ["Munchmaussen Underground"],
    },
    {
        "name": "Munchmaussen Underground",
        "org_type": "resistance movement",
        "tier": 1,
        "headquarters": "St. Gretchen's church, village of Munchmaussen, Bavaria",
        "summary": "Feeble local resistance to the baron, run from a Gothic church by Father Braun",
        "description": (
            "The feeble resistance movement of Munchmaussen valley, centered -- unknown to the baron and "
            "his minions -- in the functioning Gothic church of St. Gretchen's under Father Braun."
        ),
        "notes": "Shelter, healing and local help for runners who fail the schloss on the first try or are captured by the baron.",
        "enemies": ["Barony of Munchmaussen"],
    },
    {
        "name": "Luftlande Airlines",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Germany (Berlin Tempelhof)",
        "summary": "German transorbital carrier (shark-tooth livery); Flight 613 Seattle-Berlin, shaped-charge restraint bracelets and undercover Sky Marshals",
        "description": (
            "A German airline flying Mitsubishi Skyclimber transorbitals under a shark-tooth emblem that "
            "gives the planes an oddly predatory look. Luftlande enforces anti-augmentation restraints "
            "with remote-activated shaped-charge bracelets and shows passengers a graphic video of what "
            "happens to rule-breakers. Flight 613 (Kapitan Georg Willems) is the only Seattle-Berlin "
            "service for several days; fewer than forty passengers, acceleration couches, seat terminals "
            "with satellite news, evac suits and reentry cushions demonstrated before takeoff."
        ),
        "notes": (
            "A green-haired young woman with a sonic damper who seems to sing silently is a Luftlande Sky "
            "Marshal (Street Cop stats, dummy restraints, concealed Net Gun); she vouches for the runners "
            "with the German security police at Tempelhof after the EUD 'hijack'. Body (3) and Body (4) "
            "tests for nausea after takeoff and at booster cutoff. Airline rules in Getting There By Air "
            "(p.144): AAA Enforcement Rating, CRC taser cuffs (4D4 Stun, three shocks), Detekt-It and "
            "Gateway scanners, sub-orbital fares 1,600 coach / 4,000 first class."
        ),
    },
    {
        "name": "Bonecrack's Gang",
        "org_type": "gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Seattle (unnamed turf); currently the CIA safe house on the coast",
        "summary": "Martin 'Bonecrack' Halloran's gangers and hired mercenaries -- the muscle Ariel rents to hold and torture the runners",
        "description": (
            "The book never names Bonecrack's gang; this row covers the gangers who run with the "
            "cold-blooded samurai (Chuckles among them) and the blooded mercenaries he hires by the job "
            "-- as many as there are runners, at least four, half of them Orks, one of each pair with "
            "Wired Reflexes 1. Bonecrack gives his gangers the loyalty they expect: he protects their "
            "cut of the contract and pays medical and legal bills. He gives employers the professional "
            "loyalty they pay for, and no more."
        ),
        "leadership": [
            {"name": "Martin Halloran", "title": "'Bonecrack', leader", "notes": None},
            {"name": "Ignatius Halloran", "title": "'Iggy', Bonecrack's brother", "notes": "Child's mind, Troll's body."},
            {"name": "Chuckles", "title": "Ganger; van gunner", "notes": "AVMs the NatVat Patrol-1."},
        ],
        "notes": (
            "Mercenary gear: Ares Predator II (Firepower ammo; Stun rounds against naked prisoners), "
            "armor vest with plates (4/3), AZ-150 Super Stun Baton, Mossberg CMDT shotgun once prisoners "
            "are armed. They will not fight odds they cannot win. Murdering Chuckles in the sealed van is "
            "on tape, and Bonecrack kills the offender when he sees it. If either Halloran is saved from "
            "dying by a runner, both become loyal allies; if Iggy dies, Bonecrack hunts the killer "
            "forever."
        ),
    },
    {
        "name": "The Pretenders",
        "org_type": "go-gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "South side of Columbia, Missouri; Highway 63 between Columbia and Jefferson City",
        "summary": "Ex-bar-band wizzer go-gang of Columbia that rides 46 km of Highway 63 and hides Jane 'Frosty' Foster",
        "description": (
            "Quite a bar band several years ago, the Pretenders never got their big break and turned to "
            "their other loves, booze and bikes. A small go-gang with a rep for mischief and mayhem on "
            "the 46-km stretch of Highway 63 between Columbia and Jefferson City -- Columbia's "
            "longest-lived gang, though their raids stay small enough that the county police have not "
            "bothered hunting them. Faded leather jackets bearing the logo; several members are mages; "
            "they make a weekly appearance at B.K.'s Lounge, staking out turf by the back bar. Not "
            "nearly as tough as their reputation: they talk the talk, and a determined team can take them."
        ),
        "leadership": [
            {"name": "The Great Pretender", "title": "Leader", "notes": "Secret crush on Frosty."},
            {"name": "Rico", "title": "Lieutenant", "notes": "Suspects her leader's feelings."},
        ],
        "notes": (
            "Helped Frosty escape Ehran's recovery team, stashed her two nights, then moved her to the St. "
            "James Home under two women members (Corporate Security Guard, Unarmed 5, Ares Light Fire, "
            "armor clothing). Members: Wiz Kid Gang Member (Sprawl Sites p.121) without cyberware. They "
            "do not pull guns unless shot at; whoever draws an automatic weapon becomes every "
            "Pretender's and bouncer's target. Interrogation (2 checks before the police arrive): 4+ "
            "successes gets 'the St. James Home for Wayward Women, on Ash Street'."
        ),
    },
    {
        "name": "The Flames",
        "org_type": "gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "St. James Home for Wayward Women, Ash Street, downtown Columbia, Missouri",
        "summary": "All-girl downtown Columbia gang of thieves fronted by a fake nun, 'Sister Ann'",
        "description": (
            "An all-girl gang working downtown Columbia -- per the tourist board, well-to-do girls who "
            "roll drunks and commit petty larceny. In truth a hardened criminal calling herself Sister "
            "Ann took over the church's St. James Home halfway house under false pretenses a couple of "
            "months ago and picks prospects with useful skills from the women returning from the state "
            "correctional institute to rob businesses and homes. Their most daring robberies have not "
            "yet been connected; if they keep succeeding they will have the money to become a force."
        ),
        "leadership": [
            {"name": "Sister Ann", "title": "Boss (posing as the home's nun)", "notes": None},
        ],
        "notes": (
            "Nine Flames (Street Cop stats without Special Skill; knife and Colt L36). Thieves, not "
            "killers; they protect Ann but will not endanger her, and surrender if she is neutralized -- "
            "they will hand over Jane and themselves for a guarantee of Ann's release. Jane Foster is a "
            "guest, not a member."
        ),
    },
    {
        "name": "Guys in Sunglasses",
        "org_type": "gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Columbia, Missouri",
        "summary": "Columbia's biggest gang, a neighborhood watch that keeps 'college boys' and 'frat rats' away from local girls",
        "description": "The biggest gang in Columbia, Missouri: something of a neighborhood watch of locals mostly interested in keeping the university's college boys and frat rats away from the local girls. Fights between the Guys and various university organizations are often brutal and lethal.",
        "notes": "Tourist-board gazetteer only (p.150). Off-stage in Harlequin.",
    },
    {
        "name": "The Spirits (Columbia)",
        "org_type": "gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Residential areas of Columbia, Missouri",
        "summary": "New Columbia gang blamed for a string of violent break-ins",
        "description": "A rather new gang that sprang up in Columbia's residential areas and is reportedly responsible for a recent string of violent incidents and break-ins.",
        "notes": "Tourist-board gazetteer only (p.150). Off-stage in Harlequin.",
    },
    {
        "name": "CommTech Inc.",
        "org_type": "corporation",
        "tier": 2,
        "headquarters": "Western edge of Columbia, Missouri, on I-70 (half a dozen wooded acres)",
        "summary": "Small but rising Columbia software house (high-class IC, a rumored shadow-market sleaze program); Jane Foster's employer",
        "description": (
            "Started as a garage industry in the late 2020s and grew into one of the best-known software "
            "companies in the area; its new facility on the western edge of town is one of the first "
            "sights on I-70. Makes high-class IC sold mostly to corps on the eastern seaboard, and is "
            "rumored to be dabbling in the shadow market with a hot-shot sleaze program 'in the cooler' -- "
            "the reason for the move to a more secure site. Still small, but going places in the UCAS "
            "market under senior software VP Josh Rehndig."
        ),
        "leadership": [
            {"name": "Josh Rehndig", "title": "Senior Software Vice President", "notes": "Jane's boss."},
        ],
        "notes": (
            "No fence, visitor parking at the door, one smiling receptionist (Corporate Secretary). Jane "
            "Foster is Rehndig's secretary (the legwork calls her executive secretary to the president; "
            "three years). Nothing she handles is worth stealing; she has no headware. Visiting earns one "
            "'mark' of unwanted attention."
        ),
    },
    {
        "name": "Bratach Gheal (White Banner)",
        "org_type": "military / royal guard",
        "tier": 3,
        "headquarters": "Tir Tairngire (the High Prince's court)",
        "summary": "The High Prince of Tir Tairngire's personal guard; four of them are sent to Althain with a Princely Order for Ehran and Harlequin",
        "description": (
            "The personal guard of the High Prince of Tir Tairngire. Four members -- Allaech (leader), "
            "Aimsir, Sruth and Taelech -- in padded studded white leather and hooded tan-and-gray cloaks "
            "arrive at Althain from 'the Land of Promise' after the magical incident at Mount Saint "
            "Helens, bearing a Princely Order that Ehran and 'this Harlequin' appear before the High "
            "Prince. They carry diplomatic passes. Sruth is a plant from the Tir's secret police, whose "
            "elite are called Paladins."
        ),
        "leadership": [
            {"name": "Allaech", "title": "Squad leader", "notes": "Physical adept, Initiate grade 3."},
            {"name": "Aimsir", "title": "Combat mage", "notes": "Initiate grade 2."},
            {"name": "Sruth", "title": "Ringer from the Tir secret police", "notes": "Records everything."},
            {"name": "Taelech", "title": "Guardsman", "notes": "Disillusioned."},
        ],
        "notes": (
            "The High Prince heard of a challenge between the influential Ehran and 'some renegade Elven "
            "sorcerer named Harlequin', stayed out of it given his history with Ehran, sent spies, and "
            "then fears the personal battle went a step too far: any hint of Elven dissent is leverage "
            "for national and corporate powers, and he already has the militant Tir na nOg to deal with. "
            "If provoked the four fight hand-to-hand and Aimsir uses Stun Blast freely; ideally they and "
            "the runners team up against Ehran's real goons. Allaech ends up ranting 'Why me?!' and "
            "trying to drag the runners back to the High Prince as witnesses. Allaech's report has no "
            "effect on Tir relations, but the runners' images are on file if Sruth survived."
        ),
        "allies": ["Tir Tairngire"],
    },
    {
        "name": "Amazonia",
        "org_type": "nation",
        "tier": 5,
        "headquarters": "Former Brazil (cities include Manaus, Macapa, Fonte Boa, Eirunepe)",
        "summary": "Awakened nation that toppled Brazil 17 years ago; pro-ecology government, regrowth rituals, touchy borders not guarded by radar alone",
        "description": (
            "Ever since Awakened forces toppled the government of Brazil seventeen years ago, the country "
            "has hardly welcomed tourists. The government employs powerful magics on the scale of the "
            "Ghost Dancers' to force accelerated regrowth of the devastated rain forest; anything that "
            "threatens the ecology is forbidden or restricted, and towns like Fonte Boa cut their "
            "vehicles free of the jungle every morning. The former Brazilian cities are pits of "
            "urbanization and decay ruled with little concern for the inhabitants; emigration is "
            "encouraged but rarely affordable. Border security is real touchy and 'does not rely "
            "exclusively on radar' -- helicopters, light aircraft, flying creatures, possibly a dracoform."
        ),
        "notes": (
            "Ehran holds 'special dispensations' for the internal-combustion vehicles at Fonte do Sul. "
            "Helm's insertion: Lear Platinum via Kansas City to an Atlantic island, seaplane to a "
            "Portuguese oil tanker hiding a Soviet IL-290 VTOL stealth transport, drop west of Macapa, "
            "tug Esperanca ten days upriver (24 hours in Manaus, population just under five million) to "
            "Fonte Boa (about 70,000) at the mouth of the Jurua, Marsh Rose 650 km up the Jutai. "
            "Eirunepe is the nearest city to the plantation. Awakened lizards, snakes, birds, insects "
            "and carnivorous or heat-sensing plants everywhere."
        ),
    },
    {
        "name": "Amahuaca Indians",
        "org_type": "tribe",
        "affiliation_contact_type": "Tribe",
        "tier": 1,
        "headquarters": "Jutai river basin, upper Amazon, Amazonia",
        "summary": "Wide-ranging, peaceful hunter-gatherer tribes of the Amazon basin who help the runners at the bidding of 'the Laughing One'",
        "description": (
            "Relatively peaceful hunter-gatherer tribes that have dwelt in the Amazon basin for thousands "
            "of years. Their chief wears scores of shell necklaces; their shaman follows a Snake totem "
            "with a Healer package (Tribal Chief, Shaman, Tribesman stats; knife, bow and 20 arrows). "
            "They offer tuber stew, pork-like roast, a meter-and-a-half worm and a fiery gourd brew, and "
            "speak a form of Tupi-Guarani on the third try."
        ),
        "notes": (
            "Harlequin sought them out after discovering Ehran's plantation and its Jivaro guards, and "
            "before hiring Anson Helm told them to watch the river and aid the team in every way short "
            "of joining the run. They tell stories of previous visits by the Laughing One but the shaman "
            "denies ever saying the words. Of Fonte do Sol they say only that a great demon-spirit lives "
            "there. 2D6 warriors shadow the runners and intervene if the Jivaro fight goes badly."
        ),
        "enemies": ["Jivaro Indians"],
    },
    {
        "name": "Jivaro Indians",
        "org_type": "tribe",
        "affiliation_contact_type": "Tribe",
        "tier": 1,
        "headquarters": "Rain forest around Fonte do Sul, upper Jutai, Amazonia (native to the Ecuador-Peru border)",
        "summary": "Shotgun-loving headhunters who worship Ehran as a warrior god's avatar and guard his plantation against anyone who comes overland",
        "description": (
            "Savages who resist all incursion with violence; farms near Eirunepe have suffered their "
            "attacks. They honor great killers, 'men with livers of stone', but believe a victim's soul "
            "will rise to destroy the killer unless the head's eyes, ears, nostrils and lips are sewn "
            "shut within hours, the skull crushed and the head tanned to fist size. Great bluffers who "
            "feast a guest, then murder him off-guard. Shotguns are their most cherished possessions. "
            "Half a dozen tribes were moved east from the Ecuadorian-Peruvian border by Ehran."
        ),
        "notes": (
            "Ehran, forewarned, killed eight of their bravest when they attacked him after a feast, let "
            "the bodies lie two days, buried them, and did not sicken and die -- so they worshipped him "
            "and obeyed his command: never set foot on the plantation, never let outsiders in except by "
            "air. War party 3D6 (half with old shotguns Ehran gave them, half with bows; Tribesman stats) "
            "plus a Raven-style shaman with the Deceiver package who flees a losing fight and later "
            "conjures a Force 3 Storm Spirit (Electrical Projection, Confusion, Fear) against the "
            "escaping aircraft. Encounter chance rises every 16 km from 96 km out; automatic at 16 km."
        ),
        "allies": ["Amahuaca Indians"],
    },
    {
        "name": "Central Intelligence Agency (UCAS)",
        "org_type": "government agency",
        "tier": 5,
        "headquarters": "Downtown offices in the UCAS Federal Building, Seattle (Langley nationally)",
        "summary": "UCAS intelligence; owns the mothballed sea-cliff safe house Ariel squats in, and quietly points the free runners at it",
        "description": (
            "The UCAS security agency whose Seattle covert-ops safe house -- a bungalow over the sea with "
            "an underground complex, clinic, cells, vault and a sea cave -- was dropped from active duty "
            "after a particularly nasty mission last year and cleared of everything valuable. Its armory "
            "alarm still rings at the CIA's downtown offices in the UCAS Federal Building: agents (Former "
            "Company Man, partial armor, Uzi IIIs) arrive in twenty minutes. The abandoned armored van "
            "from Grantleigh Park is CIA-issue, so the case gets a UCAS security rating."
        ),
        "notes": (
            "About 24 hours into the free runners' legwork, a government spook contacts them: the "
            "facility 'was used for various research projects before funding was cut', may be in "
            "unsanctioned hands, and he is authorized to release certain declassified data to private "
            "citizens -- with a reminder about penalties for illegal access to federal data networks and "
            "the usual disavowal. NatVat's security director believed Ariel represented UCAS intelligence."
        ),
    },
]

LOCATIONS = [
    {
        "name": "Laubenstein Plaza",
        "location_type": "hotel",
        "district": "Downtown, Sixth Avenue and Pike Street",
        "security_level": "Patrolled / Commercial",
        "summary": "One of Seattle's best hotels -- a 15-storey purple 'sea cucumber' of balconies; Morlock rents the whole top floor",
        "description": (
            "One of the best hotels in the city, in the heart of the shopping district close to the harbor "
            "with a great view of the Sound by day. The 15-storey circular tower bulges with so many "
            "little balconies that it looks like a purple sea cucumber. The high-ceilinged, plush-carpeted "
            "lobby has a huge old reception desk with a clerk and two Knight Errant guards, a bar and the "
            "Laubenstein Gallery, overstuffed chairs and couches, a waitress in purple tights, and sleepy "
            "geriatric music. Elevator Three takes a magkey to the penthouse."
        ),
        "notes": (
            "J.P. Morlock takes the whole top floor for his midnight meet and posts four belligerent Ork "
            "thugs at the elevator as a test of finesse (bribe from 5,000 nuyen; a diversion, a bluff, or a "
            "three-round brawl). The follow-up meet is written as 'the rooftop suite at Tower 801' -- an "
            "editing slip; treat it as the same penthouse or a second Morlock address."
        ),
    },
    {
        "name": "Sylvan Information Headquarters",
        "location_type": "corporate headquarters",
        "district": "Eastern Bellevue",
        "security_level": "Corporate Standard",
        "controlling_org": "Sylvan Information",
        "summary": "Three-storey cruciform publishing house in its own park with a koi lake, barghest kennels, an electrified fence and the Sony-Cray in a frozen basement",
        "description": (
            "Sits in the center of its own landscaped park in the wealthy east of Bellevue: lawns dotted "
            "with walnut, oak, apple and cherry, an artificial lake with three bridged islands and huge "
            "gold, orange and white fish in the northeast corner, a 3 m electrified fence around it all. "
            "The building is roughly cruciform, wings 30 m long, facing south; the second and third "
            "storeys rise over the center only. Glass-enclosed foyer with two stun-baton guards by day, "
            "three receptionists at a semicircular desk, a lobby tiled in thousands of ebony and ivory "
            "pieces, junior-editor work areas east and west (12 cubicles each with dataport terminals), "
            "a loading dock to the north, an underground garage to the west, the barghest kennel and the "
            "caretaker's one-room flat in a corridor below, and the main computer room behind a heavy "
            "coded door (Maglock 5), kept at freezing. Second floor: a receptionist and six executive "
            "offices with mahogany desks, stand-alone computers and old-fashioned mechanical safes. Staff "
            "restaurant on the third floor. More than 100 people inside by day."
        ),
        "notes": (
            "Map pp.14-16. Guards 7 a.m.-7 p.m., PANICBUTTON brings a carload of Lone Star in three minutes "
            "(three cars, two men each if it goes bad); staff gone by 4 p.m., the odd junior editor until "
            "6; only executives and senior editors allowed after six. Four barghests loose in the park "
            "after sundown (1 in 6 per turn outside; their howl summons the rest, one per turn). Entry by "
            "front or rear doors, ground-floor wing windows, the garage ramp gate or the barghest tunnel "
            "beside the loading dock -- all maglocked and alarmed. Safes: shaped thermite, a Special Skill "
            "(3+ successes vs TN 5), or the combinations from Morgan's safe / file 9-205. The manuscript "
            "(several hundred handwritten pages, terrible handwriting, English, neo-philosophical) is in "
            "Sylvia Green's safe. 30 jack-in points inside; system map in the Matrix section."
        ),
    },
    {
        "name": "Takuri's",
        "location_type": "restaurant",
        "district": "Downtown",
        "security_level": "Patrolled / Commercial",
        "summary": "One of the nicer downtown restaurants; dim lighting, a big Japanese headwaiter in a kimono, a private room behind a 'coat closet' door",
        "description": (
            "One of the nicer restaurants in downtown Seattle, fairly full and lit so dimly that nobody "
            "can identify anybody. The headwaiter, a big Japanese in classic kimono, smiles slightly when "
            "asked for a name and conducts guests through what looks like a coat-closet door into a small "
            "private dining room. Real food -- a welcome change from SushiSoy."
        ),
        "notes": "Charlie Tarrow's meet for the APN job: she orders and eats dinner (her treat) before talking business, with Wyrd at her left and young Trey posted outside the door.",
    },
    {
        "name": "Seattle Public Works Archive Hall",
        "location_type": "government building",
        "district": "Downtown (sub-basement of the Public Works building)",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "Shiawase Corporation",
        "summary": "Old nuclear shelter 14 flights below the Public Works building where 88-year-old Harriet Taylor keeps the paper records; the APN building's original plans",
        "description": (
            "The Department of Public Works is administered by Shiawase Corporation; its staff lecture "
            "armed visitors on the wisdom of bringing guns into the office and deny holding plans for "
            "buildings that are 'not a current city structure'. The Archive Hall, reached through the door "
            "marked MEN in the sub-basement and 14 flights of stairs down, was an underground nuclear "
            "shelter and keeps the concrete walls, bare bulbs and screech of rodents: roughly 150 by 40 "
            "by 5 meters of files back to the presidential election of 1900. Harriet's corner office has "
            "an overstuffed easy chair, an even older TV, and a terminal into the modern filing system."
        ),
        "notes": (
            "About 35 years ago the city computerized everything, and soon after the Crash virus trashed "
            "the records; the paper survived. Charisma (4): 0 successes, three hours of moving stacks for "
            "the APN building's plans (without the sealed doors); 1, two hours plus 'someone else asked "
            "two weeks ago'; 2, that someone was an Elf who looked like a samurai, plus Aunt Sara's Baked "
            "Brownies; 3+, an update showing the basement elevator and an introduction to her daughter."
        ),
    },
    {
        "name": "Association Para-Nobilis Headquarters",
        "location_type": "policlub headquarters",
        "district": "Downtown, in the Renraku Arcology's shadow near Post and University",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "Association Para-Nobilis",
        "summary": "Old two-storey city fire garage (Seattle Fire Department posters) with a hydraulic lift to a basement armory, archery range and a surgical 'unicorn'",
        "description": (
            "An old two-storey former city building -- the ground floor once garaged large trucks, so the "
            "ceilings top four meters -- that sits in the one patch of downtown the Arcology's "
            "light-routing system leaves in shadow. Well lit by the Arcology's display lights all evening; "
            "darkest just after dawn. Ground floor: an elevator room with ancient Seattle Fire Department "
            "posters (the hydraulic lift is worked by the far light switch), tool storage, a video room "
            "with a ladder down, the main meeting garage with Tolkien murals, fake Elven weapons, a dais "
            "and folding chairs, an admissions office with a silent alarm button, a lounge where a "
            "seven-year-old sleeps on the couch, a propaganda room, Xeric's indoctrination office (a "
            "bronzed quill of 'the Elven sage Xeric', an Ares Predator II in the drawer), Deathedge's "
            "war-museum bedroom, and Fierelle's blood-red Arabian Nights bedroom at the end of the hall. "
            "Second floor: Allair's bedroom (vid stars circled in blood red), a horror-sim 'magician's "
            "workroom' of Sloppy Soy beakers, a storeroom with 30,000 nuyen of video gear and three dud "
            "AVMs, communal baths, a 13-bed bunkroom, the main lounge (trivid on Eastern Dragons), the "
            "women's bedroom, Xeric's rice-paper bedroom, and the explosive-rigged Plan Room (Maglock 10). "
            "Basement (ladder or cargo lift only): archery range, filthy unicorn stable, armory without "
            "ammunition, retina-locked ammo room, Thiran's bedroom of UrbanBrawl and Thai kick-boxing "
            "magazines."
        ),
        "notes": (
            "Maps pp.26-30 with alarm-raised and no-alarm placements for every room; 19 live-in members, "
            "up to two dozen cycles chained outside; at least four posers awake and armed; sealed doors "
            "that the original Public Works plans do not show. Lone Star in 2D6 minutes if an alarm or "
            "heavy weapons; Renraku's Reds must not be drawn in. Best hit: a quiet raid in the early "
            "morning. Little Maria in the lounge knows where the 'Red Woman' sleeps; Fierelle will talk "
            "and hand over her ear tips. Karma: envelope in Xeric's lap 1, each three ear tips 1, saving "
            "the girl 1, letting Fierelle atone 1, killing the girl -2."
        ),
    },
    {
        "name": "Kerry Taylor's Townhouse",
        "location_type": "townhouse",
        "district": "Corp sector (high-class part of town)",
        "security_level": "Corporate Standard",
        "controlling_org": "Sceptre Productions",
        "summary": "Two-storey luxury townhouse (30,000 nuyen a month) owned by Sceptre Productions where Kerry Taylor plans the APN's downfall; the APN hits it the night the runners call",
        "description": (
            "A two-storey luxury affair in the corp sector that probably costs someone a good 30 grand a "
            "month; city records list Sceptre Productions as owner and freelance reporter Kerry Taylor as "
            "resident. Use Large Residence, Sprawl Sites p.34."
        ),
        "notes": (
            "About an hour after the runners arrive, APN spies decide they are part of the YET conspiracy "
            "and attack with four more posers than there are runners, Erendahl watching from outside to "
            "gauge 'these new minions of the YET' before reporting to the Council that mercs or runners "
            "should be hired. Kerry keeps her magic (Former Wage Mage, Healer) as an ace in the hole."
        ),
    },
    {
        "name": "After",
        "location_type": "private club",
        "district": "Downtown, several blocks from the University of Washington campus",
        "security_level": "Patrolled / Commercial",
        "summary": "Sub-street private club decorated like a nuclear blast site -- crater nooks, melted furniture, ozone, simulated detonations -- with a snobbishly liberal crowd",
        "description": (
            "Exclusive but not too pricey, with a reputation for being snobbishly liberal; the name just "
            "isn't corporate. Down sub-street-level stairs to an oak door and a maitre d'. The place looks "
            "as if a bomb hit it -- that is the motif: meeting and dining nooks nestled in floor "
            "'craters', rubble strewn for effect, chairs and tables deformed as though half-melted, a "
            "sharp smell of ozone, dim light broken by the blinding flashes of simulated nuclear "
            "detonations, arcing wires crackling from shattered walls. Small groups argue politics and "
            "philosophy with manic ardor."
        ),
        "notes": (
            "Meet for Past: a French-accented elven Ms. Johnson in a neo-European business suit with two "
            "goons in the next nook, whose invitation came on a laser-engraved card in kaleidoscopic ink "
            "('The Place: After. The Time: Nine Tonight. The Reason: A Job Offer') after Walturr dropped "
            "her three hired musclemen. The book says University of Washington; the campaign's existing "
            "row is 'University of Seattle' -- treat as the same campus."
        ),
    },
    {
        "name": "Tempelhof International Airport",
        "location_type": "transportation hub",
        "city": "Berlin",
        "district": "Tempelhof",
        "security_level": "Corporate High Security",
        "summary": "Berlin's transorbital port; black smoke on the horizon, German security police, limo to Neustadt Station and the cannon-cupola bullet train to Munich",
        "description": (
            "Luftlande's Berlin terminal, 'no longer experiencing the difficulties reported in the morning "
            "news'. Black smoke boils up from the horizon on approach but there is no sign of active "
            "combat in the city; German security police sequester passengers for questioning. An airport "
            "limo runs to Neustadt Station, where the shark-nosed gray bullet train to Munich carries "
            "twin-mount cannon cupolas on every fourth car, seven teams of customs agents (one per German "
            "state crossed, fees in the ticket, stamps on real paper) and Taser augmentation restraints."
        ),
        "notes": "Berlin is 'such a mess' that Goldi fishes for political leanings by asking about it. Beyond Munich the trains are soot-streaked diesel relics with a customs stop and a dozen soldiers at every petty border.",
    },
    {
        "name": "Village Munchmaussen",
        "location_type": "village",
        "city": "Munchmaussen, Bavaria",
        "district": "Munchmaussen Valley, eastern Bavaria",
        "security_level": "Low Security",
        "controlling_org": "Barony of Munchmaussen",
        "summary": "Picture-postcard Bavarian valley village of 40 buildings -- lederhosen beside cybertractors, no aerials or neon, hidden cameras everywhere -- under the schloss",
        "description": (
            "A remote, picturesque valley where peasants in the lederhosen and long skirts of two "
            "centuries ago work beside the latest cybertractors. No more than forty structures dominated "
            "by the medieval church (St. Gretchen's) and the Town Hall where bureaucrats keep records on "
            "every resident: elegant hotels of under twenty rooms with liveried housemen, a youth hostel "
            "bunking six to a room with automated laundry and kitchen, and a main street of craft shops "
            "with carved signs -- pipes, clocks, sausages, jewelry, clockwork toys, Bavarian costumes. "
            "Women water flower boxes, old men whittle and puff long pipes, the air smells of baking "
            "apples, and above it all the schloss sits on 'our very own Matterhorn', linked by a "
            "deceptively thin tram cable."
        ),
        "notes": (
            "Tourism is the lifeblood, so the baron's police (Detective stats) and bureaucrats investigate "
            "strangers with tact -- and with the concealed cameras of I/O-1 to I/O-6 (hotels, shops, "
            "streets and the youth hostel; see Matrix section). Goldi Schonbosom meets the train, quizzes "
            "the runners ('You are mountaineers, jawohl?'), and if she wins an Opposed Intelligence Test "
            "forces herself on them as a guide for the day. No rental vehicles. Mr. Johnson's crates "
            "(silenced Predators, HK227-S, missile launcher, grapple gun, snowsuits, climbing gear; p.42) "
            "wait at the hostel -- unpacking them under the cameras puts the baron on Vigilant."
        ),
    },
    {
        "name": "St. Gretchen's Church",
        "location_type": "church",
        "city": "Munchmaussen, Bavaria",
        "district": "Village Munchmaussen",
        "security_level": "Low Security",
        "controlling_org": "Munchmaussen Underground",
        "summary": "Ancient Gothic church, still functioning, and the secret center of the valley's feeble resistance under Father Braun",
        "description": "An ancient Gothic structure and a functioning church. Unknown to the baron and his minions, it is also the center of the feeble local resistance movement.",
        "notes": "Father Braun might help runners who need allies against the baron, or a place to rest and heal after the schloss.",
    },
    {
        "name": "Schloss Munchmaussen",
        "location_type": "castle",
        "city": "Munchmaussen, Bavaria",
        "district": "Mountaintop above Munchmaussen Valley",
        "security_level": "Corporate High Security",
        "controlling_org": "Barony of Munchmaussen",
        "summary": "The Troll baron's mountaintop castle: skylift, missile batteries, drone tower, 20 m walls, a keep with a fake tome in the library, Fire Elementals in the fireplace and an Airstar in Brown Hall",
        "description": (
            "Set atop the valley's largest alp, snow-covered cliffs on every side. Reached by a two-car "
            "skylift into a 15 m tram tower (controlled from the castle's archaic computer), a 7 km "
            "switchback mountain road impassable in winter (a two-day hike under drone patrols every one "
            "to six hours), or four faces of cliff (Athletics tests, p.43). Outer walls 7 m with "
            "floodlights and cameras every 20 m and hourly guard pairs; twin gatehouse towers with an "
            "iron portcullis; a 20 m main wall with an archway, a garden gate and a rusted-shut sortie "
            "gate; five- and eight-storey conical towers used for storage except the security checkpoint, "
            "the drone launch tower and the main barracks; a courtyard with three Volksedanz and a "
            "Mitsubishi Nightsky; four-storey wooden administration buildings including a remodeled "
            "church with twin bell towers; and the four-storey crenellated Keep. Keep (pp.48-49): "
            "reception hall and bureaucrats' offices, a security post of two Ork mercs, a six-person "
            "elevator; the dining hall with a 7 m obsidian table, Antler Hall smoking room, a miniaturized "
            "kitchen, cloakroom with silent alarm, empty guest rooms; the Great Hall with a five-year-old "
            "rock-concert stage over a Rating 4 Fire Elemental conjuring circle under a tarp, the "
            "library (globe, bookstand with the replica tome, a chandelier, a stone statuette, a fireplace "
            "big enough for two Fire Elementals), the baron's chambers with a hexagonal bed under the "
            "first baron's portrait (the real tome lies open on the coffee table), a well-stocked bar, "
            "and 'closet' 15a, the secret security chamber behind a one-way portrait; servants' room "
            "with clean uniforms, a Rococo chapel the guards may not damage, Brown Hall (maglocked, key on "
            "the baron's neck; roof folds back for his Hughes Airstar), the four-guard security center; "
            "the Blue Gallery museum of the Dark Ages, vaults, a misty warm pool, weight room, boxing "
            "gym, steam room and a fungarium of exotic molds."
        ),
        "notes": (
            "Security levels Lax / Vigilant / Full Alert (p.46). The baron believes the valise is a bomb "
            "and the runners are 'Yankee hitmen'; he lets them reach the library, steps in with 'So that's "
            "all you were looking for, nicht war? I am so disappointed', and springs Goldi's two Force 4 "
            "Fire Elementals (Engulf; Project Flame only away from the books; no Flame Aura -- no "
            "sprinklers) and the keep guards. Intelligence (4) to notice lizard feet in the flames. If he "
            "cannot keep the book he escapes to hunt the runners later. Real tome: Pandemonicus Faustus / "
            "Collectanea Occultica, 15 cm thick, 30 cm wooden covers, Asmodeus frontispiece in wet-looking "
            "blood-red ink, delicate. Escape in the Airstar. System map in the Matrix section (SAN-2 and "
            "SAN-3 unlisted; SM-3 skylift; Trapped IC on the baron's SPU). Karma: survive 1, real tome 1, "
            "false tome -2, valise left 1."
        ),
    },
    {
        "name": "Fire Station 118 (YET Hall)",
        "location_type": "policlub headquarters",
        "district": "Puyallup Barrens",
        "security_level": "Low Security",
        "controlling_org": "Young Elven Technologists",
        "summary": "Pre-Awakening brick fire station turned Young Elven Technologists' hall: dream-park solarium under a 15 m skylight, Ehran's warded suite, a basement computer room of 40 workstations",
        "description": (
            "A large two-storey brick building (Barrier 6) with boarded ground-floor windows, bricked-up "
            "upper windows and 'Fire Station 118' etched into a cornerstone, on the squalid outskirts of "
            "Puyallup where even the family dog has its place on the menu. The grounds are kept clear of "
            "debris in stark contrast to the neighborhood; caged corner lights (5 m radius) and four "
            "vandalized, dead cameras. Roof: helipad over the air-conditioning plant, a bolted stair "
            "shack, an armor-glass skylight. Ground floor: lounge with simsense center, dining area, "
            "kitchen (back door Maglock 5), and the solarium -- trees, shrubs and grass under a "
            "hydroponic-lit skylight 15 m up, two wood-and-rope catwalks at 6 m, benches for formal "
            "meetings, a stair to the second floor and basement. Second floor: the commons open to the "
            "skylight, one-room flats for members between apartments (Maglock 5), and Ehran's Private "
            "Suite -- maglocked, PANICBUTTON on SM-2, a Force 10 Ward worked into the decor, spartan but "
            "for a den with a writing desk, telephone, two terminals and a datastore, shelves of his own "
            "books under his name and pseudonyms. Basement: Main Security behind armor glass, the armory "
            "(Barrier 24), a security lounge, the three section heads' offices, a conference room, and "
            "the computer room with 40 cubicles and the CPU in a soundproof glass box."
        ),
        "notes": (
            "Maps pp.55-61. Party night: 20+ in the lounge, 3D6+6 barefoot dancers, a Willpower test on "
            "leaving the solarium (Chaos-like disorientation), doorman with a Detek-It wand, three Troll "
            "samurai upstairs, 40-odd party-goers who stampede at gunfire. Run night: six guards early, "
            "three after 11 p.m., 2D6 Elven deckers in the basement (they shut the system down in 2D6 "
            "turns if they spot an intrusion), Ehran's advance bodyguards (Bodyguard + Combat Mage) in "
            "flats beside the suite after 11. Catwalk rope-cutting and falling-skylight rules p.59-60. "
            "At the moment the decker hits Dassurn, ten APN gunmen blow a 4 x 3 m hole where the front "
            "door was; both Elven groups then recognize the runners and call a truce to hunt them; APN on "
            "Honda Vikings, YET in one Ford Americar. Envelope for the suite: wax seal impressed with a "
            "laughing jester's head, the tome's frontispiece inside."
        ),
    },
    {
        "name": "Grantleigh Park",
        "location_type": "park",
        "district": "Auburn District (NatVat condo complex parkland)",
        "security_level": "Corporate Standard",
        "controlling_org": "Natural Vat Foods",
        "summary": "Hedge-bordered plaza with a center bridge and bandstand in wooded Auburn parkland where Shirley Marquis walks at sunset -- Ariel's NatVat ambush",
        "description": (
            "Quiet evening in salary-land: heavily wooded parkland around NatVat's medium-security condo "
            "complex, a hedge-bordered path to a quiet plaza with a center bridge, a bandstand, chess "
            "tables, street lights coming on as the sun fades. Perfect for a quiet extraction."
        ),
        "notes": (
            "Map p.74. Two chess players and a necking couple are plainclothes NatVat police (armor "
            "clothing, Browning Max-Powers); Squad A in the woods northeast (one turn away), Squad B in "
            "the clearing (two turns, cutting the path to the street); three Patrol-1s in garages along "
            "the street; a Yellowjacket five turns out that wipes out the runners' vehicles. Most fire "
            "should miss -- until Ariel's lean armored van hops the curb, Chuckles AVMs a Patrol-1, and a "
            "woman's voice sings out 'So, are you guys going my way?'. Turning the job down means Ariel "
            "backs off and waits for the next losing fight."
        ),
    },
    {
        "name": "CIA Safe House (Sea Cliff Bungalow)",
        "location_type": "safehouse",
        "district": "Seattle-area coast, a cliff over the sea screened by woodland",
        "security_level": "Corporate High Security",
        "controlling_org": "Central Intelligence Agency (UCAS)",
        "summary": "Mothballed UCAS covert-ops bungalow over an underground complex -- cells, clinic, interrogation room, vault, armory, escape tunnel and a sea cave with a moored Otter -- squatted by Ariel's crew",
        "description": (
            "A small bungalow on a cliff overlooking the sea, screened from the road by woods, built over "
            "an underground installation with a tunnel to a sea-level cave for clandestine boat arrivals "
            "or the secret disposal of certain items. Bungalow (p.78-79): plastiwood deck, a den wired to "
            "the newsnets, a dining-room intercom to the complex, a hidden elevator (Perception 15), a "
            "two-car garage, an unused kitchen, a trid that taps the security-booth screens, a secret "
            "staircase in the parlor closet; upstairs an empty attic, Ariel's unused bedroom (coded "
            "wristphone, 60,000 UCAS-dollar credstick, the holo-paintings) and two empty bedrooms. "
            "Underground (p.79-81): a 20 m elevator shaft with ladder, a 35 m stair, an armor-glass "
            "security booth with an FN HAR and Uzi III and a console (air seal, alarms, armory and cell "
            "locks, elevator power, foam extinguishers, IR and lights per room, three vidscreens), common "
            "room, kitchen, mercenary quarters with loot to find, Bonecrack and Iggy's room, the magic lab "
            "where Lancelot sleeps (four units of Fire Elemental ritual materials), three barred cells "
            "with cameras, storage with a government microtronics kit, a monitor room behind a one-way "
            "mirror, a scrubbed interrogation room, a small office and an emptied vault, a power "
            "substation, a utility room that can seal the air system, the Infirmary (two Rating 3 medkits, "
            "a deluxe stabilization unit, drug lockers to rating 5), Doctor What's sickroom, a two-bed "
            "sickbay, the alarmed armory (Maglock 6; 6 Uzi III, 3 FN HAR, a Ranger Arms SM-3, 3 Predator "
            "II, 12 defensive grenades, three armor jumpsuits), a storage area holding the runners' gear, "
            "a secret room (Perception 15) to the escape tunnel into the woods, and the cave with a "
            "Samuvani Criscraft Otter moored to a small pier (mouth submerged at high tide)."
        ),
        "notes": (
            "Prisoners are stripped, in Taser restraints, magicians dosed with a 'prison drug' (+10 to all "
            "mental and magical tests, astral projection a 5-10 minute Willpower (10) effort; blue injector "
            "= antidote, green = drug). Hourly: Bonecrack and two mercs (shotguns with Stun rounds) "
            "wheelchair one runner (self-locking restraints, TN 20 minus attribute to slip each) to Doctor "
            "What; Lancelot assenses; ten boxes of Mental damage, then six hours, then interrogation about "
            "every Harlequin run at 6D3 Stun per Interrogation test until ten successes. Escape hooks: "
            "the torture gear makes the lights flicker (Perception 12, cumulative successes) -- short the "
            "sink light or camera (6S2 Stun) while a Strength 6 body hits the door; Iggy's toy police car "
            "hides a monofilament utility saw. Sealing the complex's air (booth or utility room) disrupts "
            "Ariel for a month. Forcing the armory (Disarm 8) rings the CIA. The captors leave and open "
            "the cell by timer once the Doctor is done."
        ),
    },
    {
        "name": "UCAS Federal Building",
        "location_type": "government building",
        "district": "Downtown",
        "security_level": "Corporate High Security",
        "controlling_org": "Central Intelligence Agency (UCAS)",
        "summary": "Federal offices downtown; the CIA's Seattle offices and the alarm line from its abandoned safe house's armory",
        "description": "The UCAS federal building in downtown Seattle, home to the CIA's local offices among others. The armory alarm of the agency's mothballed sea-cliff safe house terminates here; twenty minutes later the place is lousy with agents.",
        "notes": "Mentioned only as the alarm's destination (p.81). Agents: Former Company Man in partial armor with Uzi IIIs.",
    },
    {
        "name": "Fonte Boa",
        "location_type": "river town",
        "city": "Fonte Boa, Amazonia",
        "district": "Mouth of the Jurua, upper Amazon",
        "security_level": "Low Security",
        "controlling_org": "Amazonia",
        "summary": "River town of 70,000 slowly losing its battle with the regrown jungle; Captain Colon's last stop and Graeme Greene's home",
        "description": (
            "A town of roughly 70,000 at the mouth of the Jurua, ten days upriver from Macapa, where the "
            "Awakened government's regrowth rituals mean flame damage and heavy cutting wherever the "
            "jungle presses in, and the inhabitants cut their vehicles free of the flora every morning. A "
            "dock, a boarding house, a good meal on Helm's tab, and a lonely old Englishman's amphibious "
            "plane hidden an hour away because its gas engine is illegal."
        ),
        "notes": "The Marsh Rose flies 650 km up the Jutai in five hours on half its fuel; from the sandbar it is 144-160 km of raft (32 km a day) and 16 km on foot to the plantation. Greene's pointed questions are loneliness, not treachery.",
    },
    {
        "name": "Fonte do Sul",
        "location_type": "plantation",
        "city": "Upper Jutai, Amazonia",
        "district": "Rain forest near the source of the Amazon, Jivaro country",
        "security_level": "Corporate Standard",
        "summary": "Ehran's secret retreat: the Aquilar family orchid plantation -- electrified fence, airstrip, mansion, greenhouse with a barghest, and a militarized Stallion with six mercs",
        "description": (
            "A clearing about a hundred meters square in a five-meter electrified chain-link fence, a "
            "million kilometers from nowhere. A grass airstrip kept lit all night to hold back the dark; "
            "a hangar with a radar dish and a shortwave to Eirunepe where a Cessna C750 makes the weekly "
            "mail run; a three-storey, two-wing mansion housing scores of staff, its whole third floor "
            "kept for the monthly visits of 'Senor Aquilar', last of the renowned Portuguese "
            "horticultural family -- Ehran under a Mask spell -- and an upper-floor study with the "
            "original portrait of him; a large greenhouse on the west wing for the Fonte do Sul orchid, "
            "with a gardener half the daylight hours and a barghest asleep in the foliage (Perception 8); "
            "a four-room work shed (electrical, mechanical, carpentry, optical-electronic); a barn of two "
            "horses, two cows and 15 hens; a pasture; a year-round vegetable field. No locks on any door. "
            "Behind the hangar: a fully militarized Hughes WK-2 Stallion (two heavy MGs, two AK-97s, "
            "autopilot) with six mercs (AK-98) and a rigger (Rotorcraft 6), sent because of the attacks "
            "on Ehran's holdings."
        ),
        "notes": (
            "Map p.103. Fence: Athletics (2) with insulated gloves or 5L2 Stun and disorientation; "
            "Electronics (4) to cut the charge, one turn per success before someone investigates. "
            "Eastern infiltration is easiest day or night. Leave Helm's 10 Mp datachip (one line of YET "
            "back-door code) in place of the cut bloom. Steal the Stallion, not the Cessna -- the mercs "
            "chase in the Cessna until fired on. The Jivaro shaman's Force 3 Storm Spirit then blacks "
            "out the sky, kills the instruments and autopilot (Electrical Projection, Confusion) and "
            "projects Fear; chopper Resistance 7. Then Lima, Peru, and Helm's tickets home. The Amahuacas "
            "call the place the home of a great demon-spirit. Karma: survive 1, goals 3, no casualties 1."
        ),
    },
    {
        "name": "The Tacoma Style",
        "location_type": "restaurant",
        "city": "Tacoma",
        "district": "Tacoma",
        "security_level": "Patrolled / Commercial",
        "summary": "One of Tacoma's trendiest restaurants: strict dress code, a grinning Troll doorwoman, an Elven hitman for a maitre d', armored-tuxedo waiters",
        "description": (
            "A fashionable, somewhat conservative corporate restaurant and bar with a reinforced door, a "
            "clean white hallway to the maitre d' stand and an elegant dining room with window tables. No "
            "weapons beyond light handguns; a strict dress code -- Betty the bouncer turns away the dirty, "
            "the too-casual and the too-outrageous. Anyone who has worked Tacoma knows this."
        ),
        "notes": (
            "Mr. Johnson's 8 p.m. meet for Future: he orders for the table, outlines the run without "
            "pausing for a peep, leaves 10,000-nuyen advance credsticks with the travel voucher, and goes. "
            "Attack him or Betty and the twelve waiters (Bartender stats, armored tuxedos) rush you while "
            "the maitre d' (Elven Hitman, silenced Beretta 101T Smartgun) hits the PANICBUTTON for half a "
            "dozen Lone Star officers."
        ),
    },
    {
        "name": "Columbia, Missouri (UCAS)",
        "location_type": "city",
        "city": "Columbia, Missouri",
        "district": "Central Missouri, I-70 between Kansas City and St. Louis",
        "security_level": "Low Security",
        "summary": "College town of 80,000 (University of Missouri, Columbia College, Stephans College), Columbia Regional Airport, Highway 63 to Jefferson City; four gangs, a secure computer grid",
        "description": (
            "UCAS Board of Tourism, 'Traveling: The Real Store', August 2050: first and foremost a college "
            "town that grew up around the University of Missouri, the first land-grant university west of "
            "the Mississippi (nearly 30,000 students; matrix geometry and applied sorcery among its "
            "fields). Equidistant on I-70 from Kansas City and St. Louis (200 km each); Highway 63 runs "
            "48 km south to Jefferson City. 80,000 residents, 86 percent of adults with college credit, "
            "cheap skilled labor, prices a little high, more night spots per capita than almost any UCAS "
            "city. Columbia Regional Airport handles 50-75 commuter and dirigible flights a day with "
            "metal detectors and passive sniffers most travelers never notice. Unsalaried mayor and "
            "nine-ward council; the real power is the hired city planner. Power from the Calloway County "
            "Nuclear Power Corporation in Fulton; electric cars and recharging stations; the unreliable "
            "CATS transit for five nuyen. Mizzou Tigers combat football at Farrow Field; the Black and "
            "Gold Bengals UrbanBrawl team at Hearnes Center; Columbia College and Stephans College; a "
            "School of Journalism that keeps the populace well informed. Ancient brick downtown, "
            "buildings no taller than eight or nine storeys, Broadway the main east-west street."
        ),
        "notes": (
            "Legwork TNs are 2 higher (6) for out-of-town runners. Crime is isolated: the Pretenders "
            "go-gang, Guys in Sunglasses, the Flames and the new Spirits. The computer grid is especially "
            "secure because three colleges turn out would-be deckers. Rental cars cost 1 percent of "
            "purchase price per day, fully insured, warrant for grand theft if not returned. Fights here "
            "are hands and blades; nobody calls the police unless a gun is drawn. Ehran's guns bunk at a "
            "small Nights Inn on the edge of town with a datachip dossier on Jane Foster that links to "
            "Sylvan's deleted genealogy block (Biology (Genetics) 12 / Perception 15)."
        ),
    },
    {
        "name": "Jane Foster's Apartment",
        "location_type": "apartment",
        "city": "Columbia, Missouri",
        "district": "Ninth Street, half a block from Broadway, downtown Columbia",
        "security_level": "Low Security",
        "summary": "Third-floor flat over an accountant over a dress shop; Navaho pottery, fine paintings, a slagged maglock and blood on the carpet",
        "description": (
            "'Foster' on a heavy street door on Ninth Street; a dark, steep single flight up to a landing "
            "with two thumbprint-scanner doors (a reinforced storage closet with an industrial maglock, "
            "and the flat, its lock crudely bypassed and fused to slag like an amateur's calling card). "
            "Inside, a beautiful, tastefully furnished apartment: expensive Navaho pottery, fine paintings "
            "and etchings, one shattered pot and a good deal of blood by the door, a soy-stocked kitchen "
            "with a few real-food luxuries, an unmade bed and a corporate suit on the valet."
        ),
        "notes": (
            "Perception (4) per room (p.111-112): a CommTech payroll stub with the corp's address; the pot "
            "was a weapon and the wound painful but not fatal; a small hand smeared through an unfinished "
            "oil painting -- Jane faced two attackers; her nightgown and an open drawer of sweaters and "
            "jeans; a nearly full lighter etched 'B. K. Lounge'; and on the steamed bathroom mirror 'HELP "
            "GET PRETENDERS'. Ehran's team no longer watches it. Ritual sorcery on her effects fails; "
            "Magical Theory (8) reveals something powerful conceals her. The flower must be left here."
        ),
    },
    {
        "name": "CommTech Facility",
        "location_type": "corporate headquarters",
        "city": "Columbia, Missouri",
        "district": "Western outskirts of Columbia on I-70",
        "security_level": "Corporate Standard",
        "controlling_org": "CommTech Inc.",
        "summary": "Unfenced software house on six wooded acres; a bare atrium, a smiling receptionist and Josh Rehndig bounding down the stairs in a string tie",
        "description": "A circular drive and visitor parking in front of the main doors of a facility set well back from the road on half a dozen wooded acres with no fence -- this part of the country is safer than Seattle. A spacious, bare atrium with a concrete-and-steel stair beside the elevator and a massive wraparound reception counter dwarfing one smiling blonde; a small conference room down the right-hand hall.",
        "notes": "Opposed Charisma vs Rehndig's Intelligence: two questions per success (Jane's address, that she likes music and a club in town, that she hangs with a tough bar or biker gang). One mark of unwanted attention per visit.",
    },
    {
        "name": "B.K.'s Lounge and Danceateria",
        "location_type": "nightclub",
        "city": "Columbia, Missouri",
        "district": "Corner of Stadium and Broadway, Columbia",
        "security_level": "Low Security",
        "summary": "The hottest spot in Columbia -- glittering sign, twin spotlights, a busy helipad, Early American tacky, one drink (kamikazes), the 'blues position' dance, and the Pretenders by the back bar",
        "description": (
            "Commands the city's best location; a sign visible from a kilometer away, twin halogen "
            "spotlights, a small helipad in near-constant use, a packed front before midnight. Two Human "
            "bouncers take a 20-nuyen cover. Inside, a strange mix of cheap dive and high-class tavern: "
            "rough wooden floors, cheap tables under plexiglass-framed art, black-and-white airbrush "
            "canvases of last century's trideo stars, one bartender serving nothing but five-nuyen "
            "kamikazes to a score of waiting clients, a massive speaker-lined dance floor with sound as "
            "good as any in Seattle, three dozen mirror-shaded punks lying motionless in the 'blues "
            "position' under a wall of screaming sound. Sooner or later everybody who is anybody shows "
            "up; it does not start happening until around twelve."
        ),
        "notes": (
            "Doormen roll Perception vs Concealability and merely ask that spotted weapons be checked "
            "(token). Rough stuff is tolerated; bouncers (Bartender stats, armor clothing, out of their "
            "league) arrive five turns into a fight and go for whoever is nearer -- the runners on a tie. "
            "The Pretenders make their weekly appearance at the back bar and attack on sight anyone "
            "asking for Frosty ('Didn't find what you were looking for when you busted into her place?'). "
            "A bar fight is one mark; learning about St. James is another."
        ),
    },
    {
        "name": "St. James Home for Wayward Women",
        "location_type": "halfway house",
        "city": "Columbia, Missouri",
        "district": "Ash Street, edge of downtown Columbia",
        "security_level": "Low Security",
        "controlling_org": "The Flames",
        "summary": "Church-founded halfway house for women out of the state prison, freshly painted and old, run for the last couple of months by 'Sister Ann' -- the Flames' front; Frosty's hiding place",
        "description": (
            "An old wooden home that has seen a lot of winters under a fresh coat of paint. Started by the "
            "local church a year and a half ago to help women returning to society after prison; the "
            "residents, 'a little rough around the edges', browse the downtown shops. A small face under "
            "the window shade, a bolt thrown back, and an older woman in sweat pants, a Columbia College "
            "tee-shirt and faded running shoes: 'Good day. I am Sister Ann.' Then, 'Beat it, Janey, "
            "they're here!'"
        ),
        "notes": (
            "Nine Flames inside going about their business (some asleep at night, some out); a Browning "
            "High-Power hidden in the kitchen. Ann stays out of it unless the team enters, then everyone "
            "fights while others fetch weapons; neutralize Ann and they surrender Jane and themselves for "
            "her release. Jane bolts barefoot off the back porch trailed by two Pretenders; if she gets "
            "away she is found again within an hour or two. Her clothes and possessions are in her room "
            "upstairs. Street: 'if that place is on the level, I'm the pope.'"
        ),
    },
    {
        "name": "Columbia Regional Airport",
        "location_type": "transportation hub",
        "city": "Columbia, Missouri",
        "district": "South of Columbia on Highway 63",
        "security_level": "Low Security",
        "summary": "Small regional airport (50-75 commuter and dirigible flights a day), a nearly deserted terminal with three dozing rental counters and a private-flight entrance where the Lear waits",
        "description": "A lighted tarmac, a maintenance crew and a service truck, no baggage check for the Cessna C750 commuter from Kansas City; a nearly deserted terminal with three rental-car companies along the far wall (cars and bikes in the basic shapes, nothing that announces you with authority) and a small side parking lot. A separate private-flight entrance to the left of the main terminal. Highway 63 runs north to Columbia and south to Jefferson City. Security is metal detectors and passive alarms keyed to certain substances.",
        "notes": "Arrival at dawn. Departure: one call to the unnamed SIN and the Lear Platinum is ready within 30 minutes; a young woman with a portable computer collects the rental keys and the credstick at the foot of the steps.",
    },
    {
        "name": "Southwind Complex",
        "location_type": "ruins",
        "district": "Tarislar, southern Puyallup Barrens",
        "security_level": "No Security / Barrens",
        "summary": "Three ruined 40-storey insurance towers of black metal and shattered glass in the ash of Tarislar; Harlequin's residence on the top floor of the center building",
        "description": (
            "Three 40-odd-storey towers, battered and broken spires of black metal and shattered glass, "
            "once offices owned and licensed by a group of diversified insurance agencies, abandoned "
            "after the eruptions and a haven for gangs and dealers for years -- until a year ago, when "
            "Harlequin took the upper floor of the center building and the criminals left, afraid of the "
            "Laughing Man they could not bribe or threaten. The locals steer clear. Elevators long dead; "
            "forty floors of dark stairs (4L2 Stun fatigue at the 20- and 40-storey marks); at thirty "
            "storeys 'One must know chaos within to give birth to a dancing star' on the wall over a dark "
            "smear; at the top a floor half open to the sky, furniture and partitions tumbled into the "
            "street, and in the sunken-and-raised presidential office at the far edge, a man with a "
            "gray-streaked ponytail playing a hundred-year-old steel guitar. 'Welcome to Mount Olympus.'"
        ),
        "notes": (
            "Air so thick with ash that a filter mask (20 nuyen, two weeks) is nearly a necessity: 3M2 "
            "Stun every ten minutes without one. A blind Elf in dust-covered white robes waits in the "
            "forecourt for hours: 'He awaits you behind me, at the top. Join him with the woman.' Astral: "
            "Harlequin masks as mundane; no spirits present; background count high; a dormant hermetic "
            "circle (Astral Perception 10) around him and Jane; a faint power aura in her thigh (18). "
            "'The RITUAL, to the best of my recollection, by -H-' is written on a wall section in black "
            "marker (p.128). The ritual, the rebound, the shattered thigh, the eight-minute-later crack of "
            "Mount Saint Helens and Harlequin's exit on a powerful Air Elemental are staged theatre to send "
            "the runners to Althain."
        ),
    },
    {
        "name": "Mount Saint Helens",
        "location_type": "landmark / monument",
        "city": "Salish-Shidhe Council lands",
        "district": "150 km south of Seattle",
        "security_level": "Low Security",
        "controlling_org": "Salish-Shidhe Council",
        "summary": "Volcano of the 1970s, 2017 and now a third, eerily plume-less eruption; S-S Council troopers, gawkers, newsnet choppers, tourist caverns and the fissures to Althain on the north slope",
        "description": (
            "Site of three major eruptions in three-quarters of a century -- the 1970s, the 2010s and a "
            "few hours ago. This time no continuing ash plume or lava: the mountain blew its top and went "
            "quiet, leaving fresh dirt, ash and rock on the near-barren slopes, steam where flaming "
            "pieces fell, battered stands of new-growth trees, and a changed profile near the peak. S-S "
            "Council troopers and a moved-in unit of guardsmen cannot cordon the whole area; gawkers hang "
            "back a few kilometers; survey and patrol helicopters pass; soldiers and early scientists "
            "search for injured hikers. The fissures and caverns of the 2017 lava gases on the north "
            "slope are a tour stop with Parks Department lighting (now dead); beyond them, lava passages "
            "re-filled by the venting, a one-meter stone bridge over a river of molten rock hundreds of "
            "meters below, and a cleanly carved tunnel that was never natural."
        ),
        "notes": (
            "Getting there (p.130): the S-S Council's daily bus tours (50 nuyen, three hours, small bags "
            "searched at the border, a one-day visa from the S-S Council Lodge on Council Island, four "
            "hours on site), bluffing past the border with the rush of newsnet choppers, or running the "
            "border (blockhouse of four Former Tribal Warriors, two with Colt M22a2s; pursuit by two "
            "PRC-42b Wasps or Hughes Stallions, Car skill vs signature). Six-hour hike to the fissures. "
            "The bridge is guarded by an Embracer (B12 Q5x3 S10 I2/4 W4 E6 R6, 9S2 +1 Reach, dual-natured; "
            "+2 to shoot it while it hugs someone) that fights to the death. The eruption was Ehran's "
            "magically controlled geothermal system venting when his spell rebounded; the illusion and "
            "confusion spells on the tourist caverns are down, the ones hiding the sanctum are not. "
            "Afterward Althain cannot be found again."
        ),
    },
    {
        "name": "Althain",
        "location_type": "magical sanctum",
        "city": "Mount Saint Helens, Salish-Shidhe Council lands",
        "district": "Inside the north slope of Mount Saint Helens",
        "security_level": "Zero Zone -- Lethal Response",
        "summary": "Ehran the Scribe's hidden marble sanctum under the volcano: munchkin stewards, an illusory sky, a warded suite, a Great Hall of unknown symbols, an alchemical workroom with a vivisected wyvern and a chained young dragon",
        "description": (
            "Beyond a warded tunnel of jewel-like dark stone (map p.151): an entryway of gold-veined white "
            "marble with silver-veined black pillars, bronze-and-black doors without locks, and four "
            "munchkin stewards in justaucorps coats, embroidered doublets, lace shirts, breeches and "
            "cavalier boots offering champagne and strawberries -- Emerald, Ash, Turquoise and Maroon "
            "('Welcome to Althain. My master awaits within.'). A foyer with a one-piece spiral staircase, "
            "late-eighteenth-century European art beside works completely alien in form, and a skylight "
            "of blue sky and clouds that is an illusion. A gray marble hallway of masterpieces known and "
            "unknown. Waiting Room 5 in modern black macroplast, chrome and hammered steel with a full AV "
            "chip library, liquor and snack bars, no phone. Waiting Room 6 in an architecture older than "
            "Christianity, marble and quartz pillars, chilled reflecting pools of strange fresh-water "
            "fish. A Main Hall whose far wall is one tapestry of a city of crystal and gold built into a "
            "cliff. A scaled-down munchkin living area, two splendid guest rooms, a kitchen with a closet "
            "of molybdenum for the munchkins. The Great Hall: richer gold veins, alcove sculptures in "
            "black and gray marble including a life-size Harlequin in a many-layered robe-cloak, a "
            "three-storey vaulted ceiling painted with an unreadable astrological chart under six gold "
            "and crystal chandeliers, a floor inlaid with arcs of dark stone and a black-and-silver "
            "octagon of ancient and unknown symbols, an overturned brazier, a balcony, a secret door "
            "(Perception 10; both sides of an alcove touched at once). Ehran's suite beyond an invisible "
            "physical and mana barrier: 1600s antiques, an unknown woman's portrait, a fire-lit sitting "
            "room under a portrait of a late-16th-century Spanish nobleman who is Ehran. Below, the "
            "Workroom: a modern alchemical laboratory with molecular analyzers and scanning microscopes "
            "where a wyvern has been magically vivisected and a young Western Dragon lies restrained by "
            "a fading red-orange barrier. Above, via the spiral stair, an arboretum of familiar and "
            "unfamiliar plants with a dining nook. Every wall is unbreakable natural marble; magical "
            "sconces light everything; nothing transmits out."
        ),
        "notes": (
            "Background count: astral perception or projection outside the 'clean' rooms costs 6M4 Stun "
            "per turn and +6 to Perception; elementals at +4 and half Force; scrying fails. The Great Hall "
            "is unusually clean; the Workroom is count 2. Ehran's research (Magical Theory + Intelligence "
            "vs TN 20, no Karma) works from effect back to cause and predicts effects that are physically "
            "and magically impossible. The 'body of Ehran' by the brazier -- white tunic, breeches, boots, "
            "no aura, no residue -- is an expendable YET member ('Windtree, perhaps?'). The dragon (B13/5 "
            "Q8x3 S32 C4 I3 W7 E(10) R6, 9D3 +2 Reach, Thermal Sense, Flame Projection) breaks free at "
            "the worst moment and goes up through the Main Hall floor. Face To Face (p.137-140): "
            "Harlequin walks in and screams; Maroon announces 'men from the Land of Promise'; Ehran "
            "appears alive in centuries-old dueling clothes with two swept-hilt rapiers, Harlequin tears "
            "off his prosthetic left ear, runners stand as seconds, a golden sphere of magical contest "
            "surrounds the duel, and on the balcony Harlequin takes Ehran's left ear -- 'We are now merely "
            "even!' -- before both vanish prismatically. Ariel warns off interference and later warns "
            "everyone out before Ehran reactivates security; she forbids looting the heirlooms."
        ),
    },
]

NPCS = [
    # -- the two principals ------------------------------------------------------------------
    {
        "name": "Harlequin",
        "role": "Immortal elven mage in harlequin face paint waging chal'han against Ehran the Scribe; the runners' unseen employer, 'the Laughing One'",
        "archetype": "Immortal Elf (hermetic Initiate)",
        "title": "Challenger in the Great Game; 'the Laughing Man' of Tarislar",
        "race": "Elf",
        "gender": "Male",
        "connection": 6,
        "description": (
            "Chaos personified. Half a head shorter than Ehran and lighter built, a face painted in the "
            "harlequin-clown markings of old, gray-streaked black hair in a ponytail, a long many-pocketed "
            "coat with pins on the left lapel, always slightly behind the times. Attitude, manner, "
            "philosophy, dress and accent change at a moment's notice; quick-witted with references only "
            "three people alive would get, quick to anger and usually quick to forgive -- but when the "
            "anger lasts, as it has for Ehran, it becomes a consuming passion. Plays a steel guitar at "
            "least a century old. Displays his magic openly, even blatantly, yet masks his aura as a "
            "mundane. 'Gentlemen! Welcome to Mount Olympus. I've been expecting you.'"
        ),
        "background": (
            "Ehran's 'old friend', 'once-brother' and fellow pupil of the same teacher, who lost his left "
            "ear to Ehran's rapier in a dawn duel on a stone bridge, in a city with a King's guard, "
            "centuries ago ('Now it will never be over'). He speaks with Ehran in a tongue nobody, not "
            "even the Tir Elves, has ever heard. A year before the adventure he took the top floor of the "
            "ruined Southwind towers in Tarislar and the gangs fled the Laughing Man they could not bribe "
            "or threaten. He knows the Amahuacas of the Jutai, who tell stories of his earlier visits. "
            "He has visited Althain once before, and a life-size statue of a man with his face and "
            "paint stands in Ehran's Great Hall. A holocard from Phoenix, Pueblo Council, a month after "
            "it ends: 'My God, it's hot. Wish you were here. -H.'"
        ),
        "notes": (
            "No game statistics by design: a full hermetic Initiate of incredible rank who can neutralize "
            "any unruly runner with magic; let the players roll and come oh-so-close. Invoked chal'han "
            "che (honor only; if Ehran dies Harlequin loses); hires only through cut-outs (Morlock, "
            "Charlie Tarrow's old network, the French Ms. Johnson, Sandii and 'Lee Gorbin' -- perhaps "
            "himself in gold teeth -- Anson Helm, the brusque Tacoma Johnson) and knows their results "
            "'through mysterious channels'. Wax-seals envelopes with a laughing jester's head. Journal: 'I "
            "have sent them against him once more... And he has learned to love flowers since last we "
            "met.' At Southwind he activates the spell lock in Jane's thigh (he understands Ehran's link "
            "because they had the same teacher), reflects Ehran's booby-trap back, heals Jane, and "
            "threatens the runners into going to Althain. There he tears off his own false left ear, "
            "duels Ehran to the balcony and takes Ehran's left ear, throws the runners a 16th-century "
            "heirloom rapier (base value 100,000 nuyen) as their final pay, and vanishes. Fixers and "
            "Johnsons from the adventure cannot reach him afterward."
        ),
    },
    {
        "name": "Ehran the Scribe",
        "role": "Pulitzer-winning Elven social theorist, YET's patron, Tir Tairngire power broker -- and an immortal Initiate with a secret daughter and a sanctum under Mount Saint Helens",
        "archetype": "Immortal Elf (hermetic Initiate)",
        "title": "Author and social theorist; chairman of the Young Elven Technologists; 'Senor Aquilar'",
        "race": "Elf",
        "gender": "Male",
        "organization": "Young Elven Technologists",
        "connection": 6,
        "description": (
            "Appears in his thirties, slightly older than most Elves ('an exuberant youth'); just over two "
            "meters, a strong square face and piercing green eyes that reveal his emotions when he "
            "speaks; always impeccably dressed in tailored suits from the finest shops in Spain and "
            "Tokyo. Studied and solemn, rarely joking except with adrenaline pumping; charismatic and "
            "eloquent enough to hold any crowd on any subject. 'Rules are everything to him' -- a true "
            "parliamentarian. His aura reads mundane; people have seen him do magic. Ten layers of "
            "thought behind the eyes; when really angry, frightening."
        ),
        "background": (
            "Who's Who in UCAS 2050: rose to national prominence in fifteen years from newsfax opinion "
            "columns to The New Magic, Life After 2001, Mankind Ascendant (Pulitzer), Metagenes: Future "
            "Spiral, and essays such as Debunking the Neo-anarchist Myth: Why Humanity Needs Leadership. "
            "Claims a youth in the Chicago Shattergraves, no formal education; residences in Seattle, "
            "Portland and New York; tied into Tir Tairngire politics. The truth: an immortal who dueled "
            "Harlequin on a Paris bridge as 'Monsieur E.', sits for portraits as a 17th-century French "
            "courtier and a late-16th-century Spanish noble, keeps the orchid plantation Fonte do Sul in "
            "Amazonia as 'Senor Aquilar' under a Mask spell and is worshipped by the Jivaros as a warrior "
            "god's avatar, holds the Free Air Elemental Ariel by her true name, and grew a tracking-and-"
            "concealment spell lock into the thigh bone of the daughter he 'allowed to lose him' after "
            "her mother's death -- Jane Foster of Columbia, Missouri, watched through Sylvan's genealogy "
            "file 8-007. Althain, his sanctum under Mount Saint Helens, reminds him of the place he lived "
            "as a child."
        ),
        "notes": (
            "No stats by design; a full hermetic Initiate of incredible rank with a Bullet Barrier and a "
            "spirit for every contingency. Bound by chal'han to act through intermediaries (Ariel, "
            "Lancelot, Bonecrack's crew, Banger's team) and forbidden to harm the pawns; afterward he "
            "orders the YET to take no retaliation. Owns SIN account LTG 5206 (19-1165) at a Tacoma bank "
            "(the Dassurn siphon's destination) and Tir commcode 3503 (395-6985), erased 24 hours after "
            "the end. Booby-trapped his daughter's spell lock to fry whoever activated it, then faked his "
            "death with an expendable YET body and reappeared in centuries-old dueling clothes with two "
            "swept-hilt rapiers of great value: 'Temeravilhas, Har'lea'quinn?' Loses his left ear on the "
            "Althain balcony -- 'You have not won! We are now merely even!' Mankind Revealed is delayed "
            "six months ('ill'); he returns fit, and sporting two ears. Relations afterward: neutral but "
            "reserved."
        ),
    },
    # -- Physical ---------------------------------------------------------------------------
    {
        "name": "J.P. Morlock",
        "role": "Death-white hump-backed Dwarf fixer in purple satin who brokers the Sylvan manuscript job from a Laubenstein Plaza penthouse",
        "archetype": "Fixer",
        "title": "Fixer for discreet Mr. Johnsons",
        "race": "Dwarf",
        "gender": "Male",
        "connection": 4,
        "description": (
            "A cross between a hump-backed Dwarf and a dour: skin best described as death white, purple "
            "satin trimmed with white and black lace, a suite reeking of jasmine and stale sweat, wine, "
            "real pate and a twisted cheroot. Play him as an offensively rich Mick Jagger. Known for "
            "handling contracts for Johnsons who want services rendered in the most discreet manner; "
            "respects professionals who talk their way past his Orks and shows only disdain for those "
            "who shoot. 'Gentlemen. I am J.P. Morlock. Please come in.'"
        ),
        "notes": (
            "Fronts for parties who 'cannot afford to be implicated' (Harlequin). Pays 5,000 + 5,000 each "
            "plus 2,000 for leaving other Sylvan data alone (3,000 + 3,000 + 1,000 if the team fought the "
            "Orks); Opposed Negotiation +500 (or +250) per net success; one week; no backup. Supplies "
            "the 20 Mp compressed virus (bunny icon; a rapier image on every terminal a day later; erases "
            "Mankind Revealed; eats 10 Mp an hour if copied). Suggests Ehran chose an Elven editor -- "
            "wrong, it is Sylvia Green. Threatens action against runners who freelance his data. Four "
            "Ork thugs (B3 Q3 S4 C4 I4 W4 E6 R3, armor 2/1, saps; Armed 4, Firearms 4) on his payroll."
        ),
        "contact_skills": ["Discreet corporate contract brokering", "Introductions to well-heeled Johnsons"],
    },
    {
        "name": "Malachi Morgan",
        "role": "President and CEO of Sylvan Information; half a million nuyen and every safe combination in his office safe",
        "archetype": "Corporate Executive",
        "title": "President and CEO, Sylvan Information",
        "race": "Human",
        "gender": "Male",
        "organization": "Sylvan Information",
        "connection": 4,
        "description": "Head of the Elven house of publishing that owns Ehran the Scribe's rights; a second-floor mahogany office with a stand-alone computer, terminal I/O 32, and a mechanical safe behind false paneling.",
        "notes": "Personnel file 6-001 links to 9-201 (his safe's combination). His safe holds half a million nuyen and a sheet listing every other safe's combination and contents -- the shortcut to Sylvia Green's. No stats; off-stage at night.",
    },
    {
        "name": "Ngon Dinh Sum",
        "role": "Vice President and Director of Sylvan Information",
        "archetype": "Corporate Executive",
        "title": "Vice President and Director, Sylvan Information",
        "race": "Human",
        "gender": "Male",
        "organization": "Sylvan Information",
        "connection": 3,
        "description": "Second in importance at Sylvan; a second-floor office with its own safe (file 6-002 / 9-202) and terminal I/O 31.",
        "notes": "Gamemaster may stock his safe as desired. No stats.",
    },
    {
        "name": "Brand Gylgalad",
        "role": "Elven First Senior Editor at Sylvan (spelled 'Elrand Gylgalad' on the system map)",
        "archetype": "Editor",
        "title": "First Senior Editor, Sylvan Information",
        "race": "Elf",
        "gender": "Male",
        "organization": "Sylvan Information",
        "connection": 3,
        "description": "The senior-most editor of the Elven house; second-floor office, safe (6-003 / 9-203), terminal I/O 30. Morlock's guess that Ehran would work with an Elven editor points at him -- wrongly.",
        "notes": "Editing inconsistency: 'Brand Gylgalad' on p.16, 'Elrand Gylgalad' at I/O 30 and file 6-003. No stats.",
    },
    {
        "name": "Mark Fathom",
        "role": "Second Senior Editor at Sylvan Information",
        "archetype": "Editor",
        "title": "Second Senior Editor, Sylvan Information",
        "race": "Human",
        "gender": "Male",
        "organization": "Sylvan Information",
        "connection": 2,
        "description": "Second-floor office, safe (6-004 / 9-204), terminal I/O 29.",
        "notes": "No stats; his safe's contents are the gamemaster's.",
    },
    {
        "name": "Sylvia Green",
        "role": "Elven Third Senior Editor at Sylvan; Ehran's editor -- the handwritten Mankind Revealed is in her safe",
        "archetype": "Editor",
        "title": "Third Senior Editor, Sylvan Information",
        "race": "Elf",
        "gender": "Female",
        "organization": "Sylvan Information",
        "connection": 3,
        "description": "Editing and converting Ehran's latest work, Mankind Revealed, to hypermedia. Second-floor office, terminal I/O 28, and an old-fashioned mechanical safe (combination 5L, 8R, 18L; file 9-205) holding several hundred handwritten pages.",
        "notes": "The only safe that matters in Physical. No stats.",
    },
    {
        "name": "Mei Lei Fujiwara",
        "role": "Fourth Senior Editor at Sylvan Information",
        "archetype": "Editor",
        "title": "Fourth Senior Editor, Sylvan Information",
        "race": "Human",
        "gender": "Female",
        "organization": "Sylvan Information",
        "connection": 2,
        "description": "Second-floor office, safe (6-006 / 9-206), terminal I/O 27.",
        "notes": "No stats.",
    },
    # -- Hates ------------------------------------------------------------------------------
    {
        "name": "Charlie Tarrow",
        "role": "'Charlie-Horse' -- retired founding-generation fixer coaxed back by a network she thought extinct; brokers the APN ear-tip job",
        "archetype": "Fixer",
        "title": "Fixer (retired; back for one job)",
        "race": "Human",
        "gender": "Female",
        "connection": 4,
        "description": (
            "A woman just starting to lose her natural good looks; not even cybernetics and cosmetics can "
            "give her the beauty that once needed no prompting. Old-fashioned: orders and eats dinner "
            "before business, and pays. Calls the runners 'posers' -- a private joke with Wyrd (they're "
            "posing as shadowrunners). Uncomfortable that far too many people know she is involved."
        ),
        "background": (
            "Helped found the fine old fixer traditions in the early 2030s, then after a long, "
            "danger-spattered career left with Wyrd and retired. She and Wyrd were shadowrunners before "
            "the term was popular. Only back because the offer came through a network of fixers she "
            "thought had fallen apart twenty years ago -- Harlequin's channels."
        ),
        "notes": (
            "Fixer contact (SR p.167) with +2 on all skills. Offers 20,000 nuyen plus 2,500 to leave the "
            "sealed envelope (Mankind Revealed's title page) in Xeric's lap and 3,000 per false left ear "
            "tip (about 40,000 total); can go up 10 percent; 5,000 advance, up to 10,000 more; arranges "
            "extra firepower for 500; Wyrd or Trey for a full share. Claims total ignorance of the "
            "conditions. Hands over old-fashioned photographs of Elves killed with swords and bows. Waits "
            "at a prearranged spot to collect the tips and pay."
        ),
        "contact_skills": ["Old-school fixer network (pre-2035 generation)", "Wetwork contracts"],
    },
    {
        "name": "Wyrd",
        "role": "Charlie Tarrow's long-time partner: red high-top-fade hermetic mage in Tres Chic synth leathers who looks like a razor",
        "archetype": "Combat Mage",
        "title": "Hermetic mage; Charlie Tarrow's bodyguard and partner",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": "His eyes flick over everyone before settling on the leader. Red hair in a high-top fade held up by more than nature and static, Tres Chic synth leathers -- everyone reads him as a razor. A hermetic mage of many years' experience, here only to safeguard Charlie while she figures out what is going on.",
        "notes": "Combat Mage (Sprawl Sites p.98). Available to the runners for a full share; Charlie trusts him for long experience.",
    },
    {
        "name": "Trey Wilson",
        "role": "Charlie Tarrow's teenage student -- brash, loyal, slicked-back vampire-movie blond with a Streetline Special",
        "archetype": "Corporate Security Guard",
        "title": "Charlie Tarrow's apprentice and door-watcher",
        "race": "Human",
        "gender": "Male",
        "age": 16,
        "connection": 1,
        "description": "Young, not used to this sort of thing and showing it: a crisply new lined coat, quick careless motions, blond hair slicked back like a refugee from an old vampire movie, the only one visibly armed (Streetline Special in a quick-release shoulder holster). Totally ignorant of subtlety.",
        "notes": "Corporate Security Guard stats. Charlie trusts him because he is too loyal to try anything; a full share if hired. The meet text says 'no more than 18', the cast list says 16.",
    },
    {
        "name": "Harriet Taylor",
        "role": "88-year-old, 36-kilo keeper of the Public Works Archive Hall for 47 years; Shiawase could not fire her; Kerry's mother",
        "archetype": "Archivist",
        "title": "Head of the Archive Office, Seattle Department of Public Works",
        "race": "Human",
        "gender": "Female",
        "age": 88,
        "organization": "Shiawase Corporation",
        "connection": 2,
        "description": "Just under a meter and a half, 36 kilos, looks as if the ceiling fan could blow her away; flowered sun dress, reading glasses, a step ladder for the top shelves; a little deaf, a little senile, pleasant, and mothers everyone -- 'the nice young people' get everything dropped for them and Aunt Sara's Baked Brownies. Pedestrian stats.",
        "background": "Has run the archive 47 years; when the city computerized everything about 35 years ago the virus trashed it all, and when Shiawase won the Public Works contract they tried to fire her and learned the department could not function without her.",
        "notes": "Charisma (4) table p.24: finds the APN building's old city plans in three hours (0 successes) to two; at 1+ mentions an Elf who looked like a samurai asked for the same plans two weeks ago; at 3+ finds the update with the basement elevator and offers to introduce her daughter Kerry.",
        "contact_skills": ["City building plans and public records back to 1900"],
    },
    {
        "name": "Kerry Taylor",
        "role": "Hard-nosed freelance reporter and secret Healer mage out for blood against the APN, who buried her lover's camera crew in ceracrete",
        "archetype": "Investigative Reporter (Former Wage Mage)",
        "title": "Freelance investigative reporter (working for Sceptre Productions)",
        "race": "Human",
        "gender": "Female",
        "organization": "Sceptre Productions",
        "connection": 3,
        "description": "Dark-haired, early thirties, Harriet Taylor's only daughter; noted for embarrassing corps and runners alike with human-rights stories. Careful not to reveal her magic unless she must -- a convenient ace in the hole. For once she does not care about the story, as long as the 'Elf-protectors' get nuked; their kind of 'white magic' the world can do without.",
        "background": "Blew the whistle on the Telamr Elven Slavery ring and wrote on the covert corp wars in Africa; never had time for herself, and a friend is dead because of it -- the leader of Sceptre's lost crew was her significant other. Four months of harassing the APN have convinced them she works for the YET.",
        "notes": "Former Wage Mage, Healer orientation (SR p.38). Gives everything she has on the inner circle: descriptions and photos. Meets in Sceptre's corp-sector townhouse; the APN attack that night is her scheduled 'swan song'.",
        "contact_skills": ["Human-rights exposes on corps and runners", "APN inner-circle dossier"],
    },
    {
        "name": "Aaron Mitchell",
        "role": "'Xeric the Mad' -- the APN's divinely chosen, genuinely mad, terrifyingly persuasive leader; keeps the club's records on paper",
        "archetype": "Bodyguard",
        "title": "Leader of the Association Para-Nobilis; 'Xeric'",
        "race": "Human",
        "gender": "Male",
        "organization": "Association Para-Nobilis",
        "connection": 3,
        "description": "Really is mad: believes he alone was chosen to save the Elves from themselves, and when he starts talking other people start to believe it too. Sleeps on a mat among desk lamps in an expensively Japanese rice-paper bedroom; indoctrinates converts in an office with a bronzed quill 'once used by the Elven sage Xeric' and an Ares Predator II in the drawer. A poser: surgery and false ear tips.",
        "background": "Leo Ridgeworth's secretary; convinced Ridgeworth's 2043 monorail death was murder, trained the 27 members as soldiers and led the covert war that left six alive, then took the name Xeric and rebuilt the APN to about 300 through recruitment. Registered leader on the Seattle Political Database as 'Aaron Mitchel'.",
        "notes": "Bodyguard stats (Sprawl Sites p.97). Phones the admissions office to confirm any silent alarm before raising the alert; once raised, joins the guards protecting Allair in the workroom. The envelope (title page) must land in his lap for 2,500 nuyen. Would have Fierelle 'die for the good of the cause' once he notices her doubts.",
    },
    {
        "name": "Fierelle the Red",
        "role": "APN founding survivor who dresses and sleeps in blood red for the Elves she could not save -- the one councilor who can be talked round",
        "archetype": "Combat Mage",
        "title": "Council of Elders, Association Para-Nobilis; 'the Red Woman'",
        "race": "Human",
        "gender": "Female",
        "organization": "Association Para-Nobilis",
        "connection": 2,
        "description": "A woman dressed entirely in red, awake and watching from a bed among red veils, red bedclothes, red walls and red carpets in a room like a blood-red Arabian Nights tale on the ground floor, a guard with a Uzi III outside. Lost her real name years ago; senior to Xeric but under his charisma; for weeks has wondered whether killing Metahumans to preserve their purity is right, not helped by seven-year-old Maria calling it murder.",
        "background": "Started all this to help people and lost her mind in the Great Purge after Ridgeworth's death; wears red as a reminder of the dead.",
        "notes": "Combat Mage (Sprawl Sites p.98). When the alarm sounds she stays put, wondering; her instinct is to talk, not shoot. Spoken to calmly she may help or at least not hinder, and hands over her cosmetic ear tips; Maria running in screaming 'Don't hurt the Red Woman' helps. Karma 1 for letting her atone.",
    },
    {
        "name": "Allair Shadowdeath",
        "role": "BTL-ruined scientist who built the APN's alarms and 'Elven philosophy' chips and now believes he is the Great and Powerful Mage of Death",
        "archetype": "Scientist (Simsense)",
        "title": "Council of Elders, Association Para-Nobilis; alarm and chip maker",
        "race": "Human",
        "gender": "Male",
        "organization": "Association Para-Nobilis",
        "connection": 2,
        "description": "A balding man with pointed ears in a long flowing black robe, asleep on a pile of rubbish under his bed among photos of vid stars circled in blood red. Woken, he demands you kneel before the 'Great and Powerful Mage of Death' -- the BTL chip in his chipjack makes him say it and believe it. No combat ability; a workroom of beakers of Sloppy Soy mixes.",
        "background": "A brilliant scientist before BTL chips took his mind 'far into the dark caverns of truth'; built the headquarters' alarm system, then illegal simsense chips to give members 'Elven' philosophy; now kills those he once hoped to save.",
        "notes": "Scientist (Sprawl Sites p.108, Simsense specialty); an HK227 is nearby but four guards defend him behind the overturned workbench when the alarm is up. Most pitiful of the core; Xeric protects him.",
    },
    {
        "name": "Blaine Deathedge",
        "role": "The APN's black-clad enforcer and biggest killer; his bedroom is a war museum from an AVM to an original Bowie knife",
        "archetype": "Street Samurai",
        "title": "Council of Elders, Association Para-Nobilis; enforcer",
        "race": "Human",
        "gender": "Male",
        "organization": "Association Para-Nobilis",
        "connection": 2,
        "description": "Always in black; does not care whether it is little old ladies the APN wants geeked as long as he gets to kill some. The biggest and deadliest of the core, 'the great mystery', who uses any weapon to finish a job -- missiles, grenades, other people. A military cot with an alarm-light panel at its head in a room that is half war museum, half cemetery. Thiran is his closest companion.",
        "notes": "Street Samurai (SR p.46). 50 percent chance he is awake meditating if no alarm; with the alarm he waits inside with an HK227 (explosive ammo) until the attackers are elsewhere, gathers surviving flunkies and hits the invaders from behind.",
    },
    {
        "name": "Thiran",
        "role": "APN Weapons Master with a fright-mask of scars, a taste for hack-and-slash and flash grenades, and explosive arrows that do not work",
        "archetype": "Former Tribal Warrior",
        "title": "Council of Elders, Association Para-Nobilis; master-at-arms",
        "race": "Human",
        "gender": "Male",
        "organization": "Association Para-Nobilis",
        "connection": 2,
        "description": "Dozens of fights have left his face a fright mask of scars and the rest of him not much better; treats his body like a chopping block on which others may shatter their swords. An expert in medieval combat better suited to frontal hack-and-slash than subtle thrust and parry. Sleeps in the basement, an outer room piled with UrbanBrawl and Thai kick-boxing magazines, to escape the others' scrutiny.",
        "notes": "Former Tribal Warrior (Sprawl Sites p.103) with a sword in place of the Beretta; Ares Predator II at all times, six or seven flash grenades, an HK227 when the archery range is defended. Retina-keyed to the ammo room. Teaches archery on a range whose wall projections protect archers from his exploding arrows.",
    },
    {
        "name": "Erendahl",
        "role": "Tall, blond, gorgeous APN councilor in it for the fun of confusing cops and geeking runners; scouts the runners at Kerry's townhouse",
        "archetype": "Former Tribal Warrior",
        "title": "Council of Elders, Association Para-Nobilis; raid leader",
        "race": "Human",
        "gender": "Male",
        "organization": "Association Para-Nobilis",
        "connection": 2,
        "description": "Probably the closest of the Council to a classic Elf in looks -- tall, blond, exceptionally handsome (and a poser). Joined to mock Lone Star and geek runners, not to preserve the Elven ideal; takes any chance to hurt or embarrass runners as long as his 'stick isn't thrown out.",
        "notes": "Former Tribal Warrior (Sprawl Sites p.103) with Projectile Combat instead of Etiquette (Tribal); Ares Predator II; HK227 in the range fight. Watches the townhouse attack from outside without engaging and reports to the Council that the runners are formidable and it should hire mercs or runners. Retina-keyed to the ammo room; plans the next raid with Thiran in the basement.",
    },
    {
        "name": "Maria (the Red Woman's friend)",
        "role": "Seven-year-old who sneaks into the APN lounge to sleep on the couch, with Fierelle's unofficial blessing; not an APN member",
        "archetype": "Child",
        "title": "Neighborhood child",
        "race": "Human",
        "gender": "Female",
        "age": 7,
        "connection": 1,
        "description": "A little girl asleep on the lounge couch under a vidscreen (under the couch once the alarm sounds). Questioned by a sympathetic runner she tells where the 'Red Woman' sleeps and, in her own words, about the Red Woman's questions on whether it is right to kill someone to keep him pure.",
        "notes": "Karma 1 for saving or protecting her, -2 for killing her by mistake. Her 'Don't hurt the Red Woman' can turn Fierelle.",
    },
    # -- Past -------------------------------------------------------------------------------
    {
        "name": "Walturr",
        "role": "Ex-runner barkeep 'hardwired to the counter' by the Seoul Men; old pal who drops three musclemen and hands over the kaleidoscopic invitation",
        "archetype": "Bartender",
        "title": "Barkeep (bar unnamed; German-beer-poster back room)",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": "An old pal who used to do some shadowrunning himself before the Seoul Men had him hardwired to the counter. Motions the runners into a back room of faded posters of bosomy German blondes and yesterday's sport stars clutching foaming mugs, then leaves three hired musclemen sprawled unconscious but unbloodied on the tavern floor and rifles their effects: 'You know them dreks? I think it's for you.'",
        "notes": "One-scene opener for Past. Whether 'Seoul Men' is a Seoulpa ring is not stated.",
        "contact_skills": ["Neighborhood bar gossip", "Quiet handling of strangers asking after runners"],
    },
    {
        "name": "Baron Munchmaussen",
        "role": "Sick, rheumatic Troll Graf of a Bavarian valley, medievalist and paranoid, who toys with 'Yankee hitmen' for the thrill and prizes a demonic tome above his life",
        "archetype": "Troll Bouncer (noble)",
        "title": "Graf Munchmaussen, ruler of Munchmaussen Valley",
        "race": "Troll",
        "gender": "Male",
        "nationality": "German (Bavarian)",
        "organization": "Barony of Munchmaussen",
        "connection": 4,
        "description": "Dresses in the medieval fashion of a German noble, speaks several languages elegantly (German with or without Bavarian accent, English), a student of Sociology and Etiquette (Jet Set). Office work by day, dinner with friends, four laps in the warm pool, a steam room for the pain, insomniac hours among his Dark Ages treasures in the Blue Gallery and a weight room he can no longer box in. 'So that's all you were looking for, nicht war? I am so disappointed.'",
        "background": "Once a big spender known from the Riviera to the Alps, now a recluse whose painful rheumatism ended the constant excess and travel; an unconscious longing for death makes him take ever greater risks. Believes he has evidence Trolls inhabited Bavaria in the middle Dark Ages and that the Pandemonicus Faustus substantiates it -- worth more to him than life.",
        "notes": "Troll Bouncer stats (SR p.173), Sociology 3, Etiquette (Jet Set); keeps the Brown Hall key on a gold chain round his neck. Believes the valise is a bomb; lets intruders reach the library replica to betray their goal, then attacks with Goldi's two Force 4 Fire Elementals and the keep guards; if captured he pries at the mission then escapes; if he cannot keep the book he flees to hunt the runners down at a time and place of his choosing. Escapes in a Hughes Airstar with collapsible rotors.",
    },
    {
        "name": "Goldi Schonbosom",
        "role": "Munchmaussen's cheery Director of Tourism -- secretly the baron's chief of intelligence and a Fighter-orientation mage with Fire Elementals in the fireplace",
        "archetype": "Former Wage Mage (Fighter)",
        "title": "Director of Tourism, Munchmaussen; chief of intelligence to the Baron",
        "race": "Human",
        "gender": "Female",
        "nationality": "German (Bavarian)",
        "organization": "Barony of Munchmaussen",
        "connection": 3,
        "description": "'Welcome, chumlichen! My name is Goldi.' Meets every train with the customs men, arranges sports tournaments and hotel dances, conducts driving tours (no rentals here), acts the kindly friend -- and quizzes strangers about their luggage, the valise ('Is one of you a doctor?'), crime back home and 'such a mess in Berlin', reading their politics with intuition and spells. Keeps her magic secret.",
        "notes": "Former Wage Mage, Fighter orientation (SR p.38), Charisma 4. Opposed Intelligence vs the talkative runner (TN 3-4 for good roleplay): if she wins she is their guide for the day and tips the baron. Summoned to the castle she conjures two Force 4 Fire Elementals in the Great Hall's Rating 4 circle, hides them in the library fireplace and watches from closet 15a through a one-way portrait; prefers Mana Bolt from behind, Sleep if losing. Personnel file DS-18 to 20 lists her 'secret' post.",
    },
    {
        "name": "Father Braun",
        "role": "Priest of St. Gretchen's and quiet heart of the Munchmaussen Underground",
        "archetype": "Priest",
        "title": "Parish priest, St. Gretchen's, Munchmaussen; leader of the local resistance",
        "race": "Human",
        "gender": "Male",
        "nationality": "German (Bavarian)",
        "organization": "Munchmaussen Underground",
        "connection": 2,
        "description": "The priest of the ancient Gothic church that, unknown to the baron, is the center of the valley's feeble resistance. Might help runners who need allies against Munchmaussen, or a place to rest and heal after the adventure.",
        "notes": "No stats. The fallback if the team fails the schloss on the first try or is captured.",
        "contact_skills": ["Sanctuary and healing in Munchmaussen Valley", "The valley's resistance"],
    },
    {
        "name": "Georg Willems",
        "role": "Kapitan of Luftlande Flight 613, the Seattle-Berlin transorbital",
        "archetype": "Pilot",
        "title": "Kapitan, Luftlande Airlines",
        "race": "Human",
        "gender": "Male",
        "nationality": "German",
        "organization": "Luftlande Airlines",
        "connection": 1,
        "description": "'This is Luftlande Flight 613, and I am Kapitan Georg Willems.' Calls the boosters, the No Smoking/Chipping sign and the reassurance that Tempelhof 'is no longer experiencing the difficulties reported in the morning news'.",
        "notes": "Voice on the intercom only; the Skyclimber's computer is what Hildi decks to kill the restraint bracelets.",
    },
    {
        "name": "Hildi",
        "role": "Eagle's Union of Destiny decker posing as half of an affectionate German couple; kills every restraint bracelet on Flight 613",
        "archetype": "Decker",
        "title": "EUD agent",
        "race": "Human",
        "gender": "Female",
        "nationality": "German",
        "organization": "Eagle's Union of Destiny",
        "connection": 1,
        "description": "Clean-cut, affectionate with her 'husband', one of two couples who board together and speak German several rows back. Once the smoke bomb goes off she jacks into the shuttle's computer to disarm her comrades' bracelets and finds she can only disarm all of them -- and does; the restraints stay dead only while she is on her deck.",
        "notes": "Decker stats (SR p.34). Partners Klaus, Fritz and Mikki (Gang Member stats, spurs) do the killing and plant the evidence.",
    },
    {
        "name": "Hardrow",
        "role": "Flashily dressed Easterner selling pure-bred man-killing hunting dogs to Germans; nearly gets himself shot going for his hounds in the putsch",
        "archetype": "Dog Trainer",
        "title": "North American dog trainer (with Sheila)",
        "race": "Human",
        "gender": "Male",
        "nationality": "UCAS (Easterner)",
        "connection": 1,
        "description": "'Pleased t'meecha. Name's Hardrow. This is Sheila. We're dog trainers.' Enormous smile; three hunting hounds in the baggage car. 'These Germans are pushovers for hunting dogs. Especially man-killers. But we don't do any of that cyberstuff.' Hears 'putsch' as 'pooch' and lurches for the baggage compartment through a firefight.",
        "notes": "Munich-to-Munchmaussen train color. Likely to die between the brigands and the liberators unless the runners step in.",
    },
    {
        "name": "Sheila (dog trainer)",
        "role": "Hardrow's companion; the only Bavarian-dialect translator on the train, wrong half the time",
        "archetype": "Dog Trainer",
        "title": "North American dog trainer (with Hardrow)",
        "race": "Human",
        "gender": "Female",
        "nationality": "UCAS",
        "connection": 1,
        "description": "Hardrow's female companion on the old diesel train into Munchmaussen. The only character who can translate the Bavarian dialect (+2 TN from ordinary German) that every German NPC speaks -- and she gets the interpretation wrong half the time.",
        "notes": "Train color; a comic liability in negotiations with the extorting soldiers.",
    },
]

NPCS += [
    # -- Loves ------------------------------------------------------------------------------
    {
        "name": "Sandii",
        "role": "Fixer with stainless-steel razor teeth (a 'gift' from a dissatisfied oyabun) and a Chevy Vanguard; the cut-out for the YET / Dassurn job",
        "archetype": "Fixer",
        "title": "Fixer (no last name, no handle -- just Sandii)",
        "race": "Human",
        "gender": "Female",
        "connection": 3,
        "description": "Slides into the runners' favorite table at Club Penumbra with a patented smile that flashes light off stainless-steel razor-teeth, rumored to be a gift from an oyabun with no tolerance for failure; her fingers are all present -- at least they seem to be hers. Drives a big Chevy Vanguard van through Thursday-night traffic with off-color remarks about Seattle's night owls. 'This is strictly a business call.'",
        "notes": "Slaps down 250 nuyen each just to listen; waits up the street from Fire Station 118 with the team's gear; hands over the chip with Johnson's program and the wax-sealed envelope once clear; takes possession of the passcodes at Club Penumbra for 40,000 each (minus deductions, plus 1,000 each for the Sylvan client list and for returning Johnson's program -- 250 if she has to ask).",
        "contact_skills": ["Puyallup Barrens fixing", "Discreet transport"],
    },
    {
        "name": "Lee Gorbin",
        "role": "Young Elven Technologists member 'delayed' so a gold-toothed twin could take his place at the party -- and possibly Harlequin's mask",
        "archetype": "Policlub Member",
        "title": "Member, Young Elven Technologists",
        "race": "Elf",
        "gender": "Male",
        "organization": "Young Elven Technologists",
        "connection": 1,
        "description": "'I tell ya, I am Lee Gorbin!' -- the shrill protest at the door as three Trolls with Ares MP-LMGs close in. The real Lee is the twin of the runners' Mr. Johnson: an Elf who could pass for a misshapen Human or a good-looking Ork, thin pink scar lines across a close-cropped scalp, a craggy quartz face, a slightly undersize mouth over stunning gold-capped teeth, and a smooth, cultured Elven accent.",
        "notes": "Alex Manke hustles the real Lee to the basement and sends the Trolls after the other one, who has simply vanished. 'Who is Mr. Johnson, the imposter Lee Gorbin? It might be Harlequin... We're not saying.' A party-goer later says 'I'm telling ya, Lee, a lot of those APN got geeked and are blaming us for it.'",
    },
    {
        "name": "Alex Manke",
        "role": "Young Elven Technologists' Security section head; Elven street samurai who hired the Troll muscle and holds the armory passkey",
        "archetype": "Elven Street Samurai",
        "title": "Security, Young Elven Technologists",
        "race": "Elf",
        "gender": "Male",
        "organization": "Young Elven Technologists",
        "connection": 3,
        "description": "Steps in during the Lee Gorbin scuffle, orders the three Trolls to find the other Gorbin and spirits the real one to the basement. Occupies the first administration office in the early evening; the armory (Barrier 24) opens only to his passkey or SM-4.",
        "notes": "Elven Street Samurai (Sprawl Sites p.104). Runs six guards early, three late; the defense is geared for a frontal assault, not subtlety. Hired the three Troll Street Samurai (Street Samurai Catalog p.108) bunking in the second-floor flats.",
    },
    {
        "name": "Nick Francis",
        "role": "Young Elven Technologists' Indoctrination section head",
        "archetype": "Policlub Officer",
        "title": "Indoctrination, Young Elven Technologists",
        "race": "Elf",
        "gender": "Male",
        "organization": "Young Elven Technologists",
        "connection": 2,
        "description": "One of the three section heads of the Puyallup branch with a maglocked basement office (passkey or SM-4). Runs the two-hour lectures and the follow-up invitations that turn curious party-goers into members.",
        "notes": "Named in the Seattle Political Database excerpt and the basement key; no stats, office empty after 11 p.m.",
    },
    {
        "name": "Patricia Stein",
        "role": "Young Elven Technologists' Recruitment section head; her attractive recruiters dance deckers into the fold",
        "archetype": "Policlub Officer",
        "title": "Recruitment, Young Elven Technologists",
        "race": "Elf",
        "gender": "Female",
        "organization": "Young Elven Technologists",
        "connection": 2,
        "description": "Section head with a maglocked basement office. Her recruiters (Simsense Star stats) ask any decker who walks the walk for the next dance: 'Deckers are just about the most important people in our organization... maybe I could show you our computer room?'",
        "notes": "Recruiting drives at the University and the decker BBSs; recruits funneled to Sylvan Information. No stats.",
    },
    {
        "name": "John Winter",
        "role": "Registered leader of the Young Elven Technologists on the Seattle Political Database; Ehran calls the shots",
        "archetype": "Policlub Leader",
        "title": "Leader, Young Elven Technologists",
        "race": "Elf",
        "gender": "Male",
        "organization": "Young Elven Technologists",
        "connection": 2,
        "description": "The name on the policlub's registration as leader. 'He's listed as a backer of the Young Elven Technologists, but I think he calls the shots' -- said of Ehran, not Winter.",
        "notes": "Name only (p.142). Never appears; a hook for a GM who wants a face for the club between Ehran's visits.",
    },
    {
        "name": "Lancelot Windtree",
        "role": "Gorgeous, whiny, racist Tir Tairngire elf mage of Ehran's entourage who assenses the runners under torture and mocks their screams",
        "archetype": "Elf Mage",
        "title": "Peripheral member of Ehran the Scribe's entourage; Young Elven Technologists",
        "race": "Elf",
        "gender": "Male",
        "nationality": "Tir Tairngire",
        "organization": "Young Elven Technologists",
        "connection": 2,
        "description": "Handsome and elegant, thin features, silver hair, the whole nine meters, and he knows it; loose natural-fiber tunic and trousers, obviously expensive, an ornamental sword slung over his back. Wears boredom and bigotry like a badge at the YET party; only Elves who use magic are his equals, other Elves barely acceptable, non-Elves inferior, Orks and Trolls most of all. Thinks that when Ehran sneezes diamonds come out of his nose. A coolly elegant voice sneering at agony.",
        "background": "An atypical, uptight Tir Tairngire Elf thrilled to receive orders directly from the patron saint of the YET to assist 'my trusted associate Ariel Nasir' in a matter of 'the greatest importance to the sacred goals of our people'. Started on Iggy one evening; only Ariel's stern intervention kept Bonecrack from putting him in the morgue.",
        "notes": "Elf Mage (Sprawl Sites p.100; else Street Mage) with a Magic Sword Focus +3; sleeps in the safe house magic lab with four units of Fire Elemental ritual materials. Attacks astrally any magician who projects from the chair; may kill Iggy in the breakout. Disappears back into Tir Tairngire if he survives -- unreachable; loyal to Ehran under interrogation. The expendable YET body faking Ehran's death in Althain is 'Windtree, perhaps?'.",
    },
    # -- Counterstroke ----------------------------------------------------------------------
    {
        "name": "Ariel Nasir",
        "role": "'Ariel' -- extremely old Free Air Elemental bound by her true name to Ehran; a young Sophia Loren who traps, stalks and, when it suits her, helps the runners",
        "archetype": "Free Air Elemental",
        "title": "Free spirit in Ehran's service; alias 'Ariel Nasir', freelance mage",
        "race": "Spirit (Free Air Elemental)",
        "gender": "Female",
        "connection": 5,
        "description": "In her favorite form a statuesque, beautiful woman of classic Mediterranean looks -- olive skin, dark chestnut hair, eyes so brown they look black, imperious aquiline features with humor at the corners of the mouth; think of the young Sophia Loren. Can take any Human or Metahuman form; in her true aspect she is wrapped in cloud, hair whipped by spectral winds, eyes pools of pearly light. Soft-spoken and courteous in the elaborate manner of Moorish culture at its height; stormy when angered; silences opposition with power. Needs no sleep, clothes or bathing; everything she seems to wear is illusion. Portrait as a lady in early-15th-century Spanish dress.",
        "background": "Ehran knows her true name and has bound her to obedience; she cannot work against him or seek to break his control, but servitude galls a spirit that has tasted freedom, and if the mortals can be led to clues about her master -- the coded wristphone, the holo-paintings -- well, that is hardly her fault. She has memories of her own of other nights, other skies.",
        "notes": "Stats p.89: B6 Q11 (x4, flies at ground speed) S5 C8 I8 W8 R9, Force 5, Spirit Energy 3; Sorcery 8, Unarmed 11, Driving 5; Magic pool 11. Powers: Aura Masking (only an initiate can pierce it), Engulf, Human Form, Manifestation, Movement, Noxious Breath, Psychokinesis, Sorcery. Spells (max Force 5, no Drain, no ritual/foci/fetishes): Chaotic World 5, Mind Probe 5, Clairvoyance 3, Powerball 5, Heal Deadly Wounds 5, Stun Blast 5. Attackers use Willpower instead of weapon skill; without her true name she can only be disrupted (a month off the physical plane). Weaknesses: Allergy (extreme) to confinement by airtight seal -- sealing the safe house air disrupts her; Vulnerability (Earth). Watches the runners astrally and with hired snoops; drives the gas van; prefers non-lethal force; returns at Althain to forbid interference in the duel, to tell what little she will (the ear, that all three are far older than they look, that Althain recalls Ehran's childhood home), and to warn everyone out before Ehran returns. Sees the runners as future tools against Ehran.",
        "contact_skills": ["Clues to Ehran the Scribe (when it serves her)"],
    },
    {
        "name": "Shirley Marquis",
        "role": "Small-cog NatVat manager, drugged to the eyebrows and set out as bait by the corporation's own police",
        "archetype": "Corporate Wage Slave",
        "title": "Mid-grade manager, Natural Vat Foods",
        "race": "Human",
        "gender": "Female",
        "organization": "Natural Vat Foods",
        "connection": 1,
        "description": "Walks Grantleigh Park every evening about sunset from the NatVat condo complex; told someone will approach with 'We're from the Easter Bunny'. Under the street light her pupils are huge -- calm, smiling, no change of expression. She is bait. You're hosed.",
        "notes": "The extraction itself was legitimate (dossier chip with holos, NatVat personnel profile, background). Whether she knew anything worth extracting is never said; nobody comes back for her.",
    },
    {
        "name": "Chuckles",
        "role": "Bonecrack's ganger who AVMs a NatVat Patrol-1, lays down LMG cover, then seals and gasses the van -- and himself",
        "archetype": "Ganger",
        "title": "Ganger, Bonecrack's gang",
        "race": "Human",
        "gender": "Male",
        "organization": "Bonecrack's Gang",
        "connection": 1,
        "description": "Rides the back of Ariel's van, puts an AVM into the Patrol-1, keeps the corp cops' heads down with an LMG, and profanely points out that he can do it only for the moment if the runners hesitate about gettin' into the fraggin' van. Once Ariel vanishes he presses the button, takes a deep breath as ordered, and joins everyone in dreamland.",
        "notes": "Gang Member stats implied. The van is bugged for video and audio; murder him and Bonecrack kills the offender when he sees the tape.",
    },
    {
        "name": "Martin Halloran",
        "role": "'Bonecrack' -- cold-blooded 27-year-old street samurai with a harness LMG whose only soft spot is his brain-damaged Troll brother",
        "archetype": "Street Samurai",
        "title": "Gang leader and mercenary; Ariel's hired muscle",
        "race": "Human",
        "gender": "Male",
        "age": 27,
        "organization": "Bonecrack's Gang",
        "connection": 3,
        "description": "Tall, scarred, bulky with real and implanted muscle; very pale skin, black hair, icy gray eyes -- street word says looking into them shows you the color of death. Rarely shows emotion; killing is neither liked nor disliked, just often the simplest solution; treats a dying enemy with the same tactical caution as a fresh one. 'Nothing personal, chummers. Biz.' Pay the fee, he does the job, kidnapped child or little old lady. Calls his brother Ignatius or 'kid', never Iggy; the old game: 'Is it... yes it is, it's the great Kid Ignatius.' 'And the crowd goeth wild!'",
        "background": "First loyalty to himself and Ignatius. Rumor says he killed the quack whose 'treatment' ruined his goblinizing brother's mind, a week after. Gives employers the professional loyalty they pay for but will not die for a hosed job; gives his gangers protection, medical and legal bills.",
        "notes": "Street Samurai (SR p.46) +2 to all combat skills and Etiquette (Street). Gear: Ares MP-LMG with deluxe gyro-mount and smartlink (100-round belts, explosive 5S5 and normal 5S3), Ingram Smartgun with gas vent 2 (gel 4L1 Stun, explosive 5M5), monofilament sword (8M3, Reach +1), shock glove (5L3 Stun), armor jacket 5/3. Runs the wheelchair escort with standard ammo; beats a merc senseless for insulting Iggy; will not let his men shoot with Iggy in the line of fire. If Iggy dies he hunts the killer without rest; if a runner saves either brother's life, both become loyal allies -- 'a tactical nuke with an unstable fuse for a sidearm'. Etiquette (Street) 6 to recognize him.",
        "contact_skills": ["Contract muscle and mercenary crews", "Street-level kidnapping and holding"],
    },
    {
        "name": "Ignatius Halloran",
        "role": "'Iggy' -- 15-year-old Troll with a seven-year-old's mind, a toy Lone Star patrol car, a talking clown doll and a combat axe; Bonecrack's brother",
        "archetype": "Troll Street Samurai",
        "title": "Bonecrack's brother",
        "race": "Troll",
        "gender": "Male",
        "age": 15,
        "organization": "Bonecrack's Gang",
        "connection": 1,
        "description": "A typical-looking Troll with a dreamy, unfocused expression, a childish lisp in a gravelly basso profundo, and a tear that rolls down a warty cheek. 'C'n I have my polithe car back, pleathe? Thay, are you crookth?' Cheerful, quick to bounce back, ecstatic as a petted puppy when someone is nice to him -- especially a woman, whatever her race; he does not understand the feelings in his body lately. Calls his brother 'Marty' and hates anyone else using his real name. Remembers how people behaved and can hold a long grudge.",
        "background": "Goblinized at eleven; his desperate parents rushed him to a doctor who advertised that his treatments could arrest or reverse the change. They did nothing but cause severe brain damage. A week later the quack was found dead in his clinic. Bonecrack has had him heavily cyber-modified: in his value system only lethal power gives Iggy a chance of survival.",
        "notes": "Troll Street Samurai (Street Samurai Catalog p.108): Armed Combat 5, Armed Combat (Axe) 7, Stealth 5, Unarmed 6. Gear: armor jacket 5/3, Bandai-US Chrysler-Nissan Patrol-1 model with action siren and lights, club (11M2 Stun), Mr. Storeez talking clown doll (100 hours of stories and jokes), Wallacher Combat Axe (10S2, thrusting 5L3). Fights only when threatened or hurt, or when Marty says someone is bad; goes berserk if Bonecrack dies, crouches over him if he falls. Sneaks the toy car -- with a monofilament utility saw hidden in the passenger compartment -- to a prisoner he likes 'to make them feel better'. Compassion to a dying Iggy is worth Karma.",
    },
    {
        "name": "Doctor What",
        "role": "Giggling cherubic street-doc torturer with a bio-injector and a taste for knives; buys his protection from a powerful Yakuza gang",
        "archetype": "Street Doc (torturer)",
        "title": "Street doc and professional interrogator (elite clientele)",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": "A chubby little beardless Santa Claus: clear pink skin, cherubic face in a fluffy halo of white hair, twinkling blue eyes. 'Hello! What is my name.' -- a statement, not a question, followed by innocent delight at the double-take. Ties on a vinyl apron, clips electrodes while rambling a pointless monologue, and hums along telling jokes as his victims scream: 'Most people hate toothache worse than anything.' A physical coward who whimpers and begs if threatened, and kills in a moment with the bio-injector given half a chance from behind.",
        "background": "A street doc with a rep known only to an elite clientele: with drugs, biofeedback probes and mostly good old-fashioned pain he can extract information from anyone, at reasonable rates. He loves his work. Ordered not to kill on this job, which limits his beloved knives.",
        "notes": "Street Doc (SR p.171) with Unarmed Combat (Bio-injector) 8 and Interrogation (Torture) 6; secure clothing (3). Bio-injector (15,000 nuyen): wrist-mounted laminated monofilament spike, 4L1 Stun plus a drug, half Impact armor, four doses -- one Narcoject, one Fugu-5, two Agonadine-delta (4D2, +4 TN nerve pain, Deadly = screaming death in minutes). Sessions: 10 boxes Mental damage the first round, then Interrogation tests at TN = victim's Willpower or Body (higher) with 6D3 Stun per test until ten successes; can paralyze vocal cords with a switch. Keeps packing his sickroom under alert. Going after him later is an adventure in itself.",
    },
    # -- Spiritual --------------------------------------------------------------------------
    {
        "name": "Anson Helm",
        "role": "One of Seattle's best-connected fixers -- an honest one, rich enough for a Lear Platinum; a mobile Mr. Johnson who is the employer, not the middleman",
        "archetype": "Fixer",
        "title": "Fixer and contractor (Lear Platinum Custom; staff of agents)",
        "race": "Human",
        "gender": "Male",
        "connection": 5,
        "description": "Immaculately groomed, late forties, a cultured voice on the intercom and a handshake with a power usually lacking in his type. 'I just bought the plane and wanted to try it out. And it's so private up here.' Exactly what he seems: when Helm makes a deal he delivers, which has earned him wealth beyond most fixers' dreams; he gives operatives every possible edge and then has never heard of them.",
        "background": "Contracts with organizations to take their special jobs and pays operatives out of pocket; keeps a small staff of agents (Mercer, the IL-290 rigger, the Portuguese tanker, Captain Colon, Graeme Greene) for short-term tasks and hires shadowrunners for the long, tough, replaceable stuff. Harlequin hired him, fronted a lot of nuyen, and told him to impress the runners with his wealth. Also written 'Helms'.",
        "notes": "Fixer contact (SR p.167) played as a mobile Johnson. Offers 150,000 nuyen each, 10 percent now, plus a 10 percent bonus for no casualties; four Tupi-Guarani linguasofts (3), two Winged 4 skillsofts, pilot chips, any gear they will actually carry (half normal encumbrance for the jungle), a plantation map marking the greenhouse, covert insertion and Lima tickets. Will not speak of his employer (see Running Harlequin p.146). Tells the returning team to hold the flower and await another Johnson.",
        "contact_skills": ["Top-end international job contracting", "Covert insertion logistics (air, sea, VTOL)"],
    },
    {
        "name": "Mercer",
        "role": "Helm's tall, dark-skinned, Boston-accented island associate; seaplane pilot to the tanker",
        "archetype": "Pilot",
        "title": "Associate of Anson Helm",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": "Waits on a grassy island strip barely big enough for the Lear in fashionable white and tan island garb, a decidedly out-of-place Boston accent, a pickup truck and a seaplane in a lagoon. Affable about local politics and sights, says nothing of Helm's plan except that it is 'one of the prettiest things I have ever seen', and lands blind by inertial and satellite nav against the dark bulk of an oil tanker.",
        "notes": "Hands over the tracking device to the river contact and briefs the VTOL drop: 'Once the VTOL grounds, you'll have only a couple of seconds.'",
    },
    {
        "name": "Captain Colon",
        "role": "Cigar-chewing Portuguese-speaking master of the ugly electric tug Esperanca; pink bandanna on the left arm; ten days up the Amazon",
        "archetype": "Riverboat Captain",
        "title": "Captain of the Esperanca",
        "race": "Human",
        "gender": "Male",
        "nationality": "Amazonian",
        "organization": "Amazonia",
        "connection": 2,
        "description": "A tall Latino with a slim cigar, leaning against the cabin of the ugliest, most battered boat you have ever seen -- an ancient tug with a retrofit electric engine, a high-frequency insect repeller and a short-wave -- barking orders in Portuguese at his laborers, a stained pink bandanna on his left arm. 'Friends, I am Captain Colon, and this is my ship, the Esperanca.' Very good English; two crewmen who sleep on deck.",
        "notes": "Ten uneventful days upriver with refueling every other day and 24 hours of business in Manaus. Gladly explains the government's pro-environment policies: an ecologically balanced nation and society.",
        "contact_skills": ["Amazon river transport, Macapa to Fonte Boa"],
    },
    {
        "name": "Graeme Greene",
        "role": "Lonely elderly British expatriate, owner-pilot of the illegal gas-engined amphibian Marsh Rose; asks too many pointed questions",
        "archetype": "Bush Pilot",
        "title": "Owner and pilot of the Marsh Rose, Fonte Boa",
        "race": "Human",
        "gender": "Male",
        "nationality": "British",
        "connection": 2,
        "description": "An elderly man with a thin white moustache and a clipped British accent, mopping sweat with a soiled pink bandanna on the Fonte Boa dock: 'Are you Helm's people?' Buys the team dinner on Helm's account, settles them in a boarding house, and plies them with suspiciously pointed questions -- the sharpness of a lonely mind living out its last years in a backwater of what he still calls Brazil, missing brighter lights.",
        "notes": "Not a counteragent. Apologizes abjectly if the team gets too suspicious. Hides the plane an hour out of town (gas engine; pollution, you know); flies 650 km up the Jutai in five hours on half his fuel and poles off the sandbar: 'If you're ever in the neighborhood again, drop by.'",
        "contact_skills": ["Amphibious flights on the upper Amazon tributaries"],
    },
    # -- Future -----------------------------------------------------------------------------
    {
        "name": "Betty (the Style)",
        "role": "Grinning Troll doorwoman of the Tacoma Style who pats you down and enforces the dress code",
        "archetype": "Troll Bouncer",
        "title": "Head doorman / bouncer, the Tacoma Style",
        "race": "Troll",
        "gender": "Female",
        "connection": 1,
        "description": "The Style's head doorman, or doorwoman, or doortroll; never stops grinning as she pats guests down for hidden weapons -- obviously her idea of a good time. Turns away the dirty, the too casual and the too outrageous; a fashion statement is one thing, but this is a conservative corporate hangout.",
        "notes": "Troll Bouncer (SR p.173) with Quickness 5, Reaction 3, Armed Combat 6; sap, armored vest, Tres Chic clothing.",
    },
    {
        "name": "Jane Foster",
        "role": "'Frosty' -- snow-white-haired CommTech secretary and Pretenders hanger-on who is, unknowing, Ehran the Scribe's daughter with a spell lock grown into her thigh",
        "archetype": "Corporate Secretary",
        "title": "Secretary at CommTech Inc., Columbia, Missouri; Ehran's hidden daughter",
        "race": "Elf",
        "gender": "Female",
        "connection": 2,
        "description": "Tall and thin with a cascade of long snow-white hair; equally at home in corporate suits or biker synth-leather, always the finest quality and one-of-a-kind, simple elegant jewelry and a heavy platinum ring shaped like a coiled dragon that she never takes off. Always in control, hates surprises, thinks constantly about the future -- hard-edged at first contact, passionate and quick to make friends when she chooses. Loyal to her friends and herself, in that order; friends are her only blind spot. (The book never states her metatype; Ehran's blood and the hair suggest Elf.)",
        "background": "Grew up in orphanages around Columbia, put herself through the University of Missouri, three years at CommTech, barely ever out of town; rides with the Pretenders, the closest thing she has to a family, but never on anything illegal. Has always wondered about her parents, especially her father, without looking. Ehran arranged a childhood illness and, in hospital, had special metals woven into her thigh bone as a spell lock that hides her from lesser magicians and lets him trace her (never activated, for fear of leading Harlequin to her -- who already knew). Sylvan file 8-007's deleted Midwest block is hers.",
        "notes": "B3 Q5 S1 C6 I5 W6 E6 R5; Athletics 3, Bike 5, Car 4, Computer 3, Etiquette (Corporate) 3; no armor, no headware. Escaped Ehran's team by clobbering Victor with her best pot; wrote 'HELP GET PRETENDERS' on the bathroom mirror; hidden at the St. James Home. Ritual sorcery cannot find her (Magical Theory 8 hints at concealment). Sullen and silent once taken; climbs Southwind with an odd light in her eyes. Harlequin's ritual shatters the lock and her thigh (right thigh p.122, left p.128) -- Seriously Wounded, healed by Harlequin -- and he carries her off; a month later she is in Phoenix in the background of his holocard, talking to an old short Ork with a soccer ball.",
    },
    {
        "name": "Josh Rehndig",
        "role": "Cowboy-shirted senior software VP of CommTech who has never missed a deadline and is beside himself over his missing 'Janey'",
        "archetype": "Company Man",
        "title": "Senior Software Vice President, CommTech Inc.",
        "race": "Human",
        "gender": "Male",
        "organization": "CommTech Inc.",
        "connection": 3,
        "description": "A tall man in jeans, boots, cowboy shirt and string tie who bounds down the stairs -- 'Howdy, gentlemen. Name's Josh' -- and shakes every hand. Relaxed management style, a hit with peers and employees, but he has never missed a deadline or failed to take appropriate action; five remarkable years at CommTech, making the small firm's name in the UCAS market.",
        "background": "Hired Jane after his last secretary mysteriously vanished, and blames himself -- though she merely eloped to St. Louis with a member of that city's championship UrbanBrawl squad. Barely knows Janey but dreads something terrible has happened to her too.",
        "notes": "Company Man (SR p.164). Opposed Charisma vs his Intelligence, two questions per success: Jane's address (he is not sure where it is), that she likes music and frequents a club, that she runs with a rough bar or biker gang he cannot name, that nothing she handles (market research, sales figures) is worth stealing. Blames the gang. Asks to be called when they know something; a GM lifeline for stuck teams.",
        "contact_skills": ["CommTech and the Columbia software scene"],
    },
    {
        "name": "The Great Pretender",
        "role": "Tall bearded leader of the Pretenders go-gang whose word is law; a thinned-out combat mage with a secret crush on Frosty",
        "archetype": "Combat Mage (gang leader)",
        "title": "Leader of the Pretenders, Columbia, Missouri",
        "race": "Human",
        "gender": "Male",
        "organization": "The Pretenders",
        "connection": 2,
        "description": "A tall, bearded man in the gang's faded leather at the back bar of B.K.'s. 'So, you're the ones... Didn't find what you were looking for when you busted into her place the first time? Well, the Pretenders take care of their own, and Frosty's with us.' Then he lashes magic at the nearest runner and the gang piles in.",
        "notes": "Combat Mage (Sprawl Sites p.98) stripped to combat spells at half Force, no spell locks or foci; a Colt L36 in an ankle holster. Will do anything to help Frosty. Resisted Interrogation to make him talk once beaten.",
    },
    {
        "name": "Rico (Pretenders)",
        "role": "The Great Pretender's most trusted lieutenant, a street mage who strikes the moment her leader does",
        "archetype": "Street Mage",
        "title": "Lieutenant of the Pretenders",
        "race": "Human",
        "gender": "Female",
        "organization": "The Pretenders",
        "connection": 1,
        "description": "Has known the Great Pretender so long she suspects his feelings for Frosty; ready for his response when strangers ask questions, she strikes at the same instant he does.",
        "notes": "Street Mage (SR p.45) with an armor vest and a Walther Palm Pistol.",
    },
    {
        "name": "Sister Ann",
        "role": "Hardened criminal in her early forties playing a nun at the St. James Home; boss of the Flames; hides Frosty out of pity",
        "archetype": "Fixer (gang boss)",
        "title": "'Sister Ann', director of the St. James Home for Wayward Women; boss of the Flames",
        "race": "Human",
        "gender": "Female",
        "organization": "The Flames",
        "connection": 2,
        "description": "Sweat pants, a Columbia College tee-shirt and faded running shoes; the quiet strength of someone who has seen and done many things; early forties and the years have been kind -- she can still turn a man's head and often does. 'Good day. I am Sister Ann.' Then the scream: 'Beat it, Janey, they're here!' and a glare daring you to do something. Restless and nervous: playing a nun is not in character and the church will find her out sooner or later.",
        "background": "Took over the church-founded halfway house a couple of months ago under false pretenses and uses it as a base to pick skilled women returning from prison for robberies across the city. Does good works on the side.",
        "notes": "Fixer (SR p.167) without cyberware; a Browning High-Power hidden in the kitchen. Stays out of the fight unless the team enters the house; if threatened or captured the Flames surrender Jane and themselves for her release.",
        "contact_skills": ["Columbia's female ex-convict underworld", "Fencing in Columbia, Missouri"],
    },
    {
        "name": "Banger",
        "role": "Leader of Ehran's thrown-together retrieval team in Columbia -- intelligent, first command, botched it, now desperate enough for brute force",
        "archetype": "Former Company Man",
        "title": "Team leader, Ehran's guns (Columbia, Missouri)",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": "Intelligent, but this is his first command and he has made serious tactical errors; frustrated, he pushes the issue with the runners by sliding a Westwind 2000 to a stop against their vehicles and piling out shooting. Fights to the end and never runs, even alone.",
        "background": "Ehran threw the team together at the last moment because the chaos Harlequin caused left no experienced people free. Banger alone knows the connection: Ehran told him to find Jane Foster, grab her, and take her to a safe location Ehran would relay once she was found. That is all he knows.",
        "notes": "Former Company Man (SR p.37). Ambush triggers at four marks of unwanted attention (Quickness (6) for a free action as the car crests the hill). The team bunks at a small Nights Inn on the edge of town with a datachip dossier on Jane. Survivors may join Ehran's real goons at Althain.",
    },
    {
        "name": "Anastasia (Ana)",
        "role": "'Ana' -- Ehran's team mage who considers Banger a moron and the whole UCAS a backward pit of drek; fights with real fury",
        "archetype": "Street Mage",
        "title": "Mage, Ehran's guns (Columbia, Missouri)",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": "Has had just about enough of Banger and this whole mission; sees the runners as one more thing gone wrong and fights with real fury.",
        "notes": "Street Mage (SR p.45), Combat orientation plus Detect Enemies 3 and Chaos 4; armor vest with plates.",
    },
    {
        "name": "Victor Vee",
        "role": "Ehran's Ork muscle who only wants to fight the tougher the better; clobbered with Jane's best Navaho pot; mildly allergic to plastic",
        "archetype": "Ork Mercenary",
        "title": "Muscle, Ehran's guns (Columbia, Missouri)",
        "race": "Ork",
        "gender": "Male",
        "connection": 1,
        "description": "Lets the others argue and talk; all he wants is to fight, and he considers the runners potentially worthy opponents. Took Jane's most expensive pot across the head and bled on her carpet -- 'some poor dude's probably singing soprano right now.'",
        "notes": "Ork Mercenary (SR p.41) with a T-250 shotgun and a Ruger Super Warhawk instead of the AK-97; Mild Allergy to plastic.",
    },
    {
        "name": "Sunny",
        "role": "Hot-shot driver on her first shadowrun who let Frosty slip from her grasp and has been out of Banger's good graces since",
        "archetype": "Mechanic (driver)",
        "title": "Driver, Ehran's guns (Columbia, Missouri)",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": "A hot-shot driver and not good for much else; drives the Westwind 2000 into a four-wheel drift and crunches the runners' rentals into the curb. Her mistake let Frosty get away in the first place, and it shows.",
        "notes": "Mechanic (SR p.168) with Car 6, Firearms 2, Unarmed 2 replacing the B/R skills; armor jacket and Ares Slivergun. Jane's small hand smeared paint pushing through a canvas -- Sunny was the second attacker.",
    },
    # -- Present ----------------------------------------------------------------------------
    {
        "name": "Allaech",
        "role": "Phoenix-born physical adept commanding the Bratach Gheal detachment at Althain; bearer of the High Prince's Order; 'Why me?!'",
        "archetype": "Physical Adept",
        "title": "Squad leader, Bratach Gheal (White Banner), Tir Tairngire",
        "race": "Elf",
        "gender": "Male",
        "nationality": "Tir Tairngire (born Phoenix)",
        "organization": "Bratach Gheal (White Banner)",
        "connection": 3,
        "description": "Highest-ranking of the four and not pleased to carry the responsibility; observation and a smattering of experience have taught him how dangerous it is to insult Ehran and his ilk, so he takes whatever solution involves the fewest complications. Accustomed to the High Prince's 'modern Elvish society', he finds Althain intriguing, astounding and frightening. Talks first to the most respectable-looking Elf present, then any Metahuman, demanding to see Ehran.",
        "notes": "B4(8) S4 Q7 C5 I3 W6 M(8) E6 R5(8), armor 3/3; Armed Combat 5, Athletics 5, Car 3, Elvish 4, Etiquette (Tir Tairngire) 4, Firearms 5, Negotiation 3, Persuasion 4, Stealth 3, Unarmed 7; Physical Adept, Initiate grade 3, Increased Reaction 3, Increased Body +4; reinforced ballistic leathers, sword (4M2, +1 Reach). Delivers the Princely Order only to Ehran; after the duelists vanish, rants in Elvish and tries to take the runners to the High Prince as witnesses (reason or fight); Sruth talks him into leaving.",
    },
    {
        "name": "Aimsir",
        "role": "Bratach Gheal combat mage awed by Althain who believes Ehran will lead the Elves out of the underclass; orders to use Stun Blast freely",
        "archetype": "Combat Mage",
        "title": "Mage, Bratach Gheal (White Banner), Tir Tairngire",
        "race": "Elf",
        "gender": "Female",
        "nationality": "Tir Tairngire",
        "organization": "Bratach Gheal (White Banner)",
        "connection": 2,
        "description": "Met Ehran once while working security at a Tir social function; he will not remember and she will not care. Awed by Althain's wonders without the perception or knowledge to grasp their implications; dumbfounded when Ehran and Harlequin vanish by a magic no one she has ever met knows, and assenses the room to find nothing. With Taelech, the most willing to explore.",
        "notes": "B3 S3 Q6 C4 I6 W6 M(7) E6 R6(9), armor 3/3; Armed Combat 4, Athletics 3, Conjuring 4, Elvish 4, Etiquette (Tir Tairngire) 3, Firearms 2, Magical Theory 4, Gaelic (centering) 4, Sorcery 7, Unarmed 5; Initiate grade 2; Magic pool 14. Ares Light Fire (explosive), reinforced ballistic leathers, sword. Fire Elemental (Rating 4, 3 services); quickened Personal Combat Sense 4. Spells: Fire Cloud 4, Heal Moderate Wounds 5, Mana Missile 3, Personal Clairvoyance (Extended) 3, Physical Mask 3, Stun Missile 4, Stunblast 4.",
    },
    {
        "name": "Sruth",
        "role": "Ringer from Tir Tairngire's secret police planted in the Bratach Gheal; records everything with a cybereye video link; despises non-Elves and shadowrunners",
        "archetype": "Street Samurai (intelligence plant)",
        "title": "Guardsman, Bratach Gheal (White Banner); agent of the Tir secret police",
        "race": "Elf",
        "gender": "Male",
        "nationality": "Tir Tairngire",
        "organization": "Bratach Gheal (White Banner)",
        "connection": 3,
        "description": "Aloof from most of the proceedings and taking a dim view of Ehran and the goings-on at Althain even though he barely understands them; especially angry to see non-Elves present, let alone shadowrunners. Not a full Paladin -- planted in the White Banner to watch it and its members; being picked for this trip was sheer luck.",
        "notes": "B5 S5 Q7 C4 I4 W3 E3.48 R5, armor 3/3; Armed Combat 4, Car 2, Elvish 2, Etiquette (Tir Tairngire) 5, Etiquette (Tribal) 3, Firearms 4, Rotor 3, Unarmed 4. Alpha-clinic Boosted Reflexes 2, chipjack, cyberear, cybereye with video link, datajack, 70 Mp headware, Skillwire 3; Ares Crusader MP (APDS), Japanese/Spanish/Salish linguasofts (3), reinforced ballistic leathers, survival knife. What he sees and hears could damage or embarrass Ehran later; recommends withdrawal; if he lives, the runners' images go into a file.",
    },
    {
        "name": "Taelech",
        "role": "Dallas-born Bratach Gheal guardsman disillusioned with the 'Land of Promise' and suspicious of a hidden agenda in the Tir hierarchy, Ehran included",
        "archetype": "Street Samurai",
        "title": "Guardsman, Bratach Gheal (White Banner), Tir Tairngire",
        "race": "Elf",
        "gender": "Male",
        "nationality": "Tir Tairngire (born Dallas)",
        "organization": "Bratach Gheal (White Banner)",
        "connection": 2,
        "description": "At a critical juncture: unhappy but unsure what to do about it. As an Elven child in Dallas he imagined Tir Tairngire as the refuge and paradise for Elves; enough years there have shown him it is far from the Land of Promise. Troubled by what he perceives as a hidden agenda among certain members of the Tir hierarchy, Ehran the Scribe included; will carry the sights and implications of Althain back with him. Willing to explore.",
        "notes": "B6 S6(7) Q7(8) C3 I3 W4 E3 R5(7), armor 3/3; Armed Combat 7, Athletics 2, Cycle 2, Elvish 2, Etiquette (Tir Tairngire) 2, Firearms 6, Gunnery 3, Unarmed 3; Muscle Replacement 1, Wired Reflexes 1; combat axe (7S2, +2 Reach), Remington Room Sweeper (explosive), reinforced ballistic leathers. A possible future contact inside the Tir for runners who want the hidden agenda.",
    },
]

ORG_UPDATES = {
    "Dassurn Securities and Investments": {
        "notes_append": (
            "Harlequin (campaign #9; the row itself was created from the later Divided Assets, which "
            "calls it tier 3 with a Seattle home office): Harlequin's Loves target and 'a major "
            "international banking firm with a high profile in the Seattle business community' (Seattle "
            "Sourcebook ch.20). A Sylvan Information client whose Seattle branch office, LTG 3206 "
            "(52-7229), carries one of the YET back-door passcodes -- installed not in the CPU but in "
            "SPU-8 (Account Transaction Control). Audits all branch offices Monday mornings; fewer "
            "security deckers at weekends; on an external alert one Major League decker (Fuchi-6, "
            "Response 1, Attack 6, Shield 2, Mirrors 2, personas 5) investigates and shuts the system "
            "down if dumped. Johnson's program, run in the Liquidations SPU, mimics a legitimate "
            "cash-out with phantom retinal and cellular confirmations, turns into a Revenue Service "
            "confiscation routine, drains the branch reservoir, cash reserves and credit line and "
            "reaches for the home office before the umbilical is cut -- routing the take to a SIN "
            "account at LTG 5206 (19-1165), a Tacoma bank, that belongs to Ehran the Scribe. No street "
            "rumors to be had. Branch node map in the Harlequin prep doc's Matrix section."
        ),
    },
    "Tir Tairngire": {
        "notes_append": (
            "Harlequin: Ehran the Scribe is 'tied up in the politics of Tir Tairngire' and Harlequin's "
            "journal calls it 'that obscene nation-state' where Ehran's voice is heard clearly. The High "
            "Prince, with a history with Ehran, keeps out of the chal'han but sends spies and then four "
            "of his personal guard, the Bratach Gheal (White Banner) -- Allaech, Aimsir, Sruth, Taelech "
            "-- with diplomatic passes and a Princely Order for Ehran and 'this Harlequin' to appear "
            "before him; any hint of Elven dissent is leverage for national and corporate powers, and he "
            "already has the militant Tir na nOg to handle. The Tir has a 'secret police' whose elite are "
            "called Paladins (Sruth is a lesser plant). Ariel's coded wristphone reaches a Tir number, "
            "commcode 3503 (395-6985), one of Ehran's, self-destructing if any other number is dialed "
            "(Electronics B/R 8 with a microtronics kit to extract; a Matrix run into the Tir RTG to "
            "trace; erased 24 hours after the adventure). Lancelot Windtree vanishes back into the Tir. "
            "Taelech no longer believes in the Land of Promise."
        ),
        "allies_add": ["Bratach Gheal (White Banner)"],
    },
    "Salish-Shidhe Council": {
        "notes_append": (
            "Harlequin: Tarislar sits almost on the Seattle / S-S Council border. The Council runs daily "
            "sightseeing bus tours from Seattle to Mounts Rainier and Saint Helens (50 nuyen, about three "
            "hours, small carry-bags searched at the border, a one-day travel visa from the S-S Council "
            "Lodge on Council Island; four hours on site) and its Parks Department lights the lava "
            "caverns for tourists. Each border crossing from Seattle is a concrete-and-steel blockhouse "
            "of four Border Patrol officers (Former Tribal Warrior; two on the road, two backing with "
            "Colt M22a2s); crashers get two PRC-42b Wasps or Hughes Stallions after them (Car skill vs "
            "vehicle signature, pilots 4 dice). After Mount Saint Helens' third eruption, Council "
            "troopers and a unit of guardsmen try to seal the mountain, with survey helicopters and "
            "two-warrior-plus-scientist search parties on the slopes. Some Nations shoot down "
            "unidentified aircraft as smugglers."
        ),
    },
    "Renraku Computer Systems": {
        "notes_append": (
            "Harlequin: the Association Para-Nobilis' headquarters, an old city fire garage near Post and "
            "University, lies in the one patch of downtown the Arcology's light-routing system leaves in "
            "shadow -- 'an apparent design flaw'; the display lights keep it lit all evening and the "
            "darkest hour is just after dawn. A noisy raid risks bringing 'the Renraku Reds' down on the "
            "runners' heads."
        ),
    },
    "Shiawase Corporation": {
        "notes_append": (
            "Harlequin: Shiawase won the contract to administer Seattle's Department of Public Works. Its "
            "staff lecture armed visitors and deny holding plans for non-current city structures; the "
            "originals live in the Archive Hall, an old nuclear shelter 14 flights below the building, "
            "run for 47 years by 88-year-old Harriet Taylor, whom Shiawase tried to fire and could not "
            "do without."
        ),
    },
    "Lone Star Security": {
        "notes_append": (
            "Harlequin: PANICBUTTONs at Sylvan Information (Bellevue) bring a carload of heavily armed "
            "officers in three minutes, at least three cars of two if a raid goes haywire; a failed team "
            "wakes in a Lone Star holding cell and is questioned for a couple of weeks before release. "
            "Lone Star responds to alarms or heavy weapons at the APN headquarters in 2D6 minutes, "
            "investigating both the APN and anyone caught on the premises, and Erendahl of the APN joined "
            "'to mock Lone Star'. Half a dozen officers answer the Tacoma Style's button. The heavily "
            "armored, combat-scarred van from the Grantleigh Park fracas turned up in a field in the "
            "northern Sprawl with traces of knock-out gas -- then the Feds clamped a UCAS security rating "
            "on the case because it is CIA-issue. Iggy Halloran's prized toy is a Bandai-US model of a "
            "Lone Star Patrol-1 with working siren and lights."
        ),
    },
    "Knight Errant Security Services": {
        "notes_append": (
            "Harlequin: two Knight Errant guards share the huge old reception desk of Laubenstein Plaza "
            "(Sixth and Pike) with the night clerk; they do nothing about the four Ork thugs J.P. Morlock "
            "posts at Elevator Three."
        ),
    },
    "Seoulpa Rings": {
        "notes_append": (
            "Harlequin: Walturr, an ex-runner barkeep, 'used to do some shadowrunning himself before the "
            "Seoul Men had him hardwired to the counter' (p.35). The book does not say whether the "
            "'Seoul Men' are a Seoulpa ring; recorded here as a probable reference."
        ),
    },
    "Yakuza (Watada-rengo)": {
        "notes_append": (
            "Harlequin: the torturer Doctor What 'buys his personal protection from a powerful Yakuza "
            "gang' -- unnamed in the book, so not necessarily the Watada-rengo; getting to him will not "
            "be easy. Sandii's stainless-steel razor teeth are rumored to be a 'gift' from a dissatisfied "
            "oyabun with no tolerance for failure."
        ),
    },
    "Tir na nOg": {
        "notes_append": (
            "Harlequin: the High Prince of Tir Tairngire 'has already enough problems dealing with the "
            "demands of the militant Tir na nOg side of the British Isles' -- one reason he wants the "
            "Ehran / Harlequin feud kept from outside eyes."
        ),
    },
    "Humanis Policlub": {
        "notes_append": (
            "Harlequin: 'The Humanis Threat' is a standing lecture topic at the Association Para-Nobilis' "
            "Thursday meetings; the Elf-poser policlub sees Humanis as the enemy while murdering Elves "
            "itself."
        ),
    },
}

LOC_UPDATES = {
    "Seattle-Tacoma Airport (Sea-Tac)": {
        "notes_append": (
            "Harlequin: 'Seattle is the Hong Kong of the 21st century' and Sea-Tac handles a drekload of "
            "traffic, suits and bodyguards to street trash escaping the rain. Weapon detectors under a "
            "trio of rent-a-cops at the doors (no heat without a license and a very good reason); "
            "tighter at the gates, where at Gate 12 a gray suit in a mirrored visor frisks Anson Helm's "
            "guests and drives them 30 m across the tarmac to his Lear Platinum Custom. Private gates "
            "let Helm's clients be escorted around security. Getting There By Air (pp.144-146): Detekt-It "
            "wands (Alpha-Gamma, rating 1-4) and Gateway stations (I-IV), cybersystem restraint cuffs "
            "for Class CB cyberware (Taser 4D4 Stun, three shocks), checked-only weapons, permits for "
            "Class E pistols, sub-orbital fares 1,600 coach / 4,000 first. Departure point for Future's "
            "12:05 Delta to Kansas City; Mr. Johnson's Nightsky full of muscle meets the returning Lear "
            "here with Jane Foster."
        ),
    },
    "Renraku Arcology (SCIRE)": {
        "notes_append": (
            "Harlequin: the Arcology's light-routing system bounces what sun Seattle has into its inner "
            "parks and residence levels and across to the downtown blocks that would sit in its shadow; "
            "the APN's old fire-garage headquarters near Post and University is in the one shadow it "
            "leaves. Its display lights keep the area lit all evening."
        ),
    },
    "Tarislar": {
        "notes_append": (
            "Harlequin: 'They say it means remembrance in Elvish, but remembrance of what?' Ever since "
            "the Night of Rage these abandoned buildings along the southern edge of the Puyallup "
            "Barrens, a short distance from the Salish-Shidhe border, have been a refuge for "
            "Metahumans, Elves especially, with nowhere else to go -- a cruel reminder of the sanctuary "
            "once promised and then denied by politics and prejudice. Black and gray ash from the 2017 "
            "eruptions is everywhere; a filter mask (20 nuyen, two weeks) or cyber air filter is nearly "
            "essential (3M2 Stun every ten minutes without). Silent figures in dark clothing and plastic "
            "filter masks line the streets at dawn on their way to the soup kitchens. A year ago "
            "Harlequin took the top floor of the center tower of the ruined Southwind office complex; "
            "the gangs and dealers fled 'the Laughing Man' and the grateful locals steer clear of the "
            "buildings. Seattle Sourcebook pp.136-143 and the map on pp.174-175."
        ),
    },
    "Club Penumbra": {
        "notes_append": (
            "Harlequin: the runners' favorite table is where the fixer Sandii finds them on a Thursday "
            "night with 250 nuyen each and an invitation to a Young Elven Technologists party in "
            "Puyallup, and where she takes delivery of the back-door passcodes afterward for 40,000 "
            "each. The music is deafening enough that '...in Puyallup' almost goes unheard."
        ),
    },
    "Underworld 93": {
        "notes_append": (
            "Harlequin: at the YET party a party-goer offers 'a bootleg chip of the time she played "
            "Underground 93' (the book's spelling) -- Mercurial's set here is circulating on the "
            "Barrens bootleg market."
        ),
    },
    "The Barrens (Seattle)": {
        "notes_append": (
            "Harlequin: Puyallup 'always has a cloud over it, be it smog, ash, or despair' -- thirty-five "
            "years ago it was a suburb, until the Ghost Dancers blew the volcanoes and ash buried homes, "
            "people and dreams; the well-marked roads still kick up dust like a desert. The Young Elven "
            "Technologists keep their hall in a pre-Awakening fire station (Fire Station 118) on the "
            "squalid outskirts where even the family dog may be on the menu, and rarely see trouble; "
            "Tarislar and the Southwind ruins lie on the southern edge by the S-S border. Both Elven "
            "policlubs know Puyallup's streets the way runners know the shadows."
        ),
    },
    "Aztechnology Pyramid": {
        "notes_append": (
            "Harlequin: Sceptre Productions' four-person video crew, assigned to watch the Association "
            "Para-Nobilis, was lost 'near the Aztechnology pyramid' five months before Hates; the bodies "
            "turned up buried in a meter of ceracrete after a bloodbath in an Elf-owned computer club, "
            "found by DocWagon through a still-working wristphone."
        ),
    },
}

NPC_UPDATES = {
    "Maria Mercurial": {
        "notes_append": (
            "Harlequin: at a Young Elven Technologists recruiting party in Puyallup a party-goer offers "
            "'a bootleg chip of the time she played Underground 93' (Underworld 93) -- her live set there is on the "
            "bootleg circuit (overheard-conversation table, p.56)."
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
None of these are built as entities; every node the book maps is listed here so they can be
constructed in the Matrix designer later.

**1. Sylvan Information Systems** (map p.17; Physical). SAN 9206 (24-1209). From outside a plain
multi-hued UMS geometric form; inside, a sculpted primeval forest -- files are trees with data on the
leaves, SPUs are hexagonal stone towers guarded by knights, I/O ports are cottages (crystal balls),
SANs are drawbridges over data streams full of fish, the CPU a castle. Authorized users wear Elven
personas. IC as beasts: Blaster = 1D4+1 coyotes (howl after subduing), Killer = 1D3 wolverines, Trace =
a fox that darts into the woods, Black IC = a humanoid black dragon that casts fireballs. Bears and
sasquatches are harmless flavor. Sony-Cray 10000 mainframe; 30 jack-in points inside the building.

| Node | Function | Rating / IC |
|---|---|---|
| SAN | Drawbridge; the only outside door | Red-8, Barrier 6, Blaster 5, Trace and Report 6 |
| SPU-1 | Security processor; Elven knight (Access) with a sleeping fox at his feet; stairs to pools and crystals of the security controls | Red-5, Access 5, Killer 4, Trace and Report 5 |
| DS-1 | Medieval library: time records and personnel files (irrelevant) | Green-5, Scramble 5 |
| I/O-1 | Crystal ball; the security-office terminal | Orange-5, Access 1 |
| SN-1 | Reflecting pool; internal and external cameras (display in the security center) | Green-5 |
| SPU-2 | Building-systems processor; unguarded tower on pristine grounds | Green-5, Access 1 |
| DS-2 | Library: parts requisitions, maintenance schedules | Green-5 |
| I/O-2 | Crystal ball; building-maintenance office terminal for the slave nodes | Green-5 |
| SN-2 | Abacus; elevators | Green-5 |
| SN-3 | Locks and keys; exterior and interior locks | Green-5 |
| SN-4 | Unlit brazier; heat sensors and fire systems | Green-5 |
| SN-5 | 'DiVinci' contraption; heating and A/C | Green-5 |
| SPU-3 | Editorial processor; a scribe at a desk of access ledgers | Green-5, Access 2, Killer 3 |
| DS-3 to DS-11 | Library rooms open to all editors: 3 Music, 4 Simsense, 5 Dynabooks, 6 Graphic Publications, 7 Administrative, 8 Personnel, 9 Artists, 10 Restricted, 11 Miscellaneous | Green-5, Scramble 4 |
| I/O 3-26 | 24 junior-editor cubicle terminals, first floor | Green-5 |
| I/O 27-32 | Executive terminals: 27 Fujiwara, 28 Green, 29 Fathom, 30 Gylgalad, 31 Sum, 32 Morgan | Green-5 |
| CPU-1 | Castle with Elven knights in silver on the path and the black dragon on the ramparts; entering dispatches a fox | Red-8, Access 5, Black IC 6, Trace and Report 6 |

Files of note: 6-001 to 6-006 (Personnel) on Morgan, Sum, Gylgalad, Fathom, Green, Fujiwara, each
linked to the safe combinations 9-201 to 9-206 (Miscellaneous; 9-205 is Green's, 5L 8R 18L). 8-007
(Restricted, 240 Mp): genealogical and biomedical surveillance on dozens of families since 1834, each
block ending 'Surveillance Terminated' at a serious illness or the subject's late thirties (Perception
10); one block deleted -- Computer (12): 1 success, a normal deletion from the Midwest regional subset;
2, a female in her late twenties; 3, the block was echoed elsewhere in the system; 4+, deleted but never
closed. The virus: 20 Mp, two turns to decompress, a bunny that burrows into the forest floor; a day
later a Renaissance rapier on every terminal and every copy of Mankind Revealed erased; copied, it
activates in six days and eats 10 Mp per hour. Karma 1 (unexplained) for taking the genealogy file.

**2. Munchmaussen Town Hall and Schloss Munchmaussen** (map p.45; Past). Three SANs on one system;
all Bavarian RTGs are Green-3. 'Archaic' but heavily iced at the top.

| Node | Function | Rating / IC |
|---|---|---|
| SAN-1 | Unlisted number for Munchmaussen Town Hall | Orange-4, Access 5 |
| SPU-1 | Data routing, town government | Orange-6 |
| SPU-2 | Town security | Orange-5, Access 8 |
| I/O-1 to 3 | Concealed cameras in the larger rooms of hotels and influential citizens' homes | Orange-5 |
| I/O-4 to 6 | Concealed cameras in shops, streets, the youth hostel | Green-3 |
| SPU-3 | Public Control Office (Town Hall) | Orange-6, Access 4 |
| I/O-7 | Terminals | Green-4 |
| DS-1 to 6 | Dossiers on every citizen, current and past investigations, public records | Green-7 |
| SAN-2 | Unlisted number for the castle | Orange-8, Access 4 |
| SPU-4 | Data routing, castle | Red-5, Tar Baby 4 |
| SPU-5 | Government bureaucracy | Green-4, Trace 6 |
| I/O-8 | Terminals | Orange-4 |
| DS-7 to 13 | Governmental records | Red-9 |
| SPU-6 | Senior bureaucracy | Orange-4, Blaster 6 |
| I/O-9 | Terminals | Orange-5 |
| DS-14 to 17 | Financial accounts of the barony | Orange-7 |
| DS-18 to 20 | Personnel records, including 'secret' personnel such as Goldi Schonbosom | Orange-6 |
| SPU-7 | Environmental control | Green-7 |
| SM-1 | Electricity | Green-7, Black IC 4 |
| SM-2 | Heating / air conditioning | Orange-5 |
| SM-3 | Skylift machinery (the way to ride the tram in) | Green-6 |
| SPU-8 | Castle security | Orange-8, Access 8 |
| I/O-10 | Security cameras concealed throughout the castle | Red-7, Access 1 |
| SM-4 | Camera movement and focus | Orange-7, Barrier 10 |
| SM-5 | Maglocks on doors and elevators | Green-5 |
| SAN-3 | Second unlisted castle number known only to the baron and his closest associates | Red-5, Black IC 4 |
| SPU-9 | Data routing for the baron | Orange-8, Trapped IC (Blaster 5 disguised as Access 3) |
| CPU | Central processor | Red-11, Killer 2 |
| SPU-10 | The baron's personal subprocessor | Red-6, Black IC 5 |
| I/O-11 | Security cameras, castle and town | Orange-6 |
| I/O-12 | Terminal in the inner library | Orange-6 |
| DS-21 | The baron's private records | Orange-6 |
| SM-6 | Master override, maglocks on doors and elevators | Red-6, Access 5 |
| SM-7 | Master override, castle cameras | Orange-5 |
| SM-8 | Master override, electricity | Red-7, Tar Pit 3 |

**3. Young Elven Technologists hall** (map pp.63-64; Loves). Not sophisticated but well protected;
'its IC has geeked more than a few brash deckers'. On an external alert one Elven Decker (SR p.36 with
the Opposition equipment p.116) investigates; five minutes or one alert later, two more; keep doubling.
On the second round four YET Muscle close on the decker's real-world location in 1D6 minutes.

| Node | Function | Rating / IC |
|---|---|---|
| SAN-0 | LTG 4206 (47-2551), unlisted private line | Orange-3, Access 3, Trace and Dump 3 |
| SAN-1 | LTG 4206 (47-1378), unlisted line in Ehran's private suite | Orange-4, Access 4, Trace and Burn 3 |
| CPU-1 | Central processor (glass box in the computer room) | Red-3, Barrier 5, Trace and Burn 4 |
| SPU-1 | Data routing | Orange-3, Access 3 |
| DS-1 | E-mail | Orange-3, Access 3 |
| DS-2 | Administrative e-mail; Ehran's file also under Scramble 4 | Orange-3, Access 4, Trace and Report 3 |
| DS-3 | Routing records | Orange-3, Scramble 4 |
| I/OP-1 | Telephones, ground and upper floors | Green-3, Access 3 |
| I/OP-2 | Telephones, basement | Orange-3, Access 4, Trace and Report 3 |
| SPU-2 | Administration | Orange-5, Barrier 4, Blaster 4 |
| DS-4 | General | Orange-3, Scramble 4 |
| DS-5 | Personnel: dossiers on every active member, including two dozen employed by Sylvan | Orange-3, Scramble 4 |
| DS-6 | Restricted: Sylvan's client list with LTGs and software purchased (10 Mp) -- cross-reference with DS-13 to match passcodes to purchasers | Red-3, Scramble 4, Black IC 3 |
| I/OP-3 | Administration-office terminals | Orange-3, Access 4, Trace and Dump 4 |
| I/OP-4 | Terminal in Ehran's suite | Orange-3, Access 5, Trace and Dump 4 |
| SPU-3 | Research and Development | Red-3, Access 4, Tar Pit 3 |
| DS-7 | General records | Orange-3, Scramble 4 |
| DS-8 | Project records: financial software and incomplete security programs (32 files at 60 Mp, worthless) | Orange-4, Scramble 4, Trace and Burn 4 |
| I/OP-5 | Computer-room terminals | Orange-3, Access 4, Trace and Dump 4 |
| SPU-4 | Secondary programming | Red-3, Barrier 5, Black IC 3 |
| DS-9 | Archive: financial programs, no back-door source | Red-3, Barrier 4, Trace and Burn 4 |
| DS-10 | Back-ups | Red-3, Barrier 4, Trace and Burn 4 |
| SPU-5 | Security | Red-3, Barrier 5, Trace and Burn 4 |
| DS-11 | General records | Orange-3, Scramble 4, Killer 4 |
| DS-12 | Access log; where Trace reports are registered | Orange-3, Barrier 4, Killer 4 |
| I/OP-6 | Main Security terminal | Orange-3, Access 4, Killer 4 |
| SM-1 | Cameras | Orange-4, Access 4, Blaster 4 |
| SM-2 | Alarms (including the suite's PANICBUTTON) | Orange-4, Access 4, Trace and Report 4 |
| SM-3 | Exterior door maglocks | Orange-4, Access 4, Blaster 4 |
| SM-4 | Interior door maglocks (armory, offices, double doors) | Orange-4, Access 4, Blaster 4 |
| SPU-6 | Ehran's system | Red-3, Barrier 5, Trace and Dump 4 |
| I/OP-7 | Second terminal in Ehran's suite | Orange-4, Access 5 |
| DS-13 | Ehran's portable datastore: the six back-door utilities (40 Mp each) | Blue-6, Trace and Dump 4 |
| DS-14 | General | Orange-3, Scramble 4 |
| DS-15 | Personal: Ehran's calendar, drafts of speeches, books, articles (10 files at 30 Mp) | Orange-3, Barrier 5 |
| DS-16 | Restricted: Ehran's intentions for the YET, oblique references to Sylvan | Red-3, Scramble 4, Black IC 3 |

**4. Dassurn Securities and Investments, Seattle branch** (map p.66; Loves). CPU and further SPUs are
beyond the branch and left to the GM. The correct back door opens SPU-8 without alarms; a wrong one
punches into a random SPU (1D6) with its IC gone but the system on External Alert; without one, the
hard way. External alert: one Major League decker (Decker p.34; Fuchi-6, Response Increase 1, Attack 6,
Shield 2, Mirrors 2, personas 5), fewer staff at weekends; shuts the system down if dumped. Johnson's
program takes three turns in the Liquidations SPU. The money goes to LTG 5206 (19-1165), a Tacoma bank,
SIN account of Ehran the Scribe (a dangerous run into the customer database to learn this).

| Node | Function | Rating / IC |
|---|---|---|
| SAN-0 | LTG 3206 (52-7229), listed | Orange-3, Barrier 3 |
| SAN-1 | Direct link to the Mercantile Exchange(s) | Red-3, Access 3, Black IC 3 |
| SAN-2 | Link to Dassurn's main system only | Green-6 |
| SPU-1 | Customer Service | Orange-4, Access 5, Trace and Dump 4 |
| I/OP-1 | Terminals | Orange-3, Access 3 |
| SPU-2 | Customer Information | Orange-4, Access 5, Blaster 4 |
| DS-1 | General data | Orange-4, Scramble 4 |
| SPU-3 | Secondary Customer Information | Orange-4, Barrier 5, Trace and Dump 4 |
| DS-2 | Archive files | Orange-3, Access 4, Tar Pit 4 |
| DS-3 | Back-up files | Orange-3, Access 3, Tar Pit 3 |
| I/OP-2 | Terminal | Orange-4, Access 5 |
| SPU-4 | Liquidations -- run Johnson's program here | Red-4, Barrier 4, Killer 4 |
| DS-4 | General files | Red-3, Scramble 4 |
| I/OP-3 | Terminals | Orange-4, Access 3 |
| SPU-5 | Exchanges | Orange-4, Barrier 3 |
| DS-5 | General files | Orange-4, Scramble 4 |
| I/OP-4 | Terminals | Orange-3, Access 3 |
| SPU-6 | Transfers | Orange-4, Barrier 3 |
| DS-6 | General files | Orange-4, Scramble 4 |
| I/OP-5 | Terminals | Orange-3, Access 3 |
| SPU-7 | Purchases | Orange-4, Barrier 3, Trace and Dump 4 |
| DS-7 | General files | Orange-4, Scramble 4 |
| I/OP-6 | Terminals | Orange-3, Access 3 |
| SPU-8 | Account Transaction Control -- where the back door lands | Red-3, Access 3, Tar Pit 4 |
| DS-8 | General files | Red-3, Barrier 3 |
| I/OP-7 | Terminals | Orange-4, Access 3 |
| SPU-9 | Data routing | Orange-4, Access 5, Trace and Report 4 |
| SPU-10 | Accounting | Red-4, Barrier 3, Trace and Burn 4 |
| DS-9 | General files | Red-3, Scramble 4 |
| I/OP-8 | Terminals | Orange-4, Access 3 |

**5. Unmapped systems mentioned**: the Luftlande Skyclimber's flight computer (Hildi jacks in to kill
the restraint bracelets); the Tacoma bank at LTG 5206 (19-1165) holding Ehran's SIN account; the Tir
Tairngire RTG (tracing commcode 3503 (395-6985)); NatVat's company network (the pretext passcodes);
Columbia, Missouri's 'especially secure' grid; the CIA safe-house console (not on the Matrix: air seal,
alarms, armory and cell locks, elevator power, extinguishers, IR, lights, three vidscreens); the
Fonte do Sul hangar radar and shortwave to Eirunepe. Improvise if a decker goes looking.
"""

NOT_BUILT = """
- **Andre and Emile, Monsieur R. of the university, Mlle. M.** -- the prologue letter describing the
  original duel (Ehran severs Harlequin's left ear on a stone bridge at dawn); on the two principals.
- **Morlock's four Ork thugs**, **Sylvan's receptionists, guards, caretaker/kennelmaster and four
  barghests** -- on the Sylvan rows. **'Tower 801'** -- editing slip, on Laubenstein Plaza.
- **Takuri's headwaiter**, **the APN's Uzi guard outside Fierelle's door**, the **'Elven sage Xeric'**
  of the bronzed quill, **the surgical unicorn**, **Aunt Sara's Baked Brownies**, the **YET samurai who
  pulled the plans**, the **Elf-owned computer club** where Sceptre's crew died -- on the APN / Hates rows.
- **Walturr's three musclemen**, **the French elven Ms. Johnson** ('Ms....er....Mr. Johnson', two goons,
  French interests, knows everything afterward), **Klaus, Fritz and Mikki** of the EUD, **the Eskimo
  shaman in sealskins**, **the three elderly Japanese Former Company Men**, **the Luftlande Sky
  Marshal**, **the frazzled mother and her Awakened Ork boy**, **the brigand baron's soldiers and the Ork
  'liberators' in the Krupp Komet**, **Graf Eisenstein**, **the Munchmaussen youth-hostel staff, tram
  cops, castle guards and Volksedanz** -- on the Past org and location rows.
- **The YET recruiter, doorman, three Troll samurai, Elven poser bruisers and hitmen, Ehran's advance
  Bodyguard and Combat Mage**, **the 'Lee Gorbin' Mr. Johnson (Will 7, Negotiation 7)**, **the mini-mono
  musician**, **the Mercantile Exchange** -- on the YET / Dassurn rows.
- **Ehran's legitimate Mr. Johnson** for the NatVat extraction (any trusted Johnson), **NatVat's security
  director, plainclothes, heavy squads, Patrol-1 drivers and Yellowjacket pilot**, **Bonecrack's
  mercenaries**, **the government spook**, **the Samuvani Criscraft Otter** -- on the Counterstroke rows.
- **The IL-290 rigger with silver eyes**, **the Portuguese tanker crew**, **the Esperanca's two crewmen**,
  **the Amahuaca chief and Snake shaman, the Jivaro shaman and his Storm Spirit**, **Fonte do Sul's
  gardener, staff, six mercs and rigger, the greenhouse barghest**, **the Aquilar family** (Ehran's
  cover), **Manaus, Macapa, Eirunepe, Lima** -- on the Spiritual rows.
- **The Tacoma Style's maitre d' and twelve waiters**, **the Future Mr. Johnson** (Mr. Johnson p.170,
  armor jacket, Fichetti Security 500; meets the Lear with a Nightsky of muscle), **the CommTech
  receptionist**, **B.K.'s bartender, doormen and bouncers**, **the two women Pretenders at St.
  James**, **the nine Flames**, **the Nights Inn**, **the rental clerk and the Lear's ground girl**,
  **Calloway County Nuclear Power Corporation (Fulton)**, **the Mizzou Tigers, Black and Gold Bengals,
  Farrow Field, Hearnes Center, Columbia College, Stephans College, CATS** -- on the Columbia rows.
- **The blind Elf in white** at Southwind, **the munchkin stewards Emerald, Ash, Turquoise and Maroon**
  and their dozen colleagues (Cleaner, Junior Cleaner, First Cook, Chambermaid, Librarian), **the
  Embracer**, **the vivisected wyvern and the young Western Dragon**, **the fake Ehran corpse**, **the
  High Prince of Tir Tairngire**, **the Tir 'Paladins'**, **Ehran's real goons** at Althain, **the old
  short Ork with a soccer ball** in Phoenix -- on the Present rows.
- **The reclusive weapons collector** (a wiz VR programmer for UCAS Data Systems in their Denver
  compound) who might buy Harlequin's 16th-century rapier -- a hook, not a row.
- **'Harlequin' the psycho-chummer** who wasted himself summoning an Elemental (SR p.87) -- a different
  man; street legwork confuses them. **The Halloweeners** joke on p.144.
- **Getting There By Air** (pp.144-146: airline Enforcement Ratings, CRC taser cuffs, Detekt-It and
  Gateway scanners, fares, private-carrier multipliers) -- rules, kept in the book.
"""

PLAY_NOTES = """
- Eight mini-adventures by eight authors, meant to be spread through a campaign with unrelated runs
  between them; the players should notice the pattern after one or two. Nothing is revealed until
  Present, and even then 'truths, half-truths, and outright lies'. Neither Ehran nor Harlequin has
  stats: they win any confrontation, and the players should feel it.
- The chain of tokens: manuscript -> its title page (Xeric's lap) -> six ear-tips (the valise left at
  the schloss) -> the tome's frontispiece (Ehran's suite, wax seal with a jester) -> a chip fragment of
  the YET back door (the greenhouse) -> the orchid (Jane's flat) -> Jane. Each Johnson knows 'through
  mysterious channels' exactly what happened.
- Physical wants finesse: praise the team's rep, then make it a liability; Morlock's Orks are a test.
  The genealogy file is the seed of Future -- award the Karma point without saying why.
- Hates is a wetwork raid on posers; give the players the sympathetic exits (Maria, Fierelle) and the
  Tarrow crew's private joke. Kerry's townhouse fight is Erendahl's scouting mission.
- Past is tongue-in-cheek: zero-g brawl, a putsch, lederhosen and cybertractors, a Troll baron who
  wants to be assassinated a little. Penalize the opposition's Initiative if it is too strong.
- Loves: reconnoiter the hall during the party (every encounter on pp.56-57), run it by Friday, and
  time the Dassurn deck to the APN's wall-breach so both Elven groups end up chasing the team.
- Counterstroke: the NatVat trap must not be survivable by force; most shots miss until the van
  arrives. Naked prisoners, hourly torture, Iggy's toy car -- play the Hallorans for pathos and let
  compassion pay off. Sealing the complex's air removes Ariel for a month. Free teammates get the
  CIA hint after a day.
- Spiritual is travelogue and jungle horror: sell Helm's professionalism, make the Jivaros bluff, and
  spring the Stallion and the Storm Spirit on a team that thinks it is home free.
- Future: track 'marks' (CommTech 1, bar fight 1, learning of St. James 1) -- four bring Banger's
  Westwind. Columbia fights are fists and blades; guns bring police. A balking team gets a 150,000
  nuyen bounty or wakes up in the Cessna.
- Present is theatre until Althain; then let them explore everything before Harlequin walks in, keep
  the dragon in reserve to defuse the standoff with the Tir Elves, and use Ariel to end the scene.
- Karma: Physical 3/2/1; Hates 1 envelope, 1 per three ear-tips, 1 girl, 1 Fierelle, -2; Past 1/1/-2/1;
  Loves 1/1/-2/1/2/-1/1/1; Counterstroke 3-5; Spiritual 1/3/1; Present a blanket 8 plus 1 per segment.
  Final pay: the rapier (base 100,000 nuyen; fencing it is its own adventure).
- Loose ends: Bonecrack and Iggy (allies or a lethal enemy), Doctor What behind Yakuza protection,
  Taelech's doubts about the Tir, Sruth's file, a Sylvan client list and a working back-door chip, an
  orchid, a hundred-thousand-nuyen sword, a Free Air Elemental who wants her name back, and a holocard
  from Phoenix. Harlequin's Back (FASA 7320) picks the thread up.
"""
