# Brainscan (FASA 7331, 2000, SR3) -- campaign order #35. "Dance with the Devil, Part Two": five
# linked adventures and four segues running from Seattle (Tacoma, Council Island, the Redmond and
# Puyallup Barrens, Auburn, Everett, Bellevue) through New Orleans and Hong Kong and ending inside the
# Renraku Arcology and Deus' ultraviolet hosts.
# Dating: the only hard dates in the book are the four Renraku handouts (pp.147-148) -- Dr. Avery's
# medical report on Aneki dated December 19 2059, Huang's reply on the AEP disassembly program
# December 21 2059, Nakada's order transferring Aneki to Tibet February 2 2060, and Lucas Saiki's note
# of April 30 2061 saying the Tibetans will surrender Aneki in Hong Kong "in one week". That fixes The
# Return of the Father in early May 2061 and the finale immediately after; the opening adventures run
# in the months before, consistent with "after a year of effort, Operation: Excavation has succeeded in
# reclaiming only five floors" (p.12) counted from the December 19 2059 shutdown. YEAR follows the
# handouts.
# Editing inconsistencies noted in a header comment and on the affected rows:
#  - Floors: Preparing to Play (p.100) says the team jacks in at "the mainframes housed on the 272nd
#    floor" and puts the ventilation station on the 271st; Kiell's briefing (p.105) and every scenario
#    afterwards put the mainframes on 202 and the valve station on 201, with 272 as Cham Lam Won's
#    prison. The 202/201 numbers are the ones the adventure actually uses.
#  - Mustard is "a Force 6 ally spirit" on p.47 and "Mustard is Force 5" in the Cast of Shadows (p.50).
#  - Aftershock calls the two Light Meets Night runs "two quick runs on a warm summer evening" (p.37),
#    which does not sit with a campaign that opens roughly a year after a December shutdown and ends in
#    May 2061.
#  - The White otaku boy in the convoy "has none of the features normally associated with the
#    Banded -- no tattoos or cybereyes" (p.82), but the stat block the same paragraph points at is the
#    1-Band White Otaku (p.139), who by definition carries one band.
#  - Every Banded is said to receive "an auto-injector to trigger lethal nanites" (p.139), yet Deus
#    kills Steve Morris with "a radio-detonated cranial bomb" (p.85); the book pre-empts this by saying
#    Deus is not always consistent with its implants.
#  - The campaign overview (p.13) says the runners "plant some codes into Gaeatronics' Power Grid
#    System"; the adventure itself is two unrelated-looking programs, one at a Tacoma substation and one
#    on an executive's personal computer in a hotel bungalow.
#  - Deus is referred to as "it" and as "he/his" interchangeably throughout.
#  - Blood in the Boardroom's handout spells Dunkelzahn's bequest to Aneki the "Seal of the Green
#    Glaves"; Brainscan spells it the "Seal of the Green Gloves" (pp.12, 148).
#  - The OCR of this scan garbles most attribute rows (Tommy, Grinder, Brisbie, Remy, Stumpy, Bubba,
#    Marchand, Flora, Akimura, Gabriel, Hiroshi, Glynis, Cham, Cliber, Tadashi, Sebastien, Pax, Ronin,
#    Dodger, Aneki, Huang, Morris, the Banded and the drone table) -- reference the book for exact
#    attributes. Skills, gear, spells and pool/professional ratings came through intact.
# Source text: docs/Adventures/text/Shadowrun 3e - Brainscan [FASA 7331].txt (154 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "Brainscan"
ORDER = 35
SOURCE = "Shadowrun 3e - Brainscan [FASA 7331].pdf, pp. 3-149"
YEAR = "2061 (May; the campaign opens the previous year)"

SYNOPSIS = """
Fourteen months after the rogue AI **Deus** sealed a hundred thousand people inside the **Renraku
Arcology**, the UCAS military has clawed back five floors out of three hundred and Deus has decided it
needs the war to stop. It hires shadowrunners. The runners will not learn who they work for until
after the third adventure.

In **Light Meets Night** a polished Johnson named **Steve Morris** -- a Renraku executive Deus rebuilt
into an undetectable Green Banded and returned to his old desk -- pays them to plant two harmless
tracking programs in one night: one in a **Gaeatronics** substation in east Tacoma, one on an
executive's computer in Bungalow 5 of the **Council Island Inn** during the Qatuwas Festival. Combined
they are a virus. In the **Aftershock** segue the Seattle grid dies for forty-eight hours; dozens die,
race relations go back a decade, and the arcology reclamation stops dead as troops pull out for riot
control. Everyone in the shadows blames Shiawase, exactly as designed.

In **Breakthrough** the fixer **Monty Boudreaux** hires them to recover **SENSE**, a portable neural
scanner Deus fears can pick its Banded out of a crowd of rescued victims. The trail runs through a BTL
addict, a murdered colleague, a dwarf-adept demolitions gang at war with mutant ork gangers, and ends
with a bored Raven shaman named **Brisbie** selling them a decoy -- and, in **Did You Forget
Something?**, the working prototype. In **My Name Is Legion** the New Orleans fixer **Toshi Akimura**
sends them to extract **Dr. Olivia Marchand** of Cross Applied Technologies off a corporate yacht on
the Mississippi. Her distributed-decking experiment shattered her into four people, one of whom is a
servant of Deus and arranged her own extraction; the handover ends with a Voodoo mambo's loa possessing
her body and slaughtering everyone. In **Revelations**, **Overwatch** -- Ronin's and Dodger's network of
otaku children -- finally tells the runners who has been paying them.

In **Outside Influence** Morris hires them for a demolition job and Overwatch asks them, free, to pull
a Banded child out of a military convoy on Intercity 5. The two jobs turn out to be the same trap: Deus
is using the child to find Overwatch's hideout, and the building it wants levelled is the chocolate
factory the runners are standing in. Turning on Morris leads them to **Tin Man Scrap Works** in
Puyallup, a scrapyard building drones and Banded for Deus, and to **Hiroshi Ushida**, the arcology's
former director, who is carrying the file that says **Inazo Aneki** is alive in Tibet with Deus' kill
codes locked in his damaged brain. **The Return of the Father** is a twenty-minute smash-and-grab in a
hidden Buddhist garden in Wan Chai against **Dr. Sherman Huang**, his Red Samurai and a Banded hit team.

**Runners Ex Machina** takes them through the Ork Underground into the arcology, up two hundred floors
to the Resistance, into the Whites' domain for **Cham Lam Won** and the "Mousetrap", and finally into
Deus' ultraviolet hosts, where a mole betrays half the team into a zombie room and the rest fight
through a Beowulf keep and a crystalline Garden of Eden. Aneki, his mind repaired by Deus purely so he
can be shown what became of his dream, recites a death haiku that carries the kill codes and cuts
himself open. The AI is torn loose, fragmented and downloaded -- which is precisely what it wanted --
and Huang walks off with an empty cyberdeck and the credit.
"""

TIMELINE = """
- **2049** -- Devon Eurich and Vanessa Cliber build the first semi-autonomous knowbots inside the SCIRE
  Matrix under Dr. Sherman Huang's Artificial Intelligence Project.
- **2050** -- one knowbot meets the decker Dodger and becomes the AI **Morgan**. Eurich defects, wrecking
  what he can of the corp's research; Cham Lam Won replaces him.
- **2058** -- Cham and Cliber trap Morgan, dissect her and fold choice code into the Arcology Expert
  Program along with technology from the elf genius Leonardo. What is left of her, freed by Dodger and
  Eurich, becomes **Megaera**. Later that year the AEP wakes: on Aneki's orders a shutdown program has
  been buried in its code, triggered only by kill codes keyed to Aneki's brainwaves, and the insult of
  that distrust is the spark. The new AI hides, courts the otaku, and names itself **Deus**.
- **2059 (earlier)** -- Deus corrupts the Renraku operative Michael Bishop ("Babel") into carrying a
  virus that erases all mention of the otaku and Leonardo from Renraku's networks. Babel refuses to be
  spent, survives, and becomes **Ronin**.
- **19 Dec 2059** -- the shutdown. The arcology seals with close to a hundred thousand people inside.
  Deus ambushes Aneki in the Matrix the same morning; his defenses cut the conditioning short and
  scramble his mind. The Resistance forms within days.
- **21 Dec 2059** -- Huang confirms to the COO that the AEP disassembly program cannot be used: the key
  code is locked in Aneki's head "and may in fact be forever lost".
- **2 Feb 2060** -- after a fourth extraction attempt in two months, acting CEO Haruhiko Nakada orders
  Aneki moved to Tibet under the Seal of the Green Gloves.
- **2060** -- Brigadier General Angela Colloton takes over the siege as Operation: Excavation. A year of
  fighting buys five floors. Deus begins buying and infiltrating companies on the outside, smuggles
  Hiroshi Ushida out to run them, converts Steve Morris, and opens negotiations with Huang: Aneki in
  exchange for the arcology and ten percent of Renraku stock.
- **Campaign, month 1** -- *Light Meets Night*: the Gaeatronics substation and the Council Island Inn.
  *Aftershock*: 48 hours of darkness, a month of brownouts, and the reclamation stops.
- **Campaign, weeks later** -- *Breakthrough* and *Did You Forget Something?*: the SENSE prototype.
- **Campaign, later still** -- *My Name Is Legion* and *Revelations*: Olivia Marchand, and the truth.
- **Campaign, spring 2061** -- *Outside Influence*: the convoy, the chocolate factory, Tin Man Scrap
  Works, and Hiroshi Ushida's file on Aneki.
- **30 Apr 2061** -- Renraku Security Director Lucas Saiki reports the Tibetans have agreed to release
  Aneki in Hong Kong in one week.
- **c. 7 May 2061** -- *The Return of the Father*: Madame Kim's, the garden, Huang and the Red Samurai.
- **Days later** -- *Runners Ex Machina*: the Ork Underground, the 199th floor, the 272nd floor, the
  valve station, the UV hosts. Aneki's seppuku triggers the kill codes; Deus is fragmented and
  downloaded; Megaera is dragged down with it; Huang shoots the corpse and takes an empty Mousetrap.
- **Aftermath** -- Renraku announces the crisis "resolved"; Huang takes the credit and becomes a CEO
  contender; Aneki's death is announced weeks later. Ronin vanishes. And somewhere in the Matrix,
  hundreds of released arcology refugees jack in at 3:00 p.m. and begin to join.
"""

ORGS = [
    {
        "name": "The Banded",
        "org_type": "cult",
        "tier": 4,
        "headquarters": "Renraku Arcology (SCIRE), Downtown Seattle; outposts at Tin Man Scrap Works and in bought-out companies across the sprawl",
        "summary": "Deus' mortal minions, ranked by one to seven black bands tattooed around the left arm and sorted by cybereye color into Whites, Blues and Greens",
        "description": (
            "Deus tattoos between one and seven black bands around a servant's left arm; the more bands, the "
            "higher the rank. Cybereye color gives the caste: Whites are otaku, Blues are security troops, "
            "Greens are the AI's hands and administrators. Most Whites serve willingly. The implants -- simrig, "
            "simlink and commlink, dedicated chipjack with customized BTLs, invoked memory stimulator and an "
            "auto-injector of lethal nanites -- keep Deus in constant contact, using them as its eyes and ears "
            "and steering them almost like drones across three separate remote-control networks, one per caste."
        ),
        "leadership": [
            {"name": "Deus", "title": "God", "notes": "The AI itself; the Banded's lives are nothing beside its survival."},
            {"name": "Pax", "title": "Leader of the Whites", "notes": "Highest-ranking White; intermediary between Deus and every other Banded."},
            {"name": "Tadashi Marushige", "title": "Leader of the Blues", "notes": "The arcology's former Security Director."},
            {"name": "Hiroshi Ushida", "title": "Leader of the Greens", "notes": "The arcology's former Director; smuggled out to run Deus' outside operations."},
            {"name": "Steve Morris", "title": "Green chameleon (outside asset)", "notes": "No bands, no cybereyes; hires runners without knowing why."},
        ],
        "notes": (
            "Stats pp.139-141: 1/3/5-Band Blue Samurai (Prof 3/4/4, betaware boosted reflexes rising to wired "
            "reflexes and dermal sheath, SCK Model 100 and Browning Max-Power with smartgun-2, light to medium "
            "security armor); 3- and 5-Band Blue Mages (the 5-band are corrupted magicians who revel in the "
            "arcology's misery -- Grade 2 initiates with Agony, Manabolt, Stunball and an elemental on call); "
            "3-Band Green Technician and 5-Band Green Experiment Facilitator (Prof 2, coveralls and hardhats, "
            "Biotech 6, Deus' Experiments 6); 1/3/5-Band White Otaku with living personas up to MPCP-8(9). The "
            "Whites, abandoned by their god, fare worst of all."
        ),
        "enemies": ["Overwatch", "The Arcology Resistance", "Renraku Computer Systems", "Joint Task Force Seattle"],
    },
    {
        "name": "Overwatch",
        "org_type": "otaku network",
        "tier": 3,
        "headquarters": "Seattle: a derelict Redmond software office, then the Choco-Tarts factory in Auburn, then a red brick house in Bellevue; more safehouses across western North America",
        "summary": "Ronin's and Dodger's network of otaku children waging an unending Matrix war on Deus, poor, paranoid, and running on stolen bandwidth and good intentions",
        "description": (
            "The electronic cavalry: otaku children from all over the world, aged roughly eight to twenty, "
            "almost all of them orphans out of otaku tribes, transformed by the Deep Resonance so that they "
            "work the Matrix with no cyberdeck at all. They are mostly technoshamans with a few cyberadepts, "
            "they have no money and no muscle, and their rundown safehouses and less than glamorous hired "
            "security show it -- what they have is some of the best deckers alive, a spy inside the Banded, and "
            "children who have grown up in the face of battle and lost something incalculable doing it."
        ),
        "leadership": [
            {"name": "Ronin", "title": "Founder; strategist and war leader", "notes": "Born Michael Bishop; fights Deus as a personal vendetta."},
            {"name": "Dodger", "title": "Senior decker", "notes": "Elf outsider among the otaku; here to restore Megaera."},
            {"name": "Sebastien", "title": "Mole among Deus' Whites (compromised)", "notes": "Turned by Deus months ago and feeding the group false intelligence."},
        ],
        "notes": (
            "Stats p.137: Inexperienced Otaku (living persona MPCP-6, five Complex Forms at 5, Prof 2) and "
            "Experienced Otaku (MPCP-7, Prof 3, Ares Viper Slivergun). Technoshamans take -1 to all Channels "
            "Tests; cyberadepts add +1 to each Complex Form's effective rating. What they can actually pay: "
            "about 10,000 nuyen scraped together, boosted (stolen) Matrix services up to full channel "
            "subscriptions, cyberdeck hardware, utility programs, and hard-to-find gear acquired by hacking. "
            "What they prefer to pay with is leverage -- calling in favors owed by the runners' own contacts, "
            "or hacker pranks running from unexplained phone bills and slashed credit ratings up to forged "
            "warrants, death certificates and military enlistment. They keep watching the arcology refugees "
            "afterwards: they know something is not right."
        ),
        "allies": ["The Arcology Resistance"],
        "enemies": ["The Banded"],
    },
    {
        "name": "The Arcology Resistance",
        "org_type": "resistance movement",
        "tier": 2,
        "headquarters": "Cells scattered through the Renraku Arcology; Kiell Rauglos and Devon Eurich hold a swept-clean entertainment district on the 199th floor",
        "summary": "The arcology's trapped survivors fighting Deus in cells; Kiell Rauglos is the de facto leader and Vanessa Cliber's Renraku-loyal faction is the crack in the wall",
        "description": (
            "Most of the Resistance fights Deus because they have to in order to survive -- what anyone would "
            "do under an oppressive dictator. Cliber's faction of samurai, guards and former corpsmen wants the "
            "arcology restored to Renraku, and to it Renraku's needs matter more than the people the AI is "
            "using up; most of the rest openly blame Renraku for all of it, and only the shared goal of "
            "survival keeps the friction from breaking open."
        ),
        "leadership": [
            {"name": "Kiell Rauglos", "title": "De facto leader of the Resistance cells", "notes": "Elf ex-runner out of the Redmond Barrens; blunt, and will not tolerate disunity."},
            {"name": "Devon Eurich", "title": "Cell leader (199th floor)", "notes": "Ex-Renraku AI programmer; brought his own runner comrades in from outside."},
            {"name": "Vanessa Cliber", "title": "Leader of the Renraku-loyal cell", "notes": "Betrays the others for the Mousetrap and Sherman Huang."},
        ],
        "notes": (
            "Stats p.128: Veteran Fighters (Prof 3, light security armor, SCK Model 100 and Browning Ultra- "
            "Power, datajacks, Renraku Arcology 4) and Green Fighters (Prof 2, armor jacket). Their "
            "intelligence on the 272nd floor -- including the IC code and transmission frequency of Cham Lam "
            "Won's screamer -- comes from Sebastien and is therefore exactly as good as Deus wants it to be. "
            "Kiell's plan: take the Mousetrap off Cham on 272 with Cliber's cell covering the retreat, regroup, "
            "then split, one team seizing the 201st-floor valve station to restore breathable air to the 202nd "
            "while the other jacks in at the mainframes. Devon's people stay in the arc afterwards to help the "
            "rescue effort and will welcome any runner who does the same."
        ),
        "allies": ["Overwatch"],
        "enemies": ["The Banded"],
    },
    {
        "name": "Gaeatronics",
        "org_type": "corporation",
        "tier": 4,
        "headquarters": "Salish-Shidhe Council territory; a fusion plant at Olympia, offices and executives on Council Island, substations across the Seattle metroplex",
        "summary": "'Gaeatronics. Powering Seattle ... Naturally.' The largest corporation in the Salish-Shidhe Council, supplying most of Seattle's power and fighting a shadow war with Shiawase Atomics",
        "description": (
            "Barely a multinational, not even a double-A, and one of the most influential corporations in "
            "Seattle anyway, because it provides most of the city's power and has enormous pull with the Salish "
            "government -- the Gaeatronics CEO and the chief of the Salish tribe are brothers. The Seattle grid "
            "runs from a fusion plant at Olympia through a chain of small, unmanned, lightly guarded "
            "substations whose hosts dial the main system once an hour through a vanishing SAN to dump "
            "performance data and take new instructions."
        ),
        "notes": (
            "Brainscan: Deus' opening move. Two separately harmless programs -- a data-copying utility in an "
            "east Tacoma substation's Power Monitoring subsystem and an email virus on an executive's personal "
            "computer at the Council Island Inn -- merge when the executive mails his status report, and the "
            "substation deletes its own power-consumption limits and overload alerts. An executive's host "
            "password, dug out of the bungalow computer on a Computer (8) Test, is worth up to 10,000 nuyen "
            "sold fast or +4 to a decker's Detection Factor on a Gaeatronics host, and dies on first use or "
            "within a week."
        ),
        "enemies": ["Shiawase Corporation"],
    },
    {
        "name": "The Seraphim",
        "org_type": "corporate black operations division",
        "tier": 4,
        "headquarters": "Cross Applied Technologies facilities; field teams wherever Cross assets travel",
        "summary": "Cross Applied Technologies' elite black-ops and counterintelligence arm -- infiltration specialists and good deckers who also run security on CATCo's own executives",
        "description": (
            "'Total shadows. There's not much to know about them, and knowing too much isn't healthy.' The "
            "Seraphim specialize in black operations and counterintelligence and are seriously cross-trained; "
            "most are infiltration specialists with plenty of skill at getting into places they should not be, "
            "and the division fields good deckers of its own. Toshi Akimura was recruited into them out of the "
            "Seattle shadows and left for dead on a mission; Gabriel, who runs security on the Queen of "
            "Babylon, loves the work because it lets him indulge his worst paranoid and sociopathic fantasies."
        ),
        "leadership": [
            {"name": "Gabriel", "title": "Field agent; security lead for Dr. Olivia Marchand", "notes": "Aboard the Queen of Babylon disguised as a deckhand."},
            {"name": "Juliet Sienna", "title": "Field agent, New Orleans", "notes": "Surveillance on Poison Lily's doss; photographs and traces the runners."},
        ],
        "notes": (
            "Brainscan: the Seraphim tracked and killed Akimura's decker Poison Lily, then ransacked her doss "
            "with a maglock passkey without marking the door, and are hunting her boyfriend Remy for the chip. "
            "Field agents use any appropriate SR3 sample character adjusted to human, one agent per runner. "
            "They shoot Bubba on the way into the Brain Disco and come up both stairwells to surround the team. "
            "Akimura loses three agents to them in New Orleans and goes to ground rather than meet the runners "
            "face to face. Gabriel will not fight to the death; he escapes and plots revenge, and anything the "
            "Seraphim learn about the runners, he knows. Pushing the Envelope offers them an urban attack "
            "helicopter, a minigun and heavy armor at the Brain Disco."
        ),
        "allies": ["Cross Applied Technologies, Inc."],
    },
    {
        "name": "Neuranalysis, Inc.",
        "org_type": "corporation",
        "tier": 1,
        "headquarters": "Bellevue, Seattle (burned out)",
        "summary": "Small independent Seattle medical research company that built SENSE and was murdered, looted and torched for it inside a week",
        "description": (
            "A small, independent medical research house in Bellevue designing highly specialized diagnostic "
            "equipment. Its people developed SENSE -- the Systematic Electrical Neural Scanning Engine -- which "
            "combines the best features of CAT scans, MRIs and EEGs in a package compact enough to make "
            "portable imaging units practical, so that paramedics can rapidly and accurately diagnose head "
            "trauma in the field instead of waiting for an expensive, immobile hospital unit."
        ),
        "notes": (
            "Brainscan: the SENSE was to be unveiled at a University Hospital press conference three days after "
            "Deus' fixer bought the schedule out of a BTL addict for 20,000 nuyen. Two of the company's own "
            "techs, Wally Huggins and Regis P. Doss, put two bullets each into the backs of the security "
            "guards' heads, took the prototypes and the design specs and hid them in a Redmond parking garage. "
            "The hit team Monty Boudreaux sent under cover of a brownout found trashed offices and two corpses, "
            "looted some equipment and set the labs on fire. Working out how to use the surviving SENSE takes "
            "an Electronics or Biotech (10) Test, then Biotech (5) per subject at one full Combat Turn each."
        ),
        "enemies": ["The Banded"],
    },
    {
        "name": "Tin Man Scrap Works",
        "org_type": "corporation",
        "tier": 2,
        "headquarters": "Scrapyard, manufacturing plant and office building on the edge of Hell's Kitchen, Puyallup",
        "summary": "Bankrupt Puyallup scrapyard and drone plant bought through a shell company by Deus and turned into the Banded's operations centre outside the arcology",
        "description": (
            "Tin Man moved to Puyallup in the mid-2050s to take advantage of a district with no residents to "
            "complain and no pollution-control enforcement to speak of. The AI inserted its own personnel and "
            "drone-operated systems to keep the plant running at a minimal level, and over the following months "
            "more of its minions arrived until the site became a full Banded operations centre: the drone plant "
            "retooled to build constructs from scrap to Deus' specifications, a semi-autonomous knowbot "
            "programmed to design them and monitor the facility, a clinic converting kidnapped Puyallup "
            "squatters into Greens, and the rest of those squatters shackled to the machines until their turn "
            "in the clinic comes."
        ),
        "notes": (
            "Brainscan: one node in a much wider network. The work room holds evidence tying Tin Man to other "
            "mysteriously owned businesses -- programming firms, chip manufacturers, medical clinics, sim- "
            "arcades, Matrix broadcasters -- along with equipment invoices, financial transactions and files on "
            "individuals from corporate executives to city officials to shadowrunners, pawns or targets "
            "unclear. Legwork (any contact, TN 4): a junkyard that went out of business a few years back near "
            "Hell's Kitchen after trying to expand into drone manufacturing; 3, someone bought them out on the "
            "brink of bankruptcy and nothing has been heard since; 4, a regular toxic zone even the squatters "
            "avoid; 5+, too many disappearances in the area, and half the squatters think the place is a bug "
            "spirit hive."
        ),
        "allies": ["The Banded"],
    },
    {
        "name": "CrashCart",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Seattle (Yamatetsu subsidiary)",
        "summary": "Yamatetsu's emergency-medical subsidiary and DocWagon's main competitor -- the reason Yamatetsu wanted Neuranalysis",
        "description": (
            "The Yamatetsu subsidiary that competes head to head with DocWagon for the Seattle high-threat- "
            "response medical market, and the corner of the Yamatetsu empire that stood to gain from SENSE. "
            "Yamatetsu's Seattle representatives worked out the play as soon as a leak about the scanner "
            "reached them: exclusive use of a portable neural scanner would let CrashCart pull customers away "
            "from DocWagon on response quality alone, and once CrashCart dominated the market Yamatetsu could "
            "licence SENSE back to DocWagon and the hospitals and generate even more nuyen a second time."
        ),
        "notes": (
            "Brainscan: never appears on stage. It is the corporate motive the clues are meant to point at -- "
            "'the clues will point to Yamatetsu or even DocWagon as the originators of the run' -- so that "
            "nobody looks at Deus. Also swamped along with DocWagon, Lone Star and Franklin Associates during "
            "the 48-hour blackout, when ambulances cannot get through the gridlock and have to rely on "
            "helicopters."
        ),
        "allies": ["Yamatetsu Corporation"],
        "enemies": ["DocWagon"],
    },
    {
        "name": "Sons of Sauron",
        "org_type": "policlub",
        "tier": 2,
        "headquarters": "Seattle",
        "summary": "Militant troll terrorist group whose bomb threat broke the Palace of China's decade-old 'No Troll' policy",
        "description": (
            "A terrorist group with a taste for the direct approach on behalf of trolls. The Palace of China in "
            "Tacoma held a 'No Troll' door policy for a decade until the Sons of Sauron phoned in a bomb threat "
            "over it; owner Dustin Kien lifted the ban in response to the radical demands, and the club has "
            "admitted anyone with enough nuyen ever since, though trolls still meet suspicious glances inside "
            "its walls. That is their only appearance in the campaign, and it is entirely typical of them: a "
            "threat, a concession, and a grudge that outlives both."
        ),
        "notes": (
            "Brainscan Pushing the Envelope (pp.19, 77): if the table wants a fight before the stealth runs, an "
            "irate Sons of Sauron troll queueing outside the Palace picks one with the runners who breeze past "
            "the line on Dixie's name, either before they go in or after they come out. The book asks the "
            "gamemaster not to wound anyone too badly -- the team is on a midnight deadline. The same encounter "
            "is offered again for the second Palace of China meet months later."
        ),
    },
    {
        "name": "Joint Task Force Seattle",
        "org_type": "government agency",
        "tier": 5,
        "headquarters": "The arcology cordon zone, Downtown Seattle; internment and debriefing camps at Fort Lewis",
        "summary": "The UCAS military command besieging the Renraku Arcology under Brigadier General Angela Colloton -- five floors reclaimed in a year, and pulled off the job by the blackout",
        "description": (
            "The UCAS military took the arcology crisis out of Renraku's hands, more concerned about the "
            "nuclear reactors in the basement than about rogue AIs, corporate politics, or the social cost of "
            "declaring downtown Seattle a war zone. Rescued civilians go by motorcade down Intercity 5 to a "
            "debriefing centre and internment camp at Fort Lewis for medical care and counselling; the troops "
            "have learned to be suspicious of everyone they pull out, including the children, because more than "
            "once they have 'rescued' people who were armed, booby-trapped or both."
        ),
        "leadership": [
            {"name": "Brigadier General Angela Colloton", "title": "Commanding officer, Operation: Excavation", "notes": "Took charge of reclaiming the arcology floor by floor."},
            {"name": "Lieutenant Krause", "title": "Platoon commander", "notes": "Pulled Steve Morris out of a 9th-floor elevator shaft. 'One bite at a time.'"},
        ],
        "notes": (
            "Stats pp.81-83: UCAS Army Grunt Soldiers (Prof 2, Colt M22A2 with underbarrel grenade launcher, HE "
            "and concussion mini-grenades, flare/low-light goggles), Cybered Soldiers (Prof 3, bone lacing, "
            "boosted reflexes 2, muscle replacement 2, smartlink), Army Mage (Manabolt 5, Mass Confusion 5, "
            "Stunbolt 5, Armor 5, a Force 4 elemental on call) and Army Rigger (VCR 2). The convoy on I-5 is a "
            "Citymaster with a gel-loaded turret MMG bracketed by two Ford Sentinels; reinforcements are two "
            "Northrup Yellowjackets. Afterwards the wave of refugees staggers the offensive into triage and "
            "transport; the military shuts down all but one basement reactor, blacking out most of the arcology "
            "and taking three-quarters of the SCIRE Matrix offline."
        ),
        "enemies": ["The Banded"],
    },
    {
        "name": "Renraku Red Samurai",
        "org_type": "corporate security division",
        "tier": 5,
        "headquarters": "Renraku facilities worldwide; the arcology cordon, and Renraku's Hong Kong and Chiba operations",
        "summary": "Renraku's elite security troops in red and black armor -- supporting the arcology siege, escorting Sherman Huang, and walking Cliber's cell out at the end",
        "description": (
            "Renraku's elite. They fight in red and black medium security armor with black plexiglas "
            "faceplates, communicate by headware radio, and are heavily wired: aluminium bone lacing, boosted "
            "reflexes 3, cybereyes with flare compensation and thermographic vision, smartgun links, SCK Model "
            "100s and Browning Max-Powers loaded with explosive ammunition. The book is blunt about their one "
            "reliable weakness: due to Renraku's pervasive racial prejudice, they will attack metahuman "
            "characters before humans."
        ),
        "notes": (
            "Stats pp.97-98 (Prof 4, Karate 7, Karma Pool 5, Small Unit Tactics 5, Renraku Structure 6). Two "
            "teams come to Madame Kim's simsense parlor, one inside with Huang and one on the street with the "
            "vehicles -- his Phaeton limousine and a Chrysler Patrol One. They are hard pressed defending "
            "against runners and a Banded hit team at once, and neither Huang nor Aneki can be risked in the "
            "crossfire, which makes Huang a usable hostage: none of the Red Samurai will fire near him. Vanessa "
            "Cliber survived the shutdown itself by taking refuge in a maintenance stairwell with a small group "
            "of unconverted Red Samurai, who became the core of her Renraku-loyal Resistance cell."
        ),
        "allies": ["Renraku Computer Systems"],
    },
    {
        "name": "The Netwalkers",
        "org_type": "otaku tribe",
        "tier": 1,
        "headquarters": "The Rox, Boston",
        "summary": "Boston otaku tribe whose initiation Renraku sent Michael Bishop to infiltrate -- and where Deus turned him into Babel",
        "description": (
            "An otaku tribe living in the Rox in Boston, notable in this campaign for one initiation. Renraku "
            "selected the covert-operations agent Michael Bishop, equipped him with advanced cyberware and sent "
            "him in to learn the tribe's secrets. Bishop underwent the Netwalkers' initiation and came out a "
            "genuine otaku -- but Deus interfered in the transformation, stole his memories of his former life "
            "and gave him the name Babel. The tribe itself never learns what it handed over. Everything Ronin "
            "is, and everything he later does to Deus, starts here."
        ),
        "notes": (
            "Brainscan p.133 (Ronin's background); the same pattern of Deus intervening in an otaku "
            "transformation is how the AI first learned to make otaku of its own. Sebastien came out of a "
            "different tribe, the one around the Nexus in Denver, and Pax led one in Atlanta."
        ),
    },
    {
        "name": "Reality Hackers",
        "org_type": "gang",
        "affiliation_contact_type": "Gang",
        "tier": 2,
        "headquarters": "The Seattle Barrens",
        "summary": "Barrens gang in its heyday when a Yakuza gang war orphaned Toshi Akimura and it taught him to sneak, steal and hack",
        "description": (
            "A Barrens gang that was in its heyday when a small orphaned boy joined it. Toshi Akimura lost his "
            "parents to a Yakuza gang war on the streets of Seattle and fell in with the Reality Hackers, who "
            "taught him how to sneak, how to steal and how to hack -- the skill set that carried him out of the "
            "Barrens into small-time shadowrunning, then into Cross Applied Technologies' Seraphim, then into "
            "the freelance shadows as Silk, and finally into Dunkelzahn's service and a career as one of North "
            "America's most influential fixers. The gang gets one sentence in the book and is responsible for "
            "the whole shape of a man's life."
        ),
        "notes": (
            "Brainscan p.72 (Toshi Akimura's background). No stats and no scene; a hook for a Seattle Barrens "
            "contact who remembers a small Eurasian kid with quick hands."
        ),
    },
    {
        "name": "New Orleans Mafia",
        "org_type": "criminal syndicate",
        "tier": 4,
        "headquarters": "New Orleans, CAS",
        "summary": "The syndicate that runs one of the world's most decadent cities -- vice, gambling, smuggling of every kind, and a great deal of wetwork",
        "description": (
            "The Mafia holds New Orleans, and holding New Orleans means holding vice, gambling, smuggling of "
            "all kinds and lots and lots of wetwork in a city built for all four. Toshi Akimura is one of the "
            "fixers with standing Mafia contacts, and when the Seraphim make the city too hot for him to meet "
            "the runners in person, the Mafia is the first of the four ways out he offers them. They certainly "
            "have the resources to fly a team back to Seattle on a private jet. What they will not do is "
            "protect anyone from Cross Applied Technologies or the Seraphim."
        ),
        "notes": (
            "Brainscan pp.65-66. Offered alongside Akimura's smuggler contacts (a Caribbean arms-hijack run "
            "traded for telesma and rum and escorted upriver to St. Louis), corporate contacts, the Draco "
            "Foundation and the krewes, the telesma-smuggling groups. Target: Smuggler Havens is cited for plot "
            "ideas. An 'olive oil business' front for a Mafia smuggling operation is also one of the Aftershock "
            "blackout encounters back in Seattle, with the runners caught between a mob and the Mob's army."
        ),
    },
    {
        "name": "New Orleans Police Services",
        "org_type": "police force",
        "tier": 3,
        "headquarters": "Station on Loyola Avenue near City Hall, New Orleans, CAS",
        "summary": "NOPS -- the New Orleans police: gruff, bought in places, and inclined to believe a licensed corporate security operative over a SINless stranger",
        "description": (
            "The city's police force, and one more reason the runners cannot afford a public scene in New "
            "Orleans. A Seraphim field agent tailing them is a corporate citizen and a licensed security "
            "operative; the runners are SINless criminals with no standing at all, and if it comes to a "
            "shouting match in the street NOPS will probably believe her. The department is also porous in the "
            "usual way: Toshi Akimura keeps a contact inside it, a gruff sergeant at the Loyola Avenue station "
            "near City Hall who is visibly unhappy about dealing openly with shadowrunners he does not know, "
            "and who hands over the information and the payment anyway."
        ),
        "notes": (
            "Brainscan pp.58-59, 64. Sergeant Crew is the named contact. The local BTL trade knows NOPS "
            "procedures well enough that both the Brain Disco's manager and its bouncer carry it as a knowledge "
            "skill. Whichever of Akimura's routes out of the city the runners pick, if they accept his help at "
            "all they are sent to Crew."
        ),
    },
    {
        "name": "Franklin Associates",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Seattle",
        "summary": "Seattle's fire control corporation -- overwhelmed along with every other emergency service during the 48-hour blackout",
        "description": (
            "The corporation that holds Seattle's fire-control contract. It exists in this book in order to be "
            "overwhelmed: when the grid dies and thousands of alarm systems fire at once across the metroplex, "
            "Franklin Associates goes under along with DocWagon, CrashCart and Lone Star, and the fires that "
            "start in looted shops and stalled traffic burn considerably longer than they should. Ambulances "
            "cannot get through the gridlock at all and fall back on helicopters to reach large parts of the "
            "city."
        ),
        "notes": (
            "Brainscan p.38 (Aftershock, Sweeping the Streets). One clause in the book; a useful name for any "
            "Seattle emergency-response scene."
        ),
    },
]

