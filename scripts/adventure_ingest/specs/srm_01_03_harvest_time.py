# SRM 01-03 Harvest Time (FanPro / WizKids, 2004, Shadowrun Missions Season One, SR3) --
# campaign order #46. The Redmond Barrens (the Raikun encampment, the sewers, an abandoned
# residential district) and Fort Lewis (DocWagon clinic #147), with the hiring meet downtown.
# SETTING NOTE / DISCREPANCY WITH THE TASK BRIEF: commissioned as "Denver in the 2060s (SR4 era)";
# the book is Seattle and "For use with Shadowrun, Third Edition". Denver is never mentioned. Every
# location carries city "Seattle".
# Dating: no in-world date is printed. The adventure runs inside a single day (the attack at about
# 4 AM, the hiring meet at noon, delivery required before 5 PM) and follows directly on the vault
# raid of SRM 01-02. YEAR follows the campaign at 2064.
# Editing inconsistencies in the book, noted again on the affected rows: the villain is "Devon
# Tyler" throughout the text, "Devon Tylor" in the Awarding Karma section, and "Devon Taylor" on
# the clinic map in the handouts; Luxi is "he" in the Cast of Shadows and in most of the text but
# becomes "she"/"her" mid-paragraph in the no-decker variant and its parenthetical note; the clinic
# is unnamed in the adventure text ("the DocWagon office in Fort Lewis") and is "DocWagon clinic
# #147" in the handout and on the map; Jimbo, Luxi and the generic Raikun Tribe Member template are
# all printed at Essence 1.0 with no cyberware listed at all, which the book never explains (the
# squatter block footnotes Essence loss to "disease, toxic environment, and other poor living
# conditions", the only rationale offered anywhere); and the drone video has the Doom Squad
# accelerating "towards the northwest" out of a Redmond Barrens camp although their destination is
# the Fort Lewis clinic to the south.
# Rows created by earlier specs are updated, never re-created: Saint James comes from
# specs/srm_00_02_demolition_run.py; Rose Croix, Michael Davenport (as Walter Broward), and Hondo
# come from specs/srm_01_01_double_cross.py and specs/srm_01_02_strings_attached.py.
# Source text: docs/Adventures/text/SRM01-03A_Harvest_Time.txt (29 pages) and
# docs/Adventures/text/SRM01-03B.txt (player handouts).
# ASCII only (pre-commit hook).

ADVENTURE = "SRM 01-03 Harvest Time"
ORDER = 46
SOURCE = "SRM01-03A_Harvest_Time.pdf, pp. 3-29; SRM01-03B.pdf (player handouts)"
YEAR = "2064 (a single day, days after the Kethers Building raid of SRM 01-02; no in-world date " \
       "is printed)"

SYNOPSIS = """
The vault raid of SRM 01-02 destroyed or carried off most of DocWagon Seattle's Type O donor organs
and its vat-grown stock, and DocWagon's contracts require reserves it can no longer show. Growing
organs takes time. So **Devon Tyler**, a low-profile executive who has just been handed
responsibility for the temporary organ storage facility in Fort Lewis, received a memo telling him
to use any method necessary -- and hired the **Doom Squad**, a team of washed-out mercenaries who
work almost exclusively for DocWagon, to kill some SINless and harvest what was inside them.

At about four in the morning they hit the **Raikun**, a small, isolated urban tribe scratching a
living out of Redmond Barrens scrap. **Kip**, the tribe's ancient shaman, had a premonition and
warned the chief; Kip, **Jimbo**'s family and **Ron**'s family hid, and everyone else -- roughly two
thirds of the tribe, some two dozen people -- was butchered in their beds. Jimbo took a bullet and
had one eye cut out of his head before the squad's leader picked up a signal that someone was
coming and called the pull-out. What that signal actually was is a rigger's drone, sitting over the
hill scouting an unrelated job, recording every second of it. The rigger sold the footage through a
friend of a friend to **Rose Croix**, and was paid handsomely.

Walter Broward's people know they did not order this, and are certain DocWagon did. The video would
anchor a media campaign that could break DocWagon's remaining reputation -- but it needs
corroboration and it needs the one-eyed man. So the fixer **Saint James** calls the runners at
lunchtime and sends them to a closed diner where a nervous first-time Johnson named **Vincent
Capello** plays them the recording, hands over a grainy printout of a face, gives them the
encampment's address and 1,000 nuyen each, and tells them to produce the witness and any evidence
tying DocWagon to the killings before five o'clock.

The encampment is a burnt-out shell with a funeral pyre in front of the scrap shed and a background
count of 4 hanging over it. A friendly ork squatter called **Mike** explains what happened; a map in
the survivors' bunker points five miles across the Barrens to a sewer; and the Doom Squad, who have
come back to finish the job, pull up in the same black Americar while the runners are still standing
in it. Below ground, **Mindy** leads the team through the tunnels to what is left of her tribe, and
Jimbo offers a bargain: help us prove who did this, and I will go and speak to your employer.

Two leads, one afternoon, pick one. Kip's, in which the tribe's totem **Rat** -- who is not a totem
at all but a trickster free spirit farming their worship -- has been pinned behind an astral barrier
by **Sqoosh-Water**, the free city spirit whose personal domain these sewers are; free him and he
leads the team to a grate opposite a DocWagon clinic in Fort Lewis and names the man at the top-floor
desk. Or **Luxi**'s, in which an anonymous tip has produced an LTG address that turns out to be the
clinic's own feeble Green host, and a file called **Operation LifeRaft** with the Doom Squad's
contact details and the Raikun's address in it.

And then, as the runners bring Jimbo up out of the sewer, an armoured DocWagon Citymaster slides to
a stop in the street. Tyler has told a High Threat Response team that Jimbo is a kidnapped client in
medical danger. They have gel rounds, legal authority, and a growing suspicion that no call for this
extraction ever came over their radios.
"""

TIMELINE = """
- **Days back** -- the Kethers Building raid (SRM 01-02) destroys or removes most of DocWagon
  Seattle's Type O donor organs and vat-grown tissue stock.
- **Shortly after** -- DocWagon fails the reserve clauses in its contracts. Devon Tyler, newly
  responsible for the Fort Lewis temporary organ storage facility, receives a memo telling him to
  use any method necessary, and opens Operation LifeRaft with the Doom Squad.
- **Day 0, about 4 AM** -- the Doom Squad hits the Raikun encampment. Kip's premonition saves two
  families; roughly two thirds of the tribe die. Jimbo is shot and loses an eye. The squad pulls out
  when its leader picks up a signal. A rigger's drone, scouting the area for an unrelated run,
  records the whole attack.
- **Day 0, dawn** -- Mike helps the survivors burn the bodies; the remnant leaves in the tribe's VW
  Superkombi for the sewer hideout Rat directed them to. The background count over the camp is 4.
- **Day 0, morning** -- the rigger sells the footage on through a mutual contact to Rose Croix.
  Saint James phones the runners; the Johnson asked for them by name.
- **Day 0, noon** -- the meet at Rosie's. 4,000 nuyen each, 1,000 up front, bonus for evidence,
  delivery before 5 PM.
- **Day 0, afternoon** -- the encampment, Mike, the bunker map; the Doom Squad returns to silence
  witnesses; the sewer walk with Mindy; the bargain with Jimbo; Kip's run or Luxi's run.
- **Day 0, late afternoon** -- Tyler gets a tip on Jimbo's location and calls out an HTR team on a
  false client-extraction pretext. The Citymaster meets the runners at the sewer mouth.
- **Day 0, before 5 PM** -- Rosie's again: Jimbo delivered, the balance paid, 1,000 nuyen per level
  more for evidence.
- **Next day** -- Lone Star raids DocWagon clinic #147 on an anonymous tip; two dozen sets of
  DNA-typed organs, Jimbo's eye matched to him, the video handed over by anonymous sources.
- **Days after** -- DOCW drops four points; Tyler is charged and expected to be convicted of murder
  in the first degree; DocWagon is fined on multiple counts and sued for the tissue lost at the
  Kethers Building; Rose Croix nearly doubles its client base.
"""

