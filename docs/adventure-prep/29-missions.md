# Missions -- Adventure Prep: NPCs, Locations, Organizations, Matrix Systems

Source: Shadowrun 2e - Adventure - Missions {FASA7325}.pdf, pp. 4-96. Campaign order #29, in-game 2057-2058 (Mission: Mars prologue is dated 18 August 2057; Malpractice runs a TRP shift shortly after DocWagon's TRP program launched late August 2057; Under the Influence and King of the Mountain give no explicit year and are treated as roughly contemporary).

Everything below is loaded into the campaign DB flagged `is_active: false` and `source_adventure: "Missions"` by `python scripts/adventure_ingest/run.py missions`; flip entries active as the party meets them. Use the **Adventure** filter on the manage pages to see just this set.

## Plot synopsis

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

## Timeline

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

## NPCs (Persons of Interest)

| Name | Role | Org |
|---|---|---|
| Sgt. Franco Tanner | Lone Star undercover officer (alias 'Leopard' Leonard) whose Futuremen investigation turned him into an unwitting Futureman | Lone Star Security |
| Captain Burns | Lone Star captain who assigns the player characters to find missing Sgt. Tanner | Lone Star Security |
| Dr. Claudio 'Dr. Cuca' Andrade | Amazonian expatriate scientist running Renraku's Futuremen conditioning project out of a fake street clinic | Renraku Computer Systems |
| Marcus Powell | Ambitious Renraku manager running the Futuremen project's day-to-day operations and evidence control | Renraku Computer Systems |
| Lindy | Renraku operative posing as MindSound Music's clerk, screening potential Futuremen 'patients' and watching for trouble | Renraku Computer Systems |
| Robert 'Doctor Bob' Khamdeng | Ex-DocWagon paramedic turned shadowrunner, hiring the party directly to root out Brown's mole inside DocWagon | independent |
| Elizabeth 'Liz' Yamato | DocWagon Internal Security officer who trains and runs the fake TRP team on Bob's behalf | DocWagon |
| Seth Palatine | Expert Team Three paramedic; devout, weary veteran medic and one of Malpractice's alternate mole candidates | DocWagon |
| Vivianne Geldhausmann | Expert Team Three's team psychiatrist and paramedic; grieving widow and alternate mole candidate | DocWagon |
| Gordon 'Hawkeye' Kurtz | Expert Team Three's brash, stimulant-dependent paramedic and physical adept; alternate mole candidate | DocWagon |
| Shawn Ferrer | Expert Team Three's dwarf rigger-paramedic; the book's default mole, secretly selling client DNA samples to Brown | DocWagon |
| Earl Brown | Mercenary front man for an unnamed organization buying metahuman DNA and medical records through a DocWagon mole | independent |
| Salthili Truan | Kidnapped 13-year-old elf DocWagon Platinum client, used by Earl Brown as bait for his final ambush | independent |
| Benjamin Steele | AresSpace Security manager who tasks the player characters with investigating the Dunkelzahn's-will Mars photos | AresSpace |
| Dr. Robert Zeus | Retired Operation Discovery research scientist, assassinated by a Veil sniper mid-interview with the player characters | independent |
| Lt. Col. James Yavin | Retired USAF officer, the sole surviving astronaut of Operation Discovery's 2011 Mars mission | independent |
| Karl Xavier | Ex-NASA/AresSpace employee and secret Veil mole who sabotaged Project Cydonia, now Astrotech Industries' founder and an AresSpace rival | Astrotech Industries |
| John Silver | Veil cleanup crew leader, a delta-grade cyborg mercenary with no reservations about killing loose ends | Veil |
| Jason 'Eldritch' Mason | Veil combat mage backing up the cleanup crew and the Dr. Zeus assassination sniper | Veil |
| Jeff 'Heartbreaker' Lisbon | UCAS Special Forces major and Operation Backhand's team commander, killed breaching Fort Ross's perimeter | independent |
| Michael Thorndike ('Archangel Michael') | Schizophrenic Grade 3 initiate hermetic mage who genuinely believes himself the Archangel Michael, City of God's spiritual and magical leader | City of God |
| Colonel Lawrence Fenmore | Disgraced ex-UCAS officer who founded the City of God to build a magical private army out of kidnapped children | City of God |
| Elizabeth Moonstraw | T-bird rigger supplying Fort Ross, captured and interrogated by UCAS agents; killed herself and her interrogators via an anchored spell | independent |
| General Daly | UCAS general who briefs and commands Operation Backhand from the rear | independent |
| Gabriel | One of Michael's six 'Alphas' -- the oldest, most loyal, best-trained physical-adept students at Fort Ross, gathered around his throne as his personal guard | City of God |
| Raphael | One of Michael's six 'Alphas' -- a physical-adept student honed for melee, gathered around his throne as his personal guard | City of God |
| Samael | One of Michael's six 'Alphas' -- a physical-adept student built to endure punishment, gathered around his throne as his personal guard | City of God |
| Anael | One of Michael's six 'Alphas' -- a hermetic mage and sorcery adept student, gathered around his throne as his personal guard | City of God |
| Cassiel | One of Michael's six 'Alphas' -- a hermetic mage and sorcery adept student, gathered around his throne as his personal guard | City of God |
| Sachiel | One of Michael's six 'Alphas' -- a hermetic mage and sorcery adept student, gathered around his throne as his personal guard | City of God |
| Miss Onizuka | Shadowrunning decker whose Black-IC-inflicted wounds and dump shock draw Expert Team Three's Citymaster into a running Lone Star gun battle | independent |
| Casey Green | T-bird rigger for the City of God supply line, found frozen to death in his overturned panzer after being caught in the same arctic storm as the player characters | independent |
| Mr. Mo | Former UCAS military decker and friend of Colonel Fenmore who laundered the funding that built the City of God | City of God |
| Dr. Rampart | Renraku researcher whose skepticism about Cuca's new conditioning drugs is overruled and dismissed | Renraku Computer Systems |

