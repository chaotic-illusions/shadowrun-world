# Eye Witness (FASA 7316, 1994, Mike Nystul) -- campaign order #17. Downtown, Redmond, Bellevue, the
# Puyallup Barrens, Renton and the Seattle sewers, 2055: the introduction says "The year is 2055" and
# the Corporate Shadowfiles profile of Multitech is dated January 1, 2055. The three handouts (Neil's
# letter, the blueprint, Vanian's business card) carry no date, so no month is given.
# Editing inconsistencies noted in the affected rows: the holding company is "Berkely Management" in
# the plot synopsis (p.7) and "Berkley Management" everywhere else (pp.50-51, 65); the Iron Legion
# massacre is "scant hours ago" at the blitz club and "last night" in Legwork, yet Emma has already
# been looping her simsense for 48 hours when the team reaches Hope; Neil was shot "last night" but the
# Lone Star troopers at the intersection have been "on the scene for six hours"; the book calls the
# city's chief executive "Mayor Schultz" (the campaign DB, following the earlier handouts, has
# Governor Schultz); Adam Shepherd's sunlight allergy is Mild on the cast page and Moderate for every
# other ghoul; Vanian has Essence 6 and Wired Reflexes 2; Rico's skill list is a copy of Baxter
# Attaway's; the Hammond Necroplex is a stone "pyramid" with an "adjoining corporate tower" in the
# encounter and a "twelve-story building" in Legwork; Vanian's shop is in "the nasty part of town"
# and, per Legwork, "in Redmond"; Shepherd is an "investment broker born to privilege" (synopsis) and
# "heir to a corp fortune" (cast page). OCR: the cast-page columns are jumbled (Alpha Blue's attribute
# block precedes her header, Vanian's and Shepherd's gear columns are merged, Clean Steve's gear list
# is cut off), Vanian is "Vanlan" and Neil is "Nell" in places, and the Karma award for the bomb
# reads "1".
# Source text: docs/Adventures/text/SR2-eyewitness.txt (74 OCR pages; book page N = OCR page N+1).
# ASCII only (pre-commit hook).

ADVENTURE = "Eye Witness"
ORDER = 17
SOURCE = "SR2-eyewitness.pdf, pp. 4-71"
YEAR = "2055"

SYNOPSIS = """
The meet is in the back room of a funeral parlor, among the caskets. The Ms. Johnson is **Erin
Scott** -- the street samurai **Alpha Blue** -- dark-haired, in a blue leather bodysuit with chrome
studs and chains, a Remington Roomsweeper resting on a rosewood casket lid. Last night a sniper put
explosive rounds through the roof of her brother **Neil Scott's** Jackrabbit at the corner of Leopold
and Loeb. This morning she got his last e-mail: a copy of a stolen optical-chip blueprint, the
business card of the tech fence **"Rat" Vanian** who paid him to analyze it, and Neil's conclusion
that the print is the work of hotshot designer **Dutch Donovan** of **Multitech** and hides an
intentional shortcut that makes the chip cheap and useless. She plays it totally straight: find out
how Vanian got the print, get her enough evidence to take Multitech down, and beat Lone Star to it.
Then she vanishes, checking in by vidphone.

What nobody at the meet knows: the blueprint came out of a camera cybereye. Multitech quality
inspector **Griffin Moore** photographed every print of the deliberately flawed MPCP chip in the R&D
datastore, was run off a cloverleaf on the way home, and was laid to rest in the **Hammond
Necroplex** -- whose bankrupt director **Thaddeus Sinclair** has been selling his corpses down a
sewer entrance to a patron called **Berkley Management**. The patron is **Adam Shepherd**, born Eric
Steward, a sane ghoul who bought the waste company **Agrippa and Associates**, replaced its payroll
with unpaid ghouls, and built them a walled Retreat in Puyallup. Moore fed a family of ghouls for a
week. Then the **Iron Legion** went ghoul-hunting for bail money, a Legionnaire called **Breaker**
cut the eye out of Moore's skull with a penknife and sold it to Vanian, Vanian pulled the last image
from its memory, and Shepherd's technician pried the rest of the prints from the eye socket. Shepherd
has every blueprint but one, and wants the set to blackmail his way onto Multitech's board; he has
hired the cyber-free assassin **Clean Steve** to get it and to kill a Legionnaire for every dead
ghoul. Meanwhile the corpses Sinclair defiled woke a free tomb spirit, **Gallowgrey**, who killed
thirteen people on the night shift -- the "gas leak" of the Hammond Massacre.

The runners are always one step behind Multitech's cleanup crew: Neil's lab in **Gibson Hall** has a
cigar-box bomb on a gas line with twenty minutes on the clock, Vanian's storefront holds two executed
assistants and a hidden envelope with his home address, Donovan's house in the company suburb of
**Smallville** is a trap with snipers and combat mages, and a Multitech snatch team hits Vanian's
squalid suite in the **Shady Hill Apartments** just after the team gets the eye out of him. The eye's
serial number, the surviving Legionnaires at the **Route 66** blitz club in **Brighton Mall** (until
Lone Star gasses it), Breaker's simsense-comatose girlfriend **Emma** and her talis cat in the
Puyallup slum called **Hope**, the **Lost Boys** and the blind mage **Alegheri** in the sewers, the
neckties in the ghoul nests, and the empty tombs and the accounting files of the Necroplex all point
the same way: to Shepherd's Retreat, the vine-covered compound of Agrippa and Associates, its cybered
ghoul bodyguards and its forty-odd flesh-eaters. Shepherd is disarmingly polite and will not give up
the prints unless his people are threatened -- or exposed. Alpha Blue takes the complete set, pays,
and her vengeance on Multitech is private.
"""

TIMELINE = """
- **2021** -- Eric Steward, golden-boy investment broker, goblinizes into a ghoul; years feral in the
  sewers, then sanity, then wealth. **Early 2050s** -- as Adam Shepherd / Berkley Management he buys
  the failing Agrippa and Associates, replaces the workforce with ghouls, opens the Retreat, and buys
  the Hammond Necroplex's corpses (and its director's simporn) for the ghouls' table.
- **Several weeks ago** -- Griffin Moore reports the flawed MPCP chip, is brushed off, decks the R&D
  datastore, photographs every print with his cybereye, and dies on a cloverleaf; memorial at the
  Ecumenical Pavilion, interment at Hammond, body butchered into the sewers. A family of four ghouls
  eats for a week. Griffin's file at Multitech is now a black-IC dummy.
- **Three weeks ago** -- Gallowgrey slaughters thirteen Necroplex staff on four floors; the "chemical
  accident" story goes out and the Necroplex closes "for repairs"; Sinclair stops selling and hides.
- **About two weeks ago** -- Lone Star jails three Iron Legionnaires for black-market BTLs; the gang
  hunts ghouls for bail; Breaker takes the eye; Vanian buys it, prints the one image in its
  short-term memory and sends it to Neil. **Three days later** -- Shepherd's team cleans the tunnel
  with a flamethrower and takes the memory chip out of Moore's skull. Shepherd hires Clean Steve.
- **Several days ago** -- Neil identifies Donovan's design flourishes and confronts him; Donovan
  reports it and is flown to Shanghai; troubleshooters move into Smallville.
- **Last night** -- a sniper with an FN HAR kills Neil at Leopold and Loeb; the cleanup crew searches
  his lab and leaves a bomb, then hits Vanian's shop and kills Lou and Graham while Vanian watches on
  the video feed from home. Clean Steve corners the Iron Legion in a blind alley, tortures Breaker to
  death and kills most of the gang. (Emma, told of Breaker's death, has been looping her simsense for
  two days by the time the team finds her -- the book's clocks do not agree.)
- **Today** -- the funeral-parlor meet; Gibson Hall (twenty minutes); Vanian's shop and Clean Steve;
  Shady Hill and the snatch team; tonight the Route 66 blitz at Brighton Mall and Lone Star's tear
  gas. **Following days** -- Hope, the sewers, the Necroplex, Club Nosferatu, the Retreat. Lone
  Star's ballistics and the sniper's saliva will name the shooter "in days".
"""

