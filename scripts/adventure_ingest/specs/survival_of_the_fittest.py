# Survival of the Fittest (FanPro 10665, 2002, SR3; writing by Steve Kenson) -- campaign order #36.
# A seven-adventure globe-spanning campaign: Seattle (Everett, the Eye of the Needle) / the Shasta
# Enclave and Mount Shasta in the California Free State / the Denver Front Range Free Zone (CAS and
# UCAS sectors) / New Orleans and the Mississippi Delta / the Gulf and the Caribbean / Macapa and the
# Amazon interior / Hong Kong / Vladivostok and Popov Island / Caerleon and Llandovery in Wales / the
# ruins of Tehran / the metaplanes.
# Dating: the book deliberately leaves the dates of the Rite of Succession undefined so gamemasters
# can drop it into a campaign, but says plainly (p.14) that "the Rite would not begin until mid-2062,
# after Ghostwalker has consolidated his power base within Denver, and probably ends in early 2063."
# Ghostwalker emerged in the last days of 2061; Dunkelzahn died in 2057; Halley's Comet has already
# passed. YEAR follows the book's own general timeframe.
# The book's own editing inconsistencies, also noted on the affected rows:
#  - The table of contents (p.3) and the chapter itself call the seventh adventure LORE; the Campaign
#    Synopsis (p.14) calls it "Memory". The same paragraph writes "the Rite of Success" for the Rite
#    of Succession.
#  - The table of contents promises a "MASTER CAST OF SHADOWS"; the printed section (p.124) contains
#    only Mr. Radek.
#  - The Denver Mr. Johnson is "Brother Goldwing" through the whole meet scene and is first given the
#    first name Martin in the Hooks paragraph on p.37; the Legwork table (p.45) then reveals that
#    "Goldwing" is itself an assumed spiritual name over his birth name, Martin Bellecote.
#  - The Wuxing CEO is "Wu Lung-Wei" here; the campaign's existing row (from Blood in the Boardroom)
#    is "Wu Lung-Wai". Flagged on that row, not rewritten.
#  - Balance's Karma table (p.77) lists "Successfully delivering Sen Lo" with no point value.
#  - The Wuxing Skytower security sheaf is printed in a sidebar whose trigger numbers are lost in the
#    OCR; the IC order survives, the steps do not.
#  - Aden lairs on Mt. Ararat in Turkey although the city he destroyed, and the site of Rest, is
#    Tehran in Iran.
#  - Several stat blocks are garbled in the OCR (Grin's Charisma, the gargoyle's and the kludde's
#    attribute rows, Mack Donelley's Willpower and Essence, Kun Xilang's Essence, Branwen's Essence,
#    the Shasta security guards' Body) -- reference the book for those.
#  - The scrolls' two guardian spirits refuse to give their names; the book calls them "the Spirit of
#    the Winds" and "the Fire Elemental". The second row is filed here as "Fire Elemental of the
#    Scrolls" so the name is not a bare common noun.
# Source text: docs/Adventures/text/Shadowrun 3e - Survival Of The Fittest [FANPRO 10665].txt (130 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "Survival of the Fittest"
ORDER = 36
SOURCE = "Shadowrun 3e - Survival Of The Fittest [FANPRO 10665].pdf, pp. 4-126"
YEAR = "2062-2063 (mid-2062 to early 2063; exact dates deliberately undefined)"

SYNOPSIS = """
**Ghostwalker** came out of the astral rift left by Dunkelzahn's assassination in the last days of
2061, took Denver away from Aztlan in an afternoon, and then learned what his fellow great dragons
had allowed while he slept: **Dunkelzahn**, the Loremaster, had disposed of his hoard by a
metahuman *will*, and the **Jewel of Memory** -- the crystal holding the accumulated lore of
dragonkind -- had simply been handed to **Lofwyr**. Ghostwalker calls a council on an isolated
mountain plateau and demands the **Rite of Succession**. Enough of the others rise into the Posture
of Defiance -- Alamais, Hualpa, Mujaji, Rhonabwy, Lung, Ryumyo, Masaru, and finally **Hestaby** --
that Lofwyr must concede, and turns the concession into a trap of his own: not a duel here and now
but a *full* Rite, an indirect contest fought through proxies, "a test of all the facets of our
nature." From that moment every dragon at the plateau is every other dragon's rival. The runners are
Hestaby's proxies for the whole campaign, and for most of it they do not know it.

**Knowledge.** A fixer named **Mr. Radek** hires the team in **The Rubber Suit**, a giant-monster
themed yakuza club in Everett, to steal a datafile code-named "Kallisti" from an isolated system in
the **Shasta Lodge** on Mount Shasta -- the home of the great dragon Hestaby. Fifty thousand nuyen on
delivery, ten up front, ten days. They cross the embattled Northern Crescent of the California Free
State, climb the mountain past bound air elementals and a great form mountain spirit, and watch
Hestaby herself take off over their heads. The run is exactly what it looks like and completely a
lie: Hestaby commissioned it herself, through a middleman, to measure the team and to stage the
"theft" of a worthless file so her rivals would waste months hunting for what she never lost. Runners
who fail get sprung from the lodge basement by a disgruntled shaman called "Abby Nightbird", who is
Hestaby in human form.

**Cunning.** In Denver, the dwarf fixer **Sappho** brokers a meet at the **Imperial Jade** in
Chinatown. **Brother Goldwing** of the Children of the Dragon wants his leader, **Joshua
Morningstar**, extracted from the cult's UCAS-sector temple along with the files proving he takes
orders from a dragon other than Ghostwalker. Morningstar is a traitor and does not know it: Hestaby
conditioned him as a sleeper, planted the Saeder-Krupp telecom records herself, and steered the
ambitious Goldwing into "discovering" them. The runners kidnap a prophet, run the sector wall, and
find **Ghostwalker** waiting at the handover in a burned-out warehouse. He hears them out, pronounces
Morningstar innocent, has Goldwing pay them, and eats Goldwing.

**Elements.** The fixer **Toshi Akimura** hands the team a shrink-wrapped crate in a New Orleans
warehouse; a **Mitsuhama** Unit 13 hit squad is on it before his car is out of the lot. The crate
holds the **Elemental Scrolls of Ak'le'ar**, Dunkelzahn's bequest to **Hualpa**, stolen from the
Dunkelzahn Institute years ago and now Hestaby's to give back. The team rides **Cap'n Fixx**'s
smuggler *Gulf Runner* through a pirate boarding in the Yucatan Channel, hires the guide **Hilde** in
Macapa, dodges the Aztechnology adept **Reynaldo Ocelopan** and two blood-drinking Sangre del
Diablos, and delivers the scrolls to an old shaman in a nameless jungle village -- where **Nell
Miyamoto**'s MCT team makes its last grab and a feathered serpent arrives to collect.

**Balance.** The free spirit **Buttercup** of Yamatetsu buys them tea at the **Eye of the Needle**
and a Northrup Wasp strafes the restaurant on the orders of her rival **Hideo Yoshida**. The job:
extract the geomancer **Sen Lo** from Hong Kong ahead of the **Red Dragon Triad** he owes, deliver
him to Vladivostok, then break into the penthouse of the **Wuxing Skytower** and re-rake the gravel.
The "redecorating" is a geomantic ritual that couples Wuxing's power site to Yamatetsu's in Russia,
capping Wuxing's rise and yanking the dragon lines of the Pacific Rim -- and the runners get a vision
of **Lung** and **Ryumyo** circling them, each accusing the other.

**Hunting.** Flown to **Caerleon**, the team is briefed inside a Roman amphitheatre under a Transys
Neuronet complex by a robed man who is **Celedyr**. He gives them bronze amulets and sends them into
**Rhonabwy**'s Welsh lair for the **Silver Songbird**. Rhonabwy is waiting -- Hestaby tipped him off
-- and, barred by the Rite from harming another dragon's agents, offers a game instead: take the
Songbird, take a five-minute head start, and survive his hunters. The drake **Branwen**, the
shapeshifter **Volk**, a centaur, a gargoyle, a kludde and a naga come across ten kilometres of dark
Welsh countryside, homing on a tracking bug in the cage that also holds a kilo of C-12.

**Rest.** Radek sends them into the ruins of **Tehran** for a square of black silk hidden under a
mosque floor: the **Shroud of Shadows**, Dunkelzahn's bequest to **Aden**, which Aden has pointedly
never claimed. The dead city holds ghouls, shedim wearing the corpses of Aden's victims, the ghost
**Farah Al-Pasha** who wants her own body destroyed, the exorcist **Musa Muqla**, the mercenary
**Mack Donelley** hunting the same prize -- and a **wraith** that eats Karma and works both sides of
every fight it can start. The Shroud is the only thing that kills a wraith. Then Aden arrives and
demands they put it back, because taking it himself would claim it and letting it go would shame him.

**Lore.** Hestaby finally meets them in human form at the Shasta Lodge, explains the Rite and its one
inviolable rule -- a dragon may not strike another dragon's agents unless struck first -- and sends
their astral forms past the **Dweller on the Threshold** into the metaplanes for the *essence* of the
Jewel of Memory. Through the Places of Battle, Charisma, Destiny, Fear, Knowledge, Magic and Spirits
they reach the **Citadel**, and find **Lofwyr** coiled around the pedestal, unable to touch them and
offering them anything they can imagine to betray Hestaby -- or a lifetime of Saeder-Krupp's
attention if they refuse.

**Endgame.** The runners' astral forms are pulled to the Council plateau with the glowing crimson
jewel in their hands, while Alamais gloats over a physical Jewel that Lofwyr all but let him steal
and that is now worth nothing. Whoever they hand the essence to wins the Rite of Succession. Hestaby,
if chosen, hands it straight back to Lofwyr, refuses the title of Loremaster, and rules that
Dunkelzahn's dispersal stands -- and Lofwyr comes to Mount Shasta afterwards to say, stiffly, that he
underestimated her and will not do so again.
"""

TIMELINE = """
- **Long before this Age** -- dragons learn to impress information onto enchanted crystals; the role
  of Loremaster is created for the dragon holding the greatest store of that lore.
- **2053** -- Hestaby turns back a Tir Tairngire invasion of northern California; the Northern
  Crescent decides she is its shield.
- **2057** -- Dunkelzahn runs for UCAS president, wins, and is assassinated on inauguration night.
  His will disperses the hoard: the Jewel of Memory to Lofwyr, the Elemental Scrolls of Ak'le'ar to
  Hualpa, the Silver Songbird to Rhonabwy, the Shroud of Shadows to Aden, the Second Coin of Luck to
  Lung, the Ring Ouroboros to Ryumyo, the Jade Dragon of Wind and Fire to Wu Lung-Wei of Wuxing, and
  to Hestaby the encryption key to a private datastore on the Zurich Orbital Habitat.
- **After 2057** -- Nachtmeister and a few other upstarts challenge Lofwyr's claim and pay for it.
  Hualpa lends the Elemental Scrolls to the Dunkelzahn Institute; they are stolen (the adventure
  *Legacy*) and pass through many hands. Wuxing's Skytower begins drawing chi and Wuxing's star rises.
- **Late 2061** -- Ghostwalker emerges from the astral rift in the Federal District of Columbia,
  destroys the Aztlan sector teocalli and claims the Front Range Free Zone.
- **Mid-2062** -- Ghostwalker calls the Council. Lofwyr concedes a full Rite of Succession. From that
  moment the dragons act only through proxies and may not strike each other's agents unless struck.
- **Knowledge** -- Radek's meet at the Rubber Suit; ten days to the Kallisti file; the climb; Hestaby
  overflies the team; the lodge; "Abby Nightbird".
- **Cunning** -- Denver: the Imperial Jade, the temple run, the sector wall, Ghostwalker eats Goldwing
  and Morningstar's position is strengthened, exactly as Hestaby designed.
- **Elements** -- New Orleans pickup and the MCT ambush; the Gulf Runner and the pirates at the
  Yucatan Channel; Macapa and Ocelopan; two days upriver; the village, the MCT assault, the feathered
  serpent. A point to Hestaby, in Hualpa's own house.
- **Balance** -- the Eye of the Needle and Yoshida's helicopter; Hong Kong and the Red Dragon Triad;
  Vladivostok and Yoshida's company men; five days to the Skytower penthouse and the midnight
  deadline; the dragon-line vision; Wuxing stumbles, Yamatetsu prospers, Vladivostok goes strange.
- **Hunting** -- Caerleon, the amulets (good until sunrise), the wolves, the labyrinth, the treasury,
  Rhonabwy's game, the five-minute head start, the hunt across ten kilometres, Radek and the replica
  Songbird on the pick-up.
- **Rest** -- ten hours in Tehran from drop-off to dawn: the mad merc and the wraith's first Karma
  tap, the factions in the streets, the mosque, the Shroud, Aden on the way out. Radek pays in London
  and puts them on a plane to Mount Shasta.
- **Lore** -- Hestaby's briefing; the Dweller; the Places; the Citadel and Lofwyr's offer; the Council
  plateau and the choice.
- **After** -- Hestaby, if she wins, returns the Jewel to Lofwyr, refuses the Loremaster's title, and
  lets Dunkelzahn's dispersal stand; Lofwyr visits Mount Shasta in astral form to concede that he
  underestimated her; Hestaby opens Dunkelzahn's Zurich Orbital letter. If Lofwyr wins, nothing
  changes except that his authority is now his by right, and Ghostwalker nurses the grudge.
"""

ORGS = [
    {
        "name": "Council of Dragons",
        "org_type": "draconic council",
        "tier": 5,
        "headquarters": "An isolated mountain plateau, attended in spirit form",
        "summary": "The great dragons of the Sixth World in formal assembly -- the first gathering in an Age, convened by Ghostwalker to demand the Rite of Succession",
        "description": (
            "Dragon society is older than any metahuman history and almost all of its culture exists "
            "to keep predators who are territorial by nature from destroying each other. There had not "
            "been a council in longer than the Young Races reckon their history; the Matrix let the "
            "great dragons follow each other's affairs at a respectful distance, which Hestaby thought "
            "would ease tensions and which instead made it feel as though they were all in each "
            "other's domains at once. Business is conducted through rites -- the Rite of Honored "
            "Greeting, the Rite of Opening, the Rite of Parting -- and through postures: the Posture "
            "of Defiance, the Pose of Challenge, the lowered head of assent. Dragons address each "
            "other by use-names: Lofwyr is Gold-Master, Ghostwalker is Doll-Maker, Celedyr is "
            "Stone-Diver, Hestaby is Orange Queen, Mujaji is Rain Queen, and the dead Dunkelzahn is "
            "Far-Scholar. Attending the council are Hestaby, Lofwyr, Ghostwalker, Hualpa, Mujaji, "
            "Arleesh, Lung, Ryumyo, Masaru, Rhonabwy, Celedyr, Alamais and Aden; Sirrurg, "
            "Schwartzkopf and Kaltenstein stay away."
        ),
        "leadership": [
            {"name": "Lofwyr", "title": "De facto Loremaster (holder of the Jewel of Memory)", "notes": "Opens the council by right of the Jewel; concedes a full Rite rather than admit to arranging Dunkelzahn's death."},
            {"name": "Ghostwalker", "title": "Convenor of the council", "notes": "Calls it, then refuses to recognise it until a Loremaster is chosen by the old ways."},
            {"name": "Hestaby", "title": "Council member; Orange Queen", "notes": "Argues for another path, is answered with silence, and takes the Pose of Challenge anyway."},
            {"name": "Hualpa", "title": "Council member; feathered serpent of Amazonia", "notes": "Backs the Rite -- the fate of his own bequest is already in doubt, so he has little to lose."},
        ],
        "notes": (
            "The rules that make the campaign playable: dragons act through chosen agents and may not "
            "directly attack another dragon's agents unless those agents attack first (defence is "
            "always allowed); agents may freely attack each other; agents are protected from "
            "retribution after the Rite, which is why Lofwyr's threats at the Citadel are largely "
            "empty. No great dragon in this book has game statistics -- they are 'more akin to an "
            "elemental force than a living being that a group of shadowrunners can hope to overcome' "
            "(p.48). Endgame p.120: a dozen dragons ring the plateau, each glowing with an aura of "
            "multicoloured light; they bow one by one until only Ghostwalker, Alamais, Hestaby and "
            "Lofwyr stand. Handing the essence to a neutral dragon (Rhonabwy, Celedyr, Hualpa) is "
            "accepted as a surprising compromise; handing it to an extreme one (Alamais, Masaru, "
            "Ryumyo) voids the Rite or awards it to Lofwyr as runner-up; destroying it means no one "
            "is Loremaster and Hestaby defends the runners; splitting it works surprisingly well and "
            "creates a true council; keeping it forfeits the Rite's protection. DISCREPANCY: the "
            "Campaign Synopsis (p.14) writes 'the Rite of Success'."
        ),
        "allies": ["Draco Foundation"],
    },
    {
        "name": "Draco Foundation",
        "org_type": "foundation",
        "tier": 4,
        "headquarters": "Established to administer Dunkelzahn's will",
        "summary": "The body that administers Dunkelzahn's last will and testament and delivered its bequests to the great dragons -- the affront that starts the Rite of Succession",
        "description": (
            "Against all draconic tradition Dunkelzahn used metahuman legal machinery to dispose of "
            "his hoard, and the Draco Foundation was in place to administer the bequests the moment "
            "the will was released. It put the Jewel of Memory into Lofwyr's hands, making him "
            "Loremaster in fact if not by right, and carried the rest of the hoard out to the winds: "
            "the Elemental Scrolls of Ak'le'ar to Hualpa, the Silver Songbird to Rhonabwy, the Shroud "
            "of Shadows to Aden, the Second Coin of Luck to Lung, the Ring Ouroboros to Ryumyo, the "
            "Jade Dragon of Wind and Fire to Wu Lung-Wei of Wuxing, and to Hestaby the encryption key "
            "to a private datastore aboard the Zurich Orbital Habitat. The Foundation has since been "
            "working with the Dunkelzahn Institute of Magical Research to recover the stolen scrolls "
            "and the face that went with them."
        ),
        "notes": (
            "Named throughout but never staged: the Foundation is background, the reason the Rite "
            "exists at all. Legwork on the Shroud (p.101) turns up conflicting stories about whether "
            "the Foundation quietly delivered Aden's bequest or was told to go frag itself; Aden's own "
            "account is that he refused it, which is why the Shroud sits under a Tehran mosque and not "
            "in a hoard on Mt. Ararat. Dunkelzahn's Will is printed in Portfolio of a Dragon and on the "
            "official Shadowrun website."
        ),
        "allies": ["Dunkelzahn Institute of Magical Research", "Council of Dragons"],
    },
    {
        "name": "Children of the Dragon",
        "org_type": "cult",
        "tier": 2,
        "headquarters": "Temples across the UCAS and CAS; founded by David Dragonson",
        "summary": "The church that grew out of Dunkelzahn's death and worships the Great Dragon Spirit; split in two when Joshua Morningstar had his vision",
        "description": (
            "Founded by David Dragonson not long after Dunkelzahn's assassination, the Children of "
            "the Dragon have achieved a real measure of legitimacy through charity work -- soup "
            "kitchens for squatters, shelters, relief -- and are widely dismissed as 'that cult that "
            "worships Dunkelzahn or something'. They venerate a Great Dragon Spirit and accord the "
            "Awakened special status for being closer to the spirit world, which in practice means "
            "shamans outrank mages inside the hierarchy and mages like Martin Bellecote find their "
            "advancement quietly capped. Joshua Morningstar rose to be Dragonson's right hand and "
            "likely successor until his vision that Ghostwalker is the Great Dragon Spirit's new "
            "incarnation split the church; the main body kept Dragonson and its scepticism, and would "
            "be very happy to see the splinter brought back into the fold."
        ),
        "leadership": [
            {"name": "David Dragonson", "title": "Founder", "notes": "Greeted Morningstar's vision with scepticism; lost several temples to the schism."},
        ],
        "notes": (
            "Legwork TN 4, any magical contact or Matrix search (p.45): 1 the church has achieved some "
            "legitimacy through charity; 2 the split has caused the Children a lot of problems, "
            "especially since Morningstar's faction is drawing the new recruits; 3 Morningstar's "
            "position is not stable and his followers may drift back or turn on him; 4+ plenty of "
            "people would like the splinter folded back in, not least the main church, and the rest "
            "simply do not want Ghostwalker building a power base out of cultists. Pushing the "
            "Envelope (p.41): radical elements of the main sect may try to kidnap or kill Morningstar "
            "at the same time as the runners."
        ),
        "enemies": ["Children of the Dragon (Denver Faction)"],
    },
    {
        "name": "Children of the Dragon (Denver Faction)",
        "org_type": "cult",
        "tier": 2,
        "headquarters": "The Children of the Dragon temple, UCAS sector, Denver Front Range Free Zone",
        "summary": "Joshua Morningstar's breakaway faction, which holds that Ghostwalker is the reincarnated Great Dragon Spirit; it seized several temples, some of them violently",
        "description": (
            "When Morningstar collapsed at a board meeting immediately after Ghostwalker's appearance "
            "and woke claiming a vision that the pale dragon was the Great Dragon Spirit reincarnate "
            "and the chosen saviour of humankind, those who believed him split off and took several of "
            "the church's temples with them -- above all the Denver temple, in the city Ghostwalker had "
            "just claimed. Morningstar's talent for settling problems by direct and even brutal "
            "confrontation served him well; there was violence over the seizures, and he is willing to "
            "break heads if people in the cult will not play it his way. The faction runs a soup "
            "kitchen for Denver's swelling squatter population out of the ground floor of its temple "
            "and keeps three shifts of eight guards -- its own members with security experience, some "
            "of them reformed gangers -- on the building. Its Awakened members maintain the ward over "
            "the upper floors and are trained to recognise astral intruders."
        ),
        "leadership": [
            {"name": "Joshua Morningstar", "title": "Leader and prophet of the Denver faction", "notes": "Petitions Ghostwalker for an audience over and over and is refused; treats it as a test of faith."},
            {"name": "Martin Goldwing", "title": "Senior member; ambitious mage", "notes": "Wants to be Morningstar's right hand or better; hires the runners to destroy him."},
        ],
        "notes": (
            "Temple guards (p.40): B3 Q3(4) S3(4) C3 I3 W3 E1.3 R3(5), Init 3(5)+1D6(2D6), Combat Pool "
            "5, KP/Prof 2/3; Athletics 3, Etiquette 2 (Church 3), Interrogation 2, Pistols 3, SMG 4, "
            "Unarmed 4; cybereyes (low-light, thermographic), datajack, Muscle Replacement 1, Wired "
            "Reflexes 1; armor vest with plates 4/3; Uzi III. Four work the ground floor and two each "
            "the upper floors; the third-floor pair stay put at night to hold the private quarters. "
            "Morningstar's two travelling bodyguards use the same stats with Wired Reflexes 2 and "
            "Unarmed 5, in a Mitsubishi Nightsky with a rigger driver. Aftermath: whichever of "
            "Goldwing and Morningstar survives the warehouse becomes Ghostwalker's 'chosen prophet', "
            "and there is no reprisal against the runners from either the cult or the dragon."
        ),
        "allies": ["Sappho's Network"],
        "enemies": ["Children of the Dragon"],
    },
    {
        "name": "Thaumaturgical Research Unit 13",
        "org_type": "corporate division",
        "tier": 4,
        "headquarters": "Mitsuhama Computer Technologies; the field team operates out of MCT North America",
        "summary": "MCT's infamous magical resources and black-ops division -- 'special thaumaturgical research', which means black magic of the deepest and most secret kind",
        "description": (
            "Unit 13 is the part of Mitsuhama that goes after magic: if it is on the cutting edge of "
            "thaumaturgy, Unit 13 wants it, and it is willing to do whatever it has to in order to get "
            "it. The unit was behind the Boston operation that lifted the Elemental Scrolls of "
            "Ak'le'ar from a Dunkelzahn Institute lab at MIT&T -- an operation that did not work out to "
            "Mitsuhama's satisfaction -- and has been hunting the scrolls ever since. Elements is its "
            "last shot at them, and it does not intend to fail again. The field team is three elite "
            "operatives -- the adept Nell Miyamoto, the thaumaturge Kozakura Hiro and the street "
            "samurai Ono Isaeo -- backed by MCT security personnel the operatives treat as expendable "
            "so long as the objective is met."
        ),
        "leadership": [
            {"name": "Nell Miyamoto", "title": "Field team leader (MCT Security, Special Projects Division)", "notes": "Technically in command; keeps her word when the runners hand the scrolls over."},
            {"name": "Kozakura Hiro", "title": "Unit 13 thaumaturge", "notes": "Junior, arrogant, considers himself in charge; a coward under the arrogance."},
            {"name": "Ono Isaeo", "title": "Team muscle", "notes": "Backs Miyamoto without hesitation; despises Kozakura and fears his magic."},
        ],
        "notes": (
            "MCT security personnel (p.62): B4 Q4 S3 I3 W3 E4.6 R3, Init 3+1D6(2D6), Combat Pool 5, "
            "KP/Prof 1/3, human; loyal but not fearless -- they retreat before overwhelming force and "
            "especially before strange magical phenomena. Deploy a number equal to the runners. They "
            "hit the New Orleans warehouse the moment Akimura drives off, with orders not to damage "
            "the package; they may reach Macapa too late and pursue upriver; they gun down the "
            "village's warriors on the way to the hut. Miyamoto offers the runners their lives for the "
            "scrolls and means it; Kozakura blocks the old shaman's stunball and the shaman dies. "
            "Legwork TN 4 (p.58) names Unit 13, the Boston dust-up and the scroll hunt. Optional "
            "escalation: a Northrup Yellowjacket strafing the village."
        ),
        "allies": ["Mitsuhama Computer Technologies"],
        "enemies": ["Dunkelzahn Institute of Magical Research", "Aztechnology"],
    },
    {
        "name": "Shasta Lodge Shamans",
        "org_type": "mystical fellowship",
        "tier": 2,
        "headquarters": "The Shasta Lodge, Mount Shasta, California Free State",
        "summary": "The shamans who keep Hestaby's lodge, tap the mountain's mojo, help the people of the enclave -- and provide the lodge's real security",
        "description": (
            "A combination spiritual retreat and safehouse run by shamans loyal to Hestaby, high on "
            "the slopes of Mount Shasta. They tap serious power from the mountain, help out the people "
            "of the Shasta Enclave from time to time and otherwise keep to themselves; their public "
            "line is that they allow no tech up there, which is a lie the lodge's satellite dish and "
            "Red-9 mainframe put to rest. At least three shamans are on hand at all times and as many "
            "as a dozen respond to a general alarm, summoning the lodge hearth spirit or Shasta's own "
            "mountain spirits rather than fighting in person. They are a peaceful lot and will not "
            "throw their lives away for the building. Hestaby's recent seat on the Tir Tairngire "
            "Council of Princes split them: some walked out in protest at what looked like selling out "
            "to the elves, and others -- 'Abby Nightbird' claims to be one -- stayed to work for change."
        ),
        "notes": (
            "Shasta shamans (p.30): B3 Q3 S2 C5 I4 W6 E6 M6, Init 3+1D6, Astral Combat 7, Combat 6, "
            "Spell 5, KP/Prof 2/3; Clubs 3, Conjuring 6, Etiquette 3 (Tribal 5), Instruction 3, "
            "Negotiations 2, Pistols 2, Sorcery 6; Analyze Truth 3, Astral Barrier 4, Cure Disease 4, "
            "Detect Life 4, Detox 4, Heal 4, Light 2, Stabilize 2, Stunbolt 4; armor clothing, Walther "
            "Palm Pistol, staff or club 4M Stun. Make them initiates a grade or two below the highest "
            "grade player character if the team includes initiates. A shaman on duty is told the "
            "instant intruders are spotted and sends a Force 6 great form mountain spirit to capture, "
            "drive off or (last) kill; more Mountain and Sky spirits at Force 4-6 follow. A shaman "
            "investigates any attack on the lodge's Rating 6 ward astrally within two Combat Turns. "
            "They heal captured runners' injuries before locking them in the basement storeroom."
        ),
        "allies": ["Shasta Enclave Gypsies"],
    },
    {
        "name": "Shasta Enclave Gypsies",
        "org_type": "nomad community",
        "affiliation_contact_type": "Tribe",
        "tier": 1,
        "headquarters": "Caravans moving through the Shasta Enclave and the Northern Crescent",
        "summary": "Refugee caravans who have made a culture out of being driven from home; fiercely independent, and they consider Hestaby their patron and protector",
        "description": (
            "Northern California is full of people driven from their homes by border wars and other "
            "conflicts, and many of them have taken up a mobile life in caravans of vans, cars and "
            "mobile homes. They call themselves gypsies and have developed their own culture and "
            "traditions in fifty years of moving. The transient population of the Shasta Enclave is "
            "far larger than Mount Shasta City's few thousand permanent residents; bands settle in one "
            "spot for weeks or months and move on. They are fiercely independent and have no problem "
            "with anyone who does not bother them, which makes them the obvious cover for a team that "
            "wants to cross the enclave without drawing attention -- but they consider Hestaby a patron "
            "and protector, and they will not be pleased to learn their guests intend to rob her."
        ),
        "notes": (
            "Getting There Is Half the Fun (p.25) offers the gypsies as an encounter, a cover identity "
            "and a source of local knowledge; runners can pose as a small band, and Debugging (p.27) "
            "suggests arriving at the lodge as gypsies petitioning to see Hestaby as a legitimate "
            "infiltration route. Contrast with the hate-groups also in the area: Human Nation and the "
            "Humanis Policlub have more than a few supporters this close to the disputed Tir border, "
            "and marauding gangs roam the Northern Crescent (use Vehicle Rigger stats, SR3 p.79, with "
            "Bike skills, plus a Tribal Shaman for magical support)."
        ),
        "allies": ["Shasta Lodge Shamans"],
        "enemies": ["Human Nation", "Humanis Policlub"],
    },
    {
        "name": "Sappho's Network",
        "org_type": "smuggling and fixer operation",
        "tier": 2,
        "headquarters": "The CAS sector of the Denver Front Range Free Zone",
        "summary": "The dwarf fixer Sappho's decade-old Denver operation: she can find, acquire or smuggle nearly any contraband into or out of the Free Zone",
        "description": (
            "Sappho has been part of Denver's shadow community for over a decade and is known "
            "primarily for her ability to find and acquire whatever a client wants -- for the right "
            "price, nearly any contraband, smuggled into or out of the Front Range Free Zone across "
            "five walled sectors. She brokers shadowruns less often, but since Ghostwalker's arrival "
            "the fragile balance in the Denver shadows has been in permanent upheaval and there has "
            "been no shortage of opportunities for a businesswoman of her stature, so she has been "
            "expanding. She has provided services for Martin Goldwing before, which is why he came to "
            "her, and she is entirely happy to end up with influence over the Children of the Dragon "
            "whichever way the fight goes: gratitude if Goldwing wins, dirt on Morningstar if he does "
            "not. She knows nothing about the great dragons' contest; she is running a business."
        ),
        "leadership": [
            {"name": "Sappho", "title": "Fixer", "notes": "All business; personal feelings never get in the way of the job or her reputation."},
        ],
        "notes": (
            "A resource, not an obstacle: so long as the runners do not cross her, Sappho will find "
            "them work afterwards -- It's a Wrap (p.45) suggests a smuggling run out of Denver heading "
            "home -- and she is especially interested in teams that can smuggle. She negotiates up to "
            "15 percent above Goldwing's offer and no further; get greedy and she wishes them luck, "
            "pays the 1,000 nuyen appearance fee and sends them on their way. Information brokers in "
            "post-Ghostwalker Denver monitor the airports and checkpoints for new shadow talent, so "
            "the whole meet may end up on a surveillance chip for sale on the open market."
        ),
    },
    {
        "name": "Red Dragon Triad",
        "org_type": "triad",
        "tier": 4,
        "headquarters": "Hong Kong Free Enterprise Zone",
        "summary": "One of the major Hong Kong triads, well named -- word has it they ultimately answer to the great dragon Lung on the mainland",
        "description": (
            "The Red Dragon is one of the major triads of Hong Kong, and the name is not decoration: "
            "the street says they ultimately answer to the great dragon Lung on the mainland, though "
            "nobody can say what a great dragon wants with a criminal syndicate. They have had "
            "difficulties of late that may or may not be connected to Wuxing's swelling influence in "
            "the Free Enterprise Zone, they have been fighting the Yakuza over the black market and "
            "smuggling in the Sea of Japan, and they have been coming down harder than usual on "
            "anyone who crosses them. The geomancer Sen Lo owes them a considerable gambling debt from "
            "games rigged in the house's favour; they ransacked his apartment looking for money and "
            "leads, left a watcher on it, and want him alive if possible and dead as an example if "
            "not. Their oaths of loyalty are not decorative either: a soldier magically coerced into "
            "talking bursts into flame and burns to ash."
        ),
        "leadership": [
            {"name": "Kun Xilang", "title": "Adept and initiate; leads the team hunting Sen Lo", "notes": "Raised in the Triad by a Triad father; rose on her adept talents despite her sex."},
            {"name": "Little Chang", "title": "Wujen attached to Xilang's team", "notes": "Dwarf; summons Spirits of the Ground before a fight when he can."},
        ],
        "notes": (
            "Triad soldiers (p.71): B4 Q4(5) S4(5) C2 I3 W3 E4.7 R3, Init 3+1D6(2D6), Combat Pool 5, "
            "KP/Prof 1/3; Athletics 3, Etiquette 1 (Triad 3), Pistols 4, SMG 3, Unarmed 4 (Kung Fu 5); "
            "Kung Fu 4 (Kick Attack 5); Boosted Reflexes 1, cybereyes (flare compensation, low-light), "
            "Muscle Replacement 1; Ares Viper Slivergun with integral silencer, HK-227-S with laser "
            "sight, silencer and folding stock; armored jacket 5/3. Well trained and literal about "
            "orders: sliverguns first, then hand-to-hand, submachine guns only when they must, because "
            "the noise draws attention. At least as many as there are runners. They will let the team "
            "walk if Sen Lo is handed over without trouble and kill everyone if not. Legwork TN 4, any "
            "criminal contact (p.78). DISCREPANCY: the campaign already carries a Seattle triad called "
            "the Red Dragon Association; the book never links the two, and the Hong Kong Red Dragon "
            "should be treated as its own body unless the GM wants a shared parent."
        ),
        "enemies": ["Wuxing, Inc.", "Yakuza (Watada-rengo)"],
    },
    {
        "name": "Knights of Rage",
        "org_type": "corporate security order",
        "tier": 3,
        "headquarters": "Celedyr's underground complex beneath the Transys Neuronet facility at Caerleon, Wales",
        "summary": "Celedyr's household guard -- ceremonially dressed, submachine guns at their belts, and authorised to use lethal force on guests who try to leave",
        "description": (
            "The men who hold Celedyr's lair are not corporate suits. They dress as Amon does, in "
            "ceremonial garb that would look at home on a film set -- wide gold collars, belted kilts, "
            "sandals, cloth headdresses -- and they watch visitors with cold stares and their hands "
            "near the submachine guns at their belts. They stand at each of the doors down the "
            "composite-walled corridors between the elevator and the amphitheatre. Their function in "
            "the adventure is simple and unambiguous: runners who decline Celedyr's job are wined and "
            "dined and then quietly informed that they are not leaving until somebody else has run the "
            "Songbird job, and it is the Knights of Rage who make that stick."
        ),
        "notes": (
            "No stat block is given; scale them to the team. Escape from the complex should be "
            "difficult to impossible: the doors out need both a keycard and a thumbprint scan, both at "
            "Rating 8 (SR3 p.235), the complex is more than 50 metres underground behind reinforced "
            "ferrocrete, and the Knights will use lethal force. Amon states the terms; the Knights are "
            "the punctuation. If the runners keep refusing, Celedyr holds them a few weeks as guests "
            "and then lets them go."
        ),
        "allies": ["Transys Neuronet"],
    },
    {
        "name": "Rhonabwy's Wild Hunt",
        "org_type": "paranormal retinue",
        "tier": 3,
        "headquarters": "Rhonabwy's domain around Llandovery, Wales",
        "summary": "The dragon's hunting pack -- a drake, a wolf shapeshifter, a centaur, a gargoyle, a kludde and a naga -- loosed on anyone he decides to make sport of",
        "description": (
            "Rhonabwy keeps a menagerie of intelligent and half-intelligent paranormals on his Welsh "
            "land and uses them as guards, scouts and, when the mood takes him, hunters. The drake "
            "Branwen leads and the wolf shapeshifter Volk is her second; both can pass for people in "
            "the outside world and serve as their master's eyes and ears. The rest are a stallion "
            "centaur whose herd patrols the estate, a European gargoyle from one of the lairs in the "
            "domain, a kludde that shifts between crow, black cat and wolf-like canine and takes its "
            "orders directly from Rhonabwy's mind, and a naga recently acquired and being tried out. "
            "They do not work well together -- Branwen and Volk look out for the others and the others "
            "are disdainful and will not come to each other's aid -- and they carry no serious weapons "
            "or high-tech gear. What they have is speed, magic and paranormal powers, and they will "
            "not stop until their quarry is out of reach, because they fear Rhonabwy more than death."
        ),
        "leadership": [
            {"name": "Branwen", "title": "Drake; leader of the hunt", "notes": "Carries the locator for the tracking bug in the Songbird's cage."},
            {"name": "Volk", "title": "Wolf shapeshifter; second in command", "notes": "Tracker and guide; allergic and vulnerable to silver."},
        ],
        "notes": (
            "Opening tactics (p.87): during the five-minute head start Branwen sustains Improved "
            "Invisibility on Andres and Volk, the naga sustains Camouflage on herself, Volk takes wolf "
            "form; then Branwen triggers the tracking signal for a five-second burst and sends the "
            "kludde ahead in crow form to scout. Kludde and gargoyle swoop first, the invisible centaur "
            "and werewolf flank from surprise, Branwen and the naga cast and provide spell defence from "
            "cover (naga: Blindness on obvious magicians; Branwen: Firewall to pen the runners in). "
            "Everyone but Branwen and Volk goes straight for the kill, but they take separate targets "
            "rather than ganging up. Branwen would rather bring live prisoners back for Rhonabwy to "
            "play with, which is the one lever the runners have. Spirits are forbidden to both sides. "
            "The unnamed hunters -- the gargoyle, the kludde and the naga -- are statted in the book at "
            "pp.91-92 and are not built as separate rows here."
        ),
    },
    {
        "name": "Donelley's Mercenary Company",
        "org_type": "mercenary company",
        "tier": 2,
        "headquarters": "Mobile; currently operating in the ruins of Tehran",
        "summary": "Mack Donelley's small outfit, hired by an unnamed client to bring the Shroud of Shadows out of Tehran -- the runners' direct competition",
        "description": (
            "Donelley built his own small operation on the back of years of contract work, including "
            "the Desert Wars, and the men he has with him in Tehran are seasoned professionals of "
            "similar ability who are completely loyal to their commander. Their current contract is "
            "the same object the runners are after, the Shroud of Shadows, but their employer could "
            "not tell them exactly where it is, so Donelley has burned days hunting for the right "
            "mosque and been distracted by the wraith and the other things living in the ruins. He is "
            "a reasonable man and will happily propose an alliance -- offering to help the team in "
            "exchange for transport out of the area, which is a lie, since he has his own -- and will "
            "betray them at the first opportunity that puts him on top."
        ),
        "leadership": [
            {"name": "Mack Donelley", "title": "Commander", "notes": "Belfast-born; being a mercenary is all he knows and he loves the work."},
        ],
        "notes": (
            "Donelley's men, four of them (p.104): B4(5) Q4(6) S4(6) C2 I3 W4 E7.5 R3(4), Init "
            "3(4)+1D6(2D6), Combat Pool 5(6), KP/Prof 2/3; Etiquette 1 (Mercenary 3), Heavy Weapons 4, "
            "Launch Weapons 4, Pistols 4, Rifles 4, Stealth 2 (Urban 4), Unarmed 4; Boosted Reflexes 1, "
            "flare compensation, Muscle Replacement 2, smartlink, aluminium bone lacing; armor 5/4; "
            "FN-HAR and Beretta Model 101T (both smartgunned) and an Ares Antioch grenade launcher with "
            "ten HE; goggles with low-light and thermographic vision, micro-transceiver 5, Nav-Dat GPS, "
            "survival kit, three trauma patches. Ork and troll mercenaries are fairly common; apply "
            "racial modifiers to taste. They can show up as rescuers during another faction's fight, at "
            "the mosque, or both; the wraith works hard to turn the two teams on each other before "
            "either realises they are rivals."
        ),
        "enemies": ["Islamic Unity Movement"],
    },
    {
        "name": "Islamic Unity Movement",
        "org_type": "religious movement",
        "tier": 4,
        "headquarters": "Mecca; the prophet Badr al Din Ibn Eisa",
        "summary": "The Muslim religious movement behind Badr al Din Ibn Eisa; Musa Muqla's cadre is cleansing the ruins of Tehran of spirits in its name, without endorsing the New Islamic Jihad's militancy",
        "description": (
            "Badr al Din Ibn Eisa's charismatic leadership drew devout Muslims across the Middle East "
            "into the Islamic Unity Movement, and his apparent assassination and miraculous "
            "resurrection convinced many of them, Musa Muqla among them, of his holiness. Not all of "
            "them follow the movement's militant wing: Muqla is not fully supportive of the New "
            "Islamic Jihad's calls for militancy and has chosen his own quest instead, taking a small "
            "cadre of fanatical followers into the ruins of Tehran to survey them and to see whether "
            "the city can be purged of the spirits and creatures haunting it, so that decent people "
            "can live there again. He has made a particular point of cleansing every mosque and holy "
            "place of malign spiritual influence, which is exactly the wrong disposition toward a team "
            "that has come to loot one. He does not yet know the Shroud of Shadows exists; if he "
            "learns, he will want it delivered into Ibn Eisa's hands in Mecca."
        ),
        "leadership": [
            {"name": "Badr al Din Ibn Eisa", "title": "Prophet and leader of the Islamic Unity Movement", "notes": "Apparently assassinated and miraculously resurrected (Year of the Comet)."},
            {"name": "Musa Muqla", "title": "Imam, exorcist and curse-breaker; leads the Tehran mission", "notes": "Pursuing his own quest rather than the New Islamic Jihad's militancy."},
        ],
        "notes": (
            "Muqla's followers (p.105): B4 Q4 S4 C2 I3 W3 E6 R3, Init 3+1D6, Combat Pool 5, KP/Prof "
            "1/3; Assault Rifles 3, Etiquette 1 (Muslim 3), Pistols 3, Stealth 2 (Urban 4), Unarmed 4; "
            "lined coat 4/2; AK-97. They are frightened of the spirits and undead they are facing but "
            "have enough faith in Muqla's abilities to stand beside him. The cadre will help the "
            "runners against an obviously inhuman foe and then want to know who they are; if Muqla "
            "learns their destination he insists on coming, which becomes a problem the moment the "
            "Shroud comes out from under the floor tile. Year of the Comet pp.52-54 covers Ibn Eisa "
            "and the New Islamic Jihad; the militant wing is name-dropped here and not built."
        ),
        "enemies": ["Donelley's Mercenary Company"],
    },
    {
        "name": "Manadyne",
        "org_type": "corporation",
        "tier": 3,
        "headquarters": "UCAS",
        "summary": "The thaumaturgical corporation Martin Bellecote worked for before he became Brother Goldwing -- and one of the parties the GM may put in the New Orleans warehouse",
        "description": (
            "Manadyne employed Martin Bellecote after Brown University, where he took a degree in "
            "thaumaturgy; he performed his duties well enough and started up the corporate ladder "
            "while something in his life stayed missing. He found it in the Children of the Dragon and "
            "left his corporate job a few months later, taking the spiritual name Goldwing with him. "
            "The corp turns up again on the list of factions that might have got wind of the Elemental "
            "Scrolls surfacing in New Orleans and sent a team of their own -- alongside Wuxing, the "
            "Draco Foundation, the Dunkelzahn Institute and the Atlantean Foundation."
        ),
        "notes": (
            "Two mentions and no scenes: Goldwing's Legwork table (p.45, 2 successes) and the Pushing "
            "the Envelope list of possible third parties in Midnight Run (p.52). Built as a row "
            "because it is the corporate half of Goldwing's history and a ready-made rival team."
        ),
    },
]

