# SRM 01-06 Lost and Found -- Adventure Prep: NPCs, Locations, Organizations, Matrix Systems

Source: SRM01-06A_Lost_and_Found.pdf, pp. 3-23; SRM01-06B.pdf (Player Aids), pp. 1-7. Campaign order #49, in-game 2064.

Everything below is loaded into the campaign DB flagged `is_active: false` and `source_adventure: "SRM 01-06 Lost and Found"` by `python scripts/adventure_ingest/run.py srm_01_06_lost_and_found`; flip entries active as the party meets them. Use the **Adventure** filter on the manage pages to see just this set.

## Plot synopsis

At 23:00 an Aztechnology engineer named **Edmundo Castellian** watches the security tape for the
fifth time and understands that he is a dead man. The tape shows him walking through the
underground parking deck, saying hello to the guard, driving out in a car with superconductive black
paint glowing white as the engine idles, and showing his pass on the way past. Billions of nuyen of
Aztechnology money, gone, and whoever took it wore his face perfectly -- no extra wrinkles around
the eyes, the voice pattern an exact match. "With that sort of perfection it could only be magic."
The **Amanecer 5000**, the prototype he is due to unveil to the board of directors at sunrise, is a
multi-billion-nuyen gap in the middle of his work floor, and once it is missed nobody will let him
protest his innocence; security will simply walk him to the lower labs. So he calls the brother he
has not spoken to in years.

The thief is **Jackson Rollo**, Edmundo's own lead assistant, who wore his boss's face out of the
building and means to "recover" the car in the morning and be the hero of the board meeting.
Promotion is a cutthroat business at Aztechnology. To park the car where nobody would look for it he
handed the keys to **Heather**, the elf dog shaman who leads a Puyallup gang of elf posers called
the **Sidhe Devils**, and told her a mole inside Aztech wanted the corporation's newest toy to reach
the right hands. She agreed to take it to **Tir Tairngire**. Rollo never imagined a gang that small
could actually get it across the border in time -- and Heather, once **Bennett** popped the hood
and found the engine, scrapped the plan to strip it and started mapping a route north.

Edmundo's brother **Eduardo "Lucien" Castellian** is a fixer with a bullet scar through his cheek, a
hatred of Aztechnology that goes back to the death of his mother and the taking of his father, and a
life debt to the brother who nursed him back from the alley where an Aztlan death squad left him.
He puts a call on the Shadowlands board at two in the morning, pays a heavy finder's fee, and meets
the runners in a stripped black van outside **Al's Stuffer Shack** at 3rd and West at 03:15: 5,000
nuyen each (1,000 up front) for the car undamaged by 05:00, half that by 06:00, 1,500 more each for
the thief. He is unarmed and unarmored and does not much mind if the team kills him.

Al's security cameras and the ork owner's memory give the team Heather, Bennett and the gang colors.
The garage is a dead three-pump filling station with a collapsed roof, two nervous sentries walking
parallel circuits, three watchers orbiting at forty meters and the glowing car up on the one working
lift. Heather casts Analyze Truth and negotiates: she will sell the car back for 15,000 nuyen, she
will hand it over rather than see her punks tortured by Aztech, and she will die before she lets them
be taken. The moment the runners settle with her -- whichever way -- an amplified voice announces
**Lt. Jose Ramirez of the Aztlan Jaguar Guards**, thirty seconds and then gas grenades, because
Rollo has hedged his bet. The runners can hand the car to Lucien, run it to the Tir with Heather and
her wolf-shaman mentor **Tarn**, or sell it to any AAA that dares and earn Aztechnology as an enemy.

## Timeline

- **23:00, the night before** -- Edmundo Castellian finds the theft on the security tapes, hacks the
  security database to confirm it, and phones his brother Eduardo. The car left the parking deck
  earlier that evening.
- **Earlier that night** -- Rollo, in a hat and coat that beat the cameras, hands Heather the keys in
  Al's Stuffer Shack parking lot and walks out of shot into a waiting cab. Bennett pops the hood,
  finds the Aztechnology GPS beacon, tears it out and drops it in the lot; the two drive off in a car
  glowing like a spotlight.
- **02:15** -- the comm rings. A familiar face with a familiar smile: a job. The team has an hour,
  enough for a few phone calls about Lucien (Legwork).
