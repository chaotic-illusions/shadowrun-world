# Missions (FASA7325, 1996) -- campaign order #29 in frontend/shared.js ADVENTURE_ORDER (the task
# brief specified ORDER=30, but counting the actual array places "Missions" at index 29, one slot
# before "Mob War!" at 30 -- used 29 to match the established one-spec-per-slot convention).
# An anthology of four short, self-contained "Alternate Campaign Concept" adventures, each with its
# own prologue, cast and Matrix hosts: Under the Influence (Lone Star undercover cops), Malpractice
# (DocWagon High Threat Response medics), Mission: Mars (AresSpace corporate security) and King of
# the Mountain (UCAS Special Forces). The four can be run as one-shots for non-runner characters, or
# with an existing shadowrunner team drafted/coerced/hired into the role. Dates are scattered and
# only loosely reconciled across the book (see YEAR below); one clear internal contradiction: in
# Malpractice, Shawn Ferrer finishes paramedic training in March 2053 and is "assigned to Expert Team
# Three nine months later" (~December 2053), but earlier the text says Liz picked Team Three because
# it is "the one HTR team that had been around since 2054" -- both dates are given verbatim in
# ORG/NPC notes below rather than silently reconciled. OCR mangles every attribute-row header in the
# book ("B Q S I W C E R" prints as garbage on nearly every stat block) and Silver's Initiative uses
# square brackets where the rest of the book uses parentheses; these are cosmetic OCR/formatting
# artifacts, not treated as canon inconsistencies. Malpractice explicitly leaves the identity of the
# DocWagon mole and of "Mr. Brown"'s employer up to the gamemaster; this spec follows the book's own
# default write-up (Shawn Ferrer as the mole, Brown's organization deliberately unnamed) and notes
# the alternates. Also unreconciled: Bob tells the runners to meet Liz "outside DocWagon's Clinic in
# Renton," but the very next scene's own descriptive text calls the same building "the Redmond
# DocWagon clinic" -- both names are preserved on the DocWagon Renton Clinic location row rather than
# silently picking one.
# Source text: docs/Adventures/text/Shadowrun 2e - Adventure - Missions {FASA7325}.txt (98 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "Missions"
ORDER = 29
SOURCE = "Shadowrun 2e - Adventure - Missions {FASA7325}.pdf, pp. 4-96"
YEAR = "2057-2058 (Mission: Mars prologue is dated 18 August 2057; Malpractice runs a TRP shift " \
       "shortly after DocWagon's TRP program launched late August 2057; Under the Influence and " \
       "King of the Mountain give no explicit year and are treated as roughly contemporary)"

SYNOPSIS = """
**Under the Influence**: Lone Star detectives (or runners hired when Lone Star's own people come up
short) are sent to find **Sgt. Franco Tanner**, an undercover cop who vanished while investigating
the **Futuremen**, a small but suspiciously disciplined and heavily cybered "street gang." The trail
leads to **MindSound Music**, a Ravenna storefront hiding the illegal chop shop of **Dr. Claudio
"Dr. Cuca" Andrade** -- and beneath it, a **Renraku Computer Systems** black project run by manager
**Marcus Powell**. Cuca's "patients" leave with more than new chrome: a voice-triggered behavior-
control implant and simsense conditioning that turn them into an obedient, memory-wiped strike team
on call. Tanner got the surgery to go undercover and became one of the gang's own puppets without
knowing it. The team must dig through two front businesses and a hidden Matrix host, survive an
ambush of conditioned Futuremen (Tanner included), and race Renraku's cleanup crew to the evidence
before the corporation quietly buries its "two renegade employees" and the whole affair.

**Malpractice**: Ex-DocWagon paramedic and shadow-community hero **"Doctor Bob" Khamdeng** hires the
runners directly (no fixer, to keep the job off the street's radar) to go undercover as fake
**Temporary Response Personnel** embedded with DocWagon **Expert Team Three**. Years earlier Bob
refused an offer from a man called **Brown** to sell DocWagon clients' DNA and medical records, and
Brown's people ambushed and nearly wiped out Bob's team for it. Bob has just learned that a second
paramedic took the deal and is still active on Team Three. Posing as TRPs through a punishing
two-week Expert Duty rotation -- a decker-caught-in-crossfire extraction, an escaped shipment of
sedated cockatrii, a sabotaged tire meant to buy the mole a moment alone with a public telecom -- the
runners must expose the DNA leak (the book's default culprit is dwarf paramedic **Shawn Ferrer**,
though Gordon, Viv or Seth can be swapped in) before **Earl Brown** realizes his cover contact has
been blown and stages a final ambush using a kidnapped child as bait.

**Mission: Mars**: A team of AresSpace Special Operations security agents is assigned by handler
**Benjamin Steele** to explain three Mars photographs that surfaced in Dunkelzahn's will -- two from
a genuine, suppressed 2001 NASA probe, and one faked "UFO" image from AresSpace's own failed 2042
**Project Cydonia**. Chasing the connection uncovers **Operation Discovery**, a disastrous secret
1970s-derived 2011 manned NASA mission to Mars run by the black-ops agency **Veil**, and Veil's
decades of quiet murder and sabotage to keep it buried -- including framing a UFO-watch group for
the Cydonia sabotage that Veil mole **Karl Xavier** actually committed. Witnesses die around the
team (a Veil sniper puts a bullet through **Dr. Robert Zeus**'s head mid-interview), "Men in Black"
warn them off, and a storage silo under a Kansas farm holds both the wrecked Discovery capsule and a
Veil cleanup crew willing to kill to keep it that way. In the end AresSpace itself chooses to bury
the truth rather than risk its government contracts.

**King of the Mountain**: A UCAS Special Forces team (**Operation Backhand**, commanded by Major
**Jeff "Heartbreaker" Lisbon**) parachutes into the Trans-Polar Aleut to investigate a fortified,
half-built Cold War shelter called **Fort Ross**, hidden inside Mountain 9347. There, disgraced ex-
Colonel **Lawrence Fenmore** and an institutionalized schizophrenic mage who believes himself the
**Archangel Michael** have spent five years running the **City of God** -- part boarding school, part
kidnapping ring, part fanatical private army, training 152 abducted magically active girls (all
secretly sterilized "to stop the cancer") for a future strike on Tir Tairngire or Aztlan. After an
arctic storm strands the team without half its gear and days of sensory-deprived isolation start
eroding their sanity, Heartbreaker dies in the first exchange of gunfire at the perimeter, and the
survivors must fight through hallucinatory "angel" encounters, Michael's elite teenage "Alphas," and
finally Michael and Fenmore themselves to decide whether Fort Ross's child army lives, dies, or simply
changes owners.
"""

TIMELINE = """
- **2001** -- a NASA Mars probe secretly photographs pyramid-like structures and an unidentified
  skeleton on the Martian surface; the Department of Defense buries the data under the black-ops
  agency **Veil**.
- **2011 (Aug-Dec)** -- Veil's manned follow-up, **Operation Discovery**, reaches Mars; on
  **December 24, 2011** the main return module crashes, killing five of eight astronauts. The three
  survivors (including **Lt. Col. James Yavin**) return with samples; everything is sealed in a
  missile silo under **Hoffman Farm**, Haggard, Kansas.
- **2016** -- NASA, bankrupted in part by Operation Discovery's cost, is bought out by Ares
  Macrotechnology and folded into **AresSpace**; Veil mole **Karl Xavier** transfers over with it.
- **2021** -- Goblinization; Colonel **Lawrence Fenmore**'s formative trauma running metahuman
  restraint duty begins his slide toward magical supremacism.
- **2029** -- the Computer Crash erases the last public records of Fort Ross.
- **Early 2040s** -- AresSpace launches the unmanned **Project Cydonia** probes; Xavier and fellow
  Veil agents sabotage the transmitted data (doctored into a fake 1950s-style "UFO" photo, chip dated
  8 December 2042) and frame a local MUFON chapter, several of whom AresSpace-hired runners kill
  hunting evidence that was never really there.
- **2043** -- Robert Khamdeng hired as a DocWagon paramedic in Seattle.
- **2047** -- "Doctor Bob" Khamdeng becomes a minor media celebrity for rescuing non-clients.
- **2049** -- a Sons of Sauron bombing (in retaliation for a Humanis Policlub strike into the Ork
  Underground) kills 38 people and fatally injures Seth Palatine's mother; around the same time
  Robert Khamdeng is seen at a couple of Humanis Policlub recruitment meetings.
- **2050** -- Fenmore's marriage ends and he is passed over for promotion; he begins recruiting
  discontented officers and the institutionalized mage who calls himself **Archangel Michael**.
- **2051** -- Fenmore rediscovers surviving hard-copy plans for Fort Ross and fakes a medical
  retirement to found the **City of God**.
- **2052 (late)** -- during the Ancients gang war, Vivianne Geldhausmann's husband Jacob is murdered
  after his footage clears the Ancients of blame; Gordon Kurtz is hired by DocWagon around the same
  time.
- **September 2054** -- Brown offers Robert Khamdeng cash for DNA samples; Khamdeng refuses. Three
  days later Brown's mercenaries ambush Khamdeng's HTR team; he is the sole survivor and fakes his
  own death.
- **March 2053 / "nine months later"** -- Shawn Ferrer completes DocWagon paramedic training and is
  assigned to Expert Team Three (the book elsewhere states Team Three has existed "since 2054" --
  both dates are given verbatim; not reconciled here).
- **August 2057** -- Dunkelzahn's Last Will and Testament is released, publishing the three Mars
  photos; DocWagon's Temporary Response Personnel program launches in the same month. Mission: Mars
  opens on **18 August 2057**.
- **2057-2058** -- Malpractice (Expert Team Three's Expert Duty shift) and Under the Influence take
  place in this window; King of the Mountain's Operation Backhand is briefed on "3 December" of an
  unspecified year and runs through the following weeks of perpetual arctic night.
"""

