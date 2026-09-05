# SRM 01-03 Harvest Time -- Adventure Prep: NPCs, Locations, Organizations, Matrix Systems

Source: SRM01-03A_Harvest_Time.pdf, pp. 3-29; SRM01-03B.pdf (player handouts). Campaign order #46, in-game 2064 (a single day, days after the Kethers Building raid of SRM 01-02; no in-world date is printed).

Everything below is loaded into the campaign DB flagged `is_active: false` and `source_adventure: "SRM 01-03 Harvest Time"` by `python scripts/adventure_ingest/run.py srm_01_03_harvest_time`; flip entries active as the party meets them. Use the **Adventure** filter on the manage pages to see just this set.

## Plot synopsis

The vault raid of SRM 01-02 destroyed or carried off most of DocWagon Seattle's Type O donor organs
and its vat-grown stock, and DocWagon's contracts require reserves it can no longer show. Growing
organs takes time. So **Devon Tyler**, a low-profile executive who has just been handed
responsibility for the temporary organ storage facility in Fort Lewis, received a memo telling him
to use any method necessary -- and hired the **Doom Squad**, a team of washed-out mercenaries who
work almost exclusively for DocWagon, to kill some SINless and harvest what was inside them.

At about four in the morning they hit the **Raikun**, a small, isolated urban tribe scratching a
living out of Redmond Barrens scrap. **Kip**, the tribe's ancient shaman, had a premonition and
warned the chief; Kip, **Jimbo**'s family and **Ron**'s family hid, and everyone else -- roughly two
thirds of the tribe, some two dozen people -- was butchered in their beds. Jimbo took a bullet and
had one eye cut out of his head before the squad's leader picked up a signal that someone was
coming and called the pull-out. What that signal actually was is a rigger's drone, sitting over the
hill scouting an unrelated job, recording every second of it. The rigger sold the footage through a
friend of a friend to **Rose Croix**, and was paid handsomely.

Walter Broward's people know they did not order this, and are certain DocWagon did. The video would
anchor a media campaign that could break DocWagon's remaining reputation -- but it needs
corroboration and it needs the one-eyed man. So the fixer **Saint James** calls the runners at
lunchtime and sends them to a closed diner where a nervous first-time Johnson named **Vincent
Capello** plays them the recording, hands over a grainy printout of a face, gives them the
encampment's address and 1,000 nuyen each, and tells them to produce the witness and any evidence
tying DocWagon to the killings before five o'clock.

The encampment is a burnt-out shell with a funeral pyre in front of the scrap shed and a background
count of 4 hanging over it. A friendly ork squatter called **Mike** explains what happened; a map in
the survivors' bunker points five miles across the Barrens to a sewer; and the Doom Squad, who have
come back to finish the job, pull up in the same black Americar while the runners are still standing
in it. Below ground, **Mindy** leads the team through the tunnels to what is left of her tribe, and
Jimbo offers a bargain: help us prove who did this, and I will go and speak to your employer.

Two leads, one afternoon, pick one. Kip's, in which the tribe's totem **Rat** -- who is not a totem
at all but a trickster free spirit farming their worship -- has been pinned behind an astral barrier
by **Sqoosh-Water**, the free city spirit whose personal domain these sewers are; free him and he
leads the team to a grate opposite a DocWagon clinic in Fort Lewis and names the man at the top-floor
desk. Or **Luxi**'s, in which an anonymous tip has produced an LTG address that turns out to be the
clinic's own feeble Green host, and a file called **Operation LifeRaft** with the Doom Squad's
contact details and the Raikun's address in it.

And then, as the runners bring Jimbo up out of the sewer, an armoured DocWagon Citymaster slides to
a stop in the street. Tyler has told a High Threat Response team that Jimbo is a kidnapped client in
medical danger. They have gel rounds, legal authority, and a growing suspicion that no call for this
extraction ever came over their radios.

## Timeline

- **Days back** -- the Kethers Building raid (SRM 01-02) destroys or removes most of DocWagon
  Seattle's Type O donor organs and vat-grown tissue stock.
- **Shortly after** -- DocWagon fails the reserve clauses in its contracts. Devon Tyler, newly
  responsible for the Fort Lewis temporary organ storage facility, receives a memo telling him to
  use any method necessary, and opens Operation LifeRaft with the Doom Squad.
- **Day 0, about 4 AM** -- the Doom Squad hits the Raikun encampment. Kip's premonition saves two
  families; roughly two thirds of the tribe die. Jimbo is shot and loses an eye. The squad pulls out
  when its leader picks up a signal. A rigger's drone, scouting the area for an unrelated run,
  records the whole attack.
