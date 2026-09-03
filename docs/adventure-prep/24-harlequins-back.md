# Harlequin's Back -- Adventure Prep: NPCs, Locations, Organizations, Matrix Systems

Source: Shadowrun 2e - Adventure - Harlequin's Back {FASA7320}.pdf, pp. 3-152. Campaign order #24, in-game 2055.

Everything below is loaded into the campaign DB flagged `is_active: false` and `source_adventure: "Harlequin's Back"` by `python scripts/adventure_ingest/run.py harlequins_back`; flip entries active as the party meets them. Use the **Adventure** filter on the manage pages to see just this set.

## Plot synopsis

Drunk and purposeless a few years after settling his ancient score with **Ehran the Scribe**,
**Harlequin** is visited by a black-robed spectral figure -- Deceit itself, "Master of the Twisted
Path" -- who warns him that **the Enemy**, world-devouring creatures from deep in the metaplanes,
will breach the Sixth World some 2,500 years early. The Great Ghost Dance that broke the old United
States spiked the world's magic to lethal levels at its ritual site in the Southwest desert, and
that spike has become a bridgehead. Fate herself chooses a team of shadowrunners for Harlequin's
astral quest to stop it. Ferried past the **Dweller on the Threshold** and briefed by Harlequin and
his apprentice (and secretly Ehran's own daughter) **Jane "Frosty" Foster**, the runners reach the
**Chasm and the Bridge**, where the Enemy is building a physical span across the gulf between worlds.
Harlequin's plan: bring back **Thayla's Voice** -- the singing voice of an ancient queen who once
held the Enemy's army at bay, now held inside an enchanted Songbird -- and use it to seal the
bridgehead. The runners must gather a hood, a perch, and a cage for the bird, one item per
metaplanar "Place," each ruled in some twisted form by **Darke**, the Enemy's human ally, and each
haunted by echoes of Harlequin and Thayla themselves.

In **Aftermath**, a post-cataclysmic future Seattle, the runners aid **Leroy** (Harlequin's avatar)
and his dying walled Enclave against **Oscuro** (Darke) and his authoritarian Collective, and win
the hood only after Leroy's wife **Talia** (Thayla) sacrifices herself. In **A Fistful of Karma**, a
cowpunk Old West valley, they back reluctant Sheriff **Bergamot** (Harlequin) and mute saloon singer
**Celia** (Thayla) against sadistic rancher **Sy Vants**, gunslinger **Dred Francis**, and the
shapeshifting **Mr. Trey** (Darke), winning a bone perch from Trey's corpse. In **By the Sword**, a
pagan pre-Grail Arthurian England frozen by **Gawaine**'s death at **Lancelot**'s hand (Harlequin's
avatar here), the runners free the amnesiac **Guinglainn**, pass the Priestess **Viviane**'s trials
and Sir **Bercilak**'s Beheading Game at **Castle Maydenlande**, and witness Lancelot's atonement
and Guinglainn's ascension as the new Spring Champion, mending Excalibur's twin, the sword that will
become the cage's metal. In **The Impossible Dream**, a mythic Chicago-flavored realm, the runners
climb an endless Tower built on the **Foreman**'s (Darke) false promise of heaven, free the
**Architect** (Harlequin) and the imprisoned **Maiden** (Thayla), and topple the Tower, earning the
finished cage. **The Songbird** itself waits in Thayla's own corpse-strewn, Enemy-corrupted kingdom,
guarded by the deaf, pleading **Warden** (Darke); the runners steal it back to the Bridge -- only to
learn its song alone cannot stop the Enemy. Following the freed bird, they reach **The Masquerade**:
a neo-Victorian manor where **Lord Umberley** (Darke, fully realized and Initiate Grade 8) hosts a
ball attended by ambiguous Great Powers in costume while his hidden, hunchbacked brother **Nacht**
-- the original dark warrior of Thayla's own legend, and genuinely in love with her -- keeps the
real, still-mute Thayla prisoner behind a butler's and a colonel's murders. Nacht dies shielding
Thayla from Umberley's own killing spell, and she agrees to return. At **the Bridge**, Darke -- out
of avatars now, and human -- is caught mid-sacrifice, torturing a beaten Harlequin on a bone lattice.
Runners who defeat him free Harlequin; then Thayla asks the question no one has answered: what stops
the Enemy from simply killing her once the runners go home? Those who volunteer to stay behind
forever, guarding her as she sings, end the threat for good and wake in their own beds in Seattle,
remembering everything, with no proof any of it happened.

## Timeline

- **Voices from the Past** -- alone and drinking, Harlequin is confronted by a spectral embodiment
  of Deceit ("Master of the Twisted Path") who warns him the Enemy is coming early and tells him to
  "destroy the bridge" with Thayla's Voice. Jane Foster interrupts, chrome pistol in hand: "Harlequin's back."
- **Foreshadows** -- weeks of subtle omens (animal deference, uncanny luck, portentous dreams, an
  uncatchable laughing clown, a "20 Questions" personality survey) build toward the quest in the
  runners' ordinary Seattle lives; a record thunderstorm puts them all to sleep the same night.
- **Into the Desert / The Bridge, Part One** -- the Dweller on the Threshold tests and passes the
  runners regardless (the Great Powers decreed it); Harlequin's minivan carries them to the site of
  the Great Ghost Dance in the Southwest desert, then to the Chasm and the Bridge, where the Enemy
  is already spanning the gap. Harlequin tells them Thayla's legend and sends them after her Voice,
  fighting off a first wave of Enemy creatures and marking them with his own blood (a personal Karma
  Pool) plus a Team Karma Pool of 50 that never refreshes.
- **Aftermath** -- the Enclave vs. the Collective; Talia's self-sacrifice heals the wasteland and
  wins the Songbird's hood from the fallen Oscuro.
- **A Fistful of Karma** -- three days in Valley Hope; Bergamot and Celia face down Vants and Dred
  Francis at high noon; Mr. Trey's true form dies to Celia's restored song, dropping the perch-bone.
- **By the Sword** -- the runners free Guinglainn, win Lancelot's broken sword from him, pass the
  trials of Avalon and Castle Maydenlande, and watch Lancelot's atonement-death and Guinglainn's
  rebirth as the Spring Champion, who mends the sword -- the cage's future metal.
- **The Impossible Dream** -- the ruined Village and its impossible Tower; the runners free the
  Architect's imprisoned Maiden from the Foreman's Labyrinth, topple the Tower, and receive the
  finished birdcage, forged from Lancelot's sword and Trey's bone.
- **The Songbird** -- Thayla's own kingdom, dead and corrupted since she left it; the runners steal
  the Songbird from the deaf Warden's tower.
- **The Bridge, Part Two** -- the Songbird's song alone fails to stop the Enemy; Harlequin binds the
  runners to the bird with silver cords to follow it to Thayla herself.
- **The Masquerade** -- Umberley Manor; two murders (Stokes, Colonel Quinn), a seance, house arrest,
  and a final confrontation in "the Engine" beneath the manor, where Nacht dies protecting Thayla
  from his own brother and she agrees to return with the runners.
- **The Bridge, Part Three** -- Darke, unmasked and human, is caught sacrificing children to pollute
  the outcropping while Harlequin hangs tortured on a bone lattice; the runners defeat him, free
  Harlequin, and must choose whether to stay with Thayla forever while she sings the Enemy back for
  good. Survivors wake in Seattle at the same dawn with no physical evidence the quest ever happened.

## NPCs (Persons of Interest)

| Name | Role | Org |
|---|---|---|
| Thayla | The ancient exiled queen whose singing Voice alone can hold the Enemy back; the quest's true object, found only in the book's final chapters | independent |
| Darke | The Enemy's sole human ally and the astral quest's recurring antagonist, appearing as a different local villain in almost every metaplanar Place | independent |
| Leroy (Aftermath) | Leader of the Enclave in the Aftermath Place; Harlequin's local avatar, a reluctant philosopher-king forced into command | The Enclave |
| Talia | Leroy's wife in the Aftermath Place; Thayla's local avatar, whose self-sacrifice alongside Leroy's blood heals the dying wasteland | The Enclave |
| Gareth | Leroy's security chief and first lieutenant in the Aftermath Place; loyal to the death, deeply distrustful of the runners | The Enclave |
| Maranda | Enclave scout leader who rescues the runners from an alacorn and first brings them into the settlement | The Enclave |
| Tela and Brannen | Sister physical-adept scouts of the Enclave who first fight beside the runners, then defect to the Collective -- Tela is later murdered as a blood sacrifice | The Enclave |
| Oscuro | Leader of the rival Collective in the Aftermath Place; Darke's avatar here, a shapeshifter between a cruel human form and an amorphous horror | The Collective |
| Enganar | Oscuro's toxic-shaman lieutenant who delivers the Collective's brutal ultimatum for Talia, killing Tela as a blood sacrifice | The Collective |
| Bellaco | Sadistic elf hermetic mage who leads the escort taking the surrendered Talia toward Oscuro, until the runners intercept them | The Collective |
| Arlen Bergamot | Reluctant sheriff of Valley Hope in the A Fistful of Karma Place; Harlequin's local avatar, broken down by Mr. Trey's manipulation and rebuilt by the runners' support | independent |
| Celia | Mute barmaid and former singer at the Songbird Saloon; Thayla's local avatar, brutalized into silence by Sy Vants years before the runners arrive | independent |
| Sy Vants | Wealthy, physically enhanced rancher terrorizing Valley Hope; the dark warrior's avatar in the A Fistful of Karma Place, sadistically fixated on Celia | Blood Eagle Gang |
| Dred Francis | Sy Vants' cybered gunslinger, released from territorial prison to finish breaking Valley Hope; the town's most feared enforcer | Blood Eagle Gang |
| Mr. Trey | Courteous, unnervingly persuasive Flattop Mining Company representative; Darke's avatar in the A Fistful of Karma Place, feeding on the town's engineered despair | Flattop Mining Company |
| Jed Porkins | Ork owner of the Songbird Saloon in Valley Hope; welcomes hero runners with free rooms and a round on the house | independent |
| Kendall Silver | Elf editor of the Valley Hope Clarion; a source of the town's history and one of the citizens who backed Bergamot's Vigilance Committee | independent |
| Doc Wunderlich | Valley Hope's town physician; another source of the valley's history and a former ally of Bergamot's Vigilance Committee | independent |
| Simon Renfrew | Valley Hope's attorney; a source of local business and legal history, and another Vigilance Committee veteran | independent |
| Winch Wardell | Proprietor of Wardell's Emporium, Valley Hope's general store | independent |
| Mrs. Venturi | Apothecary in Valley Hope, selling first-aid supplies to the runners | independent |
| Max Hammel | Blacksmith and liveryman of Valley Hope, boarding the town's horses and thunderfeet | independent |
| Parson and Mrs. Emmerick | Ork couple running Valley Hope's church, parsonage, and schoolhouse; the parson doubles as the town's exorcist | independent |
| Lancelot | Aged, guilt-broken traitor knight of the By the Sword Place; Harlequin's local avatar, who killed the true finest knight of the Round Table out of jealous rage | independent |
| Gawaine | The true finest knight of the Round Table in the By the Sword Place, murdered by Lancelot; his spirit and legacy resemble Ehran the Scribe | independent |
| Guinglainn | Gawaine's amnesiac, magically imprisoned son; freed by the runners, he becomes the new Champion of Spring and mends the broken sword | independent |
| Viviane | Powerful Priestess of Avalon who guides the runners through By the Sword's trials; speaks only to female runners and coincidentally resembles Jane Foster | Priestesses of Avalon |
| Nimue | The Lady of the Lake in the By the Sword Place; rises from the water bearing Excalibur for the story's climax | Priestesses of Avalon |
| Bercilak | Powerful knight guarding Castle Maydenlande's gate with a ritual Beheading Game; represents the barren, infertile Winter Champion, not an avatar of the Enemy | independent |
| Ragnall | Bercilak's wife at Castle Maydenlande's mansion; sets a temptation trial (the 'Test of Virtue') for the runner she selects | independent |
| Winlogee | Bercilak's daughter, cursed by an enchantment to be beautiful by day or by night but never both; her Riddle Game tests a chosen runner's understanding | independent |
| The Crone | A destructive aspect of the Goddess who guards the entrance to Gawaine's Great Hall at Castle Maydenlande | independent |
| The Architect | Elf tinkerer haunting the ruined Village in the Impossible Dream Place; Harlequin's local avatar, tormented by having designed the Tower that doomed his people | independent |
| The Maiden | A nameless, painfully shy prisoner held by the Foreman deep in the Impossible Dream's Tower Labyrinth; Thayla's local avatar | independent |
| The Foreman | The white-suited tempter who lured the Village into building the impossible Tower; Darke's avatar in the Impossible Dream Place | independent |
| Eve | The Foreman's cybered samurai enforcer in the Limbo Room, targeting male characters with high Charisma | independent |
| Blazer | The Foreman's hitman in the Limbo Room, holding fire until a runner starts casting spells | independent |
| Toady | A babbling, cowardly little frog-man who pesters climbing runners with endless nosy questions in the Impossible Dream's Tower | independent |
| Morris | A shy gnomelike spirit who offers climbing runners a mysterious black box he cannot explain | independent |
| Mister Mystery | A self-styled 'living enigma' spirit conjured by a rune-marked talisman on the Impossible Dream's Tower | independent |
| Stokes | Lord Umberley's butler at Umberley Manor; the first of Nacht's two murder victims | independent |
| Colonel Quinn | Guest of Lord Umberley at the masquerade, dressed as a harlequin; publicly identified as Thayla's grieving 'uncle' and Nacht's second murder victim | independent |
| Lady Raven | Masquerade guest who leads a seance to contact Thayla, interrupted by Colonel Quinn's murder; her impressions point the runners toward the truth | independent |
| Auric | Golden, charismatic masquerade guest at Umberley Manor -- likely a Great Power in disguise, generous and trusting toward everyone including his host | independent |
| Jack-in-the-Green | Wild, carousing masquerade guest at Umberley Manor -- likely a nature spirit or totem in disguise, contemptuous of his host beneath the revelry | independent |
| Lady Rose | Beautiful, pained masquerade guest at Umberley Manor -- likely a Great Power in disguise, weeping blood behind an otherwise perfect facade | independent |
| Luna | Haughty, moon-themed masquerade guest at Umberley Manor -- likely a Great Power in disguise, reserved and knowledgeable about magic | independent |
| Madame Rouge | Sultry, all-knowing masquerade guest at Umberley Manor -- likely a Great Power in disguise, embodying beauty and desire | independent |
| Mother Mondas | Warm, motherly masquerade guest at Umberley Manor -- likely a Great Power in disguise, urging forgiveness above all else | independent |
| Old Man Coyote | Trickster masquerade guest at Umberley Manor -- likely a totem or Great Power in disguise, answering every question with another | independent |
| Ronin | Proud, dangerous swordsman among the masquerade's guests at Umberley Manor -- likely a Great Power in disguise, contemptuous of Lord Umberley | independent |
| Smith | Shy, craft-obsessed dwarf among the masquerade's guests at Umberley Manor -- likely a Great Power in disguise, fascinated by the mansion's construction | independent |
| The Warden | Deaf, illiterate guardian of Thayla's own Songbird in her corrupted kingdom; Darke's avatar here, who cannot bear to touch or even look at the bird | independent |
| Lord Umberley | Suave, cultured host of Umberley Manor's masquerade ball; Darke's most fully realized and named avatar, an Initiate of grade 8 hiding his monstrous brother's secret | independent |
| Nacht | Lord Umberley's hidden, hunchbacked brother, kept from the world in shame; the original dark warrior of Thayla's own legend, genuinely in love with her | independent |

## Locations

| Name | Type | District | Notes |
|---|---|---|---|
| Site of the Great Ghost Dance | place of power | A remote desert in the Southwestern United States (real-world site of the Great Ghost Dance ritual) | Flat, barren 20-meter circle where the Great Ghost Dance spiked the world's background magic to lethal levels, opening a metaplanar bridgehead for the Enemy |
| The Chasm and the Bridge | place of power | The astral quest's recurring hub, visited three times as 'The Bridge, Parts One through Three' | Bottomless metaplanar gulf between the Sixth World and the Enemy's realm, spanned by a growing bone-and-spirit bridge the runners must stop before it completes |
| The Enclave (Aftermath) | walled settlement | The Aftermath Place -- ruins of a far-future Auburn, Washington | Stone-walled mesa compound of piled-rock huts around the wasteland's last pure well; Leroy's Long House, an armory, and a smithy |
| Valley Hope | town | The A Fistful of Karma Place -- a cowpunk Old West valley | 180-person frontier town threatened by Sy Vants' Blood Eagle gang and Mr. Trey's mine; Main Street and Train Street, church, jail, bank, and the Songbird Saloon |
| Blood Eagle Ranch | ranch | The Valley Hope valley (the A Fistful of Karma Place) | Sy Vants' comfortable two-storey ranch house and bunkhouse, guarded by two cowpokes per shadowrunner plus two cowpunks |
| Flattop Phlogiston Mine | mine | Outside Valley Hope (the A Fistful of Karma Place) | Abandoned phlogiston mine Mr. Trey claims as his home; in truth only ruined barracks and empty shafts, no sign anyone lives there |
| Songbird Saloon | bar | Train Street, Valley Hope (the A Fistful of Karma Place) | Only saloon with rooms to rent in Valley Hope; ork owner Jed Porkins, flaming Dragon's Breath cordial, and mute barmaid Celia -- Harlequin's Back's echo of Thayla |
| The Pagan Woodland | enchanted forest | The By the Sword Place -- a pre-Grail pagan Arthurian England locked in eternal winter | Frost-bound forest of eight paths converging on the Priestesses' fountain, Lancelot's hermit hut, and a thorn-walled clearing holding the imprisoned Guinglainn |
| Isle of Apples | sacred island | Avalon, the By the Sword Place | Avalon itself: burial place of Arthur, realm of the Goddess, reachable only by a Priestess-poled barge, and lethal to any man who sets foot on it |
| Castle Maydenlande | castle | The By the Sword Place | Ruined island castle behind Sir Bercilak's Beheading Game and mansion hospitality trials; guarded moat, animate stone knights, and a Crone barring Gawaine's Great Hall |
| The Village | ruined village | The Impossible Dream Place -- a mythic, archetypal realm laced with anachronistic Chicago debris | Abandoned village dwarfed by the impossible Tower its people built chasing a false promise of heaven; home to the Architect and the ruined Cathedral |
| The Cathedral | ruined cathedral | The Village, the Impossible Dream Place | Once dedicated to a nameless spirit called Mother, now displaying the Foreman's gifted 'treasures' -- mints, a porn magazine, gold coins, and a loaded pistol -- on its desecrated altar |
| The Tower | impossible tower | Rising from the Village, the Impossible Dream Place | Kilometers-tall structure the Village's people abandoned their lives to build chasing a false promise of treasure from the sky; guarded by three escalating Guardians and the Foreman's bunker at its summit |
| The Limbo Room | roadhouse | A pocket dimension reached only through Guardian 1's Engulf attack (the Impossible Dream Place) | A too-real Seattle roadhouse where runners get their own gear back just long enough for 'Bill Foreman' to try to bribe them off the quest before his goons open fire |
| Thayla's Palace | ruined palace | The Songbird Place -- Thayla's own kingdom, corrupted after she left it | The corpse-strewn ruin of Thayla's fairy-tale city and palace; the Songbird waits in its one surviving copper-and-gold tower, guarded by the deaf, pleading Warden |
| Umberley Manor | manor house | The Masquerade Place -- a neo-Victorian realm of landed aristocracy and techno-magical machinery | Lord Umberley's gothic-Victorian mansion: a masquerade ball, a secret passage maze, and the buried techno-magical 'Engine' where his brother Nacht keeps the real Thayla prisoner |

## Organizations (new)

| Name | Type | Tier | Notes |
|---|---|---|---|
| The Enclave | survivor settlement | 1 | Dying walled settlement of anti-magic, anti-cyber survivors in a metaplanar post-cataclysm future Seattle; led by Harlequin's avatar Leroy |
| The Collective | authoritarian settlement | 2 | Megacorp-modeled rival settlement in the Aftermath Place; physically prosperous, spiritually crushed, ruled by Darke's avatar Oscuro |
| Blood Eagle Gang | gang | 1 | Sy Vants' cowpunk gunslinger outfit terrorizing Valley Hope; broken once by Sheriff Bergamot, rebuilding to finish the job |
| Flattop Mining Company | corporation | 1 | Mining outfit fronting for the shapeshifting Mr. Trey, who wants Valley Hope's ecology broken to feed on its people's despair |
| Priestesses of Avalon | mystical fellowship | 2 | Goddess-serving priestesshood of a pagan pre-Grail Arthurian England, keepers of Avalon and Excalibur, no male ever allowed to set foot on their island alive |

## Existing locations / NPCs updated

- NPC: **Harlequin**
- NPC: **Jane Foster**

## Matrix systems -- to build in the Matrix designer (NOT built yet)

The only "Matrix"-equivalent system in Harlequin's Back is the Engine, the buried techno-magical
mechanical computer beneath Umberley Manor in The Masquerade Place -- documented here for flavor
only, never built as a real host.

| Node | Function | Color/Rating | IC |
|---|---|---|---|
| Terminal access points | Room terminals scattered through the manor; a "magic lantern" VR rig (diving-bell helmet + control glove) substitutes for a cyberdeck | Standard computer access, per Computer Theory (6) | none |
| The Engine (system core) | A cathedral-sized clockwork machine; querying it is run as a mini-astral-quest (Grimoire II, p.95) | Reaching the Citadel yields exactly one fact about the Place's cover story per successful run (never the true events of Darke's plan) | Mechanical blade/saw appendages, 5L damage, Barrier Rating 5 per limb, avoided with an opposed Reaction (4) vs. Rating 6 |
| Nacht's inner chamber | The room at the Engine's heart where Thayla is held; catwalks here are rigged to collapse into the grinding gears (8D damage) | Not a decking target -- a physical trap | Nacht himself, moving through the shadows |

## Flavor / not built

- Enemy Crawlers, Enemy Toads, alacorns, fomorians, each-uisges, animate Stone Knight statues,
  spirit hounds, the reanimated "mine monster," generic earth/fire elementals, cowpokes, cowpunks,
  and unnamed "extras" -- all generic Threat Rating opposition with no individual identity.
- Guardians 1-3 of the Impossible Dream's Tower (the land-kraken, the armored Henchman, and the
  card-playing "Cerberus Bug" cockroach) and the roach-man "Beetlebugs" -- one-scene monster set
  pieces, not persistent characters.
