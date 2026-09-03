# Super Tuesday! (FASA 7322, 1994) -- campaign order #26 (the book's position in
# frontend/shared.js ADVENTURE_ORDER: ..., "Missing Blood", "Super Tuesday!", "Shadows of the
# Underworld", ... -- ORDER follows the established index+1 convention used by every other spec).
#
# This is an anthology, not a single adventure: five independent shadowruns (Political Poison,
# Strange Attraction, Casualties of War, Ghost Story, Dry Run), each tied to one candidate in the
# UCAS presidential election of 2057, plus a general framing prologue ("Strange Bedfellows") and
# six candidate biography write-ups. All five scenarios are covered below. Casualties of War is
# set in Chicago (Bug City), not Seattle -- its rows carry city="Chicago"; everything else is
# Seattle unless noted.
#
# The book's own inconsistencies:
# - Dry Run ties Dunkelzahn's VR operation to his Lake Louise resort (Athabaskan Council) in the
#   introduction, then places the actual drugged-runner facility "near Mason City, Iowa" with
#   escape routes to Minneapolis or Des Moines in the scene text itself. The concrete scene detail
#   (Iowa) is used as the operative location; the Lake Louise framing is kept only for Dunkelzahn's
#   public VisionQuest/resort operations.
# - Political Poison's climax is staged at "the Superdome" for a Vogel rally in the Seattle
#   metroplex, but earlier canon (see total_eclipse.py) already establishes Seattle's domed
#   stadium as the Kingdome (closed for repairs in late 2051, reopened ~May 2052). Nothing in this
#   book explains a second dome or a renaming, so this is treated as the same venue and appended to
#   The Kingdome's row as a flagged discrepancy rather than creating a competing location.
# - Strange Attraction's Karma table lists "Holding on to the key for the whole adventure" and
#   "Keeping Bono alive" as bonus categories but the actual point values are missing from the scan;
#   1 point each is used, consistent with every other bonus category in the book.
# - Several stat blocks are visibly OCR-garbled (the Volk Soldiers' attribute columns, Silverblade's
#   Interrogation rating, part of Jack Neelson's Etiquette (Military) rating and his gear list, which
#   the scan cuts off entirely at the end of the book). Garbled fields are omitted rather than
#   guessed; noted inline on the affected NPCs.
# Cross-database name collisions found while ingesting (verified live, since they postdate the name
# dump this spec was written against): (1) "Karl Brackhaven" already exists as an NPC from Peacekeeper
# (Central Seattle chapter president of Humanis Policlub, ex-Aztechnology exec) -- this book's Karl is
# the same figure and the same office (it just calls it "Seattle chapter president"); handled as
# NPC_UPDATES rather than a duplicate row. (2) "The Partyzone" already exists as a location from Dark
# Angel, headquartered in South Tacoma there; this book places it "in an area of the Redmond Barrens"
# instead -- treated as the same recurring floating rave/neutral ground under a location discrepancy
# note rather than a second Partyzone.
# Source text: docs/Adventures/text/Shadowrun 2e - Adventure - Super Tuesday {FASA7322}.txt (113 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "Super Tuesday!"
ORDER = 26
SOURCE = "Shadowrun 2e - Adventure - Super Tuesday {FASA7322}.pdf, pp. 3-113"
YEAR = "2057"

SYNOPSIS = """
**Super Tuesday!** is an anthology of five unrelated shadowruns, framed by the whirlwind eight-month
race for the UCAS presidency in 2057 -- a snap election called after the "dullest election of the
century" (2056) turned out to be rigged, impeaching President **Thomas Steele** and VP **James
Booth** and installing interim President **Barry Jo Pritchard**. Six candidates run: dwarf eco-lawyer
**Arthur Vogel** (Democratic "One World"), mage academic **Dr. Rozilyn Hernandez** (New Century
Party), disgraced ex-VP **James Booth** (Technocratic), retired general **Franklin Yeats**
(Republican), Seattle magnate **Kenneth Brackhaven** (Archconservative, secretly Humanis-backed),
and the great dragon **Dunkelzahn** (Independent). A framing prologue, "Strange Bedfellows," has no
candidate of its own: runners **Raze**, **Riff**, and **Spook** steal data from Brackhaven's Seattle
campaign HQ and cross paths with an unnamed arsonist mage sent to burn the place down -- "Politics
makes strange bedfellows," Raze mutters, backing out with his gun on her.

**Political Poison** (Vogel) sends the runners chasing a leaking canister of banned insecticide
through Seattle after a friend, the runner **Silver**, is poisoned stealing it for a mysterious
buyer. That buyer is **Alan Riv**, an elf TerraFirst! saboteur horribly burned in a job Vogel
secretly orchestrated years ago, now a deranged Toxic Dog shaman living in the ruins of the plant
he tried to destroy. Riv means to gas thousands of people at a Vogel campaign rally in revenge.

**Strange Attraction** (Hernandez) opens with the runners waking up amnesiac on the Salish-Shidhe
side of the Tir Tairngire border, carrying an indestructible orichalcum key they cannot remember
acquiring. The key is a legendary Tir talisman, stolen (unknowingly, while drugged with the memory-
wiping drug laes) on a smuggling job for the **Illuminates of the New Dawn**, the hermetic order
backing Hernandez. Tir special agents called the **Ghosts**, led by the adept-mage **Speren
Silverblade**, and an Aztechnology assassin named **Belladonna** both want it before word gets out.

**Casualties of War** (Booth and Yeats) drops the runners inside the Chicago Containment Zone --
Bug City -- hired by a reporter, **Mara Suhar**, to rescue the brother of VP candidate **Anne
Penchyk** (Yeats's running mate). Suhar is really a mantis spirit of the **Desolation Angels**, and
Penchyk has secretly been turned by the cabal's leader, **Vixen**; the "rescue" is cover for
smuggling insect spirits out of the CZ. The ghoul community of **Ghoultown**, led by **Tamir Grey**,
becomes an unlikely ally against the anti-metahuman militia known as **the Volk**.

**Ghost Story** (Brackhaven) is a murder mystery: the ghost of a twelve-year-old ork boy -- "I'm not
a monster! I'm just Kenny" -- haunts a hospitalized runner, and the trail through street doc **Dr.
Christina Falt** and a frightened nurse, **Karen Johanssen**, reveals that the "real" Kenneth
Brackhaven was murdered by his own father in 2023 and replaced with a conditioned SINless double.
Brackhaven's uncle **Karl Brackhaven**, Seattle's Humanis Policlub chapter president, sends the
hitman **Fletcher Quinn** to silence anyone who learns the truth.

**Dry Run** (Dunkelzahn) hires the runners for what they believe is a real DeeCee shadowrun for the
dragon's head of security, **Carla Brooks** -- planting a bug on a rival candidate's limousine. It
is in fact an unwitting VR test run at a secret VisionQuest facility; the runners "wake" from the
simulation to find the facility under real siege by **Human Nation**, a militant anti-metahuman
splinter of Humanis Policlub trying to force Dunkelzahn out of the race.
"""

TIMELINE = """
- **2011** -- Kenneth Brackhaven born in Seattle; his mother dies of complications.
- **2012, January 27** -- Dunkelzahn first appears near Denver.
- **2022** -- Dunkelzahn's second "voice," John Timmons, is assassinated by an anti-metahuman
  gunman whom the dragon instantly vaporizes in front of witnesses.
- **2023** -- Goblinization Day floods Seattle General Hospital. Ork Kenny Brackhaven is murdered by
  his father Charles and replaced with a conditioned SINless double (Ghost Story).
- **2037** -- Dunkelzahn buys VisionQuest from Ares Macrotechnology through his advisor Damien Knight.
- **2043** -- Edward Crull-style corporate favor economics aside, the Desolation Angels' failed
  recruitment of Mitchell Truman and years of Dr. Freeman's cover-up work predate the campaign.
- **2044** -- Charles Brackhaven dies; the impostor "Kenneth" inherits Brackhaven Investments.
- **Late 2052** -- President Adams dies suddenly; VP Thomas Steele ascends, names James Booth VP.
- **2054** -- General Franklin Yeats retires from the UCAS Army over budget-cut disputes.
- **2056** -- Steele/Booth "win" the presidential election.
- **Early 2057** -- The 2056 election is exposed as rigged; Steele and Booth are impeached; Barry Jo
  Pritchard becomes interim president; an emergency ~8-month campaign season is called.
- **February 2057** -- Shadowland chatter and campaign announcements for Vogel, Hernandez, Booth,
  Yeats, and Brackhaven circulate; "Strange Bedfellows" burns Brackhaven's Seattle HQ.
- **March 15, 2057** -- Dunkelzahn announces his candidacy live on "Wyrm Talk," interviewed by
  Holly Brighton.
- **During the campaign (undated relative to each other)** -- Political Poison, Strange Attraction,
  Casualties of War, Ghost Story, and Dry Run all take place; the book gives no fixed order or dates
  among them beyond "sometime in the 2057 campaign."
- **Planned for "early August" 2057** -- Election day (outside the scope of this book).
"""

