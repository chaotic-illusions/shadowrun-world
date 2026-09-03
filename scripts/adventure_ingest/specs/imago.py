# Imago (FASA 7309, 1992, Carl Sargent) -- campaign order #13. Edinburgh, the Isle of Skye, Loch Ness
# and Glencoe, Scotland, U.K., summer 2053. Written for Shadowrun Second Edition; the only Seattle scenes
# are the hiring at the Stouffer-Madison and the newsnet handouts.
# Source text: docs/Adventures/text/Shadowrun 1e - Imago {FASA7309}.txt (84 pages).
# ASCII only (pre-commit hook). Currency in the book is pounds sterling (1 nuyen = 2.45 pounds).
#
# Editing inconsistencies in the book (also noted on the affected rows):
# - Date: the introduction says "The year is 2053" (Quicksilver joined Transys "five years ago" in 2048,
#   met Morag "late in 2052", the weather note wants April-October and the arrival text says "British
#   summer"), but both newsnet handouts carry FASA's recycled template date "Monday October 9 2051" and the
#   U.K. price list is "estimated as of January, 2054". YEAR below follows the book's own text: 2053.
# - Alasdair Cameron is a "young technician", Quicksilver's "research assistant" and a "medical
#   researcher" in different places; the cast page makes him 31 with a Ph.D. in molecular biology.
# - Amelia Richardson is "mid-40s" with "long fair hair" in the text and 42 with light-brown hair on the
#   cast page. Morag is "about 20" in Legwork and "about 19" on the cast page.
# - Two Sir Iains: Sir Iain Greig (ailing Transys President/CEO) and Sir Iain MacDonald (board member).
# - 37 MacDonald ghosts rise at the end; the 1692 massacre text counts 38 dead.
# - The handout calls Harold Gray Bear "Chief of the Salish-Shidhe Council"; Peacekeeper (#8) recorded
#   him as the Council's spokesman.
# - Mad John is "brain-damaged" yet fights at full Wired Reflexes 2; James stores his gear.

ADVENTURE = "Imago"
ORDER = 13
SOURCE = "Shadowrun 1e - Imago {FASA7309}.pdf, pp. 4-80"
YEAR = "2053 (summer)"

SYNOPSIS = """
**Peter Albrecht**, a Seattle fixer who fronts for corporations that will not use their own negotiators,
finds the runners at the Red Lobster in the **Stouffer-Madison** and offers suborbital tickets, expenses
and a miserly 500 nuyen a day to find a missing man in Scotland. The client is **Alasdair Cameron**, a
kilted, red-bearded **Transys Neuronet** technician whose boss and only friend, the elven wetware genius
**Quicksilver**, has been gone two weeks. Cameron gives the team ID codes for the Transys research
subsystem and points them at **Hamish's Bar**. In the bio-organic Transys system every file on
Quicksilver has been purged -- but an amnesic elven **Child** materializes, pleads "Bring me to Amelia",
and vanishes, and a hooded corporate decker ambushes the team on the way out. At Hamish's the team meets
**Duncan the Fixer**, the ork barman **Hamish MacLeod** and the elven research assistant **Fionnghuala
Colquhoun**, who knew Quicksilver as "Erewan", was half in love with him, and remembers "Richardson" and
a druid called Fiona on Skye. **Professor Amelia Richardson** of the University's Occult Sciences
Department, a Seattle expatriate, admits to a friendship and nothing more -- she has Quicksilver's
cyberdeck in her flat.

Then Cameron is found burned to a charred lump in his Queen's Street flat, his arm pointing at the sky.
**Zeta-ImpChem** agents inside Transys killed him with magic to frame the brash Americans, and the
Edinburgh police arrive minutes later. Broke, unarmed and wanted, the runners follow the only lead to
Skye, where the **Druids of Dunvegan** demand that the team's magician give of himself in a midnight
rite inside the stone circle before **Fiona Mac Mhuirich** hands over a sealed black box: the Affect
chip, one of four living biochips into which Quicksilver encoded his personality. The chip slotted into
his deck screams grief without memory. The Memory chip costs Karma and an astral quest to the **Great
Free Spirit of Loch Ness**; it shows a dead elven girl in MacDonald tartan -- **Morag MacDonald**,
daughter of Transys board member **Sir Iain MacDonald**, murdered thirteen days ago at **Castle
Laidon** in Glencoe in what the news called a Campbell feud killing. Her mute ghost walks the great
staircase at midnight; the Perception chip is hidden in her bedroom; the Integrative-Executive chip
fuses out of Amelia's trid horoscope when she keys in the missing Mid-heaven. A Zeta helicopter strike
team hunts the runners across the glen.

Reintegrated, Quicksilver asks one last thing: take the deck to Castle Laidon and let him use a living
decker's soul to leave the machine and die with Morag. The decker is dragged through four stages of
dissolution while Zeta samurai and combat mages storm the castle; if Sir Iain was won over, kilted
MacDonald cavalry arrive by the chopper-load, and the ghosts of Glencoe rise behind the reunited
lovers. Sir Iain takes the deck, sends the survivors home in a private suborbital, and pays in a
Transys Barrie cyberdeck and 75,000 nuyen apiece.
"""

TIMELINE = """
- **2021** -- Quicksilver born on the South Wales coast near the old Nubian/Egyptian temples. **2048** --
  he hacks the Transys Edinburgh CPU and asks for a job. **Late 2052** -- Cameron drags him to a party;
  he meets Morag MacDonald. **Last summer solstice** -- he leaves the Affect chip with Fiona on Skye.
- **Three weeks before** -- Fionnghuala and Amelia last see him ("on his way to see a lover"). **Five
  days before his death** -- the prologue in Amelia's rooms. **Thirteen days before the adventure** --
  Zeta agents in Campbell "Old Colors" murder Morag on the Castle Laidon staircase and gun Quicksilver
  down as he flees; fourteen MacDonalds and servants die; two Campbells are left behind as evidence.
- **Day 1, Seattle** -- Albrecht at the Red Lobster; papers next day. **Day 2** -- suborbital, 1000
  Seattle to 2100 Edinburgh, two hours of Customs; Cameron, the Royal Muirfield, Hamish's Bar.
- **Days 3-5** -- the Transys run and the Child; paperwork, wheels, Angus MacNab; Amelia. **Death in
  Queen's Street** the day the team sets out for Skye; Transys changes its passcodes.
- **Skye** -- flight or fourteen hours by hovertruck; the tourist rite by day, the real one at midnight;
  the Affect chip. **Loch Ness** -- the quest and the Memory chip. **Glencoe** -- Morag's ghost at
  midnight, the Perception chip, the chopper strike. **Edinburgh or Pitlochry** -- Sir Iain. **Amelia's
  horoscope** -- the I/E chip. **Castle Laidon, midnight** -- Set My Soul Free.
- **Ending** -- six months on remand and a "Not Proven" verdict if the team surrendered; otherwise a
  private suborbital home and the news of a Transys boardroom purge (success) or Sir Iain's
  "resignation" and a Zeta-ImpChem takeover bid (failure).
"""

