# Blood in the Boardroom -- Adventure Prep: NPCs, Locations, Organizations, Matrix Systems

Source: Shadowrun 2e - Adventure - Blood In The Boardroom {FASA7327}.pdf, pp. 2-87. Campaign order #31, in-game 2057-2060.

Everything below is loaded into the campaign DB flagged `is_active: false` and `source_adventure: "Blood in the Boardroom"` by `python scripts/adventure_ingest/run.py blood_in_the_boardroom`; flip entries active as the party meets them. Use the **Adventure** filter on the manage pages to see just this set.

## Plot synopsis

Not a shadowrun but a gamemaster's history of the corporate world tearing itself apart. **Dunkelzahn's**
assassination and his last will (9 August 2057) scatter stock and board seats into rivals' hands and
touch off two years of open corporate war. The book tracks it in four independent threads a group can
follow one at a time, jump between, or run freeform.

**Civil War / Neck and Neck**: Dunkelzahn's bequest of four million Renraku shares to Fuchi security
chief **Miles Lanier** hands him a board seat and, apparently, Fuchi's playbook -- Renraku's tech
suddenly leaps ahead. Fuchi's own triumvirate (**Richard Villiers** of the Americas, **Shikei
Nakatomi** of Asia, **Korin Yamana** of Pan-Europa) turns on itself; Villiers quietly buys back Fuchi
Americas as **Novatech, Inc.** and walks away rich while Yamana and Nakatomi bleed the rest of the
corp dry fighting over its remains. A Tokyo-Seattle semiballistic, Flight 1118, crashes into the
Redmond Barrens carrying Fuchi's Corporate Court justice **David Hague** -- Villiers is blamed, never
proven guilty. Renraku, meanwhile, owes its own meteoric rise to a secret deal with a vanished elf
decker genius, **Leonardo**; when he disappears (the same week the Court forces Lanier back to Fuchi),
Renraku's edge disappears with him, and its half-finished Seattle arcology locks itself down in
December 2059 for reasons nobody outside it can explain. Fuchi Industrial Electronics is formally
dissolved 28 July 2060, its pieces split among Novatech, Renraku (Nakatomi's faction) and Shiawase
(Yamana marries into the family and sells out what's left).

**Cross Purposes**: **Damien Knight**, who took Ares Macrotechnology in a sixty-three-second stock
raid back in 2033, still shares uneasy control with dragon-backed proxies while his old rival
**Leonard Aurelius** finally breaks and sells out -- to **Dr. Lucien Cross** of Quebec's **Cross
Applied Technologies (CATCo)**, an old Knight collaborator who has kept blackmail insurance on Knight
for thirty years. Aurelius's cash and inside knowledge, plus a shadow-ops division called the
**Seraphim**, vault CATCo to AAA status and turn Ares and CATCo's long cold war hot, with skirmishes
from Detroit to a Seattle proxy fight between Ares' **Karen King** and CATCo's paralyzed field
commander **Jezebel Surrateau**.

**Out of the East**: **Yamatetsu Corporation** abandons Japan entirely in 2059, relocating to
Vladivostok, Russia under its half-metahuman new chairman **Yuri Shibanokuji** and the free spirit
**Buttercup**, a major shareholder pushing the corp toward genuine metahuman equality. The move
becomes the rallying point for the **Pacific Prosperity Group**, a coalition of non-Japanese Pacific
Rim corporations led by **Wu Lung-Wai** of **Wuxing, Inc.**, built to break the Japanese megacorps'
regional stranglehold -- and, with Yamatetsu and Wuxing both landing Corporate Court seats, it
succeeds well enough to tip the whole Pacific balance of power.

## Timeline

- **9 Aug 2057** -- Dunkelzahn assassinated the night of his UCAS presidential inauguration.
- **13 Aug 2057** -- Miles Lanier leaves Fuchi for Renraku's board (Dunkelzahn's will: 4 million
  Renraku shares).
- **20 Aug 2057** -- Arthur Vogel accepts the presidency of Sierra, Inc.
- **22 Aug 2057** -- Nadja Daviar grants Damien Knight two years' voting control of Gavilan Ventures'
  Ares stock.
- **12 Sep 2057** -- Wu Lung-Wai announces Wuxing's expansion plans.
- **22 Feb 2058** -- Ares "Operation Extermination" (Strain III-Beta) clears the Chicago insect-spirit
  Containment Zone in under twelve hours; Ares withdraws immediately after.
- **7 Jan 2059** -- Yamatetsu chairman Tadamako Shibanokuji suffers a stroke; his stock is voted by CEO
  Saru Iwano under his living will.
- **22 Feb 2059** -- Shibanokuji dies; his stock reverts to his estranged ork son, Yuri.
- **3 May 2059** -- Yuri Shibanokuji survives an assassination attempt.
- **5 May 2059** -- Yamatetsu's board approves relocating its headquarters to Vladivostok, Russia.
- **16 May 2059** -- Dosan Aburakoji, a Mitsuhama Corporate Court justice, commits suicide in Kyoto.
- **6 Jun 2059** -- Fuchi sues Renraku over Lanier's inside knowledge; charges dropped within 24 hours.
  Lanier leaves Renraku, selling his stock to the Zurich-Orbital Gemeinschaft Bank.
- **16 Jun 2059** -- Navroz Chandaria of Renraku Asia takes the Corporate Court seat left by Aburakoji.
- **8 Jul 2059** -- The Pacific Prosperity Group officially forms.
- **11 Jul 2059** -- Flight 1118 (Tokyo-Seattle) crashes in the Redmond Barrens on the Salish-Shidhe
  border; ~200 dead. Corporate Court justice David Hague was aboard.
- **19 Jul 2059** -- Hague's body found in an abandoned Redmond apartment building, a week after the
  crash.
- **15 Aug 2059** -- Li Feng of Wuxing named to Hague's vacant Court seat, making Wuxing an AAA
  megacorp.
- **22 Aug 2059** -- Nadja Daviar's Gavilan Ventures proxy over Ares reverts to her.
- **29 Sep 2059** -- "White Monday": the Tokyo Stock Exchange's worst single-day drop in 70 years.
- **6 Oct 2059** -- Richard Villiers announces Novatech, Inc.; Miles Lanier becomes its security
  director.
- **20 Oct 2059** -- Leonard Aurelius sells his Ares stock to Arthur Vogel and steps down from Sierra,
  Inc. (replaced by Gary Grey).
- **27 Oct 2059** -- Aurelius joins Cross Applied Technologies' board.
- **19 Dec 2059** -- The Renraku Seattle arcology closes to visitors indefinitely.
- **3 Feb 2060** -- Renraku CEO Inazo Aneki begins an indefinite leave of absence; COO Haruhiko Nakada
  becomes acting CEO.
- **19 Mar 2060** -- An unexplained ten-minute virus attack hits Seattle's Matrix RTG.
- **20 Mar 2060** -- Navroz Chandaria dies in a New Delhi bombing; the Court seat goes to Cross Applied
  Technologies (Yves Aquillon), not Renraku.
- **5 Apr 2060** -- Shikei Nakatomi buys the same 4 million Renraku shares back from the Zurich-Orbital
  bank; Renraku begins absorbing Fuchi Asia.
- **8 Jun 2060** -- Korin Yamana announces his marriage to Mitsuko Shiawase.
- **14 Jun 2060** -- Shiawase Corporation buys the remainder of Fuchi Industrial Electronics; Yamana
  joins Shiawase's board.
- **28 Jul 2060** -- Fuchi Industrial Electronics is officially dissolved.

## NPCs (Persons of Interest)

| Name | Role | Org |
|---|---|---|
| Richard Villiers | President/CEO of Novatech, Inc. -- the corporate shark who rebuilt a third of Fuchi as his own AAA megacorp | independent |
| Miles Lanier | Novatech's director of security -- Fuchi's former security chief, briefly a Renraku board member, whose true loyalties nobody can prove either way | independent |
| Samantha Villiers | VP of Novatech Northwest -- Richard Villiers' ex-wife, who held the tiebreaking stock that decided Fuchi's fate | independent |
| Darren Villiers | Novatech Seattle's director of special assets -- Richard Villiers' dwarf brother and a former deniable covert operative | independent |
| Sadato Shiawase | Chairman of Shiawase's board and head of the Shiawase family -- publicly compassionate, privately locked in a decades-long feud with his own sister | Shiawase Corporation |
| Tadashi Shiawase | Shiawase's president and CEO in name -- his father Sadato still holds the real power | Shiawase Corporation |
| Korin Yamana | Ex-head of Fuchi Pan-Europa, who achieved his forty-year goal of controlling Fuchi only to sell what was left of it to Shiawase and marry into the family | Shiawase Corporation |
| Mitsuko Shiawase-Yamana | VP of Shiawase Envirotech's Philippines division -- married Korin Yamana as pure economic expediency, on both sides | Shiawase Corporation |
| Inazo Aneki | Renraku's President/CEO for decades -- the corporate raider turned devoted patriarch who took an indefinite leave just as Renraku's fortunes turned | Renraku Computer Systems |
| Yukiako Watanabe | Renraku's chairman of the board -- ruthless, devoted, and deeply suspicious that Miles Lanier is still Fuchi's man | Renraku Computer Systems |
| Haruhiko Nakada | Renraku's COO and acting CEO during Aneki's leave -- cheerful in public, ruthless underneath, and quietly hoping the leave never ends | Renraku Computer Systems |
| Dr. Sherman Huang | Renraku America's division manager and the Seattle arcology's executive director -- devastated by its December 2059 shutdown, still hunting the cause | Renraku Computer Systems |
| Shikei Nakatomi | Ex-head of Fuchi Asia turned Renraku board member -- the 'Business Butcher', now hunting Richard Villiers with Renraku's resources behind him | Renraku Computer Systems |
| Liam Riley | President/CEO of Transys Neuronet -- an HKB-appointed board member maneuvered into the top job, doing surprisingly well so far | Transys Neuronet |
| Karen King | Ares Seattle's supervising VP -- a ruthless climber taking bigger risks locally to catch Damien Knight's eye, currently losing a proxy war with CATCo's Seattle Seraphim | Ares Macrotechnology |
| Lucien Cross | President/CEO of Cross Applied Technologies -- Damien Knight's old programming partner, who has kept blackmail insurance on him for thirty years | Cross Applied Technologies, Inc. |
| Leonard Aurelius | Cross Applied Technologies board member -- Ares' founder's son, who finally broke free of his father's shadow by selling out to Knight's oldest enemy | Cross Applied Technologies, Inc. |
| Bernard Cross | Nominal head of Cross Advanced Electronics in Seattle -- Lucien Cross's nephew, too fear-paralyzed by one near-catastrophe to actually run it | Cross Applied Technologies, Inc. |
| Jezebel Surrateau | Seattle commander of the Seraphim, Cross Applied Technologies' elite intelligence arm -- paralyzed since taking a bullet for Lucien Cross, and running Cross Advanced Electronics in all but title | Cross Applied Technologies, Inc. |
| Buttercup | Free spirit and major Yamatetsu shareholder -- once played humanity for pets, now the driving force behind Yamatetsu's flight from Japan and its embrace of metahuman equality | independent |
| Yuri Shibanokuji | Yamatetsu's chairman -- an ork who inherited his estranged father's shares and, with Buttercup's backing, dragged the corporation out of Japan entirely | Yamatetsu Corporation |
| Saru Iwano | Yamatetsu's CEO -- voted Tadamako Shibanokuji's stock during his incapacitation, and used it to entrench the corp's anti-metahuman faction | Yamatetsu Corporation |
| Jacques Barnard | Executive VP of Yamatetsu North America -- a mistrustful hermetic mage with a personal grudge against Buttercup and a shadow network of his own | Yamatetsu Corporation |
| Mary Luce | Head of Yamatetsu Seattle -- Barnard's successor, and one of the most effective shadow-asset handlers in the sprawl | Yamatetsu Corporation |
| Wu Lung-Wai | President/CEO of Wuxing, Inc. -- 'Hong Kong's Kingmaker', who finished his father's decades-long dream of a united Pacific Rim front against the Japanese megacorps | Wuxing, Inc. |
| Sun Runming | Head of Wuxing's new Seattle division -- plays the oblivious hedonist to be underestimated, and rarely misses the moment to prove it a mistake | Wuxing, Inc. |
| Izu Cheng | Chairman of the Pacific Prosperity Group -- a gregarious Wuxing negotiator balancing giants and minnows alike to everyone's apparent satisfaction | Pacific Prosperity Group |
| Se-jong Lee | President/CEO of Eastern Tiger Corporation -- shrewd but cautious, giving the Pacific Prosperity Group little more than lip service | Eastern Tiger Corporation |
| Jessica Sirianni | President/CEO of Federated Boeing -- self-made from an Auburn childhood watching Fed-Boeing's planes overhead, now petitioning to join the Pacific Prosperity Group out of spite for Mitsuhama | Federated Boeing |
| Jae-Myung Kim | President of Kwonsham Industries -- building a multinational he can hand to his son, one Seattle trip at a time | Kwonsham Industries |
| Toshio Mitsukuri | President/COO of Monobe International -- pulled off a boardroom coup, and his ousted predecessor's plane vanished shortly after | Monobe International |
| Sau-hok Chu | President/CEO of Tan Tien, Inc. -- enigmatic, reclusive, and respected enough that other Chinese corporations follow wherever he aligns | Tan Tien, Inc. |
| Hiroshi Yakashima | President/CEO of Yakashima Technologies -- Japan's self-styled 'hostile-takeover king', freshly emboldened by Yamatetsu's exit | Yakashima Technologies |
| Jean-Claude Priault | Saeder-Krupp's Zurich-Orbital liaison -- the man Lofwyr trusts to phone in bad news, and the Prologue's viewpoint character | Saeder-Krupp Heavy Industries |
| Lofwyr | Great Western Dragon, CEO of Saeder-Krupp Heavy Industries -- opens the book manipulating a Corporate Court vote from Earth orbit and closes Track 2 erasing evidence of Leonardo's Iran hideout | independent |
| David Hague | Fuchi's Corporate Court justice, a Yamana loyalist -- died in the Flight 1118 crash that conveniently silenced him, and stayed missing for a week afterward | independent |
| Leonardo | Vanished elf decker genius whose secret deal briefly made Renraku's Matrix technology untouchable -- his disappearance is the mystery both Track 2 and a great dragon chase across two continents | independent |
| Diana Peng | Renraku's undercover agent inside the Beamwalkers otaku tribe -- came back from the Matrix's 'Deep Resonance' with her mind in ruins and an obsessive need to touch a cyberdeck | Renraku Computer Systems |
| HAL | Freelance decker who ran afoul of Fuchi's prototype truth-serum black IC -- now compulsively confessing every secret he has ever kept, including everyone else's | independent |
| Craig Sanchez | Alcoholic ork who unknowingly knows Buttercup's true name -- the one loose end from her humbling by Dunkelzahn that she still needs tied off | independent |
| Caldwell | Arrogant Yamatetsu mage sent to grab Craig Sanchez for Jacques Barnard -- and who decides, on learning why Sanchez matters, to double-cross his own boss and bind Buttercup for himself | Yamatetsu Corporation |
| Eve Aurelius ('Eve Night') | Leonard Aurelius's rebellious daughter, lead guitarist for the Unholy Machine -- stole Damien Knight's Dunkelzahn-bequeathed chess piece to spite her father and use as a pretext to date Knight | independent |
| Two-Chord Teddy | Detroit Nightmares urban brawl player and Eve Aurelius's boyfriend -- unwittingly carries the real stolen chess piece in his coat pocket | independent |
| Raymond Briggs | VP of Ares Seattle's Consumer Electronics division -- extracted from Ares by Cross Applied Technologies at the same moment his own father defects in Detroit | Ares Macrotechnology |
| William Briggs | Executive VP of Ares Global Entertainment, defecting to Cross Applied Technologies alongside Leonard Aurelius -- and pulling his son out first | Ares Macrotechnology |
| Sebastien Hull | Quebec City's chief of police -- a staunch Cross Applied Technologies supporter whose testimony could sink Damien Knight's zoning bid, if he reaches the council meeting in time | independent |
| Dieter Arkona | Rich elf holdout shareholder standing between Renraku and control of the German water-tech firm Wasserkraft -- has told both Fuchi and Renraku to frag off | independent |
| Dimitri Makaroff | Tacoma's Vary v Zakone boss -- hunting proof of a yakuza schism to blackmail his way into part of the Watada-rengo's Tacoma rackets | Vary v Zakone |
| Enric Wong | Owner of Seattle's Lee Chee Garden restaurant -- long rumored to consult an 'ancient Chinese ghost' who is really Tan Tien's CEO, astrally projecting in from Beijing | independent |
| David Gao | Octagon Triad leader worried his own men are dying for breaking their initiation oaths -- and unwittingly stumbling toward an Atlantean Foundation trap | independent |
| Chao Su-Cheng | Wuxing geomancer overseeing the renovation of its new Seattle offices -- and, quietly, a Triad member in contact with an Octagon Triad wizard | Wuxing, Inc. |
| Wu Kuan-Lai | Wuxing's founder -- helped force Hong Kong's independence from China, then spent decades chasing a united Pacific Rim front against the Japanese megacorps he never lived to see | independent |
| Tadamako Shibanokuji | Yamatetsu's chairman until his 2059 death -- a man whose secret goblinized son and buried guilt over abandoning him set Yamatetsu's flight from Japan in motion | Yamatetsu Corporation |
| Goliath | Seraphim bodyguard sent along on the Raymond Briggs extraction to keep him safe and keep Seattle and Detroit events in sync | Cross Applied Technologies, Inc. |
| Kiyoshi Nakatomi | Fuchi's murdered co-founder -- vetoed Richard Villiers' original cyberdeck-technology deal and was dead within three days | independent |
| Nicholas Aurelius | Ares Macrotechnology's founder -- built a corporate empire on the ruins of the U.S. space program and cast a shadow his son Leonard never fully escaped | independent |

## Locations

| Name | Type | District | Notes |
|---|---|---|---|
| Zurich-Orbital | orbital platform | Seat of the Corporate Court | The Corporate Court's orbital seat -- Ares' old space platform, sold to Fuchi and renamed, now run by the Zurich-Orbital Gemeinschaft Bank |
| Flight 1118 Crash Site | ruins | Redmond Barrens, near the Salish-Shidhe border | Where a Tokyo-Seattle semiballistic overshot Sea-Tac and plowed into the Barrens on 11 July 2059, killing roughly 200 -- and where Fuchi justice David Hague's body vanished for a week |
| Stasky Institute | hospital | Small medical park near Doctor's Hospital of Tacoma | Small private neurological clinic where a brain-damaged Renraku undercover agent was hidden under a false name |
| Villa Plaza | mall | Seattle | Shopping mall, home to a Hardware Etcetera cyberdeck storefront, where an extraction handoff was ambushed by the otaku tribe that had bugged the victim |
| City Center Building | corporate headquarters | Downtown Seattle, seven blocks from Pier 27 | Yamatetsu Seattle's headquarters -- the false destination in a Wuxing shell game over two crates of decommissioned mainframes |
| Cross Advanced Electronics | corporate facility | Seattle | CATCo's Seattle-facing division -- nominally run by Lucien Cross's overwhelmed nephew, actually run by his Seraphim field commander |
| Ares Bellevue Offices | corporate facility | Beaux Arts, Bellevue | Ares Seattle's office tower, linked by high-speed monorail to an exclusive executive housing district -- site of a defection extraction gone loud |
| Haukshorn Towers | corporate headquarters | Green Lake, Seattle | Former Haukshorn Chemicals headquarters, divided into rented office space -- soon to become Wuxing's new Seattle headquarters after a mainframe shell game |
| Lee Chee Garden | restaurant | Seattle | Enric Wong's soundproof-back-room restaurant, trusted neutral ground for shadowy and corporate meetings alike -- and secretly wired for Tan Tien's benefit |

## Organizations (new)

| Name | Type | Tier | Notes |
|---|---|---|---|
| Novatech, Inc. | corporation | 5 | Richard Villiers' new AAA megacorp -- Fuchi Americas rebuilt as his own, from Matrix hardware to a small orbital division |
| Cross Applied Technologies, Inc. | corporation | 5 | Dr. Lucien Cross's Matrix-and-bioware AAA megacorp; a 30-year cold war with Ares Macrotechnology just went hot |
| Sierra, Inc. | environmental organization | 2 | Old-line mainstream environmentalist group -- petitions and lawsuits, not eco-tage -- whose president sits on Ares Macrotechnology's board |
| Wuxing, Inc. | corporation | 5 | Wu Lung-Wai's Dunkelzahn-boosted AAA megacorp, the driving force and figurehead of the Pacific Prosperity Group |
| Pacific Prosperity Group | corporate alliance | 4 | Coalition of non-Japanese Pacific Rim corporations built to break the Japanese megacorps' regional dominance -- founded 8 July 2059, already a real power |
| Eastern Tiger Corporation | corporation | 3 | Unified Korea's largest single corporation -- petrochemicals and heavy manufacturing, nominal Pacific Prosperity Group member |
| Federated Boeing | corporation | 3 | UCAS aerospace major petitioning to join the Pacific Prosperity Group, apparently to spite Mitsuhama's repeated takeover attempts |
| Kwonsham Industries | corporation | 2 | United Korea industrial/electronics/agricultural conglomerate, formed from a dozen orphaned North Korean firms after reunification |
| Monobe International | corporation | 4 | AA megacorp with first-tier ambitions under a new, ruthless COO-turned-president who may have had his predecessor's plane vanish over the ocean |
| Pacific Rim Bank and Financial Services Corporation | corporation | 4 | The Pacific's largest bank, walking a shrinking neutral line between the Japanese megacorps and the Pacific Prosperity Group |
| Tan Tien, Inc. | corporation | 3 | Small but fiercely independent Chinese research corp -- leads in cyberdeck design and neural interfaces, aligned with the Pacific Prosperity Group |
| Yakashima Technologies | corporation | 3 | Japan's self-styled 'hostile-takeover king', back on the prowl now that its main rival Yamatetsu has fled the country |
| HyperSense | corporation (simsense production) | 2 | Small, unusual-recording-technique simsense studio, 51 percent owned by Renraku as a quiet tech-spinoff testbed; its own owner is trying to fake its death |
| The Beamwalkers | otaku tribe | 1 | Reclusive, technically savvy young urban tribe with strong otaku ties, several of whom trained as deckers before joining -- and who tagged Renraku's own infiltrator |
| Quick Trigger Systems | corporation (IC software) | 2 | Detroit IC-software developer secretly controlled by Damien Knight, petitioning to relocate into Quebec's Empowerment Zone right under Cross Applied Technologies' nose |
| Reactive Meditech | corporation (biotech) | 2 | Third-tier biotech corp targeted for a Cross Applied Technologies takeover; issued bearer bonds to raise defense capital, then lost track of who was quietly buying them all up |
| Leviathan Technical | corporation (cyberware) | 2 | Ares-owned Silicon Valley cyberware division whose irresponsible toxic-waste dumping has drawn Terra First! and a Fuchi data-theft both |
| Wasserkraft | corporation (water technology) | 1 | German water-pollution and purification research firm -- part magic, part technology -- caught in a Renraku takeover fight after Fuchi's collapse |
| Vary v Zakone | organized crime (Russian mob) | 2 | Tacoma's Russian mob, grown larger and bolder as Yamatetsu's relocation deepens trade -- legal and illegal -- between Tacoma and Vladivostok |
| Shotozumi-rengo | yakuza clan | 1 | Breakaway yakuza league founded when oyabun Hanzo Shotozumi finally split from the Watada-rengo, ending a Russian mob blackmail attempt but making new enemies |

## Existing organizations updated (sourced appends, nothing overwritten)

- **Transys Neuronet** -- GM notes; leadership: Liam Riley; enemies: Renraku Computer Systems
- **Ares Macrotechnology** -- GM notes; leadership: Damien Knight, Arthur Vogel, Karen King; enemies: Cross Applied Technologies, Inc.
- **Aztechnology** -- GM notes
- **Fuchi Industrial Electronics** -- GM notes; leadership: Richard Villiers, Korin Yamana, Shikei Nakatomi, Miles Lanier
- **Mitsuhama Computer Technologies** -- GM notes
- **Renraku Computer Systems** -- GM notes; leadership: Inazo Aneki, Yukiako Watanabe, Haruhiko Nakada, Dr. Sherman Huang, Shikei Nakatomi
- **Saeder-Krupp Heavy Industries** -- GM notes
- **Shiawase Corporation** -- GM notes; leadership: Sadato Shiawase, Tadashi Shiawase, Korin Yamana, Mitsuko Shiawase-Yamana
- **Yamatetsu Corporation** -- GM notes; leadership: Buttercup, Yuri Shibanokuji, Saru Iwano, Jacques Barnard, Mary Luce
- **DocWagon** -- GM notes
- **Knight Errant Security Services** -- GM notes
- **Lone Star Security** -- GM notes
- **Pueblo Corporate Council** -- GM notes
- **Salish-Shidhe Council** -- GM notes

## Existing locations / NPCs updated

- location: **The Barrens (Seattle)**
- NPC: **Damien Knight**
- NPC: **Arthur Vogel**
- NPC: **Nadja Daviar**
- NPC: **Gary Grey**
- NPC: **Hanzo Shotozumi**

## Matrix systems -- to build in the Matrix designer (NOT built yet)

Blood in the Boardroom is a background sourcebook, not a scripted run, and gives no node-by-node host
ratings anywhere in its 88 pages -- every Matrix system in it is handled narratively. GMs building any
of the following for their own table are working from a blank page, not book stats:

- **A Fuchi Asia host in San Francisco** carries the prototype psychotropic black IC "Stoolie" (removes
  the victim's ability to keep secrets) and, elsewhere in the same system, its own counter-program,
  trapped behind trace IC (Loose Lips Fry Chips, PLAY_NOTES).
- **A powered-down Fuchi host**, mid-transfer to Novatech, secretly holds a dormant Fuchi "corp war
  weapon" -- a Semi-Autonomous Knowbot (SK) -- that a rogue Aztechnology decker is trying to retarget
  after finding it (Public Secrets, NOT_BUILT).
- **HyperSense's Matrix host** hides an undisclosed real simsense-tech breakthrough behind heavy
  encryption (This Hurts Me More Than It Hurts You, PLAY_NOTES).
- **A teleporting SAN** (virtual bank) used to launder the money behind Arthur Vogel's Ares stock
  purchase, physically traced to a gutted, abandoned Santa Fe office building (Virtual Funds,
  NOT_BUILT).
- **Tan Tien's "Parallel Thought"** -- a multi-user cyberdecking interface, still in prototype, expected
  to be licensed only to Pacific Prosperity Group members once finished (see Tan Tien, Inc., ORGS).

## Flavor / not built

- **Dunkelzahn** -- the assassinated dragon president whose will triggers the whole war never appears
  on-page alive in this book's present, has no current place, and is treated as a name-drop by every
  other spec in this campaign that mentions him; left as backstory on the many rows his will touches
  rather than built as an NPC.
- Corporate Court justices named only in passing, seat-shuffles recorded in TIMELINE and on the
  affected orgs' notes rather than built as characters: **Li Feng** (Wuxing), **Navroz Chandaria**
  (Renraku), **Yves Aquillon** (Cross Applied Technologies), **Dosan Aburakoji** (Mitsuhama), **Anna
  Villalobos** and **Dominga Chavez** (Aztechnology), **Neil Benson** and **Francesco Napoli**
  (Renraku), **Lynn Osborne** (Novatech).
- **Sakehisa Tajika** (Ares' mid-century chairman, protege of Nicholas Aurelius), **Ken Roper and
  Michael Eld** (Matrix Systems' murdered founders whose Portal cyberdeck built Villiers' fortune),
  **Soka Shiawase** (Sadato's feuding sister), **Hitomi Shiawase** (Tadashi's reckless teenage
  daughter), **Newton Chin and his sister Sophia** (Yamatetsu reform-faction allies), **Hideo Yoshida**
  (Yamatetsu's conservative former chairman), **Tatiana Trigorin** (Yuri Shibanokuji's mother) --
  single-paragraph backstory folded onto the rows they connect to rather than built separately.
- **"Stuart Peng"** and the real, oblivious **Stuart Peng** (This Is Your Brain on Otaku) -- both exist
  only as the false and true identity behind the Fuchi cover story that hires the runners after Diana
  Peng; neither has independent material beyond that single beat.
- **Phaze** and the Matrix bar **Rox Roots** (Prove It to Me, Boston) -- a decker cutout and a venue
  that exist for one meet apiece, out of this campaign's Seattle focus, with nothing to reuse.
- **Breeze**, the great dragon **Hestaby**, **Ehran the Scribe**, **the Tir Ghosts**, the Renraku
  courier **Kineda**, and **the ruined Altyar research observatory in Iran** (What Does a
  Ten-Thousand-Year-Old Dragon Get?) -- a one-shot chase for Leonardo's trail spanning Iran and the Tir
  Tairngire border; Leonardo himself is built (NPCS), the supporting cast and the Iranian site are not.
- **Terra First!'s Silicon Valley investigators** (Green Piece, part OCR-garbled) and **Reactive
  Meditech's bank vault heist target** beyond Jeff Hansen (Return Policy, badly OCR-garbled) -- unnamed
  or too fragmentary to build past the org rows already covering them.
- The untitled adventure idea between Return Policy and Green Piece (p.66-67, its own name lost to OCR
  damage) -- a middleman selling devil rats experimented on with Ares' Strain-III bacteria, with a
  possible tie to the existing Alamos 20,000 org and Strain-III outbreaks across the city; too
  fragmentary in the scan to build with confidence.
- **The Atlantean Foundation's Mystic Crusaders** and Octagon Incense Master **Chen Kwan-Ti** (Tome
  Raiders) -- an unnamed elf strike team and a name-dropped rival wizard, texture on David Gao's and
  Chao Su-Cheng's rows.
- News-handout and Shadowland-BBS texture with no place in the campaign proper: **Nadja Daviar's
  mystery dinner date**, the **Renraku Seattle arcology "security malfunction"** that killed nine
  shoppers before the December 2059 lockdown, **Carlos Consuni** and the **Philippines election
  scandal**, the dragon **Masaru**, **Filipa Salonga** -- flavor only, folded into the relevant org
  notes.
- **Michael Lane** (the Yamatetsu executive who hires the runners in What's in a Name?) and **Enda
  Iyoji** (Pacific Rim Bank president) -- named once each with no material beyond a hiring line or a
  title; noted on the Yamatetsu Corporation and Pacific Rim Bank and Financial Services Corporation
  rows rather than built separately.

## GM play notes

- This is a two-year gamemastering toolkit, not a plotted adventure -- the book itself offers five
  structures (One-Track Mind, Jumping the Tracks, Freeform, Novel, and picking a track as background
  texture) and explicitly has no fixed ending; "the overt fighting may end, but the covert fighting has
  just begun." Pick the structure that fits the table before touching any framework below.
- The four tracks run in parallel and can be entered through a corporate Mr. Johnson job, a contact
  caught up in events, security or bodyguard work for a player in the war, or personal stakes -- see
  Hooking the Characters (p.11) for the book's own menu of approaches, including alternate DocWagon,
  media, law-enforcement, magical and gang campaign framings.
- Track 1/2 (Fuchi's collapse and Renraku's rise and stumble) is the Seattle-heaviest material: the
  Flight 1118 crash (Crash Team), the Renraku arcology lockdown, and Villiers' Novatech Seattle office
  are all local hooks. Track 3 (Ares vs. Cross Applied Technologies) runs mostly Detroit/Montreal but
  has a real Seattle front in the Ares Seattle/Cross Advanced Electronics rivalry. Track 4 (Yamatetsu/
  Pacific Prosperity Group) is the least Seattle-centered but supplies Wuxing's and Yamatetsu's new
  Seattle offices as fresh corporate presences to plug into an existing campaign.
- Crash Team (Track 1): runners hired to intercept Fuchi justice David Hague off his Tokyo flight find
  themselves instead fighting fake "DocWagon" Renraku operatives for his body and briefcase at the
  Flight 1118 wreck, then chasing them to an abandoned Redmond apartment building -- a fast, chaotic
  disaster-zone run with a genuine alternate DocWagon-campaign writeup.
- Loose Lips Fry Chips (Track 1): a decker contact hit by Fuchi Asia's prototype "Stoolie" black IC
  starts publicly confessing every run he's ever pulled, himself included -- all three Fuchi factions
  and everyone he's ever burned want him, in that order of urgency.
- Black Operations (Track 1): Fuchi's Yamana faction hires runners and a mercenary unit to seize one of
  Fuchi's secret "delta clinics," hidden inside Pueblo Corporate Council territory, from its
  Villiers-loyal staff -- complicated by a British vampire (Ordo Maximus) sabotaging the takeover.
- This Is Your Brain on Otaku, Prove It to Me, What Does a Ten-Thousand-Year-Old Dragon Get?, This
  Hurts Me More Than It Hurts You (Track 2): Renraku's own internal messes -- a burned-out otaku
  infiltrator, a loyalty test on Miles Lanier that never resolves, the hunt for the vanished decker
  genius Leonardo (with a great dragon and Tir Ghosts both in the chase), and a division owner faking a
  hit on his own company. None resolve neatly; use them as ongoing Renraku texture as much as one-shots.
- Double Crossover, Not in My Backyard, Knight's Gambit (Track 3): a defection extraction gone loud at
  Ares Bellevue with a Novatech snatch-and-grab on top; a false-flag Detroit bombing meant to frame
  Cross Applied Technologies, followed by a race to keep a Quebec police chief from a zoning vote;
  Dunkelzahn's bequeathed chess set turning into a three-way chase after Leonard Aurelius's rebellious
  daughter runs off with the missing king piece to bait Damien Knight into a date.
- The Needle and the Damage Done, Mainframed, What's in a Name? (Track 4): a Yamatetsu nurse framed for
  Tadamako Shibanokuji's murder (which Buttercup, unknown to everyone else, actually arranged); a
  three-way shell game over two crates of decommissioned mainframes staged by a Wuxing executive
  testing rival runner teams; a hunt for the one man who knows Buttercup's true name, cut short by a
  rival mage trying to bind her himself.
- Shorter Track 1/2 "adventure ideas" worth running standalone: Unwilling Transfer (a Fuchi Asia marine
  biologist kidnapped for Renraku's Underwater Living Project bolts to the rebel-pirate Huk Network the
  moment he's unguarded); The Squeeze (leaning on Wasserkraft holdout shareholder Dieter Arkona for
  Renraku, with a German policlub and North Sea pirates backing him up); Public Secrets (a rogue
  Aztechnology decker retargeting a dormant Fuchi "corp war weapon" knowbot found in a powered-down
  host); Transys Neuromess (forged Fuchi Asia credentials for a smash-and-grab that turns into a
  Renraku "rescue"-turned-abduction).
- Shorter Track 3 ideas: Look Before You Leap (a zero-g, no-magic, unarmed heist aboard Ares' Daedalus
  orbital platform for Leonard Aurelius's own research data); Return Policy and the untitled fragment
  after it, and Green Piece (Reactive Meditech bearer bonds, an Ares/devil-rat/Strain-III smuggling
  hint, and Leviathan Technical's toxic dumping -- see NOT_BUILT for what the OCR damage cost); Virtual
  Funds (tracing Arthur Vogel's mystery Ares-stock money to a gutted Santa Fe shell office, with Pueblo
  Security Force trouble along the way).
- Shorter Track 4 ideas: Ancient Chinese Secret, Huh? (Enric Wong's astrally-projecting "ghost" is
  really Tan Tien's own CEO); Truck Stop (a Mitsuhama-seeded rumor of milspec guns turns every Puyallup
  gang on Eastern Tiger's trucks); Mob Clash (Vary v Zakone vs. the Watada-rengo's Hanzo Shotozumi, who
  splits off as his own Shotozumi-rengo); Tome Raiders (Octagon Triad members used and killed by
  Atlantean Foundation Mystic Crusaders to lure Wuxing geomancer Chao Su-Cheng into a trap).
- Corporate Court mechanics matter to this campaign: its justices sit two per corp for the biggest
  players, meet aboard Zurich-Orbital, and can rule on inter-corp disputes (as it did against Renraku
  over Miles Lanier) -- a useful lever for GMs who want the war's stakes to feel adjudicated rather
  than purely won by force.
- Karma and reward guidance is left to the gamemaster throughout (no fixed award tables); Blood in the
  Boardroom is meant to seed an extended, GM-paced campaign rather than resolve in one sitting.

