# Harlequin's Back (FASA 7320, 1994) -- campaign order #24 (as directed). Sequel to Harlequin
# (FASA 7306, 1990, campaign order #9). The book states outright "The year is 2055" (p.8) with no
# month given; internal references ("a few years ago" since the original Harlequin adventure) are
# consistent with that gap.
# PRODUCTION/REPO DRIFT NOTE: specs/harlequin.py (the first Harlequin adventure) exists in this
# folder but contains only ADVENTURE/ORDER/SOURCE/YEAR/SYNOPSIS/TIMELINE in the checked-in file --
# no ORGS/LOCATIONS/NPCS. Production nonetheless already has full, richly detailed "Harlequin" and
# "Jane Foster" character rows tagged source_adventure "Harlequin" (confirmed live via --dry), so
# some fuller version of that spec was loaded at some point and the repo file now on disk is stale
# or was reverted after the fact. Ground truth is production: this spec does NOT recreate Harlequin
# or Jane Foster. Instead their Harlequin's Back appearances -- both recur constantly as the
# framing device -- are recorded in NPC_UPDATES (append-only), matched by their exact existing
# names. Separately, production also already has an unrelated "Leroy" (a Dock Worker groundskeeper
# from Ivy & Chrome) with no connection to this book; Aftermath's own Leroy (Harlequin's local
# avatar) is therefore named "Leroy (Aftermath)" below to avoid colliding with that pre-existing,
# unrelated character.
# Almost the entire book takes place inside a single continuous metaplanar astral quest (a shared
# dream/vision the runners cannot leave and that leaves no trace in the physical world by the
# book's own text), so every other ORG/LOCATION/NPC below is tagged to the vision rather than to
# real Seattle continuity; nothing else here plausibly links to any already-loaded spec's rows, so
# ORG_UPDATES/LOC_UPDATES are intentionally empty. Two fleeting in-joke cameos -- a "Lord
# Constable" who strongly resembles Ehran the Scribe, and a "Lady Nasir" who is explicitly the free
# air elemental Ariel Nasir from the original Harlequin adventure -- are recorded in NOT_BUILT
# rather than given stray rows, since both are already-loaded characters wearing costumes, not new
# identities.
# The book is unusually clean of the OCR-garbled editing inconsistencies seen in other titles in
# this series (aside from routine scan noise); its one deliberate loose end is authorial: the
# closing "Future Shock" sidebar tells GMs FASA had not yet decided whether "the Enemy" would
# become a recurring Shadowrun element and invited reader mail on the question, so the metaplot is
# left open by design, not by error. Whether the Songbird itself survives giving Thayla back her
# literal Voice ("sings one final enchanting note and then lies still," p.141) is left ambiguous in
# the text; flagged on the Songbird's row rather than resolved.
# Source text: docs/Adventures/text/Shadowrun 2e - Adventure - Harlequins Back {FASA7320}.txt
# (153 pages, ~15,300 OCR lines).
# ASCII only (pre-commit hook).

ADVENTURE = "Harlequin's Back"
ORDER = 24
SOURCE = "Shadowrun 2e - Adventure - Harlequin's Back {FASA7320}.pdf, pp. 3-152"
YEAR = "2055"

SYNOPSIS = """
Drunk and purposeless a few years after settling his ancient score with **Ehran the Scribe**,
**Harlequin** is visited by a black-robed spectral figure -- Deceit itself, "Master of the Twisted
Path" -- who warns him that **the Enemy**, world-devouring creatures from deep in the metaplanes,
will breach the Sixth World some 2,500 years early. The Great Ghost Dance that broke the old United
States spiked the world's magic to lethal levels at its ritual site in the Southwest desert, and
that spike has become a bridgehead. Fate herself chooses a team of shadowrunners for Harlequin's
astral quest to stop it. Ferried past the **Dweller on the Threshold** and briefed by Harlequin and
his apprentice (and secretly Ehran's own daughter) **Jane "Frosty" Foster**, the runners reach the
**Chasm and the Bridge**, where the Enemy is building a physical span across the gulf between worlds.
Harlequin's plan: bring back **Thayla's Voice** -- the singing voice of an ancient queen who once
held the Enemy's army at bay, now held inside an enchanted Songbird -- and use it to seal the
bridgehead. The runners must gather a hood, a perch, and a cage for the bird, one item per
metaplanar "Place," each ruled in some twisted form by **Darke**, the Enemy's human ally, and each
haunted by echoes of Harlequin and Thayla themselves.

In **Aftermath**, a post-cataclysmic future Seattle, the runners aid **Leroy** (Harlequin's avatar)
and his dying walled Enclave against **Oscuro** (Darke) and his authoritarian Collective, and win
the hood only after Leroy's wife **Talia** (Thayla) sacrifices herself. In **A Fistful of Karma**, a
cowpunk Old West valley, they back reluctant Sheriff **Bergamot** (Harlequin) and mute saloon singer
**Celia** (Thayla) against sadistic rancher **Sy Vants**, gunslinger **Dred Francis**, and the
shapeshifting **Mr. Trey** (Darke), winning a bone perch from Trey's corpse. In **By the Sword**, a
pagan pre-Grail Arthurian England frozen by **Gawaine**'s death at **Lancelot**'s hand (Harlequin's
avatar here), the runners free the amnesiac **Guinglainn**, pass the Priestess **Viviane**'s trials
and Sir **Bercilak**'s Beheading Game at **Castle Maydenlande**, and witness Lancelot's atonement
and Guinglainn's ascension as the new Spring Champion, mending Excalibur's twin, the sword that will
become the cage's metal. In **The Impossible Dream**, a mythic Chicago-flavored realm, the runners
climb an endless Tower built on the **Foreman**'s (Darke) false promise of heaven, free the
**Architect** (Harlequin) and the imprisoned **Maiden** (Thayla), and topple the Tower, earning the
finished cage. **The Songbird** itself waits in Thayla's own corpse-strewn, Enemy-corrupted kingdom,
guarded by the deaf, pleading **Warden** (Darke); the runners steal it back to the Bridge -- only to
learn its song alone cannot stop the Enemy. Following the freed bird, they reach **The Masquerade**:
a neo-Victorian manor where **Lord Umberley** (Darke, fully realized and Initiate Grade 8) hosts a
ball attended by ambiguous Great Powers in costume while his hidden, hunchbacked brother **Nacht**
-- the original dark warrior of Thayla's own legend, and genuinely in love with her -- keeps the
real, still-mute Thayla prisoner behind a butler's and a colonel's murders. Nacht dies shielding
Thayla from Umberley's own killing spell, and she agrees to return. At **the Bridge**, Darke -- out
of avatars now, and human -- is caught mid-sacrifice, torturing a beaten Harlequin on a bone lattice.
Runners who defeat him free Harlequin; then Thayla asks the question no one has answered: what stops
the Enemy from simply killing her once the runners go home? Those who volunteer to stay behind
forever, guarding her as she sings, end the threat for good and wake in their own beds in Seattle,
remembering everything, with no proof any of it happened.
"""

TIMELINE = """
- **Voices from the Past** -- alone and drinking, Harlequin is confronted by a spectral embodiment
  of Deceit ("Master of the Twisted Path") who warns him the Enemy is coming early and tells him to
  "destroy the bridge" with Thayla's Voice. Jane Foster interrupts, chrome pistol in hand: "Harlequin's back."
- **Foreshadows** -- weeks of subtle omens (animal deference, uncanny luck, portentous dreams, an
  uncatchable laughing clown, a "20 Questions" personality survey) build toward the quest in the
  runners' ordinary Seattle lives; a record thunderstorm puts them all to sleep the same night.
- **Into the Desert / The Bridge, Part One** -- the Dweller on the Threshold tests and passes the
  runners regardless (the Great Powers decreed it); Harlequin's minivan carries them to the site of
  the Great Ghost Dance in the Southwest desert, then to the Chasm and the Bridge, where the Enemy
  is already spanning the gap. Harlequin tells them Thayla's legend and sends them after her Voice,
  fighting off a first wave of Enemy creatures and marking them with his own blood (a personal Karma
  Pool) plus a Team Karma Pool of 50 that never refreshes.
- **Aftermath** -- the Enclave vs. the Collective; Talia's self-sacrifice heals the wasteland and
  wins the Songbird's hood from the fallen Oscuro.
- **A Fistful of Karma** -- three days in Valley Hope; Bergamot and Celia face down Vants and Dred
  Francis at high noon; Mr. Trey's true form dies to Celia's restored song, dropping the perch-bone.
- **By the Sword** -- the runners free Guinglainn, win Lancelot's broken sword from him, pass the
  trials of Avalon and Castle Maydenlande, and watch Lancelot's atonement-death and Guinglainn's
  rebirth as the Spring Champion, who mends the sword -- the cage's future metal.
- **The Impossible Dream** -- the ruined Village and its impossible Tower; the runners free the
  Architect's imprisoned Maiden from the Foreman's Labyrinth, topple the Tower, and receive the
  finished birdcage, forged from Lancelot's sword and Trey's bone.
- **The Songbird** -- Thayla's own kingdom, dead and corrupted since she left it; the runners steal
  the Songbird from the deaf Warden's tower.
- **The Bridge, Part Two** -- the Songbird's song alone fails to stop the Enemy; Harlequin binds the
  runners to the bird with silver cords to follow it to Thayla herself.
- **The Masquerade** -- Umberley Manor; two murders (Stokes, Colonel Quinn), a seance, house arrest,
  and a final confrontation in "the Engine" beneath the manor, where Nacht dies protecting Thayla
  from his own brother and she agrees to return with the runners.
- **The Bridge, Part Three** -- Darke, unmasked and human, is caught sacrificing children to pollute
  the outcropping while Harlequin hangs tortured on a bone lattice; the runners defeat him, free
  Harlequin, and must choose whether to stay with Thayla forever while she sings the Enemy back for
  good. Survivors wake in Seattle at the same dawn with no physical evidence the quest ever happened.
"""