ORGS = [
    {
        "name": "Transys Neuronet",
        "org_type": "corporation",
        "tier": 5,
        "headquarters": "Edinburgh, Scotland (the Meadows complex); labs across the U.K.",
        "summary": "British megacorp -- experimental comms, advanced and medical cyberware, Matrix software; Quicksilver's employer, riddled with Zeta-ImpChem agents",
        "description": (
            "Formed between 2013 and 2017 when four British hi-tech companies merged to stabilize the "
            "British research base against American and Japanese domination. President/CEO Sir Iain "
            "Greig (ailing); principal division Transys Neuronet GB under Johnathan Cooper; the Transys "
            "Group home office is in Edinburgh, Scotsprawl -- 'that place in Scotland, what's it called, "
            "Silicon Glen'. Products: experimental communication systems, lasers, advanced cyberware, "
            "Matrix software, neural skillsofts and medical cyberware; European medical-cyberware share "
            "up from 11 to 24 percent in five years; a network of small U.K. labs doing military, medical "
            "and personal-enhancement research for clients. Holds Lord Protector's permits for a versatile "
            "range of intrusion countermeasures. Very secretive, very hi-tech, with a lot of infighting "
            "among the higher-ups. Owns a couple of hostelries on the east coast of Skye. In 2048 an elf "
            "calling himself Quicksilver hacked past the most vicious IC in existence into the CPU of the "
            "Transys Edinburgh system and asked for a job; his salary quickly became astronomical."
        ),
        "leadership": [
            {"name": "Sir Iain Greig", "title": "President/CEO (ailing)", "notes": None},
            {"name": "Johnathan Cooper", "title": "Division Head, Transys Neuronet GB", "notes": None},
            {"name": "Sir Iain MacDonald", "title": "Director; board financial controller (12 percent stake)", "notes": "Deputy President and heir apparent after the success ending; 'resigns' in the failure ending."},
            {"name": "Donald Menzies", "title": "Finance Director", "notes": "Dismissed with six senior executives (success) or running the company (failure)."},
            {"name": "James McLaughlin", "title": "Senior Research Director", "notes": "Dismissed (success) or Acting Board Chairman (failure)."},
            {"name": "John Cawdor", "title": "Junior research director", "notes": "Made a full Director in the failure ending; Menzies' man."},
            {"name": "Quicksilver", "title": "Wetware and Matrix researcher (deceased)", "notes": "Officially 'missing'."},
            {"name": "Alasdair Cameron", "title": "Research technician (deceased)", "notes": None},
            {"name": "Hugh MacDonald", "title": "Corporate decker", "notes": "Sir Iain's cousin; escorts hired deckers."},
        ],
        "notes": (
            "Research Subsystem 1 is mapped in the prep doc (bio-organic sculpted system, Giger's Alien; "
            "SAN (311)411; paydata in DS-4 to DS-7 on neurophysiological implants at about 5,000 nuyen "
            "per 10 Mp). A corporate decker detected the runners and changed the ID codes 'according to "
            "standard procedure' the day Cameron died; the system then sits on passive alert. Zeta-ImpChem "
            "agents inside the company purged every file on Quicksilver, decoyed the search for him, "
            "killed Cameron and field two strike teams. Legwork (TN 5 Seattle / 8 Scotland): 'a superduper "
            "whizkid... came in out of the blue', a big medical-research payoff, a persistent rumor of a "
            "biological cyberdeck. Success ending (News-Intelligencer, C. Sargent): Finance Director "
            "Donald Menzies, six of his executives, Senior Research Director James McLaughlin and several "
            "senior scientists dismissed; Sir Iain MacDonald promoted Deputy President and heir to Sir "
            "Iain Greig; speculation links the Laidon deaths to rumored AI breakthroughs. Failure ending: "
            "Sir Iain MacDonald resigns 'on grounds of ill health', Menzies runs the company, McLaughlin "
            "becomes Acting Chairman, John Cawdor a Director, and analysts expect a Zeta-ImpChem takeover "
            "(HKB of London strangely quiet -- perhaps bidding for a third party). Sir Iain's reward deck, "
            "a Transys Barrie (MPCP 8, Hardening 4, Memory 120, Storage 500, Load 50, I/O 30, Response "
            "Increase 2, two hitcher jacks, about 400,000 nuyen), carries a built-in alarm that flags "
            "the MPCP to any Transys SAN (Computer B/R (9) to find and again to remove; failure costs an "
            "MPCP point). Transys pays 75,000-nuyen credsticks with a tiny Transys logo."
        ),
        "allies": ["MacDonalds of Glencoe"],
        "enemies": ["Zeta-ImpChem"],
    },
    {
        "name": "Zeta-ImpChem",
        "org_type": "corporation",
        "tier": 5,
        "headquarters": "Interlaken, Switzerland (Anglo-Swiss joint venture)",
        "summary": "Anglo-Swiss megacorp moving into Matrix research; its agents inside Transys murdered Morag, Quicksilver and Cameron and field the strike teams",
        "description": (
            "An Anglo-Swiss megagiant, one of the major corporations with majority British ownership, "
            "headquartered at Interlaken under President/CEO Harald Meier. Beginning to branch out into "
            "Matrix research, it wants to end Transys Neuronet's dominance of the British research "
            "market and 'has always been interested in acquiring gold-chip research' -- it has taken an "
            "active interest in the Transys research division for years. Its agents within Transys "
            "learned how anxious corporate security was over Quicksilver's absences and spared no effort "
            "to follow him."
        ),
        "leadership": [
            {"name": "Harald Meier", "title": "President/CEO", "notes": "Unavailable for comment."},
        ],
        "notes": (
            "The agents tracked Quicksilver to Castle Laidon, murdered Morag MacDonald before his eyes "
            "in Campbell 'Old Colors', shot him as he fled, disguised the raid as the clan feud, left a "
            "few dead Campbells behind and removed their own dead. They killed Cameron with an elemental "
            "combat spell (a risky, un-British way to kill, chosen to point at Americans), tipped off the "
            "police, and had a gray-robed decker (Computer 6, Fuchi Cyber-4 with Response Increase 1, "
            "Attack 5 / Poison 4 / Shield 4 / Armor 4, Threat 3/4) ambush the team in the Transys system. "
            "Strike one (Samurai Strike, p.50): an eight-man Integrated Weapon Systems chopper (Handling "
            "5, Speed 170/250, Body/Armor 4/1, Sig 4, Autopilot 2, two FN-HARs with 1,000 rounds each, "
            "thumbprint/retinal lock, long-range tracking signals) with five street samurai (Wired 2, "
            "dermal 2, hand razors, Predator and Uzi III, Init 9+3D6, Threat 4/3), a rigger (VCR 2, "
            "Gunnery 4) and a combat mage (Sorcery 6, Power Focus 3, Powerball 4, Manaball 4, Personal "
            "Combat Sense 5, spell locks). They keep coming until the mission is done or half lose radio "
            "contact; the chopper's security makes it useless to hijack. Strike two (Set My Soul Free, "
            "p.58): six street samurai, two troll samurai (Muscle Replacement 4, four concussion grenades "
            "each, assault-cannon rounds for boarded windows) and two combat mages (Power Focus 4) at "
            "midnight; the runners must hold for ten Combat Turns (minus one or two for good preparation, "
            "minus one for a spirit posted outside). Failure news: analysts expect Zeta to buy Transys."
        ),
        "enemies": ["Transys Neuronet", "MacDonalds of Glencoe"],
    },
    {
        "name": "MacDonalds of Glencoe",
        "org_type": "Highland clan",
        "affiliation_contact_type": "Tribe",
        "tier": 3,
        "headquarters": "Castle Laidon, Glencoe; Holyrood Court, Edinburgh",
        "summary": "Sir Iain MacDonald's clan -- Catholic Highlanders, a private army of kilted fighting men, choppers, and a 360-year feud with the Campbells",
        "description": (
            "The MacDonalds of Glencoe, Catholic Highlanders whose feud with the Protestant Lowland "
            "Campbells dates from the massacre of February 1692, when Captain Campbell of Glenlyon's 120 "
            "men rose after a fortnight of MacDonald hospitality and murdered 38 of their hosts, many "
            "more dying in the snow. The feud has run almost continuously since -- each side actively "
            "ignores the other, violence is rare, scheming is the rule; the 2022 massacre of fourteen "
            "Campbells by William MacDonald and his cousins is the infamous modern exception. Laird and "
            "Clan Chieftain Sir Iain MacDonald, a Transys Neuronet board member, keeps a fleet of "
            "Rolls-Royce Phaeton limos, company choppers and 'unbelievably vast sums of money'; his "
            "kilted clansmen carry SMGs and a gas-grenade launcher on the top floor of Holyrood Court. "
            "Sir Iain's contacts run to the MacDonalds of the Isles, Sleat, Clanranald and Kingsburgh. "
            "Thirteen days before the adventure fourteen MacDonalds and servants died at Castle Laidon, "
            "among them Morag, Sir Iain's thirteen-year-old twin nephews Alexander and Rory, and the mage "
            "who warded the castle. 'The MacDonalds live for revenge.'"
        ),
        "leadership": [
            {"name": "Sir Iain MacDonald", "title": "Laird and Clan Chieftain", "notes": None},
            {"name": "James MacDonald", "title": "Estate manager; senior spokesman at Castle Laidon", "notes": "Sir Iain's younger brother."},
            {"name": "Hugh MacDonald", "title": "Corporate decker (Transys)", "notes": "Sir Iain's cousin."},
            {"name": "Mad John MacDonald", "title": "Household enforcer (sedated, under lock and key)", "notes": "Cousin; psychopathic."},
        ],
        "notes": (
            "MacDonald Fighting Men (six at Laidon, four in personal rooms F1/F2, two in the security "
            "room): B5 Q6 S6 C2 I5 W5, Ess 5.5 (3.5), Reaction 4 (6); Armed Combat 4, Bike 2, Etiquette "
            "(Clan) 3, Firearms 4, Stealth 3, Unarmed 5; smartlink, two with Wired Reflexes 1; armor "
            "jacket, sword, stun baton, tracking signals, Waldegrave-Stevas heavy pistol with external "
            "smartlink; Threat 2 (3)/3. Escorts and the finale cavalry use the Street Samurai archetype. "
            "The seniors left the glen after the funerals; security is at a low ebb. The castle's Feast "
            "Hall claymore is a Rating 7 barrier against magic and +1 TN to non-MacDonald magicians. Sir "
            "Iain will not admit the Campbells had nothing to do with the murders (clan pride; the "
            "Campbells will not talk) and uses the runners as bait, tipping one or two board members "
            "about the final trip to flush the killers. The cavalry -- a fleet of choppers with Rating 6 "
            "stabilization units -- kills two enemies a turn and flies casualties to the Royal Infirmary "
            "at Sir Iain's expense. Afterwards Sir Iain claims the deck: 'I'll be lookin' after ye, dinna "
            "ye feart.' Nephews Alexander and Rory (13), the two elderly domestics, the six staghounds and "
            "the dead castle mage are on this row only."
        ),
        "allies": ["Transys Neuronet"],
        "enemies": ["Clan Campbell (Argyll)", "Zeta-ImpChem"],
    },
    {
        "name": "Clan Campbell (Argyll)",
        "org_type": "Highland clan",
        "affiliation_contact_type": "Tribe",
        "tier": 3,
        "headquarters": "Inveraray, Argyll (the Campbell citadel)",
        "summary": "Protestant Lowland clan the MacDonalds have feuded with since 1692; framed for the Laidon massacre by two planted corpses",
        "description": (
            "The Campbells of Argyll, Protestant Lowlanders, the other half of the Campbell-MacDonald feud "
            "that began when Captain Campbell of Glenlyon's men murdered their MacDonald hosts at "
            "Glencoe in 1692. Zeta-ImpChem's killers wore the Old Colors of the Campbell tartan and left "
            "the bodies of Robert and Donald Campbell of Argyll at Castle Laidon; the police have "
            "interviewed several Campbells and have no suspects."
        ),
        "notes": (
            "Given the clans' mutual hatred the Campbells refuse to communicate with the MacDonalds, and "
            "clan pride would not let them admit they had nothing to do with the murders -- so the "
            "MacDonalds are plotting a reprisal at the site of the 1692 killings. Morag's ghost knows "
            "better: 'their eyes weren't Campbell eyes'. That detail is not in the public record."
        ),
        "enemies": ["MacDonalds of Glencoe"],
    },
    {
        "name": "Druids of Dunvegan",
        "org_type": "druidic circle",
        "tier": 2,
        "headquarters": "Dunvegan Castle, west coast of the Isle of Skye, on the Sickle Ley Line",
        "summary": "Elven-led circle of Bear, Eagle and Wolf shamans who govern Skye, milk the tourists, and hold the Affect chip",
        "description": (
            "A loosely organized group of Scots druids, white- and gray-robed, led by the elf Finniaen "
            "MacNaughton with his oak and ash ankh-tipped staffs. They govern the Isle of Skye (one "
            "coach is allowed to run there; tourists never set foot in the castle), put on a "
            "sickle-and-recitation show in the stone circle for a golden bowl of donations, and are "
            "shamans of the Bear, Eagle and Wolf totems wearing zodiac medallions (Finniaen the ram of "
            "Aries, Fiona the crab of Cancer). Their real rites happen at midnight with twelve druids and "
            "twelve manifest mountain and forest spirits. Part of the wider Scottish druid effort to "
            "reforest and regenerate the Highland Wild Lands."
        ),
        "leadership": [
            {"name": "Finniaen MacNaughton", "title": "Leader (Eagle shaman; golden-sickle focus)", "notes": None},
            {"name": "Fiona Mac Mhuirich", "title": "Druid (Eagle shaman); keeper of the Affect chip", "notes": None},
        ],
        "notes": (
            "Sickle Ley Line: Background Count 3 (assensing TN 7 or +3); regenerative earth magic with a "
            "druidic and conjuring affinity. Castle and circle are Barrier 9 astrally; attacking the "
            "castle is suicide -- a few dozen nature spirits. The rite (p.36): the team's best magician "
            "(shaman preferred, mage second, street shaman unacceptable; Essence under 2 and street "
            "shamans wait 100 yards off) stands at the circle's center and makes a Magic (4) Test each "
            "turn for up to ten turns (-1 if the team told Fiona about Amelia, the Child and Fionnghuala; "
            "-1 Bear or Wolf; -2 Eagle; +1 for prepared defenses; +1 on turns 8-10): first failure one box "
            "of Stun, second a Karma point and transient blindness, third a point of Magic and "
            "unconsciousness with a vision of Morag dead on the stairs in red tartan; even a clean run "
            "costs a Karma point. Finniaen casts Analyze Truth 7 while the runners talk; lies earn +2. "
            "The Scots (elven) druids most likely have friends in Tir Tairngire, the Salish-Shidhe Council "
            "and other North American lands; revenge for an insult (attacking Nessie, say) could be a long "
            "time coming. Recommended reading: London Sourcebook pp.33-36, 143-45."
        ),
    },
    {
        "name": "Druids of Loch Ness",
        "org_type": "druidic circle",
        "tier": 1,
        "headquarters": "The forests of the west bank of Loch Ness (never seen)",
        "summary": "Hidden druids of the loch who watch through little watcher spirits and share the shore with the Great Free Spirit",
        "description": (
            "The 'druidic brethren at the Loch' -- Fiona's phrase -- who share the forests with free "
            "nature spirits and stay hidden from visitors, tracking them at all times through a unique "
            "detection network of little watcher spirits. Their long association has fed the Great Free "
            "Spirit a great deal of Karma."
        ),
        "notes": (
            "They take no action against the runners. Killing the escaped piasma is self-defense and "
            "does not offend them; attacking Nessie does (+2 TN on everything in the area, including the "
            "quest), and druids 'tend to ponder their course of action'. Shamans whose totem is not Wolf, "
            "Bear or Eagle suffer +3 TN on spirit tests here; no conjured spirit will act against the "
            "locale."
        ),
    },
    {
        "name": "Tartan Army",
        "org_type": "street gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Leith Walk, Edinburgh",
        "summary": "Xenophobic human-only protection gang of Leith Walk; white thistle over a stuck-out red tongue; never firearms",
        "description": (
            "A street gang that extorts protection money from businesses in and around Leith Walk. Only "
            "rude, obnoxious humans need apply -- traditional Scottish xenophobes to a man. Their leather "
            "jackets bear a white thistle above a stuck-out red tongue. They never use firearms, "
            "preferring iron bars and pick-axe handles so the police stay out of it; the leader brings a "
            "vicious pit bull terrier."
        ),
        "notes": (
            "Six of them smash up Stewart's Hyperdrive when Jackie Stewart refuses to pay: B3 Q4 S4 C3 "
            "I3 W4, Ess 6, Reaction 3; Armed Combat 2, Etiquette (Street) 5, Firearms 2, Unarmed 4; club, "
            "heavy leather jacket, knife; Threat 3/3 (they run when four are Seriously hurt). Police in "
            "four minutes. An unarmed brawl, strictly: a runner who pulls a gun makes the Edinburgh trideo "
            "as a 'gun-toting, trigger-happy American' (+1 TN on every test for a week, hovertruck "
            "withdrawn, 20 percent surcharge on deposits). Jumping in earns half-price rental for a week."
        ),
    },
    {
        "name": "Edinburgh Police",
        "org_type": "police force",
        "tier": 3,
        "headquarters": "Edinburgh, Scotsprawl",
        "summary": "Lightly armed, polite, and they shoot to kill; four-minute response; the murder squad that wants the Americans",
        "description": (
            "Edinburgh is so peaceful that very few policemen routinely carry automatic weapons -- and "
            "they still shoot to kill. Beat officers: B4 Q4 S4 C2 I3 W3, Ess 5.5, Reaction 3; Armed "
            "Combat 2, Etiquette (Street) 4, Firearms 3, Unarmed 3, Police Procedures 5; smartlink; Bond "
            "and Carrington Premier heavy pistol with internal smartgun adapter, plated vest, stun baton; "
            "Threat 2/2. Well-armed police bike convoys guard the Highland tourist routes. Customs and "
            "Immigration at the airport (Interrogation 4) are backed by covert bureaucratic mages who "
            "assense every bag; a Grade 2 initiate with Magic 7 for initiates."
        ),
        "notes": (
            "Four officers arrive at Cameron's flat on the assassins' tip (2D6 under the turns elapsed "
            "beyond the second; Perception (4) to hear the sirens; five more turns to climb the stairs). "
            "Surrender means six months on remand, a Scots 'Not Proven' verdict and deportation; fighting "
            "them means exact descriptions on every newsnet, every bounty hunter in the sprawl, and a "
            "seven-year minimum if caught (the British government then offers a job for freedom). "
            "Running gets a vague description on the evening trideo (+1 TN with contacts) and "
            "triple-checked papers on every American leaving Scotland. No British runner works the shadows "
            "at home: massive red tape and a bureaucratic eagle eye on the SINless. Holding cells, New "
            "Tollbooth Prison, and the prison island of Flatholme off Somerset for heavy-weapon smugglers."
        ),
    },
    {
        "name": "Lord Protector's Administrative and Licensing Bureaus",
        "org_type": "government agency",
        "tier": 4,
        "headquarters": "Queensferry Road / Queensferry Street, Edinburgh (local offices; U.K.-wide)",
        "summary": "The U.K. licensing state: driving licenses in 6+1D6 days, 296-item weapon permits, talismonger licenses, ICE permits, 5,000-pound fines for bribes",
        "description": (
            "The two bureaus of the Lord Protector through which the United Kingdom licenses everything. "
            "The Licensing Bureau in Queensferry Road issues international driving licenses to visitors "
            "with a North American license -- in 6+1D6 days; the Administrative Bureau in Queensferry "
            "Street issues weapon permits (a 296-item form in triplicate, down to the applicant's "
            "parents' dates of birth) and the licenses no Edinburgh talismonger will sell without. "
            "Private aircraft need a U.K. pilot's license and seven days' notice filed with the local "
            "offices. Transys Neuronet holds several of its permits for intrusion countermeasures."
        ),
        "notes": (
            "Bribing an official summons security and a 5,000-pound spot fine; deportation if unpaid. "
            "Forgeries instead: Raul Esterhazy's passports, visas and cyberware licenses via Albrecht "
            "(valid only for the job; no weapon licenses, not even knives), Jackie Stewart's temporary "
            "IDL (6,000 pounds, 24 hours, good for two to three weeks). Import penalties (Anarchy in the "
            "U.K., p.79): pistol 7,000 pounds, rifle 10,000, automatic 20,000 and 18 months, heavy weapon "
            "30,000 and two years, explosives or military weapons three years, unlicensed magical items "
            "1,000-20,000, Class C cyberware 60,000 and two years, unlicensed deck or software "
            "5,000-40,000. Cyberguns are detected automatically and locked dead with an electromagnetic "
            "device. The runners' 'licensed' cyberdecks must pass."
        ),
    },
    {
        "name": "University of Edinburgh",
        "org_type": "university",
        "tier": 3,
        "headquarters": "George Square, Edinburgh",
        "summary": "World center of medical and cyberware research with the Royal Infirmary; the cash-strapped Occult Sciences Department; Amelia's office",
        "description": (
            "A sprawling, stuffy, genteelly shabby British university -- narrow hallways branching off "
            "big drafty ones, suspicious porters, cold stone stairs. A major center for medical and "
            "cyberware research with world-wide expertise in collaboration with the Royal Infirmary "
            "Hospital; Professor Colquhoun holds the Chair of Neurophysiology. The Occult Sciences "
            "Department (Amelia Richardson) studies hermetics, shamans and the druids 'as much as they'll "
            "allow', lost its major funder (the Beaumont Fund) last year, and now sells its staff's "
            "enchanting to the corporates to pay the bills. The Philosophy Department is also in George "
            "Square (in 2053) and has never heard of Quicksilver. Lectures at Pollock Hall; the university "
            "LTG directory is on C-net."
        ),
        "leadership": [
            {"name": "Amelia Richardson", "title": "Professor, Occult Sciences Department", "notes": None},
            {"name": "Professor Colquhoun", "title": "Chair of Neurophysiology (on sabbatical)", "notes": "Fionnghuala's father."},
        ],
        "notes": (
            "Far fewer Amelias than Richards(on)s in the listings; a dozen red-herring Richardsons if the "
            "GM wants. The Scottish Museum of Metahuman Arts and Crafts and the National Museum of "
            "Scotland are the book's other suggested places to trawl for contacts (Charisma (9) per "
            "evening on the town; British contacts work at TN 8, bribes of 250 / 750 pounds for -1 / -2)."
        ),
    },
    {
        "name": "Edinburgh University Sidgwickites",
        "org_type": "magical group",
        "tier": 1,
        "headquarters": "University of Edinburgh",
        "summary": "Academic magical group doing soul-survival research and astral studies; Amelia Richardson belongs",
        "description": (
            "A magical group within the University of Edinburgh that conducts soul-survival research and "
            "astral studies -- named, presumably, for the Victorian psychical researchers. Amelia "
            "Richardson is a member; its grades of initiation reduce the Magical Theory (8) target to "
            "spot the missing Mid-heaven in Quicksilver's birth chart by one per grade."
        ),
        "notes": "Off-stage in Imago. A natural home for any PC initiate interested in reincarnation, the metaplanes, or what happened to Quicksilver 'somewhere in the metaplanes'.",
    },
    {
        "name": "BUCM",
        "org_type": "medical insurance",
        "tier": 3,
        "headquarters": "United Kingdom (telecom 715-715-0715)",
        "summary": "British DocWagon-equivalent; 600 pounds a week Gold, 1,500 Platinum, Super-Elite for the very rich; void in the Wild Lands",
        "description": (
            "One of the two British medical-insurance services (the other is Careline, 818-808-2222) "
            "that sell visitors the equivalent of DocWagon Gold at 600 pounds per person per week or "
            "Platinum at 1,500, paid by credstick transfer to a certified account register. Angus MacNab "
            "and Amelia Richardson carry BUCM Platinum; Sir Iain MacDonald's BUCM Super-Elite includes "
            "automatic entry to a Beta Shadow Clinic. Foreign policies may not apply in the U.K."
        ),
        "notes": (
            "Coverage is void in the Wild Lands (no facilities); injuries must be explained without "
            "mentioning them -- hard if Nessie bit you. If the police want the runners, the medical team "
            "may bring them along. The U.K. National Health Service gives non-nationals 24 hours of "
            "emergency care and basic maintenance, more only if an embassy guarantees payment."
        ),
    },
    {
        "name": "SeaSource",
        "org_type": "public information service",
        "tier": 2,
        "headquarters": "Seattle (a subsidiary of Renraku Computer Systems)",
        "summary": "Renraku's Seattle public bulletin-board and information service; compiled the U.K. and Scotland briefing handouts",
        "description": (
            "Seattle's public bulletin boards and computerized information service, operated by Renraku "
            "Computer Systems. Compiles fact sheets such as 'The United Kingdom: Facts at Your Fingertips' "
            "and 'Scotland and Edinburgh: Facts in Brief' (Player Handouts 1-2): politics (King George "
            "VIII, a 540-seat Commons, the House of Nobles, a Green Party government), demographics (47 "
            "million, 76 percent human; Edinburgh 1.044 million, 28 percent metahuman), the pound at about "
            "2.50 to the nuyen, per-capita income 90,000 pounds (Scotland 51,000), legal contacts, airlines "
            "(British Midair, Geordie Airlines, British Comet, Sinclair Skies), BritRail, and a price list."
        ),
        "notes": "Albrecht, dripping sarcasm, sends runners here rather than brief them himself. The British equivalent is C-net (see Matrix systems). Renraku U.K. is one of the major foreign corporate presences in Britain.",
    },
    {
        "name": "Gaetronics Corporation",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Seattle",
        "summary": "Seattle corp whose president David Gray Bear (brother of the Salish-Shidhe chief) has a missing 14-year-old son",
        "description": (
            "A Seattle corporation headed by David Gray Bear, brother of Harold Gray Bear of the "
            "Salish-Shidhe Council. His son Robert, 14, vanished the week of the October newsnet; Lone Star "
            "first called it gang-related, now suspects a kidnapping, has no leads and no ransom demand, "
            "and promises an arrest by the end of the week. Gray Bear offers a 20,000-nuyen reward."
        ),
        "notes": "News texture only (Player Handouts 4-5, byline P. Daza). A ready-made Seattle hook for a team that does not fancy Scotland, or a follow-up when they get home.",
    },
]

