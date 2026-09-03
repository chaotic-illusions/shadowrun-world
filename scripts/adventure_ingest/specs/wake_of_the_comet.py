# Wake of the Comet (FanPro 10654, 2002, SR3) -- campaign order #37. An anthology of three linked
# adventures hung on the second leg of the megacorp "Probe Race" to Halley's Comet: The Messenger
# (French Guiana / Iles du Salut, Brian Schoner), Catch a Falling Star (Seattle-Everett, Thunder Bay,
# La Ronge and the Manitou secession north of the Churchill River; Davidson Cole, Andy Frades and
# Rich Tomasso) and The Price of Liberty (Cape Canaveral, the Apollo habitat, Silicon Valley and New
# Orleans; Michelle Lyons and Malik Toms).
# Dating: The Messenger "can really take place anytime in the year 2061 or the first few months of
# 2062" (p.8); Catch a Falling Star's second hire is "some time in early May 2062" (p.34) and follows
# Halley's perihelion; The Price of Liberty's player handout is datelined "Posted 02-10-62" (p.83).
# YEAR is therefore 2062. NOTE the book's own ordering inconsistency: printed third, The Price of
# Liberty is dated February 2062, three months BEFORE Catch a Falling Star's module recovery in May.
# Run them in print order and treat the handout date as loose, or swap the last two.
# Other editing inconsistencies noted on the affected rows: the Knight Errant stat block on p.72 is
# headed "Knight Errant Eagle Shaman" but its totem line reads Owl; Proteus' arkoblock is "usually
# said to be located on Devil's Island" but actually spans all three Iles du Salut; the Catch a
# Falling Star Johnson is never given a name (this spec files him under a disambiguated one and says
# so on the row); the Manitou councillor list on p.49 numbers five "including the chief" but names
# five besides Youngman if Cloud Talon and Thunderwalker are counted, and the text is explicit that
# those two are NOT councillors; The Price of Liberty's Karma table values are lost in the OCR, as
# are several attributes (Thunderwalker's Essence/Reaction, Cloud Talon's Essence, Griebe's Body,
# the SMART mage's Quickness, Natalie Dark's Intelligence, Mercy's full stat line is intact but her
# Karma/Professional 8/2 looks like a typo for 8/4) -- reference the book for those.
# Source text: docs/Adventures/text/Shadowrun 3e - Wake Of The Comet {FanPro10654}.txt (90 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "Wake of the Comet"
ORDER = 37
SOURCE = "Shadowrun 3e - Wake Of The Comet {FanPro10654}.pdf, pp. 4-85"
YEAR = "2062"

SYNOPSIS = """
Halley's Comet came back in 2061 and the megacorps raced to touch it. The first leg of the **Probe
Race** ended in humiliation -- every highly publicized probe fell to sabotage, accident or unexplained
mishap, and only Yamatetsu's **Gagarin** got close before contact was lost. The comet has rounded the
sun and will make one last pass by the Earth on its way to deep space. There will be no more chances,
so the surviving corps are scrambling their probes into place, guarding them, and quietly wrecking
each other's. Three runs fall out of that scramble, and they take the team from the equatorial jungle
to low Earth orbit.

**The Messenger.** At Proteus AG's half-submerged arkoblock on the **Iles du Salut** off French
Guiana, the telemetry specialist **Gunther Hoff** loses the fight to put his instrument package aboard
the probe **Gotterbote** and decides that if the arrogant project lead **Dr. Heinrich Hausmann**
simply disappeared for ten days, the corporation would have to use Hoff's design instead. He hires the
runners over an anonymous Shadowland account, flies them to Cayenne, rents them a bungalow in Kourou
and points them at Hausmann's 0630 jog on Devil's Island -- or, failing that, at a dinner party at his
own house. Hausmann barely resists. The unmarked drone hovering overhead does. Hausmann is a deep-cover
**Winternight** agent whose payload is a nuclear bomb meant to knock Halley off course and into the
Earth, and his cult finds him inside a day by the transmitter in his Proteus ring and by ritual
tracking, tips Proteus off anonymously, and sends a strike team through the safe house windows. Then
"Hoff" calls a meet at the derelict **Sporting and Aero Club**: the man at the drained pool is the
toxic Raven shaman **Anderson** wearing Hoff's face, with two drones, three razorboys and a great deal
of money. Whatever happens there, the clues lead back to Hoff's house, his corpse, an accidentally
running telecom that recorded his murder and the cult's plan, and a police cordon Anderson called in
to close the case over the runners' bodies. Get the recording to Proteus or stop the launch yourself.

**Catch a Falling Star.** Gagarin is not dead. In early 2062 it burst-transmits home, crippled, its
sensor data locked in a module it is programmed to drop on its Earth flyby -- and it is off course.
Yamatetsu buries the news; the traffic gives it away. A gnarled, squeal-voiced **Mr. Johnson** hires
the team over banana splits at **Lickety-Splits Old Fashioned Ice Cream** to break into **Alaxa**, a
quiet Yamatetsu biotech front in Everett, and ride its one-minute hourly satellite burst up to the
Shibanokuji PLTG for the Gagarin files. Weeks later he calls them to **The Pines Club** in Thunder
Bay: the module is down in the anti-technology **Manitou** secession north of the Churchill River, and
whoever pays him wants it recovered, wiped, corrupted or destroyed. The crash trench is empty, the
Yamatetsu recovery team that beat them there is six frozen corpses in an ambush hollow, and a Force 7
wind spirit guards the tracks northeast. They lead to **Niwimaja**, where medicine man **Cloud Talon**
has buried the module in a warded crate under the permafrost and the whole town is quietly at war
about it. Guns lose here; the run is a council-politics brawl fought with Chief **Youngman**, the
militia leader **Thunderwalker**, the ambitious Eagle shaman **Mawnee Eaglefeather** and four other
factions -- and then a second, better Yamatetsu team walks in and everything is bid again. And if
anyone ever cracks the module: the intact readings show no comet at all, but another craft keeping
pace inside the coma, taking on returning sample drones. Somebody won the Probe Race first, in secret.

**The Price of Liberty.** **Dr. Sherman Royce** writes guidance code for AresSpace's twin **Velox**
probes and lives under twenty-four-hour Knight Errant guard in a Silicon Valley office park he cannot
leave. He wrote a remotely triggered virus called **Liberty** into both probes, sold the first one to
the Kepler consortium, and now needs three favors. The Seattle fixer **Annika Griebe** -- who takes no
job that benefits Ares -- hires the team at the changeling club **Vertigo** for a 48-hour trip to the
**Apollo** habitat to spacewalk out and re-key a backup relay. Velox I dies a day after they land.
Then the extraction: through Saito's checkpoints, over a Barrier 16 wall past a city spirit and two
Ares drones, down three sublevels to Building C, and out to New Orleans. There the talismonger
**Mercy** takes them in, Royce admits he was the Johnson all along, and he auctions the last Liberty
code on Asgard. At the **Etienne Shipyards** the buyer's negotiator offers to double their pay and
grant them protection for one address -- while the losing corp's team closes in, Griebe's own runners
watch from the swamp with orders to recover ten million nuyen at all costs, and nobody leaves the boat
graveyard without a fight.
"""

TIMELINE = """
- **2061** -- Halley's Comet returns; the megacorps' Probe Race begins and its first leg collapses in
  sabotage and mishap. Yamatetsu's Gagarin alone reaches the comet, then goes silent right before
  close sensor range. Ares' Gigas is lost to an asteroid strike.
- **2043-2061 (Winternight's long game)** -- targeted scientific training and referrals from highly
  placed cult puppets steer Heinrich Hausmann into a crucial role on Proteus' Halley probe projects.
- **2061 or early 2062 -- The Messenger, Day 0** -- Gunther Hoff loses the payload argument with Emil
  Verdan, hires the runners in a rented virtual conference room, and sets the launch ten days out.
- **Day 4 before the deadline** -- the team lands at Rochambeau Airport, Cayenne; Bala's gun deal at
  the fishing village that night; the Kourou bungalow.
- **Day 7 at the latest** -- the grab: the 0630 Devil's Island jogging trail, or the dinner party at
  Hoff's house. Hausmann's Winternight drone intervenes either way.
- **Within 24 hours of the abduction** -- Winternight fixes Hausmann by his Safe Target ring and by
  Ritual Tracking, tips Proteus anonymously, and the rescue squad hits the safe house behind flash and
  Neuro-Stun grenades. A day or two later Anderson breaks Hoff, dictates the phone call and shoots him.
- **Midnight that night** -- the Sporting and Aero Club meet; then Hoff's house, the recording, and the
  police-and-Proteus cordon. **The morning after** -- the Gotterbote launch, with or without the nuke.
- **Early 2062, after perihelion** -- Gagarin burst-transmits to Yamatetsu; Saru Iwano orders total
  secrecy and round-the-clock work. Rival corps notice the traffic.
- **Weeks later -- Catch a Falling Star, run one** -- the Lickety-Splits meet; the Alaxa break-in and
  the one-minute Shibanokuji uplink; 48-hour delivery bonus.
- **A week's notice, then early May 2062 -- run two** -- the module drops off target into Manitou land.
  The Thunder Bay meet at The Pines Club; the flight to La Ronge; the crossing of the Churchill River.
- **Two hours after the crash** -- Yamatetsu's first team lands; local Manitou have already taken the
  module to Cloud Talon; Thunderwalker's elites wipe the team out and set a wind spirit on the trail.
- **1D6 hours of searching later** -- the runners reach the crash trench, then the ambush hollow, then
  Niwimaja. Mawnee starts spreading dissent the day they arrive.
- **Less than a day after that** -- the second Yamatetsu team touches down and approaches the town,
  smooth or hostile; the council contest; Pierre O'Rourke's ambush outside the "friendly confines".
- **Months later** -- whoever holds the module breaks the encryption and finds the unidentified craft
  inside the comet's coma.
- **02-10-62 (the handout dateline) -- The Price of Liberty** -- the Vertigo meet, the Cape Canaveral
  shuttle, 48 hours on Apollo, the spacewalk and the relay chip. Velox I veers off course 24 hours
  after the runners come down; Velox II is projected to intercept Halley in about a month.
- **A day later** -- Griebe's dropbox job: the AresSpace Silicon Valley extraction and the run to New
  Orleans. **Then 72 hours** at Mercy's while the Liberty code goes to auction on Asgard (bids due in
  48 hours), Griebe's team shadowing the runners the whole time.
- **The following evening** -- the Etienne Shipyards exchange, the pitch, and the three-way ambush.
- **After** -- Shibata's Kepler wins the Probe Race if it gets the code; Ares' Velox II wins if Ares
  does; if neither, a shadow war between them while the race runs on.
"""

ORGS = [
    {
        "name": "Winternight",
        "org_type": "cult",
        "tier": 3,
        "headquarters": "None -- clandestine cells; the French Guiana cell works out of Kourou",
        "summary": "Nordic-myth apocalypse cult of toxic shamans and deep-cover sleepers working to bring on Ragnarok and earn its members places in the pantheon that will rule the reborn Earth",
        "description": (
            "A cult with spiritual beliefs based in Nordic mythology that seeks to bring about Ragnarok -- "
            "the end of the world -- so that its members can earn their place in the pantheon of Nordic "
            "deities that will once again rule the Earth. It is organized into clandestine cells that each "
            "work towards that task independently, so that no cell knows enough to compromise the rest. "
            "Many of its members are toxic shamans, followers of Raven or Wolf. The cult makes heavy use of "
            "custom-built untraceable drones and of BTL-programmed deep-cover agents inserted into corporate "
            "science by years of arranged training and referrals from other highly placed puppets. It avoids "
            "the Matrix altogether, considering it a tool of the trickster god Loki, and works by ritual "
            "sorcery, anonymous tips and hired local muscle who have no idea who they serve."
        ),
        "notes": (
            "Detailed in the (out of print) Threats sourcebook. The Guiana cell: Anderson (toxic Raven "
            "shaman, cell leader), Howe (rigger, the only non-shaman who knows the employer), Hausmann "
            "(deep-cover Proteus scientist), and the razorboys Ein, Zwei and Drei, who are paid in nuyen, "
            "cyberware and BTL chips and think their boss's mutterings about destroying life on Earth are a "
            "joke. The plan: Hausmann loads a Winternight drone into the Gotterbote payload before launch, "
            "guides the probe to a soft landing on Halley, positions it and detonates its payload -- a small "
            "but powerful nuclear bomb intended to knock the comet off course into the Earth. Unlike most "
            "toxics, Winternight shamans cooperate: a GM may pool their Potency ratings and distribute the "
            "pool among them each Combat Turn. The cult does not normally pursue revenge -- too much risk of "
            "exposure -- but will hire outside guns to silence anyone who knows too much or foiled the plan. "
            "If Anderson's cell is wiped out, no one else in Winternight knows enough about Gotterbote to "
            "carry the vendetta on."
        ),
        "enemies": ["Proteus AG"],
    },
    {
        "name": "Manitou Tribe",
        "org_type": "tribe",
        "affiliation_contact_type": "Tribe",
        "tier": 3,
        "headquarters": "Manitou territory north of the Churchill River; Niwimaja is one of its towns",
        "summary": "Manufactured, mostly-elven, anti-technology tribe that has seceded from the Algonkian-Manitou Council, seized everything north of the Churchill River, and is trading border clashes with the AMC army",
        "description": (
            "A manufactured tribe, originally formed as an all-elf grouping but open to all metatypes. Many "
            "members come from other ethnic tribal groups -- the warlike and territorial Cree, the peaceful "
            "but fiercely anti-technology Montagnais, the wandering Naskapi who cling to the old ways -- and "
            "others are so-called pinkskins. It has declared independence from the Algonkian-Manitou Council, "
            "seized all land north of the Churchill River and removed many people from that territory; border "
            "clashes with the AMC military are constant and the region is on the verge of civil war. Its "
            "towns are rebuilt on permaculture principles: roads dug up and reclaimed as footpaths, gardens "
            "where the parking lots were, solar and windmill power at best, prefab geodesic domes and skin "
            "tents around a small permanent core. To many natives this is the old days of activism come "
            "again; to Aztechnology and the AMC elite the Manitou are troublemakers driving the country "
            "toward war."
        ),
        "notes": (
            "Governance: an elected tribal council of five including the chief, some with hereditary claims "
            "for their own tribe; few sessions are closed and the unofficial medicine man and militia leader "
            "attend by right. Above the local council sits a Manitou Inner Council and other tribal "
            "authorities that Cloud Talon pointedly declines to involve in the module affair. Militia (also "
            "the local police): B4 Q5 S4 C4 I3 W4 E6 R4, Init 4+1D6, Combat Pool 6, Karma/Prof 1/3, elf; "
            "Assault Rifles 4, Biotech 3, Edged Weapons 3, Projectile Weapons 2 (Pull Bow 4), Stealth 4, "
            "Thrown Weapons 4; AK-97, bow 6M, knife, spear, armor vest 4/2. Over 500 people are in and about "
            "Niwimaja, mostly armed and intimately familiar with the terrain, and they run regular border "
            "patrols. Anti-tech bias: obvious cyberware means social modifiers at +1, gearheads get lectured, "
            "vehicles stay outside town and fossil-fuel burners get quietly sabotaged. Languages: Algonkian "
            "or Cree mostly, plus Naskapi, Montagnais and some Sperethiel; all the leadership speaks English "
            "but official business is conducted in a tribal language. Founders included Chief Youngman, once "
            "a protege of Adrian Silvermoon and later one of those who ousted her."
        ),
        "enemies": ["Algonkian-Manitou Council", "Aztechnology"],
    },
    {
        "name": "Algonkian-Manitou Council",
        "org_type": "nation-state",
        "tier": 5,
        "headquarters": "Thunder Bay is its economic center; military deployed along the Churchill River",
        "summary": "Native American nation coming apart at the seams: its Manitou tribe has seceded northward, its army holds the river line, and Aztechnology is widely believed to be the real power behind its government",
        "description": (
            "A Native American nation of the northern woods whose government is losing control of its own "
            "north. The mostly-elven, anti-technology Manitou have declared independence and seized "
            "everything above the Churchill River; AMC troops now guard that line to stop Manitou sabotage "
            "missions and to keep aid from reaching them, while the Manitou watch for an invasion, mine or "
            "destroy the bridges and heavily guard the rest. Aztechnology holds significant clout inside the "
            "AMC -- some think it is the power behind the throne -- and the Manitou expect an AMC invasion "
            "backed by Azzie money. The economy runs through Thunder Bay, a major smuggling port and the "
            "country's commercial heart; smaller northern towns such as La Ronge have been reshaped overnight "
            "by the secession, filling with resentful newcomers and quiet sympathizers alike."
        ),
        "notes": (
            "Background reading the book cites: the Algonkian-Manitou Council chapter of Shadows of North "
            "America. The AMC is big and there are lengthy stretches of unmonitored border; the runners "
            "should have tense moments crossing but no real trouble, fording one of the river's wide shallow "
            "stretches or walking across the ice. AMC army, Manitou patrols or Aztechnology forces all serve "
            "as optional hostile border encounters, and neither side pursues over the line. Elven characters "
            "of tribal ancestry may get cold shoulders in Thunder Bay from anyone the secession hurt. A "
            "runner team fleeing Niwimaja with the module can expect trouble from AMC military, Aztechnology "
            "troops, or corporate rivals who mistake them for Yamatetsu."
        ),
        "enemies": ["Manitou Tribe"],
        "allies": ["Aztechnology"],
    },
    {
        "name": "French Guiana",
        "org_type": "nation-state",
        "tier": 4,
        "headquarters": "Cayenne (capital); Kourou is the corporate town",
        "summary": "Equatorial French protectorate surrounded by Amazonia on three sides, poor and barely policed, whose only real asset is a launch latitude that Saeder-Krupp, Proteus and Novatech all pay for",
        "description": (
            "Often called simply Guiana now that the neighboring Guyana has been swallowed by Amazonia. It is "
            "one of the few pieces of northern South America Amazonia has not conquered, surrounded by it on "
            "three sides with the Atlantic on the fourth -- not for lack of interest or any strength of "
            "Guianan arms, but because Guiana is a protectorate of France and Amazonia will not take on "
            "Europe over a hundred thousand square kilometers. Physical resources are minimal: subsistence "
            "agriculture, forestry and gold mining. The country's one real asset is that it sits almost "
            "directly on the equator, ideal for launching into geostationary orbit. The population splits "
            "hard between a small wealthy, highly educated corporate class at the aerospace facilities and "
            "poor, uneducated masses on the farms, in the lumberyards and down the mines -- with rampant "
            "crime, alcoholism, drug and chip use below, and a lot of resentment aimed upward that the "
            "well-defended corporate compounds simply absorb."
        ),
        "notes": (
            "Matrix search TN 4 gets all of the above. The nation is not security-conscious; the only "
            "significant national industry revolves around Saeder-Krupp's and Proteus' space programs, which "
            "are responsible for their own security, and Cayenne customs treat anyone the UCAS let on a plane "
            "as harmless. Aerospace holdings: Proteus' offshore arkoblock at the Iles du Salut, the former "
            "European Space Agency base at Kourou now owned by Saeder-Krupp, and a massive Novatech launch "
            "complex going up outside Cayenne. French is official but most people speak a French-Amerindian "
            "creole and English is widely spoken. Yellow fever and rabies are fairly common, vaccinations "
            "recommended; avoid local milk and dairy and stick to bottled water outside the cities. The one "
            "public hospital of any size is in Cayenne -- overcrowded, understaffed and suspicious of "
            "tourists with gunshot wounds; a shaman in the slums will heal for money."
        ),
        "allies": ["Saeder-Krupp Heavy Industries", "Proteus AG"],
    },
    {
        "name": "Kourou Police",
        "org_type": "government agency",
        "tier": 2,
        "headquarters": "Kourou, French Guiana (municipal jail attached)",
        "summary": "Undertrained municipal force with no SWAT capability that leans on Saeder-Krupp's corporate security whenever anything worse than a bar fight happens",
        "description": (
            "The government-managed police force of Kourou: officers who patrol in pairs in a General "
            "Products COP, answer loud noises in 1D6 minutes, and are frankly not prepared to deal with a "
            "team of shadowrunners. The city has no SWAT teams to speak of. What it does have is a good "
            "working relationship with Saeder-Krupp's local security teams, who are far more experienced "
            "with such individuals and arrive about 1D6 minutes behind the first patrol cars with two more "
            "police cars in tow. Anyone the police take is held in the Kourou jail only until morning, when "
            "prisoners wanted by the corporations are handed over -- Proteus collects its own suspects and "
            "takes them out to the arkoblock's small jail for 'processing'."
        ),
        "notes": (
            "Officers p.22: B4 Q4 S4 C3 I4 W3 E6 R5, Init 3+1D6, Combat Pool 5, Karma/Prof 1/2, human; "
            "Interrogation 3, Intimidation 4, Pistols 4, Shotguns 4, Unarmed 4; Kourou 5, Police Procedure "
            "4; Defiance T-250, Fichetti Security 500, armor jacket 5/3, micro-transceiver, two sets of "
            "plastic restraints. Two cars respond to gunfire at Hoff's house in 1D6 minutes and 2D6 out at "
            "the derelict Sporting and Aero Club; heavy backup is called if the runners look heavily armed. "
            "Eight officers plus a Proteus strike team make the Face to Face cordon, called by a Winternight "
            "drone playing back a faked emergency call in Hoff's voice -- Anderson wants them to shoot the "
            "runners so the case closes with no witnesses. Optional upgrade (p.22): the city finally gives "
            "up on a public force and contracts security to Knight Errant or a Saeder-Krupp subsidiary."
        ),
        "allies": ["Saeder-Krupp Heavy Industries", "Proteus AG"],
    },
    {
        "name": "Alaxa",
        "org_type": "corporation (biotech)",
        "tier": 2,
        "headquarters": "Two-story facility in Everett, Seattle metroplex",
        "summary": "Small, deliberately unglamorous Everett bioware research firm secretly owned by Yamatetsu, sharing zero-g data with Shibanokuji over a dedicated satellite uplink",
        "description": (
            "A relatively new biotech firm with a crappy little office in Everett that looks about as high "
            "tech as a mattress factory. It works mostly on research and theory rather than implementation, "
            "predominantly cultured material: new bioware designs and stress reduction. Part of that work "
            "involves sharing data with Yamatetsu's zero-g bio lab aboard the Shibanokuji orbital station -- "
            "and that lab happens to sit on the same PLTG as Yamatetsu's other classified space projects, "
            "the Gagarin mission included. Yamatetsu owns Alaxa outright but has been very quiet about the "
            "investment, hoping anonymity will provide security; the trail is well hidden but the connection "
            "is definitely there for anyone who digs. Because that ownership is concealed, Alaxa's property "
            "does not enjoy extraterritoriality, and it hires off-duty Lone Star officers rather than "
            "Yamatetsu guards to keep the public distance."
        ),
        "notes": (
            "Legwork (Corporate TN 4, Matrix TN 4, Medical TN 5, Street TN 6): 1 new biotech in Everett; 2 "
            "research and theory, cultured stuff; 3 a lot of money to throw around for a new corp, the "
            "backers are Asian; 4 a contract with one of the AAAs on applications of biotech developed in "
            "zero-g labs; 5+ Yamatetsu owns them. Staffing: three guards on site at a time (two if the mage "
            "Alice Hernandez is also on site), extra guards after any unexplained incident. Guards are "
            "overworked off-duty cops -- B4 Q5 S4 C4 I4 W4 E5 R4, Init 4+1D6, Combat Pool 6, Karma/Prof 3/3, "
            "Pistols 5, Brawling 4; Defiance Super Shock taser, splatgun, HK 277, armored coat 2/1, "
            "PanicButton -- who try to immobilize intruders and get Lone Star on the line the moment they "
            "realize they are facing shadowrunners. Low-level executive Charlie Davis and his secretary "
            "Marla Munns are usually the only staff in the building after 1700."
        ),
        "allies": ["Yamatetsu Corporation", "Lone Star Security"],
    },
    {
        "name": "Shibata",
        "org_type": "corporation",
        "tier": 4,
        "headquarters": "Japan; Kepler consortium operations with Aztechnology and Federated Boeing",
        "summary": "Japanese corp running the dark-horse Kepler probe with Aztechnology and Federated Boeing, and fielding SMART -- its Major Assets Recovery Team -- to buy or take the Liberty code",
        "description": (
            "One third of the joint Aztechnology / Shibata / Federated Boeing consortium behind Kepler, the "
            "dark horse of the Probe Race and the only probe left with a chance of beating Ares' Velox II to "
            "Halley. Shibata was the corp Sherman Royce's outside contacts pointed him at when he went "
            "shopping his sabotage virus, and it paid him a significant sum on delivery to derail Velox I. "
            "It is deeply invested in winning the race and is not willing to let the second Velox slip away: "
            "when Royce auctions the last Liberty activation code on Asgard, Shibata bids, and whether it "
            "wins or loses it sends people to New Orleans. If it ends up with the code, Velox II is doomed "
            "in short order and the corporate triumvirate scores a major publicity coup by rendezvousing "
            "with the comet first."
        ),
        "notes": (
            "SHIBATA MAJOR ASSETS RECOVERY TEAM (SMART), pp.79-80 -- led by Commander Colin Walton, a "
            "grizzled black-ops veteran and a troll leading inside a Japanese corporation on sheer skill. "
            "SMART mage: B5 Q? S3 C5 I6 W5 E6 M6 R5, Init 5+1D6, Astral Init 26+1D6, Karma/Prof 3/3; Sorcery "
            "6 (Spellcasting 8); Confusion 5, Detect Enemies 6, Firewall 5, Manaball 5, Physical Barrier 4, "
            "Physical Mask 4, Stunbolt 5; a Force 5 water (3 services) and a Force 4 earth elemental (2 "
            "services) on call. Four SMART members: B4 Q6 S5 C4 I5 W5 E6 R5, Init 5+1D6, Combat Pool 8, "
            "Karma/Prof 2/3; Demolitions 3, Electronics 5, Leadership 3 (Tactics 5), Shotguns 5; Enfield "
            "AS-7, Fichetti Security 500a, secure vest 3/2, one dose of jazz each. Recommended default: "
            "Shibata wins the auction and Ares crashes the meet. A SMART team may also be seen working the "
            "New Orleans streets asking questions about Mercy before the exchange."
        ),
        "allies": ["Aztechnology", "Federated Boeing", "Kepler Project"],
        "enemies": ["Ares Macrotechnology", "AresSpace"],
    },
    {
        "name": "Kepler Project",
        "org_type": "corporate consortium",
        "tier": 4,
        "headquarters": "Joint Aztechnology / Shibata / Federated Boeing program",
        "summary": "The dark horse of the Probe Race -- a three-corp joint venture whose probe Kepler is the only serious rival left to Ares' Velox II, and which paid Sherman Royce to wreck the first one",
        "description": (
            "A joint project between Aztechnology, Shibata and Federated Boeing, and the last probe besides "
            "Ares' Velox II with a real chance at Halley's Comet. Its very obscurity is what made it useful "
            "to Dr. Sherman Royce: shopping his Liberty sabotage virus from inside AresSpace, he used "
            "contacts outside the corporation to discreetly obtain the name of the Kepler project head, and "
            "that contact professed a high degree of interest, setting up a deal in which Royce would be "
            "paid a significant amount to derail Velox I -- money paid only on success. Royce later informs "
            "the same contact about the Asgard auction for the second Velox and encourages a bid. Members of "
            "the Kepler team could not be reached for comment when Velox I went off course."
        ),
        "notes": (
            "The consortium never appears on stage; it acts through Shibata's SMART team and its unnamed "
            "project-head contact, and through the referral name 'Gabriel' that got Royce his secure line in "
            "the prologue. If the consortium gets the second Liberty code, Kepler rendezvouses with Halley "
            "and Aztechnology, Shibata and Federated Boeing win the Probe Race outright -- and the runners "
            "have earned a permanent enemy in Ares. If nobody gets the code, Kepler and Velox II race on "
            "while Shibata and Ares fight a shadow war over Royce and increase their shadow ops against each "
            "other's hardware. The book's back-page poll asked groups to report who won, so the result was "
            "left deliberately open."
        ),
        "allies": ["Aztechnology", "Shibata", "Federated Boeing"],
        "enemies": ["AresSpace", "Ares Macrotechnology"],
    },
    {
        "name": "Ares Firewatch",
        "org_type": "corporate special forces",
        "tier": 4,
        "headquarters": "Ares Macrotechnology; deployed anywhere Ares has lost something",
        "summary": "Ares' elite retrieval and retribution units -- betaware-wired soldiers, a shielding mage and a drone rigger who were on the runners' trail from the moment Velox I went off course",
        "description": (
            "Ares Macrotechnology's top-tier corporate response teams, the units the corp sends when "
            "something of its own has been taken and someone is going to answer for it. The team that "
            "appears here has been working together for over a year; it was put on the runners' trail "
            "immediately following the Velox I incident and was on the scene in Silicon Valley shortly after "
            "the Royce extraction, and by the New Orleans endgame it is either the buyer at the Etienne "
            "Shipyards or the gatecrasher at somebody else's exchange. Composition: a commander, a mage, a "
            "rigger with two drones and three soldiers, all in armor vest with plates, all betaware-cybered "
            "and trained in the Ares Wildcat style."
        ),
        "notes": (
            "Firewatch mage p.80: B4 Q5 S3 C5 I5 W6 E6 M7, Init 5+1D6, Astral Init 26+1D6, Karma/Prof 3/4; "
            "Aura Reading 6, Conjuring 5, Interrogation 5, Sorcery 6; Levitate 5, Lightning Bolt 5, Magic "
            "Fingers 5, Manaball 4, Manabolt 5, Mindlink 4, Mind Probe 5, Treat 6, Urban Renewal 6; Initiate "
            "1 (Shielding); four Force 5 elementals, one of each element, one service each; Ares Lightfire 70 "
            "with EX ammo. Firewatch rigger: B4 Q5 S5 C3 I5 W4 E2.96 R5(9), Rigged Init 9+3D6, Control Pool "
            "9; remote control deck Rating 5, an Ares Guardian and a Cyberspace Designs Wolfhound. Three "
            "soldiers: B6 Q5 S5(7) C3 I5 W4 E3.78 R5(9), Init 5(9)+1D6(3D6), Combat Pool 7, Karma/Prof 3/4; "
            "Wildcat 6 (full offense, kick attack, multi-strike); betaware smartlink-2 with rangefinder and "
            "Wired Reflexes 2 with reflex trigger; cultured enhanced articulation, muscle augmentation 2, "
            "orthoskin 2; Ares Alpha with underbarrel grenade launcher, Ares Crusader. A Firewatch team may "
            "also be seen working the New Orleans streets looking for the runners or asking about Mercy."
        ),
        "allies": ["Ares Macrotechnology", "AresSpace", "Knight Errant Security Services"],
    },
    {
        "name": "Annika Griebe's Runner Team",
        "org_type": "shadowrunner team",
        "tier": 2,
        "headquarters": "Seattle; on retainer to the fixer Annika Griebe",
        "summary": "The six runners Annika Griebe keeps on retainer -- a tactical specialist, three brothers, a bear shaman and a rigger -- used to watch her clients' backs and, in New Orleans, her clients' hires",
        "description": (
            "A team of six who have worked with Annika Griebe for over a year and work together seamlessly: "
            "Natalie Dark, an elven tactical specialist and field leader; Nate, the ork elder brother, and "
            "Crimson and Midnight, his human twin younger brothers; Aarvis 'Growler', a bear shaman; and "
            "Eddie, an old-timer rigger who has worked for Griebe longer than anyone can remember. They "
            "provide her security at meets -- heavily disguised and scattered through the crowd at Vertigo "
            "while she talks -- and they take the standing jobs she does not hand out, including watching "
            "another team on a client's behalf. They fight only in self-defense at a meet, and leave the "
            "premises immediately if trouble starts."
        ),
        "notes": (
            "At Vertigo: a Perception (5) Test spots one of the brothers watching the runners, a second "
            "Perception (5) spots his twin elsewhere in the crowd; the third brother is the large chromed "
            "Amerind in dark glasses standing beside Griebe in the back room. In New Orleans, Royce -- "
            "essentially a corp suit who does not trust his hires -- pays the team to surveil the runners "
            "and make sure they do not sell him and the Liberty code to the highest bidder; they have orders "
            "to back off immediately and not fight if they are noticed, so give the players glimpses but "
            "never a catch. At the Etienne Shipyards they watch from the swamp with spells, assensing, "
            "shotgun mics, low-light and thermographic magnification and a scanner, Nate in a sniper's nest, "
            "with orders to recover the payment at all costs and return it to Royce. If the runners take the "
            "buyer's offer, the team attacks: payment first, destroying the virus data and killing the "
            "traitors second. If the runners stay loyal and are being overwhelmed, the team may help. A "
            "captured member says nothing, but carries a credstick tied to a First Seattle Bank account in "
            "the name of 'Donna Klein' -- an alias of Griebe's."
        ),
    },
    {
        "name": "Californian Protectorate",
        "org_type": "military government",
        "tier": 4,
        "headquarters": "San Francisco Bay Area, under General Saito",
        "summary": "General Saito's military regime around the Bay, hostile to metahumans, ringing Ares-held Silicon Valley with checkpoints and shipping troublemakers to Relocation Camps",
        "description": (
            "The regime General Saito installed when he seized power in the Bay Area, and the reason Ares "
            "has mounted a campaign of armed vigilance around its Silicon Valley assets. Saito's troops "
            "patrol warily just outside the Valley's unwalled boundary while Ares troops openly guard it "
            "from the other side, and both sides run checkpoints on anyone crossing. The Protectorate is "
            "openly hostile to metahumans, who are stopped, interrogated and hassled, with any excuse good "
            "enough to drag a metahuman troublemaker off to a 'Relocation Camp'; its officers are also "
            "suspicious of metahuman resistance fighters using Ares-held Silicon Valley as a safe staging "
            "ground. San Francisco International Airport lies in Saito's territory rather than the Valley, "
            "so anyone flying a extracted scientist out has to satisfy both sets of guards."
        ),
        "notes": (
            "Background reading the book cites: p.106 Year of the Comet, p.6 Threats 2, p.50 Shadows of "
            "North America. Ares will not pursue runners into the Protectorate but will do everything it can "
            "to stop them leaving, using heavy ordnance if necessary; Saito's troops will try to seize a "
            "fleeing team for interrogation. Smugglers running Seattle to Silicon Valley charge 2,500 to "
            "5,000 nuyen a passenger and may be carrying weapons for the Metahuman People's Army with Saito's "
            "troops waiting in ambush. Inside the Valley the specter of invasion haunts the air: Ares "
            "Citymasters on the streets, troops encamped at strategic points, anti-Saito graffiti "
            "everywhere, tourism dead (hotel rooms 150 nuyen average, 60 low-end) and black market prices "
            "100 to 150 percent above normal."
        ),
        "enemies": ["Ares Macrotechnology", "AresSpace"],
    },
]

