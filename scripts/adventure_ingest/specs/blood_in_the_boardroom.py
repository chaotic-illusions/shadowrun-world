# Blood in the Boardroom (FASA 7327, 1999) -- campaign order #32. This book is not a scripted
# adventure: it is a two-year gamemaster sourcebook charting the AAA-megacorp "corp war" that follows
# Dunkelzahn's will (9 Aug 2057) through Fuchi's dissolution (28 Jul 2060), organized into four
# independent TRACKS (Civil War/Fuchi, Neck and Neck/Renraku, Cross Purposes/Ares vs Cross Applied
# Technologies, Out of the East/Yamatetsu). Each track is fiction-intro + history + player profiles +
# "adventure frameworks" (outlines, not stat-blocked runs) + one-line "adventure ideas". YEAR is given
# as a range because the book itself has no single present-day date; its own frame device (the
# Prologue, Priault's call to Lofwyr) is dated 15 August 2059, roughly the timeline's midpoint, and the
# Corporate War Timeline (p.19) runs 9 Aug 2057 to 28 Jul 2060. TIMELINE below reproduces that master
# timeline. Per the adventure-ingest rules, the many one-off "adventure framework"/"adventure idea"
# hooks are not built as scripted runs; they are summarized in SYNOPSIS/PLAY_NOTES, but this being a
# sourcebook whose entire point is its cast of named corporate players, named single-scene people and
# places are built as short real rows rather than swept into NOT_BUILT -- only Dunkelzahn (no current
# place, no scene of his own; treated as a name-drop by every other spec in this campaign) and a
# handful of genuinely unnamed or single-line figures stay there. This book gives few direct quotes
# (it is exposition-driven, not a scripted linear adventure like most others in this campaign) --
# quoted lines below are the book's own where it has them.
# A short adventure idea between "Return Policy" and "Green Piece" (Track 3, p.66-67) is badly enough
# garbled in the OCR scan that its own title is lost; from context it involves a middleman selling
# devil rats experimented on with Ares' Strain-III bacteria, a possible Alamos 20,000 tie, and an
# ambush at the exchange -- paraphrased here from what survives, not built as its own row. The
# "Not in My Backyard" framework (Track 3) gives the QTS zoning-vote deadline as both "10:15 a.m." and
# "before 11 a.m." in the same framework -- the book's own inconsistency, left as found. Bernard Cross's
# recall to Montreal (Track 3, "Double Crossover" sequel) is dated 2061, a year past the book's own
# stated 2057-2060 window -- also left as the book states it.
# Source text: docs/Adventures/text/Shadowrun 2e - Adventure - Blood In The Boardroom {FASA7327}.txt
# (88 pages). ASCII only (pre-commit hook).

ADVENTURE = "Blood in the Boardroom"
ORDER = 31
SOURCE = "Shadowrun 2e - Adventure - Blood In The Boardroom {FASA7327}.pdf, pp. 2-87"
YEAR = "2057-2060"

SYNOPSIS = """
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
"""

TIMELINE = """
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
"""