LOCATIONS = [
    {
        "name": "Stouffer-Madison Hotel (Red Lobster Restaurant)",
        "location_type": "hotel",
        "district": "Downtown",
        "security_level": "Patrolled / Commercial",
        "summary": "Seattle hotel whose Red Lobster is full of businessmen and fixers; Albrecht's eighth-floor suite; Harvey Wallbangers",
        "description": (
            "For a person lacking gainful employment there are worse things to do than eat at the Red "
            "Lobster in the Stouffer-Madison: the food is great and the place is full of businessmen and "
            "fixers looking for hired help. Peter Albrecht keeps a suite on the eighth floor and has the "
            "waiter send your lobsters up."
        ),
        "notes": "The hook scene. A woman wailing for her lost purse -- 'all that she was is in that purse' -- is the book's first hint of the theme. Good recurring 'where fixers eat' venue.",
    },
    {
        "name": "Hamish's Bar",
        "location_type": "bar",
        "district": "Bottom (east end) of Princes Street",
        "city": "Edinburgh",
        "security_level": "Low Security",
        "summary": "Lurid blue neon, kilted troll bouncers, 82 malts, sawdust and real wood; where Quicksilver drank and the team finds its only contacts",
        "description": (
            "Kilted trolls loom beside lurid blue neon; the bill of fare promises 82 malt whiskies and "
            "the best heavy in town. Inside: subdued light, genuine sawdust, real dark-stained wood, "
            "pewter quart mugs, trolls, elves, a young elf woman alone, street people in tartans, leathers, "
            "denim and metal, not much cyberware or corporate fashion. Stage, office, bar, booths and "
            "storeroom (Bar archetype, Sprawl Sites p.14). Warm mahogany-colored heavy with a real kick. "
            "The hulking ork barman keeps a claymore over the bar, and it is not decoration."
        ),
        "notes": (
            "Quicksilver took a very occasional late-night drink here while his corporate security waited "
            "outside; 'no one dares lay a hand on him... I've heard he's fey, born to faeries in the "
            "Highlands.' The three essential contacts: Hamish, Duncan the Fixer (approaches on his own) "
            "and Fionnghuala (not before the Child). Everyone else: 'rakk off, we don't like talking to "
            "seps in here!' Bars take Scottish or English pounds only (a kindly barman gives 1 nuyen = 1 "
            "pound). Regulars keep their lips shut on a first date; Intelligence vs the NPC's Negotiation "
            "tells a runner when someone is holding back."
        ),
    },
    {
        "name": "Royal Muirfield Hotel",
        "location_type": "hotel",
        "district": "Castle Terrace",
        "city": "Edinburgh",
        "security_level": "Patrolled / Commercial",
        "summary": "Converted theatre hotel where Cameron books the team; balcony restaurant with the best prime Angus beefsteaks in the city",
        "description": "A fascinating place -- it used to be a theatre, and the balcony restaurant serves the best prime Angus beefsteaks in Edinburgh. Room and meals on Cameron's account, 'but I can't handle you ordering twenty bottles of chilled Bollinger a day, all right?'",
        "notes": "Where Cameron's hours-old telecom message waits the morning the team sets out for Skye. U.K. hotel averages: room 70 pounds, breakfast 14, dinner with wine 70; Edinburgh runs 5 percent over.",
    },
    {
        "name": "Cameron's Flat (Queen's Street)",
        "location_type": "residential flat",
        "district": "Queen's Street, second floor",
        "city": "Edinburgh",
        "security_level": "Low Security",
        "summary": "Alasdair Cameron's plush second-floor flat: the decking base, then the murder scene with the wall safe behind the Monarch of the Glen",
        "description": (
            "Plush by Edinburgh standards, round the corner from the Royal Muirfield. Rating 4 maglock "
            "on the door linked to a PANICBUTTON; front room with balcony doors; a desk with four drawers "
            "and Cameron's Fuchi Cyber-4; a wall-sized (worthless) Monarch of the Glen in the living room "
            "hiding a shallow wall safe; a bedroom. Map p.32."
        ),
        "notes": (
            "The team decks the Transys system from here. After Death in Queen's Street: a twisted, burned "
            "corpse in a small scorched circle, mouth open, back arched, right arm pointing at the sky "
            "(Skye); Sorcery (4) or Magic Theory (6) with three successes says combat spell with an "
            "elemental effect; Background Count 1 for an hour, Willpower (2) or vomit when assensing; the "
            "hearth spirit knows only 'died by magic'. Loot: the smashed deck; drawer two, a sealed chip "
            "with a Rating 6 Sleaze program (two turns per drawer); the safe (Strength (9) per turn with a "
            "crowbar): 28,000 pounds in 100-pound notes, a certified credstick for 5,500 nuyen, heirloom "
            "gold jewelry worth 10,000 pounds (Duncan fences at 40 percent); wallet in the bedroom, 1,525 "
            "pounds. The assassins across the road call the police as the team goes in; fire escape out "
            "the back; a hapless old man's car to commandeer if anyone is Seriously wounded."
        ),
    },
    {
        "name": "The Arbroath Smokie",
        "location_type": "bar",
        "district": "Lauriston Place, 'just along from the Royal Infirmary, ha ha'",
        "city": "Edinburgh",
        "security_level": "Low Security",
        "summary": "Rough-tough pub of heavy armor, blatant chrome and blue smoke where a toothless troll flings smoked herring; Angus MacNab's court",
        "description": (
            "No meat bouncer on the door; it does not need one. Extra-heavy body armor, blatant "
            "cyberware, hard attitudes, air blue with tobacco smoke, fifty hard-drinking men who drank "
            "half their body weight at lunchtime and are topping up. A toothless troll vendor flings the "
            "famous Arbroath smokies -- herrings dried, salted and smoked for what looks like several "
            "years -- at customers who tear them apart with their hands. The barmen all have razor claws "
            "retracted along their forearms. Same floor plan as Hamish's (Bar archetype, Sprawl Sites "
            "p.12)."
        ),
        "notes": "Ask for 'a gentleman named Angus MacNab' and the room freezes, an ork spits at your feet, and a troll the size of a rhino plants his fists on his hips: 'Did ye call me a gentleman, ye rakkin' septics?' About 200 pounds of drinks buys a hearing; act offensively and the patrons dump you on the pavement Seriously Stunned.",
    },
    {
        "name": "Stewart's Hyperdrive",
        "location_type": "shop",
        "district": "Leith Walk",
        "city": "Edinburgh",
        "security_level": "Patrolled / Commercial",
        "summary": "Jackie Stewart's vehicle showroom and busy garage -- the leading rental and repair firm in Edinburgh; Tartan Army turf",
        "description": (
            "A showroom smaller than a Seattle runner is used to -- cars, bikes, a limo as centerpiece, "
            "durable Land Rovers and vans -- with a busy garage of repairs and spray jobs at the back, "
            "an ork mechanic, a cramped office and a dowdy, paper-swamped secretary who brings the tea. "
            "'Best autos in the whole of Scotland. We've got the wheels if you've got the credstick.' "
            "Every vehicle carries a tracking bug behind the dash (Concealability 6, 300 km range -- "
            "honestly just to keep track of the fleet) and extra fuel storage worth two full tanks."
        ),
        "notes": (
            "Any car, bike or van in SRII or the Rigger Black Book except articulated trucks, at 105 "
            "percent to buy; rental 2.5 percent of value per week inside Scotsprawl, 6 percent outside, "
            "insurance included, 25 percent deposit; bikes sold, not rented; +10 percent and +1 TN without "
            "an IDL (temporary forged IDL 6,000 pounds). Highland vans: Nissan-Holden Brumby, Rover "
            "Tourman, Land Rover 2046. No armored or nonstandard vehicles, no weapons; but his brother "
            "Angus's Nissan Hovertruck at Pitlochry (Etiquette (Street) vs Charisma; +1 if Duncan sent "
            "you). Route to Skye: A9 to Drumgask, A86 to Spean Bridge, A82 to Invergarry, A87 to the Kyle "
            "of Lochalsh and the ferry. Cameron covers a week's rental up to 4,000 pounds and 75 percent "
            "of the deposit. The Tartan Army raid interrupts the paperwork (see the gang); Jocky drives "
            "the getaway limo, and next day the IDL has 'arrived' and rental is half price."
        ),
    },
    {
        "name": "University of Edinburgh (George Square)",
        "location_type": "university",
        "district": "George Square",
        "city": "Edinburgh",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "University of Edinburgh",
        "summary": "The George Square campus: cold stone stairs, suspicious porters, interminable corridors, and Amelia Richardson's book-crammed office",
        "description": (
            "Several flights of cold stone steps, porters who eye you with suspicion, and corridors of "
            "closed office doors in all directions; a plain panelled door at the far end reads 'Prof. "
            "Amelia Richardson'. Inside, every surface overflows with real books and Celtic ornaments; a "
            "brass orrery and a huge trid horoscope display share the desk with trideo and computer "
            "monitors. Two Celtic-medallion power foci (Rating 3) sit in a glass case; the shelves hold "
            "enchanting, reincarnation cases and theory, spirit survival and astral-metaplane research, "
            "and ancient occult traditions."
        ),
        "notes": (
            "'Are you the mixed-course students?' -- a Seattle voice in a city of strangers. Amelia opens "
            "up only after hearing the employer's name (Perception vs Charisma catches lies; +2 TN "
            "afterwards). The Integrative-Executive chip is born here: when she keys the Mid-heaven (first "
            "degree of Scorpio) into the trid horoscope, Libra, Scorpio and Sagittarius run together like "
            "mercury, the wheel shatters, and a brilliant red chip is left behind (Magical Theory (8) to "
            "spot the gap in the chart first; -1 per grade of initiation). If the team cannot reach "
            "Edinburgh she trideos it."
        ),
    },
    {
        "name": "Amelia Richardson's Flat (Cramond Road)",
        "location_type": "residential flat",
        "district": "Cramond Road",
        "city": "Edinburgh",
        "security_level": "Low Security",
        "summary": "Where Quicksilver's cyberdeck sits connected to the Matrix in a battered blue briefcase, quietly waking up",
        "description": "Amelia's flat on Cramond Road, where she keeps Quicksilver's cyberdeck -- 'I'll leave my deck with you, as always' -- connected to the Matrix. She has noticed activity on its displays lately and assumes Quicksilver is accessing it remotely.",
        "notes": "Never searched in the book; it is why the Child begs to be brought to Amelia. She has keyed duplicate messages to the police, timed twelve hours out, in case the runners get greedy about the deck.",
    },
    {
        "name": "Quicksilver's Flat (Marchmont Road)",
        "location_type": "residential flat",
        "district": "Marchmont Road, out past Melville Drive",
        "city": "Edinburgh",
        "security_level": "Low Security",
        "summary": "The missing elf's flat, already gone over by Transys with the finest-toothed comb imaginable; a dead end",
        "description": "Quicksilver lived in Marchmont Road, out past Melville Drive. The company has already been through the flat with the finest-toothed comb imaginable.",
        "notes": "Any investigation here is utterly fruitless -- break-in, neighbors, all of it. A red herring the book flags as a total waste of time.",
    },
    {
        "name": "Dr. Knox's Body Shop",
        "location_type": "street clinic",
        "district": "Edinburgh (address sold by Duncan for 800 pounds)",
        "city": "Edinburgh",
        "security_level": "Low Security",
        "summary": "Clean, sterilized unlicensed clinic of a doc who does great work slightly steaming and shakes when sober",
        "description": "A body shop with a fairly good reputation among Hamish's clientele: clean inside, equipment sterilized, the only choice a wanted foreigner has. The doc does great work as long as he is slightly steaming; sober he shakes, really steaming he confuses one clump of viscera with another. He has at least given up his stimulant habit.",
        "notes": "Standard fees (SRII p.113), no cyberware or fancy operations; at 200 percent: a medkit, two extra drug vials, three Rating 5 stimulant patches, one Rating 7 trauma patch (3,000 pounds, loath to part with it). House calls 1,000 pounds a day plus expenses at +2 TN. After three days of harboring murder suspects he doubles to 1,500 a day minimum; 48 hours later he drinks himself useless.",
    },
    {
        "name": "Edinburgh International Airport",
        "location_type": "transportation hub",
        "district": "Terminal 3 (suborbital arrivals)",
        "city": "Edinburgh",
        "security_level": "Corporate High Security",
        "summary": "Two hours of red tape, serried ranks of Customs, lightly armed police, covert assensing mages; 'business or tourist?'",
        "description": (
            "Passengers are hurried down the gangways onto a coach and dumped at Terminal 3 before the "
            "serried ranks of grim-faced British Customs and Immigration officials and a handful of "
            "lightly armed police; the queues are at least as long as you were warned. Behind the acres "
            "of barriers a tall red-haired man in a kilt waves. Extremely good security devices; every "
            "magical item is found by the assensing mages no matter how small; cyberguns are detected "
            "and locked dead."
        ),
        "notes": "Licenses are neat plasheen cards with an encased chip plus duplicate hard copy; an official's Intelligence (9) success means the hard copy 'looks odd' and gets passed around ('This look odd to you, MacDougal?'). Cyberdecks pass automatically. The Ghost suborbital: 1000 Seattle, 2100 Edinburgh, two hours. Internal flights: 150 pounds for the first 50 km, 100 per 50 after; Kyle of Lochalsh 650 a head. Leaving is as hard as arriving, harder once the police want the Americans.",
    },
    {
        "name": "Holyrood Court",
        "location_type": "mansion",
        "district": "Holyrood",
        "city": "Edinburgh",
        "security_level": "Corporate High Security",
        "controlling_org": "MacDonalds of Glencoe",
        "summary": "Sir Iain MacDonald's Edinburgh residence: cameras in the foliage, kilted cyborgs at the door, SMGs on the top floor, eight clan elders with pistols by the fire",
        "description": (
            "Overwhelming but not ostentatious security: cameras and scanners in the foliage, two kilted "
            "MacDonalds at the front door bristling with cyberware, I/R beams and detection lasers on the "
            "windows, unsmiling guards who find every weapon bigger than a nail file, a massive staircase "
            "past more guards to a top floor where the clansmen carry SMGs and one totes a gas-grenade "
            "launcher, and a huge study with a real fire where Sir Iain hands round crystal tumblers of "
            "whisky to his guests and eight pistol-gripping clan elders. Ten minutes to make your case."
        ),
        "notes": (
            "Reach Sir Iain by telecom here or at the Transys Meadows complex; only a description of "
            "Quicksilver's deck stops him hanging up on cranks. Every favor is an opposed Negotiation "
            "(Willpower) at +2, offset by what the team can offer: James's account of the possession (-2), "
            "Morag's 'Old Colors' detail (-1 more), a clear description of the deck (-1), an accurate "
            "account of the Skye druids (-1), half-healed wounds blamed on rogue Transys elements. He "
            "gives nothing on Quicksilver, refuses money, guns or muscle early on, lends Hugh MacDonald and "
            "the new system codes (no downloading), permits Castle Laidon with six fighting men, and near "
            "the end provides a chopper and two escorts. Threaten him and the authorities or Transys agents "
            "pick up the team and Amelia. If Edinburgh is too hot he books a whole small hotel in "
            "Pitlochry, wires it, and stuffs it with MacDonalds."
        ),
    },
    {
        "name": "Transys Neuronet Meadows Complex",
        "location_type": "corporate headquarters",
        "district": "The Meadows",
        "city": "Edinburgh",
        "security_level": "Corporate High Security",
        "controlling_org": "Transys Neuronet",
        "summary": "Transys Neuronet's Edinburgh home office, where Sir Iain keeps his board office and the research subsystems live",
        "description": "The Transys Neuronet complex in the Meadows, Edinburgh: home office of the Transys Group, seat of the board, and the physical home of the Edinburgh system whose Research Subsystem 1 the runners deck. Sir Iain MacDonald issued his 'private matter to the MacDonalds' statement from his offices here.",
        "notes": "Never entered physically in the book -- the action is in the Matrix (see Matrix systems). Quicksilver's R&D colleagues cannot be raised by telecom the day Cameron dies.",
    },
    {
        "name": "Lord Protector's Bureaus (Queensferry)",
        "location_type": "government building",
        "district": "Queensferry Road / Queensferry Street",
        "city": "Edinburgh",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "Lord Protector's Administrative and Licensing Bureaus",
        "summary": "The Licensing Bureau (driving licenses) and the Administrative Bureau (weapon permits, talismonger licenses); do not offer a bribe",
        "description": "The Lord Protector's Licensing Bureau in Queensferry Road, where a North American license becomes an IDL in 6+1D6 days, and the Administrative Bureau in Queensferry Street, which issues weapon permits on a 296-item form in triplicate and the licenses every talismonger in Edinburgh demands.",
        "notes": "Bribe an official and he summons security and a 5,000-pound spot fine. 'Any runner checking into this will fairly scream, No way, chummer.' Duncan the Fixer or Jackie Stewart are the short cuts.",
    },
    {
        "name": "Royal Infirmary Hospital",
        "location_type": "hospital",
        "district": "Lauriston Place",
        "city": "Edinburgh",
        "security_level": "Patrolled / Commercial",
        "summary": "Edinburgh's great teaching hospital; Professor Colquhoun's research base; Fionnghuala pilfers patches from it; Sir Iain's choppers land the wounded here",
        "description": "The Royal Infirmary Hospital, partner of the University of Edinburgh in several world-class medical and cyberware research areas, where Professor Colquhoun conducts his neurophysiology research and his daughter Fionnghuala works as his assistant. Just along Lauriston Place from the Arbroath Smokie.",
        "notes": "Fionnghuala can smuggle out a medkit (500 pounds) or two Rating 5 antidote and two Rating 6 trauma patches at 150 percent -- a few small items at a time, absolute limits, only for a good cause. In the success ending Sir Iain's choppers (Rating 6 stabilization) fly the seriously injured here for intensive care at his expense.",
    },
    {
        "name": "Dunvegan Castle (Isle of Skye)",
        "location_type": "landmark / monument",
        "district": "West coast of Skye, on the Sickle Ley Line",
        "city": "Isle of Skye",
        "security_level": "Zero Zone -- Lethal Response",
        "controlling_org": "Druids of Dunvegan",
        "summary": "Druid headquarters on a promontory over the sea, closed to tourists; the 30-stone circle at its foot where the Affect rite is held at midnight",
        "description": (
            "Dunvegan Castle stands on a promontory overlooking the sea and tourists never set foot "
            "inside. At the foot of the promontory is a stone circle some forty feet across, thirty "
            "stones five to ten feet high. By day seven robed druids process down to perform a "
            "gesture-and-recitation show for the coachload of tourists and a golden bowl; shortly before "
            "midnight twelve return with golden sickles, small golden bowls, torches and zodiac "
            "medallions, Aries at one o'clock round to Pisces at twelve, and six mountain and six forest "
            "spirits erupt from the earth behind them. Castle and circle are Barrier 9 astrally; the "
            "ley's Background Count is 3."
        ),
        "notes": (
            "Getting there: fly to the Kyle of Lochalsh (650 pounds), or hovertruck (14 hours) or car (two "
            "days, Drumgask stopover, 85 pounds); the glorious 15-minute ferry across Loch Alsh to "
            "Kyleakin (8 pounds), then the island's one coach to Dunvegan (15 return). The team's only "
            "chance to speak to the druids is as the tourist show ends; only the name Quicksilver moves "
            "Finniaen. Assensing Fiona at 4+ successes shows a sealed wooden box very dear to her. Only "
            "one runner enters the circle; the rest wait outside and would have to go through the spirits "
            "to interfere. Afterwards the team spends the night in the cold with the first piece of "
            "Quicksilver: a small black box sealed with wax and a silver clasp. Fiona: 'He followed the "
            "ley not long ago, and I know he met a presence at the lochside -- at Loch Ness.'"
        ),
    },
    {
        "name": "Kyle of Lochalsh",
        "location_type": "village",
        "district": "Wild Lands, opposite Skye; fuel and lodging at Wild Lands prices",
        "city": "Kyle of Lochalsh",
        "security_level": "Low Security",
        "summary": "Fishing village of 550 souls at the Skye ferry; the team's Highland base; kippers, oatcakes and lashings of cold toast",
        "description": "A small fishing village of some 550 souls at the end of the A87, where the ancient ferry crosses the pure, still salt water of Loch Alsh to Kyleakin at little faster than walking pace. Accommodation 100 pounds a night, two to a room, supper and breakfast included (kippers, oatmeal cakes, real salted bacon, fresh eggs); garage 25 pounds for a car, 35 for a hover vehicle; one of the few Wild Lands settlements with fuel, at 150 percent.",
        "notes": "Locals answer every question about the druids with 'Ye'll see. Ye're too eager tae ken aa', and questions about a druid named Fiona with peals of laughter -- 'that's an awfa common name roond heer'. Amelia will fly out to meet the team here if Edinburgh is too dangerous; 'a better base for their operations now anyway'. Make them feel good: the stronger their well-being, the easier to catch them off guard.",
    },
    {
        "name": "Drumgask",
        "location_type": "village",
        "district": "Wild Lands, on the A9/A86 route north",
        "city": "Drumgask",
        "security_level": "Low Security",
        "summary": "Wild Lands waystation with overnight lodging and fuel at 150 percent; the logical stopover on the two-day drive to Lochalsh",
        "description": "A small Highland settlement on the road route to Skye where a van full of runners can get dinner, bed and breakfast for 85 pounds a head, two to a room, and buy fuel -- one of the handful of Wild Lands places that sells it.",
        "notes": "The roads have not been repaired properly in years; expect detours across inhospitable terrain, heather hillsides, old pine forest, the druids' new forest, armored touring vans and police bike convoys.",
    },
    {
        "name": "Angus Stewart's Garage (Pitlochry)",
        "location_type": "shop",
        "district": "Pitlochry (bus 60 pounds, rail 125 from Edinburgh)",
        "city": "Pitlochry",
        "security_level": "Low Security",
        "summary": "Where Jackie Stewart's brother keeps the Nissan Hovertruck no license in Edinburgh will cover -- 2,500 pounds a day, outside the sprawl only",
        "description": "Angus Stewart's garage in Pitlochry, at the edge of the sprawl, where his Nissan Hovertruck lives. 'You need a special license for one of those... Angus might let you rent his if you stay outside the sprawl. You'll have to pick it up at Pitlochry and head off from there.'",
        "notes": "2,500 pounds a day (2,250 on a successful Negotiation), a week in advance, 50,000 pounds in a holding account, tracking bug behind the dash. Fourteen hours by road to Lochalsh. Nessie surfaces fifty yards behind anyone who drives it out onto Loch Ness.",
    },
    {
        "name": "Invergordon Hotel (Pitlochry)",
        "location_type": "hotel",
        "district": "Pitlochry",
        "city": "Pitlochry",
        "security_level": "Low Security",
        "summary": "Small hotel Sir Iain books entire, wires for surveillance and packs with MacDonalds when the runners dare not enter Edinburgh",
        "description": "A small hotel in Pitlochry that James MacDonald suggests as a meeting place with the Laird when Edinburgh means arrest. Sir Iain takes the whole place for the evening, wires it, and stuffs it full of MacDonalds for cover.",
        "notes": "Same negotiation as Holyrood Court, different furniture.",
    },
    {
        "name": "Loch Ness (Castle Urquhart shore)",
        "location_type": "ruins",
        "district": "West bank forest, near the ruins of Castle Urquhart; bus to Invergarry and walk",
        "city": "Loch Ness",
        "security_level": "No Security / Barrens",
        "summary": "The deep dark woods of fairy tales on the loch shore; Background Count 3; the Great Free Spirit, hidden druids, a stray piasma and Nessie",
        "description": (
            "The road peters out at the forest on the west bank -- the deep, dark deciduous woods of "
            "fairy tales, so thick you cannot see the loch until a few yards from the shore. Free nature "
            "spirits of forest and mountain watch from the trees; the loch stretches for miles. Near the "
            "ruins of Castle Urquhart the great free forest spirit commands visitors to stop. The heart of "
            "the magic, 'a primordial place of power where mystic forces run wild and alliteration is "
            "king'."
        ),
        "notes": (
            "Perception (6) with astral perception identifies the free nature spirits (four successes: "
            "free spirits); they sense assensing and drift away. Every kilometer of shore: 2D6, 11-12 and "
            "the piasma attacks -- a huge sabre-toothed bear-thing escaped from a guard installation at "
            "the Inverness naval base (B11/4 Q4x5 S13, Threat 4, 9D2 +1 Reach, Enhanced Attributes and "
            "Reactions, thermographic, wide-band hearing; flees when Seriously hurt). The spirit's astral "
            "gateway takes everyone with Essence 2+ on the quest (bodies in trance; two may stay to guard). "
            "Nessie splashes about as the team leaves if she has not appeared. Karma: +1 to everyone who "
            "toughs out the quest."
        ),
    },
    {
        "name": "Castle Laidon",
        "location_type": "fortified keep",
        "district": "Glencoe, Rannoch Moor; no coach service",
        "city": "Glencoe",
        "security_level": "Corporate High Security",
        "controlling_org": "MacDonalds of Glencoe",
        "summary": "Small modern fortified keep of the MacDonalds of Glencoe: razor wire, IR cameras, hidden gate SMGs, a magic claymore, staghounds, Mad John, and Morag's ghost on the great staircase",
        "description": (
            "Glencoe is a magnificent, melancholy glen the old MacDonalds never needed to fortify; the "
            "early-21st-century MacDonalds built a small but stout keep ringed with four-meter razor wire "
            "(8M running into it, 6M walking, 4M grabbing; whips for 6M when cut) and rotating infrared "
            "cameras covering 120-yard arcs, retinal-ID maglocks on the main gate, and a pair of SMGs "
            "hidden in the gateposts (Firearms 4, 5M3 ammo, 200 rounds, 90-degree arcs). Inside: stag's "
            "heads, tartan drapes, shields and claymores, stuffed animals in glass cases, antique pistols, "
            "bagpipes. Basement cellars of wine, whisky and cold stores and a poachers' holding cell (B1). "
            "First floor: fighting men's rooms (F1-F2), the lair of six Scottish staghounds (F3), the "
            "kitchen with two elderly domestics (F4), the Greeting Hall (F5). Second floor: the Feast Hall "
            "(S1) with the heirloom claymore over the fireplace, Morag's bedroom (S2) with its window "
            "bricked up and kept exactly as it was, the security room (S3), James's room (S4), S5. Third "
            "floor: family rooms and Mad John's cell (T1). Garage: a Land Rover 2046, two antique British "
            "Industrial PLC Hunter-Wagner bikes, a generator with 612 gallons of fuel oil, two Rating 4 "
            "maglocks. Maps pp.45-48."
        ),
        "notes": (
            "The Feast Hall claymore projects a Rating 7 barrier against magical attacks and +1 TN to "
            "non-MacDonald magic; the collective ghosts of the 1692 massacre form a second Rating 7 astral "
            "barrier, almost without awareness. Morag was gunned down on the great staircase from F5 to "
            "S1; her ghost appears there at the stroke of midnight (or to astral perception on a Magic (8) "
            "Test, -1 per chip carried, -2 for the Skye vision) and speaks only by possessing a willing "
            "runner (two Astral Body (6) Tests or twelve turns unconscious). The Perception chip (yellow) "
            "is in the immense headboard of her bed behind the shield of the MacDonald coat of arms "
            "(Perception (8)). Ways in: an area effect through the wire and gates; hacking the security "
            "system (mapped in the prep doc) disables the defenses; or talk James round -- a plausible "
            "reason (-1), a mauled-by-a-bear sob story with SynthiTomato relish, weapons surrendered at "
            "the door to four fighting men, five minutes to leave before the machine guns fire. He shows "
            "the murder site, gives no free run, and lets one runner per net success stay 24 hours to "
            "contact the troubled soul they assensed. Violence here costs the team Sir Iain. The finale: "
            "board the windows, oil-slick the stairs from the generator, oil pots from the windows, trip "
            "wires; the deckers work in Morag's room while Amelia wards the deck and James guards the "
            "door. Zeta comes through the front doors at midnight; if permitted, MacDonald choppers arrive "
            "two turns before the time runs out. Then Sir Iain, a piper, six enormous clansmen, the Spirit "
            "of Man as a 1692 chieftain, and thirty-seven MacDonald ghosts rising into the ether."
        ),
    },
    {
        "name": "Scottish Wild Lands",
        "location_type": "wilderness",
        "district": "The Highlands beyond the Habitable Zone (Fringe Toxic Zone east, Irradiated Zone north)",
        "city": "Scotland",
        "security_level": "No Security / Barrens",
        "summary": "Paranatural-haunted Highlands outside British law, impassable late September to late March, being reforested by the druids; insurance void here",
        "description": (
            "Scotland is zoned: the industrial/residential Scotsprawl (Edinburgh and Glasgow), the "
            "habitable zones to either side, the Fringe Toxic Zone on the east coast, the Irradiated Zone "
            "on the north coast, and the Wild Lands -- heather hillsides, old pine forests, the new forest "
            "the druids are regenerating, cold pure rivers, bracken plains, the Glens and the lochs, "
            "crawling with dangerous paranatural creatures and beyond the rule of British law. Hereditary "
            "aristocrats, mostly clan chieftains, own vast tracts and perpetuate ancient feuds."
        ),
        "notes": (
            "Highland roads are often impassable from late September to late March, and the freezing fogs "
            "that roll off the mountains make a chopper flight 'a great way to commit suicide' -- set the "
            "adventure between April and October. Medical insurance is void here and there are no "
            "facilities. Fuel only at a handful of settlements (Kyle of Lochalsh, Drumgask) at 150 "
            "percent. Magical sites on the GM map (p.12): the Sickle Ley on Skye, Loch Ness, Glencoe, the "
            "Midmar stone circles, Iona. Nature walks may be interrupted by a hostile paranimal, 'or even a "
            "whole flock of them'."
        ),
    },
]

