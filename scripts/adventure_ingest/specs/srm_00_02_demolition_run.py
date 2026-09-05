# SRM 00-02 Demolition Run (FanPro/WizKids, 2004, SR3) -- campaign order #40. Rural Snohomish
# (the DocWagon pharmaceutical plant and the Wadsworth farm next door) and Downtown Seattle (the
# Sheraton Towers at Sixth and Pike, Paladin's boardroom).
# SETTING NOTE: Seattle, not Denver. The facility is "in a rural part of Seattle", the meet is at
# Sixth and Pike, and New Seattle is cited as the area reference. Denver appears exactly once, as
# Saint James's parting line: "take a holiday if you like -- I understand Denver's a charming city
# for the visitor." Every location row is city "Seattle".
# Dating: no in-world date is given; 2064 for the same reasons as SRM 00-01 (SR3, published 2004,
# the 2060s explicitly named as the period). The run itself takes 24 hours if the team wants the
# bonus and 48 at the outside; the last supply delivery to the plant was five days before the meet,
# the next is in 48 hours.
# Book editing inconsistencies noted on the affected rows: the introduction calls the module's
# playing aids "SRM00-01B, Demolition Run Playing Aids" when they are SRM00-02B; the security
# operator's stat block prints two initiative lines stacked ("4+1d6 [5+2d6]3+1d6 [4+2d6]"); the
# Cast of Characters leaves editorial placeholders in place ("[*include notes for Auto-injector]");
# Struthers is "Dr. Struthers, his assistant and chief operations officer" in the fiction and
# "Bob Struthers" of "the Marketing department" two paragraphs later; and File H is flagged as
# "relevant in a future mission" that the Season 0 modules never deliver.
# Source text: docs/Adventures/text/SRM00-02A_demolitionrun.txt (21 pages) and
# docs/Adventures/text/SRM00-02B_demolitionrun.txt (player aids, maps and forms, 11 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "SRM 00-02 Demolition Run"
ORDER = 40
SOURCE = "SRM00-02A_demolitionrun.pdf, pp. 3-21; SRM00-02B_demolitionrun.pdf (Player Aids), pp. 3-11"
YEAR = "2064"

SYNOPSIS = """
**Dr. Fredericks**, CEO of **Paladin Medical Technologies**, has smashed a datapad across a marble
boardroom table hard enough to open his own COO's face. Paladin has lost three contracts in a
month -- Seattle General, then the Salish border patrol -- 1.5 million nuyen a time, all of them in
the pharmaceutical supply division, all of them to a bidder who came in ten percent under Paladin's
own numbers within hours of Paladin submitting them. At the rate they are going they are out of
business inside a year.

**Katey Nagahara** found the answer and **Bob Struthers** found the mechanism. **DocWagon** has put
up a fully automated pharmaceutical plant in the rolling hills of Snohomish, discovered it can make
patches and meds far faster than DocWagon itself consumes them, and started dumping the surplus on
the Seattle market. An enterprising decker made a timely offer and sold DocWagon a walk through
Paladin's JSR database -- operating figures, contract charges, everything. That is how the bids
keep landing ten percent low. Fredericks tells his Special Security Director, **Brian Wallace**,
over the intercom that it would really help Paladin if that facility no longer existed, and that he
hopes to sleep well soon. Wallace, whose job is to make such dreams come true without Paladin's
fingerprints anywhere near them, picks up the telecom and calls a real saint of a man.

**Saint James** is a new fixer with an old resume: until recently he was a shadowrunner and the
bodyguard of one of the most successful fixers in Seattle, until she was forcibly retired. Clipped
British accent, impeccable manners, Cerebral Booster 2 behind the charm. He books a private meeting
room at the **Sheraton Towers** at Sixth and Pike, lets the hotel do his security screening for
him, sets out real coffee, and offers the runners 2,500 nuyen each plus 2,000 more if the plant is
rubble inside 24 hours. Mr. Johnson calls himself **Smithers** and says he is from Universal
Omnitech; a lucky corporate contact roll gets the truth.

The plant is the run. Four meters of slatted cyclone fence and razor wire on high ground a mile
from anything, an anti-air radar dish in the front yard and three six-round missile launchers in
the back, five human guards and a troll with reusable auto-injectors full of Jazz, a security
operator in the control shed running the cameras and a hunting rifle and a scanner tuned to the
runners' own radio traffic, and an eighteen-year-old **security mage** who has warded the break
room at Force 3 purely for the practice, which is exactly the sort of thing that makes a team
believe the break room matters. Reinforcements are thirty minutes out. The neighbouring farmer,
**David Wadsworth**, will tell a polite team almost everything, and the Matrix host will tell a
decker the rest -- including a scrambled file marked only **H**.
"""

TIMELINE = """
- **Over the past month** -- Paladin loses three pharmaceutical supply contracts, Seattle General
  and the Salish border patrol among them, each worth about 1.5 million nuyen in revenue.
- **Some time before that** -- DocWagon builds the Snohomish plant on land previously owned by
  Shiawase; two months of construction, most of it spent digging the basement out, the rest
  assembled from prefabricated duraplast pieces.
- **Recently** -- an enterprising decker cracks Paladin's JSR database and sells DocWagon its
  operating figures and contract charges; DocWagon starts undercutting by ten percent.
- **Days before the meet** -- Struthers backtracks the access logs and identifies the intrusion;
  Katey Nagahara identifies DocWagon and then the Snohomish plant. Fredericks explodes in the
  boardroom, then gives Wallace the order over the intercom.
- **Five days before the meet** -- the plant's last weekly supply delivery.
- **Meet day, early evening** -- the call: a cultured British voice, the Sheraton Towers, Sixth and
  Pike, 9 PM sharp, the Saint James party.
- **9 PM** -- weapons screening, private elevator, the briefing, 1,000 nuyen of trust and a job.
- **The next 24 hours** -- legwork, surveillance across the midnight / 8 AM / 4 PM shift changes,
  the farmer, the City Planning blueprints, the Matrix run. The next supply delivery is 48 hours
  out, so the plant is low on raw materials throughout.
- **The hit** -- guards neutralized or circumvented, four demolition packs placed on Demolitions
  (4) locations, five minutes to clear the fence, then the plant goes up loudly.
- **Thirty minutes after any alarm** -- DocWagon reinforcements arrive: six more guards and a
  security magician.
- **Afterwards** -- back to the Sheraton Towers, payment, a toast, and "I understand Denver's a
  charming city for the visitor."
"""

