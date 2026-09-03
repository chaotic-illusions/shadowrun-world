# First Run -- Adventure Prep: NPCs, Locations, Organizations, Matrix Systems

Source: SR1-first-run.pdf, pp. 3-64. Campaign order #33, in-game 2061.

Everything below is loaded into the campaign DB flagged `is_active: false` and `source_adventure: "First Run"` by `python scripts/adventure_ingest/run.py first_run`; flip entries active as the party meets them. Use the **Adventure** filter on the manage pages to see just this set.

## Plot synopsis

First Run collects three stand-alone scenarios meant to teach new players and gamemasters the game,
each with its own cast and none dependent on the others.

**Food Fight** is a shoot-out pure and simple: the team stops for munchies at a 24-hour **Stuffer
Shack** just as the thrill-gang **Chiller Thrillers** robs it, smashing the PANICBUTTON box and
terrorizing the clerk, the manager and a handful of ordinary shoppers before the gunfire starts. This
is an SR3-era reprint of the classic Shadowrun 1st Edition scenario of the same name (already covered
by this campaign's earlier Food Fight spec); the cast and location are the same store, the same gang,
mostly the same people under mostly the same names.

**Supernova** sends the team to **Club Penumbra** to meet **Nigel Terwilliger**, a panicky first-time
Mr. Johnson who is actually a Novatech cleanup specialist secretly also selling to **Renraku Computer
Systems**. Nigel hires the runners to break into **TekLon Electronics**, a small Auburn microtronics
firm both megacorps are fighting over in the wreckage of Fuchi's collapse, and lift an unfinished
cybernetic head prototype from its Alpha Wing lab -- timed, unknown to the runners, to land in the
middle of a Renraku raid on the same facility. The extraction is clean, but the payoff isn't: Nigel's
Novatech colleague **Elizabeth Chavez**, who caught him embezzling files for Renraku, has grabbed the
wrong case and dies in a Bellevue ambush by Renraku's elite **Red Samurai** and a fully armed
cyberzombie before the team can complete the swap. The runners recover both cases and Chavez's
datapad, which leads them to **Richard Villiers** and **Miles Lanier** at Novatech's Seattle
penthouse, where Nigel's double game gets him shot and the runners are asked to cover the corp's
escape from a Renraku ambush in the parking garage.

**Site of Desecration** takes the team out of the sprawl entirely. The talismonger **Daisy Quallon**
hires them to meet a smuggling crew, **the Pentagon**, in Cascade Ork territory and carry home a
shipment of magical telesma. The Pentagon has already been ambushed and robbed by the **Tooth
Warriors**, a new gang formed by the troll **Kaztok** around a crashed smuggler rotorcraft -- and
around **the Old One**, a free-willed man-of-the-woods spirit that Kaztok believes he controls. The
runners negotiate, fight and bluff their way through Kaztok's camp, the **Site of Desecration** itself,
only to discover in the end that the Old One was using Kaztok the whole time, and that the real test
was always aimed at them.

## Timeline

**Food Fight** -- a single rainy night; no date given (see food_fight.py for the established date of
2050).

**Supernova**, 2061, one evening into the small hours:
- Evening -- the meet with Nigel Terwilliger at Club Penumbra; the runners take the job.
- Same night -- the Auburn access tunnel and the (unopposed) extraction from TekLon's Alpha Wing,
  overlapping Renraku's raid on the rest of the facility.
- Just after midnight -- downtime at a safehouse or on the road while Nigel arranges the exchange.
- 2 a.m. -- the ambush at 100th and Main, Bellevue: Elizabeth Chavez dies, Red Samurai and the
  cyberzombie attack.
- Shortly after -- 3844 Belmont Avenue: Richard Villiers and Miles Lanier reveal Nigel's double game;
  Lanier kills him.
- Minutes later -- the garage escape as Renraku's remaining forces close in.

**Site of Desecration**, roughly one month after the Tooth Warriors' first ambush of Denver Bob's
Black Dog smuggling team:
- Day 0 -- Daisy Quallon hires the runners at The Magic Touch; the exchange with the Pentagon is set
  for noon the next day at Hemlock Pass.
- Day 1, morning -- the border crossing and the drive/flight up Denny Creek to Hemlock Pass.
- Day 1, midday -- the wrecked Pentagon rotorcraft and the meet with Pounder's crew.
- Day 1, night -- the confrontation with Kaztok and the Old One at Crescent Eye's farm, then the
  march to the Site of Desecration; Kaztok's "trial," the Old One's tests, and Kaztok's death.
- Day 2 -- the runners return to Seattle; Daisy is still away.
- Day 3 -- the runners deliver Daisy's telesma; the Old One reveals himself to her and departs.

## NPCs (Persons of Interest)

| Name | Role | Org |
|---|---|---|
| Nigel Terwilliger | First-time Mr. Johnson -- a Novatech cleanup specialist secretly double-dealing with Renraku, who hires the runners to rob TekLon and dies for the betrayal | Novatech, Inc. |
| Elizabeth Chavez | TekLon research scientist loyal to Novatech who exposes Nigel Terwilliger's double-dealing and dies for it in a Renraku ambush | TekLon Electronics |
| Daisy Quallon | Ms. Johnson -- an elf talismonger who hires the runners to handle a smuggling exchange she cannot make herself, and who is quietly an information source for the great dragon Hestaby | independent |
| Pounder | Black dwarf founder and leader of the Pentagon smuggling crew -- laid-back until crossed, and the crew's contact man | The Pentagon |
| Breetva | The Pentagon's negotiator -- a Russian ex-pat who kills double-crossing suppliers rather than get taken advantage of | The Pentagon |
| Heeley | The Pentagon's rigger -- looks about twelve, talks with a heavy Creole drawl, and just lost his beloved GMC Banshee to the Tooth Warriors' ambush | The Pentagon |
| Red-Scale-Snake | Ork Snake shaman of the Pentagon -- twin sister of Night-Strike-Woman, freed from slavers and grown into the crew's magical back-up | The Pentagon |
| Night-Strike-Woman | Ork physical adept of the Pentagon -- Red-Scale-Snake's bigger, quieter twin, still protective of her after the slavers | The Pentagon |
| Kaztok | Troll leader of the Tooth Warriors -- convinced he controls the Old One, when in fact the spirit has been using him the whole time | Tooth Warriors |
| The Old One | A free-willed man-of-the-woods nature spirit, not bound to any shaman or conjurer, who let Kaztok believe he was in control while pursuing an agenda entirely his own | independent |
| Crescent Eye | Cascade Ork farmer sheltering Denver Bob's captured smuggling crew, caught between Kaztok's threats and his own conscience | independent |
| Denver Bob | Leader of the Black Dog smuggling team; ambushed by the Tooth Warriors a month earlier and presumed dead, actually held and tortured at Crescent Eye's farm | Black Dog |

## Locations

| Name | Type | District | Notes |
|---|---|---|---|
| TekLon Electronics (Alpha Wing / the Pit) | research lab | Auburn | TekLon's Auburn microtronics campus; the Alpha Wing lab (nicknamed the Pit) holds the unfinished cybernetic head prototype the runners are hired to steal |
| Novatech Penthouse (3844 Belmont Avenue) | corporate headquarters | Downtown | Richard Villiers' Seattle meeting floor -- the entire fourteenth story of a brand-new downtown office tower, reached by a single unmarked elevator |
| 100th and Main (Bellevue) | warehouse district intersection | Warehouse District | Deserted four-corner warehouse intersection where Elizabeth Chavez dies and Renraku's Red Samurai ambush the runners for her case |
| The Magic Touch | talismonger shop | far eastern Renton, near the Salish-Shidhe border | Daisy Quallon's modest talismonger shop on the edge of the sprawl, where she hires the runners to handle a smuggling exchange she cannot make herself |
| Site of Desecration | gang territory | The Tooth, Cascade Mountains | The crash site of a smuggler's Ares Dragon rotorcraft, now the Tooth Warriors' camp and the Old One's haunt -- the adventure's title location and final confrontation |
| Denny Creek | mountain town | Cascade foothills, along Denny Creek | Small NAN tourist town at the edge of Cascade Ork territory, the last stop before the off-road push to Hemlock Pass and the Tooth |

## Organizations (new)

| Name | Type | Tier | Notes |
|---|---|---|---|
| TekLon Electronics | corporation (microtronics and cybertech components) | 2 | Small Auburn microtronics firm caught between Novatech and Renraku in the wreckage of Fuchi's collapse; developing an unfinished cybernetic head prototype |
| The Pentagon | smuggling crew | 1 | Five-member smuggling crew with an excellent reputation for delivering the goods with a minimum of heat; ambushed and robbed by the Tooth Warriors while dropping off telesma for Daisy Quallon |
| Tooth Warriors | gang (troll and ork thugs) | 1 | New gang formed by the troll Kaztok around a crashed smuggler rotorcraft and a captive man-of-the-woods spirit; robs smugglers passing through the Tooth |
| Black Dog | smuggling crew | 1 | Denver smuggling team led by Denver Bob; ambushed by the Tooth Warriors a month before Site of Desecration and presumed dead until the runners find survivors being tortured at Crescent Eye's farm |

## Existing organizations updated (sourced appends, nothing overwritten)

- **Novatech, Inc.** -- GM notes
- **Renraku Computer Systems** -- GM notes
- **Cascade Ork** -- GM notes
- **Chiller Thrillers** -- GM notes

## Existing locations / NPCs updated

- location: **Club Penumbra**
- location: **Stuffer Shack - Redmond Barrens**
- NPC: **Richard Villiers**
- NPC: **Miles Lanier**
- NPC: **Wendy**
- NPC: **Lucas Katcherman**
- NPC: **Frank Pilgrim**
- NPC: **Bill Pruitt**
- NPC: **Spike**
- NPC: **Willis Fabrizzi**
- NPC: **Wanda**
- NPC: **Mr. Nick**
- NPC: **Johnny**
- NPC: **Jacky Scatman**
- NPC: **Angie Scatman**

## Matrix systems -- to build in the Matrix designer (NOT built yet)

**TekLon Electronics -- Alpha Wing security slave (Supernova, before the Renraku raid)**
| Node | Function | Rating | IC |
|---|---|---|---|
| Access node (from the storage-room security box) | Log-on point; Access Rating 10 | Easy Orange (4/10/10/10/10/6) | None |
| Maglock Room (system sculpture: five power switches) | Controls doors A-E and the elevator (elevator itself off-line) | as above | None |
| Camera slave (system sculpture: a sofa, 22 monitors) | Controls all Alpha Wing cameras; Edit Slave sends a tape loop | as above | None |
| Host A | Public: company profile, catalog | Easy Orange | None |
| Host B | Company and personnel records | Easy Orange | None |
| Host C | Sales and financial records | Easy Orange | None |
| Host D | The security system itself (see above) | Easy Orange | None |
| Host E | Research, Alpha Wing and the Pit -- what the runners actually want | Easy Orange; files under Scramble 4 | None |

Security was deliberately taken off-line by Nigel Terwilliger ahead of Renraku's raid; there is no IC
anywhere on the system pre-raid. After the Renraku attack the entire system alerts to **Red Hard**
(8/16/14/18/18/18) and begins erasing files -- a decker returning to the access node afterward finds a
much harder, actively hostile system instead of the one the team already cracked.

## Flavor / not built

- **The cyberzombie** (Supernova) -- no name given ("the cyberzombie" throughout); a first-generation
  Renraku black-project asset, folded into Renraku Computer Systems' notes_append rather than built as
  an NPC row.
- **Red Samurai gun-troops and hermetic mages** (Supernova) -- generic squad stat blocks with no named
  individuals; folded into Renraku Computer Systems' notes_append.
- **Rank-and-file Tooth Warriors** (Site of Desecration) -- unnamed troll/ork thugs (generic stat
  blocks, six or more on-page); folded into the Tooth Warriors org row.
- **Hestaby** (Site of Desecration) -- the great dragon Daisy Quallon secretly informs for; never
  appears on-page, only sends an astral messenger. Already judged NOT_BUILT in blood_in_the_boardroom.py;
  this spec follows that precedent and keeps her as a name-drop on Daisy Quallon's row.
- **Abstract Media Services, Lakeview International Holding Company** (Supernova) -- defunct Fuchi-era
  shell/holding entities, name-dropped only in TekLon's background legwork; both are gone, nothing to
  build.
- **Morning Dawn** (Site of Desecration) -- Crescent Eye's sick daughter, name-dropped as the reason
  Denver Bob once helped his family; captured as color on Crescent Eye's row.
- **Mrs. Needles, Louis Needles, Timmy Thinners** (Food Fight) -- reprised bystander color, already
  judged NOT_BUILT (captured in the Stuffer Shack location notes) by food_fight.py; this spec follows
  that precedent rather than promoting them.
- **The Black Dog rotorcraft crew beyond Denver Bob** -- unnamed, unstatted; folded into the Black Dog
  org row.
- **Various generic critter suggestions** (Site of Desecration: devil rats, aardwolves, barghests,
  griffins, thunderbirds, etc.) -- explicitly left to gamemaster's choice in the text, nothing concrete
  to build.
- FASA sourcebook pointers only, no content extracted: Blood in the Boardroom (already its own spec),
  Renraku Arcology: Shutdown, New Seattle, Cyberpirates, Target: Smuggler Havens, Man and Machine, the
  Dragonheart Saga novels, Virtual Realities 2.0, Portfolio of a Dragon: Dunkelzahn's Secrets,
  Headhunters, Technobabel, Target: UCAS, Corporate Download, Magic in the Shadows, The Underworld
  Sourcebook, Predator and Prey (already its own spec).

## GM play notes

- Food Fight: this is a pure combat teaching scenario -- keep it fast and loud, and use the Food Fight
  property-damage table on every miss to keep the store chaotic. Do not let the runners get bogged down
  in roleplaying; the gang wants a fight and gets one within a page of the team walking in.
- Supernova: the TekLon extraction (Milk Run) is deliberately the easiest run the team will ever pull
  -- lean into the paranoia that easy jobs invite rather than adding real opposition. Save the actual
  danger for Four Corners, where the Red Samurai and the cyberzombie should feel like a serious step up
  in threat level.
- Supernova: Villiers and Lanier must not die, whatever the runners try at the penthouse -- escalate
  defenses (gas, wards, spirits) rather than ever letting a fight there go the runners' way.
- Site of Desecration: decide the Old One's true motive before the table sits down (curiosity about the
  wider world, as written, or something darker) -- his tests of the runners should telegraph that motive
  even while he plays naive in front of Kaztok.
- Site of Desecration: the Pentagon's priorities (reputation and a working trade deal) are not the same
  as the runners' -- use Breetva to keep pulling the group back toward a negotiated outcome if the table
  wants to shoot its way through Kaztok's camp.
- Karma awards are explicit in the book: Food Fight 2 (1 survive, 1 facing the Chiller Thrillers);
  Supernova 2 base plus up to 3 more (threat level, not harming Villiers/Lanier, killing the
  cyberzombie); Site of Desecration 2 base plus up to 6 more (threat level 1-3, surviving the Old One's
  tests 1-3).