ORGS = [
    {
        "name": "Novatech, Inc.",
        "org_type": "corporation",
        "tier": 5,
        "headquarters": "Boston, Massachusetts, UCAS",
        "summary": "Richard Villiers' new AAA megacorp -- Fuchi Americas rebuilt as his own, from Matrix hardware to a small orbital division",
        "description": (
            "Formed 6 October 2059 from the merger of Villiers International and Cambridge Holdings, "
            "Novatech is what remained of Fuchi's American operations, quietly bought back piece by "
            "piece under Villiers' own name. Its greatest strength is Matrix hardware and software -- "
            "many of Fuchi's best programmers followed Villiers over -- alongside the ex-Fuchi Orbital "
            "Division (combined with Boston's Walker Aerodesign), military and security interests, and "
            "a growing magical research division. The starburst logo is widely read as a deliberate "
            "riff on Fuchi's old star emblem. Renraku is its biggest rival, personally and "
            "professionally; Ares Macrotechnology is watching and waiting."
        ),
        "leadership": [
            {"name": "Richard Villiers", "title": "President/CEO", "notes": "Built Novatech out of Fuchi's collapse; widely (never provably) believed to have arranged Kiyoshi Nakatomi's 2035 death."},
            {"name": "Miles Lanier", "title": "Director of Security", "notes": "Ex-Fuchi security chief, ex-Renraku board member; purges Yamana/Nakatomi loyalists from absorbed Fuchi divisions."},
            {"name": "Samantha Villiers", "title": "Vice President, Novatech Northwest", "notes": "Richard's ex-wife; held the tiebreaking 2 percent of post-split Fuchi stock, sold to Korin Yamana in Jan 2060 for a one-year Novatech-Fuchi truce."},
            {"name": "Darren Villiers", "title": "Director of Special Assets, Seattle", "notes": "Richard's dwarf younger brother, a Grade 3 magical initiate and physical adept; runs deniable blackmail/burglary operations, hires runner teams."},
            {"name": "Lucas Don", "title": "Senior Vice President", "notes": "Former managing director of Cambridge Holdings, brought in with the merger."},
        ],
        "notes": (
            "Secretly bankrolled by Villiers himself (via a shell, Silveril Investments) to hostile-"
            "takeover some 22 Fuchi Americas subsidiaries before Villiers folded Cambridge Holdings, and "
            "with it those subsidiaries, into his own empire directly. Novatech Seattle sends agents "
            "hunting talented defectors from rival corps (see Cross Applied Technologies, Double "
            "Crossover)."
        ),
        "enemies": ["Renraku Computer Systems"],
    },
    {
        "name": "Cross Applied Technologies, Inc.",
        "org_type": "corporation",
        "tier": 5,
        "headquarters": "Montreal, Quebec",
        "summary": "Dr. Lucien Cross's Matrix-and-bioware AAA megacorp; a 30-year cold war with Ares Macrotechnology just went hot",
        "description": (
            "Founded on the proceeds of Damien Knight's 2033 Nanosecond Buyout -- Cross was Knight's "
            "programmer on that scheme, took payment instead of stock, and kept records proving Knight "
            "is the elusive 'David Gavilan' as insurance. Built from small Matrix hardware/software "
            "startups (Cross Matrix Technologies) into cyberware, bioware, consumer electronics and "
            "entertainment; Quebec's stiff anti-competition tariffs give it an effectively captive home "
            "market. Its Seraphim intelligence division -- equal parts corporate espionage, dirty tricks "
            "and political infiltration -- fights Ares to a standstill in the shadows. Cross Advanced "
            "Electronics is its Seattle-facing division."
        ),
        "leadership": [
            {"name": "Lucien Cross", "title": "President/CEO", "notes": "Nearing 70, still hands-on; nicknamed 'Old Stone-Face' -- polite, never forgets a favor or a grudge."},
            {"name": "Leonard Aurelius", "title": "Board member", "notes": "Sold all his Ares stock to buy in (27 Oct 2059); broke free of his father Nicholas Aurelius's shadow and Ares both, now hunting Damien Knight with CATCo's resources."},
            {"name": "Bernard Cross", "title": "Head, Cross Advanced Electronics (Seattle)", "notes": "Lucien's nephew; nearly lost the division to a 2056 Mitsuhama takeover, saved only by the Seraphim; too fear-paralyzed to make real decisions since. Recalled to Montreal (per the book's own account) in 2061, a year past its own stated timeline."},
            {"name": "Jezebel Surrateau", "title": "Seattle Seraphim commander", "notes": "Physical adept, Grade 2+ initiate; effectively runs Cross Advanced Electronics under Bernard's nominal title. Paralyzed from the waist down since taking a bullet meant for Cross in 2053 -- refuses cyberware, works from a high-tech wheelchair. Absorbed part of Dunkelzahn's old Seattle shadow network via a defector named Hawke."},
            {"name": "Yves Aquillon", "title": "Corporate Court justice", "notes": "Won CATCo's Court seat 15 Apr 2060, following Renraku's Navroz Chandaria's death -- made CATCo a true AAA megacorp."},
        ],
        "notes": (
            "1953-2053 rivalry with Ares turned violent when Cross Biomedical stole the bioware firm "
            "Bioleve out from under an Ares shell company; Knight's hired assassin nearly killed Cross "
            "(the Seraphim took the bullet), Dunkelzahn personally warned Knight off, and Cross has "
            "survived three more 'accidents' since Dunkelzahn's death removed that protection. Quick "
            "Trigger Systems, a Detroit IC-software firm secretly controlled by Damien Knight, is "
            "trying to relocate into Quebec's Empowerment Zone under CATCo's nose (see Not in My "
            "Backyard, PLAY_NOTES)."
        ),
        "enemies": ["Ares Macrotechnology"],
    },
    {
        "name": "Sierra, Inc.",
        "org_type": "environmental organization",
        "tier": 2,
        "headquarters": "Sacramento, California Free State",
        "summary": "Old-line mainstream environmentalist group -- petitions and lawsuits, not eco-tage -- whose president sits on Ares Macrotechnology's board",
        "description": (
            "One of the oldest and largest environmental organizations, dating well back into the "
            "twentieth century; works through petitions, lawsuits and peaceful resistance rather than "
            "GreenWar-style sabotage, which gives it a far larger membership than more radical rivals -- "
            "and draws accusations from those rivals of being a corporate-comfort front. Arthur Vogel's "
            "two-year presidency (2057-2059) nudged it toward more public protest without crossing into "
            "eco-tage; membership held steady."
        ),
        "leadership": [
            {"name": "Gary Grey", "title": "President", "notes": "Vogel's former running mate; took over when Vogel stepped down 20 Oct 2059 to focus on his new Ares stock."},
            {"name": "Arthur Vogel", "title": "Board member", "notes": "Ecological lawyer, former UCAS presidential candidate; still holds a board seat after his Ares board appointment (Dunkelzahn's will) and his purchase of Leonard Aurelius's Ares stock."},
        ],
        "notes": "Some members suspect Vogel has 'sold out' to the corporate establishment since joining Ares' board; he has made no bold moves against Damien Knight so far, cautious or complicit depending who is asked.",
    },
    {
        "name": "Wuxing, Inc.",
        "org_type": "corporation",
        "tier": 5,
        "headquarters": "Hong Kong Free Enterprise Zone",
        "summary": "Wu Lung-Wai's Dunkelzahn-boosted AAA megacorp, the driving force and figurehead of the Pacific Prosperity Group",
        "description": (
            "Founded by Wu Kuan-Lai, who helped force Hong Kong's 2015 independence from China and then "
            "spent decades trying to break the Japanese megacorps' stranglehold on the Pacific Rim -- a "
            "dream his son Wu Lung-Wai finally realized. A 200-million-nuyen Dunkelzahn bequest let "
            "Lung-Wai push Wuxing into biochemistry, genetic engineering, agriculture, transportation, "
            "information management and (reputedly) magical research almost overnight; persistent, "
            "unproven rumors tie a great dragon to its cash flow. Li Feng's Corporate Court seat (15 Aug "
            "2059) made Wuxing an AAA megacorp."
        ),
        "leadership": [
            {"name": "Wu Lung-Wai", "title": "President/CEO", "notes": "Brilliant, charismatic, insists on face-to-face meetings; some suspect he is a 'social adept'. Known in the Pacific Rim as 'Hong Kong's Kingmaker'."},
            {"name": "Sun Runming", "title": "Head, Seattle division", "notes": "Portly, jovial, plays the oblivious hedonist to be constantly underestimated -- and pounces on any slip once he has been."},
            {"name": "Li Feng", "title": "Corporate Court justice", "notes": "Young corporate attorney, elected as a compromise choice after David Hague's death; rivals assumed they could manipulate him for his inexperience."},
        ],
        "notes": (
            "Setting up a new Seattle headquarters (see Mainframed, LOCATIONS) using deniable runner "
            "teams played against one another to scout talent for Wuxing's future needs."
        ),
        "allies": ["Pacific Prosperity Group", "Yamatetsu Corporation", "Tan Tien, Inc."],
    },
    {
        "name": "Pacific Prosperity Group",
        "org_type": "corporate alliance",
        "tier": 4,
        "headquarters": "Hong Kong Free Enterprise Zone",
        "summary": "Coalition of non-Japanese Pacific Rim corporations built to break the Japanese megacorps' regional dominance -- founded 8 July 2059, already a real power",
        "description": (
            "A NATO/OPEC-style coalition body: any Pacific Rim-based corporation in agreement with its "
            "charter may petition to join, each gets a board seat, and the board elects its own "
            "chairman. Founding members (8 Jul 2059) were Yamatetsu, Wuxing, Tan Tien, Eastern Tiger, "
            "Kwonsham Industries, the Malaysian Independent Bank, Shibata Construction and Engineering, "
            "and Lam Look Pagkaon and PacRim Communications Unlimited; more joined that September. "
            "Membership brings favorable Malaysian Independent Bank rates, favored trade status, joint "
            "research programs and a united front, at the cost of competition rules and production "
            "limits. The free spirit Buttercup courted the founding members through early 2059, and "
            "Yamatetsu's relocation to Vladivostok became the coalition's rallying point."
        ),
        "leadership": [
            {"name": "Izu Cheng", "title": "Chairman", "notes": "Gregarious, cunning negotiator from Wuxing; balances big members like Yamatetsu against numerous smaller ones."},
        ],
        "notes": (
            "With Yamatetsu and Wuxing both AAA and both on the Corporate Court, the PPG now rivals a "
            "single Japanese AAA megacorp for regional influence, though it cannot yet match the entire "
            "Japanese corporate bloc. Federated Boeing and Lockheed have both petitioned to join; neither "
            "has been accepted yet."
        ),
        "allies": ["Wuxing, Inc.", "Yamatetsu Corporation", "Tan Tien, Inc.", "Eastern Tiger Corporation", "Kwonsham Industries"],
    },
    {
        "name": "Eastern Tiger Corporation",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Pusan, Korea",
        "summary": "Unified Korea's largest single corporation -- petrochemicals and heavy manufacturing, nominal Pacific Prosperity Group member",
        "description": (
            "Expanded rapidly since 2050 into Australia, Brunei, the Salish-Shidhe Council, Seattle and "
            "Hawai'i, and diversified into biotechnology, entertainment, consumer goods and agriculture. "
            "Offers the PPG little more than lip service and would likely quietly withdraw if competition "
            "with the Japanese megacorps got too fierce -- though its CEO's personal grudges against "
            "Renraku and Mitsuhama might push it the other way."
        ),
        "leadership": [
            {"name": "Se-jong Lee", "title": "President/CEO", "notes": "Shrewd but cautious -- quick to seize an opportunity, sometimes too quick to cut and run."},
            {"name": "Yong-jo Moon", "title": "Head, Seattle division", "notes": "Se-jong Lee's nephew, shares his uncle's caution; denied extra security despite the go-gang Red Rovers repeatedly hitting ETC's trucks."},
        ],
        "notes": "Everett manufacturing plant; the subject of Truck Stop (NOT_BUILT), a Mitsuhama-seeded rumor of a milspec weapons shipment that draws every gang in Puyallup after ETC's trucks.",
    },
    {
        "name": "Federated Boeing",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Seattle, UCAS",
        "summary": "UCAS aerospace major petitioning to join the Pacific Prosperity Group, apparently to spite Mitsuhama's repeated takeover attempts",
        "description": (
            "Runs major plants in Vladivostok, Malaysia, Indonesia and elsewhere in the Pacific, often "
            "on natural-resource or facility deals that have left it deeply unpopular with several host "
            "nations. The PPG has not officially offered membership but is glad to take whatever help "
            "Fed-Boeing offers unofficially."
        ),
        "leadership": [
            {"name": "Jessica Sirianni", "title": "President/CEO", "notes": "Self-made from a poor Auburn childhood watching Fed-Boeing planes overhead; worked her way up from draftswoman through weapons and Auburn operations to the top job (late 2057). Ruthless, hands-on, keeps unusually shady connections."},
        ],
        "notes": "Its Auburn plant employed Sirianni as a young engineer; the Tacoma Wings Urban Brawl team is Fed-Boeing-sponsored (name-drop only).",
    },
    {
        "name": "Kwonsham Industries",
        "org_type": "corporation",
        "tier": 2,
        "headquarters": "Kyongyang, Korea",
        "summary": "United Korea industrial/electronics/agricultural conglomerate, formed from a dozen orphaned North Korean firms after reunification",
        "description": (
            "Formed in 2006 when a dozen larger 'orphan' companies from the newly privatized former "
            "North Korea banded together to survive the reunification buyout craze; now one of Korea's "
            "largest employers. A wholehearted Pacific Prosperity Group member looking to expand into a "
            "UCAS-based transportation division."
        ),
        "leadership": [
            {"name": "Jae-Myung Kim", "title": "President", "notes": "Stable man in his early fifties; wants to build Kwonsham into a multinational before handing it to his son. Frequent Seattle visits; unconfirmed rumors of meetings with the Choson Seoulpa Ring."},
        ],
        "notes": "",
    },
    {
        "name": "Monobe International",
        "org_type": "corporation",
        "tier": 4,
        "headquarters": "Matsuyama, Japan",
        "summary": "AA megacorp with first-tier ambitions under a new, ruthless COO-turned-president who may have had his predecessor's plane vanish over the ocean",
        "description": (
            "A diverse AA-tier corp -- biotechnology, firearms, cyberdeck components, travel services, "
            "genetic engineering, advanced communications research -- that could have made a run at "
            "AAA status years ago if former president Sho Kubota had cared about more than lining his "
            "own pockets. Now aggressively grabbing whatever scraps of Yamatetsu, Renraku and Fuchi it "
            "can reach."
        ),
        "leadership": [
            {"name": "Toshio Mitsukuri", "title": "President/COO", "notes": "Pulled off a coup in January 2059, replacing most of the executive staff within a week of taking power. His predecessor Sho Kubota sold his stock, headed for a retirement in Sri Lanka, and vanished from radar mid-flight -- Mitsukuri has never so much as hinted at involvement, but his reputation precedes him."},
        ],
        "notes": "The Japanese megacorps, still smarting over Yamatetsu's defection, may quietly back Monobe's push for AAA status to offset Wuxing's new Corporate Court seat.",
    },
    {
        "name": "Pacific Rim Bank and Financial Services Corporation",
        "org_type": "corporation",
        "tier": 4,
        "headquarters": "Tokyo, Japan",
        "summary": "The Pacific's largest bank, walking a shrinking neutral line between the Japanese megacorps and the Pacific Prosperity Group",
        "description": (
            "Does business with virtually every major Japanese corporation as well as most large "
            "corporations across China, Korea, Taiwan, Australia, Vietnam and eastern Russia -- many of "
            "them PPG members. Has stayed formally neutral despite Japanese government and megacorp "
            "pressure to penalize PPG members, but several PPG corporations are already shifting assets "
            "to the rival Malaysian Independent Bank, and most observers expect the PRB to tilt against "
            "the PPG eventually."
        ),
        "leadership": [
            {"name": "Enda Iyoji", "title": "President", "notes": "Presides over the bank's increasingly precarious neutrality."},
        ],
        "notes": "",
    },
    {
        "name": "Tan Tien, Inc.",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Beijing, Republic of China",
        "summary": "Small but fiercely independent Chinese research corp -- leads in cyberdeck design and neural interfaces, aligned with the Pacific Prosperity Group",
        "description": (
            "Barely a third-tier megacorp by cash flow, but a research leader in protein-chip storage, "
            "cranial cyberdeck design and nonintrusive neural interfaces, licensing its patents rather "
            "than manufacturing directly. Fuchi, Renraku and Mitsuhama have all attempted takeovers -- "
            "Renraku more than once -- and every attempt has mysteriously fallen through, fueling rumors "
            "from 'homegrown otaku sabotage' to a hidden ownership stake by the great dragon Lung."
        ),
        "leadership": [
            {"name": "Sau-hok Chu", "title": "President/CEO", "notes": "Enigmatic, reclusive, highly respected across the Chinese Republic; other Chinese corporations followed his lead in aligning with Wuxing and the PPG."},
        ],
        "notes": (
            "Developing Parallel Thought, a multi-user cyberdecking interface still in prototype; widely "
            "expected to be licensed to PPG members only, which would likely provoke a renewed Mitsuhama "
            "or Renraku takeover attempt."
        ),
        "allies": ["Pacific Prosperity Group", "Wuxing, Inc."],
    },
    {
        "name": "Yakashima Technologies",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Yokohama, Japan",
        "summary": "Japan's self-styled 'hostile-takeover king', back on the prowl now that its main rival Yamatetsu has fled the country",
        "description": (
            "Built a compact, efficient corporate empire through insight and dirty tricks; grew "
            "impressively in the early 2050s and took a Dunkelzahn bequest, but its own growth drew "
            "unwanted takeover attempts from Yamatetsu and Ares that stunted it for years. With "
            "Yamatetsu gone from Japan, it has resumed grabbing undefended ex-Yamatetsu subsidiaries."
        ),
        "leadership": [
            {"name": "Hiroshi Yakashima", "title": "President/CEO", "notes": "Takes visible pleasure in laying off metahuman workers from acquired firms; the company's PR now frames Yakashima as fighting for 'human purity', and it is playing well with Japan's human public."},
        ],
        "notes": "",
        "enemies": ["Yamatetsu Corporation"],
    },
    {
        "name": "HyperSense",
        "org_type": "corporation (simsense production)",
        "tier": 2,
        "headquarters": "Seattle",
        "summary": "Small, unusual-recording-technique simsense studio, 51 percent owned by Renraku as a quiet tech-spinoff testbed; its own owner is trying to fake its death",
        "description": (
            "A small, offbeat simsense production company known for unusual recording techniques and "
            "creative editing. Nearing bankruptcy two years before this book's present, owner Jacob Kilt "
            "sold Renraku a 51 percent controlling interest in exchange for keeping his own 49 percent and "
            "the CEO's chair; Renraku quietly channeled Leonardo spin-off technology through the studio, "
            "hoping to extrapolate new simsense-cutting techniques from it. It worked -- but Kilt has kept "
            "the real breakthrough to himself rather than report it, and has borrowed heavily from a local "
            "yakuza oyabun to fund a second, secret production facility built on it. Unknown to the yaks, "
            "who now think they own a piece of the future, that facility sits on Renraku's own money."
        ),
        "leadership": [
            {"name": "Jacob Kilt", "title": "Owner / CEO", "notes": "Twitchy on old wired reflexes; hires runners under a bad Mr. Johnson act to torch his own company and shake Renraku loose of it."},
        ],
        "notes": (
            "This Hurts Me More Than It Hurts You: Kilt poses as a Mr. Johnson and hires the runners to "
            "torch HyperSense's low-security building nonlethally, hoping the 'attack' convinces Renraku "
            "to divest. His secret facility is producing a new BTL chip line, Flashers, for the yakuza who "
            "financed it; when the oyabun learns Renraku secretly owns a piece of his investment, and "
            "Renraku learns of the secret site in turn, the two collide in a battle that may burn the new "
            "site to the ground either way."
        ),
    },
    {
        "name": "The Beamwalkers",
        "org_type": "otaku tribe",
        "tier": 1,
        "headquarters": "Northern Puyallup",
        "summary": "Reclusive, technically savvy young urban tribe with strong otaku ties, several of whom trained as deckers before joining -- and who tagged Renraku's own infiltrator",
        "description": (
            "A mysterious, reclusive urban tribe of young people out of northern Puyallup with a "
            "reputation for uncanny technical skill; a number of talented deckers were associated with "
            "the Beamwalkers in their younger days, and street rumor ties the tribe to the otaku "
            "phenomenon proper, though nobody has hard evidence either way."
        ),
        "notes": (
            "This Is Your Brain on Otaku: Renraku planted an undercover agent, Diana Peng, inside the "
            "tribe; when the Beamwalkers sent her into the Matrix to seek the 'Deep Resonance' as her "
            "final initiation, she came out with severe brain damage -- and a headware tracking tag the "
            "tribe had slipped onto her during the attempt. When Renraku hid her at a private clinic and "
            "Fuchi-hired runners extracted her for study, the Beamwalkers followed the tag straight to "
            "the handoff at Villa Plaza and seized the mall's own security system to take her back. "
            "Despite her ruined mind, the tribe has taken a liking to her and 'apparently still finds her "
            "useful.'"
        ),
    },
    {
        "name": "Quick Trigger Systems",
        "org_type": "corporation (IC software)",
        "tier": 2,
        "headquarters": "Detroit, Michigan, UCAS",
        "summary": "Detroit IC-software developer secretly controlled by Damien Knight, petitioning to relocate into Quebec's Empowerment Zone right under Cross Applied Technologies' nose",
        "description": (
            "A Detroit-based intrusion-countermeasures software house, hidden behind several layers of "
            "shell ownership that lead back to Damien Knight personally. Its petition to relocate into "
            "Quebec's tax-favorable Empowerment Zones -- approved by the national government, pending "
            "only a Quebec City Council vote -- would put a piece of Ares' Matrix-security business "
            "inside Cross Applied Technologies' home turf for the first time."
        ),
        "notes": (
            "Not in My Backyard: Lucien Cross's Seraphim, unable to crack QTS's Matrix defenses cleanly, "
            "hit its Detroit facility physically -- gang members hired to fake a truck chase, a rigged "
            "explosion, and a jackpoint decker lifting internal records that could tie QTS to Knight. "
            "Knight hired runners as extra facility security beforehand and, after the theft, to hunt down "
            "the stolen data and stop Quebec City's police chief from reaching the zoning vote in time. "
            "The vote's own stated deadline shifts between '10:15 a.m.' and 'before 11 a.m.' within the "
            "same framework -- the book's own inconsistency, left as found."
        ),
    },
    {
        "name": "Reactive Meditech",
        "org_type": "corporation (biotech)",
        "tier": 2,
        "headquarters": "Not given",
        "summary": "Third-tier biotech corp targeted for a Cross Applied Technologies takeover; issued bearer bonds to raise defense capital, then lost track of who was quietly buying them all up",
        "description": (
            "A third-tier biotech company under a prolonged hostile-takeover assault from Cross Applied "
            "Technologies. During the fight it flooded the market with short-term bearer bonds to raise "
            "cash; the contest dragged on long past when Reactive Meditech expected it to end, and the "
            "bonds' looming maturity date now threatens to bankrupt the company outright unless it can "
            "recover them."
        ),
        "leadership": [
            {"name": "Jeff Hansen", "title": "Security Director", "notes": "Discovered an uncomfortably large share of the bearer bonds were bought up by one unidentified buyer -- Lucien Cross himself -- and hires runners to steal them back."},
        ],
        "notes": (
            "Return Policy: text badly garbled in the OCR scan around pp.65-66; paraphrased from "
            "surrounding context. Cross's own plan was to use the bonds to squeeze financial control over "
            "Reactive Meditech -- he will not be pleased to see runners rob the bank vault holding them."
        ),
    },
    {
        "name": "Leviathan Technical",
        "org_type": "corporation (cyberware)",
        "tier": 2,
        "headquarters": "Silicon Valley, California Free State",
        "summary": "Ares-owned Silicon Valley cyberware division whose irresponsible toxic-waste dumping has drawn Terra First! and a Fuchi data-theft both",
        "description": (
            "A Silicon Valley corporation owned by Ares Macrotechnology, recently expanded into headware "
            "and skillwire cyberware production. Its labs generate a heavy load of toxic and biomedical "
            "waste, disposed of carelessly enough to enrage local eco-activists, chiefly Terra First!, "
            "who have gathered strong but not quite conclusive evidence tying the dumping to Leviathan."
        ),
        "notes": (
            "Green Piece: a Fuchi (Nakatomi faction) decker hacked Leviathan's Matrix host looking for "
            "leverage against Ares' hold on Silicon Valley and leaked some of what he found to Terra "
            "First!, but picked up a data worm that reported his activity straight back to Ares -- who "
            "dispatched a squad to kill him and recover or destroy the data. Arthur Vogel, hoping to use "
            "the same data to pressure Ares while staying invisible to Terra First!, hires runners to beat "
            "Ares to the decker first. Part of this framework is also OCR-garbled in the scan."
        ),
    },
    {
        "name": "Wasserkraft",
        "org_type": "corporation (water technology)",
        "tier": 1,
        "headquarters": "Germany",
        "summary": "German water-pollution and purification research firm -- part magic, part technology -- caught in a Renraku takeover fight after Fuchi's collapse",
        "description": (
            "A German corporation researching water pollution and purification through both magical and "
            "technological means, formerly a Fuchi Pan-Europa (Yamana faction) subsidiary. Renraku, acting "
            "on information Miles Lanier supplied to prove his loyalty, has already bought a stake and "
            "needs one more major shareholder's shares to gain a controlling interest."
        ),
        "notes": (
            "The Squeeze: the last holdout shareholder, the rich elf Dieter Arkona, has told both Renraku "
            "and Fuchi to frag off. Renraku hires runners to 'persuade' him by any means that gets him to "
            "sell."
        ),
    },
    {
        "name": "Vary v Zakone",
        "org_type": "organized crime (Russian mob)",
        "tier": 2,
        "headquarters": "Tacoma",
        "summary": "Tacoma's Russian mob, grown larger and bolder as Yamatetsu's relocation deepens trade -- legal and illegal -- between Tacoma and Vladivostok",
        "description": (
            "The Russian organized-crime network active in Tacoma, whose size and reach have grown "
            "sharply as Yamatetsu's move to Vladivostok pulls the Russkin community, and its underworld "
            "along with it, deeper into the city's economy."
        ),
        "leadership": [
            {"name": "Dimitri Makaroff", "title": "Boss (avtoritet)", "notes": "Learned that a rival yakuza oyabun is planning to break away from his own syndicate and wants proof to use as leverage."},
        ],
        "notes": (
            "Mob Clash: Makaroff is quietly gathering evidence of yakuza oyabun Hanzo Shotozumi's plans "
            "to found his own independent league, hoping to blackmail Shotozumi into ceding choice pieces "
            "of the yakuza's Tacoma rackets. Neither side wants to drag its parent syndicate into a second "
            "Mob War, so both hire freelance runners for kidnappings, break-ins, Matrix raids, "
            "surveillance, bodyguard work and infiltration rather than committing their own soldiers."
        ),
        "enemies": ["Yakuza (Watada-rengo)"],
    },
    {
        "name": "Shotozumi-rengo",
        "org_type": "yakuza clan",
        "tier": 1,
        "headquarters": "Tacoma",
        "summary": "Breakaway yakuza league founded when oyabun Hanzo Shotozumi finally split from the Watada-rengo, ending a Russian mob blackmail attempt but making new enemies",
        "description": (
            "Formed when Tacoma yakuza oyabun Hanzo Shotozumi finally broke away from the Watada-rengo to "
            "found his own independent league, after months of trying and failing to keep the plan secret "
            "from Vary v Zakone's Dimitri Makaroff."
        ),
        "leadership": [
            {"name": "Hanzo Shotozumi", "title": "Oyabun", "notes": "Split from the Watada-rengo despite Makaroff's blackmail attempts; the break ends Makaroff's leverage but hands him new enemies to ally against."},
        ],
        "notes": "Mob Clash: once the split is public, Makaroff loses his blackmail hold on Shotozumi but gains an opening to ally with Shotozumi's new rivals within the old Watada-rengo structure.",
        "enemies": ["Yakuza (Watada-rengo)"],
    },
]