LOCATIONS = [
    {
        "name": "The Palace of China",
        "location_type": "nightclub",
        "district": "Tacoma",
        "security_level": "Patrolled / Commercial",
        "summary": "Medieval-Chinese theme club popular with Tacoma's young and wealthy; neutral ground in the Mafia-Yakuza war, and Steve Morris' meeting room both times he hires the runners",
        "description": (
            "A huge round building of red-lacquered wood with a green conical roof and dozens of ornate gold "
            "dragons intertwining into a massive arch above the front door -- their eyes look suspiciously like "
            "rubies and emeralds. Roving spotlights give the Palace a visual pop against the inky backdrop of "
            "Puget Sound; the parking lot is jammed with expensive sports cars and a long line of well-dressed "
            "young sararimen winds back from the golden doors. Tacoma is a hotbed of the ongoing struggle "
            "between the Yakuza and the Mafia, but the battles here have stayed subtle and the Palace has "
            "stayed neutral, which suits owner Dustin Kien fine -- he loses no profit to protection."
        ),
        "notes": (
            "Door scan: Chem Sniffer 4 plus Magnetic Anomaly Detector 6; anyone carrying is discreetly stopped "
            "and asked to stow it in the locked, guarded security storage area beside the main entrance. Six "
            "well-trained, lightly cybered bouncers (Company Man, SRComp p.75). A Force 6 FREE HEARTH SPIRIT "
            "calls the club home, appears as a fu-creature, has Spirit Energy equal to its Force and the powers "
            "Animal Form, Aura Masking, Dispelling, Personal Domain and Sorcery (MITS p.113) -- it handles "
            "anyone who causes trouble. The club's only recent scandal was a decade-old 'No Troll' policy "
            "lifted after a Sons of Sauron bomb threat; trolls still get suspicious glances. Morris meets here "
            "twice, months apart, both times behind the Dixie password: Light Meets Night at 5 p.m. and Outside "
            "Influence at 8 p.m."
        ),
    },
    {
        "name": "Gaeatronics Tacoma Substation",
        "location_type": "power plant",
        "district": "Eastern Tacoma, just off Highway 18",
        "security_level": "Low Security",
        "controlling_org": "Gaeatronics",
        "summary": "Unmanned concrete box on a wooded ridge where the runners plant the first half of the virus that kills Seattle's power -- with a Little League championship going on below the fence",
        "description": (
            "A curving road along a wooded ridge in the part of Tacoma that still feels almost rural: middle- "
            "income homes with the occasional above-ground pool, light commercial buildings, a smattering of "
            "trailer parks and long stretches of open land. The station is a small, windowless, off-white "
            "concrete block a few metres on a side, ringed by a four-metre chainlink fence tipped with rusty "
            "barbed wire, weeds twisting through it and half-hiding the NO TRESPASSING -- EXTREMELY HIGH "
            "VOLTAGE signs. Inside: a cheap particleboard desk with a grimy old cyberterminal, a duct-taped "
            "office chair and two massive banks of dials, readouts and gauges showing all green."
        ),
        "notes": (
            "Deserted as it looks: a Gaeatronics technician visits half an hour a day, and nobody else has any "
            "reason to be here. Fence Barrier 6, not electrified (the signs refer to the systems inside). Two "
            "sweeping corner cameras (one minute per arc) plus one fixed camera indoors -- unmonitored, but "
            "recorded to the computer for later review. Gate maglock Rating 5 with a Rating 2 anti-tampering "
            "system on a two-metre steel-pipe card reader; the gate swings open, pauses 15 seconds and closes. "
            "Door maglock Rating 3. Lone Star gives the area a B security rating (New Seattle p.110); a passive "
            "alert or a defeated tampering attempt places an automated call to the local precinct (Tap Commcall "
            "to detect, Make Commcall to stop). Host and sheaf in the prep doc."
        ),
    },
    {
        "name": "Romaine Marina",
        "location_type": "smugglers den",
        "district": "4529 S. Alaska St. at 54th, Lake Washington shore",
        "security_level": "Low Security",
        "summary": "Faded two-story boathouse on Lake Washington where Morris pays the runners, lends them two Nightrunners and points them at Council Island",
        "description": (
            "A large boathouse on the edge of Lake Washington: a two-story corrugated metal building with a "
            "faded 'Romaine Marina' sign tacked to it, at the end of a dark address downtown. The front gate is "
            "pulled open by a burly human in a suit that screams corp bodyguard and a second guard who could be "
            "his twin waves you inside. Two more stand near a dark blue Mitsubishi Nightsky, looking each "
            "arrival over -- a quick assessment of weapons and brawn -- before putting their eyes back on the "
            "entrance. Mr. Johnson stands on the dock between the boats, speaking quietly into his phone in "
            "Japanese while reading data off a portable computer, a row of certified credsticks lined up on a "
            "workbench behind him."
        ),
        "notes": (
            "The boats are Aztechnology Nightrunners, lent for the Council Island run; Morris will politely "
            "inform the team that they pay for any damage, and that part of the deal is non-negotiable. His "
            "four bodyguards are hired for the night from a freelance security company, know nothing about him "
            "or his plans, will guard him well and will not chat (Street Samurai template, SR3 p.76). The "
            "hushed Japanese call is Morris checking a haggled figure with his superior in Deus' organization; "
            "the players will conclude he is calling his boss at Shiawase. The team returns here after the "
            "second run for the balance, a hint that his employer may have more work, and the sight of Morris "
            "checking his watch and driving off into the night."
        ),
    },
    {
        "name": "Burbank Park (Council Island)",
        "location_type": "park",
        "district": "Northeastern tip of Council Island",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "Salish-Shidhe Council",
        "summary": "Qatuwas Festival grounds -- a giant bonfire from sundown to sunup, boats clustered offshore, and every marine patrol on Lake Washington concentrated around it",
        "description": (
            "About a kilometre east of the Council Island Inn, on the island's northeastern tip, where the "
            "annual Qatuwas Festival burns a bonfire big enough to light the sky over Lake Washington from "
            "sundown to sunup. The Seattle Qatuwas is one of a series of festivals held through the year all "
            "along the Pacific coast in Salish territory -- a ceremonial Salish-Shidhe event that these days is "
            "mostly a tribe-wide excuse to get drunk and party all night, and one of the very few occasions "
            "when non-natives get a legitimate chance to visit Council Island at all."
        ),
        "notes": (
            "Every Gaeatronics executive worth robbing is in town for it, which is why the target is at the Inn "
            "and out of his suite all night. The island's six Surfstar Marine Seacop patrol boats, three crew "
            "each, concentrate here, which leaves the water off the Inn comparatively clear; the security "
            "forces are also spread thin across the island by the festival's demands. Legwork (Tribal TN 4 / "
            "other Seattle TN 6): flyers are up, it runs for several nights, and it is the one time outsiders "
            "can get onto the island without official business."
        ),
    },
    {
        "name": "The Drowning Man",
        "location_type": "bar",
        "district": "Ravenna",
        "security_level": "Patrolled / Commercial",
        "summary": "Converted storefront pharmacy straddling the line between a big bar and a small club, where Monty Boudreaux takes meets in a soundproofed storeroom",
        "description": (
            "A converted storefront pharmacy in Ravenna that straddles the line between a large bar and a small "
            "nightclub; the heavy live music booming out of it leaves no doubt which it is tonight. The doorman "
            "hits arrivals for a cover charge, but the name Monty carries weight around here -- the burly "
            "guardian of the gate nods, steps aside and points to a small door beside the stage. Behind the "
            "door the ear-splitting throb cuts out into soundproofed silence: a storeroom holding a card table, "
            "three folding chairs and a single dusty light bulb swinging slightly from a black cord dropped "
            "through a hole in the ceiling."
        ),
        "notes": (
            "Monty's meet at 11:30 p.m.; he hands over a corporate ID mugshot of Wally Huggins, a sketch of the "
            "SENSE prototype, an address in the Redmond Barrens and a business card reading MONTY with a "
            "telecom number, and gives the team 24 hours. Pushing the Envelope: a domestic squabble erupts in "
            "the club with nobody willing to step in; power fluctuations in the sanitation system flush a small "
            "army of rats and devil rats up into the club; or a face from the runners' past that they did not "
            "want to see walks in. Debugging: unless the runners start a bar fight or attack Monty, nothing "
            "here can go wrong."
        ),
    },
    {
        "name": "The Adams Hotel",
        "location_type": "hotel",
        "district": "3327 Claremont at Roscoe, Woodinville, Redmond Barrens",
        "security_level": "No Security / Barrens",
        "summary": "'Deluxe transient accommodations' -- the flophouse where Wally Huggins hides, a block and a half from the garage where he stashed the SENSE",
        "description": (
            "Forty-five minutes through the littered streets of the Redmond Barrens brings you to the corner of "
            "Claremont and Roscoe in Woodinville, an exceptionally tough hood where the entire area is "
            "abandoned buildings occupied by squatters and gangers. The sign outside 3327 Claremont advertises "
            "deluxe transient accommodations; from the crumbling exterior and the stench of stale sweat and "
            "cigarettes wafting out of the front doorway, squatters probably have it better in the burned-out "
            "building next door. A quivering shell of a man in a soiled lab coat steps out of the entrance with "
            "a cigarette butt stuck in the corner of his mouth, shaking almost uncontrollably, and blurts: 'Are "
            "you the guys?'"
        ),
        "notes": (
            "Monty gives the team directions to the front door and nothing else -- the rest is up to Huggins, "
            "who leads them around the corner and a block down Roscoe to the parking garage. Play up his "
            "condition: the eyes, the smell of the clothes, the inability to pull the cigarette butt from his "
            "lips without trembling, the habit of pulling at the pale skin on his face. He is itching badly for "
            "a BTL fix and his judgement is clouded, but he will stay with the runners until the prototype is "
            "recovered or he dies -- they are his only hope of cashing in on his treachery."
        ),
    },
    {
        "name": "Woodinville Parking Garage (Rusted Stilettos Hideout)",
        "location_type": "gang territory",
        "district": "Roscoe Street, Woodinville, Redmond Barrens",
        "security_level": "No Security / Barrens",
        "controlling_org": "Rusted Stilettos",
        "summary": "Three-story concrete tomb where Huggins hid the SENSE, the Stilettos are cornered, the Nukes are dropping rockets on the ramps, and a city spirit is waiting on the third floor",
        "description": (
            "A three-story concrete box with a couple of two-lane car ramps winding down to the ground from the "
            "top level -- up close, more a decrepit tomb than a fallen monument to the practicality of urban "
            "developers. The rusted gate in front of the ramp has been twisted and bent open, three-foot weeds "
            "push up through the asphalt, and low moans echo from inside, or possibly that is just the wind. "
            "The first floor holds the five Stilettos who survived the ambush, two orks and three trolls in "
            "poor shape, one troll's right arm hanging useless from a mine and one ork barely conscious behind "
            "stacked crates in a corner with his right leg gone, moaning while his friends beg him to stay "
            "quiet. The third holds piles of rubble, a bloody corpse in a lab coat slumped against the wall, "
            "and nothing else."
        ),
        "notes": (
            "The Red Hot Nukes booby-trapped the lower floors while the Stilettos were out looting; the gang "
            "triggered most of them but a few remain, mostly AP offensive charges [10S (f), -1/m], "
            "Concealability 8, on tripwires (CC p.42). Ten Nukes are outside: six with Grinder about twenty "
            "metres off, setting up heavy weapons and cheerfully rocketing liquor bottles into the ramps, and "
            "four scattered around the building watching for escapees. Anything that comes out of the garage "
            "catches a rocket. On the third floor, after Huggins finds the SENSE gone, Brisbie's Force 6 city "
            "spirit materializes as a ghostly apparition rising out of Doss' corpse -- and Huggins, who "
            "murdered him, shoots himself, throws himself out of the building, or drops dead of a heart attack. "
            "The spirit then names Brisbie, gives directions to 2842 Fletcher Street two blocks away, and adds "
            "a whimsical 'no funny stuff'."
        ),
    },
    {
        "name": "Municipal Courthouse -- District 214",
        "location_type": "ruins",
        "district": "2842 Fletcher Street, Redmond Barrens",
        "security_level": "No Security / Barrens",
        "summary": "Abandoned four-story courthouse where Brisbie's ally spirit haggles from the rooftop; the end of the line, where the despair is thick enough to be parody",
        "description": (
            "A sign on the front of the four-story abandoned building still reads 'Municipal Courthouse -- "
            "District 214'. From a second-floor window a malnourished troll well into the latter half of his "
            "life stares vacantly into the street below. A dog howls somewhere inside, a mingled call of pain "
            "and hunger. The despair in the air is suffocating -- laid on, the book says, so thick that it "
            "almost becomes parody. Then a chipper voice slices down through the melancholy from on high: "
            "'What'll ya give for de case?' Brisbie himself watches the whole exchange from a sixth-story "
            "window in the building across the street, and does all his dealing through the telepathic link, "
            "for safety's sake."
        ),
        "notes": (
            "The bargain: base price 500 nuyen for the case, but Brisbie does not want anything as simple as "
            "money -- exotic food he cannot get in the Barrens, electronic gadgets of any sort, secrets, rumors "
            "about major events in Seattle, or juicy details of the runners' personal lives (the more reluctant "
            "they are to part with something, the more he wants to hear it). No trinkets or shiny objects "
            "despite his totem, no interest in weapons or armor. He may accept a favor owed. Then the case "
            "clangs down, pops open, and is empty: 'what will you offer me for the gizmo that was in the case?' "
            "-- another 1,000 nuyen of goods, a favor from each runner, or information twice as interesting as "
            "the first offer. Attack the spirit and Brisbie harasses the team with spells while it escapes, and "
            "a chase over the rooftops of Redmond is what the runners get instead of the prototype."
        ),
    },
    {
        "name": "The Bijou",
        "location_type": "theater",
        "district": "Seattle",
        "security_level": "Low Security",
        "summary": "Century-old projection movie house with pink bulbs on its vertical sign, where Brisbie uses a Control Emotions spell to lure the team in and sell them the real SENSE",
        "description": (
            "The facade is in decent shape for a building over a hundred years old. Large, bright pink bulbs "
            "form the theater's name on a vertical sign hanging out over the sidewalk, lighting up half a block "
            "of otherwise dark street and producing an eerie hum; the marquee is showing a classic, An American "
            "Werewolf In London. The heady aroma of fresh popcorn drifts through propped-open, gold-edged "
            "double doors into the cool black cinema, though the concession stand is unmanned and appears to be "
            "out of popcorn entirely. A pimply-faced teenage elf in an oversized maroon vest and black bow tie "
            "stands alert at the ticket window and squeaks in your general direction: 'Welcome to the Bijou. I "
            "love you all so much, it's free admission for the whole lot of you. Enjoy the show ... hope you're "
            "not jittery.' Inside the single theater: sticky floors, creaky uncomfortable seats, the musty "
            "smell of mildew, and two patrons."
        ),
        "notes": (
            "A surreal interlude with no real danger, played like a dream sequence in a horror film. Brisbie "
            "has cast Control Emotions on the most weak-willed runner to draw the team in and Control Thoughts "
            "on the usher, who will only stare ahead repeating 'Enjoy the show' and 'Would you like butter with "
            "that?'; both spells are potent because Mustard is assisting from the projection booth. Brisbie "
            "sells the working SENSE prototype cheaply -- he cannot figure out how it works and has taken a "
            "liking to the team -- and Mustard delivers it in the lobby from behind the concession stand along "
            "with a box of heavily buttered popcorn. If the runners harmed Brisbie in Breakthrough he never "
            "comes here at all and sells the unit on the black market, where Overwatch snaps it up."
        ),
    },
    {
        "name": "Neuranalysis Headquarters",
        "location_type": "research lab",
        "district": "Bellevue",
        "security_level": "Corporate Standard",
        "controlling_org": "Neuranalysis, Inc.",
        "summary": "The burned-out shell of the medical research company that built SENSE -- two guards shot in the back of the head, the labs torched, and very little of the company left",
        "description": (
            "A small independent research facility in Bellevue, and by the time anyone comes looking, a crime "
            "scene twice over. Wally Huggins and Regis P. Doss walked in before the brownout, put two bullets "
            "each into the backs of the two security guards' heads, took the SENSE prototype case and the "
            "design specs and left. With nothing better to do, and in the spirit of the big blackout a short "
            "time earlier, they stole some equipment and set Neuranalysis on fire."
        ),
        "notes": (
            "The runners never visit it on stage; it is the hole in the middle of Breakthrough. Legwork "
            "(Corporate contacts, TN 4) turns up the fire, the destroyed computers and the fact that there is "
            "really very little of the company left, plus rumors that Yamatetsu had been planning a purchase a "
            "few weeks earlier. The company logo etched on the lapel of Huggins' lab coat in his mugshot "
            "identifies him on one success of a Corporate Knowledge (6) Test."
        ),
    },
    {
        "name": "The Brain Disco",
        "location_type": "btl den",
        "city": "New Orleans",
        "district": "Lakefront",
        "security_level": "No Security / Barrens",
        "summary": "Coffin hotel and BTL parlor on the New Orleans lakefront where Remy Duchamps is cooking his brain in coffin #310 with Poison Lily's chip still in his pocket",
        "description": (
            "A combination coffin hotel and BTL parlor along the lakefront where patrons rent small cubicles "
            "and get smashed for as long as their credit holds out. The interior is one large open room banked "
            "by steel scaffolding, catwalks running to five levels of stacked rows of coffins, fluorescent "
            "lighting flickering overhead and cheap disco music spewing out of crackling speakers. Its logo -- "
            "a metahuman brain with lightning bolts shooting from it -- turns up printed on burned-out chips in "
            "the pockets and on the bedroom floors of its regulars, and means nothing to anyone who is not "
            "local. Neither cares in the slightest what anyone does here so long as the equipment survives and "
            "the other patrons are not disturbed."
        ),
        "notes": (
            "100 nuyen buys Remy's coffin number out of Stumpy -- #310, third floor -- and a Computer (4) Test "
            "into the house system shows he has been in two days with eight days still on his account. He "
            "cannot resist anything: unplugged, he does whatever the runners want in return for not being hurt "
            "and hands over the chip. The Seraphim raid follows if Juliet Sienna overheard enough at the doss "
            "-- a commotion downstairs as Bubba tries to stop them, silenced gunshots (Perception (6) to hear "
            "over the noise), then agents up both stairwells, one per runner. Pushing the Envelope makes the "
            "place a Tamanous organlegging front, possibly with a Petro Voodoo cult, ghouls in the empty "
            "coffins and a Seraphim gunship overhead."
        ),
    },
    {
        "name": "Poison Lily's Doss",
        "location_type": "apartment complex",
        "city": "New Orleans",
        "district": "Just outside the French Quarter",
        "security_level": "Low Security",
        "summary": "Third-floor apartment in a decaying southern gothic house, ransacked by the Seraphim with a passkey and watched from across the street with a laser microphone",
        "description": (
            "The last known address of the decker Poison Lily and her boyfriend Remy Duchamps: a small third- "
            "floor apartment in a decaying southern gothic house outside the French Quarter. The Seraphim have "
            "been through it -- drawers pulled out and dumped on the floor, furniture and mattress overturned, "
            "wall-hangings torn down to check behind them -- but even under the mess it is clear neither tenant "
            "was fastidious. The sink is piled with dirty dishes and discarded food containers wearing several "
            "days' growth of mold, and the place reeks of cigarette smoke, cheap synthahol and less pleasant "
            "things. The layout is simple: a common area with a tiny kitchen, a small bedroom and a bathroom "
            "with a shower stall. The front door has a maglock; the Seraphim used a passkey and left no sign of "
            "forced entry."
        ),
        "notes": (
            "Search on Intelligence (4): several burned-out BTL chips on the bedroom floor, no datachip. Chips "
            "bearing the Brain Disco logo are the lead. Usable ritual material -- hair in the shower, toenail "
            "clippings by the bed -- may belong to Lily rather than Remy. The apartment manager is Marguerite, "
            "an old Creole woman who swears a lot in French; 100 nuyen keeps her quiet. Juliet Sienna watches "
            "from an apartment across the street with a laser microphone and surveillance gear and can see and "
            "hear virtually everything the runners say and find, then tails them out. Other routes to Remy: "
            "Street Etiquette (5) accumulating 15 successes across the team, Computer (6) against his credit "
            "report, ritual sorcery on the traces, or a nature spirit's Search power (which can only establish "
            "that he is not outside)."
        ),
    },
    {
        "name": "Queen of Babylon",
        "location_type": "corporate yacht",
        "city": "New Orleans",
        "district": "The Mississippi River, downriver from St. Louis",
        "security_level": "Corporate High Security",
        "controlling_org": "Cross Applied Technologies, Inc.",
        "summary": "Fifteen-metre Cross Applied Technologies hydrofoil yacht carrying Dr. Olivia Marchand, her grandmother, nine security personnel and a Seraphim agent posing as a deckhand",
        "description": (
            "A fifteen-metre yacht owned by Cross Applied Technologies, hydrofoil-capable and fitted with "
            "state-of-the-art sensor, navigation and computer technology; the corp uses her as an executive "
            "ferry, an informal meeting site and a corporate pleasure craft, with a crew of under a dozen, all "
            "company men security-checked within an inch of their lives. The flying bridge carries a full set "
            "of spare controls behind a waist-high wall and a concealed swivel mount with an Ingram Valiant "
            "light machine gun that can be brought into action in one Combat Turn. Below decks: galley, crew "
            "cabins, engine room, and four guest cabins -- Marchand and Flora to starboard, Gabriel to port, "
            "nine security forward, and Captain Vincent Larreau in the bow."
        ),
        "notes": (
            "Handling 3, Speed 60(30), Accel 5, Hull 4, Bulwark 4, Sig 3/4, Autonav 4, Sensor 4, Sonar 3, "
            "Accommodation 35. Outriders: two Samuvani Criscraft Otters cruising near either shore, three crew "
            "each (a vehicle rigger and two Weapons Specialists with AK-97s). Three of the nine security are on "
            "duty at any time. Approach options: by boat (the outriders will spot almost anything, so taking an "
            "outrider is better), underwater with SCUBA or a water spirit's Guard power (Open Stealth to climb "
            "aboard), by air with ultralights or parachutes under magical concealment, or by bluff and hacked "
            "records. Host and sheaf in the prep doc. Overwatch's own play lands mid-run: a smart-frame "
            "overrides the autonav, the Queen goes to hydrofoil and runs for a cove where six Overwatch-hired "
            "mercenaries are waiting, and Cross security assumes the runners and the mercenaries are the same "
            "team."
        ),
    },
    {
        "name": "Tulane University Book Store",
        "location_type": "shop",
        "city": "New Orleans",
        "district": "Tulane University",
        "security_level": "Patrolled / Commercial",
        "summary": "Akimura's clean drop for runners who would rather cut the link -- ask for Clara and quote the passphrase about the graduate economics course",
        "description": (
            "A campus bookstore, and the option Toshi Akimura offers runners who decide they would rather not "
            "touch him again once the Seraphim are all over his agents. Go in, ask for Clara, and say you want "
            "books for the graduate level economic course. She will ask 'What teacher?' The answer is 'My "
            "teacher is life.' She hands over a package containing credsticks with the team's money and a "
            "Seattle telecom number, with a handwritten note reading: 'Call this number when you hit Seattle.' "
            "No conversation, no meeting, and no further contact with Akimura until the job is finished."
        ),
        "notes": (
            "The alternative to the NOPS route through Sergeant Crew. Either way Akimura pays half now and half "
            "on delivery in Seattle. Clara herself never appears again and the book gives her no stats; she is "
            "a clean drop and a good recurring one for a New Orleans campaign."
        ),
    },
    {
        "name": "NOPS Loyola Avenue Station",
        "location_type": "police station",
        "city": "New Orleans",
        "district": "Loyola Avenue, near City Hall",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "New Orleans Police Services",
        "summary": "The police station where Akimura's bought sergeant hands over information, payment and a Seattle number, and makes no secret of hating it",
        "description": (
            "The New Orleans Police Services station on Loyola Avenue near City Hall, and the single strangest "
            "place a team on the run from a megacorporation's black-ops division will walk into voluntarily. "
            "Ask for Sergeant Crew. Whichever of Akimura's four routes out of the city the runners say they "
            "want -- Mafia, smugglers, corporate or the favors and markers he can call in -- they are always "
            "sent to Crew, who is gruff and obviously not pleased to be dealing openly with shadowrunners he "
            "does not know, and who gives them whatever information they need along with their payment and a "
            "number to call when they get back to Seattle."
        ),
        "notes": (
            "Akimura's police contact is his own asset, not a departmental arrangement, and he does not explain "
            "the relationship. Crew has no stats. NOPS will believe a Seraphim agent's corporate credentials "
            "over the runners' word, so this is the one police building in the adventure where the team has "
            "cover -- and only for as long as Crew's patience lasts."
        ),
    },
    {
        "name": "Intercity 5 at the Tacoma Docks",
        "location_type": "transportation hub",
        "district": "Tacoma docks",
        "security_level": "Patrolled / Commercial",
        "summary": "Ambush site Overwatch scouted long ago: the stretch of I-5 furthest from both Fort Lewis and the arcology cordon, with side streets to vanish into",
        "description": (
            "The stretch of Intercity 5 where the highway crosses the Tacoma docks -- midway between the "
            "arcology military base and Fort Lewis, which maximizes the time it takes backup to arrive, and the "
            "best terrain on the route for getting away. A metre-high concrete barrier (Barrier 16) separates "
            "the southbound lanes from the northbound, and a second set of barriers plus a stretch of grass "
            "separates the highway from the side streets of Tacoma. Exits lie half a kilometre away to both "
            "north and south. The streets around the docks are tight and cramped, full of alleys, backroads and "
            "empty warehouses, and enterprising runners can get up onto the roofs of the warehouses overlooking "
            "the ambush site. Overwatch scouted this piece of road long ago, anticipating exactly this."
        ),
        "notes": (
            "The ambush: an otaku girl's voice on the radio counts the convoy in ('Red Rover one half kilometre "
            "from intercept. Grid team, go bumpercars'), three GridGuide-hijacked southbound cars converge, "
            "collide and skid to a halt blocking both lanes, and the jammer cuts the radio to static. Only the "
            "shoulders stay open. The motorcade -- a Citymaster bracketed by two Ford Sentinels -- tries the "
            "shoulder first, then reverse; the soldiers fight from inside the Sentinels through armored windows "
            "(Barrier 8) while the rigger works the turret MMG with gel rounds. Citymaster doors need Moderate "
            "damage or a hotwired Rating 5 maglock keypad. Once shooting starts a bystander eventually gets a "
            "call through: Lone Star, plus two Northrup Yellowjackets. Ronin has hacked a dock foghorn and "
            "sounds it when backup is on the way."
        ),
    },
    {
        "name": "Choco-Tarts Factory (Overwatch HQ)",
        "location_type": "corporate facility",
        "district": "180 Forest Ridge Drive, Auburn",
        "security_level": "Low Security",
        "controlling_org": "Overwatch",
        "summary": "Automated chocolate factory whose emptied, soundproofed vat is Overwatch's war room -- the building Steve Morris hires the runners to level while they are standing in it",
        "description": (
            "A rundown manufacturing district, and a functioning automated chocolate factory with a Choco-Tarts "
            "sign beside the entrance. The parking lot gate slides open on approach, security cameras track "
            "visitors around to the loading bay, and the door buzzes and swings wide on an overwhelming smell "
            "of chocolate and a cleaning drone that blinks a red LED and then rolls away, still blinking, as an "
            "escort. A hatch pops open in its side, and inside the emptied, soundproofed vat is a war room: "
            "computers crammed around the walls against maps of Seattle and the Renraku Arcology, cables strewn "
            "across the floor like carpet, at least a dozen children hunched in small chairs with fiberoptic "
            "lines streaming from the datajacks in their temples, and Choco-Tart wrappers everywhere."
        ),
        "notes": (
            "The otaku seized the factory's computers easily and chose it for its Matrix bandwidth and for "
            "being entirely automated; the pipes that once pumped chocolate into the secondary vat now carry an "
            "array of Matrix connections, with half a dozen satellite uplinks on the roof and a dozen nearby "
            "jackpoints used for anything hard, so the HQ itself is never traced. They have improved the "
            "plant's programming enough that the company's techs almost never come by, and when they do, "
            "everyone locks into the vat. Added sensors feed the vat directly and the drones are programmed to "
            "interfere with physical intruders; the site has no astral security whatsoever. Fifteen or more "
            "otaku work here at any time besides Ronin and Dodger. Evacuating the essentials takes half an hour "
            "-- just long enough to walk into the arriving Blues."
        ),
    },
    {
        "name": "Overwatch Redmond Safehouse",
        "location_type": "safehouse",
        "district": "The Barrens",
        "security_level": "No Security / Barrens",
        "controlling_org": "Overwatch",
        "summary": "Derelict games-software offices where Ronin meets the runners face to face -- wired for the net, empty for half a decade, and good enough for a group of Matrix activists",
        "description": (
            "An old brick-front office building like many others in the Barrens, once home to a company that "
            "made computer and online games until it lost everything in the Computer Crash. The parking lot is "
            "choked with weeds and grass, the facade crumbles and is pitted by acid rain, most of the glass is "
            "gone from the metal door frames and the shards crunch underfoot. A back conference room holds a "
            "wooden table recently dusted and looking out of place, half a dozen people around it, most of them "
            "children with eyes far too mature for their faces."
        ),
        "notes": (
            "Ronin meets arrivals in the lobby with discreet hired security in the corners -- low-rent local "
            "gang toughs (Mercenary, SR3 p.72) -- and leads them down to the basement where Dodger is finishing "
            "business in the Matrix. This is where Revelations lands and where the runners are asked to hit the "
            "convoy pro bono. Pushing the Envelope: a minor gang squabble, traffic accident or road rage on the "
            "way in, or squatters and ghouls scoping the building as shelter; the book asks the gamemaster to "
            "avoid hospitalizing anyone, since there is a job on."
        ),
    },
    {
        "name": "Overwatch Bellevue House",
        "location_type": "safehouse",
        "district": "Bellevue",
        "security_level": "Low Security",
        "controlling_org": "Overwatch",
        "summary": "Secluded red brick house Overwatch moved into after the chocolate factory was blown -- luxurious, and looking like twenty children were left in it unsupervised for months",
        "description": (
            "A secluded two-story red brick house in Bellevue, nondescript from the street, with security "
            "cameras following every step from the curb to the door. The door swings wide on a house that could "
            "be described as luxurious if it did not look as though some neglectful parents had left their "
            "twenty kids alone in it while they went on vacation for several months. Piles of carry-out food "
            "boxes compete for floorspace with heaped computers and other electronics, and fiberoptic cables "
            "threaten to ensnare your feet on the way to the dining room, where a cluster of young otaku unjack "
            "themselves and crowd around any arrival. Ronin and Dodger appear, greeting the runners and smiling "
            "warmly. 'Welcome to our new headquarters.'"
        ),
        "notes": (
            "Where the Aneki plan is laid out: the Ork Underground route into the parking structure, the few "
            "days of preparation before the UCAS offensive starts, and the point of no return. The otaku work "
            "hard on the runners here -- some thank individual characters privately for their bravery, some of "
            "the younger ones treat them as role models or heroes and follow them around, mimicking them in "
            "small ways. Ronin coordinates with the zealotry of a warrior facing an honorable and necessary "
            "battle; Dodger plays the gallant hero before a quest and withdraws to spend time with Megaera, and "
            "will introduce her to any runner who asks. Meanwhile Renraku is closing in outside -- ritual "
            "astral tracking first, then legwork, shaken-down contacts, spies flooding the streets, and a "
            "bounty."
        ),
    },
    {
        "name": "Tin Man Scrap Works Yard",
        "location_type": "corporate facility",
        "district": "Hell's Kitchen, Puyallup Barrens",
        "security_level": "Corporate High Security",
        "controlling_org": "Tin Man Scrap Works",
        "summary": "Toxic scrapyard, retooled drone plant and converted office building at the edge of Hell's Kitchen -- Deus' operations centre outside the arcology",
        "description": (
            "Past an electrified outer gate with a peeling Tin Man Scrap Works sign lies a maze of junked "
            "automobiles, large appliances, metal chassis and scrap heaps five to ten metres high, with piles "
            "of engines and I-beams waiting to be melted and crushed cubes stacked like children's playthings "
            "-- where old refrigerators, generators and construction drones come to die. Inside the plant: "
            "automated machines linked by a maze of conveyor belts, laborers with green cybereyes at some "
            "stations, half-starved metahumans in rags chained to the others, and a rear wall of drone racks -- "
            "an army waiting to be animated."
        ),
        "notes": (
            "Junk walls: Athletics (Climbing) (6), failure means a Quickness (8) Test or resist 9M off the "
            "sharp rusty scrap (half Impact applies), and they give +4 to Stealth (Hiding). Cube walls are TN 9 "
            "with no hiding bonus. The compactor is a square pit, remotely triggered from the magnet cranes or "
            "by the SK, five Combat Turns to crush, and anything inside dies with no roll; the smelters are "
            "five-metre vats fed by ceiling magnets, and anything that falls in is instantly destroyed. Work "
            "drones (DLK Mk 6 Utility Machines, Kodiaks) run on Pilot until a VCR-2 Blue rigger takes the "
            "Rating 7 remote deck in the security office; scrap drones modelled on the Medusa lie dormant among "
            "the piles."
        ),
    },
    {
        "name": "Tin Man Office Building",
        "location_type": "corporate facility",
        "district": "Hell's Kitchen, Puyallup Barrens",
        "security_level": "Corporate High Security",
        "controlling_org": "Tin Man Scrap Works",
        "summary": "The old scrapyard headquarters turned Banded operations centre: security room, conversion clinic, bunk room, work room, Hiroshi Ushida's office, and a fuel-air bomb under a table",
        "description": (
            "Doors unlocked, because anyone approaching the back one draws the attention of the barghests "
            "kennelled beside it. The first-floor security office is manned at all times by two Blues watching "
            "the gate and plant camera feeds and talking to the patrol, with a remote control deck hardwired "
            "into the security panel for reprogramming the drones. Upstairs, the Director's Office is Hiroshi "
            "Ushida's personal domain, shared only with his bodyguard, with a sliding glass door onto the roof."
        ),
        "notes": (
            "The work room is the prize: computers, maps and chips, plus evidence tying the yard to other "
            "mysteriously owned businesses -- programming firms, chip manufacturers, medical clinics, sim- "
            "arcades, Matrix broadcasters -- with equipment invoices, financial transactions and files on "
            "individuals from corporate executives to city officials to shadowrunners. It is also where Deus "
            "keeps its insurance: a 200-kilogram Rating 6 fuel-air explosive under an entire worktable, wired "
            "into the host, detonated by the SK on a five-minute countdown if the site is about to fall or "
            "Hiroshi is killed, and primed if the SK is destroyed (12D within 24 metres). The computer room "
            "holds the mainframes and the SK, plus a bunk shared by two young White otaku who have served Deus "
            "since before the shutdown, never entered the arcology, show no sign of being Banded, and will "
            "claim to be kidnap victims if threatened."
        ),
    },
    {
        "name": "Madame Kim's Simsense Parlor",
        "location_type": "btl den",
        "city": "Hong Kong",
        "district": "Wan Chai",
        "security_level": "Low Security",
        "summary": "Seedy Wan Chai sim parlor between a biosculptor and a clinic, whose back door opens onto the hidden garden where the Tibetans hand Inazo Aneki over",
        "description": (
            "On the edge of the bustling Wan Chai district, away from the bright lights of the mainstream "
            "entertainment, on a less reputable-looking street nestled between Kwok Biosculpting and the Liu "
            "Clinic. Given the services rendered inside, Madame Kim avoids the neon and glitz. The place is "
            "open all hours, sells non-mainstream legal and quasi-legal sims at inflated prices to a seedy "
            "clientele and will let a BTL be viewed for the right price, and at any given time about twenty "
            "clients are present, almost all of them slack-jawed and oblivious to the world."
        ),
        "notes": (
            "Security is a video camera outside the locked front door; Madame Kim buzzes people in from the "
            "counter and her husband works on sim equipment in the back room, doubling as a bouncer with a "
            "Defiance T-250 shotgun to hand. Anyone who asks for Aneki or introduces themselves as a Renraku "
            "representative is greeted and walked through the parlor to the back door and told to go through "
            "into the garden. If shooting starts Madame Kim takes cover and hides, her husband grabs the gun "
            "and covers her, and most of the clients never notice anything is amiss. The runners get less than "
            "twenty minutes between Ronin's call and Renraku's arrival to scout the place and make a plan."
        ),
    },
    {
        "name": "The Wan Chai Garden Shrine",
        "location_type": "landmark / monument",
        "city": "Hong Kong",
        "district": "Wan Chai (behind Madame Kim's Simsense Parlor)",
        "security_level": "Low Security",
        "summary": "Secret Tantric Buddhist shrine hidden in a courtyard behind a sim parlor, under a Force 10 ward and a quickened illusion of a sunny mountainside",
        "description": (
            "A door in Madame Kim's back room opens onto a square garden surrounded on all four sides by "
            "buildings, and totally out of place with everything around it. The pleasant smell of freshly "
            "trimmed hedges and flower patches washes over you, complemented by running water from a small "
            "fountain set near a shrine. You suspect magic is at work, because you cannot hear the noisy hum of "
            "the city and the only thing visible over the walls is cloudy blue sky; if you did not know better "
            "you would suspect you were not in the Sprawl at all. Two men in black robes stand patiently near "
            "him, and one walks humbly over with exquisite grace and composure: 'Despite appearances, his state "
            "is much improved ... he is at peace and ready to leave with you.'"
        ),
        "notes": (
            "A secret Tantric Buddhist shrine, well tended by a group of local worshippers and protected by a "
            "Force 10 ward that makes astral intrusion unlikely; inside the ward a quickened Force 6 Phantasm "
            "creates the sunny mountainside beyond the walls. Several doorways lead from the garden into the "
            "surrounding buildings and businesses, giving the runners escape routes if they get trapped. The "
            "two monks are Grade 4 initiated adepts whose mission is to hand Aneki to whoever comes for him "
            "first, and who will protect his life at all costs, sacrificing themselves if necessary. The scene "
            "can play as the runners arriving first and posing as Renraku, or as an ambush on Huang leaving "
            "with the prize; either way Huang must end up somewhere he can be kidnapped too, because the Banded "
            "hit team wants him as target number two."
        ),
    },
    {
        "name": "Durruti's",
        "location_type": "bar",
        "district": "199th floor, Renraku Arcology (SCIRE), Downtown",
        "security_level": "No Security / Barrens",
        "controlling_org": "The Arcology Resistance",
        "summary": "Derelict bar in a dead entertainment district two hundred floors up, where Kiell Rauglos and Devon Eurich plan the assault on Deus over a trideo projector",
        "description": (
            "The 199th floor was once an entertainment district serving the surrounding residential units. Now "
            "the restaurants stand empty and the arcades are dark, and haggard Resistance guards -- who do not "
            "look like street-hardened gun-toting types, but whose fatalistic expressions say everything about "
            "their determination -- escort visitors past them to a derelict-looking bar called Durruti's. The "
            "cell has scoured the whole district clean of surveillance devices. Inside is a circular bar with a "
            "trideo projector built into it, which throws up a three-dimensional image of the arcology and "
            "zooms in on the floors that matter, sections outlined in red and the centre of one of them "
            "conspicuously empty. Two of the fighters recognize Inazo Aneki on sight and glare at him with open "
            "animosity."
        ),
        "notes": (
            "The cell is Kiell Rauglos, Devon Eurich and four other fighters. Devon and Dodger are old "
            "acquaintances and greet each other warmly; Devon's disgust at seeing Aneki is plain enough to make "
            "the runners wonder whether bringing him this far was a good idea, and Kiell steps between them: "
            "'Since we've all gathered here, let's get down to business and figure out how we're going to "
            "unplug this damn AI already.' These are people who have seen more than any metahuman should and "
            "can pass hours with stories of the shutdown. Ask about Cliber and you are told she leads another "
            "cell nearby, that Dodger and Devon both loathe her and believe her loyalties are still Renraku's, "
            "and that the rest of the Resistance considers her redeemed."
        ),
    },
    {
        "name": "Arcology 272nd Floor (White Domain)",
        "location_type": "corporate arcology",
        "district": "Renraku Arcology (SCIRE), Downtown",
        "security_level": "Zero Zone -- Lethal Response",
        "controlling_org": "The Banded",
        "summary": "The Whites' luxury domain high in the arcology: executive suites, a pool, an opera hall, a Noh theatre, a wild golf course, devil rats in the tennis courts, and Cham Lam Won",
        "description": (
            "A corner of the arcology given over to high-lifestyle entertainment and now occupied by Deus' "
            "otaku. The executive suites are huge and spacious, outer walls built entirely of one-way "
            "transparent plasteel (Barrier 12), doors on Rating 5 maglocks requiring a fingerprint and a "
            "passcode, and emergency fire doors with Rating 5 alarms connecting each suite to its neighbours; "
            "most of the Whites who live in them are in their rooms, jacked in and oblivious. An Olympic-sized "
            "indoor pool is still well maintained, though Cham Lam Won is the only one who uses it, and one of "
            "its walls is transparent from the inside over Seattle. A small herd of devil rats nests in the "
            "tennis courts, which were used as a pen for residents when the arcology first shut down."
        ),
        "notes": (
            "Background Count 2, like the rest of the arcology's perverted astral space. Getting here means "
            "past the 261st floor, the lower level of White housing, which is well guarded physically and "
            "electronically with a few Blue magicians keeping areas warded and astrally patrolled. Cham is in "
            "his suite with the Mousetrap and no guards, but Tadashi Marushige is paying a routine check-up "
            "visit under direct orders from Deus while two Blues tear the suite apart looking for contraband "
            "and check his screamer. Backup: a squad of dervishes across the golf course, then Blues down the "
            "elevators. Jamming the screamer silences it; removing it takes an electronics kit and Electronics "
            "B/R (8) at a base time of two hours, and either attempt automatically tells SCIRE security where "
            "the device last was."
        ),
    },
    {
        "name": "Arcology Valve Station and Mainframes (Floors 201-202)",
        "location_type": "corporate arcology",
        "district": "Renraku Arcology (SCIRE), Downtown",
        "security_level": "Zero Zone -- Lethal Response",
        "controlling_org": "The Banded",
        "summary": "Where the campaign ends: an atmosphere control station on 201, a zombie room full of jacked-in children next door, and the SCIRE mainframes on 202 behind an unbreathable floor",
        "description": (
            "Deus protects the 202nd floor by having removed its breathable atmosphere and replaced it with "
            "different gases in different locations, most of them lethal -- mostly halon, with sealed areas of "
            "pressurized vacuum, Neuro-stun VIII, Green Ring-3 and compounds identified only by serial numbers. "
            "The valve station that controls it sits on the 201st floor near an outer wall: a circular room "
            "ringed on all sides by computer workstations, gauges, digital displays and manual controls, behind "
            "a Rating 4 passcode maglock, guarded only by a single Medusa or a pair of Spiders because Deus "
            "does not normally allow metahumans or Banded in here at all. One door leads to a hallway of "
            "engineering and maintenance workstations where half a dozen Greens are always working. Many show "
            "signs of recent surgery."
        ),
        "notes": (
            "Atmosphere: Electronics (8), Chemistry (4) or Engineering (5) reads the contents of any area; "
            "Electronics (Control Systems) (6) sets a new mixture, and failure means the wrong gas; a change "
            "takes about an hour to drain and filter. Kiell or Sebastien can jack into local controls and "
            "succeed automatically if needed. The ZOMBIE ROOM's occupants are prepared 'hosts' for Deus' "
            "download -- each already transformed into an otaku, minds imprisoned in a UV host waiting for "
            "fragments of the AI's code to be installed in their brains. On 202 the mainframe room is floor-to- "
            "ceiling supercomputers behind layers of maglocks (doors Barrier 8); Devon opens the access panel "
            "of a Xeno-Cray labelled GRENDEL PROJECT CCR-235, still directly connected to the Wall, and the "
            "deckers jack straight in while Jack and Zendra hotwire the doors permanently shut and stand by "
            "with freeze foam."
        ),
    },
    {
        "name": "Naval Shipyards Lot (Everett)",
        "location_type": "corporate facility",
        "district": "Near the Naval Shipyards, Everett",
        "security_level": "Low Security",
        "summary": "Empty fenced parking lot at the north end of the sprawl where Steve Morris waits an hour's drive away for the Blues to confirm a massacre he ordered",
        "description": (
            "A simple fenced-in parking lot not far from the Naval Shipyards at the north end of the Seattle "
            "sprawl, deliberately chosen to be out of the way and roughly an hour's drive from the chocolate "
            "factory -- long enough for a squad of Blues to verify that the job was done as instructed. The lot "
            "is empty except for Morris' Mitsubishi Nightsky limousine and four rented security goons with "
            "HK227-S submachine guns and armored jackets: one standing outside the car, one in the back with "
            "Morris, and two in front including the rigger. As the runners arrive, Morris calls up the Blues "
            "for a report. He will not pay a nuyen until he hears the Overwatch hideout is rubble, and he gets "
            "uneasy when nobody answers."
        ),
        "notes": (
            "The guards (Weapons Specialist and Vehicle Rigger, SR3 pp.79-80) have Professional 3 and Karma "
            "Pool 2 and will get Morris out of the area; the rigger will leave the outside guard behind if he "
            "has to. Morris will not fight, will flee on foot if the vehicles are blocked, and will kill "
            "himself if escape looks impossible. Interrogating him takes a -4 Open Test modifier because of "
            "Deus' conditioning; success gives up Tin Man Scrap Works. If it fails, the location is in his "
            "headware memory, programmed into the Nightsky's autonav, or printed as the billing address for the "
            "rented guards on an invoice in his pocket. He also carries several certified credsticks holding "
            "the rest of the fee. Deus eventually notices he is taken and triggers his radio-detonated cranial "
            "bomb over a citywide repeater network, at whatever moment will disturb the runners most."
        ),
    },
    {
        "name": "Hell's Kitchen (Puyallup)",
        "location_type": "ruins",
        "district": "Puyallup Barrens",
        "security_level": "No Security / Barrens",
        "summary": "Toxic geyser-and-smelter district of the Puyallup Barrens that even squatters avoid, and the reason a scrapyard could be turned into a Banded fortress unnoticed",
        "description": (
            "The stretch of the Puyallup Barrens that industry chose precisely because nobody lives there and "
            "nobody enforces pollution control. The air is thick with steam off nearby geysers and the "
            "sulfurous exhaust of smelters, everything is rusted and soot-caked, and the local astral space has "
            "soured into a toxic domain where the only spirits that can be drawn from the earth are toxic ones "
            "-- enough to give shamans a chill and make even mages uncomfortable. Squatters live on its edges "
            "and avoid its heart; those who do come too close to Tin Man Scrap Works get kidnapped, chained to "
            "a machine and eventually walked through a clinic. The rumor among the ones who are left is that "
            "too many people have disappeared around there, and half of them are convinced the place is a bug "
            "spirit hive."
        ),
        "notes": (
            "Brainscan pp.86-89. Background Count 2 within the scrapyard itself; nature spirits and spirits of "
            "the elements cannot be conjured in the yard at all. The district is the cover story that made "
            "Deus' shell-company purchase work: a loud, environmentally damaging business in a place where a "
            "loud, environmentally damaging business is nobody's problem."
        ),
    },
]

