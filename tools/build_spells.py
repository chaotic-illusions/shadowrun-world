"""Rebuild ``app/data/catalog/spells.json`` from the book transcription below.

Every stat and effect line here is taken from the printed spell descriptions:
Shadowrun Second Edition (SR2) pp.151-158, The Grimoire Second Edition (GRIM)
pp.126-132, and Awakenings (AWK) pp.130-141. Do not add mechanics that are not
in those books. Where a description and the book's Table of Spells disagree the
table is used (Stun Bolt, Spell Barrier, Foretelling).

Run from the repo root:

    python tools/build_spells.py
"""
from __future__ import annotations

import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "app" / "data" / "catalog" / "spells.json"

W = "Willpower (R)"
B = "Body (R)"
ORT = "Object Resistance Table"
ONE = "Single target"
AREA = "Area effect"
LEVELS = {"L": "Light", "M": "Moderate", "S": "Serious", "D": "Deadly"}

SPELLS: list[dict] = []


def drain(mod: int, level: str) -> str:
    if not mod:
        return f"(F/2){level}"
    return f"[(F/2){'+' if mod > 0 else '-'}{abs(mod)}]{level}"


def add(n, cat, src, pg, typ, rng, dur, drn, target, area, desc, effect=(), dmg=None, turns=None):
    s = {"n": n, "cat": cat, "typ": typ, "rng": rng, "dur": dur}
    if turns:
        s["turns"] = turns
    s.update({"drn": drn, "target": target, "area": area})
    if dmg:
        s["dmg"] = dmg
    s.update({"desc": desc, "effect": list(effect), "src": src, "pg": pg})
    SPELLS.append(s)


# ---------------------------------------------------------------- SR2: combat (p.151)
add("Fireball", "combat", "SR2", 151, "P", "LOS", "I", drain(3, "D"), B, AREA,
    "An area-effect spell that causes Physical damage.",
    ["Can ignite combustible materials in its blast area, at the gamemaster's discretion."], dmg="Serious Physical")
add("Hellblast", "combat", "SR2", 151, "P", "LOS", "I", drain(6, "D"), B, AREA,
    "An area-effect spell that causes Physical damage.",
    ["Can ignite combustible materials in its blast area, at the gamemaster's discretion."], dmg="Deadly Physical")
add("Mana Bolt", "combat", "SR2", 151, "M", "LOS", "I", drain(0, "S"), W, ONE,
    "A powerful bolt of magical energy that causes Physical damage.", dmg="Serious Physical")
add("Mana Dart", "combat", "SR2", 151, "M", "LOS", "I", drain(0, "L"), W, ONE,
    "A small dart of magical power that does Physical damage.", dmg="Light Physical")
add("Mana Missile", "combat", "SR2", 151, "M", "LOS", "I", drain(0, "M"), W, ONE,
    "A bolt of magical power that causes Physical damage.", dmg="Moderate Physical")
add("Manaball", "combat", "SR2", 151, "M", "LOS", "I", drain(0, "S"), W, AREA,
    "An area-effect spell that causes Physical damage.",
    ["This mana version affects only living targets."], dmg="Moderate Physical")
add("Power Bolt", "combat", "SR2", 151, "P", "LOS", "I", drain(1, "S"), B, ONE,
    "The physical version of Mana Bolt: a powerful bolt of magical energy that causes Physical damage.",
    dmg="Serious Physical")
add("Power Dart", "combat", "SR2", 151, "P", "LOS", "I", drain(1, "L"), B, ONE,
    "The physical version of Mana Dart: a small dart of magical power that does Physical damage.",
    dmg="Light Physical")
add("Power Missile", "combat", "SR2", 151, "P", "LOS", "I", drain(1, "M"), B, ONE,
    "The physical version of Mana Missile: a bolt of magical power that causes Physical damage.",
    dmg="Moderate Physical")
add("Powerball", "combat", "SR2", 151, "P", "LOS", "I", drain(1, "S"), B, AREA,
    "The physical version of Manaball: an area-effect spell that causes Physical damage.",
    dmg="Moderate Physical")
add("Ram", "combat", "SR2", 151, "P", "LOS", "I", drain(1, "S"), ORT, ONE,
    "Damages inanimate targets.",
    ["Add the casting's successes to the spell's Force and compare the total to the target's Barrier Rating to find the effect (Barriers, SR2 p.98).",
     "Against a vehicle, use its Body plus any vehicle armor as the Barrier Rating. Each indicated reduction does Light damage to the vehicle rather than lowering its Body.",
     "The target number comes from the Object Resistance Table (SR2 p.130)."], dmg="Serious")
add("Sleep", "combat", "SR2", 151, "M", "LOS", "I", drain(-1, "S"), W, AREA,
    "An area-effect spell that causes Stun damage to living targets only.", dmg="Moderate Stun")

# ---------------------------------------------------------------- SR2: detection (p.153)
add("Analyze Device", "detection", "SR2", 153, "P", "Limited", "S", drain(1, "M"), ORT, ONE,
    "The magician can analyze the purpose and basic operation of a device or piece of equipment.",
    ["A specific hypersense spell requiring a voluntary subject.",
     "The base target number is the object's resistance (Object Resistance Table, SR2 p.130).",
     "Previous familiarity with the device or similar objects reduces the target number by 2."])
add("Analyze Truth", "detection", "SR2", 153, "M", "Limited", "S", drain(0, "S"), W, ONE,
    "The magician can tell whether a target's statement is the truth or not.",
    ["A hypersense spell. The target resists with Willpower against the spell's Force, reducing the caster's successes.",
     "The caster needs at least 1 success to determine validity.",
     "Does not work on written materials: the magician must hear the statement."])
add("Clairvoyance", "detection", "SR2", 153, "M", "Limited", "S", drain(0, "M"), "4", ONE,
    "The magician can see distant scenes as if present, out to the range of the new sense.",
    ["A hypersense spell requiring a voluntary subject.",
     "The magician must concentrate to use the sense and cannot use physical vision while doing so.",
     "Spells cannot be cast at a target seen using clairvoyance.",
     "Does not translate sound."])
add("Clairaudience", "detection", "SR2", 153, "M", "Limited", "S", drain(0, "M"), "4", ONE,
    "The magician can hear distant sounds as if present, out to the range of the new sense.",
    ["A hypersense spell.",
     "The magician must concentrate to use the sense and cannot use physical hearing while doing so.",
     "Does not translate visual images."])
add("Combat Sense", "detection", "SR2", 153, "P", "Limited", "S", drain(1, "S"), "4", ONE,
    "The subject becomes able to subconsciously analyze combat and other dangerous situations, sensing events a split second before they occur.",
    ["A hypersense spell requiring a voluntary subject.",
     "Every 2 successes add 1 die to the subject's Combat Pool for the duration of the spell."])
add("Detect Enemies", "detection", "SR2", 153, "M", "Limited", "S", drain(1, "M"), "4", AREA,
    "Within range, detects living beings who have hostile intentions toward the subject of the spell.",
    ["An area-effect, general hypersense spell requiring a voluntary subject.",
     "Would not detect a trap (it is not alive) or a terrorist about to shoot into a crowd at random (the intention is not personal)."])
add("Detect Individual", "detection", "SR2", 153, "M", "Limited", "S", drain(0, "L"), "10 − target's Essence (or Magic)", AREA,
    "Detects the presence of a particular individual, named when the spell is cast.",
    ["An area-effect, general hypersense spell requiring a voluntary subject.",
     "Target number is 10 minus the target's Essence if the target is mundane, or 10 minus the target's Magic Rating (or Force or Essence, as appropriate) if the target is magically active."])
add("Detect Life", "detection", "SR2", 153, "M", "Limited", "S", drain(0, "L"), "4", AREA,
    "The magician detects all living beings within range and knows their number and position.",
    ["An area-effect, general hypersense spell requiring a voluntary subject.",
     "Virtually useless in a crowded area, where it picks up a blurred mass of traces."])
add("Detect (Life Form)", "detection", "SR2", 153, "M", "Limited", "S", drain(-1, "L"), "4", AREA,
    "The magician detects a specified type of life form within range (detect ork, detect dragon, and so forth).",
    ["An area-effect, general hypersense spell.", "Each variation is a separate spell."])
add("Detect (Object)", "detection", "SR2", 153, "P", "Limited", "S", drain(1, "M"), "4", AREA,
    "The magician detects a specified type of object within range (detect guns, detect computers, detect cameras, and so forth).",
    ["An area-effect, general hypersense spell.", "Each variation is a separate spell."])
add("Mind Probe", "detection", "SR2", 153, "M", "T", "S", drain(2, "D"), "4 (R)", ONE,
    "The magician can telepathically probe a subject's mind.",
    ["The target resists with Willpower against the spell's Force. The successes left over set how deep the probe goes.",
     "1 success: read surface thoughts, what the target is thinking at that instant.",
     "2 successes: find out anything the subject knows consciously. Ask one question, which the target must answer truthfully.",
     "3 or more successes: enter the target's subconscious and obtain the answer to two questions.",
     "Additional castings against the same target within a number of hours equal to the target's Willpower are at +2 per attempt."])
add("Personal Combat Sense", "detection", "SR2", 153, "P", "Self", "S", drain(1, "M"), "4", "Self",
    "The personal form of the Combat Sense spell: it affects only the caster.",
    ["Every 2 successes add 1 die to the caster's Combat Pool for the duration of the spell."])