ORGS = [
    {
        "name": "Raikun",
        "org_type": "urban tribe",
        "affiliation_contact_type": "Tribe",
        "tier": 1,
        "headquarters": "A walled scrap encampment in the Redmond Barrens; after the massacre, a bricked-off chamber in the sewers five miles away",
        "summary": "A small, deliberately neutral urban tribe of Barrens scavengers who worship the spirit they believe is the totem Rat, and who lose two thirds of their number to an organlegging run in a single night",
        "description": (
            "An urban tribe that lived in a small walled encampment in the Redmond Barrens, making "
            "its living by scavenging the surrounding area for anything that can be repaired, "
            "broken down for parts or sold as scrap metal. They are respected in the Barrens and "
            "they are respected because they are harmless: the tribe's policy under Jimbo is strict "
            "neutrality and good terms with everyone, which is why no Raikun will become anyone's "
            "contact -- to be a contact is to choose a side, and a tribe this small cannot afford "
            "one. They are guided by Kip, their spiritual leader almost since the tribe began, and "
            "through him by 'Rat', whom they take for their totem and who is in fact a trickster "
            "free spirit harvesting their worship. A dozen survive the adventure's opening "
            "massacre: Jimbo, his sister Mindy, Ron and his family, the techie Luxi, Kip, two "
            "mid-aged women, three young men with steel crowbars and three children between four "
            "and fifteen."
        ),
        "leadership": [
            {"name": "Jimbo", "title": "Leader of the Raikun", "notes": "Twenty-eight; chief for about six years; lost an eye in the attack."},
            {"name": "Kip", "title": "Spiritual leader (Rat shaman)", "notes": "Frail, ancient, failing; training Mindy to succeed him."},
            {"name": "Mindy", "title": "Rat shaman in training; Jimbo's younger sister", "notes": "Suspects Rat is not what he claims."},
            {"name": "Luxi", "title": "Tribe techie", "notes": "The tribe's electronics man; saving for a datajack."},
            {"name": "Ron", "title": "Head of the second surviving family", "notes": None},
        ],
        "notes": (
            "Raikun Tribe Member block p.28: B2 Q2 S2 C3 I3 W2, Ess 1.0, Reaction 2, Init 2+1D6, "
            "Combat Pool 3, Karma Pool 1, Professional Rating 1; Etiquette 1 (Street 3); Gang "
            "Identification 2, Street Background 2, Scrounge 5; no armour, no weapons, no gear. "
            "(The template, Jimbo and Luxi are all printed at Essence 1.0 with no cyberware listed "
            "-- the book never explains it; the squatter block's footnote blames disease, toxic "
            "environment and poor living conditions, which is the only rationale offered anywhere.) "
            "Assets: the encampment scrap shed, worth 100 nuyen at its best piece, and the tribe's "
            "prized possession, an old beat-up VW Superkombi worth about 750 nuyen. They can offer "
            "the runners about 600 nuyen total, plus 10 nuyen per net success on a negotiation, "
            "which is everything they have. Kip can add shamanic training, healing, and -- if asked "
            "nicely and treated with respect -- four doses of Spirit Strength (M and M p.123) made "
            "from Barrens mushrooms by a process Rat gives him and that he cannot repeat unaided. "
            "Aftermath: Jimbo testifies, Tyler is charged with murder in the first degree, and the "
            "tribe's neutrality ends -- 'We have always remained neutral -- as long as no one "
            "bothered us, we bothered no one. That is about to change.'"
        ),
        "enemies": ["Doom Squad", "DocWagon"],
    },
    {
        "name": "Doom Squad",
        "org_type": "shadowrunner team",
        "tier": 2,
        "headquarters": "Seattle metroplex; no fixed base given",
        "summary": "A small, old-school in-house team of washed-out mercenaries who work almost exclusively for DocWagon, take the wetwork nobody else will, and butchered the Raikun for their organs",
        "description": (
            "A team of former mercenaries who for one reason or another could not make it in a "
            "traditional military unit, gathered in the Seattle metroplex and hiring themselves out "
            "to a small client list -- DocWagon among them -- each of whom pays well enough that "
            "the squad is never spread thin. They are old-school and undiversified: no mages, no "
            "deckers, no riggers on the ground, only hard hitters, with the few specialists they "
            "have kept as senior officers who appear only for consulting agreements and training "
            "sessions. Their loyalty to their benefactors is described as flawless, and they will "
            "take missions many shadowrunners will not -- wetwork, and in this case organlegging. "
            "They have trained some of DocWagon's own High Threat Response teams."
        ),
        "leadership": [
            {"name": "Devon Tyler", "title": "DocWagon client and handler for Operation LifeRaft", "notes": "Not a member; the executive who hired them for the Raikun massacre."},
        ],
        "notes": (
            "Member block p.29: B4(5) Q5(7) S5(7) C3 I5 W4, Ess 0.4, Reaction 6(8), Init 6+1D6 "
            "(8+2D6), Combat Pool 8, Karma Pool TR, Professional Rating 4; Etiquette 5 (Corporate "
            "7), Negotiation 4, Pistols 5, SMG 6, Biotech 4, Stealth 5; Corp Background 4, "
            "Mercenary Background 4; datajack, plastic bone lacing, cybereyes (thermographic, flare "
            "compensation), Muscle Replacement 2, smartlink 2, Wired Reflexes 1, Enhanced "
            "Articulation; secure jacket (5/3, fence 200 nuyen); HK 227-S SMG (7M, 250 nuyen); "
            "commlink Rating 2 (200), certified credstick with 2,000 nuyen, flashlight (10), "
            "scalpel (50). Tactics: they came back to the encampment to make sure there were no "
            "survivors, they assume any team standing in it was hired to protect the witness, and "
            "they open with Mike -- he looks like a squatter, therefore like the survivor. Being "
            "Professional Rating 4 they do not run. Captured and interrogated (SR3 p.93) they will "
            "admit they are shadowrunners finishing an organ theft and silencing witnesses and "
            "nothing more; they will not give up their employer at any cost. Legwork ladder p.24 "
            "(Fixer or any Shadows contact, TN 4): 1 not well known, mostly an in-house team for a "
            "select group of people; 2 old-school, no mages, deckers or riggers, mostly retired "
            "mercs who could not cut it in a military mercenary unit; 3 exclusively DocWagon in the "
            "past, especially training some of their HTR teams, loyalty flawless; 4 if they learn "
            "you are coming you are toast -- surprise attacks are their specialty. The street's own "
            "verdict on the massacre is that it was amateurish: 'If they wanted organs, they should "
            "have attacked isolated individuals in random areas, not an entire tribe!' Aftermath: "
            "Operation LifeRaft holds their names and contact information, and the screamsheet "
            "reports that Tyler's associates cannot be positively identified and remain at large."
        ),
        "enemies": ["Raikun"],
        "allies": ["DocWagon"],
    },
    {
        "name": "Redmond Razors",
        "org_type": "go-gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Redmond Barrens",
        "summary": "A low-level Redmond gang in red and silver-grey, a few of whom have squatted the boarded house over the Raikun's sewer entrance",
        "description": (
            "A low-level Redmond Barrens gang whose colours are red and silver-grey. A small group "
            "of them recently found the barricaded house that sits beside the sewer access the "
            "Raikun survivors use, and spent the night in it before reporting back to their leader "
            "-- which is exactly the wrong night for a shaman who needs an empty room in which to "
            "commune with his totem. The book introduces them only as the Veteran-and-above "
            "upgrade to the three squatters who otherwise hold the house."
        ),
        "notes": (
            "Veteran ganger block p.20 (one per character): B5 Q4 S5 C3 I4 W3, Ess 6, Reaction 4, "
            "Init 4+1D6, Combat Pool 5, Karma Pool 5, Professional Rating 3/Trained; Pistols 6, "
            "Whips 4, Unarmed Combat 4; Browning Max-Power heavy pistol (9M, fence 50 nuyen), chain "
            "(5S, Reach 2); synth-leathers with plates (3/3, 75 nuyen). Elite/Prime version (two "
            "per character): Q6 W4 C4, Reaction 5, Init 5+2D6, Combat Pool 6, Professional Rating "
            "4/Professional, and they have taken Jazz before the runners come through the door. "
            "Plot use: they hold the boarded house during Kip's no-magician run, where the fight is "
            "avoidable -- Negotiation (Bargaining) (4), Intimidation (4) or Etiquette (Street) (4) "
            "buys quiet while Kip communes. A gang that has just started using a house directly "
            "over the entrance to the Raikun's hiding place is also a standing threat to the "
            "survivors after the adventure ends."
        ),
    },
]