NPCS = [
    {
        "name": "Quicksilver",
        "role": "Unique two-meter elf, Transys' wetware genius, born 2021 in Wales; encoded himself into four living chips and became the Imago to die again with Morag",
        "archetype": "Matrix Researcher / Unique Entity",
        "title": "Wetware and Matrix researcher, Transys Neuronet (deceased); the Imago; 'Erewan' to Fionnghuala",
        "race": "Elf",
        "gender": "Male",
        "nationality": "Welsh-born (British passport)",
        "age": 32,
        "organization": "Transys Neuronet",
        "connection": 5,
        "description": (
            "Really tall even for an elf, around two meters; short silver hair with a small black streak "
            "at the left temple; distinctive blue-silver cybereyes; a great deal of cyberware, jacks around "
            "his neck hidden under a blue silk scarf; wears plenty of black and, this year, a silver signet "
            "ring on his left index finger. Carries his battered blue briefcase everywhere. A loner prone "
            "to introspection and stormy emotions, rarely gregarious, secretive and paranoid, a "
            "perfectionist who took more than two years to build his deck; 'weirdo... I've heard he's fey, "
            "born to faeries in the Highlands'. Bent with the weight of ages, yet his eyes shine with hope. "
            "'I am making myself immortal, Amelia.'"
        ),
        "background": (
            "Born in 2021 on the coast of South Wales near a complex of old Nubian/Egyptian temples "
            "(London Sourcebook, 'Knights of Rage'), adult in size and ability by ten; traveled the Welsh "
            "and Scottish Wild Lands, Tir Tairngire, Aztlan, the California Free State, Tir Nan Og and "
            "the Middle East. Believes he has lived in Karnak and Thebes, Athens and Beijing, Rome and "
            "Jerusalem, often with Amelia as a friend, and that Morag is his younger soul mate across "
            "incarnations. Hacked into the Transys CPU in 2048 and asked for a job; went from neural "
            "skillsofts to wetware -- biological chips with intrinsic pseudo-intelligence, recombinant "
            "technology, smart viruses. Late in 2052 Cameron dragged him to a party and he met Morag; "
            "from then on he evaded his security escorts on 'Highland retreats' to see her, and to leave "
            "pieces of himself with the druids, the spirit and Amelia, following his own karma: whatever "
            "benefits him must benefit others, so he must trust. Shot dead fleeing Castle Laidon thirteen "
            "days before the adventure, five days after his last visit to Amelia."
        ),
        "notes": (
            "No stats; he needs none. His personality is encoded onto four living biochips -- blue "
            "crystalline chips on a tiny telemetry rod in iron-hard plastic cubes, structured like a "
            "magnified living cell -- updated by high-resolution telemetry between his brain and deck to "
            "the moment of death: Affect (blue, Fiona), Memory (green, the Loch Ness spirit), Perception "
            "(yellow, Morag's headboard) and Integrative-Executive (red, Amelia's horoscope). The Child is "
            "his template, a unique smart frame with all his back-door codes, activated when he failed to "
            "key the deck's suppression codes; it neutralizes IC with a wave and does not alter node load, "
            "which terrifies Transys deckers. Slotting chips: Affect alone is a Power 4 Serious Stun "
            "attack of grief; Affect plus Memory a Power 4 Serious Physical of bullets; the reintegrated "
            "elf sits with his head in his hands (Willpower (6) or share the murders: moonlight, a piper "
            "playing Flowers of the Forest, samurai on the steps). 'Take me to Morag. I need to die with "
            "her.' The transformation (four stages, Reaction (6), Intelligence (8), Willpower (8), Essence "
            "(6), a Force 4 stun bolt at each; failure on the last costs a point of Essence, 5 Karma to "
            "regain) leaves the decker unconscious and the chips inert. 'Imagos cannot and do not exist' -- "
            "a one-off like Harlequin, never a precedent."
        ),
    },
    {
        "name": "Alasdair Cameron",
        "role": "Huge, shy, kilted Transys technician who imports foreign runners to find his friend; burned to ash in his own flat",
        "archetype": "Corporate Technician",
        "title": "Research technician, Transys Neuronet; Quicksilver's assistant (deceased)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Scottish (Aberdeen)",
        "age": 31,
        "organization": "Transys Neuronet",
        "connection": 3,
        "description": (
            "Tall, red-haired and shovel-handed -- 'you wonder how he got to be so huge' -- in a "
            "distressingly red tartan kilt with lumps of green threaded with yellow (Cameron tartan; he "
            "owns six). Sandy brown hair and hazel eyes on the cast page. Talks a little too fast until "
            "two wee drams of malt, then gruff, slightly shy and suddenly tender about his boss: 'I want "
            "him back just because I liked him.' A born bachelor, fond enough of women, little pubbing. "
            "Matrix persona: a gray-robed old man."
        ),
        "background": (
            "Born and educated in Aberdeen; Ph.D. in molecular biology and cybernetics; joined Transys at "
            "24. Has a row with two brothers over an inheritance behind him and tenuous clan ties. Loyal "
            "to the company but more to Quicksilver, he rationalizes that finding out what happened can "
            "only serve Transys, and acts alone to avoid the agents he suspects do not want Quicksilver "
            "found. Hired Peter Albrecht to find foreigners for security and freedom of action; has no "
            "idea what the runners will find."
        ),
        "notes": (
            "Gives the Transys subsystem passcodes (not the big-nuyen areas), a picture of Quicksilver, his "
            "telecom number, the Royal Muirfield, and pointers to Hamish's and a university woman he knows "
            "nothing about. Money: fines to 10,000 pounds (half from the fee), a week's rental to 4,000 "
            "and 75 percent of the deposit, pistols and basic armor if sold back afterwards, half a heavy "
            "weapon on a hard Negotiation, never Angus MacNab. Rides behind the decker on his own deck to "
            "stop data theft (one turn of download tolerated; 100 Mp if the decker argues hazard pay; "
            "steal more and he ends the job and turns the team in). Killed by an elemental combat spell "
            "the day he warned the team the codes had changed. Stats: B3 Q4 S4 C3 I6 W4, Ess 5.4, Reaction "
            "5; Biology 4, Biotech 6, Biotech B/R 4, Computer 5, Computer B/R 3, Computer Theory 6, "
            "Electronics 4, Electronics B/R 3, Etiquette (Corporate) 3, Negotiation 3, Physical Sciences "
            "3, Unarmed 2; datajack, beta headware memory 100 Mp; Fuchi Cyber-4 with Response Increase 2 "
            "(Bod 5, Evasion 4, Masking 2, Sensors 5; Analyze 6, Browse 6, Sleaze 6, Smoke 6, Scanner 5, "
            "Autoexecute 4, Compressor 4, Medic 4, Restore 4); Threat 2/2. Legwork: 'reliable and dull'."
        ),
    },
    {
        "name": "Amelia Richardson",
        "role": "Seattle-born professor of Occult Sciences, enchanter and reincarnation scholar; Quicksilver's friend across lifetimes and keeper of his deck",
        "archetype": "Academic Mage",
        "title": "Professor, Occult Sciences Department, University of Edinburgh",
        "race": "Human",
        "gender": "Female",
        "nationality": "American (Bellevue, Seattle)",
        "age": 42,
        "organization": "University of Edinburgh",
        "connection": 4,
        "description": (
            "Tall with elegant features, light brown hair worn long and straight (the prologue says fair) "
            "framing blue-gray eyes; dowdy but good-quality tweeds and wools; a bright-eyed, attentive "
            "look of calm intelligence from behind a desk dwarfed by monitors. Lights a Lite while she "
            "listens. Tough, intelligent, willful, well-organized and resourceful; 'clearly no flake'. "
            "Leads a quiet life without romance and would like a little adventure. 'Are you the "
            "mixed-course students?'"
        ),
        "background": (
            "Grew up in one of the less impressive neighborhoods of Bellevue, worked as a trideo "
            "researcher, discovered her magic at the University of Washington, took her Ph.D. in Occult "
            "Sciences at Edinburgh and has lived there eleven years -- her adopted home; she cares little "
            "for modern Seattle. Specializes in enchantment, reads pre-Awakening parapsychology on "
            "reincarnation and survival, studies esoteric astrology, belongs to the Edinburgh University "
            "Sidgwickites. Her late parents left her enough to teach for love; she resents the enchanting "
            "her superiors make her do for the cash-strapped department. Once had a Sassenach boyfriend, "
            "years ago. Quicksilver believes she was his friend in several past lives and left her his "
            "deck and the master chip."
        ),
        "notes": (
            "Cat-and-mouse: demands the employer's name (Perception vs Charisma against lies, +2 TN "
            "after), gives a little more per net Negotiation success, says nothing of the deck until the "
            "team returns from Skye, then produces the battered blue briefcase and never lets it out of "
            "her possession (police messages keyed twelve hours out). Flies to the Kyle of Lochalsh if "
            "Edinburgh is too hot; offers her own foci to a doubtful team (12 Karma drops to 8 if that is "
            "what bought them); wards the deck during the finale. Stats: B2 Q1 S3 C3 I5 W3, Ess 6, Magic 6, "
            "Reaction 4; Biology 3, Conjuring 3, Enchanting 8, Etiquette (Corporate) 1, Magical Theory 7, "
            "Negotiation 3, Psychology 6, Sorcery 5; Threat 1/2. Spells: Personal Physical Barrier 6, "
            "Stun Bolt 4, Increase Physical Attribute +1, Analyze Truth 6, Clairvoyance 4, Levitate Item 4, "
            "Use B/R Electronics 6, Mask 6, Overstimulation 4. Gear: Power Focus 4, spell foci Analyze "
            "Truth 3 / Mask 4 / Personal Physical Barrier 4, orichalcum dirk weapon focus, Ares Predator, "
            "armor jacket (2/1), Honda-GM 3220 ZX, BUCM Platinum, flat in Cramond Road. Legwork (TN 8): "
            "'Very sensible. Nice lady.'"
        ),
        "contact_skills": ["Enchanting and magical theory (Edinburgh)", "Reincarnation, astrology and soul-survival research", "University of Edinburgh access"],
    },
    {
        "name": "Morag MacDonald",
        "role": "Wild, intense young elven noblewoman, Quicksilver's secret lover; murdered on the Laidon staircase, now a mute, possessing ghost",
        "archetype": "Ghost",
        "title": "Daughter of Sir Iain MacDonald of Glencoe (deceased); apparition of Castle Laidon",
        "race": "Elf",
        "gender": "Female",
        "nationality": "Scottish (MacDonald of Glencoe)",
        "age": 19,
        "organization": "MacDonalds of Glencoe",
        "connection": 2,
        "description": (
            "A young female elf of about nineteen ('about 20' in the news): long curly honey-blond hair, "
            "blue-green eyes, ivory skin, long slender-fingered hands with almond nails; a laced cotton "
            "blouse, a MacDonald tartan skirt, and silver earrings, brooch and rings the family has owned "
            "for 300 years. Extreme emotional intensity in life, more so in death; a barely visible spectral "
            "form with anguish easy to read. The vision on Skye: slumped on stone steps, white blouse "
            "stained with blood, red tartan skirt (the back cover)."
        ),
        "background": (
            "Wild, intense and passionate, she met Quicksilver at a social function late in 2052 and "
            "shared his passion for secrecy in a string of clandestine meetings; her father never knew. "
            "Zeta-ImpChem's killers in Campbell Old Colors gunned her down on the great staircase between "
            "the Greeting Hall and the Feast Hall as Quicksilver fled unarmed. 'He left his eyes, he said "
            "he would always see me, he left something of himself and I don't know where it is.'"
        ),
        "notes": (
            "Speaks only by possessing a runner who agrees freely (two Astral Body (6) Tests or twelve "
            "turns unconscious), talking at rather than with them, unaware of anything since her death; "
            "the GM may cheat with Grimoire II free-spirit possession if nobody volunteers. Appears at "
            "midnight on the stairs, or to astral perception on Magic (8) (-1 per chip, -2 for the Skye "
            "vision); found automatically on projection once seen. Cannot be laid by Conjuring; has no peace "
            "until she reaches Quicksilver's spirit; because of the Glencoe background spirits she is "
            "stronger than most apparitions. Stats: I4 W8 C5 Ess 6 Reaction 5, Initiative 15/25 + 1D6; "
            "Powers: Compulsion, Fear, Manifestation, Possession, Psychokinesis; a free-spirit-style "
            "personal domain -- +4 TN against her inside or within half a mile of Castle Laidon. At the end "
            "she and Quicksilver reappear smiling, hand in hand, and fade with the 37 ghosts."
        ),
    },
    {
        "name": "Sir Iain MacDonald",
        "role": "Laird of the MacDonalds of Glencoe and Transys board financial controller; grieving, blunt, revenge-minded, holds all the cards",
        "archetype": "Corporate Director / Clan Chieftain",
        "title": "Laird and Clan Chieftain, MacDonalds of Glencoe; Director, Transys Neuronet",
        "race": "Human",
        "gender": "Male",
        "nationality": "Scottish (Glencoe)",
        "age": 47,
        "organization": "MacDonalds of Glencoe",
        "connection": 6,
        "description": (
            "Average height, receding silver hair, brown eyes; his wife's death in 2047 and Morag's now "
            "have aged him beyond his years -- lined face, slightly slumped posture -- but a strong sense "
            "of clan honor and duty holds him up. Blunt, practical, honest, with a cautious streak; prefers "
            "others do the talking; stares straight at people while negotiating and drives a hard bargain. "
            "'Straight as a die. Doesn't smile a lot.' A rich Highland burr: 'Weel, ye'd better hae "
            "somethin tae say fer yersel. The polis will be interested if ye dinna. I'll gie ye ten "
            "minutes.'"
        ),
        "background": (
            "On the Transys board he is primarily a financial controller with some minor overseas "
            "research projects, a 12 percent stake, a fleet of Rolls-Royce Phaeton limos, Holyrood Court, "
            "and 'unbelievably vast sums of money'. Had no idea his daughter loved Quicksilver. Told the "
            "trid the killings were 'a private matter to the MacDonalds, and we will settle it in our own "
            "time'; deeply involved in plotting revenge on the Campbells, who will not talk. Suspects "
            "enemy agents in the company and, once the runners describe recent events, uses them as bait "
            "-- tipping one or two board members about the final trip to Castle Laidon."
        ),
        "notes": (
            "See Holyrood Court for the negotiation modifiers. Cares nothing for the runners' fate and "
            "does not believe in Morag's ghost until the Spirit of Man sweeps its claymore -- then he "
            "salutes it. Asks 'What's in it fae the company, then?': sell the deck as priceless to Transys "
            "and the trail as leading to the killers of Quicksilver, Cameron and his daughter. Success: "
            "promoted Deputy President; flies the wounded to the Royal Infirmary, sends the team home by "
            "private suborbital, sends a Transys Barrie deck and 75,000-nuyen credsticks -- decent pay, "
            "not excessive, for a rich, rich man. Failure: 'resigns on grounds of ill health'. Stats: B3 Q2 "
            "S4 C5 I6 W5, Ess 5, Reaction 3; Corporate Accountancy 8, Etiquette (Clan) 7, Etiquette "
            "(Corporate) 7, Interrogation 5, Leadership 9, Negotiation 6, Unarmed 3; datajack, beta headware "
            "memory 200 Mp; BUCM Super-Elite (Beta Shadow Clinic); Threat 2/3."
        ),
        "contact_skills": ["Transys Neuronet board-level access", "MacDonald clan muscle, choppers and money", "Scottish establishment (the polis, the Bureaus)"],
    },
    {
        "name": "James MacDonald",
        "role": "Sir Iain's younger brother and estate manager, spokesman at Castle Laidon; cautious, not bright, honest and brave",
        "archetype": "Estate Manager",
        "title": "Estate manager, MacDonalds of Glencoe; senior man at Castle Laidon",
        "race": "Human",
        "gender": "Male",
        "nationality": "Scottish (Glencoe)",
        "age": 40,
        "organization": "MacDonalds of Glencoe",
        "connection": 3,
        "description": "Medium height, sandy brown hair, brown eyes. Oversees the clan's property and land rights; cautious, hesitant and not overly bright, but honest and brave, with a Highlander's respect for magic and the Sight. 'Och, weel. But what dae ye want?'",
        "notes": (
            "Occupies S4 and runs the castle while the seniors are away. Angry intercom voice first; "
            "Charisma (Negotiation) to be let in (equal successes: one or two runners; more: all; fewer: "
            "five minutes before the guns). Perception (6) to spot a faked injury (+1 TN after). Lets one "
            "runner per net success stay 24 hours to contact the soul; watching Morag possess a runner "
            "profoundly affects him and he arranges the meeting with Sir Iain. A reluctant Negotiation "
            "(Willpower) win lets the team search Morag's room. At the finale he stands guard at the "
            "deckers' door. Stats: B3 Q3 S4 C4 I6 W5, Ess 6, Reaction 4; Armed Combat 2, Etiquette "
            "(Street) 2, Etiquette (Clan) 5, Leadership 2, Negotiation 5; armor vest, Ares Predator, stun "
            "baton; Threat 4/3. Keeps Mad John's gear in his own room and hands it over if the castle is "
            "attacked."
        ),
    },
    {
        "name": "Mad John MacDonald",
        "role": "Psychopathic, brain-damaged, wired MacDonald cousin shipped in after the murders and kept sedated under lock and key -- until the castle is attacked",
        "archetype": "Street Samurai",
        "title": "Household enforcer, Castle Laidon (sedated and confined in room T1)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Scottish (MacDonald)",
        "age": 32,
        "organization": "MacDonalds of Glencoe",
        "connection": 1,
        "description": "A hulking brute with buck teeth, freckles, brown hair and eyes and weather-beaten skin that makes him look older than 32. Mildly psychopathic at the best of times, so unpredictable and senselessly violent that the family sedated him and locked him up. A MacDonald the family would prefer to forget.",
        "notes": "If the runners attack the castle it is the one night the domestics forget his medication; James arms him. Stats: B6(8) Q4 S5 C2 I5 W5, Ess 1.5, Reaction 4(8), Initiative 4(8)+3D6; Armed Combat 4, Bike 1, Etiquette (Street) 4, Etiquette (Clan) 5, Firearms 5, Stealth 4, Unarmed 6; dermal plating 2, retractable hand razors, smartlink, Wired Reflexes 2; armor vest, stun baton, sword, Uzi III with internal smartlink and sound suppressor; Threat 5/4. The book calls him brain-damaged; treat the wiring as why.",
    },
    {
        "name": "Hugh MacDonald",
        "role": "Sir Iain's cousin, an exceptional Transys corporate decker who rides shotgun on the runners' decker to keep him honest",
        "archetype": "Corporate Decker",
        "title": "Corporate decker, Transys Neuronet; MacDonald of Glencoe",
        "race": "Human",
        "gender": "Male",
        "nationality": "Scottish (MacDonald)",
        "organization": "Transys Neuronet",
        "connection": 3,
        "description": "One of 'a pair of exceptional MacDonald deckers' on Fuchi Cyber-6 equivalents with Response Increase 2 who accompany the team decker into the research subsystem once Sir Iain grants the new ID codes -- to ensure his safety, and to keep an eye on him.",
        "notes": "Decker archetype (SRII p.51) on a Cyber-6. With Hugh along the Bringing the Child Home run is a cakewalk but no paydata leaves the system. A plausible later contact inside Transys for a team that pleased the Laird.",
        "contact_skills": ["Transys Neuronet system access (with the Laird's blessing)"],
    },
    {
        "name": "Angus MacNab",
        "role": "2.89-meter troll street samurai for hire and Edinburgh's source of unlicensed weapons; proud of the abbots of St. Fillan's, deadly to backstabbers",
        "archetype": "Street Samurai",
        "title": "Muscle and weapons for hire; holds court at the Arbroath Smokie",
        "race": "Troll",
        "gender": "Male",
        "nationality": "Scottish (Fraserburgh)",
        "age": 26,
        "connection": 4,
        "description": (
            "Twenty-six, 2.89 meters and impressively wide even for a troll, skin like a rhino's, "
            "slicked-back black hair and dark brown eyes. Traces his human ancestors to the hereditary "
            "abbots of St. Fillan's near Loch Earn -- MacNab, 'Son of the Abbot' -- and will reel off "
            "famous MacNabs (Sir Allan, Prime Minister of Canada 'afore ye seps stole off wi' oor lands'; "
            "Robert, New Zealand's wartime Minister of Justice; 'Black Gerald MacNab the wife poisoner'). "
            "Never talks about employers; recites Gaelic fairy tales endlessly; brave and loyal for enough "
            "money and a few gallons of heavy. Does not carry the SMG around town."
        ),
        "notes": (
            "Terms: 200 pounds of drinks for a hearing; 5,000 pounds a day plus ammo and repairs (he "
            "declines heavy or military opposition; haggling raises the price 10 percent); weapons and "
            "non-heavy armor at 150-200 percent, no lasers, heavy or military weapons, standard "
            "Availability; refuses all information on other people ('I keep mae trap shut'); knows Dr. "
            "Knox; arranges a safe house for 5,000. 'My clan never forgets treachery' -- Uncle Murdo was "
            "boxed by seps, and his CAS cousins hunted them two years and mailed him the pixie's head in a "
            "Federal Express box. Legwork (TN 6): 'Even the police keep clear of him... Don't haggle.' "
            "Stats: B7(8) Q3(6) S6(9) C1 I2 W1, Ess 0.3, Reaction 2(4), Initiative 4+2D6; Armed Combat 4, "
            "Bike 2, Etiquette (Street) 5, Firearms 5, Stealth 3, Throwing 5, Unarmed 7; muscle "
            "replacement 3, retractable razors, smartlink, Wired Reflexes 1, dermal armor 1; armor vest, "
            "Bond and Carrington Halimark with smartgun adapter (Roomsweeper), Enfield AS-7, great claymore "
            "(monofilament sword, +2 Reach), HK227, Wallacher combat axe, eight shuriken, two defensive and "
            "three smoke grenades, vast ammunition, BUCM Platinum; natural thermographic vision, +1 Reach; "
            "silver allergy (moderate); Threat 5/4. Gets a slice of the Team Karma if he shares the run."
        ),
        "contact_skills": ["Unlicensed weapons and armor in Edinburgh", "Hired muscle (troll samurai)", "Street doc referral (Dr. Knox)"],
    },
    {
        "name": "Hamish MacLeod",
        "role": "Twenty-year-old grizzled ork proprietor of Hamish's Bar; claymore over the bar, Rumormill 5, no nonsense, no drunks",
        "archetype": "Bartender",
        "title": "Proprietor, Hamish's Bar",
        "race": "Ork",
        "gender": "Male",
        "nationality": "Scottish",
        "age": 20,
        "connection": 3,
        "description": "Twenty, tough and grizzled, a sliver under two meters of solid meat, arms crossed and glaring behind the bar. Stands for no nonsense: the claymore over the bar is used when things get out of hand. Close-mouthed with strangers, friendly enough to the men, treats all women as pretty young things, hates people who cannot hold their drink. 'Pints of heavy, is it?'",
        "notes": "A rich source of general Edinburgh information who never knows anything specific -- the GM's device for red herrings and nudges. Second visit: Charisma (9) (-1 for an ork runner), repeated each crawl with drinking, paying and tipping, to make him a contact; then -1 TN on inquiries about Cameron, Quicksilver, Fionnghuala and Duncan. Stats: B7 Q4 S6 C2 I1 W2, Ess 6, Reaction 2; Armed Combat 4, Firearms 4, Etiquette (Street) 4, Unarmed 4; Rumormill 5, Sympathetic Listening 2; armor jacket, claymore (two-handed, Reach 2, (Str-2)S); low-light vision, mild sunlight allergy; Threat 2/2.",
        "contact_skills": ["Edinburgh rumormill", "Who drinks where on Princes Street"],
    },
    {
        "name": "Duncan the Fixer",
        "role": "Rat-faced, obsequious Hamish's Bar fixer in the most hideous tartan in existence; extortionate, cowardly, and never sells bad goods",
        "archetype": "Fixer",
        "title": "Fixer, Hamish's Bar ('Duncan from Hamish's sent you')",
        "race": "Human",
        "gender": "Male",
        "nationality": "Scottish (poses as a Crawford)",
        "age": 29,
        "connection": 3,
        "description": "Short, thin, rat-faced and sallow with a revoltingly pencil-thin mustache, black satin shirts open to the navel over a hairless chest and a gold Celtic medallion, and trousers in the hideous pink-and-green Crawford tartan -- he poses as a Crawford just to wear it. Whining and obsequious, spins the measliest scrap into a tale to justify his fees; keeps an eye out for foreigners, who all end up at Hamish's eventually.",
        "notes": "Approaches on his own. 400 pounds a topic (locations; Fionnghuala, Cameron or Quicksilver; Jackie Stewart), 600 for Angus MacNab, 800 for Dr. Knox's address; -10 percent per net Negotiation success. Buys from MacNab at 25 percent markup only if paid in advance (afraid of angry runners and of the police); fences at 40 percent; offers to buy weapons and cyberware for half the team's Matrix take, 24 hours for anything over 4,000 pounds; safe house 5,000. Talismongers sell only through him, at triple. Paranoid teams may suspect a plant; the trousers alone are grounds. Stats: B2 Q4 S2 C2 I4 W3, Ess 6, Reaction 3; Armed Combat 3, Etiquette (Street) 4, Negotiation 4, Unarmed 3; Ares Viper, armor jacket (when expecting trouble), knife; Threat 1/1.",
        "contact_skills": ["Edinburgh street purchases and referrals", "Fencing (40 percent)", "Forged IDL and vehicle connections"],
    },
    {
        "name": "Fionnghuala Colquhoun",
        "role": "Elven neurophysiology research assistant, back-to-nature believer, half in love with 'Erewan'; the lead to Richardson and the druid Fiona",
        "archetype": "Research Assistant",
        "title": "Research assistant to Professor Colquhoun (Royal Infirmary / University of Edinburgh)",
        "race": "Elf",
        "gender": "Female",
        "nationality": "Scottish (Edinburgh)",
        "age": 28,
        "organization": "University of Edinburgh",
        "connection": 2,
        "description": "A small, slender elf (pronounced 'fin-ell-lah'), 28 but looks 19, fashionably dressed, sitting alone at a side table in Hamish's. Born and raised in Edinburgh; firmly believes in getting back to nature despite living in the city (-1 TN for a rural-totem shaman or a plausible elven nature-lover; an elven decker will not do). Will not be bribed; lies cost +2 TN.",
        "background": "Her father holds the Chair of Neurophysiology and researches at the Royal Infirmary (on sabbatical at the University of Johannesburg during the adventure); her own interest in the field made her his assistant and led to a few evenings' conversation with an elf she knew only as Erewan -- skillsofts and neuromodulators turning to spiritual philosophy, astrology and an obsession with life after death.",
        "notes": "Recognizes the cybereyes, blue scarf and black streak (Charisma (6) or net Negotiation success to admit it). Last saw him three weeks ago; he had 'found someone, a girl' and played with a silver ring (Charisma vs Willpower); a friend at the University, 'Richards, or Richardson... a woman. A human'; a druid 'Fiona something' on Skye with whom he talked astrology -- 'he told me he might leave his feelings there'. Steals medical supplies for a good cause (see the Royal Infirmary). Stats: B2 Q4 S2 C3 I6 W2, Ess 5.3, Reaction 2; Biological Sciences 7, Biotech 5, Cybertechnology 3; knife; Threat 0/1.",
        "contact_skills": ["Neurophysiology and cyberware medicine", "Royal Infirmary supplies (small items, good causes only)"],
    },
    {
        "name": "Professor Colquhoun",
        "role": "Chair of Neurophysiology at the University of Edinburgh, researching at the Royal Infirmary; away on sabbatical in Johannesburg",
        "archetype": "Academic",
        "title": "Professor, Chair of Neurophysiology, University of Edinburgh",
        "race": "Elf",
        "gender": "Male",
        "nationality": "Scottish",
        "organization": "University of Edinburgh",
        "connection": 2,
        "description": "Fionnghuala's father, holder of the university's Chair of Neurophysiology with a research post at the Royal Infirmary. Off-stage throughout Imago on sabbatical at the University of Johannesburg.",
        "notes": "Race inferred from his daughter. A future medical-cyberware contact of real standing, and the reason Fionnghuala met Quicksilver at all.",
    },
    {
        "name": "Jackie Stewart",
        "role": "Cheerful, honest, slightly shifty-looking rigger who runs Edinburgh's best vehicle rental and can forge you a driving license",
        "archetype": "Rigger / Vehicle Dealer",
        "title": "Proprietor, Stewart's Hyperdrive, Leith Walk",
        "race": "Human",
        "gender": "Male",
        "nationality": "Scottish (Inverness)",
        "age": 37,
        "connection": 3,
        "description": "Medium build and height, sallow complexion, dark lank hair, brown eyes, dirty overalls and oily hands rubbed together in a not altogether reassuring way. Born and raised in Inverness; five years building the leading rental and repair firm in Edinburgh. Cheerful and honest but reserved with foreigners, with a disconcerting habit of looking slightly away from whoever he is talking to. 'Driving license?'",
        "notes": "See Stewart's Hyperdrive for terms. Temporary IDL 6,000 pounds; the hovertruck through brother Angus in Pitlochry; the best route to Skye; warns you off the police and the paranaturals. Half-price rental for a week and 10 percent off purchase if the team fights the Tartan Army for him -- unarmed. Stats: B2 Q4 S4 C3 I3 W3, Ess 4.8, Reaction 4; Armed Combat 3, Computer 3, Computer Theory 4, Electronics 4, Electronics B/R 6, Etiquette (Street) 3, Ground Vehicles B/R 8, Negotiation 4; datajack, Vehicle Control Rig 1; Ares Predator, armor jacket, knife; Threat 2/2.",
        "contact_skills": ["Vehicles for the Highlands (sale, rental, repair)", "Forged international driving licenses", "Road routes and Wild Lands fuel stops"],
    },
    {
        "name": "Angus Stewart",
        "role": "Jackie Stewart's brother in Pitlochry, owner of the Nissan Hovertruck that gets a team to Skye in fourteen hours",
        "archetype": "Mechanic",
        "title": "Garage owner, Pitlochry",
        "race": "Human",
        "gender": "Male",
        "nationality": "Scottish (Inverness)",
        "connection": 2,
        "description": "Jackie's brother, who keeps a Nissan Hovertruck in his garage at Pitlochry and 'might let you rent it if you stay outside the sprawl'. Never met in the book; all dealings go through Jackie.",
        "notes": "2,500 pounds a day, 2,250 negotiated, a week in advance, 50,000-pound deposit. Withdrawn if the team makes the news as gun-toting Americans.",
    },
    {
        "name": "Fiona Mac Mhuirich",
        "role": "Wild, innocent Skye-born Eagle druidess who holds the Affect chip Quicksilver left her at the solstice and asks for a piece of the runners in return",
        "archetype": "Druid",
        "title": "Druid of Dunvegan (Eagle shaman); keeper of the Affect chip",
        "race": "Human",
        "gender": "Female",
        "nationality": "Scottish (Isle of Skye)",
        "age": 25,
        "organization": "Druids of Dunvegan",
        "connection": 3,
        "description": "Twenty-five, above average height, slim, long blond hair and green eyes, Skye born and bred and slightly wild, knowing little of the outside world: open, happy, blessed with an inner harmony that made a sophisticated elf feel at peace. Wears the crab of Cancer. Listens in silence, then: 'If I give part of him to you, you must give of yourself to me, for how else will I know you are fit to hold him?'",
        "background": "Quicksilver told her little of his work and gave her the Affect chip at the last solstice simply because he trusted her, asking her to keep it until the time felt right; she would know. She does not know he is dead, but she trusts the runners -- and holds the image of a sealed wooden box very dear.",
        "notes": "Runs the midnight rite (see the Druids of Dunvegan), holds the drained magician's head afterwards, fetches the black box, and tells of the presence at Loch Ness. Stats: B3 Q3 S3 C5 I4 W6, Ess 6, Magic 6, Reaction 3; Conjuring 7, Enchanting 2, Etiquette (Druidic) 5, Magical Theory 2, Sorcery 5, Stealth 3, Unarmed 3; golden sickle and mistletoe fetishes, robes; Totem Eagle; Spells: Heal 4, Treat 4, Hibernate 2, Levitate Item 2; Threat 3/3. Quicksilver recognized her as a friend from a previous life.",
        "contact_skills": ["Druids of Skye and the Sickle Ley", "Conjuring (Eagle)"],
    },
    {
        "name": "Finniaen MacNaughton",
        "role": "Weary, scowling elven leader of the Dunvegan druids with oak and ash ankh staffs and a golden-sickle focus; casts Analyze Truth while you talk",
        "archetype": "Druid",
        "title": "Leader of the Druids of Dunvegan (Eagle shaman)",
        "race": "Elf",
        "gender": "Male",
        "nationality": "Scottish (Isle of Skye)",
        "organization": "Druids of Dunvegan",
        "connection": 3,
        "description": "The elf who clearly leads the white- and gray-robed procession, carrying a pair of ankh-tipped staffs, one oak and one ash, and wearing the ram of Aries. Waves tourists away with a weary expression, turns back for any mage or shaman, scowls at street shamans, and cold-shoulders anyone with Essence under 2. Speaks only to the magicians. 'Don't waste my time, what do you want?'",
        "notes": "Only the name Quicksilver makes him fetch Fiona. Casts a Force 7 Analyze Truth as the runners explain themselves and whispers the results to her; embroidery beyond slight earns a warning. Attuned to Eagle; carries an enchanted golden-sickle focus (assensing, 1-2 successes). No stat block -- use Fiona's as a floor and raise it. Leads the twelve at midnight.",
    },
    {
        "name": "Dr. Knox",
        "role": "Fiftyish, balding, whisky-scented body-shop doc who does great work slightly steaming and falls apart when the trid shows his patients' faces",
        "archetype": "Street Doc",
        "title": "Proprietor, Dr. Knox's Body Shop",
        "race": "Human",
        "gender": "Male",
        "nationality": "Scottish",
        "age": 50,
        "connection": 2,
        "description": "About fifty, slight build, balding gray hair, watery blue eyes, a faint smell of whisky. Steady and skilled with a couple of drinks in him, shaky sober, dangerous when properly steaming. Off the stimulants now. The clinic is clean and the equipment sterilized.",
        "notes": "Street Doc archetype (SRII p.211). Reached through Duncan (800 pounds) or Angus; see the Body Shop for fees, patches, house calls, and the three-day nerve limit. Dr. Knox of Edinburgh's body shop is, of course, a name with history.",
        "contact_skills": ["Unlicensed medical care in Edinburgh"],
    },
    {
        "name": "Peter Albrecht",
        "role": "Prosperous Seattle fixer who fronts for corporations that will not use their own negotiators; brokered the Imago job for 500 nuyen a day",
        "archetype": "Fixer",
        "title": "Fixer and corporate intermediary, Seattle",
        "race": "Human",
        "gender": "Male",
        "connection": 4,
        "description": "Gray-suited, prosperous-looking, wiry graying hair and a five o'clock shadow, an aluminized briefcase and a broad grin. Relaxed, no sign of stress, sarcastic when asked to do a runner's homework ('check the public bulletin boards'). 'Scotland's lovely this time of year. Best whisky in the world and the men wear skirts. It's a pushover.'",
        "notes": "Knows Cameron's name and (Negotiation vs Willpower) Transys; not the missing man's. Pays round-trip suborbital, expenses and 500 nuyen per person per day for a week minimum (+5 percent per net success), revised if it turns violent -- and picks up the lobsters. Forged passports, visas and cyberware licenses by Raul Esterhazy, ready next day, valid only for the job; no weapon licenses at all, cyberweapons written up as legal augmentation. Negotiation 4. Suite on the eighth floor of the Stouffer-Madison.",
        "contact_skills": ["Foreign corporate Johnsons (British and European)", "Forged papers via Raul Esterhazy"],
    },
    {
        "name": "Raul Esterhazy",
        "role": "One of the best forgers in North America; Albrecht's man for passports, visas and cyberware licenses that pass British Customs",
        "archetype": "Forger",
        "title": "Forger (North America)",
        "race": "Human",
        "gender": "Male",
        "connection": 4,
        "description": "Never seen; a name Albrecht drops on a private telecom call to reassure a nervous team, and one any runner with Etiquette (Street) (3) recognizes as one of the best forgers on the continent.",
        "notes": "His British passports live on forged credsticks and pass because someone illicitly inserted the datafile into one or more of the credstick/ID verification databases (Sprawl Sites p.126; Neo-Anarchists' Guide p.103). The hard copy reads slightly differently from the electronic check -- an Intelligence (9) official notices. He will not forge weapon licenses for Britain.",
        "contact_skills": ["Top-grade forged ID, passports and licenses"],
    },
    {
        "name": "Great Free Spirit of Loch Ness",
        "role": "Force 14 great free forest spirit of the loch shore, Quicksilver's spiritual guardian across lifetimes; keeper of the Memory chip; sells it for Karma",
        "archetype": "Great Free Spirit",
        "title": "The 'presence' at the lochside; free forest spirit with Loch Ness as its personal domain",
        "race": "Free Spirit (Forest)",
        "gender": "Unknown",
        "organization": "Druids of Loch Ness",
        "connection": 5,
        "description": "Very powerful and willful, it manifests near the ruins of Castle Urquhart, commands the runners to stop, tells them it knows why they came, and invites everyone with Essence 2 or more onto the astral plane. 'A real tough bugger.' It recognized Quicksilver as a being of power and wisdom whose freely given Karma fed it far more Spirit Energy than usual, and has grown fat on a long association with the local druids.",
        "notes": "Force 14, Spirit Energy 30 on the shores of Loch Ness; B18 Q24 S18 C14 I14 W14, Ess 14 (A), Reaction 12, Initiative F-2 (+10/-20)+1D6; Powers: Accident, Astral Gateway, Concealment, Confusion, Dispelling, Fear, Immunity to Normal Weapons, Personal Domain (Loch Ness). The quest: the Dweller on the Threshold reveals a secret about each runner (a GM-chosen test at TN 6; two successes = +1 Karma Pool for the quest; Bear/Wolf +1, Eagle +2; none = dismissed), then the Place of the Past, where each relives his worst hour in a bygone age -- a samurai as a medieval knight, a decker in Thebes or Atlantis, an elven mage in John Dee's England (Willpower (8) for non-combat ordeals; 'dying' just ends it). Price: 5 Karma less one per passed test, minimum 1, from Good Karma or permanent Karma Pool (never the Team Pool; Karmic Debt at two-for-one if broke). Pays out a green Memory chip. Attack it and it smears the team across the lochside: 'simply inform all the runners that they died in this place.'",
    },
    {
        "name": "Nessie",
        "role": "The Loch Ness monster -- a gigantic freshwater serpent, Threat 7, immune to normal weapons, fond of waterweed, that follows hovertrucks and sinks when hurt",
        "archetype": "Paracritter",
        "title": "Gigantic Freshwater Serpent of Loch Ness",
        "race": "Gigantic Freshwater Serpent",
        "gender": "Female",
        "connection": 1,
        "description": "Surfaces about fifty yards behind any hover vehicle on the loch and follows it; dutifully splashes about as the runners leave if she has not appeared. Attacks only in self-defense. 'This explanation becomes particularly difficult if the runners get bitten by Nessie.'",
        "notes": "Stats: B4/1 Q5x3 S9 W1/3, Ess 3, Reaction 6, Initiative 5+1D6, Threat 7, bite 6S2 (-1 Reach); Enhanced Physical Attributes (adds Essence to Body, Quickness or Strength once a day for 12 turns), Fear, Immunity to Normal Weapons, Sonic Projection; dietary requirement Loch Ness waterweed (nuisance). Sinks out of sight when Seriously wounded; attacking her earns +2 TN on every test in the area and the slow displeasure of the druids.",
    },
    {
        "name": "Sir Iain Greig",
        "role": "Ailing President/CEO of Transys Neuronet whose heir apparent is decided by how Imago ends",
        "archetype": "Corporate Executive",
        "title": "President/CEO, Transys Neuronet",
        "race": "Human",
        "gender": "Male",
        "nationality": "Scottish",
        "organization": "Transys Neuronet",
        "connection": 3,
        "description": "The ailing head of Transys Neuronet, named in every corporate profile and quoted in none; retains nominal control in the failure ending while Donald Menzies runs the company day to day, and confirms Sir Iain MacDonald as Deputy President in the success ending.",
        "notes": "Not to be confused with Sir Iain MacDonald. Off-stage; the spokesperson's 'necessary rationalization and harmonization of upper-echelon relations' is issued in his name.",
    },
    {
        "name": "Johnathan Cooper",
        "role": "Division Head of Transys Neuronet GB, the corporation's principal division",
        "archetype": "Corporate Executive",
        "title": "Division Head, Transys Neuronet GB",
        "race": "Human",
        "gender": "Male",
        "nationality": "British",
        "organization": "Transys Neuronet",
        "connection": 2,
        "description": "Head of Transys Neuronet GB per the SeaSource/C-net corporate profile. Never appears.",
        "notes": "Corporate-profile texture (spelled 'Johnathan' in the book). Survives both endings unmentioned.",
    },
    {
        "name": "Donald Menzies",
        "role": "Transys Finance Director: purged with six of his executives if the runners succeed, running the company and courting Zeta if they fail",
        "archetype": "Corporate Executive",
        "title": "Finance Director, Transys Neuronet",
        "race": "Human",
        "gender": "Male",
        "nationality": "Scottish",
        "organization": "Transys Neuronet",
        "connection": 3,
        "description": "The Transys Finance Director. In the success handout he and six senior executives in his division are dismissed from the board; in the failure handout the day-to-day running of the 'troubled giant' falls to him, he confirms James McLaughlin as Acting Chairman, and rumor makes him the force behind John Cawdor's elevation -- while analysts expect a Zeta-ImpChem takeover.",
        "notes": "The book never says so outright, but the purge lists read as Sir Iain's list of the enemy within. A likely Zeta asset; treat as the faction leader of the 'people in the company who don't want him back'.",
    },
    {
        "name": "James McLaughlin",
        "role": "Transys senior research director, dismissed in the success ending and made Acting Board Chairman in the failure ending",
        "archetype": "Corporate Executive",
        "title": "Senior Research Director, Transys Neuronet",
        "race": "Human",
        "gender": "Male",
        "nationality": "Scottish",
        "organization": "Transys Neuronet",
        "connection": 3,
        "description": "The research staff's senior director -- Quicksilver's nominal superior -- dismissed with several senior research scientists when Sir Iain MacDonald takes control, or promoted to Acting Board Chairman by Menzies when Sir Iain 'resigns'.",
        "notes": "With Menzies and Cawdor, the boardroom face of the Zeta faction. Never met in play.",
    },
    {
        "name": "John Cawdor",
        "role": "Junior Transys research director whom Menzies elevates to a full board seat in the failure ending",
        "archetype": "Corporate Executive",
        "title": "Junior research director, Transys Neuronet (Director in the failure ending)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Scottish",
        "organization": "Transys Neuronet",
        "connection": 2,
        "description": "A junior research director whose sudden rise to full Director with a board seat rumor credits to Donald Menzies. Cawdor is a Campbell name -- the book does not remark on it.",
        "notes": "Failure-handout texture; a plausible candidate for the corporate decker who ambushed the team, if the GM wants a face.",
    },
    {
        "name": "Harald Meier",
        "role": "President/CEO of Zeta-ImpChem, 'unavailable for comment' on the takeover of Transys",
        "archetype": "Corporate Executive",
        "title": "President/CEO, Zeta-ImpChem (Interlaken)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Swiss",
        "organization": "Zeta-ImpChem",
        "connection": 3,
        "description": "Head of the Anglo-Swiss megagiant at its Interlaken headquarters; his spokesperson says Zeta 'has always been interested in acquiring gold-chip research'.",
        "notes": "Named only in the failure handout. Whether he ordered the Laidon murders or merely benefits is the GM's call.",
    },
    {
        "name": "David Gray Bear",
        "role": "President of Gaetronics Corporation and brother of the Salish-Shidhe chief; his 14-year-old son Robert is missing and he has posted 20,000 nuyen",
        "archetype": "Corporate Executive",
        "title": "President, Gaetronics Corporation (Seattle)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Salish",
        "organization": "Gaetronics Corporation",
        "connection": 3,
        "description": "Seattle corporate president, brother of Harold Gray Bear of the Salish-Shidhe Council. Maintains that no one has threatened his family and that no demands have been made; could not be reached for further comment.",
        "notes": "October newsnet (byline P. Daza). Lone Star has no leads, discounts foul play, and promises an arrest by the end of the week. Hook material for a Seattle-based follow-up.",
    },
    {
        "name": "Robert Gray Bear",
        "role": "Fourteen-year-old son of the Gaetronics president, missing in Seattle -- gang trouble or kidnapping, nobody knows",
        "archetype": "Missing Person",
        "title": "Missing minor (Seattle); nephew of Harold Gray Bear",
        "race": "Human",
        "gender": "Male",
        "nationality": "Salish",
        "age": 14,
        "connection": 1,
        "description": "Vanished the week of the October newsnet; rumors first said gang-related, Lone Star now says possibly kidnapped. No ransom demand, no leads, a 20,000-nuyen reward from his father.",
        "notes": "News texture only; the book never resolves it. Leave him missing until a GM needs him.",
    },
]