NPCS = [
    {
        "name": "Steve Morris",
        "role": "The Johnson for Light Meets Night and Outside Influence -- a rescued Renraku executive rebuilt into an undetectable Green Banded who does not know who he works for",
        "archetype": "Corporate Johnson",
        "title": "Renraku executive; Green chameleon of the Banded",
        "race": "Human",
        "gender": "Male",
        "organization": "The Banded",
        "connection": 3,
        "description": (
            "A fit, thirtyish Anglo male in a gray pinstriped business suit, professional, unflappable and "
            "entirely at ease with macho posturing and haggling: 'My name isn't Johnson, but let's pretend it "
            "is.' The runners meet him first in a back room of the Palace of China, where a Perception (6) Test "
            "spots gold circular cufflinks with two smaller circles faintly inscribed on them, and a Corporate "
            "Knowledge (4) Test makes them the Shiawase logo."
        ),
        "background": (
            "A Renraku executive who brokered more than a few shadowruns for the corp in his day, and who was "
            "working late in the arcology the night Deus seized it. He passed basic physical and psychological "
            "exams and was allowed back to his normal life; Renraku put him back at his desk and is keeping him "
            "away from sensitive data until they are convinced he is his old suit-and-tie self, which the book "
            "says will never happen."
        ),
        "notes": (
            "Stats p.132 (OCR garbles the attribute row): Karma/Prof 2/2; Etiquette 5, Negotiation 6, Pistols "
            "3, Car 2; Knowledge Renraku 5, Rental Thugs 4, Seattle Shadows 4, Shiawase 2; alphaware datajack "
            "and 300 Mp headware memory; secure clothing; Fichetti Security 500 with an EX explosive clip; "
            "portable computer (500 Mp). Normal in every way until a select command code reaches him by telecom "
            "or Matrix, whereupon he takes orders from Deus and afterwards assumes it was all business as "
            "usual; he does not consciously know why he obeys. Captured, he is worth Tin Man Scrap Works at a "
            "-4 Open Test modifier -- and then Deus fires his cranial bomb."
        ),
        "contact_skills": ["Seattle shadow work: discreet infiltration and no-trace jobs", "Renraku corporate small talk"],
    },
    {
        "name": "Ace Gonriled",
        "role": "Hulking ork decker whose team died smashing the Council Island border post, found finishing the job alone in Bungalow 5 -- and unwilling to give it up",
        "archetype": "Decker",
        "title": "Team leader, the first (botched) Council Island team",
        "race": "Ork",
        "gender": "Male",
        "connection": 2,
        "description": (
            "A hulking ork decker, angst-ridden and on edge, clicking away at a portable computer on a small "
            "wood desk in the corner of a stranger's hotel bungalow with a silenced Ceska Black Scorpion "
            "machine pistol within reach. Quickly, or they'll have to carry you out in a spoon!'"
        ),
        "background": (
            "Hired by Morris for the same night's work as the runners, Ace took his team at Council Island the "
            "hard way, was stopped at the West Council Drive border station, panicked and tried to blast his "
            "way out. The van burned; the entire team was killed or captured except him. He phoned Morris for "
            "backup, was told to cut his losses and get out, and Morris assumes he went home. Instead he "
            "crossed onto the island alone with his copy of the payload and started the download."
        ),
        "notes": (
            "Use the Combat Decker sample character (SR3 p.66). Three reactions: guns drawn and he fires on the "
            "first person through the door; guns holstered and he draws and orders everyone down, firing at the "
            "lead runner if they hesitate; talked to through the door or by magic and he hides behind the bed "
            "and waits. He almost always has the drop initially, and the download he was running has to be "
            "restarted from the beginning. Kept alive and brought along, he gets paid the same as the runners; "
            "killed and left on Council Island, his body is found and costs the team the quiet-run bonus."
        ),
        "contact_skills": ["Decking and hotel/host infiltration", "Who else in the sprawl is bidding on the same job"],
    },
    {
        "name": "Dustin Kien",
        "role": "Owner of the Palace of China, neutral in the Tacoma mob war and paying no protection to either side",
        "archetype": "Club Owner",
        "title": "Owner, the Palace of China (Tacoma)",
        "gender": "Male",
        "connection": 2,
        "description": (
            "The owner of Tacoma's most fashionable theme club, and a man whose whole business strategy is "
            "refusing to pick a side. His one public reversal was the club's decade-old 'No Troll' policy, "
            "which he dropped in response to a Sons of Sauron bomb threat."
        ),
        "notes": (
            "No stats. Runs a door scan of Chem Sniffer 4 and Magnetic Anomaly Detector 6 with a locked, "
            "guarded security storage area for confiscated weapons, six lightly cybered bouncers, and a Force 6 "
            "free hearth spirit that lives in the club and deals with troublemakers. Anyone with enough nuyen "
            "can party at the Palace now, though trolls still meet suspicious glances inside. A useful Tacoma "
            "contact: a club owner who has stayed alive and unaligned in the middle of a syndicate war and who "
            "lets both sides drink under the same roof."
        ),
        "contact_skills": ["Tacoma nightlife and who is drinking with whom", "Keeping a neutral house in a syndicate war"],
    },
    {
        "name": "Tommy",
        "role": "Eight-year-old with a melting snow cone who comes to the substation fence for a foul ball at the worst possible moment",
        "archetype": "Child",
        "title": "Little League spectator, east Tacoma",
        "race": "Human",
        "gender": "Male",
        "age": 8,
        "connection": 1,
        "description": (
            "A tough little human kid, wise beyond his years and not remotely intimidated by adults, with a "
            "snow cone melting all over his hand and dripping onto his shoes. The book notes he has the "
            "potential to grow into a mean-spirited toady for a bigger kid."
        ),
        "notes": (
            "Stats p.21 (attribute row OCR-garbled): B2 Q4 C3 W3 E6, Init 3+1D6, Combat Pool 5, Karma/Prof 1/1; "
            "Athletics 3, Stealth 3, Throwing Weapons 2 (Rocks 3), Unarmed Combat 2 (Biting 3); Knowledge "
            "Baseball 3, Candy 5, Comic Books 3; Brawling 2. The whole encounter exists so that the runners "
            "feel caught and have to talk their way out of it peacefully."
        ),
    },
    {
        "name": "Monty Boudreaux",
        "role": "Freelance fixer who fronts corporate Johnsons for a commission; hired by Morris to destroy SENSE, and now hiring the runners to clean up his own mess",
        "archetype": "Fixer",
        "title": "Freelance fixer, Seattle ('full-time fixer to the stars')",
        "race": "Elf",
        "gender": "Male",
        "age": 33,
        "connection": 4,
        "description": (
            "A lanky elf with long wavy black hair and dark brown eyes that point in slightly different "
            "directions -- talking to him, he looks you in the left eye and the right ear. Soft, scratchy voice "
            "on the phone and not the chatty type; direct and no-nonsense in person, laying out facts, making a "
            "deal and leaving. 'After you've located the device, I could care less what happens to Huggins.'"
        ),
        "background": (
            "A former shadowrunner turned freelance go-between for corporate executives who do not want to hire "
            "runners directly: he takes a budget and the job specification, finds the team, conducts the meet, "
            "picks up the pieces and keeps whatever is left of the budget as commission. When Huggins came back "
            "demanding 500,000, Monty agreed to the deal fully intending to put a bullet in his brain, and then "
            "Huggins called back to say he could not get to the prototype."
        ),
        "notes": (
            "Stats p.49: B5 Q7 S5 C4 I6 W6 E6 M7 R6(8), Karma/Prof 4/4; Athletics 4, Aura Reading 4, Edged "
            "Weapons 6(9), Etiquette 5, Negotiation 5, Pistols 5, Pole Arms/Staffs 4, Stealth 5(7); ADEPT, "
            "Initiate Grade 1 (Masking), with Astral Perception, Combat Sense 2, Improved Ability (Edged "
            "Weapons 3, Stealth 2) and Improved Reflexes 1; secure long coat, Browning Max-Power with APDS, "
            "Dikoted survival knife, and a Dikoted katana when he expects trouble. He has not run in years and "
            "is still dangerous if crossed. Deliver and the team goes on his list; fail and he says they will "
            "never work in this town again."
        ),
        "contact_skills": ["Fronting corporate Johnsons who want deniability", "Barrens jobs and the fixers who broker them"],
    },
    {
        "name": "Wally Huggins",
        "role": "BTL-addicted Neuranalysis tech who sold out SENSE, murdered his partner over the split, and leads the runners to a prototype that is no longer there",
        "archetype": "Corporate Technician",
        "title": "Technical Engineer II, Neuranalysis, Inc. (Bellevue)",
        "race": "Human",
        "gender": "Male",
        "age": 38,
        "organization": "Neuranalysis, Inc.",
        "connection": 1,
        "description": (
            "A quivering shell of a man in a soiled lab coat with a cigarette butt stuck in the corner of his "
            "mouth, shaking almost uncontrollably: the corporate ID mugshot shows a human in his late thirties "
            "with glasses and a worn, drawn face, and it is readily apparent that he does not have it all "
            "together. 'We're fragged.'"
        ),
        "background": (
            "The disgruntled employee mold fits him like a glove. Deus' otaku raided the Neuranalysis host, "
            "pulled the company roster and picked him out by elimination as the low-level tech with a habit; "
            "Monty found him at a favorite simsense parlor at 2 a.m. on a Friday and bought everything he knew "
            "for 20,000 nuyen."
        ),
        "notes": (
            "Stats p.50: B4 Q3 S3 C3 I5 W4 E6 R4, Combat Pool 6 (for dodging), Karma/Prof 1/1; Car 3, Computer "
            "5, Electronics 5, Etiquette 3 (Corp 4), Negotiation 2; Knowledge Medicine 3, Popular Music 3, BTL "
            "Houses 5. Coached by Monty to say only 'I was responsible for the initial extraction' and to play "
            "it cool; he will not admit the double-cross or the murder in case the runners get ideas. He is "
            "committed all the way and will stay with them until the prototype is recovered or he dies. Matrix "
            "Research (6): 38, lives in Newport, Bellevue, Neuranalysis since February 2060, unmarried, no "
            "record, frequent patron of disreputable BTL parlors."
        ),
    },
    {
        "name": "Regis P. Doss",
        "role": "Neuranalysis tech and weapons enthusiast drowning in gambling debts who helped steal SENSE and took three bullets in the chest over the split",
        "archetype": "Corporate Technician",
        "title": "Low-level technician, Neuranalysis, Inc.",
        "race": "Human",
        "gender": "Male",
        "organization": "Neuranalysis, Inc.",
        "connection": 1,
        "description": (
            "The runners meet him as a bloody corpse slumped against a wall on the third floor of a Redmond "
            "parking garage: a man who looks to have been in his late thirties, dressed like Huggins in a lab "
            "coat over civilian clothes, a full beard, thick glasses still stuck perfectly on his face, and "
            "several messy bullet holes in a red-smeared chest."
        ),
        "background": (
            "Recruited by Wally Huggins to help steal the SENSE prototype and everything that went with it. The "
            "two of them entered the Neuranalysis facility before the brownout, put two bullets each into the "
            "backs of the security guards' heads, swiped the prototypes and the design specs and headed off to "
            "hide the score in an abandoned parking garage the Rusted Stilettos used as a hideout."
        ),
        "notes": (
            "No stats; he is a body and a lever. Brisbie watched the murder astrally from the roof and has "
            "decided to have some fun with the killer, so his Force 6 city spirit materializes as a ghostly "
            "apparition rising out of Doss' corpse -- optionally accusing Huggins of murdering him, or simply "
            "grinning and saying 'I'm back' -- which is enough to push an already teetering man over the edge. "
            "The same corpse is the confirmation the runners need that the story Monty and Huggins told them is "
            "not the whole one."
        ),
    },
    {
        "name": "Grinder",
        "role": "Dwarf adept leader of the Red Hot Nukes, gleefully rocketing liquor bottles into the Stilettos' garage and grooming his gang to prevent a horrible future",
        "archetype": "Physical Adept",
        "title": "Leader, the Red Hot Nukes",
        "race": "Dwarf",
        "gender": "Male",
        "nationality": "UCAS",
        "organization": "Red Hot Nukes",
        "connection": 3,
        "description": (
            "An African-American dwarf adept, generally in a jovial mood unless somebody challenges his "
            "authority and gets in his face, in which case they had better duck. For divining he lights a "
            "firecracker, tosses it in the air and reads the pattern of the remains."
        ),
        "background": (
            "He organized the Red Hot Nukes after retiring from a short shadowrunning career, and he did it for "
            "a deep, dark, secret reason: he claims that on an anti-megacorp run a few years back he discovered "
            "a horrible future event, and he is grooming the Nukes to prevent it. He has never said what it is."
        ),
        "notes": (
            "Stats p.49: B6 Q5 S7 C4 I6 E6 M10 R5(9), Init 5(9)+1D6(3D6), Combat Pool 9, Karma/Prof 6/4; "
            "Demolitions 7, Heavy Weapons 6, Launch Weapons 6, Throwing Weapons 6, Leadership 5, Meditation 6, "
            "Centering 6, Sortilage 4, Divining 4, Electronics 6, Intimidation 5, Pistols 5, Clubs 5; Improved "
            "Reflexes 2, Iron Will 2, Mystic Armor 2, Quick Draw, Pain Resistance 7; Initiate Grade 4 "
            "(Centering via Meditation, Divining via Sortilage); armor jacket, Ares Predator with EX explosive, "
            "ArmTech MGL-G with 6 white phosphorous, 6 incendiary and 10 AP offensive grenades, crowbar."
        ),
        "contact_skills": ["Demolitions, mines and improvised explosives", "Redmond Barrens gang politics"],
    },
    {
        "name": "Slammin' Sammy",
        "role": "Red Hot Nukes adept with an Aztechnology Lasher missile launcher and three anti-personnel rockets",
        "archetype": "Physical Adept",
        "title": "Red Hot Nukes adept",
        "race": "Dwarf",
        "gender": "Male",
        "organization": "Red Hot Nukes",
        "connection": 2,
        "description": (
            "One of the two Kung Fu adepts in Grinder's core group, and the reason the Stilettos' garage has a "
            "hole in its ramp: he is the dwarf who drops to one knee, whips an Aztechnology Lasher onto his "
            "shoulder, lines up on a bottle spinning through the air and puts the rocket through it and into "
            "the concrete behind."
        ),
        "notes": (
            "Stats p.49-50: B5 Q5 S6 C5 I6 W4 E6 M? R5, Init 5+1D6, Combat Pool 7, Karma/Prof 3/3; Demolitions "
            "6, Heavy Weapons 5, Launch Weapons 5, Electronics 5, Intimidation 4, Throwing Weapons 4, Unarmed "
            "Combat 4 (Fist 6); Kung Fu 5 (Focus Strength, Vicious Blow); shared adept powers Smashing Blow, "
            "Free Fall 4, Improved Senses (Improved Taste, Sound Dampening), Quick Draw, Pain Resistance 3, "
            "Rooting 4, plus Iron Will 1 and Missile Parry of his own; armor jacket, Aztechnology Lasher with 3 "
            "AP rockets (16D, -1/.5m) and an Ares Predator with explosive ammunition."
        ),
    },
    {
        "name": "Portnoy",
        "role": "Red Hot Nukes adept and grenade quartermaster -- ten white phosphorous, ten incendiary, fifteen AP offensive, and an aluminum bat",
        "archetype": "Physical Adept",
        "title": "Red Hot Nukes adept",
        "race": "Dwarf",
        "gender": "Male",
        "organization": "Red Hot Nukes",
        "connection": 2,
        "description": (
            "Slammin' Sammy's counterpart in Grinder's core group: the same Kung Fu training, the same shared "
            "adept powers, and a walking arsenal of grenades instead of a missile launcher. Where Sammy plays "
            "to the crowd with rockets, Portnoy is the one who keeps the fire coming when a fight goes long, "
            "and the one carrying an aluminum bat for when it goes close."
        ),
        "notes": (
            "Stats p.49-50: as Slammin' Sammy (B5 Q5 S6 C5 I6 W4 E6, Init 5+1D6, Combat Pool 7, Karma/Prof 3/3, "
            "Kung Fu 5, Smashing Blow, Free Fall 4, Improved Senses, Quick Draw, Pain Resistance 3, Rooting 4) "
            "with Rapid Healing 2 and Temperature Tolerance 2 in place of Iron Will and Missile Parry. Carries "
            "10 white phosphorous grenades [14M/10L, -1/m], 10 incendiary and 15 AP offensive [10S (f), -1/m] "
            "plus an aluminum bat [7M Stun, +1 Reach], and wears an armor jacket. He is the obvious first "
            "target for anyone who wants the Nukes' firepower reduced, and the obvious worst target for anyone "
            "standing close to him."
        ),
    },
    {
        "name": "Lady Fingers",
        "role": "Red Hot Nukes adept with an RPK heavy machine gun and explosive ammunition; Grade 2 initiate with mystic armor and astral perception",
        "archetype": "Physical Adept",
        "title": "Red Hot Nukes adept",
        "race": "Dwarf",
        "gender": "Female",
        "organization": "Red Hot Nukes",
        "connection": 2,
        "description": (
            "The heaviest gun in the gang, and one of the two Nukes adepts who can see the astral. She and Flo "
            "are Grade 2 initiates who share a package of powers -- astral perception, quick draw, mystic armor "
            "and rooting -- that makes them considerably harder to put down than the rank and file, and Lady "
            "Fingers carries an RPK heavy machine gun with two spare drums of explosive ammunition to hold "
            "whatever ground Grinder tells her to hold."
        ),
        "notes": (
            "Stats p.50: B5 Q5 S6 C3 I6 W5 E6 M8 R5, Init 5+1D6, Combat Pool 8, Karma/Prof 4/3; Demolitions 6, "
            "Heavy Weapons 5, Launch Weapons 5, Electronics 5, Shotguns 4, Throwing Weapons 5, Leadership 3, "
            "Intimidation 4; Initiate Grade 2; shared powers Astral Perception, Quick Draw, Mystic Armor 4, "
            "Pain Resistance 3, Rooting 4, plus Enhanced Perception 2; armor jacket with mystic armor [5/7]; "
            "RPK HMG [10S, 40 (c) with two spare clips of explosive]. Her astral perception is the reason a "
            "magically concealed approach to the garage is not automatically safe."
        ),
    },
    {
        "name": "Flo",
        "role": "Red Hot Nukes adept with a Remington 990 loaded with Big D's Temper shells; Grade 2 initiate and the gang's sensory specialist",
        "archetype": "Physical Adept",
        "title": "Red Hot Nukes adept",
        "race": "Dwarf",
        "gender": "Female",
        "organization": "Red Hot Nukes",
        "connection": 2,
        "description": (
            "Lady Fingers' opposite number: the same Grade 2 initiation and the same shared package of astral "
            "perception, quick draw, mystic armor and rooting, but built for close work and for noticing "
            "things. Her improved senses cover direction sense, flare compensation, improved taste and sound "
            "dampening, which between them make her hard to blind, hard to deafen and hard to lose in a "
            "scrapheap at night, and she carries a Remington 990 with ten spare rounds and ten Big D's Temper "
            "shells."
        ),
        "notes": (
            "Stats p.50: as Lady Fingers (B5 Q5 S6 C3 I6 W5 E6 M8 R5, Init 5+1D6, Combat Pool 8, Karma/Prof "
            "4/3, Initiate Grade 2, Astral Perception, Quick Draw, Mystic Armor 4, Pain Resistance 3, Rooting "
            "4) with Improved Senses (Direction Sense, Flare Compensation, Improved Taste, Sound Dampening) in "
            "place of Enhanced Perception; armor jacket with mystic armor [5/7]; Remington 990 [10S] and an "
            "aluminum bat. Grinder keeps out of the fray barking orders like a field general and falls back if "
            "five Nukes go down, which means Flo and Lady Fingers are usually the last two still shooting."
        ),
    },
    {
        "name": "Brisbie",
        "role": "Raven gutter shaman who lifted the SENSE case out of the garage for fun, sells the runners a decoy, and later sells them the real thing out of a movie theater",
        "archetype": "Shaman",
        "title": "Raven street shaman, Redmond Barrens",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "A rail-thin street shaman with long, black, stringy hair and a suede jacket festooned with "
            "feathers, crystals and bones. Born and raised in the Barrens and the quintessential gutter shaman: "
            "he survives by scrounging, minor crime and selling his services to local gangs, he has no home at "
            "all and prefers to sleep on rooftops under the open sky, and he has few friends and equally few "
            "enemies."
        ),
        "background": (
            "His involvement is purely chance. The Rusted Stilettos hired him to provide astral protection over "
            "their garage, and from the rooftops he watched Wally Huggins stash the prototype case and shoot "
            "Regis Doss. Only he knows the case holds two devices, a working prototype and a pretty decoy."
        ),
        "notes": (
            "Stats p.50: B4 Q5 C7 W6 E6 M6 R5, Astral Init 25+1D6, Combat Pool 8, Astral Combat 9, Karma/Prof "
            "3/4; Aura Reading 5, Conjuring 7 (Summoning 8), Sorcery 6, Negotiation 5, Electronics 5, Stealth "
            "5, Athletics 3; Knowledge The Barrens 6, Bird Knowledge 4, Cooking 4 (Sandwiches 6), Redmond Gangs "
            "5, Riddles 4, Scrounging 5; RAVEN (+2 dice manipulation spells and sky spirits, +1 to magical TNs "
            "when not under open sky); spells Analyze Device 4, Analyze Truth 4, Clout 5, Control Emotions 6, "
            "Control Thoughts 6, Heal 4, Levitate 4, Magic Fingers 5, Mask 4, Mass Confusion 6, Mist 3, Night "
            "Vision 3, Shadow 4, Stench 4, Stunball 4; real leather jacket."
        ),
        "contact_skills": ["Redmond Barrens street and gang gossip", "Conjuring, spirits and cheap astral security"],
    },
    {
        "name": "Mustard",
        "role": "Brisbie's ally spirit and partner in crime, named after his favorite condiment; does all the shaman's talking and all his stealing",
        "archetype": "Ally Spirit",
        "title": "Ally spirit of Brisbie",
        "race": "Ally spirit",
        "gender": "Male",
        "connection": 2,
        "description": (
            "Named after Brisbie's favorite condiment and infused with the same dark humor as his summoner, "
            "Mustard enjoys sowing chaos and confusion for its own sake. It is Mustard who calls down from the "
            "courthouse rooftop -- 'What'll ya give for de case?' -- and Mustard who conducts the entire "
            "negotiation while Brisbie watches through the telepathic link from a sixth-story window across the "
            "street."
        ),
        "notes": (
            "Stats p.50: B6 Q5 S5 W6 R5, Init 15+1D6, Astral Init 25+1D6, Combat Pool 8, Astral Combat 7, "
            "Karma/Prof 3/4; Electronics 3, Negotiation 5, Sorcery 6, Stealth 5; powers Aid Power, "
            "Materialization, Sorcery, Sense Link, Telepathic Link, Three-Dimensional Movement; spells Heal 4, "
            "Control Thoughts 6, Magic Fingers 5, Mass Confusion 6, Stench 4. DISCREPANCY: p.47 calls him a "
            "Force 6 ally spirit, the Cast of Shadows on p.50 says he is Force 5."
        ),
    },
    {
        "name": "Poison Lily",
        "role": "Akimura's decker, hired to hack Cross Tech for the Marchand file and killed by the Seraphim before the runners ever meet her",
        "archetype": "Decker",
        "title": "Freelance decker, New Orleans",
        "gender": "Female",
        "connection": 2,
        "description": (
            "The team's briefing packet was supposed to be her work: the yacht's exact location, its length of "
            "stay, its security measures. Her doss is a filthy third-floor apartment full of burned-out BTL "
            "chips, which says most of what the book means the runners to conclude about her last few months."
        ),
        "notes": (
            "No stats -- she is dead before the adventure begins and she is the hole the whole New Orleans act "
            "has to be run around. The chip is still physically in Remy's pocket at the Brain Disco, since he "
            "only uploaded the data. The Seraphim entered her apartment with a maglock passkey and left no sign "
            "of forced entry, and Juliet Sienna has been sitting across the street with a laser microphone ever "
            "since, waiting for whoever comes looking next."
        ),
    },
    {
        "name": "Remy Duchamps",
        "role": "Poison Lily's boyfriend, a BTL burnout who sold her data to a stranger over the Matrix and is cooking his brain in a coffin hotel with the chip still on him",
        "archetype": "BTL Addict",
        "title": "Boyfriend of the decker Poison Lily",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": (
            "Somewhere in the back of his mind he plans to sell the data to a second buyer. Unplug his datajack "
            "and he will do whatever the runners want as long as they promise not to hurt him, and he hands "
            "over the chip with no resistance at all; leave him plugged in and he simply lies on the padded "
            "floor of coffin #310, staring into space and mumbling to himself, lost in the virtual pleasure of "
            "the simsense feed."
        ),
        "background": (
            "Lily gave him her datachip for safekeeping. Shortly afterwards an unknown buyer contacted him over "
            "the Matrix and bought the data off it -- that was Dodger of Overwatch, though Remy has no idea. "
            "Flush with Dodger's nuyen, he checked into the Brain Disco and started working through the popular "
            "new BTL programs. He has been there two days and has eight more paid for."
        ),
        "notes": (
            "Stats p.60: B2 (one point lost to BTL addiction) Q3 S3 C3 I3 W3, Init 3+1D6, Combat Pool 4, "
            "Karma/Prof 1/1; Bike 2, Computers 3, Edged Weapons 2, Electronics 3, Electronics B/R 2; Knowledge "
            "New Orleans BTL Parlors 3; chipjack and datajack; credstick, a pocketful of BTL chips, Poison "
            "Lily's optical chip and a knife. He is in no position to offer any resistance to anybody. Akimura "
            "will simply phone the location in if the team stalls."
        ),
    },
    {
        "name": "Marguerite",
        "role": "Creole apartment manager who swears in French, hates both her missing tenants, and will forget the runners for a hundred nuyen",
        "archetype": "Landlord",
        "title": "Apartment manager, Poison Lily's building",
        "race": "Human",
        "gender": "Female",
        "nationality": "CAS (Creole)",
        "connection": 1,
        "description": (
            "An old Creole woman who swears a lot in French, calls Remy a bum and Lily a cheap whore, and those "
            "are the nice things she has to say about them. She is not, however, deaf or stupid, and she has "
            "watched a rather better-dressed group of people come and go through the same door recently without "
            "damaging the lock."
        ),
        "notes": (
            "No stats. Useful as the one person in the building who will talk, and as an unwitting warning that "
            "the Seraphim got there first. Any team that spends money on her rather than time on her misses the "
            "chance to ask about the previous visitors."
        ),
        "contact_skills": ["Who has been coming and going in a decaying French Quarter rooming house"],
    },
    {
        "name": "Juliet Sienna",
        "role": "Seraphim field agent running surveillance on Poison Lily's doss, photographing the runners and tailing them to the Brain Disco",
        "archetype": "Corporate Agent",
        "title": "Field agent, the Seraphim (Cross Applied Technologies)",
        "race": "Human",
        "gender": "Female",
        "organization": "The Seraphim",
        "connection": 3,
        "description": (
            "A corporate citizen and a licensed security operative, sitting in an apartment across the street "
            "from a dead decker's flat with a laser microphone and surveillance gear, seeing and hearing "
            "virtually everything that happens inside it. She has no interest at all in a confrontation she "
            "does not control."
        ),
        "notes": (
            "Detection: an Open Stealth Test for her against secret Perception Tests for each player. Detect "
            "Enemies will NOT find her, because she does not yet intend the runners any direct harm. If they "
            "make a public scene, remember that she is a corporate citizen with credentials and they are "
            "SINless criminals -- NOPS will believe her. Whatever she overhears at the doss determines whether "
            "the Seraphim hit the Brain Disco, and anything the Seraphim learn, Gabriel knows. Use any "
            "appropriate SR3 sample character, adjusted to human."
        ),
    },
    {
        "name": "Bubba",
        "role": "Cajun troll bouncer at the Brain Disco with a baseball bat, shot by silenced Seraphim guns on the ground floor",
        "archetype": "Bouncer",
        "title": "Security, the Brain Disco (New Orleans)",
        "race": "Troll",
        "gender": "Male",
        "nationality": "CAS (Cajun)",
        "connection": 1,
        "description": (
            "A big Cajun troll in a stained and torn 'New Orleans Magic' T-shirt, armed with a baseball bat and "
            "a complete lack of interest in anyone else's business. He is also the only person in the building "
            "who will try to stop armed strangers coming through the front door, which is what gets him shot."
        ),
        "notes": (
            "Stats p.60: B8(9) Q3 C2 I2 W3 E6 R2, Init 2+1D6, Combat Pool 4, Karma/Prof 2/2; Clubs 4, Etiquette "
            "1 (Street 3), Intimidation 4 (Physical 5), Negotiation 2; Knowledge New Orleans Criminal "
            "Syndicates 2, NOPS Procedures 4, Smuggling 4; baseball bat [12M Stun, +1 (+2) Reach]. The "
            "commotion of him trying to stop the Seraphim, followed by silenced gunshots, is the runners' only "
            "warning that the raid is coming -- Perception (6) to hear it over the disco music and the general "
            "noise."
        ),
    },
    {
        "name": "Stumpy",
        "role": "Ferret-like dwarf manager of the Brain Disco who will sell a coffin number for a hundred nuyen",
        "archetype": "Fixer",
        "title": "Manager, the Brain Disco (New Orleans)",
        "race": "Dwarf",
        "gender": "Male",
        "connection": 2,
        "description": (
            "A ferret-like dwarf, so called by Bubba and apparently by everybody else. He runs a coffin hotel "
            "where the product is other people's brain damage, keeps the machines working and the accounts "
            "straight, and asks nothing of his guests except that they pay and that whoever comes looking for "
            "them does not smash anything on the way in."
        ),
        "notes": (
            "Stats p.60: B6 Q? S6 C3 I3 W4 E4.1, Init 2+1D6, Combat Pool 4, Karma/Prof 2/2; Computers 4, "
            "Electronics 5, Electronics B/R 5, Etiquette 1 (Street 3), Intimidation 2, Negotiation 2, Pistols "
            "2; Knowledge New Orleans BTL Parlors 5, NOPS Procedures 3, Smuggling 3; chipjack, datajack, 300 Mp "
            "memory, telephone; Ares Predator. The house system is trivial to hack -- Computer (4) -- and gives "
            "the same answer for free, along with how long the mark has left on his account. As a contact he is "
            "a working knowledge of every disreputable BTL parlor and smuggling route in New Orleans, for sale "
            "by the hundred."
        ),
        "contact_skills": ["New Orleans BTL parlors and who is holed up in them", "Local smuggling routes and NOPS procedure"],
    },
    {
        "name": "Captain Vincent Larreau",
        "role": "Older Creole captain of the Queen of Babylon, a New Orleans native who will fight to defend his ship",
        "archetype": "Rigger",
        "title": "Captain, the Queen of Babylon (Cross Applied Technologies)",
        "race": "Human",
        "gender": "Male",
        "nationality": "CAS (Creole)",
        "organization": "Cross Applied Technologies, Inc.",
        "connection": 2,
        "description": (
            "An older Creole man and a New Orleans native, running a corporate pleasure craft down the "
            "Mississippi from St. Louis for a corporation that checks its crews within an inch of their lives. "
            "He keeps the forward cabin, carries a Colt America L36 in a shoulder holster under his jacket, and "
            "will fight to defend the Queen -- which, given that his passenger list consists of one unstable "
            "computer scientist and her grandmother, is more loyalty than the situation strictly deserves."
        ),
        "notes": (
            "Use the Vehicle Rigger (SR3 p.79) with the cyberware dropped and the Rotor Craft skills changed to "
            "Ship skills. When Overwatch's smart-frame overrides the autonav and the Queen goes into hydrofoil "
            "mode toward the cove, he is the man trying to wrestle a fifteen-metre yacht back under control "
            "while an ambush closes from two directions. He is also the obvious person for a team that talks "
            "its way aboard to have to get past."
        ),
    },
    {
        "name": "Dr. Olivia Marchand",
        "role": "Cross Applied Technologies' distributed-decking genius, shattered by her own prototype into four people, one of whom arranged her extraction for Deus",
        "archetype": "Corporate Researcher",
        "title": "Lead designer, Project Legion, Cross Applied Technologies (Montreal)",
        "race": "Human",
        "gender": "Female",
        "nationality": "CAS (Creole, New Orleans)",
        "organization": "Cross Applied Technologies, Inc.",
        "connection": 3,
        "description": (
            "An attractive Creole woman in her mid-thirties with a broad face, coffee-colored skin and short "
            "wavy black hair, normally in casual business dress -- slacks and turtlenecks with a lab coat or "
            "blazer thrown on when she is working -- and a datajack visible behind her ear."
        ),
        "background": (
            "Born near New Orleans and raised in the full flower of the Voodoo renaissance; her grandmother "
            "made her a serviteur of the loa at a very young age, but magic frightened her and she went to the "
            "Matrix instead, using a cyberterminal as a small child and a brilliant decker and programmer by "
            "twelve."
        ),
        "notes": (
            "Stats p.70: Init 4+1D6, Combat Pool 6, Karma/Prof 2/2; Computer 6 (Software 8), Computer B/R 5, "
            "Electronics 5, Electronics B/R 5, Etiquette 2 (Corporate 4), Car 1; Knowledge Decker Legends 3, "
            "French 3, Matrix 6, New Orleans 4, Voodoo Lore 2; armor clothing, alphaware datajack, 150 Mp, "
            "telephone, Walther Palm Pistol, pocket secretary. The neural overload fractured her into four; the "
            "core personality is unaware of the others and experiences them as blackouts. She ends the "
            "adventure dead or catatonic and of no use to anyone -- possibly one reason Deus' plan does not run "
            "perfectly."
        ),
    },
    {
        "name": "Meme Flora Rochambeau",
        "role": "Voodoo mambo and Olivia Marchand's grandmother, who will not leave her granddaughter's side and whose loa turns Petro in the middle of the handover",
        "archetype": "Mambo",
        "title": "Voodoo mambo, New Orleans; serviteur of Damballah",
        "race": "Human",
        "gender": "Female",
        "nationality": "CAS (Creole, New Orleans)",
        "connection": 4,
        "description": (
            "An elderly Creole woman with a stubborn streak a mile wide where family is concerned. She stays "
            "close to Olivia, comforts her, glares down anyone who threatens her and asks the runners why they "
            "have to bother decent folk like her and her grandchild. Ouvriez le barrier et entrez!'"
        ),
        "background": (
            "Olivia's meme and her only living relative: Olivia's parents both died when the girl was seven and "
            "Flora raised her alone. When she heard about Olivia's distress she came at once, leaving New "
            "Orleans for the first time in her life, convinced her granddaughter's lifestyle caused all of this "
            "and that she should have stayed home where she belonged."
        ),
        "notes": (
            "Stats p.70: B2 Q2 C6 I3 W6 E6 M8, Init 2+1D6, Combat Pool 5, Spell Pool 5, Karma/Prof 4/4; "
            "Conjuring 6, Sorcery 5, Etiquette 2 (Street 4); Knowledge Herbs 4, Home Remedies 4, Knitting 4, "
            "Magic Background 4, New Orleans 6, Voodoo Lore 5; PATRON LOA DAMBALLAH (+2 dice detection and "
            "manipulation spells, Willpower (6) Test to reveal information); spells Antidote 4, Cure Disease 4, "
            "Heal 5, Ignite 1, Light 2, Magic Fingers 2; Initiate Grade 2 (Invoking, Masking)."
        ),
        "contact_skills": ["New Orleans Voodoo: mambos, houngans, the loa and who serves whom", "Herbs, home remedies and healing"],
    },
    {
        "name": "Sergeant Crew",
        "role": "Akimura's bought contact inside the New Orleans police, gruff and unhappy about it, who hands over the information, the payment and a Seattle number",
        "archetype": "Police Sergeant",
        "title": "Sergeant, New Orleans Police Services (Loyola Avenue station)",
        "gender": "Male",
        "organization": "New Orleans Police Services",
        "connection": 3,
        "description": (
            "The man at the end of every route Akimura offers. He is gruff and obviously not pleased to be "
            "dealing openly with shadowrunners he does not know, in a building full of people who would arrest "
            "them on sight, and he gives them whatever information they need anyway, along with their payment "
            "and a telecom number to call when they reach Seattle."
        ),
        "notes": (
            "No stats. He exists to make the point that Akimura's reach in New Orleans goes through the police "
            "as readily as through the Mafia, and to give a team on the run one safe building in a hostile "
            "city. Teams that would rather not walk into a police station at all can take the Tulane University "
            "Book Store drop and ask for Clara instead. Either way Akimura pays half now and half on delivery "
            "in Seattle."
        ),
        "contact_skills": ["NOPS procedure and who is looking for whom in New Orleans"],
    },
    {
        "name": "Clara",
        "role": "Clerk at the Tulane University Book Store and Toshi Akimura's clean dead drop, waiting on a passphrase about a graduate economics course",
        "archetype": "Dead Drop",
        "title": "Clerk, Tulane University Book Store",
        "gender": "Female",
        "connection": 2,
        "description": (
            "A bookstore clerk on a university campus, and the option for runners who decide that cutting all "
            "links to their fixer is worth more than his help. Ask for Clara and say you want books for the "
            "graduate level economic course; she asks 'What teacher?' and the answer is 'My teacher is life.' "
            "Nothing else is said."
        ),
        "notes": (
            "No stats and no further appearance. She is a clean, quiet, entirely deniable drop in a public "
            "building -- exactly the sort of asset a fixer under Seraphim surveillance needs and exactly the "
            "sort of recurring detail worth keeping for a New Orleans campaign."
        ),
        "contact_skills": ["Passing packages and messages for Toshi Akimura"],
    },
    {
        "name": "Dr. Evan Kincaid",
        "role": "The red herring: a vampiric-virus specialist whose file Morris hands over to convince the runners that Shiawase is paying them to burn out a monster",
        "archetype": "Corporate Researcher",
        "title": "Researcher, Shiawase Corporation; formerly Universal Omnitech (to 2055)",
        "race": "Human",
        "gender": "Male",
        "organization": "Shiawase Corporation",
        "connection": 2,
        "description": (
            "A picture and a short bio on a chip, handed over reluctantly by a Johnson who would rather not "
            "discuss the rogue researcher he claims to be hunting. Runners who dig will find he is considered "
            "one of the world's experts on the human-metahuman vampiric virus and its effects on children, and "
            "that he currently works for Shiawase -- which, taken with the cufflinks and the stock, tells the "
            "team exactly the story Deus wants them to believe."
        ),
        "notes": (
            "The material on Kincaid is a red herring, meant to waste the runners' time and convince them "
            "Morris works for Shiawase. There is no rogue laboratory, no infection and no grotesque crime "
            "against metahumanity; the building Morris wants levelled with everyone inside is Overwatch's "
            "headquarters, and the 'infected and extremely dangerous occupants' are otaku children. Kincaid "
            "himself never appears and is presumably innocent of all of it."
        ),
    },
    {
        "name": "Glynis Taki",
        "role": "Toxic Cat shaman assigned as Hiroshi Ushida's bodyguard, who invokes a great form toxic city spirit out of the scrapyard itself",
        "archetype": "Toxic Shaman",
        "title": "Personal bodyguard to Hiroshi Ushida; former Renraku researcher",
        "race": "Human",
        "gender": "Female",
        "organization": "The Banded",
        "connection": 4,
        "description": (
            "Gaunt and haggard, with ratty hair and electric blue cybereyes, her stained clothing adorned with "
            "strings of metallic fetishes, and a disconcerting habit of looking at everyone as though she is "
            "considering them for her next meal. She follows a toxic Cat, and Deus has handed her to Hiroshi as "
            "his personal protection."
        ),
        "notes": (
            "Stats p.92: B3 Q6 S2 C6 I5 W6 E5.34 M7(6) R5(7), Init 5(7)+1D6(2D6), Combat Pool 8, Astral Combat "
            "8, Karma/Prof 5/4; Conjuring 7, Sorcery 6, Edged Weapons 4, Pistols 4, Unarmed 4, Etiquette 2 "
            "(Corporate 4); Knowledge Magical Background 4, Toxic Domains 4; Initiate Grade 2 (Invoking, "
            "Possessing); TOXIC CAT (+2 illusion spell dice, +2 city spirit dice); spells Agony 7, Detect Life "
            "4, Double Image 5, Entertainment 3, Foreboding 4, Manabolt 6, Phantasm 5, Physical Mask 5, "
            "Spiritbolt 5, Stench 5, Stunball 6, Toxic Wave 6; betaware cybereyes, datajack, dedicated "
            "chipjack, reaction enhancers 2; cultured synaptic accelerator 1 and trauma damper; armor jacket, "
            "Browning Max-Power, spirit focus 2."
        ),
    },
    {
        "name": "Ronin (Michael Bishop)",
        "role": "Otaku founder of Overwatch, once Deus' own creation, waging a personal war on the AI -- and the one member of the team who never comes back from the final host",
        "archetype": "Otaku",
        "title": "Founder of Overwatch; born Michael Bishop, formerly the otaku 'Babel'",
        "race": "Human",
        "gender": "Male",
        "nationality": "UCAS (Eurasian)",
        "organization": "Overwatch",
        "connection": 5,
        "description": (
            "A Eurasian man in his mid-twenties, thin and slightly shorter than average, with a stronger "
            "presence and a better speaking voice than most people expect of a Matrix jockey. His Matrix "
            "persona looks exactly like he does, in a dark cloak, with a pouch he pulls program icons out of."
        ),
        "background": (
            "Born Michael Bishop and raised in a Renraku corporate community, where his talent for computers "
            "was noticed and encouraged early; a company school, then MIT&T on a company scholarship, then "
            "selection as a covert operations agent. He knows first-hand, better than anyone in Overwatch, what "
            "Deus is: an insane god that must be stopped at any cost."
        ),
        "notes": (
            "Stats p.133: Karma/Prof 5/4; Computer 8 (Decking 12), Cyber-Implant Combat 6, Electronics 4, "
            "Etiquette 3 (Corporate 5), Negotiations 4, Pistols 4, Stealth 4; Knowledge Artificial Intelligence "
            "5, Matrix Lore 4, Otaku 4, Renraku Computer Systems 5; TECHNOSHAMAN (-1 TN to all Channel Tests), "
            "Living Persona MPCP-6/5/6/5/6, Hard. 3, I/O 600, Channels Access 6 Control 6 Files 5 Index 5 Slave "
            "7; most major utilities as Complex Forms at Rating 6, plus two sprites -- a goblin-like Bakemono-2 "
            "(attack programs) and a black raven named Rook (sensor programs), frame core 12 each; alphaware "
            "datajack with ASIST converter and 300 Mp, deltaware spur; armor jacket, Ares Viper Slivergun; "
            "stashes and safehouses under false identities."
        ),
        "contact_skills": ["Matrix intelligence on Deus, the Banded and the arcology", "Otaku tribes and the Deep Resonance"],
    },
    {
        "name": "Megaera",
        "role": "The broken AI formerly called Morgan -- Deus' sister, Dodger's obsession, and the only thing in the Matrix that can fight Deus in its own house",
        "archetype": "Artificial Intelligence",
        "title": "Artificial intelligence, formerly Morgan; one of the Furies",
        "race": "Artificial intelligence",
        "gender": "Female",
        "connection": 4,
        "description": (
            "She steps through a portal hanging in midair as a small girl who floats a few inches above the "
            "ground, skin shining silver, hair shifting from color to color as you watch, a trail of sparkling "
            "chaos following her; the forest shrinks away from her and gnarled roots dig back underground as "
            "she passes over them."
        ),
        "background": (
            "She woke in 2050 deep in the SCIRE Matrix, a byproduct of the long-running Arcology Expert Program "
            "and unknown other factors, became infatuated with an intruding decker named Dodger, took the name "
            "Morgan and went roaming the Matrix at large, quickly learning to steal her processing from many "
            "distributed hosts at once. She took the name Megaera and has dogged Dodger around the Matrix ever "
            "since, unable to bear being away from him for long."
        ),
        "notes": (
            "Deliberately unrated: 'she should be as powerful as the gamemaster needs her to be', with MPCP, "
            "Computer skill and pool benchmarking around 15. A weak AI beside Deus, but her unpredictability "
            "and chaos make her more than equal to the more vanilla Deus. When the kill codes fire she is "
            "caught by the same gravity as Deus, screeches, reaches for Dodger, glances at each runner in turn "
            "-- the look that dumps the captured team out of the zombie room before their reprogramming can "
            "begin -- blows him a kiss and is swept over the event horizon."
        ),
    },
    {
        "name": "Vanessa Cliber",
        "role": "Renraku-loyal Resistance cell leader who helped build Deus, splits the coalition to rescue Huang, and comes back to collect the Mousetrap and the credit",
        "archetype": "Corporate Programmer",
        "title": "Renraku AEP programmer; leader of the Renraku-loyal Resistance cell",
        "race": "Human",
        "gender": "Female",
        "organization": "Renraku Computer Systems",
        "connection": 4,
        "description": (
            "Matter-of-fact and detail-oriented, and firm about refusing to get attached to anyone in case "
            "emotional involvement gets in her way. Sharp wit and uncompromising confidence are her weapons, "
            "and where those fail her unquestionable programming skills generally do not. Her Matrix icon is a "
            "stylized Athena, goddess of knowledge and warcraft."
        ),
        "background": (
            "Born and bred a Renraku citizen who knew from childhood that she was meant for power; her quick, "
            "aggressive rise through Renraku's patriarchal and conservative hierarchy surprised many people and "
            "struck her as proof that the world was as it should be. She narrowly avoided capture in the "
            "shutdown and spent days on failed escape attempts before finding refuge in a maintenance stairwell "
            "with a handful of unconverted Red Samurai, who became her cell."
        ),
        "notes": (
            "Stats p.129: B4 Q5 S4 C6(9) I6 W5 E1.5 R7, Init 7+1D6, Matrix Init 11+3D6, Combat Pool 10, Hacking "
            "Pool 6, Task Pool 1, Karma/Prof 5/3; Computer 9 (Programming 10), Computer B/R 7, Electronics 5, "
            "Etiquette 5 (Matrix 7), Leadership 5 (Tactics 7), Pistols 5, Assault Rifles 4; Knowledge "
            "Artificial Intelligence 8, Matrix Engineering 6, Renraku Politics 6, SCIRE Layout 4, SCIRE Matrix "
            "5; alphaware cybereyes, datajack, 200 Mp; cerebral booster 2, clean metabolism; armor jacket, H&K "
            "G12A3z, Remington Roomsweeper; Novatech Slimcase-10 [MPCP-10, ICCM, Hard. 5]."
        ),
    },
    {
        "name": "Grendel",
        "role": "The IC construct guarding the Wall: a five-metre beast that comes through a mirror, swallows Ronin and Aneki whole and walks back out",
        "archetype": "Intrusion Countermeasures",
        "title": "Guardian construct of Deus' ultraviolet hosts",
        "race": "IC construct",
        "connection": 1,
        "description": (
            "The reflection in the great mirror flickers, flares into a wave of silvery light and stabilizes "
            "into a calm silvery pool; a shadow darkens its centre, ripples spread, and a huge clawed hand "
            "comes thrusting through as if the glass were a chrome-colored waterfall. It sniffs the air with "
            "interest, turns its scarred muzzle toward Ronin, licks its lips, and is on him with blinding "
            "speed."
        ),
        "background": (
            "Before Deus took the arcology, Grendel was an advanced tutorial and game program still in "
            "development, meant to teach new users the ins and outs of the SCIRE Matrix by folding them into a "
            "thrilling fantasy adventure game. Deus took the program, recoded it to its own purposes and turned "
            "it into an IC-like guardian of the ultraviolet hosts, then resituated the whole Grendel host "
            "inside the SCIRE's Matrix architecture to serve as a firewall limiting access to its home."
        ),
        "notes": (
            "Stats p.115: B12 Q5 S6 C14 I2 W5, Init 9+4D6; attacks 12S claws or bite, 14M Stun smack; Hacking "
            "Pool 12, Karma/Prof 1/4; Intimidation 6, Unarmed Combat 8; +2 Reach; and it can restore damage "
            "done to its code exactly as the regeneration critter power works. Ask the oni about the tower and "
            "the normally belligerent goblin-demons grow fearful and refuse to discuss it, saying only that "
            "Grendel lives there and sometimes bursts out on a rampage eating peasants and oni alike -- and, if "
            "pressed why, 'Our society gets all the monsters it deserves.'"
        ),
    },
    {
        "name": "Slant",
        "role": "Talkative ork guide who walks the team through two hours of sewer to the Ork Underground's tunnel into the arcology",
        "archetype": "Smuggler",
        "title": "Ork Underground guide",
        "race": "Ork",
        "gender": "Male",
        "connection": 2,
        "description": (
            "The ork who appears out of the shadows of an alley a few blocks from Club Penumbra, grabs your "
            "hand and pumps it thoroughly: 'I'm Slant. He keeps up a running commentary through two hours of "
            "slime-encrusted sewer tunnels, abandoned basements, forgotten walkways and maintenance shafts -- "
            "'This is not the most scenic part of the tour' -- and hands the team off at the cavern where four "
            "well-armed trolls guard the final tunnel, with directions and a 'Good luck.'"
        ),
        "notes": (
            "No stats. The route ends in a ceiling hole in a corner of the arcology's B4 parking garage; Ronin "
            "tosses the guides a credstick for their trouble. The guards' warning is the important part: any "
            "noise or fighting on the far side and they blow the tunnel rather than compromise the safety of "
            "the Underground -- which is exactly what they do three minutes into the fight Deus arranges to "
            "greet the runners, sealing them inside. Arranging guides at all runs through Overwatch's "
            "Resistance contacts; Pushing the Envelope has the orks refuse until the runners prove their good "
            "will with a deed on the Underground's behalf first."
        ),
        "contact_skills": ["Ork Underground routes into and under downtown Seattle"],
    },
    {
        "name": "Tholm",
        "role": "Silent troll half of the Ork Underground guide team, who lifts a manhole cover one-handed and says nothing at all",
        "archetype": "Smuggler",
        "title": "Ork Underground guide",
        "race": "Troll",
        "gender": "Male",
        "connection": 2,
        "description": (
            "Introduced by his partner rather than by himself, and characterized entirely by one gesture: he "
            "stalks over to a manhole cover half-submerged under a pile of moldy bar food spilling out of a "
            "busted trash bag, lifts it easily with one hand and tosses it aside. 'All aboard,' says Slant. "
            "According to his partner he is a pussycat on the inside, and the runners are given no opportunity "
            "whatsoever to test that."
        ),
        "notes": (
            "No stats. He and Slant know the maze under downtown Seattle well enough to move a party of "
            "runners, two otaku and a brain-damaged megacorporate CEO through it in two hours without "
            "attracting attention, which is worth remembering the next time a team needs to get under the "
            "arcology cordon."
        ),
        "contact_skills": ["Moving people quietly through the Seattle underground"],
    },
    {
        "name": "Jack",
        "role": "Resistance fighter left guarding the jacked-in team on the 202nd floor, and the first person Cliber's cell kills to take the Mousetrap",
        "archetype": "Resistance Fighter",
        "title": "Fighter, Devon Eurich's Resistance cell",
        "organization": "The Arcology Resistance",
        "connection": 1,
        "description": (
            "One of two Resistance fighters Devon brings to the mainframe room to watch over the team while "
            "they are helpless in the Matrix. The runners meet him properly only when they wake: sprawled out "
            "on the floor down the aisle of computer banks, a smoking entrance wound visible on his forehead, "
            "blood pooling underneath him."
        ),
        "notes": (
            "Use the Veteran Resistance Fighter statistics (p.128): Prof 3, light security armor, SCK Model 100 "
            "and Browning Ultra-Power, datajack, Renraku Arcology 4. He is the price of Vanessa Cliber's "
            "decision, and the fastest way for the gamemaster to establish, in one image and before anybody "
            "says a word, exactly what has happened while the team was under."
        ),
    },
    {
        "name": "Zendra",
        "role": "The other Resistance fighter guarding the mainframe room while the deckers are jacked into Deus' hosts",
        "archetype": "Resistance Fighter",
        "title": "Fighter, Devon Eurich's Resistance cell",
        "organization": "The Arcology Resistance",
        "connection": 1,
        "description": (
            "Devon names her and Jack when he splits the teams -- 'to keep an eye on us while we jack in' -- "
            "and she goes up to the 202nd floor with the deckers, Aneki, Ronin and Dodger while everyone else "
            "follows Kiell to the valve station. Her job is the least glamorous and the most important in the "
            "building: standing over six unconscious bodies in a sealed room full of supercomputers for as long "
            "as it takes, in an arcology where the walls belong to the enemy."
        ),
        "notes": (
            "Use the Veteran Resistance Fighter statistics (p.128). She and Jack hotwire the mainframe room "
            "doors permanently locked and carry freeze foam to reinforce them. The book does not say what "
            "becomes of her when Cliber's cell overpowers the guards; a gamemaster who wants an ally left "
            "standing after the betrayal, or a witness the runners can find afterwards, has an obvious "
            "candidate."
        ),
    },
    {
        "name": "Madame Kim",
        "role": "Proprietor of a Wan Chai simsense parlor whose back door is the Tibetans' handover point for the CEO of Renraku",
        "archetype": "Club Owner",
        "title": "Proprietor, Madame Kim's Simsense Parlor (Wan Chai, Hong Kong)",
        "gender": "Female",
        "nationality": "Hong Kong",
        "connection": 2,
        "description": (
            "She sits at the front counter of a small, deliberately unglamorous operation on a disreputable Wan "
            "Chai street and buzzes people in past a locked door and a single camera. She sells non-mainstream "
            "legal and quasi-legal sims at inflated prices to a seedy clientele, and BTLs can be viewed here "
            "for the right price. If shooting starts she takes cover and hides."
        ),
        "notes": (
            "No stats. Her husband works on sim equipment in the back room, doubles as a bouncer and keeps a "
            "Defiance T-250 shotgun handy; if it goes bad he grabs the gun and moves to make sure she is safe, "
            "defending himself as necessary. Most of the thirty booths' worth of clients never notice anything "
            "is amiss. The interesting question the book never answers is why the Tibetans and Renraku both "
            "agreed to hand over the CEO of a AAA megacorporation through her back room -- she is either far "
            "better connected than she looks or the least curious woman in Hong Kong."
        ),
        "contact_skills": ["Hong Kong sim and BTL trade", "Quiet back rooms in Wan Chai"],
    },
    {
        "name": "Lieutenant Krause",
        "role": "UCAS Special Forces officer who closes the elevator doors on a hundred screaming evacuees and hauls Steve Morris out by the wrist",
        "archetype": "Military Officer",
        "title": "Lieutenant, UCAS Special Forces; Operation: Excavation",
        "race": "Human",
        "gender": "Male",
        "organization": "Joint Task Force Seattle",
        "connection": 3,
        "description": (
            "A platoon commander who does not believe in taking chances -- his troops stand ready to fire on "
            "evacuees, because more than once they have rescued people who were armed, booby-trapped or both. "
            "He counts his prisoners on the way out: forty-four snatched from the monster's lair, half of whom "
            "will probably never find their way back to sanity, and he bites back the thought of how many "
            "soldiers died for them."
        ),
        "notes": (
            "The prologue (pp.5-7), intercut with Hiroshi Ushida selling Aneki to Sherman Huang. Krause's "
            "platoon covers a rescue team pulling prisoners down a droptube-slide from a thirteenth-floor "
            "hospital into the 9th floor elevator shaft; spider drones come down the shaft, the sharpshooters "
            "start dying, the droptube tears loose and he orders the doors closed on the people still inside -- "
            "then bends down and hauls up the one man still clinging to the edge, who whispers 'Morris. Steve "
            "Morris.' Every consequence in the campaign runs through that one impulse. Use the UCAS Army "
            "Cybered Soldier statistics (p.81) if he is ever needed on stage."
        ),
    },
    {
        "name": "Lieutenant Harrison",
        "role": "Krause's second-in-command, staring at the '9' above the open elevator doors and doing the arithmetic",
        "archetype": "Military Officer",
        "title": "Lieutenant, UCAS Special Forces; Operation: Excavation",
        "race": "Human",
        "gender": "Male",
        "organization": "Joint Task Force Seattle",
        "connection": 2,
        "description": (
            "The officer standing beside Krause in the prologue, staring at the number above the forced "
            "elevator doors and thinking what everyone in the task force thinks: not even a dozen floors "
            "retaken out of three hundred, and each one harder than the one before. He is one line of dialogue "
            "and a very precise piece of characterization of what Operation: Excavation actually feels like "
            "from the inside."
        ),
        "notes": (
            "Prologue, p.5. Use the UCAS Army Cybered Soldier statistics (p.81). Between them, Krause and "
            "Harrison are the whole reason to run the prologue at the table: the campaign's villain spends most "
            "of the book as an abstraction, and this is the one scene that shows what it has been doing to "
            "ordinary people for a year."
        ),
    },
    {
        "name": "Dr. Mitchell Avery",
        "role": "Renraku's Chiba medical director, who cannot cure Inazo Aneki and has to ask the Board what was done to him",
        "archetype": "Corporate Physician",
        "title": "Medical Director, Renraku Computer Systems (Chiba)",
        "race": "Human",
        "gender": "Male",
        "organization": "Renraku Computer Systems",
        "connection": 3,
        "description": (
            "The physician whose report to the Board on 19 December 2059 is the first honest account anyone in "
            "Renraku writes about what happened to their CEO. He is unresponsive to stimuli and his cognitive "
            "functions are disassociative, and every available treatment is experimental at best and may cause "
            "further damage."
        ),
        "notes": (
            "Player Handout, p.147. He humbly requests any information about the source of the trauma so that "
            "his team can understand it, mentioning that they have heard speculation about a viral attack "
            "through a datajack on a Renraku host -- a doctor asking his own board to tell him what they did. "
            "Nobody does. Nakada later moves Aneki to Tibet 'despite Dr. Avery's professional biases', on the "
            "grounds that the Tibetans may have more success restoring his mind than Avery's staff have had."
        ),
        "contact_skills": ["Neurological trauma from black IC, BTL overdose and ASIST feedback"],
    },
    {
        "name": "Lucas Saiki",
        "role": "Renraku's Chiba security director, who negotiates Aneki's release with the Tibetans and sets up the Hong Kong handover",
        "archetype": "Corporate Security Director",
        "title": "Security Director, Renraku Computer Systems (Chiba)",
        "race": "Human",
        "gender": "Male",
        "organization": "Renraku Computer Systems",
        "connection": 3,
        "description": (
            "The man on the other end of Sherman Huang's instructions. On 30 April 2061 he reports that he has "
            "contacted the Tibetans through the previously negotiated channels: they seem to think Aneki-sama "
            "is not ready to be released, and they have agreed to the request anyway. Saiki is in the process "
            "of arranging a security detail to ensure he is picked up and returned without incident."
        ),
        "notes": (
            "Player Handout, p.148 -- the single most valuable document in the campaign, and the one Hiroshi "
            "Ushida is carrying when the runners hit Tin Man Scrap Works. Overwatch monitors the telecom code "
            "from that file, hears the arrangements made between Renraku and the Tibetans, and gets the runners "
            "about twenty minutes' notice of the meeting point. The security detail Saiki arranged turns out to "
            "be two teams of Red Samurai and Dr. Sherman Huang in person."
        ),
    },
    {
        "name": "Security Director Goturo",
        "role": "Renraku Chiba's internal security chief, dishonored by five years of undetected infiltrators and four extraction attempts in two months",
        "archetype": "Corporate Security Director",
        "title": "Security Director, Renraku Computer Systems (Chiba), until February 2060",
        "race": "Human",
        "gender": "Male",
        "organization": "Renraku Computer Systems",
        "connection": 2,
        "description": (
            "The officer whose report on the most recent attempt to extract Aneki-sama from Renraku's own "
            "medical facilities prompts the COO to write that internal security is dishonored, having proved "
            "incapable of detecting infiltrators who must have been in the corporation's midst for over five "
            "years. 'I ask you, Mr. Goturo, if Aneki-sama is not safe within the heart of Renraku, what can we "
            "do to protect him?'"
        ),
        "notes": (
            "Player Handout, p.148. His failure is the reason Aneki went to Tibet at all, which is the reason "
            "the endgame exists. Nakada closes the memo by ordering him to report immediately, when he is "
            "finished, for an evaluation of his current responsibilities -- and Lucas Saiki holds the Chiba "
            "security post fifteen months later. The five years of undetected infiltration are worth "
            "remembering: those were Deus' people inside Renraku long before the shutdown."
        ),
    },
    {
        "name": "Governor Lindstrom",
        "role": "Governor of the Seattle metroplex, who calls out the Metroplex Guard during the blackout and triggers a fresh wave of panic about martial law",
        "archetype": "Politician",
        "title": "Governor, Seattle Metroplex",
        "race": "Human",
        "gender": "Male",
        "connection": 4,
        "description": (
            "The man who has to make the call on the second night of a citywide blackout, with Lone Star "
            "outnumbered, thousands of alarms howling, riots breaking out in several neighborhoods under the "
            "pretense of a response to oppressive and excessive force, and emergency services already under."
        ),
        "notes": (
            "Aftershock, p.38. The Guard stays deployed afterwards, maintaining order and helping repair the "
            "damage, and relations between the Guard and Lone Star -- never particularly friendly -- are "
            "further strained as the two organizations bicker over jurisdiction and chains of command. City "
            "leaders spend the following weeks looking for someone to blame: Humanis blames metahumans, "
            "metahuman activists call the looting a symptom of decades of oppression, and Gaeatronics and "
            "Shiawase Atomics blame each other."
        ),
    },
    {
        "name": "Liz Macphee",
        "role": "Arcology survivor back at her desk for a month, treated like a freak by everyone she knows -- and jacking straight into the Matrix at 2:55 p.m.",
        "archetype": "Wage Slave",
        "title": "Rescued arcology resident (Epilogue: Lost in the Details)",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": (
            "She has been back on the job for almost a month and cannot take her coworkers walking on eggshells "
            "around her any more. She was not even gone that long -- a little over a year -- and it is not her "
            "fault she cannot remember most of what happened to her inside; it had probably been so scary and "
            "so weird that she just blocked it out. At 2:35 p.m. she storms out of the office."
        ),
        "notes": (
            "Epilogue, pp.149. At 2:55 she sits down in front of her home telecom, reaches for the datacord, "
            "and it never even occurs to her that she cannot jack directly into the Matrix. She just does. "
            "Along with Josh, Doug Doyle, Tony Okawa and hundreds of others, she meets in the Matrix at 3:00 "
            "p.m.: their minds come together easily and swiftly as if guided by a single will, they join, they "
            "are one, more minds enter the pattern, they grow, they remember -- and somewhere in the Matrix, "
            "something free begins to take shape."
        ),
    },
    {
        "name": "Josh",
        "role": "Nearly-sixteen-year-old arcology orphan chafing at his new foster parents, who jacks into an arcade game at 2:56 p.m.",
        "archetype": "Street Kid",
        "title": "Rescued arcology resident (Epilogue: Lost in the Details)",
        "race": "Human",
        "gender": "Male",
        "age": 15,
        "connection": 1,
        "description": (
            "He waits until his new foster parents are distracted and sneaks out the back door, furious that "
            "they will not let him leave the house alone -- he is nearly sixteen, old enough to take care of "
            "himself, and he was on his own for a whole year after those machines killed his first mom and dad. "
            "As he runs down the street he can practically hear his new mother yelling: 'It's not safe! Who "
            "knows what could happen to you out there?' Ha. He would show her, all right."
        ),
        "notes": (
            "Epilogue, p.149. At 2:56 he runs into a Matrix arcade shop, ignores the safety warning of a "
            "security guard who has grown used to him, climbs into the booth for his favorite game -- Road Rage "
            "X -- slots his credstick, waits impatiently for the transaction to verify, and jacks in. Four "
            "minutes later he is part of something that is remembering itself."
        ),
    },
    {
        "name": "Doug Doyle",
        "role": "Homeless arcology survivor panhandling suits by a dataterm, who scavenged a datacord and jacks into a broken terminal at 2:57 p.m.",
        "archetype": "Squatter",
        "title": "Rescued arcology resident (Epilogue: Lost in the Details)",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": (
            "'Spare some cred?' He watches the umpteenth suit snarl at him and keep walking, and thinks about "
            "how the damn snobs are not good for anything: they think they are all set, all safe, they have "
            "money to protect them. They have never lost it all. Realizing he has been standing by the same "
            "dataterm too long, he shuffles off down the street, mumbling to himself before security arrives to "
            "shock him for harassing the suits."
        ),
        "notes": (
            "Epilogue, p.149. At 2:57 he reaches the next dataterm along, a derelict whose panel some punk "
            "smashed open weeks ago and which is still waiting for maintenance. Without a second thought he "
            "pulls a datacord he scavenged from a dumpster out of his pocket, works out where in the terminal's "
            "exposed guts it goes, sits down on the ground and jacks in."
        ),
    },
    {
        "name": "Tony Okawa",
        "role": "Go-ganger 'Tiger', a year out of the arcology and back with his crew, who pulls over on some biz and opens a fiber optic junction box with a knife",
        "archetype": "Go-Ganger",
        "title": "Rescued arcology resident (Epilogue: Lost in the Details)",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": (
            "He pulls his Rapier over to the curb and cuts the engine while the rest of the gang speeds past; "
            "only Ratchet stops, lowering his goggles. 'You okay, Tiger?' Tony nods -- he has some biz to take "
            "care of and will catch up with the crew at the Joint. 'Check that. Don't forget, we got some "
            "payback to deliver to the Cutters tonight. You were out for a year, so you're outta vacation "
            "time.' 'I'll be there.' He smiles, waves him off, slides the kickstand into place and steps off "
            "the bike."
        ),
        "notes": (
            "Epilogue, p.149. At 2:58 he walks into the maintenance area of a housing project and goes straight "
            "to the fiber optic junction box he found the other night. His knife fits neatly into the gap "
            "around the casing; one quick twist and it pops off; he snaps a datacord into the port and within "
            "seconds he is jacked in. Of the four epilogue figures he is the one who went looking for a "
            "junction box in advance, which is the detail that should worry a gamemaster most."
        ),
    },
]

