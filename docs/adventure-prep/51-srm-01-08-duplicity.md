# SRM 01-08 Duplicity -- Adventure Prep: NPCs, Locations, Organizations, Matrix Systems

Source: SRM01-08A_Duplicity.pdf, pp. 5-19; SRM01-08B.pdf (Play Aids), pp. 2-16. Campaign order #51, in-game 2064.

Everything below is loaded into the campaign DB flagged `is_active: false` and `source_adventure: "SRM 01-08 Duplicity"` by `python scripts/adventure_ingest/run.py srm_01_08_duplicity`; flip entries active as the party meets them. Use the **Adventure** filter on the manage pages to see just this set.

## Plot synopsis

"Griffin Biotechnology has been a revolving door for shadowrunners." Two Missions have already been
through the Everett facility: **FORCEd RECON**, where runners bluffed guards and worked contacts for
an interior layout, and **The Gambler**, where a team breached it without leaving a trace and lifted
paydata off a standalone terminal. Both were organized by the fixer **Lyle Green** and paid for by
**Rose Croix**. Now news of a prototype has pushed CEO **Walter Broward** into one last daring push.
Griffin has a working system for growing custom cultured organs -- generic marker-free organs that
genetic modification can retag for a specific patient in hours instead of months, success rates
still hovering around fifteen percent -- and it is the research that bought **DocWagon**'s support.
Broward wants it. Failing that, he wants DocWagon not to have it.

The first attempt failed. **Knight Errant**, tired of the traffic through a site it is paid to hold,
took matters into its own hands: it captured the team with a SWAT squad, dosed them with Laes and
depressants, and built an artificial version of the facility to train its elite squads in
anti-runner tactics. The adventure opens inside that simulation, on what feels like the tenth run of
the day -- bypass the monowire, drop over the wall, thirty seconds of open ground, five-four-three-
two-one-go on the hourly three-second backup gap, gun down the two guards in the entrance hall, punch
the basement button. The way out is to reach a secured section or be defeated, or to pull the plug
and eat dumpshock.

Waking up is scene two: ergonomic chairs with massagers, IV bags prepared and not yet administered,
whiteboards reading "Randomize backup cycle" and "Auditory alarm at door opening?", a heavy plasteel
door on a biometric maglock, and a technician making a panicked move for the alarm panel. The site is
an inconspicuous building in southern Tacoma near the docks, taken over in short order -- heavy
sensors outside, light security inside, four bored guards watching an urban brawl game, a SWAT squad
in debriefing, and the runners' own gear sitting in the armory, due to ship to Knight Errant HQ for
inventory in forty-eight hours. Then a text message -- "Call me, LG" -- triggers the flashback to the
seventh level of **Dante's Inferno** on Wednesday night, and the job: 3,000 nuyen plus 3,000 per
table rating each, sixty percent for destruction instead of theft.

The third act is Griffin at high alert, gloves off, with Ares-supplied security throughout, Force 8
wards, walls full of pressurised FAB bacteria, four barghest teams and thirty-nine guards. Rounding a
corner the team meets a second squad in black jumpsuits setting charges: a **Yamatetsu** covert ops
team, the same one from *Strings Attached*, with orders to demolish the underground half of the
building and close the tunnel. Their agenda and the runners' happen to line up. Afterwards, Lyle
buys dinner at **Dusty's**, and KSEA runs the words "terrorist attack".

## Timeline

- **Over the previous quarter** -- Griffin Biotechnology takes a huge influx of cash from DocWagon
  and Ares, breaks through on mapping the motor centers of the brain and on tissue development, and
  builds a state-of-the-art secured facility in Everett. Ares supplies the entire security suite at
  bargain prices; Knight Errant takes the guard contract.
- **SRM 00-03 FORCEd RECON** -- runners tramp across the grass, bluff past guards and hit every
  contact they can think of for a substantial interior layout. Organized by Lyle Green, paid for by
  Rose Croix.
- **SRM 01-04 The Gambler** -- runners breach the facility without leaving traces and steal paydata
  from a standalone terminal, using the key code and passkey of a lead researcher. Again funded by
  Rose Croix.
