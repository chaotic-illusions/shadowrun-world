# Elven Fire (FASA 7310, 1992; Tom Dowd & James Reichstadt, prologue by Michael A. Stackpole) --
# campaign order #14. Downtown / Loveland / Bellevue / Redmond / Renton / Tacoma docks, May 2053
# (intro: "The year is 2053"; both closing news handouts are the Seattle News-Intelligencer
# Update-Net of Tuesday May 20 2053, printed after "nearly a month" of violence).
# Source text: docs/Adventures/text/SR2-Elven_Fire.txt (70 pages).
#
# Editing inconsistencies in the book (recorded in the affected notes):
#  - The Bellevue club is "The Jump House" everywhere except p.24, where it is "The Jump Room".
#  - Lucinda's cast entry (p.57) reads "Lucinda Mari Adler (nee Tangier)"; the text makes clear
#    she was born Adler and uses "Tangier" as her street alias. Row name: Lucinda Mari Adler.
#  - Player Handout 4 says Wasp was killed "approximately one year ago"; the prologue has Green
#    Lucifer (his killer) in Seattle "only a few days"; Bright's orders came "four months ago".
#  - Ancients colors: "green and black" in the text, "black-blue and green" in Handout 4.
#  - Sting's cybereyes are "Fujikon" in the prologue and "Opticon" in the cast page.
#  - Hoshiro Ino is "Hoshihiro" once (p.30); the Whispering Nights are the "Whispering Might"
#    clan in Handout 7; the Witches' Circle owner is "Sam Johnson or something" in a rumor.
#  - The Karma award numbers (p.61) did not survive OCR; only the categories are known.
#  - Dumont's rifle is an "AK-98"; the yakuza soldiers' Colt Manhunter "16 (clip)"; the Meat
#    Junkie HMG rumor is explicitly misinformation (they have two LMGs).
# ASCII only (pre-commit hook).

ADVENTURE = "Elven Fire"
ORDER = 14
SOURCE = "SR2-Elven_Fire.pdf, pp. 4-69"
YEAR = "2053 (May)"

SYNOPSIS = """
Seattle is four days into an intergang war. A hoax gang called **Elven Fire** -- elves in Ancients
colors, "Elven Fire" scrawled at every scene -- has spent two and a half months hitting the Nova
Rich, a Seoulpa numbers ring, and then every big gang in the city (Meat Junkies, Tigers, Emerald
Dogs, Red Rovers, 405 Hellhounds, Halloweeners, Black Rains). The gangs hit the **Ancients** back,
other gangs declare their own mini-wars, and Lone Star chief **William Loudon** asks **Governor
Schultz** to roll the **Metroplex Guard** out of Fort Lewis in forty-eight hours. Last night a big
white-haired "elf" with one-handed SMG discipline hosed the runner wannabe **St. John** and six
yakuza at the **Witches' Circle** in Loveland; his girlfriend **Lucinda Tangier** got away.

Troll detective **Koren Thark** of Lone Star's gang division does not believe it is a gang war.
Reprimanded for saying so, he spends discretionary funds to hire the runners (20,000 each up front,
20,000 more for proof of a conspiracy) through a fixer or through **Father William Roe's** Redmond
youth shelter. His datachip holds the Witches' Circle video: one runner half-recognizes the shooter
as **Michael Dumont**, a mercenary who never came back from a run into Tir Tairngire four years ago.

The truth: **Shim Bright**, Seattle's respected consultant on elven affairs and a covert agent for
the cabal opposing the Tir High Prince, was ordered four months ago to destroy the Ancients (the
High Prince's long-time Seattle intelligence conduit) and replace them with a gang loyal to the
opposition. He invented Elven Fire, hired St. John, and was sent Dumont -- a captured runner
"re-educated" in the Tir with more cyberware than a man should carry, now schizophrenic and
hunting a "common foe" only Bright can name. St. John's first hit at **The Jump House** killed the
Nova Rich leader **Baron** and nearly killed the Ancients' second-in-command **Green Lucifer**,
who was secretly meeting him. Green Lucifer is himself **Alejandro Kylisearn**, a Tir lord exiled
for a failed coup, who assassinated the Ancients' leader **Wasp** with a sniper rifle during a
battle with the Meat Junkies and put **Sting** in charge -- and whom the High Prince planted in the
gang precisely to fight this play.

The runners chase leads through the Witches' Circle and its owner **Simon Johnson**, the yakuza
**Whispering Nights** of Loveland (oyabun **Toshihiro Ino**, the blind mage **Midori**, Tigers
warlord **Robert Ejima**) and their 48-hour stay of retribution, plastic magnate **Owen T. Adler's**
50,000-nuyen bounty on his daughter, an Ancients parley on a Tacoma dry dock that the Meat Junkies
attack in force, Bright's ambush in a Redmond tenement (the dead ganger **Half-Ace's** flat), and
Dumont's water-flooded maze in a closed Renton bottling plant. Bright, panicking, flees from his
Hunt's Point home to a helifield with Knight Errant guards and forged Salish-Shidhe papers, where
Green Lucifer recognizes him and puts a bullet in him. With Bright dead and Dumont's body as proof,
the yakuza stand down, Lone Star shifts to containment, and in a week the city is nearly normal.
Fail, and the Guard rolls; six days later Seattle is under martial law with 118 dead.
"""

TIMELINE = """
- **About ten years ago** -- Shim Bright arrives in Seattle and builds his reputation. **About four
  years ago** -- Dumont's team disappears on a run into the Tir. **A few years ago** -- Kylisearn's
  coup fails; the High Prince secretly exiles him to Wasp's custody. **Days later** -- Kylisearn kills
  Wasp and Pearl during the Meat Junkie battle on Dexter; Sting takes over; he becomes Green Lucifer.
- **Four months ago** -- Bright's orders arrive; Half-Ace argues with a snazzy elf in a Westwind and
  vanishes two days later. **Two and a half months ago** -- The Jump House firebombing; St. John goes
  to ground. **A week later** -- the Seoulpa numbers-ring decker hit. **Three weeks ago** -- Elven
  Fire starts hitting the big gangs. **Four days ago** -- open gang war; the Ancients shoot up a Meat
  Junkie truce parley.
- **Last night** -- Dumont kills St. John and six Whispering Nights at the Witches' Circle. **Day 1**
  -- the drive-by; Thark's pitch; the 48-hour clock. Handout 8 at 24 hours (Guard leaves suspended),
  Handout 9 at 36 hours (Guard ordered out) if the runners are slow. **Within 48 hours** -- the yakuza
  deadline, Interdiction, Maze Mind, the helifield.
- **Tuesday May 20, 2053** -- Seattle News-Intelligencer: "Gang Warfare Abates" (success) or "City
  Under Martial Law", sixth day (failure).
"""

