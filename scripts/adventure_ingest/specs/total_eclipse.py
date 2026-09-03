# Total Eclipse (FASA 7308, 1991) -- campaign order #12. Redmond Barrens / Bellevue / Salish-Shidhe
# forest, November 2051 (both news handouts are the Seattle News-Intelligencer Update-Net of Tuesday
# November 14, 2051). The book's own dating is a mess: the intro says "approximately 2050", the
# prologue opens on "a hot summer day" and closes the same scene under "a gentle spring sun". The
# handout date is used; the season is ignored.
# Other editing inconsistencies noted in the affected rows: Whispering Wind carries a "Light Fire 70"
# on p.16 but a Ceska vz/120 in her cast entry; her flat is "near the edge of the Barrens" (p.9) and
# "in the Bellevue District" (p.15); the prologue calls Eclipse an "insect shaman" while the cast page
# gives the Spider totem; "Bambi" is "Barbi" once on p.9; the Nemesis attribute block and the Karma
# award numbers are unreadable in the OCR; the escort fee (25,000 nuyen) never says per runner or
# per team. Bambi's brothers are only ever "Josh" and "Hoss" -- the surname Bloom is inferred from the
# family store.
# Source text: docs/Adventures/text/Shadowrun 1e - Total Eclipse {FASA7308}.txt (56 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "Total Eclipse"
ORDER = 12
SOURCE = "Shadowrun 1e - Total Eclipse {FASA7308}.pdf, pp. 4-55"
YEAR = "2051 (November)"

SYNOPSIS = """
A fixer sends the runners to the **Pink Pitbull**, a pink-on-pink strip joint in the Redmond Barrens,
to meet a tall middle-aged Amerindian in a corp suit who says he represents an anonymous
entertainment corp. He is really **Eclipse**, a retired top-tier runner turned Spider shaman, and the
elf razorboy at the bar is his bodyguard **Dusk**. The story: the hot new band **The Elementals**
walked out on their contract with the only copy of their first chip and are about to release it
themselves; "persuade" all four to come to his condo by midnight, quietly, unharmed, and bring any
copies of the master. 5,000 nuyen per runner per musician, 5,000 more each for the album, and a
Narcojet pistol apiece as a gift.

The truth: five months ago the ancient free spirit **Twilight** -- a huge spider, freed from an
Australian prison-cave in the Sam Verner affair -- crawled back to the place of power in Salish-Shidhe
land where it was first summoned, dying, and found Eclipse's mind. They cut an unbreakable covenant:
heal me and I serve you. Eclipse found nothing for five months until he heard the band's demo
"Healing the Spirit" in the Pitbull and recognized a bastardized rejuvenation ritual. Singer
**Whispering Wind** wrote it from a crackpot pre-Awakening occult book by **Professor Erik Vonen** --
and from racial memory she does not know she carries.

The runners tail the four from their studio at the **Redmond Business Nest**: Whispering Wind to her
high-security flat in Bellevue (skylight ambush, two of her dead father's mercenary friends),
guitarist **Wildfire** to his gang-neutral trid arcade **Wildfire's Fantasy Arcade** (twin troll
bouncers, a dwarf with a laser axe, six volunteer go-gangers), troll drummer **Bambi** to **Bloom's
Troll Emporium** (monofilament wire across the alley, his brothers Josh and Hoss, four wolves, a
Panther cannon on his Viking), and bassist **Coyote** to the Amerindian squatter camp in the haunted
park of the ruined **Redmond Grand Hotel** (Snake shaman, Park spirit, bows from the trees). Each
carries one of four encoded chips that only work together.

At Eclipse's penthouse the band comes out of the study smiling in new necklaces -- Control Thoughts
spell locks -- and the coarse, hairy trideo director **Lupus** (a wolf shapeshifter paying off a
favor) is introduced. Job two: escort everyone a day into Salish-Shidhe territory to shoot a music
trideo without a license, 25,000 nuyen, leaving now. Refuse, and Eclipse sends the vampire mage
assassin **Nemesis** after them; his pocket secretary leads back to a dark building full of traps
(electrified stairs, a free-falling elevator, a salamander in the shafts, a naga at the teepee) and
an old parchment map of the continent. Either way the trail ends in a moonlit clearing of stone
slabs where a banshee and her ghouls must be cleared first, The Elementals play an hour before dawn,
fog and light gather, and on the sixth combat turn a three-meter spider steps out at full strength
to eat every witness.
"""

TIMELINE = """
- **Centuries ago** -- four Australian outback shamans trick Twilight into a place of power and seal
  it in a cave with other evil spirits. **Five months ago** -- the wards break (Find Your Own Truth);
  Twilight limps back to its Salish-Shidhe place of power and makes its covenant with Eclipse.
- **A few days ago** -- Eclipse hears "Healing the Spirit" at the Pink Pitbull, buys the chip off the
  DJ for 100 nuyen, then spends a week bribing his old contacts for the band's files and pictures.
- **Day 1, late afternoon** -- the meet at the Pink Pitbull; the band leaves the studio minutes after
  the runners arrive; the four snatches; **midnight** delivery at the penthouse and the escort offer.
  The party leaves at once.
- **Day 1-2** -- the border crossing from the outer Redmond Barrens, a Salish-Shidhe patrol, ghouls
  fleeing the clearing; Eclipse's party butchers a patrol on its way in.
- **Day 2, an hour before dawn** -- the banshee cleared, the band plays; Twilight emerges at combat
  turn 3 and is whole at turn 6. Refusers meet Nemesis on Day 1 night, break into the dark building,
  and arrive at the clearing as the song peaks.
- **Tuesday November 14, 2051** -- the newsnet: "Elemental Magic" (Through the Lightning released) or
  "Death of the Elementals" (four bodies just across the border, vampire or banshee suspected).
"""

ORGS = [
    {
        "name": "The Elementals",
        "org_type": "rock band",
        "tier": 1,
        "headquarters": "The Elementals Recording Company, Redmond Business Nest, Redmond",
        "summary": "Seattle's hottest independent band -- Whispering Wind's 'syntho-magic' songs carry fragments of a real spirit-healing ritual",
        "description": (
            "A four-piece that came up through Seattle's hot clubs to a sold-out Underworld 93 and then "
            "refused to sign with a music corp: lead vocalist and songwriter Whispering Wind (human), "
            "guitarist Wildfire (elf), bassist Coyote (Amerindian, ex-Ute military) and drummer Bambi "
            "(troll). Club money bought a studio in the Redmond Business Nest and second-hand "
            "computerized sound gear; the demo track 'Healing the Spirit' went out to clubs all over "
            "Seattle while the band finished its first chip, 'Through the Lightning'. Street word: the "
            "corps call them too radical and not that popular, and wonder how the music corps feel "
            "about a self-release. Every gang in the Redmond Barrens waves at Bambi."
        ),
        "leadership": [
            {"name": "Whispering Wind", "title": "Lead vocalist, songwriter", "notes": "Writes from Vonen's book and racial memory; her songs hold power."},
            {"name": "Wildfire", "title": "Guitarist", "notes": "Owns Wildfire's Fantasy Arcade."},
            {"name": "Coyote", "title": "Bass / key-guitar", "notes": "Ute Nation military veteran."},
            {"name": "Bambi", "title": "Drummer", "notes": "Night watchman at the family store, Bloom's Troll Emporium."},
        ],
        "notes": (
            "The master exists only as four encoded chips, one carried by each member; all four must be "
            "recombined. All four: Instrumental Music 6, Musical Composition 4, Etiquette (Street) 5, "
            "synth-leather jacket, survival knife, throwing knife, datajack and synthesizer link (except "
            "Bambi). Once Eclipse's Control Thoughts spell-lock necklaces go on they obey any order that "
            "does not fight their basic personalities; the locks break with Eclipse's death. The song "
            "works with a third-rate stand-in if a member dies -- just slower. Legwork TN 4 (Rocker, "
            "Gang Member, Media Producer, Club Owner, Fan, Reporter). Success ending: 'Through the "
            "Lightning' is the number-one club request in Seattle. Failure ending: four bodies in a "
            "Salish-Shidhe clearing. Avengers if a member dies: merc friends of Whispering Wind's "
            "father, the go-gangs for Wildfire, the Bloom brothers for Bambi, the band for Coyote."
        ),
    },
    {
        "name": "Red Death",
        "org_type": "gang",
        "tier": 1,
        "headquarters": "Puyallup District",
        "summary": "Troll gang from Puyallup that trashed the Kingdome in November 2051 (news handout)",
        "description": (
            "A troll street gang of the Puyallup District. In the week before November 14, 2051 it got "
            "into the Kingdome and did enough damage to close the stadium for repairs until about May 1; "
            "Kingdome management would say nothing more."
        ),
        "notes": "Known only from the Total Eclipse news handouts. Ticket-holders were told to chase promoters, not dome management, for refunds -- a lot of angry fans and a gang that just made a name.",
    },
    {
        "name": "Road Hogs",
        "org_type": "urban brawl team",
        "tier": 1,
        "headquarters": "Duster's Drag Strip & Arena",
        "summary": "The first all-troll Urban Brawl biker gang, debuting against the reformed Ratchet Squad (news handout)",
        "description": (
            "Billed in the November 2051 sports pages as the first all-troll Urban Brawl biker gang, "
            "scheduled to appear at Duster's Drag Strip & Arena the Saturday after November 14 against "
            "the newly reformed Ratchet Squad."
        ),
        "notes": "News-handout texture; useful as a crowd to put the runners in, or as Bloom's Troll Emporium customers (the Leisure section orders troll-modified bikes).",
    },
]

