# SRM 01-01 Double Cross -- Adventure Prep: NPCs, Locations, Organizations, Matrix Systems

Source: SRM01-01A_Double_Cross.pdf, pp. 3-26; SRM01-01B.pdf (player handouts). Campaign order #44, in-game 2064 (no in-world date is printed; the book is set 'during the 2060s', references the Redmond crash of '59 and a Temporary Responder Program devised in 2057).

Everything below is loaded into the campaign DB flagged `is_active: false` and `source_adventure: "SRM 01-01 Double Cross"` by `python scripts/adventure_ingest/run.py srm_01_01_double_cross`; flip entries active as the party meets them. Use the **Adventure** filter on the manage pages to see just this set.

## Plot synopsis

**Fox**, a Seattle fixer with a taste for cigars and a low opinion of the talent he hires, calls a
team of competent unknowns to a pull-off on the west shore of Lake Washington just after dusk. The
job is wetwork: **Michael Davenport**, Chief Operations Officer of **DocWagon**'s Seattle
franchise, is to be shot or spelled at the podium during the annual shareholders' meeting in the
Grand Ballroom of the **Westin Seattle Hotel**. No explosives, no collateral damage. Ten thousand
nuyen for green runners, more for better ones, plus a fully stocked Tacoma safehouse and gear at a
twenty percent discount. One condition is non-negotiable: Fox comes along.

The reason Fox comes along is that the Johnson is Davenport himself. Two years of shot-down
proposals -- most recently a UCAS military pharmaceuticals contract with **Fort Lewis** as the
testbed, killed by CEO **Garrett Walsh**'s dislike of defense work -- convinced Davenport that
DocWagon's monopoly on metroplex health care makes it fat and cautious, and that the way to get
rich is to compete with it. He has spent months preparing: encrypted caches of customer lists and
security codes hidden across the company (one, an innocuous file named "H", sat in the Snohomish
plant that was blown up weeks ago); his own medical records swapped with those of **Earl Peabody**,
a Fort Lewis car dealer of the same build; a second Peabody clone commissioned and quietly rerouted
out of DocWagon's Tacoma storage facility. Fox reports the runners' plan to him so he can prepare
mundane countermeasures and, if he must, a mage in the audience who will drop illusions the instant
the trigger phrase is spoken. The safehouse is bugged for the same reason.

The runners get five days. They can case the hotel (a soft target with a hard PanicButton: a
magnetic anomaly detector in the guest doors, Rating 5 maglocks on credstick verification, taser-
armed private security in secure clothing, and a Lone Star contract that puts armed response inside
the building in five combat turns), work the **Rabinowitz** wedding reception in the same ballroom
the night before, deck the hotel's Orange-5 host, or get pulled into a Nightsky by an interested
investor -- Mafia don **Vincent "Numbers" Ciarniello**, sokaiya boss **Toju Shotozumi**, Paladin
Medical's **Dr. Thomas Fredericks** or the socialite **Drew Hollingsworth** -- who wants to know
which way DocWagon stock is about to move. If they dawdle, a DocWagon special ops team comes through
the safehouse windows on ropes.

At zero hour Davenport introduces **Dr. Chandra Dasari** of **Griffin Biotechnology**, says "all of
these achievements come with a price -- and not always money", and falls. A second team of runners
in DocWagon High Threat Response colors -- wearing gear taken off murdered **HTR team #27** out of
Renton -- carries him out while Fox screams over the commlink to finish the job. The runners blow
the ambulance; a Trid Phantasm and a greater form city spirit carry the real Davenport away. The
next morning's screamsheet reports five dead, DNA and dental records confirmed, cremation, a
memorial at **Reynolds Eternal Estates** in Bellevue, no surviving relatives. In a few weeks a man
with a new face named **Walter Broward** will introduce himself as Chief Executive Officer of
**Rose Croix**, a new competitor in emergency medical services, and the two-year story arc begins.

## Timeline

- **2057** -- Davenport devises DocWagon's Temporary Responder Program to augment undermanned HTR
  teams. The uniforms and credentials it produces are what the extraction team will wear.
- **'59** -- the Redmond crash; DocWagon shares have climbed steadily ever since, which is exactly
  Walsh's argument for taking no risks.
- **~2 years back** -- Walsh begins refusing Davenport's diversification proposals. The friendship
  strains.