ORGS = [
    {
        "name": "The Enclave",
        "org_type": "survivor settlement",
        "tier": 1,
        "headquarters": "A walled compound on a mesa in the ruins of a far-future Auburn, Washington (the Aftermath Place)",
        "summary": "Dying walled settlement of anti-magic, anti-cyber survivors in a metaplanar post-cataclysm future Seattle; led by Harlequin's avatar Leroy",
        "description": (
            "A community of some 36 guards and 120 other inhabitants that retreated behind stone walls "
            "generations ago as the land sickened and predators multiplied, built over the one pure "
            "spring left in the wasteland. Rejects magic and cybertech as tainted; casting a spell in "
            "this Place opens spontaneous bleeding wounds on the caster's own body, which is exactly how "
            "the Enclave always knows when an outsider has used it. Governed by a single leader chosen "
            "by rough consensus -- currently Leroy, Harlequin's avatar in this Place -- who can be "
            "unseated the moment the community stops trusting him. Slowly starving: failing crops, "
            "poisoned water, and steady losses to the rival Collective's raids and 'merger' overtures."
        ),
        "leadership": [
            {"name": "Leroy", "title": "Leader", "notes": "Harlequin's avatar; a reluctant, self-doubting philosopher-king."},
            {"name": "Gareth", "title": "Security chief / first lieutenant", "notes": "Physical adept; distrusts the runners on sight."},
            {"name": "Maranda", "title": "Scout leader", "notes": "Physical-adept archer who first brings the runners in."},
        ],
        "notes": (
            "Aftermath's climax: Oscuro's army (half real, half illusion) attacks; Leroy is struck down "
            "by Oscuro's lightning, and his wife Talia's self-sacrifice alongside his own blood heals "
            "the land and ends the siege. The runners' goal here is the leather hood off Oscuro's pet "
            "eyekiller, dropped when he is defeated or driven off."
        ),
        "enemies": ["The Collective"],
    },
    {
        "name": "The Collective",
        "org_type": "authoritarian settlement",
        "tier": 2,
        "headquarters": "A mountain settlement in the foothills of a far-future Mount Baker (the Aftermath Place)",
        "summary": "Megacorp-modeled rival settlement in the Aftermath Place; physically prosperous, spiritually crushed, ruled by Darke's avatar Oscuro",
        "description": (
            "A larger, better-fed settlement that subordinates every man, woman, and child to collective "
            "survival under an absolute dictator, using blood magic and primitive cyberware the Enclave "
            "refuses. Growing population has begun to outstrip its filtered water supply, which is the "
            "real reason behind its repeated 'merger' overtures to the Enclave -- it wants the Enclave's "
            "clean well, not more mouths to feed. Openly escalated from raids and crop-burning to a full "
            "field army (nominally a thousand-strong, actually a few hundred padded out with illusions) "
            "once Leroy refused to trade his wife Talia for a false peace."
        ),
        "leadership": [
            {"name": "Oscuro", "title": "Leader", "notes": "Darke's avatar; shapeshifts between a cruel human form and an amorphous monster."},
            {"name": "Enganar", "title": "Lieutenant", "notes": "Toxic Alacorn shaman; sacrificed Tela to power the Ram spell that broke the Enclave's gate."},
            {"name": "Bellaco", "title": "Lieutenant, hermetic mage", "notes": "Led the escort taking the surrendered Talia to Oscuro; sadistic elf mage."},
        ],
        "notes": "Its soldiers refuse capture and fight to the death; game statistics treat 'Collective Soldiers' as generic Threat Rating troops rather than named individuals.",
        "enemies": ["The Enclave"],
    },
    {
        "name": "Blood Eagle Gang",
        "org_type": "gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Blood Eagle Ranch, the Valley Hope valley (the A Fistful of Karma Place)",
        "summary": "Sy Vants' cowpunk gunslinger outfit terrorizing Valley Hope; broken once by Sheriff Bergamot, rebuilding to finish the job",
        "description": (
            "Sy Vants' private army of cowpokes and cybered 'cowpunk' gunslingers, run from the "
            "comfortable Blood Eagle Ranch. Six years before the runners arrive, Sheriff Arlen Bergamot "
            "and a citizens' Vigilance Committee broke the gang's grip on Valley Hope and put Vants' top "
            "gun, Dred Francis, in prison. With Mr. Trey's backing and Francis' release, Vants openly "
            "'hooraws' the town again ('This here's a saloon, ain't it? Whaddya gotta do t'get a drink in "
            "here?'), terrorizes the mute saloon singer Celia, and burns out fleeing homesteaders in a bid "
            "to retake the valley by force before the noon showdown."
        ),
        "leadership": [
            {"name": "Sy Vants", "title": "Boss", "notes": "Physical adept; the dark warrior's avatar in this Place; sadistically fixated on Celia."},
            {"name": "Dred Francis", "title": "Top gunslinger", "notes": "Cybered gunfighter, just released from territorial prison to finish what the gang started."},
        ],
        "notes": "Rank and file are generic cowpoke/cowpunk Threat Rating troops (six cowpunks: three human, two troll, one elf, plus an unspecified number of cowpokes), not individually named.",
        "allies": ["Flattop Mining Company"],
    },
    {
        "name": "Flattop Mining Company",
        "org_type": "corporation",
        "tier": 1,
        "headquarters": "Flattop Phlogiston Mine, outside Valley Hope (the A Fistful of Karma Place)",
        "summary": "Mining outfit fronting for the shapeshifting Mr. Trey, who wants Valley Hope's ecology broken to feed on its people's despair",
        "description": (
            "A phlogiston-mining concern that closed its Valley Hope operation years ago after its "
            "tailings poisoned the local water and its miners' camp turned lawless -- one of the two "
            "'ruinous elements' (with the Blood Eagle gang) that Sheriff Bergamot's Vigilance Committee "
            "broke. Now represented in town solely by the courteous, unnervingly persuasive Mr. Trey, "
            "who promises the valley prosperity if the mine reopens. In truth Trey is Darke's avatar in "
            "this Place; the 'company' is a fiction he uses to manipulate homesteaders, back Sy Vants, "
            "and manufacture the monster and fire elemental that terrorize the town."
        ),
        "leadership": [
            {"name": "Mr. Trey", "title": "Company representative", "notes": "Darke's avatar; a shapeshifting horror wearing a handsome human face."},
        ],
        "notes": "The abandoned mine site itself holds only ruined barracks and empty shafts -- no sign anyone, Trey included, actually lives there.",
        "allies": ["Blood Eagle Gang"],
    },
    {
        "name": "Priestesses of Avalon",
        "org_type": "mystical fellowship",
        "tier": 2,
        "headquarters": "The Isle of Apples (the By the Sword Place)",
        "summary": "Goddess-serving priestesshood of a pagan pre-Grail Arthurian England, keepers of Avalon and Excalibur, no male ever allowed to set foot on their island alive",
        "description": (
            "The priestesshood of the Goddess in a version of Arthurian Britain where the Grail Quest "
            "never happened and Gawaine, not Lancelot, was the true finest knight of the Round Table. "
            "Three of them -- Anna, Gwyar, and Belisent, described as aspects of one and the same being "
            "-- keep vigil at a fountain nexus in the pagan woodland, guiding runners without giving "
            "direct answers ('he who serves us,' Anna calls the finest knight, and no more). Viviane, "
            "their most powerful voice, and Nimue, the Lady of the Lake who bears Excalibur, live on the "
            "Isle of Apples proper. Any man who sets foot on the island turns instantly to glass and "
            "shatters; only women may land. The order's fortunes are tied to Gawaine's death and the "
            "land's resulting barrenness, and to the eventual freedom of his amnesiac son Guinglainn, "
            "the next Champion of Spring."
        ),
        "leadership": [
            {"name": "Viviane", "title": "Priestess", "notes": "Speaks only to female runners; resembles Jane Foster, coincidentally per the text."},
            {"name": "Nimue", "title": "Lady of the Lake", "notes": "Rises from the lake bearing Excalibur at the story's climax."},
        ],
        "notes": "Threatening the Priestesses at the fountain summons roughly six spirits/elementals per runner and a barrage of Force 30 chaotic world spells before they withdraw and abandon the runners to a harder version of the adventure.",
    },
]