LOCATIONS = [
    {
        "name": "The Rubber Suit",
        "location_type": "nightclub",
        "district": "Everett",
        "security_level": "Patrolled / Commercial",
        "summary": "Exclusive giant-monster-movie club in Everett and a known yakuza hangout; Mr. Radek picks it for the first meet and lets the runners draw their own conclusions",
        "description": (
            "You reach it under a tall glowing image of a giant reptile breathing neon blue flames "
            "that flash with the Japanese characters spelling out the club's name. Past the bouncers, "
            "the floor below is laid out as a scale model of the ruins of Tokyo from about a hundred "
            "years ago, so customers can feel like a giant monster stomping through the city; giant "
            "trid-screens cover the walls with loops of old flat-vid monster movies spliced together "
            "with softcore Japanese porn over a retro music track. A bar runs the whole perimeter of "
            "the floor above the ruins so patrons can lean at the rail and look down at the wreckage. "
            "The clientele mixes slumming corporate salarymen with street trash -- Anglos, Asians, "
            "mixed-bloods, a few Natives, metahumans, metavariants and the odd strange changeling. "
            "Radek sits on a 'building' down among the ruins with an untouched drink and a pocket "
            "secretary on the roof beside him. New Seattle p.48."
        ),
        "notes": (
            "Known as a hangout for the local yakuza -- the book invites the players to draw "
            "conclusions from Radek's choice of venue. If the campaign is based somewhere other than "
            "Seattle, use a local equivalent; the book suggests the Rubber Suit is popular enough to "
            "have inspired imitators or a chain, and that any venue with giant-lizard or dragon "
            "associations is appropriate. Hearth spirit (p.22): the club's hearth spirit appears as a "
            "man in a bad rubber monster suit about six feet tall, clumsy (Quickness of Force -1) but "
            "unusually strong (Strength of Force +2), with Innate Spell (Flamethrower) breathing bright "
            "blue flame from its mouth; it can speak but generally only issues high-pitched roars. "
            "Optional violence: the Red Rovers go-gang or the clown-fixated Scatterbrains outside (New "
            "Seattle p.50), possibly a test arranged by Hestaby -- watch for a tiny roto-drone or a "
            "spirit observing -- or a Mafia, Seoulpa Ring or Triad hit on the local kobun inside."
        ),
    },
    {
        "name": "The Shasta Enclave",
        "location_type": "protected wilderness region",
        "city": "Mount Shasta City",
        "district": "Northern Crescent, California Free State",
        "security_level": "Low Security",
        "summary": "Hestaby's domain in northern California: Interstate-5 straight through the middle, a small town at the mountain's foot, gypsy caravans, and radar and bound air elementals over all of it",
        "description": (
            "The land Hestaby has claimed and defended for years, dominated by Mount Shasta itself -- "
            "one of the tallest mountains in North America, snow-capped almost always, standing over "
            "everything for miles like a giant watching the whole area. Interstate-5 runs right "
            "through the centre of the enclave and traffic on it is permitted, so a low-profile team "
            "can drive as far as Mount Shasta City without arousing suspicion. The town has grown over "
            "fifty years and is still only a few thousand residents; the transient population is far "
            "larger, with gypsy tribes and families passing through constantly and settling for weeks "
            "or months at a time. The surrounding Northern Crescent is an embattled place, dangerously "
            "close to the elven lands of Tir Tairngire, with marauding gangs on the roads and "
            "anti-metahuman feeling running high -- though not inside the enclave, which is pointedly "
            "tolerant. The wilderness on the mountain is primal, mystical and a little scary."
        ),
        "notes": (
            "Aerial defences: radar and other early-warning systems plus bound Force 5 air elementals "
            "and wind spirits with orders to stop any aircraft not escorted by one of the enclave's "
            "spirits, disabling intruders with their powers and forcing them down, and to engage astral "
            "intruders in astral combat; destroyed or banished spirits are replaced within hours and "
            "every intrusion is reported to the lodge and to Hestaby. Aircraft must set down outside "
            "the enclave and cover the last forty-odd miles overland. Climbing the mountain takes at "
            "least eight hours from the base; roll 5 dice against the worst of the team's Open Stealth "
            "results, once for a road or air approach and four times (one per two hours) for a climb. "
            "Detection sends a Force 6 great form mountain spirit (B10 Q4x2 S10 C6 I6 W6 R4, Init "
            "12+1D6, astral 26+1D6, Attacks 10S; Accident, Concealment, Guard, Materialization, "
            "Movement, Search), then Mountain and Sky spirits at Force 4-6. Hestaby herself overflies "
            "the approach at some point; Perception with 13 dice against the team's Open Stealth. "
            "Critters for the slopes: eyekillers, griffins, icedrakes, perytons, piasma, thunderbirds, "
            "horned bears."
        ),
    },
    {
        "name": "Shasta Lodge",
        "location_type": "lodge",
        "city": "Mount Shasta City",
        "district": "High slopes of Mount Shasta, Shasta Enclave",
        "security_level": "Corporate High Security",
        "summary": "Hestaby's home on the mountain: half old ski lodge, half Native American medicine lodge, with a satellite dish, a Red-9 mainframe and the Kallisti file in an isolated box",
        "description": (
            "Built on the site of an old ski lodge and still shaped like one, though the current "
            "building carries a great many touches that look more like a Native American medicine "
            "lodge than a ski resort. It is not remotely as rustic as the shamans let people believe: "
            "a satellite dish is tucked into a corner of the roof and the place is as modern as "
            "anywhere in the sprawl, Matrix hook-up and all. There is no fence or barricade, just a "
            "small parking lot in front and a detached garage that would hold half a dozen vehicles; "
            "front and side entrances are covered by floodlights. The map on p.29 gives a basement, a "
            "heating room, dining area, meditation room, kitchen, reception and lounge, a security "
            "room, an office, a storeroom that doubles as a holding cell, the garages, and Hestaby's "
            "own chambers -- redwood-panelled, with a sunken seating area, a state-of-the-art home "
            "theatre and flatscreen, and walls hung with carved wooden masks, weapons and paintings. "
            "The exterior is quiet and peaceful. It is also the first target and the last stop of the "
            "whole campaign."
        ),
        "notes": (
            "Security (pp.29-30): tiny cameras sweep 15 metres in every direction with image "
            "recognition, TN 8 to see or hit plus range; roll 5 dice per turn in line of sight against "
            "the team's Open Stealth. Maglocks with card-readers on every outside door; reinforced "
            "composite doors and armored glass at Barrier 8, wired for a silent alarm; a Rating 6 ward "
            "over the outer walls that lodge shamans and their spirits pass freely. Six guards on duty "
            "at all times: three in reception, one on the monitors, two on the secure areas. Guards: "
            "Q3(5) S3(5) C3 I3 W3 E1.3 R3(5), Init 3(5)+1D6(2D6), Combat Pool 5, KP/Prof 2/3; Assault "
            "Rifles 4, Pistols 4, Interrogation 3, Unarmed 3, Car 2, Etiquette 2 (Corporate 4); "
            "commlink, cybereyes (display link, low-light, thermographic), datajack, Muscle Replacement "
            "2, Wired Reflexes 1; light security armor 6/4; AK-97 (Body garbled in the OCR). The "
            "basement holding room has a small window two metres up, a reinforced composite door on a "
            "maglock, a bench, and a Rating 8 ward inside the walls that blocks spells and pins astral "
            "forms; its maker senses any attack on it. Prisoners are healed, stripped of everything but "
            "clothing and armor, and searched quickly enough to miss gear at Concealability 12+. "
            "Computer systems in MATRIX_HOSTS. A distraction on the mountainside pulls an astral shaman "
            "and then security out of the building."
        ),
        "controlling_org": "Shasta Lodge Shamans",
    },
    {
        "name": "Imperial Jade",
        "location_type": "restaurant",
        "city": "Denver",
        "district": "Chinatown, CAS sector, Front Range Free Zone",
        "security_level": "Patrolled / Commercial",
        "summary": "Out-of-the-way Chinatown hole in the wall where Sappho brokers the Morningstar job; a private back room and a spread that is mostly real food",
        "description": (
            "A little out-of-the-way hole in the wall tucked between a couple of larger buildings on "
            "the crowded streets of Chinatown, in the CAS sector of the Free Zone. The slight, older "
            "Chinese man at the front counter is expecting you and takes you straight through the main "
            "restaurant to a private back room, seats you and closes the door. The table is already "
            "laid with a dozen different dishes and most of it is real, not soy-substitute, which in "
            "post-Ghostwalker Denver is a statement about the client. It is the sort of place the "
            "Triads have been using more and more as their activity in the city steps up, and the book "
            "offers it as a perfect stage for a shootout in the finest Hong Kong action-film style -- "
            "possibly with Triad hitters who have ties to Lung, in which case the attack on the "
            "restaurant is not random at all."
        ),
        "notes": (
            "The meet: Sappho and 'Mr. Johnson' enter after the runners are seated. Goldwing's gold "
            "ring is a Sustaining Focus 5 running Analyze Truth throughout -- roll 5 dice against a "
            "lying runner's Willpower -- and he maintains metamagical shielding, so spells cast on him "
            "or Sappho take +2 TN and they roll an extra 12 dice to resist. He masks his aura and his "
            "initiate grade but not the fact that he is a mage, and a watcher spirit hovers invisibly "
            "at his shoulder to tell him if anyone assenses him. Getting to the meet at all can be an "
            "encounter -- Denver gangers, urban scavengers, or an information broker who watches the "
            "airports and checkpoints for new shadow talent and sells the surveillance chip of the "
            "whole negotiation on the open market."
        ),
    },
    {
        "name": "Children of the Dragon Temple (Denver)",
        "location_type": "temple",
        "city": "Denver",
        "district": "UCAS sector, Front Range Free Zone",
        "security_level": "Patrolled / Commercial",
        "summary": "Morningstar's three-storey converted industrial building: worship hall and soup kitchen below, his office and files above, his quarters at the top",
        "description": (
            "A three-storey brick-face industrial building well over a hundred years old, gutted and "
            "heavily renovated into a church while keeping most of its original brickwork and its "
            "tall, narrow windows. It sits smack in the middle of the UCAS sector, which has seen "
            "better days but took relatively little damage during Ghostwalker's arrival -- the gangs "
            "and the occasional riot are slowly doing the work the dragon did not. Double front doors "
            "open into a lobby and then the worship hall; there is a side entrance into the soup "
            "kitchen the Children run for the local squatters, and a rear loading dock, and a paved "
            "parking lot wraps the whole structure with the road running past the front. The first "
            "floor holds the worship hall, kitchen, canteen, archive and library and storage, and a "
            "meditation room; the second, Morningstar's office and his secretary, a magic practice "
            "room and a meeting room; the third, Morningstar's quarters -- living room with an "
            "automated kitchen and a bedroom -- plus a recreation centre and a small temple room for "
            "employees only. Maps on pp.39 and 127."
        ),
        "notes": (
            "Open 8 AM to 6 PM daily with visitors welcome; the soup kitchen runs to 10 PM, after "
            "which every entrance is locked and needs a maglock card carried only by high-ranking "
            "members (Goldwing will not lend his -- it would implicate him). Doors and windows are "
            "wired to an alarm outside normal hours; the correct passcard kills the door alarms, "
            "otherwise handle them separately. Third-floor quarters and Morningstar's second-floor "
            "office have individual maglocks. A Rating 5 ward covers the upper two floors, maintained "
            "and attuned by the Awakened membership; attacking it alerts Morningstar and every Awakened "
            "Child in the building instantly. Morningstar works to 10 PM, retires upstairs and is "
            "asleep by about 11:30. Guard shifts and stats on the faction's org row; host system in "
            "MATRIX_HOSTS. The planted evidence -- German Alliance and Saeder-Krupp PLTG call records "
            "plus a journal about his unnamed 'master' -- is 150 Mp behind a Rating 5 Data Bomb; a "
            "Computer (6) Test shows the files have been tampered with, though not by whom."
        ),
        "controlling_org": "Children of the Dragon (Denver Faction)",
    },
    {
        "name": "Denver Sector Walls and Checkpoints",
        "location_type": "border crossing",
        "city": "Denver",
        "district": "The UCAS / CAS sector boundary, Front Range Free Zone",
        "security_level": "Corporate High Security",
        "summary": "Five walled cities in one, patrolled by paranoid trigger-happy military forces -- and the runners have to move a kidnapped cult leader across one of the seams",
        "description": (
            "The Front Range Free Zone is more like five different cities, all walled off from each "
            "other and patrolled by paranoid, trigger-happy military forces, and it has only got worse "
            "since Ghostwalker took over and the nations that claim Denver understood how vulnerable "
            "they are. Between terrorists and political dissidents, border security has tightened until "
            "a shadowrunner cannot make a dishonest living any more. The walls protecting the UCAS and "
            "CAS sectors are at least five metres high, reinforced ferrocrete at Barrier Rating 16, "
            "topped with concertina wire; the authorised checkpoints are queues of vehicles and guards "
            "asking for identification. Over the wall is a Perception Test on 5 dice against the team's "
            "Open Stealth; through the checkpoint is an Opposed Test between the lowest-rated ID in the "
            "team and a Verification Rating of 3, with a failure meaning being pulled out of line, "
            "detained and -- much worse -- having the vehicle searched. Shadows of North America "
            "pp.203-206."
        ),
        "notes": (
            "Border guards patrol in threes (p.42): B3 Q3(4) S3(4) C3 I3 W3 E0.8 R3(5), Init "
            "3(5)+1D6(2D6), Combat Pool 5, KP/Prof 1/2; Etiquette 2 (Governmental 3), Interrogation 3, "
            "Pistols 4, Rifles 4, Unarmed 3; cybereyes (low-light, thermographic), datajack, Muscle "
            "Replacement 1, smartlink, Wired Reflexes 1; light security armor 6/4 with the "
            "communications option; Ingram Smartgun. Backup arrives within one minute (20 Combat "
            "Turns). Morningstar is the complication: unsedated he can cast, and even bound, gagged and "
            "blindfolded he can astrally project -- picture his astral form manifesting in a checkpoint "
            "queue screaming for help, or a watcher spirit heading back to the temple with his "
            "location. Captured runners are pulled out of custody by Ghostwalker, who has them and "
            "Morningstar brought to his Denver lair instead of the warehouse."
        ),
    },
    {
        "name": "Abandoned Warehouse (CAS Sector Border)",
        "location_type": "warehouse",
        "city": "Denver",
        "district": "Burned-out CAS sector bordering the former Aztlan sector",
        "security_level": "No Security / Barrens",
        "summary": "Empty warehouse in a burned-out strip on the old Aztlan sector line, chosen as a quiet handover site -- and where Ghostwalker eats the runners' employer",
        "description": (
            "A warehouse building in a burned-out section of the CAS sector bordering on what used to "
            "be the Aztlan sector. There was probably a skirmish here between CAS and Azzie troops, or "
            "trouble when Ghostwalker first came down on the Aztlan sector like a ton of bricks; "
            "either way the place is empty, which makes it a good spot to handle business without "
            "unwanted visitors. Mr. Johnson waits inside with another man: tall and thin, dressed all "
            "in white from head to toe, hair almost pure white and slicked straight back from a high "
            "forehead. He welcomes the team, and then his neck elongates, wings sprout from his back "
            "and he swells to tremendous size, covered in gleaming scales the colour of old ivory, a "
            "reptilian head looking down from near the ceiling as Ghostwalker settles back on his "
            "haunches."
        ),
        "notes": (
            "Ghostwalker asks how the runners were hired, why they took Morningstar, and to see the "
            "data; defiance earns a demonstration (a section of wall melted with fiery breath or "
            "smashed with a tail or claw) and then, if that does not suffice, he eats one of them. He "
            "asks their honest opinion of Morningstar's guilt and weighs it. He knows when he is lied "
            "to. Then he has Goldwing hand over the credstick and eats Goldwing in a single strike, "
            "licking the blood off his pale jaws: 'That's what happens to those who cause trouble for "
            "me.' Runners who try to stop him die. Optional escalations: an Aztechnology hit team with "
            "heavy weapons striking at Ghostwalker outside his lair; squatter kids or a prostitute and "
            "a client wandering in for privacy, which Ghostwalker leaves the runners to handle while he "
            "watches how they do it. If Morningstar was killed earlier, Goldwing lives and becomes "
            "Ghostwalker's chosen prophet, and the runners have failed Hestaby."
        ),
    },
    {
        "name": "Akimura's Lakeside Warehouse",
        "location_type": "warehouse",
        "city": "New Orleans",
        "district": "The lakeside district, Confederation of American States",
        "security_level": "Low Security",
        "summary": "The virtually abandoned lakeside pickup site where Toshi Akimura hands over the Elemental Scrolls and a Mitsuhama team comes through both doors",
        "description": (
            "The lakeside area of the Big Easy is virtually abandoned this late at night, so there is "
            "nobody to see the team arrive outside the old warehouse. Akimura is waiting inside with "
            "two silent elven women bodyguards who are either twin sisters or have been bio-sculpted "
            "to look identical, and a plastic packing crate just over a metre long and about half that "
            "wide and tall, sealed in heavy shrink-wrap. The crate is light for its size -- about "
            "twenty kilos -- and adds a point of impact armor to what is inside. With it come a chip "
            "carrying a map to the destination and the rendezvous in the Mississippi Delta, and a "
            "certified credstick for the advance. Akimura leaves through the back of the warehouse to "
            "his waiting car, and as he drives off the Mitsuhama team that has been watching the "
            "building decides to move in, entering front and back at once."
        ),
        "notes": (
            "Pay: 150,000 nuyen with ten percent (15,000) up front. MCT sends security personnel equal "
            "in number to the runners, attacking immediately with orders to avoid damaging the package. "
            "If Akimura and his bodyguards are still present, add extra MCT personnel; the elves fight "
            "but focus on extracting their boss. Optional third parties who might have heard the "
            "scrolls surfaced: Wuxing, the Draco Foundation, the Dunkelzahn Institute, Manadyne, the "
            "Atlantean Foundation, or a rival team working for another great dragon who only knows "
            "that Hestaby wants the crate to reach Amazonia. The scrolls can throw a mana warp or wild "
            "magic into the warehouse, and a stray round into the crate brings the guardian spirits out "
            "-- which is also the book's designated rescue if MCT is winning. Target: Smuggler Havens "
            "and Shadows of North America cover New Orleans."
        ),
    },
    {
        "name": "Gulf Runner",
        "location_type": "smuggling vessel",
        "city": "Gulf of Mexico",
        "district": "Mississippi Delta to Macapa, via the Yucatan Channel and the Caribbean",
        "security_level": "Low Security",
        "summary": "Cap'n Fixx's patched-together smuggler running the runners and a hold full of BTL chips down to Amazonia -- and boarded by pirates at the Yucatan Channel",
        "description": (
            "The rendezvous is somewhere in the swampy Mississippi Delta in the dead of night, and the "
            "first thing the team sees is the gleam of an ork's cybereye winking like a firefly as the "
            "rangefinder plays over them. The Gulf Runner has stats similar to a Harland and Wolff "
            "Clasique but none of the amenities: not an opulent yacht, a seaworthy smuggler modified "
            "and patched together over years. Fixx and a crew of a dozen get the team out to her by "
            "launch and put to sea as fast as they can, particularly if anyone mentions the trouble "
            "back in New Orleans. The hold carries cases of BTL chips and other electronic goods bound "
            "for Amazonia alongside the runners' crate. The trip takes the better part of a week, with "
            "plenty of room for encounters -- other pirates, Awakened sea creatures, a jumpy Aztlan "
            "border patrol, or a toxic spirit or mutant thrown up by the chemical agents of the "
            "Yucatan War."
        ),
        "notes": (
            "One of Fixx's crew is on the take from a pirate band and has sold them the cargo "
            "manifest; the runners can find him if they think to look. The pirates hit as the Gulf "
            "Runner leaves the Yucatan Channel for the Caribbean near dawn: three GMC Riverine boats, "
            "each with an Ingram Valiant LMG on a hardpoint (50(c), BF/FA, 7S) and six pirates, one "
            "boat carrying the shark shaman Grin with a Force 5 sea spirit. Pirates (p.54): B4 Q3 S3 "
            "C2 I3 W3, Init 2+1D6, Combat Pool 4, KP/Prof 2/3; Athletics 2 (Swimming 3), Boats B/R 3, "
            "Clubs 3, Diving 2, Etiquette 2 (Pirate 3), Heavy Weapons 4, Pistols 4, Rifles 4, "
            "Motorboat 4, Unarmed 3; Ceska Black Scorpion; armored jacket 5/3. They want the crate and "
            "the contraband, do not want to sink the ship, and will kill everyone aboard if they have "
            "to. They break off if they lose half their number, two of three boats, or Grin. The crew "
            "is no match for them without the runners. If the team has a rigger with Motorboat, "
            "Akimura can supply a boat and the whole encounter becomes a chase."
        ),
    },
    {
        "name": "Macapa",
        "location_type": "port city",
        "city": "Macapa",
        "district": "Mouth of the Amazon, Amazonia",
        "security_level": "Patrolled / Commercial",
        "summary": "One of the coastal gateway cities the Amazonian Awakened keep open to the world: trade freely, break no local laws, and do not go far into the interior",
        "description": (
            "The city lies on the equator at the mouth of the Amazon River, one of the coastal cities "
            "the Amazonian Awakened maintain as gateways to the rest of the world. People come here to "
            "trade freely so long as they do not break local laws or venture too far into the "
            "interior. It is like a lot of free port cities: a riot of activity along the waterfront, "
            "ships from all over the world, every sort of person going about their business. The air "
            "is hot and sticky even by the water and the jungle is visible in the distance, always "
            "encroaching on the city limits. There are more than a few metahumans and changelings here "
            "-- Amazonia is supposed to be a haven for the Awakened -- though a striking number of them "
            "are squatters or beggars. Chaotic, full of potential dangers for the unwary, and easy "
            "enough for street-smart runners to handle."
        ),
        "notes": (
            "Finding Hilde in the small waterfront dives takes asking around and an Etiquette (4) Test, "
            "about an hour. Aztechnology keeps agents in Macapa and the other coastal cities; Reynaldo "
            "Ocelopan clocks the team on arrival, pegs them as corporate or government agents or mercs, "
            "and pays local street toughs to hassle them so he can watch how they fight. Macapan "
            "gangers: use the pirate stats minus vehicle skills and gear, armed with clubs and knives, "
            "at least as many as there are runners, often orks and trolls (or changelings); they back "
            "down if outclassed or if anyone dies. Leaving is harder than arriving: Ocelopan's ground "
            "team plus two pursuit Riverines with three crew each. He has no legal authority here and "
            "wants things quiet, but he and his men can disappear before the authorities intervene. "
            "Local colour on offer: bar brawls, more gangs, devil rats, harpies, an incubus."
        ),
    },
    {
        "name": "Nameless Village (Amazon Interior)",
        "location_type": "village",
        "city": "Amazon interior",
        "district": "Two days upriver from Macapa, Amazonia",
        "security_level": "No Security / Barrens",
        "summary": "A clearing of huts and lean-tos deep in the rainforest where an old shaman waits to receive the Elemental Scrolls -- and where Mitsuhama makes its last grab",
        "description": (
            "Two days upriver from Macapa the Amazon is wide and sluggish and murky, its banks a riot "
            "of thick jungle foliage and flowering vines, the air loud with insects, birds and animal "
            "cries and busy with things moving in the water, some of them small and some of them not. "
            "Hilde moors the boat and the team walks inland to a small nameless village of Amazonian "
            "natives: little more than a collection of huts and lean-tos in a small clearing, with the "
            "largest hut raised above the others on stilts. Four native hunters armed only with spears "
            "and bone knives meet the runners and one of them, with enough broken English to manage "
            "it, guides them to the big hut. Inside waits an old shaman with deeply tanned, weathered "
            "skin in native dress, a cloak and headdress of brightly coloured feathers and a necklace "
            "of shells and beads, who welcomes them in almost perfect English and asks why they have "
            "come. They were expected."
        ),
        "notes": (
            "The old shaman is gracious to anyone reasonably polite, opens the box, seems genuinely "
            "surprised to see the scrolls, bows and thanks them for returning them to Amazonia; he can "
            "also heal a worn-down team before the fight. En route the runners meet two Sangre del "
            "Diablos, Awakened blood-drinking trees (YOTC p.144): B16/8 Q5x0 S14 I2/5 W6 E8 R3, Init "
            "3+1D6; Compulsion, Corrosive Secretions, Engulf (sludge engulf, 8M per Combat Turn, armor "
            "does not protect), Immunity (Fire), Magical Guard -- Opposed Essence vs Willpower to "
            "compel, again to engulf. Ocelopan ambushes the landing party as they head inland. Then "
            "Miyamoto's team gun down the village warriors and move on the hut; if the runners hand the "
            "scrolls over she lets them go, and the old man dies attacking the corporate team alone. "
            "Afterwards a feathered serpent sent by Hualpa glides down beside the main hut, gravely "
            "thanks the runners on the nation's behalf, offers no explanations, and takes the scrolls. "
            "Flying in is a bad idea: Amazonia's air defences include spirits, elementals and, "
            "occasionally, a dragon."
        ),
    },
    {
        "name": "Eye of the Needle",
        "location_type": "restaurant",
        "district": "Downtown Seattle",
        "security_level": "Patrolled / Commercial",
        "summary": "One of the most exclusive restaurants in the metroplex -- revolving, with a skyline view, an elven maitre d' who checks weapons at the door, and a helicopter incoming",
        "description": (
            "Getting in normally is difficult; Mr. Radek's name works wonders, and the team is "
            "expected. The elven maitre d' politely asks them to check any weaponry at the door before "
            "showing them to their table. The restaurant rotates slowly, so the view of the metroplex "
            "skyline changes through the meal, and there is plenty of privacy. Buttercup materialises "
            "somewhere nobody is looking and is simply beside the table -- a young Japanese woman not "
            "much more than eighteen at most, rose-coloured blouse, dark skirt, black hair cut almost "
            "boyishly short, a broad smile and a slight bow -- and takes a seat at the end of the "
            "table. She will indulge the runners in anything on the menu and takes only tea herself, "
            "and only if they are having something. The armored glass, it turns out, will not stop a "
            "heavy machinegun."
        ),
        "notes": (
            "The meet is at 10 PM. Gate-crashers: a secret Perception (6) Test for each runner (or a "
            "Sorcery Test at TN 6 for anyone running Detect Enemies) spots a Northrup Wasp closing fast "
            "with a heavy machinegun swivelling on its chin mount. Anyone not under cover resists base "
            "damage 10D; the chopper banks for another pass over a full Combat Turn and makes three "
            "passes in all, breaking off early if the runners leave the room or hurt it. Wasp stats SR3 "
            "p.311 with an RPK HMG on a chin turret (half recoil); the rigger pilot has Init 8+3D6, "
            "Gunnery 4, Rotor Aircraft 4, Control Pool 8, Karma Pool 4. Make sure someone spots it, or "
            "have Buttercup call the warning. She is caught off-guard and injured if nobody warns her, "
            "though far less seriously than a mortal would be, and she urges everyone out before Lone "
            "Star arrives. Optional escalation: an HE rocket on the second pass, or three killer drones "
            "flying into the restaurant, or gunmen coming in afterwards to finish the survivors. This "
            "is the restaurant in the Space Needle; the book calls it only 'one of the most exclusive "
            "restaurants in the metroplex'."
        ),
    },
    {
        "name": "Sen Lo's Apartment and Office",
        "location_type": "apartment complex",
        "city": "Hong Kong",
        "district": "An upscale part of Hong Kong",
        "security_level": "Patrolled / Commercial",
        "summary": "The geomancer's ransacked two-storey home and office, still watched by a Red Dragon agent who tails whoever comes looking",
        "description": (
            "Sen Lo's home and office occupy a two-storey apartment in a fairly upscale part of Hong "
            "Kong, and the address in Buttercup's dossier leads to a place that has been searched very "
            "thoroughly by someone looking for something. Furniture is overturned; clothing, books, "
            "computer chips and other materials are scattered across the floor. The Red Dragon Triad "
            "did this hunting for money and for any clue to where their debtor had gone, and they left "
            "the place under surveillance in case he came back. The data chips on the floor hold Sen "
            "Lo's client records, and a Computer (4) Test through them establishes quickly that he is "
            "in serious debt, though not to whom. There are no biological material links anywhere in "
            "the apartment -- he was meticulous about that -- but there are personal items good enough "
            "for ritual tracking by anyone who knows symbolic linking."
        ),
        "notes": (
            "Unless the runners enter by extraordinary means (invisibly, for instance), the watching "
            "Red Dragon agent -- Han -- notes their arrival and the Triad puts a tail on them; make "
            "secret Perception (8) Tests once per day to notice him. Tracking Sen Lo down the mundane "
            "way is Etiquette (Street) TN 6, one test per two hours, fifteen successes in total. A "
            "ritual tracking attempt gets Sen Lo a Perception (8) Test to notice it and move on, "
            "forcing the runners to keep up. Hong Kong is under mana surge and wild magic conditions "
            "throughout (MITS pp.86-88): Astral Perception (6) senses it, and the Wild Magic Table is "
            "rolled at the start of the scenario and once for each day the team is in the city."
        ),
    },
    {
        "name": "Sen Lo's Houseboat (Hong Kong Docks)",
        "location_type": "safehouse",
        "city": "Hong Kong",
        "district": "The Hong Kong docks",
        "security_level": "Low Security",
        "summary": "A houseboat lost among dozens of other boats and junks along the docks, where a frightened geomancer is waiting for the money to buy off a Triad",
        "description": (
            "Sen Lo is hiding aboard a houseboat along the Hong Kong docks, mixed in among dozens of "
            "other boats and junks -- one grey hull in a floating crowd, which is exactly the point. He "
            "went to ground two days before Buttercup's briefing, when the Red Dragon threatened him "
            "over his gambling debts, hoping to raise enough money to pay them off before they found "
            "him. A team that tracks him here finds a cautious old man on his guard but willing to "
            "listen; put Buttercup's offer of payment and a way out of Hong Kong to him and he takes it "
            "gladly and without haggling, and tells them straight away that the Red Dragon Triad is "
            "after him, which is going to complicate their departure considerably."
        ),
        "notes": (
            "The Triad closes in one of three ways: the runners spot and take the tail (Han burns to "
            "ash rather than talk), or Han watches them lead him to Sen Lo, or the Triad simply finds "
            "the houseboat at about the same time. Xilang's team then arrives to collect. Snatching Sen "
            "Lo rather than talking to him is easy -- he is a powerful magician but not a fighter -- but "
            "Buttercup is not paying for damaged goods, and killing him costs the runners the first "
            "half of the fee though the Skytower job stays open. If the Triads are winning badly, Sen Lo "
            "can throw a well-timed illusion to give the team an edge."
        ),
    },
    {
        "name": "Wuxing Skytower",
        "location_type": "corporate megastructure",
        "city": "Hong Kong",
        "district": "Hong Kong Free Enterprise Zone",
        "security_level": "Corporate Extraterritorial",
        "summary": "Wuxing's corporate headquarters, built on a power site the Jade Dragon of Wind and Fire has been supercharging; the penthouse is a Rating 8 power site laid out as a temple",
        "description": (
            "One of the tallest and most prominent buildings on the Hong Kong skyline and one of the "
            "best protected, and it stands on a power site that Wu Lung-Wei intensified with "
            "Dunkelzahn's bequest, the Jade Dragon of Wind and Fire. It has been drawing more and more "
            "chi ever since and Wuxing's star has risen with it. The top floor is nothing like a "
            "corporate office: angled glass panels in the ceiling drop light in precise patterns "
            "across a veined marble floor, scrolls of Chinese calligraphy hang beside hexagonal mirrors "
            "in red lacquered frames, and small tables beneath them carry statuettes carved from jade "
            "and crystal. At the centre a circular depression of fine pale gravel is raked into whorls "
            "and patterns, and inside that sits a square pool with a wooden footbridge arcing over it, "
            "water trickling from small fountains, lily pads and lotus blossoms on the surface, silver "
            "and gold fish beneath, softly glowing lanterns at the corners. On a raised pedestal at the "
            "middle of the bridge stands a jade carving of three leaping fish so detailed they might "
            "have just come out of the pond. Beauty and harmony, and under it a hum of barely "
            "restrained energy that even the mundanes can feel."
        ),
        "notes": (
            "Access to the penthouse: the executive elevator (a passcode known only to high-ranking "
            "executives) or an emergency stairwell that cannot be entered without alarming the whole "
            "building; or from outside by climbing, flight, cutting a window, or the rooftop helipad "
            "(maglocked security doors, a guard station always manned by two). Exterior cameras catch "
            "anything larger than a bird. A Rating 8 ward around the penthouse blocks all astral "
            "intruders; attuning to it is extremely hard for any but high-grade initiates, and "
            "attacking it brings the duty security mage in astral form the next Combat Turn. Three "
            "bound Force 6 air elementals patrol the outside at all times. The background count adds +4 "
            "TN to all astral tests near the tower, the elementals' Perception included, which the "
            "runners can turn to their advantage. The area is an astral shallow: astral forms are "
            "permanently visible as if manifest, even to mundanes -- and the shallow vanishes if the "
            "runners succeed. The penthouse is a Rating 8 power site: any Awakened character adds 8 "
            "dice per Combat Turn to magical tests, divided as desired. Guards and the wujen are "
            "statted on the location's controlling org; host in MATRIX_HOSTS. The job itself is 180 "
            "minutes base, divided by the total successes on Intelligence (4) Tests from each runner "
            "working; all 1s is a critical error and the whole plan misfires."
        ),
        "controlling_org": "Wuxing, Inc.",
    },
    {
        "name": "Vladivostok Hospitality House",
        "location_type": "brothel",
        "city": "Vladivostok",
        "district": "The entertainment district",
        "security_level": "Low Security",
        "summary": "The discreet house in the entertainment district where Buttercup takes delivery of Sen Lo and briefs the runners on the Skytower job",
        "description": (
            "Vladivostok and Hong Kong have a good deal in common -- both are gateway cities to the "
            "Pacific Rim on the edge of a potentially hostile frontier, both full of different sorts "
            "of people doing business, much of it in the shadows -- and then the resemblance stops. "
            "Vladivostok is frozen and old, and even the newer buildings look grey and bowed with age; "
            "people call the place depressing and they are not wrong. The meet is in the entertainment "
            "district at a hospitality house where the team is expected and is shown to a private room "
            "upstairs. Sen Lo rises and bows deeply to Buttercup when she enters -- 'It is an honour to "
            "meet you, gracious lady' -- and she sends him out to the ladies waiting outside so that "
            "business can be discussed. Then a fistful of credsticks goes on the table and she asks "
            "whether the team would like to triple its money."
        ),
        "notes": (
            "Getting to the meet is the complication: two of Hideo Yoshida's Yamatetsu men in a "
            "Eurocar Westwind pick the runners out of their descriptions at whatever port of entry they "
            "used, or off the Matrix if they entered legally, rented a car or touched a public "
            "terminal. The sedan paces them; try to shake it and the company men call in backup and "
            "herd them toward an ambush or roadblock, with at least three more cars converging in "
            "minutes. Ignore it and the men follow them to the meet, which Buttercup will not "
            "appreciate -- though she will not blame the runners unless they clearly led the tail to "
            "her. Optional expansion: a full chase with security helicopters, drones and elementals "
            "guided by an astral security mage or a city spirit. Pay: 50,000 nuyen per runner for Sen "
            "Lo, 120,000 each for the Skytower run, 5 percent of the second fee if they fail but "
            "survive."
        ),
    },
    {
        "name": "Hideo Yoshida's Estate (Popov Island)",
        "location_type": "penthouse",
        "city": "Vladivostok",
        "district": "Popov Island",
        "security_level": "Corporate High Security",
        "summary": "The private estate the deposed Yamatetsu chairman keeps near the corporation's new worldwide headquarters, where captured runners are interrogated and then disposed of",
        "description": (
            "Yamatetsu's new worldwide headquarters sits on Popov Island, near Vladivostok, and Hideo "
            "Yoshida keeps a private estate there for when business brings him to the city. Runners "
            "taken by his men are not brought to the corporate HQ -- that would leave a record -- but "
            "here. Yoshida opens with an offer to double whatever Buttercup is paying them for a "
            "betrayal, with a corporate mage on hand running Analyze Truth to verify their answers and "
            "ready to Mind Probe them if they refuse to talk. The joke, which he does not believe, is "
            "that the runners do not actually know anything about Buttercup's plans. When he is "
            "satisfied he has everything they have, he orders his men to take them out and kill them "
            "and dump the bodies somewhere they will not be found -- including the ones who cooperated, "
            "on the reasonable grounds that anyone who trusts a corporate shark like him has earned it. "
            "Sen Lo is kept alive until Yoshida works out what Buttercup wanted with him."
        ),
        "notes": (
            "Yamatetsu company men loyal to Yoshida's faction (p.73): B5 Q4(5) S5(7) C2 I4 W4(5) E5.3 "
            "R4(7), Init 4(7)+1D6(3D6), Combat Pool 6(7), KP/Prof 3/3; Athletics 3(4), Car 3(4), "
            "Etiquette 3 (Corporate 5), Interrogation 3, Pistols 4(5), Stealth 4(5), Shotguns 5(6), "
            "Unarmed 5(6); cybereyes (flare compensation, low-light, thermographic) and smartlink; all "
            "cultured bioware -- adrenal pump, enhanced articulation, orthoskin 2, synaptic accelerator "
            "2, trauma damper; Ceska Black Scorpion and Mossberg SM-CMDT, both smartgunned; armor 6/4. "
            "The book explicitly offers a fresh team of runners sent to extract Sen Lo from the estate "
            "if the player characters get themselves killed here. Yoshida may also simply offer the "
            "team double to take Buttercup's job and deliberately botch it, which would ruin them on "
            "the street and end Hestaby's use for them."
        ),
        "controlling_org": "Yamatetsu Corporation",
    },
    {
        "name": "Caerleon Facility",
        "location_type": "corporate facility",
        "city": "Caerleon",
        "district": "Southeastern Wales",
        "security_level": "Corporate Extraterritorial",
        "summary": "Transys Neuronet's steel-and-glass complex wrapped around a ring of standing stones, with Celedyr's lair fifty metres beneath it inside a Roman amphitheatre",
        "description": (
            "The corporate facility stands out from the picturesque Welsh countryside: new buildings of "
            "steel, chrome and glass, more out of place still because they surround a ring of "
            "ancient-looking standing stones and tumbled ruins, the past and the future side by side. "
            "A landing pad sits on the outskirts. Inside, past a security checkpoint, a bank of "
            "elevators takes visitors down an unmarked distance -- no floor readout over the door, no "
            "control panel -- behind a keycard and a thumbprint. The corridors below look like smooth "
            "stone and are actually a modern ceramic composite; two sets of guards in ceremonial dress "
            "watch them. The double doors at the end open on a vast chamber that is the inside of an "
            "ancient ruined amphitheatre, its walls and seating rising all around, roofed with a dome "
            "of fused rock with electric lamps bolted to it casting light down into the arena. A "
            "conference table and chairs stand on the sand across from a hi-tech flatscreen multimedia "
            "deck, and a tall fair-skinned man with brassy hair in a long belted robe and sandals "
            "invites you to sit down and talk business."
        ),
        "notes": (
            "Transys has given Celedyr millions of nuyen of equipment and researchers in exchange for "
            "his support and his occasional insight into their projects; language and communication "
            "fascinate him. Terms offered here: 150,000 nuyen each, or up to twice that in Transys "
            "hardware, software and cyberware with free installation, or certified credit, gold, gems, "
            "or up to two units of refined orichalcum each (street value 176,000 nuyen if they can "
            "fence it), or about 25 percent more in corporate script or negotiable securities; "
            "magicians may take spells taught or magic items instead. No advance, but any reasonable "
            "mundane gear they can justify, theirs to keep. Celedyr vetoes scouting Rhonabwy's lair in "
            "advance and gives at most a week to prepare -- partly the rules of the Rite, which he does "
            "not explain. Refusal means indefinite hospitality under the Knights of Rage. Optional: a "
            "staged 'terrorist' attack on the facility as a test, or dry runs of the whole break-in on "
            "the Transys VR rig, with small differences to account for the gaps in Celedyr's knowledge."
        ),
        "controlling_org": "Transys Neuronet",
    },
    {
        "name": "Rhonabwy's Lair",
        "location_type": "underground bunker",
        "city": "Llandovery",
        "district": "Rhonabwy's domain, Wales",
        "security_level": "Corporate High Security",
        "summary": "A cave mouth in a hillside opening on tunnels wide enough to drive an eighteen-wheeler through; motion sensors, a Rating 10 ward and Neurostun on the threshold",
        "description": (
            "The drop-off is a rolling field about ten kilometres from the lair, over an hour past "
            "sunset, the countryside around the dragon's land dark except for stars and a crescent "
            "moon while the lights of villages show in the distance. An hour's walk at a normal pace "
            "brings the team to a cave-like structure set into a hillside. Behind the cave mouth a "
            "massive sliding metal hatch covers the real entrance, and behind that the lair is a "
            "labyrinth of tunnels cut wide enough to accommodate Rhonabwy's frame -- big enough to "
            "drive an eighteen-wheel truck through. The map Celedyr supplies runs straight to the "
            "treasury; everything else the runners see if they stray is the gamemaster's to invent, "
            "and Rhonabwy is watching their progress the whole way."
        ),
        "notes": (
            "Security: Rating 5 motion sensors in the cave entrance detect any creature moving inside "
            "and automatically activate miniature surveillance cameras; the sliding hatch has a Rating "
            "6 maglock keypad; a Rating 10 ward covers the entire lair, on top of the heavy layer of "
            "soil and rock an astral intruder would have to cross first. Trip anything and Neurostun "
            "floods the cave entrance at 6S Stun per Combat Turn, and unconscious runners are carried "
            "before Rhonabwy. En route across the fields: Open Stealth Tests at -2 for foliage and "
            "unfamiliar ground, then a Perception Test on 5 dice; success means a pack of wolves (one "
            "per runner: B5 Q5(x4) S4 I3/4 W2 E6 R5, Init 5+2D6, Combat Pool 5, KP/Prof 2/2, Attacks "
            "7M) led by a wolf shapeshifter using Volk's stats, ambushing from the shadows. Gunfire, "
            "muzzle flashes, explosions and magic can all give the team away to the guardian spirits "
            "(TN 6, lower for anything very obvious); Celedyr's amulets cover magical detection only "
            "while no magic is used, and expire at sunrise."
        ),
    },
    {
        "name": "Rhonabwy's Treasury",
        "location_type": "vault",
        "city": "Llandovery",
        "district": "The heart of Rhonabwy's lair, Wales",
        "security_level": "Corporate High Security",
        "summary": "A domed cavern of art, armor and literal tons of gold, with the Silver Songbird hanging from a brass stand and the dragon himself standing in it disguised as a statue",
        "description": (
            "A vast domed cavern, its walls sloping upward toward a ceiling lost in shadow, sconces "
            "along them holding modern electric lights shaped like brass carriage lamps whose golden "
            "glow is intensified by what they light. All around are tables and shelves of treasure: "
            "statues of fine marble, bronze and jade; gold-hilted swords in jewelled scabbards; "
            "necklaces of silver and pearls; several full suits of armor from different eras; an "
            "upright slice of translucent crystal fully two metres tall and a metre wide held in a "
            "silver stand; a statue of a rearing dragon almost three metres tall with scales of "
            "burnished red gold. In the centre, on a raised stone platform, stands a stack of gold "
            "bricks over two metres tall and wide and at least twice that in length -- hundreds upon "
            "hundreds of them, literally tons of gold, enough to bankroll a megacorp. And hanging from "
            "a brass stand, a finely wrought silver cage holding a bird of the same material, every "
            "feather picked out in the smallest detail, which shrugs its wings as though it were alive."
        ),
        "notes": (
            "The door is Barrier 24 with a Rating 10 ward and a Rating 6 maglock keypad; every other "
            "security measure in the room is switched off because Rhonabwy is standing in it, and the "
            "correct keypad code turns them off anyway. Astral perception shows active auras around the "
            "Songbird, the rearing dragon statue and many other pieces, but Rhonabwy masks his own aura "
            "and cannot be picked out. Touching the cage starts the Songbird singing -- an impossibly "
            "sweet, liquid melody that fills the air like a gentle perfume -- and the statue swells, "
            "its scales deepening to blood red and fire coming up in its eyes, as the armored door "
            "slams shut. Rhonabwy already has a fair idea who they are and is very hard to lie to; tell "
            "him about the amulets and he bends close to examine one with his breath in the wearer's "
            "face. Attacks bounce off his hide or his automatic magical defences; persist and he turns "
            "someone into stone or a toad to make the point, and drops it afterwards. Then the offer: "
            "the Songbird, a five-minute head start, and his hunters."
        ),
        "controlling_org": "Rhonabwy's Wild Hunt",
    },
    {
        "name": "Ruins of Tehran",
        "location_type": "ruins",
        "city": "Tehran",
        "district": "Northern Iran",
        "security_level": "Zero Zone -- Lethal Response",
        "summary": "A city Aden destroyed forty years ago and nobody rebuilt: ghouls, harpies, squatters, ghosts, shedim wearing the dead, mercenaries, missionaries, and a wraith farming all of it",
        "description": (
            "Tehran must have been quite the city once. The ruins sprawl in every direction as far as "
            "the eye can see across a mountainous plateau; some buildings are still intact after forty "
            "years of neglect and many others are skeletal shells or piles of rubble, with the "
            "evidence of unchecked fires still showing as blackened frames poking into the sky. The "
            "remaining streets are littered with rubble and the rusting hulks of automobiles stripped "
            "of anything useful years ago. The ruined streets are dark and quiet and the feeling of "
            "being watched from shadowy corners, empty doorways and windows that loom like blank "
            "staring eyes never lets up; something cries in the distance and it might be human, and it "
            "sounds like it is hunting. Aden levelled the place after its ayatollah declared holy war "
            "on the Awakened, the survivors were driven out, and the city has been considered cursed "
            "ever since -- so it filled up with outcasts and, ironically, with Awakened scavengers."
        ),
        "notes": (
            "Ten hours from drop-off to dawn pick-up; a TR-55 tilt-rotor flies nape-of-the-Earth over "
            "northern Iran and lifts off with its lights out. The factions, all of which the wraith "
            "works on: packs of devil rats, ghouls and harpies (Critters pp.25, 30, 32); wandering "
            "shedim in the badly decayed bodies of Aden's victims, women and children among them, "
            "hunting better hosts; Farah Al-Pasha's band of ghosts warring on the shedim for the use of "
            "their own corpses; refugee squatters with average attributes, skills at 2 or 3 and crude "
            "clubs and knives, who will not normally attack an armed team unless the wraith pushes "
            "them; Musa Muqla's cadre cleansing the holy places; and Mack Donelley's mercenaries after "
            "the same prize. The wraith only feeds on conflict with intelligent beings, so the ghouls, "
            "the shedim, the squatters, the missionaries and the mercs all pay it and the devil rats "
            "and harpies do not. The real challenge is getting across the city without giving it the "
            "bloodbath it wants. Year of the Comet pp.52-54 and Target: Awakened Lands p.98."
        ),
    },
    {
        "name": "Mosque of the Shroud",
        "location_type": "mosque",
        "city": "Tehran",
        "district": "The ruins of Tehran, northern Iran",
        "security_level": "No Security / Barrens",
        "summary": "The ruined mosque where Aden hid the Shroud of Shadows under a floor tile; holy ground to Muqla, poison to the shedim, and the stage for the campaign's most avoidable firefight",
        "description": (
            "The mosque was probably once quite impressive and even now there is a certain majesty to "
            "it, but its outside walls and roof have taken considerable damage and forty years of "
            "weather have worked at the structure through the holes. Rubble is scattered across the "
            "tile floor, a few support columns have collapsed along with sections of the ceiling, and "
            "much of the tile and stonework is cracked and worn. Small creatures scuttle out of the way "
            "as you step over the debris and your feet crunch on broken glass and loose stones. Despite "
            "all of it there is a strange feeling of serenity and peace here, almost an aura of "
            "holiness, and every member of the team senses it on entering and feels it grow stronger "
            "as they move further inside. The Shroud lies in a hollow space beneath one of the heavy "
            "floor tiles in the main chamber; a Strength (4) Test moves the tile."
        ),
        "notes": (
            "The shedim are dimly aware of the Shroud, sense that it is inimical to them and avoid the "
            "mosque, but will attack to stop it being used on them. Muqla considers the building holy "
            "ground and will take a very dim view of looting it; Donelley has been hunting for exactly "
            "this mosque for days. The likely shape of the scene: the runners reach the hiding place, "
            "rivals appear and demand they stand aside, the wraith starts inciting everyone, and "
            "bullets and magic fly through mosaics and columns -- after which the Shroud can be used to "
            "destroy the wraith, or the wraith can be destroyed first and the Shroud's aura then makes "
            "negotiation with the survivors possible. Optional hardening: make the mosque a power site "
            "aspected against every use of magic except dispelling and countering, which cripples the "
            "runners' offence but not Muqla's defensive magic; or add a bound spirit, a guard critter "
            "or a magical barrier over the Shroud itself. Perception Tests let the runners notice that "
            "the wraith shies away from the Shroud and whoever carries it; as a last resort Muqla works "
            "out that it smothers such spirits and says so."
        ),
    },
    {
        "name": "The Citadel",
        "location_type": "metaplanar citadel",
        "city": "The metaplanes",
        "summary": "A castle floating hundreds of feet above a green countryside at the heart of the metaplanes, where the essence of the Jewel of Memory turns on a pillar and Lofwyr waits",
        "description": (
            "The Place fades and the team is standing on the parapet of a great castle suspended in "
            "the air hundreds of feet above the ground. A rolling green countryside spreads out below "
            "like a quilt, cut through by a mighty winding river with white-sailed ships on it and a "
            "city of graceful white spires in the distance; the sky is vivid blue with scattered white "
            "streamers of cloud and the sun is sinking toward mountains in the west. Great archways "
            "pierce the wall behind, opening into a vast chamber with a vaulted ceiling on tall fluted "
            "columns. The dome overhead is deep dark blue, set with gold and gemstones sparkling in the "
            "shapes of the constellations; the floor is inlaid with cut stone of different colours "
            "making a map of a strange land that is probably the one outside the walls. In the middle "
            "of the room a carved stone pillar about a metre tall holds nothing -- a beautiful red "
            "gemstone the size of a troll's head hangs above it in the air, rotating slowly on its "
            "vertical axis, its deep crimson facets throwing reddish spots across the ceiling and floor "
            "as it glows with a fiery inner light."
        ),
        "notes": (
            "The gemstone is the magical essence of the Jewel of Memory that Lofwyr physically holds -- "
            "the accumulated knowledge of the Ages of dragonkind. The moment any character deliberately "
            "lifts it from its pedestal, everyone present is whisked back to the material world and "
            "into Endgame. Lofwyr enters through an archway with a sound like metal brushing metal, "
            "scales burnished gold and brass darkening toward his back and paling toward his belly, "
            "eyes like pools of red fire matching the gem, smoke trickling from his nostrils, and coils "
            "around the pillar. He cannot stop the runners taking it and cannot harm them unless they "
            "attack first; he is there to make an offer. Optional: guardians (spirits, dracoforms, "
            "critters) waiting at the Citadel who vanish once beaten, or a rival team of Lofwyr's own "
            "agents racing the runners through the Places and waiting here if any survive."
        ),
    },
    {
        "name": "The Council Plateau",
        "location_type": "landmark / monument",
        "city": "An isolated mountain range",
        "summary": "The isolated plateau among snow-capped peaks where the great dragons gather in spirit -- once to declare the Rite of Succession and once to end it",
        "description": (
            "An isolated plateau high in the mountains, ringed by snow-capped peaks under a clear night "
            "sky, reachable by great dragons flying on the winds of the spirit world while their "
            "material bodies sleep half a world away. Hestaby comes to the first gathering slowly, to "
            "give herself time to consider and prepare, and circles once for formality's sake before "
            "gliding down to take her place among her brethren; Hualpa lies coiled by a rocky outcrop "
            "with his head-plumes spread, Lung and Ryumyo take opposite quarters of the circle and "
            "glower at each other throughout, and Lofwyr lands last and most deliberately of all. At "
            "the end of the campaign the runners' own astral forms arrive here to stand in the middle "
            "of a circle of about a dozen great dragons -- eastern, western and feathered serpents -- "
            "each of them, and the runners themselves, glowing with an aura of multicoloured light."
        ),
        "notes": (
            "The prologue (pp.5-8) and Endgame (p.120) are the same place. Radar systems, sensors and "
            "spy satellites watch these mountains and none of them can see a dragon travelling in "
            "spirit; the nation that claims the land is never named. Protocol at the second gathering: "
            "the dragons bow one by one until only Ghostwalker, Alamais, Hestaby and Lofwyr are "
            "upright, then Alamais lowers his head almost sheepishly and Ghostwalker follows with an "
            "unreadable expression; Hestaby bows and Lofwyr rises, and then Hestaby rises too and draws "
            "the runners into the centre. 'Orange Queen. Why have you brought these outsiders to our "
            "Council?' -- 'It is my right, and they are instrumental in settling this matter once and "
            "for all.' Agents addressing the Council is highly unusual and the dragons permit it out "
            "of curiosity."
        ),
        "controlling_org": "Council of Dragons",
    },
]

