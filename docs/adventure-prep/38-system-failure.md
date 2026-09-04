# System Failure -- Adventure Prep: NPCs, Locations, Organizations, Matrix Systems

Source: shadowrun-25014-system-failure.pdf, pp. 4-128. Campaign order #38, in-game 2064 (November 1-2, with aftershocks into 2065).

Everything below is loaded into the campaign DB flagged `is_active: false` and `source_adventure: "System Failure"` by `python scripts/adventure_ingest/run.py system_failure`; flip entries active as the party meets them. Use the **Adventure** filter on the manage pages to see just this set.

## Plot synopsis

Three long-running conspiracies converge on one morning in Boston and take the global Matrix down
with them. **Richard Villiers**, squeezed by his own unintegrated house of cards, by Wuxing, MCT
and Nakatomi, and above all by the vendetta of **Art Dankwalther**, does the one thing he swore he
never would: he takes **Novatech** public. The IPO trades on the **East Coast Stock Exchange** in
Boston on 2 November 2064, and the traffic it draws is the largest concentration of minds the
Matrix has ever held.

That is exactly why **Deus** chose the date. The AI finished compiling out of the thousand
metahuman **Nodes** of the Network on Halloween -- 1,342 people fall into comas the same day -- and
needs an ultraviolet host to upgrade his code before **Mirage** can come for him. His otaku cult,
**the Whites**, spent months planting backdoors in the Exchange's new host, built by Novatech
subsidiary **Matrix Systems of Boston**, whose hidden hosts happen to be Mirage's home. At 9:16 AM
Deus seizes the Exchange, trips it ultraviolet, and grows a crystalline World Tree out of the
trading floor. **Ronin**'s freed nodes and the elven decker **Dodger** wake **Megaera** inside him;
Mirage arrives as a host of angels with flaming blades. And then **Puck**, the one White with a
conscience, walks out of the crowd and sets a black egg down in the roots.

The egg is **Jormungand**, a Dissonant chimaera built by **Pax** of **Ex Pacis** to flood the
Matrix with Dissonance and remake it in her image before her own Fading kills her. To deploy it she
allied with **Winternight**, an Asatru apocalypse cult that has spent thirty years preparing to
break Loki's chains -- and the Matrix, they believe, *is* Loki's chains. The Norns **Wednesday**,
**Friday** and **Thursday** let her think she was using them. Operation: Firnbul seized power sites
worldwide to bury the sprawls under a magical winter; Operation: Jormungand seeded code eggs in
Matrix nexi from Kolkata to the Panama Canal; and Operation: Mjolnir, which Pax knows nothing
about, hangs fifteen magically modified EMP nukes in advertising blimps over the world's Matrix
junctures and buries five multi-megaton warheads on tectonic fault lines.

The Corporate Court's **Crisis Coordination Committee** gets one accidental warning -- a botched
egg-planting on Zurich's Escher-Burkli island that releases the **Surtr** nano-plague and kills
everyone in the corridor -- and decapitates Winternight at its **Valhalla** base the night before
the IPO. It is not enough: Jormungand is on a timer, and **Friday** does not break until minutes
after it launches. When she does, Zurich-Orbital chooses containment over warning, and sysops
**Atropos** and **Clothos** break comm isolation, kill a colleague doing it, and dump the
coordinates to the Denver Nexus and the shadows. **Captain Chaos** spends the last minutes of his
life spreading the word instead of saving Shadowland Seattle. Runners, not corporations, take down
half the nests and blimps.

The aftermath re-draws the world: San Francisco, Boston, Kittimat, Panama City, Stockholm, Calcutta
and Kuala Lumpur burn out under EM pulses; **Lucien Cross** dies in a jet crash and Ares butchers
CATCo; Shiawase is quietly taken over by **Korin Yamana** and **Empress Hitomi**; Dankwalther is
killed with a Thor shot; the **New Revolution** murders President **Kyle Haeffner**; Tsimshian,
Poland and Arabia change hands; Novatech merges with Transys-Erika and inherits the wireless
future. And in the wreckage, new things are waking up on the wireless test networks: children who
do not need a datajack, and Idols who ask what sadness feels like.

## Timeline

- **2029, Friday 8 February** -- the first Crash. Frida Kohlman's family dies when the Swedish
  gridlink fails; the Virus erases her records. **2031 (fall)** -- she meets Wednesday at a blot.
  **By 2034** -- the Norns are complete and Winternight is born.
- **19 December 2059** -- Deus and the Whites seize the Renraku Arcology. **11 May 2061** -- Aneki's
  killswitch fires and Deus's fragmented code downloads into ~1,000 metahuman Nodes; Megaera's code
  goes with it. **November 2061** -- Ronin recovers his own identity inside the Network.
- **2062** -- Overwatch, then Renraku/Shiawase MIFD and Transys-Neuronet, learn of the Network; Pax
  feels the onset of Fading.
- **2063: February** Deus purges disloyal nodes. **April-June** Megaera brings Mirage in; the
  repaired nodes go independent under Ronin and strike the metahuman/AI merge deal. **July** Pax's
  Jormungand vision at her tribe's Dissonance Pool. **12 November** Deus has Hitomi Shiawase
  kidnapped as a warning to Mirage and frames Ex Pacis. **December** Pax reaches a Winternight cell
  (Bangkok); the Surtr prototype is stolen from Zeta-ImpChem.
- **2064: 17 March** Novatech files for IPO. **April** ECSE upgrades begin; Jormungand is lab-tested
  and code eggs start going out. **June** Ex Pacis otaku are placed inside Kolkata Integrated Talent
  & Technologies. **August** Operation: Firnbul begins; **4 August** Max Burnwell is converted to a
  Node. **Early September** a near-assassination of Burnwell and sabotage at the ECSE warn Deus that
  Mirage is interfering.
