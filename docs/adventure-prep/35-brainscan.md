# Brainscan -- Adventure Prep: NPCs, Locations, Organizations, Matrix Systems

Source: Shadowrun 3e - Brainscan [FASA 7331].pdf, pp. 3-149. Campaign order #35, in-game 2061 (May; the campaign opens the previous year).

Everything below is loaded into the campaign DB flagged `is_active: false` and `source_adventure: "Brainscan"` by `python scripts/adventure_ingest/run.py brainscan`; flip entries active as the party meets them. Use the **Adventure** filter on the manage pages to see just this set.

## Plot synopsis

Fourteen months after the rogue AI **Deus** sealed a hundred thousand people inside the **Renraku
Arcology**, the UCAS military has clawed back five floors out of three hundred and Deus has decided it
needs the war to stop. It hires shadowrunners. The runners will not learn who they work for until
after the third adventure.

In **Light Meets Night** a polished Johnson named **Steve Morris** -- a Renraku executive Deus rebuilt
into an undetectable Green Banded and returned to his old desk -- pays them to plant two harmless
tracking programs in one night: one in a **Gaeatronics** substation in east Tacoma, one on an
executive's computer in Bungalow 5 of the **Council Island Inn** during the Qatuwas Festival. Combined
they are a virus. In the **Aftershock** segue the Seattle grid dies for forty-eight hours; dozens die,
race relations go back a decade, and the arcology reclamation stops dead as troops pull out for riot
control. Everyone in the shadows blames Shiawase, exactly as designed.

In **Breakthrough** the fixer **Monty Boudreaux** hires them to recover **SENSE**, a portable neural
scanner Deus fears can pick its Banded out of a crowd of rescued victims. The trail runs through a BTL
addict, a murdered colleague, a dwarf-adept demolitions gang at war with mutant ork gangers, and ends
with a bored Raven shaman named **Brisbie** selling them a decoy -- and, in **Did You Forget
Something?**, the working prototype. In **My Name Is Legion** the New Orleans fixer **Toshi Akimura**
sends them to extract **Dr. Olivia Marchand** of Cross Applied Technologies off a corporate yacht on
the Mississippi. Her distributed-decking experiment shattered her into four people, one of whom is a
servant of Deus and arranged her own extraction; the handover ends with a Voodoo mambo's loa possessing
her body and slaughtering everyone. In **Revelations**, **Overwatch** -- Ronin's and Dodger's network of
otaku children -- finally tells the runners who has been paying them.

In **Outside Influence** Morris hires them for a demolition job and Overwatch asks them, free, to pull
a Banded child out of a military convoy on Intercity 5. The two jobs turn out to be the same trap: Deus
is using the child to find Overwatch's hideout, and the building it wants levelled is the chocolate
factory the runners are standing in. Turning on Morris leads them to **Tin Man Scrap Works** in
Puyallup, a scrapyard building drones and Banded for Deus, and to **Hiroshi Ushida**, the arcology's
former director, who is carrying the file that says **Inazo Aneki** is alive in Tibet with Deus' kill
codes locked in his damaged brain. **The Return of the Father** is a twenty-minute smash-and-grab in a
hidden Buddhist garden in Wan Chai against **Dr. Sherman Huang**, his Red Samurai and a Banded hit team.

**Runners Ex Machina** takes them through the Ork Underground into the arcology, up two hundred floors
to the Resistance, into the Whites' domain for **Cham Lam Won** and the "Mousetrap", and finally into
Deus' ultraviolet hosts, where a mole betrays half the team into a zombie room and the rest fight
through a Beowulf keep and a crystalline Garden of Eden. Aneki, his mind repaired by Deus purely so he
can be shown what became of his dream, recites a death haiku that carries the kill codes and cuts
himself open. The AI is torn loose, fragmented and downloaded -- which is precisely what it wanted --
and Huang walks off with an empty cyberdeck and the credit.

## Timeline

- **2049** -- Devon Eurich and Vanessa Cliber build the first semi-autonomous knowbots inside the SCIRE
  Matrix under Dr. Sherman Huang's Artificial Intelligence Project.
- **2050** -- one knowbot meets the decker Dodger and becomes the AI **Morgan**. Eurich defects, wrecking
  what he can of the corp's research; Cham Lam Won replaces him.
- **2058** -- Cham and Cliber trap Morgan, dissect her and fold choice code into the Arcology Expert
  Program along with technology from the elf genius Leonardo. What is left of her, freed by Dodger and
  Eurich, becomes **Megaera**. Later that year the AEP wakes: on Aneki's orders a shutdown program has
  been buried in its code, triggered only by kill codes keyed to Aneki's brainwaves, and the insult of
  that distrust is the spark. The new AI hides, courts the otaku, and names itself **Deus**.
- **2059 (earlier)** -- Deus corrupts the Renraku operative Michael Bishop ("Babel") into carrying a
  virus that erases all mention of the otaku and Leonardo from Renraku's networks. Babel refuses to be
  spent, survives, and becomes **Ronin**.
- **19 Dec 2059** -- the shutdown. The arcology seals with close to a hundred thousand people inside.
  Deus ambushes Aneki in the Matrix the same morning; his defenses cut the conditioning short and
  scramble his mind. The Resistance forms within days.