ORGS = [
    {
        "name": "Paladin Medical Technologies",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Seattle",
        "summary": "Mid-tier Seattle pharmaceutical and medical supplier being undercut into extinction by DocWagon, and the run's real employer.",
        "description": (
            "A Seattle medical technology corporation with a pharmaceutical supply division, a "
            "marketing arm, a clinic staffed by a dozen or so technicians, and a Special Security "
            "Directorate whose job is to solve problems without Paladin's name appearing anywhere "
            "near them. It is nowhere near triple-A: it competes for hospital and government supply "
            "contracts against the likes of DocWagon and loses them one at a time. Three contracts "
            "have gone in the past month, Seattle General and the Salish border patrol among them, "
            "each about 1.5 million nuyen in lost revenue, and the CEO's own estimate is that "
            "another failure means dropped shifts and layoffs and that the company is a year from "
            "the wall. Boardroom culture is set by Dr. Fredericks personally: he smashed a datapad "
            "on the marble table hard enough to lacerate his chief operations officer's face and "
            "arms, and everybody in the room understood that the injury was the point."
        ),
        "notes": (
            "Leadership: Dr. Fredericks (CEO, 'the old man'), Dr. Bob Struthers (assistant and "
            "chief operations officer, who traced the JSR database intrusion), Katey Nagahara "
            "(contract intelligence, who identified DocWagon and then the Snohomish plant), Brian "
            "Wallace (Special Security Director, and Mr. Johnson for this run under the name "
            "Smithers). Plot role: Paladin is the client and must never be connected to the job. "
            "Wallace hires through Saint James at arm's length and presents himself as being from "
            "Universal Omnitech; only a Corporate Etiquette (4) roll of 8 successes gets 'Ah, yes, "
            "Smithers. He's a Johnson for Paladin Medical Technologies -- his real name is "
            "Wallace.' Aftermath: the plant's destruction badly dents the supply of certain "
            "medicines and pharmaceuticals across the sprawl and buys Paladin the time to challenge "
            "DocWagon on its own ground. Nothing in the module stops a GM from having DocWagon work "
            "the same chain backwards later."
        ),
        "enemies": ["DocWagon"],
    },
    {
        "name": "Seattle City Planning Department",
        "org_type": "government agency",
        "tier": 2,
        "headquarters": "Seattle Metroplex civic offices, Downtown",
        "summary": "Metroplex planning authority whose public website sells the original blueprints of any permitted building for 250 nuyen.",
        "description": (
            "The metroplex's civic planning authority, which keeps the permit record and the filed "
            "construction blueprints for buildings across the sprawl and makes them available to "
            "the public over the Matrix for a fee. It is unglamorous, entirely legal, and one of "
            "the most useful shadow resources in Seattle: anything that was built with a permit has "
            "its bones on file somewhere in the department's archive."
        ),
        "notes": (
            "Play use: the original blueprints of the DocWagon Snohomish plant can be pulled from "
            "the department website with a Computer (6) test at a cost of 250 nuyen -- no Matrix "
            "run required, and no alarm raised. What the runners get is the ORIGINAL blueprint "
            "(player aid, SRM00-02B p.4), not the current layout: it shows the two levels and the "
            "prefabricated shell but nothing DocWagon has installed since, which is why the Master "
            "Map is only obtainable astrally. A cheap, safe, legwork-rewarding option that new "
            "players routinely overlook."
        ),
    },
]

