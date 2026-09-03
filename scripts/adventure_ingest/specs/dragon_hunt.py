# Dragon Hunt (FASA 7307, 1991) -- campaign order #10. Bellevue / Redmond Barrens / Everett /
# Downtown, October 2051 (both news handouts are the Seattle News-Intelligencer of Monday October 9
# 2051; the Dragon checked into Seattle General "last Tuesday at three in the morning"; Blackwing and
# Rhiannon "came back to Seattle in mid-2051"; Cerberus was proposed 4/4/50 and failed 12/29/50).
# The introduction's boilerplate "In the year 2050" is ignored in favor of the dated handouts.
# Source text: docs/Adventures/text/Shadowrun 1e - Dragon Hunt {FASA7307}.txt (63 pages).
# ASCII only (pre-commit hook).
#
# Editing inconsistencies in the book (recorded on the affected rows):
#  - EF's street is "Southampton Street" in the Dragon's speech and Legwork but "Southhampton Street"
#    in The Mad Scientist; "Southampton" is used here.
#  - The earring is worth "probably 50,000 nuyen, maybe more" (p.14) but has a fence base price of
#    10,000 nuyen (p.54).
#  - Grier is "Director of Operations" on her nameplate, calls herself CEO, and the jeweler calls her
#    "head of research"; the Legwork corporate profile lists her as President/CEO.
#  - The KE safehouse living room text says one guard; its stat header says "(Two)".
#  - The Cobalt Marie map posts eight cameras; the Matrix map has seven camera slave nodes.
#  - Eliohann is also spelled "Elighann" and "Eilohann"; "Dragonhunt" and "Dragon Hunt" both appear.
#  - Blackwing's stats differ from Bottled Demon (Essence .16 vs 0.2; Demolitions/Car/Computer dropped;
#    both arms are now Alpha cyberlimbs) -- explained in-world by his San Francisco clinic rebuild after
#    the Dragon bit his right arm off at the elbow.
#  - The Redmond Arms is "six-story" outside but has "only five rooms" inside.
#  - The Karma award numbers on p.52 were lost to OCR; only the categories survive.

ADVENTURE = "Dragon Hunt"
ORDER = 10
SOURCE = "Shadowrun 1e - Dragon Hunt {FASA7307}.pdf, pp. 4-63"
YEAR = "2051 (October)"

SYNOPSIS = """
A fixer offers straight legwork at 2,000 nuyen a day; a voice-only call from hospital orderly
**David Childers** sets a one o'clock meet in the lobby of **Seattle General Hospital**. Up on the
bullet-pocked fourteenth floor, behind Lone Star guards and a weapons detector, the Mr. Johnson is a
seven-meter, green-gold, bandaged **Western Dragon** named **Eliohann**, flipping trideo channels with
a claw. He crashed through the roof last Tuesday at 3 a.m., has amnesia, and wants to know who he is
and who tried to kill him. He remembers three things -- "Cobalt Marie", an old Ork with the tip of his
left ear missing and a coin earring, and "Southampton Street" -- and pays with a diamond-studded gold
earring, a replica of one **Maria Mercurial** wore in her Johnny Disk interview. Two heavily modified
datajacks are hidden under the bandages behind his horns.

What the runners piece together: **Emerging Futures Unlimited**, a small Bellevue think-tank on an
exclusive Ares contract, was handed **Project Cerberus** -- animal minds jacked into cyberspace as
"watchdog" IC -- by **Armand DeHavillier**, an Ares R&D supervisor who forged the authorizations and
skimmed the funding because Ares had turned him down. When dogs failed, **Dr. Justine Grier** had
runner teams kidnap paranormal animals: a griffin, a basilisk, two nagas and a very young dragon who
only got caught because he could not stop staring at their trideo player. Eliohann learned the stock
market from the animal keeper's trideo, stole Grier's wedding ring (and her left arm), terrorized a
burnt-out Ork mage called **Coinspinner** into being his agent, and bought EF out from inside his own
cage, with Coinspinner as the "Chairman's" proxy. Ares found out, panicked, ordered everything
terminated, sued, bought stock, and negotiated at the **Cobalt Marie** -- a hidden Redmond Barrens
club that sells its guests' secrets for favors -- while Coinspinner bribed a **Marie** to leak Ares'
plans. An Ares raid wrecked EF's Barrens research compound; the Dragon forced his datajack surgery;
Grier convinced the Board what their Chairman was; an elimination team went in; Eliohann tore his
cage open, jacked into the prototype Cerberus deck, screamed, and fled through a missile barrage and
**Blackwing's** freelance response team, half-dead and mindless, onto the roof of Seattle General.

The trail runs through a staged robbery at **King Solomon's Mine** in **Bellevue Square** (Handout 1:
sold to Justine Grier), Grier's stonewall and her five-storey fortress on Southampton Street (the
Cerberus proposal and progress report in her desk, and a note asking why she doesn't just kill the
nosy ones), the Persuaders -- Blackwing, **Rhiannon**, **John Whitefeather** and **Render** -- warning
and then hunting the team, the Marie's blinding lasers, Troll guards and trideo vault (Coinspinner's
lighter: a gold "RA" in olive branches, est. 1851 -- the **Redmond Arms Hotel**), and, if they were
loud, **Knight Errant's** safehouse in **Beverly Park, Everett**. Coinspinner, rescued, offers any sum
to save "the boss". The runners shoot their way past thirty of Knight Errant's best into Room 25 --
where the Dragon, freshly signed as an Ares "researcher", asks why on earth he would want rescuing.
Ares pays 50,000 nuyen each for the report and the silence. Outside, it looks like rain.
"""

TIMELINE = """
- **2041** -- Emerging Futures founded. **2045** -- five-year exclusive contract with Ares.
- **4/4/50** -- Ares Cybernetics Research Division drafts Project Cerberus (approved 4/30/50; DeHavillier
  named liaison; research to begin by 6/1/50; four German Shepherds, two Dobermans, a cheetah and a
  Bengal tiger). **12/29/50** -- Grier's progress brief: total failure; proposes paranatural subjects.
- **Early 2051** -- four runner teams deliver a griffin, a basilisk, two nagas and Eliohann. Within
  weeks Cerberus "turns around". **~Spring 2051** -- DeHavillier, under audit, liquidates his own credit
  and stock to keep it alive; Grier cuts the basilisk, a naga, staff and simdeck time; Eliohann begins
  to plan. Coinspinner's astral run; the ring; the Banque Orbitale de Suisse account.
- **Mid-2051** -- Blackwing and Rhiannon return to Seattle and sign on with EF for "security" work.
- **~August 2051** -- Eliohann's takeover agency seizes a majority of EF; Coinspinner sits as proxy
  chairman. DeHavillier's secretary passes Grier's report to Ares internal security; Ares orders
  termination, forms a Corporate Crisis Team, buys EF's remaining stock. **~September** -- Ares sues for
  breach of contract; weeks of negotiations at the Cobalt Marie; Ares raids the EF research compound
  in the Barrens (leaked hours ahead by the Marie).
- **~Late September** -- datajack surgery; Grier persuades the Board; the elimination team; the Dragon
  jacks in, rampages, and flies off under missile fire (Blackwing loses his right arm).
- **Tuesday ~October 3, 3 a.m.** -- Eliohann lands on Seattle General. **Monday October 2** -- Ares and
  EF "settle out of court" (the takeover). **~October 4-8** -- the adventure: the hospital, the
  robbery, EF, the Marie, the Redmond Arms, Beverly Park, the second hospital assault.
- **Monday October 9, 2051** -- Seattle News-Intelligencer: "Ares Announces Takeover" (success) or
  "Hospital Patient Assassinated" (failure).
"""

