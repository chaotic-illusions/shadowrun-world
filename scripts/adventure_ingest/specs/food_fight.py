# Food Fight (Shadowrun 1st Edition core rulebook, "First Run" chapter, pp. 202-208) -- campaign order #2.
# Source text: docs/Adventures/text/Shadowrun 1st - Corebook.txt (viewer pages 220-226).
# ASCII only (pre-commit hook).

ADVENTURE = "Food Fight"
ORDER = 2
SOURCE = "Shadowrun 1st - Corebook.pdf, viewer pp. 220-226 (book pp. 202-208, 'First Run')"
YEAR = "2050 (late)"

SYNOPSIS = """
Late one rainy night, coming home from a run, the biggest, baddest member of the team gets a raging
case of the munchies and the crew pulls into the nearest **Stuffer Shack** -- the 24-hour Aztechnology
supermarket chain that sells everything from Holohayo 3D greeting cards to Ludivenko Lovely
Soya-Sloppies with the DoubleThick option. Half a dozen cars, a couple of bikes and an electro-scoot
sit in the lot; nobody loiters in the rain.

Inside are a clerk, a manager, a stock boy, a handful of customers -- and three members of the
**Chiller Thrillers**, a psychotic thrill-gang casing the joint. When they signal their leader, the
rest of the gang piles out of a van, Spike smashes the PANICBUTTON box outside, and the robbery is
on. Credit cannot be stolen in 2050, so the gang wants stuffers, valuables, and an excuse to hurt
someone. They goad, body-search, and smash the place up until somebody objects, and then they shoot.
They do not back down and they fight until killed or incapacitated.

The equalizer is **Sally Tsung**, the gorgeous street mage with the sword from the "Night on the Town"
fiction, in for a quick munch. She fades into the stockroom at the first sign of trouble, keeps up
Spell Defense, blows away the gang's Coyote shaman Wiley if the team cannot, then slips out the back
door and turns invisible if followed.

Afterwards the property damage outweighs any gratitude from Stuffer Shack, Inc.; the Badges are on
the way and the runners have no urge to explain their hardware to Lone Star. Team karma: 2.
"""

TIMELINE = """
- The team is scattered through the aisles when Slicer Dicer, Static and Wendy signal Catcher.
- Van in the lot empties; Spike smashes the PANICBUTTON box; Catcher, Spike, Wiley and the rest come in.
- Casual brutality escalates: Wendy and Wiley body-search customers; the gang starts trashing shelves.
- Firefight. Every miss rolls on the Food Fight Table (liquid / powder / mushy -- the floor becomes
  Difficult Terrain). Sally Tsung covers the team from the stockroom, then vanishes.
- Lone Star arrives after the shooting stops; the runners should be gone.
"""

ORGS = [
    {
        "name": "Chiller Thrillers",
        "org_type": "gang",
        "affiliation_contact_type": "Gang",
        "tier": 1,
        "headquarters": "Seattle (mobile -- they work out of a van)",
        "summary": "Six-member psychotic thrill-gang; emblem is a skull with a bloody icicle through the left eye",
        "description": (
            "A small thrill-gang that robs for kicks as much as for loot. Their emblem -- a skull pierced "
            "through the left eye socket with a bloody icicle -- is worn on lined coats and armored dusters. "
            "They have the minds of psychotics who get their kicks out of having their feet on someone "
            "else's neck: they kill on a whim, they do not back down, and they fight until killed or "
            "incapacitated. Six known members: Lucas \"Catcher\" Katcherman (leader), Frank \"Slicer "
            "Dicer\" Pilgrim, Bill \"Static\" Pruitt, Wendy, Spike, and the Coyote shaman Willis \"Wiley\" "
            "Fabrizzi."
        ),
        "leadership": [
            {"name": "Lucas Katcherman", "title": "Leader (\"Catcher\")", "notes": "Psychotic; keeps up a high-speed rap when not fighting."}
        ],
        "notes": (
            "Robbery in 2050 means commodities: food, weapons, gold fillings, anything of value the "
            "customers carry. Their method is to case a store with three members inside, then hit it "
            "from the van with the rest, smash the PANICBUTTON box, and goad people into fighting. Use "
            "the Gang Member archetype for the rank and file (Catcher adds Wired Reflexes 1). If the "
            "team wipes them out in Food Fight, the survivors (if any) are a ready-made grudge."
        ),
    },
]