LOCATIONS = [
    {
        "name": "DocWagon Snohomish Pharmaceutical Facility",
        "location_type": "corporate facility",
        "city": "Seattle",
        "district": "Snohomish (rural)",
        "security_level": "Corporate High Security",
        "controlling_org": "DocWagon",
        "summary": "Automated drug plant on high ground in the Snohomish farmland, fenced, missile-defended, and the target of the run.",
        "description": (
            "An automated pharmaceutical plant sitting on high ground in the rolling farm country of "
            "Snohomish, about a mile from any other building, reached by a single access road and "
            "well outside regular Lone Star patrol routes. A four-meter cyclone fence topped with "
            "razor wire rings it, with duraplast slats woven vertically through the chain links to "
            "stiffen the fence and block line of sight (barrier 10, extending a meter below grade "
            "against digging; climbing is Athletics (6) and 6L from the wire, half impact armor). "
            "Signs warn that it is private property. Just inside the gate is a flat-roofed "
            "outbuilding serving as entry post and shipping/receiving -- a short hallway and a "
            "storage and receiving dock, a personnel door and an overhead rolling door on each "
            "side, walls barrier 12, doors barrier 10, a rating 5 maglock in each door rather than "
            "the frames. Beyond it is one large yard of mown grass, kept by an automated lawn drone, "
            "with an asphalt drive to a rolling door in the side of the main building. The main "
            "building is prefabricated duraplast, flat-roofed, walls barrier 12, doors barrier 10, "
            "windows painted black at barrier 6, exterior maglocks rating 4 and habitually left "
            "open. A ferrocrete platform in the front yard carries a rotating radar dish; three more "
            "at the rear carry missile launchers with six anti-air missiles apiece. Two heavily "
            "reinforced raw-material tanks (barrier 16, harmless contents) stand against one wall, "
            "and a windowless control shed sits at the very back."
        ),
        "notes": (
            "Maps: original blueprints SRM00-02B p.4 (City Planning, Computer (6), 250 nuyen), "
            "current exterior p.5 (obtainable by getting close and looking through the fence slats, "
            "or by a drone before the SAMs kill it), master map p.6 (astral recon only), Matrix "
            "camera views p.7. MAIN FLOOR: automated manufacturing lines, storage tanks, supply "
            "bins, conveyors and auto-factories, all barrier 12 and all usable as cover; the noise "
            "gives +4 to hearing-based Perception. Lighting is on automatic circuits neither side "
            "can cut. Ceilings 3 meters (troll-friendly). Interior walls and doors barrier 10, "
            "interior doors unlocked and a Simple Action to open -- which the guards exploit (one "
            "opens the door, another fires through on a held action, the first shuts it again). Also "
            "on this floor: a guard break room with an attached toilet, a circular table, six "
            "chairs, two vending machines and a security case holding two AK-97s with Gas-Vent III, "
            "shock pads, low-light scopes and internal smartguns plus ten clips (3,800 nuyen each, "
            "Complex Action to open, keyed to guard credsticks); a storage room with stairs down; "
            "and recharge units for two IWS DLK MK 8 forklift drones (Hand 4/4, Speed 20, Body 3, "
            "Armor 4, Pilot 2, hydraulic lift equal to Strength 20, no weapons, excellent cover, "
            "useless to a runner since they take direction from the facility computer). BASEMENT, "
            "reached by the stairs or the automated elevator platform inside the rolling door: an "
            "unused storage room, liquid bulk storage (the waist-high middle tank gives partial "
            "cover), bulk parts storage where the troll guard works, and a crawlspace equipment room "
            "holding the power regulators, air conditioning and the facility mainframe. REAR YARD: "
            "the launchers are not portable, but Gunnery B/R (6) partially disassembles one so it "
            "can be aimed at the plant -- take the control shed as well and the missiles destroy the "
            "facility utterly. CONTROL SHED: no windows, two outward-opening doors on rating 4 "
            "maglocks, the missile control electronics, the security operator's duty station and "
            "camera panel, a roof hatch onto the flat roof (a sniping position over the back yard), "
            "and the lawn drone's recharging bay. GARRISON: five human guards, one troll guard, one "
            "security operator, one security mage, twenty-four hours a day; one guard usually in "
            "shipping, one patrolling the front and one the rear on a ten-minute cycle. Guard "
            "Perception outward through the slats is at +4. Shift change by DocWagon truck at "
            "midnight, 0800 and 1600, half an hour long, doubling as the daily product pickup by "
            "automated forklift; spotting that the men leaving are not the men who entered is "
            "Perception (10) needing four successes, -1 per level of Mnemonic Enhancer, -2 with "
            "vision enhancement, -4 if on site or astrally present. A shift change replaces every "
            "member of the garrison -- including a security mage the team thought it had dealt "
            "with. Aerial drones are engaged by the automated defenses: Gunnery (Launch Weapons) 4, "
            "missile Intelligence 4, 12D vehicular. Loot: 2D6 medkits at 200 nuyen and twice that "
            "many medkit supply refills at 50 nuyen and half a kilo each. Reinforcements thirty "
            "minutes after any alarm: six guards and a security magician (SR3 Combat Mage stats), "
            "sirens audible in time to run. Demolition: four packs of commercial explosive on "
            "pre-set timers, each placement a Demolitions (4) test, five minutes to clear out."
        ),
    },
    {
        "name": "Sheraton Towers",
        "location_type": "hotel",
        "city": "Seattle",
        "district": "Downtown (Sixth and Pike)",
        "security_level": "Corporate Standard",
        "summary": "Upmarket Downtown hotel at Sixth and Pike where Saint James runs his meets and lets the house do his screening.",
        "description": (
            "A high-end hotel at Sixth and Pike in Downtown Seattle, with doormen who visibly want "
            "to throw shadowrunners back into the street until the name Saint James is mentioned, "
            "at which point they become extremely helpful. Guests are run through security, then "
            "escorted to a private elevator and up to a floor of private meeting rooms; the escorts "
            "take deliberate care that visitors do not stray from the path and that as few paying "
            "guests as possible get a look at them. The meeting room itself is genuinely handsome: "
            "synthleather-upholstered executive chairs around a large synthoak table, several of "
            "them sized for larger metahumans, and a side table with several pots of what smells "
            "very much like real coffee."
        ),
        "notes": (
            "Security: doormen have Intelligence 5 and run every guest through an architectural "
            "weapons detection system of rating 6 (SR3 p.237) -- roll 6 dice against a weapon's "
            "concealability, one success detects it. Anyone caught is asked to surrender the weapon "
            "to building security; refusal means no entry. Behind that, a house security rigger has "
            "been watching the team since they set foot on hotel property and controls hidden "
            "weapon mounts: attack the guards and he shoots the offender to pieces without warning. "
            "A runner who breaks away to roam the hotel is sealed between two airtight doors, gassed "
            "with Neurostun-VII, stripped of the gas, carried out by the guards and dumped on the "
            "pavement -- for that character the adventure is over. Saint James chose the venue "
            "partly to impress the runners with the setting and the refreshments, and partly "
            "because letting the hotel screen them saves him hiring security of his own. He is "
            "also here for the debrief and payment at the end of the run."
        ),
    },
    {
        "name": "Paladin Medical Technologies Headquarters",
        "location_type": "corporate headquarters",
        "city": "Seattle",
        "district": "Seattle metroplex",
        "security_level": "Corporate Standard",
        "controlling_org": "Paladin Medical Technologies",
        "summary": "Paladin's offices, boardroom and in-house clinic, where the order to level the DocWagon plant is given.",
        "description": (
            "The corporate offices of Paladin Medical Technologies: a boardroom with a marble "
            "tabletop, an executive floor wired with an intercom the CEO uses instead of walking, "
            "the marketing and pharmaceutical supply divisions, and an in-house clinic with a dozen "
            "or so technicians on hand -- which on the day of the boardroom explosion is where the "
            "chief operations officer goes to have plastic and glass picked out of his face and "
            "arms. The Special Security Director's office is on the same floor and is where the "
            "call to Saint James is placed, over the anonymity of the telecom."
        ),
        "notes": (
            "Pure background in the module -- the runners are never sent here and are never meant "
            "to learn Paladin's involvement at all. It exists for the GM who has to answer the "
            "question 'so who is really paying us?', for a team that back-traces Smithers, and as "
            "the obvious setting for a later reprisal plot: DocWagon lost a plant and will "
            "eventually want to know why. The JSR database that the enterprising decker cracked "
            "lives here, and the access logs that Struthers backtracked are still on file."
        ),
    },
    {
        "name": "Wadsworth Farm",
        "location_type": "farm",
        "city": "Seattle",
        "district": "Snohomish (rural)",
        "security_level": "Low Security",
        "summary": "Bioengineered-wheat agri-farm neighbouring the DocWagon plant; David Wadsworth's land and the team's best human intelligence.",
        "description": (
            "One of the working agricultural holdings in the Snohomish farmland around the DocWagon "
            "plant, growing bioengineered wheat on contract to one of the agricorps. It is close "
            "enough to the compound that its owner has watched the whole thing go up over two "
            "months, notices every truck that comes and goes on the access road, and has heard "
            "rifle shots from inside the fence often enough to have an opinion about the make of "
            "rifle. There is no gate guard and no security to speak of; there is a middle-aged "
            "farmer who will talk to anyone who talks to him properly."
        ),
        "notes": (
            "The 'Negotiation' optional scene, and the single best legwork source in the module for "
            "a team with a face. Approach it by day and David Wadsworth is out on the land. What he "
            "gives up: the plant belongs to DocWagon; it was built in two months on land previously "
            "owned by Shiawase, mostly prefabricated, with most of the time spent digging out the "
            "basement; it has two levels; a truck comes every eight hours, men get out, go in, and "
            "a different-looking group comes out half an hour later; a second large truck comes "
            "about weekly and stays an hour, the last one five days ago; the fence is not "
            "electrified and critters get in; he has heard rifle shots he would put on a Remington "
            "750 hunting rifle; and no DocWagon inspection team has ever stopped there. Treat him "
            "as a hayseed and the well goes dry."
        ),
    },
]

