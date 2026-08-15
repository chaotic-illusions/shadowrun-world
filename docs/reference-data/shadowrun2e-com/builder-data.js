/* =============================================================
   Character Builder reference data (SR2 core, FASA7901).
   Validated against: Master Character Creation Table p.45,
   Racial Maximum Table p.43, Racial Modifications Table p.45,
   Resources / Force Points p.46, derived-attribute rules p.45.
   Plus the PDF field-name map for assets/sr2-charsheet.pdf.
   ============================================================= */

/* Priority table — assign A–E once each across the five categories. */
window.SR2_PRIORITY = {
  race: {
    A: "Metahuman (Elf / Dwarf / Ork / Troll)",
    B: "Human", C: "Human", D: "Human", E: "Human",
  },
  magic: {
    A: "Full Magician (Human)",
    B: "Adept (Human) · or Full Magician (Metahuman)",
    C: "Adept (Metahuman)",
    D: "Mundane", E: "Mundane",
  },
  attributes: { A: 30, B: 24, C: 20, D: 17, E: 15 },
  skills:     { A: 40, B: 30, C: 24, D: 20, E: 17 },
  resources: {
    A: { nuyen: 1000000, fp: 50 },
    B: { nuyen: 400000,  fp: 35 },
    C: { nuyen: 90000,   fp: 25 },
    D: { nuyen: 5000,    fp: 15 },
    E: { nuyen: 500,     fp: 5 },
  },
};

/* Magic availability by race + magic priority (letter rank A=1 … E=5).
   You qualify if your Magic priority is at least as good as the threshold. */
window.SR2_MAGIC_RULES = {
  rank: { A: 1, B: 2, C: 3, D: 4, E: 5 },
  fullMage: { human: "A", metahuman: "B" },
  adept:    { human: "B", metahuman: "C" },
  startingMagic: 6,        // Magic Rating at chargen (Essence 6 → floor 6)
  spellForceMaxAtChargen: 6,
};

/* Shamanic totems (SR2 core, pp.120-122). A shaman MUST pick one at chargen
   (p.47: "if a shaman, what is its totem?"). Each gives spell-category dice
   bonuses, often a conjuring bonus for certain spirits, sometimes a penalty,
   and always a behavioural geas. Values transcribed directly from the book —
   these supersede the magic.html catalogue, which had several errors.
   Hermetic mages take no totem. */