- **Last month (relative to the prologue)** -- Walsh approves the Snohomish pharmaceutical plant;
  supply contracts signed with Seattle General Hospital and the university clinic.
- **A few months back** -- Davenport begins laying the groundwork: hidden encrypted files (including
  "H" in Snohomish), the Peabody records swap, retagged clones, a second Peabody clone commissioned
  "for shipment to the east coast".
- **A few weeks back** -- someone destroys the Snohomish facility; DocWagon loses six months of
  production and has to buy from outside vendors at a premium.
- **Recently** -- Yamatetsu, with AG Chemie of Europe and Paladin Medical Technologies, wins the
  UCAS defense contract Davenport wanted. The contract is the only thing keeping Paladin afloat.
- **Days back** -- someone pokes around the unopened Griffin Biotechnology facility in Everett and
  learns nothing; Knight Errant has the site.
- **Day 0 (evening)** -- Fox meets the team at Lake Washington. Five days to zero hour.
- **Days 1-4** -- the safehouse, the hotel, legwork, the Rabinowitz reception, the optional
  DocWagon raid and the optional limousine interview.
- **Day 4 (the night before)** -- the Rabinowitz-Ginsberg wedding reception fills the Grand Ballroom.
- **Day 5, evening** -- the shareholders' meeting. CEO speech, CFO speech, Davenport's speech,
  Dasari's introduction, the trigger phrase, the hit, the HTR extraction, the ambulance.
- **+30 minutes** -- the safehouse; Fox's phone call confirms Davenport and the medical team dead;
  cigars and certified credsticks.
- **The next morning** -- the KSEA screamsheet. Memorial Saturday, Reynolds Eternal Estates.
- **A few weeks on** -- surgery, a new identity, and Walter Broward of Rose Croix.

## NPCs (Persons of Interest)

| Name | Role | Org |
|---|---|---|
| Michael Davenport | Chief Operations Officer of DocWagon Seattle and the true Mr. Johnson -- he hired both teams, faked his own death and walks away as Walter Broward of Rose Croix | independent |
| Garrett Walsh | Chief Executive Officer of DocWagon Seattle -- the cautious boss whose refusals set the whole plot in motion, and who eulogises the man who robbed him | DocWagon |
| Dr. Chandra Dasari | Griffin Biotechnology's lead neurology researcher, presented to the shareholders under bodyguard moments before the shooting starts | Griffin Biotechnology |
| Margo Fleming | DocWagon Seattle's Vice President of Marketing and Davenport's personal assistant -- the one person who runs toward him when he falls | DocWagon |
| Kevin McKeen | Manager of the Westin Seattle -- the man whose staff can be bribed, whose maglocks are Rating 5 and whose PanicButton brings Lone Star in five turns | Westin International Hotel Corporation |
| Vincent "Numbers" Ciarniello | The longest-serving Mafia don in Seattle -- an accountant at heart who plays the market and wants advance warning of what is about to happen to DocWagon stock | Seattle Mafia |
| Drew Hollingsworth | Wealthy socialite and adventurer with an uncanny nose for corporate trouble; senses that DocWagon's management is about to change and wants to know how | independent |
| Levi Rabinowitz | Senior partner of Howell, Shultz, and Rabinowitz, whose wedding reception fills the Grand Ballroom the night before the hit | Howell, Shultz, and Rabinowitz |
| Sarah Rabinowitz | The bride -- Sarah Ginsberg of the Seattle Federal Savings and Loan family, married to Levi Rabinowitz the night before the shareholders' meeting | Seattle Federal Savings and Loan |
| Alan Ginsberg | President of Seattle Federal Savings and Loan and father of the bride | Seattle Federal Savings and Loan |
| Earl Peabody | Fort Lewis car dealer of Davenport's build whose medical records, clone tags and second clone were quietly appropriated to provide a corpse | independent |
| Kyle Matthews | Dwarf paramedic and support gunner of DocWagon HTR team #27 out of Renton -- murdered so his team's ambulance and gear could be used for the extraction | DocWagon |
| Yolanda | Garrett Walsh's executive assistant -- the last friendly face Davenport passes on the way to the meeting that decides everything | DocWagon |

## Locations

