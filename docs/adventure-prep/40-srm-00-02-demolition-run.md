# SRM 00-02 Demolition Run -- Adventure Prep: NPCs, Locations, Organizations, Matrix Systems

Source: SRM00-02A_demolitionrun.pdf, pp. 3-21; SRM00-02B_demolitionrun.pdf (Player Aids), pp. 3-11. Campaign order #40, in-game 2064.

Everything below is loaded into the campaign DB flagged `is_active: false` and `source_adventure: "SRM 00-02 Demolition Run"` by `python scripts/adventure_ingest/run.py srm_00_02_demolition_run`; flip entries active as the party meets them. Use the **Adventure** filter on the manage pages to see just this set.

## Plot synopsis

**Dr. Fredericks**, CEO of **Paladin Medical Technologies**, has smashed a datapad across a marble
boardroom table hard enough to open his own COO's face. Paladin has lost three contracts in a
month -- Seattle General, then the Salish border patrol -- 1.5 million nuyen a time, all of them in
the pharmaceutical supply division, all of them to a bidder who came in ten percent under Paladin's
own numbers within hours of Paladin submitting them. At the rate they are going they are out of
business inside a year.

**Katey Nagahara** found the answer and **Bob Struthers** found the mechanism. **DocWagon** has put
up a fully automated pharmaceutical plant in the rolling hills of Snohomish, discovered it can make
patches and meds far faster than DocWagon itself consumes them, and started dumping the surplus on
the Seattle market. An enterprising decker made a timely offer and sold DocWagon a walk through
Paladin's JSR database -- operating figures, contract charges, everything. That is how the bids
keep landing ten percent low. Fredericks tells his Special Security Director, **Brian Wallace**,
over the intercom that it would really help Paladin if that facility no longer existed, and that he
hopes to sleep well soon. Wallace, whose job is to make such dreams come true without Paladin's
fingerprints anywhere near them, picks up the telecom and calls a real saint of a man.

**Saint James** is a new fixer with an old resume: until recently he was a shadowrunner and the
bodyguard of one of the most successful fixers in Seattle, until she was forcibly retired. Clipped
British accent, impeccable manners, Cerebral Booster 2 behind the charm. He books a private meeting
room at the **Sheraton Towers** at Sixth and Pike, lets the hotel do his security screening for
him, sets out real coffee, and offers the runners 2,500 nuyen each plus 2,000 more if the plant is
rubble inside 24 hours. Mr. Johnson calls himself **Smithers** and says he is from Universal
Omnitech; a lucky corporate contact roll gets the truth.

The plant is the run. Four meters of slatted cyclone fence and razor wire on high ground a mile
from anything, an anti-air radar dish in the front yard and three six-round missile launchers in
the back, five human guards and a troll with reusable auto-injectors full of Jazz, a security
operator in the control shed running the cameras and a hunting rifle and a scanner tuned to the
runners' own radio traffic, and an eighteen-year-old **security mage** who has warded the break
room at Force 3 purely for the practice, which is exactly the sort of thing that makes a team
believe the break room matters. Reinforcements are thirty minutes out. The neighbouring farmer,
**David Wadsworth**, will tell a polite team almost everything, and the Matrix host will tell a
decker the rest -- including a scrambled file marked only **H**.

## Timeline

- **Over the past month** -- Paladin loses three pharmaceutical supply contracts, Seattle General
  and the Salish border patrol among them, each worth about 1.5 million nuyen in revenue.
- **Some time before that** -- DocWagon builds the Snohomish plant on land previously owned by
  Shiawase; two months of construction, most of it spent digging the basement out, the rest
  assembled from prefabricated duraplast pieces.
- **Recently** -- an enterprising decker cracks Paladin's JSR database and sells DocWagon its
  operating figures and contract charges; DocWagon starts undercutting by ten percent.
- **Days before the meet** -- Struthers backtracks the access logs and identifies the intrusion;
  Katey Nagahara identifies DocWagon and then the Snohomish plant. Fredericks explodes in the
  boardroom, then gives Wallace the order over the intercom.
- **Five days before the meet** -- the plant's last weekly supply delivery.
- **Meet day, early evening** -- the call: a cultured British voice, the Sheraton Towers, Sixth and
  Pike, 9 PM sharp, the Saint James party.
- **9 PM** -- weapons screening, private elevator, the briefing, 1,000 nuyen of trust and a job.
- **The next 24 hours** -- legwork, surveillance across the midnight / 8 AM / 4 PM shift changes,
  the farmer, the City Planning blueprints, the Matrix run. The next supply delivery is 48 hours
  out, so the plant is low on raw materials throughout.
- **The hit** -- guards neutralized or circumvented, four demolition packs placed on Demolitions
  (4) locations, five minutes to clear the fence, then the plant goes up loudly.