- **21 Dec 2059** -- Huang confirms to the COO that the AEP disassembly program cannot be used: the key
  code is locked in Aneki's head "and may in fact be forever lost".
- **2 Feb 2060** -- after a fourth extraction attempt in two months, acting CEO Haruhiko Nakada orders
  Aneki moved to Tibet under the Seal of the Green Gloves.
- **2060** -- Brigadier General Angela Colloton takes over the siege as Operation: Excavation. A year of
  fighting buys five floors. Deus begins buying and infiltrating companies on the outside, smuggles
  Hiroshi Ushida out to run them, converts Steve Morris, and opens negotiations with Huang: Aneki in
  exchange for the arcology and ten percent of Renraku stock.
- **Campaign, month 1** -- *Light Meets Night*: the Gaeatronics substation and the Council Island Inn.
  *Aftershock*: 48 hours of darkness, a month of brownouts, and the reclamation stops.
- **Campaign, weeks later** -- *Breakthrough* and *Did You Forget Something?*: the SENSE prototype.
- **Campaign, later still** -- *My Name Is Legion* and *Revelations*: Olivia Marchand, and the truth.
- **Campaign, spring 2061** -- *Outside Influence*: the convoy, the chocolate factory, Tin Man Scrap
  Works, and Hiroshi Ushida's file on Aneki.
- **30 Apr 2061** -- Renraku Security Director Lucas Saiki reports the Tibetans have agreed to release
  Aneki in Hong Kong in one week.
- **c. 7 May 2061** -- *The Return of the Father*: Madame Kim's, the garden, Huang and the Red Samurai.
- **Days later** -- *Runners Ex Machina*: the Ork Underground, the 199th floor, the 272nd floor, the
  valve station, the UV hosts. Aneki's seppuku triggers the kill codes; Deus is fragmented and
  downloaded; Megaera is dragged down with it; Huang shoots the corpse and takes an empty Mousetrap.
- **Aftermath** -- Renraku announces the crisis "resolved"; Huang takes the credit and becomes a CEO
  contender; Aneki's death is announced weeks later. Ronin vanishes. And somewhere in the Matrix,
  hundreds of released arcology refugees jack in at 3:00 p.m. and begin to join.

## NPCs (Persons of Interest)