NPCS = [
    {
        "name": "Saint James",
        "role": "Cultured British ex-runner turned fixer; hires and pays the team, and will set the charges himself if nobody else can",
        "archetype": "Fixer",
        "title": "\"The Saint\" -- independent fixer, Seattle",
        "race": "Human",
        "gender": "Male",
        "nationality": "British",
        "connection": 4,
        "description": (
            "A tall man in a grey business suit with a clipped British accent and impeccable "
            "manners, who greets a room full of armed strangers with 'Ah, greetings. My name is "
            "Saint James. Please, join me,' waves them at synthleather chairs and real coffee, and "
            "waits for them to be comfortable before he talks business. Two burly bodyguards stand "
            "like statues in the corner throughout. He is amused rather than offended by attempts "
            "to out-negotiate him, genuinely interested in the runners' account of the job "
            "afterwards, and prone to trailing off mid-reminiscence: 'Reminds me of the old days, "
            "running for -- ah, but you don't need to hear my old war stories.' His phone manner is "
            "the same: 'Do be on time, I so dislike the fashionably late.'"
        ),
        "background": (
            "Until recently Saint James was a shadowrunner himself, and bodyguard to one of the "
            "most successful fixers in Seattle. When that fixer was forcibly retired he decided to "
            "make a go of the business on his own, and has been surprisingly successful at it: the "
            "accent, the manners, the charisma and the negotiating skill make his deals profitable, "
            "and the runner's skills and contacts underneath make sure the deals are kept. He "
            "remembers where he came from and looks after the people who work for him -- he will "
            "walk into a cleared facility and set demolition charges for a team that has no "
            "demolitions expert, and refuse to charge them for it, on the grounds that they need "
            "every nuyen and Smithers is paying him enough anyway. Street legwork at 6 successes "
            "brings the loose end into view: 'He used to work for that one fixer, what was her name "
            "again...' -- almost certainly the fixer whose death opens SRM 00-01 Mission Briefing."
        ),
        "notes": (
            "No full stat block; the module gives Intelligence 8 (natural 6 plus Cerebral Booster "
            "2) and Negotiation 6, and notes he was a shadowrunner with years of experience who "
            "will take cover and fight competently if attacked, backed by his two bodyguards. "
            "Negotiation: each net success in the runners' favor adds 500 nuyen to the base; net "
            "successes in his favor are ignored. Terms he offers: 2,500 nuyen each, 2,000 more per "
            "runner if the plant is down inside 24 hours, 48 hours at the outside; demolition packs "
            "supplied; guards need not be killed; Lone Star response about ten minutes; air "
            "approach not recommended because of the SAM pods; reprisal expected to be low unless "
            "the team is unprofessional. He will not name Mr. Johnson. Legwork on him: Etiquette "
            "(Street) 4 -- new fixer, good to work for, takes care of his people; Etiquette "
            "(Corporate) 4 -- honorable gentleman, play straight and he will too, and at 7 "
            "successes, 'I understand he's working with a gentleman named Smithers currently.' "
            "Attack him and he blackballs the team out of the shadows entirely: doors close, nobody "
            "talks, the careers are over. He is the campaign's on-ramp fixer and should survive."
        ),
        "contact_skills": ["Shadow work and Johnsons", "Demolitions", "Corporate contract gossip"],
    },
    {
        "name": "Brian Wallace",
        "role": "Paladin's Special Security Director; Mr. Johnson for the run under the alias Smithers of Universal Omnitech",
        "archetype": "Corporate Security Executive",
        "title": "Special Security Director, Paladin Medical Technologies (alias \"Smithers\", Universal Omnitech)",
        "race": "Human",
        "gender": "Male",
        "organization": "Paladin Medical Technologies",
        "connection": 4,
        "description": (
            "The narrator of the module's opening fiction: the man seated at the far end of the "
            "boardroom table, far enough from Dr. Fredericks to be spared the datapad shrapnel, who "
            "notices exactly who was not so lucky and files it away. He answers his CEO's carefully "
            "deniable phrasing with equally careful phrasing of his own -- 'Of course, sir. I "
            "understand completely. I hope you will be able to sleep well soon' -- and then makes "
            "the call. In the shadows he is Smithers, a soft-spoken corporate man from Universal "
            "Omnitech, and he has no intention of meeting the runners face to face."
        ),
        "background": (
            "Wallace has been in the loop on the DocWagon problem from the start, and his job as "
            "Special Security Director is to see that the CEO's dreams come to fruition without "
            "the direct involvement of Paladin or any of its subsidiaries. He calls Saint James "
            "because he knows the former runner to be competent and knowledgeable, and because "
            "hiring through a fixer with a reputation is cheaper than owning the consequences. The "
            "Universal Omnitech cover is well chosen: UniOmni is a biotech firm widely rumored to "
            "be moving into the emergency medical services business in Seattle, which makes it a "
            "perfectly plausible enemy for DocWagon to blame."
        ),
        "notes": (
            "No stat block. The runners are not meant to meet him at all -- Saint James stands "
            "between them, and Mr. Johnson does not wish his identity known. Piercing the cover "
            "takes a Corporate Etiquette (4) legwork roll: 4 successes gets the name Smithers, 5 "
            "gets Universal Omnitech, and 8 gets the whole thing, 'He's a Johnson for Paladin "
            "Medical Technologies -- his real name is Wallace.' The Universal Omnitech line at 4 "
            "successes on the UniOmni table (they are looking to get into the DocWagon business) is "
            "an explicit red herring, planted to make the cover hold. A team that identifies "
            "Wallace has leverage worth far more than the run fee -- and a very good reason not to "
            "use it."
        ),
        "contact_skills": ["Corporate security and deniable contracting", "Seattle pharmaceutical industry"],
    },
    {
        "name": "Dr. Fredericks",
        "role": "CEO of Paladin Medical Technologies; orders the plant destroyed without ever saying so",
        "archetype": "Corporate Executive",
        "title": "Chief Executive Officer, Paladin Medical Technologies",
        "race": "Human",
        "gender": "Male",
        "organization": "Paladin Medical Technologies",
        "connection": 4,
        "description": (
            "'The old man'. He opens the module by screaming 'This is the third contract we've lost "
            "in the past month! Another 1.5 million nuyen lost in revenues!' and smashing a datapad "
            "against a marble tabletop hard enough that the fragments open his own COO's face and "
            "arms, then glares down the half dozen executives in front of him demanding an "
            "explanation. He tells his contracts analyst to 'find out!' and reminds the room that "
            "if it happens again he will be dropping shifts and laying off personnel, and that they "
            "can all guess where he will start. In private he is careful: the order to level a "
            "rival's plant is delivered as a wish. 'I think it would really help out Paladin if "
            "that facility were to no longer exist. If only there was a way to make such dreams a "
            "reality, eh, Wallace?'"
        ),
        "background": (
            "Fredericks has every reason to be upset. Paladin has lost its biggest contracts one "
            "after another, all in the pharmaceutical supply division -- Seattle General first, "
            "then the Salish border patrol -- and by his own reckoning the company is out of "
            "business within a year at this rate. He is not a stupid man; he simply knows exactly "
            "how to phrase an instruction so that no recording of it convicts him of anything."
        ),
        "notes": (
            "No stat block; background only. He never appears on screen during play. His function "
            "is to establish that the run is a corporate execution ordered from the top, that the "
            "employer is desperate rather than cynical, and that everyone below him is frightened "
            "enough to make bad decisions. Useful to a GM continuing the thread: DocWagon losing a "
            "plant to a competitor's deniable contractor is exactly the sort of thing that "
            "eventually reaches an executive who is not careful about phrasing."
        ),
    },
    {
        "name": "Bob Struthers",
        "role": "Paladin's COO, cut open by the CEO's datapad, who traced the intrusion into the company's JSR database",
        "archetype": "Corporate Executive",
        "title": "Chief Operations Officer and assistant to the CEO, Paladin Medical Technologies",
        "race": "Human",
        "gender": "Male",
        "organization": "Paladin Medical Technologies",
        "connection": 3,
        "description": (
            "Seated near enough to Fredericks to catch the full brunt of the datapad, and left with "
            "lacerations to the face and arms from the flying plastic and glass -- nothing the "
            "company clinic cannot repair, though as the narrator notes, the emotional scars will "
            "be harder to heal. He answers by valiantly taking some of the old man's rage onto "
            "himself and redirecting it: 'Sir, I believe that this is not a failing of the "
            "Marketing department, but rather the result of a malicious attack against our data "
            "systems.'"
        ),
        "background": (
            "The book calls him 'Dr. Struthers, his assistant and chief operations officer' in one "
            "paragraph and speaks of the Marketing department in the next, which is one of the "
            "module's small internal inconsistencies. Whatever his exact remit, he is the one who "
            "finally backtracked the access logs and discovered an unauthorized access of Paladin's "
            "current JSR database, from which the intruder retrieved the company's operating "
            "figures and its charges on various customer contracts -- the leak that lets DocWagon "
            "bid ten percent under Paladin every single time."
        ),
        "notes": (
            "No stat block; background only, and never met during play. He is the reason anyone at "
            "Paladin knows this is sabotage rather than incompetence, and by extension the reason "
            "the run exists. A GM extending the plot has an obvious hook in him: the enterprising "
            "decker who sold DocWagon that data is still out there, unnamed and unpunished, and "
            "Struthers has the logs."
        ),
    },
    {
        "name": "Katey Nagahara",
        "role": "Paladin contract analyst who traced the losses to DocWagon and located the Snohomish plant",
        "archetype": "Corporate Analyst",
        "title": "Contract intelligence, Paladin Medical Technologies",
        "race": "Human",
        "gender": "Female",
        "organization": "Paladin Medical Technologies",
        "connection": 3,
        "description": (
            "Seated at Wallace's right hand in the boardroom with the anxiety coming out of her "
            "pores -- and yet her voice is strong when Fredericks turns on her and demands to know "
            "how Paladin lost the Salish border patrol contract. 'It appears that a new bid was "
            "entered shortly after our own -- the new bidder was able to supply the necessary drugs "
            "in the desired amounts for almost ten percent less than us. My sources cannot "
            "ascertain the winner of the contract.' Told to find out, she does."
        ),
        "background": (
            "Katey runs what the fiction calls her 'sources': whatever mix of legitimate market "
            "intelligence and quiet purchases lets a mid-tier corporation see who is bidding "
            "against it. Within days of the boardroom scene she has established that DocWagon is "
            "the culprit behind Paladin's collapsing market share, and then found the reason -- "
            "the recently erected automated pharmaceutical factory in the rolling hills of "
            "Snohomish, running far past DocWagon's own needs and dumping the surplus on the "
            "Seattle market at a price nobody else can match."
        ),
        "notes": (
            "No stat block; background only, and never met during play. She is the one person at "
            "Paladin who has actually done competent shadow work, and the natural NPC for a GM who "
            "wants to bring Paladin back on screen later -- as the handler who inherits Wallace's "
            "files, as a source the runners can turn, or as a target once DocWagon starts asking "
            "who was interested enough in the plant to find it."
        ),
        "contact_skills": ["Pharmaceutical contract intelligence", "Corporate bid and market data"],
    },
    {
        "name": "David Wadsworth",
        "role": "Snohomish agri-farmer next to the plant; the module's best legwork source, if the runners do not condescend",
        "archetype": "Farmer",
        "title": "Agri-farmer, bioengineered wheat, Snohomish",
        "race": "Human",
        "gender": "Male",
        "age": 45,
        "nationality": "UCAS",
        "connection": 2,
        "description": (
            "A man in his middle forties who has farmed all his life and talks very laconically, "
            "which reads as hayseed to anyone in a hurry. He is nothing of the kind: he is "
            "intelligent, knowledgeable about technology and closely observant of changes around "
            "his land. He is also perfectly capable of noticing when he is being patronized, and "
            "the module says so flatly -- being laconic 'does not make him stupid... until the "
            "player characters decide to treat him as one.'"
        ),
        "background": (
            "Wadsworth grows bioengineered wheat on contract to one of the agricorps on land "
            "adjoining the DocWagon compound. He watched the plant go up over two months on ground "
            "that used to belong to Shiawase, watched most of that time go into digging the "
            "basement out and the rest into bolting prefabricated pieces together, and has been "
            "watching the trucks ever since."
        ),
        "notes": (
            "The Negotiation optional scene; find him on the land during the day. Everything he "
            "gives up: DocWagon owns it; two months to build, on former Shiawase land, prefab, most "
            "of the time spent excavating; two levels, a basement and a ground floor; a truck every "
            "eight hours, men in, half an hour, men out, drive away (he is watching shift changes "
            "without knowing it); another large truck about weekly, staying an hour, the last one "
            "five days ago; the fence is not electrified and critters get through; he has heard "
            "rifle shots inside the fence and would put them on a Remington 750 hunting rifle (the "
            "security operator's); and no DocWagon inspection team has ever stopped there -- which "
            "is exactly why the surprise-inspection ploy gets the team ambushed. Handled well he "
            "is worth more than the Matrix run; handled badly he says nothing at all."
        ),
        "contact_skills": ["Snohomish farmland and back roads", "Local traffic and who comes and goes"],
    },
    {
        "name": "DocWagon Snohomish Shift Leader",
        "role": "Senior guard of the plant's five-man human detail; the man who names a price to look the other way",
        "archetype": "Corporate Security Guard",
        "title": "Shift leader, DocWagon Snohomish facility security detail",
        "race": "Human",
        "gender": "Male",
        "organization": "DocWagon",
        "connection": 2,
        "description": (
            "Unnamed in the module, and the only one of the five human guards with lines of his "
            "own. A trained corporate guard in an armor jacket with a smartlinked HK 227 and a "
            "reusable auto-injector loaded with Jazz, who spends half his shift checking machinery "
            "and doing light repairs and the other half in the break room playing cards -- which is "
            "why the whole detail negotiates better than corporate guards usually do. Approached "
            "with money he does not bluster; he names a figure, listens to the counter-offer, and "
            "if the number is wrong he picks up the phone."
        ),
        "background": (
            "DocWagon recruits its Snohomish detail as technician-guards: they repair the automated "
            "lines as their day job and defend the plant as their other one. Because the site is "
            "remote, the company skipped reflex enhancement and implanted reusable auto-injectors "
            "instead, giving each of them one dose of Jazz for emergencies -- cheaper than wired "
            "reflexes and, in the company's judgment, sufficient. The men know what the drug costs "
            "them and do not use it until intruders are actually on the grounds."
        ),
        "notes": (
            "Guard stats (all five humans): B5 Q5[7] S5 C4 I4 W4, Ess 5.0, Reaction 4(5), Init "
            "4+1D6 [5+2D6 on Jazz], Combat Pool 6[7], Karma TR, Pro 3/Trained. Assault Rifles 5, "
            "SMG 5, Unarmed 4, Athletics 4, Stealth 3, Etiquette 3, Negotiation 4, Electronics 3, "
            "Electronics B/R 3, Computers 3, Computers B/R 3, Biotech 3; DocWagon Operational "
            "Procedures 4, Security Procedures 4, DocWagon Personnel 3, Card Games 4. Cyber: "
            "smartlink, hearing damper, datajack, reusable auto-injector. Armor jacket 5/3. HK 227 "
            "with external smartgun, 2 clips normal and 2 gel. Rating 1 transceiver with rating 2 "
            "broadcast encryption, medkit, Stim 3 and trauma patches. Jazz lasts 1D6 x 10 minutes: "
            "+2 Quickness (and Reaction) and +1D6 Initiative. BRIBE: get the guard roster (Matrix "
            "Files test) or otherwise reach him and he wants 15,000 nuyen to let the plant be "
            "demolished, provided it can be made to look as though the guards had no part in it; "
            "standard Negotiation shifts it 1,000 nuyen a net success, and he will not go below "
            "10,000. Refuse and he reports the approach, and the garrison roughly doubles. TACTICS: "
            "the detail waits and ambushes rather than charging, takes cover, uses aim actions, "
            "throws handfuls of inert white process residue in eyes, and works the unlocked "
            "interior doors -- one opens, one fires on a held action, the first shuts it again. "
            "They are not ordered to capture anyone; lethal force is authorized by the operations "
            "manual, and as far as they are concerned the runners are trespassers."
        ),
    },
    {
        "name": "DocWagon Snohomish Troll Guard",
        "role": "The plant's basement muscle, hauling raw materials where no security camera watches",
        "archetype": "Corporate Security Guard",
        "title": "Security guard (basement detail), DocWagon Snohomish facility",
        "race": "Troll",
        "gender": "Male",
        "organization": "DocWagon",
        "connection": 2,
        "description": (
            "Unnamed, and the module's proof that DocWagon is an equal-opportunity employer. He "
            "spends his shift in the basement, manhandling delivered materials into the storage "
            "tanks and parts hoppers when they run low, with an Enfield AS-7 slung. Large, and "
            "psychologically reliant on being large: he is an intimidator rather than a negotiator "
            "and genuinely enjoys frightening an opponent into backing down before anything has to "
            "be fired."
        ),
        "background": (
            "Part of the same technician-guard detail as the five humans, on the same terms -- the "
            "same implanted auto-injector, the same one dose of Jazz, the same card games in the "
            "break room upstairs when he is not needed below."
        ),
        "notes": (
            "Stats: B9(10) Q4[6] S8 C2 I3 W3, Ess 5.0, Reaction 4(5), Init 3+1D6 [4+2D6 on Jazz], "
            "Combat Pool 5[6], Karma TR, Pro 3/Trained. Assault Rifles 5, Shotguns 5, Unarmed 6, "
            "Athletics 3, Stealth 4, Etiquette 2, Intimidation 4, Electronics 3, Computers 3, "
            "Biotech 3; DocWagon Operational Procedures 4, Security Procedures 4, DocWagon "
            "Personnel 3, Card Games 4. Cyber: smartlink, hearing damper, datajack, reusable "
            "auto-injector. Armor jacket 5/3. Enfield AS-7 with internal smartgun, 2 clips slug and "
            "2 flechette (8D(f)). Rating 1 transceiver with rating 2 encryption, medkit, Stim 6 and "
            "trauma patches. THE AMBUSH: there are no security cameras in the basement, so a team "
            "that has been tracking the garrison on the monitors will not know he is down there. He "
            "uses cover, takes time to aim, and if the intruders look unarmored he switches to "
            "flechette and empties a burst into them. He is the single most likely thing in the "
            "module to kill a starting character."
        ),
    },
    {
        "name": "DocWagon Snohomish Security Operator",
        "role": "Camera and missile watchstander in the control shed; the reason the guards know the team is coming",
        "archetype": "Security Rigger",
        "title": "Security operator, DocWagon Snohomish facility control shed",
        "race": "Human",
        "gender": "Male",
        "organization": "DocWagon",
        "connection": 2,
        "description": (
            "Unnamed, and by his own job description little more than a nanny to an automated "
            "gunnery system -- so DocWagon has also handed him overwatch of the whole compound. "
            "Long hours of duty with nothing to do have made him inventive about recreation: he "
            "keeps a scoped hunting rifle to shoot animals that get through the fence before they "
            "can gnaw the cables to the anti-air defenses, and a radio scanner he normally uses to "
            "listen to unencrypted Lone Star and DocWagon traffic for entertainment."
        ),
        "background": (
            "Stationed alone in the windowless control shed at the back of the compound with the "
            "missile control electronics, the camera panel, a roof hatch and the lawn drone's "
            "charging bay. Every camera in the facility feeds to his console, which makes him the "
            "detection system for the entire site and the man who calls DocWagon for "
            "reinforcements."
        ),
        "notes": (
            "Stats: B4 Q5[7] S4 C3 I5 W5, Ess 5.7, Reaction 4(5), Init 4+1D6 [5+2D6 on Jazz] (the "
            "book prints two initiative lines stacked here), Combat Pool 7[8], Karma TR, Pro "
            "3/Trained. Rifles 5, Gunnery 5, Unarmed 4, Athletics 3, Stealth 4, Etiquette 3, "
            "Electronics 3, Electronics B/R 3, Computers 3, Computers B/R 3, Biotech 3. Cyber: "
            "datajack, reusable auto-injector. Armor jacket 5/3. Remington 750 Sport Rifle with "
            "rating 1 magnification scope, 20 rounds. Rating 2 transceiver with rating 4 broadcast "
            "encryption, rating 4 scanner, medkit, Stim 3 and trauma patches. PLAY: he will "
            "probably spot intruders the moment they cross a camera's view and warn the guards "
            "inside; he can turn the scanner onto the runners' own comm traffic and feed the "
            "garrison their movements in real time, which is the module's blunt lesson about "
            "encrypted communications; and he can go up through the roof hatch and snipe into the "
            "back yard. He calls DocWagon the moment runners are inside the fence, starting the "
            "thirty-minute reinforcement clock. Taking the shed also takes the missile controls -- "
            "combine that with a Gunnery B/R (6) on a launcher and the facility destroys itself."
        ),
    },
    {
        "name": "DocWagon Snohomish Security Mage",
        "role": "Eighteen-year-old company magician getting practical experience; warded the break room for fun",
        "archetype": "Corporate Mage",
        "title": "Security mage (trainee), DocWagon Snohomish facility",
        "race": "Human",
        "gender": "Male",
        "age": 18,
        "organization": "DocWagon",
        "connection": 2,
        "description": (
            "Unnamed, eighteen years old, a complete neophyte and, in the module's own words, 'more "
            "of a Wiz Kid mage than a real magician'. He is on site because DocWagon wants him to "
            "get practical experience guarding a facility that nobody expects anyone to attack. "
            "Young and very overconfident: presented with a single opposing magician on the astral "
            "he will take the fight; presented with two, or a magician and a spirit, he is back in "
            "his body and shouting for the guards."
        ),
        "background": (
            "To pass the time and stretch his abilities he has thrown a Force 3 ward around the "
            "guards' break room -- purely as practice, and with no idea that the single most "
            "misleading thing he could have done to an astrally scouting shadowrunner is to ward "
            "the one room in the building that contains a table, six chairs, two vending machines "
            "and a gun cabinet."
        ),
        "notes": (
            "Stats: B4 Q5 S3 C5 I5 W6, Ess 6, Magic 6, Reaction 4, Init 4+1D6, Combat Pool 7, Spell "
            "Pool 5, Karma TR, Pro 1/Semi-Trained. Sorcery 5, Conjuring 3, Pistols 3, Unarmed 5, "
            "Stealth 4, Electronics 2, Computers 2, Biotech 3; Magical Threats 3, Sorcery "
            "Background 3, DocWagon Operational Procedures 3. Spells: Clairvoyance 3, Mindlink 2, "
            "Heal 3, Invisibility 4, Armor 3. Lined coat 4/2, Beretta Model 101T with one clip. "
            "PLAY: his real function is to give the team a fright and make them overestimate the "
            "site. Break the break-room ward and he reports it at once and goes astral to look. "
            "With intruders confirmed the guards order him to stay in the break room; he obeys, "
            "then projects and flies the compound astrally, and if challenged by a magician backed "
            "by runners he flees to his body and tells the guards which one of them is the mage. He "
            "also runs Clairvoyance surveillance and shares it by Mindlink with a guard, and casts "
            "Invisibility and runs for the fence if cornered. Remember the shift change: kill or "
            "capture him and the next shift brings a replacement."
        ),
    },
]