- **Thirty minutes after any alarm** -- DocWagon reinforcements arrive: six more guards and a
  security magician.
- **Afterwards** -- back to the Sheraton Towers, payment, a toast, and "I understand Denver's a
  charming city for the visitor."

## NPCs (Persons of Interest)

| Name | Role | Org |
|---|---|---|
| Saint James | Cultured British ex-runner turned fixer; hires and pays the team, and will set the charges himself if nobody else can | independent |
| Brian Wallace | Paladin's Special Security Director; Mr. Johnson for the run under the alias Smithers of Universal Omnitech | Paladin Medical Technologies |
| Dr. Fredericks | CEO of Paladin Medical Technologies; orders the plant destroyed without ever saying so | Paladin Medical Technologies |
| Bob Struthers | Paladin's COO, cut open by the CEO's datapad, who traced the intrusion into the company's JSR database | Paladin Medical Technologies |
| Katey Nagahara | Paladin contract analyst who traced the losses to DocWagon and located the Snohomish plant | Paladin Medical Technologies |
| David Wadsworth | Snohomish agri-farmer next to the plant; the module's best legwork source, if the runners do not condescend | independent |
| DocWagon Snohomish Shift Leader | Senior guard of the plant's five-man human detail; the man who names a price to look the other way | DocWagon |
| DocWagon Snohomish Troll Guard | The plant's basement muscle, hauling raw materials where no security camera watches | DocWagon |
| DocWagon Snohomish Security Operator | Camera and missile watchstander in the control shed; the reason the guards know the team is coming | DocWagon |
| DocWagon Snohomish Security Mage | Eighteen-year-old company magician getting practical experience; warded the break room for fun | DocWagon |

## Locations

| Name | Type | District | Notes |
|---|---|---|---|
| DocWagon Snohomish Pharmaceutical Facility | corporate facility | Snohomish (rural) | Automated drug plant on high ground in the Snohomish farmland, fenced, missile-defended, and the target of the run. |
| Sheraton Towers | hotel | Downtown (Sixth and Pike) | Upmarket Downtown hotel at Sixth and Pike where Saint James runs his meets and lets the house do his screening. |
| Paladin Medical Technologies Headquarters | corporate headquarters | Seattle metroplex | Paladin's offices, boardroom and in-house clinic, where the order to level the DocWagon plant is given. |
| Wadsworth Farm | farm | Snohomish (rural) | Bioengineered-wheat agri-farm neighbouring the DocWagon plant; David Wadsworth's land and the team's best human intelligence. |

## Organizations (new)

| Name | Type | Tier | Notes |
|---|---|---|---|
| Paladin Medical Technologies | corporation | 3 | Mid-tier Seattle pharmaceutical and medical supplier being undercut into extinction by DocWagon, and the run's real employer. |
| Seattle City Planning Department | government agency | 2 | Metroplex planning authority whose public website sells the original blueprints of any permitted building for 250 nuyen. |

## Existing organizations updated (sourced appends, nothing overwritten)

- **DocWagon** -- GM notes; enemies: Paladin Medical Technologies
- **Universal Omnitech** -- GM notes
- **Aztechnology** -- GM notes
- **Shiawase Corporation** -- GM notes
- **Lone Star Security** -- GM notes
- **Salish-Shidhe Council** -- GM notes

## Existing locations / NPCs updated

- location: **Seattle General Hospital**

## Matrix systems -- to build in the Matrix designer (NOT built yet)

### DocWagon Snohomish plant host

Green-4/8/8/8/8/12. Deliberately soft: the plant holds no important files and only manufactures
standard biotech gear, so DocWagon has not thought it worth serious protection. An inexperienced
decker should get in and out. It is also the single richest legwork source in the module.

| Step | Event |
| --- | --- |
| 4 | Probe-4 |
| 8 | Probe-6 |
| 11 | Tar Baby-6, Passive Alert |
| 14 | Probe-8 |
| 20 | Killer-6, Active Alert |
| 24 | Shutdown |

Tasks and tests:

- **Interior surveillance footage** -- Slave test (hand out the Matrix camera-view player aid,
  SRM00-02B p.7).
- **List of files** -- Index test. Guard roster, operations manual, production schedule, delivery
  schedule, inventory, random files -- plus, optionally, a backup copy of **File H**, scrambled and
  encrypted, flagged by the module as "relevant in a future mission".
- **Guard roster** -- Files test. Opens the bribery route (15,000 nuyen for a whole shift, floor
  10,000) and the option of removing individual guards magically or physically before the hit.
- **Operations manual** -- Files test, one hour to read. Automated camera monitoring, no
  inspections, unexpected inspection teams are presumed saboteurs and are to be denied access or
  otherwise dealt with, and lethal force against intruders is authorized with no requirement to
  capture.
