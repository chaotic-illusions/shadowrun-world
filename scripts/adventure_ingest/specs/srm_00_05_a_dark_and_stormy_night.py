# SRM 00-05 A Dark and Stormy Night (FanPro/WizKids, 2004, SR3) -- campaign order #43. The Redmond
# Barrens, just off Redmond Fall City Road and dangerously close to Glow City, at 2:00 AM in a hail
# and acid-rain storm.
# SETTING NOTE: Seattle, not Denver -- the Redmond Barrens, Glow City, Fort Lewis, Puyallup,
# Everett. Denver is never mentioned. Every location row is city "Seattle".
# Dating: no in-world date; 2064 as for the rest of Season 0. The adventure runs in real time --
# an Ares containment team is flying in from Fort Lewis and the Game Over, Man! scene fires
# automatically when 45 minutes of the play slot remain, whatever the runners are doing.
# Book editing inconsistencies noted on the affected rows: the Introduction and Campaign Synopsis
# were copied from SRM 00-02 and still say "Demolition Run" twice and refer to "the downtown area
# where this scenario takes place" for an adventure set in the Redmond Barrens; the first scene is
# titled "Snow, Rain, Sleet or Hale"; "Many will explain that Kat was working on a contract"
# (Manny); the plot synopsis says "Kat is not aware that Stella was working for Ares", reversing
# the two names; the ruin is "a twelve story office building" of which "only the first six floors
# remain" in one paragraph and "only four stories remaining" in the read-aloud text; "containment
# breech"; Bishop's Green/Streetwise stat block prints Magic/Essence as "8/6" and omits a separate
# Essence line; and Schmitty's block carries a second, duplicated "Cyberware:" line belonging to
# Ralphie.
# Name disambiguation: the escaped flesh-form spirit is filed as "John (Flesh Form Ant Spirit)"
# because "John" alone is uselessly generic in a world with a dozen Johns.
# Source text: docs/Adventures/text/SRM00-05A_A_Dark_and_Stormy_Night.txt (23 pages) and
# docs/Adventures/text/SRM00-05B.txt (player aids, enemy card and forms, 9 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "SRM 00-05 A Dark and Stormy Night"
ORDER = 43
SOURCE = "SRM00-05A_A_Dark_and_Stormy_Night.pdf, pp. 3-23; SRM00-05B.pdf (Playing Aids), pp. 3-9"
YEAR = "2064"

SYNOPSIS = """
Several months ago **Ares Arms**, the military subdivision of Ares Macrotechnology, quietly built a
four-sublevel research and development facility into the old parking garage beneath a ruined
office block in the **Redmond Barrens**, off Redmond Fall City Road and close enough to Glow City
that runners will spend the night speculating about radiation. Its purpose is to bioengineer a
better toxin for killing insect spirits, and it keeps live specimens -- true-form and flesh-form
ant spirits -- in warded stasis for the testing. **Kat Austing**, an initiated hermetic mage who
contracts to the highest bidder, took the job as head of magical security through a friend on the
inside.

A few hours ago a bug spirit cut through Kevlar restraints during a dissection. It tore one
scientist in half, and Kat -- distracted, her spell released early, her ward above the door
flickering and dying as she watched -- was killed by it. She wounded it badly enough that
**Bishop**, the facility's other mage, could finish it. The facility is locked down, waiting for a
containment team flying in from **Fort Lewis** aboard Ares TR-55s, and for a few hours its magical
defences are crippled.

Kat had been on the phone the whole time. **Stella Smith**, her girlfriend, a Dog shaman who never
understood why Kat could not talk about her work, heard the screaming and then silence -- and had
the presence of mind to keep the line open while she called **Manny** on the telecom. Manny put one
of his star deckers on the open cell signal, got GPS coordinates, and at 2:00 AM starts calling
runners: 2,000 nuyen each to find out what happened to Kat and 3,000 more if they bring her home
alive. If the worst has happened, retrieve as much of the body as possible for the insurance
claim.

What follows is a horror scenario dressed as a rescue. Acid rain, a Background Count of 1 outside,
a generator that overloads and dies and leaves the place on failing emergency lights, and a
facility that seems entirely deserted because every surviving employee is locked down somewhere
the runners are not. Egyptian hieroglyphics etched on frosted glass walls that turn out to be
ward components -- Force 4 on sublevel 2, Force 8 on 3, and a Force 15 barrier wrapping the roof,
walls and floor of sublevel 4. A fire elemental Kat bound permanently to the emergency stairwell,
hidden behind a masking ward. Fresh blood. A test subject dragging himself along the floor begging
for help who is not remotely a man. And, when the clock runs down, ten five-man containment teams
coming out of the dark with insecticide rounds and a captain who tells everyone over the tannoy to
remain diligent at their posts until relieved.
"""

TIMELINE = """
- **Several months ago** -- Ares Arms sets up the Redmond Barrens facility to bioengineer a more
  effective anti-bug-spirit toxin, stocking it with captive true-form and flesh-form ant spirits
  as test subjects. Kat Austing hears through a friend at Ares Arms that the corporation needs a
  high-level mage for a "project" and uses that influence to win the contract.
- **Over those months** -- a flesh-form worker spirit calling itself John is operated on
  repeatedly; the scars record the pattern.
- **A few hours before the adventure** -- during a dissection a bug spirit tears through Kevlar
  straps. It kills a scientist and then Kat, who wounds it fatally; Bishop finishes it. Five
  flesh-form spirits are shot dead by guards; one escapes an operating table. Protocol CHARLIE,
  chemical rounds, lockdown. Sergeant Colby and Corporal Rachovsky ride the elevator down into it.
- **Immediately after** -- Ares calls for a containment team from Fort Lewis, expected in several
  hours by TR-55 VTOL. With Kat dead the facility's magical security is crippled in the meantime.
- **Stella, still on the open line**, hears everything, keeps the connection alive and calls Manny
  on the telecom. Manny puts a decker on the signal and has GPS coordinates within minutes, then
  tells Stella to hang up so nothing traces back to her.
- **2:00 AM** -- Manny calls the runners out of bed into a hail storm: 2,000 nuyen each, paid
  immediately by secure transfer, plus a data file with the coordinates and a photograph of Kat;
  3,000 more each if she comes home alive. He wants news within the hour.
- **That night** -- the drive into the Barrens, the ruin, the sensors, the elevator or the
  stairwell, four sublevels, Bishop, and Kat's body in the sealed testing lab behind yellow tape.
- **When 45 minutes of the session remain** -- the TR-55s land and Captain Kenneth Brooks assumes
  control. Get out quietly or lose everything.
"""