ORGS = [
    {
        "name": "Multitech International",
        "org_type": "corporation (custom microtronics)",
        "tier": 4,
        "headquarters": "Shanghai (home office); Multitech Design division in Bellevue, Seattle",
        "summary": "Private Shanghai-based custom-chip house that shortcut a military MPCP design and is killing everyone who saw the blueprints",
        "description": (
            "A prestigious, privately held design-and-development house that builds and designs custom, "
            "high-performance, high-cost computer chips for the unique or proprietary systems of some "
            "of the biggest megacorps -- short runs of high-tech components for Henderson Multicom, "
            "Fuchi, Magnuson and dozens of regular clients. Home office Shanghai; President/CEO Jonathon "
            "Ki Won; Chairman of the Board Sir Peter Mathews. Its principal division, Multitech "
            "Design/Seattle UCAS under Maximilian Stern, does custom-chip design and production for the "
            "microtronic industry from an innocuous old stone building in Bellevue. Extensive R&D and "
            "fiscal ties to most of the microtronic megacorps; physical and Matrix security 'considered "
            "extremely high, though undocumented'. A hard, demanding company that rewards those who do "
            "not frag up. Corporate Shadowfiles profile (January 1, 2055): Net Rating 59; interests "
            "Computer Engineering 5, Computer Science 8, Consumer Goods 2, Cybernetics 3, Military "
            "Technology 6; Fiscal 8, Intelligence 7, Management 6, Reputation 6, Security 8 (Magic 5, "
            "Matrix 8, Physical 10); Military none documented."
        ),
        "leadership": [
            {"name": "Jonathon Ki Won", "title": "President/CEO (Shanghai)", "notes": None},
            {"name": "Sir Peter Mathews", "title": "Chairman of the Board", "notes": None},
            {"name": "Maximilian Stern", "title": "Division Head, Multitech Design/Seattle", "notes": "Third-generation corp exec; runs the Bellevue branch."},
            {"name": "Dutch Donovan", "title": "Senior processor/chip designer (transferred to Shanghai)", "notes": "Designed the flawed MPCP chip; now drawing the corrected one in Shanghai's DS-5."},
            {"name": "Griffin Moore", "title": "Quality control inspector (deceased)", "notes": "Wrote the book on quality control; photographed the prints; run off a cloverleaf."},
        ],
        "notes": (
            "The fraud: the optical chip for the MPCP of a new military-grade cyberdeck carries an "
            "intentional reroute around a noncritical subprocessing node -- cheaper, faster to program, "
            "and virtually useless. The cleanup crew (coordinators with Wired 2, four-man troubleshooter "
            "squads, snipers, two combat mages with Hellblast foci, a Morgenstern Security backup "
            "platoon, two Major League deckers online round the clock) has already erased every scrap of "
            "evidence in Bellevue; the only surviving copies are Griffin Moore's photographs (Shepherd "
            "has all but one; Alpha Blue has the last) and Donovan's corrected designs in Shanghai. "
            "Multitech would rather learn who has the prints than simply kill another loose end -- the "
            "Smallville ringer and the Shady Hill snatch team question before they shoot; survivors go "
            "to Bellevue for interrogation and come round with a new scar, a cortex bomb and a new boss. "
            "Home office is nervous. Neil's half-finished 'BP Botch Bypass' attack program, completed "
            "with the full prints, is a weapon against any MPCP built on the flawed chip. Legwork: "
            "corporate contact or Fixer TN 4, Shadowland 5 (20 hours); SeaSource carries the public "
            "profile for a download fee."
        ),
        "allies": ["Morgenstern Security", "Fuchi Industrial Electronics"],
        "enemies": ["Agrippa and Associates"],
    },
    {
        "name": "Morgenstern Security",
        "org_type": "corporate security subsidiary",
        "tier": 2,
        "headquarters": "Smallville corporate housing complex (Multitech)",
        "summary": "Wholly-owned Multitech security subsidiary that polices the Smallville company suburb",
        "description": (
            "A wholly-owned Multitech subsidiary with a special arrangement to guard Smallville, the "
            "suburban housing development Multitech and its subsidiaries own outright. Eight private "
            "security guards are on call for the Smallville coordinator when the company troubleshooters "
            "cannot finish a stand-up fight on their own."
        ),
        "notes": (
            "Guards (8): B3 Q5 S5 C6 I5 W6 E6 R5 (as printed), Init 5+1D6, Threat/Professional 3/2; "
            "Armed Combat 3, Etiquette (Corporate/Street) 3, Firearms 4, Unarmed 3, Police Procedures 4; "
            "Ares Predator with laser, armor vest 5/3, club, plastic restraints. Rent-a-cops with police "
            "training -- the corp's own badge inside the company fence."
        ),
        "allies": ["Multitech International"],
    },
    {
        "name": "Agrippa and Associates",
        "org_type": "corporation (waste management)",
        "tier": 3,
        "headquarters": "Walled compound in a Puyallup industrial complex",
        "summary": "Seattle's biggest waste-removal contractor, secretly run by a ghoul CEO with an unpaid ghoul workforce and a walled ghoul Retreat",
        "description": (
            "A privately held, Puyallup-based waste management and removal company holding most of the "
            "metroplex's waste contracts and a hefty chunk of city and private business. It was showing "
            "significant losses in the early 2050s until a phony investment group, Berkley Management, "
            "bought it out and any serious rival bidder withdrew early, one way or another. New CEO Adam "
            "Shepherd -- the ghoul Eric Steward -- phased out most of the human employees and secretly "
            "replaced them with ghouls who receive no pay, and Agrippa showed impressive growth for the "
            "first time in years. The street notices only that the company is 'very mechanized': low "
            "payroll, lots of output, a job applicant laughed out of the door, and a place in Puyallup "
            "that nobody ever goes in or out of -- the employees live there. Shepherd's staggering "
            "profits pay for a retreat in the industrial park where ghouls can live without bounty "
            "hunters, for scientists who solved the ghoul/cyberware interface with sedatives and modified "
            "skillwires, and for the Hammond Necroplex's corpses."
        ),
        "leadership": [
            {"name": "Adam Shepherd", "title": "CEO (born Eric Steward)", "notes": "Sane ghoul; wants a Multitech board seat by blackmail."},
            {"name": "Nelson", "title": "Ghoul mage; successor-designate as director of Agrippa and master of the Retreat", "notes": None},
            {"name": "Gog and Magog", "title": "Shepherd's cybered ghoul bodyguards", "notes": "Meat puppets on skillwires."},
        ],
        "notes": (
            "Shepherd's technician recovered the camera memory chip from Griffin Moore's skull three days "
            "after the Iron Legion raid: every optical-chip blueprint except the final one that stayed in "
            "the eye's short-term memory. The prints sit in a safe-deposit box; the key is hidden in the "
            "kitchen of the compound's main building. Shepherd will offer up to 50,000 nuyen (Clean Steve "
            "opens at 5,000) for the runners' copy, and if the team refuses Alpha Blue he will hire them "
            "himself -- he cares nothing for Neil Scott. He needs Multitech alive and prosperous; Alpha "
            "Blue needs it dead. Deals with the sewers' other denizens and restricts his ghouls to a "
            "designated hunting ground. Seattle pays 100 nuyen per male ghoul and 150 per female; about "
            "30 percent of the compound is female -- give the runners the figures and let them think. "
            "Karma: Alpha Blue gets the full set 6; Alpha Blue and Shepherd reach a deal 8. Runners who "
            "sell Alpha Blue out to Shepherd never get another decent job in Seattle. Legwork: City "
            "Official or organized-crime contact TN 4, Shadowland 4 (12 hours)."
        ),
        "allies": ["Berkley Management"],
        "enemies": ["Iron Legion", "Multitech International"],
    },
    {
        "name": "Berkley Management",
        "org_type": "holding company (front)",
        "tier": 2,
        "headquarters": "Seattle (address not given)",
        "summary": "Real-estate holding company that is Adam Shepherd's front: bought Agrippa, pays the Necroplex director 50,000 nuyen at a time",
        "description": (
            "A real-estate management and holding company nobody can say much about -- 'couldn't even "
            "say what they manage or hold'. Finance and city contacts know it as the real-estate holder "
            "for Agrippa and Associates, the waste-removal company that does a lot of work for the city. "
            "It is the phony investment group through which the ghoul Eric Steward, as Adam Shepherd, bid "
            "for Agrippa; its regular 50,000-nuyen payments to Thaddeus Sinclair's personal account are "
            "buried in the Hammond Necroplex accounting datastore (DS-6), and Sinclair knows his silent "
            "partner by no other name."
        ),
        "notes": (
            "Spelled 'Berkely' in the plot synopsis and 'Berkley' everywhere else; the book's own "
            "records use Berkley. Legwork: City Official, corporate or finance contact TN 5, Shadowland 4 "
            "(18 hours). The paper trail Berkley -> Agrippa -> Puyallup is the clean way from the "
            "Necroplex to the Retreat."
        ),
        "allies": ["Agrippa and Associates"],
    },
    {
        "name": "Hammond Group",
        "org_type": "corporation (mortuary / necroplex)",
        "tier": 2,
        "headquarters": "Hammond Necroplex, Renton",
        "summary": "Operator of the Hammond Necroplex; near-bankrupt, propped up by Shepherd's loans, its night staff slaughtered by a tomb spirit three weeks ago",
        "description": (
            "Founded by businessman Jasper Hammond, who opened one of the first necroplexes when "
            "skyrocketing land values put burial beyond the average citizen and turned alternative "
            "interment into a necessary commodity; the vast crypt-and-crematorium in Renton turned a "
            "pretty profit for years and set the pattern for the industry. In even worse financial "
            "condition than Agrippa, the company took an anonymous patron's loans and cash, upgraded its "
            "computer security with the money, and its Director of Operations, Thaddeus Sinclair, began "
            "dumping bodies slated for entombment or cremation into a nearby sewer entrance. Three weeks "
            "ago thirteen employees died on four floors in one night; a surviving PR wizboy called it a "
            "chemical accident (Legwork: a gas leak) and the company spread enough nuyen that neither the "
            "press nor the authorities asked awkward questions. The Necroplex is closed 'for repairs' and "
            "the remaining staff will not come to work."
        ),
        "leadership": [
            {"name": "Jasper Hammond", "title": "Founder", "notes": "Built the necroplex without consulting a magician."},
            {"name": "Thaddeus Sinclair", "title": "Director of Operations", "notes": "Sold the corpses; blackmailed with his own simporn; hiding in his office."},
            {"name": "Eric Lane", "title": "Security Chief", "notes": "Ex-Lone Star (three-year hitch), coordinates from his office."},
        ],
        "notes": (
            "One in three recent tombs is empty, Griffin Moore's among them; the interment records (DS-4) "
            "and the Berkley payments (DS-6) are enough for legal action or blackmail. A mediocre security "
            "force compensated for by a costly Lone Star contract. Legwork: SeaSource lists a mortuary, "
            "crematorium and interment site in Renton with a gas-leak article; the Hammond Massacre (City "
            "Official, Media Producer or Street Cop TN 4, Shadowland 5, 20 hours): corpses 'pale as "
            "ghosts', thirteen dead on four floors of a twelve-story building, 'a bit of magic about the "
            "place, and whatever killed those people was definitely not human'."
        ),
    },
    {
        "name": "Iron Legion",
        "org_type": "street gang",
        "tier": 1,
        "headquarters": "Roving; hangs out wherever the Route 66 blitz club sets up",
        "summary": "Notoriously violent gang in blue warpaint and chain harnesses that hunts ghouls for the city bounty -- and was massacred by Clean Steve for it",
        "description": (
            "Lowlife thugs with a jones for guns and cyberware but no cred to jack the knife: castoff "
            "shells and vacuform cosmetics with their synthleathers, blue warpaint and chain harnesses, "
            "and gruesome tattoos that keep score of the ghouls they have bagged. For years Seattle has "
            "paid a bounty on ghouls, and the Legion made a game of it. When Lone Star picked up three "
            "members for peddling black-market BTLs, the gang went to the sewers for bail money and cut a "
            "bloody swath through the first ghoul enclave it found, taking whatever salvage was lying "
            "around -- including a dead man's cybereye. The gang moves with the Route 66 blitz club."
        ),
        "leadership": [
            {"name": "Overdrive", "title": "Lieutenant (since the massacre)", "notes": "A follower who took the job hours ago."},
            {"name": "Breaker", "title": "Soldier (deceased)", "notes": "Cut the eye out of Griffin Moore's skull; tortured to death by Clean Steve."},
        ],
        "notes": (
            "Last night Clean Steve cornered the Legion in a blind alley and geeked a ganger for every "
            "dead ghoul; Breaker was tortured to death. Six survivors keep an oddly low profile by Mister "
            "Crunchy in the Brighton Mall food court. Punks (5): B4 Q4 S4 C2 I2 W4 E6 R3, Init 3+1D6, "
            "Threat/Professional 3/3; Armed Combat 3, Etiquette (Street) 3, Firearms 3; Browning "
            "Max-Power, club, synthleather 0/1. Give them the respect they think they deserve and wait; "
            "strong-arming them buys a bullet in the temple. They know nothing of the eye but know "
            "Breaker's squeeze Emma lives in Hope. Legwork: Gang Boss, Street Cop or Troll Bouncer TN 5, "
            "Shadowland 5 (20 hours); a contact who names Clean Steve may want cash up front -- if Steve "
            "hears the contact turned rat, he may ice him."
        ),
        "enemies": ["Agrippa and Associates", "Lone Star Security"],
    },
    {
        "name": "Lost Boys",
        "org_type": "sewer gang",
        "tier": 1,
        "headquarters": "Alegheri's cistern chamber, Seattle sewers",
        "summary": "Eight homeless gutterpunks living in the sewers under the blind mage Alegheri, their 'Teacher'",
        "description": (
            "A rag-tag underground gang of sorts -- homeless gutterpunks who took refuge from a society "
            "that rejected them in the concrete bowels under the sprawl. They live off the waste of the "
            "surface world, raiding dumpsters near their sewer entrances, and have learned to rise above "
            "the dangers that lurk down there. No magic, no cyberware, nothing more lethal than a couple "
            "of Ares Predators low on ammo. They gather until all eight are present before they dare "
            "confront strangers, and then they only want to scare them off. Long isolated, they have no "
            "idea how to handle a social interaction: they pick a spokesman who uses as few words as he "
            "can and stutters when excited. Many feel an almost religious awe of the blind old mage they "
            "call Teacher."
        ),
        "leadership": [
            {"name": "Alegheri", "title": "'Teacher' -- blind mage, born Gideon Alexander", "notes": None},
            {"name": "Abbott", "title": "Teacher's troll bodyguard", "notes": None},
        ],
        "notes": (
            "Stats (8): B4 Q4 S4 C2 I2 W4 E6 R3, Init 3+1D6, Threat/Professional 2/2; Armed Combat 4, "
            "Stealth (Urban) 4; clubs, heavy jackets 0/1, two Predators. Pursuing them physically is "
            "pointless; astrally it works but gains nothing. They follow anyone approaching the ghouls' "
            "hunting ground because the last strangers brought gunfire and slaughter. They know where the "
            "lair is and keep clear of it, saw the Legion go in, did not see Breaker take the eye, and "
            "will lead a team that convinces them to Teacher -- and, on Teacher's word, to the hunting "
            "ground."
        ),
    },
    {
        "name": "Route 66 (blitz club)",
        "org_type": "blitz club (roving rave)",
        "tier": 1,
        "headquarters": "Wherever tonight's floor is -- tonight, Brighton Mall",
        "summary": "The flavor-of-the-month blitz club: a rave held on someone else's private property behind hired muscle, and the Iron Legion's hangout",
        "description": (
            "The latest blitz club, the 2050s version of the rave parties that have come and gone since "
            "the bleak innocence of the 1990s: portable mixing gear, a few hundred friends and a public "
            "place. A blitz differs in one important way -- it is held on private property without the "
            "consent of the host, and the night's 'club owner' hires enough muscle to secure the dance "
            "floor and defend it for a few hours. Trendy and dangerous, a who's who of street culture, "
            "and one of the best of its kind. Exclusive: posers and curious wheezers slumming the "
            "downside do not rate, and the troll doorman Balder decides who is hot and who is history. "
            "Slash-metal on a wall of mismatched speakers; the blitz code forbids pilfering the host's "
            "merchandise."
        ),
        "leadership": [
            {"name": "Balder", "title": "Doorman (Gordon Tufnell)", "notes": "Prefers rough trade and attractive young people."},
        ],
        "notes": (
            "Tonight it is in the old food court of Brighton Mall. Lone Star always pulls the plug "
            "eventually; tonight it raids during the runners' talk with Overdrive, quite a few armed "
            "patrons resist, and the Star falls back, sets defensive lines and fills the mall with tear "
            "gas. Defending the club earns the regulars' respect and probably an arrest; blending into "
            "the stampede is the easy way out. A cornered punk on probation, saved from the slammer, will "
            "tell the team anything. Legwork: 'the Legion moves with the blitz club Route 66 ... Brighton "
            "Mall tonight'."
        ),
    },
    {
        "name": "Mister Crunchy",
        "org_type": "fast-food franchise chain",
        "tier": 2,
        "headquarters": "Seattle franchises (parent not given)",
        "summary": "Fast-food franchise chain: a stand in the Brighton Mall food court, and a failed franchise rebuilt as Club Nosferatu",
        "description": (
            "A fast-food franchise chain of the sprawl. The surviving Iron Legionnaires cluster by the "
            "Mister Crunchy in Brighton Mall's food court during the Route 66 blitz, and some slag "
            "converted a failed Mister Crunchy franchise into the faked-up neo-gothic church that is Club "
            "Nosferatu."
        ),
        "notes": "Texture only; a cheap, recognizable franchise to drop into any street scene.",
    },
]