- **03:15** -- the meet at 3rd and West, Puyallup, outside Al's. Perception (hearing) TN 4 notices
  that the normal night noise of the barrens is missing -- the gangers are sequestered in their
  garage. Briefing, 1,000 nuyen each up front.
- **03:15-05:30** -- Al's Stuffer Shack (cameras, the credstick scanner, the broken beacon in the
  lot), legwork on the Sidhe Devils (Etiquette Street 6, minus 2 with Ancients contacts) and the
  garage blueprints (Computer TN 4+TR, TN 3+TR through city hall; one success in an hour, ten
  minutes off per extra success).
- **05:00** -- Lucien's deadline. Full pay, 5,000 nuyen each.
- **05:30** -- if nobody has interfered, the Sidhe Devils finish mapping their route; Heather calls
  the gang to mount up and they are on the road inside two minutes, with a car that can outrun almost
  anything. Heather is also waiting on a callback that will not come until 05:30.
- **06:00** -- the late deadline. Half pay, 2,500 nuyen each.
- **The moment the garage is resolved** -- the Jaguar Guards announce themselves and give thirty
  seconds before the gas grenades.
- **08:00** -- the Aztechnology board of directors meets at the testing track to see the Amanecer
  unveiled at sunrise. Marketing thought it would be symbolic.
- **After** -- the fixer who set the run up gets quiet thanks from Aztechnology and is bumped from
  connection 1 to 2; teams who sell the car elsewhere collect a Corporate Favor and Enemy:
  Aztechnology.

## NPCs (Persons of Interest)

| Name | Role | Org |
|---|---|---|
| Eduardo "Lucien" Castellian | The Mr. Johnson -- an Aztlan-born fixer who hates Aztechnology and is spending his brother's blood money to save his brother's life | independent |
| Edmundo Castellian | The Aztechnology engineer framed for stealing his own prototype, footing the bill for the run with what his brother calls blood money | independent |
| Jackson Rollo | Edmundo's lead assistant -- the thief who wore his boss's face, parked the car with a gang, and tipped the Jaguar Guards to make himself the hero | independent |
| Heather | Elf dog shaman leading the Sidhe Devils, holding a stolen prototype she means to gift to Tir Tairngire; a contact who owes fetishes if the runners help her escape | independent |
| Bennett | Heather's boyfriend and the Sidhe Devils' mechanic -- the one who found the beacon, opened the hood and realized what the gang had stolen | Sidhe Devils |
| Al Preswick | Owner of Al's Stuffer Shack -- bluster, a baseball bat, a security system and everything the team needs to find the gang | independent |
| Lt. Jose Ramirez | Jaguar Guard lieutenant who surrounds the garage on Rollo's tip and gives everyone inside thirty seconds | Aztlan Jaguar Guards |
| Tarn | Heather's mentor -- an elf wolf shaman with real contacts inside the Tir, and the reason the escort scene has an ending | independent |
| Maurice "Butcher" Bigio | Mafia capo with a weakness for Al's soyburgers, and an optional very bad complication for a team making a scene at a protected business | Seattle Mafia |

## Locations

| Name | Type | District | Notes |
|---|---|---|---|
| Al's Stuffer Shack | convenience store | Puyallup | The Puyallup Stuffer Shack at 3rd and West where Rollo handed over the keys, where Lucien holds the meet, and whose cameras and credstick scanner hold everything the team needs to start |
| The Sidhe Devils' Garage | gang territory | Puyallup | The burnt-out three-pump filling station where the gang has the Amanecer up on the one working lift, guarded by two green sentries and three watchers |
| Aztechnology Prototype Vehicle Facility (Seattle) | research lab | Downtown | The plant where the Amanecer 5000 was built and stolen -- an underground parking deck, a work floor with a multi-billion-nuyen gap in the middle, and the lower labs nobody comes back from |
| Aztechnology Seattle Testing Track | corporate facility |  | Where the Aztechnology board of directors gathers at 08:00 to watch a glowing car they may not have |
| Tarn's Home (Puyallup) | residential community | Puyallup | The wolf shaman's house in a better part of Puyallup -- Heather's first stop with the car, and the one neighborhood in this adventure where Lone Star answers a call |
| Telestrian Pickup Point (Salish Border) | smugglers den | Salish-Shidhe border country | Specific coordinates a mile past the Salish border where a Tir Banshee collects the car, the shamans and the gang |