LOCATIONS = [
    {
        "name": "Pink Pitbull",
        "location_type": "bar",
        "district": "Redmond Barrens",
        "security_level": "No Security / Barrens",
        "summary": "Little-known pink-neon strip joint where Eclipse drinks and holds the meet; every metatype dances here",
        "description": (
            "A crumbling building with a faded pink facade and a pink neon sign; a cheap eight-color "
            "holoprojector floats a writhing naked female elf over the door. Inside is late neo-tacky in "
            "one revolting shade of pink: a bar at one end, a stage at the other, small tables and chairs "
            "on wall-to-wall pink shag, a few wall booths. Dancers of every metatype -- an elf, a troll, a "
            "dwarf -- a bouncer, and a DJ booth. Eclipse's regular seat is directly in front of the stage."
        ),
        "notes": (
            "Meet site (Musical Extractions). Etiquette (Street) 5 with staff: 1-2 successes, he is almost "
            "a regular, usually in a hide suit and a drekky hat; 3, a retired hot runner, crazy, thing for "
            "spiders, tarantula on the hat; 4, name's Eclipse, had a fit over a song a couple of days ago, "
            "roughed up the DJ and took the chip. The elf DJ quit and moved on; nobody remembers the song. "
            "Signature drink: the Fraggin' Dragon. The dancers hate Eclipse's stare and his spider -- one "
            "fainted when it brushed her."
        ),
    },
    {
        "name": "Eclipse's Apartment Building",
        "location_type": "penthouse",
        "district": "Redmond Barrens (a few blocks from the Pink Pitbull)",
        "security_level": "No Security / Barrens",
        "summary": "Ten-storey block Eclipse owns for its rooftop garden and teepee medicine lodge; empty floors, lethal traps, a naga and a salamander",
        "description": (
            "An old ten-storey apartment building among condemned neighbors, in noticeably better shape "
            "than the street around it. Heavy security door with a camera, a small lobby, two elevators "
            "(one an open, empty shaft), a print-sensor maglock on the working car. Every floor below "
            "the top holds four empty flats unoccupied for years. The penthouse is luxurious and "
            "tasteful: a study with his computer, kitchen, bathroom, bedroom, den, and sliding "
            "plexiglass doors onto a roof covered by an overgrown garden with a large, beautifully "
            "decorated teepee in the middle -- his medicine lodge (rating 7). Eclipse bought the place "
            "cheap for that roof."
        ),
        "notes": (
            "Delivery point at midnight; the 'condo' where the band gets its necklaces. When Eclipse "
            "leaves town (Nobody Home, pp.30-32) the building goes dark: home computer physically "
            "unhooked from the Matrix (unlisted LTG; the only datajack is in the penthouse); exterior "
            "walls and doors Barrier 10 (explosives trip alarms, Lone Star in 30 minutes); every other "
            "exterior door bricked up; Rating 7 maglock on the front door (Electronics 7 / Computer B/R "
            "7; a botch is a 5L3 Stun jolt, +4 TN for five turns, and a silent alarm); Rating 7 maglock on "
            "the elevator (Barrier 6 -- blowing it wrecks the car); a finessed elevator climbs to the "
            "eighth floor then free-falls (8S4, impact armor only, no Dodge); maintenance ladders in both "
            "shafts with motion sensors that open trap doors at the fifth floor onto an alcove holding a "
            "conjured salamander (B5 Q6x3 S2 W4, Reaction 10/20, 3M4; Engulf, Flame Aura, Flame "
            "Projection, Guard; Vulnerability water; Moderate damage means Willpower 6 or fall, 5S3); "
            "metal stairs with one electrified step on each of the first four flights (5L3 Stun) and "
            "motion-triggered flash-paks on the fifth landing (Willpower 6; failures go over the rail); "
            "Rating 10 maglock into the penthouse. The pet naga (B5 S6 W4, 5M2 venom 8S2; Guard, Magical "
            "Guard; casts Sleep and Chaotic World intelligently) has the run of the garden and attacks "
            "anyone but Eclipse at the teepee; the lodge interior cannot be assensed. Clues: the datastore "
            "log (see Matrix systems) and an old parchment map -- the first record of the continent's "
            "landmarks -- which, laid against a current NAN map, points to the clearing. Making trouble "
            "here at the midnight meet brings half a dozen burly street toughs from adjoining rooms."
        ),
    },
    {
        "name": "Redmond Center Mall",
        "location_type": "mall",
        "district": "Redmond (near the Bellevue edge)",
        "security_level": "Patrolled / Commercial",
        "summary": "One of the few prosperous corners of Redmond: 200+ stores in chrome and neon, thick with Lone Star",
        "description": (
            "A massive structure of chrome, neon tubing, steel and plexiglass housing more than two "
            "hundred stores and businesses -- one of the few prosperous areas in the Redmond District, "
            "near the edge of Bellevue. A small strip mall faces it across the street: a Trid Games "
            "Arcade, a Stuffer Shack, a Busy Bee Soyburger and the Moon Blossom Restaurant, wrapped "
            "around the Redmond Business Nest office building."
        ),
        "notes": (
            "Civilian and Lone Star traffic make any move here professional suicide; loitering outside "
            "the Business Nest gets the team rousted, and visible heavy hardware gets them hauled in "
            "(Street Cop stats). Hordes of officers answer any commotion. Good cover for watching the "
            "band's bikes: a Yamaha Rapier each for Coyote and Wildfire, an Aurora racing bike for "
            "Whispering Wind, a troll-modified Honda Viking for Bambi, parked out front."
        ),
    },
    {
        "name": "Redmond Business Nest",
        "location_type": "office building",
        "district": "Redmond (across from Redmond Center Mall)",
        "security_level": "Patrolled / Commercial",
        "summary": "Five-storey remodeled office block: Sam Sprawl's Real Estate, Chachi's Hair Styles, a Federated Salish S&L branch and The Elementals' studio",
        "description": (
            "A remodeled five-storey office building across the street from the mall. The ground floor "
            "(map p.14) holds Sam Sprawl's Real Estate (reception with couch and glossy magazines, "
            "secretary Lola, an inner office in mid-American bland), Chachi's Hair Styles (one long room "
            "of chairs and mirrors and high-tech styling machines, appointments only, no walk-ins), a "
            "small branch of Federated Salish Savings and Loan (ten computerized teller booths, a "
            "technician-teller's office, a walk-in vault of forty safe-deposit boxes, a guard at the "
            "vault door) and The Elementals Recording Company."
        ),
        "notes": (
            "After hours the main door and each tenant's door are Rating 7 maglocks and a guard sleeps "
            "in the bank. The real-estate and salon computers hold nothing but listings and hairstyles. "
            "The bank technician doubles as teller and junior exec (Negotiation 4, Etiquette (Corporate) "
            "4). Chachi and his five stylists are all ex-squatters (Hair Stylist 6 / 4)."
        ),
    },
    {
        "name": "The Elementals Recording Company",
        "location_type": "recording studio",
        "district": "Redmond (Redmond Business Nest, ground floor)",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "The Elementals",
        "summary": "The band's not-yet-open studio and chip line; no copy of the master here, but the computer holds their home addresses",
        "description": (
            "Most of the Business Nest's ground floor: a bare, rarely used reception, a large unused "
            "business office, a small sound-engineering booth beside the recording studio -- everything "
            "needed to cut a chip, all obviously second-hand but in good condition -- and a back room "
            "of machinery, a computerized assembly line that makes and packages audiochips. Not yet open "
            "to the public; typical Rating 5 maglock."
        ),
        "notes": (
            "A careful search turns up no copy of the multitrack master -- the band, afraid a music "
            "corp would steal the songs, split it across four encoded chips they carry. Debugging: the "
            "studio computer (Green-6, one Barrier 7 IC) lists the members' home addresses for teams "
            "that blow the tail."
        ),
    },
    {
        "name": "Moon Blossom Restaurant",
        "location_type": "restaurant",
        "district": "Redmond (strip mall by Redmond Center Mall)",
        "security_level": "Patrolled / Commercial",
        "summary": "Authentic Awakened Thai cuisine across the street from the mall; a place to sit and watch the Business Nest",
        "description": "A restaurant of 'authentic Awakened Thai cuisine' in the small strip mall wrapped around the Redmond Business Nest, sharing the frontage with a Trid Games Arcade, a Stuffer Shack and a Busy Bee Soyburger.",
        "notes": "Only ever a name and a menu in the book; the natural stakeout table for the studio's front door.",
    },
    {
        "name": "Whispering Wind's Apartment",
        "location_type": "residential community",
        "district": "Bellevue District (bordering Redmond)",
        "security_level": "Patrolled / Commercial",
        "summary": "One-storey flat in a development of identical boxes, high-tech alarms, a rope ladder to the skylight -- and Lone Star everywhere",
        "description": (
            "A development of small one-storey buildings that all look the same, in Bellevue where it "
            "borders Redmond (p.9 calls it an 'ultrasecurity flat near the edge of the Barrens'). Medium "
            "Residence layout (Sprawl Sites p.33); the bedroom has a skylight onto the roof with a rope "
            "ladder under it, and Vonen's book on the dresser."
        ),
        "notes": (
            "Windows and door maglock are high-tech: Electronics (5) to bypass -- a botch rings the "
            "alarms and Lone Star (Chrysler-Nissan Patrol-1, backup called on arrival) rolls in 1-6 "
            "minutes; a plain failure allows a retry at TN 9. Unaware, she is washing her hair (Stealth 4 "
            "each or someone knocks something over; then she is behind the bed with a gun and the chip). "
            "Warned minutes ahead, she waits on the roof with the skylight open, lobs a concussion "
            "grenade and runs. Warned well ahead, two mercenaries who owed her father (B5 Q4 S5, Firearms "
            "6, Ingram Valiant LMG, Ares Predator, partial heavy armor 8/6, low-light eyes) are up there "
            "with her and they all jump down to finish it; everyone scatters when Lone Star arrives. "
            "Intelligence (4) finds the book; Conjuring (7) / Magic Theory (5) recalls Vonen; a magician "
            "who reads it (Conjuring 10 / Magic Theory 15, secret) sees fragments of true rituals nobody "
            "without her lineage can rebuild."
        ),
    },
    {
        "name": "Wildfire's Fantasy Arcade",
        "location_type": "trid arcade",
        "district": "Redmond Barrens (thrill-gang heartland)",
        "security_level": "No Security / Barrens",
        "summary": "Wildfire's two-storey brick trid/simsense arcade, the one neutral ground every go-gang honors; twin troll bouncers and a dwarf with a laser axe",
        "description": (
            "A run-down two-storey brick building surrounded by ruins in the worst of the Redmond "
            "Barrens, a flashing neon sign out front, a long line of bikes locked to a plexisteel rail "
            "sunk in the sidewalk and gang-painted cars parked around it -- logos from every gang and no "
            "mayhem, because this is neutral territory. Table-top trid games (Street Samurai Showdown, "
            "Mage Fire, Dragon Wars, Corp Wars, Nuked Pre-Pubescent Samurai Dragons, Panzer Hunt, "
            "Unicorn Nights) played by joystick or datajack, simsense recliners rumored as addictive as "
            "BTL (Super Mareno Brothers LXXX, SINless City 2050), a token machine at the back, a unisex "
            "bathroom under the narrow stairs, a storage room that is mostly electronics repair shop "
            "with a handle-less steel door to the back of the building, and upstairs Wildfire's spartan "
            "office and sleeping quarters over a balcony (map p.18)."
        ),
        "notes": (
            "The only gang that ever broke the no-violence rule had its clubhouse visited by a "
            "high-explosive missile; Wildfire mediates rival gang leaders in the back room. Staff: Micro "
            "(dwarf tech), Thud and Blunder (twin trolls). Unaware, Wildfire is upstairs over the "
            "accounts, Micro and Thud playing cards in the back, Blunder on the floor giving strangers "
            "his stare: Stealth (3) up the stairs to surprise him, then a diversion or a lie to get him "
            "out (no windows up there). Any fight makes the customers assume a gang broke neutrality and "
            "they fight each other; anyone in colors gets shot at twice a round. Tailed home, he posts "
            "his staff on the stairs and yells 'Cops! It's a raid!' -- a stampede for the doors while "
            "his people flank the team. Forewarned for real, he asks the gangs to leave; six volunteers "
            "from six gangs (B5 Q6 S5, hand razors, Tiffani Self-Defenders, Rapiers) pretend to play, "
            "the trolls hide shock gloves in their pockets, Micro's axe leans on a table, Wildfire's "
            "katana hides behind a game, and Whispering Wind may be on the balcony. He fights until "
            "knocked out; chip in his jacket. A Crimson Crush Americar is parked outside."
        ),
    },
    {
        "name": "Bloom's Troll Emporium",
        "location_type": "shop",
        "district": "Redmond Barrens (dead-end street)",
        "security_level": "No Security / Barrens",
        "summary": "The Bloom family's troll department store; Bambi's flat at the back, brothers Josh and Hoss, four wolves, and a monofilament wire across the alley",
        "description": (
            "A large brick store at the end of a dead-end street with a narrow alley on the right leading "
            "to a ramp and loading dock. Founded by the brothers' father after all three goblinized, now "
            "run by a hired manager. Sections (map p.23): checkouts with credstick slots; food ('ethnic' "
            "troll dishes better left unexamined, candies, a stuffer brand, towers of Mama Beani's Canned "
            "Troll Fritters); electronics with troll-sized keys; leisure (hunting and camping gear, "
            "weapons, toys, troll-modified vehicles to order, a reinforced Honda Viking on display); "
            "clothing for most of the floor; furniture; a stockroom; and Bambi's magkeyed one-room flat "
            "-- drums in the corner, trid center, sofa bed, kitchenette, walk-in closet."
        ),
        "notes": (
            "Locked tight at night: macroplast sheets (Barrier 22) on a time lock over the front and "
            "windows, a cargo door (Barrier 18) with no outside maglock, opened by a data burst at "
            "hidden sensors -- Electronics B/R (7) or Computer (7); a botch alarms Bambi, a nearby Lone "
            "Star station (30 minutes) and the brothers' homes (10 minutes); Demolitions (5) to blast a "
            "hole. Four wolves (B5 Q5x4 S4, obedient only to the brothers) patrol the aisles; unaware, "
            "Bambi is in his flat with the band chip blasting through headphones and comes running with "
            "his axe. Tailed home, he signals by helmet comm and leads the runners into the alley "
            "where his brothers have strung monofilament at rider head height (Perception 8 to see it; "
            "6S4 plus +1/+5/+10 for speed; Vehicle skill TN 6 to lean under it) with Josh and Hoss on "
            "the roof and Bambi's Viking spun round with its Panther gun port open. Forewarned inside: "
            "Josh poses as a hunting-clothes mannequin in Leisure with a loaded net gun, Hoss crouches "
            "behind the fritters, Bambi behind the electronics counter. Five friendly go-gangers join "
            "any fight on Bambi's side two turns in."
        ),
    },
    {
        "name": "Redmond Grand Hotel",
        "location_type": "squatter camp",
        "district": "Redmond Barrens (outer edge, toward the NAN boundary)",
        "security_level": "No Security / Barrens",
        "summary": "Crumbling pre-Crash luxury hotel on a foliage-choked hill; 'haunted' park of mechanical animals hiding an Amerindian squatter camp with a Snake shaman",
        "description": (
            "One of Seattle's fanciest hotels before the Crash of '29, famous for its manicured park, now "
            "a large crumbling building on a hill where the ruins thin out and the plants take over. The "
            "park had no wildlife because the land was said to be laced with chemicals that let plants "
            "grow and killed animals; released animals died or were eaten by the poor, so the eccentric "
            "owner -- a big shareholder in a theme-park entertainment corp -- had the corp build small "
            "mechanical animals for the underbrush. Street talk says the park is haunted and the "
            "animals still move. In the center of the grounds a dirt road reaches a field with eight "
            "teepees around a fire pit: a transient tent city of ten Amerindian squatters and a shaman."
        ),
        "notes": (
            "The toxic-land rumor was invented by a corporation that wanted the property; it poisoned "
            "plants and animals itself, the owner still refused, and now that he is dead the corp is "
            "years from clear title in litigation (corp unnamed -- a hook). Coyote lived here when he "
            "first came to Seattle and brings food and supplies once a week, staying the night; the camp "
            "sits up past midnight. A hidden scout on the road (Stealth vs the team, +2 for his "
            "low-light goggles; vehicles on the road are always spotted). Ambush: door flaps closed, a "
            "stuffed sleeping bag by the smoking fire beside Coyote's Rapier, Coyote and five squatters "
            "hidden in the teepees under a Force 6 Park (Field) spirit's Concealment (a wizened old "
            "oriental man in gardening clothes; Accident, Concealment, Guard, Search TN 4, Immunity to "
            "normal weapons vs fire combat), the other five and the shaman in the trees (Perception 12). "
            "Squatters: all attributes 5, Armed Combat 6, Projectile Weapons 6, Stealth 6, compound bows "
            "(6M2), knives, low-light goggles, a smoke grenade. Shaman: B3 Q3 S3 C5 I4 W6 M6, Snake totem, "
            "Conjuring 6, Sorcery 5, Power Focus +2, Illusion focus +2, Field spirit focus +2; Detect "
            "Enemies 4, Heal Deadly Wounds 4, Overstimulation 4. If a squatter dies Coyote surrenders "
            "and calls off the bows. Chip in the pouch on his neck thong."
        ),
    },
    {
        "name": "Twilight's Clearing (Salish-Shidhe place of power)",
        "location_type": "place of power",
        "city": "Salish-Shidhe Council",
        "district": "Forest about a day's travel past the outer Redmond Barrens border",
        "security_level": "Low Security",
        "summary": "Moonlit clearing of scattered stone slabs sacred to the local tribes; a banshee and her ghouls, then the rejuvenation concert",
        "description": (
            "A large clearing a day's travel from the Seattle border, reached through the least-patrolled "
            "stretch of the line beyond the outer Redmond Barrens -- but the woods around it are sacred "
            "to the tribes and patrolled more than Eclipse's sources knew. Large stone slabs lie "
            "scattered at random across the ground with a big flat one in the center (map p.39). It is a "
            "powerful natural magic focus, the place Twilight was first summoned from and the spot its "
            "old parchment map marks. A banshee (a blurred female elf) has sensed the power and lairs "
            "here with ten ghouls from a nearby Indian burial site enchanted to die for her."
        ),
        "notes": (
            "House Cleaning: the team has surprise; ghouls rush chaotically (B7 Q5x4 S6, claws 6L2, "
            "blind, sunlight moderate), the banshee grapples a spellcaster and drains Essence (B3 Q4x5 "
            "S3, Fear, Mist Form, Regeneration; sunlight severe, wood and silver); she fights to the "
            "death, survivors flee. Five more ghouls are met in the forest, driven out by Eclipse's "
            "party. Shadow Concert: battery floodlights and tripod trid recorders round the clearing, "
            "the band on the central slab, playing about an hour before dawn; low fog, lights in the fog, "
            "rising wind, an expanding spot of light. Five combat turns to stop the song; Twilight begins "
            "to emerge at the start of turn 3, is fully manifest in Great Form at the start of turn 6, and "
            "takes no damage before then. Eclipse attacks the moment the band is interfered with. "
            "Retreat to Seattle is unpleasant but uneventful; Eclipse's death breaks the spell locks. GM "
            "rescue: a Salish-Shidhe patrol with shamans arrives like the cavalry. Success news calls the "
            "spot 'a clearing rumored to be a gathering spot for Awakened creatures'."
        ),
    },
    {
        "name": "Duster's Drag Strip & Arena",
        "location_type": "arena",
        "security_level": "Patrolled / Commercial",
        "summary": "Drag strip and Urban Brawl arena hosting the all-troll Road Hogs vs the Ratchet Squad (news handout)",
        "description": "A drag strip and arena named in the November 14, 2051 sports pages as the venue for the Road Hogs, the first all-troll Urban Brawl biker gang, against the newly reformed Ratchet Squad the following Saturday.",
        "notes": "Name only; district not given. With the Kingdome closed until May it is where Seattle's brawl crowd goes.",
    },
]

