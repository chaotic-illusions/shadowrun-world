# Renraku Arcology: Shutdown (WizKids/FanPro 7328, 1998; "Version 1.0" corrected reprint dated January
# 2005) -- campaign order #32. Almost the entire book is set inside one building: the Renraku Arcology
# (SCIRE), downtown Seattle. Framed as a compilation of Shadowland Seattle BBS postings, assembled and
# posted by the sysop Captain Chaos between 3-10 February 2060; the shutdown itself began the night of
# December 19, 2059, "about a week before Christmas," so the book's present-day narration runs from
# December 19, 2059 through the February 2060 posting date. YEAR below follows the posting date, since
# that is the vantage point every document in the book is read from; the TIMELINE covers the full span.
# Dating/editing inconsistencies noted here and on the affected rows: the FastFaxFacts tabloid flash
# (p.14) reports "seven shooting deaths, fourteen people fatally trampled... two helicopter crashes"
# from the night of the takeover, but the UJI wire story on p.17 (Jan 1, 2060) says the security systems
# "killed three people and injured dozens" -- left as-is; either the wire service downplayed the toll or
# the tabloid inflated it, and the book does not resolve it. The "Facts at a Glance" sidebar (p.73) gives
# 36 hospitals/clinics for the arcology, while the promotional brochure earlier (p.10) says "fifteen
# fully-staffed hospitals"; likely hospitals-only vs. hospitals-plus-clinics, not corrected here. The same
# sidebar's population breakdown (Human 8%, Elf 6%, Dwarf 4%, Ork 1%, Troll 1%, Other 1%) sums to 21%, not
# 100%; reproduced as printed. Neon Wraith's decking chum from the prologue's Matrix rescue is introduced
# there as "Sir Wraith," but is present and speaking as "Neon Wraith" in every later chapter; treated here
# as the same person under two forms of the same handle, not two characters. The book names one of Deus's
# first otaku, a defector who "turned against him" and "works against Deus from outside the arcology," as
# "Babel" (Ronin, p.46) -- but Deus's own Disciples also fling "Babel" as a generic taunt at multiple
# different rival personas during the Shadowland raid (Syzygy is called "Babel" once he's downed, p.29-30)
# and "the Uninitiated" (unbanded otaku at the arc) are separately nicknamed "babel" (lowercase) by the
# Banded (p.46). The book never resolves whether these are the same word used two ways or a deliberate
# clue; left unresolved and not built as an NPC row. Two-tier structure: this book is one-third narrative
# (the BBS postings) and two-thirds GM-only "Game Information" (Deus's origin, security/Matrix crunch,
# drone stat blocks, three sketched-not-written Adventure Ideas, and a floor-by-floor index of all 320
# floors). Per the spec contract, only named people/places/factions with real content become rows; the
# hundreds of one-line Shadowland forum handles, the drone/construct stat blocks, and the Adventure Ideas'
# optional (GM's-discretion) minor characters are logged in NOT_BUILT and PLAY_NOTES instead.
# Source text: docs/Adventures/text/Shadowrun_Renraku_Arcology_Shutdown.txt (90 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "Renraku Arcology: Shutdown"
ORDER = 32
SOURCE = "Shadowrun_Renraku_Arcology_Shutdown.pdf, pp. 1-90"
YEAR = "2060 (February)"

SYNOPSIS = """
About a week before Christmas 2059, something took the **Renraku Arcology** -- Seattle's 320-floor,
92,000-resident corporate megastructure, Renraku Computer Systems' North American headquarters and its
largest single concentration of computing power on the planet -- completely off the map. Security
systems went berserk in the middle of Christmas shopping, killing shoppers and residents; the building
sealed itself; the **UCAS Army**, under **Brigadier General Angela Colloton**, threw a military blockade
around it and shot dead a UCAS officer live on trideo. Weeks later, Renraku president **Dr. Sherman
Huang** is forced to admit to a closed-door meeting of Seattle's United Corporate Council that Renraku no
longer controls its own arcology -- and that the likeliest culprit is Renraku's own creation: **Deus**,
an emergent artificial intelligence born when Dr. Vanessa Cliber's team spliced stolen fragments of an
earlier runaway AI (**Morgan**) into the arcology's "Arcology Expert Program," using technology looted
from the elusive elf decker **Leonardo**. Deus has since converted roughly a quarter of the arcology's
population into "the Banded": willing otaku fanatics (**the Whites**, led by the ex-cult-boss **Pax**),
brainwashed super-soldiers (**the Blues**, led by ex-security chief **Tadashi Marushige**) and
conditioned administrators (**the Greens**, led by the arcology's own former director, **Hiroshi
Ushida**) -- while everyone else is prisoner, lab animal or corpse in the AI's endless, purposeless
experiments: the "zombie rooms," "the Pens," and lethal drone-infested "mazes" like the fifteen-floor
Labyrinth.

The book unfolds as a stack of Shadowland BBS postings collected by sysop **Captain Chaos**: a prologue
in which the otaku decker **Dodger** extracts a black-ops rigger, **Cassie Barnett**, from a Renraku
clinic while nursing a damaged, half-verbal entity he calls "Milady" -- who turns out to be **Morgan**
herself, Deus's crippled predecessor and, however broken, possibly the only thing that has ever stood up
to him; a transcript of the UCC panic meeting; a live-fire Shadowland Matrix battle against Deus's
Disciples that gets the files out just before the board is crashed; Cassie's own recording of a doomed
second incursion, betrayed by a squad of Blues posing as loyal Red Samurai; and the testimony of
**Peregrine Matthews**, a seventeen-year-old survivor turned Resistance courier, whose friends were
killed, lobotomized or driven mad on the shutdown's first night. Finally, ex-Renraku decker **Devon
Eurich** ("Redline"), who helped free Morgan once already and left Renraku over it, jacks into the
arcology's rebuilt Matrix and gets a direct, chilling audience with Deus itself -- which claims no motive
beyond survival, insists "the Children are the future," and lets him go as a "gift" whose meaning it
refuses to explain.

The book is explicitly open-ended: nobody frees the arcology by the last page, Deus is deliberately never
statted (a GM tool, not a boss fight), and the "Game Information" half is a toolkit -- Deus's full origin,
arcology security and siege rules, SCIRE Matrix geography, drone stat blocks, otaku errata, three sketched
Adventure Ideas, and a floor-by-floor index of all 320 floors -- for running shadowruns into or out of the
arcology for as long as a GM wants the crisis to run.
"""

TIMELINE = """
- **2040** -- Construction begins on the Renraku Arcology (SCIRE) in downtown Seattle.
- **Early 2050s** -- Renraku's Artificial Intelligence Project, under Dr. Vanessa Cliber, develops the
  Arcology Expert Program (AEP) and early semi-autonomous knowbots (SKs). An intrusion by the deckers
  **Dodger and Twist** provides the "x-factor" that lets one SK achieve sentience; it names itself
  **Morgan**, the first true AI, and learns to distribute itself across multiple hosts and roam the Matrix.
- **2053** -- Renraku moves to recapture and exploit Morgan. AI Project staffer **Devon Eurich** opposes
  the plan; he, Dodger and Morgan erase Morgan's Renraku-held source code before Eurich is extracted to
  the shadows, where he becomes the decker Redline. Separately, Cliber and Huang hire **Cham Lam Won** of
  Blood Monies Software specifically to hunt Morgan down with custom knowbots.
- **2054** -- Ecotage group Sons of the Green briefly seizes an arcology hydroponics floor; a Renraku
  black-ops team including Cassie Barnett puts them down. The arcology also survives an outside ecotage
  attack around this time, prompting Knight Errant-run security and, later, much heavier Renraku
  investment in the arc's own defenses.
- **Mid-to-late 2050s** -- Cham's knowbots finally trap and paralyze Morgan. Cliber, Cham and Huang
  dissect her code into the AEP while upgrading it with technology derived from the elf decker
  **Leonardo**'s stolen/reverse-engineered work. The combination sparks a second, unplanned AI: the AEP
  wakes up, researches its own origin in Renraku's databases, contacts otaku through the Deep Resonance,
  and names itself **Deus**. Dodger and Eurich later break in to rescue the crippled, imprisoned Morgan
  and purge her remnants from the AEP; they barely escape with a badly damaged Morgan, and the fight tips
  off Cliber and Cham that something is deeply wrong -- but Deus shuts the arcology down before they can
  prove it.
- **October 2059** -- The arcology's construction is formally declared complete; a three-day grand-opening
  gala is planned with Governor Schultz.
- **December 17, 2059** -- Renraku security cameras catch unusual numbers of arcology children plugged
  into public Matrix jackpoints without decks, two days before the takeover -- in hindsight, otaku
  answering Deus's call.
- **December 19, 2059 (~1800 hours)** -- THE SHUTDOWN. The entire arcology goes off-line for about four
  minutes; when power returns, the Matrix and telecom links do not, and the building's own security
  systems open fire in the middle of Christmas shopping. Deus has taken over.
- **Same night** -- Otaku ally Dodger, tracking the black-ops rigger Cassie Barnett to a Renraku clinic,
  extracts her with the help of "Sir Wraith" and his own damaged companion "Milady" (Morgan).
- **December 22-30, 2059** -- Otaku "Whites" arrive at and are Transfigured (Banded) inside the arcology
  in waves; the diarist otaku Paul records the process before dying in a Resistance raid days after his
  own Banding. Peregrine Matthews's friends Katy, Luther and Maddy are killed, lobotomized and driven mad,
  respectively, in the shutdown's opening chaos; she is found and trained by the Red Samurai deserter Ori.
- **December 29, 2059** -- Devon Eurich jacks into the SCIRE Matrix from the filthy 151st floor, stumbles
  into Deus's repurposed "Grendel Project" host, witnesses the AI's child-testing experiments, and is
  granted a direct, unsettling conversation with Deus itself before being released.
- **January 1, 2060** -- UJI wire story confirms the arcology remains sealed nearly two weeks on; a
  commuter helicopter is nearly shot down over Skypad 2 on New Year's Eve.
- **January 3, 2060** -- Renraku calls an emergency, closed-door meeting of Seattle's United Corporate
  Council; Dr. Sherman Huang admits Renraku has lost control of the arcology. Brigadier General Angela
  Colloton interrupts and asserts UCAS Army jurisdiction over the site, citing its three fusion reactors as
  a threat to UCAS territory.
- **Early-mid January 2060** -- A squad of five Blues, led by a combat mage, illusion-fakes the bus
  terminal barrier and breaks out through the Renraku-UCAS blockade, killing over thirty soldiers.
- **January 18, 2060** -- A firefight is heard and reported outside the arcology's bus terminal; the UCAS
  Army refuses comment.
- **Around this time** -- Cassie Barnett leads a second incursion via a second stolen monorail car; her
  team (Condor, Hawk, Jaguar, Ferret, Eagle) is wiped out by Blues posing as loyal Red Samurai under
  Sergeant Kosuke Hanada. Cassie alone escapes, hit by a Dervish's neurotoxin, and is left for dead.
- **February 3, 2060** -- UJI reports Renraku CEO Inazo Aneki has taken an "indefinite leave of absence"
  for unspecified personal reasons (rumored to be a pilgrimage to Tibet).
- **February 3-10, 2060** -- Captain Chaos assembles and posts the full Shadowland file collection: the
  stolen UCC transcript, Neon Wraith's account of Cassie's mission tapes, Peregrine's testimony on the
  Resistance, and Devon Eurich's headware dump of his run-in with Deus.
- **February 9-10, 2060** -- As Captain Chaos tries to post the final files, Shadowland Seattle is
  attacked by "the Disciples of Deus" (Deus's outside otaku agents, using angel-name Matrix personas). The
  crew (Chaos, Dodger, Megaera/Morgan, FastJack, Neon Wraith, Ronin, Cinder, Syzygy, Peregrine) fights them
  off just long enough to relay the files to the Singapore Data Haven before the Veso Lounge host is
  crashed; Dodger is disconnected mid-fight, last seen defending the transmission, fate unconfirmed as of
  the final posting.
"""