LOCATIONS = [
    {
        "name": "Site of the Great Ghost Dance",
        "location_type": "place of power",
        "city": "Metaplanes",
        "district": "A remote desert in the Southwestern United States (real-world site of the Great Ghost Dance ritual)",
        "security_level": "Low Security",
        "summary": "Flat, barren 20-meter circle where the Great Ghost Dance spiked the world's background magic to lethal levels, opening a metaplanar bridgehead for the Enemy",
        "description": (
            "An otherwise unremarkable stretch of hard desert, reached from the highway by dirt track "
            "and then on foot; nothing grows here. Harlequin conjures a shadowless silver globe of light "
            "to examine it and explain that the blood-magic cost of the Ghost Dance -- the deaths of "
            "many of its own practitioners -- permanently raised local background magic to a level the "
            "rest of the planet will not reach for a thousand years, drawing the world-devouring Enemy "
            "across the metaplanes centuries ahead of schedule. 'This is where they broke the spirit, "
            "pardon the pun, of the good ol' U.S. of A.,' he tells the runners. 'This is where they "
            "danced the Big One, the Great Ghost Dance. And this is where we start.'"
        ),
        "notes": (
            "Astral perception here is a 5D Stun attack (no Dice Pool applies); a shaman's Magic Attribute "
            "doubles here, any other magician's halves. This is where Harlequin performs the ritual that "
            "opens the astral quest proper and where the Enemy's first attack (Enemy Crawlers) hits the "
            "runners before Harlequin sends them through a chalk-drawn doorway to Aftermath."
        ),
    },
    {
        "name": "The Chasm and the Bridge",
        "location_type": "place of power",
        "city": "Metaplanes",
        "district": "The astral quest's recurring hub, visited three times as 'The Bridge, Parts One through Three'",
        "security_level": "No Security / Barrens",
        "summary": "Bottomless metaplanar gulf between the Sixth World and the Enemy's realm, spanned by a growing bone-and-spirit bridge the runners must stop before it completes",
        "description": (
            "A vast rock outcropping -- the physical echo of the Ghost Dance's power spike -- juts out "
            "over a chasm whose bottom cannot be seen; a violet, storm-wracked sky churns overhead. Far "
            "across the gap, a horde of Enemy creatures labors around the clock on a dark bridge of bone "
            "and captured spirits, already kilometers long. 'They're coming, you see,' Harlequin shouts "
            "against the roaring wind on the runners' first sight of it, 'and the Great Ghost Dance, this "
            "outcropping, has made it thousands of years easier for them.' Harlequin waits here through "
            "the whole adventure preparing the Place for Thayla's return while the runners gather the "
            "pieces of the Songbird's hood, perch, and cage across five other metaplanar Places."
        ),
        "notes": (
            "Part One: the runners first see the Bridge and are attacked by six Enemy Crawlers, then a "
            "second wave, before fleeing through Harlequin's chalk doorway. Part Two: the returned "
            "Songbird sings here but fails alone to slow the Enemy's work, so Harlequin binds the runners "
            "to the bird with silver cords to follow it to Thayla. Part Three (the climax): Darke, no "
            "longer masked as any avatar, is caught here sacrificing drugged children (who speak a "
            "2055 Mexican/Aztlan-dialect Spanish -- their origin is never explained) to raise the "
            "Background Count and pollute the outcropping against Thayla, while Harlequin hangs tortured "
            "on a bone-and-sinew lattice nearby. Ten Enemy Crawlers/Toads and Darke himself must be "
            "defeated; afterward Thayla asks what will stop the Enemy from simply killing her once the "
            "runners leave, and one or more of them must volunteer to remain and guard her forever while "
            "she sings, at which point the Great Powers manifest to protect the Place 'for a time.'"
        ),
    },
    {
        "name": "The Enclave (Aftermath)",
        "location_type": "walled settlement",
        "city": "Metaplanes",
        "district": "The Aftermath Place -- ruins of a far-future Auburn, Washington",
        "controlling_org": "The Enclave",
        "security_level": "No Security / Barrens",
        "summary": "Stone-walled mesa compound of piled-rock huts around the wasteland's last pure well; Leroy's Long House, an armory, and a smithy",
        "description": (
            "A dozen crude stone-and-turf buildings inside a three-meter rock wall, centered on a "
            "communal well two meters wide and ten deep -- the only potable water for kilometers. A "
            "single barred wooden gate (Barrier 13) is the only way in. The Long House, the largest "
            "building, serves as both Leroy's home and the settlement's town hall, with an armory, a "
            "meeting hall, and guest and guard quarters; two guards with swords and pole arms stand "
            "outside its door at all times."
        ),
        "notes": (
            "Recognizably built over the ruins of real-future Auburn -- runners with Physical Sciences "
            "can identify the 'rocks' underfoot as ferroconcrete altered by some non-radiant process, and "
            "the surrounding volcanoes as Rainier, Baker, and St. Helens. Site of the Delegation "
            "negotiations, the Price of Peace ultimatum (Talia's abduction), and the climactic siege by "
            "the Collective's army in Leroy's Last Stand."
        ),
    },
    {
        "name": "Valley Hope",
        "location_type": "town",
        "city": "Metaplanes",
        "district": "The A Fistful of Karma Place -- a cowpunk Old West valley",
        "security_level": "Low Security",
        "summary": "180-person frontier town threatened by Sy Vants' Blood Eagle gang and Mr. Trey's mine; Main Street and Train Street, church, jail, bank, and the Songbird Saloon",
        "description": (
            "A tidy frontier town split by the fork of Main Street (south) and Train Street, along which "
            "landsteamers run. Notable buildings: a church with a clockwork steeple; the parsonage and "
            "schoolhouse of Parson and Mrs. Emmerick; the sheriff's office and jail; the Valley Hope "
            "Clarion newspaper office, run by editor Kendall Silver; Festus Barber Shop; Mrs. Jenning's "
            "Boarding House; Fergus Fine Yard Goods; Max Hammel's smithy and livery stable; the Union "
            "Feed Store; the Old No. 93 Saloon; Hasher's Carpentry and Lumberyard; the Flattop Mining Co. "
            "business office; attorney Simon Renfrew's office; a Western Spherics crystal-ball message "
            "office and its crystallomancer's tower; the Union Continental landsteamer station; Doc "
            "Wunderlich's surgery; the Valley Hope Bank; the Songbird Saloon; the land office (burned by "
            "Trey's fire elemental on the runners' first night); the Farmers' Cooperative; Winch "
            "Wardell's general-store Emporium; and Mrs. Venturi's apothecary."
        ),
        "notes": (
            "Founded on ground fought over by the Blood Eagle gang and the Flattop mine for years before "
            "Sheriff Bergamot's Vigilance Committee broke both six years ago; the whole valley is a "
            "closed loop while the story is unresolved -- runners who try to ride out simply re-enter "
            "from the opposite side. About a hundred more people live scattered across nearby homesteads "
            "in the wider valley."
        ),
    },
    {
        "name": "Blood Eagle Ranch",
        "location_type": "ranch",
        "city": "Metaplanes",
        "district": "The Valley Hope valley (the A Fistful of Karma Place)",
        "controlling_org": "Blood Eagle Gang",
        "security_level": "Low Security",
        "summary": "Sy Vants' comfortable two-storey ranch house and bunkhouse, guarded by two cowpokes per shadowrunner plus two cowpunks",
        "description": "A two-storey ranch house with a large gang bunkhouse, cattle pens, stables, and outbuildings -- Sy Vants' seat of power over the valley.",
        "notes": "Guard strength drops to four cowpokes and one cowpunk only twice in the story: during the Hooraw! street riot and during the No Escape refugee ambush, when most of the gang is elsewhere.",
    },
    {
        "name": "Flattop Phlogiston Mine",
        "location_type": "mine",
        "city": "Metaplanes",
        "district": "Outside Valley Hope (the A Fistful of Karma Place)",
        "controlling_org": "Flattop Mining Company",
        "security_level": "No Security / Barrens",
        "summary": "Abandoned phlogiston mine Mr. Trey claims as his home; in truth only ruined barracks and empty shafts, no sign anyone lives there",
        "description": "The remains of the miners' barracks and the mine's empty tunnels and shafts, closed years ago after its tailings poisoned Valley Hope's water. Mr. Trey directs all mine-business inquiries here but is never actually found on site.",
        "notes": "Source of the reanimated 'mine monster' that attacks Valley Hope on the runners' arrival, built by Trey from a dead miner's corpse.",
    },
    {
        "name": "Songbird Saloon",
        "location_type": "bar",
        "city": "Metaplanes",
        "district": "Train Street, Valley Hope (the A Fistful of Karma Place)",
        "security_level": "Low Security",
        "summary": "Only saloon with rooms to rent in Valley Hope; ork owner Jed Porkins, flaming Dragon's Breath cordial, and mute barmaid Celia -- Harlequin's Back's echo of Thayla",
        "description": (
            "The town's social hub and the runners' de facto base: a harpsichord player in a soiled "
            "wig, barmaids and barboys, hogsheads of beer and wine, and the signature flaming cordial "
            "Dragon's Breath (escalating Stun damage per round drunk). Upstairs rooms are rented to guests; "
            "owner Jed Porkins lives next door. The mute former singer Celia works the floor here and "
            "gives the saloon its name."
        ),
        "notes": "Site of the Hooraw! confrontation where Sy Vants publicly torments Celia, and of the climactic High Noon showdown between Bergamot, Vants, and Dred Francis.",
    },
    {
        "name": "The Pagan Woodland",
        "location_type": "enchanted forest",
        "city": "Metaplanes",
        "district": "The By the Sword Place -- a pre-Grail pagan Arthurian England locked in eternal winter",
        "security_level": "Low Security",
        "summary": "Frost-bound forest of eight paths converging on the Priestesses' fountain, Lancelot's hermit hut, and a thorn-walled clearing holding the imprisoned Guinglainn",
        "description": (
            "A lightly wooded, perpetually sub-freezing landscape whose paths always return travelers to "
            "where they started if they stray. At its nexus, eight paths meet at a small pavilion and "
            "fountain where the Priestesses Anna, Gwyar, and Belisent wait; nearby stands Lancelot's "
            "rough stone hermit's hut (well, woodpile, Christian icons inside, his broken sword hidden "
            "under the pallet bed); and a separate clearing holds a three-meter wall of living thorns "
            "guarding a pod-like plant containing the cursed, amnesiac Guinglainn. A northern lakeshore, "
            "reached later, is where Lancelot's atonement and Excalibur's return finally take place."
        ),
        "notes": (
            "Background Count 2 throughout (5 on the Isle of Apples). Freeing Guinglainn requires cutting "
            "through the animate, retaliating thorn wall while resisting a magical Willpower-draining "
            "beguilement; the wall's assaults do not target the pod itself."
        ),
    },
    {
        "name": "Isle of Apples",
        "location_type": "sacred island",
        "city": "Metaplanes",
        "district": "Avalon, the By the Sword Place",
        "security_level": "Low Security",
        "summary": "Avalon itself: burial place of Arthur, realm of the Goddess, reachable only by a Priestess-poled barge, and lethal to any man who sets foot on it",
        "description": (
            "Glimpsed across misty water from the northern shoreline and reachable only aboard a small "
            "flat-bottomed barge poled by a faceless, hooded, silent figure that appears only after the "
            "runners have met both Lancelot and freed Guinglainn, warning them in a dispassionate female "
            "voice: 'No man may set foot on the Isle of Apples and live.' Unlike the frozen mainland, the "
            "island itself is perpetually on the verge of spring. Viviane meets female runners here (men "
            "who disembark turn instantly to glass and shatter); an optional 'Ritual/Dream of Flowers' "
            "offers a symbolic vision of the Flower Maiden abduction myth tied to Gawaine's own legend."
        ),
        "notes": "Background Count 5. Viviane can grant hawthorn berries (each heals 1 box of Physical damage once a character is already wounded) and the crucial clue that a male runner must draw blood at Castle Maydenlande with the same broken sword-metal that killed Gawaine.",
    },
    {
        "name": "Castle Maydenlande",
        "location_type": "castle",
        "city": "Metaplanes",
        "district": "The By the Sword Place",
        "security_level": "Zero Zone -- Lethal Response",
        "summary": "Ruined island castle behind Sir Bercilak's Beheading Game and mansion hospitality trials; guarded moat, animate stone knights, and a Crone barring Gawaine's Great Hall",
        "description": (
            "Reached by another silent ferryman, the island holds a guarded gate manned by the knight "
            "Bercilak, whose Beheading Game (submit to an axe-blow, then return two days later to receive "
            "one in kind) opens the way to his mansion; there his wife Ragnall and daughter Winlogee test "
            "chosen runners with a seduction trial and a loathly-lady riddle. Beyond a moat holding two "
            "torpid each-uisge water horses lies the ruined castle proper: animate Stone Knight statues "
            "guarding the corridor to the Great Hall, and an old woman -- a destructive aspect of the "
            "Goddess -- who interrogates and then tests any runner seeking entry. Inside the Great Hall, "
            "the broken tip of Lancelot's sword hangs bleeding on the wall beside a stained-glass rose "
            "window inscribed with a binding oath from the Books of Broceliande."
        ),
        "notes": (
            "All target numbers here are increased by 5 (reduced by up to several points for gifts earned "
            "in earlier trials: Belisent's girdle, Ragnall's belt, Winlogee's choker, success in the "
            "Beheading Game, being female, or having experienced the Dream of Flowers). A male runner "
            "must cut himself with the sword-tip and bleed into the great cauldron on the table to summon "
            "Gawaine's spectral form, who sends the party to reunite Lancelot with the Lady of the Lake."
        ),
    },
    {
        "name": "The Village",
        "location_type": "ruined village",
        "city": "Metaplanes",
        "district": "The Impossible Dream Place -- a mythic, archetypal realm laced with anachronistic Chicago debris",
        "security_level": "Low Security",
        "summary": "Abandoned village dwarfed by the impossible Tower its people built chasing a false promise of heaven; home to the Architect and the ruined Cathedral",
        "description": (
            "A long-empty settlement at the base of the Tower, littered with incongruous modern-day "
            "Chicago refuse the locals cannot explain. At its heart, in a shaft of light beneath the "
            "Tower's branches, sits the ruined Cathedral; nearby, a dark ring of graves called Deadfall "
            "circles the Tower's base, each headstone reading 'Icarus.' The elf Architect, wound like a "
            "clockwork toy by a key between his shoulder blades, tends the ruins alone."
        ),
        "notes": "Runners arrive here in gray robes with no gear (cyberware persists but looks organic); trying to leave in any direction but forward toward the Village produces an Exit Door guarded by a powerful spirit Bouncer who warns, 'Leaving so soon? I can't stamp your hand, y'know. If you leave, you're gone. Be a shame to miss the opening act.'",
    },
    {
        "name": "The Cathedral",
        "location_type": "ruined cathedral",
        "city": "Metaplanes",
        "district": "The Village, the Impossible Dream Place",
        "security_level": "Low Security",
        "summary": "Once dedicated to a nameless spirit called Mother, now displaying the Foreman's gifted 'treasures' -- mints, a porn magazine, gold coins, and a loaded pistol -- on its desecrated altar",
        "description": (
            "In better repair than the rest of the Village: a foyer basin of warm broth-like liquid, "
            "pegs of ceremonial masks once worn before the Patron, and stained-glass windows depicting "
            "every world religion. The altar's toppled statue lies shattered on the stairs, replaced by "
            "the Foreman's trivial treasures on velvet cushions -- including an inexplicably warm, loaded "
            "Ares Predator II, one of the only firearms available in this Place."
        ),
        "notes": "Approaching the altar rouses Mother, a shattered spirit who reforms from the broken statue, is disgusted by any unmasked (visibly sinful) face -- 'Your features may be fair, but I can see your soul reflected in your face. Your sins are blemishes I cannot bear' -- and begs the runners to 'bring her children back,' the Tower's climbers.",
    },
    {
        "name": "The Tower",
        "location_type": "impossible tower",
        "city": "Metaplanes",
        "district": "Rising from the Village, the Impossible Dream Place",
        "security_level": "Zero Zone -- Lethal Response",
        "summary": "Kilometers-tall structure the Village's people abandoned their lives to build chasing a false promise of treasure from the sky; guarded by three escalating Guardians and the Foreman's bunker at its summit",
        "description": (
            "A skeletal superstructure that grows from Gothic construction near its base to post-"
            "industrial scaffolding near its top, its architectural style shifting the way the Village's "
            "own culture did as the climbers abandoned it floor by floor. A layer of gas-filled balloons "
            "near the summit keeps the unstable structure standing; above them, the Foreman's bunker sits "
            "on an elevated platform, guarded by an armored Henchman and an endless supply of gunmen."
        ),
        "notes": (
            "Guardian 1 (a land-adapted kraken) Engulfs runners into the Limbo Room pocket dimension; on "
            "a second climb it has lost most of its powers. Roughly 200 of the 500 villagers who climbed "
            "over five years have fallen to their deaths (the Deadfall graves below). When the Maiden is "
            "freed and the villagers descend, the Tower's stabilizing balloons break free and it "
            "collapses to dust while the Maiden sings the crowd calm."
        ),
    },
    {
        "name": "The Limbo Room",
        "location_type": "roadhouse",
        "city": "Metaplanes",
        "district": "A pocket dimension reached only through Guardian 1's Engulf attack (the Impossible Dream Place)",
        "security_level": "Low Security",
        "summary": "A too-real Seattle roadhouse where runners get their own gear back just long enough for 'Bill Foreman' to try to bribe them off the quest before his goons open fire",
        "description": (
            "A dusty Arizona-desert roadhouse with cars and motorcycles parked outside; inside, low light, "
            "a live band, and a booth where a spandex-dressed girl and a long-coated elf bodyguard sit "
            "beside a trideo terminal linking (via a false Matrix a decker can actually run) to 'Bill "
            "Foreman' -- a heavyset man in a white suit fidgeting with rosary beads."
        ),
        "notes": "Accepting Foreman's bribe (an open-ended briefcase of temptation) ends the quest on the spot; refusing triggers an ambush by the enforcer Eve, the hitman Blazer, and one thug per runner before the runners are dumped back at the edge of the Village to restart the climb.",
    },
    {
        "name": "Thayla's Palace",
        "location_type": "ruined palace",
        "city": "Metaplanes",
        "district": "The Songbird Place -- Thayla's own kingdom, corrupted after she left it",
        "security_level": "Zero Zone -- Lethal Response",
        "summary": "The corpse-strewn ruin of Thayla's fairy-tale city and palace; the Songbird waits in its one surviving copper-and-gold tower, guarded by the deaf, pleading Warden",
        "description": (
            "A city and palace the gamemaster is instructed to model on the players' own hometown, laid "
            "waste and preserved in eternal putrefaction by the Enemy after Thayla left with the dark "
            "warrior and her land's protection failed. A quarter of the palace is burned rubble; only a "
            "single tower survives, reached by thousands of steps past bodies locked in violence and "
            "ravens picking at their eyes and tongues. At the top, a circular chamber painted with sky "
            "and sun holds the caged Songbird on a golden chain."
        ),
        "notes": (
            "Any spirit summoned anywhere in this Place is automatically toxic and hostile to its "
            "summoner. Four deaf guardian creatures with pain whips defend the palace and tower; the "
            "Warden (Darke's avatar here) begs the runners to kill the Songbird for him rather than take "
            "it, but cannot bear to touch or even look at the bird himself."
        ),
    },
    {
        "name": "Umberley Manor",
        "location_type": "manor house",
        "city": "Metaplanes",
        "district": "The Masquerade Place -- a neo-Victorian realm of landed aristocracy and techno-magical machinery",
        "security_level": "Corporate High Security",
        "summary": "Lord Umberley's gothic-Victorian mansion: a masquerade ball, a secret passage maze, and the buried techno-magical 'Engine' where his brother Nacht keeps the real Thayla prisoner",
        "description": (
            "A hulking mansion the runners reach following the Songbird through driving storm-rain. "
            "Butler Stokes greets guests at the door ('Welcome to Umberley Manor. You are just in time "
            "for the festivities.'); a vaulted chessboard-marble foyer leads to guest rooms (each with an "
            "Engine terminal) and a two-storey ballroom lit by candle chandeliers and stained glass "
            "depicting world mythologies, where an animal-costumed string quartet plays for a masquerade "
            "of guests who may be ambiguous Great Powers in disguise. Every wall carries a Force 6 ward. "
            "A hidden passage maze behind the guest rooms connects to the library and, far below, to "
            "'the Engine' -- a cavern-sized techno-magical mechanical computer, its innermost chamber "
            "Nacht's own lair, where he keeps the real, still-mute Thayla captive."
        ),
        "notes": (
            "Cyberware becomes magical amulets or vanishes entirely; firearms become period revolvers; "
            "body armor is essentially gone. Stokes and (later) Colonel Quinn are both murdered by Nacht "
            "in the secret passages; the Lord Constable confines the whole party to their rooms as prime "
            "suspects, forcing the runners into the tunnels (hunted by four spirit hounds) to find Thayla "
            "before Umberley can stall them long enough for Darke to move against Harlequin at the Bridge. "
            "The Engine itself: MATRIX_HOSTS documents it, never built."
        ),
    },
]