window.SR2_TOTEMS = [
  { n: "Bear", env: "Forest", spells: "+2 dice to Health spells", spirits: "+2 dice conjuring Forest spirits", penalty: "",
    geas: "Berserker: when wounded, make a Willpower (4) test or go berserk and attack the nearest living thing with your deadliest weapon." },
  { n: "Cat", env: "Urban", spells: "+2 dice to Illusion spells", spirits: "+2 dice conjuring City spirits", penalty: "",
    geas: "Toys with prey: while unwounded, a Willpower (6) test is needed to cast a combat spell (else you cast the weakest you know). +1 TN to all tests while dirty or unkempt." },
  { n: "Coyote", env: "Anywhere", spells: "", spirits: "", penalty: "",
    geas: "The Trickster. No bonuses and no penalties — Coyote refuses to be limited by any rule, oath, or expectation, and lives by his own wits." },
  { n: "Dog", env: "Urban", spells: "+2 dice to Detection spells", spirits: "+2 dice conjuring Field & Hearth spirits", penalty: "",
    geas: "Single-minded loyalty: changing plans or tactics needs a Willpower (4) test and a Complex Action." },
  { n: "Eagle", env: "Mountains", spells: "+2 dice to Detection spells", spirits: "+2 dice conjuring Wind spirits", penalty: "",
    geas: "Will not tolerate evil or ignoble actions; a fierce defender of the land and the purity of nature." },
  { n: "Gator", env: "Swamp / River (or urban sewers)", spells: "+2 dice to Combat & Detection spells", spirits: "+2 dice conjuring Swamp/Lake/River spirits (City spirits if an urban totem)", penalty: "−1 die to Illusion spells",
    geas: "Lazy & greedy: breaking off a fight, chase, or other direct action needs a Willpower (6) test. Loathe to share or lend." },
  { n: "Lion", env: "Prairie", spells: "+2 dice to Combat spells", spirits: "+2 dice conjuring Prairie spirits", penalty: "−1 die to Health spells",
    geas: "Proud, direct warrior: strikes from a position of strength (surprise/ambush), holds strength in reserve, and disdains subtle or menial tasks." },
  { n: "Owl", env: "Anywhere (learns spells by night)", spells: "+2 dice to ALL Sorcery & Conjuring — night only", spirits: "", penalty: "",
    geas: "Creature of the night: +2 to ALL target numbers (even non-magical) in direct sunlight, and +2 TN to all magic during the daytime even when sheltered." },
  { n: "Raccoon", env: "Anywhere but desert", spells: "+2 dice to Manipulation spells", spirits: "+2 dice conjuring City spirits", penalty: "−1 die to Combat spells",
    geas: "Loner and insatiably curious — ignores danger in the pursuit of information. A proud thief who steals only the very best." },
  { n: "Rat", env: "Urban", spells: "+2 dice to Detection & Illusion spells", spirits: "+2 dice conjuring Spirits of Man", penalty: "−1 die to Combat spells",
    geas: "Dirty & furtive: dislikes open fighting, preferring spells from the shadows or a silenced pistol from a doorway." },
  { n: "Raven", env: "Open sky", spells: "+2 dice to Manipulation spells", spirits: "+2 dice conjuring Wind spirits", penalty: "−1 die to Combat spells",
    geas: "Gluttonous and conflict-averse (lets others fight). +1 to ALL target numbers whenever not under the open sky." },
  { n: "Shark", env: "On or by the sea", spells: "+2 dice to Combat & Detection spells", spirits: "+2 dice conjuring Sea spirits", penalty: "",
    geas: "Berserker (like Bear) when wounded or after a kill — Willpower (4) test. Believes the only good enemy is a dead one; strikes to kill." },
  { n: "Snake", env: "Anywhere except mountains", spells: "+2 dice to Illusion & Detection spells", spirits: "+2 dice conjuring one Spirit of the Land (wilderness) or one Spirit of Man (urban), your choice", penalty: "−1 die to spells cast during combat",
    geas: "Will not fight unless defending herself or hunting to eat. Obsessed with secrets and will take enormous risks to learn them." },
  { n: "Wolf", env: "Forest / Prairie / Mountain", spells: "+2 dice to Detection & Combat spells", spirits: "+2 dice conjuring Forest or Prairie spirits (your choice)", penalty: "",
    geas: "Fierce loyalty to friends and family unto death; never betrays a bond and never shows cowardice. Can go Berserker like Bear." },
];

/* Foci (SR2 core). Two costs at chargen, paid from two pools:
     • nuyen  — from the Resources nuyen budget (Magical Equipment Table, p.263)
     • Force Points — equal to the focus's bonding Karma (Focus Bonding Table,
       p.137); at chargen Force Points stand in for the bonding Karma.
   nuyen  = nuyenFlat, or nuyenBase + nuyenPer × Rating.
   karma  = karmaFlat, or karmaPer × Rating.  (karma is paid in Force Points.)
   who: "mage" = full magician only; "both" = magician or adept.
   Adepts may bond only Weapon Foci in SR2 core (p.138). */