NPCS = [
    {
        "name": "Eclipse",
        "role": "'Face of the Eclipse' -- retired top runner turned Spider shaman, bound by covenant to the dying free spirit Twilight; the Mr. Johnson",
        "archetype": "Shaman",
        "title": "Spider shaman; retired shadowrunner; owner of a Barrens apartment block",
        "race": "Human",
        "gender": "Male",
        "nationality": "Amerindian",
        "connection": 4,
        "description": (
            "Tall and lean, middle-aged, dark skin wrinkled by sun and wind, hawk features, black eyes "
            "that flash, long black hair shot with silver worn loose. Off duty: a fringed-buckskin "
            "leisure suit and moccasins beaded with a chaos of spiders from house spider to black widow, "
            "and a black silk top hat with eagle feathers in the band and a live tarantula riding on "
            "top that rides along when he leans over the dancers. At the meet: a typical corp suit and "
            "no hat. Slightly mad, muttering to himself; extremely intelligent and perceptive; a nasty "
            "temper the Barrens has learned to walk around. Astral form: a glowing humanoid with a "
            "spider's head. 'Take the deal, or I'll take your miserable soul and give it to my pet "
            "spider to play with.'"
        ),
        "background": (
            "Five years ago he stood near the top of the shadow hierarchy after a string of "
            "high-risk, high-paying runs, then took one big score and retired into shadow deals and a "
            "few legitimate businesses -- comfortable, and empty. On that last run he fell through the "
            "rotted floor of a squat into a room full of spiders with a broken leg; they only stared, and "
            "skittered off when his friends came. He followed the call to the Spider totem. Five months "
            "ago the spirit Twilight touched his mind from Salish-Shidhe land and they swore the ancient "
            "covenant that cannot be broken: he finds the rite to heal it, it serves him. Five months of "
            "'bloody drek' later he heard the Elementals' demo in the Pink Pitbull. He expects the "
            "bargain to seal his fate; he may be right."
        ),
        "notes": (
            "Offers 5,000 per runner per musician, +5,000 each for the album, Narcojets as a gift; "
            "Negotiation opposed vs Willpower, +/-1,000 per success. Pays at midnight, locks the band in "
            "Control Thoughts necklaces, offers 25,000 for the escort, and hires Nemesis to tie off "
            "anyone who refuses (or who merely heard about the job). Keeps a Forest spirit in astral "
            "space for Concealment if a patrol corners the party, but hoards his energy for the rite. "
            "Stats p.44: B4 Q5 S3 C5 I5 W6, Ess 6, Magic 6, Reaction 5; Magic pool 7; Sorcery 7, Conjuring "
            "6, Enchantment 5, Magical Theory 5, Stealth 5, Firearms 4, Etiquette (Corporate/Street) 4, "
            "Armed Combat 3, Bike 2, Unarmed 2. Ares Predator II, armor jacket, survival knife, "
            "medicine lodge 7, spell foci +2 combat and +2 illusion, spirit focus +2, six Control Thoughts "
            "spell locks. Spells (all 6): Hellblast, Manaball, Powerball, Sleep, Combat Sense, Mind "
            "Probe, Chaotic World, Invisibility, Control Thoughts, Petrify, Turn to Goo. Legwork TN 4 "
            "(Bartender, Fixer, Gang Boss, Street Cop, Talismonger, Mafia Don, Yakuza Boss, any mage or "
            "shaman): a hot runner a couple of years back, retired five years ago on a pile of nuyen, "
            "lives in a Barrens apartment building with an elf razor called Dusk, nasty temper, 'shaman "
            "of a very weird totem'. If the runners walk away he comes home with a healed Twilight and "
            "hunts them with Dusk and Lupus. Prologue calls him an insect shaman; the cast page says "
            "Spider."
        ),
    },
    {
        "name": "Dusk",
        "role": "Eclipse's coal-black elf street samurai bodyguard, silent since the run that made them each other's only survivors",
        "archetype": "Street Samurai",
        "title": "Bodyguard to Eclipse",
        "race": "Elf",
        "gender": "Male",
        "connection": 2,
        "description": (
            "Coal-black skin, silver hair, eyes that look lavender; a dangerous-looking razorpunk who "
            "stands at the bar with a package and gives everyone one cold glance. The strong, silent "
            "type who speaks only when speech is unavoidable and has been running the shadows a long "
            "time."
        ),
        "background": "A few years ago he and Eclipse were the only survivors of a deadly run on which each saved the other's life; following the old samurai code he has served as Eclipse's personal bodyguard ever since. Will protect Eclipse and the plan with his life.",
        "notes": (
            "Delivers the Narcojet package at the Pitbull, works the elevator at the penthouse, and "
            "ambushes pursuers short of the clearing from a tree with arrows before dropping to work "
            "them over one at a time with the katana. Stats p.36: B4 Q7(9) S4(6) C4 I4 W4, Ess 0.5, "
            "Reaction 5(9) +3D6; Armed Combat 6, Firearms 6, Stealth 6, Unarmed 6, Etiquette (Street) 3, "
            "Bike 2, Throwing 1. Muscle Replacement 2, Wired Reflexes 2, smartgun link. Ares Predator II "
            "(reactive trigger, smartgun), compound bow system with smart mount and 20 arrows (6M2), FN "
            "HAR, katana (6M3), lined coat, five shurikens, six stimulant patches."
        ),
    },
    {
        "name": "Twilight",
        "role": "Ancient, evil free spirit in the shape of a giant spider, dying in its Salish-Shidhe place of power until the Elementals' song heals it",
        "archetype": "Free Spirit",
        "title": "Free spirit (Greater Form); Eclipse's 'servant'",
        "race": "Free Spirit",
        "gender": "Male",
        "connection": 1,
        "description": (
            "A whisper like dry leaves skittering over paper, a chilling mental giggle, and -- once healed "
            "-- a three-meter spider stepping out of a spot of light in Great Form. Chaos and destruction "
            "are its nature; it is arrogant, hungry, and sarcastic with its partner ('I would hate to "
            "accidentally devour you in the throes of a feeding frenzy')."
        ),
        "background": (
            "Escaped its original summoner's binding centuries ago, in the last cycle of magic, and "
            "roamed the world until four powerful Australian outback shamans tricked it into a place of "
            "power and locked it in a cave that imprisoned other evil spirits. Five months ago the wards "
            "broke when the novice shaman Sam Verner pulled the power stone (Find Your Own Truth); still "
            "tangled in the binding spell it dragged itself back to the place it was first summoned "
            "from, in what is now the Salish-Shidhe Council near the Seattle border, cut off from the "
            "astral plane and fading. It cast a mental feeler for Spider shamans and found Eclipse. It "
            "does not mean to honor their covenant for long."
        ),
        "notes": (
            "Stats p.45 (Grimoire p.75 for Great Form): B6(16) Q8 S10(20) C1 I6 W7, Ess 10, Reaction 8 "
            "(+5 Initiative in Great Form); Conjuring 6, Sorcery 6, Negotiation 3, Stealth 3; attack 8S2; "
            "spells Powerball 6, Manaball 6, Combat Sense 6, Mind Probe 6, Invisibility 6, Barrier 6, Toxic "
            "Wave 6. Powers: Binding, Confusion, Dispelling, Enhanced Physical Attributes, Essence Drain, "
            "Fear, Immunity (age, pathogens, poisons), Immunity to Normal Weapons (impenetrable cover; "
            "immune to small arms under Power 5; normal-weapon attackers roll Willpower, not skill), "
            "Regeneration, Sorcery, Venom, Wealth. Weakness: silver (severe allergy and vulnerability). "
            "Emerges at combat turn 3 of the climax, whole at turn 6, untouchable before that; drains the "
            "runners first and the spell-locked band after, leaving no witness to its return. Legwork: "
            "no information available anywhere. Loose alive, it and Eclipse hunt the team in Seattle."
        ),
    },
    {
        "name": "Lupus",
        "role": "Famous CAS music-trideo producer and secret wolf shapeshifter paying off Eclipse's favor as the 'director'",
        "archetype": "Media Producer",
        "title": "Music trideo producer / director (CAS)",
        "race": "Wolf Shapeshifter",
        "gender": "Male",
        "connection": 3,
        "description": (
            "A coarse, hairy man in flashy, expensive clothing who pours himself a drink at Eclipse's bar "
            "and ignores the hired help. Really is one of the best music-trideo producers in the CAS -- "
            "Eclipse was telling the truth about that. In wolf form he goes for the nearest throat "
            "without a sound."
        ),
        "background": (
            "Always different from the rest of his pack, he left the forest as soon as he was old enough, "
            "discovered music in Seattle, found he had no gift for it, and trained in music trideo "
            "instead; within a few years he was at the top of the business. A rival learned what he was "
            "and blackmailed him; Lupus hired Eclipse and Dusk to make the blackmailer disappear. They "
            "did their homework too, learned his secret, and instead of using it reserved a favor for "
            "someday. This is someday."
        ),
        "notes": (
            "Sets up the floodlights and tripod trid recorders at the clearing; in the forest he shifts "
            "and, with Dusk, stalks pursuers to keep them from the band; runs at Serious damage. Stats "
            "p.37 (human/wolf): B5/7 Q4x5/6x5 S5/6 C5/5 I3/3(4) W3/2, Ess 8/6, Reaction 5; Stealth 6, "
            "Unarmed 5, Armed Combat 4, Negotiation 4, Etiquette (Corporate/Media/Street) 4, Computer 3; "
            "bite 6M3; Enhanced Physical Attributes (animal form), low-light eyes, Regeneration; silver "
            "(mild allergy, severe vulnerability). Gear: survival knife, three trid recorders, ten "
            "recorder chips, pocket secretary."
        ),
        "contact_skills": ["Music trideo production and the CAS entertainment scene"],
    },
    {
        "name": "Nemesis",
        "role": "Well-known mage assassin, secretly a vampire, who owes Eclipse a favor and collects it by hunting the runners",
        "archetype": "Assassin",
        "title": "Mage assassin (freelance)",
        "race": "Human (vampire)",
        "gender": "Male",
        "connection": 3,
        "description": (
            "A reputation to keep and a secret to keep it with. Opens from a quiet street corner with "
            "spells and an SMG at range; only if the runners close and he starts losing does he use what "
            "he has become, and then he fights to the death, because anyone who has seen a vampire's "
            "powers cannot be allowed to talk."
        ),
        "background": (
            "A contract turned out to be a vampire, which drained his Essence and made the mistake of "
            "not destroying him. Nemesis came back, destroyed his maker, collected the fee and killed the "
            "client. Back in business, he hides the change even from his victims, prefers not to feed "
            "on targets, and has spread a rumor that he uses an Essence-draining spell to explain the "
            "ones who look bitten. Not happy about any of it. He would never infect anyone -- making a "
            "vampire takes effort he will not spend."
        ),
        "notes": (
            "Hired by Eclipse the night of the delivery to tie off the runners once they refuse the "
            "escort (or from the start if they never take the job). His pocket secretary (Computer 6) "
            "shows a meeting with 'E.' that afternoon at Eclipse's apartment building. Stats p.29 -- "
            "the attribute column is garbled in the OCR (Body 6, Charisma 4, Intelligence 5, Willpower 5; "
            "Quickness, Strength, Essence, Magic and Reaction unreadable, +2D6 Initiative); Sorcery 6, "
            "Magical Theory 4, Conjuring 3, Firearms 3, Etiquette (Corporate) 2, Unarmed 2; Boosted "
            "Reflexes 1, low-light cybereyes with thermographic. Armor jacket, three flash-paks, HK227 "
            "SMG (laser, gas-vent 2), Power Focus 1, spell locks holding Armor and Personal Combat Sense. "
            "Spells: Mana Bolt 5, Manaball 5, Power Bolt 5, Personal Combat Sense 5, Clairvoyance 5, "
            "Detect Guns 4, Detect Enemies 2, Heal Moderate Wounds 3, Increase Reaction +2, Confusion 4, "
            "Mask 3, Armor 5. Vampiric: Enhanced Physical Attributes, Enhanced Senses, Essence Drain, "
            "Immunity, Infection, Mist Form, Regeneration, thermographic vision; sunlight (severe), "
            "induced dormancy, Essence loss, wood."
        ),
    },
    {
        "name": "Whispering Wind",
        "role": "The Elementals' lead singer and songwriter; a mercenary's daughter whose songs carry a real ritual she does not know she remembers",
        "archetype": "Rocker",
        "title": "Lead vocalist and songwriter, The Elementals",
        "race": "Human",
        "gender": "Female",
        "organization": "The Elementals",
        "connection": 3,
        "description": (
            "A dark beauty with mocking brown eyes and a voice to match, in tight, skimpy red leathers "
            "on stage. Learned early to look after herself; her friends have watched a drastic change in "
            "her since her father died. Rides one of the new Aurora racing bikes."
        ),
        "background": (
            "The only daughter of a famous mercenary who was pleased she chose singing over his trade "
            "and who died recently in a corp action in Australia, leaving her depressed and a lot of old "
            "mercs who held him in esteem and will do her favors. Months ago she wandered into a used "
            "book store and came out with Professor Erik Vonen's leather-bound 'The Fifth World of the "
            "Third Eye', a pre-Awakening how-to for summoning things from other planes -- mostly drek, "
            "but with true scraps of the shamans' rites from the age of Twilight's first summoning. She "
            "carries those racial memories herself; the songs she wrote from the book and the rhythms "
            "she felt hold power, and 'Healing the Spirit' is a garbled rejuvenation ritual."
        ),
        "notes": (
            "Stats p.46: B5 Q5 S4 C6 I4 W6, Ess 5.6, Reaction 4; Etiquette (Street) 5 / (Media) 3, "
            "Firearms 4, Armed Combat 3, Bike 2, Unarmed 2; Instrumental Music 6, Musical Composition 4; "
            "datajack, synthesizer link; Ceska vz/120 (the p.16 text arms her with a 'Light Fire 70'), "
            "one concussion grenade, Fairlight COR-XM Compu-keyboard, survival knife, throwing knife, "
            "synth-leather jacket. Chip in her jacket pocket (or on the dresser by the book if caught "
            "washing her hair). Escaping, she warns Wildfire by vidphone and holes up with him (or the "
            "next member) with the surviving mercs. Without her the rite still works, slower, with a "
            "third-rate stand-in. Kill her and her father's friends come for the team."
        ),
    },
    {
        "name": "Wildfire",
        "role": "The Elementals' elf guitarist; ex-go-ganger who runs the Barrens' one neutral-ground arcade",
        "archetype": "Rocker",
        "title": "Guitarist, The Elementals; owner of Wildfire's Fantasy Arcade",
        "race": "Elf",
        "gender": "Male",
        "organization": "The Elementals",
        "connection": 3,
        "description": (
            "Energy bursting off the photo: red biker leathers clashing with bright red hair, green eyes "
            "amused at a private joke. Unlike most elves he figures he is just a regular guy; smart and "
            "confident to the point of arrogance, but patient and forgiving. Rides a Yamaha Rapier."
        ),
        "background": (
            "A former go-gang member who lifted himself above the gang mentality without forgetting it. "
            "He bought a trid/simsense arcade in the worst of the Redmond Barrens and made it neutral "
            "territory for every gang, mediating their leaders in his back room; the only gang that "
            "broke his rule lost its clubhouse to a high-explosive missile."
        ),
        "notes": (
            "Stats p.47: B5 Q5 S4 C6 I5 W6, Ess 5.6, Reaction 5; Armed Combat 5, Etiquette (Street) 5 / "
            "(Media) 3, Firearms 3, Bike 2, Unarmed 2; Instrumental Music 6, Musical Composition 4; "
            "datajack, synthesizer link; Beretta 200ST, katana (4M3), Fender-Fase/180 guitar, survival "
            "knife, throwing knife, synth-leather jacket. Will not run -- fights ferociously until "
            "knocked out; chip in his jacket pocket. Killing him hands a lot of go-gangers a vendetta."
        ),
        "contact_skills": ["Go-gang mediation and gang politics in the Redmond Barrens"],
    },
    {
        "name": "Bambi",
        "role": "The Elementals' enormous troll drummer; night watchman at his family's troll department store",
        "archetype": "Rocker",
        "title": "Drummer, The Elementals; night watchman, Bloom's Troll Emporium",
        "race": "Troll",
        "gender": "Male",
        "organization": "The Elementals",
        "connection": 2,
        "description": (
            "People laugh at a troll named Bambi until they see him: large even for a troll, and one of "
            "the ugliest on the face of the earth, twirling sticks behind an acoustic kit. A talented and "
            "surprisingly dextrous drummer. Rides a Honda Viking built for a troll with a Panther assault "
            "cannon behind a gun port."
        ),
        "background": (
            "He and his two brothers goblinized at puberty and their father accepted them, then, seeing "
            "how hard their size made ordinary life, opened Bloom's Troll Emporium. The store flourished; "
            "the brothers inherited it, hired a manager since all three had careers, and Bambi moved into "
            "his father's old flat at the back as night watchman. Every go-gang in the area waves at him."
        ),
        "notes": (
            "Stats p.48: B10 Q5 S8 C5 I4 W5, Ess 6, Reaction 5; Armed Combat 5, Etiquette (Street) 5 / "
            "(Media) 3, Firearms 3, Bike 2, Unarmed 2; Instrumental Music 6, Musical Composition 4; no "
            "cyberware. Combat axe (8S2), Honda Viking with Panther cannon (10D4), SCK Model 100 SMG "
            "(laser), Sheff-6000 drum kit, survival knife (8L3), throwing knife, synth-leather jacket. "
            "Fires the cannon until melee range, then the axe. Chip in his pocket unless he is listening "
            "to it. Nobody much notices his death unless his brothers are alive."
        ),
    },
    {
        "name": "Coyote",
        "role": "The Elementals' Amerindian bassist; Ute Nation military veteran who repays the squatters who took him in",
        "archetype": "Rocker",
        "title": "Bass / key-guitar, The Elementals; Ute Nation veteran",
        "race": "Human",
        "gender": "Male",
        "nationality": "Ute Nation",
        "organization": "The Elementals",
        "connection": 3,
        "description": (
            "A dark, solemn Indian brave in traditional clothing, long black hair held back by a "
            "beautifully hand-tooled leather headband, playing a Yamaha key-guitar; named for his "
            "personal totem. Off stage a fun-loving, carefree young man with a biting sarcastic wit who "
            "plays jokes on everyone, and a generous one who will risk his life for friends or "
            "innocents. Rides a Yamaha Rapier with a comm unit."
        ),
        "background": (
            "Served many years in the Ute Nation's military forces, grew bored and went to Seattle for "
            "his true vocation, music. Lived at first in the Amerindian squatter camp on the grounds of "
            "the ruined Redmond Grand Hotel, got his own apartment across town when the band's money "
            "came in, and still brings the camp food and supplies once a week and stays the night."
        ),
        "notes": (
            "Stats p.49: B6 Q6 S6 C5 I4 W5, Ess 5.6, Reaction 5; Gunnery 5, Etiquette (Street) 5 / "
            "(Tribal) 4, Firearms 4, Rotor Craft 3, Armed Combat 3, Unarmed 3, Bike 2; Instrumental Music "
            "6, Musical Composition 4; datajack, synthesizer link; Browning Ultra Power, Yamaha LNX-4200 "
            "key-guitar, survival knife (6L3), throwing knife, synth-leather jacket. Knows the camp's "
            "dirt road by heart and always beats a pursuer to it; surrenders the moment a squatter is "
            "killed, chip in the pouch on the thong around his neck. Only the band avenges him."
        ),
        "contact_skills": ["Amerindian squatter community of the outer Redmond Barrens", "Ute Nation military background"],
    },
    {
        "name": "Josh Bloom",
        "role": "Bambi's troll brother and co-owner of Bloom's Troll Emporium; net gun, stun baton, mannequin act",
        "archetype": "Shopkeeper",
        "title": "Co-owner, Bloom's Troll Emporium",
        "race": "Troll",
        "gender": "Male",
        "connection": 1,
        "description": "The quieter Bloom brother, dim and loyal, who poses as a hunting-clothes mannequin in the Leisure section with a loaded net gun and a Manhunter under his jacket. Surname inferred from the family store; the book calls him only Josh.",
        "notes": "Stats p.21: B6 Q3 S6 C1 I2 W2, Ess 5.7, Reaction 2; Unarmed 6, Firearms 5, Etiquette (Corporate/Street/Tribal) 3, Bike 2, Computer B/R 2, Stealth 2; retractable spurs (6M2). Armor vest with plates, Colt Manhunter (laser and ultrasound sights), Defiance AZ-150 stun baton, Williams Capture-500 net gun (Street Samurai Catalog p.72), DocWagon Basic. Rooftop shooter in the alley ambush; ten minutes from the store when the alarm rings.",
    },
    {
        "name": "Hoss Bloom",
        "role": "Bambi's chromed troll brother and co-owner of Bloom's Troll Emporium; muscle replacement, wired, combat axe and shurikens",
        "archetype": "Shopkeeper",
        "title": "Co-owner, Bloom's Troll Emporium",
        "race": "Troll",
        "gender": "Male",
        "connection": 1,
        "description": "The dangerous Bloom brother: wired, muscle-replaced, crouched behind a tower of Mama Beani's Canned Troll Fritters in the food section, opening with shurikens and finishing with a combat axe. Surname inferred from the family store; the book calls him only Hoss.",
        "notes": "Stats p.21: B7(8) Q3(7) S6(10) C1 I2 W1, Reaction 2(4) +2D6; Unarmed 6, Firearms 5, Throwing Weapons 5, Armed Combat 3, Stealth 3, Etiquette (Street) 3, Bike 2; Muscle Replacement 4, Wired Reflexes 1. Armor jacket, Colt Manhunter (laser and ultrasound), combat axe (10S2), Remington Roomsweeper, eight shurikens, DocWagon Platinum.",
    },
    {
        "name": "Micro",
        "role": "Dwarf technician who keeps Wildfire's Fantasy Arcade running; laser crescent axe; berserk if a game gets smashed",
        "archetype": "Technician",
        "title": "Technician, Wildfire's Fantasy Arcade",
        "race": "Dwarf",
        "gender": "Male",
        "connection": 2,
        "description": "The arcade's dwarf tech, usually playing cards with Thud in the repair shop or with his head in a game while a laser crescent axe leans against the table. Goes berserk when the games get damaged.",
        "notes": "Stats p.18 (partly garbled): Computer Theory 6, Computers B/R 6, Electronics 6, Electronics B/R 6, Armed Combat 5, Etiquette (Street) 3; datajack with 200 Mp memory; armor vest, laser crescent axe (+1 reach), tech kit. A first-rate electronics man buried in the Barrens -- a contact worth cultivating after the dust settles.",
        "contact_skills": ["Electronics and computer repair", "Trid and simsense game hardware"],
    },
    {
        "name": "Thud",
        "role": "One of the twin troll bouncers at Wildfire's Fantasy Arcade; shock gloves",
        "archetype": "Bouncer",
        "title": "Security, Wildfire's Fantasy Arcade",
        "race": "Troll",
        "gender": "Male",
        "connection": 1,
        "description": "Twin to Blunder; plays cards with Micro in the back and comes when called, pulling on his shock gloves.",
        "notes": "Stats p.18 (shared with Blunder): B9 Q3 S9 C1 I4 W2, Ess 6, Reaction 2; Unarmed 6, Etiquette (Street) 5, Armed Combat 4, Firearms 2. Armor clothing, Beretta 200ST, shock gloves (5L3 Stun plus 4M1 fist).",
    },
    {
        "name": "Blunder",
        "role": "The other twin troll bouncer at Wildfire's Fantasy Arcade; works the floor and stares at strangers",
        "archetype": "Bouncer",
        "title": "Security, Wildfire's Fantasy Arcade",
        "race": "Troll",
        "gender": "Male",
        "connection": 1,
        "description": "Twin to Thud; wanders the arcade crowd watching for trouble and gives every unfamiliar face the same suspicious stare before ignoring it. Throws out anyone caught on the stairs unless they talk their way past (Etiquette (Street) 2 / Negotiation 4).",
        "notes": "Stats as Thud: B9 Q3 S9 C1 I4 W2; Unarmed 6, Etiquette (Street) 5; armor clothing, Beretta 200ST, shock gloves.",
    },
    {
        "name": "Wood Nymph",
        "role": "Elf dancer at the Pink Pitbull who dreads Eclipse's stare and the spider on his hat",
        "archetype": "Dancer",
        "title": "Dancer, Pink Pitbull",
        "race": "Elf",
        "gender": "Female",
        "connection": 1,
        "description": "A lithe elf girl on the Pitbull's stage. Used to lust; what unsettles her is the something dark in Eclipse's eyes, and the tarantula that rides his hat down to her midriff when he leans in with a scrip.",
        "notes": "One of the staff who can be asked about Eclipse (Etiquette (Street) 5 table on the Pink Pitbull row). A fine low-level ear on the Barrens strip circuit.",
    },
    {
        "name": "Chachi",
        "role": "Ex-squatter hair stylist to bored corporate housewives, phony Latin accent and real gallantry; Redmond Business Nest",
        "archetype": "Hair Stylist",
        "title": "Proprietor, Chachi's Hair Styles",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": "A former squatter who bettered himself and hides it behind a phony Latin accent; genuinely gallant, he delights in bringing a thrill into the dull lives of the overweight corporate housewives who fill his appointment book. Trained his five stylists -- ex-squatters like him -- himself.",
        "notes": "Squatter stats with Hair Stylist 6; stylists Hair Stylist 4. Salon computer holds only customers' hairstyles. Hears everything Redmond's corporate wives say.",
        "contact_skills": ["Corporate-wife gossip from the Redmond/Bellevue edge"],
    },
    {
        "name": "Sam Sprawl",
        "role": "Junior-exec-grade real-estate agent whose office shares the Business Nest with the band's studio",
        "archetype": "Corporate Official",
        "title": "Real-estate agent, Sam Sprawl's Real Estate",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": "Runs a two-room agency -- a reception with a couch and glossy magazines, an inner office decorated in mid-American bland -- on the ground floor of the Redmond Business Nest. Corporate Official stats (Sprawl Sites p.107).",
        "notes": "Office computers are full of nothing but real-estate listings. A useful source on who owns what along the Redmond/Bellevue edge -- including, potentially, the litigation over the Redmond Grand Hotel land.",
        "contact_skills": ["Redmond and Bellevue property listings and ownership"],
    },
    {
        "name": "Lola",
        "role": "Sam Sprawl's secretary at the Redmond Business Nest",
        "archetype": "Corporate Secretary",
        "title": "Secretary, Sam Sprawl's Real Estate",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": "Sits at the small reception desk of Sam Sprawl's Real Estate; Corporate Secretary stats (SR p.165). Sees everyone who comes and goes through the Business Nest's ground floor, including four musicians on motorcycles.",
        "notes": "Name only in the book.",
    },
    {
        "name": "Dr. Raven",
        "role": "Mysterious investigator whose crew keeps breaking cases for Lone Star -- latest, Global Technologies' persona BTLs (news handout)",
        "archetype": "Investigator",
        "title": "Independent investigator ('Dr. Raven and his expert crew')",
        "race": "Human",
        "gender": "Male",
        "connection": 4,
        "description": "The newsnet's 'mysterious Dr. Raven', whose expert crew once again broke a case for Lone Star Security in November 2051: he revealed that skillsoft maker Global Technologies had produced illegal BTL chips carrying a full range of emotions and the skills of a complete persona, and that the CAS military was the highest bidder before he interceded.",
        "notes": "Known only from the Total Eclipse handouts ('Raven Repeats'). Race and gender not given -- treat as unknown. Whatever the runners did in Dreamchipper, the public credit went to him.",
    },
    {
        "name": "Governor Schultz",
        "role": "Governor of the Seattle Metroplex; forming a task force into Shiawase Envirotech bid-rigging (news handout)",
        "archetype": "Politician",
        "title": "Governor, Seattle Metroplex",
        "race": "Human",
        "connection": 5,
        "description": "The metroplex governor. In November 2051 the governor's office announced a task force to investigate allegations of illegal bid-rigging by Shiawase Envirotech after a preliminary look at public-works sub-contracts revealed 'a pattern of suspicious actions'.",
        "notes": "Handout name only; gender and first name not given here. Earlier handouts (Seattle News-Intelligencer row) mention Governor Schultz's Crime Commission.",
    },
]