| Name | Type | District | Notes |
|---|---|---|---|
| The Westin Seattle | hotel | Downtown (Fifth Avenue and Stewart Street) | Sixty floors in three towers the locals call the corncobs; headquarters and flagship of Westin International, most meeting space in the metroplex, and the site of the DocWagon hit |
| Fox's Tacoma Safehouse | safehouse | Northern Tacoma | A four-bedroom house indistinguishable from its neighbours, fully stocked, with a ritual attic and a smart-house security system -- and wired end to end with Fox's bugs |
| Lake Washington Waterfront Pull-Off | meeting site | West shore of Lake Washington, just outside downtown | The deserted waterfront lay-by just after dusk where Fox lays out the wetwork contract; no cover for eavesdroppers, no room for an ambush |
| The Kethers Building | corporate facility | Tacoma (1366 Crescent Boulevard) | DocWagon's Tacoma clone and tissue vault; Davenport's 'deniable assets' rerouted a second Peabody clone out of it, and that clone is the body in the ambulance |
| Reynolds Eternal Estates | cemetery / memorial park | Primrose Boulevard, Bellevue | The Bellevue memorial park where DocWagon buries a Fort Lewis car dealer's clone under Michael Davenport's name |

## Organizations (new)

| Name | Type | Tier | Notes |
|---|---|---|---|
| Rose Croix | corporation | 3 | The new competitor in metroplex emergency medical services, biomedical research and related contracts, founded on stolen DocWagon customer lists and security codes by a dead man |
| Westin International Hotel Corporation | corporation | 3 | Hotel chain whose flagship and headquarters is the three-towered Westin Seattle; runs the metroplex's largest meeting-space operation and its own private security staff |
| Howell, Shultz, and Rabinowitz | corporation | 2 | One of the most prestigious corporate law firms in the metroplex; senior partner Levi Rabinowitz's wedding reception fills the Grand Ballroom the night before the hit |
| Seattle Federal Savings and Loan | corporation | 2 | Metroplex savings and loan whose president, Alan Ginsberg, married his daughter to a senior partner of Howell, Shultz, and Rabinowitz |

## Existing organizations updated (sourced appends, nothing overwritten)

- **DocWagon** -- GM notes; leadership: Garrett Walsh, Michael Davenport, Margo Fleming; allies: Griffin Biotechnology, Knight Errant Security Services; enemies: Rose Croix, Paladin Medical Technologies
- **Lone Star Security** -- GM notes
- **Knight Errant Security Services** -- GM notes
- **Yamatetsu Corporation** -- GM notes; allies: Paladin Medical Technologies
- **Seattle Mafia** -- GM notes; leadership: Vincent "Numbers" Ciarniello
- **Yakuza (Watada-rengo)** -- GM notes; allies: Shotozumi-rengo
- **Griffin Biotechnology** -- profile; GM notes; leadership: Dr. Chandra Dasari; allies: DocWagon, Knight Errant Security Services
- **Paladin Medical Technologies** -- profile; GM notes; allies: Yamatetsu Corporation; enemies: DocWagon
- **Shotozumi-rengo** -- GM notes; leadership: Toju Shotozumi
- **Seattle Metroplex Guard** -- GM notes

## Existing locations / NPCs updated

- location: **Griffin Biotechnology Everett Research Facility**
- location: **DocWagon Snohomish Pharmaceutical Facility**
- location: **Harborview Medical Center**
- location: **Seattle General Hospital**
- location: **Fort Lewis**
- NPC: **Fox**
- NPC: **Dr. Fredericks**
- NPC: **Toju Shotozumi**

## Matrix systems -- to build in the Matrix designer (NOT built yet)

One mapped system. The book gives it in SR3 Matrix notation (security code / subsystem ratings and
a trigger-step table) rather than as a node map, so it is reproduced as printed.

**Westin-Seattle Hotel Computer Network** (p.19). Standard Matrix iconology throughout -- from the
entry node the whole system is visible with nothing hidden or unusual: the hotel control systems
(elevators, lighting, and the rest) on one side, the data files on the other, and in the distance a
connector to the private Westin International network that carries reservations and corporate data
between all Westin properties.

Security code: **Orange-5/9/9/8/9/9**

| Trigger step | Event |
|---|---|
| 3 | Probe-4 |
| 7 | Tar Baby-6 |
| 12 | Probe-6, Tar Pit-6, Passive Alert |
| 18 | Probe-6, Killer-6 |
| 25 | Tar Pit-6, Tar Pit-6, Killer-6 |
| 30 | Shutdown |