ORGS = [
    {
        "name": "The Futuremen",
        "org_type": "gang",
        "tier": 1,
        "headquarters": "Underground research facility beneath MindSound Music, Ravenna, Seattle",
        "summary": "Seattle 'street gang' of the future -- actually a Renraku black project turning volunteer chop-shop patients into a memory-wiped, voice-controlled cybersoldier squad",
        "description": (
            "About twenty heavily cybered members who hit corporate targets (mostly Renraku's Big "
            "Eight rivals) with military precision and vanish without a trace, coordinated in real "
            "time by Renraku staffers via subdermal headware radios and a pair of overhead recon "
            "drones. None of them know they are Futuremen: Dr. Cuca's cyberclinic implants a "
            "behavior-control radio device during routine (if illegal) surgery, then uses custom "
            "simsense recovery-room players to condition each patient to obey Amazonian Portuguese "
            "voice commands and forget everything afterward. The gang's 'operations' are field tests "
            "for the project; the corporate damage to Renraku's rivals is a welcome side effect."
        ),
        "notes": (
            "Created and run by Renraku Computer Systems (Marcus Powell, project manager; Dr. Cuca, "
            "chief scientist) as a proof-of-concept for large-scale behavioral conditioning. Members "
            "have only a limited 'command set' (move, attack, wait, retreat) and cannot improvise; "
            "cutting their controllers' surveillance (jamming, illusion, moving out of drone sight) "
            "cripples them, and anyone who knows the trigger Portuguese phrases can countermand their "
            "orders. Sgt. Franco Tanner became an unwitting member after an undercover softlink "
            "upgrade at Cuca's clinic. If exposed, Renraku evacuates and demolishes the facility "
            "(9D-damage charges) within about an hour and denies all corporate knowledge, branding "
            "Cuca and Powell 'two renegade employees.' The project can resurface in another city if "
            "not fully dismantled."
        ),
        "allies": ["Renraku Computer Systems"],
        "enemies": ["Lone Star Security"],
    },
    {
        "name": "Veil",
        "org_type": "government agency",
        "tier": 5,
        "headquarters": "Classified facility, Washington DC (UCAS Department of Defense)",
        "summary": "Off-the-books black-ops agency inside the old US, then UCAS, Department of Defense; on paper it does not exist",
        "description": (
            "Formed to run and then bury the secret manned Mars mission Operation Discovery (2011), "
            "Veil has spent nearly five decades eliminating anyone or anything that threatens to "
            "expose it -- witnesses, evidence, corporate probes that stray too close, even its own "
            "former agents when convenient. It keeps a permanent mole inside AresSpace's predecessor "
            "NASA and, later, inside AresSpace itself (Karl Xavier), and maintains standing 'cleanup "
            "crews' and softer 'Men in Black' intimidation teams to respond the moment its secret is "
            "threatened, as it was by the Mars photographs in Dunkelzahn's will."
        ),
        "notes": (
            "Cleanup crew led by John Silver (former mercenary) and combat mage Jason 'Eldritch' "
            "Mason, backed by UCAS soldiers; a separate twelve-man 'Men in Black' detail handles "
            "intimidation, confiscation and detention rather than killing. Veil placed surveillance "
            "bugs on both surviving Operation Discovery witnesses (Yavin, Zeus) the moment the photos "
            "went public. Runs the UCAS/Veil Matrix host in DC (see MATRIX_HOSTS)."
        ),
        "enemies": ["AresSpace"],
    },
    {
        "name": "AresSpace",
        "org_type": "corporation",
        "tier": 4,
        "headquarters": "AresSpace Headquarters, Houston, Texas",
        "summary": "Ares Macrotechnology's aerospace division, built on the 2016 NASA buyout; runs its own Special Operations security teams and keeps its own decades-old secret",
        "description": (
            "Formed when Ares Macrotechnology bought out a NASA nearly bankrupted by the secret "
            "Operation Discovery program in 2016. AresSpace's Special Operations Division security "
            "agents are the corporate-shadowrunner equivalent -- deckers, mages and combat specialists "
            "who dress in business suits and rarely carry obvious cyberware. The 2042 failure of its "
            "own Project Cydonia probe mission (sabotaged, though AresSpace never learned by whom) "
            "cost several careers, including Benjamin Steele's, and left a grudge that outlives the "
            "corporation's official amnesia about the whole affair."
        ),
        "notes": (
            "Fields corporate-security-guard NPCs and the Special Ops team assigned to investigate "
            "the Dunkelzahn's-will Mars photos in Mission: Mars. When that team reports the truth "
            "about Operation Discovery and the Cydonia sabotage, AresSpace's leadership (implicitly "
            "Damien Knight) chooses to bury the story rather than risk its UCAS government contacts, "
            "forfeiting Dunkelzahn's 1%-Ares-stock bequest in the process; Steele quietly arranges the "
            "'accidental' deaths of both Yavin and Xavier afterward."
        ),
        "allies": ["Ares Macrotechnology"],
        "enemies": ["Astrotech Industries", "Veil"],
    },
    {
        "name": "Astrotech Industries",
        "org_type": "corporation",
        "tier": 2,
        "headquarters": "Astrotech Industries Headquarters, Houston, Texas",
        "summary": "Small but fast-growing Houston aerospace firm founded by ex-AresSpace/Veil mole Karl Xavier, increasingly poaching AresSpace's UCAS government contracts",
        "description": (
            "Founded by Karl Xavier not long after he helped sabotage AresSpace's Project Cydonia "
            "data and left both AresSpace and Veil. Xavier parlayed his UCAS Department of Defense "
            "connections and his private copy of the real, unsabotaged Cydonia footage into a steady "
            "pipeline of government satellite-construction and launch contracts, hinting to officials "
            "that he will go public with the data (and its Operation Discovery implications) if they "
            "stop steering business his way."
        ),
        "notes": (
            "Host C of its Matrix system (see MATRIX_HOSTS) holds a 30 Mp summary of Operation "
            "Discovery, including the Hoffman Farm silo's location, and a 200 Mp file of the original "
            "unsabotaged Cydonia footage. Xavier will discuss Operation Discovery candidly with "
            "AresSpace investigators who approach him civilly, but stonewalls about his own role in "
            "the Cydonia sabotage unless pressed (2+ net successes on an opposed Charisma/"
            "Interrogation/Negotiation vs. his Willpower gets a confession and the silo's location; "
            "4+ gets his own data copy). Xavier dies in a 'mysterious car crash' shortly after the "
            "adventure -- Steele's quiet revenge."
        ),
        "enemies": ["AresSpace"],
    },
    {
        "name": "MUFON (Houston Chapter)",
        "org_type": "UFO watch group",
        "tier": 1,
        "headquarters": "Houston, Texas",
        "summary": "Small local Mutual UFO Network chapter framed by Karl Xavier for sabotaging AresSpace's Project Cydonia probe data -- an accusation that got several of its members killed for a crime it never committed",
        "description": (
            "A local branch of the Mutual UFO Network that requested, and was denied, access to "
            "AresSpace's Project Cydonia findings. When the probe's data turned out to be sabotaged "
            "static and a faked photograph, AresSpace Security's investigation found evidence "
            "(planted by Veil mole Karl Xavier and his fellow deckers to cover their own tracks) "
            "pointing at the chapter as the culprits who had intercepted and swapped the data."
        ),
        "notes": (
            "AresSpace hired a team of shadowrunners to retrieve the 'stolen' original data from the "
            "chapter; the runners succeeded only in killing several of its members. The data was "
            "never recovered because MUFON never had it. No member names or chapter roster are given "
            "in the source text."
        ),
        "enemies": ["AresSpace"],
    },
    {
        "name": "City of God",
        "org_type": "cult",
        "tier": 2,
        "headquarters": "Fort Ross, Mountain 9347, Trans-Polar Aleut",
        "summary": "Colonel Lawrence Fenmore's kidnapping ring, boarding school and fanatical private magical army, hidden inside a half-finished Cold War bio/nuclear shelter",
        "description": (
            "A five-year-old operation built around a self-proclaimed 'Archangel Michael' (in "
            "reality a schizophrenic hermetic mage, Michael Thorndike) and 35 adult staff, all "
            "recruited or coerced by ex-UCAS Colonel Lawrence Fenmore. The 'school' kidnaps magically "
            "active girls from magophobic families worldwide, sterilizes them, and trains them under "
            "Christian-apocalyptic religious framing into ranked magical soldiers (Alpha through "
            "Epsilon) intended for a future strike on Tir Tairngire or Aztlan. Funded through a "
            "decker known only as 'Mr. Mo,' who laundered money through the Volgograd Seven, corrupt "
            "Japanese military officers, Detroit organized crime and unwitting banks and investors."
        ),
        "leadership": [
            {"name": "Colonel Lawrence Fenmore", "title": "Founder / commander", "notes": "Ex-UCAS Army; the calculating, sane half of the leadership."},
            {"name": "Michael Thorndike ('Archangel Michael')", "title": "Spiritual leader / chief instructor", "notes": "Schizophrenic Grade 3 initiate hermetic mage; believes he is literally the Archangel Michael."},
        ],
        "notes": (
            "33 adult soldier/staff (10 magically active guard-instructors, 2 riggers, 1 decker, 11 "
            "maintenance/teaching staff, 5 with high-grade cyberware, 4 Fenmore loyalists, 3 doctors) "
            "plus 152 magically active girls aged 11-20 of every specialty and metatype, none given "
            "SINs or legal existence. Michael's six most trusted teenage students -- the 'Alphas' -- "
            "form his personal guard (see NPCS). If both Fenmore and Michael are killed or captured, "
            "the UCAS military quietly absorbs the surviving girls as a black operation rather than "
            "disband the program; a surviving Fenmore becomes a lasting Enemy (4-point: Power 3, "
            "Motivation 5, Knowledge 3) who will hunt anyone who saw his face."
        ),
        "enemies": ["Tir Tairngire", "Aztlan"],
    },
]