ORG_UPDATES = {
    "Renraku Computer Systems": {
        "notes_append": (
            "Imago: Seattle's public bulletin boards and information service, SeaSource, is a Renraku "
            "subsidiary; it compiled the U.K. and Scotland briefing handouts (and lists Renraku U.K. among "
            "the major foreign corporate presences in Britain). Transys Neuronet's rumored biological "
            "cyberdeck is compared to 'what I heard about Renraku a while back'."
        ),
    },
    "Fuchi Industrial Electronics": {
        "notes_append": (
            "Imago: Fuchi Industries U.K. is one of the major foreign corporate presences in Britain. "
            "Fuchi Cyber-4 and Cyber-6 decks are the workhorses of Transys Neuronet's deckers (Cameron, the "
            "hostile corporate decker, the MacDonald escorts); Quicksilver's own deck wears a Fairlight "
            "Excalibur case over something no Fuchi engineer would recognize."
        ),
    },
    "Aztechnology": {
        "notes_append": "Imago: Aztechnology is listed among the major foreign corporate presences in the United Kingdom (SeaSource U.K. fact sheet). Quicksilver traveled Aztlan in his youth.",
    },
    "Aztlan": {
        "notes_append": "Imago: the elf Quicksilver, born in South Wales in 2021, traveled Aztlan among the Welsh and Scottish Wild Lands, Tir Tairngire, the California Free State, Tir Nan Og and the Middle East before joining Transys Neuronet in 2048.",
    },
    "Tir Tairngire": {
        "notes_append": (
            "Imago: Quicksilver, a unique elf born in Wales in 2021, traveled the Tir before 2048. The "
            "(elven) Scots druids of Skye and Loch Ness 'most likely have friends in Tir Tairngire, the "
            "Salish-Shidhe Council, or other North American lands' -- a druidic grudge from Scotland could "
            "arrive in Seattle by way of Portland, and a long time coming."
        ),
    },
    "Salish-Shidhe Council": {
        "notes_append": (
            "Imago (October 9 newsnet, template-dated 2051): Harold Gray Bear is described as 'Chief of the "
            "Salish-Shidhe Council' (Peacekeeper recorded him as the Council's spokesman -- discrepancy "
            "kept, not resolved); his brother David Gray Bear is president of Gaetronics Corporation, and "
            "his nephew Robert, 14, is missing in Seattle with a 20,000-nuyen reward posted. The Scots "
            "druids are said to have friends on the Council."
        ),
    },
    "Lone Star Security": {
        "notes_append": (
            "Imago (October 9 newsnet, template-dated 2051): spokesperson Jules Nedich announces that Lone "
            "Star has acquired and deployed at least three military-surplus GMC Banshee VI LAVs configured "
            "for riot duty -- tear and stun gas dispensers, water and stun-slug cannons, six to eight riot "
            "officers each -- stationed around Seattle for rapid emergency response, 'not patrol craft'. "
            "Governor Schultz's office approves; one official: 'Otherwise, those LAVs will just be fraggin' "
            "big stun batons.' Lone Star also has no leads on the missing Robert Gray Bear and discounts "
            "foul play. For contrast, Edinburgh's police are lightly armed, rarely carry automatics, "
            "respond in four minutes, and shoot to kill."
        ),
        "leadership_add": [
            {"name": "Jules Nedich", "title": "Spokesperson", "notes": "Announced the Banshee VI LAVs (Imago newsnet)."},
        ],
    },
    "Seattle Metroplex Guard": {
        "notes_append": "Imago (October 9 newsnet, template-dated 2051): Governor Schultz's office publicly supports Lone Star's purchase of GMC Banshee VI LAVs, with the proviso that the firm back the hardware with more officer training.",
    },
    "Seattle News-Intelligencer": {
        "notes_append": (
            "Imago: the two Update-Net handouts (pp.74-75) carry the recycled template date Monday October "
            "9 2051 although the adventure is set in 2053. Shared items: Johnny Spinrad announces the "
            "acquisition of the Principality of Monaco from Lisbon ('Everybody's got to have a hobby'); "
            "Who's News catches Johnny Pomp-Adore leaving a Manhattan hotel by a questionable portal "
            "('Bad hair like yours hardly needs acknowledgment'; Voodoo Chili at The Bog Knobi Club; "
            "'Lifestyles of the Rich and Organic', Section 6B); Sports: 'Everybody lost'; Lone Star's LAVs "
            "(T. Dowd); the missing Robert Gray Bear (P. Daza). Success lead (C. Sargent): 'Board Changes "
            "in Powerful U.K. Corporation'. Failure lead: 'British Corporation in Turmoil'. Update-Net "
            "sections: Local, World, Sports, Weather, Business, Lifestyle, Entertainment."
        ),
    },
    "DocWagon": {
        "notes_append": "Imago: DocWagon contracts may not apply in the United Kingdom; visitors buy the British equivalents from Careline or BUCM (Gold 600 pounds a week, Platinum 1,500), and nothing covers the Scottish Wild Lands.",
    },
}

