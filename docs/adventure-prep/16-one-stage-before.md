# One Stage Before -- Adventure Prep: NPCs, Locations, Organizations, Matrix Systems

Source: Shadowrun 2e - Adventure - One Stage Before {FASA7312}.pdf, pp. 4-63. Campaign order #16, in-game 2053 (August).

Everything below is loaded into the campaign DB flagged `is_active: false` and `source_adventure: "One Stage Before"` by `python scripts/adventure_ingest/run.py one_stage_before`; flip entries active as the party meets them. Use the **Adventure** filter on the manage pages to see just this set.

## Plot synopsis

Seattle has gone crazy over **The Shadows**, the hottest band since Jetblack died: one show at the
Kingdome, sixty-five thousand tickets gone in an hour, ten dead at the ticket offices. Broke and
nursing drinks at the **Blue Flame Tavern**, the runners are collected by two immaculate Highstar
"junior expediters" (**Daniel Maynes** and **Lester Hatton**), handed a 5,000-nuyen credstick for
showing up, and driven in a Rolls Royce Phaeton to **Kobe Terrace Park**, where **Jonathon Teague** of
**Highstar Incorporated** (a Mitsuhama subsidiary) offers 80,000 nuyen to find out who has been sending
death threats to **Lew Allenby**, the irascible dwarf who owns **Caravan Productions** and manages The
Shadows. Start by talking to Allenby, Teague says. Allenby throws them out of his Occidental Avenue
office the moment they mention Teague ("Those vultures?"), and on the way out a chromed giant who calls
himself "just **Wallace**" pumps them about Allenby.

Three hours later a Lone Star patrol opens fire on sight: Allenby is dead at his desk, still jacked in,
and a tip with manufactured evidence names the runners. Teague is "in conference". **Meta**, Teague's
lethal expediter, meets them at **The Mattresses** under the Space Needle to say Allenby is dead and
she wants the killer -- and proves her chrome when the ork **Teddy Boys** shoot up the club (pure
coincidence). Teague finally calls, sets a meet at Highstar's Harbor Island warehouse, and it is a
sniper-and-samurai gauntlet that ends with a swim in Elliott Bay. Then **Tangent**, Allenby's
secretary, phones from hiding: her boss spent his last afternoon reviewing simsense demos, somebody
wiped the demo directory, and The Shadows will be at media producer **Blair Wickingham's** party in
Matthews Beach. At the party the band toasts "absent friends, and those who are no further away than
sunset", Teague's double flees, and go-gangers in grim-reaper colors -- the **Nightstalkers** -- turn
out to be the band's security. Tailing the ganger **Blaze** to a dead firehouse in Bitter Creek, the
runners meet the gang's leader: **Jetblack**, the angst-rock megastar who faked his death, now a
vampire, Allenby's old friend, and the band's secret protector.