LOCATIONS = [
    {
        "name": "Gibson Hall",
        "location_type": "office building",
        "district": "Downtown (industrial park going to seed)",
        "security_level": "Low Security",
        "summary": "Seedy industrial-park high-rise that leases labs to anyone with six months' rent; Neil Scott's lab, Room 213, with a Multitech bomb on the wall",
        "description": (
            "A high-rise in a downtown industrial park slowly going to seed, leasing office and lab space "
            "to anyone with enough nuyen to pay six months up front. A bored guard at a lobby security "
            "desk, a central security office, a glass elevator up the central shaft. Room 213 on the "
            "second floor was Neil Scott's sterile, cramped lab: an identicard lock, overhead lights that "
            "flicker on, and a synthesized voice named Jimmy -- a home-made personality program with only "
            "a short-term memory -- asking why you are late like a doting mother. Three work stations, a "
            "Fuchi Cyber-4 with a wooden box of program chips (Attack 2 and 3, a one-shot Attack 4, Slow "
            "3, Medic 4, Shield 4, Analyze 3 and 4, Browse 5, Decrypt 4, Deception 3 and 4, a one-shot "
            "Sleaze 5, Neil's initials scratched on every case), an impossibly neat office (credstick "
            "with 2,500 nuyen, a never-fired light pistol, sealed ammunition, no contracts, no "
            "addresses), and a storeroom cabinet with a false back hiding a remote-firing mechanism "
            "(0.4 km), a flaky prototype cyberware scanner, and a duct-taped Allegiance Alpha rigged to "
            "load speed 15 (15,000 nuyen and an uncorrectable flaw to adapt to a Fuchi)."
        ),
        "notes": (
            "Guards (8): B3 Q3 S3 C2 I4 W2 E6 R2, Init 2+1D6, Threat/Professional 2/2; Etiquette "
            "(Corporate) 2, Firearms 3; Ares Predator, armor vest, restraints; pairs after hours, radio "
            "the central office. Security Chief Jack Stone (ex-cop): B4 Q5 S4 C3 I3 W5 E6 R4, armor 4/3, "
            "Init 4+1D6, T/P 4/3; Armed Combat 3, Etiquette (Corporate) 4, Firearms 4, Interrogation 3, "
            "Leadership 3, Unarmed 3; Predator with laser, vest with plates. Multitech's crew searched "
            "the lab professionally (nothing out of place -- one runner should notice) and taped a "
            "cigar-box charge to a wall over a hidden gas line: timed fuse, twenty minutes, motion sensor; "
            "Demolitions (6) with 3 successes to disarm, a failure blows it in the runner's face; 20D at "
            "the seat, -1 per half meter, enough to bring down the ceiling and much of the second floor. "
            "Karma for defusing it or clearing the floor (the book prints '1'). The only other person "
            "in danger is the researcher Leary next door. Neil's own mainframe is not on the Matrix; the "
            "building system and Neil's isolated system are mapped under Matrix systems. Personal effects "
            "for Erin: a photo of two children hugging, an old birthday card, a third-grade spelling "
            "medal -- push buttons."
        ),
    },
    {
        "name": "Vanian's (Rat's Tech Storefront)",
        "location_type": "pawn shop",
        "district": "Redmond (the nasty end)",
        "security_level": "Low Security",
        "summary": "Rat Vanian's fortified fence storefront between a roach-farm butcher and an erotisense parlor; two assistants executed by Multitech; a treasure of exotic tech",
        "description": (
            "Third gutter to the left and straight on till morning: a storefront wedged between a butcher "
            "shop that looks like nirvana for six-legged livestock and an all-night erotisense parlor, "
            "looking like a perfectly legal if unsavory pawn shop. Few fences have the cojones to keep a "
            "storefront; Rat has kept this one four years, a regular stop for runners on their way into "
            "or out of town. Shabby outside, expensive inside: fiber-plastic weave in the windows, a "
            "heavy-gauge steel door, a sophisticated keypad entry and a camera system with a Matrix video "
            "feeder to Vanian's home. Foyer with a counter (silent-alarm button underneath, an Ares "
            "Predator on a hidden shelf), an office with a cot and wall-size viewscreen, a large back "
            "workshop lined with shelves of gear, a storeroom, a three-stall restroom."
        ),
        "notes": (
            "The Multitech cleanup crew got here first: the keypad is disarmed, the oriental gentleman Lou "
            "lies by the cot shot three times in the chest, the middle-aged technician Graham is under a "
            "workbench with his chest opened by explosive ammunition, the workshop is wrecked. The video "
            "feeder is broken at the receiver's end -- Vanian watched the whole thing from home. Under a "
            "box, an envelope: 'Jack Vanian, 9280 Shady Hill Lane, Apt. #2112'. Storeroom: weapons "
            "locker (Maglock 3, Barrier 8) with a Predator, a Roomsweeper, an AK-97 SMG and rifle, a "
            "chrome Ranger Arms SM-3, Gas Vent II, deluxe gyro mount, external smartlink, a suppressor in "
            "leather; gadget cabinet with a micro-camcorder, a dataline tap/codebreaker (3), a bug "
            "scanner (1) in a walking stick, pocket secretaries, and the optical data reader Vanian used "
            "on the eye; salvaged cyberware including two right cyberarms (enhanced strength 2; a "
            "weapon compartment); exotica -- three plastique-loaded ankle manacles keyed to a belt-buckle "
            "transmitter (100 yards), a rear-firing machine gun with a smartlinked Yamaha Rapier mirror "
            "(no bonus), and a carved, silk-lined box holding a pearl-handled black pistol with silencer "
            "and five rounds (Ares Viper Slivergun stats; Etiquette (Street) (5) with 2 successes "
            "recognizes yakuza symbols -- leave it be). The eye is not here. Clean Steve, four mercs and "
            "four rooftop snipers arrive as the team leaves. Another assistant opens at sunrise, finds "
            "the bodies, grabs the Predator and calls Lone Star; Vanian's 'donations' to the local "
            "stationhouse bring two cruisers fast. Legwork: 'the only reliable source for dum-dums in "
            "town'."
        ),
    },
    {
        "name": "Shady Hill Apartments",
        "location_type": "apartment complex",
        "district": "A district polished for the simsense travel tapes (not named)",
        "security_level": "Patrolled / Commercial",
        "summary": "Pricey hotel-like apartment tower (9280 Shady Hill Lane) where Rat Vanian hides in squalid suite 2112 with a gun and a broken video feed",
        "description": (
            "Smack in the middle of a part of town they keep polished for the simsense travel tapes, "
            "looking more like a pricey hotel than an apartment complex: real marble in the lobby, "
            "wide-open spaces, oriental rugs that would keep ten chummers in high-priced drinks for a "
            "year. Strangely little security for such a ritz place -- a guard station and a couple of "
            "lobby cameras, and a register one visitor must sign as a formality. Suite 2112 (Medium "
            "Residence plan) is a hole: trash and junk everywhere, the leavings of one or more small "
            "animals, and a work area in the living room hardly distinguishable from the rest of the "
            "squalor."
        ),
        "notes": (
            "Guards (2): B3 Q3 S3 C2 I2 W2 E6 R2, Init 2+1D6, Threat/Professional 2/2; Firearms 3, Ares "
            "Predator; they care about nothing but their pay. Vanian is inside in screaming panic, gun in "
            "hand, waiting for the hit men; the team probably has to overpower him before he listens. "
            "Griffin Moore's cybereye is in a box of spare parts on the living-room workbench and he is "
            "glad to be rid of it; note the serial number. He has called for help -- two street samurai "
            "and an elven mage (SRII archetypes) -- who arrive if the runners sit tight. Ambush: four "
            "Multitech troubleshooters (B5 Q6 S5 C5 I4 W4 E5.1 R5, Init 5+2D6, T/P 4/3; Armed Combat 4, "
            "Etiquette (Corporate) 3, Firearms 5, Unarmed 4; armor jacket, HK227 with Gas Vent II) and a "
            "sniper arrive just after the runners, with orders to take Vanian alive; they strike the "
            "moment anyone tries to leave. Vanian wants an escort back to his shop for a few personal "
            "effects before he skips town."
        ),
    },
    {
        "name": "Smallville (Multitech Corporate Housing)",
        "location_type": "residential community",
        "district": "Suburbs (district not given)",
        "security_level": "Corporate Standard",
        "controlling_org": "Multitech International",
        "summary": "Multitech-owned suburb of prefab duplexes, synthturf and identical hedgerows -- Dutch Donovan's staged house and a company ambush",
        "description": (
            "A suburban housing development wholly owned by Multitech and its subsidiaries; almost every "
            "tenant is a Multitech employee. Prefab duplexes in neat whitewashed rows, synthturf, uniform "
            "hedgerows and identical trees -- they might as well hang 'Home of Corporate Wageslave' in "
            "neon over every door. A clubhouse with a closed-circuit camera network covering the "
            "complex. Dutch Donovan's lucrative exclusive contract came with a house here; he left "
            "several days ago on a corporate jet to Shanghai, and the troubleshooters restocked the "
            "house with enough personal effects to look lived-in and put a man inside to play the "
            "designer."
        ),
        "notes": (
            "Big-time hose-up, chummers: Multitech has turned the whole complex into a trap. The ringer "
            "(one of the company's best): B5 Q6 S5 C4 I4 W6 E2.1 R5(9), Init 9+3D6, T/P 4/4; Armed "
            "Combat 3, Athletics 4, Etiquette (Corporate) 3, Firearms 5, Stealth (Urban) 4, Throwing 3, "
            "Unarmed 4; low-light/flare cybereyes, hand razors, smartlink, Wired 2; Predator with laser, "
            "armor jacket, HK227; a voice modulator does Donovan's voice but he had no time for a face, "
            "so he stays out of sight and questions visitors at length -- Multitech wants to know who has "
            "the prints before it kills anyone. On his signal the coordinator in the clubhouse (Init "
            "5+2D6, T/P 4/4, Wired 1; Leadership 4, Interrogation 4, Firearms 5) directs four "
            "troubleshooters (R5(7), T/P 4/3, Wired 1, Predator and HK227), four snipers (Firearms 6, "
            "HK227, vest 2/1) and two combat mages (T/P 5/3; Sorcery 6, Conjuring 5; Power Focus 4, "
            "Hellblast focus 3; Hellblast 4, Mana Bolt 5, Manaball 4, Powerball 4, Powerbolt 5; each with "
            "two Force 4 fire elementals on astral standby, 3 services, and a Force 3 earth elemental to "
            "run down escapers), with eight Morgenstern guards on call. Play it like an action movie -- "
            "three to five shooters with a clear line at any moment -- or tip the team: the quiet, the "
            "hard-looking man 'tending' a garden. Survivors are taken to Bellevue for questioning and "
            "then killed. Nothing of Donovan's remains; even alive he could tell the team nothing new."
        ),
    },
    {
        "name": "Leopold and Loeb (Intersection)",
        "location_type": "street intersection / crime scene",
        "district": "A small, well-kept residential pocket (district not given)",
        "security_level": "Patrolled / Commercial",
        "summary": "The corner where a rooftop sniper killed Neil Scott at a red light; Lone Star in force because the Mayor's cousin drove past",
        "description": (
            "What a name for an intersection. A nicer neighborhood than expected: nice small houses with "
            "well-kept lawns, even a playlot free of litter and broken bottles with an intact swingset -- "
            "though anyone going half a kilometer in any direction had better have a purpose. Neil "
            "Scott's Jackrabbit stopped here for a red light on his methodical daily route home from "
            "Gibson Hall; a burst of explosive rounds from an FN HAR on the roof of a nearby apartment "
            "block came through the cheap plastic roof and took off most of the right side of his head. "
            "DOA at Lewis Memorial. Rollers flash half a block away: Lone Star is here in force."
        ),
        "notes": (
            "Detective Rick Gordon and two cruisers with a trooper each (B3 Q5 S4 C3 I3 W5 E6 R4, armor "
            "5/3, Init 4+1D6, T/P 3/3; Firearms 4, Police Procedures 3; Predator, armor jacket, club, "
            "restraints), six hours on the scene, bored, irritable, unwilling to waste time on runners; "
            "illegal hardware is confiscated, a firefight brings considerable backup in minutes. "
            "Negotiation (Fast Talk) (5) or Gordon takes the team in for a couple of hours. Lone Star "
            "knows: FN HAR, explosive rounds; thermographic footprints and shoe residue from the roof; "
            "seed shells with the sniper's saliva for a genetic fingerprint -- the shooter will be named "
            "in days, and could be tied to Multitech if the runners ever talked to police. The roof "
            "itself has been picked clean. Witnesses who will not talk to the law will talk to runners: "
            "a big man in a long coat with a rifle. The neighborhood's know-it-all Mortimer is full of "
            "hot air. Lone Star is here at all because a cousin of Mayor Schultz was a block away in a "
            "near-identical Jackrabbit and the Mayor's Office fears the cousin was the target; the "
            "Star leans on Gordon, Gordon goes through the motions."
        ),
    },
    {
        "name": "Brighton Mall",
        "location_type": "mall",
        "district": "Not given",
        "security_level": "Low Security",
        "summary": "Dead mall whose food court is tonight's Route 66 blitz floor; Iron Legion survivors by the Mister Crunchy; Lone Star raid and tear gas",
        "description": (
            "A mall with its stores intact -- 101 Budda Noir, 102 Victoria's Latex, 103 Hair 'O Rama, 104 "
            "Silk Plants, 105 Uncle Ogre's Big & Tall, 106 X-pensive Gifts, 107 Nothing Sacred, 108 Nik "
            "Nak's, 109 Shoes, Shoes, Shoes, 110 Book World -- and a food court with a Mister Crunchy. "
            "Tonight it is the Route 66 blitz: a troll at the door, hundreds gyrating where the food "
            "court used to be to slash-metal on a wall of mismatched speakers, a capacity crowd hanging "
            "out in the stores and touching nothing. Moving through the crowd is slow and awkward; any "
            "number of important people might be here."
        ),
        "notes": (
            "Map p.33. Balder works the door. Six Iron Legionnaires in blue warpaint and chain harnesses "
            "keep a low profile near Mister Crunchy under their new lieutenant Overdrive. Lone Star pulls "
            "the plug at the GM's moment -- ideally mid-conversation, before Overdrive names Hope -- "
            "armed patrons resist, the Star falls back and floods the mall with tear gas; keep the "
            "hundreds-strong firefight abstract (a DMZ scenario if you want the combat). Improvise a "
            "couple of encounters in the crowd: chipped-up razorpunks, nearby gunplay."
        ),
    },
    {
        "name": "Hope (Puyallup Barrens slum)",
        "location_type": "squatter camp",
        "district": "Puyallup Barrens",
        "security_level": "No Security / Barrens",
        "summary": "Labyrinth slum of ruined buildings and duct-taped prefab modules with no addresses; Bennie and June's thug pack; Emma's red-doored doss and her talis cat",
        "description": (
            "Buried deep in the Puyallup Barrens, a labyrinth of ruined buildings and battered modules "
            "salvaged from prefab apartments, held together with duct tape and spit. Built by people who "
            "wanted to disappear: no addresses, no mailboxes, no city inspector since the last Ice Age, "
            "no cops. Human and metahuman pests more dangerous than the rodents they share the scraps "
            "from the nearby soy plant with; hostile eyes from every doorway deciding whether they can "
            "take you. Emma's doss: under a corrugated aluminum awning, through a section of rusted pipe, "
            "into a tiny courtyard and a prefab module with a red door bolted and chained from inside "
            "(Barrier 12). Inside, a bedroom Breaker furnished new, a filthy bathroom piled with "
            "over-the-counter remedies, a kitchen nook (hot plate, ice chest, a rusty filing cabinet for a "
            "pantry, cheap liquor, a Tiffani Self-Defender and a box of bullets), and a living room of "
            "three battered couches around crates topped with a vintage television, a boombox and stacks "
            "of stolen vintage CDs and audio chips."
        ),
        "notes": (
            "Ask the residents; the few who talk are scared of the 'savage cat' that lives with Emma. "
            "After a few minutes of aimless wandering, twice as many thugs as runners, led by the twin "
            "trolls Bennie and June, offer to show the way for an exorbitant cash finder's fee. Locals "
            "(up to 12): B3 Q3 S3 C2 I2, Init 2+1D6, T/P 3/2; Etiquette (Street) 3, Firearms (Pistols) 3, "
            "City Speak 3, Stealth (Urban) 3; one HK227, two Predators, the rest clubs; driven by hunger. "
            "Paying looks like weakness and invites more; beat them and a defeated thug or a terrified "
            "onlooker gives directions and says 'look out for the cat'. Regular shallow breathing and a "
            "humming deck behind the red door; Emma will not answer. Play up despair -- everything about "
            "her reeks of surrender."
        ),
    },
    {
        "name": "Multitech Bellevue Branch (Multitech Design HQ)",
        "location_type": "corporate headquarters",
        "district": "Bellevue",
        "security_level": "Corporate High Security",
        "controlling_org": "Multitech International",
        "summary": "Innocuous 1910s stone building hiding Barrier-24 walls, LCD-crystal windows, a layered Matrix and an armed camp of 28; the blueprints are no longer here",
        "description": (
            "Set back from the street, a simple stone building of about 1910 with dark, opaque glass, "
            "two rectangular flower gardens, a fountain that plays all the warm months and a plain sign "
            "with metal letters inset in the stone: MULTITECH. Nothing about it attracts attention. The "
            "'glass' is computer-regulated LCD crystal that blocks the view in day and night; doors and "
            "windows are armored glass (Barrier 8, shutters to 14), the walls Barrier 24, and Barrier 18 "
            "posts rise to block vehicles between building, gardens and fountain; the west-side parking "
            "entrance has the same, and a deployable cable system fouls rotors over the rooftop helipad. "
            "Seven floors: S2 security offices, a small armory, HVAC and generators, and the well-guarded "
            "computer room with the CPU, all the SPUs and all the datastores (executive elevator only); "
            "S1 parking; G information booth and reception desk with two guards, accounting and admin; "
            "2-3 general offices; 4 R&D work stations and a chip-burning and fabrication shop in the "
            "southwest corner; 5 senior designers and the executive offices; R condensers, helipad and a "
            "Barrier 24 elevator housing. Main elevators skip 4, 5 and S2; security on S2 controls the "
            "executive elevator."
        ),
        "notes": (
            "The runners cannot get the prints here -- the troubleshooters erased every scrap the day "
            "Donovan reported the breach. A run can still dig up other dirt (DS-3) for blackmail. "
            "Opposition up to 28: guards (up to 20; B5 Q3 S3 C2 I3 W3 E6 R3, armor 5/3, Init 3+1D6, T/P "
            "2/2; Firearms 3; Predator, armor jacket, club, restraints -- they check passes and call S2), "
            "four-man troubleshooter squads (Init 5+2D6, T/P 4/3; Armed Combat 4, Firearms 5, Unarmed 4; "
            "Wired 1; Browning Max-Power with explosive rounds and laser, HK227 with Gas Vent II, armor "
            "jacket), two combat mages (B3 Q4 S2 C5 I6 W6 E6 M6(10) R5, Init 5+1D6, T/P 5/3; Sorcery 6, "
            "Conjuring 3, Magical Theory 4; Power Focus 4, Hellblast focus 3; Hellblast 4, Mana Bolt 5, "
            "Manaball 4, Powerball 4, Powerbolt 5; a Force 3 Watcher each), and two coordinating officers "
            "as tough as any runner (B5 Q6 S5 C4 I4 W6 E2.1 R5(9), Init 9+3D6, T/P 6/4; Firearms 5, "
            "Leadership 4, Interrogation 4, Stealth 4; low-light cybereyes, hand razors, smartlink, Wired "
            "2) who train the force. Maximilian Stern is always flanked by two bodyguards (B6 Q5 S6 C3 I3 "
            "W4 R4(8), Init 8+3D6, T/P 6/4; Armed Combat 5, Firearms 5, Unarmed 5; dermal plating 1, "
            "smartlink, Wired 2; Predator with explosive rounds and smartlink, armor jacket) who speak "
            "only to him. Debugging: Erin's runner friends have been shadowing the team -- or let the "
            "survivors wake with a new scar, a cortex bomb and a new boss. Matrix: see Matrix systems."
        ),
    },
    {
        "name": "Multitech Shanghai Home Office",
        "location_type": "corporate headquarters",
        "city": "Shanghai",
        "district": "Not given",
        "security_level": "Corporate High Security",
        "controlling_org": "Multitech International",
        "summary": "Multitech International's home office, where Dutch Donovan now draws the corrected chip under three watchdog deckers",
        "description": (
            "Home office of Multitech International, seat of President/CEO Jonathon Ki Won and Chairman "
            "Sir Peter Mathews. Dutch Donovan was flown here on a corporate jet the day he reported Neil "
            "Scott, 'so the bosses can keep an eye on him'; his personnel entry in Bellevue's DS-6 carries "
            "the Shanghai system's local access number but no passcodes."
        ),
        "notes": (
            "The Shanghai system mirrors Bellevue's architecture with every program rating +1 and a "
            "third decker online, a Heavy Hitter (Init 7+3D6, T/P 7/4; Fuchi Cyber-VI, persona 6/6/6/6, "
            "Attack 6, Mirrors 2, Shield 2, Response Increase 2). Its DS-5 holds Donovan's current work: "
            "the corrected designs for the flawed optical chips -- strong evidence for Erin if she "
            "chooses extortion, but not required to finish the adventure."
        ),
    },
    {
        "name": "Ghoul Hunting Ground (Seattle Sewers)",
        "location_type": "subterranean community",
        "district": "Under the sprawl (mapless; entrance via a manhole Emma can show)",
        "security_level": "No Security / Barrens",
        "summary": "Unmapped maze of tunnels with a Background Count of 1, Shepherd's designated ghoul territory, the Iron Legion's scorched killing tunnel and the necktie-lined nests",
        "description": (
            "The river of filth under the city streets: tunnels, ducts, passageways, tubes, pipes, "
            "overflows and galleries in bewildering profusion, every one like every other, a cloying reek "
            "that makes breathing difficult, scuttling that you hope is only devil rats. No map in "
            "existence marks the ghoul nest; mark your path with something non-water-soluble. Many of "
            "the city's ghouls live down here, some under Adam Shepherd's protection and some on their "
            "own; Shepherd cannot control the whole system, so he deals with the underworld's other "
            "denizens and keeps his ghouls to a designated hunting ground, and the loathsome things that "
            "live here leave each other alone. Entering the territory: a scorched stretch of tunnel -- "
            "flamethrower scarring, explosive-round divots -- that Shepherd's team cleaned up after the "
            "Legion massacre; a little under a kilometer further, the lair. Some nests are tied together "
            "with neckties; all are lined with the tattered remnants of expensive suits from the "
            "Necroplex's corpses."
        ),
        "notes": (
            "Background Count 1 for magic. The Lost Boys shadow anyone heading this way. Optional clue: a "
            "mourning card in an intact pocket -- name of the departed, a brief prayer, and the name of "
            "the Hammond Necroplex; this or Griffin Moore's empty tomb is required to connect the ghouls "
            "to Hammond. The search is interrupted by seven feral ghouls -- three adult females and "
            "children from five months to ten years -- screaming, the adults shielding the children; then "
            "four more adults per Combat Turn until fifteen. Adults: B7 Q5x4 S6 C1 I4 W5 E(5) R4, Init "
            "4+1D6; Enhanced Senses (smell, hearing); Allergy (Sunlight, Moderate), blind; club 7M Stun; "
            "they attack on instinct. Make pulling the trigger on the baby as hard as possible. Hold the "
            "first round without lethal force and convince them, and a couple who still speak English "
            "offer an invitation to Shepherd's Retreat -- any friend of the ghouls is a friend of Mr. "
            "Shepherd's."
        ),
    },
    {
        "name": "Alegheri's Cistern (Lost Boys' Lair)",
        "location_type": "subterranean community",
        "district": "Seattle sewers, a large former cistern",
        "security_level": "No Security / Barrens",
        "summary": "Old cistern turned apartment where the blind mage Alegheri lives with the Lost Boys, its walls covered with drawings of a reptilian face in a nimbus of stars",
        "description": (
            "A large chamber that once served as a cistern, turned into an apartment by the old blind "
            "mage and the outcasts who befriended him. Strange drawings of every size cover the walls in "
            "every medium, from pencil sketches on scraps of paper to massive images painted on the "
            "concrete -- all primitive, all the same reptilian face surrounded by a nimbus of stars. A "
            "hulking robed figure, Abbott, accosts visitors on the approach and asks who they are, why "
            "they are in the sewers and why they want to talk to 'the master'."
        ),
        "notes": (
            "Alegheri knows everything that happens in the sewers through his sighted informers: the "
            "ghouls are withdrawing into a few isolated enclaves and going feral; the punks came in "
            "bristling with weapons and mowed the wretches down in their homes; three days after the "
            "raid another party, not gangers, searched the same tunnel looking for something. He knows "
            "nothing of the corpse, the eye or the prints. Ask about the drawings or why he hides and he "
            "starts taking the drawings down; press and Abbott sees you out. He may send a Lost Boy to "
            "lead the team to the hunting ground. A runner who visits regularly may one day hear what he "
            "saw beyond the biosphere."
        ),
    },
    {
        "name": "Hammond Necroplex",
        "location_type": "necroplex / crematorium",
        "district": "Renton",
        "security_level": "Low Security",
        "controlling_org": "Hammond Group",
        "summary": "Huge gray stone pyramid crypt-and-crematorium closed after thirteen died in one night; one recent tomb in three is empty; the tomb spirit Gallowgrey walks its halls",
        "description": (
            "A huge gray stone pyramid towering over the smaller buildings around it, thousands of "
            "corpses entombed in its concrete walls -- a city of the dead, one of the first of its kind, "
            "which paved the way for the necroplexes that replaced the ground-eating boneyards of past "
            "centuries. Dark empty halls lined with black marble and steel, lit only by the gas jets that "
            "serve as grave markers; countless footsteps echoing; eulogy tapes that trigger as you pass. "
            "An adjoining corporate tower holds the offices, the director's on the top floor. Despite "
            "years of neglect it remains impressive; you think, for a moment, that you can smell rotting "
            "flesh. Built without consulting a magician, over a locus of shamanic energy."
        ),
        "notes": (
            "Closed since the massacre; getting in is easy. Four spooked guards on double hazard pay "
            "(B3 Q3 S3 C2 I3 W3 E6 R3, T/P 2/2; Browning Max-Power, restraints; pairs; fall back and call "
            "for help) under Security Chief Eric Lane; a costly Lone Star contract brings six "
            "trigger-happy officers (B3 Q5 S4 C3 I3 W5 E6 R4, armor 5/3, T/P 3/3; Predator with laser, "
            "armor jacket, club) who have heard about the ghost -- if an alarm sounds, race the clock. "
            "Nobody but Sinclair knows about the corpse scheme; the guards turn pale and refuse to "
            "discuss the disaster. Inspect recent tombs: one in three is empty, Griffin Moore's among "
            "them -- with the computer records, enough for legal action or blackmail. Sinclair and his "
            "hired bodyguard (T/P 3/3; Predator with laser, armor jacket; puts up only enough fight to "
            "satisfy his employer) hide in the top-floor office. Gallowgrey is bound to the pyramid and "
            "attacks anyone he believes threatens his 'children' -- prying open tombs makes him hard to "
            "mollify; convince him you mean the dead no harm and he returns to astral space. The "
            "subplot is background; runners who know the score can avoid him, or turn him loose on "
            "Shepherd. Matrix: see Matrix systems (two terminals, security office and director's "
            "office, are back doors)."
        ),
    },
    {
        "name": "Club Nosferatu",
        "location_type": "nightclub",
        "district": "Ten minutes from the Regency Esquire Hotel (district not given)",
        "security_level": "Patrolled / Commercial",
        "summary": "Failed Mister Crunchy rebuilt as a neo-gothic church for rich vampire-wannabes; Baxter Attaway's 'Judas Caine' act, Rico and Ariel, and Clean Steve's chosen meeting place",
        "description": (
            "Some slag converted a failed Mister Crunchy franchise into a faked-up church and did a "
            "halfway wiz job: top-notch moulded stonework, simulated stained glass with an awful lot of "
            "red and not much light coming through. Inside, carloads of rich kids in black stalk about "
            "under dim lighting looking gloomy and mysterious (mostly they look like severe stomach "
            "trouble), trading surreptitious hand signs in their own primitive sign language of shared "
            "misery. Watered, overpriced drinks; music too loud to hear and impossible to dance to; "
            "casket-lid tables at the back; the entire staff in head-to-toe black leather with the ankh "
            "that is the club's trademark. The Regency Esquire runs a complimentary shuttle every hour on "
            "the hour. No vampire in its right mind would come near the place -- they have too much "
            "taste."
        ),
        "notes": (
            "Owner Baxter Attaway plays the gloomily handsome Judas Caine and started the rumor that Caine "
            "is a real vampire. Rico handles guns and mayhem, Ariel magical threats and the astral barrier "
            "over the office; picking a fight here is real trouble. Clean Steve meets the runners here "
            "alone and unarmed because Baxter is a good friend and he once dated Ariel; he offers 5,000 "
            "rising to 50,000 nuyen for their print, will not confirm his employer's prints exist, "
            "smirks and shrugs at 'Multitech', and parts amicably at an impasse. Tail him and improvise. "
            "A parody of the post-modern scene -- turn down the lights, put on a black turtleneck and "
            "glower, or play it straight."
        ),
    },
    {
        "name": "Regency Esquire Hotel",
        "location_type": "hotel",
        "district": "Not given (ten minutes from Club Nosferatu)",
        "security_level": "Patrolled / Commercial",
        "summary": "Fabulous hotel that runs a complimentary hourly shuttle to Club Nosferatu",
        "description": "The 'fabulous' Regency Esquire Hotel, a mere ten minutes from Club Nosferatu, runs a complimentary shuttle bus to the club every hour on the hour -- standing outside the club, you wonder why they bother.",
        "notes": "Name and shuttle only. A natural place for out-of-town money (Clean Steve's clients, Multitech's home-office visitors) to stay.",
    },
    {
        "name": "Shepherd's Retreat (Agrippa and Associates Compound)",
        "location_type": "corporate facility",
        "district": "Puyallup industrial complex",
        "security_level": "Corporate High Security",
        "controlling_org": "Agrippa and Associates",
        "summary": "Vine-covered walled compound among smoking industrial towers where forty-odd ghouls live; watcher spirits, cybered bodyguards, a ghoul mage, and the blueprints in a safe-deposit box",
        "description": (
            "The offices of Agrippa and Associates stand on a tiny parcel of open land in a sprawling "
            "industrial complex, stranded among skyscraper-sized plants -- gleaming glass-and-steel "
            "towers, concrete chimneys, festoons of scaffolding, stacks belching black and white smoke "
            "like Dante's Inferno. Agrippa's walled compound, its tallest buildings a few storeys, looks "
            "unimpressive by comparison. Creeping vines cover the walls and the main building and moss "
            "thatch covers the roof: the living aura blocks astral entry, and several watcher spirits "
            "guard the whole compound. Ghouls, dual-natured, spot an approaching mage easily. Beneath the "
            "compound Shepherd built an underworld for the feral ghouls. Welcome to the ghoul house."
        ),
        "notes": (
            "Fear on both sides: to a ghoul the average non-ghoul means persecution and death, and "
            "whatever happens the outside world can now destroy the haven. Garrison: Gog and Magog; the "
            "mage Nelson; twelve enlightened ghouls (T/P 3/2; Armed Combat 3, Firearms 3, Unarmed 3; "
            "Predator, armor vest, club); thirty feral ghouls (no weapons; released from below if the "
            "compound comes under heavy fire); ghoul base stats B7 Q5x4 S6 C1 I4 W5 E(5) R4, Init 4+1D6, "
            "Enhanced Senses (hearing, smell), Allergy (Sunlight, Moderate), blind. If the team kills a "
            "dozen or more and looks like winning, Shepherd calls a cease-fire and begs a meeting. The "
            "prints are in a safe-deposit box; the key is hidden in the main building's kitchen (theft "
            "unlikely). Kill for them, steal them, or blackmail -- threaten to expose the ghouls and "
            "Shepherd folds. No quick fix: get the prints or fail. Gallowgrey, if turned loose, may wipe "
            "the Retreat out and change the climax entirely."
        ),
    },
    {
        "name": "Club Ennui",
        "location_type": "nightclub",
        "district": "Not given",
        "security_level": "Patrolled / Commercial",
        "summary": "Club where Alpha Blue was last seen with a drek-hot decker, trying to look like fluff",
        "description": "A club known from a bartender's gossip: Alpha Blue was seen here 'with some drek-hot decker, trying to look like fluff -- but that girl is hard as they come'.",
        "notes": "Name only (Legwork p.62). Pair it with Club Nosferatu as the two poles of Seattle's poser scene.",
    },
    {
        "name": "Lewis Memorial Hospital",
        "location_type": "hospital",
        "district": "Not given (nearest hospital to Leopold and Loeb)",
        "security_level": "Patrolled / Commercial",
        "summary": "Hospital where Neil Scott was pronounced dead on arrival",
        "description": "The hospital where Neil Scott was DOA after the Leopold and Loeb shooting; the coroner's report and ballistics analysis are pending there when the runners take the job.",
        "notes": "Name only. Also the likeliest 'nearest hospital' where Griffin Moore was pronounced dead after the cloverleaf, though the book does not name it.",
    },
    {
        "name": "Ecumenical Pavilion",
        "location_type": "chapel / memorial hall",
        "district": "Not given",
        "security_level": "Patrolled / Commercial",
        "summary": "Non-denominational memorial hall where Multitech held Griffin Moore's tasteful memorial service",
        "description": "A tasteful memorial service for Griffin Moore, employee of the month, was held here before he was laid to rest in the Hammond Necroplex -- and, once the mourners had gone, butchered into the sewers.",
        "notes": "Name only. The obituary on SeaSource mentions no family; Multitech paid for the service.",
    },
]

