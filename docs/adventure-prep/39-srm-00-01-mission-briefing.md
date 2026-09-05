# SRM 00-01 Mission Briefing -- Adventure Prep: NPCs, Locations, Organizations, Matrix Systems

Source: SRM00-01A_missionbriefing.pdf, pp. 3-29; SRM00-01B_missionbriefing.pdf (Player Aids), pp. 3-21. Campaign order #39, in-game 2064.

Everything below is loaded into the campaign DB flagged `is_active: false` and `source_adventure: "SRM 00-01 Mission Briefing"` by `python scripts/adventure_ingest/run.py srm_00_01_mission_briefing`; flip entries active as the party meets them. Use the **Adventure** filter on the manage pages to see just this set.

## Plot synopsis

Weeks ago somebody dropped a three-storey building in **Redmond** on top of one of the best fixers
in the Seattle metroplex. Shadowrunners digging the rubble pulled out a cyberdeck, an armored
storage unit and a fireproof box holding a will dated only weeks before. Two days of cracking the
encryption later they had the whole empire in their hands: contacts, runners for hire, markers,
access codes, blueprints, recon photos, and enough compromising material to blackmail half of
Seattle's political and corporate establishment. Releasing it would start another shadow war, so
they followed the will's own instructions -- divide and conquer. Invitations went out to a dozen of
the more honorable fixers in the sprawl.

The meet is at high noon on a Monday in the **Maynard Pavilion**, an enclosed hire-able pavilion
inside **Freeway Park**, the deck of greenery built over the I-5 canyon next to the **Seattle Trade
and Convention Center** in Downtown. One hour of uninterrupted bargaining is all it takes. Because
even honorable fixers do not trust each other, each attending fixer nominated one guard who is new
to the Seattle scene and has no stake in the outcome -- that is the runners. **Trotter**, a bland
ex-runner who worked for the dead fixer, hands them 1,000 nuyen each in the Combat Biker room of
**THE Sports Bar** at 1130, promises 1,500 more at 1300, and tells them nothing: external security
only, nobody enters after the doors close, no attention drawn. Downtown is AAA and the convention
next door is the **Confederation of Security Providers** trade show -- the largest single gathering
of cops, feds and corporate security on the continent, all of them eating lunch in the park.

What nobody says out loud is that one of the fixers who refused the invitation sees the meet as a
chance to thin the herd. He bribed one of the organizing runners for the details and loaded five
kilos of liquid Compound XII into the fluid reservoir of a Chrysler-Nissan Caretaker gardening
drone -- the one the park's resident Mouse shaman **Scarper** calls "Hugh". At 1254 Hugh rolls to
the pavilion wall; at 1255 it goes off for 26D with a mere -1 per meter of falloff. Hugh has not
watered anything all morning, has no maintenance record in the park host, and smells faintly of
chemicals. Scarper will tell anyone polite enough to listen that he is worried about Hugh.

Around that hour: the fixer **Rolando** (Ray Marcello), a boorish initiate hermetic in gold chains,
arrives late with two ork bodyguards and intends to walk in anyway; a pair of Kamikaze-crazed
**Halloweeners** ride in off Seneca with stolen flamethrowers; a free field spirit in the shape of
a skateboarding girl plays Accident on whoever amuses her; a cyber-beagle from the trade show
records everything; a Wuxing drone demo comes down the I-5 canyon with the guns pointed at the
team; the reporter **Pete/Petra Sprent** offers 5,000 nuyen for an interview and knows about the
bomb; and a green FBI agent, **Barnaby Mason**, is watching from the vending machines. Play it
quiet and every fixer in the pavilion offers to be a contact.

## Timeline

- **Weeks before** -- the fixer's Redmond headquarters is levelled in a shadow war; runners recover
  the deck, the storage unit and the will (dated weeks earlier).
- **Two days later** -- the encryption falls; the will's list of honorable fixers is used to send
  out invitations.
- **A week after that** -- the fixers agree to terms: Freeway Park, one hour, one nominated outside
  guard each. A refused invitee bribes an organizing runner for the details.
