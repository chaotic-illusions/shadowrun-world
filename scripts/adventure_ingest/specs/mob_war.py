# Mob War! (FASA 7326, 1997) -- campaign order #30. Seattle metroplex-wide, January 2058. Don James
# O'Malley, capo of the Seattle Mafia, is assassinated January 1, 2058 -- the very end of the Chinese
# Year of the Ox; the Year of the Tiger, which Triad sorcery treats as the syndicate's chance to seize
# the city, begins in February 2058. This is a sourcebook, not one linear adventure: four independent
# "tracks" (the Mafia, the Yakuza, the Triads, the Seoulpa Rings), each with its own history, players,
# adventure frameworks and adventure ideas, plus a Shadowland-BBS "Dragon Crimelord" appendix (great
# dragons Ryumyo and Lung allegedly running the Yakuza and the Triads from the shadows) that the book
# itself frames as unconfirmed underworld rumor, argued down by its own in-thread skeptics -- captured
# here as org notes and NOT_BUILT color, not as dragon NPC rows.
# Editing inconsistencies: the timeline prints "5 January 2048" for an event that is clearly January
# 2058 (surrounding entries and the funeral four days earlier are dated 2058) -- corrected here. The
# book's political critic of Governor Schultz is named "Kenneth Brackhaven"; the existing NPC row from
# Peacekeeper is "Karl Brackhaven" (Humanis Central Seattle chapter president, ex-Aztechnology exec) --
# flagged as a possible book/book discrepancy on that row rather than creating a duplicate NPC.
# Cross-database name collisions found while ingesting (verified live, since they postdate the name
# dump this spec was written against): (1) "Hanzo Shotozumi" already exists as an NPC from Elven Fire,
# oyabun of "Dungeness Crab Clan" -- genuinely the same canon character, so this spec updates that row
# (NPC_UPDATES) instead of creating a duplicate, and flags the org-name discrepancy rather than relinking
# him. (2) "The Tigers" already exists as an unrelated Elven Fire yakuza gang (Dungeness Crab muscle
# loaned to the Whispering Nights); this book's own, unrelated Triad-muscle gang of the same short name
# is created here as "The Tigers (Eighty-Eights)" to avoid clobbering the existing row. (3) "Shigeda-
# gumi" already exists as an unrelated invented crime cell from the Mercurial spec (Sumiko Hotoda,
# Toroshi, New Horizons Development); this book's canonical Takeo-Shigeda-led Yakuza clan is created
# here as "Shigeda-gumi (Takeo Shigeda)" instead. All three are cross-referenced from the affected rows
# and from the Yakuza (Watada-rengo) discrepancy log. (4) "William Louden" and "Nadja Daviar" already
# exist as NPCs (from Predator and Prey and Super Tuesday! respectively) -- genuinely the same
# characters, so both are updated via NPC_UPDATES instead of duplicated.
# Source text: docs/Adventures/text/7326-mob-war.txt (66 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "Mob War!"
ORDER = 30
SOURCE = "Mob War! {FASA7326}.pdf, pp. 3-65"
YEAR = "2058 (January)"

SYNOPSIS = """
Two disgruntled Mafia dons hire the freelance assassin organization **Chimera** to kill **Don James
O'Malley**, capo of the Seattle Mafia and head of the **Finnigan Family**. O'Malley dies January 1,
2058, shot from a distance while walking to breakfast with his daughter **Rowena O'Malley**, freshly
home from Harvard Law. She claims her father's seat over the objections of Mafia tradition, backed by
consiglieri **Al Cavalieri**, while the **Bigio Family** (Don **Maurice "The Butcher" Bigio**) and the
**Ciarniello Family** (Don **Vince "Numbers" Ciarniello**) -- the two families who arranged the hit --
maneuver to betray each other and seize Seattle for themselves. Milwaukee's **Don Leo McCaskill**, who
inherited authority over Chicago's shattered operations after the Chicago Containment Zone, holds the
Commissione's mandate to decide who ends up running Seattle, and is waiting to see who proves it first.

The Mafia's disarray is everyone else's opportunity. **Hanzo Shotozumi**, oyabun of the dominant
**Shotozumi-gumi**, wants to break his three Seattle gumis away from Japan's Watada-rengo into his own
West Coast rengo, and starts by muscling into Mafia gambling and vice operations -- using the Amerind
gang **First Nations** as deniable muscle and racing to secure the loyalty of the **Nishidon-gumi** and
the **Shigeda-gumi** before either gets ambitious. The **Yellow Lotus** Triad, led by **Zheng Li Kwan**
(who secretly commands the ancient vampire **Su Cheng** through a stolen soul jar), tries to unite
Seattle's three Triads -- the tech-forward **Eighty-Eights** (Rick Wu, muscle supplied by the gang
**The Tigers**, unrelated to the Elven Fire yakuza gang of the same name) and the weak, magically puppeteered **Octagon** (nominal leader David Gao, real power
the wizard **Chen Kwan-Ti**) -- into a single force that can take Seattle from the Yakuza. And the
**Seoulpa Rings** -- autonomous cells of Korean ex-Yakuza who survived "the Schism," the 2043 purge that
birthed them -- see a rare chance for revenge: the dockside **Choson Ring** (Kyu), the Redmond-Barrens
**Komun'go Ring** (Chulsoon Gray-Wolf) and the Ork Underground's secretive **Tartarus Ring** (The Lord
of the Inner Darkness) all move against a Yakuza that is suddenly fighting on three fronts at once.

Behind the visible war, a Shadowland leaker calling himself Dragonslayer claims the Yakuza and the
Triads are not really rival syndicates at all but instruments of two great dragons -- **Ryumyo** behind
the Watada-rengo, **Lung** behind the Hung Lung Mun (the Red Dragon Association) -- both quietly digging
toward the same ancient, mana-soaked prize along the Pacific Rim's Ring of Fire. Nobody in Seattle's
underworld can confirm it, and the book itself treats it as one more piece of shadowtalk a runner might
or might not believe.

Lone Star (chief **William Louden**, quietly recruiting shadowrunners to do what his cops legally
cannot) and Knight Errant (angling to win Lone Star's metroplex contract out from under it) both try to
profit from the chaos without becoming its next casualty, while Governor **Schultz** and Colonel **Ben
O'Neil**'s Metroplex Guard stay on the sidelines rather than risk another Night of Rage.
"""

TIMELINE = """
- **2010** -- the Watada-rengo formally recognizes the Seattle Yakuza as the "Dungeness Crabs of the
  87th Prefecture," fueling its rapid growth.
- **2026** -- the Commissione sends **Brian O'Malley** of Milwaukee to head the Finnigan Family and
  serve as capo of Seattle against Yakuza expansion.
- **2030** -- Yakuza assassins kill Brian O'Malley; a retaliatory hit the next day kills the responsible
  oyabun and his lieutenants. Both sides, exhausted, agree to an uneasy truce. **Patrick Finnigan**
  becomes capo.
- **2031** -- Brian's older brother **James O'Malley**, capo of Milwaukee, is stripped of his post and
  forced into retirement after his obsession with revenge wrecks his own city's operations.
- **2032** -- the Watada-rengo sends a new, largely Korean upper echelon to rebuild the Seattle gumi.
- **2042** -- **Akira Watada**, oyabun of the Watada-rengo, issues an ultimatum to the Korean oyabuns of
  Seattle: swear loyalty or else. They refuse.
- **January 2043 -- "the Schism"** -- Watada-rengo assassins purge nearly all of the Seattle Yakuza's
  Korean leadership in a week of killings; survivors flee underground and eventually organize into the
  **Seoulpa Rings**. **Hanzo Shotozumi** is made oyabun of the new Shotozumi-gumi to clean up and hold
  the metroplex.
- **2044** -- with Patrick Finnigan unable to hold the line against renewed Yakuza expansion, the
  Commissione recalls James O'Malley from retirement as Don of Seattle. He, his wife and 15-year-old
  daughter Rowena move to the city; the two syndicates settle into fourteen years of stalemate.
- **August 2055** -- the UCAS government seals the Chicago Containment Zone. The Chicago Mafia is lost;
  the Commissione transfers its authority to **Don Leo McCaskill** of Milwaukee, a former O'Malley
  lieutenant.
- **October 2057** -- the Bigio and Ciarniello dons begin meeting secretly with **Sergei Malenkin**,
  public contact for the assassin organization **Chimera**.
- **1 January 2058 -- "the New Year's Hit"** -- Chimera operative **Firebird** shoots Don James O'Malley
  dead outside his home with a single sniper round.
- **4 January 2058** -- O'Malley's funeral; Hanzo Shotozumi attends with a Yakuza honor guard to deny
  Yakuza involvement and imply the Yakuza intends to reclaim lost territory. Rowena O'Malley announces
  her claim to the Finnigan Family and the capo's seat, backed by Al Cavalieri.
- **5 January 2058** -- the first Underworld files hit Shadowland (drawing shadowrunner attention citywide);
  Rowena informs the other Families, Don McCaskill and the Commissione of her claim; word spreads that
  the Yakuza is recruiting gangs as soldiers (book prints this date as "5 January 2048" -- a typo).
- **7 January 2058** -- Yakuza soldiers begin openly muscling into Mafia gambling and vice operations;
  sporadic street fighting breaks out.
- **8 January 2058** -- an assassination attempt on Rowena O'Malley is narrowly averted, hardening her
  resolve.
- **February 2058** -- the Chinese Year of the Tiger begins; Triad sorcerer Chen Kwan-Ti's prophecy that
  this is the Triads' year to take Seattle starts to drive Yellow Lotus strategy citywide.
"""