LOCATIONS = [
    {
        "name": "Zurich-Orbital",
        "location_type": "orbital platform",
        "city": "Earth orbit",
        "district": "Seat of the Corporate Court",
        "security_level": "Corporate Extraterritorial",
        "summary": "The Corporate Court's orbital seat -- Ares' old space platform, sold to Fuchi and renamed, now run by the Zurich-Orbital Gemeinschaft Bank",
        "description": (
            "Originally Ares Macrotechnology's orbital operations platform, sold to Fuchi Industrial "
            "Electronics and renamed when the Corporate Court moved its own headquarters aboard. Life "
            "aboard is a constant series of tradeoffs against the vacuum outside; corporate officials "
            "who can afford otherwise spend as little time here as duty demands. The platform "
            "'de-cloaks' from its usual communications posture only for Court business."
        ),
        "notes": (
            "Prologue setting (15 Aug 2059): Saeder-Krupp's Jean-Claude Priault reports to Lofwyr here "
            "by telecom on the Corporate Court vote seating Wuxing's Li Feng. The Court convenes here in "
            "person for genuinely urgent business -- an 18-hour communications blackout in June 2059 "
            "produced the ruling that sent Miles Lanier back to Fuchi custody. The Zurich-Orbital "
            "Gemeinschaft Bank, which holds the Renraku stock sold by Lanier and bought back by Shikei "
            "Nakatomi, is based here."
        ),
    },
    {
        "name": "Flight 1118 Crash Site",
        "location_type": "ruins",
        "district": "Redmond Barrens, near the Salish-Shidhe border",
        "security_level": "No Security / Barrens",
        "summary": "Where a Tokyo-Seattle semiballistic overshot Sea-Tac and plowed into the Barrens on 11 July 2059, killing roughly 200 -- and where Fuchi justice David Hague's body vanished for a week",
        "description": (
            "The downed aircraft broke into four major pieces across several square miles of the "
            "Redmond Barrens: the tail section in James Lake, mostly submerged, and the nose section "
            "plowed into a hillside several miles east, with a wide swath of wreckage, fire and bodies "
            "between them. In the crash's chaos, DocWagon ambulances, Lone Star, Metroplex Guard, "
            "reporters, corporate volunteer teams, go-gangs and looters converge from every direction."
        ),
        "notes": (
            "Corporate Court justice David Hague was aboard, seen boarding in Tokyo; his body was not "
            "found at the crash site, but turned up a week later in an abandoned apartment building "
            "some miles away, minus his cyberware headware memory. A fake DocWagon Crisis Response Team "
            "-- actually Renraku operatives -- worked the wreckage the night of the crash, extracting "
            "Hague's body and Corporate Court briefcase before a real DocWagon team caught them at it. "
            "Site of the Crash Team adventure framework, PLAY_NOTES."
        ),
    },
    {
        "name": "Stasky Institute",
        "location_type": "hospital",
        "city": "Tacoma",
        "district": "Small medical park near Doctor's Hospital of Tacoma",
        "security_level": "Patrolled / Commercial",
        "summary": "Small private neurological clinic where a brain-damaged Renraku undercover agent was hidden under a false name",
        "description": (
            "A two-story clinic specializing in neurological dysfunctions in a well-to-do part of "
            "Tacoma; security is built to keep patients in rather than intruders out, though Lone Star "
            "patrols the area frequently."
        ),
        "notes": (
            "Renraku checked its brain-damaged otaku-tribe infiltrator Diana Peng in here under the "
            "alias 'Olivia Tang' after a Matrix expedition into the 'Deep Resonance' left her with "
            "severe cognitive damage and an obsessive fixation on cyberdecks. See This Is Your Brain on "
            "Otaku, PLAY_NOTES."
        ),
    },
    {
        "name": "Villa Plaza",
        "location_type": "mall",
        "district": "Seattle",
        "security_level": "Patrolled / Commercial",
        "summary": "Shopping mall, home to a Hardware Etcetera cyberdeck storefront, where an extraction handoff was ambushed by the otaku tribe that had bugged the victim",
        "description": (
            "An ordinary Seattle mall notable for a Hardware Etcetera store selling cyberdecks near its "
            "main entrance, and for the fact its security system can apparently be seized wholesale by a "
            "sufficiently determined decker."
        ),
        "notes": (
            "Handoff point in This Is Your Brain on Otaku: the Beamwalkers tribe, tracking a headware "
            "bug they placed on Diana Peng, seize Villa Plaza's mall security and the Hardware Etcetera "
            "storefront's after-hours locks to reclaim her from her captors mid-exchange."
        ),
    },
    {
        "name": "City Center Building",
        "location_type": "corporate headquarters",
        "district": "Downtown Seattle, seven blocks from Pier 27",
        "security_level": "Corporate High Security",
        "controlling_org": "Yamatetsu Corporation",
        "summary": "Yamatetsu Seattle's headquarters -- the false destination in a Wuxing shell game over two crates of decommissioned mainframes",
        "description": "A downtown Seattle office tower serving as Yamatetsu Seattle's headquarters, seven blocks from the Pier 27 docks.",
        "notes": (
            "In Mainframed, a Wuxing executive posing as 'Ms. Johnson' plants false clues pointing here "
            "as the destination for two hijacked mainframe crates actually bound for Wuxing's new "
            "Haukshorn towers office at Green Lake -- while the real owner, Tsuruga International "
            "(Yamatetsu Asia), tracks the cargo by transponder the whole way."
        ),
    },
    {
        "name": "Cross Advanced Electronics",
        "location_type": "corporate facility",
        "district": "Seattle",
        "security_level": "Corporate Standard",
        "controlling_org": "Cross Applied Technologies, Inc.",
        "summary": "CATCo's Seattle-facing division -- nominally run by Lucien Cross's overwhelmed nephew, actually run by his Seraphim field commander",
        "description": (
            "Cross Applied Technologies' Seattle division, in open, ongoing competition with Ares "
            "Seattle for local market share and shadow-ops advantage. Nearly lost to a 2056 Mitsuhama "
            "takeover attempt before a Seraphim intervention saved it."
        ),
        "notes": (
            "Bernard Cross holds the title; Jezebel Surrateau, the Seraphim's Seattle commander, "
            "actually runs it and handles its 'Ms. Johnson' shadow contracting. Ares' Karen King has made "
            "beating CAE her personal project, so far without success (see Ares Macrotechnology)."
        ),
    },
    {
        "name": "Ares Bellevue Offices",
        "location_type": "corporate facility",
        "district": "Beaux Arts, Bellevue",
        "security_level": "Corporate High Security",
        "controlling_org": "Ares Macrotechnology",
        "summary": "Ares Seattle's office tower, linked by high-speed monorail to an exclusive executive housing district -- site of a defection extraction gone loud",
        "description": (
            "Ares' Seattle office building, connected by a private high-speed monorail to Ares-owned "
            "executive housing in the exclusive Beaux Arts district a few miles away; both ends run "
            "tight security, including some of Knight Errant's best."
        ),
        "notes": (
            "Double Crossover: Cross Applied Technologies' Seraphim extract Consumer Electronics VP "
            "Raymond Briggs from here (his father William Briggs was defecting to CATCo in Detroit the "
            "same week) using back doors William provided into the building's and monorail's Matrix "
            "systems; Novatech agents try to poach Raymond mid-extraction."
        ),
    },
    {
        "name": "Haukshorn Towers",
        "location_type": "corporate headquarters",
        "district": "Green Lake, Seattle",
        "security_level": "Corporate Standard",
        "controlling_org": "Wuxing, Inc.",
        "summary": "Former Haukshorn Chemicals headquarters, divided into rented office space -- soon to become Wuxing's new Seattle headquarters after a mainframe shell game",
        "description": (
            "The former corporate headquarters of Haukshorn Chemicals, eight miles north of downtown "
            "Seattle by Green Lake, now divided into office space rented out to smaller companies."
        ),
        "notes": (
            "The true (falsely denied) destination for two crates of decommissioned Yamatetsu mainframes "
            "hijacked and re-hijacked across three competing runner teams in Mainframed; a week after the "
            "adventure, Wuxing announces it has purchased the towers outright to convert into its Seattle "
            "headquarters."
        ),
    },
    {
        "name": "Lee Chee Garden",
        "location_type": "restaurant",
        "district": "Seattle",
        "security_level": "Patrolled / Commercial",
        "summary": "Enric Wong's soundproof-back-room restaurant, trusted neutral ground for shadowy and corporate meetings alike -- and secretly wired for Tan Tien's benefit",
        "description": (
            "A well-regarded Chinese restaurant whose soundproofed back room has long been used by "
            "corporate and shadow clientele alike as safely neutral ground for sensitive meetings. Wong "
            "himself is rumored to summon and consult an 'ancient Chinese ghost' in that room from time "
            "to time."
        ),
        "notes": (
            "The 'ghost' is really the astrally projected form of Tan Tien's CEO Sau-hok Chu, Wong's "
            "half-brother; the back room's conversations are quietly recorded and passed back to Chu, "
            "feeding Tan Tien's information network. See Ancient Chinese Secret, Huh?, PLAY_NOTES."
        ),
    },
]