NPCS = [
    {
        "name": "Thayla",
        "role": "The ancient exiled queen whose singing Voice alone can hold the Enemy back; the quest's true object, found only in the book's final chapters",
        "archetype": "Mage",
        "title": "Queen (in exile); Initiate, grade 10",
        "race": "Human",
        "gender": "Female",
        "connection": 2,
        "description": (
            "Tall, of light to medium build, raven-black hair, pale skin with a faint blush, and eyes of "
            "impossibly brilliant emerald; poised, regal, and calmly commanding even in captivity. Her "
            "formidable magic is bound up entirely in her singing voice, which she uses as a Centering "
            "Skill and cannot cast at all until the Songbird restores it to her in The Masquerade's "
            "climax, whereupon she commands the fighting to stop with a single word: 'Stop!' At the "
            "Bridge she asks the runners the question none of them can answer: 'What happens when you "
            "leave?'"
        ),
        "background": (
            "Ages ago she ruled a rich valley whose people prospered under her protection; each dawn she "
            "sang the sun up and no evil could enter her land while she sang. A dark warrior fell in love "
            "with her song and would not be driven off, and his mere presence slowly poisoned her land; to "
            "save her people she left with him, first placing her Voice in an enchanted Songbird so the "
            "land would still be protected. She has wandered the metaplanes with her dark companion ever "
            "since, worn down to near-apathy by the years. Her land itself later fell anyway, corrupted by "
            "the Enemy once she was gone (see The Songbird), and she herself was eventually taken -- still "
            "mute -- by Lord Umberley's brother Nacht, who genuinely fell in love with her without knowing "
            "who she truly was."
        ),
        "notes": (
            "B3 Q4 S2 C8 I5 W6, Ess 6, Magic 16, Reaction 4; Singing 12, Sorcery 8, Conjuring 6; once her "
            "voice is restored, each singing attack (a Complex Action) inflicts 16M damage on every Enemy "
            "entity in the area, resistible only by Willpower. Her metaplanar avatars/echoes across the "
            "book are Talia (Aftermath), Celia (A Fistful of Karma), the Maiden (The Impossible Dream), "
            "and the Songbird itself (The Songbird) -- all recorded as separate rows since each is a "
            "distinct named character with her own scene, race, and fate. At the climax she must be "
            "talked into risking self-sacrifice a second time, and asks the question the runners must "
            "answer themselves: what stops the Enemy from killing her the moment they leave her alone at "
            "the Bridge."
        ),
    },
    {
        "name": "Darke",
        "role": "The Enemy's sole human ally and the astral quest's recurring antagonist, appearing as a different local villain in almost every metaplanar Place",
        "archetype": "Mage",
        "title": "Initiate, grade 4",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "A powerful magician so thoroughly given over to the Enemy's service that his presence "
            "echoes across the metaplanes, manifesting in each Place as both a human face and, when "
            "pushed, something monstrous. No fixed physical description is given for his true self; his "
            "many local avatars vary sharply in appearance."
        ),
        "background": (
            "Never explained in the text beyond his role as the Enemy's chosen agent among humanity. Each "
            "of his metaplanar avatars -- Oscuro (Aftermath), Mr. Trey (A Fistful of Karma), the Foreman "
            "(The Impossible Dream), the Warden (The Songbird), and Lord Umberley (The Masquerade) -- is "
            "recorded as its own NPC row, since each is a distinct named character within its own Place, "
            "but all are explicitly the same being; killing an avatar ends only that Place's manifestation."
        ),
        "notes": (
            "B5 Q4 S4 C3 I6 W6, Ess 6, Magic 8, Reaction 5; Sorcery 6, Armed Combat 4, Firearms 5; carries "
            "a Power Focus (3) and spell locks for Anti-Bullet Barrier and Increased Reflexes. Vulnerable "
            "to the Architect's sword (an artifact the runners win in The Impossible Dream). Unmasked and "
            "fully himself only at the climax, The Bridge, Part Three, where he is caught sacrificing "
            "drugged, Aztlan-dialect-speaking children to pollute the outcropping against Thayla and has "
            "tortured Harlequin nearly to death; killing him here kills him in the real world as well, "
            "though the text notes 'the Enemy will find others like him.'"
        ),
    },
    {
        "name": "Leroy (Aftermath)",
        "role": "Leader of the Enclave in the Aftermath Place; Harlequin's local avatar, a reluctant philosopher-king forced into command",
        "archetype": "Physical Adept",
        "title": "Leader, the Enclave",
        "race": "Human",
        "gender": "Male",
        "age": 28,
        "organization": "The Enclave",
        "connection": 2,
        "description": (
            "A leather-jumpsuited, black-cloaked physical adept who resembles Harlequin closely enough "
            "that runners familiar with the elf notice it at once, though Leroy is unmistakably human and "
            "has no knowledge of metaplanes, quests, or Harlequin himself. His name, he notes bitterly, is "
            "a corruption of 'le Roi' -- the king. Meets the captured runners with a curious rather than "
            "threatening tone: 'My name is Leroy. Who are you people, and what is your business here?'"
        ),
        "background": (
            "Born and raised entirely within the Enclave, Leroy never sought leadership but was pushed "
            "into it because his people trust him as if he were infallible -- a pressure he privately finds "
            "close to unbearable, certain that his first major failure will break both his self-esteem and "
            "the community's cohesion. Married to Talia."
        ),
        "notes": (
            "Physical adept: Improved Ability (Armed Combat +6), Improved Physical Attributes (Str +1, "
            "React +1), Increased Reflexes (+1); wields a Rating 3 weapon-focus sword. Survives the "
            "Collective's siege only by inches, struck down by Oscuro's lightning at the height of the "
            "battle; healing magic from the runners keeps him alive long enough for Talia's self-sacrifice "
            "to complete the ritual that heals the wasteland. Named 'Leroy (Aftermath)' here only to avoid "
            "colliding with an unrelated pre-existing 'Leroy' (a Dock Worker from Ivy & Chrome); in-story "
            "everyone, including himself, calls him simply Leroy."
        ),
    },
    {
        "name": "Talia",
        "role": "Leroy's wife in the Aftermath Place; Thayla's local avatar, whose self-sacrifice alongside Leroy's blood heals the dying wasteland",
        "archetype": "Face",
        "title": "Leroy's wife",
        "race": "Human",
        "gender": "Female",
        "age": 28,
        "organization": "The Enclave",
        "connection": 1,
        "description": "Tall, rail-thin, and beautiful, with long ebony hair and brilliant green eyes; speaks rarely and always to the point, carrying an air of ineffable sadness as though she foresees a dark future.",
        "background": (
            "Married to Leroy, the Enclave's leader. When Oscuro's lieutenant Enganar demands her in "
            "exchange for peace and kills the runners' earlier ally Tela to prove his resolve, Talia "
            "slips away alone to surrender herself and spare the Enclave, leaving only a note reading "
            "'I love you.' The runners rescue her from her escort before she reaches Oscuro."
        ),
        "notes": (
            "B4 Q5 S3 C5 I5 W6, Reaction 5; Armed Combat 3, Leadership 2, Psychology 4, Stealth 5. At the "
            "siege's climax, as a runner heals the mortally wounded Leroy, Talia stabs herself in the "
            "heart; their mingled blood and the healing magic together transform the barren wasteland "
            "into fertile land, ending the adventure's central symbolic arc."
        ),
    },
    {
        "name": "Gareth",
        "role": "Leroy's security chief and first lieutenant in the Aftermath Place; loyal to the death, deeply distrustful of the runners",
        "archetype": "Physical Adept",
        "title": "Security chief, the Enclave",
        "race": "Human",
        "gender": "Male",
        "age": 38,
        "organization": "The Enclave",
        "connection": 1,
        "description": "A big, scarred physical adept nearly two meters tall, dark hair and eyes against pale skin; utterly devoted to Leroy and to everything the Enclave stands for, and takes his security duties with grim seriousness. Orders the runners flatly at their first meeting: 'My name is Gareth. Go with Maranda. Leroy will speak with you later,' and walks off assuming obedience.",
        "notes": "B6 Q4 S6 C3 I4 W6, Reaction 6; Armed Combat 5, Leadership 4, Projectile Weapons 5 (Crossbows 7); Improved Ability (Projectile Weapons +2), Increased Reaction (+2), Increased Reflexes (+1). Fights at Leroy's side through the final siege.",
    },
    {
        "name": "Maranda",
        "role": "Enclave scout leader who rescues the runners from an alacorn and first brings them into the settlement",
        "archetype": "Physical Adept",
        "title": "Scout leader, the Enclave",
        "race": "Human",
        "gender": "Female",
        "age": 32,
        "organization": "The Enclave",
        "connection": 1,
        "description": "Black-haired, whipcord-muscled physical adept archer with a marathoner's build and the pale, weathered complexion typical of the Enclave; guarded and observant, rarely says more than she must. Steps forward unarmed after the alacorn fight and demands, 'I am Maranda. Who are you, and where does your allegiance lie?' -- and treats the runners' visible use of magic with instant suspicion.",
        "notes": "B5 Q6 S4 C4 I5 W6, Reaction 4(5); Armed Combat 4, Etiquette (Enclave) 6, Leadership 2, Projectile Weapons 4 (Bows 6), Stealth 3 (Wilderness 5); Combat Sense (2), Improved Ability (Projectile Weapons +2), Increased Reaction (+1), Increased Reflexes (+1). Leads Tela and Brannen on the patrol that first meets the runners.",
        "contact_skills": ["Enclave scouting and wilderness survival in the Aftermath wasteland"],
    },
    {
        "name": "Tela and Brannen",
        "role": "Sister physical-adept scouts of the Enclave who first fight beside the runners, then defect to the Collective -- Tela is later murdered as a blood sacrifice",
        "archetype": "Physical Adept",
        "title": "Scouts, the Enclave (later defectors)",
        "race": "Human",
        "gender": "Female",
        "organization": "The Enclave",
        "connection": 1,
        "description": "Younger sisters of similar build to Maranda, less self-assured and openly distrustful of outsiders; both physical-adept archers who fight alongside the runners against the alacorn but refuse to speak to them without Maranda's leave.",
        "background": (
            "Visibly drawn to the affluent, well-fed delegates the Collective sends to court the Enclave; "
            "after one such delegation departs, both sisters secretly follow it back to Oscuro's "
            "settlement and defect. Enganar later drags Tela out at the Enclave's gate and cuts her throat "
            "to power the Ram spell that shatters it, delivering Oscuro's ultimatum for Talia in blood."
        ),
        "notes": "B5 Q4 S4 C3 I4 W6, Reaction 4(5); Armed Combat 4, Etiquette (Enclave) 5, Projectile Weapons 3 (Bows 5); Combat Sense (1), Improved Ability (Projectile Weapons +2), Increased Reaction (+1), Increased Reflexes (+1). Brannen's fate after the defection is not stated on the page.",
    },
    {
        "name": "Oscuro",
        "role": "Leader of the rival Collective in the Aftermath Place; Darke's avatar here, a shapeshifter between a cruel human form and an amorphous horror",
        "archetype": "Mage",
        "title": "Leader, the Collective",
        "race": "Human",
        "gender": "Male",
        "organization": "The Collective",
        "connection": 2,
        "description": (
            "Prefers a small, slightly built, cruelly handsome human form -- short dark hair, blue-gray "
            "eyes, an aquiline nose -- carrying only a knife that doubles as a Rating 4 weapon focus and a "
            "hooded pet 'falcon' (actually a local eyekiller variant) on his wrist. His true form is an "
            "amorphous, multi-limbed horror with dozens of eye-like protrusions, faster and reeking of "
            "rotting meat; he assumes it only in dire emergency, since it visibly breaks his own army's "
            "morale."
        ),
        "notes": (
            "Grade 4 Initiate. Human/true-form stats: B6/9 Q8/11 S4/8 C4/-- I5/5 W6/6, Reaction 8/8; "
            "Armed Combat 8, Sorcery 6, Leadership 6; spells include Animate, Chaotic World, Death Touch, "
            "Fire Strike, Hellblast, Power Bolt, and more, several boostable by sacrificing a bodyguard's "
            "life. Commands the Collective's siege of the Enclave from horseback (or in true form); "
            "defeating or driving him off yields the leather hood the Songbird needs, which he drops "
            "when he looses his eyekiller in a last-ditch defense."
        ),
    },
    {
        "name": "Enganar",
        "role": "Oscuro's toxic-shaman lieutenant who delivers the Collective's brutal ultimatum for Talia, killing Tela as a blood sacrifice",
        "archetype": "Toxic Shaman",
        "title": "Lieutenant, the Collective",
        "race": "Human",
        "gender": "Male",
        "organization": "The Collective",
        "connection": 1,
        "description": (
            "A large man dressed even more extravagantly than the Collective's usual delegates, with a "
            "nightmare grin of pure sadistic glee; a toxic shaman following the Alacorn totem who "
            "genuinely relishes his cruelty. Announces himself under a white flag: 'I am Enganar, and I "
            "bring a message from Master Oscuro. He wishes to know if you want peace... Would you pay a "
            "price for peace?' When Leroy asks what price, he points at Talia: 'Her! Your wife.'"
        ),
        "notes": (
            "B6 Q4 S5 C6 I6 W6, Reaction 5; Armed Combat 5, Conjuring 6, Sorcery 6; spells include a "
            "modified Barrier (invisible personal shield), Flamethrower, Increase Reflexes, and Ram (used "
            "to shatter the Enclave's gate). Armed with a Force 4 toxic land spirit escort. Cuts Tela's "
            "throat in front of the Enclave to demonstrate the Collective's resolve, then laughs off "
            "Leroy's answering crossbow bolt, which stops dead an inch from his skin: 'I have your answer, "
            "then. It will be war. And the Enclave will fall as easily as that gate.'"
        ),
    },
    {
        "name": "Bellaco",
        "role": "Sadistic elf hermetic mage who leads the escort taking the surrendered Talia toward Oscuro, until the runners intercept them",
        "archetype": "Combat Mage",
        "title": "Escort leader, the Collective",
        "race": "Elf",
        "gender": "Male",
        "organization": "The Collective",
        "connection": 1,
        "description": "An almost caricatured, exaggerated elf who takes open pleasure in cruelty and humiliating a defeated enemy; a hermetic mage who draws his own blood with a knife to power his spells. Caught describing to a bound Talia how his men mean to 'entertain' themselves with her when the runners find them.",
        "notes": (
            "B4 Q6(11) S4 C3 I6 W4, Reaction 6(8); Armed Combat 5, Conjuring 3, Sorcery 6; Grade 2 "
            "Initiate. Oscuro has personally cast and Quickened an Increase Quickness (+4) spell on him. "
            "If cornered without hope of winning, he tries to kill Talia to boost a final spell's Force. "
            "Ambushes his five-man escort at a ravine breather stop, where the runners catch up and rescue "
            "Talia."
        ),
    },
    {
        "name": "Arlen Bergamot",
        "role": "Reluctant sheriff of Valley Hope in the A Fistful of Karma Place; Harlequin's local avatar, broken down by Mr. Trey's manipulation and rebuilt by the runners' support",
        "archetype": "Gunfighter",
        "title": "Sheriff, Valley Hope",
        "race": "Human",
        "gender": "Male",
        "organization": None,
        "connection": 2,
        "description": (
            "A courageous, decisive lawman when not under Trey's psychological assault; bears a distinct "
            "physical resemblance to Harlequin, whose avatar he is. Once a saddle tramp gunslinger with "
            "'a gun like lightning.' Found drunk and despairing before the showdown: 'I stood up to these "
            "monsters once, long ago. But then I had the people standing behind me... Now I'm alone. "
            "Don't you understand that? Alone!' Faces Francis at high noon with a flat, 'My job, I think, "
            "friends,' answered by Francis' 'Seems we been here before' and his own 'Never again.'"
        ),
        "background": (
            "Arrived in Valley Hope years ago to claim a small inheritance from a murdered brother, ended "
            "up building the evidence to indict the Flattop mine's manager for that murder, then agreed to "
            "lead a citizens' Vigilance Committee that broke both the mine's grip on the town and Sy "
            "Vants' Blood Eagle gang, wounding and jailing Vants' gunman Dred Francis in the process. Six "
            "years later, with Francis released and Trey's psychological pressure mounting, Bergamot is "
            "found drunk and despairing days before the showdown; the runners can talk him back to his "
            "feet in time for High Noon."
        ),
        "notes": (
            "B4 Q6 S4 C5 I4 W2, Reaction 5; Armed Combat 6, Firearms 8, Leadership 4, Negotiation 6, "
            "Riding 5, Whip 5; carries a bullwhip, a bowie knife, two throwing knives, a heavy pistol "
            "loaded with argent (silver) rounds, and an argent-loaded heavy rifle. Faces Dred Francis and "
            "a resurgent Sy Vants alone at high noon unless the runners stand with him."
        ),
    },
    {
        "name": "Celia",
        "role": "Mute barmaid and former singer at the Songbird Saloon; Thayla's local avatar, brutalized into silence by Sy Vants years before the runners arrive",
        "archetype": "Face",
        "title": "Barmaid, Songbird Saloon",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": "A compassionate, pale-skinned, black-haired woman whose trauma has not broken her will; used to sing at the Songbird until Sy Vants beat her nearly to death for resisting him, leaving her unable to speak or sing since. Her first word after the High Noon showdown, hands still at her throat, is a single 'Thank you.'",
        "notes": (
            "B3 Q4 S2 C6 I4 W6, Reaction 4; Negotiation 4, Singing 6, Unarmed Combat 3. Publicly tormented "
            "by Vants during the Hooraw! scene and taken hostage during the High Noon showdown; her voice "
            "returns the instant she screams to warn Bergamot, and Bergamot's cry of 'Sing!' turns her "
            "restored voice into a weapon (10S damage per Combat Turn) that finally kills Trey's true "
            "monstrous form."
        ),
    },
    {
        "name": "Sy Vants",
        "role": "Wealthy, physically enhanced rancher terrorizing Valley Hope; the dark warrior's avatar in the A Fistful of Karma Place, sadistically fixated on Celia",
        "archetype": "Physical Adept",
        "title": "Boss, Blood Eagle Gang",
        "race": "Human",
        "gender": "Male",
        "organization": "Blood Eagle Gang",
        "connection": 2,
        "description": (
            "A near-insane physical adept combining inherited wealth with a lust for power and a "
            "possessive, sadistic obsession with Celia that borders on madness; a coward at heart when he "
            "faces real resistance rather than the cowed town he expects. Swaggers into the Songbird "
            "demanding service -- 'This here's a saloon, ain't it? Whaddya gotta do t'get a drink in "
            "here?' -- and, if crossed, backs out screaming, 'Yer all dead men. Y'hear me?! Dead men!'"
        ),
        "background": "Son of one of Valley Hope's first settlers who treated the whole valley as his feudal preserve; broken once by Sheriff Bergamot's Vigilance Committee years ago (shot in the arm, publicly horsewhipped out of town) but bought his way out of prison and has quietly rebuilt the Blood Eagle gang since, backed by Mr. Trey's mine money.",
        "notes": (
            "B5(6) Q6 S6 C4 I3 W3, Reaction 4; Armed Combat 6, Firearms 6, Riding 8; Improved Body 1, "
            "Improved Unarmed Combat Skill 3, Increased Reflexes 1, Pain Resistance 5. Fatally shot at the "
            "High Noon climax but, in one staged version of the ending, drags himself back onto his feet "
            "on 'sheer hate' for one last attack before finally falling for good."
        ),
    },
    {
        "name": "Dred Francis",
        "role": "Sy Vants' cybered gunslinger, released from territorial prison to finish breaking Valley Hope; the town's most feared enforcer",
        "archetype": "Gunfighter",
        "title": "Top gunslinger, Blood Eagle Gang",
        "race": "Human",
        "gender": "Male",
        "organization": "Blood Eagle Gang",
        "connection": 1,
        "description": "A killing machine whose mere name terrified Valley Hope for years before Sheriff Bergamot wounded and jailed him; returns on the noon steamer specifically to settle that old score, greeting Bergamot with an unhurried, 'Seems we been here before... Whenever you like, sheriff.'",
        "notes": (
            "B4(5) Q4(6) S4(5) C2 I3 W2, Reaction 3(7); Armed Combat 6, Firearms 8, Riding 6; Cyberarm with "
            "Gun Hand, Cybereye with Smartgun Lens, Dermal Armor 1 (animal bond), Muscle Implant 2 (animal "
            "bond), Wired Reflexes 2 (clockwork). Faces Bergamot in a one-on-one duel at High Noon."
        ),
    },
    {
        "name": "Mr. Trey",
        "role": "Courteous, unnervingly persuasive Flattop Mining Company representative; Darke's avatar in the A Fistful of Karma Place, feeding on the town's engineered despair",
        "archetype": "Mage",
        "title": "Representative, Flattop Mining Company",
        "race": "Human",
        "gender": "Male",
        "organization": "Flattop Mining Company",
        "connection": 2,
        "description": (
            "Tall, handsome, and persuasive in his human guise; his true form is a monstrous serpent-"
            "bodied horror with a second pair of arms and an elongated, three-eyed, needle-toothed face. "
            "Can teleport freely within the valley at night (never by day, and never on horseback, which "
            "he loathes) and paralyze victims with terror via an 'icy hand' power. Steps from the smoke of "
            "his own arson to tell the beaten town: 'You have all been very brave. Honorable, "
            "courageous... and very, very annoying. Unfortunately, you are also more competent than my "
            "late associates,' before his face 'shudders and shifts' into something horrible: 'If you "
            "cannot afford me amusement, then you can die.'"
        ),
        "background": (
            "Drawn to Valley Hope by the legacy of the mine's pollution and the town's twisted history; "
            "spent a year quietly gaining control through human pawns (Vants, corrupted townsfolk) with "
            "the ultimate goal of reopening the mine not for phlogiston but to destroy the valley's "
            "ecology and feast on the resulting misery."
        ),
        "notes": (
            "Human/true form: B7/9 Q8x3/10x3 S4/6 C6/8 I6/8 W8/8, Reaction 17/19; Negotiation 8, Riding 3, "
            "Sorcery 8; sends a Force 8 fire elemental to burn Valley Hope's land office and animates a "
            "corpse into a monster to attack the town. Dies at the climax to Celia's restored, weaponized "
            "singing voice, exploding and leaving behind the white bone the runners need for the "
            "Songbird's perch."
        ),
    },
    {
        "name": "Jed Porkins",
        "role": "Ork owner of the Songbird Saloon in Valley Hope; welcomes hero runners with free rooms and a round on the house",
        "archetype": "Shopkeeper",
        "title": "Owner, Songbird Saloon",
        "race": "Ork",
        "gender": "Male",
        "organization": None,
        "connection": 1,
        "description": "The nervous, sweating saloonkeeper Sy Vants addresses only as 'Porky.' Warily approaches Vants' table with 'What can I get you fellas, Sy?' and, cowed by the threat, scuttles off to fetch Celia with a stammered, 'OK, OK. I'll send her out.'",
        "background": "Lives next door to the saloon he owns and runs; makes the runners welcome with free rooms and a round of drinks after their public heroics fighting the mine monster or the landsteamer robbers.",
        "notes": "Sets the Songbird Saloon's price list (Dragon's Breath cordial, meals, rooms, entertainment) and stocks the town's one hospitable base for the runners' stay in Valley Hope.",
    },
    {
        "name": "Kendall Silver",
        "role": "Elf editor of the Valley Hope Clarion; a source of the town's history and one of the citizens who backed Bergamot's Vigilance Committee",
        "archetype": "Reporter",
        "title": "Editor, Valley Hope Clarion",
        "race": "Elf",
        "gender": "Male",
        "organization": None,
        "connection": 1,
        "description": "Runs the town's newspaper out of the Clarion offices on Main Street; one of three community leaders (with Doc Wunderlich and attorney Simon Renfrew) who worked alongside Bergamot to break Sy Vants' power in the valley six years ago.",
        "notes": "Freely tells runners the valley's Town History without requiring a Success Test: how the mine poisoned the water, how Vants ruled the range like feudal property, and how Bergamot's Vigilance Committee broke both.",
    },
    {
        "name": "Doc Wunderlich",
        "role": "Valley Hope's town physician; another source of the valley's history and a former ally of Bergamot's Vigilance Committee",
        "archetype": "Doctor",
        "title": "Physician, Valley Hope",
        "race": "Human",
        "gender": "Male",
        "organization": None,
        "connection": 1,
        "description": "Runs a crude-by-2055-standards infirmary in town; a steady, practical voice among the citizens who once helped Bergamot put steel into the valley's spine against Sy Vants.",
        "notes": "One of the three community leaders who can recount Valley Hope's Town History to the runners without a Success Test; treats wounded runners in his surgery at ordinary care, not hospital-grade, quality.",
    },
    {
        "name": "Simon Renfrew",
        "role": "Valley Hope's attorney; a source of local business and legal history, and another Vigilance Committee veteran",
        "archetype": "Lawyer",
        "title": "Attorney, Valley Hope",
        "race": "Human",
        "gender": "Male",
        "organization": None,
        "connection": 1,
        "description": "Keeps his office on Main Street and can answer questions about business matters in the valley as readily as the town's history; part of the trio (with Silver and Wunderlich) who backed Bergamot's Vigilance Committee against Sy Vants and the mine.",
        "notes": "Freely recounts Valley Hope's Town History to the runners without a Success Test.",
    },
    {
        "name": "Winch Wardell",
        "role": "Proprietor of Wardell's Emporium, Valley Hope's general store",
        "archetype": "Shopkeeper",
        "title": "Proprietor, Wardell's Emporium",
        "race": "Human",
        "gender": "Male",
        "organization": None,
        "connection": 1,
        "description": "Runs the general-goods emporium on Valley Hope's Main Street, the town's practical source for supplies during the runners' stay.",
        "notes": "Named only as the Emporium's proprietor; no dialogue given in the text.",
    },
    {
        "name": "Mrs. Venturi",
        "role": "Apothecary in Valley Hope, selling first-aid supplies to the runners",
        "archetype": "Shopkeeper",
        "title": "Apothecary, Valley Hope",
        "race": "Human",
        "gender": "Female",
        "organization": None,
        "connection": 1,
        "description": "Sells bandages, herbal poultices, and antiseptic at 50 cents per unit from her Main Street apothecary -- Valley Hope's closest thing to a pharmacy.",
        "notes": "Named only as the apothecary's proprietor; no dialogue given in the text.",
    },
    {
        "name": "Max Hammel",
        "role": "Blacksmith and liveryman of Valley Hope, boarding the town's horses and thunderfeet",
        "archetype": "Shopkeeper",
        "title": "Smith and liveryman, Valley Hope",
        "race": "Human",
        "gender": "Male",
        "organization": None,
        "connection": 1,
        "description": "Runs the smithy and livery stable on Train Street, charging 25 cents a night to board a horse and 50 cents for a thunderfoot.",
        "notes": "Named only as the smithy's proprietor; no dialogue given in the text.",
    },
    {
        "name": "Parson and Mrs. Emmerick",
        "role": "Ork couple running Valley Hope's church, parsonage, and schoolhouse; the parson doubles as the town's exorcist",
        "archetype": "Clergy",
        "title": "Parson and schoolteacher, Valley Hope",
        "race": "Ork",
        "gender": None,
        "organization": None,
        "connection": 1,
        "description": "Parson Emmerick tends the church, its new clockwork steeple visible across town, and is also a fire-and-water magician kept busy putting down the increasingly common angry spirits and toxic critters plaguing the valley. Mrs. Emmerick teaches at the attached schoolhouse.",
        "notes": "A townsman's legwork line sums up the pressure on them both: 'Tetchy fire critter tried to burn down the livery last week. Well, I hope to tell ya, it was a near thing.'",
    },
    {
        "name": "Lancelot",
        "role": "Aged, guilt-broken traitor knight of the By the Sword Place; Harlequin's local avatar, who killed the true finest knight of the Round Table out of jealous rage",
        "archetype": "Knight",
        "title": "Knight (retired); hermit",
        "race": "Human (half-fay)",
        "gender": "Male",
        "age": 70,
        "connection": 1,
        "description": "Stooped with age, tall, gray-haired, hazel-eyed, arthritic hands; lives alone in a rough stone hut, devout in his adopted Christian faith and visibly ashamed of a secret he barely holds in check by clutching a bronze cross to his chest and reciting a simple prayer over and over when pressed.",
        "background": (
            "In this Place's pagan, pre-Grail version of the legend, Lancelot was never the finest knight "
            "of the Round Table -- that was Gawaine, whom Lancelot killed out of jealous, frenzied lust "
            "for Guinevere, the sword's tip snapping off in Gawaine's flank. Half-fay through his mother, "
            "a Priestess of Avalon, Lancelot has spent decades in guilt-wracked isolation, torn between his "
            "Christian self-image and the fay nature he refuses to accept."
        ),
        "notes": (
            "B3 Q2 S5 C6 I6 W6, Reaction 6; Armed Combat 4 (Sword 8), Etiquette (Court) 8, Leadership 8, "
            "Military History (Albion) 10. Gives up the broken half of his sword to runners who show "
            "compassion and honesty. At the story's climax he kneels at the lakeshore and drives Excalibur "
            "through his own chest as his final atonement, dying at peace and returning at last to Avalon."
        ),
    },
    {
        "name": "Gawaine",
        "role": "The true finest knight of the Round Table in the By the Sword Place, murdered by Lancelot; his spirit and legacy resemble Ehran the Scribe",
        "archetype": "Knight",
        "title": "Finest Knight of the Round Table (deceased)",
        "race": "Human",
        "gender": "Male",
        "age": 45,
        "connection": 1,
        "description": "Strikingly handsome, wavy blond hair, blue eyes, a ready smile; appears only as a spectral form hovering within Castle Maydenlande's stained-glass rose window, a visible sword wound on his hip. Speaks little but unfailingly politely, especially to female runners, telling them simply: 'Find Lancelot, and take him to the Lady of the Lake.'",
        "background": (
            "Champion of the pagan Goddess and the true measure of knightly honor in this Place's telling; "
            "his death at Lancelot's hand left the land barren and cursed his son Guinglainn with amnesia "
            "and imprisonment. Bears a striking resemblance, the text notes, to Ehran the Scribe."
        ),
        "notes": "Appears only when summoned by a male runner's blood sacrifice with the broken sword-tip; confirms Lancelot's guilt, commands the runners to reunite Lancelot with the Lady of the Lake, and vanishes.",
    },
    {
        "name": "Guinglainn",
        "role": "Gawaine's amnesiac, magically imprisoned son; freed by the runners, he becomes the new Champion of Spring and mends the broken sword",
        "archetype": "Knight",
        "title": "Champion of Spring (upon his release)",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": "A young man of 1.7 meters, medium build, wavy blond hair, blue eyes -- strikingly like his father Gawaine. Held dormant inside a plant-pod behind a wall of living, retaliating thorns, cursed with simple-minded amnesia but protected by near-total invulnerability while the curse holds. Wakes confused, remembering only: 'I was walking in the snow and I saw a raven lying wounded on the ground, blood around it. When I saw this, I fell into a trance. I know nothing else.'",
        "background": "The Goddess both cursed and protected him -- madness and amnesia in exchange for invulnerability -- to preserve him until the land's need was greatest. Once freed, he can enter neither Lancelot's hut (the old knight cannot bear his presence) nor Umberley-adjacent trials, but joins the runners for the rest of the adventure as a companion.",
        "notes": (
            "B2 Q5 S0 C5 I5 W4, Reaction 5; Armed Combat 4 (Sword 8), Athletics 5, Etiquette (Court) 6. "
            "His Strength rises by 1 between 11 a.m. and 1 p.m., echoing his father's waxing and waning "
            "prowess. At the story's climax, restored to his full self, he says only 'The blade is still "
            "broken,' claims Excalibur from Nimue, and hands it to Lancelot for the old knight's final act "
            "of atonement -- 'blood must be atoned' -- then mends the broken sword with his bare hands "
            "afterward, the metal that becomes the Songbird's cage."
        ),
    },
    {
        "name": "Viviane",
        "role": "Powerful Priestess of Avalon who guides the runners through By the Sword's trials; speaks only to female runners and coincidentally resembles Jane Foster",
        "archetype": "Priestess",
        "title": "Priestess of Avalon",
        "race": "Human",
        "gender": "Female",
        "organization": "Priestesses of Avalon",
        "connection": 1,
        "description": (
            "A woman in her middle years, 1.8 meters tall, thick wavy brown hair, green eyes, dressed in a "
            "simple brown robe with a black-red-white neck scarf and a green belt; a beauty felt more than "
            "seen. The text notes she 'most resembles Jane Foster,' though this bears no significance to "
            "the plot. Also stands in, statistically, for the three fountain Priestesses Anna, Gwyar, and "
            "Belisent, who are described as aspects of the same being."
        ),
        "notes": (
            "B3 Q6 S2 C10 I8 W6, Magic 40, Reaction 7; Sorcery 10, Conjuring 40, Enchantment 40, Leadership "
            "10, Psychology 10; carries a Power Focus (8) and a Spell Lock: Mask (40). Meets female runners "
            "on the Isle of Apples, confirms Guinglainn's parentage and Lancelot's guilt when approached "
            "with compassion, gives the key clue about drawing blood at Castle Maydenlande, and can offer "
            "the optional Dream of Flowers ritual. Presides over Lancelot's final rites at the lakeshore."
        ),
    },
    {
        "name": "Nimue",
        "role": "The Lady of the Lake in the By the Sword Place; rises from the water bearing Excalibur for the story's climax",
        "archetype": "Priestess",
        "title": "Lady of the Lake",
        "race": "Elf",
        "gender": "Female",
        "organization": "Priestesses of Avalon",
        "connection": 1,
        "description": "A Priestess with an elfin beauty, girded with pearls and fine-fronded flowering lake plants; rises from the northern lake at Lancelot's call bearing Excalibur, whose power is unmistakable to any magician present.",
        "notes": "Present only for the climactic lakeside scene: hands Excalibur to Guinglainn, watches Lancelot's self-sacrifice, and gives the sword back to Guinglainn once the atonement is complete. The Maiden in The Impossible Dream physically resembles her, among others.",
    },
    {
        "name": "Bercilak",
        "role": "Powerful knight guarding Castle Maydenlande's gate with a ritual Beheading Game; represents the barren, infertile Winter Champion, not an avatar of the Enemy",
        "archetype": "Knight",
        "title": "The Winter Champion; guardian of Castle Maydenlande",
        "race": "Human",
        "gender": "Male",
        "age": 45,
        "connection": 1,
        "description": "A little over 2 meters tall, powerfully built, black hair and beard streaked with gray, gray eyes, polite but reticent; wields a personally crafted axe (Weapon Focus 4) that only he can use effectively. Kneels as if for execution when a runner accepts his game, then keeps his word to the letter two days later, returning the blow with the same weapon and the same intensity.",
        "background": "Represents the barren, infertile aspect of the land as the Winter Champion. Challenges arriving runners to the Beheading Game -- strike him, then kneel two days later to receive an identical blow in return -- as a test of courage and honor before granting entry to his mansion and, ultimately, the ruined castle beyond.",
        "notes": (
            "B7 Q6 S7 C3 I4 W6, Reaction 5; Armed Combat 10 (Axe 12), Athletics 5, Etiquette 6. A runner "
            "who does not flinch when the return blow falls passes the game outright, rejuvenating "
            "Bercilak to youth and opening the castle gate; failure or violence forces a straight fight "
            "for his keys instead. Bans all trolls from his mansion (giants remind him too much of them)."
        ),
    },
    {
        "name": "Ragnall",
        "role": "Bercilak's wife at Castle Maydenlande's mansion; sets a temptation trial (the 'Test of Virtue') for the runner she selects",
        "archetype": "Priestess",
        "title": "Bercilak's wife",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": "Surpassingly beautiful, honey-blond hair, green eyes, fine pale skin, dressed in green edged with yellow with a matching lace belt; could pass for Winlogee's sister rather than her mother. Wakes her chosen runner alone at night, dressed provocatively, and when he demurs out of respect for her marriage, claims, 'her husband is impotent,' and presses harder still.",
        "notes": "Uses Viviane's game statistics if needed. A runner who resists (Willpower 6) passes the Test of Virtue and earns her lace belt as a keepsake, useful later at Castle Maydenlande proper.",
    },
    {
        "name": "Winlogee",
        "role": "Bercilak's daughter, cursed by an enchantment to be beautiful by day or by night but never both; her Riddle Game tests a chosen runner's understanding",
        "archetype": "Priestess",
        "title": "Bercilak's daughter",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": "As beautiful as her mother Ragnall, honey-blond hair and green eyes, dressed in pale blue trimmed with cream lace and a white lace choker; visibly conflicted about her attraction to a chosen male runner, and unmistakably ambivalent through dinner and breakfast alike.",
        "notes": (
            "Uses Viviane's game statistics if needed. Seduces her chosen runner in a darkened room, then "
            "throws back her veil to reveal an aged hag's face on a young woman's body, and asks him to "
            "choose whether she should be beautiful by day or by night. The correct answer ('the choice "
            "should be hers') breaks the curse permanently and earns her lace choker, a further "
            "target-number discount at Castle Maydenlande proper."
        ),
    },
    {
        "name": "The Crone",
        "role": "A destructive aspect of the Goddess who guards the entrance to Gawaine's Great Hall at Castle Maydenlande",
        "archetype": "Priestess",
        "title": "Guardian of the Great Hall, Castle Maydenlande",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": "An old woman dressed entirely in black, white-haired and green-eyed, stooped and hard-faced, seated amid dusty furniture and filthy drapes in a ruined chamber.",
        "notes": (
            "Interrogates arriving runners on their purpose before deciding how hard to test them; the "
            "Force Rating of her attack spells drops by one for each of three required points the runners "
            "successfully make (that they come to free Gawaine's line, that they serve the Priestesses' "
            "will, and that they offer their own sacrifice). Sorcery/Conjuring 12, base spell Rating 8, "
            "immune to perception- and volition-affecting magic, will not attack Guinglainn or any female "
            "runner who experienced the Dream of Flowers. Her weapon focus loses its power if removed from "
            "this Place."
        ),
    },
    {
        "name": "The Architect",
        "role": "Elf tinkerer haunting the ruined Village in the Impossible Dream Place; Harlequin's local avatar, tormented by having designed the Tower that doomed his people",
        "archetype": "Mage",
        "title": "The Architect (self-styled)",
        "race": "Elf",
        "gender": "Male",
        "connection": 1,
        "description": "An aged elf so overgrown with clockwork-like machinery that it seems to have grown into him like vines; wound to life by a key lodged between his shoulder blades. Answers questions about his identity only in ritualistic, riddling monotone: 'Who am I? I am Thomas Alva Edison. I am Henry Ford. I am the Genie who can make your dreams come true. I am the Monkey's Paw that can turn your dreams into nightmares. I am Pandora's Box. I am the Architect.'",
        "background": (
            "As a young man he loved a Maiden of uncommon beauty from afar and, hoping to win her, agreed "
            "to design the Village's Tower when the tempter-serpent Foreman promised the villagers "
            "treasure from the sky. When the Tower failed to reach it, the villagers blamed him and turned "
            "to the Foreman instead, abandoning the Village to labor and die in the Tower's upper reaches; "
            "the Maiden stayed with him as long as she could before following her people in, vowing to "
            "bring them back, and never returned."
        ),
        "notes": (
            "B3 Q3 S3 C4 I8 W8, Reaction 5; Architecture 10, Metalworking 8. Forged a magic sword meant to "
            "kill the Foreman but could not bring himself to wield it; gives it to runners who swear to "
            "find the Maiden. Cannot bring himself to enter the Tower under any circumstances. At the "
            "story's end, reunited with the freed Maiden, builds the Songbird's cage from Lancelot's "
            "sword and Trey's bone at the runners' request."
        ),
    },
    {
        "name": "The Maiden",
        "role": "A nameless, painfully shy prisoner held by the Foreman deep in the Impossible Dream's Tower Labyrinth; Thayla's local avatar",
        "archetype": "Face",
        "title": "The Foreman's prisoner",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": "A beautiful girl found lying inside a chalk circle in a bare room papered with obituaries of everyone the runners have ever killed, a metal clamp sealing her mouth shut; physically resembles Talia, Celia, and Nimue, though the text notes none of them truly resembles her either.",
        "background": "Imprisoned years ago by the Foreman, who threatened to kill the Architect if she ever left the chalk circle or the room; she has never dared test the threat and has forgotten her own name.",
        "notes": (
            "B2 Q4 S2 C6 I6 W8, Reaction 5; Singing 10. Cannot cross the chalk circle unassisted even once "
            "it is erased -- she must be physically carried across, which triggers the room's dissolution "
            "and a flashback confrontation with the Foreman. Freed of her gag only when the Foreman dies "
            "and drops the key from his ashes; afterward persuades the Tower's villagers to abandon the "
            "climb and sings the panicking crowd calm as the Tower collapses."
        ),
    },
    {
        "name": "The Foreman",
        "role": "The white-suited tempter who lured the Village into building the impossible Tower; Darke's avatar in the Impossible Dream Place",
        "archetype": "Mage",
        "title": "The Foreman",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": (
            "Appears first as a heavyset man in a white suit fidgeting with rosary beads on a trideo "
            "screen in the Limbo Room (as 'Bill Foreman'), later as the same man in the Village and Tower, "
            "his lower body ending in a scorpion-like tail and his mouth lined with fangs when he sheds "
            "pretense. Resembles Oscuro and Mr. Trey. Offers the runners an escape from the quest in "
            "smooth, oily concern: 'You are involved in something you cannot hope to understand. If you "
            "persist, you will face powers you cannot hope to overcome... I implore you to reconsider.' "
            "Refused, his image simply mutters, 'Pity,' before dissolving into a shrieking skull that "
            "orders the attack."
        ),
        "background": (
            "Told the Village's simple people they were poor and enslaved, and that treasure waited above "
            "the clouds if only they built a Tower tall enough to reach it; recruited the lovesick young "
            "Architect to design it and stayed on as construction foreman while the villagers abandoned "
            "their homes, fields, and eventually their lives to keep climbing."
        ),
        "notes": (
            "B4 Q6 S5 C4 I6 W2, Reaction 5(9); Firearms 6, Unarmed Combat 7. First encountered as a "
            "false-Matrix bribery attempt in the Limbo Room (offering an open-ended temptation to abandon "
            "the quest), backed by the enforcer Eve, the hitman Blazer, and one thug per runner; later "
            "found in the Village sealing the Architect into a wall with his minions before the runners "
            "intervene. Dies curling into a ball and bursting into flame, leaving a silver key that "
            "unlocks the Maiden's gag."
        ),
    },
    {
        "name": "Eve",
        "role": "The Foreman's cybered samurai enforcer in the Limbo Room, targeting male characters with high Charisma",
        "archetype": "Street Samurai",
        "title": "Enforcer",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": "A vicious cybered samurai bodyguard who accompanies the Foreman's Limbo Room persona, watching the runners with open suspicion before opening fire once the bribe is refused; the lead singer of the club's house band breaks into an a cappella 'Games without Frontiers' as she and Blazer take up position at the booth.",
        "notes": "B4 Q6 S5 C5 I4 W6, Reaction 2(5); Armed Combat 6, Firearms 4, Unarmed Combat 5; Cybereyes (low-light, thermographic, flare compensation), retractable spurs, Wired Reflexes 2. Attacks only male characters, prioritizing the highest Charisma first.",
    },
    {
        "name": "Blazer",
        "role": "The Foreman's hitman in the Limbo Room, holding fire until a runner starts casting spells",
        "archetype": "Hitman",
        "title": "Hitman",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": "A patient professional who lets the Limbo Room ambush unfold around him, waiting specifically for a spellcaster to reveal themselves before opening up with his SMG.",
        "notes": "B3 Q5 S4 C5 I5 W5, Reaction 5(7); Firearms 5, Unarmed Combat 4; Dermal Plating 1, Smartlink, Wired Reflexes 1. Carries an armor jacket, a Browning Max-Power, and an HK227 with Gas Vent II and Smartlink.",
    },
    {
        "name": "Toady",
        "role": "A babbling, cowardly little frog-man who pesters climbing runners with endless nosy questions in the Impossible Dream's Tower",
        "archetype": "Spirit",
        "title": "Playful spirit",
        "race": "Unknown",
        "gender": "Male",
        "connection": 1,
        "description": "A tiny, warty froggyman who hoppy-hops up to the runners babbling about 'wut are dey doin' and 'wut is dat' in a broken, childish patter, going on and on about nothing in particular. Runs off crying at the first hint of a fight or a harsh word.",
        "notes": "One of the random 'Playful Spirits' the gamemaster may roll up while the runners climb the Tower; pure comic-relief color, harmless and easily driven off.",
    },
    {
        "name": "Morris",
        "role": "A shy gnomelike spirit who offers climbing runners a mysterious black box he cannot explain",
        "archetype": "Spirit",
        "title": "Playful spirit",
        "race": "Unknown",
        "gender": "Male",
        "connection": 1,
        "description": "A gnomelike creature who waits quietly on the climb with a big black box in his lap, speaking only if spoken to. If asked about the box, he hands it over readily, warning that it 'could contain just about anything and that they should be careful.'",
        "notes": "One of the random 'Playful Spirits' the gamemaster may roll up on the Tower; the box's actual contents are left entirely to the gamemaster's discretion.",
    },
    {
        "name": "Mister Mystery",
        "role": "A self-styled 'living enigma' spirit conjured by a rune-marked talisman on the Impossible Dream's Tower",
        "archetype": "Spirit",
        "title": "Playful spirit",
        "race": "Unknown",
        "gender": "Male",
        "connection": 1,
        "description": "Dressed entirely in black, his eyes glowing green fire, Mister Mystery appears from a touched talisman and tries to draw runners into pointless, cryptic exchanges, turning every question back on the asker until they give up on him -- at which point he vanishes 'mysteriously.'",
        "notes": "One of the random 'Playful Spirits' the gamemaster may roll up on the Tower; wastes time rather than threatens the runners.",
    },
    {
        "name": "Stokes",
        "role": "Lord Umberley's butler at Umberley Manor; the first of Nacht's two murder victims",
        "archetype": "Servant",
        "title": "Butler, Umberley Manor",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": "A tall, thin man in formal butler's attire who greets the runners at the manor door with 'Welcome to Umberley Manor. I am Stokes. You are just in time for the festivities,' and shows them to their rooms; found stabbed to death in the mansion's secret passage maze shortly afterward.",
        "notes": "His murder is the runners' first clue that something violent is loose in Umberley Manor beyond the masquerade's genteel surface; Lord Umberley may later try to pin the killing on the runners if it goes undiscovered.",
    },
    {
        "name": "Colonel Quinn",
        "role": "Guest of Lord Umberley at the masquerade, dressed as a harlequin; publicly identified as Thayla's grieving 'uncle' and Nacht's second murder victim",
        "archetype": "Aristocrat",
        "title": "Colonel (retired); guest, Umberley Manor",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": "Tall and slender, narrow features, dark hair brushed back from a high forehead; costumed as a harlequin and bearing a striking resemblance to Harlequin himself, though he says little to the runners beyond a tentative smile and nod. Grows pale under his clown makeup when pressed about Thayla: 'She was a lovely girl, so kind and giving,' before excusing himself, unwell.",
        "background": "Introduced by Lord Umberley as an old friend, Quinn is in truth the alcoholic uncle who helped Umberley fake the death of his niece Thayla years ago so she could become Nacht's lifelong captive companion. Is stabbed to death mid-seance shortly after, staggering into the ballroom to collapse with a dagger in his back.",
        "notes": "His murder, alongside Stokes', is used by Lord Umberley and the Lord Constable to place the runners under house arrest and cast suspicion on them.",
    },
    {
        "name": "Lady Raven",
        "role": "Masquerade guest who leads a seance to contact Thayla, interrupted by Colonel Quinn's murder; her impressions point the runners toward the truth",
        "archetype": "Medium",
        "title": "Guest, Umberley Manor",
        "race": "Unknown",
        "gender": "Female",
        "connection": 1,
        "description": (
            "A tall figure in a gown of glossy black feathers with a beaked raven mask; low, rich, "
            "exotically accented voice that gives no clue to gender, though nearly everyone refers to her "
            "as female. Polite but guarded, most interested in trading secrets. Opens the seance with a "
            "flourish: 'We shall hold a seance, and I will use my gifts to call a spirit from beyond to "
            "speak to us,' then chants into the dark, 'There is resistance. All is not as it seems. I "
            "sense sorrow and regret and great anger. I cannot reach her; a dark force stands in the way, "
            "gleaming death in its hand' -- moments before Quinn's body is found."
        ),
        "notes": (
            "During her seance, before Colonel Quinn's body interrupts it, she senses that Thayla is alive "
            "rather than dead, blocked by a jealous 'dark presence,' and glimpses her held within a vast "
            "machine of gears and cogs -- the Engine. Questioned afterward without a formal test, she can "
            "confirm these impressions to the runners in roleplay."
        ),
    },
    {
        "name": "Auric",
        "role": "Golden, charismatic masquerade guest at Umberley Manor -- likely a Great Power in disguise, generous and trusting toward everyone including his host",
        "archetype": "Aristocrat",
        "title": "Guest, Umberley Manor",
        "race": "Unknown",
        "gender": "Male",
        "connection": 1,
        "description": "A young man with tanned skin, golden hair, blue eyes, and a bright smile, dressed as a French nobleman from the time of Louis XIV without the wig or face makeup; a poet's soul and a powerful, instantly likable charisma that draws admirers wherever he goes. Recites his own verse if coaxed. On Lord Umberley: 'I would not wish to debate him unprepared.'",
        "notes": "One of the masquerade's ambiguous 'Great Powers in costume' guests; the text never confirms his true nature. Later revealed to be Luna's younger brother.",
    },
    {
        "name": "Jack-in-the-Green",
        "role": "Wild, carousing masquerade guest at Umberley Manor -- likely a nature spirit or totem in disguise, contemptuous of his host beneath the revelry",
        "archetype": "Nature Spirit",
        "title": "Guest, Umberley Manor",
        "race": "Unknown",
        "gender": "Male",
        "connection": 1,
        "description": "A young man clad in furs and a crown of laurel and oak leaves, a full wine goblet perpetually in hand, drinking hard and behaving with a loud, near-rude abandon that some guests find hilarious and others merely a bore. Coherent when actually spoken to, and willing to drink a runner under the table for the chance to talk.",
        "notes": "One of the masquerade's ambiguous 'Great Powers in costume' guests. A runner who keeps pace with his drinking learns that Lord Umberley has 'something hidden, something he holds on to as tightly as a miser does his gold.'",
    },
    {
        "name": "Lady Rose",
        "role": "Beautiful, pained masquerade guest at Umberley Manor -- likely a Great Power in disguise, weeping blood behind an otherwise perfect facade",
        "archetype": "Aristocrat",
        "title": "Guest, Umberley Manor",
        "race": "Unknown",
        "gender": "Female",
        "connection": 1,
        "description": "Tall, willowy, and fair, strawberry-blond hair coiled at the nape of her neck, in a silken pink-and-gold gown that flatters her skin's faint blush -- every feature beautiful except her deep forest-green eyes, which carry a hidden, abiding pain that shows only at the edges. Occasionally dabs at her face with a handkerchief, wiping away a drop of blood.",
        "notes": "One of the masquerade's ambiguous 'Great Powers in costume' guests; pleasant but evasive with the runners. Refers to Luna, privately, as 'witch-queen.'",
    },
    {
        "name": "Luna",
        "role": "Haughty, moon-themed masquerade guest at Umberley Manor -- likely a Great Power in disguise, reserved and knowledgeable about magic",
        "archetype": "Mage",
        "title": "Guest, Umberley Manor",
        "race": "Unknown",
        "gender": "Female",
        "connection": 1,
        "description": "Pale-skinned with midnight-dark hair and eyes, dressed in soft black trimmed with a star-spangled silk wrap and a crescent pendant on a silver chain; a quiet, almost menacing presence who speaks little but drops cryptic remarks on magic to anyone who will listen. Haughty and reserved, especially with men, though strong-willed women may see her thaw slightly.",
        "notes": "One of the masquerade's ambiguous 'Great Powers in costume' guests; Lady Rose privately calls her 'witch-queen.' Admits, under pressure, that Auric is her younger brother.",
    },
    {
        "name": "Madame Rouge",
        "role": "Sultry, all-knowing masquerade guest at Umberley Manor -- likely a Great Power in disguise, embodying beauty and desire",
        "archetype": "Aristocrat",
        "title": "Guest, Umberley Manor",
        "race": "Unknown",
        "gender": "Female",
        "connection": 1,
        "description": "Clad in scarlet silks and a matching veil, Madame Rouge embodies beauty, flirtation, and desire; seems to know every secret thought the runners have ever had, coyly hinting at knowledge of their innermost wants. Her appearance and manner subtly shift to mirror whoever is looking at her -- a runner fixated on finding Thayla may briefly mistake her for the queen herself.",
        "notes": "One of the masquerade's ambiguous 'Great Powers in costume' guests.",
    },
    {
        "name": "Mother Mondas",
        "role": "Warm, motherly masquerade guest at Umberley Manor -- likely a Great Power in disguise, urging forgiveness above all else",
        "archetype": "Aristocrat",
        "title": "Guest, Umberley Manor",
        "race": "Unknown",
        "gender": "Female",
        "connection": 1,
        "description": "A heavyset, middle-aged woman of average height in a voluminous green dress, a scarf holding back long brown hair; almost overwhelmingly friendly, handing out warm hugs and listening more than she speaks. Firmly convinced that everyone has some good in them and preaches forgiveness above all else.",
        "notes": "One of the masquerade's ambiguous 'Great Powers in costume' guests.",
    },
    {
        "name": "Old Man Coyote",
        "role": "Trickster masquerade guest at Umberley Manor -- likely a totem or Great Power in disguise, answering every question with another",
        "archetype": "Nature Spirit",
        "title": "Guest, Umberley Manor",
        "race": "Unknown",
        "gender": "Male",
        "connection": 1,
        "description": "Tall and thin, with long gray braids, dressed in shapeless brown clothing under a gray cloak and broad-brimmed hat over a coyote-faced mask, leaning on a wooden staff entwined with small yellow flowers. Smiles easily, wields a biting wit, and deflects direct questions with more of the same: asked whether Lord Umberley can be trusted, he replies, 'I don't know. What do you think? You seem to suggest he can't be.'",
        "notes": "One of the masquerade's ambiguous 'Great Powers in costume' guests; a runner who makes a Perception (4) Test finds him naggingly familiar without placing why.",
    },
    {
        "name": "Ronin",
        "role": "Proud, dangerous swordsman among the masquerade's guests at Umberley Manor -- likely a Great Power in disguise, contemptuous of Lord Umberley",
        "archetype": "Street Samurai",
        "title": "Guest, Umberley Manor",
        "race": "Unknown",
        "gender": "Male",
        "connection": 1,
        "description": "A small, supremely confident oriental man in samurai garb, a pair of swords at his belt; his self-assurance borders on arrogance, and he seems perpetually to be looking for a fight. Any runner foolish enough to accept his challenge is swiftly, humiliatingly beaten but never seriously harmed.",
        "notes": "One of the masquerade's ambiguous 'Great Powers in costume' guests. A runner who treats him with proper respect finds him a genuinely useful ally: 'he cares little for Lord Umberley' and will say he believes his lordship is up to something.",
    },
    {
        "name": "Smith",
        "role": "Shy, craft-obsessed dwarf among the masquerade's guests at Umberley Manor -- likely a Great Power in disguise, fascinated by the mansion's construction",
        "archetype": "Craftsman",
        "title": "Guest, Umberley Manor",
        "race": "Dwarf",
        "gender": "Male",
        "connection": 1,
        "description": "Wears jeans, workboots, and a scorched leather apron over a T-shirt, a belt of tools at his waist and a slight limp in his step; spends the masquerade examining the mansion's architecture and furniture rather than mingling. Shy in ordinary conversation but talks readily, at length, the moment the subject turns to building or construction.",
        "notes": "One of the masquerade's ambiguous 'Great Powers in costume' guests; drifts away from any conversation that isn't about construction.",
    },
    {
        "name": "The Warden",
        "role": "Deaf, illiterate guardian of Thayla's own Songbird in her corrupted kingdom; Darke's avatar here, who cannot bear to touch or even look at the bird",
        "archetype": "Mage",
        "title": "Warden of the Songbird's Tower",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": "Three meters tall, dark-haired, swarthy-skinned, black-eyed, with a soulless laugh; resembles Oscuro, Trey, and the Foreman. Wields a long, thin-bladed sword that drips steaming blood, and begs the runners in speech he cannot know they hear, since he is deaf: 'So lovely, so fine! Kill it for me and I will give you this town. Strangle it, snap its neck, drown it, eat it, I care not. Make it be quiet.'",
        "background": "Guards the Songbird in the tower at the heart of Thayla's own ruined, corrupted kingdom, unable to communicate with the runners (deaf and fully illiterate) and unwilling to so much as look at the bird he is meant to protect.",
        "notes": (
            "B10 Q8 S8 C3 I6 W7, Reaction 11(15); Armed Combat 8, Unarmed Combat 6; Regeneration; sword "
            "does 12D damage split between Physical and Stun. Cannot kill the Songbird himself or even bear "
            "to look at it; vulnerable to the Architect's sword."
        ),
    },
    {
        "name": "Lord Umberley",
        "role": "Suave, cultured host of Umberley Manor's masquerade ball; Darke's most fully realized and named avatar, an Initiate of grade 8 hiding his monstrous brother's secret",
        "archetype": "Mage",
        "title": "Lord, Umberley Manor",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": (
            "A wealthy, bored aristocrat whose outward charm hides a devious, twisted soul willing to "
            "manipulate and destroy anyone to protect his comfort and his family's secret; black hair and "
            "neatly trimmed beard and mustache, small horns visible beneath his hairline in full "
            "masquerade dress. Resembles Oscuro, Trey, the Foreman, and the Warden. Greets arriving "
            "runners with practiced warmth -- 'How do you do? I am Lord Umberley, your host. I see you "
            "made it all right despite this wretched weather, eh?' -- and, cornered in the Engine's heart "
            "beside Nacht and the captive Thayla, drops the mask entirely: 'Fear not, dear brother... "
            "these ruffians will soon cease to trouble us... Turn back or die. The choice is yours.'"
        ),
        "background": "Arranged, years ago, for his brother Nacht's beloved -- a mute girl named Thayla from a neighboring estate -- to be declared dead by her alcoholic uncle Colonel Quinn, so Nacht could keep her as a lifelong captive companion in secret. Hosts the masquerade ball specifically to delay and, if possible, destroy the runners before they can find her.",
        "notes": (
            "B6(12) Q9 S4 C5 I8 W6, Magic 14, Reaction 6; Conjuring 7, Etiquette (Upper Class) 6, Sorcery 7, "
            "Nahuatl (his spellcasting centering language, the Aztec language) 5; Grade 8 Initiate; power "
            "focus and Rating 4 combat spell focus cane. Every wall of the mansion carries a Force 6 ward. "
            "At the climax, hurls a killing spell at Thayla when she begins to defy him; Nacht dies "
            "shielding her from it. His 'death' as an avatar only ends this Place's manifestation of Darke."
        ),
    },
    {
        "name": "Nacht",
        "role": "Lord Umberley's hidden, hunchbacked brother, kept from the world in shame; the original dark warrior of Thayla's own legend, genuinely in love with her",
        "archetype": "Street Samurai",
        "title": "Umberley's brother (concealed)",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": (
            "Hunchbacked and twisted, with huge, ape-like muscles and surprising speed; inspires both pity "
            "and disgust. Neither stupid nor foolish despite his bestial appearance and ragged clothing. "
            "Bears a superficial resemblance to Sy Vants. Snarls at the runners who finally corner him "
            "with Thayla, 'Why have you come? You cannot take her! She will not go with you!' -- and dies "
            "leaping into the path of Umberley's own killing spell, whispering to Thayla with his last "
            "breath, 'My beauty, only now do I leave your side. I love you.'"
        ),
        "background": (
            "Locked away for most of his life out of family shame, Nacht once chanced to see and fall in "
            "love with a beautiful mute girl from a neighboring estate; his brother Umberley arranged with "
            "her alcoholic uncle to fake her death so Nacht could keep her as a lifelong companion. That "
            "girl is Thayla, and Nacht himself is the original dark warrior of her ancient legend -- a "
            "creature of pure appetite who, across a very long captivity together, came to feel something "
            "he cannot name for her."
        ),
        "notes": (
            "B8 Q5 S8 C1 I3 W6, Reaction 6; Armed Combat (Knife) 6, Athletics 5, Stealth 7, Unarmed Combat "
            "7; armed with a heavy-bladed knife. Murders both Stokes and Colonel Quinn in the mansion's "
            "secret passages and rigs the Engine's catwalks with collapsing traps to keep intruders from "
            "reaching Thayla."
        ),
    },
]