ORGS = [
    {
        "name": "Finnigan Family",
        "org_type": "Mafia family",
        "tier": 3,
        "headquarters": "O'Malley family compound, Seattle",
        "summary": "The Seattle Mafia's ruling family for fifty years; leaderless since Don James O'Malley's assassination, contested between his daughter and his own relatives-by-marriage",
        "description": (
            "Founded in the early twenty-first century by old-world Irishman Ian Finnigan, the Finnigans "
            "rose to lead the Seattle Mafia through aggressive, tradition-bending business -- and paid "
            "for it when the Yakuza decimated the family's leadership, killing Ian and his sons James and "
            "Michael. The Commissione twice imposed outside Milwaukee dons (Brian, then James O'Malley) "
            "over the family rather than trust an unblooded Finnigan; Ian's widow Mary Finnigan has never "
            "forgiven either imposition. With James O'Malley's murder the family is headless again, "
            "caught between his daughter Rowena's claim and Mary Finnigan's decades-long plan to install "
            "her grandnephew James Michael instead."
        ),
        "leadership": [
            {"name": "Rowena O'Malley", "title": "Daughter and heir apparent to Don James O'Malley", "notes": "Claims the Family and the capo's seat; backed by Al Cavalieri."},
            {"name": "Al Cavalieri", "title": "Consiglieri", "notes": "James O'Malley's oldest Milwaukee friend; Rowena's closest advisor."},
            {"name": "Mary Finnigan", "title": "Widow of founder Ian Finnigan", "notes": "78 years old, plots to install grandnephew James Michael instead of Rowena."},
            {"name": "Patrick Finnigan", "title": "Former capo of Seattle (Mary's nephew)", "notes": "Weak leader turned Matrix-savvy accountant; quietly supports Rowena."},
            {"name": "James Michael Finnigan", "title": "Caporegime, heir-apparent in Mary Finnigan's eyes", "notes": "Patrick's son, 29, obsessed with marrying Rowena to claim the Family."},
        ],
        "notes": (
            "Mafia Organization Diagram (p.22) places Don James O'Malley (deceased) above the family as "
            "capo of Seattle. Allied with the magical street gang the Merlyns (Al Cavalieri's two-year-old "
            "deal, forged after a defeat by Triad mages). Rumor holds O'Malley was about to offer the "
            "Merlyns a Family position when hard-liners had him killed for it -- unconfirmed. Adventure "
            "role: Tracking the Assassin (runners hunt O'Malley's killer, implicating Bigio and "
            "Ciarniello) and Shotgun Wedding (James Michael kidnaps Al Cavalieri to force a marriage to "
            "Rowena; Patrick Finnigan is secretly the Mr. Johnson who hires runners to stop it) both "
            "center on this family."
        ),
        "allies": ["Merlyns"],
        "enemies": ["Bigio Family", "Ciarniello Family"],
    },
    {
        "name": "Bigio Family",
        "org_type": "Mafia family",
        "tier": 2,
        "headquarters": "Bigio family mansion, Tacoma",
        "summary": "Seattle's number-two Mafia family, thinned by decades of front-line losses to the Yakuza and now making its play for the top spot via a secret deal with Chimera",
        "description": (
            "Known for hard adherence to La Cosa Nostra tradition, the Bigios took the brunt of Yakuza "
            "reprisals over the years and carry the resulting blood debt as a grievance. Don Maurice "
            "\"The Butcher\" Bigio rose from soldatos to protege of the aging Don Gianelli, earning his "
            "nickname through brutal enforcement, and moved secretly with Don Vince Ciarniello to hire "
            "Chimera and remove James O'Malley -- each intending to betray the other for sole control "
            "once O'Malley was gone."
        ),
        "leadership": [
            {"name": "Maurice Bigio", "title": "Don, head of the Bigio Family", "notes": "Arranged O'Malley's assassination with Chimera; now moving on Rowena and Ciarniello both."},
            {"name": "Marleen Bigio", "title": "Don Maurice's wife", "notes": "Society patron; her lavish Tacoma parties are a way to get close to the family."},
            {"name": "Tony Gianelli", "title": "Consiglieri (former Don, Maurice's mentor)", "notes": "Owns Gianelli's Restaurant, Tacoma; privately worried the war will hurt more than help."},
            {"name": "Vincent DeClerry", "title": "Accountant / numbers soldier", "notes": "Former soldier, now runs the Family's Tacoma money clearinghouse from above his own bar."},
        ],
        "notes": (
            "Adventure role: Blood Money (Ivy Ciarniello and Dan Grizetti frame Bigio's mansion break-in "
            "to look like Ciarniello's doing) and The Witness (sottocapo Anthony \"Toothless\" Boniduchi, "
            "shot for threatening to talk, survives under DocWagon guard in Everett) both hinge on this "
            "family. If exposed as O'Malley's killers, the Bigios become Rowena's primary revenge target."
        ),
        "allies": ["Ciarniello Family", "Chimera"],
        "enemies": ["Finnigan Family"],
    },
    {
        "name": "Ciarniello Family",
        "org_type": "Mafia family",
        "tier": 2,
        "headquarters": "Everett",
        "summary": "The Mafia's Everett-based gambling family, run with corporate efficiency by a fear-driven don whose young wife is quietly robbing him blind",
        "description": (
            "Don Vince \"Numbers\" Ciarniello oversees most of the Mafia's profitable Seattle gambling "
            "operations (notably \"Casino Corner\" in Everett) with an accountant's efficiency. He agreed "
            "to Maurice Bigio's plan to kill O'Malley out of fear, after O'Malley discovered a caporegime "
            "skimming Ciarniello's casino take. Unknown to Vince, his elf wife Ivy and his own consiglieri "
            "Dan Grizetti are having an affair and embezzling from the family behind his back."
        ),
        "leadership": [
            {"name": "Vince Ciarniello", "title": "Don, head of the Ciarniello Family", "notes": "Ambitious but fear-driven; agreed to the O'Malley hit to protect himself."},
            {"name": "Ivy Ciarniello", "title": "Don Vince's wife", "notes": "Elf, Barrens-orphan past; skimming Family funds with Dan Grizetti behind Vince's back."},
            {"name": "Dan Grizetti", "title": "Consiglieri (\"Fancy Dan\")", "notes": "Having an affair with Ivy; leaked the 'Golden Goose' blackmail file to Bigio to frame Vince."},
            {"name": "Caesar Ciarniello", "title": "Son and heir apparent (\"Chrome\")", "notes": "28, cybered Mafia punk who despises Ivy as a gold-digger and distrusts elves generally."},
        ],
        "notes": (
            "Adventure role: Blood Money (Grizetti and Ivy plan to abscond with skimmed money via Sea-Tac, "
            "framing Vince and the runners); By the Blood (a ritual-link theft targets Vince via a private "
            "clinic break-in). If the Chimera hit is exposed, Vince is the most likely to fold and name "
            "Maurice Bigio as the real mastermind."
        ),
        "allies": ["Bigio Family"],
        "enemies": ["Finnigan Family"],
    },
    {
        "name": "McCaskill Family",
        "org_type": "Mafia family",
        "tier": 3,
        "headquarters": "Milwaukee",
        "summary": "The Milwaukee Mafia family that inherited authority over Seattle and the former Chicago operations after the Chicago Containment Zone, and now must decide who runs the Seattle Mob war",
        "description": (
            "Don Leo McCaskill, once a lieutenant of James O'Malley, took control of the former Chicago "
            "Mafia's operations in August 2055 after the UCAS government sealed the Chicago Containment "
            "Zone and the Commissione gave up the Chicago don for dead. With O'Malley's murder, the "
            "Commissione hands McCaskill responsibility for deciding Seattle's new capo -- both to use his "
            "Chicago experience and to see how he handles the pressure. He wants Seattle settled fast, "
            "since ongoing chaos threatens his own shot at a seat on the Commissione's Inner Circle, and "
            "will back whichever Seattle family looks most likely to restore order quickly."
        ),
        "notes": (
            "Never appears on-page in person; acts entirely through the Seattle Families' maneuvering to "
            "win his favor. A useful off-screen arbiter for a gamemaster who wants an external deadline or "
            "authority figure to validate whichever family the runners end up backing."
        ),
    },
    {
        "name": "Chimera",
        "org_type": "assassin organization",
        "tier": 2,
        "headquarters": "Seattle (concealed)",
        "summary": "A freelance organization of Russian-expatriate professional assassins, hired by the Bigio Family to kill Don James O'Malley",
        "description": (
            "Most of Chimera's members belonged to a branch of Russian intelligence that disintegrated "
            "after the EuroWars troubles in Moscow; in roughly four years operating out of Seattle they "
            "have built a fearsome reputation as kick artists. Chimera considers the O'Malley hit a closed "
            "business transaction -- if another client wants another Seattle target dead, that is a "
            "separate deal -- but the organization will kill to protect its own security, including "
            "silencing its own operative Firebird if she becomes a serious liability."
        ),
        "leadership": [
            {"name": "Sergei Malenkin", "title": "Public contact / broker", "notes": "Runs a legitimate Everett import/export front; will not compromise Chimera's security for any price."},
            {"name": "Firebird", "title": "Assassin (Natasha Romanov)", "notes": "KGB-trained kick artist; shot O'Malley with a custom sniper rifle from a concealed position."},
        ],
        "notes": (
            "See the Underworld Sourcebook, p.75, for more on Chimera's general activities. Adventure "
            "role: the climax of Tracking the Assassin pits the runners directly against Firebird, sent "
            "by a panicked Maurice Bigio to silence anyone getting close to the truth."
        ),
    },
    {
        "name": "Merlyns",
        "org_type": "magical gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Seattle",
        "summary": "A hermetic-mage street gang retained by the Finnigan Family for two years as magical muscle, education and a lucrative telesma-smuggling sideline",
        "description": (
            "Originally a loose collection of magical geeks who did not fit in elsewhere, the Merlyns were "
            "hired by Al Cavalieri after the Finnigans suffered an embarrassing defeat to Triad adepts and "
            "mages. About thirty members strong, they name themselves after astronomical bodies by rank "
            "(planets for leadership, constellations for the second tier, comets and distant objects for "
            "recruits), wear a crescent-moon-over-earth symbol, and have grown steadily more combat-minded "
            "since joining the Mafia's payroll."
        ),
        "leadership": [
            {"name": "Saturn", "title": "Leader (Grade 3 hermetic initiate)", "notes": "Rumored illegitimate son of the murdered Michael Finnigan; increasingly a power broker rather than a field mage."},
            {"name": "Mercury", "title": "Lieutenant / head educator", "notes": "Teaches magic to Mafia goons; creates foci, fetishes and permanent spells for Mafia warriors."},
            {"name": "Venus", "title": "Lieutenant (Saturn's lover)", "notes": "Elf; the gang's real strategic brain; runs a profitable telesma-and-talisman smuggling pipeline from the CFS, Tir Tairngire and the NAN."},
            {"name": "Mars", "title": "Lieutenant / warlord", "notes": "Coordinates the gang's magical support in any Mafia combat operation."},
        ],
        "notes": (
            "Initiation once meant escalating spellcasting until collapse; current rumor adds physical "
            "tests from Mars and Mafia-administered loyalty oaths. Given Rowena O'Malley's known pro-magic "
            "leanings, the Merlyns expect ritual magic work to be added to their portfolio if she "
            "consolidates power."
        ),
        "allies": ["Finnigan Family"],
    },
    {
        "name": "Shotozumi-gumi",
        "org_type": "Yakuza clan",
        "tier": 3,
        "headquarters": "Seattle",
        "summary": "The most powerful Yakuza clan in Seattle; its oyabun dreams of breaking away from Japan's Watada-rengo to found his own West Coast rengo",
        "description": (
            "Formed from the wreckage of the Schism and built into an efficient, feared organization by "
            "oyabun Hanzo Shotozumi over fifteen years, the Shotozumi-gumi enforces Yakuza tradition "
            "strictly and conservatively -- few women or metahumans hold any real position, the notable "
            "exception being wakagashira-hosa Miko Ishikawa. With James O'Malley dead and the Mafia in "
            "disarray, Shotozumi moves to secure the loyalty of Seattle's other two gumis and seize the "
            "gambling and \"entertainment\" turf long contested with the Mafia, especially Casino Corner "
            "in Everett -- only to find himself fighting the Mafia, the Triads and the Seoulpa Rings all "
            "at once."
        ),
        "leadership": [
            {"name": "Hanzo Shotozumi", "title": "Oyabun", "notes": "Inscrutable, coldly efficient; wants his own West Coast rengo independent of the Watada-rengo."},
            {"name": "Shiro Tanaka", "title": "Wakagashira (second in command)", "notes": "Utterly loyal; handles Shotozumi's most delicate business personally."},
            {"name": "Miko Ishikawa", "title": "Wakagashira-hosa (assistant second in command)", "notes": "Rare female power-holder; secretly a spy reporting Shotozumi's activities to Akira Watada."},
            {"name": "Toju Shotozumi", "title": "Head of the sokaiya branch (Isogashii)", "notes": "Hanzo's cousin; runs corporate blackmail/stock operations against Seattle businesses."},
        ],
        "notes": (
            "Uses the Amerind gang First Nations as deniable front-line muscle and is allied to it. "
            "Hanzo's daughter Keiko ran away years ago and works the shadows as the decker \"Kiku,\" "
            "secretly undermining her father's operations. Adventure role: Dirty Laundry (BrightSky "
            "Finances Matrix trap door into a Shigeda-gumi host, framed by the Triads), A Matter of Honor "
            "(Miko's double game), Neon Flower (Kiku's revenge heist against her father). Underworld "
            "chatter (Dragonslayer's Shadowland thread, unconfirmed) claims the great dragon Ryumyo is the "
            "true power behind the entire Watada-rengo and, by extension, this gumi."
        ),
        "allies": ["First Nations"],
        "enemies": ["Seattle Mafia", "Yellow Lotus"],
    },
    {
        "name": "Nishidon-gumi",
        "org_type": "Yakuza clan",
        "tier": 2,
        "headquarters": "Seattle",
        "summary": "The oldest Yakuza clan in Seattle, nursing a long-standing grudge against Hanzo Shotozumi's rise to dominance",
        "description": (
            "Isao Nishidon survived the Schism relatively unscathed by acting on his own initiative and "
            "eliminating his own clan's Korean oyabun before the Watada-rengo's purge order even arrived "
            "-- for which Akira Watada rewarded him with his own gumi. He was soon eclipsed by the more "
            "powerful Shotozumi-gumi and has resented Hanzo Shotozumi ever since; if Shotozumi ever breaks "
            "from the Watada-rengo, Nishidon and his gumi will be his hardest problem to bring to heel."
        ),
        "leadership": [
            {"name": "Isao Nishidon", "title": "Oyabun", "notes": "Acted decisively during the Schism to keep his own seat; deeply resents Shotozumi's seniority."},
        ],
        "notes": "Nominally acknowledges Shotozumi as the senior Seattle oyabun; how far that loyalty extends if Shotozumi tries to formalize his own rengo is an open question the book leaves for the gamemaster.",
    },
    {
        "name": "Shigeda-gumi (Takeo Shigeda)",
        "org_type": "Yakuza clan",
        "tier": 2,
        "headquarters": "Seattle",
        "summary": "The newest, weakest and most progressive of Seattle's three Yakuza clans, formed after the Schism and likely to side with whoever seems strongest",
        "description": (
            "Formed from the remnants of clans decimated by the Schism's purge of Korean leadership, the "
            "Shigeda-gumi is led by Takeo Shigeda, born in San Francisco but a twenty-three-year resident "
            "of Seattle, whose watchwords are safety and prosperity rather than aggressive expansion. It "
            "is the most progressive of the three gumis -- more women and magicians hold real positions in "
            "its ranks than in the Shotozumi-gumi or Nishidon-gumi, though traditional restrictions on "
            "metahumans remain intact -- but its underlings' habit of quietly handling their own problems "
            "means Shigeda-sama sometimes hears about trouble only once it is already a crisis."
        ),
        "leadership": [
            {"name": "Takeo Shigeda", "title": "Oyabun", "notes": "Prioritizes safety and prosperity over expansion; likely to side with whichever Yakuza faction seems strongest."},
            {"name": "Jiro Egami", "title": "Wakagashira", "notes": "Investigates security breaches personally; cautious and thorough."},
        ],
        "notes": (
            "Named 'Shigeda-gumi' in the book; qualified here as 'Shigeda-gumi (Takeo Shigeda)' because an "
            "unrelated organization of the same exact name -- Maria Mercurial's own invented crime cell, "
            "led by Sumiko Hotoda and Toroshi -- already exists in the database from the Mercurial spec. "
            "The two are not the same organization; do not merge them. Adventure role: Dirty Laundry -- "
            "wakagashira Jiro Egami investigates a suspected security breach at BrightSky Finances in Fort "
            "Lewis after shadowrunners use a trapdoor planted by the Triad Eighty-Eights to access one of "
            "this gumi's Matrix hosts (see BrightSky Finances and MATRIX_HOSTS)."
        ),
    },
    {
        "name": "First Nations",
        "org_type": "gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Seattle (territory wherever the Yakuza needs it)",
        "summary": "An all-Amerindian gang fed nuyen, weapons and flattery by Hanzo Shotozumi until it became the Yakuza's fiercest deniable muscle",
        "description": (
            "A near-extinct street gang that Hanzo Shotozumi revived nearly two years ago by supplying "
            "weapons and cash and stoking its members' pride in a romanticized Amerindian warrior "
            "heritage -- part of Shotozumi's longer-term hope of building ties to the Native American "
            "Nations. Fifteen members strong, all Salish-Shidhe except one, they now act mainly as Yakuza "
            "muscle while running their own smuggling trade between Seattle and Salish-Shidhe territory."
        ),
        "leadership": [
            {"name": "Blood of the Buffalo", "title": "Leader (Grade 5 physical adept)", "notes": "Salish-Shidhe elf; follows the Way of the Warrior."},
            {"name": "Wind-Walker", "title": "Lieutenant / shaman (Coyote)", "notes": "Salish-Shidhe human; twin to Wind-Rider; Grade 3 initiate."},
            {"name": "Wind-Rider", "title": "Lieutenant / shaman (Raven)", "notes": "Salish-Shidhe human; twin to Wind-Walker; Grade 3 initiate."},
            {"name": "Moon Hawk", "title": "Lieutenant (mundane)", "notes": "Sioux; beta-grade wired reflexes; recruited after a shadowrun caught the Yakuza's attention."},
        ],
        "notes": (
            "Initiation: forty-eight hours in a sweat lodge, then dropped blindfolded into the Salish-"
            "Shidhe wilderness to reach a preordained Seattle-area location within forty-eight more hours; "
            "survivors are tattooed with the gang symbol (a raven flying over a howling coyote) and a "
            "personal vision. Currently fighting the Choson Ring for control of Everett-dock smuggling. "
            "Adventure role: Warpath (runners hired to disarm them without alerting the Yakuza)."
        ),
        "allies": ["Shotozumi-gumi"],
        "enemies": ["Choson Ring"],
    },
    {
        "name": "Yellow Lotus",
        "org_type": "Triad",
        "tier": 3,
        "headquarters": "Bellevue (Lodgemaster's private residence)",
        "summary": "The most powerful Triad in Seattle, ambitiously recruiting metahumans the Yakuza and Mafia will not take, and led by a man secretly commanding an enslaved vampire",
        "description": (
            "Lodgemaster (Shan Chu) Zheng Li Kwan left Hong Kong -- a city the Triads had already subdued "
            "-- for Seattle's rawer opportunities, took control of the Yellow Lotus six years ago and more "
            "than doubled it through aggressive recruitment of Barrens and Ork Underground metahumans shut "
            "out of the Yakuza and Mafia. He has floated a standing alliance offer to the Eighty-Eights "
            "and the Octagon against their common Yakuza enemy, with a private long-term plan to absorb "
            "both into a single Triad under his own control."
        ),
        "leadership": [
            {"name": "Zheng Li Kwan", "title": "Lodgemaster (Shan Chu)", "notes": "Physical adept, high-grade Triad initiate; collects ancient Chinese artwork; wants to unify Seattle's Triads under himself."},
            {"name": "Su Cheng", "title": "Incense Master", "notes": "Actually an ancient Chinese vampire bound to obedience because Zheng controls the vase holding his Hidden Life; resents his servitude."},
        ],
        "notes": (
            "Adventure role: Soul Jar (Su Cheng secretly hires runners to steal his own soul-jar vase back "
            "from Zheng's warded Tacoma warehouse storage; a decoy vase sits in Zheng's Bellevue home) and "
            "Ringers (Yellow Lotus mages of the Heaven and Earth Circle plan to replace Seoulpa Ring "
            "leaders, including the Choson Ring's Kyu, with shapeshifted impostors). Dragonslayer's "
            "Shadowland thread (unconfirmed) claims the great dragon Lung secretly controls the Hung Lung "
            "Mun -- i.e., the existing Red Dragon Association -- and, through it, much of the Triad world "
            "the Yellow Lotus answers to."
        ),
        "allies": ["Eighty-Eights", "The Octagon"],
        "enemies": ["Shotozumi-gumi"],
    },
    {
        "name": "Eighty-Eights",
        "org_type": "Triad",
        "tier": 2,
        "headquarters": "Seattle",
        "summary": "Seattle's most Westernized, tech-forward Triad, fighting the Yakuza for gambling turf with beta-grade cyberware and the street muscle of the gang the Tigers",
        "description": (
            "Grown out of a decades-old organization heavily Westernized by its years in Seattle, the "
            "Eighty-Eights hold to traditional Triad structure and initiation but have largely dropped the "
            "mystical trappings in favor of technology, run by third-generation Chinese-American leader "
            "Rick Wu, who considers himself a businessman first. Their alliance of convenience with the "
            "Yellow Lotus and the Octagon is aimed squarely at prying gambling operations away from the "
            "Yakuza."
        ),
        "leadership": [
            {"name": "Rick Wu", "title": "Leader", "notes": "Third-generation Chinese-American; distrusts 'mystical mumbo-jumbo,' prefers Western-trained mages and beta-grade cyberware."},
        ],
        "notes": (
            "Adventure role: Dirty Laundry -- the Eighty-Eights dupe shadowrunners into hacking a trapdoor "
            "into a Shigeda-gumi Matrix host via the corp BrightSky Finances, then try to silence them "
            "afterward to avoid blowback. Controls the gang the Tigers -- see The Tigers (Eighty-Eights) "
            "-- as its main street muscle."
        ),
        "allies": ["Yellow Lotus", "The Octagon"],
        "enemies": ["Shotozumi-gumi"],
    },
    {
        "name": "The Tigers (Eighty-Eights)",
        "org_type": "gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Seattle (wherever the Eighty-Eights need a foothold)",
        "summary": "A fanatical death-cult gang serving as the Eighty-Eights' foot soldiers, fed the promise that Triad magic will one day resurrect their fallen",
        "description": (
            "Uncertain even to their own patrons whether they predate the Eighty-Eights or were created "
            "by them, the Tigers fight with total disregard for their own lives, believing that ultimate "
            "Triad victory will let Triad magic revive their dead. Membership is open to anyone willing to "
            "kill; twenty to fifty members blur into the Eighty-Eights' own ranks."
        ),
        "leadership": [
            {"name": "Tiger's Breath", "title": "Leader (Grade 7 physical adept)", "notes": "Unseen in public for months; rumored dead, unconfirmed."},
            {"name": "Dragon-eyes", "title": "Lieutenant / physical magician (Grade 7 initiate)", "notes": "Irises without whites; the gang's mystical center."},
            {"name": "Tiger Claw", "title": "Lieutenant, leader-in-waiting (Grade 3 physical adept)", "notes": "Follows the Invisible Way; rumored to have killed five sleeping Yakuza members single-handed."},
        ],
        "notes": (
            "Called simply 'the Tigers' in the book; named 'The Tigers (Eighty-Eights)' here to avoid a "
            "name collision with the unrelated Elven Fire yakuza gang of the same name already in the "
            "database. Uniform: orange and black, usually a tiger-striped bandanna. Symbol: a tiger "
            "looking through grass. Longtime street rivals of the gang Ancients and several other large "
            "Seattle gangs; considers only the Mafia and the Yakuza worth calling true enemies."
        ),
        "allies": ["Eighty-Eights"],
        "enemies": ["Ancients", "Seattle Mafia", "Shotozumi-gumi"],
    },
    {
        "name": "The Octagon",
        "org_type": "Triad",
        "tier": 1,
        "headquarters": "Tacoma / the Barrens",
        "summary": "The weakest of Seattle's three Triads, its nominal leader a puppet controlled by a wizard with an unexplained private agenda",
        "description": (
            "Losing a long, slow turf war to the Yakuza in Tacoma and the Barrens, the Octagon accepted "
            "Zheng Li Kwan's unification offer as its only real hope of gaining ground. Its public leader, "
            "David Gao, is thoroughly controlled through spells and secret potions by the Octagon's "
            "Incense Master, mainland-Chinese wizard Chen Kwan-Ti, whose true interest in Seattle -- "
            "possibly Su Cheng's soul jar, possibly some other magical prize -- is never made clear."
        ),
        "leadership": [
            {"name": "David Gao", "title": "Leader (nominal)", "notes": "A puppet; real authority rests entirely with Chen Kwan-Ti."},
            {"name": "Chen Kwan-Ti", "title": "Incense Master (true power)", "notes": "Mainland Chinese wizard, rumored trained by the great dragon Lung; arrived in Seattle two years ago; specializes in control and illusion magic."},
        ],
        "notes": "Effectiveness badly weakened by Chen's control of Gao. Prophesied by Chen (via Zheng's sorcerer Chen Kwan-Ti's own reputation) to gain ground in the coming Year of the Tiger alongside the other Triads.",
        "allies": ["Yellow Lotus", "Eighty-Eights"],
        "enemies": ["Shotozumi-gumi"],
    },
    {
        "name": "Choson Ring",
        "org_type": "Seoulpa Ring",
        "tier": 2,
        "headquarters": "Seattle docks",
        "summary": "One of the first Seoulpa Rings to earn a public reputation, a well-established dockside smuggling operation whose Schism-survivor leader dreams of killing Hanzo Shotozumi with his bare hands",
        "description": (
            "An older, disciplined Ring with established rules and traditions, the Choson holds fiercely "
            "to survival, profit and revenge against the Yakuza that gutted its founders' generation. "
            "Leader Kyu survived the Schism as a young man and bars Japanese and Amerinds from membership "
            "outright (the latter because the First Nations gang allied with the hated Yakuza); he "
            "distrusts elves enough that elven initiates have been known to die 'accidentally.'"
        ),
        "leadership": [
            {"name": "Kyu", "title": "Leader", "notes": "Korean, Schism survivor; personal goal is killing Hanzo Shotozumi with his own hands."},
            {"name": "An Soo", "title": "Lieutenant (records and computer systems)", "notes": "Korean, loyal to Kyu; tech-head."},
            {"name": "Jung-mo", "title": "Lieutenant (logistics)", "notes": "Ex-rigger who lost his panzer on a Denver run; handles pickups and deliveries."},
            {"name": "Danny Cho", "title": "Lieutenant (face-man)", "notes": "Talks to clients and arranges meets."},
        ],
        "notes": (
            "Thirty-five initiated members plus hired muscle; symbol a red-and-blue yin yang. Controls two "
            "small dockside warehouses and pays off the Metroplex Guard to look away. Has absorbed most of "
            "the smuggling business The Cutters lost after that gang nearly went under a few years back. "
            "Currently at war with the First Nations over Everett-dock smuggling and has had a run-in with "
            "Renraku security near the Renraku Arcology docks. Initiation is brutal torture-resistance "
            "testing; most members display the scars proudly."
        ),
        "enemies": ["Shotozumi-gumi", "First Nations"],
    },
    {
        "name": "Komun'go Ring",
        "org_type": "Seoulpa Ring",
        "tier": 1,
        "headquarters": "Redmond Barrens, near the NAN border",
        "summary": "A street-level Redmond Ring blending Korean and Haida tribal tradition, fighting the Yakuza and the Rusted Stilettos for the Barrens' protection rackets",
        "description": (
            "Led by Chulsoon Gray-Wolf, a Korean-Amerind half-breed whose Yakuza father died in the "
            "Schism, the Komun'go recruits from the Redmond streets and fosters the idea that 'the "
            "streets take care of their own.' Chulsoon's chief lieutenant and spiritual advisor, the Haida "
            "Wolf shaman Black-Cloud-in-Morning, conducts the Ring's initiations and reads the will of the "
            "spirits for every major decision."
        ),
        "leadership": [
            {"name": "Chulsoon Gray-Wolf", "title": "Leader", "notes": "Korean-Amerind, ~29; father a Yakuza killed in the Schism; hid under his Amerind mother's surname growing up."},
            {"name": "Black-Cloud-in-Morning", "title": "Lieutenant / shaman advisor (Wolf totem)", "notes": "Full-blood Haida; conducts initiations, reads omens for Chulsoon."},
        ],
        "notes": (
            "Twenty initiated members plus ties to small Redmond gangs. Symbol: a black wolf's head with "
            "the Korean word for 'honor' in white. Runs protection rackets across the Redmond Barrens near "
            "the NAN border, partly enforced by the threat of hearth and city spirits disrupting a "
            "non-payer's business. Its greatest non-Yakuza enemy is the Rusted Stilettos, who Chulsoon "
            "suspects the Yakuza is quietly arming against him."
        ),
        "enemies": ["Shotozumi-gumi", "Rusted Stilettos"],
    },
    {
        "name": "Tartarus Ring",
        "org_type": "Seoulpa Ring",
        "tier": 2,
        "headquarters": "Ork Underground, toward the Puyallup Barrens",
        "summary": "A secretive Ring operating through the Ork Underground's tunnels, run almost as a cult by a Bat shaman known only as the Lord of the Inner Darkness",
        "description": (
            "The Tartarus Ring appears when opportunity knocks and vanishes back into the tunnels; the "
            "Underground tolerates it so long as it causes no trouble on the surface. It has distanced "
            "itself from the other Rings' feud with the Yakuza, focusing instead on smuggling, occasional "
            "organlegging (rumored ties to Tamanous, unconfirmed) and a new mushroom-derived street drug, "
            "'shade,' that is cutting into every other syndicate's BTL market."
        ),
        "leadership": [
            {"name": "The Lord of the Inner Darkness", "title": "Leader (Bat shaman)", "notes": "True name unknown; never leaves his dark underground chambers; leads almost as a cult."},
            {"name": "Crawler", "title": "Lieutenant (surface operations)", "notes": "Ork; knows the Underground's tunnels better than anyone, handles anything that requires visiting the surface."},
            {"name": "Greely", "title": "Lieutenant / advisor", "notes": "Cadaverous appearance; persistent rumor holds he is a ghoul, and that the Ring counts ghouls among its members."},
        ],
        "notes": (
            "Twenty to thirty core members, mostly orks, humans and dwarfs. Symbol: bat amulets, patches "
            "or tattoos worn by members. Uniquely among the Seoulpa Rings, has no real enemies -- it stays "
            "out of the Yakuza feud and out of everyone else's way."
        ),
    },
]

