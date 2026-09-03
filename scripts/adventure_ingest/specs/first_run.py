# First Run (FASA 7115, 1999, SR3) -- campaign order #33. An anthology of three self-contained
# introductory scenarios: Food Fight (Seattle, a Stuffer Shack), Supernova (Seattle/Auburn/Bellevue/
# Downtown, corporate espionage), and Site of Desecration (the Cascades, Salish-Shidhe territory).
# Dating: only Supernova states a year outright -- "The year is 2061" (Background Story). Food Fight
# and Site of Desecration are undated in the text; both are treated as the same year as Supernova
# since nothing in the anthology suggests otherwise.
# Food Fight is an SR3 reprint of the classic scenario from the Shadowrun 1st Edition core rulebook,
# already ingested as its own adventure (food_fight.py, campaign order #2, 2050). Per "earlier books
# are canon," this spec does not recreate the Chiller Thrillers, the Stuffer Shack staff/customers,
# or the store itself -- it only appends First Run's SR3-era variations to those existing rows.
# Notable variation: the gang member named "Wendy" in the 2050 printing is renamed "Zany" here, with
# the same role (the gang's "chick," Wiley's jealous obsession) -- flagged as a discrepancy on Wendy's
# row rather than treated as a new character. First Run also drops the 2050 printing's "equalizer,"
# Sally Tsung, entirely; no update needed on her row, just noted here for the record. Mrs. Needles,
# Louis Needles and Timmy Thinners reappear with slightly more color but were already judged
# NOT_BUILT bystanders in the 2050 spec; this spec follows that precedent rather than re-litigating it.
# Supernova's Richard Villiers, Miles Lanier and Novatech, Inc. are also pre-existing (created in
# blood_in_the_boardroom.py, campaign order #32, which dates Novatech's founding to 6 October 2059);
# Supernova's 2061 setting is consistent with that timeline, roughly two years later. Club Penumbra
# (the Supernova meet site) and Cascade Ork (whose claimed land, the Tooth, hosts Site of Desecration)
# are likewise pre-existing and are only updated here.
# OCR note: every printed attribute-row header ("B Q S C I W E M R") is garbled or missing spaces
# throughout the book; this is a cosmetic scan artifact, not a canon inconsistency, and is not
# reproduced in the notes below.
# Source text: docs/Adventures/text/SR1-first-run.txt (66 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "First Run"
ORDER = 33
SOURCE = "SR1-first-run.pdf, pp. 3-64"
YEAR = "2061"

SYNOPSIS = """
First Run collects three stand-alone scenarios meant to teach new players and gamemasters the game,
each with its own cast and none dependent on the others.

**Food Fight** is a shoot-out pure and simple: the team stops for munchies at a 24-hour **Stuffer
Shack** just as the thrill-gang **Chiller Thrillers** robs it, smashing the PANICBUTTON box and
terrorizing the clerk, the manager and a handful of ordinary shoppers before the gunfire starts. This
is an SR3-era reprint of the classic Shadowrun 1st Edition scenario of the same name (already covered
by this campaign's earlier Food Fight spec); the cast and location are the same store, the same gang,
mostly the same people under mostly the same names.

**Supernova** sends the team to **Club Penumbra** to meet **Nigel Terwilliger**, a panicky first-time
Mr. Johnson who is actually a Novatech cleanup specialist secretly also selling to **Renraku Computer
Systems**. Nigel hires the runners to break into **TekLon Electronics**, a small Auburn microtronics
firm both megacorps are fighting over in the wreckage of Fuchi's collapse, and lift an unfinished
cybernetic head prototype from its Alpha Wing lab -- timed, unknown to the runners, to land in the
middle of a Renraku raid on the same facility. The extraction is clean, but the payoff isn't: Nigel's
Novatech colleague **Elizabeth Chavez**, who caught him embezzling files for Renraku, has grabbed the
wrong case and dies in a Bellevue ambush by Renraku's elite **Red Samurai** and a fully armed
cyberzombie before the team can complete the swap. The runners recover both cases and Chavez's
datapad, which leads them to **Richard Villiers** and **Miles Lanier** at Novatech's Seattle
penthouse, where Nigel's double game gets him shot and the runners are asked to cover the corp's
escape from a Renraku ambush in the parking garage.

**Site of Desecration** takes the team out of the sprawl entirely. The talismonger **Daisy Quallon**
hires them to meet a smuggling crew, **the Pentagon**, in Cascade Ork territory and carry home a
shipment of magical telesma. The Pentagon has already been ambushed and robbed by the **Tooth
Warriors**, a new gang formed by the troll **Kaztok** around a crashed smuggler rotorcraft -- and
around **the Old One**, a free-willed man-of-the-woods spirit that Kaztok believes he controls. The
runners negotiate, fight and bluff their way through Kaztok's camp, the **Site of Desecration** itself,
only to discover in the end that the Old One was using Kaztok the whole time, and that the real test
was always aimed at them.
"""

TIMELINE = """
**Food Fight** -- a single rainy night; no date given (see food_fight.py for the established date of
2050).

**Supernova**, 2061, one evening into the small hours:
- Evening -- the meet with Nigel Terwilliger at Club Penumbra; the runners take the job.
- Same night -- the Auburn access tunnel and the (unopposed) extraction from TekLon's Alpha Wing,
  overlapping Renraku's raid on the rest of the facility.
- Just after midnight -- downtime at a safehouse or on the road while Nigel arranges the exchange.
- 2 a.m. -- the ambush at 100th and Main, Bellevue: Elizabeth Chavez dies, Red Samurai and the
  cyberzombie attack.
- Shortly after -- 3844 Belmont Avenue: Richard Villiers and Miles Lanier reveal Nigel's double game;
  Lanier kills him.
- Minutes later -- the garage escape as Renraku's remaining forces close in.

**Site of Desecration**, roughly one month after the Tooth Warriors' first ambush of Denver Bob's
Black Dog smuggling team:
- Day 0 -- Daisy Quallon hires the runners at The Magic Touch; the exchange with the Pentagon is set
  for noon the next day at Hemlock Pass.
- Day 1, morning -- the border crossing and the drive/flight up Denny Creek to Hemlock Pass.
- Day 1, midday -- the wrecked Pentagon rotorcraft and the meet with Pounder's crew.
- Day 1, night -- the confrontation with Kaztok and the Old One at Crescent Eye's farm, then the
  march to the Site of Desecration; Kaztok's "trial," the Old One's tests, and Kaztok's death.
- Day 2 -- the runners return to Seattle; Daisy is still away.
- Day 3 -- the runners deliver Daisy's telesma; the Old One reveals himself to her and departs.
"""