ORG_UPDATES = {}
LOC_UPDATES = {}
NPC_UPDATES = {
    "Harlequin": {
        "description_append": (
            "In Harlequin's Back (a few years after the events of the original Harlequin adventure), "
            "he is drinking heavily and adrift, having lost his sense of purpose once his score with "
            "Ehran was settled. A spectral visitation -- possibly hallucination, possibly true -- warns "
            "him 'the Enemy,' ancient world-devouring creatures, will breach the Sixth World some 2,500 "
            "years early because of the background-magic spike left by the Great Ghost Dance. Jane "
            "Foster interrupts his confrontation with the vision, chrome pistol in hand: 'Harlequin's "
            "back. Can't you tell?' Fate herself chooses a team of shadowrunners for the astral quest "
            "that follows; Harlequin drives them to the ritual site in a nondescript minivan (a Pink "
            "Floyd Dark Side of the Moon T-shirt and a Brooklyn Dodgers cap this trip), explains the "
            "danger, and guides them from the Chasm and the Bridge -- the metaplanar hub he spends the "
            "whole adventure preparing for Thayla's return -- while the runners gather a hood, a perch, "
            "and cage metal for her enchanted Songbird across five other metaplanar Places."
        ),
        "notes_append": (
            "Harlequin's Back: appears as an avatar figure in most of the Places the runners visit -- "
            "Leroy (Aftermath, a walled settlement's reluctant leader), Sheriff Bergamot (A Fistful of "
            "Karma), Lancelot (By the Sword, in a version where he, not Gawaine, is the guilty traitor "
            "knight), and the Architect (The Impossible Dream, designer of a doomed Tower). As in the "
            "original adventure, the book gives him no combat statistics by design ('give it stats and "
            "someone will kill it'); his personal Essence for healing-spell purposes is treated as 8 "
            "without explanation. Grants the runners a one-time personal Karma Pool (via a threshold "
            "test) and a non-refreshing Team Karma Pool of 50 at the quest's start. Is captured, "
            "stripped, and tortured on a bone lattice by Darke before the climax at the Bridge, freed "
            "only when the runners defeat Darke there."
        ),
    },
    "Jane Foster": {
        "description_append": (
            "In Harlequin's Back she travels at Harlequin's side throughout the astral quest as his "
            "apprentice, riding shotgun in his minivan behind narrow Italian sunglasses and regarding "
            "the runners 'critically' before turning back to the desert scenery. Still does not know "
            "Ehran the Scribe is her father, or that she has inherited his immortality; Harlequin has "
            "not told her either. Reacts to the revelation of Nacht's true nature at the story's climax "
            "with a flat 'Holy frag. That was the Enemy?'"
        ),
        "notes_append": (
            "Harlequin's Back: B3 Q3 S2 C6 I5 W6, Ess 6, Magic 8, Reaction 5; Sorcery 4, Conjuring 3, "
            "Etiquette (Corporate) 5, Unarmed Combat 3; Initiate grade 2. Present throughout the quest, "
            "navigating and occasionally acting independently; her presence substitutes for a female "
            "player character where the story requires one (notably By the Sword). Grows increasingly "
            "uncertain during the quest whether it is time to move on from Harlequin's tutelage."
        ),
    },
}
TAG_EXISTING = {}