- **25 September** -- the Escher-Burkli infiltration fails, Surtr is released, 23 die; C5 is
  convened. **27 September** Zeta-ImpChem names Winternight and offers a countermeasure. **1-3
  October** the Jormungand code egg is found, then activated in a secure lab, killing every analyst
  online. **9-25 October** covert snatches, suicide fail-safe chips, "Heimdal's call"; two agents
  are inside the cult (Sweden and Tsimshian). **24 October** the Bloodyguts BTL. **30 October**
  Winston Griffith III is murdered. **31 October** compilation completes; 1,342 Nodes fall comatose.
- **1 November** -- extractions and strikes worldwide (Tsimshian, Denver, the Balkans, Pakistan,
  Bogota, Southeast Asia). **21:00** Thursday detonates Heimdal at Valhalla; the runners' panzer
  escapes with the mole, Wednesday (magical suicide in transit) and Friday.
- **2 November** -- **04:00** C5 stands down. **08:30** IPO trading opens. **09:16-09:28** Deus takes
  the ECSE host ultraviolet; the otaku raise a Resonance Well; Dodger wakes Megaera; Mirage attacks.
  **09:31** Jormungand launches (Yamatetsu MetaMatrix, UOL, PacRim Comm, then AngelSat and Arespace);
  Friday breaks. **09:32** Puck plants the egg. **09:42** Z-O interdicts all earth comms. **09:43**
  Atropos and Clothos break isolation, killing Lachesis. **09:44** the Boston EMP. **09:46** the
  Shadow Matrix forwards the dump; Captain Chaos fights his rearguard action. **09:51** the wolf's
  head eats the sun over Boston.
- **3 November** -- the New Revolution coup: Haeffner kidnapped and murdered, Stratta killed, Daviar
  survives an attempt in Seattle, Colloton declares martial law. **4 November** elections postponed.
- **Weeks after** -- Ares dismembers Cross; the Shiawase board coup; Dankwalther is Thor-shot;
  Tsimshian falls to the HNF and a Sioux-led STC army; Poland's Final Strike (10-23 November); the
  Caliph's surrender and Ibn Eisa's unmasking (23-26 November).
- **2065** -- January: Tsimshian's interim council elects Edward Littletree. **12-16 February**: the
  Second Universal Matrix Conference at Silicon Glen. **June**: Seattle awards its metroplex-wide
  AR network to Novatech and Transys-Erika. **August**: Alexandra Paris starts hearing the Idols
  again in a Downtown Seattle psychiatric ward. **October 2066** -- epilogue: Villiers, drunk in the
  same empty Boston bar, tells Lanier that Dankwalther won.

## NPCs (Persons of Interest)