window.SR2_FOCI = [
  { n: "Specific Spell Focus", who: "mage", rated: true, nuyenPer: 45000, karmaPer: 1,
    applies: "one specific spell", fx: "+Rating dice to that spell's Sorcery tests" },
  { n: "Spell Category Focus", who: "mage", rated: true, nuyenPer: 75000, karmaPer: 3,
    applies: "one spell category", fx: "+Rating dice to Sorcery tests for that whole category" },
  { n: "Spirit Focus", who: "mage", rated: true, nuyenPer: 60000, karmaPer: 2,
    applies: "one spirit type", fx: "+Rating dice to Conjuring that spirit type" },
  { n: "Power Focus", who: "mage", rated: true, nuyenPer: 105000, karmaPer: 5,
    applies: "", fx: "+Rating dice to the Magic Pool (helps every Magic test)" },
  { n: "Spell Lock", who: "mage", rated: false, nuyenFlat: 45000, karmaFlat: 1,
    applies: "one sustained spell", fx: "holds a sustained spell live without the caster maintaining it (Rating 1)" },
  { n: "Weapon Focus (Small)", who: "both", rated: true, nuyenBase: 100000, nuyenPer: 90000, karmaPer: 4,
    applies: "a Reach-0 melee weapon (knife, etc.)", fx: "the weapon counts as magical and adds +Rating dice to attacks" },
  { n: "Weapon Focus (Large)", who: "both", rated: true, nuyenBase: 200000, nuyenPer: 90000, karmaPer: 5,
    applies: "a Reach-1+ melee weapon (sword, staff, etc.)", fx: "the weapon counts as magical and adds +Rating dice to attacks" },
];

/* ============================================================
   MATRIX / DECKING (SR2 core Matrix chapter, pp.162-179;
   Hacking Pool & Detection Factor from Virtual Realities 2.0 p.18)
   ============================================================ */

/* Persona programs are firmware built into the deck (no active-memory cost).
   The four ratings TOGETHER cannot exceed 3 x the deck's MPCP. (SR2 p.174) */
window.SR2_PERSONA = [
  { n: "Bod", desc: "Persona Body — soaks Matrix damage and sets the TN that IC must beat to crash your deck." },
  { n: "Evasion", desc: "The persona's dodge — evades active IC and hostile system commands." },
  { n: "Masking", desc: "Hides the persona from detection/identification IC; half of your Detection Factor." },
  { n: "Sensors", desc: "Lets the persona perceive nodes, IC, and constructs in the Matrix." },
];

/* Utility programs (SR2 p.174-177). Memory size in Mp = Rating^2 x mult.
   SR2 has no flat purchase price — programs are written (Computer/Programming
   skill) or bought as object code from a deckmeister at GM-set prices, so the
   builder leaves nuyen editable (default 0) and tracks the real constraint:
   the deck's Active Memory. */
window.SR2_PROGRAMS = [
  { n: "Attack", type: "Combat", mult: 2, fx: "Your Matrix weapon — crashes hostile IC (Attack rating + Hacking Pool vs the IC's rating; each success fills one IC box)." },
  { n: "Slow", type: "Combat", mult: 4, fx: "Degrades a target IC, lowering its effective rating." },
  { n: "Medic", type: "Defense", mult: 4, fx: "Repairs damage to the persona/deck, clearing MPCP Condition Monitor boxes." },
  { n: "Shield", type: "Defense", mult: 4, fx: "Armor for the persona — reduces IC damage; degrades 1 point per Combat Turn it absorbs." },
  { n: "Mirrors", type: "Defense", mult: 3, fx: "Spins up decoy personas — adds its rating to your Evasion." },
  { n: "Smoke", type: "Defense", mult: 2, fx: "Raises IC target numbers to obscure you; degrades as it runs." },
  { n: "Analyze", type: "Sensor", mult: 3, fx: "Examines a node, IC, or construct to reveal ratings and identity." },
  { n: "Browse", type: "Sensor", mult: 1, fx: "Searches a datastore's contents for the file or paydata you want." },
  { n: "Decrypt", type: "Sensor", mult: 1, fx: "Defeats scramble/encryption protecting data or operations." },
  { n: "Evaluate", type: "Sensor", mult: 2, fx: "Assesses the street value of data you've located." },
  { n: "Sleaze", type: "Masking", mult: 3, fx: "Slips the persona past IC unseen — drives your Detection Factor; every serious decker runs one." },
  { n: "Deception", type: "Masking", mult: 2, fx: "Generates fake passcodes to fool IC and access gates." },
  { n: "Relocate", type: "Masking", mult: 2, fx: "Feeds trace IC a false location, defeating the trace." },
];