LOCATIONS = [
    {
        "name": "Solomon Arms",
        "location_type": "hotel",
        "city": "Seattle",
        "district": "Ravenna",
        "security_level": "Low Security",
        "summary": "Shabby-but-not-squalid four-story hotel where Sgt. Tanner holes up under his 'Leopard' Leonard undercover identity",
        "description": (
            "A four-story hotel that sounds better than it looks, with a desk clerk conscientious "
            "enough to notice visitors and greedy enough to take a bribe. Tanner's third-floor suite "
            "is a genuine day-to-day mess -- dirty socks, Nuke-It Burger wrappers -- with no sign of "
            "struggle."
        ),
        "notes": (
            "The telecom's datastore holds a Scramble-6-encrypted file (Computer 5 to bypass the "
            "terminal, Computer 10 to decrypt) containing Tanner's full notes on Dr. Cuca's clinic, "
            "including its LTG number and a partial suspect list. Tanner himself returns here, "
            "visibly 'glitching' under Cuca's remote commands, partway through the investigation."
        ),
    },
    {
        "name": "MindSound Music",
        "location_type": "shop",
        "city": "Seattle",
        "district": "Ravenna",
        "security_level": "Corporate High Security",
        "controlling_org": "Renraku Computer Systems",
        "summary": "Unremarkable music store fronting Dr. Cuca's illegal cyberclinic and, beneath it, Renraku's entire Futuremen research complex",
        "description": (
            "A one-story storefront (reinforced glass, roll-down night shutters, an elf clerk named "
            "Lindy) flanked by two more Renraku fronts -- Kennedy's Cheap Electronics and the Cafe do "
            "Amazonia -- each hiding its own entrance to the same underground facility. Below "
            "MindSound's back room is Cuca's cyberclinic (surgery, recovery room wired with custom "
            "conditioning simsense players, one-way-mirrored observation rooms, Cuca's office); "
            "beyond that, Marcus Powell's office, a guard ready-room with an on-duty security mage, "
            "storage-room alternate entrances under the two other fronts, a guard room, and the "
            "Command Center -- three dozen workstations, each with a radio and signal tracer bonded "
            "to one Futureman, issuing commands in Amazonian Portuguese."
        ),
        "notes": (
            "A dozen guards plus one security mage (Force 3 watcher spirits in each front building) "
            "patrol at all times; every entrance has a hidden cyberware scanner. Renraku evacuates and "
            "demolishes the entire complex (staged timeline, ~1 hour once triggered: lock down, load "
            "trucks, transmit and wipe Host C's data, plant and detonate explosive charges for 9D "
            "damage to anyone still inside) the moment it believes the operation is blown. See "
            "MATRIX_HOSTS for the three linked Matrix hosts."
        ),
    },
    {
        "name": "Cafe do Amazonia",
        "location_type": "restaurant",
        "city": "Seattle",
        "district": "Ravenna",
        "security_level": "Corporate High Security",
        "controlling_org": "Renraku Computer Systems",
        "summary": "No-frills Renraku-front cafe next door to MindSound Music, hiding a storage-room entrance down into the Futuremen complex",
        "description": (
            "A plain neighborhood cafe of 'authentic Amazonian' cooking, separated from MindSound "
            "Music by a narrow alley; its cook and waiter are both Renraku agents rather than "
            "genuine restaurant staff. A careful decker sifting the front's own bookkeeping system "
            "might reasonably wonder why a no-frills cafe in Seattle needs four dozen Amazonian "
            "Portuguese linguasofts."
        ),
        "notes": (
            "Its basement storage room -- stocked with ordinary-looking foodstuffs to fool a casual "
            "look -- hides one of the complex's alternate entrances, guarded by a passkey-locked door "
            "and a hidden cyberware scanner. See MindSound Music and MATRIX_HOSTS (Host B) for the "
            "shared underground facility and its Matrix system."
        ),
    },
    {
        "name": "Kennedy's Cheap Electronics",
        "location_type": "shop",
        "city": "Seattle",
        "district": "Ravenna",
        "security_level": "Corporate High Security",
        "controlling_org": "Renraku Computer Systems",
        "summary": "Renraku-front electronics outlet next door to MindSound Music, hiding another storage-room entrance down into the Futuremen complex",
        "description": (
            "A discount electronics storefront on MindSound Music's other side, staffed by two "
            "Renraku agents posing as salesmen. Its own bookkeeping system quietly keeps ordering "
            "more cyber-radio implants than the store has ever recorded selling -- one of several "
            "loose threads that give the Futuremen complex away to a thorough decker."
        ),
        "notes": (
            "Its basement storage room hides another alternate entrance into the underground "
            "complex, guarded the same way as the Cafe do Amazonia's. See MindSound Music and "
            "MATRIX_HOSTS (Host B) for the shared underground facility and its Matrix system."
        ),
    },
    {
        "name": "You Should Not Eat So Much!",
        "location_type": "restaurant",
        "city": "Seattle",
        "district": "Pier 60 area",
        "security_level": "Patrolled / Commercial",
        "summary": "Family fast-food restaurant near Pier 60 where 'Doctor Bob' Khamdeng deliberately hires runners in plain sight",
        "description": (
            "A busy, wholesome family restaurant -- sararimen, children, security guards eyeing the "
            "clientele -- chosen by Bob precisely because it is the last place anyone would expect a "
            "shadow meet. Runners in typical street gear draw stares from the other diners but no real "
            "trouble unless they start it themselves."
        ),
        "notes": "Meet site for Malpractice's job offer; also where Bob pays out (or explains his failure to pay) at the end of the run.",
    },
    {
        "name": "DocWagon Renton Clinic",
        "location_type": "hospital",
        "city": "Renton",
        "controlling_org": "DocWagon",
        "security_level": "Patrolled / Commercial",
        "summary": "The clinic where Liz Yamato first picks up the runners in Citymaster #264-10 and drives them to a warehouse for crash TRP training",
        "description": (
            "Bob tells the runners to meet Liz 'outside DocWagon's Clinic in Renton'; when they "
            "arrive she is leaning against her marked Citymaster's door. The book's own scene-setting "
            "text for the meeting moments later calls it 'the Redmond DocWagon clinic' instead -- "
            "'too white, too clean and smelling of the sick, injured and dead' -- an unreconciled "
            "Renton/Redmond naming inconsistency preserved here rather than silently fixed."
        ),
        "notes": "Liz then drives the team to an abandoned warehouse west of the Federated Boeing Shipyards for a compressed 48-hour TRP training course before dropping them at the 83rd Street Clinic to begin their cover posting.",
    },
    {
        "name": "DocWagon 83rd Street Clinic",
        "location_type": "hospital",
        "city": "Seattle",
        "controlling_org": "DocWagon",
        "security_level": "Patrolled / Commercial",
        "summary": "Expert Team Three's home clinic: apartments, garage, dispatch and a helipad, for the two weeks the fake TRPs are embedded there",
        "description": (
            "A working DocWagon facility with three color-coded medical wards, an employees-only "
            "vehicle garage (five ambulances, three Citymasters, a rotorcraft in for repair), Expert "
            "Team Three's shared apartment (lounge, kitchenette, bedrooms), and a rooftop helipad. "
            "Klaxons and dispatch announcements send teams scrambling within seconds of a call."
        ),
        "notes": (
            "Where the TRPs (the runners) bunk, draw gear (gel/stun rounds plus one round of real "
            "ammo per weapon, signed for and returned after every run), and where Liz Yamato "
            "eventually arrives with Internal Security muscle to take the exposed mole into custody."
        ),
    },
    {
        "name": "Spring Lakes Apartments (construction site)",
        "location_type": "landmark",
        "city": "Renton",
        "district": "Spring Lakes",
        "security_level": "Low Security",
        "summary": "Unfinished apartment complex where Earl Brown stages his final ambush of Expert Team Three, using a kidnapped Platinum client's son as bait",
        "description": (
            "Skeletal building frames behind a twelve-foot open gate, a dirt bridge over a drainage "
            "ditch, stacked I-beams and wide sections of pipe scattered across bare ground -- ideal "
            "cover for an ambush and a fake medical emergency call."
        ),
        "notes": (
            "Brown drops kidnapped 13-year-old Salthili Truan from the fourth floor as bait, then "
            "hits the responding Citymaster with two tactical-computer-guided LAWS rockets (aimed to "
            "flip the vehicle into the ditch, not destroy it) and five camo-jacketed mercenaries "
            "hidden in the pipes and behind girder stacks. Brown personally departs before the fight "
            "starts. The child dies unless reached within 7 combat turns."
        ),
    },
    {
        "name": "AresSpace Headquarters",
        "location_type": "corporate headquarters",
        "city": "Houston",
        "controlling_org": "AresSpace",
        "security_level": "Corporate Standard",
        "summary": "AresSpace's Houston HQ, former NASA territory, where handler Benjamin Steele runs the Mars-photo investigation out of a briefing room",
        "description": "A modern corporate campus built partly on NASA's old Houston footprint. Recessed lighting bathes the corridor walls in soft light on the way to the soundproof Briefing Room, where Benjamin Steele waits at the far end of the table with a small image projector; the characters' Special Operations team reports here for briefings, gear and debriefs throughout Mission: Mars.",
        "notes": "PCs are issued a 100,000-nuyen operating budget, Project Cydonia data passcodes and transportation on request; leftover budget becomes their bonus.",
    },
    {
        "name": "Astrotech Industries Headquarters",
        "location_type": "corporate headquarters",
        "city": "Houston",
        "controlling_org": "Astrotech Industries",
        "security_level": "Corporate Standard",
        "summary": "Karl Xavier's aerospace company, a rising rival to AresSpace built on stolen Cydonia data and government leverage",
        "description": (
            "A modern high-rise with a metal-detector lobby search, a 23rd-floor conference room for "
            "meetings with Xavier, and armed corporate security (Ares Predators, armored business "
            "suits) that will not start a fight but responds hard if the characters do."
        ),
        "notes": "Host C of Astrotech's Matrix system holds Xavier's private Operation Discovery and Cydonia files; see MATRIX_HOSTS.",
    },
    {
        "name": "Ellington Air Force Base",
        "location_type": "military installation",
        "city": "Houston",
        "summary": "CAS Air Force base near Houston where retired Lt. Col. James Yavin, Operation Discovery's sole surviving astronaut, lives out his retirement",
        "description": "A functioning CAS Air Force base; Yavin's on-base home is packed with Air Force and NASA memorabilia, including photos of him with a NASA space shuttle and a Saturn-V-class rocket.",
        "notes": (
            "Guards wave visitors through if they call ahead or state honest (if vague) business; "
            "Veil has bugged Yavin's home with four listening devices since the Mars photos went "
            "public (Target Number 7 per device to find with a bug scanner). Characters who give false "
            "names to the gate guards get detained by CAS Military Police on the way out."
        ),
    },
    {
        "name": "Brook Park",
        "location_type": "landmark",
        "city": "Houston",
        "summary": "Public Houston park where Dr. Robert Zeus insists on meeting the player characters, believing a crowd will protect him -- and where a Veil sniper kills him instead",
        "description": (
            "Zeus's terse, nervous voice-only telecom message sets the meet: 'Brook Park. 2 p.m., "
            "near the entrance gate.' He leads the characters from the gate toward a small grove of "
            "trees to talk, choosing the open, public setting on the theory that no one would risk an "
            "attack in front of civilians."
        ),
        "notes": "A Veil cleanup-crew sniper, tipped off by bugs on Zeus's telecom, has been watching the meet from 300 yards out the entire time; see Dr. Robert Zeus (NPCS) for how the encounter plays out.",
    },
    {
        "name": "Hoffman Farm (storage silo)",
        "location_type": "underground bunker",
        "city": "Kansas",
        "district": "Haggard, near Wichita (Route 23, one mile south of Route 56)",
        "summary": "Abandoned missile silo beneath a derelict farm, secretly repurposed to store every piece of physical evidence from Operation Discovery",
        "description": (
            "A ramshackle farmhouse and outbuildings the US government bought from the Hoffman "
            "family in the late 1970s; a storm-cellar entrance behind one of the barns leads down "
            "through a Rating 5 then Rating 7 maglocked door (both Force 6 warded against astral "
            "entry) into a nuclear missile silo, dismantled and converted into secret storage. Rooms: "
            "a security console room, an isolated (non-Matrix) archive computer and filing cabinets, "
            "a main storage area with sealed sample bins and a Plexiglas-walled chamber holding the "
            "actual Operation Discovery return capsule, a stripped laboratory, and a hallway leading "
            "to the old launch bay and a ventilation-shaft surface exit two kilometers away."
        ),
        "notes": (
            "Storage bins hold the three astronauts' EVA suits, Mars stone and bone samples (including "
            "a meter-and-a-half femur-like bone), and a media bin of CD-ROMs/data-tapes/optical chips "
            "labeled 'NASA Security/Sentry Probe: Original Data,' 'Operation Discovery: Original "
            "Footage,' and 'Project Cydonia: Original Data' (200 minutes of raw Mars footage showing "
            "the wrecked Discovery ship). Veil's cleanup crew (John Silver, Jason 'Eldritch' Mason and "
            "one soldier per player character) arrives 5+2D6 minutes after intruders enter, in 2x2 "
            "cover formation, and will plant 1 kg of C4 per crew member (10 minutes to place, "
            "detonating 5 minutes after withdrawal) to erase the site and anyone still inside."
        ),
    },
    {
        "name": "Fort Ross",
        "location_type": "underground bunker",
        "city": "Trans-Polar Aleut",
        "district": "Mountain 9347, Alaska Range (Kuskokwim River valley)",
        "security_level": "Zero Zone -- Lethal Response",
        "controlling_org": "City of God",
        "summary": "Half-finished Cold War nuclear/biowarfare shelter, rediscovered and finished by Colonel Fenmore as the hidden home of the City of God",
        "description": (
            "A blast door and landing pad concealed under rock overhangs and snowdrifts (Barrier 32 "
            "door, Rating 8 maglock, motion/IR sensors defeated by the region's frequent sleet storms, "
            "railgun-burst anti-air defenses), plus a disused underwater entrance through a river "
            "tributary (a lone Sentry gun behind a propeller-guarded flooded tunnel). Inside: miles of "
            "abandoned or ruined service tunnels; a rigger station and a voiceprint-locked Security "
            "Central controlling every alarm and the exterior railguns; active hallways behind a "
            "Barrier-24 raisable wall leading to a staff office (evidence of the funding-launderer "
            "'Mr. Mo' and a wall chart ranking the girls Alpha through Epsilon), enchanting workshops, "
            "religious-icon classrooms (Background Count 2 from constant magic use), bathrooms, a "
            "gymnasium, an all-white lounge, a computer room with a Rating 8 online hermetic library, "
            "a cafeteria/kitchen/walk-in fridge, staff quarters, a laundry, Michael's disguised "
            "'Heaven' bedroom, a 200-seat chapel, and a voiceprint-locked generator/boiler room."
        ),
        "notes": (
            "The main door's rigger lets intruders past the outer defenses before firing two tripod-"
            "mounted Sentry guns (Barrier 12, LMG/APDS) that reliably kill the mission commander, "
            "Heartbreaker, in the opening seconds. Astral entry is blocked at multiple points by "
            "biological-material-reinforced walls and doors. Discovered documents (Heartbreaker's own "
            "dossier) reveal the UCAS government has watched Fenmore for years but deliberately "
            "declassified enough information to let him act, wanting to see what he would build before "
            "moving against him."
        ),
    },
]