- **Two days before the meet** -- the gardening drone "Hugh" goes in for "service" and comes back
  wrong; the bomb is fitted to its fluid reservoir.
- **Meet day, mid-morning (Monday)** -- each runner gets the call, two hours' notice, 2,500 nuyen.
- **1130** -- muster under the Everett Jets poster in the Combat Biker room of THE Sports Bar;
  Trotter pays 1,000 nuyen each and briefs them.
- **1145-1200** -- the runners get about fifteen minutes to walk the park; the fixers arrive in
  separate groups, one obvious bodyguard apiece.
- **1200** -- the pavilion doors close. Rating 6 ward, two force 3 watchers, a force 6 air elemental
  inside; the summoning magician sits in a cafe 300 meters away.
- **1200-1300** -- Rolando's arrival, the Halloweener firebomb run, the field spirit, Snoop, the
  Wuxing fly-by, the reporter, the fed, Deborah Figgis's allergy attack -- in whatever order the GM
  needs them.
- **1254** -- Hugh drives directly at a pavilion wall.
- **1255** -- detonation, 26D, -1 per meter, unless the drone has been shut down.
- **1300** -- contract over. Balance paid, 500 nuyen bonus if the hour was clean; each runner may
  take one fixer contact plus one other contact.

## NPCs (Persons of Interest)

| Name | Role | Org |
|---|---|---|
| Trotter | Bland ex-runner Face who worked for the dead fixer; arranges the meet, hires and pays the team | independent |
| Rolando | Gaudy initiate hermetic fixer, uninvited and late, who intends to walk into the meet regardless | independent |
| Betsy Ross | Ork bodyguard sister to Becky; Rolando's muscle at the pavilion door | independent |
| Becky Ross | Ork bodyguard sister to Betsy; Rolando's muscle at the pavilion door | independent |
| Scarper | Elderly Mouse shaman, ex-runner and unpaid keeper of Freeway Park; the adventure's safety net and clue-giver | independent |
| Fox | Archetypal Seattle fixer at the meet; treats runners as expendable tools but deals fairly | independent |
| Joeli Gibson | Dwarf fixer at the meet; smuggler networks, hardware and drones, lives on her yacht in Puget Sound | independent |
| Lyle Green | Young ex-simstar fixer at the meet; connector, media and high-society specialist | independent |
| Manny | Sociable mid-tier fixer at the meet; magical and street knowledge, expert on the city's unwritten history | independent |
| Michelle Rampling | Elf fixer at the meet hiding behind a piano teacher's life; data brokerage and the Seattle Matrix | independent |
| Willis Daltree | Old ork fixer of the Ork Underground at the meet; low-key, broad, loyal contact base | independent |
| Pete/Petra Sprent | Beautiful investigative reporter chasing the meet; 5,000 nuyen for an interview, and knows the bomb rumor | independent |
| Barnaby Mason | Ambitious junior FBI agent working the meet off the books, hoping to recruit a source | UCAS Federal Bureau of Investigation |
| Snoop | Cybernetically wired beagle turned loose in the park as a live surveillance demo for the trade show | Confederation of Security Providers |
| Crawler (Halloweeners) | Human Halloweener recruit on Kamikaze, burning his way across the park with a stolen flamethrower | Halloweeners |
| Toss | Elf Halloweener recruit riding with Crawler; the second flamethrower | Halloweeners |
| Deborah Figgis | Seattle local going into anaphylactic shock in the middle of the runners' perimeter | independent |
| Ranjit Devi | Nervous Indian tourist mistaken for an assailant when Deborah Figgis collapses on him | independent |

## Locations