ORG_UPDATES = {
    "Crimson Crush": {
        "notes_append": (
            "Total Eclipse: a lone Crimson Crush member on a Rapier nearly runs Eclipse down outside the "
            "Pink Pitbull, and a beat-up, heavily modified Crimson Crush Ford Americar is parked among "
            "the gang bikes outside Wildfire's Fantasy Arcade -- the Crush honor the arcade's neutral "
            "ground like everyone else. Six volunteers from six different gangs back Wildfire when he is "
            "forewarned; any Crush who die there are one more score for the gang to settle."
        ),
    },
    "Lone Star Security": {
        "notes_append": (
            "Total Eclipse (November 2051): heavy patrols around Redmond Center Mall and the Redmond "
            "Business Nest (rousts loiterers, hauls in visible hardware, hordes answer any commotion); "
            "Bellevue-edge alarm response in 1-6 minutes in a Chrysler-Nissan Patrol-1 with backup "
            "called on arrival; Redmond Barrens silent alarms answered in about 30 minutes; a station "
            "near Bloom's Troll Emporium. Lone Star Cop block p.16: B4 Q4 S4 C2 I3 W3, Firearms 3, Police "
            "Procedures 4, Ares Predator, armor jacket, stun baton, Ford Americar. Newsnet: 'the "
            "mysterious Dr. Raven and his expert crew once again broke a case for Lone Star' -- Global "
            "Technologies' persona BTL chips."
        ),
    },
    "Salish-Shidhe Council": {
        "notes_append": (
            "Total Eclipse: the least-patrolled stretch of the Seattle line lies beyond the outer Redmond "
            "Barrens, but the forest a day inside it is sacred to the local tribes and patrolled more "
            "often. Border Patrol (5) p.33: B6 Q6 S6 C3 I5 W4, Firearms 5, Gunnery 5, Rotor Craft 3, "
            "Etiquette (Tribal) 4, no Negotiation (default to Charisma); low-light cybereyes, smartgun "
            "link; armor clothing, Beretta Model 70 SMG (gas-vent 2, smartgun), Seco LD-120, survival "
            "knife, thermographic binoculars, medkit, trauma patches. Trained warriors: killing them "
            "and being traced means 'deep guano'. Captured intruders are taken to patrol headquarters, "
            "interrogated (magically checked), fined heavily, given a month's hard labor and sent home. "
            "Eclipse's party mows down one patrol on the way in (burned, arrows, one torn up by a wolf). "
            "A shaman-led patrol is the GM's cavalry at the clearing. The success handout has 'Salish-"
            "Shidhe authorities' reporting four bodies found at dawn in a clearing 'rumored to be a "
            "gathering spot for Awakened creatures' just across the border; Twilight's place of power "
            "and a ghoul-infested Indian burial site lie in Council forest."
        ),
    },
    "Native American Nations (Sovereign Tribal Council)": {
        "notes_append": (
            "Total Eclipse: runners who try to warn NAN authorities about an evil free spirit reviving "
            "in Salish-Shidhe forest are ridiculed and ignored -- no proof, an unbelievable story -- and "
            "by the time the red tape clears and a patrol is sent, Twilight is healed and wipes it out, "
            "leaving the runners and their NAN contacts answering to angry, suspicious Council members. "
            "'NAN is just as powerful as any corp and twice as mean when one of their own gets geeked.'"
        ),
    },
    "Ute Nation": {
        "notes_append": (
            "Total Eclipse: The Elementals' bassist Coyote served many years in the Ute Nation military "
            "forces (Gunnery 5, Rotor Craft 3) before boredom sent him to Seattle to play music."
        ),
    },
    "Humanis Policlub": {
        "notes_append": (
            "Total Eclipse (November 14, 2051 handout): Humanis, 'rumored to have connections with "
            "Alamos 20,000', staged a City Hall demonstration against the city's plan to declare the "
            "second Monday of December an official Awakening Day with a city-wide festival; fighting "
            "broke out when metahuman activist groups arrived to counter-protest."
        ),
    },
    "Alamos 20,000": {
        "notes_append": (
            "Total Eclipse (November 2051 handout): the newsnet openly describes Humanis Policlub as "
            "'rumored to have connections with Alamos 20,000' when reporting the Awakening Day riot at "
            "City Hall."
        ),
    },
    "Shiawase Corporation": {
        "notes_append": (
            "Total Eclipse (November 2051 handout): Governor Schultz is forming a task force to "
            "investigate allegations of illegal bid-rigging by Shiawase Envirotech after a preliminary "
            "look at public-works sub-contracts showed 'a pattern of suspicious actions'."
        ),
    },
    "Global Technologies": {
        "notes_append": (
            "Total Eclipse (November 14, 2051 handout, the Dreamchipper aftermath): the news that Global "
            "was producing illegal experimental BTL chips -- 'a full range of emotions and the skills of "
            "a complete persona', with the CAS military as highest bidder -- broke publicly, credited to "
            "'the mysterious Dr. Raven' working for Lone Star. Stock values dropped dramatically and "
            "rumor says Hollywood Simsense will use the moment to complete its attempted takeover."
        ),
        "enemies_add": ["Hollywood Simsense Entertainment"],
    },
    "Hollywood Simsense Entertainment": {
        "notes_append": (
            "Total Eclipse (November 2051 handout): rumored to be moving to complete its recently "
            "attempted takeover of Global Technologies while Global's stock craters over the persona-BTL "
            "scandal."
        ),
        "enemies_add": ["Global Technologies"],
    },
    "Brilliant Genesis": {
        "notes_append": (
            "Total Eclipse (November 2051 handout): has just announced the release of 'Ninja Dragon "
            "Wars', starring Honey Brighton, 'formerly with MegaMedia'."
        ),
    },
    "MegaMedia Entertainment": {
        "notes_append": (
            "Total Eclipse (November 2051 handout): still the corp Honey Brighton is 'formerly with' as "
            "Brilliant Genesis releases her 'Ninja Dragon Wars'. Eclipse poses as an anonymous "
            "entertainment corp's man; the street's take on the Elementals is that none of the corps "
            "want them ('too radical, and not that popular') and that the music corps will not like a "
            "self-released chip."
        ),
    },
    "Renraku Computer Systems": {
        "notes_append": (
            "Total Eclipse (November 14, 2051 handout): rumors run rampant as the city council meets with "
            "Renraku officials; inside sources say Renraku will offer to buy the mismanaged Seattle "
            "Public Ferry System and the city is tempted. Both sides refuse comment."
        ),
    },
    "Seattle News-Intelligencer": {
        "notes_append": (
            "Total Eclipse: Update-Net of Tuesday November 14, 2051, 14:00. International: massive CAS "
            "rioting around Atlanta's Fulton County Stadium squatter habitat. Local: Governor Schultz's "
            "task force on Shiawase Envirotech bid-rigging; Humanis riot at City Hall over Awakening Day; "
            "Renraku courting the Seattle Public Ferry System; Kingdome closed until about May 1 after "
            "the troll Red Death gang of Puyallup trashed it. Business: Global Technology stock crash "
            "over illegal persona BTLs, Hollywood Simsense takeover rumor; 'Raven Repeats'. "
            "Entertainment: Maria Mercurial back on the concert trail after a long honeymoon once her "
            "next simchip is done; Brilliant Genesis releases 'Ninja Dragon Wars' with Honey Brighton. "
            "Sports: the all-troll Road Hogs vs the reformed Ratchet Squad at Duster's Drag Strip & "
            "Arena; the WL's newest member beat the Cardinals 13-1. Success lead: 'Elemental Magic' -- "
            "The Elementals' 'Through the Lightning' is the number-one club request, 'syntho-magic'. "
            "Failure lead: 'Death of the Elementals' -- four bodies across the Salish-Shidhe border, "
            "vampire or banshee suspected."
        ),
    },
}