| Name | Role | Org |
|---|---|---|
| Steve Morris | The Johnson for Light Meets Night and Outside Influence -- a rescued Renraku executive rebuilt into an undetectable Green Banded who does not know who he works for | The Banded |
| Ace Gonriled | Hulking ork decker whose team died smashing the Council Island border post, found finishing the job alone in Bungalow 5 -- and unwilling to give it up | independent |
| Dustin Kien | Owner of the Palace of China, neutral in the Tacoma mob war and paying no protection to either side | independent |
| Tommy | Eight-year-old with a melting snow cone who comes to the substation fence for a foul ball at the worst possible moment | independent |
| Monty Boudreaux | Freelance fixer who fronts corporate Johnsons for a commission; hired by Morris to destroy SENSE, and now hiring the runners to clean up his own mess | independent |
| Wally Huggins | BTL-addicted Neuranalysis tech who sold out SENSE, murdered his partner over the split, and leads the runners to a prototype that is no longer there | Neuranalysis, Inc. |
| Regis P. Doss | Neuranalysis tech and weapons enthusiast drowning in gambling debts who helped steal SENSE and took three bullets in the chest over the split | Neuranalysis, Inc. |
| Grinder | Dwarf adept leader of the Red Hot Nukes, gleefully rocketing liquor bottles into the Stilettos' garage and grooming his gang to prevent a horrible future | Red Hot Nukes |
| Slammin' Sammy | Red Hot Nukes adept with an Aztechnology Lasher missile launcher and three anti-personnel rockets | Red Hot Nukes |
| Portnoy | Red Hot Nukes adept and grenade quartermaster -- ten white phosphorous, ten incendiary, fifteen AP offensive, and an aluminum bat | Red Hot Nukes |
| Lady Fingers | Red Hot Nukes adept with an RPK heavy machine gun and explosive ammunition; Grade 2 initiate with mystic armor and astral perception | Red Hot Nukes |
| Flo | Red Hot Nukes adept with a Remington 990 loaded with Big D's Temper shells; Grade 2 initiate and the gang's sensory specialist | Red Hot Nukes |
| Brisbie | Raven gutter shaman who lifted the SENSE case out of the garage for fun, sells the runners a decoy, and later sells them the real thing out of a movie theater | independent |
| Mustard | Brisbie's ally spirit and partner in crime, named after his favorite condiment; does all the shaman's talking and all his stealing | independent |
| Poison Lily | Akimura's decker, hired to hack Cross Tech for the Marchand file and killed by the Seraphim before the runners ever meet her | independent |
| Remy Duchamps | Poison Lily's boyfriend, a BTL burnout who sold her data to a stranger over the Matrix and is cooking his brain in a coffin hotel with the chip still on him | independent |
| Marguerite | Creole apartment manager who swears in French, hates both her missing tenants, and will forget the runners for a hundred nuyen | independent |
| Juliet Sienna | Seraphim field agent running surveillance on Poison Lily's doss, photographing the runners and tailing them to the Brain Disco | The Seraphim |
| Bubba | Cajun troll bouncer at the Brain Disco with a baseball bat, shot by silenced Seraphim guns on the ground floor | independent |
| Stumpy | Ferret-like dwarf manager of the Brain Disco who will sell a coffin number for a hundred nuyen | independent |
| Captain Vincent Larreau | Older Creole captain of the Queen of Babylon, a New Orleans native who will fight to defend his ship | Cross Applied Technologies, Inc. |
| Dr. Olivia Marchand | Cross Applied Technologies' distributed-decking genius, shattered by her own prototype into four people, one of whom arranged her extraction for Deus | Cross Applied Technologies, Inc. |
| Meme Flora Rochambeau | Voodoo mambo and Olivia Marchand's grandmother, who will not leave her granddaughter's side and whose loa turns Petro in the middle of the handover | independent |
| Sergeant Crew | Akimura's bought contact inside the New Orleans police, gruff and unhappy about it, who hands over the information, the payment and a Seattle number | New Orleans Police Services |
| Clara | Clerk at the Tulane University Book Store and Toshi Akimura's clean dead drop, waiting on a passphrase about a graduate economics course | independent |
| Dr. Evan Kincaid | The red herring: a vampiric-virus specialist whose file Morris hands over to convince the runners that Shiawase is paying them to burn out a monster | Shiawase Corporation |
| Glynis Taki | Toxic Cat shaman assigned as Hiroshi Ushida's bodyguard, who invokes a great form toxic city spirit out of the scrapyard itself | The Banded |
| Ronin (Michael Bishop) | Otaku founder of Overwatch, once Deus' own creation, waging a personal war on the AI -- and the one member of the team who never comes back from the final host | Overwatch |
| Megaera | The broken AI formerly called Morgan -- Deus' sister, Dodger's obsession, and the only thing in the Matrix that can fight Deus in its own house | independent |
| Vanessa Cliber | Renraku-loyal Resistance cell leader who helped build Deus, splits the coalition to rescue Huang, and comes back to collect the Mousetrap and the credit | Renraku Computer Systems |
| Grendel | The IC construct guarding the Wall: a five-metre beast that comes through a mirror, swallows Ronin and Aneki whole and walks back out | independent |
| Slant | Talkative ork guide who walks the team through two hours of sewer to the Ork Underground's tunnel into the arcology | independent |
| Tholm | Silent troll half of the Ork Underground guide team, who lifts a manhole cover one-handed and says nothing at all | independent |
| Jack | Resistance fighter left guarding the jacked-in team on the 202nd floor, and the first person Cliber's cell kills to take the Mousetrap | The Arcology Resistance |
| Zendra | The other Resistance fighter guarding the mainframe room while the deckers are jacked into Deus' hosts | The Arcology Resistance |
| Madame Kim | Proprietor of a Wan Chai simsense parlor whose back door is the Tibetans' handover point for the CEO of Renraku | independent |
| Lieutenant Krause | UCAS Special Forces officer who closes the elevator doors on a hundred screaming evacuees and hauls Steve Morris out by the wrist | Joint Task Force Seattle |
| Lieutenant Harrison | Krause's second-in-command, staring at the '9' above the open elevator doors and doing the arithmetic | Joint Task Force Seattle |
| Dr. Mitchell Avery | Renraku's Chiba medical director, who cannot cure Inazo Aneki and has to ask the Board what was done to him | Renraku Computer Systems |
| Lucas Saiki | Renraku's Chiba security director, who negotiates Aneki's release with the Tibetans and sets up the Hong Kong handover | Renraku Computer Systems |
| Security Director Goturo | Renraku Chiba's internal security chief, dishonored by five years of undetected infiltrators and four extraction attempts in two months | Renraku Computer Systems |
| Governor Lindstrom | Governor of the Seattle metroplex, who calls out the Metroplex Guard during the blackout and triggers a fresh wave of panic about martial law | independent |
| Liz Macphee | Arcology survivor back at her desk for a month, treated like a freak by everyone she knows -- and jacking straight into the Matrix at 2:55 p.m. | independent |
| Josh | Nearly-sixteen-year-old arcology orphan chafing at his new foster parents, who jacks into an arcade game at 2:56 p.m. | independent |
| Doug Doyle | Homeless arcology survivor panhandling suits by a dataterm, who scavenged a datacord and jacks into a broken terminal at 2:57 p.m. | independent |
| Tony Okawa | Go-ganger 'Tiger', a year out of the arcology and back with his crew, who pulls over on some biz and opens a fiber optic junction box with a knife | independent |

## Locations