ORGS = [
    {
        "name": "TekLon Electronics",
        "org_type": "corporation (microtronics and cybertech components)",
        "tier": 2,
        "headquarters": "Alpha Wing, Auburn (five fenced, guarded buildings connected by sidewalks, with underground complexes)",
        "summary": "Small Auburn microtronics firm caught between Novatech and Renraku in the wreckage of Fuchi's collapse; developing an unfinished cybernetic head prototype",
        "description": (
            "An 'orphan corporation' -- one of the small companies Fuchi Industrial Electronics had "
            "quietly invested in before it broke apart, leaving its ownership disputed. TekLon's work in "
            "advanced cybertech and microtronics design is valuable enough that both Novatech, Inc. and "
            "Renraku Computer Systems now claim to be its legitimate parent, and employees loyal to both "
            "sides work inside it while the company clings to nominal independence. Renraku intends to "
            "take TekLon by force; Novatech has gone the stealthier route, inserting a cleanup specialist "
            "to grab what it wants and set the research lab up for destruction. TekLon's own claim to fame "
            "on the street is a rumored 'revolutionary microtronics breakthrough' -- in truth, an unfinished "
            "cybernetic head prototype built in the Alpha Wing lab known as the Pit."
        ),
        "notes": (
            "Supernova: security on the Alpha Wing Matrix system is normally Easy Orange (system ratings "
            "4/10/10/10/10/6, no IC) -- deliberately taken off-line by Novatech's Nigel Terwilliger ahead "
            "of the Renraku raid he tipped off. After the raid the system snaps to Red Hard "
            "(8/16/14/18/18/18) and begins erasing files. Legwork TN 4 (Corporate Contacts) 1 a Auburn "
            "microtronics manufacturer; 2 supplies roughly 75 percent of cyberlimb microtronics; 3-4 lost "
            "backing during the corp war (Lakeview International Holding Company, a Fuchi shell); 5 "
            "Novatech and Renraku both claim ownership; 6+ a 'revolutionary' announcement is coming. "
            "Street-level contacts give the same beats with more color and less certainty."
        ),
        "enemies": ["Renraku Computer Systems"],
        "allies": ["Novatech, Inc."],
    },
    {
        "name": "The Pentagon",
        "org_type": "smuggling crew",
        "tier": 1,
        "headquarters": "New Orleans (mobile; runs the New Orleans-Seattle route via Denver or Minneapolis)",
        "summary": "Five-member smuggling crew with an excellent reputation for delivering the goods with a minimum of heat; ambushed and robbed by the Tooth Warriors while dropping off telesma for Daisy Quallon",
        "description": (
            "A tight, professional smuggling crew who call their own shots and answer to no Johnson: "
            "Pounder (founder, contact man and spokesman), Breetva (negotiator), Heeley (rigger), and the "
            "ork twins Red-Scale-Snake (shaman) and Night-Strike-Woman (physical adept). They have worked "
            "for the talismonger Daisy Quallon before, running quality telesma and other magical goods up "
            "from New Orleans. Smugglers live and die by reputation -- no nuyen means no biz -- so the "
            "Pentagon will fight, deal, or do both in the same conversation to protect a delivery and their "
            "name on the street."
        ),
        "notes": (
            "Site of Desecration: ambushed at the Tooth by the Tooth Warriors under cover of a spirit "
            "attack from the Old One; their cargo and ready weapons taken, their T-bird downed by the "
            "spirit's Accident power on the escape and crash-landed at Hemlock Pass. Cut a deal with the "
            "player characters (or the runners' muscle) to hit the Tooth Warriors' camp and recover both "
            "Daisy's telesma and the Pentagon's own stolen goods. Keep their word: become a smuggling "
            "contact for the team if the exchange goes honestly, spread word of the runners' help on the "
            "street either way."
        ),
    },
    {
        "name": "Tooth Warriors",
        "org_type": "gang (troll and ork thugs)",
        "tier": 1,
        "headquarters": "Site of Desecration, the Tooth, Cascade Mountains (Cascade Ork territory)",
        "summary": "New gang formed by the troll Kaztok around a crashed smuggler rotorcraft and a captive man-of-the-woods spirit; robs smugglers passing through the Tooth",
        "description": (
            "A month-old gang of disenfranchised trolls and orks that Kaztok gathered after he discovered "
            "a nature spirit, the Old One, in the wreckage of a crashed Ares Dragon smuggling rotorcraft. "
            "Convinced the spirit answers to him, Kaztok uses its Fear and Confusion powers to waylay and "
            "rob the smugglers who have traditionally traded peacefully with the Tooth, keeping the guns, "
            "cyberware, decks and drugs the locals never used to see. At least fifty orks and trolls camp "
            "around the wreck, none of them trained mages or shamans; six or more Tooth Warriors do the "
            "actual muscle work under Kaztok's direct command."
        ),
        "notes": (
            "Site of Desecration: not sanctioned by the wider Cascade Ork tribe -- Kaztok is exploiting "
            "local resentment at how little smugglers historically leave behind, not tribal policy. "
            "Already ambushed Denver Bob's Black Dog smuggling team a month before the adventure (guns "
            "stolen, the crew captured and tortured rather than killed) and the Pentagon at the adventure's "
            "opening. The gang -- and Kaztok's authority over it -- collapses the moment the Old One turns "
            "on him at the Site of Desecration, killing him in a staged 'accident.'"
        ),
        "enemies": ["The Pentagon", "Black Dog"],
    },
    {
        "name": "Black Dog",
        "org_type": "smuggling crew",
        "tier": 1,
        "headquarters": "Denver (mobile)",
        "summary": "Denver smuggling team led by Denver Bob; ambushed by the Tooth Warriors a month before Site of Desecration and presumed dead until the runners find survivors being tortured at Crescent Eye's farm",
        "description": (
            "A smuggling crew out of Denver, on friendly terms with the farmers of the Tooth -- Denver Bob "
            "himself once brought medicine for a sick child rather than take payment. Ambushed and robbed "
            "by the newly formed Tooth Warriors, their rotorcraft brought down by the Old One's Accident "
            "power; presumed dead in the sprawl for a month while Kaztok's people kept the survivors as "
            "prisoners and leverage against the farmer Crescent Eye, who had been sheltering them."
        ),
        "notes": (
            "Site of Desecration: the player characters find Denver Bob and at least one other Black Dog "
            "member being worked over in Crescent Eye's barn. If the runners help them (directly or by "
            "resolving the Kaztok/Old One situation), word gets back to Black Dog -- they do not become "
            "contacts, but the team earns solid goodwill in the wider smuggling community."
        ),
    },
]