LOCATIONS = [
    {
        "name": "Rosie's",
        "location_type": "restaurant",
        "city": "Seattle",
        "district": "Tenth and Terrace",
        "security_level": "Low Security",
        "summary": "The tiny dinner restaurant at Tenth and Terrace, closed and empty, where Rose Croix's first-time Johnson plays the runners a drone recording of a massacre",
        "description": (
            "An incredibly small dinner restaurant at Tenth and Terrace with a CLOSED sign hanging "
            "in the door. When the runners arrive at noon the Johnson opens it for them himself. "
            "There is nobody else inside: he has pushed two tables together, set out chairs and a "
            "computer, and that is the whole of the room's furniture as far as this meeting is "
            "concerned. He starts the moment the last runner is through the door. The same room is "
            "where the job ends -- Jimbo is delivered here and the balance paid over the same "
            "tables."
        ),
        "notes": (
            "Both the Hire and Meet and Picking Up The Pieces scenes. The video is played on the "
            "computer here: aerial, shaky, long range, night, low-light lens; a chemical warehouse "
            "on a hillside with a shanty town below it; four men in black combat gear setting down "
            "a large box and entering shacks; a man shot at a doorway; a gunman kneeling, setting "
            "down his SMG and cutting out the man's eye; the squad bagging it, closing the box (two "
            "men to lift it), loading it into the trunk of a black Ford Americar and accelerating "
            "away; then the camera panning back to the survivors gathering round the one-eyed man, "
            "one of them cradling him and singing with his head raised while a strange nimbus forms "
            "over them both, and others dragging bodies out of the huts, one large man's chest "
            "cavity clearly open. Terms: 4,000 nuyen each, 1,000 in advance, non-negotiable for the "
            "witness; the bonus for evidence is negotiable and pays 1,000 nuyen per level each. "
            "Deadline 5 PM the same day. Alternatives to more cash, of which the team picks exactly "
            "one: free surgery and recovery at a clinic with some of the metroplex's finest doctors "
            "(cyberware and bioware, but not cultured bioware or anything requiring brain surgery; "
            "off the record, and they will install illegal security or military grade if the "
            "runners can find it); another 1,000 nuyen per character in medical supplies, chemicals "
            "and controlled drugs, poolable across the team; an introduction to a street shaman who "
            "turned Rose Croix down and heals the needy; or a tip on an upcoming AAA megacorporate "
            "announcement, with the Johnson buying the stock on their behalf."
        ),
    },
    {
        "name": "Raikun Encampment",
        "location_type": "squatter camp",
        "city": "Seattle",
        "district": "Redmond Barrens",
        "security_level": "No Security / Barrens",
        "controlling_org": "Raikun",
        "summary": "The walled scrap camp where two thirds of a tribe were butchered for their organs, now empty except for a funeral pyre and a background count of 4",
        "description": (
            "About twenty-five metres square, at the bottom of a hill beneath a warehouse full of "
            "chemicals and next to a junkyard, so that the smell is a competition between the "
            "chemicals above and the burnt bodies below. Corrugated steel sheets two and a half "
            "metres high make the walls -- Barrier 4, flimsy and badly weakened by acid rain, "
            "intended to keep devil rats out rather than people -- with a five-metre opening for a "
            "gateway. Inside are five shacks of the same steel and one larger structure built from "
            "the remains of a small warehouse, and debris everywhere: rusted car hulks, mechanical "
            "parts, plasticreet blocks, steel beams, a handyman's dream. A small funeral pyre with "
            "the remnants of the burnt bodies sits in front of the warehouse. A chilling impression "
            "fills the place."
        ),
        "notes": (
            "ASTRAL: the massacre of about two dozen people and the pyre that followed have pushed "
            "the background count from its normal 1 (toxic chemicals plus Rat's workings) to 4. It "
            "decays normally over the next couple of hours unless an Initiate intervenes with "
            "Cleansing. There is no background count inside the bunker. THE WAREHOUSE: three walls "
            "and a roof piled with scrap, open end facing the gate, where the Raikun stored what "
            "they scrounged for sale -- parts of cyberdecks, drones and vehicles, all low quality, "
            "the best single piece worth 100 nuyen. THE SHACKS: four to six beds, a table, chairs, "
            "a chemical toilet and drawers each, very dim without a light source, beds mostly "
            "covered in blood, nothing of value left. Jimbo's larger shack near the entrance has a "
            "dozen beds and no blood on them at all -- Perception (4). THE BUNKER: behind the "
            "warehouse, a one-metre concrete drainage culvert into the hillside with its iron lid "
            "left lying on the ground (the survivors did not close it behind them), opening into a "
            "1.5-metre sewer pipe that runs about three metres in to a small bunker with eight "
            "beds, a cable-spool table, chairs and a locker. The locker holds what they forgot: a "
            "very old Colt American L36 in poor condition with a full clip of normal rounds, bottles "
            "of water and cans of food. On the table lies a simple map to another hideout in the "
            "sewers about five miles away -- the runners must leave with it. SCENES: Mike wanders "
            "in while they search; the Doom Squad's black Ford Americar pulls up opposite as they "
            "leave. Veteran and above: ghosts or shedim drawn by the killing and the pyre, which "
            "will try to take the body of any mage who goes astral and leaves it unprotected."
        ),
    },
    {
        "name": "Raikun Sewer Refuge",
        "location_type": "subterranean community",
        "city": "Seattle",
        "district": "Redmond Barrens (an old residential district five miles from the encampment)",
        "security_level": "No Security / Barrens",
        "controlling_org": "Raikun",
        "summary": "A bricked chamber off the Redmond sewers where a dozen surviving Raikun hide; reached through an open manhole in the backyard of a derelict house and a five-minute walk in the dark",
        "description": (
            "Above ground it is a street of houses nearly two centuries old, once probably very "
            "luxurious and now ramshackle and all but abandoned, with an open sewer access "
            "improbably sited in one of the backyards. Below, the tunnels are a series of corridors "
            "and turns dark enough that low-light vision does not help, with walkways either side "
            "of a centre channel and rats and insects scattering ahead of every footstep -- visible "
            "with thermographic, ultrasound or astral vision. The ceilings are low enough that orks "
            "and trolls must either stoop against the curve of the wall or walk the channel through "
            "a foot of raw sewage. Five minutes in, an opening in the wall that was clearly cut "
            "some time after the original construction leads to a large room: old brick walls, "
            "three practically rotted wooden pillars like old railroad ties holding up the ceiling, "
            "and furniture consisting of boxes, crates and camp beds. A dozen people in old brownish "
            "stained clothes: Jimbo with a bloodied bandage over his missing eye at the table with "
            "Ron and Kip, two mid-aged women, three young men holding steel crowbars, and three "
            "children between four and fifteen."
        ),
        "notes": (
            "Mindy meets the runners in the street -- a short hooded figure in a brown cape, long "
            "brown hair and a noticeable stench -- challenges them, and drops out of sight into the "
            "manhole without waiting for an answer. She walks in front, navigating by some sense "
            "she does not explain and telling them only to be quiet. Intelligence (6) to remember "
            "the way back out, with up to a -4 target number for GPS or other directional talents. "
            "These sewers are the Personal Domain of a powerful free spirit, and the toxic and "
            "sometimes radioactive waste illegally dumped into them has fed it and left a background "
            "count of 1. Kip has a Detect Truth spell sustained from before the runners arrive and "
            "will tell Jimbo if they lie. Optional encounter on the way in: devil rats. THE BARGAIN: "
            "Jimbo will go and meet the Johnson, and asks in return for help making the killers pay; "
            "the tribe can offer about 600 nuyen (+10 per net success), which is all the money they "
            "have and most of it hypothetical until they sell the van. Time management matters -- if "
            "there is half an hour left, skip the sub-runs and go straight to Jimbo's extraction. "
            "The book is clear that helping the Raikun is strongly in the players' interest and "
            "equally clear not to push a group that refuses."
        ),
    },
    {
        "name": "The Boarded House",
        "location_type": "ruins",
        "city": "Seattle",
        "district": "Redmond Barrens (beside the Raikun's sewer entrance)",
        "security_level": "No Security / Barrens",
        "summary": "The derelict, planked-up house next to the sewer access where Kip must go to reach Rat when no magician is available -- and where three squatters, or a gang, already live",
        "description": (
            "One of the near-two-century-old houses on the abandoned residential street, barricaded "
            "from the outside with planks over every window and door. Inside it is completely empty "
            "-- a basement, a ground floor and a second story, no furniture at all, no sign anyone "
            "has lived here recently, and light coming only in strips between the boards. Kip goes "
            "to a corner of it, tells the runners to watch over him, and commits himself to a trance "
            "to commune with Rat while the team stands in the dark listening to a house that turns "
            "out not to be as empty as it looks."
        ),
        "notes": (
            "Entry: ordinary tools break the barricade easily, or a Strength (5) test; a Perception "
            "(6) examination of the outside finds loose planks over a basement window. Three "
            "squatters live on the second story -- secure squats like this one are rare in the "
            "sprawl and they do not want their claim jumped. They come down the stairs with guns "
            "and tell the runners to leave; they will fight briefly and break the moment they think "
            "they cannot win. Negotiation (Bargaining) (4), Intimidation (4) or Etiquette (Street) "
            "(4) makes them wait quietly instead. Squatter block p.18: B1 Q2 S4 C2 I4 W4, Ess 5.0 "
            "(the book footnotes the loss to disease, toxic environment and other poor living "
            "conditions), Reaction 4, Init 4+1D6, Combat Pool 6, Karma Pool 1, Professional Rating "
            "2; Pistol 2, Unarmed Combat 2, Stealth 2; Colt American L36 (6L light pistol, fence 25 "
            "nuyen). At Veteran and above, replace them with Redmond Razors gangers who found the "
            "house and stayed the night. After a few minutes Kip surfaces with Devon Tyler's name, "
            "face and location, having followed Rat to 'the secret hiding places of those that "
            "would do such an act'."
        ),
    },
    {
        "name": "Sqoosh-Water's Domain",
        "location_type": "sewer network",
        "city": "Seattle",
        "district": "Redmond Barrens (beneath the abandoned residential district)",
        "security_level": "No Security / Barrens",
        "summary": "The stretch of Redmond sewers a greater free city spirit has claimed as its Personal Domain, fed on illegally dumped toxic and radioactive waste, where it keeps a rival spirit caged in a puddle of goo",
        "description": (
            "The same tunnels the Raikun hide in, seen as the thing that lives in them sees them. "
            "Decades of illegally dumped toxic and sometimes radioactive waste have fed the free "
            "spirit that claims them, and left a background count of 1 through the whole network. "
            "At a junction some way from the Raikun's chamber the spirit stands materialised in the "
            "middle of the passage: a tall humanoid mass of waste, wet and shapeless and eight feet "
            "of it. In a corner behind it is a small pile of goo that is not goo at all but a "
            "Rating 2 astral barrier, and inside the barrier is a rat."
        ),
        "notes": (
            "Sqoosh-Water, Free City Spirit, block p.17: B9 Q10 (x3) S6 C8 I8 W8, Ess 8.0, Reaction "
            "9, Init 28+1D6 astral / 15+1D6 physical, Combat Pool 13, Karma Pool 1, Professional "
            "Rating 4, Force 4, Spirit Energy 2 (4 in its domain); Greater Form, Divination, "
            "Personal Domain, Accident, Concealment, Confusion, Fear, Guard, Materialization, "
            "Search; Armor 12 and Immunity to Normal Weapons; melee 6M; it can attack or use powers "
            "on four targets simultaneously. Claiming the sewers as a Personal Domain doubles its "
            "effective Spirit Energy. Tactics: it will not allow anyone near the prison. It opens "
            "with Confusion and Fear in combination, hoping the runners leave and get lost in the "
            "tunnels; failing that it uses Accident to keep them off balance and unable to dodge "
            "while it clobbers them physically. Banished or otherwise dealt with, the Rating 2 "
            "barrier comes down easily and a small rat runs out. The book warns the GM that players "
            "will smell a rat at the idea of a city spirit imprisoning a totem, and gives them the "
            "answer: neither of these is a totem. Sqoosh-Water is a free spirit that dislikes "
            "interference in its domain, and 'Rat' is another free spirit that was travelling in "
            "the form of an ordinary sewer rat, was caught by surprise, and was too weak to break "
            "the barrier."
        ),
    },
    {
        "name": "DocWagon Clinic #147",
        "location_type": "hospital",
        "city": "Seattle",
        "district": "Fort Lewis (a commercial district just across the border)",
        "security_level": "Corporate Standard",
        "controlling_org": "DocWagon",
        "summary": "A two-storey neighbourhood clinic in Fort Lewis with DocWagon's temporary organ storage, a small vat-growing lab and Devon Tyler's office on the floor above it",
        "description": (
            "A two-storey building in a very commercial part of Fort Lewis. The ground floor is a "
            "fully operating public clinic -- waiting room, four examining rooms, two operating "
            "rooms, three recovery rooms, a scrub room, records, administration, break room, "
            "storage -- busy by day with patients, doctors and administrative staff, none of whom "
            "know anything about what happens upstairs beyond the fact that there are offices and "
            "some special labs they are not authorised to enter, and that a DocWagon executive "
            "named Devon Tyler works out of them. The second floor is the peripheral office that "
            "manages temporary donor-organ storage for the Seattle division, with a lobby, three "
            "offices, a small meeting room, a break room, two labs, a tissue lab, cold storage, a "
            "security pool, and rooms for the senior managers, the assistant director and the "
            "director."
        ),
        "notes": (
            "ENTRY: the main door is reinforced glass, unlocked in business hours and on a keycard "
            "maglock (5) at night; a short corridor leads to another reinforced glass door into the "
            "examining rooms and a stairway at the end. Upstairs, a reinforced glass door carrying "
            "only the DocWagon logo is locked at all times with keycard AND keycode maglocks (both "
            "Rating 6), watched by a ceiling camera recording the stairs, with a call button beside "
            "it. A security guard is on duty at all times at a desk immediately inside with a view "
            "of the lobby: Perception (5) each turn anyone stands at the door; he will not let "
            "anyone in without a very convincing Bargaining (Fast Talk) (9), because security "
            "procedures have been sharply raised since the last shadowrun against DocWagon, and a "
            "failed attempt goes straight to Lone Star on a PanicButton. Employee cards open the "
            "lock (the reader is cardreader-only for staff). Behind the building a metal stairway "
            "leads to an exit-only emergency door, Barrier 16, whose structure absorbs the sound of "
            "knocking. Guard block p.19: B4 Q4 S3 C3 I3 W3, Ess 6.0, Reaction 3, Init 3+1D6, Combat "
            "Pool 4, Karma Pool 1, Professional Rating 2; Clubs 2 (Stun Baton 4), Pistols 2 (Ruger "
            "Thunderbolt 4), Unarmed 3, Car 2, Etiquette 2 (Street 3), City Law 3, Security "
            "Procedures 3; armour jacket (5/3, 100 nuyen); AZ-150 stun baton (8S Stun, 100), Ruger "
            "Thunderbolt (12S, 100), commlink Rating 4 (100). He calls Lone Star at anything unusual "
            "and will not fight unless he believes his life is truly in danger. UPSTAIRS: a heavy "
            "door (Barrier 20) with a biohazard symbol and an Authorized Personnel Only sign leads "
            "to the lab area, which is where the Raikun's organs currently are; retinal scan maglock "
            "plus cardreader, Rating 6, opened only by the four DocWagon technicians and Devon "
            "Tyler. A second door on a Maglock 8 cardreader holds the terminal that carries "
            "privileged access to the DocWagon system. Office terminals are password protected: "
            "Computer (6), base time 30 minutes, or hack them as a Green-4/4/4/4/4/4 system; they "
            "hold organ inventories, request forms and lab analyses and nothing incriminating, "
            "because the confidential data lives on the main host and cannot be reached from here. "
            "Tyler's terminal holds Operation LifeRaft -- the Doom Squad's names and contact "
            "information plus the Raikun encampment's address, with no mention of harvesting "
            "anything, which is damning enough alongside the stolen organs and Jimbo's DNA-matched "
            "eye. Slave controls for the organ storage equipment are not remotely accessible; you "
            "have to jack in on site. WHO IS HERE: whatever time the runners come, upstairs holds "
            "only two lab technicians -- waiting for the Doom Squad to bring in more organs -- and "
            "the guard. AFTERMATH: Lone Star raids the clinic the next evening on an anonymous tip, "
            "finds over two dozen sets of DNA-typed organs including the eye, and matches it to its "
            "owner. The clinic stays operational; the organs are confiscated. NAMING: the adventure "
            "text calls it only 'the DocWagon office in Fort Lewis'; the handout and the map name it "
            "clinic #147, and the map labels the director's office 'Devon Taylor'."
        ),
    },
]