NPCS = [
    {
        "name": "Hestaby",
        "role": "The great dragon of Mount Shasta and the campaign's hidden employer -- the runners are her proxies in the Rite of Succession from the first job to the last",
        "archetype": "Great Dragon",
        "title": "Orange Queen; great western dragon of Mount Shasta; member of the Council of Princes of Tir Tairngire",
        "gender": "Female",
        "organization": "Council of Dragons",
        "connection": 6,
        "description": (
            "In dracoform she is a western dragon whose scales are the colour of amber and whose "
            "wingspan would dwarf a fighter jet, taking the air off the lodge roof with long slow "
            "beats that throw up a mist of snow. In human form -- how she chooses to meet the runners, "
            "to put them at ease -- she is a striking, clearly tall woman with long auburn hair "
            "framing a beautiful, almost elven face, in a bulky grey sweater and blue jeans with her "
            "feet bare, reading an actual dead-tree book; her eyes are a deep honey-amber that matches "
            "the golden undertones in her skin and hair. She plays her cards as close as Dunkelzahn "
            "did and deflects what she will not answer with 'You're better off not knowing that.' "
            "Her third face is 'Abby Nightbird', a shaman in mixed native and modern garb, features "
            "predominantly Hispanic, dark hair tied at the nape."
        ),
        "background": (
            "She has claimed Mount Shasta as lair and domain for many years and defended the "
            "surrounding land against anyone who came for it, including turning back an attempted Tir "
            "Tairngire invasion of northern California in 2053 -- which is why the Northern Crescent "
            "took her for its shield, and why her recent seat on the Tir's ruling Council of Princes "
            "reads to many of them as treason and has cost her supporters and split her own lodge. She "
            "is a progressive as dragons go: she genuinely likes and admires the young races, has "
            "watched them develop, was inspired by Dunkelzahn's willingness to defy custom, and has "
            "taken up his cause since his death. Dunkelzahn left her the encryption key to his private "
            "datastore on the Zurich Orbital Habitat. She did not want the Rite of Succession; she "
            "entered it to keep the dragons' conflict from wrecking what she has been building, to "
            "take the measure of her rivals and possible allies, and because someone has to win it who "
            "will hand the prize back."
        ),
        "notes": (
            "No game statistics, like every great dragon in this book. As 'Abby Nightbird' her aura "
            "masking is beyond any player character to penetrate -- assensing shows a normal human "
            "shaman of modest ability; taken hostage she permits it and leaves whenever she likes; "
            "attacked, her defences hold and she may fake an injury or a death. She heals injured "
            "runners with a touch at the Lore briefing. Her four moves in the Rite: fake the theft of a "
            "worthless file (Knowledge), burn Goldwing through Ghostwalker's temper to plant Morningstar "
            "closer to him (Cunning), return Hualpa's scrolls in person to score in his own house "
            "(Elements), rebalance the Pacific dragon lines through Buttercup (Balance), steal the "
            "Songbird from Rhonabwy while Celedyr takes the blame (Hunting), and take the Shroud out of "
            "Aden's reach either way (Rest). She loses esteem for runners who kill unnecessarily and it "
            "shows in her treatment of them at the Endgame. Legwork TN 6 (p.32). Ending: she hands the "
            "Jewel straight back to Lofwyr, refuses the Loremaster's title, rules that Dunkelzahn's "
            "dispersal stands, and later proposes not rivalry but friendship to Lofwyr's face."
        ),
        "contact_skills": ["Draconic politics and the rites of the Council of Dragons", "Northern California, the Shasta Enclave and Tir Tairngire's Council of Princes", "Half a million nuyen a head and personal gratitude"],
    },
    {
        "name": "Ghostwalker",
        "role": "Doll-Maker, the great dragon who woke into a changed world, seized Denver and forced the Rite of Succession; eats the runners' Denver employer in front of them",
        "archetype": "Great Dragon",
        "title": "Doll-Maker; great western dragon; master of the Denver Front Range Free Zone",
        "gender": "Male",
        "organization": "Council of Dragons",
        "connection": 6,
        "description": (
            "The largest male at the Council after Lofwyr, his bleached scales gleaming in the pale "
            "mountain sunlight, gravely accepting the Rite of Honored Greeting and visibly prepared for "
            "a fight even while his manner stays calm and controlled. At the Denver warehouse he "
            "appears first in human form: tall and thin, dressed all in white from head to toe, hair "
            "almost pure white and slicked straight back from a high forehead. Then his neck elongates, "
            "wings sprout, and he swells to tremendous size in scales the colour of old ivory, a "
            "reptilian head looking down from near the ceiling. 'HOLD!' -- a single word that rings in "
            "the minds of a dozen great dragons and echoes off the mountains."
        ),
        "background": (
            "A peer of Dunkelzahn, and only recently returned from a long sojourn in the depths of the "
            "higher astral planes while his body lay in a deep and dreamless sleep near modern Denver. "
            "His spirit came back out of the astral rift Dunkelzahn's death left in the Federal "
            "District of Columbia in the last days of 2061; he immediately laid claim to his old "
            "domain, assaulted the Aztlan sector of Denver, destroyed the teocalli there and made it "
            "abundantly clear that Aztlan would be removed and everyone else would acknowledge him. "
            "Then he learned what had become of the Loremaster's hoard, was outraged at the violation "
            "of draconic tradition and at the cowardice that let it stand, and called the Council. He "
            "was clearly close to Dunkelzahn once and considers himself the rightful heir to his "
            "position; his alliance with the Nexus data haven and his open-door petitioning policy show "
            "he is learning the new Age fast."
        ),
        "notes": (
            "No game statistics -- he recently levelled a good portion of a city sector and fought off "
            "armed attack craft; attacking him is suicide and he will kill anyone who tries, possibly "
            "leaving one alive to tell other would-be dragon-slayers. He has a short temper and fits of "
            "pique, and he is not pleased by this new Age. He accepts the Children of the Dragon's "
            "worship as his due but has no interest in worshippers who know nothing of his true nature, "
            "dislikes the cult's name for its hubris and for reminding him of other things, and has "
            "kept Morningstar cooling his heels without an audience -- an oversight this adventure "
            "turns into a problem. At the warehouse he questions the runners, knows when they lie, "
            "weighs their honest opinion of Morningstar's guilt, pronounces Morningstar sincere, has "
            "Goldwing pay them and then eats Goldwing for wasting his time. If Morningstar died first, "
            "Goldwing lives and becomes his chosen prophet instead. Legwork TN 4 (p.46). At the "
            "Endgame he is one of the last four standing; if the runners give him the essence he claims "
            "the title at once, lays claim to every item Dunkelzahn willed away to other dragons, and "
            "concedes that the modern world requires adaptation -- but not the casual discarding of "
            "everything old."
        ),
    },
    {
        "name": "Hualpa",
        "role": "The great feathered serpent who founded Amazonia; the Elemental Scrolls are his, and Hestaby scores against him by returning them to his own doorstep",
        "archetype": "Great Dragon",
        "title": "Great feathered serpent; founder and power behind the Awakened nation of Amazonia",
        "gender": "Male",
        "organization": "Council of Dragons",
        "connection": 6,
        "description": (
            "At the Council he lies coiled by a rocky outcropping with his brightly feathered wings "
            "folded close against his body and his head-plumes spread in an impressive display, and "
            "speaks quietly and before Ghostwalker can, which is its own statement. He is something of "
            "an enigma even by dragon standards. When he rises to back the Rite he spreads his brightly "
            "coloured wings, and Mujaji follows him a moment later."
        ),
        "background": (
            "Perhaps the most prominent feathered serpent in the world, he led a coalition of Awakened "
            "forces -- several other dragons among them, including Sirrurg -- that overthrew the "
            "government of Brazil and established Amazonia. He was not the first dragon to attack a "
            "sovereign nation but he was the first to make a go of founding one, and Amazonia is "
            "recognised by most of the world as a legitimate nation, a bastion of Awakened rights and "
            "progressive ecology preserving one of the most vital ecosystems on Earth. He is "
            "peace-loving at heart but will do what the future of the world requires; wary of "
            "technology for the damage it does, he considers magic superior and more natural and holds "
            "that technology is only useful under careful control and in harmony with nature -- a "
            "philosophy that costs Amazonia the full use of modern tools. His great concern is Aztlan, "
            "the embodiment of everything he fears, and the recent Yucatan War with its lasting "
            "physical and magical damage; he wants Aztlan and Aztechnology out of power so the harm can "
            "be healed."
        ),
        "notes": (
            "No game statistics and no on-screen appearance: he sends a feathered serpent to the "
            "village to collect the scrolls, which lands by the main hut, greets the old shaman, "
            "gravely thanks the runners for returning the Elemental Scrolls to Amazonia and tells them "
            "they have the nation's thanks, invites them to stay or go, and answers no questions about "
            "the scrolls. If the team impressed him he may hire them to root out Ocelopan's remaining "
            "confederates in Macapa, and he can provide safe passage out of the interior. He cares "
            "little for the Rite except as it serves his cause: greater respect from his peers would "
            "let him pull more of them away from the power games of Lofwyr, Lung and Ryumyo. He backed "
            "the Rite at the Council partly because the fate of his own bequest was already in doubt, "
            "which meant he had little to lose and much to gain."
        ),
    },
    {
        "name": "Lung",
        "role": "The great eastern dragon of T'ai Shan, locked in an ages-old proxy war with Ryumyo; the Red Dragon Triad answers to him and the Balance ritual drags his attention onto the runners",
        "archetype": "Great Dragon",
        "title": "Great eastern dragon; lord of T'ai Shan in central China",
        "gender": "Male",
        "organization": "Council of Dragons",
        "connection": 6,
        "description": (
            "A sinuous eastern dragon whose iridescent scales glimmer as he moves and whose tail lashes "
            "slowly back and forth in barely restrained agitation. He and Ryumyo arrive together, take "
            "up places on opposite sides of the Council circle and remain coolly formal as custom "
            "demands while glowering at each other the entire time. When the dragon lines shift he "
            "appears to the runners in the Skytower vision as a vast serpentine form towering over "
            "them, coils stretching around them, orbiting in the opposite direction to his rival. 'How "
            "have you done this?'"
        ),
        "background": (
            "China has been the focus of his attention since his awakening in the modern world; before "
            "he established a lair atop the sacred mountain T'ai Shan he operated in the shadows of the "
            "warring Chinese nations, influencing local warlords and the Triads. He and Ryumyo have "
            "fought a proxy war since the dawn of the Sixth World and for some time before that in a "
            "previous Age, and both have recently moved to positions of greater prominence in Asia as "
            "the conflict escalates. One of the prizes they struggle over is control of the dragon "
            "lines and power sites of Asia and the Pacific Rim, some of the greatest untapped magical "
            "power in the world -- rich enough to draw the other great dragons in if either of them "
            "gets close to winning it. Wuxing's Skytower has been disrupting both their plans for years."
        ),
        "notes": (
            "No game statistics. His main interest in the Rite is making sure Ryumyo does not win; he "
            "would take the Loremaster's title happily enough but is too wrapped up in the feud to work "
            "for it. Dunkelzahn left him the Second Coin of Luck 'in hopes that he might benefit from "
            "the long view as I have'; he is said to hold two of the four Coins of Luck (one is "
            "Wuxing's, one is unaccounted for). The Red Dragon Triad of Hong Kong is well named -- word "
            "has it they ultimately answer to Lung on the mainland, though nobody knows what a great "
            "dragon wants with a syndicate. Pushing the Envelope options put Triad hitters with ties to "
            "Lung in the Imperial Jade, and put Lung himself in the Skytower penthouse in astral form "
            "ordering the runners to stop interfering with something they do not understand -- he is "
            "reluctant to break the ward, which would alert Wuxing, and can do little to them astrally."
        ),
    },
    {
        "name": "Ryumyo",
        "role": "The first dragon seen in the modern age, Lung's rival, shadow-power in Japan; the other half of the vision at the Skytower and a real contender for the Loremaster's title",
        "archetype": "Great Dragon",
        "title": "Great eastern dragon; shadow-power of the Japanese Empire; lair unknown, presumed Japan",
        "gender": "Male",
        "organization": "Council of Dragons",
        "connection": 6,
        "description": (
            "As mysterious as Lung and seen in public only a handful of times, and hardly at all in "
            "recent years. At the Council his iridescent scales glimmer and his tail lashes in the same "
            "restrained agitation as his rival's across the circle. In the Skytower vision he is the "
            "second vast serpent circling the runners from the opposite side, wary and unsurprised: "
            "'It is not my doing. I could ask you the same.' The two of them finish in unison -- 'We "
            "will see' -- and split off in opposite directions."
        ),
        "background": (
            "His power base is Japan, where he originally held considerable influence with the Yakuza "
            "and through them with several Japanese megacorporations, pulling strings from behind the "
            "scenes to suit his schemes. The recent disasters in Japan have forced him to take a more "
            "active hand, and it is widely suspected that he has ties to the young Emperor and is "
            "steering the Empire; the truth is that his influence is not as great as people think, and "
            "the free spirit Buttercup and Yamatetsu have caused him real trouble. He continues to "
            "consolidate through the Yakuza and other agents in the shadows. Dunkelzahn willed him "
            "'my envy at stealing my chance to be the very first dragon' along with the Ring "
            "Ouroboros, since it is the early bird who catches the wyrm."
        ),
        "notes": (
            "No game statistics. Unlike Lung, he is genuinely interested in the Rite for its own sake "
            "-- he believes the title and position could serve his plans and has diverted resources "
            "toward it, though his attention is stretched thin by everything else happening in the "
            "Empire and its territories. Hestaby suspects the natural disasters that struck Japan may "
            "be connected to the continued drain the Wuxing Skytower has been putting on the dragon "
            "lines, which is one of her reasons for the Balance operation. Handing him the essence of "
            "the Jewel at the Endgame is one of the choices the other dragons will not accept: the Rite "
            "is either declared invalid and begun again, or awarded to the runner-up, who is Lofwyr."
        ),
    },
    {
        "name": "Rhonabwy",
        "role": "The Welsh dragon whose Silver Songbird the runners steal; barred from harming another dragon's agents, he sets his hunters on them instead and calls it a game",
        "archetype": "Great Dragon",
        "title": "Great western dragon of Llandovery, Wales; shadow-investor, collector and patron of the arts",
        "gender": "Male",
        "organization": "Council of Dragons",
        "connection": 6,
        "description": (
            "He waits in his own treasury disguised as a statue of a rearing dragon almost three metres "
            "tall with scales of burnished red gold, and when he lets it go he swells to many times "
            "that size, head reaching toward the ceiling and wings spreading toward the walls, scales "
            "deepening to blood red, fiery light coming up in his eyes, filling the middle of the "
            "chamber with his bulk. His manner is unhurried and gracious to the point of mockery: "
            "'Magnificent, isn't it?', 'Welcome to my home. Would you be so good as to tell me who you "
            "are and why it is you are here?', and at the end something akin to a smirk on his "
            "reptilian face -- 'I hope that you prove challenging prey for them; they're getting sorely "
            "out of practice.'"
        ),
        "background": (
            "He claimed a region of Wales shortly after his awakening and plays the corporate game as "
            "well as Lofwyr does, but differently: rather than buying a megacorporation outright he is "
            "a shadow-investor with shares in numerous corporations and business interests -- never "
            "enough for outright control of a top-tier corp, more than enough for insight into the "
            "operations and dealings of most of them, and a tremendous amount of wealth from shrewd "
            "investment. He and Lofwyr politely dance around each other in corporate circles, rarely "
            "getting close enough to require a response but always testing. He is a collector with a "
            "vast hoard and fancies himself a connoisseur and patron of the arts, with priceless "
            "treasures from around the world, some predating any known human civilisation; music is his "
            "particular love and he supports education and performance, though his tastes run to folk, "
            "classical and opera rather than nova-rock. Legend gives him a rival sea dragon in Cardigan "
            "Bay and ties to the Arthurian legends; he neither confirms nor denies either, and neither "
            "appears in this campaign."
        ),
        "notes": (
            "No game statistics; attacks bounce off his hide or are deflected by magical defences that "
            "operate automatically, and persistent attackers get turned into stone or a toad until he "
            "has made his point. He is very difficult to lie to and already has a fair idea who the "
            "runners are, because Hestaby tipped him off. The rules of the Rite forbid him from harming "
            "another dragon's agents, which is precisely why he offers a hunt instead -- Hestaby was "
            "counting on his penchant for games. Terms: take the Songbird, five minutes' head start, "
            "escape his hunters alone and without outside aid and it is theirs; spirits are forbidden "
            "to both sides, and any spirit a runner summons is attacked by his guardians one Combat "
            "Turn after it reaches the astral. He keeps his word if they win -- and has hidden a kilo "
            "of C-12 in the cage as retribution in case they do. He may be impressed enough to hire "
            "them later."
        ),
    },
    {
        "name": "Celedyr",
        "role": "Stone-Diver, the other Welsh dragon and Transys Neuronet's patron; hires the runners for the Songbird job and takes the fall for Hestaby when it succeeds",
        "archetype": "Great Dragon",
        "title": "Stone-Diver; great western dragon of Caerleon, Wales; patron and partner of Transys Neuronet",
        "gender": "Male",
        "organization": "Council of Dragons",
        "connection": 6,
        "description": (
            "He meets the runners in human form and calls himself Mr. Johnson: a tall, fair-skinned man "
            "with brassy-coloured hair in a long belted robe and a pair of sandals, standing on the "
            "sand of a ruined amphitheatre fifty metres underground, gesturing to a conference table "
            "and a flatscreen deck. 'Welcome. Please be seated and we can talk business.' He is a canny "
            "negotiator and not used to being questioned. At the Council he sits back on his haunches "
            "and folds his wings to declare the matter settled, and he is the one who speaks up for "
            "Lofwyr's claim when nobody expected any of the others to involve themselves: 'Far-Scholar "
            "clearly chose quite deliberately to give the Jewel to Gold-Master, for reasons he did not "
            "see fit to reveal to us. Do you, of all of us, question his judgment?'"
        ),
        "background": (
            "He lairs at Caerleon in southeastern Wales, under an ancient Roman amphitheatre and the "
            "high-tech complex Transys Neuronet built on top of it. Communication, and language in "
            "particular, fascinates him, which makes him a natural ally for a telecommunications "
            "megacorp; Transys has given him millions of nuyen of equipment and researchers in exchange "
            "for his support and his occasional insights into their projects. He has a kinder attitude "
            "toward the young races than Rhonabwy does and is still perfectly ruthless about his own "
            "interests. He and Rhonabwy have kept up a friendly rivalry for a long time with no open "
            "hostilities -- at least, not yet, which is exactly the crack Hestaby puts a wedge into. "
            "Hestaby arranged for the runners and for the intelligence on Rhonabwy's lair to reach him."
        ),
        "notes": (
            "No game statistics. He pays 150,000 nuyen each or up to twice that in Transys hardware and "
            "cyberware, gold, gems, orichalcum, script, or spells and foci for magicians, with free "
            "installation and any reasonable mundane gear thrown in -- but no advance, no scouting of "
            "the target, and at most a week to prepare, partly because of rules of the Rite he does not "
            "explain. Runners who decline are held as guests by the Knights of Rage until another team "
            "has run the job. When he eventually discovers his Songbird is a replica he assumes "
            "Rhonabwy duped the runners and chalks it up as another move in the Rite, which is exactly "
            "what Hestaby wants -- she gets the Songbird, the win over Rhonabwy, and the deception of "
            "both Welsh dragons, and if the runners fail she loses only their services and Celedyr "
            "takes the blame. Handing him the Jewel's essence at the Endgame is treated as a surprising "
            "but acceptable compromise."
        ),
    },
    {
        "name": "Aden",
        "role": "The sirrush who destroyed Tehran; the Shroud of Shadows is his by Dunkelzahn's will and he refuses to claim it, so he demands the runners put it back themselves",
        "archetype": "Great Dragon",
        "title": "Great sirrush of Mt. Ararat, Turkey; destroyer of Tehran",
        "gender": "Male",
        "organization": "Council of Dragons",
        "connection": 6,
        "description": (
            "A body at least fifteen metres long, not counting an almost equal length of tail trailing "
            "out behind hind legs tipped with powerful curving claws like scimitars; wickedly pointed "
            "fangs jut from his mouth and his eyes are like saucers. He banks out of a dark sky, "
            "bending sinuously, coiling in on himself like a snake preparing to strike, and comes to "
            "the ground with surprising speed and grace for something of his size, coils moving to "
            "surround the runners. 'I am Aden. You have taken something that once belonged to another "
            "of my kind. You will return it, or you will die.' At the Council he snorts faintly: 'I "
            "care not for this matter. As Stone-Diver says, let it be finished.'"
        ),
        "background": (
            "A sirrush, a variety of eastern dragon found in the Middle East and Asia Minor. He is best "
            "known for systematically destroying Tehran after its ruling ayatollah declared a jihad "
            "against the Awakened -- Iranian military might proved no match for him, the city was "
            "evacuated and largely abandoned, and he retreated to his lair high atop Mt. Ararat in "
            "neighbouring Turkey and has been seen only rarely since; the locals give him a wide berth "
            "rather than risk angering him again. He has little interest in metahumanity provided the "
            "young races show proper deference to their betters, and no compunction about another "
            "object lesson if they do not. Something of a contemplative, he prefers the solitude of his "
            "lair. He is a traditionalist: he did not agree with Dunkelzahn's means of distributing his "
            "hoard, and registered his disapproval by refusing the bequest -- and entertains the "
            "thought that he would make a good Loremaster himself."
        ),
        "notes": (
            "No game statistics. His bind: he does not consider the Shroud his because he did not win "
            "it, and it still belongs to Dunkelzahn until a dragon claims it properly. Letting thieves "
            "walk off with it costs him face; taking it from them himself claims it. So he wants the "
            "runners to put it back where they found it, keeping himself uninvolved. He warded the "
            "resting place to warn him of tampering. He is also bluffing: the Rite forbids him to "
            "attack the runners unless they attack him first, though he may kill anyone who does, and "
            "he can obstruct and trap them (a physical barrier is fair, a Stunball or Control Thoughts "
            "is not). He is reluctant to kill the last runner, since somebody has to carry the Shroud "
            "back. Perception (4) notices that his demand is odd and that he did not simply kill them. "
            "He is also, quietly, afraid of the Shroud and of what owning it would oblige. He will "
            "negotiate -- nuyen or treasures from his hoard, payable after -- and anyone who drapes the "
            "Shroud over him finds even a great dragon's anger draining away. Karma: 1 for getting the "
            "Shroud, 2 for getting Aden to claim it."
        ),
    },
    {
        "name": "Alamais",
        "role": "Lofwyr's brother, jealous and traditionalist; backs the Rite at once and spends the campaign arranging to steal the physical Jewel of Memory that Lofwyr all but hands him",
        "archetype": "Great Dragon",
        "title": "Great western dragon; brother of Lofwyr; patron of radical policlubs and terrorist groups",
        "gender": "Male",
        "organization": "Council of Dragons",
        "connection": 5,
        "description": (
            "Hestaby ignores him at the Council as best she can, wanting as little to do with him as "
            "possible, and is mildly surprised he came at all after his recent dealings with his "
            "brother -- but Alamais was never one to miss an opportunity to further his own cause. He "
            "rises into the Posture of Defiance the moment Ghostwalker does, glaring across the circle: "
            "'Not all of us have been willing to permit this.' Lofwyr answers by baring his teeth in a "
            "sneer and saying 'Remember Nachtmeister', and Alamais flinches, only slightly, in "
            "recollection of those fangs at his neck. At the Endgame he is one of the last four "
            "standing and then lowers his head almost sheepishly."
        ),
        "background": (
            "A great western dragon and Lofwyr's brother, who has not adapted to the modern world "
            "nearly as well and remains jealous of his brother's success. He despises Lofwyr's "
            "corporate wheeling and dealing as weak and unbefitting a great dragon, and works instead "
            "through radical policlubs and terrorist groups to keep the nations of Europe divided where "
            "Lofwyr would unite them under Saeder-Krupp's logo. His struggles against Lofwyr and his "
            "subsequent failures are well known. During the Rite he arranges the theft of the Jewel of "
            "Memory itself from Saeder-Krupp -- and Lofwyr, who knew what Hestaby was planning for the "
            "essence, all but let him have it."
        ),
        "notes": (
            "No game statistics and no scenes except the two Council gatherings. The Two-Pronged Attack "
            "option (p.108) makes him usable: Hestaby sends a second team into Saeder-Krupp "
            "headquarters in the German Alliance for the physical Jewel, where they may run into "
            "Alamais's people going after the same stone. Handing him the essence at the Endgame is one "
            "of the choices the other dragons reject outright, voiding the Rite or awarding it to "
            "Lofwyr as runner-up."
        ),
    },
    {
        "name": "Mujaji",
        "role": "The Rain Queen of Africa, a great feathered serpent who keeps to her own affairs and backs the Rite to shore up her position",
        "archetype": "Great Dragon",
        "title": "Rain Queen; great feathered serpent with a lair near the Cape of Good Hope",
        "gender": "Female",
        "organization": "Council of Dragons",
        "connection": 5,
        "description": (
            "One of only three females Hestaby expects at the Council, and one of the three feathered "
            "serpents there; she keeps close to Hualpa and Arleesh, as feathered serpents tend to "
            "congregate with their own kind. She is the one who raises the practical objection: 'The "
            "Rite of Succession is impractical, at best. Even if we are willing to submit our gains "
            "from Far-Scholar's death to the judgment of the Rite, what of the rest of his hoard? It "
            "has been scattered to the winds.' When Hualpa answers her and rises, she rises after him."
        ),
        "background": (
            "The Rain Queen of Africa lairs near the Cape of Good Hope and tends to keep to her own "
            "affairs -- markedly less active in mortal politics than Arleesh. Hestaby reads her support "
            "for the Rite as her own business, but suspects a desire to shore up her position in the "
            "face of events in Africa and perhaps to curry a little favour with Hualpa and his domain "
            "in Amazonia."
        ),
        "notes": (
            "No game statistics; present only at the two Council gatherings. Useful as a name for a "
            "great dragon who is neither an ally nor an enemy and who might be added to the campaign as "
            "a client for one of the extra adventures the book invites gamemasters to insert."
        ),
    },
    {
        "name": "Sirrurg",
        "role": "The Destroyer -- a draconic terrorist absent from the Council and from the Rite unless the gamemaster wants him",
        "archetype": "Great Dragon",
        "title": "The Destroyer; great dragon; last seen in the coalition that overthrew Brazil",
        "gender": "Male",
        "organization": "Council of Dragons",
        "connection": 4,
        "description": (
            "Absent from the Council and unsurprisingly so. Hestaby suspects Hualpa knows where the one "
            "called the Destroyer is, as the last of their kind to have real dealings with him, but "
            "she will not ask -- it would be improper. If Sirrurg wishes to cut himself off from his "
            "own kind, that is his business."
        ),
        "background": (
            "Something of a draconic terrorist: a great dragon who has supported Awakened causes by "
            "striking at government and even civilian targets. He was last seen publicly as part of the "
            "coalition that overthrew the Brazilian government and established Amazonia, and has not "
            "been seen since."
        ),
        "notes": (
            "No game statistics and no role in Survival of the Fittest unless the gamemaster wants one. "
            "Listed with Schwartzkopf and Kaltenstein among the noted absences from the Council -- "
            "Hestaby wonders whether the missing are too wrapped up in their own affairs or whether "
            "some of the elder ones are simply gone now."
        ),
    },
    {
        "name": "Nachtmeister",
        "role": "The upstart who challenged Lofwyr's claim to the Jewel of Memory and paid for it -- the object lesson Lofwyr throws in Alamais's face at the Council",
        "archetype": "Great Dragon",
        "title": "Great dragon; challenger to Lofwyr's claim as Loremaster",
        "gender": "Male",
        "connection": 3,
        "description": (
            "Not present, and not alive to be. His name is a single word Lofwyr uses as a weapon at the "
            "Council -- 'Yes, but those who object have been show the error of their ways. Remember "
            "Nachtmeister' -- delivered with bared teeth to a brother who flinches at the memory of "
            "those fangs at his own neck."
        ),
        "background": (
            "When the Draco Foundation put the Jewel of Memory into Lofwyr's hands, most of the great "
            "dragons did not care to challenge his possession of it because they were not certain they "
            "could take it from him. A few upstarts, Nachtmeister among them, did challenge -- and paid "
            "the ultimate price for their defiance, which discouraged further challenges until "
            "Ghostwalker returned with enough weight behind him to demand a Rite instead of a duel."
        ),
        "notes": (
            "A name-drop with a role, built as a row because his fate is the reason the Rite of "
            "Succession happens through proxies rather than teeth: the last dragon to object directly "
            "is dead, and every dragon at the plateau knows it. No statistics, no scenes."
        ),
    },
    {
        "name": "Mr. Radek",
        "role": "The fixer who hires the runners for most of the campaign on Hestaby's behalf -- and who does not know for the first several jobs who he is really working for",
        "archetype": "Fixer",
        "title": "Fixer and middle-man; the runners' primary contact throughout the Rite of Succession",
        "race": "Human",
        "gender": "Male",
        "connection": 4,
        "description": (
            "One hundred percent suit: good-looking in that bland corporate way and as at ease as he is "
            "out of place in a monster-movie club, sitting on a model 'building' with an untouched "
            "drink and a pocket secretary beside him. Slightly above average height with a trim build "
            "under designer-cut suits, apparently of Mediterranean heritage, completely bald or shaved, "
            "with a neat black beard and moustache. He frequently wears dark glasses even indoors, "
            "which hide intense brown eyes and double as a screen for the data displays he is "
            "constantly checking; a gold watch and a ring set with a red stone, which does not assense "
            "as magical. Quietly efficient, candid where he can be, and he lets his satisfied clients "
            "speak for him. 'Let's not keep our host waiting.'"
        ),
        "background": (
            "His manner and connections suggest previous corporate experience, perhaps with a megacorp, "
            "though he no longer works for any one employer; he is a middle-man who arranges 'special "
            "personnel' for clients who need them and prefers to reach those clients through other "
            "fixers and middle-men, which keeps things discreet. He has a solid street reputation and "
            "is considered decent to work for. He was contacted for the Kallisti job by a middleman who "
            "had in turn been contacted anonymously by an agent of Hestaby's, and for most of the "
            "campaign he genuinely does not know who is behind it -- which is why neither Mind Probe "
            "nor Analyze Truth gets anything out of him, and why the runners' contacts know nothing "
            "about the connection either."
        ),
        "notes": (
            "Stats p.124: Init 3+1D6, Combat Pool 6, KP/Prof 5/3, mundane with a modest amount of "
            "alphaware. Computer 3, Drive 2, Etiquette 5 (Corporate 6, Street 7), Interrogation 4, "
            "Intimidation 4, Negotiation 6, Pistols 3; Cityspeak 4, Data Havens 4, English 5, Fine Art "
            "3, Japanese 4, Shadowrunners 5. Datajack, display link, 200 Mp headware memory; armor "
            "clothing 2/0; Fichetti Security 500; pocket secretary with cell phone and display link. "
            "Negotiates in good faith with instructions to cultivate the team for future work: 60,000 "
            "nuyen for the Kallisti run rising to 200,000 all in, 1,000 a head just to hear the Denver "
            "pitch, 200,000 each for Tehran. Astral assensing shows a cool, collected professional with "
            "no ill will and no emotional stake. He rewards professionalism, forgives setbacks and has "
            "little tolerance for amateurs. He is on the pick-up after the Welsh hunt with the replica "
            "Songbird, pays in London after Tehran and puts the team on the plane to Mount Shasta, and "
            "pays out at the end with the warning to always be careful when dealing with dragons. The "
            "book explicitly leaves open that he may be more than a fixer -- a direct agent of Hestaby, "
            "or even a drake in human form. Legwork TN 4 (p.32)."
        ),
        "contact_skills": ["Discreet employers who will not give their names", "Freelance deckers and specialists on short notice", "Global travel and transport arrangements"],
    },
    {
        "name": "Martin Goldwing",
        "role": "Ambitious mage of the Children of the Dragon who hires the runners to destroy his own leader -- and is eaten in front of them for wasting Ghostwalker's time",
        "archetype": "Mage",
        "title": "Brother Goldwing of the Children of the Dragon; born Martin Bellecote",
        "race": "Human",
        "gender": "Male",
        "nationality": "UCAS",
        "organization": "Children of the Dragon (Denver Faction)",
        "connection": 3,
        "description": (
            "Taller-looking than he is standing beside a dwarf: thin build, thinning dark hair brushed "
            "back from a high forehead, a dark double-breasted suit and a designer tie he adjusts as he "
            "takes the room in with a glance, light gleaming on a gold ring set with a red stone on his "
            "right hand. He should project mystery and a little subtle menace without seeming to "
            "threaten the people he is hiring. He pauses to compose himself when he speaks about the "
            "betrayal, and the outrage is real even where the evidence is not. 'I'm not sure that you "
            "would understand, but I believed very deeply in Brother Morningstar's message. I still do "
            "in many ways, and so do all the people who matter to me. I have to know if he has betrayed "
            "us; if it was all for nothing.' At the warehouse he hangs back looking nervous, and hands "
            "over the credstick with a trembling hand."
        ),
        "background": (
            "Born and raised in the northeastern corridor of the UCAS, Martin Bellecote took a degree "
            "in thaumaturgy at Brown University and put it to work for Manadyne. A moderately agnostic "
            "neo-pagan, he performed well enough and started up the corporate ladder with something "
            "missing from his life; he was shocked along with the rest of the nation by Dunkelzahn's "
            "assassination and found the Children of the Dragon not long after David Dragonson founded "
            "the movement. He joined, took the spiritual name Goldwing, left the corporate job a few "
            "months later and rose through the hierarchy on his magical training -- but laboured under "
            "the prejudice against a mage among the church's shamans, which capped his advancement and "
            "frustrated him badly, because he knew he had so much to contribute. He followed "
            "Morningstar in the schism out of both genuine belief and calculation, advanced under him, "
            "and then let jealousy and ambition convince him that Morningstar was a traitor."
        ),
        "notes": (
            "Stats p.47: B2 Q3 S2 C5 I5 W6 E6 M9 R4, Init 4+1D6; Astral 3, Astral Combat 8, Combat 7, "
            "Spell 6; KP/Prof 4/3, Initiate Grade 3 (Centering (chanting), Masking, Shielding). Aura "
            "Reading 4, Car 1, Centering 4, Conjuring 5, Etiquette 3 (Corporate 5), Instruction 3, "
            "Leadership 3, Negotiation 3, Pistols 2, Sorcery 6 (Ritual 8); Chanting 4, Children of the "
            "Dragon 6, Dragons 3, History 3, Magic Background 5, Metaplanes 4, Shamanism 4. Spells: "
            "Analyze Truth 5, Clairvoyance 4, Detect Enemies 3, Entertainment 1, Fashion 1, "
            "Flamethrower 4, Magic Fingers 3, Mob Mood 4, Physical Barrier 5, Powerbolt 4, Stunbolt 5, "
            "Treat 3. Armor 4/1; Fichetti Security 500; dragon amulet (Detection Spell Focus 3), gold "
            "ring (Sustaining Focus 5, Analyze Truth, active through the meet), pocket secretary. He "
            "will supply the temple layout and access codes to everything but the highest security "
            "areas, which only Morningstar holds. He does not know the files have been altered. Runners "
            "who refuse the job or insult him too far get a hired ambush before they leave Denver, "
            "because they know too much. He petitioned Ghostwalker for an audience confident the run "
            "would succeed; Ghostwalker came out of curiosity about a possible double agent in his "
            "domain. Legwork p.45: TN 6 magical, TN 4 Denver -- 4+ successes give up the birth name."
        ),
    },
    {
        "name": "Sappho",
        "role": "Denver fixer who brokers the Morningstar job; smuggles anything into or out of the Free Zone and intends to come out ahead whichever way the cult's power struggle falls",
        "archetype": "Fixer",
        "title": "Fixer, CAS sector of the Denver Front Range Free Zone",
        "race": "Dwarf",
        "gender": "Female",
        "connection": 4,
        "description": (
            "A dwarf decked out in a stylish suit from some Euro-designer, hair styled and gelled "
            "within an inch of its life, a hard lined face that says this halfer does not take drek "
            "from anybody. She should ooze confidence and professionalism with a hard edge. She does "
            "the introductions and the numbers and leaves the pitch to her client: 'I'm Sappho. I "
            "believe that you're all well acquainted with Mr. Johnson, in one form or another. Let's "
            "get down to business, shall we?' Astral assensing shows a mundane with a modest amount of "
            "high-class, invisible headware, entirely professional and detached, a little greedy and "
            "otherwise uninvested."
        ),
        "background": (
            "She has been part of Denver's shadow community for over a decade and has not made a living "
            "in the shadows that long by being soft-hearted. Her reputation is for acquisition -- "
            "finding and getting hold of nearly any contraband a client wants and smuggling it into or "
            "out of the Free Zone -- and she brokers shadowruns less often, though the upheaval since "
            "Ghostwalker's arrival has given a businesswoman of her stature no shortage of opportunities "
            "and she has been expanding. She has provided services for Martin Goldwing before, which is "
            "why he came to her. Mr. Radek or another of the runners' fixer contacts recommended them to "
            "her. She knows little about the politics inside the Children of the Dragon and nothing "
            "about the conflict between the great dragons."
        ),
        "notes": (
            "Stats p.47: B3 Q2 S2 C4 I5 W5 E3.8 M0 R3, Init 3+1D6, Combat Pool 6, KP/Prof 8/3. Car 3, "
            "Computer 3, Electronics 3, Etiquette 5 (Street 7), Negotiation 7, Pistols 3; Denver "
            "Politics 6, Denver Shadows 5, Evaluate Items 6, Organized Crime 5, Smuggling Routes 5, "
            "Vices 6. Chipjack, cybereyes, datajack, 300 Mp headware memory, knowsoft link, telephone; "
            "secure clothing 3/0; Ares Viper Slivergun with integral silencer; assorted knowledge and "
            "language chips at Rating 3-5. She is on hand to broker the deal and nothing more, and "
            "wants influence with the Children of the Dragon either way -- gratitude from Goldwing, or "
            "dirt on Morningstar. She will go 15 percent above the offer and no further; greedy runners "
            "get their 1,000 nuyen appearance fee and a polite goodbye. Cross her and she is an enemy; "
            "do not and she is a standing resource in Denver, particularly for smuggling work."
        ),
        "contact_skills": ["Contraband and rare acquisitions in the Front Range Free Zone", "Smuggling routes across the Denver sector walls", "Denver politics, shadows and organised crime"],
    },
    {
        "name": "Joshua Morningstar",
        "role": "Prophet of the Denver Children of the Dragon and the runners' extraction target -- a genuine visionary who is also, without knowing it, Hestaby's conditioned sleeper agent",
        "archetype": "Shaman",
        "title": "Brother Morningstar, leader of the Denver faction of the Children of the Dragon; born Joshua Keller",
        "race": "Human",
        "gender": "Male",
        "nationality": "CAS",
        "organization": "Children of the Dragon (Denver Faction)",
        "connection": 3,
        "description": (
            "A tall, imposing man with long dark hair and a neatly trimmed beard and moustache, in "
            "clerical robes when handling the public business of the church and casual business attire "
            "the rest of the time. He keeps in excellent physical shape and is quite capable of taking "
            "care of himself, as the runners may discover. He resists capture with everything he has, "
            "magic included, but he is no fool and surrenders against unfavourable odds, cooperating to "
            "stay alive without making anything easy and keeping the extent of his magical abilities "
            "back as an ace. Before Ghostwalker he beams with vindication: 'I have seen a vision of the "
            "future and, if humanity is to survive, we must all of us give ourselves over to the "
            "guidance of the Great Dragon Spirit, embodied in this world by the great dragon called "
            "Ghostwalker. He is our savior and our guide to a new age of peace and prosperity.'"
        ),
        "background": (
            "Joshua Keller was raised by a corporate family in the CAS and studied marketing and "
            "communications at the University of Virginia, where he also acquired liberal and even "
            "radical politics and got involved with TerraFirst! and various civil-rights causes. He was "
            "one of the many drawn to Dunkelzahn's message and campaigned for the dragon early in the "
            "'57 election, until he was dismissed for using violent methods against the campaign's "
            "opponents -- Kenneth Brackhaven in particular. He joined the Children of the Dragon "
            "shortly after its founding, took the name Morningstar, and rose fast through charisma, "
            "self-sacrifice and hard work until by 2060 he was in the church's upper echelons, David "
            "Dragonson's close friend, right hand and likely successor. Then Ghostwalker appeared, "
            "Morningstar collapsed at a board meeting and woke claiming a vision that the pale dragon "
            "was the Great Dragon Spirit reincarnate. Dragonson and the other leaders were sceptical; "
            "the church split; Morningstar's talent for direct and brutal confrontation carried several "
            "temples with him. He has been Awakened since the vision -- he was mundane when he joined."
        ),
        "notes": (
            "Stats p.48: B3 Q3 S3 C6 I4 W6 E6 M8 R3, Init 3+1D6; Astral 2, Astral Combat 8, Combat 6, "
            "Spell 6; KP/Prof 5/4; Totem Dragon (YOTC p.146), Initiate Grade 2 (Divining (dreaming), "
            "Shielding). Athletics 3, Car 1, Clubs 2, Computer 1, Conjuring 4, Divining 5, Etiquette 4 "
            "(Church 5), Interrogation 4, Intimidation 4, Leadership 4 (Speechmaking 6), Negotiation 5, "
            "Pistols 4, Sorcery 6, Unarmed 3; Children of the Dragon 6, Dragons 5, Dreaming 5, "
            "Environmental Groups 4, Magical Background 2, Politics 5, Radical Groups 4. Spells: Analyze "
            "Magic 2, Clout 4, Confusion 4, Dream 3, Flame Aura 4, Healthy Glow 2, Ignite 4, Increase "
            "Charisma 5, Mass Confusion 4, Resist Pain 4. Armor 4/1; Fichetti Security 500; dragon "
            "amulet (Sustaining Focus 5, Increase Charisma), pocket secretary. He is a traitor who does "
            "not know it: Hestaby conditioned him as a sleeper and planted the Saeder-Krupp evidence "
            "herself. Ghostwalker pronounces his claims of innocence true in his own mind, which is "
            "precisely correct and precisely useless. He petitions Ghostwalker constantly for an "
            "audience and treats the refusals as tests of faith. Killing him costs the runners the "
            "mission for Hestaby. Legwork TN 4 (p.45)."
        ),
    },
    {
        "name": "David Dragonson",
        "role": "Founder of the Children of the Dragon, who greeted Morningstar's vision with scepticism and lost several temples and his likely successor to the schism",
        "archetype": "Cult Leader",
        "title": "Founder of the Children of the Dragon",
        "race": "Human",
        "gender": "Male",
        "organization": "Children of the Dragon",
        "connection": 3,
        "description": (
            "Never staged. He is the figure at the centre of the church the runners' targets broke away "
            "from -- the man who drew Martin Bellecote in not long after Dunkelzahn's assassination, "
            "who took Joshua Morningstar as a fast friend and right hand, and who was in the room at "
            "the board meeting where Morningstar collapsed and woke up a prophet."
        ),
        "background": (
            "He founded the Children of the Dragon in the wake of Dunkelzahn's death and built it into "
            "something with a real measure of legitimacy -- charity work, soup kitchens, shelters -- "
            "and a hierarchy in which the Awakened held special status for being closer to the spirit "
            "world. By 2060 Morningstar was widely acknowledged as Dragonson's right hand and likely "
            "successor. When Morningstar came round from his collapse claiming that Ghostwalker was the "
            "Great Dragon Spirit made flesh, Dragonson was the leading sceptic, and the church split "
            "along the line his scepticism drew."
        ),
        "notes": (
            "No statistics and no scenes; named twice in the Cast of Shadows and Legwork. He matters as "
            "the pressure behind the Denver faction: the main church would be very happy to have the "
            "splinter folded back in, and Pushing the Envelope (p.41) offers radical elements of "
            "Dragonson's sect trying to kidnap or kill Morningstar at the same moment the runners do. "
            "Whether he authorises that is left open."
        ),
    },
    {
        "name": "Toshi Akimura",
        "role": "New Orleans fixer with old Dunkelzahn ties, now indirectly working for Hestaby; hands the runners the Elemental Scrolls and leaves an MCT hit team behind him",
        "archetype": "Fixer",
        "title": "Fixer, New Orleans",
        "race": "Human",
        "gender": "Male",
        "nationality": "CAS",
        "connection": 4,
        "description": (
            "He waits in the old lakeside warehouse with the crate and two bodyguards -- elven women "
            "who are either twin sisters or have been bio-sculpted to look identical, silent "
            "throughout, acting only to protect him or on his order. He explains nothing about what is "
            "in the box, provides the map chip and the certified credstick, and takes his leave through "
            "the back of the warehouse to his waiting car. He does not negotiate last-minute changes "
            "and he does not tolerate teams that look untrustworthy or unprofessional -- he will simply "
            "call the deal off and take the package away to find someone else, which will not stop "
            "Mitsuhama from attacking the runners anyway."
        ),
        "background": (
            "A well-known fixer in New Orleans who once had ties to Dunkelzahn (the adventure 'My Name "
            "Is Legion' from Brainscan, and Portfolio of a Dragon), and is now working -- indirectly "
            "-- for Hestaby. His only real stake in the operation is his reputation, which he means to "
            "protect. Teams that already know him from earlier work and are on cordial terms make the "
            "whole introduction simpler."
        ),
        "notes": (
            "No stat block; the two elven bodyguards use the Adept sample character (SR3 p.55). He can "
            "be swapped out for any other fixer NPC the campaign already has. If the MCT team proves "
            "too much, his bodyguards return to help, since he has an interest in the run going "
            "through; if the team has a rigger with Motorboat he can supply a boat instead of putting "
            "them on the Gulf Runner. Pay: 150,000 nuyen with 15,000 in advance. He knows what he needs "
            "to know and no more."
        ),
        "contact_skills": ["Contraband movement out of New Orleans and the Mississippi Delta", "Smugglers and captains working the Gulf and the Caribbean"],
    },
    {
        "name": "Cap'n Fixx",
        "role": "Ork smuggler captain of the Gulf Runner, paid to carry the runners and their crate to Amazonia and ask nothing -- with a traitor in his crew",
        "archetype": "Smuggler",
        "title": "Captain of the Gulf Runner",
        "race": "Ork",
        "gender": "Male",
        "connection": 3,
        "description": (
            "A rather mangy-looking ork whose cybereye is the first thing the team sees of him in the "
            "Mississippi Delta at night -- a tiny light in the darkness like the winking of a bright "
            "firefly, then a rangefinder playing briefly over them -- before he lowers his Ares "
            "Predator slightly. 'I'm Cap'n Fixx. Have you got the goods?' Gruff, direct, and entirely "
            "uninterested in what is in the crate. He gets the runners aboard by launch and puts to "
            "sea as fast as he can, especially if anyone mentions trouble in New Orleans."
        ),
        "background": (
            "He and his crew of a dozen smugglers have operated in the Gulf region for years and know "
            "the area extremely well; they have dodged patrol ships from Aztlan, the CAS and the Carib "
            "League as well as corporate vessels and lived to tell about it. Akimura is paying him to "
            "carry the runners and their cargo from the CAS to Amazonia with no questions asked, and "
            "that is exactly what he is going to do. He is also running his own contraband on the same "
            "trip -- cases of BTL chips and other electronic goods for the Amazonian market."
        ),
        "notes": (
            "No stat block. What he does not know is that one of his crew is on the take from a pirate "
            "band and has been feeding them information about his cargoes; this one interested them "
            "enough to make a move as the Gulf Runner clears the Yucatan Channel. His crew fights back "
            "but is no match for the pirates without the runners' help, particularly against the shark "
            "shaman. The crossing takes the better part of a week, which is plenty of time for the "
            "runners to mingle with the crew, form friendships or rivalries, and investigate the leak "
            "if the thought occurs to them."
        ),
        "contact_skills": ["Gulf and Caribbean smuggling routes", "Getting people and cargo into Amazonia without customs"],
    },
    {
        "name": "Grin",
        "role": "Shark shaman of the pirate band that boards the Gulf Runner; the one opponent in the crossing the crew cannot handle",
        "archetype": "Shaman",
        "title": "Shark shaman of a Caribbean pirate band",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": (
            "He rides one of the three GMC Riverines that come out of the dawn as the Gulf Runner "
            "leaves the Yucatan Channel, with a Force 5 sea spirit already on hand when the attack "
            "begins. He focuses his effort on countering any magicians aboard the ship, keeps his spell "
            "defence on himself and the boat he is riding, and leaves the rest of the band largely on "
            "their own. His totem lets him go berserk when wounded."
        ),
        "background": (
            "The band's magical muscle, operating in the Caribbean off information bought from crew "
            "members aboard the ships they hit -- in this case one of Fixx's own dozen. They want the "
            "runners' crate and the smuggled contraband in the hold, they would rather not sink the "
            "ship, and they have no objection to killing everyone aboard if it comes to that."
        ),
        "notes": (
            "Stats p.54: B3 Q4 S4 I3 W6 E6 M6, Init 3+1D6, Combat Pool 6, Spell Pool 5, KP/Prof 3/3 "
            "(Charisma garbled in the OCR). Athletics 2 (Swimming 4), Boats B/R 3, Conjuring 6, Diving "
            "3, Etiquette 3 (Pirate 4), Pistols 3, Motorboat 4, Sorcery 6, Unarmed 3. Totem Shark: +2 "
            "dice for combat and detection spells and sea spirits, may go berserk when wounded. Spells: "
            "Agony 4, Armor 5, Combat Sense 3, Confusion 5, Influence 4, Oxygenate 2, Power Bolt 4, "
            "Shape Water 4, Treat 3. Ceska Black Scorpion; armored jacket 5/3. Losing him is one of the "
            "three things that will make the pirates break off (the others being half their number or "
            "two of their three boats); if he can, he orders the sea spirit to cover the retreat. To "
            "harden the encounter, make him an initiate with Invoking and possibly Shielding and give "
            "him a great form sea spirit."
        ),
    },
    {
        "name": "Hilde",
        "role": "The elven guide who takes the runners two days up the Amazon; paid not to ask questions and privately delighted to be inconveniencing Aztechnology",
        "archetype": "Guide",
        "title": "Riverboat guide to the Amazonian interior (the only name she gives or answers to)",
        "race": "Elf",
        "gender": "Female",
        "connection": 3,
        "description": (
            "Latina colouring and attractive elven features, and a hardened, street-smart professional "
            "underneath them. She is found by asking around the small waterfront dives of Macapa, sizes "
            "the runners up, asks when they want to leave and goes along with whatever they say -- "
            "content to wait in the city if that is what they want, though she suggests getting "
            "underway as soon as possible. Her boat is a GMC Riverine and she knows how to navigate the "
            "river and avoid most of the obvious hazards, which does not make the trip a pleasure "
            "cruise."
        ),
        "background": (
            "She makes her living guiding people into parts of the Amazonian interior and has been "
            "hired to take the runners to their delivery point. Like Cap'n Fixx she has been paid not "
            "to ask questions and has no real interest in what the runners are doing. Years of "
            "experience have given her a strong dislike of Aztlan and Aztechnology, which is likely to "
            "make her considerably more sympathetic to the team once Ocelopan starts shooting."
        ),
        "notes": (
            "No stat block. She advises hard against flying to the destination -- Amazonia's defences "
            "against airborne intruders include air spirits, elementals and other paranormals in the "
            "service of the Awakened, and it is not unknown for a dragon to bring down an unwanted "
            "aircraft -- so the river is both lower-profile and what the employer wants. She can pull "
            "strings to get arrested runners out of a Macapan cell, though possibly not before Ocelopan "
            "or Miyamoto has claimed the scrolls. If the team has a rigger with Motorboat, reduce her "
            "to a contact who supplies the boat and the local knowledge and lets the rigger drive."
        ),
        "contact_skills": ["Navigating the Amazon and the Amazonian interior", "Macapa's waterfront and who is watching it"],
    },
    {
        "name": "Reynaldo Ocelopan",
        "role": "Aztechnology's undercover adept in Macapa, who tests the runners with hired street toughs and then hunts them up the river for whatever MCT wants so badly",
        "archetype": "Physical Adept",
        "title": "Aztechnology field agent, Macapa",
        "gender": "Male",
        "nationality": "Aztlan",
        "organization": "Aztechnology",
        "connection": 3,
        "description": (
            "One of the Aztechnology agents at work in Macapa and the other Amazonian coastal cities, "
            "and careful about it -- he has no legal authority in Amazonia and prefers everything "
            "quiet. He notices the runners when they arrive and start asking after Hilde, pegs them as "
            "corporate or government agents or mercenaries on business, and pays local street toughs to "
            "hassle them so he can watch how they handle themselves and what they can do. When quiet "
            "stops working he has no compunction about escalating, knowing he and his men can vanish "
            "before the authorities intervene."
        ),
        "background": (
            "An Aztechnology adept running the corporation's interests in a nation founded expressly to "
            "check Aztlan's power. He pursues the runners into the depths of the Amazon either because "
            "of the damage they did leaving Macapa or because he has learned that Mitsuhama is hunting "
            "them and wants to know why -- and to acquire whatever it is MCT wants."
        ),
        "notes": (
            "The book gives him no stat block, only the label 'the Aztechnology adept'; build him at "
            "the level of the team's best combatant. His resources: a ground team of security agents "
            "equal in number to the runners (more if they handled the last encounter easily), two GMC "
            "Riverines with three crew each for the waterfront pursuit, and optionally a hired Tribal "
            "Shaman (SR3 p.78) if the runners have shown magical muscle. He surrounds the team as they "
            "land upriver and asks for the package before ordering the attack. If any runner has "
            "crossed Aztechnology before he may recognise them and go for the bounty. He can be turned "
            "into an asset: get his men and Miyamoto's fighting each other and the runners win the "
            "village fight for free. Hualpa may hire the team afterwards to root out his surviving "
            "confederates in Macapa. Referred to simply as 'Ocelopan' in most of the text."
        ),
    },
    {
        "name": "Nell Miyamoto",
        "role": "MCT Unit 13 field leader hunting the Elemental Scrolls; a physical adept with everything to lose, and the rare corporate operative who keeps her word",
        "archetype": "Physical Adept",
        "title": "MCT Security, Special Projects Division; field leader for Thaumaturgical Research Unit 13",
        "race": "Human",
        "gender": "Female",
        "nationality": "UCAS",
        "organization": "Thaumaturgical Research Unit 13",
        "connection": 3,
        "description": (
            "No-nonsense and visibly military, a karateka whose adept talents were honed in training "
            "rather than discovered in a temple. She calls for the runners to surrender the scrolls and "
            "tells them they will be allowed to go if they do -- and she is true to her word, and does "
            "let them leave. If her team is seriously outclassed she is not stupid about it: she pulls "
            "back, regroups, and comes at the runners with more firepower next time."
        ),
        "background": (
            "Eight years with MCT North America after a hitch in the UCAS military. She worked her way "
            "up through MCT Security into the Special Projects Division on the strength of her military "
            "experience and her ability to take charge -- opportunities she was not always given, "
            "because she is both a woman and half-Anglo, so she pushed herself to be twice as capable "
            "as any man and let her adept powers make it so. She worked hard for her current position "
            "and will not let anything endanger it, and part of her suspects her superiors handed her "
            "this mission specifically to set her up for a fall."
        ),
        "notes": (
            "Stats p.61: B4(6) Q6 S4 C5 I4 W5 E6 M9 R5, Init 5+1D6(3D6), Combat Pool 7, KP/Prof 5/3; "
            "Initiate Grade 3 (Centering (Combat Skills), Centering (Physical Skills), Masking). "
            "Athletics 5(7), Bike 2, Biotech 2 (First Aid 4), Car 3, Centering (Katas) 4, Etiquette 3 "
            "(Military 5), Interrogation 4, Intimidation 4, Leadership 4, Pistols 5, Rifles 4, Stealth "
            "6(8), Unarmed Combat (Karate) 6; English 5, Karate Katas 4, Japanese 4, Japanese "
            "Philosophy 3, UCAS Military Bases 4. Karate 6 (focus strength, focus will, sweep, throw). "
            "Adept powers: Great Leap 2, Improved Athletics 2, Improved Body 2, Improved Reflexes 2, "
            "Improved Stealth 2, Killing Hands (Serious), Pain Resistance 3. Browning Max-Power; armor "
            "7/3 (armor jacket over form-fitting); cell phone, transceiver 4, two concussion grenades. "
            "She leads the New Orleans ambush (or sends security ahead of her), the pursuit upriver and "
            "the village assault. She is the reason surrendering the scrolls is a genuine option."
        ),
    },
    {
        "name": "Kozakura Hiro",
        "role": "Unit 13's junior thaumaturge, who considers himself in charge, is fascinated by the scrolls, and blocks the old shaman's last spell",
        "archetype": "Mage",
        "title": "Doctor; Thaumaturgical Research Unit 13, Mitsuhama Computer Technologies",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japan",
        "organization": "Thaumaturgical Research Unit 13",
        "connection": 3,
        "description": (
            "Arrogant and entirely assured of his magical knowledge and abilities, eager to test them, "
            "and at heart a coward who looks out for himself before anything else and would gladly "
            "sacrifice anyone else on the team to get what he wants. He considers himself in command of "
            "the operation even though Miyamoto is technically his superior, and everyone in the team "
            "knows it. At the village his contribution is decisive and ugly: he blocks the old shaman's "
            "stunball, and the old man dies for it."
        ),
        "background": (
            "Raised inside the corporate family and sent to school on a company scholarship when his "
            "magical gifts appeared. He completed his doctorate in thaumaturgy recently and his company "
            "connections got him assigned to Unit 13, where he has a promising future provided he "
            "proves his usefulness in the field. The Elemental Scrolls fascinate him as an object of "
            "study, but the promotion and prestige that would come with recovering them interest him "
            "considerably more."
        ),
        "notes": (
            "Stats p.61: B3 Q4 S2 C4 I6 W6 E6 M8, Init 5+1D6, Astral 2, Astral Combat 8, Combat 8, "
            "Spell 6, KP/Prof 3/3; Initiate Grade 2 (Centering (Mudras), Shielding). Car 2, Centering "
            "(Mudras) 5, Conjuring 4 (Banishing 6), Enchanting 5, Etiquette 3 (Corporate 5), Leadership "
            "2, Pistol 3, Sorcery 6, Stealth 2; Calligraphy 4, English 4, Japanese 6, Magical "
            "Background 6, Mudras 5, Paranormal Animals 4, Yoga 4. Spells: Alter Memory 4, Analyze "
            "Magic 3, Blindness 4, Control Thoughts 4, Cripple Limb 4, Levitate 3, Manabolt 5, Physical "
            "Barrier 5, Preserve 1, Stunbolt 4, Treat 5. Fichetti Security 500; lined coat 4/2; cell "
            "phone, transceiver 4. He can be given subordinates of his own -- the Combat Mage sample "
            "character (SR3 p.57), with an elemental or two -- to harden the New Orleans ambush."
        ),
    },
    {
        "name": "Ono Isaeo",
        "role": "Unit 13's muscle: a career soldier with two obvious cyberarms who respects Miyamoto, despises Kozakura, and is quietly frightened of him",
        "archetype": "Street Samurai",
        "title": "Security operative, Thaumaturgical Research Unit 13, Mitsuhama Computer Technologies",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japan",
        "organization": "Thaumaturgical Research Unit 13",
        "connection": 3,
        "description": (
            "A soldier: he always has been and he will be until he dies. Two obvious cyberarms with "
            "retractable spurs, and enough alphaware behind them to make him the fastest thing in most "
            "rooms. He has come to respect Nell Miyamoto's abilities both as a soldier and as a leader "
            "and backs her without hesitation, and he makes no secret of his disdain for Dr. Kozakura, "
            "whom he considers a paper-pusher and a bookworm who thinks he is in charge -- though he is "
            "a bit frightened of Kozakura's magic all the same."
        ),
        "background": (
            "He worked MCT Security in San Francisco for several years until the recent change in the "
            "political climate there, and was reassigned. Unit 13 got him, and Miyamoto got a soldier "
            "who does what he is told by the person actually running the operation."
        ),
        "notes": (
            "Stats p.62: B4(6) Q6 S4(7) C3 I5 W5 E0.1 R6(11), Init 6(11)+1D6(3D6), Combat Pool 7, "
            "KP/Prof 4/3. Athletics 4, Edged Weapons 4 (Spurs 6), Etiquette 2 (Military 4), Leadership "
            "3, Pistols 6, Stealth 4, Submachine Guns 6; English 4, Japanese 4, Megacorporate Security "
            "4, Security Procedures 3, Small-Unit Tactics 6. All alphaware: two obvious cyberarms with "
            "smartlink, retractable spurs and Strength Enhancement 3, cybereyes (flare compensation, "
            "display link, thermographic), dampener, datajack, dermal plating 1, hearing amplification, "
            "reaction enhancer, Wired Reflexes 2. Ares Predator and Ingram Smartgun (both smartgunned), "
            "five concussion grenades, armor jacket 5/3, transceiver 4. He is the reason a straight "
            "firefight with the MCT team is dangerous even for a well-armed group."
        ),
    },
    {
        "name": "Spirit of the Winds",
        "role": "One of the two free spirits bound to the Elemental Scrolls; appears whenever the scrolls are endangered and removes them from harm",
        "archetype": "Free Spirit",
        "title": "Guardian of the Elemental Scrolls of Ak'le'ar",
        "gender": "Male",
        "connection": 4,
        "description": (
            "It manifests as a powerfully muscled troll made up of translucent mist, crackling with "
            "flashes of lightning, its eyes glowing electric yellow. It is intelligent and capable of "
            "conversation and is fairly evasive about itself and about the scrolls -- it will not give "
            "its name or explain what the scrolls are, saying only that those things are 'part of the "
            "reason why the scrolls exist' and that it is a 'shadow of what once was'. Quite reasonable "
            "otherwise, and completely unwilling to help anyone with anything beyond keeping its charge "
            "safe."
        ),
        "background": (
            "One of two spirits particularly associated with the Elemental Scrolls of Ak'le'ar, who "
            "appear only when the existence of their charge is threatened -- an attempt to damage them, "
            "a stray round through the crate, a fire. They do not appear to care who possesses the "
            "scrolls so long as the scrolls are unharmed, which makes them a wildcard rather than an "
            "ally. They can be disrupted but cannot be destroyed so long as the scrolls exist, and they "
            "always come back."
        ),
        "notes": (
            "Stats p.60: Force 10, Spirit Energy 3, Great Form. B11(12) Q16x4 S10 C10 I10 W10 R15, Init "
            "25+1D6, Astral 33+1D6, Astral Combat 15, Combat 18, KP/Prof 8/3, Attacks 10M Stun. Powers: "
            "Aura Masking, Cleansing, Concealment, Confusion, Engulf, Guard, Magical Guard, "
            "Materialization, Movement, Psychokinesis, Storm, Wealth. Great Form bonuses: Armor 2/2, "
            "Body +1, Reach +1. Weakness: Vulnerability (Earth). Its priority is removing the scrolls "
            "from danger as fast as possible, usually by psychokinesis, rather than fighting. It will "
            "resist any effort to divert it from its task and flees to the metaplanes if seriously "
            "outmatched. The GM's designated ace in the hole for the pirate boarding and the New "
            "Orleans ambush -- and a threat to runners who threaten the scrolls to keep them from MCT."
        ),
    },
    {
        "name": "Fire Elemental of the Scrolls",
        "role": "The second guardian spirit of the Elemental Scrolls, which eliminates threats to them with ruthless efficiency",
        "archetype": "Free Spirit",
        "title": "Guardian of the Elemental Scrolls of Ak'le'ar",
        "gender": "Male",
        "connection": 4,
        "description": (
            "It appears as a human male in flowing robes, shrouded in fire so that his features are "
            "shadowy and indistinct, with eyes that glow like a furnace. Where the Spirit of the Winds "
            "removes the scrolls from danger, this one removes the danger, and does it with ruthless "
            "efficiency, relying on its innate powers and reaching for sorcery when it must. Like its "
            "companion it will talk, will not give its name, and will not lift a finger for anything "
            "except the safety of the scrolls."
        ),
        "background": (
            "The second of the two free spirits bound to the Elemental Scrolls of Ak'le'ar, appearing "
            "only when the scrolls are endangered. Both call themselves 'shadows of what once was'. "
            "They can be disrupted but not destroyed while the scrolls exist. Runners who took part in "
            "the adventure Legacy in Corporate Punishment will recognise both the scrolls and the "
            "spirits on sight."
        ),
        "notes": (
            "Stats p.60: Force 12, Great Form. B13 Q14x3 S10 C12 I12 W12 R13, Init 23+1D6, Astral "
            "32+1D6, Astral Combat 18, Combat 19, Spell 12, KP/Prof 6/4, Attacks 10M. Powers: Aura "
            "Masking, Dispelling, Engulf (12 metre radius, never harms the scrolls), Flame Aura, Guard, "
            "Hidden Life, Innate Spell (Flamethrower), Materialization, Sorcery (Skill 10); all "
            "elemental, telekinetic and transformation manipulation spells at Force 6. Weakness: "
            "Vulnerability (Water). The book's specific suggestion for the pirate attack: it destroys "
            "one or more of the pirate boats in fiery explosions, either driving them off or giving the "
            "runners the opening to finish them. NAMING: the book calls it only 'the Fire Elemental'; "
            "the row name is descriptive so it is not a bare common noun."
        ),
    },
    {
        "name": "Hideo Yoshida",
        "role": "Deposed Yamatetsu chairman and Buttercup's enemy inside the corporation; sends a helicopter through a Seattle restaurant and a kill team through Vladivostok",
        "archetype": "Corporate Executive",
        "title": "Former chairman of the board, Yamatetsu Corporation",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japan",
        "organization": "Yamatetsu Corporation",
        "connection": 5,
        "description": (
            "Never staged directly unless the runners are captured, and then he is a corporate shark "
            "with a mage at his elbow: an offer of double whatever Buttercup is paying, Analyze Truth "
            "running on every answer, Mind Probe waiting for anyone who declines, and an order to have "
            "the bodies dumped somewhere they will not be found once he has everything -- for the "
            "cooperative and the defiant alike, because anyone who trusts him has earned what they get."
        ),
        "background": (
            "The former chairman of the Yamatetsu board, displaced by the faction Buttercup backs; the "
            "free spirit's support for the current chairman and the corporation's relocation to Russia "
            "are the reasons he is a former chairman, and the reasons he keeps a private estate on "
            "Popov Island and men who are personally loyal to him rather than to the company. His spies "
            "inside the corporation told him about Buttercup's secret meeting in Seattle, and he "
            "arranged the hit knowing full well that it could do no more than disrupt her briefly -- "
            "the real target was whoever she was meeting, and a month without her would be a month he "
            "could use."
        ),
        "notes": (
            "No stat block. His resources: a hired local fixer and a rigger with a Northrup Wasp for "
            "the Seattle strafing (with enough layers of deniability that the runners will never trace "
            "it back to him), and Yamatetsu company men on his personal payroll in Vladivostok "
            "(statted on the Popov Island estate row) who identify the runners off their descriptions "
            "at the port of entry or off the Matrix. He may also simply approach the team with an offer "
            "of at least double Buttercup's fee to take her job and deliberately botch it -- which "
            "would smear their reputations, end Hestaby's use for them and leave Buttercup free to deal "
            "with them as she likes -- and he will make hunting them down a priority if they take the "
            "offer and then cross him. Once the Skytower run is done he causes no further trouble "
            "unless the runners have given him a personal reason."
        ),
    },
    {
        "name": "Sen Lo",
        "role": "The Hong Kong geomancer whose expertise the ritual needs; sixty years old, deep in debt to the Red Dragon Triad, and hiding on a houseboat",
        "archetype": "Wujen",
        "title": "Geomancer and feng shui consultant, Hong Kong",
        "race": "Human",
        "gender": "Male",
        "age": 60,
        "nationality": "Hong Kong",
        "connection": 4,
        "description": (
            "Getting on in years and still in good health, though not as active as he once was; a "
            "wujen of real ability who is not a combat mage or a shadowrunner in any sense, and whose "
            "magic is entirely bent to his work -- geomancy and the design of harmonious environments. "
            "Found on his houseboat he is cautious and on his guard but willing to listen, takes "
            "Buttercup's offer of payment and a way out of Hong Kong gladly and without haggling, and "
            "tells the runners about the Triad straight away. He bows deeply to Buttercup in "
            "Vladivostok: 'It is an honour to meet you, gracious lady.' All he wants is out of debt and "
            "back to some semblance of the successful life he had."
        ),
        "background": (
            "A well-known geomancer and practitioner of feng shui whose services as a consultant are "
            "highly sought after in Hong Kong, and who has forgotten more about feng shui than most "
            "people will ever know. He is not nearly as good at business or personal affairs: he "
            "turned down Wuxing when they wanted to acquire his services permanently, which was "
            "probably not the smartest career move ever made, and he has run up considerable gambling "
            "debts with the Red Dragon Triad -- his good fortune does not extend to the gaming table, "
            "especially when some of the games are rigged in the house's favour. When the Triad "
            "threatened him he went to ground, hoping to raise enough to pay them off."
        ),
        "notes": (
            "Stats p.78: B2 Q2 S2 C3 I6 W6 E6 M9 R4, Init 4+1D6, Astral 26+1D6, Astral Combat 7, Combat "
            "7, Spell 7, KP/Prof 3/2; Initiate Grade 3 (Divining, Masking, Sensing). Aura Reading 6, "
            "Conjuring 4, Divining (Sortilage) 5, Etiquette 3 (Corporate 5), Negotiation 2 (Business "
            "4), Sorcery 5 (Ritual Sorcery 7); Architecture 5, Astrology 6, Chinese Brush Painting 4, "
            "Dowsing 5, Gardening 5, Geomancy 8, Interior Decorating 4, Sortilage 6. Spells: Astral "
            "Window 3, Catalog 4, Cure Disease 4, Detect Life 3, Detox 4, Light 3, Phantasm 4, Physical "
            "Camouflage 4, Shape Earth 5, Shape Water 4. Wooden staff 4M Stun; armor clothing 2/0; "
            "divination coins and a copy of the I Ching. He is meticulous enough to leave no biological "
            "material links in his apartment, and gets a Perception (8) Test to notice ritual tracking "
            "and move on. He can throw a well-timed illusion to help a losing team. Legwork TN 6, any "
            "magical contact (p.77)."
        ),
        "contact_skills": ["Geomancy, feng shui and the power sites of Hong Kong", "Hong Kong's high-price magical consulting clientele"],
    },
    {
        "name": "Kun Xilang",
        "role": "Red Dragon Triad adept leading the team sent to collect Sen Lo alive or make an example of him dead",
        "archetype": "Physical Adept",
        "title": "Adept and initiate of the Red Dragon Triad, Hong Kong",
        "race": "Human",
        "gender": "Female",
        "nationality": "Hong Kong",
        "organization": "Red Dragon Triad",
        "connection": 3,
        "description": (
            "Hardened by a life inside the Triad and merciless toward its enemies. She fights kung fu "
            "at an adept's speed and centres on a kiai shout. Her orders are to collect Sen Lo alive if "
            "possible and kill him if that is what it takes to stop him leaving, because his death as "
            "an example to anyone else who thinks they can cheat the Triads is worth more than letting "
            "him go. She will let the runners walk away if they hand him over without trouble, and kill "
            "them and anyone else in the way if they do not."
        ),
        "background": (
            "Her father was a member of the Triad and she was raised to believe in it and follow its "
            "precepts. Her adept talents proved the key to her rise through the ranks despite her sex, "
            "giving her a position of authority and respect that would otherwise have been closed to "
            "her."
        ),
        "notes": (
            "Stats p.70: B4 Q6(8) S4 C3 I4 W6 M8, Init 6+1D6(3D6), Combat Pool 9, KP/Prof 3/3 (Essence "
            "garbled in the OCR); Initiate Grade 2 (Centering (melee combat skills), Centering "
            "(Athletics skill)). Athletics 5, Bike 4, Centering (Kiai Shout) 4, Etiquette 2 (Triad 4), "
            "Intimidation 4, Leadership 3, Pistols 4, Stealth 5, Unarmed Combat 6 (Kung Fu 8); "
            "Cantonese 5, English 3, Kiai Shout 4, Martial Arts 5, Triad Traditions 5, Zen Philosophy "
            "4. Kung Fu 6 (Kick Attack 8) with Kick Attack, Kip-up, Multi-Strike, Whirling. Adept "
            "powers: Improved Quickness 2, Improved Reflexes 2, Improved Unarmed Combat 2, Killing "
            "Hands (Serious), Pain Resistance 3. Ares Predator; armor jacket 5/3. She brings Little "
            "Chang and at least as many soldiers as there are runners. To harden the fight, raise her "
            "initiate grade; to soften it, cut soldiers. The confrontation can become a chase through "
            "the crowded streets, or a speedboat pursuit through the harbour with Chang throwing "
            "Spirits of the Water."
        ),
    },
    {
        "name": "Little Chang",
        "role": "Dwarf wujen attached to Kun Xilang's team, who summons a Spirit of the Ground before a fight whenever he gets the chance",
        "archetype": "Wujen",
        "title": "Wujen of the Red Dragon Triad, Hong Kong",
        "race": "Dwarf",
        "gender": "Male",
        "nationality": "Hong Kong",
        "organization": "Red Dragon Triad",
        "connection": 3,
        "description": (
            "Short even for a dwarf -- just over a metre tall -- and broadly built with it. He wears "
            "traditional robes under a heavy lined coat and a conical straw hat, and carries a staff "
            "almost twice his own height topped with three jangling rings. If he has any warning before "
            "the runners are encountered he summons a Spirit of the Ground and brings it into the fight "
            "alongside the Triad soldiers."
        ),
        "background": (
            "The magical support attached to Xilang's collection team; the staff and the rings are as "
            "much a working tool as a costume. Known by the name everyone uses for him rather than any "
            "other."
        ),
        "notes": (
            "Stats p.70: B6 Q3 S4 C5 I3 W6 E6 M6 R3, Init 3+1D6, Astral 23+1D6, Astral Combat 7, Combat "
            "6, Spell 5, KP/Prof 2/3. Aura Reading 4, Etiquette 3 (Triad 5), Conjuring 5, Pistols 3, "
            "Sorcery 6, Stealth 2; Cantonese 4, English 4, Magical Background 4, Mandarin 4, Triad "
            "History 4. Spells: Animate 3, Clairaudience 4, Death Touch 5, Gecko Crawl 3, Hot Potato 5, "
            "Intoxication 4, Shape Earth 5, Stunball 4, Thunderclap 4, Treat 3. Browning Max-Power; "
            "lined coat 4/2; three-ring staff (Spirit Focus (Spirits of the Ground) 2). Make him an "
            "initiate with Invoking (great form spirits) or Shielding if the Triad team needs to be "
            "harder. Remember Hong Kong's mana surge -- his spells, like everyone's, may fizzle or go "
            "off far stronger than intended."
        ),
    },
    {
        "name": "Han",
        "role": "The Red Dragon soldier watching Sen Lo's ransacked apartment, who tails whoever comes looking -- and burns to ash rather than break his oath",
        "archetype": "Syndicate Soldier",
        "title": "Red Dragon Triad agent, Hong Kong",
        "race": "Human",
        "gender": "Male",
        "nationality": "Hong Kong",
        "organization": "Red Dragon Triad",
        "connection": 2,
        "description": (
            "One more face in a very crowded city, which is the point. He is on the apartment when the "
            "runners arrive and follows them through Hong Kong afterwards, waiting for them to lead him "
            "to the man his Triad wants; secret Perception (8) Tests once a day are the runners' chance "
            "to spot him. Captured and interrogated he gives up his name and that he works for the Red "
            "Dragon Triad, which is also after Sen Lo, and refuses point blank to say anything more. "
            "Try to force it out of him with magic or any other coercion and he screams and bursts into "
            "flames, burning instantly to ash in front of the runners."
        ),
        "background": (
            "A Triad soldier assigned to surveillance after the syndicate tore Sen Lo's apartment apart "
            "looking for money and for a lead on where he had gone. The Triads take their oaths of "
            "loyalty quite seriously, and Han is the demonstration."
        ),
        "notes": (
            "No individual stat block -- use the Triad soldier stats on the Red Dragon Triad row. Three "
            "ways the surveillance pays off for the syndicate: the runners spot and take the tail (and "
            "learn only what Han's death teaches them), or Han watches them close in on Sen Lo and "
            "calls the collection team, or the Triad finds the houseboat independently at about the "
            "same time. Killing or losing him only buys time; another agent replaces him. He is also "
            "the reason entering the ransacked apartment invisibly matters."
        ),
    },
    {
        "name": "Amon",
        "role": "Celedyr's majordomo, who meets the runners on the Caerleon tarmac, takes them down to the dragon, and explains what happens to guests who decline",
        "archetype": "Corporate Aide",
        "title": "Majordomo to Celedyr, Caerleon",
        "gender": "Male",
        "nationality": "Africa",
        "organization": "Knights of Rage",
        "connection": 3,
        "description": (
            "Not a typical corporate suit at all: African, tall and well muscled, dressed in what looks "
            "like ceremonial costume from a film set -- a wide gold collar, a kind of belted kilt, "
            "sandals and a cloth headdress. He gives the runners a shallow bow at the foot of the "
            "tilt-rotor stairs and a deep-voiced greeting: 'Greetings, welcome to Caerleon. I am Amon, "
            "I will take you to meet your host. This way, please.' He slots his card and presses his "
            "thumb to the scanner at every door, walks ahead down the composite corridors past guards "
            "who watch with cold stares, and bows the team through the double doors into the "
            "amphitheatre."
        ),
        "background": (
            "Celedyr's man on the surface and underground: he handles the arrivals, the briefings and "
            "the terms, and the other men dressed as he is -- the Knights of Rage -- handle everything "
            "that goes wrong afterwards. He shares the briefing on the Songbird job with 'Mr. Johnson' "
            "and answers the runners' questions to the best of his ability."
        ),
        "notes": (
            "No stat block. His hardest scene is Debugging (p.83): if the runners refuse the job, "
            "Celedyr invites them to enjoy his hospitality and think it over, and Amon is the one who "
            "makes the choice explicit -- accept, or remain guests until another team has completed the "
            "run, for security. They are treated decently and they are prisoners for what could be "
            "weeks. His keycard and thumbprint are both Rating 8 (SR3 p.235) and the complex is more "
            "than 50 metres down behind reinforced ferrocrete, so 'take Amon hostage and walk out' is "
            "a much worse plan than it looks."
        ),
    },
    {
        "name": "Branwen",
        "role": "Rhonabwy's drake agent and the smartest of his hunters; escorts the runners out of the lair and then leads the pack that comes after them",
        "archetype": "Drake",
        "title": "Drake; trusted agent of Rhonabwy and leader of his hunt",
        "gender": "Female",
        "connection": 4,
        "description": (
            "In her elven form she is fairly tall, with long pure white hair flowing past her shoulders "
            "and green eyes, in jeans tucked into serviceable boots, a close-fitting T-shirt and a "
            "synth-leather jacket that probably has armor under it, and she carries herself with "
            "confidence even in the presence of a great dragon. She smiles slightly when Rhonabwy tells "
            "the runners his hunters are getting sorely out of practice and gestures them toward the "
            "door: 'After you.' At the surface she gives them a last once-over like an assessment and "
            "says, 'You had better get going, the clock's running.' Her other form is a small western "
            "dragon about three metres long with ivory-coloured scales."
        ),
        "background": (
            "A drake (Threats 2 pp.72-80) in Rhonabwy's service, and one of the two hunters who can "
            "pass as an ordinary person in the outside world, which makes her and Volk their master's "
            "eyes and ears. She is loyal, though not so loyal that she will be quick to sacrifice "
            "herself for him, and she has enough authority over the rest of the pack that they know "
            "better than to disobey her. She would rather bring the runners back alive and in disgrace "
            "for Rhonabwy to play with again than kill them."
        ),
        "notes": (
            "Stats p.91: B3(7/6) Q4(5x4) S4(8) C4 I4 W5 M6 R4(5), Init 4+1D6 (drake form 5+2D6), Astral "
            "26+1D6, Astral Combat 6, Combat 6(7), Spell 5, KP/Prof 4/4, Attacks 4M Stun (8M and +1 "
            "Reach in dracoform); Essence garbled in the OCR. Changing form is an Exclusive Complex "
            "Action; her gear does not transform and some of it may be destroyed in the process. "
            "Drake-form powers: Astral Armor, Enhanced Senses (wide-band hearing, low-light, "
            "thermographic), Innate Spell (Flamethrower). Skills: Athletics 4, Aura Reading 4, Biotech "
            "4, Conjuring 3, Etiquette 3 (Draconic 5), Negotiation 3, Pistols 5, Sorcery 5, Stealth 4, "
            "Unarmed 5. Spells: Detect Life 4, Firewall 5, Improved Invisibility 4, Magic Fingers 3, "
            "Manabolt 5, Resist Pain 5, Stealth 4, Treat 4. Morrissey Alta; armor jacket 5/3. She can "
            "cast in either form, carries the tracking locator, sustains two spells during the opening "
            "phase, heals the pack between assaults, and drops the invisibility and shifts to "
            "dracoform if she is threatened or injured. If she survives, the runners may meet her again "
            "-- and Rhonabwy may hire them."
        ),
    },
    {
        "name": "Andres",
        "role": "The centaur stallion of Rhonabwy's estate herd, who charges with a lance, tramples, and cannot be reasoned with in any language the runners speak",
        "archetype": "Centaur",
        "title": "Stallion of the centaur herd on Rhonabwy's land",
        "gender": "Male",
        "organization": "Rhonabwy's Wild Hunt",
        "connection": 2,
        "description": (
            "Andres is what others call him; his true name sounds more like a series of grunts and "
            "whinnies. He is the stallion of a small herd of centaurs living on Rhonabwy's land, and he "
            "and the other males help patrol the area and keep intruders away. Aggressive and "
            "straightforward: he charges with his lance to spear an opponent or tramples them "
            "underfoot, and he does not stop to consider alternatives. He understands some simple words "
            "in Welsh and no English or any other language, so he is difficult to communicate with at "
            "the very best."
        ),
        "background": (
            "One of Rhonabwy's estate patrol rather than a specialist hunter, brought into the wild "
            "hunt for his speed and his tracking. His Magic Sense power lets him detect characters "
            "using or sustaining magic, and his Search power makes him an excellent tracker -- which "
            "makes him a very poor thing to be near with an active spell running."
        ),
        "notes": (
            "Stats p.90: B10 Q4x5 S7 I3/5 W6 R4, Init 4+2D6, Combat Pool 6, KP/Prof 3/4, Attacks 6S "
            "(trample) with +1 Reach. Powers: Enhanced Senses (low-light, thermographic), Magic Sense, "
            "Search. Skills: Athletics 4, Pole Arms 4 (Lance 6), Stealth 3, Unarmed Combat 4 (Trample "
            "5). Lance 11L with +2 Reach; armor vest 2/1. Branwen sustains Improved Invisibility on him "
            "during the head start, so he comes out of nowhere on the flank after the fliers have "
            "committed. He charges his chosen target and tries to trample them, and he is disdainful "
            "enough of the others in the pack that he will not come to their aid."
        ),
    },
    {
        "name": "Volk",
        "role": "Rhonabwy's wolf shapeshifter, second in command of the hunt and the best tracker in it; the silver in the Songbird's cage is meant for him",
        "archetype": "Shapeshifter",
        "title": "Wolf shapeshifter in the service of Rhonabwy",
        "gender": "Male",
        "organization": "Rhonabwy's Wild Hunt",
        "connection": 3,
        "description": (
            "In humanoid shape he is a hairy, human-looking man with dark hair and a full beard; since "
            "clothing and accoutrements do not change with him he does not bother with any unless he is "
            "leaving the area on a mission. He speaks and understands English and Welsh, though not in "
            "wolf form, and during the hunt he stays a wolf unless there is a reason not to. He spends "
            "most of his time guarding the dragon's domain and living in the wilderness until Rhonabwy "
            "needs him."
        ),
        "background": (
            "A mature wolf shapeshifter whose role is much the same as Branwen's -- both can pass as "
            "ordinary people in the outside world and serve as their master's eyes and ears -- and who "
            "is an excellent tracker and guide in either form. He is her second in the hunt, and one of "
            "the two hunters who will actually look out for the others. The wolf pack the runners may "
            "meet on the way in is led by a shapeshifter using his statistics."
        ),
        "notes": (
            "Stats pp.91-92: human form B5 Q5 S5 C5 I3 W5 E8Z R4, Init 4+1D6, Combat Pool 6, Attacks 5M "
            "Stun; wolf form B7 Q6x5 S6 C5 I3/5 W5 E7 R4, Init 4+2D6, Combat Pool 8, Attacks 8M; "
            "KP/Prof 4/4. Powers: Enhanced Physical Attributes (animal form), Regeneration. Weaknesses: "
            "Allergy (Silver, Moderate) and Vulnerability (Silver). Skills: Athletics 4 (Running 6), "
            "Clubs 4, Intimidation 5, Pistols 4, Stealth 6 (Tracking 8), Unarmed Combat 5. The runners "
            "will not be able to tell him from an ordinary wolf without astral perception, at least "
            "until he is wounded and starts regenerating. The silver wire and filigree of the "
            "Songbird's cage can be bent into crude shotgun shot or simple hand weapons doing (STR)L "
            "against him -- and taking the cage apart to do it is also how the runners are most likely "
            "to find the tracking bug and the C-12. He and Branwen should be the last hunters removed "
            "if the pack needs thinning for a small team."
        ),
    },
    {
        "name": "The Wraith",
        "role": "A Karma-eating free spirit haunting the ruins of Tehran, inciting every fight it can find and growing on the results; the Shroud is the only thing that can destroy it",
        "archetype": "Free Spirit",
        "title": "Wraith of the Tehran ruins",
        "connection": 4,
        "description": (
            "Wraiths generally appear as amorphous clouds of black or grey mist lit from within by a "
            "deep violet light, and materialise either as that mist or as a tall dark figure in "
            "tattered robes surrounded by it. The runners' first sight of it, if anyone makes the "
            "Perception (8) Test during the mad merc's attack, is a shadowy cloaked shape with glowing "
            "violet eyes about ten metres away (TN 6 with astral perception). It avoids direct "
            "confrontation, follows the team through astral space at a distance, watches from behind "
            "ruins and out of windows, vanishes whenever it is threatened and comes back a short while "
            "later. The chill of a Karma tap should be described without explaining it -- only that the "
            "character loses a point of Karma, and was almost overwhelmed by rage and violence."
        ),
        "background": (
            "Wraiths are a very rare type of spirit, similar to shadow free spirits in that they feed "
            "on intense emotion, and unique in being able to steal Karma outright to increase their "
            "Spirit Energy. They are drawn to scenes of intense violence, which are the best feeding "
            "opportunities; their native metaplane is unknown; they are completely immune to summoning "
            "and banishing by Conjuring; and whether they have true names at all is conjecture, since "
            "nobody has ever discovered one. They often enter temporary partnerships with corrupt "
            "magicians and mundanes, strip the follower of all their Karma, and then inspire a new "
            "follower to kill the old one. This one has already used up a mercenary, who is now a "
            "raving puppet, and has spotted better prey."
        ),
        "notes": (
            "Opening stats (p.95): Force 3, Spirit Energy 1. B8 Q10 S4 C4 I4 W4 E4A R5, Init 15+1D6, "
            "Astral 25+1D6, Astral Combat 6, Combat 9, Attack 4M Stun or powers. Generic wraith (p.102): "
            "B F+4, Q F+6, S/C/I/W F, R F+1, Init F+11+1D6, Astral F+20+1D6. Powers: Empathy, Fear, "
            "Influence, Karma Tap, Magic Resistance, Magic Sense, Materialization. Karma Tap: it must "
            "coerce a victim into an act of violence rather than touch them, makes a free Opposed "
            "Force (Willpower) Test alongside any use of Fear, Empathy or Influence, and then drains 1 "
            "point of Good Karma per death the victim causes under its influence (max 1 per minute, or "
            "1 Karma Pool point if the victim has no Good Karma). It also earns 1 Karma when a victim "
            "under its influence dies committing violence, which is why it works both sides of every "
            "fight. Growth: 2 Karma to Spirit Energy 2, 3 more to 3, then 12 to Force 4 (Spirit Energy "
            "drops to 2), 3 more to 3, 4 more to 4, then 15 to Force 5, and so on; grant it a new power "
            "such as confusion, shadow cloak or psychokinesis on each Force increase. It can only "
            "Influence or use Empathy on one character at a time. Destroying it -- not merely "
            "disrupting it -- returns all the Karma to its surviving victims, and the Shroud of Shadows "
            "destroys it outright on a failed Opposed Force Test."
        ),
    },
    {
        "name": "Farah Al-Pasha",
        "role": "The specter leading Tehran's ghosts against the shedim wearing their corpses; she wants her own body destroyed so she can finally rest",
        "archetype": "Specter",
        "title": "Specter; de facto leader of the ghosts of Tehran",
        "race": "Human",
        "gender": "Female",
        "nationality": "Iran",
        "connection": 3,
        "description": (
            "A slim female figure covered from head to toe in dark robes and veils that leave only her "
            "eyes and hands visible; her hands are terribly burned and scarred and her eyes sometimes "
            "seem to glow with a flickering reddish light like the reflection of a bonfire. She is "
            "slightly transparent when she manifests and appears quite solid when she materialises. She "
            "will follow the runners, alternately pleading for their aid and heaping curses on them "
            "until they either help her or drive her off, and she will take any opportunity to possess "
            "one of them. She speaks fluent Arabic and very little English."
        ),
        "background": (
            "She lived in Tehran with her husband and children and understood little of the Awakening "
            "or the other events changing the world until they collided with her life. She died trying "
            "to rescue her children from a terrible fire, and her spirit lingered, forever trying to "
            "save her loved ones and always too late -- until a shedim possessed and animated her "
            "corpse. She considers that a terrible violation and believes that by destroying the shedim "
            "she can at least find peace. She has become the de facto leader of a small group of ghosts "
            "who have been similarly violated, and they struggle against the shedim with every power "
            "they have."
        ),
        "notes": (
            "Stats p.103: Force 5. B6 Q7(x3) S7 C5 I5 W5 E5A R6, Init 16+1D6, Astral 25+1D6, Astral "
            "Combat 7, Combat 8, Attack 3M. Powers: Fear, Materialization, Paralyzing Touch, "
            "Possession, Psychokinesis. English at an effective skill of 1. She is not inclined to "
            "trust anyone and is intensely focused on one purpose: destroy the shedim and lay her body "
            "and the others to final rest. She respects devout Muslims and is far more likely to heed "
            "someone who can quote the Quran and speak Arabic. She can lead the runners to the shedim "
            "if they agree to help -- and a fight with the shedim will bring the wraith. If the runners "
            "helped her, she and her fellow ghosts may appear at the mosque to even the odds."
        ),
    },
    {
        "name": "Mack Donelley",
        "role": "Belfast-born mercenary commander hunting the same Shroud on someone else's contract; a reasonable man who will ally with the runners and sell them out",
        "archetype": "Mercenary",
        "title": "Commander of his own mercenary company",
        "race": "Human",
        "gender": "Male",
        "age": 35,
        "nationality": "Ireland",
        "organization": "Donelley's Mercenary Company",
        "connection": 3,
        "description": (
            "Mid-thirties with the build of a champion weightlifter, though most of it is implants: a "
            "thick neck and close-cropped blond hair, military-style fatigues in the field, goggles "
            "pushed up on his head or hanging loose around his neck. He is never without a weapon close "
            "at hand and he is also deadly unarmed. He is a fairly simple man at heart -- being a "
            "mercenary is all he knows and he loves the work -- and he does not particularly care about "
            "anyone other than the people under his command."
        ),
        "background": (
            "He grew up in war-torn Belfast and got out by signing on with a mercenary company, putting "
            "the skills he had learned in the streets to work on a battlefield. In the years since he "
            "has become a veteran of a number of operations, including the Desert Wars, and earned "
            "enough cred to start his own small outfit. His current employer wants the Shroud of "
            "Shadows out of Tehran but could not provide precise information, so he has wasted days "
            "tracking down the particular mosque and been distracted by the wraith and the other things "
            "in the ruins."
        ),
        "notes": (
            "Stats p.104: B5(7) Q4(6) S6(8) C4 I4, Init 4(6)+1D6(2D6), Combat Pool 6(7), KP/Prof 4/4 "
            "(Willpower and Essence garbled in the OCR). Etiquette 1 (Mercenary 3), Heavy Weapons 6, "
            "Launch Weapons 4, Pistols 4, Rifles 6, Stealth 2 (Urban 4), Unarmed Combat 6; Arabic 2, "
            "Desert Wars 4, English 5, Electronics Background 4, German 2, Mercenary Groups 4, "
            "Mercenary Hot Spots 4, Weightlifting 4. All alpha-grade: Boosted Reflexes 2, electronic "
            "vision magnification 3, flare compensation, Muscle Replacement 2, smartlink, titanium bone "
            "lacing. Armor 6/4. FN-HAR and Beretta Model 101T (both smartgunned), Ares Antioch grenade "
            "launcher with ten HE grenades; goggles with low-light and thermographic vision, "
            "micro-transceiver 5, Nav-Dat GPS, survival kit, three trauma patches. He will consider an "
            "alliance if he thinks it gets him closer to the Shroud -- offering to help in exchange for "
            "transport out of the area, which is a lie -- and will betray the runners at the first "
            "opportunity to come out on top. He can appear as a rescuer mid-fight, at the mosque, or "
            "both, and the wraith will work overtime to set the two teams against each other."
        ),
    },
    {
        "name": "Musa Muqla",
        "role": "Imam, exorcist and unique aspected magician trying to cleanse Tehran of spirits; a potential ally who will not stand by while the runners loot a mosque",
        "archetype": "Aspected Magician",
        "title": "Imam of the Islamic Unity Movement; exorcist and curse-breaker",
        "race": "Human",
        "gender": "Male",
        "nationality": "Iran",
        "organization": "Islamic Unity Movement",
        "connection": 3,
        "description": (
            "A devout Muslim who has charged himself with an enormous task and taken a small cadre of "
            "fanatical followers into a dead city to do it. He is cold and disdainful toward the "
            "Awakened members of the runners' team, and quite angered by anyone who suggests his own "
            "abilities are magic rather than a blessing from Allah. He will aid the runners against an "
            "obviously inhuman foe, then want to know who they are and what they are doing in Tehran; "
            "he has no quarrel with them until he learns where they are going, at which point he "
            "insists on coming along."
        ),
        "background": (
            "Muqla was a devoted follower of the Islamic Unity Movement and of Badr al Din Ibn Eisa. "
            "Over the years he built a reputation as an exorcist and curse-breaker, which led to his "
            "becoming an imam; he was drawn to Ibn Eisa's charismatic leadership and became even more "
            "convinced of his holiness following the apparent assassination and miraculous "
            "resurrection. He is not fully behind the New Islamic Jihad's calls for militancy and chose "
            "his own quest instead: assessing whether Tehran can be purged of the spirits and creatures "
            "haunting its ruins so that decent people could live there again, and cleansing every "
            "mosque and holy place of malign spiritual influence along the way."
        ),
        "notes": (
            "Stats p.105: B3 Q3 S3 C6 I4 W6 E6 M8 R3, Init 3+1D6, Combat Pool 6, Spell Pool 6; Initiate "
            "Grade 2 (Masking, Shielding). Aura Reading 4, Clubs 4, Conjuring 4 (Banishing 8), Etiquette "
            "3 (Muslim 5), Intimidation 4, Leadership 4, Negotiation 3, Pistols 4, Sorcery 5 (Spell "
            "Defense 7); Arabic 3, Magical Background 4, Middle East 4, Persian 3, Quran 6, Spirits 5. "
            "Lined coat 4/2; heavy staff 4M Stun; Browning Max-Power. A unique sort of aspected "
            "magician (SR3 p.160): he can use magic only defensively -- Conjuring to defend against and "
            "banish spirits of all types, Sorcery and Spell Pool for spell defence, shielding and "
            "dispelling, and astral perception to read auras and intent and see through disguises and "
            "illusions with his Masking. He cannot otherwise perform magic himself, which may simply be "
            "a mental block, since he considers magic evil. He does not yet know the Shroud exists; if "
            "he learns, he wants it delivered to Ibn Eisa in Mecca, perhaps after using it to clear "
            "Tehran. He can also be the GM's safety valve: he can temporarily overcome the wraith's "
            "powers, work out that the Shroud smothers such spirits, and say so out loud."
        ),
    },
    {
        "name": "Badr al Din Ibn Eisa",
        "role": "The Muslim prophet whose apparent assassination and resurrection made Musa Muqla a believer; the intended recipient of the Shroud if Muqla gets it",
        "archetype": "Religious Leader",
        "title": "Prophet and leader of the Islamic Unity Movement; based in Mecca",
        "gender": "Male",
        "organization": "Islamic Unity Movement",
        "connection": 5,
        "description": (
            "Off-screen throughout, and present in the adventure entirely through the conviction of the "
            "man carrying his mission into the ruins. His charismatic leadership drew devout Muslims "
            "across the region into the Islamic Unity Movement, and the apparent assassination and "
            "miraculous resurrection settled the question of his holiness for those already inclined to "
            "believe. His name is also attached to the New Islamic Jihad and its calls for militancy, "
            "which Muqla does not fully support."
        ),
        "background": (
            "Detailed in Year of the Comet pp.52-54, which the book recommends handing to players as "
            "background reading for this adventure. In Survival of the Fittest he is the reason Musa "
            "Muqla is in Tehran at all, and the destination Muqla has in mind for the Shroud of Shadows "
            "should he ever learn it exists -- delivered into Ibn Eisa's hands in Mecca, perhaps after "
            "being used to rid Tehran of some of its more malignant spirits."
        ),
        "notes": (
            "No statistics, no scenes, and no direct involvement in the campaign; built as a row "
            "because he is the authority Muqla answers to and the loose end if the Shroud goes to the "
            "missionaries instead of to Radek or back under the mosque floor. A GM who wants to extend "
            "Rest has an obvious hook: the Shroud, a prophet in Mecca, and a great dragon who would "
            "rather nobody had it at all."
        ),
    },
    {
        "name": "Dweller on the Threshold",
        "role": "The guardian of the metaplanes, who asks the runners why they have come, tells everyone their secrets, and tests each of them before letting them pass",
        "archetype": "Metaplanar Guardian",
        "title": "The Dweller on the Threshold",
        "connection": 4,
        "description": (
            "The runners drift in an utter blackness, only barely aware of their bodies, for a length "
            "of time they cannot judge. Then a light appears, a pinpoint at first and steadily larger, "
            "with a figure standing silhouetted in it whose features never resolve. The rest of the "
            "team steps out of the darkness into the circle of illumination. It regards them silently "
            "for a moment before speaking. 'Why have you come here?' Then, to the first runner who "
            "answers: 'Are you prepared to face what lies ahead?' -- and whichever way they answer, the "
            "reply is designed to shake their confidence or confirm their fears."
        ),
        "background": (
            "The guardian of the metaplanes (Magic in the Shadows p.92), effectively all-knowing and "
            "all-powerful within its own domain. It can cause anything to happen, or at least seem to, "
            "which on the astral is much the same thing, and it knows everything about the "
            "shadowrunners including things they are not consciously aware of. Its question is a "
            "formality -- it does not actually care what they are after."
        ),
        "notes": (
            "It does three things: asks why they wish to enter, reveals something personal about each "
            "character to everyone present -- preferably a secret, embarrassing or shameful thing, "
            "which the GM should prepare in advance or ask the players for -- and sets each of them a "
            "test. Test options: a Skill (6) Test against their highest-rated skill in a scenario the "
            "Dweller invents; a seemingly impossible task where the point is the courage to try, "
            "resolved by Willpower (6); a puzzle or riddle by Intelligence (6), with an automatic "
            "success for a player who actually solves it; or a demand that the character act against "
            "his nature, where standing firm and sacrificing for the greater good both count as "
            "success, Willpower (6) with an automatic success for roleplaying the choice. No successes: "
            "'You may pass, but you are not ready for the challenges that lie ahead. You will fail.' "
            "One or more: 'You may pass. May you be as successful in your quest.' Every two full "
            "successes grant a bonus point of Karma Pool for the duration of the astral quest. Unlike a "
            "normal astral quest, the Dweller must let them through whether they succeed or not, so "
            "long as they observe the formalities -- working for a great dragon has its benefits. "
            "Runners who try to muscle past simply fail; its patience is seemingly infinite."
        ),
    },
]