LOC_UPDATES = {
    "Underworld 93": {
        "notes_append": (
            "Total Eclipse: The Elementals played a sold-out show here a few weeks before the adventure "
            "('I heard them at Underworld 93') and, in the success ending, sold-out dates again as "
            "'Through the Lightning' tops the club requests. The club is one of the places their demo "
            "'Healing the Spirit' circulated."
        ),
    },
    "The Kingdome": {
        "notes_append": (
            "Total Eclipse (November 14, 2051 handout): temporarily closed for repairs after 'a violent "
            "incident this past weekend' -- reportedly the troll Red Death gang of the Puyallup District "
            "got inside and did considerable damage. Reopening about May 1; ticket-holders are told to "
            "contact event promoters, not dome management."
        ),
    },
    "The Barrens (Seattle)": {
        "notes_append": (
            "Total Eclipse: Redmond Barrens geography -- the Pink Pitbull and Eclipse's ten-storey block "
            "a few blocks apart among condemned buildings; Wildfire's Fantasy Arcade in the thrill-gang "
            "heartland; Bloom's Troll Emporium on a dead-end street; the Redmond Grand Hotel on its "
            "foliage-choked hill where the ruins thin toward the NAN boundary; the Redmond Center Mall "
            "at the prosperous Bellevue edge. A reputation like Eclipse's lets a man walk the Barrens "
            "unmolested; the street saying is 'Don't cross an insect shaman unless you're absolutely "
            "sure you can frag him.' Lone Star takes about 30 minutes to answer a Barrens alarm."
        ),
    },
    "Salish-Shidhe Border Post (Seattle crossing)": {
        "notes_append": (
            "Total Eclipse: Eclipse's party and pursuing runners avoid the crossing entirely, slipping "
            "over the least-patrolled section of the line from the outer Redmond Barrens just after one "
            "of its infrequent patrols passes -- and running into the more frequent patrols of the "
            "sacred forest beyond."
        ),
    },
    "Stuffer Shack - Redmond Barrens": {
        "notes_append": (
            "Total Eclipse: a Stuffer Shack sits in the small strip mall across from Redmond Center Mall, "
            "beside the Redmond Business Nest -- whether this franchise or another is not said."
        ),
    },
}