| Name | Type | District | Notes |
|---|---|---|---|
| Freeway Park | park | Downtown | Green deck built over the I-5 canyon beside the Convention Center; the run's whole battlefield. |
| Maynard Pavilion | pavilion | Downtown (Freeway Park) | Hireable pavilion in an enclosed corner of Freeway Park; the fixers' meet happens inside it. |
| Seattle Trade and Convention Center | convention center | Downtown | Convention hall adjoining Freeway Park, hosting the Confederation of Security Providers show. |
| THE Sports Bar | bar | Downtown (University Street and Terry Avenue) | Family-style sports bar on University and Terry where Trotter briefs and pays the team; rumored Mafia money. |
| Scarper's Bower | squatter camp | Downtown (Freeway Park) | The overgrown corner of Freeway Park the Mouse shaman Scarper has made into a home the authorities tolerate. |

## Organizations (new)

| Name | Type | Tier | Notes |
|---|---|---|---|
| Confederation of Security Providers | trade association | 4 | Continental trade body of police, federal and corporate security providers, holding its annual show next door to the meet. |
| Puget Sound Sports Fishing Club | social club | 1 | Respectable anglers' club whose small lapel pin is the one non-magical thing Rolando wears. |

## Existing organizations updated (sourced appends, nothing overwritten)

- **Halloweeners** -- GM notes
- **Lone Star Security** -- GM notes
- **UCAS Federal Bureau of Investigation** -- GM notes; leadership: Barnaby Mason
- **Wuxing, Inc.** -- GM notes
- **Seattle Mafia** -- GM notes
- **Knight Errant Security Services** -- GM notes
- **DocWagon** -- GM notes

## Existing locations / NPCs updated

- location: **Renraku Arcology (SCIRE)**
- location: **The Ork Underground**

## Matrix systems -- to build in the Matrix designer (NOT built yet)

### Freeway Park host (run from the Seattle Trade and Convention Center)

Green-5/10/8/8/9/8. Feeds every camera, sensor, microphone, speaker, sprinkler and interactive
display in the park, plus the park maintenance schedules (including the service record that does
*not* show a maintenance call for "Hugh"). Access from the park side: Electronics B/R (4), base
time 30 seconds, to open an interactive unit's casing, then Electronics (4) to fit a dataline tap;
the same pair of tests shuts an individual camera or sensor down. Camera feeds are not monitored
constantly -- automated pattern recognition triggers the alerts, and a few dead cameras are
expected, so the pavilion's coverage can be blacked out for the hour without an alarm. Uncovered
suspicious activity is recorded on a 1-2 on 1D6.

| Step | Event |
| --- | --- |
| 5 | Probe-6 |
| 10 | Probe-8 |
| 15 | Scout-7 |
| 20 | Trace-7 |
| 25 | Passive Alert; security deckers (inferior) |
| 30 | Ripper (bind-rip)-7 |
| 35 | Trace-7 with trap Blaster-4 |
| 40 | Blaster-7 |
| 45 | Active Alert |
| 50 | Construct-8 (Killer-10, Probe-6) |
| 55 | Blaster-9 |
| 60 | Sparky-11 |
| 65 | Shutdown |

Paydata: 3 points (100 Mp, 70 Mp, 40 Mp). Michelle Rampling (Fences 3 (Paydata 6), Seattle Matrix
8) is the obvious buyer. Note the campaign cap: no single character walks away with more than
about 5,000 nuyen from this run, paydata included.

The park is also a known playground for young hackers who break in to make mischief -- sprinklers
firing unexpectedly, the park speakers turned up loud and badly -- which the GM can use as cover
noise or as a complication in the middle of the meet hour.

## Flavor / not built

- **The dead fixer** -- never named. The intro calls the fixer "he or she" and the Legwork table
  says "a local fixer got popped and now one of her buddies is selling off her little black book",
  so the book leans female without committing; the headquarters was a three-storey building in
  Redmond, now a lot full of concrete and rebar. Captured in the synopsis and Trotter's background.
- **The rival fixer who planted the bomb** -- never named either. He refused the invitation, bribed
  one of the organizing shadowrunners for the details, and expects to seize the data cheaply once
  the competition is dead. A deliberate loose end for later Missions play.
- **The unnamed summoning magician** in a cafe 300 meters from the pavilion, holding the rating 6
  ward, two force 3 watchers and the force 6 air elemental; run him with the Lone Star magician
  stats from New Seattle p.114. Folded into the Maynard Pavilion notes.