- **Delivery schedule** -- Files test. Weekly deliveries, the next one in 48 hours, so the plant is
  low on raw material for the whole adventure.
- **Production schedule** -- Files test. Finished product is picked up every 24 hours and moved to
  a secure warehouse; there is never much product on site.
- **List of automated programs** -- Index test. Fixed menu: medkit construction, antidote slap
  patch, stim patch, tranq patch, trauma patch.
- **Creating a new automated program** -- Computer (6), base time 48 hours, then a Files test to
  upload and a Control test at +2 to implement. The target numbers are meant to defeat the idea; if
  a team somehow pulls it off the plant can be made to turn out DMSO, Freeze Foam, oxygenated
  fluorocarbons (P4MO), Jazz (from the stim drug elements) or MAO (from the tranq elements).
- **Changing the running program** -- Slave test.

File H is worth a Karma point on its own: sell it and the team gets nuyen, destroy it or quietly
keep it and they get the Karma. Saint James, asked about it, shrugs -- "Haven't the foggiest, old
son. Maybe you should hang onto it..."

## Flavor / not built

- **The enterprising decker** who cracked Paladin's JSR database and sold DocWagon its operating
  figures and contract charges -- never named, never met, and the entire cause of the adventure. A
  standing hook.
- **Saint James's two bodyguards**, who stand like statues in the corner of the meeting room and
  fight for him if he is attacked -- no names, no stats.
- **The Sheraton Towers security rigger**, who has been watching the team since they set foot on
  hotel property and controls hidden weapon mounts and the airtight-door gas trap. Folded into the
  Sheraton Towers notes.
- **The four remaining human guards** of the Snohomish detail share the shift leader's stat block
  and are run as a unit; only the shift leader gets a row.
- **The DocWagon reinforcement element** -- six additional guards and a security magician (SR3
  Combat Mage stats) arriving thirty minutes after any alarm. Folded into the facility notes.
- **The IWS DLK MK 8 forklift drones** (two) and the lawn-care drone -- machines with stat blocks,
  kept in the facility notes; the forklifts are excellent cover and useless to a runner.
- **The agricorp** David Wadsworth grows his bioengineered wheat for -- unnamed.
- **The secure warehouse** that takes the plant's finished product every 24 hours -- unnamed and
  off-map.
- **"New Lifers"**, Ares, Renraku, Remington, Enfield, Heckler & Koch, Beretta, Colt -- one-line
  name-drops in legwork banter or on gear.
- **The Table Rating chart** (TR 1 Green TN 4 / 2 Streetwise TN 5 / 3 Professional TN 6 / 4 Veteran
  TN 8 / 5 Elite TN 10 / 6 Prime Runner TN 12, by average career Good Karma) -- a campaign scaling
  aid introduced in this module, referenced in the NPC notes as "Karma TR".

## GM play notes

- This is a much harder module than SRM 00-01 and the book says so: the guards use real tactics,
  will usually see the team before the team is inside, set ambushes, and are well armed. If the
  players are new, drop the Jazz -- without it the guards are not street samurai and the tactics
  alone carry the fight.
- Reward legwork above everything. There are five separate routes into the plant's secrets -- the
  farmer, distance surveillance across a shift change, City Planning blueprints for 250 nuyen,
  astral recon for the only full interior map, and the Matrix host -- and a team that uses three of
  them will find the run comfortable while a team that uses none will probably lose people.
- The 30-minute reinforcement clock is the real timer, not the 24-hour bonus. Once the security
  operator calls it in, everything is a countdown; the sirens are audible in time to run.
- Do not let the surprise-inspection trick work. It is in the text specifically as a lesson that
  the opposition is not stupid: the guards invite the "inspectors" inside, surround them, and open
  fire.
- Guards do not have to die, and the Karma says so: 1 for destroying the facility, 1 for not
  killing the guards, 1 more (cumulative) for circumventing them entirely -- bribery, drugs, magic,
  stealth, anything that gets the charges laid without an alarm -- and 1 for keeping or destroying
  File H rather than selling it.
- Bribery is a legitimate solution and worth signposting: the guard roster is one Files test away,
  the shift leader wants 15,000 nuyen and will take 10,000, and the whole thing costs less than a
  firefight. Refuse his price, though, and the garrison doubles.
- Never let a wounded runner call DocWagon without spelling out the consequences first. That is a
  career-ending mistake dressed up as a reflex.
- Saint James is the season's fixer and should end the module liked. He debriefs with real
  interest, pays without argument, sets the charges himself for free if the team has no demolitions
  expert, and toasts them at the end. Attacking him ends careers, permanently.
- Two threads to keep alive: File H, which the module explicitly plants for later; and the "one
  fixer, what was her name again" that Saint James used to guard, who is the dead fixer whose
  estate was being divided in SRM 00-01.