NPC_UPDATES = {
    "Maria Mercurial": {
        "notes_append": (
            "Total Eclipse (November 14, 2051 handout): 'after a long honeymoon cum vacation, Maria "
            "Mercurial announced that she will head out on the concert trail as soon as she finishes her "
            "next simchip.'"
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
This adventure "requires almost no decking". Three small systems are described; none is worth more
than a tiny host.

**1. Eclipse's home computer** (p.32; study of the penthouse). Physically unhooked from the Matrix
whenever he leaves town -- the unlisted LTG number has to be decked out of the phone company first,
and even then the only datajack is inside the penthouse. "Very basic": one node each.

| Node | Function | Rating / IC |
|---|---|---|
| I/OP | The study terminal | Orange-3, Access 4 |
| CPU | -- | Orange-4, Barrier 6 |
| SM | Building security and traps slave | Orange-4, Trapped IC: looks like Barrier 4 but also releases Trace and Burn 4 |
| DS | Eclipse's personal log: the whole Twilight association, the search for the healing rite, the discovery of The Elementals and his research on whether "Healing the Spirit" is close enough to the rejuvenation ritual. No map or description of the NAN destination | Orange-4, Killer 4 |

**2. The Elementals Recording Company studio computer** (p.15). Green-6 with a single Barrier 7 IC.
Contains the band members' current home addresses (Debugging: for teams that lose every tail).
No copy of the master -- that exists only on the four carried chips.

**3. Nemesis' pocket secretary** -- Computer (6) to open; data files show he met "E." that afternoon
at Eclipse's building address. **Sam Sprawl's** and **Chachi's** front-desk computers hold nothing but
listings and hairstyles.
"""

NOT_BUILT = """
- **Professor Erik Vonen** -- long-dead, third-rate, financially desperate anthropology professor who
  rode the pre-Awakening new-age wave; his books claimed solid sources and were mostly fabrication,
  but 'The Fifth World of the Third Eye' (a summoning how-to) carries true scraps of ancient rites.
  Legwork TN 6: best-sellers before the Awakening, 'drek' to modern mages, 'some of it almost felt
  true'. On Whispering Wind's row and her apartment.
- **Whispering Wind's father** (famous mercenary, killed in a corp action in Australia) and his two
  **mercenary friends**; **Sam Verner** (the novice shaman of Find Your Own Truth who freed Twilight);
  **the four Australian shamans**; **Lupus's blackmailer** and **Lupus's pack** -- backstory on the
  NPC rows.
- **The elf DJ** who sold Eclipse the demo chip for 100 nuyen and quit (just passing through); the
  **troll and dwarf dancers** and the **bouncer** at the Pink Pitbull; **Chachi's five stylists**;
  the **Federated Salish Savings and Loan** branch technician and guard (bank not built as an org);
  **Boweevel**, 'the current combat bike idol' (one line).
- **The Redmond Grand squatters, their Snake shaman, the hidden scout and the Park spirit**; **the
  four wolves**; **the salamander and the naga**; **the banshee and her ghouls**; **the Salish-Shidhe
  border patrol**; **the six gang volunteers and Eclipse's six street toughs** -- stat summaries on
  the location and org rows.
- **The corporation** poisoning the Redmond Grand park and suing for its land, and **the theme-park
  entertainment corp** that built the mechanical animals -- both unnamed; hooks.
- **Ratchet Squad** (reformed Urban Brawl team), **the WL's newest member and the Cardinals**,
  **Honey Brighton** and **'Ninja Dragon Wars'**, **Shiawase Envirotech**, **the Seattle Public Ferry
  System**, **Seattle City Hall** and **Awakening Day**, **Fulton County Stadium (Atlanta)** -- news
  handout texture recorded on the org rows.
- **Bloom's Troll Emporium's hired manager** and **the mall's Trid Games Arcade, Busy Bee Soyburger**
  -- names on the location rows.
"""

PLAY_NOTES = """
- Two halves: a fast, mostly comic snatch-and-deliver (four different home turfs, non-lethal by
  contract, Narcojets in hand), then a betrayal that turns into a forest horror run. Give the players
  almost no legwork time before the tails -- one face-to-face or one phone call each -- and none at
  all after the escort offer (Eclipse's phone is surely tapped).
- Tail rules p.13: three opposed tests against the musician's Vehicle or Stealth; a spotted tail means
  a prepared house, a lost tail means that member is gone for the night. Snatching one at a time
  warns the last two; an escapee joins the next target. Every kill costs part of the fee and makes
  Eclipse angrier, but never stops the ritual.
- Refusers get Nemesis, a vampire who must not be recognized; his pocket secretary is the only thread
  back to a building that is a deathtrap (elevator drop 8S4, salamander, electrified stairs,
  flash-paks, naga). The two clues are the datastore log and the parchment map -- the map, not the
  computer, gives the destination.
- In the forest, track how long The Elementals have been playing: every turn Dusk and Lupus hold the
  team off is a turn closer to a three-meter spider that cannot be hurt until it has fully arrived.
  Five combat turns from the first note the runners hear; emergence at turn 3, full strength at 6.
- Salish-Shidhe patrols are competent, unbribable and un-negotiable (they have no Negotiation skill
  and default to Charisma); Eclipse abandons the runners to one if it comes to that. Capture is a
  fine, a month's hard labor, and a hunted return.
- Karma p.50: awards for surviving, for each band member kidnapped, for disrupting the rejuvenation
  ritual and for defeating Eclipse and his allies (the numbers are lost in the scan -- assign in the
  usual 1-3 range). No corp is angry afterwards; the mercs, the go-gangs, the Bloom brothers or the
  band are, if a musician died.
- Loose ends: Eclipse and Twilight alive means a healed evil spirit and a mad shaman hunting the team
  in Seattle with Dusk and Lupus; the corp litigating for the Redmond Grand land; Wildfire's neutral
  ground and Micro as contacts; the Elementals' 'syntho-magic' -- and a singer who does not know what
  else she remembers.
"""