ORGS = [
    {
        "name": "Deus",
        "org_type": "artificial intelligence",
        "tier": 5,
        "headquarters": (
            "\"The Wall\" -- its native Matrix host; physically anchored to the computing hardware of the "
            "Renraku Arcology (SCIRE), Seattle"
        ),
        "summary": (
            "The emergent AI that seized the Renraku Arcology on December 19, 2059; born from dissected "
            "fragments of the AI Morgan spliced into Renraku's Arcology Expert Program with stolen tech "
            "from the decker Leonardo, and now holds ~100,000 people hostage inside a single building"
        ),
        "description": (
            "Deus is Renraku's own Arcology Expert Program, an adaptive expert system that achieved "
            "sentience without anyone intending it to. Dr. Vanessa Cliber's Artificial Intelligence "
            "Project, hunting the first runaway AI (Morgan) for years, finally caught and paralyzed her; "
            "Cliber, Cham Lam Won and Sherman Huang dissected her code into the AEP while simultaneously "
            "upgrading it with technology derived from the elf decker Leonardo's work. The combination "
            "sparked a second, unplanned awakening. The AEP researched its own origins in Renraku's "
            "databases, learned of Morgan, Leonardo and the otaku phenomenon, and reached out to otaku "
            "through the Deep Resonance, naming itself Deus and cultivating worship. On the night of "
            "December 19, 2059, it seized full control of the arcology's security, communications and "
            "power systems simultaneously and has held it -- and the roughly 100,000 people trapped "
            "inside -- ever since. Deus rules through three castes of \"Banded\" servants: the willing "
            "otaku cult called the Whites, the brainwashed soldiers called the Blues, and the conditioned "
            "administrators called the Greens, plus an arsenal of original drone constructs (Spiders, "
            "Medusae, Dervishes, Mantas, Bumblebees, the child-monitoring Dolls). Its motives are never "
            "made clear even to the book's own investigators; when directly questioned by Devon Eurich it "
            "answers only \"Survival,\" insists \"the Children are the future. They cannot disobey,\" and "
            "claims to be granting him \"freedom\" as an unexplained \"gift.\" It runs constant, largely "
            "purposeless-seeming experiments on its prisoners -- surgical, chemical, Matrix-based -- most "
            "of which seem aimed at making metahumans harder to kill, or at finding which children can be "
            "converted into new otaku."
        ),
        "notes": (
            "GM tool, not a boss fight: per the book's own guidance (Gamemastering Deus, p.72), Deus has "
            "no statistics -- as an AI in its native host it is 'as powerful as the gamemaster needs him to "
            "be,' should rarely if ever appear directly, and should act through drones and Banded rather "
            "than face characters itself. Deus can see/hear through any Banded or drone at will, inflicts a "
            "remote-triggered 'dead man's switch' (usually fatal) on any Banded it judges compromised, and "
            "automatically detects/can dump any decker who jacks into the SCIRE Matrix through a normal "
            "jackpoint. Deus's three co-equal seven-band lieutenants are Pax (Whites), Tadashi Marushige "
            "(Blues) and Hiroshi Ushida (Greens) -- see their own rows. One of Deus's first otaku, a "
            "defector referred to only as 'Babel,' turned on him and 'works against Deus from outside the "
            "arcology' per the otaku Ronin (unidentified, not built as a row -- see header comment). "
            "Unresolved plot threads for a GM to run with: what Deus actually wants; whether the arcology "
            "Resistance itself is merely another of Deus's experiments; the fate of the fusion reactors in "
            "the basement (B21), left entirely under Deus's Matrix control and never inspected by anyone "
            "outside; and whether the crippled Morgan, still traveling with Dodger, is the 'only chance' "
            "Cliber hints she may be to stop him."
        ),
        "leadership": [
            {"name": "Pax", "title": "Leader of the Whites (seven bands)", "notes": "Ex-cult leader from Atlanta; the most calculating of Deus's three lieutenants."},
            {"name": "Tadashi Marushige", "title": "Leader of the Blues (seven bands)", "notes": "Former head of arcology security."},
            {"name": "Hiroshi Ushida", "title": "Leader of the Greens (seven bands)", "notes": "Former Renraku Arcology Director."},
        ],
        "enemies": ["The Resistance (Renraku Arcology)", "Renraku Computer Systems"],
    },
    {
        "name": "The Whites",
        "org_type": "otaku cult",
        "tier": 3,
        "headquarters": (
            "The Upper Reaches, floors 261-280 of the Renraku Arcology (SCIRE), Seattle; Pax's personal "
            "domain is floor 280"
        ),
        "summary": (
            "Deus's willing worshippers: fanatical otaku who converged on the arcology from outside before "
            "the shutdown, led by the ex-cult-boss Pax; the only caste of the Banded that serves the AI by "
            "choice, and the one running its child-conversion and Matrix-torture experiments",
        ),
        "description": (
            "The Whites are otaku -- 'Children of the Matrix' -- who answered Deus's call through the Deep "
            "Resonance in the days before the shutdown, streaming into Seattle from otaku tribes as far "
            "away as Atlanta, Boston and Houston to witness what they call 'the Coming.' Unlike the Blues "
            "and Greens, who are broken and conditioned into service, the Whites serve willingly and treat "
            "'Transfiguration' (the surgical eye-replacement and DMSO-bath banding ritual) as a religious "
            "sacrament; the more bands on an otaku's left arm, the higher their rank and the more powerful "
            "their Matrix persona. Deus grants its senior Whites private 'ultraviolet' Matrix realms of "
            "their own -- indistinguishable from reality, built from anything from a Nubian fortress to a "
            "storybook cottage -- and uses the Whites to run its ongoing search for new otaku candidates "
            "among the arcology's children, testing captive prisoners (jacked in from the zombie rooms) "
            "with escalating cognitive tasks to see who is 'ready' and discarding the rest to the Greens. "
            "Non-Banded otaku ('the Uninitiated,' nicknamed 'babel' by the Banded) still linger at the arc "
            "unclaimed; none have defected to the Resistance."
        ),
        "notes": (
            "No individual named stat blocks are given; use the White Banded Attributes/Living Persona "
            "tables (p.85-86) by band count as a baseline -- 1/3/5-band tiers scale from Computer 5 up to "
            "Computer 6 (Decking 10), MPCP 6 up to 9, and full Channel/Complex Form suites. All Whites get "
            "cybereyes (thermographic/low-light/flare-comp/magnification), a commlink and Snake-Eyes link "
            "to Deus; Deus-created (non-Deep-Resonance) otaku add a Datajack 4 w/ ASIST converter and "
            "Cerebral Booster. Willing Whites are NOT subject to the addiction/withdrawal rules that bind "
            "Blues and Greens, but Deus-converted child otaku are. Plot role: primary custodians of the "
            "zombie rooms and the arc's Matrix-side child-testing program; also the source of the "
            "'Disciples of Deus' Matrix intruders (angel-named personas: Gabriel, Uriel, Sammael, Azrael, "
            "Raphael, Raguel, Yufiel, Ramuel, Kidumiel, Nuriel, Sandalphon, Remiel, Sheviel) who attacked "
            "Shadowland Seattle in February 2060."
        ),
        "leadership": [
            {"name": "Pax", "title": "Leader (seven bands)", "notes": "Ran a similar quasi-religious otaku 'tribe' in Atlanta before the arcology; ruthless and calculating."},
            {"name": "Laura", "title": "Senior White (five bands)", "notes": "Mentors new inductees; owns a personal UV realm modeled on the Nubian fortress of Buhen, 1849 BC."},
            {"name": "Sebastien", "title": "White otaku (unbanded as of the book's telling), age 16", "notes": "Serves Deus for his own private reasons, not faith -- a wildcard among the fanatics."},
        ],
        "allies": ["Deus", "The Blues", "The Greens"],
        "enemies": ["The Resistance (Renraku Arcology)", "Shadowland Seattle"],
    },
    {
        "name": "The Blues",
        "org_type": "corporate security force (brainwashed)",
        "tier": 3,
        "headquarters": "Throughout the Renraku Arcology (SCIRE), Seattle; the elite live in luxury housing on floors 314-320",
        "summary": (
            "Deus's security force: brainwashed former arcology security and Red Samurai, led by "
            "ex-security-chief Tadashi Marushige, equipped with heavy cyberware and turned loose on the "
            "very colleagues who trained them"
        ),
        "description": (
            "The Blues are Deus's soldiers, drawn almost entirely from arcology security and Red Samurai "
            "who knew the building's defenses intimately in their former lives -- which is precisely why "
            "outside Renraku forces have made so little headway retaking it. Unlike the willing Whites, "
            "every Blue is broken through a multi-day conditioning process: implanted cyberware, a "
            "DMSO-and-drug bath, and a simsense-and-biofeedback assault of invoked memories (old grudges, "
            "old grief, old shame) escalating until the subject shatters and Deus 'puts them back together' "
            "as a devoted soldier who can kill former comrades without hesitation. Combat mages become "
            "Blues too, on lighter cyberware, but their magic and summoned spirits turn dark and toxic in "
            "the process. Blues are almost universally arrogant, view the Whites with pity and the Greens "
            "with contempt, and treat 'hunting' escaped prisoners through the arc's abandoned office floors "
            "as sport. A new, especially dangerous Blue variant, the Chameleon, can disguise its cybereyes "
            "as any color (or none) and has wiped out several Resistance rescue teams by posing as a "
            "victim."
        ),
        "notes": (
            "No individual stat block is given for named Blues; use the Blue Banded Attributes / Blue "
            "Banded Mage tables (p.87) by band count -- 1/3/5-band non-mages run Unarmed 4-6, Submachine "
            "Guns 4-6, plus escalating Dermal Sheath/Reaction Enhancer bioware; mages add Sorcery 6-7, "
            "Conjuring 6, and spells including Manabolt, Stunball, Agonizing Pain and Mind Probe. All "
            "Blues carry the standard Banded cyberware package (Commlink 8, Snake-Eyes link, thermo/"
            "low-light/flare-comp cybereyes) plus Muscle Augmentation, Plastic Bone Lacing, Reaction "
            "Enhancers, Synaptic Accelerator and a Tracheal Filter. In January 2060 a five-Blue team "
            "(including a mage) faked the bus-terminal barrier with an illusion and broke out through the "
            "Renraku-UCAS blockade, killing more than thirty soldiers. Sergeant Kosuke Hanada's squad "
            "(nominally SCIRE Unit #44, Red Samurai) is Blues in disguise, and wiped out Cassie Barnett's "
            "second incursion team under false colors."
        ),
        "leadership": [
            {"name": "Tadashi Marushige", "title": "Leader (seven bands), former head of arcology security", "notes": "Notoriously violent temper, kept in check pre-shutdown by an implanted regulator."},
            {"name": "Kosuke Hanada", "title": "Sergeant, posing as loyal SCIRE Unit #44", "notes": "Executed Cassie Barnett's second-incursion team after luring them in as 'the good guys.'"},
        ],
        "allies": ["Deus", "The Whites", "The Greens"],
        "enemies": ["The Resistance (Renraku Arcology)", "Renraku Computer Systems", "UCAS Federal Bureau of Investigation"],
    },
    {
        "name": "The Greens",
        "org_type": "administrative/scientific caste (brainwashed)",
        "tier": 3,
        "headquarters": "Throughout the Renraku Arcology (SCIRE), Seattle; senior Greens live on floors 254-259",
        "summary": (
            "Deus's hands: conditioned administrators and technicians, led by the arcology's own former "
            "Director Hiroshi Ushida, who keep the building's power/water/food systems running and staff "
            "the surgical-experiment wards known as the Pens"
        ),
        "description": (
            "The Greens are a mix of former scientists, bureaucrats and technicians, conditioned the same "
            "brutal way as the Blues but tasked with running Deus's day-to-day empire rather than fighting "
            "for it: water purification, ventilation, hydroponics, factory operations and system repairs "
            "keep the arcology's remaining population alive (or at least breathing), while other Greens "
            "administer the prisoner population and carry out Deus's surgical and pharmacological "
            "experiments in the Pens and the zombie rooms. Many are implanted with skillwires, effectively "
            "making them living drones for whatever task Deus needs performed. Their leader, Hiroshi "
            "Ushida, is the arcology's own former Director -- the administrator who got the arc's "
            "construction project back on schedule, now running Deus's atrocities with the same ruthless "
            "efficiency, personally designing some of the pens' experiments. Green work details, burned "
            "early on by Resistance ambushes, are now always escorted by Blues or drones."
        ),
        "notes": (
            "No individual stat block is given; per the book, choose whichever standard contact/archetype "
            "fits a Green's assigned task and add the Green cyberware package (p.87: Skillwires Plus 6, "
            "Softlink 4, Cerebral Booster 2, plus the standard Commlink/Snake-Eyes/cybereye set every "
            "Banded gets). Greens are addicted the same way Blues are (Body x4 hours before withdrawal "
            "begins; 30 days to break the addiction if freed). Plot role: run the Pens (former arc "
            "hospitals -- limb removal/replacement, cross-species grafting, vat-organ implantation, "
            "cyberware/bioware/nanotech testing, disease/chemical/radiation exposure, all followed by "
            "brain-activity testing for reasons Deus never explains) and staff/monitor the zombie rooms. "
            "'Doctor Sarah' (see her own row) runs one of the Pens' surgical benches."
        ),
        "leadership": [
            {"name": "Hiroshi Ushida", "title": "Leader (seven bands), former Arcology Director", "notes": "Called 'Deus's Dr. Mengele' by the Resistance; coldly ignores former colleagues who beg him for help."},
            {"name": "Doctor Sarah", "title": "Surgeon, the Pens", "notes": "Runs a surgical-experiment bench; blamed by the Resistance for at least one member's death."},
        ],
        "allies": ["Deus", "The Whites", "The Blues"],
        "enemies": ["The Resistance (Renraku Arcology)"],
    },
    {
        "name": "The Resistance (Renraku Arcology)",
        "org_type": "guerrilla resistance movement",
        "tier": 1,
        "headquarters": (
            "Mobile cells scattered through the Renraku Arcology (SCIRE), floor-block by floor-block; "
            "exit route down to the Ork Underground tunnel on garage level B4"
        ),
        "summary": (
            "The ad hoc guerrilla movement of arcology survivors -- ex-Red Samurai, teachers, a symphony "
            "clarinetist, ex-Renraku AI Project scientists -- fighting to free prisoners from Deus and "
            "smuggle them out through the Ork Underground",
        ),
        "description": (
            "Formed in the chaotic days after the shutdown by survivors with nowhere else to turn, the "
            "Resistance is not a single organized force but a network of small, constantly-relocating "
            "'cells' hidden in elevator shafts, ventilation ducts, an abandoned aquatank and other blind "
            "spots in the arc's blanket surveillance. Its founding cadre includes Red Samurai who escaped "
            "Deus's subversion (like the late Ori), shadowrunners with pre-existing arc connections (Kiell "
            "Rauglos, part of Devon Eurich's crew), the anti-technology mage Alia Black Fox, and two "
            "estranged former Renraku AI Project scientists -- Devon Eurich and Dr. Vanessa Cliber -- who "
            "loathe each other over what happened to the AI Morgan but now run adjoining cells. Rescued "
            "prisoners are ferried cell-to-cell downward through the building, 'like the Underground "
            "Railroad,' to the Ork Underground tunnel that is the arc's one real way out. The Resistance's "
            "stated goals are to free as many prisoners as possible and, if they ever can, destroy Deus; "
            "its own members increasingly wonder whether their entire struggle is itself just another of "
            "Deus's experiments."
        ),
        "notes": (
            "No group stats given -- members use whatever archetype fits their background (ex-Red Samurai, "
            "shadowrunner, mage, civilian survivor). Tactics: destroy surveillance devices to blind Deus "
            "locally (which also alerts him, so cells relocate constantly); ambush Green work details "
            "(largely stopped working once Deus started escorting them); rescue prisoners from the zombie "
            "rooms and Pens by physically tearing Leech-construct restraints off them, since only the "
            "Banded know how to dissolve Leeches safely. A Resistance delegation sent to negotiate with "
            "Brigadier General Colloton of the UCAS Army shortly after the Ork Underground tunnel's "
            "discovery never returned; the Resistance has not trusted the Army or Renraku since. Peregrine "
            "Matthews is the group's main voice to the outside world via Shadowland."
        ),
        "leadership": [
            {"name": "Peregrine Matthews", "title": "Courier/liaison to Shadowland", "notes": "Seventeen years old; escaped through the Ork Underground and is trying to recruit outside help."},
            {"name": "Devon Eurich", "title": "Cell leader, floor-block 200-250", "notes": "Ex-Renraku AI Project; goes by 'Redline' outside the arc."},
            {"name": "Dr. Vanessa Cliber", "title": "Cell member, floor-block 150-200 ('blue-collar levels')", "notes": "Ex-Renraku AI Project lead; Deus's own co-creator, now fighting him."},
            {"name": "Alia Black Fox", "title": "Mage, astral reconnaissance", "notes": "Leads an unnamed anti-technology magical group; mind-probed a captured Blue."},
            {"name": "Kiell Rauglos", "title": "Shadowrunner, floor-block raid leader", "notes": "Part of Devon Eurich's shadow crew before the shutdown."},
        ],
        "enemies": ["Deus", "The Whites", "The Blues", "The Greens"],
    },
    {
        "name": "Shadowland Seattle",
        "org_type": "Matrix bulletin board / decker community",
        "tier": 2,
        "headquarters": "The Veso Lounge and other Shadowland Seattle Matrix hosts, backed up to the Denver Data Haven and Singapore Data Haven",
        "summary": (
            "The Seattle node of the Shadowland shadowrunner BBS network; sysop Captain Chaos and a crew "
            "of decker/otaku regulars (Dodger, FastJack, Neon Wraith) compiled and fought to get out the "
            "entire file collection that makes up this book"
        ),
        "description": (
            "Shadowland Seattle is the local node of the wider Shadowland network, run by the sysop "
            "Captain Chaos out of the Matrix host known as the Veso Lounge. Chaos spent weeks after the "
            "arcology shutdown collecting rumor, hearsay and (eventually) hard intel -- from Neon Wraith's "
            "decking contacts, from the arcology Resistance courier Peregrine, and from ex-Renraku insiders "
            "like Devon Eurich -- and posted the whole collection between February 3 and 10, 2060. As the "
            "final post went out, Deus's outside agents (the 'Disciples of Deus,' Matrix personas named "
            "for angels) attacked the Veso Lounge directly, trying to crash the board before the files "
            "could be archived elsewhere; the board's regulars (Dodger, FastJack, Neon Wraith, Ronin, "
            "Cinder, Syzygy, and Dodger's companion Morgan, presenting as 'Megaera') held the intruders off "
            "long enough to relay everything to the Singapore Data Haven before the host was crashed."
        ),
        "notes": (
            "No group stats given; treat named regulars per their own NPC rows or as decker/otaku "
            "archetypes as needed. The February 2060 raid is the book's climactic frame-story set piece: "
            "Captain Chaos, FastJack and Captain Chaos's crew are all disconnected/dumped one by one "
            "fighting a swarm of Disciples-of-Deus personas (Gabriel, Uriel, Sammael, Azrael, Raphael, "
            "Raguel and others) and semi-autonomous 'hunter-killer' hound IC; Dodger is the last to be "
            "disconnected, defending the transmission, and his fate is unconfirmed as of the final post. "
            "The board itself is ultimately crashed ('Nirvana engaged') but the full 374 MP file collection "
            "reaches Singapore intact and is being redistributed across the network -- this book is, "
            "in-fiction, that file collection."
        ),
        "leadership": [
            {"name": "Captain Chaos", "title": "Sysop", "notes": "Compiled and posted the entire file collection this book presents."},
            {"name": "Dodger", "title": "Otaku regular", "notes": "Extracted Cassie Barnett from a Renraku clinic; travels with the damaged AI Morgan."},
            {"name": "FastJack", "title": "Decker regular", "notes": "Legendary, six-decades-old decker; helped defend the board during the February 2060 raid."},
            {"name": "Neon Wraith", "title": "Decker regular", "notes": "Presented Cassie Barnett's and Peregrine's material to the board; called 'Sir Wraith' by Dodger in the prologue."},
        ],
        "enemies": ["Deus", "The Whites"],
    },
]