ORGS = [
    {
        "name": "Emerging Futures Unlimited",
        "org_type": "corporation (research think-tank)",
        "tier": 2,
        "headquarters": "Southampton Street, Bellevue, Seattle (five-storey HQ); research compound in the Redmond Barrens",
        "summary": "Small freelance think-tank on an exclusive Ares contract that secretly ran Project Cerberus, was bought by its own dragon test subject, and is being swallowed by Ares",
        "description": (
            "A small corporate think-tank providing research and feasibility studies to larger corporations "
            "on a freelance basis since 2041 (public profile: hardware and software research and design on "
            "a contractual basis; home office Seattle, UCAS). In 2045 it signed a five-year exclusive "
            "contract with Ares Macrotechnology, expecting only 'spill-over' work but a reputation among the "
            "big boys. Ares R&D supervisor Armand DeHavillier handed it Project Cerberus in 2050 -- animal "
            "minds interfaced with cyberspace as watchdog IC -- with forged authorizations Ares knew "
            "nothing about. Under pressure to succeed, Director of Operations Justine Grier switched to "
            "covertly kidnapped paranatural animals and a very young Western Dragon, Eliohann, who bought "
            "the company out from his cage through the proxy 'Mr. Coinspinner'. Ares learned of the "
            "experiments, ordered everything terminated, sued for breach of contract, bought EF's remaining "
            "stock and raided its Barrens research compound; the Board voted to kill the Dragon and make "
            "peace; the Dragon wrecked the fourth floor and fled. Acting head Grier is now spending major "
            "nuyen on shadowrunners and thugs to hunt Coinspinner and the Dragon and erase every trace of "
            "Cerberus -- files, the stolen data, even the jeweler's records -- and to scare off or kill "
            "anyone who snoops. The street knows only that 'some corp up in Bellevue' is hiring runners "
            "and that Ares is making war on it."
        ),
        "leadership": [
            {"name": "Justine Grier", "title": "President/CEO (nameplate still reads Director of Operations)", "notes": "Dr.; acting head after the Dragon's ouster. Lost her left arm to an Eliohann 'accident'."},
            {"name": "Eliohann", "title": "Chairman of the Board (secret; via proxy)", "notes": "The Dragon test subject; owned a majority of EF until the Ares settlement."},
            {"name": "Coinspinner", "title": "Proxy for the Chairman (former)", "notes": "Old Ork mage; at large with copies of nearly half the Cerberus files."},
            {"name": "Bob", "title": "Research Director", "notes": "First name only, from Grier's memo demanding the Cerberus feasibility study."},
        ],
        "notes": (
            "Five-year Ares contract expires 2050/51. Security: 25 competent, understaffed guards (B5 Q4 "
            "S5 C3 I4 W3, Ess 5.05, R4; Armed Combat 6, Firearms 6, Military Theory 2, Stealth 3, Unarmed "
            "6; low-light cybereyes, radio; armor jacket 5/3, Uzi III), two security mages (B2 Q3 S1 C1 I5 "
            "W3, Magic 6; Sorcery 6, Conjuring 6; Heal Severe Wounds 3, Mana Bolt 6, Powerball 6, Sleep 5; "
            "dressed as guards, cast silently) with a Force 4 Fire and a Force 4 Earth Elemental patrolling "
            "astral space, and a rigger (B5 Q6 S4 C4 I6 W5, Ess 1.4; Car 6, Gunnery 4; VCR 2) with two "
            "hunter/surveillance drones (Body 4, Speed 63; two LMGs, 200 rounds each) sent up the "
            "elevators. Guards shoot first and take no prisoners after the Ares commandos and the Dragon. "
            "Matrix system taken off the network at night against Ares deckers. Cerberus files erased "
            "one week before the adventure under user GRIER-DOP; document inventory of 200+ items in "
            "Grier's desk, nearly half marked as stolen by Coinspinner. Success ending: Ares announces "
            "the takeover (October 9 news) as a condition of an out-of-court settlement, with the story "
            "that EF ran illicit experiments and a bloody cover-up without Ares' knowledge. Company memo "
            "style: 'Bob: Where is the Cerberus feasibility study?'"
        ),
        "allies": ["Blackwing's Team"],
        "enemies": ["Ares Macrotechnology", "Knight Errant Security Services"],
    },
    {
        "name": "Cobalt Marie (owners)",
        "org_type": "secret negotiation club / intelligence broker",
        "tier": 3,
        "headquarters": "The Cobalt Marie, Redmond Barrens (owners unknown)",
        "summary": "The mystery owners of the Cobalt Marie, who sell what corps say in its 'neutral' meeting rooms for favors owed -- five years of favors, none yet cashed",
        "description": (
            "Ostensibly the Cobalt Marie is one of the most exclusive establishments in Seattle, a "
            "fashionable members-only night club with a small, affluent clientele that offers major and "
            "up-and-coming corporations a low-profile, high-security place to relax or negotiate deals "
            "best kept from the public eye -- neutral ground with guaranteed secrecy. What even fewer people "
            "know is that every conference room is closely monitored and the inside information is "
            "offered to the most powerful corporations for a price that is never money, only the promise of "
            "a favor later. Operating this way for five years, the owners have accumulated numerous favors "
            "from the most powerful organizations in Seattle and have cashed none. Who they are remains a "
            "complete mystery. Four women surgically made identical play 'Marie', the hostess everyone "
            "assumes runs the place; thirteen cybered Troll guards, a security mage, technicians and a "
            "bartender stay out of sight."
        ),
        "leadership": [
            {"name": "Marie", "title": "Hostess (four identical women)", "notes": "Cosmetic-surgery twins from the mean streets, combat-trained, always armed; two on site on 12-hour shifts, pairs rotated fortnightly."},
        ],
        "notes": (
            "Hosted the Ares/EF Cerberus negotiations and had 'not yet taken advantage' of leverage from "
            "previous Ares dealings. One Marie, bribed by Coinspinner, fed Ares' plans to EF (including the "
            "raid, hours ahead); the owners found the leak, watched her, overheard her with the runners, "
            "and terminated her ('Security Analysis: ref Marie (informer)... Per orders, subject has been "
            "terminated'). They knew all along where Coinspinner was hiding but held out on Ares for more "
            "favors; if the runners raise an alarm or steal the disks, they hand Ares the trideo. After the "
            "adventure the secret is out and the owners may want the runners silenced. Marie stats: B5 Q4 "
            "S4 C6 I4 W6, Ess 5.04; Etiquette (Corporate) 8, Negotiation 6, Unarmed 6, Firearms 4; "
            "cybereyes, hand razors, radio; DocWagon Platinum. Troll guard stats on the location row."
        ),
        "allies": ["Ares Macrotechnology"],
    },
    {
        "name": "Blackwing's Team",
        "org_type": "shadowrunner team",
        "tier": 1,
        "headquarters": "Seattle (no fixed base); Nightsky and Westwind 2000; retained by Emerging Futures",
        "summary": "The Persuaders: Blackwing, Rhiannon, Whitefeather and Render -- EF's freelance emergency response team turned hit squad",
        "description": (
            "The four-runner team Emerging Futures hired for 'security' work in mid-2051 and sent, at ten "
            "thousand each plus medical, to kill 'the animal' loose on its fourth floor: the fugitive Tir "
            "elven samurai Blackwing, his mate the deserter combat mage Rhiannon, the Salish deserter John "
            "Whitefeather and the Barrens-bred Troll Render, whom Blackwing hired a few months ago. Render "
            "was burned nearly to death and Blackwing lost his right cyberarm at the elbow to the Dragon. "
            "Now Grier's 'best shadowrunner team', used to scare off nosy types -- laser dots and sniper "
            "near-misses, a stranger eating a sandwich in your living room, a car bomb -- and, if that "
            "fails, to kill them one careful stand-off attack at a time, then fade like ghosts. Their "
            "last-ditch attempt on the Dragon at Seattle General comes at the same moment as the runners'."
        ),
        "leadership": [
            {"name": "Blackwing", "title": "Leader; elven street samurai", "notes": "Job first, team second, himself third."},
            {"name": "Rhiannon", "title": "Combat mage", "notes": "Loyal only to Blackwing."},
            {"name": "John Whitefeather", "title": "Point man / heavy weapons", "notes": "Loyal only to himself."},
            {"name": "Render", "title": "Troll muscle; assault cannon and sniper rifle", "notes": None},
        ],
        "notes": (
            "Through Blackwing EF hired three street toughs (and a fixer, now dead by Blackwing's hand) to "
            "rob King Solomon's Mine of its records. Blackwing prefers well-planted bombs, sniping and "
            "ambushes on isolated characters, one attempt at a time; if it misses the team withdraws. "
            "Fill dead members with Mercenary archetypes for the finale. GM: a phobia about runners and "
            "dragons is growing; save Blackwing for later engagements."
        ),
        "allies": ["Emerging Futures Unlimited"],
        "enemies": ["Tir Tairngire", "Knight Errant Security Services"],
    },
    {
        "name": "Banque Orbitale de Suisse",
        "org_type": "bank (orbital)",
        "tier": 4,
        "headquarters": "L-5 orbital station (Swiss)",
        "summary": "Orbital Swiss bank; Eliohann's numbered account holds the fortune that bought Emerging Futures",
        "description": (
            "A Swiss bank operating from the L-5 orbital station, offering numbered accounts beyond any "
            "sprawl government's reach. Eliohann's first deposit was the price of Justine Grier's diamond "
            "wedding ring, sold by the Influenced animal keeper; the profits of the Dragon's stock "
            "portfolio, run through Coinspinner and a corporate-takeover agency, followed until it held a "
            "considerable fortune."
        ),
        "notes": (
            "Coinspinner, as proxy, is legal arbiter of the Dragon's fortune and can promise the runners "
            "'as much money as they want' from it. Whether Ares now controls the account after Eliohann "
            "sold his interest in EF is unstated -- a hook."
        ),
    },
    {
        "name": "DocWagon",
        "org_type": "corporation (emergency medical contracts)",
        "tier": 4,
        "headquarters": "Seattle operations (parent elsewhere; not given)",
        "summary": "Contract emergency medical service; Gold and Platinum contracts carried by Blackwing, Render, Grier and the Maries",
        "description": (
            "The contract emergency-medical service whose Gold and Platinum cards mean an armed response "
            "team and a trauma bay for anyone who can pay. In Dragon Hunt Blackwing carries Gold, Render and "
            "every Cobalt Marie hostess carry Platinum, and Dr. Justine Grier's Platinum coverage bought her "
            "a new left arm after the Dragon's 'accident'."
        ),
        "notes": (
            "Created here as world texture because several stat blocks cite the contracts; an earlier "
            "adventure may already have created it (the loader skips existing names). No DocWagon "
            "personnel appear in the book."
        ),
    },
    {
        "name": "Ueber Corporation",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Not given (news handout)",
        "summary": "High-tech electronics research corp going public for the first time; new parabiology department under Prof. Alexander La Grande",
        "description": (
            "A high-tech electronic research company that announced, in the October 9 2051 business news, "
            "its first public stock offering since its founding. Spokesman Martin Van der Dann also "
            "announced that it had retained Prof. Alexander La Grande for its new parabiology research "
            "department."
        ),
        "leadership": [
            {"name": "Martin Van der Dann", "title": "Executive spokesman", "notes": None},
            {"name": "Prof. Alexander La Grande", "title": "Head, parabiology research department", "notes": "Newly retained."},
        ],
        "notes": "News-handout texture only. A corp buying parabiologists the week Ares buries a paranormal-animal cyberware scandal is a hook the GM can pull.",
    },
    {
        "name": "High Cyber Corporation",
        "org_type": "corporation",
        "tier": 2,
        "headquarters": "Not given (news handout)",
        "summary": "Cybernetics firm taking orders for a new machine for high-risk and contaminated environments (October 2051 news)",
        "description": (
            "Plans to unveil a new cybernetic machine within six months; orders are already being accepted "
            "for work in high-risk and/or highly contaminated environments (Seattle News-Intelligencer, "
            "October 9 2051)."
        ),
        "notes": "News-handout texture only.",
    },
    {
        "name": "Watermark Greetings",
        "org_type": "corporation",
        "tier": 2,
        "headquarters": "Seattle (news handout; address not given)",
        "summary": "Greeting-card corp whose slogan writer Jonathan Trainer was extracted from the Neon Spraygun nightclub; two Watermark Security agents dead",
        "description": (
            "A greeting-card company with its own security arm, Watermark Security. In October 2051 a man "
            "disguised as a waiter shot slogan writer Jonathan Trainer's bodyguard with an MP5TX at the "
            "Neon Spraygun nightclub and fled; Trainer is missing, presumed kidnapped, and two Watermark "
            "Security agents were found dead on a fire escape beside the wreck of a rigged, armed Eurocar "
            "Westwind 2000. Lone Star calls it corporate extraction, 'under investigation'."
        ),
        "notes": "News-handout texture; a ready-made extraction job or revenge hook. The rigged Westwind is the same model Blackwing drives -- coincidence unless the GM decides otherwise.",
    },
]