LOCATIONS = [
    {
        "name": "TekLon Electronics (Alpha Wing / the Pit)",
        "location_type": "research lab",
        "district": "Auburn",
        "city": "Auburn",
        "security_level": "Corporate Standard",
        "controlling_org": "TekLon Electronics",
        "summary": "TekLon's Auburn microtronics campus; the Alpha Wing lab (nicknamed the Pit) holds the unfinished cybernetic head prototype the runners are hired to steal",
        "description": (
            "Five fenced, guarded buildings connected by sidewalks, with underground complexes beneath "
            "them. The runners' entry point is a disused cable-access tunnel a kilometer from an Auburn "
            "manhole, sealed off from Alpha Wing by a warded (Force 6) ferrocrete wall that a corporate "
            "solvent turns briefly gelatinous. Inside: a storage room of medical supplies, a post-op ward, "
            "an operating theater lined with resin skeletons of each metahuman race, a dressing room, a "
            "stairwell, a carpeted hallway of personal offices and a break lounge, and the microtronics "
            "labs proper -- a glass-walled bench area and a glove-box 'clean room' whose far corner holds a "
            "complete microtronics skeleton missing its head. A steel blast door (Barrier Rating 16), off "
            "the security Matrix entirely, seals the rest of the facility from Alpha Wing."
        ),
        "notes": (
            "Supernova: security taken off-line ahead of time by Nigel Terwilliger (see TekLon Electronics, "
            "org). The prize -- a locked case with a Novatech starburst logo, containing an unfinished, "
            "skinless cybernetic head prototype -- sits alone on a bench in the lab's third glass-walled "
            "room. Renraku's raid on the rest of the facility (explosions, gunfire, a fist punching through "
            "the sealed blast door) happens while the runners are still inside but never reaches Alpha "
            "Wing itself; it exists to terrify the team into a clean, fast exit. See MATRIX_HOSTS for the "
            "system layout."
        ),
    },
    {
        "name": "Novatech Penthouse (3844 Belmont Avenue)",
        "location_type": "corporate headquarters",
        "district": "Downtown",
        "security_level": "Corporate High Security",
        "controlling_org": "Novatech, Inc.",
        "summary": "Richard Villiers' Seattle meeting floor -- the entire fourteenth story of a brand-new downtown office tower, reached by a single unmarked elevator",
        "description": (
            "A fourteen-story office building so new the paint still smells fresh, with a single glass "
            "entrance, a deserted marble lobby, and one working elevator whose only button reads "
            "'Penthouse.' The top floor is a single vast room: a wall of video monitors running newscasts "
            "and stock tickers, a full bar along a window wall with a spectacular skyline view, five "
            "custom-built desks (including dwarf- and troll-sized furniture), a sunken entertainment pit "
            "with a circular fireplace, and a round meeting table with its own terminal. Framed photos and "
            "shelves of books complete the impression of a man who lives here as much as he works here."
        ),
        "notes": (
            "Supernova: the maglock on the street doors is battery-powered and off the Matrix entirely; "
            "the fourteenth floor carries a Force 14 ward, though the elevator shaft itself does not. If "
            "the runners turn hostile, Villiers and Lanier retreat behind a Barrier Rating 12 sealed "
            "chamber while neuro-stun gas floods the room, or a Force 12 hearth spirit and fire elemental(s) "
            "handle the problem -- Villiers and Lanier never actually die here regardless of what the "
            "runners try. This is where Nigel Terwilliger's double game against Renraku is exposed and "
            "Miles Lanier kills him; the garage one floor below is where the escape from Renraku's Red "
            "Samurai (Too Much of a Good Thing) plays out."
        ),
    },
    {
        "name": "100th and Main (Bellevue)",
        "location_type": "warehouse district intersection",
        "district": "Warehouse District",
        "city": "Bellevue",
        "security_level": "Low Security",
        "summary": "Deserted four-corner warehouse intersection where Elizabeth Chavez dies and Renraku's Red Samurai ambush the runners for her case",
        "description": (
            "A dead, four-story warehouse block with no doorway cover -- the entrances sit flush with the "
            "building fronts -- and an alley half a block down 100th Street with fire-escape access to the "
            "roofs, the closest thing to a defensible position on the corner. No cars, no people, little "
            "light; a good meeting spot by smuggler or spy standards, and exactly why Elizabeth Chavez "
            "picked it for the case exchange with Nigel Terwilliger's runners."
        ),
        "notes": (
            "Supernova (Four Corners): Chavez arrives in a wrecked, smoking car and dies before the swap "
            "can happen; two five-man Red Samurai teams (four gun-troops and a hermetic mage each) rappel "
            "in from helicopters to recover her case, backed by a van carrying two more mages and Renraku's "
            "fully armed cyberzombie -- see Renraku Computer Systems, org, for both. The Renraku case in "
            "Chavez's car carries an active Rating 8 tracking device, which is how the Red Samurai found "
            "her; her personal datapad gives the runners the Belmont Avenue payout address and code."
        ),
    },
    {
        "name": "The Magic Touch",
        "location_type": "talismonger shop",
        "district": "far eastern Renton, near the Salish-Shidhe border",
        "city": "Renton",
        "security_level": "Patrolled / Commercial",
        "summary": "Daisy Quallon's modest talismonger shop on the edge of the sprawl, where she hires the runners to handle a smuggling exchange she cannot make herself",
        "description": (
            "A small shop in a part of Renton that feels more like the wilds of the NAN lands than the "
            "sprawl -- trees, grass, small animals that have not yet learned to fear metahumans. The front "
            "is unremarkable and often looks closed; the back room holds an elaborate Force 6 hermetic "
            "circle painted directly into the floor tiles, fine enough art to impress even a non-magical "
            "eye, where Daisy briefs the runners after-hours on her problem: a smuggling crew, the "
            "Pentagon, is bringing her quality telesma up from New Orleans, and an emergency out-of-town "
            "trip means she cannot make the pickup herself."
        ),
        "notes": (
            "Site of Desecration: Daisy keeps three Force 6 elemental spirits (fire, air, earth) bound "
            "here. Pays 5,000 nuyen per runner, or lets a mage put the same amount toward raw materials or "
            "a focus from her stock; will not negotiate the offer. She is not asking the team to shadowrun "
            "-- to her this is a simple courier job, and she is embarrassed to have to ask at all. This is "
            "also where the Old One is ultimately delivered at the adventure's close, and where Daisy "
            "quietly contacts the great dragon Hestaby once she recognizes what he is."
        ),
    },
    {
        "name": "Site of Desecration",
        "location_type": "gang territory",
        "district": "The Tooth, Cascade Mountains",
        "city": "Salish-Shidhe Council",
        "security_level": "No Security / Barrens",
        "controlling_org": "Tooth Warriors",
        "summary": "The crash site of a smuggler's Ares Dragon rotorcraft, now the Tooth Warriors' camp and the Old One's haunt -- the adventure's title location and final confrontation",
        "description": (
            "A clearing violently opened by a rotorcraft that hit the earth nose-first, the wreck now hung "
            "with lamps and looming over a camp of at least fifty orks and trolls around a dozen or more "
            "campfires. None of the camp are trained mages or shamans; the only magic here is the Old One "
            "himself, who drifts constantly in and out of the physical plane as tree, shadow, animal or a "
            "gaunt tribal-dressed old man, never quite where the eye expects him. Kaztok holds a rough camp "
            "'trial' here for captured smugglers and the runners alike, deciding who lives, who is "
            "'tested,' and who gets handed over as the Old One's plaything."
        ),
        "notes": (
            "Site of Desecration: Kaztok's hidden stash of stolen goods (guns, ammunition, simchips, "
            "medical supplies, telesma and other magical goods, regional trade goods, cheap cyberdecks) is "
            "kept apart from the main camp; runners who cut a deal are sent to retrieve it under guard. The "
            "climax happens here: Kaztok, having outlived his usefulness, is killed in a staged 'accident' "
            "by the Old One in front of the whole camp once the spirit decides who among the runners or the "
            "Pentagon is strong enough to take him beyond these woods."
        ),
    },
    {
        "name": "Denny Creek",
        "location_type": "mountain town",
        "district": "Cascade foothills, along Denny Creek",
        "city": "Salish-Shidhe Council",
        "security_level": "Low Security",
        "summary": "Small NAN tourist town at the edge of Cascade Ork territory, the last stop before the off-road push to Hemlock Pass and the Tooth",
        "description": (
            "A town built to resemble outsiders' idea of a small NAN settlement -- tourist-friendly on the "
            "surface, but real people live and work here, and few orks, trolls or dwarfs are seen who "
            "aren't obvious out-of-towners. Prices run double Seattle's; nothing illegal is for sale, though "
            "bows, arrows and knives are legal in the NAN and openly displayed. The creekside road out of "
            "town runs past Keekwulee Falls and Snowshoe Falls before giving way to dirt paths and, "
            "eventually, trackless wilderness toward the creek's source and Hemlock Pass."
        ),
        "notes": (
            "Site of Desecration: many locals, especially humans, carry open anti-sprawl sentiment. The "
            "runners can pose as tourists and overnight here on the way back from the Tooth to cross the "
            "Seattle border during the safer morning rush -- any player character with a credstick willing "
            "to pay for rooms avoids trouble beyond some odd stares."
        ),
    },
]