ORGS = [
    {
        "name": "Illuminates of the New Dawn",
        "org_type": "mystical fellowship",
        "tier": 4,
        "headquarters": "Federal District of Columbia (DeeCee)",
        "summary": "Secretive hermetic order backing Rozilyn Hernandez; believes magic and science together herald a new human era",
        "description": (
            "A hermetic magical order, headquartered in DeeCee, that reads the Awakening as the dawn "
            "of a new stage in human development in which science and magic must be reconciled. Most "
            "of its members are also active in the New Century Party, which has fed persistent -- "
            "unproven -- Shadowland chatter comparing the order to a resurrected Universal Brotherhood: "
            "'Don't forget about her magical chummers, either. The Illuminates of the New Dawn are a "
            "for-real hermetic magical order and they can sling some powerful mojo.' The order's "
            "initiate-mages are willing to steal, kill, and blacklist to protect its interests and "
            "Hernandez's candidacy."
        ),
        "leadership": [
            {"name": "Nicholas Grace", "title": "Initiate mage, campaign agent", "notes": "Fanatically devoted to Hernandez; ran the Portland smuggling job through the fixer Bono."},
            {"name": "Dr. Rozilyn Hernandez", "title": "High-grade initiate; presidential candidate", "notes": "The order's public face."},
        ],
        "notes": (
            "Strange Attraction: hired the runners (through the fixer Beaumont 'Bono' Noble, posing "
            "as order members with diplomatic passes) to smuggle an ancient orichalcum key out of "
            "Tir Tairngire from a Portland contact, Birch Kirby -- unaware the key was a Tir state "
            "talisman until Tir special agents came hunting it. When the runners' memories were wiped "
            "by the Tir border patrol's laes drug and the handoff fell through, the order blacklisted "
            "them regardless of outcome: expect harassment, and worse if Hernandez wins the "
            "presidency. Nobody outside the order seems to know why the key mattered so much."
        ),
    },
    {
        "name": "New Century Party",
        "org_type": "political party",
        "tier": 3,
        "headquarters": "Federal District of Columbia (DeeCee)",
        "summary": "Rozilyn Hernandez's 'science and magic together' party, formed from disaffected Technocrats and hermetic progressives",
        "description": (
            "A new party built around Dr. Rozilyn Hernandez's belief that technological and magical "
            "development, pursued together, can lift the UCAS into a golden age -- pro-research, "
            "pro-education, ruthlessly pro-progress, and willing to spend individual freedoms to get "
            "there: 'Our technology isn't doing enough. Magic isn't doing enough. Neither of them has "
            "lived up to what they could be. We need to take back the reins of power and guide the "
            "world into a new era.' Formed from Technocrats who jumped ship after the 2056 rigged-"
            "election scandal plus academic hermetics close to the Illuminates of the New Dawn, whose "
            "members overlap heavily with the party's staff -- prompting street nicknames like 'the "
            "granola party.'"
        ),
        "leadership": [
            {"name": "Dr. Rozilyn Hernandez", "title": "Presidential candidate", "notes": "Georgetown University social scientist and mage; Illuminates of the New Dawn initiate."},
            {"name": "Ramsay McMulkin", "title": "Vice-presidential candidate", "notes": "Former Technocrat film star; campaigns via simsense recordings of his own point of view, generating sympathy (and funding both the party and, allegedly, the IOND)."},
        ],
        "notes": "Named-only outside its role as the frame for Strange Attraction; no scenes take place at party offices.",
    },
    {
        "name": "One World Association",
        "org_type": "political party",
        "tier": 2,
        "headquarters": "Ontario / Seattle campaign trail",
        "summary": "Arthur Vogel's eco-conscious Democratic affiliate: 'We cannot heal our nation until we have healed the Earth'",
        "description": (
            "The ecological advocacy group Arthur Vogel founded in 2052, since adopted by the "
            "Democratic Party as its presidential platform in exchange for lending Vogel "
            "respectability, money, and exposure. Its message: 'We cannot heal our nation until we "
            "have healed the Earth. We cannot make peace with ourselves until we have made peace with "
            "our planet. No one is above the laws of nature -- not people, not corporations.' The "
            "corporations oppose Vogel for exactly that reason."
        ),
        "leadership": [
            {"name": "Arthur Vogel", "title": "Presidential candidate", "notes": "Dwarf ecological attorney; secretly funded a TerraFirst! sabotage cell years before the campaign."},
            {"name": "Gary Grey", "title": "Vice-presidential candidate", "notes": "Troll Eagle shaman; a powerful public speaker who links his totem to the UCAS's founding symbolism."},
        ],
        "notes": "Political Poison: never appears as an organization in its own right, but Vogel's rally under its banner is Alan Riv's target for a mass poisoning.",
    },
    {
        "name": "Technocratic Party",
        "org_type": "political party",
        "tier": 2,
        "headquarters": "Federal District of Columbia (DeeCee)",
        "summary": "James Booth's establishment party -- 'the status quo' -- tainted by the 2056 rigged-election scandal",
        "description": "The incumbent party of the disgraced Steele/Booth administration, running on continuity and a promise to end 'this three-ring circus of a campaign.' Booth's chief goal is clearing his own name of the 2056 rigging scandal that got him impeached.",
        "leadership": [
            {"name": "James Booth", "title": "Presidential candidate", "notes": "Former Secretary of State and Vice President; corporate lawyer and DeeCee lobbyist by trade."},
            {"name": "Brandon Ekimatsu", "title": "Vice-presidential candidate", "notes": "Former Mitsuhama Computer Technologies executive; political moderate seen as a corporate lapdog."},
        ],
        "notes": "Dry Run: the (fictional, VR-simulated) target of the runners' bug-planting mission is Booth's own limousine -- an operation that never actually touches the real man.",
    },
    {
        "name": "Republican Party",
        "org_type": "political party",
        "tier": 2,
        "headquarters": "Federal District of Columbia (DeeCee)",
        "summary": "Franklin Yeats's hawkish 'Rebuild America' party, running on Bug City outrage and military expansion",
        "description": "The party backing General Franklin Yeats's promise to rebuild the UCAS military and, many suspect, reclaim California and press territorial claims against the CAS and NAN by force if diplomacy fails.",
        "leadership": [
            {"name": "General Franklin Yeats", "title": "Presidential candidate", "notes": "Retired UCAS Army general; Bug City is his personal cause."},
            {"name": "Anne Penchyk", "title": "Vice-presidential candidate", "notes": "Ork meta-rights advocate; secretly compromised by the Desolation Angels (see her NPC row)."},
        ],
        "notes": "Casualties of War: the entire adventure exists to protect the ticket's reputation and Penchyk's secret during a faked rescue mission into the Containment Zone.",
    },
    {
        "name": "Archconservative Party",
        "org_type": "political party",
        "tier": 3,
        "headquarters": "Downtown Seattle (Brackhaven Campaign Headquarters)",
        "summary": "Kenneth Brackhaven's 'One People, One Nation' party, secretly bankrolled and steered by the Humanis Policlub",
        "description": (
            "The vehicle for Kenneth Brackhaven's anti-Awakened, anti-dragon, 'return to traditional "
            "values' platform: 'I pledge to you, my friends -- I will use the office of the presidency "
            "to defend our traditions and the values of faith, family and country from any and all "
            "directions.' Publicly a business-and-family-values ticket; privately steered by Karl "
            "Brackhaven and the Seattle Humanis Policlub."
        ),
        "leadership": [
            {"name": "Kenneth Brackhaven", "title": "Presidential candidate", "notes": "See his NPC row -- an impostor concealing his predecessor's 2023 murder."},
            {"name": "William Ager", "title": "Vice-presidential candidate", "notes": "Ex-Fuchi America 'resources adjuster'; anti-elf zealot convinced of a secret 'elven conspiracy'."},
        ],
        "notes": "Ghost Story: the party's Seattle headquarters employs no metahumans at all and treats any metahuman visitor as a security incident (see the Brackhaven Campaign Headquarters location).",
        "allies": ["Humanis Policlub"],
    },
    {
        "name": "One Nation Under God",
        "org_type": "policlub",
        "tier": 1,
        "headquarters": "Not given",
        "summary": "Self-described 'not-for-profit citizen advocacy group' behind an inflammatory anti-Hernandez pamphlet",
        "description": "Publishers of a Shadowland-circulated pamphlet, 'Four Reasons Why You Shouldn't Vote for Rozilyn Hernandez,' framing her as an elitist mage-o-crat secretly steering the country through the Illuminates of the New Dawn: 'CAN WE AFFORD TO FIND OUT THE HARD WAY? ... THE COUNTRY YOU SAVE MAY BE YOUR OWN.'",
        "notes": "Super Tuesday campaign texture only; no scenes, no further role beyond the pamphlet.",
        "enemies": ["Illuminates of the New Dawn", "New Century Party"],
    },
    {
        "name": "Hawkshorne Chemical",
        "org_type": "corporation",
        "tier": 2,
        "headquarters": "Seattle",
        "summary": "Struggling Seattle chemical corp whose stockpiled banned pesticide becomes Alan Riv's weapon of choice",
        "description": (
            "A 'lame corp' bled by a decade of environmental lawsuits and bad publicity: 'some big "
            "losses over the past ten years have left them gasping for breath.' Decades ago it "
            "manufactured a pesticide toxic to metahumans; a TerraFirst! cell sabotaged the plant that "
            "made it, and Arthur Vogel's class-action suit got the chemical banned in 2048 -- but "
            "Hawkshorne quietly kept its remaining stock instead of destroying it, storing it behind "
            "Wolverine Security guards rather than in-house protection. 'No matter how many times they "
            "get slapped down because of enviro-regs, Hawkshorne doesn't learn.'"
        ),
        "notes": (
            "Political Poison: hired the shadow team Callieach, Red Lana, Webb, and Wheels to recover "
            "a stolen canister of the pesticide from the runner Silver after she stole it (for Alan "
            "Riv) and it began leaking. Never learns that the canister was meant for a mass poisoning "
            "at a Vogel rally rather than resale."
        ),
        "enemies": ["Reservoir Dogs"],
    },
    {
        "name": "Wolverine Security",
        "org_type": "corporation",
        "tier": 1,
        "headquarters": "Seattle",
        "summary": "Bargain-tier rent-a-cop agency guarding Hawkshorne Chemical's storage facility",
        "description": "A step below the Big corps' in-house forces -- 'not a bad outfit, but not very high-class, either' -- the kind of security agency a struggling corp like Hawkshorne Chemical hires because it cannot afford Knight Errant or its own force. Barghest guard dogs and baby-faced rookies rather than veterans.",
        "notes": "Political Poison: a Wolverine guard nicknamed 'Skippy' by the runner Silver nearly caught her stealing the pesticide canister; his shot cracked its valve, starting the leak that poisoned her.",
    },
    {
        "name": "Reservoir Dogs",
        "org_type": "gang",
        "tier": 1,
        "headquarters": "Puyallup Barrens (Hawkshorne Chemical Plant)",
        "summary": "Crazed, kamikaze-boosted go-gang cult serving the toxic shaman Alan Riv",
        "description": (
            "A gang of scarred, deformed street toughs of every metatype who have thrown in with the "
            "toxic shaman Alan Riv, living out of the burned-out Hawkshorne Chemical plant in the "
            "Puyallup Barrens: 'He's leading us to a real future. He's got serious mojo and everybody "
            "underground is afraid of him, but he's good to people who do what he wants.' Riv keeps "
            "them doped on kamikaze and sends them to retrieve stolen property or silence loose ends; "
            "a captured member breaks under Interrogation (5) and reveals Riv's lair and his grudge "
            "against Arthur Vogel, 'the Poisoner of the Great Mother.'"
        ),
        "notes": (
            "Stats: B(6) Q(5) S(6) I3 W4(5) C2 Ess5.9 Reaction4, Armor 5/3, TR/PR 3/3; Armed Combat 4, "
            "Firearms 4, Stealth 3, Unarmed Combat 4; hand razors, one dose of kamikaze; armor jacket, "
            "Colt America L36. Not led by Riv as a member -- he commands them as his followers, not "
            "their gang boss."
        ),
        "enemies": ["Hawkshorne Chemical"],
    },
    {
        "name": "Desolation Angels",
        "org_type": "cult",
        "tier": 3,
        "headquarters": "The Kaleidoscope, Chicago Containment Zone",
        "summary": "Mantis-spirit circle inside Bug City, fronting as an all-female street gang, that recruits powerful women as hosts",
        "description": (
            "A circle of mantis spirits operating inside the Chicago Containment Zone under the "
            "female mantis Vixen, hunting rival insect spirits to grow its strength and recruiting "
            "strong-willed women as hosts -- granting the mantis full access to a host's memories and "
            "skills to move undetected through human society. Before the Bug City outbreak, a Desolation "
            "Angels member (posing as street-gang muscle) tried and failed to invest simsense mogul "
            "Daniel Truman's son Mitchell with a male mantis spirit; Mitchell escaped that attempt but "
            "was later killed by other insect spirits (Shadowrun novel Burning Bright)."
        ),
        "leadership": [
            {"name": "Vixen", "title": "Circle leader", "notes": "Force 7 mantis spirit; ambitious, targets powerful women for hosting."},
        ],
        "notes": (
            "Casualties of War: recruited VP candidate Anne Penchyk as a host or asset (unconfirmed "
            "even by the book) and used the mantis Mara Suhar, in the guise of a reporter, to lure "
            "shadowrunners into the CZ under a fake rescue-mission cover -- the real goal being to get "
            "Penchyk's Containment Zone gate passcodes and schedules into Vixen's hands so mantis "
            "spirits can be smuggled out and infiltrate positions of influence. Trades captured "
            "humans with the ghoul community of Ghoultown. Base of operations: an abandoned nightclub, "
            "the Kaleidoscope, near Fullerton and Halsted on the edge of the Shattergraves."
        ),
        "enemies": ["Ghoultown", "The Volk"],
    },
    {
        "name": "The Volk",
        "org_type": "militia",
        "tier": 2,
        "headquarters": "Volksville, Chicago Containment Zone (along I-55 near 31st Street)",
        "summary": "Violently anti-metahuman, anti-magic survivalist enclave inside the Chicago Containment Zone",
        "description": (
            "A militant survivalist enclave controlling a walled section of the Containment Zone, "
            "claiming to protect the 'true' victims of Bug City -- mundane, unAwakened humans -- and "
            "murdering metahumans, magicians, and insect spirits alike on sight. Grown more militant as "
            "the Chicago winter drags on. Full canon detail in the Bug City sourcebook, pp. 113-14."
        ),
        "notes": (
            "Casualties of War: Mara Suhar led the runners and Anne Penchyk into Volksville on a false "
            "lead about Penchyk's brother, then revealed her mantis form and fled with Penchyk, "
            "leaving the runners to a howling mob of Volk who assume any bug sighting means disguised "
            "infiltrators. Volk Soldiers: Firearms 4, Interrogation 2, Unarmed Combat 3; AK-97 carbine, "
            "lined coat (4/2), radio communicator (the scan's attribute columns for this block are "
            "garbled beyond safe reconstruction and are omitted here)."
        ),
        "enemies": ["Desolation Angels", "Ghoultown"],
    },
    {
        "name": "Ghoultown",
        "org_type": "tribe",
        "tier": 2,
        "headquarters": "Cabrini-Green housing blocks, Chicago Containment Zone",
        "summary": "Walled ghoul community in the old Cabrini-Green projects, split between a cooperative faction and a militant separatist one",
        "description": (
            "Chicago relocated its ghoul population into the condemned Cabrini-Green public-housing "
            "blocks years before Bug City, walling them in for the neighbors' 'protection.' When the "
            "insect-spirit outbreak hit, that same wall made the enclave one of the safer places in the "
            "Containment Zone; the ghouls reinforced it, added guard towers, and armed their patrols -- "
            "'ironic, isn't it?' Full canon detail in the Bug City sourcebook, p. 150."
        ),
        "leadership": [
            {"name": "Tamir Grey", "title": "Community leader / diplomat", "notes": "Thin, skeletal, dual being who can assense; believes ghouls and 'norms' must unite against the bugs."},
            {"name": "Blaine Hammond", "title": "Commander, Ghoultown defense forces", "notes": "Militant separatist; wants no 'normals' inside Ghoultown except as livestock."},
        ],
        "notes": (
            "Casualties of War: ghouls scouting the Volk rescued the runners from a lynch mob and "
            "brought them to Grey, who traded intelligence on the Desolation Angels (the mantids have "
            "been trading for captured humans with Ghoultown, and a woman matching Mara Suhar's "
            "description represents them) for a favor -- smuggling his interview and journal disks on "
            "ghoul society out to the media. Ghoul stats: B7 Q6 S5 I4 W5 C1 Reaction4(6), TR/PR 3/2; "
            "Firearms 3, Tracking 3, Unarmed Combat 4; Enhanced Senses (hearing, smell); Allergy "
            "(Sunlight, mild), Reduced Sense (blind); lined coat, Uzi III. Hostile runners are held in "
            "a 'larder' stocked with preserved human meat until they can escape."
        ),
        "enemies": ["Desolation Angels", "The Volk"],
    },
    {
        "name": "Tir Ghosts",
        "org_type": "government agency",
        "tier": 4,
        "headquarters": "Tir Tairngire",
        "summary": "Elite, semi-mythical Tir Tairngire special-forces adept squad answering directly to the Council of Princes",
        "description": (
            "A special-operations unit of physical adepts reporting straight to Tir Tairngire's "
            "Council of Princes -- so deniable that street rumor holds they don't exist: 'Ghosts? They "
            "can't exist, chummer. They're just a myth.' Riven by factional loyalties among the "
            "different Princes, which has caused internal friction before. Prefer stealth, subterfuge, "
            "and non-lethal capture to open firefights."
        ),
        "leadership": [
            {"name": "Speren Silverblade", "title": "Field agent", "notes": "Believes elves are the world's rightful caretakers; condescending toward other metatypes but keeps his word when it serves him."},
        ],
        "notes": (
            "Strange Attraction: hunted a stolen orichalcum talisman (see Illuminates of the New "
            "Dawn) from Portland to Seattle, tortured and killed the Illuminates' Portland contact "
            "Birch Kirby for information, and pursued the runners and the fixer Bono through the city. "
            "Squad stats: B5 Q6 S5 I5 W5 C5 Ess6 Magic7 Reaction5, TR/PR 4/3, Initiate Grade 1; Armed "
            "Combat 6(9), Athletics 5(7), Car 4, Centering (Kata) 5, Etiquette (Elven) 4, Stealth 6(8), "
            "Unarmed Combat 6; Enhanced Centering (Combat Skills), Improved Ability (Armed Combat 3 / "
            "Athletics 2 / Stealth 2), Improved Reflexes 1, Killing Hands (SL), Pain Resistance 2; "
            "Crusader machine pistol, lined coat (4/2), monoknife (8L), shock glove (7S Stun)."
        ),
    },
    {
        "name": "Human Nation",
        "org_type": "terrorist cell",
        "tier": 2,
        "headquarters": "Unknown (cell-based)",
        "summary": "Militant anti-metahuman splinter of the Humanis Policlub, willing to commit mass-casualty terrorism",
        "description": (
            "A shadowy, more tactically violent offshoot of the Humanis Policlub, recruiting from "
            "prison contacts and ex-military washouts who see metahumans as a plague to be exterminated "
            "rather than merely opposed politically. Trained, well-equipped, and willing to die for the "
            "cause."
        ),
        "notes": (
            "Dry Run: a twelve-strong cell led by ex-UCAS-Marine Jack Neelson (dishonorably discharged "
            "for assaulting a metahuman off-base, radicalized in prison through Humanis contacts) "
            "seized Dunkelzahn's secret VisionQuest testing facility near Mason City, Iowa, wired it "
            "with explosives, and demanded the dragon withdraw from the presidential race or the "
            "facility -- and everyone in it, including the runners, mid-VR-test -- would be destroyed."
        ),
        "allies": ["Humanis Policlub"],
        "enemies": ["VisionQuest"],
    },
    {
        "name": "VisionQuest",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Lake Louise, Athabaskan Council",
        "summary": "Dunkelzahn's virtual-reality and simsense research company, bought from Ares Macrotechnology in 2037",
        "description": (
            "A leading-edge VR company Dunkelzahn purchased from Ares Macrotechnology in 2037 (Damien "
            "Knight brokered the sale for reasons never made public). Builds the technology behind the "
            "dragon's Lake Louise resort as well as covert VR test facilities elsewhere, including one "
            "near Mason City, Iowa, used to run unwitting shadowrunner teams through simulated jobs to "
            "refine scenarios -- without informing the test subjects that nothing they experience is real."
        ),
        "leadership": [
            {"name": "Carla Brooks", "title": "Head of security, Dunkelzahn's presidential campaign", "notes": "Elf; heavily cybered; oversees the Mason City facility's protection."},
        ],
        "notes": (
            "Dry Run: the facility's VR system perfectly simulates a DeeCee shadowrun -- including a "
            "full mock Secret Service Matrix host chain -- down to neural feedback so convincing that "
            "test subjects cannot tell it from reality (see MATRIX_HOSTS; that system exists only "
            "inside the simulation and is not a real Matrix host). A Human Nation cell seized the real "
            "facility while a runner team was mid-test."
        ),
        "enemies": ["Human Nation"],
    },
]