ORG_UPDATES = {
    "DocWagon": {
        "notes_append": (
            "SRM 00-02 Demolition Run: DocWagon has erected a fully automated pharmaceutical plant "
            "in the rolling hills of Snohomish, on land bought from Shiawase and built in two "
            "months from prefabricated duraplast pieces, most of that time spent digging out the "
            "basement. It turns out patches and meds far faster and in far greater quantity than "
            "DocWagon's own operations consume, so the company sells the surplus into the Seattle "
            "market -- and, armed with data an enterprising decker lifted from Paladin Medical "
            "Technologies' JSR database, undercuts competitors' bids by about ten percent every "
            "time. That has cost Paladin three major contracts in a month, including Seattle "
            "General and the Salish border patrol, and gets the plant blown up. Garrison: five "
            "human technician-guards, one troll, a security operator and a trainee security mage, "
            "around the clock, relieved by truck at midnight, 0800 and 1600; instead of reflex "
            "enhancement DocWagon implants reusable auto-injectors carrying one dose of Jazz each. "
            "The operations manual authorizes lethal force against intruders, does not require "
            "capture, and instructs the guards to treat any unexpected inspection team as corporate "
            "saboteurs -- there are no DocWagon inspections of this site. Reinforcements are 30 "
            "minutes out: six guards and a security magician. Note the sting in the tail: a wounded "
            "runner who calls DocWagon for retrieval will be treated and then held responsible for "
            "the damage -- policy cancelled and blacklisted at best, prosecution and a long "
            "sentence at worst."
        ),
        "enemies_add": ["Paladin Medical Technologies"],
    },
    "Universal Omnitech": {
        "notes_append": (
            "SRM 00-02 Demolition Run: Paladin's Mr. Johnson poses as 'Smithers of Universal "
            "Omnitech' precisely because the cover is plausible. Corporate legwork (Etiquette "
            "(Corporate) 4) gives: a biotech research firm specializing in biological products but "
            "branching into everything biotech-related (1 success); 'sort of owned by Aztechnology "
            "-- although they're not a subsidiary, the Azzies seem to think UniOmni's their "
            "territory, like an exclusive partner' (2); and at 4 successes the deliberate red "
            "herring, 'I hear they're looking into getting into the emergency medical services "
            "provider business in Seattle. You know, like DocWagon.' UniOmni has nothing to do with "
            "the destruction of the Snohomish plant and is left holding the blame."
        ),
    },
    "Aztechnology": {
        "notes_append": (
            "SRM 00-02 Demolition Run: Seattle corporate gossip holds that Universal Omnitech is "
            "'sort of owned by Aztechnology' -- not a subsidiary, but treated by the Azzies as "
            "their territory and an exclusive partner. That relationship is what makes the "
            "'Smithers of Universal Omnitech' cover story credible to anyone the runners ask."
        ),
    },
    "Shiawase Corporation": {
        "notes_append": (
            "SRM 00-02 Demolition Run: the rural Snohomish parcel on which DocWagon built its "
            "automated pharmaceutical plant was previously Shiawase land. The neighbouring farmer "
            "David Wadsworth remembers the sale and the two-month construction that followed."
        ),
    },
    "Lone Star Security": {
        "notes_append": (
            "SRM 00-02 Demolition Run: the DocWagon plant sits in a rural sector of Snohomish "
            "outside regular Lone Star patrol routes; Saint James estimates a ten-minute response "
            "time to anything that happens there, which is the entire reason the job is feasible. "
            "The plant's own security operator passes his shifts listening to unencrypted Lone Star "
            "and DocWagon broadcasts on a rating 4 scanner."
        ),
    },
    "Salish-Shidhe Council": {
        "notes_append": (
            "SRM 00-02 Demolition Run: the Salish border patrol pharmaceutical supply contract is "
            "the third and most recent contract Paladin Medical Technologies has lost to DocWagon's "
            "ten-percent underbidding, worth about 1.5 million nuyen in revenue. Katey Nagahara's "
            "sources could not even establish who had won it, which is what set Paladin hunting."
        ),
    },
}