# ---------------------------------------------------------------- SR2: health (pp.154-155)
for lv, turns in zip("LMSD", (5, 10, 15, 20)):
    add(f"Antidote {lv} Toxin", "health", "SR2", 154, "P", "T", "P", drain(0, lv), "Toxin's Strength", ONE,
        f"Acts against a toxin (poison or drug) of {LEVELS[lv]} Damage Level in the subject's body.",
        ["Must be used before the toxin damages the victim.",
         "Each success reduces the Strength of the toxin by 1, making the subject's own Resistance Tests easier.",
         "A separate version of the spell exists for each toxin Damage Level."], turns=turns)
for lv, turns in zip("LMSD", (5, 10, 15, 20)):
    add(f"Cure {lv} Disease", "health", "SR2", 154, "P", "T", "P", drain(0, lv), "Disease's Virulence", ONE,
        f"Kills the germs of a disease of {LEVELS[lv]} Damage Level in the patient's system and eliminates any symptoms at once.",
        ["Can be used at any point after infection.",
         "Each success reduces the Virulence (Power) of the disease by 1, making the subject's own Resistance Tests easier.",
         "Does not heal damage already done by the disease; that takes a separate healing spell.",
         "A separate version of the spell exists for each disease Damage Level."], turns=turns)
for n, lv in zip((1, 2, 3, 4), "LMSD"):
    add(f"Decrease -{n} Attribute", "health", "SR2", 154, "P", "T", "S", drain(1, lv), "10 − target's Essence (R)", ONE,
        f"Reduces one of the target's Attributes by {n}.",
        ["The target resists with the Attribute being attacked, not necessarily Body. The magician needs only 1 net success.",
         "If a Physical Attribute is reduced to 0 the victim is unconscious or paralyzed; at a Mental Attribute of 0 the victim stands about mindlessly.",
         "A separate version of the spell exists for each Physical and Mental Attribute and for Reaction. Other Special Attributes cannot be affected.",
         "Does not affect targets with cyberware modifiers to the Attribute."])
for lv, turns in zip("LMSD", (5, 10, 15, 20)):
    add(f"Detox {lv} Toxin", "health", "SR2", 154, "P", "T", "P", drain(-2, lv), "Toxin's Strength", ONE,
        f"Relieves the effects of a drug or poison of {LEVELS[lv]} Damage Level.",
        ["Must overcome the toxin as the Antidote spell does.",
         "Does not heal damage from toxins, but eliminates their other effects on the victim (dizziness, hallucinations, nausea, pain, and so on).",
         "A separate version of the spell exists for each toxin Damage Level."], turns=turns)
for n, lv in zip((1, 2, 3, 4), "LMSD"):
    effect = ["A single success is sufficient.",
              "A separate version of the spell exists for each Physical and Mental Attribute and for Reaction. Other Special Attributes cannot be increased.",
              "Does not affect cybernetically modified Attributes; those need Increase Cybered Attribute.",
              "Does not stack with other Increase Attribute spells of the same type. Cast on an already magically boosted Attribute (such as a physical adept's), the target number is +4."]
    if n < 4:
        nxt = "MSD"[n - 1]
        effect.append(f"The Increase Reaction version has Drain one level higher: {drain(1, nxt)}, and it raises only the Reaction Rating.")
    else:
        effect.append("There is no Increase Reaction +4 spell.")
    add(f"Increase +{n} Attribute", "health", "SR2", 154, "M", "T", "S", drain(1, lv), "2 × the Attribute's rating", ONE,
        f"Increases one of the subject's normal Attributes by {n}.", effect)
for n, lv in zip((1, 2, 3, 4), "LMSD"):
    effect = ["A single success is sufficient.",
              "Works like Increase Attribute, but on Attributes already affected by cybernetics."]
    if n == 4:
        effect.append("Increase Cybered Reaction +4 has a Drain Code of [(F/2)+5]D.")
    add(f"Increase +{n} Cybered Attribute", "health", "SR2", 155, "P", "T", "S", drain(3, lv), "2 × the Attribute's rating", ONE,
        f"Increases one of the subject's cybernetically modified Attributes by {n}.", effect)
for n, lv in zip((1, 2, 3), "MSD"):
    add(f"+{n} Initiative Di{'e' if n == 1 else 'ce'}", "health", "SR2", 155, "M", "T", "S", drain(0, lv), "2 × subject's Reaction", ONE,
        f"Increase Reflexes: adds {n} Initiative di{'e' if n == 1 else 'ce'} to a voluntary subject.",
        ["There is no cybered version: characters with cybernetic enhancements that add Initiative dice (such as wired reflexes) cannot be boosted by this spell."])
HEALING = ["Each success on the Spell Success Test heals 1 box of damage.",
           "The spell must be maintained for a base time set by the subject's wound level: Deadly 20 turns, Serious 15, Moderate 10, Light 5.",
           "Successes can be split between healing boxes of damage and reducing that base time (divide the time by the successes used).",
           "The Drain Level equals the subject's current Wound Level: Light, Moderate, Serious or Deadly.",
           "A character can be magically treated or healed only once for any single set of injuries, and a successful casting also rules out first aid.",
           "Reduces Physical overflow damage."]
add("Treat", "health", "SR2", 155, "M", "T", "P", "(F/2)(Wound)", "8 − subject's Essence", ONE,
    "Heals an injured subject. Must be applied within one hour of the injury.",
    ["Must be applied within one hour of the injury to have any effect; after that, use Heal."] + HEALING)
add("Heal", "health", "SR2", 155, "M", "T", "P", "(F/2)(Wound)", "10 − subject's Essence", ONE,
    "Heals an injured subject. May be applied at any time after the injury.",
    ["May be applied at any time, unlike Treat, which must be applied within one hour."] + HEALING)

# ---------------------------------------------------------------- SR2: illusion (pp.155-156)
add("Chaos", "illusion", "SR2", 155, "P", "LOS", "S", drain(2, "M"), "Intelligence (R)", ONE,
    "Consumes all the target's senses in a cloud of blinding sights, fierce odors and tickling sensations.",
    ["The target suffers +1 to all target numbers for every success remaining after the Spell Resistance Test.",
     "Also deceives technological sensing devices."])
add("Chaotic World", "illusion", "SR2", 155, "P", "LOS", "S", drain(2, "S"), "Intelligence (R)", AREA,
    "An area-effect version of the Chaos spell.",
    ["Each target suffers +1 to all target numbers for every success remaining after its Spell Resistance Test.",
     "Also deceives technological sensing devices."])
add("Confusion", "illusion", "SR2", 155, "M", "LOS", "S", drain(0, "S"), W, AREA,
    "Fills the area with visual illusions: shifting forms, dazzling lights and pools of shadow.",
    ["Those who fail to resist suffer +1 to all target numbers for every 2 successes remaining after the Spell Resistance Test.",
     "Similar to Chaos, but does not affect technological systems."])
add("Entertainment", "illusion", "SR2", 156, "M", "LOS", "S", drain(1, "L"), "4", AREA,
    "Creates obvious but entertaining illusions for all who wish to watch.",
    ["Requires voluntary subjects.", "The number of successes measures how entertaining the audience finds the illusion."])
add("Improved Invisibility", "illusion", "SR2", 156, "P", "T", "S", drain(1, "M"), "4", ONE,
    "Like the Invisibility spell, except that it also affects technological sensing devices.",
    ["Double the number of successes to get the target number for an observer's Perception Test to notice the subject."])
add("Invisibility", "illusion", "SR2", 156, "M", "T", "S", drain(0, "M"), "4", ONE,
    "The subject becomes invisible to normal light.",
    ["Double the number of successes to get the target number for an observer's Perception Test. A successful test means the invisible person or thing has been noticed.",
     "Thermographic vision can still detect body heat, and the subject remains tangible and detectable by hearing, smell and so forth.",
     "Does not affect technological sensing systems. Cybereyes count as natural vision."])
add("Mask", "illusion", "SR2", 156, "M", "T", "S", drain(0, "L"), "4", ONE,
    "A voluntary subject assumes a physical appearance, of the same basic size and shape, chosen by the caster.",
    ["The number of successes becomes the target number for Perception Tests by observers.",
     "Does not work through technological devices."])
add("Stimulation", "illusion", "SR2", 156, "M", "LOS", "S", drain(1, "L"), "4", ONE,
    "The voluntary subject experiences a full sensory illusion of whatever type the spellcaster desires.",
    ["Successes measure the pleasure of the subject."])
add("Stink", "illusion", "SR2", 156, "M", "LOS", "S", drain(1, "S"), W, AREA,
    "An area spell that stimulates the sense of smell with a sickening stench.",
    ["Each success remaining after the Spell Resistance Test increases all of that victim's target numbers by +1."])

# ---------------------------------------------------------------- SR2: manipulation (pp.156-158)
add("Control Actions", "manipulation", "SR2", 156, "M", "LOS", "S", drain(2, "S"), W, ONE,
    "Like a puppeteer, the magician controls the physical actions of a target.",
    ["The victim's consciousness is not affected; it becomes a passenger in its own body.",
     "The victim uses any skills it possesses at the magician's orders, but with +4 to all target numbers.",
     "The Threshold is the target's Willpower Rating."])