LOCATIONS = [
    {
        "name": "Proteus Iles du Salut Arkoblock",
        "location_type": "corporate arcology",
        "city": "Kourou",
        "district": "Iles du Salut (Salvation Islands), 15 km offshore in the Atlantic",
        "security_level": "Corporate Extraterritorial",
        "controlling_org": "Proteus AG",
        "summary": "Twenty stories of concrete and glass on three old prison islands, plunging fifteen more down the cliffs and a kilometer out along the sea floor; Gotterbote's launch pad and Hausmann's underwater flat",
        "description": (
            "Sheer-sided slabs of stone in a raging sea, palm-covered and ringed by swirling currents and "
            "circling sharks, crowned by a facility of chrome, steel and plastic bristling with antennae and "
            "satellite dishes. Forty meters of rocky cliff carry twenty-some stories of concrete and glass; "
            "at the islands' eastern edge the building keeps going, plunging fifteen floors down to sea "
            "level in a massive curved wall of windows and then fanning out in three or four submerged "
            "floors that run over a kilometer along the shallow sea floor. Only a small part is actually "
            "underwater -- storage and aquatech research labs below, the aerotech labs and construction "
            "halls above, employee quarters along the great slablike outer wall facing the Atlantic, and a "
            "handful of residents like Hausmann who prefer an underwater view. Inside, all trace of the "
            "wilderness is shut away: clean corridors, expensive offices and plenty of bland art, "
            "indistinguishable from any other corporate building in the world. Ile Royale, the largest "
            "island, holds the rocket launch pad and gantry; Ile Saint-Joseph holds the docks, hangar and "
            "helipad, the only legitimate ways in and the most heavily guarded ground; Devil's Island itself "
            "is empty but for a 3-kilometer jogging trail through heavy woods and a small fitness center."
        ),
        "notes": (
            "Map p.18. The complex is usually SAID to be on Devil's Island but spans all three Iles du Salut, "
            "all now owned by Proteus. Guards: two roving three-man patrols on Saint-Joseph, one on each "
            "other island, and a three-man unit each at the docks, hangar, launch pad and the three "
            "arkoblock entrances; three security mages live on site with one on duty at a time in the main "
            "security office, astrally projecting to any alarm with medics standing by. Sensors equivalent "
            "to Rating 10, but the radar is extremely unreliable at surface level in the rough seas; roof "
            "mini-turrets with AV missiles warn unidentified aircraft twice, then fire; door scanners Rating "
            "6, launch-boarding ID scanner Rating 3 with a daily arrival list (Intelligence (6) per stolen "
            "ID). Cliffs: Climbing base TN 5, +4 height, +2 seaspray, -4 with a grapple gun. Underwater: "
            "sonar cannot resolve anything smaller than a minisub, the floor is 12-13 m down, and eight "
            "tethered Haifisch II observer drones (Handling 4/4, Speed 30, Body 2, Sensor 5, gyrojet gun "
            "12M/12S underwater, 200 m from their cable) patrol the perimeter; an underwater alarm launches "
            "two patrol boats in five minutes carrying three 'Sub-Marines' each (Colt M24A3 Water Carbine, "
            "diving armor 4/2, Underwater Combat 5) and puts a six-man squad inside every airlock. Docks: "
            "the launch is a Zemlya-Poltava Swordsman, plus two Surfstar Marine Seacop patrol boats. Hangar: "
            "a Hughes Airstar, an Ares Executive tilt-wing, an Ares Cargoliner and three Northrup PRC-44F "
            "Yellowjackets, one always fueled on the pad. The West Entrance door is dwarfed by the 60 m by "
            "50 m Assembly Room gate. Because Proteus assumes intruders never arrive, internal defenses are "
            "light. Launches from here go up to Treffpunkt Raumhaufen. PLTG in the prep doc."
        ),
    },
    {
        "name": "Kourou",
        "location_type": "town",
        "city": "Kourou",
        "district": "Atlantic coast, French Guiana; 40 km up the coast road from Cayenne",
        "security_level": "Low Security",
        "controlling_org": "French Guiana",
        "summary": "Corporate company town around Saeder-Krupp's local headquarters -- radio telescopes and top-drawer hotels a few blocks from craft stalls, shacks and decrepit shrimp fisheries, and brutally hot",
        "description": (
            "Smaller than Cayenne but considerably more modernized, and the best illustration of Guiana's "
            "split. The local headquarters of Saeder-Krupp dominates the town center, and the few blocks "
            "around the S-K building are relatively clean and prosperous, providing housing, shopping and "
            "entertainment for corporate employees and the occasional tourist. Everything beyond that ring "
            "is run-down and poverty-stricken. The whole place is a curious mixture of high and low tech: "
            "massive radio telescopes, top-drawer hotels and bleeding-edge research facilities standing side "
            "by side with street-corner craft stalls, dilapidated shacks and decrepit shrimp fisheries. It "
            "is brutally hot and humid, and the tropical rain forest begins literally a few meters outside "
            "town. Proteus' employees meet all their shopping and recreational needs inside the arkoblock "
            "and rarely see Kourou proper at all."
        ),
        "notes": (
            "The old European Space Agency base here is now Saeder-Krupp's. A handful of Proteus employees "
            "come into town on business on any given day and new transfers arrive from the mainland, which "
            "makes mugging one for an ID card the most viable way onto the islands. Cheap guns (Availability "
            "3 or lower) can be scrounged here with legwork and hard Etiquette (Street) rolls. Places to hide "
            "after the Proteus raid: paying poor locals to shelter you (they would just as happily take "
            "Proteus' money for turning in wanted criminals), the jungle a few meters out of town (heat, "
            "humidity, disease, quicksand, caimans, poisonous snakes) or simply living in the van and moving "
            "it around. Motor launches run to the arkoblock at dawn and dusk, the evening one departing 2130."
        ),
    },
    {
        "name": "Cayenne",
        "location_type": "city",
        "city": "Cayenne",
        "district": "Capital of French Guiana; Atlantic coast",
        "security_level": "Low Security",
        "controlling_org": "French Guiana",
        "summary": "Crowded colonial capital of about 50,000 with two-lane streets and three-story buildings, an international airport, botanical gardens and a Novatech aerospace complex rising outside town",
        "description": (
            "Guiana's capital, a crowded city of about 50,000 full of attractive if somewhat archaic "
            "colonial buildings. The streets are two lanes at best and few of the buildings are more than "
            "three stories tall. Its only significant modern facilities are the international airport where "
            "outsiders arrive and the massive aerospace complex Novatech is building outside of town; unless "
            "visitors are fond of botanical gardens there is really not much for them to do. It is hot "
            "enough that stepping off a plane feels like walking into an oven, and it is the sort of place "
            "where customs officers reason that anyone the UCAS authorities let onto a plane is unlikely to "
            "present a threat here. About thirty minutes out along the two-lane coast road toward Kourou, "
            "past an ancient overgrown plastic truck hulk, a dirt track leads down to a fishing village of "
            "two huts and a dog whose rickety dock makes a convenient place to buy guns."
        ),
        "notes": (
            "The only public hospital of any size in Guiana is here -- overcrowded, understaffed and "
            "suspicious of tourists with gunshot wounds; a shaman in the slums will patch runners up for "
            "money. Hoff's rental van waits at the airport (an aging but reliable VW Superkombi III, p.171 "
            "R3) and the drive up to Kourou takes a little over an hour. Bala's meet is held at the fishing "
            "village dock shortly after dark on the day of arrival; the villagers are dirt-poor locals who "
            "stare apathetically at arrivals and will take cover in their huts and stay there if shooting "
            "starts, having no interest in helping either side."
        ),
    },
    {
        "name": "Rochambeau Airport",
        "location_type": "transportation hub",
        "city": "Cayenne",
        "district": "Cayenne international airport, French Guiana",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "French Guiana",
        "summary": "Guiana's one international airport -- a faded concrete runway and a terminal like a massive oven, where customs is effectively a joke",
        "description": (
            "The international airport at Cayenne and one of the only two significant modern facilities in "
            "the capital. For a moment as the plane door opens arrivals are sure the pilot has landed "
            "underwater; the hot wet wave rolling into the cabin is only the air. Light reflecting off the "
            "faded concrete runway is enough to make a runner squint through mirrorshades, not that much can "
            "be made out through the rippling heat waves anyway, and the walk down the stairway into the "
            "terminal breaks the whole body out in a sweat. Customs here should be a joke unless the runners "
            "are particularly aggressive or sporting obviously combat-oriented cyberware -- the officers "
            "reason that anyone UCAS authorities allowed on the plane is unlikely to be a threat."
        ),
        "notes": (
            "The hard security is at the other end: any North American airport large enough to run a "
            "scheduled flight to French Guiana scans passengers with both a magnetic anomaly detector and a "
            "chem sniffer at Rating 8, and anyone with dangerous-looking cyberware or a bad attitude gets a "
            "pat-down. Optional trouble (p.14): a bomb threat leaves the agents edgy and the team is "
            "randomly selected for a thorough look at papers and luggage. Runners who make enemies of "
            "Proteus and the police cannot use Hoff's return tickets and must go home through Caribbean "
            "League smugglers or across the Amazonian border instead."
        ),
    },
    {
        "name": "Gunther Hoff's House",
        "location_type": "residence",
        "city": "Kourou",
        "district": "Old suburban neighborhood, Kourou",
        "security_level": "Low Security",
        "summary": "Two-story A-frame of dark wood and windows in a pleasant old suburb -- the dinner-party grab site, then the murder scene where Hoff's telecom recorded everything",
        "description": (
            "A smallish two-story A-frame house made with dark wood and lots of windows, a deck running "
            "around two sides and a small garage nearby. The neighborhood is actually fairly nice by "
            "Kourou's standards: the buildings are not new and the whole place is still hotter than a "
            "Vindicator after ten minutes of sustained fire, but it reads as a pleasant, old-fashioned "
            "suburb without the mass-produced sameness of corporate housing. Lots of trees screen the "
            "neighbors' view and the neighbors themselves are pretty far away. Hoff bought it years ago "
            "while he worked for Saeder-Krupp and elected not to move into the arkoblock when he took his "
            "Proteus position. Inside, past a great room with a fireplace and up to a loft bedroom, is the "
            "study where he kept his telecom -- and where the runners find him cuffed to his desk chair, "
            "head flung back, a neat bullet hole in his forehead and a small-caliber revolver on the floor."
        ),
        "notes": (
            "Maps p.21 (first floor and second floor). The dinner party: nine guests -- Hausmann, two other "
            "single employees and three couples -- helicopter in from the arkoblock and take taxis from "
            "town, arriving about 1830 for a 1930 dinner; the house alarm is off, no guest is armed or "
            "magically active, and Hausmann leaves by 2115 to catch the 2130 launch. His taxi driver carries "
            "a light pistol he has no intention of using and will surrender his passenger, his cab, his "
            "wallet and his pants. Hoff asks the team to avoid property damage and bystanders, to take "
            "Hausmann as he leaves, and if they must go loud to fake a robbery with Hausmann grabbed as a "
            "random afterthought. He will skew his own witness statement to help them escape but cannot do "
            "much about the other guests. Later: the front door hangs ajar in the hot breeze, one light on "
            "at the back, and the telecom blinks 'RECORDING ENDED -- OUT OF STORAGE SPACE. PLAYBACK NOW? "
            "(Y/N)'. Anderson deliberately left the body cuffed to frame the team, set a high-altitude drone "
            "to watch the house, and had it call the police with a faked emergency recording in Hoff's voice "
            "the moment the runners walked in; eight Kourou officers and a Proteus strike team arrive."
        ),
    },
    {
        "name": "The Kourou Safe House",
        "location_type": "safehouse",
        "city": "Kourou",
        "district": "Derelict tourist-resort bungalow complex outside Kourou",
        "security_level": "Low Security",
        "summary": "One intact bungalow in a dead resort, stocked with a week of rations, a generator and a chemical toilet -- and the target of Proteus' flash-and-gas raid",
        "description": (
            "One of a series of bungalows in what used to be an upscale tourist resort. The resort went out "
            "of business years ago and most of the bungalows have had their interior walls knocked out for "
            "use as makeshift warehouses; this one is still intact, a one-story apartment with boarded-up "
            "windows, threadbare carpeting and little or no furniture. The ground around it is lightly "
            "wooded and overgrown with tall grass, and most of the other buildings in the complex are some "
            "distance away with none in a direct line of sight. Hoff has stocked it with a week's worth of "
            "prepackaged foods and bottled water, a prepaid portable phone set to accept incoming calls "
            "only, a small portable generator and a chemical toilet, since neither the plumbing nor the "
            "electricity in the building works."
        ),
        "notes": (
            "Map p.25. Winternight locates Hausmann here within 24 hours -- by the Safe Target ring's "
            "constant transmission (a few hundred meters' range, swept for by drones quartering the city) "
            "and by Ritual Tracking off DNA samples -- then passes the address to Proteus as an anonymous "
            "tip rather than risk exposure. Proteus sends an astrally projecting mage first, who cannot "
            "recognize Hausmann's aura but will call the tip valid on any sign of magical defenses, "
            "firearms, a drugged person, or being attacked; the strike team lands 1D6 minutes later. Dispose "
            "of the ring AND beat the ritual (a ward, astral watch and disrupted sending) and no attack ever "
            "comes. Moving Hausmann elsewhere does not help: they find him anyway. The raid: flash grenades "
            "through the windows, Neuro-Stun VII behind them, simultaneous entry front and back, everyone "
            "put down and sorted out afterwards."
        ),
    },
    {
        "name": "Sporting and Aero Club",
        "location_type": "ruins",
        "city": "Kourou",
        "district": "Desolate edge of Kourou",
        "security_level": "No Security / Barrens",
        "summary": "Kourou's abandoned health club -- chainlink, a freshly cut padlock, a drained pool and rusting patio furniture, where Anderson wears Hoff's face to buy Hausmann back",
        "description": (
            "Once Kourou's best physical fitness center, with handball, racquetball and tennis courts, "
            "pools, Jacuzzis, saunas and massage tables, kept in business by employees of the French space "
            "facility nearby and the occasional tourist. When Saeder-Krupp took over the base and built its "
            "own health club for its people, the club could no longer afford to stay open. Now it is "
            "abandoned, dilapidated, dark and dreary: a chainlink fence around the whole property and a big "
            "padlock on the front gate that has been cut open, recently, by the look of it. The building is "
            "big and thin moonlight gives no clue where anyone might be waiting. Around the corner is what "
            "used to be the pool area, dried up long ago and now nothing but a cracked concrete hole in the "
            "ground, with a covered walkway running around the building's edge filled with rusting stacks of "
            "wrought-iron patio furniture. It is very quiet out here at midnight."
        ),
        "notes": (
            "Map p.27. Anderson waits in the shadows of the walkway wearing Hoff's face via Physical Mask, "
            "with two Winternight drones hovering at a discreet distance under Howe's control from a car "
            "outside the fence (a rigger-equipped Toyota Elite and a Ford Americar) and three razorboys "
            "hidden inside the club building as his ace in the hole. The walk-around-the-pool exchange he "
            "proposes puts the runners in perfect ambush position, though he will listen to any reasonable "
            "alternative and will not pay without proof Hausmann is alive. Offers: the balance of the fee, "
            "then a 'flexibility bonus' of another 50 percent, then double -- generosity so unlike Hoff's "
            "haggling that it is itself a tell. Winternight's first priority is Hausmann alive; money and "
            "their own lives are comparatively unimportant. Unsilenced gunfire draws the Kourou police in "
            "2D6 minutes out here. Clues planted to send the team to Hoff's house: a 'if found, please "
            "return to' label inside the credstick bag, a slip of paper with the address on a dead man, or "
            "the address offered outright as a fresh safe house Anderson 'won't be needing any more'."
        ),
    },
    {
        "name": "Treffpunkt Raumhaufen",
        "location_type": "orbital platform",
        "city": "Low Earth orbit",
        "district": "Proteus AG orbital facility",
        "security_level": "Corporate Extraterritorial",
        "controlling_org": "Proteus AG",
        "summary": "Proteus' orbital platform, where payloads boosted from the Iles du Salut are mated to a deep-space rocket and fired at Halley's Comet",
        "description": (
            "The orbital station at the far end of Proteus' launch chain. Payloads assembled in the "
            "arkoblock's Assembly Room and rolled out to the Ile Royale gantry are boosted up here, where "
            "the Gotterbote probe is loaded onto a deep-space rocket and launched toward Halley's Comet. "
            "Heinrich Hausmann is believed to have designed the platform's primary sensor systems before his "
            "assignment to the comet probe, which is part of why Proteus' regional director insisted on him "
            "for Gotterbote in the first place. It is the last point at which anyone can still stop the "
            "launch once the payload has left the ground, and the other space-oriented megacorps know it."
        ),
        "notes": (
            "Gotterbote legwork (Matrix TN 5) gets the name, the planned launch date and the fact that the "
            "probe is boosted from the Devil's Island arkoblock to Treffpunkt Raumhaufen; everything else is "
            "classified and only inside Proteus' own Matrix. If the runners fail and the nuke goes up, "
            "Saeder-Krupp, Ares, Novatech and Yamatetsu all want the launch to fail even without knowing "
            "about the bomb, and any of them might send a shadow team up here to stop it -- the book "
            "suggests the GM can have such a run go wrong and destroy the entire station in an unexplained "
            "nuclear blast, a campaign-scale event that would spike tensions between every megacorp."
        ),
    },
    {
        "name": "Lickety-Splits Old Fashioned Ice Cream",
        "location_type": "restaurant",
        "city": "Seattle",
        "district": "Storefront parlor with a neon sign over the sidewalk",
        "security_level": "Patrolled / Commercial",
        "summary": "Storefront ice cream parlor where a gnarled Mr. Johnson holds meets over banana splits, with an ork on the door asking 'Sherbet?' and real dairy inside",
        "description": (
            "One of the strangest places a team is ever likely to take a meet. The neon sign hanging out "
            "over the sidewalk reads 'Lickety-Splits Old Fashioned Ice Cream' and a thick ork with a face "
            "scarred from a lifetime of fisticuffs stands outside the door, looking arrivals up and down "
            "before muttering the passphrase, 'Sherbet?' Through the window there is nothing but inky "
            "blackness and the shadowy outlines of an ice cream counter and a smattering of chairs turned "
            "upside down and crowning the tables. Inside, the pleasant smell of waffle cones and confections "
            "fills the nose, and all the way at the back a flimsy card table waits with a row of stools set "
            "out. The ice cream is real old-fashioned dairy, not soy, and it is quite good -- something the "
            "Johnson will press on his guests to the point where they may find it suspicious."
        ),
        "notes": (
            "Passphrase 'Sherbet?', response 'Rainbow'. The runners come in through one of their usual "
            "fixers, who knows only that it is a B&E datasteal job -- light physical security, heavy Matrix "
            "sec. The Johnson's intentions with the ice cream are entirely innocent. Optional staging: he "
            "insists on meeting during business hours instead, surrounded by screaming, playing, "
            "ice-cream-smeared children whose parents eye the runners nervously and who may become "
            "fascinated or frightened by the team mid-negotiation; or he comes from a culture where refusing "
            "hospitality is a serious offense, so the runners must eat the mysterious ice cream to get the "
            "job at all."
        ),
    },
    {
        "name": "Alaxa Facility (Everett)",
        "location_type": "research lab",
        "city": "Seattle",
        "district": "Everett; light industrial",
        "security_level": "Corporate Standard",
        "controlling_org": "Alaxa",
        "summary": "Two floors of gray brick behind rusty barbed wire, with a roof dish that burst-uplinks to Shibanokuji once an hour and a security office no bigger than the cold room",
        "description": (
            "Small and unassuming: two floors of gray brick ribboned with two rows of one-way mirrored "
            "windows that do not open, looking about as high tech as a mattress factory. A two-meter chain "
            "link fence topped with rusty barbed wire runs around the entire perimeter, the grounds "
            "terribly neglected with weeds and dandelions choking patchy dull green and brown grass and a "
            "few dry, thirsty bushes on the lawn; the main gate with its keycard-swipe access post is the "
            "only gap in the fence, and just inside it a parking lot and a detached garage hold an "
            "ambulance and a security vehicle. Inside, the coloring is uniformly gray and antiseptically "
            "clean, offices carpeted and lobby and labs tiled. The roof carries maintenance access, vents, a "
            "few antennas and the satellite dish, watched by camera. Cold Storage keeps rows of padlocked "
            "glass-door refrigeration units full of bar-coded tissue samples and small puddles of goo, and "
            "at five o'clock the whole place empties out as fast as if it were on fire."
        ),
        "notes": (
            "Maps pp.39-40. Perimeter: low-light cameras on several fence posts and thermographic cameras on "
            "the building corners for full coverage. Interior: infrared cameras and motion detectors Rating "
            "5 in corridors and labs, Rating 4 maglocks on external doors and labs, fire doors in each major "
            "corridor, and Rating 6 maglocks on the Security Office and the Server Room (guards and a few "
            "key employees only). Ventilation is heavily filtered and separate per floor -- useless for "
            "movement -- and the building runs at slightly negative pressure to keep airborne samples in. "
            "The Security Office's two consoles can monitor everything, track personnel, lock or open every "
            "door and take the comms grid offline; it also holds a locked cabinet of gas masks and spare "
            "weapons. Samples: half are worth something (100 nuyen times an Open Test of Biotech, Medicine "
            "or Science each; a random armful is 3D6 x 50). Alice Hernandez's Force 4 wards cover the "
            "exterior, each research lab and the security office and alert her wherever she is. Host and "
            "PLTG sheafs in the prep doc."
        ),
    },
    {
        "name": "The Pines Club",
        "location_type": "bar",
        "city": "Thunder Bay",
        "district": "Algonkian-Manitou Council",
        "security_level": "Low Security",
        "summary": "Rundown log-cabin bar hung with mounted carcasses -- including a squirrel on skis wearing goggles -- where Mr. Johnson hires the team for the module run",
        "description": (
            "A rundown log cabin posing as a bar, a rustic dump with definite backwoods charm that may never "
            "have seen better days and has certainly never seen any ice cream served. Various animal "
            "carcasses are mounted throughout the main room, some respectfully and others not so much, like "
            "the squirrel on skis wearing goggles. A room in the back is prepared for the meet, with a "
            "carved wooden table where Mr. Johnson sits, his familiar ork bodyguard over his left shoulder "
            "and a towering stuffed grizzly over his right. The runners arrive while the club is closed and "
            "the Johnson will likely have a fire burning in the stone fireplace, so the light in the room "
            "flickers either eerily or invitingly depending entirely on the team's attitude toward log cabin "
            "life."
        ),
        "notes": (
            "The second hire: 20,000 nuyen each with up to 25 percent up front, a 10 percent bonus for "
            "completion within 48 hours, and +1,000 nuyen or +5 percent bonus per success on a Negotiation "
            "(5) Test; proof of success required on return. The Johnson wants it done in 24 hours and it "
            "visibly pains him to grant the longer window. He will not confirm the Gagarin connection even "
            "when the runners guess it, though he is impressed by valid insight. From here the team is flown "
            "north to La Ronge with a modified SUV (a Land Rover or Gaz Willys Nomad) waiting, plus whatever "
            "gear their unnamed employer's identity allows."
        ),
    },
    {
        "name": "Thunder Bay",
        "location_type": "transportation hub",
        "city": "Thunder Bay",
        "district": "Algonkian-Manitou Council; port and commercial center",
        "security_level": "Low Security",
        "controlling_org": "Algonkian-Manitou Council",
        "summary": "The AMC's economic center and a major smuggling port -- almost any gear is available at smuggler prices, and elven newcomers get cold looks over the secession",
        "description": (
            "A real city with easy access to the outside world, the economic center of the Algonkian-Manitou "
            "Council and a major smuggling port. Almost any gear a shadowrunner might want to buy before "
            "heading north is available here, at smuggler prices, though a Johnson in a hurry will press the "
            "team along before they can establish good connections or good deals. Beneath the commerce it is "
            "seedy: smuggler gangs, pickpockets and young bravos looking to make a name for themselves. The "
            "Manitou secession has left scars in the city too -- elven characters, especially those of "
            "tribal ancestry, may get cold shoulders from anyone the secession hurt, and that hostility can "
            "boil over into a verbal or physical attack that draws in passers-by."
        ),
        "notes": (
            "Runners flown in are met at the airport and driven to The Pines Club. Employers with reach here "
            "can hand over contact references: Ares has good contacts in Thunder Bay, and Aztechnology has "
            "clout throughout the AMC. Optional staging (p.44): the Johnson brings the team in early and has "
            "them wait on standby for the module to fall, giving them days in seedy Thunder Bay before the "
            "run north."
        ),
    },
    {
        "name": "La Ronge",
        "location_type": "town",
        "city": "La Ronge",
        "district": "Northern Algonkian-Manitou Council, 50 km south of the Churchill River",
        "security_level": "Low Security",
        "controlling_org": "Algonkian-Manitou Council",
        "summary": "The last friendly town before the Manitou border, full of resentful newcomers and quiet sympathizers, where a guide can be bought and the runners are on their own afterwards",
        "description": (
            "A small northern town fifty kilometers south of the Churchill River and the staging point for "
            "anything going into Manitou land. People who seem to be expecting the runners meet the plane on "
            "the airfield, hand over the remainder of whatever gear and information was promised, and give "
            "them passcodes to transportation parked in the nearby lot. Prospecting for clues here is "
            "nothing like Thunder Bay: it is a much smaller community and there has been a great deal of "
            "change since the Manitou declaration of independence. Most of the newcomers show clear "
            "resentment toward the Manitou, but there are sympathizers in town as well, and between them a "
            "team can pick up reports of sightings of the crash and, with luck or skill, word of the "
            "Yamatetsu recovery team or at least of people going out that way. It is the last place they can "
            "receive any aid at all."
        ),
        "notes": (
            "A local guide can be hired -- a rough sort, native to the area, who wants payment up front and "
            "will not be involved in any of the troubles with the fighting up there; use the Amerindian "
            "Tribesperson, p.74 SRComp. From here it is fifty kilometers or more north through a border "
            "standoff. The Churchill River crossing: AMC troops hold the south bank against Manitou "
            "sabotage, Manitou watch the north for invasion, many bridges are destroyed or mined and the "
            "rest heavily guarded, so the team improvises -- the river has many stretches that are wide but "
            "not deep and easily forded, and at the GM's discretion may be frozen enough to walk across."
        ),
    },
    {
        "name": "Gagarin Module Crash Site",
        "location_type": "crash site",
        "city": "Manitou territory (Algonkian-Manitou Council)",
        "district": "Wooded hills about a day southwest of Niwimaja",
        "security_level": "No Security / Barrens",
        "controlling_org": "Manitou Tribe",
        "summary": "A steaming trench of flattened trees ending in a crater of scrap and charred beasts -- and two sets of tracks heading northeast, one of them concealed",
        "description": (
            "Even through the low-lying mist it is obvious something came down here fast and hot. A crash "
            "trench several dozen meters long still steams, trees lying flattened along its length, ending "
            "in a crater surrounded by scorched trunks and the charred remains of a few four-legged beasts. "
            "The ground stays noticeably warmer than the surrounding air, keeping the light snow at bay and "
            "leaking a surface fog that creeps eerily from the center of the furrow as though the empty "
            "ground were spilling it forth. A pile of upturned soil looms high at the end of the gash and "
            "something metallic gleams inside the crater -- but it is only the scrap of the module's "
            "carrier. Somebody has been here already. A few kilometers up the tracks is the ambush hollow: "
            "rake marks in the snow, impact points in the trees, blast holes in pristine earth, shreds of "
            "cloth on snapped branches, six bodies and bloodstained snow, and terrain that is a perfect "
            "death trap for anyone who did not know it."
        ),
        "notes": (
            "The Johnson's coordinates put the team within 1D6 hours of searching, or minutes if they search "
            "from the air. Electronics (4) on the wreckage shows a component of the payload has been "
            "physically removed. Crash Site Search Table, Perception (6): 1 six sets of prints; 2 a "
            "helicopter landed nearby; 3 the prints came from the helicopter; 4 they criss-cross the area "
            "then head northeast; 5 an older, better-concealed set of tracks from a group that got here "
            "first in flatter-soled boots; 6 those tracks also lead northeast. At the ambush hollow "
            "Perception (8) finds the concealed trail continuing; the corpses carry Yamatetsu insignia but "
            "no useful gear (the Manitou stripped them and took their own casualties away), and a Biotech, "
            "Medicine or Forensics (4) Test shows most died of cuts, slashes and puncture wounds rather than "
            "bullets. Assensing gives a Background Count of 1 from the killing; the Manitou carefully "
            "removed their astral signatures. A FORCE 7 WIND SPIRIT summoned before they left watches the "
            "site with orders to stop anyone tracking past this point -- Confusion on magicians first, "
            "Concealment to split the party into a search for a missing member, Movement and Accident to "
            "slow them, all done subtly. It lasts only until the next sunset or sunrise after summoning."
        ),
    },
    {
        "name": "Niwimaja",
        "location_type": "town",
        "city": "Niwimaja",
        "district": "Manitou territory north of the Churchill River",
        "security_level": "Low Security",
        "controlling_org": "Manitou Tribe",
        "summary": "Permaculture Manitou town of 500-plus, roads dug up into footpaths, geodesic domes and skin tents around a permanent core -- and the module buried somewhere under it",
        "description": (
            "The approach road's asphalt has been dug up and the road reclaimed as a decorated trail. Down "
            "it a cluster of buildings sits nestled among hills and trees, surrounded by a perimeter of "
            "tents and biofabricated huts; several storage silos loom over dirt footpaths and extensive "
            "gardens, rows of residential buildings lead into the center of town where a large, rustic, "
            "steepled council hall stands, and there are no roads or vehicles anywhere -- just decorated "
            "pathways, small parks and horses. The town has been redeveloped on permaculture principles and "
            "most of it has no electricity, save a few dwellings on solar power or windmills. Few structures "
            "are permanent and those cluster at the center; the rest of the community lives in prefab "
            "geodesic domes built from recycled materials, tents of preserved animal skins and a few "
            "tree-homes built among the sturdier trunks, heating with small fires whose thin plumes of smoke "
            "rise all across the town. There is exactly one Matrix connection, hidden and unused in the "
            "clutter of the council hall."
        ),
        "notes": (
            "Over 500 people are in and about the town, mostly armed and intimately familiar with the "
            "surrounding territory; supplies are stockpiled all year for the winter population increase, "
            "when permanent townsfolk trade with new arrivals for news, exotic supplies and currency. "
            "Approach openly and Thunderwalker's patrol slips out of the nooks and crannies to escort the "
            "team to Chief Youngman; sneaking in provides no benefit and only earns mistrust, and anyone "
            "caught and judged hostile is escorted to the AMC border and expelled. After questioning the "
            "team may move freely so long as they do not stir up trouble, watched but not guarded, and "
            "Thunderwalker will find them a bunk in one of the common houses -- communal living with a dozen "
            "tribals, far from the Ritz, more like a youth hostel only colder. The town is happy enough to "
            "see outsiders and trade with them; some resent the drain on resources, some see a chance to vie "
            "for power, and some resent any non-Manitou presence at all. Fifty to one odds, strong magic and "
            "home ground: violence loses here. Take hostages and Youngman hands over the module, and the "
            "Manitou will then do their damnedest to see the team never leaves their territory alive."
        ),
    },
    {
        "name": "Niwimaja Council Hall",
        "location_type": "government building",
        "city": "Niwimaja",
        "district": "Center of Niwimaja, across a community garden that was once a parking lot",
        "security_level": "Low Security",
        "controlling_org": "Manitou Tribe",
        "summary": "The steepled hall at the center of town -- pelt-curtained doorway, two smoldering fire pits, trade boards on one side and ceremonial storage on the other",
        "description": (
            "The large rustic building at the center of Niwimaja, reached across a community garden that was "
            "once a parking lot. A pair of animal pelts has replaced the glass entranceway, hung across the "
            "opening to act as an airlock and keep the heat inside; the methods may be old fashioned but the "
            "effect is excellent, and the interior is stiflingly hot, fueled by two large and smoldering "
            "fire pits centered near each end of the building. One side holds various tables and tack boards "
            "advertising trade or need as well as services and gatherings; the other is filled with built-in "
            "storage bins and what looks to be tribal ceremonial garb and items. It is where Chief Youngman "
            "warms his hands and receives outsiders, where the tribal council meets, and where the town's "
            "single hidden Matrix connection sits buried in the clutter."
        ),
        "notes": (
            "Council sessions: five elected members including the chief, with Cloud Talon and Thunderwalker "
            "attending by right though neither is a councillor. Few sessions are closed and various people "
            "attend regularly. The runners' presence inspires at least one and probably several sessions, "
            "each faction sending a representative to state its case; the longer the team stays the more "
            "frequent the sessions, until most councillors are in session or in private meetings most of the "
            "time. The runners will most likely NOT get to plead their own case here -- they have to earn "
            "representation by roleplaying their way into the heart of a faction. Barring extraordinary "
            "maneuvering, no decision is reached before the second Yamatetsu team arrives and reopens "
            "everything."
        ),
    },
    {
        "name": "Cloud Talon's Hut and Medicine Lodge",
        "location_type": "residence",
        "city": "Niwimaja",
        "district": "Outskirts of Niwimaja, by the oldest pine in the area",
        "security_level": "Low Security",
        "controlling_org": "Manitou Tribe",
        "summary": "The medicine man's sunken earthen hut and the lodge beside it -- the two places everyone wrongly suspects the module is hidden, and nobody dares tear up to check",
        "description": (
            "Cloud Talon lives in an earthen hut at the outskirts of Niwimaja, dug into the ground and "
            "consisting of a single good-sized room with several modern conveniences in it -- a portable "
            "heater, a food preparation unit, a small lamp -- so that the whole abode gives the impression "
            "of a long-term camp site rather than a home. His medicine lodge (Rating 7) is set up a few "
            "meters from his sunken door, near the oldest pine he could find in the area. Those in Niwimaja "
            "who know that the tribe has the crashed module and that Cloud Talon took charge of it suspect "
            "he has hidden it inside the hut or the lodge, but very few are willing to risk tearing either "
            "of them up to prove the theory."
        ),
        "notes": (
            "They are wrong: the module is literally underfoot. On receiving it from Thunderwalker, Cloud "
            "Talon summoned a Spirit of the Land to help him bury it deep underground in a crate warded at "
            "Rating 6. Nobody saw him do it and nobody in town knows where. Searching for it: without "
            "ground-penetrating radar or a sonar imaging setup the runners would not know where to begin, "
            "and the tribe would certainly object to digging up the ground or summoning a spirit to do it; "
            "a spirit with the Search power or a Detect (Object) spell might work but the ward and the depth "
            "make it hard, especially if the team does not know what the module looks like. If negotiations "
            "succeed, Cloud Talon simply summons the spirit again to dig the crate up and opens it. Optional "
            "twist (p.53): he was observed, Eaglefeather has already moved the module, and the recovered "
            "crate is empty when it is finally opened in front of everyone."
        ),
    },
    {
        "name": "Shibanokuji",
        "location_type": "orbital platform",
        "city": "Low Earth orbit",
        "district": "Yamatetsu orbital resort and research station",
        "security_level": "Corporate Extraterritorial",
        "controlling_org": "Yamatetsu Corporation",
        "summary": "Yamatetsu's orbital resort and low-g medical lab -- a party in orbit, the hottest place to watch the comet last fall, and host to the classified PLTG carrying the Gagarin project",
        "description": (
            "Yamatetsu's orbital station: officially a party in orbit and a big tourism attraction, the "
            "hottest place from which to watch the comet the previous fall, and a recreation spot where "
            "some very big names have been patched up in low gravity while looking out at the stars. It also "
            "carries a genuine medical lab doing research that needs zero g, and, aside from the "
            "sight-seeing decks, access to the working parts of the station is very tight. Its zero-g bio "
            "lab shares data with Yamatetsu's quiet Everett subsidiary Alaxa over a dedicated satellite "
            "link -- and that lab sits on the same private LTG as Yamatetsu's other classified "
            "space-oriented projects, the Gagarin mission included. Other corps would dearly love a "
            "competing platform, or an excuse to cause a problem for this one."
        ),
        "notes": (
            "The uplink from Alaxa fires once an hour while the station is overhead, generally a two to six "
            "hour window, in one-minute burst transmissions; a decker must be in the Alaxa host at the "
            "moment of transmission and then has 20 Combat Turns before being kicked off. The Yamatetsu PLTG "
            "is sculpted as a fantastic alien landscape with massive heavenly bodies rotating by in the "
            "starry sky above. Sheafs in the prep doc. If the runners cannot get in through Alaxa they must "
            "find another Yamatetsu facility with a dedicated uplink -- these are few and far between -- or, "
            "as a last resort, travel up the well to Shibanokuji itself, which is costly and hard (detail on "
            "the station is in Target: Wastelands)."
        ),
    },
    {
        "name": "Club Vertigo",
        "location_type": "nightclub",
        "city": "Seattle",
        "district": "Downtown",
        "security_level": "Patrolled / Commercial",
        "summary": "Rave-reviewed downtown changeling club, weapon-free, with lightly chromed twin bouncers on the door and a white-noise back room where Annika Griebe does business",
        "description": (
            "Nothing has changed more since SURGE hit than the club scene, and Vertigo is the proof. It is "
            "alive with the rhythmic bass of the latest power-jungle tracks and strobe lights radiate from "
            "the doorway, turning it green then yellow, red then green again. A pair of twins has replaced "
            "the street-standard troll bouncer, both attractive, muscular and lightly chromed, in tight "
            "white and black vinyl suits and dressed to kill -- a phrase that seems particularly apt for "
            "these women, who are all business and not to be trifled with. 'Vertigo is a weapon-free "
            "environment, for the safety of our guests.' Inside is a carnival of the insane: broad, muscular "
            "men with feathered backs chatting near the bar, a short human with a horn jutting from the "
            "center of his head careening recklessly across the dance floor, and prosthetic and real grown "
            "hard to tell apart in the whitewash of derangement. A door at the far end leads to a quiet back "
            "room with a white noise generator."
        ),
        "notes": (
            "Griebe's meet is set for 2000, the start of the resident DJ's four-hour slot, when the floor is "
            "packed with metahumans and changelings and her security team has ample cover. Password to the "
            "bouncers: 'liberty'; they are Professional Rating 3 and conduct a Brisk search (Physical Search "
            "Modifiers Table, p.236 SR3), taking weapons and issuing a ticket. The club is run by "
            "professionals who do not want a mess: any trouble brings Lone Star to round up everyone who "
            "does not play well with others. Griebe and the owner are friends and the staff cover for her "
            "very efficiently; she and her team fight only in self-defense and leave at once. Optional "
            "colour: the racial issues that come with a changeling club, slam-dancing across the floor, "
            "fending off an intoxicated changeling's affections, a Humanis sit-in outside, or a local "
            "syndicate leaning on the owners for protection money. A fight before the meet gets it moved to "
            "a limo cruising the highway later that night."
        ),
    },
    {
        "name": "Ares Cape Canaveral Launch Facility",
        "location_type": "military installation",
        "city": "Cape Canaveral",
        "district": "Florida, Confederated American States",
        "security_level": "Corporate High Security",
        "controlling_org": "Ares Macrotechnology",
        "summary": "Massive commercial launch site servicing Ares, lesser corps and governments alike -- three independent checkpoints, three bound air elementals and a silver and white shuttle at the end of it",
        "description": (
            "The sheer mass of the place is overwhelming. Stepping out of the fifteen-nuyen shuttle van from "
            "Orlando feels like walking into the proverbial lion's den: the corporate security presence is "
            "massive, Ares officers moving past in light armor brandishing assault rifles and handling the "
            "outer level of security, with a number of different corporate logos displayed beyond the "
            "checkpoints and, somewhere past all of that, a silver and white space shuttle just like the "
            "ones on the trid. Cape Canaveral services not only Ares but lesser corps and governments with "
            "assets in low orbit, and even several megas such as MCT and Shiawase run low-security launches "
            "from here, so the launch building is full of high-level businessmen wandering the port waiting "
            "for a flight to whichever station is their destination, and a shadowrun team is very obviously "
            "out of its element."
        ),
        "notes": (
            "Three separate checkpoints, each manned by four security officers, a combat mage and a "
            "corporate representative -- Ares at the first, the flying corp's own (Federated Boeing here) at "
            "the last two -- with the representative a political agent for handling special clearances. "
            "First checkpoint is the front door: physical search, astral scan, proof of identification and a "
            "clearance visa; each runner rolls Etiquette (Corporate) (4) not to look suspicious. Second is "
            "the boarding gate, third is aboard the shuttle. Each checkpoint is redundant but INDEPENDENT, "
            "so a lie that worked once may fail next time and vice versa. Weapon and cyberware scans at each "
            "(Rating 4 MAD, Rating 3 chem sniffer, physical search); astral scan only at the first. "
            "Cyberweaponry is escorted to the medical center and switched off, weapon foci are confiscated, "
            "and Federated Boeing Security IDs permit flechette, narcoject and taser weapons at the station "
            "but not on the shuttle. Three Force 5 bound air elementals patrol the pad with orders to "
            "contact Ares' main security office at any major trouble. Pull a gun here and the launch is "
            "cancelled and professional corpsec is called out; a replacement shuttle can be arranged from "
            "Edwards Aerospace Center in southern California within a few days."
        ),
    },
    {
        "name": "Apollo Low Earth Orbit Space Station",
        "location_type": "orbital platform",
        "city": "Low Earth orbit",
        "district": "Ares commercial station; Main Street, Park Place, Marvin Gardens, Vermont Avenue",
        "security_level": "Corporate Standard",
        "controlling_org": "Ares Macrotechnology",
        "summary": "Ares' rented-pod orbital hub and the closest thing to an R&R stop in orbit -- zero-g Main Street, three habitation arms, a drug and prostitution trade and a background count of 9",
        "description": (
            "A commercial station Ares uses as a hub and as a source of income, renting pod space to "
            "corporations without the means or the desire to build a station of their own; nowhere else will "
            "a runner find such a wide variety of corporations fraternizing in such a small place, and it "
            "has become something of an R&R stop for people who make their living out here. The main part is "
            "a long vertical corridor the locals call Main Street, with every working area connected "
            "directly to it and the sections without attached pods used as docking bays; Main Street and the "
            "pods around it are at effectively zero gravity. Toward the top, three long arms lead out to "
            "habitation pods -- Park Place and Marvin Gardens for the permanent scientists and workers, "
            "Vermont Avenue for transients -- joined at the far end by long open-space elevators and spun to "
            "a low artificial gravity. At the other end of Main Street is the Recreation Zone, with the "
            "station's only bar and a small shopping area beside it. Residents are friendly and close-knit; "
            "the drug and prostitution trades are lively, and the gambling hall and the Community Chest "
            "brothel are floating operations that set up in whatever pod is vacant."
        ),
        "notes": (
            "Detailed further on p.75 of Target: Wastelands; zero-g operating and combat rules p.126. "
            "Visitor quarters are two 2 by 3 meter three-bunk cabins and a shared bathroom (vacuum toilet, "
            "six vacuum urinals, hygiene kits, mirror and pre-moistened towelettes); the strapped bunks are "
            "sized for standard humans and orks and trolls will not fit. The station is cramped -- small "
            "doorways are hard on orks and trolls and a claustrophobe will be on edge the whole visit. "
            "APOLLO EFFECTIVELY HAS A BACKGROUND COUNT OF 9 from the mana warp; Awakened characters are "
            "immediately aware of their disconnection from the manasphere and may become despondent and "
            "homesick. Black market close-combat weapons (stun batons, brass knuckles) sell at +4 Street "
            "Index and 1.5 times Availability. Security is primarily a peacekeeping force but heavier than "
            "most stations because of the turnover: three-person units on semi-regular patrol, two units at "
            "a time in eight-hour shifts, off-duty guards callable at once; they do not board arriving "
            "shuttles but usually greet them. Caught doing something questionable, the runners need "
            "Etiquette (Corporate) (5) or are detained 1 to 12 hours while clearances are checked. Officers: "
            "B5 Q5 S5 C5 I4 W5 E3.5 R4(6), Combat Pool 6, Karma/Prof 3/3; smartlink, Wired Reflexes 1, Ares "
            "Viper Slivergun with integral silencer, stun baton, secure jacket 5/4. Airlock A at the top of "
            "the station: Rating 6 palm print maglock on the inner door wired to the guard station halfway "
            "down Main Street, Rating 7 palm print maglock on the outer door, which will not open until the "
            "inner one is closed. Earthbound Ares shuttles leave once every 24 hours and there is almost "
            "nowhere on a space station to hide."
        ),
    },
    {
        "name": "The Water Works",
        "location_type": "bar",
        "city": "Low Earth orbit",
        "district": "Recreation Zone, Apollo station",
        "security_level": "Corporate Standard",
        "controlling_org": "Ares Macrotechnology",
        "summary": "Apollo's only bar and Sketch's office -- no tables, no chairs, a bar halfway up one wall and clusters of floating drinkers sipping pouches through straws",
        "description": (
            "The only bar on the station, which makes it easy to find; the name is written on a sign "
            "attached next to the doorway leading in. It is very obviously not an Earth-side bar. For "
            "starters, everyone is floating. There are no tables and no chairs, just a bar running along one "
            "wall about halfway up to the ceiling and groups of floating people scattered around the room "
            "with pouches of drinkable materials, complete with straws, and a newcomer floating in has to "
            "concentrate on not colliding with anyone. It is where Sketch holds court, drink in hand, "
            "talking boisterously at whoever will hold still, and where Griebe told the runners to find him: "
            "'Ah, tourists in search of adventure. Everyone wants a bit of my wares, it seems. I'll be back "
            "soon, my dove. Shall we step into my office?'"
        ),
        "notes": (
            "Legwork on Sketch (any Space contact, TN 5) puts him here: 'always hanging out at the Water "
            "Works'. He will not come along on the spacewalk -- he has nothing that gets past the maglocks "
            "and only Ares station residents, not transients like him, are cleared for airlock access -- but "
            "he will pull the guards off the guard station for 30 minutes for 4,000 nuyen up front. Treated "
            "decently and forgiven his pragmatism, he becomes a Level 1 contact after the run."
        ),
    },
    {
        "name": "AresSpace Silicon Valley Office Park",
        "location_type": "corporate facility",
        "city": "Silicon Valley, California",
        "district": "Ares-held enclave; Building C, second sublevel",
        "security_level": "Corporate High Security",
        "controlling_org": "AresSpace",
        "summary": "Four city blocks of bunker-like buildings behind a Barrier 16 wall, tank traps and watchtowers, where prized scientists commute by video-monitored tunnel and live more like inmates",
        "description": (
            "A business park that looks like a life-sucking, soulless prison. High drab walls guarded by "
            "actual watchtowers are pierced only by a single metal gate with tank traps to deter ramming; "
            "sick-looking trees and listless shrubs do nothing to liven up the landscaping between half a "
            "dozen bunker-like buildings, and a sad walking trail snakes between them, spotted with a few "
            "decrepit benches that look like they never get used. It is hard to distinguish the dormitories "
            "and rec areas from the offices and work areas at all. The park covers about four city blocks "
            "and six buildings, each three stories tall over three basement levels, holding offices, dorms, "
            "recreation (gym, sim theater, arcade, a few shops), a security station with a 24-hour rigger "
            "and a night-shift shaman, and an operations center linked directly to AresSpace Command in "
            "Houston. Every building connects by subterranean video-monitored tunnel, and workers are "
            "'encouraged' to commute that way -- going outside between buildings requires special permission."
        ),
        "notes": (
            "Maps pp.72-73. Wall Barrier 16, three meters, watchtowers at the four corners and the gate, "
            "each with one guard behind full-length one-way windows (Barrier 8) and low-light cameras "
            "covering the walls, the gate, the approaches and part of the grounds; a laser trip-beam runs "
            "along the top (Perception (6) to notice, Athletics (6) to cross without tripping). Gate Barrier "
            "6 behind tank traps Barrier 24, opened only by the gate guard or the security rigger, 3 full "
            "Combat Turns to move, Rating 4 passcard reader on a post. Magic: at sunup and sundown the "
            "shaman summons a Force 5 city spirit to patrol and chase off astral intruders, accompanied at "
            "night by a Force 3 watcher that reports to him immediately; the whole park has Background Count "
            "1. Drones: an Ares Sentinel on tracks along the gate wall (Ares Alpha, AV ammo, concussion "
            "grenades) and an Ares Guardian inside the grounds on hardline (Ares HV MP-LMG, APDS). Building "
            "C: dull gray block, glass-block windows, cameras almost everywhere linked to the building "
            "security room and the compound rigger, Rating 4 maglocks with card reader and retinal scanner "
            "on every door, doors Barrier 4 and stairwell fire doors Barrier 8. Ground floor: empty "
            "reception desk with a jackpoint behind it, the security room (three guards, monitor bank, nine "
            "lockers and three Ares Alphas), the Matrix host hardware, a conference room, a lounge and "
            "smoking area occupied even late at night, admin offices, two executive offices and bathrooms; "
            "the elevator takes a passcard swipe and has a rear door to the loading area, and the front "
            "stairwell holds a fire axe in a glass box. Second sublevel (Royce's floor, and the template for "
            "the others): cafeteria, conference room, bathrooms with a maintenance closet, programmer "
            "offices, the tunnel entrance splitting 20 meters out toward Building A and the dorms in "
            "Building D, and Royce's own office, sparse and uncluttered unlike its neighbors. One alarm puts "
            "the compound on passive alert and calls in the shaman (4+1D6 minutes); a second triggers "
            "lockdown -- every maglock forced locked, off-duty security recalled, Barrier 12 shutters down "
            "over every building entrance including the tunnels. Matrix sheafs in the prep doc."
        ),
    },
    {
        "name": "Roger's Boutique",
        "location_type": "shop",
        "city": "New Orleans",
        "district": "Alleyway of shops near Bourbon Street",
        "security_level": "Low Security",
        "summary": "Lace-curtained mask shop near Bourbon Street that is very obviously a front -- Mercy's talismonger business, Royce's bolthole and the runners' New Orleans quartermaster",
        "description": (
            "A shop in a long alleyway of shops near Bourbon Street, so unlikely an address that arriving "
            "runners check it twice. White lace curtains adorn the windows and a sign above reads 'Roger's "
            "Boutique', and anyone escorting a hunted scientist through the door with their safeties off "
            "will be wondering whether the store is really some kind of front. Inside is just like the "
            "outside: more lace, early twentieth-century furniture, and a display case featuring over a "
            "hundred masks of all different shapes and sizes, some of them ritual masks from tribal "
            "cultures and some over a hundred years old. Then a blue velvet curtain parts and a woman well "
            "over two meters tall in a light blue knit dress introduces herself as Mercy and asks how she "
            "can help."
        ),
        "notes": (
            "Mercy has been paid to set the team up with whatever they need; she deals in magical materials "
            "and can get her hands on weapon and power foci, and she supplies the credstick verification "
            "reader for the exchange. This is where Royce delivers the runners' final payment for the "
            "extraction, admits he was the Johnson behind all three runs, tells them what he is escaping "
            "and why, and puts them on 500 nuyen a day retainer for 72 hours while the auction runs. Side "
            "hooks the GM can hang on the shop: the Mafia leaning on Mercy for protection money, or a rare "
            "telesma she is trying to keep out of the hands of the zobop. Ares Firewatch and Shibata's SMART "
            "may both be on the streets asking questions about Mercy while the runners wait."
        ),
    },
    {
        "name": "Etienne Shipyards",
        "location_type": "ruins",
        "city": "New Orleans",
        "district": "50 km outside the city, on the edge of the bayou",
        "security_level": "No Security / Barrens",
        "summary": "Private boat graveyard three football fields across against the swamp, cleared of caretakers and dogs for one night's exchange -- and nobody gets out of it without a fight",
        "description": (
            "A private ship junkyard fifty kilometers outside New Orleans, hard against the bayou. Driving "
            "up, the Yard's faded sign shows on a long, battered concrete wall right next to the swamp, with "
            "the hull of an old riverboat jutting over the wall's ragged top; beyond it are other derelict "
            "boats, dozens or possibly hundreds of them, filling an area three football fields in size. A "
            "graveyard for ships, and hopefully not for anyone else. The Yard itself is a maze of hulls from "
            "yachts to fishing trawlers to personal small-engine craft, ringed by a crumbling two-meter wall "
            "broken by four chain-link gates, one on each side, with one left unlocked for the night. Under "
            "a new moon it has a haunted feel, and there is no telling what is behind the next hull."
        ),
        "notes": (
            "Mercy arranged the use of the Yard and had its usual caretakers, workers and guard dogs "
            "evacuated for the night, choosing the place because it should be easy to escape from. The "
            "runners get about half an hour to pick a spot, plan an escape route and prepare; they carry a "
            "Rating 4 tracking signal (which they may plant anywhere rather than keep on them) and the "
            "buyers a signal locator. The buyer's magician scouts astrally first and zips back to his body "
            "if he meets an astral watcher or is attacked; the team then enters close but not clustered, "
            "leaving the payment -- a case of certified credsticks totalling 10 million nuyen -- outside "
            "with a drone or elemental to be brought in once everything checks out. The GM should make sure "
            "that case never actually stays in the runners' hands; that kind of nuyen breaks a campaign. "
            "Optional dressing: ghosts of drowned sailors, shedim or other astral creeps; ghouls, squatters "
            "or paranormals living in one of the hulks; or the bayou forced on the team as the only escape "
            "route, a maze of creek beds and forest patches with alligators, afancs, a behemoth or a nomad "
            "in it."
        ),
    },
]