LOCATIONS = [
    {
        "name": "Seattle General Hospital",
        "location_type": "hospital",
        "district": "Downtown",
        "security_level": "Patrolled / Commercial",
        "summary": "Fourteen-storey central hospital; the Dragon's ward on the bullet-holed top floor; Lone Star lost the security contract to Knight Errant mid-adventure",
        "description": (
            "The city's central hospital: a crowded, quiet, white antiseptic lobby with no shadows to fade "
            "into, a Lone Star guard flirting with the nurses (armor vest, Ares Predator instead of the usual "
            "stun baton, checking in by radio), timid eyes over magazines, thirty people waiting. Ground "
            "floor: nurses' desk, Security Control with camera monitors of the service areas, the "
            "Rating-8-maglocked mainframe room, pharmacy, gift shop, cafeteria, a Cyberware Selections(TM) "
            "office (same-day cyberware) and a Cryotech Sciences(TM) office (cryogenic suspension, 'a 30 "
            "percent average of successful revivification'). Floors 2-14 share a layout: lobby, cyberware "
            "storage, nurses' desk and station, security control, a computer subprocessor room, pharmacy, "
            "records, waiting area, four-bed recovery rooms 16-19 and private rooms 20-25. Floor 14 was "
            "cleared for the Dragon: workmen plaster dozens of bullet holes, a new nurses' desk goes in, "
            "guards in all-seeing visors and heavy armor carry assault rifles, and a weapons detector meets "
            "the elevator. Security Rating A (Sprawl Sites): small blades and pistols get through, nothing "
            "heavier. The Dragon crashed through the roof and ceiling last Tuesday at 3 a.m."
        ),
        "notes": (
            "First visit (Lone Star): five more guards on Turn 3 and ten on Turn 7 if it goes loud; the "
            "orderly will suggest a quieter entrance. Second visit (Knight Errant, after Ares bought the "
            "contract 'at an incredibly high price'): two KE guards at every nurses' station, thirty of "
            "KE's best on 14 -- six in the lobby, two waiting in cyberware storage to hit attackers from "
            "behind, four at the nurses' desk, two in security control, eight in the waiting area, two "
            "each in recovery rooms 16 and 18, and pairs in the hall by the private rooms with an Ares MP "
            "LMG apiece; no weapons allowed; the top floor sits tight and waits. The hospital SAN is "
            "disconnected from the Matrix. Room 25 holds the Dragon, a terrified doctor and two unarmed "
            "Ares officials signing his deal. David Childers waits with a smuggled Uzi III. Blackwing's "
            "team hits at the same moment. Afterwards: ~200 booted feet, medics for the wounded, 50,000 "
            "nuyen each paid in cash in the lobby, out through the service entrance past the reporters. "
            "KE 'rank and file take a dim view of runners who waste 20 to 30 of their comrades'. Failure "
            "news: the only patient on the top floor 'assassinated in a bloody, terrorist-style attack'."
        ),
    },
    {
        "name": "Bellevue Square",
        "location_type": "mall",
        "district": "Bellevue",
        "security_level": "Patrolled / Commercial",
        "summary": "Five-storey open-atrium mall for Eurofashion execs and upper-echelon mobsters; ten-odd jewelry shops; PANICBUTTON brings Lone Star in five minutes",
        "description": (
            "A small mall nestled against a hill in safe, scenic Bellevue, home to well-heeled executives "
            "and upper-echelon mobsters. Five storeys set perpendicular to the street around an open-air "
            "atrium where men and women in the latest Eurofashions sip espresso at white cafe tables and "
            "pretend runners do not exist. Ten or so jewelry shops; King Solomon's Mine is the seventh you "
            "try, on the third floor."
        ),
        "notes": "Two Lone Star patrol cars answer a PANICBUTTON call in four to five minutes -- leave before the SIN questions. Getaway car for the robbery: a tinted, plateless Mitsubishi Runabout a block and a half to the right.",
    },
    {
        "name": "King Solomon's Mine",
        "location_type": "shop",
        "district": "Bellevue (Bellevue Square, third floor)",
        "security_level": "Patrolled / Commercial",
        "summary": "Howard Karascyk's reputation-only custom jewelry shop; made the Dragon's earring for Justine Grier; robbed for its records by EF's hired toughs",
        "description": (
            "No neon, no bars on the small show window, just a simple sign over the door -- a place that "
            "does biz by reputation, one of a handful in Seattle capable of the earring's hand work. A small "
            "track-lit showroom where a trideo projection of Mr. Karascyk appears over each case to describe "
            "the jewels (all fakes -- the owner is eccentric, not stupid); a workshop of machine tools; an "
            "office of faded yellow index cards; a Metals Storage room (Barrier 18, Rating 10 retinal-and-"
            "thumbpad maglock wired to a PANICBUTTON; ten 15-kg boxes, 50,000 nuyen of gold and silver); a "
            "Jewelry Storage room locked the same way and guarded by a Force 4 Fire Elemental (75,000 nuyen "
            "of originals); storeroom; restrooms."
        ),
        "notes": (
            "Three street toughs (B5 Q4 S4 C5 I2 W2; Firearms 4; Remington Roomsweepers, synthetic "
            "leather) hired by a fixer for Blackwing/EF smash the cases, ransack the office, shoot Karascyk "
            "and run for the street with the jewels and the records in a bag; a fourth drives. If the "
            "runners arrive first (Mercurial contacts give the shop's name; otherwise they arrive during "
            "the getaway) Karascyk denies everything until the toughs walk in (Reaction (8) surprise "
            "table). Handout 1, the index card: earring per sketch, customer Justine Grier, Emerging "
            "Futures, 'rush job'. Rhiannon and Blackwing watch from a Nightsky outside and take "
            "descriptions. The toughs' fixer is found dead, Blackwing's work."
        ),
    },
    {
        "name": "Emerging Futures Unlimited Headquarters",
        "location_type": "corporate headquarters",
        "district": "Southampton Street, Bellevue",
        "security_level": "Corporate Standard",
        "controlling_org": "Emerging Futures Unlimited",
        "summary": "Five-storey war-zone of an office block: scaffolding to the fourth floor, 25 guards, drones, elementals, the wrecked Cerberus lab and Grier's desk full of handouts",
        "description": (
            "Halfway down Southampton Street, a five-storey building with scaffolding on two sides where a "
            "whole corner block of fourth-floor windows is being replaced and drifts of crushed glass line "
            "the curb. A burly Ork at the double doors, a Human at the marble lobby's welcome desk, an "
            "elevator with a Rating 6 autonomous weapons detector ('Beep... Subject one is carrying two "
            "weapons') and RAC bracelets -- directional explosive cuffs that sever a limb if cyberware "
            "fires. First floor: HR and PR offices, Security Control (five guards, two mages, the rigger, "
            "drones, four passkeys), the Security Chief's office (Rating 7 maglock, Ruger Super Warhawk), "
            "conference room, technicians, equipment, backup generators, the mainframe room (two guards; "
            "general data only, five minutes to boot), break room. Second and third floors: researchers' "
            "offices (papers everywhere, no Cerberus), workstations, support services, fax/copy/shredder. "
            "Fourth floor (Rating 8 maglocks, failed bypasses alarm Security Control): R&D areas of "
            "unidentifiable machinery, the backup simulation computer (Computer (4): every CERBERUS file "
            "erased a week ago by GRIER-DOP), the Observation Room with both windows shot out, the "
            "Cerberus Prototype Room under repair and still smelling of smoke, and the huge Simsense "
            "Room/Animal Storage of wrecked cerebral monitors, industrial simdecks and cages with a "
            "cartridge still plugged in: 'CERBERUS: Matrix sim 2.0 (penetration simulation)'. Fifth: "
            "executive conference room, the Research Director's office ('Bob: Where is the Cerberus "
            "feasibility study?'), the Computer Services Director's office (a Fairlight Excalibur in the "
            "cabinet), Grier's empty old office and her new President's Office (Rating 9 maglock)."
        ),
        "notes": (
            "Ways in: front doors (Barrier 5, maglock Electronics (5) or the desk switch; 'we didn't order "
            "a pizza'), two first-floor emergency doors (alarm TN 6), a window per room (TN 7), roof "
            "stairwell (TN 5). 25 guards -- four on 5, two each on 2-4, fifteen on 1 -- patrol every 15 "
            "minutes with radios; Security Control locks the elevators to ground, posts two guards per "
            "exit and sends three-quarters of the force plus the drones at the disturbance. Force 4 Fire "
            "and Earth Elementals attack any astral traveler. Go at night. In Grier's desk: the Cerberus "
            "proposal (Handout 2) and progress report (Handout 3), the 200-document inventory with "
            "Coinspinner's thefts asterisked, and the handwritten 'why not just kill the nosy ones off?'. "
            "Grier's daytime office: modest, comfortable, phone always in hand; she pumps visitors for what "
            "they know, denies everything even shown Handout 1, and has four guards show them out. Stats "
            "for guards, mages, rigger and drones on the EF org row."
        ),
    },
    {
        "name": "Emerging Futures Research Compound (Redmond)",
        "location_type": "research lab",
        "district": "Redmond Barrens",
        "security_level": "Corporate Standard",
        "controlling_org": "Emerging Futures Unlimited",
        "summary": "EF's industrial research facility in the Barrens, shot up by an Ares strike team hours after the Cobalt Marie leaked the raid",
        "description": (
            "Emerging Futures' 'research facility in the Redmond Barrens' -- the industrial complex Ares "
            "commandos hit to seize the Cerberus data and kill the test subjects. The Marie leaked the raid "
            "to EF only hours ahead; it was foiled, barely, after severe damage to the compound. The street "
            "version: 'Ares sent a strike team into the Redmond Barrens and shot up some industrial complex. "
            "Looks like war!' The mayor is hot, 'but hey, it's the Barrens, right?'"
        ),
        "notes": (
            "Never mapped; the book conflates it with the Bellevue HQ at points (the Dragon was caged and "
            "jacked in on the HQ's fourth floor; Coinspinner's astral run was 'probing the Emerging Futures "
            "compound'). Use it as the empty, cordoned wreck where the griffin and naga cages once stood, or "
            "as a place EF's guards 'won't forget their run-ins with the Ares commandos'."
        ),
    },
    {
        "name": "The Cobalt Marie",
        "location_type": "nightclub",
        "district": "Redmond Barrens (near NE 75th Street and 151st Avenue NE)",
        "security_level": "Corporate High Security",
        "controlling_org": "Cobalt Marie (owners)",
        "summary": "Hidden corporate negotiating club behind a basement door scrawled 'Marie': blinding lasers, thirteen cybered Trolls, monitored meeting rooms and a vault of trideo disks",
        "description": (
            "A deserted, god-forsaken Barrens street with one grimed-over lamp; a flight of trash-covered "
            "stairs to a basement door with 'Marie' scrawled on it; then total darkness and a narrow "
            "concrete corridor a hundred-plus meters long, lined with weapon detectors, until a tall, "
            "exquisitely beautiful woman in a close-fitting cobalt-blue gown, flame-red curls and glowing "
            "Zeiss cybereyes steps into a pool of white light: 'Welcome to the Cobalt Marie.' Inside, "
            "computers aim weak wall lasers at cybereyes so low-light and thermographic settings haze out; "
            "a bar lit in cobalt blue where extravagantly paid bodyguards nurse drinks; a holostage dance "
            "floor; four luxurious meeting rooms with circular smoke-glass tables, recessed terminals, trid "
            "projectors, stocked bars, couches for aides, a Barrier 20 steel door, a Rating 12 white-noise "
            "generator and a Rating 10 astral barrier apiece -- and hidden cameras and microphones in every "
            "one. The back door is the loading dock of a ruined, rat-infested, burned-out apartment building "
            "a hundred meters from the front, where the Real Foodstuff truck honks four times."
        ),
        "notes": (
            "Nothing heavier than a light pistol; Marie names each armed guest and points to the weapon; "
            "four Trolls step from concealment to hold them. Reservations or a corp name get you in ('EF' "
            "or 'Coinspinner' makes the informer Marie take you to a private room; 'Ares' gets a room "
            "and a wait; anything else, the door). Back door: Barrier 20 steel, Electronics (8). Rooms: "
            "storeroom/kitchen, band room, star's dressing room, two Marie apartments (one occupied, "
            "Rating 5 maglock), meeting areas 7-10, dance floor, main entrance hall (two Trolls per "
            "alcove, magcards), bar, Security Control (technician, entranced astral mage, four Trolls, "
            "four magcards, eight cameras), rest area, armory (TN 10, alarmed; ten FN HAR, four Uzi III, "
            "two Ingram LMGs, 1,000 rounds each, 25 concussion grenades in 'UCAS Military Forces' "
            "crates), computer room (Rating 9; damage the CPU and the system crashes), monitoring room "
            "(Rating 9), main office (TN 9; Barrier 24 safe; the 'informer terminated' report), trideo "
            "editing/storage (open safe, 50 dated disks; four 'Emerging Futures' plus a backup: "
            "Coinspinner stalling Ares, 'the Chairman' never named, and his 'RA est. 1851' lighter). "
            "Troll guards (13): B7(8) Q3(7) S6(10) C1 I2 W1, Ess 0, R2(3); Firearms 5, Unarmed 6, "
            "Etiquette (Corporate) 5; Muscle Replacement 4, Wired 1, smartlink, radio; FN HAR, sap, light "
            "security armor 6/4 -- capture and bludgeon first, rifles once a Troll dies. Security mage: "
            "B2 Q2 S1 C4 I5 W4, Magic 6; Sorcery 6, Conjuring 6; Mana Bolt 6, Powerball 6, Heal Severe 3; "
            "Ares Slivergun. Patrols: 1 on 1D6 per new area meets two Trolls; 10+ on 2D6 the astral mage. "
            "Copy the disks and slip out clean and you beat Ares to Coinspinner (Karma); an alarm or "
            "stolen disks and the Marie sells him out. Matrix map in the prep doc."
        ),
    },
    {
        "name": "Redmond Arms Hotel",
        "location_type": "hotel",
        "district": "Redmond Barrens (western edge, burned-out district)",
        "security_level": "No Security / Barrens",
        "summary": "Burnt-out six-storey flophouse of five rooms where only the desperate hide; Coinspinner's bolt-hole (Room Five); 'RA est. 1851' on his lighter",
        "description": (
            "Dead center of a burned-out section on the western edge of the Redmond Barrens, a place of "
            "disease and dog-sized rats where hunched shapes dart among the rubble and hungry eyes watch. "
            "A six-storey hotel of crumbling brick and sagging concrete in little better shape than the "
            "rubble; ten nuyen at the deserted front desk buys a room number; a single corridor under a "
            "sagging roof leads to the only five rooms it has. Its old logo -- a gold 'RA' in olive "
            "branches, 'est. 1851' -- survives on Coinspinner's lighter. 'Only the really desperate types "
            "try hiding out in there.'"
        ),
        "notes": (
            "Say 'Eliohann' or even 'Dragon' at the door of Room Five and the old Ork lets you in and "
            "explains everything; Intelligence (2) to hear the Knight Errant Citymaster convoy coming and "
            "overhear an officer mention the other team securing the Dragon at Seattle General. Too late "
            "and the street is lined with KE urban personnel carriers, troops in full armor, a K-E "
            "chopper skimming rooftops, ~75 gung-ho troops and five armed APCs, plainclothes investigators "
            "on the steps, and Room Five thoroughly searched. Do not fight them."
        ),
    },
    {
        "name": "Knight Errant Safehouse (Beverly Park)",
        "location_type": "safehouse",
        "district": "Beverly Park, Everett",
        "security_level": "Low Security",
        "controlling_org": "Knight Errant Security Services",
        "summary": "Little-known KE interrogation townhouse in an upper-class Everett neighborhood; six guards, two interrogators, Coinspinner sedated in the guest bedroom",
        "description": (
            "A small townhouse on the outskirts of Seattle in the Beverly Park neighborhood of Everett -- "
            "out in the country, so to speak, in the middle of an upper-class neighborhood where nobody in "
            "their right mind would attack a safe house. Ground floor: living room with a small security "
            "station (monitors for cameras on the front and back doors) and one guard watching trideo, "
            "study (a guard reading, feet on the desk), kitchen (two making sandwiches), dining room (one "
            "playing solitaire), closets. Upstairs: two master bedrooms with the interrogators asleep, a "
            "storage closet, a master bathroom with one guard, two guest bedrooms -- Coinspinner sedated "
            "in the second."
        ),
        "notes": (
            "Address from a street cop, Mr. Johnson, company man, fire fighter or government contact for "
            "1,000 nuyen (-100 per Negotiation success). Guards (six; B5 Q4(6) S5(7) C3 I4 W3, Ess 3.18; "
            "Armed Combat 8, Firearms 8, Demolitions 4, Gunnery 4; low-light eyes, muscle replacement 2, "
            "smartlink, radio; Predator II, FN HAR, partial heavy armor 6/4) call for help and fall back "
            "upstairs; hold 15 minutes and a KE Urban Reaction team arrives, 40 troops in four Citymasters. "
            "Interrogators (two; B6 Q5 S6 C2 I4 W5; Interrogation 5, Firearms 7; Predator II with laser, "
            "lined coat). Losing, the guards trade the prisoner for their lives -- Coinspinner has given "
            "Ares all they will get. Debug: Coinspinner pops a spell or two at their backs."
        ),
    },
    {
        "name": "Neon Spraygun",
        "location_type": "nightclub",
        "district": "Not given (news handout)",
        "security_level": "Patrolled / Commercial",
        "summary": "Nightclub where a waiter-disguised extraction team shot Jonathan Trainer's bodyguard and took him from Watermark Greetings (October 2051 news)",
        "description": (
            "The nightclub in the October 9 2051 news where a man disguised as a waiter shot Watermark "
            "Greetings slogan writer Jonathan Trainer's bodyguard with an MP5TX and fled with Trainer; two "
            "Watermark Security agents were found dead on a fire escape beside a wrecked, rigged, armed "
            "Eurocar Westwind 2000."
        ),
        "notes": "News-handout texture; a venue the GM can furnish for a corporate-extraction hook.",
    },
]