LOCATIONS = [
    {
        "name": "O'Malley Family Compound",
        "location_type": "landmark / estate",
        "district": "Seattle",
        "security_level": "Corporate High Security",
        "controlling_org": "Finnigan Family",
        "summary": "James O'Malley's private Seattle estate, its snow-covered courtyard the scene of his assassination and the household where Rowena O'Malley now makes her stand",
        "description": (
            "A walled compound with a cobbled courtyard connecting the main house to a separate living "
            "area, formidable enough in its magical and electronic security that whoever killed Don "
            "O'Malley 'knew the don's schedule and had some means of subverting' it. On the morning of "
            "January 1, 2058, a fresh layer of snow covered the courtyard's cobbled walkway as O'Malley, "
            "escorted by consiglieri Al Cavalieri and a black-clad wiseguy, crossed it on his way to "
            "breakfast with his daughter -- 'their shoes crunched on the fresh layer of snow,' O'Malley "
            "'turned his coat collar up against the chill January wind, still smiling despite the "
            "weather' -- moments before a single sniper round from Firebird put him face down in it, 'a "
            "bright crimson bloodstain spreading across the whiteness like a winter flower.'"
        ),
        "notes": (
            "Where Rowena O'Malley now lives under heavy Family guard and where she announced her claim "
            "to lead the Finnigans after her father's funeral. Referred to in the book only as the estate "
            "or 'the family compound'; also the 'Finnigan Family estate' the runners must reach in time "
            "to interrupt James Michael Finnigan's forced wedding to Rowena in the Shotgun Wedding "
            "adventure framework -- treat as the same property. The funeral itself, attended by 'all the "
            "major Mafia figures of the metroplex' and, uninvited but present, Hanzo Shotozumi's honor "
            "guard, is not given a separate venue in the book; run it here or at a church of the "
            "gamemaster's choosing."
        ),
    },
    {
        "name": "Casino Corner",
        "location_type": "commercial district",
        "city": "Everett",
        "district": "Everett",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "Ciarniello Family",
        "summary": "The Ciarniello Family's cluster of Mafia-run gambling operations in Everett, coveted by Hanzo Shotozumi for over a decade",
        "description": (
            "A concentration of Mafia-controlled casinos and gambling parlors in Everett, run with "
            "corporate efficiency under Don Vince Ciarniello -- the Family's most profitable turf and one "
            "of the most lucrative pieces of territory contested between the Mafia and the Yakuza. Hanzo "
            "Shotozumi has coveted 'this particularly lucrative piece of territory for more than a "
            "decade,' and his ambitions for a West Coast rengo run directly through taking it away from "
            "the Ciarniellos."
        ),
        "notes": "Ivy Ciarniello worked here as a dancer and waitress before catching Don Vince's eye. A likely flashpoint location for any Mafia-vs-Yakuza turf adventure the gamemaster wants to run.",
    },
    {
        "name": "Bigio Family Mansion",
        "location_type": "landmark / estate",
        "city": "Tacoma",
        "district": "Tacoma",
        "security_level": "Corporate High Security",
        "controlling_org": "Bigio Family",
        "summary": "Don Maurice Bigio's well-protected Tacoma home, the scene of Marleen Bigio's lavish society parties and the ambush that opens the Blood Money adventure framework",
        "description": (
            "A well-protected Tacoma house that Marleen Bigio uses as a venue for the lavish parties she "
            "throws as patron of Seattle's current artistic and media fads -- 'an excellent way for player "
            "characters to get close to her or to Don Maurice, or to check out the Bigios' home in "
            "Tacoma.' Its Matrix system is protected by 'some heavy ice from the outside,' but is more "
            "vulnerable to a decker who can sleaze it from a jackpoint inside the house itself."
        ),
        "notes": (
            "Never given a proper name in the book, only 'Bigio's Tacoma mansion.' In the Blood Money "
            "framework, runners hired to recover the 'Golden Goose' blackmail file sneak in through "
            "Marleen's social calendar and find Don Bigio has been tipped off by Dan Grizetti -- the ice "
            "jumps the decker while Bigio's henchmen close on the rest of the team, and the don "
            "interrogates any captives to learn whether Don Ciarniello sent them before deciding what to "
            "do with them."
        ),
    },
    {
        "name": "DeClerry's",
        "location_type": "bar",
        "city": "Tacoma",
        "district": "Tacoma",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "Bigio Family",
        "summary": "Vincent DeClerry's Tacoma bar, doubling as a clearinghouse for Bigio Family money and goods",
        "description": (
            "A Tacoma bar owned and run by made man Vincent \"Bonecrusher\" DeClerry, a former Mafia "
            "soldier who 'no longer works the rough side of the business' and instead serves the Bigio "
            "Family as an accountant and numbers man. His office above the bar handles Mafia cash and "
            "goods moving through Tacoma, making the bar itself a quiet financial hub disguised as an "
            "ordinary neighborhood watering hole."
        ),
        "notes": "DeClerry no longer works the rough side of the business; treat him as an information source on Bigio Family finances if the runners can get to him.",
    },
    {
        "name": "Gianelli's Restaurant",
        "location_type": "restaurant",
        "city": "Tacoma",
        "district": "Tacoma",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "Bigio Family",
        "summary": "Former Don Tony Gianelli's retirement restaurant in Tacoma, where he still advises his protege Maurice Bigio",
        "description": (
            "The retirement business of Tony \"The Chef\" Gianelli, 'a jolly old man approaching his "
            "seventieth birthday' who owns and runs the restaurant as his retirement trade after stepping "
            "down as don in favor of his protege Maurice Bigio. He advises Maurice on all Family matters "
            "from here, worrying privately that the Mob war 'could end up hurting the Family more than "
            "helping it' while keeping such doubts to himself as 'the foolish worries of an old man.'"
        ),
        "notes": "A soft, semi-public place to find and pressure Gianelli, who is more sentimental and less guarded than Bigio himself.",
    },
    {
        "name": "St. Mary's Parish",
        "location_type": "landmark / monument",
        "district": "Bellevue",
        "security_level": "Low Security",
        "controlling_org": "Finnigan Family",
        "summary": "The Bellevue Catholic parish where the devout Mary Finnigan worships every Sunday with her family, cultivating her image as a kindly, generous grandmother",
        "description": (
            "A Bellevue Catholic parish where Mary Finnigan is 'well known as a generous parishioner,' "
            "attending services every Sunday, usually with her family in tow. Her conservative dress -- "
            "antique jewelry, an ever-present crucifix -- and her public piety there help maintain the "
            "image of a kindly grandmother that masks the devious, calculating matriarch running her "
            "branch of the Finnigan Family."
        ),
        "notes": "Named only in passing as the church Mary Finnigan attends; a plausible, low-security place to approach or observe her outside Family business.",
    },
    {
        "name": "Finnigan Family Cabin",
        "location_type": "safehouse",
        "district": "Salish-Shidhe territory, outskirts of Seattle",
        "security_level": "No Security / Barrens",
        "controlling_org": "Finnigan Family",
        "summary": "A remote cabin where James Michael Finnigan's men hold Al Cavalieri (and any captured runners) until Rowena's forced wedding can go forward",
        "description": (
            "A cabin on the outskirts of Seattle in Salish-Shidhe territory, reached along back roads that "
            "put it beyond easy Family or law-enforcement reach. Guarded by a squad of Mafia soldiers and "
            "several trained barghests that hunt intruders through the surrounding woods, it is where Al "
            "Cavalieri is held drugged and captive -- and where Patrick Finnigan and any captured runners "
            "are taken alongside him -- until James Michael and Rowena's wedding can be safely completed "
            "back at the Finnigan Family estate."
        ),
        "notes": "The Shotgun Wedding adventure framework's central set piece; the runners must either escape it or fight their way out and still reach the wedding in time.",
    },
    {
        "name": "Malenkin Import/Export",
        "location_type": "shop",
        "city": "Everett",
        "district": "Everett",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "Chimera",
        "summary": "Sergei Malenkin's legitimate-looking Everett import/export business, the only public front for the assassin organization Chimera",
        "description": (
            "A legitimate import/export business Sergei Malenkin runs out of Everett, complete with 'a "
            "sophisticated Matrix connection, some expert systems and half a dozen employees' -- all "
            "Russian refugees like Malenkin himself, 'completely loyal to him' and with 'no knowledge of "
            "their employer's real job.' It is the only point of contact through which anyone can reach "
            "Chimera to hire an assassin."
        ),
        "notes": "Reachable only by those who ask the right street contacts and score 4+ successes on an Etiquette (Street or Corporate) Test; Malenkin will pass messages to Chimera for a price but will not compromise the organization's security for any amount of nuyen.",
    },
    {
        "name": "Firebird's Apartment",
        "location_type": "penthouse",
        "district": "Downtown Seattle",
        "security_level": "Corporate High Security",
        "summary": "The luxury downtown Seattle apartment where the Chimera assassin Firebird maintains an airtight cover identity as a wealthy widow",
        "description": (
            "A luxury apartment in downtown Seattle where Natasha Romanov -- the Chimera assassin known as "
            "Firebird -- lives behind 'an airtight cover identity as a wealthy widow.' Consistent with her "
            "training as a social chameleon who shows no fixed personality of her own, nothing about the "
            "apartment or her presence there would mark it as an assassin's safehouse to a casual "
            "observer."
        ),
        "notes": "Not detailed beyond its existence and cover purpose; a plausible base for the gamemaster to build out if runners trace Firebird back to it during Tracking the Assassin.",
    },
    {
        "name": "Miko Ishikawa's Apartment",
        "location_type": "penthouse",
        "district": "Downtown Seattle",
        "security_level": "Corporate High Security",
        "controlling_org": "Shotozumi-gumi",
        "summary": "The twentieth-floor apartment of Shotozumi-gumi wakagashira-hosa Miko Ishikawa, the target of her own staged kidnapping in A Matter of Honor",
        "description": (
            "A high-security building in downtown Seattle where Miko Ishikawa keeps an apartment on the "
            "twentieth floor. Her home computer system (Blue-G/10/8/8) is 'state-of-the-art, but nothing "
            "any competent decker can't handle,' and holds the private files she wants stolen as part of "
            "her scheme to fake her own kidnapping and feed intelligence to Akira Watada without "
            "Shotozumi's knowledge."
        ),
        "notes": (
            "Miko's own agents quietly feed runners information about the building's security -- not so "
            "much that they'd wonder where it came from -- to make sure the fake kidnapping succeeds "
            "without being 'too easy.' She offers no resistance when taken and plays mildly curious about "
            "the identity of the runners' employer."
        ),
    },
    {
        "name": "Zheng Li Kwan's Residence",
        "location_type": "penthouse",
        "district": "Bellevue",
        "security_level": "Corporate High Security",
        "controlling_org": "Yellow Lotus",
        "summary": "The Yellow Lotus Lodgemaster's private home in Bellevue, holding a decoy copy of Su Cheng's soul-jar vase among his collection of ancient Chinese artwork",
        "description": (
            "Zheng Li Kwan's home in Bellevue, where the collector of ancient Chinese artwork keeps 'a "
            "copy of it in his private collection' -- a decoy version of the ancient vase that supposedly "
            "holds Su Cheng's Hidden Life, deliberately planted to mislead anyone who comes looking for "
            "the genuine article, which Zheng actually keeps warded in a Tacoma warehouse."
        ),
        "notes": "The Soul Jar adventure framework's first false lead; runners (and Su Cheng himself) must discover through legwork that the real vase is not here before they can find it in Tacoma.",
    },
    {
        "name": "Yellow Lotus Warehouse",
        "location_type": "smugglers den",
        "city": "Tacoma",
        "district": "Tacoma (warehouse district)",
        "security_level": "Corporate High Security",
        "controlling_org": "Yellow Lotus",
        "summary": "A magically warded Tacoma warehouse where Zheng Li Kwan hides the true vase holding Su Cheng's Hidden Life behind guard animals, a spell trap and a Force 5 ward",
        "description": (
            "A warehouse in Tacoma's warehouse district that handles legitimate shipments of goods bound "
            "for Triad operations across the metroplex, and secretly conceals a warded safe holding the "
            "real vase containing Su Cheng's Hidden Life. Sophisticated electronic security and paranormal "
            "guard animals (most likely cockatrices) protect the building; an anchored spell trap linked "
            "to the safe transforms any intruder but Zheng into a carp, left 'flopping helplessly on the "
            "floor, gasping for breath' for ten minutes -- long enough to suffocate -- while the safe "
            "itself sits behind a Force 5 ward. The vase, protected by Su Cheng's own Hidden Life power, "
            "has an Armor Value of 6 and a Body of 1: rough handling will not damage it, but any attack "
            "that penetrates the armor will."
        ),
        "notes": "The Soul Jar adventure framework's central heist location. The spell trap can be dispelled or destroyed in astral combat and only functions twice before it must be reset.",
    },
    {
        "name": "Restaurant near Kobe Terrace Park",
        "location_type": "restaurant",
        "district": "Seattle (near Kobe Terrace Park)",
        "security_level": "Patrolled / Commercial",
        "summary": "A small restaurant where Su Cheng, posing as an ordinary Mr. Johnson, hires runners to steal back his own soul jar -- and where the Yellow Lotus ambushes them afterward",
        "description": (
            "A small restaurant near Seattle's Kobe Terrace Park where a trusted fixer arranges for "
            "runners to meet their Mr. Johnson in a private room. He 'appears, seemingly out of thin air,' "
            "a strange Oriental man in ancient-looking black robes -- Su Cheng, though he never reveals "
            "that he is a vampire or why he really wants the ancient vase back."
        ),
        "notes": "Both the Soul Jar framework's setup meet and, unless the runners are careful, its climax: Zheng's Yellow Lotus mages magically trace the recovered vase back here and set an ambush for whoever shows up carrying it.",
    },
    {
        "name": "Choson Ring Warehouses",
        "location_type": "smugglers den",
        "district": "Seattle docks",
        "security_level": "No Security / Barrens",
        "controlling_org": "Choson Ring",
        "summary": "The Choson Ring's pair of small dockside warehouses, the operational heart of its smuggling trade and its long war with the First Nations gang",
        "description": (
            "At least two small warehouses on the Seattle docks that Kyu's Choson Ring uses 'for covert "
            "transfers and storage of contraband,' backed by numerous hideouts and boltholes across the "
            "dockside area the Ring knows intimately. The Ring regularly pays off the Metroplex Guard to "
            "ignore its operations here, and has absorbed much of the smuggling business The Cutters lost "
            "'a few years back.'"
        ),
        "notes": "Currently contested with the First Nations gang for control of Everett-dock smuggling; the Ring has also had at least one run-in with Renraku security near the Renraku Arcology.",
    },
    {
        "name": "BrightSky Finances",
        "location_type": "corporate facility",
        "city": "Fort Lewis",
        "district": "Fort Lewis",
        "security_level": "Corporate Standard",
        "summary": "A small, clean corporation in Fort Lewis whose systems hide a Matrix trapdoor into a Shigeda-gumi host -- the target of the Dirty Laundry frame job",
        "description": (
            "Offices 'exactly like the offices of every other corp of the same size,' with somewhat "
            "heavier security than usual (electronic alarms, maglocks, and hell hounds or barghests "
            "patrolling the grounds at night) given the general spike in corporate paranoia since "
            "Dunkelzahn's will. Its clean reputation and lack of any significant shadow presence make it a "
            "plausible, low-suspicion target for what looks like an ordinary data run."
        ),
        "notes": (
            "The Eighty-Eights supply forged access codes that trigger a trapdoor from BrightSky's system "
            "into the Shigeda-gumi (Takeo Shigeda)'s Matrix host (Red-10/16/18/14/16/14, Trace/Probe IC up "
            "through Killer, Blaster and Black; see MATRIX_HOSTS), framing whoever takes the job for a "
            "security breach that draws Yakuza wakagashira Jiro Egami down on the site in person."
        ),
    },
    {
        "name": "Pachinko Parlor",
        "location_type": "casino",
        "city": "Tacoma",
        "district": "Tacoma",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "Shotozumi-gumi",
        "summary": "A Tacoma Shotozumi-gumi gambling operation, targeted as a diversion in Kiku's Neon Flower heist against her own father",
        "description": (
            "One of Hanzo Shotozumi's gambling operations in Tacoma, its games house-rigged in the usual "
            "Yakuza fashion. In the Neon Flower adventure framework, shadowrunners break in, get access to "
            "the casino's main computer, and reprogram it so the rigged games 'begin blatantly cheating in "
            "favor of the patrons' -- loud enough to draw Yakuza security and cover Kiku's own burglary of "
            "her father's home elsewhere in the city."
        ),
        "notes": "Purely a diversion target in the book; no interior detail given beyond the rigged main computer. The runners must evade pursuing Yakuza soldiers and magicians for at least twenty minutes to give Kiku the time she needs.",
    },
    {
        "name": "Hanzo Shotozumi's Home",
        "location_type": "penthouse",
        "district": "Seattle",
        "security_level": "Corporate High Security",
        "controlling_org": "Shotozumi-gumi",
        "summary": "Hanzo Shotozumi's Seattle residence, burgled by his own estranged daughter Kiku while a diversion at the Pachinko Parlor pulls his security away",
        "description": (
            "Hanzo Shotozumi's home in Seattle, secure enough that his own daughter Kiku needs a loud, "
            "citywide-visible diversion just to get inside without alerting Shotozumi's security -- she "
            "tells the runners hired to stage that diversion only that 'she needs a distraction to pull it "
            "off without alerting Shotozumi's security,' and gives them no further detail about the house "
            "itself. It is here that she steals the secret files revealing her father's plan to bring a "
            "large shipment of the new BTL chip 'neon flower' -- based on the 2XS chips that hit the "
            "streets a few years back, offering 'a more powerful and addictive high than any other beetles "
            "on the street' -- into the metroplex from Yakuza suppliers in California, intending to flood "
            "the Seattle market and knock out the Mafia's and Triads' cheaper 'kong chips.'"
        ),
        "notes": "No physical description of the house itself given beyond its role as Kiku's burglary target in the Neon Flower adventure framework; build the interior to suit the table.",
    },
]

