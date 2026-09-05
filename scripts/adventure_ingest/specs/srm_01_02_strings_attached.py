# SRM 01-02 Strings Attached (FanPro / WizKids, 2004, Shadowrun Missions Season One, SR3) --
# campaign order #45. Renton (Greenwood Memorial Park) and Tacoma (the Kethers Building, 1366
# Crescent Boulevard, and the sewers under it), with Rose Croix's new offices downtown.
# SETTING NOTE / DISCREPANCY WITH THE TASK BRIEF: commissioned as "Denver in the 2060s (SR4 era)";
# the book is Seattle and "For use with Shadowrun, Third Edition". Denver is never mentioned. Every
# location carries city "Seattle".
# Dating: no in-world date is printed. Internal anchors: the adventure is "about a month" after the
# shareholders' meeting of SRM 01-01; Michelle Rampling "has lived in Seattle since 2046"; Timothy
# Van der Loff started as a janitor in the Kethers Federal Reserve Building "in 2015" and was made
# department head "in 2054"; the Federal Reserve left the building in 2020 when President Jarman
# dissolved Washington State; Crash Cart died "in the early fifties"; DocWagon has held the building
# "for over 12 years". YEAR follows 01-01 at 2064.
# Editing inconsistencies in the book, noted again on the affected rows: primary target #99-804 is
# "Donald Ramos -- Trideo Actor", said to be "a cousin of Domingo Ramos, of Aztechnology", but the
# player handout's screamsheet has "trideo action hero Domingo Ramos" cutting the ribbon at Rose
# Croix and signing as its Ebony-level spokesman -- the two Ramoses are swapped between text and
# handout. There are also two maintenance Tims: Timothy Van der Loff, Head of Building Maintenance
# since 2054, and Tim Reed, "one of the maintenance technicians", who is the ghouls' contact known
# to them only as "Tim" from the name sewn on his shirt. The handout calls the company "Rose Croix
# Biomedical Solutions" where the adventure text always says "Rose Croix". The DocWagon host is
# printed as "Orange-6 10/10/13/11/10" -- five subsystem ratings where SR3 wants five, so the code
# is complete, but the security sheaf lists two separate events at trigger step 020 and two at 043.
# Rows created by earlier specs are updated, never re-created: Michelle Rampling comes from
# specs/srm_00_01_mission_briefing.py; Rose Croix, Michael Davenport (as Walter Broward), Garrett
# Walsh, Earl Peabody and the Kethers Building itself come from specs/srm_01_01_double_cross.py.
# Source text: docs/Adventures/text/SRM01-02A_Strings_Attached.txt (30 pages) and
# docs/Adventures/text/SRM01-02B.txt (player handouts).
# ASCII only (pre-commit hook).

ADVENTURE = "SRM 01-02 Strings Attached"
ORDER = 45
SOURCE = "SRM01-02A_Strings_Attached.pdf, pp. 3-30; SRM01-02B.pdf (player handouts)"
YEAR = "2064 (about a month after SRM 01-01 Double Cross; no in-world date is printed)"

SYNOPSIS = """
A month after his own funeral, Michael Davenport is back from the Carib League with a new face, a
Boston University diploma and the name **Dr. Walter Broward**, sitting in a real leather chair as
Chief Executive Officer of **Rose Croix**. Embezzled DocWagon money, his own funds and private
venture capital have bought him clinics, equipment and staff. What he needs now is clients and one
loose end tied off -- because to fake his death he had his cloned body and tissue records switched
with those of **Earl Peabody**, a Fort Lewis used-car dealer who went missing the same day
Davenport was "assassinated", and that switch will not survive an audit.

The fixer **Michelle Rampling** calls the team to **Greenwood Memorial Park**, a rundown Renton
cemetery, at night, in a fog so thick that astral perception is useless. Waiting in a crypt is her
Johnson: **Mr. Bones**, six feet of scarred Jamaican with three-foot dreadlocks, filed teeth, dead
black eyes and barely enough essence left to register on a scanner. The street remembers him as
**Dredd**, a shadowrunner who retired to the Caribbean League years ago and was thought dead; he
now does all of Broward's dirty work. The job is an extraction from the **Kethers Building** at
1366 Crescent Boulevard in Tacoma, DocWagon's fortress-like repository of every client tissue
sample, clone and corporate database in the metroplex. Two primary subjects, two secondary, two
safety deposit boxes, 72 hours, 5,000 nuyen per Table Rating each for the primaries and 1,000 more
for each secondary. The runners are told the VIPs are uncooperative and unaware; they are not told
why. The subjects are numbers: **99-312**, **99-804**, **99-603**, **99-815**, boxes **34-987** and
**89-661**.

The subjects are clones -- featureless proto-humans hanging on cables in open tanks of blue-green
syrup with serial numbers tattooed on their foreheads, grown for the instant tissue availability
that DocWagon's Platinum contract promises. 99-312 is Peabody, which is to say Davenport's own
body. 99-804 belongs to the trid actor **Ramos**, whom Broward wants as the face of Rose Croix.
99-603 is **Donald Watanabe** of Yamatetsu and 99-815 is **Gregory Rasmussen** of Ares/Knight
Errant, two contracts Broward intends to inherit. Take a Platinum client's clone and you take his
business.

The building is a 1957 Federal Reserve bank with twenty-centimetre granite walls, steel shutters and
a twin fifty-calibre turret over the door -- and a staff that is quietly selling it out from
underneath itself. A clan of **ghouls** in the sewers has a secret tunnel into the subbasement and
a standing arrangement with a maintenance technician they know only as "Tim", who trades them failed
clones for jewellery. **Norman Trasker** sells socialites 5,000-nuyen "rejuvenation baths" in the
clone growth vats and will walk paying customers straight past security. Senior programmer **Thomas
Duttman** owes the Seattle Mafia more than he can pay and has been settling it in organs. And a
six-strong **Yamatetsu** covert ops team, mostly Russians, is coming through a faulty window sensor
on an upper floor the same night, after the glowing, astrally active tissue in box **89-661** -- the
runners' own secondary objective, which they will destroy rather than surrender.

Afterwards the street knows, and DocWagon's magically active clients start pulling their contracts
in terror of ritual sorcery. Rose Croix Biomedical Solutions opens its doors with the governor in
attendance, three clinics, a new cryogenic storage facility, a subdermal implant instead of a
wristband, and a trideo action hero as its spokesman.
"""

TIMELINE = """
- **1957** -- the Kethers Building is completed as the home of the U.S. Federal Reserve Bank.
- **2015** -- Timothy Van der Loff starts work in the building as a 19-year-old janitor.
- **2020** -- President Jarman signs the resolution dissolving Washington State and recognising the
  Seattle Metroplex; the Federal Reserve leaves and the government sells the building to IngenTech,
  a small biotics corporation.
- **~2052 or earlier** -- DocWagon buys IngenTech and takes the building; it has held it as its
  secure storage centre "for over 12 years".
- **Early 2050s** -- Crash Cart's "mysterious debacle" removes DocWagon's only real competitor in
  the metroplex.
- **2046** -- Michelle Rampling arrives in Seattle from Marseilles.
- **2054** -- Van der Loff is made head of Building Maintenance and Support.
- **Years back** -- a decker called Hondo steals the updated DocWagon-era building plans out of the
  DocWagon host and leaves a same-sized joke file in their place. Nobody has opened it since.
- **Months before the adventure** -- Davenport lays the groundwork for the Walter Broward identity
  and starts the shell corporation that becomes Rose Croix.
- **About a month back** -- the DocWagon shareholders' meeting (SRM 01-01); Davenport "dies"; Earl
  Peabody is reported missing the same day; Davenport flies out by private jet.
- **A few weeks back** -- Rose Croix opens as a corporation and begins quietly hiring staff and
  buying equipment.
- **Days back** -- Broward returns from the Caribbean healed, takes his office, and tells Mr. Bones
  to put out feelers. Rose Croix's own new state-of-the-art facility comes online "tomorrow".
- **Night 0** -- the meet at Greenwood Memorial Park. 72 hours on the clock. Halloweeners arrive as
  the team leaves.
- **Nights 1-2** -- legwork: the building's history, the sewers, the staff, the rumours, the
  Yamatetsu team, Trasker's phone number, Duttman's debts, the DocWagon host.
- **The run** -- Taking the Fortress. Somewhere in it the Yamatetsu team is also inside.
- **Afterwards** -- Rampling arranges the drop and the payoff with Mr. Bones.
- **The following week** -- the KSEA piece: Rose Croix Biomedical Solutions is certified, the
  governor attends, Ramos signs as spokesman, and DocWagon's magical clients start leaving.
"""