add("Control Emotion", "manipulation", "SR2", 156, "M", "LOS", "S", drain(2, "M"), W, ONE,
    "The subject feels one overwhelming emotion, chosen by the magician when the spell is cast.",
    ["No penalty for actions in keeping with the emotion.",
     "Actions not relevant to the emotion take distraction modifiers (+2 or more to target numbers).",
     "Acting directly against the emotion needs a Willpower Test against the spell's Force. Distraction penalties apply even if it succeeds."])
add("Control Thoughts", "manipulation", "SR2", 157, "M", "Limited", "S", drain(2, "D"), W, ONE,
    "The magician controls the thoughts of the subject, who carries out orders wholeheartedly while the spell is sustained.",
    ["Orders that would be terribly destructive to the target or their loved ones allow a Willpower Test against the spell's Force to fight the spell.",
     "If the magician is not present, a single success resists the command. If present, the magician rolls Willpower against the target's Willpower and those successes reduce the target's; one net success still resists."])
add("Hibernate", "manipulation", "SR2", 157, "P", "T", "S", drain(0, "S"), "4", ONE,
    "Puts a voluntary or unconscious subject into a form of suspended animation.",
    ["Double the successes to get the factor by which bodily processes are slowed. With 4 successes the subject's metabolism slows by a factor of 8.",
     "A subject who has exceeded the Condition Monitor would then take an extra box of damage every 80 minutes instead of every 10."])
LEVITATE = ["The target can be moved a total distance in meters equal to the magician's Magic Rating times the successes, in any mix of horizontal and vertical movement measured from its starting point.",
            "The target number is +1 for every 100 kg of mass. A living being masses 50 kg per point of Body; a vehicle masses 1,000 kg.",
            "The object can be moved anywhere while the spell is maintained and it stays in view, up to the full distance within one Action Phase.",
            "If the item is attached to or held by a living being, that being makes a Strength Test against the spell's Force to reduce the caster's successes. At least 1 net success is needed."]
add("Levitate Item", "manipulation", "SR2", 157, "P", "LOS", "S", drain(1, "L"), "4", ONE,
    "Lifts an item from the ground and moves it around.", LEVITATE)
add("Levitate Person", "manipulation", "SR2", 157, "P", "LOS", "S", drain(1, "M"), "4", ONE,
    "Lifts a person from the ground and moves them around.", LEVITATE)
add("Magic Fingers", "manipulation", "SR2", 157, "P", "LOS", "S", drain(2, "M"), "6", ONE,
    "Classic telekinesis: the magician creates invisible hands and can hold or manipulate items by mental power.",
    ["The number of successes becomes the spell's Strength and Quickness ratings.",
     "The magician can use their own skills through the fingers, at +2 to all target numbers. Even simple actions may require a Quickness Test.",
     "The fingers can reach any point the magician can see. Clairvoyance or remote-viewing technology can give a close-up, as long as the actual location is within view."])
add("Poltergeist", "manipulation", "SR2", 157, "P", "LOS", "S", drain(1, "S"), "4 (R)", AREA,
    "Within the area, all small objects and debris up to a kilogram in mass whirl around in random patterns.",
    ["Reduces visibility in the area: +2 to all target numbers.",
     "Does Light Stun damage. Targets resist with Quickness rather than Body, against the spell's Force.",
     "Impact armor protects against this damage."], dmg="Light Stun")
add("Armor", "manipulation", "SR2", 158, "P", "Limited", "S", drain(2, "M"), "4", ONE,
    "Gives a voluntary subject built-in armor, knitting their tissues into tougher compounds.",
    ["Treat one-half the successes as a Dermal Armor Rating (added to Body) for as long as the spell is maintained."])
add("Barrier", "manipulation", "SR2", 158, "P", "Limited", "S", drain(2, "S"), "6", AREA,
    "Forms a force field of crackling energy, as a dome or as a wall.",
    ["A wall's height is the spell's Force in meters. The length of the wall or radius of the dome equals the magician's Magic Rating, adjustable like any area-effect radius.",
     "Anything larger than a molecule treats it as a physical barrier with a Barrier Rating equal to the spell's Force, cumulative with armor. Air and other gases pass through.",
     "Attacks directed through the barrier have a visibility modifier of -1.",
     "Does not impede spells, even manipulation spells."])
add("Mana Barrier", "manipulation", "SR2", 158, "M", "Limited", "S", drain(1, "S"), "6", AREA,
    "Forms a barrier that blocks living beings and magic but not unliving things.",
    ["Blocks movement by living beings. Unliving things such as bullets pass through, and passengers inside closed vehicles are not affected.",
     "Add one-half the spell's Force (the barrier's Rating) to the target numbers of all magicians casting spells across the barrier.",
     "It is also an astral barrier."])
add("Ignite", "manipulation", "SR2", 158, "P", "LOS", "P", drain(2, "D"), "4", ONE,
    "Accelerates molecular speed in a target until it catches fire. Anything that can burn is subject to this spell.",
    ["The base time to ignite the target is 10 turns, divided by the magician's successes.",
     "Needs more successes than the Body Rating of a living target or the base Barrier Rating of an inanimate one.",
     "A burning being takes (Force)M damage on the first turn, and the Power rises by 1 each Combat Turn. Make a Damage Resistance Test at the end of each turn, counting one-half impact armor.",
     "Ammo or explosives carried by the victim may go off. If not extinguished, the flames burn out in 1D6 Combat Turns."], dmg="(Force)M Physical")
DAMAGING = ["The Damage Code is (Force)M. Every 2 successes increase the damage by one level.",
            "Resisted with Body. One-half the value of impact armor reduces the Power of the attack.",
            "Resolve using the ranged combat procedure.",
            "Being real flame, it causes easily flammable materials to ignite and burn."]
add("Flame Bomb", "manipulation", "SR2", 158, "P", "LOS", "I", drain(1, "D"), "4", AREA,
    "An area-effect spell that creates a blast of real flame surrounding the target.", DAMAGING, dmg="(Force)M Physical")
add("Flamethrower", "manipulation", "SR2", 158, "P", "LOS", "I", drain(1, "S"), "4", ONE,
    "Creates a stream of real flame from the caster to the target.", DAMAGING, dmg="(Force)M Physical")
add("Ice Sheet", "manipulation", "SR2", 158, "P", "LOS", "I", drain(1, "S"), "4", "Magic × successes, in square meters",
    "Creates a flat sheet of ice covering a number of square meters equal to the caster's Magic Rating times the successes.",
    ["Characters crossing the sheet must make a Quickness Test against a Target Number 3 to avoid falling prone.",
     "Vehicles must make a Handling Test to avoid having to make a Crash Test.",
     "The sheet melts at a rate of 1 square meter per minute."])
add("Light", "manipulation", "SR2", 158, "P", "LOS", "S", drain(2, "M"), "4", AREA,
    "Creates a mobile point of light that illuminates an area equal to the magician's Magic Rating times the successes, in meters.",
    ["Roughly as bright as a good flashlight, but over an area.",
     "Cannot be used to blind, but offsets visibility modifiers for darkness: 2 successes counter a +1 modifier."])
add("Shadow", "manipulation", "SR2", 158, "P", "LOS", "S", drain(2, "M"), "2 to 6, by lighting", AREA,
    "Creates a pool of darkness equal to one-half the caster's Magic Rating times the successes, in meters.",
    ["Target number depends on local conditions: bright midday 6; day 5; overcast day 4; twilight 3; street light or darker 2.",
     "Every 2 successes impose a +1 target modifier on Combat or Perception Tests against targets within the shadow."])
add("Spark", "manipulation", "SR2", 158, "P", "LOS", "I", drain(1, "M"), "4", ONE,
    "Creates a small spark of electricity that springs from the spellcaster to the target.",
    DAMAGING[:3], dmg="(Force)M Physical")

# ---------------------------------------------------------------- GRIM: combat (pp.126-127)
FIRE = "Uses the elemental effect of fire."
add("Death Touch", "combat", "GRIM", 126, "M", "T", "I", drain(-1, "S"), W, ONE,
    "A particularly lethal combat spell that causes Physical damage to a single target the magician touches.",
    dmg="Deadly Physical")
add("Fire Bolt", "combat", "GRIM", 126, "P", "LOS", "I", drain(1, "D"), B, ONE,
    "A powerful bolt of energy that causes Physical damage to a single target.", [FIRE], dmg="Serious Physical")
add("Fire Cloud", "combat", "GRIM", 126, "P", "LOS", "I", drain(1, "D"), B, AREA,
    "An area-effect cloud of magical energy that causes Physical damage.", [FIRE], dmg="Moderate Physical")
add("Fire Dart", "combat", "GRIM", 126, "P", "LOS", "I", drain(1, "M"), B, ONE,
    "An energy dart that causes Physical damage to a single target.", [FIRE], dmg="Light Physical")
add("Fire Missile", "combat", "GRIM", 126, "P", "LOS", "I", drain(1, "S"), B, ONE,
    "A bolt of magical energy that causes Physical damage to a single target.", [FIRE], dmg="Moderate Physical")
add("Mana Cloud", "combat", "GRIM", 126, "M", "LOS", "I", drain(0, "S"), W, AREA,
    "An area-effect spell that raises a cloud of magical energy that does Physical damage.", dmg="Moderate Physical")
add("Manablast", "combat", "GRIM", 126, "M", "LOS", "I", drain(0, "D"), W, AREA,
    "A powerful area-effect blast of magical energy that causes Physical damage.",
    ["Uses the elemental effect of blast."], dmg="Moderate Physical")