NPCS = [
    {
        "name": "Sgt. Franco Tanner",
        "role": "Lone Star undercover officer (alias 'Leopard' Leonard) whose Futuremen investigation turned him into an unwitting Futureman",
        "archetype": "Investigator",
        "title": "Undercover Sergeant, Lone Star Division of Investigation",
        "race": "Human",
        "gender": "Male",
        "organization": "Lone Star Security",
        "connection": 3,
        "description": "Well-tanned skin, curly black hair, a pointy little beard. Burns' file photo makes him look like just another face, but he is an eight-year veteran with a moderate stack of citations and no black marks. Fresh out of Cuca's clinic, he checks over his returned Browning and gear before he even sits up -- old habits -- and tells the nurse, 'No, I think this'll do it, thanks,' with no idea he was gone long enough for anyone to worry.",
        "background": "Spent the last four years doing extended, deep-cover undercover work and developed a real knack for it. Assigned to trace the Futuremen, he worked a web of street contacts as his alter ego 'Leopard' Leonard for weeks with nothing to show, until several dead gangers' contacts pointed him to Dr. Cuca's illegal clinic. He went in for an off-the-record softlink upgrade hoping to overhear something useful, and came out conditioned to obey Cuca's voice commands with no memory of any of it.",
        "notes": (
            "B4 Q5 S4 C4 I5 W4, Ess3.03, React5(6); Threat/Prof 4/3 (2/4 when under Cuca's control); "
            "Boosted Reflexes2, headware radio w/subdermal speakers, Smartlink, Softlink4 (all alpha "
            "grade), Skillwires Plus3; Browning Ultra-Power, Securetech Ultra-Vest 4/3. Suffers "
            "'brain glitches' -- sudden topic changes, contradictory suggestions -- whenever Cuca's "
            "staff issue him remote commands; leads the party into a Futuremen ambush if not caught "
            "in time. Cuca's coroner-visible implants are proof of the conspiracy if Tanner dies."
        ),
    },
    {
        "name": "Captain Burns",
        "role": "Lone Star captain who assigns the player characters to find missing Sgt. Tanner",
        "archetype": "Police Captain",
        "title": "Captain, Lone Star Division of Investigation",
        "race": "Human",
        "gender": "Male",
        "organization": "Lone Star Security",
        "connection": 1,
        "description": "Always looks unhappy, but looks even more unhappy than usual the morning he calls the team in; motions everyone to sit even though his cramped office has only two chairs, one of which he is sitting in. 'Let me just point out that the company takes this gang situation seriously -- very seriously,' he warns them. 'The media are chewing Chief Herthel a new one over this... so do whatever you have to -- but find him and keep his cover secure if it's not already blown.'",
        "notes": "Briefs the team, loads Futuremen case files onto their terminals, and orders them to keep Tanner's cover intact unless his life is in danger. No stat block given.",
    },
    {
        "name": "Dr. Claudio 'Dr. Cuca' Andrade",
        "role": "Amazonian expatriate scientist running Renraku's Futuremen conditioning project out of a fake street clinic",
        "archetype": "Mad Scientist",
        "title": "Street doc / lead researcher, Futuremen project",
        "race": "Human",
        "gender": "Male",
        "nationality": "Amazonian",
        "organization": "Renraku Computer Systems",
        "connection": 4,
        "description": "A small, brilliant Amazonian man with a wide, gleaming smile and an oddly old-fashioned mechanical wristwatch he checks constantly. Occasionally manic but not clinically insane; his mind is narrowly focused and he tends to overestimate his research's significance while badly underestimating its real-world consequences. Reports to his corporate handler with clipped professional pride -- 'Bem, Mr. Powell. The new medications are keeping the dissociative stress well under control' -- and plays a convincing, slightly eccentric street doc when patients are watching.",
        "background": "Fled Amazonia after a research subject turned out to be the mayor of Sao Paulo's cousin; Renraku recruited him to continue the work in the UCAS. The Futuremen operation is his research's first field test.",
        "notes": (
            "B3 Q4 S2 C3 I6 W5, Ess6, React5; Threat/Prof 1/2, no cyberware by choice; "
            "Biology4[Medicine6], Biotech4[Transimplant Surgery6], Computer3, Etiquette(Corporate)3, "
            "Interrogation4, Psychology7, Unarmed3; wrist computer, 800 Mp memory. Panics and orders "
            "a Futuremen ambush the moment he suspects a visitor is Lone Star; evacuates and destroys "
            "the complex if exposed."
        ),
    },
    {
        "name": "Marcus Powell",
        "role": "Ambitious Renraku manager running the Futuremen project's day-to-day operations and evidence control",
        "archetype": "Corporate Manager",
        "title": "Project manager, Futuremen program",
        "race": "Human",
        "gender": "Male",
        "organization": "Renraku Computer Systems",
        "connection": 3,
        "description": "Keeps Cuca and the project staff under tight control while chasing more funding and personal glory, though he spends much of his time in off-site meetings rather than at the facility itself. Not well liked by the project personnel, and does not much care. Cold and results-driven with subordinates: watching Tanner twitch through conditioning on a monitor, he asks only 'How are we doing, Doctor?' and, satisfied, tells Cuca to 'make those modifications part of the standard procedure' before turning to watch Tanner lace up his boots with a quiet 'Beautiful. Just beautiful.'",
        "notes": (
            "B3 Q3 S3 C5(7) I5 W4, Ess5.5, React6; Threat/Prof 2/2; Computer4, Etiquette(Corporate)5(7), "
            "Firearms3, Leadership3(5), Negotiation4(6); Tailored Pheromones2; Datajack4 w/75Mp; "
            "Morrissey Elite pistol, Vashon Island 'Houndstooth' Armored Suit 3/3. On discovery, his "
            "priorities in order are: erase Renraku's fingerprints, preserve the research data, save "
            "the equipment and staff."
        ),
    },
    {
        "name": "Lindy",
        "role": "Renraku operative posing as MindSound Music's clerk, screening potential Futuremen 'patients' and watching for trouble",
        "archetype": "Screener / Guard",
        "title": "Front-desk operative, MindSound Music",
        "race": "Elf",
        "gender": "Male",
        "organization": "Renraku Computer Systems",
        "connection": 1,
        "description": "Frizzy-haired, wiry, maybe thirty, half a dozen rings in each ear and color-cycling tattoos running down both arms. Perched on a stool behind the counter making adjustments to an antique guitar, stubbing out a nicotine stick and eyeing new arrivals speculatively before offering a flat 'Help you find anything?' Bright and not easily fooled -- his job is screening potential 'patients' and keeping an eye out for trouble, and he is good at both.",
        "notes": (
            "B6 Q6 S6 I4 W5 C4, Ess2.15, React5(10), Armor4/3; Firearms6, Unarmed6; Retractable Spur, "
            "Skillwires Plus3, Softlink3, Wired Reflexes2; Enhanced Articulation, Orthoskin3, Trauma "
            "Damper; FFBA-2, Ares Viper Slivergun, Music/Biotech/Amazonian Portuguese skillsofts. "
            "Reacts differently depending on whether the party arrives with Tanner and whether Cuca's "
            "staff already suspect they are cops; can trigger a Command Center alert if pressed."
        ),
    },
    {
        "name": "Robert 'Doctor Bob' Khamdeng",
        "role": "Ex-DocWagon paramedic turned shadowrunner, hiring the party directly to root out Brown's mole inside DocWagon",
        "archetype": "Fixer",
        "title": "Freelance operator (formerly DocWagon paramedic)",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": "A minor former media celebrity ('Doctor Bob'), a diehard Supersonics fan who will rattle off team stats given the slightest encouragement and talks up the band Murphy's L.A.W. between bites of pie. Deliberately avoids fixers and hires runners face to face over lunch at a family restaurant, believing the best place to hide something is in the open. Refuses to haggle: 'my name is Khamdeng, not Johnson. I'm as poor as you are; I don't have corp funding to back me up.'",
        "background": "Hired by DocWagon in 2043, famous for rescuing non-clients despite the fines; refused Brown's DNA-sample offer in September 2054, and three days later his HTR team was ambushed and wiped out. Faked his own death and went shadow, and has spent years hunting Brown's identity.",
        "notes": (
            "No combat stat block given; a Legwork subject only. Refuses to haggle pay (his own money, "
            "not corp funds): 15,000 nuyen split on success, a 2-year DocWagon Platinum contract and "
            "SIN, ~1,000 nuyen/week during the posting, plus his Sonics season pass if pushed hard. "
            "Pays for the job with money promised by a trid station for his own exposed story."
        ),
    },
    {
        "name": "Elizabeth 'Liz' Yamato",
        "role": "DocWagon Internal Security officer who trains and runs the fake TRP team on Bob's behalf",
        "archetype": "Internal Security",
        "title": "Officer, DocWagon Internal Security Division",
        "race": "Dwarf",
        "gender": "Female",
        "organization": "DocWagon",
        "connection": 2,
        "description": "Leans against the Citymaster's door with a husky, sexy voice that catches new recruits by surprise: 'Any of you need a shot of Morphine?' -- then, once they answer with the Sonics code phrase, 'Get in. It's time to make you into spies.' All business and fully aware of what she risks compressing DocWagon's usual three-week TRP training course into 48 hours; she takes her job, and the risk to her career if it goes wrong, seriously.",
        "notes": "No combat stat block given (gamemaster's discretion). Drives Citymaster #264-10, oversees the mole hunt, and arrives with ISD muscle once the party has hard evidence.",
    },
    {
        "name": "Seth Palatine",
        "role": "Expert Team Three paramedic; devout, weary veteran medic and one of Malpractice's alternate mole candidates",
        "archetype": "Paramedic",
        "title": "Paramedic, DocWagon Expert Team Three",
        "race": "Human",
        "gender": "Male",
        "organization": "DocWagon",
        "connection": 2,
        "description": "Almost always acts in a business-like manner, masking his feelings from others and, most of the time, from himself; nearly twenty years on the front lines of Seattle's street war have left deep worry lines on his face and made him feel vulnerable whenever he shows real emotion. Spends much of his downtime alone in his room reading the Koran.",
        "background": "Lost his father and two sisters to VITAS-II as a child; his mother died from injuries suffered in a 2049 Sons of Sauron bombing (retaliation for a Humanis strike into the Ork Underground) that killed 38 people, an event Seth witnessed firsthand as a Metroplex Guard cordon kept him from the wounded.",
        "notes": (
            "B4 Q5 S3 C3 I4 W5, Ess6, React4; Threat/Prof 2/3; Orthoskin2; Biotech6, Biology2[Medicine4], "
            "Athletics3, Urban Stealth3; Beretta Model 110-T (gel rounds), AZ-150 Stun Baton, DocWagon "
            "Armor Jacket 5/3. Default innocent unless the GM makes him the mole."
        ),
    },
    {
        "name": "Vivianne Geldhausmann",
        "role": "Expert Team Three's team psychiatrist and paramedic; grieving widow and alternate mole candidate",
        "archetype": "Paramedic",
        "title": "Psychiatrist / paramedic, DocWagon Expert Team Three",
        "race": "Human",
        "gender": "Female",
        "organization": "DocWagon",
        "connection": 2,
        "description": "The team's psychiatrist, graduated eighth in her class at Cambridge; cheerful, quick to smile, and a great help to the rest of the team in coping with the day-to-day horrors they witness, though she walks with a slight limp -- the legacy of a gunshot to the leg taken pulling a client from a gang war years ago. Her once-bright outlook has never fully recovered from her husband's murder.",
        "background": "Husband Jacob, a photojournalist moonlighting as a Lone Star informant, was killed during the 2052 Ancients gang war after his footage cleared the Ancients of starting it; his killer was never caught.",
        "notes": (
            "B3 Q3 S3 C5 I4 W4, Ess6, React3; Threat/Prof 2/2; Biotech4, Psychology5, Negotiation5; "
            "Ares Crusader MP (gel rounds), AZ-150 Stun Baton, DocWagon Armor Jacket 5/3. Default "
            "innocent unless the GM makes her the mole (motive per the book: told by Brown that his "
            "people would use the DNA to cure VITAS-3)."
        ),
    },
    {
        "name": "Gordon 'Hawkeye' Kurtz",
        "role": "Expert Team Three's brash, stimulant-dependent paramedic and physical adept; alternate mole candidate",
        "archetype": "Paramedic (Physical Adept)",
        "title": "Paramedic, DocWagon Expert Team Three",
        "race": "Human",
        "gender": "Male",
        "organization": "DocWagon",
        "connection": 2,
        "description": "In his late twenties but still looks about eighteen; a ladies' man of any metatype or ethnicity, known for a jovial manner and sharply funny one-liners. When his current dose of stimulant starts to wear off he turns bitter and mean, singling out one person to pick on and rag until he is in danger of getting punched in the mouth.",
        "background": "Ex-Crashcart medic hired by DocWagon in late 2052; relies on stimulants to fit an active social life around a demanding job and funds the habit by embezzling and selling DocWagon supplies to his suppliers.",
        "notes": (
            "Magically active: B5(7) Q5 S4 C4 I2 W4, Magic6, Ess6, React3; Threat/Prof 3/3 (2 extra "
            "dice from Combat Sense); Adept Powers Combat Sense2, Improved Body2, Pain Resistance1; "
            "Biotech5[First Aid7]; Ares Predator II (gel rounds), AZ-150 Stun Baton. Default innocent "
            "unless the GM makes him the mole (motive: Brown blackmails his stimulant habit)."
        ),
    },
    {
        "name": "Shawn Ferrer",
        "role": "Expert Team Three's dwarf rigger-paramedic; the book's default mole, secretly selling client DNA samples to Brown",
        "archetype": "Rigger / Paramedic",
        "title": "Rigger / paramedic, DocWagon Expert Team Three",
        "race": "Dwarf",
        "gender": "Male",
        "organization": "DocWagon",
        "connection": 3,
        "description": "Ear surgery makes him pass as human at a glance -- the gamemaster's option to give him the Human-Looking Flaw, per the book. Speaks softly and slowly, rarely meeting the eyes of whoever he's addressing; unwinds off-duty by practicing yo-yo tricks. Tall for a dwarf and once accomplished enough at sports that classmates called him 'a respectable halfer,' though the phrase still stings.",
        "background": (
            "Ex-CAS military transport pilot; nearly drowned in 2051 when Caribbean League pirates "
            "capsized his landing craft and came to believe his human unit-mates hesitated to save "
            "him because he was a dwarf. Had cosmetic surgery on his ears afterward and retrained as a "
            "DocWagon rigger/paramedic (training completed March 2053, assigned to Team Three ~nine "
            "months later, though the book elsewhere says Team Three has existed 'since 2054' -- both "
            "dates as printed). Recruited by Brown, who promised to one day 'make him all human' in "
            "exchange for DNA samples; has fed Brown information for three years."
        ),
        "notes": (
            "B4 Q3 S4 C2 I3(4) W4, Ess1.4, React3 (7+3D6 rigging); Threat/Prof 3/3; claustrophobic "
            "(does not affect him rigging); Vehicle Control Rig2, Cerebral Booster1, Orthoskin1; "
            "Hammerli Model 610S (gel rounds), AZ-150 Stun Baton. The book's default culprit -- caught "
            "by rigging the Citymaster's tire to blow near a public telecom so he can transmit the "
            "stolen data, with a 'Cleopatra' dead-man's-switch email that alerts Brown if his capture "
            "isn't delayed within 24 hours."
        ),
    },
    {
        "name": "Earl Brown",
        "role": "Mercenary front man for an unnamed organization buying metahuman DNA and medical records through a DocWagon mole",
        "archetype": "Mercenary Handler",
        "title": "Contractor / handler, unnamed organization",
        "race": "Human",
        "gender": "Male",
        "connection": 4,
        "description": "Speaks in careful ambiguities, never states anything outright, and lets people draw their own conclusions; a former UCAS Army tactical-computer test subject whose implanted computer has left him cold and calculating. Directs an ambush on a DocWagon ambulance with the same flat calm he might use ordering lunch -- 'Fire one!... Fire two!... Bait has been discarded' -- then muses about catching a movie afterward while breaking down his rifle.",
        "background": (
            "Dishonorably discharged and imprisoned two years after crippling a senator's son in a "
            "drunken fight; resurfaced as a mercenary hunting DNA samples for an organization the book "
            "deliberately leaves unnamed (left to each GM to define, possibly via a Threats-sourcebook "
            "faction). Ambushed and nearly wiped out Robert Khamdeng's DocWagon team in 2054 after "
            "Khamdeng refused his offer; still runs a mole on Expert Team Three."
        ),
        "notes": (
            "B5 Q6(7) S2(3) C4(6) I4 W3, Ess0.6, React5(6); Threat/Prof 5/4; Tactical Computer1, "
            "Boosted Reflexes1, cybereyes w/rangefinder, Smartlink II; Damage Compensators6, Enhanced "
            "Articulation, Muscle Augmentation1, Tailored Pheromones2; Barret Model 121 sniper rifle "
            "(APDS), Colt Cobra SMG (APDS), Interrogation6[Torture8]. Stages the Spring Lakes ambush "
            "personally, guiding LAWS rockets via tactical computer, and flees before the fight ends "
            "to keep his own hands clean. Intended by the book to become a lasting shadowrunner Enemy."
        ),
    },
    {
        "name": "Salthili Truan",
        "role": "Kidnapped 13-year-old elf DocWagon Platinum client, used by Earl Brown as bait for his final ambush",
        "archetype": "Victim",
        "title": "Platinum client (child)",
        "race": "Elf",
        "gender": "Male",
        "age": 13,
        "connection": 1,
        "description": "A wealthy Spring Lakes, Renton family's son; Brown kidnaps him en route home from school, keeps him bound and unconscious, then drops him from the fourth floor of the Spring Lakes construction site to fake a medical emergency and lure Team Three's Citymaster into the ambush.",
        "notes": "No combat stat block given. Dies if the responding paramedics cannot reach and revive him within 7 combat turns of the ambush beginning.",
    },
    {
        "name": "Benjamin Steele",
        "role": "AresSpace Security manager who tasks the player characters with investigating the Dunkelzahn's-will Mars photos",
        "archetype": "Corporate Handler",
        "title": "Manager, AresSpace Security",
        "race": "Human",
        "gender": "Male",
        "organization": "AresSpace",
        "connection": 3,
        "description": "Seated at the far end of the briefing-room table with a small projector at hand, gesturing for the team to take their seats before dimming the lights on the three Mars photographs: 'Good morning. Let's get down to business.' Businesslike and controlled in front of the team, but personally obsessed with proving Cydonia was sabotage rather than incompetence.",
        "background": "A mid-level manager in data transmission and interpretation when Project Cydonia's data turned out to be worthless static and a faked photo, Steele's career nosedived; AresSpace reassigned him to the low-status job of requisitions manager. He clawed his way back into a position of authority in AresSpace Security through sheer hard work, but has never forgotten the fiasco and has spent years quietly chasing the truth behind it.",
        "notes": (
            "No combat stat block given. Provides the team a 100,000-nuyen operating budget, Cydonia "
            "system passcodes, and transport. Quietly arranges the 'accidental' deaths of Yavin and "
            "Xavier after the mission as personal revenge for his ruined career; keeps the whole truth "
            "buried per AresSpace corporate orders."
        ),
    },
    {
        "name": "Dr. Robert Zeus",
        "role": "Retired Operation Discovery research scientist, assassinated by a Veil sniper mid-interview with the player characters",
        "archetype": "Scientist",
        "title": "Retired research scientist, Operation Discovery",
        "race": "Human",
        "gender": "Male",
        "age": 72,
        "connection": 2,
        "description": "Average height and build, thick gray hair and glasses, looks younger than his 72 years -- an old man still indulging a lifelong weakness for browsing the Matrix ('an old man was surely entitled to his few pleasures, wasn't he?'). Nervous, chain-smoking, paces as he talks and takes real pride and a hint of nostalgia in recounting his work on Operation Discovery. Insists on meeting in a public park, Brook Park, on the theory that a crowd of civilians will deter an attacker -- he is wrong.",
        "background": "One of the scientists who debriefed the Operation Discovery astronauts and studied the Martian samples; has lived under the knowledge of the cover-up for decades and immediately recognized the Dunkelzahn's-will photos.",
        "notes": (
            "No combat stat block given (killed before combat could occur). Can disclose up to ten key "
            "facts about Operation Discovery, Project Cydonia and the Hoffman Farm storage facility "
            "before a Veil sniper puts a single silenced round through his head from 300 yards; the "
            "sniper then fires two more rounds at the party before withdrawing. His home has already "
            "been searched and trashed by Veil's cleanup crew."
        ),
    },
    {
        "name": "Lt. Col. James Yavin",
        "role": "Retired USAF officer, the sole surviving astronaut of Operation Discovery's 2011 Mars mission",
        "archetype": "Retired Officer",
        "title": "Lieutenant Colonel, USAF (retired)",
        "race": "Human",
        "gender": "Male",
        "age": 75,
        "connection": 2,
        "description": "Thinning gray hair, slight build, cynical and embittered, long since lost faith in his country; lives quietly at Ellington Air Force Base surrounded by photos of himself with a NASA space shuttle and a Saturn-V-class rocket. Has been waiting for someone to knock on his door ever since the Mars photos went public and tells his story like a man half expecting not to be believed: 'If I hadn't seen it with my own eyes... I know it sounds incredible, but....'",
        "background": "One of only three survivors of the Operation Discovery crash on December 24, 2011; the other two have since died. Convinced the timing of the crash and the appearance of the great dragon Ryumyo (marking the Awakening) are connected.",
        "notes": (
            "No combat stat block given. Bugged by Veil since the Mars photos surfaced; will confirm "
            "the photos, the mission, the crash, and the Hoffman Farm storage location if treated "
            "civilly. Dies of a 'massive coronary' shortly after the adventure -- Steele's quiet "
            "revenge."
        ),
    },
    {
        "name": "Karl Xavier",
        "role": "Ex-NASA/AresSpace employee and secret Veil mole who sabotaged Project Cydonia, now Astrotech Industries' founder and an AresSpace rival",
        "archetype": "Corporate Executive",
        "title": "Founder / CEO, Astrotech Industries",
        "race": "Human",
        "gender": "Male",
        "age": 70,
        "organization": "Astrotech Industries",
        "connection": 3,
        "description": "In excellent health for his age, thick gray hair, thin-rimmed glasses, dark business suit, a concealed Fichetti Security 500 under the jacket; a man of deliberately ambiguous loyalties.",
        "background": "Transferred from NASA to AresSpace at the 2016 buyout while secretly still working for Veil; sabotaged Project Cydonia's transmission data and framed MUFON for it, then left both AresSpace and Veil to found Astrotech Industries using his stolen copy of the real data as leverage.",
        "notes": (
            "B3 Q2 S2 I5 W5 C5; Threat/Prof 4/4; Computer5, Electronics4, Firearms3, Interrogation5, "
            "Leadership4, Military Theory3, Negotiation4, Psychology3; Chipjack, Datajack100Mp; "
            "Armored Clothing3/1, Fichetti Security 500. Meets the party at his 23rd-floor Houston "
            "conference room, backed by 2 guards (8 more, then 6 heavier-armed reinforcements, on "
            "call). Dies in a 'mysterious car crash' shortly after the adventure -- Steele's revenge."
        ),
    },
    {
        "name": "John Silver",
        "role": "Veil cleanup crew leader, a delta-grade cyborg mercenary with no reservations about killing loose ends",
        "archetype": "Mercenary",
        "title": "Team leader, Veil cleanup crew",
        "race": "Human",
        "gender": "Male",
        "organization": "Veil",
        "connection": 3,
        "description": "Tall, muscular, blond crew cut, almost always in a dark business suit; will not negotiate under any circumstances.",
        "notes": (
            "B4(6) Q5(6) S5(6) C3 I4(7) W4, Ess.625, React4(8); Threat/Prof 6/4; Task Pool2 "
            "(Encephalon); delta-grade Chipjack, Cybereyes, Datajack, Dermal Plating2, Encephalon2, "
            "Muscle Replacement1, Reaction Enhancer+2, Smartlink, Tactical Computer1, Wired Reflexes1; "
            "Cerebral Booster2, Synaptic Accelerator2; Ares Alpha Combat Gun, Ares Predator, Partial "
            "Heavy Armor6/4, Demolition Kit, 4 offensive grenades. Leads the Hoffman Farm silo assault "
            "and carries the demolition charges' detonators personally."
        ),
    },
    {
        "name": "Jason 'Eldritch' Mason",
        "role": "Veil combat mage backing up the cleanup crew and the Dr. Zeus assassination sniper",
        "archetype": "Combat Mage",
        "title": "Special agent (combat mage), Veil",
        "race": "Human",
        "gender": "Male",
        "organization": "Veil",
        "connection": 2,
        "description": "Tall, slender, dark hair and eyes; wears a business suit or an armored jacket depending on the job.",
        "background": "A veteran of UCAS special forces; after retiring from active military duty he joined Veil as a special agent, and has since risen to Grade 3 initiate.",
        "notes": (
            "Grade3 initiate; B3(5) Q4 S2 C2 I5 W5, Magic6(10), MagicPool6, Ess6; Threat/Prof 5/4; "
            "Conjuring4, Sorcery6; combat spells Hellblast4/Manaball4/Mana Bolt5/Power Bolt5/Ram5, "
            "detection spells incl. Personal Combat Sense5, Heal4, Armor3; Combat Spell Focus3, Power "
            "Focus4, Spell Lock(Armor). Guards Dr. Zeus's sniper astrally and will engage any player-"
            "character magician who investigates in astral space; part of the Hoffman Farm silo assault."
        ),
    },
    {
        "name": "Jeff 'Heartbreaker' Lisbon",
        "role": "UCAS Special Forces major and Operation Backhand's team commander, killed breaching Fort Ross's perimeter",
        "archetype": "Physical Adept Commando",
        "title": "Major, UCAS Special Forces",
        "race": "Elf",
        "gender": "Male",
        "age": 26,
        "connection": 2,
        "description": "Tall Anglo elf with a crew cut; a wild, prank-loving physical adept who transfers teams constantly, hence the nickname, and is manic and half-inspirational under pressure.",
        "background": "Grew up bullied in Seattle's elven district, discovered his adept powers at sixteen, and rose through air-mobile infantry into EOD, thaumaturgic applications and eventually Delta Force.",
        "notes": (
            "B5 Q7(8) S5 C6 I4 W6, Magic8, Ess6, React5(6); Threat/Prof 8/4; Physical Adept Powers "
            "incl. Improved Physical Senses, Improved Abilities, Increased Reflexes1, Killing Hands(M), "
            "Pain Resistance4, Spell Shroud2; Firearms6, Unarmed Combat6, Gunnery5. Insists on taking "
            "point at the mountain entrance and is killed instantly by twin Sentry guns the moment the "
            "team breaches -- scripted to die early and leave the party leaderless. Carries a "
            "classified dossier revealing the UCAS deliberately let Fenmore's operation grow to see "
            "what he would build."
        ),
    },
    {
        "name": "Michael Thorndike ('Archangel Michael')",
        "role": "Schizophrenic Grade 3 initiate hermetic mage who genuinely believes himself the Archangel Michael, City of God's spiritual and magical leader",
        "archetype": "Cult Leader / Combat Mage",
        "title": "'Archangel Michael', spiritual leader of the City of God",
        "race": "Human",
        "gender": "Male",
        "organization": "City of God",
        "connection": 3,
        "description": "An abused childhood and institutionalization produced full-blown delusion; underneath his illusion spells he is an ordinary, out-of-shape man with an unkempt beard in an ugly yellow lab coat. His astral form is a huge, six-winged, flaming-sworded angel invulnerable to physical attacks and shielded by a Force 8 mana barrier.",
        "background": "Fenmore recruited him off a trid news broadcast after he revealed his powers in a psychiatric hospital, recognizing an easily controlled, naive but powerful ally. Believes he once bound Dunkelzahn and cast him into a lake of fire for trying to 'rule the whole Earth' (he was nowhere near FDC at the time).",
        "notes": (
            "B3 Q3 S4 C6 I5 W9, Magic8, Ess5, React4; Threat/Prof 6/4; Initiatory Grade3; Sorcery6"
            "[Spellcasting8], Enchanting4, Leadership6[Religious8], Negotiation4[Intimidation6]; spells "
            "incl. Hellblast6, Landscape4 (quickened over his 'bedroom' to disguise it as Heaven), "
            "Mask5 (quickened over his own body), Control Thoughts6, Control Emotions6, Detect Phrase4 "
            "('City of God'), an anchored Fire Touch5 spell on his longsword; God's Wrath copper bowl "
            "(Power Focus2). Created the new spells Landscape, Personal Physical Shapechange, Shatter "
            "Armor and Fire Touch, taught to City of God students under religious terminology (see "
            "PLAY_NOTES). Dies easily once physically confronted in melee -- his real body is weak."
        ),
    },
    {
        "name": "Colonel Lawrence Fenmore",
        "role": "Disgraced ex-UCAS officer who founded the City of God to build a magical private army out of kidnapped children",
        "archetype": "Cult Founder / Commander",
        "title": "Colonel, UCAS Army (retired); founder, City of God",
        "race": "Human",
        "gender": "Male",
        "organization": "City of God",
        "connection": 4,
        "description": "Calculating, self-controlled, and far saner than Michael; a manipulative megalomaniac who genuinely believes he is protecting both society and his 'girls' by turning them into weapons.",
        "background": (
            "Traumatized by restraint duty on newly goblinized metahumans in 2021 and by Tir "
            "Tairngire's forced expulsion of his family from Oregon, Fenmore came to see magic (not "
            "metahumanity) as the real coming threat. His marriage ended, a critical weapons contract "
            "was handed to Tir-owned Telestrian Industries, and he was passed over for brigadier "
            "general in 2050; he rediscovered Fort Ross's plans in 2051, faked a medical retirement at "
            "51, and used decker 'Mr. Mo' to launder funding through the Volgograd Seven and other "
            "criminal sources."
        ),
        "notes": (
            "B4 Q4 S3 C5 I5 W5, Ess5.3, React4+1D6; Threat/Prof 4/3; Datajack w/50Mp headware memory, "
            "tooth compartment with cyanide; Negotiation6, Psychology6[Conditioning9], Interrogation4"
            "[Verbal6], Military Theory6[Strategy8]; FFBA level3 (4/1). Attempts to negotiate a UCAS-"
            "sanctioned future for the City of God once Michael is dead; if refused, signals four "
            "loyalist soldiers ('Fenmore's Friends,' full military stat block, Threat/Prof drops to 2 "
            "if he dies) for a final mundane firefight. Surviving and escaping makes him a 4-point "
            "Enemy (Power3, Motivation5, Knowledge3)."
        ),
    },
    {
        "name": "Elizabeth Moonstraw",
        "role": "T-bird rigger supplying Fort Ross, captured and interrogated by UCAS agents; killed herself and her interrogators via an anchored spell",
        "archetype": "Smuggler Rigger",
        "title": "T-bird rigger, Fort Ross supply line",
        "race": "Human",
        "gender": "Female",
        "nationality": "Salish-Shidhe",
        "connection": 1,
        "description": "A blond crew-cut gives her the proto-military, masculine look favored by T-bird riggers; her eyes are ringed with deep bruises, her face lined with fatigue and fear under interrogation, but her defiance keeps surfacing -- 'Am I allowed to say no?' and 'If you already know, why are you doing this? For kicks?' From Olympia, Salish-Shidhe, flying supply runs from Trans-Polar Aleut through the Athabascan Council to Maine before she was caught.",
        "notes": "No combat stat block given (dies in the prologue). Her death is the inciting incident that sends UCAS Army Rangers, and then the player characters, after Fort Ross.",
    },
    {
        "name": "General Daly",
        "role": "UCAS general who briefs and commands Operation Backhand from the rear",
        "archetype": "Military Commander",
        "title": "General, UCAS Army",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": "By-the-book, gives an ironic smile before every briefing, and is willing to answer honest questions -- but conceals that a prior Army Ranger recon team sent to Fort Ross never returned, judging it unnecessary information for morale. Opens the mission briefing crisply: 'Gentlemen and ladies, at 02:33:15 Pacific Standard Time, 3 December, our defense satellites spotted this shape over the Trans-Polar Aleut Nation... someone or something is in there who does not want to be found.'",
        "notes": "No combat stat block given. Issues the mission briefing and rendezvous coordinates, and later debriefs the surviving team, deciding what becomes of the City of God's rescued girls.",
    },
    {
        "name": "Gabriel",
        "role": "One of Michael's six 'Alphas' -- the oldest, most loyal, best-trained physical-adept students at Fort Ross, gathered around his throne as his personal guard",
        "archetype": "Physical Adept",
        "title": "Alpha-rank student (physical adept), City of God",
        "race": "Human",
        "gender": "Female",
        "organization": "City of God",
        "connection": 2,
        "description": "Fights in Full Heavy Armor magically masked by a Fashion spell to look like angelic robes and wings, wielding a longsword Weapon Focus at Michael's side. A brainwashed fanatic who believes absolutely that Michael is the literal Archangel Michael; the book gives no individual physical description beyond the shared angelic disguise she and her five sister-Alphas wear into battle.",
        "background": "Kidnapped as a magically active child from a magophobic family and raised at Fort Ross under Michael's religious-military training; now his most trusted enforcer, the oldest and highest-ranked of the City of God's Alpha students.",
        "notes": (
            "Initiatory Grade3; Threat/Prof 5/4; Armed Combat6[Edged Weapons8], Athletics5, Firearms2, "
            "Leadership3[Military5], Magical Theory5, Military Theory5[Tactics7], Stealth4, Survival"
            "(Wilderness)4, Unarmed Combat6[Wing Chun Kung Fu8]; Physad Powers: Improved Ability[Armed "
            "Combat+2], Improved Physical Senses[Flare Compensation, Hearing Damper, Low-Light Vision, "
            "Thermographic Vision], Increased Reaction1, Increased Reflexes2, Killing Hands(S). Gear: "
            "God's Wrath (Power Focus2, believed usable by Michael), Longsword (Str+3/M, Rating3 "
            "Weapon Focus), Full Heavy Armor (masked). Fastest Initiative of the three physad Alphas "
            "(3D6+6)."
        ),
    },
    {
        "name": "Raphael",
        "role": "One of Michael's six 'Alphas' -- a physical-adept student honed for melee, gathered around his throne as his personal guard",
        "archetype": "Physical Adept",
        "title": "Alpha-rank student (physical adept), City of God",
        "race": "Human",
        "gender": "Female",
        "organization": "City of God",
        "connection": 2,
        "description": "Fights in Full Heavy Armor magically masked by a Fashion spell to look like angelic robes and wings, wielding a longsword Weapon Focus. The most heavily boosted melee combatant of the three physad Alphas, trained to close distance and strike before an enemy can react; a brainwashed fanatic who believes absolutely that Michael is the literal Archangel Michael.",
        "background": "Kidnapped as a magically active child from a magophobic family and raised at Fort Ross under Michael's religious-military training; drilled into one of his most physically dangerous Alpha bodyguards.",
        "notes": (
            "Initiatory Grade3; Threat/Prof 5/4; same shared skills as Gabriel/Samael; Physad Powers: "
            "Distance Strike, Increased Reflexes1, Improved Ability[Armed Combat+4, Athletics+2, "
            "Stealth+2, Unarmed Combat+4], Improved Physical Senses[Direction Sense, High Frequency "
            "Hearing, Thermographic Vision], Temperature Tolerance2. Gear: God's Wrath (Power Focus2), "
            "Longsword (Str+3/M, Rating3 Weapon Focus), Full Heavy Armor (masked). Initiative 2D6+5."
        ),
    },
    {
        "name": "Samael",
        "role": "One of Michael's six 'Alphas' -- a physical-adept student built to endure punishment, gathered around his throne as his personal guard",
        "archetype": "Physical Adept",
        "title": "Alpha-rank student (physical adept), City of God",
        "race": "Human",
        "gender": "Female",
        "organization": "City of God",
        "connection": 2,
        "description": "Fights in Full Heavy Armor magically masked by a Fashion spell to look like angelic robes and wings, wielding a longsword Weapon Focus. The toughest of the three physad Alphas, able to shrug off punishment that would drop the others; a brainwashed fanatic who believes absolutely that Michael is the literal Archangel Michael.",
        "background": "Kidnapped as a magically active child from a magophobic family and raised at Fort Ross under Michael's religious-military training; the Alpha most trusted to hold a line and keep fighting.",
        "notes": (
            "Initiatory Grade3; Threat/Prof 5/4; same shared skills as Gabriel/Raphael; Physad Powers: "
            "Astral Perception, Improved Physical Senses[Enhanced Hearing, Enhanced Smell, Low-Light "
            "Vision], Increased Reflexes1, Killing Hands(S), Pain Resistance6. Gear: God's Wrath (Power "
            "Focus2), Longsword (Str+3/M, Rating3 Weapon Focus), Full Heavy Armor (masked). Initiative "
            "2D6+5; the only physad Alpha with astral perception, so she alerts the group to astral "
            "intrusion."
        ),
    },
    {
        "name": "Anael",
        "role": "One of Michael's six 'Alphas' -- a hermetic mage and sorcery adept student, gathered around his throne as his personal guard",
        "archetype": "Hermetic Mage / Sorcery Adept",
        "title": "Alpha-rank student (hermetic mage), City of God",
        "race": "Human",
        "gender": "Female",
        "organization": "City of God",
        "connection": 2,
        "description": "Fights in Full Heavy Armor magically masked to look like angelic robes and wings, wearing a Golden Halo spell lock that holds a quickened Increase Reflexes spell. One of the three spellcasting Alphas who layer Shatter Armor onto the physad Alphas' targets and hide the whole group behind Michael's Force 8 mana barrier; a brainwashed fanatic who believes absolutely that Michael is the literal Archangel Michael.",
        "background": "Kidnapped as a magically active child from a magophobic family and raised at Fort Ross under Michael's religious-military and hermetic training; one of the three Alpha students who carry both Conjuring and Enchanting skill (the book notes Cassiel alone lacks one of these).",
        "notes": (
            "Initiatory Grade1; Threat/Prof 5/4; Armed Combat3, Athletics4, Conjuring4, Enchanting4, "
            "Leadership5[Military7], Magical Theory7, Military Theory6[Tactics8], Singing5, Sorcery7, "
            "Stealth3, Survival(Wilderness)4, Theology4, Unarmed Combat3[Wing Chun Kung Fu5]; spells "
            "incl. Shatter Armor5, Personal Bullet Barrier6, Mind Probe6, Mana Barrier6, Heal5, Fashion4, "
            "Compel Truth5, Invisibility5, Powerball6, Stunbolt5. Gear: Longsword (Str+3 M), Full Heavy "
            "Armor (masked), God's Wrath (Level2 Power Focus), Golden Halo (Spell Lock, Increase "
            "Reflexes+3). Initiative 4D6+5."
        ),
    },
    {
        "name": "Cassiel",
        "role": "One of Michael's six 'Alphas' -- a hermetic mage and sorcery adept student, gathered around his throne as his personal guard",
        "archetype": "Hermetic Mage / Sorcery Adept",
        "title": "Alpha-rank student (hermetic mage), City of God",
        "race": "Human",
        "gender": "Female",
        "organization": "City of God",
        "connection": 2,
        "description": "Fights in Full Heavy Armor magically masked to look like angelic robes and wings, wearing a Golden Halo spell lock that holds a quickened Increase Reflexes spell. The book's stat block footnotes that Cassiel alone among the three spellcasting Alphas lacks one shared skill (Conjuring or Enchanting, as printed); a brainwashed fanatic who believes absolutely that Michael is the literal Archangel Michael.",
        "background": "Kidnapped as a magically active child from a magophobic family and raised at Fort Ross under Michael's religious-military and hermetic training alongside Anael and Sachiel.",
        "notes": (
            "Initiatory Grade1; Threat/Prof 5/4; same shared skill list as Anael/Sachiel except one "
            "skill (Conjuring or Enchanting) per the book's asterisk footnote; same spell list incl. "
            "Shatter Armor5, Personal Bullet Barrier6, Mind Probe6, Mana Barrier6, Heal5. Gear: "
            "Longsword (Str+3 M), Full Heavy Armor (masked), God's Wrath (Level2 Power Focus), Golden "
            "Halo (Spell Lock, Increase Reflexes+3). Initiative 4D6+5."
        ),
    },
    {
        "name": "Sachiel",
        "role": "One of Michael's six 'Alphas' -- a hermetic mage and sorcery adept student, gathered around his throne as his personal guard",
        "archetype": "Hermetic Mage / Sorcery Adept",
        "title": "Alpha-rank student (hermetic mage), City of God",
        "race": "Human",
        "gender": "Female",
        "organization": "City of God",
        "connection": 2,
        "description": "Fights in Full Heavy Armor magically masked to look like angelic robes and wings, wearing a Golden Halo spell lock that holds a quickened Increase Reflexes spell. One of the three spellcasting Alphas who layer Shatter Armor onto the physad Alphas' targets and hide the whole group behind Michael's Force 8 mana barrier; a brainwashed fanatic who believes absolutely that Michael is the literal Archangel Michael.",
        "background": "Kidnapped as a magically active child from a magophobic family and raised at Fort Ross under Michael's religious-military and hermetic training alongside Anael and Cassiel.",
        "notes": (
            "Initiatory Grade1; Threat/Prof 5/4; Armed Combat3, Athletics4, Conjuring4, Enchanting4, "
            "Leadership5[Military7], Magical Theory7, Military Theory6[Tactics8], Singing5, Sorcery7, "
            "Stealth3, Survival(Wilderness)4, Theology4, Unarmed Combat3[Wing Chun Kung Fu5]; same "
            "spell list as Anael incl. Shatter Armor5, Personal Bullet Barrier6, Mind Probe6, Mana "
            "Barrier6, Heal5. Gear: Longsword (Str+3 M), Full Heavy Armor (masked), God's Wrath (Level2 "
            "Power Focus), Golden Halo (Spell Lock, Increase Reflexes+3). Initiative 4D6+5."
        ),
    },
    {
        "name": "Miss Onizuka",
        "role": "Shadowrunning decker whose Black-IC-inflicted wounds and dump shock draw Expert Team Three's Citymaster into a running Lone Star gun battle",
        "archetype": "Decker",
        "title": "Decker (shadowrunner)",
        "race": "Human",
        "gender": "Female",
        "age": 23,
        "connection": 1,
        "description": "5'4\", 110 pounds, black hair and black eyes cosmetically altered to purple; wears a datajack and headware memory. Nearly died breaking into a Lone Star facility's evidence-locker system when black IC caught her before she could finish copying files, and now suffers a Deadly Stun wound and a Serious Physical wound on top of severe dump shock from being yanked offline by a teammate.",
        "background": "Part of a small shadowrunning team (one mercenary, a rigger, two street samurai and Onizuka herself as decker) that broke into a Lone Star facility to remove an incriminating item from an evidence locker; while inside, she stumbled onto files proving the facility's director was embezzling from the company, triggering the black IC that nearly killed her and the running gun battle that follows.",
        "notes": "No combat stat block given (use the Decker archetype, Virtual Realities 2.0 p.79, if needed). DocWagon's Expert Team Three responds to the dispatcher's call for 'Miss Onizuka' without realizing she is a shadowrunner caught in a Lone Star cover-up rather than an ordinary client.",
    },
    {
        "name": "Casey Green",
        "role": "T-bird rigger for the City of God supply line, found frozen to death in his overturned panzer after being caught in the same arctic storm as the player characters",
        "archetype": "Smuggler Rigger",
        "title": "T-bird rigger, Fort Ross supply line",
        "race": "Human",
        "gender": "Male",
        "nationality": "Anglo",
        "connection": 1,
        "description": "Identified only by the wallet in his pocket; found dead inside his overturned GMC Banshee panzer, which the characters may shelter in overnight since its garbage-packed hold makes good insulation despite the smell. Carries little besides a certified credstick for 5,000 nuyen -- evidence he had just been paid for a supply run before the storm caught him on the way back from the mountain.",
        "notes": "No combat stat block given (already dead when found). His death, alongside Elizabeth Moonstraw's capture, is one of two signs the player characters find of the City of God's ongoing supply operation before they ever reach Fort Ross itself.",
    },
    {
        "name": "Mr. Mo",
        "role": "Former UCAS military decker and friend of Colonel Fenmore who laundered the funding that built the City of God",
        "archetype": "Decker (Financier)",
        "title": "Financier / decker, City of God (off-site)",
        "race": "Human",
        "gender": "Male",
        "organization": "City of God",
        "connection": 1,
        "description": "Never appears in person; known only from a soldiers' office at Fort Ross whose back wall of evidence links him to a wide web of dirty money -- the Volgograd Seven, corrupt Japanese military officers, organized crime figures in Detroit, and numerous unwitting tipped-off banks and investors.",
        "background": "A former UCAS military decker Fenmore turned to for money when he decided to found the City of God; Mr. Mo found it, laundering the funding for the entire project through criminal and financial channels around the world.",
        "notes": "No combat stat block or physical description given. A pure evidence trail rather than an on-screen character -- discovered through the paperwork in Fort Ross's staff office (see Fort Ross location notes).",
    },
    {
        "name": "Dr. Rampart",
        "role": "Renraku researcher whose skepticism about Cuca's new conditioning drugs is overruled and dismissed",
        "archetype": "Researcher",
        "title": "Researcher, Renraku Computer Systems",
        "race": "Human",
        "organization": "Renraku Computer Systems",
        "connection": 1,
        "description": "Never appears on-page; known only through Marcus Powell's passing question to Dr. Cuca -- 'Dr. Rampart suggested that they might reduce the real-world effectiveness of the conditioning' -- and Cuca's dismissive rebuttal that Rampart 'based that theory on one outdated drug-interaction report.'",
        "notes": "No combat stat block given; a single skeptical voice inside the Futuremen project, overruled before the player characters ever hear the name.",
    },
]