- **Day 0, dawn** -- Mike helps the survivors burn the bodies; the remnant leaves in the tribe's VW
  Superkombi for the sewer hideout Rat directed them to. The background count over the camp is 4.
- **Day 0, morning** -- the rigger sells the footage on through a mutual contact to Rose Croix.
  Saint James phones the runners; the Johnson asked for them by name.
- **Day 0, noon** -- the meet at Rosie's. 4,000 nuyen each, 1,000 up front, bonus for evidence,
  delivery before 5 PM.
- **Day 0, afternoon** -- the encampment, Mike, the bunker map; the Doom Squad returns to silence
  witnesses; the sewer walk with Mindy; the bargain with Jimbo; Kip's run or Luxi's run.
- **Day 0, late afternoon** -- Tyler gets a tip on Jimbo's location and calls out an HTR team on a
  false client-extraction pretext. The Citymaster meets the runners at the sewer mouth.
- **Day 0, before 5 PM** -- Rosie's again: Jimbo delivered, the balance paid, 1,000 nuyen per level
  more for evidence.
- **Next day** -- Lone Star raids DocWagon clinic #147 on an anonymous tip; two dozen sets of
  DNA-typed organs, Jimbo's eye matched to him, the video handed over by anonymous sources.
- **Days after** -- DOCW drops four points; Tyler is charged and expected to be convicted of murder
  in the first degree; DocWagon is fined on multiple counts and sued for the tissue lost at the
  Kethers Building; Rose Croix nearly doubles its client base.

## NPCs (Persons of Interest)

| Name | Role | Org |
|---|---|---|
| Devon Tyler | The low-profile DocWagon executive who read a memo about reserves and ordered a tribe butchered for its organs; the man Rose Croix needs identified | DocWagon |
| Vincent Capello | Rose Croix's brand-new Mr. Johnson, hand-picked by Walter Broward and running his first shadowrun without knowing how to talk to shadowrunners | Rose Croix |
| Jimbo | Chief of the Raikun, the one-eyed witness the whole run exists to recover, and the man whose testimony ends Devon Tyler | Raikun |
| Kip | The Raikun's ancient, failing shaman, whose premonition saved two families and whose totem is not a totem | Raikun |
| Mindy | Jimbo's younger sister and Kip's apprentice, the tribe's guide through the sewers -- and the only Raikun who suspects their totem is a fraud | Raikun |
| Luxi | The Raikun's self-taught electronics man, who owns half a Matrix rig and one anonymous tip pointing at DocWagon's clinic host | Raikun |
| Ron | Head of the second Raikun family to survive the massacre; one of the three men at the table when the runners arrive | Raikun |
| Mike | Ork squatter and longtime friend of the Raikun who wanders into the ruined encampment to grieve, and gets shot at for looking like a witness | independent |
| Rat (Trickster Free Spirit) | The trickster city free spirit the Raikun worship as their totem, caged in a sewer puddle by a rival, and the only thing that knows Devon Tyler's name | independent |
| Sqoosh-Water | The greater free city spirit whose Personal Domain the Redmond sewers are; it caged Rat and will not let anyone near the cage | independent |
| Hank | Bear street shaman of the Redmond Barrens who turned down Rose Croix's magical healing program to keep treating anyone who walks in | independent |
| Ratman | The Matrix handle whose anonymous tip gave Luxi the LTG address of DocWagon's Fort Lewis host -- and let the tribe believe their totem sent it | independent |

## Locations