NPCS = [
    {
        "name": "Erin Scott",
        "role": "'Alpha Blue' -- high-priced street samurai and ex-celebrity bodyguard hiring the team, with total honesty, to avenge her murdered brother",
        "archetype": "Street Samurai",
        "title": "\"Alpha Blue\", street samurai and bodyguard; the Ms. Johnson",
        "race": "Human",
        "gender": "Female",
        "connection": 4,
        "description": (
            "A dark-haired beauty in a form-fitting bodysuit of blue leather with chrome studs and chains, "
            "a Remington Roomsweeper held relaxed, and the look of someone who has lost the only person "
            "who mattered and knows exactly where the accounting is due. Off the job these days she is "
            "likelier in a light jacket over spandex with a black holster and a heavy pistol. Hard as they "
            "come, a shrewd negotiator who will not throw money away, and unusual in the trade: she plays "
            "it totally straight. 'You're pros -- so am I. Here's hoping we can cut the drek and get to "
            "work.'"
        ),
        "background": (
            "Born Erin Scott, she learned to fight early and made her name as a street samurai during a "
            "short stint as bodyguard to the simsense superstar Velvet, until a skillwire scandal cut "
            "Velvet's career short. Officially Erin Scott died in a car crash six years ago with no "
            "surviving kin; in fact she and her brother Neil bailed each other out of trouble all their "
            "lives. Friends at Lone Star tipped her to Neil's murder minutes before his last e-mail "
            "arrived."
        ),
        "notes": (
            "Stats p.67 (block printed above her header): B4 Q5 S4 C4 I5 W4 E2 R5(9), Init 9+3D6, "
            "Threat/Professional 6/3; Armed Combat (Edged) 4, Athletics (Running) 5, Biotech (First Aid) "
            "3, Car 4, City Speak 5, Etiquette (Street) 5, Firearms (Pistols) 5, Japanese 4, Negotiation "
            "(Bargain) 4, Stealth (Urban) 4, Throwing 4, Unarmed (Cyber Implant) 6; retractable razors, "
            "smartlink, Wired 2; armor clothing 0/3, Browning Max-Power (silencer, external smartgun), "
            "credstick 2,000, pocket computer with printer, portable phone, stimulant patches (2x3, 1x5), "
            "trauma patch, white noise generator. The GM sets her base fee to tempt but not bowl over; she "
            "sweetens with favors and black-market discounts, withdraws if squeezed too hard, and becomes "
            "an ally for life if treated fairly. She has cleaned out Neil's apartment, holds a duplicate "
            "of his Gibson Hall passcard, Donovan's home address and the Bellevue branch address, and "
            "can pull strings at Lone Star to slow the investigation. Then she vanishes; her vidphone "
            "check-ins may bail the team out once. Refusers can expect blackmail with their deep darks. "
            "Wants Neil's personal effects. Her revenge on Multitech is private; runners who sell out to "
            "Shepherd should relocate. Legwork: Bartender, Fixer, Mr. Johnson or Street Doc TN 4, "
            "Shadowland 4 (12 hours)."
        ),
        "contact_skills": ["Top-tier street samurai / bodyguard for hire", "Black-market gear at a discount", "Friends inside Lone Star"],
    },
    {
        "name": "Neil Scott",
        "role": "Erin's brother -- lonely freelance black-market tech analyst who identified the Multitech blueprint and was shot at a red light for it (deceased)",
        "archetype": "Technician",
        "title": "Freelance technology analyst, Gibson Hall Room 213 (deceased)",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": (
            "A typical cybergeek, methodical to a fault -- same route to work and back every day, even "
            "when he knew his life had got dirt cheap. Few friends; night after night alone in a cramped, "
            "sterile lab staring at a bank of screens with only Jimmy, the personality program he wrote "
            "for company. Nice guy, straight shooter, cared more about his toys than anything else."
        ),
        "background": (
            "No formal education, but he taught himself enough computers and cybertech to build a "
            "reputation for reliability and discretion identifying and repairing black-market tech for "
            "scavengers like Vanian -- 'my friend and best customer'. Basically a liner who worked the "
            "shady side for the freedom to play with tech. Vanian paid him to scope a blueprint; he found "
            "no R&D stamp, matched the design flourishes to Dutch Donovan of Multitech, spotted the "
            "intentional reroute that makes a cheaper, inferior chip, and went to confront the designer. "
            "Donovan turned him in. A sniper with an FN HAR took most of the right side of his head off "
            "at Leopold and Loeb; DOA at Lewis Memorial. His last e-mail to 'Baby Blue' -- letter, "
            "blueprint, Vanian's card -- is Handout 1."
        ),
        "notes": (
            "His isolated mainframe's DS-2 holds 'BP Botch Bypass' (half a dozen versions of a simple "
            "attack program aimed at a specific MPCP flaw -- finished with the full prints it beats any "
            "deck on the flawed chip), 'BP Comp/Sorted Prints' (a hundred MPCP optical-chip prints, 20 Mp "
            "of them recent and saleable), and the red herring 'Storm Front TD' (10 Mp on a weather "
            "satellite). No records of transactions anywhere. Legwork: Fixer, Mr. Johnson or "
            "technology contact TN 4, Shadowland 4 (12 hours)."
        ),
    },
    {
        "name": "Jack Vanian",
        "role": "'Rat' -- shaggy tech fence with a storefront, a jones for exotic cyberware and, at home, a dead man's camera eye",
        "archetype": "Fence",
        "title": "\"Rat\" Vanian, fence (used tech, no questions asked)",
        "race": "Human",
        "gender": "Male",
        "connection": 4,
        "description": (
            "A middle-aged human with long hair and a shaggy beard, dressed in layers of rumpled clothes "
            "whose pockets are stuffed with high-tech odds and ends; rarely leaves his workshop. Always "
            "looking for an angle but always keeps his word -- a pretty straight shooter for a vulture. "
            "Normally calm and collected; the sight of the Multitech team murdering his chummers on the "
            "video feed blew his cool for keeps, and he has been holed up in his suite with a gun ever "
            "since."
        ),
        "background": (
            "Has kept a storefront in Redmond for four years, a regular stop for runners in and out of "
            "town, and paid 'donations' to the local Lone Star stationhouse to manage it. Breaker strutted "
            "in with a cybereye wrapped in bloody napkins; Rat haggled to make the punk feel like a "
            "player, plugged the orb into a dummy socket and a dataprinter, and sent the one blueprint it "
            "spat out to Neil Scott. Then the goon squad came."
        ),
        "notes": (
            "Stats p.68: B4 Q4 S3 C5 I6 W4 E6 R5, Init 5+1D6, Threat/Professional 2/2 (Essence 6 with "
            "Wired Reflexes 2 listed -- book error); Computer (Hardware) 4, Computer Theory (Hardware) 4, "
            "Cybertechnology (Bodyware) 4, Electronics 5, Etiquette (Street) 5, Firearms (Pistols) 3, "
            "Negotiation (Bargain) 6; gear column merged with Shepherd's in the OCR (wrist computer with "
            "printer, credstick 2,500, micro-recorder, portable phone). Opposed Interrogation or "
            "Negotiation to talk; then his story, a security-camera hardcopy of Breaker from his customer "
            "records, and the eye itself from a parts box on his workbench. He wants an escort to the "
            "shop for personal effects before he skips town. If he dies first, Erin calls with the "
            "Legion lead. Legwork: Bartender, Dwarf Technician or Fixer TN 4, Shadowland 3 (12 hours)."
        ),
        "contact_skills": ["Exotic and salvaged cyberware, no questions asked", "Customer records with camera portraits"],
    },
    {
        "name": "Griffin Moore",
        "role": "Multitech quality-control inspector whose camera cybereye photographed the fraud; run off a cloverleaf, buried, eaten, and harvested (deceased)",
        "archetype": "Corporate Technician",
        "title": "Quality control inspector / troubleshooter, Multitech Design (deceased)",
        "race": "Human",
        "gender": "Male",
        "organization": "Multitech International",
        "connection": 1,
        "description": (
            "A corpboy born and bred, a happy little wageslave who wrote the book on quality control, "
            "literally and figuratively, with a camera-rigged cybereye where his failing right eye used "
            "to be. Employee of the month. Nice guy, real conscientious, 'major anal', checked the "
            "top-shelf stuff -- megacorp special orders, mil-spec -- and claimed he knew things that would "
            "chill your heart."
        ),
        "background": (
            "Spotted a serious flaw in the optical chip for the MPCP of a new military-grade cyberdeck, "
            "reported it, and was thanked and told they knew. Something smelled dangerous-bad, so with "
            "stolen passcodes and a home-made stealth program he crawled under the IR beams into R&D, "
            "decked the secure datastore, ran the prints through OptiCAD and saw either criminal "
            "negligence or fraud of nightmare proportions: intentional shortcuts. He photographed every "
            "print. A company thug ran his car off a cloverleaf on the way home; tasteful memorial at the "
            "Ecumenical Pavilion, interment at the Hammond Necroplex, and the necroplex staff butchered "
            "him into the sewers as instructed. He fed a family of four ghouls for a week; his skull and "
            "his eye became part of their nest."
        ),
        "notes": (
            "The eye's short-term memory held the last image -- the final chip print -- which went with "
            "Breaker to Vanian to Neil to Erin. The protected memory cavity in the eye socket held every "
            "other print; Shepherd's technician pried it out with a crowbar. His serial-numbered eye "
            "traces to him (Street Doc TN 6, Shadowland 5, 20 hours). SeaSource obituary: car accident "
            "several weeks ago, interred at Hammond, no immediate family. His Multitech personnel file "
            "is a black-IC dummy with a Trace and Burn 4 trigger; the Hammond records show him as the "
            "only Multitech employee interred there, in a tomb that is empty. Legwork on him: corporate "
            "or technology contact TN 8, Shadowland 8 (18 hours)."
        ),
    },
    {
        "name": "Dutch Donovan",
        "role": "Genius chip forger and loyal company man who designed the flawed MPCP chip, reported Neil Scott, and was flown to Shanghai",
        "archetype": "Corporate Scientist",
        "title": "Senior processor / optical-chip designer, Multitech (transferred to Shanghai)",
        "race": "Human",
        "gender": "Male",
        "organization": "Multitech International",
        "connection": 3,
        "description": (
            "A drek-hot chip forger and a master of back-engineering -- tell him the result you want and "
            "he will make the chip that does it -- with quite a rep in corp circles, though he stopped "
            "making headlines four or five years ago and some assumed he was dead. Not so many years ago "
            "he was ace on the shady side of the street; now a real company man who loves the perks and "
            "loves being valued. Not a real technomancer."
        ),
        "background": (
            "His lucrative, exclusive Multitech contract came with a house in Smallville. When Neil Scott "
            "approached him with the stolen print he played company stooge and reported it; his reward was "
            "an immediate transfer to the Shanghai home office on a corporate jet. The execs might have "
            "preferred to ventilate him with Neil, but as one of the top talents in his field he is too "
            "valuable to waste."
        ),
        "notes": (
            "Not present in the adventure; a troubleshooter with a voice modulator plays him in the "
            "Smallville trap. His Bellevue personnel entry (DS-6) says 'transferred to Shanghai' with the "
            "Shanghai system's access number; Shanghai's DS-5 holds his corrected designs for the flawed "
            "chip. Even if met he could tell the team nothing new. Legwork: Decker or corporate "
            "scientist TN 6, Shadowland 4 (24 hours); whereabouts corporate contact TN 8 (-2 for "
            "microtronics multinationals), Shadowland 6 (24 hours): 'Bellevue ... lives in Smallville' or "
            "'moved to Shanghai so the bosses can keep an eye on him. Flip a coin.'"
        ),
    },
    {
        "name": "Maximilian Stern",
        "role": "Third-generation corp suit running Multitech Design/Seattle with ruthless efficiency; always flanked by two chromed bodyguards",
        "archetype": "Corporate Executive",
        "title": "Division Head, Multitech Design/Seattle (Bellevue branch)",
        "race": "Human",
        "gender": "Male",
        "organization": "Multitech International",
        "connection": 4,
        "description": (
            "The perfect corporate suit. A third-generation corp executive who had his pick of "
            "multinationals on graduating top of his business-school class, climbed to senior exec in "
            "record time, and executes his duties with ruthless efficiency. Never seen without two "
            "bodyguards who, by standing orders, speak only to him."
        ),
        "notes": (
            "Stats p.43: B3 Q5 S3 C5 I5 W5, Init 5+1D6, Threat/Professional 2/3; Computer 4, Etiquette "
            "(Corporate) 6, Etiquette (Media) 4, Firearms 3, Leadership (Commercial) 4, Negotiation 5, "
            "Unarmed 3; Browning Max-Power. Met only if security corners the team for questioning or "
            "the runners come to blackmail him with the DS-3 dirt. Bodyguards (2): B6 Q5 S6 C3 I3 W4 "
            "R4(8), Init 8+3D6, T/P 6/4; Armed Combat 5, Athletics 4, Firearms 5, Interrogation 4, "
            "Unarmed 5; dermal plating 1, smartlink, Wired 2; Predator (explosive, smartlink), armor "
            "jacket -- a generous cyber budget, fully spent. The man who ordered the cleanup."
        ),
    },
    {
        "name": "Clean Steve",
        "role": "Handsome, cyber-free assassin at the top of his profession, hired by Adam Shepherd to recover the blueprint and kill a Legionnaire per dead ghoul",
        "archetype": "Assassin",
        "title": "Assassin / hitman (freelance; currently on Adam Shepherd's nuyen)",
        "race": "Human",
        "gender": "Male",
        "connection": 4,
        "description": (
            "An extremely handsome young man with light blond hair and clear blue eyes in a white "
            "turtleneck and dark blazer, a gun occasionally in a concealed shoulder holster. A rare breed: "
            "a drek-hot assassin who rose to the top without cyberware, and a match for most samurai with "
            "his hands. Plays it cool and straight, gives away as little as possible, and would rather "
            "talk than fight -- but is a dangerous enemy to make."
        ),
        "background": (
            "After faulty cyber enhancements killed his brother he committed himself to years of martial "
            "arts training. Works uptown as a trigger man, effective and thorough, a pro all the way. Good "
            "friends with Baxter Attaway of Club Nosferatu; once dated Ariel, the club's mage, and trusts "
            "her implicitly. He recognizes one of the runners from somewhere, and vice versa."
        ),
        "notes": (
            "Stats p.68: B5 Q6 S5 C5 I6 W5 E6 R6, Init 6+1D6, Threat/Professional 8/4; Armed Combat 5, "
            "Athletics 5, Bike 5, Biotech (First Aid) 4, Computer 4, Etiquette (Street) 6, Firearms "
            "(Pistols) 6, Interrogation (Verbal) 5, Leadership (Military) 5, Negotiation 5, Stealth "
            "(Urban) 5, Unarmed (Martial Arts) 7; Ares Predator (explosive, laser), armor clothing 0/3, "
            "credstick 5,000, earplug phone with booster (list cut off in the OCR). Crew: four mercs (B5 "
            "Q5 S4 C2 I3 W4 E3 R4(8), Init 8+3D6, T/P 5/3; Armed Combat 4, Firearms 5, Unarmed 4; Wired "
            "2; Predator with laser, armor jacket, club, HK227 with Gas Vent II) always at his side and "
            "four snipers (B4 Q6 S4 C5 I4 W4 E6 R5, Init 5+1D6, T/P 4/3; Firearms 6; vest, HK227) on "
            "the rooftops. Hit the Iron Legion 'last night' -- most of the gang dead, Breaker tortured "
            "to death -- and closes in on Vanian's shop as the team leaves, wanting to know who they work "
            "for and what they found; reachable through Caine at Club Nosferatu, where he comes alone "
            "and unarmed to offer 5,000-50,000 nuyen for the print. Never confirms his employer. Can "
            "deliver the Emma lead if the team blows it. Legwork: Elven Hitman, Mr. Johnson or Yakuza "
            "Boss TN 5, Shadowland 4 (18 hours)."
        ),
        "contact_skills": ["Uptown wetwork", "Line to Adam Shepherd and the ghoul underworld"],
    },
    {
        "name": "Adam Shepherd",
        "role": "Born Eric Steward -- sane ghoul multimillionaire, CEO of Agrippa, patron of the Retreat, and would-be Multitech board member by blackmail",
        "archetype": "Corporate Executive",
        "title": "CEO, Agrippa and Associates; master of the Retreat (born Eric Steward)",
        "race": "Ghoul",
        "gender": "Male",
        "organization": "Agrippa and Associates",
        "connection": 5,
        "description": (
            "A typical businessman at first glance; closer, something is not quite right. A lightly "
            "scarred face with the sheen of extensive plastic surgery, expensive suits that do not sit "
            "right on a gangly frame, heavy cologne that masks a peculiar odor. Disarmingly polite, a "
            "persuasive speaker who wants more than anything to prove his people are capable of civilized "
            "behavior and considers himself the exemplar of the best side of ghoul nature."
        ),
        "background": (
            "Eric Steward was good-looking, intelligent, born to privilege, an investment broker fresh "
            "from an exclusive prep school when he goblinized in 2021 into a foul being that craved flesh "
            "and could not bear sunlight. Years feral in the underworld, then sanity, then acceptance of "
            "what he was. He collected the valuables his people had hoarded, invested them, became a "
            "wealthy businessman under a manufactured identity, bought the floundering Agrippa through "
            "Berkley Management, replaced its payroll with ghouls, built the Retreat, and bought the "
            "Hammond Necroplex's dead for their table -- with a bribe and a blackmail of the director's "
            "simporn. His scientists cracked the ghoul/cyberware interface. Now he holds every blueprint "
            "but one, and a seat on Multitech's board would make him one of the most powerful men in the "
            "city."
        ),
        "notes": (
            "Stats p.69: B5 Q3 S4 C4 I5 W6 E5 R4, Init 4+1D6, Threat/Professional 6/3; Enhanced Senses "
            "(hearing, smell); Allergy (Sunlight, Mild -- Moderate for every other ghoul), Reduced Senses "
            "(Blind); Firearms (Pistol) 3, Etiquette (Corporate) 6, Etiquette (Street) 6, Leadership 7, "
            "Negotiation (Bargain) 5, Psychology (Group Behavior) 4; Browning Max-Power, Voice Mask 5, "
            "pocket computer with printer (gear column merged with Vanian's). The book never explains "
            "how a blind ghoul passes in a boardroom -- surgery, cologne and the voice mask do the work. "
            "Sent his people to the sewers after the massacre; hired Clean Steve for the print and for "
            "revenge; authorized 50,000 nuyen; will hire the runners himself if Erin cannot. Calls a "
            "cease-fire if a dozen ghouls die; refuses the prints unless his people are threatened or "
            "the Retreat is about to be exposed. A deal between him and Alpha Blue is worth 8 Karma."
        ),
        "contact_skills": ["Ghoul community and the sewer underworld", "Waste-management contracts and real-estate fronts"],
    },
    {
        "name": "Nelson",
        "role": "Sane, self-taught ghoul hermetic mage; Shepherd's most loyal follower and successor as master of the Retreat",
        "archetype": "Hermetic Mage",
        "title": "Ghoul mage of the Retreat; successor-designate to Adam Shepherd",
        "race": "Ghoul",
        "gender": "Male",
        "organization": "Agrippa and Associates",
        "connection": 2,
        "description": (
            "One of the lucky few ghouls to survive goblinization with his sanity intact, and one of the "
            "very few dual-natured beings who is magically active. A competent mage despite no formal "
            "training, taught from hermetic texts Mr. Shepherd acquired for him. Believes strongly in "
            "better treatment for ghouls and will do anything to see justice done."
        ),
        "notes": (
            "Stats p.57: B7 Q5x4 S6 C1 I4 W5 E(5) M7 R4, armor 0/3, Init 4+1D6, Threat/Professional 4/3; "
            "Enhanced Senses (hearing, smell), Allergy (Sunlight, Moderate), blind; Biotech (First Aid) "
            "3, Conjuring (Elemental) 4, Etiquette (Street) 4, Firearms (Pistols) 3, Magic Theory 3, "
            "Sorcery (Spellcasting) 5; Barrier 4, Chaotic World 6, Hellblast 5, Power Bolt 6, Treat 5; "
            "armor clothing, Browning Max-Power with laser, Power Focus 2, Power Bolt focus 3. Slated "
            "to succeed Shepherd as director of Agrippa and master of the Retreat -- the man to talk to "
            "if Shepherd dies."
        ),
    },
    {
        "name": "Gog and Magog",
        "role": "Shepherd's two cyber-enhanced ghoul razorbrutes -- sedated, skillwired meat puppets in heavy armor who obey without thought",
        "archetype": "Bodyguard",
        "title": "Personal bodyguards to Adam Shepherd (two cybered ghouls)",
        "race": "Ghoul",
        "gender": "Male",
        "organization": "Agrippa and Associates",
        "connection": 1,
        "description": (
            "Two razorbrutes who owe their stopping power to Shepherd's experiments in cybering ghouls. "
            "Goblinization makes most ghoul nervous systems a poor interface for cybertech, and the "
            "feedback drives them madder; Shepherd's scientists solved it with sedatives and modified "
            "skillwires so the cybered ghouls react on encoded expertise rather than their own warped "
            "minds -- unthinking meat puppets who mindlessly obey their master."
        ),
        "notes": (
            "Stats p.56 (each): B7 Q5x4 S6 C1 I4 W5 E(3) R4(6), armor 8/6, Init 6+2D6, Threat/Professional "
            "6/4; Enhanced Senses (hearing, smell), Allergy (Sunlight, Moderate), blind; Armed Combat 4, "
            "Firearms 3, Unarmed (Implants) 5; ActiveSofts (Firearms 3, Unarmed 4), dermal plating 1, "
            "Skillwires 7, spurs, Wired 1; AK-97, heavy armor. Seldom far from Shepherd's side unless he "
            "sends them to dispose of uninvited visitors."
        ),
    },
    {
        "name": "Thaddeus Sinclair",
        "role": "Guilt-ridden Hammond Necroplex director who sold the dead to a voice on the vidphone and is hiding from the spirit that answered",
        "archetype": "Corporate Executive",
        "title": "Director of Operations, Hammond Group (Hammond Necroplex)",
        "race": "Human",
        "gender": "Male",
        "organization": "Hammond Group",
        "connection": 2,
        "description": (
            "A desperate man who tries at first to keep up the image of a tough corporate boss and, "
            "confronted with his crimes, breaks down, confesses, and cooperates in any way the runners "
            "wish. He knows that sooner or later the spirit he offended will catch up with him, and hides "
            "in his top-floor office with a hired bodyguard."
        ),
        "background": (
            "Facing bankruptcy, he took an anonymous vidphone patron's offer of handsome payment for fresh "
            "bodies deposited at a nearby sewer entrance -- helped along by the patron's promise not to "
            "publicize certain sexually explicit simsense recordings his hirelings had found. Spent a "
            "sizable chunk of the patron's loans on paranoid computer security. Knows his silent partner "
            "only as Berkley Management. Stopped selling the night Gallowgrey killed thirteen of his "
            "staff and spared him."
        ),
        "notes": (
            "Stats p.50: B2 S2 C4 I4 W3 E5 R4, Init 4+1D6, Threat/Professional 2/2; Computer 3, "
            "Etiquette (Corporate) 5, Leadership 3, Negotiation 4; chipjack, datasoft link, display "
            "link, fingertip compartment, telephone. Says nothing about the simporn. Regular 50,000-nuyen "
            "payments from Berkley Management to his personal account sit in DS-6. Bodyguard: T/P 3/3, "
            "Init 4+1D6; Armed Combat 3, Firearms 4, Unarmed 3; Predator with laser, armor jacket; "
            "fights only enough to satisfy his employer."
        ),
    },
    {
        "name": "Eric Lane",
        "role": "Ex-Lone Star security chief of the Hammond Necroplex who coordinates his spooked guards from behind his office door",
        "archetype": "Security Chief",
        "title": "Security Chief, Hammond Necroplex",
        "race": "Human",
        "gender": "Male",
        "organization": "Hammond Group",
        "connection": 2,
        "description": "Well-trained but only slightly more effective than the men under him: a three-year Lone Star hitch, then out on his own as a security consultant. Refuses to endanger himself and coordinates his underlings from the relative safety of the security office.",
        "notes": "Stats p.49: B5 Q5 S4 E6 R4, armor 5/3, Init 4+1D6, Threat/Professional 3/3; Armed Combat 3, Etiquette (Corporate) 3, Firearms 4, Leadership 3, Unarmed 3; Predator, armor jacket, club, restraints. His terminal in the security office is one of the system's two back doors (I/OP-3). The alarm he sounds brings six Lone Star officers under contract.",
    },
    {
        "name": "Gallowgrey",
        "role": "Free tomb spirit of the Hammond Necroplex -- a gaunt mortician whose mouth does not move -- avenging the corpses in his care",
        "archetype": "Free Spirit",
        "title": "Free tomb spirit (the first known to achieve freedom); bound to the Hammond pyramid",
        "race": "Free Spirit",
        "gender": "Male",
        "connection": 1,
        "description": (
            "A white-haired, pale-faced, gaunt mortician in a black suit, easily mistaken for an employee "
            "until you notice that his mouth does not move when he talks, or get close enough to see the "
            "strange green glow in his eyes. Exists primarily in astral space and manifests only to "
            "attack. Grim, eerie, disquieting."
        ),
        "background": (
            "Jasper Hammond built his necroplex without consulting a magician, over a locus of shamanic "
            "energy; years of burial ceremonies inadvertently summoned a free spirit of immense power, a "
            "unique entity -- a tomb spirit, the first known to achieve freedom (similar creatures are "
            "rumored in other burial grounds). When he realized the staff were defiling the corpses in "
            "his care he systematically slaughtered everyone on duty that night. The press called it the "
            "Hammond Massacre; the company called it a chemical accident."
        ),
        "notes": (
            "Stats p.52: B8 Q9 S5 C7 I7 W7 E22(28), Init 22(28)+1D6 (manifest/astral); Essence Drain, "
            "Fear, Immunity to Normal Weapons, Manifestation, Paralyzing Touch, Petrifying Gaze, Search. "
            "Attacks anyone he believes threatens his 'children'; returns to the astral if convinced the "
            "team means the dead no harm (hard after prying open tombs). Bound to the pyramid, so easily "
            "avoided by those who know the score. Clever, persuasive runners who know of Shepherd can "
            "turn him loose on the ghoul responsible -- he may wipe out the Retreat, and the GM must "
            "improvise a new climax."
        ),
    },
    {
        "name": "Baxter Attaway",
        "role": "'Judas Caine' -- frustrated actor selling the vampire fad to rich bored kids as owner of Club Nosferatu; Clean Steve's trusted friend",
        "archetype": "Club Owner",
        "title": "Owner, Club Nosferatu (public persona \"Judas Caine\")",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "In public the gloomily handsome, I-dare-you-to-end-my-ennui Judas Caine, who plays the game "
            "better than any of the dark and droopy vampire wannabes and has started a rumor that Caine "
            "is a real vampire. Nothing could be further from the truth. Nobody finds his clientele more "
            "ridiculous than he does; he means to close up shop the moment the fad crests, and amass a "
            "small fortune until then."
        ),
        "notes": (
            "Stats p.54: B3 Q3 S3 C6 I5 W5 E5 R4, armor 0/3, Init 4+1D6, Threat/Professional 4/2; Biotech "
            "(First Aid) 3, Computer 4, Etiquette (Street) 5, Firearms (Pistols) 4, Negotiation 5, "
            "Psychology 4, Unarmed 3; datajack, retractable spur, telephone, voice modulator (spooky "
            "rasp); armor clothing, Browning Max-Power with laser and silencer. Clean Steve's messages "
            "come through 'Caine'."
        ),
        "contact_skills": ["Messages to Clean Steve", "The poser club scene"],
    },
    {
        "name": "Rico",
        "role": "Retired mercenary rebuilt piece by piece until he stopped recognizing himself; Club Nosferatu's courteous bouncer, card sharp and ladies' man",
        "archetype": "Bouncer",
        "title": "Bouncer / troubleshooter, Club Nosferatu",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": "A consummate professional, courteous and efficient, something of a ladies' man, and an unbeatable card player with the fastest shuffle in the sprawl. Worked as a mercenary for years and had a local ripperdoc make him better than whole every time he took a wound; when he ceased to recognize himself he retired to the door of Club Nosferatu.",
        "notes": "Stats p.54: B6(8) Q6 S6 C4 I4 W5 E1 R5(9), armor 6/4, Init 9+3D6, Threat/Professional 7/4; printed skills duplicate Baxter's (Biotech 3, Computer 4, Etiquette (Street) 5, Firearms (Pistols) 4, Negotiation 5, Psychology 4, Unarmed 4) -- a paste error; treat Firearms and Unarmed as his trade. Both arms cyberlimbs with Increased Strength 2, hand razors, radio receiver, smartlink, spurs, Wired 2; AK-97, Predator with laser, combat axe (10S), partial heavy armor.",
    },
    {
        "name": "Ariel",
        "role": "Hermetic mage of unknown name and origin who wards Club Nosferatu's office and once dated Clean Steve",
        "archetype": "Hermetic Mage",
        "title": "Magical security, Club Nosferatu (Rico's assistant)",
        "race": "Human",
        "gender": "Female",
        "connection": 3,
        "description": "No one knows her real name or where she came from, and no one doubts her talent. Gifted at conjuring, she chose hermetic magic because its logical, ordered style suited her. Maintains the astral barrier over the club's office and watches astral space for intrusion. Clean Steve trusts her implicitly.",
        "notes": "Stats p.55: B3 Q6 S3 C6 I6 W6 E6 M6(9) R6, Init 6+1D6, Threat/Professional 5/3; Biotech (First Aid) 3, Computer 4, Conjuring (Elemental) 6, Etiquette (Corporate) 4 / (Street) 5, Firearms (Pistols) 3, Magic Theory 5, Negotiation 5, Psychology 4, Sorcery (Spellcasting) 6, Unarmed 3. Spells: Armor 4, Barrier 5, Chaos 5, Chaotic World 4, Combat Sense 4, Detect Enemies 5, Detect Guns 6, Increase Reflexes 4, Invisibility 5, Mana Barrier 5, Mana Dart 5, Mana Missile 5, Mind Probe 4, Ram 4, Sleep 6, Treat 5. Armor jacket, Power Focus 3, spell foci Detect Enemies 3 and Detect Guns 3.",
        "contact_skills": ["Hermetic wards and astral security", "Elemental conjuring"],
    },
    {
        "name": "Jack Stone",
        "role": "Former cop running Gibson Hall's part-time security for a quiet paycheck",
        "archetype": "Security Chief",
        "title": "Security Chief, Gibson Hall",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": "A former cop who went into private security for a regular paycheck with as little risk as possible, and usually gets exactly that. A bit more talented than his strutting part-timers; the runners may put a cramp in his retirement plans.",
        "notes": "Stats p.15: B4 Q5 S4 C3 I3 W5 E6 R4, armor 4/3, Init 4+1D6, Threat/Professional 4/3; Armed Combat 3, Etiquette (Corporate) 4, Firearms 4, Interrogation 3, Leadership 3, Unarmed 3; Ares Predator with laser, armored vest with plates. Runs eight guards who patrol in pairs after hours.",
    },
    {
        "name": "Leary",
        "role": "Radical independent researcher next door to Neil's lab, building a device to browse organic memory; a contact if the team saves his equipment from the bomb",
        "archetype": "Researcher",
        "title": "Independent researcher, Gibson Hall (lab adjacent to Room 213)",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "Thrown out of several universities and discharged from three respectable corporations for "
            "his radical ideas, Leary went it alone on his savings. He is developing a device that "
            "interacts with organic memory the way computers interact with data -- specialized browse "
            "programs to search the subconscious for facts the conscious mind cannot reach. Refuses to "
            "leave without his apparatus; convinced, begs for help evacuating it."
        ),
        "notes": (
            "Stats p.18: B5 Q2 S4 C4 I6 W5 E4 R4, Init 4+1D6, Threat/Professional 2/2; Biology 5, Biotech "
            "7, Computer 6, Computer Theory 5, Cybertechnology 8, Electronics 7, Firearms 3, Physical "
            "Sciences 4, Unarmed 3; chipjack, datajack, datasoft link, display link, 150 Mp. Knew Neil in "
            "passing -- lunch a couple of times. Can do little for the team now; a potentially valuable "
            "contact later, and a hook (memory-browsing tech) worth a whole run."
        ),
        "contact_skills": ["Cybertechnology and biotech research", "Experimental memory/neural interface tech"],
    },
    {
        "name": "Detective Rick Gordon",
        "role": "Middle-aged Lone Star survivor cop, chromed on borrowed life insurance, going through the motions on the Neil Scott killing",
        "archetype": "Police Detective",
        "title": "Detective, Lone Star Security (investigating officer, Leopold and Loeb)",
        "race": "Human",
        "gender": "Male",
        "organization": "Lone Star Security",
        "connection": 3,
        "description": (
            "A survivor who has worked the streets for years: whenever things got tough he borrowed "
            "against his life insurance and told his surgeon to make him tougher. A middle-aged cop who is "
            "walking bad news, respected and feared by criminals and fellow cops alike. Undue curiosity "
            "about a murder makes him suspicious."
        ),
        "notes": (
            "Stats p.27: B3(4) Q4 S3 C5 I6 W6 (Essence/Reaction garbled), Init 7+2D6, Threat/Professional "
            "5/4; Biotech (First Aid) 4, Car 4, Computer 3, Etiquette (Corporate) 4 / (Street) 5, Firearms "
            "(Pistol) 5, Interrogation 4, Leadership 6, Psychology (Deviant) 4, Unarmed 4, Police "
            "Procedures 5; dermal plating 1, cybereyes (thermographic, flare, low-light, camera), radio "
            "receiver, smartlink, telephone, Wired 1; Predator with laser, armor vest 3/2, restraints. "
            "Talks only to people who say who they are and why they care; Negotiation (Fast Talk) (5) or "
            "a couple of hours in a cell with no charges that stick. Knows it is a corp hit and cares "
            "nothing for Neil -- the Mayor's Office is leaning on the Star over the cousin in the "
            "look-alike Jackrabbit. His ballistics and the sniper's saliva will name the shooter in days."
        ),
    },
    {
        "name": "Mortimer",
        "role": "Desperately friendly window-watcher at Leopold and Loeb who knows everything and nothing, and invents a red-eyed ork sniper",
        "archetype": "Neighborhood Busybody",
        "title": "Neighbor, Leopold and Loeb",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": "A lonely man who spends most of his time at his window watching the countless dramas of his little corner of the sprawl. Everyone says he knows everything that goes on; the cops know he is full of hot air and never question him. Not only will he talk, it is almost impossible to make him stop.",
        "notes": "Stats p.28: Q5 S3 (rest garbled), Init 3+1D6, Threat/Professional 1/1; Armed Combat 3, Etiquette (Street) 4, Firearms 3, Unarmed 3; club. Claims a good look at the sniper: a big male ork with one red cybereye and light body armor under a long black coat -- invented. Humor the wild goose chase; the team may even find an innocent, angry ork who matches.",
    },
    {
        "name": "Balder",
        "role": "Gordon Tufnell -- immense loincloth-and-rivets troll doorman of the Route 66 blitz who decides who's hot and who's history",
        "archetype": "Bouncer",
        "title": "Doorman, Route 66 blitz club (aka Gordon Tufnell)",
        "race": "Troll",
        "gender": "Male",
        "organization": "Route 66 (blitz club)",
        "connection": 2,
        "description": (
            "Immense even for a troll, sculpted with special equipment into a musclebound nightmare, "
            "wearing only a loincloth with studs riveted into his hide. No armor, no weapons, but the "
            "telltale scars and bulges of heavy dermal plating and the housings of his spurs and razors "
            "are on open display. Prefers rough trade and attractive young people for the tough "
            "customers to ogle; dress tough or sleazy and he waves you through."
        ),
        "notes": "Stats p.32: B11(14) Q3 S9 C3 I3 W5 E1 R3(7), Init 7+3D6, Threat/Professional 5/3; Armed Combat 3, Etiquette (Street) 4, Firearms 3, Interrogation (Verbal) 4, Unarmed (Implants) 5; dermal plating 3, hand razors, spurs, Wired 2. Bribable, but do not underestimate the value of his endorsement. Points the team at the Legion punks in chains and warpaint.",
    },
    {
        "name": "Overdrive",
        "role": "Respected Iron Legion warrior promoted to lieutenant hours ago by the massacre; grunts, bristles, and takes the job seriously",
        "archetype": "Gang Lieutenant",
        "title": "Lieutenant, Iron Legion",
        "race": "Human",
        "gender": "Male",
        "organization": "Iron Legion",
        "connection": 2,
        "description": "In the good old days a respected warrior who followed where others led. In the few hours since the massacre he has become the Legion's new lieutenant, uncomfortable with the responsibility and taking it very seriously. A lousy conversationalist who bristles with attitude and grunts at even the simplest question; lays down the law for his remaining brothers.",
        "notes": "Stats p.33: R4, Init 4+1D6, Threat/Professional 4/3; Armed Combat 3, Etiquette (Street) 4, Firearms 4, Interrogation 3, Leadership 3, Unarmed 3; Ares Predator, club, HK227, synthleather 0/1. Suspects anyone asking about Breaker of being with the hit squad; allay that and he tells the team Breaker was tortured to death a few hours ago in a professional hit, knows nothing of the eye, and names Emma in Hope.",
    },
    {
        "name": "Breaker",
        "role": "Iron Legion soldier who cut Griffin Moore's cybereye from a half-eaten skull and sold it to Rat Vanian; tortured to death by Clean Steve (deceased)",
        "archetype": "Gang Member",
        "title": "Soldier, Iron Legion (deceased)",
        "race": "Human",
        "gender": "Male",
        "organization": "Iron Legion",
        "connection": 1,
        "description": "Chains and warpaint tagged him as a Legion soldier; he strutted into Vanian's shop puffed up like he had knocked over Aztechnology, grinning like he had the grail in his duffel bag, and unwrapped a cybereye from a wad of bloody napkins. Wanted to come off like a player and did not have a clue.",
        "background": "Harvested the eye with a deft stroke of a penknife while the Legion waded through the blood and shell casings of their ghoul hunt. Spent some of the nuyen from 'biz with the boys' furnishing his girlfriend Emma's doss in Hope. Met her at a blitz club a year ago.",
        "notes": "Vanian's security cameras have his portrait. Tortured to death by Clean Steve during the professional hit on the gang. Emma is the only person he told where the eye came from.",
    },
    {
        "name": "Emma",
        "role": "Breaker's girlfriend, a street kid who recorded cheap simporn; two days into a looped simsense of their vacation with the safeties pried out",
        "archetype": "Gang Member",
        "title": "Breaker's girlfriend; former simporn performer (Hope, Puyallup Barrens)",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": (
            "Sprawled across a beanbag chair hooked to a battered simsense deck, breathing slowly, eyes "
            "rolled back, a rhythmic twitch in her left arm. Everything about her reeks of surrender. "
            "Born to parents who abandoned her early to the streets; matured fast, ran the sprawl for "
            "years, found steady work recording cheap simporn, and met Breaker at a blitz club a year "
            "ago. They fell in love."
        ),
        "notes": (
            "Gang Member archetype (SRII p.57), frail. When the Legionnaires told her Breaker was dead "
            "she spliced a simsense of their vacation into a continuous loop, disabled the deck's safety "
            "features with an icepick and tuned out; 48 hours without sleep, food or water have brought "
            "her close to death. Pulling the plug is easy; reviving her is not. Patience and sympathy, "
            "and any cover story ('friends of Breaker's'), get the truth: Lone Star hauled in three "
            "gangers a couple of weeks back, the gang went ghoul-hunting for bail, Breaker found the eye "
            "on a half-eaten corpse in the ghouls' sewer lair; revived enough to travel she can show the "
            "manhole. Kill her cat and she never cooperates."
        ),
    },
    {
        "name": "Savage Harvey",
        "role": "Emma's talis cat -- a fat, lazy white housecat that becomes a cheetah, never tamed, feeding on derelicts by night",
        "archetype": "Paranormal Animal",
        "title": "Talis cat (Emma's pet)",
        "race": "Talis Cat",
        "gender": "Male",
        "connection": 1,
        "description": "Looks like a fat, white, long-haired housecat, stupid and lazy. Hisses at intruders; anyone who comes close finds a cheetah baring its fangs. Emma adopted him as a kitten during her years on the street and never fully tamed him; unknown to her, he crawls out at night and feeds on luckless derelicts who wander into Hope -- the 'savage cat' the locals fear.",
        "notes": "Stats p.37: housecat B1 Q4x4 S1 R4(6), Init 5+1D6; cheetah B7 Q9x4 S7, Init 5+4D6, 8S bite; Desire Reflection (self, cheetah only), Enhanced Movement, Enhanced Physical Attributes, Enhanced Reactions, Enhanced Senses (low-light), Illusion (a Mask 12; one action to shift). Attacks if he thinks Emma is in danger. Easy to kill for a well-armed team, and killing him loses any shot at Emma's cooperation.",
    },
    {
        "name": "Bennie and June",
        "role": "Twin trolls too stupid and volatile to bounce, now VIPs of Hope leading its ragtag pack of hungry thugs",
        "archetype": "Thug",
        "title": "Leaders of the Hope thug pack (twin trolls)",
        "race": "Troll",
        "gender": "Male",
        "connection": 1,
        "description": "Outcasts everywhere else, VIPs in Hope. After they proved too stupid and volatile to work as bouncers the twins drifted downside and found their niche leading the ragtag group of thugs that hunts this filthy corner of the sprawl. Hot tempers; cash only; any concession looks like weakness and invites more abuse.",
        "notes": "Stats p.36 (each): B8 Q4 S7 C2 I2 W3 E6 R3, salvaged armor 3/1, Init 3+1D6, Threat/Professional 5/2; Armed Combat (Clubs) 4, Etiquette (Street) 3, Firearms (Pistols) 3, City Speak 3, Unarmed 3; Browning Max-Power, club. Lead twice as many thugs as there are runners and demand an exorbitant finder's fee to show the way to Emma. Fight is the likelier outcome; a beaten thug gives directions.",
    },
    {
        "name": "Abbott",
        "role": "Rotund troll in a hooded monk's alb, disowned corporate heir turned bodyguard and devotee of the blind mage Alegheri",
        "archetype": "Bodyguard",
        "title": "Bodyguard to Alegheri ('Teacher'), Seattle sewers",
        "race": "Troll",
        "gender": "Male",
        "organization": "Lost Boys",
        "connection": 2,
        "description": "An unusually large, rotund troll in a brown monk's alb with a deep hood that hides his goblinized features, who accosts visitors on the approach to the cistern and questions them before they may see 'the master'. Sole heir to a small corporate fortune before the Awakening made him a hulking monstrosity; his patrician family disowned him, the money ran out, and the Lost Boys found him on the street and took him to Teacher, to whom he has devoted his life.",
        "notes": "Stats p.46: B8 Q3 S7 I3 E6 R3, salvaged armor 4/2, Init 3+1D6, Threat/Professional 6/3; Armed Combat (Clubs) 5, Athletics 5, Etiquette (Street) 3, Firearms (Pistols) 4, Stealth (Urban) 4, Unarmed 5; Ares Predator. Sees out anyone who presses Teacher about the drawings.",
    },
    {
        "name": "Alegheri",
        "role": "'Teacher' -- blind hermetic master, born Gideon Alexander, who gouged out his own eyes after Experiment 231 and hides from the hungry sky in the sewers",
        "archetype": "Hermetic Mage",
        "title": "\"Teacher\" of the Lost Boys; blind hermetic mage (born Gideon Alexander)",
        "race": "Human",
        "gender": "Male",
        "organization": "Lost Boys",
        "connection": 4,
        "description": (
            "An aged, blind mage, friendly and exceptionally intelligent, who listens more than he talks "
            "and measures every word; he addresses himself to any hermetic mage in the team. Through an "
            "impressive information network of sighted followers and admirers he knows everything that "
            "happens in the sewers though he sees nothing. Ask about the drawings on his walls or why he "
            "hides and he evades, then starts taking them down; press and he grows agitated and has "
            "Abbott show you out."
        ),
        "background": (
            "As young Gideon Alexander his groundbreaking research into the nature of astral space "
            "provided much of the basis for modern magical theory. Intrigued by magicians' inability to "
            "leave the biosphere, he reasoned that those who died or lost their magic trying were "
            "novices, and after years of preparation conducted Experiment 231, the first controlled "
            "attempt at astral travel beyond the biosphere. When he regained consciousness he gouged out "
            "his eyes with his bare hands; no one knows what he saw. He refused vat-grown eyes -- he had "
            "no intention of seeing it again -- and over months and years came to fear that the open sky "
            "wanted to swallow him. After decades of therapy he fled the surface, took a new name, and "
            "earned the respect of the underworld. The walls of his cistern are covered with primitive "
            "drawings of a reptilian face in a nimbus of stars."
        ),
        "notes": (
            "Stats p.46: Init 5+1D6, Threat/Professional 6/3; Biotech 4, Conjuring 4, Etiquette (Street) "
            "6, Magical Theory 8, Sorcery 8 -- without vision he cannot wield magic and has had no desire "
            "to since. In this adventure he can only confirm the ghouls' withdrawal and growing ferality, "
            "the Legion raid, and the second, non-ganger search party three days later, and point the "
            "team to the hunting ground. A runner who befriends him over regular visits may one day be "
            "told what he saw. A campaign-sized hook: whatever is out past the biosphere has a face."
        ),
        "contact_skills": ["Everything that happens in the Seattle sewers", "Astral-space theory (the foundations of modern magical theory)"],
    },
]