ORGS = [
    {
        "name": "Elven Fire",
        "org_type": "hoax gang / covert-ops front",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "The closed Renton soft-drink bottling plant (the only place its members ever met 'Rook')",
        "summary": "Shim Bright's fictitious Ancients splinter group: Dumont plus a handful of bought Ancients, twelve hits in three months",
        "description": (
            "A name, a scrawl on a wall, and a dumb frame of an elf in green-and-black wreathed in "
            "flame. Elven Fire was invented by the Tir agent Shim Bright to discredit and destroy the "
            "Ancients: attacks on the Ancients' enemies, carried out by 'elves in Ancients colors', so "
            "that the enemies would strike back. Its real membership is Michael Dumont (the shooter), "
            "the dismissed runner St. John, and a handful of peripheral Ancients (Vandal, Tirade, two "
            "or three others) recruited through Bright's gang contacts and told the plan is to replace "
            "Sting and Green Lucifer with a new gang under 'Rook'. The Ancients, Lone Star and the "
            "street all believe it is a real splinter faction; Bright even tells Thark 'Elven Fire' was a "
            "proposed name for the Ancients when the gang formed."
        ),
        "leadership": [
            {"name": "Shim Bright", "title": "Controller ('Rook')", "notes": "Tir opposition agent; never seen by his gangers under his own name."},
            {"name": "Michael Dumont", "title": "Assassin", "notes": "Every Elven Fire hit with a body count."},
        ],
        "notes": (
            "Hit list (Thark's briefing, p.16): The Jump House firebombing (Nova Rich; killed Baron and "
            "innocents, missed Green Lucifer); the Redmond Seoulpa Ring numbers account (aimed at the "
            "Leather Devils); a 'purify the city by the searing heat of an Elven Fire' message planted in "
            "NewsNet's computer; small gangs; then Meat Junkies, Tigers, Emerald Dogs, Red Rovers, 405 "
            "Hellhounds, Halloweeners, Black Rains; St. John and six yakuza at the Witches' Circle (card: "
            "'Even those the authorities fear are not spared the heat of the Elven Fire'). Lone Star "
            "Handout 5: twelve incidents in three months, one perpetrator image on file (PH-AN-1276-AN). "
            "Ambush team in Interdiction: Vandal, Tirade and four hired elven thugs. Success news (May 20): "
            "Lone Star calls it 'a hoax aimed at breaking up the Ancients'; street rumor links it to Tir "
            "agents; the Tir embassy declines comment."
        ),
        "enemies": ["Ancients"],
    },
    {
        "name": "Whispering Nights",
        "org_type": "yakuza clan",
        "tier": 2,
        "headquarters": "A Japanese courtyard house behind a run-down cafe storefront in Loveland (Puyallup)",
        "summary": "The only yakuza clan in Loveland; lost six soldiers and face at the Witches' Circle; oyabun Toshihiro Ino",
        "description": (
            "One of the many yakuza clans in and around Seattle and the only one operating the Loveland "
            "area. Oyabun Toshihiro Ino rules from a meticulously tended rock-garden house hidden behind "
            "a Loveland cafe, with first lieutenant Willy Chen and first son Hoshiro sharing power under "
            "him, third son Mamoru as greeter, and his blind daughter Midori -- a grade-3 initiate mage "
            "of the Way of the Whispering Nights -- assensing every visitor from a bare tatami room. Uses "
            "the Tigers (loaned by the Dungeness Crabs) as street soldiers and keeps Simon Johnson's "
            "office at the Witches' Circle bugged."
        ),
        "leadership": [
            {"name": "Toshihiro Ino", "title": "Oyabun", "notes": None},
            {"name": "Willy Chen", "title": "First lieutenant (equal power with Hoshiro)", "notes": "Counsels study before retribution."},
            {"name": "Hoshiro Ino", "title": "First son", "notes": "Urges swift retribution against the Ancients."},
            {"name": "Mamoru Ino", "title": "Third son; greeter", "notes": "No say in the matter."},
            {"name": "Midori Ino", "title": "Daughter; initiate mage", "notes": "Blind; no say in the matter."},
        ],
        "notes": (
            "Meeting protocol (three tests): leave unnecessary weapons on the porch, remove shoes for "
            "slippers, an hour of tea and small talk before business. Gateway III weapon/cyber scanner in "
            "the hall lattice (Rating 6 vs weapons, 3 vs cyberware). Only three runners enter. Contact: "
            "Etiquette (Street) 4 (3 with yakuza connections or Etiquette (Yakuza)); meeting in 2D6+4 "
            "hours minus successes; guide is the teenager Tok. The clan knows St. John fell out with his "
            "former partner Mike Dumont about 2.5 months ago and could not find Dumont. Under pressure "
            "from Kim Marsau (Marsau Clan, Puyallup) and Hanzo Shotozumi (Dungeness Crabs) to restore "
            "face; convinced, the oyabun grants a 48-hour stay. Two yakuza soldiers (Boosted Reflexes 3, "
            "Ceska Black Scorpion, Colt Manhunter, FFBA 3). Every six hours 2D6 <= 5 finds Lucinda. Fail "
            "the tests and the runners are on the clan's drek list until they prove the Ancients innocent."
        ),
        "allies": ["Dungeness Crab Clan", "Marsau Clan", "The Tigers"],
        "enemies": ["Ancients", "Elven Fire"],
    },
    {
        "name": "Dungeness Crab Clan",
        "org_type": "yakuza clan",
        "tier": 3,
        "headquarters": "Seattle (the head yakuza clan of the metroplex per this book)",
        "summary": "'The yakuza who run Seattle' in Elven Fire; oyabun Hanzo Shotozumi; the Tigers are theirs",
        "description": (
            "The head Seattle yakuza clan according to Elven Fire, under oyabun Hanzo Shotozumi. The "
            "Tigers gang is tied to the Crabs and has been loaned to the Whispering Nights as soldiers. "
            "Shotozumi is not asking for a blood bath, but wants the Whispering Nights to resolve the "
            "Witches' Circle matter and restore the face lost there. Any newcomer who picked up the "
            "Ancients' pieces after a yakuza war would face the Crabs' constant harassment."
        ),
        "leadership": [
            {"name": "Hanzo Shotozumi", "title": "Oyabun", "notes": "'The big oyabun' of street rumor."},
        ],
        "notes": (
            "Relationship to the campaign's existing 'Yakuza (Watada-rengo)' row is not stated in this book; "
            "treat the Crabs as the Seattle clan the Loveland and Puyallup clans answer to and reconcile "
            "with earlier canon at the table (see the discrepancy note on the Watada-rengo row)."
        ),
        "allies": ["Whispering Nights", "The Tigers"],
    },
    {
        "name": "Marsau Clan",
        "org_type": "yakuza clan",
        "tier": 3,
        "headquarters": "Puyallup",
        "summary": "Puyallup's senior and most powerful yakuza group; oyabun Kim Marsau leans on the Whispering Nights",
        "description": "Puyallup's senior and most powerful yakuza clan. Its oyabun, Kim Marsau, is pressuring the Whispering Nights to settle the Witches' Circle killings and restore face -- without a blood bath.",
        "notes": "Off-stage in Elven Fire; a name the Whispering Nights invoke. A natural next rung if the runners keep dealing with Puyallup yakuza.",
        "leadership": [
            {"name": "Kim Marsau", "title": "Oyabun", "notes": None},
        ],
        "allies": ["Whispering Nights"],
    },
    {
        "name": "The Tigers",
        "org_type": "street gang (martial-arts; yakuza muscle)",
        "affiliation_contact_type": "Gang",
        "tier": 2,
        "headquarters": "Loveland / Puyallup (stationed near the Witches' Circle)",
        "summary": "Yakuza-tied fighting gang ('Tigers of the Neon Jungle') loaned to the Whispering Nights; warlord Robert Ejima",
        "description": (
            "A gang that fights the old-fashioned way -- staffs, shuriken and bare hands, Browning "
            "Max-Powers as a last resort -- tied to the Dungeness Crab clan and currently loaned to the "
            "Whispering Nights as soldiers. Their warlord Robert Ejima, a grade-5 adept initiate of the "
            "'Tigers of the Neon Jungle', sits at the oyabun's left hand and has volunteered to bring "
            "Sting's head in a basket. Long-time Ancients rivals ('the last time we tangled with the "
            "Tigers ... we got gnawed real good'); hit by Elven Fire three weeks ago."
        ),
        "leadership": [
            {"name": "Robert Ejima", "title": "Warlord", "notes": "Adept, Initiate grade 5."},
        ],
        "notes": (
            "Orders: find Lucinda Tangier and bring her to the Whispering Nights; failure means a hundred "
            "lashes before their master. Not a death mission -- they fall back if outmatched and kill "
            "their own wounded rather than leave them. Squad: leader (adept: B4(6) Q4 S4(6) C2 I2 W4; "
            "Armed 6, Unarmed 6, Stealth 6, Throwing 6, Firearms 6, Etiquette (Yakuza) 5; Killing Hands, "
            "Body +2, Strength +2, Reaction +1; armor vest, Max-Power explosive, 4 shuriken, staff) plus "
            "six members (B4 Q5 S3 C3 I3 W3; Unarmed 5, Armed 4). Contact table TN 5 (4 with yakuza "
            "connections): 3+ successes gets a yakuza introduction."
        ),
        "allies": ["Whispering Nights", "Dungeness Crab Clan"],
        "enemies": ["Ancients", "Elven Fire"],
    },
    {
        "name": "Meat Junkies",
        "org_type": "street gang (human / ork)",
        "affiliation_contact_type": "Gang",
        "tier": 2,
        "headquarters": "Dexter to Aurora, Harrison to Denny (by the monorail on Dexter), north of downtown",
        "summary": "The Ancients' archrivals around Denny Park: armored war-wagons, barghests, two LMGs, twenty riders on the Tacoma dock",
        "description": (
            "A large, mixed human-and-ork gang ('grunges' in rat-skin masks) holding the blocks between "
            "Dexter and Aurora from Harrison down to Denny Way, tight with the Emerald Dogs and "
            "sometime allies of the Ragers on the Tacoma docks. They fight from heavily armored trucks "
            "with loudspeakers, field barghests on leashes and ork snipers with AK-97s, and outnumber "
            "the Ancients while being outgunned by them. Their leader -- a massive ork with twin Uzis -- "
            "was shot through the arm and hip by Green Lucifer's sniper rifle in the battle that killed "
            "Wasp; the street credits Wasp's death to them. Hit by Elven Fire three weeks ago; broke a "
            "televised truce ('the Ancients greeted a truce parley with a hail of gunfire')."
        ),
        "notes": (
            "Dock attack (Ancient Words, p.25): twenty Junkies, fifteen on foot and five on Harley "
            "Scorpions, tipped off by the Ragers; two LMG teams (Gunnery 2) firing from behind heavy "
            "metal shields (-2 Quickness, +5 Ballistic / +8 Impact), belt boxes of 300. Human Junkie: B3 "
            "Q4 S3 C2 I2 W3; Firearms 3; armor vest, Beretta 101T, Mossberg CMDT or HK227. Ork Junkie: "
            "B6 Q3 S5 C2 I2 W2. Street rumor that they have HMGs is misinformation. Contact tables p.44: "
            "they will 'nuke those pointies real good, real soon' and go after every Ancients splinter, "
            "especially Elven Fire. Bob's Cartage and Freight sits in their turf."
        ),
        "allies": ["Emerald Dogs", "The Ragers"],
        "enemies": ["Ancients", "Elven Fire"],
    },
    {
        "name": "Emerald Dogs",
        "org_type": "street gang (yakuza-backed)",
        "affiliation_contact_type": "Gang",
        "tier": 2,
        "headquarters": "Seattle elven communities (yakuza interests)",
        "summary": "Yakuza-backed gang fighting the Ancients over yakuza involvement in elven communities; tight with the Meat Junkies",
        "description": "A yakuza-backed street gang whose conflict with the Ancients is over Emerald Dog / yakuza involvement in the elven communities (Lone Star Handout 4). Tight enough with the Meat Junkies that Sting feared them as a flanking threat in the Dexter battle. On Elven Fire's hit list three weeks ago.",
        "notes": "Named, never staged. Use them when the Meat Junkies need reinforcements or the yakuza need a gang that is not the Tigers.",
        "allies": ["Meat Junkies"],
        "enemies": ["Ancients"],
    },
    {
        "name": "Eastsiders",
        "org_type": "street gang (elven)",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "East side of Seattle (met the Ancients at the border on Westlake)",
        "summary": "Elven gang led by Keno and Johnny Dark that rode with the Ancients against the Meat Junkies",
        "description": "An elven gang under Keno and Johnny Dark that joined the Ancients' 'consolidation' assault on the Meat Junkies, adding roughly half again to Wasp's strength. They formed one pincer of the attack down Aurora and Dexter.",
        "notes": "From the prologue only. Reliable Ancients allies; a way to give Sting extra bodies if the dock fight goes badly.",
        "leadership": [
            {"name": "Keno", "title": "Co-leader", "notes": None},
            {"name": "Johnny Dark", "title": "Co-leader", "notes": None},
        ],
        "allies": ["Ancients"],
        "enemies": ["Meat Junkies"],
    },
    {
        "name": "Nova Rich",
        "org_type": "street gang (rich kids)",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Bellevue (The Jump House was one of their hangouts)",
        "summary": "Spoiled rich elves and humans who use mommy and daddy's clout to stay out of jail; leader Baron killed at The Jump House",
        "description": "A Bellevue gang of rich, bored elves and humans whose image Shim Bright despised enough to make them Elven Fire's training target. Their leader Mitchell 'Baron' Corbin died in The Jump House firebombing while secretly meeting Green Lucifer; the rest of the gang was not there.",
        "notes": "Leaderless since the first Elven Fire hit. Lone Star took a while to connect the bombing to them.",
        "leadership": [
            {"name": "Mitchell Corbin", "title": "Leader 'Baron' (deceased)", "notes": None},
        ],
        "enemies": ["Elven Fire"],
    },
    {
        "name": "Leather Devils",
        "org_type": "street gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Redmond",
        "summary": "Gang backing the Redmond Seoulpa numbers ring whose Matrix account Elven Fire's decker looted",
        "description": "The gang backing a Redmond Seoulpa Ring numbers operation. A week after The Jump House, a decker lifted 'spirits knows how much nuyen' from the ring's secret Matrix account and left a dumb frame of a flaming elf in Ancients colors -- a hit Lone Star reads as aimed at the Leather Devils.",
        "notes": "Named only in Thark's briefing.",
        "enemies": ["Elven Fire"],
    },
    {
        "name": "Fetid Vikings",
        "org_type": "street gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Bellevue",
        "summary": "Machine-gunned a Bellevue choir practice to kill a Leopard Hearts leader's sister -- 'they're killing families now'",
        "description": "A Bellevue gang in a blood feud with the Leopard Hearts. Hours before Thark's pitch they machine-gunned a choir practice because the younger sister of a Leopard Hearts leader was there, in retaliation for a Leopard hit on the father of one of the Vikings.",
        "notes": "Thark's example of how far the war has gone. No stats.",
        "enemies": ["Leopard Hearts"],
    },
    {
        "name": "Leopard Hearts",
        "org_type": "street gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Bellevue",
        "summary": "Bellevue gang feuding with the Fetid Vikings; hit a Viking's father, lost a leader's sister in the choir massacre",
        "description": "A Bellevue gang whose feud with the Fetid Vikings has escalated to families: a Leopard hit on a Viking's father was answered by the choir-practice massacre.",
        "notes": "Thark's briefing only.",
        "enemies": ["Fetid Vikings"],
    },
    {
        "name": "Black Rains",
        "org_type": "street gang",
        "affiliation_contact_type": "Gang",
        "tier": 2,
        "headquarters": "Seattle (not given)",
        "summary": "One of the big gangs on Elven Fire's hit list alongside the Halloweeners, Red Rovers and 405 Hellhounds",
        "description": "Listed by Thark among the big gangs Elven Fire began hitting about three weeks before the adventure. Nothing more is said.",
        "notes": "Name only.",
        "enemies": ["Elven Fire"],
    },
    {
        "name": "Gothic Phantoms",
        "org_type": "street gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Snohomish, near Shadow Lake",
        "summary": "Snohomish street gang clashing with the go-gang Blood Rumblers near Shadow Lake (KTXX Handout 1)",
        "description": "Street rivals of the Blood Rumblers go-gang in Snohomish. Their clash near Shadow Lake killed two Rumblers and three passersby on the fourth day of the war.",
        "notes": "KTXX newscast only.",
        "enemies": ["Blood Rumblers"],
    },
    {
        "name": "The Ragers",
        "org_type": "street gang (dock)",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Tacoma docks",
        "summary": "Tacoma dock gang, sometime allies of the Meat Junkies, who tipped them off to the Ancients' dry-dock parley",
        "description": "A gang of the Tacoma docks (Seattle Sourcebook p.74) and sometime allies of the Meat Junkies. They spotted the Ancients' army escorting the runners to the dry dock and sold the Junkies the location.",
        "notes": "Off-stage. A grudge waiting to happen if the runners learn who tipped the Junkies.",
        "allies": ["Meat Junkies"],
        "enemies": ["Ancients"],
    },
    {
        "name": "Silent P's",
        "org_type": "street gang (elven)",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Seattle (not given)",
        "summary": "Elven gang the Ancients have assisted on occasion (Lone Star Handout 4)",
        "description": "An elven street gang that the Ancients, who have no traditional allies, have assisted on occasion, according to Lone Star's file.",
        "notes": "Name only.",
        "allies": ["Ancients"],
    },
    {
        "name": "Adler Plastics",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "Adler Plastic Tower, Bellevue (some seventy floors)",
        "summary": "North America's number-one single-cast plastic furniture maker; Owen T. Adler's 50,000-nuyen bounty on his daughter",
        "description": (
            "North America's number one supplier of single-cast plastic furniture (cast intact in a "
            "single mold, not assembled), run from the top of the Adler Plastic Tower in Bellevue by its "
            "short, booming founder Owen T. Adler, who has no grasp of anything else. Posted a corporate "
            "finder's fee for Lucinda Mari Adler through a Mr. Johnson: 50,000 nuyen certified on Daddy's "
            "doorstep, 25,000 for her location -- and would very much like to find her before the yakuza do."
        ),
        "leadership": [
            {"name": "Owen T. Adler", "title": "Owner / CEO", "notes": None},
            {"name": "Moose", "title": "Bodyguard", "notes": "Three meters of custom silk suit."},
            {"name": "Eleanor", "title": "Executive secretary", "notes": None},
        ],
        "notes": "A comic-relief scene ('Plastic Magnate', p.32) that is also an alternative payday. Lucinda will object strenuously to either option. Lone Star's records on her were deleted by illegal system penetration (Handout 6) -- probably Adler money.",
    },
    {
        "name": "KTXX",
        "org_type": "media (local trideo station)",
        "tier": 2,
        "headquarters": "Seattle",
        "summary": "Local Seattle trideo news station; source of Player Handouts 1, 8 and 9 (the gang-war and Guard newscasts)",
        "description": "A local Seattle trideo station whose newscasts frame the adventure: the fourth day of intergang warfare and 22 more dead, Falchion's on-camera threat, Lone Star's Carol Lake, the Guard's leave suspension and finally its deployment -- after which the screen blasts to static and the station logo stays up for hours.",
        "notes": "Field crews and John Whimmer's air-quality segment. A reporter contact here hears everything a day before the street does.",
    },
    {
        "name": "NewsNet",
        "org_type": "media (news service)",
        "tier": 3,
        "headquarters": "Seattle bureau",
        "summary": "News corporation whose computer received Elven Fire's 'purify the city' message; T. A. Dowd's Seattle byline",
        "description": "A news corporation with a Seattle bureau. Just before The Jump House bombing its representatives found a message in the company computer calling for the city to be purified by the searing heat of an Elven Fire; they dismissed it as a prank until the hits started. Its Seattle wire (bylines T. A. Dowd, Walter G. Smith) runs in the Seattle News-Intelligencer Update-Net.",
        "notes": "Its system was penetrated once already; Elven Fire's decker (never identified) is a loose end.",
    },
]