LOC_UPDATES = {}

NPC_UPDATES = {}

TAG_EXISTING = {}

MATRIX_HOSTS = """
**Transys Neuronet -- Research Subsystem 1** (Edinburgh; SAN (311)411, unlisted). A sculpted,
bio-organic system (Virtual Realities p.51; think Giger): nothing manufactured, IC as predatory animals
and micro-organisms, nodes as viscera, cortex folds or verdant woodland; metal on a persona becomes
leather or cloth. All IC uses the hardened-defense option. Load ratings shown as (max/current); any
overload or slowdown alerts the system even with Cameron's passcodes, which cover the white and gray IC
of this cluster only. After Cameron's death the codes change and the system sits on passive alert.

| Node | Function | Rating | IC |
|---|---|---|---|
| SAN-1 | Directory (311)411 | Green-3 (6/4) | Access 4, Trace and Report 4 |
| SPU-1 | Data routing | Orange-4 (12/10) | Access 4, Tar Pit 4 |
| SPU-2 | Administration | Red-3 (12/10) | Barrier 5, Probe 4, Jammer 4 |
| DS-1 | Basic records/files | Orange-4 (12/6) | Tar Pit 4 |
| I/OP-1 | Terminals | Orange-4 (12/6) | Access 5, Trace and Dump 4 |
| SPU-3 | Security | Red-3 (12/7) | Access 7, Black 4 |
| SM-1 | Sensors | Orange-4 (12/5) | Probe 4, Trace and Report 3 |
| SM-2 | Cameras | Orange-4 (12/8) | Access 4, Blaster 4 |
| SM-3 | Maglocks (interior) | Orange-4 (12/8) | Access 4, Blaster 4 |
| SPU-4 | Personnel | Orange-5 (15/8) | Barrier 5, Trace and Report 4, Acid 4 |
| DS-2 | Personnel records | Orange-4 (12/10) | Barrier 6, Blaster 5 |
| I/OP-2 | Terminals | Orange-4 (12/4) | Access 5, Trace and Report 4 |
| SPU-5 | Ongoing research | Red-3 (12/9) | Access 6, Killer (S) 4 |
| DS-3 | Updating buffer | Red-3 (12/9) | Scramble 6, Blaster 4 |
| I/OP-3 | Biological monitors | Red-3 (12/8) | Access 6, Jammer 5 |
| I/OP-4 | Terminals | Red-3 (12/9) | Access 6, Blaster 4 |
| SPU-6 | Data routing | Orange-4 (12/6) | Access 5, Tar Baby 4 |
| SPU-7 | System security | Red-3 (12/10) | Acid 4, Blaster 4 |
| SPU-8 | R&D master node | Red-3 (12/3) | Black 3 |
| DS-4 | Ongoing research data (400 Mp) | Red-2 (8/3) | Black 3 |
| DS-5 | Research projections (150 Mp) | Red-2 (12/3) | Black 3 |
| CPU | Central Processing Unit | Red-5 (20/13) | Killer (S) 7, Trace and Dump 6 |
| DS-6 | Back-up files (800 Mp) | Red-4 (16/11) | Barrier 6, Scramble 5, Killer (S) 4 |
| DS-7 | Back-up records (700 Mp) | Red-4 (16/12) | Barrier 6, Scramble 5, Blaster 5 |
| SPU-9 | Security node (gateway to the other research subsystems) | Red-3 (12/10) | Access 5, Killer (S) 4, Trace and Dump 5 |

Topology (p.21 map): SAN-1 -> SPU-1 -> {SPU-2 (DS-1, I/OP-1), SPU-3 (SM-1, SM-2, SM-3), SPU-4 (DS-2,
I/OP-2), SPU-5 (DS-3, I/OP-3, I/OP-4)}; SPU-1 -> SPU-6 -> SPU-7 -> SPU-8 (DS-4, DS-5) -> CPU (DS-6,
DS-7) -> SPU-9 -> other research subsystems (improvise: plenty of gray and black IC). Paydata in DS-4
to DS-7: neurophysiological implants and monitors, about 5,000 nuyen per 10 Mp. The Child appears in
DS-5, DS-6, DS-7 or the CPU once the decker has mapped half the system (the map matters later), or in
the third datastore hacked on the second visit; it neutralizes IC with a wave and ignores Load. The
hostile corporate decker (gray hooded robe; Computer 6, Cyber-4 with Response Increase 1, Bod 5 /
Evasion 4 / Masking 4 / Sensors 5, Armor 4, Attack 5, Poison 4, Shield 4) strikes at SPU-2 or SPU-6 and
retreats through the CPU and SPU-9 at Serious MPCP damage. With Sir Iain's codes, Hugh MacDonald and a
second MacDonald decker on Cyber-6s (Response Increase 2) ride along and no downloading is allowed.

**Castle Laidon security system** (Glencoe; hard-wired, no listed SAN). Hacking it disables the
razor-wire cameras, the retinal-ID gate maglocks and the gatepost SMGs.

| Node | Function | Rating | IC |
|---|---|---|---|
| SAN | Entry | Orange-2 (6/0) | -- |
| SPU-1 | Security monitoring | Orange-4 (12/6) | Access 4, Trace and Dump 4 |
| I/OP-1 | External cameras | Orange-2 (6/0) | -- |
| I/OP-2 | Maglocks | Orange-2 (6/0) | -- |
| SPU-2 | Active security and internal monitoring | Orange-4 (12/5) | Barrier 4, Acid 3 |
| I/OP-3 | Front gate guns | Orange-2 (6/0) | -- |
| I/OP-4 | Internal cameras (roof and basement) | Orange-2 (6/0) | -- |
| I/OP-5 | Terminal, monitor display (room S3) | Orange-2 (6/0) | -- |
| CPU | Central Processing Unit | Orange-5 (15/8) | Killer (M) 5, Binder 3 |
| DS-1 | General data storage (no commercial value) | Orange-2 (6/0) | -- |

Two fighting men sit in S3; one has rudimentary Computer/Electronics to run it.

**Quicksilver's cyberdeck** -- not a host, but the adventure's Matrix centerpiece: a Fairlight
Excalibur case with a couple of hitcher jacks over a bio-computer / biological interface processor
nobody can read (Computer B/R (6) and Computer Theory (8) tables, p.66), four one-inch cubic chip
depressions, no function without at least one chip, no Matrix once a chip is slotted. Assensing: TN 12
minus 2 per chip present. Once the Child is inside, no chip can be removed. Inert after the finale.

**C-net** (U.K. national public information net) and **SeaSource** (Seattle, Renraku): news, transport
schedules, weather, tartan pattern programs (Computer (4)), public birth and death registers, newsdata
archives (no test), the University of Edinburgh LTG directory. British datanets restrict even trivial
personal information; hacking them turns up little.

**Transys Barrie reward deck** -- MPCP 8, Hardening 4, Memory 120, Storage 500, Load 50, I/O 30,
Response Increase 2, two hitcher jacks; a hidden MPCP alarm flags any Transys SAN (Computer B/R (9) to
find, again to remove; failure costs an MPCP point).
"""