ORG_UPDATES = {
    "Renraku Computer Systems": {
        "notes_append": (
            "Missions: ran a black-project behavior-control experiment out of a fake Ravenna chop "
            "shop and music store (see The Futuremen), implanting voice-triggered conditioning "
            "devices in unwitting 'patients' to build an on-call cybersoldier squad. Exposed by a "
            "Lone Star investigation into missing undercover Sgt. Franco Tanner; corporate leadership "
            "publicly disowned project lead Marcus Powell and Dr. Cuca as 'renegade employees' rather "
            "than admit sponsorship, and may have quietly relocated the project to another city."
        ),
    },
    "Ares Macrotechnology": {
        "notes_append": (
            "Missions: its AresSpace division (see AresSpace org) traces to the 2016 NASA buyout, "
            "which folded in the secret, decades-buried Operation Discovery Mars program. When an "
            "AresSpace security team confirmed the Operation Discovery/Project Cydonia cover-up in "
            "2057, Damien Knight's leadership chose to bury the story rather than jeopardize AresSpace's "
            "UCAS government contracts, forfeiting Dunkelzahn's 1%-Ares-stock bequest for solving the "
            "riddle in his will."
        ),
    },
    "DocWagon": {
        "notes_append": (
            "Missions (Malpractice): launched the Temporary Response Personnel (TRP) program in late "
            "August 2057 -- shadowrunner-caliber security temps embedded two weeks at a time with High "
            "Threat Response teams -- on a trial basis through August 2058. Expert Team Three (Seth "
            "Palatine, Vivianne Geldhausmann, Gordon Kurtz, Shawn Ferrer), based out of the 83rd Street "
            "Clinic, harbored a mole selling client DNA and medical records to a mercenary handler "
            "known only as 'Mr. Brown'; runners posing as TRPs exposed the leak (the book's default "
            "culprit is Shawn Ferrer) during a live rotation."
        ),
    },
    "Lone Star Security": {
        "notes_append": (
            "Missions (Under the Influence): a squad of DI/DOC/DPI officers (or hired runners, in a "
            "non-Star campaign) traced undercover Sgt. Franco Tanner to a Renraku black project hidden "
            "beneath a Ravenna music store; case notes and NPC stat blocks (Foot Patrol Officer, FRT "
            "Trooper, DPI Combat Mage) reused elsewhere in the anthology (Malpractice's 'I Fought the "
            "Law' encounter involves a separate incident of Lone Star officers covering for an "
            "embezzling facility director)."
        ),
    },
    "Humanis Policlub": {
        "notes_append": (
            "Missions: Colonel Lawrence Fenmore, founder of the City of God cult/army (see org row), "
            "is a longtime member, though his acceptance of magic as a weapon rather than a threat "
            "puts him at odds with most Humanis doctrine (Malpractice). Robert 'Doctor Bob' Khamdeng "
            "was seen at a couple of Humanis recruitment meetings around 2049, for reasons never "
            "clarified (possibly mere curiosity)."
        ),
    },
    "Ancients": {
        "notes_append": (
            "Missions (Malpractice): Vivianne Geldhausmann's husband Jacob, a photojournalist "
            "moonlighting as a Lone Star informant, was murdered in late 2052 during a gang war "
            "involving the Ancients, shortly after his footage helped clear the Ancients of starting "
            "the conflict. His killer was never identified."
        ),
    },
    "Seattle Metroplex Guard": {
        "notes_append": (
            "Missions (Malpractice): Metroplex Guardsmen cordoned off the scene of a 2049 Sons of "
            "Sauron bombing (retaliation for a Humanis Policlub strike into the Ork Underground), "
            "preventing paramedic Seth Palatine from reaching the wounded -- including, unknowingly, "
            "his own mother, who died of her injuries afterward."
        ),
    },
}