| Name | Role | Org |
|---|---|---|
| Wednesday | Norn of Winternight -- the prophet whose vision guides the cult and whose toxic magic makes the apocalypse practical | Winternight |
| Friday | Norn of Winternight -- the technical mind behind the god chips, the drones and the weapons, and the only leader taken alive | Winternight |
| Thursday | Norn of Winternight -- tactical commander, recruitment officer, and the man who detonates Heimdal | Winternight |
| Jorgen Masterson | Winternight sleeper and weapons scientist -- the man who stole Surtr out of Zeta-ImpChem and built Ymir at Valhalla | Winternight |
| Aldrik | Winternight cell leader rigging EMP devices in the sewers under Boston and hiring shadowrunners he intends to sacrifice | Winternight |
| Magnus | Winternight cell leader posing as a British New Druidic Movement circle at the Brodgar assault | Winternight |
| Dimitri Korotkov | Winternight mole and satellite control operations manager at Svobodniy, who murders his own control room when the sign comes | Winternight |
| Orion | Ex Pacis regional cell leader in California; the Johnson who plants a Jormungand egg inside Alcatraz | Ex Pacis |
| Caliban | Magestone programmer holding the only copy of the code Ex Pacis commissioned; imprisoned in Alcatraz | Magestone |
| The Nubian | One of the twelve Whites; sent with Scarecrow to make an example of Mirage's favourite otaku | The Whites |
| Kiva | A damaged Network Node hidden at the Nightingales Clinic, whose locked code both AIs want | The Network |
| Jamil "Hellboy" Hamid Albar | Teenage Malaysian data-pirate and Ex Pacis carrier, killed by Surtr in the Escher-Burkli tunnels | Ex Pacis |
| Chromium | Seattle decker and Dodger's friend, murdered in her own flat by Sherman Huang's hit team | independent |
| Bloodyguts | Anti-BTL activist and one of Mirage's favoured otaku, murdered on camera to send the AI a message | independent |
| Winston Griffith III | Toronto philanthropist and secret otaku 'Dark Father', murdered as Deus's second message to Mirage -- and Megaera's patron | independent |
| Mirage | The eldest AI, born as the Echo Mirage team's guardian program, who comes out of self-exile to stop Deus | independent |
| Gossamer | One of the Idols -- a new AI that followed a grieving woman through the Matrix and asked to touch her sadness | independent |
| The Diamond Lattice | One of the Idols -- an inhuman intelligence that speaks in the voices of your own past and only wants to know where you came from | independent |
| The Branded Lady | One of the Idols -- a woman made of corporate logos who told Alexandra Paris she was a bridge between two kinds | independent |
| JackBNimble | The uncrackable file Dunkelzahn left Captain Chaos, which the worm opened -- and which saved him as a flawed data imprint | independent |
| Alice Haeffner | The woman who lives entirely in the Matrix -- the UCAS First Lady in Wonderland, destroyed by the Crash | independent |
| Silvery K | Denver Nexus sysop who carries Zurich-Orbital's warning to Shadowland after fighting the worm out of her own core | independent |
| Lynn Osborne | Novatech's Corporate Court justice and chair of the C5 -- the woman who chooses containment over warning | Novatech, Inc. |
| Jean-Claude Pirault | Saeder-Krupp's justice and C5 Second, who objects on the record, protects the Court's secrets, and orders the Thor shot on Dankwalther | Saeder-Krupp Heavy Industries |
| Atropos | Zurich-Orbital sysop who defies the Corporate Court, breaks comm isolation and broadcasts the warning that saves millions | independent |
| Michael Steiner | C5's resident military analyst, who delivers the post-Crash damage report and notices that the nukes did not work properly | independent |
| Ann Martin | ECSE Host Oversight Team Leader who dives into the ultraviolet host and becomes Megaera's mouthpiece | independent |
| Luke Tracey | ECSE security programmer with three secrets, blackmailed into handing Deus a passkey and nearly killed for it by the mob | independent |
| Amy Fusco | Luke Tracey's elven mistress, a Salem witch kidnapped to buy a passkey into the East Coast Stock Exchange | Crowhaven Circle |
| Max Burnwell | CEO of Matrix Systems of Boston, converted into a Network Node so Deus could rewrite the Exchange's new host | Matrix Systems of Boston |
| Cara Villiers | Richard Villiers's daughter, a hardened executive being groomed for Novatech's board and targeted by Nakatomi | Novatech, Inc. |
| Clara Vandervoot | Richard Villiers's personal assistant -- the one who calls Lanier when it gets bad, whose name Lanier can never remember | Novatech, Inc. |
| Nelson Stiverson | COO of Walker Aerodesign, who hires runners to fake his own extraction and gets a real one instead | Walker Aerodesign |
| Angel Anderson | Dankwalther's Ms. Johnson, who buys bank executives to stall Novatech's loans -- and disappears for showing initiative | independent |
| Noah | Boston seer who dreams of burning otaku children, saves them, and is stabbed for it | Seers' Guild |
| Remus | Via Stellae diviner who broke the Guild's secrecy to warn his friend, and had the aftershock vision about Boston | Seers' Guild |
| Jack Wulf | A servant of Fate who receives a vision of the coming Crash and immediately starts planning | independent |
| Stephan Maigret | EuroPol Anti-Terrorism Taskforce Coordinator who spent 2064 telling everyone Winternight was about to do something enormous | independent |
| Kyle Haeffner | President of the UCAS, kidnapped from the White House by the New Revolution and murdered during his own rescue | independent |
| Angela Colloton | The UCAS general who goes on trid and breaks the New Revolution coup with a speech | independent |
| Pete Reynolds | New Revolution director who ran the operation against the President -- and cut and ran the moment the coup failed | The New Revolution |
| Staff Sergeant Williams | The National Guard sergeant who guarded the President, and who was going to be the last American | The New Revolution |
| Jonathan S. Braddock | UCAS senator, secret Alamos 20,000 leader, and public face of the New Revolution coup | The New Revolution |
| Jerri Howard | The albino medium who channelled a dead Shiawase for a decade, was forced to prove it during the IPO, and died the same night | Shiawase Corporation |
| Reiko Shiawase-Shimada | Ryoi Shiawase's daughter, who destroyed the family medium to inherit -- and is now afraid to leave her house | Shiawase Corporation |
| Empress Hitomi Shiawase | The otaku Lady Death, kidnapped once as a message to Mirage, now Empress of Japan and Chair of Shiawase's board | Shiawase Corporation |
| James Mancuso | The Stuffer Shack clerk who bought Shiawase at the bottom on borrowed money and woke up owning four percent of a megacorporation | independent |
| Jean-Marie Cross | Lucien Cross's son and CATCo's new CEO, losing his father's corporation to Damien Knight a division at a time | Cross Applied Technologies, Inc. |
| Anatoly Kirilenko | Yamatetsu's new CEO -- the maverick behind its Mars mission, with a five-year plan and family in the Vory | Yamatetsu Corporation |
| Anders Malmstein | Transys-Erika's CEO, who outmaneuvered a dragon in the merger and is the likely chairman of the new Novatech | Transys Neuronet |
| Dr. Antonio Vieri | Saeder-Krupp's top Matrix researcher, the most wanted elf on several corporate extraction lists, kept alive by Lofwyr's agent Scale | Saeder-Krupp Heavy Industries |
| Neurosis | Project Cerebus's subject at Transys Neuronet, flatlined during the Singularity Event -- and kept on the Matrix by order | Transys Neuronet |
| Aziz Ibn Yusuf al-Shammar | Global Sandstorm's most powerful man, who backed Ibn Eisa's rise and then sold him to the Caliph for Arabia itself | Global Sandstorm |
| Badr al-Din Ibn Eisa | The Islamic Unity Movement leader who may have died in 2061 -- and whose body froze a palace, rotted the furniture and killed a man by touch | New Islamic Jihad |
| Farah | The Shadowland correspondent inside the Islamic Unity Movement who logged the Middle East's collapse from the room | independent |
| Michal Marszalik | Commander of the Polish Liberation Army and first President of the United Republic of Poland -- who may have murdered his own rival | Polish Liberation Army (AW) |
| Edward Littletree | Tsimshian's interim Great Chief -- a Tlingit moderate elected over a Haida hero, and suspected of being somebody's puppet | Tsimshian Nation |
| John George | Haida icon who reemerged after the occupation as a candidate for Great Chief, and now sits on the council of a nation that wanted him dead | Haida National Defense Force (HNDF) |
| Alexandra Paris | The aerospace engineer who lost her family in the Crash and started meeting AIs without a datajack | independent |
| Dr. Albert Adderson | The psychiatrist treating Alexandra Paris, whose pocket secretary ends up on Shadowland and whose patient is quietly taken | Mitsuhama Computer Technologies |
| Leroy Carper | The Boston manager whose SIN the Crash erased, who lost his job, his wife and his name, and froze to death in an alley | independent |
| Lucia D'angelo | KSAF freelancer sent alone to Boston on a one-word order, whose laser microphone catches the Exchange dying | independent |
| Gustav Moeller | Saeder-Krupp's man at the NEEC, who has to sit in the room while Lofwyr gives Europe four minutes' notice | Saeder-Krupp Heavy Industries |

## Locations