NPCS = [
    {
        "name": "Gunther Hoff",
        "role": "Proteus telemetry specialist who hires the runners to kidnap his rival for ten days, then is broken and murdered in his own study by the cult he never knew existed",
        "archetype": "Corporate Scientist",
        "title": "Telemetry specialist, Gotterbote payload development team, Proteus AG",
        "race": "Human",
        "gender": "Male",
        "nationality": "German",
        "organization": "Proteus AG",
        "connection": 2,
        "description": (
            "A middle-aged corporate scientist who paces when he argues and slaps his hands on his "
            "superior's desk in frustration. Brilliant, proud and convinced he is right; he read his opening "
            "speech to the runners off a script he had been rewriting and practicing for days, and once it "
            "runs out he improvises and audibly loses confidence. Deep and dry-voiced with a trace of a "
            "German accent over the phone. Nervous, morally conflicted, intelligent and cautious, and "
            "utterly out of his depth: 'Simulations? Bah! A child with a wrist computer could meet those "
            "parameters.' He does not handle death threats well at all."
        ),
        "background": (
            "One of the few scientific geniuses that the smaller, fast-growing Proteus AG relies on instead "
            "of huge staffs. He developed an extraordinarily compact, powerful and sensitive scientific "
            "payload for Gotterbote that almost doubles Hausmann's data throughput in the same mass and "
            "volume, covers a much broader frequency spectrum and returns chromatography data -- but it "
            "failed three of the nine basic telemetry tests on a defective circuit, and Emil Verdan will not "
            "gamble the corporation's last look at the comet on a 75 percent chance. He bought a home in "
            "Kourou years ago while he worked for Saeder-Krupp and did not move into the arkoblock when he "
            "took the Proteus job. Convincing himself he is acting for the good of the corporation, he "
            "decided that if Hausmann simply vanished before the launch, his own design would fly."
        ),
        "notes": (
            "Negotiation 4 with +1 to all his target numbers from sheer unfamiliarity with what runners are "
            "worth. Absolute ceiling 80,000 nuyen for the whole job, hoping for 40,000 or less; 10 percent "
            "up front (negotiable to 20), 30 percent on arrival in Guiana, the rest at the end of the ten "
            "days; he can scrounge more from his corporate savings if pushed. He provides an information "
            "file on Hausmann with photos, physical description and work schedule, rough maps of the "
            "arkoblock floors and exterior, commercial airline tickets to Cayenne, a rental van, the Kourou "
            "bungalow, and a disposable audio-only phone bought for the run. He will not risk his identity "
            "or expose himself to blackmail, discourages any air assault, and if the arkoblock proves too "
            "hard offers the dinner party at his own house without admitting whose house it is. He wants "
            "Hausmann taken at least three days before launch to swap the payload in. Anderson's cell breaks "
            "into his home, beats him, cuffs him to his desk chair and gets the whole story in minutes; he "
            "dictates the meet call at gunpoint and is shot in the forehead the moment it ends. His telecom "
            "was recording a rehearsal for Verdan and captured all of it."
        ),
        "contact_skills": ["Proteus AG's Gotterbote project and payload politics", "Telemetry and guidance instrumentation"],
    },
    {
        "name": "Heinrich Hausmann",
        "role": "Arrogant young Gotterbote project lead, secretly a Winternight sleeper who means to put a nuclear bomb on Halley's Comet and steer the comet into the Earth",
        "archetype": "Corporate Scientist",
        "title": "Project lead, Gotterbote payload package, Proteus AG; Winternight deep-cover agent",
        "race": "Human",
        "gender": "Male",
        "age": 26,
        "nationality": "German",
        "organization": "Proteus AG",
        "connection": 3,
        "description": (
            "Twenty-six, short and slender, and he looks like he would fall over if hit by a stiff breeze, "
            "much less a good punch. Extraordinarily intelligent, with a charming personality and a "
            "remarkable ability to lie his way out of almost any situation; play him sincere and honest "
            "while lying through his teeth. Down-to-earth and friendly with his kidnappers, calm and unafraid "
            "throughout capture and imprisonment, and quietly watching for a chance to run. He is also quite "
            "capable of killing a majority of the Earth's population and more than willing to do it: years of "
            "indoctrination in Winternight's principles made him an almost perfect psychopath, though he "
            "never needed much help along the way. He wears a golden ring bearing the Proteus logo."
        ),
        "background": (
            "German national, born 2034, BSE in Electronic Engineering from Aachen University of Technology "
            "and four years of advanced study at the Astrophysics Institute of Potsdam, with excellent "
            "grades and employee evaluations his whole career and a national science prize in his senior "
            "year. Unmarried, no living family. Believed to have designed the primary sensor systems for "
            "Proteus' Treffpunkt Raumhaufen platform, which is why the regional director assigned him "
            "personally to Gotterbote. None of that was chance: years of targeted scientific training and "
            "referrals from other highly placed Winternight puppets were carefully designed to put him in a "
            "crucial role on Proteus' Halley probe projects. He refuses to let anyone see a schematic of his "
            "payload for a very good reason -- his mission is to slip a Winternight drone into the "
            "Gotterbote payload just before launch, guide the probe to a soft landing on the comet, position "
            "it, and then detonate its payload: a small but powerful nuclear bomb meant to knock Halley off "
            "course and into the Earth."
        ),
        "notes": (
            "Stats p.32: B3 Q4 S3 C5 I6 W6 E3, Reaction 5(9), Init 5+1D6, Rigging Init 9+3D6, Combat Pool 8, "
            "Control Pool 9, Karma/Prof 2/2; Car 2 (Remote Operations 4), Etiquette 4 (Corporate 6), "
            "Leadership 4, Negotiation 6, Unarmed 3; Astrophysics 6, Computer 5, Electronics 6, Electronics "
            "B/R 6. Alphaware: datajack, 100 Mp headware memory, Math SPU 3, vehicle control rig 2 -- and a "
            "MICROBOMB. The rig runs survey drones and remote equipment; he is a lousy combat driver. No "
            "combat skills worth speaking of: attacked, he runs and screams for the guards, and a tranq dart "
            "or stun spell takes him. He will stall attackers until his Winternight bodyguard drone arrives "
            "and try to use the fight as cover to escape. Interrogated he admits his name and his job, "
            "offers sincerely to double whatever the runners are being paid, claims the ring came with the "
            "job and that he knows nothing of the drone, and shuts up the instant he realizes Analyze Truth "
            "is running. Push magical coercion to the edge of revealing Winternight and he triggers the "
            "cranial bomb and dies instantly. The ring was made for him by Winternight: it carries the Safe "
            "Target chip that stops cult drones firing on him and transmits constantly out to a few hundred "
            "meters. Legwork: Matrix research only, TN 6."
        ),
    },
    {
        "name": "Anderson",
        "role": "Toxic Raven shaman and leader of the Guiana Winternight cell; wears Hoff's face to buy Hausmann back, then frames the runners for the murder he committed",
        "archetype": "Toxic Shaman",
        "title": "Cell leader, Winternight (French Guiana)",
        "race": "Elf",
        "gender": "Male",
        "nationality": "German",
        "organization": "Winternight",
        "connection": 3,
        "description": (
            "A tall, slender elf with long, wavy blond hair and dark brown eyes, handsome, with a pleasant "
            "if cool demeanor and a smooth, cultured German accent -- and a voice that turns oily and sharp "
            "when he is crossed. He acts as though he is in total control no matter how badly he is "
            "outnumbered, which may be the creepiest thing about him. Merciless: he will sacrifice anyone "
            "and anything to achieve the destruction of all life on Earth. 'Patience, Zwei. Let us not harm "
            "Herr Hoff, at least until he has told us what we want to know.' And later: 'Does it really "
            "matter? You will get your money, and your original employer will never complain about your "
            "service. You won't hear from him again.'"
        ),
        "background": (
            "Born in one of Germany's most heavily polluted states, Anderson always believed that mankind "
            "should be punished for its abuse of the Earth and its creatures. He never fell from the normal "
            "shaman's path into the Toxic Way -- he started out toxic; Winternight simply gave a path to the "
            "beliefs he grew up with. He runs the Guiana cell, handles Hausmann's reports, and acted the "
            "moment those reports suggested the ambitious Hoff might try something underhanded that could "
            "endanger Gotterbote."
        ),
        "notes": (
            "Stats p.28: B4 Q7 S4 C4 I6 W6 E6 M8(11) R6, Init 6+1D6, Astral Combat 9, Combat 9, Potency 3, "
            "Spell 6, Karma/Prof 4/4; Aura Reading 4, Conjuring 5, Edged Weapons 5 (Sword 7), Etiquette 4, "
            "Interrogation 5, Intimidation 5, Leadership 5, Negotiation 4, Sorcery 7, Stealth 4, Unarmed 4; "
            "Kourou 4. Totem Raven (toxic): +2 dice on Manipulation spells and to summon toxic sky spirits, "
            "+1 to all magical target numbers when not under the open sky. Spells: Agony 5, Alter Memory 5, "
            "Armor 5, Compel Truth 4, Detect Individual 4, Dream 4, Eyes of the Pack 4, Influence 5, "
            "Lightning Bolt 6, Manaball 5, Mind Probe 5, Physical Mask 5, Redirect 5, Thunderclap 4. Force 2 "
            "weapon focus sword (6M), knife, secure clothing and Secure Ultra-vest 4/2. Assisted by two "
            "shamans with identical stats for the Ritual Tracking that finds Hausmann. At the club he pays "
            "the balance, then a 50 percent 'flexibility bonus', then double; Hausmann alive matters more "
            "than the money or his own people's lives, so in a fight he targets whoever threatens Hausmann "
            "first, uses no area damage near him, and is likely to summon a high-Force spirit. A Resistance "
            "Test or successful assensing sees through the Physical Mask, and he does not know the details "
            "of any conversation the runners had with Hoff except the setup call."
        ),
    },
    {
        "name": "Howe",
        "role": "Winternight's rigger, the only man besides Anderson and Hausmann who knows who he really works for; runs the cell's drones and the frame-up call",
        "archetype": "Rigger",
        "title": "Rigger, Winternight (French Guiana cell)",
        "race": "Ork",
        "gender": "Male",
        "organization": "Winternight",
        "connection": 2,
        "description": (
            "An ogre, and bitter about it. Born to a wealthy human family who found his race an "
            "embarrassment in polite society and disowned him at an early age, he grew into a resentful man "
            "who is genuinely happy to help Winternight destroy mankind. He waits in a nondescript car "
            "outside the fence at the Sporting and Aero Club, running two drones by remote deck, and brings "
            "them in low on Anderson's signal to encourage cooperation without firing a shot."
        ),
        "background": (
            "Disowned young by a wealthy human family for being born metahuman, Howe found in Winternight a "
            "cause that made his grudge into a religion. He is one of only three people in the Guiana "
            "operation who know the cult's name -- himself, Anderson and Hausmann -- and he handles all of "
            "its untraceable custom drones, including the one hovering over Hausmann's morning jog and the "
            "high-altitude unit that watched Hoff's house."
        ),
        "notes": (
            "Stats p.28: B5 Q4 S5 C3 I4 W4 E2.3, Reaction 4(8), Init 4+1D6, Rigging Init 8+3D6, Combat Pool "
            "6, Control Pool 8, Karma/Prof 2/3; Car 6, Electronics 4, Etiquette 2 (Street 4), Gunnery 6, "
            "Pistols 4, Vectored Thrust Aircraft 3 (Remote Operations 6); Kourou 5. Savalette Guardian with "
            "smartgun link, datajack, smartlink, vehicle control rig 2, secure jacket 5/3, Remote Control "
            "Deck 6. Vehicles: a rigger-equipped but otherwise nondescript Toyota Elite sedan and a Ford "
            "Americar. If he survives Masquerade and sees the runners trying to surrender at Hoff's house, "
            "he has a drone open fire on the Kourou police from the direction of the house so the police "
            "shoot the witnesses. A live Anderson or Howe is the reason Winternight might come back at the "
            "team later -- with hired guns rather than cult members, to limit exposure."
        ),
    },
    {
        "name": "Ein, Zwei and Drei",
        "role": "Three loyal local razorboys who do Anderson's wet work without the faintest idea he serves an apocalypse cult; the trio who beat and shot Gunther Hoff on camera",
        "archetype": "Street Samurai",
        "title": "Anderson's razorboys (Kourou)",
        "race": "Human",
        "gender": "Male",
        "organization": "Winternight",
        "connection": 1,
        "description": (
            "Three cybered local muscle who have worked for Anderson for a year or so. He pays them well, "
            "bought most of their cyberware and hands out BTL chips as a reward for a job well done, so they "
            "are very loyal -- and as for his occasional mutterings about destroying all life on Earth, "
            "well, who takes those things seriously? On the recording one of them kicks Hoff in the ribcage "
            "as he tries to rise, another cocks a revolver noisily next to his ear to make a point, and the "
            "first puts the barrel in the center of his forehead and fires. 'Won't look like a suicide, shot "
            "there,' the second grunts. The first shrugs and drops the pistol on the floor."
        ),
        "notes": (
            "One stat block for all three, p.28: B5(7) Q5 S5 C3 I3 W4 E2, Reaction 4(6), Init 4+1D6 (6+2D6), "
            "Combat Pool 6, Karma/Prof 3/4; Car 3, Cyber-Implant Combat 5, Etiquette 2 (Street 4), "
            "Intimidation 4, Stealth 4, Submachine Guns 6; Kourou 4. Cybereyes (flare compensation, "
            "thermographic, low-light), Dermal Plating 2, retractable spur (5M), smartlink, Wired Reflexes 1. "
            "SCK Model 100 with APDS, smartgun link and sound suppressor; secure jacket 5/3. Also carries a "
            "small-caliber revolver -- the one left beside Hoff's body. They hide inside the club building "
            "during the Masquerade meet as Anderson's ace in the hole and he will not reveal them unless "
            "combat breaks out. Runners who saw Anderson unmasked or fought the razorboys will certainly "
            "recognize them in the murder recording. Survivors get sniper rifles in the Face to Face "
            "cordon, to keep the team from reaching custody alive."
        ),
    },
    {
        "name": "Emil Verdan",
        "role": "Hoff's superior at Proteus, who ruled Hausmann's payload onto the probe and never learns what that decision set in motion",
        "archetype": "Corporate Manager",
        "title": "Gotterbote project manager, Proteus AG (Iles du Salut arkoblock)",
        "race": "Human",
        "gender": "Male",
        "nationality": "German",
        "organization": "Proteus AG",
        "connection": 3,
        "description": (
            "A patient manager who stifles his sighs, steeples his fingers on the desk and tries to explain "
            "himself to brilliant men behaving like spoiled children fighting over who Mama liked best. He "
            "tosses his hands up in exasperation rather than raise his voice, and he does not finish the "
            "sentence about what happens if the Regional Director's personal appointment does not get what "
            "he wants. 'This is our last chance at getting a good look at the comet, and if it fails for any "
            "reason, Proteus will have wasted billions of nuyen and tens of thousands of man-hours. I'd "
            "rather have a 100 percent chance of getting his data than a 75 percent chance of getting "
            "yours.'"
        ),
        "background": (
            "He runs the Gotterbote payload team and has repeatedly asked the temperamental Hausmann to "
            "consult with the rest of the staff, without success; he will not prod harder for fear Hausmann "
            "walks off the project at this late date, because the Regional Director assigned him personally. "
            "He acknowledges that Hoff's instrumentation may well be better, but Hoff's cluster failed three "
            "of nine telemetry tests and there is only one chance to get this right."
        ),
        "notes": (
            "No stat block; he never appears on stage. He is the man Hoff was rehearsing a speech to when "
            "Anderson kicked the door in -- 'Herr Verdan, Heinrich would want us to continue with the "
            "launch. I know he would. But we can't use his payload package without him' -- which is exactly "
            "why the recording exists at all. He is the natural recipient for the murder video if the "
            "runners want Proteus to check the payload before it flies, and the man who would have to sign "
            "off on Hoff's package replacing Hausmann's after the abduction. A useful long-term corporate "
            "contact for anyone who saves Proteus a billion nuyen and its public reputation."
        ),
        "contact_skills": ["Proteus AG aerospace project management", "Gotterbote launch scheduling and payload approvals"],
    },
    {
        "name": "Bala",
        "role": "Bitter Guianan gun-runner who sells the team its weapons out of a boat at a fishing-village dock, then demands double at gunpoint",
        "archetype": "Smuggler",
        "title": "Independent arms smuggler, Guianan coast",
        "race": "Human",
        "gender": "Female",
        "age": 45,
        "connection": 2,
        "description": (
            "A slender but muscular human woman, forty-something, in faded combat fatigues, with long grimy "
            "auburn hair and a face pockmarked with tiny scars. She does not appear to be carrying any "
            "weapons -- the sawed-off shotgun is stashed near the crates -- and she gives arrivals a "
            "once-over before jerking her head toward the oilcloth-covered crates at the back of her boat. "
            "'Let's get this over with.' Tough and confident, she gambles only where she knows the odds are "
            "in her favor, and she holds all the cards at her own dock."
        ),
        "background": (
            "A smuggler's daughter who has been running contraband all her life, since the days when "
            "Amazonia was still Brazil. She started out an idealistic kid trying to help supply the "
            "Amazonian resistance with what it needed to fight back against the government; now she is "
            "bitter and disillusioned and her only concern is looking out for herself. The shipment she "
            "sells the runners was originally bound for Amazonian revolutionaries in Belem."
        ),
        "notes": (
            "Stats p.14: B4 Q4 S4 C4 I4 W5 E6 R4, Init 4+1D6, Combat Pool 6, Karma/Prof 3/3; Clubs 4, Edged "
            "Weapons 4, Etiquette 3 (Smuggler 5), Intimidation 4, Leadership 5, Motorboat 5, Motorboat B/R "
            "4, Negotiation 5, Pistols 4, Shotguns 4; Smuggling Routes 6. Sawed-off Remington 990, knife, "
            "Secure Ultra-Vest 3/2. Stock: nothing above Availability 4, no heavy or special weapons, and "
            "double the cost including Street Index; the guns are used but in good working order and the "
            "ammunition is crated separately, so nothing on the boat is loaded. She lets only one or two "
            "runners aboard and keeps the rest on the dock under Paco's gunsights, then demands double the "
            "agreed price for 'an unexpected business expense'. Look dangerous enough -- numbers, obvious "
            "combat cyberware, a visible magician -- and she settles for the original price after a lot of "
            "haggling; refuse and she simply has them escorted off at gunpoint, since she gains nothing by "
            "killing them. Her boat is an unarmed Blohm & Voss River Commander and the hold has a Spike "
            "disposable rocket launcher with an anti-vehicular rocket or two for emergencies."
        ),
        "contact_skills": ["Guianan coastal smuggling routes", "Small arms out of the Amazonian pipeline"],
    },
    {
        "name": "Ebaninho",
        "role": "Bala's cyber-spurred dwarf muscle, six months on the crew and loyal to nobody",
        "archetype": "Street Samurai",
        "title": "Crewman and enforcer for Bala",
        "race": "Dwarf",
        "gender": "Male",
        "connection": 1,
        "description": (
            "Pronounced eh-bah-NEEN-yu. A young dwarf with a bad attitude and the hardware to back it up, "
            "armed for bear and standing at his boss's shoulder when the buyers arrive. He is one of the two "
            "who take a runner aboard the boat to inspect the merchandise, and he is the one Bala counts on "
            "if the inspection turns into a problem."
        ),
        "background": (
            "Originally from Amazonia like Bala, but unlike her he never had any illusions that running guns "
            "was anything other than a source of money. He has been working with her for about six months "
            "and has not developed any particular loyalty to her."
        ),
        "notes": (
            "Stats p.14: B7 Q4 S5 C2 I4 W6 E4.5, Reaction 4(5), Init 4+1D6 (5+2D6), Combat Pool 7, "
            "Karma/Prof 2/3; Cyber-implant Combat 5, Etiquette 2 (Smuggler 4), Intimidation 4, Motorboat 3, "
            "Motorboat B/R 3, Pistols 4, Submachine Guns 5; Smuggling Routes 4. Beretta Model 70 with laser "
            "sight and sound suppressor plus two spare clips, Browning Max-Power, retractable spur (5M), "
            "Boosted Reflexes 2, Secure Ultra-Vest 3/2. His lack of loyalty is the crack in Bala's extortion "
            "play: a team that outguns the crew can probably buy or bluff him out of the fight rather than "
            "shoot their way off the dock. If the runners take the boat, they still need someone who can "
            "pilot it and somewhere to keep it."
        ),
    },
    {
        "name": "Paco",
        "role": "Bala's ork gunman, ex-Caribbean League pirate, holding the dock with an AK-97 while the deal goes bad on the boat",
        "archetype": "Street Samurai",
        "title": "Crewman and enforcer for Bala",
        "race": "Ork",
        "gender": "Male",
        "nationality": "Aztlan",
        "connection": 1,
        "description": (
            "A big ork who grins a broken-tusked grin at the runners over his AK-97 while they wait on the "
            "dock. Not especially bright, but tough and he knows how to fight. He is the one left watching "
            "whoever does not go aboard, which makes him the first target and the first problem if the "
            "extortion turns into a firefight."
        ),
        "background": (
            "Originally from Aztlan, he fell into crime at a young age and served as a pirate crewman in the "
            "Caribbean League before joining up with Bala."
        ),
        "notes": (
            "Stats p.14: B8 Q4 S7 C2 I2 W3 E6 R3, Init 3+1D6, Combat Pool 4, Karma/Prof 2/3; Assault Rifles "
            "5, Clubs 4, Etiquette 1 (Street 3), Intimidation 3, Launch Weapons 2, Motorboat 3, Motorboat "
            "B/R 3, Unarmed 5; Smuggling Routes 2. AK-97 with two spare clips and a sound suppressor, club "
            "(7M Stun), Secure Ultra-Vest 3/2. His Launch Weapons skill is the reason the Spike rocket "
            "launcher in the hold matters. The dirt-poor villagers take cover in their huts if shooting "
            "starts and stay there, having no interest in helping either side."
        ),
    },
    {
        "name": "Mr. Johnson (Lickety-Splits)",
        "role": "Twisted, squeal-voiced fixer for an unnamed megacorp who buys the Gagarin datasteal over ice cream and the module recovery over a whiskey in a log cabin",
        "archetype": "Corporate Fixer",
        "title": "Mr. Johnson for the Gagarin operation (employer chosen by the GM)",
        "race": "Human",
        "gender": "Male",
        "connection": 4,
        "description": (
            "Extremely short but not a dwarf, with gnarled, twisted, bent limbs that all appear to still be "
            "functional, a scarred body and a thin, tightly groomed mustache; his voice is a shrill, nasal "
            "squeal, as if his vocal chords were twisted in accordance with the rest of him. He is "
            "noticeably disfigured and it is not clear what did it, and woe to anyone who asks. His mind is "
            "sharp, his manner calm and friendly, and he likes to speak in colloquialisms to put runners at "
            "ease; he is not self-conscious about his condition at all and it has in fact made him more "
            "confident. He dresses well but with a casual element so he does not look like a corp shark. "
            "'I'm glad you could all make it on such short notice. Please sit. Would any of you like some "
            "ice cream? It's quite good here.'"
        ),
        "background": (
            "He has worked for his employer for several years with a good track record, and when news of the "
            "Gagarin transmission came his name was on the short list to handle the shadow side of the "
            "operation. He researched the runners well enough to know they were qualified for the first job "
            "and had other skills useful for a follow-up. Whom he actually works for is the gamemaster's "
            "choice -- Ares, Aztechnology, Saeder-Krupp, Shiawase, or Novatech, Proteus, Shibata or a "
            "government -- and that choice decides both the gear he can supply in Thunder Bay and whether "
            "the module is to be recovered, wiped, corrupted or destroyed."
        ),
        "notes": (
            "The book never gives him a name; this row files him under a disambiguated one. Stats p.55: B3 "
            "Q3 S2 C5 I6 W7 E5 R4, Init 4+1D6, Combat Pool 8, Karma/Prof 6/4; Computer 4, Electronics 4, "
            "Etiquette 6 (Corporate 7, Street 8), Interrogation 4, Leadership 5, Negotiation 7, Pistols 4, "
            "Small Unit Tactics 4; Corporate Policies 6, English 4, Fixers 4, Japanese 4, Law 4, Megacorp "
            "Black Ops 6, Security Procedures 5, Shadowrunners 5. Lined coat 4/2. Two ork bodyguards in "
            "matching thigh-length leather coats, dark jeans and boots (B6 Q5 S4 C3 I4 W3.2, Reaction 4(6), "
            "Combat Pool 7, Karma/Prof 5/4; alphaware Boosted Reflexes 3, cybereyes, smartlink; HK 227, Ares "
            "Viper Slivergun, smoke grenade, lined coat, Eurocar Westwind 2000 with Armor 2) who will lay "
            "down their lives and get him out fast. Job one: 8,000 nuyen each plus a 10 percent bonus inside "
            "48 hours, up to 25 percent in advance, +500 each or +5 percent on the bonus per success on a "
            "Negotiation (5) Test, plus 1,000 nuyen per search success above five on delivery. Job two: "
            "500 nuyen a head just to fly out on a week's notice, then 20,000 each. Legwork (TN 6): 'the "
            "shriveled shrimp with the shrieky voice and the ork duo -- weird and eccentric, but solid'; he "
            "never screwed anyone over, rehires teams as long as they produce, and tends to hire for jobs "
            "with more to them than meets the eye."
        ),
        "contact_skills": ["Megacorp black ops contracting", "Orbital and probe-race industry gossip"],
    },
    {
        "name": "Ivan Kolenko",
        "role": "Gagarin project manager at Yamatetsu, first to realize the dead probe has come back on line",
        "archetype": "Corporate Manager",
        "title": "Project manager, Gagarin probe, Yamatetsu Corporation",
        "race": "Human",
        "gender": "Male",
        "organization": "Yamatetsu Corporation",
        "connection": 3,
        "description": (
            "The man who was buried in a progress report when the console lit up and started beeping. He "
            "keeps his head while the engineer nearly jumps out of his skin, checks the tracking before he "
            "believes it, and then enjoys himself a little at his colleague's expense -- 'Congratulations, "
            "Yoshi. It looks like we won't have to write off Gagarin after all,' delivered with a smirk and "
            "a smack on the back, knowing perfectly well the news could throw a three-pack-a-day man into a "
            "full-on coronary."
        ),
        "background": (
            "He has run the Gagarin project through its brief triumph in 2061 and the humiliation that "
            "followed, when contact was lost right after the probe's sensors began gathering data on the "
            "comet and every attempt to re-establish it failed. Nobody ever learned what went wrong. When "
            "the burst transmission arrives in early 2062, his team goes to twenty-four-seven work under "
            "Saru Iwano's direct orders and total secrecy."
        ),
        "notes": (
            "No stat block. Prologue only, but he is the natural point of contact for anything technical "
            "about Gagarin: the probe is intact on long-range monitoring, guidance is operational, the "
            "communications system is only half-functional, the sensor memory module is offline and cannot "
            "be read remotely, and the probe is still programmed to deposit that module on its Earth flyby "
            "-- slightly off course, so nobody knows where. His name and the transmission logs are exactly "
            "what a decker who runs the Gagarin Transmission Host on the Shibanokuji PLTG comes away with. "
            "Iwano's demand for a list of everyone in the facility who knows within the hour means Kolenko, "
            "Hakeda and Richards are all now personally on the hook."
        ),
        "contact_skills": ["Yamatetsu deep-space probe telemetry", "Gagarin mission history and status"],
    },
    {
        "name": "Yoshi Hakeda",
        "role": "Yamatetsu executive over the Gagarin project who has to phone the CEO with half good news and half catastrophe",
        "archetype": "Corporate Executive",
        "title": "Executive responsible for the Gagarin project, Yamatetsu Corporation",
        "race": "Human",
        "gender": "Male",
        "organization": "Yamatetsu Corporation",
        "connection": 3,
        "description": (
            "Three packs of cigarettes a day leave him breathless from even the briefest physical exertion, "
            "and he arrives at the control room gasping, chest heaving, and is speechless for a full minute "
            "before he can flip a cigarette between his lips and light it. He coats his report to his boss "
            "in an air of false confidence that fools nobody, and pales as he dials. 'I knew everything was "
            "going to be okay. I just knew it.' By the end of the call he is standing alone in a corridor "
            "with his thirty-second cigarette of the young day and a life that has just become hell."
        ),
        "background": (
            "He carried the Gagarin project's public failure in 2061 and is the man Saru Iwano holds "
            "personally responsible for its resurrection. Iwano orders total secrecy -- not even word of the "
            "probe's return may leak, because if the module cannot be retrieved or holds nothing, Yamatetsu "
            "looks like a bigger fool than before -- twenty-four-seven work, immediate updates on anything, "
            "and a list within the hour of every person in the facility who knows."
        ),
        "notes": (
            "No stat block. 'We cannot claim a victory until we have concrete sensor information in our "
            "hands... If that is the case, I would have preferred Gagarin to have been lost forever.' Hakeda "
            "is the man who signs off on both Yamatetsu recovery teams, and therefore the man whose career "
            "ends when the first one is wiped out by Manitou militia and the second one comes home empty. "
            "The secrecy he is enforcing is exactly why other corps noticed the traffic in the first place, "
            "and why an unnamed rival could put shadowrunners on the Alaxa uplink before Yamatetsu knew "
            "anyone was looking."
        ),
        "contact_skills": ["Yamatetsu corporate hierarchy and internal politics", "Space division project funding"],
    },
    {
        "name": "Richards",
        "role": "Yamatetsu console engineer who caught Gagarin's burst transmission and had to say out loud that the sensor module was offline",
        "archetype": "Corporate Technician",
        "title": "Telemetry engineer, Gagarin project, Yamatetsu Corporation",
        "race": "Human",
        "gender": "Male",
        "organization": "Yamatetsu Corporation",
        "connection": 2,
        "description": (
            "The engineer at the fully lit console, nearly jumping out of his skin with excitement -- 'It's "
            "back! Gagarin sent us a signal!' -- and certain of it: 'Positive, the datastream came from dead "
            "center on our satellite tracking.' Then he keeps his eyes locked on the screens to catch "
            "everything, and repeats the bad news flatly for two men who heard him perfectly well the first "
            "time. 'The sensor module. It's offline.'"
        ),
        "notes": (
            "No stat block; prologue only. His read on the probe is the technical baseline for the whole "
            "adventure: corruption in the data and numbers that make no sense, filtering underway, only "
            "basic housekeeping data with no images or scientific measurements, guidance and most other "
            "systems operational, communications half-functional, the probe intact on long-range monitoring "
            "though that is hard to judge at range, the memory inaccessible, and the module still due to be "
            "deposited on the Earth flyby from a slightly off course trajectory. He is one of the names on "
            "the list Iwano demanded of everyone who knows, which makes him a man with a great deal to lose "
            "and a plausible leak for a rival corp to have turned."
        ),
        "contact_skills": ["Deep-space telemetry and probe diagnostics"],
    },
    {
        "name": "Alice Hernandez",
        "role": "Alaxa's licensed security mage, who warded the building and the labs and will fight only as far as she has to",
        "archetype": "Corporate Mage",
        "title": "Contract security mage, Alaxa (Everett)",
        "race": "Human",
        "gender": "Female",
        "organization": "Alaxa",
        "connection": 2,
        "description": (
            "A licensed corporate security mage with a protective streak she has had all her life, which is "
            "what made security such easy work for her to find. She does not like using her magic to hurt "
            "people and will only overcome that distaste to protect herself or her charges -- which shapes "
            "her whole spell list, heavy on barriers, healing and nuisance effects and light on anything "
            "lethal. She cannot be on duty all the time, so she staffs the facility in staggered eight-hour "
            "shifts and lets the wards do the watching when she is elsewhere."
        ),
        "background": (
            "She discovered her magical talent on a field trip to Aztlan when she was eighteen and has been "
            "refining it ever since. Alaxa hired her as its single licensed mage because a firm hiding its "
            "Yamatetsu ownership cannot very well import Yamatetsu's magical security along with its "
            "guards -- the same reasoning that has off-duty Lone Star officers walking the halls."
        ),
        "notes": (
            "Stats pp.39-40: B4 Q4 S4 C4 I5 W5 E6 M6, Init 4+1D6, Astral Init 24+1D6, Astral Combat 7, "
            "Combat 7, Spell 5, Karma/Prof 3/3; Aura Reading 5, Biotech 1 (First Aid 3), Conjuring 6, Edged "
            "Weapons 4, Electronics 3, Etiquette 3 (Corporate 5), Negotiation 4, Pistols 4, Sorcery 6, "
            "Stealth 3; Magical Threats 4, Security Procedures 3, Small Unit Tactics 3. Spells: Armor 4, "
            "Astral Barrier 6, Entertainment 4, Hot Potato 6, Levitate 4, Magic Fingers 5, Manabolt 5, "
            "Physical Barrier 4, Stench 5, Treat 5, Wreck 5. Expendable focus 3 (Hot Potato), expendable "
            "focus 4 (Manabolt), sustaining focus 6 (Physical Barrier); Defiance Super Shock taser, "
            "splatgun, knife, armored coat 2/1, PanicButton, wristphone, access card. Two elementals on "
            "call: Force 3 air (3 services) and Force 5 water (3 services). Her Force 4 wards cover the "
            "building exterior, each research lab and the security office, and alert her wherever she is -- "
            "beating them quietly is the single hardest part of the Alaxa run. When she is on site, the "
            "guard count drops from three to two."
        ),
    },
    {
        "name": "Charlie Davis",
        "role": "Married Alaxa executive whose after-hours affair with his secretary makes him the most cooperative man in the building",
        "archetype": "Corporate Executive",
        "title": "Low-level executive, Alaxa (Everett)",
        "race": "Dwarf",
        "gender": "Male",
        "age": 52,
        "organization": "Alaxa",
        "connection": 2,
        "description": (
            "A fifty-two-year-old married dwarf and a low-level executive, and one of the last two people in "
            "the building after the five o'clock exodus -- for reasons that become obvious when runners "
            "creeping the halls hear pleasurable moans and follow them to find him and his secretary "
            "engaged atop a copy machine. He will cooperate with anyone for fear of exposure, deny "
            "everything adamantly at the same time, and plead for the secret to be kept, because his wife at "
            "home would kill him if she found out."
        ),
        "background": (
            "For the last three months he and Marla Munns have kept their trysts to passionate after-hours "
            "encounters at the office and have been debating whether to venture out in public. The security "
            "guards know all about it and ignore them aside from regular joking."
        ),
        "notes": (
            "No stat block; a roleplaying encounter (p.41). He and Marla have little loyalty to Alaxa and "
            "will trade cooperation, a little nuyen, or information for silence -- useful if the team is "
            "stumped on the server room, the satellite dish or the uplink schedule. Handled badly he is "
            "still not a fighter; handled well he is a standing lever on a Yamatetsu front company, and a "
            "man whose access card opens more than his job requires."
        ),
        "contact_skills": ["Alaxa internal operations and personnel", "Corporate gossip on Yamatetsu's Everett holdings"],
    },
    {
        "name": "Marla Munns",
        "role": "Alaxa secretary caught in the after-hours affair, as motivated as her boss to make trespassers go away quietly",
        "archetype": "Corporate Staff",
        "title": "Secretary to Charlie Davis, Alaxa (Everett)",
        "race": "Human",
        "gender": "Female",
        "age": 34,
        "organization": "Alaxa",
        "connection": 1,
        "description": (
            "Thirty-four and a multi-divorcee, and one half of the reason the Alaxa building is not quite as "
            "empty after hours as the security schedule implies. Caught, she is cooperative out of fear of "
            "exposure, denies the affair adamantly all the same, and pleads for the runners' silence. Like "
            "her boss, she has little loyalty to Alaxa and rather more to her own reputation."
        ),
        "background": (
            "Three months into an affair with a married executive, conducted entirely in the office after "
            "hours, with the guards' amused tolerance and an ongoing argument about whether to go public."
        ),
        "notes": (
            "No stat block; the other half of the p.41 roleplaying encounter. As a secretary she is the one "
            "who actually knows the building's paperwork -- schedules, deliveries, who has which access card "
            "-- which makes her the more useful of the pair to a team that needs something specific rather "
            "than a bribe. If the runners handle the discovery with any grace, both of them will be quite "
            "sure they saw nothing at all."
        ),
        "contact_skills": ["Alaxa scheduling, deliveries and access records"],
    },
    {
        "name": "Thunderwalker",
        "role": "Niwimaja's militia leader, the elf whose elites wiped out the first Yamatetsu team and carried the module home to Cloud Talon",
        "archetype": "Tribal Warrior",
        "title": "Leader of the Niwimaja militia, Manitou Tribe",
        "race": "Elf",
        "gender": "Female",
        "nationality": "Cree (Manitou Tribe)",
        "organization": "Manitou Tribe",
        "connection": 3,
        "description": (
            "An elven woman of average physical dimensions with short cropped pitch-dark hair and piercing "
            "black eyes. Her whole demeanor speaks of career military, from her short economical meals to "
            "the march that passes for a walk, and she is never without a weapon of some sort, from her "
            "wicked combat knife to the long heavy assault rifle whose barrel is notched all along its "
            "length. A no-nonsense woman who will speak out vehemently against any outside influence among "
            "the tribe, and who arrives to meet strangers with an armed patrol that materializes out of the "
            "nooks and crannies and gestures them along without a word."
        ),
        "background": (
            "Cree by descent and upbringing. She once served in the AMC military -- ironically specializing "
            "in the combat applications of modern technology -- before becoming disgusted with the anti-elf "
            "and anti-woman attitudes she frequently encountered there. She has no particular bent against "
            "technology herself, but is exceptionally loyal to the Manitou cause and extremely hostile to "
            "anyone who threatens it, megacorps above all. She trained many of Niwimaja's militia herself, "
            "and she has accepted Cloud Talon as her superior officer since the moment the two met and obeys "
            "his edicts over anyone else's."
        ),
        "notes": (
            "Stats p.56: B5 Q7 S5 C5 I5 W5, Init 6+1D6 (2D6), Combat Pool 8, Karma/Prof 5/4 (Essence and "
            "Reaction garbled in the OCR); Assault Rifles 6, Athletics 5, Biotech 2 (First Aid 4), Car 2, "
            "Edged Weapons 4 (Knife 6), Etiquette 3, Intimidation 4, Leadership 5, Pistols 3, Projectile "
            "Weapons 2 (Pull Bow 4), Small Unit Tactics 4, Stealth 7; Algonkian 4, AMC Military 5, AMC "
            "Politics 4, Cree 4, English 3, Hunting 5, Magic Background 3, Manitou Policies 4, Niwimaja Area "
            "5, Paranormal Animals 3. Bioware: sleep regulator, synaptic accelerator 1. AK-97 with laser "
            "sight, combat knife 6M, camouflage jumpsuit 3/2, trauma patch, medkit. She and her elites set "
            "the ambush that killed all six of the first Yamatetsu team after their leader made the wrong "
            "move, stripped the bodies, took their own casualties home and left the corpses for the wolves. "
            "She thinks the runners are dangerous but follows Cloud Talon's lead on how to treat them, keeps "
            "them under guard until Youngman has questioned them, has an obviously low opinion of the "
            "Yamatetsu team, and will find the team beds in a common house. A half-lie about hunting a "
            "meteor gets them told it fell a day southwest and asked to move along. She is also a possible "
            "romance for a runner who earns it."
        ),
        "contact_skills": ["Manitou militia and border patrol movements", "Wilderness travel north of the Churchill River"],
    },
    {
        "name": "Chief Robert \"Silver-Tongue\" Youngman",
        "role": "Founding elder and elected chief of Niwimaja, the greatest ally an outsider could win among the Manitou and the hardest",
        "archetype": "Tribal Leader",
        "title": "Chief of Niwimaja and founder of the Manitou Tribe",
        "race": "Elf",
        "gender": "Male",
        "age": 50,
        "nationality": "Manitou Tribe",
        "organization": "Manitou Tribe",
        "connection": 4,
        "description": (
            "A physically imposing elf who has just turned fifty and does not look it, wearing stereotypical "
            "native garb despite being an Anglo mutt, with a few distinctive orange feathers always tied "
            "into his hair or headdress and a palpable air of authority about him. His voice can be "
            "threatening and soothing at the same time, and beneath the serious demeanor is a joy that can "
            "be both seen and felt; he often looks upon the world with the eyes of a child. He greets "
            "strangers warming his hands at the council hall fire: 'I can never seem to get all the cold out "
            "of my bones during this time of year. I am Chief Youngman. I suspect that you want to talk.'"
        ),
        "background": (
            "One of the founders of the Manitou tribe and a protege of Adrian Silvermoon, and later one of "
            "those who ousted her. An educated and influential man both inside and outside the tribe, and a "
            "skilled diplomat who places the value and needs of the tribe above anyone's personal needs, his "
            "own included, always choosing for the whole and not the one. He is just and fair and refuses to "
            "decide anything without as much information as he can get, without ever falling into the trap "
            "of indecisiveness. He backs Cloud Talon thoroughly in public and berates him in private for "
            "refusing to bring the Manitou Inner Council and other tribal authorities into the module affair."
        ),
        "notes": (
            "Stats pp.56-57: B7 Q4 S5 C6 I5 W6 E6 R4, Init 4+1D6, Combat Pool 7, Karma/Prof 10/4; Athletics "
            "4, Biotech 5, Edged Weapons 3, Etiquette 4, Instruction 4, Interrogation 2 (Lie Detector 4), "
            "Leadership 6, Negotiation 4 (Bargain 6), Projectile Weapons 1 (Pull Bow 3), Rifles 4; Algonkian "
            "3, Administration 4, AMC Corps 3, AMC Politics 6, English 5, Haudenosaunee 3, Manitou Policies "
            "6, Niwimaja Area 5, Painting 6. His Lie Detector specialization matters: a team that lies to "
            "him at the first interview is unlikely to get anything afterwards. He and Thunderwalker will "
            "not surrender any information about the module until the elders have been consulted, but after "
            "the interrogation the runners may stay and move freely so long as they cause no trouble. If "
            "runners take hostages he will hand the module over -- and the tribe will then hunt them out of "
            "Manitou territory and may hand their names to Yamatetsu."
        ),
        "contact_skills": ["Manitou tribal politics and the Inner Council", "AMC national politics and corporate dealings"],
    },
    {
        "name": "Cloud Talon",
        "role": "Niwimaja's medicine man by consensus, who buried the Gagarin module in a warded crate under the town and will not tell anyone why",
        "archetype": "Shaman",
        "title": "Unofficial Medicine Man of Niwimaja; Haudenosaunee shaman, Initiate Grade 3",
        "race": "Human",
        "gender": "Male",
        "nationality": "Haudenosaunee (Iroquois)",
        "organization": "Manitou Tribe",
        "connection": 4,
        "description": (
            "An old man full of contradictions: not a private man, though almost nothing is known of his "
            "history before he joined the Manitou in their fight for independence. Like a chess master, he "
            "thinks ahead multiple moves and sees all the potential outcomes; he is the first to step up in "
            "his people's defense and the last to back down from the correct course, and he knows that some "
            "day he must die, by his actions or of old age, and does not fear it, knowing there is another "
            "to take his place. He assures people his goal is to improve life for the tribe and will not say "
            "specifically how, which begins to annoy people badly as the days pass and nothing is resolved."
        ),
        "background": (
            "A powerfully trained Haudenosaunee shaman skilled in the arts of war, peace and diplomacy, and "
            "an outsider who has become the accepted medicine man of a manufactured tribe by sheer "
            "consensus; in council his advice carries weight second only to Chief Youngman's, and "
            "Thunderwalker reveres him as no other. He knows Mawnee Eaglefeather has cast him as her "
            "personal adversary and bears her no ill will at all, seeing her as misguided at times and as "
            "his own logical replacement -- an opinion she has no idea he holds. When Thunderwalker brought "
            "him the crashed module he immediately saw an opportunity: something valuable enough to trade "
            "for something the Manitou actually need."
        ),
        "notes": (
            "Stats p.57: B4 Q4 S4 C5 I6 W6 R5, Init 5+1D6, Astral Init 29+1D6, Astral 3, Astral Combat 8, "
            "Combat 8, Spell 7, Karma/Prof 9/3 (Essence garbled in the OCR); Aura Reading 5, Biotech 2 "
            "(First Aid 4, Natural Medicine 5), Conjuring 8, Enchanting 4, Etiquette 4 (Tribal 7), "
            "Leadership 6, Negotiation 5, Sorcery 7; AMC Politics 6, Flute 6, French 6, Haudenosaunee 4, "
            "Local Spirits 4, Manitou Area 5, Naskapi 4, Ojibwe 4, Psychology 6. Spells: Agony 6, Analyze "
            "Device 4, Analyze Truth 4, Astral Barrier 6, Control Fire 4, Cure Disease 5, Detox 6, "
            "Entertainment 4, Heal 5, Light 4, Magic Fingers 4, Oxygenate 3, Preserve 3, Resist Pain 4, "
            "Shapechange 4, Stabilize 5. Totem ELK: +1 die for health spells, +1 for spell defense, +2 for "
            "spirits of the land, -2 for combat spells. Initiate Grade 3: Invoking, Masking, Shielding. Colt "
            "American L36, spear 5M (stacked focus: power 3, spirit (forest) 2), knife, lined coat 4/2, "
            "expendable foci 4 (Heal) and 3 (Agony), sustaining focus 4 (Shapechange), shamanic lodge Rating "
            "7. He summoned a Spirit of the Land to bury the module deep in a Rating 6 warded crate with no "
            "witnesses, and will summon it again to dig the crate up if a deal is struck. Optional stubborn "
            "variant (p.53): he refuses to release it at all, citing a horrific vision of a great evil "
            "unleashed on the world."
        ),
        "contact_skills": ["Manitou spiritual authority and land spirits", "Natural medicine and Haudenosaunee shamanic tradition"],
    },
    {
        "name": "Mawnee Saukuk Eaglefeather",
        "role": "Powerful Eagle shaman and councillor who believes the medicine man's post was stolen from her, and who will use the module and the runners to take it back",
        "archetype": "Shaman",
        "title": "Tribal councillor of Niwimaja; Eagle shaman, Initiate Grade 2",
        "race": "Elf",
        "gender": "Female",
        "nationality": "Manitou Tribe",
        "organization": "Manitou Tribe",
        "connection": 4,
        "description": (
            "Her dark elven beauty is unsurpassed in the tribe and she uses it deliberately; many of the "
            "town's councillors and respected members owe their continued position to her silence. Far "
            "subtler than her totem implies, and neither undefended nor short of backers. She will pretend "
            "friendliness with the runners from the moment they arrive and adopt whatever position she "
            "thinks will lever outsiders to her aid, short of anything that would actually harm the tribe. "
            "There is a running current of jealousy between her and Dalianis Starseeker, and an open "
            "vendetta against Cloud Talon that the whole council can see."
        ),
        "background": (
            "She took her grandfather's name into her own when he died. As he had been the previous tribal "
            "medicine man, she assumed she would be the next choice, even though he named no successor; the "
            "council chose nobody, and then the outsider Cloud Talon became the accepted medicine man by "
            "consensus. Mawnee is not amused, and has cast the venerable Cloud Talon as her enemy -- a fact "
            "that has escaped neither the tribal council nor the man himself. To her the crashed module is a "
            "gift from Mother Earth and Father Sky, and she intends to use it to its greatest potential by "
            "turning as much of the tribe and council against Cloud Talon and anyone who sides with him as "
            "she possibly can."
        ),
        "notes": (
            "Stats pp.58-59: B3 Q6 S3 C8 I6 W6 E6 M8 R6, Init 6+1D6, Astral Init 28+1D6, Astral 2, Astral "
            "Combat 10, Combat 9, Spell 6, Karma/Prof 7/3; Aura Reading 5, Biotech 5 (Natural Medicine 7), "
            "Centering 6, Conjuring 6, Divination 5, Enchanting 4, Etiquette 7, Intimidation 5, Leadership "
            "5, Sorcery 6, Stealth 5; Algonkian 5, AMC Politics 4 (Manitou 6), Dreaming 5, Flora and Fauna "
            "6, Ojibwe 6, Singing 6, Sperethiel 4. Spells: Antidote 5, Astral Armor 4, Clairaudience 4, "
            "Clairvoyance 4, Compel Truth 5, Cure Disease 4, Detect Enemies 3, Detect Life 5, Diagnose 4, "
            "Dream 5, Heal 6, Influence 6, Mindprobe 5, Mist 4, Physical Camouflage 5, Physical Double Image "
            "4, Stunbolt 5, Thunderclap 5. Totem Eagle (+2 detection spells, +2 all spirits of the sky). "
            "Initiate Grade 2: Centering (Singing), Divining (Dreaming). Knife, real leather 0/2, expendable "
            "foci 4 (Compel Truth) and 3 (Mindprobe), wooden bracelet sustaining focus 4 (Physical Double "
            "Image), shamanic lodge Rating 7, and the ally spirit Gichi. Her rabble-rousing over the hidden "
            "module is what turns a quiet secret into a town-wide crisis, and Cloud Talon did not see it "
            "coming because he assumed her reason would outrun her jealousy. Despite the vendetta she would "
            "make a model medicine man, and she remains a staunch protector of the tribe. A possible romance."
        ),
        "contact_skills": ["Niwimaja council politics and factional leverage", "Divination and Eagle-totem shamanic practice"],
    },
    {
        "name": "Dalianis Starseeker",
        "role": "Naskapi Raven shaman and councillor who wants the module, the outsiders and all their gear gone from tribal land as fast as possible",
        "archetype": "Shaman",
        "title": "Tribal councillor of Niwimaja; Naskapi Raven shaman, Initiate Grade 1",
        "race": "Human",
        "gender": "Female",
        "age": 30,
        "nationality": "Naskapi (Manitou Tribe)",
        "organization": "Manitou Tribe",
        "connection": 3,
        "description": (
            "A young-looking human woman of thirty whose temperament and appearance both flourish in the "
            "cold and dry. Her hair is dark and long and her eyes are a deep, sparkling brown that seem to "
            "hold wisdom beyond her years; she dresses in traditional garb with a smattering of more modern "
            "and effective cold-weather gear. She has her totem's characteristic wit, cunning and charisma, "
            "and she treats outsiders exactly as respectfully as they behave toward her."
        ),
        "background": (
            "A member of the Naskapi faction of the Manitou, a talented shaman sorcerer and a follower of "
            "Raven who wanders the land around the town gathering what her tribe needs from Nature's bounty. "
            "She believes technology and industrial society are inherently flawed and oppressive and rejects "
            "them, but she is a pragmatist who knows some compromise must be made and chooses carefully "
            "where she bends so as not to topple her philosophical core. She knew nothing about the module "
            "until the runners arrived and does not know where it is."
        ),
        "notes": (
            "Stats p.59: B3 Q4 S3 C6 I6 W5 E6 M7 R5, Init 5+1D6, Astral Init 27+1D6, Astral 1, Astral Combat "
            "8, Combat 7, Spell 6, Karma/Prof 5/3; Aura Reading 6, Biotech 4 (Natural Medicine 5), Conjuring "
            "6, Edged Weapons 4, Enchanting 2, Etiquette 4, Leadership 4, Negotiation 3, Sorcery 5, Stealth "
            "5; AMC Politics 5, Botany 5, Dancing 4, Ecology 5, Haudenosaunee 3, Manitou Area 4, Naskapi 5, "
            "Permaculture 5. Spells: Alter Temperature 4, Animal Sight 3, Calm Animal 3, Diagnose 4, Fix 4, "
            "Gecko Crawl 5, Ignite 4, Influence 5, Transform 5, Wind 4. Totem Raven (+2 manipulation spells, "
            "+2 spirits of the sky, +1 to all target numbers when not under the open sky). Initiate Grade 1: "
            "Cleansing. Knife 3L, real leather 0/2. She has a great deal of local influence and resources "
            "and is helpful to whoever will make the outsiders and the module go away quickly; she is "
            "unlikely to ally with the runners, since their arrival and the module are the same problem to "
            "her, but she finds them more approachable than the Yamatetsu team and will say so. There is a "
            "current of jealousy between her and Mawnee that a clever team can work."
        ),
        "contact_skills": ["Naskapi faction opinion within the Manitou", "Local wilderness, botany and permaculture"],
    },
    {
        "name": "Jamis Bearpaw",
        "role": "Montagnais ork councillor and de facto leader of the radical anti-technology faction, who judges every visitor by how much chrome they carry",
        "archetype": "Tribal Leader",
        "title": "Tribal councillor of Niwimaja; leader of the radical anti-technology faction",
        "race": "Ork",
        "gender": "Male",
        "nationality": "Montagnais (Manitou Tribe)",
        "organization": "Manitou Tribe",
        "connection": 3,
        "description": (
            "A massive ork, more in girth than in height, thick with muscle yet still capable of great "
            "bursts of speed, wearing a vicious-looking bear's paw over his right hand -- won in the battle "
            "that earned him his name and the three red scars across his right cheek. He dresses in only "
            "what the Earth Mother grants him through his own arm or the arms of others in the tribe, "
            "carries a flint knife, and when necessary a powerful wooden bow he made with his own hands and "
            "arrows fletched from fallen branches. He takes an almost immediate adversarial role against "
            "anyone carrying cyberware or high-tech gadgetry: 'Do you use that gadget, or does that gadget "
            "use you?'"
        ),
        "background": (
            "One of the traditional Montagnais, the peaceful but fiercely anti-technology strand of the "
            "Manitou mix, and the man the radicals in Niwimaja look to. Rumors that he is a physical adept "
            "circulate around the tribe, but his aura shows nothing of the sort; in truth he is simply a "
            "skilled and powerful man, physically and psychologically."
        ),
        "notes": (
            "Stats p.59: B7 Q4 S7 C3 I5 W5 E6 R4, Init 4+1D6, Combat Pool 7, Karma/Prof 4/4; Biotech 5, "
            "Edged Weapons 5, Intimidation 4, Leadership 4, Pole Arms/Staffs 4, Projectile Weapons 4 (Pull "
            "Bow 7), Projectile Weapons B/R 4, Rifles 3, Stealth 6, Thrown Weapons 4, Unarmed 5; AMC "
            "Politics 3, Botany 3, Carpentry 4, Haudenosaunee 3, Hunting 4, Niwimaja Area 5, Ojibwe 3, "
            "Wildlife 3, Woodworking 4. Bow 9M with 20 arrows, flint knife 8L, staff 9M Stun, real leather "
            "0/2. He is unlikely to side with either the runners or Yamatetsu, but he may enjoy the company "
            "of particular individuals: adepts and magicians carrying little or no high-tech gear he will "
            "take a liking to and try to persuade to give up what technology they have left. He will "
            "certainly take no such liking to any invading corporate force, which can make him a valuable "
            "ally by default. Escalated, his faction may demand the runners destroy some of their gear "
            "before entering town or donate it to the recycling bin."
        ),
        "contact_skills": ["Manitou anti-technology faction", "Bush hunting and traditional weapon craft"],
    },
    {
        "name": "Shaun Ojibwan",
        "role": "Dwarf academic councillor who drafts Niwimaja's policy, expects an Aztechnology-backed AMC invasion, and sees the module as a chance at a global ally",
        "archetype": "Academic",
        "title": "Tribal councillor and policy drafter, Niwimaja",
        "race": "Dwarf",
        "gender": "Male",
        "nationality": "Manitou Tribe",
        "organization": "Manitou Tribe",
        "connection": 3,
        "description": (
            "He carries himself with a gentle kindness and has a firm voice devoid of harshness, and he "
            "tries to look each participant in a conversation in the eyes -- made difficult by his "
            "diminished dwarven stature. He is balding a bit, though his hair retains its youthful black "
            "color despite his advancing age; his movements are those of a tired man and his shoulders "
            "occasionally stoop as if under a great weight, some of which lifts as the current danger "
            "seems to pass. Behind the forgiving countenance his eyes are dark and fiery, filled with a deep "
            "resounding intelligence and restrained fury."
        ),
        "background": (
            "A student of political affairs throughout history, and usually the one who drafts policy for "
            "the Niwimaja Manitou; his opinion is respected and deferred to on anything touching outside "
            "relations. He is not particularly opposed to technological influence, seeing technology itself "
            "as a neutral tool; he is anti-capitalist and opposed to the oppressive role megacorps play in "
            "modern society and how they use technology to enforce it. He is convinced the AMC will soon "
            "invade Manitou land with Aztechnology backing unless the tribe can gather support at the world "
            "level -- so although he believes holding the module will only bring trouble, he sees it as an "
            "opportunity to foster a global ally."
        ),
        "notes": (
            "Stats p.60: B5 Q3 S3 C4 I5 W7 E6 R4, Init 4+1D6, Combat Pool 7, Karma/Prof 4/2; Instruction 5, "
            "Leadership 4, Negotiation 5, Rifles 3, Stealth 4, Unarmed 3; AMC Politics 6, Anarchist Theory "
            "3, Economics 4, English 5, Haudenosaunee 3, Marxist Theory 5, Ojibwe 5, Political History 6, "
            "Social Movements 4, Sociology 5. He is the councillor most likely to genuinely befriend the "
            "runners -- and, ironically, the councillor whose reasoning most naturally opens the door for "
            "Yamatetsu, since a megacorp that would back Manitou secession is exactly the global ally he is "
            "looking for. A team that wants to keep him has to give him a better answer to that question "
            "than the corp does. Also listed as a possible romance for a runner."
        ),
        "contact_skills": ["Manitou policy and outside relations", "AMC political history and corporate influence"],
    },
    {
        "name": "Gichi-baapi-animikiiwaanakwad",
        "role": "Mawnee Eaglefeather's ally spirit, a Force 4 spirit eagle out of the Realm of the Sky, called Gichi for short",
        "archetype": "Ally Spirit",
        "title": "Great Laughing Thundercloud -- ally spirit of Mawnee Saukuk Eaglefeather",
        "race": "Spirit",
        "gender": "Unknown",
        "connection": 2,
        "description": (
            "Great Laughing Thundercloud, Gichi for short. A large spirit eagle whose native plane is the "
            "Realm of the Sky, bound to the most ambitious shaman in Niwimaja and as much a part of her "
            "political standing as her beauty and her silence. Anyone who moves against Mawnee inside "
            "Niwimaja is moving against the ally as well, and it can see and speak for her at a distance."
        ),
        "notes": (
            "Stats p.60: Force 4; native plane the Realm of the Sky; Quickness 5; Immunity to Normal "
            "Weapons; Materialization; Sense Link; Sorcery 5; Thunderclap 5; form a large spirit eagle. Its "
            "Sense Link is the practical problem for runners doing anything quietly in town while Mawnee is "
            "in council, and its Sorcery makes it a genuine second caster in any confrontation. Note that "
            "Mawnee's totem gives +2 dice for all spirits of the sky, so anything she summons alongside Gichi "
            "comes easily; Dalianis shares that Raven bonus, which is part of why the two women's rivalry is "
            "dangerous rather than merely tiresome."
        ),
    },
    {
        "name": "Pierre O'Rourke",
        "role": "Yamatetsu's second recovery team leader -- an initiated Quebecois adept who will charm the Manitou in town and then lie in the bushes outside it",
        "archetype": "Physical Adept",
        "title": "Recovery team leader, Yamatetsu security and operations division",
        "race": "Elf",
        "gender": "Male",
        "nationality": "Quebecois",
        "organization": "Yamatetsu Corporation",
        "connection": 4,
        "description": (
            "A Quebecois elf who knows how to talk, and whose team follows his lead without question and "
            "watches each other's backs; any experienced runner can tell at a glance that this is a "
            "professional outfit and not the one the Manitou already killed. He commands in Japanese. He "
            "will play the good sport in Niwimaja whichever way the council falls -- and then wait outside "
            "the friendly confines with a slivergun and a jo stick, because failure is not an option for "
            "him. Depending on the runners' standing with the tribe he arrives either laying on all the "
            "charm or walking in weapons in hand demanding the return of corporate property."
        ),
        "background": (
            "He signed on with Yamatetsu six years ago and made a name for himself in their security and "
            "operations divisions. His orders come straight from his section commander, Nikoli Rostov: get "
            "the data module back intact, or at minimum copy the memory core and destroy the module so no "
            "one else can have it. He has been fully briefed on the political situation inside the AMC and "
            "carries enough authorization to draft a deal in the company name -- Yamatetsu will worry about "
            "keeping its end of any bargain later."
        ),
        "notes": (
            "Stats pp.51-52: B6 Q6 S5 C5 I5 W5 E6 M8, Reaction 5(9), Init 5(9)+1D6(3D6), Combat Pool 8, "
            "Karma/Prof 7/4; Athletics 6, Clubs 6, Etiquette 4 (Corporate 5, Street 6), Leadership 4, Small "
            "Unit Tactics 6, Negotiation 5, Pistols 6, Assault Rifles 6, Stealth 8, Throwing Weapons 5, "
            "Unarmed 6; Algonkian 4, AMC Politics 4, Bushido 4, Japanese 3, Psychology 5, Recon Operations "
            "4, Spirit Combat 4. Aikido 6 (Close Combat, Throw, Whirling). Initiate Grade 2: Centering "
            "(Meditation), Masking. Adept powers: Astral Perception, Enhanced Perceptions (Direction Sense, "
            "Low-Light, Thermographic), Improved Reflexes 2, Nerve Strike, Quick Draw. Nanosymbiotes. AK-97, "
            "Ares Viper Slivergun, concussion grenade, three throwing knives, jo stick (Weapon Focus 2), "
            "armored vest 4/3, encrypted transceiver, Nav-Dat GPS, satellite phone, survival kit. His team: "
            "four enforcers (three human, one dwarf), an electronics specialist with a CMT Avatar and "
            "satellite uplink under orders to transmit the module data the instant she has it, and an ork "
            "wagemage with Shielding, four elementals and a full spell list. In town he will cast doubt on "
            "the runners' honesty and credibility, may try to eliminate them or frame them for an offense "
            "against the tribe, and can offer the Manitou resources and intelligence on Aztechnology and "
            "the AMC government -- which some councillors will try to convert into corporate backing for "
            "the secession itself. His team will do nothing that risks damaging the module."
        ),
    },
    {
        "name": "Nikoli Rostov",
        "role": "Yamatetsu section commander who wrote O'Rourke's orders: bring the module back intact, or copy the core and destroy it",
        "archetype": "Corporate Security Officer",
        "title": "Section commander, Yamatetsu security and operations",
        "race": "Human",
        "gender": "Male",
        "organization": "Yamatetsu Corporation",
        "connection": 3,
        "description": (
            "The voice on the other end of O'Rourke's satellite phone. He is the man any major deal in the "
            "Manitou negotiation has to be cleared with, and the man whose standing authorization lets "
            "O'Rourke draft an agreement in Yamatetsu's name on the spot -- an authority Yamatetsu grants "
            "precisely because it does not intend to be bound by whatever gets promised to a tribe of "
            "secessionists."
        ),
        "notes": (
            "No stat block; named on p.52 as the source of O'Rourke's orders. He is the level at which the "
            "Gagarin recovery meets the rest of Yamatetsu -- above him sit Yoshi Hakeda and, through him, "
            "Saru Iwano and the standing instruction to retrieve the module at all costs and let nothing "
            "leak. A team that beats O'Rourke to the module has Rostov as their next problem: he is the man "
            "who decides whether Yamatetsu writes off two dead teams or comes after the runners, and the man "
            "the Manitou would have to deal with if they tried to convert the module into corporate backing "
            "for their independence."
        ),
        "contact_skills": ["Yamatetsu corporate security operations", "Recovery and extraction tasking"],
    },
    {
        "name": "Sherman Royce",
        "role": "AresSpace's caged star programmer, who wrote a sabotage virus into both Velox probes and hired the runners three times to buy himself out of the corporate world",
        "archetype": "Decker",
        "title": "Senior programmer, Velox I and II guidance systems, AresSpace",
        "race": "Human",
        "gender": "Male",
        "organization": "AresSpace",
        "connection": 3,
        "description": (
            "Thinning gray-brown hair, a shaking hand and a nervous habit of covering with hardcopy when "
            "the door opens -- 'I was just trying to figure out where a hitch in the code was, but I've "
            "gotten it now. Sometimes hardcopy is still useful.' A man three years past the end of his "
            "patience, holding a smile together in front of a Knight Errant lieutenant while thinking that "
            "the watchdog is starting to suspect and it is time to move anyway. Once he is out of the "
            "compound he grows elated and exuberant, like a slave set free. He is also, for all that, "
            "essentially a corp suit who does not trust his own hires and hires a second team to watch them."
        ),
        "background": (
            "When he was younger Royce did not want much out of life: a good job with a corp, a decent "
            "salary and days spent on computer games. He scored a job with AresSpace right out of school and "
            "shot through the ranks as a skilled programmer, and he was on the Velox program when the Probe "
            "Race began and security clamped down. As his reputation grew his freedom shrank -- constant "
            "surveillance, no leaving the grounds without permission and a retinue of bodyguard 'keepers', "
            "no social life left, even his Matrix activity monitored and curtailed -- and a rival corp's "
            "extraction of one of his comrades early in the race made it worse, as did the tightening after "
            "the Gigas mishap. Ares had no intention of accepting his resignation, so he built an escape: a "
            "remotely triggered virus called Liberty written into both probes' guidance systems, and a buyer "
            "for it at the Kepler project found through outside contacts and a referral name, Gabriel."
        ),
        "notes": (
            "Stats p.81: B2 Q4 S3 C3 I6(8) W3 E4.3, Reaction 5(6), Init 5(6)+1D6, Combat Pool 7, Karma/Prof "
            "2/3; Computer 7 (Programming 9), Computer B/R 5, Electronics 5, Electronics B/R 7, Etiquette 2 "
            "(Corporate 4, Matrix 7); Astrophysics 5, Astronomy 4, Databases 6, Math 6, Satellite Management "
            "7, Spacecraft 4, Telemetry Systems 5. Datajack, 300 Mp headware memory, Math SPU 3; cultured "
            "cerebral booster 2. He knows about his own extraction and will help: through Griebe he can "
            "arrange to be somewhere specific inside Building C at a specific time, probably supply a copy "
            "of his retinal prints, and warn when an employee is leaving the grounds with a passcard worth "
            "acquiring -- but he cannot get himself outside the building and does not want security noticing "
            "the traffic. Delay too long and suspicion falls on him: rescue from Knight Errant custody, from "
            "an Ares detainment facility, or off a transport to a treason trial. In New Orleans he admits he "
            "was the Johnson all along, pays 500 nuyen a day retainer, and auctions the second Liberty code "
            "on Asgard. Loyal runners who bring the money back get paid as agreed plus a 100,000 nuyen bonus "
            "and he vanishes free and clear. Legwork (Ares contact TN 5 or Matrix TN 6): top Ares "
            "programmer, primary code-meister on AresSpace's comet probes, locked away in a code farm down "
            "in Silicon Valley."
        ),
        "contact_skills": ["Probe guidance and telemetry programming", "AresSpace internal security and personnel handling"],
    },
    {
        "name": "Annika Griebe",
        "role": "One of Seattle's top fixers, who refuses on principle to arrange anything that benefits Ares and hires the team for all three of Royce's jobs",
        "archetype": "Fixer",
        "title": "Elite Seattle fixer; formerly an Ares Ms. Johnson",
        "race": "Human",
        "gender": "Female",
        "nationality": "German",
        "connection": 5,
        "description": (
            "Tall and blonde, wrapped in a Donce' Fabrini business suit with glasses framing electric blue "
            "eyes, and a ghost of a German accent. All business, with connections across the globe. She "
            "catches a contact's gaze across a packed club floor, nods once and walks into the back room "
            "without waiting to see if they follow. 'I don't wish to keep my client waiting.' She refuses "
            "questions about her client flatly and has the reputation to leave it at that; press her about "
            "the last job's surprises and she notes that if just anyone could do what she needs, she would "
            "have no need for shadowrunners."
        ),
        "background": (
            "She worked for Ares as a Ms. Johnson about five years ago until a run went bad and she took the "
            "fall; she and the corp had a falling out and she entered the shadows, building a reputation as "
            "one of Seattle's finest. She does not take jobs that benefit Ares, which everyone in the "
            "shadows knows and which some people insist is a ruse to cover her still being on Ares' payroll. "
            "She finds runners through fixers, through underworld contacts in each of the local crime "
            "syndicates and through the Seattle Shadowland data haven -- never through corporate contacts. "
            "She keeps a team of six runners on retainer, and banks under the alias Donna Klein."
        ),
        "notes": (
            "Stats p.81: Q6 S5 C6 I6 W6 E4.51 R6, Init 6+1D6, Combat Pool 9, Karma/Prof 8/4 (Body garbled in "
            "the OCR); Car 5, Computer 5, Electronics 5, Etiquette 6 (Corporate 8, Street 8), Leadership 5, "
            "Negotiation 7, Pistols 5; Ares Corporate History 8, Corporate Politics 8, Corporate Social "
            "Structure 8, Fixers 6, Shadowrunners 5, Smuggling Routes 4. Alphaware datajack and 500 Mp "
            "headware memory; Fichetti Security 500 with APDS, armored suit 3/0. Job one: 10,000 nuyen each, "
            "authorized to 20,000, Opposed Negotiations (6) at +1,000 per net success, no operating costs. "
            "Job two, by dropbox on Shadowland addressed to 'Runner X', password Griebe: 50,000 each plus up "
            "to 10,000 expenses, +5,000 per net success. She pays well, takes care of her people, and has an "
            "unshakable reputation of never turning on runners who work for her unless it is their fault. "
            "She does not go looking for new talent often, and turning her down means she never calls again. "
            "She would pay 1,000 nuyen a head just for the meeting. Legwork (any Street or Corporate, TN 4)."
        ),
        "contact_skills": ["Elite Seattle fixing -- corporate freelance placements", "Ares corporate history, politics and social structure"],
    },
    {
        "name": "Mercy",
        "role": "New Orleans talismonger, initiate of grade four and Griebe's opposite number in the Crescent City; hides Royce and stages the Etienne Yards exchange",
        "archetype": "Talismonger",
        "title": "Talismonger and fixer, Roger's Boutique, New Orleans",
        "race": "Elf",
        "gender": "Female",
        "connection": 4,
        "description": (
            "Tall even for an elf, well over two meters, with long black hair and red lips, in a light blue "
            "knit dress that sets off her tanned skin. She comes out from behind a blue velvet curtain in "
            "the middle of a stranger's thought about the antique masks on display: 'Some of these are over "
            "one hundred years old. My name is Mercy. How can I help you?' A low-key woman whose work is "
            "top notch, and a good deal more dangerous than the lace and the early-twentieth-century "
            "furniture suggest -- some of the krewes still hold a grudge over a lesson she taught them a "
            "few years back."
        ),
        "background": (
            "A talismonger with connections to Annika Griebe; her client base and her friendship have made "
            "her very useful as a fixer, and like the other fixers in this affair she has been paid to set "
            "the runners up with whatever they need. She deals in magical materials and can get her hands "
            "on weapon and power foci. She helps Royce put the Liberty activation code on the Asgard data "
            "haven, arranges the buyer's meeting, and picks the Etienne Yards for it precisely because it "
            "should be easy for the runners to escape from if anything goes wrong."
        ),
        "notes": (
            "Stats p.85: B4 Q6 S4 C7 I6 W6 E6 M10 R6, Init 6+1D6, Astral Init 30+1D6, Astral 4, Astral "
            "Combat 9, Combat 9, Spell 7, Karma/Prof 8/2 (the professional rating looks like a typo); "
            "Centering 6, Conjuring 5, Enchanting 4, Etiquette 6, Leadership 4, Pistols 5, Sorcery 7 "
            "(Spell Casting 9); Magical Groups 8, New Orleans Magic 6, Singing 6, Spell Design 6, "
            "Talismongering 5. Initiate Grade 4: Anchoring, Centering (Singing), Masking, Possessing. "
            "Spells: Alter Memory 5, Catalog 4, Confusion 6, Diagnose 4, Fashion 4, Fireball 8, Magic "
            "Fingers 8, Manaball 6, Physical Barrier 5, Poltergeist 5, Translate 4. A mask that is a Power "
            "focus 4. She evacuated the Yard's caretakers, workers and guard dogs for the night, equips the "
            "runners with a credstick verification reader, and is the one who calls the buyer with the "
            "location. Side hooks: the Mafia leaning on her for protection money, or a rare telesma she is "
            "trying to keep away from the zobop. Legwork (Street contacts or Fixers, TN 4): a low-key New "
            "Orleans fixer with a mask shop, top-notch work -- 'careful, though, she's a powerful sorceress'."
        ),
        "contact_skills": ["New Orleans black market and talismongery", "Weapon and power foci, magical materials"],
    },
    {
        "name": "Sketch",
        "role": "Loud, unreliable orbital fixer at Apollo's only bar who tells the runners where the relay is and sells them thirty minutes of distracted guards",
        "archetype": "Fixer",
        "title": "Orbital fixer and fence, Apollo station",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": (
            "A dark-haired, dark-eyed man of Southeast Asian descent with, unexpectedly, a British accent "
            "and a gregarious manner. He is usually floating at the Water Works bar with a drink in hand, "
            "talking boisterously at a bored-looking woman, and he greets arriving strangers by announcing "
            "them to the room: 'Ah, tourists in search of adventure. Everyone wants a bit of my wares, it "
            "seems. I'll be back soon, my dove... Shall we step into my office?' He enjoys exchanging war "
            "stories with newcomers or really anyone who will stand still long enough, but he is a "
            "professional through and through."
        ),
        "background": (
            "A low-grade fixer who sets things up in orbit and is currently working Apollo, a transient "
            "rather than an Ares station resident -- which is exactly why he cannot help with the airlock. "
            "The word on him among people with space contacts is that he is more trouble than he is worth: "
            "a big mouth who always says he can get the job done, except he hardly ever gets it done and he "
            "never gets it done on time."
        ),
        "notes": (
            "Stats p.68: B3 Q4 S3 C6 I4 W4 E6 R4, Init 4+1D6, Combat Pool 6, Karma/Prof 2/2; Athletics 4, "
            "Etiquette 5 (Corporate 7, Underworld 8), Negotiation 5 (Fast Talk 7), Pistols 5, Shotguns 4; "
            "Apollo Habitat Hideouts 4, Fencing 6, Orbital Black Market 6, Orbital Smuggling 7; armor vest "
            "2/1. He knows the relay is at the top of the station on the outside with no interior access, "
            "and points the team at the spacesuits and spacewalk gear in Airlock A. He will not go out with "
            "them -- he has nothing that beats the maglocks and only Ares station residents are cleared for "
            "access -- but he will pull the guards away from the guard station for 30 minutes for 4,000 "
            "nuyen up front. Treat him decently and forgive the pragmatism and he becomes a Level 1 contact "
            "after the run. Optional complication: the runners have to bail him out of a bind in the "
            "station's seedy underworld before he can help them, on a 48-hour clock. Legwork: any Space "
            "contact, TN 5."
        ),
        "contact_skills": ["Orbital black market and smuggling", "Apollo habitat hideouts and fencing"],
    },
    {
        "name": "Lt. Radford",
        "role": "Knight Errant lieutenant on Royce's watch detail -- polite, smiling, and standing right outside the door",
        "archetype": "Corporate Security Officer",
        "title": "Lieutenant, Knight Errant Security Services (AresSpace Silicon Valley)",
        "race": "Human",
        "gender": "Male",
        "organization": "Knight Errant Security Services",
        "connection": 2,
        "description": (
            "Tall, clean cut, and every inch a security officer: a strong jaw, a military haircut and a "
            "really impressive firearm -- one of the latest Predator variants, held loosely at his side in a "
            "posture somehow meant to seem non-threatening, as though the fact it is not holstered will go "
            "unnoticed. His shoulder logo says Knight Errant almost as loudly as the rest of him does. He "
            "wears the All-American Boy smile that probably landed him the assignment in the first place, "
            "and he is presumably supposed to be good with high-strung scientists. 'Everything all right, "
            "Dr. Royce? Major Layton was worried that you were unhappy with your food... You need anything, "
            "just wave to the surveillance camera or give us a call. We're just right outside.'"
        ),
        "notes": (
            "No individual stat block; use the Knight Errant Security Officer block, p.72 -- B4 Q4 S5 C3 I4, "
            "Reaction 4(7), Init 4(7)+1D6(2D6), Combat Pool 6 (4 in armor), Karma/Prof 2/3; Assault Rifle 5, "
            "Electronics 4, Etiquette 3 (Corporate 4), Heavy Weapons 3, Pistols 5, Unarmed 5; Muay Thai 5 "
            "(kick attack, sweep); Reaction Enhancers 1, Smartlink-2, Wired Reflexes 1 with reflex trigger; "
            "Ares Alpha with underbarrel grenade launcher, Ares Crusader, light security armor 7/6 with "
            "helmet, chemical seal, encrypted transceiver and ultrasound vision; plasteel restraints. Like "
            "the AresSpace employees, these guards are required to live on site and have extremely limited "
            "options for traveling off it -- a fact worth mentioning to any player who assumes the guards "
            "are freer than the scientists. Radford is the 'flavor of the day' on a rotating watch, which "
            "means Royce's minders change often enough that a well-briefed impostor is not impossible."
        ),
    },
    {
        "name": "Major Layton",
        "role": "The watchdog running Royce's surveillance detail, who is starting to suspect his prize scientist is up to something",
        "archetype": "Corporate Security Officer",
        "title": "Major commanding Dr. Royce's security detail, AresSpace Silicon Valley",
        "race": "Human",
        "gender": "Male",
        "organization": "Knight Errant Security Services",
        "connection": 3,
        "description": (
            "Never seen on stage, only felt: the man who sends a lieutenant in to ask whether the prisoner "
            "was unhappy with his lunch, and who is close enough to the mark that Royce decides on the spot "
            "it is time to move. 'Fragging Major Layton. I guess the watchdog is starting to suspect "
            "something. Lucky for me, it's time to move anyway. I'm way too fed up to hide it very well for "
            "much longer, and I suppose it's starting to show.'"
        ),
        "notes": (
            "No stat block; named once in the prologue. He is the clock on the whole adventure. The longer "
            "the runners take over the extraction the more suspicion falls on Royce, until Layton's people "
            "have him in Knight Errant custody, then in an Ares prison or detainment facility awaiting a "
            "treason trial, with the extraction correspondingly harder each step. He is also the natural "
            "author of any extra security the gamemaster wants to layer on: house-arrest-style radio "
            "beacons on the AresSpace scientists, hard to remove and carrying an anti-extraction charge "
            "(knockout gas, or a lethal injection to kill Royce rather than let him fall into the wrong "
            "hands), extra wards, bound spirits, paranormal guard animals, pressure plates or gas systems."
        ),
    },
    {
        "name": "Natalie Dark",
        "role": "Move-by-wire elven tactical specialist who leads Griebe's retained team, watching the runners in New Orleans with orders to recover ten million nuyen at any cost",
        "archetype": "Street Samurai",
        "title": "Tactical specialist and field leader, Annika Griebe's runner team",
        "race": "Elf",
        "gender": "Female",
        "organization": "Annika Griebe's Runner Team",
        "connection": 3,
        "description": (
            "An elven woman with black hair and completely black cybereyes, which she generally hides behind "
            "sunglasses; she dresses in gang-style clothing, preferring leather jackets and jeans, which "
            "makes her almost invisible in a Seattle club crowd and entirely wrong for a swamp. Essence 0.08 "
            "and Move-by-Wire 2 make her something closer to a weapon system than a person, and a tactical "
            "computer with four dedicated ports makes her the reason six runners on retainer fight as one "
            "unit."
        ),
        "background": (
            "Field leader of the six-person team Annika Griebe has kept on retainer for over a year: "
            "herself, the three brothers Nate, Crimson and Midnight, the bear shaman Aarvis and the rigger "
            "Eddie. They work together seamlessly, provide Griebe's security at meets, and take the standing "
            "assignments she does not farm out -- including, in New Orleans, the job of watching another "
            "team on a client's behalf."
        ),
        "notes": (
            "Stats pp.83-84: B6 Q8(10) S5 C6 W7 E0.08, Reaction 7(11), Init 7(11)+1D6(3D6), Combat Pool "
            "10(11), Karma/Prof 4/4 (Intelligence garbled in the OCR); Athletics 3(5), Computer 4, Edged "
            "Weapons 8, Electronics 6, Etiquette 4 (Street 7), Pistols 6, Small Unit Tactics 8, Stealth "
            "4(6), Unarmed 6; Gang ID 5, Megacorp Special Forces 6, Military History 4, Sioux 4, Sperethiel "
            "5. Capoeira 6 (disorient, ground fighting, kip-up). Alphaware cybereyes (flare compensation, "
            "low-light, thermographic), hearing amplification, Move-by-Wire 2, two smartlinks, sound "
            "dampener, tactical computer with 4 dedicated ports. Two Savalette Guardians, monofilament sword "
            "8M, secure jacket 5/4, microtransceiver 4, shotgun microphone 4, scanner 4. In the Yard her "
            "team observes from the swamp with spells, assensing, shotgun mics and image magnification; if "
            "the runners take the buyer's offer she attacks -- payment first, destroying the virus data and "
            "killing the traitors second. If the runners stay loyal and are losing, she may intervene, "
            "though the money still comes first. Orders are to back off and not fight if noticed."
        ),
    },
    {
        "name": "Aarvis \"Growler\"",
        "role": "Bear shaman on Griebe's team who avoids melee and does his work with spells, from Improved Invisibility to Powerball",
        "archetype": "Shaman",
        "title": "Bear shaman, Annika Griebe's runner team",
        "race": "Human",
        "gender": "Male",
        "organization": "Annika Griebe's Runner Team",
        "connection": 2,
        "description": (
            "A human male of slight build with wispy brown hair that is turning gray -- which is why his "
            "teammates call him Growler, and why he takes some care to avoid melee combat and use spells "
            "instead. His Bear totem gives him healing and forest spirits and, less conveniently for a "
            "surveillance job, a Willpower (4) Test to avoid going berserk for three Combat Turns when the "
            "shooting starts. He is the reason the team can watch a boat graveyard astrally and stay "
            "invisible doing it."
        ),
        "background": (
            "One of the six on Annika Griebe's standing retainer, working with her and the others for over a "
            "year. Masking at Initiate Grade 1 is what lets him sit in a swamp beside a meet without being "
            "spotted by the buyer's astral scout."
        ),
        "notes": (
            "Stats p.83: B3 Q4 S4 C6 I5 W5 E6 M7 R4, Init 4+1D6, Astral Init 26+1D6, Astral 1, Astral Combat "
            "8, Combat Pool 7, Spell 5, Karma/Prof 3/4; Aura Reading 4, Conjuring 6, Etiquette 2 (Magical "
            "5), Pistols 4, Sorcery 6 (Spell Casting 7); Magical Groups 4, Totem Identification 4. Totem "
            "Bear (+2 health spells and forest spirits; Willpower (4) Test to avoid going berserk for 3 "
            "Combat Turns). Spells: Animal Sight 4, Clairaudience 5, Control Emotions 5, Heal 6, Improved "
            "Invisibility 5, Increased Reflexes +2 4, Oxygenate 4, Powerball 5, Resist Pain 4. Initiate "
            "Grade 1: Masking. Power Focus 2, sustaining focus 4 (Increased Reflexes +2), microtransceiver "
            "4. Note the combination: Masking to hide the team astrally, Clairaudience and Animal Sight for "
            "the surveillance itself, and Powerball if the exchange turns."
        ),
    },
    {
        "name": "Nate",
        "role": "Ork elder brother on Griebe's team, the one who waits in the background for the tactical advantage while his brothers charge -- and takes the sniper's nest at the Yard",
        "archetype": "Street Samurai",
        "title": "Heavy weapons and close combat, Annika Griebe's runner team",
        "race": "Ork",
        "gender": "Male",
        "organization": "Annika Griebe's Runner Team",
        "connection": 2,
        "description": (
            "The older ork brother of the two human twins Crimson and Midnight. Where they prefer to race "
            "into battle as a way of proving their prowess, Nate waits in the background looking for the "
            "tactical advantage -- which is why, at the Etienne Shipyards, he is the one who sets himself up "
            "in a good sniper's position while the others watch the gates. Body 10 and Strength 8 with a "
            "combat axe and an Enfield AS-7, and no cyberware at all."
        ),
        "background": (
            "One of three brothers on Annika Griebe's retained team, and the only ork among them. Over a "
            "year working with Natalie Dark, Aarvis and Eddie has made the six of them seamless."
        ),
        "notes": (
            "Stats p.83: B10 Q5 S8 C4 I5 W6 E6 R5, Init 5+1D6, Combat Pool 8, Karma/Prof 5/3; Athletics 4, "
            "Leadership 4, Pistols 3, Pole Arms/Staffs 5, Shotgun 4, Stealth 5, Unarmed 6; Archaic Weapons "
            "4, Martial Arts Styles 4. Brawling 6. Enfield AS-7 with integral laser sight, combat axe (8S, "
            "+2 Reach), armored jacket 4/2, microtransceiver 4. He is the team member most likely to be "
            "spotted first by a careful runner team, because he has to take up a position and hold it -- and "
            "the one whose fire opens the Griebe team's attack if the runners sell Royce out."
        ),
    },
    {
        "name": "Crimson and Midnight",
        "role": "Nate's wired human twin brothers -- good in a fight, no tactical sense of their own, and dressed like the trideo taught them",
        "archetype": "Street Samurai",
        "title": "Assault pair, Annika Griebe's runner team",
        "race": "Human",
        "gender": "Male",
        "organization": "Annika Griebe's Runner Team",
        "connection": 2,
        "description": (
            "Nate's younger brothers and each other's twins. They dress and act as though they discovered "
            "shadowrunning on the trideo as kids and fell in love with the idea, and the result is two "
            "headstrong yet skilled runners -- good in combat, but with no tactical sense of their own, "
            "which is exactly what Natalie Dark's tactical computer is for. At Vertigo, a Perception (5) "
            "Test catches one of them watching the runners and a second Perception (5) finds his twin "
            "somewhere else in the crowd."
        ),
        "notes": (
            "One stat block for both, p.83: B7(10) Q5 S5 C4 I3 W6 E1, Reaction 4(8), Init 4(8)+1D6(3D6), "
            "Combat Pool 7, Karma/Prof 2/3; Athletics 3, Etiquette 2 (Street 4), Pistols 5, Stealth 4, "
            "Submachine Guns 5, Unarmed 4; Trideo Movies 4. Kung Fu 4 (full offense, vicious blow). Dermal "
            "Plating 3, Smartlink-2, Wired Reflexes 2. Ares Predator 3, Ingram Smartgun-10 with smartlink, "
            "lined coat 4/2, microtransceiver 4. Their third brother is the large chromed Amerind in dark "
            "sunglasses standing beside Griebe in the Vertigo back room -- that one is Nate. Griebe's whole "
            "team fights only in self-defense at a meet and leaves the premises immediately if trouble "
            "starts, since she and the club owner are friends and the staff will cover for her."
        ),
    },
    {
        "name": "Eddie",
        "role": "Griebe's veteran rigger, a decade in the shadows and longer with her than anyone can remember; runs the surveillance drones over the Yard",
        "archetype": "Rigger",
        "title": "Rigger, Annika Griebe's runner team",
        "race": "Human",
        "gender": "Male",
        "organization": "Annika Griebe's Runner Team",
        "connection": 2,
        "description": (
            "An old-timer, meaning he has been shadowrunning on and off for over a decade, and he has worked "
            "for Ms. Griebe longer than anyone on the team can remember. A scar runs from the side of his "
            "left eye down to his jaw, something he refers to as a 'T-bird Love Bite' and will happily "
            "explain at length to anyone who asks. A Vehicle Control Rig 3 and a Reaction of 11 rigged mean "
            "that whatever the team is watching, he is watching it from further away and faster."
        ),
        "background": (
            "The longest-serving member of Annika Griebe's retained team. His knowledge skills say what kind "
            "of rigger he is: Matrix Topography, Decker Tricks, Drones, Security Procedures and Security "
            "Rigger Systems -- a man who thinks about the other side's rigger before he thinks about his own "
            "drones."
        ),
        "notes": (
            "Stats p.83: B4 Q4 S3 C3 I5 W7 E0.5, Reaction 5(11), Init 5+1D6, Rigging Init 11+4D6, Combat "
            "Pool 8, Control Pool 11, Karma/Prof 6/3; Car 5, Car B/R 6, Computer 4, Electronics B/R 5, "
            "Gunnery 5, Hovercraft 4, Motorcycle 3, Motorcycle B/R 4, Pistol 3, Unarmed 4, Vectored Thrust "
            "Aircraft 6; Matrix Topography 3, Decker Tricks 3, Drones 5, Security Procedures 4, Security "
            "Rigger Systems 4. Brawling 4. Datajack, vehicle control rig 3. Browning Max-Power with laser "
            "sight, armored jacket 5/3, Remote Control Deck 4, microtransceiver 4, and two surveillance "
            "drones of the gamemaster's choice. Those two drones are how Griebe's team keeps the runners in "
            "sight across three days of New Orleans without ever being caught at it."
        ),
    },
    {
        "name": "Lt. Robert Berkeley",
        "role": "Ares Firewatch team commander, on the runners' trail from the hour Velox I went off course",
        "archetype": "Corporate Special Forces",
        "title": "Lieutenant, Ares Firewatch unit commander",
        "race": "Human",
        "gender": "Male",
        "age": 28,
        "organization": "Ares Firewatch",
        "connection": 4,
        "description": (
            "A sandy-haired twenty-eight-year-old human male with gray cybereyes, and a man who has served "
            "as a Firewatch unit commander for much of a career that started very young. Quickness and "
            "Strength 9 on betaware muscle replacement, Reaction 11 on Wired Reflexes 2, and orthoskin under "
            "an armor vest with plates; he negotiates at 5 and leads at 5 with a Tactics specialization at "
            "7, which means he can be the man making the pitch at the Yard as easily as the man kicking the "
            "door."
        ),
        "background": (
            "His team has been working together for over a year. They were put on the runners' trail "
            "immediately following the Velox I incident and were on the scene in Silicon Valley shortly "
            "after the Royce extraction, which is why Ares is anywhere near New Orleans at all."
        ),
        "notes": (
            "Stats p.80: B6 Q7(9) S7(9) C5 I5 W6 E2.4, Reaction 6(11), Init 6(11)+1D6(3D6), Combat Pool "
            "9(10), Karma/Prof 8/4; Assault Rifles 7(8), Biotech 4(5), Electronics 3(4), Etiquette 5 "
            "(Corporate 6), Leadership 5 (Tactics 7), Negotiation 5, Pistols 6(7), Small Unit Tactics 6, "
            "Unarmed 5(6); Ares Corporate Structure 4, Megacorp Security 5, Security Procedures 5. Wildcat "
            "5(6) (multi-strike, vicious blow). Betaware cybereyes (flare compensation, low-light, optical "
            "magnification 3), Muscle Replacement 2, Smartlink 2 with rangefinder, Wired Reflexes 2 with "
            "reflex trigger; cultured enhanced articulation and orthoskin 2. AK-98 with integral underbarrel "
            "grenade launcher and offensive grenades, Ares Predator 3, armor vest with plates plus orthoskin "
            "5/4. With him: a Firewatch mage (Shielding, four Force 5 elementals), a rigger with an Ares "
            "Guardian and a Cyberspace Designs Wolfhound, and three Wildcat-trained soldiers. If Ares wins "
            "the auction he is the negotiator who offers to double the runners' pay and grant them "
            "protection for one address; if it loses, he is the team that crashes the exchange."
        ),
    },
    {
        "name": "Commander Colin Walton",
        "role": "Troll commander of Shibata's Major Assets Recovery Team, who earned a leadership position inside a Japanese corporation on sheer competence",
        "archetype": "Corporate Special Forces",
        "title": "Commander, Shibata Major Assets Recovery Team (SMART)",
        "race": "Troll",
        "gender": "Male",
        "organization": "Shibata",
        "connection": 4,
        "description": (
            "A grizzled corp veteran with years of black ops experience, and a troll who has earned a "
            "leadership position inside a Japanese corporation purely on skill -- which tells a runner "
            "something about both the man and the reputation he must have built to get there. Strength 11 "
            "and Body 10 on muscle replacement, Wired Reflexes 2, a Remington Roomsweeper loaded half "
            "flechette and half APDS, and a combat axe that does 11S."
        ),
        "background": (
            "Shibata's recovery specialist for exactly this kind of problem: an asset in the wrong hands and "
            "a very short window. He leads SMART into New Orleans either as the winning bidder collecting "
            "the Liberty activation code, or as the losing bidder determined that nobody else will have it "
            "and that Dr. Royce will be attending a personal meeting whether he likes it or not."
        ),
        "notes": (
            "Stats pp.79-80: B9(10) Q5(6) S10(11) C4 I5 W4 E1.5, Reaction 5(9), Init 5(9)+1D6(3D6), Combat "
            "Pool 7, Karma/Prof 4/4; Athletics 5, Intimidation 3, Leadership 4, Negotiations 5, Pistols 5, "
            "Pole Arms/Staffs 6, Unarmed 4; Corporate Politics 5, Security Procedures 6, Smugglers 4. Arnis "
            "De Mano (kick attack, throw). Muscle Replacement 1, smartlink, Wired Reflexes 2. Remington "
            "Roomsweeper (smartlinked, 8 rounds flechette and 8 APDS), combat axe 11S, secure vest 3/2. His "
            "team: a SMART mage with Confusion, Firewall, Manaball and a water and an earth elemental on "
            "call, and four members with Enfield AS-7s, Demolitions 3, Electronics 5 and a dose of jazz "
            "each. Note the Negotiations 5 -- if Shibata wins the auction he makes the buyout pitch himself, "
            "and a troll offering a runner team protection from Ares is a genuinely tempting scene."
        ),
    },
    {
        "name": "Paul Thomas",
        "role": "AresSpace spokesman who has to explain on the record why the corporation's flagship probe is no longer going anywhere near Halley's Comet",
        "archetype": "Corporate Media Officer",
        "title": "Spokesman, AresSpace (Detroit)",
        "race": "Human",
        "gender": "Male",
        "organization": "AresSpace",
        "connection": 2,
        "description": (
            "The name at the bottom of the news item the runners read a day after they come down from "
            "Apollo, and the man given the job of making sabotage sound like maintenance: 'Velox I has "
            "irretrievably deviated from its trajectory due to a telemetry problem. It will be unable to "
            "reach Halley's Comet.' A telemetry problem is, technically, exactly what it was."
        ),
        "notes": (
            "Player handout p.83, datelined Detroit (NN), 02-10-62. The rest of the release is the runners' "
            "situation report: Velox I is the first of two near-identical AresSpace probes and Velox II "
            "remains on target, projected to intercept Halley in approximately one month, ahead of the other "
            "contenders; the Ares probe Gigas succumbed to damage sustained striking an asteroid in deep "
            "space; the Kepler probe, a joint project between Aztechnology, Shibata and Federated Boeing, is "
            "the only other probe left with a chance to beat Velox II, and members of the Kepler team could "
            "not be reached for comment. The Probe Race has been highly publicized, with nearly every major "
            "competitor suffering accidents, mishaps and failures -- often claimed as sabotage by rival "
            "corporations. Deliver this handout only AFTER Griebe's second job offer."
        ),
        "contact_skills": ["AresSpace public relations and press lines"],
    },
]