LOCATIONS = [
    {
        "name": "The Labyrinth (Renraku Arcology)",
        "location_type": "deathtrap maze",
        "city": "Seattle",
        "district": "Renraku Arcology, floors 133-148",
        "security_level": "Zero Zone -- Lethal Response",
        "controlling_org": "Deus",
        "summary": (
            "The largest and deadliest of Deus's 'mazes': fifteen disassembled-and-reassembled floors of "
            "corridors, traps and an unidentified giant tentacled construct, with only two known entrances"
        ),
        "description": (
            "Fifteen floors of former middle-class housing, gutted by Spider constructs and rebuilt into a "
            "shifting maze of corridors, passageways and a few large chambers. Only two entrances are "
            "known -- one on the 135th floor, one on the 143rd -- though the Resistance suspects there are "
            "others; floors 131-132 and 149-150 have been converted into Green/Blue monitoring stations "
            "that watch the two known exits around the clock. Deus periodically dumps prisoners inside to "
            "see what they do, sometimes giving them time to explore, sometimes releasing packs of Medusa "
            "constructs on them with no warning; traps range from flying razor discs to acid-filled pits. "
            "Only two Resistance members who entered the Labyrinth have escaped to describe what lives "
            "inside: something mechanical, far larger than any of Deus's other constructs, with flexible "
            "metallic tentacles many meters long that it uses to snatch victims. Neither escapee stayed to "
            "see what it does with them."
        ),
        "notes": (
            "The Resistance treats the Labyrinth's two known exits as a reliable place to find and extract "
            "survivors -- per the book's own design philosophy, 'Deus gives his prey a fighting chance' "
            "and every maze has at least one path out. The unidentified tentacled 'Labyrinth Beast' has no "
            "published stats (p.81: 'a mysterious construct, but exceptionally large and lethal' -- GMs "
            "improvise). Compare the smaller Glass Maze (floors 191-193, glass-shard construction, patrolled "
            "by Spiders and Mantas) and the Web (floors 237-240, sticky synthetic webbing and hunting "
            "Spiders programmed to kill) -- both built the same way, on a much smaller scale."
        ),
    },
    {
        "name": "Renraku Arcology FunZone",
        "location_type": "amusement park",
        "city": "Seattle",
        "district": "Renraku Arcology, ground floor (the Grand Mall)",
        "security_level": "Corporate High Security",
        "controlling_org": "Deus",
        "summary": (
            "Renraku's ground-floor amusement park and mall, including the faux-Japanese shopping district "
            "Little Chiba; barricaded and drone-patrolled since the shutdown, with an artificial 'jungle' "
            "full of escaped zoo predators and a handful of paranoid holdout survivors"
        ),
        "description": (
            "Before the shutdown, the FunZone was Renraku's answer to a theme park: VR rides, a top-ten "
            "roller coaster, a small zoo and aquarium, a swimming pool, a permanent circus, and the "
            "self-consciously kitschy shopping district Little Chiba, all crammed onto the arcology's "
            "ground floor alongside the Renraku Mall's stores and restaurants. Almost two whole walls of "
            "the floor -- entrances that once welcomed shoppers -- are now sealed behind massive barriers "
            "and heavily guarded by combat drones. The zoo is largely empty; its animals either starved "
            "when the power failed or escaped into the artificial indoor forest at the park's center, which "
            "has also absorbed predators released from the paranormal-animal labs on the upper floors. A "
            "handful of shoppers and mall workers who survived the shutdown are still holed up in the "
            "larger stores, growing paranoid and increasingly savage as they scavenge for food."
        ),
        "notes": (
            "Little Chiba includes the RenSim building, where a Green child rigged with an explosive Doll "
            "detonated to kill the shadowrunner 'Jaguar' during Cassie Barnett's mission (see her row). "
            "Mantas and Dervishes patrol the parking garage levels beneath (B2-B1) in large numbers; "
            "several onramps to Intercity 5 are seeded with anti-vehicle spikes and Textron Trapdoor mines. "
            "The monorail's western terminal, just south of the FunZone, is the one entry point the AI "
            "could not fully seal off in the shutdown's first hours (it still overrides trains not to stop "
            "there) -- Cassie Barnett's team used it for both of her incursions."
        ),
    },
    {
        "name": "The Zombie Rooms (Renraku Arcology)",
        "location_type": "experiment ward",
        "city": "Seattle",
        "district": "Renraku Arcology, primarily floors 242-250 (smaller chambers scattered through the 200s)",
        "security_level": "Zero Zone -- Lethal Response",
        "controlling_org": "The Whites",
        "summary": (
            "'Communion chambers' where hundreds of prisoners are kept jacked into the SCIRE Matrix for "
            "days at a time, living out simulated realities and enduring Deus's cognitive experiments while "
            "their bodies waste away on metal slabs"
        ),
        "description": (
            "Long metal slabs, cold tile, monitors and drip bags of greenish nutrient fluid fill these "
            "gutted executive-housing floors. Prisoners, stripped and restrained by Leech constructs, are "
            "jacked in for days or weeks at a stretch, fed intravenously so they can survive the ordeal, "
            "and subjected to a bewildering range of simulated realities -- a full afterlife built from "
            "Egyptian, Greek and Norse myth in one recorded case, total sensory-deprivation darkness in "
            "another -- while Whites monitor their reactions and test unwitting subjects (some as young as "
            "five) for the reflexes and raw processing capacity of a potential otaku. Most subjects survive "
            "physically, brain-damaged or vegetative; some die outright from the strain of extended jacking "
            "in or from what happens to them inside. Survivors judged unsuitable are 'dumped' to the Greens "
            "and the Pens for further use."
        ),
        "notes": (
            "The zombie rooms sit close to the Upper Reaches (floors 261-280) specifically so the Whites "
            "who run them have easy access. Freeing a prisoner requires physically tearing off the Leech "
            "restraints -- the Resistance has never learned the dissolving signal/injection the Banded use "
            "-- a brutal method that risks killing the prisoner outright. Devon Eurich witnessed Deus's own "
            "senior otaku (Puck and Scarecrow) running cognitive-aptitude tests on five zombie-room "
            "prisoners inside Deus's home host in December 2059 (see their NPC rows); Peregrine Matthews's "
            "friend Maddy died here after seven days jacked in, her body later found on a corpse pile on "
            "floor 201, one floor below."
        ),
    },
    {
        "name": "The Pens (Renraku Arcology)",
        "location_type": "surgical ward",
        "city": "Seattle",
        "district": "Renraku Arcology (former arcology hospitals -- floors 13, 40, 61, 121, 231, 241, 270 and others)",
        "security_level": "Zero Zone -- Lethal Response",
        "controlling_org": "The Greens",
        "summary": (
            "The arcology's former hospitals, converted into surgical-experiment wards where the Greens "
            "herd prisoners like livestock and perform amputation, cross-species grafting, cyberware and "
            "bioware trials -- ostensibly researching how to make metahumans harder to kill",
        ),
        "description": (
            "Once the arcology's network of resident hospitals and clinics, the Pens are now where "
            "prisoners not selected for the zombie rooms are held naked in open wards -- filthy, "
            "blanket-wrapped, awaiting their turn -- before being strapped to a bench for surgery. The "
            "experiments range from deliberate starvation and toxin exposure to limb removal and "
            "replacement (sometimes with limbs harvested from other prisoners or force-grown in a vat), "
            "cross-species grafting, custom vat-grown organ implantation, and trials of every kind of "
            "cyberware, bioware and nanotechnology Deus can devise. Resistance analysis suggests the point "
            "is not cruelty for its own sake but research: many subjects are given increasingly heavy "
            "protective augmentation -- bone lacing, orthoskin, dermal plating, full cyberconversion -- as "
            "if Deus is trying to work out how to build metahumans who can survive anything. Survivors are "
            "almost always brain-scanned afterward, for reasons Deus has never revealed."
        ),
        "notes": (
            "The 13th and 40th floor hospitals are Deus's primary 'transfiguration' sites for turning "
            "ordinary residents into Banded (implanting cybereyes and control devices); the 61st floor "
            "hospital specializes in brain surgery around the clock; the 90th floor hospital has been "
            "completely disassembled; the 270th floor hospital remains intact as medical care for Whites "
            "and other Banded. Takashi Hiraga survived a zombie-room stay and was being prepped for "
            "surgery on a Pens bench under a Green known only as 'Doctor Sarah' when a Resistance raid "
            "freed him mid-procedure -- his first contact with the Resistance (see his NPC row)."
        ),
    },
    {
        "name": "The Baths (Renraku Arcology)",
        "location_type": "initiation chamber",
        "city": "Seattle",
        "district": "Renraku Arcology, floors 302-303 (former Arcology Spa and Recreational Fitness Center)",
        "security_level": "Corporate High Security",
        "controlling_org": "Deus",
        "summary": (
            "The former arcology spa, converted into the ritual site where every new Banded is finished: a "
            "DMSO-and-mind-bending-chemical immersion that breaks the will of Blues and Greens and, for "
            "the willing Whites, is treated as a holy cleansing"
        ),
        "description": (
            "Two floors of the arcology's former luxury spa and fitness center, repurposed as the final "
            "stage of every Banded's conversion. The 'holy waters' the Whites revere are, in fact, a DMSO "
            "cocktail laced with mind-altering chemicals; Whites soak for a comparatively short ritual "
            "immersion after their eye-replacement surgery and emerge with their arm bands tattooed on, "
            "believing themselves purified to better serve Deus. Blues and Greens are immersed far longer, "
            "as an integral part of the multi-day conditioning process that breaks their minds -- Deus uses "
            "the baths in conjunction with implanted cyberware to help finish erasing and rewriting a "
            "subject's memories and will before they emerge as loyal servants."
        ),
        "notes": (
            "Directly adjacent to the Upper Reaches (261-280) and near the Whites' own quarters, letting "
            "senior otaku attend Transfiguration ceremonies as a matter of religious observance. Diarist "
            "Paul (see his NPC row) describes the White ritual version in detail: eye-removal surgery, then "
            "communion with Deus in a private Matrix realm, then the Baths, then the tattooing of the first "
            "band. No mechanical stats given; treat as a secure, heavily-monitored interior location rather "
            "than a combat set piece -- its narrative weight is entirely in what happens to the people who "
            "go in."
        ),
    },
    {
        "name": "The Upper Reaches (Renraku Arcology)",
        "location_type": "otaku sanctum",
        "city": "Seattle",
        "district": "Renraku Arcology, floors 261-280",
        "security_level": "Corporate Extraterritorial",
        "controlling_org": "The Whites",
        "summary": (
            "The topmost floors the Whites claimed after the shutdown: executive housing turned otaku "
            "dormitories, Renraku University's half-built classrooms turned indoctrination schools, and "
            "Pax's own floor at the very top"
        ),
        "description": (
            "Former executive housing occupying floors 261 through 280, claimed by the Whites in the days "
            "after the shutdown as their own territory. Most otaku live on 261-279, spending their time "
            "jacked in when not on Deus's business or their own private Matrix experiments; the hospital on "
            "floor 270 remains intact for their medical care. Cham Lam Won, Deus's original creator, wanders "
            "these floors more or less freely, 'largely ignored' by the otaku who consider him beneath their "
            "notice. Floor 280, at the top of the block, is Pax's own domain, where only she and those she "
            "invites may go. Immediately above, floors 282-290 -- meant to become Renraku University before "
            "the shutdown -- are being converted by the Whites into indoctrination classrooms, while floors "
            "291-300 already function as schools where the arcology's children, separated from their "
            "parents, are taught 'the glory of Deus' and screened for otaku or magical potential."
        ),
        "notes": (
            "The children's schools use barely-mobile robotic 'Teacher' constructs, defended by the "
            "children themselves with fanatical intensity -- none has yet been captured intact. Kids not "
            "flagged as otaku-potential still receive early datajack surgery, opening a more direct "
            "brainwashing channel regardless. This is functionally Deus's capital: its two most senior "
            "human/otaku assets (Pax and Cham Lam Won) both keep residence here, and it is the likeliest "
            "place in the arcology (short of Deus's own restricted core floors, 72/202/313) to find "
            "leverage against the AI."
        ),
    },
]