LOCATIONS = []

NPCS = [
    {
        "name": "Lucas Katcherman",
        "role": "'Catcher' -- leader of the Chiller Thrillers; psychotic; shotgun and Warhawk",
        "archetype": "Gang Boss",
        "title": "\"Catcher\", leader of the Chiller Thrillers",
        "race": "Human",
        "gender": "Male",
        "age": 22,
        "organization": "Chiller Thrillers",
        "connection": 1,
        "description": (
            "Average height and build, hair spiked in various lengths and colors. Psychotic. When he is "
            "not in combat he keeps up a dangerous, high-speed rap on any number of subjects."
        ),
        "notes": (
            "Gang Member archetype plus Wired Reflexes 1. Gear: Defiance T-250 shotgun (3 magazines), "
            "Ruger Super Warhawk, lined coat with the Chiller Thrillers' emblem. Waits in the van with "
            "Spike and Wiley for the inside crew's signal, then leads the entry."
        ),
    },
    {
        "name": "Frank Pilgrim",
        "role": "'Slicer Dicer' -- would-be samurai with a katana; never refuses single combat",
        "archetype": "Gang Member",
        "title": "\"Slicer Dicer\", Chiller Thrillers",
        "race": "Human",
        "gender": "Male",
        "age": 22,
        "organization": "Chiller Thrillers",
        "connection": 1,
        "description": (
            "Tall and wiry, in a short Japanese-style jacket with his hair dyed blood-red and styled into "
            "a samurai topknot, just like martial-arts simsense star Nicky Saitoh. Carries a long sack "
            "over one shoulder the shape of a katana. Fancies himself a modern samurai, utters loud kiai "
            "in combat, and will not refuse an apparent challenge to single combat."
        ),
        "notes": (
            "Street Samurai archetype with arm spurs instead of hand razors. Gear: katana, Ares Predator, "
            "nine shuriken, armor jacket tailored into a samurai tunic. Cases the store from Aisle 12 "
            "(personal hygiene)."
        ),
    },
    {
        "name": "Bill Pruitt",
        "role": "'Static' -- burned-out wirehead who talks sports to motor-oil displays",
        "archetype": "Gang Member",
        "title": "\"Static\", Chiller Thrillers",
        "race": "Human",
        "gender": "Male",
        "age": 32,
        "organization": "Chiller Thrillers",
        "connection": 1,
        "description": (
            "A big guy who looks like he has had major muscle replacement -- steroid abuser and "
            "weight-lifter both. Balding, hair dyed stark white and cropped close, temples studded with "
            "half a dozen jacks. Baggy fatigues under an armor coat covered in circuit diagrams of wires "
            "he has jacked. A burned-out wirehead with significant brain damage who is convinced that "
            "numerous inanimate objects are his friends; he likes to talk sports with them."
        ),
        "notes": (
            "Gang Member archetype: Willpower -2, Strength +2, Firearms 6. His optical cyberware is still "
            "burned out from overindulging in Screaming MeeMee wire; the hand razors still work. Gear: "
            "Defiance shotgun (3 clips) concealed under the coat, Defiance Super-Shock taser, large "
            "shoulder bag. Cases the store from Aisle 2, conversing animatedly with a motor-oil display."
        ),
    },
    {
        "name": "Wendy",
        "role": "The gang's 'mom' -- CAS drawl, spike heels, H&K 227 smartgun",
        "archetype": "Gang Member",
        "title": "Chiller Thrillers (\"mom\" of the gang)",
        "race": "Human",
        "gender": "Female",
        "age": 23,
        "organization": "Chiller Thrillers",
        "connection": 1,
        "description": (
            "Voluptuous and heavily made up, hair in the latest Nova style and dyed neon blue, an "
            "armored duster with the gang's gory emblem over skimpy cutoffs and a halter top. Affects "
            "to be the gang's mom, speaks with a deep CAS drawl, and plays one ganger off against "
            "another for her maternal affections. Her current good boy is Wiley."
        ),
        "notes": (
            "Street Samurai archetype: Strength -1, Quickness +1. Gear: H&K 227 SMG with smartgun "
            "circuitry, lined coat with the emblem, shoulder bag with an Ares Predator. Her spike heels "
            "make all terrain Difficult Ground for her (+5 if she runs on really Difficult Ground). Cases "
            "the store from Aisle 8 near the Aztec-Mex displays; body-searches customers with Wiley."
        ),
    },
    {
        "name": "Spike",
        "role": "The reluctant one -- wants food and loot, not a fight; looks like customer Timmy Thinners",
        "archetype": "Gang Member",
        "title": "Chiller Thrillers",
        "race": "Human",
        "gender": "Male",
        "organization": "Chiller Thrillers",
        "connection": 1,
        "description": (
            "Real name and age unknown. Strongly resembles Timmy Thinners, an innocent customer in the "
            "store: very tall, scrawny, hollow-eyed, long scruffy black hair, tattered black leathers. "
            "Unlike the rest of the gang, Spike does not really like trouble and will sometimes try to "
            "talk the others out of getting too violent."
        ),
        "notes": (
            "Gang Member archetype. Gear: Ares Predator (3 clips). Smashes the PANICBUTTON box outside "
            "and covers the entrance, herding stragglers inside. The one Chiller Thriller who might be "
            "talked down, flipped, or spared -- and the one the players may shoot by mistake (Timmy)."
        ),
    },
    {
        "name": "Willis Fabrizzi",
        "role": "'Wiley' -- manic Coyote shaman who climbs the shelves and howls",
        "archetype": "Street Shaman",
        "title": "\"Wiley\", Coyote shaman of the Chiller Thrillers",
        "race": "Human",
        "gender": "Male",
        "age": 19,
        "organization": "Chiller Thrillers",
        "connection": 1,
        "description": (
            "Wears a full-length synth-fur lined coat; greasy brown hair done up in a beehive of dirt, "
            "mud, feathers, twigs and small rocks; a bulging leather pouch on his belt and fetishes "
            "everywhere. A Coyote shaman, and manic. Tags along with Wendy during the robbery but follows "
            "her by clambering over the tops of the displays and shelves, howling in moments of excitement."
        ),
        "notes": (
            "Street Shaman archetype: Conjuring 2, Sorcery 6, the 10-point Fighter spell package at +1 "
            "Force because he casts with fetishes (four expendable fetishes per spell). Gear: "
            "Colt-American L36 pistol. Sally Tsung's target if the team cannot handle him; until he is "
            "down she maintains Spell Defense on the players."
        ),
    },
    {
        "name": "Sally Tsung",
        "role": "The gorgeous street mage with the sword from 'Night on the Town'; the scenario's equalizer",
        "archetype": "Street Mage",
        "title": "Street mage (the equalizer)",
        "race": "Human",
        "gender": "Female",
        "connection": 3,
        "description": (
            "The gorgeous mage with the sword from the core book's \"Night on the Town\" fiction, in the "
            "Stuffer Shack for a quick munch. Stays clear of the fighting but will not let the team die."
        ),
        "background": (
            "One of the best-known faces in the Seattle shadows. Her real stats are certainly better than "
            "the fighter-orientation Street Mage archetype the scenario uses for her."
        ),
        "notes": (
            "At the first sign of trouble she fades into the stockroom (area G). She maintains Spell "
            "Defense on the runners and, if they cannot handle Wiley, blows the Chiller Thrillers' shaman "
            "away herself. Once Wiley is down she ducks out the back door; if pursued she goes invisible "
            "and is long gone by the time the fight ends. A natural future contact or Mr. Johnson lead "
            "-- she has now seen the team work."
        ),
        "contact_skills": ["Magic (hermetic street mage), Spell Defense", "Seattle shadow scene"],
    },
    {
        "name": "Wanda",
        "role": "Stuffer Shack checkout clerk; orange hair cemented into a single spike",
        "archetype": "Corporate Wage Slave",
        "title": "Checkout clerk, Stuffer Shack",
        "race": "Human",
        "gender": "Female",
        "age": 22,
        "connection": 1,
        "description": (
            "Vapidly pretty, pale skin, orange hair cemented into a single spike (terminal mousse abuse). "
            "Reacts to events and comments a few seconds after they occur. Stands behind the checkout "
            "counter (area C)."
        ),
        "notes": "Squatter NPC profile. Frightened, passive victim during the robbery. Johnny the stock boy has a secret crush on her.",
    },
    {
        "name": "Mr. Nick",
        "role": "Stuffer Shack manager with a Defiance shotgun under his desk; will probably get killed",
        "archetype": "Corporate Wage Slave",
        "title": "Store manager, Stuffer Shack",
        "race": "Human",
        "gender": "Male",
        "age": 43,
        "connection": 1,
        "description": "Short and dumpy. Keeps a Defiance shotgun under his desk in the manager's office (area F).",
        "notes": (
            "Squatter NPC profile plus the shotgun. He is working in his office when the robbery begins "
            "and will try to ambush the robbers from his door -- and will probably get killed. If the "
            "runners save him he is a grateful (if cheap) friend at the local Shack."
        ),
    },
    {
        "name": "Johnny",
        "role": "Stuffer Shack stock boy, 17, stocking soup in Aisle Nine",
        "archetype": "Corporate Wage Slave",
        "title": "Stock boy, Stuffer Shack",
        "race": "Human",
        "gender": "Male",
        "age": 17,
        "connection": 1,
        "description": "Gangly and pimpled, close-cut blond hair, Stuffer Shack apron. Has a secret lust for Wanda. Stocking boxes of soup in Aisle Nine when the robbery begins.",
        "notes": "Squatter NPC profile. Frightened, passive victim.",
    },
    {
        "name": "Jacky Scatman",
        "role": "Would-be rocker king in white leathers and GoodAsGold jewelry; armed, shoots only in self-defense",
        "archetype": "Rocker",
        "title": "Would-be rocker (customer)",
        "race": "Human",
        "gender": "Male",
        "age": 32,
        "connection": 1,
        "description": (
            "A would-be rocker king in white leathers and several kilograms of GoodAsGold jewelry, buying "
            "pet food in Aisle Six with his wife Angie. Carries a Walther Palm-Pistol in a shoulder holster."
        ),
        "notes": "Squatter NPC profile. The Scatmans will not start a firefight; once shooting starts they shoot only in self-defense.",
    },
    {
        "name": "Angie Scatman",
        "role": "Would-be rocker queen: 42 zippers, eight meters of chain, a Beretta in the bag",
        "archetype": "Rocker",
        "title": "Would-be rocker (customer)",
        "race": "Human",
        "gender": "Female",
        "age": 27,
        "connection": 1,
        "description": (
            "A would-be rocker queen in a tight black leather jumpsuit with about 42 zippers, draped with "
            "some eight meters of heavy steel chain. Carries a Beretta Model 101T in her shoulder bag. In "
            "Aisle Six with Jacky, buying pet food."
        ),
        "notes": "Squatter NPC profile. Shoots only in self-defense.",
    },
]

