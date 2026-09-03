# Celtic Double-Cross -- Adventure Prep: NPCs, Locations, Organizations, Matrix Systems

Source: Shadowrun 2e - Adventure - Celtic Double Cross {FASA7315}.pdf, pp. 4-79. Campaign order #20, in-game 2054.

Everything below is loaded into the campaign DB flagged `is_active: false` and `source_adventure: "Celtic Double-Cross"` by `python scripts/adventure_ingest/run.py celtic_double_cross`; flip entries active as the party meets them. Use the **Adventure** filter on the manage pages to see just this set.

## Plot synopsis

Over lobster in a ritzy restaurant, the polished aide **James Wassall** hires the runners as
"peripheral surveillance" for a politician whose own security "is potentially compromised": 2,500
nuyen a day each for five days, full medical, fly out in two days, tell nobody. The Boss turns out to
be **Pat MacNamara**, self-made millionaire and independent candidate for mayor of New York, making
the traditional pilgrimage to the **John F. Kennedy Memorial Park** in **Tir na nOg** to press flesh,
look up ancestors and cut a transport deal with the elven nation's communications and transport
giant **O'Toole Transcom**. The Tir bans private security and MacNamara does not want the black-beret
**Tir Republican Corps** in his photo-ops, so a few out-of-town faces with wristphone panic buttons
will do. At JFK the runners meet the entourage: chief of staff **Caspar Rosenberg**, press secretary
**Anthea Brown**, the towering elf "tour guide and translator" **Nathair MacSweeney**, the spin
doctor **Peter Lewis**, the money decker **Xavier Almodovar**, Brown's neglected chip-head assistant
**Petra Johnson**, and six wired bodyguards in long coats.

Two days of easy money in Dublin follow -- the **Flathail Hotel**, museums, Bloduedd's -- with one
scripted moment: at the O'Toole luncheon the dazzling **Bridgit O'Toole** (or her brother **Padraic**)
picks the team's most charismatic member out of the grunts' suite and asks him to peel her a grape.
Petra, ignored, is the other contact worth making. Unnoticed, O'Toole staff hand the entourage plans
of the company's docks at **Rosslare Harbor**.

What the runners do not know: MacNamara owes the Mob. In exchange for silence about the kickbacks and
the **Gambaccini family** deal that built his fortune in New Jersey in '39, the family's fledgling
Irish branch wants the Rosslare plans so it can smuggle BTLs into the Tir. On Day 4, after the JFK
Park photo-ops, MacSweeney springs a "change of itinerary": two Hughes Stallions to **Altan Lodge**
in Glenveagh National Park, County Donegal, where Rosenberg hands the printouts to tall dark men in
overcoats with cyber-troll bodyguards. An hour in, a mortar round takes the west wing. MacSweeney
tipped the **Irish National Liberation Army**, which does not want the Mafia muscling in on its
rackets; its price was that no elf be shot and one chopper left intact. MacSweeney, Rosenberg and
most of the mobsters lift off while the second helicopter explodes, and the elf screams "Traitors!
Only you knew!" across the garden. Three four-man INLA cells on Kamikaze close in through the fog.

The runners are alone in a national forest at night, hunted by fomorians, with pistols, a dead capo's
signet ring and the Rosslare plans. MacSweeney -- a Tir Tairngire sleeper agent, distant cousin of
Prince **Aithne Oakforest**'s wife, Grade 3 initiate of the elven **Order of Stars**, who despises
MacNamara as a racist -- has the Danaan-mor druid **Dominic O'Brien** plant a fake INLA history for
one of them in the TRC's Derry system, tips the Garda at 3 a.m., and by dawn is at **Boyle Abbey**
on Lough Key negotiating elven affairs with O'Brien while the entourage quietly moves hotels and
flies home without them. From 4 a.m. Day 5 the TRC officer **Mairtin O'Neill** and his squad are on
the road. The runners must run a visible-action tally, steal cars, phone contacts across the
Atlantic, cultivate Petra and Bridgit, deck a rural Garda station and the brutal sculpted TRC host,
and find a way out: a blackmail deal with MacNamara (who will happily double-cross them into a jet
full of TRC commandos), a surrender to O'Neill that turns into a sanctioned raid on Boyle Abbey, or
an elven concord with O'Brien himself -- who, once he learns he was fed lies, turns on MacSweeney and
offers safe passage and future work for the Tir.

## Timeline