MATRIX_HOSTS = """
The only "Matrix"-equivalent system in Harlequin's Back is the Engine, the buried techno-magical
mechanical computer beneath Umberley Manor in The Masquerade Place -- documented here for flavor
only, never built as a real host.

| Node | Function | Color/Rating | IC |
|---|---|---|---|
| Terminal access points | Room terminals scattered through the manor; a "magic lantern" VR rig (diving-bell helmet + control glove) substitutes for a cyberdeck | Standard computer access, per Computer Theory (6) | none |
| The Engine (system core) | A cathedral-sized clockwork machine; querying it is run as a mini-astral-quest (Grimoire II, p.95) | Reaching the Citadel yields exactly one fact about the Place's cover story per successful run (never the true events of Darke's plan) | Mechanical blade/saw appendages, 5L damage, Barrier Rating 5 per limb, avoided with an opposed Reaction (4) vs. Rating 6 |
| Nacht's inner chamber | The room at the Engine's heart where Thayla is held; catwalks here are rigged to collapse into the grinding gears (8D damage) | Not a decking target -- a physical trap | Nacht himself, moving through the shadows |
"""

NOT_BUILT = """
- Enemy Crawlers, Enemy Toads, alacorns, fomorians, each-uisges, animate Stone Knight statues,
  spirit hounds, the reanimated "mine monster," generic earth/fire elementals, cowpokes, cowpunks,
  and unnamed "extras" -- all generic Threat Rating opposition with no individual identity.
- Guardians 1-3 of the Impossible Dream's Tower (the land-kraken, the armored Henchman, and the
  card-playing "Cerberus Bug" cockroach) and the roach-man "Beetlebugs" -- one-scene monster set
  pieces, not persistent characters.
- The Bouncer (a spirit guardian barring the Village's "Exit Door") and the Dweller on the
  Threshold (the robed ferryman who tests the runners at the astral quest's outset) -- unnamed,
  function-only gatekeeper spirits.
- "Fate" -- the unspeaking, sparkle-robed woman glimpsed on the dock at the quest's start; never
  interacted with.
- The unnamed "blue-skinned man in a trench coat" and the unnamed bat-winged sprite from the
  Impossible Dream's random "Playful Spirits" table, plus its lying "false Guardian" con-man --
  the table's three named entries (Toady, Morris, Mister Mystery) are recorded above.
- The "Lord Constable" (a masquerade guest who strongly resembles Ehran the Scribe) and "Lady
  Nasir" (explicitly identified as Ariel Nasir, the free air elemental from the original Harlequin
  adventure) -- cameo name-drops of characters from specs/harlequin.py, which has not yet been
  built out; do not create stray rows for them here.
- The unnamed sacrificed children at the Bridge, Part Three, who speak a 2055 Mexican/Aztlan
  dialect of Spanish -- a deliberately unexplained detail, not a resolvable character.
- The unnamed, faceless barge-ferrymen of the Isle of Apples and Castle Maydenlande -- silent,
  function-only guides.
- The "20 Questions" player-handout survey and the general Foreshadows-chapter omens (barking
  animals, portentous dreams, an uncatchable laughing clown) -- pre-adventure GM techniques, not
  in-fiction rows.
"""

PLAY_NOTES = """
- This is a single continuous framing adventure, not eight independent ones: run The Bridge, Parts
  One through Three, as the connective tissue between Aftermath, A Fistful of Karma, By the Sword,
  The Impossible Dream, The Songbird, and The Masquerade, in that order.
- Hard rule carried over from the source text: no astral projection is permitted anywhere in this
  adventure -- it breaks the story by revealing too much too soon.
- Each metaplanar Place transforms gear, cyberware, and magic differently (see each location's
  notes); brief players on the relevant Place's rules before they arrive rather than all at once.
- Player-character death mid-quest has three GM-chosen resolutions in the source text (temporary
  "death" with no Karma for that leg; permanent memory-wipe departure; or true death) -- pick one
  approach before play and apply it consistently, per the book's own Introduction section (not
  reproduced here as a row).
- The climactic choice at The Bridge, Part Three -- volunteering to remain with Thayla forever, or
  leaving her undefended -- is the adventure's real ending and should not be rushed; the book treats
  it as a roleplaying decision, not a dice roll.
- Both the Songbird's survival after restoring Thayla's voice, and the true nature of the
  masquerade's Great Powers guests, are left ambiguous by design; do not resolve them without a
  reason arising from your own table's play.
"""