LOCATIONS = [
    {
        "name": "Hawkshorne Chemical Storage Facility",
        "location_type": "corporate facility",
        "district": "Seattle",
        "security_level": "Low Security",
        "controlling_org": "Hawkshorne Chemical",
        "summary": "Fenced warehouse where Hawkshorne stockpiled its banned pesticide, guarded by Wolverine Security and drugged barghests",
        "description": (
            "A secure warehouse holding metal racks of labeled canisters -- forbidden chemical "
            "compounds Hawkshorne Chemical was banned from selling in the UCAS but never destroyed, "
            "their sharp chemical stink cutting through a filter mask. Guarded by Wolverine Security's "
            "rent-a-cops and barghest guard dogs rather than in-house corporate security."
        ),
        "notes": "Political Poison: the runner Silver drugged the barghests with tainted meat scraps, stole a passkey from a low-level exec, and lifted a canister of the pesticide; a guard's shot cracked its valve on her way out, starting the leak that poisoned her.",
    },
    {
        "name": "Hawkshorne Chemical Plant (abandoned)",
        "location_type": "ruins",
        "district": "Puyallup Barrens, near Hell's Kitchen",
        "security_level": "No Security / Barrens",
        "summary": "Burned-out shell of the plant TerraFirst! sabotaged years ago, now the toxic shaman Alan Riv's lair and a Toxic Domain",
        "description": (
            "A single large building, condemned and fenced off with 'KEEP OUT' signs the city never "
            "enforced, gutted by the explosion that ended a TerraFirst! raid years earlier -- a maze "
            "of ruined machinery, rusting catwalks, and chemical-soaked corridors, charred and reeking "
            "under Alan Riv's control. Grimoire II treats the plant and its grounds as a Toxic Domain, "
            "with at least one Force 5 toxic earth spirit always on astral guard."
        ),
        "notes": "Political Poison: Riv converted a relatively intact conference room into a medicine lodge decorated with charred bones, painted symbols, and a defaced Vogel campaign poster; flyers for Vogel's Superdome rally and a crumpled map of the venue litter the table. Three spell-locked hell hounds guard the lodge itself. Home base of the Reservoir Dogs gang.",
        "controlling_org": "Reservoir Dogs",
    },
    {
        "name": "Brackhaven Campaign Headquarters (Seattle)",
        "location_type": "office building",
        "district": "Downtown Seattle",
        "security_level": "Corporate Standard",
        "controlling_org": "Archconservative Party",
        "summary": "Kenneth Brackhaven's downtown Seattle campaign office, deliberately staffed by no metahumans at all",
        "description": (
            "A nondescript, pastel-toned corporate office suite -- reception, comfortable chairs, "
            "campaign posters on the walls, a secretary behind a broad desk -- indistinguishable from "
            "a hundred others except for one detail: no metahumans work there, and none are welcome. "
            "Security personnel go on alert and notify Lone Star the moment a metahuman visitor enters, "
            "and campaign workers openly stare and mutter."
        ),
        "notes": "Ghost Story: Karl Brackhaven, Kenneth's uncle, runs the Seattle campaign from here and receives (unwelcome) visitors investigating his nephew's past; Secret Service agents and an on-call Lone Star fast-response team back up the in-house security.",
    },
    {
        "name": "Norton Sporting Goods",
        "location_type": "shop",
        "district": "Redmond Barrens",
        "security_level": "No Security / Barrens",
        "summary": "Defunct storefront -- decrepit 2040s mannequins in the window -- wired with explosives as a hitman's trap",
        "description": "An old storefront in surprisingly good shape for its block, a faded 'Norton Sporting Goods' sign still in the window behind decrepit mannequins modeling street-surfing gear a decade and a half out of style. The interior holds nothing but wreckage and whatever looters left behind.",
        "notes": "Ghost Story: Fletcher Quinn, hired by Karl Brackhaven, lured the runners here with a forged message from Karen Johanssen, wired the store to level it, and waited on a nearby rooftop with a poisoned compound bow to pick off survivors.",
    },
    {
        "name": "Chicago Containment Zone (Bug City)",
        "location_type": "military installation",
        "city": "Chicago",
        "district": "Central Chicago",
        "security_level": "Zero Zone -- Lethal Response",
        "summary": "The walled-off, insect-spirit-infested heart of Chicago, under permanent UCAS Army quarantine",
        "description": "The section of Chicago overrun by insect spirits and sealed behind the Wall -- a barricade of demolished buildings, fencing, razor-wire, and guard towers ringing the city, patrolled by UCAS Army units under strict shoot-on-sight orders for anyone trying to cross in either direction. Full canon detail in the Bug City sourcebook.",
        "notes": (
            "Casualties of War: entry by air (Piloting (8) vs. a Sensor Test, or interception by two "
            "Force 4 elementals under an astral combat mage), by land (climbing the debris Wall, "
            "Climbing (10), risk of Serious falling damage, Corporate Security Guard-statted UCAS "
            "sentries with AK-97s and grenade launchers), or by water (frozen-lake crossing in winter, "
            "Navy sensor buoys, risk of falling through the ice). Inside, the Zone has fractured into "
            "hostile enclaves: the Volk, Ghoultown, and the Desolation Angels' turf near the fallen "
            "Sears Tower (the Shattergraves)."
        ),
    },
    {
        "name": "Volksville",
        "location_type": "gang territory",
        "city": "Chicago",
        "district": "Chicago Containment Zone (along I-55, near 31st Street)",
        "security_level": "No Security / Barrens",
        "controlling_org": "The Volk",
        "summary": "The Volk's fenced enclave inside Bug City, defended by armed patrols and monitored gates",
        "description": "A section of the Containment Zone the Volk have ringed with chain-link and concertina wire (Barrier Rating 5), gates manned by four guards each, patrolled in pairs that keep each other in sight -- neat and militant compared to the ruin around it.",
        "notes": "Casualties of War: Mara Suhar led the runners and Anne Penchyk here on a false lead about Penchyk's brother, then betrayed them, triggering a mob that treats every stranger as a suspected bug.",
    },
    {
        "name": "The Kaleidoscope",
        "location_type": "nightclub",
        "city": "Chicago",
        "district": "The Shattergraves (near Fullerton and Halsted)",
        "security_level": "No Security / Barrens",
        "controlling_org": "Desolation Angels",
        "summary": "Abandoned nightclub the Desolation Angels use as a base and holding pen for human captives",
        "description": "A dark, shuttered nightclub on the ruined outskirts of the Shattergraves -- the haunted ground surrounding the fallen Sears Tower -- its unlit sign still readable in the ruins. Secured with Rating 3 maglocks, walls of Barrier Rating 15, and armored-glass doors and windows of Barrier Rating 8; a faint light and the occasional scream are the only signs anyone is home.",
        "notes": "Casualties of War: base of operations for Vixen's mantis circle; holds fresh victims and captive hosts-to-be, and is where Anne Penchyk is 'held' before the runners free her.",
    },
]