LOC_UPDATES = {}
NPC_UPDATES = {}
TAG_EXISTING = {}

MATRIX_HOSTS = """
### Under the Influence -- Futuremen Project (Renraku), Ravenna, Seattle
| Node | Function | Color/Rating | Key IC |
|---|---|---|---|
| Host A | MindSound Music accounting/advertising + concealed body-shop records; UMS iconography (Maria Mercurial T-shirts on sales/accounting icons); trap door to Host C in Control | Green-6/8/10/8/9/10 | Probe-5, Jammer-7, Bouncer (upgrades to Orange-8), Cascading Jam-Rip-6, Trap Trace-8(Blaster-6), Expert Sparky-8, Shutdown |
| Host B | Cafe do Amazonia + Kennedy's Cheap Electronics front-business records; tapeworm IC in Control; trap door to Host C | Green-8/11/15/12/12/11 | Probe-6, Trace-8(Shield), Jam-Rip-8, Tar Pit-10, Active Alert+Trace-10, Construct(Armor,Shifting)+Blaster-5+Mark-Rip-5, Shutdown |
| Host C | Futuremen project core: names, cyberware manifests and Portuguese command list; sculpted as a guarded tropical beach | Red-10/18/15/16/16/13 | Cascading Mark-Rip-8, Trap Trace-10(Sparky-8), Passive Alert+Construct+Probe-6+Trace-6+Killer-6, Cascading Sparky-10, Active Alert (Renraku decker in 2D6 turns), Expert Black IC-8, Party IC, Cascading Black IC-10, Shutdown |

### Mission: Mars -- UCAS/Veil Host, Washington DC
| Node | Function | Color/Rating | Key IC |
|---|---|---|---|
| UCAS/Veil Host | Department of Defense + Veil records on the 2001 NASA mission, Operation Discovery and Project Cydonia; Paydata 13, Data Density 2D6x5 | Red-9/17/19/15/17/15 | Probe-9, Tar Baby-8, Trap Trace-10(Killer-9), Passive Alert, Expert Construct+Trace-8+Tar Baby-5+Marker-6, Cascading Blaster-9, Active Alert (govt decker arrives next turn), Expert Construct+Black IC-8(lethal)+Acid-7, Cascading Black IC-7(lethal), Shutdown |

### Mission: Mars -- Astrotech Industries, Houston (Tiered Access, 3 hosts)
| Node | Function | Color/Rating | Key IC |
|---|---|---|---|
| Host A | Standard corporate operations | Green-5/8/10/8/10/10 | Standard corp sheaf (per VR2.0 Ares Macrotechnology sheaf) |
| Host B | Standard corporate operations, tougher tier | Orange-10/13/13/14/13/15 | Standard corp sheaf (per VR2.0 Ares Macrotechnology sheaf) |
| Host C | Xavier's private files: 30 Mp Operation Discovery summary (incl. Hoffman Farm location) + 200 Mp original Project Cydonia data; spy-film sculpting, guarded by Superior-grade deckers; Paydata 10, Data Density 2D6x5 | Red-9/14/16/13/14/14 | Trace-10, Probe-8, Trap Probe-8(Killer-9), Passive Alert, Acid-10(Armor,Shifting), Expert Blaster-12/Defense+1, Active Alert (Astrotech decker in 2 turns), Expert Construct/Offense+2+Blaster-7+Acid-5+Tar Baby-4, Black IC-8(Armor)(lethal), Shutdown |
"""