NPCS = [
    {
        "name": "Devon Tyler",
        "role": "The low-profile DocWagon executive who read a memo about reserves and ordered a tribe butchered for its organs; the man Rose Croix needs identified",
        "archetype": "Corporate Executive",
        "title": "Senior executive, DocWagon Seattle; director of the Fort Lewis temporary organ storage facility (clinic #147)",
        "race": "Human",
        "gender": "Male",
        "organization": "DocWagon",
        "connection": 3,
        "description": (
            "A man at a desk in a top-floor office, seen at long range or through a spirit's eyes. "
            "Assensing (Aura Reading (4)) gives one or two successes: he appears healthy, has "
            "little or no cyberware, and is mundane. Three or more adds the only other thing there "
            "is to know about him: he is nervous. He is the sort of executive the campaign is "
            "built out of -- not a monster, an administrator who was handed an impossible target "
            "and a memo that said any method necessary, and who then made every subsequent decision "
            "badly and in a hurry."
        ),
        "background": (
            "A low-profile DocWagon executive who had recently been made responsible for overseeing "
            "the temporary organ storage facility in Fort Lewis when the Kethers Building raid "
            "destroyed or removed most of DocWagon Seattle's Type O donor organs and vat-grown "
            "stock. DocWagon's contracts require reserves; growing new organs takes time; the bulk "
            "of its clients still need donor organs in the meantime. The memo Tyler received asked "
            "him to use any method necessary. He chose the most drastic one available: hire "
            "shadowrunners to kill SIN-less people and harvest what was in them, and gave the "
            "operation a name -- LifeRaft."
        ),
        "notes": (
            "No statistics; he never meets the runners. Both leads end on his name: Rat leads Kip to "
            "the grate opposite clinic #147 and identifies the man at the desk, and the LifeRaft "
            "file is on his terminal, behind the only encrypted hardware key in the office. He is "
            "also the reason for the endgame -- a tip reaches him about Jimbo's location and, out of "
            "ideas, he calls out a DocWagon High Threat Response team on the lie that Jimbo is a "
            "kidnapped client in medical danger. That is an abuse of his authority and DocWagon's "
            "main office will recall the team once someone notices. Aftermath (handout): Lone Star "
            "raids the clinic, Tyler is named as the mastermind, DOCW drops four points, and he is "
            "expected to be convicted of murder in the first degree while his associates remain at "
            "large. Shadowland's reading is that he is taking the fall -- 'more than likely, Tyler "
            "was given an order to handle the situation in nebulous tones. That way, if Tyler did "
            "do something wrong, they would have plausible deniability... Standard corporate "
            "politics.' NAMING: 'Devon Tyler' in the text, 'Devon Tylor' in the Awarding Karma "
            "section, 'Devon Taylor' on the clinic map."
        ),
    },
    {
        "name": "Vincent Capello",
        "role": "Rose Croix's brand-new Mr. Johnson, hand-picked by Walter Broward and running his first shadowrun without knowing how to talk to shadowrunners",
        "archetype": "Corporate Executive",
        "title": "Mr. Johnson for Rose Croix (Vincent \"Vinny\" Capello)",
        "race": "Human",
        "gender": "Male",
        "organization": "Rose Croix",
        "connection": 3,
        "description": (
            "A plain-clothes human with a sharp haircut and a somewhat pointy nose, who opens the "
            "locked door of a closed diner himself and starts the moment everyone is seated. "
            "Careful, rehearsed and a little brittle: he will not say who employs him ('all will "
            "become known in due time. Suffice it to say that it is in your best interests to help "
            "us in this endeavor, but also it would be better for you not to be connected directly "
            "to us at this time'), and at any sign of menace or pressure he asks the runners to "
            "calm down and reminds them that he can pull out of the deal at any time. At the end, "
            "with the witness delivered, he relaxes into the only warm line he has: 'Ah, excellent "
            "work. I'm sure my superiors will be most pleased.'"
        ),
        "background": (
            "Vincent 'Vinny' Capello was hired away from a local corporation to help build Rose "
            "Croix, and was hand-picked by Walter Broward himself. He does not know why Broward "
            "hired him or how he learned of him and his talents. What came out during the interview "
            "was that Vinny wanted to be more involved in the inner workings of the corporation "
            "from the covert side -- that he wanted to become a Mr. Johnson and deal with "
            "shadowrunners and the exciting life that promised. Broward decided to give him his "
            "chance. This is his first assignment."
        ),
        "notes": (
            "Stats p.25: B3 Q3 S3 C4 I5 W4, Ess 4.6, Reaction 4, Init 4+1D6, Combat Pool 6, Karma "
            "Pool 3, Professional Rating 2; Etiquette 5 (Corporate 7), Negotiation 4, Pistols 2; "
            "Corp Background 4, Shadowrunners 1, Street Background 1; datajack, chipjack; secure "
            "clothing (3/0); Fichetti Security 500 (6L, fence 75 nuyen); pocket secretary (400), "
            "gold ID credstick in the name Vincent Capello with a balance of 42,752 nuyen, Rolex "
            "wristwatch (500). Note the Shadowrunners knowledge skill of 1 -- he genuinely does not "
            "know how to handle the people he has hired, and the book says the runners have the "
            "advantage in any negotiation here, though he will not bankrupt his benefactors. Terms "
            "and the alternative concessions are on the Rosie's location row. Digging into him "
            "yields nothing: he is very new in the business, and the best the runners' own history "
            "gives them is a guess that they are working for Rose Croix, which he will neither "
            "confirm nor deny. He is an obvious recurring Johnson for the rest of the arc, and a "
            "man whose first job ended with a corporate executive convicted of murder."
        ),
        "contact_skills": ["Rose Croix contracts and Johnson work", "Corporate background research"],
    },
    {
        "name": "Jimbo",
        "role": "Chief of the Raikun, the one-eyed witness the whole run exists to recover, and the man whose testimony ends Devon Tyler",
        "archetype": "Tribal Leader",
        "title": "Leader of the Raikun",
        "race": "Human",
        "gender": "Male",
        "age": 28,
        "organization": "Raikun",
        "connection": 3,
        "description": (
            "Twenty-eight years old, with a bloodied bandage over the socket where his left eye was "
            "cut out this morning, sitting at a makeshift table in a brick room under the Barrens "
            "with what is left of his people around him. Calm and calculating, but with a "
            "passionate fire under it that the GM is told to make the players feel. 'Chummers, these "
            "fraggers will pay dearly for what they have done.' Guarded with strangers and "
            "unfailingly courteous to them anyway. At the end, thanks that runners are not used to "
            "receiving: 'Thank you for all you've done. I assure you, the Raikun will get their "
            "revenge for today's tragedy. We have always remained neutral -- as long as no one "
            "bothered us, we bothered no one. That is about to change.'"
        ),
        "background": (
            "Leader of the Raikun for about six years, one of the younger chiefs in the tribe's "
            "short history, who has led through strength, wisdom and an unswerving commitment to "
            "the tribe. His governing policy is neutrality: keep the tribe on good terms with "
            "everyone and give nobody a reason to move against them. That is why he will not become "
            "anyone's contact and will not let any Raikun become one -- being a contact reads as "
            "choosing a side, and a tribe this small cannot survive having chosen one. Kip's "
            "premonition reached him in time to hide his own family and Ron's; everyone else died. "
            "He was shot in his doorway and had an eye extracted before the killers were called "
            "off."
        ),
        "notes": (
            "Stats p.26: B5 Q4 S4 C5 I5 W4, Ess 1.0, Reaction 4, Init 4+1D6, Combat Pool 6, Karma "
            "Pool 5, Professional Rating 3; Etiquette 5 (Street 7), Negotiation 4, Pistols 3, Clubs "
            "4; Gang Identification 4, Gang Turf 4, Street Background 5; no cyberware listed despite "
            "the Essence, and no armour; boot knife (4L, fence 10 nuyen). He is the mission: Rose "
            "Croix can do nothing with any amount of documentary proof without an eyewitness, so if "
            "Jimbo dies or is taken by the HTR team the run is a failure. Karma turns on his "
            "condition -- 2 if he is recovered less than Seriously wounded and before 5 PM, 1 if he "
            "arrives unconscious, Seriously injured or late. He will bolt back into the sewers "
            "rather than let the standoff at the manhole play out. Aftermath (handout): he "
            "testifies, his extracted eye is DNA-matched to him in the clinic's storage, and Tyler "
            "is charged with murder in the first degree. His refusal to be a contact is a standing "
            "rule that the massacre does not overturn -- what changes is the neutrality."
        ),
    },
    {
        "name": "Kip",
        "role": "The Raikun's ancient, failing shaman, whose premonition saved two families and whose totem is not a totem",
        "archetype": "Shaman",
        "title": "Spiritual leader of the Raikun (Rat shaman)",
        "race": "Human",
        "gender": "Male",
        "organization": "Raikun",
        "connection": 3,
        "description": (
            "Very small for a human and made smaller by a rickety frame bent over all the time. He "
            "speaks in an uneven, croaky, gravelly voice, and what he says makes a fair number of "
            "people conclude he has a nut or two loose. His body is frail and weak; his mind is not. "
            "'Rat contacted me. He knows who did this and he can lead me to him. But an unfriendly "
            "spirit in these sewers don't seem to like Rat.' And on the man at the desk in Fort "
            "Lewis: 'This madman will be punished. His name is Devon Tyler and he works for "
            "DocWagon. We have his face, his location and his name. No need to do anything else, "
            "he's surely a pawn in DocWagon's schemes.'"
        ),
        "background": (
            "Spiritual leader of the Raikun almost since the tribe began. He has felt his advancing "
            "years arrive: magical battles, toxins, pollutants, viruses and the other challenges of "
            "a long life in the Barrens have cost him a good deal of his life force. Knowing he has "
            "little time left, he has begun teaching Jimbo's younger sister Mindy the ways of Rat "
            "so that she can carry on his tradition and his partnership with the spirit. He does "
            "not know, and Mindy has not told him, that the partnership is a con: the 'Rat' he has "
            "served for years is a trickster free spirit that appeared in the middle of one of his "
            "own conjurings and has been farming the tribe's worship and karma ever since. His "
            "premonition of the attack is what saved anybody at all."
        ),
        "notes": (
            "Stats p.26: B1 Q2 S1 C5 I4 W6, Ess 5.0, Reaction 3, Init 3+1D6, Combat Pool 6, Spell "
            "Pool 5, Karma Pool 8, Professional Rating 3; Etiquette 5 (Street 7), Sorcery 5, "
            "Conjuring 5, Enchanting 3; Fungus 3, Junk Value 3, Scrounging 4; Rat totem modifiers "
            "+2 Detection and Illusion, -1 Combat, +2 Spirits of Man; Analyze Device 3, Catalog 4, "
            "Chaotic World 5, Magic Fingers 4, Heal 5, Flamethrower 3; a satchel of odd plants, "
            "herbs and fungus, and four doses of Spirit Strength (M and M p.123) worth 1,000 nuyen "
            "each, made from Barrens mushrooms by a secret process Rat gives him from time to time "
            "-- he cannot reproduce it unaided and cannot share the recipe. He sustains Detect Truth "
            "from before the runners reach the chamber, so Jimbo knows at once whether they are "
            "lying. He runs one of the adventure's two leads either way: with a magician on the "
            "team he asks them to free Rat from Sqoosh-Water's barrier and then follows the spirit "
            "through the tunnels to Fort Lewis; without one he asks for an escort to the boarded "
            "house so he can commune above ground. Offered shamanic training and healing to the "
            "team as part of the tribe's payment."
        ),
        "contact_skills": ["Rat shamanism and Barrens spirit lore", "Healing, poultices and Spirit Strength doses"],
    },
    {
        "name": "Mindy",
        "role": "Jimbo's younger sister and Kip's apprentice, the tribe's guide through the sewers -- and the only Raikun who suspects their totem is a fraud",
        "archetype": "Shaman",
        "title": "Rat shaman in training, Raikun; Jimbo's younger sister",
        "race": "Human",
        "gender": "Female",
        "organization": "Raikun",
        "connection": 2,
        "description": (
            "A somewhat short figure at the side of a derelict house in a brown hooded cape with the "
            "hood drawn up to shadow the face, long brown hair spilling out of the folds and a "
            "noticeable stench coming off her. 'Psssst... You there! Who are ya, and what ya be "
            "doin' here?' Satisfied, she gives them exactly one sentence -- 'I'm Mindy, and the "
            "Raikun are my kin. My father will speak to ya, but until that time, please keep it "
            "quiet.' -- takes a step back and drops out of sight into a manhole. In the tunnels she "
            "walks in front navigating by some unknown sense, will not talk, and tells the runners "
            "they will have all the time and answers they need when they arrive. Delivered, she "
            "goes off to play games with the children."
        ),
        "background": (
            "Jimbo's younger sister, working with Kip to learn about Rat and the magic that keeps "
            "the tribe alive, and marked out as his successor because he knows he has little time. "
            "She also handles the tribe's dealings with other area tribes and neighbours when Kip "
            "sends her on errands, and it is that exposure that has started her thinking: she is "
            "beginning to suspect that Rat is not all he claims, and may be just another spirit "
            "that duped Kip and the tribe into worship so it could gain power. She has voiced this "
            "to nobody. She is waiting to learn more, and she feels that she will soon be stronger "
            "than Kip."
        ),
        "notes": (
            "Stats p.27: B3 Q5 S3 C4 I5 W4, Ess 6.0, Reaction 5, Init 5+1D6, Combat Pool 7, Spell "
            "Pool 2, Karma Pool 2, Professional Rating 2; Etiquette 3 (Street 5), Sorcery 2, "
            "Conjuring 3; Gang Identification 3, Street Background 3; Rat totem modifiers as Kip's; "
            "Analyze Device 3, Chaotic World 3, Magic Fingers 4, Silence 3, Heal 2; heavy cloak "
            "(0/1, fence 25 nuyen). The book leaves her question open and it is the best hook in "
            "the adventure: when she is strong enough, does she bring what she suspects to the "
            "tribe, or bargain with the spirit herself? A team that discovers what 'Rat' really is "
            "-- which the Kip's-run version of the lead hands them outright, since aura reading "
            "shows the freed rat to be a low-strength spirit -- has the choice of telling her, "
            "telling Kip, telling nobody, or using it. NAMING: she calls Jimbo 'my father' when she "
            "challenges the runners; the Cast of Shadows says she is his younger sister. Read the "
            "greeting as the tribe's usage rather than a literal claim, or as one of the book's "
            "several slips."
        ),
        "contact_skills": ["Redmond Barrens tribes and their dealings", "Rat shamanism"],
    },
    {
        "name": "Luxi",
        "role": "The Raikun's self-taught electronics man, who owns half a Matrix rig and one anonymous tip pointing at DocWagon's clinic host",
        "archetype": "Technician",
        "title": "Tribe techie, Raikun (Luxi, short for Luxury)",
        "race": "Human",
        "gender": "Male",
        "organization": "Raikun",
        "connection": 2,
        "description": (
            "Talks nervously and fast, and starts talking the instant Kip stops. 'Hey and I'll need "
            "a decker too! Rat contacted me too and gave me a mysterious address on the grid. "
            "However, I'm not drek-hot on the Matrix, and I would need some real wiz skills to "
            "follow the lead and bypass the nice IC on the system to gather whatever paydata the "
            "trail will lead to!' He runs the Matrix on a cheap tortoise deck -- a 200 Mp portable "
            "computer and a jury-rigged electrode net -- and it is the reason he cannot do this "
            "himself."
        ),
        "background": (
            "Luxi is short for Luxury, because his parents used to say that having him was the "
            "biggest luxury they had living in the Barrens. He was always liked by the others in "
            "the tribe and is one of the very few who has had any sort of formal education. He is a "
            "quick study and the best person in the tribe for anything electrical, working through "
            "the odds and ends the others bring in to salvage usable chips and parts to sell. He is "
            "currently saving up for a datajack so that he can use the Matrix properly instead of "
            "through a jury-rigged trode net. The address he is offering did not come from Rat at "
            "all -- it came from one of his own contacts, a handle called Ratman -- but he will go "
            "on insisting it came from the totem, because the totem governs so much of the tribe's "
            "existence that saying otherwise is unthinkable."
        ),
        "notes": (
            "Stats p.27: B3 Q4 S3 C3 I6 W3, Ess 1.0, Reaction 5, Init 5+1D6, Combat Pool 6, Karma "
            "Pool 2, Professional Rating 1; Etiquette 2 (Street 4), Computer 2, Electronics 3, "
            "Computer B/R 2, Electronics B/R 3; Matrix Jackpoints 3, Electronics Background 4; "
            "portable computer 200 Mp (fence 500 nuyen), electrode rig (50), electronics toolkit "
            "(250). He runs the second of the adventure's two leads: with a decker on the team he "
            "hands over the LTG address and finds a working terminal jackpoint in a neighbouring "
            "house; without one, he asks to be escorted to the nearest jackpoint and guarded while "
            "he goes in himself, or (in the no-decker branch as printed) the address resolves to a "
            "physical location in Fort Lewis and the team simply breaks into it. His small lie about "
            "Rat is the same crack Mindy is looking through from the other side. NAMING: the Cast of "
            "Shadows and most of the text make Luxi male; the no-decker paragraph and its "
            "parenthetical note switch to 'she' and 'her' mid-sentence -- a book slip, resolved here "
            "in favour of the Cast entry."
        ),
        "contact_skills": ["Barrens salvage electronics and jackpoints", "Matrix rumour from Redmond handles"],
    },
    {
        "name": "Ron",
        "role": "Head of the second Raikun family to survive the massacre; one of the three men at the table when the runners arrive",
        "archetype": "Tribal Elder",
        "title": "Head of the second surviving family, Raikun",
        "race": "Human",
        "gender": "Male",
        "organization": "Raikun",
        "connection": 1,
        "description": (
            "One of the three men sitting at the makeshift table in the sewer chamber when the "
            "runners are brought in -- Jimbo with his bandaged eye on one side, Kip on the other, "
            "and Ron between them, in the same old brownish stained clothes as everyone else. His "
            "family shared Jimbo's shelter on the night of the attack, which is the entire reason "
            "they are alive to sit there."
        ),
        "background": (
            "Head of the second of the two families that survived. When Kip's premonition reached "
            "Jimbo there was time to hide only the chief's family and the family sharing his "
            "shelter; every other Raikun in the encampment was killed in their beds. The book gives "
            "Ron no further history, but his position -- the other surviving patriarch, seated at "
            "the table where the tribe's decisions are made -- makes him the second voice in "
            "whatever the Raikun become after they stop being neutral."
        ),
        "notes": (
            "No individual statistics; use the Raikun Tribe Member block (B2 Q2 S2 C3 I3 W2, Ess "
            "1.0, Init 2+1D6, Combat Pool 3, Karma Pool 1, Professional Rating 1; Etiquette 1 "
            "(Street 3), Gang Identification 2, Street Background 2, Scrounge 5). Recorded because "
            "he is named and seated with the leadership, and because the surviving tribe is going "
            "to need somebody to hold it together while Jimbo is off testifying in a Lone Star "
            "courtroom against a DocWagon executive whose associates are still at large."
        ),
    },
    {
        "name": "Mike",
        "role": "Ork squatter and longtime friend of the Raikun who wanders into the ruined encampment to grieve, and gets shot at for looking like a witness",
        "archetype": "Squatter",
        "title": "Redmond Barrens squatter",
        "race": "Ork",
        "gender": "Male",
        "age": 24,
        "connection": 2,
        "description": (
            "About twenty-four, in terribly filthy clothes, wandering into the wrecked encampment "
            "while the runners are searching it and talking to himself about how cruel this is. He "
            "asks them no questions at all about why they are there -- he has only come to look "
            "around. Spoken to, he is genuinely social and answers everything without hesitation, "
            "and what comes across most is how much he liked these people."
        ),
        "background": (
            "A squatter from the local area and always a friend of the Raikun. He can tell the "
            "runners that they were a respected tribe in the Barrens who lived by reselling the "
            "junk they found. He helped burn the corpses after the attack, and then watched the "
            "remnants of the tribe drive away in their old beat-up VW Superkombi; he does not know "
            "where they went."
        ),
        "notes": (
            "Stats p.12: B6 Q3 S7 C2 I3 W3, Ess 6, Reaction 3, Init 3+1D6, Combat Pool 4, Karma "
            "Pool 2, Professional Rating 2; Athletics 2, Stealth 4, Panhandling 4, Scrounge 5, "
            "Redmond Barrens 4; no armour, no gear. Two functions. First, he is the fallback if the "
            "team decides not to visit the encampment at all -- the book names him as the "
            "appropriate street contact to point them at the tribe's new home. Second, he is the "
            "Doom Squad's first target when they come back, because a filthy squatter standing in "
            "the massacre site reads to them as the survivor they were sent to finish. Protecting "
            "him is the runners' first chance to earn the Barrens' opinion of them, and losing him "
            "costs them a witness who could corroborate the video."
        ),
        "contact_skills": ["Redmond Barrens street knowledge", "Scrounging and Barrens squatter networks"],
    },
    {
        "name": "Rat (Trickster Free Spirit)",
        "role": "The trickster city free spirit the Raikun worship as their totem, caged in a sewer puddle by a rival, and the only thing that knows Devon Tyler's name",
        "archetype": "Free Spirit",
        "title": "\"Rat\" -- trickster city free spirit posing as the Raikun's totem",
        "gender": "Unknown",
        "connection": 3,
        "description": (
            "Presents to the tribe as a ghostly rat and to the runners as an ordinary sewer rat "
            "trapped behind a small pile of goo that turns out to be a Rating 2 astral barrier. "
            "Freed, it runs straight to Kip, jumps onto his shoulders and makes whiffing sounds; "
            "then it drops back down and scurries away down the tunnel with the old man running "
            "behind it, ten minutes to a ladder and a grate, and up the wall of a DocWagon clinic "
            "and straight through the wall into a top-level office. Astral perception shows it for "
            "what it is: a low-strength spirit, and nothing remotely like a totem."
        ),
        "background": (
            "After awakening from confinement as the servant of another city Rat shaman, 'Rat' "
            "travelled the Barrens for a time learning how the streets worked and how the "
            "metahumans in them behaved. He came across a group of struggling squatters besieged by "
            "gangs, competing squatters and the forces of the city itself, and when their Rat "
            "shaman began summoning a city spirit he saw his opportunity: he appeared before the "
            "conjuring was finished and pretended to be the spirit called. Having performed the "
            "task set for him he returned later in the form of a ghostly rat, and the shaman took "
            "him for the totem itself. Ever since he has worked to have the tribe worship him and "
            "donate karma to build his powers. He was travelling to Kip in ordinary rat form when "
            "Sqoosh-Water caught him by surprise; he was too weak to break the barrier."
        ),
        "notes": (
            "Stats p.28 -- add the Table Rating (its Spirit Energy) to every attribute: B4 Q5 (x3) "
            "S1 C3 I3 W3, Ess 3.0, Reaction 4, Init 23+TR+1D6 astral / 14+1D6 physical, Combat Pool "
            "(11+TR)/2, Karma Pool 3, Professional Rating 4, Force 3, Spirit Energy TR; Animal "
            "Form, Sorcery, Accident, Concealment, Confusion, Fear, Guard, Materialization, Search; "
            "Armor 3/1 from Force plus Spirit Energy; melee (1+TR)M. Plot use: he is Kip's lead. "
            "Once freed he identifies Devon Tyler by leading the shaman to his office window and "
            "whispering in his ear. The book is explicit that the 'real' Rat has never corrected "
            "Kip's or Mindy's misplaced beliefs, and that the tribe's four doses of Spirit Strength "
            "come from a process he grants Kip and withholds the understanding of -- a supply "
            "relationship, not a gift. The interesting question the adventure raises and does not "
            "answer: the runners have just done a genuine, substantial favour for a free spirit who "
            "trades in obligations."
        ),
        "contact_skills": ["Redmond Barrens secrets, hiding places and who did what to whom"],
    },
    {
        "name": "Sqoosh-Water",
        "role": "The greater free city spirit whose Personal Domain the Redmond sewers are; it caged Rat and will not let anyone near the cage",
        "archetype": "Free Spirit",
        "title": "Free city spirit; Personal Domain: the Redmond sewers beneath the abandoned district",
        "gender": "Unknown",
        "connection": 2,
        "description": (
            "A tall humanoid mass of waste standing in the centre of a sewer junction, materialised "
            "out of the thing it lives in. It does not negotiate and it does not explain. Its "
            "preference is not to fight at all but to make the intruders leave and lose themselves "
            "in the tunnels -- Confusion and Fear used in combination -- and only when that fails "
            "does it start using Accident to keep them off balance and unable to dodge while it "
            "hits them."
        ),
        "background": (
            "A free spirit that has claimed this stretch of the Redmond sewer network as its "
            "Personal Domain, which doubles its effective Spirit Energy inside it. Decades of "
            "illegally dumped toxic and sometimes radioactive waste have fed it and left a "
            "background count of 1 through the tunnels. It does not like interference from other "
            "spirits in its territory, which is the entire reason it caught the free spirit "
            "travelling through in rat form and pinned it behind a barrier in a corner rather than "
            "destroying it."
        ),
        "notes": (
            "Stats p.17: B9 Q10 (x3) S6 C8 I8 W8, Ess 8.0, Reaction 9, Init 28+1D6 astral / 15+1D6 "
            "physical, Combat Pool 13, Karma Pool 1, Professional Rating 4, Force 4, Spirit Energy "
            "2 (4 in its domain); Greater Form, Divination, Personal Domain, Accident, Concealment, "
            "Confusion, Fear, Guard, Materialization, Search; Armor 12, Immunity to Normal Weapons; "
            "melee damage 6M; can attack or use powers against four targets simultaneously. The "
            "barrier holding Rat is Rating 2 and comes down easily once the spirit is banished or "
            "otherwise dealt with. This is the hardest fight in the adventure by a distance, and "
            "the book offers no alternative to it in the magician branch -- although a spirit with "
            "Divination and a grievance against trespassing spirits is negotiable in the hands of a "
            "GM who would rather run a conversation. Left alone it keeps the sewers, which are also "
            "where the surviving Raikun now live: a permanent complication for the tribe and a "
            "recurring landmark for anyone who uses these tunnels again."
        ),
    },
    {
        "name": "Hank",
        "role": "Bear street shaman of the Redmond Barrens who turned down Rose Croix's magical healing program to keep treating anyone who walks in",
        "archetype": "Shaman",
        "title": "\"Hank\" -- Bear street shaman, Redmond Barrens (real name unknown)",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "Just what the name sounds like: a large, burly human who could be mistaken for a truck "
            "driver, slow and gentle, called by Bear to do healing works. He moves in strange "
            "circles in the Redmond Barrens because he will treat anyone who comes to him for aid "
            "regardless of metatype or political leaning, and the various gangs have declared him "
            "off limits -- one of the very few things they can all agree on, since they all need "
            "him. He works with natural healing herbs wherever he can and rarely has any need for "
            "modern medicine, using his magic to make powerful poultices and healing potions "
            "instead."
        ),
        "background": (
            "Rose Croix approached Hank early on and offered him a lucrative post in its magical "
            "healing services program, and he surprised them by turning it down. He has nothing "
            "against corporations as such; he has simply decided that he is needed more in the "
            "Barrens than in 'some clean, white lab where rich housewives come for cosmetic "
            "surgery'. That refusal is why Rose Croix's Johnson can offer him as a favour -- one of "
            "the four alternative concessions in the hiring meet is an introduction to 'a street "
            "shaman that has refused to join their organization, but has committed himself to "
            "healing those that need it'."
        ),
        "notes": (
            "Contact card (SRM01-03B): B5 Q3 S5 I5 W6 C5, Ess 6.0, Reaction 4, Init 4+1D6, Karma "
            "Pool 7, Professional Rating 3; Etiquette 3 (Street 5), Biotech 4, Sorcery 8, Conjuring "
            "3, Enchanting 4; Talismongering 4, Faith Healing 3; Initiate Grade 3 with Centering, "
            "Cleansing and Anchoring; all Health spells at 8; a Medicine Lodge 9 and a healing kit. "
            "Uses: healing, street information, training. Meets only at his personal residence in "
            "the Redmond Barrens; availability 3-6. A character who has Hank as a contact may stop "
            "once per adventure for whatever they need. Note the Cleansing metamagic -- he is "
            "exactly the Initiate the encampment's background count of 4 needs, and he is a "
            "half-hour's walk away in the same district."
        ),
        "contact_skills": [
            "Magical healing, poultices and potions",
            "Redmond Barrens street information",
            "Talismongering and magical training",
        ],
    },
    {
        "name": "Ratman",
        "role": "The Matrix handle whose anonymous tip gave Luxi the LTG address of DocWagon's Fort Lewis host -- and let the tribe believe their totem sent it",
        "archetype": "Decker",
        "title": "Matrix handle \"Ratman\"; one of Luxi's contacts",
        "gender": "Unknown",
        "connection": 2,
        "description": (
            "A name on an e-mail and nothing else. The message contained an address -- on the "
            "Seattle LTG in the decker branch, a street address in Fort Lewis in the other -- and "
            "either way it pointed straight at the DocWagon office that ordered the massacre, "
            "delivered to a Barrens teenager with a tortoise deck within hours of it happening."
        ),
        "background": (
            "One of Luxi's contacts, and the actual source of the second of the adventure's two "
            "leads. Luxi tells the tribe that Rat gave it to him and will keep saying so, because "
            "the totem governs so much of the Raikun's existence that contradicting it is not worth "
            "the trouble. The handle is a joke at the tribe's expense or a coincidence, and the "
            "book does not say which."
        ),
        "notes": (
            "No statistics; never appears. Worth a row because the tip is the load-bearing "
            "coincidence of the adventure and the book leaves it entirely unexplained: somebody who "
            "calls himself Ratman knew within hours which DocWagon office held the organs, and gave "
            "it away for nothing to the one surviving member of the tribe most likely to act on it. "
            "Candidates a GM can pick from: the rigger who filmed the attack and had already sold "
            "the footage; Rose Croix hedging its bets by seeding the tribe as well as hiring "
            "runners; a Doom Squad member with a conscience; or the free spirit itself, working "
            "through a channel Kip cannot audit."
        ),
        "contact_skills": ["Matrix addresses and anonymous tips in the Redmond grid"],
    },
]