NPCS = [
    {
        "name": "Richard Villiers",
        "role": "President/CEO of Novatech, Inc. -- the corporate shark who rebuilt a third of Fuchi as his own AAA megacorp",
        "archetype": "Corporate Executive",
        "title": "President/CEO, Novatech, Inc.",
        "race": "Human",
        "gender": "Male",
        "connection": 6,
        "description": (
            "One of the most respected and feared men in the UCAS. Talked his way into a third of Fuchi "
            "Industrial Electronics decades ago by selling it stolen cyberdeck technology, then spent "
            "2059 alone sending Renraku's stock into a nosedive, driving Fuchi to self-destruction, and "
            "building his own portion of it into Novatech -- a new AAA megacorp, one of the smallest "
            "ever to earn the rank."
        ),
        "background": (
            "Made his name as a Boston corporate raider before recognizing the potential of Matrix "
            "Systems' prototype cyberdeck (the Portal) in 1933; its founders, Ken Roper and Michael Eld, "
            "died within an hour of each other under murky circumstances shortly after, and Villiers "
            "bought the ruined company for a fraction of its value. He parlayed the recovered technology "
            "into a third of Fuchi Industrial Electronics and decades of internal maneuvering against his "
            "co-owners, the Yamana and Nakatomi families, culminating in Novatech's formation."
        ),
        "notes": (
            "Widely, never provably, believed to have arranged Kiyoshi Nakatomi's 2035 death. Secretly "
            "funded the shell Cambridge Holdings (via Silveril Investments) to strip roughly 22 "
            "subsidiaries out of Fuchi Americas before folding Cambridge into Novatech directly. "
            "Suspected, again without proof, of sabotaging Flight 1118 to remove Corporate Court justice "
            "David Hague."
        ),
        "contact_skills": ["Corporate finance and hostile takeovers", "Fuchi/Novatech internal politics"],
    },
    {
        "name": "Miles Lanier",
        "role": "Novatech's director of security -- Fuchi's former security chief, briefly a Renraku board member, whose true loyalties nobody can prove either way",
        "archetype": "Corporate Executive",
        "title": "Director of Security, Novatech, Inc.",
        "race": "Human",
        "gender": "Male",
        "connection": 4,
        "description": (
            "An ex-UCAS Army sniper who would have made general had he stayed; instead built a "
            "reputation as one of the great tactical minds of his generation inside Fuchi's security "
            "apparatus. Arrogant, demanding, but undeniably brilliant."
        ),
        "background": (
            "Fuchi's head of internal security and Richard Villiers' close friend until Dunkelzahn's "
            "will handed him a Renraku board seat and four million shares of Renraku stock in 1957 -- he "
            "left Fuchi within the day. His inside knowledge helped Renraku leap ahead of Fuchi "
            "technologically for two years, until a June 2059 Corporate Court ruling forced him back to "
            "Fuchi custody. He resurfaced as Novatech's security director when Villiers formed the corp "
            "that October."
        ),
        "notes": (
            "Whether his Renraku tenure was genuine defection or an elaborate Villiers scam was never "
            "settled -- Renraku chairman Yukiako Watanabe ran three separate deniable loyalty tests on "
            "him and came away with nothing conclusive either way (see Prove It to Me, PLAY_NOTES). Now "
            "purges Yamana/Nakatomi loyalists from ex-Fuchi divisions being retooled as Novatech and "
            "redesigns their physical and Matrix security."
        ),
    },
    {
        "name": "Samantha Villiers",
        "role": "VP of Novatech Northwest -- Richard Villiers' ex-wife, who held the tiebreaking stock that decided Fuchi's fate",
        "archetype": "Corporate Executive",
        "title": "Vice President, Novatech Northwest",
        "race": "Human",
        "gender": "Female",
        "age": 48,
        "connection": 3,
        "description": (
            "Divorced from Richard more than a decade; sharp-witted, wealthy, and by all accounts one of "
            "Seattle's most eligible singles, with no apparent interest in remarrying."
        ),
        "background": (
            "Rose through Fuchi Systems Design and Fuchi Northwest to become Novatech Northwest's VP. "
            "When the post-split Fuchi stock left Korin Yamana and Shikei Nakatomi deadlocked at roughly "
            "45 percent each, Samantha's remaining 2 percent became the tiebreaker."
        ),
        "notes": "Sold her 2 percent to Korin Yamana in January 2060 in exchange for a one-year non-interference truce between Novatech and Fuchi.",
    },
    {
        "name": "Darren Villiers",
        "role": "Novatech Seattle's director of special assets -- Richard Villiers' dwarf brother and a former deniable covert operative",
        "archetype": "Physical Adept",
        "title": "Director of Special Assets, Novatech Seattle",
        "race": "Dwarf",
        "gender": "Male",
        "connection": 3,
        "description": (
            "Richard Villiers' younger brother and the only known metahuman in the Villiers family, a "
            "Grade 3 magical initiate with a talent for stealth and burglary."
        ),
        "background": (
            "Held the title of Fuchi's SVP for Seattle operations for years while spending little time "
            "in the office -- he was really working the shadows, alone or leading unwitting runner "
            "teams, to acquire blackmail material on Seattle politicians and rival executives."
        ),
        "notes": "Now hires others to do most of the dirty work as Novatech's Seattle director of special assets, though he still occasionally handles sensitive jobs personally.",
    },
    {
        "name": "Sadato Shiawase",
        "role": "Chairman of Shiawase's board and head of the Shiawase family -- publicly compassionate, privately locked in a decades-long feud with his own sister",
        "archetype": "Corporate Executive",
        "title": "Chairman of the Board, Shiawase Corporation",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Shiawase Corporation",
        "connection": 4,
        "description": "Presents a stern but compassionate public face built on Shiawase's family-oriented image; privately a hard-nosed businessman who wishes he could buy out the rest of his own family.",
        "background": "Has feuded with his sister Soka Shiawase since at least 2051; the siblings maintain a unified public front while trading actual assassination attempts.",
        "notes": "",
    },
    {
        "name": "Tadashi Shiawase",
        "role": "Shiawase's president and CEO in name -- his father Sadato still holds the real power",
        "archetype": "Corporate Executive",
        "title": "President/CEO, Shiawase Corporation",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Shiawase Corporation",
        "connection": 3,
        "description": "Sadato's son; capable and inclined to reject his father's pure bottom-line mentality when given the chance, but too cowed to push hard for fear of being replaced.",
        "background": "Will likely not come into his own until his father retires or dies -- unlikely either happens soon.",
        "notes": "His weakness is his reckless teenage daughter Hitomi, who has nearly died at least once escaping her bodyguards.",
    },
    {
        "name": "Korin Yamana",
        "role": "Ex-head of Fuchi Pan-Europa, who achieved his forty-year goal of controlling Fuchi only to sell what was left of it to Shiawase and marry into the family",
        "archetype": "Corporate Executive",
        "title": "Board Member, Shiawase Corporation",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "age": 90,
        "organization": "Shiawase Corporation",
        "connection": 4,
        "description": "Ninety years old; achieved his decades-long ambition to control Fuchi in January 2060 only to find it a hollow, short-lived victory as the corp collapsed around him regardless.",
        "background": (
            "One of Fuchi's three founding co-owners (Fuchi Pan-Europa). Gained majority control when "
            "Samantha Villiers sold him her tiebreaking Fuchi stock, but by mid-2060, with Fuchi's Asia "
            "faction gone to Renraku and its Americas faction long since Novatech, arranged a marriage "
            "to Mitsuko Shiawase (announced 8 June 2060) and sold the remainder of Fuchi Industrial "
            "Electronics to Shiawase Corporation for stock and a board seat."
        ),
        "notes": "Now overseeing Fuchi's absorption into Shiawase; considering retirement to Zurich-Orbital or a quiet estate once the integration is complete.",
    },
    {
        "name": "Mitsuko Shiawase-Yamana",
        "role": "VP of Shiawase Envirotech's Philippines division -- married Korin Yamana as pure economic expediency, on both sides",
        "archetype": "Corporate Executive",
        "title": "Vice President, Shiawase Envirotech (Philippines)",
        "race": "Human",
        "gender": "Female",
        "nationality": "Japanese",
        "organization": "Shiawase Corporation",
        "connection": 3,
        "description": "Dispassionate and analytical, fiercely devoted to her mother Soka Shiawase first and Shiawase Corporation second; evaluates everything else in purely practical terms.",
        "background": "Tasked by her mother with stopping anti-Japanese rebel and pirate attacks on Shiawase's Philippine installations.",
        "notes": "Views her marriage to Korin Yamana as pure economic expediency, a judgment she knows he shares; the couple live separately and rarely speak.",
    },
    {
        "name": "Inazo Aneki",
        "role": "Renraku's President/CEO for decades -- the corporate raider turned devoted patriarch who took an indefinite leave just as Renraku's fortunes turned",
        "archetype": "Corporate Executive",
        "title": "President/CEO, Renraku Computer Systems",
        "race": "Human",
        "gender": "Male",
        "age": 70,
        "organization": "Renraku Computer Systems",
        "connection": 5,
        "description": "Never married; considers Renraku itself his family. Patient and prudent now, a far cry from the young raider who bought the failing Keruba International out from under its shareholders in 2029.",
        "background": (
            "Built Renraku from the wreckage of Keruba International, survived a boardroom coup attempt "
            "with a 'reverse coup' of his own, purged the corp's rampant corruption through the 2030s, "
            "and steered it back into the first tier by 2045. Cut a secret 1957 deal with the elf decker "
            "genius Leonardo that briefly made Renraku's Matrix technology untouchable."
        ),
        "notes": (
            "Began an indefinite leave of absence in February 2060 -- using the Seal of the Green "
            "Glaves, a token Dunkelzahn's will bequeathed him granting entry to Tibet -- leaving COO "
            "Haruhiko Nakada as acting CEO. No word since on his whereabouts or return."
        ),
    },
    {
        "name": "Yukiako Watanabe",
        "role": "Renraku's chairman of the board -- ruthless, devoted, and deeply suspicious that Miles Lanier is still Fuchi's man",
        "archetype": "Corporate Executive",
        "title": "Chairman of the Board, Renraku Computer Systems",
        "race": "Human",
        "gender": "Female",
        "nationality": "Japanese",
        "organization": "Renraku Computer Systems",
        "connection": 4,
        "description": "Intelligent, confident, ruthless and fiercely devoted to Renraku; rules the boardroom with an iron hand and generally sees eye to eye with Aneki, sparing Renraku the kind of infighting that tore Fuchi apart.",
        "background": "Rose to the top of a Japanese boardroom despite the odds long stacked against a woman doing so.",
        "notes": (
            "Ran three separate deniable loyalty tests on Miles Lanier through hired runners -- "
            "surveillance, a staged fake assassination attempt, and a sting operation -- without ever "
            "proving his loyalties either way (see Prove It to Me, PLAY_NOTES). Has since grudgingly "
            "given him wider access."
        ),
    },
    {
        "name": "Haruhiko Nakada",
        "role": "Renraku's COO and acting CEO during Aneki's leave -- cheerful in public, ruthless underneath, and quietly hoping the leave never ends",
        "archetype": "Corporate Executive",
        "title": "Chief Operating Officer / Acting CEO, Renraku Computer Systems",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Renraku Computer Systems",
        "connection": 4,
        "description": "Known even in Chiba by the nickname 'Harry'; a cheerful, outgoing facade over a basically ruthless nature.",
        "background": "Long groomed by Aneki as his likely successor.",
        "notes": "Believes Aneki's leave is partly a test of his own capability, and won't take unnecessary risks that would jeopardize succeeding him in a few years -- no coup attempt, just patience.",
    },
    {
        "name": "Dr. Sherman Huang",
        "role": "Renraku America's division manager and the Seattle arcology's executive director -- devastated by its December 2059 shutdown, still hunting the cause",
        "archetype": "Corporate Executive",
        "title": "Division Manager, Renraku America / Executive Director, Seattle Arcology",
        "race": "Human",
        "gender": "Male",
        "organization": "Renraku Computer Systems",
        "connection": 3,
        "description": "A hands-on manager unlike most of his rank -- personally instrumental in developing the arcology's Arcology Expert Program; eccentric but sharp, consistently underestimated.",
        "background": "A close friend of Inazo Aneki; relocated his office to Renraku's New York headquarters but still returns often to Seattle to test theories on the shutdown.",
        "notes": "",
        "contact_skills": ["Arcology systems and the Arcology Expert Program"],
    },
    {
        "name": "Shikei Nakatomi",
        "role": "Ex-head of Fuchi Asia turned Renraku board member -- the 'Business Butcher', now hunting Richard Villiers with Renraku's resources behind him",
        "archetype": "Corporate Executive",
        "title": "Board Member, Renraku Computer Systems",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Renraku Computer Systems",
        "connection": 5,
        "description": "Known during his Fuchi days as the 'Business Butcher' for his ruthlessness in pursuit of profit; now his motivations have turned personal as well.",
        "background": (
            "Inherited his father Kiyoshi Nakatomi's share of Fuchi Asia after Kiyoshi's 2035 murder "
            "(long suspected, never proven, to be Richard Villiers' doing). Lost the internal Fuchi "
            "power struggle to Korin Yamana in early 2060, then bought back into Renraku (April 2060) "
            "with the same 4 million shares Miles Lanier once sold there, gaining a board seat and "
            "bringing Fuchi Asia's remaining assets with him."
        ),
        "notes": "Blames Richard Villiers for everything that has gone wrong at Fuchi and Renraku alike; is quietly building a Villiers-hating faction on Renraku's board and will push for a full assault on Novatech once he has the votes.",
    },
    {
        "name": "Liam Riley",
        "role": "President/CEO of Transys Neuronet -- an HKB-appointed board member maneuvered into the top job, doing surprisingly well so far",
        "archetype": "Corporate Executive",
        "title": "President/CEO, Transys Neuronet",
        "race": "Human",
        "gender": "Male",
        "organization": "Transys Neuronet",
        "connection": 3,
        "description": "A relative newcomer to AA-megacorp politics, appointed to Transys's board in 2053 from the rank and file of HKB's Data Services division.",
        "background": "The Hildebrandt-Kleinfart-Bernal financial empire maneuvered him into the presidency in 2058 despite the decidedly suspect nature of his rise.",
        "notes": "Market analysts reserve judgment on where HKB's real long-term agenda for Transys will lead.",
    },
    {
        "name": "Karen King",
        "role": "Ares Seattle's supervising VP -- a ruthless climber taking bigger risks locally to catch Damien Knight's eye, currently losing a proxy war with CATCo's Seattle Seraphim",
        "archetype": "Corporate Executive",
        "title": "Supervising Vice President, Ares Seattle",
        "race": "Human",
        "gender": "Female",
        "age": 50,
        "organization": "Ares Macrotechnology",
        "connection": 3,
        "description": "A young-looking fifty who earned her post the only way that matters to Damien Knight -- by ruthlessly crushing everyone in her way. Ten-plus years running Ares Seattle, and hunting for a shot at the next rung up.",
        "background": "Knight rarely visits or checks her work personally, which cuts both ways -- fewer chances to impress him directly, so she has begun gambling more with local operations.",
        "notes": "Fixated on beating Cross Advanced Electronics, CATCo's Seattle division, which has held its own against her far longer than expected; losing her overpriced campaign against it could cost her the job.",
    },
    {
        "name": "Lucien Cross",
        "role": "President/CEO of Cross Applied Technologies -- Damien Knight's old programming partner, who has kept blackmail insurance on him for thirty years",
        "archetype": "Corporate Executive",
        "title": "President/CEO, Cross Applied Technologies, Inc.",
        "race": "Human",
        "gender": "Male",
        "age": 69,
        "organization": "Cross Applied Technologies, Inc.",
        "connection": 6,
        "description": "Nearing seventy and showing no sign of slowing down; still personally oversees Cross Matrix Technologies, holds weekly division-head teleconferences, and visits every major CATCo facility quarterly. Polite to a fault, drives a hard bargain without raising his voice, and never forgets a favor or a grudge -- employees call him 'Old Stone-Face'.",
        "background": (
            "Programmed Damien Knight's 2033 Nanosecond Buyout as 'David Gavilan's' collaborator; took a "
            "commission instead of stock, but kept the original planning records proving Knight's true "
            "identity as insurance. Built Cross Matrix Technologies into Cross Applied Technologies over "
            "two decades, funded quietly by Dunkelzahn for years before that patronage became public."
        ),
        "notes": (
            "Survived Knight's hired assassin in 2053 (the Seraphim took the bullet meant for him) after "
            "stealing the bioware firm Bioleve out from under an Ares shell company; has survived three "
            "more suspicious 'accidents' since Dunkelzahn's death removed the dragon's protection."
        ),
    },
    {
        "name": "Leonard Aurelius",
        "role": "Cross Applied Technologies board member -- Ares' founder's son, who finally broke free of his father's shadow by selling out to Knight's oldest enemy",
        "archetype": "Corporate Executive",
        "title": "Board Member, Cross Applied Technologies, Inc.",
        "race": "Human",
        "gender": "Male",
        "organization": "Cross Applied Technologies, Inc.",
        "connection": 5,
        "description": "Spent most of his life in the shadow of his famous, domineering father Nicholas Aurelius, worried about losing what Nicholas built and afraid of failing him -- a conservative, if intelligent, leader as a result.",
        "background": (
            "Ousted from Ares' top spot by Damien Knight's Nanosecond Buyout in 2033; spent decades "
            "trying to reclaim it. An explosive argument with his youngest daughter finally pushed him to "
            "stop living for his dead father's legacy. Sold all his Ares stock in 2059 to buy into Cross "
            "Applied Technologies, giving Cross both cash and detailed insider knowledge of Knight."
        ),
        "notes": "Sold his own remaining personal Ares stock privately to Arthur Vogel rather than the open market -- deliberately arming the man most likely to make life difficult for Knight. Still hopes to reclaim Ares someday, on his own terms, but will sacrifice that hope to destroy Knight if it comes to a choice.",
    },
    {
        "name": "Bernard Cross",
        "role": "Nominal head of Cross Advanced Electronics in Seattle -- Lucien Cross's nephew, too fear-paralyzed by one near-catastrophe to actually run it",
        "archetype": "Corporate Executive",
        "title": "Head, Cross Advanced Electronics (Seattle)",
        "race": "Human",
        "gender": "Male",
        "organization": "Cross Applied Technologies, Inc.",
        "connection": 2,
        "description": "Never particularly decisive; terrified into near-total indecision after nearly losing his entire division and his life in 2056.",
        "background": "Misread a 2056 Mitsuhama takeover attempt on Cross Advanced Electronics almost fatally; only a direct, bloody Seraphim intervention saved him and the division.",
        "notes": "Relies entirely on Jezebel Surrateau and the Seraphim for the division's real day-to-day decisions; the Cross family name is what has kept him employed. Recalled to Montreal in 2061 per the book's own account, a year past its stated timeline.",
    },
    {
        "name": "Jezebel Surrateau",
        "role": "Seattle commander of the Seraphim, Cross Applied Technologies' elite intelligence arm -- paralyzed since taking a bullet for Lucien Cross, and running Cross Advanced Electronics in all but title",
        "archetype": "Physical Adept",
        "title": "Seattle Commander, the Seraphim",
        "race": "Human",
        "gender": "Female",
        "organization": "Cross Applied Technologies, Inc.",
        "connection": 4,
        "description": "One of Lucien Cross's hand-picked agents, specialized in investigation, physical intrusion and theft; also long rumored to be his mistress. At least a Grade 2 magical initiate, developing adept abilities her paralysis will not hinder.",
        "background": "Took a bullet meant for Cross during the 2053 assassination attempt and has been paralyzed from the waist down ever since; refused invasive surgery or cyberware to remove it and works from a high-tech wheelchair.",
        "notes": (
            "Sent to Seattle when Bernard Cross began drowning in the job; her take-charge leadership has "
            "kept Ares' Karen King from making real headway against Cross Advanced Electronics. Recently "
            "absorbed part of Dunkelzahn's old Seattle shadow network after a runner named Hawke defected "
            "to her over the death of a friend."
        ),
        "contact_skills": ["Corporate espionage and shadow-asset management (Seattle)"],
    },
    {
        "name": "Buttercup",
        "role": "Free spirit and major Yamatetsu shareholder -- once played humanity for pets, now the driving force behind Yamatetsu's flight from Japan and its embrace of metahuman equality",
        "archetype": "Free Spirit",
        "title": "Major Shareholder, Yamatetsu Corporation",
        "race": "Free Spirit",
        "gender": "Female",
        "connection": 5,
        "description": (
            "Appears in human form as a petite, pretty Japanese girl of about eighteen, long black hair "
            "often tied up, an expressive face that glows when excited or agitated; moves with unnatural "
            "grace and sometimes floats slightly above whoever she is addressing. Known powers include "
            "Astral Gateway, Aura Masking, Human Form, Possession, Sorcery and Wealth; can use Sense Link "
            "with anyone who feeds her mana, and anyone who learns her true name can attempt a Telepathic "
            "Link with her."
        ),
        "background": (
            "Summoned centuries before the Awakening and free since sometime before the twentieth "
            "century; long considered mortals beneath her notice, rewarding and punishing them on a "
            "whim. Clashed with Dunkelzahn, who bound her into an underprivileged ork's body for a year "
            "and a day to teach her humility; she has since become an advocate for equality among all "
            "sentient life, using Dunkelzahn's own investment strategy to build a major stake in "
            "Yamatetsu."
        ),
        "notes": (
            "Pushed Yamatetsu toward its meta-friendly policy after Dunkelzahn's death, then engineered "
            "the corporation's May 2059 relocation to Vladivostok by producing proxies for nearly a "
            "quarter of Yamatetsu's stock and personally buying up more once the move was announced, "
            "giving her roughly 37 percent control alongside Yuri Shibanokuji's. Had Tadamako Shibanokuji "
            "killed via a possessed nurse rather than let his anti-metahuman faction keep control of his "
            "voting stock -- a fact only she knows for certain."
        ),
    },
    {
        "name": "Yuri Shibanokuji",
        "role": "Yamatetsu's chairman -- an ork who inherited his estranged father's shares and, with Buttercup's backing, dragged the corporation out of Japan entirely",
        "archetype": "Corporate Executive",
        "title": "Chairman of the Board, Yamatetsu Corporation",
        "race": "Ork",
        "gender": "Male",
        "age": 39,
        "organization": "Yamatetsu Corporation",
        "connection": 4,
        "description": "A born human who goblinized at puberty and remembers nothing of life before; raised with strong morals in multiracial Vladivostok, which kept him from underestimating himself for his race the way Japan would have.",
        "background": (
            "Son of Tadamako Shibanokuji and a Russian port official, Tatiana Trigorin; sent back to "
            "Russia with his mother as a child when his father's corporate enemies threatened to use his "
            "metahumanity against him. Built a small restaurant chain before inheriting his father's "
            "Yamatetsu shares in early 2059, over the board's expectation that he would simply sell out "
            "and retire."
        ),
        "notes": "Proposed relocating Yamatetsu's headquarters to his own home of Vladivostok at an emergency board meeting in May 2059; the motion seemed doomed until Buttercup rallied enough proxies to pass it. In over his head at Yamatetsu and knows it -- leans heavily on Buttercup and Newton Chin.",
    },
    {
        "name": "Saru Iwano",
        "role": "Yamatetsu's CEO -- voted Tadamako Shibanokuji's stock during his incapacitation, and used it to entrench the corp's anti-metahuman faction",
        "archetype": "Corporate Executive",
        "title": "President/CEO, Yamatetsu Corporation",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Yamatetsu Corporation",
        "connection": 3,
        "description": "Visibly upset but silent when the board voted to relocate to Vladivostok against his own faction's wishes.",
        "background": "Held Tadamako Shibanokuji's voting shares under the terms of his living will during his 1959 incapacitation and used the leverage to reinstall conservative chairman Hideo Yoshida.",
        "notes": "Remains as president and CEO under Yuri Shibanokuji and Buttercup's control, an uneasy arrangement neither side has moved to end.",
    },
    {
        "name": "Jacques Barnard",
        "role": "Executive VP of Yamatetsu North America -- a mistrustful hermetic mage with a personal grudge against Buttercup and a shadow network of his own",
        "archetype": "Corporate Executive",
        "title": "Executive Vice President, Yamatetsu North America",
        "race": "Human",
        "gender": "Male",
        "organization": "Yamatetsu Corporation",
        "connection": 4,
        "description": "A hermetic mage himself, with a deep mistrust of any spirit he does not personally control; ruthless, determined and efficient.",
        "background": "Former head of Yamatetsu Seattle, now based in Kyoto but keeping close tabs on his old territory through his successor Mary Luce.",
        "notes": "Maintains a long-standing feud with Buttercup and uses underhanded means to cast her negatively wherever he can; keeps his own personal contacts in Seattle's shadow community for off-the-books operations.",
    },
    {
        "name": "Mary Luce",
        "role": "Head of Yamatetsu Seattle -- Barnard's successor, and one of the most effective shadow-asset handlers in the sprawl",
        "archetype": "Corporate Executive",
        "title": "Head, Yamatetsu Seattle",
        "race": "Human",
        "gender": "Female",
        "organization": "Yamatetsu Corporation",
        "connection": 3,
        "description": "Almost total control over Yamatetsu's Seattle activities; rumored to be at least a low-grade magical initiate.",
        "background": "Maintained and expanded Barnard's web of shadow contacts, preferring to recruit reliable runners onto Yamatetsu's full-time payroll rather than treat them as expendable.",
        "notes": "Has no particular loyalty to either faction on Yamatetsu's board, though she has inherited some of Barnard's mistrust of Buttercup.",
        "contact_skills": ["Seattle shadow community recruitment and handling"],
    },
    {
        "name": "Wu Lung-Wai",
        "role": "President/CEO of Wuxing, Inc. -- 'Hong Kong's Kingmaker', who finished his father's decades-long dream of a united Pacific Rim front against the Japanese megacorps",
        "archetype": "Corporate Executive",
        "title": "President/CEO, Wuxing, Inc.",
        "race": "Human",
        "gender": "Male",
        "nationality": "Chinese",
        "organization": "Wuxing, Inc.",
        "connection": 5,
        "description": "Brilliant, charismatic, extraordinarily shrewd; insists on face-to-face business meetings rather than telecom or Matrix conferences, which combined with unconfirmed reports of magical activity has led some to speculate he is a 'social adept'.",
        "background": "Inherited control of Wuxing from his father Wu Kuan-Lai, who founded the company and helped force Hong Kong's 2015 independence but died in 2039 without seeing his dream of a united Pacific Rim front realized.",
        "notes": "A 200-million-nuyen Dunkelzahn bequest let him finally build Wuxing into a real AAA-adjacent power and found the Pacific Prosperity Group.",
    },
    {
        "name": "Sun Runming",
        "role": "Head of Wuxing's new Seattle division -- plays the oblivious hedonist to be underestimated, and rarely misses the moment to prove it a mistake",
        "archetype": "Corporate Executive",
        "title": "Head, Wuxing Seattle Division",
        "race": "Human",
        "gender": "Male",
        "age": 58,
        "nationality": "Chinese",
        "organization": "Wuxing, Inc.",
        "connection": 3,
        "description": "A portly, cheerful man in his late fifties who has made a career of being underestimated; business meetings with him often degenerate into late-night drinking and carousing.",
        "background": "New to Seattle, setting up Wuxing's first local office.",
        "notes": "Has an almost unnatural ability to keep his head clear through the act and will pounce on any slip of the tongue his rivals make; few fall for the 'good ol' boy' routine twice.",
    },
    {
        "name": "Izu Cheng",
        "role": "Chairman of the Pacific Prosperity Group -- a gregarious Wuxing negotiator balancing giants and minnows alike to everyone's apparent satisfaction",
        "archetype": "Corporate Executive",
        "title": "Chairman, Pacific Prosperity Group",
        "race": "Human",
        "gender": "Male",
        "nationality": "Chinese",
        "organization": "Pacific Prosperity Group",
        "connection": 4,
        "description": "Gregarious and cunning; elected the PPG's first chairman and has performed admirably so far.",
        "background": "A Wuxing negotiator before taking the PPG chairmanship.",
        "notes": "Has kept the interests of large members like Yamatetsu balanced against the PPG's many smaller members with little visible internal friction so far.",
    },
    {
        "name": "Se-jong Lee",
        "role": "President/CEO of Eastern Tiger Corporation -- shrewd but cautious, giving the Pacific Prosperity Group little more than lip service",
        "archetype": "Corporate Executive",
        "title": "President/CEO, Eastern Tiger Corporation",
        "race": "Human",
        "gender": "Male",
        "nationality": "Korean",
        "organization": "Eastern Tiger Corporation",
        "connection": 3,
        "description": "Swift to seize an opportunity, sometimes too quick to cut and run if it turns sour.",
        "background": "Built Eastern Tiger's rapid post-2050 expansion into Australia, Brunei, the Salish-Shidhe Council, Seattle and Hawai'i.",
        "notes": "Carries real grudges against Renraku and Mitsuhama for foiling past expansion plans, which might yet push him to back the PPG harder than his caution otherwise would.",
    },
    {
        "name": "Jessica Sirianni",
        "role": "President/CEO of Federated Boeing -- self-made from an Auburn childhood watching Fed-Boeing's planes overhead, now petitioning to join the Pacific Prosperity Group out of spite for Mitsuhama",
        "archetype": "Corporate Executive",
        "title": "President/CEO, Federated Boeing",
        "race": "Human",
        "gender": "Female",
        "organization": "Federated Boeing",
        "connection": 4,
        "description": "A self-made workaholic with a reputation for ruthlessness in business and personal dealings alike; a hands-on manager unafraid to break the rules when it benefits her or her company.",
        "background": (
            "Born in the poorest part of Auburn; taught herself enough from stolen books and "
            "compassionate teachers to reach Seattle Central Community College, paid her own way through "
            "an aerospace engineering degree at the University of Washington, and rose from draftswoman "
            "through director of aircraft weaponry and director of Auburn operations to the top job in "
            "late 2057, after a power struggle with predecessor William Yourel."
        ),
        "notes": "Keeps a wide range of shady connections, some predating her Fed-Boeing career.",
    },
    {
        "name": "Jae-Myung Kim",
        "role": "President of Kwonsham Industries -- building a multinational he can hand to his son, one Seattle trip at a time",
        "archetype": "Corporate Executive",
        "title": "President, Kwonsham Industries",
        "race": "Human",
        "gender": "Male",
        "age": 52,
        "nationality": "Korean",
        "organization": "Kwonsham Industries",
        "connection": 3,
        "description": "A stable man in his early fifties, wholeheartedly embracing the Pacific Prosperity Group as his route to real multinational status.",
        "background": "Made numerous recent trips to Seattle laying groundwork for a UCAS-based Kwonsham transportation division.",
        "notes": "Unconfirmed rumors place him meeting with representatives of the Choson Seoulpa Ring during several of those trips.",
    },
    {
        "name": "Toshio Mitsukuri",
        "role": "President/COO of Monobe International -- pulled off a boardroom coup, and his ousted predecessor's plane vanished shortly after",
        "archetype": "Corporate Executive",
        "title": "President/COO, Monobe International",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Monobe International",
        "connection": 4,
        "description": "A bloodthirsty reputation the rest of Monobe's board is walking on eggshells to avoid confirming.",
        "background": "Pulled off a coup as chief operating officer in January 2059, replacing most of Monobe's executive officers within a week of taking the presidency from Sho Kubota.",
        "notes": "Kubota sold his stock and headed for a retirement in Sri Lanka; his private plane disappeared from radar mid-flight and he has not been heard from since. Mitsukuri has never so much as hinted at involvement.",
    },
    {
        "name": "Sau-hok Chu",
        "role": "President/CEO of Tan Tien, Inc. -- enigmatic, reclusive, and respected enough that other Chinese corporations follow wherever he aligns",
        "archetype": "Corporate Executive",
        "title": "President/CEO, Tan Tien, Inc.",
        "race": "Human",
        "gender": "Male",
        "nationality": "Chinese",
        "organization": "Tan Tien, Inc.",
        "connection": 4,
        "description": "Enigmatic and reclusive, but among the most respected business leaders in the Chinese Republic; other Chinese corporations often use Tan Tien's moves as a guideline for their own.",
        "background": "Aligned Tan Tien with Wuxing and the Pacific Prosperity Group, prompting several other Chinese corporations to follow suit.",
        "notes": "Astrally projects into Seattle to consult, in secret, with restaurant owner Enric Wong -- widely rumored among Wong's shadowy and corporate clientele to be an 'ancient Chinese ghost' Wong summons (see Ancient Chinese Secret, Huh?, NOT_BUILT).",
    },
    {
        "name": "Hiroshi Yakashima",
        "role": "President/CEO of Yakashima Technologies -- Japan's self-styled 'hostile-takeover king', freshly emboldened by Yamatetsu's exit",
        "archetype": "Corporate Executive",
        "title": "President/CEO, Yakashima Technologies",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Yakashima Technologies",
        "connection": 3,
        "description": "Takes particular, visible pleasure in laying off metahuman workers from newly acquired ex-Yamatetsu subsidiaries.",
        "background": "Built Yakashima into a compact, efficient corporate empire through insight and dirty tricks before Yamatetsu's and Ares' takeover attempts stunted its growth for years.",
        "notes": "Now framing Yakashima's acquisitions as a fight for 'human purity' in its PR, playing well with Japan's post-Yamatetsu human public.",
    },
    {
        "name": "Jean-Claude Priault",
        "role": "Saeder-Krupp's Zurich-Orbital liaison -- the man Lofwyr trusts to phone in bad news, and the Prologue's viewpoint character",
        "archetype": "Corporate Executive",
        "title": "Zurich-Orbital Personnel Director, Saeder-Krupp Heavy Industries",
        "race": "Human",
        "gender": "Male",
        "nationality": "French",
        "organization": "Saeder-Krupp Heavy Industries",
        "connection": 3,
        "description": (
            "A man who can survey the entire Earth from his small, spartan Zurich-Orbital office -- a "
            "plain desk, a telecom, one comfortable chair, a few carefully chosen paintings -- and still "
            "loses himself in the view after years in orbit. Calls Lofwyr 'master' without shame or "
            "sarcasm, the way a sergeant might call a general 'sir'; he would never use the word for "
            "another human being. 'Not well, master,' he reports, taking a deep breath first, as he "
            "always does before delivering bad news."
        ),
        "background": (
            "Responsible for all Saeder-Krupp personnel aboard Zurich-Orbital; prefers the discomfort of "
            "life in the station to the alternative on Earth, telling himself it is the view, though he "
            "suspects it is really the perspective -- the reminder that some things (dragons among them) "
            "are more powerful than any man, corporation, or vacuum-hardened space station."
        ),
        "notes": (
            "Opens the book (15 Aug 2059) reporting to Lofwyr that Wuxing's Li Feng won the Corporate "
            "Court seat left by David Hague's death, and that one of Saeder-Krupp's own electors "
            "apparently voted against orders -- only to learn from Lofwyr that the 'betrayal' was staged "
            "misdirection all along. 'You have done admirably well,' Lofwyr tells him. 'I didn't say I "
            "didn't want him elected.'"
        ),
    },
    {
        "name": "Lofwyr",
        "role": "Great Western Dragon, CEO of Saeder-Krupp Heavy Industries -- opens the book manipulating a Corporate Court vote from Earth orbit and closes Track 2 erasing evidence of Leonardo's Iran hideout",
        "archetype": "Great Dragon",
        "title": "President/CEO, Saeder-Krupp Heavy Industries",
        "race": "Dragon",
        "gender": "Male",
        "connection": 6,
        "description": (
            "Speaks over the telecom in his assumed human form, his voice 'like liquid amber'; shows no "
            "concern, only mild interest, in nearly everything -- Lofwyr's emotions always appear mild, "
            "except for rage, which 'could shake down Everest.' Takes obvious pleasure in a clever plan "
            "well executed: 'I apologize for the deception, Jean-Claude, but you are always at your most "
            "eloquent when you honestly believe in what you are saying.'"
        ),
        "background": (
            "One of the Great Dragons and Saeder-Krupp's controlling shareholder and CEO; his machinations "
            "in the corporate war are worked from behind a human face and a telecom line, never in person "
            "in this book."
        ),
        "notes": (
            "Prologue (15 Aug 2059): engineered his own Corporate Court electors' apparent 'betrayal' -- "
            "voting to seat Wuxing's Li Feng despite public Saeder-Krupp opposition -- to make Japan trust "
            "Saeder-Krupp as an ally, bait Aztechnology and Ares into a vote he wanted them to make anyway, "
            "and sow suspicion of internal dissent among his rivals. Separately hired Abu Khalid's "
            "Blackscarf Revolutionaries to raze an abandoned Renraku research observatory near Altyar, "
            "Iran, erasing evidence of the vanished elf decker Leonardo's presence there (see What Does a "
            "Ten-Thousand-Year-Old Dragon Get?, PLAY_NOTES)."
        ),
    },
    {
        "name": "David Hague",
        "role": "Fuchi's Corporate Court justice, a Yamana loyalist -- died in the Flight 1118 crash that conveniently silenced him, and stayed missing for a week afterward",
        "archetype": "Corporate Executive",
        "title": "Corporate Court Justice, Fuchi Industrial Electronics",
        "race": "Human",
        "gender": "Male",
        "connection": 4,
        "description": "A Fuchi justice on the Corporate Court, aligned with the Yamana faction against Richard Villiers' growing independence.",
        "background": (
            "Boarded the ill-fated semiballistic Flight 1118 from Tokyo in July 2059, apparently suspected "
            "by Richard Villiers of knowing too much about Villiers' plans to secede from Fuchi. The "
            "flight crashed into the Redmond Barrens; Hague's body was not found among the wreckage."
        ),
        "notes": (
            "His body turned up a week later in an abandoned Redmond apartment building, minus its "
            "cyberware headware memory -- taken, along with his Corporate Court briefcase, by a fake "
            "'DocWagon' team that was really Renraku operatives working the crash site the night it "
            "happened. His death left Fuchi's other Corporate Court seat, held by Villiers ally Lynn "
            "Osborne, unopposed inside the corp, and handed Wuxing's Li Feng the vacated seat outright. "
            "Yamana and Nakatomi both suspected Villiers of arranging the crash; no proof ever surfaced. "
            "See Crash Team, PLAY_NOTES, and Flight 1118 Crash Site, LOCATIONS."
        ),
    },
    {
        "name": "Leonardo",
        "role": "Vanished elf decker genius whose secret deal briefly made Renraku's Matrix technology untouchable -- his disappearance is the mystery both Track 2 and a great dragon chase across two continents",
        "archetype": "Decker",
        "title": "Independent decker; formerly Renraku's secret technology source",
        "race": "Elf",
        "gender": "Male",
        "connection": 5,
        "description": (
            "Erratic but undeniably brilliant; took his working name from the fifteenth-century polymath "
            "and pursued a mysterious, staggeringly expensive project he called his 'Great Work.' Nobody "
            "outside Renraku's inner circle, and now perhaps not even they, know what he actually looks "
            "like or where he has gone."
        ),
        "background": (
            "In mid-2057, launched blackmail attacks against every AAA megacorp simultaneously, "
            "penetrating their most secure Matrix systems without ever tripping an alarm, to fund his "
            "Great Work. A Renraku agent finally traced the attacks to him; confronted, Leonardo offered "
            "Renraku CEO Inazo Aneki a trade -- technological breakthroughs in exchange for funding -- and "
            "Aneki took the deal. For about two years Leonardo's tech, much of it beyond even Renraku's "
            "own technicians' understanding, powered Renraku's sudden leap past Mitsuhama and into Fuchi's "
            "traditional markets."
        ),
        "notes": (
            "Vanished the same week in June 2059 that a Corporate Court ruling forced Miles Lanier back "
            "into Fuchi's custody -- taking his technology's underlying secrets with him and leaving "
            "gaping, unexplained holes in Renraku's own databases (including the public SeaSource). The "
            "great dragon Hestaby, his ally, hires runners to find him after tracing his last known "
            "location to a research observatory near Altyar, Iran -- destroyed by Lofwyr's hired "
            "mercenaries before they arrive. The trail ends with an unbreakable encrypted optical chip "
            "and a Renraku courier's data-locked headware, fought over by Hestaby's agents and the Tir "
            "Ghosts alike. See What Does a Ten-Thousand-Year-Old Dragon Get?, PLAY_NOTES."
        ),
    },
    {
        "name": "Diana Peng",
        "role": "Renraku's undercover agent inside the Beamwalkers otaku tribe -- came back from the Matrix's 'Deep Resonance' with her mind in ruins and an obsessive need to touch a cyberdeck",
        "archetype": "Security Agent",
        "title": "Undercover Security Agent, Renraku Computer Systems",
        "race": "Human",
        "gender": "Female",
        "age": 20,
        "organization": "Renraku Computer Systems",
        "connection": 1,
        "description": (
            "A third-generation Renraku employee on paper a data-entry clerk in the Seattle arcology's "
            "security division; in reality an undercover specialist. After the Deep Resonance leaves her "
            "with severe brain damage, she takes no notice of the world around her, staring into space "
            "and humming quietly to herself -- unless she sees a cyberdeck, at which point she goes wild, "
            "screaming 'Back! Back! Back!' at the top of her lungs. Asked a direct question, patiently, "
            "she will only answer, eagerly, 'Back?'"
        ),
        "background": (
            "Sent into the Beamwalkers otaku tribe months before this book's present as part of a Renraku "
            "program to learn the secrets of the otaku phenomenon; earned the tribe's trust well enough to "
            "be sent into the Matrix to seek the 'Deep Resonance' as her final initiation."
        ),
        "notes": (
            "The Spirit of the Matrix, or whatever met her there, left her with severe, permanent brain "
            "damage and no memory of what happened; Renraku hid her at the Stasky Institute in Tacoma "
            "under the alias 'Olivia Tang' to keep the Beamwalkers from tracing the failed operation back "
            "to them. She carries a high-quality datajack (epoxy-stoppered) and a retractable forearm "
            "spur she seems totally unaware of. The Beamwalkers, having tagged her headware during the "
            "Deep Resonance attempt, track her the whole time she is held and eventually reclaim her. "
            "Later glimpsed disappearing into the Renraku arcology's mall, regardless of whose custody she "
            "ended the adventure in -- the otaku 'apparently still find her useful.'"
        ),
    },
    {
        "name": "HAL",
        "role": "Freelance decker who ran afoul of Fuchi's prototype truth-serum black IC -- now compulsively confessing every secret he has ever kept, including everyone else's",
        "archetype": "Decker",
        "title": "Freelance decker",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": (
            "Normally friendly but quiet; under the IC's effect he talks up a storm, loudly and in public, "
            "about programs he's written, systems he's seen, and finally the details of an illegal Fuchi "
            "run in San Francisco -- including exactly how much nuyen he skimmed. Asked what's wrong, he "
            "answers, helplessly, 'I can't seem to stop myself. Which reminds me of the time we sabotaged "
            "that Aztechnology munitions factory back in '54...'"
        ),
        "background": "A freelance decker who has worked with almost every shadowrunner in town at one time or another.",
        "notes": (
            "Infected by Fuchi Asia's prototype psychotropic black IC, code-named 'Stoolie', during an "
            "illegal run on a Fuchi host in San Francisco; the IC works like a truth serum, but far more "
            "thoroughly, stripping away any interest in keeping secrets at all, no matter the personal "
            "cost. Fuchi Asia wants him silenced before he can spill their internal plans; Fuchi Americas "
            "and Pan-Europa want him alive to debrief; and every runner he has ever worked with, or "
            "burned, wants him quiet before he names names. A counter-program exists on the same host he "
            "was infected from, trapped behind trace IC. See Loose Lips Fry Chips, PLAY_NOTES."
        ),
    },
    {
        "name": "Craig Sanchez",
        "role": "Alcoholic ork who unknowingly knows Buttercup's true name -- the one loose end from her humbling by Dunkelzahn that she still needs tied off",
        "archetype": "Drifter",
        "title": "Recipient of a Dunkelzahn trust fund; unemployed",
        "race": "Ork",
        "gender": "Male",
        "age": 36,
        "connection": 1,
        "description": (
            "Old and debilitated by years of alcohol dependence; offers little resistance to anyone who "
            "comes for him. Lives out of an unwashed, liquor-bottle-strewn apartment on automatic rent "
            "payments and 100-nuyen-a-day spending limits from a trust fund he barely understands the "
            "source of."
        ),
        "background": (
            "Was once, briefly, a young unschooled human when Dunkelzahn bound the free spirit Buttercup "
            "into his body for a year and a day to teach her humility about mortal life; when the ritual "
            "ended, Dunkelzahn gave the ork a new identity as 'Craig Sanchez', a SIN, and a sizable trust "
            "fund from a shell called Libra Holdings, then let him go. The binding left Sanchez knowing "
            "Buttercup's true name -- he never realized its significance, and never told anyone."
        ),
        "notes": (
            "Dunkelzahn's will left him a magical pendant meant to shield him from Buttercup's attempts to "
            "find him, but Sanchez lost it when he was evicted from an earlier apartment. Buttercup, "
            "having finally traced him to Seattle, hires runners to bring him somewhere safe and "
            "permanently silent (not dead) about her name; Jacques Barnard, hearing of the search, sends "
            "his own mage, Caldwell, to grab Sanchez first and use him as leverage -- or, once Caldwell "
            "learns what Sanchez actually knows, to bind Buttercup himself. See What's in a Name?, "
            "PLAY_NOTES."
        ),
    },
    {
        "name": "Caldwell",
        "role": "Arrogant Yamatetsu mage sent to grab Craig Sanchez for Jacques Barnard -- and who decides, on learning why Sanchez matters, to double-cross his own boss and bind Buttercup for himself",
        "archetype": "Mage",
        "title": "Field Operative, Yamatetsu Corporation",
        "race": "Human",
        "gender": "Male",
        "organization": "Yamatetsu Corporation",
        "connection": 2,
        "description": "Polite but pointed threats over demands: wants to know who the runners work for and why they're after Sanchez, and will suggest they hand over any evidence before things turn unpleasant -- though he won't start a fight unless his side outnumbers them.",
        "background": "Leads the Yamatetsu enforcement team Jacques Barnard sends after learning that Buttercup wants a 'nonstandard operative' recovered from Seattle.",
        "notes": (
            "Mind-probes Sanchez en route to a safehouse and discovers he knows Buttercup's true name -- "
            "and immediately decides to betray Barnard and bind the free spirit himself, spending ten "
            "hours preparing a hermetic circle and downloading Yamatetsu's conjuring library at a nearby "
            "warehouse. If the ritual succeeds before the runners stop him, he briefly controls Buttercup "
            "outright; if he dies mid-fight, she is freed and rewards the runners with 30,000 nuyen each "
            "-- and a dose of laes to erase their memory of the ritual and her true name."
        ),
    },
    {
        "name": "Eve Aurelius ('Eve Night')",
        "role": "Leonard Aurelius's rebellious daughter, lead guitarist for the Unholy Machine -- stole Damien Knight's Dunkelzahn-bequeathed chess piece to spite her father and use as a pretext to date Knight",
        "archetype": "Rocker",
        "title": "'Eve Night' -- lead guitarist, the Unholy Machine",
        "race": "Human",
        "gender": "Female",
        "organization": None,
        "connection": 2,
        "description": (
            "Taking full advantage of her father's absence to fool around at his mansion with her "
            "boyfriend rather than mind his household; never learned to play chess and has to take a "
            "crash course from an elf squatter at a hipster cafe so she can use the stolen king piece to "
            "get a date -- and a rise -- out of Damien Knight."
        ),
        "background": "Leonard Aurelius's daughter, from his Ares years; plays lead guitar for a local band, the Unholy Machine, and dates Detroit Nightmares urban brawl player Two-Chord Teddy.",
        "notes": (
            "Stole the black king piece Aurelius left behind in his old Ares office -- the half of "
            "Dunkelzahn's antique chess set Aurelius inherited, the white pieces having gone to Damien "
            "Knight -- purely to needle her father, then decided using it to bait a chess date with Knight "
            "would needle him even more. Refuses to surrender the piece to the runners hunting it on "
            "Aurelius's orders unless they help her set up the game; brings Knight a duplicate rather than "
            "the real piece, a fraud easy to spot up close but unlikely to be noticed mid-firefight. See "
            "Knight's Gambit, PLAY_NOTES."
        ),
    },
    {
        "name": "Two-Chord Teddy",
        "role": "Detroit Nightmares urban brawl player and Eve Aurelius's boyfriend -- unwittingly carries the real stolen chess piece in his coat pocket",
        "archetype": "Athlete",
        "title": "Player, Detroit Nightmares (Urban Brawl)",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": "Plays for the Detroit Nightmares urban brawl team; takes up chess as a new hobby on a trid interview, unaware he is carrying the very piece his girlfriend stole.",
        "background": "",
        "notes": "Eve hides Dunkelzahn's stolen black king in Teddy's coat pocket during the runners' raid on the Aurelius estate; his casual trid-interview mention of a new chess hobby is one of the few clues that points the runners toward Eve.",
    },
    {
        "name": "Raymond Briggs",
        "role": "VP of Ares Seattle's Consumer Electronics division -- extracted from Ares by Cross Applied Technologies at the same moment his own father defects in Detroit",
        "archetype": "Corporate Executive",
        "title": "Vice President, Consumer Electronics, Ares Seattle",
        "race": "Human",
        "gender": "Male",
        "organization": "Ares Macrotechnology",
        "connection": 3,
        "description": "Young and fit by management standards, a few years on Ares' competitive tae kwon do team behind him; fights his own extraction surprisingly well for a civilian before the runners subdue him.",
        "background": (
            "Son of Ares Global Entertainment executive VP William Briggs, who is defecting to Cross "
            "Applied Technologies alongside Leonard Aurelius and needs his son pulled out of Ares Seattle "
            "before Damien Knight's people can retaliate against him for it."
        ),
        "notes": (
            "Has been secretly married six months to an ork wife he never told his father about, certain "
            "William would disapprove; breaks his Platinum DocWagon wristband mid-extraction to summon a "
            "High Threat Response team, nearly blowing the runners' cover. Insists on joining the follow-"
            "up raid to rescue his wife from Ares housing, guided by Seraphim bodyguard Goliath. Becomes "
            "the new head of Cross Advanced Electronics regardless of how the runners' fight with a rival "
            "Novatech extraction team turns out. See Double Crossover, PLAY_NOTES."
        ),
    },
    {
        "name": "William Briggs",
        "role": "Executive VP of Ares Global Entertainment, defecting to Cross Applied Technologies alongside Leonard Aurelius -- and pulling his son out first",
        "archetype": "Corporate Executive",
        "title": "Executive Vice President, Ares Global Entertainment",
        "race": "Human",
        "gender": "Male",
        "organization": "Ares Macrotechnology",
        "connection": 2,
        "description": "Cannot risk telling his son Raymond about his own defection ahead of time, for fear Knight's people intercept the warning; arranges the extraction through back channels instead.",
        "background": "Following his old friend Leonard Aurelius from Ares to Cross Applied Technologies in Detroit.",
        "notes": (
            "Supplies Jezebel Surrateau's runner team with Matrix back doors into Ares' Bellevue office "
            "building and its executive monorail; becomes a special consultant to Cross Entertainment and "
            "Multimedia once his own defection and his son's extraction both succeed, bringing profitable "
            "contracts with him. See Double Crossover, PLAY_NOTES."
        ),
    },
    {
        "name": "Sebastien Hull",
        "role": "Quebec City's chief of police -- a staunch Cross Applied Technologies supporter whose testimony could sink Damien Knight's zoning bid, if he reaches the council meeting in time",
        "archetype": "Police Official",
        "title": "Chief of Police, Quebec City",
        "race": "Human",
        "gender": "Male",
        "nationality": "Quebecois",
        "connection": 3,
        "description": (
            "Cannot vote on the City Council himself but wields enough influence over its aldermen that "
            "they almost always follow his lead; rides in a well-armored, well-armed Rolls Royce Phaeton "
            "limousine with a combat rigger, four personal bodyguards (two trolls, a physical adept and a "
            "mage), and a four-gendarme escort that doesn't stop for traffic lights."
        ),
        "background": "A staunch Cross Applied Technologies supporter; if he learns Damien Knight secretly controls Quick Trigger Systems, his word alone could sway the council's zoning vote against it.",
        "notes": "Not It My Backyard: Knight sends runners to keep Hull from reaching the council meeting before its 10:15 a.m./11 a.m. deadline (the book states both times), by any means short of killing Quebec's own police chief in the street.",
    },
    {
        "name": "Dieter Arkona",
        "role": "Rich elf holdout shareholder standing between Renraku and control of the German water-tech firm Wasserkraft -- has told both Fuchi and Renraku to frag off",
        "archetype": "Corporate Shareholder",
        "title": "Major Shareholder, Wasserkraft",
        "race": "Elf",
        "gender": "Male",
        "nationality": "German",
        "connection": 3,
        "description": "A strong-willed man with powerful friends, unwilling to accept Renraku's takeover attempt lying down; has told both Renraku and Fuchi to frag off rather than sell.",
        "background": "Holds the last major independent shareholding in Wasserkraft, a Fuchi Pan-Europa subsidiary Renraku is trying to absorb.",
        "notes": (
            "Protected by connections including the rulers of the Grand Duchy of Pomorya and Klabauterbund, "
            "a policlub tied to GreenWar and a band of North Sea pirates; has camouflaged any real "
            "skeletons well enough that runners hired to pressure him may need to manufacture a "
            "compromising situation rather than find one. Will ambush the runners himself if pushed too "
            "hard, and will sell to Fuchi out of pure spite if Renraku's pressure gets truly desperate. "
            "See The Squeeze, PLAY_NOTES."
        ),
    },
    {
        "name": "Dimitri Makaroff",
        "role": "Tacoma's Vary v Zakone boss -- hunting proof of a yakuza schism to blackmail his way into part of the Watada-rengo's Tacoma rackets",
        "archetype": "Crime Boss",
        "title": "Boss (avtoritet), Vary v Zakone",
        "race": "Human",
        "gender": "Male",
        "nationality": "Russian",
        "organization": "Vary v Zakone",
        "connection": 4,
        "description": "Watching the growing Russkin trade between Tacoma and Vladivostok for every opportunity it opens.",
        "background": "Learned that Tacoma yakuza oyabun Hanzo Shotozumi is secretly planning to break away from the Watada-rengo and found his own independent league.",
        "notes": (
            "Hires runners for surveillance and infiltration work trying to nail down proof of Shotozumi's "
            "plans, hoping to blackmail him into ceding choice Tacoma rackets to the Vary v Zakone rather "
            "than risk exposure; loses that leverage once Shotozumi splits publicly, but gains an opening "
            "to ally with Shotozumi's new rivals inside the old Watada-rengo structure instead. See Mob "
            "Clash, PLAY_NOTES."
        ),
    },
    {
        "name": "Enric Wong",
        "role": "Owner of Seattle's Lee Chee Garden restaurant -- long rumored to consult an 'ancient Chinese ghost' who is really Tan Tien's CEO, astrally projecting in from Beijing",
        "archetype": "Restaurateur",
        "title": "Owner, Lee Chee Garden",
        "race": "Human",
        "gender": "Male",
        "nationality": "Chinese",
        "connection": 3,
        "description": "Trusted as a neutral party by his many shadowy and corporate regulars, who use his soundproof back room for meetings they would rather nobody overhear.",
        "background": "Half-brother to Tan Tien's reclusive CEO Sau-hok Chu, a fact he has kept carefully hidden even from his closest customers.",
        "notes": (
            "Secretly records the back-room conversations his customers trust him to keep private, feeding "
            "the intelligence back to Chu, who consults with him astrally under cover of the 'ancient "
            "Chinese ghost' rumor. Abducted by Mitsuhama operatives who learned of the arrangement and want "
            "to blackmail Chu into pulling Tan Tien out of the Pacific Prosperity Group; his 'cousin' -- "
            "really another Tan Tien operative -- hires runners to recover him. See Ancient Chinese Secret, "
            "Huh?, PLAY_NOTES."
        ),
        "contact_skills": ["Shadow and corporate gossip overheard at Lee Chee Garden"],
    },
    {
        "name": "David Gao",
        "role": "Octagon Triad leader worried his own men are dying for breaking their initiation oaths -- and unwittingly stumbling toward an Atlantean Foundation trap",
        "archetype": "Crime Boss",
        "title": "Leader, Octagon Triad",
        "race": "Human",
        "gender": "Male",
        "nationality": "Chinese",
        "connection": 3,
        "description": "Worried enough by two Triad members' sudden, horrible deaths to bring in outside help rather than let the matter go unexamined.",
        "background": "Concludes both deaths were the price of broken initiation oaths -- his own men betraying the Triad in some way he cannot yet identify.",
        "notes": (
            "Hires runners to find out what the two victims were doing and how they betrayed him; the "
            "trail leads to Mystic Crusaders of the Atlantean Foundation using Triad members to lure "
            "Wuxing geomancer Chao Su-Cheng into a trap over a scroll of geomantic wisdom. See Tome "
            "Raiders, PLAY_NOTES."
        ),
    },
    {
        "name": "Chao Su-Cheng",
        "role": "Wuxing geomancer overseeing the renovation of its new Seattle offices -- and, quietly, a Triad member in contact with an Octagon Triad wizard",
        "archetype": "Geomancer",
        "title": "Geomancer, Wuxing, Inc. (Seattle)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Chinese",
        "organization": "Wuxing, Inc.",
        "connection": 2,
        "description": "Brought to Seattle specifically to oversee the feng shui and geomantic renovation of Wuxing's new local offices.",
        "background": "A Triad member himself, in quiet contact with Octagon Incense Master Chen Kwan-Ti.",
        "notes": "Lured by the Atlantean Foundation's Mystic Crusaders, using Triad intermediaries, to a fake meeting meant to draw out a geomantic scroll he possesses -- a source of real geomantic wisdom the Crusaders intend to steal and study. See Tome Raiders, PLAY_NOTES.",
    },
    {
        "name": "Wu Kuan-Lai",
        "role": "Wuxing's founder -- helped force Hong Kong's independence from China, then spent decades chasing a united Pacific Rim front against the Japanese megacorps he never lived to see",
        "archetype": "Corporate Executive",
        "title": "Founder, Wuxing, Inc.",
        "race": "Human",
        "gender": "Male",
        "nationality": "Chinese",
        "connection": 3,
        "description": "A corporate maverick whose ambition did not stop with Hong Kong's independence.",
        "background": (
            "A major force in forming the Hong Kong Corporate Directorate during Hong Kong's 2015 "
            "independence push, forging alliances strong enough to withstand China's attempts to reclaim "
            "the colony -- and, once free of Beijing, still constrained by the Japanese megacorps' "
            "stranglehold on the Pacific Rim. Spent the rest of his life quietly courting other Pacific Rim "
            "businesses toward a united front capable of standing up to Fuchi, Mitsuhama, Renraku and "
            "Shiawase."
        ),
        "notes": "Died in 2039 without seeing his dream realized; his son Wu Lung-Wai finally built the Pacific Prosperity Group two decades later, with a Dunkelzahn bequest Wu Kuan-Lai never lived to see either.",
    },
    {
        "name": "Tadamako Shibanokuji",
        "role": "Yamatetsu's chairman until his 2059 death -- a man whose secret goblinized son and buried guilt over abandoning him set Yamatetsu's flight from Japan in motion",
        "archetype": "Corporate Executive",
        "title": "Chairman of the Board, Yamatetsu Corporation (deceased)",
        "race": "Human",
        "gender": "Male",
        "age": 84,
        "organization": "Yamatetsu Corporation",
        "connection": 4,
        "description": (
            "Publicly a conservative, traditionalist voice on Yamatetsu's board for decades; privately "
            "carried a guilt he confided to no one, and in his final years began quietly voting to support "
            "the board's pro-metahuman reform faction, to the confusion of everyone who did not know why."
        ),
        "background": (
            "As a young division manager for his father's shipping company, Tsuruga International, fell "
            "in love with a Vladivostok port official named Tatiana Trigorin and married her; when their "
            "son goblinized into an ork during the birth pangs of UGE, Tadamako -- fighting for control of "
            "Tsuruga's board after his own father's death, and unable to risk a metahuman son as ammunition "
            "for his corporate enemies -- sent the boy back to Russia with his mother rather than surrender "
            "him to the newly formed kawaruhito camps. Tatiana never forgave him and their divorce, years "
            "later, was a formality. He never spoke of his son's condition to anyone again, and for years "
            "voted anti-metahuman on Yamatetsu's board to prove to himself that his conscience was clear."
        ),
        "notes": (
            "Suffered a debilitating stroke on 7 January 2059, leaving CEO Saru Iwano to vote his shares "
            "under his living will and hand the board's conservative faction effective control; died six "
            "weeks later without recovering his power of speech. His shares reverted to his son Yuri, who "
            "defied everyone's expectation that he would simply cash out. Buttercup, who had known his "
            "secret for years, is directly responsible for his death -- having a Yamatetsu nurse, possessed "
            "or coerced, administer a fatal injection rather than let the anti-metahuman faction keep "
            "control of his voting stock (see The Needle and the Damage Done, PLAY_NOTES)."
        ),
    },
    {
        "name": "Goliath",
        "role": "Seraphim bodyguard sent along on the Raymond Briggs extraction to keep him safe and keep Seattle and Detroit events in sync",
        "archetype": "Street Samurai",
        "title": "Field Agent, the Seraphim",
        "race": "Amerindian",
        "gender": "Male",
        "organization": "Cross Applied Technologies, Inc.",
        "connection": 2,
        "description": "An Amerindian street samurai fielded by Jezebel Surrateau specifically to shadow Raymond Briggs through his own extraction.",
        "background": "One of Surrateau's Seraphim operatives.",
        "notes": "Insists on accompanying Raymond back into Ares housing to rescue his wife, acting as his personal bodyguard through the second half of Double Crossover, PLAY_NOTES.",
    },
    {
        "name": "Kiyoshi Nakatomi",
        "role": "Fuchi's murdered co-founder -- vetoed Richard Villiers' original cyberdeck-technology deal and was dead within three days",
        "archetype": "Corporate Executive",
        "title": "Head, Dekita Industries / Fuchi Asia (deceased)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "connection": 3,
        "description": "CEO of Dekita Industries before its 2011 merger with Yamana Electronics formed Fuchi Industrial Electronics.",
        "background": (
            "Used his controlling stake in Fuchi to veto Richard Villiers' original offer of Matrix "
            "Systems' stolen cyberdeck technology in exchange for a third of the company, remembering all "
            "too well how a similar deal with Korin Yamana had cost him control of Dekita years before."
        ),
        "notes": "Murdered by his own limousine driver three days after the veto; the driver was killed before he could be brought to trial. Villiers renewed the offer to Kiyoshi's son and heir Shikei Nakatomi, who accepted -- and observers have suspected Villiers' hand in the killing ever since, without proof.",
    },
    {
        "name": "Nicholas Aurelius",
        "role": "Ares Macrotechnology's founder -- built a corporate empire on the ruins of the U.S. space program and cast a shadow his son Leonard never fully escaped",
        "archetype": "Corporate Executive",
        "title": "Founder, Ares Industries / Ares Macrotechnology (deceased)",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": "A wealthy Detroit businessman perceived as a gambler whose gambles usually won big.",
        "background": (
            "Consolidated a variety of Detroit-area holdings into Ares Industries in 2002 after the 2001 "
            "Shiawase decision granted large corporations extraterritoriality, then bought the entire U.S. "
            "space program from a cash-strapped UCAS government in 2016, salvaging derelict satellites and "
            "orbital equipment for profit and building the foundation of AresSpace."
        ),
        "notes": "Died shortly after retiring from day-to-day leadership; his son Leonard Aurelius spent decades trying to live up to his legacy before an explosive argument with his own daughter finally pushed Leonard to let it go.",
    },
]