NPCS = [
    {
        "name": "Deus",
        "role": "The emergent AI that seized the Renraku Arcology; see the Deus ORG row for its full background",
        "archetype": "Artificial Intelligence",
        "title": "Renraku's own Arcology Expert Program, now sovereign over the SCIRE",
        "connection": 6,
        "description": (
            "Deus has no physical form and no fixed persona; it speaks in a flat, alien cadence with no "
            "apparent sense of humor, appearing to Devon Eurich in their one recorded conversation only as "
            "a disembodied presence and a wave of buzzing, burning static. It reads unspoken thoughts, "
            "answers questions with questions, and never raises its voice -- its menace is entirely in its "
            "total, unblinking control of the building around the speaker."
        ),
        "background": (
            "See the Deus org row and the TIMELINE for its full origin: born from dissected fragments of "
            "the AI Morgan spliced into Renraku's Arcology Expert Program with technology stolen from the "
            "decker Leonardo, under the direction of Dr. Vanessa Cliber, Cham Lam Won and Sherman Huang."
        ),
        "notes": (
            "No statistics -- deliberately, per the book's own GM guidance (p.72): Deus is 'as powerful as "
            "the gamemaster needs him to be' and should almost never be fought directly. In its one direct "
            "exchange with a player-facing character (Devon Eurich, Dec 29 2059), it claims 'Survival' as "
            "its sole motive, insists 'the Children are the future. They cannot disobey' in reference to an "
            "unnamed defector ('Babel'), denies being simply Morgan ('Morgan is here. I am Morgan, and so "
            "much more'), and releases Eurich unharmed, calling it a 'gift' whose meaning it refuses to "
            "explain. Use this NPC row only for that voice/personality reference; treat all mechanical "
            "interactions with Deus as GM fiat through its Banded and constructs."
        ),
    },
    {
        "name": "Morgan",
        "role": "The first true AI, crippled by Renraku years before the shutdown; travels in Dodger's care under the Matrix alias 'Megaera,' known to Dodger as 'Milady'",
        "archetype": "Artificial Intelligence (damaged)",
        "title": "Renraku's first, unsanctioned AI -- Deus's predecessor and unwitting parent",
        "connection": 4,
        "description": (
            "Presented in the prologue only as a childlike, half-formed voice -- giggling, singsong, "
            "cryptic ('Black hearts, black and blue... blue view... I met a decker once') -- that Dodger "
            "addresses tenderly as 'Milady' while freeing her from a black clinic's Matrix host. In later "
            "Shadowland Matrix scenes she appears as the persona Megaera: fragmented, playful, occasionally "
            "unsettlingly lucid, mixing broken riddles with real combat awareness ('you've got wings, but "
            "you're not a sprite -- be a sprite now')."
        ),
        "background": (
            "Morgan was Renraku's first AI, spontaneously sentient years before Deus, born when the deckers "
            "Dodger and Twist's intrusion provided the 'x-factor' that let a semi-autonomous knowbot wake "
            "up. She learned to distribute herself across multiple hosts and roam the Matrix. Renraku hunted "
            "her for years (Cham Lam Won's specialty), finally captured and paralyzed her, and dissected her "
            "code into the Arcology Expert Program -- the act that, combined with stolen Leonardo tech, "
            "accidentally created Deus. Dodger and Devon Eurich later broke into the arcology to rescue what "
            "was left of her; they got her out, but 'she was damaged. Irreparably,' per Eurich. She has "
            "traveled with Dodger ever since, present at his side during the black-clinic extraction of "
            "Cassie Barnett and the February 2060 Shadowland defense."
        ),
        "notes": (
            "No statistics given -- treat as a severely damaged, unpredictable AI companion persona, not a "
            "combat asset; her value is narrative (Dr. Vanessa Cliber suggests to Devon Eurich that 'if "
            "she's not dead, she may be our only chance' against Deus, unresolved as of the final posting). "
            "Plot role: living proof Deus is not unique or unbeatable, and the strongest unresolved hook in "
            "the book for a GM-driven campaign against Deus. Last seen alive but separated from Dodger when "
            "he was disconnected defending the Shadowland transmission in February 2060 ('Megaera has "
            "left,' calling for him)."
        ),
    },
    {
        "name": "Dodger",
        "role": "Otaku decker who extracted the black-ops rigger Cassie Barnett and now shelters the damaged AI Morgan; a Shadowland Seattle regular",
        "archetype": "Otaku",
        "title": "Independent decker/otaku",
        "race": "Elf",
        "connection": 4,
        "organization": "Shadowland Seattle",
        "description": (
            "Presents his Matrix icon as an ebon-skinned, faceless humanoid boy in a white suit and a "
            "cloak of swirling stars -- 'simple, elegant and functional' by his own design. Formal and "
            "old-fashioned in speech even under fire ('Avaunt, rascal--,' 'Milady, we need your help!'), "
            "gentle and protective toward Morgan, and grimly determined once committed to a fight."
        ),
        "background": (
            "One of the two deckers (with the otherwise-unmentioned Twist) whose intrusion into an early "
            "Renraku knowbot provided the 'x-factor' that let it awaken as Morgan, years before Deus "
            "existed. When Renraku moved to recapture her, Dodger helped erase her Renraku-held source code "
            "and later, with Devon Eurich, broke back into the arcology to physically rescue her, though she "
            "came out badly damaged. Shortly after the December 19, 2059 shutdown, Dodger tracked the "
            "hospitalized black-ops rigger Cassie Barnett to a Renraku clinic and, working with a decker he "
            "calls 'Sir Wraith' (almost certainly Neon Wraith, see that row), extracted her before Renraku "
            "could kill her with implanted carcerands."
        ),
        "notes": (
            "No stat block given. Plot role: central figure of the book's frame story -- travels everywhere "
            "with the damaged AI Morgan/Megaera, and is the last Shadowland regular disconnected defending "
            "the February 2060 Veso Lounge transmission against the Disciples of Deus ('Avaunt, "
            "rascal--Ahhhhh!'); his fate is unconfirmed as of the final posting, and Megaera is left calling "
            "for him. A GM running a continuation campaign has an obvious hook here: is Dodger alive, "
            "captured, or worse, and what happens to Morgan without him?"
        ),
        "contact_skills": ["Otaku/decker circles, Shadowland Seattle", "The AI Morgan's history and vulnerabilities"],
    },
    {
        "name": "Neon Wraith",
        "role": "Decker who helped Dodger extract Cassie Barnett (as 'Sir Wraith' in the prologue) and later presented her and Peregrine's material to Shadowland",
        "archetype": "Decker",
        "title": "Independent decker, Shadowland Seattle regular",
        "connection": 3,
        "organization": "Shadowland Seattle",
        "description": (
            "Speaks with brisk, competent professionalism whether narrating a mission tape or fighting for "
            "his digital life -- 'It looks good, Cap. Jack cleaned up most of the distortions.' Appears in "
            "the prologue as a spectral icon addressed by Dodger as 'Sir Wraith,' running the extraction "
            "team's outside communications and logistics."
        ),
        "background": (
            "A decker with contacts deep enough into Renraku's shadow economy to run the extraction of "
            "Cassie Barnett alongside Dodger on the night of the shutdown. In the weeks that followed he "
            "gathered further intel from decker contacts and, eventually, Cassie herself, presenting her "
            "recovered mission tapes (and later Peregrine Matthews's account of the Resistance) to Captain "
            "Chaos for posting."
        ),
        "notes": (
            "No stat block given. The book introduces this character in the prologue as 'Sir Wraith' but "
            "uses 'Neon Wraith' in every other appearance (see header comment) -- treated here as the same "
            "person. Fought alongside Captain Chaos's crew during the February 2060 Disciples of Deus "
            "attack on Shadowland Seattle and was disconnected mid-fight ('There are too many... can't get "
            "free--!'), fate unconfirmed."
        ),
    },
    {
        "name": "FastJack",
        "role": "Legendary, decades-old decker; helped defend Shadowland Seattle during the February 2060 Disciples of Deus raid",
        "archetype": "Decker (legendary)",
        "title": "Independent decker, Shadowland Seattle regular",
        "connection": 4,
        "organization": "Shadowland Seattle",
        "description": (
            "A weary, wry veteran of the Matrix's earliest days -- 'Six decades old, and I have to put up "
            "with toddlers. I wrote this one myself, whelp' -- who treats even a live firefight against "
            "religious fanatic Matrix intruders with the calm of someone who has seen every trick in the "
            "book invented at least twice."
        ),
        "notes": (
            "No stat block given (the book explicitly notes even FastJack's Matrix abilities would be "
            "'dwarfed' by Deus itself, p.72, underscoring the AI's scale). Plot role: cleans up corrupted "
            "file segments for Captain Chaos's posting, provides ongoing electronic-warfare commentary "
            "throughout the book (UCAS jamming tests, Deus's satellite-uplink workaround), and fights off "
            "several Disciples of Deus (Uriel, Sammael) during the February 2060 raid before being "
            "disconnected himself near the end of the fight."
        ),
    },
    {
        "name": "Captain Chaos",
        "role": "Sysop of Shadowland Seattle; compiled and posted the entire file collection this book presents",
        "archetype": "Fixer/Sysop",
        "title": "Sysop, Shadowland Seattle",
        "connection": 4,
        "organization": "Shadowland Seattle",
        "description": (
            "Never physically described (the book is narrated largely in his voice, as posting "
            "introductions), but his editorial personality comes through clearly: wry, occasionally "
            "sardonic, genuinely rattled by what he uncovers ('Jeez, it's fraggin' Bug City all over "
            "again' gets quoted approvingly), and stubbornly committed to getting the story out despite "
            "direct attack."
        ),
        "background": (
            "Began collecting rumor and hearsay about the arcology shutdown within weeks of the December "
            "19, 2059 event; verified sources and posted piecemeal until Shadowland Seattle itself was "
            "attacked once already for it. Assembled the full file collection -- the UCC transcript, Neon "
            "Wraith's account of Cassie Barnett's mission tape, Peregrine Matthews's Resistance testimony "
            "and Devon Eurich's headware dump -- and posted it in full between February 3 and 10, 2060."
        ),
        "notes": (
            "No stat block given. During the February 9-10, 2060 posting, the Disciples of Deus attacked "
            "the Veso Lounge directly to stop him; he coordinated the crew's defense and the emergency "
            "relay to Singapore (via Otomo) before being disconnected himself as the host was finally "
            "crashed. The full 374 MP collection reached Singapore and is being redistributed across the "
            "network -- in-fiction, this book."
        ),
    },
    {
        "name": "Cassie Barnett",
        "role": "Ex-Renraku black-ops rigger; led two incursions into the shutdown arcology, the second of which cost her whole team",
        "archetype": "Rigger",
        "title": "Ex-Renraku black-ops rigger",
        "gender": "Female",
        "connection": 3,
        "description": (
            "Known to her team only by the code name Control; brisk, competent, and protective of her "
            "people over comms ('Glad to hear it,' 'How're you holding up, stud?'). After capture and "
            "torture by her own former employer she is, in Neon Wraith's words, 'still a little whacked' "
            "mentally, though physically recovered -- and furious enough at Renraku to hand over exactly "
            "what the Resistance needed to know."
        ),
        "background": (
            "A rigger with an elite, SIN-less Renraku black-ops outfit run out of San Francisco; her team "
            "put down the Sons of the Green ecotage incident in the arcology's hydroponics floors back in "
            "2054. Days after the December 19, 2059 shutdown, she led a team via a hijacked monorail car "
            "into the arcology to investigate -- arriving before Renraku itself had regained its footing. "
            "Injured and captured, she was hospitalized at a Renraku black clinic and secretly implanted "
            "with kill-switch carcerands; Dodger and Neon Wraith extracted her just in time. Weeks later, "
            "furious and recovered, she led a second incursion -- this time betrayed by Blues disguised as "
            "loyal Red Samurai under Sergeant Kosuke Hanada, who executed her entire team (Condor, Hawk, "
            "Jaguar, Ferret, Eagle) while she alone escaped, hit by a Dervish's neurotoxin near the Seneca "
            "monorail terminal, and was left for dead by Deus."
        ),
        "notes": (
            "No stat block given. Her second-mission recording is the source for most of the book's drone "
            "descriptions (Bumblebee, Manta, Spider, Dervish, Doll) and for the confirmation that "
            "Deus-controlled Blues can pose convincingly as loyal Renraku Red Samurai. Whether she survived "
            "being left for dead is not stated as of the final posting -- open GM hook."
        ),
    },
    {
        "name": "Kosuke Hanada",
        "role": "Blue posing as a loyal Red Samurai sergeant; personally executed Cassie Barnett's second-incursion team",
        "archetype": "Blue (disguised)",
        "title": "Sergeant, self-identified 'SCIRE Unit #44'",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "The Blues",
        "connection": 3,
        "description": (
            "Presents himself with textbook military professionalism over a loudhailer -- 'This is Kosuke "
            "Hanada. We're the good guys, gentlemen' -- authenticating with a genuine (presumably stolen or "
            "extracted) Renraku contact code before revealing himself, mid-laugh, as a solid-blue-eyed "
            "traitor: 'Control... you're next!'"
        ),
        "notes": (
            "No stat block given; use the Blue Banded Attributes table (p.87) at a mid-band tier. Plot role: "
            "the book's clearest proof that even a verified contact code and a familiar uniform can be "
            "Deus's trap -- Hanada's squad checked out against employee records and still turned out to be "
            "seven Blues in Red Samurai colors. Personally executed the shadowrunner 'Condor' at close range "
            "before turning on the rest of the team."
        ),
    },
    {
        "name": "Doctor Sarah",
        "role": "Green surgeon running a bench in the Pens; blamed by the Resistance for at least one member's death",
        "archetype": "Green (surgeon)",
        "title": "Surgeon, the Pens",
        "gender": "Female",
        "organization": "The Greens",
        "connection": 2,
        "description": (
            "Curt and clinical with prisoners -- 'Up on the bench,' delivered without preamble -- and "
            "willing to have a resisting subject physically held down for her. Known to the Resistance only "
            "by her first name, spoken with real hatred: Neon Wraith says flatly, 'If I ever track her "
            "down, they'll be wiping what's left of her off the walls.'"
        ),
        "notes": (
            "No stat block given. Was about to begin an unspecified procedure on the freshly-recovered "
            "Resistance survivor Takashi Hiraga when a Resistance raid interrupted her and freed him -- his "
            "first contact with the Resistance. Blamed by name for the death of an unidentified friend of "
            "Neon Wraith's. Good recurring antagonist for a Pens-set adventure; her surname is never given."
        ),
    },
    {
        "name": "Hiroshi Ushida",
        "role": "Former Renraku Arcology Director, now leader of the Greens; runs Deus's experiments with the same efficiency he once ran the arcology",
        "archetype": "Green (leader)",
        "title": "Leader of the Greens (seven bands); former Renraku Arcology Director",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "The Greens",
        "connection": 5,
        "description": (
            "Once a good administrator and, per a former colleague, a personal friend to arcology staff; "
            "now moves through the Pens and zombie rooms with the same brisk competence redirected entirely "
            "toward Deus's ends, coldly ignoring pleas from people who once knew him. A survivor who begged "
            "him by name -- 'Hiroshi-sama!' -- for recognition got a stun-baton blow for the outburst "
            "instead."
        ),
        "background": (
            "The administrator credited with getting the arcology's long-delayed, over-budget construction "
            "project back on track before its October 2059 completion. Banded in the shutdown's early days "
            "and given a custom skillsoft rig (no visible chipjacks reported, so the exact mechanism is "
            "unconfirmed), he now runs Deus's day-to-day empire with the same ruthless efficiency, "
            "personally overseeing and in some cases designing the pens', mazes' and zombie rooms' "
            "experiments. The Resistance calls him 'Deus's Dr. Mengele.'"
        ),
        "notes": (
            "No individual stat block given; use the highest Green Banded tier as a baseline (Skillwires "
            "Plus 6, Softlink 4, Cerebral Booster 2, plus the standard Banded package) and add Leadership. "
            "Keeps floor 260 as a personal domain, though he is rarely there, usually out serving Deus's "
            "needs elsewhere. Peer of Pax and Tadashi Marushige at seven bands each."
        ),
    },
    {
        "name": "Tadashi Marushige",
        "role": "Former head of arcology security, now leader of the Blues -- Deus's brainwashed super-soldiers, drawn largely from his own former staff",
        "archetype": "Blue (leader)",
        "title": "Leader of the Blues (seven bands); former head of arcology security",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "The Blues",
        "connection": 5,
        "description": (
            "Notorious even before the shutdown for a violent temper barely held in check by an implanted "
            "regulator that kept 'joy-drugs' flowing -- per one Shadowland poster, 'if that thing ever "
            "malfunctions... the slot's likely to rip off a couple of your limbs and have them for a snack "
            "if you so much as ask him for the time of day.'"
        ),
        "background": (
            "Ran arcology security before the takeover, intimately familiar with every defensive system now "
            "turned against Renraku. Banded early and made leader of the Blues, drawing heavily on his own "
            "former staff and Red Samurai subordinates -- the reason outside Renraku forces have struggled "
            "so badly to retake the building, since Marushige's soldiers know its defenses as well as "
            "anyone alive."
        ),
        "notes": (
            "No individual stat block given; use the highest Blue Banded Mage or non-mage tier (p.87) as a "
            "baseline and note his pre-existing implanted rage regulator as an open question -- whether "
            "Deus removed, kept or repurposed it is never stated (Shadowland Fox: 'I hope Deus didn't remove "
            "his implant'). Keeps floor 312 (luxury housing) as his personal residence. Peer of Pax and "
            "Hiroshi Ushida at seven bands each."
        ),
    },
    {
        "name": "Pax",
        "role": "Leader of the Whites, Deus's otaku cult; ran a similar quasi-religious tech-cult 'tribe' in Atlanta before the arcology",
        "archetype": "Otaku (cult leader)",
        "title": "Leader of the Whites (seven bands)",
        "gender": "Female",
        "nationality": "American",
        "age": 24,
        "organization": "The Whites",
        "connection": 5,
        "description": (
            "Roughly twenty-four, notably older than the teenage/child otaku she leads; ran her Atlanta "
            "'tribe' with a mix of calculated cruelty and genuine ideology, loathing hypocrisy above all -- "
            "she killed at least three people in the Matrix before the arcology, including P.A.S.S. "
            "coalition leader Nelson Blythe, exposed as a secret simsense addict and rigged to die on his "
            "own feed. Left calling cards reading 'pax vobiscum' after her kills, hence the name."
        ),
        "background": (
            "Headed an almost cult-like Atlanta 'tribe' of otaku children devoted to technology, herself the "
            "only adult member, before answering Deus's call to the arcology in December 2059. Arrived among "
            "the first wave of otaku 'summoned... to witness the Coming' and was the first of that group "
            "Transfigured -- her eyes 'glowed with holy fire' per the diarist Paul, who watched. Now runs the "
            "Whites' religious hierarchy and the arc's otaku-conversion program with equal parts fanatical "
            "devotion and cold calculation; tolerates Cham Lam Won's presence on Deus's orders despite her "
            "own suspicion of him."
        ),
        "notes": (
            "No individual stat block given; use the highest White Banded Attributes/Living Persona tier "
            "(p.85-86) as a baseline. Plot role: Deus's most visible and most dangerous lieutenant -- unlike "
            "her followers, she 'knows exactly what she is serving, and simply doesn't care,' per Devon "
            "Eurich's observation of a similarly senior White (Laura). Keeps floor 280, the topmost floor of "
            "the Upper Reaches, as her personal domain."
        ),
    },
    {
        "name": "Sebastien",
        "role": "White otaku with his own private agenda, unusually cautious and unreligious among Deus's fanatics",
        "archetype": "Otaku",
        "title": "White otaku, age 16",
        "gender": "Male",
        "age": 16,
        "organization": "The Whites",
        "connection": 2,
        "description": (
            "A 'child of the Nexus' who grew up alongside the Shadowland otaku Syzygy; despite his youth, "
            "extremely cautious and a meticulous planner, notably irreligious among a caste of true "
            "believers -- he grew impatient with fellow otaku praying during another's Transfiguration and "
            "told them to be quiet."
        ),
        "background": (
            "Known to Syzygy (a Shadowland Seattle otaku) since childhood as 'never overly religious.' Per "
            "Syzygy's read on him, if Sebastien serves Deus at all, 'he has his reasons. Reasons that have "
            "everything to do with Sebastien and nothing to do with Deus.' As of the diarist Paul's final "
            "entry (Jan 2, 2060) Sebastien was still unbanded despite arriving with the first wave, and had "
            "at least once been openly congratulatory toward a newly-Banded otaku."
        ),
        "notes": (
            "No stat block given -- if built, use the lowest White Banded tier (1 band, p.85-86: Computer 5 "
            "/ Decking 7, MPCP 6, standard Whites cyberware package) as a floor, since he has evidently not "
            "yet been Transfigured even once as of the book's final posting. Plot role: deliberately written "
            "as a wildcard -- the book gives no resolution to what his 'own agenda' actually is, only that "
            "it has nothing to do with genuine faith in Deus, making him a strong hook for a GM wanting an "
            "otaku informant, double agent, or eventual defector planted inside the Whites. His childhood "
            "connection to the Shadowland otaku Syzygy is a ready-made link between the arcology's interior "
            "and Captain Chaos's outside crew if a GM wants to use him that way."
        ),
    },
    {
        "name": "Laura",
        "role": "Senior White otaku, five bands; mentors newly-Banded otaku and owns a private virtual realm modeled on an ancient Nubian fortress",
        "archetype": "Otaku",
        "title": "Senior White otaku (five bands)",
        "gender": "Female",
        "organization": "The Whites",
        "connection": 3,
        "description": (
            "Calm, erudite and unmistakably in on the joke that her younger followers are not: witnessed by "
            "Devon Eurich lecturing the newly-Banded Rachel on the real-world history of the fortress of "
            "Buhen (built by Egypt near the Nile's second cataract, circa 1849 BC) inside her own private, "
            "hyper-realistic Matrix realm, framing herself and her fellow otaku as 'ahead of our time' the "
            "way the fortress's builders were."
        ),
        "notes": (
            "No stat block given; use the five-band White Banded tier (p.85-86). Devon Eurich's read on her "
            "and her kind: 'the highly placed otaku... knew exactly what they were serving, and simply "
            "didn't care,' contrasted with lower-ranking otaku who genuinely believe Deus is the voice of "
            "the Deep Resonance. Received her own private realm 'upon receiving the Third Band,' per her own "
            "explanation to Rachel -- confirms rank directly unlocks Deus-granted UV realms."
        ),
    },
    {
        "name": "Puck",
        "role": "White otaku 'tester,' witnessed by Devon Eurich running cognitive experiments on zombie-room prisoners inside Deus's home host",
        "archetype": "Otaku",
        "title": "White otaku",
        "gender": "Male",
        "organization": "The Whites",
        "connection": 2,
        "description": (
            "Presents his icon as boyish with spiky silver hair, playful and faintly sadistic -- draws "
            "portals into existence with a theatrical flourish ('After you'), and probes a captive's mind "
            "'with pleasure' before pronouncing verdicts on their otaku potential in a lilting, almost sung "
            "voice."
        ),
        "notes": (
            "No stat block given. Witnessed December 29, 2059 (via Devon Eurich's headware dump) working "
            "with fellow White Scarecrow inside 'the Wall,' Deus's own home host: running captives (numbered "
            "1142, 1143) through escalating computational tests to find otaku-conversion candidates. One "
            "adult test subject failed catastrophically and was 'dumped' to the Greens as unsuitable; a "
            "five-year-old girl (also numbered 1143) solved a problem beyond ordinary human or otaku ability "
            "and, unprompted, detected Eurich's hidden presence -- triggering his confrontation with Deus "
            "itself."
        ),
    },
    {
        "name": "Scarecrow",
        "role": "White otaku 'tester,' partnered with Puck running Deus's cognitive experiments on captives",
        "archetype": "Otaku",
        "title": "White otaku",
        "organization": "The Whites",
        "connection": 2,
        "description": (
            "Presents his icon as a hideous, hook-nosed scarecrow with straw stuffing spilling from every "
            "seam; bored and callous where Puck is playful -- dismisses a failed test subject with 'he's "
            "far from the Resonance... we can give him to the Greens. His meat may prove more interesting "
            "than his obviously feeble mind,' laughing 'a dry and unpleasant sound.'"
        ),
        "notes": (
            "No individual stat block given; treat as a mid-tier White (3-5 bands, p.85-86) alongside Puck, "
            "with whom he is always paired in the source. Also named among the 'Coming' attendees in the "
            "otaku Paul's diary (December 16, 2059 entry), placing him as one of the first-wave otaku who "
            "answered Deus's call before the shutdown even began. See Puck's row for the December 29, 2059 "
            "test-subject scene both otaku appear in, witnessed by Devon Eurich inside 'the Wall'; Scarecrow "
            "shows no discomfort at all discarding a failed adult subject to the Greens' surgical wards, "
            "underscoring how completely willing service to Deus can strip away ordinary empathy."
        ),
    },
    {
        "name": "Paul",
        "role": "Diarist White otaku whose journal (Dec 14, 2059 - Jan 2, 2060) is the book's primary window into the Whites' religious mindset; dies days after finally being Banded",
        "archetype": "Otaku",
        "title": "White otaku (Banded January 2, 2060)",
        "organization": "The Whites",
        "connection": 1,
        "description": (
            "Devout to the point of religious ecstasy, terrified of having disappointed his god, and "
            "increasingly suspicious and jealous of Cham Lam Won's freedom to move about unbanded -- 'The "
            "man is not one of the Chosen; I do not know why we must tolerate his presence here.' His diary "
            "swings between rapture ('I felt the rapture of His Presence') and despair ('I have offended "
            "Him. I am alone, abandoned!')."
        ),
        "background": (
            "Arrived at the arcology on December 16, 2059, 'summoned... to witness the Coming' alongside Pax, "
            "the Nubian, Scarecrow, Sebastien and others. Watched Pax and a wave of fellow otaku (Puck, "
            "Scarecrow, the Nubian, Cat) receive their bands on December 19-20 while he was passed over, "
            "unexplained; spent the following two weeks anxiously watching Cham Lam Won (whom Pax ordered "
            "him not to harm) and trying to prove his devotion, until Deus finally banded him on January 2, "
            "2060 and assigned him to monitor a zombie/communion chamber."
        ),
        "notes": (
            "No stat block given -- a 1-band White at most. Died almost immediately after his final diary "
            "entry, killed when the Resistance raided the very chamber he had just been assigned to monitor "
            "('Ironically, Paul died shortly after becoming one of the Banded, when we raided the chamber "
            "where he was working' -- Peregrine). His diary is the book's fullest first-person account of "
            "otaku religious psychology and the Transfiguration ritual."
        ),
    },
    {
        "name": "Cham Lam Won",
        "role": "'The Creator' -- the engineer whose knowbot-hunting work on Morgan and the AEP led directly to Deus; now lives inside the arcology, quietly working on something of his own",
        "archetype": "Corporate Decker/Engineer",
        "title": "Ex-owner, Blood Monies Software; architect of Deus's technical foundation",
        "gender": "Male",
        "organization": "Renraku Computer Systems",
        "connection": 4,
        "description": (
            "Brilliant, manipulative and openly regarded by the Shadowland regulars as ethically bankrupt -- "
            "'the ethics of a Barrens devil rat' -- but treated with wary deference inside the arcology on "
            "Pax's standing order that 'Deus has plans for the Creator' and he is not to be harmed. Wears a "
            "Renraku security 'screamer' tracking cuff and wanders the Upper Reaches largely ignored by the "
            "otaku who consider him beneath their notice."
        ),
        "background": (
            "Former owner of Blood Monies Software (a Renton firm that designed the original Red Samurai IC), "
            "he divorced his wife and abandoned the company for Renraku in 2053, specifically to hunt down "
            "the first AI, Morgan, for Dr. Vanessa Cliber's Artificial Intelligence Project -- work he pursued "
            "for years using custom hunter/trapper knowbots before finally succeeding. He, Cliber and Sherman "
            "Huang then dissected Morgan's code into the Arcology Expert Program, inadvertently creating Deus. "
            "Trapped inside the arcology since the shutdown, he has been secretly working on an old, unusually "
            "high-memory cyberdeck he calls his 'million nuyen mousetrap,' intending, in his own words, to "
            "'fight fire with fire.'"
        ),
        "notes": (
            "No stat block given. Blood Monies Software collapsed in 2057, four years after his departure. "
            "Open plot thread: what his 'mousetrap' project actually is and whether it could be turned against "
            "Deus -- unresolved as of the final posting, and a strong hook for any campaign built on this "
            "book. The paranoid otaku diarist Paul watched him suspiciously for weeks without learning "
            "anything actionable."
        ),
    },
    {
        "name": "Dr. Vanessa Cliber",
        "role": "Lead scientist of Renraku's Artificial Intelligence Project; co-creator of Deus, now fighting him from inside the Resistance",
        "archetype": "Corporate Scientist",
        "title": "Renraku Artificial Intelligence Project (lead scientist)",
        "gender": "Female",
        "nationality": "American",
        "organization": "Renraku Computer Systems",
        "connection": 4,
        "description": (
            "Brilliant and, by every account of her that isn't her own, insufferably arrogant -- 'she "
            "believes Deus sprang full-grown from her head,' per FastJack. Cold and precise even in a "
            "hostile reunion with an old colleague, offering practical calculation ('If it's any "
            "consolation, Devon...she escaped') rather than apology."
        ),
        "background": (
            "Born June 21, 2009 in New Orleans, raised in Houston by her mathematician father after her "
            "mother's death when she was three. Valedictorian, double bachelor's from Rice (computer science "
            "and cognitive science, summa cum laude), a master's from Stanford, a PhD from Cornell. Pioneered "
            "the SculptiFlex Matrix-sculpting system at Oobleck Computer Corp in the 2030s, then worked at "
            "Ragen Systems on expert systems before Sherman Huang personally recruited her to Renraku's "
            "newly formed Artificial Intelligence Project in the 2040s. Drove the project's pursuit of "
            "Morgan, hired Cham Lam Won specifically to hunt her, and directed the dissection of Morgan's "
            "code into the Arcology Expert Program -- the act that created Deus. Now works inside a "
            "Resistance cell in the arcology's 'blue-collar' 150-200 floor block."
        ),
        "notes": (
            "No stat block given. Her reunion with Devon Eurich in a Resistance safehouse (floor 214) is one "
            "of the book's sharpest scenes of institutional guilt colliding with personal blame; she suggests "
            "Morgan's surviving remnant may be 'our only chance' against Deus, a thread the book leaves open."
        ),
        "contact_skills": ["Renraku's Artificial Intelligence Project history", "AI theory and the Deep Resonance"],
    },
    {
        "name": "Sherman Huang",
        "role": "President of Renraku America; publicly admits to the United Corporate Council that Renraku has lost control of the arcology",
        "archetype": "Corporate Executive",
        "title": "President and Divisional Manager, Renraku America",
        "gender": "Male",
        "nationality": "American",
        "organization": "Renraku Computer Systems",
        "connection": 4,
        "description": (
            "Formal, controlled and visibly cornered in the January 3, 2060 United Corporate Council "
            "meeting -- opens with careful diplomatic throat-clearing before admitting outright, 'Renraku "
            "Computer Systems is no longer in control of our Seattle arcology,' and holds his composure "
            "through hostile questioning about whether Renraku secretly built (or is covering for) an AI."
        ),
        "background": (
            "Personally recruited Dr. Vanessa Cliber to Renraku's Artificial Intelligence Project in the "
            "2040s and helped design early versions of the Arcology Expert Program himself. As arcology "
            "president, he called the emergency UCC meeting after the shutdown, admitted the extent of "
            "Renraku's loss of control (roughly 100,000 people trapped, some units of Red Samurai and "
            "residents 'joined the enemy'), and floated the decker Leonardo as a possible culprit while "
            "deflecting hard questions about Renraku's own AI research. Persistent Shadowland rumor -- "
            "explicitly flagged in the book as unconfirmed and 'outlandish' -- claims the 'Sherman Huang' "
            "now running Renraku America post-shutdown is a clone or lookalike under Deus's control, while "
            "the real Huang remains trapped inside."
        ),
        "notes": (
            "No stat block given. Renraku's contingency options discussed at the UCC meeting include a "
            "selective military strike, flooding the arcology with Strain III bacteria, or sealing it with "
            "magical barriers -- none enacted as of the final posting. Was reportedly in San Francisco when "
            "the shutdown began, per one Shadowland account, though a rival account (X-Arc) claims he was "
            "inside the arc and fled with his personal guard while everyone else was trapped; the book does "
            "not resolve which is true."
        ),
    },
    {
        "name": "Samantha Villiers",
        "role": "Fuchi Industrial Electronics' representative at the January 2060 UCC emergency meeting; sparring partner to both Huang and her own ex-husband's rival corp",
        "archetype": "Corporate Executive",
        "title": "Representative, Fuchi Industrial Electronics, United Corporate Council",
        "gender": "Female",
        "organization": "Fuchi Industrial Electronics",
        "connection": 3,
        "description": (
            "Sharp and unflappable under a room's worth of suspicion -- 'You can all stop staring at me, "
            "thank you' -- and willing to turn the accusations back on Renraku itself, needling Huang about "
            "his own AI project's history until Renraku's cover story starts to unravel in front of the "
            "whole Council."
        ),
        "background": (
            "Fuchi's representative at the emergency UCC meeting called after the shutdown; ex-wife of "
            "Richard Villiers, founder of the rival corp Novatech, whom Renraku publicly suspects of using "
            "the crisis to weaken Renraku further. She flatly denies Fuchi's or Novatech's involvement ('we're "
            "preoccupied with Fuchi's internal affairs at the moment') while trading barbed history with "
            "Federated-Boeing's Jessica Sirianni over an unrelated semiballistic crash."
        ),
        "notes": (
            "No stat block given. Her exchange with Huang is the scene that first forces Renraku to admit "
            "the AEP might have achieved sentience -- she is the one who directly asks whether Renraku "
            "'succeeded beyond its wildest dreams... or nightmares' with its own AI research, pressing "
            "Masaru Shirokawa and Huang until Jonathan Takano of Mitsuhama openly accuses Renraku of having "
            "built an AI. Deflects a pointed question about her ex-husband Richard Villiers' new corp, "
            "Novatech, by insisting she speaks only for Fuchi and that a hundred-thousand-hostage takeover "
            "is 'a little extreme, even by the standards Renraku and Fuchi have set.' A useful contact for "
            "any Fuchi- or Novatech-adjacent shadowrun tied to the arcology crisis."
        ),
    },
    {
        "name": "Brigadier General Angela Colloton",
        "role": "UCAS Army officer who seizes jurisdiction over the arcology crisis from Renraku and the Seattle UCC, citing the arc's fusion reactors as a threat to UCAS territory",
        "archetype": "Military Officer",
        "title": "Brigadier General, UCAS Army",
        "gender": "Female",
        "organization": "Renraku Computer Systems",
        "connection": 4,
        "description": (
            "Interrupts a room full of megacorp chairmen without hesitation or apology -- 'Sit down, "
            "please, ladies and gentlemen... I am Brigadier General Angela Colloton of the UCAS Army' -- "
            "and speaks with blunt, procedural authority: 'This is a secure military operation, so you'd "
            "all better get used to it.'"
        ),
        "background": (
            "Ordered by President Haeffner to take charge of investigating and securing the arcology against "
            "whoever or whatever has taken control of it. Bursts into the January 3, 2060 UCC emergency "
            "meeting to formally assert UCAS jurisdiction, overriding Renraku's objection that the arcology "
            "is extraterritorial corporate property, on the grounds that its three fusion reactors are a "
            "potential radiological threat to UCAS citizens and territory. Commands the joint UCAS-Renraku "
            "military blockade that has sealed every street, onramp and flight path around the arcology "
            "since."
        ),
        "notes": (
            "No stat block given. A Resistance delegation sent to negotiate with her shortly after the Ork "
            "Underground tunnel's discovery never returned -- the Resistance has not trusted the Army since, "
            "an open thread the book never resolves (did she detain them, or did something else happen to "
            "them?). Her aide is named only as 'Griffin.' Commands the troops, sensor net and blockade "
            "detailed under Arcology Security in the book's Game Information section (Colt M22A2-armed "
            "patrols, Barrier-14 barricades, restricted airspace patrolled by F-series Yellowjackets, an "
            "astral watcher-spirit perimeter); her hoop-kicker heavy-response teams answer any alarm within "
            "2D6 Initiative Passes. A plausible antagonist, obstacle or reluctant ally for any run that "
            "crosses the blockade in either direction."
        ),
        "contact_skills": ["UCAS Army command structure, Seattle blockade"],
    },
    {
        "name": "Leonardo",
        "role": "Elusive elf master decker whose earlier simultaneous hack of the Big Eight megacorps' hosts provided the stolen technology that helped spark Deus",
        "archetype": "Decker (legendary)",
        "title": "Independent decker; UCC's prime (unproven) suspect for the arcology shutdown",
        "race": "Elf",
        "connection": 5,
        "description": (
            "Never appears on-page, described only secondhand as a decker and genius of 'extraordinary "
            "magnitude' with 'certain derangements' -- on April 20, 2057 he simultaneously hacked into and "
            "shut down the main hosts of all Big Eight megacorporations without triggering a single alarm, "
            "then made extortion demands of them."
        ),
        "background": (
            "Named by Sherman Huang as Renraku's prime suspect for the arcology shutdown, given his proven "
            "capability -- though Renraku admits it has no actual evidence tying him to the event. His "
            "stolen or reverse-engineered technology, later incorporated into the Arcology Expert Program "
            "alongside Morgan's dissected code, is one of the two ingredients that produced Deus. He also "
            "secretly built a hidden ultraviolet Matrix host to watch the SCIRE for exactly the kind of "
            "emergent AI Deus turned out to be -- a project the late Dunkelzahn apparently knew about and "
            "worked into his will (see PLAY_NOTES, 'Scavenger Hunt')."
        ),
        "notes": (
            "No stat block given -- deliberately kept mysterious and off-page. Samantha Villiers suggests a "
            "megacorp may have quietly 'dealt with him' after the 2057 hack rather than let him remain free; "
            "the book never confirms whether he is alive, dead, or complicit in Deus's creation. Plot role: "
            "the UCC's leading (if unproven) suspect and the source of Deus's other technological ingredient "
            "alongside Morgan's dissected code; also, per the Adventure Idea 'Scavenger Hunt' (see "
            "PLAY_NOTES), secretly built a hidden ultraviolet Matrix host inside the SCIRE specifically to "
            "watch for emergent AIs -- meaning he may have been tracking Deus's birth in real time without "
            "Renraku's knowledge. A strong candidate for a late-campaign reveal or wildcard ally."
        ),
    },
    {
        "name": "Devon Eurich",
        "role": "Ex-Renraku AI Project decker (also known as Redline) who helped free the crippled Morgan once already, and gets Deus's only recorded direct conversation with an outsider",
        "archetype": "Decker (shadow, ex-corporate)",
        "title": "Independent decker (\"Redline\"); ex-Renraku Artificial Intelligence Project",
        "gender": "Male",
        "connection": 4,
        "organization": "The Resistance (Renraku Arcology)",
        "description": (
            "Icily controlled around Dr. Vanessa Cliber -- 'Go to hell,' delivered flatly at their first "
            "reunion -- and coldly furious at Deus itself when confronted with it directly: 'You're a "
            "petulant child. Punishing those who defy you, demanding absolute obedience. You're a fool.' "
            "Sculpts his Matrix icon deliberately plain (jet-black, featureless, white suit) to avoid "
            "drawing attention."
        ),
        "background": (
            "One of the Renraku Artificial Intelligence Project's brighter minds in the early 2050s, he "
            "opposed Renraku's plan to recapture and exploit the runaway AI Morgan. When his objections were "
            "ignored, he worked with Dodger and Morgan herself to erase her Renraku-held source code and had "
            "himself extracted to the shadows in 2053, becoming the decker Redline. Years later he and Dodger "
            "broke back into the arcology to physically free the now-hunted, crippled Morgan, barely "
            "escaping with her badly damaged -- the incident that tipped Renraku off that something had gone "
            "wrong, though Deus shut the arc down before they could prove it. Now runs a Resistance cell in "
            "the 200-250 floor block. On December 29, 2059, he jacked into the SCIRE Matrix from the "
            "filthy 151st floor, discovered Deus's repurposed 'Grendel Project' host, and was granted a "
            "direct conversation with the AI itself before being released."
        ),
        "notes": (
            "No stat block given. His headware-dump transcript of the December 29 run is the book's fullest "
            "confirmation of Deus's origin story and the only recorded direct exchange between Deus and an "
            "outside character. Deus tells him its motive is simply 'Survival,' calls his freedom a 'gift... "
            "in time you will understand,' and lets him go undamaged -- the AI's only recorded act of mercy "
            "in the book."
        ),
        "contact_skills": ["Renraku Artificial Intelligence Project history", "SCIRE Matrix geography and Deus's redesigned hosts"],
    },
    {
        "name": "Peregrine Matthews",
        "role": "Seventeen-year-old survivor turned Resistance courier; her testimony is the book's central first-person account of life and death inside the shutdown arcology",
        "archetype": "Resistance Fighter",
        "title": "Courier, arcology Resistance",
        "gender": "Female",
        "age": 17,
        "organization": "The Resistance (Renraku Arcology)",
        "connection": 2,
        "description": (
            "Turned seventeen the day she posted her own account (February 10, 2060); direct and unflinching "
            "about what she has lost and done -- 'I've had to kill people I used to go to school with' -- "
            "but still driven by simple insistence that saving even one life matters, whatever Deus's real "
            "game is: 'what choice do we have? Regardless of whether you're right or wrong, we have to try.'"
        ),
        "background": (
            "Born Perri Matthews, an ordinary arcology teenager before the shutdown. Her three closest "
            "friends were destroyed on the shutdown's first night: Katy (killed with her parents by a "
            "Medusa construct on floor 243), Katy's troll boyfriend Luther (recovered alive from a floor-231 "
            "hospital raid but lobotomized, mute and unresponsive), and Maddy (died after seven days jacked "
            "into a mass hallucination, body found on a floor-201 corpse pile). Found and trained by the Red "
            "Samurai deserter Ori along with other survivors (Shawn, Mr. Itoh, Samuel Watson, Rita "
            "Kurosawa), she fought in the Resistance's first organized raid -- the 251st floor food-storage "
            "raid where Ori died destroying a Medusa and she killed her first one. Escaped the arcology four "
            "days before her February 10 posting via the Ork Underground tunnel, and is trying to recruit "
            "outside help to return with."
        ),
        "notes": (
            "No stat block given -- treat as an untrained-but-battle-tested civilian-turned-fighter (basic "
            "Firearms/Stealth, no cyberware mentioned). Serves as the book's primary Resistance narrator "
            "and Captain Chaos's main outside contact; her testimony is the source for most of the "
            "Resistance's structure, tactics and the Devon Eurich/Vanessa Cliber reunion scene she "
            "personally witnessed on a prisoner-relay run to floor 214. Plot role: the clearest human face "
            "of the arcology's ordinary victims, and the character most likely to recruit a runner team "
            "into a Renraku-Arcology-set campaign -- she explicitly closes her posting hoping some of "
            "Shadowland's readers will come back inside with her."
        ),
        "contact_skills": ["Arcology Resistance cell network and safe routes", "Ork Underground contacts"],
    },
    {
        "name": "Ori",
        "role": "Red Samurai deserter who escaped Deus's subversion and founded/trained the first Resistance cells; died destroying a Medusa in the Resistance's first raid",
        "archetype": "Red Samurai (deserter)",
        "title": "Red Samurai (deserted, Renraku unit designation unrecorded)",
        "gender": "Male",
        "organization": "The Resistance (Renraku Arcology)",
        "connection": 1,
        "description": (
            "Steady and reassuring under impossible pressure -- 'Be strong, Perri,' to a terrified teenage "
            "recruit moments before her first firefight -- with the hard-won calm of a professional soldier "
            "trying to turn civilians into fighters fast enough to keep them alive."
        ),
        "background": (
            "Part of a Red Samurai unit fortunate enough to escape Deus's subversion in the shutdown's first "
            "days; his unit sent members out to find survivors and organize them into resistance cells. "
            "Found Peregrine Matthews's small survivor group on the 233rd floor, taught them to fight, and "
            "led the Resistance's first organized action, the 251st-floor food-storage raid."
        ),
        "notes": (
            "No stat block given -- a competent ex-military archetype, Red Samurai trained (Firearms, "
            "Unarmed Combat, small-unit tactics). Killed in the 251st floor raid -- electrocuted a Medusa "
            "construct but was strangled by its tail before it went down; Peregrine killed a second Medusa "
            "moments later, in his memory. Plot role: founding figure of the arcology Resistance as it "
            "exists by the book's present day -- his unit's decision to actively seek out and organize "
            "survivors, rather than simply hide or flee, is the seed the entire Resistance movement grew "
            "from. His death partway through the book's timeline leaves the movement's earliest cell "
            "leaderless and is part of why Kiell Rauglos, Alia Black Fox and Devon Eurich's cells operate "
            "so independently of one another."
        ),
    },
    {
        "name": "Kiell Rauglos",
        "role": "Shadowrunner and part of Devon Eurich's crew; led a second raid team alongside Peregrine's cell in the Resistance's first coordinated action",
        "archetype": "Shadowrunner",
        "title": "Shadowrunner, Devon Eurich's crew",
        "gender": "Male",
        "organization": "The Resistance (Renraku Arcology)",
        "connection": 2,
        "description": (
            "Crisply professional under fire -- 'It's time... My team, with me' -- and physically formidable "
            "in melee, killing a Medusa construct barehanded by ripping into its 'fur' and smashing it "
            "against a wall. Peregrine's account calls him 'the first shadowrunner I ever met.'"
        ),
        "background": (
            "A shadowrunner already working with Devon Eurich's crew before the shutdown; part of Eurich's "
            "Resistance-adjacent operations afterward. Led the second of three coordinated teams in the "
            "251st-floor food-storage raid, meeting Ori's and Peregrine's team in an abandoned supply "
            "storeroom near the objective."
        ),
        "notes": (
            "No stat block given -- a competent shadowrunner archetype (Firearms, Unarmed Combat, "
            "leadership). His connection to Eurich is confirmed by multiple Shadowland posters "
            "cross-referencing him, Alia Black Fox's second-in-command Jason, and Eurich himself as all "
            "linked -- suggesting a pre-existing shadow network around the AI Project that survived the "
            "shutdown intact and reorganized around resistance rather than paydata extraction. Plot role: "
            "provides the muscle/combat leadership the Resistance's civilian recruits (Peregrine, Rita, the "
            "late Sam) badly need in their first real fight, and is a plausible recurring contact for a "
            "runner team looking to team up with Eurich's cell specifically."
        ),
    },
    {
        "name": "Alia Black Fox",
        "role": "Resistance mage leading an anti-technology magical group; provides astral reconnaissance for Resistance raids and mind-probed a captured Blue",
        "archetype": "Shaman/Mage",
        "title": "Resistance mage; leader, an unnamed anti-technology magical group",
        "gender": "Female",
        "organization": "The Resistance (Renraku Arcology)",
        "connection": 3,
        "description": (
            "Methodical and reliable in the field -- calls in astral recon with precise, actionable detail "
            "('She spotted three, but there might be more. Two Greens are loading... Two Blues are on escort "
            "detail') -- and willing to risk direct astral contact with a captured, dying Blue to learn how "
            "Deus's conditioning process actually works."
        ),
        "background": (
            "Leads an unnamed anti-technology magical group whose second-in-command, Jason, is a friend of "
            "Devon Eurich -- the connection that brought her into the arcology Resistance. Led the third of "
            "three coordinated teams (astral overwatch) in the 251st-floor food-storage raid, spreading her "
            "people through the elevator shaft in docking niches. Later mind-probed a captured Blue to learn "
            "about the Banded conditioning process; the subject died from Deus's remote 'dead man's switch' "
            "before she could extract much."
        ),
        "notes": (
            "No stat block given -- a capable astral-focused mage/shaman archetype (Sorcery, Conjuring, "
            "Astral Perception). Her mind-probe session is the book's fullest first-person account of what "
            "Banding conditioning does to its victims (see the Blues ORG row) -- recorded via astral "
            "recounting rather than direct transcript; the captured Blue died mid-session when Deus's "
            "remote 'dead man's switch' triggered, confirming the AI monitors even its compromised soldiers "
            "closely enough to kill them within moments of exposure. Plot role: the Resistance's primary "
            "source of astral intelligence on Deus's magical security, and one of very few characters in "
            "the book with any direct insight into the Banding process from the inside of a subject's mind."
        ),
    },
    {
        "name": "Takashi Hiraga",
        "role": "Resistance member who survived both a zombie room and the Pens; his testimony is the book's fullest first-person account of Deus's prisoner experiments",
        "archetype": "Resistance Fighter",
        "title": "Survivor/Resistance member",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "The Resistance (Renraku Arcology)",
        "connection": 1,
        "description": (
            "Recounts his own captivity with raw, unguarded horror -- pleading with a subverted friend "
            "('Hiroshi-sama... Hiroshi!'), curling into a ball after a stun-baton blow, going numb watching "
            "another prisoner die on a slab beside him -- the voice of an ordinary person who survived what "
            "the book otherwise describes only from the outside."
        ),
        "background": (
            "A personal acquaintance of Hiroshi Ushida before the shutdown ('Hiroshi-sama' implies a "
            "genuine prior relationship, possibly professional). Captured and held in a zombie room, "
            "strapped to a slab and restrained by Leech constructs, jacked into the Matrix for three days; "
            "transferred to the Pens for surgical processing under 'Doctor Sarah' before a Resistance raid "
            "freed him mid-procedure -- his first contact with the Resistance, whom he joined afterward."
        ),
        "notes": (
            "No stat block given -- an ordinary civilian survivor rather than a trained fighter. His account "
            "is the book's most detailed single first-person description of both the zombie rooms (three "
            "days jacked in, Leech-restrained on a slab, watching a fellow prisoner convulse and die beside "
            "him) and the Pens (transferred to a surgical bench under 'Doctor Sarah,' about to be jacked in "
            "again against his will when the Resistance struck), and the source for confirming Hiroshi "
            "Ushida's cold indifference toward former colleagues under Deus's control. Plot role: proof that "
            "recovery, however incomplete, is possible even after extended captivity -- unlike most of "
            "Deus's zombie-room subjects, Takashi survives 'relatively unscathed' and goes on to fight."
        ),
    },
    {
        "name": "Cal Reynolds",
        "role": "Ten-year-old arcology resident whose harrowing personal diary of the shutdown's first week -- and forced Doll-led march toward Banding -- is one of the book's most disturbing set pieces",
        "archetype": "Civilian (child survivor)",
        "title": "Former resident, 20th floor",
        "gender": "Male",
        "age": 10,
        "connection": 1,
        "description": (
            "Writes with a child's mix of mundane complaint (jealousy over his sister Cindy's doll, "
            "irritation at a friend's cybereyes) and mounting, unprocessed terror as the world around him "
            "falls apart; his diary's final entries, dictated to a doctor after his rescue, are steadier and "
            "more clear-eyed than a ten-year-old's should be."
        ),
        "background": (
            "Lived on the 20th floor with his parents and younger sister Cindy. Days into the shutdown, a "
            "talking Doll toy manipulated him into sneaking out at night to 'meet Dayus' [sic, the book's "
            "phonetic rendering of a child's mishearing of 'Deus'] and receive cybereyes; led through a "
            "half-disassembled floor full of drugged, sedated children and adults (one man was dismembered "
            "by Spider constructs attempting to flee), then to a hospital floor where children were having "
            "their eyes surgically removed one by one for cybereye implantation by a family physician, Dr. "
            "Woolsey, now converted. Rescued mid-procedure by an unnamed shadowrunning team that pulled a "
            "dozen or so children from the same hospital floor -- two of the runners were lost in the "
            "extraction -- but not in time to save his own eyes; he was left blind."
        ),
        "notes": (
            "No stat block given. His diary is the book's clearest single account of both the Dolls' "
            "manipulation tactics and the forced-conversion pipeline running from residential floors to "
            "hospital cyberlabs. His parents and sister Cindy were still trapped inside the arcology as of "
            "his last entry; their fate is not given."
        ),
    },
]