LOCATIONS = [
    {
        "name": "Witches' Circle",
        "location_type": "nightclub",
        "district": "Loveland, Puyallup",
        "security_level": "Low Security",
        "summary": "Once-fading Loveland club, now the hot spot of the district because St. John and six yakuza were shot at a roped-off table",
        "description": (
            "A single large room of big tables that serve as mini-bars seating a dozen each, a small "
            "stage and dance floor, indirect lighting, minimal floor light and artificial fog that "
            "shroud the club in perpetual gloom; state-of-the-art audio, no video or light show. Owner "
            "Simon Johnson owns the whole building and redecorates with the public's tastes. Since the "
            "hit there is a neon sign, a line of tourists, an aging ork bouncer dressed like a Halloween "
            "shadowrunner (Thorton), a hostess (Shannon), and St. John's table roped off with its "
            "stains and bullet holes as a grim attraction."
        ),
        "notes": (
            "Staff give the media version of the shooting and retreat if pushed. Johnson's office is bugged "
            "by the Whispering Nights (Rating 3 wireless mic; Opposed Test vs sweep gear); if it is live, "
            "Tigers stationed nearby tail the runners out. Most staff have Lone Star PANICBUTTONs. Street "
            "rumor: 'shadowrunners won't go near the place now, but the tourist biz is up'. Map p.19."
        ),
    },
    {
        "name": "Johnson's Warehouse (Loveland)",
        "location_type": "safehouse",
        "district": "Alley behind the Witches' Circle, Loveland",
        "security_level": "Low Security",
        "summary": "Abandoned-looking warehouse fifty meters down the club's rear alley where Simon Johnson hides Lucinda Tangier",
        "description": "An abandoned-looking warehouse about fifty meters down the alley behind the Witches' Circle, also owned by Simon Johnson, with ladder access to an upper level (map p.20). Lucinda Tangier steps out of its shadows when Johnson calls her name.",
        "notes": "The Tigers try to surround it, close to hand-to-hand and grab Lucinda. Johnson will not protect her after the fight.",
    },
    {
        "name": "Whispering Nights Den",
        "location_type": "safehouse",
        "district": "Loveland, Puyallup (behind a small cafe)",
        "security_level": "Low Security",
        "controlling_org": "Whispering Nights",
        "summary": "Run-down cafe storefront that opens into a Japanese courtyard house: rock garden, tatami rooms, Gateway III scanner",
        "description": (
            "A small, bustling Loveland cafe (one older Asian waitress) with a hall of offices behind it "
            "and an impressive wooden door under a camera. Beyond: a courtyard open to the sky, a red "
            "stone path through a meticulous rock garden in full bloom, purple flowers trailing from "
            "overhead baskets, wooden steps to a porch and rice-paper doors, a row of slippers, "
            "latticework halls hiding a Gateway III weapon-and-cyberware scanner, Midori Ino's bare "
            "tatami room, and a traditional meeting room of low tables where the oyabun sits with Chen "
            "and Ejima at his left and his sons at his right. Two yakuza soldiers stand by the door."
        ),
        "notes": "Map p.28 ('The Yakuza Den'). Only three runners may enter. The tests, the Gateway rules and the clan's attitudes are on the Whispering Nights row.",
    },
    {
        "name": "Loveland (Puyallup)",
        "location_type": "gang territory",
        "district": "Loveland, Puyallup",
        "security_level": "Low Security",
        "controlling_org": "Whispering Nights",
        "summary": "Run-down Puyallup district: the Whispering Nights' turf, the Witches' Circle, Tigers on the corners",
        "description": "A run-down stretch of Puyallup where almost any street looks the same: the Whispering Nights' territory, patrolled by their loaned Tigers, home to the Witches' Circle and St. John's yakuza connections. Asking around here for the clan's base is an Etiquette (Street) 4 Test.",
        "notes": "KTXX promises 'more on the gang violence in Loveland'. Meetings with the yakuza are set 'somewhere near Loveland'.",
    },
    {
        "name": "The Jump House",
        "location_type": "nightclub",
        "district": "Bellevue",
        "security_level": "Patrolled / Commercial",
        "summary": "Bellevue hangout for local richies and the Nova Rich; firebombed by Elven Fire two and a half months ago -- the first hit",
        "description": "A Bellevue club where the local rich kids and the Nova Rich hung out. Elven Fire's first public action: St. John's firebombing, meant for a Nova Rich meeting, that killed the gang's leader Baron and some innocents and nearly killed Green Lucifer, who was meeting Baron incognito. 'Elven Fire' was scrawled on a wall nearby (Handout 2).",
        "notes": "Called 'The Jump Room' once (p.24). Everyone who knew Green Lucifer was there is dead, which is why the Ancients think the hit was an inside job.",
    },
    {
        "name": "Adler Plastic Tower",
        "location_type": "corporate headquarters",
        "district": "Bellevue",
        "security_level": "Corporate Standard",
        "controlling_org": "Adler Plastics",
        "summary": "Seventy-odd floors; Owen T. Adler's white-marble corner office, a workout machine, a smoked-acrylic desk and Moose",
        "description": "Adler Plastics' Bellevue tower: a plastic-looking receptionist who buzzes scruffy runners straight up, an elevator that pops your ears over some seventy floors, a white marble corridor, the secretary Eleanor and giant rosewood doors, and a stark white corner office with a view of a small building and Puget Sound, a multi-system workout apparatus, a huge smoked acrylic desk and three plush plastic chairs.",
        "notes": "Runners who learned Lucinda's identity at the Witches' Circle get in without help; via Legwork a Mr. Johnson sighs and sends them here. 'Well, Moose may break all the runners in half. Oh, well.'",
    },
    {
        "name": "Half-Ace's Tenement (Bargain Basement)",
        "location_type": "apartment complex",
        "district": "Bargain Basement, Redmond Barrens",
        "security_level": "No Security / Barrens",
        "summary": "Half-occupied squatter high-rise, dead elevators, apartment 17J: Bright's kill-box for the runners and Thark",
        "description": "A multi-storey tenement on a litter-strewn street, half occupied by squatters, with power but no elevators; police tape and pools of ork blood out front where Crimson Crush members were geeked four hours earlier. On the 17th floor an elven child bounces a ball, doors slam and lock, a trideo laughs, a woman cries; apartment 17J is a single room with a small trideo tuned to 'Death or Taxes' and a man wrapped in a blanket over an SMG.",
        "notes": (
            "Map p.33 ('The Ambush Tenement'). Ambushers: Vandal in 17J, four hired elven thugs in nearby "
            "flats holding families hostage (told to look natural to astral scouts -- cards, robes, "
            "blankets), Tirade across the street attacking astrally with two Force 5 elementals and a "
            "Watcher guarding his body. Goal: kill. Tenants knew Half-Ace as 'Nick'; four months ago a "
            "snazzy elf in a Westwind with a rude talking alarm argued with him, and two days later he "
            "vanished; the current tenants of his flat were rousted hours ago. If everyone dies, plant "
            "out-of-date bottle caps on a body."
        ),
    },
    {
        "name": "Renton Bottling Plant",
        "location_type": "ruins",
        "district": "Renton, near the Maple Valley mall",
        "security_level": "No Security / Barrens",
        "controlling_org": "Elven Fire",
        "summary": "Closed soft-drink plant, a two-storey maze of machinery and catwalks under pouring roof-water: Dumont's lair and 'Rook's' meeting place",
        "description": (
            "An enormous production and bottling plant closed for months: no fence, no security, every "
            "door unlocked and recently used. Inside, a maze of machinery two storeys tall cut everywhere "
            "by crosswalks and catwalks; the roof drains have failed and water pours down from the "
            "ceiling over everything; rats leap from machine to machine; the air smells of rust. No "
            "floor plan, no power, only what light seeps in. Astrally dark and dormant, the metal "
            "impeding sight -- 'something alive and waiting'. Dumont's mind is scrawled on the walls: "
            "'Have I been born yet?', 'Rook is my angel', 'Every child cries', 'Rook says kill', and "
            "chalk sketches running in the water -- a bride with her face smeared away, a man with water "
            "pouring from his eyes, and a flame-wreathed angel with Shim Bright's face drowning an infant."
        ),
        "notes": (
            "No map by design. Two booby traps (Perception 5; Reaction 4 reduces a 6M2 blast), then "
            "Dumont's assault-rifle ambush and a cat-and-mouse chase resolved by Opposed Tracking or "
            "Reaction Tests (rules p.37). The only place Vandal and Tirade ever met 'Rook'. A hired thug "
            "who has been here recognizes Dumont as 'a burly elf'. Street: a 'zombie kinda joker' seen "
            "wandering near the Maple Valley mall and going into the old soda pop factory."
        ),
    },
    {
        "name": "Maple Valley Mall",
        "location_type": "mall",
        "district": "Renton / Maple Valley",
        "security_level": "Patrolled / Commercial",
        "summary": "The mall near which Michael Dumont was seen wandering like a zombie; the old soda pop factory is close by",
        "description": "A shopping mall on the Renton / Maple Valley side of the sprawl. Well-connected street contacts shown Dumont's picture remember a zombie-like man wandering near it and going into the closed bottling plant nearby.",
        "notes": "Legwork landmark only (p.49).",
    },
    {
        "name": "Shim Bright's Residence (Hunt's Point)",
        "location_type": "residential community",
        "district": "Hunt's Point, Bellevue",
        "security_level": "Corporate High Security",
        "summary": "Small, expensive, well-kept house behind a low stone wall in a AAA neighborhood; two silent guard dogs; a 2051 Westwind left as a decoy",
        "description": "A large single-dwelling residence (Sprawl Sites p.34 plan) in the Hunt's Point section of Bellevue: low stone wall, patio, a 2051 Eurocar Westwind in the driveway, a dark shape under the patio table that turns out to be one of two trained guard dogs (B3 Q4x4 S3; Stealth 4; attack silently, 4M2; neither paranormal nor cyber). Bright relies on his bodyguards and the neighborhood's AAA rating; the house has no other security and holds no papers, chips or clues.",
        "notes": "The telecom's message light replays a video from the helifield: his aircraft is twenty minutes late for weather. Thark, if he went ahead alone, is found here beaten and shot and left for dead by Bright's goons; he may need a heal spell to talk.",
    },
    {
        "name": "Hunt's Point Helifield",
        "location_type": "transportation hub",
        "district": "Bellevue, minutes from Hunt's Point",
        "security_level": "Patrolled / Commercial",
        "summary": "Three-pad helicopter / tilt-rotor field with a fuel depot and a radar shack; Bright's stand-off with Knight Errant, two fussy officials and a Tir-registered Commuter",
        "description": "A small field of three landing points, a refueling depot and an administrative building housing a local-scale radar system, with scarce cover between it and the road. Bright waits on the tarmac by a white corporate-marked sedan and his Westwind with one Tir bodyguard, a second bodyguard with a sniper rifle in the admin building, and three freshly hired Knight Errant guards in a perimeter, while two field officials query a flight plan to Salish-Shidhe territory with no destination.",
        "notes": (
            "Map p.39. The officials have called the FAA and Lone Star (low priority) and mean to let the "
            "aircraft land but not take off. A Federated Boeing Commuter tilt-wing with Tir Tairngire "
            "registration (Pilot 3 to notice) hovers off if lead is flying and leaves after ten Combat "
            "Turns. Shoot First / Talk First branches p.40-41; Bright's hand signal marks Green Lucifer as "
            "the sniper's first target; Knight Errant's contract is defense only and they will not engage "
            "Lone Star. Reinforcements: Green Lucifer on his bike (with 'a friend's' elementals) and a "
            "Lone Star contingent."
        ),
    },
    {
        "name": "Ancients Dry Dock (Tacoma Waterfront)",
        "location_type": "gang territory",
        "district": "Tacoma waterfront, past the warehouses",
        "security_level": "No Security / Barrens",
        "controlling_org": "Ancients",
        "summary": "Empty dock and dry dock on the Tacoma waterfront where Sting, Green Lucifer, Falchion and Viper parley -- and twenty Meat Junkies attack",
        "description": "Through the gates of an empty dock past Tacoma's warehouses and storage facilities, down a slip to a dry dock where three cycles and their riders wait. Runners are led here from Highland and Terry near Lake Union by a lone Ancients rider (Viper), gathering an army of green, black and steel through the streets that then disperses to its posts, leaving a token guard on the upper level. Out on the Sound the UCAS carrier Koontz runs heavy air operations toward Fort Lewis.",
        "notes": "Large-scale map at the back of the book (DMZ map p.70). Defenders: four gangers in the dry dock, the four leaders, seven mounted Ancients including two mages above. First warning: 'MEAT JUNKIES!' from the upper level. Retreat into Puget Sound beats getting shot.",
    },
    {
        "name": "Ancients Warehouse (Prologue)",
        "location_type": "gang territory",
        "district": "Seattle (unnamed; a ride from the Meat Junkie border)",
        "security_level": "No Security / Barrens",
        "controlling_org": "Ancients",
        "summary": "Warehouse gathering hall from the prologue: billiard table for maps, an armory of Ingrams and clips, a huge descending door",
        "description": "The warehouse where Wasp gathered the Ancients before the Meat Junkie assault: bikes on the floor, a billiards table where the map is unfolded on the green felt, an armory that hands a newcomer an Ingram and 'enough clips to last well into the next century', and a huge door that descends as the pack rides out.",
        "notes": "Stackpole's prologue only; not used in the adventure proper. A ready-made Ancients hangout if the runners are invited deeper into the gang.",
    },
    {
        "name": "Elven District (Denny Park)",
        "location_type": "gang territory",
        "district": "North-northeast of Denny Park, downtown",
        "security_level": "Low Security",
        "controlling_org": "Ancients",
        "summary": "Seattle's downtown elven district and Ancients heartland, bordering Meat Junkie turf around Denny Park",
        "description": "The elven district north-northeast of Denny Park: the Ancients' home territory (Lone Star Handout 4) and the front line of their turf war with the Meat Junkies. Sting grew up here and knows it better than anyone. The KTXX truce-parley shooting happened here. Not to be confused with Tarislar, the elven district of Puyallup.",
        "notes": "Dexter, Aurora, Harrison, Republican, Thomas and Denny Way frame the prologue battle; the monorail line runs along Dexter.",
    },
    {
        "name": "Bob's Cartage and Freight",
        "location_type": "corporate facility",
        "district": "Meat Junkie turf between Dexter and Aurora",
        "security_level": "Low Security",
        "summary": "Freight company inside the disputed blocks; the yakuza 'have designs on' it, which Sting thinks explains Wasp's corporate-fed war",
        "description": "A cartage and freight yard in the blocks between Dexter and Aurora that Wasp wanted to take from the Meat Junkies. Sting: 'we know the yakuza have designs on them. Is there anything you ain't telling us?' Wasp: 'The yaks ain't in on this play.'",
        "notes": "Prologue only. A hook for who was really paying Wasp.",
    },
    {
        "name": "Father Roe's Youth Shelter (Redmond)",
        "location_type": "safehouse",
        "district": "Redmond",
        "security_level": "Low Security",
        "summary": "Lutheran street-kid shelter: curtained sleep cubicles, Father Roe's office, Whisper's room with a hidden AK-47; where Thark meets hostile runners",
        "description": "A shelter for street kids run by the Lutheran minister Father William Roe (Policlub Meeting Hall plan, Sprawl Sites p.32): a main hall subdivided into curtain-partitioned sleep cubicles, Roe's office in one corner and, opposite, the room where Whisper, the near-mute ork custodian and guardian, sleeps, works and keeps an antique AK-47. 2D6 street kids at any time, most harmless, some with attitude.",
        "notes": "Used when the runners are on bad terms with Lone Star: the street kid Wiser fetches them, Roe pleads for the kids, and Koren Thark steps out of Whisper's room. Recognizing Thark: Etiquette (Law Enforcement) 3 / (Street) 5 / others 8.",
    },
    {
        "name": "The House (Tir Tairngire)",
        "location_type": "military installation",
        "city": "Tir Tairngire",
        "district": "Location unknown; a related military installation lies near the CFS border",
        "security_level": "Zero Zone -- Lethal Response",
        "controlling_org": "Tir Tairngire",
        "summary": "Rumored Tir military-intelligence think-tank and interrogation camp that 're-educates' captured foreign agents; where Michael Dumont was remade",
        "description": "'One of those places people in the biz don't like to talk about': a Tir Tairngire camp holding 'agents of foreign powers' who infiltrated the country, a think-tank for military intelligence doing high-level, intense interrogation and limited 're-education' with magic. Most who go through it eventually lose their minds. Dumont was seen there a year ago before being transferred to a military installation near the CFS border.",
        "notes": "Legwork TN 8 (Tir or intelligence contacts). Shim Bright assures Thark no such facility could exist in the Tir's political climate. Details deliberately vague; expand at will.",
    },
    {
        "name": "Siegmund's",
        "location_type": "nightclub",
        "district": "Downtown",
        "security_level": "Patrolled / Commercial",
        "summary": "Downtown nightclub packing them in with Peggy's Playful Porkers -- a return of animal acts? (May 20 news)",
        "description": "A downtown nightclub that, in May 2053, is packing them in with the animal act Peggy's Playful Porkers.",
        "notes": "Entertainment filler from the closing news handout.",
    },
    {
        "name": "Frank's Fish World",
        "location_type": "shop",
        "district": "Western Ave, downtown",
        "security_level": "Patrolled / Commercial",
        "summary": "Western Avenue fish shop displaying the 1.63-meter Puget Sound geoduck (May 20 news)",
        "description": "A fish shop on Western Ave where boaters Roger Browning and Wendy Tancredi have put a motorbike-sized geoduck (1.63 m shell, 0.33 m neck) on display while Seattle University's Dr. Carmela Cuomo insists it is abnormal but not paranormal.",
        "notes": "Color from the closing news handout. Tancredi wants the shell to go to Evergreen College, whose mascot is the geoduck.",
    },
]