NPCS = [
    {
        "name": "Alan Riv",
        "role": "Toxic Dog shaman plotting mass murder at a Vogel rally to avenge his disfigurement",
        "archetype": "Toxic Shaman",
        "title": "Leader, Reservoir Dogs (unofficial)",
        "race": "Elf",
        "gender": "Male",
        "connection": 3,
        "description": (
            "Once a fiery, idealistic young TerraFirst! saboteur, Riv survived a botched raid on "
            "Hawkshorne Chemical horribly burned and now believes the world a twisted, uncaring place "
            "where 'nobody really cares for anything other than themselves.' He hates physically "
            "attractive people, especially other elves, and will not allow mirrors or reflective "
            "surfaces near him. A corrosive or acid-based attack sends him into an unstoppable "
            "berserk flashback to the fire that scarred him, screaming, fighting until he or everyone "
            "around him is dead."
        ),
        "background": (
            "Years ago, Riv's TerraFirst! cell tried to sabotage a Hawkshorne Chemical plant making a "
            "banned metahuman-toxic pesticide -- a raid secretly arranged by Arthur Vogel as part of a "
            "quasi protection racket. Hawkshorne's security ambushed them; the cell and many guards "
            "died in the resulting explosion. Riv alone survived, badly burned, and fled into the "
            "sewers, where isolation and pain twisted his shamanic path toward toxic magic. He rebuilt "
            "himself as a Toxic Dog shaman, gathered underground outcasts as followers, and never "
            "stopped planning revenge on the man he blames for everything: Arthur Vogel, 'the "
            "Poisoner of the Great Mother.'"
        ),
        "notes": (
            "Political Poison: hired the runner Silver to steal a canister of Hawkshorne's stockpiled "
            "pesticide; when it leaked and Silver nearly died, Riv sent toxic earth spirits and the "
            "Reservoir Dogs gang to retrieve it. Rigged the canister with a timer above the crowd at "
            "Vogel's Superdome rally, using his Gecko Crawl spell to move freely on beams and catwalks. "
            "Stats: B4 Q5 S4 I5 W6 C6 Ess6 Magic 11(15) Reaction5, Init 5+1D6, TR/PR 6/4, Initiate "
            "Grade 5; Armed Combat 4, Conjuring 7, Electronics (Demolitions) 3, Enchanting 5, Etiquette "
            "(Street/Underground) 6, Firearms 4, Leadership 6, Magical Theory 5, Sorcery 6, Stealth 6, "
            "Unarmed Combat 3; animal-skull necklace (Power Focus 4), lined coat (4/2), orichalcum-"
            "tipped spear (Weapon Focus 4, +2 Reach, 6M), Uzi III SMG (7M, laser sight, gas-vent 2). "
            "Spells: Manabolt 5, Stunball 6, Urban Renewal 5, Animal Spy 4, Combat Sense 3 (quickened), "
            "Detect Life 2, Resist Serious Pain 2, Treat 3, Acid 6, Control Animal 5, Gecko Crawl 3 "
            "(quickened), Agonizing Pain 6, Personal Physical Barrier 6, Shadow 4. Always keeps a Force "
            "5 toxic earth or water spirit nearby in astral space; several more guard his lair."
        ),
    },
    {
        "name": "Silver",
        "role": "Independent Seattle runner poisoned stealing the canister that draws everyone into Political Poison",
        "archetype": "Infiltrator",
        "title": None,
        "race": "Human",
        "gender": "Female",
        "connection": 2,
        "description": (
            "Adrienne DuMont, known on the street as Silver: a corporate executive's daughter who left "
            "a stiflingly conformist home at eighteen. Cool under a gun in her face -- 'Security "
            "inspection, mister, from head office. This place is in pretty sorry shape' -- specializes "
            "in stealth break-ins and thefts of small, valuable items: get in, get the goods, get out, "
            "no one the wiser."
        ),
        "background": "Built a solid reputation running with teams that never sacrifice their own; on at least one job her quick thinking saved the whole team.",
        "notes": (
            "Political Poison: hired by Alan Riv (through an unnamed Johnson) for a snatch-and-grab on "
            "a Hawkshorne Chemical storage facility. A guard's shot cracked the stolen canister's seal "
            "on her way out; she made it to her safehouse before collapsing, and a PC friend has to "
            "save her (Biotech (4) to diagnose, Biotech (8) with a medkit for an antidote, or an "
            "Antidote Deadly Toxin spell at TN 8 plus a Body (8) test for her, 2+ successes needed). "
            "Stats: B5 Q5 S3 I4 W4 C5 Ess3.3 Reaction5(7), Init 5(7)+1D6, TR/PR 5/?; Armed Combat 4, "
            "Athletics 5, Car 3, Etiquette (Corporate) 4 / (Street) 5, Firearms 6, Stealth 6, Unarmed "
            "Combat 6; cybereyes with low-light, smartlink, Wired Reflexes 1; armor clothing (3/0), "
            "Browning Ultra Power, fake-SIN credstick (1,500 nuyen), portable phone, trauma patch, 3 "
            "stimulant patches."
        ),
    },
    {
        "name": "Callieach",
        "role": "Ork Raven shaman leading Hawkshorne's hired shadow team, greedy and utterly mercenary",
        "archetype": "Raven Shaman",
        "title": "Team leader",
        "race": "Ork",
        "gender": "Female",
        "connection": 2,
        "description": (
            "A tough and wily old bird, much like her totem, following a neo-Celtic shamanic tradition "
            "(not a druid). Insatiably greedy and coldly professional -- 'the old crone is tougher than "
            "nails and has a heart of ice. She'd sell out her own family if she had any' -- though her "
            "jobs together with her team have stayed mutually profitable so far."
        ),
        "notes": (
            "Political Poison: hired by Hawkshorne Chemical to recover the pesticide canister Silver "
            "stole; raided Silver's safehouse with Red Lana, Webb, and Wheels. Stats: B6 Q4 S5 I5 W6 "
            "C5 Ess6 Reaction4, Init 4+1D6, TR/PR 5/3; Armed Combat (Knife) 5, Conjuring 6, Enchanting "
            "5, Etiquette (Street) 4, Firearms 4, Gaelic (Centering) 5, Magic Theory (Shamanic) 5, "
            "Negotiation 5, Sorcery 6; armor clothing (3/0), feather cloak (spell lock, Raven Form), "
            "spell fetishes, walking stick (Manipulation focus 4), Streetline Special holdout pistol, "
            "thermographic goggles. Spells: Barrier 6, Clairvoyance 4, Clout 4, Cripple Limb 4, "
            "Foretelling 3, Invisibility 2, Magic Fingers 3, Paralyze 5, Poltergeist 4, Raven Form 3, "
            "Sap Strength 5, Sleep 6, Thunderclap 6, Wind 5."
        ),
        "contact_skills": ["Corporate wetwork and 'personnel adjustment' contracts"],
    },
    {
        "name": "Red Lana",
        "role": "Vain, heavily chromed street samurai on Callieach's hired team",
        "archetype": "Street Samurai",
        "title": None,
        "race": "Human",
        "gender": "Female",
        "nationality": "Anglo-Korean",
        "connection": 1,
        "description": "Known for the trademark red leather she wears as working clothes; all the physical attractiveness modern chrome can supply and little warmth behind it. A skilled killer with a history of wetwork who watches Webb's back more closely than anyone else's -- feelings she would never admit to.",
        "notes": (
            "Political Poison: raided Silver's safehouse with Callieach's team. Stats: B8(9) Q4(4.5) "
            "S6(7) I5 W5 C2 Ess0.1 Reaction5, Init 5(9)+3D6, TR/PR 5/3; Armed Combat (Bladed) 6, Car 3, "
            "Etiquette (Street) 4, Firearms 6, Stealth 5, Unarmed Combat 6; cybereyes with low-light, "
            "dermal plating 2, muscle replacement 1, retractable hand razors, smartlink, Wired Reflexes "
            "2; Ares Predator II (laser sight), armor jacket (5/3), Ingram Smartgun SMG (smartgun "
            "link), katana, thermographic goggles."
        ),
    },
    {
        "name": "Webb",
        "role": "Zen-like Brazilian physical adept on Callieach's hired team, master of unarmed combat",
        "archetype": "Physical Adept",
        "title": None,
        "race": "Human",
        "gender": "Male",
        "nationality": "Brazilian",
        "connection": 1,
        "description": "Slim and lithe, a master of unarmed combat whose hands smash through wood and brick as easily as flesh. Prefers close-quarters melee over guns and takes real pleasure in beating opponents down; maintains an air of Zen detachment otherwise.",
        "notes": (
            "Political Poison: raided Silver's safehouse with Callieach's team. Stats: B6 Q5 S5 I4 W5 "
            "C2 Ess6, Init 4+2D6, TR/PR 3/3; Armed Combat 4, Firearms 5, Stealth 5, Unarmed Combat "
            "(Martial Arts) 7(10); Killing Hands (M), Improved Reflexes 1, Improved Unarmed Combat 3, "
            "Pain Resistance 3, Smashing Blow; armor jacket (5/3), Browning Ultra Power, thermographic "
            "goggles."
        ),
    },
    {
        "name": "Wheels",
        "role": "Apathetic elf rigger/decker driving and scouting for Callieach's hired team",
        "archetype": "Rigger",
        "title": "Team driver and spymaster",
        "race": "Elf",
        "gender": "Male",
        "connection": 1,
        "description": "Cares about little beyond his latest piece of electronic hardware; shadowrunning is a video game to him. Combines drone surveillance with Callieach's astral scouting to case targets before every job, and only truly relaxes buttoned up behind a remote deck or inside one of his armored vehicles.",
        "notes": (
            "Political Poison: raided Silver's safehouse with Callieach's team. Stats: B? Q6 S4 I6 W5 "
            "C4 Ess1.5 Reaction6(10), Init 6(10)+1D6(3D6); TR/PR 3/3; Bike 4, Car 5, Computer 3, "
            "Electronics 4, Etiquette (Street) 1, Firearms 2, Gunnery 4, Ground Vehicles (B/R) 4; "
            "cybereyes (low-light, flare protection, thermographic), datajack, radio, smartlink, "
            "Vehicle Control Rig 2; Ares Predator II, armor jacket (5/3), EuroCar Westwind 2000 "
            "(concealed LMG and 2-shot AVM launcher), Hunter-Spotter Drone (2 LMGs, remote gear), "
            "remote control deck, surveillance drone."
        ),
    },
    {
        "name": "Speren Silverblade",
        "role": "Tir Ghosts field agent hunting the stolen orichalcum key across Strange Attraction",
        "archetype": "Elf Special Agent",
        "title": "Field agent, Council of Princes",
        "race": "Elf",
        "gender": "Male",
        "connection": 3,
        "organization": "Tir Ghosts",
        "description": (
            "A loyal Tir Tairngire citizen who genuinely believes elves are the world's rightful "
            "caretakers, condescending toward every other metatype. Prefers stealth and subtlety over "
            "firepower; shows the runners considerable mercy as long as they remain useful to him, and "
            "none at all once they stop being so. 'The parties I represent are not interested in "
            "retribution against you, but they do require information about the individuals who hired "
            "you for the run.'"
        ),
        "background": "Does not know the true nature of the orichalcum talisman he is pursuing -- only that his mentors on the Council of Princes want it back badly enough to authorize torture and murder.",
        "notes": (
            "Strange Attraction: tracked the stolen key from Portland art collector Birch Kirby (whom "
            "he killed for information) to Seattle, captured the runners outside the Underworld 93 or "
            "at a Ghosts safehouse, interrogated them with a quickened Analyze Truth and a Mind Probe "
            "spell, and offered amnesty (plus a largely ceremonial elven blood oath) in exchange for "
            "help identifying their employer. Stats: B5 Q6 S4 I5 W6 C5 Ess6 Magic 9 Reaction5, Init "
            "5+3D6, TR/PR 6/3, Initiate Grade 3; Armed Combat (Blade Weapons) 6, Car 4, Conjuring 5, "
            "Etiquette (Elf) 5, Firearms 5, Leadership 5, Magic Theory 4, Sorcery 6, Stealth 5, Unarmed "
            "Combat 6; 'Argentine,' a silver-chased longsword (stacked Rating 4 Power/Weapon Focus), "
            "Crusader machine pistol, armored long coat over body armor (5/3), Vashon Island miner "
            "shackles, 2 smoke grenades. Spells: Manabolt 6, Sleep 5, Increase Reflexes +2: 3(6, "
            "quickened), Paralyze 4, Treat 2, Bind 4, Magic Fingers 3, Personal Bullet Barrier 5, "
            "Analyze Truth 3 (quickened), Clairvoyance 2, Enhance Aim 4 (quickened), Mind Probe 3, "
            "Personal Combat Sense 4 (quickened), Chaotic World 4, Disregard 3, Mask 3, Silence 4."
        ),
    },
    {
        "name": "Belladonna",
        "role": "Aztechnology hitwoman-troubleshooter hunting the orichalcum key for her corporate masters",
        "archetype": "Assassin",
        "title": "Personal assistant to a high-ranking Aztechnology executive",
        "race": "Human",
        "gender": "Female",
        "connection": 2,
        "organization": "Aztechnology",
        "description": "Heavily cybered (though not yet cybermantic) and stunningly enhanced, walking a razor's edge as 'a huntress who lives for the thrill of the hunt and the kill.' Likes to toy with prey when she can spare the time, and enhances her chrome with a carefully chosen wardrobe.",
        "notes": (
            "Strange Attraction: assigned to recover the stolen orichalcum key for Aztechnology, "
            "sniping at the runners to raise the stakes (Deadly Nightshade) and later converging on the "
            "final handoff (Good Night, Gracie). Highly resistant to interrogation; carries no ID, is "
            "paid via certified credstick. Stats: B5(7) Q6(9) S5(8) I5 W6 Ess1.26 Reaction7(11), Init "
            "7(11)+3D6, TR/PR 6/4; Armed Combat 6, Athletics 5, Cyberweapons 8, Etiquette (Corporate) 3 "
            "/ (Street) 5, Firearms 7, Seduction 6, Stealth 8, Unarmed Combat 8; beta-grade 2 cyberarms "
            "(Str+3, Qui+3, hand razors, smartgun link II), cybereyes (low-light, thermographic), 2 "
            "cyberlegs (Str+3, Qui+3), datajack, oral spur, Wired Reflexes 2; armor jacket over body "
            "armor (6/4), Colt Manhunter with extra clip, Ranger Arms sniper rifle, throwing spikes "
            "(BL, neuro-stun toxin, 6S Stun on any Light+ wound)."
        ),
    },
    {
        "name": "Beaumont Noble",
        "role": "Small-time Seattle fixer -- 'Bono' -- who unwittingly set the runners up for Strange Attraction",
        "archetype": "Fixer",
        "title": None,
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": "A low-class, small-time fixer, wire-frame glasses and several days' beard, slouching like he wants to vanish into his own oversized jacket. Paranoid at the best of times, whining and asking needless questions when out of his depth -- which this job put him firmly in: 'Where the frag are you? Please be there ... Okay, I've gotta talk to you about the job. There have been some, uh, complications ... This is fraggin' big, omae. Don't tell anyone, just get here quick, okay?'",
        "notes": (
            "Strange Attraction: hired by Nicholas Grace of the Illuminates of the New Dawn to hire the "
            "runners for the Portland smuggling job; when the return handoff fell through (the runners "
            "were captured and memory-wiped by Tir border guards), Bono assumed a double-cross and went "
            "underground, hunted by both the Tir Ghosts and the Illuminates. Stats: B2 Q3 S2 I5 W5 C3 "
            "Ess2.5 Reaction4, Init 4+1D6, TR/PR 2/2; Computer 3, Electronics 3, Etiquette (Street) 6, "
            "Evaluate Goods 6, Firearms 2, Interrogation 4, Negotiation (rating illegible in the scan); "
            "cybereyes, datajack, display link, headware memory (300 Mp); armor clothing (3/0), Colt "
            "America L36 (laser sight), pocket secretary."
        ),
    },
    {
        "name": "Nicholas Grace",
        "role": "Fanatical Illuminates of the New Dawn initiate mage who hired the runners for the doomed Portland job",
        "archetype": "Initiate Mage",
        "title": "Initiate, Illuminates of the New Dawn",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "organization": "Illuminates of the New Dawn",
        "description": (
            "Slim and bookish, wears glasses rather than risk corneal surgery affecting his magic. "
            "Fanatically devoted to Rozilyn Hernandez as a near-messianic figure who will finally win "
            "mundane society's respect for magicians. Willing to act unethically for the cause; centers "
            "himself with elaborate, faintly glowing arcane diagrams traced in the air by hand and arm."
        ),
        "notes": (
            "Strange Attraction: hired Bono to hire the runners to smuggle the orichalcum key from "
            "Portland to Seattle. At the final handoff, negotiates through a masked flunky (Physical "
            "Mask spell) while scrying and hiding nearby, backed by hired mercenaries. Stats: B3 Q5 S2 "
            "I6 W6 C5 Ess6 Magic 10 Reaction5, Init 5+2D6, TR/PR 5/3, Initiate Grade 4; Conjuring 6, "
            "Enchanting 6, Etiquette (Magical) 5 / (Political) 4, Gesture (Centering) 6, History 5, "
            "Leadership 2, Magic Theory 6, Political Theory 4, Sorcery 7; gold and copper amulet "
            "(anchoring item, Force 1 personal barrier + Force 3 detect bullet spell locks), silver "
            "ring set with an amethyst (Power Focus 3). Maintains five bound Force 5 elementals (two "
            "earth, one each of the others) at all times."
        ),
    },
    {
        "name": "Birch Kirby",
        "role": "Portland art collector and Illuminates contact who handed over the orichalcum key -- and paid for it with his life",
        "archetype": "Art Collector",
        "title": "Illuminates of the New Dawn contact, Portland",
        "gender": "Male",
        "connection": 2,
        "organization": "Illuminates of the New Dawn",
        "description": "A rich Portland art collector who received the runners as honored guests -- a sumptuous dinner served in a large dining room before a short man he trusted brought in a locked box and spoke in hushed tones, passing over the orichalcum key.",
        "notes": "Strange Attraction: killed by the Tir Ghosts before the adventure proper begins, tortured for information about the key's new carriers; his own driver dropped the runners near the Tir border afterward. Never appears alive on-page -- known only through flashback fragments and Ghosts intelligence.",
    },
    {
        "name": "Anne Penchyk",
        "role": "Franklin Yeats's VP running mate, secretly compromised by the Desolation Angels mantis cabal",
        "archetype": "Political Operative",
        "title": "Vice-presidential candidate (Yeats ticket)",
        "race": "Ork",
        "gender": "Female",
        "connection": 4,
        "organization": "Republican Party",
        "description": (
            "Iron-willed and used to not taking no for an answer -- built her own marketing-consulting "
            "firm, AP Designs, from nothing after goblinizing in her twenties cost her a promising "
            "advertising career. A tireless metahuman-rights advocate and former two-term Wisconsin "
            "Representative. Shows up armed and armored to join the run herself: 'We've decided to go "
            "with you. Any objections? Good. Then let's move it. The passcodes are only good for 24 "
            "hours.' Refuses to yield to the runners' judgment even though it is their expertise she "
            "hired; her only goal is getting into the Containment Zone."
        ),
        "background": (
            "Met General Franklin Yeats through Congressional debates over metahuman integration into "
            "the military; the two became close friends, and he picked her as his running mate. Her "
            "brother Vincent was trapped in Chicago when the Containment Zone went up; friends say her "
            "personality has changed since."
        ),
        "notes": (
            "Casualties of War: hired the runners (through the mantis spirit 'Mara Suhar') to escort her "
            "into the Containment Zone under the pretext of rescuing Vincent -- who is already dead. "
            "The book leaves it deliberately ambiguous whether Penchyk has already been made a mantis "
            "host; what is certain is that she has been feeding Vixen's circle CZ gate passcodes and "
            "military schedules gained through Yeats, and will sacrifice the runners without hesitation "
            "to protect the cabal's plans. Stats: B6 Q3 S4 I4 W4 C4 Ess5 Reaction3, Init 4+1D6, TR/PR "
            "2/3; Administration 4, Car 2, Etiquette (Corporate) 6 / (Media) 4 / (Political) 6, "
            "Leadership (Political) 4, Marketing 8, Negotiation 6; chipjack, datajack, display link, "
            "headware memory (50 Mp)."
        ),
    },
    {
        "name": "Mara Suhar",
        "role": "Cover identity of a Desolation Angels mantis spirit, formerly a real Chicago anchorwoman",
        "archetype": "Mantis Spirit",
        "title": None,
        "race": "Human (possessed)",
        "gender": "Female",
        "connection": 3,
        "organization": "Desolation Angels",
        "description": (
            "Once an award-winning Chicago anchorwoman of East Indian descent, dark-skinned with pouty "
            "lips and a loose dark braid over one shoulder, known for hard-hitting investigative "
            "journalism -- captured while chasing Bug City leads too aggressively and invested with a "
            "female mantis spirit by Vixen. 'Suhar' as a person no longer exists; the spirit uses her "
            "memories and a compulsion power to steer the humans around her: 'You've done well. I'll "
            "leave you to your fellow humans.'"
        ),
        "notes": (
            "Casualties of War: hired the runners under a fake rescue story, led them and Anne Penchyk "
            "into Volksville, then revealed her true form and fled with Penchyk once the Volk mob "
            "turned on the party. Stats (manifest form; astral form uses Force for all attributes): B8 "
            "Q6(4x4) S5 I5 W5 Reaction15(25), Init 25(35)+1D6, Force 5, TR/PR 5/4, Skill 15, Damage 8S; "
            "Animal Control (Mantids), Aura Masking, Compulsion, Enhanced Senses (Smell), Fear, Human "
            "Form, Summoning; Vulnerability (Insecticides). Treat as a Grade 6 initiate for purposes of "
            "resisting aura masking detection."
        ),
    },
    {
        "name": "Vixen",
        "role": "Force 7 mantis spirit leading the Desolation Angels' Chicago circle",
        "archetype": "Mantis Spirit",
        "title": "Circle leader, Desolation Angels",
        "race": "Free Spirit",
        "gender": "Female",
        "connection": 2,
        "organization": "Desolation Angels",
        "description": "The dominant female of the mantis circle operating inside Bug City, ambitious and expansionist -- recruiting strong-willed women as hosts so the cabal can move undetected into positions of influence outside the Containment Zone.",
        "notes": (
            "Casualties of War: personally recruited Anne Penchyk and directs the operation to smuggle "
            "mantis spirits out of the CZ using Penchyk's access. Confronts the runners at the "
            "Kaleidoscope when they come for Penchyk. Stats (manifest form; astral form uses Force for "
            "all attributes): B(11) Q(16) S7 I? W(7) Reaction7, Init 7(27)+1D6, Force 7, TR/PR 7/3, "
            "Skill 7, Damage 10S; Animal Control (Mantids), Aura Masking, Compulsion, Enhanced Senses "
            "(Smell), Fear, Human Form, Summoning; Vulnerability (Insecticides)."
        ),
    },
    {
        "name": "Tamir Grey",
        "role": "Ghoultown's cooperative-faction leader, a shrewd diplomat trading intelligence for a media favor",
        "archetype": "Ghoul Leader",
        "title": "Community leader, Ghoultown",
        "race": "Ghoul",
        "gender": "Male",
        "connection": 3,
        "organization": "Ghoultown",
        "description": "So thin even for a ghoul that his features look sculpted from steel; waves a skeletal hand to take in the whole cramped office around him. 'Welcome to Ghoultown. My name is Tamir Grey, and I have a proposition for you.' A dual being who can assense auras, which he uses throughout every conversation to catch a lie. Believes ghouls and 'norms' must cooperate against the insect spirits or none of them survive Bug City.",
        "notes": (
            "Casualties of War: rescued the runners from a Volk lynch mob and questioned them at length; "
            "in exchange for the truth, traded intelligence that the Desolation Angels have been trading "
            "for captured humans and that a woman matching Mara Suhar's description represents them, and "
            "asked the runners to smuggle his interview and journal disks -- documenting ghoul society "
            "and survival in the CZ -- out to the media (sellable for up to 10,000 nuyen). Rival to "
            "Blaine Hammond's militant separatist faction within Ghoultown."
        ),
        "contact_skills": ["Ghoultown politics and the Chicago ghoul community"],
    },
    {
        "name": "Blaine Hammond",
        "role": "Militant separatist commander of Ghoultown's defense forces, hostile to Tamir Grey's cooperation with outsiders",
        "archetype": "Ghoul Commander",
        "title": "Commander, Ghoultown defense forces",
        "race": "Ghoul",
        "gender": "Male",
        "connection": 1,
        "organization": "Ghoultown",
        "description": "Tall and muscular for a ghoul, dressed in combat leathers with a sidearm like almost every Ghoultown resident. Storms into Grey's office snarling and baring his sharp teeth, furious that Grey brought outsiders in without consulting the other leaders; makes clear he wants no 'normals' inside Ghoultown at all -- except, perhaps, as livestock.",
        "notes": "Casualties of War: argues with Grey and storms out again; does not act against the runners directly in this book, but is a standing internal threat to any future dealings with Ghoultown.",
    },
    {
        "name": "Kenneth Brackhaven",
        "role": "Archconservative presidential candidate -- and a murdered ork boy's identity, stolen and worn for thirty years",
        "archetype": "Politician",
        "title": "Presidential candidate, Archconservative Party ('One People, One Nation')",
        "race": "Human",
        "gender": "Male",
        "connection": 5,
        "organization": "Archconservative Party",
        "description": (
            "A polished, designer-suited Seattle magnate who presents himself as a self-made success "
            "story and a defender of 'traditional values' -- family, faith, and a UCAS purged of "
            "metahuman influence: 'I pledge to you, my friends -- I will use the office of the "
            "presidency to defend our traditions and the values of faith, family and country from any "
            "and all directions.' Publicly unreachable behind a wall of Secret Service and campaign "
            "security; the runners are never able to meet him directly."
        ),
        "background": (
            "The real Kenneth Brackhaven, an ork born in 2011, goblinized in 2023 and was secretly "
            "murdered in his hospital bed by his own father Charles Brackhaven, ashamed of a metahuman "
            "heir. A SINless orphan was surgically and psychologically conditioned to replace him and "
            "raised by Charles and his brother Karl to share their hatred of metahumans; that impostor "
            "inherited the family fortune in 2044 and, backed by Humanis Policlub money and doctrine, is "
            "now running for the UCAS presidency on the very bigotry that killed the boy whose name he "
            "carries. If exposed, Brackhaven tearfully claims (genuinely, per the book) that he has no "
            "memory of the events, having been 'very sick' as a child."
        ),
        "notes": (
            "Ghost Story: the murdered boy's ghost haunts Seattle General Hospital, appearing to a "
            "hospitalized runner in dreams and poltergeist manifestations, pleading 'Father? It hurts. "
            "I'm sorry, please don't be mad. It hurts so much. Make it stop, please make it stop ... "
            "I'm not a monster! I'm not, I'm just Kenny. Why do you all hate me? Help me, please help "
            "me,' seeking only to have the truth told. It cannot be banished by force (any attempt "
            "knocks the caster unconscious into the boy's death-memory instead) and rests only if the "
            "truth of the murder and substitution is finally exposed -- appearing one last time to smile "
            "at the runners before fading into darkness. No combat stats are given for either the ghost "
            "or the adult candidate; both are purely narrative figures."
        ),
    },
    {
        "name": "Dr. Christina Falt",
        "role": "World-weary Redmond Barrens street doc who blew the whistle on the fraudulent research covering up Brackhaven's murder",
        "archetype": "Street Doc",
        "title": None,
        "race": "Human",
        "gender": "Female",
        "age": 58,
        "connection": 2,
        "description": "A world-weary woman who has seen the Ghost Dance War, the Awakening, goblinization, and every plague since, and whom nothing shocks anymore: 'Always willing to help. What foolishness have you gotten yourselves into?' Honest, no-nonsense, and impossible to intimidate or fool with a line -- 'I was ready to take on the world. I thought I could really make a difference and help to heal people.'",
        "background": (
            "An intern at Seattle General Hospital during the 2023 goblinization outbreak, fired after "
            "raising concerns about Dr. Freeman's bogus 'goblinization remission' research project -- "
            "research secretly funded by Charles Brackhaven to cover up his son's murder. Freeman "
            "falsified hospital records to list Falt as the attending physician on Kenny Brackhaven's "
            "case, a lie that first points investigating runners her way. Later built a respected street "
            "clinic in the Redmond Barrens, reached through the fixer Walks-With-Yen."
        ),
        "notes": (
            "Ghost Story: tells honest investigators the true story of Freeman's research and points "
            "them toward his former research assistant and mistress, nurse Karen Johanssen, in exchange "
            "for a future favor. Stats: B2 Q3 S2 I6 W4 C4 Ess5.1 Reaction4, Init 4+1D6, TR/PR 1/3; "
            "Biotech 8, Cybertech 4, Car 2, Etiquette (Corporate) 2 / (Street) 4, Negotiation 3; blood "
            "filters 3, datajack, display link."
        ),
        "contact_skills": ["Street medicine and Redmond Barrens back-channel referrals"],
    },
    {
        "name": "Fletcher Quinn",
        "role": "Clinical, professional hitman hired by Karl Brackhaven to silence the runners and Karen Johanssen",
        "archetype": "Assassin",
        "title": None,
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": "A tall, silver-haired 'kick artist' who treats every job as an intellectual exercise, executed with clinical detachment and no personal malice toward his targets. Never fights unreasonable odds; prefers explosives, poisons, and a compound bow to a straight gunfight -- 'discretion is the better part of valor.'",
        "notes": (
            "Ghost Story: hired by Karl Brackhaven to eliminate the runners once their investigation "
            "becomes a threat. Wired the storefront Norton Sporting Goods to explode and sniped "
            "survivors with poisoned arrows (Shafted), then ambushed the runners again at Karen "
            "Johanssen's condo using her as a hostage (Parting Shot). If defeated rather than killed, "
            "may resurface working for Brackhaven -- or someone else -- in a future adventure. Stats: "
            "B5 Q6 S5 I4 W5 C3 Magic 6 Ess6 Reaction5, Init 5+3D6, TR/PR 5/2; Car 3, Chemistry (Toxins) "
            "5, Demolitions (Anti-Personnel) 4, Etiquette (Corporate/Street) 4, Firearms (Pistols) 5, "
            "Projectile Weapons (Bows) 8(10), Stealth 6(8), Unarmed Combat 6; Enhanced Senses (Vision "
            "Magnification 2), Improved Projectile Weapons (7), Improved Stealth (2), Increased "
            "Reflexes (2), Missile Parry; armor jacket, Colt Manhunter, form-fitting body armor, radio "
            "detonator, Ranger-X compound bow with 30 arrows, assorted explosives."
        ),
    },
    {
        "name": "Karen Johanssen",
        "role": "Tacoma DocWagon administrator unknowingly sitting on the proof of Kenneth Brackhaven's murder",
        "archetype": "DocWagon Administrator",
        "title": "Private care administrator, Tacoma DocWagon office",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "organization": "DocWagon",
        "description": "Divorced, in her fifties, dark hair, a smart gray business suit; peers through the security chain at her front door with wary eyes -- 'Yes? What do you want?' -- and threatens Lone Star at the first sign of trouble. Genuinely does not understand the significance of what she is holding.",
        "background": "Had an affair with Dr. Freeman decades ago while both worked at Seattle General Hospital during the goblinization crisis; never learned the full extent of his crimes.",
        "notes": (
            "Ghost Story: received a box of Dr. Freeman's papers after his death roughly a decade ago -- "
            "stored unread in her attic -- plus an encrypted optical disk (Computer (6) to crack) "
            "labeled 'SGH Years' containing his medical/DNA records for Kenneth Brackhaven's case and a "
            "written confession describing the murder and substitution, which Freeman kept as insurance "
            "against Charles Brackhaven. Stonewalls investigators (Astral Perception (4) or Perception "
            "(8) reveals she is lying) until Fletcher Quinn kidnaps and beats her looking for the same "
            "evidence; if the runners save her and pass a Charisma (4) test, she hands the material over."
        ),
    },
    {
        "name": "Walks-With-Yen",
        "role": "Redmond Barrens fixer who vets visitors for Dr. Christina Falt",
        "archetype": "Fixer",
        "title": None,
        "gender": "Male",
        "connection": 2,
        "description": "Wears a dark duster and broad-brimmed hat, keeps his hands visible at his sides, and takes contacts to Dr. Falt's clinic only after satisfying himself they mean her no harm: 'I hear you're looking for a consultation. You need to tell me about your symptoms before I can see if the doctor is in.' Respected by, and protective of, Falt.",
        "notes": "Ghost Story: meets contacts at the Partyzone at 1 a.m. and escorts them to Falt's basement clinic; warns that Falt has many friends -- some of them dangerous -- who would take it very personally if she were harmed.",
        "contact_skills": ["Redmond Barrens street medicine referrals"],
    },
    {
        "name": "Charles Brackhaven",
        "role": "Kenneth's father -- financier, virulent racist, and the murderer at the heart of Ghost Story -- dead since 2044",
        "archetype": "Corporate Financier",
        "title": "Founder, Brackhaven Investments (deceased)",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": "A corporate shark and virulent racist who taught his son 'everything he knew' -- once best known in certain political circles for publishing a tract 'proving' that humans were innately more intelligent than metahumans. A control freak who bought his son's way into university and business school rather than accept anything short of the golden boy he wanted.",
        "background": "Blamed his wife's death on Kenneth's birth and never forgave the boy; when Kenneth goblinized in 2023, Charles saw it not as his son's suffering but as his own image's final failure, and had the child killed and replaced rather than let a metahuman heir touch the family name. Died in 2044, having never been caught.",
        "notes": "Ghost Story: never appears on-page; known only through the testimony of Dr. Falt, the records held by Karen Johanssen, and Karl Brackhaven's own unrepentant recollection of the 'mercy killing.'",
    },
    {
        "name": "Dr. Freeman",
        "role": "Corrupt hospital physician who covered up Kenneth Brackhaven's murder for Charles Brackhaven's money -- dead about a decade before the adventure",
        "archetype": "Corrupt Physician",
        "title": "Former head of services, Seattle General Hospital (deceased)",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": "An 'expert at covering his own butt' who parlayed a bogus 'goblinization remission' research grant -- funded by Charles Brackhaven to explain away a murder -- into a lucrative career as the hospital's head of services.",
        "background": "Falsely listed intern Christina Falt as attending physician on Kenneth Brackhaven's 2023 case to distance himself from scrutiny, and had an affair with his research assistant, nurse Karen Johanssen, to whom he later entrusted his private insurance policy against Charles Brackhaven ever turning on him: a written confession and Kenneth's real medical and DNA records, hidden on an encrypted disk.",
        "notes": "Ghost Story: dead roughly ten years before the adventure begins; his hidden evidence, inherited unread by Karen Johanssen, is the proof that finally exposes the Brackhaven substitution.",
    },
    {
        "name": "Carla Brooks",
        "role": "Dunkelzahn's head of security, who recruits the runners for what turns out to be an unwitting VR test",
        "archetype": "Security Chief",
        "title": "Head of security, Dunkelzahn's presidential campaign",
        "race": "Elf",
        "gender": "Female",
        "connection": 4,
        "description": "Tall and willowy, snowy-haired, deep brown complexion and deep blue eyes, dressed in finely tailored evening wear and expensively tasteful jewelry -- poised and confident, at home in posh restaurants but happiest working alongside her security team, who consider her intelligent, competent, and scrupulously fair. Utterly loyal to Dunkelzahn: 'My boss needs a few people for a simple run -- a straightforward job, with minimal complications.'",
        "notes": (
            "Dry Run: recruits the runners at the Eye of the Needle restaurant for a supposed DeeCee "
            "shadowrun (planting a bug on James Booth's limousine) for 20,000 nuyen each -- actually a "
            "VisionQuest VR test scenario the runners are drugged into believing is real. Carries "
            "identification and a video statement from Nadja Daviar to prove her identity; wears enough "
            "magical countermeasures to block truth-detection. Extracts the runners after the Human "
            "Nation terrorist attack on the real facility, arranging transport and a bonus payment. "
            "Stats: B4 Q4 S4 I5 W6 C5 Ess1.775 Reaction4(10), Init 4(10)+1D6(4D6), TR/PR 3/4; "
            "Electronics 3, Etiquette (Corporate) 5 / (Security) 6, Firearms 5, Interrogation 2, "
            "Leadership 5, Negotiation 5, Stealth 2, Unarmed Combat 4; delta-grade cyberware including "
            "active softs, crypto circuit (10), cybereyes (camera, flare compensation, low-light, "
            "optical magnification 3, retinal clock, rangefinder, thermographic), datajack, display "
            "link, radio with com link, skillsofts, skillwire+ (9), smartlink, softlink (4), Wired "
            "Reflexes 3."
        ),
    },
    {
        "name": "Jack Neelson",
        "role": "Human Nation cell leader who seizes Dunkelzahn's secret VisionQuest facility mid-test",
        "archetype": "Terrorist Commander",
        "title": "Cell leader, Human Nation",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "organization": "Human Nation",
        "description": "A former UCAS Marine, dishonorably discharged for assaulting a metahuman off-base and radicalized in prison through Humanis Policlub contacts. Genuinely believes metahumans are a plague to be exterminated for the safety of his own race, yet carefully looks after the men and women under his command, accepting that 'tactical sacrifices are sometimes necessary.'",
        "notes": (
            "Dry Run: leads a twelve-strong commando cell (including rigger Mark Underhill, who takes "
            "control of the facility's security systems, and a decker) that seizes Dunkelzahn's secret "
            "VisionQuest test facility near Mason City, Iowa, wires it with explosives, and demands the "
            "dragon withdraw from the presidential race. Familiar enough with magicians from his Marine "
            "service that he is hard to catch off guard with a magical attack. Stats: B5(6) Q6(7) S6(7) "
            "I4 W5 C3 Ess1.1 Reaction5(9), Init 5(9)+3D6, TR/PR 5/4; Armed Combat 5, Athletics 5, Car 4, "
            "Etiquette (Military) (rating illegible in the scan), Firearms 7, Leadership 4, Stealth 4, "
            "Unarmed Combat 6; cybereyes with low-light and thermographic, datajack, dermal plating 1, "
            "muscle replacement 1, Wired Reflexes 2; Ares Predator II with 10 extra clips, armor jacket "
            "over body armor (the rest of his gear list is cut off in the scan -- the book's text ends "
            "mid-entry)."
        ),
    },
    {
        "name": "Mark Underhill",
        "role": "Human Nation's rigger, who seizes the VisionQuest facility's security systems during the siege",
        "archetype": "Rigger",
        "title": "Rigger, Human Nation commando cell",
        "gender": "Male",
        "connection": 1,
        "organization": "Human Nation",
        "description": "Jack Neelson's rigger, who takes the main security console the moment the facility falls, running Closed-Circuit Simsense surveillance on every corridor to hunt the runners as they try to escape or retake the site.",
        "notes": "Dry Run: uses the unmodified Rigger archetype (SR2 p.59); the runners must beat his Intelligence (6) in opposed Stealth Tests to move through the facility undetected, or overpower him directly at the security station to regain their confiscated equipment.",
    },
    {
        "name": "Dubronski",
        "role": "The runners' DeeCee fixer contact inside Dry Run's virtual-reality simulation",
        "archetype": "Fixer",
        "title": None,
        "race": "Ork",
        "gender": "Male",
        "connection": 1,
        "description": "A burly ork in a plaid jacket who looks the runners up and down with a perfect poker face at their pre-arranged meet, then hands over a surveillance bug and an optical chip of mission specs with no patience for questions: 'Look -- just do what you're told and take the cred, OK? Save your brilliance for figuring out how to get the bug in place.'",
        "notes": "Dry Run: exists only inside VisionQuest's VR test scenario -- a simulated contact the runners never actually meet, since the entire 'DeeCee run' is a fiction generated to test them. Provides the surveillance device and near-unlimited equipment (short of military or 'top secret' hardware) within 24 hours.",
    },
    {
        "name": "Dr. Tronsa",
        "role": "VisionQuest technician running the VR test simulations for Carla Brooks",
        "archetype": "VR Technician",
        "title": "Simulation technician, VisionQuest",
        "gender": "Male",
        "connection": 1,
        "description": "Watches over drugged, unconscious test subjects with clinical care before reporting results by telecom, visibly anxious about the project's stakes: 'Ms. ... Ms. Brooks, is my work producing satisfactory progress? I don't like calling only to report qualified failures ...' Talks himself out of wondering too hard what his superiors -- employed by a dragon -- actually want the simulation for.",
        "notes": "Dry Run prologue: runs the VR test on a prior shadowrunner team (Tanner, Marley, Half-Trak) before the player characters' own test run, resetting the simulation with new data after every failure.",
    },
    {
        "name": "Mr. Smith",
        "role": "Karl Brackhaven's smooth, anonymous intermediary sent to buy off investigating runners",
        "archetype": "Negotiator",
        "title": None,
        "gender": "Male",
        "connection": 2,
        "description": "A forgettable suit in a dim corner booth at Matchstick's, one hand extended, the other conspicuously visible on the tabletop: 'Good evening, won't you sit down? I believe that we have both a mutual acquaintance and a mutual interest.' Uses the Mr. Johnson archetype (SR2 p.216); his real name, he says, 'is of no importance.'",
        "notes": "Ghost Story: offers each runner access codes to a blind escrow account (5,000 nuyen, negotiable up to 10,000 nuyen per runner) to drop the Brackhaven investigation. Two bodyguards (Bodyguard archetype) back him up if threatened.",
    },
    {
        "name": "Tom Fiske",
        "role": "Veteran Secret Service team leader guarding James Booth inside Dry Run's VR simulation",
        "archetype": "Bodyguard",
        "title": "Team leader, Booth protection detail",
        "gender": "Male",
        "connection": 1,
        "description": "A thirteen-year Secret Service veteran who has protected two presidents, calm and no-nonsense under pressure. Uses the Bodyguard archetype (SR2 p.49) with Etiquette (Political) 4 and Security Procedures 5.",
        "notes": "Dry Run: exists only inside the VR simulation; leads Booth's fictional protection detail alongside Monique Karlen, Eldred O'Connor, and Kara Kiramatsu, and reports anything unusual straight to the central office with a backup request.",
    },
    {
        "name": "Monique Karlen",
        "role": "Government-trained security mage on James Booth's simulated protection detail",
        "archetype": "Combat Mage",
        "title": "Security magician, Booth protection detail",
        "gender": "Female",
        "connection": 1,
        "description": "Skilled but somewhat inflexible in her thinking, government-trained down to the letter of procedure; has clashed with team leader Tom Fiske over method before, though the two set differences aside on the job. Uses the Combat Mage archetype (SR2 p.50).",
        "notes": "Dry Run: exists only inside the VR simulation, part of Booth's fictional Secret Service detail.",
    },
    {
        "name": "Eldred O'Connor",
        "role": "Youngest member of James Booth's simulated protection detail, eager to prove himself",
        "archetype": "Physical Adept",
        "title": "Chief protection specialist, Booth protection detail",
        "gender": "Male",
        "connection": 1,
        "description": "The team's youngest member, in charge of guarding Booth directly and visibly feeling he has something to prove to Fiske and Karlen. Uses the Executive Protection Adept archetype (Corporate Security Handbook p.107).",
        "notes": "Dry Run: exists only inside the VR simulation, part of Booth's fictional Secret Service detail.",
    },
    {
        "name": "Kara Kiramatsu",
        "role": "'Kay-Kay,' the driver on James Booth's simulated protection detail",
        "archetype": "Rigger",
        "title": "Driver, Booth protection detail",
        "gender": "Female",
        "connection": 1,
        "description": "More comfortable buttoned up in her vehicle than navigating diplomatic small talk; trained in evasive and combat driving, stays with the car at all times, and privately thinks Eldred O'Connor is too much of a hot shot -- though she keeps that to herself. Uses the Rigger archetype (SR2 p.59) with Car 6 and Firearms 4.",
        "notes": "Dry Run: exists only inside the VR simulation, part of Booth's fictional Secret Service detail.",
    },
    {
        "name": "Arthur Vogel",
        "role": "Dwarf eco-lawyer presidential candidate whose secret TerraFirst! dealings created his own would-be assassin",
        "archetype": "Politician",
        "title": "Presidential candidate, Democratic Party ('One World')",
        "race": "Dwarf",
        "gender": "Male",
        "nationality": "Ontarian",
        "connection": 4,
        "organization": "One World Association",
        "description": (
            "One of the first dwarfs born in Canada after UGE, a dynamic courtroom champion of "
            "ecological causes -- 'we cannot heal our nation until we have healed the Earth' -- who "
            "built his career pulling off difficult settlements against major corporations. Publicly a "
            "passionate environmentalist; privately, for years, ran what amounted to a protection "
            "racket, using the threat of eco-terrorism to extract lucrative settlements from corporate "
            "opponents."
        ),
        "background": "Founded the One World Association in 2052 as a Democratic Party affiliate devoted to ecological consciousness; his running mate is Gary Grey, a troll Eagle shaman.",
        "notes": (
            "Political Poison: years ago, secretly sent a TerraFirst! cell to sabotage a Hawkshorne "
            "Chemical plant; the sole survivor, Alan Riv, was horribly burned and has spent years "
            "since plotting mass murder at a Vogel campaign rally in revenge. If the runners stop Riv, "
            "Vogel publicly calls them 'heroes for the environment' and owes them a future favor "
            "(useful if he wins); if the poison is released, he survives (he was never at the rally), "
            "uses the tragedy as a rallying cry against 'poison-spewing corporations,' and leads calls "
            "for the runners' deaths if they are caught."
        ),
    },
    {
        "name": "Gary Grey",
        "role": "Arthur Vogel's troll Eagle-shaman running mate, whose booming voice electrifies rallies",
        "archetype": "Politician",
        "title": "Vice-presidential candidate, One World Association",
        "race": "Troll",
        "gender": "Male",
        "connection": 2,
        "organization": "One World Association",
        "description": "A powerful public speaker in his own right, with a deep, resonant voice that 'can electrify a crowd' without half trying, playing cleverly on the connection between his Eagle totem and the old United States' national symbol: he speaks of Eagle and the UCAS in almost the same reverent tone, both proud and strong, 'capable of flying high and never meant to be caged or bound.'",
        "notes": "Political Poison background: never appears in the adventure itself, but stands alongside Vogel throughout the campaign bios -- the comical visual of a dwarf and a troll on the same ticket is remarked on more than once in the Shadowland chatter.",
    },
    {
        "name": "Dr. Rozilyn Hernandez",
        "role": "New Century Party candidate and Illuminates of the New Dawn initiate, at the center of Strange Attraction's stolen talisman",
        "archetype": "Politician",
        "title": "Presidential candidate, New Century Party",
        "race": "Human",
        "gender": "Female",
        "connection": 3,
        "organization": "New Century Party",
        "description": "A controversial social scientist and mage who has taught at Georgetown University for fourteen years: 'Our technology isn't doing enough. Magic isn't doing enough ... Magic and technology working together can show us the new directions that our nation needs to take.' Accused by critics of running her academic followers like a cult of personality -- 'she's as sharp as a monoblade, and just as dangerous.'",
        "background": "A high-grade initiate of the Illuminates of the New Dawn, the hermetic order that also backs her party and much of its staff. Her running mate is Ramsay McMulkin, a former Technocrat film star.",
        "notes": "Strange Attraction: never appears directly, but the entire adventure -- the theft of an orichalcum Tir talisman, the Tir Ghosts' manhunt, Aztechnology's interest -- unfolds because the Illuminates of the New Dawn are working, by means Hernandez may or may not sanction personally, to acquire magical assets in support of her candidacy.",
    },
    {
        "name": "James Booth",
        "role": "Disgraced former vice president running a comeback bid, unknowingly the target of a VR bugging test in Dry Run",
        "archetype": "Politician",
        "title": "Presidential candidate, Technocratic Party",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "organization": "Technocratic Party",
        "description": "A career corporate lawyer and lobbyist who rose fast -- Secretary of State in 2051, then Vice President after President Adams's sudden death in late 2052 -- only to be impeached alongside President Steele when the 2056 election was exposed as rigged: 'I believe my record of service to our nation speaks for itself, and I invite any other candidate who wishes to debate the real issues of this campaign to join me.' Desperate to learn who rigged the election and clear his name.",
        "background": "His running mate is Brandon Ekimatsu, a former Mitsuhama Computer Technologies executive.",
        "notes": "Dry Run: the (simulated) VR shadowrun the player characters are drugged into believing is real involves planting a Dunkelzahn-ordered surveillance device on Booth's limousine during a DeeCee fundraiser -- an operation that, notably, never actually happens to the real Booth, since the entire 'run' takes place inside a VisionQuest simulation.",
    },
    {
        "name": "General Franklin Yeats",
        "role": "Retired UCAS general running on Bug City outrage, unaware his running mate has been turned by insect spirits",
        "archetype": "Politician",
        "title": "Presidential candidate, Republican Party",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "organization": "Republican Party",
        "description": "A working-class Chicago-born UCAS Army veteran who rose to the Joint Chiefs of Staff before retiring in 2054 over budget cuts he opposed: 'If we want the United Canadian and American States to survive, we have to elect leaders who care about something beyond their own personal ambitions.' Chicago is his hometown and personal cause; he escaped internment in the Containment Zone only because he happened to be in DeeCee when the outbreak hit. Hawkish, pro-military-rebuilding, and open to reclaiming California by force.",
        "background": "Chose longtime friend Anne Penchyk, an ork former Wisconsin Representative and meta-rights advocate, as his running mate -- unaware she has deeply buried, active ties to the Desolation Angels mantis cabal inside Bug City.",
        "notes": "Casualties of War: never appears in person, but the entire adventure turns on protecting his campaign's reputation -- and Penchyk's secret -- during a supposed rescue mission into the Containment Zone.",
    },
    {
        "name": "Dunkelzahn",
        "role": "The great dragon running for UCAS president as an independent, whose VR research facility comes under terrorist siege in Dry Run",
        "archetype": "Great Dragon",
        "title": "Presidential candidate, Independent",
        "race": "Dragon",
        "gender": "Male",
        "connection": 6,
        "description": (
            "An ancient western dragon, first sighted near Denver in 2012, now one of the most "
            "recognizable beings on the planet through decades of media presence, philanthropy, and his "
            "own long-running talk show 'Wyrm Talk.' Speaks through a series of human 'interpreters' who "
            "voice his thought-speech; on live TV announcing his candidacy, he tells Holly Brighton: 'I "
            "am an ancient being, Holly. I've seen first-hand more history than many shorter-lived "
            "people have forgotten ... I do not concern myself with matters of species or race. Ask me "
            "what I am and I will tell you.' Owns VisionQuest and the Lake Louise resort in the "
            "Athabaskan Council."
        ),
        "background": (
            "Announced his independent candidacy live on 'Wyrm Talk' on March 15, 2057, pledging SIN "
            "amnesty and registration for the UCAS's SINless population and casting the megacorporations "
            "as an obstacle to, rather than an engine of, real innovation. His running mate is Boston "
            "investor Kyle Haefiner, chosen on the advice of his advisor Damien Knight."
        ),
        "notes": (
            "Dry Run: his head of security Carla Brooks unwittingly drugs runners for VisionQuest VR "
            "test scenarios; a Human Nation cell, opposed to his candidacy, seizes one such facility "
            "(near Mason City, Iowa) mid-test and threatens to destroy it and everyone in it unless he "
            "withdraws from the race. No combat statistics are given for Dunkelzahn himself -- he never "
            "appears in person during the adventure."
        ),
    },
    {
        "name": "Damien Knight",
        "role": "Ares Macrotechnology-linked advisor who brokered VisionQuest's sale to Dunkelzahn and vets his VP options",
        "archetype": "Corporate Advisor",
        "title": "Sometime advisor to Dunkelzahn on metahumanity",
        "gender": "Male",
        "connection": 3,
        "description": "A 'master manipulator' whose reasons for selling Dunkelzahn the cutting-edge VisionQuest subsidiary in 2037 have never been made public -- Shadowland speculation holds that 'Ares didn't sell off VisionQuest out of fear -- it's a sure bet Damien Knight got something more than nuyen out of the deal.'",
        "notes": "Dunkelzahn campaign background: proposed Boston investor Kyle Haefiner as Dunkelzahn's running mate, an old friend Knight trusts to be loyal to him first and the dragon second. Never appears in a scene.",
    },
    {
        "name": "Holly Brighton",
        "role": "Retired anchorwoman and Dunkelzahn's first interpreter, who returns from retirement to interview him for his candidacy announcement",
        "archetype": "Media Figure",
        "title": "Retired anchorwoman; former business partner to Dunkelzahn",
        "gender": "Female",
        "connection": 3,
        "description": "Won the twelve-hour, sixteen-minute interview that gave humanity its first real look at the Awakening after fighting off reporters from around the globe in 2012, then kept a business relationship with the dragon until her 2047 retirement. Comes out of semi-retirement to host his March 15, 2057 candidacy announcement on 'Wyrm Talk,' adjusting her own feed into the studio system with the ease of old habit.",
        "notes": "Dunkelzahn campaign background: still lives at the Lake Louise resort and wields real influence there, particularly over 'Wyrm Talk' itself, and is frequently at odds with the dragon's current interpreter Nadja Daviar.",
    },
    {
        "name": "Nadja Daviar",
        "role": "Dunkelzahn's enigmatic current interpreter, with no discoverable personal history",
        "archetype": "Political Aide",
        "title": "Interpreter and voice to Dunkelzahn",
        "race": "Elf",
        "gender": "Female",
        "nationality": "Eastern European",
        "connection": 3,
        "description": "A raven-haired elven beauty with a mesmerizing voice who has served the dragon since 2039 and 'reigns over the Lake Louise resort like a queen'; someone has 'taken great pains to erase any traces of her background, and done a damn fine job of it, too' -- persistent rumor links her to Polish intelligence circles, unconfirmed.",
        "notes": "Dunkelzahn campaign background: provides Carla Brooks's video-statement credentials in Dry Run so the runners can verify Brooks actually works for Dunkelzahn. Rival of Holly Brighton for influence within the dragon's circle.",
    },
    {
        "name": "John Timmons",
        "role": "Dunkelzahn's second interpreter, assassinated in 2022 and instantly avenged by the dragon in front of witnesses",
        "archetype": "Media Figure",
        "title": "Former interpreter to Dunkelzahn (deceased)",
        "gender": "Male",
        "connection": 1,
        "description": "A young Denver resident who agreed to 'speak' for the dragon, translating his thought-voice into words microphones could record; became a major force in the post-Awakened Protestant revival, preaching tolerance against a tide of religious reactionism.",
        "background": "Killed in 2022 by an anti-metahuman-linked assassin who made the mistake of firing in Dunkelzahn's presence; witnesses reported the dragon reduced the gunman 'to his component flaring atoms' with a glance. Critics still ask why, with all his power, Dunkelzahn could not have stopped the shooting before it happened; the dragon has never commented.",
        "notes": "Dunkelzahn campaign background/lore only; dead decades before the adventure, no scenes.",
    },
    {
        "name": "Teri Ann Ribeiro",
        "role": "Dunkelzahn's third interpreter, who parlayed the role into an acting career and keeps a tell-all manuscript as insurance",
        "archetype": "Media Figure",
        "title": "Former interpreter to Dunkelzahn",
        "gender": "Female",
        "connection": 1,
        "description": "A perky, personable neophyte reporter when the dragon 'discovered' her in 2028; popular enough as his voice to launch a successful, if not critically noteworthy, acting career in 2039.",
        "notes": "Dunkelzahn campaign background: has repeatedly refused huge sums of money to make a tell-all documentary about her year with the dragon, but reportedly keeps a manuscript on the subject as insurance -- 'if she dies under mysterious circumstances, it goes public.' Never appears in a scene.",
    },
    {
        "name": "Raze",
        "role": "Razorboy street samurai in the 'Strange Bedfellows' framing prologue, who burns down Brackhaven's original campaign HQ",
        "archetype": "Street Samurai",
        "title": None,
        "gender": "Male",
        "connection": 1,
        "description": "Distrusts magic -- prefers 'things you can see and touch' -- and covers a room with an HK slung like it weighs nothing, flash-bangs at the ready. Levels his smartgun on a rival mage without flinching from her laser sight and, watching Brackhaven's tower burn behind them, delivers the line the whole book takes its cue from: 'Politics makes strange bedfellows.'",
        "notes": "Strange Bedfellows (framing prologue only): breaks into Kenneth Brackhaven's Seattle campaign HQ for data with Riff and Spook, crosses paths with an unnamed arsonist mage sent to burn the place down, and strikes an uneasy truce with her rather than fight two-front. No stats given; illustrative color for the book's tone, not meant to recur.",
    },
    {
        "name": "Riff",
        "role": "Combat mage in the 'Strange Bedfellows' framing prologue, whose fire-elemental-summoning rival nearly kills him",
        "archetype": "Combat Mage",
        "title": None,
        "gender": "Male",
        "connection": 1,
        "description": "Casts a detection spell to scout for intruders and, cornered with a gun to his neck by a rival mage, keeps his composure enough to quietly ward Raze against whatever she might throw -- even as a two-meter fire elemental coalesces at her shoulder and the heat starts a sweat rolling down his back.",
        "notes": "Strange Bedfellows (framing prologue only): the team's mage on the Brackhaven HQ data-theft job; no stats given, illustrative color only.",
    },
    {
        "name": "Spook",
        "role": "Decker in the 'Strange Bedfellows' framing prologue, who cracks Brackhaven's files under fire",
        "archetype": "Decker",
        "title": None,
        "gender": "Male",
        "connection": 1,
        "description": "Keeps working the keys through a room-clearing firefight and a Lone Star raid -- 'you can't make this kind of stuff happen any faster, chum' -- and gets the last word as the team roars off on their bikes watching Brackhaven's tower burn: 'Now that's what I call a political statement.'",
        "notes": "Strange Bedfellows (framing prologue only): downloads the stolen data off Brackhaven's system while Raze and Riff cover the room; no stats given, illustrative color only.",
    },
]

