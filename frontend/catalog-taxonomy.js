/* Shared SR2 catalog taxonomy -- how catalog items are bucketed into display groups
   (weapon class, armor class, cyberware location, vehicle piloting skill). Loaded by BOTH the
   gear picker (gear-picker.js, mounted in play-sheet.html's Buy Gear modal) and the character
   builder's Asset Manifest step (character-builder.html) so the two browsers always group the same
   item the same way. Keep this the single source of truth; do not re-declare these names in the
   page scripts. */
"use strict";

// Title-case a lowercase catalog category ("firearm" -> "Firearm") for a group header.
function titleCase(s) { return String(s || "Other").replace(/\b\w/g, c => c.toUpperCase()); }

const WEAPON_GROUP_ORDER = ["Pistols", "SMGs", "Rifles", "Shotguns", "Machine Guns", "Other Firearms",
  "Heavy Weapons", "Explosives & Grenades", "Melee", "Bows & Crossbows", "Exotic Weapons", "Accessories", "Ammunition"];
// Bucket a weapon into a display section: firearms split by sub (Pistols/SMGs/Rifles/...), other cats map straight.
function weaponGroupLabel(it) {
  const c = it.cat || "", sub = it.sub || "";
  // Ammunition first: arrows/bolts, and missiles/rockets are ammo -- not the weapon that fires them.
  if (c === "ammo" || /arrow|bolt/i.test(sub)) return "Ammunition";
  if (c === "explosive" && /rocket|missile/i.test(sub)) return "Ammunition";
  if (/machine gun/i.test(sub)) return "Machine Guns";   // LMG/MMG/HMG from the firearm OR heavy cats
  if (c === "firearm") {
    if (/hold-?out|pistol|taser/i.test(sub)) return "Pistols";
    if (/smg|submachine/i.test(sub)) return "SMGs";
    if (/shotgun/i.test(sub)) return "Shotguns";
    if (/rifle|carbine/i.test(sub)) return "Rifles";
    return "Other Firearms";
  }
  return { heavy: "Heavy Weapons", explosive: "Explosives & Grenades", melee: "Melee",
    projectile: "Bows & Crossbows", exotic: "Exotic Weapons", accessory: "Accessories", ammo: "Ammunition" }[c]
    || titleCase(c || "Other");
}

const ARMOR_GROUP_ORDER = ["Worn Armor", "Military-Grade", "Helmets", "Shields", "Accessories"];
function armorGroupLabel(it) {
  return { worn: "Worn Armor", military: "Military-Grade", helmet: "Helmets", shield: "Shields", accessory: "Accessories" }[it.cat || ""]
    || titleCase(it.cat || "Other");
}

const CYBER_GROUP_ORDER = ["Headware", "Eyeware", "Earware", "Bodyware", "Cyberlimbs", "Bodywire", "Rigger Gear", "Skillsofts", "Other"];
function cyberGroupLabel(it) {
  if (it.soft) return "Skillsofts";   // Active / Know / Linguasofts only
  return { headware: "Headware", earware: "Earware", eyeware: "Eyeware", bodyware: "Bodyware", limb: "Cyberlimbs", bodywire: "Bodywire", rigger: "Rigger Gear", other: "Other" }[it.cat] || titleCase(it.cat || "Other");
}

// The "Gear" shop tab mixes several unrelated sub-categories (rigger gear, tools, survival,
// surveillance, ...) into one tab -- these are its section headers. Anything not listed falls
// back to a title-cased version of its raw cat value.
const GEAR_CAT_LABELS = { rigger: "Rigger Gear", tool: "Tools & Repair", survival: "Survival",
  security: "Security & B&E", stealth: "Stealth & Concealment", transport: "Personal Transport",
  vehweapon: "Vehicle Weapons", program: "Matrix Programs", deck: "Cyberdecks" };
function gearGroupLabel(it) { return GEAR_CAT_LABELS[it.cat] || titleCase(it.cat || "Other"); }

// The vehicle catalogue groups by piloting skill, matching the (SV) specialization buckets.
const VEHICLE_SKILL_ORDER = ["Bike", "Car", "Hovercraft", "Motorboat", "Blimp", "Rotor Craft", "Winged Plane", "Vectored Thrust", "Drones", "Other"];
const SV_SKILL = {
  "Bike": { types: ["Bikes"] },
  "Car": { types: ["Cars & Ground", "Trucks & Vans"] },
  "Hovercraft": { sub: /hovercraft/ },
  "Motorboat": { sub: /boat|skiff|cruiser|speedboat|yacht|dinghy|catamaran|hydrofoil|water scooter/ },
  "Blimp": { sub: /blimp|zeppelin|airship|dirigible/ },
  "Rotor Craft": { sub: /helicopter|rotor|autogyro|gyro|tilt-wing/ },
  "Winged Plane": { sub: /prop|ultralight|glider|airliner|turbine/ },
  "Vectored Thrust": { sub: /jet|thunderbird|jump|vtol/ },
};
// Broad vehicle types (used to bucket vehicles into piloting-skill categories).
function vehicleType(v) {
  if ((v.cat || "") === "drone") return "Drones";
  const s = (v.sub || "").toLowerCase();
  // Watercraft first so "Water Scooter" doesn't fall into Bikes.
  if (/boat|skiff|cruiser|hovercraft|hydrofoil|\bship\b|yacht|submarine|speedboat|dinghy|raft|barge|catamaran|water|hull|jetski/.test(s)) return "Watercraft";
  if (/bike|cycle|moto|chopper|scooter|scoot|trike|moped/.test(s)) return "Bikes";
  if (/truck|van|apc|\bbus\b|lav|tank|\brv\b|transport|flatbed|tractor|ambulance|semi/.test(s)) return "Trucks & Vans";
  if (/heli|tilt|jet|prop|plane|glider|ultralight|blimp|airship|rotor|vtol|aircraft|wing|fighter|autogyro|gyro|airliner|turbine|zeppelin/.test(s)) return "Aircraft";
  return "Cars & Ground";
}
// Piloting-skill bucket for a vehicle. The GM overlay (VEHICLE_CLASSES, loaded per page) wins when
// set; otherwise fall back to the regex classification.
function vehicleSkillCategory(v) {
  if ((v.cat || "") === "drone") return "Drones";   // drones always cluster in their own section
  const overlay = (typeof VEHICLE_CLASSES !== "undefined" ? VEHICLE_CLASSES : {});
  const cls = overlay[v.n];
  if (cls && cls.skill) return cls.skill;
  // Check the sub-typed skills before Car so an air/water craft mis-typed as ground still lands right.
  for (const skill of ["Bike", "Hovercraft", "Motorboat", "Blimp", "Rotor Craft", "Winged Plane", "Vectored Thrust", "Car"]) {
    const def = SV_SKILL[skill];
    if (def.types && def.types.includes(vehicleType(v))) return skill;
    if (def.sub && def.sub.test((v.sub || "").toLowerCase())) return skill;
  }
  return "Other";
}
