"""One-off generator for docs/gear_modifiers_report.csv -- a reviewable list of every catalog item
whose description/notes carry a mechanical bonus not yet in a structured field. Columns include a
blank "Corrected Value" for the user to annotate (same workflow as the vehicle name report).

Placement column reflects the user's guidance:
  - weapon bonuses w/o clean math -> the weapon's Modifiers slot (recoil comp, smartlink, TN sights)
  - armor bonuses -> folded into the armor Total (shown alongside what they're wearing)
  - attribute mods -> the attribute slot (e.g. Encephalon +Int)
  - skill-dice mods -> a note in the Gear section next to the item (or an existing dice pool)
  - ammo / misc TN -> Modifiers or Gear section
"""
import csv
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

# (file, item, bonus text, mechanical effect, suggested field, sheet placement)
ROWS = [
    # ---- armor.json ----
    ("armor.json", "Lined Coat", "+2 to conceal any weapon hidden beneath it", "+2 Conceal to all weapons beneath", "conceal_bonus / conceal_scope=beneath", "Weapon Conceal (DONE)"),
    ("armor.json", "Secure Long Coat", "adds 50% to concealability of any weapon rated 4+", "+50% Conceal for weapons conceal>=4", "conceal_bonus_pct / conceal_min_rating", "Weapon Conceal (DONE)"),
    ("armor.json", "Forearm Guards", "Can be used to strike, doing (Str+1)M damage", "Melee attack mode (STR+1)M", "melee_attack", "Weapon (as a melee entry)"),
    ("armor.json", "Heavy Armor, Partial Suit", "affects Combat Pool (see p.84)", "Combat Pool penalty (armor vs Quickness)", "combat_pool_penalty", "Combat Pool / armor note"),
    ("armor.json", "Heavy Armor, Full Suit", "affects Combat Pool (see p.84)", "Combat Pool penalty", "combat_pool_penalty", "Combat Pool / armor note"),
    ("armor.json", "Light Military Armor", "Reduces Combat Pool by 1 per 2 Ballistic above Quickness", "-1 Combat Pool per 2 Ballistic > Qck", "combat_pool_penalty", "Combat Pool / armor note"),
    ("armor.json", "Medium Military Armor", "same Combat Pool formula", "-1 Combat Pool per 2 Ballistic > Qck", "combat_pool_penalty", "Combat Pool / armor note"),
    ("armor.json", "Heavy Military Armor", "same Combat Pool formula", "-1 Combat Pool per 2 Ballistic > Qck", "combat_pool_penalty", "Combat Pool / armor note"),
    ("armor.json", "Gel-Pack Armor", "Makes host armor Hardened; halves host Concealability", "Grants Hardened; host Conceal x0.5", "grants_hardened / host_conceal_mult", "Armor total note"),
    ("armor.json", "Small/Large Riot Shield", "+2 modifier to own melee attacks; strike (Str+2)S Stun", "+2 melee TN penalty; melee (STR+2)S", "melee_attack_penalty / melee_attack", "Weapon modifiers"),
    ("armor.json", "Camo-Spec Camouflage Suit/Jacket", "Grants Perception concealment bonuses (p.77)", "+TN to spot the wearer", "perception_penalty_to_spot", "Gear note"),
    # ---- weapons.json accessories ----
    ("weapons.json", "Concealable Holster", "+2 to pistol Concealability", "+2 Conceal to one holstered pistol/taser", "conceal_bonus / conceal_scope=pistol", "Weapon Conceal (DONE)"),
    ("weapons.json", "Bipod", "provides 2 points recoil comp", "Recoil Comp 2", "recoil_comp", "Weapon modifiers"),
    ("weapons.json", "Gas-Vent II", "recoil comp Rating 1", "Recoil Comp 1", "recoil_comp", "Weapon modifiers"),
    ("weapons.json", "Gas-Vent III", "recoil comp Rating 2", "Recoil Comp 2", "recoil_comp", "Weapon modifiers"),
    ("weapons.json", "Gyro Mount, Standard", "recoil/movement comp Rating 5", "Recoil/movement Comp 5", "recoil_comp", "Weapon modifiers"),
    ("weapons.json", "Gyro Mount, Deluxe", "recoil/movement comp Rating 6; built-in smartgun link", "Recoil Comp 6 + Smartlink -2 TN", "recoil_comp / smartlink", "Weapon modifiers"),
    ("weapons.json", "Improved Gyro-Mount System", "negates recoil up to rating; half Combat Pool; +4 melee", "Recoil Comp 5; Combat Pool x0.5; +4 melee TN", "recoil_comp / combat_pool_mult / melee_tn_penalty", "Weapon modifiers"),
    ("weapons.json", "Deluxe Gyro-Mount System", "same, Rating 7", "Recoil Comp 7; Combat Pool x0.5; +4 melee TN", "recoil_comp / combat_pool_mult / melee_tn_penalty", "Weapon modifiers"),
    ("weapons.json", "Shock Pads", "1 point recoil comp", "Recoil Comp 1", "recoil_comp", "Weapon modifiers"),
    ("weapons.json", "Tripod", "6 points recoil comp", "Recoil Comp 6", "recoil_comp", "Weapon modifiers"),
    ("weapons.json", "Laser Sight", "aiming beam to improve accuracy", "-1 TN at short range", "tn_bonus_short", "Weapon modifiers"),
    ("weapons.json", "Sound Suppressor", "+2 to detect the shooter", "+2 TN to locate shooter", "detect_shooter_penalty", "Weapon modifiers"),
    ("weapons.json", "ArmTech MGL-12 / Mini-6", "+2 recoil modifier; comp only via gyro-mounts", "+2 recoil penalty", "recoil_penalty", "Weapon modifiers"),
    ("weapons.json", "Ultrasound Sight", "reveals targets in darkness/thermo/invis", "Vision-bypass targeting", "vision_mode", "Weapon modifiers"),
    ("weapons.json", "Ultrasound Goggles", "halves visibility penalties (dim/dark/invis)", "Visibility penalty x0.5", "vis_penalty_mult", "Gear note"),
    # ---- weapons.json ammo ----
    ("weapons.json", "Regular Ammo", "-1 Concealability per extra 10 rounds", "-1 Conceal per 10 extra rounds", "extra_conceal_penalty_per", "Gear note"),
    ("weapons.json", "EX Explosive Ammo", "Adds +2 to the weapon's Power", "+2 Power", "power_bonus", "Weapon modifiers / gear"),
    ("weapons.json", "Tracer Ammo", "-1 TN beyond Short per third tracer (auto)", "-1 TN beyond Short per 3rd tracer", "tn_bonus_beyond_short", "Gear note"),
    ("weapons.json", "APDS Ammunition", "halves Ballistic/Barrier; vehicle armor half + -1 dmg lvl", "Halves ballistic; vehicle armor x0.5, -1 dmg", "halve_ballistic / vehicle_armor_half", "Weapon modifiers / gear"),
    # ---- weapons.json firearms with integral accessories ----
    ("weapons.json", "HK HK227", "integral laser sight; integral gas-vent recoil comp", "Laser -1 TN; Recoil Comp 1", "recoil_comp / laser_sight", "Weapon modifiers"),
    ("weapons.json", "Uzi III", "integral folding stock; integral laser sight", "Stock recoil comp; laser -1 TN", "recoil_comp / laser_sight", "Weapon modifiers"),
    ("weapons.json", "FN HAR", "integral folding stock; barrel gas-vent recoil comp", "Recoil Comp 1", "recoil_comp", "Weapon modifiers"),
    ("weapons.json", "Ingram Valiant", "gas-vent (Rating 2) + recoil pad (Rating 1)", "Recoil Comp 3", "recoil_comp", "Weapon modifiers"),
    ("weapons.json", "Enfield AS-7", "-1 die to recoil compensation", "-1 die recoil comp", "recoil_comp", "Weapon modifiers"),
    ("weapons.json", "Crusader Machine Pistol", "Integral Gas-Vent 2 recoil compensation", "Recoil Comp 2", "recoil_comp", "Weapon modifiers"),
    ("weapons.json", "Predator II", "Integral Ares Smartlink", "Smartlink -2 TN", "smartlink", "Weapon modifiers"),
    ("weapons.json", "Beretta Model 200ST", "Shoulder-stock gives 1 point Recoil Compensation", "Recoil Comp 1 (w/ stock)", "recoil_comp", "Weapon modifiers"),
    ("weapons.json", "Ultra-Power", "Integral LasSys XMS laser sight", "Laser -1 TN", "laser_sight", "Weapon modifiers"),
    ("weapons.json", "Black Scorpion", "Folding stock gives 1 point Recoil Reduction", "Recoil Comp 1", "recoil_comp", "Weapon modifiers"),
    ("weapons.json", "Combat Axe", "Spring-out point: Reach 0, Damage (Str+2)S", "Secondary attack (Reach 0, (STR+2)S)", "alt_attack", "Weapon modifiers"),
    ("weapons.json", "Shock Glove", "Damage (Str+1)M when worn but not discharging", "Passive damage mode (STR+1)M", "alt_attack", "Weapon modifiers"),
    ("weapons.json", "Ares Alpha Combatgun", "Integral Smartlink II; 2 Recoil Reduction; grenade launcher", "Smartlink -2 TN; Recoil Comp 2; GL", "smartlink / recoil_comp", "Weapon modifiers"),
    ("weapons.json", "Ares HVAR", "Integral Smartlink II, 3 Recoil Reduction", "Smartlink -2 TN; Recoil Comp 3", "smartlink / recoil_comp", "Weapon modifiers"),
    ("weapons.json", "Barret Model 121", "2 Recoil Reduction w/ +2 recoil mod; Integral Smartlink I", "Net Recoil Comp 2 (+2 pen); Smartlink -2 TN", "smartlink / recoil_comp / recoil_penalty", "Weapon modifiers"),
    ("weapons.json", "Franchi SPAS-22", "1 Recoil Reduction; +2 recoil mod; Integral Smartlink II", "Recoil Comp 1 (+2 pen); Smartlink -2 TN", "smartlink / recoil_comp / recoil_penalty", "Weapon modifiers"),
    ("weapons.json", "MP Laser", "No recoil penalty; halves Ballistic/Impact armor", "Recoil immune; armor halved", "no_recoil / halve_armor", "Weapon modifiers"),
    ("weapons.json", "Ares MP Laser III", "Ballistic ignored; Impact halved; Power -2 per band > Short", "Full ballistic bypass; power falloff", "armor_bypass / power_falloff", "Weapon modifiers"),
    ("weapons.json", "Flash-Bang Grenade (BSW)", "+5 to target numbers from the flash", "+5 TN to targets", "flash_tn", "Gear note"),
    ("weapons.json", "(~35 BSW firearms)", "Integrated smartlink / gas-vent recoil / laser sight", "Same recoil/smartlink/laser gaps as above", "recoil_comp / smartlink / laser_sight", "Weapon modifiers"),
    # ---- gear.json ----
    ("gear.json", "Sneak Suit", "+4 to all TNs to spot the wearer", "+4 TN to spot (when active)", "perception_penalty_to_spot", "Gear note"),
    ("gear.json", "Thermographic Camouflage Dye", "mixed thermo/normal viewers get +2 spotting penalty", "+2 TN mixed-vision spotters (+4 thermo)", "perception_penalty_mixed", "Gear note"),
    ("gear.json", "RadTech SmartWheel", "+1 effective Quickness for skating only", "+1 Quickness (skating)", "qck_bonus / scope=skating", "Gear note"),
    ("gear.json", "StreetMaster PoonGun", "Taser ranges at +1 to all TNs", "+1 TN to all attacks", "tn_penalty", "Weapon modifiers"),
    # ---- cyberware.json ----
    ("cyberware.json", "Smartlink", "reduces TN on smartgun weapons by 2", "-2 TN on smartgun weapons", "smartlink", "Weapon modifiers"),
    ("cyberware.json", "Dermal Plating L1/L2/L3", "+1/2/3 Body for resisting damage", "+N Ballistic & Impact armor", "ballistic_bonus / impact_bonus", "Armor total"),
    ("cyberware.json", "Dermal Sheath L1/L2/L3", "+1/2/3 Ballistic and Impact", "+N Ballistic & Impact", "ballistic_bonus / impact_bonus", "Armor total"),
    ("cyberware.json", "Bone Lacing", "+Body/+Impact/+Ballistic + unarmed (Str+N)M by level", "Armor + unarmed damage upgrade", "impact_bonus / ballistic_bonus / unarmed_dmg", "Armor total + Weapon"),
    ("cyberware.json", "Encephalon", "L1 +1 Int; L3 +2 Int (+ Task Pool)", "+1/+2 Intelligence", "modsPer.intelligence", "Attribute slot (Int)"),
    ("cyberware.json", "Tactical Computer", "lowers ranged TN by 1 (melee 1 per 2 levels)", "-1 ranged TN; -1 melee per 2 lvl", "ranged_tn_bonus / melee_tn_bonus", "Weapon modifiers"),
    ("cyberware.json", "Spatial Recognizer", "-2 TN on hearing-location Perception", "-2 TN hearing-location Perception", "perception_tn_bonus", "Gear note"),
    ("cyberware.json", "Balance Augmenter", "-2 TN Athletics (balance); -2 opposed Knockdown", "-2 TN balance; -2 knockdown", "athletics_tn_bonus / knockdown_bonus", "Gear note"),
    ("cyberware.json", "Move-by-Wire L1-L4", "+1/2/3/4 die for Athletics and Stealth", "+N dice Athletics & Stealth", "skill_dice_bonus", "Gear note / skill dice"),
    ("cyberware.json", "Pain Editor", "ignores wound modifiers; +4 TN tactile Perception", "Wound-mod immunity; +4 TN tactile", "ignore_wound_mods / tactile_penalty", "Gear note"),
    ("cyberware.json", "Vehicle Control Rig L1/L2/L3", "+2/4/6 Reaction while rigging", "+2/4/6 Reaction (rigging)", "reaction_while_rigging", "Reaction (already modeled)"),
    ("cyberware.json", "Olfactory Booster", "+1 die smell Perception per lvl; +1 taste per 3 lvl", "+N dice smell/taste Perception", "perception_dice_bonus", "Gear note"),
    ("cyberware.json", "Cyberarm Gyromount", "standard gyromount, 3 Recoil Reduction", "Recoil Comp 3", "recoil_comp", "Weapon modifiers"),
    # ---- bioware.json ----
    ("bioware.json", "Orthoskin L1/L2/L3", "+Impact / +Ballistic by level", "+N Ballistic & Impact armor", "ballistic_bonus / impact_bonus", "Armor total"),
    ("bioware.json", "Synthacardium L1/L2", "+1/+2 dice to Athletics tests", "+N dice Athletics", "athletics_dice_bonus", "Gear note / skill dice"),
    ("bioware.json", "Tailored Pheromones L1/L2", "+1/+2 dice Charisma/Social tests", "+N dice Social/Charisma", "social_dice_bonus", "Gear note / skill dice"),
    ("bioware.json", "Adrenal Pump L1/L2", "+Qck/+Str/+Wil/+Reaction on activation", "Activated attribute boosts", "activated_mods", "Attribute slot (activated)"),
    ("bioware.json", "Damage Compensator", "ignore wound penalties up to its level", "Ignore N wound boxes", "ignore_wound_boxes", "Gear note"),
    ("bioware.json", "Mnemonic Enhancer", "+1 die/2 lvl Knowledge/Language; -1 TN/lvl recall", "+dice Knowledge; -TN recall", "knowledge_dice_bonus / recall_tn_bonus", "Gear note"),
    ("bioware.json", "Enhanced Articulation", "+1 die to motion-intensive Active-Skill tests", "+1 die motion skills (Athletics etc.)", "motion_skill_dice_bonus", "Gear note / skill dice"),
    ("bioware.json", "Trauma Damper", "reduce wound's Damage Level by 1; +2 TN to cause you pain", "Wound-level -1; +2 TN pain attempts", "wound_damage_reduction / pain_tn_penalty", "Gear note"),
    ("bioware.json", "Nephritic Screen", "+1 Body vs toxins/pathogens; -1 blood-toxin Power", "+1 Body vs toxins; -1 blood-toxin Power", "toxin_body_bonus / blood_toxin_power", "Gear note"),
    ("bioware.json", "Platelet Factory", "Body Test at +1 TN per use (thrombosis risk)", "+1 TN Body test per use (cumulative)", "cumulative_use_penalty", "Gear note"),
    # ---- adept_powers.json ----
    ("adept_powers.json", "Combat Sense", "+1/2/3 Combat Pool dice", "+N Combat Pool dice", "combat_pool_bonus", "Combat Pool"),
    ("adept_powers.json", "Mystic Armor", "+1 armor vs ALL attacks per level", "+N Ballistic & Impact", "mystic_armor_bonus", "Armor total"),
    ("adept_powers.json", "Iron Will", "+1 die resist Control/Illusion/Influence per lvl", "+N spell-resist dice (categories)", "spell_resist_dice_bonus", "Powers note"),
    ("adept_powers.json", "Magic Resistance", "+1 die resist any hostile sorcery per lvl", "+N general spell-resist dice", "spell_resist_dice_bonus", "Powers note"),
    ("adept_powers.json", "Quick Draw", "eliminates +2 TN for draw-and-fire", "Removes +2 draw-and-fire TN", "negate_draw_and_fire_penalty", "Weapon modifiers"),
    ("adept_powers.json", "Killing Hands", "Power = Strength; magical weapon", "Unarmed damage code; magical weapon", "unarmed_dmg / is_magical_weapon", "Weapon (unarmed)"),
]


def main():
    out = ROOT / "docs" / "gear_modifiers_report.csv"
    with open(out, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["Catalog", "Item", "Bonus Text", "Mechanical Effect",
                    "Suggested Field", "Sheet Placement", "Corrected Value"])
        for file, item, text, effect, field, placement in ROWS:
            w.writerow([file, item, text, effect, field, placement, ""])
    print(f"Wrote {out}  ({len(ROWS)} rows)")


if __name__ == "__main__":
    main()