| File | Size | Contents and protection |
|---|---|---|
| Current Reservations | 2500 Mp | Every active reservation for the next four months: guest names, contact information, arrival and departure dates and times. Scramble-4 |
| Guest List | 2500 Mp | The current registry: names, addresses, phone numbers, current billing, and annotations on VIPs and their preferred services and meals. PAYDATA, 5,000-7,500 nuyen to the right fixer or fence. Scramble-6 |
| Duty Roster | 100 Mp | Every member of staff, position, pay rate and credstick ID code. Must be modified by anyone posing as hotel staff |
| Catering | 1500 Mp | Ballroom event schedules and special instructions, current and six months out: the Rabinowitz reception and the DocWagon shareholders' meeting, who runs each event, what security is being provided, menu, table set-up. No guest name lists -- those belong to each event's own coordinator |
| Inventory | 2000 Mp | Every material good in the hotel, from kitchen pots to the painting in room 1610 |
| Supplies | 1200 Mp | Consumables: linen, cleaning supplies, the little shampoo bottles |
| Contracts | 1800 Mp | All current hotel work contracts -- delivery, trideo, elevator licences, liquor licences. Scramble-4 |
| Logs | 3000 Mp | Four months of department logs, checklists and day-to-day paperwork; compressed and shipped to corporate for archiving every six months |
| Larder | 1500 Mp | Current foodstuffs and liquor for the restaurants and bars, plus recipes and purchasing schedules |
| Register | 1000 Mp | Pointers to actual funds -- 22,720 nuyen transferable to credsticks. Scramble-6 |

Consequences: an active alert raises hotel security for six hours; a full shutdown additionally
takes the system down for at least two hours, during which the hotel takes no reservations and
checks nobody out. Elevators, maglocks, fire control, lighting and HVAC are all under computer
control and therefore reachable from the control side of this host.

**Not mapped**: the private Westin International inter-property network behind the connector;
DocWagon Seattle's corporate system (where Davenport's encrypted caches are hidden, including the
file "H" that was in the Snohomish plant -- his biometrics plus a secret passcode, otherwise years
to break); the DocWagon dispatch system, where an executive can keep HTR corporate bracelets from
registering; and the safehouse smart-house system (Sensors 4, Maglock 6, and Fox's bugs).

## Flavor / not built

- **Trader Vic's**, **The Emerald Room** and **the Elven View** (the Westin's three first-class
  restaurants), the **Lobby Bar** and the **Fifth Avenue Corner Cafe**, and the named function rooms
  from the handout maps (**Vashon I-II**, **Whidbey**, **Orcas**, **Blakely**, **Cascade Ballroom**,
  **Glacier Peak**, **St. Helens**, **Stuart**, **Baker**, **Adams**, **Olympic**, **Stanwood**,
  **Emerald City Gallery**, **Elliott Bay Room**) -- all folded into the Westin Seattle row.
- **The Grand Ballroom** itself -- the adventure's climax happens in it, but it is a room in the
  hotel, described in full on the hotel row rather than given a location of its own.
- **AG Chemie of Europe** -- the European partner on the defense contract, a pure name-drop; recorded
  on the Yamatetsu and Paladin rows.
- **The university clinic** that contracted for Snohomish overage -- unnamed; on the Snohomish row.
- **The unnamed CFO** of DocWagon Seattle (second speaker at the meeting), the **Master of
  Ceremonies**, the **DocWagon security director** who ran Davenport's black operations, and
  **Davenport's decker** who hid and encrypted the caches -- unnamed roles, on the DocWagon and
  Davenport rows.
- **The extraction team** (the shaman with the greater form city spirit, the rigger, the mages with
  Improved Invisibility anchoring foci) and **the shadowrunner mage in the audience** -- deliberately
  statless in the book, uncapturable by design; on the Rose Croix row.
- **Dr. Dasari's two bodyguards**, the **personal bodyguards** and **contracted private security** at
  the Rabinowitz reception, **Westin hotel security** and the **DocWagon special ops team** -- stat
  blocks and behaviour on the Westin International, Howell Shultz and Rabinowitz, and DocWagon rows.