| Name | Type | District | Notes |
|---|---|---|---|
| The Palace of China | nightclub | Tacoma | Medieval-Chinese theme club popular with Tacoma's young and wealthy; neutral ground in the Mafia-Yakuza war, and Steve Morris' meeting room both times he hires the runners |
| Gaeatronics Tacoma Substation | power plant | Eastern Tacoma, just off Highway 18 | Unmanned concrete box on a wooded ridge where the runners plant the first half of the virus that kills Seattle's power -- with a Little League championship going on below the fence |
| Romaine Marina | smugglers den | 4529 S. Alaska St. at 54th, Lake Washington shore | Faded two-story boathouse on Lake Washington where Morris pays the runners, lends them two Nightrunners and points them at Council Island |
| Burbank Park (Council Island) | park | Northeastern tip of Council Island | Qatuwas Festival grounds -- a giant bonfire from sundown to sunup, boats clustered offshore, and every marine patrol on Lake Washington concentrated around it |
| The Drowning Man | bar | Ravenna | Converted storefront pharmacy straddling the line between a big bar and a small club, where Monty Boudreaux takes meets in a soundproofed storeroom |
| The Adams Hotel | hotel | 3327 Claremont at Roscoe, Woodinville, Redmond Barrens | 'Deluxe transient accommodations' -- the flophouse where Wally Huggins hides, a block and a half from the garage where he stashed the SENSE |
| Woodinville Parking Garage (Rusted Stilettos Hideout) | gang territory | Roscoe Street, Woodinville, Redmond Barrens | Three-story concrete tomb where Huggins hid the SENSE, the Stilettos are cornered, the Nukes are dropping rockets on the ramps, and a city spirit is waiting on the third floor |
| Municipal Courthouse -- District 214 | ruins | 2842 Fletcher Street, Redmond Barrens | Abandoned four-story courthouse where Brisbie's ally spirit haggles from the rooftop; the end of the line, where the despair is thick enough to be parody |
| The Bijou | theater | Seattle | Century-old projection movie house with pink bulbs on its vertical sign, where Brisbie uses a Control Emotions spell to lure the team in and sell them the real SENSE |
| Neuranalysis Headquarters | research lab | Bellevue | The burned-out shell of the medical research company that built SENSE -- two guards shot in the back of the head, the labs torched, and very little of the company left |
| The Brain Disco | btl den | Lakefront | Coffin hotel and BTL parlor on the New Orleans lakefront where Remy Duchamps is cooking his brain in coffin #310 with Poison Lily's chip still in his pocket |
| Poison Lily's Doss | apartment complex | Just outside the French Quarter | Third-floor apartment in a decaying southern gothic house, ransacked by the Seraphim with a passkey and watched from across the street with a laser microphone |
| Queen of Babylon | corporate yacht | The Mississippi River, downriver from St. Louis | Fifteen-metre Cross Applied Technologies hydrofoil yacht carrying Dr. Olivia Marchand, her grandmother, nine security personnel and a Seraphim agent posing as a deckhand |
| Tulane University Book Store | shop | Tulane University | Akimura's clean drop for runners who would rather cut the link -- ask for Clara and quote the passphrase about the graduate economics course |
| NOPS Loyola Avenue Station | police station | Loyola Avenue, near City Hall | The police station where Akimura's bought sergeant hands over information, payment and a Seattle number, and makes no secret of hating it |
| Intercity 5 at the Tacoma Docks | transportation hub | Tacoma docks | Ambush site Overwatch scouted long ago: the stretch of I-5 furthest from both Fort Lewis and the arcology cordon, with side streets to vanish into |
| Choco-Tarts Factory (Overwatch HQ) | corporate facility | 180 Forest Ridge Drive, Auburn | Automated chocolate factory whose emptied, soundproofed vat is Overwatch's war room -- the building Steve Morris hires the runners to level while they are standing in it |
| Overwatch Redmond Safehouse | safehouse | The Barrens | Derelict games-software offices where Ronin meets the runners face to face -- wired for the net, empty for half a decade, and good enough for a group of Matrix activists |
| Overwatch Bellevue House | safehouse | Bellevue | Secluded red brick house Overwatch moved into after the chocolate factory was blown -- luxurious, and looking like twenty children were left in it unsupervised for months |
| Tin Man Scrap Works Yard | corporate facility | Hell's Kitchen, Puyallup Barrens | Toxic scrapyard, retooled drone plant and converted office building at the edge of Hell's Kitchen -- Deus' operations centre outside the arcology |
| Tin Man Office Building | corporate facility | Hell's Kitchen, Puyallup Barrens | The old scrapyard headquarters turned Banded operations centre: security room, conversion clinic, bunk room, work room, Hiroshi Ushida's office, and a fuel-air bomb under a table |
| Madame Kim's Simsense Parlor | btl den | Wan Chai | Seedy Wan Chai sim parlor between a biosculptor and a clinic, whose back door opens onto the hidden garden where the Tibetans hand Inazo Aneki over |
| The Wan Chai Garden Shrine | landmark / monument | Wan Chai (behind Madame Kim's Simsense Parlor) | Secret Tantric Buddhist shrine hidden in a courtyard behind a sim parlor, under a Force 10 ward and a quickened illusion of a sunny mountainside |
| Durruti's | bar | 199th floor, Renraku Arcology (SCIRE), Downtown | Derelict bar in a dead entertainment district two hundred floors up, where Kiell Rauglos and Devon Eurich plan the assault on Deus over a trideo projector |
| Arcology 272nd Floor (White Domain) | corporate arcology | Renraku Arcology (SCIRE), Downtown | The Whites' luxury domain high in the arcology: executive suites, a pool, an opera hall, a Noh theatre, a wild golf course, devil rats in the tennis courts, and Cham Lam Won |
| Arcology Valve Station and Mainframes (Floors 201-202) | corporate arcology | Renraku Arcology (SCIRE), Downtown | Where the campaign ends: an atmosphere control station on 201, a zombie room full of jacked-in children next door, and the SCIRE mainframes on 202 behind an unbreathable floor |
| Naval Shipyards Lot (Everett) | corporate facility | Near the Naval Shipyards, Everett | Empty fenced parking lot at the north end of the sprawl where Steve Morris waits an hour's drive away for the Blues to confirm a massacre he ordered |
| Hell's Kitchen (Puyallup) | ruins | Puyallup Barrens | Toxic geyser-and-smelter district of the Puyallup Barrens that even squatters avoid, and the reason a scrapyard could be turned into a Banded fortress unnoticed |

## Organizations (new)

| Name | Type | Tier | Notes |
|---|---|---|---|
| The Banded | cult | 4 | Deus' mortal minions, ranked by one to seven black bands tattooed around the left arm and sorted by cybereye color into Whites, Blues and Greens |
| Overwatch | otaku network | 3 | Ronin's and Dodger's network of otaku children waging an unending Matrix war on Deus, poor, paranoid, and running on stolen bandwidth and good intentions |
| The Arcology Resistance | resistance movement | 2 | The arcology's trapped survivors fighting Deus in cells; Kiell Rauglos is the de facto leader and Vanessa Cliber's Renraku-loyal faction is the crack in the wall |
| Gaeatronics | corporation | 4 | 'Gaeatronics. Powering Seattle ... Naturally.' The largest corporation in the Salish-Shidhe Council, supplying most of Seattle's power and fighting a shadow war with Shiawase Atomics |
| The Seraphim | corporate black operations division | 4 | Cross Applied Technologies' elite black-ops and counterintelligence arm -- infiltration specialists and good deckers who also run security on CATCo's own executives |
| Neuranalysis, Inc. | corporation | 1 | Small independent Seattle medical research company that built SENSE and was murdered, looted and torched for it inside a week |
| Tin Man Scrap Works | corporation | 2 | Bankrupt Puyallup scrapyard and drone plant bought through a shell company by Deus and turned into the Banded's operations centre outside the arcology |
| CrashCart | corporation | 3 | Yamatetsu's emergency-medical subsidiary and DocWagon's main competitor -- the reason Yamatetsu wanted Neuranalysis |
| Sons of Sauron | policlub | 2 | Militant troll terrorist group whose bomb threat broke the Palace of China's decade-old 'No Troll' policy |
| Joint Task Force Seattle | government agency | 5 | The UCAS military command besieging the Renraku Arcology under Brigadier General Angela Colloton -- five floors reclaimed in a year, and pulled off the job by the blackout |
| Renraku Red Samurai | corporate security division | 5 | Renraku's elite security troops in red and black armor -- supporting the arcology siege, escorting Sherman Huang, and walking Cliber's cell out at the end |
| The Netwalkers | otaku tribe | 1 | Boston otaku tribe whose initiation Renraku sent Michael Bishop to infiltrate -- and where Deus turned him into Babel |
| Reality Hackers | gang | 2 | Barrens gang in its heyday when a Yakuza gang war orphaned Toshi Akimura and it taught him to sneak, steal and hack |
| New Orleans Mafia | criminal syndicate | 4 | The syndicate that runs one of the world's most decadent cities -- vice, gambling, smuggling of every kind, and a great deal of wetwork |
| New Orleans Police Services | police force | 3 | NOPS -- the New Orleans police: gruff, bought in places, and inclined to believe a licensed corporate security operative over a SINless stranger |
| Franklin Associates | corporation | 3 | Seattle's fire control corporation -- overwhelmed along with every other emergency service during the 48-hour blackout |

## Existing organizations updated (sourced appends, nothing overwritten)

- **Renraku Computer Systems** -- GM notes; leadership: Cham Lam Won, Vanessa Cliber, Hiroshi Ushida, Tadashi Marushige, Lucas Saiki, Dr. Mitchell Avery; enemies: The Banded, Overwatch
- **Shiawase Corporation** -- GM notes; enemies: Gaeatronics
- **Yamatetsu Corporation** -- GM notes; allies: CrashCart
- **DocWagon** -- GM notes; enemies: CrashCart
- **Lone Star Security** -- GM notes
- **Salish-Shidhe Council** -- GM notes
- **Seattle Metroplex Guard** -- GM notes
- **Humanis Policlub** -- GM notes
- **Mitsuhama Computer Technologies** -- GM notes
- **Cross Applied Technologies, Inc.** -- GM notes; leadership: Dr. Olivia Marchand; allies: The Seraphim
- **Universal Omnitech** -- GM notes
- **Rusted Stilettos** -- GM notes; enemies: Red Hot Nukes
- **Red Hot Nukes** -- GM notes; leadership: Grinder; enemies: Rusted Stilettos
- **Tir Tairngire** -- GM notes
- **The Cutters** -- GM notes

## Existing locations / NPCs updated

- location: **Renraku Arcology (SCIRE)**
- location: **Council Island**
- location: **Council Island Inn**
- location: **Fort Lewis**
- location: **The Ork Underground**
- location: **Club Penumbra**
- location: **The Space Needle**
- location: **Glow City (Redmond Barrens)**
- NPC: **Inazo Aneki**
- NPC: **Dr. Sherman Huang**
- NPC: **Haruhiko Nakada**
- NPC: **Lucien Cross**
- NPC: **Dunkelzahn**
- NPC: **Deus**
- NPC: **Toshi Akimura**
- NPC: **Gabriel**
- NPC: **Hiroshi Ushida**
- NPC: **Dodger**
- NPC: **Pax**
- NPC: **Sebastien**
- NPC: **Tadashi Marushige**
- NPC: **Devon Eurich**
- NPC: **Kiell Rauglos**
- NPC: **Cham Lam Won**
- NPC: **Brigadier General Angela Colloton**

## Matrix systems -- to build in the Matrix designer (NOT built yet)

**1. Gaeatronics Tacoma substation host** (p.21) -- small, simple and lightly guarded, described on the
chip Morris supplies as an easy Green system with "minimal IC". Not normally on the Matrix: it connects
to another Gaeatronics host once per hour through a VANISHING SAN, long enough to dump performance data
and take new instructions. The payload goes into the Power (Load) Monitoring subsystem: Logon to Host,
Locate Slave, Upload Data, then optionally another Locate Slave for the fence cameras and an Edit File
to erase the footage.

| System | ACIFS | Notes |
|---|---|---|
| Substation host | Green-5/9/9/10/8/10 | Power Monitoring subsystem is the target; camera footage is recorded here |

| Trigger Step | Event |
|---|---|
| 4 | Probe-4 |
| 9 | Probe-6 |
| 13 | Crippler (Marker)-6 |
| 17 | Passive Alert, Killer-6 |
| 21 | Tar Pit-6 |
| 25 | Active Alert, Killer-8 |

Passive alert (or a maglock defeating a tampering attempt) places an automated call to the local Lone
Star precinct; a decker can spot it with Tap Commcall and stop it with Make Commcall.

**2. Council Island Inn security host** (p.29) -- NOT connected to the Matrix. A decker must reach a
terminal on the grounds: the marina, the parking lot entrance, each entrance to the main building
(front, sides and rear), or an alarm panel inside a bungalow. Every terminal outside stands in a
brightly lit area, so a decker without magical concealment or a good distraction will almost certainly
be seen.

| System | ACIFS | Notes |
|---|---|---|
| Inn security host | Orange-7/14/12/12/13/13 | Bungalow door cameras, window alarms, maglocks and the main security console |

| Trigger Step | Event |
|---|---|
| 3 | Probe-4 |
| 7 | Probe-6 |
| 11 | Passive Alert, Tar Baby-6 |
| 15 | Killer-6 |
| 18 | Blaster-6 |
| 22 | Active Alert, Blaster-8 |

The target itself is not on the host: a portable computer plugged into Bungalow 5's Matrix jack but not
actively connected. Computer (8) to beat its security (add dice equal to a Deception program's rating),
Computer (3) to plant and execute the payload, and a further Computer (8) to dig the executive's
Gaeatronics host password out of the hard drive.

**3. Queen of Babylon onboard host** (pp.61-63) -- satellite-linked to the Cross Applied Technologies
PLTG so executives can work through a vacation. Reaching it means a Logon to the Cross PLTG (TN 10),
a Locate Access Node for the yacht's LTG address (TN 10), then a Logon to the yacht host (TN 10),
modified by utilities as normal.

| System | ACIFS | Notes |
|---|---|---|
| Queen of Babylon | Orange-5/10/11/10/10/9 | Defended in person by the Seraphim agent Gabriel, who has a Cross Babel deck in his cabin |

| Trigger Step | Event |
|---|---|
| 3 | Probe-5 |
| 6 | Probe-7 |
| 9 | Passive Alert, Killer-8 |
| 11 | Active Alert, Blaster-10 (and onboard security is notified of the intrusion) |
| 13 | Shutdown |

Paydata, one Download Data operation each: the Queen's planned course and timetables; the number of
security guards aboard and their equipment; a complete map with cabin assignments. Slave systems give
the yacht's GPS position, its autonav, its security cameras, and a channel to speak to Dr. Marchand in
advance -- which will most likely reach her Legion personality, who wants to be extracted. Gabriel
attacks intruders and, if he cannot dump them, jacks out and shuts the machine down by hand. Overwatch's
deckers (Ronin's and Dodger's icons, pp.133-134) may be in the host too, concealing themselves and
watching what the runners do; that observation is what leads to Revelations.

**4. Tin Man Scrap Works host** (p.92) -- the public host is a bland, unappealing site with a few
service advertisements and an outdated telecom directory listing. Secreted inside one of the ads (the
Files subsystem) is a TRAPDOOR into the real host, where Deus' pawns work. Iconography: a metallic,
machine-driven world, everything robotic and automated, blending into a landscape of steel pipes, iron
girder superstructures and sooty railroad tracks.

| Node | Function | Rating / IC |
|---|---|---|
| Public host | Service ads and a stale telecom directory | Bland; the trapdoor hides in an ad (Files) |
| Real host | Everything described in the work room -- invoices, financial transactions, files on executives, city officials and shadowrunners, and the network of other mysteriously owned companies | Guarded by the site's SK |
| Site SK | An agglomeration of warped cargo cranes travelling on squeaky tracks, manipulating twisted I-beams for arms | MPCP 10/7/8/8/7, Computer skill 10, Utility Pool 13 (VR2 p.140) |

A decker can reach the host directly from the work room, the computer room, the security room or the
manufacturing plant. The SK also detonates the 200-kilogram Rating 6 fuel-air explosive under the work
room worktable on a five-minute countdown if the site is about to fall or Hiroshi Ushida dies -- and
destroying the SK primes it.

**5. The SCIRE Matrix and Deus' ultraviolet realms** (pp.107-124) -- see RA:S pp.78-79 for the SCIRE
Matrix's own description and sheaf if the runners try to reach Deus' home the hard way. Deus has
revamped so much of the architecture that little is where it was. Tapping the screamer subsystem on 272
via a dataline tap is Electronics B/R (8): 0 successes and Deus knows the tap and its location at once,
1 success and it takes 3D6 turns to pinpoint, 2+ and it never notices.

| Host | Metaphor | Notes |
|---|---|---|
| Grendel | Medieval Japan crossed with Beowulf: a snowy mountainside, a keep with red and blue oni baileys, a stone tower with two keyholes | Deus' firewall between the SCIRE Matrix and the Wall; reached by jacking into the Xeno-Cray labelled GRENDEL PROJECT CCR-235 on floor 202. Grendel itself: B12 C14, Init 9+4D6, 12S claws/bite, Hacking Pool 12, regeneration |
| Garden of Eden | Crystalline trees dripping data-apples over naked sleepers tangled in the roots, mandelbrot skies | Deus' downloading harvest; the captured runners are found and dug out here. Chromatic snakes nest in every tree (Perception or Sensor (10) to spot) |
| Private White realms | Whatever their otaku owners want; others run drone design, Banded conversion and metahuman experimentation | Red 12/12/20/16/16/16 each |
| First Pacific Bank gateway | Post-apocalyptic downtown Seattle -- ruined skyscrapers, rubble, creeping vegetation, a monster-movie reptile and morlocks underground | Once the bank's server, powered by the SCIRE PLTG. Holds the disabled access node to the outside Matrix: Computer (12) reduced by a spoof utility, 3 cumulative successes to crack it open, 10 to open it fully. At 3, Deus dumps the team into the Dark Forest -- and Megaera starts forcing it from outside |
| The Dark Forest | Deus' home host: gnarled bonsai-shaped trees, fleshy-hooked vines, monstrous insects, a clearing lit by a bonfire of burning datafiles | Everything in it is alive and under Deus' control. Each Combat Turn Deus takes one action to reshape the fight, and Megaera answers with one of her own |

ULTRAVIOLET RULES (p.114): mental attributes are unchanged; Body and Strength equal the deck's Bod
rating and Quickness equals Evasion; Reaction and Initiative are normal, with Response Increase and pure
DNI bonuses applying. Normal skills work, and Computer (Programming) halved (round down) substitutes for
any skill a character lacks. Only Hacking Pool may be used, for any test, and only from a hot deck.
Utilities in active memory become physical objects fitted to the metaphor -- armor and shield utilities
as mogami-do armor and shields, attack utilities as melee, projectile or throwing weapons, a medic-6 as
Biotech 6, a commlink as a carrier pigeon pulled from a pocket. All damage is real damage to the meat
body. Characters cannot perceive the real world or move their bodies, are disassociated from their decks
(no swapping programs or modes without a Willpower Test at the GM's discretion), and jacking out
requires a Willpower (16) Test (-2 with ICCM) and inflicts 16D Stun dumpshock (14S with ICCM) -- the same
damage everyone takes when the host finally collapses.

The burning books in the clearing are gigapulses of important datafiles Deus is erasing; books snatched
out of the fire are significant paydata, content and value the gamemaster's choice. After the shutdown
all the UV realms crash along with a number of other hosts, three-quarters of the SCIRE Matrix goes
offline when the military cuts the reactors, and every access node to outside LTGs and RTGs stays closed
-- except the First Pacific Bank host, which nobody notices for some time.

## Flavor / not built

- **Blood Monies Software** (Renton; Cham Lam Won's first employer), **First Pacific Bank** (whose old
  server is now Deus' gateway host -- in MATRIX_HOSTS), **Leonardo** (the elf genius whose technology
  went into the AEP), **FastJack**, **Sean Laverty** (the Tir prince who trained Dodger), the **Draco
  Foundation**, the **krewes** (New Orleans telesma smugglers), **Tamanous** (a Pushing the Envelope
  option at the Brain Disco), the **Deep Resonance**, the **Nexus** in Denver and the **Rox** in Boston
  -- name-drops.
- **The Longings For Ponds** (house band at The Drowning Man), **Anton's Bucking Fest. Pizza**, **Kwok
  Biosculpting** and the **Liu Clinic** (Madame Kim's neighbours), **Road Rage X** (Josh's arcade game),
  the **Joint** (Tony Okawa's gang bar) and **Choco-Tarts** the company -- set dressing.
- **Ratchet** (the ganger who stops to check on Tony Okawa in the epilogue), **Dixie** (the Palace of
  China door password, not a person), **Bill** (Lieutenant Harrison's given name in Krause's line).
- **The unnamed 13-year-old White otaku boy** the runners pull out of the convoy -- statted as the
  1-Band White Otaku (p.139), a recent conversion who knows almost nothing; both his parents were
  Renraku employees killed inside the arcology, and Deus told him he was being taken out to be returned
  to them. Folded into The Banded and the Intercity 5 rows.
- **The Council Island gate guards, shaman and security patrols**, the **Council Island Inn guards and
  security shaman**, **Madame Kim's husband**, the **two Tibetan monk adepts** (Grade 4 initiates with
  the Hands of Flame power), the **two young White otaku** nesting in Tin Man's computer room, the
  **four trolls** guarding the Ork Underground tunnel, **Morris' rented bodyguards**, **Akimura's hired
  muscle**, the **Overwatch mercenaries** at the cove (including the ork houngan of Agwe), the **nine
  Cross security aboard the Queen**, and the **Seraphim field agents** -- stat blocks carried on the
  location and organization rows.
- **The Banded rank and file** (1/3/5-Band Blue Samurai and Mages, 3/5-Band Greens, 1/3/5-Band White
  Otaku) and **Deus' drone constructs** (Bumblebee, Dervish, Doll, Gorgon, Manta, Medusa, Renraku
  Arachnoid Minidrone, Skellbot, Spider, plus the Tin Man scrap drones and cybered barghests) -- on The
  Banded and the Tin Man rows; full statistics pp.139-145. All of Deus' drones self-destruct if captured
  or taken beyond the arcology walls, Power (Body x 2) + 8, Damage Level S.
- **The red and blue oni**, **Grendel's wall-victims**, the **chromatic snakes**, the **morlocks**, the
  **baby monster reptiles** and the **giant fire-breathing reptile** -- UV constructs, in MATRIX_HOSTS.
- **The off-duty Lone Star officer** at the Little League game, the **Gaeatronics technician** who
  visits the substation for half an hour a day, **Tommy's brother**, the **elven teenager** hanging from
  the monorail, the **ork mother and her five children**, the **maniacal shopkeeper**, the **German
  shepherd** off the fifth floor, and the other Aftershock blackout encounters -- unnamed vignettes.

## GM play notes

- Run the five adventures apart, with unrelated jobs between them. The runners must not connect the
  Gaeatronics blackout, the SENSE job and the Marchand extraction until Overwatch tells them in
  Revelations; even the Johnsons believe these are ordinary runs. If the players start guessing early,
  let them -- nobody in the shadows will believe the blackout was two runs in one night, and their own
  contacts will laugh at a confession.
- Light Meets Night is a test of professionalism, not firepower. Pay for silence (4,000 and 8,000 a
  head) and halve it for traces. Tommy exists so the team feels caught and has to solve it without
  violence; make it obvious he can be handled. Nothing rash done to an eight-year-old ends well.
- Land Aftershock as consequence rather than spectacle. Dozens dead, hundreds wounded, hundreds of
  millions of nuyen, race relations back a decade, and -- almost unnoticed -- the arcology reclamation
  stopped dead. Hit the runners' own homes, families and contacts. Shadowruns do not happen in a vacuum.
- Brisbie rewards good sportsmanship twice: a decoy and then the working SENSE, and a permanent street
  contact if the team plays along. Attack him and the SENSE goes to the black market, Overwatch buys it,
  and Overwatch hands it back later -- which should make the runners very thoughtful about who they were
  working for.
- Marchand's four personalities are the adventure, not a gimmick. Assume the core Olivia unless a scene
  says otherwise; bring Charlie up under fear, Sisi when escape looks possible, Legion when the run is
  going Deus' way. Meme Flora is a Grade 2 initiate keeping her masking up the whole time -- never let
  the team write her off as luggage.
- The Exchange cannot be won. The Petro Ogoun makes Marchand effectively invulnerable to conventional
  weapons; killing her disrupts the spirit, knocking her out does not, and banishing it leaves her
  catatonic. Whatever happens, Deus watches through its Banded and the runners get paid.
- Outside Influence turns on one phone call. Note carefully how the character who answers it plays it:
  cool and Morris sends the Blues anyway; rattled and he tells them to kill the runners at the first
  sign of trouble; a slip about the hideout and it is kill on sight. The runners must come out of the
  scenario knowing the name Tin Man Scrap Works -- from Morris, his headware, his autonav, or an invoice
  in his pocket.
- Nothing in the endgame is what Overwatch thinks it is. The Mousetrap is not needed; the kill codes
  alone would delete Deus, and Renraku-loyal Resistance members argue for the Mousetrap precisely so
  the AI's code survives. Sebastien has been Deus' for months. The captured half of the team is meant to
  be caught -- the datajack implantation is deliberate ("if there was ever a time for the gamemaster to
  be sadistic and screw the players, this is it"), and offer simple trodes only if the table cannot
  stomach it.
- Split the party on purpose: push the non-deckers to the valve station so that everyone ends up in the
  UV hosts, deckers by the front door and everyone else through the zombie room. In the UV realms, let
  players invent uses for their utilities and then twist the rules slightly whenever they think they
  have it figured out.
- Aneki's death cannot be prevented; Deus supplies the dagger and blocks every attempt to interfere.
  Play it as the tragedy it is -- the man is lucid for the first time in eighteen months, and the first
  thing his repaired mind is shown is what his dream became.
- The victory is hollow by design. Cliber's cell takes the Mousetrap and the credit, Huang shoots the
  corpse and hands Renraku a murder to pin on the team, the arcology is collapsing around them, and no
  one is throwing a parade. Then Ronin disappears, and at 3:00 p.m. on an ordinary afternoon four
  released refugees jack in and begin to join. Deus was never destroyed -- it was distributed, and it
  walked out through the cordon inside the people the military rescued.