ORGS = [
    {
        "name": "Ares Arms",
        "org_type": "corporation",
        "tier": 5,
        "headquarters": "Ares Macrotechnology; Seattle divisional operations at Fort Lewis",
        "summary": "Ares Macrotechnology's military systems subdivision -- weapons, armor, vehicles, and the most extensive military capability of any megacorp.",
        "description": (
            "Ares Arms is the military systems subdivision of Ares Macrotechnology, and the module "
            "quotes Corporate Shadowfiles on what that means: a competitive Desert Wars force; an "
            "extensive set of trained test-and-evaluation personnel capable of putting any new "
            "weapon or support system through its paces; and a team of end-user consultants "
            "assigned to train purchasers of Ares' military products to use them efficiently. With "
            "the possible exception of Aztechnology, Ares has the most extensive military "
            "capability of any megacorporation. Expect Ares Arms always to have the best new toys "
            "on the market, all military grade. Its combat troops and military security forces are "
            "almost always cybered to the gills and outfitted with full military-grade armor and "
            "tactical communications gear, and standby teams can respond by helicopter or tilt-rotor "
            "to another Ares Arms facility within ten minutes. Though primarily concerned with "
            "military hardware, it staffs arcane security forces as well: combat-trained adepts and "
            "mages, paranormal animals and spirits."
        ),
        "notes": (
            "In this adventure Ares Arms is running something well outside the weapons catalogue. "
            "Several months ago it built a four-sublevel research and development facility in the "
            "Redmond Barrens to bioengineer a new toxin more effective against insect spirits, and "
            "stocked it with live true-form and flesh-form ant spirits as test subjects -- an "
            "operation with a higher-than-normal amount of magical security precisely because of "
            "what is in the specimen storage rooms. The security posture is built around "
            "containment rather than intrusion: chemical rounds instead of lead, spray dispensers "
            "of insecticide foam in the labs, Ares ELD-AR assault rifles loaded with insecticide "
            "rounds in the alcove outside the main testing lab, Chemsuits in the decontamination "
            "room, protocol CHARLIE, and a containment team on call at Fort Lewis that arrives by "
            "TR-55 VTOL transport. The security-cleared guards are not allowed into the labs at all "
            "unless an alarm sounds, and they trade theories about mutants from the Glow, space "
            "aliens from the crashed suborbital, and things that go bump in the night."
        ),
        "allies": ["Ares Macrotechnology", "Ares Arms Seattle Division"],
    },
    {
        "name": "Ares Arms Seattle Division",
        "org_type": "corporation",
        "tier": 5,
        "headquarters": "Fort Lewis (operations and division headquarters), Seattle",
        "summary": "The Seattle arm of Ares Arms, and the enemy a careless team walks away from this run having made.",
        "description": (
            "Seattle's Ares Arms division works out of and supports Fort Lewis and the military "
            "base there. Its offices are spread throughout Seattle, including space in the main "
            "Ares Macrotechnology enclave for administration; Fort Lewis holds operations and the "
            "divisional headquarters; a facility in Everett manufactures armor plating for all "
            "drones and vehicles; and the division routinely uses the Puyallup and Redmond Barrens "
            "for weapons testing and demonstrations -- a habit that provides convenient cover for a "
            "black research site in Redmond that has nothing to do with weapons testing at all."
        ),
        "notes": (
            "This is the enemy card the module hands out (SRM00-05B p.5), and the mechanics matter. "
            "Initial rating 2 -- Power 5, Motivation 0, Knowledge 2 (SR Companion p.68; rating "
            "totals 0/4/6/8/11/14/17 points). Modifiers earned in this run: minimal damage or "
            "killing +0/+0/+0; significant damage or killing +0/+1/+0; selling information about "
            "the facility +0/+1/+0, cumulative with either of the first two. A runner photographed "
            "committing heavy property damage, looting or killing every guard they meet AND later "
            "identified as selling the data takes +0/+2/+0. Crucially, the enemy is gained ONLY if "
            "the runners are photographed: masks, disguises, invisibility or defeating the camera "
            "system means no image and no dossier. Note it on the Mission Log -- having an Enemy "
            "means a file is being kept and that the division will appear in later adventures and "
            "act according to its current level. Fencing the facility data yourself rather than "
            "through Manny brings five Ares fast response teams to ambush the deal."
        ),
        "allies": ["Ares Arms", "Ares Macrotechnology"],
    },
    {
        "name": "Ares Arms Special Magic Corps",
        "org_type": "corporate security division",
        "tier": 5,
        "headquarters": "Fort Lewis, Seattle",
        "summary": "Ares Arms' magical containment force, flown in by TR-55 to lock down a breached facility and relieve everyone in it.",
        "description": (
            "The unit that arrives at the end of the adventure: ten five-man containment teams plus "
            "a captain, a rigger, a decker and a team of medical doctors, all in full security "
            "armor with environmental seals, delivered by Ares TR-55 VTOL transports from Fort "
            "Lewis. Its commander announces himself over the facility loudspeakers -- 'This is "
            "captain Kenneth Brooks of the Ares Arms Special Magic corps containment team. I am "
            "assuming control as chief security officer at this facility. My team is being "
            "dispatched throughout the facility and will take over for security and containment. "
            "Please remain diligent at your post until relieved by the containment team.' Every "
            "five-man element pairs two heavily cybered security specialists with two grade 4 "
            "initiate warrior adepts and a grade 4 hermetic combat mage, with bound elementals in "
            "support."
        ),
        "notes": (
            "Five-man team composition. SECURITY SPECIALIST (2): B6(8) Q5 S4 C3 I5 W4, Reaction "
            "5(9), Init 9+3D6, Combat Pool 7, Karma 3; Wired Reflexes 2, Smartlink II, cybereyes "
            "(thermo, flare comp, rangefinder), dermal plating 2; Assault Rifle 6, Stealth 6, "
            "Pistol 4, Thrown 4; Bio-containment Protocol 4, Bug Spirits 4, Magic Threats 3. WARRIOR "
            "ADEPT (2): B6 Q8 S9 C9 I5 W5, Reaction 6, Init 8+2D6, Magic 10, grade 4 initiate "
            "(Masking, Centering with stealth, athletics and melee); Improved Reflexes 1, Quick "
            "Strike, Astral Perception, Counter Strike 2; Unarmed 8, Assault Rifle 6, Stealth 6, "
            "Centering 6, Athletics 6; Bug Spirits 6. COMBAT MAGE (1): B4(8) Q4 S3 C4 I6 W6, "
            "Reaction 5(8), Init 5+1D6 / 8+4D6, Magic 9, grade 4 hermetic initiate (Masking, "
            "Quickening, Anchoring, Shielding); Sorcery 9, Conjuring 6; Manabolt 7, Stun Ball 9, "
            "Control Thoughts 8, Armor 8, Improved Invisibility 6 and more. All wear light security "
            "armor with helmet, enviroseal, rating 5 encrypted helmet commlink and heads-up display "
            "(7/6), and carry Ares Alpha assault rifles switching between EX explosive (10M) and "
            "capsule rounds loaded with insecticide, plus a grenade link, four mini offensive "
            "grenades (10S) and an Ares Predator III. Support spirits: a Force 8 water elemental "
            "(2 services) and two Force 6 air elementals (2 services each). The mage sustains Armor "
            "with 4 successes on every man until his first action, the specialists get +4 dice of "
            "spell shielding from him and target mages first, and the adepts carry quickened Flame "
            "Aura 3 and Spell Shield 6 with an air elemental sustaining a Force 2 Invisibility on "
            "each of them at 10 successes. NOT A COMBAT SCENE: engage one team and two more join "
            "after two rounds; the module instructs the GM to make the outcome automatic -- every "
            "player takes a Deadly wound, loses all weapons and all magical, security- and "
            "military-grade gear, mages roll for magic loss, and everyone pays living and healing "
            "costs for the recovery time."
        ),
        "allies": ["Ares Arms", "Ares Arms Seattle Division"],
    },
]