ORG_UPDATES = {
    "Transys Neuronet": {
        "leadership_add": [
            {"name": "Liam Riley", "title": "President/CEO", "notes": "Blood in the Boardroom: HKB-appointed board member since 2053, maneuvered into the presidency in 2058; market analysts reserve judgment on where HKB's real agenda is headed."},
        ],
        "notes_append": (
            "Blood in the Boardroom: fell behind Renraku's Leonardo-fueled Matrix leap and has since "
            "pivoted its flagship Caerleon, Wales research facility toward viable Matrix connections for "
            "dragons, satyrs and other paranormal creatures. Uses Fuchi's internal chaos and Renraku's "
            "setbacks to poach technology, planting a runner team with forged Fuchi Asia scientist "
            "credentials to loot a Fuchi Asia facility (see Transys Neuromess, PLAY_NOTES)."
        ),
        "enemies_add": ["Renraku Computer Systems"],
    },
    "Ares Macrotechnology": {
        "leadership_add": [
            {"name": "Damien Knight", "title": "President/CEO", "notes": "Blood in the Boardroom: still holds Ares through decades of boardroom maneuvering against Leonard Aurelius's faction; ordered the 1958 Strain III-Beta clearance of the Chicago insect-spirit Containment Zone."},
            {"name": "Arthur Vogel", "title": "Board member", "notes": "Blood in the Boardroom: Dunkelzahn's will seat; bought Leonard Aurelius's Ares stock in 2059, giving him a marginal edge over Knight's own holdings."},
            {"name": "Karen King", "title": "Supervising Vice President, Ares Seattle", "notes": "Blood in the Boardroom: locked in an ongoing local proxy war against Cross Applied Technologies' Seattle division."},
        ],
        "notes_append": (
            "Blood in the Boardroom: Ares' long cold war with Cross Applied Technologies (CATCo) went "
            "hot in 2059 when Leonard Aurelius sold his Ares stock to buy into CATCo, giving Lucien "
            "Cross both cash and thirty years of insider knowledge of Damien Knight. Ares Seattle "
            "(Karen King) and CATCo's Seattle Seraphim (Jezebel Surrateau) are running an active shadow "
            "proxy war for local market share. Ares' Chicago 'Operation Extermination' (Feb 1958) is "
            "widely credited with clearing the insect-spirit Containment Zone, though rumors persist "
            "that some spirits escaped the blockade unnoticed."
        ),
        "enemies_add": ["Cross Applied Technologies, Inc."],
    },
    "Aztechnology": {
        "notes_append": (
            "Blood in the Boardroom (15 Dec 2059): Anna Villalobos replaced Dominga Chavez as "
            "Aztechnology's representative on the Corporate Court."
        ),
    },
    "Fuchi Industrial Electronics": {
        "leadership_add": [
            {"name": "Richard Villiers", "title": "President/CEO (through Oct 2059)", "notes": "Blood in the Boardroom: head of Fuchi Americas; left to found Novatech, Inc. in Oct 2059, selling off the rest of his Fuchi stock at a huge profit."},
            {"name": "Korin Yamana", "title": "President/CEO (Oct 2059-Jul 2060, nominal)", "notes": "Blood in the Boardroom: last of Fuchi's three founding families still standing; sold what remained of the corp to Shiawase Corporation and joined its board."},
            {"name": "Shikei Nakatomi", "title": "Head, Fuchi Asia (until Apr 2060)", "notes": "Blood in the Boardroom: lost the internal power struggle to Yamana, then took Fuchi Asia's remaining assets into Renraku Computer Systems."},
            {"name": "Miles Lanier", "title": "Head of Internal Security (until Aug 2057)", "notes": "Blood in the Boardroom: left for a Renraku board seat under Dunkelzahn's will, later returned to Fuchi custody by Corporate Court order, then joined Novatech."},
        ],
        "notes_append": (
            "Blood in the Boardroom: Dunkelzahn's will (Aug 2057) touched off Fuchi's collapse -- a "
            "Renraku board seat for security chief Miles Lanier weakened Richard Villiers, and Yamana "
            "and Nakatomi's factions turned on him. Villiers quietly rebuilt his third of the company as "
            "Novatech, Inc. (Oct 2059) and cashed out; Corporate Court justice David Hague (a Yamana "
            "backer) died in the July 2059 Flight 1118 crash, suspiciously convenient for Villiers but "
            "never proven his doing. Nakatomi's remaining Fuchi Asia assets went to Renraku (Apr 2060); "
            "the rump Fuchi Pan-Europa was sold whole to Shiawase Corporation when Korin Yamana married "
            "into the family (Jun 2060). Fuchi Industrial Electronics was officially dissolved 28 July "
            "2060."
        ),
    },
    "Mitsuhama Computer Technologies": {
        "notes_append": (
            "Blood in the Boardroom: Corporate Court justice Dosan Aburakoji committed suicide at his "
            "Kyoto home (16 May 2059) amid unconfirmed rumors of yakuza pressure. MCT has made repeated "
            "takeover attempts on the independent Chinese research firm Tan Tien, Inc., all of which "
            "have mysteriously fallen through, and remains a major rival to the rising Pacific "
            "Prosperity Group; its Optical Industries and Sisyphus Systems subsidiaries turn up as cover "
            "identities in Seattle-area corporate maneuvering during this period."
        ),
    },
    "Renraku Computer Systems": {
        "leadership_add": [
            {"name": "Inazo Aneki", "title": "President/CEO", "notes": "Blood in the Boardroom: took an indefinite leave of absence (Feb 2060) using Dunkelzahn's bequeathed Seal of the Green Glaves; whereabouts since unknown."},
            {"name": "Yukiako Watanabe", "title": "Chairman of the Board", "notes": "Blood in the Boardroom: ran repeated deniable loyalty tests on board member Miles Lanier without ever settling the question of his true allegiance."},
            {"name": "Haruhiko Nakada", "title": "Chief Operating Officer / Acting CEO", "notes": "Blood in the Boardroom: running the corp day-to-day during Aneki's leave, believing it to be a test of his own readiness to succeed him."},
            {"name": "Dr. Sherman Huang", "title": "Division Manager, Renraku America / Executive Director, Seattle Arcology", "notes": "Blood in the Boardroom: still investigating the arcology's Dec 2059 lockdown from Renraku's New York headquarters."},
            {"name": "Shikei Nakatomi", "title": "Board Member", "notes": "Blood in the Boardroom: ex-Fuchi Asia; bought back into Renraku Apr 2060, bringing Fuchi Asia's assets with him and building an anti-Villiers faction on the board."},
        ],
        "notes_append": (
            "Blood in the Boardroom: Renraku's brief 1957-59 technological surge came from a secret deal "
            "with the vanished elf decker Leonardo, whose disappearance (coinciding with a June 2059 "
            "Corporate Court ruling that forced board member Miles Lanier back to Fuchi custody) cost "
            "Renraku both its Matrix edge and gaps in its own databases, including the public SeaSource. "
            "The Seattle arcology closed to visitors indefinitely on 19 December 2059 after an "
            "unexplained security-systems failure; nobody outside it, corporate or shadow, has "
            "successfully penetrated its defenses since, and general belief holds that Renraku no longer "
            "controls the building. Corporate Court rep Navroz Chandaria died in a New Delhi bombing (20 "
            "Mar 2060); the resulting seat went to Cross Applied Technologies, not Renraku."
        ),
    },
    "Saeder-Krupp Heavy Industries": {
        "notes_append": (
            "Blood in the Boardroom: opens on Zurich-Orbital executive Jean-Claude Priault reporting to "
            "Lofwyr (15 Aug 2059) on the Corporate Court vote seating Wuxing's Li Feng -- a result Lofwyr "
            "had engineered to look like a Saeder-Krupp defeat while sowing distrust among Fuchi's "
            "electors. Lofwyr also hired Abu Khalid's Blackscarf Revolutionaries to destroy an "
            "abandoned Renraku research observatory near Altyar, Iran, erasing evidence of the elf "
            "decker Leonardo's work there."
        ),
    },
    "Shiawase Corporation": {
        "leadership_add": [
            {"name": "Sadato Shiawase", "title": "Chairman of the Board", "notes": "Blood in the Boardroom: locked in a long-running feud with his sister Soka Shiawase."},
            {"name": "Tadashi Shiawase", "title": "President/CEO", "notes": "Blood in the Boardroom: cowed by his father Sadato, who still holds the real power."},
            {"name": "Korin Yamana", "title": "Board Member (from Jun 2060)", "notes": "Blood in the Boardroom: sold the remnants of Fuchi Industrial Electronics to Shiawase and married into the family."},
            {"name": "Mitsuko Shiawase-Yamana", "title": "Vice President, Shiawase Envirotech (Philippines)", "notes": "Blood in the Boardroom: married Korin Yamana as pure economic expediency, on both sides."},
        ],
        "notes_append": (
            "Blood in the Boardroom: Fuchi's Korin Yamana married Mitsuko Shiawase (announced 8 Jun "
            "2060) and sold the remainder of Fuchi Industrial Electronics to Shiawase for stock and a "
            "board seat (14 Jun 2060), giving Shiawase its first real European foothold. The Pacific "
            "Prosperity Group's rise has begun cutting into Shiawase's long-standing dominance of Asian "
            "markets outside Japan."
        ),
    },
    "Yamatetsu Corporation": {
        "leadership_add": [
            {"name": "Buttercup", "title": "Major Shareholder", "notes": "Blood in the Boardroom: engineered the corporation's 2059 relocation to Vladivostok and pushes its meta-friendly reforms."},
            {"name": "Yuri Shibanokuji", "title": "Chairman of the Board", "notes": "Blood in the Boardroom: an ork who inherited his estranged father Tadamako's shares and proposed the move out of Japan."},
            {"name": "Saru Iwano", "title": "President/CEO", "notes": "Blood in the Boardroom: entrenched the corp's anti-metahuman faction while voting Tadamako Shibanokuji's shares under his living will, before Yuri and Buttercup outmaneuvered him."},
            {"name": "Jacques Barnard", "title": "Executive Vice President, Yamatetsu North America", "notes": "Blood in the Boardroom: former head of Yamatetsu Seattle, feuds with Buttercup."},
            {"name": "Mary Luce", "title": "Head, Yamatetsu Seattle", "notes": "Blood in the Boardroom: Barnard's successor, runs one of the most effective shadow networks in the sprawl."},
        ],
        "notes_append": (
            "Blood in the Boardroom: the board approved relocating Yamatetsu's headquarters from Kyoto "
            "to Vladivostok, Russia on 5 May 2059, after chairman Tadamako Shibanokuji's death left "
            "control of his stock to his estranged ork son Yuri; the free spirit Buttercup rallied "
            "enough shareholder proxies to pass the motion and then personally bought up Yamatetsu's "
            "publicly traded stock, giving her roughly 37 percent of the corporation. The relocation "
            "became the founding catalyst for the Pacific Prosperity Group. Japan's Ministry of Trade "
            "responded with escalating regulatory harassment before the move and has punished Yamatetsu "
            "economically since; ironically, Japan's own metahumans lost their most willing employer and "
            "took the public blame for the corp's departure, sparking a spike in racial violence there. "
            "As of this book's account, official headquarters records elsewhere in this campaign may "
            "still show Kyoto -- treat Vladivostok as the current in-fiction headquarters going forward."
        ),
    },
    "DocWagon": {
        "notes_append": (
            "Blood in the Boardroom: a real DocWagon Crisis Response Team responding to the July 2059 "
            "Flight 1118 crash in the Redmond Barrens found a fake 'DocWagon' team -- actually Renraku "
            "operatives -- already working the wreckage; the two teams shot it out over the crash site. "
            "Separately, a Platinum-tier executive used a false 'bone rupture alert' distress signal to "
            "summon a High Threat Response team mid-extraction during a corporate defection (see Ares "
            "Bellevue Offices)."
        ),
    },
    "Knight Errant Security Services": {
        "notes_append": (
            "Blood in the Boardroom: Knight Errant troops unleashed the Chicago insect-spirit hive on "
            "the city with an August 1955 raid, then helped enforce the resulting UCAS quarantine before "
            "Ares' Strain III-Beta operation cleared it in Feb 1958; the corp's brutal suppression of "
            "Detroit riots against Chicago refugees drew criticism, later balanced by efficient, "
            "restrained riot suppression after Dunkelzahn's 2057 assassination."
        ),
    },
    "Lone Star Security": {
        "notes_append": (
            "Blood in the Boardroom: Lone Star Quebec and Knight Errant's rival security contracts in "
            "Quebec are cited as a natural flashpoint for a law-enforcement-campaign angle on the "
            "Ares/Cross Applied Technologies rivalry (Running Blood in the Boardroom, p.13)."
        ),
    },
    "Pueblo Corporate Council": {
        "notes_append": (
            "Blood in the Boardroom: a Fuchi 'delta clinic' -- an unregistered cutting-edge cyberware "
            "research facility -- operates secretly inside Pueblo Corporate Council territory near Santa "
            "Fe under Villiers-faction control; Pueblo Security Force also arrested a runner team "
            "investigating a virtual bank tied to Arthur Vogel's Ares stock purchase, on suspicion of "
            "espionage and treason."
        ),
    },
    "Salish-Shidhe Council": {
        "notes_append": (
            "Blood in the Boardroom: Flight 1118, a Tokyo-Seattle semiballistic carrying Corporate Court "
            "justice David Hague, crashed in the Redmond Barrens near the Salish-Shidhe border on 11 "
            "July 2059, killing roughly 200."
        ),
    },
}