- The Bouncer (a spirit guardian barring the Village's "Exit Door") and the Dweller on the
  Threshold (the robed ferryman who tests the runners at the astral quest's outset) -- unnamed,
  function-only gatekeeper spirits.
- "Fate" -- the unspeaking, sparkle-robed woman glimpsed on the dock at the quest's start; never
  interacted with.
- The unnamed "blue-skinned man in a trench coat" and the unnamed bat-winged sprite from the
  Impossible Dream's random "Playful Spirits" table, plus its lying "false Guardian" con-man --
  the table's three named entries (Toady, Morris, Mister Mystery) are recorded above.
- The "Lord Constable" (a masquerade guest who strongly resembles Ehran the Scribe) and "Lady
  Nasir" (explicitly identified as Ariel Nasir, the free air elemental from the original Harlequin
  adventure) -- cameo name-drops of characters from specs/harlequin.py, which has not yet been
  built out; do not create stray rows for them here.
- The unnamed sacrificed children at the Bridge, Part Three, who speak a 2055 Mexican/Aztlan
  dialect of Spanish -- a deliberately unexplained detail, not a resolvable character.
- The unnamed, faceless barge-ferrymen of the Isle of Apples and Castle Maydenlande -- silent,
  function-only guides.
- The "20 Questions" player-handout survey and the general Foreshadows-chapter omens (barking
  animals, portentous dreams, an uncatchable laughing clown) -- pre-adventure GM techniques, not
  in-fiction rows.

## GM play notes

- This is a single continuous framing adventure, not eight independent ones: run The Bridge, Parts
  One through Three, as the connective tissue between Aftermath, A Fistful of Karma, By the Sword,
  The Impossible Dream, The Songbird, and The Masquerade, in that order.
- Hard rule carried over from the source text: no astral projection is permitted anywhere in this
  adventure -- it breaks the story by revealing too much too soon.
- Each metaplanar Place transforms gear, cyberware, and magic differently (see each location's
  notes); brief players on the relevant Place's rules before they arrive rather than all at once.
- Player-character death mid-quest has three GM-chosen resolutions in the source text (temporary
  "death" with no Karma for that leg; permanent memory-wipe departure; or true death) -- pick one
  approach before play and apply it consistently, per the book's own Introduction section (not
  reproduced here as a row).
- The climactic choice at The Bridge, Part Three -- volunteering to remain with Thayla forever, or
  leaving her undefended -- is the adventure's real ending and should not be rushed; the book treats
  it as a roleplaying decision, not a dice roll.
- Both the Songbird's survival after restoring Thayla's voice, and the true nature of the
  masquerade's Great Powers guests, are left ambiguous by design; do not resolve them without a
  reason arising from your own table's play.