LOCATIONS = [
    {
        "name": "Ares Arms Redmond Research Facility",
        "location_type": "research lab",
        "city": "Seattle",
        "district": "Redmond Barrens (off Redmond Fall City Road, near Glow City)",
        "security_level": "Corporate High Security",
        "controlling_org": "Ares Arms",
        "summary": "Black bug-spirit research site hidden in an old parking garage beneath a ruined office block in the Barrens.",
        "description": (
            "Above ground there is nothing but a ruin. A twelve-storey office building of which only "
            "the lower floors survive, choked with rubble from the collapsed floors above, standing "
            "among other buildings in the same state -- the wreckage of the riots of the early "
            "2000s, now makeshift homes for people eking out an existence in the Barrens. Picture a "
            "square doughnut: four outside walls, no roof, every ground entrance blocked by fallen "
            "rubble, and a centre that cannot be seen from the road cleared all the way down to "
            "ground level like an arena. In that cleared centre Ares keeps a secret landing pad for "
            "VTOL and rotor aircraft, and a small shed-like structure that is really the head of an "
            "elevator running four sublevels down into what used to be the building's underground "
            "parking garage. Below, the facility is entirely sterile and entirely alien -- ancient "
            "Egyptian inscriptions etched into frosted glass panes that serve as doors and inner "
            "walls throughout, a blend of hospital, magic library, prison and military installation. "
            "Tonight the main generator kicks on, overloads and dies, and the whole place runs on "
            "failing emergency lights."
        ),
        "notes": (
            "OUTSIDE. Perception is at minimal lighting (+6) and heavy rain (+6); the acid rain "
            "requires a Body (3) test modified by protective gear, with failure costing a Light "
            "stun wound plus sickness and coughing for the rest of the adventure, and the pollution "
            "creates a Background Count of 1 outdoors. Surveillance equipment is spotted on "
            "Perception (3); the sensors are rating 4 with opposed Stealth and a +5 TN penalty of "
            "their own for the rain, and being spotted alerts the facility at once. From above "
            "(Perception (4) or Sensors (2)): 0 successes shows the cleared arena and a makeshift "
            "shed; 1 identifies a landing pad; 2 catches warm exhaust from a grate hidden in the "
            "debris; 3 finds a hidden structure at floor level; 4+ shows a worn path from the pad "
            "to the shed. Astral scouting finds no magic at all from the surface, and the hidden "
            "stairwell exit takes Perception (6) physically or Astral Perception (6) (Background "
            "Count applies, darkness modifiers do not). WARDS: elevator and shaft Force 6, sublevel "
            "1 none, sublevel 2 Force 4, sublevel 3 Force 8, sublevel 4 Force 15; the hieroglyphics "
            "on the frosted glass are the physical components, so a mage passes only by winning "
            "astral combat or physically opening the doors. Frosted glass is barrier rating 8. "
            "ELEVATOR: the main entrance, sterile and chemically sealed (Perception (4)), with a "
            "chemical detector alarm, retinal, passkey and passcode security all at rating 6 -- one "
            "failed roll alerts the rigger and cuts power to the car. A frosted glass plaque at the "
            "back is a Force 7 expendable anchor focus (MITS p.45) carrying Detect Specific Facility "
            "Passkey Badge (Force 3) linked to Stun Ball (Force 4): anyone in the car without a "
            "passkey triggers it when the doors shut, 4M resolved on 7 dice against everyone "
            "inside. It is astrally active and can be beaten in astral combat. The roof hatch opens "
            "on an Electronics (5) override; the shaft is lined with rating 3 sensors. STAIRWELL: "
            "the old parking-garage emergency stair, running from the bottom level to a rubble "
            "blockage near the top where a ladder was added out to a well-hidden and never-used "
            "surface exit. Unlit, littered with garbage and putrid. Each level's door is "
            "chemically sealed, alarmed and one-way outward -- Electronics (4) kills the alarm, "
            "Lockpick (6) opens it from outside. Kat permanently bound a greater-form fire elemental "
            "with karma to guard it (Force 4, 7 or 10 by table rating; Engulf, Flame Aura, Guard, "
            "Materialization, Spell Flamethrower), hiding in an alcove near the top behind a masking "
            "ward (MITS p.89) -- only an initiate deliberately assensing for masked auras will find "
            "it. It engulfs the whole party on entry and sets the garbage alight. RIGGER SECURITY: "
            "cameras on levels 1-3, level 4 blacked out; all doors on rating 6 maglocks with card "
            "readers and every guard carrying a keycard; bypassing any device is base 10 minutes "
            "divided by successes. Ralphie rolls 5 dice for Perception at TN 4 for a door "
            "opened/closed, 6+successes for successful maglock tampering, 2 for failed tampering, 2 "
            "for a destroyed device, 6+successes for a carefully deactivated one, 8 every 10 minutes "
            "for runners walking visibly in the halls, 3 every 20 minutes for a patrol that misses "
            "its report, 3 every 10 minutes for guards missing from posts. Alerted, he shadows them "
            "on camera, locks the facility down (all doors and the elevator, overridable by him), "
            "briefs the inbound containment team on numbers, abilities and tactics, and sends "
            "Bishop. SUBLEVEL 1: environmental units, fuel, generators, guard quarters, storage -- "
            "a typical military installation. SUBLEVEL 2: employee quarters, offices and recreation, "
            "and the likeliest place the personnel are confined. SUBLEVEL 3: science labs, "
            "fabrication, security operations (Ralphie plus four guards) and the data centre "
            "(Schmitty asleep at his desk). Every workstation's memory was uploaded to the data "
            "centre, forwarded to the Ares Arms main database, wiped, and the whole system shut "
            "down -- a player decker will find nothing at all to deck. The labs engineer improved "
            "insecticides for killing bug spirits: Biotech (4) identifies toxin work, and Chemistry "
            "(4), Biology (6) or Biotech (4) at 20 minutes divided by successes identifies advanced "
            "insecticide."
        ),
    },
    {
        "name": "Ares Arms Redmond Facility Sublevel Four",
        "location_type": "research lab",
        "city": "Seattle",
        "district": "Redmond Barrens (off Redmond Fall City Road)",
        "security_level": "Corporate Extraterritorial",
        "controlling_org": "Ares Arms",
        "summary": "The clean level: a Force 15 ward, warded stasis tanks of live ant spirits, the mages' quarters, and Kat's body.",
        "description": (
            "Sublevel four looks like a maximum security prison with ancient Egyptian inscriptions "
            "written on the walls -- to some eyes, like the inside of a modern Egyptian pyramid. It "
            "is the clean level, and it is where everything that matters is kept: a decontamination "
            "suite, the mages' quarters, the main testing labs and the specimen storage rooms. "
            "Stepping off the elevator puts a visitor in a large locker room with men's and "
            "women's showers off it and a dozen human-sized yellow Chemsuits on the racks, ending "
            "in a small air lock into the decontamination area -- and that air lock is where the "
            "Force 15 ward begins. There are no security cameras anywhere on this level. Tonight "
            "there is fresh blood on the floor from a guard wounded hours ago, and behind yellow "
            "caution tape at the end of the level a sealed testing lab nobody has been back into."
        ),
        "notes": (
            "THE WARD: unlike the others, the Force 15 barrier wraps the roof, sides AND floor of "
            "the entire level, with the hieroglyphic components inscribed on the frosted glass "
            "floor rather than the walls and doors -- so a mage passes it only by winning astral "
            "combat or by shutting down every focus, every sustained spell and all other active "
            "magic. SPECIMEN STORAGE, room one: three true-form ant spirits held in large "
            "cylindrical stasis chambers of bluish liquid, each individually Force 15 warded, made "
            "of barrier rating 10 armoured glass with the Egyptian writing on the sides forming the "
            "ward. The module gives no stats on purpose -- no runner should be foolish enough to "
            "release them -- and the astral plane shows nothing through the ward. They appear as "
            "human-sized ants and are a horrific sight. SPECIMEN STORAGE, room two: a maximum "
            "security cell that held six flesh-form ant spirits; five were shot dead by guards "
            "during the breach and their remains are so damaged that identifying them takes a Magic "
            "Threat (8) test. The sixth got loose (see John). MAGE QUARTERS: Kat's and Bishop's. "
            "Kat's room is pristine and utilitarian, broken only by a few leather-bound books on a "
            "dresser; the top drawer holds an engraved oaken jewellery box 15 centimetres square "
            "containing several sets of diamond earrings, a jade earring-and-necklace set, and a "
            "friendship bracelet with some of Stella's hair woven into it -- none of it magical, "
            "worth 2,000 nuyen before fencing, and priceless to Stella. MAIN TESTING LAB: a "
            "security alcove outside serves as a weapons store and still holds four Ares ELD-AR "
            "assault rifles loaded with insecticide rounds (Biotech (4) to identify the "
            "ammunition); the rest were taken by the guards. The lab door is shut with yellow "
            "caution tape and the room is sealed pending the containment team. Inside, Kat and "
            "several guards lie in pools of blood against the white of their torn containment "
            "suits, some of the bodies ripped in half and bitten apart. Kat's cell phone is on the "
            "floor beside her, still where she dropped it."
        ),
    },
    {
        "name": "Ares Arms Everett Armor Plating Plant",
        "location_type": "corporate facility",
        "city": "Seattle",
        "district": "Everett",
        "security_level": "Corporate High Security",
        "controlling_org": "Ares Arms Seattle Division",
        "summary": "The Seattle division's manufacturing site, producing armor plating for all Ares drones and vehicles.",
        "description": (
            "The manufacturing leg of Ares Arms' Seattle division: a facility in Everett that makes "
            "the various armor plating fitted to all of the corporation's drones and vehicles. It "
            "is one of the four locations named on the division's own dossier card -- offices "
            "throughout Seattle including the main Ares Macrotechnology enclave for administration, "
            "Fort Lewis for operations and divisional headquarters, Everett for manufacturing, and "
            "the Puyallup and Redmond Barrens for testing."
        ),
        "notes": (
            "Not visited in this adventure; it exists on the enemy card as part of the division's "
            "footprint, and it is the obvious place a GM sends a team that has just made an enemy "
            "of Ares Arms and wants to hit back at something -- or the obvious source for anyone "
            "shopping for vehicle plating on the grey market. Remember the division's standing "
            "capability: standby teams respond by helicopter or tilt-rotor to any other Ares Arms "
            "facility within ten minutes."
        ),
    },
    {
        "name": "Ares Macrotechnology Seattle Enclave",
        "location_type": "corporate megastructure",
        "city": "Seattle",
        "district": "Seattle metroplex",
        "security_level": "Corporate Extraterritorial",
        "controlling_org": "Ares Macrotechnology",
        "summary": "Ares' main Seattle enclave, housing the administrative offices of the Ares Arms division among much else.",
        "description": (
            "The main Ares Macrotechnology enclave in Seattle, named on the Ares Arms division "
            "dossier as the site of the division's administrative offices. Everything about the "
            "corporation's public face in the metroplex runs through here, while the operational "
            "side of Ares Arms lives at Fort Lewis, the manufacturing in Everett, and the testing "
            "-- officially -- out in the Puyallup and Redmond Barrens."
        ),
        "notes": (
            "Background rather than a location the runners visit. Its value to a GM is the split it "
            "documents: the administrative record of Ares Arms sits in the enclave, the operational "
            "record at Fort Lewis, and the Redmond research facility appears in neither if anyone "
            "has done their job properly. A team that survives this run holding data about a black "
            "bug-spirit laboratory has something the enclave would very much like to know it has."
        ),
    },
]