NPCS = [
    {
        "name": "Eliohann",
        "role": "Very young, tech-obsessed Western Dragon: Cerberus test subject, secret Chairman of EF, amnesiac Mr. Johnson, and finally an Ares 'researcher'",
        "archetype": "Western Dragon",
        "title": "Western Dragon; secret Chairman of Emerging Futures; Ares 'researcher' (post-adventure)",
        "race": "Western Dragon",
        "gender": "Male",
        "organization": "Ares Macrotechnology",
        "connection": 4,
        "description": (
            "A mere seven meters long and two at the shoulder, scaled green-gold, lying on the bare floor of "
            "a stripped hospital room under oversized trauma and pressure bandages, an earring on the base "
            "of his left horn and sterile patches over two heavily modified datajacks behind the skull "
            "plate. Speaks politely, distractedly, while flipping trid channels with a claw every thirty "
            "seconds -- rapt at a rocker group, rapt at a children's program about the Matrix -- more "
            "interested in the machine making pictures than in what it shows. 'You have arrived at my hour "
            "of allotted trideo time.' Exposure to the real Matrix left him on the edge of insanity; the "
            "amnesia is trauma, not injury, and under it a Dragon's crafty intelligence and ruthlessness "
            "survive: 'What a Dragon cannot kill, it will seek to control.'"
        ),
        "background": (
            "Awakened only three years ago and gifted with intelligence and magic usually found only among "
            "the greater of his kind, he roamed the mountains of the Sinsearach and Tir Tairngire until a "
            "runner team trapping paranaturals for Cerberus baited him with a small trideo player and a "
            "barrage of tranquilizer darts. Too fascinated by their tech to take revenge, he let himself be "
            "taken to Emerging Futures, hid his abilities (EF filed him as 'pre-adolescent, "
            "average-to-below-average intelligence for type'), became the project's star subject, and "
            "decided information was the hoard he would build at any cost to anyone. He learned the stock "
            "market from the animal keeper's nightly trideo, arranged the 'accident' that cost Dr. Grier her "
            "left arm and her diamond wedding ring, had the Influenced keeper sell it into a Banque "
            "Orbitale de Suisse account, ambushed the astral form of a burnt-out Ork mage and made him his "
            "agent, and bought a majority of EF from inside his cage. When Ares ordered him killed he "
            "forced through the datajack surgery, then woke to an elimination team, rended the cage like "
            "paper, dragged a screaming technician to the prototype deck and jacked in. Cyberspace was "
            "agony; he went berserk, took Blackwing's arm, flew through a missile barrage and came down on "
            "Seattle General with no memory of who he was."
        ),
        "notes": (
            "Stats: B8/4 Q9x3 S20 C4 I6 W8, Ess (10), R5; attacks 10D3, +2 Reach; Defense pools 16/16, "
            "Dodge 9; Powers: Astral Travel, Enhanced Senses, Flame Projection, Influence; Skills: Computer "
            "1. Assensing his orderly shows a powerful suggestion. Pays with the earring only ('I will not "
            "negotiate any further'); wants no daily reports; a week at most. Fragments he remembers: Cobalt "
            "Marie, the Ork's missing ear tip and coin earring, Southampton Street. Ending: Ares' Crisis "
            "Team offered him all the technology and Matrix simulation he wants as a 'researcher' in "
            "exchange for his interest in EF; he did not hesitate. 'This has been a wonderful day so "
            "far... now, what have you to report to me?' A gleam of memory when told he was both subject "
            "and chairman, then sidelong looks at the Ares men. Ares will sequester him in a remote "
            "facility far from Seattle; the runners are not meant to see him again -- but a Dragon "
            "contact who remembers who did his legwork is the book's own suggestion. Even other Dragons "
            "did not know he was in Seattle."
        ),
        "contact_skills": ["A Dragon's favor (if Ares ever lets him call)", "Dragon/Matrix interface research"],
    },
    {
        "name": "Coinspinner",
        "role": "Burnt-out, lucky old Ork mage who became a Dragon's astral go-between and proxy Chairman of EF; on the run with the Cerberus files",
        "archetype": "Street Mage",
        "title": "Proxy for the Chairman of Emerging Futures (former); shadowrunner and mage (burning out)",
        "race": "Ork",
        "gender": "Male",
        "organization": "Emerging Futures Unlimited",
        "connection": 3,
        "description": (
            "An older Ork with scraggly black hair, the tip of his left ear missing and a large coin "
            "earring in the same ear; a deep voice cracking with age; a worn-out man in a chairman's chair. "
            "Tosses a Redmond Arms lighter from hand to hand while he stalls Ares across a table. Frantic "
            "once rescued: 'They have to rescue the boss!'"
        ),
        "background": (
            "Once well known on the streets as a runner and a mage, famous early for his luck -- a security "
            "guard's katana slash, aimed to split his skull, took only the tip of his left ear and a bite of "
            "shoulder armor because he had cocked his head to listen. Believing himself luck incarnate he "
            "took up gambling and a roller-coaster life; when the money and the magic were nearly gone he "
            "tried one last solo run, astrally probing a small think-tank called Emerging Futures. A Dragon "
            "fell on his astral form pretending to be a guardform, drove him almost insane with fear, and "
            "offered a partnership in exchange for his life. Months of astral reports later he was 'Mr. "
            "Coinspinner', the Chairman's proxy, bluffing the Board about a friendly big corp and pushing "
            "for the Dragon's datajack surgery."
        ),
        "notes": (
            "Escaped the fourth-floor massacre with copies of nearly half the Cerberus files as a hostage "
            "against his life ('by morning it would be splashed all over the screamsheets'). Hides in "
            "Room Five of the Redmond Arms; Ares wants him and the data. Legal arbiter of the Dragon's "
            "fortune: offers as much money as the runners want to rescue Eliohann, takes a weapon and comes "
            "along, and explains the whole Introduction synopsis on request. Legwork (Target 8 from "
            "description, 5 from name): 'used to be a real hot mage, then burned out... I think he's "
            "dead' / 'made himself a powerful partner... had to go underground'. Stats: B3 Q3 S2 C3 I4 W5, "
            "Ess 5.5, Magic 1, R3; Conjuring 9, Sorcery 9, Magical Theory 9, Etiquette (Street) 9, "
            "Firearms 4, Stealth 3, Bike 2; smartlink; armor clothing, ritual sorcery materials, Ruger "
            "Super Warhawk. If he survives he stays with the Dragon and the Ares men; the runners never "
            "see him again."
        ),
        "contact_skills": ["Street lore and old-runner gossip (Etiquette Street 9)", "Magical theory and conjuring (rating 9, Magic 1)"],
    },
    {
        "name": "Justine Grier",
        "role": "Dr. Grier: EF's ambitious, one-armed Director of Operations turned acting President, running Cerberus and now burying it with hired guns",
        "archetype": "Corporate Executive",
        "title": "President/CEO (acting), formerly Director of Operations, Emerging Futures Unlimited",
        "race": "Human",
        "gender": "Female",
        "organization": "Emerging Futures Unlimited",
        "connection": 3,
        "description": (
            "Behind a desk buried in papers and reports in a modest, comfortable fifth-floor office, hanging "
            "up the phone as you enter, motioning you to sit without rising; introduces herself as chief "
            "executive officer while the nameplate reads Director of Operations ('recently promoted'). "
            "Cooperative on the surface, pumping for what you know: 'Sorry, I don't know anything about "
            "that. Can I help you with anything else?' Her left arm is a DocWagon Platinum replacement."
        ),
        "background": (
            "Highly skeptical of Project Cerberus and said so, but not about to argue with Ares money. Eight "
            "months in she was ready to report a dismal failure; pressure from above made her switch to "
            "covertly kidnapped paranaturals instead -- 'the key to the entire project'. Never knew Ares had "
            "no idea Cerberus existed. Was the first to suspect who the new Chairman really was and "
            "persuaded the Board to terminate the project, the Dragon, and the war with Ares."
        ),
        "notes": (
            "Orders Blackwing's team to scare off and then kill anyone snooping; pays for the jewelry-shop "
            "robbery; erased every CERBERUS file as GRIER-DOP a week before the adventure. Denies the "
            "earring and the Dragon even shown Handout 1, then has four guards show the runners out and "
            "puts them on her hit list. If kidnapped, the Persuaders hit the snatch hard and she drops a "
            "file case holding Handouts 2 and 3. Her memos: 'Bob: Where is the Cerberus feasibility "
            "study?'; her progress brief of 12/29/50 declared the last German Shepherd brain-dead and "
            "proposed nagas, griffins and basilisks. No stat block; use a corporate executive."
        ),
    },
    {
        "name": "Armand DeHavillier",
        "role": "Ares R&D mid-level supervisor who forged Project Cerberus into existence to buy himself a vice-presidency; now under internal audit and informed on",
        "archetype": "Corporate Executive",
        "title": "Mid-level supervisor, Ares Research and Development (Cybernetics Research Division liaison)",
        "race": "Human",
        "gender": "Male",
        "organization": "Ares Macrotechnology",
        "connection": 2,
        "description": (
            "A mid-level manager with his sights on an executive vice-presidency, hunting the 'Golden "
            "Project' that would open the road to promotion. Off-stage throughout; his name is on Handouts "
            "2 and 3 as EF's liaison with Ares Cybernetics Research Division."
        ),
        "background": (
            "When Ares would not accept his idea -- a stopgap between IC and AI, animal minds going 'naked' "
            "into the Matrix behind a behavioral analog interpreter -- he skimmed funding from a hundred "
            "smaller projects, forged the authorizations and quietly gave the work to subcontractor "
            "Emerging Futures in 2050, meaning to present the results when the time was right. Halfway to "
            "his vice-presidency a year later and under intense internal audit, he liquidated his own credit "
            "and stock to keep Cerberus alive -- not half what it needed."
        ),
        "notes": (
            "His secretary was an Ares internal-security informant and passed Grier's progress report "
            "upstairs; Ares reacted with panic. His fate is not stated -- the 'big internal shakeup over at "
            "Ares' in the Legwork is presumably him. A ruined man who knows exactly what Ares is now "
            "researching with the Dragon: a hook."
        ),
    },
    {
        "name": "David Childers",
        "role": "Young Seattle General orderly under the Dragon's Influence; the voice on the phone, the guide upstairs, and the surprise Uzi in the finale",
        "archetype": "Hospital Orderly",
        "title": "Orderly, Seattle General Hospital",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": (
            "A young man with a distant, almost distracted air who will not make conversation; assensing "
            "shows a powerful form of suggestion. Spreads his hands and smiles in the lobby: 'You must be "
            "the people here to visit Mr. Johnson. Please follow me.' Lives in a downtown apartment with "
            "nothing of value in it and knows nothing about the job beyond the meet."
        ),
        "notes": (
            "The Dragon's Influence instills a strange loyalty. Kept away from Eliohann once the Ares men "
            "arrive, he smuggles an Uzi III in through the service entrance and hangs around waiting for a "
            "chance to shoot his way in -- an ace-in-the-hole the GM can spend when the runners most need "
            "help. Stats: B2 Q3 S2 C2 I4 W2, Ess 5.8; datajack; Biotech 3, Firearms 2, Unarmed 1. If he "
            "survives he stays with the Dragon and is never seen again."
        ),
    },
    {
        "name": "Rhiannon",
        "role": "Elven combat mage who deserted the Tir Tairngire military to break Blackwing out of his death cell; his mate and only loyalty",
        "archetype": "Combat Mage",
        "title": "Combat mage, Blackwing's team; deserter, Tir Tairngire military",
        "race": "Elf",
        "gender": "Female",
        "nationality": "Tir Tairngire",
        "organization": "Blackwing's Team",
        "connection": 3,
        "description": (
            "Quiet and reserved with a will of iron; compassionate (it is she who cannot look away from the "
            "dying Elf guard) yet generally disdainful of Humans. Gloved finger to her lover's lips: 'Enough "
            "words over what can't be helped.' Calls from an alley -- 'I wouldn't do that if I were you' -- "
            "as your car explodes."
        ),
        "background": (
            "Met Blackwing in the Tir as casual lovers; only when he was sentenced to die for treason did she "
            "discover how deeply she cared. She threw her career away, broke him out of his prison cell and "
            "fled with him to the California Free State and San Francisco, returning to Seattle in mid-2051."
        ),
        "notes": (
            "Stats: B2(4) Q4 S2 C2 I5 W5, Ess 5.1, Magic 5, R4(8); Sorcery 6, Magical Theory 4, Conjuring "
            "3, Firearms 3; hypoallergenic boosted reflexes 1 and smartlink; Power Focus 1; spell locks "
            "Armor and Personal Combat Sense; HK227, Ruger Super Warhawk, flash-paks, armor jacket 3/2. "
            "Spells: Manaball 5, Mana Bolt 5, Power Bolt 5, Clairvoyance 5, Detect Enemies 2, Detect Guns "
            "4, Personal Combat Sense 5, Heal Moderate Wounds 3, Increase Reaction +2, Mask 3, Armor 5, "
            "Confusion 4. Low-light eyes; plastic allergy (nuisance). Stabilized Render after the Dragon's "
            "flame. Drives the Nightsky outside Bellevue Square."
        ),
    },
    {
        "name": "John Whitefeather",
        "role": "Salish tribal-military deserter playing the grinning madman on point; cold, calculating, loyal to nobody but his next nuyen",
        "archetype": "Mercenary",
        "title": "Point man and heavy weapons, Blackwing's team",
        "race": "Human",
        "gender": "Male",
        "nationality": "Salish (Salish-Shidhe Council)",
        "organization": "Blackwing's Team",
        "connection": 2,
        "description": (
            "Massive shoulders, a maniac's laugh and a manic grin -- 'You ever eat fried lizard, man? Good "
            "stuff' -- seemingly carefree while bullets fly. The act hides a cold, calculating mind that "
            "only cares where the next nuyen is coming from. Found on your own chair eating a sandwich and "
            "watching your trideo: 'Get in here! You're missing the best part!'"
        ),
        "background": (
            "Called the Son of Coyote by his parents, he grew up a scoundrel and hellion among the Salish "
            "tribe of Washington State until his father forced him into the tribal military to teach him "
            "maturity. He took to the training and rebelled against every authority, deserted to avoid a "
            "court-martial, and drifted to Seattle, where a Troll named Render pulled him out of a knife "
            "fight with a gang of Orks. Blackwing hired the pair a few months ago."
        ),
        "notes": (
            "Stats: B6 Q6 S6 C3 I5 W4, Ess 5.3, R5; Firearms 5, Etiquette (Street) 5, (Tribal) 4, Armed "
            "Combat 3, Athletics 3, Car 3, Stealth 3, Unarmed 3; low-light retinal mod, smartlink; Beretta "
            "Model 70 with gas vent, armor clothing 3/0, medkit, survival knife, trauma patches; an Ares GPMG "
            "in the prologue. Burned by the Dragon's flame but functional. Delivers the 'maybe I planted a "
            "bomb' warning."
        ),
    },
    {
        "name": "Render",
        "role": "Redmond-bred Troll survivor with a Panther assault cannon and a laser-sighted sniper rifle; Whitefeather's partner, Blackwing's muscle",
        "archetype": "Street Samurai",
        "title": "Troll heavy, Blackwing's team",
        "race": "Troll",
        "gender": "Male",
        "organization": "Blackwing's Team",
        "connection": 2,
        "description": (
            "Huge and misshapen, given to staring into space lost in some reverie, a Panther assault cannon "
            "looking like a mere rifle in his hands. 'Big lizard. Big deal.' Cold, cynical and brutal; "
            "something about a lunatic Human's attitude once amused him enough to save the man he had meant "
            "to mug."
        ),
        "background": (
            "Born and raised in the hell called the Redmond Barrens, abandoned by his parents, a hard "
            "survivor of the streets by thirteen. Took protection money from John Whitefeather after pulling "
            "him out of a knife fight with Orks and has worked the streets as his partner since; hired by "
            "Blackwing a few months ago. Nearly burned to death by the Dragon on EF's fourth floor and "
            "stabilized by Rhiannon."
        ),
        "notes": (
            "Stats: B7(8) Q3(7) S6(10) C1 I2 W1, Ess 0, R2(3); Unarmed 6, Firearms 5, Throwing Weapons 5, "
            "Bike 4, Etiquette (Street) 5; Muscle Replacement 4, Wired Reflexes 1; Panther Assault Cannon "
            "on a gyro mount, Range Arms SM-3 sniper rifle (the laser dot on your forehead), Remington "
            "Roomsweeper, smart goggles, armor jacket 3/0, Harley Scorpion, DocWagon Platinum. +1 Reach, "
            "dermal armor 1, thermographic eyes; silver allergy (mild)."
        ),
    },
    {
        "name": "Howard Karascyk",
        "role": "Eccentric old master jeweler of King Solomon's Mine who made the Dragon's earring and is gunned down for his index cards",
        "archetype": "Jeweler",
        "title": "Owner and jeweler, King Solomon's Mine (Bellevue Square)",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": (
            "An old man who comes out of the back room -- 'Can I be of service?' -- and appears again as a "
            "trideo ghost over every display case describing his work. Keeps his records on faded yellow "
            "index cards, his display jewels fake, his originals behind a Fire Elemental, and his clients' "
            "names to himself. Eccentric, not stupid."
        ),
        "notes": (
            "Made the earring as a rush job for Justine Grier of Emerging Futures. Adamantly denies it "
            "until the toughs arrive; if the runners save him he is grateful enough to hand over Handout 1 "
            "at once. Arrive late and he lies fatally shot in the workshop with the PANICBUTTON on his "
            "wrist telecomm already tripped. A first-rate custom jeweler who owes the team his life is a "
            "fine contact."
        ),
        "contact_skills": ["Custom jewelry and fine metalwork (one of a handful in Seattle)", "Who commissions what from Bellevue's rich"],
    },
    {
        "name": "Marie (the informer)",
        "role": "The Cobalt Marie hostess Coinspinner bribed to leak Ares' plans to EF; mistakes the runners for his people and is terminated for it",
        "archetype": "Hostess",
        "title": "Hostess, the Cobalt Marie (one of four identical 'Maries'); EF's informer (terminated)",
        "race": "Human",
        "gender": "Female",
        "organization": "Cobalt Marie (owners)",
        "connection": 2,
        "description": (
            "Tall and exquisitely beautiful in a close-fitting cobalt-blue gown, flame-red curls to her "
            "shoulders, Zeiss cybereyes that shine with their own light, a low husky voice and an enigmatic "
            "smile -- until the steel door seals and the pretense drops: 'You're obviously working for "
            "Coinspinner. Where the hell have you guys been?' New to the informer game and not entirely "
            "logical about it."
        ),
        "background": (
            "Delivered from the mean streets, surgically made identical to three other women so that "
            "'Marie' can greet corporate guests around the clock, combat-trained and always armed. Took "
            "Coinspinner's bribe to feed EF what Ares said in the meeting rooms -- including the raid on the "
            "research compound, hours ahead."
        ),
        "notes": (
            "Tells the runners she cannot pass 'your boss' any more information -- 'these people play for "
            "keeps' -- moments before Central overrides the door and the Ares men walk in; two Trolls take "
            "her arms and the main-office report later reads 'Per orders, subject has been terminated'. "
            "Another Marie takes her place and offers drinks. Stats (all Maries): B5 Q4 S4 C6 I4 W6, Ess "
            "5.04; Etiquette (Corporate) 8, Negotiation 6, Unarmed 6, Firearms 4, Armed Combat 3; "
            "cybereyes, hand razors, radio; DocWagon Platinum."
        ),
    },
    {
        "name": "Sgt. Jonathan Phillips",
        "role": "Quotable Lone Star sergeant on the downtown squatter-gang massacre who smells Yakuza",
        "archetype": "Police Officer",
        "title": "Sergeant, Lone Star Security",
        "race": "Human",
        "gender": "Male",
        "organization": "Lone Star Security",
        "connection": 2,
        "description": (
            "The Lone Star sergeant quoted in the October 9 2051 news after six bodies of a local squatter "
            "gang were found in the alleys behind a favorite downtown establishment: 'I haven't seen "
            "mangled bodies like that since the riots at the last combat bike championships.' Speculates "
            "the condition of the bodies points to Yakuza involvement; 15-20 men, 2:30 a.m."
        ),
        "notes": "News-handout texture; a Lone Star street contact with a taste for combat biking.",
        "contact_skills": ["Lone Star downtown patrol gossip"],
    },
    {
        "name": "Edgar Kepple",
        "role": "Former Global Technologies VP (TerraForming Division) found suffocated in his downtown apartment five days after resigning",
        "archetype": "Corporate Executive",
        "title": "Former Vice President, TerraForming Division, Global Technologies (deceased)",
        "race": "Human",
        "gender": "Male",
        "organization": "Global Technologies",
        "connection": 1,
        "description": (
            "Found dead in his bed at 8:14 a.m. by his girlfriend Lisa Lechenko in his downtown Seattle "
            "apartment; cause of death apparently suffocation, five days after announcing his resignation. "
            "'A very kind man, he loved this planet and its people,' says his successor."
        ),
        "notes": "News handout, October 9 2051. Responsible for much of Global Tech's work in NAN lands. Lone Star has not said whether Lechenko is a suspect. A murder hook.",
    },
    {
        "name": "David Wuo",
        "role": "Global Technologies' new VP and head of the TerraForming Division, warm about the predecessor who died the day he took over",
        "archetype": "Corporate Executive",
        "title": "Vice President and Head, TerraForming Division, Global Technologies",
        "race": "Human",
        "gender": "Male",
        "organization": "Global Technologies",
        "connection": 2,
        "description": "Appointed the day Edgar Kepple was found dead: 'I only hope I can continue the fine work he began with as much success.'",
        "notes": "News handout, October 9 2051. Whether he had anything to do with Kepple's death is the GM's call.",
    },
    {
        "name": "Lisa Lechenko",
        "role": "Edgar Kepple's girlfriend, who found him dead; Lone Star will not say whether she is a suspect",
        "archetype": "Civilian",
        "title": "Girlfriend of the late Edgar Kepple",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": "Found Kepple in his bed at 8:14 a.m. in his downtown apartment (October 9 2051 news).",
        "notes": "News-handout texture; a witness or suspect for a murder hook.",
    },
    {
        "name": "Jonathan Trainer",
        "role": "Watermark Greetings slogan writer extracted at gunpoint from the Neon Spraygun; missing, presumed kidnapped",
        "archetype": "Corporate Wage Slave",
        "title": "Slogan writer, Watermark Greetings (missing)",
        "race": "Human",
        "gender": "Male",
        "organization": "Watermark Greetings",
        "connection": 1,
        "description": "A greeting-card slogan writer important enough to have a bodyguard, a security detail and a rigged Westwind -- and to be worth a professional extraction (October 9 2051 news).",
        "notes": "News-handout texture; why anyone would extract a slogan writer is the hook.",
    },
    {
        "name": "Martin Van der Dann",
        "role": "Ueber Corporation executive who announced its first public offering and its new parabiology department",
        "archetype": "Corporate Executive",
        "title": "Executive spokesman, Ueber Corporation",
        "race": "Human",
        "gender": "Male",
        "organization": "Ueber Corporation",
        "connection": 2,
        "description": "The Ueber executive quoted in the October 9 2051 business news announcing the stock offering and the hiring of Prof. Alexander La Grande.",
        "notes": "News-handout texture.",
    },
    {
        "name": "Prof. Alexander La Grande",
        "role": "Parabiologist newly retained to head Ueber Corporation's parabiology research department",
        "archetype": "Scientist",
        "title": "Head, parabiology research department, Ueber Corporation",
        "race": "Human",
        "gender": "Male",
        "organization": "Ueber Corporation",
        "connection": 2,
        "description": "An academic parabiologist hired into corporate research the same week Ares buries a paranatural-animal experiment (October 9 2051 news).",
        "notes": "News-handout texture; a plausible expert on dragons, nagas and griffins for a later run.",
        "contact_skills": ["Parabiology / paranatural animals (academic)"],
    },
]