add("Powerblast", "combat", "GRIM", 127, "P", "LOS", "I", drain(1, "D"), B, AREA,
    "A powerful area-effect blast of magical energy that causes Physical damage.",
    ["Uses the elemental effect of blast."], dmg="Moderate Physical")
add("Ram Touch", "combat", "GRIM", 127, "P", "T", "I", drain(-1, "M"), ORT, ONE,
    "Damages inanimate objects. Works like the Ram spell (SR2 p.151), except that the magician must touch the target.",
    dmg="Serious")
add("Slay (Race/Species)", "combat", "GRIM", 127, "M", "LOS", "I", drain(-1, "S"), W, ONE,
    "Causes Physical damage to a target of one specific race or species.",
    ["Each version has a different, specific formula: slay ork, slay dog, slay western dragon and so forth are all separate spells."],
    dmg="Serious Physical")
add("Spirit Bolt", "combat", "GRIM", 127, "M", "LOS", "I", drain(-1, "S"), "Force (R)", ONE,
    "A bolt of magical energy that causes Physical damage to a single spirit.",
    ["Restricted target: spirits only."], dmg="Serious Physical")
add("Sterilize", "combat", "GRIM", 127, "P", "LOS", "I", drain(1, "D"), "4", AREA,
    "An area-effect spell that kills small life forms such as bacteria and other microorganisms.",
    ["Only 1 success is required.",
     "Also destroys or renders unusable biomaterial such as skin flakes, stray hairs and spilled blood. Affected material cannot be used as a material link for ritual magic.",
     "Does not affect biomaterial attached to a living being, so it does not kill microorganisms living inside a creature.",
     "Does not affect organisms classified as bioweapons."], dmg="Deadly")
add("Stun Bolt", "combat", "GRIM", 127, "M", "LOS", "I", drain(-1, "D"), W, ONE,
    "A bolt of magical energy that causes Stun damage to a single target.", dmg="Serious Stun")
add("Stun Cloud", "combat", "GRIM", 127, "M", "LOS", "I", drain(-1, "S"), W, AREA,
    "An area-effect spell that instantly produces a cloud of magical energy that causes Stun damage.", dmg="Moderate Stun")
add("Stun Missile", "combat", "GRIM", 127, "M", "LOS", "I", drain(-1, "M"), W, ONE,
    "A missile of magical energy that causes Stun damage to a single target.", dmg="Moderate Stun")
add("Stun Touch", "combat", "GRIM", 127, "M", "T", "I", drain(-2, "M"), W, ONE,
    "A hands-on spell that causes Stun damage to a single target.", dmg="Serious Stun")
add("Stunball", "combat", "GRIM", 127, "M", "LOS", "I", drain(-1, "D"), W, AREA,
    "An area-effect spell that causes Stun damage.", dmg="Serious Stun")
add("Stunblast", "combat", "GRIM", 127, "M", "LOS", "I", drain(1, "D"), W, AREA,
    "An area-effect spell that causes Stun damage.", ["Uses the elemental effect of blast."], dmg="Serious Stun")
add("Urban Renewal", "combat", "GRIM", 127, "P", "LOS", "I", drain(0, "D"), ORT, AREA,
    "An area-effect spell that works like Ram (SR2 p.151) but affects only parts of buildings.",
    ["Restricted target: buildings.",
     "The gamemaster checks the actual effect only against significant objects within the area and uses discretion for the rest."],
    dmg="Serious")
add("Wrecker", "combat", "GRIM", 127, "P", "LOS", "I", drain(0, "S"), ORT, ONE,
    "Works like Ram (SR2 p.151) but affects only a single vehicle.", ["Restricted target: vehicles."], dmg="Serious")

# ---------------------------------------------------------------- GRIM: detection (p.128)
BG = "The background count of an area affects ranged detection spells cast within it."
add("Analyze Magic", "detection", "GRIM", 128, "M", "Limited", "S", drain(0, "M"), "Force or Rating of the magic", ONE,
    "Allows the magician to analyze a magic item as if assensing it.",
    ["The target number is the Force Rating of the spell, focus or other magical phenomenon being analyzed.",
     "Consult the Astral Examination table (SR2 p.146) for the information acquired.", BG])
add("Clairaudience (Extended)", "detection", "GRIM", 128, "M", "Extended", "S", drain(-1, "S"), "4", ONE,
    "Works like the Clairaudience spell (SR2 p.153), with the Extended Range option.", [BG])
add("Clairvoyance (Extended)", "detection", "GRIM", 128, "M", "Extended", "S", drain(-1, "S"), "4", ONE,
    "Works like the Clairvoyance spell (SR2 p.153), with the Extended Range option.", [BG])
add("Detect Enemies (Extended)", "detection", "GRIM", 128, "M", "Extended", "S", drain(0, "S"), "4", AREA,
    "Works like the Detect Enemies spell (SR2 p.153), with the Extended Range option.", [BG])
add("Detect Magic", "detection", "GRIM", 128, "M", "Limited", "S", drain(0, "L"), "4", AREA,
    "Detects the presence of active magic within range: foci, sustained, quickened or anchored spells, and spirits.",
    ["An area-effect, general hypersense spell requiring a voluntary subject.",
     "Does not detect magically active characters.", BG])
add("Mindlink (Individual)", "detection", "GRIM", 128, "M", "Limited", "S", drain(2, "M"), "4", ONE,
    "Lets the magician communicate mentally with one specific person, exchanging conversation, emotions and mental images.",
    ["A hypersense spell requiring a voluntary subject. The person is chosen when the spell is designed.",
     "1 success establishes the link. The subject must be within line of sight and range at casting, and may then move out of sight but must stay within range.",
     "A subject who does not wish to communicate may resist with Willpower against the spell's Force, reducing the caster's successes.",
     "If the link fails, the magician must recast the spell and resist Drain again."])

# ---------------------------------------------------------------- GRIM: health (p.129)
for n, lv in zip((1, 2, 3, 4), "LMSD"):
    add(f"Decrease -{n} Cybered Attribute", "health", "GRIM", 129, "P", "T", "S", drain(3, lv), "10 − target's Essence (R)", ONE,
        f"Reduces one of the target's cybernetically modified Attributes by {n}.",
        ["Works like the Decrease Attribute spell (SR2 p.154), except that it affects cybered Attributes.",
         "The version that affects cybered Reaction has Drain one level higher."])
for n, mod, lv in ((1, 1, "S"), (2, 1, "D"), (3, 3, "D")):
    add(f"Decrease Reflexes -{n} Initiative Di{'e' if n == 1 else 'ce'}", "health", "GRIM", 129, "M", "LOS", "S",
        drain(mod, lv), "2 × target's Reaction", ONE,
        f"Reduces the number of Initiative dice available to the target by {n}.",
        ["Does not affect characters with cybernetic Initiative enhancements.",
         "A character left with no Initiative dice, or a negative number, uses Reaction as Initiative."])
add("Healthy Glow", "health", "GRIM", 129, "P", "T", "P", drain(0, "L"), "4", ONE,
    "A cosmetic spell that brightens eyes and hair, sloughs off dead skin cells, improves circulation and promotes general well-being.",
    ["Needs no sustaining, but wears off in time depending on the subject's lifestyle, diet, vices and so on."], turns=5)
add("Oxygenate", "health", "GRIM", 129, "P", "Limited", "S", drain(2, "M"), "4", ONE,
    "Oxygenates a voluntary subject's blood.",
    ["The subject gains 1 extra Body die for every 2 successes to resist suffocation, strangulation, inhaled gas or any other effect of oxygen deprivation.",
     "Also allows the subject to breathe water."])
add("Preserve", "health", "GRIM", 129, "P", "Limited", "S", drain(1, "M"), ORT, ONE,
    "Prevents dead organic matter from drying out, decaying or putrefying.",
    ["A single success is required.",
     "Can be used on food, but is most often used to protect cadavers before autopsy or to preserve organic samples for later use as a material link.",
     "Often applied with a spell lock."])
for lv in "LMSD":
    add(f"Prophylaxis ({lv}) Pathogen", "health", "GRIM", 129, "P", "Limited", "S", drain(2, lv), "4", ONE,
        f"Gives a voluntary subject extra resistance to infection, drugs or toxins of {LEVELS[lv]} Damage Level.",
        ["The subject gains 1 extra Body die for every 2 successes to resist infection, drugs or toxins.",
         "The subject also resists beneficial medicines."])
for name, lv, turns in (("Light", "M", 5), ("Moderate", "S", 10), ("Serious", "D", 15)):
    add(f"Resist Pain ({name})", "health", "GRIM", 129, "M", "Limited", "P", drain(0, lv), "4", ONE,
        f"Offsets the injury modifiers a character suffers at the {name} Condition Level.",
        ["Offsets the target number and Initiative penalties of Physical damage only, not Stun. It does not heal or treat the damage.",
         "A different spell is needed for each of the Light, Moderate and Serious Condition Levels. A Deadly injury cannot be countered.",
         "The relief does not wear off, but the spell dissipates if the subject's damage rises above this level or the wounds heal."],
        turns=turns)
add("Stabilize", "health", "GRIM", 129, "P", "LOS", "P", drain(0, "S"), "4 + minutes since the injury", ONE,
    "Applied to a character with Deadly Physical damage, stabilizes their condition so that they do not die.",
    ["Add the number of minutes elapsed since the character took the damage to the target number."], turns=20)