NPCS = [
    {
        "name": "Kat Austing",
        "role": "Initiated freelance hermetic mage, head of magical security at the Redmond facility; already dead when the run begins",
        "archetype": "Mage",
        "title": "Lead mage and head of magical security, Ares Arms Redmond research facility",
        "race": "Human",
        "gender": "Female",
        "nationality": "Egyptian",
        "organization": "Ares Arms",
        "connection": 4,
        "description": (
            "A powerful initiate who works entirely for money -- 'As a follower of the hermetic "
            "tradition, I cared only about one thing: money; and Ares was offering plenty of it. "
            "Classified jobs paid even more, and this one was just through the roof.' Calm and "
            "unflappable under a strapped-down two-meter carpenter ant, dismissive of the mundane "
            "scientists working with her, indulgent and a little exasperated with the girlfriend "
            "who keeps calling: 'Stella, I thought I told you to call me only in an emergency! You "
            "don't realize how much trouble I could get into by talking to you right now!' She was "
            "not supposed to have a cell phone in the lab at all. Corporate legwork remembers her "
            "as a mage who does corporate freelance work, and thinks she is Egyptian."
        ),
        "background": (
            "Kat contracts herself to the highest bidder. A friend inside Ares Arms told her the "
            "corporation needed a high-level mage for a 'project', and she used that friend's "
            "influence to win the contract as lead mage -- responsible for maintaining magical "
            "security for the facility and for ensuring containment of the test specimens. She "
            "built the ward system on Egyptian hieroglyphics etched into frosted glass, permanently "
            "bound a fire elemental with karma to guard the emergency stairwell and hid it behind a "
            "masking ward, and lived on sublevel four in a pristine, utilitarian room whose only "
            "personal contents were a few leather-bound books and a jewellery box holding a "
            "friendship bracelet woven with Stella Smith's hair. Legwork at 4+ successes: 'I've "
            "been told she is very close with a woman named Stella Smith... very close if ya know "
            "what I mean.'"
        ),
        "notes": (
            "No stat block, because she is a corpse before the first scene. What happened: during a "
            "dissection she cleared two mundane scientists out of the lab on the excuse of "
            "preparing a binding ritual, and was mid-chant when the strapped ant spirit cut through "
            "its Kevlar bonds. The scientists burst back in, she released her spell early and "
            "missed, the bolt struck the transom above the door, and the glyph above it flickered "
            "and died as the creature tore her apart. She wounded it badly enough that Bishop could "
            "finish it. Her death is what cripples the facility's magical defences for the few "
            "hours this adventure occupies. The body lies in the sealed main testing lab on "
            "sublevel four behind yellow caution tape with several guards, in torn white "
            "containment suits, some of them ripped in half; her cell phone is on the floor beside "
            "her. Team Karma: 1 for discovering what happened to her, 1 for bringing the body back. "
            "Manny's brief is explicit -- if the worst has happened, retrieve as much of the body "
            "as possible for processing the insurance claims."
        ),
        "contact_skills": ["Wards, containment and spirit binding", "Freelance corporate magical security"],
    },
    {
        "name": "Stella Smith",
        "role": "Dog shaman, Kat Austing's girlfriend, and the client -- she heard the whole thing over an open line",
        "archetype": "Shaman",
        "title": "Dog shaman; Manny's friend of many years",
        "race": "Human",
        "gender": "Female",
        "connection": 3,
        "description": (
            "Frantic, warm, and utterly without corporate instincts -- 'That's a Dog shaman for "
            "you, always trying to be one big happy family.' She never understood why Kat could not "
            "talk about her job, or the concept of classified projects, or why people need to hide "
            "things, and she calls to check up on her partner far more often than security allows. "
            "On the telecom to Manny she goes straight into a single unpunctuated sentence: 'Manny "
            "its Stella I don't know what's happened but something terrible has happened to my "
            "friend Kat I just know it I just know it...' She calms the moment somebody competent "
            "takes charge."
        ),
        "background": (
            "Stella has known the fixer Manny for many years and turned to him without hesitation. "
            "She was on the phone with Kat when the containment breach began, heard the alien "
            "shrieks and Kat's shouting and then nothing at all -- and had the presence of mind, in "
            "the middle of that, to keep the line open. She does not know where Kat works or for "
            "whom; only that Kat was contracted by someone for a project a few months ago and that "
            "it was classified. She is paying Manny whatever it takes."
        ),
        "notes": (
            "No stat block; she never appears on screen after the opening fiction, and the runners "
            "deal with Manny rather than with her. Her open line is the entire premise: Manny put "
            "one of his star deckers on the signal and got GPS coordinates off it, then told her to "
            "hang up so nothing could trace back to her. Two things make her worth keeping as a "
            "row. First, the friendship bracelet woven with her hair in Kat's jewellery box is "
            "described as priceless to her, which gives a team an option other than fencing it. "
            "Second, whoever brings Kat's body home has to tell her, and the module leaves that "
            "scene entirely to the table."
        ),
        "contact_skills": ["Dog shamanic tradition", "Seattle magical community gossip"],
    },
    {
        "name": "Bishop",
        "role": "Troll combat mage and vampire wannabe; inherits magical security when Kat dies and is sent to kill the team",
        "archetype": "Combat Mage",
        "title": "Combat mage, Ares Arms Redmond research facility; acting head of magical security",
        "race": "Troll",
        "gender": "Male",
        "organization": "Ares Arms",
        "connection": 4,
        "description": (
            "A shadow up ahead in the darkness, a large hulking figure with some sort of cape, gone "
            "when you look again -- and then a sound behind you, and a huge caped figure standing "
            "over you, long sharp pointed teeth catching the emergency lights as a pale-faced troll "
            "swoops down. Many people at the facility believe Bishop is a vampire, and he has gone "
            "to considerable trouble to encourage them: cosmetic surgery to alter his features, "
            "gothic armour and clothing tailored for the part, the manner and the voice to match. "
            "People in the know realize he is obviously nothing of the kind. He is a huge troll "
            "spellcaster with a vampire fixation, and he has been spending the lockdown meditating "
            "in his private study."
        ),
        "background": (
            "Kat and Bishop were the two mages responsible for astral security at the facility, "
            "with the work split cleanly: her expertise was spirits and wards, his is combat "
            "spells. With Kat dead he is in charge of magical security, and he is one of the very "
            "few personnel permitted out of lockdown. It was Bishop who finished off the bug spirit "
            "after Kat had mortally wounded it."
        ),
        "notes": (
            "Scaled by table. GREEN/STREETWISE: B7(8) Q5x3 S6 C4 I4 W6, Reaction 4, Magic 8, Init "
            "4+4D6, grade 2 initiate (Quickening, Masking), Combat Pool 7, Magic Pool 6; Unarmed 7, "
            "Sorcery 6, Conjuring 6, Intimidation 4, Pistols 3, Etiquette 2 (Corporate 4). "
            "PROFESSIONAL/VETERAN: I5 W7, Magic 10, Init 6+4D6, grade 4 (adds Possessing, "
            "Reflecting), Sorcery 8, Conjuring 7. ELITE/PRIME: Q6x3 I6 W8, Reaction 6, Magic 12, "
            "Init 9+4D6, grade 6 (adds Divining, Shielding), Sorcery 9, Conjuring 8. Spells across "
            "all versions: Decrease Charisma, Manabolt, Death Touch, Fashion, Foreboding, Improved "
            "Invisibility, Increase Reflexes +3, Increase Reaction at the higher grades, plus one "
            "GM's choice. Always a Force 4 water elemental and a Force 4 air elemental. Gear: "
            "gothic secure jacket 5/3, form-fitting body armour (shirt, half-body or full-body by "
            "level), Ares Predator II (9M), and quickened Foreboding (plus quickened Increase "
            "Reflexes and Increase Reaction at the higher grades). PLAY: he is sent the moment the "
            "rigger alerts, arrives late in the adventure and preferably on or near sublevel four, "
            "and uses fear and surprise -- pick off a lone runner if the party splits, and consider "
            "skipping the dice for effect, as the module suggests: a wisp of smoke and he is gone, "
            "or he simply appears out of nowhere with the jump on the team. The fight should be "
            "tough but survivable unless the team has split up."
        ),
    },
    {
        "name": "Ralphie",
        "role": "Dwarf security rigger who runs the facility's whole surveillance and lockdown system from sublevel three",
        "archetype": "Rigger",
        "title": "Security rigger, Ares Arms Redmond research facility (Ralph Schroeder)",
        "race": "Dwarf",
        "gender": "Male",
        "organization": "Ares Arms",
        "connection": 3,
        "description": (
            "Ralph Schroeder, jacked into the security console in the operations room on sublevel "
            "three with four guards around him, in full control of every camera, door and maglock "
            "in the building except on the one level that has no cameras at all. He is not a "
            "fighter and he is not a fanatic -- he is a rigger doing a night shift during a "
            "lockdown, and his orders if intruders appear are simply to monitor them and relay what "
            "he sees to the containment team."
        ),
        "background": (
            "Ralphie does not know what the facility actually researches. Sublevel four has no "
            "security cameras, so he has no idea what happens down there; he knows the layout, the "
            "procedures, the guard postings and the fact that a containment team is inbound from "
            "Fort Lewis, and that is the whole of it."
        ),
        "notes": (
            "Stats: B4 Q6 S3 C2 I5 W6, Reaction 5, Init 5+1D6 (9+3D6 rigged), Combat Pool 8, "
            "Control Pool 9. Computer 3, Electronics 3 (Security Systems 6), Electronics B/R 5, "
            "Etiquette 3 (Corporate 5), Pistols 5, Gunnery 3, Security Procedures 4. Cyber: vehicle "
            "control rig 2, headware radio 6, subvocal microphone, datajack. Ares Predator II (9M), "
            "secure jacket. He is the single most important obstacle in the facility: his 5-dice "
            "Perception rolls against the table of security-event target numbers are what turn a "
            "quiet infiltration loud, and once he is alerted the facility locks down, the "
            "containment team is briefed on the team's numbers, abilities and tactics, and Bishop "
            "is sent. Subdue him and a player rigger can simply jack in and take the entire system. "
            "Interrogation or Intimidation (SR3 p.93) gets the security layout, general facility "
            "information and the news about the inbound containment team -- but nothing about "
            "sublevel four, because he has never seen it."
        ),
        "contact_skills": ["Security systems and rigged surveillance", "Corporate security procedures"],
    },
    {
        "name": "Schmitty",
        "role": "Facility decker asleep at his desk in a data centre that has already been wiped and shut down",
        "archetype": "Decker",
        "title": "Facility decker, Ares Arms Redmond research facility (David Schmidt)",
        "race": "Human",
        "gender": "Male",
        "organization": "Ares Arms",
        "connection": 2,
        "description": (
            "David Schmidt, found asleep at his work desk in a cluttered data centre in the middle "
            "of a containment lockdown. He spends most of his time writing science fiction stories "
            "and looking for ways to get out of doing real work at the facility, and it shows in "
            "his stats: Body 1, Quickness 2, and a Computer skill of 5 keeping him employed."
        ),
        "background": (
            "Schmitty knows very little about the workings of the facility, and most of what he "
            "will offer is speculation -- the same speculation circulating among all the support "
            "staff about alien autopsies, genetic experimentation and new military bioware. Since "
            "the breach, every workstation's memory in the building has been uploaded to his data "
            "centre, forwarded to the Ares Arms main database, wiped at source, and the whole "
            "system shut down."
        ),
        "notes": (
            "Stats: B1 Q2 S2 C2 I5 W4, Reaction 3, Init 3+1D6, Combat Pool 5. Computer 5, Computer "
            "B/R 4, Etiquette 2. Cyber: datajack, 300 Mp headware memory. Decking statistics "
            "deliberately not provided. THE POINT OF HIM: a player decker who tries to work the "
            "facility from inside immediately discovers that the system is shut down and there is "
            "nothing to be gained by decking at all -- this is a physical-infiltration adventure "
            "and the module closes the Matrix door on purpose. Interrogation or Intimidation gets "
            "everything he has, which is very little. THE PRIZE: his cyberdeck is built into the "
            "computer mainframe and is the equivalent of a Novatech Hyperdeck-6. The mainframe is "
            "too big to move; extracting the deck is a Computer B/R (8) test at a base time of one "
            "hour divided by successes, and a failed test trips an antitheft device that destroys "
            "the deck beyond repair. Note the containment clock while deciding whether that is "
            "worth an hour."
        ),
        "contact_skills": ["Corporate data centre operations", "Science fiction, at length"],
    },
    {
        "name": "John (Flesh Form Ant Spirit)",
        "role": "Escaped flesh-form worker ant spirit posing as a tortured human test subject to get carried out of the facility",
        "archetype": "Insect Spirit",
        "title": "Test subject \"John\"; flesh form worker ant spirit, Force 3",
        "race": "Flesh form ant spirit",
        "gender": "Male",
        "connection": 1,
        "description": (
            "'Help me.' A man dragging himself along the ground in obvious pain, reaching out with "
            "words barely audible, arms falling to the ground as he looks helplessly up at the "
            "runners. Examination shows scars from recent operations all over him. He tells them he "
            "is a construction worker who lives with his family in Redmond, abducted several months "
            "ago and subjected to human genetic experimentation by the doctors of this facility. "
            "Every word of it is a lie. Astral perception shows a twisted, mangled flesh form ant "
            "spirit; caught out, he pleads ignorance of being an insect spirit at all, and attacked "
            "he begs helplessly for his life to whichever player looks most sympathetic."
        ),
        "background": (
            "One of six flesh form ant spirits held in a maximum security cell on sublevel four as "
            "test subjects for the insecticide program; he has been operated on repeatedly over "
            "several months. During the containment breach five of his fellows were shot dead by "
            "guards and he used the confusion to get off an operating table. He has been hiding on "
            "the fourth floor ever since, and he sees the runners as his way out."
        ),
        "notes": (
            "Stats: Force 3, B1 Q2 S2 C3 I3 W3, Essence (3)Z, Reaction 2, Init 2+1D6, Combat Pool "
            "4, Karma Pool 2. Powers: Skill (Carpentry B/R: Construction Worker 3) -- the "
            "construction-worker cover story is a stolen skill, not an invention. Biotech (5) "
            "examination: 0 successes finds multiple operation scars all over his body; 1 shows a "
            "pattern of operations dating back several months; 2+ finds a strange patch of rigid "
            "hair on a discoloured, hard piece of black skin under his upper arm. He cannot walk "
            "and must be carried. He is dual natured and cannot normally pass the Force 15 barrier "
            "around sublevel four -- carried through, treat him as being pressed through the "
            "barrier (MITS p.83): he passes, but is knocked unconscious in the process, which is "
            "the last clear warning a team gets. The Karma award for helping John escape is MINUS "
            "one for the team. He is the module's moral trap, and he is very good at it."
        ),
    },
    {
        "name": "Captain Kenneth Brooks",
        "role": "Commander of the Ares Arms Special Magic Corps containment team; his arrival ends the adventure",
        "archetype": "Corporate Security Officer",
        "title": "Captain, Ares Arms Special Magic Corps containment team",
        "race": "Human",
        "gender": "Male",
        "organization": "Ares Arms Special Magic Corps",
        "connection": 4,
        "description": (
            "A voice over the facility loudspeakers, and nothing else: 'This is captain Kenneth "
            "Brooks of the Ares Arms Special Magic corps containment team. I am assuming control as "
            "chief security officer at this facility. My team is being dispatched throughout the "
            "facility and will take over for security and containment. Please remain diligent at "
            "your post until relieved by the containment team.' Calm, procedural, and entirely "
            "unhurried, because he has just landed ten five-man teams on top of whoever is inside."
        ),
        "background": (
            "Brooks commands the containment element assembled at Fort Lewis the moment the breach "
            "was reported and flown in aboard Ares TR-55 VTOL transports -- ten teams plus his own "
            "command group, a rigger, a decker and a team of medical doctors, all in full security "
            "armour with environmental seals. If Ralphie has already spotted the runners, Brooks "
            "arrives knowing their numbers, their abilities and their tactics."
        ),
        "notes": (
            "No personal stat block; he functions as a clock rather than an opponent. The Game "
            "Over, Man! scene fires automatically when 45 minutes of the play slot remain, no "
            "matter where the runners are or what they are doing. His teams spread out and secure "
            "each area in turn; engaging one brings two more after two rounds of combat. The module "
            "is explicit that this is not a combat scene and that the outcome is fixed if the team "
            "insists: every player automatically takes a Deadly wound, loses all weapons and all "
            "magical, security- and military-grade equipment, mages roll for magic loss, and "
            "everyone pays the living and healing costs for the recovery. A team that has found a "
            "quick way out -- the emergency stairwell most obviously -- should have no problem "
            "leaving before he reaches them."
        ),
    },
    {
        "name": "Sergeant Colby",
        "role": "Facility guard twenty minutes from the end of his shift when the containment alarm went off",
        "archetype": "Corporate Security Guard",
        "title": "Sergeant, facility security, Ares Arms Redmond research facility",
        "race": "Human",
        "gender": "Male",
        "organization": "Ares Arms",
        "connection": 2,
        "description": (
            "A working sergeant with twenty minutes left on a Level Four patrol shift and a "
            "thoroughly reasonable attitude to it: 'Why does this drek have to always happen when "
            "I'm about ready to get relieved??' He and his corporal are cleared to walk the hallway "
            "and not to enter the labs unless an alarm is triggered, which suits him fine. Like "
            "everyone else on the guard force he has heard the theories -- mutants exposed to the "
            "Glow, space aliens recovered from the crashed suborbital, stranger tales of things "
            "that go bump in the night -- and he has never wanted to know."
        ),
        "background": (
            "Colby and Corporal Rachovsky were making the security rounds on Level Four when the "
            "claxons went and the tannoy announced a breach in Laboratory B: protocol CHARLIE, all "
            "security teams to duty stations, load chemical rounds. They checked their magazines "
            "for the special ammunition -- neither of them knows what the chemicals are, only that "
            "lead bullets are not to be used in the facility -- rode the elevator down and walked "
            "into the fight. They emptied their clips on full automatic into a two-meter carpenter "
            "ant covered in white insecticide foam and, with luck on their side, put it down. A "
            "facility mage then ordered the lockdown and left Colby and his partner to oversee it "
            "until the professionals arrived."
        ),
        "notes": (
            "Facility guard stats: B3 Q4 S3 C2 I4 W4, Reaction 4, Init 4+2D6, Combat Pool 6. "
            "Assault Rifle 5, Pistols 4, Edged Weapons 3, Small Unit Tactics 2, Etiquette 3 "
            "(Corporate 5). Cyber: headware radio 2, subvocal microphone, boosted reflexes 1, "
            "smartlink. Light security armor with helmet, Ares Delta SMG (7M, treat as an Ingram), "
            "Ares Predator II (9M), Ares Combat Knife (3M). Chemical rounds are the standing load "
            "inside the facility. THE INTENTION: the module states that the runners should "
            "preferably never meet ANY facility personnel -- the emptiness is the horror. Colby is "
            "written into the opening fiction to establish what the guards know, what they carry, "
            "and how frightened they are, and he is the natural face to put on the lockdown if a GM "
            "decides the team must meet somebody. Guards who fail to report in give Ralphie a "
            "Perception roll every 20 minutes."
        ),
    },
    {
        "name": "Corporal Rachovsky",
        "role": "Colby's partner on the Level Four rounds; helped put down the escaped bug spirit",
        "archetype": "Corporate Security Guard",
        "title": "Corporal, facility security, Ares Arms Redmond research facility",
        "race": "Human",
        "gender": "Male",
        "organization": "Ares Arms",
        "connection": 2,
        "description": (
            "The junior half of the Level Four patrol, who answers his sergeant's 'What the hell is "
            "going on?' with a shrug because that is genuinely all he has. He checks his magazine "
            "for the special chemical rounds without being told, screams along with his sergeant "
            "when the ant shrieks at them, and empties his clip into it on full automatic in a "
            "matter of seconds."
        ),
        "background": (
            "Tasked with the security rounds on Level Four -- where the main labs are -- alongside "
            "Sergeant Colby, cleared for the hallway only and not for the labs themselves unless an "
            "alarm sounds. Between the two of them and their standing orders, they represent "
            "exactly how much the ordinary guard force knows about what Ares Arms is doing three "
            "levels beneath its own guard quarters, which is nothing at all."
        ),
        "notes": (
            "Same facility guard stats as Sergeant Colby: B3 Q4 S3 C2 I4 W4, Init 4+2D6, Combat "
            "Pool 6; Assault Rifle 5, Pistols 4, Edged Weapons 3, Small Unit Tactics 2; headware "
            "radio 2, subvocal mic, boosted reflexes 1, smartlink; light security armor with "
            "helmet, Ares Delta SMG, Ares Predator II, Ares Combat Knife, chemical rounds loaded. "
            "Like Colby he is written for the opening fiction and should ideally never be met. If "
            "the GM does need a guard on screen, the pair are the obvious choice -- they have "
            "already seen a bug spirit tear a scientist off a wall tonight, and they will treat any "
            "unauthorized person on the lower levels as part of the same problem."
        ),
    },
]