- **Over a month later, Wednesday 17:30** -- Lyle Green makes initial contact with the team.
- **Wednesday 22:15** -- the meet on the seventh level of Dante's Inferno. 3,000 + (3,000 x TR) each
  for the prototype and all associated research, 60 percent for destroying them instead. 48 hours.
- **Thursday, before 13:20** -- the assault goes in using a stolen car. It fails.
- **Thursday 13:20** -- the runners are captured by a Knight Errant SWAT squad and taken to the
  Tacoma site. Laes and depressants; the simulation begins.
- **Thursday, through the day** -- at least five runs through the simsense reconstruction of Griffin
  at high alert, each ending differently. KE's whiteboards fill up with lessons learned.
- **Thursday 20:10** -- the runners realize they are in a simulation. Adventure begins.
- **Immediately after** -- breaking the sim, the escape from the Tacoma compound, recovering gear
  (and ideally KE uniforms) from the armory, and optionally inserting false data into the Everett
  host from the Tacoma secondary host.
- **Friday** -- the flashback meet is remembered, and the team goes back to Griffin. All security
  measures are at high alert because of the failed attempt. The Yamatetsu team rolls in on its own
  schedule with charges already placed through the ventilation and the FAB delivery panels.
- **Friday 22:00** -- job deadline (the Cold Shower scene says 21:00).
- **After** -- payoff at Dusty's in Everett. KSEA reports a terrorist attack, dozens dead, one wing
  demolished. Knight Errant stock drops a tenth of a point; Griffin plummets seven points. The
  runners' gear was due to ship to Knight Errant HQ for inventory forty-eight hours after capture.

## NPCs (Persons of Interest)

| Name | Role | Org |
|---|---|---|
| Mr. Tamagochi | The name the shadows give for reaching the Yamatetsu covert ops team -- ask for him at the Wyndham Crossroads | Yamatetsu Corporation |
| Knight Errant Security Guard (Griffin Biotechnology) | The average two-year veteran on the Griffin detail -- professional, wired, all but immune to fast talk, bribes or intimidation | Knight Errant Security Services |
| Knight Errant K-9 Handler (Griffin Biotechnology) | A standard guard with a barghest on the leash -- four handler teams on constant duty for the duration of the alert | Knight Errant Security Services |
| Barghest (Knight Errant K-9) | Dual-natured black mastiff with sonar, Fear and a Paralyzing Howl, walking the Griffin perimeter with its handler | Knight Errant Security Services |
| Knight Errant Security Mage (Griffin Biotechnology) | Grade 3 initiate posted in the Griffin control room with quickened reflexes, three elementals and three watchers combing the site | Knight Errant Security Services |
| Knight Errant SWAT Trooper | The elite squad that captured the runners in the first place and is being trained on them at the Tacoma site | Knight Errant Security Services |
| Knight Errant Labtech (Tacoma Simsense Site) | The technicians running the illegal simsense training programme -- brainy pushovers between the runners and the alarm panel | Knight Errant Security Services |
| Yamatetsu Covert Ops Operative | One of five combat operators in black jumpsuits wiring Griffin's underground half to blow -- willing to ally, willing to double-cross | Yamatetsu Corporation |
| Yamatetsu Covert Ops Mage | Arcane support for the demolition team -- grade 3 initiate with anchoring, four elementals and a gold ring that keeps the squad invisible | Yamatetsu Corporation |

## Locations

| Name | Type | District | Notes |
|---|---|---|---|
| Knight Errant Tacoma Compound | corporate facility | South Tacoma (near the docks) | The inconspicuous building where Knight Errant runs captured shadowrunners through a simsense reconstruction of Griffin Biotech to train its own squads -- heavy sensors outside, light security inside |
| Griffin Biotechnology Compound Grounds | corporate facility | North Everett (172nd Street off Marine Drive) | Hillside, pine forest and a 4m elemental-raised granite wall under monowire, seeded with hidden cameras, pressure pads, UV laser grids and ultrasound -- and one exploitable weakness |
| Griffin Biotechnology Subterranean Labs (Float Floor) | research lab | North Everett (172nd Street off Marine Drive) | The buried half of Griffin: Beta Clinic, microtech and cyberware prototyping, the main nanotech lab on a vibration-isolated float floor -- and the wing Yamatetsu came to bring down |
| Wyndham Crossroads | hotel |  | Where the legwork table says to ask for a Mr. Tamagochi if you want to reach the Yamatetsu covert ops team |