ORG_UPDATES = {
    "Humanis Policlub": {
        "notes_append": (
            "Super Tuesday (2057 campaign): Karl Brackhaven -- the Central Seattle chapter president "
            "introduced in Peacekeeper -- secretly runs his nephew Kenneth Brackhaven's Archconservative "
            "presidential campaign and will kill to keep the family's true history buried (Ghost Story). "
            "The militant splinter cell Human Nation recruits from Humanis's more tactically violent "
            "members and, opposed to Dunkelzahn's candidacy, seizes and threatens to destroy one of his "
            "VisionQuest facilities (Dry Run)."
        ),
        "allies_add": ["Human Nation"],
    },
    "Aztechnology": {
        "notes_append": (
            "Super Tuesday (Strange Attraction): sent the assassin Belladonna to recover a stolen "
            "orichalcum talisman coveted by Tir Tairngire and the Illuminates of the New Dawn, sniping "
            "at the runners and converging on the final handoff."
        ),
    },
    "Tir Tairngire": {
        "notes_append": (
            "Super Tuesday (Strange Attraction): the Council of Princes' elite adept squad, the Tir "
            "Ghosts, hunted a stolen orichalcum talisman from Portland to Seattle, killing the "
            "Illuminates of the New Dawn's Portland contact Birch Kirby for information and pursuing "
            "the runners through the city under agent Speren Silverblade."
        ),
    },
    "TerraFirst!": {
        "notes_append": (
            "Super Tuesday (Political Poison): years before the campaign, a TerraFirst! cell sabotaged "
            "a Hawkshorne Chemical plant on Arthur Vogel's secret orders; the sole survivor, badly "
            "burned elf Alan Riv, became a deranged Toxic Dog shaman bent on killing Vogel. If the "
            "runners stop Riv's rally attack, TerraFirst! and 'nearly every other environmental "
            "terrorist organization' reach out to recruit them afterward."
        ),
    },
    "Ares Macrotechnology": {
        "notes_append": "Super Tuesday (Dry Run background): sold VisionQuest, its cutting-edge VR subsidiary, to Dunkelzahn in 2037, brokered by advisor Damien Knight for reasons never made public.",
    },
    "Mitsuhama Computer Technologies": {
        "notes_append": "Super Tuesday (candidate bios): former executive Brandon Ekimatsu is James Booth's vice-presidential running mate on the Technocratic ticket; widely seen as a corporate lapdog by rival campaigns.",
    },
    "Fuchi Industrial Electronics": {
        "notes_append": "Super Tuesday (candidate bios): former New York City 'resources adjuster' William Ager, Kenneth Brackhaven's Archconservative running mate, built his shadow-hiring career at Fuchi's Rotten Apple branch before his family was displaced by the Tir Tairngire invasion of Northern California.",
    },
}