NPCS = [
    {
        "name": "Nigel Terwilliger",
        "role": "First-time Mr. Johnson -- a Novatech cleanup specialist secretly double-dealing with Renraku, who hires the runners to rob TekLon and dies for the betrayal",
        "archetype": "Corporate Fixer",
        "title": "Cleanup specialist, Novatech, Inc. (double agent for Renraku Computer Systems)",
        "race": "Human",
        "gender": "Male",
        "age": 35,
        "organization": "Novatech, Inc.",
        "connection": 2,
        "description": (
            "Thirty-five, a bit portly, gray starting to show at the temples -- so utterly average and "
            "unremarkable that he can sit down at any desk in any office and no one thinks to notice him, "
            "the gift that made him a first-rate corporate infiltrator. As Mr. Johnson he is a bundle of "
            "nerves, stammering over his own alias, glancing over his shoulder, in an ordinary gray suit, "
            "white shirt and red tie."
        ),
        "background": (
            "A former Fuchi Industrial Electronics infiltration specialist who rode out Fuchi's collapse at "
            "the doomed research outfit Abstract Media Services, then landed with Novatech within days of "
            "the corp publicly revealing its own interest in Abstract. Novatech uses him to insert himself "
            "into 'orphan' corporations left ownerless by Fuchi's breakup, secure whatever technology or "
            "information Novatech wants, and either bring the company into the fold or burn its assets so "
            "Renraku or Shiawase cannot have them. Assigned to TekLon Electronics to steal an unfinished "
            "cybernetic head prototype and set the research lab up for destruction, Nigel got greedy and "
            "sloppy: he started selling copies of everything he touched to Renraku as well, running both "
            "sides for a highly profitable few years before his cover slipped."
        ),
        "notes": (
            "Stats: B3 Q3 S3 C4 I6 W6, Init 4+1D6; Biotech 2, Car 3, Computer 4, Electronics 6, Etiquette "
            "4 (Corporate 7), Negotiation 8; datajack; Colt American L36. Fellow TekLon employee Elizabeth "
            "Chavez catches him copying research files for Renraku on the same night Renraku's own raid on "
            "TekLon (which Nigel tipped off) is set to go; she flees with the wrong case, forcing him to "
            "hire the runners to retrieve it and arrange a swap that will cover his tracks with both "
            "employers at once. Miles Lanier shoots him dead at the Novatech penthouse once Villiers "
            "confirms the double game via Chavez's recovered datapad."
        ),
        "contact_skills": ["Corporate infiltration and cleanup work", "Orphan-corp ownership disputes (post-Fuchi)"],
    },
    {
        "name": "Elizabeth Chavez",
        "role": "TekLon research scientist loyal to Novatech who exposes Nigel Terwilliger's double-dealing and dies for it in a Renraku ambush",
        "archetype": "Research Scientist",
        "title": "Research scientist, TekLon Electronics (loyal to Novatech, Inc.)",
        "race": "Elf",
        "gender": "Female",
        "organization": "TekLon Electronics",
        "connection": 1,
        "description": (
            "An elf research scientist at TekLon whose quiet loyalty to Novatech makes her the one person "
            "who notices something is wrong when company files start going missing or destroyed. Careful "
            "and controlled under pressure -- she picks a defensible four-corner intersection for a case "
            "exchange with total strangers on a few hours' notice, and keeps a private calendar disciplined "
            "enough to lay out the whole night's events for anyone who finds her datapad."
        ),
        "background": (
            "Discovered that Nigel Terwilliger was copying and destroying TekLon research files and "
            "confronted him; he claimed they both answered to Novatech's Miles Lanier, and she chose to "
            "watch rather than immediately report it. On the night Nigel hired the runners and Renraku "
            "raided TekLon, she saw him copy files into a case and place a call to arrange 'an event,' "
            "grabbed the case herself believing it held Novatech's property, and fled with Nigel chasing "
            "her. She called her real Novatech contact, was told to make the swap with Nigel and then go on "
            "to the Belmont Avenue payout, and arranged the 2 a.m. exchange herself."
        ),
        "notes": (
            "Supernova (Four Corners): the case she actually stole holds nothing but copies of research "
            "Novatech already has -- the prize Nigel meant for Renraku -- and carries an active Rating 8 "
            "Renraku tracking device, unknown to everyone including her. Arrives at the 100th and Main "
            "exchange in a wrecked, smoking car and is dead before the runners can reach her; on the seat "
            "beside her body are the case and her personal datapad, whose recovered calendar entries expose "
            "the whole scheme and lead the runners to the Belmont Avenue payout."
        ),
    },
    {
        "name": "Daisy Quallon",
        "role": "Ms. Johnson -- an elf talismonger who hires the runners to handle a smuggling exchange she cannot make herself, and who is quietly an information source for the great dragon Hestaby",
        "archetype": "Talismonger",
        "title": "Talismonger, The Magic Touch (Renton)",
        "race": "Elf",
        "gender": "Female",
        "age": 25,
        "connection": 2,
        "description": (
            "Twenty-five, green-eyed, blond hair dyed in at least six colors -- one of the most striking "
            "women the runners are likely to meet, and could easily have been a sim starlet instead of "
            "running a modest talismonger shop. Practical and a little embarrassed to be asking for help at "
            "all: 'I'm in an old-fashioned squeeze,' she tells her contact, laughing nervously at her own "
            "predicament."
        ),
        "background": (
            "Born in the disputed northern California Free State to an elf and an Amerindian who fled "
            "persecution from both Tir Tairngire's elves and anti-elf Californians; has lived most of her "
            "adult life in Seattle. Runs The Magic Touch out near the Salish-Shidhe border and deals "
            "honestly in the magical underground, but she never shadowruns herself and does not consider a "
            "simple courier pickup to be one either. Quietly gathers information on magical undercurrents in "
            "Seattle, the NAN territories and Tir Tairngire for the great dragon Hestaby -- an allegiance "
            "she will never confirm to anyone, including the runners she hires."
        ),
        "notes": (
            "Stats: B2 Q4 S1 C6 I5 W6, Init 4+1D6, Astral 25+1D6; Aura Reading 6, Conjuring 6, Enchanting "
            "6, Etiquette 4 (Magical Groups 6), Sorcery 6; three Force 6 elemental spirits (fire, air, "
            "earth) bound to her Force 6 hermetic circle. Hires the runners to meet the Pentagon smuggling "
            "crew at Hemlock Pass, pay them, and bring back her telesma shipment; pays 5,000 nuyen per "
            "character or lets it go toward raw materials/a focus, and will not negotiate further. When the "
            "runners eventually deliver the Old One to her shop, she recognizes him for what he is and "
            "quietly contacts Hestaby, whose astral messenger prompts the spirit to move on."
        ),
        "contact_skills": ["Talismonger stock: quality telesma and foci", "Magical undercurrents (Seattle, NAN territories, Tir Tairngire)"],
    },
    {
        "name": "Pounder",
        "role": "Black dwarf founder and leader of the Pentagon smuggling crew -- laid-back until crossed, and the crew's contact man",
        "archetype": "Smuggler Boss",
        "title": "Leader, The Pentagon",
        "race": "Dwarf",
        "gender": "Male",
        "organization": "The Pentagon",
        "connection": 2,
        "description": (
            "A black dwarf with an easy New Orleans attitude that turns dangerous fast once he's actually "
            "annoyed. Runs the Pentagon almost hands-off, with total faith in his people, and does the "
            "team's talking even though he lets Breetva handle the actual negotiating. Knows lots of people "
            "and can get his hands on nearly anything worth smuggling."
        ),
        "background": (
            "Founded the Pentagon and has held it together through hard times, recruiting Breetva out of a "
            "Vladivostok run and taking in the trafficked ork twins Red-Scale-Snake and Night-Strike-Woman "
            "after freeing them from slavers -- an act that ended his stomach for that particular trade for "
            "good."
        ),
        "notes": (
            "Stats: B6 Q3 S5 C2 I3 W4, Init 3+1D6; Assault Rifle 4, Etiquette 2 (Smuggling 6), Gunnery 5, "
            "Leadership 5, Pistols 4; Ares Predator, FN-HAR, survival knife, defensive grenades, Lined Coat, "
            "forest camo. Fires warning shots to keep the runners off the wrecked rotorcraft, then makes "
            "contact once he recognizes Daisy's password or name; brokers the deal to trade Daisy's crates "
            "for the runners' help retrieving the Pentagon's own stolen cargo from the Tooth Warriors."
        ),
    },
    {
        "name": "Breetva",
        "role": "The Pentagon's negotiator -- a Russian ex-pat who kills double-crossing suppliers rather than get taken advantage of",
        "archetype": "Smuggler Negotiator",
        "title": "Negotiator, The Pentagon",
        "race": "Human",
        "gender": "Female",
        "nationality": "Russian",
        "organization": "The Pentagon",
        "connection": 1,
        "description": (
            "A tall, rock-hard-bodied brunette with a thick Russian accent -- her name literally means "
            "'razor.' Has negotiated with street scum, pirates, the Mafia, the yakuza and megacorp "
            "operatives alike, and has a reputation for drinking anyone in New Orleans under the table, a "
            "reputation constantly re-tested there."
        ),
        "background": (
            "Met Pounder on a smuggling run into Vladivostok, where she killed the suppliers who tried to "
            "double-cross her rather than let it slide; Pounder recruited her on the spot and never "
            "regretted it."
        ),
        "notes": (
            "Stats: B5 Q4(5) S5(6) C3 I4 W3, Init 4(6)+1D6(2D6); Etiquette 3 (Smuggling 6), Intimidation 4, "
            "Negotiations 8, Pistols 6; retractable hand spurs (alphaware), Wired Reflexes 1, Ares Predator, "
            "Ceska Black Scorpion. Handles all real negotiation for the Pentagon -- with Kaztok over the "
            "Tooth Warriors' loot, and as a last resort with the runners themselves, offering a share of "
            "future smuggled goods if the team's payment falls through."
        ),
    },
    {
        "name": "Heeley",
        "role": "The Pentagon's rigger -- looks about twelve, talks with a heavy Creole drawl, and just lost his beloved GMC Banshee to the Tooth Warriors' ambush",
        "archetype": "Rigger",
        "title": "Rigger, The Pentagon",
        "race": "Human",
        "gender": "Male",
        "nationality": "Creole (New Orleans)",
        "organization": "The Pentagon",
        "connection": 1,
        "description": (
            "Well into his thirties but looks about twelve years old, with a heavy Creole drawl that "
            "outsiders often struggle to follow. Uses his young looks to bait marks into betting "
            "competitions he then wins, with Breetva on hand to smooth over any hard feelings after."
        ),
        "background": (
            "Pounder's oldest partner in the crew; the two of them used to broker deals in New Orleans "
            "between pirates who would not dock and smugglers who would not go to sea. Poured his heart "
            "into his customized GMC Banshee, 'Creole Lady' -- smashed to pieces in the crash that opens "
            "Wreckage."
        ),
        "notes": (
            "Stats: B5 Q6 S4 C3 I6 W5, Init 6+1D6, Rigging Init 10+3D6; Vector Thrust Vehicles 5 (GMC "
            "Banshee 7), Vehicle Control Rig 2, Gunnery 5; Ceska Black Scorpion, survival kit. Lost control "
            "of the fleeing rotorcraft as the Old One's Accident power struck; can help work out what really "
            "happened at the crash site (rigger tests) once the runners find the wreck."
        ),
    },
    {
        "name": "Red-Scale-Snake",
        "role": "Ork Snake shaman of the Pentagon -- twin sister of Night-Strike-Woman, freed from slavers and grown into the crew's magical back-up",
        "archetype": "Street Shaman",
        "title": "Shaman, The Pentagon",
        "race": "Ork",
        "gender": "Female",
        "nationality": "Pueblo Corporate Council",
        "organization": "The Pentagon",
        "connection": 1,
        "description": (
            "Marked by her Snake shamanic mask with gray, silver and black scaled bands radiating from her "
            "mouth; her eyes narrow to slits and her voice turns to a hiss when she casts. Long red hair "
            "reaches nearly to the ground when unbound, usually held up with a snake bone; she has a "
            "disconcerting habit of peeling dry skin like molting, which her Pentagon crewmates have long "
            "since stopped noticing."
        ),
        "background": (
            "Sold with her twin, Night-Strike-Woman, as trafficked 'exotic sex slaves' to a rich Confederated "
            "American States landowner they killed almost on arrival; the pair ended up homeless in New "
            "Orleans until Pounder took them in, seeing how well they worked together and having no "
            "magical support of his own at the time."
        ),
        "notes": (
            "Stats: B6 Q3 S5 C5 I3 W6, Init 3+1D6, Astral 23+1D6; Aura Reading 5, Conjuring 6, Sorcery 5; "
            "totem Snake (+2 detection/health/illusion, +2 vs Mountain Spirits, -1 all spells in combat); "
            "spells including Manabolt, Antidote Toxin, Treat; Power Focus 2, Manipulation Focus 3. Astrally "
            "scouted the Tooth ahead of the original ambush and nearly did not make it back to her body "
            "after brushing against the Old One's true power -- her account of that encounter is the "
            "runners' first real clue what they are dealing with."
        ),
    },
    {
        "name": "Night-Strike-Woman",
        "role": "Ork physical adept of the Pentagon -- Red-Scale-Snake's bigger, quieter twin, still protective of her after the slavers",
        "archetype": "Physical Adept",
        "title": "Physical adept, The Pentagon",
        "race": "Ork",
        "gender": "Female",
        "nationality": "Pueblo Corporate Council",
        "organization": "The Pentagon",
        "connection": 1,
        "description": (
            "Bigger and stronger than her minutes-younger twin sister and protective of her since "
            "childhood; talks little and lets Red-Scale-Snake speak for both of them. Being sold as a "
            "slave alongside her sister shattered her trust in her own tribe more deeply than it did Red's, "
            "though Pounder's willingness to help them both restored some of it."
        ),
        "notes": (
            "Stats: B8 Q5 S8 C3 I3 W4, Init 4(6)+1D6(2D6); Athletics 6, Unarmed Combat 6(8); Combat Sense "
            "2, Improved Ability (Unarmed Combat) 2, Improved Reflexes 1, Killing Hands, Missile Parry, Pain "
            "Resistance 2, Rapid Healing 2; Ceska Black Scorpion, heavy crossbow. The Pentagon's muscle in a "
            "fight -- the runners likely will not realize she is a physical adept until they see her in "
            "hand-to-hand. Breaks from cover to charge the Tooth Warriors torturing Denver Bob's crew if the "
            "runners hesitate too long at Crescent Eye's farm."
        ),
    },
    {
        "name": "Kaztok",
        "role": "Troll leader of the Tooth Warriors -- convinced he controls the Old One, when in fact the spirit has been using him the whole time",
        "archetype": "Gang Boss",
        "title": "Leader, Tooth Warriors",
        "race": "Troll",
        "gender": "Male",
        "organization": "Tooth Warriors",
        "connection": 1,
        "description": (
            "Taller, fatter and a touch smarter than the average troll -- enough to make him an effective "
            "gang leader and an ideal patsy in the same breath. Spent months resenting how little the "
            "smugglers passing through the Tooth left behind, drinking and plotting without the nerve to "
            "act, until an Ares Dragon crashed at his feet and handed him both muscle and an excuse."
        ),
        "background": (
            "Found the Old One sitting motionless in the wreckage of the crashed rotorcraft, mistook for a "
            "tree stump at first; when the spirit asked who had 'destroyed his woods,' Kaztok's answer of "
            "'smugglers' gave the Old One a target and gave Kaztok, in his own mind, a spirit under his "
            "command. Used the Old One's Fear and Confusion powers to build the Tooth Warriors and rob "
            "smuggling crews of everything the Tooth had never seen before -- guns, cyberware, decks."
        ),
        "notes": (
            "Stats: B11(12) Q3 S9 C3 I3 W5, Init 3+1D6; Intimidation 5, Pistols 5, Rifles 5, Unarmed Combat "
            "5; Ares Predator, Leadership Staff (a piece of the Ares Dragon's landing gear), survival knife, "
            "Lined Coat. Holds a rough 'trial' over the runners and the Pentagon at the Site of Desecration, "
            "convinced the team is holding out valuable gear on him; shot dead by his own ricocheting bullet "
            "-- the Old One's doing -- the moment the spirit decides he has outlived his usefulness."
        ),
    },
    {
        "name": "The Old One",
        "role": "A free-willed man-of-the-woods nature spirit, not bound to any shaman or conjurer, who let Kaztok believe he was in control while pursuing an agenda entirely his own",
        "archetype": "Nature Spirit",
        "title": "Man-of-the-woods (unbound)",
        "race": "Spirit (man-of-the-woods)",
        "connection": 3,
        "description": (
            "Normally appears as a smaller-than-average human in tribal dress, but shifts constantly and "
            "at will between forms -- a deep patch of living shadow, a walking, branch-tossing tree, a "
            "talking woodland animal. Assensed, he reads as a flickering, shimmering humanoid. Acts naive "
            "and biddable around Kaztok, a performance so convincing the troll never suspects who is really "
            "testing whom."
        ),
        "background": (
            "A rare, powerful nature spirit that exists on the physical plane without ever having been "
            "conjured, tied to no domain, shaman or ritual -- dispelling him only banishes him for hours "
            "equal to the banisher's Force before he returns, usually angry. Has lived in the Tooth longer "
            "than anyone now living, and has grown curious about the wider world from decades of "
            "eavesdropping on smugglers passing through his woods."
        ),
        "notes": (
            "Stats: B12 Q8x2 S9 C7 I7 W7, Init 17+1D6, Astral 27+1D6; Attacks 7S; Powers: Accident, "
            "Concealment, Confusion, Fear (all Domain), Immunity to Normal Weapons, Magical Guard, "
            "Materialization, Movement, Weather Control. Lets Kaztok believe he commands him while pursuing "
            "his own goal -- reaching a strong enough traveling companion to take him beyond his woods -- "
            "and tests the runners (and the Pentagon) with Charisma/Willpower contests, staged 'accidents,' "
            "and outright Fear once Kaztok is no longer useful. Will not die in combat, only retreat to the "
            "metaplanes and return later; an excellent recurring character if the gamemaster wants him back."
        ),
    },
    {
        "name": "Crescent Eye",
        "role": "Cascade Ork farmer sheltering Denver Bob's captured smuggling crew, caught between Kaztok's threats and his own conscience",
        "archetype": "Farmer",
        "title": "Farmer, the Tooth",
        "race": "Ork",
        "gender": "Male",
        "connection": 1,
        "description": (
            "A man of conscience with no taste for trouble, squeezed between Kaztok's threats and his own "
            "loyalty to the Black Dog smugglers who have always treated his family well. Argues with Kaztok "
            "in front of the runners rather than simply give in: 'Denver Bob brought medicine for Morning "
            "Dawn when she was sick ... he isn't anyone's enemy, no matter what the Old One says.'"
        ),
        "notes": (
            "Stats: B5 Q3 S4 C2 I2 W3, Init 2+1D6; Rifles 1, Shotguns 1, Unarmed Combat 1; Leather Jacket. "
            "Sheltering the surviving Black Dog smugglers in his barn brings Kaztok and three Tooth Warriors "
            "down on his farm; the Old One tests the runners on his behalf, once making him flee into the "
            "woods under the Fear power as a pretext to get the team away from camp. His daughter Morning "
            "Dawn's illness, and Denver Bob's kindness treating it without payment, is the emotional core of "
            "the scene."
        ),
    },
    {
        "name": "Denver Bob",
        "role": "Leader of the Black Dog smuggling team; ambushed by the Tooth Warriors a month earlier and presumed dead, actually held and tortured at Crescent Eye's farm",
        "archetype": "Smuggler Boss",
        "title": "Leader, Black Dog",
        "race": "Human",
        "organization": "Black Dog",
        "connection": 1,
        "description": (
            "A well-known, experienced smuggler on the Seattle-Denver route, on good enough terms with the "
            "farmers of the Tooth that he once brought medicine for a sick child and refused payment beyond "
            "a home-cooked meal. Beaten and bandaged when the runners find him, still defiant."
        ),
        "background": (
            "Led the Black Dog crew into an ambush by the newly formed Tooth Warriors a month before the "
            "adventure's main events; his shipment of guns was stolen and his rotorcraft brought down by "
            "the Old One's Accident power as his team tried to flee. Presumed dead ever since -- in truth, "
            "he and at least one crewmate have been kept alive and periodically worked over in Crescent "
            "Eye's barn as leverage against the farmer."
        ),
        "notes": (
            "No published stat block (Black Dog is not statted as a team). Screams in pain under a Tooth "
            "Warrior's beating when the runners first spot Kaztok's confrontation with Crescent Eye -- the "
            "trigger point for the scene's key decision. If freed, word of the runners' help reaches Black "
            "Dog's people in Denver even though the crew itself does not become a contact."
        ),
    },
]

