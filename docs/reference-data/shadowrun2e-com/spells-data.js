/* =============================================================
   Spell catalogue (219 entries) compiled from:
   - Shadowrun, Second Edition (FASA7901)   pp. 151-158  ( 79 spells)
   - Grimoire 2nd Edition (FASA7903)        pp. 126-132  ( 79 spells)
   - Awakenings (FASA7120)                  pp. 130-141  ( 61 spells)

   Field reference:
     n      - name
     cat    - combat | detection | health | illusion | manipulation
     typ    - M (Mana, vs living only) | P (Physical)
     rng    - LOS | T (Touch) | Area | Self
     dur    - I (Instant) | S (Sustained) | P (Permanent)
     drn    - drain code as printed, e.g. "[(F/2)+3]D"
     desc   - one-sentence original description
     effect - bullets of mechanical effect: damage, resistance,
              success scaling, duration nuances. Written so the
              card is self-contained at the table.
     src    - SR2 | GRIM | AWK
     pg     - printed page number

   For Combat spells, an automatic "> DAMAGE" line is rendered from
   the drain code's trailing letter (Power = Force, Damage Level
   = L/M/S/D, type from `typ`). The `effect` array adds nuance
   (area, special targeting, etc.).
   ============================================================= */

window.SR2_SPELLS = [

  /* ============== SR2 CORE -- Combat (p. 151) ============== */
  { n: "Fireball", cat: "combat", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+3]D",
    target: "Body", area: "Radius = Magic (m)", dmg: "(Force) Physical - Serious",
    desc: "Hurls a fiery blast across a wide area, scorching targets and igniting combustibles.",
    effect: [
      "Area effect: applies to every target inside the blast radius.",
      "Each target rolls Body vs Power (= Force) independently.",
      "Ignites flammable materials caught in the blast.",
      "Drain TN starts high -- risky to overcast at low Magic Rating."
    ],
    src: "SR2", pg: 151 },

  { n: "Hellblast", cat: "combat", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+6]D",
    target: "Body", area: "Radius = Magic (m)", dmg: "(Force) Physical - Deadly",
    desc: "Massively amplified fireball -- devastating range and force.",
    effect: [
      "Area effect with much larger radius than Fireball.",
      "Each target rolls Body vs Power (= Force).",
      "Drain TN is brutal -- typically reserved for prepared casts with Magic Pool backup.",
      "Ignites everything flammable in the blast zone."
    ],
    src: "SR2", pg: 151 },

  { n: "Mana Bolt", cat: "combat", typ: "M", rng: "LOS", dur: "I", drn: "(F/2)S",
    target: "Willpower", area: "Single", dmg: "(Force) Physical - Serious",
    desc: "A single bolt of raw mana savaging one living target's life force.",
    effect: [
      "Single-target. Affects living beings only.",
      "Target resists with Willpower vs Power (= Force).",
      "Each net success stages the damage up by one level."
    ],
    src: "SR2", pg: 151 },

  { n: "Mana Dart", cat: "combat", typ: "M", rng: "LOS", dur: "I", drn: "(F/2)L",
    target: "Willpower", area: "Single", dmg: "(Force) Physical - Light",
    desc: "A small mana dart for a light wound.",
    effect: [
      "Single-target, living-only.",
      "Low drain -- useful for plinking or finishing wounded enemies."
    ],
    src: "SR2", pg: 151 },

  { n: "Mana Missile", cat: "combat", typ: "M", rng: "LOS", dur: "I", drn: "(F/2)M",
    target: "Willpower", area: "Single", dmg: "(Force) Physical - Moderate",
    desc: "A moderate mana missile against a single living target.",
    effect: [
      "Single-target, living-only.",
      "Mid-range drain; the workhorse mid-tier mana attack."
    ],
    src: "SR2", pg: 151 },

  { n: "Manaball", cat: "combat", typ: "M", rng: "LOS", dur: "I", drn: "(F/2)S",
    target: "Willpower", area: "Radius = Magic (m)", dmg: "(Force) Physical - Serious",
    desc: "Sphere of mana bursting across an area, harming living things inside.",
    effect: [
      "Area effect, living targets only.",
      "Each target rolls Willpower vs Power (= Force) separately.",
      "Buildings, vehicles, drones: unaffected."
    ],
    src: "SR2", pg: 151 },

  { n: "Power Bolt", cat: "combat", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+1]S",
    target: "Body", area: "Single", dmg: "(Force) Physical - Serious",
    desc: "Bolt of magical energy that damages anything in line of sight.",
    effect: [
      "Single-target. Affects living AND inanimate matter (vs Manabolt's living-only).",
      "Target rolls Body vs Power (= Force).",
      "Higher drain than Manabolt -- the price of versatility."
    ],
    src: "SR2", pg: 151 },

  { n: "Power Dart", cat: "combat", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+1]L",
    target: "Body", area: "Single", dmg: "(Force) Physical - Light",
    desc: "Small physical dart of magical force for a light wound.",
    effect: [
      "Single-target. Affects anything in LOS.",
      "Low drain version of Power Bolt."
    ],
    src: "SR2", pg: 151 },

  { n: "Power Missile", cat: "combat", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+1]M",
    target: "Body", area: "Single", dmg: "(Force) Physical - Moderate",
    desc: "Moderate-damage physical missile.",
    effect: [
      "Single-target. Affects anything in LOS.",
      "Mid-range drain -- utility cast."
    ],
    src: "SR2", pg: 151 },

  { n: "Powerball", cat: "combat", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+1]S",
    target: "Body", area: "Radius = Magic (m)", dmg: "(Force) Physical - Serious",
    desc: "Sphere of magical force injuring everything in the blast.",
    effect: [
      "Area effect. Affects living AND inanimate.",
      "Each target rolls Body vs Power (= Force).",
      "Drain is moderate-to-heavy."
    ],
    src: "SR2", pg: 151 },

  { n: "Ram", cat: "combat", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+1]S",
    target: "Barrier Rating", area: "Single", dmg: "(Force) Physical - Serious - inanimate only",
    desc: "Battering blast of force that wrecks inanimate matter and ignores living tissue.",
    effect: [
      "Single-target.",
      "Affects ONLY inanimate matter -- living targets are untouched.",
      "Use to smash doors, walls, drones, vehicles."
    ],
    src: "SR2", pg: 151 },

  { n: "Sleep", cat: "combat", typ: "M", rng: "LOS", dur: "I", drn: "[(F/2)-1]S",
    target: "Willpower", area: "Radius = Magic (m)", dmg: "(Force) Stun - Serious",
    desc: "Drives living targets in an area into unconsciousness via accumulating Stun.",
    effect: [
      "Area effect, living targets only.",
      "Each target rolls Willpower vs Power (= Force).",
      "Stun damage -- knocks out rather than kills.",
      "Low drain TN for an area spell -- popular for non-lethal takedowns."
    ],
    src: "SR2", pg: 151 },

  /* ============== SR2 CORE -- Detection (p. 153) ============== */
  { n: "Analyze Device", cat: "detection", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+1]M",
    target: "4", area: "Single object",
    desc: "Reveals an object's purpose and operating procedure.",
    effect: [
      "Sustained: caster learns details while concentrating.",
      "Each success reveals one operating feature or function (how to fire, activate, defuse, etc.).",
      "Works on mundane and magical objects."
    ],
    src: "SR2", pg: 153 },

  { n: "Analyze Truth", cat: "detection", typ: "M", rng: "LOS", dur: "S", drn: "(F/2)S",
    target: "Willpower (R)", area: "Single subject",
    desc: "Lets the caster sense whether each statement a willing subject hears is sincerely believed true.",
    effect: [
      "Sustained.",
      "Caster perceives whether each statement made <em>to</em> the subject is sincerely believed by the speaker.",
      "Does NOT detect objective truth -- only the speaker's belief. Mistakes and delusions read as 'true'."
    ],
    src: "SR2", pg: 153 },

  { n: "Clairvoyance", cat: "detection", typ: "M", rng: "LOS", dur: "S", drn: "(F/2)M",
    target: "4", area: "Single (remote point)",
    desc: "Projects the caster's sight to a chosen distant point.",
    effect: [
      "Sustained. Caster's body becomes vulnerable while concentrating.",
      "Successes determine clarity and range -- more successes, sharper view at greater distance.",
      "Caster sees as if at the remote location; cannot hear (use Clairaudience for that)."
    ],
    src: "SR2", pg: 153 },

  { n: "Clairaudience", cat: "detection", typ: "M", rng: "LOS", dur: "S", drn: "(F/2)M",
    target: "4", area: "Single (remote point)",
    desc: "Projects the caster's hearing to a chosen distant point.",
    effect: [
      "Sustained.",
      "Successes determine clarity and range of remote audio.",
      "Pair with Clairvoyance for full surveillance."
    ],
    src: "SR2", pg: 153 },

  { n: "Combat Sense", cat: "detection", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+1]S",
    target: "4", area: "Single subject",
    desc: "Sharpens combat awareness on the touched subject.",
    effect: [
      "Sustained on one subject.",
      "Each net success adds 1 die to the subject's Combat Pool while the spell is active.",
      "Subject is never surprised -- gets a free Reaction Test against ambush.",
      "Touched subjects can be allies; targeting hostile would require resistance."
    ],
    src: "SR2", pg: 153 },

  { n: "Detect Enemies", cat: "detection", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+1]M",
    target: "4", area: "Within range",
    desc: "Senses any living being within range that currently intends harm to the subject.",
    effect: [
      "Sustained.",
      "Each net success reveals one hostile-intent being in range, including approximate direction and threat level.",
      "Range scales with Force x Magic Rating."
    ],
    src: "SR2", pg: 153 },

  { n: "Detect Individual", cat: "detection", typ: "M", rng: "LOS", dur: "S", drn: "(F/2)L",
    target: "10 - target's Magic/Essence", area: "Within range",
    desc: "Locates a single named / known person if within range.",
    effect: [
      "Sustained.",
      "Caster must know the target (name, image, recent encounter).",
      "Successes determine range and precision of the directional sense.",
      "Useful for tracking known runners or fugitives."
    ],
    src: "SR2", pg: 153 },

  { n: "Detect Life", cat: "detection", typ: "M", rng: "LOS", dur: "S", drn: "(F/2)L",
    target: "4", area: "Within range",
    desc: "Reveals every living being nearby.",
    effect: [
      "Sustained.",
      "Caster senses position and approximate count of all living things in range.",
      "Does not distinguish friend / foe / species -- just life."
    ],
    src: "SR2", pg: 153 },

  { n: "Detect (Life Form)", cat: "detection", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)-1]L",
    target: "4", area: "Within range",
    desc: "Variant homing in on one specific species of living being.",
    effect: [
      "Sustained.",
      "Caster picks the specific species (orks, dragons, ghouls, etc.) when learning the spell.",
      "Successes determine range and detail.",
      "Cheaper drain than Detect Life because of the narrower focus."
    ],
    src: "SR2", pg: 153 },

  { n: "Detect (Object)", cat: "detection", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+1]M",
    target: "4", area: "Within range",
    desc: "Locates a particular type of object -- guns, recording devices, drugs.",
    effect: [
      "Sustained.",
      "Caster picks the object class when learning the spell.",
      "Each success reveals one instance of that class in range.",
      "Used heavily by security mages scanning for contraband."
    ],
    src: "SR2", pg: 153 },

  { n: "Mind Probe", cat: "detection", typ: "M", rng: "T", dur: "S", drn: "[(F/2)+2]D",
    target: "Willpower (R)", area: "Single subject",
    desc: "Forces past a touched target's mental defenses to interrogate.",
    effect: [
      "Sustained. Caster must maintain contact and concentration.",
      "Each net success extracts one piece of information from the target (a memory, a name, a question's answer).",
      "Target rolls Willpower (and Magic Resistance if any) to oppose; net successes win.",
      "Target may be aware of the probe and remember the violation."
    ],
    src: "SR2", pg: 153 },

  { n: "Personal Combat Sense", cat: "detection", typ: "P", rng: "Self", dur: "S", drn: "[(F/2)+1]M",
    target: "4", area: "Self",
    desc: "Self-only version of Combat Sense.",
    effect: [
      "Sustained on caster only.",
      "Each net success adds 1 die to caster's Combat Pool.",
      "Caster is never surprised -- free Reaction Test against ambush.",
      "Lower drain than the targetable Combat Sense."
    ],
    src: "SR2", pg: 153 },

  /* ============== SR2 CORE -- Health (p. 154-155) ============== */
  { n: "Antidote L Toxin", cat: "health", typ: "P", rng: "T", dur: "P", drn: "(F/2)L",
    target: "Toxin Power", area: "Single subject",
    desc: "Neutralizes a mild ingested or inhaled poison.",
    effect: [
      "Permanent -- once neutralized, the toxin is gone.",
      "Successes determine effectiveness -- typically each success removes one level of toxin severity.",
      "Useful for casual food / drink poisoning."
    ],
    src: "SR2", pg: 154 },

  { n: "Antidote M Toxin", cat: "health", typ: "P", rng: "T", dur: "P", drn: "(F/2)M",
    target: "Toxin Power", area: "Single subject",
    desc: "Counters a moderate-strength toxin coursing through the touched subject's body.",
    effect: [
      "Permanent.",
      "Successes reduce toxin severity; sufficient successes neutralize entirely.",
      "Use within the toxin's effect window."
    ],
    src: "SR2", pg: 154 },

  { n: "Antidote S Toxin", cat: "health", typ: "P", rng: "T", dur: "P", drn: "(F/2)S",
    target: "Toxin Power", area: "Single subject",
    desc: "Purges a serious-rated poison before it can do worse.",
    effect: [
      "Permanent.",
      "Higher drain matches the toxin's danger.",
      "Successes are crucial -- partial neutralization leaves residual damage."
    ],
    src: "SR2", pg: 154 },

  { n: "Antidote D Toxin", cat: "health", typ: "P", rng: "T", dur: "P", drn: "(F/2)D",
    target: "Toxin Power", area: "Single subject",
    desc: "Wipes out even a deadly toxin from the subject's system.",
    effect: [
      "Permanent.",
      "Critical for nerve agents, military toxins, and bioweapons.",
      "Brutal drain -- Force > Magic risks Physical Drain."
    ],
    src: "SR2", pg: 154 },

  { n: "Cure L Disease", cat: "health", typ: "P", rng: "T", dur: "P", drn: "(F/2)L",
    target: "Disease virulence", area: "Single subject",
    desc: "Eliminates a mild infectious disease.",
    effect: [
      "Permanent.",
      "Successes determine speed and completeness of cure.",
      "Useful for street-clinic infections, flu, mild parasites."
    ],
    src: "SR2", pg: 154 },

  { n: "Cure M Disease", cat: "health", typ: "P", rng: "T", dur: "P", drn: "(F/2)M",
    target: "Disease virulence", area: "Single subject",
    desc: "Burns a moderate disease out of the subject's system.",
    effect: [
      "Permanent.",
      "Successes accelerate the cure; partial casts may leave the subject still ill."
    ],
    src: "SR2", pg: 154 },

  { n: "Cure S Disease", cat: "health", typ: "P", rng: "T", dur: "P", drn: "(F/2)S",
    target: "Disease virulence", area: "Single subject",
    desc: "Eradicates a serious pathogen.",
    effect: [
      "Permanent.",
      "Necessary for diseases that would otherwise kill -- VITAS variants, infectious bioweapons, severe parasites."
    ],
    src: "SR2", pg: 154 },

  { n: "Cure D Disease", cat: "health", typ: "P", rng: "T", dur: "P", drn: "(F/2)D",
    target: "Disease virulence", area: "Single subject",
    desc: "Wipes a lethal disease from the subject before it can finish them.",
    effect: [
      "Permanent.",
      "Last-resort cast for terminal infections.",
      "Drain matches the danger -- Force > Magic = Physical Drain."
    ],
    src: "SR2", pg: 154 },

  { n: "Decrease -1 Attribute", cat: "health", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+1]L",
    target: "10 - target Essence (R)", area: "Single subject",
    desc: "Suppresses one of the victim's natural Attributes by a point.",
    effect: [
      "Sustained: caster must maintain concentration (+2 TN to all other tests).",
      "Target rolls Willpower vs Power (= Force) to resist.",
      "Applies a -1 modifier to one specified Attribute on success.",
      "Cannot reduce an Attribute below 1."
    ],
    src: "SR2", pg: 154 },

  { n: "Decrease -2 Attribute", cat: "health", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+1]M",
    target: "10 - target Essence (R)", area: "Single subject",
    desc: "Saps two points from one of the victim's natural Attributes.",
    effect: [
      "Sustained.",
      "Target rolls Willpower vs Power.",
      "-2 modifier on success.",
      "Stacks with other Decrease spells if multiple are cast separately."
    ],
    src: "SR2", pg: 154 },

  { n: "Decrease -3 Attribute", cat: "health", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+1]S",
    target: "10 - target Essence (R)", area: "Single subject",
    desc: "Severely weakens by lowering an Attribute three points.",
    effect: [
      "Sustained.",
      "Target rolls Willpower vs Power.",
      "-3 modifier on success -- dramatic effect on rolls."
    ],
    src: "SR2", pg: 154 },

  { n: "Decrease -4 Attribute", cat: "health", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+1]D",
    target: "10 - target Essence (R)", area: "Single subject",
    desc: "Crushes one of the victim's Attributes by four points.",
    effect: [
      "Sustained.",
      "Target rolls Willpower.",
      "-4 -- catastrophic.",
      "Very high drain -- magicians often pair with Spell Defense / Centering."
    ],
    src: "SR2", pg: 154 },

  { n: "Detox L Toxin", cat: "health", typ: "P", rng: "T", dur: "P", drn: "[(F/2)-2]L",
    target: "Toxin Power", area: "Single subject",
    desc: "Eases out the lingering effects of a mild drug.",
    effect: [
      "Permanent.",
      "Use for hangovers, mild intoxication, residual drug effects.",
      "Very low drain -- utility cast."
    ],
    src: "SR2", pg: 154 },

  { n: "Detox M Toxin", cat: "health", typ: "P", rng: "T", dur: "P", drn: "[(F/2)-2]M",
    target: "Toxin Power", area: "Single subject",
    desc: "Flushes a moderate-strength substance from the subject's body.",
    effect: [
      "Permanent.",
      "Successes determine how quickly the drug is cleared."
    ],
    src: "SR2", pg: 154 },

  { n: "Detox S Toxin", cat: "health", typ: "P", rng: "T", dur: "P", drn: "[(F/2)-2]S",
    target: "Toxin Power", area: "Single subject",
    desc: "Cleans a serious dose of intoxicant out of the bloodstream.",
    effect: [
      "Permanent.",
      "For overdoses, combat stims, dangerous narcotics."
    ],
    src: "SR2", pg: 154 },

  { n: "Detox D Toxin", cat: "health", typ: "P", rng: "T", dur: "P", drn: "[(F/2)-2]D",
    target: "Toxin Power", area: "Single subject",
    desc: "Forces a near-lethal dose of substance out of the body.",
    effect: [
      "Permanent.",
      "Critical for lethal overdose scenarios.",
      "High drain matches the rescue's importance."
    ],
    src: "SR2", pg: 154 },

  { n: "Increase +1 Attribute", cat: "health", typ: "P", rng: "T", dur: "S", drn: "[(F/2)+2]L",
    target: "2 x affected Attribute", area: "Single subject",
    desc: "Pumps up one of the subject's natural Attributes by a point.",
    effect: [
      "Sustained on a willing subject (concentration penalty applies to caster).",
      "Adds +1 to one chosen Attribute for the duration.",
      "Cannot exceed 1.5 x Racial Maximum.",
      "Voluntary -- no resistance from target."
    ],
    src: "SR2", pg: 154 },

  { n: "Increase +2 Attribute", cat: "health", typ: "P", rng: "T", dur: "S", drn: "[(F/2)+2]M",
    target: "2 x affected Attribute", area: "Single subject",
    desc: "Bolsters one Attribute by two points.",
    effect: [
      "Sustained on willing subject.",
      "+2 to chosen Attribute.",
      "Cap: 1.5 x Racial Maximum."
    ],
    src: "SR2", pg: 154 },

  { n: "Increase +3 Attribute", cat: "health", typ: "P", rng: "T", dur: "S", drn: "[(F/2)+2]S",
    target: "2 x affected Attribute", area: "Single subject",
    desc: "Lifts one Attribute by three points.",
    effect: [
      "Sustained.",
      "+3 to chosen Attribute.",
      "Cap: 1.5 x Racial Maximum."
    ],
    src: "SR2", pg: 154 },

  { n: "Increase +4 Attribute", cat: "health", typ: "P", rng: "T", dur: "S", drn: "[(F/2)+2]D",
    target: "2 x affected Attribute", area: "Single subject",
    desc: "Floods the subject with magical vigor -- +4 to a natural Attribute.",
    effect: [
      "Sustained.",
      "+4 to chosen Attribute.",
      "Cap: 1.5 x Racial Maximum.",
      "Drain is brutal -- typically locked into a Spell Lock for combat use."
    ],
    src: "SR2", pg: 154 },

  { n: "Increase +1 Cybered Attribute", cat: "health", typ: "P", rng: "T", dur: "S", drn: "[(F/2)+3]L",
    target: "2 x affected Attribute", area: "Single subject",
    desc: "Raises an Attribute already augmented by cyberware by one more point.",
    effect: [
      "Sustained.",
      "+1 on top of cyberware enhancements (Wired Reflexes Reaction, Muscle Replacement Strength, etc.).",
      "Drain TN is one step higher than the natural version."
    ],
    src: "SR2", pg: 155 },

  { n: "Increase +2 Cybered Attribute", cat: "health", typ: "P", rng: "T", dur: "S", drn: "[(F/2)+3]M",
    target: "2 x affected Attribute", area: "Single subject",
    desc: "Stacks two more points onto a cyber-boosted Attribute.",
    effect: [
      "Sustained.",
      "+2 on top of cyberware bonuses.",
      "Useful for hybrid sam-mage builds when allowed."
    ],
    src: "SR2", pg: 155 },

  { n: "Increase +3 Cybered Attribute", cat: "health", typ: "P", rng: "T", dur: "S", drn: "[(F/2)+3]S",
    target: "2 x affected Attribute", area: "Single subject",
    desc: "Three more points on top of cyber-augmented baseline.",
    effect: [
      "Sustained.",
      "+3 above cybered rating.",
      "Drain is significant."
    ],
    src: "SR2", pg: 155 },

  { n: "Increase +4 Cybered Attribute", cat: "health", typ: "P", rng: "T", dur: "S", drn: "[(F/2)+3]D",
    target: "2 x affected Attribute", area: "Single subject",
    desc: "Four more points on top of cybernetic enhancement -- extreme boost.",
    effect: [
      "Sustained.",
      "+4 above cybered rating.",
      "Drain is severe -- Force > Magic = Physical Drain."
    ],
    src: "SR2", pg: 155 },

  { n: "+1 Initiative Die", cat: "health", typ: "M", rng: "T", dur: "S", drn: "(F/2)M",
    target: "2 x Reaction", area: "Single subject",
    desc: "Quickens the subject's reflexes -- one extra initiative die per turn.",
    effect: [
      "Sustained on touched subject.",
      "Adds 1 to the subject's initiative dice while active.",
      "Voluntary -- no resistance.",
      "Typically locked into a Spell Lock to avoid concentration penalty."
    ],
    src: "SR2", pg: 155 },

  { n: "+2 Initiative Dice", cat: "health", typ: "M", rng: "T", dur: "S", drn: "(F/2)S",
    target: "2 x Reaction", area: "Single subject",
    desc: "Adds two initiative dice to the subject.",
    effect: [
      "Sustained.",
      "+2 init dice while active.",
      "Heavy drain -- but matches Wired 2 cyberware bonus without Essence cost."
    ],
    src: "SR2", pg: 155 },

  { n: "+3 Initiative Dice", cat: "health", typ: "M", rng: "T", dur: "S", drn: "(F/2)D",
    target: "2 x Reaction", area: "Single subject",
    desc: "Hyper-accelerates reflexes -- three extra initiative dice.",
    effect: [
      "Sustained.",
      "+3 init dice (cyber-Reflexes 3 equivalent, no Essence cost).",
      "Drain D -- sustaining without a Spell Lock crushes the caster."
    ],
    src: "SR2", pg: 155 },

  { n: "Treat", cat: "health", typ: "M", rng: "T", dur: "P", drn: "(F/2)(Wound)",
    target: "8 - target Essence", area: "Single subject",
    desc: "Stabilizes and partially mends an injured subject -- only works soon after the injury.",
    effect: [
      "Permanent: damage healed stays healed.",
      "Each success heals 1 box of damage (Stun or Physical).",
      "Must be cast within Force minutes of the injury -- otherwise use Heal.",
      "Drain TN scales with the wound level being treated: (F/2) + level number (3 / 5 / 8 / 10 for L/M/S/D)."
    ],
    src: "SR2", pg: 155 },

  { n: "Heal", cat: "health", typ: "M", rng: "T", dur: "P", drn: "(F/2)(Wound)M",
    target: "10 - target Essence", area: "Single subject",
    desc: "Closes wounds on a subject, even hours after the injury.",
    effect: [
      "Permanent: damage stays healed.",
      "<strong>Each success on the Spell Success Test heals 1 box of damage</strong> (Stun or Physical) on the touched subject.",
      "Drain TN scales with the wound's severity: (F/2) + wound level number (3 / 5 / 8 / 10 for L/M/S/D).",
      "<strong>No time limit</strong> -- can heal injuries days old (vs Treat, which requires minutes-fresh wounds).",
      "Cannot exceed the subject's Body in successes for a single cast."
    ],
    src: "SR2", pg: 155 },

  /* ============== SR2 CORE -- Illusion (p. 155-156) ============== */
  { n: "Chaos", cat: "illusion", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]M",
    target: "Intelligence (R)", area: "Single subject",
    desc: "Bombards a target's senses with random illusions.",
    effect: [
      "Sustained, single-target.",
      "Target rolls Willpower vs Power (= Force) to disbelieve.",
      "Failure: target suffers TN penalty to all sensory tests (+ disorientation).",
      "Physical illusion: also fools cameras and sensors."
    ],
    src: "SR2", pg: 155 },

  { n: "Chaotic World", cat: "illusion", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]S",
    target: "Intelligence (R)", area: "Within range",
    desc: "Area Chaos -- overwhelms every sense for everyone caught inside.",
    effect: [
      "Sustained, area effect.",
      "Each target inside rolls Willpower vs Power to disbelieve.",
      "Heavy combat-disrupting field -- useful for cover or escape."
    ],
    src: "SR2", pg: 155 },

  { n: "Confusion", cat: "illusion", typ: "M", rng: "LOS", dur: "S", drn: "(F/2)S",
    target: "Willpower (R)", area: "Single subject",
    desc: "Weaves disorienting illusions directly in one target's mind.",
    effect: [
      "Sustained, single-target. Mana spell -- living only.",
      "Target rolls Willpower vs Power.",
      "Failure: target acts erratically, suffers test penalties.",
      "Lower drain than Chaos because mana-only."
    ],
    src: "SR2", pg: 155 },

  { n: "Entertainment", cat: "illusion", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+1]L",
    target: "-- (voluntary)", area: "Within range",
    desc: "Obvious area illusion designed for viewing -- magical sideshow.",
    effect: [
      "Sustained, area effect.",
      "Caster shapes the visuals; pre-designed scenes work best.",
      "Mana illusion -- works on living observers only.",
      "Common for street performances, distraction, urban shamanism."
    ],
    src: "SR2", pg: 156 },

  { n: "Improved Invisibility", cat: "illusion", typ: "P", rng: "T", dur: "S", drn: "[(F/2)+1]M",
    target: "Perception to detect", area: "Single subject",
    desc: "Makes the subject invisible to living and electronic observers.",
    effect: [
      "Sustained on touched subject.",
      "Each observer rolls Willpower vs Power to spot the subject.",
      "Physical illusion: cameras, sensors, drones also fooled.",
      "Premier infiltration buff -- typically locked into a Spell Lock."
    ],
    src: "SR2", pg: 156 },

  { n: "Invisibility", cat: "illusion", typ: "M", rng: "T", dur: "S", drn: "(F/2)M",
    target: "Perception to detect", area: "Single subject",
    desc: "Hides the subject from living observers; tech can still detect them.",
    effect: [
      "Sustained.",
      "Observer rolls Willpower vs Power to perceive.",
      "Mana illusion -- cameras and electronic sensors are NOT fooled (use Improved Invisibility for tech).",
      "Cheaper drain than Improved Invisibility."
    ],
    src: "SR2", pg: 156 },

  { n: "Mask", cat: "illusion", typ: "M", rng: "T", dur: "S", drn: "(F/2)L",
    target: "Perception to detect", area: "Single subject",
    desc: "Cloaks the subject in an illusory disguise.",
    effect: [
      "Sustained.",
      "Subject appears as another person (chosen at cast time).",
      "Observer rolls Willpower vs Power to see through.",
      "Mana illusion -- doesn't fool cameras (see Physical Mask in Grimoire 2e)."
    ],
    src: "SR2", pg: 156 },

  { n: "Stimulation", cat: "illusion", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+1]L",
    target: "-- (voluntary)", area: "Single subject",
    desc: "Fills a willing subject's senses with a vivid imagined experience.",
    effect: [
      "Sustained, voluntary subject.",
      "Caster designs the sensory experience -- sight, sound, smell, touch.",
      "Useful for entertainment, therapy, or covertly sharing visions."
    ],
    src: "SR2", pg: 156 },

  { n: "Stink", cat: "illusion", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+1]S",
    target: "Willpower (R)", area: "Within range",
    desc: "Fills an area with a vile imagined odor that drives bystanders away.",
    effect: [
      "Sustained, area effect.",
      "Each living target rolls Willpower vs Power to resist.",
      "Failure: target wants to leave the area; TN penalties to concentrate inside.",
      "Mana illusion -- no effect on cyber noses or sensors."
    ],
    src: "SR2", pg: 156 },

  /* ============== SR2 CORE -- Manipulation (p. 156-158) ============== */
  { n: "Control Actions", cat: "manipulation", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+2]S",
    target: "Willpower (R)", area: "Single subject",
    desc: "Hijacks the target's body to perform actions of the caster's choice.",
    effect: [
      "Sustained.",
      "Opposed Willpower test (caster's net successes determine control).",
      "Caster directs physical actions only -- not thoughts or beliefs.",
      "Target retains awareness; can recognize the control later."
    ],
    src: "SR2", pg: 156 },

  { n: "Control Emotion", cat: "manipulation", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+2]M",
    target: "Willpower (R)", area: "Single subject",
    desc: "Forces an overpowering mood onto a victim.",
    effect: [
      "Sustained.",
      "Target rolls Willpower vs Power.",
      "Caster picks the emotion: love, hate, fear, calm, despair.",
      "Subtler than Control Thoughts -- target acts in line with the new emotion."
    ],
    src: "SR2", pg: 156 },

  { n: "Control Thoughts", cat: "manipulation", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+2]D",
    target: "Willpower (R)", area: "Single subject",
    desc: "Reduces the victim to a puppet whose every thought is the caster's.",
    effect: [
      "Sustained.",
      "Opposed Willpower test.",
      "Caster dictates the target's reasoning -- total mind control.",
      "Brutal drain; sustaining is dangerous without Spell Lock + Centering."
    ],
    src: "SR2", pg: 157 },

  { n: "Hibernate", cat: "manipulation", typ: "P", rng: "T", dur: "S", drn: "(F/2)S",
    target: "4 (voluntary)", area: "Single subject",
    desc: "Drops a touched subject into a slow-breathing suspended state.",
    effect: [
      "Sustained on willing subject.",
      "Metabolism slows; injuries, hunger, thirst progress at a fraction of normal speed.",
      "Subject is unconscious / immobile while in hibernation.",
      "Useful for long transport, dire wounds, suspended-animation tactics."
    ],
    src: "SR2", pg: 157 },

  { n: "Levitate Item", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+1]L",
    target: "4", area: "Single object",
    desc: "Lifts an inanimate object through the air at the caster's command.",
    effect: [
      "Sustained.",
      "Force x Magic Rating determines maximum liftable mass (rough guideline).",
      "Caster directs the object mentally; speed and finesse scale with successes.",
      "Object Resistance for bound / warded items applies."
    ],
    src: "SR2", pg: 157 },

  { n: "Levitate Person", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+1]M",
    target: "4 (Willpower if unwilling)", area: "Single subject",
    desc: "Hoists a living being into the air and steers them against gravity.",
    effect: [
      "Sustained.",
      "Voluntary subject: caster directs movement.",
      "Hostile target: Body Resistance Test vs Power.",
      "Force x Magic determines lifting capacity / speed."
    ],
    src: "SR2", pg: 157 },

  { n: "Magic Fingers", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]M",
    target: "4", area: "Single object",
    desc: "Conjures invisible telekinetic hands.",
    effect: [
      "Sustained.",
      "Effective Strength = Force.",
      "Can grab, manipulate, throw, even attack -- uses caster's relevant Skill at -2 dice.",
      "Hands are invisible; observers see objects moving on their own."
    ],
    src: "SR2", pg: 157 },

  { n: "Poltergeist", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+1]S",
    target: "4", area: "Within range", dmg: "(Force) Physical - Light",
    desc: "Hurls every small loose object in an area at the targets.",
    effect: [
      "Sustained, area effect.",
      "Chaotic damage to anyone caught in the area; Power = Force.",
      "Each target rolls Body to resist damage.",
      "Requires loose objects in the area -- empty rooms produce nothing."
    ],
    src: "SR2", pg: 157 },

  { n: "Armor", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]M",
    target: "4 (voluntary)", area: "Single subject",
    desc: "Knits a magical armor layer onto the subject's clothes.",
    effect: [
      "Sustained.",
      "Each net success adds 1 point of Ballistic and Impact armor.",
      "Stacks with worn armor and Dermal Plating.",
      "Subject's armor visible as a faint shimmer; not concealable."
    ],
    src: "SR2", pg: 158 },

  { n: "Barrier", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]S",
    target: "4", area: "Created barrier",
    desc: "Conjures a wall of magical force that blocks attacks and passage.",
    effect: [
      "Sustained.",
      "Barrier Rating = Force; attacks must beat that to penetrate.",
      "Shapes: wall, dome, ring. Caster chooses dimensions within Force x Magic limit.",
      "Stops both physical and astral movement through it (unlike Mana Barrier)."
    ],
    src: "SR2", pg: 158 },

  { n: "Mana Barrier", cat: "manipulation", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+1]S",
    target: "6", area: "Created barrier",
    desc: "Barrier that stops only living beings, magic, and astral travelers -- ignores matter.",
    effect: [
      "Sustained.",
      "Barrier Rating = Force, applied vs living beings / spells / spirits / astral travelers.",
      "Physical matter (bullets, walls, drones) passes through.",
      "Useful for warding a room against magical intrusion without blocking sight."
    ],
    src: "SR2", pg: 158 },

  { n: "Ignite", cat: "manipulation", typ: "P", rng: "LOS", dur: "P", drn: "[(F/2)+1]D",
    target: "4", area: "Single target", dmg: "Fire -- ongoing",
    desc: "Heats a chosen object until it bursts into flame.",
    effect: [
      "Permanent: the fire, once started, continues naturally.",
      "Caster picks a target object; flammable objects ignite, less-flammable just heat.",
      "Object Resistance applies; some materials resist outright.",
      "Drain D -- very expensive for a sustained-fire effect."
    ],
    src: "SR2", pg: 158 },

  { n: "Flame Bomb", cat: "manipulation", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+1]D",
    target: "Body", area: "Within range", dmg: "(Force) Physical - Moderate",
    desc: "Bursts a blast of flames at a chosen point.",
    effect: [
      "Instant, area effect.",
      "Each target in the blast rolls Body vs Power (= Force).",
      "Ignites flammables in the area; lingering fires may persist.",
      "Damage Level taken from drain code letter (D = Deadly)."
    ],
    src: "SR2", pg: 158 },

  { n: "Flamethrower", cat: "manipulation", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+1]S",
    target: "Body", area: "Single (stream)", dmg: "(Force) Physical - Serious",
    desc: "Sprays a jet of fire from the caster.",
    effect: [
      "Instant, narrow cone effect.",
      "Single-target damage (or short cone -- see GM ruling).",
      "Target rolls Body vs Power.",
      "Ignites flammables in the line."
    ],
    src: "SR2", pg: 158 },

  { n: "Ice Sheet", cat: "manipulation", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+1]S",
    target: "4", area: "Sheet = Magic (m2)",
    desc: "Coats the ground with a wide slick of ice.",
    effect: [
      "Instant -- the ice forms, then exists naturally.",
      "Area: anyone moving across rolls Quickness against TN to stay upright.",
      "Slows movement, may cause falls.",
      "Persists until ice melts (Force x 5 minutes typically)."
    ],
    src: "SR2", pg: 158 },

  { n: "Light", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]M",
    target: "4", area: "Within range",
    desc: "Creates a floating point of light illuminating an area.",
    effect: [
      "Sustained.",
      "Illumination strength scales with Force -- equivalent to a strong flashlight or floodlight.",
      "Caster can move the light within sight; no physical bulb to break.",
      "Counter to Shadow."
    ],
    src: "SR2", pg: 158 },

  { n: "Shadow", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]M",
    target: "4", area: "Within range",
    desc: "Pools deep gloom across an area.",
    effect: [
      "Sustained.",
      "Anyone inside suffers Vision penalty modifiers proportional to Force.",
      "Useful for combat cover and stealth.",
      "Counter to Light."
    ],
    src: "SR2", pg: 158 },

  { n: "Spark", cat: "manipulation", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+1]M",
    target: "Body", area: "Single target", dmg: "(Force) Physical - Moderate",
    desc: "Snaps a small jolt of electricity at a target.",
    effect: [
      "Instant, single-target.",
      "Target rolls Body vs Power.",
      "Damage Level M (Moderate); can short out electronics on a critical."
    ],
    src: "SR2", pg: 158 },

  /* ============== Grimoire 2e -- Combat (p. 126-127) ============== */
  { n: "Death Touch", cat: "combat", typ: "M", rng: "T", dur: "I", drn: "[(F/2)-1]S",
    target: "Willpower (R)", area: "Single subject", dmg: "(Force) Physical - Serious - living only",
    desc: "Close-quarters mana strike requiring skin contact.",
    effect: [
      "Touch range -- caster must make an Unarmed Combat or Touch attack.",
      "Target rolls Willpower vs Power.",
      "Living targets only.",
      "Low drain because of the touch requirement."
    ],
    src: "GRIM", pg: 126 },

  { n: "Fire Bolt", cat: "combat", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+1]D",
    target: "Body", area: "Single target", dmg: "(Force) Physical - Serious - fire",
    desc: "Bolt of fire that punches into a target with serious force.",
    effect: [
      "Single-target.",
      "Target rolls Body vs Power.",
      "Ignites flammables on the target.",
      "Drain D -- pricey."
    ],
    src: "GRIM", pg: 126 },

  { n: "Fire Cloud", cat: "combat", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+1]D",
    target: "Body", area: "Within range", dmg: "(Force) Physical - Serious - fire",
    desc: "Cloud of fire blanketing an area.",
    effect: [
      "Area effect.",
      "Each target rolls Body vs Power.",
      "Lingering flames may ignite flammables in the area.",
      "Effective for crowds and dense formations."
    ],
    src: "GRIM", pg: 126 },

  { n: "Fire Dart", cat: "combat", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+1]M",
    target: "Body", area: "Single target", dmg: "(Force) Physical - Light - fire",
    desc: "Small flaming dart at a single target.",
    effect: [
      "Single-target.",
      "Target rolls Body vs Power.",
      "Low-drain fire option."
    ],
    src: "GRIM", pg: 126 },

  { n: "Fire Missile", cat: "combat", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+1]S",
    target: "Body", area: "Single target", dmg: "(Force) Physical - Moderate - fire",
    desc: "Fast flaming missile with serious force.",
    effect: [
      "Single-target.",
      "Target rolls Body vs Power.",
      "Ignites flammables on impact.",
      "Mid-tier fire damage with manageable drain."
    ],
    src: "GRIM", pg: 126 },

  { n: "Mana Cloud", cat: "combat", typ: "M", rng: "LOS", dur: "I", drn: "(F/2)S",
    target: "Willpower (R)", area: "Within range", dmg: "(Force) Physical - living only",
    desc: "Roiling cloud of mana that gnaws at living things.",
    effect: [
      "Area effect, living-only.",
      "Each target rolls Willpower vs Power.",
      "Stun damage."
    ],
    src: "GRIM", pg: 126 },

  { n: "Manablast", cat: "combat", typ: "M", rng: "LOS", dur: "I", drn: "(F/2)D",
    target: "Willpower (R)", area: "Within range", dmg: "(Force) Physical - living only",
    desc: "Area concussion of mana that brutalizes every living target.",
    effect: [
      "Area effect, living-only.",
      "Each target rolls Willpower vs Power.",
      "Damage D -- extremely punishing.",
      "Affects everyone alive in the radius -- friend or foe."
    ],
    src: "GRIM", pg: 126 },

  { n: "Powerblast", cat: "combat", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+1]D",
    target: "Body", area: "Within range", dmg: "(Force) Physical",
    desc: "Area shockwave of magical energy that pummels everything caught in it.",
    effect: [
      "Area effect; living AND inanimate.",
      "Each target rolls Body vs Power.",
      "Damage D -- destroys cover and drones alongside flesh."
    ],
    src: "GRIM", pg: 127 },

  { n: "Ram Touch", cat: "combat", typ: "P", rng: "T", dur: "I", drn: "[(F/2)-1]M",
    target: "Barrier Rating", area: "Single (touch)", dmg: "(Force) Physical - inanimate only",
    desc: "Touch-range Ram variant for wrecking inanimate matter.",
    effect: [
      "Touch range; living targets unaffected (as Ram).",
      "Caster must touch the object.",
      "Lower drain than ranged Ram."
    ],
    src: "GRIM", pg: 127 },

  { n: "Slay (Race/Species)", cat: "combat", typ: "M", rng: "LOS", dur: "I", drn: "[(F/2)-1]S",
    target: "Willpower (R)", area: "Single subject", dmg: "(Force) Physical - living only - named race",
    desc: "Targeted mana bolt that affects only one chosen race or species.",
    effect: [
      "Single-target. Mana spell.",
      "Caster picks the race/species when learning the spell (orks, elves, ghouls, drakes, etc.).",
      "Only beings of that type are affected.",
      "Rules-lawyer's nightmare; GM should approve scope."
    ],
    src: "GRIM", pg: 127 },

  { n: "Spirit Bolt", cat: "combat", typ: "M", rng: "LOS", dur: "I", drn: "[(F/2)+2]S",
    target: "Willpower (R)", area: "Single (spirits)", dmg: "(Force) Physical - vs spirits",
    desc: "Mana bolt attuned to wound spirits and elementals.",
    effect: [
      "Single-target spirit / elemental / paranormal critter.",
      "Spirit rolls its Force vs Power.",
      "Doesn't affect ordinary living creatures.",
      "Essential against spirit-heavy threats."
    ],
    src: "GRIM", pg: 127 },

  { n: "Sterilize", cat: "combat", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+1]D",
    target: "--", area: "Within range", dmg: "Kills microorganisms",
    desc: "Annihilates microscopic organisms across an area.",
    effect: [
      "Area effect, microbial-targeted.",
      "Purges bacteria, viruses, parasites -- useful for biotech labs, evidence cleanup.",
      "Does NOT harm living beings directly.",
      "May affect implanted bioware or biotech cultures."
    ],
    src: "GRIM", pg: 127 },

  { n: "Stun Bolt", cat: "combat", typ: "M", rng: "LOS", dur: "I", drn: "[(F/2)-1]D",
    target: "Willpower (R)", area: "Single subject", dmg: "(Force) Stun - Serious",
    desc: "Mana strike that knocks one target senseless rather than killing.",
    effect: [
      "Single-target, living-only.",
      "Target rolls Willpower vs Power.",
      "Stun damage -- knocks out, doesn't kill.",
      "Drain D but easier to soak (Stun) -- popular for non-lethal takedowns."
    ],
    src: "GRIM", pg: 127 },

  { n: "Stun Cloud", cat: "combat", typ: "M", rng: "LOS", dur: "I", drn: "[(F/2)-1]D",
    target: "Willpower (R)", area: "Within range", dmg: "(Force) Stun",
    desc: "Area version of Stun Bolt.",
    effect: [
      "Area effect, living-only.",
      "Each target rolls Willpower vs Power.",
      "Stun damage."
    ],
    src: "GRIM", pg: 127 },

  { n: "Stun Missile", cat: "combat", typ: "M", rng: "LOS", dur: "I", drn: "[(F/2)-1]M",
    target: "Willpower (R)", area: "Single subject", dmg: "(Force) Stun - Moderate",
    desc: "Streaking mana bolt that moderately stuns.",
    effect: [
      "Single-target, living-only.",
      "Target rolls Willpower vs Power.",
      "Stun M -- moderate knockout potential."
    ],
    src: "GRIM", pg: 127 },

  { n: "Stun Touch", cat: "combat", typ: "M", rng: "T", dur: "I", drn: "[(F/2)-2]M",
    target: "Willpower (R)", area: "Single (touch)", dmg: "(Force) Stun",
    desc: "Short-range mana shock applied by touch.",
    effect: [
      "Touch range.",
      "Target rolls Willpower vs Power.",
      "Stun M -- non-lethal contact takedown.",
      "Very low drain."
    ],
    src: "GRIM", pg: 127 },

  { n: "Stunball", cat: "combat", typ: "M", rng: "LOS", dur: "I", drn: "[(F/2)-1]D",
    target: "Willpower (R)", area: "Within range", dmg: "(Force) Stun - Serious",
    desc: "Area sphere of stunning mana.",
    effect: [
      "Area effect, living-only.",
      "Each target rolls Willpower vs Power.",
      "Stun D -- drops everyone in radius if successful.",
      "Workhorse mass-takedown spell."
    ],
    src: "GRIM", pg: 127 },

  { n: "Stunblast", cat: "combat", typ: "M", rng: "LOS", dur: "I", drn: "[(F/2)+1]D",
    target: "Willpower (R)", area: "Within range", dmg: "(Force) Stun",
    desc: "High-power stunning detonation overwhelming every mind in range.",
    effect: [
      "Area effect, living-only.",
      "Each target rolls Willpower vs Power.",
      "Stun damage at higher staging than Stunball.",
      "Heavier drain than Stunball."
    ],
    src: "GRIM", pg: 127 },

  { n: "Urban Renewal", cat: "combat", typ: "P", rng: "LOS", dur: "I", drn: "(F/2)D",
    target: "Object Resistance", area: "Within range", dmg: "Destroys objects (area)",
    desc: "Demolishes buildings and structures in an area.",
    effect: [
      "Area effect, structures-only.",
      "Living beings inside structures unaffected directly -- but collapse can crush them.",
      "Buildings roll Object Resistance vs Power.",
      "Surgical demolition tool."
    ],
    src: "GRIM", pg: 127 },

  { n: "Wrecker", cat: "combat", typ: "P", rng: "LOS", dur: "I", drn: "(F/2)S",
    target: "Object Resistance", area: "Single (one vehicle/object)", dmg: "Destroys target",
    desc: "Ram variant tuned to wreck vehicles.",
    effect: [
      "Single-target -- vehicles, drones, aircraft.",
      "Vehicle rolls its Body or Armor vs Power.",
      "Useful for chase scenes and vehicle takedowns."
    ],
    src: "GRIM", pg: 127 },

  /* ============== Grimoire 2e -- Detection (p. 128) ============== */
  { n: "Analyze Magic", cat: "detection", typ: "M", rng: "LOS", dur: "S", drn: "(F/2)M",
    target: "Force/Rating", area: "Single (the magic)",
    desc: "Examine an active spell or magical item.",
    effect: [
      "Sustained.",
      "Each success reveals one detail: Force, type, caster's signature, sustained-or-permanent, etc.",
      "Useful for assessing wards, foci, active spells, and astral phenomena."
    ],
    src: "GRIM", pg: 128 },

  { n: "Clairaudience (Extended)", cat: "detection", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)-1]S",
    target: "4", area: "Single (remote point)",
    desc: "Clairaudience at much greater distances.",
    effect: [
      "Sustained.",
      "Range extends significantly past base Clairaudience -- up to kilometers with successes.",
      "Less precise than the standard version; difficult to filter ambient noise at extreme range."
    ],
    src: "GRIM", pg: 128 },

  { n: "Clairvoyance (Extended)", cat: "detection", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)-1]S",
    target: "4", area: "Single (remote point)",
    desc: "Clairvoyance at much greater distances.",
    effect: [
      "Sustained.",
      "Range extends significantly past base Clairvoyance.",
      "Detail and clarity scale with successes."
    ],
    src: "GRIM", pg: 128 },

  { n: "Detect Enemies (Extended)", cat: "detection", typ: "M", rng: "LOS", dur: "S", drn: "(F/2)S",
    target: "4", area: "Within range",
    desc: "Senses hostile beings at much greater range.",
    effect: [
      "Sustained.",
      "Each net success reveals one hostile-intent being in (extended) range.",
      "Range significantly larger than base Detect Enemies."
    ],
    src: "GRIM", pg: 128 },

  { n: "Detect Magic", cat: "detection", typ: "M", rng: "LOS", dur: "S", drn: "(F/2)L",
    target: "4", area: "Within range",
    desc: "Reveals presence of any active spells, foci, or magical phenomena nearby.",
    effect: [
      "Sustained.",
      "Each success reveals one source of magic in range (location and rough intensity).",
      "Does NOT identify what each effect IS (use Analyze Magic for that).",
      "Great for spotting hidden wards before entering."
    ],
    src: "GRIM", pg: 128 },

  { n: "Mindlink (Individual)", cat: "detection", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+2]M",
    target: "4 (Willpower if unwilling)", area: "Single subject",
    desc: "Two-way mental connection allowing silent communication with one willing person.",
    effect: [
      "Sustained.",
      "Both parties communicate telepathically -- words, images, concepts.",
      "Voluntary -- target must consent.",
      "Useful for stealth team coordination."
    ],
    src: "GRIM", pg: 128 },

  /* ============== Grimoire 2e -- Health (p. 129) ============== */
  { n: "Decrease -1 Cybered Attribute", cat: "health", typ: "P", rng: "T", dur: "S", drn: "[(F/2)+3]L",
    target: "10 - target Essence (R)", area: "Single subject",
    desc: "Saps a single point from an Attribute already augmented by cyberware.",
    effect: [
      "Sustained.",
      "Target rolls Body vs Power.",
      "-1 to one cybernetically-augmented Attribute on success.",
      "Useful against cyber-heavy targets."
    ],
    src: "GRIM", pg: 129 },

  { n: "Decrease -2 Cybered Attribute", cat: "health", typ: "P", rng: "T", dur: "S", drn: "[(F/2)+3]M",
    target: "10 - target Essence (R)", area: "Single subject",
    desc: "Strips two points from a cyber-augmented Attribute.",
    effect: [
      "Sustained.",
      "Target rolls Body vs Power.",
      "-2 to one cybered Attribute."
    ],
    src: "GRIM", pg: 129 },

  { n: "Decrease -3 Cybered Attribute", cat: "health", typ: "P", rng: "T", dur: "S", drn: "[(F/2)+3]S",
    target: "10 - target Essence (R)", area: "Single subject",
    desc: "Slashes three points off a cybered Attribute.",
    effect: [
      "Sustained.",
      "Target rolls Body vs Power.",
      "-3 to one cybered Attribute. Devastating against street samurai."
    ],
    src: "GRIM", pg: 129 },

  { n: "Decrease -4 Cybered Attribute", cat: "health", typ: "P", rng: "T", dur: "S", drn: "[(F/2)+3]D",
    target: "10 - target Essence (R)", area: "Single subject",
    desc: "Hammers a cybered Attribute down by four points.",
    effect: [
      "Sustained.",
      "Target rolls Body.",
      "-4 to cybered Attribute -- cripples the augmentation.",
      "Brutal drain."
    ],
    src: "GRIM", pg: 129 },

  { n: "Decrease Reflexes -1 Initiative Die", cat: "health", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+1]S",
    target: "2 x Reaction (R)", area: "Single subject",
    desc: "Drags victim's combat reactions down by one initiative die.",
    effect: [
      "Sustained.",
      "Target rolls Willpower vs Power.",
      "-1 initiative die per turn while sustained."
    ],
    src: "GRIM", pg: 129 },

  { n: "Decrease Reflexes -2 Initiative Dice", cat: "health", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+1]D",
    target: "2 x Reaction (R)", area: "Single subject",
    desc: "Removes two initiative dice from the target.",
    effect: [
      "Sustained.",
      "Target rolls Willpower vs Power.",
      "-2 init dice -- drops cybered runners hard."
    ],
    src: "GRIM", pg: 129 },

  { n: "Decrease Reflexes -3 Initiative Dice", cat: "health", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+2]D",
    target: "2 x Reaction (R)", area: "Single subject",
    desc: "Slows target to a crawl, robbing three initiative dice.",
    effect: [
      "Sustained.",
      "Target rolls Willpower.",
      "-3 init dice -- even Wired 3 samurai are reduced to baseline."
    ],
    src: "GRIM", pg: 129 },

  { n: "Healthy Glow", cat: "health", typ: "M", rng: "T", dur: "P", drn: "(F/2)L",
    target: "4 (voluntary)", area: "Single subject",
    desc: "Cosmetic spell that clears the eyes, smooths skin, adds vitality.",
    effect: [
      "Permanent for several hours after casting.",
      "No combat effect -- purely cosmetic.",
      "Useful for high-society infiltration, dates, photoshoots."
    ],
    src: "GRIM", pg: 129 },

  { n: "Oxygenate", cat: "health", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]M",
    target: "4 (voluntary)", area: "Single subject",
    desc: "Forces extra oxygen into the subject's blood.",
    effect: [
      "Sustained on willing subject.",
      "Subject can hold breath, tolerate low-O2 environments, or function in smoke.",
      "Duration scales with sustained concentration.",
      "Useful for underwater work, smoke-filled rooms, high-altitude operations."
    ],
    src: "GRIM", pg: 129 },

  { n: "Preserve", cat: "health", typ: "P", rng: "LOS", dur: "P", drn: "[(F/2)+2]M",
    target: "Object Resistance", area: "Single object",
    desc: "Halts decay in dead organic material.",
    effect: [
      "Permanent: object stays in stasis until spell dispelled.",
      "Useful for corpse preservation, evidence chains, biological samples.",
      "Does NOT revive -- only prevents further decomposition."
    ],
    src: "GRIM", pg: 129 },

  { n: "Prophylaxis (L) Pathogen", cat: "health", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]L",
    target: "4 (voluntary)", area: "Single subject",
    desc: "Protects against infection by mild airborne / contact pathogens.",
    effect: [
      "Sustained on willing subject.",
      "Subject gains immunity to one chosen mild pathogen category for the duration.",
      "Useful in disease zones -- Bug City refugee camps, slum operations."
    ],
    src: "GRIM", pg: 129 },

  { n: "Prophylaxis (M) Pathogen", cat: "health", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]M",
    target: "4 (voluntary)", area: "Single subject",
    desc: "Wards against moderately dangerous pathogens.",
    effect: [
      "Sustained.",
      "Immunity to one chosen moderate pathogen category."
    ],
    src: "GRIM", pg: 129 },

  { n: "Prophylaxis (S) Pathogen", cat: "health", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]S",
    target: "4 (voluntary)", area: "Single subject",
    desc: "Shields against serious infectious diseases.",
    effect: [
      "Sustained.",
      "Immunity to one chosen serious pathogen category."
    ],
    src: "GRIM", pg: 129 },

  { n: "Prophylaxis (D) Pathogen", cat: "health", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]D",
    target: "4 (voluntary)", area: "Single subject",
    desc: "Magical immunity against lethal infectious diseases.",
    effect: [
      "Sustained.",
      "Immunity to one chosen deadly pathogen.",
      "Critical for medical staff entering plague zones."
    ],
    src: "GRIM", pg: 129 },

  { n: "Resist Pain (Light)", cat: "health", typ: "M", rng: "LOS", dur: "P", drn: "(F/2)L",
    target: "4 (voluntary)", area: "Single subject",
    desc: "Numbs the pain of a Light wound.",
    effect: [
      "Permanent for the duration of the wound's effects.",
      "Removes the +1 TN modifier from a Light wound.",
      "Damage itself remains -- subject just doesn't feel it.",
      "Subject may aggravate the injury unknowingly."
    ],
    src: "GRIM", pg: 129 },

  { n: "Resist Pain (Moderate)", cat: "health", typ: "M", rng: "LOS", dur: "P", drn: "(F/2)M",
    target: "4 (voluntary)", area: "Single subject",
    desc: "Pushes aside the agony of a Moderate wound.",
    effect: [
      "Permanent for wound duration.",
      "Removes the +2 TN modifier from a Moderate wound."
    ],
    src: "GRIM", pg: 129 },

  { n: "Resist Pain (Serious)", cat: "health", typ: "M", rng: "LOS", dur: "P", drn: "(F/2)D",
    target: "4 (voluntary)", area: "Single subject",
    desc: "Erases the pain of a Serious wound.",
    effect: [
      "Permanent for wound duration.",
      "Removes the +3 TN modifier from a Serious wound.",
      "Drain D -- significant cost."
    ],
    src: "GRIM", pg: 129 },

  { n: "Stabilize", cat: "health", typ: "P", rng: "LOS", dur: "P", drn: "(F/2)S",
    target: "4 + minutes elapsed", area: "Single subject",
    desc: "Locks a wounded character at current condition.",
    effect: [
      "Permanent.",
      "Prevents further bleeding / deterioration from already-taken damage.",
      "Does NOT heal -- buys time for transport to a Heal-capable mage.",
      "Critical for casualties at Deadly damage."
    ],
    src: "GRIM", pg: 129 },

  /* ============== Grimoire 2e -- Illusion (p. 130) ============== */
  { n: "Overstimulation", cat: "illusion", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+1]M",
    target: "Willpower (R)", area: "Single subject", dmg: "(successes) Stun",
    desc: "Floods the target's senses with overload.",
    effect: [
      "Sustained, single-target.",
      "Target rolls Willpower vs Power.",
      "Failure: subject suffers Stun-like effects (TN penalties, possible incapacitation).",
      "Mana illusion -- affects only living."
    ],
    src: "GRIM", pg: 130 },

  { n: "Physical Mask", cat: "illusion", typ: "P", rng: "T", dur: "S", drn: "[(F/2)+1]L",
    target: "Perception to detect", area: "Single subject",
    desc: "Mask variant that also fools cameras and electronic recording.",
    effect: [
      "Sustained.",
      "Physical illusion: works on tech (cameras, sensors, drones) AND living observers.",
      "Observer rolls Willpower vs Power; sensors use their detection rating.",
      "Premier disguise spell -- preferred over Mask when tech is involved."
    ],
    src: "GRIM", pg: 130 },

  { n: "Spectacle", cat: "illusion", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+1]M",
    target: "-- (voluntary)", area: "Within range",
    desc: "Multi-sensory area illusion designed to draw crowds.",
    effect: [
      "Sustained, area effect.",
      "Caster designs the spectacle in advance.",
      "Mana illusion -- works on living observers only.",
      "Used for distraction, performance, propaganda."
    ],
    src: "GRIM", pg: 130 },

  { n: "Trid Entertainment", cat: "illusion", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]L",
    target: "-- (voluntary)", area: "Within range",
    desc: "Entertainment variant that registers on trideo and electronic sensors.",
    effect: [
      "Sustained, area effect.",
      "Physical illusion -- fools both living and tech observers.",
      "Used for ad campaigns, surveillance deception, holographic theater."
    ],
    src: "GRIM", pg: 130 },

  { n: "Trid Spectacle", cat: "illusion", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]M",
    target: "-- (voluntary)", area: "Within range",
    desc: "Spectacle visible to recording gear too.",
    effect: [
      "Sustained, area effect.",
      "Physical illusion: shows up on cameras and sensors.",
      "Useful for fooling drone-based surveillance and broadcasting deception."
    ],
    src: "GRIM", pg: 130 },

  { n: "Vehicle Mask", cat: "illusion", typ: "P", rng: "T", dur: "S", drn: "(F/2)L",
    target: "Perception to detect", area: "Single (vehicle)",
    desc: "Disguises a touched vehicle as a different make / model.",
    effect: [
      "Sustained on touched vehicle.",
      "Observer rolls Willpower (or sensor rating) vs Power to see through.",
      "Physical illusion -- fools cameras and sensor sweeps."
    ],
    src: "GRIM", pg: 130 },

  /* ============== Grimoire 2e -- Manipulation (p. 130-132) ============== */
  { n: "Control Animal", cat: "manipulation", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+2]D",
    target: "Willpower/Essence (R)", area: "Single (animal)",
    desc: "Puppeteer a non-sentient animal.",
    effect: [
      "Sustained.",
      "Opposed Willpower test (animal's Willpower is typically low).",
      "Caster directs the animal's actions.",
      "Doesn't work on awakened paranormal critters (uses other rules)."
    ],
    src: "GRIM", pg: 130 },

  { n: "Influence", cat: "manipulation", typ: "M", rng: "LOS", dur: "P", drn: "[(F/2)+2]S",
    target: "Willpower (R)", area: "Single subject",
    desc: "Plants a single forceful suggestion in the victim's mind.",
    effect: [
      "Permanent: the suggestion sticks.",
      "Target rolls Willpower vs Power.",
      "Caster gives one specific instruction; target carries it out believing it's their own idea.",
      "Limited to one action or short sequence -- not ongoing control."
    ],
    src: "GRIM", pg: 130 },

  { n: "Mob Mind", cat: "manipulation", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+3]D",
    target: "Willpower (R)", area: "Within range",
    desc: "Area Control Thoughts on a crowd.",
    effect: [
      "Sustained, area effect.",
      "Each target rolls Willpower vs Power.",
      "Crowd acts as a unified entity under the caster's direction.",
      "Brutal drain -- typically requires Spell Lock + Centering."
    ],
    src: "GRIM", pg: 130 },

  { n: "Mob Mood", cat: "manipulation", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+2]D",
    target: "Willpower (R)", area: "Within range",
    desc: "Sways the emotions of an entire crowd.",
    effect: [
      "Sustained, area effect.",
      "Each target rolls Willpower vs Power.",
      "Caster picks the dominant emotion; crowd shifts to match.",
      "Used for riot control, political rallies, public manipulation."
    ],
    src: "GRIM", pg: 130 },

  { n: "Animate", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]M",
    target: "Object Resistance", area: "Single object",
    desc: "Imbues an inanimate object with movement.",
    effect: [
      "Sustained.",
      "Object moves at caster's command -- walks, attacks, follows orders.",
      "Force determines effective Strength / Quickness of the animated object.",
      "Object Resistance applies if the item resists."
    ],
    src: "GRIM", pg: 130 },

  { n: "Clout", cat: "manipulation", typ: "P", rng: "LOS", dur: "I", drn: "(F/2)M",
    target: "4 (Impact armor defends)", area: "Single target", dmg: "(Willpower) Stun - Moderate",
    desc: "Short, focused telekinetic punch.",
    effect: [
      "Instant.",
      "Target rolls Body vs Power.",
      "Stun damage -- knocks back, doesn't kill.",
      "Quick non-lethal option."
    ],
    src: "GRIM", pg: 131 },

  { n: "Use (Skill)", cat: "manipulation", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+3]L",
    target: "4 (voluntary)", area: "Single subject",
    desc: "Telekinetically wield a chosen skill at range.",
    effect: [
      "Sustained.",
      "Caster picks the skill when learning (e.g., Pistols, Lockpicking, Computers).",
      "Mage uses their skill rating against a remote target object.",
      "Useful for safe-cracking, sniping, hacking without proximity."
    ],
    src: "GRIM", pg: 131 },

  { n: "Acid", cat: "manipulation", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+1]S",
    target: "4", area: "Single target", dmg: "(Force) Physical - acid",
    desc: "Sprays corrosive jet at one target.",
    effect: [
      "Instant, single-target.",
      "Target rolls Body vs Power.",
      "Reduces armor -- acid eats through ballistic protection."
    ],
    src: "GRIM", pg: 131 },

  { n: "Acid Bomb", cat: "manipulation", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+1]D",
    target: "4", area: "Within range", dmg: "(Force) Physical - acid",
    desc: "Bursts a glob of acid across an area.",
    effect: [
      "Instant, area effect.",
      "Each target rolls Body vs Power.",
      "Lasting damage from acid residue (per GM)."
    ],
    src: "GRIM", pg: 131 },

  { n: "Acid Stream", cat: "manipulation", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+1]D",
    target: "4", area: "Single (stream)", dmg: "(Force) Physical - acid",
    desc: "Sustained stream of acid hosing one target.",
    effect: [
      "Instant single-target (deals all damage in one go).",
      "Target rolls Body vs Power.",
      "Heavy damage; can eat through armor over time."
    ],
    src: "GRIM", pg: 131 },

  { n: "Astral Static", cat: "manipulation", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+1]D",
    target: "4", area: "Within range",
    desc: "Saturates an area with chaotic mana disrupting spellcasting.",
    effect: [
      "Sustained, area effect.",
      "All spellcasting in the area suffers TN penalty.",
      "Useful for anti-mage tactics in dense magic zones."
    ],
    src: "GRIM", pg: 131 },

  { n: "Bind", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]S",
    target: "Quickness (R)", area: "Single subject",
    desc: "Wraps target in cords of mystic energy.",
    effect: [
      "Sustained.",
      "Target rolls Body vs Power.",
      "Failure: target is held in place; Strength test (vs Force) to break free.",
      "Non-lethal restraint option."
    ],
    src: "GRIM", pg: 131 },

  { n: "Blade Barrier", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]M",
    target: "4", area: "Created barrier", dmg: "Barrier Rating = Force",
    desc: "Barrier variant offering extra protection against bladed weapons.",
    effect: [
      "Sustained.",
      "Barrier Rating = Force; +X armor specifically against edged / pointed melee.",
      "Less effective against blunt or ballistic attacks."
    ],
    src: "GRIM", pg: 131 },

  { n: "Blast Barrier", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]M",
    target: "4", area: "Created barrier",
    desc: "Barrier tuned to soak explosions and shrapnel.",
    effect: [
      "Sustained.",
      "Barrier Rating = Force; +X armor specifically against explosive / concussive damage.",
      "Use against grenades, demolitions, area weapons."
    ],
    src: "GRIM", pg: 131 },

  { n: "Bullet Barrier", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]M",
    target: "4", area: "Created barrier",
    desc: "Barrier built to deflect firearm rounds.",
    effect: [
      "Sustained.",
      "Barrier Rating = Force; +X armor specifically against ballistic damage.",
      "Less effective against melee, magic, or explosions."
    ],
    src: "GRIM", pg: 131 },

  { n: "(Critter) Form", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]S",
    target: "Willpower", area: "Single subject",
    desc: "Transform a volunteer into a specific paranormal critter.",
    effect: [
      "Sustained, voluntary subject.",
      "Caster picks the paranormal critter when learning the spell.",
      "Subject gains the critter's stats and abilities.",
      "Mind remains the subject's own; can speak only if the critter form allows."
    ],
    src: "GRIM", pg: 131 },

  { n: "Fashion", cat: "manipulation", typ: "P", rng: "LOS", dur: "P", drn: "[(F/2)+2]M",
    target: "4", area: "Single subject",
    desc: "Restyles a subject's clothing into a desired outfit.",
    effect: [
      "Permanent -- changes outlast the spell.",
      "Useful for instant costume changes, high-society disguises.",
      "Physical illusion -- works under inspection."
    ],
    src: "GRIM", pg: 131 },

  { n: "Fire Strike", cat: "manipulation", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+3]D",
    target: "Body (R)", area: "Within range", dmg: "(Force) Physical - Serious - fire",
    desc: "Torrent of flame at an area.",
    effect: [
      "Instant, area effect.",
      "Each target rolls Body vs Power.",
      "Ignites flammables across the entire area.",
      "Drain D -- most expensive fire spell."
    ],
    src: "GRIM", pg: 132 },

  { n: "Flame Burst", cat: "manipulation", typ: "P", rng: "LOS", dur: "I", drn: "[(F/2)+1]D",
    target: "Body (R)", area: "Single target", dmg: "(Force) Physical - fire",
    desc: "Directed burst of fire at one target.",
    effect: [
      "Instant, single-target.",
      "Target rolls Body vs Power.",
      "May ignite clothing / hair / flammables on target."
    ],
    src: "GRIM", pg: 132 },

  { n: "Lock", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]M",
    target: "Object Resistance", area: "Single (door/object)",
    desc: "Magically jams a door or container closed.",
    effect: [
      "Sustained.",
      "Lock strength = Force; opens with corresponding Lockpicking / Strength test against Force.",
      "Only the caster can release the lock at will."
    ],
    src: "GRIM", pg: 132 },

  { n: "Makeover", cat: "manipulation", typ: "P", rng: "LOS", dur: "P", drn: "[(F/2)+2]M",
    target: "4 (voluntary)", area: "Single subject",
    desc: "Permanently restyles a willing subject's appearance.",
    effect: [
      "Permanent.",
      "Subject's grooming, cosmetics, hair are reshaped to the caster's design.",
      "Underlying body structure unchanged -- for that, see Physical Mask."
    ],
    src: "GRIM", pg: 132 },

  { n: "Seal", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]S",
    target: "4", area: "Created barrier",
    desc: "Lock variant that also fortifies the sealed object's Barrier Rating.",
    effect: [
      "Sustained.",
      "Lock strength = Force; AND Barrier Rating of the sealed object increases by Force.",
      "Use to lock + reinforce doors against breach attempts."
    ],
    src: "GRIM", pg: 132 },

  { n: "Shapechange", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]S",
    target: "Willpower (R)", area: "Single subject",
    desc: "Morph subject into a chosen natural animal.",
    effect: [
      "Sustained, voluntary subject.",
      "Subject gains the chosen normal critter's abilities.",
      "Mind remains the subject's own.",
      "Limited to natural (non-paranormal) animals."
    ],
    src: "GRIM", pg: 132 },

  { n: "Spell Barrier", cat: "manipulation", typ: "M", rng: "LOS", dur: "S", drn: "[(F/2)+2]M",
    target: "6", area: "Created barrier",
    desc: "Mana barrier that selectively blocks incoming spells.",
    effect: [
      "Sustained.",
      "Barrier Rating = Force vs incoming spells only.",
      "Physical objects and people pass through normally.",
      "Useful for warding a space against magical intrusion without restricting movement."
    ],
    src: "GRIM", pg: 132 },

  { n: "Thunderclap", cat: "manipulation", typ: "P", rng: "LOS", dur: "I", drn: "(F/2)S",
    target: "Body (R)", area: "Within range", dmg: "(Force) Stun - Moderate",
    desc: "Cracks the air with a deafening sonic burst.",
    effect: [
      "Instant, area effect.",
      "Each target rolls Body vs Power.",
      "Stun damage from sonic impact; deafens nearby ears.",
      "Useful for breaking up crowds and disorienting enemies."
    ],
    src: "GRIM", pg: 132 },

  { n: "Transform", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "[(F/2)+2]S",
    target: "Willpower (R)", area: "Single subject",
    desc: "Reshapes subject into a normal animal form, keeping human mind.",
    effect: [
      "Sustained, voluntary subject.",
      "Subject gains the chosen normal animal's body but keeps their own mind.",
      "Cannot speak as a normal animal would not.",
      "Useful for stealth and reconnaissance."
    ],
    src: "GRIM", pg: 132 },

  /* ============== Awakenings -- Voudoun (p. 130) ============== */
  { n: "Corps Cadavre", cat: "manipulation", typ: "P", rng: "T", dur: "P", drn: "(F/2)+2S",
    target: "Object Resistance", area: "Single corpse",
    desc: "Reanimates a prepared corpse into a Petro-zombie.",
    effect: [
      "Permanent -- zombie persists until destroyed.",
      "Voudoun bocor-only ritual; requires a prepared body.",
      "Zombie is obedient to the bocor's commands.",
      "Treated as a paranormal critter for combat purposes."
    ],
    src: "AWK", pg: 130 },

  /* ============== Awakenings -- Combat (p. 133-134) ============== */
  { n: "Redirect", cat: "combat", typ: "P", rng: "LOS", dur: "I", drn: "Special",
    target: "4", area: "Single (incoming spell)", dmg: "Reflects attacker's spell",
    desc: "Bounces an incoming projectile or magical attack back at its original attacker.",
    effect: [
      "Instant, reactive -- declared in response to an incoming attack.",
      "Drain is special -- see Awakenings p. 133 for the exact mechanism.",
      "Successful redirect reverses the attack against its originator."
    ],
    src: "AWK", pg: 133 },

  { n: "Rot", cat: "combat", typ: "P", rng: "LOS", dur: "I", drn: "(F+2)+1M",
    target: "Object Resistance / Body", area: "Single target", dmg: "(Force) Physical - Serious - organic",
    desc: "Decays organic matter and damages zombies and undead.",
    effect: [
      "Single-target.",
      "Target rolls Body vs Power.",
      "Particularly effective against undead, zombies, and otherwise-tough organic threats.",
      "Aspected drain notation: (F+2) base."
    ],
    src: "AWK", pg: 134 },

  { n: "Shattershield", cat: "combat", typ: "M", rng: "LOS", dur: "I", drn: "(F+2)S",
    target: "Ward/Force (R)", area: "Single (ward/barrier)", dmg: "(Force) - Deadly vs barriers",
    desc: "Strikes astral barriers and wards to weaken or breach.",
    effect: [
      "Single-target -- barrier / ward.",
      "Barrier rolls its Force vs Power.",
      "Net successes reduce the barrier's Force or breach it entirely.",
      "Essential for breaching warded facilities."
    ],
    src: "AWK", pg: 134 },

  /* ============== Awakenings -- Detection (p. 134-135) ============== */
  { n: "Animal Spy", cat: "detection", typ: "M", rng: "LOS", dur: "S", drn: "(F+2)L",
    target: "4", area: "Single (animal)",
    desc: "Perceive through a non-paranormal animal's senses.",
    effect: [
      "Sustained.",
      "Caster sees / hears / smells through an animal's senses.",
      "Animal is a willing or controlled subject.",
      "Useful for reconnaissance -- animals raise less suspicion."
    ],
    src: "AWK", pg: 134 },

  { n: "Astral Sense", cat: "detection", typ: "M", rng: "LOS", dur: "S", drn: "(F+2)M",
    target: "10", area: "Single subject",
    desc: "Grants astral awareness to a willing subject.",
    effect: [
      "Sustained on willing subject.",
      "Subject gains astral perception without being able to project.",
      "Useful for non-magicians who need to spot magical phenomena.",
      "Subject doesn't see auras in detail like a true magician."
    ],
    src: "AWK", pg: 134 },

  { n: "Catalogue", cat: "detection", typ: "P", rng: "LOS", dur: "I", drn: "(F+2)+1L",
    target: "4", area: "Within range",
    desc: "Lists every object inside a viewed space.",
    effect: [
      "Instant snapshot.",
      "Caster compiles a mental inventory of objects in the viewed area.",
      "Useful for examining warehouses, vaults, evidence sites.",
      "Doesn't reveal hidden compartments unless caster can see them."
    ],
    src: "AWK", pg: 134 },

  { n: "Diagnose", cat: "detection", typ: "M", rng: "LOS", dur: "I", drn: "(F+2)+1M",
    target: "10 - target Essence", area: "Single subject",
    desc: "Reveals injuries, illnesses, and cyberware in a target.",
    effect: [
      "Instant assessment.",
      "Each success reveals one detail: wounds, diseases, drugs, or cyberware implants.",
      "Useful for street docs, ambush planning, infiltration screening."
    ],
    src: "AWK", pg: 134 },

  { n: "Enhance Aim", cat: "detection", typ: "M", rng: "LOS", dur: "S", drn: "(F+2)L",
    target: "4", area: "Single subject",
    desc: "Lowers target numbers for ranged attacks.",
    effect: [
      "Sustained on willing subject (typically a shooter).",
      "Successes reduce the subject's TN for ranged attacks.",
      "Useless if subject has smartlink + cybereye targeting (those already optimize).",
      "Useful for runners using mundane sights."
    ],
    src: "AWK", pg: 134 },

  { n: "Foretelling", cat: "detection", typ: "M", rng: "Self", dur: "I", drn: "(F+2)D",
    target: "10", area: "Self",
    desc: "Glimpses the likely outcome of a contemplated event.",
    effect: [
      "Instant.",
      "Caster mentions a specific intended action; GM reveals one likely consequence.",
      "Drain D -- heavy cost for divination.",
      "GM should answer in flavor terms, not exact mechanics."
    ],
    src: "AWK", pg: 135 },

  { n: "Night Vision", cat: "detection", typ: "P", rng: "T", dur: "S", drn: "(F+2)L",
    target: "4", area: "Single subject",
    desc: "Grants the touched target low-light vision.",
    effect: [
      "Sustained on touched subject.",
      "Subject gains low-light vision equivalent to cybereye Low-Light.",
      "Useful for non-cybered teammates."
    ],
    src: "AWK", pg: 135 },

  { n: "Translate", cat: "detection", typ: "M", rng: "LOS", dur: "S", drn: "(F+2)+1L",
    target: "4", area: "Single subject",
    desc: "Establishes telepathic conversation despite language barriers.",
    effect: [
      "Sustained.",
      "Both parties exchange thoughts as if speaking a common language.",
      "Useful for international ops, alien encounters, ancient texts.",
      "Subjects don't actually learn the language -- only communicate via the spell."
    ],
    src: "AWK", pg: 135 },

  { n: "X-Ray Vision", cat: "detection", typ: "M", rng: "LOS", dur: "S", drn: "(F+2)+2S",
    target: "4", area: "Single subject",
    desc: "See through solid barriers up to a limit.",
    effect: [
      "Sustained on willing subject.",
      "Barrier Rating <= Force can be seen through.",
      "Useful for spotting hidden contraband, mapping interiors.",
      "Doesn't reveal magical wards (use Detect Magic for that)."
    ],
    src: "AWK", pg: 135 },

  /* ============== Awakenings -- Health (p. 135-136) ============== */
  { n: "Alleviate Allergy", cat: "health", typ: "P", rng: "LOS", dur: "S", drn: "(F+2)L",
    target: "6", area: "Single subject",
    desc: "Temporarily suppresses an allergic reaction.",
    effect: [
      "Sustained on subject.",
      "Subject's allergy effects are negated for the duration.",
      "Useful for metahuman allergies, environmental allergens.",
      "Doesn't remove the underlying allergy -- just suppresses reaction."
    ],
    src: "AWK", pg: 135 },

  { n: "Awaken", cat: "health", typ: "M", rng: "T", dur: "I", drn: "(F+2)+1L",
    target: "10 - target Essence", area: "Single subject",
    desc: "Rouses an unconscious subject to full alertness.",
    effect: [
      "Instant.",
      "Subject snaps to awareness immediately.",
      "Useful for waking knocked-out allies, rescuing comatose patients.",
      "Does NOT heal the underlying cause -- only restores consciousness."
    ],
    src: "AWK", pg: 135 },

  { n: "Blindness", cat: "health", typ: "M", rng: "LOS", dur: "S", drn: "(F+2)+1D",
    target: "Body (R)", area: "Single subject",
    desc: "Magically blinds the target.",
    effect: [
      "Sustained.",
      "Target rolls Willpower vs Power.",
      "Failure: target is completely blind, including through cybereyes (mana spell ignores tech).",
      "Combat-disabling effect."
    ],
    src: "AWK", pg: 135 },

  { n: "Cause Allergy", cat: "health", typ: "M", rng: "LOS", dur: "S", drn: "(F+2)L",
    target: "Body (R)", area: "Single subject",
    desc: "Inflicts a temporary allergy on the subject.",
    effect: [
      "Sustained.",
      "Target rolls Willpower vs Power.",
      "Failure: subject becomes allergic to a specific substance the caster names.",
      "Useful for sabotage and inconvenience."
    ],
    src: "AWK", pg: 135 },

  { n: "Cripple Limb", cat: "health", typ: "M", rng: "T", dur: "S", drn: "(F+2)S",
    target: "10 - target Essence (R)", area: "Single subject",
    desc: "Renders one limb of the target useless.",
    effect: [
      "Sustained.",
      "Target rolls Willpower vs Power.",
      "Failure: chosen limb becomes useless -- arm can't lift, leg can't walk.",
      "Touch range -- requires close contact."
    ],
    src: "AWK", pg: 136 },

  { n: "Fast", cat: "health", typ: "M", rng: "T", dur: "P", drn: "(F+2)L",
    target: "4 (voluntary)", area: "Single subject",
    desc: "Negates feelings of hunger or thirst.",
    effect: [
      "Permanent for ~10 turns (the spell's stated duration).",
      "Subject doesn't feel hunger / thirst.",
      "Body still NEEDS food and water -- this just removes the urge.",
      "Useful for extended stealth or survival situations."
    ],
    src: "AWK", pg: 136 },

  { n: "Intoxication", cat: "health", typ: "M", rng: "LOS", dur: "S", drn: "(F+2)+2M",
    target: "Body (R)", area: "Single subject",
    desc: "Inflicts drunkenness on the target.",
    effect: [
      "Sustained.",
      "Target rolls Willpower vs Power.",
      "Failure: target suffers TN penalties as if drunk; gradually accumulates Stun.",
      "Subtle takedown spell."
    ],
    src: "AWK", pg: 136 },

  { n: "Nutrition", cat: "health", typ: "M", rng: "T", dur: "P", drn: "(F+2)L",
    target: "4 (voluntary)", area: "Single subject",
    desc: "Provides a willing subject with a full day's nourishment.",
    effect: [
      "Permanent -- meal effect lasts a full day.",
      "Subject does not need to eat for the duration.",
      "Useful for extended ops, survival, refugee aid."
    ],
    src: "AWK", pg: 136 },

  { n: "Paralyze", cat: "health", typ: "M", rng: "LOS", dur: "S", drn: "(F+2)+1D",
    target: "Willpower (R)", area: "Single subject",
    desc: "Overrides voluntary muscle control.",
    effect: [
      "Sustained.",
      "Target rolls Willpower vs Power.",
      "Failure: subject cannot move or speak.",
      "Combat-disabling; brutal but useful for non-lethal capture."
    ],
    src: "AWK", pg: 136 },

  /* ============== Awakenings -- Illusion (p. 136-137) ============== */
  { n: "Agonizing Pain", cat: "illusion", typ: "M", rng: "LOS", dur: "S", drn: "(F+2)M",
    target: "Willpower (R)", area: "Single subject", dmg: "(successes) Stun",
    desc: "Wracks the target with phantom pain.",
    effect: [
      "Sustained, single-target.",
      "Target rolls Willpower vs Power.",
      "Failure: target suffers TN penalties from imagined-but-felt pain.",
      "Accumulates Stun over time."
    ],
    src: "AWK", pg: 136 },

  { n: "Chaff", cat: "illusion", typ: "P", rng: "LOS", dur: "S", drn: "(F+2)+1M",
    target: "4", area: "Within range",
    desc: "Fills the air with fake sensor returns.",
    effect: [
      "Sustained, area effect.",
      "Physical illusion: defeats radar, lidar, magnetic and electronic weapon-tracking.",
      "Useful against missile lock-ons and drone targeting."
    ],
    src: "AWK", pg: 136 },

  { n: "Crowd Scene", cat: "illusion", typ: "P", rng: "LOS", dur: "S", drn: "(F+2)+2M",
    target: "4", area: "Within range",
    desc: "Conjures sights and sounds of a milling crowd.",
    effect: [
      "Sustained, area effect.",
      "Physical illusion -- works on cameras and sensors.",
      "Useful for distractions, crowd cover, public confusion."
    ],
    src: "AWK", pg: 136 },

  { n: "Disregard", cat: "illusion", typ: "M", rng: "T", dur: "S", drn: "(F+2)L",
    target: "4 (Intelligence to notice)", area: "Single subject",
    desc: "Bystanders dismiss and overlook the subject.",
    effect: [
      "Sustained on touched subject.",
      "Observer rolls Willpower vs Power to actually notice the subject.",
      "Bystanders look past the subject unless given a specific reason.",
      "Premier infiltration spell -- subtler than Invisibility."
    ],
    src: "AWK", pg: 137 },

  { n: "Dream", cat: "illusion", typ: "M", rng: "LOS", dur: "S", drn: "(F+2)L",
    target: "Willpower (R)", area: "Single subject",
    desc: "Transmits a chosen vivid dream to a sleeping target.",
    effect: [
      "Sustained while target sleeps.",
      "Caster designs the dream content.",
      "Useful for psychological warfare, prophecy, communication with unreachable allies."
    ],
    src: "AWK", pg: 137 },

  { n: "Flare", cat: "illusion", typ: "P", rng: "LOS", dur: "I", drn: "(F+2)+1M",
    target: "Quickness (R)", area: "Within range",
    desc: "Burst of physical light that dazzles eyes and cyber-optics.",
    effect: [
      "Instant, area effect.",
      "Each observer in the affected area rolls Willpower (or sensor rating for tech) vs Power.",
      "Physical illusion -- blinds cybereyes too.",
      "Brief but effective combat opener."
    ],
    src: "AWK", pg: 137 },

  { n: "Silence", cat: "illusion", typ: "P", rng: "LOS", dur: "S", drn: "(F+2)S",
    target: "4", area: "Within range",
    desc: "Smothers all sound in an area.",
    effect: [
      "Sustained, area effect.",
      "Physical illusion: blocks acoustic sensors, microphones, and natural hearing.",
      "Essential for stealth operations.",
      "Communication inside the zone requires line of sight."
    ],
    src: "AWK", pg: 137 },

  /* ============== Awakenings -- Manipulation: Control (p. 137-138) ============== */
  { n: "Calm Animal", cat: "manipulation", typ: "M", rng: "LOS", dur: "S", drn: "(F+2)+2L",
    target: "Willpower/Essence (R)", area: "Single (animal)",
    desc: "Quiets a non-paranormal animal.",
    effect: [
      "Sustained.",
      "Animal rolls Willpower vs Power.",
      "Failure: animal becomes docile, stops hostile / agitated behavior.",
      "Useful against guard dogs, swarms, etc."
    ],
    src: "AWK", pg: 137 },

  { n: "Compel Truth", cat: "manipulation", typ: "M", rng: "LOS", dur: "S", drn: "(F+2)+2L",
    target: "Willpower (R)", area: "Single subject",
    desc: "Forces truthful answers.",
    effect: [
      "Sustained.",
      "Target rolls Willpower vs Power.",
      "Failure: target answers questions truthfully (as they understand truth).",
      "Doesn't compel volunteering info -- only forces truthful response to direct questions."
    ],
    src: "AWK", pg: 137 },

  { n: "False Memory", cat: "manipulation", typ: "M", rng: "LOS", dur: "P", drn: "(F+2)+2S",
    target: "Willpower (R)", area: "Single subject",
    desc: "Implants a fabricated memory.",
    effect: [
      "Permanent.",
      "Target rolls Willpower vs Power.",
      "Failure: caster designs a false memory; target recalls it as their own genuine experience.",
      "Used for misdirection, alibi-construction, mind-control follow-up."
    ],
    src: "AWK", pg: 138 },

  { n: "Possession", cat: "manipulation", typ: "M", rng: "LOS", dur: "S", drn: "(F+2)+2S",
    target: "Willpower (R)", area: "Single subject",
    desc: "Caster inhabits the target's body.",
    effect: [
      "Sustained.",
      "Target rolls Willpower vs Power.",
      "Failure: caster's mind controls target's body; target lies comatose in caster's body.",
      "If the caster's body is destroyed while possessing, caster's mind is trapped."
    ],
    src: "AWK", pg: 138 },

  { n: "Terrorize", cat: "manipulation", typ: "M", rng: "LOS", dur: "S", drn: "(F+2)+2S",
    target: "Willpower (R)", area: "Single subject",
    desc: "Floods target with overwhelming fear.",
    effect: [
      "Sustained.",
      "Target rolls Willpower vs Power.",
      "Failure: target experiences crippling fear -- may flee, cower, or be paralyzed."
    ],
    src: "AWK", pg: 138 },

  /* ============== Awakenings -- Manipulation: Telekinetic (p. 138) ============== */
  { n: "Catfall", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "(F+2)+2L",
    target: "4", area: "Single subject",
    desc: "Magically slows a falling subject.",
    effect: [
      "Sustained on subject.",
      "Subject falls slowly -- touches down without impact damage.",
      "Useful for parachute jumps, escape from windows, dramatic landings."
    ],
    src: "AWK", pg: 138 },

  { n: "Deflect", cat: "manipulation", typ: "P", rng: "T", dur: "S", drn: "(F+2)+1S",
    target: "6", area: "Single subject",
    desc: "Telekinetically nudges incoming projectiles aside.",
    effect: [
      "Sustained on touched subject.",
      "Each success on the cast gives +1 die to dodge / Reaction Tests against ranged attacks.",
      "Useful for bodyguard work."
    ],
    src: "AWK", pg: 138 },

  { n: "Fling", cat: "manipulation", typ: "P", rng: "T", dur: "I", drn: "(F+2)M",
    target: "Ranged Combat Test", area: "Single (object)", dmg: "by thrown object",
    desc: "Hurls a small object with telekinetic force.",
    effect: [
      "Instant.",
      "Used as a thrown ranged attack -- caster's Magic Pool can supplement Throwing Weapons.",
      "Damage from the thrown object (rocks, knives, etc.) plus telekinetic Power."
    ],
    src: "AWK", pg: 138 },

  { n: "Gecko Grip", cat: "manipulation", typ: "P", rng: "T", dur: "S", drn: "(F+2)+1M",
    target: "6", area: "Single subject",
    desc: "Allows subject to cling and climb vertical or inverted surfaces.",
    effect: [
      "Sustained on touched subject.",
      "Subject ignores normal Climbing penalties.",
      "Useful for infiltrators, urban explorers, ninjas."
    ],
    src: "AWK", pg: 138 },

  /* ============== Awakenings -- Manipulation: Transformation (p. 138-141) ============== */
  { n: "Alter Temperature", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "(F+2)+2S",
    target: "6", area: "Within range",
    desc: "Raises or lowers ambient temperature in a small area.",
    effect: [
      "Sustained.",
      "Force x degrees of change (rough guideline).",
      "Useful for environmental hazards, comfort, melting locks."
    ],
    src: "AWK", pg: 138 },

  { n: "Bug Barrier", cat: "manipulation", typ: "M", rng: "LOS", dur: "S", drn: "(F+2)+2D",
    target: "6", area: "Created barrier",
    desc: "Wall that repels and damages insect spirits.",
    effect: [
      "Sustained.",
      "Insect spirits attempting to cross suffer Power damage.",
      "Essential in Bug City and similar hot zones."
    ],
    src: "AWK", pg: 139 },

  { n: "Clean Air", cat: "manipulation", typ: "P", rng: "LOS", dur: "I", drn: "(F+2)+2S",
    target: "Object Resistance", area: "Within range",
    desc: "Strips smoke, fumes, and airborne pollutants from a volume.",
    effect: [
      "Instant cleansing of the area.",
      "Useful in tear-gassed rooms, smoke-filled areas, polluted air.",
      "Affects volume up to Force x cubic meters."
    ],
    src: "AWK", pg: 139 },

  { n: "Clean Water", cat: "manipulation", typ: "P", rng: "T", dur: "P", drn: "(F+2)S",
    target: "Object Resistance", area: "Within range",
    desc: "Removes contaminants from water.",
    effect: [
      "Permanent on the affected water.",
      "Useful for survival, refugee aid, anti-poisoning."
    ],
    src: "AWK", pg: 139 },

  { n: "Control Fire", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "(F+2)+2S",
    target: "Object Resistance", area: "Existing flames",
    desc: "Guides existing flames.",
    effect: [
      "Sustained.",
      "Caster directs flames to spread, shrink, or move.",
      "Requires existing fire -- cannot create.",
      "Use Ignite or Flame Bomb to start the fire."
    ],
    src: "AWK", pg: 139 },

  { n: "Extinguish Fire", cat: "manipulation", typ: "P", rng: "LOS", dur: "I", drn: "(F+2)+1S",
    target: "Object Resistance", area: "Within range",
    desc: "Snuffs out an area of natural fire.",
    effect: [
      "Instant.",
      "Each success reduces fire's Power; sufficient successes extinguish entirely.",
      "Useful for fire-fighting, escaping burning buildings."
    ],
    src: "AWK", pg: 139 },

  { n: "Firewall", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "(F+2)+2D",
    target: "Object Resistance", area: "Created wall", dmg: "(Force) Physical - fire (barrier)",
    desc: "Wall of flame.",
    effect: [
      "Sustained.",
      "Anyone crossing rolls Body vs Power.",
      "Dimensions scale with caster's Magic Rating.",
      "Useful for area denial."
    ],
    src: "AWK", pg: 139 },

  { n: "Fix", cat: "manipulation", typ: "P", rng: "T", dur: "P", drn: "(F+2)+1M",
    target: "Object Resistance", area: "Single object",
    desc: "Repairs damage to an object.",
    effect: [
      "Permanent.",
      "Each success heals 1 box of object damage / Barrier Rating point.",
      "Useful for vehicles, drones, equipment.",
      "Doesn't replace missing parts -- only mends existing material."
    ],
    src: "AWK", pg: 139 },

  { n: "Flame Aura", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "(F+2)+2M",
    target: "6 (voluntary)", area: "Single subject", dmg: "(Force) fire on contact",
    desc: "Surrounds subject with flames burning anyone in melee.",
    effect: [
      "Sustained on willing subject.",
      "Anyone striking the subject in melee takes Power damage from the flame aura.",
      "Subject is unharmed by their own aura.",
      "Useful for tank-mages."
    ],
    src: "AWK", pg: 140 },

  { n: "Freeze Water", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "(F+2)+2S",
    target: "Object Resistance", area: "Within range",
    desc: "Solidifies a body of water into ice.",
    effect: [
      "Sustained.",
      "Useful for emergency bridges, drowning trap escapes, freezing drinks.",
      "Volume scales with Force x Magic."
    ],
    src: "AWK", pg: 140 },

  { n: "Glue", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "(F+2)+2S",
    target: "6", area: "Single (surface)",
    desc: "Bonds touching surfaces with magical adhesion.",
    effect: [
      "Sustained.",
      "Bond strength = Force x adhesion factor.",
      "Useful for locking doors, sealing rooms, sticking enemies in place."
    ],
    src: "AWK", pg: 140 },

  { n: "Heat Shield", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "(F+2)+2M",
    target: "6 (voluntary)", area: "Single subject",
    desc: "Shields target from fire and heat attacks.",
    effect: [
      "Sustained.",
      "Reduces incoming heat-based Power by Force.",
      "Useful for fire-mage fights, demolitions cleanup."
    ],
    src: "AWK", pg: 140 },

  { n: "Light Ray", cat: "manipulation", typ: "P", rng: "LOS", dur: "I", drn: "(F+2)+1D",
    target: "4", area: "Single target", dmg: "(Force) Physical - Moderate - light",
    desc: "Fires a coherent laser-like beam of light.",
    effect: [
      "Instant, single-target.",
      "Target rolls Body vs Power.",
      "Physical damage from focused light.",
      "Doesn't ignite combustibles like normal fire."
    ],
    src: "AWK", pg: 140 },

  { n: "Mental Shield", cat: "manipulation", typ: "M", rng: "T", dur: "S", drn: "(F+2)+1M",
    target: "4 (voluntary)", area: "Single subject",
    desc: "Protects subject against mental probes and mana manipulations.",
    effect: [
      "Sustained on touched subject.",
      "Adds Force to Willpower for resisting mana-based mind-affecting spells.",
      "Useful for VIPs and corp executives."
    ],
    src: "AWK", pg: 140 },

  { n: "Mist", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "(F+2)+2S",
    target: "6", area: "Within range",
    desc: "Conjures a dense fog bank.",
    effect: [
      "Sustained, area effect.",
      "All vision tests inside suffer heavy TN penalty.",
      "Useful for cover, escape, ambush setup."
    ],
    src: "AWK", pg: 140 },

  { n: "Net", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "(F+2)+2L",
    target: "Quickness (R)", area: "Within range",
    desc: "Area-effect Bind that snares everyone caught in webbing.",
    effect: [
      "Sustained, area effect.",
      "Each target rolls Body vs Power.",
      "Failure: target is held in magical webbing; Strength test vs Force to break free."
    ],
    src: "AWK", pg: 141 },

  { n: "Sap Strength", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "(F+2)+2S",
    target: "4", area: "Single subject",
    desc: "Drains target's Strength.",
    effect: [
      "Sustained.",
      "Target rolls Body vs Power.",
      "Failure: target's Strength is reduced to a fraction of normal.",
      "Specifically targets Strength -- narrower than Decrease Attribute."
    ],
    src: "AWK", pg: 141 },

  { n: "Shape Earth", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "(F+2)+2D",
    target: "Object Resistance", area: "Within area",
    desc: "Moves and reshapes earth, soil, or stone.",
    effect: [
      "Sustained.",
      "Volume scales with Force x Magic.",
      "Useful for tunneling, fortification, ambush pits.",
      "Stone Resistance applies."
    ],
    src: "AWK", pg: 141 },

  { n: "Shape Water", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "(F+2)+2D",
    target: "Object Resistance", area: "Within area",
    desc: "Manipulates water or liquids.",
    effect: [
      "Sustained.",
      "Volume scales with Force x Magic.",
      "Useful for currents, water bridges, flooding tactics."
    ],
    src: "AWK", pg: 141 },

  { n: "Smoke Cloud", cat: "manipulation", typ: "P", rng: "LOS", dur: "S", drn: "(F+2)+3D",
    target: "4", area: "Radius = Magic (m)", dmg: "(Force) Stun - Moderate",
    desc: "Cloud of choking sulphurous smoke.",
    effect: [
      "Sustained, area effect.",
      "Each living target inside rolls Body vs Power.",
      "Obscures vision; inflicts Stun damage from inhalation.",
      "Drain D -- very expensive."
    ],
    src: "AWK", pg: 141 },

  { n: "Spirit Barrier", cat: "manipulation", typ: "M", rng: "LOS", dur: "S", drn: "(F+2)+2M",
    target: "6", area: "Created barrier",
    desc: "Wall that spirits cannot easily cross.",
    effect: [
      "Sustained.",
      "Spirits attempting to cross lose successes equal to Force.",
      "Useful for warding rooms against summoned threats."
    ],
    src: "AWK", pg: 141 },

  { n: "Temper", cat: "manipulation", typ: "P", rng: "T", dur: "P", drn: "(F+2)+1M",
    target: "Object Resistance", area: "Single object",
    desc: "Hardens an inanimate item.",
    effect: [
      "Permanent.",
      "Each success adds Force to the item's Barrier Rating.",
      "Useful for fortifying doors, weapons, vehicles."
    ],
    src: "AWK", pg: 141 },

  { n: "Wind", cat: "manipulation", typ: "P", rng: "LOS", dur: "I", drn: "(F+2)+1S",
    target: "6", area: "Within range",
    desc: "Powerful gust of wind.",
    effect: [
      "Instant, area effect.",
      "Targets in path roll Body vs Power; failure: staggered or knocked back.",
      "Scatters loose objects, can disrupt smoke clouds or chemicals."
    ],
    src: "AWK", pg: 141 },

];