## Existing organizations updated (sourced appends, nothing overwritten)

- **Griffin Biotechnology** -- GM notes; enemies: Rose Croix
- **Rose Croix** -- GM notes; enemies: Griffin Biotechnology
- **Knight Errant Security Services** -- GM notes
- **Ares Macrotechnology** -- GM notes
- **DocWagon** -- GM notes
- **Yamatetsu Corporation** -- GM notes; enemies: Griffin Biotechnology
- **Mackie Construction** -- GM notes
- **Draco Foundation** -- GM notes
- **Universal Omnitech** -- GM notes

## Existing locations / NPCs updated

- location: **Griffin Biotechnology Everett Research Facility**
- location: **Dusty's Steak House**
- location: **Dante's Inferno**
- location: **Brackhaus Estate**
- location: **Dohner Estate**
- location: **Draco Foundation Everett Complex**
- location: **Marine Drive Stuffer Shack and BP Gas Station**
- location: **Mackie Construction Offices**
- NPC: **Lyle Green**
- NPC: **Michael Davenport**
- NPC: **Rebecca Owls-Breath**
- NPC: **Dr. Indira Chontel**
- NPC: **Knight Errant Shift Supervisor (Griffin Everett)**

## Matrix systems -- to build in the Matrix designer (NOT built yet)

Six systems, in two clusters. Neither Tacoma host is sculpted, and because the decker is coming in
from an internal jackpoint at that site the security is toned down.

### Knight Errant Tacoma -- primary host

Orange-7/14/15/12/13/13. Controls all security measures and negotiates the connection to the outside
world through a vanishing SAN and one-way data flows.

| Step | Event |
| --- | --- |
| 4 | Probe-5 |
| 8 | Probe-7 |
| 12 | Passive Alert, Trace-9 |
| 16 | Blaster-8 |
| 20 | Active Alert |
| 24 | Shutdown |

### Knight Errant Tacoma -- secondary data host

Green-5/9/9/8/9/9.

| Trigger Step | Event |
| --- | --- |
| 3 | Probe-4 |
| 7 | Tar Baby-6 |
| 12 | Probe-6, Tar Pit-6, Passive Alert |
| 18 | Probe-6, Killer-6 |
| 25 | Tar Pit-6, Tar Pit-6, Killer-6 |
| 30 | Shutdown |

Paydata: **Personnel Files (250 Mp)**, protected with scramble-6 -- the current listing of all Knight
Errant personnel at the Griffin Biotech facility including training profiles and serial numbers,
annotated with the gear assigned on a standard basis and the additional gear each guard is qualified
to use. Worth 7,500 nuyen to the right fixer or fence. This host is also where a team decker can
insert false data for transmission to the Everett host -- which, combined with stolen KE uniforms
from the armory, is the book's suggested alternative to fighting through Griffin's front gate. If
the facility alert is triggered by an alarm panel or by security hearing the fray, both Tacoma hosts
go to active alert.

### Griffin Biotechnology -- communications network

Green-8/8/14/10/15/11. No paydata. The only system directly connected to the Matrix, via a standard
SAN. Houses the public corporate site, email and telecom connections, and the pattern recognition
and control software that analyzes and routes data packets by content. All inbound streams are
inspected; telecom signals pass to their recipients on the main network, email is retained in data
storage. Any traffic trying to pass through to the main network via the internal SAN is analyzed for
viruses, smart frames, persona programs and other illegal datastreams -- a decker must evade the
program's Sensor rating and then the node's Access rating.

| Trigger Step | Event |
| --- | --- |
| 5 | Probe-8 |
| 10 | Probe-10, Tar Baby-10 |
| 15 | Tar Pit-10, Passive Alert |
| 20 | Mark-Rip-12, Tar Pit-12 |
| 24 | Sparky-12, Active Alert |
| 28 | Shutdown |