- The Shadowland posters on the handout -- **Hondo**, **The Chromed Accountant**, **Skeptic**,
  **Penny Ante**, **Sweet Gypsy Rose** and **Deacon Blues** -- board handles with no face and no
  location; their claims are recorded on the Davenport and Kyle Matthews rows. Penny Ante (Matthews's
  childhood friend) and Deacon Blues (who names HTR team #27) are the two worth promoting to real
  NPCs if a GM wants the loose end chased.
- The **simsense starlet** whose dress gets a tray of drinks, the **boisterous old friend** of the An
  Old Friend scene, and the **wedding relative** hunting for a shared college past -- roles the GM
  casts to fit the table, not fixed people.
- **Howell** and **Shultz** (the other two named partners of the law firm) -- on the firm's row.

## GM play notes

- This is a Shadowrun Missions convention scenario, so it is written for a table of strangers with
  a four-hour clock. Two structural things follow: the main line (Crossed) is five scenes long, and
  the Crossed Again section is a pile of optional scenes to spend spare time on. Pick from Crossed
  Again by what the table lacks, not in printed order.
- The whole adventure is a rail with one honest purpose: the runners must succeed, and their success
  must be someone else's plan. The book states outright that they will never find the safehouse
  bugs, never catch Fox reporting, never capture an extraction-team member, and that the ambulance
  explodes no matter what they hit it with. If your table hates being handled, the fix is not to
  break the plot but to let them work out afterwards that they were used -- the handout's Shadowland
  thread is written to hand them exactly that.
- Fox's presence on the run is non-negotiable and players will push back. Sell it as value: an extra
  gun, a driver, a decker, contact access, temporary IDs and a 20 percent gear discount. He is 'as
  good as you need him to be'.
- Mind-affecting magic is the one real threat to the deception. Fox avoids mages with Mind Probe or
  Analyze Truth on their sheet, and if he thinks he is being probed he stops talking and adds the
  Table Rating to his Willpower while singing 'Row Your Boat'. If a mage gets through anyway, they
  learn he reports the team's plans and nothing more -- he genuinely does not know why, and does not
  believe the team is being crossed.
- Payment scales with Table Rating: 10,000/12,000 green up to 30,000/40,000 prime, 20 percent
  available up front, gear at a 20 percent discount, captured hardware fenced at 20 percent of book
  (which can beat street price where the Street Index is under 1).
- The White Doves scene exists so a character who will not do wetwork is rewarded rather than
  benched: the player runs a second character (an established one, or an SR3 archetype -- never a
  freshly generated one), the pacifist keeps the Karma including a bonus point, the surrogate keeps
  the money. At a multi-table event, ask whether the player would rather move tables, and never push
  a table below four players to do it.
- Zero Hour wants miniatures or markers. The runners get one free combat turn on the trigger phrase
  before initiative. Hotel and DocWagon security try to capture, then to herd them into the street
  for Lone Star; anyone maintaining a cover identity and not shooting is ignored. Personal
  bodyguards only fire if their charge is threatened. Five turns brings two patrol cars and TR d6
  contract guards, twelve brings a Lone Star response team.
- Do not let a runner reach Davenport's body. If one closes, a panicking would-be hero's stray shot
  'hits' him, and he shoves Fleming and his assistant away shouting at them to run -- staged so that
  nobody examines him. Prefer mundane countermeasures over magic so a watching mage sees nothing;
  where magic is needed, the planted mage casts in the segments around the attack.
- Insider Trading can be run more than once with different runners: Ciarniello for Mafia contacts,
  Toju for yakuza, Fredericks for corporate, Hollingsworth for high society. Easy way for faces,
  hard way (gamma-scopolamine and a truth-drug interview) for everyone else.
- Ambush! is the pacing valve. Use it when the team over-plans. If they are all captured, Fox
  escapes, hires a rescue team, and they resume the run with a hardened target and less time --
  which is a better outcome than a TPK and the book says so.
- Karma: 1 for the 'elimination', 1 for no unnecessary collateral damage or dead innocents, up to 3
  individual, maximum 5 (6 with White Doves). Runners who behaved professionally, took command and
  made Fox look good can take Fox as a contact.
- Arc hooks to plant now: Peabody's swapped medical records; the missing dwarf Kyle Matthews; who
  actually blew up Snohomish; the file "H"; Dasari and her unopened lab; and Margo Fleming, who was
  close enough to Davenport to have noticed the preparations. Every one of them pays off better if
  the team first believes it did a clean job.