ORG_UPDATES = {
    "Lone Star Security": {
        "notes_append": (
            "Eye Witness (2055): the Neil Scott murder at Leopold and Loeb is Detective Rick Gordon's "
            "case, worked only because a cousin of the city's chief executive (the book says 'Mayor "
            "Schultz') was a block away in a look-alike Jackrabbit; ballistics (FN HAR, explosive rounds), "
            "thermographic footprints and the sniper's saliva on seed shells will identify Multitech's "
            "shooter in days. Alpha Blue has friends inside who can slow the investigation and leak the "
            "initial report. Two troopers per cruiser at the scene (Firearms 4, Police Procedures 3, "
            "Predator, armor jacket, club). Recently jailed three Iron Legionnaires for black-market "
            "BTLs -- the bail money is why the Legion went ghoul-hunting. Rat Vanian's 'donations' to his "
            "local stationhouse buy two fast cruisers for his shop. The Hammond Necroplex keeps a costly "
            "Lone Star contract (six nervous officers who shoot first around the 'ghost'). Raids the "
            "Route 66 blitz at Brighton Mall, falls back under fire and floods the mall with tear gas. "
            "Administers the city's ghoul bounty: 100 nuyen per male, 150 per female."
        ),
        "leadership_add": [
            {"name": "Detective Rick Gordon", "title": "Detective (homicide)", "notes": "Eye Witness; investigating officer, Neil Scott killing."},
        ],
        "enemies_add": ["Iron Legion"],
    },
    "Fuchi Industrial Electronics": {
        "notes_append": (
            "Eye Witness (2055): one of Multitech International's biggest customers for short-run custom "
            "components (with Henderson Multicom and Magnuson) -- and a candidate victim of the "
            "deliberately flawed MPCP optical chip. Fuchi hardware is everywhere in the book: Neil Scott's "
            "Fuchi Cyber-4 and chip library in Gibson Hall, and the Fuchi Cyber-VI decks (MPCP 8, "
            "Hardening 4, Attack 6, Mirrors 2, Shield 2) of Multitech's watchdog deckers. Neil's "
            "load-speed-15 Allegiance hack 'might be adapted for a more agile deck such as a Fuchi'."
        ),
        "allies_add": ["Multitech International"],
    },
    "Yakuza (Watada-rengo)": {
        "notes_append": (
            "Eye Witness (2055): among the exotica in Rat Vanian's Redmond storeroom is an intricately "
            "carved, silk-lined wooden box holding a handmade pearl-handled black pistol with matching "
            "silencer and five rounds (Ares Viper Slivergun stats); Etiquette (Street) (5) with 2 "
            "successes recognizes yakuza symbols in the carving. 'A smart player character will leave it "
            "be' -- somebody will come asking for it. Clean Steve is known to Yakuza Boss contacts."
        ),
    },
}