- **"Hugh"** -- the Chrysler-Nissan Caretaker gardening drone carrying the bomb (Hand 4/4, Speed 10,
  Body 1, Pilot 1, gardening autosoft 3, 5-liter liquid tanks). A machine, not a person; kept in the
  Freeway Park notes and the synopsis. Base value 3,500 nuyen if defused and stolen.
- **The free field spirit of Freeway Park** -- unnamed, materializes as a 1.5-meter girl with a
  skateboard and plays Accident on whoever amuses it. Kept in the Freeway Park notes.
- **The other five or six fixers at the meet** -- the will listed almost a dozen and only six get
  contact cards; the rest arrive, each with one obvious bodyguard, and are never described.
- **Chrysler-Nissan, Ares Macrotechnology, Mitsuhama, Ruger, Colt, Ceska, Heckler & Koch, Defiance**
  -- manufacturer name-drops on gear only.
- **The Everett Jets** (the poster in THE Sports Bar's Combat Biker room) -- team name-drop.
- **The frustrated park technician, the annoying busybody, the wanted fugitive** -- Pushing the
  Envelope hooks with no names or stats.

## GM play notes

- This is the campaign's demo scenario: it must run in as little as two hours, with the optional
  Case Studies dropped in only when there is time. Leave 15-20 minutes at the end for Debriefing
  Logs. Only one event has a fixed clock -- the bomb at 1255 -- so everything else can be reordered
  freely to suit the table.
- Every field of expertise is deliberately covered (combat, negotiation, magic, rigging, Matrix) and
  several Case Studies exist to let one archetype shine: The Drunken Shaman for magicians, Cyber
  Snoop and Fly By for riggers and deckers, Here's the News and The Nosey Fed for faces, Watch What
  You Eat for a medic. Pick by team composition. Do not run more than two or three at once.
- The core lesson is restraint. Downtown is AAA, the convention next door is full of cops and
  corporate security eating lunch, and the correct answer to almost every provocation is the quiet
  one. If the team is spoiling for a fight, stage the demonstration the book suggests: an unrelated
  NPC across the park draws a weapon and is instantly gunned down by the guards (with gel rounds,
  though nobody watching can tell).
- Scarper is the safety net and the clue line. Etiquette (Street) (4) plus Interrogation (4) gets
  "Hugh" out of him; he also advises on the field spirit, comments on unsubtle work, and can
  miraculously survive the blast to heal the wounded. Do not overplay him -- let the runners do the
  work.
- The bomb clues are layered: Scarper's worry; no maintenance record in the host; a Perception (6)
  after half an hour notices Hugh has watered nothing; a Perception (10) within a meter catches the
  chemical smell; and at 1254 the drone simply drives at the wall. Disarming is Electronics B/R (6)
  over a base minute to get inside (failure detonates it), then Electronics (4) to kill the timer.
  Draining the tank without disabling the safeguard detonates it at half volume for 18D.
- Rolando is a set-piece in three modes -- confrontation, persuasion or smarts. Reward the team that
  makes him leave without a shot fired; he departs with insults and grudging admiration and is
  available as a contact.
- Payoff: balance of 2,500 nuyen each, plus 500 if the hour was genuinely clean, plus scavenged
  gear and paydata, capped at about 5,000 nuyen per character. Karma: 1 for finding the bomb, 1 for
  disarming it, 1 for an uninterrupted meeting, 1 for not being publicly identified as a
  shadowrunner, -1 for unnecessary public violence; 7 maximum with roleplaying awards.
- Contacts are the real reward and the campaign's on-ramp: each character may take at most one
  fixer (Fox, Joeli Gibson, Lyle Green, Manny, Michelle Rampling, Willis Daltree, or Rolando) plus
  one other (Scarper, Barnaby Mason, Pete/Petra Sprent). Match the fixer to how the player actually
  played the hour -- that choice is what carries forward into the rest of the season.