NPCS = [
    {
        "name": "James O'Malley",
        "role": "Capo of the Seattle Mafia and head of the Finnigan Family, assassinated January 1, 2058 -- the event that starts the whole Mob war",
        "archetype": "Mafia Don (deceased)",
        "title": "Former Don, Finnigan Family; former capo of Seattle",
        "race": "Human",
        "gender": "Male",
        "organization": "Finnigan Family",
        "connection": 5,
        "description": (
            "Nicknamed \"The Hammer,\" an old-fashioned man who preferred to touch and hold his day's "
            "business printed and organized by hand rather than call it up on a screen, and who could not "
            "let go of his murdered brother Brian even decades on: \"When will that fraggin' Shotozumi "
            "learn not to mess with me? I tell you, Al, that man's like the Devil. He never gives up, not "
            "in all the years I've been here.\" His dark mood broke instantly, though, at the thought of "
            "his daughter home from school: \"I didn't know she was up. ... It's good to have my little "
            "girl home, isn't it, Al?\" Recalled from forced retirement in 2044 to lead the Finnigans and "
            "hold the line against Yakuza expansion, he did so successfully for fourteen years, earning "
            "the respect of most of Seattle's caporegimes even as tensions simmered with Mary Finnigan's "
            "branch of the family."
        ),
        "background": (
            "Milwaukee capo, forced into retirement in 2031 after his obsession with avenging Brian's "
            "death wrecked his own city's operations; recalled to Seattle in 2044 when Patrick Finnigan "
            "could not hold off renewed Yakuza pressure. Shot outside on his way to breakfast the morning "
            "of January 1, 2058, by the Chimera assassin Firebird, hired secretly by the Bigio and "
            "Ciarniello dons."
        ),
        "notes": (
            "No stat block given -- he dies in the prologue before any encounter, crossing his own "
            "courtyard on a fresh snowfall to breakfast with Rowena: \"The shot was totally unexpected, "
            "almost anticlimactic ... lying face down in the snow ... a bright crimson bloodstain "
            "spreading across the whiteness like a winter flower.\" DocWagon medics who reach the scene "
            "can only pronounce him dead. His death is the entire premise of the book: the Commissione "
            "hands responsibility for naming his successor to Don McCaskill, his daughter Rowena O'Malley "
            "claims the Family and the capo's seat over his relatives-by-marriage, and every other Seattle "
            "syndicate moves to exploit the resulting Mafia disarray. His consiglieri Al Cavalieri and the "
            "Finnigan Family both build their next moves around avenging him and confirming who ordered "
            "the hit."
        ),
    },
    {
        "name": "Rowena O'Malley",
        "role": "James O'Malley's daughter and sole heir, a 28-year-old Harvard-trained lawyer claiming the Finnigan Family and the capo's seat over Mafia tradition",
        "archetype": "Mafia Princess / Negotiator",
        "title": "Heir apparent, Finnigan Family",
        "race": "Human",
        "gender": "Female",
        "organization": "Finnigan Family",
        "connection": 4,
        "description": (
            "Dark-haired, freckled and impish-looking, with a driving, ambitious personality behind the "
            "youthful face. Raised as a 'Mafia princess' but educated at Harvard and licensed to practice "
            "law in the UCAS, she has no significant combat ability but Superior negotiation, oratory and "
            "legal skill, plus a datajack, headware memory and display link."
        ),
        "background": (
            "Sent East to school by her father to shield her from Family business, she remained close to "
            "him and benefited from 'Family protection' via his friend Don Conor O'Rilley of Boston during "
            "her ten years at Harvard. With his death she claims her 'rightful place' as head of the "
            "Finnigans and capo of Seattle, believing she can modernize the Mafia while honoring its "
            "traditions -- and survives a Bigio-ordered assassination attempt within a week of the funeral."
        ),
        "notes": (
            "No significant combat abilities; Superior negotiation, oratory and legal skill (at least 2 "
            "rating points above the highest-rated player character). Datajack, headware memory, display "
            "link, no offensive or defensive cyberware. Protected at all times by an elite group of Mafia "
            "bodyguards with abilities at least equal to the player characters -- who might be the player "
            "characters themselves, if the gamemaster runs the Lady in Distress hook. Central figure of "
            "Tracking the Assassin (hires or orders the runners to find her father's killer and confirm "
            "Bigio and Ciarniello involvement, which would let her discredit both rival families and win "
            "Don McCaskill's backing) and Shotgun Wedding (the target of James Michael Finnigan's plot to "
            "kidnap Al Cavalieri and force her into a marriage that would surrender her claim to the "
            "Finnigan Family and the capo's seat under Mafia tradition). Rescued from the forced wedding, "
            "she leaves James Michael at the altar; either way she continues her push to consolidate power "
            "and avenge her father, and can call on grateful runners for future work."
        ),
    },
    {
        "name": "Al Cavalieri",
        "role": "The Finnigan Family's consiglieri, James O'Malley's oldest friend and Rowena's closest advisor",
        "archetype": "Mafia Advisor",
        "title": "Consiglieri, Finnigan Family",
        "race": "Human",
        "gender": "Male",
        "organization": "Finnigan Family",
        "connection": 4,
        "description": (
            "\"Uncle Al\" to Rowena since her birth, a man in his late fifties whose combat skills have "
            "faded but whose Negotiation and Etiquette are Superhuman, with a Superior understanding of "
            "the Yakuza earned negotiating peace in multiple cities. No cyberware; rumors of a "
            "superthyroid gland explaining his appetite are unconfirmed."
        ),
        "background": (
            "Worked alongside James O'Malley for more than thirty years, moderating his worst revenge-"
            "driven impulses against the Yakuza. Arranged the Finnigan Family's two-year deal with the "
            "magical gang the Merlyns. Considered an 'outsider' by native Seattle Mafiosi like the other "
            "Milwaukee transplants, which is why he needs Rowena to succeed. Stood over O'Malley's body "
            "in the courtyard the instant he was shot, already thinking past his grief: \"Forgive me, "
            "Jimmy, he thought. He would mourn his friend later. Right now, he was consiglieri of the "
            "Finnigan family, and the King was dead.\""
        ),
        "notes": (
            "Skills roughly Inferior to Equal against the player characters in a straight fight (his late "
            "fifties have caught up with him), but his Negotiation and Etiquette are Superhuman and his "
            "understanding of the Yakuza -- earned negotiating peace between the two syndicates in "
            "multiple cities, including Los Angeles and New York -- is Superior. Considered a Superior "
            "street-level tactician after thirty years of survival. No cyberware; the superthyroid-gland "
            "rumor is unconfirmed. Kidnapped by agents of James Michael Finnigan in the Shotgun Wedding "
            "adventure framework to force Rowena into a marriage that would surrender her claim; held "
            "drugged in the Finnigan Family Cabin in Salish-Shidhe territory until the runners free him "
            "and get him back to the Finnigan Family estate in time to stop the wedding. If they succeed, "
            "both Rowena and Patrick Finnigan gain a debt to the runners; James Michael and Mary Finnigan "
            "do not forget the interference."
        ),
    },
    {
        "name": "Mary Finnigan",
        "role": "The 78-year-old widow of founder Ian Finnigan, plotting for decades to install her grandnephew as head of the Family",
        "archetype": "Mafia Matriarch",
        "title": "Widow of founder Ian Finnigan",
        "race": "Human",
        "gender": "Female",
        "organization": "Finnigan Family",
        "connection": 3,
        "description": (
            "\"Too damn stubborn to die,\" in Al Cavalieri's phrase -- a devout, generous parishioner of "
            "St. Mary's Parish in Bellevue who looks closer to sixty than eighty thanks to Sixth World "
            "medicine, dresses conservatively in antique jewelry and an ever-present crucifix, and rules "
            "her immediate family with an iron fist behind a kindly-grandmother facade. Deeply prejudiced "
            "against magic despite an unrecognized latent gift of her own -- Superior Spell Defense she "
            "attributes to divine grace, not innate talent, having used it only twice in her life and "
            "credited both to \"God's grace\" protecting her and her loved ones from \"Devil-spawned "
            "magic.\""
        ),
        "background": (
            "Watched her husband Ian and both sons murdered by Yakuza reprisals, then watched the "
            "Commissione twice impose Milwaukee outsiders (Brian, then James O'Malley) over her family "
            "rather than trust her nephew Patrick or, later, her grandnephew James Michael. Sees O'Malley's "
            "death as a God-given opportunity to finally install a true Finnigan -- James Michael -- as "
            "capo, with only Rowena O'Malley standing in the way."
        ),
        "notes": (
            "No significant combat abilities; Negotiation and Etiquette Superior (at least 2 points higher "
            "than the player characters). Her one latent gift, Spell Defense, is roughly Equal to an "
            "average player-character magician's but she has invoked it only twice in her life and does "
            "not understand it as magic at all. Rules the Finnigan Family's internal politics as its real "
            "power broker even when not formally in charge, having controlled Patrick Finnigan throughout "
            "his fourteen years as capo and now grooming his son James Michael to replace Rowena O'Malley. "
            "Al Cavalieri suspects she may have had a hand in arranging O'Malley's murder, but fears her "
            "too much to voice it; her endgame in the Shotgun Wedding adventure framework is thwarted if "
            "the runners free Al Cavalieri and reach the wedding in time, but she remains a long-term "
            "obstacle to Rowena's consolidation of power."
        ),
    },
    {
        "name": "Patrick Finnigan",
        "role": "Weak former capo of Seattle turned Matrix-savvy accountant, quietly supporting Rowena over his own son's ambitions",
        "archetype": "Decker / Accountant",
        "title": "Caporegime; former Don, Finnigan Family",
        "race": "Human",
        "gender": "Male",
        "organization": "Finnigan Family",
        "connection": 2,
        "description": (
            "A balding, overweight, soft-spoken Matrix geek in ill-fitting suits, with almost no combat "
            "skill (Inferior Firearms) but Superior ability in Matrix accounting and finance "
            "applications -- he knows every trick for hiding, transferring and laundering illegal funds."
        ),
        "background": (
            "A capable young Mafia accountant, good with computers and with a love of the Matrix that "
            "'made the electronic world feel like a second home,' when Brian O'Malley became capo of "
            "Seattle at 25; secretly relieved rather than resentful, he swore loyalty without a quibble "
            "over Mary Finnigan's objections and went back to his books. Four years later, Brian's death "
            "forced him to take up the family mantle himself; he did the job capably but joylessly for "
            "fourteen years, unable to match O'Malley's or his uncle Ian's fire, and gladly retired again "
            "when James O'Malley took over in 2044 -- 'arguing with his aunt Mary that day, standing up to "
            "her for the first time in his memory.' Strongly suspects Mary had a hand in O'Malley's murder "
            "but is too afraid of her to say so; supports Rowena's claim, which brings the Family's "
            "official backing with him as nominal 'head of household.'"
        ),
        "notes": (
            "Almost no combat skill (Inferior Firearms, at least 2 points below the average player "
            "character, minimum 1). His real strength is the Matrix: Inferior general Computer Skill next "
            "to a player-character decker, but Superior (at least 2 points) in accounting and finance "
            "applications specifically -- he knows every trick for hiding, transferring and laundering "
            "illegal funds. Secretly the Mr. Johnson behind Shotgun Wedding, hiring runners via an "
            "anonymous Matrix icon to free the kidnapped Al Cavalieri and stop his own son's forced "
            "marriage to Rowena before it can go through; reveals his identity to the runners partway "
            "through when they might otherwise suspect a double-cross. Afraid of what his son and aunt "
            "might do to him if they learn of his interference, so keeps a low profile and stays out of "
            "everyone's way afterward."
        ),
    },
    {
        "name": "James Michael Finnigan",
        "role": "Patrick Finnigan's ambitious son, Mary Finnigan's chosen heir, obsessed with marrying Rowena O'Malley to seize the Family",
        "archetype": "Caporegime",
        "title": "Caporegime, Finnigan Family (\"Jimmy Mac\")",
        "race": "Human",
        "gender": "Male",
        "organization": "Finnigan Family",
        "connection": 3,
        "description": (
            "Twenty-nine, ambitious and aggressive, with the abilities of a former Company Man roughly "
            "Equal to an average player character. Chafed under James O'Malley's rule and nurses a "
            "near-obsessive adolescent crush on Rowena that has curdled into a plan to marry his way into "
            "power."
        ),
        "background": (
            "Raised by his great-aunt Mary Finnigan on stories of how the rightful Finnigan birthright had "
            "been stolen away 'not once, but twice' by the O'Malleys and the Commissione. Knew Rowena in "
            "her teens, before she went East to school, and developed an adolescent crush that has since "
            "'blossomed into a near-obsession'; Rowena considers him crude, cruel and classless and has no "
            "interest in him whatsoever. Completely under Mary's sway -- if he ever becomes capo of "
            "Seattle he would likely rely on her advice, 'though the power might go to his head' and "
            "prompt him to stop listening to anyone at all."
        ),
        "notes": (
            "Skills roughly Equal to an average player character, per the former Company Man archetype; "
            "does not have strong Etiquette or Negotiation on his own, but with Mary quietly coaching him "
            "he can appear more capable at both than he really is. Arranges Al Cavalieri's kidnapping in "
            "the Shotgun Wedding adventure framework to pressure Rowena into marrying him before she can "
            "consolidate power on her own, using a captured 'contact' inside the Finnigan Family to set a "
            "trap for whoever comes looking for Cavalieri. If the runners rescue Cavalieri and reach the "
            "wedding in time, Rowena leaves him at the altar and he and Mary Finnigan hold a lasting grudge "
            "against the runners."
        ),
    },
    {
        "name": "Maurice Bigio",
        "role": "Don of the Bigio Family, who arranged James O'Malley's assassination through Chimera and is now maneuvering to betray his co-conspirator Don Ciarniello",
        "archetype": "Mafia Don",
        "title": "Don, head of the Bigio Family",
        "race": "Human",
        "gender": "Male",
        "organization": "Bigio Family",
        "connection": 4,
        "description": (
            "\"The Butcher\" -- a large, physically intimidating man (minimum Body and Strength 7) whose "
            "dark stare cows even hardened soldiers. Combat skills Equal to the player characters, no "
            "cyberware; Inferior Negotiation and Etiquette but Superior Leadership and Interrogation."
        ),
        "background": (
            "Started as a soldatos, becoming a made man twenty-seven years ago while Patrick Finnigan ran "
            "Seattle; rose through the ranks as caporegime and eventual protege of the aging Don Gianelli, "
            "who had no sons of his own, earning his nickname through the brutality of the 'object "
            "lessons' he administered on Gianelli's behalf. Wanted the top spot from Patrick Finnigan but "
            "lost his chance to James O'Malley, so swore loyalty and worked with him against the Yakuza "
            "while biding his time. Once the Yakuza threat eased, he made overtures to Don Vince "
            "Ciarniello and the two together hired the assassin organization Chimera to remove O'Malley -- "
            "each secretly planning to betray the other once the Finnigans are neutralized."
        ),
        "notes": (
            "Minimum Body and Strength 7; combat skills Equal to the player characters, no cyberware. "
            "Inferior Negotiation and Etiquette but Superior Leadership and Interrogation -- his "
            "interrogation sessions 'usually end with Maurice getting what he wants and the pigeon ending "
            "up in Puget Sound.' Needs to accomplish three things to secure the capo's seat: neutralize "
            "Rowena O'Malley and the Finnigans, deal with his increasingly unreliable ally Vince Ciarniello "
            "(willingly, through blackmail, or by force if it comes to that), and beat back the Yakuza or "
            "anyone else muscling in on Mafia turf. Pays Chimera to send Firebird after any runners who "
            "get too close to the truth of the assassination during Tracking the Assassin; if exposed, "
            "becomes Rowena O'Malley's primary target for revenge."
        ),
    },
    {
        "name": "Marleen Bigio",
        "role": "Don Maurice Bigio's socially prominent wife, a route into the Bigio household through Tacoma's arts and media scene",
        "archetype": "Mafia Wife",
        "title": "Wife of Don Maurice Bigio",
        "race": "Human",
        "gender": "Female",
        "organization": "Bigio Family",
        "connection": 2,
        "description": "The ideal quietly supportive, not-too-curious Mafia wife, who spends most of her time patronizing whatever artistic or media fad strikes her as worthy in a given month.",
        "notes": (
            "No stats given -- a purely social figure, never a combatant. Her lavish parties are the "
            "book's suggested way for runners to get close to her or to Don Maurice, or simply to case the "
            "Bigio Family Mansion in Tacoma without raising suspicion."
        ),
    },
    {
        "name": "Tony Gianelli",
        "role": "Maurice Bigio's mentor and consiglieri, a retired don running a Tacoma restaurant and privately worried the Mob war will hurt the Family",
        "archetype": "Retired Mafia Don",
        "title": "Consiglieri, Bigio Family",
        "race": "Human",
        "gender": "Male",
        "organization": "Bigio Family",
        "connection": 2,
        "description": "\"The Chef\" -- a jolly old man approaching his seventieth birthday who owns and runs Gianelli's Restaurant in Tacoma as his retirement business.",
        "background": "The don who groomed Maurice Bigio as his protege and successor before retiring into the restaurant trade; still advises Maurice on all Family matters as his consiglieri.",
        "notes": (
            "No stats given -- a mentor and advisor, not a fighter. Privately worries the conflict could "
            "end up hurting the Family more than helping it, but has so far kept those doubts to himself, "
            "believing them to be nothing more than 'the foolish worries of an old man.'"
        ),
    },
    {
        "name": "Vincent DeClerry",
        "role": "Bigio Family made man who runs a Tacoma bar as a clearinghouse for Mafia money and goods",
        "archetype": "Mafia Accountant",
        "title": "Accountant / numbers soldier, Bigio Family",
        "race": "Human",
        "gender": "Male",
        "organization": "Bigio Family",
        "connection": 2,
        "description": "\"Bonecrusher\" -- a former Mafia soldier turned accountant and numbers man, longtime associate of Maurice Bigio who goes back with him a long way.",
        "background": "A made man in the Bigio Family who left the rough side of the business behind for the numbers side, but kept the nickname from his soldier days.",
        "notes": "No stats given. Owns and runs the Tacoma bar (DeClerry's) that bears his name; his office above it serves as a clearinghouse for Mafia money and goods moving through Tacoma, making him a useful information source on Bigio Family finances if runners can get to him.",
    },
    {
        "name": "Vince Ciarniello",
        "role": "Fear-driven don of the Ciarniello Family, who agreed to O'Malley's murder to protect himself and is unaware his own wife is robbing him",
        "archetype": "Mafia Don",
        "title": "Don, head of the Ciarniello Family (\"Numbers\")",
        "race": "Human",
        "gender": "Male",
        "organization": "Ciarniello Family",
        "connection": 3,
        "description": (
            "Fifty-five, originally a middle manager with an eye for efficiency who became don after his "
            "uncle's death in Yakuza conflict. Superior business acumen; other skills roughly Equal to the "
            "player characters; datajack and headware memory, Matrix skills Equal."
        ),
        "background": (
            "Agreed to Maurice Bigio's plan to kill O'Malley out of fear -- fear his past indiscretions "
            "would surface, fear of losing his position, and fear of what O'Malley might do to him after "
            "discovering a caporegime skimming Casino Corner's take on Vince's watch. Primarily wants to "
            "survive the Mob war with his position intact."
        ),
        "notes": (
            "Superior business acumen (at least 2 points above the player characters); other skills "
            "Equal, with a datajack, headware memory and Equal Matrix skills. Not squeamish or weak "
            "despite his fears -- runs Casino Corner profitably and deals with his enemies 'ruthlessly and "
            "efficiently' when he has to. Agreed to Bigio's assassination plot purely out of fear of what "
            "O'Malley might do to him, and now wants above all to come out of the Mob war alive and ahead. "
            "Will fold and name Maurice Bigio as the real mastermind if confronted with solid enough "
            "evidence of his own involvement, in Tracking the Assassin. Grateful and forgiving of his "
            "wife's public behavior in Blood Money, but privately furious at her betrayal once it comes "
            "out; makes an example of Dan Grizetti and puts the money-skimming scandal to rest to "
            "strengthen his own position in the Mob war."
        ),
    },
    {
        "name": "Ivy Ciarniello",
        "role": "Vince Ciarniello's much younger elf wife, secretly embezzling Family funds with her lover Dan Grizetti and planning to flee the country",
        "archetype": "Mafia Wife / Grifter",
        "title": "Wife of Don Vince Ciarniello",
        "race": "Elf",
        "gender": "Female",
        "organization": "Ciarniello Family",
        "connection": 2,
        "description": (
            "A poor Barrens orphan (born Ivy Broadstreet, orphaned in the Night of Rage) who worked as a "
            "dancer and waitress at Casino Corner before catching Vince's eye; the whole Family knows she "
            "\"can wrap her husband around her little finger\" and resents her for it. No combat skill, "
            "but social skills and Charisma Equal to the player characters, minimum Charisma 8."
        ),
        "background": (
            "Married Vince four years ago and enjoys the wealth and influence but wants more. Has spent "
            "the marriage carefully cultivating an affair with consiglieri Dan Grizetti, using it to skim "
            "gambling profits with him -- the two plan to abscond overseas, leaving Vince and any runners "
            "involved to take the blame."
        ),
        "notes": (
            "No combat skill; social skills and Charisma Equal to the player characters, minimum Charisma "
            "8. Despised by Vince's son Caesar, partly out of straightforward anti-elf prejudice. Central "
            "to the Blood Money adventure framework: she and Dan Grizetti intend to abscond with skimmed "
            "Family money via a Sea-Tac flight, framing Vince (and any runners hired to recover the "
            "'Golden Goose' blackmail file) to take the blame. If confronted at the airport and returned "
            "to Vince, he pins the money-skimming scam entirely on Grizetti to keep her; she returns to "
            "life as a Mafia wife, though Vince's trust in her never fully recovers and she or Vince may "
            "later see runners who know the truth as a liability."
        ),
    },
    {
        "name": "Dan Grizetti",
        "role": "Ciarniello Family consiglieri, having an affair with Don Vince's wife and quietly leaking blackmail material to frame him",
        "archetype": "Mafia Consiglieri",
        "title": "Consiglieri, Ciarniello Family (\"Fancy Dan\")",
        "race": "Human",
        "gender": "Male",
        "organization": "Ciarniello Family",
        "connection": 3,
        "description": (
            "A dashingly handsome made man with a taste for the finest suits, cars and surroundings; a new "
            "generation Mafioso with the abilities of a former Company Man, roughly Equal to the player "
            "characters."
        ),
        "background": (
            "Drawn to Ivy from the moment he met her, and used by her ever since; leaked the 'Golden "
            "Goose' blackmail file on Vince to Maurice Bigio in the first place to make Vince look more "
            "guilty in the Mob war, while he and Ivy quietly skim Family funds for their planned escape."
        ),
        "notes": (
            "Abilities of the former Company Man archetype, roughly Equal to the player characters. Leaked "
            "the 'Golden Goose' blackmail file (evidence Vince let subordinates skim Casino Corner's take) "
            "to Maurice Bigio in the first place, turning what should have been a simple recovery job into "
            "a tailchaser that makes Vince look even more guilty. Blind to how thoroughly Ivy is using him "
            "-- 'he likes to think that he's different from the other people Ivy has used in the past' -- "
            "and likely to be made an example of by Vince once the embezzlement scheme unravels in Blood "
            "Money."
        ),
    },
    {
        "name": "Caesar Ciarniello",
        "role": "Vince Ciarniello's son and heir, a cybered Mafia punk who despises his father's elf wife",
        "archetype": "Mafia Heir",
        "title": "Heir apparent, Ciarniello Family (\"Chrome\")",
        "race": "Human",
        "gender": "Male",
        "organization": "Ciarniello Family",
        "connection": 2,
        "description": (
            "Twenty-eight, used to the privileges of his position, regularly reprimanded by his father for "
            "throwing his weight around. Muscle and reflex augmentation, cybereyes and retractable hand "
            "razors; combat abilities roughly Equal to the average player character."
        ),
        "background": "Took an instant, openly prejudiced dislike to his father's new wife Ivy on sight, convinced that \"everyone knows\" elves are \"devious, sneaky, underhanded slitches,\" and has repeatedly tried, unsuccessfully, to convince Vince she is a gold-digging fraud.",
        "notes": (
            "Combat abilities roughly Equal to the average player character, backed by muscle and reflex "
            "augmentation, cybereyes and retractable hand razors he uses mainly to intimidate people. Will "
            "actively try to pin any suspicious activity on Ivy if runners come sniffing around the "
            "Ciarniello household, seeing it as his chance to finally get her 'out of his father's life' -- "
            "his blatant prejudice undercuts his own credibility with Vince every time he tries."
        ),
    },
    {
        "name": "Sergei Malenkin",
        "role": "Chimera's Russian-expatriate public contact, running a legitimate Everett import/export business as a front",
        "archetype": "Fixer / Broker",
        "title": "Public contact, Chimera",
        "race": "Human",
        "gender": "Male",
        "connection": 4,
        "description": (
            "A Russian immigrant whose combat skills are Equal to the player characters but whose "
            "Negotiation, Interrogation and Leadership are Superior. Runs an Everett import/export office "
            "staffed by six Russian refugees who know nothing of his real business."
        ),
        "background": "Possibly a former Chimera assassin himself; now the organization's power broker and gatekeeper, reachable by player characters only if they speak with the right contacts and score 4 or more successes on an Etiquette (Street or Corporate) Test.",
        "notes": (
            "Combat skills Equal to the player characters; Negotiation, Interrogation and Leadership "
            "Superior. Will not compromise Chimera's security for any price or reveal information about "
            "the organization's clients, but might be persuaded to pass along messages and information for "
            "the right price. Sole interest is protecting his own position and Chimera's reputation, not "
            "any particular outcome of the Mob war."
        ),
    },
    {
        "name": "Firebird",
        "role": "Chimera's KGB-trained assassin, who shot Don James O'Malley from concealment with a custom sniper rifle",
        "archetype": "Assassin",
        "title": "Assassin, Chimera",
        "race": "Human",
        "gender": "Female",
        "connection": 3,
        "description": (
            "Natasha Romanov -- a social chameleon with almost no fixed personality of her own, trained by "
            "the KGB as spy and kick artist, living under an airtight cover identity as a wealthy widow in "
            "a luxury downtown Seattle apartment. Superhuman in most respects, with heavy alpha- and "
            "beta-grade cyber- and bioware; master of all forms of combat."
        ),
        "background": (
            "A Russian expatriate trained by the KGB as a government spy and kick artist before Chimera "
            "was formed out of the wreckage of Russian intelligence following the EuroWars troubles in "
            "Moscow. Shot O'Malley from a great distance with a custom rifle and ammunition, using "
            "knowledge of his schedule and the means to bypass his formidable home security -- 'she is "
            "very good at what she does and prides herself on professionalism.' Has no discernible "
            "accent and is adept at using clothing, makeup and mannerisms to radically alter her "
            "appearance."
        ),
        "notes": (
            "Superhuman for most purposes -- the gamemaster can use the Cyber Assassin archetype "
            "(Cybertechnology p.89) as a guideline. A master of all forms of combat, skills at least 2 "
            "points higher than any player character, with a great deal of alpha- and beta-grade cyber- "
            "and bioware. Sent by a panicked Maurice Bigio to eliminate anyone who gets close to the truth "
            "of the assassination; the climax of Tracking the Assassin, most likely by kidnapping one or "
            "more of the runners' contacts and forcing calls that lure them into a prepared trap. If "
            "necessary the gamemaster can give her street muscle 'on loan' from Bigio to even the odds "
            "against a group. May survive an apparent death via a cybernetic or magical fail-safe from "
            "Chimera and become a recurring Enemy at the gamemaster's discretion."
        ),
    },
    {
        "name": "Saturn",
        "role": "Leader of the Merlyns, a Grade 3 hermetic initiate rumored to be the illegitimate son of the murdered Michael Finnigan",
        "archetype": "Hermetic Mage",
        "title": "Leader, Merlyns",
        "race": "Human",
        "gender": "Male",
        "organization": "Merlyns",
        "connection": 3,
        "description": "A Superior hermetic mage (all skills Superior to the player characters) who refuses to divulge his real name, increasingly a power broker and researcher who leaves front-line magical combat to his three lieutenants.",
        "background": "Took the gang name Saturn on initiation, as all Merlyns rename themselves for an astronomical body (planets for leadership, constellations for the second tier, comets and distant objects for new recruits) after 'rejecting the past.' Some say his underlings are expected to call him 'Don Saturn,' though that could be a rumor spread by his enemies.",
        "notes": "If the rumor that he is the illegitimate son of the murdered Michael Finnigan is true, he is Mary Finnigan's grandson -- a secret with obvious leverage potential either for or against the Merlyns' standing with the Finnigan Family, and a possible thread for a gamemaster who wants to complicate Mary's plans for James Michael.",
    },
    {
        "name": "Mercury",
        "role": "Merlyns lieutenant who educates Mafia troops in basic magic and crafts foci, fetishes and spell locks for the Family",
        "archetype": "Hermetic Mage",
        "title": "Lieutenant / head educator, Merlyns",
        "race": "Human",
        "gender": "Male",
        "organization": "Merlyns",
        "connection": 2,
        "description": "An 'ordinary-looking practicer of Satan's filth,' as Mary Finnigan once called him -- nothing about his appearance marks him as the gang's magical instructor.",
        "notes": "No formal rating given beyond his role. Teaches basic magic to the made men and goons of the Seattle Mafia, and has personally added magical protection to many of the Mafia's holdings and created foci, fetishes and permanent spells for Mafia warriors.",
    },
    {
        "name": "Venus",
        "role": "Merlyns lieutenant, Saturn's lover and the gang's real strategic brain, running a profitable telesma-smuggling operation for the Mafia",
        "archetype": "Hermetic Mage",
        "title": "Lieutenant, Merlyns",
        "race": "Elf",
        "gender": "Female",
        "organization": "Merlyns",
        "connection": 3,
        "description": "An extremely beautiful elf mage widely believed to have been the Merlyns' brains from the start -- 'some say' this has been true since before Saturn rose to lead the gang.",
        "background": "Began working with Don James O'Malley nearly two years ago to smuggle talismans and telesma out of the CFS, Tir Tairngire and the NAN, and has built an extensive network of magical contacts across North America running the pipeline.",
        "notes": "No individual rating given. Saturn's lover as well as his lieutenant; the smuggling operation she convinced the Mafia to back has become a profitable sideline for both the Merlyns and the Mob, and gives her personal reach into the magical underworld well beyond Seattle.",
    },
    {
        "name": "Mars",
        "role": "Merlyns lieutenant and warlord, coordinating the gang's magical support in Mafia combat operations",
        "archetype": "Hermetic Mage",
        "title": "Lieutenant / warlord, Merlyns",
        "race": "Human",
        "gender": "Male",
        "organization": "Merlyns",
        "connection": 2,
        "description": "The quickest of Saturn's lieutenants to adopt the Mafia's kill-or-be-killed mindset; supervises the gang's mages whenever the Merlyns deploy in the field.",
        "notes": "No individual rating given. The Merlyns' warlord, he coordinates magical support whenever the Mafia wants a target hit with sorcery, and is rumored to run part of the current initiation's physical-test component alongside the older escalating-spellcasting ordeal.",
    },
    {
        "name": "Shiro Tanaka",
        "role": "Wakagashira (second in command) of the Shotozumi-gumi, utterly loyal to Hanzo Shotozumi",
        "archetype": "Yakuza Lieutenant",
        "title": "Wakagashira, Shotozumi-gumi",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Shotozumi-gumi",
        "connection": 3,
        "description": (
            "A long-time associate of Shotozumi who knows his oyabun's needs and ambitions intimately; "
            "has the abilities of the Company Man archetype with dated or heavily upgraded cyberware. "
            "Social and combat skills 1-2 points higher than the player characters."
        ),
        "notes": (
            "Social and combat skills 1-2 points higher than the player characters (Superior), per the "
            "Company Man archetype with either dated cyberware or a great deal spent quietly on upgrades "
            "to keep his edge. Trusted with Shotozumi's most delicate business matters when necessary; "
            "Shotozumi knows Tanaka 'would lay down his life for him or for the gumi at his command.' Not "
            "overly fond of his assistant Miko Ishikawa but tolerates her because her work is 'supremely "
            "efficient,' and suspects she may not owe Shotozumi her complete loyalty -- but has no proof "
            "and has not yet brought his suspicions to the oyabun."
        ),
    },
    {
        "name": "Miko Ishikawa",
        "role": "Wakagashira-hosa of the Shotozumi-gumi, a rare female power-holder in the Yakuza secretly spying for Akira Watada",
        "archetype": "Yakuza Lieutenant / Spy",
        "title": "Wakagashira-hosa, Shotozumi-gumi",
        "race": "Human",
        "gender": "Female",
        "nationality": "Japanese",
        "organization": "Shotozumi-gumi",
        "connection": 3,
        "description": "Rose from kobun to assistant second-in-command through skilled administration and clever leadership, reminding Shotozumi enough of his missing daughter Keiko that he set aside some of his tradition-bound views on women in the gumi to promote her.",
        "background": (
            "Began as an ordinary kobun in the Shotozumi-gumi years ago; her initiative and ambition drew "
            "the attention of superiors who were forced to acknowledge her skilled administration and "
            "clever leadership 'despite her gender.' Stepped smoothly into the second-in-command's "
            "assistant role when her predecessor died in a 2056 clash with the Mafia, handling the crisis "
            "well enough that Shotozumi-sama decided it would be 'shameful not to recognize her "
            "achievement' and promoted her -- since then she has 'worked doubly hard' to prove herself "
            "worthy of the position. Reports Shotozumi's activities directly to Akira Watada in Japan out "
            "of her own driving ambition to one day become an oyabun herself, knowing she must be twice as "
            "capable as any male rival to get there."
        ),
        "notes": (
            "No significant combat ability beyond Firearms Equal to the player characters. Understandably "
            "paranoid, always alert for any threat to her position. Central to the A Matter of Honor "
            "adventure framework: she hires runners to fake her own kidnapping and delete/exfiltrate her "
            "private files, posing the job as a Seoulpa Ring operation so she can 'escape' afterward as an "
            "innocent victim. The scheme goes sideways when Shotozumi traces suspicious activity to her "
            "own agent (who dies in a gun battle rather than betray her) and sends soldiers to ambush "
            "whoever shows up at the planned handoff meeting; she reveals her true plan to the runners only "
            "if it becomes the only way to save her own life, and otherwise continues playing them as "
            "patsies."
        ),
    },
    {
        "name": "Toju Shotozumi",
        "role": "Hanzo Shotozumi's cousin, running the gumi's corporate blackmail (sokaiya) branch under the name Isogashii",
        "archetype": "Corporate Blackmailer",
        "title": "Head of sokaiya operations (Isogashii), Shotozumi-gumi",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Shotozumi-gumi",
        "connection": 3,
        "description": (
            "A slim, proper, clean-shaven man who styles himself a 'businessman' rather than a gangster "
            "and shows obvious distaste for shadowrunners and street types. Beta-grade datajack, headware "
            "memory, cybereyes and cyberears with professional add-ons; Inferior combat and general Matrix "
            "skills but Superior business-software Matrix skill on a state-of-the-art Fairlight Excalibur "
            "deck, and Superior social skills."
        ),
        "background": "The son of Hanzo Shotozumi's father's brother, placed in charge of the gumi's sokaiya branch by his oyabun cousin. Loyal and effective, he runs the Isogashii, the gumi's primary sokaiya organization, brokering stock and boardroom influence traditionally within Japanese-run corporations -- a restriction that has begun to loosen over the past decade as the sokaiya push into non-Japanese business.",
        "notes": "Inferior combat skills and general Matrix ability next to the player characters, but Superior on any Matrix activity involving business software on his state-of-the-art Fairlight Excalibur deck, and Superior social skills otherwise. Deals harshly with anyone, runner or otherwise, who threatens the Isogashii's corporate profits; player characters who get involved in the Yakuza's corporate interests will run into him sooner or later.",
    },
    {
        "name": "Kiku",
        "role": "Hanzo Shotozumi's estranged daughter, a shadowrunner decker who hates the Yakuza and secretly works against her father",
        "archetype": "Decker",
        "title": "Shadowrunner (born Keiko Shotozumi)",
        "race": "Human",
        "gender": "Female",
        "nationality": "Japanese",
        "connection": 2,
        "description": (
            "Uses the Human Decker archetype; decking skills Equal to the player characters, rising to "
            "Superior against Yakuza systems. Well known in the shadows as a capable data thief who "
            "specializes in running against the Japanacorps."
        ),
        "background": (
            "Raised to be 'a proper Japanese girl' but endlessly fascinated by the world outside her "
            "family's sheltering walls; found Seattle 'scruffy and chaotic compared to the orderly, clean "
            "cities of Japan, but also full of different and interesting people' after the family's move. "
            "Grew more defiant with age, using her considerable computer skills to secretly learn about "
            "the outside world despite her father's severe punishments -- punishments her mother allowed, "
            "which Keiko grew to despise her for. Just after turning nineteen, she gathered her "
            "possessions and a small amount of money siphoned from Yakuza accounts and disappeared into "
            "the Seattle shadows, taking the street name Kiku (a pun on Keiko, meaning chrysanthemum). Has "
            "run for eight years, never sharing her true past with anyone for fear of being used as a tool "
            "against her father."
        ),
        "notes": (
            "Central to the Neon Flower adventure framework: contacts the runners (whom she may already "
            "know by reputation) with a job that requires breaking into her father's Seattle home. She "
            "needs a diversion -- runners staging a fake run against a Shotozumi-gumi gambling operation "
            "in Tacoma (the Pachinko Parlor) to draw Yakuza security away for at least twenty minutes -- "
            "while she burgles Hanzo Shotozumi's secret files. What she finds is worse than expected: a "
            "shipment of a powerful new BTL chip, 'neon flower,' that the Yakuza plans to flood the Seattle "
            "market with to seize the chip trade from the Mafia and Triads. She hires the runners again to "
            "help destroy the shipment in a dockside firefight, which may make Shotozumi a personal enemy "
            "of the runners but earns Kiku's lasting friendship if they act honorably toward her."
        ),
    },
    {
        "name": "Takeo Shigeda",
        "role": "Oyabun of the Shigeda-gumi, the most progressive and least powerful of Seattle's three Yakuza clans",
        "archetype": "Yakuza Oyabun",
        "title": "Oyabun, Shigeda-gumi",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Shigeda-gumi (Takeo Shigeda)",
        "connection": 3,
        "description": "Born in San Francisco, a 23-year Seattle resident whose watchwords are safety and prosperity rather than aggressive expansion; prefers to see things run smoothly and without problems.",
        "background": "Rebuilt a gumi from the remnants of clans decimated by the purge of Korean leadership in the Schism, drawing mostly on long-time Seattle dwellers like himself rather than transplants from Japan.",
        "notes": (
            "No formal rating given. Most likely to side with whatever forces in the Yakuza seem in "
            "control and most likely to stay that way. His tolerant attitude toward women and magicians in "
            "the gumi's ranks -- more of both than the Shotozumi-gumi or Nishidon-gumi allow, though "
            "traditional restrictions on metahumans remain intact -- has kept the Shigeda-gumi from "
            "progressing in its operations and standing within the rengo as rapidly as its more "
            "conservative rivals. His underlings' habit of handling problems themselves rather than "
            "bringing them to him gives the gumi's lower ranks useful initiative most of the time, but also "
            "means he sometimes hears about trouble only once it has reached crisis proportions -- as when "
            "Jiro Egami has to investigate a security breach at BrightSky Finances days after the fact."
        ),
    },
    {
        "name": "Jiro Egami",
        "role": "Shigeda-gumi wakagashira, cautious and quick to notice a security breach at Yakuza-linked facilities",
        "archetype": "Yakuza Lieutenant",
        "title": "Wakagashira, Shigeda-gumi",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Shigeda-gumi (Takeo Shigeda)",
        "connection": 2,
        "description": "A cautious man who will immediately notice anything wrong at a facility under his watch, and personally verifies security at Yakuza-linked sites when Takeo Shigeda gets late word of a possible breach.",
        "notes": (
            "No formal rating given. Arrives at BrightSky Finances with a squad of Yakuza soldiers roughly "
            "matching a runner team in numbers during the Dirty Laundry adventure framework, after Takeo "
            "Shigeda's belated discovery of evidence suggesting a security breach there; takes appropriate "
            "precautions if the runners have left any clear evidence of their presence, which may turn "
            "into a straight fight or a tense stand-off if the runners try to bluff or flee instead. May be "
            "accompanied by a Yakuza mage (Former Wage Mage archetype) if the runners are packing "
            "significant magical firepower."
        ),
    },
    {
        "name": "Isao Nishidon",
        "role": "Oyabun of the Nishidon-gumi, the oldest Yakuza clan in Seattle and Hanzo Shotozumi's bitterest internal rival",
        "archetype": "Yakuza Oyabun",
        "title": "Oyabun, Nishidon-gumi",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Nishidon-gumi",
        "connection": 3,
        "description": "A traditionalist who earned his own gumi through decisive action rather than seniority alone.",
        "background": (
            "When the Watada-rengo's order came down to purge Koreans from the Seattle Yakuza, Nishidon "
            "acted on his own initiative and eliminated his own clan's Korean oyabun before the official "
            "order even arrived -- 'restoring order' with minimal loss of property or business. Akira "
            "Watada rewarded him with oyabun status over his own gumi for it. He was soon eclipsed by "
            "Hanzo Shotozumi, who became head of a more powerful gumi and Watada's voice among the Seattle "
            "Yakuza, and has 'nursed a grudge against him ever since.'"
        ),
        "notes": "No formal rating given. The most likely internal obstacle if Shotozumi tries to formalize his own independent West Coast rengo; the book leaves it to the gamemaster to decide how far his resentment might push him to actively work against his rival oyabun.",
    },
    {
        "name": "Blood of the Buffalo",
        "role": "Leader of the First Nations gang, a Salish-Shidhe physical adept who follows the Way of the Warrior",
        "archetype": "Physical Adept",
        "title": "Leader, First Nations",
        "race": "Elf",
        "gender": "Male",
        "nationality": "Salish-Shidhe",
        "organization": "First Nations",
        "connection": 2,
        "description": "A Grade 5 initiate physical adept who has rebuilt the First Nations into a fierce fighting force under Yakuza patronage, combining renewed pride in Amerindian heritage with a hard warrior focus.",
        "background": "Took over a nearly-dead street gang once Hanzo Shotozumi began feeding it nuyen, weapons and flattering talk of the members as 'noble and honorable warriors descended from a mighty people.' Under his leadership the gang has become a fierce fighting unit, its skill surpassing most smaller Seattle gangs.",
        "notes": "Gang Rating Superior. Leads the First Nations' ongoing war with the Choson Ring over Everett-dock smuggling, and will go after any group he feels has failed to show the gang proper respect.",
    },
    {
        "name": "Wind-Walker",
        "role": "First Nations lieutenant and shaman, twin sister to Wind-Rider, following the Coyote totem",
        "archetype": "Shaman",
        "title": "Lieutenant / shaman, First Nations",
        "race": "Human",
        "gender": "Female",
        "nationality": "Salish-Shidhe",
        "organization": "First Nations",
        "connection": 1,
        "description": "A Grade 3 initiate Salish-Shidhe shaman, one of the gang's two spiritual leaders and twin to Wind-Rider.",
        "notes": "No formal rating given beyond her Grade. Follows Coyote; alongside her twin, guides initiates through the gang's forty-eight-hour sweat-lodge-then-wilderness initiation ordeal that ends in a survival tattoo and a vision tattoo for those who pass.",
    },
    {
        "name": "Wind-Rider",
        "role": "First Nations lieutenant and shaman, twin sister to Wind-Walker, following the Raven totem",
        "archetype": "Shaman",
        "title": "Lieutenant / shaman, First Nations",
        "race": "Human",
        "gender": "Female",
        "nationality": "Salish-Shidhe",
        "organization": "First Nations",
        "connection": 1,
        "description": "A Grade 3 initiate Salish-Shidhe shaman, one of the gang's two spiritual leaders and twin to Wind-Walker.",
        "notes": "No formal rating given beyond her Grade. Follows Raven; alongside her twin, guides initiates through the gang's forty-eight-hour sweat-lodge-then-wilderness initiation ordeal that ends in a survival tattoo and a vision tattoo for those who pass.",
    },
    {
        "name": "Moon Hawk",
        "role": "First Nations lieutenant, the gang's one mundane member, recruited by Shotozumi after a shadowrun caught the Yakuza's eye",
        "archetype": "Street Samurai",
        "title": "Lieutenant, First Nations",
        "race": "Human",
        "gender": "Male",
        "nationality": "Sioux",
        "organization": "First Nations",
        "connection": 1,
        "description": "Relies on reputedly beta-grade wired reflexes and high-powered weaponry rather than magic; the gang's sole non-Salish-Shidhe, non-adept member.",
        "background": "A Sioux mundane who came to the Yakuza's attention as part of a hired shadowrun team; impressed enough that Shotozumi personally offered him membership in the First Nations and placed him as one of its lieutenants.",
        "notes": "No formal rating given. Gives the otherwise magic-heavy First Nations leadership a straightforward combat option when raw firepower, not adept tricks or shamanic ritual, is what a job calls for.",
    },
    {
        "name": "Zheng Li Kwan",
        "role": "Lodgemaster of the Yellow Lotus, Seattle's most powerful Triad, secretly commanding an enslaved vampire and angling to unite all three local Triads under himself",
        "archetype": "Triad Lodgemaster",
        "title": "Lodgemaster (Shan Chu), Yellow Lotus",
        "race": "Human",
        "gender": "Male",
        "nationality": "Chinese",
        "organization": "Yellow Lotus",
        "connection": 5,
        "description": (
            "A ruthless physical adept and high-grade Triad initiate (at least two grades above the "
            "highest player-character initiate), all skills Superior; a collector of ancient Chinese "
            "artwork, some of which finances his ambitions."
        ),
        "background": (
            "Left an already-subdued Hong Kong for Seattle's rawer opportunities, taking control of the "
            "Yellow Lotus six years ago and more than doubling it through aggressive recruitment of "
            "metahumans shut out of the Yakuza and Mafia. Controls the ancient Chinese vampire Su Cheng by "
            "holding the vase containing his Hidden Life, using him as a deniable 'secret weapon' against "
            "rivals."
        ),
        "notes": (
            "Gamemasters should make him an initiate at least two grades higher than the highest-grade "
            "player character initiate, with all skills Superior; may also have more exotic physical adept "
            "powers such as Delay Damage or Distance Strike at the gamemaster's discretion. Has offered the "
            "Eighty-Eights and the Octagon a standing alliance against the Yakuza, privately intending to "
            "absorb both into a single Triad under his own control once the Yakuza is beaten back. Uses Su "
            "Cheng as an untraceable assassin against his enemies and blackmails the vampire's cooperation "
            "by holding his soul jar; in the Soul Jar adventure framework, if Su Cheng recovers the jar "
            "with runner help, Zheng sends a circle of four Yellow Lotus magicians (aided by nature "
            "spirits) to recover it or destroy everyone involved, and holds a lasting grudge against "
            "whichever side the runners end up helping."
        ),
    },
    {
        "name": "Su Cheng",
        "role": "The Yellow Lotus's 'Incense Master,' actually an ancient Chinese vampire enslaved by Zheng Li Kwan's control of his soul jar",
        "archetype": "Vampire Magician",
        "title": "Incense Master, Yellow Lotus",
        "race": "Human (vampire)",
        "gender": "Male",
        "nationality": "Chinese",
        "organization": "Yellow Lotus",
        "connection": 3,
        "description": (
            "Dressed in flowing silk robes with a drooping Fu Manchu mustache, the image of a venerable "
            "sorcerer. Full classic vampiric abilities plus the free spirit power Hidden Life; a powerful "
            "magician in the Triad tradition, fond of illusion and manipulation spells to alter his "
            "appearance."
        ),
        "background": (
            "Bound to Zheng Li Kwan's will because Zheng possesses the ancient vase holding his life "
            "force; cannot be permanently killed while it remains intact, and regenerates from even severe "
            "injury. Has served for years as Zheng's secret weapon, responsible for many of the "
            "mysterious deaths of Zheng's enemies, and has grown to resent his servitude."
        ),
        "notes": (
            "Full classic vampiric abilities (SR1 p.234) plus the free spirit power Hidden Life; a "
            "powerful magician in the Triad tradition who knows many spells and frequently uses illusion "
            "and manipulation magic to change his appearance. So long as the vase holding his life force "
            "stays undamaged he cannot be permanently killed and regenerates from even the severest "
            "injury; his position lets him conduct magical research and feed with impunity, and 'at one "
            "time [he] might have willingly accepted his role as Zheng's ally,' but the Lodgemaster's "
            "blackmail has poisoned any real trust. Secretly hires runners at a small restaurant near Kobe "
            "Terrace Park to steal his own soul jar back from Zheng's warded Tacoma warehouse in the Soul "
            "Jar adventure framework, paying 4,000 nuyen each (or whatever sum the gamemaster judges "
            "reasonable) without explaining why he wants the vase or that he is a vampire; aids the runners "
            "against Zheng's ambush at the climax until he has the vase in hand, then 'cuts and runs.'"
        ),
    },
    {
        "name": "Rick Wu",
        "role": "Leader of the tech-forward, Westernized Eighty-Eights Triad, a self-styled businessman who distrusts magic",
        "archetype": "Triad Leader",
        "title": "Leader, Eighty-Eights",
        "race": "Human",
        "gender": "Male",
        "nationality": "Chinese-American",
        "organization": "Eighty-Eights",
        "connection": 4,
        "description": "Third-generation Chinese-American with the slick, macroflash bearing of a hip gangster-businessman; heavy beta-grade cyberware -- the gamemaster can give him just about anything -- and comfort with Matrix environments unmatched by any other Triad in Seattle.",
        "background": "Considers himself a businessman first and a Triad leader second; has little use for what he calls 'mystical nonsense' and has westernized the Eighty-Eights further than any other Seattle Triad, emphasizing technology and cash over ritual and tradition.",
        "notes": (
            "No formal rating given beyond the description above. Employs a few magicians for magical "
            "security and protection against rival syndicates' mages, but prefers Western-trained mages "
            "with 'a scientific bent' over Triad-trained ones, which he dismisses as 'mystical mumbo-"
            "jumbo.' Controls the gang the Tigers (see The Tigers (Eighty-Eights)) as his main street "
            "muscle -- the greatest advantage the Eighty-Eights hold over Seattle's other Triads -- and "
            "uses shadowrunners as unwitting cutouts in schemes like Dirty Laundry, disposing of loose "
            "ends afterward to keep his own hands clean."
        ),
    },
    {
        "name": "Tiger's Breath",
        "role": "Unseen leader of the Eighty-Eights' Tigers gang, rumored dead but unconfirmed",
        "archetype": "Physical Adept",
        "title": "Leader, The Tigers (Eighty-Eights)",
        "race": "Human",
        "gender": "Male",
        "organization": "The Tigers (Eighty-Eights)",
        "connection": 1,
        "description": "A Grade 7 initiate physical adept following the Way of the Warrior, known only by his gang name -- as with most Tiger leadership, no birth name is on record.",
        "notes": "No formal combat rating given beyond his initiate grade. Has not been seen in public for months; neither the Eighty-Eights nor the Tigers have confirmed or denied rumors of his death, leaving Dragon-eyes as the gang's visible mystical center and Tiger Claw positioned to formally succeed him if the rumor is confirmed.",
    },
    {
        "name": "Dragon-eyes",
        "role": "The Tigers' physical magician lieutenant and the gang's mystical center, with irises like a dragon's",
        "archetype": "Physical Magician",
        "title": "Lieutenant, The Tigers (Eighty-Eights)",
        "race": "Human",
        "gender": "Male",
        "organization": "The Tigers (Eighty-Eights)",
        "connection": 1,
        "description": "A Grade 7 initiate physical magician whose eyes are reputed to look like a dragon's -- irises without whites, the trait people say gave him his gang name.",
        "notes": "No formal combat rating given beyond his initiate grade. Serves as the mystical center around which the Tigers' death-cult beliefs revolve -- their conviction that ultimate Triad victory will let Triad magic revive the gang's dead -- and reinforces that faith on the Eighty-Eights' behalf.",
    },
    {
        "name": "Tiger Claw",
        "role": "The Tigers' leader-in-waiting, a female physical adept rumored to have killed five sleeping Yakuza members single-handed",
        "archetype": "Physical Adept",
        "title": "Lieutenant / leader-in-waiting, The Tigers (Eighty-Eights)",
        "race": "Human",
        "gender": "Female",
        "organization": "The Tigers (Eighty-Eights)",
        "connection": 1,
        "description": "A Grade 3 initiate physical adept following the Invisible Way, rumored among the Tigers to have single-handedly killed five Yakuza members while they slept in their homes.",
        "notes": "No formal combat rating given beyond her initiate grade. Positioned to take over gang leadership if Tiger's Breath is ever confirmed dead; already treated by the rank and file as the gang's leader-in-waiting.",
    },
    {
        "name": "David Gao",
        "role": "Nominal leader of the weak Octagon Triad, thoroughly controlled through spells and potions by his own Incense Master",
        "archetype": "Triad Puppet Leader",
        "title": "Leader, The Octagon (nominal)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Chinese",
        "organization": "The Octagon",
        "connection": 2,
        "description": "Publicly the Octagon's leader and the one who accepted Zheng Li Kwan's unification alliance out of eagerness for any hope of gaining ground against the Yakuza, but privately dominated in every important decision.",
        "background": "Controlled through spells and secret potions by the Octagon's own Incense Master, Chen Kwan-Ti, who used them to establish himself as the Triad's real power not long after arriving in Seattle two years ago.",
        "notes": "No formal rating given -- purely a puppet figure. Chen Kwan-Ti's control over Gao is the single biggest reason the Octagon has fallen so far behind Seattle's other Triads, though from the outside Gao still appears to be making his own decisions.",
    },
    {
        "name": "Chen Kwan-Ti",
        "role": "The Octagon's true power, a mainland Chinese wizard rumored to have studied under the great dragon Lung, with an unexplained private agenda in Seattle",
        "archetype": "Wizard",
        "title": "Incense Master (true power), The Octagon",
        "race": "Human",
        "gender": "Male",
        "nationality": "Chinese",
        "organization": "The Octagon",
        "connection": 3,
        "description": "Magical abilities at least Equal to the strongest player-character magician, focused on subtlety, control manipulations and illusion rather than open combat.",
        "background": "Arrived in Seattle from mainland China two years ago and quickly rose to dominate the Octagon through spells and secret potions used on David Gao; never explains why he left China.",
        "notes": "His actual goal in Seattle is never revealed -- possibly Su Cheng's soul jar, possibly some other magical prize connected to Dunkelzahn's will or a Seattle corporate breakthrough. Also the source of the Year-of-the-Tiger prophecy driving Yellow Lotus strategy.",
    },
    {
        "name": "Kyu",
        "role": "Leader of the Choson Ring, a Schism survivor consumed by hatred of the Yakuza and a personal wish to kill Hanzo Shotozumi with his own hands",
        "archetype": "Seoulpa Ring Leader",
        "title": "Leader, Choson Ring",
        "race": "Human",
        "gender": "Male",
        "nationality": "Korean",
        "organization": "Choson Ring",
        "connection": 4,
        "description": "Fiercely proud of his Korean heritage; bars Japanese and Amerinds from the Ring outright and distrusts elves enough that elven initiates have died 'accidentally' during initiation.",
        "background": "Survived the Schism as a young man and has never let go of the hatred it left him with -- both for the Japanese Yakuza who purged his people and, by extension, for the Amerind First Nations gang that now serves the Yakuza as muscle.",
        "notes": (
            "Gang Rating Superior. Not a fool -- pursues opportunities to hurt the Yakuza only when the "
            "risk to his Ring is acceptable, and knows his organization's limits even as he dreams of "
            "killing Hanzo Shotozumi with his bare hands. Runs the Choson Ring's dockside smuggling "
            "operations through his three loyal lieutenants (An Soo, Jung-mo, Danny Cho), each handling a "
            "different piece of the trade, and puts prospective members through rigorous torture-"
            "resistance tests before admitting them -- most surviving members proudly show the scars."
        ),
    },
    {
        "name": "An Soo",
        "role": "Choson Ring lieutenant handling records and computer systems",
        "archetype": "Technician",
        "title": "Lieutenant (records), Choson Ring",
        "race": "Human",
        "gender": "Male",
        "nationality": "Korean",
        "organization": "Choson Ring",
        "connection": 1,
        "description": "A tech-head loyal to Kyu, responsible for the Ring's records and computer systems.",
        "notes": "No individual rating given -- covered under the Ring's Superior Gang Rating. One of three lieutenants who each handle a different aspect of the Ring's smuggling trade; his records keep track of contraband, contacts and payoffs to the Metroplex Guard.",
    },
    {
        "name": "Jung-mo",
        "role": "Choson Ring lieutenant handling smuggling logistics, an ex-rigger who lost his panzer on a Denver run",
        "archetype": "Rigger",
        "title": "Lieutenant (logistics), Choson Ring",
        "race": "Human",
        "gender": "Male",
        "nationality": "Korean",
        "organization": "Choson Ring",
        "connection": 1,
        "description": "A former rigger who lost his vehicle on an ill-fated Denver run; now handles most of the Ring's pickup and delivery logistics on foot rather than behind the wheel.",
        "notes": "No individual rating given -- covered under the Ring's Superior Gang Rating. Loyal to Kyu like the Ring's other lieutenants; coordinates the timing and routes for the Ring's dockside contraband shipments.",
    },
    {
        "name": "Danny Cho",
        "role": "Choson Ring lieutenant and face-man, handling clients and arranging meets",
        "archetype": "Fixer",
        "title": "Lieutenant (face-man), Choson Ring",
        "race": "Human",
        "gender": "Male",
        "nationality": "Korean",
        "organization": "Choson Ring",
        "connection": 2,
        "description": "The Ring's public-facing lieutenant, who talks to clients and sets up meetings on Kyu's behalf.",
        "notes": "No individual rating given -- covered under the Ring's Superior Gang Rating. The most likely point of contact for shadowrunners approaching the Choson Ring for work, since Kyu himself rarely deals with outsiders directly.",
    },
    {
        "name": "Chulsoon Gray-Wolf",
        "role": "Leader of the Komun'go Ring, a Korean-Amerind half-breed who grew up hiding from the Schism that killed his father",
        "archetype": "Seoulpa Ring Leader",
        "title": "Leader, Komun'go Ring",
        "race": "Human",
        "gender": "Male",
        "nationality": "Korean-Amerind",
        "organization": "Komun'go Ring",
        "connection": 3,
        "description": "One of the youngest Seoulpa Ring leaders, just under thirty, carrying both a hatred of the Yakuza and fierce pride in his dual heritage.",
        "background": "His Yakuza father died in the Schism, leaving him and his Amerind mother to flee underground; for years the family identified themselves using his mother's surname to escape the purge. He grew up with a hatred of the Yakuza and fierce pride in his dual heritage, becoming involved with the Komun'go Ring as a teenager and rising to become one of the youngest Seoulpa Ring leaders in Seattle.",
        "notes": (
            "Gang Rating Equal (weaker than the other major Rings). Fosters a sense that 'the streets take "
            "care of their own' among Redmond Barrens residents who use the Ring's protection services. "
            "Takes lieutenant Black-Cloud-in-Morning's spiritual advice very seriously; suspects the Yakuza "
            "is quietly supplying weapons and information to the Ring's chief rival, the Rusted Stilettos, "
            "to keep the Komun'go off balance."
        ),
    },
    {
        "name": "Black-Cloud-in-Morning",
        "role": "Komun'go Ring lieutenant and Wolf shaman, seer and advisor whose counsel Chulsoon Gray-Wolf trusts completely",
        "archetype": "Shaman",
        "title": "Lieutenant / shaman advisor, Komun'go Ring",
        "race": "Human",
        "gender": "Male",
        "nationality": "Haida",
        "organization": "Komun'go Ring",
        "connection": 2,
        "description": "A full-blood Haida Wolf shaman who advises Chulsoon on the will of the spirits and the omens surrounding any decision the Ring faces.",
        "notes": (
            "No individual rating given. Conducts the Ring's initiation rites, blending Korean and Haida "
            "tribal tradition: the initiate is brought before 'the Spirits of the Land' in a patch of "
            "wilderness on the edge of NAN territory, put through trials that test heart and spirit, and "
            "finally subjected to a magical mind probe that lets Black-Cloud 'see into your heart' and "
            "judge whether the desire to join is sincere. Ring members believe he knows all their darkest "
            "secrets and their deepest fears, and accord him both fear and respect for it. Also trains two "
            "other shamans to assist him and regularly calls on nature spirits to help the Ring's "
            "operations, an edge that has helped the group survive and prosper."
        ),
    },
    {
        "name": "The Lord of the Inner Darkness",
        "role": "The Tartarus Ring's Bat-shaman leader, who never leaves his underground chambers and runs the Ring almost as a cult",
        "archetype": "Shaman",
        "title": "Leader, Tartarus Ring",
        "race": "Human",
        "gender": "Male",
        "organization": "Tartarus Ring",
        "connection": 3,
        "description": "A Bat shaman whose true name, if he has one, is unknown even to his own Ring; leads through fear and mystique from deep within the Ork Underground and never leaves his dark underground chambers.",
        "notes": (
            "Gang Rating Superior. Occasional rumors imply he has some hidden agenda or plan for the Ring "
            "he keeps entirely to himself, never elaborated on in the book -- under his current, "
            "unexplained leadership goals, the Tartarus Ring has simply prospered. New initiates are bound "
            "and forced to drink a strange herbal concoction he brews, then left overnight alone and "
            "helpless in a pitch-black abandoned stretch of the Underground to face whatever visions come; "
            "some initiates have died or gone mad from the ordeal, others drawn strength from it."
        ),
    },
    {
        "name": "Crawler",
        "role": "Tartarus Ring lieutenant who handles all of the Ring's surface-facing business, since The Lord never leaves the tunnels",
        "archetype": "Smuggler",
        "title": "Lieutenant (surface operations), Tartarus Ring",
        "race": "Ork",
        "gender": "Male",
        "organization": "Tartarus Ring",
        "connection": 1,
        "description": "A long-time Ork Underground resident said to know its tunnels and passages better than anyone alive.",
        "notes": "No individual rating given -- covered under the Ring's Superior Gang Rating. Handles anything the Ring needs done above ground, since The Lord of the Inner Darkness never leaves his chambers; the most likely lieutenant a runner or contact would actually meet face to face.",
    },
    {
        "name": "Greely",
        "role": "Tartarus Ring lieutenant and advisor to The Lord of the Inner Darkness, cadaverous enough that other members whisper he is a ghoul",
        "archetype": "Advisor",
        "title": "Lieutenant / advisor, Tartarus Ring",
        "race": "Human",
        "gender": "Male",
        "organization": "Tartarus Ring",
        "connection": 1,
        "description": "A cadaverous figure whose gaunt, corpse-like appearance has fueled a persistent, unconfirmed rumor that the Ring counts ghouls among its members.",
        "notes": "No individual rating given -- covered under the Ring's Superior Gang Rating. The Lord's closest advisor after Crawler; his appearance alone does much of the work of keeping outsiders and rival Ring members unsettled around him.",
    },
    {
        "name": "Colonel Ben O'Neil",
        "role": "Commander of the Seattle Metroplex Guard, who would impose martial law on the Mob war if Governor Schultz let him",
        "archetype": "Military Officer",
        "title": "Commander, Seattle Metroplex Guard",
        "race": "Human",
        "gender": "Male",
        "organization": "Seattle Metroplex Guard",
        "connection": 3,
        "description": "A career soldier who privately disagrees with Governor Schultz's policies but keeps his opinions to himself, believing the current situation in Seattle warrants martial law.",
        "notes": (
            "No stats given. Would impose order 'by any means necessary' if given the option, but "
            "'fortunately for the people of Seattle,' he would never do so in violation of orders or on "
            "his own initiative -- currently limited by Schultz's refusal to authorize the three-battalion "
            "Guard for anti-organized-crime action, restricting him instead to protecting essential "
            "government services from Mob-war fallout."
        ),
    },
    {
        "name": "Anthony Boniduchi",
        "role": "A Bigio caporegime shot for disloyalty, now recovering under DocWagon guard in Everett and ready to expose Bigio's ties to Chimera and O'Malley's murder",
        "archetype": "Mafia Soldier / Witness",
        "title": "Caporegime, Bigio Family (\"Toothless\")",
        "race": "Human",
        "gender": "Male",
        "organization": "Bigio Family",
        "connection": 1,
        "description": "A Bigio caporegime ready to \"spill all he knows\" about Maurice Bigio's involvement with Chimera and Don O'Malley's death.",
        "background": "Don Bigio already tried to have him killed for his disloyalty before he could talk; DocWagon managed to save his life and now keeps him under guard in one of their Everett clinics while he lies unconscious.",
        "notes": (
            "No stats given -- currently unconscious and unable to act. Bigio is trying to convince Don "
            "Ciarniello to help him finish the job before Boniduchi regains consciousness and squeals to "
            "the cops, while Rowena O'Malley wants to speak with him herself before the police get "
            "involved in what she considers a Family matter. Player characters could be the DocWagon team "
            "protecting him, Lone Star or UCAS FBI agents guarding a star witness, or Mafia agents (on "
            "either side) trying to reach him first -- the centerpiece of The Witness adventure idea."
        ),
    },
    {
        "name": "Gerald Kane",
        "role": "A Finnigan Family sottocapo whose daughter is nearly kidnapped by a Triad physical adept for leverage against him",
        "archetype": "Mafia Sottocapo",
        "title": "Sottocapo, Finnigan Family",
        "race": "Human",
        "gender": "Male",
        "organization": "Finnigan Family",
        "connection": 2,
        "description": "A Finnigan Family sottocapo whose daughter Angela enjoys Seattle's night life more than her bodyguards can always keep up with.",
        "notes": "No stats given; does not appear on-page beyond his relationship to Angela. Will be good for a future favor to any runners who rescue Angela from a Triad kidnapping attempt in the First Date adventure idea.",
    },
    {
        "name": "Angela Kane",
        "role": "Gerald Kane's daughter, nearly kidnapped by a Triad physical adept outside a Seattle nightclub for use as leverage against her father",
        "archetype": "Mafia Family Member",
        "title": "Daughter of Gerald Kane, Finnigan Family",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": "Fond of Seattle's night life -- an indulgence Hai Feng used to get close to her by posing as a suitor, before he 'knocks her unconscious' hauling her into a nearby alley.",
        "notes": "No stats given. Ditched her two bodyguards in a nightclub crowd before Hai Feng grabbed her; the guards appear at the end of the alley four combat turns later and help the runners fight him off if they see the rescue in progress.",
    },
    {
        "name": "Hai Feng",
        "role": "A Triad physical adept who tries to kidnap Angela Kane outside a nightclub for use as leverage against her Mafia father",
        "archetype": "Physical Adept",
        "title": "Physical adept (freelance / Triad-linked)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Chinese",
        "connection": 1,
        "description": "Poses as Angela Kane's suitor at the nightclub to get her alone, ditching her bodyguards in the crowd before knocking her unconscious in a nearby alley to carry her off.",
        "notes": "No stats given beyond his archetype. Prefers to escape with Angela as a hostage if possible; if that proves too difficult he throws her at one of the runners (preferably into their line of fire) and makes a break for it rather than fight it out.",
    },
    {
        "name": "Aldo Burke",
        "role": "Bigio Family sottocapo shot dead over dinner in a Mafia-owned restaurant by a Yakuza hitter disguised as a Ciarniello man",
        "archetype": "Mafia Sottocapo (deceased)",
        "title": "Sottocapo, Bigio Family (\"Al the Squid\")",
        "race": "Human",
        "gender": "Male",
        "organization": "Bigio Family",
        "connection": 1,
        "description": "Finishing his dinner at a Mafia-owned restaurant when a known Mafia soldier walks up, draws a gun and kills him and his guards, saying \"Ciarniello says buono appetito, chummer\" a moment before firing.",
        "notes": (
            "No stats given -- dies in the opening beat of the scene. The 'hitter' is actually a Yakuza "
            "operative disguised by a mask spell cast by a Yakuza mage waiting in a getaway van, meant to "
            "spark a Bigio reprisal against the Ciarniello Family while the Yakuza itself stays hidden. If "
            "runners capture or kill the hitter and reveal the truth, Don Bigio may offer them a job "
            "directly; otherwise they may get caught up in a Bigio reprisal against the confused Ciarniello "
            "Family before the misunderstanding can be resolved -- the Just Desserts adventure idea."
        ),
    },
    {
        "name": "Tony Miller",
        "role": "Mafia courier who stashes a sealed chip case with the runners rather than let pursuing Yakuza operatives recover it, then dies for it",
        "archetype": "Mafia Courier (deceased)",
        "title": "Courier, Finnigan Family",
        "race": "Human",
        "gender": "Male",
        "organization": "Finnigan Family",
        "connection": 1,
        "description": "A man in a dark suit who approaches runners in their favorite hangout offering 2,000 nuyen each to hold a sealed chip case overnight, promising to collect it -- and pay them -- at 8:00 the next morning.",
        "background": "Needs to get chip-borne information to Rowena O'Malley but is being tailed by Yakuza shadowrunners, and needs to stash the chips somewhere safe while he tries to convince his tail he doesn't have what they are looking for, hoping to double back and recover the chips once he has lost them.",
        "notes": (
            "No stats given -- dies off-page. The Yakuza runners catch him, work him over for information "
            "and kill him once they learn he passed the chips off to the player characters. When the "
            "runners return to their hangout at 8 a.m. they find a message from 'Mr. J' asking them to wait "
            "half an hour; if he never shows, they are to deliver the chip case to Rowena O'Malley's "
            "address themselves for 4,000 nuyen each -- twice what Miller promised -- with the Yakuza "
            "already picking up their scent from the same night spot. The Carriers adventure idea."
        ),
    },
    {
        "name": "Shelly Greenbriar",
        "role": "A Yakuza-run bunraku prostitute so altered and BTL-addled she genuinely believes she is Vice President Nadja Daviar, and means to assassinate the real one",
        "archetype": "Bunraku Prostitute",
        "title": "Bunraku prostitute (posing as Nadja Daviar)",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": "Surgically and neurologically altered to look and act exactly like Nadja Daviar -- the Yakuza's stock in trade for its bunraku houses -- and so far gone on personafix BTL that she has stopped pretending and genuinely believes she is the Vice President, hiring shadowrunners through a reputable fixer to help her 'prove her identity' against the 'impostor.'",
        "notes": "In truth plans to use her physical resemblance to get close enough to Daviar during the real VP's Seattle speaking engagement to kill her; runners who take the job must uncover the truth in time to stop an assassination that could tear apart the UCAS. The First Lady adventure idea.",
    },
]