NOT_BUILT = """
- The generic shadowrunning team backing up Miss Onizuka (mercenary, rigger, two street samurai),
  and the Lone Star patrol officers and FRT troopers in "Never Deal With the Wagon" -- all unnamed
  archetype reuse (Mercenary, Rigger, Street Samurai, Foot Patrol Officer, FRT Trooper); no names
  given beyond Onizuka herself.
- The abandoned warehouse near the Federated Boeing Shipyards -- Liz Yamato's improvised TRP
  training site; unnamed, single-scene, no map given.
- The nine optional "Sleepless in Seattle" emergency-call suggestions (Mr. Johnson chase, Elliot Bay
  plane crash, yakuza/Mafia crossfire, tanker explosion, hostage situation, apartment fire,
  Brackhaven Investments board member, go-gang car-jacking, I-405 traffic altercation) -- flavor
  prompts for the gamemaster to pick from, not built encounters.
- "Mr. Brown"'s employer organization (Malpractice) -- deliberately left unnamed by the book for
  each gamemaster to define; Earl Brown himself is built as an NPC with organization left blank.
- Karl Xavier's administrative assistant -- never named ("Xavier's administrative assistant will
  meet the characters"); and the generic Astrotech/AresSpace corporate security guards (Corporate
  Security Guard archetype reuse).
- The dead Army Ranger recon team found in the snow near Fort Ross -- four unnamed bodies (two
  human, two ork), an environmental horror beat, not individuated.
- The 33 City of God adult staff and 152 magically active girls beyond the six named Alphas --
  explicitly "no two of them are alike" in the book; represented in aggregate under the City of God
  org entry and the Fort Ross location rather than as individual NPCs.
"""