| Name | Type | District | Notes |
|---|---|---|---|
| Rosie's | restaurant | Tenth and Terrace | The tiny dinner restaurant at Tenth and Terrace, closed and empty, where Rose Croix's first-time Johnson plays the runners a drone recording of a massacre |
| Raikun Encampment | squatter camp | Redmond Barrens | The walled scrap camp where two thirds of a tribe were butchered for their organs, now empty except for a funeral pyre and a background count of 4 |
| Raikun Sewer Refuge | subterranean community | Redmond Barrens (an old residential district five miles from the encampment) | A bricked chamber off the Redmond sewers where a dozen surviving Raikun hide; reached through an open manhole in the backyard of a derelict house and a five-minute walk in the dark |
| The Boarded House | ruins | Redmond Barrens (beside the Raikun's sewer entrance) | The derelict, planked-up house next to the sewer access where Kip must go to reach Rat when no magician is available -- and where three squatters, or a gang, already live |
| Sqoosh-Water's Domain | sewer network | Redmond Barrens (beneath the abandoned residential district) | The stretch of Redmond sewers a greater free city spirit has claimed as its Personal Domain, fed on illegally dumped toxic and radioactive waste, where it keeps a rival spirit caged in a puddle of goo |
| DocWagon Clinic #147 | hospital | Fort Lewis (a commercial district just across the border) | A two-storey neighbourhood clinic in Fort Lewis with DocWagon's temporary organ storage, a small vat-growing lab and Devon Tyler's office on the floor above it |

## Organizations (new)

| Name | Type | Tier | Notes |
|---|---|---|---|
| Raikun | urban tribe | 1 | A small, deliberately neutral urban tribe of Barrens scavengers who worship the spirit they believe is the totem Rat, and who lose two thirds of their number to an organlegging run in a single night |
| Doom Squad | shadowrunner team | 2 | A small, old-school in-house team of washed-out mercenaries who work almost exclusively for DocWagon, take the wetwork nobody else will, and butchered the Raikun for their organs |
| Redmond Razors | go-gang | 1 | A low-level Redmond gang in red and silver-grey, a few of whom have squatted the boarded house over the Raikun's sewer entrance |

## Existing organizations updated (sourced appends, nothing overwritten)

- **DocWagon** -- GM notes; leadership: Devon Tyler; allies: Doom Squad; enemies: Raikun
- **Rose Croix** -- GM notes; leadership: Vincent Capello
- **Lone Star Security** -- GM notes

## Existing locations / NPCs updated

- NPC: **Saint James**
- NPC: **Michael Davenport**
- NPC: **Hondo**

## Matrix systems -- to build in the Matrix designer (NOT built yet)

Two systems, both in SR3 notation. Neither is a major host: the point of the Fort Lewis office is
how weak it is, and how carefully the one door that matters is locked.

**1. DocWagon Fort Lewis office host (clinic #147)** (p.18). A small peripheral office with very few
critical datastores, because everything confidential lives on the main DocWagon host.

Security code: **Green-7/9/10/7/10/8**

| Trigger step | Security event |
|---|---|
| 4 | Probe-4 |
| 8 | Probe-6 |
| 12 | Passive Alert, Trace-8 |
| 16 | Blaster-6 |
| 20 | Active Alert |
| 24 | Shutdown |

Details:
- The host is not sculpted at all and its security is lacking. It is essentially an internal gateway
  to the main DocWagon host, and the only sculpted icon in it is a vault gate leading there.
- **The DocWagon gateway** is the real security. Opening it takes an 8-digit combination AND a
  signature file held in an encrypted chip in the terminal's own hardware -- a peripheral key, so
  that access is only ever possible from selected terminals. In the Fort Lewis office, only Devon
  Tyler's terminal carries the chip.
- A very skilled decker can turn that into a permanent asset. Understanding the encrypted hardware
  key: **Computer (10)**, base time 6 hours. Using it to build an access to DocWagon's main host with
  a personal account: **Computer (15)**, base time two weeks. If achieved, write the permanent access
  through the Fort Lewis office on the Mission Summary sheet.
- **Operation LifeRaft** -- the contact information for the runners DocWagon hired and the details of
  the run -- is protected by **Scramble (6)**.
- A security camera slave continuously records the front door, and the front-door maglock can be
  controlled from here.
- 5,000 nuyen worth of paydata sits in the local office host.
- The slave controls for the temporary organ storage equipment are NOT remotely accessible. The only
  way to reach them is to jack in physically inside the office.

**2. The clinic's office terminals** (p.19). Password protected: Computer (6) with a base time of 30
minutes to get into one directly, or hack them through a cyberterminal as a **Green-4/4/4/4/4/4**
system. They hold organ inventory files, organ request forms and lab analyses -- nothing
incriminating, since DocWagon keeps confidential data on the main host and it cannot be reached from
here. The exception is Devon Tyler's own terminal, which carries the LifeRaft file.

**Not mapped**: the main DocWagon host behind the vault gate (the prize for the decker who spends
two weeks on the hardware key); Rose Croix's systems; the LTG address itself, which Luxi's contact
"Ratman" mailed him and which simply resolves to system 1 above.

## Flavor / not built

- **The rigger** who filmed the massacre from a drone while scouting for an unrelated run, and the
  **mutual contact** who brokered the footage to Rose Croix -- deliberately anonymous. The Johnson
  says only that the rigger is unconnected to the attack, that the filming was purely random, that
  no contact information is available, and that he waited until his own run was finished before
  selling. On the Rose Croix row.
- **The two lab technicians** waiting upstairs at clinic #147 for the Doom Squad's next delivery,
  the **four DocWagon technicians** who can open the lab, the **security guard**, the ground-floor
  clinic's **doctors, patients and administrative staff**, and the **HTR team** in the Citymaster --
  stat blocks and behaviour on the DocWagon Clinic #147 and DocWagon rows.
- **The three squatters** in the boarded house -- stat block on that location's row; the Redmond
  Razors who replace them at higher table ratings do get an org row.
- **The two mid-aged women, three crowbar-armed young men and three children** in the sewer refuge,
  and the **Raikun Tribe Member** template -- on the Raikun row.
- **Devil rats** (the optional sewer encounter) -- same block as SRM 01-02; and the **ghosts or
  shedim** offered as a Veteran-and-above hazard at the encampment, which try to take the body of any
  mage who goes astral unprotected.
- **The DocWagon modified Citymaster** and the **Hughes WK-2 Stallion** flown by the aerial response
  team -- the book refers the GM to Rigger 3 rather than printing stats.
- **The other city Rat shaman** who once bound "Rat" as a servant, and the **struggling squatters**
  whose conjuring he hijacked -- backstory on the Rat row.
- **The memo** that told Devon Tyler to use any method necessary, and whoever wrote it -- the single
  most important unnamed thing in the adventure, and the reason Shadowland assumes Tyler is taking a
  fall for his superiors.
- The Shadowland posters on the handout other than Hondo -- **OurTeam**, **Linei**, **The Chromed
  Accountant**, **Bitrunner** and **Deacon Blues** -- board handles with no face; their claims are
  recorded on the Rose Croix, DocWagon and Lone Star rows.

## GM play notes

- Everything happens in one day and the clock is diegetic: the attack was at 4 AM, the meet is at
  noon, the witness has to be delivered before 5 PM. Say the deadline out loud and hold to it -- late
  delivery costs a Karma point.
- The adventure is a straight line with one fork, and the fork is the whole design: Kip's lead needs
  a magician, Luxi's needs a decker, and both variants have a no-specialist fallback that turns into
  bodyguarding or a break-in. Pick the branch the table can actually run, and do not offer a branch
  they cannot. Both leads reach the same two answers -- Devon Tyler's name and Operation LifeRaft --
  so nothing is lost either way.
- Tone: the book wants dread, and gives the GM the tools. A background count of 4 over a funeral
  pyre. A dead camp that stinks of chemicals and burnt people. Five minutes of low tunnels where
  low-light vision does not work and orks have to walk in the sewage. Whispering, milky-eyed
  neighbours in SRM 01-02's building were mood; here the mood is grief.
- Shadows Crossing must not become a set-piece. The Doom Squad exists to prove the runners are on
  the right track and that somebody professional is on the other side. Resolve it in about one combat
  turn and twenty minutes of real time; if it drags, have a local ganger or two wade in on the
  runners' side, and let them charge Doom Squad gear as their fee. The squad opens on Mike because he
  looks like the survivor -- protecting him is the scene's actual test.
- The Raikun cannot pay. They have 600 nuyen, a van worth 750, and Kip's four doses of Spirit
  Strength, which he will part with only if the team asks nicely and treats him with respect. Helping
  them anyway is what makes the run work; the book says so and so does the Karma table.
- Sqoosh-Water is much stronger than everything else in the adventure -- Force 4 doubled in its own
  domain, Immunity to Normal Weapons, four targets at once. Run it as a spirit that would rather
  frighten intruders off than fight, lead with Confusion and Fear, and let a clever team leave with
  the barrier down rather than the spirit dead.
- Out of the Rat's Hole is the trap that looks like a fight and is not. The HTR team is on gel
  rounds, is legally entitled to shoot, and is already uneasy: no call came over the radios, no
  signal is coming from the "customer", and the order came from someone senior they cannot name.
  DocWagon Procedures (4) lets a sharp runner name the breach out loud. Convince them Jimbo is not a
  client and they stand down. If the fight starts and runs long, have the main office recall them and
  let the table wonder why.
- Do not let the runners strip the Citymaster. The technicians stay aboard, seal themselves in, and
  can kill the engine and fuel system; the doors need a Rating 5 thumbprint and a Rating 6 palmprint
  that know the difference between an unconscious owner and a dead one, and a failed bypass warns the
  team. Bring in the aerial unit if you have to.
- If time is short at either end: skip the sub-runs and go straight to Jimbo's extraction, or have
  the team escape the sewer mouth by a hair as the Citymaster pulls up. The one thing that cannot be
  cut is delivering Jimbo alive.
- Karma: 2 for Jimbo recovered less than Seriously wounded and before 5 PM, or 1 if he is
  unconscious, Seriously injured or late; 1 more for datafiles implicating DocWagon and Tyler; up to
  3 individual; maximum 5.
- Arc hooks to plant: Mindy's growing suspicion of Rat and what the runners choose to tell her; the
  favour a free spirit now owes the team; who Ratman is; the memo Tyler was following and who wrote
  it; the Doom Squad's surviving members, still at large and now able to identify the team; and
  Deacon Blues's warning that the next move is DocWagon's.