window.SR2_MATRIX = {
  personaCapMult: 3,                 // total persona ratings <= MPCP x 3 (SR2 p.174)
  activeMemPerMp: 5,                 // expand active memory at 5Y/Mp (SR2 p.172)
  activeMemCapMult: 50,              // ...up to MPCP x 50 Mp
  storagePerMp: 2.5,                 // storage expands at 2.5Y/Mp, no cap (SR2 p.172)
  responseIncrease: [100, 400, 900], // Response Increase Lv1/2/3 cost = MPCP^2 x this (SR2 p.173)
  // Hacking Pool   = floor((Intelligence + MPCP) / 3)   (VR2.0 p.18)
  // Detection Factor = ceil((Masking + Sleaze) / 2)     (VR2.0 p.18)
};

/* Metatypes — racial attribute modifiers, racial maximums, vision, notes.
   Maximums are the FINAL attribute caps (after modifiers). */
window.SR2_METATYPES = {
  Human: {
    mods: {},
    max: { body: 6, quickness: 6, strength: 6, charisma: 6, intelligence: 6, willpower: 6 },
    vision: "Normal", notes: [],
  },
  Elf: {
    mods: { quickness: 1, charisma: 2 },
    max: { body: 6, quickness: 7, strength: 6, charisma: 8, intelligence: 6, willpower: 6 },
    vision: "Low-Light", notes: [],
  },
  Dwarf: {
    mods: { body: 1, quickness: -1, strength: 2, willpower: 1 },
    max: { body: 7, quickness: 5, strength: 8, charisma: 6, intelligence: 6, willpower: 7 },
    vision: "Thermographic", notes: ["+2 dice to resist disease & toxins"],
  },
  Ork: {
    mods: { body: 3, strength: 2, charisma: -1, intelligence: -1 },
    max: { body: 9, quickness: 6, strength: 8, charisma: 5, intelligence: 5, willpower: 6 },
    vision: "Low-Light", notes: [],
  },
  Troll: {
    mods: { body: 5, quickness: -1, strength: 4, charisma: -2, intelligence: -2 },
    max: { body: 11, quickness: 5, strength: 10, charisma: 4, intelligence: 4, willpower: 5 },
    vision: "Thermographic", notes: ["+1 Reach (armed & unarmed)", "Dermal armor +1 (Body)"],
  },
};

/* Active skills for the builder pick-list (SR2). attr = linked attribute;
   group: combat | physical | technical | magic | social | vehicle | knowledge.
   In SR2 all skills (active, knowledge, etc.) are bought from the same
   Skills priority points; only native language is free (Intelligence + 2).
   conc = suggested Concentrations from the skill descriptions (SR2 p.70-73);
   the builder still lets you type a custom Concentration / Specialization. */