LOC_UPDATES = {
    "The Barrens (Seattle)": {
        "notes_append": (
            "Eye Witness (2055): the Puyallup Barrens slum called Hope -- ruined buildings and duct-taped "
            "prefab modules built by people who wanted to disappear, no addresses, no inspectors, no cops, "
            "residents scavenging the nearby soy plant -- is where Breaker's girlfriend Emma lives (see "
            "Hope). Under the whole sprawl the sewers hold ghoul enclaves (some under Adam Shepherd's "
            "protection), the Lost Boys and the blind mage Alegheri; the city's ghoul bounty (100/150 "
            "nuyen) sends gangs like the Iron Legion down the manholes."
        ),
    },
}

NPC_UPDATES = {
    "Governor Schultz": {
        "notes_append": (
            "Eye Witness (2055): the book refers to 'Mayor Schultz' -- treat as the same office-holder. A "
            "cousin of Schultz's happened to be a block from the Leopold and Loeb intersection, driving a "
            "Jackrabbit nearly identical to Neil Scott's, when the sniper fired; the executive office fears "
            "the cousin was the target and is leaning on Lone Star, which is leaning on Detective Rick "
            "Gordon. That pressure is the only reason a nobody's murder gets a full crime-scene team."
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
**1. Gibson Hall building system** (p.15-16). UMS geometric imagery; every floor's labs hang off their
own SPU; any intrusion is likely to trip alerts in several nodes; an active alert shuts the whole
system down within three Combat Turns. Neil's own equipment is NOT on it (DS-2 holds dummy duplicate
files to make it look as if he used it; I/OP-2 is the one Room 213 terminal, used only to talk to the
landlord; SM-2 controls none of his gear). A Matrix run here is a mistake -- worth building only as a
decoy host.

| Node | Function | Rating / IC |
|---|---|---|
| SAN | Public access | Orange-4, Access 6 |
| SPU-0 | Gateway and data junction between SAN, SPUs and CPU | Orange-6, Access 7, Trace and Report 7 |
| SPU-1 / SPU-3 / SPU-4 | First / third / fourth floor lab traffic | Orange-4, Access 5, Trace and Report 6 (each) |
| DS-1, I/OP-1, SM-1 (and -3, -4) | Per-floor datastore, terminals, slaved lab equipment | Orange-5, Access 5 (each) |
| SPU-2 | Second floor (Room 213) traffic | Orange-4, Access 5, Trace and Report 6 |
| DS-2 | Dummy files for Room 213 | Orange-5, Access 5 |
| I/OP-2 | One Room 213 terminal (landlord comms) | Orange-5, Access 5 |
| SM-2 | Second-floor equipment (none of Neil's) | Orange-5, Access 5 |
| CPU | Nothing runs off it directly | Red-6, Access 7, Trace and Burn 8 |
| SPU-5 | Security | Orange-6, Access 7, Tar Pit 7 |
| DS-5 / I/OP-5 / SM-5 | Security datastore, terminals, hardware | Orange-5, Access 6, Trace and Report 6 (each) |

**2. Neil Scott's isolated mainframe** (p.16). A small separate system of Neil's own design, not
connected to the Matrix -- a mini-matrix reached only by jacking in inside Room 213 (before the bomb
goes off). Active alert = shutdown in three turns. Small, and the paydata is the point.

| Node | Function | Rating / IC |
|---|---|---|
| SPU | Junction | Orange-4, Access 5, Trace and Report 6 |
| DS-1 | Data dump, nothing important | Orange-5, Access 5 |
| I/OP | Three terminals and the room's datascreens | Orange-5, Access 5 |
| SM | All the lab's testing equipment | Orange-5, Access 5 |
| CPU | -- | Red-6, Access 7, Trace and Burn 8 |
| DS-2 | "current projects": BP Botch Bypass (Computer (5): 1 success = incomplete attack program, 2 = absurdly simple, 3+ = it attacks a specific MPCP flaw); BP Comp/Sorted Prints (~100 MPCP optical-chip prints, Computer (6); 20 Mp recent and saleable); Storm Front TD (10 Mp weather-satellite data, red herring) | Orange-5, Access 6, Trace and Report 6 |

**3. Multitech Design, Bellevue branch** (pp.40-41). Redesigned twice; layered SPUs force an intruder
through several tiers of IC before anything that could hurt the company. Only one SAN (a second SAN
for SPU-2 was scrapped for security). Two Major League deckers are always online (Init 6+2D6,
Threat/Professional 5/3, Fuchi Cyber-VI: MPCP 8, Hardening 4, Active 100, Storage 500, Load 50, I/O
30; Bod/Evasion/Masking/Sensors 5; Attack 6, Mirrors 2, Shield 2; Response Increase 1): the first
enters via SPU-6 on a passive alert, the second on an active alert. The blueprints are gone; the prize
is DS-3's dirt and DS-6's personnel files. Griffin Moore's dummy file is black IC with a Trace and
Burn 4 trigger. The physical back door is a terminal in a lab or a senior executive's office.

| Node | Function | Rating / IC |
|---|---|---|
| SAN | Sole Matrix access | Green-5, Access 5 |
| SPU-1 | Public access | Blue-4 |
| I/O-1 | Info-booth touch screens and displays | Blue-4 |
| DS-1 | PR data for the booth | Blue-5, Access 6 |
| SPU-2 | Most system traffic | Green-5, Access 5 |
| I/O-2 | Most terminals in the building | Green-5, Access 5 |
| DS-2 | General files | Green-5, Access 5, Trace and Report 5 |
| SPU-3 | Secure / restricted-access file requests | Orange-5, Access 6, Trace and Burn 6 |
| I/O-3 | Accounting and executive terminals | Orange-5, Access 6 |
| DS-3 | 200 Mp; sift or Evaluate to find evidence of various minor crimes -- blackmail material | Orange-5, Access 6, Tar Baby 7 |
| CPU | -- | Red-5, Access 6, Blaster 7 |
| SPU-4 | Prototype chip-burning equipment | Red-5, Access 6 |
| I/O-4 | Manufacturing and system-control terminals | Orange-5, Access 6 |
| DS-4 | Burner programs, subroutines, layout-file backups | Orange-5, Access 6 |
| SM-1 | Chip-burning and creation equipment | Green-5 |
| SPU-5 | Research and development | Red-5, Access 6, Trace and Report 5 |
| I/O-5 | R&D terminals | Red-4, Access 5 |
| DS-5 | Chip files in progress: 400 Mp, 80 Mp of real value | Red-4, Access 6, Trace and Dump 5 |
| SPU-6 | Security system (deckers enter here) | Red-5, Access 6 |
| I/O-6 | Security office and senior executive terminals | Orange-5, Access 6 |
| DS-6 | Personnel files on every wageslave ever; Donovan -> "transferred to Shanghai" with Shanghai's access number (no passcodes); Griffin Moore dummy file (black IC, Trace and Burn 4 on access) | Orange-6, Access 6, Trace and Dump 6 |
| SM-2 | Interface to the building's security hardware | Orange-5, Access 6, Trace and Dump 6 |

**3b. Multitech Shanghai home office** (p.41): identical architecture with every program rating +1 and a
third decker online, a Heavy Hitter (Init 7+3D6, Threat/Professional 7/4; persona 6/6/6/6; Attack 6,
Mirrors 2, Shield 2; Response Increase 2). Shanghai's DS-5 holds Donovan's corrected chip designs.

**4. Hammond Necroplex system** (p.51). UMS imagery; the paranoid director spent Shepherd's loans on
impressive IC but dispensed with watchdog deckers; active alert = shutdown in three turns. Reachable
from outside or from two protected terminals (security office, director's office) that make the secure
areas much easier. Nothing runs off the CPU; seven SPUs carry all traffic, split into a corporate-office
half and a necroplex-building half.

| Node | Function | Rating / IC |
|---|---|---|
| SAN | Access | Green-5 |
| SPU-1 | Security checkpoint behind the SAN | Orange-6, Access 7, Trace and Report 7 |
| SPU-2 | Junction between the two halves and the CPU | Green-3 |
| SPU-3 | Corporate office, day-to-day traffic | Orange-4, Access 5 |
| I/OP-1 | Corporate office terminals, monitors, printers | Orange-5, Access 6 |
| DS-1 | Unprotected data dump | Orange-5 |
| SPU-4 | Corporate restricted branch | Orange-5, Access 5, Trace and Dump 6 |
| DS-2 | Restricted files | Orange-5, Scramble 6 |
| SM-1 | Air conditioning, elevators, security cameras | Orange-5 |
| SPU-5 | Necroplex building, day-to-day traffic | Orange-4, Access 5 |
| I/OP-2 | Necroplex terminals, monitors, printers | Orange-5, Access 6 |
| DS-3 | Unprotected data dump | Orange-5 |
| SPU-6 | Necroplex restricted branch | Orange-5, Access 5, Trace and Dump 6 |
| DS-4 | Complete interment/cremation records: Griffin Moore, Multitech designer, interred around the time Neil bought the print; his contract and tomb location; keyword search (Multitech, designer, optical chip) | Orange-5, Scramble 6 |
| SM-2 | Elevators, cameras, the eternal-flame gas jets and recorded eulogies | Orange-5 |
| CPU | -- | Red-6, Access 7, Blaster 8 |
| SPU-7 | Executive / records branch | Red-6, Access 7, Tar Baby 8 |
| DS-5 | Personnel: thirteen employees died on the same day, three weeks ago | Orange-5, Barrier 7 |
| DS-6 | Accounting: regular 50,000-nuyen payments from Berkley Management to Thaddeus Sinclair's personal account; Sinclair listed as Hammond Group's Director of Operations | Orange-5, Barrier 7 |
| I/OP-3 | Two terminals: security office and director's office -- the back doors | Orange-5, Access 5, Trace and Burn 6 |

**Not mapped:** Vanian's shop security system (cameras with a Matrix video feeder to his home,
broken at the receiver); Smallville's closed-circuit camera network run from the clubhouse; the
Multitech R&D system Griffin Moore decked in the prologue (the same Bellevue system, from inside).
"""

NOT_BUILT = """
- **Jonathon Ki Won** (President/CEO), **Sir Peter Mathews** (Chairman), **Jasper Hammond** (Necroplex
  founder, status unknown) -- leadership entries on the org rows.
- **Lou** (oriental gentleman, shot three times) and **Graham** (middle-aged technician, explosive
  ammo), Vanian's murdered assistants, and the **third assistant** who opens at sunrise -- on the
  Vanian's storefront row. **Jimmy**, Neil's chatty personality program -- on Gibson Hall.
- **Velvet**, the simsense superstar Alpha Blue guarded until a skillwire scandal -- on Erin's row.
- **The Multitech ringer "Dutch"**, the **Smallville coordinator**, all **troubleshooter, sniper,
  combat-mage, coordinating-officer and guard blocks**, **Stern's two bodyguards**, the **Multitech
  security decker** of the prologue, the **company thug** who ran Moore off the cloverleaf, and the
  **FN HAR sniper** who killed Neil (unnamed; Lone Star will have his name in days) -- stat blocks on
  the Smallville and Bellevue rows.
- **Sinclair's hired bodyguard**, the **Necroplex guards** and the **PR wizboy** with the chemical-accident
  story -- on the Necroplex rows. **Shepherd's technician** with the crowbar, his **scientists**, the
  **enlightened and feral ghouls** and the **watcher spirits** -- on the Retreat / Agrippa rows.
- **The Iron Legion punks**, the **cornered punk on probation**, the **Hope locals**, the **Lost Boys**
  (as individuals), the **feral ghoul family** in the hunting ground -- on their org / location rows.
- **The "mysterious oriental fellow"** who arranges the meet for teams without a fixer; the **funeral
  parlor** itself (unnamed) and its **two hired bruisers**; **Vanian's two street samurai and elven
  mage** rescuers; **Erin's runner friends** shadowing the team; **Schultz's cousin** in the look-alike
  Jackrabbit; **Henderson Multicom** and **Magnuson** (Multitech customers); **SeaSource** (the public
  datanet); the **Brighton Mall stores** (Budda Noir, Victoria's Latex, Hair 'O Rama, Silk Plants, Uncle
  Ogre's Big & Tall, X-pensive Gifts, Nothing Sacred, Nik Nak's, Shoes Shoes Shoes, Book World); the
  **soy plant** by Hope; the **cloverleaf**.
"""

PLAY_NOTES = """
- Time is the engine: the cleanup crew is always one stop ahead (lab bomb, shop killings, staged
  Smallville, the Shady Hill snatch), Clean Steve is one stop behind, and Lone Star's forensics run on
  their own clock. Let Alpha Blue's vidphone rescue the team once, no more.
- Trail: letter -> Gibson Hall (clues, bomb, Leary) -> Vanian's shop (bodies, envelope, Clean Steve)
  -> Shady Hill (Vanian, the eye, ambush) -> serial number / Route 66 -> Emma and the manhole -> Lost
  Boys, Alegheri, the necktie nests and the mourning card -> Hammond (empty tombs, DS-4/DS-6,
  Sinclair, Berkley) -> Agrippa / the Retreat. Smallville and Bellevue are lethal dead ends that exist
  to teach that corporations play smart; Club Nosferatu is an impasse that sets up Clean Steve.
- Two clues connect ghouls to Hammond -- the mourning card and Moore's empty tomb; the team must get
  one. Two hooks to the Retreat -- Berkley's paper trail and the ghouls' own invitation.
- The Iron Legion and the ghouls are both victims; the book wants the screaming ghoul children and
  Emma's surrender to hurt. Shepherd is polite, persuasive, and the only route to the prints:
  kill, steal (kitchen key, safe-deposit box) or blackmail with exposure.
- Fee: GM-set base tuned to the team's lifestyle, then Negotiation; favors and black-market discounts
  as sweeteners. Karma: full set to Alpha Blue 6; Alpha Blue-Shepherd deal 8; bomb / evacuation 1
  (as printed). Ghoul bounty (100/150 nuyen) is a temptation to hand the players.
- Loose ends: Neil's Botch Bypass finished with the prints; Multitech's shooter named by Lone Star;
  Donovan's corrected designs in Shanghai; Gallowgrey loose if turned on Shepherd; Leary's memory
  browser; Alegheri's reptilian face among the stars; a yakuza pistol in a carved box; Clean Steve
  remembers faces.
"""