ORG_UPDATES = {
    "Ares Macrotechnology": {
        "description_append": (
            "Dragon Hunt (public profile, 2051): home office Detroit, Michigan, UCAS; President/CEO Damien "
            "Knight; principal divisions Knight Errant Security (head Roger Soaring Owl -- multi-faceted "
            "private and corporate security, physical, magical and electronic) and Ares Arms (head Guido "
            "Cantarelli -- military and police equipment from small arms to top-line combat vehicles). "
            "Also Ares Research and Development / Ares Labs Cybernetics Research Division."
        ),
        "notes_append": (
            "Dragon Hunt: Ares never authorized Project Cerberus -- R&D supervisor Armand DeHavillier forged "
            "it and skimmed a hundred budgets -- and learned of it only when his secretary, an internal-"
            "security informant, passed up Grier's report. Imagining animal-rights outrage and Great "
            "Dragons like Lofwyr finding out, Ares ordered EF to terminate the project and all subjects, "
            "formed a Corporate Crisis Team, bought all of EF's remaining stock within a day, sued for "
            "breach of contract, considered killing Cerberus staff likely to talk, negotiated at the Cobalt "
            "Marie (whose owners now hold unused leverage over Ares), and authorized a commando raid on EF's "
            "Barrens research compound. Its men at the Marie carry Knight Errant intelligence dossiers on "
            "the runners and treat intimidation with genuine amusement; a plastic card makes an irate Lone "
            "Star cop apologize. Its Seattle central complex is behind a gatehouse half a kilometer out and "
            "'breaking in would be an elaborate form of suicide'. Ending: bought Seattle General's security "
            "contract from Lone Star, signed the Dragon as a 'researcher' in exchange for his EF interest "
            "(continued Matrix/Dragon interface research), pays the runners 50,000 nuyen each for their "
            "report and silence, pins the illicit experiments and bloody cover-up on EF, announces the "
            "takeover (October 9 2051), and will sequester Eliohann in a remote facility far from Seattle. "
            "Legwork: 'some big internal shakeup over at Ares'; Knight Errant undercover investigators "
            "rough up anyone who asks too much."
        ),
        "leadership_add": [
            {"name": "Damien Knight", "title": "President/CEO", "notes": "Dragon Hunt public profile."},
            {"name": "Roger Soaring Owl", "title": "Division Head, Knight Errant Security", "notes": "Dragon Hunt public profile."},
            {"name": "Guido Cantarelli", "title": "Division Head, Ares Arms", "notes": "Dragon Hunt public profile."},
            {"name": "Armand DeHavillier", "title": "Mid-level supervisor, Research and Development", "notes": "Forged Project Cerberus; under internal audit (Dragon Hunt)."},
        ],
        "enemies_add": ["Emerging Futures Unlimited"],
        "allies_add": ["Cobalt Marie (owners)"],
    },
    "Knight Errant Security Services": {
        "notes_append": (
            "Dragon Hunt (October 2051): Ares' security arm (head Roger Soaring Owl) is everywhere in this "
            "run. Its intelligence section faxes complete dossiers -- vital statistics and a log of past "
            "exploits -- on the runners to the Marie within minutes. Its 'security teams' flash a card and "
            "walk away from Lone Star. It takes the Redmond Arms with ~75 troops in full armor, five APCs "
            "with turret MGs, a K-E chopper and Citymasters, led by a short, bald, bespectacled "
            "plainclothes investigator in a synth-leather trenchcoat ('You are amateurs in a game of "
            "professionals'). It runs a little-known interrogation safehouse in Beverly Park, Everett (six "
            "guards, two interrogators, an Urban Reaction team of 40 in four Citymasters 15 minutes out) "
            "and, after Ares bought the contract from Lone Star, guards Seattle General with thirty of its "
            "best on the Dragon's floor. Guard stats: B5 Q4(6) S5(7) C3 I4 W3, Ess 3.18; Armed Combat 8, "
            "Firearms 8, Demolitions 4, Gunnery 4; low-light eyes, muscle replacement 2, smartlink, radio; "
            "Predator II, FN HAR, partial heavy armor 6/4, survival knife; some carry Ares MP LMGs. A "
            "senior guard may recognize Coinspinner and stand aside. Afterwards the rank and file 'take a "
            "dim view of runners who waste 20 to 30 of their comrades' -- a real bad rep. Joint statement "
            "with Lone Star if the Dragon dies."
        ),
        "leadership_add": [
            {"name": "Roger Soaring Owl", "title": "Division Head", "notes": "Dragon Hunt public profile of Ares."},
        ],
        "enemies_add": ["Emerging Futures Unlimited", "Blackwing's Team"],
    },
    "Lone Star Security": {
        "notes_append": (
            "Dragon Hunt (October 2051): held Seattle General's security contract when the Dragon crashed "
            "through the roof -- a lobby officer in an armor vest with a Predator instead of a stun baton "
            "radioing every few minutes, heavy-armor guards with assault rifles, an Ingram LMG and a "
            "weapons detector on the cleared fourteenth floor; Security Rating A, small blades and pistols "
            "tolerated, a bribe gets the rest 'kept an eye on', otherwise an arrest attempt and five more "
            "guards on Turn 3, ten on Turn 7. Ares then bought the contract out from under it at an "
            "incredibly high price and Knight Errant moved in. Two patrol cars answer Bellevue Square's "
            "PANICBUTTON in four to five minutes. A Knight Errant 'security team' leader's plastic card makes "
            "an irate Lone Star cop hand it back and apologize. News: Sgt. Jonathan Phillips on the "
            "downtown squatter-gang massacre (Yakuza suspected); 'under investigation' on the Watermark "
            "extraction; no comment on Lisa Lechenko."
        ),
    },
    "Tir Tairngire": {
        "notes_append": (
            "Dragon Hunt: the unnamed noble who hired Blackwing in Bottled Demon claimed the samurai tried "
            "to double-cross him with a forgery of the idol; Blackwing was found guilty of treason and "
            "sentenced to death, and the Tir military combat mage Rhiannon deserted to break him out of "
            "his cell and flee to the California Free State. Both are back in Seattle from mid-2051 working "
            "for Emerging Futures. Grier's progress brief notes 'the tremendous amount of legal protection "
            "granted to paranatural animals by both the Indian States and Tir Tairngire', which is why "
            "Cerberus subjects were acquired covertly; the young dragon Eliohann roamed the mountains of "
            "the Sinsearach and the Tir before runners trapped him."
        ),
        "enemies_add": ["Blackwing's Team"],
    },
    "Salish-Shidhe Council": {
        "notes_append": (
            "Dragon Hunt: John Whitefeather, 'Son of Coyote', grew up among the Salish tribe of Washington "
            "State, was forced into the tribal military by his father, rebelled, and deserted to Seattle to "
            "avoid a court-martial; he now runs with Blackwing. Paranatural animals enjoy strong legal "
            "protection in the Indian States, so EF's dragon, griffin, nagas and basilisk were poached "
            "covertly. Global Technologies' late VP Edgar Kepple ran its TerraForming work in NAN lands."
        ),
    },
    "Mitsuhama Computer Technologies": {
        "notes_append": (
            "Dragon Hunt (Seattle News-Intelligencer, October 9 2051): corporate spokesmen denied reports "
            "that the Mitsuhama corporate helistat research station had been destroyed over the Gulf of "
            "Mexico -- it was 'only damaged' by tropical storm Laura."
        ),
    },
    "Global Technologies": {
        "notes_append": (
            "Dragon Hunt (Seattle News-Intelligencer, October 9 2051): 'GLOBAL TECH VP DEAD' -- former Vice "
            "President Edgar Kepple, head of GT's TerraForming Division and responsible for much of its work "
            "in NAN lands, found suffocated in his downtown apartment five days after resigning; David Wuo "
            "takes over the division. DISCREPANCY: Dreamchipper describes Global Technologies as a "
            "127-person Bellevue skillsoft house with no such division; either the news refers to a "
            "different, larger 'Global Technologies' or the company diversified wildly in a year. Recorded, "
            "not reconciled."
        ),
        "leadership_add": [
            {"name": "Edgar Kepple", "title": "Former Vice President, TerraForming Division (deceased)", "notes": "Dragon Hunt news, October 2051; see discrepancy note."},
            {"name": "David Wuo", "title": "Vice President and Head, TerraForming Division", "notes": "Dragon Hunt news, October 2051."},
        ],
    },
    "Seattle News-Intelligencer": {
        "notes_append": (
            "Dragon Hunt: Update-Net edition of Monday October 9 2051, 14:00 (compiled by Ken Hlavic, "
            "Walter Smith and T. Gallagher; bylines M. Perneta, M. Lee, 'Sirpriz', M. Stackpole). Stories: "
            "Montreal Public Health Ministry denies a new rogue VITAS strain (unnamed sources: 16 UCAS "
            "visitors dead, 6 in isolation); Ueber Corporation goes public and hires parabiologist Prof. "
            "Alexander La Grande; High Cyber Corporation's new machine for contaminated environments; "
            "Mitsuhama's storm-damaged helistat; the Fortified Twist dance craze (osteopath Marcus "
            "Brannigan on the morning after); the Kingdome ready for next weekend's Panzer Pull after fire "
            "damage in the Battle of the Super Bruisers; the Watermark Greetings extraction at the Neon "
            "Spraygun; 'Battles in the Street' (six squatter-gang dead downtown, Yakuza suspected); "
            "'Global Tech VP Dead'; and either 'Ares Announces Takeover' of Emerging Futures (settled out "
            "of court 'unexpectedly last Monday') or 'Hospital Patient Assassinated' at Seattle General."
        ),
    },
    "Yakuza (Watada-rengo)": {
        "notes_append": (
            "Dragon Hunt (October 9 2051 news): Lone Star Sgt. Jonathan Phillips speculated that the "
            "condition of six mangled squatter-gang bodies found behind a favorite downtown establishment "
            "after a 2:30 a.m. firefight of 15-20 men 'indicated Yakuza involvement'. Names withheld."
        ),
    },
}