## Organizations (new)

| Name | Type | Tier | Notes |
|---|---|---|---|
| Sidhe Devils | go-gang | 1 | A small Puyallup gang of elf posers -- five to seven surgically elf-ified humans behind a real elf dog shaman -- who accidentally end up holding a multi-billion-nuyen Aztechnology prototype |
| Aztlan Jaguar Guards | military unit | 5 | Aztlan's elite troops, called in by Jackson Rollo to take the prototype back from a gang of teenagers -- gas first, then rifle fire on anyone who leaves cover |

## Existing organizations updated (sourced appends, nothing overwritten)

- **Aztechnology** -- GM notes; enemies: Sidhe Devils
- **Aztlan** -- GM notes
- **Tir Tairngire** -- GM notes; allies: Telestrian Industries
- **Salish-Shidhe Council** -- GM notes
- **Lone Star Security** -- GM notes
- **Seattle Mafia** -- GM notes; leadership: Maurice "Butcher" Bigio
- **Telestrian Industries** -- GM notes; allies: Tir Tairngire
- **Ancients** -- GM notes

## Existing locations / NPCs updated

- location: **Aztechnology Pyramid**
- location: **Salish-Shidhe Border Post (Seattle crossing)**
- location: **Huitzilopochtli Plaza**

## Matrix systems -- to build in the Matrix designer (NOT built yet)

There is no decking scene in this adventure -- the Matrix work is short, opportunistic and mostly
happens on other people's small systems. Four systems are worth building if the GM wants them.

### Al's Stuffer Shack security system

A franchise fast-food package: interior cameras covering the restaurant, exterior cameras covering
the parking lot, rating 3 maglocks on the Plexiglas doors, and a separate rating 3 credstick scanner
at the counter. No host rating is printed. Access in play is by Electronics (3) to review the
footage, or Perception (4) to spot the cameras in the first place; the scanner has to be hacked
without Al Preswick noticing, and it still holds the personal information of the corporate suit who
handed the car keys over earlier that night. The footage cannot be made to give up Jackson Rollo's
face -- the hat and coat beat every angle -- but yields stills of the car, Bennett and Heather.

### The Aztechnology facility security database

Never entered by the runners; the theft footage the whole plot hangs on comes from Edmundo
Castellian hacking his own building's security database in the hour after he realizes what has
happened. It holds the parking-deck entry, the greeting from the guard, the drive-out and the pass
check -- and survives magnification at every level Edmundo can apply, with no extra wrinkles around
the eyes and a perfect voice-pattern match. Treat it as a corporate security host at whatever rating
the campaign uses for Aztechnology; a team that decked it directly would short-circuit the entire
adventure.

### Seattle city hall permit and blueprint archive

The source of the garage blueprints (Handout). Computer test at TN 4+TR, dropping to TN 3+TR for a
contact inside city hall. One success retrieves the blueprints in an hour; each additional success
cuts ten minutes off the retrieval time. No IC or alert structure is given -- this is legwork, not
an intrusion.

### The Shadowlands board

Lucien puts the call for a rush team out on Shadowlands at about two in the morning and agrees to
pay a heavy finder's fee for any reliable runners who can be produced on that notice. The deckers
who take the call are the ones who contact the player characters, which is why the adventure's
reward table hands the credit -- and an increase from connection 1 to connection 2 -- to the contact
who arranged the run rather than to the team.

### The Amanecer 5000's GPS beacon

An Aztechnology-stamped locator beacon, roughly six inches square, torn out of the car by Bennett in
Al's parking lot and left broken on the ground; Perception (6) finds it, Electronics (4) identifies
it. Its last transmitted fix is the reason Lucien holds the meet at the Stuffer Shack. Note the
book's own contradiction: Heather believes the car still carries a live tracking device and cannot
work out why it has not been activated.

## Flavor / not built