ORG_UPDATES = {
    "Aztechnology": {
        "notes_append": (
            "Stuffer Shack, the 24-hour / 365-day supermarket chain, carries the Aztec-Mex cuisine line "
            "(\"Wussy\" to \"Meltdown\") with the Aztechnology step-pyramid logo on most products. The "
            "Food Fight robbery by the Chiller Thrillers is the runners' first brush with Stuffer Shack, "
            "Inc., whose gratitude for a prevented robbery never outweighs the property damage."
        ),
    },
    "Lone Star Security": {
        "notes_append": (
            "A Lone Star patrol will pull over runners who look armed for war on a trip to the corner "
            "store (Food Fight). Police statements are a permanent record -- \"Just what is your SIN, "
            "citizen?\" -- so runners clear out before the Badges arrive."
        ),
    },
}

LOC_UPDATES = {
    "Stuffer Shack - Redmond Barrens": {
        "description_append": (
            "The chain sells everything: Holohayo 3D greeting cards, pneumatic fluid for your bike, "
            "cheap fetish trinkets for magical wannabes, soymilk, soykaf, soygrits, and a full line of "
            "stuffers with no redeeming nutritional or social value. Open 24 hours a day, 365 days a year. "
            "Sixteen aisles (13 is overpriced Tribal-territory organics, 14 the freezer section, 15-16 "
            "under refurbishment with paint cans and bonding resin everywhere), a hardcopy book nook with "
            "NewsFax terminals (A), four simsense arcade games at 1 nuyen a minute (B: \"Orbital Ninja "
            "Death Commando\", \"Super Mareno Brothers LXXVIII\"), the checkout (C), Dispenser Bars for "
            "Shmoozies, Fizzygoo and Ludivenko Lovely Soya-Sloppies with the DoubleThick option (D), a "
            "locked electronics case (E), the manager's office (F), a stockroom whose door opens on the "
            "back alley (G), and the employee lounge (H)."
        ),
        "notes_append": (
            "The Food Fight store (move it to whichever Shack is in the team's home zone). Staff: Wanda "
            "(clerk), Mr. Nick (manager, Defiance shotgun under the desk), Johnny (stock boy). Regulars "
            "on the night: Mrs. Needles (33, obese, drives her cart down Aisle 11 like a Destructo Derby "
            "finalist, screams herself hoarse behind it) and her son Louis (8, streetwise urchin, "
            "smartmouth cracks all through the robbery); Timmy Thinners (29, over two meters, scrawny, "
            "tattered black leathers -- a dead ringer for the ganger Spike, scoping the audio players in "
            "area E); Jacky and Angie Scatman (armed would-be rockers in Aisle 6). Spotting a concealed "
            "weapon on any of them is Perception TN 8. Full map key at Corebook p.205; every miss rolls on "
            "the Food Fight Table and the floor becomes Difficult Terrain."
        ),
    },
}