ORGS = [
    {
        "name": "IngenTech",
        "org_type": "corporation",
        "tier": 2,
        "headquarters": "The Kethers Building, 1366 Crescent Boulevard, Tacoma (until the DocWagon buyout)",
        "summary": "The small biotics corporation that bought the old Federal Reserve building from the government in 2020 and was later swallowed by DocWagon, taking the fortress with it",
        "description": (
            "A small biotics corporation, and the reason DocWagon owns a bank. When President "
            "Jarman's resolution dissolved Washington State in 2020 and recognised the Seattle "
            "Metroplex, the U.S. Federal Reserve Bank moved out of its Tacoma building and the "
            "government sold the property; IngenTech bought it. DocWagon later bought IngenTech, "
            "and has used the fort-like structure as its secure storage centre for more than twelve "
            "years. Nothing else of the company survives in the record except its staff: Timothy "
            "Van der Loff worked his way up through the IngenTech years and the DocWagon merger to "
            "become head of building maintenance, and the institutional habits of a small biotics "
            "firm are visible in a facility that still keeps a 112-seat cafeteria, a gymnasium and "
            "an indoor gun range it no longer needs."
        ),
        "notes": (
            "Legwork: the sale and the buyout are Building History/Background (3) -- public data, "
            "library and Matrix searches, or any contact. Plot use is entirely archaeological: the "
            "only building plans anyone can still get hold of are the Federal Reserve floor plans "
            "in the government archives, because the updated DocWagon-era drawings were stolen "
            "years ago by the decker Hondo. Anything IngenTech built or altered between 2020 and "
            "the buyout is therefore undocumented, which is exactly why the ghouls' tunnel into the "
            "subbasement pump room has never been found."
        ),
        "allies": ["DocWagon"],
    },
    {
        "name": "Crash Cart",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Seattle metroplex (defunct as a local competitor)",
        "summary": "The emergency medical corporation whose 'mysterious debacle in the early fifties' left DocWagon unopposed in Seattle; owned and operated by Yamatetsu, which still hunts new medical technology",
        "description": (
            "DocWagon's last real competitor in the Seattle metroplex. Crash Cart's demise after "
            "what the campaign calls 'their mysterious debacle in the early fifties' paved the way "
            "for DocWagon to become the de facto provider of emergency care services in the sprawl, "
            "with no competition to force it to grow, develop or take risks -- the condition that "
            "made Michael Davenport's whole career impossible and his fake death inevitable. The "
            "company is owned and operated by Yamatetsu, which as a consequence is 'constantly on "
            "the lookout for new medical technologies' and will send its own covert operatives "
            "after a promising tissue sample rather than trust the job to shadowrunners."
        ),
        "notes": (
            "The name is the first thing a Shadowland poster reaches for when Rose Croix is "
            "announced -- 'What the heck is this? Another Crash Cart??' -- and the answer another "
            "poster gives is the campaign's thesis: this one is a legitimate and brilliantly funded "
            "venture, and Broward is 'the latest Damien Knight'. Plot use in this adventure is "
            "indirect but decisive: Crash Cart's parent is why a Yamatetsu covert ops team is "
            "inside the Kethers Building on the same night as the runners, hunting the glowing "
            "tissue in box 89-661. The book never says what the debacle was, which leaves an entire "
            "corporate atrocity available to a GM who wants one."
        ),
        "allies": ["Yamatetsu Corporation"],
        "enemies": ["DocWagon"],
    },
    {
        "name": "Kethers Sewer Ghoul Clan",
        "org_type": "ghoul clan",
        "tier": 1,
        "headquarters": "The sewers and drainage tunnels under 1366 Crescent Boulevard, Tacoma",
        "summary": "A small, quiet clan of ghouls living under the Kethers Building who dug a secret tunnel into its subbasement and buy failed clones from a maintenance technician with scavenged jewellery",
        "description": (
            "A small clan of ghouls that lives in the sewers and tunnels beneath the streets around "
            "the Kethers Building. They are a quiet group who prefer to be left alone and in peace, "
            "and they have made the neighbourhood quiet with them -- one of the rumours the runners "
            "can turn up is that, strangely for anywhere outside the most elite parts of the "
            "sprawl, there are no squatters or homeless anywhere near the building. The clan "
            "scavenges jewellery, watches and trinkets from what people drop and from previous "
            "feastings, and spends them on a standing arrangement with a DocWagon maintenance "
            "technician they know only as 'Tim', the name sewn on his shirt: one corpse a week, "
            "delivered to the old pump room in the subbasement. The corpses are clones that failed "
            "the forced-growth process and would have been destroyed anyway. Right now the clan is "
            "worried, because the bling has run out and they are back to dumpster diving."
        ),
        "notes": (
            "Ghoul stat block p.28: B3 Q3 S4 C1 I3 W2, Ess 5.0Z, Reaction 3, Init 3+1D6, Combat "
            "Pool 4, Karma Pool 1, Professional Rating 3; Athletics 3, Aura Reading 4, Intimidation "
            "4, Stealth 4 (Hiding 7), Unarmed Combat 5; Gang Identification 4, Gang Turf 4, Ghoul "
            "Society 4, Local Hideouts 5, Scrounge 5, Sewers 4; Mild Allergy (Sunlight), Blind, "
            "Enhanced Hearing and Smell, Sensitive System, Diet Requirements (Raw Flesh), Immunity "
            "(VITAS); serrated knife (4L, fence 10 nuyen); assorted jewellery and trinkets (500 "
            "nuyen). Their tunnel runs from the main drainage pipes to a service grate in an almost "
            "unused old pump room in the subbasement, and it is the safest way in and the fastest "
            "way out. Etiquette (Street) (7) opens negotiations; 1,000 nuyen buys an escort to the "
            "hidden entrance, and a diversion or help carrying clones and boxes costs at least "
            "1,000 nuyen per character with standard negotiation. They will not be found by "
            "searching -- a team that hunts for the door alone needs Stealth (6) or Perception (9), "
            "and the book says they cannot find it inside the time allowed. Threaten or intimidate "
            "them and the clan is simply gone the next time anyone comes down. Inside the vaults "
            "they are atmosphere first: whispers in dark corners and the reflection of milky eyes, "
            "which the staff upstairs have decided means the building is haunted."
        ),
    },
    {
        "name": "Novatech",
        "org_type": "corporation",
        "tier": 5,
        "headquarters": "Boston, UCAS",
        "summary": "The megacorporation that inherited Fuchi's North American Matrix business and now maintains DocWagon Seattle's host, including the one at the Kethers Building",
        "description": (
            "The corporation carrying the Matrix business that used to be Fuchi Industrial "
            "Electronics' North American division. DocWagon's network was bought from Fuchi "
            "originally and runs standard Matrix iconology; Novatech maintains it now. That "
            "inheritance is the whole of Novatech's presence in this adventure, but it is not "
            "nothing: the security sheaf a decker walks into at the Kethers Building is Novatech's "
            "work, and so is the fact that the host has never noticed that its building-plan file "
            "was replaced years ago with a joke of exactly the same size."
        ),
        "notes": (
            "Mentioned once, in the Glowing Grids scenario, as the current maintainer of a system "
            "'purchased originally from Fuchi's North America division'. Recorded as a row rather "
            "than a name-drop because a corporation that maintains a rival's security host is a "
            "permanent lever: Novatech technicians have legitimate access to everything the runners "
            "spent the adventure breaking into, and DocWagon's side business in secure offline "
            "storage for small corporations is exactly the sort of thing a Matrix contractor would "
            "know the contents of."
        ),
    },
]

LOCATIONS = [
    {
        "name": "Greenwood Memorial Park",
        "location_type": "cemetery / memorial park",
        "city": "Seattle",
        "district": "Renton",
        "security_level": "No Security / Barrens",
        "summary": "The rundown Renton cemetery where Rampling and Mr. Bones hire the team out of a crypt in a fog thick enough to blind astral perception; the Halloweeners hold parties here",
        "description": (
            "A rundown cemetery in the heart of Renton, dark and fogbound. Fallen tombstones, dead "
            "leaves and refuse lie between forbidding crypts and weatherworn, vaguely sinister "
            "statues; open graves make the walk back to the road a hazard in the dark. About a "
            "hundred metres in from the gate a light stands beside a leaning granite sundial with a "
            "small vault behind it, and a slim, wraith-like form waits at the edge of it. Somewhere "
            "in the distance a dog howls, or something that the runners would prefer to believe is "
            "a dog. When the meeting ends the light goes out, and motorcycles and troll doom metal "
            "come up the road."
        ),
        "notes": (
            "The Halloweeners sometimes use the place for parties, which is the reason Rampling "
            "gives for wanting the meet finished quickly, and they arrive as the team leaves. "
            "Astral: the astral here is 'thick and bright, much like a thick fog in a car's "
            "headlights', so anyone perceiving has a hard time seeing anything. The book is explicit "
            "that there is no explanation for this and none should be given -- it is a mood device, "
            "and an unexplained thing is scarier than an explained one. Run the arrivals together "
            "at the gate so strangers can introduce themselves. Rampling appears mundane and "
            "slightly unnerved by the venue and the Johnson but otherwise stable and healthy, with "
            "a moderate amount of cyberware and a visible datajack; Mr. Bones shows only the "
            "smallest traces of essence and an aura that is a swirling mass of blacks, reds and "
            "foul greens."
        ),
    },
    {
        "name": "Low's Tavern",
        "location_type": "bar",
        "city": "Seattle",
        "district": "Tacoma (two blocks from 1366 Crescent Boulevard)",
        "security_level": "Low Security",
        "summary": "The small Tacoma bar with the nearest manhole to the Kethers Building outside its door -- the runners' way down into the ghouls' sewers",
        "description": (
            "A small bar two blocks from the Kethers Building. Its only role in the adventure is "
            "the manhole in the street in front of it, which is the nearest sewer access to "
            "DocWagon's fortress and therefore the mouth of the safest route in and out of the "
            "entire scenario. Anyone going that way is climbing into a hole in the pavement outside "
            "a working bar, in view of whoever happens to be smoking on the step."
        ),
        "notes": (
            "The sewers below: pipes are a tight fit and must be travelled single file. Body 3 or "
            "smaller metahumans manage easily; anyone larger stoops and scrunches, and a troll is "
            "practically naked and folded double to get through. Large gear -- sniper rifles, "
            "polearms and the like -- simply will not fit, which the book offers as a legitimate "
            "way to limit what a team brings. The concentration of chemicals and gases is an 8M "
            "Stun attack every five minutes (every combat turn while fighting or working hard) "
            "without a respirator, chemsuit or the cyberware equivalent, and the transit takes about "
            "fifteen minutes. The sewers under the building are very old, with collapsed and "
            "abandoned branches; the ghouls have partly rebuilt them as their food route. A map of "
            "the area's sewer and drainage network comes from a public records search with Computer "
            "(Decking) (6), or a contact with Etiquette (6) at a threshold of three successes, or "
            "from the ghouls; three or more net successes on any Utility Access (6) legwork test "
            "also produces it. Optional encounter: Devil Rats, two per character."
        ),
    },
    {
        "name": "Rose Croix Cryogenic Storage Facility",
        "location_type": "corporate facility",
        "city": "Seattle",
        "district": "Downtown Seattle",
        "security_level": "Corporate High Security",
        "controlling_org": "Rose Croix",
        "summary": "The brand-new tissue and clone vault that comes online the day after the run -- built to receive exactly the 'guests' the runners are being paid to carry out of DocWagon",
        "description": (
            "Rose Croix's new state-of-the-art cryogenic storage facility, which Broward notes is "
            "'coming online tomorrow' on the night of the run. It is the destination for everything "
            "the runners take out of the Kethers Building: Peabody's clone, which will be re-filed "
            "as Broward's own, the actor's clone that buys a spokesman, and the Yamatetsu and "
            "Ares/Knight Errant executives' clones that are meant to buy two corporate contracts. "
            "Its official ribbon-cutting is a public event attended by the governor and by trideo "
            "action hero Ramos, who signs as an Ebony-level customer and the company's official "
            "spokesperson on the same day."
        ),
        "notes": (
            "Never entered in this adventure -- the runners hand their cargo to Mr. Bones at a drop "
            "site and are paid -- but it is the whole point of the run and an obvious target for a "
            "later chapter. Rose Croix service tiers run Standard, Silver, Gold, Platinum and "
            "Ebony; instead of DocWagon's bulky wristband, customers carry a subdermal implant not "
            "much larger than a grain of rice, activated on demand, tagged with the contract "
            "identification number and tied into the medical-history databases, with continuous "
            "vital-sign sensors at the higher tiers. Anyone holding a client's clone holds the "
            "client, which is precisely the leverage Broward built the building to exercise -- and "
            "precisely the vulnerability the runners have just demonstrated DocWagon has."
        ),
    },
    {
        "name": "Rose Croix Corporate Offices",
        "location_type": "corporate headquarters",
        "city": "Seattle",
        "district": "Downtown Seattle",
        "security_level": "Corporate High Security",
        "controlling_org": "Rose Croix",
        "summary": "Broward's new office overlooking downtown, where a dead man in a real leather chair briefs a cyberzombie on the destruction of his old employer",
        "description": (
            "The offices of a corporation a few weeks old, bought with embezzled DocWagon money, "
            "Davenport's personal funds and private venture capital. Broward's own room has real "
            "leather on the high-backed chair and a window over the lights of downtown Seattle; his "
            "executive assistant **Lucy Turnbull** shows visitors in and is dismissed with a curt "
            "thank you. This is where he hands Mr. Bones a printed datafile of the job -- on paper, "
            "because nothing about this operation goes into a system -- and where he does his "
            "thinking about Garrett Walsh and about who is asleep at the wheel in Tacoma tonight."
        ),
        "notes": (
            "The prologue scene only; the runners never see it. Rose Croix Biomedical Solutions has "
            "three clinics at this point -- near the centre of downtown, near Fort Lewis and near "
            "downtown Everett -- plus the new cryogenic storage facility, all with new "
            "state-of-the-art equipment. Broward's public biography makes him a graduate of Boston "
            "University and 'a recent addition to Seattle's skyline'. Lucy Turnbull looked, on the "
            "night Mr. Bones came in, like someone who had seen a ghost, which given who she works "
            "for is closer to true than she knows. For GMs: an executive assistant who has met "
            "Broward's fixer face to face is the softest target in the corporation."
        ),
    },
]