NPCS = [
    {
        "name": "Koren Thark",
        "role": "Troll Lone Star gang-division detective who breaks every rule to hire the runners and stop the Guard rolling out",
        "archetype": "Police Detective",
        "title": "Detective, Street Affairs Division (Metahuman Gangs), Lone Star Security",
        "race": "Troll",
        "gender": "Male",
        "organization": "Lone Star Security",
        "connection": 4,
        "description": (
            "Average height and build for a troll, with an uncharacteristic graying and receding "
            "hairline, bright blue eyes and an expressive face. Simple, direct and impassioned; comes to "
            "meets in plainclothes and lightly armed, leaving the Mossberg CMDT at home, and makes no "
            "attempt to hide who he is. 'I will lose my job if Lone Star finds out I'm doing this.'"
        ),
        "background": (
            "Born human, goblinized with much of mankind in 2021 and so has a normal human lifespan. A "
            "good cop, usually, and bothered when he is not; pleased with the progress in racial justice "
            "since the Night of Rage and optimistic about the next decade. Reprimanded publicly and "
            "privately for telling his superiors the gang war is being pushed by someone; frightened and "
            "embittered by Lone Star's answer of head-on war. Has worked with Shim Bright for years and "
            "trusts him completely -- the revelation shatters him."
        ),
        "notes": (
            "Offer: 20,000 each up front plus injury expenses, 20,000 more for evidence of a conspiracy "
            "(Opposed Negotiation vs Willpower, +5 percent; can 'lose' one warrant per net success). "
            "Datachip, wristphone, Downtown LTG mailbox; reports every six hours or he comes looking after "
            "twelve; pulls Lone Star records in 1D6 hours (Handouts 4-7). Relays Bright's misinformation "
            "in good faith. Found near dead at Bright's house if he goes ahead alone; will go after Bright "
            "himself if the runners do not. Stats: B6(8) Q3 S6 C3 I4 W3, Ess 5, Init 3+2D6; Firearms 7, "
            "Police Procedures 4, Armed 3, Car 3, Etiquette (Street) 3; Boosted Reflexes 1, smartlink; "
            "Colt Manhunter (Firepower), lined coat, portable phone."
        ),
        "contact_skills": ["Lone Star gang-division records and warrants", "Authority on Lone Star and police matters", "Discretionary funds (once)"],
    },
    {
        "name": "Shim Bright",
        "role": "Seattle's respected consultant on elven affairs -- a covert Tir agent for the High Prince's enemies, secret initiate mage, author of Elven Fire",
        "archetype": "Spy",
        "title": "Independent Counsel on Elven Affairs to Lone Star and the Governor's Office; Tir opposition field agent ('Rook')",
        "race": "Elf",
        "gender": "Male",
        "nationality": "Tir Tairngire",
        "organization": "Elven Fire",
        "connection": 4,
        "description": (
            "More than two meters tall and built lean, thick dark hair in a fashionable short cut, never "
            "caught in yesterday's fashions; slick, practiced, his words always the ones his listeners "
            "want to hear. Arrogant on the news show 'Chet Chit-Chat', explaining why people do things on "
            "streets he has never walked. Drives a 2051 Eurocar Westwind with a rude, talking alarm. Has "
            "never let anyone in Seattle know he is a mage."
        ),
        "background": (
            "'Shim Bright' is not his real name. He arrived a decade ago, used his Tir masters' "
            "connections and the elven underworld to set up as a sociopolitical analyst, and within a few "
            "years Lone Star (Metahuman Affairs) and the City were consulting him on elven and Tir "
            "matters; expected to enter politics one day. Ostensibly an agent of the Tir's intelligence "
            "arm, loyal in fact to the cabal opposing the High Prince. Four months ago it ordered him to "
            "destroy the Ancients and replace them; an excellent intelligence-gatherer, he is nearly "
            "incompetent at running agents, failed to identify Green Lucifer, tampered with Dumont's "
            "programming, killed Half-Ace while pumping him, and watched the plan spiral into a city-wide "
            "war. Now hopes only to delay the Guard until the yakuza or the gangs finish the Ancients."
        ),
        "notes": (
            "Feeds Thark misinformation (no Tir backing, 'Elven Fire' an Ancients in-joke, no re-education "
            "facility, St. John a boaster); panics and orders hits when the runners meet the Ancients; flees "
            "to the helifield with forged Salish-Shidhe diplomatic papers, two Tir bodyguards and three "
            "Knight Errant guards. Recognizes Kylisearn at the end ('The High Prince said you were dead ... "
            "who better to guard the sheep from the wolves than another wolf?') and dies to Green Lucifer's "
            "gun. Stats: B2 Q4 S2 C4 I5 W6, Magic 8, Ess 6, Reaction 4(7); Initiate grade 3 (Sect of the "
            "Blooded Moon); Sorcery 7, Armed Combat 7, Conjuring 6, Negotiation 6, Stealth 5, Etiquette "
            "(Street 5 / Tir Politics 5 / Corporate 4 / Seattle Politics 4), Covert Operations 4, "
            "Sperethiel 5. Spells: Mana Dart 10, Ram 8, Stun Cloud 8, Anti-Spell Barrier 8, Fireball 7, "
            "Physical Mask 7, Combat Sense 7, Detect Enemies 6, Invisibility 6, Armor 6. Power Focus 2, "
            "Weapon Focus 3 (katana), Fichetti Security 500 and MP-5 TX with APDS, armor jacket, DocWagon "
            "Platinum, Westwind. If he escapes he will be seen again; if he dies, someone like him rises."
        ),
        "contact_skills": ["Lone Star and City Hall access on elven affairs", "Tir Tairngire opposition intelligence", "Seattle elven underworld"],
    },
    {
        "name": "Michael Dumont",
        "role": "Once the best mercenary a runner knew; captured and 're-educated' in the Tir, over-chromed into schizophrenia, Elven Fire's assassin",
        "archetype": "Mercenary",
        "title": "Elven Fire assassin (the Witches' Circle shooter); former corporate / national mercenary",
        "race": "Human",
        "gender": "Male",
        "organization": "Elven Fire",
        "connection": 2,
        "description": (
            "Large, built like a football player, short white hair on the Witches' Circle video (dark in "
            "the cast page), a square face, deep green eyes and cosmetically altered elven features that "
            "fool a camera about eighty percent of the time. Holds an SMG rock-steady one-handed, ejects "
            "clips by cybernetic command and catches them falling. Lucinda: 'Cold, like someone dead. "
            "There was only death in his eyes.' Play him as Michael Biehn's depth-crazed SEAL in The "
            "Abyss: the driven instincts of a hunting animal and the cunning of a man gone mad."
        ),
        "background": (
            "Signed for whichever corp or nation paid most and was first pick for every special team -- "
            "resourceful, stable, a hell of a shot; that is the man one runner remembers from a jungle "
            "ambush about four years ago. Then a simple border-hop snatch-and-grab into the Tir went "
            "sour and none of the team came back. What happened there no one will ever know (mind probes "
            "cannot reach it); a rumor a year ago placed him in the Tir camp called The House, then a "
            "military installation near the CFS border. He returned with more cyberware than a man was "
            "meant to carry and a conditioning that says mankind has a common foe only 'Rook' can name. "
            "Bright's meddling with his programming and the stress of the streets finished him. He has "
            "secretly stopped taking Bright's medication -- the foe's obvious avenue of attack."
        ),
        "notes": (
            "Not at the tenement ambush; found in the Renton bottling plant behind two booby traps, "
            "opening up with the AK-98 then vanishing into the maze (chase rules p.37). Babbles Rook's "
            "plan, the High Prince's orders, Tir nobility and 'Nerps -- California Style!'; reveals that "
            "Bright serves the High Prince's opposition. Claiming to represent the High Prince confuses him "
            "(+2 TN); the runner who knew him can talk him down with three failed Willpower (5) Tests into "
            "'the mind of a small, lost boy'. Carries a datafax picture of Bright marked 'Rook'. Months "
            "from catatonia, years from death. Stats: B6 Q6(8) S6(8) C1 I5 W5, Ess 0.3, Reaction 5(11), "
            "Init 11+4D6; Firearms 10, Armed 9, Unarmed 9, Gunnery 7, Car 5, Stealth 5, Throwing 5, "
            "Etiquette (Corporate) 5, Rotor Craft 2; Wired Reflexes 3, Muscle Replacement 2, improved "
            "retractable razors, smartlink, full cyberears and cybereyes (thermo, low-light, rangefinder), "
            "Commlink X, Scramble Breaker; AK-98 with grenade launcher (APDS, IPE mini-grenades), Ares "
            "Predator II (APDS), tres chic armored jacket, knives, flash and smoke grenades. His body or "
            "his testimony ends the yakuza clock."
        ),
    },
    {
        "name": "Sting",
        "role": "Copper-haired street-born elf samurai who leads the Ancients since Wasp; suspicious of corps, the Tir and her own second",
        "archetype": "Gang Boss",
        "title": "Leader of the Ancients",
        "race": "Elf",
        "gender": "Female",
        "organization": "Ancients",
        "connection": 4,
        "description": (
            "Slightly above average height, the light build of her kind, long loose copper hair she "
            "braids when the going looks tough, the yellow flash of Opticon (Fujikon in the prologue) "
            "cybereyes, long canine implants, and a ragged scar from her left eye to her pointed ear from "
            "the Tigers fight. Dominant, aggressive, uses her image as a weapon; a whipcord samurai who "
            "picks her shots and once cut a barghest in half with her hand razors. 'Are they paying us by "
            "the pint this time?'"
        ),
        "background": (
            "A child of Seattle's streets, rejected by her parents, who found solace, education and a home "
            "there and believes in its freedoms and codes; knows the Elven District as well as anyone. "
            "Wasp's lieutenant and open critic (a corp's hosed intelligence got the gang 'gnawed' by the "
            "Tigers; his corporate paymasters treated gang war as 'metahuman birth control'), possibly his "
            "former lover. Took over when he died on Dexter and has continued his diversification into "
            "mercenary work while trying, and failing, to rebuild ties with a Tir she has little use for."
        ),
        "notes": (
            "Believes Elven Fire is an internal splinter led by two or three ex-Ancients; has tried and "
            "failed to parley with it; grows visibly confused as outside proof mounts, and angrier as the "
            "Tir's hand shows. Will deal with runners whose help seems genuine. Does not know the Tir "
            "cabal has been feeding the High Prince lies about her. Stats: B4 Q6 S3 C6 I5 W3, Ess 5.3, "
            "Reaction 5, Init 5+2D6; Armed Combat 7, Unarmed 7, Bike 6, Firearms 6, Etiquette (Street) 5, "
            "Athletics 4, Stealth 4; Boosted Reflexes 1, improved retractable razors; armor vest, HK227 "
            "(laser, recoil reduction 3), Harley Scorpion. DMZ stats p.58."
        ),
        "contact_skills": ["Ancients muscle and street intelligence", "Downtown elven district"],
    },
    {
        "name": "Alejandro Kylisearn",
        "role": "'Green Lucifer' -- exiled Tir lord and failed coup plotter, secret mage, Wasp's assassin and the Ancients' second-in-command",
        "archetype": "Gang Lieutenant",
        "title": "\"Green Lucifer\", second-in-command of the Ancients; Lord Kylisearn of Tir Tairngire (exiled)",
        "race": "Elf",
        "gender": "Male",
        "nationality": "Tir Tairngire",
        "organization": "Ancients",
        "connection": 4,
        "description": (
            "Slightly below average height and build for an elf, but with presence to make up for it; "
            "gray eyes, a stylish purple-and-green mohawk he privately despises, and a temper that gets "
            "the better of his calculating manner. Quotes Virgil and Milton ('Better to reign in hell, "
            "than to serve in heav'n'). Curses Elven Fire in long, detailed Elvish. Rides a Harley "
            "Scorpion; keeps a Ranger Arms SM-3 in a kevlar-lined steel case."
        ),
        "background": (
            "A Tir noble whose coup against the High Prince was aborted early; his co-conspirators served "
            "him up and he was publicly sentenced to the deepest dungeon -- and secretly banished to "
            "Seattle in the custody of Wasp. Days after arriving, dressed too perfectly to pass, he joined "
            "Sting's flanking team against the Meat Junkies, shot the jester Pearl, put a 900-grain round "
            "through Wasp's nose from an upstairs window, crippled the Meat Junkie leader and became "
            "Sting's second as 'Green Lucifer'. He tells the gang he 'chose exile over imprisonment' for an "
            "unpopular cause. What he learns at the helifield: the High Prince planted him in the Ancients "
            "knowing his betrayers would one day move against the gang."
        ),
        "notes": (
            "Suspects the truth but cannot say so; fears Elven Fire knows he killed Wasp (higher caliber "
            "than the Junkies' AK-97 -- nobody did wound analysis); asks the runners to stay in constant "
            "contact so he can intercept anything about himself and 'has no qualms about removing' them. "
            "Stunned by proof the shooter was human; remembers Dumont from The Jump House. Arrives at the "
            "helifield to finish Bright ('Did I know you?'), possibly with a pair of elementals 'sent by a "
            "friend'. Afterwards: 'someone in one of the Tir's golden halls decided the Ancients had "
            "outlived their usefulness' -- and asks the runners to let it drop. Stats: B4 Q7 S4 C7 I6 W5, "
            "Magic 6, Ess 6, Reaction 6; Firearms 8, Unarmed 8, Athletics 7, Stealth 7, Sorcery 7, Armed "
            "6, Etiquette (Tir Tairngire) 6 / (Political) 4 / (Street) 3, Conjuring 3, Enchanting 3, "
            "Sperethiel 4. Spells: Powerball 6, Mana Missile 4, Heal Moderate Wounds 4, Combat Sense 3. No "
            "cyberware. Ares Light Fire 70, Uzi III, Ranger Arms SM-3, lined coat, Harley Scorpion."
        ),
        "contact_skills": ["Tir Tairngire court politics and exiles", "Ancients leadership"],
    },
    {
        "name": "Lucinda Mari Adler",
        "role": "'Lucinda Tangier' -- bored Bellevue heiress slumming in the Barrens, St. John's surviving girlfriend, untrained magician; a 50,000-nuyen bounty",
        "archetype": "Socialite",
        "title": "\"Lucinda Tangier\"; daughter of Owen T. Adler (Adler Plastics)",
        "race": "Human",
        "gender": "Female",
        "connection": 2,
        "description": (
            "Average height and build, short stylish brunette hair, blue eyes, dressed to the height of "
            "fashion in tres chic clothing, affecting a street patois that is more than a little "
            "transparent. Rich, good-looking, rich, fairly intelligent, completely lacking in common "
            "sense, and rich, in that order."
        ),
        "background": (
            "Tired of people who liked her for her money or her father, she took to visiting the Barrens "
            "as a make-believe SINless and fell for the image of a down-and-out runner called St. John, "
            "never noticing his illegal work. Found his cloak-and-dagger 'laying low' wiz until it was "
            "microwaved snacks and rented sims; came to the Witches' Circle dressed to impress to watch "
            "him 'cut a deal for some ancient secrets' and hit the floor when the shooting started. His "
            "death changed her views, though she is not yet sure how."
        ),
        "notes": (
            "Refuses to go home or to the yakuza; will bribe, coerce, fight or run to stop the runners "
            "handing her over. Knows St. John did 'special jobs' for a highly placed elven city official, "
            "went to ground 2.5 months ago after a call ('I didn't know he was there!'), recognized his "
            "killer, and that his flat was ransacked and sealed. Insists the shooter was human ('cold like "
            "the dead') -- she reflexively assensed him: magically active, untrained (Perception 6 to "
            "notice). Lone Star's file on her was deleted by illegal penetration. Stats: B2 Q3 S3 C6 I3 W3, "
            "Magic 6 (untrained), Ess 6; Unarmed 2. Possible future: a rich, grateful, untrained magician "
            "-- or a yakuza bargaining chip."
        ),
    },
    {
        "name": "St. John",
        "role": "Marginal runner wannabe who fronted Elven Fire's first hit, botched it, and died selling the story to the yakuza",
        "archetype": "Shadowrunner",
        "title": "Shadowrunner (deceased -- Witches' Circle); legal name unknown",
        "race": "Human",
        "gender": "Male",
        "organization": "Elven Fire",
        "connection": 1,
        "description": "A down-and-out runner with a good opening act who blew it by the end of every job; 'couldn't put on his underwear without screwing up'; named himself after an apostle. Loved a pun: 'I'm out of my cocoon, squeeze. I'm doing a deal for some secrets, some ancient secrets.'",
        "background": "Local underworld figure with yakuza connections in Loveland and Puyallup (Lone Star: weapons possession 2049, armor possession 2050, reckless endangerment 2051, all fined). Recruited by Shim Bright, insisted on running the Nova Rich hit himself, misread his contacts and firebombed The Jump House while Baron was meeting Green Lucifer. Paid off, lay low for two and a half months, then tried to sell Bright and the Ancients to the Whispering Nights.",
        "notes": "Shot at his table by Dumont with six yakuza the night before the adventure; cremated, no next of kin. His flat was ransacked before Lone Star sealed it. Bragged the Tir agent's identity 'would make you spit up last week's lunch'. Not the Matchstick's doorman 'Saint John' (Silver Angel).",
    },
    {
        "name": "Matthew Baelyrn",
        "role": "'Wasp' -- the Ancients' corpse-pale blond mage-leader who took corporate money for gang wars; shot through the nose by Green Lucifer",
        "archetype": "Gang Boss",
        "title": "\"Wasp\", former leader of the Ancients (deceased)",
        "race": "Elf",
        "gender": "Male",
        "organization": "Ancients",
        "connection": 3,
        "description": "Blond hair flowing down his back, a corpse-white face that shows no emotion, mirrored sunglasses in the dark, a slender body that stretches like a cat; a sorcerer whose fireballs turned Meat Junkies into votive candles. 'I run the Ancients. I do the thinking! I do the planning!'",
        "background": "The High Prince's long-time source of information and influence in Seattle, given custody of the exiled Kylisearn. Under him the gang diversified into mercenary and corporate muscle work, a corp's bad intelligence got them mauled by the Tigers, and the Tir's intelligence arm soured on the Ancients. Took a corporate contract to 'consolidate' the blocks from Dexter to Aurora and died in that battle -- the street says to a Meat Junkie sniper, Lone Star's file says 'approximately one year ago'.",
        "notes": "Half-Ace, his trusted aide, bragged he knew something about Wasp 'that nobody, including those in the Tir, would want known'. Corporate contacts: 'rendered faceless by a high-caliber slug'. No stats.",
    },
    {
        "name": "Falchion",
        "role": "Highly placed Ancients street soldier loyal to Sting and Green Lucifer; gave KTXX the 'colors not stained red' interview",
        "archetype": "Gang Lieutenant",
        "title": "Ancients street soldier (leadership circle)",
        "race": "Elf",
        "gender": "Male",
        "organization": "Ancients",
        "connection": 2,
        "description": "One of the three Ancients waiting on the dry dock. An independent thinker whose loyalties to Sting and Green Lucifer run deep; listens carefully and remembers. On the news: 'If blood is what they demand as tribute, then by god blood is what they shall get. And when we do, the only colors not stained red will be ours.'",
        "notes": "Ancients Soldier stats (B4 Q6 S4 C3 I3 W4; Armed 6, Firearms 5; Uzi III laser, Beretta 101T, flash and smoke grenades, lined coat, Honda Viking). Use him and Viper for later intrigue inside the gang.",
    },
    {
        "name": "Viper",
        "role": "Newer Ancients rider who leads the runners' escort to the Tacoma dock; listens, remembers, and may talk to the rank and file",
        "archetype": "Gang Member",
        "title": "Ancients street soldier",
        "race": "Elf",
        "gender": "Female",
        "organization": "Ancients",
        "connection": 2,
        "description": "The lone rider in green and black who meets the runners at Highland and Terry, gathers an army through the streets and leads them down the slip. Newer to the gang than Falchion and less bound to its leaders; an independent thinker who takes no action now but remembers everything said at the parley.",
        "notes": "Ancients Soldier stats. A GM lever for future Ancients politics -- especially anything that sounded like a threat to the gang as a whole.",
    },
    {
        "name": "Vandal",
        "role": "Ancients soldier turned Elven Fire; the blanket-wrapped gunman in apartment 17J who hired the ambush thugs",
        "archetype": "Gang Member",
        "title": "Ancients soldier (Elven Fire faction)",
        "race": "Elf",
        "gender": "Male",
        "organization": "Elven Fire",
        "connection": 1,
        "description": "Sits half-facing the door in Half-Ace's old flat, wrapped in an old blanket with an SMG under it, a trideo game show for company. 'I understand you're looking for Elven Fire. You've found it.'",
        "notes": "Hired and dressed the four thugs. Knows Bright only as 'Rook', met only at the Renton bottling plant; believes Rook's plan is to replace Sting and Green Lucifer with a new gang under Rook (not called Elven Fire); has assisted Dumont on hits and is frightened of him ('the common foe'). Does not know the Tir is behind it. Does not take hostages. Ancients Soldier stats.",
    },
    {
        "name": "Tirade",
        "role": "Elven Fire's Ancients mage: attacks the tenement ambush astrally with two Force 5 elementals while a Watcher guards his body",
        "archetype": "Street Mage",
        "title": "Ancients mage (Elven Fire faction)",
        "race": "Elf",
        "gender": "Male",
        "organization": "Elven Fire",
        "connection": 1,
        "description": "Hidden across the street from the tenement; on the first shot he launches astrally into apartment 17J flanked by a Fire Elemental and an Air Elemental, hitting spell locks, foci and spirits while the elementals manifest and fight.",
        "notes": "Knows the same as Vandal (Rook, the bottling plant, fear of Dumont). Stats: B4 Q3 S2 C3 I4 W5, Magic 6; Sorcery 7, Conjuring 6, Magic Theory 4; Astral pool 9. Spells: Powerball 6, Stun Missile 5, Armor 4, Clairvoyance 4, Heal Moderate Wounds 4, Mana Bolt 4. Power Focus 2, Weapon Focus 2, Fire Elemental F5, Air Elemental F5, Watcher F3; armor jacket, Uzi III, Honda Viking.",
    },
    {
        "name": "Half-Ace",
        "role": "Legless original Ancient and Wasp's old aide, 'Nick' to his neighbors; killed by Bright four months ago and used as bait",
        "archetype": "Gang Member",
        "title": "Former Ancient (deceased); Bargain Basement tenant 'Nick'",
        "race": "Elf",
        "gender": "Male",
        "organization": "Ancients",
        "connection": 1,
        "description": "One of the original Ancients and one of Wasp's most trusted aides until harsh words with Wasp and a losing fight with a semitrailer put him out of the gang; lost both legs and his body rejected every replacement. Lived in apartment 17J in a Bargain Basement tenement, where the neighbors knew him as Nick.",
        "notes": "Bragged he knew something about Wasp nobody in the Tir would want known. A snazzy elf in a Westwind (Bright) argued with him four months ago; he vanished two days later -- an early victim of Bright's attempts to learn Ancients secrets. Word of his death has not got around, so Bright's tip checks out.",
    },
    {
        "name": "Pearl",
        "role": "The Ancients' jester with a pink scar over a milky eye; named Kylisearn 'Greenie', then took his bullet",
        "archetype": "Gang Member",
        "title": "Ancients rider (deceased)",
        "race": "Elf",
        "gender": "Male",
        "organization": "Ancients",
        "connection": 1,
        "description": "The gang's clown -- pink scar slashed over one milky eye, drops his pants in derision, wipes his hands on the newcomer's jacket ('His Majesty has sent his Minister of Fashion to us') -- and Wasp's whispered watchdog on the greenie.",
        "notes": "Prologue only. Shot by Kylisearn in the sniper's window the moment he realized who the target was.",
    },
    {
        "name": "Tiny",
        "role": "Huge, ugly Ancients elf 'big enough to be half troll' who adopted Greenie as his pal",
        "archetype": "Gang Member",
        "title": "Ancients rider",
        "race": "Elf",
        "gender": "Male",
        "organization": "Ancients",
        "connection": 1,
        "description": "Looks like the result of an unholy union between elf and troll. Rides at the back of the pack with the newcomer, explains that only the leader can give you a street name, takes two rounds through the shoulder and gets up to shove an AK-97 in a Meat Junkie's face.",
        "notes": "Prologue only; presumably still riding under Sting. Nearly killed by a barghest until Sting cut it in half.",
    },
    {
        "name": "Keno",
        "role": "Co-leader of the Eastsiders who brings his elves to the Ancients' war",
        "archetype": "Gang Boss",
        "title": "Co-leader, Eastsiders",
        "race": "Elf",
        "gender": "Male",
        "organization": "Eastsiders",
        "connection": 2,
        "description": "With Johnny Dark, pulled the Eastsiders together to meet the Ancients at the border on Westlake and ride against the Meat Junkies.",
        "notes": "Prologue name only. Ancients Soldier stats if needed.",
    },
    {
        "name": "Johnny Dark",
        "role": "Co-leader of the Eastsiders alongside Keno",
        "archetype": "Gang Boss",
        "title": "Co-leader, Eastsiders",
        "race": "Elf",
        "gender": "Male",
        "organization": "Eastsiders",
        "connection": 2,
        "description": "Keno's partner in leading the Eastsiders, the elven gang that added half again to the Ancients' strength on Dexter.",
        "notes": "Prologue name only.",
    },
    {
        "name": "Mitchell Corbin",
        "role": "'Baron' -- Nova Rich leader killed at The Jump House while secretly meeting Green Lucifer",
        "archetype": "Gang Boss",
        "title": "\"Baron\", leader of the Nova Rich (deceased)",
        "race": "Elf",
        "gender": "Male",
        "organization": "Nova Rich",
        "connection": 2,
        "description": "One of the leaders of Bellevue's rich-kid gang, at The Jump House incognito for a private meeting with the Ancients' second-in-command when St. John's firebomb went off.",
        "notes": "What he and Green Lucifer were discussing is never said -- a free hook. Everyone who knew of the meeting died with him.",
    },
    {
        "name": "Toshihiro Ino",
        "role": "Oyabun of the Whispering Nights: a patient, honor-bound old yakuza willing to hear 'honorless beasts' if they show respect",
        "archetype": "Crime Boss",
        "title": "Oyabun, Whispering Nights (Loveland)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Whispering Nights",
        "connection": 5,
        "description": "Sits at the head of a low table in a traditional room, his sons on his right, Chen and Ejima on his left, and speaks of everything under the sun for an hour before business. Not a stupid man; suspicious enough of the Witches' Circle killings to listen to alternatives, and privately glad to see the Tigers taught humility -- even by ronin.",
        "notes": "Convinced, he grants 48 hours to prove the Ancients innocent over Ejima's and Hoshiro's objections. Holds Lucinda as a negotiating point if the Tigers caught her. Stats: B2 Q3 S3 C5 I6 W5, Ess 6, Reaction 4; Etiquette (Yakuza) 8, (Street) 5, Leadership 5, Negotiation 5, Firearms 5, Business Management 6, Economics 5; Form-Fitting Body Armor 2. Second disrespect ends the meeting.",
        "contact_skills": ["Whispering Nights clan and Loveland underworld", "Japanese-style negotiation"],
    },
    {
        "name": "Hoshiro Ino",
        "role": "The oyabun's first son, sharing power with Willy Chen; urges swift retribution against the Ancients",
        "archetype": "Yakuza Lieutenant",
        "title": "First son of the oyabun, Whispering Nights",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Whispering Nights",
        "connection": 3,
        "description": "Signals for tea and argues for swift, just retribution against the Ancients; worries that a 48-hour delay gives the elves time to marshal their defenses. Spelled 'Hoshihiro' once in the book.",
        "notes": "Stats: B5 Q4 S4 C3 I4 W5, Ess 6; Negotiation 4, Etiquette (Yakuza) 4, Economics 4; Beretta 200ST (laser), Form-Fitting Body Armor 2.",
    },
    {
        "name": "Mamoru Ino",
        "role": "The oyabun's third son: the polite young man in dark glasses who greets the runners and administers the three tests",
        "archetype": "Yakuza Soldier",
        "title": "Third son of the oyabun, Whispering Nights",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Whispering Nights",
        "connection": 2,
        "description": "A young Japanese man in dark glasses and a suit who bows once to each visitor and waits for the courtesy to be returned. Invites, never demands: weapons on the porch, shoes for slippers, three runners only. Glares fiercely when a meeting ends badly.",
        "notes": "No say in clan business. Stats: B4 Q5 S4 C4 I4 W4, Ess 6; Armed 4, Firearms 4, Negotiation 3, Etiquette (Yakuza) 4, Business Management 3, Economics 3; Beretta 200ST (laser, burst), Form-Fitting Body Armor 2. The book's example of Romanized name order (Ino Mamoru in Japan).",
    },
    {
        "name": "Midori Ino",
        "role": "The oyabun's blind daughter, a grade-3 initiate mage who sees through Clairvoyance and reports every visitor's aura to her father by Mind Speech",
        "archetype": "Mage",
        "title": "Daughter of the oyabun; initiate mage (Way of the Whispering Nights)",
        "race": "Human",
        "gender": "Female",
        "nationality": "Japanese",
        "organization": "Whispering Nights",
        "connection": 3,
        "description": "A young woman in a traditional gown with modern styling, listening to old Japanese music on an expensive chip-player in an otherwise bare tatami room, staring at the wall with opaque, sightless eyes. In astral space she is not blind at all: her astral form gives an assensing runner a sly grin and shakes its head.",
        "notes": "Sustains Personal Clairvoyance (No Range) for sight and a custom Mind Speech spell to her father. No say in clan matters -- and the most dangerous person in the house. Stats: B2 Q5 S2 C5 I5 W5, Magic 9, Ess 6; Initiate grade 3; Sorcery 7, Conjuring 6, Magic Theory 5, Negotiation 4, Etiquette (Yakuza) 5, Ritual Dance 6 (centering), Popular Dance 5; Astral pool 10. Spells: Influence 9, Stun Touch 9, Power Missile 7, Mana Bolt 6, Personal Anti-Spell Barrier 6, Fire Bolt 5, Personal Anti-Bullet Barrier 5, Oxygenate 4, Stabilize 4, Entertainment 3, Heal Moderate 3, Clairvoyance 3, Combat Sense 3, Detect Enemies (Extended). Power Focus 3, knife, Form-Fitting Body Armor 1.",
        "contact_skills": ["Japanese hermetic tradition and initiation", "Astral assessment of visitors"],
    },
    {
        "name": "Willy Chen",
        "role": "First lieutenant of the Whispering Nights, sharing power with Hoshiro; the voice for study over vengeance",
        "archetype": "Yakuza Lieutenant",
        "title": "First lieutenant, Whispering Nights",
        "race": "Human",
        "gender": "Male",
        "organization": "Whispering Nights",
        "connection": 4,
        "description": "Seated at the oyabun's left; argues that city-wide events and the uncharacteristic nature of the Witches' Circle attack call for further study before retribution. The negotiator of the clan.",
        "notes": "Stats: B2 Q2 S2 C4 I6 W4, Ess 6, Reaction 4; Negotiation 6, Etiquette (Street) 6, (Yakuza) 6, Unarmed Combat 6; Form-Fitting Body Armor 2. The runners' natural ally inside the clan.",
        "contact_skills": ["Whispering Nights negotiations", "Loveland street intelligence"],
    },
    {
        "name": "Robert Ejima",
        "role": "Warlord of the Tigers, a grade-5 adept who wants to bring the oyabun Sting's head in a basket",
        "archetype": "Physical Adept",
        "title": "Warlord of the Tigers (of the Neon Jungle)",
        "race": "Human",
        "gender": "Male",
        "organization": "The Tigers",
        "connection": 3,
        "description": "Sits at the oyabun's left beside Chen and delights in every rise of tension in the room; vocally upset by any runner who has roughed up his Tigers, to the point of earning the oyabun's reprimand. Volunteered Sting's head; politely declined, for now.",
        "notes": "Holds grudges over Lucinda and the warehouse fight. Stats: B4(8) Q4 S4(7) C2 I2 W4, Ess 6, Reaction 3(7), Init 3(7)+3D6; Unarmed 9, Armed 8, Etiquette (Yakuza) 7, Firearms 6, Stealth 6, Throwing 6, Athletics 5, Interrogation 5, Etiquette (Street) 5; Initiate grade 5 (Tigers of the Neon Jungle); Killing Hands, Body +4, Strength +3, Reaction +2, Automatic Successes (Unarmed) 2; armor vest, Browning Max-Power (explosive).",
    },
    {
        "name": "Tok",
        "role": "Teenage yakuza go-between in a Supersonics jacket and Seahawks cap who walks the runners to the Whispering Nights",
        "archetype": "Gang Member",
        "title": "Runner / guide for the Whispering Nights",
        "race": "Human",
        "gender": "Male",
        "organization": "Whispering Nights",
        "connection": 1,
        "description": "An Asian youth in his mid or late teens: jeans, cowboy boots, a western shirt, an old Seattle Supersonics jacket, a current Seahawks baseball cap and dark wraparound shades. Will give only the name 'Tok'.",
        "notes": "Meets the runners somewhere near Loveland and leads them to the cafe. No stats.",
    },
    {
        "name": "Hanzo Shotozumi",
        "role": "Oyabun of the Dungeness Crab clan, 'the yakuza who run Seattle' in this book; wants face restored, not a blood bath",
        "archetype": "Crime Boss",
        "title": "Oyabun, Dungeness Crab Clan (Seattle)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Dungeness Crab Clan",
        "connection": 6,
        "description": "The big oyabun of street rumor, giving the Whispering Nights grief 'about honor'. Not asking for slaughter; asking for resolution.",
        "notes": "Off-stage. See the discrepancy note on the Yakuza (Watada-rengo) row before using him at the table.",
    },
    {
        "name": "Kim Marsau",
        "role": "Oyabun of the Marsau Clan, Puyallup's most powerful yakuza group",
        "archetype": "Crime Boss",
        "title": "Oyabun, Marsau Clan (Puyallup)",
        "race": "Human",
        "gender": "Male",
        "organization": "Marsau Clan",
        "connection": 5,
        "description": "Puyallup's senior oyabun, pressing Toshihiro Ino to settle the Witches' Circle matter.",
        "notes": "Off-stage name; gender not stated in the book.",
    },
    {
        "name": "Owen T. Adler",
        "role": "Short, booming single-cast-plastic-furniture magnate who understands nothing but his business and wants 'his baby' back",
        "archetype": "Corporate Executive",
        "title": "Owner, Adler Plastics (Bellevue)",
        "race": "Human",
        "gender": "Male",
        "organization": "Adler Plastics",
        "connection": 4,
        "description": "A dwarf ... no, a human, just short, with a voice twice as large as his body, coming round the smoked-acrylic desk with hand and arm outstretched: 'I understand you're gonna find my baby?' Think Danny DeVito crossed with Nathan Arizona Sr. Insists on hearing everything about his daughter, 'that pile of filth' she ran with (St. John's death does not register) and 'this gang-war thing', and gets confused by any real explanation.",
        "notes": "Corporate Official contact stats (Sprawl Sites p.107). 50,000 certified for Lucinda on his doorstep, 25,000 for her location; no middlemen. Does not know his daughter is Awakened.",
        "contact_skills": ["Corporate money, no questions (Bellevue)", "Plastics industry"],
    },
    {
        "name": "Moose",
        "role": "Three-meter mountain of custom silk who guards Owen T. Adler and can recite Paradise Lost in twelve languages",
        "archetype": "Bodyguard",
        "title": "Bodyguard to Owen T. Adler",
        "race": "Troll",
        "gender": "Male",
        "organization": "Adler Plastics",
        "connection": 1,
        "description": "Almost three meters tall and maybe half as wide, smiling as he says 'Moose' and adjusts the cuffs of an obviously custom-tailored silk suit; takes up the rear down the white marble corridor, still grinning. Inhumanly big, impossibly strong, and not, as you might think, stupid.",
        "notes": "Race not stated ('he (you think)'); troll by size. Give him whatever stats make him an effective foil. Go ahead, ask him about Milton.",
    },
    {
        "name": "Eleanor",
        "role": "Owen T. Adler's harried executive secretary who opens the rosewood doors",
        "archetype": "Corporate Wage Slave",
        "title": "Executive secretary to Owen T. Adler",
        "race": "Human",
        "gender": "Female",
        "organization": "Adler Plastics",
        "connection": 1,
        "description": "Rushes from her desk to push the giant rosewood doors open with one hand and her glasses back up her nose with the other. 'Mr. Adler will see you now.' 'Thank you, Eleanor,' rumbles Moose.",
        "notes": "One line of color; the person who actually knows Adler's calendar.",
    },
    {
        "name": "Simon Johnson",
        "role": "Owner of the Witches' Circle, cashing in on St. John's murder while hiding Lucinda in his warehouse",
        "archetype": "Club Owner",
        "title": "Owner, Witches' Circle (and its building and the warehouse behind it)",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": "Laughs openly at accusations: 'Though I'm sure there's a connection between St. John's death and my current fiscal good health, I think continuing that particular business strategy might end up being bad for my personal health.' Has redecorated with the public's tastes for years; opens early and closes late now that death sells.",
        "notes": "Club Owner contact (Sprawl Sites p.106); no bodyguard, staff on PANICBUTTONs; his office is bugged and he does not know it. Lucinda was 'chummer to somebody' at the club before St. John -- him. Leads runners who seem willing to help her to the warehouse; after the Tigers hit it, frightened for his life, he drops her. Rumor calls him 'Sam Johnson or something'.",
        "contact_skills": ["Loveland nightlife and who drinks where", "A quiet warehouse"],
    },
    {
        "name": "Thorton",
        "role": "Aging ork bouncer at the Witches' Circle dressed like a Halloween shadowrunner, who blanches at the real thing",
        "archetype": "Bouncer",
        "title": "Bouncer, Witches' Circle",
        "race": "Ork",
        "gender": "Male",
        "connection": 1,
        "description": "An aging ork in costume shadowrunner gear at the door under the new neon sign. Scowls, blinks, blanches, and asks very politely if he can help you; tries to keep runners out and lets them past if pushed.",
        "notes": "Pedestrian stats. Gives the media version of the shooting and nothing else.",
    },
    {
        "name": "Shannon",
        "role": "Hostess at the Witches' Circle who seats the runners and repeats the newscast",
        "archetype": "Hostess",
        "title": "Hostess, Witches' Circle",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": "Greets the runners promptly, introduces herself and shows them to a booth. Properly nervous; retreats if pressed beyond the official story.",
        "notes": "Pedestrian stats. Knows the staff's fingers are on PANICBUTTONs.",
    },
    {
        "name": "Father William Roe",
        "role": "Lutheran minister running a Redmond street-kid shelter; Thark's back channel to runners Lone Star cannot approach",
        "archetype": "Priest",
        "title": "Lutheran minister; director of a Redmond youth shelter",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": "An old acquaintance of one of the runners, not spoken to in some time. May welcome them warmly on Thark's word or see them as the hopeless future of the kids he shelters; either way his plea is the same -- the violence will draw the kids in as victims or recruits. Introduces Thark, not immediately by name, as someone who shares their concern or 'understands the value of community and choices'.",
        "notes": "Store Owner contact stats (Sprawl Sites p.119). Uses the office in the corner of the shelter; can calm a meeting that goes wrong with the kids' help.",
        "contact_skills": ["Redmond street kids and what they see", "Back channel to Koren Thark"],
    },
    {
        "name": "Wiser",
        "role": "Redmond street kid ('why-zer') who carries Father Roe's summons and guarantees there is money in it",
        "archetype": "Street Kid",
        "title": "Street kid, Father Roe's shelter",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": "Familiar by sight to at least one runner. Delivers the message that Roe wants to talk that evening, will 'guarantee' there is money in it, and leads the way if asked.",
        "notes": "Street Kid stats (Sprawl Sites p.119). Some of the other kids get intrigued by overt runners.",
    },
    {
        "name": "Whisper",
        "role": "Near-mute ork custodian and guardian of Father Roe's shelter, fists first, billy club second, antique AK-47 last",
        "archetype": "Ork Mercenary",
        "title": "Custodian / guardian, Father Roe's shelter",
        "race": "Ork",
        "gender": "Male",
        "connection": 1,
        "description": "Named for his manner of speech. Always there; sleeps and works in the room opposite Roe's office, where he keeps an antique AK-47 hidden. Prefers his fists, then a handy billy club (Str+1 M2 Stun), then the rifle.",
        "notes": "Ork Mercenary archetype (SR p.41). Thark steps out of his room to make the pitch.",
    },
    {
        "name": "William Loudon",
        "role": "Lone Star's Seattle chief who asked the Governor to mobilize the Metroplex Guard against the gangs",
        "archetype": "Corporate Executive",
        "title": "Regional director / Division Head, Lone Star Seattle",
        "race": "Human",
        "gender": "Male",
        "organization": "Lone Star Security",
        "connection": 5,
        "description": "Lone Star's Seattle chief, who decided the gang conflict is warfare and should be treated as such, put every officer and employee on active duty (cancelling vacations, leaves and retirements), and personally advised Governor Schultz to consider mobilizing the Metroplex Guard.",
        "notes": "Off-stage. The man who reprimanded Thark; consults Shim Bright on elven affairs.",
    },
    {
        "name": "Carol Lake",
        "role": "Lone Star Security spokesperson: the contract does not cover violence on this scale; later, Elven Fire 'was a hoax'",
        "archetype": "Spokesperson",
        "title": "Spokesperson, Lone Star Security (Seattle)",
        "race": "Human",
        "gender": "Female",
        "organization": "Lone Star Security",
        "connection": 3,
        "description": "Reached for comment on KTXX: the terms of Lone Star's contract with the metroplex do not encompass prolonged violence on this scale, local assets are at breaking point, and Lone Star will strive to maintain order. On May 20 she tells NewsNet the whole Elven Fire organization was a hoax aimed at breaking up the Ancients and refuses comment on Tir rumors.",
        "notes": "News handouts only.",
        "contact_skills": ["Lone Star's official line, a day early"],
    },
    {
        "name": "Captain Mickey Colton",
        "role": "Metroplex Guard captain whose platoon lost its APC to wiz-kid mages in the International District (failure news)",
        "archetype": "Military Officer",
        "title": "Captain, Seattle Metroplex Guard",
        "race": "Human",
        "gender": "Male",
        "organization": "Seattle Metroplex Guard",
        "connection": 2,
        "description": "Commands a platoon of eight men and an armored personnel carrier. 'The little bastards just jumped us, no warning, no nothing. Since they were just kids I told my men to hold their fire, then the APC went up and I thought, screw that.' Denies his men fired the missile that blacked out the International District.",
        "notes": "Failure-ending news only. A face for the Guard if martial law becomes the campaign.",
    },
    {
        "name": "Master Sergeant Seamus LeGuinne",
        "role": "Fort Lewis spokesman who reported 'light casualties' from the British Royal Family's inspection",
        "archetype": "Military NCO",
        "title": "Spokesman, Fort Lewis",
        "race": "Human",
        "gender": "Male",
        "organization": "Seattle Metroplex Guard",
        "connection": 2,
        "description": "Fort Lewis spokesman quoted in the May 20 news: the British Royal Family inspected the fort and casualties were light (special photo section and casualty list, page 14).",
        "notes": "News only. Whether he is Guard or UCAS Army is not stated.",
    },
    {
        "name": "Dr. Walter Hunt",
        "role": "Seattle University expedition leader back from Southeast Asia with four of twelve alive after a Vietnamese bandit king",
        "archetype": "Academic",
        "title": "Research expedition leader, Seattle University",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": "'It's all too soon, all too tragic.' Refuses to discuss the deaths of eight team members; the university says his team ran afoul of a Vietnamese bandit king and had to be rescued.",
        "notes": "May 20 news; a hook for a Southeast Asian sequel. The book says 'Seattle University' (see the University of Seattle row).",
    },
    {
        "name": "Dr. Carmela Cuomo",
        "role": "Seattle University marine biologist ruling the giant geoduck abnormal but not paranormal",
        "archetype": "Academic",
        "title": "Marine biologist, Seattle University",
        "race": "Human",
        "gender": "Female",
        "connection": 2,
        "description": "'It appears to be purely of the species Panope generosa. And very generosa, at that.' Needs the mollusk dead for a proper tissue test and declines to speculate how it got so big.",
        "notes": "May 20 news.",
        "contact_skills": ["Puget Sound marine biology and paracritter screening"],
    },
    {
        "name": "Jerome Einsdorff",
        "role": "Mariners owner denying rumors of a move to Oakland unless the Kingdome's management changes",
        "archetype": "Businessman",
        "title": "Owner, Seattle Mariners",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": "'If we get the changes we want in Kingdome management, we will happily stay here.'",
        "notes": "May 20 news; Kingdome leverage.",
    },
    {
        "name": "Ellen Donnelly",
        "role": "Shadow-market figure blown up in her Saab Dynamit outside Matchstick's -- 'a professional assassination'",
        "archetype": "Fixer",
        "title": "Underworld figure (deceased -- car bomb, May 19, 2053)",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": "Killed instantly at 11:45 p.m. when her Saab Dynamit exploded on ignition outside the jazz club Matchstick's; reportedly tied to underworld figures of the shadow market and other crime syndicates, and not a member of the private club. Lone Star has no leads.",
        "notes": "Both endings carry the story: whoever killed her is a free plot thread, and Matchstick's doorman Saint John would remember her face.",
    },
    {
        "name": "John Whimmer",
        "role": "KTXX correspondent on why today's air may be the best you breathe all year",
        "archetype": "Reporter",
        "title": "Correspondent, KTXX",
        "race": "Human",
        "gender": "Male",
        "organization": "KTXX",
        "connection": 1,
        "description": "Follows the gang-war coverage with an air-quality segment on the one sunny day of the adventure.",
        "notes": "Handout 1 only.",
    },
]