LOC_UPDATES = {
    "The Barrens (Seattle)": {
        "notes_append": (
            "Blood in the Boardroom: Flight 1118, a Tokyo-Seattle semiballistic, overshot Sea-Tac and "
            "crashed into the Redmond Barrens on 11 July 2059, killing roughly 200 people and burning "
            "for more than 24 hours -- see Flight 1118 Crash Site."
        ),
    },
}

NPC_UPDATES = {
    "Damien Knight": {
        "notes_append": (
            "Blood in the Boardroom: still holds Ares Macrotechnology through decades of boardroom "
            "maneuvering, helped for years by Dunkelzahn's secretly held Ares stock (via Gavilan "
            "Ventures) swinging votes his way. Ordered Operation Extermination (Feb 1958), the Strain "
            "III-Beta assault that cleared Chicago's insect-spirit Containment Zone in under twelve hours "
            "-- a PR win after his own earlier Knight Errant raid had accidentally unleashed the hive on "
            "the city in the first place. Backed the Dunkelzahn/Kyle Haefner presidential ticket in 2057; "
            "Knight Errant's efficient riot suppression after Dunkelzahn's assassination rebuilt Ares' "
            "public image. Lucien Cross of Cross Applied Technologies has kept blackmail proof of "
            "Knight's 'David Gavilan' Nanosecond Buyout identity for thirty years as insurance against "
            "him, and Cross Applied Technologies' 2059 alliance with Leonard Aurelius has turned their "
            "old cold war hot. Refers to fellow Ares board member Arthur Vogel privately as 'this "
            "greenhead dwarf lawyer I've been saddled with.'"
        ),
        "enemies_add": ["Cross Applied Technologies, Inc."],
    },
    "Arthur Vogel": {
        "background_append": (
            "Blood in the Boardroom: bought Leonard Aurelius's entire Ares stake privately in October "
            "2059, putting his holdings, combined with his inherited Gavilan Ventures shares, slightly "
            "ahead of Damien Knight's own once Knight's Gavilan proxy control expired that August."
        ),
        "notes_append": (
            "Has made no bold moves against Knight so far -- supporters call it caution, detractors call "
            "it having sold out while his bank account grows. Should he team with Nadja Daviar's Gavilan "
            "shares, the combined vote could seriously threaten Knight's control. Knight, for his part, "
            "still is not sure what to make of 'this greenhead dwarf lawyer I've been saddled with.'"
        ),
    },
    "Nadja Daviar": {
        "background_append": (
            "Blood in the Boardroom: inherited Gavilan Ventures -- and the roughly 12 percent of Ares "
            "Macrotechnology stock it controls -- from Dunkelzahn's will, then signed two years' voting "
            "proxy over to Damien Knight rather than to Leonard Aurelius, who had hoped for her support. "
            "Reasons unclear; rumor points to blackmail or a threat against someone close to her."
        ),
        "notes_append": "Regained direct control of the Gavilan shares in August 2059. Persistent Shadowland gossip places a mystery man dining with her in Washington DC.",
    },
    "Gary Grey": {
        "background_append": "Blood in the Boardroom: Arthur Vogel's running mate during his brief public political career; took over as Sierra, Inc.'s president when Vogel stepped down in October 2059 to focus on his new Ares Macrotechnology stock.",
    },
    "Hanzo Shotozumi": {
        "background_append": (
            "Blood in the Boardroom (Mob Clash): a Tacoma-area oyabun who finally broke away from his "
            "parent syndicate to found his own independent league, the Shotozumi-rengo, after months of "
            "trying to keep the plan secret from Vary v Zakone boss Dimitri Makaroff, who was digging for "
            "proof of it to use as blackmail leverage over Tacoma's yakuza rackets."
        ),
        "notes_append": "The split ends Makaroff's blackmail hold on him but draws new enemies from within his old syndicate's structure.",
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
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
"""

NOT_BUILT = """
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
"""

PLAY_NOTES = """
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
"""