# ---------------------------------------------------------------- GRIM: illusion (p.130)
add("Overstimulation", "illusion", "GRIM", 130, "M", "LOS", "S", drain(1, "M"), W, ONE,
    "Stimulates the sensory centers of the target's brain.",
    ["While the spell lasts, the subject suffers penalties to all actions as if a number of boxes equal to the caster's successes were filled in on the Stun Condition Monitor. This is not actual damage.",
     "With 10 or more successes, the victim is conscious but incapable of action."])
add("Physical Mask", "illusion", "GRIM", 130, "P", "LOS", "S", drain(1, "L"), "4", ONE,
    "Like the Mask spell (SR2 p.156), but this version works against technological devices.")
add("Spectacle", "illusion", "GRIM", 130, "M", "LOS", "S", drain(1, "M"), "4", AREA,
    "A multi-sensory version of the Entertainment spell (SR2 p.156).")
add("Trid Entertainment", "illusion", "GRIM", 130, "P", "LOS", "S", drain(2, "L"), "4", AREA,
    "Like the Entertainment spell (SR2 p.156), but this version can be seen by electronic cameras.")
add("Trid Spectacle", "illusion", "GRIM", 130, "P", "LOS", "S", drain(2, "M"), "4", AREA,
    "A version of the Spectacle spell that can be seen by electronic cameras.")
add("Vehicle Mask", "illusion", "GRIM", 130, "P", "T", "S", drain(0, "L"), "6", ONE,
    "Works like the Physical Mask spell, specifically affecting vehicles.",
    ["The caster must touch the vehicle.",
     "Only affects vehicles with a Body Rating equal to or less than one-half the magician's Magic Rating (round down)."])

# ---------------------------------------------------------------- GRIM: manipulation (pp.130-132)
add("Control Animal", "manipulation", "GRIM", 130, "M", "LOS", "S", drain(2, "D"), W, ONE,
    "Like the Control Thoughts spell (SR2 p.157), but works only on non-sentient animals.",
    ["Sentience is determined at the gamemaster's discretion.",
     "Paranormal animals resist with Willpower or Essence, whichever is higher."])
add("Influence", "manipulation", "GRIM", 130, "M", "Limited", "P", drain(2, "S"), W, ONE,
    "Permanently implants a single suggestion in the victim's mind.",
    ["The victim acts on the suggestion or carries out the order as if it were their own idea.",
     "Proving the falseness of the idea to the victim, or forcing the caster to withdraw it, overcomes the spell."], turns=10)
add("Mob Mind", "manipulation", "GRIM", 130, "M", "Limited", "S", drain(3, "S"), W, AREA,
    "An area-effect spell that allows the caster to control the thoughts of all within its range.",
    ["Treat the crowd as a single character for the Success Test. Pedestrians are assumed to have a Willpower of 3.",
     "Major characters defend individually against the successes of the caster's single test."])
add("Mob Mood", "manipulation", "GRIM", 130, "M", "Limited", "S", drain(2, "M"), W, AREA,
    "Like Mob Mind, but affects only the crowd's emotions.",
    ["Does not give the caster control of the crowd; it shifts the crowd's mood."])
add("Animate", "manipulation", "GRIM", 130, "P", "Limited", "S", drain(2, "M"), ORT, ONE,
    "Makes an inanimate object move according to its structure: balls roll, rugs crawl, humanoid statues walk.",
    ["Gives solid things enough flexibility to move as if they had joints.",
     "The caster can move only the whole object, not one part of it such as computer keys or vehicle weapons.",
     "The object moves a number of meters per action equal to one-half the caster's Magic Rating (round down)."])
add("Clout", "manipulation", "GRIM", 131, "P", "LOS", "I", drain(0, "M"), "4", ONE,
    "A telekinetic punch.",
    ["Damage Code is (caster's Willpower)M Stun.",
     "Normal Ranged Combat modifiers apply, and successes may be used to increase the damage as in ranged combat.",
     "Impact armor defends against this spell."], dmg="(Willpower)M Stun")
add("Use (Skill)", "manipulation", "GRIM", 131, "P", "LOS", "S", drain(3, "L"), "6", ONE,
    "A limited form of the Magic Fingers spell (SR2 p.157) that allows the caster to use one skill telekinetically.",
    ["The gamemaster determines which skills may be used. Knowledge skills, which need no physical action, are not appropriate.",
     "Works like Magic Fingers, except that the caster's actual Skill Rating determines the effect."])
ACID = "Uses the elemental effect rules (acid)."
add("Acid", "manipulation", "GRIM", 131, "P", "LOS", "I", drain(1, "S"), B, ONE,
    "Strikes the target with a spray of acid.", [ACID], dmg="Moderate")
add("Acid Bomb", "manipulation", "GRIM", 131, "P", "LOS", "I", drain(1, "D"), B, AREA,
    "An area-effect spell that strikes targets with a spray of acid.", [ACID], dmg="Moderate")
add("Acid Stream", "manipulation", "GRIM", 131, "P", "LOS", "I", drain(1, "D"), B, ONE,
    "Strikes the target with a stream of acid.", [ACID], dmg="Serious")
add("Astral Static", "manipulation", "GRIM", 131, "M", "Limited", "S", drain(1, "D"), "6", AREA,
    "An area-effect spell that creates a cloud of crackling, swirling mana in astral space.",
    ["Generates a background count of 1 for every 2 successes.",
     "The static's rating increases the target numbers of all Astral Success Tests within the area, including the caster's."])
add("Bind", "manipulation", "GRIM", 131, "P", "LOS", "S", drain(2, "S"), "Quickness (R)", ONE,
    "Entraps and holds the target in bands of mystical energy.",
    ["The target resists with a Quickness Test against the spell's Force. Net successes in the caster's favor are the Barrier Rating of the bands.",
     "To break free, compare the target's Strength to the Barrier Rating using the barrier rules (SR2 p.98). A Strength Test against the spell's Force adds 1 to effective Strength for every 2 successes.",
     "On breaking free, the target must resist (Strength)L Stun damage from the effort."])
PERSONAL = "The personal form of this spell has a Drain Code of [(F/2)+2]L."
add("Blade Barrier", "manipulation", "GRIM", 131, "P", "LOS", "S", drain(2, "M"), "6", AREA,
    "Like the Barrier spell (SR2 p.158), but provides protection against bladed weapons.",
    ["The Barrier Rating equals the spell's Force. Impact armor may be added to it.", PERSONAL])
add("Blast Barrier", "manipulation", "GRIM", 131, "P", "LOS", "S", drain(2, "M"), "6", AREA,
    "Like the Barrier spell (SR2 p.158), but provides protection against blast from grenades and similar weapons.",
    ["The Barrier Rating equals the spell's Force. Impact armor may be added to it.", PERSONAL])
add("Bullet Barrier", "manipulation", "GRIM", 131, "P", "LOS", "S", drain(2, "M"), "6", AREA,
    "Like the Barrier spell (SR2 p.158), but provides protection against bullets and other ballistic weapons.",
    ["The Barrier Rating equals the spell's Force. Ballistic armor may be added to it.", PERSONAL])
add("(Critter) Form", "manipulation", "GRIM", 131, "P", "Limited", "S", drain(2, "M"), "Willpower", ONE,
    "Like the Shapechange spell, but changes a voluntary subject into one specific, non-paranormal animal.")
add("Fashion", "manipulation", "GRIM", 131, "P", "LOS", "P", drain(2, "M"), "4", ONE,
    "Instantly tailors clothing, transforming a voluntary subject's garments into any fashion the caster wishes.",
    ["Extra successes measure the degree of style in the tailoring.",
     "Cannot change the clothing's protective value, only its cut, color and fit."], turns=10)
add("Fire Strike", "manipulation", "GRIM", 132, "P", "LOS", "I", drain(3, "D"), B, AREA,
    "An area-effect spell that blasts flame into an area.", [FIRE], dmg="Serious")
add("Flame Burst", "manipulation", "GRIM", 132, "P", "LOS", "I", drain(1, "D"), B, ONE,
    "Strikes the target with a burst of flame.", [FIRE], dmg="Serious")
add("Lock", "manipulation", "GRIM", 132, "P", "LOS", "S", drain(2, "M"), ORT, ONE,
    "Holds a door, portal or other closure magically closed for as long as the caster sustains the spell.",
    ["The lock is as strong as the material of the door, so opening it means breaking or blasting through."])
add("Makeover", "manipulation", "GRIM", 132, "P", "LOS", "P", drain(2, "M"), "4", ONE,
    "Gives a voluntary subject a complete makeover: cosmetics, hair, clothes and so on.",
    ["The changes are as permanent as those made in a real beauty salon.",
     "The number of successes measures the degree of style.",
     "Nothing actually changes; the subject is only cleaned and spruced up."], turns=10)
add("Seal", "manipulation", "GRIM", 132, "P", "LOS", "S", drain(2, "S"), ORT, ONE,
    "Like the Lock spell, but reinforces a locked doorway.",
    ["Every 2 successes increase the door's Barrier Rating by 1."])