LOC_UPDATES = {
    "Underworld 93": {
        "notes_append": "Super Tuesday (Strange Attraction): the fixer Bono, on the run from both the Tir Ghosts and the Illuminates of the New Dawn, tries to meet the runners here; the club's troll bouncer Newt is on the door as always.",
    },
    "The Partyzone": {
        "notes_append": (
            "Super Tuesday (Ghost Story): the fixer Walks-With-Yen meets contacts here at 1 a.m., "
            "amid gangers, chip-heads, and street trash partying to portable-amp shag metal, before "
            "taking them to Dr. Christina Falt's clinic. DISCREPANCY: this book places the Partyzone "
            "'in an area of the Redmond Barrens,' not South Tacoma (Dark Angel) -- treated as the same "
            "recurring floating rave/neutral ground rather than a second Partyzone."
        ),
    },
    "Matchstick's": {
        "notes_append": "Super Tuesday (Ghost Story): Karl Brackhaven's intermediary 'Mr. Smith' meets investigating runners here to buy off their silence; doorman Saint John gives them the usual once-over on the way in.",
    },
    "Seattle General Hospital": {
        "notes_append": (
            "Super Tuesday (Ghost Story): the site of Kenny Brackhaven's 2023 murder at his father's "
            "hands during the goblinization crisis; his ghost still haunts the wards, seeking only to "
            "have the truth of his death told."
        ),
    },
    "The Kingdome": {
        "notes_append": (
            "Super Tuesday (Political Poison, 2057): Arthur Vogel's climactic campaign rally, and Alan "
            "Riv's attempted mass poisoning of the crowd, are staged at what this book calls 'the "
            "Superdome' -- almost certainly this venue under another name, since no other Seattle dome "
            "stadium appears anywhere else in the setting's canon and the book never explains a "
            "renaming or a second stadium. Flagged as a discrepancy rather than treated as a separate "
            "location."
        ),
    },
    "The Space Needle": {
        "notes_append": "Super Tuesday (Dry Run): Carla Brooks recruits the runners for what they believe is a real DeeCee shadowrun over dinner at 'the Eye of the Needle,' a private-room restaurant here -- the meeting is genuine even though the job itself turns out to be a VR test.",
    },
}