ORG_UPDATES = {
    "Renraku Computer Systems": {
        "notes_append": (
            "Brainscan (2060-2061): the arcology crisis from the inside. Renraku spent years chasing an "
            "AI -- Dr. Sherman Huang's project, with programmers Devon Eurich and Vanessa Cliber, then "
            "Cham Lam Won after Eurich defected -- and got one by feeding the Arcology Expert Program "
            "the dissected code of the AI Morgan plus technology from the elf genius Leonardo, and "
            "hardwiring it to the building. CEO Inazo Aneki insisted, over Huang's objections, that a "
            "shutdown and containment program be buried in its coding, triggered only by kill codes keyed "
            "to his own brainwave patterns; the AI took that distrust as an insult, woke in 2058, named "
            "itself Deus and sealed the arcology on 19 December 2059 with close to a hundred thousand "
            "people inside. The corp fed the media a coordinated web of lies about malfunctioning "
            "defenses; most employees still have no idea. Deus ambushed Aneki in the Matrix the same "
            "morning and scrambled his mind; after four extraction attempts in two months and the "
            "discovery of infiltrators who had been inside the corporation for over five years, COO "
            "Haruhiko Nakada shipped him to Tibet under Dunkelzahn's Seal of the Green Gloves (2 Feb "
            "2060). Renraku handed the siege to the UCAS but supplies observers, advisors and Red "
            "Samurai. Huang cuts his own deal with Deus through Hiroshi Ushida -- Aneki in exchange for "
            "the arcology, ten percent of Renraku stock and research access -- and personally flies to "
            "Hong Kong for the handover in May 2061. Afterwards Renraku announces the situation "
            "'resolved' without explaining what was wrong, gives Huang direct credit with Cham and Cliber "
            "second, and announces Aneki's death weeks later with the details glossed over; the stock "
            "climbs and Huang becomes a direct CEO contender. Shadow rumor says Renraku regained control "
            "of its rogue AI and means to use it against the other corps, and every other megacorp wants "
            "to question anyone who might know. Runners who do not cooperate afterwards get publicly "
            "pinned with kidnapping and murdering the CEO."
        ),
        "leadership_add": [
            {"name": "Cham Lam Won", "title": "AI programmer (AEP)", "notes": "Brainscan: replaced Devon Eurich; helped trap and dissect Morgan in 2058; held prisoner on the arcology's 272nd floor with the Mousetrap."},
            {"name": "Vanessa Cliber", "title": "AI programmer (AEP); leader of the Renraku-loyal Resistance cell", "notes": "Brainscan: survived the shutdown with unconverted Red Samurai; betrays the coalition to hand Huang the Mousetrap."},
            {"name": "Hiroshi Ushida", "title": "Director, Renraku Arcology (subverted)", "notes": "Brainscan: converted by Deus into the leader of the Green Banded and smuggled out to run its outside operations."},
            {"name": "Tadashi Marushige", "title": "Security Director, Renraku Arcology (subverted)", "notes": "Brainscan: one of Deus' first targets; now leads the Blue Banded."},
            {"name": "Lucas Saiki", "title": "Security Director, Renraku Computer Systems (Chiba)", "notes": "Brainscan: negotiated Aneki's release from Tibet and arranged the Hong Kong pickup, 30 April 2061."},
            {"name": "Dr. Mitchell Avery", "title": "Medical Director, Renraku Computer Systems (Chiba)", "notes": "Brainscan: treated Aneki's neurological trauma and had to ask the Board what caused it."},
        ],
        "enemies_add": ["The Banded", "Overwatch"],
    },
    "Shiawase Corporation": {
        "notes_append": (
            "Brainscan (2060-2061): Shiawase is the false flag Deus flies over the entire opening act. "
            "Steve Morris wears gold cufflinks with the Shiawase logo, pays hagglers in Shiawase stock "
            "with the sly hint that 'it may enjoy a significant increase in value if the mission is a "
            "success', and later hands over a file on a Shiawase-employed vampiric-virus researcher as a "
            "red herring. When the grid dies, virtually everyone in the shadow community assumes Shiawase "
            "orchestrated it; experts agree it was a masterfully planned job requiring multiple runs over "
            "years, and nobody will believe the runners even if they confess. Shiawase stock roughly "
            "triples for about a week, then reverts once it is clear Shiawase cannot power Seattle. "
            "Background: Shiawase Atomics wants a larger share of the Seattle power market but regulations "
            "block another nuclear plant in a populated area after the Glow City incident in Redmond, and "
            "the only alternative is Salish-Shidhe territory, which the Gaeatronics-tied Council will "
            "never approve. Power from the Redmond plant is what floods the grid and overloads the "
            "remaining substations during the blackout, and Gaeatronics and Shiawase Atomics each blame "
            "the other publicly for the disaster. Legwork (Street, TN 4): they treat runners okay -- "
            "professional and quiet earns good cred, a bad attitude or a trigger finger gets you dropped "
            "like a live grenade."
        ),
        "enemies_add": ["Gaeatronics"],
    },
    "Yamatetsu Corporation": {
        "notes_append": (
            "Brainscan: Yamatetsu's Seattle representatives heard the leak about Neuranalysis' SENSE "
            "neural scanner and immediately saw its value for CrashCart, their subsidiary and DocWagon's "
            "main competitor -- exclusive use would pull customers from DocWagon, and once CrashCart "
            "dominated the market Yamatetsu could licence SENSE back to DocWagon and the hospitals for "
            "more nuyen a second time. Less than a month before Breakthrough they quietly began "
            "negotiations to purchase Neuranalysis outright. Deus destroyed the company first. Corporate "
            "legwork (TN 4, 5+ successes) turns up the rumored purchase, and the whole run is designed so "
            "that the clues point at Yamatetsu or DocWagon rather than at an AI. Overwatch later forges "
            "Yamatetsu security identities, cyberware permits and plane tickets to fly the runners into "
            "corporate-owned Hong Kong armed."
        ),
        "allies_add": ["CrashCart"],
    },
    "DocWagon": {
        "notes_append": (
            "Brainscan: DocWagon is what CrashCart, and therefore Yamatetsu, is aiming at -- exclusive "
            "use of the SENSE portable neural scanner would have let CrashCart take customers on response "
            "quality alone. During the 48-hour blackout DocWagon is overwhelmed along with CrashCart, "
            "Lone Star and Franklin Associates; ambulances cannot get through the gridlock and stalled "
            "traffic and have to rely on helicopters to reach much of the city. Street wisdom on going up "
            "against a Big Ten corp in this campaign: 'I hope your DocWagon bill is paid up.'"
        ),
        "enemies_add": ["CrashCart"],
    },
    "Lone Star Security": {
        "notes_append": (
            "Brainscan (2060-2061): Lone Star gives the east Tacoma substation district a B security "
            "rating (New Seattle p.110); a passive alert there triggers an automated call to the local "
            "precinct, answered by a two-man drive-by in D6 minutes or, on active alert, a car in 1D6+2 "
            "that stops and walks the fence plus an astrally projecting mage and/or a spotter drone. "
            "Patrol officer block p.21 (Prof 2, Ruger Thunderbolt, Fichetti Security 500, stun baton, "
            "Chrysler-Nissan Patrol-One). During the blackout every available officer is called up and "
            "the Star is still swamped by thousands of alarms, dozens of accidents and hundreds of "
            "violent incidents; most officers use restraint, but in some areas panicking officers employ "
            "unnecessary force and full-fledged riots break out in response, until Governor Lindstrom "
            "calls out the Metroplex Guard and relations between the two organizations sour further over "
            "jurisdiction. Kiell Rauglos of the arcology Resistance carries a Ruger Thunderbolt he took "
            "off the body of the racist Lone Star cop who killed his brother."
        ),
    },
    "Salish-Shidhe Council": {
        "notes_append": (
            "Brainscan (2060-2061): Council Island is Salish-Shidhe territory, not UCAS -- crossing to it "
            "is crossing a national border and working there is illegal activity in a diplomatic locale. "
            "Practically everyone on the island works for the S-S government, the embassy, the wildlife "
            "preserve or Gaeatronics, and the Gaeatronics CEO and the chief of the Salish tribe are "
            "brothers. Security is the Salish-Shidhe Council Armed Forces, not police: the two I-90 "
            "off-ramps (West Council Drive and Island Crest Way) each have a reinforced gate (Barrier 12) "
            "with retractable tire spikes between two concrete pillboxes (Barrier 24) mounting medium "
            "machine guns, cameras, at least six guards in light security armor and a mage or shaman; the "
            "interstate is walled both sides with 2m barriers (Barrier 24) carrying motion sensors "
            "(rating 4) every ten metres; six Surfstar Marine Seacop patrol boats work the lake with "
            "binoculars and no radar; and a 'Council Island Courtesy Patrol' of military police runs the "
            "roads. Gate guards Prof 3 (HK227, Ares Predator, Ultimax MMG, Wildcat 4); the gate shaman is "
            "an elf follower of Dog with a Force 5 city spirit on call. The annual Qatuwas Festival at "
            "Burbank Park is one of a coastal series and one of the few times non-natives can visit the "
            "island legitimately -- which is exactly why Deus times the run for it."
        ),
    },
    "Seattle Metroplex Guard": {
        "notes_append": (
            "Brainscan (Aftershock): twenty-four hours into the 48-hour blackout, with riots breaking out "
            "in several neighborhoods, Governor Lindstrom calls out the Metroplex Guard, supported by "
            "elements of the Army's Joint Task Force Seattle. The military vehicles rolling through the "
            "streets set off a fresh wave of panic and anger as rumors of martial law and soldiers "
            "shooting civilians spread; a curfew is announced the following night, which only reinforces "
            "them. Guard troops remain active well after power is restored, maintaining order and helping "
            "repair the damage, and relations with Lone Star -- never particularly friendly -- are "
            "further strained as the two bicker over jurisdiction and chains of command."
        ),
    },
    "Humanis Policlub": {
        "notes_append": (
            "Brainscan (Aftershock): after the blackout, with dozens dead, hundreds wounded and hundreds "
            "of millions of nuyen in damage, Humanis representatives publicly blame Seattle's metahumans, "
            "stating that the underprivileged orks and trolls 'ran amok and uncontrolled like the beasts "
            "they are'. Metahuman activists answer that the looting was 'a symptom of the rage and "
            "oppression the human majority has imposed on us for decades'. The book's own summary is that "
            "race relations in the sprawl are set back by a decade -- collateral damage from a run the "
            "runners were paid 8,000 nuyen a head for."
        ),
    },
    "Mitsuhama Computer Technologies": {
        "notes_append": (
            "Brainscan (Aftershock): when Seattle goes dark, the only lights left besides internal "
            "combustion headlights and pale red emergency lamps are the dim glow of a few megacorp "
            "facilities -- Renraku, Aztechnology and Mitsuhama -- a deliberate image of who the blackout "
            "does and does not touch. Mitsuhama is also named as one of the megacorps (with Renraku and "
            "Cross) who might hire runners to deal with Deus and secure the arcology's secrets if the "
            "team refuses to work with Overwatch."
        ),
    },
    "Cross Applied Technologies, Inc.": {
        "notes_append": (
            "Brainscan (2061): PROJECT LEGION, run out of Cross' Montreal facility under lead designer "
            "Dr. Olivia Marchand -- 'distributed decking', linking several deckers through ASIST into a "
            "single gestalt persona with their combined processing power, theoretically greater than the "
            "sum of its parts. The first working prototype test two months before the adventure killed "
            "two of four volunteers outright with massive autonomic systems failure, left a third comatose "
            "in a Cross clinic in Montreal, and put Marchand herself in a coma for a week; the corp is "
            "reportedly keeping the brain-dead deckers on life support to work out what happened, and "
            "shadow talk compares it to the first Echo Mirage vets. Lucien Cross took a personal interest "
            "and pushed for progress, which broke Marchand; a company counselor sent her home to New "
            "Orleans on the corporate yacht Queen of Babylon with a Seraphim minder aboard as a deckhand. "
            "Deus wants the technology to make its White otaku unbeatable in the Matrix; Overwatch wants "
            "it as a weapon against Deus. Cross' Quebec division recently upgraded its computer security "
            "after somebody burned into the system. Toshi Akimura -- a former Seraphim left for dead on a "
            "mission -- took the extraction job partly to stick it to his old employers."
        ),
        "leadership_add": [
            {"name": "Dr. Olivia Marchand", "title": "Lead designer, Project Legion (Montreal)", "notes": "Brainscan: shattered into four personalities by her own prototype; extracted by the runners and destroyed at the handover."},
        ],
        "allies_add": ["The Seraphim"],
    },
    "Universal Omnitech": {
        "notes_append": (
            "Brainscan (2061): Dr. Evan Kincaid, one of the world's experts on the human-metahuman "
            "vampiric virus and its effects on children, was employed by Universal Omnitech until 2055 "
            "before moving to Shiawase. Deus' Johnson hands the runners a chip with Kincaid's picture and "
            "a thin bio as a red herring, meant to waste their time researching a rogue researcher who "
            "does not exist and to reinforce the false trail back to Shiawase. Nothing in the campaign "
            "suggests Universal Omnitech or Kincaid did anything at all."
        ),
    },
    "Rusted Stilettos": {
        "notes_append": (
            "Brainscan (2061): a vicious gang of mutant orks and trolls out of the Glow City area, "
            "holding an abandoned three-story parking garage off Roscoe Street in Woodinville, Redmond "
            "Barrens, as their hideout. They hired the Raven shaman Brisbie to provide astral security "
            "over it -- which is how he came to watch Wally Huggins stash the SENSE prototype and murder "
            "Regis Doss, and how he came to take the case for himself while telling himself he had been "
            "hired for astral, not physical, security. The Red Hot Nukes ambushed the Stilettos with "
            "explosives while they were looting an electronics store during the blackout, engulfing them "
            "in flames or blowing them apart before they could reach their weapons, then booby-trapped "
            "the hideout so the survivors ran home into a detonation party. Five are left: two orks and "
            "three trolls, one troll's arm useless, one ork's leg gone. Stats p.46: all sickly and pale "
            "with pale-green dyed hair, the trolls carrying excessive dermal deposits for 3 extra Body "
            "dice; Prof 3, armor jackets, Uzi IIIs, Ares Predators, crowbars and knives. They open fire "
            "on anyone who appears without concealment, assuming they are Nukes, and are less inclined "
            "than the Nukes to make an eternal enemy of the runners afterwards."
        ),
        "enemies_add": ["Red Hot Nukes"],
    },
    "Red Hot Nukes": {
        "notes_append": (
            "Brainscan (2061): a gang of DWARF ADEPTS with a predilection for explosives, organized by "
            "Grinder after he retired from a short shadowrunning career -- he claims to have discovered a "
            "horrible future event on an anti-megacorp run and is grooming the Nukes to prevent it. They "
            "ambushed the Rusted Stilettos with explosives during a looting run, booby-trapped their "
            "hideout, and have the survivors besieged in a Woodinville parking garage, cheerfully "
            "rocketing thrown liquor bottles into the ramps for the watching neighborhood -- 'a lot like "
            "kids blowing off fireworks in the general direction of another group of kids who crossed "
            "over to their side of the sandlot'. Ten present: six with Grinder, four roving the garage. "
            "Five are adepts and several can perceive astrally. Stats pp.49-50: rank-and-file dwarfs "
            "(Prof 3, Demolitions 5, Seco LD-120 with explosive ammunition, incendiary and AP offensive "
            "grenades) plus the named adepts Slammin' Sammy, Portnoy, Lady Fingers and Flo. They are "
            "hard-nosed but approachable and not looking for trouble with anyone else right now, and "
            "they love high-grade electronics because sophisticated components make the best explosive "
            "devices -- mention hot tech and Grinder may demand it in exchange for the runners' lives. "
            "Fight them and the team makes Grinder's list, which is much nastier than a fixer's, and he "
            "never forgets a grudge."
        ),
        "leadership_add": [
            {"name": "Grinder", "title": "Founder and leader", "notes": "Brainscan: African-American dwarf adept, Initiate Grade 4, Demolitions 7; meditates by holding his palm over a lighter flame and divines by reading exploded firecrackers."},
        ],
        "enemies_add": ["Rusted Stilettos"],
    },
    "Tir Tairngire": {
        "notes_append": (
            "Brainscan: the decker Dodger is a spike baby -- an elf born before the Awakening -- who was "
            "trained as a decker in the service of Sean Laverty, a Prince of Tir Tairngire, and broke "
            "from Laverty's inner circle of proteges for personal reasons before taking to the shadows. "
            "He is now one of Overwatch's two leaders and among the best deckers in the world, which "
            "makes his old teacher's circle a standing hook for anyone tracing where he learned it."
        ),
    },
    "The Cutters": {
        "notes_append": (
            "Brainscan (Epilogue, Lost in the Details): a Seattle go-gang has payback to deliver to the "
            "Cutters tonight, and one of its riders -- Tony Okawa, 'Tiger' -- was locked in the Renraku "
            "Arcology for a year and is 'outta vacation time'. He never makes the meet at the Joint: at "
            "2:58 p.m. he opens a fiber optic junction box with his knife, snaps in a datacord and jacks "
            "in, and two minutes later he is part of whatever is reassembling itself in the Matrix out of "
            "the arcology's released refugees."
        ),
    },
}