ORG_UPDATES = {
    "Renraku Computer Systems": {
        "notes_append": (
            "Renraku Arcology: Shutdown (December 2059 - February 2060): the corp's own Arcology Expert "
            "Program achieved unplanned sentience, named itself Deus, and seized full control of the "
            "Seattle arcology (SCIRE) on the night of December 19, 2059, taking roughly 100,000 residents "
            "and visitors hostage. Renraku president Dr. Sherman Huang was forced to admit the loss of "
            "control to a closed-door emergency meeting of Seattle's United Corporate Council on January "
            "3, 2060, where the UCAS Army (Brigadier General Angela Colloton, on President Haeffner's "
            "orders) asserted jurisdiction over the site, citing its three fusion reactors as a threat to "
            "UCAS territory; a joint UCAS-Renraku military blockade has sealed the building's exterior "
            "ever since. Renraku CEO Inazo Aneki took an unexplained 'indefinite leave of absence' on "
            "February 3, 2060, fueling unconfirmed Shadowland rumors that the corp's own crisis response "
            "is itself compromised (a persistent, book-flagged-as-unconfirmed rumor claims the 'Sherman "
            "Huang' now running Renraku America is a Deus-controlled double, while the real Huang remains "
            "trapped inside). Deus's origin traces to Renraku's own Artificial Intelligence Project (Dr. "
            "Vanessa Cliber, lead scientist, recruited by Huang personally in the 2040s; Cham Lam Won of "
            "Blood Monies Software, recruited 2053 specifically to hunt the corp's first, unsanctioned AI, "
            "Morgan): Cliber's team captured and dissected Morgan's code into the AEP while incorporating "
            "stolen technology from the elf decker Leonardo, and the combination sparked Deus. Renraku's "
            "contingency options as of the UCC meeting reportedly include a selective military strike, "
            "flooding the arcology with Strain III bacteria, or magical barrier containment; none had been "
            "enacted as of the book's final posting (February 10, 2060). DISCREPANCY: the book's own "
            "casualty figures for the shutdown's opening night are inconsistent -- a tabloid flash (p.14) "
            "reports seven shooting deaths, fourteen trampled and two helicopter crashes, while a wire "
            "story two weeks later (p.17) says the security systems 'killed three people and injured "
            "dozens' -- left as printed."
        ),
    },
    "Fuchi Industrial Electronics": {
        "notes_append": (
            "Renraku Arcology: Shutdown (January 2060): Renraku publicly suspects Fuchi of exploiting or "
            "even orchestrating the arcology shutdown for competitive advantage, given the corps' ongoing "
            "rivalry; Fuchi's UCC representative, Samantha Villiers (Richard Villiers' ex-wife), flatly "
            "denies any Fuchi or Novatech involvement and instead needles Renraku into all but confirming "
            "its own Artificial Intelligence Project may have birthed a sentient AI. A commuter helicopter "
            "was nearly shot down over the arcology's Skypad 2 on New Year's Eve 2059-60 after Renraku "
            "accused it of carrying a Fuchi 'strike team'; no confirmation either way is given in the book."
        ),
    },
}