window.SR2_SKILLS = [
  { n: "Athletics", attr: "Quickness", group: "physical", conc: ["Running", "Climbing", "Lifting", "Jumping", "Swimming"] },
  { n: "Stealth", attr: "Quickness", group: "physical", conc: ["Urban", "Wilderness", "Farmland"] },
  { n: "Escape Artist", attr: "Quickness", group: "physical" },
  { n: "Armed Combat", attr: "Strength", group: "combat", conc: ["Edged Weapons", "Pole Arms/Staff", "Whips/Flails", "Clubs"] },
  { n: "Unarmed Combat", attr: "Strength", group: "combat", conc: ["Cyber-Implant Weaponry", "Aikido", "Boxing", "Judo", "Jiu-Jitsu", "Karate", "Kickboxing", "Muay Thai", "Ninjutsu", "Tae Kwon Do"] },
  { n: "Firearms", attr: "Quickness", group: "combat", conc: ["Pistols", "Rifles", "Submachine Guns", "Light Machine Guns", "Grenade Launchers", "Tasers"] },
  { n: "Projectile Weapons", attr: "Quickness", group: "combat", conc: ["Bows", "Crossbows"] },
  { n: "Throwing Weapons", attr: "Quickness", group: "combat", conc: ["Aerodynamic", "Non-Aerodynamic"] },
  { n: "Gunnery", attr: "Quickness", group: "combat", conc: ["Machine Guns", "Missile/Rocket Launchers", "Assault Cannon", "Vehicle-Mounted Cannon"] },
  { n: "Demolitions", attr: "Intelligence", group: "technical", conc: ["Commercial Explosives", "Plastic Explosives"] },
  { n: "Computer", attr: "Intelligence", group: "technical", conc: ["Hardware", "Software"] },
  { n: "Electronics", attr: "Intelligence", group: "technical", conc: ["Control Systems", "Electronic Warfare", "Maglocks", "Device Linking", "Diagnostics"] },
  { n: "Biotech", attr: "Intelligence", group: "technical", conc: ["Transimplant Surgery", "Organ Culture", "Replacement Construction", "Extended Care", "First Aid"] },
  { n: "Sorcery", attr: "Willpower", group: "magic", conc: ["Spellcasting", "Ritual Sorcery"] },
  { n: "Conjuring", attr: "Willpower", group: "magic", conc: ["Elementals", "Nature Spirits"] },
  { n: "Enchanting", attr: "Intelligence", group: "magic" },
  { n: "Etiquette", attr: "Charisma", group: "social", conc: ["Corporate", "Matrix", "Media", "Street", "Tribal"] },
  { n: "Interrogation", attr: "Charisma", group: "social", conc: ["Verbal", "Machine-Aided"] },
  { n: "Leadership", attr: "Charisma", group: "social", conc: ["Military", "Commercial"] },
  { n: "Negotiation", attr: "Charisma", group: "social", conc: ["Bargain", "Bribe", "Fast Talk"] },
  { n: "Instruction", attr: "Charisma", group: "social" },
  { n: "Bike", attr: "Reaction", group: "vehicle", conc: ["Two-wheeler", "Three-wheeler", "Racing", "Remote Operation"] },
  { n: "Car", attr: "Reaction", group: "vehicle", conc: ["Passenger Vehicle", "Truck", "Racing", "Remote Operation"] },
  { n: "Hovercraft", attr: "Reaction", group: "vehicle", conc: ["Passenger Craft", "Transport Craft", "Racing", "Remote Operation"] },
  { n: "Motorboat", attr: "Reaction", group: "vehicle", conc: ["Pleasure Craft", "Racing", "Remote Operation"] },
  { n: "Blimp", attr: "Reaction", group: "vehicle", conc: ["Pleasure Craft", "Transport Craft", "Remote Operation"] },
  { n: "Rotor Craft", attr: "Reaction", group: "vehicle", conc: ["Tilt-Rotor", "Fixed-Rotor", "Remote Operation"] },
  { n: "Winged Plane", attr: "Reaction", group: "vehicle", conc: ["Gliders", "Propellers", "Remote Operation"] },
  { n: "Vectored Thrust", attr: "Reaction", group: "vehicle", conc: ["Vertical Take-Off and Landing", "LAV Craft", "Remote Operation"] },
  { n: "Biology", attr: "Intelligence", group: "knowledge", conc: ["Zoology", "Botany", "Medicine", "Parazoology", "Parabotany"] },
  { n: "Computer Theory", attr: "Intelligence", group: "knowledge", conc: ["Hardware", "Software", "Matrix Theory"] },
  { n: "Cybertechnology", attr: "Intelligence", group: "knowledge", conc: ["Headware", "Bodyware"] },
  { n: "Physical Sciences", attr: "Intelligence", group: "knowledge", conc: ["Engineering", "Physics", "Chemistry", "Geology"] },
  { n: "Magical Theory", attr: "Willpower", group: "knowledge", conc: ["Design", "History"] },
  { n: "Military Theory", attr: "Willpower", group: "knowledge", conc: ["Military History", "Tactics"] },
  { n: "Psychology", attr: "Willpower", group: "knowledge", conc: ["Individual Behavior", "Group Behavior", "Deviant Behavior"] },
  { n: "Sociology", attr: "Willpower", group: "knowledge", conc: ["History", "Anthropology", "Archaeology"] },
  { n: "Firearms B/R", attr: "Intelligence", group: "br" },
  { n: "Gunnery B/R", attr: "Intelligence", group: "br" },
  { n: "Projectile Weapons B/R", attr: "Intelligence", group: "br" },
  { n: "Throwing Weapons B/R", attr: "Intelligence", group: "br" },
  { n: "Armed Combat B/R", attr: "Intelligence", group: "br" },
  { n: "Computer B/R", attr: "Intelligence", group: "br" },
  { n: "Electronics B/R", attr: "Intelligence", group: "br" },
  { n: "Biotech B/R", attr: "Intelligence", group: "br" },
  { n: "Ground Vehicle B/R", attr: "Intelligence", group: "br" },
  { n: "Boat B/R", attr: "Intelligence", group: "br" },
  { n: "Aircraft B/R", attr: "Intelligence", group: "br" },
];