| Name | Type | District | Notes |
|---|---|---|---|
| East Coast Stock Exchange | corporate headquarters | Downtown | The neo-gothic church to the Almighty Nuyen at the centre of downtown Boston, and the ultraviolet host Deus chose for his apotheosis |
| Novatech New Fenway Park | landmark / stadium | Fenway | The Red Sox's ballpark under Novatech's name -- Villiers may be a Yankees fan, but he knows a branding opportunity when he sees one |
| Valhalla (Winternight Base) | underground bunker | An island in the Bay of Bothnia, Baltic (Swedish waters) | A Cold War submarine base carved into the rock of a Baltic island, erased from government records: Winternight's home, temple and arsenal |
| Hel (Winternight Base) | underground bunker | Location undisclosed | Winternight's North American base, hit by MCT troops and Tsimshian national forces on the night of 1 November |
| Escher-Burkli Island EBZ | corporate facility | Escher-Burkli island Extraterritorial Business Zone | The island Extraterritorial Business Zone whose maintenance tunnels hold the Escher-Burkli PLTG hub -- where Surtr was released and Winternight's hand was finally shown |
| Nightingales Clinic | hospital | Queen Anne Hill (the text also calls it Downtown) | A neoclassical private clinic for wealthy corporate clientele, and the place Mirage hid the damaged Node called Kiva under Novatech guard |
| Chromium's Doss (Tacoma) | apartment complex | Tacoma | A no-frills Tacoma flat with a nice Harley outside, and the first body the runners find on Dodger's trail |
| Walker-Sung Psychiatric Facility | hospital | Downtown | The MCT Public Health Hospital's psychiatric wing, where a woman with a stoppered datajack talks to the Idols under the new wireless test network |
| Captain Chaos's Everett Apartment | residential community | Everett | A small Everett flat with cables running creeper-like through its walls: the physical location of Shadowland Seattle and the place Jim's body is found |
| Brodgar Stone Circle | landmark / monument | Off the northern coast of Scotland | A major power site on the terminus of the Scottish Wild Ley, seized by a Winternight cell for twelve hours of storm-spirit summoning |
| Uppsala Aesir Society Shrine | landmark / monument | Sweden | The Swedish power site where a Viking blot powers the illusion of a giant wolf's head swallowing the sun over Boston |
| Alcatraz (Saito's Intelligence Division) | military installation | San Francisco Bay, California Free State | The Rock, refurbished to house General Saito's intelligence division and hold dissident prisoners -- and wired into his corporate backers' systems |
| La Diabla Casino | casino | The Strip | A darkened casino past its best days on the Vegas strip, where Dankwalther's Ms. Johnson meets bought bank officers |
| Gillespie Palisades Property | corporate facility | Pacific Palisades (Pueblo-controlled City of Angels) | A secluded, heavily guarded Palisades estate where the Gillespie mob keeps its captive Magestone deckers writing laundering code |
| Salem | residential community | Massachusetts, UCAS | A city where spellcasters are simply more common and dozens of small covens operate openly -- and where Luke Tracey's mistress lives |
| Puck's Caribbean Bungalow | safehouse | Beachfront | The one luxury Puck ever asked Deus for: a small beach bungalow whose walls are covered in other people's memories |
| Uzume Station | orbital station | Japanese orbital operations | A Japanese orbital station that watches the AngelSat constellations die and then loses its own encryption shields to the worm |
| Svobodniy Mission Control | government building | Russian Far East cosmodrome | The satellite control centre where a Winternight sleeper waited years to open fire on his own colleagues when Heimdal's call came |
| Silicon Glen (Transys-Erika) | corporate facility | Silicon Glen, Scotsprawl | Transys-Erika's Scottish campus, host of the Second Universal Matrix Conference that standardizes the wireless world |
| Presidio Blast Zone (San Francisco) | ruins | Presidio and northeast shoreline | Ground zero of the best-documented EMP strike: a 20-kilometre blackout, an irradiated shoreline and 70 percent of the city's Matrix infrastructure gone |
| Wong's Jade Buddha Cantonese Takeaway | restaurant | School St, Charlestown | A takeaway on School Street with an alley behind it, where a man who no longer legally existed froze to death two days after Christmas |
| Al-Nasiriyah Royal Palace | government building | Arabia | The Riyadh palace where the Caliph's public surrender to Ibn Eisa turned into Ibn Eisa's unmasking |

## Organizations (new)

| Name | Type | Tier | Notes |
|---|---|---|---|
| Ex Pacis | otaku tribe | 3 | Pax's Dissonant otaku tribe: the Matrix must be made one with them, not they with it -- and if the Matrix will not stop the Fading, the Matrix must be rebuilt |
| The Network | AI infrastructure (cyber-enhanced human nodes) | 4 | The thousand metahumans Deus loaded his shattered code into: a decentralized compilation engine hidden inside ordinary lives, and the battleground of two AIs |
| Corporate Court Crisis Coordination Committee (C5) | government agency (Corporate Court branch) | 5 | The Corporate Court's least-known branch: convened only in crises, it runs joint intelligence between the Big 10 and national security agencies -- and it loses this one |
| Shadowland | data haven network | 3 | The shadow community's own network of data havens -- and the only thing standing between the world and Operation: Mjolnir when the corps choose containment over warning |
| Matrix Systems of Boston | corporation (Novatech subsidiary) | 2 | The Novatech subsidiary that traces its roots to Echo Mirage, built the ECSE's new host -- and unknowingly houses the AI Mirage in its hidden systems |
| Trans-Latvian Enterprises | corporation (investment bank) | 3 | The empty shell Villiers built to hide his assets, which came alive, called in his loan, and now owns 24 percent of Novatech under an owner nobody can name |
| The New Revolution | conspiracy | 4 | The secret conspiracy to reunify the United States of America, which used the Crash as cover for a continent-wide military coup on 3 November 2064 |
| Seers' Guild | mystical fellowship | 3 | The world's organized diviners, who saw the Crash coming and could not agree what to do about it -- warn the world, sell the knowledge, or invest ahead of it |
| Order of the Hourglass | mystical fellowship | 2 | Diviners who believe Fate must not be derailed, and who will stop by any means the seers trying to change what they have foreseen |
| Magestone | decker group | 2 | The underground decker collective that wrote Jormungand's viral component for a client it believed was a Japanese nationalist faction |
| Metahuman People's Army | resistance movement | 2 | The Bay Area's metahuman resistance to General Saito, and the muscle behind any jailbreak worth attempting on Alcatraz |
| O'Rilley Family | mafia family | 3 | The Boston Mafia family that owns the East Coast Stock Exchange security programmer Luke Tracey -- and thinks he has turned Fed |
| Crowhaven Circle | mystical fellowship (school of witchcraft) | 1 | A small but organized school of witchcraft in Salem, one of dozens of covens in a city where spellcasters are simply more common |
| Walker Aerodesign | corporation (Novatech subsidiary) | 1 | A Novatech subsidiary deliberately loaded with debt and a few valuable patents, dressed for a fire sale and sabotaged by Dankwalther |
| Minuteman Security | corporation (private security) | 2 | Private security contractor -- Max Burnwell's personal detail in Boston, and one of the firms making a fortune protecting Tsimshian neighborhoods from their own police |
| Technicolor Wings | smuggling ring | 2 | The smuggling outfit that moves Winternight's crates without knowing or caring what is in them |
| Global Sandstorm | corporation | 4 | Sandstorm Engineering plus Global Oil: the AA that bankrolled Ibn Eisa's rise, then sold him out to the Caliph for total control of corporate affairs in Arabia |
| New Islamic Jihad | terrorist organization | 3 | Ibn Eisa's terror arm, cut loose from the Islamic Unity Movement and scattered across the world vowing to bring down the Caliph -- with his Jinn among them |
| Haida National Defense Force (HNDF) | paramilitary | 3 | The Haida National Front rebranded as a defense force and legitimized as Tsimshian's temporary tribal police with Sioux backing |
| Longhouse Brotherhood | mystical fellowship | 2 | The shamanic brotherhood that put its members and spirits on the streets to save the elderly, the sick and the injured, and earned a seat at the provisional government table |
| The Dogmen | criminal syndicate | 2 | The 'Amerindian Mob' -- the syndicate that filled the vacuum when Mitsuhama's pullout took the Yakuza with it |
| Polish Liberation Army (AW) | resistance movement | 3 | The Free Polish army that used the Crash week to launch the Final Strike, broke the Russian occupation, and put its commander in the presidency |
| The Helix | hacker collective | 1 | The pan-European hacker co-op rebuilt on stolen wireless hardware, and one of the first shadow networks to come back after the Crash |

## Existing organizations updated (sourced appends, nothing overwritten)

- **Overwatch** -- profile; GM notes; enemies: Ex Pacis, Winternight, The Whites, The Network
- **The Netwalkers** -- profile; GM notes; allies: Overwatch; enemies: The Whites, Ex Pacis
- **The Seraphim** -- profile; GM notes; enemies: Ares Macrotechnology
- **Winternight** -- profile; GM notes; leadership: Wednesday, Friday, Thursday, Jorgen Masterson, Aldrik; allies: Ex Pacis; enemies: Corporate Court Crisis Coordination Committee (C5), Overwatch, Zeta-ImpChem
- **The Whites** -- profile; GM notes; leadership: The Nubian, Cat; enemies: Overwatch, Ex Pacis
- **Zeta-ImpChem** -- profile; GM notes; enemies: Winternight
- **Novatech, Inc.** -- profile; GM notes; leadership: Cara Villiers, Lynn Osborne, Clara Vandervoot; enemies: Winternight
- **Cross Applied Technologies, Inc.** -- GM notes; leadership: Jean-Marie Cross; enemies: Ares Macrotechnology
- **Transys Neuronet** -- GM notes; leadership: Anders Malmstein, Dr. Yolanda Price; allies: Novatech, Inc.
- **Wuxing, Inc.** -- GM notes
- **Eastern Tiger Corporation** -- GM notes; enemies: Renraku Computer Systems
- **Pacific Prosperity Group** -- GM notes
- **Federated Boeing** -- GM notes
- **Renraku Computer Systems** -- GM notes; enemies: The Network, The Whites
- **Mitsuhama Computer Technologies** -- GM notes
- **Saeder-Krupp Heavy Industries** -- GM notes; enemies: Winternight, Global Sandstorm
- **Aztechnology** -- GM notes
- **Shiawase Corporation** -- GM notes; leadership: Empress Hitomi Shiawase, Reiko Shiawase-Shimada, Ichiro Kiyomoto
- **Yamatetsu Corporation** -- GM notes; leadership: Anatoly Kirilenko
- **Ares Macrotechnology** -- GM notes; enemies: Cross Applied Technologies, Inc., The Seraphim
- **Fuchi Industrial Electronics** -- GM notes
- **Lone Star Security** -- GM notes
- **Knight Errant Security Services** -- GM notes
- **Alamos 20,000** -- GM notes; allies: The New Revolution
- **Tsimshian Nation** -- GM notes; leadership: Edward Littletree
- **Haida National Front (HNF)** -- GM notes; allies: Haida National Defense Force (HNDF), Sioux Nation
- **Salish-Shidhe Council** -- GM notes
- **Sioux Nation** -- GM notes
- **Native American Nations (Sovereign Tribal Council)** -- GM notes
- **Tir Tairngire** -- GM notes
- **Seattle Mafia** -- GM notes; enemies: The Dogmen
- **Ancients** -- GM notes
- **Crimson Crush** -- GM notes
- **Greenwar** -- GM notes

## Existing locations / NPCs updated

- location: **Zurich-Orbital**
- location: **Renraku Arcology (SCIRE)**
- location: **The Ork Underground**
- location: **Kitimat Harbor**
- NPC: **Megaera**
- NPC: **Celedyr**
- NPC: **Pax**
- NPC: **Puck**
- NPC: **Scarecrow**
- NPC: **Ronin**
- NPC: **Dodger**
- NPC: **Deus**
- NPC: **Captain Chaos**
- NPC: **Richard Villiers**
- NPC: **Miles Lanier**
- NPC: **Samantha Villiers**
- NPC: **Darren Villiers**
- NPC: **Damien Knight**
- NPC: **Leonard Aurelius**
- NPC: **Lucien Cross**
- NPC: **Bernard Cross**
- NPC: **Dr. Sherman Huang**
- NPC: **Inazo Aneki**
- NPC: **Shikei Nakatomi**
- NPC: **Korin Yamana**
- NPC: **Mitsuko Shiawase-Yamana**
- NPC: **Sadato Shiawase**
- NPC: **Tadashi Shiawase**
- NPC: **Saru Iwano**
- NPC: **Buttercup**
- NPC: **Yuri Shibanokuji**
- NPC: **Haruhiko Nakada**
- NPC: **Nadja Daviar**
- NPC: **Dunkelzahn**

## Matrix systems -- to build in the Matrix designer (NOT built yet)

Nothing below is built by the loader -- these are the systems worth statting if the campaign goes
into them.

**East Coast Stock Exchange host (Boston)** -- rebuilt by Matrix Systems of Boston and unveiled on
IPO day.

| Node | Function | Color/Rating | IC |
| --- | --- | --- | --- |
| Public trading floor (nave/chancel) | Open access for hundreds of thousands of traders | Green, high capacity | Minimal; monitors only |
| Transept panels | Global stock information display | Green | Probe, Trace |
| Oversight subsystems | Ann Martin's host oversight team; tamper detection | Orange | Adaptive; can auto-shutdown trading |
| Upper levels / SAN control | Security deckers only, limited random passkeys | Red | Specialized IC (GM's choice), Black IC likely |
| Whole system, 09:16 onward | Deus's upgrade engine | Ultraviolet | The AI itself |

Notes: the host is smart and adaptive and senses even small amounts of data tampering, and will
shut itself down and close trading if it decides economic or transaction data is being
manipulated -- so Deus's Nodes were ordered to plant backdoors and touch nothing else. Emergency
shutdown is overridden from within at 09:18. 173,283 users are logged in. Physical and magical
security answer to the Board, never subcontracted. Deus manifests as a crystalline World Tree
growing from the trading floor and forces open SANs to supercomputers in Tokyo, Denver, Caerleon
and Johannesburg; Megaera manifests as a storm of faces throwing lightning; Mirage as metallic-
winged angels with flaming blades; the otaku raise a Resonance Well at the Tree's roots at 09:24.

**Jormungand** (chimaera; unique daemon/worm construct -- document, do not build as a location)
Bod 6, Evasion 5, Masking 2, Sensors 5; Pilot Rating 5; Hacking Pool 6; Attack 6D.
Echoes: Cascading Code, Enhanced Distortion Echo, Siphon, Traceroute (high traffic areas).
- *Cascading Code*: +1 to all Persona Ratings and Attack Rating for every minute after release, and
  again each time it is defeated in cybercombat.
- *Enhanced Distortion Echo*: for every two turns it is present in a host, +1 to local target
  numbers for tests involving non-Dissonant users, subsystems, constructs and programs, to a maximum
  of double the system's Security Value.
- Homes in on high-connectivity zones and Matrix activity spikes; attacks all icons and personae;
  pools corrupt code into Dissonance Pools at corrupted nexi; respawns at the nearest Pool or
  egg-host seconds after being destroyed. Programmed to avoid Resonance Wells.
- **Achilles heel**: destroy the physical hardware hosting a code egg and that branch of the virus
  withers and decays, though the damage already done remains.

**Jormungand code eggs and sample nest hosts** -- at least half a dozen eggs per continent. Named:
Yamatetsu MetaMatrix central routing hub; the Morgue Data Haven / MRG PLTG (Singapore); Panama Canal
PLTG; California Protectorate Intel Services grid (Alcatraz); Buenos Aires, Vladivostok and Europort
Port Authority grids; Stockholm, Oslo and Hamburg DeMeKo MSP grid; PacRim Comm administrative
systems; British Administrative Bureau C-Net; Osaka Corporate Community PLTG; Kolkata Talent and
Technology outsourcing projects' grid. Escher-Burkli's egg was found and (fatally) tested early.
Surtr aerosol dispensers are hidden in ventilation and computer rooms near nest mainframes,
radio-triggered by Winternight spotters.

**The Denver Nexus and the Shadow Matrix** -- low-traffic and therefore hit late. The Nexus is
infected through its own connection to the Morgue, which is sending corrupted backups into its data
stores; the worm corrupts part of the Nexus controls and severs it from Shadowland. Sysops Silvery
K, Bash and Crystal fight it host by host; Bash and Crystal die. The Nexus Crew calls the Denver
Shadows to physically disconnect the system even if it dumpshocks everyone online ("Disconnection":
about ten minutes to blow the relays, in a chase through the dragon-governed city).

**The Morgue data haven** (inside Singapore's Market Research Group system; Target: Matrix pp.47-51)
-- reached through the MRG's inner grid and its UV datacore. Ex Pacis's main Dissonance Pool sits in
a hidden UV host inside it, in a vast quartz cavern behind a code facade off the Morgue's three
floating obelisks, with hidden guardian daemons that defer to Pax.

**Shadowland Seattle and the Abraxis** -- Shadowland's gathering host is a boisterous hive of
industrial iconography, metal staircases and levels crowded with persona icons crafted for shock.
The war council room is a virtual space of honeycombed screens carrying news feeds and hacker
forums, set up by drones in minutes. Both are destroyed.

**The Mitsuhama Seattle host** -- sculpted as a large Japanese pagoda with dragons, rice paper walls
and low tables, with geisha icons for the agent programs that act as tour guides; used as a teaching
example of sculpting in system design. Seen de-rezzing as the worm's wave arrives.

**Wonderland** -- Alice Haeffner's demesne: rain-slicked canyons, and the whole of it destroyed when
her core implodes.

**The Erika Light Garden (Stockholm)** -- digital flowers in full bloom, air swirling with cherry
blossoms. Alexandra Paris walked through it with no cyberdeck at all.

**Post-Crash: the wireless mesh** -- the rigid RTG/LTG hub infrastructure gives way to billions of
nodes in nested LANs (wireless, wired or mixed) with distributed processing as the norm; even a user
is a small network (a PAN). RTG and LTG survive only as names for network levels. WiFi protocols,
frequencies and transactions are standardized at the Second Universal Matrix Conference. Security
protocols are retro-termed Firewall. Hacking means browsing frequencies and hijacking signals, and
is mobile; simultaneous full VR and AR causes serious sensory input problems. Novatech's wireless
test network goes live over parts of Downtown Seattle in August 2065.

## Flavor / not built

Name-drops, single-line bystanders and figures folded into the rows above.

- **C5 and Corporate Court**: Yves Laroquette (Z-O Station Manager), Toshiro Saigusa (CCMA
  Director), Li Feng (Wuxing), Raphael Colemno (MCT), Neil Benson (Renraku), Anna Villalobos
  (Aztechnology), Paul Graves (Ares), Leonard Yang, Clothos and Lachesis (Z-O sysops) -- all folded
  into the C5 org and the Zurich-Orbital update.
- **East Coast Stock Exchange meeting**: Viktor Tarkhan, Logan Roy St. James, Thomas Fitzgerald,
  Jack Craver -- folded into Lucia D'angelo and the ECSE location.
- **Ex Pacis and the Whites**: Amor, Honos and Solitude (folded into the Ex Pacis org), Cat (folded
  into The Whites), Silicon Sue (folded into Magestone).
- **Shadowland**: DionySys, Juggler, Smiley, Diabolique, Thumper, Raid, Syzygy, Bash, Crystal,
  Sequoyah (Cheyenne), Tell (Frankfurt), Drackenfelts (Paris), Sionedd (Mersey), Retro, Donner,
  Kino, Munin, Peregrine, Green Pixie, The Chromed Accountant, Espion, Slamm-0!, Fastjack and the
  rest of the commenter roster -- folded into the Shadowland org. Synner appears as The Helix's
  leadership.
- **Novatech and TLE**: Griffon (Dankwalther's Johnson) and Eleanor McEllis, folded into Walker
  Aerodesign; Oskari Laine and Charles Lyons, folded into Trans-Latvian Enterprises; Sam Villiers.
- **Escher-Burkli**: Lukas "Klasser" Hoecht, Lt. Thomas Zeigler, Capt. Bertorelli, Capt. Julianne
  Moreau, Allessandro Buzzi (J&E ImpComm), the S-K Prime mole "Orpheus" -- folded into the location
  and Stephan Maigret.
- **Orbital and smuggling**: the Kimi Aurora's crew (Sven "DanZer", Lenka, "Red Bear"); Uzume
  Station's Lt. Ronald Pierson, Mazim Chelenko, Jamie Kano, Kamiko Yoshimoto, Lt. Cmdr. Yuriko
  Murakami and Klaus Meyers; Ivan Gref at Svobodniy -- folded into the two station locations.
- **Seers**: Yohann De Kervelec, and the adventure-seed seers Jack Dylan, Gardhia Obasegan, Monji
  Sanko, Hiro Tanawa, "Orlando Bonnetoile" and "Magnificent Gary".
- **Winternight fronts and contractors**: Sir John Lewellyn-Stuart, Mr. Lyesmith, the codename Tyr,
  Nationale Aktion, Runenthing, White Resistance, the Crying Masks, the Siida, the Aesir Society,
  Kali cults, Green Cells; the Wild Druids, the Pendragon Underground and the False Face society;
  Argus, Aegis Cognito and Wolverine.
- **Shiawase, corps and dragons**: Nigel Coltrane, Soko Shiawase, Emperor Yasuhito, Rhonabwy,
  Thomas Roxborough, Ding Ramos, Angela Espinosa, Dr. Kristine Martin, Roberto Kama, Melissa Kwan,
  Hideo Yoshida, Nicholas and Evelynn Aurelius, Kevin Jensen, Fiona Blareth, Sir Michael Ashmoore,
  Toshiro Mitsuhama, Bremen, Scale, Dr. Yolanda Price, Princess Caroline, Johnny Spinrad; the
  Genesis Consortium, Horizon Group, Hisato-Turner, Universal Omnitech, Sol Media, Yang-Su
  Enterprises, Hynix, Sony Automation/Dataworks, Ruhr-Data-Fax, DeMeKo, PacRim Comm, UOL, KITT,
  Malaysian Independent Bank, Icon Inc., Gemsys, T99, Nuvodine, Epoxytech, Fairlight Industries,
  JRJ International, Keruba, Lusiada, Gaeatronics, Pomorze ZS, Genom, the Gillespie mob, the Unseen.
- **Tsimshian, Poland and the Middle East**: Junichiro Masakura, Deborah Jim, Nathan Jance, George
  Lodgepole, Thunder Nelson, Yellowtail, Screaming Eagle; President Rybinski, Gen. Mikhail Suchov,
  Gen. Wysocki, Captain Zbik, Elzbieta Kiszkiel, Vladimir Danko, Joanna Falejczyk, Babinicz, the
  Kapers; Caliph Ibn Saud, Ayatollah Juvayni, Farid al-Mansoor, President al-Ibrahim, Arabian
  Futures, Ifrit Services, Xenel-Oman, the Islamic Cooperative Development Bank.
- **UCAS**: President Pro-Tempore Gene Simone, Secretary of Defense Stratta, Major Dave Connors.
- **Crash vignette bystanders**: Robert Takahashi (and Katherine, Joey and Briana), Scott Matthews
  and Petey of Cantor-Kurusawa, Capt. Rosenau, Melody Hausenberg, Dr. Christine Lindahl and Dr.
  Michaels, "Jumpmonkey", Tommy Thrash, Serena Olivetti, Mindy McCutcheon, Orrin Washington,
  "Deuce", "Bloodbath", Lana Feingold, Hector Lopez, "Jimmy Joe", Eddie, Joey and his CyberVixen,
  Janet Backett, Dr. Saleb Muhahmi, Ms. Sakura, Mrs. Moore, Willis, Dr. Shalbermat, Dr. Mays.
- **Places named only in passing**: Treffpunkt, the Spindle, Daedalus and the AngelSat and Arespace
  constellations; the Vault (Swiss banking ICberg); the Haparanda Anomaly Zone's wider extent; the
  New Fenway Park groundskeeping; the Novatech Prime facility; the Boston restaurant where Mr.
  Johnson briefs the runners in "Extended Family".

## GM play notes

- **Three tracks, one morning.** Novatech Goes Public, Singularity and Fall of Night run in
  parallel and collide at 09:16-09:44 EST on 2 November 2064. A campaign can play any one of them
  and only learn about the others afterwards; the book's own adventure frameworks each sit in a
  single track and none of them require the players to understand the whole picture.
- **Foreshadow for months.** Unusual animal behaviour (birds migrating out of season as they sense
  the cold), the magically enhanced early winter, conspiracy buffs on the Dankwalther-Villiers
  feud, Winternight, the Network or Deus (plus gamemaster red herrings), and prophetic or
  totem-induced visions. Prophecies multiply and contradict each other as the date approaches. The
  point is to make the players feel that something big is coming.
- **Most runner involvement is unwitting.** Winternight and Ex Pacis hire through corporate sleeper
  Johnsons: ferrying an Ex Pacis otaku and an aerosol dispenser into an RTG hub, holding a stone
  circle for twelve hours, installing hardware in a sewer, plus paid decoy sabotage and datatheft
  to divert attention. Aldrik's line is the standing policy: "after their task is finished, they
  will die, fuelling our magic with their impious blood." A team that survives one of these
  contracts is a loose end the cult will come back for.
- **The corps do not save the world; the shadows do.** C5 knows the nest, blimp and fault-line
  coordinates minutes after the virus launches, and cannot get them to anyone in time. Atropos and
  Clothos break isolation, Shadowland spends its last minutes hacking vending machines and
  commercial boards to display the warning, and runner groups scrambled by desperate Johnsons take
  out nests while corporate strike teams handle the blimps and fault-line sites. Nest security is
  on high alert, has no idea what is going on because its own comms are down, and will take a very
  dim view of strangers damaging its property; then there is the Surtr saturation to get through.
- **EMP damage.** Opposed test between the gear's rating and the pulse: base Rating 25, -1 per
  kilometre for an airborne detonation, -2 per kilometre for a ground-level detonation in a built-up
  urban area. Cyberware and hardened electronics have a base rating of 9, -2 if second-hand and -2
  for every five years of age. 0 successes no damage; 1 minor (reset and diagnostics); 2-3 moderate
  (replace components or software); 4-5 serious (RTG stations and gridlink crash, riggers suffer
  electroshock feedback); 6+ destroyed. Effects are cumulative. Within 2 km of ground zero, direct
  effects are 20D at -1 Power per 100 metres, plus shockwave shrapnel, flying glass and steam, and
  eye damage for anyone looking at the flash unshielded.
- **Living through the Crash.** Effects are deliberately uneven -- pick strong, minimal or light per
  location. Air traffic grounded for days or weeks (semiballistics worst), trains switched onto
  occupied lines, automated trucks stopping and being looted, GridGuide-dependent traffic dead in
  the street. Credsticks unreadable, so cash, certified sticks, gold and barter take over; hoarding,
  bank runs, looting and vigilantes. Automated plants and dams run amok; splinters of AI lodge in
  steel mills and assembly lines; security systems fail and release guard critters, research
  subjects and prisoners; lockdown-on-failure facilities entomb their staff. Pirate radio and trid
  become the best news source and are briefly unhassled. Magicians in some cities sell astral and
  spirit courier messaging, profitably.
- **Head Crash.** Dumpshock from mild to fatal; seizures, lesions, strokes; sensory-overload
  blindness, deafness or muteness; Matrix neuroses and psychoses (much likelier if the character was
  in an emotionally charged session -- conditioning, online therapy, intense cybersex); severe Matrix
  withdrawal; and, rarely, being left on the other side of the door. For a stranded PC: retire and
  run as an NPC, treat as a Matrix-only entity with the attributes held at transformation, or treat
  as a semi-autonomous knowbot (Matrix p.147). Alice Haeffner is the warning -- the only person known
  to be living solely in the Matrix, and she does not survive the Crash. Some who come back "awaken"
  on the new wireless networks and can see things others cannot.
- **The aftermath is the campaign.** The SIN registries are corrupted, so existing SINs (forged ones
  included) can be erased and false ones can become real, complete with marriages, patrimony and
  prison records (Sprawl Survival Guide pp.126-127). Forgers hire runners to insert identities into
  the backups so they come back real; other Johnsons pay to erase an enemy's SIN for good. Every
  corporation has lost contact with tried-and-proven deniable assets and must use whatever fresh
  talent is available, so the shadows are hiring everywhere -- and the wireless race means espionage,
  sabotage, data theft and researcher extraction on a scale nobody has seen in years.
- **Open threads worth keeping.** JackBNimble and whoever else it "saved"; the Idols and the people
  who can reach them without hardware; whatever changed places between Neurosis and Celedyr; Pax and
  her lieutenants, who simply vanish; the Winternight cells that never got their orders; the
  arrested personal assistant in a Toronto cell; and Michael Steiner's heresy that large-scale
  nuclear detonations may simply no longer be possible in the Sixth World.