NPCS = [
    {
        "name": "Mr. Bones",
        "role": "Walter Broward's fixer, enforcer and intermediary -- the ex-shadowrunner Dredd, now barely alive enough to register on a scanner, who hires the team out of a crypt",
        "archetype": "Fixer",
        "title": "\"Mr. Bones\" -- Jeremiah Marley, formerly the shadowrunner \"Dredd\"; Broward's intermediary",
        "race": "Human",
        "gender": "Male",
        "nationality": "Caribbean League",
        "organization": "Rose Croix",
        "connection": 4,
        "description": (
            "A massive shape hulking out of a narrow crypt doorway -- the runners expect an ork or a "
            "small troll until the light finds his face: a scarred black man with three-foot "
            "dreadlocks and the scariest black pits of eyes anyone has seen, eyes that look dead, "
            "as though the soul had left the body some time ago and probably in fear. Deep, "
            "menacing voice with a heavy Caribbean League accent. 'Da t'ing you got to 'member is "
            "dat if you screw dis up, you gon' answer ta me! Dese here bwana mans, they don' know "
            "nuttin' bout ta grab... you jus' gets them and gets them safe and secure, mon.' Press "
            "him for anything he has not offered and he simply smiles, baring sharpened, pointed "
            "teeth. To his employer he is almost gentle: 'No problem, boss. Everyt'ing gonna work "
            "out all right. You be jammin' too much on dis an your heart, it come a blowin' right "
            "out o' your chest.'"
        ),
        "background": (
            "A shadowrunner called Dredd who retired to the Caribbean League a few years ago; some "
            "thought he had died, others that he had become a cyberzombie, and nobody knows the "
            "truth. He worked with Michael Davenport back when Davenport was DocWagon Seattle's "
            "COO buying deniable operations against other corporations, and he came back to the "
            "sprawl with him about a month ago, after the reconstructive surgery. He works strictly "
            "for one man now -- Walter Broward of Rose Croix -- and handles all of his dirty work. "
            "This is Michelle Rampling's first time working with him; his credentials are "
            "impeccable and his cred is right."
        ),
        "notes": (
            "No statistics are printed; he is an experienced runner who knows how to handle other "
            "runners in a negotiation, and the runners can learn nothing about him by digging "
            "because the job came through the fixer. Astral perception shows only the smallest "
            "traces of essence remaining -- a major amount of cyberware -- and an aura that is a "
            "swirling mass of blacks, reds and foul-looking greens. Knowledge: Shadowrunners (6) or "
            "Etiquette (Street) (8) identifies him as Dredd. Legwork ladder p.26 (any street "
            "contact, TN 5): 1 a new name in Seattle, though some say he has been here for years; "
            "2 he used to be Dredd, thought dead until he reappeared a month ago; 3 he is cutting "
            "the edge close to being a cyberzombie, barely enough life left to register on a "
            "scanner, 'real Darth Vader type that one'; 4 he works strictly for Walter Broward at "
            "Rose Croix and handles all his dirty work. Terms he can offer: 5,000 nuyen x TR each "
            "for all three primaries, 1,000 x TR each per secondary, up to 5,000 x TR to the team "
            "for anything else of interest reported back, 72 hours; an Etiquette (Street) or "
            "(Mercenary) (12) test with two or more successes adds 2,000 x TR each to the primary "
            "payout and nothing else will be considered; he is authorised to supply a Demolitions "
            "skillsoft and up to six kilos of Compound-IV to teams without the skills or gear, or "
            "to replace consumables (not magical supplies) up to 1,000 x TR per runner. He tells "
            "Broward he has 'a back up plan in case da first boys don' cut it right' -- the book "
            "never says what it is."
        ),
        "contact_skills": [
            "Deniable work for Rose Croix",
            "Demolitions gear and skillsofts at short notice",
            "Caribbean League shadow contacts",
        ],
    },
    {
        "name": "Lucy Turnbull",
        "role": "Walter Broward's executive assistant at Rose Croix -- the one employee who has seen Mr. Bones walk into the CEO's private office",
        "archetype": "Corporate Aide",
        "title": "Executive assistant to the Chief Executive Officer, Rose Croix",
        "race": "Human",
        "gender": "Female",
        "organization": "Rose Croix",
        "connection": 2,
        "description": (
            "Knocks softly at the CEO's door and leads Mr. Bones into the private office with the "
            "look of someone who has seen a ghost -- and perhaps she has, since the man behind the "
            "desk is legally dead and the visitor is barely alive. Broward dismisses her with a "
            "curt 'thank you' and turns his back on her to talk business."
        ),
        "background": (
            "One of the staff Rose Croix has been quietly hiring since it opened as a corporation a "
            "few weeks ago -- Broward has been recruiting 'some of the best young minds in business "
            "and medicine' with embezzled DocWagon money and venture capital. The book gives her "
            "one sentence and a surname, which in a company this new makes her one of a very small "
            "number of people with routine access to its founder."
        ),
        "notes": (
            "No statistics; a prologue appearance only. Kept as a row because she is the softest "
            "point in Broward's security and the campaign is going to need one: the CEO's own "
            "assistant has met the intermediary who hires his shadowrunners, knows the diary, and "
            "is frightened of the man in the dreadlocks. Anyone in the Rose Croix arc trying to "
            "prove Walter Broward is Michael Davenport starts with the people who watch him come "
            "and go."
        ),
        "contact_skills": ["Rose Croix executive schedules and visitors"],
    },
    {
        "name": "Rupert Agawamnapur",
        "role": "Director of Operations of the Kethers facility and a front-runner for DocWagon Seattle's vacant COO chair -- the man whose fortress is about to be robbed",
        "archetype": "Corporate Executive",
        "title": "Director of Operations, Kethers Facility; senior director, DocWagon Seattle",
        "race": "Elf",
        "gender": "Male",
        "nationality": "British",
        "organization": "DocWagon",
        "connection": 3,
        "description": (
            "Old-school British colonial stock: born in New Delhi, raised in London, educated at the "
            "finest schools available, and a night elf, which the book notes seems to have had no "
            "adverse effect whatever on his career. He heads a staff of 125 and is a fast-rising "
            "star in the halls of DocWagon. He and his head of security butt heads frequently over "
            "discipline and corporate etiquette, which tells you which of the two cares about "
            "etiquette."
        ),
        "background": (
            "A senior director of DocWagon Seattle running the corporation's most important storage "
            "site, and rumoured to be one of the front-runners for the Chief Operations Officer "
            "post -- ahead of several vice presidents. That post is vacant because Michael "
            "Davenport was assassinated at the shareholders' meeting a month ago, and DocWagon, "
            "which has a good record of promoting from within, is full of functionaries doing "
            "everything they can to catch the board's notice. A robbery at the Kethers Building is "
            "the last thing his candidacy needs."
        ),
        "notes": (
            "No statistics; he is a legwork target, not an encounter. Building Staff (8) through "
            "corporate, scientific or security contacts, or public shareholder reports, or decking "
            "DocWagon. Plot use is the aftermath: whoever robs this building destroys "
            "Agawamnapur's promotion and hands the COO chair to somebody else, which is a "
            "consequence the Rose Croix arc can spend. He is also the one man at the site with the "
            "authority to fix its personnel problem -- half the staff have side businesses running, "
            "and every route the runners take in goes through one of them. Discrepancy note: the "
            "legwork section spells the surname Agawamnapur throughout, which is the only spelling "
            "the book gives."
        ),
        "contact_skills": ["DocWagon Seattle senior management and site operations"],
    },
    {
        "name": "Dr. Kevin O'Hara",
        "role": "Head of Cryogenics and Genetics for DocWagon Seattle -- the man responsible for every tissue sample and clone the runners are about to steal or destroy",
        "archetype": "Corporate Scientist",
        "title": "Head of Cryogenics / Genetics, DocWagon Seattle",
        "race": "Human",
        "gender": "Male",
        "age": 68,
        "organization": "DocWagon",
        "connection": 3,
        "description": (
            "In his late sixties and the only person in this building whose reputation and habits "
            "the book calls above reproach -- which in a facility where the janitor sells corpses "
            "to ghouls, the medical technician sells fake rejuvenation baths and the senior "
            "programmer sells organs to the Mafia, is a distinction worth having."
        ),
        "background": (
            "The lead scientist in charge of tissue samples and cloning processes for DocWagon's "
            "Seattle branch, and with the corporation since the beginning. The forced-growth "
            "process is his, and so is the protein emulsion the clones are vat-grown in -- the same "
            "emulsion Norman Trasker sells to socialites at 5,000 nuyen a bath. Every failed clone "
            "that the ghouls eat comes off his production line and was scheduled for destruction "
            "anyway."
        ),
        "notes": (
            "No statistics; discovered through Building Staff (8) legwork. He never appears in a "
            "scene, which is a missed opportunity a GM should take: he is the one person who can "
            "look at the vault after the run and say exactly what was taken and what was faked, and "
            "the one person who could recognise that subject 99-312's tissue records do not match "
            "its DNA. A team that wants to blow the whole Rose Croix conspiracy open needs O'Hara, "
            "and Broward needs him not to look. Useful as a contact for cloning, tissue culture and "
            "cryogenic storage questions anywhere in the campaign."
        ),
        "contact_skills": ["Cloning, forced growth and cryogenic tissue storage", "DocWagon client tissue records"],
    },
    {
        "name": "Ignatius O'Malley Riordan",
        "role": "Head of Matrix Security for DocWagon Seattle -- 'Iggy', a bare-knuckle persona behind the state of the art, who sometimes pulls a shift as the Kethers building rigger himself",
        "archetype": "Decker",
        "title": "Head of Matrix Security, DocWagon Seattle (reports to the DocWagon CIO)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Irish",
        "organization": "DocWagon",
        "connection": 4,
        "description": (
            "A proud Irishman and the man in charge of everything computer-related in the DocWagon "
            "corporate structure -- if it involves the Matrix, he runs it. His persona online is a "
            "late-1800s Irish pugilist, bare knuckles up, and he is as scrappy and ready for a "
            "fight as any man alive. He is a bit behind the state of the art in both skills and "
            "cyberware and makes up for it with dogged persistence, which is a fair description of "
            "the man out of the Matrix as well."
        ),
        "background": (
            "Riordan reports directly to the DocWagon Chief Information Officer and can occasionally "
            "be found pulling a shift himself as building rigger and Matrix security on the "
            "DocWagon nodes -- which means the rigger a decker meets in the Kethers host on any "
            "given night might be the head of Matrix security for the entire Seattle operation. He "
            "inherited a network bought from Fuchi's North America division and now maintained by "
            "Novatech, and he inherited its blind spots: the DocWagon-era building plans were "
            "stolen years ago by a decker called Hondo, who left a file of exactly the same size in "
            "their place, and the periodic inventory has never caught it."
        ),
        "notes": (
            "No statistics; use the security office rigger (Drone Rigger archetype, human) if he is "
            "on shift. Found through Building Staff (8) legwork. He is the reason a decker should "
            "not assume the Kethers host is unwatched -- the book suggests running the security "
            "sheaf already partly accumulated by another, unknown decker, or starting the system on "
            "a passive alert. Plot use afterwards: Riordan is the man who audits the intrusion, "
            "which means he is the man who will eventually find Thomas Duttman's back door and "
            "Hondo's twenty-year-old joke file. Discrepancy: the book gives his full name as "
            "Ignatius O'Malley Riordan and then calls him 'Iggy Riordan' thereafter."
        ),
        "contact_skills": ["DocWagon Matrix architecture and host security", "Seattle corporate Matrix gossip"],
    },
    {
        "name": "Timothy Van der Loff",
        "role": "Head of Building Maintenance and Support at the Kethers Building -- forty-nine years in the same building, and about to retire into it collapsing",
        "archetype": "Corporate Manager",
        "title": "Head of Building Maintenance and Support, Kethers Facility",
        "race": "Human",
        "gender": "Male",
        "age": 68,
        "organization": "DocWagon",
        "connection": 2,
        "description": (
            "The book's own verdict is that it has been a long and frankly boring career. He is "
            "almost ready for retirement; his wife has already found them a nice retirement villa "
            "in Lake Havasu, with a lovely view of the Old London Bridge. He knows the pipes, the "
            "generators, the pump rooms and the maze of the subbasement better than any security "
            "plan does, because he has been walking them since before most of the guards were born."
        ),
        "background": (
            "Started in 2015 as a nineteen-year-old janitor in the Kethers Federal Reserve Building "
            "and worked his way up -- through the sale to IngenTech, through the DocWagon merger, "
            "and finally to department head in 2054. Forty-nine years in one building, across three "
            "owners and two changes of national government."
        ),
        "notes": (
            "No statistics; a Building Staff (8) legwork result. The obvious question the book "
            "leaves open: the ghouls know their supplier only as 'Tim', from the name sewn on his "
            "shirt, and the adventure names Tim Reed, one of the maintenance technicians, as the "
            "man who actually meets them -- but the head of maintenance is also a Tim, and the "
            "maintenance department is where every route into the subbasement runs. A GM who wants "
            "a twist has one prepared: a man three months from a villa in Lake Havasu is exactly "
            "the sort of employee who has been selling failed clones for years and letting a "
            "technician take the risk. As written he is simply the institutional memory of the "
            "building, and the single best source of unrecorded structural knowledge the runners "
            "could possibly get to."
        ),
        "contact_skills": ["Kethers Building infrastructure, pump rooms and subbasement layout"],
    },
    {
        "name": "Thomas Duttman",
        "role": "Senior Programmer at the Kethers facility -- gambler, BTL user, and the Seattle Mafia's inside man, who can hand the runners the building",
        "archetype": "Corporate Programmer",
        "title": "Senior Programmer, Kethers Facility (DocWagon Seattle client databases)",
        "race": "Human",
        "gender": "Male",
        "organization": "DocWagon",
        "connection": 3,
        "description": (
            "One of the lead programmers on the giant client information databases held at the "
            "Kethers facility. He is also a gambler and a BTL user, and he is a spent man who knows "
            "it -- anyone who represents the Mafia, or merely knows what he has been doing, can "
            "talk him into almost anything. He has rationalised it the way everyone in this "
            "building has: half a dozen people already have side ventures running, so one more will "
            "not hurt, and as Senior Programmer he can have the automated systems keep track of his "
            "'babies' for him."
        ),
        "background": (
            "The gambling came first and the debts followed; an Etiquette (Street) (9) test on his "
            "name brings up a string of outstanding markers to bookies and dealers, some of them "
            "Family owned. The arrangement he made to work them off is to supply the Seattle Mafia "
            "with organs and sometimes complete clones out of DocWagon's vaults. It is one of the "
            "rumours on the street: the family gets cut-rate medical supplies and bioware because "
            "they have someone under their control on the inside."
        ),
        "notes": (
            "No statistics; he is a lever, not a fight. Calling Your Bluff: connect the Mafia rumour "
            "to Duttman's debts, then call him directly or squeeze him through a Mafia contact -- "
            "the latter works but incurs a marker against the runner who owns the contact, unless "
            "the Mafia happens to owe that runner one already. Squeezed, he will open a door or "
            "window, pull guards off a post, or push a virus or special routine at the alarm "
            "systems and the security rigger; he has full administrative rights to the computers and "
            "everything they control. For a decker he can build a back door and supply the "
            "passcodes (which roll over the next day anyway), which grants full administrative "
            "access and means no Computer tests at all for the rest of the run. Fail: expose him in "
            "public -- show up at the building asking for him, or drop the hammer where anyone can "
            "hear -- and DocWagon locks his account immediately and he is worthless. Aftermath: the "
            "inquiries that follow the run find him, he is expelled from DocWagon, and he spends "
            "the next several years working in a Stuffer Shack. He is never viable as a contact."
        ),
    },
    {
        "name": "Malcolm Smith",
        "role": "Head of Security at the Kethers Building -- the black sheep who does everything his own way, and so far has got away with it",
        "archetype": "Security Chief",
        "title": "Head of Security, Kethers Facility, DocWagon Seattle",
        "race": "Human",
        "gender": "Male",
        "organization": "DocWagon",
        "connection": 3,
        "description": (
            "The black sheep of the facility. He does things his way and only his way, and so far it "
            "has worked well -- so far. He and Director Agawamnapur butt heads frequently over "
            "discipline and corporate etiquette, and the book's own judgement is that it is only a "
            "matter of time until something he does comes back to bite him."
        ),
        "background": (
            "Security at the Kethers facility is the model for all other DocWagon facilities "
            "worldwide, and the staff is the cream of the crop drawn from every other site, with "
            "pay and prestige to match. That is Smith's inheritance and his problem: sixteen "
            "hand-picked guards on four-day ten-hour shifts who have spent years guarding what "
            "amounts to a morgue, who no longer fit their armour, who will not walk the vault level "
            "because it gives them the creeps, and who can be bribed if caught alone in a corridor. "
            "The building is a fortress and its people are the crack in it."
        ),
        "notes": (
            "No statistics; use the DocWagon Security Guard block for him and his shift supervisors. "
            "Found through Building Staff (8) legwork. He commands a standing complement of sixteen "
            "with a shift supervisor (Captain), an assistant supervisor (Lieutenant), a rotated-in "
            "DocWagon-affiliated mage and a building rigger; six pairs of roving guards on standard "
            "patterns, the rigger and mage in the third-floor security office beside the armoury. "
            "The turret over the front entrance and the roof cupola nests are his. Aftermath: this "
            "is the something that comes back to bite him -- whatever the runners do, Smith is the "
            "man who loses his job over it, which makes him an embittered, extremely well-informed "
            "free agent for the rest of the arc."
        ),
        "contact_skills": ["DocWagon physical security doctrine and site procedures"],
    },
    {
        "name": "Yeardley Runs the Night",
        "role": "Head of Magical Security at the Kethers facility -- Pueblo mage, MIT&T doctorate, and the department's diplomat",
        "archetype": "Corporate Mage",
        "title": "Head of Magical Security, Kethers Facility; right hand to Malcolm Smith",
        "race": "Human",
        "gender": "Male",
        "nationality": "Pueblo",
        "organization": "DocWagon",
        "connection": 4,
        "description": (
            "A Pueblo Indian and Malcolm Smith's right hand: a mage, and the diplomat of a "
            "department run by a man who has none, so he handles most of the meetings and all of "
            "the client interaction. Where Smith does things his own way, Yeardley is the one who "
            "explains afterwards why it was the right way."
        ),
        "background": (
            "One of the first graduates of the Doctoral Metaphysics program at MIT&T, which places "
            "him among the best formally trained corporate magical security officers in the UCAS "
            "and explains why DocWagon's most important facility got him. He runs magical security "
            "for a building whose clients include the magically active -- the same clients who, "
            "after this run, pull their contracts en masse for fear of what someone can do with a "
            "stolen tissue sample and a ritual."
        ),
        "notes": (
            "No statistics printed; the on-shift security mage uses the Street Mage archetype, "
            "human, and rotates in from other assignments because mages are too rare and expensive "
            "to station permanently -- so Yeardley himself is not necessarily in the building on "
            "the night of the run. Found through Building Staff (8) legwork. Aftermath: the "
            "Shadowland thread after the adventure is explicit that DocWagon's magical clients no "
            "longer trust it to keep their tissue safe from ritual sorcery and are moving to Rose "
            "Croix in numbers. That is Yeardley's failure on paper and his warning in fact -- he is "
            "the one man at DocWagon likely to work out what the theft of a specific set of clones "
            "actually means, and a superb ally or antagonist for the rest of the arc."
        ),
        "contact_skills": ["Corporate magical security and warding", "Ritual sorcery threat assessment", "Pueblo and MIT&T magical academia"],
    },
    {
        "name": "Norman Trasker",
        "role": "Medical technician at the Kethers Building running a 5,000-nuyen fake rejuvenation racket in the clone growth vats -- and a walk-in door for anyone who can pay",
        "archetype": "Con Artist",
        "title": "Medical technician, Kethers Facility",
        "race": "Human",
        "gender": "Male",
        "organization": "DocWagon",
        "connection": 3,
        "description": (
            "A confidence man in a lab coat, making money hand over fist at 5,000 nuyen a treatment. "
            "He hands out a private extension rather than a name and answers it with a simple "
            "'hello'. Once satisfied that callers are on the up and up he arranges an evening, "
            "meets them at a side or back entrance, and walks them down to the tanks -- money in "
            "advance, on a certified credstick. Threaten to expose him and he will tell you smugly, "
            "and correctly, that you have no proof at all."
        ),
        "background": (
            "There is a subsection of the richest and vainest of Seattle's social elite that cannot "
            "abide the thought of ageing and will try any harebrained scheme to offset it. The "
            "hottest of these lately is that bathing regularly in an emulsion of various proteins "
            "strips ten years away -- which happens to be exactly the mix DocWagon uses to force "
            "vat-grow its clones and tissues. Trasker has convinced a network of highly placed and "
            "influential people that he can supply it, and he has not yet met anyone who knows the "
            "procedure has no merits whatsoever."
        ),
        "notes": (
            "No statistics. Fountain of Youth is the second-easiest way into the building: pose as "
            "corporate or social elite, pay the 5,000 nuyen, and be escorted past the guards to the "
            "vault level. Blackmail is the hard road -- with no physical evidence he is hesitant, "
            "and may double-cross the team by telling security their plans, which puts them in "
            "front of a DocWagon security response instead of a lift. His phone number reaches the "
            "runners through the corporate or social-elite rumour channel in Other "
            "Information/Rumors (5). Aftermath: a technician with a client list of the metroplex's "
            "vainest millionaires is a blackmail asset in his own right, and the day someone tells "
            "his customers what they have really been bathing in, he becomes a man who urgently "
            "needs to leave Seattle."
        ),
        "contact_skills": ["Kethers Building side entrances and vault access", "Seattle social elite who pay for miracle cures"],
    },
    {
        "name": "Phil Collingsworth",
        "role": "Seattle hotel magnate found naked in a clone growth tank in the middle of the run -- blackmail material, a payoff, or a berserk problem",
        "archetype": "Corporate Executive",
        "title": "Hotel magnate, Seattle metroplex",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "A hotel magnate with more money than judgement, who has paid Norman Trasker to let him "
            "into a corporate vault at night so he can float in a tank of clone nutrient beside a "
            "body. The runners find him mid-treatment, or dripping and naked and trying to escape "
            "after a loud encounter, which is the book's deliberate comic relief in an adventure "
            "that has otherwise been trying to frighten the table."
        ),
        "background": (
            "One of the socialites and corporate executives Trasker has recruited by passing around "
            "his private extension. Collingsworth believes the protein emulsion will take ten years "
            "off him; the book is clear that it will not, and that removing the concoction from the "
            "tanks does no good either -- something about the solution, the tanks and the "
            "arrangement makes the whole ritual 'special', and it takes at least an hour of soaking "
            "before anyone notices any difference."
        ),
        "notes": (
            "Enraged stat block p.20 (Pushing the Envelope: the nutrients and the slight electrical "
            "current through the tank make the bather aggressive and almost animal): B3(8) Q3(8)x3 "
            "S3(8) C5 I4 W4, Ess 5.5, Reaction 3(8), Init 3+1D6 (8+1D6), Combat Pool 5(8), Karma "
            "Pool 1; attack 8M Stun; Thermographic Vision, Unarmed Combat 4; berserker rage as a "
            "Shark shaman, with powers like Spirit Strength (M and M p.123). Subdued, the effects "
            "wear off and he collapses unconscious from the strain. Three ways to leave him: let "
            "him go as a harmless weirdo; force him to become a Level 1 Contact under threat of the "
            "press (more reliable with photographs); or take the money -- 2,000 nuyen x TR each, "
            "negotiable up to another 1,000 x TR each, paid tomorrow on certified credsticks or "
            "transferred to a numbered account, against the surrender of every negative, photo and "
            "video, on pain of a Reputation hit. He will carry boxes if ordered but will not, under "
            "any circumstances, help carry a clone."
        ),
        "contact_skills": ["Seattle hotel industry and high society"],
    },
    {
        "name": "Tim Reed",
        "role": "Maintenance technician at the Kethers Building who sells failed clones to the ghouls for jewellery -- the only member of staff who knows the building is not haunted",
        "archetype": "Technician",
        "title": "Maintenance technician, Kethers Facility",
        "race": "Human",
        "gender": "Male",
        "organization": "DocWagon",
        "connection": 2,
        "description": (
            "Known to the ghouls only as 'Tim', from the name sewn on his shirt. Once a week he "
            "carries a body down to the old pump room in the subbasement and comes back up with "
            "jewellery, watches and whatever else the clan has scavenged. He is the only person in "
            "the building who knows that the whispers the janitors hear in the lower levels are not "
            "ghosts, and he has every reason to let everyone go on believing they are."
        ),
        "background": (
            "The corpses are clones that failed the forced-growth process and were scheduled for "
            "destruction anyway, which is how a maintenance technician squares selling human bodies "
            "to flesh eaters with getting up in the morning. The ghouls do not know how he gets at "
            "the clones; the arrangement has run long enough that they have exhausted their supply "
            "of trinkets and gone back to dumpster diving, and the next delivery is scheduled for "
            "tomorrow."
        ),
        "notes": (
            "No statistics. Reed is the pivot of the easiest route into the building: find the "
            "ghouls, learn about 'Tim', and you have both a secret door and a man with a "
            "career-ending secret. The book never has him meet the runners, so the GM decides "
            "whether he is a lever, a witness or a casualty. NAMING: the adventure text calls the "
            "ghouls' contact 'Tim' throughout and identifies him once as 'Tim Reed, one of the "
            "maintenance technicians'; the head of the maintenance department is also a Timothy "
            "(Van der Loff), which the book never addresses. Aftermath: the inquiry after the run "
            "will look hardest at whoever had access to the subbasement, and the man who has been "
            "walking bodies down there weekly is the first name on the list."
        ),
        "contact_skills": ["Kethers subbasement access and the ghoul clan below it"],
    },
    {
        "name": "Jose",
        "role": "Ork janitor, eleven years the low man on the Kethers cleaning staff, who has to mop the clone vault alone every single night",
        "archetype": "Janitor",
        "title": "Janitorial staff, Kethers Facility",
        "race": "Ork",
        "gender": "Male",
        "organization": "DocWagon",
        "connection": 1,
        "description": (
            "The money is great, especially for an ork with no education, and the people are pretty "
            "nice -- only the occasional racist crap from a few of the guards. What he hates is the "
            "Vault, and cleaning it is the low man's job, which after eleven years is still his. "
            "The smell hits the instant the door swings: crisp, acrid ammonia and metal, and under "
            "it the barest trace of meat, like a clean cold freezer in a slaughterhouse. The chiller "
            "hum is barely audible and he feels it in his chest. He bumped a tank once while "
            "mopping; the cables hissed, an arm flopped out, the skin was cold, and he ran screaming "
            "up the stairs. He has never bumped a tank since."
        ),
        "background": (
            "Eleven years on the DocWagon janitorial staff at the Kethers Building without ever "
            "getting off the bottom of the rota. He has low-light vision and still has to squint "
            "and peer around the dim red lights of the vault to work. His is the prologue voice "
            "that tells the players what the room they are about to break into feels like."
        ),
        "notes": (
            "No statistics and no scene -- Jose exists to set the mood, and the GM should reuse "
            "every detail of his description when the runners reach the vault level. He is also the "
            "cheapest legwork source in the adventure that nobody thinks to ask: a bored, "
            "underpaid, slightly resentful janitor with eleven years of unsupervised access to "
            "every floor of DocWagon's most secure building, who has heard the whispers, knows "
            "which guards skip which patrols, and would probably talk to anyone who bought him a "
            "drink."
        ),
        "contact_skills": ["Kethers Building night routines, guard habits and which doors are really locked"],
    },
    {
        "name": "Donald Ramos",
        "role": "Seattle trideo actor whose clone is primary target 99-804 -- Broward's intended spokesman and the poster child for Rose Croix",
        "archetype": "Trideo Actor",
        "title": "Trideo actor (soap operas, latterly action roles); DocWagon Platinum client 99-804",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "A famous trid actor in the Seattle area, known for his roles in soap operas and lately "
            "as an action hero -- exactly the kind of face that makes a new corporation a household "
            "word. In the vault he is a featureless proto-human hanging from cables in a tank of "
            "blue-green syrup with the number 99-804 tattooed on its forehead, which is all the "
            "runners are ever told about him."
        ),
        "background": (
            "A Platinum-level DocWagon client, which is why a fully grown clone of him is maintained "
            "round the clock: the service is for clients in positions that involve risk, and an "
            "action star who does his own stunts qualifies. He is also a cousin of Domingo Ramos of "
            "Aztechnology. Broward's plan calls for a spokesman to make Rose Croix a household "
            "word, and identified him as the perfect one before the run was ever commissioned -- "
            "Broward has Ramos's agent scheduled for a meeting the following week."
        ),
        "notes": (
            "Primary objective #99-804; his loss to Rose Croix is worth 5,000 nuyen x TR per runner "
            "together with the other two primaries, and failing to bring him back voids every "
            "secondary bonus as well. Names are for GM reference and are never given to the "
            "players. Aftermath (player handout): the ribbon-cutting on Rose Croix's new cryogenic "
            "storage facility is attended by a trideo action hero of the same surname who signs as "
            "an Ebony-level customer and the company's official spokesperson -- 'If you want to "
            "live life, you need to know you have the best protection money can buy, but where "
            "you're more than just a customer. Rose Croix, they're like family!' DISCREPANCY: the "
            "adventure text names the target Donald Ramos and his Aztechnology cousin Domingo; the "
            "handout names the new Rose Croix spokesman Domingo. The two are swapped between text "
            "and handout and the book never reconciles them. Shadowland notices the anomaly for "
            "itself -- Rose Croix's Ebony tier is no cheaper than DocWagon's Super Platinum and he "
            "is not being paid much for the face time, which is exactly what a poster called "
            "Bitrunner points out before guessing why."
        ),
        "contact_skills": ["Seattle trideo and entertainment industry"],
    },
    {
        "name": "Domingo Ramos",
        "role": "Aztechnology's Ramos -- named in the adventure as the target actor's cousin and in the handout as the man who becomes Rose Croix's Ebony-tier spokesman",
        "archetype": "Corporate Executive",
        "title": "Aztechnology (position unspecified); cousin of the trideo actor Ramos",
        "race": "Human",
        "gender": "Male",
        "organization": "Aztechnology",
        "connection": 4,
        "description": (
            "Named once in the adventure text, as the Aztechnology connection that makes a trid "
            "actor's clone worth more than a trid actor's clone, and once in the player handout, as "
            "the action hero standing beside the governor at Rose Croix's ribbon-cutting. The book "
            "gives him no description in either place, which leaves a GM free to decide whether "
            "Aztechnology's man and the star are two people who share a surname or one person the "
            "editing lost track of."
        ),
        "background": (
            "The adventure's Legwork on the VIPs describes primary subject 99-804 as 'Donald Ramos "
            "- Trideo Actor... also a cousin of Domingo Ramos, of Aztechnology'. The screamsheet in "
            "the handouts describes the Rose Croix launch as attended by 'trideo action hero "
            "Domingo Ramos', who signs as an Ebony customer and becomes the official spokesperson. "
            "Both statements are printed; neither is corrected."
        ),
        "notes": (
            "No statistics. Recorded as his own row so the discrepancy survives in the campaign "
            "record rather than being silently reconciled -- earlier books are canon and this one "
            "contradicts itself, so both readings stay available. Whichever way a GM plays it, the "
            "Aztechnology link is the interesting half: Broward acquiring a spokesman with a cousin "
            "inside Aztechnology, at a moment when he is deliberately courting Yamatetsu and "
            "Ares/Knight Errant contracts by holding their executives' clones, is a corporation "
            "shopping for megacorporate patronage in three directions at once."
        ),
        "contact_skills": ["Aztechnology Seattle connections"],
    },
    {
        "name": "Donald Watanabe",
        "role": "Yamatetsu's Seattle Chief of Operations, secondary target 99-603 -- a contract Broward intends to inherit by holding the man's body",
        "archetype": "Corporate Executive",
        "title": "Seattle Chief of Operations, Yamatetsu Corporation; DocWagon Platinum client 99-603",
        "race": "Human",
        "gender": "Male",
        "organization": "Yamatetsu Corporation",
        "connection": 4,
        "description": (
            "One of Yamatetsu's most valued employees in Seattle, and to the runners a numbered "
            "proto-human in a tank. The book gives him no face; what it gives him is a position "
            "important enough that Broward wants his medical contract badly enough to steal his "
            "clone for it."
        ),
        "background": (
            "A Platinum-level DocWagon client whose position involves enough risk to justify a fully "
            "grown clone maintained round the clock. Broward's reasoning is stated plainly: "
            "planning ahead is key, and by taking hold of one of Yamatetsu's most valued employees "
            "in Seattle he hopes to smooth the many business dealings he intends to have with the "
            "AAA megacorporation in future. The irony the runners are never told is that a "
            "Yamatetsu covert ops team is inside the same building on the same night after "
            "something else entirely."
        ),
        "notes": (
            "Secondary objective #99-603, worth 1,000 nuyen x TR per runner -- but only if all three "
            "primaries come back too. Names are GM reference and never given to the players; the "
            "runners can identify subjects by cross-referencing serial numbers in the DocWagon "
            "system, or by recognising a face with the right skills. Aftermath hook: a Yamatetsu "
            "executive who discovers that his clone is now in a competitor's vault has been "
            "leveraged, and may respond by moving his contract, by having Rose Croix investigated, "
            "or by having the clone taken back."
        ),
        "contact_skills": ["Yamatetsu Seattle operations"],
    },
    {
        "name": "Gregory Rasmussen",
        "role": "Ares/Knight Errant's Seattle Division Chief of Operations, secondary target 99-815 -- Broward's intended doorway into military and security contracts",
        "archetype": "Corporate Executive",
        "title": "Seattle Division Chief of Operations, Ares / Knight Errant; DocWagon Platinum client 99-815",
        "race": "Human",
        "gender": "Male",
        "organization": "Knight Errant Security Services",
        "connection": 4,
        "description": (
            "The operations chief of one of the metroplex's largest security concerns, and in this "
            "adventure a tank with 99-815 tattooed on its forehead. Like the other subjects he is a "
            "Platinum client because his job carries risk, which in his case is a considerable "
            "understatement."
        ),
        "background": (
            "Broward is hoping to capitalise on military and security contracts, both for volume and "
            "for repeat business, and reasons that getting Rasmussen to switch his personal medical "
            "contract will start the ball rolling on future dealings with Ares and Knight Errant. "
            "The book files him under 'Ares/Knight Errant' without separating the two."
        ),
        "notes": (
            "Secondary objective #99-815, worth 1,000 nuyen x TR per runner, contingent on all three "
            "primaries. The danger the adventure does not spell out: of the four subjects, this is "
            "the one whose employer runs its own investigations division and its own private army. "
            "Knight Errant holds contracts across the metroplex, including Griffin Biotechnology's "
            "Everett facility, and a Knight Errant executive who learns his clone was taken has both "
            "the motive and the instruments to find out by whom. An excellent way to bring the "
            "consequences of this run back onto the team later in the arc."
        ),
        "contact_skills": ["Ares and Knight Errant Seattle security contracting"],
    },
    {
        "name": "Hondo",
        "role": "The decker who stole the Kethers Building's updated plans out of the DocWagon host years ago and left a laughing cowpoke in their place",
        "archetype": "Decker",
        "title": "Shadow decker (Shadowland handle \"Hondo\")",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "Present only as his own calling card. A decker who opens the DocWagon file that should "
            "hold the converted building's plans gets a drunken, laughing cowpoke sitting on a "
            "barrel, who looks up and says 'Howdy pardner, I wuz wondering how long it would take "
            "for someone to come a lookin' for this file!', then holds out an empty whiskey bottle "
            "and tips it upside down. A single drop falls. The image disappears. There is nothing "
            "else in the file."
        ),
        "background": (
            "Years ago Hondo stole the updated plans for the Kethers Building -- the drawings made "
            "when the old Federal Reserve was converted into a DocWagon secure facility -- and "
            "replaced them with a Matrix message file of exactly the same size, which is why "
            "DocWagon's periodic file inventory has never noticed. The file has not been accessed "
            "since the day he left it. The same handle posts on Shadowland after the Double Cross "
            "assassination, correctly calling Michael Davenport's death an elaborate ruse to cover "
            "his retirement from DocWagon."
        ),
        "notes": (
            "No statistics; he never appears. Two consequences the runners care about: the only "
            "building plans anyone can now obtain are the pre-2020 Federal Reserve floor plans from "
            "the government archives (Orange-11/16/18/17/13/18, Quick Resolution System, or a "
            "contact who can pull them), so nothing built or altered under IngenTech or DocWagon is "
            "documented anywhere -- and somebody out there has been holding a complete set of "
            "current plans to DocWagon's most secure building for years. A GM who wants a fifth "
            "route into the Kethers Building has one: find Hondo and buy them. Given his Double "
            "Cross post, he is also already interested in the Rose Croix affair, which makes him a "
            "very natural recurring contact or rival for the arc."
        ),
        "contact_skills": ["Stolen architectural and security plans", "Shadowland rumour and old datasteals"],
    },
]