PLAY_NOTES = """
- Malpractice explicitly leaves the mole's identity to the gamemaster (Shawn Ferrer is the book's
  default write-up); swapping in Gordon Kurtz, Vivianne Geldhausmann or Seth Palatine (or making all
  four complicit) only requires re-flagging the relevant NPC notes, not rewriting the adventure.
- Mission: Mars deliberately never resolves what the Mars pyramids/skeleton actually are, nor
  whether the Operation Discovery crash and Ryumyo's appearance (the Awakening) are truly connected
  -- leave both as GM-determined mysteries per the source text.
- The anthology's four adventures share one theme worth playing up across all of them: every
  institution involved (Renraku, DocWagon corporate, AresSpace, the UCAS military) ultimately
  chooses its own deniability and self-interest over full disclosure, no matter what the player
  characters uncover or how the fight ends.
- King of the Mountain's four new spells (Landscape, Personal Physical Shapechange, Shatter Armor,
  Fire Touch) are Archangel Michael's own creations, taught with heavy Christian religious framing;
  the book leaves it to each gamemaster whether they leak into wider play once discovered.
- Character-creation guidance for each alternate campaign type (Lone Star cop, DocWagon TRP,
  AresSpace corporate security, UCAS Special Forces) lives in the source sourcebooks (Shadowrun
  Companion: Beyond the Shadows, primarily) and is not reproduced in these rows -- see the source
  text's "Getting Started" sections per scenario if running one as a one-shot for non-runner PCs.
- Both Under the Influence and King of the Mountain script an NPC ally death early on (Tanner is
  optional/negotiable; Heartbreaker's death at the Fort Ross perimeter is written as unavoidable) --
  telegraph the danger but do not feel obligated to fudge dice against the book's intent.
"""