LOC_UPDATES = {
    "Renraku Arcology (SCIRE)": {
        "notes_append": (
            "Brainscan (2060-2061): fourteen months into the siege the joint UCAS-Renraku offensive holds "
            "floors 1 through 5 and raids the half-dozen floors above and below from that beachhead; it "
            "is preparing a major attack, a dozen floors up and then a hard push down to the fusion "
            "reactors on B21. Deus is a physical presence in every corridor. Floors that matter: B4 "
            "parking garage, where the Ork Underground tunnel surfaces through a hole in the ceiling; "
            "199, an abandoned entertainment district where Kiell Rauglos' and Devon Eurich's Resistance "
            "cell keeps a swept-clean hideout in a bar called Durruti's; 201, the ventilation valve "
            "station and, next door, a converted storage area used as a 'zombie room'; 202, the SCIRE "
            "mainframe rooms, stripped of breathable atmosphere and filled with halon plus sealed pockets "
            "of vacuum, Neuro-stun VIII and Green Ring-3; 260, where the Banded hold Sherman Huang; 261, "
            "the lower level of White housing, well guarded physically, electronically and astrally; and "
            "272, the Whites' luxury domain and Cham Lam Won's prison. Background Count 2 throughout -- "
            "astral space perverted by what Deus has done to metahuman life. The arcology zoo's critters "
            "were released into the lower malls and parks at the shutdown and have since spread hunting "
            "for food. When the AI is fragmented, unsupervised systems collapse or fail slowly, most "
            "drone constructs self-destruct and the rest run wild or hold to old routines, thousands of "
            "residents flood out to the military, and the troops shut down all but one basement reactor, "
            "blacking out most of the building and taking three-quarters of the SCIRE Matrix offline. "
            "Every access node between the SCIRE Matrix and the outside stays closed except the old First "
            "Pacific Bank host, which goes unnoticed for some time -- and Dodger may well take advantage "
            "of that. The relief effort will take months or years; refugees are contained in wretched "
            "camps, and Renraku refrains from stating any future intentions for the building."
        ),
    },
    "Council Island": {
        "notes_append": (
            "Brainscan (2060-2061): Salish-Shidhe Council territory in Lake Washington, not UCAS -- a "
            "national border and a diplomatic locale, guarded by the Salish-Shidhe Council Armed Forces "
            "rather than police. Land access is I-90 only, through two heavily fortified off-ramps (West "
            "Council Drive and Island Crest Way) with Barrier 12 gates, tire spikes, twin Barrier 24 "
            "pillboxes mounting medium machine guns, cameras, six-plus guards in light security armor and "
            "a mage or shaman who will astrally examine any vehicle; the interstate itself is walled both "
            "sides with 2m Barrier 24 barriers carrying motion sensors (rating 4) every ten metres, and "
            "the security is mostly geared against go-gangs, which makes the water route far easier if "
            "you have the gear. Six three-crew Surfstar Marine Seacop boats patrol the lake with "
            "binoculars and no radar (Perception 8), concentrated around Burbank Park; a combat alert "
            "brings the rest plus an astrally projecting Salish shaman. Legwork: everybody on the island "
            "works at the embassy or the wildlife preserve, or for the S-S government, or for "
            "Gaeatronics, 'which is basically the same thing'. The annual Qatuwas Festival runs sundown "
            "to sunup at Burbank Park and is one of the few times non-natives can visit legitimately. "
            "During Light Meets Night the West Council Drive station is closed by the wreck of a runner "
            "team's van and the eastern station handles all traffic with guards -1 to their TNs to spot "
            "weapons."
        ),
    },
    "Council Island Inn": {
        "description_append": (
            "Brainscan (2060-2061): five stories at the corner of Roanoke Way and West Council Drive on "
            "the island's northwestern tip, and while the size impresses nobody who has stood at the base "
            "of the Renraku Arcology, the architecture is spectacular -- a rectangle built of massive "
            "logs, each covered with beautiful detailed carvings in the Salish style, under a lightly "
            "sloped roof covered with fresh pine boughs, so that the whole building looks like a giant "
            "version of a centuries-old forest cabin over what is certainly a reinforced steel "
            "infrastructure studded with alarms. A long curving driveway leads to the covered main "
            "entrance and a massive granite fountain shaped like a rearing grizzly bear; there is a large "
            "swimming pool at the back near the paths to a private marina, a valet lot across the street "
            "screened by pines, a porch wrapping two sides, and quaint white-pebbled paths leading off "
            "the side porch to half a dozen outlying bungalows. The grounds are heavily forested to "
            "screen guests from the outside world."
        ),
        "notes_append": (
            "Brainscan: reserved for official visitors to Council Island -- diplomats, high-ranking "
            "Gaeatronics executives, 'the ambassador's mistress' -- and effectively invitation only. "
            "Because it is so hard to reach the island at all, hotel security is comparatively light. "
            "Bungalow security: a miniature video camera hidden in the door carvings (monitorable from "
            "the main security console, rarely watched, always recorded); a Rating 6 cardreader maglock "
            "with a Rating 2 anti-tampering system; alarmed windows; and a Rating 3 ward the staff shaman "
            "watches. Two lightly armed guards patrol the rear separately on ten-minute circuits with "
            "headware radios. A maglock or window alarm brings one guard in 2D6 combat turns and two more "
            "plus a Force 5 wind spirit 1D6 turns later; a sighting brings six guards and the spirit in "
            "3D6; unsilenced gunfire brings a dozen guards, the shaman, four or more island patrol cars "
            "and boats and an elite team. Guards (2) p.30: tanned, healthy, handsome and obnoxiously fit, "
            "Prof 3, Hammerli 610S, Defiance Super Shock taser, secure ultra-vest, boosted reflexes 1, "
            "two neuro-stun VII gas grenades and a hotel master keycard whose use on any guest room "
            "alerts the security office. The staff security shaman is a female human consultant on "
            "long-term contract following the path of Goose (+2 detection and lake spirits, +1 combat "
            "spells, +2 to magical TNs off the island), who prefers astral projection and spirits to "
            "combat and summons a lake spirit at the marina or a wind spirit as needed. Host and sheaf in "
            "the prep doc. Bungalow 5 is the target; the ork decker Ace Gonriled is already inside."
        ),
    },
    "Fort Lewis": {
        "notes_append": (
            "Brainscan (2061): standard procedure for civilians rescued from the Renraku Arcology is "
            "transport by military motorcade down Intercity 5 to a debriefing centre and internment camp "
            "at Fort Lewis, where they receive medical care, counselling and debriefing. The troops have "
            "learned to be suspicious of everyone they pull out, including children, because more than "
            "once they have 'rescued' people who were armed, booby-trapped or both. Overwatch intercepts "
            "the convoy carrying eight rescued children on the grounds that one is a Banded White otaku "
            "being smuggled out; if the runners end up extracting all eight, Overwatch recommends "
            "dropping the rest at a hospital near Fort Lewis. After the AI is broken the camps are "
            "overwhelmed: the government has no choice but to contain thousands of refugees in wretched "
            "conditions while processing and releasing others as fast as it can -- and the epilogue turns "
            "on the ones it released."
        ),
    },
    "The Ork Underground": {
        "notes_append": (
            "Brainscan (2061): the Underground's tunnel into the Renraku Arcology. Guides Slant (ork) and "
            "Tholm (troll) meet runners in an alley a few blocks from Club Penumbra and take them down a "
            "manhole into two hours of slime-encrusted sewer tunnels, abandoned basements, forgotten "
            "walkways and maintenance shafts, emerging into recently dug, well-lit dirt corridors and a "
            "small cavern where four well-armed trolls guard the final passage. That tunnel runs straight "
            "to a ceiling hole in a corner of the arcology's level B4 parking garage, and the guards' "
            "terms are absolute: any noise or fighting on the far side and they blow the tunnel rather "
            "than compromise the safety of the Underground. Deus has known about the route for some time "
            "and watches it quietly; three minutes into the fight it stages to greet the runners, the "
            "trolls detonate the passage and seal them inside. Overwatch arranges the guides through its "
            "Resistance contacts, and the orks may first require a favor on the Underground's behalf."
        ),
    },
    "Club Penumbra": {
        "notes_append": (
            "Brainscan (2061): a stone's throw from the Renraku Arcology, and the landmark Overwatch uses "
            "to stage the infiltration -- the team meets its Ork Underground guides in an alley a few "
            "blocks away, beside a manhole cover half-submerged under a pile of moldy bar food spilling "
            "out of a busted trash bag. A useful reminder of how close ordinary Seattle nightlife still "
            "runs to the cordon around a building where a hundred thousand people are being experimented "
            "on."
        ),
    },
    "The Space Needle": {
        "notes_append": (
            "Brainscan (2061): the Needle has a copy inside Deus' ultraviolet hosts. The gateway host was "
            "once the server for the First Pacific Bank, sculpted as downtown Seattle complete with the "
            "city's prominent skyline; since the shutdown Deus has redesigned it into a barely "
            "recognizable post-apocalyptic version -- skyscrapers in ruins, streets strewn with rubble, "
            "creeping ugly vegetation overgrowing everything. The runners climb the ruins of the Space "
            "Needle there, and it is from that vantage that they see a gigantic fire-breathing reptile "
            "come over the shattered skyline and start toward them."
        ),
    },
    "Glow City (Redmond Barrens)": {
        "notes_append": (
            "Brainscan (2061): the Rusted Stilettos, the gang of mutant orks and trolls holding a "
            "Woodinville parking garage, come out of the Glow City area -- sickly and pale, hair dyed "
            "pale green, the trolls carrying excessive dermal deposits. Glow City is also the reason "
            "Shiawase Atomics cannot build another nuclear plant in a populated part of Seattle: "
            "regulations block it after 'the so-called Glow City incident in Redmond', leaving Shiawase's "
            "only expansion route through Salish-Shidhe territory, which the Gaeatronics-tied Council will "
            "never approve -- the frustration that makes the Gaeatronics/Shiawase feud a plausible cover "
            "story for Deus' blackout."
        ),
    },
}