ORG_UPDATES = {
    "Seattle Mafia": {
        "notes_append": (
            "Mob War (January 2058): capo James O'Malley assassinated January 1 by the Chimera operative "
            "Firebird, hired secretly by the Bigio and Ciarniello dons. The capo's seat is contested "
            "between O'Malley's daughter Rowena O'Malley (Finnigan Family) and the Bigio and Ciarniello "
            "families who arranged his death; Don Leo McCaskill of the Milwaukee-based McCaskill Family "
            "holds the Commissione's mandate to decide who ends up on top and will back whichever Seattle "
            "family looks most likely to restore order fastest. See the Finnigan Family, Bigio Family and "
            "Ciarniello Family org rows for the three Seattle families in detail."
        ),
        "leadership_add": [
            {"name": "James O'Malley", "title": "Former capo of Seattle (deceased, assassinated 1 January 2058)", "notes": "Head of the Finnigan Family; his murder starts the Mob war."},
        ],
        "enemies_add": ["Chimera", "Shotozumi-gumi"],
    },
    "Yakuza (Watada-rengo)": {
        "notes_append": (
            "-- Mob War --\n"
            "Mob War (January 2058): the Japan-based Watada-rengo, led by oyabun Akira Watada, oversees "
            "Seattle's three Yakuza gumis -- the dominant Shotozumi-gumi (oyabun Hanzo Shotozumi, who "
            "wants his own independent West Coast rengo), the older, rival Nishidon-gumi (oyabun Isao "
            "Nishidon) and the smaller, more progressive Shigeda-gumi (oyabun Takeo Shigeda; database row "
            "'Shigeda-gumi (Takeo Shigeda)' -- an unrelated, same-named Mercurial org already occupies the "
            "plain 'Shigeda-gumi' name, see that row's notes). In 2043 Watada purged nearly all of the "
            "Seattle Yakuza's Korean leadership in a week of killings known as 'the Schism' after the "
            "Koreans refused an ultimatum to swear renewed loyalty; the survivors went underground and "
            "became the Seoulpa Rings, who hold a lasting grudge. With the Mafia's capo dead, Seattle's "
            "Yakuza moves aggressively into Mafia gambling and vice turf while fighting the Triads and the "
            "Seoulpa Rings on other fronts. Unconfirmed Shadowland rumor (the Dragonslayer thread) claims "
            "the great dragon Ryumyo has secretly controlled the entire Watada-rengo since the 1920s, "
            "along with significant hidden influence over Mitsuhama Computer Technologies and lesser "
            "influence over Renraku, Shiawase, Yamatetsu and Fuchi Industrial Electronics -- the book's own "
            "in-thread skeptics dispute all of it. DISCREPANCY: this book's Hanzo Shotozumi is oyabun of "
            "his own Shotozumi-gumi, one of three clans under the Watada-rengo; the campaign's existing "
            "Hanzo Shotozumi character row instead makes him oyabun of the whole 'Dungeness Crab Clan' per "
            "Elven Fire (which itself never names the Watada-rengo -- see that discrepancy note above). "
            "Treat the Shotozumi-gumi as the Dungeness Crab Clan's Seattle inner circle, or reconcile "
            "however suits the table."
        ),
        "leadership_add": [
            {"name": "Akira Watada", "title": "Oyabun, Watada-rengo (Chiba, Japan)", "notes": "Ordered the 2043 Schism; receives Miko Ishikawa's secret reports on Shotozumi-gumi loyalty."},
        ],
        "enemies_add": ["Seattle Mafia", "Yellow Lotus", "Choson Ring", "Komun'go Ring"],
    },
    "Seoulpa Rings": {
        "notes_append": (
            "Mob War (January 2058): born from 'the Schism,' the 2043 purge of Korean Yakuza leadership "
            "from the Watada-rengo's Seattle gumis, the Rings survive as small, secretive, autonomous "
            "cells rather than a unified hierarchy, sharing only a common thirst for revenge against the "
            "Yakuza that cast their founders out. With O'Malley dead and the Yakuza fighting on multiple "
            "fronts, three major Seattle Rings move against Yakuza interests: the dockside Choson Ring, "
            "the Redmond-Barrens Komun'go Ring and the Ork Underground's Tartarus Ring (see their "
            "individual org rows). Most Rings work independently and sometimes at cross purposes, without "
            "a unified command."
        ),
        "enemies_add": ["Shotozumi-gumi"],
    },
    "Lone Star Security": {
        "notes_append": (
            "Mob War (January 2058): Seattle chief William Louden has upped patrols and cracked down hard "
            "on the syndicates as the Mob war escalates, only to see the Mafia, the Yakuza and the Triads "
            "all show willingness to target Lone Star officers directly. Louden is quietly considering "
            "covertly hiring shadowrunners for jobs his own officers cannot legally do, and is using the "
            "crisis as leverage in the corporation's ongoing metroplex security contract renegotiation -- "
            "leverage undercut by rival Knight Errant Seattle's public-relations campaign to look like the "
            "more 'personal' alternative."
        ),
        "enemies_add": ["Knight Errant Security Services"],
    },
    "Knight Errant Security Services": {
        "notes_append": (
            "Mob War (January 2058): Ares Macrotechnology's Seattle subsidiary offers discounted "
            "'supplemental' security to private clients and runs a public-relations campaign painting "
            "itself as personal and high-tech against Lone Star's 'impersonal' image, hoping the Mob war "
            "gives it the opening it needs to finally win the metroplex's own security contract. May "
            "arrange shadowruns of its own to damage Lone Star's standing with the Seattle government."
        ),
        "enemies_add": ["Lone Star Security"],
    },
    "Seattle Metroplex Guard": {
        "notes_append": (
            "Mob War (January 2058): commanded by Colonel Ben O'Neil, who would favor martial law against "
            "the syndicates but stays out of anti-organized-crime action on Governor Schultz's orders, "
            "restricted instead to protecting essential government services from Mob-war fallout. The "
            "Choson Ring keeps a standing payoff arrangement with Guard personnel to look away from its "
            "dockside smuggling."
        ),
    },
    "Rusted Stilettos": {
        "notes_append": (
            "Mob War (January 2058): the Komun'go Seoulpa Ring's greatest non-Yakuza enemy in Redmond, "
            "repeatedly trying to muscle in on the Ring's protection rackets. Komun'go leader Chulsoon "
            "Gray-Wolf suspects the Yakuza is quietly arming and informing the Stilettos to keep the "
            "Ring off balance."
        ),
        "enemies_add": ["Komun'go Ring"],
    },
    "The Cutters": {
        "notes_append": (
            "Mob War (January 2058): the Choson Ring has absorbed most of the dockside smuggling business "
            "The Cutters lost after the gang 'nearly succumbed to disaster' a few years back -- the book "
            "gives no further detail on what that disaster was."
        ),
    },
    "Ancients": {
        "notes_append": "Mob War (January 2058): long-time street rivals of the Eighty-Eights' Tigers gang (The Tigers (Eighty-Eights) row -- not the unrelated Elven Fire yakuza gang of the same short name).",
        "enemies_add": ["The Tigers (Eighty-Eights)"],
    },
    "Mitsuhama Computer Technologies": {
        "notes_append": (
            "Mob War (January 2058): named by multiple Yakuza-track sources as the Japanacorp with the "
            "closest ties to the Seattle Yakuza. Unconfirmed Shadowland rumor (the Dragonslayer thread) "
            "goes further, claiming the great dragon Ryumyo secretly controls the corporation through "
            "those Yakuza ties -- disputed by the thread's own skeptics."
        ),
    },
    "Renraku Computer Systems": {
        "notes_append": (
            "Mob War (January 2058): the Choson Ring has had a run-in with Renraku security over dockside "
            "smuggling operations that strayed too close to the areas the Renraku Arcology watches. "
            "Separately, unconfirmed Shadowland rumor claims the dragon Ryumyo holds hidden influence over "
            "the corporation through the Yakuza, alongside similar claims about Shiawase, Yamatetsu and "
            "Fuchi Industrial Electronics."
        ),
    },
    "Red Dragon Association": {
        "notes_append": (
            "Mob War (January 2058, Dragon Crimelord appendix): a Shadowland leaker calling himself "
            "Dragonslayer claims this is the Hung Lung Mun -- 'Red Dragon Association' being a literal "
            "translation of the name -- the most powerful Triad in Hong Kong and along the Pacific Rim, "
            "secretly controlled by the great dragon Lung since at least 2019. The claim is presented "
            "as unconfirmed underworld rumor and disputed by other posters in the same thread; the book "
            "gives no on-the-ground Seattle detail connecting this association to the Yellow Lotus, "
            "Eighty-Eights or Octagon beyond the shared claim of dragon patronage."
        ),
    },
}