add("Shapechange", "manipulation", "GRIM", 132, "P", "Limited", "S", drain(2, "S"), "Willpower", ONE,
    "Transforms a voluntary subject into a normal critter, though the subject retains human consciousness.",
    ["Use the critter's Physical Attributes (Critter Statistics Table, SR2 p.233), adding 1 to its base ratings for every 2 successes.",
     "Increase the critter's Reaction by the subject's Intelligence. Mental Attributes remain the subject's own.",
     "Does not transform clothing or equipment.",
     "Magicians under this spell can cast spells, but cannot fulfil geasa or use Centering Skills that need actions the animal shape cannot perform, such as speech."])
add("Spell Barrier", "manipulation", "GRIM", 132, "M", "LOS", "S", drain(1, "M"), "6", AREA,
    "Like the Mana Barrier spell (SR2 p.158), but provides protection against spells.", [PERSONAL])
add("Thunderclap", "manipulation", "GRIM", 132, "P", "LOS", "I", drain(0, "S"), B, ONE,
    "Strikes the target with an explosion of air, making a thunderous noise.",
    ["Causes Stun damage.", "Deafens the target for 1 Combat Turn for every 2 successes."], dmg="Moderate Stun")
add("Transform", "manipulation", "GRIM", 132, "P", "Limited", "S", drain(2, "S"), "Willpower", ONE,
    "Changes the subject into a normal critter.",
    ["The transformed being has no awareness of its former state and has only animal intelligence.",
     "Does not transform clothing or equipment."])

# ---------------------------------------------------------------- AWK (pp.130-141)
add("Corps Cadavre", "manipulation", "AWK", 130, "P", "T", "P", drain(2, "S"), "6", ONE,
    "Cast on a specially prepared corpse, animates it as a corps cadavre.",
    ["The corpse must first be prepared with the Enchanting Skill (base time 10 days, Target Number 4).",
     "The caster can issue simple spoken commands to the creature to carry out basic tasks.",
     "The corps cadavre obeys its creator until it rots away, within a month or two."], turns=20)
add("Redirect", "combat", "AWK", 133, "P", "LOS", "I", "(F/2)(Attack − 1)", "4", ONE,
    "Sends the energy of an incoming physical or melee attack back against the attacker as a powerful mental shock.",
    ["The magician must have a higher Initiative than the attacker and must delay their action.",
     "If the magician's successes exceed the attacker's Attack Test successes, the attack is avoided and the attacker suffers Stun damage with the Damage Code of the original attack.",
     "On a tie the spell has no effect and the magician takes the damage of the original attack.",
     "The attacker may resist the Stun damage with Willpower. Armor has no effect.",
     "Drain is half the spell's Force, at a Damage Level one less than that of the original attack.",
     "May be anchored to places or objects."], dmg="Stun, at the Damage Code of the original attack")
add("Rot", "combat", "AWK", 134, "P", "LOS", "I", drain(1, "M"), ORT, ONE,
    "Causes inanimate organic matter such as leather, wood, meat and paper to decay rapidly and disintegrate.",
    ["Effective against loa zombies, which are animated corpses: base Damage Level Serious, target number the zombie's Body modified by any armor or magic.",
     "Does not affect ghouls, vampires, banshees and similar altered living creatures, zombies created by zombie dust, or corps cadavres."],
    dmg="Serious")
add("Shattershield", "combat", "AWK", 134, "M", "LOS", "I", drain(0, "S"), "Force (R)", ONE,
    "Designed to break through magical barriers such as wards, striking the barrier with a single attack.",
    ["A successful attack reduces the Barrier or Ward Rating by 1, plus 1 more for every 2 successes beyond the first.",
     "Against astral barriers such as wards or mana barriers, the caster must be astrally active and able to assense the barrier."],
    dmg="Deadly")
add("Animal Spy", "detection", "AWK", 134, "M", "Limited", "S", drain(0, "L"), "4", ONE,
    "The magician perceives the surroundings using the senses of any non-paranormal animal.",
    ["The animal must be within a radius of Spell Test successes × Magic × 5 meters.",
     "The caster has no control over the animal and cannot target spells through its eyesight.",
     "While sustaining the spell, the caster can switch to another animal in range with a Simple Action.",
     "If the gamemaster believes the animal would resist, it makes a Willpower Test against the spell's Force; success means the spell does not affect it."])
add("Astral Sense", "detection", "AWK", 134, "M", "Limited", "S", drain(0, "M"), "10", "Within range",
    "The caster senses the presence of astrally active forms within Magic × 5 meters, even while not astrally active.",
    ["The caster senses astrally active forms of a Force or Magic rating up to the number of successes.",
     "Cannot tell spirits, spells and other astrally active forms such as foci and wards apart."])
add("Catalogue", "detection", "AWK", 134, "P", "LOS", "I", drain(-1, "L"), "4", AREA,
    "An area-effect spell that lets the caster compile a comprehensive, itemized list of all the non-living items within line of sight.",
    ["The caster writes or dictates the list in a manner similar to automatic writing. Items the magician would not recognize on sight are listed as unknown.",
     "Cannot catalogue what the caster cannot see: a warehouse full of boxes lists the boxes, not their contents.",
     "The caster forgets the exact items and quantities as soon as the list is produced."])
add("Diagnose", "detection", "AWK", 134, "M", "Limited", "I", drain(-1, "M"), "10 − subject's Essence", ONE,
    "Gives the caster information on any illnesses, injuries or other medical problems the subject suffers from.",
    ["1 success: whether the subject is healthy or ill, and a general idea of their Essence.",
     "3 successes: specific illnesses or injuries.",
     "5 successes: even difficult-to-detect viruses (such as HMHVV) and internal injuries.",
     "Cannot tell whether low Essence is due to deadly wounds or cyberware."])
add("Enhance Aim", "detection", "AWK", 134, "M", "Limited", "S", drain(0, "S"), "6", ONE,
    "Reduces a fellow character's ranged attack target modifiers by 2.",
    ["Not cumulative with smartgun links, smartgoggles or laser sights, but does enhance non-electronic rangefinders and scopes.",
     "Cast on the magician themself, the penalty for sustaining the spell cancels the benefit unless something else sustains it."])
add("Foretelling", "detection", "AWK", 135, "M", "Self", "I", drain(0, "M"), "10", "Self",
    "Gives the caster a brief insight into the probabilities surrounding a future event.",
    ["On a success the magician receives a brief vision of the circumstances surrounding a specific event, or the answer to a single yes-or-no question about a future event.",
     "The truth and degree of information provided are at the gamemaster's discretion."])
add("Night Vision", "detection", "AWK", 135, "P", "T", "S", drain(0, "L"), "6", ONE,
    "Grants the target the low-light vision modifiers on the Visibility Table (SR2 p.89).")
add("Translate", "detection", "AWK", 135, "M", "Limited", "S", drain(1, "L"), "4", ONE,
    "Sets up a low-level telepathic connection between two willing subjects, who can converse as if both spoke the same language.",
    ["Translates a speaker's intent more accurately than the exact phrasing.",
     "The number of successes indicates the quality of the translation."])
add("X-Ray Vision", "detection", "AWK", 135, "P", "Limited", "S", drain(2, "S"), "4", ONE,
    "Enables a willing subject to see through inanimate barriers.",
    ["For each success the subject can see through 1 Barrier Rating point of non-living material. Doing so takes a Simple Action.",
     "The line of sight provided fulfils the LOS requirement for casting other spells.",
     "Does not see through living or magical barriers and does not work in astral space."])
SEVERITY = (("Nuisance", "L"), ("Mild", "M"), ("Moderate", "S"), ("Severe", "D"))
for name, lv in SEVERITY:
    add(f"Alleviate {name} Allergy", "health", "AWK", 135, "P", "LOS", "S", drain(0, lv), "6", ONE,
        f"Reduces the effects of a {name} allergy suffered by the target.",
        ["Does not aid against vulnerabilities: it would protect a vampire from sunlight, but not from a wooden weapon."])
add("Awaken", "health", "AWK", 135, "M", "T", "I", drain(-1, "L"), "10 − subject's Essence", ONE,
    "The target wakes up and is immediately aware of their surroundings.",
    ["Can also revive an unconscious subject, who stays conscious for only one minute per success before lapsing back into unconsciousness."])
add("Blindness", "health", "AWK", 135, "M", "LOS", "S", drain(1, "D"), B, ONE,
    "Magically renders a subject blind for the duration of the spell.",
    ["Affects the brain's ability to receive visual information, so it affects subjects with cybereyes as well."])
for name, lv in SEVERITY:
    add(f"Cause {name} Allergy", "health", "AWK", 135, "M", "LOS", "S", drain(1, lv), "10 − subject's Essence", ONE,
        f"Inflicts on the subject a {name} allergic reaction of the caster's choice, subject to gamemaster approval.",
        ["The allergy must be triggered by a specific material. The subject suffers its standard effects.",
         "Severe allergies to some substances, such as sunlight or iron, may be fatal if sustained long enough.",
         "The Alleviate Allergy spell cancels the effects of this spell."])
add("Cripple Limb", "health", "AWK", 136, "M", "T", "S", drain(0, "S"), B, ONE,
    "Incapacitates any organic limb the caster touches. The limb is useless for the duration of the spell.")
add("Fast", "health", "AWK", 136, "M", "T", "P", drain(0, "L"), "Subject's Body", ONE,
    "Lets a voluntary subject ignore feelings of hunger or thirst for 48 hours from the casting.",
    ["Removes only the desire for food and water, not the subject's need for nourishment or hydration."], turns=10)