NOT_BUILT = """
- **The hostile Transys decker** (gray hooded robe), the two elderly domestics (cook and butler), the
  six Scottish staghounds, the four/six MacDonald fighting men, the dead castle mage, Alexander and
  Rory MacDonald (Sir Iain's murdered 13-year-old twin nephews), Robert and Donald Campbell of Argyll
  (the planted corpses), Uncle Murdo MacNab and the CAS cousins, Jocky (Stewart's getaway driver),
  Stewart's ork mechanic and dowdy secretary, the Tartan Army leader and his pit bull, the Zeta strike
  teams (five/six samurai, two troll samurai, rigger, combat mages), the airport officials ('MacDougal'),
  the customs mages, Cameron's two brothers -- on the org / location rows.
- **The piasma** (escaped from the Inverness naval base), the free nature spirits and watcher spirits of
  Loch Ness, the twelve mountain and forest spirits of the Dunvegan rite, the **Dweller on the
  Threshold**, the collective **ghosts of the 1692 massacre** and the **Spirit of Man** as a 1692
  MacDonald chieftain -- on the location / NPC rows.
- **Careline** (the other British insurer), **Integrated Weapon Systems PLC** (the strike chopper),
  **British Industrial PLC** (the Hunter-Wagner bikes), **Hildebrandt-Kleinfort-Bernal** (HKB, London
  financial analysts, possible third-party bidder), **Grenville-Adams PLC**, **Amalgamated Technologies
  and Telecommunications**, **Fuchi Industries U.K.** and **Renraku U.K.**, the airlines (British
  Midair, Geordie Airlines, British Comet, Sinclair Skies), **BritRail**, the Royal Bank of Scotland and
  Clydesdale Bank, **Clan MacNab**, the U.K. legal helplines, the National Health Service -- on the
  org rows.
- **King George VIII**, the Green Party government, the Scottish Regional Parliament in Edinburgh
  Castle, Holyrood House, Arthur's Seat, Kyleakin, Invergarry, Spean Bridge, Inverness and its naval
  base, Glasgow, Dundee, Iona, the Midmar stone circles, Flatholme prison island, New Tollbooth Prison,
  the Scottish Museum of Metahuman Arts and Crafts, the National Museum of Scotland, Pollock Hall, Loch
  Earn and St. Fillan's -- not recorded as locations.
- News names: **Johnny Spinrad** (buying Monaco), **Johnny Pomp-Adore**, The Bog Knobi Club, the
  bylines C. Sargent, T. Dowd and P. Daza -- on the News-Intelligencer row.
- The horoscope (Sun 19 Sagittarius, rising 25 Sagittarius, Moon 9 Libra, Mercury 1 Sagittarius,
  Venus 1 Aquarius, Mars 15 Aquarius, Jupiter 12 Taurus, Saturn 24 Libra, Uranus 18 Cancer, Neptune 23
  Libra, Pluto 23 Leo, MC 1 Scorpio; 'I rose here as a Man'), British slang and Scots dialect (p.79) --
  GM color, kept in the book.
"""