ORG_UPDATES = {
    "Novatech, Inc.": {
        "notes_append": (
            "First Run (Supernova, 2061): a Boston-run cleanup specialist, Nigel Terwilliger, is caught "
            "secretly also selling to Renraku Computer Systems while working the disputed orphan corp "
            "TekLon Electronics for Novatech. Richard Villiers personally handles the fallout at Novatech's "
            "Seattle penthouse (3844 Belmont Avenue), has Miles Lanier execute Terwilliger, and recruits the "
            "runner team who recovered both cases to run interference against a Renraku Red Samurai strike "
            "on the building's garage -- a favor Villiers repays later, at his own discretion."
        ),
    },
    "Renraku Computer Systems": {
        "notes_append": (
            "First Run (Supernova, 2061): sends a Red Samurai raid on TekLon Electronics' Auburn facility "
            "(tipped off by its own double agent inside Novatech, Nigel Terwilliger) and, separately, two "
            "five-man Red Samurai teams (four gun-troops plus one hermetic elf mage each) to recover a "
            "tracked case from the dying Novatech researcher Elizabeth Chavez at 100th and Main, Bellevue. "
            "The second strike is backed by a first-generation cyberzombie -- unnamed, dual-natured, "
            "controlled by the accompanying mages' spoken commands, immune to normal weapons and treated by "
            "any astrally perceiving character as a source of 'negative mana.' Red Samurai never speak "
            "aloud on operations, coordinating entirely by headware; per Renraku's own institutional "
            "prejudice, its rank-and-file gun-troops are recruited exclusively human even as its attached "
            "combat mages are elves. A third strike, in force, hits Novatech's Seattle penthouse garage "
            "shortly after, trying to stop Richard Villiers and Miles Lanier from getting away."
        ),
    },
    "Cascade Ork": {
        "notes_append": (
            "First Run (Site of Desecration, 2061): a troll named Kaztok forms a rogue splinter gang, the "
            "Tooth Warriors, in the Tooth using a captive-in-his-own-mind nature spirit (the Old One) to rob "
            "smugglers who have traditionally traded peacefully with the tribe -- not sanctioned by wider "
            "Cascade Ork leadership, and resolved (one way or another) within about a month of forming."
        ),
    },
    "Chiller Thrillers": {
        "notes_append": (
            "First Run (Food Fight, SR3 reprint): same six-member gang and the same Stuffer Shack robbery, "
            "restatted for Third Edition. Gang member 'Wendy' appears here as 'Zany' with the same role -- "
            "flagged as a discrepancy, not treated as a different person (see Wendy, NPC_UPDATES). This "
            "printing drops the 2050 version's 'equalizer,' the street mage Sally Tsung, entirely; no update "
            "needed on her row."
        ),
    },
}