- **The Amanecer 5000** -- the prototype itself, a machine rather than a character. Hand 2/7, Speed
  380 (limited to 80 in city driving), Accel 21, Body 3, Armor 0, Sig 2, Auto 0, Sensor 2, Cargo 5,
  Load 50, Seating 2, Entry 2, Fuel EC, Econ 24 km/l. A bronze-steel alloy body coated in dikote that
  acts as a superconductor over titanium-steel wheels dikoted as insulators; the engine's excess
  current runs through the outer frame and makes the car glow whitish-blue whenever it is running,
  obvious from 150 meters. Current cracks water vapor as it goes, feeding hydrogen back into the fuel
  canister and shunting the oxygen into the cabin. The voltage is high but the resistance too high to
  hurt anyone -- touching it is a carpet-and-doorknob shock. The windows are synthetic diamond,
  specially tinted so as not to disrupt conductivity, and act as one-way mirrors. It has not been
  fully speed-rated, so the top of the engine is unknown. Kept in the garage and facility notes.
- **The parking-deck guard** who says "Welcome Back Mr. Castellian" -- unnamed, and the only reason
  the frame-up failed. Folded into the Aztechnology Prototype Vehicle Facility notes.
- **The Aztechnology marketing man** who scheduled a sunrise unveiling because the car is called "the
  dawn" -- quoted, never named. Folded into the testing track notes.
- **The Telestrian Banshee crew** -- competent, faceless, and given no statistics; they take everyone
  into protective custody until the story checks out. Folded into the Telestrian Industries notes.
- **The Salish border guards and the Yellowjacket reinforcements** -- an instruction to the GM
  ("elite troops armed at least as well as the Jaguar guards") rather than a cast entry. Folded into
  the Salish-Shidhe Council and border post updates.
- **The cab driver** who collects the suit outside Al's after the handover -- one line in the street
  legwork table.
- **Leyland-Rover, Harley-Davidson, Ares, GMC, Chrysler-Nissan** -- manufacturer name-drops on gear
  and vehicles only.
- **The Shadowlands deckers** who answered Lucien's call and passed the job to the runners -- the
  book deliberately leaves them as the players' own existing contacts, and explicitly warns the GM
  not to use the standard SRM NPCs (Fox, Joey and company) for the introductory contact.

## GM play notes

- Three and a half hours of play in a four-to-five hour slot, with 15-20 minutes at the end for
  Debriefing Logs. Everything runs on one clock: 02:15 the call, 03:15 the meet, 05:00 full pay,
  05:30 the gang leaves, 06:00 half pay. Keep close track of elapsed time -- the whole adventure is
  built on the deadline, and the Debugging notes warn repeatedly that legwork detours (especially a
  team with no Electronics skill carrying Al's security data elsewhere) will eat the window.
- The opening is atmosphere, not threat: the barrens around 3rd and West are near-silent because the
  gang is sequestered in its garage, and a Perception (hearing) TN 4 test tells the players that the
  normal night noises are missing. Lucien did not stage it. If you play music, horror-movie
  background is suggested. Let the team be weirded out before they spot each other.
- The Jaguar Guards trigger on resolution, not on a clock. Whatever way the garage ends -- a purchase
  at 15,000 nuyen, a bluff, a threat, a massacre, an alliance -- Lt. Ramirez's amplified voice comes
  a moment later. If the gang is alive and friendly they fight alongside the runners; if not, it is a
  three-way firefight. The Jaguars are elite: do not try to kill the party, but scale up if the table
  can take it, and for a full effect give them an Ares Citymaster and a rigger.
- The moral choices are the point and the karma table says so: taking the car from the Sidhe Devils
  without violence is worth a point, standing by while the Jaguar Guards slaughter the gangers costs
  one, delivering the car to Lucien is worth one and delivering it to Tir Tairngire is worth two.
  Maximum six good karma including three for roleplaying.
- Heather is written to be negotiable in every direction and immovable on one point: her people go
  free. She casts Analyze Truth as a matter of course, so lying to her is a contest, not a
  formality. A team that presents itself as Aztechnology can extort her; a team that is obviously
  stronger can force her; neither gets her gang.
- Following the Leader is optional and explicitly a time-filler. Run it only if the team sided with
  Heather and there is session left. Remember the Amanecer is a two-door two-seater -- Heather and
  Tarn ride in it and everyone else is on a Scorpion.
- Selling the car elsewhere is allowed but expensive: any AAA will take it, nothing smaller will
  risk Aztechnology, and the team collects both the "A Corporate Favor" and the "Enemy:
  Aztechnology" handouts. Note them on the Mission Record Sheets. Any shadowrunner should know the
  car is far too flashy to keep.
- If the players refuse the job at the van, hand them their event log and end the session -- the
  book's own Debugging instruction.