ORG_UPDATES = {
    "DocWagon": {
        "notes_append": (
            "SRM 01-02 Strings Attached (about a month after the shareholders' meeting): the "
            "Kethers Building at 1366 Crescent Boulevard in Tacoma is DocWagon Seattle's primary "
            "holding area for the tissue samples and clones of every client in the metroplex, plus "
            "its main databases and corporate files, and its security is 'the model for all other "
            "DocWagon facilities worldwide' with staff drawn as the cream of the crop from every "
            "other site. Platinum-contract clients in risky positions get a fully grown clone "
            "maintained round the clock; other clients get partial clones and vials. Side business: "
            "DocWagon runs secure OFFLINE (off the Matrix) storage of other small corporations' "
            "data at the same site, and every Seattle-area DocWagon facility ships its archive "
            "units there because the climate control is so good. Named staff: Director of "
            "Operations Rupert Agawamnapur (rumoured front-runner for the COO chair Davenport "
            "vacated, ahead of several VPs), Head of Cryogenics/Genetics Dr. Kevin O'Hara, Head of "
            "Matrix Security Ignatius O'Malley 'Iggy' Riordan (reports to the DocWagon CIO; "
            "occasionally pulls a shift as building rigger himself), Head of Building Maintenance "
            "Timothy Van der Loff, Senior Programmer Thomas Duttman, Head of Security Malcolm "
            "Smith, Head of Magical Security Yeardley Runs the Night. The corporation's condition "
            "is the point of the adventure: with Crash Cart gone since the early fifties DocWagon "
            "has had no competition, has grown 'static and overconfident', and is 'a tough "
            "exterior, but a nice, gooey and soft inside'. Half the Kethers staff run private side "
            "businesses -- clones sold to ghouls, fake rejuvenation baths sold to socialites, "
            "organs sold to the Mafia -- and every route the runners take into the building goes "
            "through one of them. DocWagon Security Guard block p.28: B5 Q4 S4 C2 I3 W3, Ess 4.1, "
            "Reaction 3, Init 3+2D6, Combat Pool 3, Karma Pool 3, Professional Rating 3; Athletics "
            "3, Clubs 3, Etiquette 2 (Corporate 3), Interrogation 3, Leadership 3, Pistols 4, SMG "
            "2, Gunnery 4, Unarmed 4; Tactics 4, Corporate Law 2, Security Systems 3; Boosted "
            "Reflexes 1, headware radio Rating 3, smartlink 2, subvocal microphone; light security "
            "armour (6/4) plus helmet (+1/+2) with thermographic and low-light; Browning Max Power "
            "(9M); plastic restraints, mage mask, datapad, medkit Rating 3, passkey. They are "
            "bored, overconfident and outgrowing their armour, will fight anyone attacking the "
            "building but not a runner met alone in a corridor, can be bribed to look away, and "
            "will break and run from any display of powerful magic without magical backup. "
            "Transport: DocWagon has contracted Ferrari 'Morgan' APCs (a civilian derivative of the "
            "Appaloosa Light Scout, turret and military armour stripped, diesel in place of the jet "
            "turbine, rear compartment sealed and refrigerated) to replace its ageing fleet of GMC "
            "Bulldogs -- Handling 4/6, Speed 120, Accel 8, Body 6, Armor 3, Sig 2, Autonav 3, "
            "Sensor 2, Cargo 50, Load 1,000, Seating 2+1b, Fuel D (250 l), Econ 5 km/l, SI 2, "
            "Avail 17/20 days, 200,000 nuyen. Aftermath: the run costs DocWagon four Platinum "
            "clients' clones, an unknown number of destroyed samples, and -- worst -- the trust of "
            "the magical community, which pulls its contracts en masse for fear of ritual sorcery "
            "and takes them to Rose Croix."
        ),
        "leadership_add": [
            {"name": "Rupert Agawamnapur", "title": "Director of Operations, Kethers Facility; senior director, DocWagon Seattle", "notes": "Night elf; rumoured front-runner for the vacant COO post."},
            {"name": "Dr. Kevin O'Hara", "title": "Head of Cryogenics / Genetics, DocWagon Seattle", "notes": "With DocWagon since the beginning; reputation above reproach."},
            {"name": "Ignatius O'Malley Riordan", "title": "Head of Matrix Security, DocWagon Seattle", "notes": "Reports to the DocWagon CIO; sometimes pulls a shift as building rigger."},
            {"name": "Malcolm Smith", "title": "Head of Security, Kethers Facility", "notes": "Black sheep; clashes with Agawamnapur over discipline."},
            {"name": "Yeardley Runs the Night", "title": "Head of Magical Security, Kethers Facility", "notes": "Pueblo mage; one of the first MIT&T Doctoral Metaphysics graduates."},
        ],
        "enemies_add": ["Crash Cart"],
    },
    "Rose Croix": {
        "description_append": (
            "SRM 01-02 Strings Attached: by a month after the assassination the company is real. "
            "Michael Davenport has returned from the Caribbean healed and resurfaced as Dr. Walter "
            "Broward, a graduate of Boston University and 'a recent addition to Seattle's skyline'; "
            "he has filed the paperwork and permits, taken the CEO's chair and the chairmanship of "
            "the board, and quietly hired 'some of the best young minds in business and medicine'. "
            "The handout gives the full trading name as Rose Croix Biomedical Solutions, certified "
            "as an emergency medical response company at a launch the governor attended. Three "
            "clinics -- near the centre of downtown, near Fort Lewis and near downtown Everett -- "
            "plus a new state-of-the-art cryogenic storage facility, all with new equipment. "
            "Service tiers run Standard, Silver, Gold, Platinum and Ebony; instead of DocWagon's "
            "bulky wristband, customers carry a rice-grain subdermal implant activated on demand, "
            "tagged with the contract identification number and tied into the medical-history "
            "databases, with continuous vital-sign monitoring at the higher tiers."
        ),
        "notes_append": (
            "SRM 01-02 Strings Attached: the funding is 'what little money he had managed to "
            "embezzle from DocWagon, along with personal funds and those of private venture "
            "capitalists he'd approached', spent on medical teams, security teams and facilities in "
            "strategic areas of the sprawl. Broward's stated strategy is that DocWagon is soft from "
            "lack of competition since Crash Cart died in the early fifties, and that he will go "
            "for the soft underbelly. This adventure is the first strike: a shadowrun on DocWagon's "
            "Tacoma vault to recover the Earl Peabody clone (his own body, and the one physical "
            "link back to his death) and to steal the clones of high-profile Platinum clients so "
            "they can be persuaded to move their contracts once DocWagon can no longer honour them "
            "-- 'basically kidnapping the VIPs' business by transferring their clones'. His fixer, "
            "enforcer and intermediary is Mr. Bones, the ex-shadowrunner Dredd, who does all his "
            "dirty work and reports having a back-up plan in case the hired team fails. His "
            "executive assistant is Lucy Turnbull. Broward talks openly of crushing 'imbeciles like "
            "Garrett Walsh'. Aftermath (handout): the ribbon-cutting, a trideo action hero signed "
            "as Ebony-tier spokesman, and -- the real prize -- DocWagon's magically active clients "
            "moving en masse to Rose Croix because a stolen tissue sample is a ritual link. "
            "Shadowland's verdict: 'This Broward fellow seems to be the latest Damien Knight.'"
        ),
        "leadership_add": [
            {"name": "Mr. Bones", "title": "Intermediary and enforcer to the CEO", "notes": "The ex-shadowrunner Dredd, formerly of the Caribbean League."},
            {"name": "Lucy Turnbull", "title": "Executive assistant to the Chief Executive Officer", "notes": None},
        ],
        "enemies_add": ["Yamatetsu Corporation"],
    },
    "Yamatetsu Corporation": {
        "notes_append": (
            "SRM 01-02 Strings Attached (Seattle, 2064): Yamatetsu owns and operates Crash Cart and "
            "is therefore 'constantly on the lookout for new medical technologies'. Word of the "
            "glowing, astrally active tissue in DocWagon safety deposit box #89-661 reached its "
            "representatives in the sprawl, and rather than trust the job to shadowrunners the "
            "corporation sent its own people -- a six-member covert ops team from the Seattle "
            "division, mostly of Russian origin, five combat specialists and a mage. They found a "
            "faulty security sensor on an upper-floor window of the Kethers Building and intend to "
            "stealth down to the cryo vaults and out again in the same night the runners do. They "
            "are extremely loyal, assigned to Seattle for missions 'the company can't even afford "
            "to trust to shadowrunners', trained together closely enough to look like they are "
            "running a Battletac when they are not, and booby-trapped so that neither they nor "
            "their gear can be traced back to Yamatetsu if they fall. They will co-operate with "
            "another team wherever goals do not conflict, and on box #89-661 they will not take no "
            "for an answer -- they will destroy the box rather than let anyone else have it, "
            "although 1,000 nuyen per runner is trivial enough that they will simply buy it. "
            "Covert Ops Member block p.29: B5 Q7(8) S6(7) C5 I5 W4, Ess 1.75, Reaction 6(12), Init "
            "8+1D6 (12+3D6), Combat Pool 8, Karma Pool 3, Professional Rating 4; Athletics 6, "
            "Biotech 3, Car 5, Etiquette 3 (Corporate 5), Pistols 7, Small Unit Tactics 4, SMG 6, "
            "Stealth 6, Throwing 6, Unarmed 6; Security Procedures 5, Tactics 4, Russian 5, "
            "Japanese 3, English 3; all-alpha cybereyes (display link, flare compensation, low "
            "light), Muscle Replacement 1, Reaction Enhancers 2, Wired Reflexes 2 with trigger; "
            "black combat clothing (5/3) plus tactical vest (3/1) plus helmet (+1/+1) for 7/4; "
            "HK-227s (7M), narcojet pistol (6D Stun), flash pak, pocket secretary, medkit Rating 3. "
            "Covert Ops Mage p.29: B4 Q6(8) S3 C5 I6 W5, Ess 6.0, Reaction 6, Init 6+1D6 (6+4D6), "
            "Combat Pool 6, Spell Pool 8, Karma Pool 4, Professional Rating 4; Sorcery 8, Conjuring "
            "6; Magic 9, Initiate Grade 3 (Quickening, Anchoring, Shielding); quickened Increased "
            "Reflexes 3 and Increased Quickness 2; Manabolt 5, Powerbolt 5, Stunball 5, Improved "
            "Invisibility 6, Trid Spectacle 6, Transform 5, Shapechange 5, Chaotic World 6, Heal 6, "
            "Silence 5, Oxygenate 4; gold ring with anchored Improved Invisibility; Earth Elemental "
            "Force 5 (3 services), two Earth Elementals Force 6 (2 services each), Fire Elemental "
            "Force 4 (4 services). Also in play: Yamatetsu's Seattle Chief of Operations Donald "
            "Watanabe is DocWagon Platinum client 99-603, and his clone is one of the runners' "
            "secondary targets -- Broward wants his contract as the doorway to future dealings with "
            "the megacorporation. A Shadowland poster with Yamatetsu contacts confirms afterwards "
            "that there was more than one team of runners in the building that night."
        ),
        "allies_add": ["Crash Cart"],
    },
    "Knight Errant Security Services": {
        "notes_append": (
            "SRM 01-02 Strings Attached (Seattle, 2064): Gregory Rasmussen, Seattle Division Chief "
            "of Operations for Ares/Knight Errant, is DocWagon Platinum client 99-815, and Rose "
            "Croix hires shadowrunners to steal his clone out of the Kethers Building -- Broward "
            "hopes that moving Rasmussen's personal medical contract will start the ball rolling on "
            "military and security contracts with 'one of the metroplex's largest security "
            "concerns', for volume and repeat business. The book files Ares and Knight Errant "
            "together without distinguishing them. Of the four subjects taken, this is the one "
            "whose employer has both the investigative apparatus and the private army to find out "
            "who did it."
        ),
        "leadership_add": [
            {"name": "Gregory Rasmussen", "title": "Seattle Division Chief of Operations, Ares / Knight Errant", "notes": "DocWagon Platinum client 99-815; his clone is a Rose Croix target."},
        ],
    },
    "Seattle Mafia": {
        "notes_append": (
            "SRM 01-02 Strings Attached (Seattle, 2064): the Family has an inside man at DocWagon's "
            "Kethers Building. Word on the street through organised-crime contacts is that they get "
            "cut-rate medical supplies and some bioware because they have someone under their "
            "control there; the man is Senior Programmer Thomas Duttman, who has been paying down "
            "gambling and BTL debts to Mafia-owned bookies by supplying organs and sometimes "
            "complete clones out of the vaults. Runners with a Mafia contact can have him leaned "
            "on into opening the building for them -- but doing so incurs a marker against the "
            "runner who owns the contact, unless the Family happens to owe that runner one already."
        ),
    },
    "Halloweeners": {
        "notes_append": (
            "SRM 01-02 Strings Attached (Seattle, 2064): the Halloweeners sometimes use Greenwood "
            "Memorial Park, a rundown cemetery in the heart of Renton, for parties. The fixer "
            "Michelle Rampling picks the place for a midnight meet precisely because it is empty "
            "at that hour and wants the business finished before they show -- 'there is no need for "
            "any unnecessary distractions'. As the runners leave they hear motorcycles and troll "
            "doom metal coming up the road behind them."
        ),
    },
    "Fuchi Industrial Electronics": {
        "notes_append": (
            "SRM 01-02 Strings Attached (Seattle, 2064): DocWagon's Matrix system was purchased "
            "originally from Fuchi's North America division and uses standard Matrix iconology; it "
            "is now maintained by Novatech. The Kethers Building host a decker meets -- Orange-6, "
            "with a seventeen-step security sheaf running from a Crippler at step 003 to "
            "Cerebropathic Black IC at 059 -- is Fuchi architecture under new management."
        ),
    },
}