/* Common 2050s languages for the chargen datalist (suggestions only — type any).
   English is the UCAS lingua franca; Sperethiel = Elvish, Or'zet = Ork/Troll.
   City Speak / Tunnel Talk are the typical Street-lifestyle dialects. */
window.SR2_LANGUAGES = [
  "English", "Japanese", "Sperethiel (Elvish)", "Or'zet (Orkish)", "German",
  "French", "Spanish", "Aztlaner Spanish", "Cantonese", "Mandarin", "Russian",
  "Italian", "Korean", "Salish", "Lakota", "Arabic", "Hindi", "Portuguese",
  "Latin", "City Speak", "Tunnel Talk", "Lingua Franca",
];

/* Sample contact archetypes from the SR2 Contacts chapter (p.202+) — suggestions. */
window.SR2_CONTACT_ARCHETYPES = [
  "Fixer", "Mr. Johnson", "Decker", "Street Doc", "Talismonger", "Fence",
  "Weapons Dealer", "Bartender", "Beat Cop", "Lone Star Officer", "Corporate Suit",
  "Rigger", "Smuggler", "Gang Member", "Squatter", "Shaman", "Mage", "Reporter",
  "Simsense Star", "Mafia Soldier", "Yakuza", "Mercenary", "Talislegger", "Dock Worker",
];

/* Archetype starter kits — sensible, editable starting points.
   gear/spells/powers reference catalogue names; the builder resolves
   them to live stats at load (so prices/effects stay in sync). */
