/* =============================================================
   Adept Powers catalogue (37 entries) compiled from:
   - Shadowrun, Second Edition (FASA7901) pp. 125-126  (9 powers)
   - Grimoire 2nd Edition (FASA7903)     p. 34          (6 powers)
   - Awakenings (FASA7120)               pp. 115-119    (22 powers)

   Game-stat fields (n, pp, tiers, effect bullets, act, src, pg)
   are facts from the book; `desc` is paraphrased original language.

   Field reference:
     n      - power name
     pp     - PP cost headline ("2 PP" or "0.5 / 1 / 2 PP")
     act    - activation type:
              "always"     Always on (passive, permanent)
              "toggle"     Turn on/off at no cost
              "action"     Costs an action to use
              "reaction"   Triggers reactively when conditions met
              "activated"  Activated effect with Drain (the only spell-like one)
              "special"    Unique activation rule -- see effect bullets
     tiers  - optional inline tier-cost breakdown
     desc   - one-sentence original description
     effect - array of mechanical-effect bullets
     src    - SR2 | GRIM | AWK
     pg     - printed page number
   ============================================================= */

window.ADEPT_POWERS = [

  /* ============ SR2 CORE (pp. 125-126) ============ */
  { n: "Astral Perception", pp: "2 PP", act: "toggle",
    desc: "Toggleable astral sight -- the adept perceives astral space at will.",
    effect: [
      "Activated / deactivated as a Simple Action.",
      "Adept uses normal Combat Pool dice for astral combat while perceiving.",
      "Adept CANNOT astrally project -- only perceive."
    ],
    src: "SR2", pg: 125 },

  { n: "Combat Sense", pp: "2 / 3 / 4 PP", act: "always",
    tiers: "Lv 1: +1 Combat Pool die - Lv 2: +2 - Lv 3: +3",
    desc: "A sixth-sense awareness in combat -- never surprised, plus extra Combat Pool dice.",
    effect: [
      "Each level grants +1 die to the adept's Combat Pool.",
      "Adept is never surprised -- gets a free defensive Reaction Test against ambush."
    ],
    src: "SR2", pg: 125 },

  { n: "Improved Ability", pp: "0.25 - 1 PP per die", act: "always",
    tiers: "Athletics & Stealth: 0.25/die - Armed/Unarmed/Throwing/Projectile: 0.5/die - Firearms & Gunnery: 1/die",
    desc: "Buys extra dice for one chosen Skill -- permanently baked into every roll.",
    effect: [
      "Bonus dice apply to the general Skill AND inherit to its Concentrations and Specializations.",
      "Cap (Combat Skills only): bonus dice <= current general Skill Rating. Firearms 4 cannot have more than 4 Improved Ability dice.",
      "Skill-Web defaulting: lose 1 Improved Ability die per circle crossed, on top of the +2 TN per circle.",
      "No activation -- dice are always in the skill pool."
    ],
    src: "SR2", pg: 125 },

  { n: "Improved Physical Attributes", pp: "0.5 / 1 / 1.5 PP per +1", act: "always", rated: true, maxLevel: 6, attrChoice: true, ppTier: [0.5, 1, 1.5], modsAttr: 1,
    tiers: "Up to 1/2 racial max: 0.5 per +1 - up to racial max: 1 per +1 - up to 1.5x racial max: 1.5 per +1",
    desc: "Permanently raise Body, Quickness, or Strength -- augments the Attribute itself.",
    effect: [
      "One Physical Attribute per purchase (Body, Quickness, or Strength). Multiple purchases stack.",
      "Cap: 1.5 x Racial Maximum for that Attribute.",
      "Cost climbs as the rating passes half the racial max, then the racial max itself.",
      "Always on -- the Attribute is simply higher."
    ],
    src: "SR2", pg: 125 },

  { n: "Improved Physical Senses", pp: "0.25 PP per level", act: "always",
    desc: "Sensory upgrade -- one enhancement per level, chosen when bought.",
    effect: [
      "Each level grants one sense modification. The adept can buy as many as wanted.",
      "SR2 core options include: Low-Light Vision, Thermographic Vision, hearing-range extension, scent/taste enhancement.",
      "Awakenings expands the list with: Flare Compensation, High-Frequency Hearing, Improved Scent, Improved Taste, Low-Frequency Hearing, Sound Dampening.",
      "Effects identical to the matching cyberware sensory mods -- without the Essence hit."
    ],
    src: "SR2", pg: 125 },

  { n: "Increased Reaction", pp: "0.5 / 1 / 2 PP per +1", act: "always", rated: true, maxLevel: 6, ppTier: [0.5, 1, 2], modsPer: { reaction: 1 },
    tiers: "Up to 1/2 racial max: 0.5 - up to racial max: 1 - up to 1.5x max: 2",
    desc: "Direct boost to the Reaction Attribute -- no initiative dice (those are Increased Reflexes).",
    effect: [
      "Adds +N to Reaction Rating (used for initiative score and dodging).",
      "Does NOT add initiative dice -- those are bought separately via Increased Reflexes.",
      "Cap: 1.5 x Racial Maximum for Reaction.",
      "Always on -- Reaction is simply higher."
    ],
    src: "SR2", pg: 126 },

  { n: "Increased Reflexes", pp: "1 / 3 / 6 PP", act: "always", rated: true, maxLevel: 3, ppTbl: [1, 3, 6], modsPer: { initDice: 1 },
    tiers: "+1 init die: 1 - +2 dice: 3 - +3 dice: 6",
    desc: "Buy extra initiative dice -- adept's answer to Wired Reflexes without the Essence cost.",
    effect: [
      "Adds +1 / +2 / +3 initiative dice to every combat turn.",
      "Does NOT add to Reaction -- that's Increased Reaction.",
      "Buy once at a chosen level; later levels require Karma.",
      "Always on -- extra dice are rolled every turn automatically."
    ],
    src: "SR2", pg: 126 },

  { n: "Killing Hands", pp: "0.5 / 1 / 2 / 4 PP", act: "toggle",
    tiers: "(Str)L: 0.5 PP - (Str)M: 1 PP - (Str)S: 2 PP - (Str)D: 4 PP -- Power = Strength, Damage Level chosen at purchase",
    desc: "Adept's unarmed strikes can deal real Physical damage at the chosen level.",
    effect: [
      "Damage Power = Strength. Damage Level = the L/M/S/D you bought.",
      "Counts as a magical weapon -- affects critters with Immunity to Normal Weapons.",
      "Improved Ability for Unarmed Combat (and other unarmed bonuses) still apply on top.",
      "Toggle -- the adept chooses round-by-round whether to use Killing Hands or strike for Stun normally."
    ],
    src: "SR2", pg: 126 },

  { n: "Pain Resistance", pp: "0.5 PP per point ignored", act: "always",
    desc: "Ignore wound modifiers -- keep fighting through injuries that slow others.",
    effect: [
      "Each point ignored = one box of damage whose wound modifiers don't apply.",
      "Practical cap ~ 10 points (Deadly is 10 boxes -- beyond that the adept simply drops).",
      "DOES NOT prevent the damage itself, only the TN penalties it would impose.",
      "Doesn't prevent unconsciousness or death at Deadly damage.",
      "Always on -- the modifiers simply don't apply."
    ],
    src: "SR2", pg: 126 },

  /* ============ Grimoire 2e (p. 34) ============ */
  { n: "Attribute Boost", pp: "0.5 PP per Level", act: "activated",
    desc: "Briefly surge one Physical Attribute past its racial maximum -- at the cost of Drain.",
    effect: [
      "Activated as an action. Each level adds +1 Rating to a chosen Physical Attribute for the boost's duration.",
      "Maximum effective boost = the levels of the power purchased.",
      "Inflicts DRAIN damage when the boost ends, scaled to the rating used. The body pays for the surge.",
      "One Physical Attribute is chosen at purchase; buying for a different Attribute is a separate purchase.",
      "The ONLY adept power that resembles spellcasting -- it has drain and a temporary effect."
    ],
    src: "GRIM", pg: 34 },

  { n: "Body Control", pp: "5 PP per skill category", act: "always",
    desc: "Magical resistance to drugs, toxins, and poisons within a chosen category.",
    effect: [
      "Adds a Body-based Damage Resistance Test against poisons/toxins/drugs from one chosen category.",
      "Categories must each be bought separately -- narcotics, neurotoxins, etc. are different categories.",
      "Successes on the Body test reduce the chemical's effect.",
      "Always on -- Body roll triggers automatically when exposure happens."
    ],
    src: "GRIM", pg: 34 },

  { n: "Enhanced Centering", pp: "2 PP per Skill Category", act: "always",
    desc: "Use a non-physical Skill as a Centering Skill to soak drain.",
    effect: [
      "Allows a Skill from a chosen category to be used as a Centering Skill against Drain.",
      "Each Skill Category (Build/Repair, Combat, Knowledge, Language, Magical, Social, Technical, Vehicle) must be purchased separately.",
      "Centering reduces Drain levels per the standard Centering rules.",
      "Always on -- the option is just available."
    ],
    src: "GRIM", pg: 34 },

  { n: "Missile Parry", pp: "1 PP", act: "reaction",
    desc: "Deflect slow-moving thrown missiles like arrows, shuriken, and javelins.",
    effect: [
      "Triggers when targeted by a slow physical missile (arrows, shuriken, thrown weapons).",
      "Costs a Reaction Test against the attacker's success roll.",
      "On success, the missile is deflected harmlessly.",
      "Does NOT work against bullets or other fast projectiles."
    ],
    src: "GRIM", pg: 34 },

  { n: "Mystic Armor", pp: "1 PP per level", act: "always",
    desc: "Magical armor that stacks against both Physical and Mana attacks.",
    effect: [
      "Each level adds 1 point of armor against ALL incoming attacks (Physical AND Mana).",
      "Cannot be defeated by armor-piercing rounds -- only by a successful Magic Test from the attacker.",
      "Stacks with worn armor and Dermal Plating.",
      "Always on -- armor is just there."
    ],
    src: "GRIM", pg: 34 },

  { n: "Suspended State", pp: "1 PP", act: "special",
    desc: "Self-induced hibernation -- slow metabolism for survival or stealth.",
    effect: [
      "Voluntarily entered as an extended action.",
      "Heart rate, breathing, and metabolism slow drastically.",
      "Injuries, thirst, hunger, and infection progress at a fraction of normal speed.",
      "Adept can be awakened at will or by external stimulus.",
      "Has indefinite duration but the adept is unconscious / immobile while in the state."
    ],
    src: "GRIM", pg: 34 },

  /* ============ Awakenings (pp. 115-119) ============ */
  { n: "Blind Fighting", pp: "0.5 PP", act: "always",
    desc: "Fight effectively when blinded -- mystical senses fill in for vision.",
    effect: [
      "Halves the TN penalty from being blinded (smoke, darkness, flashbangs, sealed eyes).",
      "Removes the +TN bonus enemies normally gain against an unaware target when the adept is blind.",
      "Always on -- kicks in automatically when sight is lost."
    ],
    src: "AWK", pg: 115 },

  { n: "Counterstrike", pp: "0.5 PP per level", act: "reaction",
    desc: "After being missed in unarmed combat, immediately counter with a free attack.",
    effect: [
      "Triggers when an attacker MISSES the adept in unarmed combat.",
      "Adept makes a free unarmed Counterstrike at no penalty.",
      "Each level grants one additional counter-attack per turn.",
      "Only applies to Unarmed Combat exchanges."
    ],
    src: "AWK", pg: 115 },

  { n: "Delay Damage", pp: "2 PP", act: "special",
    desc: "One-use: postpone an attack's effects so the adept can finish a critical action.",
    effect: [
      "Declared after taking damage from a single attack.",
      "Damage and wound modifiers DO NOT apply during the delay (typically up to several hours).",
      "When the delay ends, all damage applies at once -- adept may collapse immediately.",
      "One-use per situation per GM ruling -- not a recurring effect."
    ],
    src: "AWK", pg: 115 },

  { n: "Distance Strike", pp: "2 PP", act: "action",
    desc: "Project a kinetic strike at range as if punching from close in.",
    effect: [
      "Costs the adept's normal Unarmed Combat attack action.",
      "Adept makes an Unarmed Combat attack against a target at medium range.",
      "Resolved as a normal Unarmed Combat Test (with Killing Hands applying if bought).",
      "Requires Unarmed Combat (martial-arts) Skill."
    ],
    src: "AWK", pg: 116 },

  { n: "Empathic Sense", pp: "0.5 PP", act: "always",
    desc: "Vague awareness of nearby emotional states and hidden magic.",
    effect: [
      "Adept senses the general emotional state (anger, fear, calm) of nearby people.",
      "Can quietly defeat magical Masking on initiates -- adept perceives the disguised aura.",
      "Always on -- passive ambient awareness."
    ],
    src: "AWK", pg: 116 },

  { n: "Enhanced Coordination", pp: "0.5 PP per level", act: "always",
    desc: "Hands and feet ambidextrous -- reduces off-hand penalty.",
    effect: [
      "Each level adds an effective Ambidexterity level for both hands and feet.",
      "Reduces or eliminates the off-hand TN penalty (per standard Ambidexterity rules).",
      "Always on -- no activation."
    ],
    src: "AWK", pg: 116 },

  { n: "Flexibility", pp: "0.25 PP per level", act: "always",
    desc: "Preternaturally supple limbs -- escape and contortion specialist.",
    effect: [
      "Each level reduces TN modifiers for contortion, escape, and tight-space maneuvers by 1.",
      "Useful with Escape Artist (Awakenings) and Athletics (Climbing concentration).",
      "Always on."
    ],
    src: "AWK", pg: 116 },

  { n: "Freefall", pp: "0.25 PP per level", act: "always",
    desc: "Mystically cushion falls -- soak impact damage like a cat.",
    effect: [
      "Each level adds one automatic success to the falling Damage Resistance Test.",
      "Stacks with the adept's Body roll on that test.",
      "Always on -- triggers automatically when falling."
    ],
    src: "AWK", pg: 116 },

  { n: "Iron Will", pp: "0.5 PP per level", act: "always",
    desc: "Mental resistance against mind-affecting magic.",
    effect: [
      "Each level adds 1 die to resist Control, Illusion, and Influence spells specifically.",
      "Levels apply on top of normal Willpower resistance dice.",
      "Always on -- adds to the resistance roll automatically."
    ],
    src: "AWK", pg: 117 },

  { n: "Magic Resistance", pp: "1 PP per level", act: "always",
    desc: "Always-on spell defense -- every hostile sorcery gets harder.",
    effect: [
      "Each level adds 1 die to resist ANY hostile sorcery.",
      "Works exactly like spell defense -- the adept always has it active without thinking about it.",
      "Does not require a Sorcery skill -- the adept never casts, only resists.",
      "Always on -- no toggle, no expiry."
    ],
    src: "AWK", pg: 117 },

  { n: "Magic Sense", pp: "1 PP", act: "toggle",
    desc: "Toggle-on minor astral awareness with a 5-meter range.",
    effect: [
      "Detects active magical effects and bonded foci within 5 meters.",
      "Does NOT perceive astral space generally -- just the magical activity near the adept.",
      "Toggle on/off as a Free Action."
    ],
    src: "AWK", pg: 117 },

  { n: "Missile Mastery", pp: "1 PP", act: "always",
    desc: "Throw ordinary objects as deadly weapons.",
    effect: [
      "Adept can use Throwing Weapons skill with improvised objects of similar weight.",
      "Improves accuracy of normal thrown weapons -- reduces TN modifiers on Throwing tests.",
      "Damage from improvised throws is GM-adjudicated based on object.",
      "Always on."
    ],
    src: "AWK", pg: 117 },

  { n: "Nerve Strike", pp: "1 PP", act: "action",
    desc: "Touch attack that delivers Stun, ignoring armor.",
    effect: [
      "Costs the adept's normal Unarmed Combat attack action (or Touch attack).",
      "Damage = Stun, at Power equal to Strength and Damage Level chosen at purchase.",
      "Bypasses armor (no ballistic or impact reduction).",
      "Target rolls Body to resist as normal."
    ],
    src: "AWK", pg: 117 },

  { n: "Quick Draw", pp: "3 PP", act: "action",
    desc: "Ready and use a weapon in a single action -- no draw-then-fire penalty.",
    effect: [
      "Adept may draw AND fire a pistol, or draw AND attack with a melee weapon, in one Simple Action.",
      "Eliminates the normal +2 TN penalty for drawing and attacking in the same turn.",
      "Applies once per turn."
    ],
    src: "AWK", pg: 117 },

  { n: "Quick Strike", pp: "0.25 PP per level", act: "always",
    desc: "Surprise-attack specialist -- enemies struggle to react.",
    effect: [
      "Each level reduces the surprise-test bonus enemies get when the adept initiates sudden combat.",
      "Effectively makes the adept harder to react to in surprise rounds.",
      "Mostly relevant in ambush / first-strike situations.",
      "Always on -- applies automatically when initiating combat."
    ],
    src: "AWK", pg: 118 },

  { n: "Rapid Healing", pp: "0.5 PP per level", act: "always",
    desc: "Recover from injury much faster than normal.",
    effect: [
      "Each level adds 1 die to the adept's natural Healing Test.",
      "Affects only natural healing -- not magical Heal spell results.",
      "Useful between sessions or long down-time.",
      "Always on -- added to healing rolls automatically."
    ],
    src: "AWK", pg: 118 },

  { n: "Rooting", pp: "0.25 PP per level", act: "always",
    desc: "Anchor the body -- hard to knock down, throw, or move.",
    effect: [
      "Each level adds +1 TN against being knocked down, thrown, grappled, or moved against the adept's will.",
      "Applies to physical and magical attempts to move the adept.",
      "Always on -- the resistance is constant."
    ],
    src: "AWK", pg: 118 },

  { n: "Sixth Sense", pp: "3 PP", act: "always",
    desc: "Precognitive warning of personal danger.",
    effect: [
      "Adept cannot be surprised by attacks directed at the adept personally.",
      "Free defensive Perception Test against incoming threats.",
      "Does not warn of dangers to others or general environmental hazards.",
      "Always on -- works automatically."
    ],
    src: "AWK", pg: 118 },

  { n: "Smashing Blow", pp: "1 PP", act: "action",
    desc: "Barrier-breaking unarmed strike -- punch through walls.",
    effect: [
      "Costs the adept's normal Unarmed Combat attack action.",
      "Unarmed strike's Power doubles when attacking inanimate barriers (walls, doors, furniture).",
      "Effective for breaking down doors, walls, restraints.",
      "Does not increase damage against living targets -- only barriers."
    ],
    src: "AWK", pg: 118 },

  { n: "Spell Shroud", pp: "0.25 PP per level", act: "always",
    desc: "Magical concealment from detection sorcery.",
    effect: [
      "Each level adds +1 TN to Detection-category spells trying to locate or perceive the adept.",
      "Includes Detect Individual, Mind Probe, Clairvoyance, and similar.",
      "Always on -- does not require activation."
    ],
    src: "AWK", pg: 119 },

  { n: "Temperature Tolerance", pp: "0.25 PP per level", act: "always",
    desc: "Resist extreme heat and cold -- Body bonus to environmental tests.",
    effect: [
      "Each level adds 1 die to the adept's Body roll for resisting heat or cold damage.",
      "Applies to environmental exposure (cold weather, fire, freezing water).",
      "Does not affect heat/cold damage from spells or weapons directly.",
      "Always on."
    ],
    src: "AWK", pg: 119 },

  { n: "Traceless Walk", pp: "0.5 PP", act: "always",
    desc: "Leave no trace -- physical or astral -- when moving.",
    effect: [
      "Adept leaves no footprints, scent, broken twigs, or other physical tracking signs.",
      "Leaves no astral signature for astral trackers.",
      "Ground sensors and motion detectors do not register the adept's passage.",
      "Always on -- no activation required."
    ],
    src: "AWK", pg: 119 },

];