NPC_UPDATES = {}

MATRIX_HOSTS = """
None. The Stuffer Shack's only electronics are the checkout terminal, the arcade rigs, and the
PANICBUTTON box outside (which Spike smashes). Nothing to build.
"""

NOT_BUILT = """
- **Mrs. Needles and Louis Needles, Timmy Thinners** -- bystander color; captured in the Stuffer Shack notes rather than as NPC rows.
- **Nicky Saitoh** (martial-arts simsense star Slicer Dicer copies), **Geist, Morgan, Skinner, Toshi** (the narrator's crew in the opening fiction), **Danny Danger** (rules example) -- name-drops only.
- **Stuffer Shack, Inc.** -- the chain is already represented as Aztechnology-front locations; no separate org.
- The **Food Fight Table** (Corebook p.206) -- a rules aid, referenced in the location notes.
"""

PLAY_NOTES = """
- Arrange the munchies beforehand with the player of the biggest, baddest character; getting to
  the Shack with a hunger-crazed troll in the back seat is half the fun.
- Sidearms only. Runners who look armed for war get a Lone Star patrol stop on the way.
- The gang wants to goad someone into starting it. The longer nobody does, the more abusive they get.
- Sally Tsung is the safety net; do not let her steal the fight. She takes Wiley only if the team cannot.
- Karma: 1 for surviving, 1 for the Chiller Thrillers being nasty opposition; individual awards on top.
"""