window.SR2_ARCHETYPES = {
  streetsam: {
    name: "Street Samurai", blurb: "Chromed frontline shooter — Resources A for cyber, strong physicals.",
    prio: { resources: "A", attributes: "B", skills: "C", race: "D", magic: "E" },
    metatype: "Human", magicType: "Mundane",
    base: { body: 6, quickness: 6, strength: 4, charisma: 2, intelligence: 3, willpower: 3 },
    skills: [["Firearms", 6], ["Unarmed Combat", 4], ["Stealth", 5], ["Athletics", 4], ["Car", 3], ["Etiquette", 2]],
    spells: [], powers: [],
    gear: { weapons: ["Ares Predator", "AK-97"], armor: ["Armor Jacket"], cyber: ["Wired Reflexes", "Smartlink", "Datajack", "Dermal Plating"], other: ["Medkit"] },
  },
  combatmage: {
    name: "Combat Mage", blurb: "Full magician slinging combat spells — Magic A, no cyber to keep Magic 6.",
    prio: { magic: "A", attributes: "B", skills: "C", resources: "D", race: "E" },
    metatype: "Human", magicType: "Full Mage", tradition: "Hermetic",
    base: { body: 3, quickness: 5, strength: 2, charisma: 3, intelligence: 5, willpower: 6 },
    skills: [["Sorcery", 6], ["Conjuring", 4], ["Firearms", 4], ["Stealth", 4], ["Negotiation", 3], ["Athletics", 3]],
    spells: [["Mana Bolt", 3], ["Stun Bolt", 3], ["Heal", 3], ["Armor", 3], ["+2 Initiative Dice", 3]],
    powers: [],
    gear: { weapons: ["Ceska vz/120"], armor: ["Armor Vest"], cyber: [], other: ["Medkit"] },
  },
  decker: {
    name: "Decker", blurb: "Matrix runner — Resources A for a top deck, Skills B, brains over brawn.",
    prio: { resources: "A", skills: "B", attributes: "C", race: "D", magic: "E" },
    metatype: "Human", magicType: "Mundane",
    base: { body: 3, quickness: 2, strength: 2, charisma: 2, intelligence: 6, willpower: 5 },
    skills: [["Computer", 6], ["Electronics", 5], ["Firearms", 4], ["Stealth", 4], ["Negotiation", 4], ["Car", 3], ["Athletics", 4]],
    spells: [], powers: [],
    deck: "Fuchi Cyber-6",
    persona: { bod: 6, evasion: 6, masking: 6, sensors: 6 },
    programs: [["Attack", 6], ["Sleaze", 5], ["Analyze", 5], ["Deception", 4], ["Medic", 4], ["Browse", 5]],
    gear: { weapons: ["Ares Predator"], armor: ["Armor Vest"], cyber: ["Datajack", "Encephalon"], other: ["Pocket Secretary", "Medkit"] },
  },
  face: {
    name: "Face", blurb: "Elf social specialist — Race A for elf Charisma; talks the team in and out.",
    prio: { race: "A", attributes: "B", skills: "C", resources: "D", magic: "E" },
    metatype: "Elf", magicType: "Mundane",
    base: { body: 3, quickness: 4, strength: 2, charisma: 6, intelligence: 4, willpower: 5 },
    skills: [["Negotiation", 6], ["Etiquette", 5], ["Leadership", 4], ["Firearms", 3], ["Stealth", 3], ["Car", 3]],
    spells: [], powers: [],
    gear: { weapons: ["Ceska vz/120"], armor: ["Armor Clothing"], cyber: [], other: ["Pocket Secretary", "Medkit"] },
  },
  rigger: {
    name: "Rigger", blurb: "Vehicle & drone specialist — Resources A for rides, VCR-wired.",
    prio: { resources: "A", skills: "B", attributes: "C", race: "D", magic: "E" },
    metatype: "Human", magicType: "Mundane",
    base: { body: 2, quickness: 4, strength: 2, charisma: 2, intelligence: 6, willpower: 4 },
    skills: [["Car", 6], ["Gunnery", 5], ["Electronics", 5], ["Firearms", 4], ["Computer", 4], ["Stealth", 3], ["Athletics", 3]],
    spells: [], powers: [],
    gear: { weapons: ["Ares Predator"], armor: ["Armor Jacket"], cyber: ["Vehicle Control Rig", "Datajack"], vehicles: ["Eurocar Westwind 2000", "MCT-Nissan Roto-Drone", "Renraku Arachnoid Mini-Drone"], other: [] },
  },
  adept: {
    name: "Physical Adept", blurb: "Magic through the body — Magic B for adept powers, top physicals (Attributes A).",
    prio: { attributes: "A", magic: "B", skills: "C", resources: "D", race: "E" },
    metatype: "Human", magicType: "Adept",
    base: { body: 5, quickness: 6, strength: 5, charisma: 3, intelligence: 5, willpower: 6 },
    skills: [["Unarmed Combat", 6], ["Firearms", 4], ["Athletics", 5], ["Stealth", 5], ["Etiquette", 2], ["Car", 2]],
    spells: [], powers: ["Killing Hands", "Improved Ability", "Improved Physical Attributes"],
    gear: { weapons: ["Katana", "Ares Predator"], armor: ["Armor Clothing"], cyber: [], other: ["Medkit"] },
  },
};

window.SR2_ATTRS = ["body", "quickness", "strength", "charisma", "intelligence", "willpower"];
window.SR2_ATTR_LABEL = {
  body: "Body", quickness: "Quickness", strength: "Strength",
  charisma: "Charisma", intelligence: "Intelligence", willpower: "Willpower",
};