LOC_UPDATES = {
    "Seattle General Hospital": {
        "notes_append": (
            "SRM 00-02 Demolition Run: Seattle General was the first of the three big "
            "pharmaceutical supply contracts Paladin Medical Technologies lost in a single month to "
            "a bidder who came in ten percent under their number within hours of the bid being "
            "filed -- DocWagon, running its automated Snohomish plant on stolen figures. The loss "
            "of the plant means the availability of certain medicines and pharmaceuticals across "
            "the sprawl takes a real hit for a while, which lands on hospitals like this one."
        ),
    },
}

NPC_UPDATES = {}

TAG_EXISTING = {}

MATRIX_HOSTS = """
### DocWagon Snohomish plant host

Green-4/8/8/8/8/12. Deliberately soft: the plant holds no important files and only manufactures
standard biotech gear, so DocWagon has not thought it worth serious protection. An inexperienced
decker should get in and out. It is also the single richest legwork source in the module.

| Step | Event |
| --- | --- |
| 4 | Probe-4 |
| 8 | Probe-6 |
| 11 | Tar Baby-6, Passive Alert |
| 14 | Probe-8 |
| 20 | Killer-6, Active Alert |
| 24 | Shutdown |

Tasks and tests:

- **Interior surveillance footage** -- Slave test (hand out the Matrix camera-view player aid,
  SRM00-02B p.7).
- **List of files** -- Index test. Guard roster, operations manual, production schedule, delivery
  schedule, inventory, random files -- plus, optionally, a backup copy of **File H**, scrambled and
  encrypted, flagged by the module as "relevant in a future mission".
- **Guard roster** -- Files test. Opens the bribery route (15,000 nuyen for a whole shift, floor
  10,000) and the option of removing individual guards magically or physically before the hit.
- **Operations manual** -- Files test, one hour to read. Automated camera monitoring, no
  inspections, unexpected inspection teams are presumed saboteurs and are to be denied access or
  otherwise dealt with, and lethal force against intruders is authorized with no requirement to
  capture.
- **Delivery schedule** -- Files test. Weekly deliveries, the next one in 48 hours, so the plant is
  low on raw material for the whole adventure.
- **Production schedule** -- Files test. Finished product is picked up every 24 hours and moved to
  a secure warehouse; there is never much product on site.
- **List of automated programs** -- Index test. Fixed menu: medkit construction, antidote slap
  patch, stim patch, tranq patch, trauma patch.
- **Creating a new automated program** -- Computer (6), base time 48 hours, then a Files test to
  upload and a Control test at +2 to implement. The target numbers are meant to defeat the idea; if
  a team somehow pulls it off the plant can be made to turn out DMSO, Freeze Foam, oxygenated
  fluorocarbons (P4MO), Jazz (from the stim drug elements) or MAO (from the tranq elements).
- **Changing the running program** -- Slave test.

File H is worth a Karma point on its own: sell it and the team gets nuyen, destroy it or quietly
keep it and they get the Karma. Saint James, asked about it, shrugs -- "Haven't the foggiest, old
son. Maybe you should hang onto it..."
"""