LOC_UPDATES = {
    "Renraku Arcology (SCIRE)": {
        "notes_append": (
            "Mob War (January 2058): the Choson Seoulpa Ring has had at least one run-in with Renraku "
            "security after a dockside smuggling operation strayed too close to the areas the Arcology "
            "keeps under watch."
        ),
    },
}

NPC_UPDATES = {
    "Governor Schultz": {
        "notes_append": (
            "Mob War (January 2058): five-term Seattle governor of nineteen years, first elected after "
            "the 2039 assassination of predecessor Governor Allenson following the Night of Rage (Schultz "
            "was then mayor of Bellevue). Increasingly seen as too weak to stop the syndicates fighting in "
            "the streets and under public attack from political critic Karl (called 'Kenneth' in this "
            "book) Brackhaven; refuses to mobilize the Metroplex Guard against the Mob war for fear of "
            "sparking another Night of Rage."
        ),
    },
    "Karl Brackhaven": {
        "notes_append": (
            "Mob War (January 2058): publicly attacks Governor Schultz as 'soft on crime' over her failure "
            "to stop the Mob war, and is widely expected to run for governor himself in the 2060 election. "
            "This book calls him 'Kenneth Brackhaven' throughout -- likely the same recurring Humanis "
            "figure introduced in Peacekeeper as 'Karl Brackhaven' under a book-to-book naming "
            "inconsistency, not a separate person."
        ),
    },
    "William Louden": {
        "description_append": (
            "Mob War (January 2058): a competent administrator, better at running an organization than "
            "commanding a small war, who has carefully covered himself against blame for a crisis for "
            "years -- until now."
        ),
        "background_append": (
            "Mob War: has upped Lone Star's forces and cracked down hard on the syndicates as the Mob war "
            "escalates, but the crackdown has only aggravated the situation -- the Mafia, the Yakuza and "
            "the Triads have all shown willingness to target Lone Star officers directly. Convinced that "
            "continued trouble will cost him his job to Lone Star Central in Texas, and quietly looking "
            "into covertly hiring freelance shadowrunners for not-entirely-legal work to curb the "
            "syndicates' worst excesses."
        ),
        "notes_append": "Mob War: a good hook for a law-enforcement-adjacent Mob War campaign, distinct from his brief press-conference cameo in Predator and Prey.",
    },
    "Nadja Daviar": {
        "description_append": (
            "Mob War (January 2058, First Lady adventure idea): glimpsed by Albert and James Cavalieri on "
            "a New Year's trideo broadcast giving a speech before a corporate consortium in DeeCee, her "
            "poise and beauty as ethereal and unearthly as ever -- 'of course, they would be unearthly; "
            "Daviar wasn't human.'"
        ),
        "notes_append": (
            "Mob War: never actually appears on-page. Comes to Seattle for a speaking engagement a few "
            "days after the runners are approached by a fixer with a job from a woman claiming to be "
            "Daviar herself, kidnapped and replaced by an impostor -- in truth a Yakuza bunraku prostitute, "
            "Shelly Greenbriar, so overdosed on personafix BTL that she genuinely believes she is the Vice "
            "President and means to use her resemblance to assassinate the real Daviar at the speaking "
            "engagement. The real threat comes entirely from Greenbriar, not from any conspiracy actually "
            "touching Daviar herself."
        ),
    },
    "Hanzo Shotozumi": {
        "description_append": (
            "Mob War (January 2058): \"the term 'inscrutable' might have been coined for Hanzo Shotozumi\" "
            "-- a face that might as well be carved from stone, always polite and proper no matter the "
            "circumstances, showing his most intense rage only by raising his voice slightly, a mannerism "
            "that strikes terror into anyone who knows him. Handles even the most unpleasant business as "
            "routine, able to \"order a kobun to commit suicide as if he was ordering lunch.\" Minimal "
            "cyberware (smartlink, datajack, headware memory, beta-grade cybereyes); combat skills Equal "
            "to the player characters, Negotiation, Interrogation and Leadership Superior."
        ),
        "background_append": (
            "Mob War: made oyabun of his own Shotozumi-gumi in 2043 to clean up after the Schism, and has "
            "spent fifteen years building it into the most powerful of Seattle's Yakuza clans -- now "
            "pushing to unite the Nishidon-gumi and the Shigeda-gumi under him and break away from the "
            "Watada-rengo into his own independent West Coast rengo, with the Mafia's capo newly dead and "
            "the timing finally right. Married, with two sons (the elder training as his second-in-"
            "command, the younger a kobun) and a runaway daughter, Keiko, who works Seattle's shadows as "
            "the decker Kiku and secretly undermines his operations. Has cultivated the Amerind gang First "
            "Nations as deniable muscle in a longer-term bid for influence with the Native American "
            "Nations."
        ),
        "notes_append": (
            "Mob War: DISCREPANCY -- this book makes him oyabun specifically of the Shotozumi-gumi, one of "
            "three Seattle clans under the Watada-rengo (see that org's notes), rather than of the whole "
            "'Dungeness Crab Clan' this row's organization link (from Elven Fire) makes him head of; "
            "organization link left as-is per the no-relink rule. Unconfirmed underworld rumor (Dragonslayer's "
            "Shadowland thread) holds that the great dragon Ryumyo is the true power behind the entire "
            "Watada-rengo, and by extension behind Shotozumi's own ambitions -- disputed by the thread's "
            "own posters."
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
Three Matrix systems are described with enough detail to build; several more (Miko Ishikawa's home
system, the Seoulpa Rings' vanishing SAN) are mentioned only in passing.

**1. BrightSky Finances** (Dirty Laundry framework, Fort Lewis). A small, clean corp's system whose
forged Eighty-Eights access codes trigger a trapdoor into a Shigeda-gumi host.

| Node | Function | Rating / IC |
|---|---|---|
| Host | BrightSky's own system | Light corporate ice; first layer only, per the forged codes |
| Trapdoor | Hidden link triggered by the forged codes | Leads directly to the Shigeda-gumi host below |

**2. Shigeda-gumi host** (reached via the BrightSky trapdoor). Japanese-modern motif. Host rating string
Red-10/16/18/14/16/14; runs Trace and Probe IC escalating to Killer, Blaster and Black IC (the book
suggests using the sample Yakuza host, p.152, VR 2.0). Three successful File operations complete the
requested data changes once past any of the host's ice.

**3. Miko Ishikawa's home computer** (A Matter of Honor framework, her downtown Seattle high-rise
apartment). Blue-G/10/8/8 -- state-of-the-art but with very little IC; holds the files she wants stolen
and the false trail she wants sent to a vanishing SAN address.

**4. The vanishing SAN** (The Great Yak Caper framework, Seoulpa Rings track). A remote server that only
connects to the Matrix at intermittent, encrypted-message-announced times; holds the cryptographic key
the Rings need to build a Yakuza-fund-siphoning virus. No host stats given -- build to the scene.
"""

NOT_BUILT = """
- **Ryumyo** and **Lung** -- the great dragons a Shadowland leaker (\"Dragonslayer\") claims secretly run
  the Yakuza (via the Watada-rengo) and the Triads (via the Hung Lung Mun / Red Dragon Association)
  respectively, as parallel moves in a mana-hoarding scheme centered on the Pacific Rim's Ring of Fire
  and a legendary Inner Earth. The book itself frames this entirely as unconfirmed BBS rumor, argued
  down point-for-point by other in-thread posters (Skeptic, Reality Czech, Magister and others); no
  dragon NPC rows are built. Rumor threads: Akira Watada's 2027 Mount Fuji encounter with a mysterious
  green-eyed stranger; the terrorist group ALOHA and a failed Hawaiian coup Ryumyo allegedly funded;
  Denver Red Dragon Triad Lodgemaster **Choi-mu**, rumored to be an eastern dragon in human form.
- **Don Ian Finnigan** and his murdered sons **James and Michael Finnigan** (Finnigan Family founder and
  his generation, all killed by Yakuza reprisals decades before the adventure); **Don Gianelli** (Tony
  Gianelli's late mentor and predecessor as Bigio consiglieri); **Gerard Vigillia** (Ciarniello
  caporegime killed for skimming Casino Corner, the original spark for Ciarniello's fear of O'Malley);
  **Don Conor O'Rilley** of Boston (protected Rowena during her years at Harvard) -- backstory on the
  Finnigan Family and Ciarniello Family rows.
- **Aldo "Al the Squid" Burke** (Bigio sottocapo shot by a Yakuza hitter disguised via mask spell, framed
  to look like Ciarniello's doing) and **Tony Miller** (Mafia courier killed by Yakuza runners after
  stashing chips meant for Rowena O'Malley) -- one-scene casualties from the Mafia and Yakuza adventure
  ideas, name-drops only.
- **Nadja Daviar**, real UCAS Vice President, and **Shelly Greenbriar**, a bunraku prostitute who
  overdosed on personafix BTL until she genuinely believes she is Daviar and means to assassinate her --
  the First Lady adventure idea; not built as it centers on a canon government figure rather than the
  Seattle underworld.
- **The Heaven and Earth Circle** (the mystic order Zheng Li Kwan's shapeshifting magician-agents belong
  to) and the **Changgo Ring** (a Seoulpa Ring "broken up by Fuchi Corporation, since re-formed," used as
  Miko Ishikawa's cover story) -- named but undeveloped organizations from the Ringers and A Matter of
  Honor adventure ideas.
- **The Sisterhood of Ariadne**, a Seattle magical order that received Dunkelzahn-will dragon-talon
  clippings and plans to sell some to a Tir Tairngire contact -- The Dragon's Claws adventure idea.
- Unnamed set-piece locations folded into org/NPC notes rather than built as rows: the O'Malley family
  compound (Finnigan Family headquarters), Bigio's Tacoma mansion (Bigio Family headquarters, Blood
  Money climax), Zheng Li Kwan's decoy-vase residence in Bellevue and the warded Tacoma warehouse
  holding the real soul jar (Soul Jar framework), Hanzo Shotozumi's Seattle home (Neon Flower framework),
  Miko Ishikawa's downtown high-rise apartment, St. Mary's Parish in Bellevue (Mary Finnigan's church).
"""

PLAY_NOTES = """
- This is a sourcebook, not a linear adventure: run one track as the spine and use the other three as
  background texture ("One-Track Mind," p.16), let the party jump between tracks as opportunities arise
  ("Jumping the Tracks"), run it fully free-form off the Timeline, or structure it like a novel with a
  clear beginning, middle and end. Characters can belong to any syndicate, freelance for the highest
  bidder, work Lone Star's or Knight Errant's side, or simply get pulled in through a contact, a debt or
  a bodyguard job (see Hooking the Characters, p.9, for the book's full menu of entry points).
- The war has no built-in ending. Don McCaskill's decision on Seattle's next capo, Shotozumi's bid for
  an independent rengo, Zheng Li Kwan's Triad-unification scheme and the Seoulpa Rings' revenge campaign
  are all left open for the gamemaster to resolve however suits the campaign -- or to keep running
  indefinitely as background conflict.
- Track One (Mafia) frameworks: Tracking the Assassin, Shotgun Wedding, Blood Money. Track Two (Yakuza):
  Dirty Laundry, A Matter of Honor, Neon Flower. Track Three (Triads): Soul Jar. Track Four (Seoulpa
  Rings): The Great Yak Caper. Each track's "Adventure Ideas" section (captured in org/NPC notes and
  NOT_BUILT above) supplies several shorter hooks the gamemaster can run standalone or use to bridge
  between frameworks.
- Most major NPCs are statted only in relative terms (Inferior/Equal/Superior/Superhuman/Ultimate against
  the player characters, per Shadowrun Companion: Beyond the Shadows pp.84-85) rather than full stat
  blocks -- deliberately, so the gamemaster can scale every syndicate figure to the power level of their
  own table. Scale up or down freely; the book explicitly expects it.
- Triad loyalty oaths are real magic in this book, not just underworld enforcement (p.50): a broken oath
  triggers an automatic, GM-authored punishment regardless of normal Shadowrun conventions about ritual
  sorcery requiring a link. Use sparingly and dramatically if any player character is initiated into a
  Triad.
- The Dragon Crimelord appendix is written entirely as a skeptical Shadowland BBS thread, complete with
  other posters picking the leaker's claims apart line by line -- treat Ryumyo and Lung's involvement as
  a rumor players can chase, dismiss or never resolve, not a confirmed campaign fact.
"""