/* Constants & finishing-touch data. */
window.SR2_CHARGEN = {
  startEssence: 6,
  startKarmaPool: 1,      // SR2 starting Karma Pool
  startGoodKarma: 0,
  conditionBoxes: 10,
  attrFloor: 1,
  freeContacts: 2,
  contactCost: 5000,
  buddyCost: 10000,
  lifestyles: [           // monthly cost
    { name: "Street", cost: 0 },
    { name: "Squatter", cost: 100 },
    { name: "Low", cost: 1000 },
    { name: "Middle", cost: 5000 },
    { name: "High", cost: 10000 },
    { name: "Luxury", cost: 100000 },
  ],
  // Derived formulas (computed in builder.js):
  //   Reaction   = floor((Quickness + Intelligence) / 2)
  //   Initiative = Reaction + 1D6   (more dice from wired/boosted reflexes)
  //   CombatPool = floor((Quickness + Intelligence + Willpower) / 2)
  //   Magic      = floor(Essence)   for awakened; 0 for mundane
};

/* =============================================================
   PDF field-name map for assets/sr2-charsheet.pdf — our OWN
   original, fillable sheet (generated by build-charsheet.mjs).
   Clean field names; no quirky swapped boxes like the old sheet.
   ============================================================= */
(function () {
  const SKILLS = [];
  for (let n = 1; n <= 20; n++) SKILLS.push({ name: "sk" + n + "_n", rating: "sk" + n + "_r" });
  const SPELLS = [];
  for (let n = 1; n <= 11; n++) SPELLS.push({ name: "sp_n" + n, type: "sp_t" + n, drain: "sp_dr" + n, target: "sp_tg" + n, duration: "sp_du" + n, force: "sp_f" + n });
  const ARMOR = [];
  for (let n = 1; n <= 5; n++) ARMOR.push({ type: "ar_t" + n, rating: "ar_r" + n });
  const CYBER = [];
  for (let n = 1; n <= 12; n++) CYBER.push({ type: "cy_t" + n, rating: "cy_e" + n });
  const WEAPONS = [];
  for (let n = 1; n <= 12; n++) WEAPONS.push({ name: "w_n" + n, type: "w_t" + n, conceal: "w_c" + n, reach: "w_re" + n, mode: "w_m" + n, ammo: "w_am" + n, damage: "w_d" + n, modifiers: "w_mod" + n });
  const CONTACTS = [];
  for (let n = 1; n <= 14; n++) CONTACTS.push("c" + n);
  const GEAR = [];
  for (let n = 1; n <= 18; n++) GEAR.push("g" + n);

  window.SR2_PDFMAP = {
    identity: { name: "name", race: "metatype", sex: "sex", age: "age", description: "desc", note: "desc" },
    attributes: {
      body: "a_body", quickness: "a_qui", strength: "a_str",
      charisma: "a_cha", intelligence: "a_int", willpower: "a_wil",
      essence: "essence", magic: "magic",
    },
    derived: { reaction: "reaction", initiative: "initiative", combatPool: "pool_combat", karmaPool: "karma_pool", goodKarma: "good_karma" },
    pools: [
      { name: "pool1_n", value: "pool1_v" },
      { name: "pool2_n", value: "pool2_v" },
      { name: "pool3_n", value: "pool3_v" },
    ],
    deck: {
      type: "deck_type", persona: "deck_mpcp", hardening: "deck_hard", memory: "deck_amem",
      storage: "deck_store", load: "deck_load", io: "deck_io", response: "deck_resp",
      bod: "deck_bod", evasion: "deck_eva", masking: "deck_mask", sensors: "deck_sens",
    },
    vehicle: {
      type: "veh_type", handling: "veh_hand", speed: "veh_speed", body: "veh_body",
      armor: "veh_armor", signature: "veh_sig", pilot: "veh_pilot",
      firmpoints: "veh_firm", hardpoints: "veh_hard",
    },
    contacts: CONTACTS,
    gearList: GEAR,
    notes: "notes",
    skills: SKILLS,
    spells: SPELLS,
    armor: ARMOR,
    cyber: CYBER,
    weapons: WEAPONS,
  };
})();