ORG_UPDATES = {
    "Proteus AG": {
        "notes_append": (
            "Wake of the Comet (2062), The Messenger: Proteus is a significant player in the Halley Probe "
            "Race, relying more on the abilities of a few scientific geniuses than on the huge staffs the "
            "other space-oriented corps use. Its probe is GOTTERBOTE (German for 'God-messenger'), boosted "
            "from the Iles du Salut arkoblock to the Treffpunkt Raumhaufen orbital platform and there mated "
            "to a deep-space rocket. Corporate legwork TN 4: 0 'they're not a triple-A megacorporation, so I "
            "can't be bothered to keep tabs on them'; 1-2 a German AA specializing in heavy industry "
            "including a lot of aquatechnology; 3 extraterritorial for about ten years and drawing a lot of "
            "attention from the Big Ten; 4 expanding into aerospace, having just completed a big new "
            "arcology in South America dedicated solely to orbital launches, not a threat to Ares and "
            "Novatech yet but watched very closely; 5 that new arcology is in French Guiana. DISCREPANCY: "
            "Corporate Punishment's list of nine completed arkoblocks (five North Sea, two off Japan, one "
            "near Fiji, one off South America, one off Salish-Shidhe) does not obviously include this one, "
            "and this book calls the Guianan facility both an arkoblock and an arcology; treat the Iles du "
            "Salut complex as the South American entry, since only a small portion of it is actually "
            "underwater. Security blocks: guards B5 Q4 S4 C3 I3 W4 E6 R3, Init 3+1D6, Combat Pool 5, "
            "Karma/Prof 1/3, Athletics 3, Interrogation 3, Intimidation 3, Pistols 4, SMG 5, Unarmed 4, "
            "HK227 and Walther PB-120, Secure Jacket 5/3 (flechette loads underwater; light security armor "
            "7/6 and Combat Pool 3 on a formal alarm). Security mages B3 Q3 S3 C4 I5 W5 E6 M6 R4, Astral "
            "Init 25+1D6, Analyze Truth 4, Mind Probe 4, Spiritbolt 4, Stunball 4, Stunbolt 5, Treat 4, "
            "three Force 4 elementals each. Security riggers B4 Q4 S4 C1 I5 W5 E3 R4(8), Gunnery 4, "
            "Submarines 4, vehicle control rig 2. Rescue squad: an Ares Mobmaster (up to 15 troops plus "
            "rigger and mage), ten troopers with Boosted Reflexes 1, smartlinks, Colt M22A2s with "
            "underbarrel flash grenades, Neuro-Stun VII and light security armor 7/6 with chemical seal and "
            "respirator. Captured intruders are executed or pressed into Proteus' own shadow ops division "
            "-- 'cortex bombs are wonderful recruitment tools'. Proteus is also floated as a possible "
            "employer for the Gagarin module recovery in Catch a Falling Star."
        ),
        "leadership_add": [
            {"name": "Emil Verdan", "title": "Gotterbote project manager, Iles du Salut arkoblock", "notes": "Ruled Hausmann's payload onto the probe over Hoff's objection."},
            {"name": "Heinrich Hausmann", "title": "Project lead, Gotterbote payload package", "notes": "Winternight sleeper; means to put a nuclear bomb on the comet."},
            {"name": "Gunther Hoff", "title": "Telemetry specialist, Gotterbote payload team", "notes": "Hired the runners to abduct Hausmann; murdered by Winternight."},
        ],
        "enemies_add": ["Winternight"],
    },
    "AresSpace": {
        "notes_append": (
            "Wake of the Comet (2062), The Price of Liberty: AresSpace runs the twin VELOX I and VELOX II "
            "comet probes and lost a third, GIGAS, to an asteroid strike in deep space. Its Silicon Valley "
            "office park -- four city blocks, six buildings, three sublevels each, a Barrier 16 wall with "
            "watchtowers and tank traps, tunnels between buildings and an operations center linked directly "
            "to AresSpace Command in Houston -- keeps its prize scientists under twenty-four-hour Knight "
            "Errant surveillance and rarely lets them leave the grounds. Dr. Sherman Royce, one of its top "
            "programmers and its primary code-meister on the comet probes, wrote a remotely triggered "
            "sabotage virus called Liberty into both Velox guidance systems, sold the first activation to "
            "the Kepler consortium and auctioned the second on the Asgard data haven after extracting "
            "himself. The extraction pressure was self-inflicted: security tightened drastically after a "
            "rival corp extracted one of Royce's colleagues early in the Probe Race, and again after Gigas. "
            "Public line on Velox I (spokesman Paul Thomas, 02-10-62): 'irretrievably deviated from its "
            "trajectory due to a telemetry problem'. If Ares recovers the second Liberty code it disables "
            "the virus remotely and Velox II wins the Probe Race; if Shibata gets it, Velox II dies and "
            "Kepler wins."
        ),
        "leadership_add": [
            {"name": "Sherman Royce", "title": "Senior programmer, Velox I and II guidance systems", "notes": "Wrote the Liberty virus; extracted himself to New Orleans."},
            {"name": "Paul Thomas", "title": "AresSpace spokesman (Detroit)", "notes": "Announced Velox I's loss as a telemetry problem."},
        ],
        "enemies_add": ["Kepler Project", "Shibata"],
    },
    "Ares Macrotechnology": {
        "notes_append": (
            "Wake of the Comet (2062): Ares runs the massive Cape Canaveral launch facility, which services "
            "not only its own traffic but lesser corps, governments and even low-security launches by other "
            "megas such as MCT and Shiawase; three independent checkpoints, a combat mage at each and three "
            "Force 5 bound air elementals on the pad. It also owns and operates the Apollo Low Earth Orbit "
            "Space Station, renting pod space to corps that cannot build their own -- a commercial hub, an "
            "R&R stop, and a station with a background count of 9. Its FIREWATCH teams were put on the "
            "runners' trail the hour Velox I went off course. In Catch a Falling Star, Damien Knight is one "
            "of the four suggested employers for the Gagarin module job: he wants the data and if possible "
            "the module, even in pieces, as much as he wants Yamatetsu to lose, and if the runners cannot "
            "get it exclusively for Ares their orders are to destroy it -- Ares also has the best data on "
            "the crash site and good contacts in Thunder Bay, plus Algonkian and Iroquois linguasofts. "
            "Around Silicon Valley, Ares troops openly guard the enclave perimeter against General Saito's "
            "Californian Protectorate, run their own checkpoints, are particularly suspicious of people of "
            "Asian descent, and will not pursue fugitives into Saito's territory but will use heavy ordnance "
            "to stop them leaving."
        ),
        "allies_add": ["Ares Firewatch"],
        "enemies_add": ["Californian Protectorate", "Shibata"],
    },
    "Yamatetsu Corporation": {
        "notes_append": (
            "Wake of the Comet (2062), Catch a Falling Star: Yamatetsu's GAGARIN was the only probe to reach "
            "Halley's Comet in the first leg of the Probe Race, and lost contact right after its sensors "
            "began gathering data -- a public humiliation. In early 2062, after perihelion, Gagarin "
            "burst-transmitted home: intact but crippled, guidance operational, communications "
            "half-functional, the sensor memory module offline and unreadable, and the probe slightly off "
            "course with the module still programmed to drop on the Earth flyby. CEO Saru Iwano ordered "
            "total secrecy, twenty-four-seven work and a list within the hour of everyone in the facility "
            "who knew; the resulting traffic is exactly what tipped the rival corps off. Yamatetsu owns "
            "Alaxa, a small Everett biotech front, and shares zero-g data with it from the Shibanokuji "
            "orbital station over a dedicated once-an-hour, one-minute satellite burst -- on the same PLTG "
            "as all its classified space projects. Two recovery teams went into Manitou land: the first "
            "(six people) was wiped out to the last man by Thunderwalker's militia after its leader made the "
            "wrong move; the second, under Pierre O'Rourke and answering to section commander Nikoli Rostov, "
            "is authorized to draft deals in the company name that Yamatetsu has no intention of honoring. "
            "If Yamatetsu does recover the data it finds its own worst nightmare -- the readings show "
            "another craft already at the comet -- and quietly buries the whole thing rather than admit it "
            "lost. Legwork: Gagarin (Yamatetsu or space-fan contacts TN 3, other Corporate or Matrix TN 4) "
            "and Shibanokuji (same) tables in the prep doc."
        ),
        "leadership_add": [
            {"name": "Yoshi Hakeda", "title": "Executive responsible for the Gagarin project", "notes": "Reports directly to Saru Iwano; his career rides on the module."},
            {"name": "Ivan Kolenko", "title": "Project manager, Gagarin probe", "notes": None},
            {"name": "Nikoli Rostov", "title": "Section commander, security and operations", "notes": "Issued O'Rourke's recovery orders."},
            {"name": "Pierre O'Rourke", "title": "Recovery team leader, security and operations", "notes": "Quebecois elf adept; leads the second Manitou recovery team."},
        ],
        "allies_add": ["Alaxa"],
    },
    "Saeder-Krupp Heavy Industries": {
        "notes_append": (
            "Wake of the Comet (2062): Saeder-Krupp owns the former European Space Agency base at Kourou, "
            "French Guiana, and its local headquarters dominates the town center -- the few blocks around "
            "the S-K building are the only clean and prosperous part of Kourou, providing housing, shopping "
            "and entertainment for corporate employees. When S-K took over the base it built its own health "
            "club for its people, which is what killed the Sporting and Aero Club. Its local security teams "
            "are far more experienced with shadowrunners than the Kourou police, who have a good working "
            "relationship with them and call them in 1D6 minutes behind the first patrol cars; use the "
            "Proteus counterstrike stats for an S-K squad. Along with Ares, Novatech and Yamatetsu, "
            "Saeder-Krupp wants the Gotterbote launch to fail even without knowing about the nuke aboard. "
            "In Catch a Falling Star, Lofwyr is one of the four suggested employers for the Gagarin module "
            "job: he is curious what the probe collected but does not want it in anyone else's hands, "
            "especially Yamatetsu's, so the runners are to download the data, leave no traces, wipe the "
            "module clean and leave it behind. S-K has little influence inside the AMC but can supply "
            "Algonkian linguasofts, a GPS unit, survival gear and a vehicle rigger."
        ),
        "allies_add": ["French Guiana", "Kourou Police"],
    },
    "Aztechnology": {
        "notes_append": (
            "Wake of the Comet (2062): Aztechnology is one third of the Aztechnology / Shibata / Federated "
            "Boeing consortium behind the KEPLER probe, the dark horse of the Probe Race and the only rival "
            "left to Ares' Velox II. It also holds significant clout inside the Algonkian-Manitou Council -- "
            "some think it is the power behind the throne -- and Shaun Ojibwan of Niwimaja is convinced the "
            "AMC will soon invade Manitou land with Azzie backing. That clout stops dead at the Manitou "
            "border, where interference by Aztechnology is seriously disliked; runners revealed to be "
            "working for the Azzies in Niwimaja have a serious problem. As a Gagarin employer, Aztechnology "
            "simply wants the module and the data destroyed and does not much care how, and can supply "
            "survival gear, valid AMC identity documents, extra transportation in La Ronge, a decent map of "
            "the Manitou area and an approximate crash location. Aztechnology forces are also listed as one "
            "of the possible hostile border encounters on the Churchill River."
        ),
        "allies_add": ["Shibata", "Kepler Project", "Federated Boeing", "Algonkian-Manitou Council"],
        "enemies_add": ["Manitou Tribe"],
    },
    "Shiawase Corporation": {
        "notes_append": (
            "Wake of the Comet (2062): Shiawase is one of the megacorps that runs low-security launches out "
            "of Ares' Cape Canaveral facility. It is also one of the four suggested employers for the "
            "Gagarin module recovery in Catch a Falling Star: Shiawase wants the module and the data "
            "destroyed and would prefer the damage to look like it came from the crash, and can supply the "
            "runners with a magnetic anomaly detector, a chip storage unit with a datalock and medical "
            "supplies. Like the other Probe Race also-rans it has a standing interest in seeing Yamatetsu "
            "denied any claim on having reached Halley's Comet first."
        ),
    },
    "Novatech, Inc.": {
        "notes_append": (
            "Wake of the Comet (2062): Novatech is building a massive aerospace complex outside Cayenne, "
            "French Guiana -- one of only two significant modern facilities in the capital, alongside the "
            "international airport, and part of what makes the equatorial protectorate worth having despite "
            "its minimal resources. Along with Saeder-Krupp, Ares and Yamatetsu, Novatech wants Proteus' "
            "Gotterbote launch to fail even without knowing about the nuclear payload aboard, and might send "
            "a shadow team up to Proteus' Treffpunkt Raumhaufen platform to arrange it. Novatech is also "
            "listed as an alternative employer for the Gagarin module job."
        ),
    },
    "Federated Boeing": {
        "notes_append": (
            "Wake of the Comet (2062): Federated Boeing is one third of the Aztechnology / Shibata / "
            "Federated Boeing consortium behind the Kepler probe, the last serious rival to Ares' Velox II "
            "in the Probe Race. It also flies out of Ares' Cape Canaveral facility with its own corporate "
            "representative at the second and third checkpoints, and its security squad uniform is the cover "
            "Annika Griebe buys for the Apollo run -- Federated Boeing jumpsuits, clearance visas and "
            "Security ID badges that hold up to scrutiny and permit flechette, narcoject and taser weapons "
            "at the station though not aboard the shuttle. Its shuttle safety briefing carries the standard "
            "disclaimer that the use of magic or attempted contact with the astral plane outside Earth's "
            "atmosphere has been linked to severe psychological trauma and death, and that neither Ares nor "
            "Federated Boeing is responsible for the consequences."
        ),
        "allies_add": ["Aztechnology", "Shibata", "Kepler Project"],
    },
    "Knight Errant Security Services": {
        "notes_append": (
            "Wake of the Comet (2062), The Price of Liberty: Knight Errant holds the security contract at "
            "the AresSpace Silicon Valley office park, where its officers guard the corp's prize scientists "
            "around the clock under Major Layton, keep a 24-hour security rigger and a night-shift shaman "
            "on staff, and are themselves required to live on site with extremely limited options for "
            "traveling off it. Officer block p.72: B4 Q4 S5 C3 I4, Reaction 4(7), Init 4(7)+1D6(2D6), Combat "
            "Pool 6 (4 in armor), Karma/Prof 2/3; Assault Rifle 5, Electronics 4, Heavy Weapons 3, Pistols "
            "5, Unarmed 5, Muay Thai 5; Reaction Enhancers 1, Smartlink-2, Wired Reflexes 1 with reflex "
            "trigger; Ares Alpha with underbarrel grenade launcher, Ares Crusader, light security armor 7/6 "
            "with helmet, chemical seal, Rating 4 encrypted transceiver and ultrasound vision. The night "
            "shaman (headed 'Eagle Shaman' on p.72 but with an OWL totem in the same block -- a book error) "
            "summons a Force 5 city spirit at sunup and sundown and a Force 3 watcher at night; the troll "
            "security rigger runs an Ares Sentinel on the gate wall and an Ares Guardian inside the grounds. "
            "The Kourou police could plausibly contract their security out to Knight Errant as an optional "
            "difficulty increase in The Messenger."
        ),
        "leadership_add": [
            {"name": "Major Layton", "title": "Commanding Dr. Royce's security detail, AresSpace Silicon Valley", "notes": "Suspects his scientist is up to something; the clock on the extraction."},
            {"name": "Lt. Radford", "title": "Lieutenant, Royce's watch detail", "notes": None},
        ],
        "allies_add": ["AresSpace", "Ares Firewatch"],
    },
    "Lone Star Security": {
        "notes_append": (
            "Wake of the Comet (2062), Catch a Falling Star: Alaxa, the Everett biotech firm quietly owned "
            "by Yamatetsu, does not use Yamatetsu guards -- to keep the ownership hidden it hires OFF-DUTY "
            "LONE STAR COPS who need extra income. They are generally tired from overworking and not as "
            "alert as they should be, respond to trouble with cop bravado, try to immobilize intruders with "
            "splatguns and tasers, and get on the phone to Lone Star for backup the moment they realize they "
            "are dealing with shadowrunners; blocks in the Alaxa row. If they get that call out, Lone Star "
            "may respond to its own officers with maximum speed and force. Lone Star also polices Vertigo, "
            "the downtown changeling club where Annika Griebe holds her meets, rounding up everyone involved "
            "in any trouble and escorting the lot of them to the station."
        ),
    },
    "Mitsuhama Computer Technologies": {
        "notes_append": (
            "Wake of the Comet (2062): MCT is named as one of the megacorps running low-security launches "
            "out of Ares' Cape Canaveral facility, alongside Shiawase -- a reminder that even the Big Ten "
            "rent pad time from each other for routine orbital traffic rather than duplicating equatorial "
            "launch infrastructure."
        ),
    },
    "Humanis Policlub": {
        "notes_append": (
            "Wake of the Comet (2062): Vertigo, the downtown Seattle club where Annika Griebe recruits, is "
            "largely a changeling club with all the racial issues that come with that; a Humanis sit-in "
            "outside the doors is one of the suggested complications for the runners on their way in or out."
        ),
    },
}