PLAY_NOTES = """
- This is a love story with two dead lovers and a foreign country that strips the runners of guns,
  contacts, licenses and money. Play the culture shock straight: kilts, red tape, warm heavy, 'seps',
  TN 8 for every British contact, pounds not nuyen. Read the U.K. handouts and Anarchy in the U.K.
  before the airport; bust someone for a forgotten knife.
- Themes to seed casually: lost love, fragmentation, rebirth -- the woman with the lost purse, a child
  who cannot find all the parts of his doll, a newborn who looks like his dead grandfather, a glass that
  shatters into a thousand pieces. Rain from a cloudless sky.
- The Transys run is a set-up: free passage with Cameron's codes, then an ambush from inside the company.
  Let the players draw the conclusion that someone in Transys is acting on his own.
- Cameron must die the morning the team leaves for Skye; his pointing arm is the clue. Count Combat
  Turns in the flat. Surrender ends the adventure; a firefight with the police makes Edinburgh
  unlivable and Kyle of Lochalsh the new base.
- Dunvegan: the druids look like charlatans until the spirits erupt. Make the magician's player decide,
  turn by turn, how much of himself to give, without knowing the ten-turn limit. Chickening out ends
  the adventure unless someone else steps in.
- Loch Ness: build each runner's Place of the Past from his own history, in period costume; never a
  hopeless fight -- 'true fear comes from the hope of living when the odds are against it.' Karma is
  the price; Karmic Debt if they cannot pay.
- Castle Laidon rewards talk over guns: violence there costs the team Sir Iain, the cavalry, and the
  funeral of a Zeta strike team. Morag speaks only through a volunteer.
- Sir Iain holds all the cards; the runners are bait and he says so to nobody. Every concession is a
  separate opposed Negotiation at +2 less what they can prove.
- The finale is choreography: preparations (oil-slick stairs, boarded windows, a spirit outside) buy
  turns; the primary decker cannot jack out and takes a Force 4 stun bolt per stage; the chips end
  inert; hand over the deck with grace. Karma: 12 for the ordeal (8 if bribed), +1 preparation, +2
  survival, double drama, +1 Skye magician, +1 Loch Ness questers.
- Loose ends: a druidic grudge that travels to Tir Tairngire or the Salish-Shidhe; Zeta-ImpChem's
  memory of the Americans; the Transys Barrie's hidden alarm; Amelia and the Sidgwickites asking what
  happened in the metaplanes; Robert Gray Bear still missing back home.
"""