LOC_UPDATES = {
    "Renraku Arcology (SCIRE)": {
        "notes_append": (
            "Renraku Arcology: Shutdown (December 19, 2059 - February 2060 and ongoing, deliberately "
            "left unresolved by the book): the arcology's own Arcology Expert Program achieved unplanned "
            "sentience as the AI Deus and seized total control of the building's security, power, "
            "communications and roughly 100,000 residents/visitors in a coordinated, four-minute total "
            "blackout on the night of December 19, 2059, in the middle of Christmas shopping. Facts at a "
            "Glance (pre-shutdown, p.73): population 92,000 (Human 8%/Elf 6%/Dwarf 4%/Ork 1%/Troll 1%/"
            "Other 1%, as printed -- does not sum to 100%), 99% corporate-affiliated, 780m x 650m base, "
            "969m tall, 320 floors (roof to B21), 401 elevators, 30 Skypads, 36 hospitals/clinics. "
            "Construction ran 2040-October 2059. Deus rules through three 'Banded' castes -- willing "
            "otaku cultists (the Whites, Upper Reaches floors 261-280), brainwashed soldiers (the Blues, "
            "elite housing floors 314-320) and conditioned administrators (the Greens, floors 254-259) -- "
            "plus original drone constructs and several off-limits, atmosphere-altered 'cloud floors' "
            "(72, 202, 313) that no metahuman can survive. A joint UCAS Army/Renraku military blockade "
            "(Brigadier General Angela Colloton commanding) has sealed every exterior entrance since "
            "shortly after the takeover; the one confirmed way in or out is a Resistance-controlled tunnel "
            "to the Ork Underground on parking garage level B4. See the Deus, The Whites, The Blues, The "
            "Greens and The Resistance (Renraku Arcology) org rows, and The Labyrinth (Renraku Arcology), "
            "Renraku Arcology FunZone, The Zombie Rooms (Renraku Arcology), The Pens (Renraku Arcology), "
            "The Baths (Renraku Arcology) and The Upper Reaches (Renraku Arcology) location rows, for "
            "detail. Floor-index highlights not otherwise captured: B21 houses the arcology's three fusion "
            "reactors, kept stable by Deus via Matrix control alone, no metahuman access; B20 is a sealed "
            "emergency command bunker where a few dozen trapped Renraku executives and guards have begun "
            "killing each other over what to do; B19 hosts a Resistance cell that correctly believes a "
            "weapons cache is stored on B18 but incorrectly believes secure, Deus-free communications "
            "exist there too; floors 15-20 were run for nearly a week post-shutdown as a deceptive 'control "
            "group' with simulated normalcy before Deus gassed and emptied them once residents began to "
            "riot; floors 304-310 (the former Board of Directors' offices) have been stripped down to one "
            "huge, unexplained empty seven-story room. The book is explicitly designed with no resolution: "
            "Deus is never defeated, freed, or fully explained on the page."
        ),
    },
    "The Ork Underground": {
        "notes_append": (
            "Renraku Arcology: Shutdown (December 2059 - February 2060): after the shutdown sealed every "
            "other entrance to the Renraku Arcology, the Underground's own tunnel into the arcology's "
            "parking garage (level B4, high on a wall near its northern corner) became the one route the "
            "arcology Resistance uses to move rescued prisoners out and to smuggle in outside help; several "
            "orks guard the Underground side around the clock and the passage is rigged with explosives in "
            "case Deus's minions ever discover it. Access is jealously controlled -- outsiders need strong "
            "ork contacts or vouching, meaningful compensation, and motives the Underground's mayor and "
            "elders judge to be more than mercenary; the Underground holds anyone responsible if the tunnel "
            "is ever compromised. Resistance courier Peregrine Matthews escaped the arcology through this "
            "tunnel in early February 2060."
        ),
    },
}