LOC_UPDATES = {}

NPC_UPDATES = {
    "Saru Iwano": {
        "notes_append": (
            "Wake of the Comet (2062), Catch a Falling Star prologue: when Gagarin unexpectedly "
            "burst-transmits home, Yoshi Hakeda phones Iwano's private number voice-only and it is answered "
            "before the first ring finishes. Iwano hears the concern in his voice before he speaks: 'I am "
            "glad to hear it. Now give me the bad news.' Then: 'Yoshi, I find none of this news to be good. "
            "In fact, I find it entirely sickening. We cannot claim a victory until we have concrete sensor "
            "information in our hands. In fact, we cannot even let word of Gagarin's return leak out, "
            "because if we cannot retrieve the module or it holds no data, we look like even bigger fools. "
            "If that is the case, I would have preferred Gagarin to have been lost forever. Your team is now "
            "working on this twenty-four seven. Get Gagarin back on-line and determine if it collected "
            "anything -- if it did, retrieve it at all costs. Our enemies will seek to keep that data out of "
            "our grasp by any means they can. Nothing about this leaves your circle and you update me "
            "immediately on anything.' He then demands a thorough list within the hour of everyone in the "
            "facility who knows, and that it be made clear there will be consequences for failure. His voice "
            "is described as deep and dark. That order -- total secrecy, at all costs, with a named list of "
            "everyone who knows -- is what puts two Yamatetsu recovery teams into the field and gets the "
            "first one killed."
        ),
        "background_append": (
            "Wake of the Comet: as of 2062 Iwano is Yamatetsu's CEO and personally directs the Gagarin "
            "recovery, holding the corp's public humiliation over the head of the executive responsible."
        ),
    },
    "Lofwyr": {
        "notes_append": (
            "Wake of the Comet (2062), Catch a Falling Star: Lofwyr is one of the four suggested principals "
            "behind the Mr. Johnson who hires the runners for the Gagarin module. His brief is "
            "characteristically its own third position: he is curious to see what data the probe collected "
            "but does not want it to fall into anyone else's hands, Yamatetsu's least of all, so the runners "
            "are instructed to download the data, leave no traces, and wipe the module clean and leave it "
            "behind rather than take or destroy it. Saeder-Krupp has little influence inside the "
            "Algonkian-Manitou Council and can offer only Algonkian linguasofts, a GPS unit, survival gear "
            "and a vehicle rigger on retainer -- so a team working for the dragon goes into Manitou land "
            "with less cover than one working for Ares or Aztechnology."
        ),
    },
    "Damien Knight": {
        "notes_append": (
            "Wake of the Comet (2062), Catch a Falling Star: Damien Knight is one of the four suggested "
            "principals behind the Gagarin module job, and the book states his motive plainly -- he is as "
            "interested in getting his hands on the data, and if possible the module itself even in pieces "
            "of wreckage, as he is in seeing Yamatetsu lose. If the runners cannot obtain the data "
            "exclusively for Ares, their orders are to destroy it. Ares can back that with the best data on "
            "the crash site, good contacts in Thunder Bay, and Algonkian and Iroquois linguasofts, survival "
            "gear, weapons and accessories. In The Price of Liberty his corporation is on the other side of "
            "the board entirely, losing Velox I to a bought programmer's virus and Gigas to an asteroid."
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
Wake of the Comet gives security codes and trigger-step sheafs rather than mapped node lists, so these
are recorded as sheafs. Node contents are described in prose where the book gives them.

**1. Proteus Satellite PLTG** (p.17). The arkoblock's internal system is NOT accessible from outside
except by hacking through this heavily protected satellite network, so a team without a top-notch decker
cannot get in remotely at all.

| Security Code | Trigger | Event |
|---|---|---|
| Red-10/15/15/13/13/14 | 2 | Probe-5 |
| | 4 | Binder-5 |
| | 6 | Killer-6, Passive Alert |
| | 8 | Blaster-6 |
| | 10 | Blaster-8, Active Alert |

**2. Proteus Arkoblock PLTG** (p.17). Reached through the satellite network or by jacking in on site;
jackpoints exist in the main building, the docks, the hangar, the launch pad, the fitness center and the
hangar conference room where "emergency landing" visitors are parked. The gamemaster creates sheafs for
any specific host inside the PLTG a decker wants.

| Security Code | Trigger | Event |
|---|---|---|
| Orange-6/10/10/9/8/10 | 3 | Probe-5 |
| | 7 | Binder-5 |
| | 11 | Tar Baby-6 |
| | 14 | Killer-6, Passive Alert |
| | 17 | Blaster-6 |
| | 20 | Blaster-8, Active Alert |

**3. Alaxa Host** (p.40). Not on the Matrix at all: reachable only from a workstation inside the
building (office workstations need a passcode), the server room computers or the roof satellite dish.
Sculpted as a swarming mass of jigsaw-puzzle pieces on a light background; each successful operation
snaps a few pieces together into an appropriate icon or scenescape.

| Security Code | Trigger | Event |
|---|---|---|
| Orange-6/8/12/8/10/12 | 5 | Probe-5 |
| | 12 | Probe-7 |
| | 17 | Passive Alert, Tar Baby-6 |
| | 21 | Active Alert, Blaster-8 |
| | 27 | Shutdown |

**4. Yamatetsu PLTG (Shibanokuji)** (p.40). Reached only by being inside the Alaxa host at the moment of
the hourly one-minute burst uplink and logging on; the decker then has 20 Combat Turns before being
kicked off to wait for the next burst. Sculpted as a fantastic alien landscape with massive heavenly
bodies rotating by in the starry sky above. It has real sysops -- if decking goes too easily, drop in a
security sysop (Computer 6, Small Unit Tactics 2 (Matrix 4), Hacking Pool 4, Transys Highlander,
utilities at Rating 6), or protect the target files with Scramble-9 or dataworms.

| Security Code | Trigger | Event |
|---|---|---|
| Red-8/14/14/12/12/16 | 2 | Probe-9 |
| | 6 | Jammer-6 |
| | 10 | Marker-6 |
| | 12 | Scramble-9 (Access) |
| | 15 | Passive Alert, Blaster-6 |
| | 19 | Jammer-7 |
| | 22 | Active Alert, Tar Baby-8 |
| | 25 | Sparky-9 |
| | 30 | Tar Pit-10 |

**5. Gagarin Transmission Host** (p.40; no security code given). The target host inside the Yamatetsu
PLTG. Locate Access Node, Logon to Host, then Locate File; the search begins turning up relevant material
at 5 successes and the complete set of files is 500 Mp -- instrument readings, condition reports,
position and trajectory telemetry, a full analysis of Gagarin's sensor module and various trajectory
simulations. Payment is 1,000 nuyen per success above five. Search results by successes: 5 = 25 Mp
(Yamatetsu has re-established contact); 6 = 50 Mp (the probe is partially crippled, only partially
communicative, slightly off course); 7 = 100 Mp (its sensor data cannot be accessed remotely); 8 = 250
Mp (it will drop a sensor module on the Earth flyby); 9+ = all 500 Mp (Yamatetsu expects the module to
miss the Sea of Japan near Vladivostok and come down somewhere in North America).

| Trigger | Event |
|---|---|
| 3 | Probe-5 |
| 8 | Probe-9 |
| 12 | Marker-6 |
| 15 | Passive Alert, Blaster-5 |
| 19 | Jammer-7 |
| 22 | Active Alert, Tar Baby-8 |
| 25 | Sparky-9 |
| 30 | Tar Pit-10 |

**6. AresSpace Top Host** (p.74). The AresSpace office park system IS connected to the Matrix and Griebe
can supply the access node address. Combination tiered / host-to-host configuration: the deeper a decker
goes the tougher the hosts get and the more likely a chokepoint or a timed SAN. Sculpted to mimic the
solar system and various celestial bodies. Royce's own workstation sits on the internal Ares host, level
12 -- burnished golden walls and comfortable furnishings, with a screened alcove and mirror in a shadowed
corner that he unlocks by touching the frame in three places to reach an outside secure line.

| Security Code | Trigger | Event |
|---|---|---|
| Orange-8/13/13/12/11/12 | 3 | Trace-8 with trap Killer-12 |
| | 7 | Killer-10 |
| | 10 | Tar Pit-10 |
| | 13 | Passive Alert |
| | 16 | Construct-8 |
| | 19 | Active Alert |
| | 24 | Scout-8 |
| | 27 | Sparky-8 |
| | 30 | Shutdown |

**7. AresSpace Building C** (p.74). Deeper in the same system; a jackpoint sits behind the empty
reception desk on the ground floor and the building's host hardware fills First Floor Room 3.

| Security Code | Trigger | Event |
|---|---|---|
| Red-6/15/16/17/15/13 | 2 | Probe-7 |
| | 6 | Tar Baby-9 |
| | 10 | Passive Alert |
| | 12 | Tar Pit-5 |
| | 16 | Tar Pit-7 |
| | 20 | Active Alert |
| | 22 | Crippler-7 |
| | 25 | Ripper-7 |
| | 28 | Non-Lethal Black IC-7 |
| | 30 | Shutdown |

**Not mapped**: the Apollo station security host (only referenced as an optional obstacle -- a decker may
need to open the airlock doors from it); the Asgard data haven, where the Liberty auction is run through
anonymous dropboxes (see p.34, Target: Matrix); the Seattle Shadowland data haven, used for Hoff's
anonymous job ad, Griebe's recruiting and the "Runner X" dropbox (password: Griebe); and Niwimaja's
single Matrix connection, hidden and unused in the clutter of the council hall.
"""

NOT_BUILT = """
- **Gotterbote**, **Gagarin**, **Velox I** and **Velox II**, **Gigas** and **Kepler** (the Probe Race
  hardware), the **Liberty** virus, the **Safe Target ring**, the **Winternight bodyguard drone** and the
  **Haifisch II** observer drones -- objects and vehicles, folded into the rows that carry them.
- **Asgard** (the data haven hosting the Liberty auction) and **Shadowland** (Hoff's anonymous job ad,
  Griebe's recruiting channel and the "Runner X" dropbox) -- name-drops with sourcebook references.
- **General Saito** -- named only as the man who seized the Bay Area; on the Californian Protectorate
  row. **Adrian Silvermoon** -- Manitou founder, named only as the woman Youngman was protege to and
  helped oust. **Gabriel** -- the referral name that got Royce his secure line to the Kepler contact.
  **The Kepler project head** and **the Lone Star executive**-equivalent unnamed hooks.
- **The Metahuman People's Army** -- named once as a smuggler's other cargo in the Bay Area.
- **The fishing village** thirty minutes outside Cayenne ("two huts and a dog"), the **Kourou jail**, the
  **Edwards Aerospace Center** fallback launch site, the **Community Chest brothel** and the Apollo
  gambling hall, the **New Orleans Mafia** and the **zobop** krewes leaning on Mercy -- unnamed or
  single-line places and factions, folded into the location and NPC rows.
- **Proteus guards, Sub-Marines, security mages, security riggers and the rescue squad**; **Kourou
  policemen**; **Alaxa guards**; the **Manitou militia**; **Yamatetsu's four enforcers, electronics
  specialist and magical specialist**; **Mr. Johnson's two ork bodyguards**; the **Vertigo bouncers**;
  **Cape Canaveral security officers, security mages and corporate representatives**; **Apollo security
  officers**; **Knight Errant officers, the night shaman and the security rigger**; the **Firewatch mage,
  rigger and three soldiers**; and the **SMART mage and four team members** -- stat blocks carried on the
  org and location rows.
- **The first Yamatetsu recovery team** (six dead in the ambush hollow), the **helicopter crew**, the
  **Force 7 wind spirit** and the **Spirit of the Land** that buried the module, the **Force 5 city
  spirit** and **Force 3 watcher** at the AresSpace park, and the **three Force 5 bound air elementals**
  at Cape Canaveral -- on the location rows.
- **Hausmann's taxi driver**, the **nine dinner guests**, the **Alaxa night staff**, the **La Ronge
  guide** (use the Amerindian Tribesperson, p.74 SRComp) and the **Water Works barfly** Sketch is
  chatting up -- nameless single-scene figures.
- **The unidentified craft inside Halley's coma** and its **sample drones** -- the campaign's real
  loose end, deliberately left unexplained.
"""

PLAY_NOTES = """
- Three separate runs, not one campaign arc: the only connective tissue is the Probe Race. Run them in
  print order and treat the February handout dateline in The Price of Liberty as loose, or swap the last
  two adventures so the dates line up. Nothing in any adventure depends on the others.
- **The Messenger** is explicitly linear and explicitly bad for deckers -- offer a decker player an
  alternate character (a rigger or magician) or build extra Matrix work in. Take it easy on the team
  through the Bala meet; they are in plenty of trouble soon enough. The arkoblock is a fortress from the
  outside and light on the inside, so let the plan be the fun part. If it scares them off, Hoff produces
  the dinner party instead -- and if they fail twice he calls the run off entirely.
- Hausmann is the whole trick: play him sincere, friendly, down-to-earth and completely innocent, and
  generate real sympathy for him, so that the later revelation lands. He will trigger his own cranial
  bomb rather than let magic expose Winternight, which kills the plot dead unless you prefer to let the
  runners learn the truth first and then have him die.
- Get rid of the ring AND beat the ritual tracking and the Proteus raid never happens at all -- the book
  says to congratulate the players for being thorough and skip straight to Masquerade. Reward that.
- The Messenger's best ending is evidence, not gunfire: getting the murder recording to Proteus or the
  Kourou police clears the team of Hoff's death and gets the payload examined before it flies. Stopping
  the launch by force works and makes Proteus a permanent enemy over millions of nuyen.
- **Catch a Falling Star** is a negotiation adventure wearing a wilderness adventure's coat -- "firepower
  may not be needed at all; finesse and smooth talking will be far more important." Decide the employer
  before play, since it sets both the gear and the objective (recover, wipe, corrupt or destroy).
- In Niwimaja the runners cannot address the council; they must win a faction and be represented. Learn
  the six NPCs cold and play the town's internal quarrel, not the module. Race and cyberware matter at
  every door. Fifty-to-one odds, home ground and strong magic mean violence loses; hostages win the
  module and end the team's chance of leaving Manitou land alive.
- If neither side argues well enough, let the council decide by ordeal -- a sweat lodge, a storytelling
  contest, the best joke, babysitting while the hunt goes out, cleaning a kill, carving a totem pole.
  "Okay, Mr. Shadowrunner, let's see how quickly you can skin an arctic fox with a bone knife."
- The module's payoff is a campaign hook, not a paycheck: months of decryption yield mostly corrupted
  data, and the clearest readings show another craft keeping station inside the comet's coma taking on
  returning sample drones. Somebody already won the Probe Race and said nothing. Let that sit unresolved.
- **The Price of Liberty** hinges on one ethical choice at the Yard, so build to it: professional pride
  and money on the way in, then a negotiator who offers double pay and corporate protection for one
  address. Give the players a few minutes to decide and no longer. Either answer ends in a firefight.
- Never let the ten-million-nuyen case stay in the runners' hands; the book is explicit that it would
  break a campaign, so it falls through their fingers one way or the other.
- Apollo is a roleplaying set piece: background count 9 leaves Awakened characters cut off and homesick,
  orks and trolls do not fit the doorways or the bunks, and the spacewalk is a Willpower Test against
  sheer terror before it is a skill test. Make the players sweat; they would have to work hard to fail it.
- Griebe is a career-maker. She never turns on her runners unless it is their fault, she rarely looks for
  new talent, and turning her down or whining about the last job means she never calls again -- say so
  through a contact if the players do not feel it.
- Karma. The Messenger: surviving 2, threat level 2, preventing the nuke from launching 1. Catch a
  Falling Star: survival 1, completing the Alaxa/Shibanokuji datasteal 1, doing it unspotted, untraced
  and without killing anyone 1, retrieving or destroying the module's data as instructed 2, successfully
  negotiating with the Manitou 1, using the Yamatetsu arrival to their advantage 1, a creative solution
  1. The Price of Liberty's table is lost in the OCR but rewards survival, completing the Apollo run,
  extracting Royce, escaping the exchange with the money, and not betraying Royce.
- Loose ends worth keeping: a live Anderson or Howe and Winternight's hired guns; new contacts in Sketch,
  Mercy, Charlie Davis, Emil Verdan and Shaun Ojibwan; Pierre O'Rourke's grudge;
  the Manitou secession heading for civil war; whichever corp did not get the Liberty code; and the
  unidentified craft in the coma. The book's own back-page poll left the Probe Race winner to the table.
"""