NOT_BUILT = """
- **The enterprising decker** who cracked Paladin's JSR database and sold DocWagon its operating
  figures and contract charges -- never named, never met, and the entire cause of the adventure. A
  standing hook.
- **Saint James's two bodyguards**, who stand like statues in the corner of the meeting room and
  fight for him if he is attacked -- no names, no stats.
- **The Sheraton Towers security rigger**, who has been watching the team since they set foot on
  hotel property and controls hidden weapon mounts and the airtight-door gas trap. Folded into the
  Sheraton Towers notes.
- **The four remaining human guards** of the Snohomish detail share the shift leader's stat block
  and are run as a unit; only the shift leader gets a row.
- **The DocWagon reinforcement element** -- six additional guards and a security magician (SR3
  Combat Mage stats) arriving thirty minutes after any alarm. Folded into the facility notes.
- **The IWS DLK MK 8 forklift drones** (two) and the lawn-care drone -- machines with stat blocks,
  kept in the facility notes; the forklifts are excellent cover and useless to a runner.
- **The agricorp** David Wadsworth grows his bioengineered wheat for -- unnamed.
- **The secure warehouse** that takes the plant's finished product every 24 hours -- unnamed and
  off-map.
- **"New Lifers"**, Ares, Renraku, Remington, Enfield, Heckler & Koch, Beretta, Colt -- one-line
  name-drops in legwork banter or on gear.
- **The Table Rating chart** (TR 1 Green TN 4 / 2 Streetwise TN 5 / 3 Professional TN 6 / 4 Veteran
  TN 8 / 5 Elite TN 10 / 6 Prime Runner TN 12, by average career Good Karma) -- a campaign scaling
  aid introduced in this module, referenced in the NPC notes as "Karma TR".
"""