Jetblack's password ("Unruly") opens the hidden datastore on Allenby's computer: his diary (Teague
wanted Caravan; over Allenby's dead body), and backups of the deleted demos -- one of them carrying
Killer black IC written by Teague's decker **Himem**, which fried Allenby through his datajack.
Wallace, an FBI contractor with no homicide jurisdiction, supplies the word "Charon", which reveals
the tapped SAN into Highstar's own system: takeover files, Himem's research, and Teague's home address
at **Vashon Heights**. Twenty-five **Hard Corps** guards, dogs, lasers and an earth elemental defend
it. Only a reunion -- convincing Jetblack that The Shadows know what he is and do not care -- buys the
runners twenty Nightstalkers for a diversion. The proof is a notebook computer in Teague's den. Lone
Star recalls the warrants without apology; Highstar and Mitsuhama declare Teague a loose cannon and he
"commits suicide" in a Redmond rooming house within 48 hours; The Shadows pay 100,000 nuyen, and
Jetblack plays one private jam with them -- the first time all five stand on one stage.

## Timeline

- **Prologue (twelve days before the Kingdome show)** -- Allenby hangs up on Teague for the last time;
  Tangent confirms the Kingdome, cancellation insurance and Knight Errant security.
- **Day 1** -- Blue Flame Tavern pickup; Kobe Terrace Park meet (10,000 binder); Caravan offices;
  Wallace outside. Three-plus hours later Lone Star attacks (Allenby is already dead, killed by the
  booby-trapped demo). Meta's call and The Mattresses; the Teddy Boys.
- **Day 1-2** -- Teague's warehouse ambush at Pier 16, Harbor Island; Tangent's call; Wickingham's
  party that evening (Teague's double, Meta's covering fire, the toast).
- **Following days** -- Blaze the tail; the Nightstalkers' firehouse and Jetblack ("Unruly"); Mindfield
  at Caravan (Himem's Black-5 IC and the Highstar Special Ops van in ten minutes); Wallace again
  ("Charon"); the Highstar system and Himem's dogfight; Jetblack refuses, then the Richmond Highlands
  reunion (night only); the assault on Vashon Heights.
- **Friday August 25 2053** -- the News-Intelligencer reports Teague's "suicide" (success) or the
  "Nightwalkers" gang war on Vashon Island (failure). The Kingdome show follows within days.

## NPCs (Persons of Interest)

| Name | Role | Org |
|---|---|---|
| Jonathon Teague | Highstar's Machiavellian executive VP posing as 'a junior expediter'; hires the runners to frame them for Allenby's murder | Highstar Incorporated |
| Lew Allenby | Irascible dwarf owner of Caravan Productions, manager of Jetblack and The Shadows; murdered at his desk by a booby-trapped simsense | Caravan Productions |
| Darryl Wallace | 'Just Wallace' / 'Ripper' -- chromed ex-Special Forces FBI contractor investigating Caravan; feeds the runners the word 'Charon' | UCAS Federal Bureau of Investigation |
| Meta | Teague's personal expediter -- an ex-shadowrunner 'hatchetwoman' in haute couture and silver gloves who does not know about the murder | Highstar Incorporated |
| Jetblack | Angst-rock megastar who faked his death, became a vampire, and now secretly leads the Nightstalkers; Allenby's old friend, The Shadows' hidden protector | The Nightstalkers |
| Marli Bremerton | The Shadows' lead singer and main songwriter; the band's face to the world and the one who opens the door for Jetblack | The Shadows |
| Joey Nightmare | The Shadows' lead synth-guitarist, cosmetically modified to look like a cross between a devil and an ape; a soft-spoken nice guy | The Shadows |
| Sid Id | The Shadows' elven synth player, programmer and record producer; waist-length blond hair, gray eyes, rarely makes sense when he speaks | The Shadows |
| Ernest Hawkins | The Shadows' second synth player, backing vocalist and light-show designer; lemur-eyed, sloth-slow, coaxes music out of trashed instruments | The Shadows |
| Tangent | Allenby's golden-haired assistant who knows the runners did not kill him, survives a hit, and hands them Wickingham's invitations before leaving town | Caravan Productions |
| David Graves | Caravan's shy database clerk, a musician wannabe frightened of most things, runners included | Caravan Productions |
| Gnasher | Allenby's well-spoken troll bodyguard who escorts unwanted visitors out -- as hard as necessary | Caravan Productions |
| Daniel Maynes | Highstar 'junior expediter' -- Teague's immaculate, inhumanly calm talker and knife-thrower; also the bodyguard who covers the double | Highstar Incorporated |
| Lester Hatton | Highstar 'junior expediter' -- Daniel's stockier partner who takes center stage when the hard option is the only option | Highstar Incorporated |
| Himem | Teague's 23-year-old wunderkind decker who murders by simsense: booby-trapped chips, modified Black-5 IC, and an ego that will not cut and run | Highstar Incorporated |
| Takahashi Yanaga | Highstar's well-entrenched president, whose chair Teague is trying to take; never appears | Highstar Incorporated |
| Blaze | Young elven Nightstalker on a Yamaha Rapier, new to the surveillance game, who leads the runners home to Jetblack | The Nightstalkers |
| Blair Wickingham | Hot media producer with big-network connections whose Matthews Beach penthouse party is where The Shadows can be met | independent |
| The Pig | 115 kilos of ork fat, muscle and bad temper, heeled like a walking armory; Blue Flame regular pinned to the wall by Daniel's knife | independent |
| Dr. Silvus Nyberg | University of Seattle physicist whose quantum-physics-and-metaphysics lab blew out a wing of the science building (August 2053 news) | University of Seattle |
| Kyle Arigharu | Fuchi spokesperson who announced the Symbolic Processor AI milestone with fireworks (August 2053 news) | Fuchi Industrial Electronics |

## Locations

| Name | Type | District | Notes |
|---|---|---|---|
| Caravan Productions Offices | corporate facility | Occidental Avenue, south of the Kingdome, near the docks | Suite 500 in a pitted pre-2000 ferrocrete building with no cameras or guards; platinum discs, Tangent's desk, Allenby's antique desk and the computer that killed him |
| Kobe Terrace Park | park | Downtown, South Jackson Street just west of the freeway | A little oasis of green among the skyrakers by day, a gang killing ground by night; Teague's Mr. Johnson meet |
| The Mattresses | private members club | Denny Way near Seattle Center, under the Space Needle (beside Tam's Under the Needle) | Underground members-only club where bigwigs from every corp meet in guaranteed safety -- the members hunt down and kill anyone who causes trouble |
| Highstar Warehouse (Pier 16, Harbor Island) | warehouse | Pier 16, north shore of Harbor Island | Deserted wharf where Teague's 'meet' is a sniper, samurai and street-mage gauntlet that ends in Elliott Bay |
| Highstar Incorporated Building | corporate headquarters | Downtown (address not given) | Highstar's Seattle offices: weapons detectors, chem-sniffers, a lobby full of guards; Teague is always 'in conference' |
| Wickingham's Penthouse (Matthews Beach) | penthouse | Matthews Beach (exclusive side) | Media producer Blair Wickingham's twelve-storey penthouse party: starlets, producers, The Shadows, Nightstalker doormen, and Teague's double |
| Nightstalkers' Firehouse (Bitter Creek) | gang territory | Palatine Avenue North, Bitter Creek (northern Downtown) | Deserted fire station with black-painted windows: bikes in the garage, a dormitory of bedrolls upstairs, Jetblack in the dark |
| The Shadows' Richmond Highlands Condo | residential community | Richmond Highlands | Ground-floor condo of a musician friend where The Shadows hide between shows; a guard in a bulletproof booth and no obvious alarms |
| Teague's Vashon Heights Compound | private estate / compound | Vashon Heights, north tip of Vashon Island (waterfront, 1 km from the hydroplane-ferry terminal) | Teague's three-hectare waterfront fortress: monowire fence, 25 Hard Corps guards, dogs, lasers, pressure pads, an earth elemental, gunships in ten minutes -- and the proof in his den |

## Organizations (new)

| Name | Type | Tier | Notes |
|---|---|---|---|
| Highstar Incorporated | corporation (entertainment; Mitsuhama subsidiary) | 3 | Seattle entertainment corp -- live shows, trid -- that is really a Mitsuhama puppet; Teague's takeover of Caravan runs through it |
| Caravan Productions | talent management / production company | 2 | Lew Allenby's one-man empire: Seattle's premiere management and production company; managed Jetblack, manages The Shadows |
| The Shadows | music band (megastar act) | 2 | The hottest band since Jetblack died: Marli Bremerton, Joey Nightmare, Sid Id, Ernest Hawkins; one sold-out Kingdome show |
| The Nightstalkers | go-gang | 2 | Low-profile biker gang led in secret by the vampire Jetblack; every member carries his bite; moonlights as The Shadows' security |
| The Teddy Boys | mucker gang (ork) | 1 | Ork vandals in cheap Edwardian velvet and lace who prefer defacing people to property; their attack on The Mattresses is a genuine coincidence |
| Hard Corps Security Inc. | private security corporation | 3 | One of the best and toughest security firms in the plex -- astral, computer, lasers, and gunship back-up inside ten minutes; guards Teague's Vashon Island compound |

## Existing organizations updated (sourced appends, nothing overwritten)

- **Mitsuhama Computer Technologies** -- GM notes; allies: Highstar Incorporated
- **Lone Star Security** -- GM notes; enemies: The Teddy Boys
- **Knight Errant Security Services** -- GM notes; allies: Caravan Productions
- **Fuchi Industrial Electronics** -- GM notes
- **Renraku Computer Systems** -- GM notes
- **Universal Brotherhood** -- GM notes
- **University of Seattle** -- GM notes
- **Tir Tairngire** -- GM notes
- **Seattle News-Intelligencer** -- GM notes
- **Rusted Stilettos** -- GM notes
- **Crimson Crush** -- GM notes
- **Salish-Shidhe Council** -- GM notes
- **UCAS Federal Bureau of Investigation** -- GM notes; leadership: Darryl Wallace

## Existing locations / NPCs updated

- location: **Blue Flame Tavern**
- location: **The Kingdome**
- location: **The Space Needle**
- NPC: **The Chinaman**
- NPC: **Maria Mercurial**

## Matrix systems -- to build in the Matrix designer (NOT built yet)

**1. Allenby's computer / Caravan Productions system** (map p.32). Officially NOT on the Matrix; the
only way in is physical (Allenby's desk, datajack or keyboard as a tortoise). Himem hardwired a tap
from an LTG line, giving it a concealed SAN into Highstar. Two hidden datalines, each revealed only by
a password spoken as a system command: "Unruly" (CPU-1 to DS-2) and "Charon" (CPU-1 to SAN-1).
Tortoise utilities on the box: Bod 3, Sensors 2, Analyze 1, Evaluate 1, Browse 2, Decrypt 2.

| Node | Function | Rating / IC |
|---|---|---|
| CPU-1 | System CPU | Orange-3, Blaster 3, Trace and Report 7 (report vanishes down the hidden line to SAN-1 after 1 turn; destroy it first) |
| SPU-1 | Graphics / numeric co-processor array | Green-2, Access 2 |
| DS-1 | Primary datastore: Caravan business records; the demo directory Himem wiped | Orange-3, Scramble 2, Blaster 3, Trace and Report 7 (report goes to CPU-1 then SAN-1; 2 turns to kill it) |
| DS-2 | Concealed datastore ("Unruly"): daily bit-for-bit backups of DS-1, Allenby's diary (100+ Mp, five hours; keywords Shadows / Nightstalkers / Jetblack / Teague), and six backed-up simsense demos (~4 min each) -- one is the booby trap | Orange-3, Scramble 2, Blaster 3 |
| I/OP-1 | Keyboard and terminal | Green-2, Access 2 |
| I/OP-2 | Datajack connection | Green-2, Access 2 |
| SAN-1 | Hidden SAN ("Charon"); second dataline onward to Highstar SAN-1 | Orange-3 |

Notes: Perception (4) on meeting the Trace and Report 7 ice reveals it was added to the original
security. Playing the rigged demo = combat with Killer 4 black IC in an Orange-3 node: from a cyberdeck,
normal; jacked straight into Allenby's box, only its tortoise utilities; through a trode rig, no
fighting back, Willpower (4) to jack out, reduced damage. Five actions after a successful trace Himem
drops two modified semi-autonomous Black-5 IC into SAN-1, one to CPU-1 and one to DS-1; they leave when
the decker is down or out, and only white IC remains afterward. Perception (4) on seeing black IC
emerge from the CPU "wall" reveals a second hidden dataline. Physical response: Highstar Special Ops in
10 minutes (7 on the second run).

**2. Highstar Incorporated corporate system** (map p.36-37). Reached from Allenby's SAN-1; SAN-2 is the
public Matrix door. Highstar is a shell company and DS-1 says so. Himem defends it in person and will
not retreat.

| Node | Function | Rating / IC |
|---|---|---|
| SAN-1 | Link from Allenby's system | Orange-3 |
| SAN-2 | Matrix access | Orange-4, Killer 3, Tar Pit 3 |
| CPU-1 | Main CPU | Orange-3, Tar Baby 4, Barrier 5 |
| SPU-1 | Newly installed; manages the Highstar-Caravan link | Red-3, Blaster 4, Trace and Burn 4 |
| SPU-2 | Accounting processor | Orange-3, Barrier 4 |
| DS-1 | Basic accounting: reveals Highstar is a shell | Orange-3, Barrier 3, Scramble 3 |
| I/OP-1 to 3 | Accounting terminals and datajacks | Green-3, Barrier 2 |
| SPU-3 | "Executive" SPU, almost exclusively Teague's | Red-3, Barrier 4, Killer 3 |
| DS-3 | Teague's Caravan takeover files plus a PI report on Allenby's blackmail vulnerability; motive not proof; 25 Mp, 10,000 nuyen to the right buyer | Red-2, Barrier 3, Scramble 3, Black-4 |
| I/OP-5 | Teague's office terminal | Red-2, Barrier 4 |
| CPU-2 | Back-up CPU; mainly supports Himem's research in SPU-6 | Orange-3, Tar Baby 4, Barrier 5 |
| SPU-4 | Traffic between CPU-1 and CPU-2 | Orange-3, Barrier 3 |
| SPU-5 | Personnel | Orange-4, Barrier 4, Trace and Burn 3, Killer 3 |
| DS-2 | Personnel data, including Teague's home address (Vashon Heights, north tip of Vashon Island) | Red-2, Barrier 3, Scramble 3, Blaster 3 |
| I/OP-4 | Personnel terminal | Orange-3, Barrier 3 |
| SPU-6 | Himem's research processor | Red-4, Barrier 4, Trace and Burn 3, Tar Pit 3, Trace and Report 8, Killer (Black-4) |
| DS-4 | Himem's modified-black-IC research (100 Mp, 50,000 nuyen as a set, 1,000 per 10 percent) and encrypted booby-trapped-simsense notes (Intelligence (8), 24 hours; 150 Mp, 200,000 nuyen; 2,000 per 10 percent); value drops 10 percent a week | Red-4, Barrier 4, Scramble 4, Trace and Report 8, Black-5 |
| I/OP-6 | Datajack in Himem's research lab | Red-3, Barrier 5 |
| SPU-7 | Manages SAN-2; monitors all Matrix traffic | Orange-4, Barrier 6, Tar Baby 3 |

Notes: an external alert or a successful Trace and Report brings Himem (Fairlight Excalibur, Attack 7,
Hacking Pool 12) into the system toe-to-toe and the Special Ops van back to Caravan in seven minutes.
Fencing the paydata is a trap -- Teague has told the shadows the team pays more dead.

**3. Teague's compound security computer** (map p.43). Not on the public Matrix: SAN-1 is
dial-out-only and calls Hard Corps headquarters on active alert. Entry is the guard-shack terminal
(I/OP-1) or the concealed terminal in Teague's den. Beating it shuts down most of the house systems.

| Node | Function | Rating / IC |
|---|---|---|
| CPU-1 | Controls the entire system | Orange-4, Barrier 4, Blaster 4 |
| SPU-1 | CPU to SAN-1 communications | Orange-2, Barrier 3 |
| SPU-2 | Seawall motion detectors | Orange-4, Barrier 3 |
| SPU-3 | House lasers and pressure pads | Orange-4, Barrier 3, Blaster 3 |
| SAN-1 | Dial-out-only; auto-calls Hard Corps HQ | Orange-4, Barrier 3 |
| I/OP-1 | Guard-shack terminal | Orange-4, Barrier 4, Blaster 3 |
| I/OP-2 | Terminal in Teague's study | Orange-4, Barrier 3 |
| SM-1 | Seawall motion-detector system (Rating 8, 10 m) | Orange-4, Barrier 4, Blaster 2 |
| SM-2 | Two-phase laser system on the house perimeter (doors, windows, patio) | Orange-4, Barrier 4, Blaster 2 |
| SM-3 | Pressure-pad system in the main hallways (40 kg) | Orange-4, Barrier 4, Blaster 2 |

**4. Teague's notebook computer** (den, p.44-45) -- a stand-alone portable, Green-2, password security
equivalent to Barrier 2; jack in with the right interface hardware or run it as a tortoise. Contains
the takeover files and Himem's installation notes: the proof. Not worth a host of its own.

## Flavor / not built

- **Teague's double** (only knows his original is in hiding; briefed with the runners' pictures),
  **the Phaeton driver / rigger** (VCR 2, Car 4 / Phaeton 8, Beretta 200ST), **Teague's Greek-declaiming
  wage mage**, **the Highstar combat mage**, **Highstar Security Operatives**, **the seven park
  guards** -- stat blocks on the Highstar org row.
- **Teague's cook** (Pedestrian archetype, butcher knife, hides under the sink), **Hard Corps guards,
  troll animal handlers, dogs and riggers**, the **Force 4 earth elemental** -- on the Hard Corps and
  compound rows.
- **The Mattresses' elf maitre d'** and its security team; **Wickingham's lobby guards, interior guards,
  serving staff and twenty-five guests**; **Lone Star troopers, combat mages and SWAT** -- on the
  location and Lone Star rows.
- **The ambush team** at Pier 16 (three snipers, a street mage, five street samurai) -- on the
  warehouse row; hired through untraceable "channels".
- **Tam's Under the Needle** (the business beside The Mattresses' stairway; nothing else is said of it),
  **Teague's city home** (address never given, "guarded by a small army"), **the Redmond rooming house**
  where Teague's body turns up, **the hydroplane-ferry terminal** on Vashon Island and its mainland dock
  south of Lincoln Park, **the Lone Star building downtown**.
- **Concrete Dreams** (the only megastar act Allenby never managed), **Adam Vikk**, **Elvis** and **Jim
  Morrison** -- name-drops. **The vampire fan** who infected Jetblack; **the friend who modified
  Allenby's hardware**.
- News-handout names: **Herb Bass** (NABA commissioner), **Kevin Welch** (Portland Sports Committee),
  **Sonora Quigley** (musicologist), **the Moolah Shriners** and the **Moolah Temple** (St. Louis),
  **Bi-Star Police**, **All-Salish Nations Bank**, **Crusader Security** (Chicago) and the **Byrne
  Projects** riot, **Hurricane Ethelbert**, the **Pacific blue slime**. Reporters' bylines are FASA staff
  jokes (N. Findley, C. Kubasik).
- **Sprawl Sites archetypes** used for maps: Mid-size Restaurant (The Mattresses), Large Residence
  (Wickingham's penthouse; the Richmond Highlands condo), Fire Station (the Nightstalkers).

## GM play notes

- A decision-tree frame-up: the runners are Class A murderers by the end of Day 1 and every phone call
  leads to trouble. Keep Teague alive and unreachable until the end (the double at the party), and keep
  the Highstar building impregnable -- the only way in is Matrix, via Allenby's tapped SAN.
- Needs a decker and a mage. Three Matrix runs escalate: Allenby's box (tortoise-capable), Highstar
  (Himem in person), the compound security computer (shuts down lasers and pressure pads).
- The Teddy Boys are a genuine coincidence; do not let the players build a theory on them. Wallace is
  odd on purpose -- "let them wonder who the frag that guy was."
- The toast is the key to the climax: "to those who are no further away than sunset" means The Shadows
  know Jetblack is a vampire. Intelligence (4) to recall it if the players are stuck. Jetblack meets at
  night only.
- Fencing Highstar paydata is suicide while Teague's bounty stands: every fixer meet becomes an ambush
  of escalating lethality until the team takes Teague down.
- The final assault is a movie: 50-70 guns on the grounds, but only shots aimed at the runners get
  rolled; the Nightstalker diversion happens off-stage. Get in and out before the Yellowjacket (10 min)
  and the Stallion / Citymaster (15 min).
- Karma: dump Himem 1; evidence in the Highstar system 1; find the booby-trapped simsense 1; the
  Jetblack / Shadows reunion 3; defeat Teague yourselves 2 OR let his corp eliminate him 1; the proof in
  the notebook 3.
- Payoff: Teague never pays. The Shadows pay 100,000 nuyen plus two Kingdome tickets each; Highstar /
  Mitsuhama may pay a 20,000 "public service" retainer; blackmail = hit teams. Lone Star recalls the
  warrants without apology.
- Loose ends: Himem alive and humiliated; Wallace as a future Johnson; Jetblack and The Shadows as
  contacts (and a bootleg jam-session simsense the team must not sell); Meta if she survived; Hard
  Corps' opinion of whoever hit their showpiece; Tangent gone from Seattle; a hundred-thousand-nuyen
  band with no manager.