**OperateIT (application smart frame, programmed by Ares).** Smart Core Rating 20, Size 1,416 Mp.
B 5, E 0, M 0, S 15, R 20, I 3D6. Programs: Analyze 6, Commlink 6, Read/Write 6. Options: DINAB-8.
Fence value 22,500 nuyen. Uses Analyze to detect anomalies (deckers, illegal programs) in any data
packet travelling in or through the system; uses Read/Write to send error and alarm messages to the
security consoles and to delete or edit files with illegal attachments or viruses; Commlink routes
all telecom traffic and inspects the signal for monitoring or tampering.

### Griffin Biotechnology -- logistics network

Green-8/8/15/8/8/15. No paydata. Same trigger table as the communications network. The facility's
nerve center for non-security automation: housekeeping and gardening drones, HVAC control, lighting,
elevator control, fire suppression, sprinklers and the PANICBUTTON system. Its link to the
communications network is one-way outbound and dedicated to PANICBUTTON reaching the Matrix to
notify the authorities -- and it runs on a dead man's switch, constantly transmitting status update
packets. Shutting down either the communications or the logistics network cuts that feed and
immediately triggers an alarm, unless a clever decker can somehow spoof the outbound data. The
security network has override control over most of this network's functions.

### Griffin Biotechnology -- main network

Orange-10/12/15/12/12/15. Handles all processing for the labs, offices and research areas. Not
connected to the Matrix directly, though research data and reports can be routed through the
communications network -- reaching it from outside means decking through two SANs, the second of
which only admits communications packets and standard packets directly requested by an internal
user. Deckers can obtain data files, all in the biomedical field, worth up to a combined maximum of
**100,000 nuyen**.

| Trigger Step | Event |
| --- | --- |
| 3 | Probe-8 |
| 6 | Probe-10, Tar Baby-10 |
| 10 | Tar Pit-10, Passive Alert |
| 13 | Mark-Rip-12, Tar Pit-12 |
| 17 | Sparky-12, Active Alert |
| 20 | Shutdown |

### Griffin Biotechnology -- security network

Red-8/15/12/10/12/15. No paydata. Controls all security-specific hardware inside and out and can
override the logistics network. This is the system the external dataline tap reaches -- from inside
it, runners can modify the biometrics database, pull guard schedules and more.

| Trigger Step | Event |
| --- | --- |
| 3 | Probe-8 |
| 5 | Probe-10, Tar Baby-10 |
| 8 | Tar Pit-10, Passive Alert |
| 10 | Mark-Rip-12, Tar Pit-12 |
| 12 | Sparky-12, Active Alert |
| 15 | Shutdown |

**Overwatch-VI Smart Core (programmed by Ares).** Rating 20, Size 1,850 Mp. B 5, E 0, M 0, S 15,
R 20, I 6D6. Programs: Analyze 10, Read/Write 5. Options: DINAB-8. Fence value 25,000 nuyen. Monitors
input from Matrix-wired cameras and sensors for differences from normal states, using its Analyze
rating as a Perception test with filters for waving branches, fans and similar false readings. On a
disparity it reroutes the camera's video feed to a primary monitor at a security station, creates a
log entry and sends a visual, audio and/or text alert. The same rating checks for attempts to modify
a camera's or sensor's signal, control or time code, which is what prevents looping and splicing.
Meant for a mainframe; a character who downloads it gets object code only, which cannot be modified,
but can be sold at the listed price.

## Flavor / not built

- **The Shadowland posters on the aftermath handout** -- **Iblis**, **ConspiracyTheorist**,
  **Skeptic**, **HammerJack**, **Wingless Falcon**, **Deacon Blues** and **Spider**, arguing about
  whether Broward got what he wanted, why anyone would flatten a cash cow every runner in the
  metroplex had been through, and whether this is a smear campaign that will make Knight Errant and
  Lone Star harder on minor infringements. Handles on a board, not characters.
- **The Dusty's Maitre D** -- unnamed, waits behind a small podium in a closed restaurant and will
  comment on the attire, odor and gunshot wounds of anyone who comes straight from the run. Folded
  into the Dusty's Steak House update.
- **The Griffin shift commander and corporate liaison as an individual** -- the post is filled by
  the Knight Errant Shift Supervisor row created by SRM 00-03 FORCEd RECON and appended to here.