ORG_UPDATES = {
    "Ares Macrotechnology": {
        "notes_append": (
            "SRM 00-05 A Dark and Stormy Night: Ares Arms, the corporation's military systems "
            "subdivision, set up a black research and development facility in the Redmond Barrens "
            "several months ago -- four sublevels in the old parking garage beneath a ruined office "
            "block off Redmond Fall City Road, close to Glow City -- to bioengineer a toxin more "
            "effective against insect spirits, using live captive true-form and flesh-form ant "
            "spirits as test subjects. Security is built for containment rather than intrusion: "
            "chemical rounds instead of lead, insecticide-loaded Ares ELD-AR rifles, spray "
            "dispensers, Chemsuits, protocol CHARLIE, and a Special Magic Corps containment team on "
            "call at Fort Lewis that arrives by TR-55 VTOL. Magical security ran on a ward system "
            "of Egyptian hieroglyphics etched into frosted glass, built by the freelance initiate "
            "Kat Austing -- Force 4 on sublevel 2, Force 8 on 3, Force 15 wrapping the whole of "
            "sublevel 4 including its floor, and Force 6 on the elevator shaft, plus a permanently "
            "bound fire elemental hidden behind a masking ward in the emergency stairwell. Her "
            "death in a containment breach leaves those defences crippled for a few hours. The "
            "Seattle Ares Arms division's own dossier lists its footprint: administrative offices "
            "in the main Ares Macrotechnology enclave, operations and divisional headquarters at "
            "Fort Lewis, manufacturing in Everett (armor plating for all drones and vehicles), and "
            "testing in the Puyallup and Redmond Barrens."
        ),
    },
    "The Ant Hive (Glow City)": {
        "notes_append": (
            "SRM 00-05 A Dark and Stormy Night: by 2064 Ares Arms is running a bug-spirit research "
            "facility a short distance from Glow City, in the Redmond Barrens off Redmond Fall City "
            "Road, whose entire purpose is bioengineering a more effective insecticide for killing "
            "insect spirits. It holds live specimens: three true-form ant spirits in individually "
            "Force 15 warded stasis chambers of bluish liquid behind barrier rating 10 armoured "
            "glass, and a maximum security cell that held six flesh-form ant spirits for "
            "vivisection. The module gives no stats for the true forms on the explicit grounds that "
            "no runner should be foolish enough to release them. Where the specimens came from is "
            "never stated -- but the nearest hive is next door."
        ),
    },
    "The Ant Hive (Puyallup)": {
        "notes_append": (
            "SRM 00-05 A Dark and Stormy Night: Ares Arms' Redmond facility is developing an "
            "advanced insecticide specifically for killing bug spirits, and keeps captive ant "
            "spirits of both true and flesh form for the testing -- the first corporate "
            "anti-insect-spirit weapons program in the metroplex the runners are likely to have "
            "seen from the inside. The Ares Arms Special Magic Corps containment teams carry Ares "
            "Alpha rifles switching between EX explosive rounds and capsule rounds loaded with "
            "insecticide, and their people carry Bug Spirits as a knowledge skill at ratings of 4 "
            "to 6."
        ),
    },
}