ORG_UPDATES = {
    "Dunkelzahn Institute of Magical Research": {
        "notes_append": (
            "Survival of the Fittest: the Institute is the reason Elements happens. Hualpa lent it the "
            "Elemental Scrolls of Ak'le'ar -- Dunkelzahn's bequest to him -- for study, and a "
            "Mitsuhama Thaumaturgical Research Unit 13 operation heisted them out of a lab at MIT&T in "
            "Boston (the adventure Legacy in Corporate Punishment). There were complications, MCT did "
            "not keep them, and after passing through several hands the scrolls ended up with Hestaby, "
            "who returns them to Amazonia to score a point in the Rite of Succession. Ever since the "
            "theft the Institute has been working with the Draco Foundation to recover them and, in "
            "one contact's words, 'scrambling to kiss Hualpa's feathered hoop to avoid a big "
            "incident'. It never appears on-screen, but it is on the book's list of parties who might "
            "crash the New Orleans handover with a team of their own. Legwork on the scrolls, TN 6, "
            "any magical contact (p.59)."
        ),
        "enemies_add": ["Thaumaturgical Research Unit 13"],
    },
    "Human Nation": {
        "notes_append": (
            "Survival of the Fittest: Human Nation and the Humanis Policlub both have more than a few "
            "supporters in northern California, where the Northern Crescent sits against a disputed "
            "Tir Tairngire border and anti-metahuman and particularly anti-elven sentiment runs high; "
            "they hold human-only enclaves scattered through the area. Getting There Is Half the Fun "
            "(p.25) offers them as one of the optional encounters on the way to Mount Shasta: "
            "metahuman or changeling runners may draw their attention, and some of the bigots will "
            "take it on themselves to teach the unwanted 'freaks' a lesson before discovering they "
            "have bitten off more than they can chew. No stats or named individuals are given; scale "
            "the mob to the team. The book sets them explicitly as the counterpoint to the tolerance "
            "of the Shasta Enclave's gypsy caravans, and notes that the enclave itself is not like "
            "this."
        ),
        "enemies_add": ["Shasta Enclave Gypsies"],
    },
    "Saeder-Krupp Heavy Industries": {
        "notes_append": (
            "Survival of the Fittest: Lofwyr's megacorporation is the answer to the question the whole "
            "Rite of Succession asks -- he poured his hoard into it because a corporation is the true "
            "source of power in the twenty-first century, and it is now the largest, wealthiest and "
            "most powerful megacorp in the world. Headquarters: the Rhine-Ruhr Megaplex, German "
            "Alliance. It holds the Jewel of Memory, delivered by the Draco Foundation, which makes "
            "Lofwyr de facto Loremaster. During the Rite, Alamais arranges the theft of the physical "
            "Jewel from S-K headquarters and Lofwyr all but lets him have it, knowing Hestaby is after "
            "the astral essence and that the stone without it is worthless. The Two-Pronged Attack "
            "option (p.108) sends a second runner team into S-K headquarters for the same stone, "
            "possibly running into Alamais's people. In Cunning, the evidence Hestaby plants on Joshua "
            "Morningstar is a set of telecom records to and from PLTGs in the German Alliance or "
            "associated with Saeder-Krupp; a Computer (6) Test spots the tampering. At the Citadel "
            "Lofwyr offers the runners anything within reason to betray Hestaby -- delta-grade "
            "cyberware, magical lore, limitless wealth, longevity treatments, their own island -- and "
            "promises every resource S-K has turned to ruining their lives if they refuse. The Rite "
            "protects agents from retribution afterwards, so the threat is largely (not entirely) "
            "empty."
        ),
        "enemies_add": ["Council of Dragons"],
    },
    "Mitsuhama Computer Technologies": {
        "notes_append": (
            "Survival of the Fittest: MCT is the corporate antagonist of Elements through "
            "Thaumaturgical Research Unit 13, its magical resources and black-ops division -- 'special "
            "thaumaturgical research', which the street reads as black magic of the deepest and most "
            "secret kind. Unit 13 ran the Boston operation that heisted the Elemental Scrolls of "
            "Ak'le'ar from a Dunkelzahn Institute lab at MIT&T; there were complications, MCT did not "
            "keep them, and Unit 13 has been hunting them ever since. Elements is the last shot: a "
            "field team of Nell Miyamoto, Dr. Kozakura Hiro and Ono Isaeo plus expendable security "
            "hits the New Orleans handover, tracks the runners to Macapa and assaults the Amazonian "
            "village. MCT security personnel: B4 Q4 S3 I3 W3 E4.6 R3, Init 3+1D6(2D6), Combat Pool 5, "
            "KP/Prof 1/3 -- loyal but not fearless, and they retreat before overwhelming force or "
            "strange magic. Legwork TN 4, any corporate contact or Matrix search (p.58) names Unit 13, "
            "the Boston dust-up and the scroll hunt."
        ),
        "enemies_add": ["Dunkelzahn Institute of Magical Research", "Amazonia"],
    },
    "Aztechnology": {
        "notes_append": (
            "Survival of the Fittest: Aztechnology is one of the two megacorps with a strong interest "
            "in magic chasing the Elemental Scrolls of Ak'le'ar, and it keeps undercover agents in "
            "Macapa and the other Amazonian coastal gateway cities -- Reynaldo Ocelopan among them, "
            "who tests the runners with hired street toughs, tries to stop them leaving the waterfront "
            "with a ground team and two pursuit Riverines, and ambushes them upriver. He has no legal "
            "authority in Amazonia and prefers things quiet, but he and his men can disappear before "
            "the authorities intervene. Hualpa's stated goal is to see Aztlan and Aztechnology removed "
            "from power so the damage they have done -- the Yucatan War above all -- can be healed, "
            "and Amazonia was created at least partly as a check on Aztlan's expansion. Optional (p.44): "
            "Aztechnology agents with heavy weapons take the chance to strike at Ghostwalker outside "
            "his lair during the Denver warehouse meet."
        ),
        "enemies_add": ["Amazonia", "Thaumaturgical Research Unit 13"],
    },
    "Aztlan": {
        "notes_append": (
            "Survival of the Fittest: Ghostwalker's first act on returning in the last days of 2061 "
            "was to assault the Aztlan sector of the Denver Front Range Free Zone, destroy the teocalli "
            "there and make it clear that Aztlan would be removed from the city entirely. The CAS "
            "sector still borders a burned-out strip along the old Aztlan line, which is where the "
            "runners hand Morningstar over. Azzie-backed terrorists and dissidents are the main "
            "opposition Ghostwalker still faces in Denver. Aztlan patrol ships in the Gulf are one of "
            "the hazards Cap'n Fixx's Gulf Runner routinely dodges, and they are jumpy given the "
            "situation in the Yucatan; the chemical agents used in the Yucatan War may have thrown up "
            "toxic spirits and mutant creatures in the Caribbean."
        ),
        "enemies_add": ["Council of Dragons", "Amazonia"],
    },
    "Yamatetsu Corporation": {
        "notes_append": (
            "Survival of the Fittest: Yamatetsu is the beneficiary of Balance. The free spirit "
            "Buttercup, who sits on its board, strikes a bargain with Hestaby to divert some of the "
            "chi Wuxing has been accumulating under its Hong Kong Skytower to Yamatetsu's power site "
            "in Vladivostok, so that the two ostensibly allied Pacific Prosperity Group corporations "
            "become like the poles of a magnet -- Wuxing checked, Yamatetsu lifted, and Lung and "
            "Ryumyo distracted by the shift in the dragon lines. The corporation's new worldwide "
            "headquarters is on Popov Island near Vladivostok. The internal fight is real: Buttercup "
            "backs the current chairman, and the deposed former chairman Hideo Yoshida keeps a private "
            "estate on Popov Island and men personally loyal to him, who tail and try to take the "
            "runners in Vladivostok. Company men of Yoshida's faction: B5 Q4(5) S5(7) C2 I4 W4(5) E5.3 "
            "R4(7), Init 4(7)+1D6(3D6), Combat Pool 6(7), KP/Prof 3/3, cultured bioware throughout. "
            "Afterwards Yamatetsu gains new opportunities, helps prop up its stumbling ally inside the "
            "PPG, and Vladivostok sees a spell of unusual magical activity."
        ),
        "enemies_add": ["Wuxing, Inc."],
    },
    "Wuxing, Inc.": {
        "notes_append": (
            "Survival of the Fittest: Dunkelzahn willed the statue known as the Jade Dragon of Wind "
            "and Fire to Wuxing's CEO, who used its magical properties to intensify the power site "
            "under the corporation's Hong Kong headquarters. The Wuxing Skytower has been drawing "
            "increasing amounts of chi ever since and Wuxing's star has risen with it -- disrupting "
            "Lung's and Ryumyo's plans for the Asian dragon lines, warping the use of magic across "
            "Hong Kong into mana surge and wild magic conditions, and possibly (Hestaby suspects) "
            "contributing to the natural disasters that struck Japan. The penthouse is a Rating 8 "
            "power site laid out as a temple; the tower is warded at Rating 8, patrolled by three "
            "bound Force 6 air elementals, carries a +4 TN background count on astral tests and sits "
            "inside an astral shallow that makes every astral form permanently visible. The runners' "
            "feng shui 'redecorating' couples it to Vladivostok, the astral shallow disappears, and "
            "Wuxing suffers a run of minor setbacks. Wuxing security guards: B5 Q5 S5 C3 I4 W4 E3.78 "
            "R4(8), Init 4(8)+1D6(3D6), betaware smartlink and Wired Reflexes 2, Savalette Guardian "
            "and Ingram Smartgun with EX ammo, light security armor with helmets 7/6. Security wujen: "
            "B3 Q4 S4 C6 I5 W5 E6 M8 R4, Initiate 2 (Invoking, Reflecting), Conjuring 7, Sorcery 5 "
            "(Spellcasting 6), dragon figurine (Levitate sustaining focus 4). Wuxing also turns up on "
            "the list of parties who might crash the New Orleans handover, and Sen Lo once turned down "
            "a permanent post with them. DISCREPANCY: this book spells the CEO 'Wu Lung-Wei'; the "
            "campaign's existing row is 'Wu Lung-Wai'. Not rewritten."
        ),
        "enemies_add": ["Red Dragon Triad", "Yamatetsu Corporation"],
    },
    "Pacific Prosperity Group": {
        "notes_append": (
            "Survival of the Fittest: the PPG is the frame for Balance. Wuxing and Yamatetsu are "
            "allies inside it and Buttercup has no particular fondness for Wuxing -- an ally of "
            "convenience, nothing more -- so she is willing to divert its accumulated mystic power to "
            "her own corporation to put the two on more even footing and stop Wuxing dominating the "
            "group. She would still prefer Wu Lung-Wei never learned of her involvement. After the "
            "ritual Wuxing suffers minor setbacks and Yamatetsu, having gained new opportunities, "
            "helps maintain its ally's position within the Group -- which is precisely the balance "
            "Hestaby was buying."
        ),
    },
    "Tir Tairngire": {
        "notes_append": (
            "Survival of the Fittest: Hestaby turned back an attempted Tir invasion of northern "
            "California in 2053, which is why the people of the Northern Crescent of the California "
            "Free State regarded her as their deterrent against elven aggression -- and why her recent "
            "appointment to the Tir's ruling Council of Princes has alienated many of them, who now "
            "call her a traitor. It also split the Shasta Lodge: some shamans left in protest at what "
            "looked like selling out to the elves, and others stayed to work for change. Legwork on "
            "Hestaby (TN 6, magician / Tir Tairngire / dragon-watcher contacts, p.32) turns this up at "
            "one success. The Tir border is a live one throughout Knowledge: Tir patrols may shoot "
            "down aircraft crossing their territory, few smugglers will cut through the Tir on the way "
            "into CalFree, and anti-elven sentiment runs high in the Northern Crescent because of the "
            "proximity. Hestaby refuses to discuss her Tir business with the runners: 'That has "
            "nothing to do with the matter at hand.'"
        ),
    },
    "Transys Neuronet": {
        "notes_append": (
            "Survival of the Fittest: the telecommunications megacorp is the great dragon Celedyr's "
            "corporate partner. Its Caerleon facility in southeastern Wales -- new steel, chrome and "
            "glass wrapped around a ring of ancient standing stones -- sits directly above his "
            "underground lair, and Transys has supplied him with millions of nuyen of equipment and "
            "researchers in exchange for his support and his occasional insights into their projects; "
            "language and communication fascinate him. The corporation flies the runners in and out by "
            "tilt-rotor, its state-of-the-art VR rig can be used to run dry runs of the Songbird "
            "break-in, and Celedyr will pay a team up to twice their 150,000 nuyen fee in Transys "
            "hardware, software and cyberware with free installation by Transys technicians. The "
            "ceremonially dressed guards holding the underground corridors are the Knights of Rage."
        ),
        "allies_add": ["Knights of Rage"],
    },
    "Amazonia": {
        "notes_append": (
            "Survival of the Fittest: Elements takes the runners into Amazonia. The coastal cities "
            "such as Macapa, at the mouth of the Amazon on the equator, are maintained by the "
            "Amazonian Awakened as gateways where anyone may trade freely so long as they break no "
            "local laws and do not venture too far into the interior. The interior teems with Awakened "
            "life and the nation protects the rainforest with an iron fist -- usually by letting the "
            "jungle critters eat anyone who crosses the line. Air defences include air spirits, "
            "elementals and other paranormals in the service of the Awakened, and it is not unknown "
            "for a dragon to bring down unwanted aircraft, which is why guides insist on the river. "
            "Amazonia is a haven for the Awakened in principle, though many of the metahumans and "
            "changelings in Macapa are squatters or beggars. Hualpa sends a feathered serpent to a "
            "nameless jungle village to collect the returned Elemental Scrolls of Ak'le'ar and thanks "
            "the runners on the nation's behalf. Legwork TN 4 for activist contacts, TN 6 otherwise "
            "(p.59)."
        ),
        "enemies_add": ["Aztlan", "Aztechnology"],
    },
    "The Nexus": {
        "notes_append": (
            "Survival of the Fittest: Ghostwalker moved quickly to make an ally of the Nexus data "
            "haven after seizing Denver -- one of the two signs (with his open-door 'petitioning' "
            "policy) that a great dragon fresh out of a long sojourn on the higher astral planes is "
            "adapting to the modern age faster than anyone expected of him."
        ),
    },
    "TerraFirst!": {
        "notes_append": (
            "Survival of the Fittest: Joshua Keller -- later Brother Joshua Morningstar, prophet of "
            "the Denver Children of the Dragon -- developed liberal and even radical politics at the "
            "University of Virginia and became involved with TerraFirst! and various civil-rights "
            "causes before he joined Dunkelzahn's 1957 campaign and was dismissed from it for using "
            "violent methods against the dragon's opponents. Environmental Groups 4 and Radical Groups "
            "4 are still on his knowledge skill list, and Legwork (TN 4, p.45) reports that he did not "
            "have any problem getting his hands dirty and still knows how to get things done on the "
            "streets."
        ),
    },
    "Humanis Policlub": {
        "notes_append": (
            "Survival of the Fittest: the Humanis Policlub and the hate group Human Nation both have "
            "more than a few supporters in northern California, where the Northern Crescent sits "
            "against a disputed Tir Tairngire border and anti-metahuman and particularly anti-elven "
            "sentiment runs high. Metahuman or changeling runners crossing the country toward Mount "
            "Shasta may draw attention from one of their human-only enclaves, and some of the bigots "
            "will take it on themselves to teach the unwanted 'freaks' a lesson (Getting There Is Half "
            "the Fun, p.25). The Shasta Enclave itself is pointedly not like this."
        ),
        "enemies_add": ["Shasta Enclave Gypsies"],
    },
    "Yakuza (Watada-rengo)": {
        "notes_append": (
            "Survival of the Fittest: The Rubber Suit, the exclusive giant-monster-movie club in "
            "Everett where Mr. Radek holds the campaign's first meet, is known to be something of a "
            "hangout for the local yakuza -- the book invites the players to draw their own "
            "conclusions from a fixer choosing it. Pushing the Envelope (p.23) offers the club as a "
            "perfect place for the Mafia to stage a hit on the local kobun, or for a Seoulpa Ring, a "
            "Triad or gangers in their employ to do the same, with the runners caught in the "
            "crossfire. Separately, Ryumyo's power base in Japan runs through the Yakuza and, through "
            "them, several Japanese megacorporations, and the Yakuza have been fighting the Red Dragon "
            "Triad over the black market and smuggling in the Sea of Japan."
        ),
    },
    "Red Dragon Association": {
        "notes_append": (
            "Survival of the Fittest: DISCREPANCY / disambiguation. Balance introduces the Red Dragon "
            "Triad of Hong Kong -- one of the major Hong Kong triads, said on the street to answer "
            "ultimately to the great dragon Lung on the mainland, currently feuding with the Yakuza "
            "over the Sea of Japan black market and holding the geomancer Sen Lo's gambling debts. The "
            "book never links it to the Seattle Red Dragon Association and gives no shared leadership, "
            "so the two are filed as separate bodies here; a gamemaster who wants them to share a "
            "parent syndicate has nothing in either text standing in the way."
        ),
    },
}