LOC_UPDATES = {
    "The Kethers Building": {
        "description_append": (
            "SRM 01-02 Strings Attached: the building in full. Completed in 1957 as the home of the "
            "U.S. Federal Reserve Bank and used as such until 2020, when President Jarman signed "
            "the resolution dissolving Washington State and recognising the Seattle Metroplex; the "
            "government sold it to IngenTech, a small biotics corporation later bought by DocWagon, "
            "which has used the fort-like structure as its secure storage centre for over twelve "
            "years. 130,000 square feet; a 160-vehicle enclosed parking facility adjoining the main "
            "structure and fifteen vehicle spaces inside; a cafeteria built for 112 (now reduced to "
            "24, the rest converted into storage and datacentres); a gymnasium; an indoor gun "
            "range; multiple failsafe power backups including two onsite generators. Six floors: "
            "three above ground, a basement, a vault level with seven massive vaults, and a "
            "subbasement. The building itself is a fortress -- granite walls twenty centimetres "
            "thick, and steel shutters on every door and window that close in seconds. A gun turret "
            "with twin mounted .50 calibre machine guns covers the front entrance, visible on close "
            "examination of the facade, normally slaved to the building rigger but with manual "
            "controls; more nests sit in the cupolas at the roof corners. Inside at night it is "
            "cold, thick concrete and solid marble, most offices dark, only the front lobby and the "
            "main hallways lit."
        ),
        "notes_append": (
            "SRM 01-02 Strings Attached -- the target of the run, and the site's full write-up. "
            "STAFF: 125, headed by Director of Operations Rupert Agawamnapur; about 40 technical "
            "staff (scientists, computer engineers, programmers); most work 8am-5pm with 12-20 on "
            "hand overnight. SECURITY: a complement of sixteen at all times on four-day, ten-hour "
            "shifts -- a shift supervisor (Captain), an assistant (Lieutenant), a DocWagon-"
            "affiliated mage rotated in from other assignments because mages are too rare and "
            "expensive to station, and a building rigger; the rigger (Drone Rigger archetype, "
            "human) and mage (Street Mage archetype, human) spend most of the shift in the "
            "third-floor security office and do not fraternise with the guards; six pairs of roving "
            "guards on standard patterns. FLOORS: SUBBASEMENT -- climate control for the cryo "
            "vaults, HVAC for the rest of the building, two ageing diesel generators, large battery "
            "systems for the vault and sensitive support systems, and a maze of narrow corridors "
            "through pipes and wiring harnesses; the ghouls' secret entrance is in one dark corner, "
            "and guards do not patrol here at all without a reason. VAULT LEVEL -- six side vaults "
            "plus the large central area where the clones hang from cables in suspended open tanks; "
            "the old Federal Reserve vaults and deposit boxes, retrofitted with cryogenic systems. "
            "Treat as Minimal Lighting (SR3 p.112); thermographic vision gets a kaleidoscope, "
            "because forced metabolism runs the clones hotter than a metahuman body; hoses hiss, "
            "fog rolls, equipment clicks in the quiet and footsteps echo like thunder. Perception "
            "or Biotech (5) works out the filing method; base ten minutes to find a subject, "
            "divided by successes, and each split-up group tests separately. Boxes breathe cool "
            "smoke when opened and hold tubes of fluid and quarter-sized Petri dishes; #89-661 "
            "glows faintly and is astrally active. Biotech (5) disconnects a clone without damaging "
            "the organs. Demolitions (6) identifies the power couplings and the main cryo control "
            "unit as the targets: one kilo of C-12 spread evenly around each row's coupling and the "
            "corners of the control unit. Guards are uneasy around the clones and avoid the level "
            "unless an alarm has been raised elsewhere, after which two of them sweep it every "
            "twenty minutes. BASEMENT -- electrical distribution, plumbing access, the "
            "Matrix/telecom demarcation, the internal parking bay the armoured trucks used to use "
            "(fifteen vehicles maximum; on the night of the run nine refrigerated Ferrari Morgan "
            "transports and no ambulances), the gymnasium and the internal pistol range. The "
            "busiest level at any hour: mechanics, gym staff, and off-duty guards shooting hoops or "
            "practising, unarmoured and mostly unarmed. GROUND -- marble stairs from the lobby, a "
            "reception desk staffed by security in ordinary uniform, well lit at all times; the "
            "shrunken cafeteria and the datacentres that hold DocWagon's backup databases and the "
            "paid offsite archives of small corporations; common rooms unlocked, offices on card "
            "maglocks (Rating 5), datacentres on card/keypad maglocks (Rating 5); two roving guards "
            "plus the desk. SECOND -- DocWagon Seattle's medical supply storage, rooms dark unless "
            "in use, hallways dimmed after hours; card/keypad maglocks (Rating 5) throughout, and "
            "one store of the most expensive and desirable drugs behind a palmprint reader (Rating "
            "1 + TR) that only the shift supervisor, the assistant or authorised DocWagon personnel "
            "-- not guards -- can open; two guards who take turns walking the doors while the other "
            "fetches coffee downstairs. THIRD -- offices, the security office and the armoury "
            "(card/keypad Rating 5), roof access from the inside only with a doorbell outside and "
            "the same lock, ladders up to the cupola machine-gun nests; two guards who mostly stand "
            "at the top of the stairs playing games. ROUTES IN: the ghoul tunnel from the sewers "
            "into the old pump room; Norman Trasker's paid rejuvenation-bath escort through a side "
            "or back entrance; Thomas Duttman opening a door and blinding the systems; the "
            "Yamatetsu team's faulty upper-floor window sensor; and a frontal assault, which the "
            "book says will not last long. The weak point of this facility is its personnel. "
            "LEGWORK TNs: Building History/Background (3), Utility Access (6), Security Procedures "
            "(6) (+2 to the TN for educated guesses without an insider), Building Staff (8), The "
            "VIPs (5), Other Information/Rumors (5). RUMOURS: the place is haunted -- janitors in "
            "the lower levels hear whispers and nothing is ever found (the ghouls); a man with a "
            "Russian accent has been asking the same questions the runners are (Yamatetsu); there "
            "are no squatters or homeless anywhere in the area, which is unheard of outside the "
            "elite districts (the ghouls again); an employee can arrange a rejuvenation bath that "
            "takes ten years off you (Trasker); the Family gets cut-rate supplies from someone on "
            "the inside (Duttman); and DocWagon is making money supplying blood to vampires "
            "(false). Maps: there are none for the players -- the book withholds them deliberately "
            "so the building stays an unknown, and gives the GM basic plans only."
        ),
    },
}