- **The four guards in the Tacoma guardroom, the astrally projecting mage who answers a Tacoma
  alarm, and the Rapid Response Team the guards are relying on** -- posts and stat-block references
  rather than people; folded into the Knight Errant Tacoma Compound notes.
- **The technician in the van** at Griffin -- there is none in this adventure; the equivalent role
  belongs to SRM 01-09.
- **KSEA** -- the news outlet carrying the "Innocents Slaughtered as Griffin Biotechnology Struck by
  Terrorist Attack" story; a byline-free masthead.
- **The stolen car** used for the failed first assault, and the runners' vehicles, which are "in a
  safe location of the players choosing" while they are in the simulation.
- **Ares, Enfield, HK, Leyland-Rover, GMC, Ford** -- manufacturer name-drops on gear and vehicles.
- **Universal Omnitech and Ares private property, Puget Sound** on the aerial recon photo -- captured
  in the org updates and the compound grounds notes.

## GM play notes

- The structure is unusual and the book flags it: the adventure begins in media res, inside a
  simulation, with the run already failed. Scenes one and two (Waking Up, Getting out of bed) are
  paced differently from a normal Mission, and scene three (Cold Shower) is a flashback to the meet
  the players never got to play. After that it proceeds traditionally.
- Ending the simulation properly -- reaching the Beta Clinic or passing the airlock toward the
  nanotech facility, or being defeated with everyone captured, knocked out or killed -- gives the
  better payoff: a chance to interact with the facility at high alert without the danger of horrific
  death, and an exit from the host with minimal personal damage. Jacking out is a Willpower test at
  TN 8 and 5S Stun to soak; otaku with the Neurofilter echo and deckers running ICCM on a cranial
  cyberdeck get TN 6 and 3M Stun. It is not advised but is offered for players who know the Matrix
  rules and want the shortcut.
- Anyone with Simsense Vertigo runs at full negatives inside the simulation, which is a strong hint
  that something is not right. A memory test at TN 6 recalls flashes of a lab and of the team
  debriefing each other after failing the mission.
- The sadistic option the book prints and then disclaims: do not mention that this is the fifth run
  through the encounter, and reveal what is going on only after inducing a total party kill. "Neither
  the campaign director nor the author assume any responsibility for what players might do to any GM
  who would pull such a nefarious stunt."
- The runners are unarmed and unarmored until the armory. Emphasize it. Security responds
  non-lethally at first with flash-bangs and gel and goes lethal only against deadly force.
- Minimal legwork by design -- three Missions have already covered this facility, and players get the
  same security briefings issued in FORCEd RECON and The Gambler. If a player has extra information
  in hard copy or from memory, let them use it.
- The high-alert assault is written as potentially a high-mortality encounter. Push the players to
  understand how deadly it is. Distractions mostly backfire: Knight Errant investigates with the
  nearest team, deploys the rest for containment rather than a pitched battle, and gets spirits,
  astral scouts and support teams on scene within minutes. The book's own suggestion for a team that
  did not take uniforms and insert false security data into the Tacoma host is a go-gang assaulting
  the front gate, or individuals spread along the perimeter with launch weapons.
- The Yamatetsu encounter is the pressure valve: either a godsend for a beaten and battered team or
  another batch of stiff opposition. Their agendas line up right now. Play the standoff -- both squads
  had already assumed firing positions before anyone spoke.
- Karma: retrieving or destroying the prototype 1, retrieving or destroying the research 1, escaping
  the lab without heavy casualties or alerting security 1; maximum 3 team plus 3 individual. The book
  notes explicitly that this mission has a great impact throughout corporate Seattle and that the
  runners' business ethics should be awarded in consequence.
- Debugging for a team that refuses to go back: emphasize the reputation hit for turning down a job
  mid-run and remind them they know the facility better now. If they still refuse, pack up -- no
  karma and a hit to their reputation score.
- Debriefing Log boxes: the prototype was extracted / destroyed / remained secure; the research data
  was extracted / destroyed / remained secure; Griffin Biotechnology was BOOM! / stealthfully
  infiltrated / unharmed in any way.