## Locations

| Name | Type | District | Notes |
|---|---|---|---|
| Solomon Arms | hotel | Ravenna | Shabby-but-not-squalid four-story hotel where Sgt. Tanner holes up under his 'Leopard' Leonard undercover identity |
| MindSound Music | shop | Ravenna | Unremarkable music store fronting Dr. Cuca's illegal cyberclinic and, beneath it, Renraku's entire Futuremen research complex |
| Cafe do Amazonia | restaurant | Ravenna | No-frills Renraku-front cafe next door to MindSound Music, hiding a storage-room entrance down into the Futuremen complex |
| Kennedy's Cheap Electronics | shop | Ravenna | Renraku-front electronics outlet next door to MindSound Music, hiding another storage-room entrance down into the Futuremen complex |
| You Should Not Eat So Much! | restaurant | Pier 60 area | Family fast-food restaurant near Pier 60 where 'Doctor Bob' Khamdeng deliberately hires runners in plain sight |
| DocWagon Renton Clinic | hospital |  | The clinic where Liz Yamato first picks up the runners in Citymaster #264-10 and drives them to a warehouse for crash TRP training |
| DocWagon 83rd Street Clinic | hospital |  | Expert Team Three's home clinic: apartments, garage, dispatch and a helipad, for the two weeks the fake TRPs are embedded there |
| Spring Lakes Apartments (construction site) | landmark | Spring Lakes | Unfinished apartment complex where Earl Brown stages his final ambush of Expert Team Three, using a kidnapped Platinum client's son as bait |
| AresSpace Headquarters | corporate headquarters |  | AresSpace's Houston HQ, former NASA territory, where handler Benjamin Steele runs the Mars-photo investigation out of a briefing room |
| Astrotech Industries Headquarters | corporate headquarters |  | Karl Xavier's aerospace company, a rising rival to AresSpace built on stolen Cydonia data and government leverage |
| Ellington Air Force Base | military installation |  | CAS Air Force base near Houston where retired Lt. Col. James Yavin, Operation Discovery's sole surviving astronaut, lives out his retirement |
| Brook Park | landmark |  | Public Houston park where Dr. Robert Zeus insists on meeting the player characters, believing a crowd will protect him -- and where a Veil sniper kills him instead |
| Hoffman Farm (storage silo) | underground bunker | Haggard, near Wichita (Route 23, one mile south of Route 56) | Abandoned missile silo beneath a derelict farm, secretly repurposed to store every piece of physical evidence from Operation Discovery |
| Fort Ross | underground bunker | Mountain 9347, Alaska Range (Kuskokwim River valley) | Half-finished Cold War nuclear/biowarfare shelter, rediscovered and finished by Colonel Fenmore as the hidden home of the City of God |

## Organizations (new)

| Name | Type | Tier | Notes |
|---|---|---|---|
| The Futuremen | gang | 1 | Seattle 'street gang' of the future -- actually a Renraku black project turning volunteer chop-shop patients into a memory-wiped, voice-controlled cybersoldier squad |
| Veil | government agency | 5 | Off-the-books black-ops agency inside the old US, then UCAS, Department of Defense; on paper it does not exist |
| AresSpace | corporation | 4 | Ares Macrotechnology's aerospace division, built on the 2016 NASA buyout; runs its own Special Operations security teams and keeps its own decades-old secret |
| Astrotech Industries | corporation | 2 | Small but fast-growing Houston aerospace firm founded by ex-AresSpace/Veil mole Karl Xavier, increasingly poaching AresSpace's UCAS government contracts |
| MUFON (Houston Chapter) | UFO watch group | 1 | Small local Mutual UFO Network chapter framed by Karl Xavier for sabotaging AresSpace's Project Cydonia probe data -- an accusation that got several of its members killed for a crime it never committed |
| City of God | cult | 2 | Colonel Lawrence Fenmore's kidnapping ring, boarding school and fanatical private magical army, hidden inside a half-finished Cold War bio/nuclear shelter |

## Existing organizations updated (sourced appends, nothing overwritten)

- **Renraku Computer Systems** -- GM notes
- **Ares Macrotechnology** -- GM notes
- **DocWagon** -- GM notes
- **Lone Star Security** -- GM notes
- **Humanis Policlub** -- GM notes
- **Ancients** -- GM notes
- **Seattle Metroplex Guard** -- GM notes

## Matrix systems -- to build in the Matrix designer (NOT built yet)

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

## Flavor / not built

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

## GM play notes

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