NPC_UPDATES = {
    "Michael Davenport": {
        "description_append": (
            "SRM 01-02 Strings Attached: as Dr. Walter Broward, a month later, caressing the real "
            "leather of the high-backed chair in his new office -- Chief Executive Officer, "
            "Chairman of the Board, 'The Big Cheese' -- and looking out over the lights of "
            "downtown Seattle wondering who is asleep at the wheel in Tacoma tonight. Energised "
            "rather than chastened by the Caribbean. His contempt is unchanged and now has a name "
            "attached: there will be 'time enough to crush imbeciles like Garrett Walsh over at "
            "DocWagon', because 'people of vision like himself could not tolerate incompetence or "
            "short sightedness'. He briefs his enforcer off a printed sheet of paper rather than a "
            "datafile, slides it across the desk, and does not check whether it is read."
        ),
        "background_append": (
            "SRM 01-02 Strings Attached: after the assassination the extraction team put Davenport "
            "on a private jet out of the metroplex; he spent about a month in the Caribbean League "
            "healing from reconstructive surgery with the mercenary Dredd, then returned and filed "
            "the paperwork and permits for Rose Croix with himself as CEO under the identity of Dr. "
            "Walter Broward, a Boston University graduate whose groundwork he had laid months "
            "earlier along with the shell corporation. Funding: money embezzled from DocWagon, his "
            "own funds, and private venture capital, most of it already spent on office space, "
            "medical equipment, trained medical personnel, security teams and facilities across the "
            "sprawl. His reading of the market is that DocWagon's record growth since the "
            "suborbital crash and the passing of the comet has left it with a shortage of medical "
            "personnel and of the security forces needed to back them up, and that a complacent "
            "giant has a soft underbelly."
        ),
        "notes_append": (
            "SRM 01-02 Strings Attached: Broward's first strike. He hires runners through Mr. Bones "
            "and Michelle Rampling to raid DocWagon's Kethers Building for two purposes at once -- "
            "to recover the Earl Peabody clone (his own body, and the only physical evidence that "
            "the corpse in the ambulance was not his) plus the matching tissue samples, and to take "
            "the clones of four high-profile Platinum clients so that once DocWagon can no longer "
            "honour their contracts he can persuade them to move to Rose Croix. Peabody's clone "
            "will simply be re-filed in Rose Croix storage as belonging to Broward. He pays 5,000 "
            "nuyen x TR per runner for the primaries and 1,000 x TR per secondary, and insists that "
            "no secondary bonus is paid unless every primary comes back. He has the actor's agent "
            "booked for a meeting the following week and Rose Croix's own cryogenic facility coming "
            "online the day after the run. The runners never meet him and never learn who employed "
            "them: only Mr. Bones connects the job to Rose Croix, and only a level-4 legwork result "
            "on Mr. Bones names Broward at all."
        ),
        "contact_skills_add": ["Rose Croix corporate strategy and client acquisition"],
    },
    "Michelle Rampling": {
        "description_append": (
            "SRM 01-02 Strings Attached: at the Greenwood Memorial Park meet she is the slim, "
            "wraith-like form at the edge of a light in the fog. Brisk and businesslike -- 'Glad "
            "you could make it. Now that everyone is here, let's get things going. The Halloweener's "
            "sometimes use this place for parties and there is no need for any unnecessary "
            "distractions.' -- and honest about the limits of what she will say: 'This looks like a "
            "very risky job and there is little room for error -- I can't tell you any more unless "
            "you agree to the job.' She reads the target numbers off a datapad with a great show of "
            "waiting to see whether anyone is taking notes. Astrally she appears mundane, healthy "
            "and slightly unnerved by both the venue and the Johnson, with a moderate amount of "
            "cyberware and a visible datajack. If the team turns the job down she thanks them for "
            "coming and apologises pointedly to Mr. Bones for wasting his time, assuring him she "
            "will be more careful in her choices in future."
        ),
        "background_append": (
            "SRM 01-02 Strings Attached: born and raised in a quiet middle-class suburb of "
            "Marseilles, in Seattle since 2046, where she has found a comfortable niche in the "
            "shadows. Her first love is music; to all outside appearances she is an unassuming "
            "piano teacher, and it is largely because she seems nothing like a successful (if low "
            "end) fixer that she remains one. A bland-looking, soft-spoken woman with an extreme "
            "aversion to violence who keeps her hand in information brokerage for her own reasons. "
            "Her contacts are mostly ordinary folk from various walks of life, though she knows some "
            "influential music personalities; she maintains a constant Matrix presence and is quite "
            "the data broker without being a decker herself, and she has many overseas friends, "
            "most of them former clients of her legal business. This is her first job for Mr. Bones "
            "-- his credentials are impeccable and his cred is right."
        ),
        "notes_append": (
            "SRM 01-02 Strings Attached: contact card p.27 -- I 4, W 5, C 4 (Body, Quickness, "
            "Strength, Essence and Reaction printed as '?'; Initiative unknown), Karma Pool 4, "
            "Professional Rating 2; Etiquette 6 (Corporate 8), Negotiation 6, Computer 4; "
            "Entertainment Industry 5 (Music 8), Fences 3 (Paydata 6), Passcodes 3, Shadowrunners "
            "4, Matrix Deckers 5, Seattle Matrix 8; a datajack; music instruction (piano), overseas "
            "contacts (Western Europe), acquiring Matrix gear (hardware and software); no relevant "
            "gear. Contact by phone, email, Matrix or at her residence; always available, though "
            "she has a real life as a piano instructor. Preferred runners: deckers and quiet types. "
            "Legwork ladder p.26 (any street contact TN 5, any corporate or Matrix contact TN 3): "
            "0 'Michelle? Sure, she's the weather girl on Channel 125, right?'; 1 a fixer working "
            "the shadows, getting some major business lately; 2 an elf, kind of homely, passionate "
            "about music, teaches classical piano to pass the time; 3 spends a lot of time on the "
            "Matrix talking to old friends somewhere in France; 4 dependable and trustworthy, "
            "normally deals in information and Matrix runs, anything non-violent, will not touch "
            "wetwork. Note that in this adventure she brokers an extraction with a standing "
            "instruction that all other subjects may be eliminated -- the edge of what she will "
            "take. She arranges the drop and the payoff with Mr. Bones afterwards, and is 'pleased "
            "that you were able to come through for her', which matters: her reputation is the "
            "collateral on this job."
        ),
        "contact_skills_add": [
            "Extraction and datasteal contracts (nothing violent)",
            "Seattle Matrix, paydata fencing and passcodes",
        ],
    },
    "Earl Peabody": {
        "notes_append": (
            "SRM 01-02 Strings Attached: Peabody 'was reported missing about a month ago -- the same "
            "day as Michael Davenport was assassinated at DocWagon's shareholders' meeting', which "
            "the book states flatly and never explains. His clone, DocWagon subject #99-312, is the "
            "adventure's first primary objective, because it is in fact Davenport's own body: the "
            "records switch that produced a matching corpse also left Davenport's real clone filed "
            "under Peabody's name in a vault DocWagon is eventually going to audit. Broward pays "
            "shadowrunners to steal it, together with the matching tissue samples in safety deposit "
            "box #34-987, and will re-file it in Rose Croix storage as his own. The runners are "
            "given the number and not the name; the book is explicit that they cannot discover "
            "whose body it really is. Anyone reconstructing the conspiracy afterwards has two "
            "threads here -- a missing car dealer and a clone that walked out of a fortress."
        ),
    },
    "Garrett Walsh": {
        "notes_append": (
            "SRM 01-02 Strings Attached: a month after eulogising him, Walsh is the man the "
            "resurrected Davenport intends to destroy by name -- 'Time enough, he thought, to crush "
            "imbeciles like Garrett Walsh over at DocWagon.' Walsh has no idea any of this is "
            "happening. His corporation is short of medical personnel and of the security to back "
            "them up after years of record growth, its most secure building is being sold out from "
            "under it by half its own staff, and this adventure ends with its magically active "
            "clients pulling their contracts for fear of ritual sorcery and taking them to a "
            "competitor that did not exist six weeks ago. He also has a Chief Operations Officer's "
            "chair to fill, with Kethers director Rupert Agawamnapur rumoured to be the "
            "front-runner ahead of several vice presidents -- a promotion the events of this "
            "adventure are about to ruin."
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
Two systems, both given in SR3 notation.

**1. The DocWagon network / the Kethers Building host** (p.21, Glowing Grids). Reachable from
outside for legwork or from a terminal inside the building to open maglocks and blind security.
Purchased originally from Fuchi's North America division, maintained now by Novatech, and running
standard Matrix iconology.

Security code: **Orange-6 10/10/13/11/10**

| Trigger step | Security event ((R) = reactive IC) |
|---|---|
| 003 | Crippler (Bod) 5 |
| 007 | Crippler (Evasion) 5 |
| 012 | Trap Probe 7 (R) / Killer 7 |
| 016 | Trap Probe 9 (R) / Killer 5 |
| 020 | Passive Alert (+2 on all subsystem ratings) |
| 020 | Trap Scout 7 (R) / Blaster 5 |
| 024 | Scout 7 |
| 029 | Trap Probe 7 (R) / Data Bomb 7 |
| 033 | Trap Scout 5 (R) / Killer 7 |
| 038 | Sparky 5 |
| 043 | Active Alert |
| 043 | Non-Lethal Black IC 7 |
| 048 | Ripper (Evasion) 7 |
| 051 | Crippler (Bod) 5 |
| 056 | Killer 7 |
| 059 | Cerebropathic Black IC 7 |
| 062 | Shutdown Started |

Paydata on the host: 60 Mp behind Deathworm 7; 90 Mp behind Data Bomb 10; 30 Mp with no defense;
70 Mp behind Data Bomb 9; 70 Mp behind Scramble IC 9.

What is in it: the client register that ties serial numbers to names (99-312 Peabody, 99-804 Ramos,
99-603 Watanabe, 99-815 Rasmussen), the maglocks and security systems of the whole building, and
the file that should hold the converted building's plans and instead holds Hondo's laughing cowpoke.
The book suggests running the sheaf already partly accumulated by another, unknown decker, or
starting the host on a passive alert, since DocWagon is a frequent target. Thomas Duttman has full
administrative rights and can hand a decker a back door and passcodes that remove the need for any
Computer test at all. Note the two duplicated trigger steps (020 and 043) as printed.

**2. The government archives** (p.12). The only source of building plans anyone can still get:
the original Federal Reserve floor plans, pre-2020, showing nothing that IngenTech or DocWagon
added.

Security code: **Orange-11/16/18/17/13/18** -- run it with the Quick Resolution System.

**Not mapped**: DocWagon's secure OFFLINE archive service in the ground-floor datacentres (deliberately
not on the Matrix -- every Seattle-area DocWagon facility ships its archive units there, and small
corporations pay a nominal fee for the same); Rose Croix's own systems; and the building rigger's
turret and drone control, which is reachable through the Kethers host rather than existing separately.
"""

NOT_BUILT = """
- **Safety deposit boxes 34-987 and 89-661** -- objectives, not places; described on the Kethers
  Building row. 89-661's glowing, astrally active tissue is explicitly a MacGuffin ("actually a
  MacGuffin", the book says) that the adventure never explains and Yamatetsu will destroy rather
  than surrender.
- **The old pump room** in the subbasement and the **ghouls' secret tunnel** -- on the Kethers
  Building and Kethers Sewer Ghoul Clan rows.
- **The Yamatetsu covert ops team** (five members and a mage) and the **DocWagon security guards,
  shift supervisor, assistant supervisor, building rigger and rotated-in security mage** -- stat
  blocks on the Yamatetsu Corporation and DocWagon rows.
- **Devil rats** (the optional sewer encounter, 2 per character) -- stat block: B2 Q5x3 S1 C5 I2/5
  W3, Ess 4Z, Reaction 5, Init 5+1D6, Combat Pool 6, Karma Pool 2, attack 4L at -1 Reach;
  Concealment (Personal), Immunity (Pathogens, Poisons); Weakness (Sunlight -- any bright light,
  flash grenade, flash pack or Nova scares the whole swarm off). A bite that rolls 11 or 12 on 2D6
  carries VITAS-3: Body (4) needing 3 successes, or 6D damage overnight with fever, chills and
  vomiting until reduced to Light, magic loss checked as normal, and no known treatment. In the
  narrow pipes, dodging is limited to Reaction in Combat Pool dice, melee with Reach over 0 takes a
  target-number penalty equal to the Reach, and all ranged attacks are point blank.
- **The Ferrari "Morgan" transport** and the **GMC Bulldogs** it replaces -- vehicle stats on the
  DocWagon row.
- **President Jarman** (who dissolved Washington State in 2020), **Damien Knight** (the comparison
  Shadowland reaches for), **MIT&T**, **Lake Havasu** and the **Old London Bridge** -- name-drops on
  the rows they belong to.
- **The DocWagon CIO**, the **shift Captain and Lieutenant**, the **mechanics**, the **gym and
  range staff**, **Ramos's agent**, the **governor** at the Rose Croix launch and the **other half
  dozen Kethers employees with side ventures** -- unnamed roles.
- The Shadowland posters on the handout -- **Nurse Maid**, **The Chromed Accountant**, **Luigi**,
  **Bitrunner**, **Yellow Rose**, **Neon Flux** and **Deacon Blues** -- board handles with no face;
  their claims are recorded on the Rose Croix, DocWagon and Yamatetsu rows. (**Hondo**, who posts
  under the same handle in the 01-01 handout, does get a row, because in this adventure he has done
  something.)
"""

PLAY_NOTES = """
- The adventure has a horror register and the book keeps saying so. Fog that blinds astral
  perception with no explanation given; a Johnson who files his teeth; a vault full of numbered
  bodies hanging on cables in glowing tanks; whispers in the dark that the staff have decided are
  ghosts. Play the unexplained straight -- the book's own note is that a thing the character and the
  player both fail to understand is more frightening than one that has a reason.
- Read Jose's prologue out loud, or steal every image in it, when the runners reach the vault level:
  the ammonia-and-cold-meat smell, the chiller hum felt in the chest, the dim red lights, the arm
  that flops out of a bumped tank.
- The Kethers Building is a fortress with a soft centre, and the centre is the payroll. Four ways in
  are written (the ghouls, Trasker's rejuvenation racket, Duttman's debts, the Yamatetsu team's
  faulty window sensor) and all four are people. Steer hard away from a frontal assault -- "if a team
  is stupid enough to have to resort to a frontal assault, they are not going to last long."
- Always Do Your Homework is the hardest scene to run because the team will split up. Have the
  legwork TNs to hand (Building History 3, Utility Access 6, Security Procedures 6, Building Staff 8,
  The VIPs 5, Rumors 5) and make sure the rumours land, because each one is a scene.
- The Black Russians dilemma is the best decision in the adventure and should be presented as one:
  cooperating with a visibly better team makes the run far easier and costs the party one 1,000
  nuyen x TR secondary. If the players do not see the trade, let them test for it or simply say so.
  Yamatetsu will pay 1,000 per runner for the box rather than fight, will destroy it rather than
  lose it, and against a team that has planned for everything else may double-cross them outright.
- The Fountain of Youth is deliberate comic relief in the middle of a horror scenario. Use it when
  the table needs to breathe. If they need a fight instead, the enraged Collingsworth block is
  there.
- Do not give the players a map. The book withholds the building plans on purpose ("having maps
  tends to ruin the mood... they no longer are facing an unknown"). The sewer map is the exception
  and is a legitimate legwork prize.
- Guards are the mood, not the obstacle: bored, overconfident, out of shape, unwilling to walk the
  vault level, bribable one-on-one, and quick to run from real magic. Have them shorten patrols and
  bang a console until the warning light goes out. "Why would anyone attack a fortress like the
  Kethers Building?? Why would anyone attack DocWagon??"
- Pushing the envelope here means near-misses rather than harder walls: let a maglock buzz and beep
  for a few moments before it opens, as though the test had failed. Keep them on a razor's edge and
  do not push them off it.
- Payment: 5,000 nuyen x TR each for the three primaries together, 1,000 x TR each per secondary,
  nothing for secondaries if a primary is missed, up to 5,000 x TR to the team for anything else of
  interest reported to Mr. Bones, and 9,000 x TR each if everything comes back. Etiquette (Street or
  Mercenary) (12) with 2+ successes adds 2,000 x TR each and no other raise will be considered. Mr.
  Bones will supply a Demolitions skillsoft and six kilos of Compound-IV, or replace consumables
  (not magical supplies) up to 1,000 x TR per runner.
- Karma: 1 for attempting and failing to bring in all three primaries, or 3 for a successful
  mission; up to 3 individual; maximum 6.
- Arc hooks to plant: the glowing sample in 89-661 that nobody explains; Hondo and the stolen
  building plans; Malcolm Smith, who is about to lose his job; Rupert Agawamnapur, whose promotion
  the runners have just destroyed; Yeardley Runs the Night, the one DocWagon officer who might work
  out what a targeted clone theft means; and Dr. Kevin O'Hara, the only man who can prove subject
  99-312 was not Earl Peabody.
"""