ORG_UPDATES = {
    "Ancients": {
        "description_append": (
            "Elven Fire (Lone Star Handout 4): street gang with go-gang tendencies; territory the "
            "metahuman communities and the elven district north-northeast of Denny Park; interests weapons "
            "smuggling, mercenary activity and pro-elven/metahuman action; exclusively elven, about 72 "
            "percent male, believed to recruit Tir Tairngire political outcasts, 100-150 members citywide. "
            "Appeared shortly after the birth of Tir Tairngire with a strong, covert connection to the "
            "elven state; capabilities sometimes approach a tactical military unit's; armaments allegedly "
            "smuggled from the Tir. Colors black-blue and green. No traditional allies (assist the Silent "
            "P's); enemies the Emerald Dogs, Humanis Policlub and the Meat Junkies. 'In Seattle, the "
            "Ancients are regarded not so much as a biker gang, but as a force of nature.'"
        ),
        "notes_append": (
            "Elven Fire: the gang has been the High Prince's source of information and influence in "
            "Seattle since its founding, fed weapons across the border; under Wasp (then Sting) it "
            "diversified into corporate muscle and mercenary work, the Tir's intelligence arm soured on it, "
            "and the High Prince's opposition -- fed lies -- decided to destroy it and replace it with a "
            "loyal copy (Shim Bright, Elven Fire). Leadership succession: Wasp killed on Dexter by Green "
            "Lucifer's sniper rifle during a corporate-paid 'consolidation' against the Meat Junkies (the "
            "street blames a Junkie sniper); Sting, his lieutenant and critic, now leads with Green Lucifer "
            "second, Falchion and Viper in the circle, plus dissent over the mercenary policy. Internal "
            "'civil war' rumors; a few peripheral members have been bought by Bright (Vandal, Tirade). "
            "Ancients never go in for cyberware. Soldier block (p.25): B4 Q6 S4 C3 I3 W4; Armed 6, "
            "Firearms 5; Beretta 101T, Uzi III (laser), flash/smoke grenades, lined coat, Honda Viking. "
            "Mage block: B4 Q3 S2 C3 I4 W5 M6; Sorcery 6; Powerball 6, Mana Bolt 4, Stun Missile 3, Heal "
            "Moderate 4. Contact: Etiquette (Street) 4 (3 for elves), meet in 2D6+4 hours minus successes at "
            "Highland and Terry, escorted to a Tacoma dry dock; leadership parley p.23-25. Recently making "
            "local weapons purchases as Tir shipments dwindle; weapons still cross the border to someone "
            "else. Outcome: lose some face when Elven Fire is exposed, gain the runners as friends, and "
            "everyone involved lands on a Tir list of meddlers. DMZ stats p.58-60."
        ),
        "leadership_add": [
            {"name": "Sting", "title": "Leader", "notes": "Elven Fire; took over from Wasp."},
            {"name": "Alejandro Kylisearn", "title": "Second-in-command 'Green Lucifer'", "notes": "Exiled Tir lord; killed Wasp."},
            {"name": "Matthew Baelyrn", "title": "Former leader 'Wasp' (deceased)", "notes": None},
            {"name": "Falchion", "title": "Street soldier (leadership circle)", "notes": None},
            {"name": "Viper", "title": "Street soldier", "notes": None},
        ],
        "allies_add": ["Eastsiders", "Silent P's"],
        "enemies_add": ["Meat Junkies", "Emerald Dogs", "The Tigers", "Whispering Nights", "Elven Fire", "Humanis Policlub"],
    },
    "Lone Star Security": {
        "notes_append": (
            "Elven Fire (May 2053): Seattle chief William Loudon treats the gang war as warfare -- every "
            "officer on active duty, retirements cancelled -- and asks Governor Schultz to mobilize the "
            "Metroplex Guard; spokesperson Carol Lake says the metroplex contract 'does not encompass "
            "prolonged violence on this scale'. Detective Koren Thark (Street Affairs Division / Metahuman "
            "Gangs) is reprimanded for dissenting and hires runners with discretionary funds. Lone Star "
            "Data Services synopses on the Ancients, Elven Fire, Lucinda Tangier (deleted by illegal "
            "penetration) and St. John are Handouts 4-7. Out-of-house Counsel on Elven Affairs is Shim "
            "Bright, a Tir agent. Responds to a helifield disturbance as low priority; will arrive in force "
            "to keep the peace, not to arrest Bright. Success ending: containment over confrontation; "
            "overnight violence down 71 percent in a week."
        ),
        "leadership_add": [
            {"name": "William Loudon", "title": "Regional director / Division Head, Lone Star Seattle", "notes": "Elven Fire."},
            {"name": "Koren Thark", "title": "Detective, Street Affairs Division (Metahuman Gangs)", "notes": "Elven Fire; hires the runners."},
            {"name": "Carol Lake", "title": "Spokesperson", "notes": "Elven Fire news handouts."},
        ],
    },
    "Knight Errant Security Services": {
        "notes_append": (
            "Elven Fire: Shim Bright hires three Knight Errant guards within hours for the helifield (B4 Q4 "
            "S4 C3 I3 W4; Boosted Reflexes 1, smartlink; Ares Predator II, H&K MP5-TX, airfoil concussion "
            "grenades, armor jacket; Security Procedures 3). Contract is personal defense only, not full-"
            "aspect combat: they ask approaching runners to drop weapons, defend Bright with less "
            "enthusiasm once he provokes the fight, call for back-up, and will not engage Lone Star."
        ),
    },
    "Tir Tairngire": {
        "notes_append": (
            "Elven Fire (2053): the High Prince's court is split. A powerful cabal opposing the High Prince "
            "runs its own agents in Seattle -- Shim Bright, ten years established as the city's elven-affairs "
            "consultant -- and ordered the Ancients (the Prince's covert Seattle intelligence conduit) "
            "destroyed and replaced. The Prince, who exiled the coup plotter Lord Alejandro Kylisearn to the "
            "Ancients in secret while announcing a dungeon sentence, planted him there to fight exactly this "
            "play ('who better to guard the sheep from the wolves than another wolf?'). The Tir's foreign "
            "intelligence arm smuggles weapons to the Ancients (now dwindling; some shipments go elsewhere). "
            "A camp called The House 're-educates' captured foreign agents (Michael Dumont). Bright flees on "
            "a Federated Boeing Commuter with Tir registration and forged Salish-Shidhe papers; the Tir "
            "embassy refuses comment on Elven Fire. Runners who succeed 'appear on a long list of meddlers "
            "to be dealt with in Tir Tairngire'."
        ),
        "enemies_add": ["Elven Fire"],
    },
    "Seattle Metroplex Guard": {
        "notes_append": (
            "Elven Fire (May 2053): home at Fort Lewis; the UCAS carrier Koontz, in from the Pacific, runs "
            "heavy air operations ferrying to the fort. Governor Schultz suspends all leaves at the "
            "24-hour mark and orders the Guard into the streets at 36 if the runners are slow. Failure "
            "ending: a quasi-military force with state-of-the-art support gear rolls out after the yakuza's "
            "48-hour deadline; much of the city goes to a AAA security rating; the gangs stop fighting each "
            "other to fight the Guard; sixth day of martial law, 118 dead, a platoon under Captain Mickey "
            "Colton loses its APC to wiz-kid mages and the International District loses power; Washington "
            "considers putting the Koontz battlegroup under Guard command. 'If any of you remember '39, "
            "the Night of Rage will look like a footnote.'"
        ),
        "leadership_add": [
            {"name": "Captain Mickey Colton", "title": "Platoon commander", "notes": "Elven Fire failure ending."},
        ],
    },
    "Humanis Policlub": {
        "notes_append": "Elven Fire (Lone Star Handout 4): the Ancients' harassment of the policlub is long-standing; Lone Star lists Humanis among the gang's known enemies.",
        "enemies_add": ["Ancients"],
    },
    "Seoulpa Rings": {
        "notes_append": "Elven Fire: a Redmond Seoulpa Ring runs a numbers setup backed by the Leather Devils gang; a week after The Jump House bombing a decker lifted an unknown sum from its secret Matrix account and left a dumb frame of an elf in Ancients colors wreathed in flame -- Elven Fire's second hit.",
    },
    "Yakuza (Watada-rengo)": {
        "notes_append": (
            "Elven Fire discrepancy: this book names the Dungeness Crab clan under oyabun Hanzo Shotozumi "
            "as 'the yakuza who run Seattle', with the Marsau Clan (Kim Marsau) senior in Puyallup and the "
            "Whispering Nights (Toshihiro Ino) holding Loveland, and never mentions the Watada-rengo. Earlier "
            "canon stands; treat the Crabs as one of the clans under (or beside) the rengo as the table "
            "prefers. 'The Loveland Whispering Nights are but one of the many yakuza clans operating in and "
            "around Seattle.'"
        ),
    },
    "405 Hellhounds": {
        "notes_append": "Elven Fire: hit by 'Elven Fire' about three weeks before the adventure, in the wave that reached the big gangs.",
        "enemies_add": ["Elven Fire"],
    },
    "Halloweeners": {
        "notes_append": "Elven Fire: 'even the Halloweeners' were hit by Elven Fire about three weeks before the adventure.",
        "enemies_add": ["Elven Fire"],
    },
    "Red Rovers": {
        "notes_append": "Elven Fire: on Elven Fire's hit list about three weeks before the adventure.",
        "enemies_add": ["Elven Fire"],
    },
    "Blood Rumblers": {
        "notes_append": "Elven Fire (KTXX, Handout 1): the go-gang clashed with its street rivals the Gothic Phantoms in Snohomish near Shadow Lake on the fourth day of the war; two Rumblers and three passersby dead.",
        "enemies_add": ["Gothic Phantoms"],
    },
    "Crimson Crush": {
        "notes_append": "Elven Fire: a few Crimson Crush members were geeked outside a Bargain Basement tenement in Redmond four hours before Bright's ambush there -- police tape and pools of ork blood; part of what keeps the whole building jittery.",
    },
    "Seattle News-Intelligencer": {
        "notes_append": (
            "Elven Fire: Update-Net of Tuesday May 20 2053 (both endings): Spirit Air jumbo jet down in the "
            "Andes 200 km south of Machu Picchu with 254 aboard (pilgrim charter airline); the British Royal "
            "Family visits Seattle and inspects Fort Lewis, 'casualties light' (Master Sergeant Seamus "
            "LeGuinne); Peggy's Playful Porkers at Siegmund's; Mariners owner Jerome Einsdorff denies a move "
            "to Oakland, California Free State; a Seattle University expedition returns from Southeast Asia "
            "with four of twelve alive (Dr. Walter Hunt; a Vietnamese bandit king); Ellen Donnelly killed by "
            "a car bomb outside Matchstick's (P. Daza); a 1.63-meter geoduck at Frank's Fish World (T. "
            "Gallagher; Dr. Carmela Cuomo). Lead story by T. A. Dowd, NewsNet: 'Gang Warfare Abates' "
            "(violence down 26 percent overnight, 71 percent on the week; Carol Lake calls Elven Fire a "
            "hoax) or 'City Under Martial Law' (sixth day, 118 dead, Captain Colton's APC, Governor Schultz to "
            "ask President Alan Adams for federal help)."
        ),
    },
    "Salish-Shidhe Council": {
        "notes_append": "Elven Fire: gang violence spreads into immediately neighboring Salish-Shidhe territory (KTXX). Shim Bright files a flight plan into Salish-Shidhe land with no destination and claims Salish-Shidhe diplomatic immunity on forged papers, saying 'the embassy is clearing it up with the Seattle FAA' -- a lie the helifield officials swallow at gunpoint.",
    },
    "University of Seattle": {
        "notes_append": "Elven Fire (May 20 2053 news, which calls it 'Seattle University' -- possibly the same institution): a twelve-member research expedition to Southeast Asia under Dr. Walter Hunt came home with four survivors after running afoul of a Vietnamese bandit king; marine biologist Dr. Carmela Cuomo examines the giant Puget Sound geoduck.",
    },
}