LOC_UPDATES = {
    "Glow City (Redmond Barrens)": {
        "notes_append": (
            "SRM 00-05 A Dark and Stormy Night: Ares Arms' hidden bug-spirit research facility sits "
            "just off Redmond Fall City Road, 'dangerously close to Glow City', and the module "
            "tells the GM to play up the fear -- let the players speculate freely about radiation "
            "poisoning on the drive in. The Barrens around it are ruins from the riots of the early "
            "2000s, collapsed structures now serving as makeshift homes for people eking out an "
            "existence there. On the night of the run a storm has driven the gangers and squatters "
            "indoors, the acid rain is heavy enough to cost an exposed character a Light stun wound "
            "on a failed Body (3) test, and the pollution raises a Background Count of 1 outdoors. "
            "The facility guards trade rumors about mutants exposed to the Glow, space aliens "
            "recovered from the crashed suborbital, and stranger things."
        ),
    },
    "Fort Lewis": {
        "notes_append": (
            "SRM 00-05 A Dark and Stormy Night: Fort Lewis holds the operations arm and the "
            "divisional headquarters of Ares Arms, Seattle Division, which works out of and "
            "supports the base. When the Redmond research facility suffered a containment breach, "
            "the Special Magic Corps containment team was assembled here and flown in aboard Ares "
            "TR-55 VTOL transports -- ten five-man teams plus a captain, rigger, decker and medical "
            "doctors, arriving a few hours after the alarm. Ares Arms standby teams can reach any "
            "other Ares Arms facility by helicopter or tilt-rotor within ten minutes."
        ),
    },
}