LOC_UPDATES = {
    "Club Penumbra": {
        "notes_append": (
            "First Run (Supernova, 2061): the meet site for Nigel Terwilliger's job offer -- a nervous "
            "first-time Mr. Johnson in a booth with a silver case, hiring the team to hit TekLon Electronics "
            "for 20,000 nuyen a head. Business is slow that season; the club's usual draw suffers for "
            "sitting too close to the UCAS military security zone thrown up around the (recently, "
            "mysteriously shut-down) Renraku Arcology."
        ),
    },
    "Stuffer Shack - Redmond Barrens": {
        "notes_append": (
            "First Run (Food Fight, SR3 reprint): the same robbery scenario restatted for Third Edition, "
            "with Wanda, Mr. Nick and Johnny unchanged, Jacky Scatman and Angie Scatman present as before "
            "(here as 'Jack' and Angie), and the same store layout. Adds a little more color to the "
            "established background bystanders -- Mrs. Needles pushes her cart down an aisle like an Urban "
            "Brawl player before hiding and screaming, her son Louis pesters everyone in earshot about "
            "dragons and ghouls, and Timmy Thinners works up his nerve to talk to Wanda from the electronics "
            "aisle -- without promoting any of them beyond the color captured on this row already."
        ),
    },
}

NPC_UPDATES = {
    "Richard Villiers": {
        "description_append": (
            "First Run (Supernova, 2061): mid-fifties, solidly built, black hair with an olive cast to his "
            "skin, no obvious cyberware, credits a photographic memory for his recall. A showman as much as "
            "a businessman -- the center of attention wherever he goes -- unmarried and consistently touted "
            "as one of the UCAS's most eligible bachelors."
        ),
        "notes_append": (
            "First Run (Supernova): personally handles the fallout when his cleanup specialist Nigel "
            "Terwilliger is caught also selling to Renraku over the TekLon Electronics job -- receives the "
            "runner team at his Seattle penthouse (3844 Belmont Avenue), pays them their promised fee plus a "
            "bonus for the recovered Renraku case and datapad, has Miles Lanier execute Terwilliger on the "
            "spot, and asks the team to cover his and Lanier's escape from a Renraku Red Samurai ambush in "
            "the building's garage -- a favor he repays later, on his own terms and schedule."
        ),
    },
    "Miles Lanier": {
        "description_append": (
            "First Run (Supernova, 2061): mid-forties but reads as thirty to most people; a bit taller than "
            "average, slight build, chestnut hair perpetually a week overdue for a cut. His near-black eyes "
            "never seem to blink; many assume they are cybereyes, and he never confirms or denies it. Rarely "
            "smiles, lets his actions speak, and notices things most people miss even after they are pointed "
            "out."
        ),
        "notes_append": (
            "First Run (Supernova): shoots Nigel Terwilliger dead at the Novatech penthouse the moment "
            "Villiers confirms, via Elizabeth Chavez's recovered datapad, that Terwilliger was selling "
            "TekLon research to Renraku as well. Coordinates the garage escape from Renraku's Red Samurai "
            "immediately afterward, with the runner team running interference."
        ),
    },
    "Wendy": {
        "notes_append": (
            "First Run (Food Fight, SR3 reprint, pp. 15-16): this printing renames the character 'Zany' "
            "with the same role -- the gang's 'chick,' the object of Wiley's jealousy, sitting on the "
            "dispenser-bar counter during the robbery, armed with an H&K 227 and armored spike heels. Same "
            "person under a different name across printings; not a new gang member."
        ),
    },
    "Lucas Katcherman": {
        "notes_append": "First Run (Food Fight, SR3 reprint, p.16): restatted for Third Edition as 'Catcher,' same psychotic giggling gunman using Wanda and the counter for cover. No change to his established role.",
    },
    "Frank Pilgrim": {
        "notes_append": "First Run (Food Fight, SR3 reprint, p.16): restatted for Third Edition as 'SlicerDicer,' same katana-wielding bushi wannabe who never refuses a challenge to single combat. No change to his established role.",
    },
    "Bill Pruitt": {
        "notes_append": "First Run (Food Fight, SR3 reprint, pp.15-16): restatted for Third Edition as 'Static,' same burned-out wirehead who talks to store objects and only opens fire once a non-ganger 'harms' one. No change to his established role.",
    },
    "Spike": {
        "notes_append": "First Run (Food Fight, SR3 reprint, p.17): restatted for Third Edition, same reluctant newbie more interested in loot, vid-game high scores and porno sims than in hurting anyone.",
    },
    "Willis Fabrizzi": {
        "notes_append": "First Run (Food Fight, SR3 reprint, p.17): restatted for Third Edition as 'Wiley,' same manic Coyote shaman howling and clambering over the shelves during the robbery. No change to his established role.",
    },
    "Wanda": {
        "notes_append": "First Run (Food Fight, SR3 reprint, p.13): same checkout clerk, same delayed reactions, same failure to hit the PANICBUTTON.",
    },
    "Mr. Nick": {
        "notes_append": "First Run (Food Fight, SR3 reprint, pp.13-14): same manager, same Defiance shotgun kept under his desk, same attempt to ambush the robbers from his office.",
    },
    "Johnny": {
        "notes_append": "First Run (Food Fight, SR3 reprint, p.14): same stock boy, still trying to keep out of sight during the robbery.",
    },
    "Jacky Scatman": {
        "notes_append": "First Run (Food Fight, SR3 reprint, pp.14-15): appears here as 'Jack Scatman,' buying cat food with Angie, still armed and still under strict orders (from the scenario, not the character) to fire only in self-defense.",
    },
    "Angie Scatman": {
        "notes_append": "First Run (Food Fight, SR3 reprint, pp.14-15): same character, same self-defense-only stance during the robbery.",
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
**TekLon Electronics -- Alpha Wing security slave (Supernova, before the Renraku raid)**
| Node | Function | Rating | IC |
|---|---|---|---|
| Access node (from the storage-room security box) | Log-on point; Access Rating 10 | Easy Orange (4/10/10/10/10/6) | None |
| Maglock Room (system sculpture: five power switches) | Controls doors A-E and the elevator (elevator itself off-line) | as above | None |
| Camera slave (system sculpture: a sofa, 22 monitors) | Controls all Alpha Wing cameras; Edit Slave sends a tape loop | as above | None |
| Host A | Public: company profile, catalog | Easy Orange | None |
| Host B | Company and personnel records | Easy Orange | None |
| Host C | Sales and financial records | Easy Orange | None |
| Host D | The security system itself (see above) | Easy Orange | None |
| Host E | Research, Alpha Wing and the Pit -- what the runners actually want | Easy Orange; files under Scramble 4 | None |

Security was deliberately taken off-line by Nigel Terwilliger ahead of Renraku's raid; there is no IC
anywhere on the system pre-raid. After the Renraku attack the entire system alerts to **Red Hard**
(8/16/14/18/18/18) and begins erasing files -- a decker returning to the access node afterward finds a
much harder, actively hostile system instead of the one the team already cracked.
"""

NOT_BUILT = """
- **The cyberzombie** (Supernova) -- no name given ("the cyberzombie" throughout); a first-generation
  Renraku black-project asset, folded into Renraku Computer Systems' notes_append rather than built as
  an NPC row.
- **Red Samurai gun-troops and hermetic mages** (Supernova) -- generic squad stat blocks with no named
  individuals; folded into Renraku Computer Systems' notes_append.
- **Rank-and-file Tooth Warriors** (Site of Desecration) -- unnamed troll/ork thugs (generic stat
  blocks, six or more on-page); folded into the Tooth Warriors org row.
- **Hestaby** (Site of Desecration) -- the great dragon Daisy Quallon secretly informs for; never
  appears on-page, only sends an astral messenger. Already judged NOT_BUILT in blood_in_the_boardroom.py;
  this spec follows that precedent and keeps her as a name-drop on Daisy Quallon's row.
- **Abstract Media Services, Lakeview International Holding Company** (Supernova) -- defunct Fuchi-era
  shell/holding entities, name-dropped only in TekLon's background legwork; both are gone, nothing to
  build.
- **Morning Dawn** (Site of Desecration) -- Crescent Eye's sick daughter, name-dropped as the reason
  Denver Bob once helped his family; captured as color on Crescent Eye's row.
- **Mrs. Needles, Louis Needles, Timmy Thinners** (Food Fight) -- reprised bystander color, already
  judged NOT_BUILT (captured in the Stuffer Shack location notes) by food_fight.py; this spec follows
  that precedent rather than promoting them.
- **The Black Dog rotorcraft crew beyond Denver Bob** -- unnamed, unstatted; folded into the Black Dog
  org row.
- **Various generic critter suggestions** (Site of Desecration: devil rats, aardwolves, barghests,
  griffins, thunderbirds, etc.) -- explicitly left to gamemaster's choice in the text, nothing concrete
  to build.
- FASA sourcebook pointers only, no content extracted: Blood in the Boardroom (already its own spec),
  Renraku Arcology: Shutdown, New Seattle, Cyberpirates, Target: Smuggler Havens, Man and Machine, the
  Dragonheart Saga novels, Virtual Realities 2.0, Portfolio of a Dragon: Dunkelzahn's Secrets,
  Headhunters, Technobabel, Target: UCAS, Corporate Download, Magic in the Shadows, The Underworld
  Sourcebook, Predator and Prey (already its own spec).
"""

PLAY_NOTES = """
- Food Fight: this is a pure combat teaching scenario -- keep it fast and loud, and use the Food Fight
  property-damage table on every miss to keep the store chaotic. Do not let the runners get bogged down
  in roleplaying; the gang wants a fight and gets one within a page of the team walking in.
- Supernova: the TekLon extraction (Milk Run) is deliberately the easiest run the team will ever pull
  -- lean into the paranoia that easy jobs invite rather than adding real opposition. Save the actual
  danger for Four Corners, where the Red Samurai and the cyberzombie should feel like a serious step up
  in threat level.
- Supernova: Villiers and Lanier must not die, whatever the runners try at the penthouse -- escalate
  defenses (gas, wards, spirits) rather than ever letting a fight there go the runners' way.
- Site of Desecration: decide the Old One's true motive before the table sits down (curiosity about the
  wider world, as written, or something darker) -- his tests of the runners should telegraph that motive
  even while he plays naive in front of Kaztok.
- Site of Desecration: the Pentagon's priorities (reputation and a working trade deal) are not the same
  as the runners' -- use Breetva to keep pulling the group back toward a negotiated outcome if the table
  wants to shoot its way through Kaztok's camp.
- Karma awards are explicit in the book: Food Fight 2 (1 survive, 1 facing the Chiller Thrillers);
  Supernova 2 base plus up to 3 more (threat level, not harming Villiers/Lanier, killing the
  cyberzombie); Site of Desecration 2 base plus up to 6 more (threat level 1-3, surviving the Old One's
  tests 1-3).
"""