PLAY_NOTES = """
- This is a much harder module than SRM 00-01 and the book says so: the guards use real tactics,
  will usually see the team before the team is inside, set ambushes, and are well armed. If the
  players are new, drop the Jazz -- without it the guards are not street samurai and the tactics
  alone carry the fight.
- Reward legwork above everything. There are five separate routes into the plant's secrets -- the
  farmer, distance surveillance across a shift change, City Planning blueprints for 250 nuyen,
  astral recon for the only full interior map, and the Matrix host -- and a team that uses three of
  them will find the run comfortable while a team that uses none will probably lose people.
- The 30-minute reinforcement clock is the real timer, not the 24-hour bonus. Once the security
  operator calls it in, everything is a countdown; the sirens are audible in time to run.
- Do not let the surprise-inspection trick work. It is in the text specifically as a lesson that
  the opposition is not stupid: the guards invite the "inspectors" inside, surround them, and open
  fire.
- Guards do not have to die, and the Karma says so: 1 for destroying the facility, 1 for not
  killing the guards, 1 more (cumulative) for circumventing them entirely -- bribery, drugs, magic,
  stealth, anything that gets the charges laid without an alarm -- and 1 for keeping or destroying
  File H rather than selling it.
- Bribery is a legitimate solution and worth signposting: the guard roster is one Files test away,
  the shift leader wants 15,000 nuyen and will take 10,000, and the whole thing costs less than a
  firefight. Refuse his price, though, and the garrison doubles.
- Never let a wounded runner call DocWagon without spelling out the consequences first. That is a
  career-ending mistake dressed up as a reflex.
- Saint James is the season's fixer and should end the module liked. He debriefs with real
  interest, pays without argument, sets the charges himself for free if the team has no demolitions
  expert, and toasts them at the end. Attacking him ends careers, permanently.
- Two threads to keep alive: File H, which the module explicitly plants for later; and the "one
  fixer, what was her name again" that Saint James used to guard, who is the dead fixer whose
  estate was being divided in SRM 00-01.
"""