NPC_UPDATES = {
    "Manny": {
        "background_append": (
            "SRM 00-05 A Dark and Stormy Night: Manny has known the Dog shaman Stella Smith for "
            "many years, and she turns to him without hesitation when she hears her partner "
            "attacked over an open phone line. He talks her down -- 'Whoa, calm down Stella, calm "
            "down. OK, Manny is here to help' -- while working the telecom with his other hand: he "
            "pulls up one of his star deckers in a second window, relays her cell number and a "
            "request to trace it, gets GPS coordinates within moments, and then tells her to hang "
            "up the open line so nothing can trace back to her. The module's own summary of him: "
            "'The fixer picked up on the second ring... Manny used his many years of experience to "
            "quickly assess the situation.' He knows exactly which console cowboy to depend on and "
            "how fast to move."
        ),
        "notes_append": (
            "SRM 00-05 A Dark and Stormy Night: Manny runs this job personally and hires the team "
            "out of bed at 2:00 AM in a hail storm. He calls each runner, gives them the basics, "
            "patches everyone who is interested into a conference call, briefs them, pays 2,000 "
            "nuyen each by secure computer transaction on the spot, sends each of them a small data "
            "file with Kat's last known GPS coordinates and a photograph, and hangs up -- leaving "
            "the team on the call to decide what to do. Terms: 2,000 nuyen each to find out what "
            "happened to Kat Austing, 3,000 more each if they bring her home alive, and if the "
            "worst has happened, retrieve as much of the body as possible for processing the "
            "insurance claims. He expects to hear from them in an hour or so. He will also buy the "
            "team's data on the facility, at 10 percent of its market value (which runs from 10,000 "
            "nuyen at Green to 250,000 at Prime Runner) -- which is a much better deal than it "
            "sounds, because a team that fences the data itself is ambushed at the meet by five "
            "Ares fast response teams."
        ),
        "contact_skills_add": ["Deckers for phone and signal tracing", "Rapid team assembly at any hour"],
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
There is no host to run in this adventure, and that is a design decision rather than an omission.

### Ares Arms Redmond research facility -- data centre (sublevel 3)

Following the containment breach, every workstation memory in the facility was uploaded to the
data centre, forwarded from there to the Ares Arms main corporate database, wiped at source, and
the entire system shut down. A player decker who tries to work the facility from inside
immediately establishes that the system is dead and that no information whatsoever can be gained
by decking. The adventure is a physical infiltration and the module closes the Matrix door on
purpose.

What is still in the data centre is hardware. The facility decker Schmitty uses a cyberdeck built
directly into the computer mainframe, equivalent to a **Novatech Hyperdeck-6**. The mainframe
itself is far too large to remove. Extracting the deck is a Computer B/R (8) test with a base time
of one hour divided by the successes achieved; a failed test trips an antitheft device that
destroys the cyberdeck beyond repair. Weigh that hour against the containment team's arrival.

### Facility security system (not a host)

The security network is rigger-controlled rather than decked: Ralphie sits jacked into it in the
security operations room on sublevel 3 with four guards. Cameras cover levels 1 to 3; **level 4 is
blacked out entirely**, which is why nobody in the security chain knows what is on it. All doors
carry rating 6 maglocks with card readers and every guard holds a keycard; every security rating
in the building is 6, and bypassing any device takes a base 10 minutes divided by successes.
Subdue Ralphie and a player rigger can jack in and take full control of the system without further
tests.

### Magical "security architecture" -- the real network here

| Zone | Ward |
| --- | --- |
| Elevator and elevator shaft | Force 6 |
| Sublevel 1 | None |
| Sublevel 2 | Force 4 |
| Sublevel 3 | Force 8 |
| Sublevel 4 (roof, sides and floor) | Force 15 |
| Each true-form specimen stasis chamber | Force 15, individually |
| Stairwell alcove (hiding the bound fire elemental) | Masking ward, MITS p.89 |

Components are Egyptian hieroglyphics inscribed on frosted glass panes (barrier rating 8) that
double as the facility's doors and inner walls, so a magician's only routes past a ward are astral
combat or physically opening the door. The sublevel 4 ward is the exception: its glyphs are on the
frosted glass FLOOR, so it can also be crossed by shutting down every focus, sustained spell and
other active magic. The elevator carries a Force 7 expendable anchor focus (MITS p.45) holding
Detect Specific Facility Passkey Badge (Force 3) linked to Stun Ball (Force 4) -- 4M on 7 dice
against everyone in the car the moment the doors shut on anyone without a passkey.
"""

NOT_BUILT = """
- **The bug spirit that killed Kat Austing** -- unnamed, and already dead when the adventure
  starts, finished by Bishop after Kat wounded it. Described only in the opening fiction as a
  two-meter carpenter ant with black mandibles.
- **The three true-form ant spirits** in the sublevel 4 stasis chambers. The module deliberately
  gives no statistics, on the grounds that no runner should be foolish enough to release them; kept
  in the sublevel 4 location notes.
- **The five flesh-form ant spirits** shot dead by guards during the breach, whose remains take a
  Magic Threat (8) test to identify.
- **The greater-form fire elemental** Kat permanently bound with karma to the emergency stairwell
  (Force 4, 7 or 10 by table rating), hidden behind a masking ward -- a bound spirit, kept in the
  facility notes.
- **The facility support personnel** -- eight support staff, four administrators and clerks and six
  technicians (B2 Q2 S2 C2 I3 W3, Init 2+1D6, Combat 4, Karma 2), who can describe the general
  layout, headcount and the function of each sublevel but do not know the true nature of the
  research and speculate about alien autopsies, genetic experimentation and military bioware.
- **The five adept scientist-engineers** (B3 Q3 S3 C5 I5 W7, Combat 7, Karma 3; Astral Perception,
  Iron Will 4, Magic Resistance 2; +6 dice against magical interrogation and +4 against standard;
  Biotech 5, B/R Biotech 6, various sciences 6) who DO know what the facility does and are very
  valuable to Ares -- killing or injuring one greatly angers the corporation. They know Kat was
  last seen fighting a bug spirit on sublevel 4 but not whether she is alive.
- **The rest of the facility guard force** -- the stat block is carried on Sergeant Colby's row.
  The module's strong preference is that the runners meet no facility personnel at all.
- **The Special Magic Corps rank and file** -- ten five-man teams plus a rigger, a decker and
  medical doctors; stat blocks folded into the Ares Arms Special Magic Corps org row.
- **The decker Manny hires** to trace Stella's open cell line and produce Kat's GPS coordinates --
  one of his star deckers, unnamed, and a standing hook.
- **The friend inside Ares Arms** whose influence got Kat the contract in the first place --
  unnamed, and never followed up.
- **Ares TR-55 VTOL transports, Ares ELD-AR and Ares Alpha rifles, Ares Delta SMG, Ares Predator II
  and III, Ares Combat Knife, Novatech Hyperdeck-6, Chemsuit (6)** -- gear name-drops.
- **Protocol CHARLIE** -- the facility's containment lockdown procedure, referenced but never
  detailed.
"""

PLAY_NOTES = """
- Run this as horror, not as a raid. The module gives an unusual amount of explicit staging advice
  and it is all worth following: play up the storm, the acid rain, the Background Count outdoors,
  the generator that overloads and dies, the emergency lights that flicker and fail, and above all
  the emptiness. Every surviving employee is on lockdown somewhere the runners are not, and the
  module names the target feeling -- Resident Evil. Statistics for the facility personnel exist
  purely so the GM has them; the strong recommendation is that the runners never meet a soul.
- Do not be afraid to skip dice at dramatic moments. When Bishop casts invisibility, just say a
  wisp of smoke surrounds him and he is gone. When he attacks, assume he has the jump. Roll
  Perception for things that are not there. Give an astrally projecting mage a nosebleed. Put fresh
  blood on sublevel 4 before anyone finds a body.
- The clock is real and it is not negotiable: Game Over, Man! fires when 45 minutes of the session
  remain, wherever the runners are. Keep them moving -- if they start looting and investigating,
  drop hints about the inbound containment team. The Ares Arms Special Magic Corps is not an
  encounter; a team that fights it automatically takes a Deadly wound each, loses every weapon and
  every piece of magical, security- or military-grade gear, and pays the healing bill.
- Two ways in, and they teach different lessons. The elevator is the obvious route and is trapped
  three ways -- rating 6 retinal, passkey and passcode, a failed roll that both alerts Ralphie and
  kills the power, and a Force 7 anchored Stun Ball that fires on anyone without a facility
  passkey the instant the doors close. The hidden stairwell is quieter but holds a permanently
  bound fire elemental behind a masking ward that only a deliberately assensing initiate will find
  before it engulfs the whole party.
- Ralphie is the adventure's difficulty dial. His Perception table turns every door, every maglock
  and every visible minute in a corridor into a roll, and once he is alerted the facility locks
  down and Bishop comes hunting. Subduing him hands a rigger the whole building.
- Sublevel 4 is the payoff and the Force 15 ward is the gate. A mage must either win astral combat
  against it or drop every focus and sustained spell -- which is a genuinely frightening thing to
  ask of a magician about to walk into a room full of ant spirits.
- John is a trap and should be played completely straight. Let the sympathetic runner carry him. If
  they astrally perceive, or make the Biotech (5) and find the patch of rigid hair on hard black
  skin under his arm, they get the choice honestly. Carrying him through the barrier knocks him out
  -- the last free warning. Helping him escape costs the team a point of Karma.
- Reward the photograph, not the fight. Faces caught on camera means Ares Arms, Seattle Division as
  an Enemy at initial rating 2 (Power 5 / Motivation 0 / Knowledge 2), worsened by significant
  damage or killing and by selling the data. Masks, disguises, invisibility or beating the camera
  system means no image and no dossier at all -- and that distinction is the most useful lesson
  Season 0 teaches a new runner.
- Karma: 1 individual point for a creative infiltration; 1 team for discovering what happened to
  Kat, 1 for bringing her body back, 1 for learning what the facility is actually doing, and MINUS
  1 for helping John escape. Seven maximum with roleplaying awards.
"""