LOC_UPDATES = {
    "The Space Needle": {
        "notes_append": (
            "Survival of the Fittest: the Eye of the Needle, the revolving restaurant at the top of "
            "the Needle, is where Mr. Radek books the meet with Buttercup at 10 PM in Balance -- one "
            "of the most exclusive restaurants in the metroplex, hard to get into without a name that "
            "works wonders, with an elven maitre d' who checks weaponry at the door. Midway through "
            "the negotiation a Northrup Wasp on a chin-mounted RPK HMG makes three strafing passes at "
            "the side of the restaurant the team is sitting on, shattering the armored glass (base "
            "damage 10D to anyone not under cover) on the orders of the deposed Yamatetsu chairman "
            "Hideo Yoshida. The book never names the Needle -- it says only 'one of the most exclusive "
            "restaurants in the metroplex' -- but the rotating floor and the skyline view leave little "
            "doubt. See the Eye of the Needle row."
        ),
    },
}

NPC_UPDATES = {
    "Lofwyr": {
        "description_append": (
            "Survival of the Fittest: at the Council of Dragons he is larger than even Ghostwalker, "
            "his scales shining in a rich range of gold, copper and burnished brass with undertones of "
            "terra cotta and dun; he lands last and most majestically of all, folding his wings with "
            "deliberate slowness, each movement studied and precise, and accepts the Rite of Honored "
            "Greeting as his rightful due. His thought-voice stays controlled and tightly leashed even "
            "when Ghostwalker interrupts the opening of the Council, and he answers a peer with "
            "exaggerated patience 'as if he were speaking to a hatchling'. His aura remains placid "
            "throughout, showing tremendous control. In the metaplanar Citadel he enters through an "
            "archway with a sound like metal brushing metal, scales darkening toward his back and "
            "paling toward his belly, eyes like pools of red fire matching the gemstone, smoke "
            "trickling from his nostrils, and coils around the pillar as though smiling."
        ),
        "background_append": (
            "Survival of the Fittest: his use-name among his own kind is Gold-Master. Dunkelzahn "
            "willed him the Jewel of Memory, and the Draco Foundation delivered it, making him "
            "Loremaster in fact without his having to risk anything to win it -- which is the "
            "irregularity Ghostwalker returns from the astral planes to challenge. A few upstarts, "
            "Nachtmeister among them, contested the claim and paid the ultimate price, discouraging "
            "the rest. At the Council he declines to say whether he arranged Dunkelzahn's death "
            "(which would have made his claim rightful) rather than lie in front of witnesses who "
            "might have proof, concedes the Rite, and then turns the concession into his own trap: not "
            "a duel here and now but a full Rite fought through proxies. He also all but lets his "
            "brother Alamais steal the physical Jewel during the contest, knowing Hestaby is after the "
            "astral essence and that the stone without it is worth nothing."
        ),
        "notes_append": (
            "Survival of the Fittest: no game statistics, like every great dragon in this book; in the "
            "metaplanes his power is such that no player character survives attacking him. His offer "
            "at the Citadel (p.120): hand him the gemstone back in the physical world and he will give "
            "the runners whatever they want within reason -- delta-grade cyberware, magical knowledge "
            "and lore, limitless wealth, gene-therapy longevity treatments, reconstructive surgery, "
            "their own island -- sworn as a solemn oath in a place where oaths are not easily broken, "
            "and he means it, because even a billion nuyen is chump change to him. He is not a "
            "wish-granting genie: he cannot make a runner President of the UCAS, only fund the "
            "attempt. The alternative he paints just as vividly is every resource Saeder-Krupp has "
            "turned to ruining a handful of lives. He cannot interfere in a fight among the runners "
            "themselves but will happily nudge one side into eliminating the other. Beaten at the "
            "Endgame, he comes to Mount Shasta in astral form to tell Hestaby he underestimated her "
            "and that it will not happen again -- and is visibly thrown when she proposes friendship "
            "instead of rivalry: 'You have become too enamoured of the young races and their ideas, "
            "Orange Queen. What is friendship to us?'"
        ),
    },
    "Dunkelzahn": {
        "background_append": (
            "Survival of the Fittest: to his own kind Dunkelzahn is Far-Scholar, and he was Loremaster "
            "of the dragons long before he appeared to the modern world -- holder of the greatest "
            "store of draconic knowledge and the accumulated lore of untold millennia, recognised as "
            "the authority on draconic tradition, respected and feared by his peers. Some of them "
            "feared his fascination with the young races would lead him to reveal things best kept "
            "secret, and made the consequences of doing so abundantly clear to him. His death left the "
            "Loremaster's seat vacant for the first time in more than an Age, and then he surprised "
            "them all again with a will -- metahuman legal machinery used to disperse a hoard, which "
            "no dragon had ever done and which is the affront the entire Rite of Succession exists to "
            "answer."
        ),
        "notes_append": (
            "Survival of the Fittest: his bequests drive all seven adventures -- the Jewel of Memory "
            "to Lofwyr, the Elemental Scrolls of Ak'le'ar to Hualpa, the Silver Songbird to Rhonabwy, "
            "the Shroud of Shadows to Aden, the Second Coin of Luck to Lung, the Ring Ouroboros (and "
            "'my envy at stealing my chance to be the very first dragon') to Ryumyo, the Jade Dragon "
            "of Wind and Fire to Wu Lung-Wei of Wuxing, and to Hestaby the encryption key to his "
            "private datastore on the Zurich Orbital Habitat -- which she opens in the epilogue to "
            "find a letter beginning 'My dear Hestaby, I am sure there will soon come a time when you "
            "face a challenge among our kind. When you do, consider my advice for dealing with our "
            "fellow dragons ...'. He also appears in person, in a manner of speaking: one of the "
            "suggested Place of Fear challenges (p.116) drops the runners into the back seat of his "
            "limousine on inauguration night, where Dunkelzahn in human form and a tuxedo tells them "
            "he is having second thoughts about the sacrifice he is about to make and the ripples his "
            "will is going to create, and it falls to the runners to convince him he is doing the "
            "right thing before the limo goes up in a fireball and he thanks them. The Children of the "
            "Dragon cult grew out of his assassination; Hestaby has taken up his cause; and Lofwyr's "
            "sourest compliment to her is 'You're beginning to sound like Far-Scholar.'"
        ),
    },
    "Buttercup": {
        "description_append": (
            "Survival of the Fittest: she appears to the runners as a Japanese girl no more than "
            "eighteen at the most -- a rose-coloured blouse, a dark skirt, black hair cut almost "
            "boyishly short, a broad smile and a slight bow -- materialising where nobody is watching "
            "so she can walk up on a table of hardened street operatives unheard. She goes by 'Ms. "
            "Johnson'; asked whether she is Buttercup she smiles and says 'Yes, I get that a lot', or "
            "'As I understand it, it isn't wise to ask someone's true name in this business', and "
            "keeps coyly deflecting. She indulges the runners in anything on the menu and takes only "
            "tea herself, and only if they are eating."
        ),
        "background_append": (
            "Survival of the Fittest: she is the runners' employer in Balance and Hestaby's partner in "
            "it. Her agenda is to further Yamatetsu's fortunes while reining Wuxing in and putting the "
            "two corporations on even footing inside the Pacific Prosperity Group -- technically a "
            "betrayal of an ally, but Wuxing is an ally of convenience and nothing more, and she would "
            "rather Wu Lung-Wei never learned of her part in it. She decided the matter was too "
            "delicate to entrust to anyone else, which was also a convenient excuse to take the "
            "measure of Hestaby's chosen agents in person."
        ),
        "notes_append": (
            "Survival of the Fittest: treated as an Ultimate-level NPC (SRComp p.84) with no game "
            "statistics; assume she knows whatever spell the situation needs and can cast it at Force "
            "6 or better with no drain. Assensing shows a mundane girl unless the character penetrates "
            "her Aura Masking (treat her as a Grade 9 initiate for the Masking Test); Intelligence "
            "(8), or TN 6 with Free Spirits or Yamatetsu knowledge skills or contacts, recognises her "
            "from Yamatetsu documentation on the Matrix. She is difficult to harm and even a massive "
            "attack only disrupts her for a time -- Hideo Yoshida's helicopter strike on the Eye of "
            "the Needle is intended to drive her out of the physical world for a month and to kill "
            "whoever she was meeting. Learning her true name requires penetrating the masking and then "
            "a Quest Rating 10+ astral quest; she bitterly resents and mercilessly eliminates anyone "
            "who tries to bind her. Terms: 50,000 nuyen a head for delivering Sen Lo to Vladivostok "
            "plus 120,000 each for the Wuxing Skytower run, up to 5,000 each in advance, negotiable up "
            "20 percent and no further, and 5 percent of the second fee if the team survives but "
            "fails. She reveals nothing about the second job until Vladivostok and lets the runners "
            "decline it without hard feelings. Legwork TN 4, any corporate contact (p.77): she backs "
            "the current chairman and without her he would probably have been geeked already; she has "
            "an agenda of her own for Yamatetsu, and the relocation to Russia was part of it; people "
            "who assumed she was just playing businesswoman underestimated her badly."
        ),
        "contact_skills_add": ["Yamatetsu board politics and the Pacific Prosperity Group", "Geomancy, dragon lines and the power sites of the Pacific Rim"],
    },
    "Masaru": {
        "background_append": (
            "Survival of the Fittest: Masaru attends the first Council of Dragons, quite possibly his "
            "first -- Hestaby cannot recall having had cause to encounter him before -- taking the "
            "third eastern quarter of the circle almost exactly between the feuding Lung and Ryumyo. "
            "He shows more composure than his elders, though his eyes glow with an eagerness Hestaby "
            "finds oddly disturbing. He glances at the other two easterns and then rears up with them "
            "for the Rite of Succession: 'Let this be settled honorably,' he says gravely, and Hestaby "
            "restrains a chuckle at the idealism of the young."
        ),
        "notes_append": (
            "Survival of the Fittest: described in Dealing with Dragons (p.17) as an eastern great "
            "dragon associated with rebel factions in the Philippines, fairly young by great dragon "
            "standards and fiercely dedicated to his ideals, which primarily involve protecting 'his' "
            "islands from outsiders including the Empire of Japan. He plays no active part in the "
            "campaign beyond the two Council scenes, and handing him the essence of the Jewel of "
            "Memory at the Endgame is one of the choices the other dragons reject outright -- the Rite "
            "is either declared invalid and begun again, or awarded to the runner-up, Lofwyr."
        ),
    },
    "Arleesh": {
        "background_append": (
            "Survival of the Fittest: Arleesh attends the first Council of Dragons among the feathered "
            "serpents, near Hualpa and Mujaji -- Hestaby suspects she and Mujaji are the only other "
            "females who will appear, and notes that feathered serpents tend to congregate with their "
            "own kind. When the circle turns to her she shakes her head somewhat sadly and sides "
            "against the Rite: 'I cannot support the need for the Rite when there is so much else to "
            "be done.'"
        ),
        "notes_append": (
            "Survival of the Fittest: Dealing with Dragons (p.17) describes her as a female great "
            "feathered serpent, more active in mortal affairs than Mujaji and fairly young by dragon "
            "standards, devoted to protecting the world against Awakened threats the young races are "
            "not yet aware of and not prepared to handle -- which is exactly why she votes for getting "
            "on with the work instead of holding a contest. No further role in the campaign."
        ),
    },
    "Wu Lung-Wai": {
        "notes_append": (
            "Survival of the Fittest: Dunkelzahn's will left him the Jade Dragon of Wind and Fire, and "
            "he used the statue's magical properties to intensify the power site on which Wuxing's "
            "Hong Kong headquarters was built. The Wuxing Skytower has been drawing increasing amounts "
            "of chi ever since, Wuxing's star has risen with it, and the side effects -- warped magic "
            "across Hong Kong, disrupted dragon lines, and possibly the disasters that struck Japan -- "
            "are what bring Hestaby and Buttercup into Balance against him. He never appears on-screen; "
            "Buttercup's one stated preference is that he never learn of her involvement in the "
            "rebalancing. DISCREPANCY: this book spells the name 'Wu Lung-Wei' throughout (pp.63, 78). "
            "The existing row's spelling is left as it stands."
        ),
    },
    "Kenneth Brackhaven": {
        "notes_append": (
            "Survival of the Fittest: Joshua Keller -- later Brother Joshua Morningstar of the "
            "Children of the Dragon -- campaigned for Dunkelzahn early in the '57 election and was "
            "dismissed from the campaign for using violent methods to advance the dragon's cause and "
            "hinder his opponents, Brackhaven in particular. The book names him 'Arch-Conservative "
            "candidate Kenneth Brackhaven' (p.47)."
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
Three systems are mapped in the campaign. None are built by this loader.

**1. Shasta Lodge mainframe** (p.30). Rated **Red-9/13/11/13/13/13**. Access to it lets a decker take
the site's security system with a successful Control Slave operation, overriding the cameras and the
maglocks.

| Step | Event |
|---|---|
| 2 | Crippler (jammer)-10 |
| 4 | Tar Pit-8 (Armor) |
| 7 | Crippler (marker)-8 (Expert Offense-1) |
| 9 | Passive Alert |
| 12 | Probe-10 with trap Sparky-10 with trap Black-8 |
| 16 | Construct-11 with trap Blaster-11 |
| 20 | Killer-10 with trap Killer-10 |
| 24 | Active Alert |
| 27 | Crippler (acid)-8 (Shielding) |
| 31 | Lethal Black IC-11 |
| 34 | Killer-10 (Shifting) with trap Black-8 |
| 37 | Non-Lethal Black IC-8 |
| 39 | Psychotropic Black IC (positive conditioning)-8 |
| 43 | Shutdown |

**Shasta Lodge isolated data store** (p.30): reachable only by an on-site decker, or by physically
wiring the unit to the mainframe (about a minute and a Computer (4) Test). The Kallisti file is 500 Mp
behind **Scramble IC-8**. Same security sheaf as the mainframe except that it shuts down at step 20.
The whole unit weighs about 10 kilos -- delicate and unwieldy, but carryable, which is the book's own
fallback for a team that cannot beat the IC. The file itself is worthless nonsense text, as is
everything else in the system.

**2. Children of the Dragon temple host, Denver** (p.40). Rated **Orange-7/12/14/14/11/12**.
Morningstar's personal files are protected by a **Rating 5 Data Bomb** and only he has the passcodes;
the files the runners need total 150 Mp. Goldwing can supply access codes to everything except the
highest-security areas and systems.

| Step | Event |
|---|---|
| 3 | Tar Baby-7 (Armor) |
| 8 | Probe-9 with trap Black-7 (Armor) |
| 11 | Tar Pit-5 (Armor) |
| 14 | Killer-5 (Shielding) |
| 18 | Tar Pit-9 (Shifting) |
| 21 | Probe-5 with trap Black-10 (Armor) |
| 26 | Passive Alert |
| 29 | Ripper (bind-rip)-7 (Shifting) |
| 32 | Crippler (acid)-9 (Armor) |
| 37 | Ripper (acid-rip)-7 (Shifting) |
| 41 | Sparky-5 (Armor) |
| 44 | Sparky-5 (Shielding) |
| 49 | Sparky-7 with trap Sparky-9 |
| 54 | Active Alert |
| 59 | Ripper (bind-rip)-7 (Cascading) |
| 62 | Scout-7 (Armor) |
| 65 | Non-Lethal Black IC-5 |
| 68 | Crippler (binder)-5 |
| 72 | Lethal Black IC (cyberphobia)-7 |
| 76 | Shutdown |

**3. Wuxing Skytower host, Hong Kong** (p.75). Rated **Red-10/15/18/16/16/18**. A decker can use it to
beat the executive elevator's passcode (Logon to Host, then Locate Slave, then Control Slave or Edit
Slave) or to suppress the stairwell alarm and the exterior cameras. The sheaf is printed in a sidebar
whose step numbers are lost in the OCR; the order of the IC survives, the trigger steps do not.

| Order | Event |
|---|---|
| 1 | Scout-8 (Cascading) |
| 2 | Trace-8 (Shifting) |
| 3 | Crippler (binder)-10 (Shifting) |
| 4 | Crippler (jammer)-8 (Armor) |
| 5 | Passive Alert |
| 6 | Ripper (jam-rip)-6 (Armor) |
| 7 | Killer-12 (Armor) |
| 8 | Blaster-8 (Party Cluster) |
| 9 | Sparky-6 (Shifting) |
| 10 | Active Alert |
| 11 | Psychotropic Black IC |
| 12 | Cerebropathic Black IC-6 |
| 13 | Scout-10 (Cascading) |
| 14 | Crippler (jammer)-8 (Shifting) |

**Not mapped**: the Children of the Dragon door and window alarm circuit; the Shasta Lodge camera and
maglock subsystems (slaved to the mainframe); the forged evidence chain in Morningstar's telecom
records (Computer (6) to detect tampering); Sen Lo's client-record chips (Computer (4)); the Yamatetsu
and Aztechnology systems that identify the runners at Vladivostok's port of entry; and the Matrix
searches used to identify Buttercup (Computer (6) from memory) and to confirm that the Silver Songbird
appears in Dunkelzahn's will (Computer (4)).
"""

NOT_BUILT = """
- **The European gargoyle, the kludde and the naga** of Rhonabwy's hunt -- three of the six hunters,
  fully statted at pp.91-92 but never named; their stat blocks and tactics sit on the Rhonabwy's Wild
  Hunt org row.
- **The old shaman** of the nameless Amazonian village, **the four native hunters** who meet the
  runners, and **the feathered serpent** Hualpa sends to collect the scrolls -- all unnamed; folded
  into the village location row and Hualpa's row.
- **The mad merc** outside Tehran (the wraith's used-up puppet, statted p.95), **Akimura's twin elven
  bodyguards** (Adept sample character, SR3 p.55), **the traitor in Cap'n Fixx's crew**, **the pirate
  band** Grin runs with, **the Macapan street toughs** Ocelopan hires, **Ocelopan's security agents
  and boat crews**, **the Wuxing security guards and wujen**, **Yoshida's Yamatetsu company men**,
  **the Red Dragon soldiers**, **the Children of the Dragon temple guards**, **the Denver border
  guards**, **the Shasta Lodge security guards and shamans**, **Musa Muqla's followers** and
  **Donelley's four men** -- stat blocks carried on the relevant org and location rows.
- **The shedim**, **Tehran's ghouls, harpies and devil rats**, **the refugee squatters**, and the
  **Sangre del Diablos** -- creature stats on the Ruins of Tehran and Nameless Village rows.
- **Schwartzkopf** and **Kaltenstein**, the two named great dragons absent from the Council, and the
  **rival sea dragon of Cardigan Bay** legend gives Rhonabwy -- name-drops with no role.
- **The artefacts themselves** -- the Jewel of Memory, the Elemental Scrolls of Ak'le'ar, the Silver
  Songbird, the Shroud of Shadows, the Jade Dragon of Wind and Fire, the Second Coin of Luck, the Ring
  Ouroboros and the fourth unaccounted-for Coin of Luck. Described in full on the location and NPC
  rows that stage them; they are items, not rows.
- **The Nexus** data haven, the **New Islamic Jihad**, the **Atlantean Foundation**, **General
  Saito**, the **Pueblo Security Forces**, the **Carib League**, the **Scatterbrains** and **Red
  Rovers** go-gangs, **Yamatetsu's Popov Island worldwide headquarters**, **Brown University**, the
  **University of Virginia** and **MIT&T** -- name-drops.
- **The Rubber Suit's hearth spirit** (a man in a bad rubber monster suit with Innate Spell
  (Flamethrower)) and **the lodge hearth spirit** -- on their location rows.
- **The rigger who flies Yoshida's Northrup Wasp** and **the local fixer who hired him** -- unnamed
  by design, with enough layers of deniability that the runners can never trace them back.
- **The Places of the metaplanes** (Battle, Charisma, Destiny, Fear, Knowledge, Magic, Spirits) -- the
  book gives sample challenges rather than fixed locations, and expects the GM to invent the rest; see
  PLAY_NOTES.
"""

PLAY_NOTES = """
- The one rule that makes the whole campaign work: a great dragon may not directly attack another
  dragon's chosen agents unless those agents attack first, though any dragon may defend itself, and
  agents may freely go after each other. Hestaby spells this out at the Lore briefing; before that,
  the players should be feeling it without knowing it. It is why Rhonabwy offers a hunt instead of a
  killing, why Aden is bluffing, and why Lofwyr can only make offers at the Citadel.
- Seven adventures, each self-contained with its own Mr. Johnson. Knowledge should come first; the
  middle five (Cunning, Elements, Balance, Hunting, Rest) can be run in any order, and Lore must come
  last. Time between them is deliberately vague, and the book encourages inserting unrelated runs so
  the players cannot tell which jobs are part of the Rite.
- Do not let the players fight a great dragon. None of them have statistics -- they are 'more akin to
  an elemental force'. Ghostwalker eats a runner who defies him; Rhonabwy turns one into a toad and
  drops it after making his point; Lofwyr simply kills anyone who attacks him in the metaplanes; Aden
  cannot strike first but everything else about him is lethal.
- Radek is the spine. He is a genuine fixer who does not know who he is really working for, which
  means Analyze Truth, Mind Probe and the runners' contacts all come up clean. Keep him warm, keep
  him professional, and let the players' growing suspicion be the campaign's slow burn.
- The runners are being tested in Knowledge and everything after it is Hestaby cashing in. Killing
  unnecessarily costs them her esteem and changes how she treats them at the Endgame -- flag that
  early, not at the end.
- Denver is the one adventure where the players can see the shape of the manipulation. Reward a team
  that runs the Computer (6) Test on Morningstar's files and tells Ghostwalker the evidence is
  planted: it is worth a Karma point and it is the correct read.
- Elements is a wilderness adventure for city characters. Make sure the group has some survival
  skill, a shaman and some magical muscle; a decker is only minimally useful, so give them something
  to do or lean on the Avoiding Deadweight advice (p.115) about re-skilling characters later.
- Balance rewards patience: five days to plan the Skytower and a hard midnight deadline, and the
  break-in must not be so early that Wuxing notices and corrects the feng shui first. The penthouse
  is a Rating 8 power site giving Awakened characters 8 extra dice per Combat Turn -- an enormous
  temptation and an enormous risk, since wrecking the chamber wrecks the plan.
- Hunting is a chase, not a dungeon. The tracking bug in the Songbird's cage is the whole puzzle, and
  the C-12 under it is the punishment for not looking. Drop hints ('you don't know how they keep
  finding you') rather than solving it for them. Spirits are forbidden to both sides. Silver from the
  cage wire is the counter to Volk.
- Rest is the one adventure where fighting makes things worse: every death feeds the wraith and drains
  the runners' Karma permanently until the wraith is destroyed rather than merely disrupted. Reward
  non-violent handling with a Karma point and make the Shroud's aversion visible before the players
  have to guess.
- Lore is a different game. Change the runners' identities Place by Place -- fantasy characters,
  animals, dracoforms, historical figures -- so that the decker and the rigger are not deadweight, and
  keep every challenge thematically about dragons, tradition versus change, and the runners' own place
  in the Rite. Stun damage clears between Places; smart teams will notice and heal in transit.
- The Endgame has no wrong answer. Hestaby returns the Jewel to Lofwyr and refuses the title; Lofwyr
  confirms his authority and warns off future challengers; Ghostwalker claims everything Dunkelzahn
  willed away; a neutral dragon is accepted as a compromise; an extreme one voids the Rite; destroying
  the essence means nobody is Loremaster; splitting it creates a real council. A genuinely clever plan
  is worth an extra Karma point.
- Karma by adventure: Knowledge 1/1/1/1 (survive, the file, undetected, no unnecessary casualties);
  Cunning 1/1/1/1 (survive, Morningstar alive, the data, spotting the frame-up); Elements 1/1/1/1
  (survive, scrolls delivered, MCT handled, Aztechnology handled); Balance 1 + Sen Lo + 2 (the Karma
  table prints no value for delivering Sen Lo); Hunting 1/1/2/1 (survive, reach the Songbird, deal
  with the hunters, find the explosives); Rest 2/1/1 plus either 1 for the Shroud or 2 for getting
  Aden to claim it; Lore 1/2/1 (survive, complete the quest, decide well), plus a 2-4 point bonus for
  the campaign as a whole.
- Loose ends: Sappho and Radek as standing fixers; Branwen and Rhonabwy as future employers; Hilde,
  Cap'n Fixx and Akimura as travel contacts; Sen Lo as a geomancer who owes them; Hualpa's offer to
  clear Ocelopan's people out of Macapa; Musa Muqla and the Shroud; Yoshida's grudge; and a handful of
  great dragons who now know the runners' faces and cannot touch them -- yet.
"""