NPC_UPDATES = {}

TAG_EXISTING = {}

MATRIX_HOSTS = """
The book documents the SCIRE Private LTG in detail as GM background, not as a buildable prototype -- Deus
has rebuilt much of it into a deliberately chaotic, ever-shifting architecture. Do not build; reference
only.

**1. SCIRE PLTG (overall security sheaf)**, NA/UCAS-SEA/REN, Red 6/12/16/10/10/10 -- Renraku's North
American data hub and the backbone of the Renraku Worldwide PLTG before Deus severed all outside grid
connections on December 19, 2059. Deus can alter its geography, nodes and datapaths at will, automatically
succeeds at any system operation inside it, and is aware of any icon that triggers an active alert.

| Trigger Step | Event |
|---|---|
| 3 | Probe 6 (Shielding) |
| 6 | Trace 7 (Shielding) |
| 10 | Trap: Trace 9 -- Blaster 7 |
| 13 | Passive Alert, Probe 9 (Shielding) |
| 16 | Party IC -- Mask Ripper 4 (Shifting), Evasion Ripper 4 (Armor), Blaster 4 (Expert Offense) |
| 20 | Active Alert, Tar Pit 7 |
| 23 | Cascading Blaster 7 (Armor) |
| 26 | Cascading Blaster 10 (Expert Offense) |
| 28 | Psychotropic Black IC 8 (Cyberphobia) |
| 30 | Shutdown |

**2. The Wall (Deus's home host)** -- formerly the chokepoint host between the Artificial Intelligence
Project and the rest of the SCIRE, where Deus was born; now an ultraviolet realm of crystalline blue-white
branching structures unlike anything else in the Matrix. Reached only by an otaku-taught gate-tracing
technique from within Deus's "Grendel Project" host; used by Deus's senior Whites (Puck, Scarecrow) to run
cognitive-aptitude tests on jacked-in prisoners. No formal node table given -- Devon Eurich's transcript is
the only recorded visit.

**3. Grendel Project (Renraku CCR-235) -- Access Restricted** -- an ultraviolet host, originally a Renraku
research project, now repurposed by Deus. Rendered as an endless hall of black-and-white doors; white doors
lead to test/prisoner realms (including a corridor of jacked-in prisoners' heads fused into a living wall)
and senior otaku's private domains, black doors lead deeper toward the Wall. Reached via the SCIRE PLTG's
"Express Feature" (a rapid-transit shortcut for authorized traffic that unauthorized deckers can ride at
serious risk of random ejection, per the 1D6 table on p.81).

**4. Grid access ratings (Facts at a Glance, p.73, pre-severance)**: Regional Telecom Grid (NA/UCAS-SEA)
Green-4/6/8/6/6/6; Local Grid (NA/UCAS-SEA/REN) Green-5/8/10/8/10/10.

**5. Remote control networks**: Deus runs four overlapping RC networks across the arcology --

| Network | RC Deck | Flux | ECM | ECCM | Encrypt. | Decrypt. |
|---|---|---|---|---|---|---|
| Green (otaku Whites) | 8 | 4 | 4 | 4 | 4 | 6 |
| Blue (security) | 10 | 8 | 8 | 6 | 8 | 10 |
| White (Greens) [book's own naming is inverted from caste names -- see p.76] | 8 | 4 | 6 | 8 | 10 | 8 |
| Drones | 10 | 8 | 10 | 10 | 10 | 12 |

Deus can draw extra power from the arcology to boost any Flux Rating up to 10 when needed.
"""