add("Intoxication", "health", "AWK", 136, "M", "LOS", "S", drain(2, "M"), B, ONE,
    "Causes a subject to feel the effects of inebriation.",
    ["The subject suffers penalties to all actions as if a number of boxes equal to the caster's successes were filled in on the Stun Condition Monitor. This is not actual damage.",
     "With 10 or more successes the subject remains conscious but becomes incapable of action.",
     "Magician targets may use Antidote or Detox spells to resist. Blood filters do not help, because there are no toxins in the blood."])
add("Nutrition", "health", "AWK", 136, "M", "T", "P", drain(0, "L"), "4", ONE,
    "Provides a voluntary target with a full day's nourishment and hydration.",
    ["Does not satisfy feelings of hunger or thirst."], turns=15)
add("Paralyze", "health", "AWK", 136, "M", "Limited", "S", drain(1, "D"), W, ONE,
    "Overrides all of a subject's voluntary muscles, leaving them unable to move or speak while the spell is sustained.",
    ["Each round the subject may make a Willpower Test against the spell's Force. If any of those tests yields more successes than the caster's Spell Test, the spell is broken.",
     "Cyberware that works independently of the body's functions, such as a datajack, dermal plating or tactical computer, may continue to work."])
add("Agonizing Pain", "illusion", "AWK", 136, "M", "LOS", "S", drain(1, "M"), W, ONE,
    "Inflicts crippling pain on a target.",
    ["The target suffers temporary Stun damage of 1 box for each success, and its target modifiers apply to all the target's tests. It is not real damage and needs no recovery.",
     "With 10 or more successes the pain incapacitates the subject, leaving them unable to move or act.",
     "A successful Willpower Test against a target number equal to the caster's successes lets the target ignore the spell and perform 1 action."])
add("Chaff", "illusion", "AWK", 136, "P", "LOS", "S", drain(-1, "S"), ORT, ONE,
    "A variation of the Chaotic World spell (SR2 p.155) that interferes with non-living sensing devices.",
    ["Adds 1 to the target numbers for use of all non-living sensing devices, including weapon targeting systems such as the smartgun link."])
add("Crowd Scene", "illusion", "AWK", 136, "P", "LOS", "S", drain(2, "M"), "4", AREA,
    "Creates an area-effect illusion of a fairly homogeneous crowd of people milling about, typical for the place.",
    ["The image is not solid and makes no sound. Anyone physically interacting with the crowd knows at once that it is an illusion.",
     "Otherwise a character can make a Resistance Test against a target number of twice the caster's successes to recognize the illusion.",
     "Being physical, the image registers on cameras and other sensing devices."])
add("Disregard", "illusion", "AWK", 137, "M", "T", "S", drain(0, "M"), "4", ONE,
    "Places a voluntary subject outside the perceptions of other individuals, who simply fail to notice them.",
    ["The subject remains visible and detectable by mechanical means.",
     "A character may defeat the spell with an Intelligence Test against a target number of twice the caster's successes."])
add("Dream", "illusion", "AWK", 137, "M", "LOS", "S", drain(0, "L"), W, ONE,
    "Transmits a dream image to a sleeping subject.",
    ["Dream images cannot cause actual harm, but may entertain, relax or frighten. Subjects vividly remember them when awakened.",
     "Subjects experiencing nightmares get no rest and do not recover Mental or Stun damage while the nightmares persist.",
     "A subject may discern that the dream is magical with an Intelligence Test against a target number of twice the caster's successes."])
add("Flare", "illusion", "AWK", 137, "P", "LOS", "I", drain(1, "M"), "Quickness (R)", ONE,
    "Creates a bright flash of light that temporarily blinds a target.",
    ["The target makes an opposed Quickness Test against the spell's Force. Flare compensation, as an adept power or as cyberware, reduces that target number by 4 (minimum 2).",
     "Each net success blinds the target for 1 Combat Turn.",
     "A physical illusion, so cameras and cybereyes can be affected."])
add("Silence", "illusion", "AWK", 137, "P", "LOS", "S", drain(2, "S"), "6", AREA,
    "An area-effect spell that creates a sound-deadening field.",
    ["All sounds created within the area are deadened, and no sound can pass into or through it.",
     "Being physical, it also stops recording devices picking up the sounds. Sonic attacks and sound-based critter powers fail within the area.",
     "A caster standing inside the area suffers its effects too.",
     "The personal version affects only a single subject and has a Drain Code of [(F/2)+2]M."])
add("Calm Animal", "manipulation", "AWK", 137, "M", "LOS", "S", drain(2, "L"), W, ONE,
    "Causes a subject of animal-level intelligence to become calm and passive.",
    ["Subjects engaged in combat reduce their target number to resist the spell by 2.",
     "A calmed animal attacks only to protect itself.",
     "The area-effect version has limited range and a Drain Code of [(F/2)+2]M."])
add("Compel Truth", "manipulation", "AWK", 137, "M", "LOS", "S", drain(2, "L"), W, ONE,
    "Forces a target to speak the truth as they know it.",
    ["Whatever the target believes to be true counts as the truth.",
     "The target may choose not to speak or may withhold information, but cannot deliberately lie."])
add("False Memory", "manipulation", "AWK", 138, "M", "Limited", "P", drain(2, "S"), W, ONE,
    "Creates and implants a false memory in the mind of a target, or modifies an existing one.",
    ["The subject cannot tell a successfully implanted memory from a real one.",
     "The gamemaster secretly makes a Spell Resistance Test for the subject each time the false memory is recalled and tallies the successes. When the tally exceeds the caster's successes, the spell ends and the real memories return."],
    turns=20)
add("Possession", "manipulation", "AWK", 138, "M", "LOS", "S", drain(3, "S"), W, ONE,
    "The magician enters a target's body with their own consciousness and controls it.",
    ["The caster falls into a trance while their consciousness controls the target's body.",
     "The caster may use the subject's physical skills at +2, uses their own mental skills, and cannot use magic skills.",
     "Damage to either body affects the caster's target numbers while in the subject's body.",
     "If the subject dies during the spell, the caster must resist 8D Stun damage or die. If the caster's own body dies, the caster dies and the spell is broken.",
     "Subjects have no memory of the time the spell was in effect."])
add("Terrorize", "manipulation", "AWK", 138, "M", "LOS", "S", drain(2, "S"), W, ONE,
    "Fills a single target with fear of the spellcaster.",
    ["A target who fails to resist must flee from the caster as quickly as possible.",
     "Once out of sight of the caster, the subject may make a Willpower Test each round to overcome the spell."])
add("Catfall", "manipulation", "AWK", 138, "P", "LOS", "S", drain(2, "L"), "4", ONE,
    "Psychokinetically slows a target's fall and ensures that the subject lands upright.",
    ["The subject may fall successes × the magician's Magic Rating in meters without danger of injury.",
     "For a longer fall, subtract that distance from the distance fallen before calculating damage."])
add("Deflect", "manipulation", "AWK", 138, "P", "T", "S", drain(1, "S"), "6", ONE,
    "Psychokinetically deflects physical missile attacks against a target.",
    ["Every 2 successes give the target 1 additional Combat Pool die, usable only for Damage Resistance Tests against physical ranged attacks.",
     "Does not protect against energy attacks such as lasers or energy manipulation spells."])
add("Fling", "manipulation", "AWK", 138, "P", "T", "I", drain(0, "M"), "As a ranged attack", ONE,
    "The caster psychokinetically hurls a single object at a target.",
    ["The caster must touch the item, and its weight in kilograms may not exceed the caster's Magic Rating.",
     "The object is thrown with a Strength equal to the spell's Force.",
     "Treat the Spell Success Test as a normal ranged attack test. Throwing weapons travel the standard range for the weapon type, based on the spell's Force."])
add("Gecko Crawl", "manipulation", "AWK", 138, "P", "T", "S", drain(1, "M"), "6", ONE,
    "A voluntary subject can crawl along vertical surfaces at half their normal Quickness Rating.",
    ["Gravity still applies: the subject falls if they jump or push away from the surface.",
     "On a particularly slick surface the gamemaster may require Athletics (Climbing) Tests."])
add("Alter Temperature", "manipulation", "AWK", 138, "P", "Limited", "S", drain(2, "S"), "6", AREA,
    "An area-effect spell that raises or lowers the ambient temperature, as the caster chooses.",
    ["Alters the area's temperature by 5 degrees centigrade for every 2 successes.",
     "Sufficiently extreme temperatures generally cause unprotected characters 4L Stun damage per minute of exposure, and may interfere with some machines."])
add("Bug Barrier", "manipulation", "AWK", 139, "M", "LOS", "S", drain(2, "D"), "6", AREA,
    "Creates a magical shield, similar to a Mana Barrier (SR2 p.158), that blocks only insect spirits.",
    ["The Barrier Rating equals the spell's Force.",
     "Any insect spirit touching the shield suffers feedback with a base Damage Code of (Force)L, raised one level for every 2 successes on the casting."],
    dmg="(Force)L to insect spirits")
add("Clean Air", "manipulation", "AWK", 139, "P", "Limited", "I", drain(1, "S"), "Object Resistance (set by the impurities)", AREA,
    "An area-effect spell that clears all impurities from the air in the area, leaving it clean and breathable.",
    ["The gamemaster sets the target number by the impurities present: 3 or 4 for smoke or fog, as high as 10 or 12 for complex nerve toxins.",
     "In an open area with moving air, the cleared air quickly mixes with the surrounding air."])