- **2039** -- MacNamara's New Jersey satellite-suburb contract: kickbacks to planning officials
  Fitzwalter and Stein and a deal with the Gambaccini family ("before the Consortium took over the
  show"). The same year Boston police question Caspar Rosenberg over the Scions of the Rose
  disappearances. **2040-45** MacSweeney's hermetic studies at University College Dublin, paid by
  Aithne Oakforest. **2047, 2050** Peter Lewis's two stints at the Cooper-Klein clinic. **January
  2051** MacSweeney joins the MacNamara entourage.
- **Before the job** -- the Portland emissary Corrame meets MacSweeney: a Mob file on MacNamara in
  exchange for mediating a family matter with Dominic O'Brien; "get some strangers into the
  entourage". Wassall's dinner offer; two days later the JFK briefing.
- **Day 1** -- 10:00 EST briefing at JFK; noon orbital; 8:00 p.m. GMT Shannon (foreign minister
  O'Kennedy, treasury minister Richard O'Toole, TRC at the crowd's edge); 9:00 p.m. Dublin, President
  O'Dunn, motorcade to the Flathail Hotel.
- **Day 2** -- Chamber of Commerce breakfast; Trinity College, Leinster House, the museum; noon O'Toole
  luncheon (Dark Blue Eyes; the Rosslare plans change hands); 2:00 p.m. Renraku Eireann-Tir at Dun
  Laoghaire (runners free); 9:00 p.m. Bloduedd's.
- **Day 3** -- 10:30 walkabout ("the perennial nightmare"); Dublin Castle luncheon with the Mayor;
  4:00 p.m. O'Toole talks at the Eireann-Tir Tours offices; Dublin Castle dinner and the Order of
  Brigid's play.
- **Day 4** -- Wexford: JFK Memorial Park walkabout, Robert Kennedy Lodge lunch, Genealogy Exhibition;
  5:00 p.m. to Shannon and the Inter-Tir Hotel; 8:00 p.m. the "Connaught business meeting" at Altan
  Lodge; **~9:00 p.m.** the INLA attack. 8:00 p.m. the false INLA file goes into the TRC computers;
  9:40 p.m. MacSweeney and Rosenberg brief MacNamara at the Inter-Tir.
- **Day 5, small hours** -- 1:00 a.m. Petra overhears the spin meeting ("go to the boil"); 2:15 it
  breaks up; 2:30 the entourage moves to the Shannon Bridge Hotel, leaving the runners' gear; 3:00
  MacSweeney tips the Garda, Connaught calls monitored; 3:15 Garda at Altan Lodge; 3:20-3:25 INLA and
  the runners named to the TRC; 3:55 the capo's body logged; **4:00 warrants, the TRC hunt begins**;
  6:00 MacSweeney at Shannon airport, all calls out of the Tir monitored; 6:25 MacSweeney at Boyle
  Abbey; 7:00 a Garda team reaches the McDonnell farm; 8:00 the alert goes Tir-wide; 9:30 banks open.
- **Day 5, official** -- 9:00 Knocknarea and Rathcroghan with the Order of Ogma; 12:30 Roscommon
  Castle with taoiseach Martin O'Connor; 3:00 p.m. helicopter to Shannon; 4:00 p.m. orbital to JFK.
  Everyone but MacSweeney leaves on schedule. The runners have a day to deal with him.
- **Days later, New York** -- "Opinion Polls Point to MacNamara Win" (7-point lead over Andrew T.
  Small; "former aide" MacSweeney's criminal affiliations exposed) or "MacNamara Campaign in Ruins"
  (dropped out; Donegal Mafia meeting; the New York Sentinel's kickback story).

## NPCs (Persons of Interest)

| Name | Role | Org |
|---|---|---|
| Pat MacNamara | Independent candidate for mayor of New York; self-made millionaire with a Mafia debt; the Boss the runners never really meet | MacNamara Campaign |
| James Wassall | MacNamara's polished aide and fixer who recruits and briefs the runners; loyal while there is a career in it | MacNamara Campaign |
| Caspar Rosenberg | MacNamara's patronizing chief of staff who hands the Rosslare plans to the Mob at Altan Lodge; a Scions of the Rose skeleton in Boston | MacNamara Campaign |
| Anthea Brown | MacNamara's relentlessly efficient press secretary and speechwriter; ju-jitsu practitioner; sits on the Altan Lodge news to protect the Day 5 photo-op | MacNamara Campaign |
| Peter Lewis | MacNamara's egregious little spin doctor -- 'image-profile analyst' -- and a twice-treated BTL addict | MacNamara Campaign |
| Xavier Almodovar | MacNamara's handsome, money-obsessed business decker who runs the Matrix checks that 'confirm' the runners' terrorist links | MacNamara Campaign |
| Petra Johnson | Anthea Brown's neglected, chip-head media analyst -- the runners' best inside contact once they are hunted | MacNamara Campaign |
| Nathair MacSweeney | The double-crosser: MacNamara's elven image consultant, a Tir Tairngire sleeper and Order of Stars initiate who tips the INLA and frames the runners | MacNamara Campaign |
| Bridgit O'Toole | Breathtaking 24-year-old division head of O'Toole Transport Systems who picks a runner out of the grunts' suite; the team's rich, bored, dangerous friend | O'Toole Transcom |
| Padraic O'Toole | Bridgit's brother and MacNamara's other chief negotiator; takes her role with a female runner, and his father lets him do as he pleases | O'Toole Transcom |
| Seamus O'Toole | Grizzled Danaan-mor patriarch, president and CEO of O'Toole Transcom, 'a wily old devil' who has any man seen with his daughter tailed | O'Toole Transcom |
| Maire O'Toole | Seamus O'Toole's other daughter, kept under the same tight rein as Bridgit | O'Toole Transcom |
| Richard O'Toole | Tir na nOg treasury minister, Danaan-mor, lurking on the Shannon tarmac to greet MacNamara | Tir na nOg |
| Samuel O'Kennedy | Tir na nOg foreign minister who shakes MacNamara's hand on the Shannon tarmac | Tir na nOg |
| William O'Dunn | President of Tir na nOg; welcomes MacNamara at Dublin airport and shares prime-time drinks | Tir na nOg |
| Graeme Patrick Finnegan | The Worshipful Mayor of Dublin, MacNamara's Day 3 luncheon host at Dublin Castle | Tir na nOg |
| Martin O'Connor | Taoiseach of Tir na nOg; hosts the Day 5 lunch at Roscommon Castle | Tir na nOg |
| Judge Martin MacNamara | Immensely influential member of the Danaan Council of Stewards; the Day 5 handshake Anthea Brown protects by burying the Altan Lodge news for six hours | Tir na nOg |
| Dominic O'Brien | Grave, quiet Danaan-mor druid of the Council of Stewards, CEO of Sculpted Environmental Systems; planted the forged files, then turns on MacSweeney and offers the runners a way home | Sculpted Environmental Systems, Inc. (SES) |
| Mairtin O'Neill | TRC oifigeach, Reach Fuileach assassin and physical adept leading the hunt for the runners; curious enough to take them alive, and ready to send them at Boyle Abbey | Tir Republican Corps (TRC) |
| Corrame | Tall elder elf, emissary from Portland, who recruits MacSweeney for Tir Tairngire's plot in the prologue | Tir Tairngire |
| Aithne Oakforest | Tir Tairngire prince who paid for MacSweeney's education, runs him as a sleeper, and is quietly linking elven interests across the world | Tir Tairngire |
| Hugh McDonnell | Donegal farmer with an ancient shotgun and two sons, tracking a fomorian pack; the cavalry in the forest and a night's whiskey | independent |
| Rory McDonnell | Hugh McDonnell's son, owner of a Radio Shack deck that 'fell off the back of a lorry' and no idea how to use it | independent |
| James McDonnell | Hugh McDonnell's other son; shotgun, pitchfork and questions about America | independent |
| Cormac Roche | Aging, unemployed elven actor of the Roche Danaan-mor family of Munster, full of Guinness, blarney and O'Toole scandal | independent |

## Locations

| Name | Type | District | Notes |
|---|---|---|---|
| John F. Kennedy International Airport | transportation hub | Queens, New York (UCAS) | Chaos in action: the VIP-lounge briefing, the permits, the contraband deposit box and the noon orbital to Shannon |
| Shannon International Airport | transportation hub | Shannon, a small sprawl on the west coast (Munster) | One of the Tir's two international airports: MacNamara kisses the tarmac, the Garda work customs and the TRC lurk at the crowd's edge |
| Dublin International Airport | transportation hub | North of the city | Where President O'Dunn welcomes MacNamara on Day 1 and the private jet to Wexford leaves on Day 4 |
| Flathail Hotel | hotel | Fitzwilliam Street, central Dublin | The entourage's Dublin base: the fifth floor booked, the James Joyce suite for the bigwigs, the Mary Margaret O'Hara suite for the grunts |
| Bloduedd's Night Club and Restaurant | nightclub | Central Dublin (Tir na nOg sourcebook p.114) | Elves-only society club where the Day 2 reception for Tir businessmen, media and artists is held -- 'NO TROLLS, ORKS, OR DWARFS' |
| Dublin Castle | government building | Central Dublin | Seat of the Dublin City Corporation and the Leinster Assembly; the Mayor's luncheon and the state dinner with the Order of Brigid's play |
| Trinity College (Dublin) | university | Central Dublin | First stop of the Day 2 cultural motorcade |
| Leinster House | government building | Central Dublin | Day 2 cultural-tour stop; Garda cordon at the doors |
| Natural History Museum (Dublin) | museum | Central Dublin | Where MacNamara admires 'relics of reputed ancient MacNamara family scions' for the cameras on Day 2 morning |
| Eireann-Tir Tours Offices | corporate facility | Central Dublin, near the DART rail line | Offices where MacNamara holds the Day 3 trade talks with the O'Toole Transcom directors; runners on station outside from 3:00 p.m. |
| Brendan's Wine Shop | shop | 22 Chancery Street | Exclusive wine merchant; advice here on an unusual champagne wins Bridgit O'Toole's heart faster than a diamond |
| Niall MacGuinness's Flat (Curtis Street) | safehouse | Curtis Street, just off York Street | Empty flat of a friend of a friend of Bridgit's, owner on holiday for a week; break in and keep the trideo down |
| Bridgit O'Toole's Penthouse | penthouse | Off Chichester Street, central Dublin | Bridgit's penthouse suite; she never brings the runners here and will not come alone to their flat |
| O'Toole Transcom Dun Laoghaire Outstation | corporate facility | Dun Laoghaire, on Dublin Bay | The O'Toole site where runners who surrender their weapons to Bridgit's security can deck in peace on a Fairlight Excalibur -- until the TRC knock |
| De Valera Habitat (Renraku Eireann-Tir) | corporate facility | Dun Laoghaire | Renraku's Tir subsidiary habitat at Dun Laoghaire; MacNamara talks to its executives on Day 2 afternoon under Renraku's own security |
| Inter-Tir Hotel | hotel | Near Shannon International Airport | The Day 4 hotel; MacSweeney springs the 'change of itinerary' from his room here and the entourage sneaks out at 2:30 a.m., leaving the runners' gear and decoy watchers |
| Shannon Bridge Hotel | hotel | Near Shannon International Airport | Where MacNamara hides after 2:30 a.m. Day 5; its simple Matrix host holds the helicopter booking to Boyle Abbey |
| Altan Lodge | country house | Glenveagh National Park, County Donegal (Ulster) | Grand old Irish mansion in a floodlit clearing where the Mafia meeting is mortared by the INLA; three bodies, the Rosslare plans and a capo's ring in the west wing |
| McDonnell Farm | farm | About eight kilometers southwest of Altan Lodge | Hugh McDonnell and his sons' farm: whiskey, a bed, a map, petrol, an ancient truck and a cheap Radio Shack deck that fell off a lorry |
| INLA Base (Enniskillen) | terrorist base | County Fermanagh (Ulster) | The base from which an anonymous cell commander passes the Altan Lodge orders by password an hour before the meeting |
| John F. Kennedy Memorial Park | landmark / monument | County Wexford (Leinster), by Wexford Airport | The traditional pilgrimage for Irish-American politicians: JFK Memorial, the Robert Kennedy Lodge and the Genealogy Exhibition where MacNamara 'finds' his ancestors on camera |
| Rosslare Harbor (O'Toole Transcom Port) | transportation hub | Southern Tir coast (County Wexford); ferries to Fishguard, Cherbourg and Le Havre | The southern port handling much of the European ferry trade; O'Toole's docks and cargo-transfer plans are what the Mob wants for BTL smuggling |
| Boyle Abbey | corporate headquarters | Lough Key Forest Park, Connaught | SES headquarters and Dominic O'Brien's home: a thorned hedge that grabs, spine-firing plants, a slowing lawn, water elementals in the carp ponds, gas-spraying motion detectors -- and the endgame suite |
| Roscommon Castle | government building | Connaught | Where taoiseach Martin O'Connor hosts MacNamara's Day 5 lunch; security operatives wait outside the grounds |
| Knocknarea and Rathcroghan (Sacred Sites) | landmark / monument | Sligo (Knocknarea) and Roscommon (Rathcroghan) | Celtic ritual sites toured with the Druidic Order of Ogma on Day 5 morning -- the photo-op with Judge Martin MacNamara that Anthea Brown protects at any cost |
| TRC Station, Derry | police station | Derry (Ulster) | The TRC station every Connaught police alert reports to, and home of the sculpted Red-7 TRC host that holds the runners' forged terrorist file |

## Organizations (new)

| Name | Type | Tier | Notes |
|---|---|---|---|
| Tir Republican Corps (TRC) | state security / counter-terrorism | 4 | Jet-black uniforms, black berets, wrap-around sunglasses, almost all elves: the hardened anti-terror commandos who hunt the runners from 4 a.m. Day 5 |
| Reach Fuileach | elite assassin unit (TRC) | 3 | 'Bloody body' -- the TRC's physical-adept assassins in magical armor and spell locks; the deadliest killers in Tir na nOg (Tir na nOg p.152) |
| Order of Cu Chulainn | magical order (TRC) | 3 | The TRC's hermetic path: warrior-mage initiates who use a ritual wardance for metamagic; Cu Chulainn is the favorite decker persona |
| Garda (Tir na nOg) | civilian police | 3 | The Tir's mostly human civilian police: black uniforms with white edging, flat white caps, NN-15s and shock batons; they cordon crowds and hand terrorism to the TRC |
| O'Toole Transcom | communications and transport corporation | 4 | Tir na nOg's communications and transport giant, run by the Danaan-mor patriarch Seamus O'Toole; its Rosslare port plans are the Mob's price |
| Sculpted Environmental Systems, Inc. (SES) | ecological research corporation | 4 | Dominic O'Brien's major Tir corporation: underground caverns and buildings through Lough Key forest, 'sculpting' plant ecologies that detoxify soil -- and guard the abbey |
| Druidic Order of Ogma | druidic magical order | 4 | The Tir's druidic path; its members escort MacNamara round the sacred sites on Day 5 and its Grade 8 initiate Dominic O'Brien holds Boyle Abbey |
| Order of Stars | elven hermetic order | 3 | Secretive elves-only hermetic order that shares magical learning across countries and quietly brokers high-level political contacts; MacSweeney is a Grade 3 initiate |
| Order of Brigid | cultural / bardic order | 2 | Performs musical and poetic entertainments at the Dublin Castle state dinner, including Doncha O'Brien's play 'The Destiny of Ages' |
| Irish National Liberation Army (INLA) | terrorist / organized crime | 3 | Terrorist-gangster army of fanatical psychopaths on Kamikaze who mortar Altan Lodge to keep the Mafia out of their rackets -- and whom the runners are framed as fundraising for |
| Ulster Revolutionary Force (URF) | terrorist / paramilitary | 3 | The more organized Ulster Protestant paramilitary: attacks on government and military targets, broadly anti-metahuman; intermittently at war with the NURM |
| New Ulster Revolutionary Movement (NURM) | terrorist / paramilitary | 3 | Hard-line Ulster Protestant terrorists who hit economic and civilian targets and are openly anti-metahuman; 'relatives blown up by the NURM' fuel Tir anger at American money |
| Irish Republican Army (IRA) | terrorist / anti-elven insurgency | 3 | The old Republican brigades, now an anti-elven-rule movement with ork and troll members, split into Official and Provisional IRA |
| Gambaccini Family | Mafia family | 4 | East Coast Mafia family that owns MacNamara's past and wants the Rosslare plans to smuggle BTLs into the Tir; a capo dies at Altan Lodge |
| MacNamara Campaign | political campaign | 3 | Pat MacNamara's independent run for mayor of New York -- image consultants, a spin doctor, a chip-head media analyst, a money decker, six beta-wired bodyguards and an elven traitor |
| Scions of the Rose | pseudo-hermetic cult (broken up) | 2 | Boston pseudo-hermetic group whose 'very nasty rituals involving kids' followed a rash of missing orphans in 2039; Rosenberg was questioned and released |
| Liptons | anarchist street-theatre troupe | 1 | Infamous theatrical anarchists and guerrilla poets who wreck public-relations events with impromptu street theatre -- non-violent, unstoppable |
| Radio-Trideo Eireann-Tir (RTET) | national broadcaster | 3 | Tir na nOg's national broadcasting company; its street reporters would love an American's on-camera opinion of Pat MacNamara |
| Inflame | underground broadsheet | 1 | Underground cultural broadsheet, a prohibited document under the Tir's cultural laws; its reporter wants the latest UCAS entertainment gossip |

## Existing organizations updated (sourced appends, nothing overwritten)

- **Tir na nOg** -- profile; GM notes; leadership: William O'Dunn, Samuel O'Kennedy, Richard O'Toole, Martin O'Connor, Graeme Patrick Finnegan, Judge Martin MacNamara, Dominic O'Brien; enemies: Irish National Liberation Army (INLA), Ulster Revolutionary Force (URF), New Ulster Revolutionary Movement (NURM), Irish Republican Army (IRA)
- **Tir Tairngire** -- GM notes; leadership: Aithne Oakforest
- **Humanis Policlub** -- GM notes
- **Renraku Computer Systems** -- GM notes
- **Aztechnology** -- GM notes

## Matrix systems -- to build in the Matrix designer (NOT built yet)

Decking is central to the second half ("an experienced decker ... will greatly increase the group's
chance of success"). Every mapped system is below; the TRC host is the big build.

**Access notes.** The public **treuntas** system (Tir na nOg pp.18, 161) gives maps, rail and road
data and news with no test; it never reports Altan Lodge. Its public bulletin board on terrorism
auto-triggers an Orange-2 trace-and-report (fail: +2 tally). The national **TTG-SAN** is Red-5; every
run into a foreign database is +1 tally, +2 for a second run from the same place, and so on. Civil
**aviation** and **land registries** open on Computer (4) (the Stallion; Altan Lodge's owner James
Mairtin MacSweeney). Rural runners need an Electronics (B/R) (4) makeshift commline interface. Visible
actions: any police datastore +1, TRC DS-17 +2. Gear: anything under a Fuchi Cyber-6 has little chance
against the TRC; Bridgit or O'Neill can supply a Fairlight Excalibur (Bridgit's has a cutting-edge
anti-trace). Rory McDonnell's Radio Shack PCD-100 (all programs at 2) is the desperate option.

**1. Small Police System** (p.43) -- a typical rural Garda station; deck one for the TRC's SAN numbers.

| Node | Function | Rating / IC |
|---|---|---|
| SAN-1 | Matrix access | Orange-3 |
| SPU-1 | Traffic to the CPU and station terminals | Orange-2, Access 4, Tar Baby 4 |
| DS-1 | Civil monitoring, traffic, public order | Orange-2, Access 4 |
| DS-2 | Local crime, nothing on organized crime or terrorism | Orange-4, Access 5, Trace and Dump 4 |
| I/OP-1 | Main station terminal | Orange-4, Access 5, Barrier 4 |
| CPU-1 | System horsepower | Orange-4, Tar Pit 4, Barrier 5 |
| SPU-2 | Guards the sensitive datastores | Orange-4, Barrier 5, Trace and Dump 4 |
| DS-3 | Personnel records (not sensitive; the Garda are just paranoid) | Orange-4, Access 4 |
| DS-4 | Directory: Matrix and phone numbers, emergency services, military, a TRC directory -- the access SANs of the TRC Derry system | Orange-4, Barrier 5 |
| DS-5 | Out-of-date archives, unreliable informant data | Orange-3, Access 4 |
| DS-6 | Sensitive current cases: after 3:30 a.m. Day 5 (Connaught stations; all stations after 8 a.m.) a factual summary of the Altan Lodge attack -- the runners armed and dangerous, terrorist affiliation, no details | Orange-4, Access 4 |
| SPU-3 | District traffic signals | Orange-3, Access 4 |
| I/OP-2 | Relay between signals and SPU-3 | Orange-3, Access 4 |

Timing: nothing before 3:00 a.m.; from 3:30 a general alert to forces within 160 km of Altan Lodge
(describes the runners, orders sightings reported to the TRC station in Derry); Tir-wide at 8:00 a.m.

**2. TRC Derry System** (pp.44-46; identical systems at Armagh and Dublin). A **sculpted** system
(Virtual Realities): organic and pastoral motif. TRC decker personas are mythic Irish heroes, usually
Cu Chulainn with a terrifying aspect; datastores are subterranean burial cairns, files oval stones
covered in Celtic designs and Gaelic characters. Access IC a bolted wooden gate; Barrier a thorny
hedge; Scramble a sorceress with a rosewood wand who smiles beatifically as a file dies; Blaster
mythic animals (bears, boars, stags, horses) attacking as the beast would; Killer a fomorian, an
each-uisge, or a harmless-looking leshy with a long pin; Tar Baby a banshee that clutches utilities,
wails and fades; Tar Pit a peat bog becoming an oil slick; Trace programs Irish wolfhounds; Trace and
Burn a fire-breathing black dog; Black IC a Reach Fuileach assassin, or a sword-wielding elven mage in
a brown or gray Celtic-patterned cloak who fights like a physical adept (TRC deckers wear the same).
The sculpted reality imposes itself on intruders (a rustic peasant in excrement-covered rags): at
each node roll MPCP dice against the node rating (the Red-7 SAN needs 4 successes at 7+); failure is
-2 Reaction for the run, one retry per new node at +2. Hostile TRC decker on 1D6: 1 (no alert), 1-2
(passive), 1-3 (active); a 6 on a second die brings another. TRC decker: Decker archetype, Attack 6,
Shield 2, Mirrors 2, persona programs 6, Fuchi Cyber-7 with response increase 2. Run it like a video
game; substitute acid and jammer from Virtual Realities freely; the decker should get the data but
have the ride of his life.

| Node | Function | Rating / IC |
|---|---|---|
| SAN-1, SAN-2 | Twin access nodes | Red-7, Access 4, Trace and Report 4 |
| CPU-1 | Horsepower for the terrorism subsystem | Red-7, Barrier 5, Blaster 5 |
| SPU-1 | Guards CPU-1 from SAN-1 | Red-5, Access 5, Trace and Dump 5 |
| SPU-2 | Guards one subset of terrorism files | Red-5, Black 4, Killer 5 |
| DS-1 to DS-5 | Active terrorist organizations by province (DS-1 Ulster, DS-2 Leinster ... DS-5 Connaught). DS-5 gains the Altan Lodge file at 3:15 a.m. (firefight, terrorists), 3:25 (INLA confirmed, runners present, 'anonymous source'), 3:55 (a known Irish Mafia body recovered) | Red-5, Scramble 5, Tar Pit 5 |
| SPU-3 | Guards DS-6 | Red-6, Access 6, Trace and Burn 6 |
| DS-6 | Individuals outside the Tir: exiles and foreign citizens tagged as terrorist sympathizers (accuracy varies; blackmail and media value). The team decker's own falsified history | Red-8, Barrier 6, Scramble 8, Trace and Report 6 |
| SPU-4 | Guards recent-terrorism files | Red-6, Black 2, Access 6, Trace and Burn 6 |
| DS-7 to DS-12 | Terrorist tactics and activity of the past 12 months by province (DS-12 nationwide analyses); DS-11 duplicates DS-5 on the runners; the file on the runner courting Bridgit is cross-referenced from DS-14 | (as DS-1 to DS-5) |
| SPU-5 | Guards DS-13 | Red-7, Black 5, Barrier 7, Killer 6 |
| DS-13 | Ongoing anti-terrorist operations; updated only by senior officers, so nothing on Altan Lodge or the runners -- but the details of MacNamara's double-cross ambush are entered here | Red-7, Access 6, Scramble 6, Tar Pit 6 |
| CPU-2 | Main 'mobile' computing power | Red-8, Black 4, Barrier 6, Blaster 6, Trace and Dump 6 |
| SPU-6 | Guards DS-14 | Red-7, Black 6, Access 7, Trace and Dump 6 |
| DS-14 | Selected information on members of the Danaan-mor: 900,000 nuyen (30,000 per 10 Mp) and selling it attracts TRC assassins; Bridgit O'Toole's file; Dominic O'Brien's file, whose numeric authority code suppressed MacSweeney's record | Red-8, Black 6, Barrier 6, Scramble 8 |
| SPU-7 | Controls DS-15, DS-16, DS-17 | Red-5, Barrier 5, Tar Pit 5 |
| DS-15 | Economic terrorism | Red-7, Access 6, Trace and Burn 5 |
| DS-16 | Criminal economic enterprises of foreign terrorist groups and organized crime; 4:02 a.m. file: Mob involvement at Altan Lodge, analyzed as an INLA strike to keep the nascent Irish Mafia branch out | Red-6, Access 6, Tar Baby 5 |
| DS-17 | Foreign visitors of the past 12 months -- backgrounds, histories, itineraries (500,000 nuyen; 10,000 per 10 Mp). 'MacNamara Boys' file = Legwork p.62; MacSweeney's entry 'suppressed by the authority of' a numeric code (hard copy only); the runners' own files duplicate DS-5/DS-11 | Red-5, Access 4, Tar Pit 4 |
| SPU-8 | CPU-1 to CPU-2 | Red-4, Access 4, Trace and Report 4 |
| SPU-9 | CPU-2 to CPU-3 | Red-4, Access 4, Trace and Report 4 |
| CPU-3 | Power for one large and one small datasystem and the I/O SPUs | Red-7, Barrier 5, Blaster 5 |
| SPU-10 | Guards CPU-3 from the SAN | Red-5, Access 5, Trace and Dump 5 |
| SPU-11 | Guards DS-18 to DS-21 | Red-7, Barrier 6, Trace and Dump 5 |
| DS-18 | All registered Tir hermetic mages (60,000; 6,000 per 10 Mp) | Red-6, Barrier 6, Trace and Dump 6 |
| DS-19 | All registered shamans and non-elven druids (12,000; 3,000 per 10 Mp) | Red-6, Barrier 6, Trace and Dump 6 |
| DS-20 | Groups suspected of cultural crimes (Tir na nOg p.44) | Red-4, Barrier 5, Trace and Dump 5 |
| DS-21 | Members of the hermetic orders of the Paths (30,000; 3,000 per 10 Mp); Dominic O'Brien: Druidic Order of Ogma, high rank, residence Boyle Abbey | Red-7, Black 5, Barrier 6, Trace and Burn 6 |
| SPU-12 | Guards DS-22 | Red-7, Black 5, Barrier 7, Scramble 7, Trace and Burn 6 |
| DS-22 | Experimental research on the morph-seeking weapons of the TRC's elite assassins (4,000,000 nuyen; 100,000 per 10 Mp; selling attracts assassins) | Red-7, Black 5, Barrier 7, Scramble 7, Killer 7 |
| DS-23 | Personal information on TRC operatives | Red-4, Access 5, Scramble 5, Trace and Burn 5 |
| SPU-13 | Terminals to CPU-3 | Orange-4, Barrier 4, Trace and Report 4 |
| I/OP-1 | Terminals in TRC centers | Orange-3, Access 4, Trace and Report 4 |

Anything stolen from here is deleted from the deck under O'Neill's deal.

**3. Shannon Bridge Hotel System** (p.47) -- simple, minimal security; the helicopter clue.

| Node | Function | Rating / IC |
|---|---|---|
| SAN-1 | Hotel Matrix access | Green-3, Access 3, Trace and Report 2 |
| CPU-1 | Power for the system | Green-4, Access 4, Trace and Dump 4 |
| SPU-1 | Data flow to the Matrix; reservation database | Green-3, Access 3, Trace and Report 2 |
| DS-1 | Current and six weeks of reservations; after 2:20 a.m. the MacNamara entourage in an executive suite for one night | (none listed) |
| SPU-2 | Guards DS-2 | Green-3, Access 3, Blaster 4 |
| DS-2 | Service contracts, local rivals, transport and special arrangements: Nathair MacSweeney booked Stallion YHB-156722 for 7 a.m. (text: 'Day 4'), civil aviation cleared a flight path to Boyle Abbey; treuntas shows the Stallion registered to Dominic O'Brien | (none listed) |
| SPU-3 | CPU to the SM/I/OP network | Green-2, Access 2, Trace and Report 2 |
| I/OP-1 | Climate sensors | -- |
| SM-1 | Central heating, alarms | -- |

**4. Boyle Abbey System** (pp.55-56) -- Sculpted Environmental Systems; crack it and the abbey's
sensors, alarms and weapons go down. Security Post A's terminal is a physical way in.

| Node | Function | Rating / IC |
|---|---|---|
| SAN-1 | Abbey Matrix access | Red-3, Access 5, Barrier 5, Trace and Report 5 |
| SAN-2 | Access to the rest of the SES system (nothing relevant; improvise) | Red-3, Access 5, Barrier 5, Trace and Report 5 |
| CPU-1 | Power for the whole system | Red-4, Access 6, Trace and Burn 6 |
| SPU-1 | Guards CPU-1 | Red-3, Access 5, Trace and Burn 5 |
| SPU-2 | Guards the sensitive datafiles | Red-4, Barrier 5, Tar Pit 5 |
| DS-1 | Archive of international journal abstracts on parabotany and parazoology | Green-4, Access 5, Trace and Report 4 |
| DS-2 | Dominic O'Brien's personal research notes -- a gigantic clipboard, too haphazard to be valuable | Red-3, Access 6, Trace and Report 5 |
| DS-3 | Condensed abstracts of research reports from other SES operatives (15 Mp, 5,000 nuyen) | Red-3, Access 4, Barrier 3, Tar Baby 4 |
| SPU-3 | Security systems around the abbey | Red-3, Barrier 4, Blaster 4, Trace and Burn 4 |
| I/OP-1 | Motion detectors | Red-2, Barrier 4, Blaster 4 |
| I/OP-2 | Gas-emission devices on the motion detectors | Red-2, Barrier 4, Blaster 4 |
| I/OP-3 | Window sensors and break-in alarms | Red-2, Barrier 4, Blaster 4 |
| I/OP-4 | Security cameras | Red-2, Barrier 4, Blaster 4 |
| SPU-4 | Terminals around the abbey | Orange-4, Access 5, Tar Pit 4 |
| I/OP-5 | Security desk inside the abbey | Orange-4, Access 4, Trace and Report 4 |
| I/OP-6 | Perimeter security posts | Orange-4, Access 4, Trace and Report 4 |

**5. Unmapped.** Prince Aithne Oakforest's personal system in Tir Tairngire (TRC-level security;
contents on his row); a Boston police database for the Rosenberg check (three days' questioning,
nothing conclusive); any police database confirming Rory MacNamara's Humanis membership; hotel
reservation lists near Shannon; foreign systems as Quick Matrix systems (SRII p.192).

## Flavor / not built

- **Mealla Oakforest** (Aithne's wife, MacSweeney's distant cousin); **Rory / 'Rony' MacNamara** (the
  candidate's Humanis-member brother); **Billy Fitzwalter** and **Robert Stein** (New Jersey planning
  officials bribed in 2039); **Andrew T. Small** (Democratic incumbent, 'a ditbrain') and **Norbert
  Quayle** (fundamentalist Republican) -- names on the MacNamara rows and handouts.
- **James Mairtin MacSweeney**, the Derry elf abroad who owns Altan Lodge and is no relation (a red
  herring if wanted); **Niall MacGuinness**, the Curtis Street flat's absent owner; **Doncha O'Brien**,
  author of 'The Destiny of Ages'; **the Cooper-Klein clinic** (Lewis's BTL therapy; city not given);
  **the New York Sentinel** (the kickback story); **'the Consortium'** that 'took over the show' after
  2039 and the corporate consortium MacNamara will kiss up to; **'the European Party'** (Wassall's
  name for the Mob's Irish branch).
- **Wassall's two troll samurai**, **MacNamara's six bodyguards**, the **Mob trolls** and **the dead
  Gambaccini capo**, the **INLA cells**, the **fomorians**, **Boyle Abbey's guards, mages and
  wolfhounds**, the **water elementals** -- stat summaries on the org and location rows.
- Downtime walk-ons: the **RTET reporter**, the **Inflame reporter**, the **Seattle tourist** who
  cannot find a Nuke-It burger, the **Celtic Purists**, **Metahuman Rights Activists**,
  **anti-American demonstrators**, the **Ork Resistance Movement** pub, the **whiskey-sodden local
  doctor**, the **Dublin cabbie**, the **McDonnell farmhand**.
- Tir sourcebook places name-checked: **University College Dublin**, **Zoological Gardens**,
  **Plunkett's Toy Shop**, **Sharkey's Fine Books**, **Griswold's Bar**, the DART rail system,
  **Wexford Airport**, the villages **Creeslough, Dunfanaghy, Gort an Choircre, Meenacung** and the
  towns **Letterkenny, Ballyshannon, Strabane**; **Belfast**, **Derry**, **Armagh**; the **Danaan
  Council of Stewards**, **Leinster Assembly**, **Dublin City Corporation** and the **Order of Sun,
  Moon, and Stars** (on the Tir na nOg row); **Renraku Eireann-Tir** (on the Renraku update and the
  Dun Laoghaire location); **Eireann-Tir Tours** as a company (location only); **Aer Lingus**.

## GM play notes

- Brains over brawn: pistols, light armor, basic decks and defensive talismans only; the TRC squash
  street samurai like bugs. Warn players out of character that assensing a TRC squad tells a mage to
  run, and that surrender is a real, survivable option. Human and elf runners have it easier; each
  ork, troll, dwarf or non-white face is +1 on the tally before anything happens.
- Run the **visible action tally** (p.19) from customs onward and be consistent: prior record,
  Aztech, Brits, metatype; brawls +4, arrests +6, four-plus foreign calls a day, a hijacked car, a
  bought car after the alert, dating Bridgit more than twice. A potential visible action is noticed on
  2D6 6+, or bought off with a permanently lost Karma point. From 4 a.m. Day 5 roll 4D6 per hour and
  per action against it: Garda first, then O'Neill.
- Keep a clock. The book's behind-the-scenes itinerary (Days 4-5) drives what Petra hears, what the
  hotel and police hosts contain, and when calls out of Connaught (3 a.m.) and the Tir (6 a.m.) are
  traced; overseas contacts answer in 2D6+1 hours at Etiquette TN 6-12 and hot information costs
  favors, 5D6 x 1,000 nuyen or a Karma point per item.
- The two Dublin days are the investment: Petra (companionship, confidence, one excursion) and
  Bridgit (flowers, wit, danger, Brendan's champagne) are the only contacts in the Tir and every later
  target number bends to how well they were courted. Nobody else in the retinue will talk. Notice
  the Rosslare papers changing hands at lunch.
- Altan Lodge must force a retreat -- add a cell if needed -- and MacSweeney must get away clean
  (fudge his resistance tests). Give them the west wing: the ring, the cash, the plans.
- The clean chain of deduction: 'go to the boil' -> the only Boyle on the map -> Boyle Abbey = SES ->
  Dominic O'Brien (hotel DS-2, treuntas registration, TRC DS-14/DS-17/DS-21, or Bridgit's father).
- Three exits, mutually exclusive except the O'Neill-plus-MacNamara combination: MacNamara
  (Negotiation 8 or Bridgit's call; he double-crosses on a failure or if police died), O'Neill
  (surrender, prove the forged file, raid the abbey wired for sound), O'Brien (talk, Charisma 6,
  Bargain 4 for 18,000 each). Team Karma p.60: legwork 1, romance 1, Petra 1, retinue dirt 1-2, the
  forged TRC file 1, and an unreadable award per deal (assume 2-3). Failure is a secret trial: 2D6
  years, or execution for cop-killers.
- Loose ends: MacSweeney's 'accident' if MacNamara wins; O'Brien's commissions or a lease to Tir
  Tairngire; the O'Brien family's face-saving revenge; O'Neill's cortex-bombed agents in New York; the
  future mayor (and maybe president) who owes the runners or wants them dead; an O'Toole who might be
  bored enough to call.