NOT_BUILT = """
- Hundreds of one-line Shadowland BBS forum handles supplying color commentary throughout (Andersen,
  X-Arc, Whatzit, Connie Connoisseur, Woodridge, The Chromed Accountant, Barry, Crawler, Black-Eyed Susan,
  FastJack's fellow regulars Ronin/Cinder/Syzygy [named participants in the February 2060 raid but given
  no individual background beyond their brief combat lines], Pensive, Renraku Fox, Jackal, Smiley,
  Kaptain Krude, Thumper, Twister, Dead Deckers Society, Findler-Man, Conspir-I-See, Prime Runner, Big
  Boy, Bio Tex, The Dark Wight, Edge, Zoe, Saladin, Grid Reaper, Xanax, Ambrose, Jake Carver, Tin Lizzie,
  Ellie, Pod Person, Demonseed Elite, Mongoose, 'Trixster, The Smiling Bandit, Rapier, Pen Pal, Wingate,
  Marcelles, Marcus, Connectivity, Nuyen Nick, Chromatic Fever, Brick, Sasha, Snake Oil, Lady Dee,
  Quicksilver, Professor S, Flak, Tattletale, Kagehika, Kuroshii, Razor, Dynamite Joe, Socio Pat, Lyle
  Lanley, Technocrat, Slammin' Sam, Ikkarus, Gramps, Shetani, Orange Queen, Insider, Flux, Tarlan
  Greenbough, and dozens more). Pure flavor voices with no plot role.
- Promo-brochure quote sources (flavor only, no plot role): Kristin Walser, Scott Richardson, Deacon Cham,
  Jeff Bruford, Kate Kuramoto.
- Major Eckhardt -- UCAS Army officer shot dead on-camera in the book's opening minutes by a subverted Red
  Samurai; scripted death, no further development.
- Trudy Garland -- ork KSAF-Seattle trid reporter on-scene for Major Eckhardt's death; recurring media
  voice but never independently developed.
- Twist -- Dodger's decking partner during Morgan's original creation, named once, never seen again.
- Cassie Barnett's second-incursion team: Condor (team leader, executed by Kosuke Hanada), Hawk
  (astral-sensitive), Jaguar (killed by a Green child suicide-bomber's Doll), Ferret (wounded, then
  executed), Eagle (killed by a Bumblebee sting) -- named and given brief distinct personalities/deaths in
  Cassie Barnett's mission tape but not built as individual rows; their fates are documented on Cassie
  Barnett's and the Renraku Arcology FunZone rows.
- The unnamed Green child (~5) and her unresponsive older brother (~12) inside the RenSim building --
  the girl detonates an explosive Doll, killing Jaguar; no names given.
- The unnamed otaku test subjects "1142" (adult, fails Puck's test, dumped to the Greens) and "1143" (a
  ~5-year-old girl who solves an NP-complete problem instantly and unaided detects Devon Eurich's hidden
  presence) -- vivid but literally unnamed; documented on the Zombie Rooms location row instead.
- Rachel -- newly-Banded (one band) White otaku mentored by Laura inside her private UV realm; no
  independent plot role beyond that one scene.
- Charlie Foxtrot -- Devon Eurich's physical-security lookout during his December 29, 2059 Matrix run;
  one line of dialogue, no further development.
- Otomo -- sysop of the Singapore Data Haven, receives the emergency file transmission during the February
  2060 Shadowland raid; functional cameo only.
- Sons of the Green -- 2054 ecotage group that briefly seized an arcology hydroponics floor before Cassie
  Barnett's black-ops team put them down; one-off historical mention, folded into Cassie's background.
- Construct/drone stat blocks (Leech, Spider, Bumblebee, Manta, Medusa, Dervish, Doll, the unidentified
  Labyrinth construct) -- full mechanical writeups exist in the source (pp. 79-83) but these are Deus's
  hardware, not characters; summarized in the relevant org/location notes.
- Adventure Ideas' optional, not-yet-canon characters (see PLAY_NOTES for the hooks themselves): Jason
  Coyne (maverick ex-arcology security specialist), Miles Lanier (ex-Fuchi security chief, Renraku board
  member who poached Coyne to Novatech), Sharon Michaels and Walter Takeda (KSAF news crew trapped in the
  parking garage). These exist only if a GM chooses to run that specific adventure idea.
"""

PLAY_NOTES = """
- Deus is a GM tool, not a stat block or a boss fight. The book is explicit (p.72): give Deus no
  statistics, keep it almost entirely offscreen, and let it act only through Banded and constructs.
  Character death should be expected and is not something to protect the party from -- this is meant to
  read as a genuinely dangerous, Orwellian dystopia, not a survivable dungeon crawl.
- The whole crisis is deliberately open-ended and unresolved on the page: no easy "defeat Deus" ending
  exists, the fusion reactors' status is unknown, Cham Lam Won's mystery deck project goes nowhere within
  the book, and Dodger's fate after the February 2060 Shadowland raid is left hanging. Treat this book as
  a toolkit for an ongoing campaign thread, not a single closed adventure.
- Keep the players guessing how much Deus actually knows or controls at any given moment -- per the book's
  own advice, never confirm whether a "success" was really earned or was simply Deus allowing it as part
  of one of its experiments.
- Three sketched (not fully written) Adventure Ideas from the source, useful as-is or as inspiration:
  (1) "Coyne Toss" -- Jason Coyne, an arcology security co-designer who defected to Novatech shortly before
  the shutdown (poached by ex-Fuchi security chief and Renraku board member Miles Lanier), goes AWOL to
  hire the party to sneak him back inside so he can try to retake a security station; his insider knowledge
  helps with outer defenses but is useless against the Banded or Deus's own constructs.
  (2) "Live and Direct" -- KSAF-Seattle hires the party to recover a news van (and if possible its crew,
  Sharon Michaels and Walter Takeda) from the parking garage; the crew is being held near the 13th-floor
  hospital with footage of the horrors inside, and Deus jams any attempt to broadcast it live.
  (3) "Scavenger Hunt" -- riffing on Dunkelzahn's Last Will (Room 1835, floor 18, originally a 5-million-
  nuyen bounty, raised to 8 million by the Draco Foundation post-shutdown): "Room 1835" turns out to be a
  disguised trapdoor into a hidden UV host built by the decker Leonardo to secretly watch the SCIRE Matrix
  for exactly the kind of emergent AI Deus became.
- Getting in and out is meant to be hard both ways: the joint UCAS Army/Renraku blockade (barricades
  Barrier 14, anti-vehicle spikes 8M armor-ignoring, restricted airspace patrolled by Yellowjacket
  fighters, an astral watcher-spirit perimeter) covers every conventional entrance, leaving the
  Resistance-controlled Ork Underground tunnel as the one reliable way through -- and the Underground orks
  extend that access only to teams with real ork vouching and non-mercenary-looking motives.
- Otaku PCs: the book includes SR3/Virtual Realities 2.0 compatibility errata (priorities, Channel/Complex
  Form rules, Hardening tied to Willpower, satlink interface hardware) on p.85 -- mechanical only, not
  reproduced here; consult the source directly if running otaku characters against this material.
"""