add("Clean Water", "manipulation", "AWK", 139, "P", "T", "P", drain(0, "S"), "Object Resistance (set by the impurities)", AREA,
    "Removes impurities from a sphere of water with a radius equal to the caster's Magic Rating in meters.",
    ["The gamemaster sets the target number by the impurities: 3 for dirt and organic sediment, as high as 10 for industrial chemicals.",
     "In an open body of water, the cleared water quickly mixes with the surrounding water."], turns=10)
add("Control Fire", "manipulation", "AWK", 139, "P", "LOS", "S", drain(2, "S"), "Power of the flames", ONE,
    "The caster controls normal flames within line of sight.",
    ["The gamemaster sets the fire's Power: 3 or 4 for a camp fire or a single burning item, as high as 15 to 20 for a burning building or forest fire.",
     "The caster can move the flames up to 1 meter per success, provided there is fuel, make them flare (+1 Power for every 2 successes), or contain them and let them burn out.",
     "Does not affect magically sustained flames such as fire elementals or Firewall spells, but does affect flames started by spells such as Ignite."])
add("Extinguish Fire", "manipulation", "AWK", 139, "P", "LOS", "I", drain(1, "S"), "Power of the flames", AREA,
    "An area-effect spell that extinguishes fires.",
    ["The gamemaster sets the fire's Power: 3 or 4 for a camp fire or a single burning item, as high as 15 to 20 for a burning building or forest.",
     "Every 2 successes reduce the fire's Damage Level by 1, starting from (Power)M. Reduced to nothing, the fire is out. Otherwise it regains 1 Damage Level per Combat Turn up to its initial strength.",
     "Has no effect on magically sustained fires, but does affect fires set by magical means such as Ignite."])
add("Firewall", "manipulation", "AWK", 139, "P", "LOS", "S", drain(2, "D"), "6", AREA,
    "Creates a wall of fire.",
    ["The wall's height in meters equals the spell's Force. Its length or radius equals the magician's Magic Rating.",
     "Causes (Force)M damage to anything that comes in contact with it and gives full visual cover to anyone behind it.",
     "Not solid: it does not block attacks, though it detonates explosives and other munitions that pass through."],
    dmg="(Force)M Physical")
add("Fix", "manipulation", "AWK", 139, "P", "T", "P", drain(1, "M"), ORT, ONE,
    "Repairs cracks, rips, tears, fractures and other damage to an inanimate object.",
    ["A single success is required.",
     "The item's weight in kilograms may not exceed the caster's Magic Rating, and the caster must have all the pieces.",
     "Makes only physical repairs; it does not restore magical bonds or properties."], turns=10)
add("Flame Aura", "manipulation", "AWK", 140, "P", "Limited", "S", drain(2, "M"), "6", ONE,
    "Creates a rippling aura of flames around a voluntary target, extending a number of centimeters equal to the spell's Force.",
    ["The flames do not harm the target or anything the target carries or wears.",
     "Anyone landing a successful melee attack on the subject must resist (Force)M damage. Armor helps if they strike with an armored part of the body.",
     "The subject's own successful melee attacks have the Power of their Damage Code increased by 2."],
    dmg="(Force)M Physical")
add("Freeze Water", "manipulation", "AWK", 140, "P", "LOS", "I", drain(1, "S"), "4", AREA,
    "An area-effect spell that freezes all water in the area into ice.",
    ["In a large body of water it creates a free-floating iceberg. Water freezing in containers or pipes may burst them.",
     "The ice melts normally according to the ambient temperature.",
     "Does not affect the water in living beings, manifested water spirits or water elementals."])
add("Glue", "manipulation", "AWK", 140, "P", "LOS", "S", drain(2, "S"), "6", ONE,
    "Magically bonds two inanimate surfaces together.",
    ["The bond's Force equals the spell's Force plus 1 for every 2 successes.",
     "Separating the surfaces takes a Strength Test against the Force of the bond.",
     "A surface with a Barrier Rating lower than the bond's Force is torn apart when the surfaces are separated."])
add("Heat Shield", "manipulation", "AWK", 140, "P", "Limited", "S", drain(2, "M"), "6", AREA,
    "Creates a barrier that offers protection from fire- and heat-based attacks.",
    ["Subtract the spell's Force from the Power of flame spells, flame powers, flamethrowers and similar attacks when determining damage.",
     "Does not protect against the Ignite spell or anything that lights a fire.",
     "The personal form of this spell has a Drain Code of [(F/2)+2]L."])
add("Light Ray", "manipulation", "AWK", 140, "M", "LOS", "I", drain(1, "D"), "4", ONE,
    "Fires a beam of light at a target, with effects comparable to those of a laser weapon.",
    ["At the gamemaster's discretion it may produce elemental light effects."], dmg="Serious")
add("Mental Shield", "manipulation", "AWK", 140, "M", "LOS", "S", drain(1, "M"), "4", ONE,
    "Protects against spells and powers that affect the mind.",
    ["For every 2 successes the subject gains 1 extra die to resist mind probe, control manipulations, mana-based illusions, and critter powers such as influence and desire reflection.",
     "Does not protect against mana-type combat spells."])
add("Mist", "manipulation", "AWK", 140, "P", "Limited", "S", drain(2, "S"), "6", AREA,
    "An area-effect spell that creates a thick mist.",
    ["Imposes the vision penalties for heavy fog (Visibility Table, SR2 p.89) for as long as the spell is sustained.",
     "When the spell is dropped the mist dissipates quickly, depending on temperature and wind."])
add("Net", "manipulation", "AWK", 141, "P", "LOS", "S", drain(2, "D"), "Quickness (R)", AREA,
    "An area-effect version of the Bind spell (Grimoire p.131) that traps and holds any target in the area.",
    ["Targets resist with a Quickness Test against the spell's Force. The net's Barrier Rating equals the caster's net successes.",
     "Targets may break out by the standard barrier rules. A Strength Test against the spell's Force adds 1 to Strength for every 2 successes.",
     "After breaking free, the character must resist (Strength)L Stun damage from the effort."])
add("Sap Strength", "manipulation", "AWK", 141, "P", "LOS", "S", drain(2, "S"), "6", ONE,
    "Reduces the strength of a living or inanimate target.",
    ["Living target: Strength is reduced by 1 for every 2 successes. At 0 or less the subject is immobilized.",
     "Inanimate target: if the successes exceed its Barrier Rating, the target collapses."])
add("Shape Earth", "manipulation", "AWK", 141, "P", "LOS", "S", drain(2, "D"), ORT, AREA,
    "The caster magically moves and shapes a quantity of earth in the spell's area of effect.",
    ["Lets the caster rapidly dig or fill holes, tunnels and trenches, push over earthen barricades and the like.",
     "Also works on processed materials such as glass, metal and concrete.",
     "Reshaped material reverts to its previous shape when the spell is dropped."])
add("Shape Water", "manipulation", "AWK", 141, "P", "LOS", "S", drain(2, "D"), ORT, AREA,
    "Works in the same manner as the Shape Earth spell, but affects water and other liquids.",
    ["Reshaped liquid reverts to its previous shape when the spell is dropped."])
add("Smoke Cloud", "manipulation", "AWK", 141, "P", "LOS", "S", drain(3, "D"), "4", AREA,
    "Creates a cloud of thick, sulfurous smoke covering a radius in meters equal to the caster's Magic Rating.",
    ["Each Combat Turn the cloud inflicts Stun damage on all targets within the area.",
     "Adds 4 to all sight-based target numbers for tests made in the area.",
     "Armor does not reduce the damage, but a sealed breathing apparatus or air filter negates it entirely."],
    dmg="Moderate Stun")
add("Spirit Barrier", "manipulation", "AWK", 141, "M", "Limited", "S", drain(2, "M"), "6", AREA,
    "An area-effect spell that works like a Mana Barrier but affects only spirits and other astral entities, such as astrally projecting magicians.",
    ["All other creatures and objects, including dual-natured creatures and bonded magical items, pass through normally.",
     "The Barrier Rating equals one-half the spell's Force. Add it to the target numbers of magicians casting spells through the barrier."])
add("Temper", "manipulation", "AWK", 141, "P", "T", "S", drain(1, "M"), ORT, ONE,
    "Alters an inanimate material to make it stronger.",
    ["For every success, increase the Barrier Rating of the item by 2.",
     "The object's weight in kilograms may not exceed twice the caster's Magic Rating."])
add("Wind", "manipulation", "AWK", 141, "P", "LOS", "I", drain(1, "S"), "6", AREA,
    "An area-effect spell that produces a wind in whatever direction the caster desires.",
    ["The strength of the wind equals the Force of the spell.",
     "Scatters light objects, and knocks over freestanding items with a Barrier Rating lower than the spell's Force.",
     "Living targets in the area must make a Knockdown Test against the spell's Force."])


def main() -> None:
    names = [s["n"] for s in SPELLS]
    assert len(names) == len(set(names)), "duplicate spell name"
    lines = ",\n".join(json.dumps(s, ensure_ascii=False) for s in SPELLS)
    OUT.write_text(f"[\n{lines}\n]\n", encoding="utf-8")
    print(f"wrote {len(SPELLS)} spells to {OUT}")


if __name__ == "__main__":
    main()