LOC_UPDATES = {
    "The Barrens (Seattle)": {
        "notes_append": (
            "Dragon Hunt: the Cobalt Marie hides under a basement door in a deserted Redmond Barrens "
            "street (legwork points to NE 75th Street and 151st Avenue NE) behind a burned-out apartment "
            "block; the Redmond Arms Hotel rots at the dead center of a burned-out district on the "
            "Barrens' western edge among dog-sized rats; Emerging Futures' research compound in the "
            "Barrens was shot up by an Ares strike team ('the mayor's hot, but hey, it's the Barrens'). "
            "Squatters sell bum directions for a two-nuyen bribe and vanish. Render was raised here."
        ),
    },
    "The Kingdome": {
        "notes_append": (
            "Dragon Hunt (October 9 2051 news): Kingdome officials affirm the playing field will be ready "
            "for next weekend's Panzer Pull after extensive fire damage during this past weekend's Battle "
            "of the Super Bruisers."
        ),
    },
}

NPC_UPDATES = {
    "Blackwing": {
        "background_append": (
            "Dragon Hunt: the Tir noble claimed Blackwing tried to double-cross him with a forgery of the "
            "idol; he was found guilty of treason and sentenced to death. Rhiannon, his casual lover in the "
            "Tir, broke him out of his cell and they fled to the California Free State and San Francisco, "
            "where a shadow clinic reworked his chrome. Back in Seattle from mid-2051 doing 'security' work "
            "for Emerging Futures with Rhiannon, John Whitefeather and Render, he led the freelance response "
            "team sent to kill EF's escaped 'animal' -- warned the Shaikujin it was a Dragon, went 'right "
            "down its throat' with an iaido drawcut, and lost his right cyberarm at the elbow to its teeth. "
            "Toward runners who survived Bottled Demon he feels respect, gratitude for saving his life at "
            "Lochlann, and bitterness: he holds them responsible for his failure and the treason charge, so "
            "he discharges the debt with a warning first ('take a long vacation, far away from this grimy "
            "city') and tries to kill them if they ignore it."
        ),
        "notes_append": (
            "Dragon Hunt: Grier's 'best shadowrunner team' -- the Persuaders. Stand-off attacks only: "
            "bombs, sniping, ambushes on isolated characters, one at a time, then fade. Assaults Seattle "
            "General to kill the Dragon at the same moment as the runners' rescue. Stats (Dragon Hunt): "
            "B5(6) Q6 S4(7) C3 I5 W5, Ess .16, R5(11) +3D6; Firearms 8, Unarmed 7, Armed Combat 5, "
            "Etiquette (Street) 5; Alpha cyberware: both arms cyberlimbs with smartlink and Increased "
            "Strength 3, cyberears with hearing amplification, radio, Wired Reflexes 3; Ares Predator, FN "
            "HAR with gas vent 2, katana (7M3), tres chic armor clothing 3/0, Eurocar Westwind 2000, "
            "DocWagon Gold; low-light eyes, sunlight allergy (nuisance). DISCREPANCY with Bottled Demon: "
            "Essence .16 vs 0.2 and no Demolitions/Car/Computer listed -- the San Francisco rebuild. Swears "
            "by 'the Bright Lady'. 'He is too good an NPC to waste'; developing a phobia about runners and "
            "Dragons."
        ),
    },
    "Maria Mercurial": {
        "notes_append": (
            "Dragon Hunt: the young dragon Eliohann became infatuated with an earring Maria wore in her "
            "Johnny Disk interview -- a gem-studded gold band with a hanging globe of gold leaf set with "
            "diamonds -- and had Dr. Grier commission an oversized replica from Howard Karascyk of King "
            "Solomon's Mine, Bellevue Square. Runners on good terms with Maria (or Hernandez) can get the "
            "store's name from her and reach it before the robbery. Any rocker recognizes the piece."
        ),
    },
    "Johnny Disk": {
        "notes_append": (
            "Dragon Hunt: 'that interview with Johnny Disk a year or so ago' is where a caged dragon saw "
            "Maria Mercurial's earring on a trideo and wanted one; the replica is the clue that starts the "
            "whole investigation. Media contacts (Target 4) can place it."
        ),
    },
    "Armando Hernandez": {
        "notes_append": (
            "Dragon Hunt: knows which Bellevue jeweler made Maria's famous earring -- King Solomon's Mine "
            "in Bellevue Square -- and will say so to runners he is on reasonable terms with, putting them "
            "in the shop before EF's toughs rob it."
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
**1. The Cobalt Marie system** (map p.39). Address from a decker's contacts: Etiquette (8), then
Negotiation (7); the data costs 2,000 nuyen minus 500 per success. Heavy Red security throughout; the
only Green nodes are the entertainment subsystem. Worth building as the run's showpiece host -- it is
the way to control the cameras before a physical entry. Note the physical map posts eight cameras but
only seven camera slave nodes are listed.

| Node | Function | Rating / IC |
|---|---|---|
| SAN-1 | Connects the Marie to the Matrix | Red-6, Barrier 5 |
| SPU-1 | Security main processing unit | Red-5, Barrier 5, Trace and Burn 5 |
| DS-1 | Security subprograms | Orange-7, Access 7 |
| SM-1 | Corridor sensors and the blinding lasers | Red-5 |
| SM-2 | Security cameras (control) | Red-5 |
| I/OP-1 | Security data terminal (Security Control, room 14) | Orange-7, Access 7 |
| CPU | Main processor (Computer Room 17; combat damage crashes the system and alerts Security) | Red-6, Barrier 6, Trace and Burn 6 |
| DS-2 | Processor subprograms | Red-6, Barrier 6, Blaster 6 |
| DS-3 | Processor backup programs | Red-6, Barrier 6 |
| I/OP-2 | Data terminal in the main office (room 19) | Red-6, Access 5 |
| DS-4 | Surveillance records -- the same Coinspinner/Ares recordings as the room 20 disks; 2 Mp | Red-7, Scramble 7 |
| DS-5 | Backup records (same content, 2 Mp) | Red-7, Scramble 7 |
| SPU-2 | Entertainment systems subprocessor | Green-4, Access 4 |
| DS-6 | Entertainment subprograms | Green-4, Access 4 |
| SM-3 | Holostage | Green-4, Access 4 |
| I/OP-3 | Data terminal behind the holostage | Green-4 |
| I/OP-4 | Data terminal behind the bar | Green-4 |
| SPU-3 | Monitoring / surveillance subprocessor | Red-6, Barrier 6 |
| SM-4 to SM-10 | Cameras 1-7 | Red-7 each |
| DS-7 | Monitoring systems subprograms | Red-6, Barrier 6, Trace and Burn 7 |

A Matrix alarm counts as a general alert: the Marie hands Ares the Coinspinner trideo and Knight
Errant reaches the Redmond Arms first.

**2. Emerging Futures mainframe** -- unmapped. Its Matrix address is easy to get, but EF takes the
system off the network and shuts it down every night against Ares deckers; by day it holds only
general corporate data (HR, PR and support terminals; Mainframe Computer Room 11 on the first floor,
five minutes to boot and load). Nothing on Cerberus. The elevator weapons-detector controls are on
manual until the mainframe runs. Improvise a small Orange system if a decker insists.

**3. Emerging Futures backup simulation computer** (Computer Room 39, fourth floor) -- standalone,
deck in directly or use its monitor terminal: Computer (4) for one hour minus ten minutes per extra
success (terminal: Computer (2), three hours). Log listings show every CERBERUS file erased one week
ago under user GRIER-DOP. A Fairlight Excalibur sits in the Computer Services Director's cabinet.

**4. Seattle General Hospital system** -- unmapped. Address is easy, but during Knight Errant's tenure
the hospital's System Access Node is disconnected from the Matrix and the system is isolated. Physical
nodes: mainframe room 5 on the ground floor (Rating 8 maglock) and a computer subprocessor room 7 on
every upper floor (Rating 8 maglock); service-area cameras feed Security Control. Build only as a
small isolated host for a rooftop or service-entrance approach.

**5. King Solomon's Mine** -- no host; wrist-telecomm and maglock PANICBUTTON links to Lone Star only.
"""

NOT_BUILT = """
- **The Shaikujin** (EF's unnamed thinning-haired middle manager in the prologue) and the **EF
  technician** the Dragon dragged to the deck -- on the EF row. **"Bob"** the Research Director, the
  **Security Chief**, the **HR / PR / Computer Services directors**, the **animal keeper** who sold
  Grier's ring, **DeHavillier's secretary** (the Ares informant), the **four runner teams** that
  poached the paranaturals, and the **corporate-takeover agency** -- leadership entries or notes only.
- **The griffin, basilisk and two nagas** of Project Cerberus, and the **German Shepherds, Dobermans,
  cheetah and Bengal tiger** of Handout 2 -- on the EF row and the timeline.
- **The three street toughs and their driver**, **their fixer** (dead by Blackwing) -- King Solomon's
  Mine row. **EF's Ork and Human lobby guards, 25 guards, two mages, rigger and drones** -- EF row.
- **The other three Maries, the thirteen Troll guards, the security mage, technicians and bartender**
  of the Cobalt Marie -- location and org rows. **The two Ares sararimen and their two samurai** --
  Ares row. **The Real Foodstuff delivery truck** -- location row.
- **The short bald Knight Errant investigator**, the **safehouse guards and interrogators**, the
  **Urban Reaction team**, the **terrified doctor and two Ares officials** in Room 25 -- KE / Ares /
  hospital rows. **David Childers' downtown apartment** (nothing of value).
- **Ares' Seattle central complex and gatehouse** -- not mapped; suicide to enter.
- **Cyberware Selections(TM)** and **Cryotech Sciences(TM)** (offices in Seattle General) -- hospital
  row. **Banque Orbitale de Suisse** is an org row, not a location.
- **Lofwyr** (the Great Dragon Ares fears will find out) -- name-drop. **The Sinsearach mountains**
  where Eliohann roamed -- on his row.
- News-handout names: **Ken Hlavic, Walter Smith, T. Gallagher** (compilers), **M. Perneta, M. Lee,
  Sirpriz, M. Stackpole** (bylines), **Marcus Brannigan** (osteopath, the Fortified Twist), the
  **Montreal Public Health Ministry** and the rogue VITAS strain, **Watermark Security**, **the Panzer
  Pull** and **the Battle of the Super Bruisers**, **tropical storm Laura**.
- Mercurial / Bottled Demon tie-ins already in the DB: Maria Mercurial, Armando Hernandez, Johnny Disk,
  Geyswain, the idol (updated, not re-created).
"""

PLAY_NOTES = """
- A straightforward mystery with corporate war for weather: backtrack the Dragon's trail (earring ->
  jeweler -> Grier -> EF's fifth floor -> Coinspinner -> the Marie -> the Redmond Arms -> Everett ->
  the hospital) while two corps that 'seem to be everywhere and know everything' lean on the team.
  Play the Ares men amused by intimidation; play the Persuaders as unnerving ghosts.
- Weapons discipline matters everywhere: Security Rating A in the hospital lobby, a Rating 6 detector
  and RAC bracelets in EF's elevator, light pistols only at the Marie, nothing at all in Seattle General
  under Knight Errant. Walking Downtown 'with enough weapons to invade a small nation' is bad for reps.
- The Marie is the hinge: slip in and out clean (copy the disks) and they beat Ares to Coinspinner;
  any alarm, Matrix or physical, or stolen disks, and it is the Everett safehouse instead. Give a
  contact the Redmond Arms address at the last minute if legwork stalls.
- Pay: 2,000 nuyen per person per day promised by the fixer; the earring (50,000 on the street, 10,000
  fence base -- the book disagrees with itself); 'money is no object' from Coinspinner; 50,000 each
  from Ares at the end. The Persuaders were paid 10,000 each plus medical.
- Lone Star can crash any firefight; the Knight Errant team surrenders, flashes a card and walks.
- Debug levers: Grier's dropped file case (Handouts 2 and 3) if the runners kidnap her; Childers and
  his Uzi; Coinspinner casting at the guards' backs; a senior KE guard who recognizes Coinspinner and
  stands aside; kill off Blackwing's team in a machine-gun burst if the finale is going badly.
- Karma (p.52; numbers lost to OCR): Survival; Success -- figuring out the Dragon was both test
  subject and Chairman of EF; slipping in and out of the Cobalt Marie without raising an alarm;
  successfully 'rescuing' the Dragon; Threat. Individual Karma at GM discretion.
- Loose ends: the Marie's owners want the runners silenced; Knight Errant remembers 20-30 dead
  comrades; Blackwing survives to hate them and Dragons; Eliohann is sequestered far from Seattle,
  but 'you know what they say about making deals with Dragons'; DeHavillier; a parabiologist newly
  hired at Ueber; a dead Global Tech VP; a missing slogan writer.
"""