ORG_UPDATES = {
    "DocWagon": {
        "notes_append": (
            "SRM 01-03 Harvest Time (days after the Kethers raid): the consequences arrive. With "
            "most of its Type O donor organs and vat-grown stock destroyed or stolen, DocWagon "
            "Seattle cannot meet the reserve clauses in its own contracts, and vat-growing "
            "replacements takes time the bulk of its clients do not have. A memo told Devon Tyler, "
            "the low-profile executive newly responsible for the temporary organ storage facility "
            "at clinic #147 in Fort Lewis, to use any method necessary; he opened Operation LifeRaft "
            "and hired the Doom Squad to murder SINless people for their organs. The street's "
            "corporate legwork ladder gets there on its own: organ theft, too large-scale for black "
            "market dealings, donor organs are the only stopgap while tissue is grown, 'I'd bet on "
            "DocWagon. The word is out that recently their donor organ stocks and vat-grown tissues "
            "were destroyed or stolen.' Security procedures across DocWagon sites have been sharply "
            "raised since the Kethers run. The Doom Squad has also trained some of DocWagon's own "
            "HTR teams. HTR Team Member block p.29: B4(5) Q5(7) S4(6) C2 I3 W4, Ess 0.7, Reaction "
            "4(8), Init 6+1D6 (8+3D6), Combat Pool 8, Karma Pool 3, Professional Rating 3; Car 2, "
            "Biotech 2, Negotiation 3, Pistols 4, Assault Rifle 6, Thrown Weapon (Non Aerodynamic) "
            "4 (6); Medicine 2, DocWagon Procedures 4; datajack, alpha plastic bone lacing, "
            "cybereyes (thermographic, flare compensation), alpha Muscle Replacement 2, smartlink "
            "2, alpha Wired Reflexes 2, Enhanced Articulation; light security armour (6/4, 2,500 "
            "nuyen) with helmet (+1/+2, 75); AK-98 loaded with gel (6M Stun, 750), one concussion "
            "grenade (12M Stun), two flash grenades, two neuro-stun gas grenades (6D Stun), one IR "
            "smoke grenade; commlink Rating 2, silver ID credstick in the individual's name with "
            "1D6 x 1,000 nuyen. Doctrine: a technician always stays aboard the transport, because "
            "teams have been lured out to a site and their vehicles boarded, and the driver "
            "remotely closes and locks every door. Vehicle security (NeoAnarchist's Guide to Real "
            "Life p.100): patient and driver compartments are separate, all doors maglock when the "
            "vehicle is unattended, the patient compartment takes a Rating 5 thumbprint scanner and "
            "the driver's a Rating 6 palmprint, both smart enough to refuse a dead (though not "
            "unconscious) owner or a detached extremity, and a failed bypass transmits a warning to "
            "the team's transceivers; the technicians can also hit an emergency cutoff on the "
            "engine and fuel system. Tyler abuses all of this at the end of the adventure by calling "
            "an HTR team out on the lie that the witness is a kidnapped client -- a breach of "
            "protocol the team itself half-notices (no call on the radios, no signal from the "
            "customer, orders direct from someone senior they cannot name; DocWagon Procedures (4) "
            "spots it) and that the main office eventually corrects by recalling them. Aftermath "
            "(handout): Lone Star raids clinic #147, DOCW drops four points, Tyler is charged as "
            "the mastermind of the organlegging, DocWagon is fined on multiple counts of neglect "
            "and abuse, and civil suits open over the tissue samples and organs lost at the Kethers "
            "Building. Rose Croix nearly doubles its client base."
        ),
        "leadership_add": [
            {"name": "Devon Tyler", "title": "Senior executive, DocWagon Seattle; director of the Fort Lewis organ storage facility (clinic #147)", "notes": "Ordered the Raikun massacre; charged with murder in the first degree."},
        ],
        "enemies_add": ["Raikun"],
        "allies_add": ["Doom Squad"],
    },
    "Rose Croix": {
        "notes_append": (
            "SRM 01-03 Harvest Time: the third move against DocWagon, and the first one Rose Croix "
            "did not start. A rigger scouting the Redmond Barrens for an unrelated run recorded the "
            "Doom Squad's massacre of the Raikun on a drone, recognised it as organlegging, and "
            "sold the footage on -- through a friend of a friend who works at Rose Croix -- for a "
            "handsome fee. The corporation knew it had ordered no such operation and concluded "
            "DocWagon had. The recording would make the centrepiece of a media smear campaign "
            "against the incumbent provider and let Rose Croix pick up disillusioned customers, but "
            "the decision from the top was that more proof was needed, plus the one-eyed man in the "
            "video for an interview. Walter Broward hand-picked Vincent Capello -- a hire from a "
            "local corporation who told Broward at interview that he wanted to be a Mr. Johnson -- "
            "and gave him the job as his first assignment. Rose Croix also has a magical healing "
            "services program, and offered a post in it to the Redmond Barrens street shaman known "
            "as Hank, who turned it down. Aftermath (handout): the evidence and the witness reach "
            "Lone Star through 'anonymous sources', Devon Tyler is charged with murder in the first "
            "degree, DocWagon is fined and sued, and Rose Croix nearly doubles its client base in a "
            "couple of weeks, especially among the high-profile clients. Shadowland's read: 'Lone "
            "Star's anonymous tips came directly from Rose Croix representatives' and 'Rose Croix "
            "has been systematically hitting DocWagon from various angles. I'm betting my nuyen "
            "that the next move is going to be from DocWagon...'"
        ),
        "leadership_add": [
            {"name": "Vincent Capello", "title": "Mr. Johnson", "notes": "Hand-picked by Broward; Harvest Time is his first assignment."},
        ],
    },
    "Lone Star Security": {
        "notes_append": (
            "SRM 01-03 Harvest Time (Seattle, 2064): Lone Star closes the adventure rather than "
            "appearing in it. The clinic guard's PanicButton is the only Lone Star presence during "
            "play. Afterwards, according to its own Public Affairs Office, Lone Star had had its eye "
            "on DocWagon and Devon Tyler for some time when an anonymous tip led detectives to raid "
            "DocWagon clinic #147 in Fort Lewis, where they uncovered over two dozen sets of "
            "DNA-typed organs -- including an eye whose owner, a homeless man missing one, was "
            "positively matched to it. Corroborating drone video reached them from anonymous "
            "sources. Tyler is expected to be convicted of murder in the first degree; his "
            "associates cannot be positively identified and remain at large. The clinic stays "
            "operational and the organs are confiscated. Shadowland's assumption is that every one "
            "of those anonymous inputs came from Rose Croix."
        ),
    },
}