NPC_UPDATES = {
    "Saint John": {
        "notes_append": "Super Tuesday (Ghost Story, 2057): still working the door at Matchstick's; gives investigating runners the same curt once-over he gives everyone.",
    },
    "Newt": {
        "notes_append": "Super Tuesday (Strange Attraction, 2057): still bouncing at Underworld 93; exchanges nods with runners known to the club.",
    },
    "Karl Brackhaven": {
        "background_append": (
            "Ghost Story: the only living person besides his late brother Charles who knows the truth: "
            "the real Kenneth Brackhaven, an ork, was murdered by his own father Charles in 2023 -- "
            "ashamed of his goblinized son and unwilling to let it damage the family's image -- and "
            "replaced with a conditioned SINless double. Karl considers the killing a 'mercy killing' "
            "and feels no guilt; he helped raise the substitute 'Kenny' to share his own hatred of "
            "metahumans, giving Humanis its first real shot at a UCAS president who genuinely believes "
            "in its cause."
        ),
        "notes_append": (
            "Ghost Story (this book calls his chapter title 'Seattle chapter president'; Peacekeeper's "
            "existing row has him as Central Seattle chapter president -- treated as the same office). "
            "Also runs Kenneth Brackhaven's Seattle presidential campaign out of its downtown "
            "headquarters. Laughs off threats with nerves of steel -- 'Frag them before they frag you, "
            "that's basic politics' -- and when a runner asks why he hired metahumans for a job in the "
            "first place, only smiles: 'My dear, because you're the most expendable, of course.' When "
            "investigating runners get too close to the truth, first tries to buy them off through an "
            "intermediary ('Mr. Smith,' 5,000-10,000 nuyen per runner via blind escrow at Matchstick's), "
            "then hires the hitman Fletcher Quinn to kill them and silence the nurse Karen Johanssen. "
            "Depending on the runners' final choice, becomes either a lifelong enemy (if exposed), a "
            "blackmail victim plotting their deaths (if blackmailed), or an assassin who reneges on any "
            "deal (if the runners simply hand back the evidence). Stats (this book): B4 Q3 S4 I5 W4 C5 "
            "Ess5.2 Reaction4, Init 4+1D6, TR/PR 2/2; Administration 5, Car 3, Etiquette (Corporate) 5 / "
            "(Media) 3 / (Political) 4, Leadership 3, Negotiation 5; datajack, display link, headware "
            "memory (50 Mp)."
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
Two systems appear across the book; neither should be built as a live host.

**1. Seattle General Hospital records system** (Ghost Story, p.82). Orange 3/8/8/9/6/10, Trace 5.
Public patient search; searching "Kenny"/"Kenneth" plus the room number where the ghost first
appeared turns up Kenneth Brackhaven's falsified 2023 record (attending physician listed as "Dr. C.
Falt," the rest of the record "lost in the Crash of '29").

**2. The Secret Service DeeCee Matrix system** (Dry Run, pp.106-108) -- **this system is not real**.
It exists only inside VisionQuest's VR test simulation, built to let a decker character "hack" a
fully convincing but entirely fictional target while unknowingly wired into a VR pod. Documented here
for GM reference only, in case a table plays through Dry Run's decking scene as written:

| Host | Function | Rating | Notable IC |
|---|---|---|---|
| A (public) | VIP scheduling, day-to-day office systems | Blue-4/8/10/9/9/8 | Probe-5; Trap Probe-1 (Blaster-7); government decker in 2D3 turns after step 27 |
| B (chokepoint) | Security gate between Host A and Host C; no data of its own | Red-01/14/05/07/16/18 | Tar Baby-8; Trap Trace-10 (Killer-8); Expert Constructs; Cascading Black IC-7; government decker in 1D6 turns |
| C (paydata) | Motor-pool routing, security assignments, VIP itineraries | Green-10/17/18/13/15/14 | Trap Probe-10 (Killer-11); Party IC (Tar Pit-4, Killer-10, Marker-6); Cascading Psychotropic Black IC-9 (Cyberphobia); government decker in 1D3 turns |

Any damage a decker takes here is simulated, not real -- a "killed" decker is only rendered
unconscious within the VR feed.
"""

NOT_BUILT = """
- **Tanner, Marley, Half-Trak** -- the Dry Run prologue's prior (unrelated) VisionQuest test-run
  shadowrunner team, captured and drugged before the player characters' own run even begins;
  illustrative color establishing that this has happened before, no stats or lasting role.
- **The VIP garage / DeeCee heist infrastructure** (Off and Running, pp.104-109) -- guard rosters,
  wards, and the fictional Secret Service Matrix system (see MATRIX_HOSTS) are all part of the VR
  simulation, not a real Washington DC location; not eligible for a LOCATION row.
- **Interim President Barry Jo Pritchard, President Thomas Steele** -- campaign-backdrop figures,
  name-dropped only for the 2056 rigged-election scandal that triggered this emergency race.
- **Kyle Haefiner** -- Dunkelzahn's running mate, a Boston investor and philanthropist widowed when
  his decker wife Alice was killed by the Crash Virus decades ago; named and given a paragraph of
  bio color but never appears in a scene, folded into Dunkelzahn's own notes.
- **Brandon Ekimatsu, William Ager** -- Booth's and Brackhaven's running mates; enough real color to
  be tempting (Ekimatsu the ex-Mitsuhama moderate, Ager the anti-elf ex-Fuchi 'resources adjuster'
  whose daughter Clarice died in the Tir invasion of Northern California) but no scenes of their own,
  folded into their running mates' NPC notes and the relevant ORG_UPDATES.
- **"The Macmillan Group" panel and CBC News Service, One Nation Under God's pamphleteers** --
  in-world media texture (a talk-show panel debating the race, an anti-Hernandez propaganda group
  already given a thin ORG row for its pamphlet) with no further plot role beyond quotable color.
"""

PLAY_NOTES = """
- The five adventures are fully independent -- run any subset in any order, or thread all five
  through a single campaign as the runners get pulled deeper into the 2057 election's shadow economy.
  Nothing in one adventure depends on outcomes from another.
- Political Poison rewards fast improvisation: give the runners almost no time to plan once Silver's
  poisoning starts the chase, and let the Reservoir Dogs fight hand Riv's lair location to the players
  rather than making them dig for it.
- Strange Attraction runs best as a genuine mystery for the players, not just the characters -- keep
  the flashback triggers subtle and let three-way tension between the Ghosts, Aztechnology, and the
  Illuminates do the work of keeping the runners guessing who (if anyone) they can trust.
- Casualties of War needs the Bug City sourcebook on hand for the Wall crossing and the Volk; the
  emotional core is the ghouls of Ghoultown being more trustworthy than the "client" who hired the
  runners in the first place.
- Ghost Story works whether or not a PC ever sets foot in a hospital -- reroute the haunting to an
  NPC contact's bedside if none of the party is laid up, and lean on the flashback/dream imagery hard
  before the ghost ever "speaks."
- Dry Run's VR framing is a one-time trick: once a table has seen it, the "glitches" (idealized
  colors, a decker's unexplained interface lag, a chronic pain that doesn't bother a character today)
  become obvious tells. Use the neural-feedback dice-pool nudge sparingly and keep every modification
  secret from the players.
- Across all five: none of the six candidates ever needs stats. Keep them as offstage political
  weather -- the runners' actual antagonists are always the operatives, cults, and cabals working in
  each candidate's name, not the candidates themselves.
"""