LOC_UPDATES = {
    "Fort Lewis": {
        "notes_append": "Elven Fire: home of the Metroplex Guard. The Guard musters here when Governor Schultz suspends leaves; the UCAS carrier Koontz ferries aircraft back and forth from Puget Sound; the British Royal Family conducts a formal inspection on May 19, 2053 ('casualties were light').",
    },
    "Matchstick's": {
        "notes_append": "Elven Fire (May 20 2053 news): Ellen Donnelly, a woman with shadow-market and syndicate ties who was not a member of the private club, was killed at 11:45 p.m. when her Saab Dynamit exploded on ignition outside; Lone Star calls it a professional assassination with no leads.",
    },
    "The Kingdome": {
        "notes_append": "Elven Fire (May 2053 news): Mariners owner Jerome Einsdorff wants changes in Kingdome management and is denying rumors the team will move to Oakland, CFS.",
    },
    "The Barrens (Seattle)": {
        "notes_append": "Elven Fire: Redmond -- the Bargain Basement section (half-squatted tenements with dead elevators; Half-Ace's flat 17J; Crimson Crush killings out front); Father Roe's youth shelter. Weapons are 'all over the streets and practically free' during the gang war, with a discount if you are gunning for the Ancients.",
    },
}

NPC_UPDATES = {
    "Governor Schultz": {
        "notes_append": (
            "Elven Fire (May 2053): asked by Lone Star's William Loudon to mobilize the Metroplex Guard "
            "against the gang war. Suspends all Guard leaves and orders every member to Fort Lewis at the "
            "24-hour mark (Handout 8), orders the Guard into the streets at 36 hours (Handout 9), and under "
            "martial law schedules a news conference to request federal assistance from UCAS President Alan "
            "Adams. Her Office on Metahuman Affairs consults Shim Bright, the Tir agent behind Elven Fire."
        ),
    },
    "Saint John": {
        "notes_append": "Elven Fire: not the same man as 'St. John', the runner wannabe shot with six yakuza at the Witches' Circle in Loveland (separate row). Ellen Donnelly was car-bombed outside Matchstick's on May 19, 2053 -- the doorman with the photographic memory would know whether she had ever been inside.",
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
Elven Fire maps no Matrix systems ("this adventure requires almost no decking"); nothing to build.
Systems the book names, for a GM who wants to improvise them:

- **Koren Thark's electronic mailbox** -- a Downtown Seattle LTG and box number on his datachip, where
  the runners drop reports every six hours and he drops Lone Star data pulls (1D6 hours per request).
- **Lone Star Data Services** -- restricted synopses on the Ancients, Elven Fire, Lucinda Tangier and
  St. John (Handouts 4-7). Lucinda's record has been deleted "by illegal system penetration".
- **Redmond Seoulpa Ring numbers account** -- a secret Matrix account (Leather Devils backing) that
  Elven Fire's unnamed decker emptied, leaving a dumb frame of a flaming elf in Ancients colors.
- **NewsNet's computer** -- penetrated to plant the "purify the city" message before The Jump House.
- **Public databases** -- Shim Bright's file is PR hype; general legwork by Matrix search takes 2D6
  hours against Etiquette (Matrix) or Intelligence, no Hacking Pool.
- **Non-Matrix security**: the Whispering Nights' Gateway III scanner (Rating 6 weapons / 3 cyberware;
  bioware invisible), the Rating 3 wireless bug in Simon Johnson's office, the helifield's local radar,
  Lone Star PANICBUTTONs at the Witches' Circle.
"""

NOT_BUILT = """
- **The High Prince of Tir Tairngire** (never named in this book) and **the opposition cabal** -- on the
  Tir Tairngire row. **Bright's two Tir bodyguards** (one with a sniper rifle, no stats), **the two
  helifield officials**, **the Commuter pilot**, **the Meat Junkie leader** (massive ork, twin Uzis,
  crippled by Kylisearn), **the Tigers' adept squad leader**, **the four hired elven thugs**, **the six
  drive-by punks**, **the ork sniper**, **the Loveland cafe waitress**, **Lone Star's snitch** with the
  headware camera -- on the org / location rows.
- **Sect of the Blooded Moon** (Bright's initiatory group), **Way of the Whispering Nights** (Midori's),
  **Tigers of the Neon Jungle** (Ejima's) -- magical groups named only.
- **Custer Military Academy** (Wasp's jibe), **"Death or Taxes"**, **"Chet Chit-Chat"**, **"Nerps --
  California Style!"** -- trideo.
- News names: **Spirit Air**, **the British Royal Family**, **Peggy's Playful Porkers**, **the Seattle
  Mariners**, **Oakland, California Free State**, **UCAS President Alan Adams**, **Roger Browning and
  Wendy Tancredi**, **Evergreen College**, **the FAA (Seattle)**, **Walter G. Smith, P. Daza, T. Gallagher,
  T. A. Dowd** (bylines) -- on the News-Intelligencer row.
- Places: **Highland and Terry** (the Ancients meet point near Lake Union), **Westlake border**,
  **Denny Park**, **Shadow Lake (Snohomish)**, **the International District power station**, **Bob's**
  is built; **St. John's apartment** (ransacked, sealed) is not.
- **The UCAS carrier Koontz** and the **Federated Boeing Commuter** -- vehicles, not entities.
- **DMZ integration** (pp.58-60) and the **Gateway III rules** (p.28) -- rules reprints.
"""

PLAY_NOTES = """
- The clock is the adventure: 48 hours to the Guard (flexible, secretly) and 48 hours from the
  yakuza. Drop Handouts 8 and 9 at 24 and 36 hours; let street rumor and KTXX do the pressure.
- Drive-By is a tone poem, not a fight -- show the bystanders bleeding. If the runners die to six
  punks, "Go directly to Character Generation."
- Thark believes every word; play him straight and let Bright's misinformation arrive through him.
  The runner who half-recognizes Dumont controls the pace: the sooner "mercenary" comes up, the
  faster the book goes (Intelligence test only when a real reference triggers it).
- Three courts, three etiquettes: the Ancients (Green Lucifer hostile, Sting listening), the
  Whispering Nights (weapons, shoes, an hour of tea; two slips and you are on the drek list), and
  Owen T. Adler (a joke with 50,000 nuyen in it).
- Green Lucifer is the hidden knife: he wants to intercept everything the runners learn about him
  and will remove them if they learn too much. Never let him admit the coup or Wasp unless the
  runners bring "incredibly damning" proof. Bright's dying line at the helifield is the reveal.
- Interdiction is a kill-box (hostages, an astral mage with two Force 5 elementals); watch the
  numbers. Maze Mind is horror -- water, rats, chalk, and a man who can be talked down into a lost
  boy if the runner who knew him spends every action on it.
- Karma (p.61): categories are dealing with the yakuza, defeating Dumont, defeating Bright and
  down-scaling the gang war (values lost in the scan; award in that order of weight), plus 2 each
  for surviving.
- Loose ends: the Ancients as friends and a Tir list of meddlers; the yakuza's respect or their
  drek list; Lucinda (rich, Awakened, grateful or captive); Bright's masters and whoever replaces
  him; Elven Fire's decker; who tipped the Ragers; what Baron and Green Lucifer were discussing;
  Ellen Donnelly's car bomb; and, if the Guard rolls, a city under martial law for the next arc.
"""