LOC_UPDATES = {}

NPC_UPDATES = {
    "Saint James": {
        "description_append": (
            "SRM 01-03 Harvest Time: he opens the adventure as a voice on the phone late on a cool, "
            "drizzling morning -- a cultured British voice emanating confidence. 'Good evening. "
            "This is Saint James. I have a job opportunity for you. I don't have any details "
            "however, other than it needs to be done with haste, discretion, and professionalism -- "
            "so of course, I immediately thought of you! Strangely enough, so did your prospective "
            "employer -- he asked for you by name.' He books the meet and gets out of it: 'So I "
            "wish you Good Luck, or I'll speak to you next time!'"
        ),
        "notes_append": (
            "SRM 01-03 Harvest Time: Saint James brokers the introduction between Rose Croix's "
            "first-time Johnson, Vincent Capello, and the runners, and takes no part in the "
            "adventure beyond it -- the Johnson asked for the team by name. Runners who worked with "
            "him in SRM 00-02 Demolition Run are recognised and greeted as such, and the book has "
            "him recommending them on the strength of that job. To anyone who did not, the word on "
            "the street is that Saint James is a fixer who can be trusted and who usually handles "
            "high-profile, high-paying shadowruns, and that can be confirmed through the usual "
            "channels. The book uses this to make a teaching point about the trade: the relationship "
            "between a fixer and a Johnson is often very thin, so sometimes a team meets a Johnson "
            "without the fixer's screening -- though a good fixer will time the meet to leave the "
            "runners room to look into things first."
        ),
        "contact_skills_add": ["Introductions to corporate Johnsons"],
    },
    "Michael Davenport": {
        "notes_append": (
            "SRM 01-03 Harvest Time: Broward's campaign background is restated and extended -- he "
            "'has been called the next Damien Knight', his rise at DocWagon hit a glass ceiling at "
            "COO where the CEO's shortsightedness overruled everything he proposed, and he now "
            "intends 'a chess match of shadowruns that would help to weaken the de facto heavyweight "
            "in the sprawl while strengthening Rose Croix'. He is not behind the organlegging: Rose "
            "Croix knew it had ordered no such operation and bought the drone footage from a rigger "
            "through an intermediary because it recognised a weapon when it saw one. His third move "
            "is therefore opportunistic rather than planned, and it works better than either of the "
            "first two -- DocWagon is fined, sued, four points down on the exchange and publicly "
            "tied to the butchery of two dozen SINless, while Rose Croix nearly doubles its client "
            "base. He also personally selected the Johnson who runs it, Vincent Capello, for reasons "
            "Capello has never been told."
        ),
    },
    "Hondo": {
        "notes_append": (
            "SRM 01-03 Harvest Time: posts again on the Shadowland thread after the organlegging "
            "story breaks, and is the one who puts the number on it -- 'Is it any surprise to anyone "
            "that Rose Croix has almost doubled their client base in the past couple of weeks, "
            "especially with the more lucrative high profile clients?' Three adventures running, "
            "Hondo has been ahead of the board on the Rose Croix arc: he called Michael Davenport's "
            "death a staged retirement within a day of it happening, and he is now tracking the "
            "client migration that the whole scheme was built to produce."
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
Two systems, both in SR3 notation. Neither is a major host: the point of the Fort Lewis office is
how weak it is, and how carefully the one door that matters is locked.

**1. DocWagon Fort Lewis office host (clinic #147)** (p.18). A small peripheral office with very few
critical datastores, because everything confidential lives on the main DocWagon host.

Security code: **Green-7/9/10/7/10/8**

| Trigger step | Security event |
|---|---|
| 4 | Probe-4 |
| 8 | Probe-6 |
| 12 | Passive Alert, Trace-8 |
| 16 | Blaster-6 |
| 20 | Active Alert |
| 24 | Shutdown |

Details:
- The host is not sculpted at all and its security is lacking. It is essentially an internal gateway
  to the main DocWagon host, and the only sculpted icon in it is a vault gate leading there.
- **The DocWagon gateway** is the real security. Opening it takes an 8-digit combination AND a
  signature file held in an encrypted chip in the terminal's own hardware -- a peripheral key, so
  that access is only ever possible from selected terminals. In the Fort Lewis office, only Devon
  Tyler's terminal carries the chip.
- A very skilled decker can turn that into a permanent asset. Understanding the encrypted hardware
  key: **Computer (10)**, base time 6 hours. Using it to build an access to DocWagon's main host with
  a personal account: **Computer (15)**, base time two weeks. If achieved, write the permanent access
  through the Fort Lewis office on the Mission Summary sheet.
- **Operation LifeRaft** -- the contact information for the runners DocWagon hired and the details of
  the run -- is protected by **Scramble (6)**.
- A security camera slave continuously records the front door, and the front-door maglock can be
  controlled from here.
- 5,000 nuyen worth of paydata sits in the local office host.
- The slave controls for the temporary organ storage equipment are NOT remotely accessible. The only
  way to reach them is to jack in physically inside the office.

**2. The clinic's office terminals** (p.19). Password protected: Computer (6) with a base time of 30
minutes to get into one directly, or hack them through a cyberterminal as a **Green-4/4/4/4/4/4**
system. They hold organ inventory files, organ request forms and lab analyses -- nothing
incriminating, since DocWagon keeps confidential data on the main host and it cannot be reached from
here. The exception is Devon Tyler's own terminal, which carries the LifeRaft file.

**Not mapped**: the main DocWagon host behind the vault gate (the prize for the decker who spends
two weeks on the hardware key); Rose Croix's systems; the LTG address itself, which Luxi's contact
"Ratman" mailed him and which simply resolves to system 1 above.
"""

NOT_BUILT = """
- **The rigger** who filmed the massacre from a drone while scouting for an unrelated run, and the
  **mutual contact** who brokered the footage to Rose Croix -- deliberately anonymous. The Johnson
  says only that the rigger is unconnected to the attack, that the filming was purely random, that
  no contact information is available, and that he waited until his own run was finished before
  selling. On the Rose Croix row.
- **The two lab technicians** waiting upstairs at clinic #147 for the Doom Squad's next delivery,
  the **four DocWagon technicians** who can open the lab, the **security guard**, the ground-floor
  clinic's **doctors, patients and administrative staff**, and the **HTR team** in the Citymaster --
  stat blocks and behaviour on the DocWagon Clinic #147 and DocWagon rows.
- **The three squatters** in the boarded house -- stat block on that location's row; the Redmond
  Razors who replace them at higher table ratings do get an org row.
- **The two mid-aged women, three crowbar-armed young men and three children** in the sewer refuge,
  and the **Raikun Tribe Member** template -- on the Raikun row.
- **Devil rats** (the optional sewer encounter) -- same block as SRM 01-02; and the **ghosts or
  shedim** offered as a Veteran-and-above hazard at the encampment, which try to take the body of any
  mage who goes astral unprotected.
- **The DocWagon modified Citymaster** and the **Hughes WK-2 Stallion** flown by the aerial response
  team -- the book refers the GM to Rigger 3 rather than printing stats.
- **The other city Rat shaman** who once bound "Rat" as a servant, and the **struggling squatters**
  whose conjuring he hijacked -- backstory on the Rat row.
- **The memo** that told Devon Tyler to use any method necessary, and whoever wrote it -- the single
  most important unnamed thing in the adventure, and the reason Shadowland assumes Tyler is taking a
  fall for his superiors.
- The Shadowland posters on the handout other than Hondo -- **OurTeam**, **Linei**, **The Chromed
  Accountant**, **Bitrunner** and **Deacon Blues** -- board handles with no face; their claims are
  recorded on the Rose Croix, DocWagon and Lone Star rows.
"""

PLAY_NOTES = """
- Everything happens in one day and the clock is diegetic: the attack was at 4 AM, the meet is at
  noon, the witness has to be delivered before 5 PM. Say the deadline out loud and hold to it -- late
  delivery costs a Karma point.
- The adventure is a straight line with one fork, and the fork is the whole design: Kip's lead needs
  a magician, Luxi's needs a decker, and both variants have a no-specialist fallback that turns into
  bodyguarding or a break-in. Pick the branch the table can actually run, and do not offer a branch
  they cannot. Both leads reach the same two answers -- Devon Tyler's name and Operation LifeRaft --
  so nothing is lost either way.
- Tone: the book wants dread, and gives the GM the tools. A background count of 4 over a funeral
  pyre. A dead camp that stinks of chemicals and burnt people. Five minutes of low tunnels where
  low-light vision does not work and orks have to walk in the sewage. Whispering, milky-eyed
  neighbours in SRM 01-02's building were mood; here the mood is grief.
- Shadows Crossing must not become a set-piece. The Doom Squad exists to prove the runners are on
  the right track and that somebody professional is on the other side. Resolve it in about one combat
  turn and twenty minutes of real time; if it drags, have a local ganger or two wade in on the
  runners' side, and let them charge Doom Squad gear as their fee. The squad opens on Mike because he
  looks like the survivor -- protecting him is the scene's actual test.
- The Raikun cannot pay. They have 600 nuyen, a van worth 750, and Kip's four doses of Spirit
  Strength, which he will part with only if the team asks nicely and treats him with respect. Helping
  them anyway is what makes the run work; the book says so and so does the Karma table.
- Sqoosh-Water is much stronger than everything else in the adventure -- Force 4 doubled in its own
  domain, Immunity to Normal Weapons, four targets at once. Run it as a spirit that would rather
  frighten intruders off than fight, lead with Confusion and Fear, and let a clever team leave with
  the barrier down rather than the spirit dead.
- Out of the Rat's Hole is the trap that looks like a fight and is not. The HTR team is on gel
  rounds, is legally entitled to shoot, and is already uneasy: no call came over the radios, no
  signal is coming from the "customer", and the order came from someone senior they cannot name.
  DocWagon Procedures (4) lets a sharp runner name the breach out loud. Convince them Jimbo is not a
  client and they stand down. If the fight starts and runs long, have the main office recall them and
  let the table wonder why.
- Do not let the runners strip the Citymaster. The technicians stay aboard, seal themselves in, and
  can kill the engine and fuel system; the doors need a Rating 5 thumbprint and a Rating 6 palmprint
  that know the difference between an unconscious owner and a dead one, and a failed bypass warns the
  team. Bring in the aerial unit if you have to.
- If time is short at either end: skip the sub-runs and go straight to Jimbo's extraction, or have
  the team escape the sewer mouth by a hair as the Citymaster pulls up. The one thing that cannot be
  cut is delivering Jimbo alive.
- Karma: 2 for Jimbo recovered less than Seriously wounded and before 5 PM, or 1 if he is
  unconscious, Seriously injured or late; 1 more for datafiles implicating DocWagon and Tyler; up to
  3 individual; maximum 5.
- Arc hooks to plant: Mindy's growing suspicion of Rat and what the runners choose to tell her; the
  favour a free spirit now owes the team; who Ratman is; the memo Tyler was following and who wrote
  it; the Doom Squad's surviving members, still at large and now able to identify the team; and
  Deacon Blues's warning that the next move is DocWagon's.
"""