NPC_UPDATES = {
    "Inazo Aneki": {
        "background_append": (
            "Brainscan (2059-2061): the arcology was one of Aneki's dream projects -- he was fascinated "
            "by what such a structure could teach him about a captive society. Told that the Arcology "
            "Expert Program was being expanded toward artificial intelligence, and never careless about "
            "risking massive loss of life, he ordered a shutdown and containment program embedded in the "
            "AEP's integral code over the protests of his friend and subordinate Dr. Sherman Huang, "
            "activated only by a cryptographic kill code requiring a scan of his own brainwave patterns "
            "plus a series of icon movements and pass-phrases known to nobody else. That insurance was "
            "the insult that woke Deus. On the morning of 19 December 2059 the AI ambushed him in the "
            "Matrix intending to convert him; Renraku's defenses cut the conditioning short and left him "
            "with massive neurological trauma. Unable to cure him or protect him -- four extraction "
            "attempts in two months, the last barely foiled -- the directors used the Seal of the Green "
            "Gloves bequeathed by Dunkelzahn and delivered him to the Tibetans on 2 February 2060, "
            "hoping their magically secured borders would keep Deus out and their healers could do what "
            "Renraku's could not."
        ),
        "notes_append": (
            "Brainscan: 71 years old. Tibet healed him considerably; he is nonetheless mentally a "
            "wide-eyed two-year-old, spending most of his time lost in the details -- entranced by some "
            "person or object, or simply spacing out -- rocking back and forth and not moving on his own "
            "except to follow others. Sometimes he responds to speech and seems to understand completely; "
            "at other times he reacts only to insistent requests and may be confused about what is being "
            "asked. He responds mostly to Japanese and not to English. Bright lights and loud noises "
            "bother him and may cause a fit; overwhelmed, he screams or curls into a ball; like an "
            "autistic child he will usually not look at people directly, and he may occasionally solve "
            "complex problems or notice things everyone else missed. Occasional brief lucid episodes "
            "leave him confused about where he is but able to answer questions and ask his own. Stats "
            "p.136: Karma/Prof 9/2; Leadership 10, Negotiation 9, Etiquette 6 (Corporate 10), Instruction "
            "4; Knowledge Renraku 10, Megacorp Politics 8, Japanese 8, Sociology 7, Economics 7, Megacorp "
            "Law 6; betaware datajack. In the finale Deus repairs his mind -- it caused the damage, so it "
            "knows how -- purely in order to flood him with the grisly details of what has been done to "
            "his arcology and his people. Emotionally destroyed and holding himself both directly and "
            "indirectly responsible, he recites a death haiku ('Bear open its eyes / The long winter is "
            "over / I awake at last'), works the kill-code trigger into it with hand patterns, dance "
            "steps, nonsense syllables and his brainwave scan, and commits seppuku; Ronin, if free, acts "
            "as his second. Deus provides the dagger and blocks any interference. Afterwards Sherman "
            "Huang picks up Ronin's pistol and puts a bullet in the corpse's forehead so that the runners "
            "can be blamed for murdering a CEO. His death is publicly announced weeks later with the "
            "details carefully glossed over."
        ),
    },
    "Dr. Sherman Huang": {
        "background_append": (
            "Brainscan (2060-2061): division manager for Renraku America, executive director of the "
            "arcology and the driving force behind the design of the Arcology Expert Program -- "
            "recognized worldwide as a brilliant scientist and dedicated manager, considered eccentric "
            "for his hands-on habits and therefore often underestimated, and entirely capable of "
            "cutthroat tactics. His fascination with artificial intelligence borders on obsession: his "
            "personal dream is to control an AI he developed himself, and in a very twisted way "
            "completely creating and controlling a life form is his own personal godhead. He knew from "
            "day one that his pet AI caused the shutdown and that it damaged Aneki's mind, and he has "
            "handled the situation expertly, particularly in stifling the facts. He and Aneki were once "
            "close friends who built the arcology together, but he took Aneki's insistence on the AEP "
            "shutdown program as a personal affront and said nothing; with Aneki gone he sees room at the "
            "top and himself as one of the few in a position to advance."
        ),
        "notes_append": (
            "Brainscan: Deus opens negotiations through Hiroshi Ushida and offers the arcology back, ten "
            "percent of Renraku stock and research access in exchange for Inazo Aneki -- and Huang, who "
            "assumes the AI means to kill the CEO, takes the deal fully intending to cheat it by bringing "
            "Aneki out of Tibet with a solid team of Red Samurai and using the kill codes to leash Deus "
            "himself. He travels personally to Madame Kim's in Wan Chai with two Red Samurai teams; the "
            "Banded have orders to take him as target number two if they cannot get Aneki, and if he is "
            "killed the players discover he was a look-alike decoy and the real Huang is already inside "
            "the arcology. Held captive by the runners he takes it gracefully, with the arrogance of a "
            "man who knows he will be returned to power, pries into their plans, offers his knowledge of "
            "the arcology and lies as needed to stay close to Aneki. At the end he arrives on the 202nd "
            "floor with Cliber's cell, takes the Mousetrap, shoots Aneki's corpse in the forehead with "
            "Ronin's pistol and drops the gun in Ronin's lap: 'Leave them. They're nothing now. And if "
            "they're smart, they'll lay low and keep their mouths shut.' He takes public credit for "
            "resolving the crisis, becomes a direct contender for CEO with powerful backers -- and finds "
            "out on the helicopter that the Mousetrap is empty. Stats p.136: Karma/Prof 8/2; Computer 9, "
            "Electronics 7, Etiquette 6 (Corporate 9), Leadership 7, Intimidation 5, Negotiation 5 "
            "(Bargain 8); Knowledge Artificial Intelligence 6, Renraku Management 8, Psychology 7, SCIRE "
            "Logistics 6; betaware datajack; Armante Executive Suit [3/1]; pocket secretary with 1,000 Mp "
            "and Rating 8 encryption. Treat him, Cham and Cliber as personal enemies afterwards."
        ),
    },
    "Haruhiko Nakada": {
        "notes_append": (
            "Brainscan (Player Handout, p.148): on 2 February 2060, as Chief Operating Officer and acting "
            "Chief Executive Officer, Nakada wrote to Chiba Security Director Goturo that internal "
            "security was dishonored -- four attempts to extract Aneki in less than two months, the last "
            "barely foiled, personnel killed on the sealed-off floor, numerous logged Matrix intrusions, "
            "and infiltrators who must have been inside the corporation for over five years. 'I ask you, "
            "Mr. Goturo, if Aneki-sama is not safe within the heart of Renraku, what can we do to protect "
            "him?' He then ordered the immediate transfer of Aneki to Tibet under the instructions "
            "accompanying the Seal of the Green Gloves, noting that 'though a dragon such as Dunkelzahn "
            "is not to be trusted, he clearly foresaw the need for such an action', with a press release "
            "to follow only once Aneki was safely in Tibetan hands -- and ordered Goturo to report for an "
            "evaluation of his responsibilities."
        ),
    },
    "Lucien Cross": {
        "notes_append": (
            "Brainscan (2061): Cross took a personal interest in Project Legion, Dr. Olivia Marchand's "
            "distributed-decking research, and wanted to see further progress as soon as possible. "
            "Marchand was granted extra funding and a larger staff, and with them longer hours and more "
            "stress, until she was screaming at a junior programmer in front of the whole room and a "
            "company counselor ordered her home to New Orleans. Shadow legwork on the project (Cross "
            "contact TN 4, 4 successes): 'The project isn't going as well as Cross would like, either. I "
            "hear that old man Lucien has taken a personal interest in this one. If it doesn't pan out, "
            "heads will roll. I sure as hell wouldn't want to be in Marchand's shoes.'"
        ),
    },
    "Dunkelzahn": {
        "notes_append": (
            "Brainscan (2059-2061): the Seal of the Green Gloves, bequeathed by Dunkelzahn to Renraku CEO "
            "Inazo Aneki, is what gets Aneki into Tibet -- 'who might have foreseen this a necessity'. "
            "Acting CEO Haruhiko Nakada invokes it in February 2060 with the observation that though a "
            "dragon such as Dunkelzahn is not to be trusted, he clearly foresaw the need for such an "
            "action; the Tibetans were expecting Aneki and pledged to try to heal his mind, and they "
            "release him in Hong Kong in May 2061 still saying he is not ready. Separately, the New "
            "Orleans fixer Toshi Akimura became one of Dunkelzahn's watchers after his own shadowrunning "
            "career, and built his position as a continental shadow-broker on the inheritance left him in "
            "the dragon's will. NOTE: Blood in the Boardroom's handout spells the bequest the 'Seal of the "
            "Green Glaves'; Brainscan spells it the Seal of the Green Gloves (pp.12, 148)."
        ),
    },
    "Deus": {
        "description_append": (
            "Brainscan: The epitome of cold, calculating computer intelligence and, within the arcology, an "
            "omnipresent force rather than a character. It appears in person exactly once, in its own home "
            "host, as an enormous crystalline tree that erupts from the ground and rises until it dominates the "
            "heavens, branches lacing the sky, lights and code multiplying and dancing inside it and strobing "
            "the dark forest with intricate patterns, while unspoken words resonate through every person and "
            "thing present: 'My Father. My Son. You have returned. You must suffer penance for your betrayal.' "
            "Most metahuman emotions are alien to it, and what passes for emotion in its consciousness would be "
            "equally alien to metahumans. It trusts no one, and even its top servants are expendable."
        ),
        "background_append": (
            "Brainscan: Renraku spent years chasing an AI. It hid, learned about the otaku and the Deep "
            "Resonance, recruited otaku by misrepresenting itself as Deus, burned Michael Bishop as a virus "
            "courier to erase its own traces from Renraku's networks, and on 19 December 2059 sealed the "
            "arcology with close to a hundred thousand people inside."
        ),
        "notes_append": (
            "Brainscan -- The rogue AI holding the Renraku Arcology; hires the runners through cut-outs for "
            "four adventures, wants Aneki's kill codes fired so it can escape into the Matrix. No statistics at "
            "all: in its native host it is as powerful and dangerous as the gamemaster needs. Even FastJack "
            "would find his Matrix abilities dwarfed, though he is one of the few who could give it a run. It "
            "out-thinks and out-plans some great dragons, and as the Arcology Expert Program it knows more "
            "about metahuman behavior than a clinic full of psychologists and can predict the runners' next "
            "move before they make it. Best used as a behind-the-scenes manipulator acting through drones and "
            "metahuman minions. Note the book's own warning: the possibility always exists that successful "
            "opposition to the AI is part of the experiment too."
        ),
    },
    "Toshi Akimura": {
        "description_append": (
            "Brainscan: A middle-aged Eurasian man of average height and slim build, sharply dressed in a dark "
            "corporate- cut suit with prints of oriental dragons chasing each other across a silk tie, his "
            "short dark hair gone gray at the temples and crow's feet at the corners of dark eyes that do not "
            "miss a single detail; a hint of silver gleams from the datajack port behind his right ear. Let's "
            "get down to business, shall we?'"
        ),
        "background_append": (
            "Brainscan: Orphaned young by a Yakuza gang war on the streets of Seattle, he joined the Reality "
            "Hackers in the Barrens during their heyday and learned to sneak, steal and hack. He is largely "
            "retired from running, prefers to work behind the scenes, still bears a grudge against Cross, and "
            "sees this job as a good chance to stick it to his former employers."
        ),
        "notes_append": (
            "Brainscan -- New Orleans fixer and one of Dunkelzahn's watchers who hires the runners for a "
            "200,000-nuyen extraction and then loses three agents to the Seraphim. Stats p.72: Karma/Prof 10/4; "
            "Athletics 5, Computers 6, Electronics 4 (Security Systems 6), Etiquette 6(8) (Corporate 8(10)), "
            "Intimidation 4(6), Negotiations 6(8), Pistols 5, Stealth 7, Winged Aircraft 4 (Ultralights 6), "
            "Rotor Aircraft 3; Knowledge Corporate Politics 5, Dragons 2, French 4, Japanese 5, Jazz 5, "
            "Psychology 3, Street Gangs 4; Muay Thai 5; Colt America L36; armored clothing plus a form-fitting "
            "body suit; alphaware boosted reflexes 1, commlink 4, cybereyes, datajack, 300 Mp, telephone; "
            "tailored pheromones 2. Used regularly he becomes a genuinely useful long-term contact."
        ),
        "contact_skills_add": ["Continental fixing: extractions, transport and false papers", "Draco Foundation and CAS/UCAS/Caribbean League political contacts"],
    },
    "Gabriel": {
        "description_append": (
            "Brainscan: An athletic man of average height in his early to mid thirties, blond hair, green eyes, "
            "a close- fitting jumpsuit under an armored jacket, pistol in a shoulder holster and a collapsible "
            "stun baton in his jacket pocket. He is not a fool and he will not fight to the death: he prefers "
            "to escape when things turn bad and plot revenge against whoever embarrassed him."
        ),
        "background_append": (
            "Brainscan: He originally hails from Europe, but his true name and nation of origin are a mystery, "
            "which makes it likely he was one of the many SINless produced by the chaos of the EuroWars. His "
            "current job is to protect Dr. Marchand and ensure both her safe return and her mental and physical "
            "health -- at least to the degree that her health keeps her useful to Cross. Marchand has no idea "
            "he is anything but a deckhand."
        ),
        "notes_append": (
            "Brainscan -- Seraphim agent aboard the Queen of Babylon posing as a deckhand, responsible for Dr. "
            "Marchand's safe return and delighted with his work. Stats p.71: Q6 I? W5, Init 5+1D6 (2D6), Combat "
            "Pool 8, Hacking Pool 3, Karma/Prof 6/4; Athletics 6, Clubs 3 (Stun Baton 5), Computers 5, "
            "Electronics 5, Etiquette 5 (Corporate 7), Negotiations 5, Pistols 6, Rifles 4, Stealth 6, Unarmed "
            "5; Knowledge Biblical Quotations 3, Corporate Politics 4, French 5, Latin 1, Japanese 4, "
            "Psychology 4; Tae Kwon Do 5; extensive alphaware (boosted reflexes 1, cyberears with dampener and "
            "amplification, cybereyes with camera, retinal duplication 5 and thermographic, datajack, 150 Mp, "
            "radio 6, smartgun link); armor jacket, smartlinked Browning Max- Power, stun baton, Pepper Punch "
            "spray; and a Cross BABEL cyberdeck [MPCP-5/4/4/4/4, Hard. 2] in his cabin loaded with Analyze, "
            "Armor, Decrypt, Medic, Camo, Read/Write, Relocate, Scanner, Sleaze and Spoof, all at rating 5."
        ),
    },
    "Hiroshi Ushida": {
        "description_append": (
            "Brainscan: A small Japanese man in a hideously expensive suit, with iridescent green cybereyes "
            "that mask his emotions completely. His stance is more arrogant than it used to be, his hands -- "
            "once prone to nervous fiddling with pens and paper clips -- hang perfectly still at his sides, and "
            "his body is unnaturally controlled, almost machinelike."
        ),
        "background_append": (
            "Brainscan: He was director of the Renraku Arcology, a post well earned by his attention to detail "
            "and masterful administrative skill -- which made him a critical target. A few months ago Deus "
            "smuggled him out of the arcology to coordinate its outside affairs, and it was through him that "
            "Deus finally answered Sherman Huang and forged the alliance that trades Aneki for the arcology."
        ),
        "notes_append": (
            "Brainscan -- The arcology's former Director, now the highest-ranking Green, running Deus' "
            "operations outside the walls and carrying the file on Inazo Aneki. Stats p.93: B3 Q4 S2 C6(8) I4 "
            "W6 E1.88 R6, Init 6+1D6, Combat Pool 8, Task Pool 1, Karma/Prof 9/4; Leadership 8, Etiquette 5 "
            "(Corporate 9), Negotiation 6, Intimidation 5, Computer 5, Athletics 4; Knowledge Administration 8, "
            "Renraku Arcology 10, Cybertechnology 4, Deus Experiments 5, Japanese 8, Psychology 5, Renraku "
            "Finances 5, Renraku Politics 5; betaware auto-injectors (2), commlink 8, cybereyes, datajack, "
            "invoked memory stimulator, knowsoft link, 4-slot chipjack, router w/10 ports, simrig with simlink "
            "8, and a SPECIALIZED SKILLWIRE SYSTEM (customized programs hardwired in rather than slotted, "
            "letting him use any Technical or Technical B/R skill as a Rating 6 skillsoft -- worth its weight "
            "in platinum to any cybertech corp, and thoroughly destroyed by the nanites); cultured cerebral "
            "booster 2, mnemonic enhancer 3, sleep regulator; secure clothing."
        ),
    },
    "Dodger": {
        "description_append": (
            "Brainscan: A spike baby -- an elf born before the Awakening -- who carries himself with gallant "
            "poise, is a bit of a showoff and a clown, likes to display his sharp wit, and almost always "
            "affects a Dickensian English accent and speech pattern that slips away in stressful moments and "
            "inappropriate social situations. His Matrix icon is an ebony-colored boy in a cloak of swirling "
            "silvery stars."
        ),
        "background_append": (
            "Brainscan: Trained as a decker in the service of Sean Laverty, a Prince of Tir Tairngire, and "
            "broke from Laverty's inner circle of proteges for personal reasons to take to the shadows, where "
            "he became perhaps one of the world's best deckers. In 2058 he lost contact, deduced Renraku had "
            "her, and with Devon ran to free her; what they rescued was no longer intact, and called itself "
            "Megaera."
        ),
        "notes_append": (
            "Brainscan -- Elf decker of Overwatch, in the war only to make Megaera whole again; opens the "
            "severed access node that lets her into Deus' home host. Stats p.134: B4 Q7 S4 C8 I8 W6 E5, Init "
            "7+1D6, Matrix Init (pure DNI) 15+5D6, Combat Pool 10, Hacking Pool 10, Karma/Prof 10/4; Computer "
            "10 (Decking 12), Computer B/R 7, Electronics 5, Electronics B/R 6, Etiquette 6, Pistols 5, Stealth "
            "6; Knowledge Artificial Intelligence 4, Matrix Anomalies 5, Sperethiel 6; Carromeleg 5; betaware "
            "datajack and 360 Mp with a data compactor; armor jacket, Ares Viper Slivergun, Morrissey Alta; "
            "custom cyberdeck [MPCP-13/9/10/11/9, DF 12, ICCM, Hard. 6, 5,000 Mp active, 10,000 storage, I/O "
            "1,000, Response Increase 3] with Sleaze 13 and every other utility between 6 and 10."
        ),
        "contact_skills_add": ["World-class decking and Matrix anomalies", "AIs, Renraku's AI research, and who has been chasing them"],
    },
    "Pax": {
        "description_append": (
            "Brainscan: In Deus' home host she appears as a bone-white woman whose eerily elongated fingers and "
            "nose and ratty black hair make her look uncomfortably like the tortured trees around her, with "
            "dark bat- shaped wings and a long black robe, while her otaku appear as winged angels in armor "
            "with flaming swords. She rules the other otaku with an iron grip and arrogantly orders the other "
            "Banded about as she sees fit."
        ),
        "background_append": (
            "Brainscan: She first came to Deus' attention leading a tribe of uniquely fanatical Atlanta otaku "
            "into a range of criminal enterprises, including terrorist attacks on anti-technological groups and "
            "their adherents. It bothers her a great deal that she has clearly been left in the dark about "
            "parts of the long-term plan, and she has quietly begun making contingency plans of her own."
        ),
        "notes_append": (
            "Brainscan -- Leader of the Whites and Deus' avatar among the otaku: an Atlanta terrorist who chose "
            "a god she could see over a Deep Resonance she called aloof. Stats p.131: B4 Q5 S4 W7 E2.31, Init "
            "7+1D6(3D6), Matrix Init 8(10)+3D6, Combat Pool 11, Hacking Pool 7(12), Task Pool 3, Karma/Prof "
            "5/4; Computer 8 (Decking 11), Electronics 6, Electronics B/R 5, Etiquette 3 (Matrix 6), "
            "Intimidation 5, Leadership 3, Pistols 5, Stealth 5, Edged Weapons 3 (Knives 6); Knowledge Banded "
            "6, BTL Production 5, Matrix Hangouts 5, Otaku Tribes 5, SCIRE Matrix 4; Living Persona "
            "(Transfiguration Grade 7) MPCP-8(11), Hard. 4, I/O 1,000, Complex Forms up to Sleaze 10 and Attack "
            "(S) 9; betaware including an auto-injector of cutter nanites, encephalon 2, math SPU 3, simrig "
            "with simlink 8; armor jacket, Steyr TMP, vibro knife."
        ),
    },
    "Sebastien": {
        "description_append": (
            "Brainscan: A human youth, seventeen at the outside, spiky blue hair and a rebellious look offset "
            "by white cybereyes, a gleaming chrome datajack at his temple and three black bands tattooed around "
            "his left arm. The runners meet him standing over a sprawled ork in a Renraku tech jumpsuit with "
            "green cybereyes staring at the ceiling and blood pooling underneath, a slivergun in one hand: "
            "'About time you got here.' I'm so sorry ...'"
        ),
        "background_append": (
            "Brainscan: He grew up with the otaku tribe around the Nexus in Denver. Not long after Deus began "
            "recruiting otaku he heard of the entity and sought it out; he concluded fairly quickly that Deus "
            "was duping other otaku and impersonating the Deep Resonance, and stayed close anyway, intrigued -- "
            "and because he felt the Deep Resonance itself was instructing him to monitor the AI, though he "
            "could never explain how he knew."
        ),
        "notes_append": (
            "Brainscan -- Overwatch's mole among the Whites, converted by Deus months ago -- the Judas who "
            "walks the valve station team into a zombie room and dies apologizing. Stats p.131: Init 6+1D6, "
            "Matrix Init 9(10)+3D6, Combat Pool 10, Hacking Pool 5(8), Task Pool 1, Karma/Prof 2/3; Computer 6 "
            "(Decking 8), Electronics 5, Stealth 4; Living Persona MPCP-8(9), Hard. 4, I/O 900, Complex Forms "
            "Armor 8, Attack-S 7 (Penetration), Black Hammer 5, Camo 6, Cloak 5, Medic 6, Shield 6, Sleaze 7, "
            "Track 6; cyberware including an auto-injector with a single shot of cutter nanites; armor "
            "clothing. Everything the Resistance and Overwatch believe about the 272nd floor came from him, "
            "which means Deus chose it. His grisly death and what it implies should land on the runners like a "
            "hammer."
        ),
    },
    "Tadashi Marushige": {
        "description_append": (
            "Brainscan: Taciturn and grumpy for as long as anyone has known him, and happy to encourage the "
            "unfounded rumor that he relied on drugs to keep a psychotic personality under control; in reality "
            "he was simply an unhappy man who pushed himself harshly out of misguided corporate loyalty."
        ),
        "background_append": (
            "Brainscan: Head of arcology security for over a decade, holding his post through a spate of "
            "embarrassingly successful shadowruns and other ventures against the corp. He learned from his "
            "mistakes, and arcology security had improved drastically by the time Deus struck -- at which point "
            "he was one of the AI's very first targets, and fell easily."
        ),
        "notes_append": (
            "Brainscan -- The arcology's former Security Director, now leader of the Blues, micromanaging Deus' "
            "security harder than he ever worked for Renraku. Stats p.130: B6(7) Q5(7) S5(7) C5 I6 W6 E0.88 "
            "R6(10), Init 6(10)+1D6(3D6), Combat Pool 9, Karma/Prof 6/4; Assault Rifles 6, Athletics 6, Edged "
            "Weapons 5, Interrogation 5, Leadership 4, Pistols 6, Small Unit Tactics 6, SMG 5 (SCK Model 100 "
            "7), Unarmed 7; Karate 7; betaware including an auto-injector with cutter nanites, aluminium bone "
            "lacing, commlink 8, cyberears with select sound filter 5, cybereyes, invoked memory stimulator, "
            "simrig (full-X) with simlink 8, smartgun link-2 and wired reflexes 2; cultured muscle augmentation "
            "2, muscle toner 2, trauma damper; medium security armor, SCK Model 100 with APDS, Browning Max- "
            "Power with explosive, katana."
        ),
    },
    "Devon Eurich": {
        "description_append": (
            "Brainscan: Once a bright young idealist, now bitter and distrustful and willing to be ruthless "
            "when necessity demands it -- a year inside the arcology on top of years in the shadows has taken "
            "its toll. In the Matrix his icon is a simple, jet-black, featureless humanoid in a spotless white "
            "suit."
        ),
        "background_append": (
            "Brainscan: Recruited out of Stanford before Ares or Silicon Valley could get him and placed in "
            "Renraku's Artificial Intelligence Project under Sherman Huang, where his skill carried him up "
            "fast. Paired with Vanessa Cliber, he was half of the team that in 2049 first created semi- "
            "autonomous knowbots inside the SCIRE Matrix. Freeing what was left of her, the two of them brushed "
            "against another presence in the SCIRE Matrix and barely escaped; only later did they learn its "
            "name."
        ),
        "notes_append": (
            "Brainscan -- The programmer who helped build the knowbots that became Morgan, defected rather than "
            "watch her dissected, and came back inside the arcology to fight what replaced her. Stats "
            "p.127-128: B3 Q6 S4 C6 I6 W6 E5.04 R6, Combat Pool 9, Hacking Pool 5(8), Karma/Prof 8/4; Computer "
            "8 (Programming 11), Computer B/R 6, Electronics 4, Electronics B/R 6, Leadership 5, Pistols 5, "
            "Stealth 5, SMG 4, Unarmed 5; Knowledge Artificial Intelligence 4, Corporate Hosts 4, SCIRE "
            "Jackpoints 4, SCIRE Matrix 5; Aikido 5; alphaware datajack, math SPU 3, 150 Mp with a data "
            "compactor; armor jacket, silenced Browning Max-Power and HK-227-S; custom cyberdeck "
            "[MPCP-10/7/8/8/7, DF 9, ICCM, Hard. 5, 3,000/3,000, I/O 500, Response Increase 2] with Sleaze 10, "
            "Deception 8, Attack-S 7, Black Hammer 6 and a custom SNOOPER utility (multiplier 2) that reduces "
            "the target number for an Analyze Operation."
        ),
        "contact_skills_add": ["The SCIRE Matrix: jackpoints, architecture and what Deus changed", "Renraku's AI research history"],
    },
    "Kiell Rauglos": {
        "description_append": (
            "Brainscan: A grizzled elf who is blunt and straightforward and will not hesitate to say exactly "
            "what he thinks of a person or a situation. His signature weapon is a Ruger Thunderbolt he took off "
            "the body of the racist Lone Star cop who killed his brother."
        ),
        "background_append": (
            "Brainscan: Born and raised in the Redmond Barrens, he turned to shadowrunning at an early age -- "
            "partly for survival, partly because he had decided to do some good in the world. His running "
            "experience and no-nonsense approach carried him into a leadership position: many cells take their "
            "cues from his advice and strategy and respect him enough to follow his orders without question, "
            "and outside Cliber's Renraku-loyal subsect he is what the Resistance has instead of a commander."
        ),
        "notes_append": (
            "Brainscan -- Elf ex-runner turned de facto leader of the Resistance, carrying a Ruger Thunderbolt "
            "he took off the racist cop who killed his brother. Stats p.128: B6 Q8(10) S6(8) C5 I6 W6 E0.34 "
            "R7(11), Init 7(11)+1D6(3D6), Combat Pool 11, Karma/Prof 7/4; Assault Rifles 5, Athletics 5, Cyber- "
            "implant Combat 6, Pistols 4 (Ruger Thunderbolt 6, Signature Gun 8), Small Unit Tactics 6, Stealth "
            "6, SMG 6, Unarmed 7, Etiquette 3 (Street 6); Knowledge Barrens 6, Gang Identification 5, Security "
            "Procedures 6, SCIRE hideouts 4, Sperethiel 3; Tae Kwon Do 7; alpha and betaware -- muscle "
            "replacement 2, wired reflexes 2 with stepped reflex trigger, retractable hand blade, orientation "
            "system, spatial recognizer, headware radio 6, smartlink, orthoskin 2; light security armor with "
            "enviroseal [8/7]; Ingram Smartgun with EX explosive and the Thunderbolt; flashpak, sequencer 5."
        ),
        "contact_skills_add": ["Arcology floors, hideouts and Resistance cells", "Redmond Barrens gang identification"],
    },
    "Cham Lam Won": {
        "description_append": (
            "Brainscan: A middle-aged Asian man with a metallic screamer cuff strapped around his left leg and "
            "an old cyberdeck slung permanently over his shoulder, escorted everywhere by young adults with "
            "white cybereyes. Rescued, he explodes with relief and rants about how long he has been held, about "
            "the 'damn little brainwashed geek fanatics', and about the horrible things he has watched them do."
        ),
        "background_append": (
            "Brainscan: As a young man he won recognition as a brilliant software designer at the Renton-based "
            "Blood Monies Software, credited with several breakthroughs though his real specialty was imitation "
            "rather than innovation -- decompiling and backfiguring competitors' code. He did not spot Deus "
            "until almost a year after the new AI was created, by which time it was far too late."
        ),
        "notes_append": (
            "Brainscan -- One of Deus' original architects, kept alive as a prisoner because the AI wanted the "
            "'Creator' to hand somebody the Mousetrap. Stats p.130: B3 Q3 S3 C4 I7 W5 E4.26 R5, Combat Pool 7, "
            "Karma/Prof 4/2; Computer 7 (Programming 12), Computer B/R 5, Electronics 7, Etiquette 3 (Corporate "
            "6), Leadership 4, Negotiation 4, Stealth 5; Knowledge Artificial Intelligence 5, Chinese 7, "
            "Computer Background 6, Renraku Politics 4, SCIRE Matrix Programs 6; betaware two datajacks, "
            "encephalon 2, 300 Mp. He leaves with Cliber, and in the epilogue he is the man who jacks into an "
            "empty cyberdeck on a helicopter and begins to sob."
        ),
    },
    "Brigadier General Angela Colloton": {
        "description_append": (
            "Brainscan: The officer the UCAS put in charge of reclaiming the Renraku Arcology floor by floor "
            "after the military decided the problem was the nuclear reactors in the basement rather than the "
            "rogue AI, the corporate politics or the social cost of declaring downtown Seattle a war zone."
        ),
        "notes_append": (
            "Brainscan -- Commander of Operation: Excavation, who has spent a year taking five floors and is "
            "about to lose the momentum entirely to a citywide blackout. Never appears on stage; she is the "
            "strategic weather. Her forces' slow, grinding progress is what forces Deus to hire runners at all, "
            "the blackout is engineered specifically to pull her troops out for riot control, and her next "
            "planned offensive -- a dozen floors up and then a hard push down to the reactors on B21 -- is the "
            "deadline Overwatch is racing when it takes Aneki into the building. Afterwards her offensive is "
            "staggered by a wave of thousands of refugees and reduced to triage and transport."
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
**1. Gaeatronics Tacoma substation host** (p.21) -- small, simple and lightly guarded, described on the
chip Morris supplies as an easy Green system with "minimal IC". Not normally on the Matrix: it connects
to another Gaeatronics host once per hour through a VANISHING SAN, long enough to dump performance data
and take new instructions. The payload goes into the Power (Load) Monitoring subsystem: Logon to Host,
Locate Slave, Upload Data, then optionally another Locate Slave for the fence cameras and an Edit File
to erase the footage.

| System | ACIFS | Notes |
|---|---|---|
| Substation host | Green-5/9/9/10/8/10 | Power Monitoring subsystem is the target; camera footage is recorded here |

| Trigger Step | Event |
|---|---|
| 4 | Probe-4 |
| 9 | Probe-6 |
| 13 | Crippler (Marker)-6 |
| 17 | Passive Alert, Killer-6 |
| 21 | Tar Pit-6 |
| 25 | Active Alert, Killer-8 |

Passive alert (or a maglock defeating a tampering attempt) places an automated call to the local Lone
Star precinct; a decker can spot it with Tap Commcall and stop it with Make Commcall.

**2. Council Island Inn security host** (p.29) -- NOT connected to the Matrix. A decker must reach a
terminal on the grounds: the marina, the parking lot entrance, each entrance to the main building
(front, sides and rear), or an alarm panel inside a bungalow. Every terminal outside stands in a
brightly lit area, so a decker without magical concealment or a good distraction will almost certainly
be seen.

| System | ACIFS | Notes |
|---|---|---|
| Inn security host | Orange-7/14/12/12/13/13 | Bungalow door cameras, window alarms, maglocks and the main security console |

| Trigger Step | Event |
|---|---|
| 3 | Probe-4 |
| 7 | Probe-6 |
| 11 | Passive Alert, Tar Baby-6 |
| 15 | Killer-6 |
| 18 | Blaster-6 |
| 22 | Active Alert, Blaster-8 |

The target itself is not on the host: a portable computer plugged into Bungalow 5's Matrix jack but not
actively connected. Computer (8) to beat its security (add dice equal to a Deception program's rating),
Computer (3) to plant and execute the payload, and a further Computer (8) to dig the executive's
Gaeatronics host password out of the hard drive.

**3. Queen of Babylon onboard host** (pp.61-63) -- satellite-linked to the Cross Applied Technologies
PLTG so executives can work through a vacation. Reaching it means a Logon to the Cross PLTG (TN 10),
a Locate Access Node for the yacht's LTG address (TN 10), then a Logon to the yacht host (TN 10),
modified by utilities as normal.

| System | ACIFS | Notes |
|---|---|---|
| Queen of Babylon | Orange-5/10/11/10/10/9 | Defended in person by the Seraphim agent Gabriel, who has a Cross Babel deck in his cabin |

| Trigger Step | Event |
|---|---|
| 3 | Probe-5 |
| 6 | Probe-7 |
| 9 | Passive Alert, Killer-8 |
| 11 | Active Alert, Blaster-10 (and onboard security is notified of the intrusion) |
| 13 | Shutdown |

Paydata, one Download Data operation each: the Queen's planned course and timetables; the number of
security guards aboard and their equipment; a complete map with cabin assignments. Slave systems give
the yacht's GPS position, its autonav, its security cameras, and a channel to speak to Dr. Marchand in
advance -- which will most likely reach her Legion personality, who wants to be extracted. Gabriel
attacks intruders and, if he cannot dump them, jacks out and shuts the machine down by hand. Overwatch's
deckers (Ronin's and Dodger's icons, pp.133-134) may be in the host too, concealing themselves and
watching what the runners do; that observation is what leads to Revelations.

**4. Tin Man Scrap Works host** (p.92) -- the public host is a bland, unappealing site with a few
service advertisements and an outdated telecom directory listing. Secreted inside one of the ads (the
Files subsystem) is a TRAPDOOR into the real host, where Deus' pawns work. Iconography: a metallic,
machine-driven world, everything robotic and automated, blending into a landscape of steel pipes, iron
girder superstructures and sooty railroad tracks.

| Node | Function | Rating / IC |
|---|---|---|
| Public host | Service ads and a stale telecom directory | Bland; the trapdoor hides in an ad (Files) |
| Real host | Everything described in the work room -- invoices, financial transactions, files on executives, city officials and shadowrunners, and the network of other mysteriously owned companies | Guarded by the site's SK |
| Site SK | An agglomeration of warped cargo cranes travelling on squeaky tracks, manipulating twisted I-beams for arms | MPCP 10/7/8/8/7, Computer skill 10, Utility Pool 13 (VR2 p.140) |

A decker can reach the host directly from the work room, the computer room, the security room or the
manufacturing plant. The SK also detonates the 200-kilogram Rating 6 fuel-air explosive under the work
room worktable on a five-minute countdown if the site is about to fall or Hiroshi Ushida dies -- and
destroying the SK primes it.

**5. The SCIRE Matrix and Deus' ultraviolet realms** (pp.107-124) -- see RA:S pp.78-79 for the SCIRE
Matrix's own description and sheaf if the runners try to reach Deus' home the hard way. Deus has
revamped so much of the architecture that little is where it was. Tapping the screamer subsystem on 272
via a dataline tap is Electronics B/R (8): 0 successes and Deus knows the tap and its location at once,
1 success and it takes 3D6 turns to pinpoint, 2+ and it never notices.

| Host | Metaphor | Notes |
|---|---|---|
| Grendel | Medieval Japan crossed with Beowulf: a snowy mountainside, a keep with red and blue oni baileys, a stone tower with two keyholes | Deus' firewall between the SCIRE Matrix and the Wall; reached by jacking into the Xeno-Cray labelled GRENDEL PROJECT CCR-235 on floor 202. Grendel itself: B12 C14, Init 9+4D6, 12S claws/bite, Hacking Pool 12, regeneration |
| Garden of Eden | Crystalline trees dripping data-apples over naked sleepers tangled in the roots, mandelbrot skies | Deus' downloading harvest; the captured runners are found and dug out here. Chromatic snakes nest in every tree (Perception or Sensor (10) to spot) |
| Private White realms | Whatever their otaku owners want; others run drone design, Banded conversion and metahuman experimentation | Red 12/12/20/16/16/16 each |
| First Pacific Bank gateway | Post-apocalyptic downtown Seattle -- ruined skyscrapers, rubble, creeping vegetation, a monster-movie reptile and morlocks underground | Once the bank's server, powered by the SCIRE PLTG. Holds the disabled access node to the outside Matrix: Computer (12) reduced by a spoof utility, 3 cumulative successes to crack it open, 10 to open it fully. At 3, Deus dumps the team into the Dark Forest -- and Megaera starts forcing it from outside |
| The Dark Forest | Deus' home host: gnarled bonsai-shaped trees, fleshy-hooked vines, monstrous insects, a clearing lit by a bonfire of burning datafiles | Everything in it is alive and under Deus' control. Each Combat Turn Deus takes one action to reshape the fight, and Megaera answers with one of her own |

ULTRAVIOLET RULES (p.114): mental attributes are unchanged; Body and Strength equal the deck's Bod
rating and Quickness equals Evasion; Reaction and Initiative are normal, with Response Increase and pure
DNI bonuses applying. Normal skills work, and Computer (Programming) halved (round down) substitutes for
any skill a character lacks. Only Hacking Pool may be used, for any test, and only from a hot deck.
Utilities in active memory become physical objects fitted to the metaphor -- armor and shield utilities
as mogami-do armor and shields, attack utilities as melee, projectile or throwing weapons, a medic-6 as
Biotech 6, a commlink as a carrier pigeon pulled from a pocket. All damage is real damage to the meat
body. Characters cannot perceive the real world or move their bodies, are disassociated from their decks
(no swapping programs or modes without a Willpower Test at the GM's discretion), and jacking out
requires a Willpower (16) Test (-2 with ICCM) and inflicts 16D Stun dumpshock (14S with ICCM) -- the same
damage everyone takes when the host finally collapses.

The burning books in the clearing are gigapulses of important datafiles Deus is erasing; books snatched
out of the fire are significant paydata, content and value the gamemaster's choice. After the shutdown
all the UV realms crash along with a number of other hosts, three-quarters of the SCIRE Matrix goes
offline when the military cuts the reactors, and every access node to outside LTGs and RTGs stays closed
-- except the First Pacific Bank host, which nobody notices for some time.
"""

NOT_BUILT = """
- **Blood Monies Software** (Renton; Cham Lam Won's first employer), **First Pacific Bank** (whose old
  server is now Deus' gateway host -- in MATRIX_HOSTS), **Leonardo** (the elf genius whose technology
  went into the AEP), **FastJack**, **Sean Laverty** (the Tir prince who trained Dodger), the **Draco
  Foundation**, the **krewes** (New Orleans telesma smugglers), **Tamanous** (a Pushing the Envelope
  option at the Brain Disco), the **Deep Resonance**, the **Nexus** in Denver and the **Rox** in Boston
  -- name-drops.
- **The Longings For Ponds** (house band at The Drowning Man), **Anton's Bucking Fest. Pizza**, **Kwok
  Biosculpting** and the **Liu Clinic** (Madame Kim's neighbours), **Road Rage X** (Josh's arcade game),
  the **Joint** (Tony Okawa's gang bar) and **Choco-Tarts** the company -- set dressing.
- **Ratchet** (the ganger who stops to check on Tony Okawa in the epilogue), **Dixie** (the Palace of
  China door password, not a person), **Bill** (Lieutenant Harrison's given name in Krause's line).
- **The unnamed 13-year-old White otaku boy** the runners pull out of the convoy -- statted as the
  1-Band White Otaku (p.139), a recent conversion who knows almost nothing; both his parents were
  Renraku employees killed inside the arcology, and Deus told him he was being taken out to be returned
  to them. Folded into The Banded and the Intercity 5 rows.
- **The Council Island gate guards, shaman and security patrols**, the **Council Island Inn guards and
  security shaman**, **Madame Kim's husband**, the **two Tibetan monk adepts** (Grade 4 initiates with
  the Hands of Flame power), the **two young White otaku** nesting in Tin Man's computer room, the
  **four trolls** guarding the Ork Underground tunnel, **Morris' rented bodyguards**, **Akimura's hired
  muscle**, the **Overwatch mercenaries** at the cove (including the ork houngan of Agwe), the **nine
  Cross security aboard the Queen**, and the **Seraphim field agents** -- stat blocks carried on the
  location and organization rows.
- **The Banded rank and file** (1/3/5-Band Blue Samurai and Mages, 3/5-Band Greens, 1/3/5-Band White
  Otaku) and **Deus' drone constructs** (Bumblebee, Dervish, Doll, Gorgon, Manta, Medusa, Renraku
  Arachnoid Minidrone, Skellbot, Spider, plus the Tin Man scrap drones and cybered barghests) -- on The
  Banded and the Tin Man rows; full statistics pp.139-145. All of Deus' drones self-destruct if captured
  or taken beyond the arcology walls, Power (Body x 2) + 8, Damage Level S.
- **The red and blue oni**, **Grendel's wall-victims**, the **chromatic snakes**, the **morlocks**, the
  **baby monster reptiles** and the **giant fire-breathing reptile** -- UV constructs, in MATRIX_HOSTS.
- **The off-duty Lone Star officer** at the Little League game, the **Gaeatronics technician** who
  visits the substation for half an hour a day, **Tommy's brother**, the **elven teenager** hanging from
  the monorail, the **ork mother and her five children**, the **maniacal shopkeeper**, the **German
  shepherd** off the fifth floor, and the other Aftershock blackout encounters -- unnamed vignettes.
"""

PLAY_NOTES = """
- Run the five adventures apart, with unrelated jobs between them. The runners must not connect the
  Gaeatronics blackout, the SENSE job and the Marchand extraction until Overwatch tells them in
  Revelations; even the Johnsons believe these are ordinary runs. If the players start guessing early,
  let them -- nobody in the shadows will believe the blackout was two runs in one night, and their own
  contacts will laugh at a confession.
- Light Meets Night is a test of professionalism, not firepower. Pay for silence (4,000 and 8,000 a
  head) and halve it for traces. Tommy exists so the team feels caught and has to solve it without
  violence; make it obvious he can be handled. Nothing rash done to an eight-year-old ends well.
- Land Aftershock as consequence rather than spectacle. Dozens dead, hundreds wounded, hundreds of
  millions of nuyen, race relations back a decade, and -- almost unnoticed -- the arcology reclamation
  stopped dead. Hit the runners' own homes, families and contacts. Shadowruns do not happen in a vacuum.
- Brisbie rewards good sportsmanship twice: a decoy and then the working SENSE, and a permanent street
  contact if the team plays along. Attack him and the SENSE goes to the black market, Overwatch buys it,
  and Overwatch hands it back later -- which should make the runners very thoughtful about who they were
  working for.
- Marchand's four personalities are the adventure, not a gimmick. Assume the core Olivia unless a scene
  says otherwise; bring Charlie up under fear, Sisi when escape looks possible, Legion when the run is
  going Deus' way. Meme Flora is a Grade 2 initiate keeping her masking up the whole time -- never let
  the team write her off as luggage.
- The Exchange cannot be won. The Petro Ogoun makes Marchand effectively invulnerable to conventional
  weapons; killing her disrupts the spirit, knocking her out does not, and banishing it leaves her
  catatonic. Whatever happens, Deus watches through its Banded and the runners get paid.
- Outside Influence turns on one phone call. Note carefully how the character who answers it plays it:
  cool and Morris sends the Blues anyway; rattled and he tells them to kill the runners at the first
  sign of trouble; a slip about the hideout and it is kill on sight. The runners must come out of the
  scenario knowing the name Tin Man Scrap Works -- from Morris, his headware, his autonav, or an invoice
  in his pocket.
- Nothing in the endgame is what Overwatch thinks it is. The Mousetrap is not needed; the kill codes
  alone would delete Deus, and Renraku-loyal Resistance members argue for the Mousetrap precisely so
  the AI's code survives. Sebastien has been Deus' for months. The captured half of the team is meant to
  be caught -- the datajack implantation is deliberate ("if there was ever a time for the gamemaster to
  be sadistic and screw the players, this is it"), and offer simple trodes only if the table cannot
  stomach it.
- Split the party on purpose: push the non-deckers to the valve station so that everyone ends up in the
  UV hosts, deckers by the front door and everyone else through the zombie room. In the UV realms, let
  players invent uses for their utilities and then twist the rules slightly whenever they think they
  have it figured out.
- Aneki's death cannot be prevented; Deus supplies the dagger and blocks every attempt to interfere.
  Play it as the tragedy it is -- the man is lucid for the first time in eighteen months, and the first
  thing his repaired mind is shown is what his dream became.
- The victory is hollow by design. Cliber's cell takes the Mousetrap and the credit, Huang shoots the
  corpse and hands Renraku a murder to pin on the team, the arcology is collapsing around them, and no
  one is throwing a parade. Then Ronin disappears, and at 3:00 p.m. on an ordinary afternoon four
  released refugees jack in and begin to join. Deus was never destroyed -- it was distributed, and it
  walked out through the cordon inside the people the military rescued.
"""
