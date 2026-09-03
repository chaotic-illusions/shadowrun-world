# Dark Angel (FASA 7313, 1993, SR2) -- campaign order #18. Seattle Center / Everett (Pinehurst,
# Lowell) / South Tacoma / Renton (Merideth, Maple Valley) / Downtown / Puget Sound, 2054.
# Dating: the introduction says flatly "The year is 2054" and the campaign sheet places the book in
# 2054; both news handouts are dated "Friday, September 8 2051" -- September 8 is a Friday in 2051
# and a Tuesday in 2054, so the handout template date was carried over from the 2051 books. The year
# follows the intro; the month follows the handout day and is a best guess.
# Other editing inconsistencies noted in the affected rows: the magical-protection agency behind
# Xanadu's blue PANICBUTTON is "Hermetic Securities Unlimited" on p.21 and "Hermetic Protection
# Services, Inc." on p.24; Lili Ice has only an apartment (p.14) until p.44 gives her a "talisman
# shop" with windows to smash; Lone Star officers are Threat/Professional 3/3 on p.24 and 2/2 on
# p.40; Akmura is a lean tattooed woman in tight dark clothes in the prologue and a "plain little
# woman" in casual Western clothing on p.64; the ship carries "four of the six Oni-do" but only four
# Oni-do trolls plus Mushui are statted; Akmura's yacht is "well outside the harbor" in Puget Sound
# yet the astral view shows the trees of Council Island (Lake Washington); the failure handout has
# Earth Dawn released by Xanadu with Angel still "dead", the success handout has Angel announcing it
# in person; "After the Adventure" says Earth Dawn is recorded months after the rescue. Several stat
# blocks are garbled in the OCR (Julie Wallace, Bryan, Nolan, Kachu, the Lab Rats, Eagle and Sal,
# Hack and Slash's attributes) -- reference the book for those.
# Source text: docs/Adventures/text/SR2-Dark_Angel.txt (72 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "Dark Angel"
ORDER = 18
SOURCE = "SR2-Dark_Angel.pdf, pp. 4-72"
YEAR = "2054 (September)"

SYNOPSIS = """
Two weeks ago Lone Star pulled the burned remains of the elven street rocker **Dark Angel** out of
**Heaven**, a notorious BTL den in Lowell, Everett, and the coroner called it a chip suicide. Before
the ashes were cold a promoter named **Dynamo Blue** was waving a signed will that gives her studio,
**Xanadu Studios**, every song he ever wrote, and the first Dark Angel album, *Flaming Wings*, is top
of the local charts -- from a man who refused on principle ever to record. His lover, the small-time
talismonger **Lili Ice** ("Icelady"), hires the runners in the back room of **Club Chiaroscuro**:
prove Dynamo killed him and the will is void, or "encourage" her to give the songs up; 100,000 nuyen
out of the record profits, 1,000-1,500 each in advance.

The truth: Angel is Jim Crull, younger brother of **Edward Crull**, a Mitsuhama thaumaturgical
analyst who in 2043 bought his promotion with a rite of fealty to the yakuza oyabun **Kat Akmura** --
a rite that pledged his whole household. Jim skipped the ceremony, took his guitar to the street, and
sang more truth than Akmura liked. She waited eleven years, until he had something to lose. Then she
had him clubbed in an alley by an Oni-do troll, had **Hack and Slash** dress a murdered squatter as
his corpse, had a Lone Star executive bury the case, forced him to record, made him sign the will,
and now keeps him chained beside a fish tank in her cabin on the yacht **Shio-Zuchi**, anchored in
Puget Sound, singing on command. Edward planned the kidnapping. Dynamo is a pawn who pays "Crull-san"
eighty percent.

The leads cross and re-cross: Xanadu's run-down offices in Renton (a Knight Errant shadow site next
door, a platinum ring in Dynamo's drawer, a Matrix full of payments to "Mr. Crull"); **Lieutenant
Dolchev** at **Lone Star Precinct 249**, who will sell the name of the man who ordered the cover-up
for 5,000 nuyen and professionalism; the **Golden Gators**, the culties and the yakuza spies at
Heaven, and the two bodyboys who built the corpse; Angel's band, the **Fallen Heroes**, who have been
handed a forged chip "proving" Lili sold him out and are about to beat her up; and Crull's house in
Maple Valley, where his trafficked Haida wife **Sarah Crull** knows almost everything. Two hit teams
come for the team along the way -- Crull's punks and samurai staging a fake sniper-and-cops scene,
then Akmura's Oni-do assassins **Akimoto** and **Kure** driving a mob-minded gang in front of them.

Nobody kills a yakuza oyabun and lives unless another oyabun says so. The runners must go to **Shiro
Usaka** in the loft of the **Mindwarp** (Akmura's treacherous ally, who will test them with an ambush
and then hand them an ivory thimble) or to the serene old **Homatsu Jinjiro** at his estate **Marian
Parks** (senior oyabun of the Sword Water clan, who wants Akmura humbled and will give them the deck
plans on condition of one clean hit). Then a James Bond climax on the Shio-Zuchi: machine-gun ports,
a warded hull, a torpedo shark under the keel, four troll physical adepts, two mages, and Akmura's
minisub and scuttling charge. Angel comes home quiet and pensive, re-releases *Flaming Wings* under
his own name, and gives most of the money away.
"""

TIMELINE = """
- **2043** -- Edward Crull seeks promotion in Mitsuhama's hermetic-research division; Akmura demands
  the household rite of fealty; Jim Crull skips it, hits the street as Dark Angel, meets Lili Ice.
- **About a month before the meet** -- Angel plays The Whistler, is clubbed in the alley, wakes on the
  Shio-Zuchi. Hack and Slash deliver a burned squatter's corpse; Lone Star rules suicide. *Flaming
  Wings* released; the forged Global Trust chip is handed to Bryan and Drew at Heaven.
- **Two weeks before the meet** -- Lili learns of the "suicide" (p.9).
- **Day 1** -- the meet at Club Chiaroscuro (Julie Wallace's watchers listening; Julie may tip Shiro).
  Hours later Sheera Persian phones Lili with the account number; Lili summons the runners.
- **Day 1-2** -- legwork: Xanadu (1D6 hours of bugging catches Dynamo's call to Crull), Precinct 249,
  Heaven, the Partyzone (1D6 hours before the band leaves). Crull learns of the team from the yakuza
  spies, Dolchev, Orduffer, or Xanadu's cameras; the Smash 'n' Grabbers hit Lili's windows and the
  fake sniper ambush waits a block away. Crull finds an average team within a day.
- **Day 3 if nothing intervenes** -- the band roughs Lili up outside her apartment. If the runners
  sit still two days and Crull knows about Lili, he kills her.
- **After Crull fails** -- Akimoto and Kure find the team in 1D6 hours and attack after an hour of
  astral tailing. Usaka's test ambush or kill team may come at any point after the Mindwarp visit.
- **Climax** -- the Shio-Zuchi; Akmura flees when four of six Oni-do are down; the ship sinks in 4D6
  minutes.
- **After** -- Angel's bland press statement; *Flaming Wings* re-released; *Earth Dawn* months later;
  he marries Lili. **Epilogue** -- press reports *Earth Dawn: The Scourge*; a fire destroys his home
  and studio; he and Lili vanish; a lone witness saw three elves. (News handouts: Friday September 8,
  14:00 -- see the header comment on the date.)
"""

ORGS = [
    {
        "name": "Sword Water Clan",
        "org_type": "yakuza clan",
        "tier": 4,
        "headquarters": "Marian Parks (Homatsu); the Mindwarp (Usaka); the yacht Shio-Zuchi (Akmura)",
        "summary": "The yakuza clan of 'this part of the sprawl': senior oyabun Homatsu Jinjiro over the young rivals-turned-allies Kat Akmura and Shiro Usaka; fingers in Mitsuhama",
        "description": (
            "'We deal with three oyabuns in this part of the sprawl, all from the Sword Water clan' "
            "(also 'the Sword Water Society'). Homatsu Jinjiro, one of the city's oldest oyabun, has run "
            "his territory for more than thirty years from behind the scenes and is the nominal superior "
            "of the two young Turks: Kat Akmura, who struck big nuyen somewhere, has her fingers in "
            "several corporate pies (music, body-dumping, office politics at MCT) and is said to have "
            "stolen Seattle out from under two or three big oyabun in Japan; and Shiro Usaka, the weakest "
            "of the three, who fought for years to take Akmura's rackets, lost, and formed an alliance of "
            "convenience with her rather than keep Homatsu on top by their feuding. All three have their "
            "fingers in Mitsuhama Computer Technologies. The clan keeps silent ninja warriors (Chigo "
            "Akwe trained with them from fourteen), soldiers in gray hats, wired 'special assistants', "
            "troll bouncers, mages (Kojika, Kachu) and, through Akmura, the hired Oni-do. Members mark "
            "themselves with colorful tattoos in concealable places -- the higher the rank, the more "
            "extensive. The code is zuni, honor; the tradition is fraternity and vendetta, and anyone "
            "who harms a member without the sanction of other members has signed his own death warrant."
        ),
        "leadership": [
            {"name": "Homatsu Jinjiro", "title": "Senior oyabun (Sword Water clan)", "notes": "Traditionalist; wants Akmura humbled; grants one clean hit."},
            {"name": "Kat Akmura", "title": "Oyabun (Seattle operations from the Shio-Zuchi)", "notes": "Holds Dark Angel; Edward Crull's patron."},
            {"name": "Shiro Usaka", "title": "Oyabun (the Mindwarp)", "notes": "Akmura's ally of convenience; waits to join the winning side."},
            {"name": "Kojika", "title": "Chief henchman and mage to Usaka", "notes": None},
            {"name": "Kachu", "title": "Advisor and bodyguard mage to Akmura", "notes": None},
            {"name": "Chigo Akwe", "title": "Chief ninja in Homatsu's service", "notes": None},
        ],
        "notes": (
            "Dark Angel: killing Akmura without permission from Homatsu or Usaka makes Chigo Akwe the "
            "team's stalker for the rest of the campaign (poison gas, DMSO contact poison, sabotaged gear, "
            "murder in someone else's cell); attacking Homatsu himself brings hits from oyabuns across the "
            "world. Legwork TN 4 (Fixer, Media Producer, Street Cop, Yakuza Boss, Mafia types): 1 the "
            "three oyabuns with fingers in MCT; 2 Homatsu is senior; 3+ Usaka and Akmura used to be fierce "
            "rivals and are getting along lately. Stat blocks: yakuza soldiers p.32 (B5 Q6 S5, Boosted "
            "Reflexes 1, smartlink, HK227, Threat 5/4); special assistants p.34 (Wired 3, Init 12+4D6, "
            "Armed Combat/Firearms/Unarmed 8); Mindwarp troll guards p.31 (B10 S12, Boosted Reflexes 3, "
            "Muscle Replacement 2, club 13M Stun); Jinjiro's bodyguards p.39 (physical adepts, "
            "Init 7+3D6, monofilament whips, SCK Model 100); yakuza spies p.29 (cyberears, hand razors 8, "
            "fight to the death). Seattle Sourcebook pp.153-154 for the wider yakuza. DISCREPANCY: the "
            "campaign's established Seattle yakuza is the Watada-rengo; this book never names it. Treat "
            "the Sword Water clan as one clan under or beside the rengo (as Elven Fire's Dungeness Crabs)."
        ),
        "allies": ["Oni-do", "Mitsuhama Computer Technologies", "Xanadu Studios"],
    },
    {
        "name": "Oni-do",
        "org_type": "warrior cult / assassin society (troll martial artists)",
        "tier": 3,
        "headquarters": "Japan (an 'orphan society' for goblinized children of the Ginza); Seattle presence aboard the Shio-Zuchi",
        "summary": "'The Way of the Goblin': yakuza-run society that takes Japanese goblin kids, breeds and trains trolls from birth as hitters, and sells clean kills to anyone with the cred",
        "description": (
            "Oni-do, the Way of the Goblin, is a warrior cult of troll martial artists run by 'a buncha "
            "wizboys'. 'You know how the Japanese feel about goblin kids? If you're a mama-san in the "
            "Ginza with a troll in the family tree, the Oni-do will take the little trog off your hands.' "
            "They take goblin kids and teach them to kill, breed trolls and train them from birth, and "
            "dust folks for the honor of a clean kill, selling their services to anyone with the cred; "
            "in Seattle their biggest employer has to be Kat Akmura, whose bodyguards they are. The "
            "trolls' inhuman physiques and complete indoctrination leave them no outside interests or "
            "friends -- they live for duty alone. Their symbol is a fanged face with the Japanese "
            "characters for 'Goblin Way', worn on katana hilts and fetishes. The society also keeps a few "
            "human magicians (Mushui, the Rat shaman Akimoto) who attach themselves to the trolls to "
            "practice their craft."
        ),
        "notes": (
            "Dark Angel: Oni-do troll block p.53: B11(13) Q3(4) S10(11) C1 I1 W5, Init 2+3D6; Athletics 2, "
            "Armed Combat 6, Axe 8, Firearms 4, Gunnery 3, Unarmed 5; adept powers Improved Ability Armed "
            "Combat 2, Improved Physical Attributes Quickness 1 / Strength 1, Increased Reflexes 2; armor "
            "jacket, combat axe, SCK Model 100; severe allergy to SILVER; Resist Pain (Serious) sustained "
            "on all of them by Mushui. Four trolls plus Mushui and Kachu on the ship; Akmura hires two more "
            "trolls if Usaka tips her off. Assassins Akimoto (Rat shaman, Grade 2 initiate) and Kure (troll "
            "adept) are the 'best hit team'. Legwork TN 4 (Fixer, Street Samurai, Talismonger, Yakuza Boss, "
            "dockworkers). 'Any team that refuses to decisively end this adventure must fight an endless "
            "stream of Oni-do, and the organization has other operatives with skills at least equal.'"
        ),
        "allies": ["Sword Water Clan"],
    },
    {
        "name": "Xanadu Studios",
        "org_type": "corporation (recording studio)",
        "tier": 2,
        "headquarters": "A small industrial center in Renton's Merideth district",
        "summary": "Dynamo Blue's small-time studio that suddenly owns Dark Angel's music and pays Edward Crull eighty percent of it",
        "description": (
            "A tiny recording corporation that meant nothing to anybody -- two or three little successes, "
            "the Lab Rats' first record -- until its owner Dynamo Blue produced a signed and validated "
            "will and released Flaming Wings, the hottest recording in Seattle music history. It remains "
            "small-time because the yakuza siphon off most of the real money: several million nuyen have "
            "gone to Mr. Crull as 'Community Donations', 'Annual Gratuities' and 'Miscellaneous Services "
            "Rendered', roughly the album's income. Ten guards under two mercenary captains, a camera "
            "net, PANICBUTTONs to Lone Star and a blue button to a magical-protection agency. Akmura can "
            "replace guards, buildings, even Dynamo; every Xanadu music and business document is on chips "
            "in cold storage on her ship, so no matter how many times the team destroys the place it "
            "bounces back. Success ending: Angel cancels the relationship and Zor Entertainment takes over; "
            "failure ending: Xanadu releases the second album, Earth Dawn."
        ),
        "leadership": [
            {"name": "Dynamo Blue", "title": "Owner / Director", "notes": "Akmura's pawn; pays 'Crull-san' 80 percent."},
            {"name": "Mike Orduffer", "title": "Advertising executive", "notes": "Owes Akmura 20,000 nuyen; reports every irregularity to her."},
        ],
        "notes": (
            "Dark Angel: Legwork TN 4 (Club Habitue, Club Owner, Media Producer, reporters, rockers): 1-2 "
            "Dynamo has the highest body count in the biz, love 'em and dump 'em; 3 no connection with "
            "Angel before Flaming Wings; 4+ Blue should be a lot richer than she is -- the studio is still "
            "a fragging hole and she lives on Nuke-&-Serve takeout. Guard blocks p.23-24 (guards Threat "
            "3/2, Uzi III; captains Wired 2, HK227, cut their losses). Computer system in the prep doc."
        ),
        "allies": ["Sword Water Clan"],
    },
    {
        "name": "Fallen Heroes",
        "org_type": "go-gang / rock band",
        "tier": 1,
        "headquarters": "The Partyzone, South Tacoma (squatting an empty warehouse beside it)",
        "summary": "Dark Angel's band and the 'musical musclemen' go-gang that keeps the peace at the Partyzone; Bryan, Drew, Sheera Persian, Nolan",
        "description": (
            "A pack of go-gangers from Tacoma who called themselves the Fallen Heroes 'but were really "
            "more of a band': armored jackets, Day-Glo mohawks, and a love of music as strong as their "
            "love of gang action. They enforce the peace at the Partyzone vacant lot, neutral ground for "
            "the South Tacoma gangs, and set up its nightly concerts. Dark Angel played and partied with "
            "them; his band -- the elf brothers Bryan and Drew (both Heroes), the sorcerer-singer Sheera "
            "Persian and the barefoot Irish elf Nolan -- still meets on Heroes turf nursing its shock and "
            "plotting revenge on Lili Ice, whom it believes sold Angel to Xanadu. 'Their music's okay, but "
            "they're going nowhere without Angel.'"
        ),
        "leadership": [
            {"name": "Bryan", "title": "Band leader (guitar); Fallen Heroes", "notes": None},
            {"name": "Drew", "title": "Lead vocalist; Fallen Heroes", "notes": None},
        ],
        "notes": (
            "Dark Angel: gang block p.18 (6): B5 Q6 S5 C6 I5 W4, Init 5+1D6, Threat 2/2, Armed Combat 5, "
            "Bike 4, Firearms 4, Stealth 5, armor jacket, Beretta 101T, club; join a Partyzone fight 1-3 at "
            "combat turn 2 and 1-3 more at turn 4. The band wants 'what we've got coming' from the "
            "record; a fake Global Trust chip (account 22343, over 1,000,000 nuyen 'from Xanadu' to Lili) "
            "handed to Bryan and Drew at Heaven by a Japanese punker on Akmura's orders convinced them; "
            "the real Xanadu accounts or Hack and Slash's testimony clears her, though nothing makes them "
            "like her. They will not kill; kill one of them and the survivors murder Lili by any means and "
            "the Heroes dog the team in future adventures. They know everything under Dark Angel in "
            "Legwork."
        ),
    },
    {
        "name": "Golden Gators",
        "org_type": "street gang (BTL dealers)",
        "tier": 1,
        "headquarters": "Heaven, the ruined clinic BTL den in Lowell, Everett",
        "summary": "Ex-thrill-slashers turned chip dealers who consider themselves the proprietors of Heaven; led by the Gator shaman Lizard Pete",
        "description": (
            "Sweet-faced gangers in jackets painted with a gray rock below crossed keys and the words "
            "'Golden Gators', selling chips outside Heaven and watching for the cops. After years of "
            "thrill-slashing the gang discovered that BTL offered far higher profits at lower risk; now "
            "they want order on their turf to protect the trade, control Heaven's chip business, keep "
            "other gangs away, and revert to the old violence the moment someone threatens the peace or "
            "'crashes their turf'. 'Chummer, we're writin' you a ticket to hell.'"
        ),
        "leadership": [
            {"name": "Lizard Pete", "title": "Leader; Urban Gator shaman", "notes": "Relaxes and waits for the money; enjoys the battles."},
        ],
        "notes": (
            "Dark Angel: block p.28 (6): B5 Q5 S6(8) C6 I5 W4, Init 5+1D6, Threat 2/2; Armed Combat "
            "(Sword) 8, Unarmed (Grapple) 7, Firearms 4, Negotiation 4; Muscle Replacement 2; armor jacket, "
            "Browning Max-Power, sword. Chips: 50 nuyen per five minutes or 3,000 a chip; on 2D6 = 12 the "
            "chip carries a lethal feedback error (4D Stun, Willpower (2) or lose a point of Essence). "
            "Fight hand-to-hand; shot at from range they hide in the basements under Heaven. Etiquette "
            "(Street) 6: 0 'Buzz, chummer' (then attack); 1 'Angel never hung here'; 2 they point out the "
            "'salvage team', Hack and Slash. Smart enough to stay out of the Angel mess."
        ),
    },
    {
        "name": "Hot Papas",
        "org_type": "street gang",
        "tier": 1,
        "headquarters": "Tacoma",
        "summary": "Heavyset Tacoma gangers of mixed ethnicity who hire out to corporate executives in hopes of cutting-edge cyberware; Crull's replacement muscle",
        "description": (
            "A Tacoma street gang with dreams of cutting-edge cyberware, mainly heavyset human men of "
            "mixed ethnic groups, who gladly contract themselves out to corporate executives in hopes of "
            "acquiring enhancements. Edward Crull uses them to replace any losses among his hired killers "
            "-- not professionals of the same caliber, but well armed."
        ),
        "notes": "Dark Angel: block p.44: B5 Q6 S5 C6 I5 W4 E5.8, Init 5+1D6, Threat 2/2; Firearms 6, Armed Combat 5, Stealth 5, Bike 4; thermographic eyes; Ares Predator (smartlink), FN HAR (APDS, external smartlink, gas vent III), armor jacket.",
    },
    {
        "name": "Smash 'n' Grabbers",
        "org_type": "thrill gang (troll)",
        "tier": 1,
        "headquarters": "Everett / Seattle streets (turf not given)",
        "summary": "Timid hulking troll thrill-gang of burglars, muggers and car-lifters under the tattooed Sweet Petunia; hired by Crull's punk to smash Lili's windows",
        "description": (
            "Trolls who believe their sheer size should terrify smaller races into submission, and turn "
            "tail and run when it fails. They support the gang through burglaries, muggings and car "
            "theft -- a group of gangers lifts the car and carries it away by hand. Pretty timid for such "
            "hulking brutes; they will do anything to avoid a real fight."
        ),
        "leadership": [
            {"name": "Sweet Petunia", "title": "Leader", "notes": "Male; body covered in tattoos of bloody daggers, dragons and hairy mythological beasts."},
        ],
        "notes": "Dark Angel: block p.44 (6): B9 Q3 S9 C1 I1 W2, Init 2+1D6, Threat 2/3; Unarmed 6, Stealth 5, Armed Combat 4; Ares Predator, armor jacket, sword. Half a dozen are recruited by one of Crull's punks to smash the windows of Lili's shop and shout threats -- bait for the ambush a block away; they flee at the first sign of trouble.",
    },
    {
        "name": "Caesar's Scythers",
        "org_type": "street gang",
        "tier": 1,
        "headquarters": "Seattle streets (turf not given)",
        "summary": "Kevlar-and-chain-mail gangers under Caesar and his wizlady Cleopatra, mob-minded by Akimoto into the Oni-do ambush",
        "description": (
            "The sprawl breeds thousands of punks like these: vacant-eyed youths in armor of kevlar, "
            "chain mail and chrome with the name Caesar's Scythers on their jackets. They were simply in "
            "the wrong place when the Oni-do shaman Akimoto decided to collect muscle for his run and put "
            "four of them under a Mob Mind spell. Their leaders, the street samurai Caesar and the shaman "
            "Cleopatra, know a spell was cast over their chummers and are not happy campers."
        ),
        "leadership": [
            {"name": "Caesar", "title": "Leader (street samurai)", "notes": "Street Samurai archetype, SRII p.62."},
            {"name": "Cleopatra", "title": "Wizlady (street shaman)", "notes": "Street Shaman archetype, SRII p.63."},
        ],
        "notes": "Dark Angel: block p.50 (4): B6 Q6 S6 C4 I3 W2 E4.8, Init 4+1D6, Threat 5/4 under Mob Mind (1/2 without it); Firearms 6, Unarmed 6, Armed Combat 4; thermographic eyes, spurs (8M); AK-97 (gas vent III), armor jacket. Rush, grapple and overwhelm in melee, dig in when the lead flies, hold until they die. GM bail-out: Caesar and Cleopatra arrive looking for the invisible pair.",
        "enemies": ["Oni-do"],
    },
    {
        "name": "Lab Rats",
        "org_type": "rock band",
        "tier": 1,
        "headquarters": "Xanadu Studios, Renton (their label)",
        "summary": "Gutterpunk band in spray-painted denim, pipes and chains; Xanadu's other act, negotiating their second record 'Child of Fire'",
        "description": (
            "Little more than a group of gutterpunks from the harder side of town, always jazzed for a "
            "little action -- 'thrills keep the music pumpin''. Eight plexers in spray-painted denim who "
            "wear pipes, chains and other hardware as costume and weapon. Dynamo put out their first "
            "record; their agent Clifton Perkins is negotiating a contract for their latest, Child of Fire. "
            "Proud to share a label with Dark Angel: 'Like, way to go Dynamo, way to go Rats.'"
        ),
        "notes": "Dark Angel: block p.22 (8): B4 Q5 S5 C6 I4 W6, Init 3+1D6, Threat 2/2; Armed Combat (Clubs) 8, Etiquette (Street) 5, Instrumental Music 6; datajack, synthlink; armor jacket, club. Jump in to defend Xanadu if a free-for-all starts, try to cool down anyone who looks like starting one.",
    },
    {
        "name": "Hermetic Securities Unlimited",
        "org_type": "magical-protection agency",
        "tier": 2,
        "headquarters": "Seattle (not given)",
        "summary": "Astral-response contractor whose blue PANICBUTTON delivers a Force 7 fire elemental to a client within one Combat Turn",
        "description": (
            "A magical-protection agency that sells astral security to clients with no magical defenses "
            "of their own. Xanadu Studios' guards carry its blue PANICBUTTON: pressed, a Force 7 fire "
            "elemental 'in the employ' of the agency appears within one Combat Turn (astral response "
            "times are fast) under precise instructions to attack anyone or anything present in astral "
            "space in or near the client's premises."
        ),
        "notes": "Dark Angel: named 'Hermetic Securities Unlimited' on p.21 and 'Hermetic Protection Services, Inc.' on p.24 -- the same outfit. Elemental block p.24: B8 Q10 S5 C7 I7 W7 E7 R8, Init 18+1D6 (28+1D6 astral), Threat 4; Engulf, Fire Aura, Fire Projection, Guard, Manifestation; Vulnerability (Water).",
    },
    {
        "name": "BodyBits Organ Donation Service",
        "org_type": "corporation (body-parts clinic)",
        "tier": 2,
        "headquarters": "Everett (not given)",
        "summary": "Medical clinic that pays bodyboys a finder's fee for every unclaimed corpse and recycles the parts; Hack and Slash's employer",
        "description": (
            "One of the clinics that pays a finder's fee to bodyboys -- underprivileged citizens who "
            "supplement their income by turning recently deceased bodies over for recycling. Its "
            "'freelance collection agents' Hack and Slash work Heaven, where the firefights and lethal "
            "BTL provide a ready source of merchandise, and it pays a pair of unskilled trolls pretty "
            "well."
        ),
        "notes": "Dark Angel: the official story says Lone Star received Angel's corpse 'indirectly from two bodyboys'. Legwork on Dark Angel (2-3 successes): 'a coupla trolls called Hack and Slash who wuz gonna sell him for spare parts'.",
    },
    {
        "name": "Friends of Trolls",
        "org_type": "metahuman awareness group",
        "tier": 2,
        "headquarters": "Seattle",
        "summary": "Metahuman awareness group on its second recruitment drive: 5,000 nuyen buys a Trollfriends T-shirt and bumper sticker (news handout)",
        "description": (
            "A metahuman awareness group kicking off its second recruitment drive in September 2054. For "
            "a donation of 5,000 nuyen individuals receive T-shirts and bumper stickers identifying "
            "themselves as Trollfriends. 'Showing one's support for the troll community isn't just a "
            "matter of politics. It's a very healthy step for an individual.'"
        ),
        "leadership": [
            {"name": "Butch Hatchett", "title": "Leader in the Trollfriends movement", "notes": "A troll himself."},
        ],
        "notes": "Dark Angel: news-handout texture (both endings). A natural foil or ally for Humanis plots; the 5,000-nuyen donation tier suggests a well-heeled membership.",
    },
    {
        "name": "Zor Entertainment",
        "org_type": "corporation (music production)",
        "tier": 2,
        "headquarters": "Seattle",
        "summary": "The production company that handles all Dark Angel productions after he breaks with Xanadu (success ending)",
        "description": "Named only in the success news handout: after Dark Angel's return 'Zor Entertainment now handles all Angel productions', including the second album, Earth Dawn.",
        "notes": "Dark Angel: exists only if the runners bring Angel home. Not to be confused with Club Zor (Ivy & Chrome).",
    },
    {
        "name": "Seattle Paranormal Facility",
        "org_type": "research institute (parazoology)",
        "tier": 2,
        "headquarters": "Seattle",
        "summary": "Parazoology research facility whose researcher Luke Emerson was eaten by torpedo sharks during a feeding-frenzy field study (news handout)",
        "description": "A Seattle parazoological research facility. In September 2054 its researcher Luke Emerson was killed by a school of torpedo sharks (Portheus velocis) in Puget Sound while gathering data on feeding frenzies. 'He had said he really wanted to get inside these animals,' said colleague Dr. Sheila Clinton of Seattle University. 'I guess he got his wish.'",
        "notes": "Dark Angel: news-handout texture. A torpedo shark guards the Shio-Zuchi (p.53); the facility is the obvious place to learn what pheromones keep one from straying.",
    },
    {
        "name": "TectonicRock (Channel 234)",
        "org_type": "media (rock trideo channel)",
        "tier": 2,
        "headquarters": "Seattle",
        "summary": "Rock trideo channel whose reporter works the crowd at Heaven interviewing anyone who will talk about Dark Angel",
        "description": "A rock music trideo channel. Its reporter scans the scene at Heaven with a palm-sized lens, stopping to interview anyone who cares to comment on Dark Angel or his death.",
        "notes": "Dark Angel: reporter uses Media Producer contact stats (SRII p.209) and avoids combat. Handy for planting or reading the public story.",
    },
]

LOCATIONS = [
    {
        "name": "Club Chiaroscuro",
        "location_type": "nightclub",
        "district": "Seattle Center (three blocks from the Space Needle)",
        "security_level": "Patrolled / Commercial",
        "summary": "Light-and-shadow neo-mystic club where Icelady does biz with wizards; owner Julie Wallace's six watcher spirits eavesdrop; two fez-wearing troll Genies on the doors",
        "description": (
            "Black lights and colored neon over neo-mystic decor: patches of darkness chased across the "
            "room by oddly shaped beams, colored lamps flashing multihued shadows, tables, chairs and bar "
            "trimmed in luminescent violet triggered by black lights in the floor, a mirrored dance floor, "
            "Electroslam from the floor speakers and posters for a rocker called Dark Angel who is not on "
            "stage. Well-dressed patrons, many with the deep auras of the magically proficient. Map p.12: "
            "two main entrances with translucent light-studded plastic doors (a Genie at each), bar, "
            "private booths behind synthetic-bamboo sound screens (no barrier to spirits), Julie "
            "Wallace's curtained office (shatterproof windows, bulletproof curtains), storeroom, a stage "
            "at the center of a holographic pentagram shifting red to green to midnight blue, dressing "
            "rooms, one public restroom, a locked staff restroom and a back room of wires, pipes and "
            "building guts where Icelady holds her meet."
        ),
        "notes": (
            "Six Force 3 watcher spirits (three-foot figures in tight jeans, silk shirts and shades, "
            "sipping tiny drinks): two watch for magical threats, four tail interesting guests -- anyone "
            "with Icelady, obvious cyber or magic -- and report to Julie. Anything said here may be "
            "overheard unless a magician watches the watchers. Julie pays protection to Shiro Usaka and "
            "updates him on anyone asking about the yakuza (2,000 nuyen or Etiquette (Street) 6 with 2 "
            "successes buys her silence). Lili spent 3,000+ nuyen of Julie's promotion on Angel's "
            "cancelled gig. Brawl: 1D6 each round, 1-3 club security hits the runners, 4-6 their "
            "opponents; Julie goes invisible (water elemental sustaining) and casts with fire elementals "
            "boosting; afterwards yakuza-connected patrons go out the door and everyone else to Lone "
            "Star, which arrives in 4D6 minutes. 1D6 3-4: Lili is here doing biz with wizards."
        ),
    },
    {
        "name": "Icelady's Doss (Pinehurst)",
        "location_type": "apartment complex",
        "district": "Pinehurst, Everett",
        "security_level": "Low Security",
        "city": "Seattle",
        "summary": "Lili Ice's fifth-floor flat and talisman storeroom; the band, Crull's trolls and the yakuza all come here; 20,000 nuyen of fetishes",
        "description": (
            "The fifth floor of an apartment house in Pinehurst, Everett. An ordinary tan door opens on "
            "the main room, living area, kitchen and storeroom in one: a trid set and a Micron III food "
            "unit competing for space with piles of gray shipping containers stacked to the ceiling, a "
            "few open on the carpet to show stones, feathers and carved-wood fetishes, strangely solid "
            "among the plastic crates and synthfoam packing. Angel never had his own place; he kept his "
            "things here and slept over when he felt like it."
        ),
        "notes": (
            "Lili installs any security the team suggests out of the 30,000 nuyen she can spare; video "
            "camera Rating 4, sound/IR sensor 5, high-tech combination 6 (Stealth/Electronics vs the "
            "watchers' best Intelligence). 20,000 nuyen of fetishes and trinkets on hand, any common item; "
            "most enchanted gear in 24 hours for a price. Fence value of the stock is poor and Lili hires "
            "another team to punish anyone who robs her. Scenes here: the band roughs her up outside "
            "(day 3), the Smash 'n' Grabbers smash 'her talisman shop's' windows while Crull's real "
            "ambush waits a block away, Akmura's trace-triggered assassins. p.44 calls it a shop with "
            "windows; nowhere else does she own one -- the doss doubles as it. 1D6 1-2: Lili is home."
        ),
    },
    {
        "name": "The Partyzone",
        "location_type": "gang territory",
        "district": "South Tacoma",
        "security_level": "No Security / Barrens",
        "controlling_org": "Fallen Heroes",
        "summary": "Vacant lot that is neutral ground for the South Tacoma gangs and Seattle's nightly street-music venue; the Fallen Heroes keep the peace",
        "description": (
            "By day nothing but a large vacant lot: gang symbols and scorch marks on the plascrete walls "
            "of the surrounding buildings, crushed cans and ashes on broken asphalt, a gutterpunk asleep "
            "with his head on a garbage bag. After dark electroslam shakes the tenements as orks, gangers "
            "and elf poseurs mix freely with the rest of the sprawl, moving to Seattle's street musicians "
            "like a single organism. Neutral ground for many South Tacoma gangs; people from all over "
            "Seattle party here regardless of race or affiliation, and anything and everything is "
            "available on request. Dark Angel's band still meets here, squatting one of the empty "
            "warehouses on the map (p.15)."
        ),
        "notes": "The noise makes tracking anyone down virtually impossible. Fights bring 1-3 Fallen Heroes at turn 2 and 1-3 more at turn 4; stalk the band instead and 1D6 hours later they leave and can be accosted outside. The band talks gladly if not attacked; everyone should survive a skirmish here.",
    },
    {
        "name": "Xanadu Studios",
        "location_type": "recording studio",
        "district": "Renton, Merideth district (small industrial center)",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "Xanadu Studios",
        "summary": "Half of a scruffy industrial building with the Kubla Khan poem over the door: lobby, cubicles, security station, studio, chip archive, Orduffer's and Dynamo's offices; Knight Errant's shadow site next door",
        "description": (
            "'In Xanadu did Kubla Khan a stately pleasure-dome decree' scrolls on a little display screen "
            "over a door covered in chipping brown paint; otherwise Xanadu looks like drek. It rents half "
            "a building in a little industrial center in Renton's Merideth district (electronic locks "
            "flicker on the doorways; they need them here). Map p.20: Lobby with faint promotional holos "
            "(the Lab Rats pacing, their agent in a lime suit reading Rocker Born, a receptionist with "
            "neon-pink hair in a bun); pastel cubicles where three wageslaves tap at terminals wired "
            "straight into I/OP-1; Security Station lit blue by six monitors, guards in gray armor "
            "smoking under a Naked Steele holo; a soundproofed Studio behind plate glass with smoke "
            "nozzles and an ivory console (10,000 nuyen of portable electronics); Archives of steel "
            "cabinets and rubber trays of chips (15,000 nuyen before the fence, Angel's copies but not the "
            "originals); Mike Orduffer's Marketing Office with a hulking chrome terminal; and Dynamo's "
            "corner 'Office of the Director' -- thick carpet, molded-plastic desk, automatic soykaf maker, "
            "electronic secretary, telephone censor, a platinum ring in a drawer."
        ),
        "notes": (
            "Ten guards and two captains fire from cover and hold for Lone Star (2D6 minutes; four "
            "officers in a Chrysler-Nissan Patrol); each guard's PANICBUTTON summons them, the blue "
            "button summons Hermetic Securities' Force 7 fire elemental in one turn. After any disturbance "
            "guards double and Crull sends his hit team, with the camera footage. Bug or spirit-watch the "
            "place for 1D6 hours and Dynamo phones 'Crull-san' to report Flaming Wings sales and his "
            "eighty percent; her comms database gives his home. The platinum ring is Lili's gift to Angel "
            "-- she demands Dynamo's death if she hears of it, and it makes Lone Star listen. Neighboring "
            "complex: polished black doors, visible cameras, bare plaster and dust -- a Knight Errant "
            "shadow operation (see its row). Computer system in the prep doc."
        ),
    },
    {
        "name": "Knight Errant Shadow Site (Merideth)",
        "location_type": "safehouse",
        "district": "Renton, Merideth district (next to Xanadu Studios)",
        "security_level": "Corporate Standard",
        "controlling_org": "Knight Errant Security Services",
        "summary": "Empty, camera-watched half of Xanadu's building: a Knight Errant front being fitted out as a clinic staffed by undercover operatives",
        "description": (
            "Black polished doors that practically scream nuyen and visible security cameras outside, "
            "and inside only bare plaster walls, dusty floors and an unfinished electrical system. The "
            "complex belongs to a shadow operation financed by Knight Errant Security that plans to "
            "convert it into a clinic manned by undercover operatives. A small tag on the wiring "
            "instructs repairmen to bill an LTG; Computer (4) on the telecom databases shows the LTG is "
            "Knight Errant's."
        ),
        "notes": "The cameras transmit intruders' images straight to KE headquarters. If the GM wants the team roughed up, four special agents track the trespassers to find out what they wanted; satisfied the runners are no threat to the site, they ignore them and abandon it. No bearing on the Angel plot -- a loose thread for later.",
    },
    {
        "name": "Lone Star Precinct 249",
        "location_type": "police station",
        "district": "Pinehurst, Everett",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "Lone Star Security",
        "summary": "Seedy little blue-neon cop shop handling the Dark Angel 'suicide'; Lieutenant Dolchev's precinct; fifteen officers and five detectives",
        "description": (
            "A seedy little station with a blue neon sign that looks like every other cop-office: scuffed "
            "floors, gray walls, the constant beep of the telecom keeping rhythm with the whoosh of the "
            "automatic doors, a squad car cruising past now and then. Police Station archetype (Sprawl "
            "Sites p.30); fifteen officers and five detectives in the building, all in armor jackets with "
            "Ares Predators and FN-HAR assault rifles to hand. Lone Star's famed indifference and "
            "corruption hits like a wall at the door."
        ),
        "notes": (
            "The duty officer hands anyone with evidence or questions to Lieutenant Dolchev. 'Investigations "
            "take time, chummer.' The public datanet version: two bodyboys, a burnt corpse identified by "
            "forensics with signs of heavy BTL use, suicide by self-inflicted burns. Presenting evidence "
            "against Dynamo (the ring) reaches Edward Crull at once and starts his assassination plan -- the "
            "station makes a good feint. Attacking an officer or kidnapping Dolchev brings Lone Star's "
            "near-infinite resources. Matrix system in the prep doc: files match the official story."
        ),
    },
    {
        "name": "Heaven (BTL den, Lowell)",
        "location_type": "btl den",
        "district": "Lowell, Everett",
        "security_level": "No Security / Barrens",
        "controlling_org": "Golden Gators",
        "summary": "Half-collapsed former public health clinic, Seattle's most famous BTL den, where Dark Angel officially died; Gators, chipheads, Angel-clone culties, yakuza spies, Hack and Slash",
        "description": (
            "A lot in Lowell, Everett, that makes most Toxic Zones look like picnic spots. Once a public "
            "health clinic, now half caved in, rubble in the street, jagged plasteel spars, a fire "
            "roaring in a dumpster and graffiti on every standing wall; basements underneath. Everyone "
            "in Seattle has seen the newsvids. Chipheads as pale as zombies creep through the dark "
            "interior; Golden Gators sell chips at the doors and watch for cops. Since Angel's death a "
            "new clientele: girls with rainbow mohawks dancing to the new record, pilgrims from miles "
            "around, a cluster of 'culties' surgically altered into eerie clones of the dead singer, a "
            "TectonicRock cameraman with a palm-sized lens. Map p.27 places each group."
        ),
        "notes": (
            "Three rules: the Gators attack any disturbance (and warn off nervous, nosy or out-of-place "
            "runners first); two yakuza spies among the culties (cyberears, dreadlocks in many colors) "
            "listen to anyone asking about Angel and radio Crull, who sends his killers; Hack and Slash "
            "slip away the moment anyone asks about the night of the death. Bystanders: Etiquette "
            "(Street) 4, 2+ successes -- 'talk to Hack and Slash' (the trolls); otherwise obscenities and "
            "the Gators' invitation to leave. The Japanese punker who gave the band the forged chip is "
            "here with yakuza enforcers (Perception 4 from Bryan's description; Mafia Soldier / Gang Member "
            "stats; knows only that a yak higher-up who works for Crull at MCT handed it to him). Lure "
            "the trolls away with a corpse deal; violence here 'deserves a horror show', and Lone Star "
            "breaks up an extermination."
        ),
    },
    {
        "name": "Mindwarp",
        "location_type": "nightclub",
        "district": "Downtown",
        "security_level": "Patrolled / Commercial",
        "controlling_org": "Sword Water Clan",
        "summary": "Six-vidscreen glitz palace and Shiro Usaka's headquarters: a members-only loft, seven cybered troll bouncers, eight soldiers, three wired killers, the mage Kojika and a Force 6 fire elemental overhead",
        "description": (
            "Downtown's bright lights outside; inside a sea of color, six enormous vidscreens serving as "
            "walls, floor and ceiling, translucent panels vibrating to deafening music with garish waves, "
            "checkerboards, whirlpools and sunbursts. Dancers whirl; other patrons sit limp at the bar, "
            "overwhelmed. An enclosed loft shadows half the floor -- a club within the club for a select "
            "few, reached by an elevator guarded by a well-dressed troll. Upstairs the music is soft "
            "enough to talk over: surgically perfect men and women in stiff angular Tokyo fashion, "
            "beetle-browed Japanese men in the corners, rice-paper alcoves, and on a dais a small couch "
            "where a balding Japanese man in his late thirties reclines with two women under his arms and "
            "two trolls in dark suits with hoglegs on web slings. Map pp.32-33: lobby with coat check and "
            "magnetic anomaly scanners (guns are checked; 3D6 vs Concealability to smuggle one), the "
            "crystalline bar (Fenswick tending, a skagman in white synth-leather and rhinestones selling "
            "BTL at 50 a chip), stage of rose plastic, dressing rooms, back room where two trolls and "
            "eight yakuza soldiers play trid games, Eric Girard's control station for the screens, "
            "Kojika's bare ivory chamber with its hermetic circle, lavish cherry-and-leather offices, the "
            "special assistants' rooms and Usaka's waterbed under silk curtains of ink-black dragons. The "
            "private rooms' air ducts carry every word to recorders too far away for bug detectors."
        ),
        "notes": (
            "Astral: a Force 6 fire elemental over the club attacks anything projecting, allows "
            "perception. Loft admission: friends and guests of Usaka, members (500 nuyen and three weeks, "
            "or 1,500 to the troll to 'hurry things up'), Charisma 6+, or mention of Crull, Akmura, "
            "Homatsu or Dark Angel -- which also marks you. Better: an appointment through any Fixer or "
            "Yakuza Boss contact, which also looks professional. A fight here meets seven troll guards, "
            "the soldiers, the three special assistants and Kojika using the corridors to cut off escape "
            "-- and an unauthorized attack on Shiro brings Homatsu's wrath. The offices hold yakuza "
            "records worth 100,000 nuyen (fence value lower, and the theft gets avenged). Usaka's "
            "judgment of the team: Etiquette (Street/Japanese/Yakuza) TN 6 with modifiers (see his row). "
            "Captives are interrogated by Kojika and sent to Akmura as goodwill presents."
        ),
    },
    {
        "name": "Marian Parks",
        "location_type": "private estate / compound",
        "district": "Phantom Lake (Bellevue side of Lake Sammamish; skyline view east to downtown)",
        "security_level": "Corporate High Security",
        "controlling_org": "Sword Water Clan",
        "summary": "Homatsu Jinjiro's feudal-Japanese estate behind a nine-foot hedge: tea under a weeping willow, five adept bodyguards, the ninja Chigo Akwe, four Force 6 fire elementals",
        "description": (
            "Country living at its finest: a stainless-steel driveway gate, Phantom Lake to the north, "
            "the downtown skyline to the east, and a black iron fence hidden in the nine-foot hedge. "
            "Inside, low tile-roofed buildings like a village in feudal Japan among curtains of tapered "
            "evergreens, a sleek black limousine in a white modern garage with three satellite dishes, "
            "a tennis court, little battery-powered cameras in the trees (no Matrix link), ten servants. "
            "Astrally the steel and prefab fade and the estate is a Japanese landscape garden of "
            "incredible skill, stones and trees arranged to make vast space of a small area, with three "
            "ruddy peasants in broad hats wandering the paths carrying hoes made of fire. Guests are met "
            "at the gate by Homatsu himself with a bow, surrender weapons and shoes, and take tea from a "
            "priceless porcelain set on a straw tatami in a courtyard shaded by an enormous weeping "
            "willow. Map p.38."
        ),
        "notes": (
            "Any Fixer or Yakuza Boss contact can arrange the meet. Five minutes of small talk, then "
            "business; raise Akmura and he listens without a word. Ask permission and he grants it on one "
            "condition: a single clean hit, no street war; he hands over deck plans of the Shio-Zuchi and "
            "warns of the Oni-do. Five bodyguards (p.39) and Chigo Akwe hide behind the screens; three "
            "Force 6 fire elementals guard the astral and a fourth manifests against spellcasters (p.38 "
            "block: B11 Q12 S8, Init 21+1D6, 10M ranged to 20 m); if routed they extract the oyabun in a "
            "Eurocar Westwind 2000 armored to Level 8. Attacking Homatsu is a death sentence for the "
            "rest of the campaign. Unsanctioned killers of Akmura may instead get a terrifying 'warning' "
            "and a summons here; plead well and he forgives, halts Usaka and may hire the team."
        ),
    },
    {
        "name": "Mitsuhama Residential Facility (Maple Valley)",
        "location_type": "residential community",
        "district": "Renton, Maple Valley district",
        "security_level": "Corporate Standard",
        "controlling_org": "Mitsuhama Computer Technologies",
        "summary": "Edward Crull's modular MCT company house with a fake rock garden: Rating 8 maglocks, ultrasonics, an automated carport gun, five killers in the guest house, Sarah Crull bored in the trid room",
        "description": (
            "A Mitsuhama Modular Residential Facility, about as homey as it sounds: dull blue plaswood "
            "walls, a sloped roof with the MCT logo, and a small Japanese rock garden of fake rocks in "
            "the patch the brochures call a yard. Map p.42: foyer of plastic furniture and austere "
            "black-and-white corporate art; Crull's dim office behind a Rating 8 maglock (teak desk on "
            "bare slate, ivory terminal not on the Matrix, a hermetic circle); bathroom; kitchenette; "
            "master bedroom (gray foam mattress, steel cabinet, a small framed mountain scene and a "
            "non-magical Haida mask that is Sarah's; Rating 8 maglock); an entertainment center crammed "
            "with simsense units and trideo where Sarah sits on the carpet nibbling stuffers; a sunken "
            "carport with a Toyota Elite and two Ford Americars; and the cluttered guest house of "
            "clothes on chairs and pizza boxes where the hired killers live. Adjoining apartments hold "
            "the 'junior magicians and assistants' MCT lets him keep -- his bodyguards."
        ),
        "notes": (
            "Ultrasonic system on every door and window (Electronics 6); Rating 8 maglocks; the alarm "
            "calls Lone Star (four officers in 1D6 minutes; Renton police are better trained and "
            "corp-friendly, p.41) and flashes silent lights in the guest house so the guards arrive in "
            "seconds. Carport door Rating 6 maglock: Electronics (8), fail twice and an automated SMG "
            "fires explosive slugs (skill 6, 10S) at whoever stands in front. Office computer: Computer "
            "(6) shows almost a third of Crull's income going to a mysterious Fuji bank account; tax "
            "records Computer (6) or a Virtual Realities quick run TN 6, 1 success = a Seattle owner with "
            "illegal concealment, 2+ = Kat Akmura. Prowling: roll 1D6 every five minutes, 1 Sarah walks "
            "in, 2-3 a samurai. Crull is home evenings (office or bedroom), gone 8 a.m. to 9 p.m. in the "
            "Elite (Rating 7 armor) with three punks, scanning astrally for ambushes. Losers may be kept "
            "alive for interrogation and sale in the Orient as slaves; Sarah may let them go."
        ),
    },
    {
        "name": "Mitsuhama Office Complex (68th Avenue)",
        "location_type": "corporate headquarters",
        "district": "Downtown, 68th Avenue",
        "security_level": "Corporate High Security",
        "controlling_org": "Mitsuhama Computer Technologies",
        "summary": "The black downtown Mitsuhama tower where Edward Crull works a tenth-floor office; ID-card entry, five guards a door, special response teams of senior technicians and security mages",
        "description": (
            "The black towers of Seattle rise around it, windows flickering as the sararimen slave for "
            "their masters, guards in bulky armor scuffing plasteel boots around the Mitsuhama building. "
            "No one enters without a valid corporate identity card. Five security guards (navy armored "
            "jackets, red MCT helmets, SCK Model 100s; 'brawny gaijin fighting men') watch each external "
            "door; a special response team of four Japanese senior technicians (loose black trousers, "
            "ivory helmets, Wired 1, Firearms 7) and two security mages (Chaos, Mana Bolt, Power Bolt, "
            "Sleep, Urban Renewal; two Force 4 fire elementals each and a Force 1 air elemental "
            "sustaining Personal Combat Sense) arrives in 1D6 turns, with three more teams and thirty "
            "guards in the building (blocks p.46). Crull's extensive office is on the tenth floor "
            "(Junior Executive Office, Sprawl Sites p.20)."
        ),
        "notes": (
            "Office workers (Etiquette (Corporate) 5) know Crull owes his career to unwholesome sources and "
            "that his brother's indiscretions nearly ruined him. Among his software: a chip labeled "
            "BlackBook Plus, an electronic datebook with Kat Akmura's phone number and the name and "
            "location of her ship. 'Never allow an easy attack on the Mitsuhama offices' -- the most a "
            "brazen team deserves is a slim chance to escape. NOTE: the guards here 'do not hesitate to "
            "surrender or run away', softer than the campaign's zero-zone canon for MCT; treat this as an "
            "ordinary office tower rather than a research facility."
        ),
    },
    {
        "name": "Shio-Zuchi (Kat Akmura's yacht)",
        "location_type": "yacht / floating headquarters",
        "district": "Puget Sound, anchored well outside the harbor",
        "security_level": "Zero Zone -- Lethal Response",
        "controlling_org": "Sword Water Clan",
        "summary": "Akmura's black needle-nosed racing yacht and floating HQ: warded hull, four MG gunports, Oni-do adepts, two mages, a torpedo shark, a minisub and a scuttling charge; Dark Angel chained in her cabin",
        "description": (
            "An enormous vessel with the needle nose and slim body of a racing craft, more aircraft than "
            "boat, black streamlined hull lapped by the waves far outside the harbor for privacy. "
            "Astrally the hull is a ward (Grimoire II p.92, renewed by Mushui and Kachu) ringed by a "
            "constellation of glimmering spirits. Design 'based on the principles of Japanese art', no "
            "wasted features. Map p.54: a dark convex deck with four button-launched life rafts; four "
            "sunken gunports with pivot-mounted medium machine guns (1,000-round belts, half recoil, "
            "11S; Barrier 4, gunners visible to spells); a black sausage-shaped bridge blister with "
            "mirrored wraparound glass (two crew; Boat (4) to steer, Electronics (8) to reprogram the "
            "autopilot); an observation tower with its own gunport; the Oni-do guard post, a barren "
            "cylinder of bunks and weapon racks with hidden passages to bridge and gunports; galley (a "
            "month's food), Japanese-style bathroom, quadruple-bunk crew compartment, an infirmary with "
            "a ceiling-track surgical theater, an engine room (Boat B/R (8) overrides the bridge), and a "
            "hold of food, medicine and munitions with a floor hatch to the minisub and scuttling "
            "charges (Demolitions (6)). Akmura's uncluttered suite: waterbed, multi-entertainment "
            "system, her one office terminal, Kachu's room, composite-armored furniture (Barrier 6), and "
            "Dark Angel chained in the living room beside a tank of sapphire-blue fish, made to sing. "
            "Vehicle: Handling 4, Speed 30/60, Body 10, Armor 2, Signature 4, Pilot 4."
        ),
        "notes": (
            "Defenses: Kachu's Detect Enemies locked on Akmura (60 m) and six watchers in the water "
            "(alert at 1,000 m, reported to the tower); a crew member with a megaphone -- 'Seafarers! This "
            "is vessel Shio-Zuchi. Too close, please.' -- then alert, then fire; a plausible story or "
            "Etiquette (Japanese/Yakuza) 6 gets a party aboard under escort of the three Area E Oni-do. "
            "Posts: one troll and Mushui in the tower (physical and astral watch), three trolls at the "
            "guard post (firing positions in 1D6-2 actions, gunports against boats, melee if boarded), "
            "Kachu with Akmura (1D6 actions to react; may turn them both invisible). Torpedo shark under "
            "the keel (B7 Q5x4 S6, 8S3, kept home by hull pheromones). Fifteen sailors and servants "
            "(one a surgeon, Biotech 8) withdraw at the first wound. Akmura runs when four of six Oni-do "
            "fall: the minisub (Handling 4, Speed 10/30, Body 2, Armor 3, Signature 8) leaves the hold, "
            "the ship lists, and a 5 kg Compound 12 charge tears the bottom out -- damage only in the "
            "hold; she sinks in 4D6 minutes; Akmura makes no effort to kill or take Angel. Play it like a "
            "Bond film; the GM may rule the Oni-do will not fire machine guns in public waters. Matrix "
            "system in the prep doc. The astral description sees the trees of Council Island -- a "
            "Lake Washington landmark -- from a Puget Sound anchorage; pick one water."
        ),
    },
    {
        "name": "The Whistler",
        "location_type": "nightclub",
        "district": "The club strip (district not given)",
        "security_level": "Low Security",
        "summary": "Squalid club on the strip where Dark Angel played his last gig for 1,000 nuyen before the black van took him in the alley; owner Monarch",
        "description": (
            "A club on the strip packed with elves, streetmages, scuzboys and go-girls, fluorescent "
            "mohawks and flashing earrings; dreamqueens and androgynous fanboys line the backstage "
            "hallway. The back room is small and squalid, bare wires and stained plascrete, where the "
            "owner Monarch pays the acts by credstick from her payroll computer. Behind it a shadowy, "
            "graffiti-covered alley of litter and loose gravel lit by distant streetlights, thirty meters "
            "to the nearest turn."
        ),
        "notes": "Prologue only (pp.4-5): Angel's balance went from 9.34 to 1,009.34 nuyen; a dull black van with bulging smoked windows made two passes of the strip; an Oriental troll with an iron bar and enhanced reflexes dropped him with three blows and dragged him to the van. The chipheads and party-girls who usually work the alley were nowhere in sight that night -- somebody cleared it.",
    },
    {
        "name": "Infinity Music",
        "location_type": "shop",
        "district": "Downtown (a 'major Seattle record emporium')",
        "security_level": "Patrolled / Commercial",
        "summary": "Major Seattle record store; owner Nigel Spector is the press's go-to quote on the Dark Angel phenomenon; likely site of Angel's comeback appearance",
        "description": "A major Seattle record emporium owned by Nigel Spector, quoted in the September news on the waning Dark Angel boom: 'These trends only last so long. Even death can't make you immortal.' In the success ending Angel announces Earth Dawn 'at a downtown record store'.",
        "notes": "Dark Angel: news-handout texture; a plausible face for the music-industry legwork (Club Habitue / Media Producer tables).",
    },
]

NPCS = [
    {
        "name": "Dark Angel (Jim Crull)",
        "role": "Elven street-rocker legend who refused to record, faked dead by the yakuza and chained singing on Akmura's yacht; Edward Crull's younger brother",
        "archetype": "Rocker",
        "title": "\"Dark Angel\" -- street musician; born Jim Crull of a Mitsuhama shaikujin family",
        "race": "Elf",
        "gender": "Male",
        "connection": 3,
        "description": (
            "Tall, thin and gaunt with long black hair, handsome features that captivity has made almost "
            "spectral, dark hair, wide-set gray eyes and a cleft chin (the features Crull ordered for the "
            "corpse), a rich sonorous voice that rises slightly when he sings, a Stratocaster and "
            "synthleather on stage. Before: a rock 'n' roll rebel of fierce idealism and fiercer contempt "
            "for the criminal, racist yakuza, who sang a bit more truth than Akmura liked to hear. After: "
            "quiet, pensive, properly grateful, aged by his time as her 'guest', his spiritual awareness "
            "deepened. Always wore the platinum ring Lili gave him."
        ),
        "background": (
            "Born the elf in a family of human shaikujin, the youngest, monopolizing his parents' "
            "attention and infuriating his brother Edward; nobody could deny his musical talent. When "
            "Edward's promotion required the household to pledge fealty to Kat Akmura in 2043, Jim "
            "skipped the ceremony and hit the street, guitar in hand. Booking himself as Dark Angel he "
            "became a legend in Seattle's cheap clubs, refusing the yakuza-tainted recording industry -- "
            "partly principle, partly fear that wealth would make him vulnerable to Akmura, partly fear "
            "of the public eye. His music revives lost elven ballads he hears in dreams and believes are "
            "racial memory; magicians, elves, Amerindians and haters of soulless cyber culture love it, "
            "and some call him a new kind of adept, a true bard. He met the talismonger Lili Ice at a gig "
            "and they took a squat together. Akmura waited until he had something to lose."
        ),
        "notes": (
            "Stats p.67: B2 Q7 S2 C8 I4 W4, Ess 6, Magic 6, Reaction 5, Init 5+1D6, Threat 3/4; Etiquette "
            "(Street) 4, Firearms 2, Unarmed 2; Elven History 2, Instrumental Music 6, Singing 6. His talent "
            "borders on the supernatural (no combat use); he never uses synthesized sound and shows a "
            "magician's aura astrally. Held in Akmura's cabin, commanded to sing for her amusement and for "
            "new recordings (SM-2 holds unreleased tapes); Akmura's file: 'The bird sings quite prettily in "
            "my cage.' Rescued, he rewards his rescuers even if Lili is dead, issues a bland statement, "
            "re-releases Flaming Wings, records Earth Dawn months later, becomes a multimillionaire who "
            "gives most of it away to old pals, down-and-outers and elven culture, marries Lili in a tense "
            "reunion -- an invaluable patron and music-industry source. Epilogue: after press reports of "
            "'Earth Dawn: The Scourge' a fire destroys his home and studio and he and Lili vanish; a lone "
            "witness saw three elves. Legwork TN 4 table p.60 (5 successes: a suit has seen him giving "
            "private concerts for some big wheel)."
        ),
        "contact_skills": ["Seattle street-music and club scene", "Elven ballads and elven cultural circles"],
    },
    {
        "name": "Lili Ice",
        "role": "'Icelady' -- savage little club talismonger, Dark Angel's lover and Mr. Johnson; wants the songs and Dynamo dead; 100,000 nuyen from the profits",
        "archetype": "Talismonger",
        "title": "\"Icelady\", small-time talismonger working the clubs",
        "race": "Human",
        "gender": "Female",
        "connection": 2,
        "description": (
            "A savage-looking little woman with a tangle of black hair and dark, flashing eyes, a sharp "
            "angry voice and a presence that shouts danger. Practical to the bone -- 'If Angel's songs "
            "belong to anyone, they belong to me' -- with a jealous streak and a vindictive temper that "
            "current events have brought right out; sarcasm is the only way she knows to ask for help. "
            "'Can't you people slot and run?' Behaves sensibly in real danger."
        ),
        "background": (
            "A small-time talismonger who works the clubs for biz; she met Angel at one of his gigs and "
            "stuck with him, paying his rent 'like a fraggin' slave' and telling him to sign a contract "
            "and make himself a success. Believes he geeked himself in a BTL joint and was unfaithful with "
            "the party-girl Dynamo, recording for her what he never would for anyone; blames Dynamo for "
            "everything and has no idea Akmura exists. Lives in Pinehurst, Everett; 'kinda knows' Julie "
            "Wallace and had just booked Angel into Club Chiaroscuro."
        ),
        "notes": (
            "Stats p.10: B2 Q3 S3 C2 I3 W4, Ess 6, Magic 6, Reaction 3, Init 3+1D6, Threat 2/3; Enchanting 4, "
            "Etiquette (Street) 4, Magic Theory 8, Negotiation 6, Sorcery 4; Evaluate Magical Goods 6, "
            "Metalworking 4, Woodworking 4; armor jacket, Browning Max-Power, credstick 30,000 nuyen. Pays "
            "1,000 per runner in advance, 1,500 with bargaining (Negotiation vs her Willpower, 5 percent a "
            "success), 100,000 promised from the record; up to 1,000 more each to handle the band; the "
            "30,000 also covers any security bought for her flat. Akmura keeps her alive to savor Angel's "
            "humiliation until she becomes trouble; the band beats her up on day 3; Sheera's call names a "
            "Global Trust account she has never heard of. Killing Angel infuriates her and soils the "
            "team's reputation; betray her and she hires another team to punish the traitors. Ending: "
            "marries Angel, invests his profits, never fully understands him again; vanishes with him "
            "in the epilogue fire."
        ),
        "contact_skills": ["Talismonger stock: any common fetish, exotic gear in 24 hours", "Club and rocker gossip"],
    },
    {
        "name": "Kat Akmura",
        "role": "Diminutive yakuza oyabun who waited eleven years to destroy Dark Angel; runs her Seattle empire from the yacht Shio-Zuchi; the villainess or a recurring patron",
        "archetype": "Crime Boss",
        "title": "Oyabun, Sword Water clan (Seattle operations aboard the Shio-Zuchi)",
        "race": "Human",
        "gender": "Female",
        "nationality": "Japanese",
        "organization": "Sword Water Clan",
        "connection": 5,
        "description": (
            "A plain little woman with her hair in two black braids, eyes that glitter like a hawk's and "
            "features frozen in a permanent frown, in casual Western clothing worn with an arrogant "
            "disregard for fashion (the prologue shows her lean and sleek-muscled in tight dark clothes, "
            "unbuttoning her blouse to show the dragons, phoenixes, turtles and apes tattooed across her "
            "golden skin: 'I am yakuza. I am oyabun'). Never fails to punish those who offend her and "
            "may wait decades for the perfect revenge; keeps her victims alive to gloat. An icy temper; "
            "'You insulted me, Angel. I never forget that.'"
        ),
        "background": (
            "Rose fast by yakuza standards, resorting to any tactic she could get away with while staying "
            "technically inside the syndicate's codes; said to have stolen Seattle out from under two or "
            "three big oyabun in Japan, which displeased the conservatives who would like her operations. "
            "Fingers in music, body-dumping and office politics at Mitsuhama. In 2043 she demanded the "
            "household rite of fealty from Edward Crull; his brother's refusal was the insult. She let "
            "Angel build a reputation and fall in love, then took it all: the alley, the burned squatter, "
            "the buried case, the forced recordings, the will to Dynamo, the forged chip to turn his band "
            "on his lover. The Angel affair is a footnote in her ambitions; his defiance, not the nuyen, "
            "moved her."
        ),
        "notes": (
            "Stats p.64: B5 Q6 S4 C3 I6 W6, Ess 2, Reaction 6(10), Init 10+3D6, Threat 3/4; Etiquette "
            "(Corporate) 6 / (Street) 5 / (Yakuza) 6, Firearms 6, Leadership 5, Negotiation 6, Stealth 5, "
            "Unarmed 4; datajack, cybereyes (flare, thermographic), 10 Mp headware, smartlink, Wired "
            "Reflexes 2; armor clothing, SCK Model 100 (gas vent III, smartlink). Kachu keeps Detect "
            "Enemies locked on her. Fights from behind Barrier 6 furniture; flees by minisub when four of "
            "six Oni-do are down and scuttles the ship. Would trade Angel for a more valuable prize -- "
            "influence, information, most likely services -- and has more than enough jobs for enterprising "
            "runners; 'those who can work under her icy temper can expect ample pay and extensive "
            "support.' Legwork TN 4 p.62. Her computer's Angel file: 'Neutralized. Presumed dead -- "
            "operation clean.' Killed without Homatsu's or Usaka's sanction, the whole clan avenges her."
        ),
    },
    {
        "name": "Edward Crull",
        "role": "Dark Angel's elder brother -- Mitsuhama thaumaturgical analyst and yakuza agent who planned the kidnapping and sends the first hit team",
        "archetype": "Corporate Mage",
        "title": "Thaumaturgical analyst, Mitsuhama Computer Technologies (Thaumaturgical Department); Akmura's man",
        "race": "Human",
        "gender": "Male",
        "organization": "Mitsuhama Computer Technologies",
        "connection": 3,
        "description": (
            "The ultimate corporate suit: gray suit and dark tie that have become part of him, a life "
            "lived by office memos and quarterly reports, self-worth measured in salary. Ambitious, "
            "craving advancement, willing to do anything for it. Flees at the first sign of danger; tries "
            "to destroy anyone who Mind Probes him."
        ),
        "background": (
            "Born in the Mitsuhama corporate complex; hated having a metahuman as a younger brother and "
            "found Angel's dreamy ideals frivolous. Discovering his aptitude for magic he joined MCT's "
            "Thaumaturgical Department, found promotion slow and competition fierce, and in 2043 sought "
            "Kat Akmura's blessing; her rite of fealty pledged his whole household and Jim refused it, "
            "blocking the promotion. He wanted to kill his brother; instead he gladly planned and executed "
            "the kidnapping, paid Hack and Slash for a matching corpse, had a Lone Star executive order "
            "the cover-up, and takes eighty percent of Xanadu's Flaming Wings money -- a third of his own "
            "income goes back to Akmura's Fuji account. The yakuza bought him a Haida wife, Sarah. Angel's "
            "'indiscretions' nearly ruined his career."
        ),
        "notes": (
            "Stats p.66: B2 Q5 S1 C5 I5 W5, Ess 6, Magic 6(9), Reaction 5, Init 5+1D6, Threat 3(6 "
            "sorcery)/4; Conjuring 5, Etiquette (Corporate) 6, Magic Theory 6, Sorcery (Spellcasting) 7; "
            "armor clothing, fetishes, Power Focus 3, Walther Palm Pistol. Spells: Stunblast 4, Stun Bolt "
            "4, Chaos 4, Chaotic World 5, Analyze Device 5, Combat Senses 2, Mind Probe 3, Barrier 4, Magic "
            "Fingers 4, Personal Physical Barrier 5. Five Force 5 elementals (two earth, one air, two "
            "water) sustain Combat Sense, Chaotic World and Barrier. Force 4 watchers (potbellied "
            "luminescent imps) hunt the team; finds an average team in a day. Hit team: three punks (AK-97, "
            "Predator, sword, Wired-free but Threat 3/3) and the samurai Eagle and Sal, refilled from the "
            "Hot Papas; ambush = rooftop 'snipers' shoot a businessman while the samurai play Lone Star "
            "and grapple the runners (p.45). Never at the ambush himself. His BlackBook Plus chip holds "
            "Akmura's number and the ship's name and location. If Angel dies the rights pass to him as "
            "next of kin. Legwork p.61 (only MCT/yakuza contacts know him)."
        ),
    },
    {
        "name": "Sarah Crull",
        "role": "Edward Crull's trafficked Haida wife -- bored, ambitious, spying on him; knows nearly the whole Angel story and may become a contact or a runner",
        "archetype": "Corporate Wife",
        "title": "Wife of Edward Crull; born Sarah Cold-Stream-Water of the Haida (Tsimshian)",
        "race": "Human",
        "gender": "Female",
        "nationality": "Haida (Tsimshian Nation)",
        "connection": 2,
        "description": (
            "Wide dark eyes, bronze skin, lustrous oiled hair and few other cosmetics; striking enough "
            "to impress Crull's colleagues. An active intellect, a powerful imagination, considerable "
            "ambition and a keen sense of adventure, all going to waste on stuffers and trideo on the "
            "carpet of the entertainment room. Lonely, restless, unappreciated, bored. Courteous to all "
            "visitors, and one call from the guards."
        ),
        "background": (
            "Grew up among the oppressed Haida in Tsimshian with no assets but her looks, fell in with the "
            "tribe's less savory members, proved far smarter than her pimps and charmed her way out. The "
            "yakuza brought her to Seattle and sold her to Edward Crull, who wanted a wife with no "
            "corporate or national ties and nowhere else to go -- white slavery being 'only technically "
            "illegal'. She neither loves nor respects him. Crull tells her nothing; she delights in spying "
            "and knows almost the entire Angel affair, though not where Akmura's stronghold is."
        ),
        "notes": (
            "Stats p.42: B3 Q5 S5 C6 I5 W6, Ess 6, Reaction 5, Init 5+1D6, Threat 2/3; Armed Combat 3, "
            "Athletics 6, Biotech 3, Etiquette (Street) 3, Firearms 6, Stealth 6; Ares Predator, armor "
            "clothing. Lets in unarmed callers with a plausible reason; talks for the prospect of an "
            "affair, a hefty credstick or the thrill of a run -- Charisma (5): 1 success she takes a "
            "5,000-nuyen bribe, 2+ no bribe needed; the walls muffle whispers but the guards notice long "
            "talks. Helps ambush or question her husband only if the team is capable, dashing and can "
            "show her money or power. Can release captured runners; can help implicate Crull if Angel "
            "dies; may leave him and find her own place -- a useful contact or companion on future runs, "
            "or most valuable left in place at Mitsuhama."
        ),
        "contact_skills": ["Edward Crull's secrets and MCT household gossip", "Haida flats of Tsimshian (the hard way out)"],
    },
    {
        "name": "Dynamo Blue",
        "role": "Tough, racy small-time record promoter who 'owns' Dark Angel's music; Akmura's pawn, not the killer; a future music-industry contact",
        "archetype": "Media Producer",
        "title": "Owner and Director, Xanadu Studios",
        "race": "Human",
        "gender": "Female",
        "organization": "Xanadu Studios",
        "connection": 3,
        "description": (
            "Tough and shrewd, with a racy reputation from an aggressiveness that keeps landing her in "
            "turbulent love affairs -- 'the chica with the highest body count in the biz, love 'em and "
            "dump 'em, and if they hang around, pound the drek out of 'em'. Carries a respectable weapon, "
            "makes the occasional shadowrun, fears the yakuza more than any runner, and lives on "
            "Nuke-&-Serve takeout because she never sees the money."
        ),
        "background": (
            "Runs one of Seattle's minor studios, sometimes downright charitably -- a start for young "
            "bands, records too radical for the majors -- and sometimes nastier, because small-time rock "
            "'n' roll overlaps with big-time crime and she has no choice but to work with the yakuza. She "
            "played no part in planning the Angel affair until Edward Crull ordered her to release "
            "Flaming Wings, an order she happily carried out; she pays Crull-san eighty percent and can "
            "guess Angel is alive because her contacts act as if they have a bottomless supply of him."
        ),
        "notes": (
            "Stats p.65: B5 Q6 S4 C5 I4 W6, Ess 5.6, Reaction 5, Init 5+1D6, Threat 3/3; Etiquette (Media) "
            "5 / (Street) 4, Firearms 6, Stealth 5, Unarmed 4; datajack, synthlink; armor jacket, HK227 "
            "(gas vent III, laser). Cannot be intimidated into signing the rights away; killing her "
            "resolves nothing -- Akmura replaces her. Keeps Angel's platinum ring in a desk drawer. Never "
            "intended malice toward the team or Lili; avoid a battle and she becomes a contact for the "
            "music industry or the street."
        ),
        "contact_skills": ["Small-label music industry and radical bands", "Street-level rock scene"],
    },
    {
        "name": "Shiro Usaka",
        "role": "Shark-smiling young oyabun of the Mindwarp; Akmura's ally of convenience who tests the runners with an ambush and joins whoever wins",
        "archetype": "Crime Boss",
        "title": "Oyabun, Sword Water clan (the Mindwarp)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Sword Water Clan",
        "connection": 5,
        "description": (
            "Nearly bald in his late thirties, reclining on a couch on a dais with two surgically perfect "
            "women under his arms, the smile and personality of a shark. Never misses food, drink or "
            "women. Considerable cunning undone by impatience; 'there is no need for haste' -- he has won "
            "more than once by holding back until a situation unfolded and stepping in on the winning "
            "side."
        ),
        "background": (
            "The weakest of the three oyabun and one of the younger generation, aware that his rapid rise "
            "could vanish in an equally rapid fall. Fought for years to take over Akmura's rackets, lost "
            "repeatedly, realized the feud only kept Homatsu on top, and formed an alliance of "
            "convenience with her -- one precaution among many, with no friendship in it. Julie Wallace "
            "pays him protection and reports to him."
        ),
        "notes": (
            "Stats p.69: B5 Q5 S4 C4 I6 W5, Ess 3.15, Reaction 5(7), Init 7+2D6, Threat 4/3; Etiquette "
            "(Corporate/Street/Yakuza) 5, Firearms 6, Leadership 4, Negotiation 4, Unarmed 4; chipjack, "
            "cybereyes (flare, thermo), datajack, smartlink, Wired Reflexes 1; armor jacket, SCK Model 100. "
            "Judging the team (Etiquette Street/Japanese/Yakuza TN 6; better if Crull is already beaten "
            "or the meet came through a third party, worse for ignorant or blunt questions, fear, bribes, "
            "unseemly behavior, street gossip, insults): 0 successes he tips Akmura (assassins, two more "
            "Oni-do trolls on the ship, his own killers too); 1-2 he says nothing and stages a test ambush "
            "(three soldiers, one special assistant with six trauma patches, Kojika sustaining Combat "
            "Sense and Invisibility on the assistant; live captives for Akmura) -- beat it and he sends "
            "an antique ivory thimble painted with Mount Fuji (20,000 nuyen), blocks any vengeance and "
            "prepares to take Akmura's rackets; 3+ minor help and no vengeance. Kill team: Kojika, three "
            "soldiers, two assistants, a black Ford Americar for ramming (Body 4). Finds the team at "
            "Etiquette (Street) vs TN 5 (8 new hideout, 9 new IDs, 11 new face). A powerful recurring "
            "enemy if crossed. Legwork p.62."
        ),
    },
    {
        "name": "Homatsu Jinjiro",
        "role": "Legendary, serene senior oyabun of the Sword Water clan; disgusted by Akmura's audacity, he licenses one clean hit -- or avenges an unsanctioned one",
        "archetype": "Crime Boss",
        "title": "Senior oyabun, Sword Water clan; master of Marian Parks",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Sword Water Clan",
        "connection": 6,
        "description": (
            "An elderly gentleman in loose cotton clothing who meets guests at his own gate with a bow, "
            "snow-white hair and tiny wrinkles the only signs of age, a low calm voice, an outward "
            "serenity no shock can break. Reveres the old ways; his tranquil estate is a testament to his "
            "power. Few on the street would recognize him."
        ),
        "background": (
            "One of the city's oldest oyabun, managing his territory for more than thirty years through "
            "tact, caution and ancient tradition, wielding vast influence from behind the scenes through "
            "lesser yakuza. The rash, flamboyant younger gangsters disgust him; he fears their excesses "
            "will bring a police crackdown or a ruinous civil war. Turns up in Seattle politics and at "
            "corporate gatherings; few know exactly what he does or why the big shots listen. Kat Akmura "
            "is an upstart with far too much power; he would not mind seeing her embarrassed or "
            "eliminated, though he is far too discreet to say so."
        ),
        "notes": (
            "Stats p.67-68: B4 Q6 S4 C5 I6 W6, Ess 2.9, Reaction 6(10), Init 10+3D6, Threat 3/3; Armed "
            "Combat 6, Etiquette (Corporate) 6 / (Street) 7 / (Yakuza) 9, Leadership 7, Negotiation 8, "
            "Stealth 5, Unarmed 4; datajack, Wired Reflexes 2; armor clothing, monofilament whip. Grants "
            "permission on one condition -- a single clean hit, no street war -- keeps his word, gives the "
            "Shio-Zuchi deck plans and the Oni-do warning. GM back-on-track device: drops the team an "
            "anonymous hint. Unsanctioned killers of Akmura get Chigo Akwe, or a warning and a summons; "
            "plead well and he forgives, orders Usaka off, may hire the team. Attack him and oyabuns "
            "across the world commission hits for the rest of the campaign. Legwork p.62-63: 'He will "
            "soon teach them their place.'"
        ),
    },
    {
        "name": "Kojika",
        "role": "Shiro Usaka's chief henchman -- arrogant, cruel yakuza mage who leads the Mindwarp ambushes under a Mask and interrogates captives",
        "archetype": "Hermetic Mage",
        "title": "Chief henchman and mage to Shiro Usaka",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Sword Water Clan",
        "connection": 3,
        "description": (
            "A plump, pouting face like a jaded dilettante's; arrogant and cruel since his rapid rise, "
            "sharing his master's lack of scruples and appetite for pleasure. Under his Mask he is a "
            "middle-aged woman whose face twists like putty into an adolescent male with a shaved head "
            "and a dragon tattooed on his scalp. Sleeps in a bare ivory chamber with a hermetic circle."
        ),
        "background": "A talent for magic propelled him from the ranks of yakuza soldiers to Usaka's right hand.",
        "notes": (
            "Stats p.68: B4 Q4 S1 C5 I4 W6, Ess 6, Magic 6, Reaction 4, Init 4+1D6, Threat 4/4; Conjuring 6, "
            "Interrogation 4, Sorcery (Spellcasting) 7, Stealth 6; armor jacket. Spells: Stun Bolt 4, "
            "Stunblast 4, Wrecker 4, Chaotic World 4, Invisibility 2, Physical Mask 2, Analyze Device 5, "
            "Combat Sense 2, Mind Probe 3, Armor 3, Clout 2, Influence 2, Levitate Item 2, Cure Disease 2, "
            "Detox Toxin 2, Heal 2. Five Force 5 elementals (two water, two earth, one air): air sustains "
            "Combat Sense, earth Armor, water Invisibility. Tails the team on foot (motor scooter if "
            "needed) with a special assistant, Mask on all of them (Stealth -1 vs Perception); in the "
            "fight goes invisible, takes cover, throws Chaotic World and Wrecker, allocates two elementals "
            "to astral defense and targets the team's magician. Flees to the Mindwarp if losing; Usaka "
            "grudgingly takes him back. Interrogates captives individually before they go to Akmura."
        ),
    },
    {
        "name": "Kachu",
        "role": "Akmura's fat, luxury-addicted advisor-bodyguard mage aboard the Shio-Zuchi; keeps Detect Enemies locked on her; a coward at heart",
        "archetype": "Hermetic Mage",
        "title": "Advisor and bodyguard mage to Kat Akmura (lives in her suite)",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Sword Water Clan",
        "connection": 2,
        "description": (
            "A gray leisure suit, a gem-studded chronometer, gold-rimmed sunglasses and an ample stomach "
            "over his belt -- clownish, until you notice the hermetic trinkets dangling round his tie. "
            "Soft, addicted to gourmet food, swanky clothes and every legal or illegal entertainment a "
            "gangster can command; avoids risking Akmura's life or his own."
        ),
        "background": "The son of a senior yakuza, whose parentage and magical aptitude assured him an easy career in organized crime. Does not live by the discipline of the Oni-do; his watchers report to the tower rather than disturb him.",
        "notes": (
            "Stats p.52 (attribute line garbled in the OCR): Init 6+3D6, Threat 5/2; Conjuring 6, "
            "Enchanting 4, Etiquette (Japanese) 5, Magic Theory 3, Sorcery (Spellcasting) 7; armor jacket, "
            "fetishes, spell lock (Increase Reflexes +2). Spells: Barrier 5, Detect Enemies 4, Heal 2, "
            "Increase Reflexes 4, Invisibility 4, Mana Barrier 4, Mana Bolt 5, Stunblast 5. Two water and "
            "one earth elemental (Force 4, one service each). Detect Enemies locked on Akmura (60 m); six "
            "watchers circling the ship to 1,000 m; renews the hull wards with Mushui. Takes 1D6 actions "
            "to respond to a surprise attack; in a pitched battle stays with Akmura and may make them "
            "both invisible to escape."
        ),
    },
    {
        "name": "Mushui",
        "role": "Small, long-nailed 'artist of combat wizardry' who serves the Oni-do trolls; watches the Shio-Zuchi's tower and sinks boats with spells",
        "archetype": "Combat Mage",
        "title": "Combat mage attached to the Oni-do; lookout on the Shio-Zuchi",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Oni-do",
        "connection": 2,
        "description": "A small man with long fingernails in a simple martial artist's robe who sees himself as an artist of combat wizardry: disabling opponents at long range, sinking boats, levitating heavy weapons out of reach, dropping Chaos over enemy magicians, letting elementals sustain his best spells.",
        "background": "Human, but attached himself to the Oni-do troll warrior society to practice his craft.",
        "notes": (
            "Stats p.52: B4(8) Q4 S1 C5 I6 W6, Ess 6, Magic 6, Reaction 5(13), Init 5+1D6, Threat 3(5)/3; "
            "Athletics 3, Conjuring 6, Etiquette (Japanese) 2, Gunnery 4, Sorcery (Spellcasting) 7, Stealth "
            "3; armor jacket, fetishes, spell locks (Armor 8 successes, Combat Sense 8 successes). Spells: "
            "Armor 4, Chaos 2, Chaotic World 4, Clout 4, Combat Sense 2, Levitate Item 4, Resist Pain "
            "(Serious) 2, Stunblast 3, Wrecker 4. Five Force 3 elementals (two fire, two water, one earth), "
            "one service each. Resist Pain sustained on himself and every Oni-do troll; renews the wards. "
            "Posted in the observation tower with one troll, watching both planes; descends to melee if "
            "everyone boards."
        ),
    },
    {
        "name": "Akimoto",
        "role": "Grim, cowardly Oni-do Rat shaman and initiate who leads Akmura's best hit team from a dumpster, invisible, with a mob-minded gang in front",
        "archetype": "Shaman",
        "title": "Oni-do assassin; Rat shaman, Grade 2 initiate",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Oni-do",
        "connection": 2,
        "description": (
            "A taciturn, grim-faced loner. Astrally a shadowy manlike shape crouched among the auras that "
            "vanishes when looked at -- a human magician masking his initiate status. Has little real "
            "courage: once he takes Physical damage he runs, and he does not hold up well under pain."
        ),
        "background": "Drifted for years, unable to fit Japan's conformist corporate society, until he found the Oni-do; a man without honor, morality or loyalty to anything but the society, he finds the assassin's life to his liking. Uses meditation as a Centering skill.",
        "notes": (
            "Stats p.63: B4 Q5 S1 C3 I5 W6, Ess 6, Magic 8, Reaction 5, Init 5+1D6, Threat 4/4; Conjuring "
            "5, Sorcery (Spellcasting) 7, Firearms 3, Stealth (Urban) 8; armor jacket, Browning Max-Power "
            "(laser), fetishes bearing the Oni-do symbols. Spells: Combat Sense 2, Treat 2, Chaos 2, Chaotic "
            "World 3, Invisibility 5, Barrier 2, Clout 3, Mob Mind 4. Six watchers and a Force 6 city "
            "spirit. Finds the team in 1D6 hours via Akmura's contacts, tails astrally for an hour, "
            "attacks the smallest group: four Mob-Minded Caesar's Scythers charge, Akimoto (Invisibility "
            "8 successes) watches from cover with Magic Pool on spell defense, the city spirit Alienates "
            "the strongest runner and invisible Kure kills him; heals and moves to the next group. Under "
            "interrogation lies three times -- a Scyther ('Scythers rule!'), a fixer named Jackal of the "
            "Fenris Nacht policlub, then a fake breakdown blaming Aztechnology -- and then tells the "
            "truth: Akmura holds Angel on her ship."
        ),
    },
    {
        "name": "Kure",
        "role": "Enormous child-minded troll physical adept of the Oni-do, Akimoto's invisible blade; fights on regardless of odds and never talks",
        "archetype": "Physical Adept",
        "title": "Oni-do assassin; troll physical adept",
        "race": "Troll",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Oni-do",
        "connection": 1,
        "description": (
            "The body of an enormous troll with the mentality of a young child and the gifts of a physical "
            "adept; the Oni-do insignia on the hilt of his katana. Loves and trusts the Oni-do leaders as "
            "parents and will do absolutely anything they ask. Under questioning he never intentionally "
            "reveals anything, but sneers at every wrong guess and shudders at every right one."
        ),
        "background": "Entered puberty as a human in Japanese corporate society; the shock of goblinization ravaged his mind and his parents' attempts at 'treatment' deranged him further. By the time the Oni-do found him he was what he is now.",
        "notes": (
            "Stats p.69: B10(11) Q3 S10 C1 I1 W4, Ess 6, Magic 6, Reaction 2(4), Init 4+2D6, Threat 4/3; "
            "Athletics 2, Armed Combat (Katana) 8, Firearms 4, Gunnery 3, Stealth 6, Unarmed 3; armor "
            "jacket, HK227, katana (13M). Adept powers: Improved Ability Armed Combat 3, Improved Physical "
            "Attributes Body 1, Increased Reflexes 2. Enters the ambush under Akimoto's Invisibility (3 "
            "successes), geeks whoever the city spirit has isolated, fights to the end. Mind Probe at +2 "
            "TN; leading questions and his sneers and shudders confirm suspicions. Knows the ship's "
            "general layout and that Angel is there."
        ),
    },
    {
        "name": "Chigo Akwe",
        "role": "Homatsu's chief ninja -- a Grade 4 initiate adept of the Sword Water clan's silent warriors; the patient, ingenious death sentence for unsanctioned killers of an oyabun",
        "archetype": "Assassin",
        "title": "Chief ninja in Homatsu Jinjiro's service",
        "race": "Human",
        "gender": "Male",
        "nationality": "Japanese",
        "organization": "Sword Water Clan",
        "connection": 3,
        "description": (
            "Every move displays grace and simplicity of action. Unconcerned with the politics or "
            "motivations of the yakuza, he cares only for the mystic beauty of his art. Patient, "
            "ingenious, merciless: poison gas, contact poison in DMSO, sabotage of vital gear, or waiting "
            "until other enemies have jailed his targets and killing them in their cells."
        ),
        "background": "At fourteen he sought enlightenment in ninjutsu; the silent warriors of the Sword Water clan taught him and he gradually attained wisdom as well as great skill. Initiated to Grade 4 by the clan's ninja.",
        "notes": (
            "Stats p.64-65: B6 Q6 S4 C2 I6 W6, Ess 6, Magic 6(10), Reaction 6, Init 6+3D6, Threat 5/4; "
            "Athletics 6, Armed Combat 7, Firearms 4, Stealth 8, Unarmed 7. Adept powers: Improved Ability "
            "Armed Combat 3 / Athletics 2 / Stealth 4, Improved Physical Senses (hearing damper and "
            "amplification, flare compensation, thermographic), Increased Reflexes 2, Pain Resistance 4. "
            "Gear: Ares Squirt with two 10-round DMSO cartridges, an ampule of cyanide (4D3) and one of "
            "Hyper (+1 TN, +4 concentration, 60 minutes; Body (4) shortens), armor jacket, two offensive "
            "grenades, HK227, one monofilament whip ready and one taped to his leg (10S). DMSO: rigid "
            "armor halves, porous armor useless. Waits with the bodyguards behind Homatsu's screens; "
            "attacks 'in all likelihood during a future shadowrun', with two bodyguards if forced to "
            "strike directly. May be told to deliver only a terrifying warning."
        ),
    },
    {
        "name": "Julie Wallace",
        "role": "Cool, scruple-free owner of Club Chiaroscuro; hermetic mage with six watchers and six elementals who sells yakuza gossip and reports to Shiro",
        "archetype": "Club Owner",
        "title": "Owner, Club Chiaroscuro",
        "race": "Human",
        "gender": "Female",
        "connection": 3,
        "description": "A slim woman with her hair in a bun, mirrored shades and a constant expression of indifference, speaking in a low musical tone; a club owner on the rise who has never allowed herself too many scruples and does what she needs to without worrying about ethics.",
        "background": "Made her mark with a successful nightclub; pays protection to Shiro Usaka as the price of doing business and usually keeps what happens in her club to herself -- but updates Shiro on anyone who asks about the local yakuza. Icelady 'kinda knows' her and talked her into booking Angel and 3,000 nuyen of promotion.",
        "notes": (
            "Stats p.13 (attribute line garbled: Body 3, Strength 3, Charisma 3, Intelligence 6, Willpower "
            "4), Init 3(6)+1D6, Threat 3/3; Conjuring 6, Etiquette (Media) 4 / (Street) 4, Magic Theory 3, "
            "Negotiation 4, Sorcery 6; armor clothing, spell lock (Increase Reaction +3), spirit focus "
            "(watchers) 3. Spells: Clout 2, Detox 2, Increase Reaction 5, Invisibility 2, Magic Fingers 2, "
            "Mind Probe 2, Sleep 4, Stun Bolt 4, Trid Spectacle 2. Six Force 3 watchers; six Force 3 "
            "elementals (two fire, two water, one earth, one air) at two services each. Trust: Etiquette "
            "(Street) 6 and a gift of at least 1,000 nuyen buys the yakuza briefing (three oyabuns, the "
            "Akmura-Usaka alliance, Homatsu the traditionalist) and the addresses of the Mindwarp and "
            "Marian Parks. Silence: 2,000 nuyen or two successes. Feels 'pretty fragged' about the "
            "cancelled gig."
        ),
        "contact_skills": ["Seattle yakuza politics (for a price)", "Club bookings and rocker gossip"],
    },
    {
        "name": "The Genies",
        "role": "Club Chiaroscuro's two nine-foot troll bouncers in sequined satin and blue fezzes, Turkish accents and weighted nightsticks",
        "archetype": "Bouncer",
        "title": "Bouncers, Club Chiaroscuro (two trolls)",
        "race": "Troll",
        "gender": "Male",
        "connection": 1,
        "description": "Nine-foot monsters in baggy trousers, tight jackets of sequined black satin and blue fezzes, one at each main door; thick Turkish accents and a historical Near-Eastern style, unusually cultured for this part of town, quick to violence when needed. No more force than necessary on ordinary drunks; weighted nightsticks materialize from their pockets for real trouble.",
        "notes": "Stats p.13: B10 Q2 S8 C2 I2 W3, Ess 6, Reaction 2, Init 2+2D6, Threat 4/3; Armed Combat 6, Etiquette (Street) 3, Unarmed 4; Wired Reflexes 1; armor clothing, club (11M Stun). In a brawl they may hit both sides.",
    },
    {
        "name": "Bryan",
        "role": "Chain-smoking, hard-drinking elf leader of Dark Angel's band and the Fallen Heroes; wants Lili punished and a cut of the record",
        "archetype": "Rocker",
        "title": "Band leader, Dark Angel's band; Fallen Heroes go-ganger",
        "race": "Elf",
        "gender": "Male",
        "nationality": "African-American",
        "organization": "Fallen Heroes",
        "connection": 2,
        "description": "Torn jeans, a heavy leather jacket and a black T-shirt with the Thundering Herd logo; an aquiline nose and glittering eyes hint at his power. A deep voice and swift decisions put him in charge. Smokes constantly and drinks heavily, without pleasure. Drew's brother.",
        "notes": "Stats p.17 (partly garbled): B5 Q6 S5, I6, Init 5+2D6, Threat 2/3; Armed Combat 5, Bike 4, Etiquette (Street) 4, Firearms 4, Projectile 3, Stealth 5, Unarmed 4; Instrumental Music 4, Musical Composition 5, Singing 3; mastoid speakers, thermographic eyes, synthlink, Wired Reflexes 1; armor jacket, Browning Max-Power (explosive rounds, laser), club. With Drew, went to Heaven after the death and took the forged chip from the Japanese punker; can describe him (Perception 4 to find him). 'Not Angel, man, he's made of steel.'",
    },
    {
        "name": "Drew",
        "role": "Baby-faced, dreadlocked elf lead vocalist of Dark Angel's band with a high voice and a cultured British accent; Bryan's brother",
        "archetype": "Rocker",
        "title": "Lead vocalist, Dark Angel's band; Fallen Heroes go-ganger",
        "race": "Elf",
        "gender": "Male",
        "nationality": "African-American",
        "organization": "Fallen Heroes",
        "connection": 2,
        "description": "Dreadlocks swinging round his waist, the innocent expression and ready smile of a baby, round mirrored sunglasses, a naturally high-pitched voice and a cultured British accent; the skill with which he manipulates that voice made him the band's natural lead vocalist.",
        "notes": "Stats p.17: B4 Q6 S6 C6 I5 W4, Ess 5.5, Reaction 5, Init 5+1D6, Threat 2/3; skills as Bryan; Instrumental Music 3, Musical Composition 3, Singing 5; mastoid speakers, thermographic eyes, synthlink; armor jacket, Browning Max-Power (explosive, laser), club (7M Stun).",
    },
    {
        "name": "Sheera Persian",
        "role": "Cold, mirror-shaded hermetic sorcerer-singer of Dark Angel's band who secretly loved him and hates Lili with a passion; phones the threat",
        "archetype": "Rocker",
        "title": "Singer and sorcerer adept, Dark Angel's band",
        "race": "Human",
        "gender": "Female",
        "organization": "Fallen Heroes",
        "connection": 2,
        "description": "A dark-skinned, slow-eyed woman in gleaming mirrored shades with a perpetually cold expression, long black hair sweeping either side of a heart-shaped face. A woman of strong dislikes; hates Icelady mostly because of her own secret obsession with Dark Angel, and would risk anything to punish his killers. A hermetic sorcerer adept.",
        "notes": "Stats p.17: B3 Q6 S5 C6 I5 W6, Ess 6, Reaction 5, Init 5+1D6, Threat 3/3; Armed Combat 5, Bike 4, Etiquette (Street) 4, Magical Theory 4, Sorcery 5 (Spellcasting 7), Stealth 5, Unarmed 4; Instrumental Music 4, Musical Composition 4, Singing 4; armor jacket, Browning Max-Power, club. Spells: Entertainment 5, Fashion 2, Healthy Glow 2, Improved Invisibility 2, Mana Bolt 3, Physical Mask 2, Power Bolt 3, Sleep 2. Hours after the hire she calls Lili: 'Global Trust, account two two three four three. You just watch your magical little back.' Eventually talks the others into roughing Lili up.",
    },
    {
        "name": "Nolan",
        "role": "Barefoot, bearded Irish elf guitarist of Dark Angel's band -- the even-tempered one who liked Angel and keeps an open mind about Lili",
        "archetype": "Rocker",
        "title": "Guitarist, Dark Angel's band",
        "race": "Elf",
        "gender": "Male",
        "nationality": "Irish",
        "organization": "Fallen Heroes",
        "connection": 2,
        "description": "A barefoot Irish elf with a mop of unruly hair, a reddish-blond beard, a perpetual ironic smile and a warm, knowing one; tank top and jeans, usually relaxed against a wall or lamppost playing his guitar. A remarkably even temper makes him the band's stabilizing influence.",
        "notes": "Stats p.18 (attribute line lost in the OCR): Threat 2/3; Armed Combat 5, Bike 4, Etiquette (Street) 4, Firearms 4, Projectile 3, Stealth 5, Unarmed 4; Instrumental Music 5, Musical Composition 4, Singing 4; mastoid speakers, thermographic eyes, synthlink; armor jacket, Browning Max-Power (explosive, laser), club (5M Stun). The band member most likely to talk first.",
    },
    {
        "name": "Lieutenant Dolchev",
        "role": "Crooked but competent Lone Star lieutenant supervising the Dark Angel 'suicide'; sells the cover-up's author for 5,000 nuyen and professionalism",
        "archetype": "Police Officer",
        "title": "Lieutenant, Lone Star Precinct 249 (Pinehurst, Everett); supervisor of the Dark Angel case",
        "race": "Human",
        "gender": "Male",
        "organization": "Lone Star Security",
        "connection": 3,
        "description": "Good at his job -- go-gangs quiet, burglars cautious, chipheads under control, streets as safe as Pinehurst gets -- and an ideal policeman for the 2050s: knows how not to investigate a crime and which bribes to accept, a man of his times who does business with all the real powers in Seattle and respects power and professionalism on the street and off. No special loyalty to the yakuza.",
        "background": "Knows from personal experience what the sprawl does to someone who refuses to play the game. Accepted without question a cover-up ordered by a Lone Star executive: forensics privately identified the burned corpse as a recently murdered squatter, and the corp rumor mill says Edward Crull of Mitsuhama asked for it -- and Crull has yakuza ties.",
        "notes": "Stats p.25: B5 Q5 S4 C5 I4 W5, Ess 4.95, Reaction 5, Init 5+1D6, Threat 3/3; Armed Combat 4, Car 4, Etiquette (Street) 7, Firearms 5, Negotiation 6, Unarmed 4; cybereyes (low-light, camera), radio; Ares Predator (laser), armor jacket, medkit, micro-recorder, plastic restraints, four trauma patches. Deals only with those 'in the know' -- mention the Dynamo-Crull link or the ring; at least 5,000 nuyen to the 'Police Widows Fund', Etiquette (Street) 8 for one success; misjudge the unwritten rules and he arrests the team for bribery. Keeps his Matrix files matching the official story. Kidnapping him is 'harming a Lone Star officer'. May trade information for temporary amnesty after a firefight.",
        "contact_skills": ["Pinehurst precinct files and who ordered what", "Lone Star's unwritten rules"],
    },
    {
        "name": "Lizard Pete",
        "role": "Smug Urban Gator shaman who built the Golden Gators and now waits for the BTL money; drops a garbage-bag city spirit on your head",
        "archetype": "Gang Boss",
        "title": "Leader, Golden Gators; Gator shaman",
        "race": "Human",
        "gender": "Male",
        "organization": "Golden Gators",
        "connection": 2,
        "description": "A perpetually smug expression reinforced by a wide mouth and smooth tanned skin. Worked hard to establish the Gators and set himself up as leader; now he relaxes and waits for the money to flow in, caring little for the business so long as he gets a cut -- but he enjoys their battles.",
        "notes": "Stats p.28: B6 Q4 S1 C4 I4 W6, Ess 6, Magic 6, Reaction 4, Init 4+1D6, Threat 2/3; Conjuring (City Spirits) 7, Etiquette (Street) 4, Leadership 5, Sorcery (Spellcasting) 7, Unarmed 3; armor jacket, Browning Max-Power, sword; totem Gator. Spells: Armor 2, Combat Sense 2, Manablast 5, Mana Bolt 4, Powerball 5, Treat 2. Opens a fight with a Force 5 city spirit that manifests as a trash bag of wet greasy garbage landing on the most dangerous enemy's head (Confusion), then joins in with spells.",
    },
    {
        "name": "Hack and Slash",
        "role": "Timid, good-humored troll bodyboy brothers who built the fake Dark Angel corpse for Crull; BodyBits' 'freelance collection agents' at Heaven",
        "archetype": "Bodyboy",
        "title": "Freelance collection agents, BodyBits Organ Donation Service (two troll brothers)",
        "race": "Troll",
        "gender": "Male",
        "organization": "BodyBits Organ Donation Service",
        "connection": 1,
        "description": "Two Caucasian trolls with light blue eyes and an obvious family resemblance who enjoy their work, take its gruesome side in good humor, avoid anything that might land them in trouble and are actually a little timid -- though they give a good account of themselves in a fight. Linger near Heaven because the firefights and lethal BTL keep the merchandise coming.",
        "notes": "Stats p.30: B10 Q1 S10 C1 I1 W4, Ess 6, Reaction 1, Init 1+1D6, Threat 1/2; Armed Combat (Combat Axe) 8, Biotech 3, Etiquette (Street) 2, Firearms 4, Unarmed 6; AK-97, armor jacket, combat axe, dissection gear, body bags. Edward Crull paid them to disguise a burn victim as Angel and report it -- he asked for a burned male corpse with dark hair, wide-set gray eyes and a cleft chin; they never realized whose features those were. Sneak off when anyone asks about that night; can't be threatened in Heaven (the Gators intervene); lure them out with a believable corpse deal (Negotiation vs Intelligence, opposed). Know Crull has yakuza ties and can point to his Renton house. Their testimony clears Lili with the band.",
    },
    {
        "name": "Mike Orduffer",
        "role": "Xanadu's advertising executive, 20,000 nuyen in debt to Akmura, who reports every irregularity to her and runs at the first sign of trouble",
        "archetype": "Media Producer",
        "title": "Advertising executive, Xanadu Studios",
        "race": "Human",
        "gender": "Male",
        "organization": "Xanadu Studios",
        "connection": 1,
        "description": "Works behind a hulking chrome terminal lit with psychedelic sound-chip album art. Already owes Kat Akmura 20,000 nuyen and will go to almost any length to avoid the hint of further trouble.",
        "notes": "Media Producer contact stats (SRII p.209) if forced to fight. Reports the slightest irregularity in office routine to Akmura -- one of the ways the yakuza learn of the team.",
    },
    {
        "name": "Clifton Perkins",
        "role": "Pasty music agent in a lime suit managing the Lab Rats and several aspiring novastars; cowers behind his chair in a firefight",
        "archetype": "Talent Agent",
        "title": "Music agent (the Lab Rats and other aspiring novastars)",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": "A pasty-skinned corp type in a lime suit reading last week's Rocker Born in Xanadu's lobby, refusing to be impressed by the studio's recent successes. Expertly manages the careers of several aspiring novastars but is uncomfortable around his clients' associates.",
        "notes": "Stats p.23: B2 Q3 S2 C5 I4 W4, Ess 4.8, Reaction 3, Init 3+1D6, Threat 1/1; Computer 3, Etiquette (Corporate) 4 / (Media) 4 / (Street) 2, Negotiation 4; datajack, 100 Mp. Pleads with his clients to stay out of the line of fire.",
        "contact_skills": ["Up-and-coming bands and small-label contracts"],
    },
    {
        "name": "Eric Girard",
        "role": "Thin mustached technician who runs the Mindwarp's six vidscreens from the control station -- and a Fuchi Cyber-4 decker",
        "archetype": "Decker",
        "title": "Vidscreen technician, the Mindwarp",
        "race": "Human",
        "gender": "Male",
        "organization": "Sword Water Clan",
        "connection": 1,
        "description": "A thin, dark-haired fellow with a small mustache at the single terminal that governs every vidscreen in the Mindwarp.",
        "notes": "Stats p.34: B1 Q4 S2 C2 I6 W5, Ess 5.5, Reaction 5, Init 5+1D6 (5+2D6 in the Matrix), Threat 1/2 (3/3 in the Matrix); Computer 6, Electronics 6; datajack, 30 Mp; Fuchi Cyber-4 (MPCP 6, Hardening 3, Active 100, Storage 500, Load 20, I/O 20; persona Bod 5, Evasion 4, Masking 5, Sensors 4; Attack 6; Response Increase 1). Usaka's house decker if the club's system is ever attacked.",
        "computer_skill_enabled": True,
        "computer_skill_rating": 6,
    },
    {
        "name": "Fenswick",
        "role": "Young bartender in a light suit at the Mindwarp's crystalline bar, next to the rhinestoned BTL skagman",
        "archetype": "Bartender",
        "title": "Bartender, the Mindwarp",
        "race": "Human",
        "gender": "Male",
        "organization": "Sword Water Clan",
        "connection": 1,
        "description": "A young man in a light suit tending the glittering slab of crystalline plastic that abuts the dance floor, while a young Japanese skagman in white synth-leather and rhinestones sells BTL at 50 nuyen a chip to well-to-do chipheads (Etiquette (Street) 3 to notice).",
        "notes": "No stats. Knows the loft rules and who goes up.",
    },
    {
        "name": "Eagle and Sal",
        "role": "Edward Crull's man-and-woman samurai team -- beta-chromed grenade ambushers who play Lone Star cops and grapple the runners for the snipers",
        "archetype": "Street Samurai",
        "title": "Hired samurai to Edward Crull (two)",
        "race": "Human",
        "gender": "Mixed",
        "organization": "Mitsuhama Computer Technologies",
        "connection": 1,
        "description": "The same stony faces, the same whipcord-lean builds; ruthless and cynical after long careers on the streets but committed to each other -- they may desert Crull in a losing battle but will always get each other out alive. Hate a straight fight; neutralize enemy mages first; retractable spurs below the right wrist.",
        "notes": "Stats p.43 (partly garbled): Q7 S7 C2 I6 W6, Ess 1.56, Reaction 6(9), Init 9+3D6, Threat 3/4; Firearms (FN HAR) 8, Unarmed (Grapple) 8, (Spurs) 8, Throwing 4, Armed Combat 1; beta-grade cybereyes (thermo, flare, mag 3), Dermal Plating 3, Muscle Replacement 1, Retractable Spur (7M), smartlink, Wired Reflexes 2; AFR-7 flash grenade, three defensive grenades (10S), Ares Predator, FN HAR (APDS, external smartlink, gas vent III), armor jacket; Crull's Increase Cybered Attributes +3 locked on both. Stay at the house by day (the punks go to MCT). Ambush: in Lone Star blue they 'rescue' the team from Crull's rooftop punks ('Just sit tight till the SWAT boys can move in') and grapple magicians until the act fails, then back off and open up with the HARs, dropping flash grenades if they must run.",
    },
    {
        "name": "Sweet Petunia",
        "role": "Tattooed troll leader of the Smash 'n' Grabbers thrill gang -- daggers, dragons and hairy mythological beasts head to toe",
        "archetype": "Gang Boss",
        "title": "Leader, Smash 'n' Grabbers",
        "race": "Troll",
        "gender": "Male",
        "organization": "Smash 'n' Grabbers",
        "connection": 1,
        "description": "A troll who has covered his body with tattoos of bloody daggers, dragons and hairy mythological beasts; leads a gang that lifts cars by hand and runs from real fights.",
        "notes": "Gang block p.44. Six of his trolls take a punk's nuyen to smash Lili's windows; whether Petunia comes himself is the GM's call.",
    },
    {
        "name": "Caesar",
        "role": "Street-samurai leader of Caesar's Scythers, angry that a shaman mind-controlled his gangers; may arrive mid-ambush hunting the invisible pair",
        "archetype": "Gang Boss",
        "title": "Leader, Caesar's Scythers",
        "race": "Human",
        "gender": "Male",
        "organization": "Caesar's Scythers",
        "connection": 1,
        "description": "The gang's leader; Street Samurai archetype (SRII p.62). Knows Akimoto cast a spell over his chummers and is not a happy camper.",
        "notes": "GM bail-out for the Oni-do ambush: he and Cleopatra show up looking for the invisible pair, tipping the team to pinpoint its real enemies and hose them with numbers.",
    },
    {
        "name": "Cleopatra",
        "role": "Caesar's wizlady -- the Scythers' street shaman, who can see what Akimoto did to her gang",
        "archetype": "Street Shaman",
        "title": "Shaman, Caesar's Scythers",
        "race": "Human",
        "gender": "Female",
        "organization": "Caesar's Scythers",
        "connection": 1,
        "description": "Caesar's wizlady; Street Shaman archetype (SRII p.63). Less firepower than the Oni-do assassins but knows enough to look for the invisible pair.",
        "notes": "Arrives with Caesar if the GM needs to bail the runners out of Akimoto's ambush.",
    },
    {
        "name": "Monarch",
        "role": "Overweight, pasty owner of The Whistler who paid Dark Angel his last thousand nuyen minutes before the van took him",
        "archetype": "Club Owner",
        "title": "Owner, The Whistler",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": "The Whistler's overweight, pasty-skinned owner, paying the acts from a payroll computer in a squalid back room of bare wires and stained plascrete. Angel gave her a gallant nod on his way out to the alley.",
        "notes": "Prologue only. The last person to see Angel free, and the club whose alley was suspiciously empty that night -- a witness the book never uses.",
    },
    {
        "name": "Nigel Spector",
        "role": "Owner of Infinity Music, the major Seattle record emporium; the press's quote on the Dark Angel boom",
        "archetype": "Shopkeeper",
        "title": "Owner, Infinity Music",
        "race": "Human",
        "gender": "Male",
        "connection": 2,
        "description": "The record-store owner the Seattle News-Intelligencer rings for a music-business quote: 'These trends only last so long. Even death can't make you immortal.'",
        "notes": "News-handout name (failure ending). No stats.",
        "contact_skills": ["Seattle record retail and what is selling"],
    },
    {
        "name": "Butch Hatchett",
        "role": "Troll leader in the Friends of Trolls 'Trollfriends' movement, quoted on its second recruitment drive",
        "archetype": "Political Activist",
        "title": "Leader, Friends of Trolls (Trollfriends movement)",
        "race": "Troll",
        "gender": "Male",
        "organization": "Friends of Trolls",
        "connection": 2,
        "description": "'I think this group is a really positive thing. Showing one's support for the troll community isn't just a matter of politics. It's a very healthy step for an individual.'",
        "notes": "News-handout name (both endings). No stats.",
    },
    {
        "name": "Dr. Sheila Clinton",
        "role": "Seattle University academic quoted, drily, on her colleague Luke Emerson's death by torpedo-shark feeding frenzy",
        "archetype": "Academic",
        "title": "Parazoologist, Seattle University (colleague of the late Luke Emerson)",
        "race": "Human",
        "gender": "Female",
        "organization": "University of Seattle",
        "connection": 2,
        "description": "'He had said he really wanted to get inside these animals. I guess he got his wish.'",
        "notes": "News-handout name. The handout says 'Seattle University'; the campaign row is University of Seattle. A natural source on torpedo sharks (Portheus velocis) and the pheromone trick that keeps one under the Shio-Zuchi.",
        "contact_skills": ["Paranormal marine fauna (torpedo sharks)"],
    },
]

ORG_UPDATES = {
    "Yakuza (Watada-rengo)": {
        "notes_append": (
            "Dark Angel discrepancy: this book (2054) calls the yakuza of 'this part of the sprawl' the "
            "Sword Water clan (or Society) under senior oyabun Homatsu Jinjiro with the young oyabuns Kat "
            "Akmura and Shiro Usaka beneath him, and never names the Watada-rengo. Earlier canon stands; "
            "treat the Sword Water clan as one clan under or beside the rengo, as with Elven Fire's "
            "Dungeness Crabs. The book's yakuza rules are worth keeping: colorful tattoos always in "
            "concealable places, more with rank; the code of zuni; decades-long vendettas; 'anyone who "
            "harms a yakuza member without the sanction of other members has signed his own death "
            "warrant' -- to hit an oyabun and live, get another oyabun's permission first. Three oyabuns "
            "have their fingers in Mitsuhama. Runners identified by the yakuza lose Karma (-1)."
        ),
        "allies_add": ["Sword Water Clan"],
    },
    "Mitsuhama Computer Technologies": {
        "notes_append": (
            "Dark Angel (2054): thaumaturgical analyst Edward Crull of the Thaumaturgical Department "
            "(hermetic-research division) bought his 2043 promotion track with a household rite of fealty "
            "to yakuza oyabun Kat Akmura; the corp lets him keep 'junior magicians and assistants' as "
            "bodyguards in a Mitsuhama Modular Residential Facility in Renton's Maple Valley district and "
            "gives him a tenth-floor office in the MCT complex on 68th Avenue downtown. Legwork: 'the "
            "three big oyabuns with their fingers in MCT are Shiro Usaka, Homatsu Jinjiro and Kat "
            "Akmura'; the book calls MCT 'a multinational megacorp, very likely run by the yakuza'. The "
            "forged Global Trust chip is 'a rare Mitsuhama format'. Renton police give MCT's corporate "
            "citizens 'the best protection available'. Security blocks p.46: five guards a door (navy "
            "jackets, red MCT helmets, SCK Model 100s, Threat 4/3, will surrender or run), special "
            "response teams of four senior technicians (Wired 1, Firearms 7) and two security mages "
            "(Force 4 fire elementals), four teams and thirty guards in the building. DISCREPANCY: the "
            "office-tower guards here are softer than the campaign's zero-zone canon."
        ),
        "allies_add": ["Sword Water Clan"],
    },
    "Lone Star Security": {
        "notes_append": (
            "Dark Angel (2054): Precinct 249 in Pinehurst, Everett, under Lieutenant Dolchev handles the "
            "Dark Angel 'suicide'; a Lone Star executive ordered the cover-up at Edward Crull's request "
            "and forensics privately knows the corpse was a murdered squatter. Dolchev sells what he "
            "knows for 5,000 nuyen to the 'Police Widows Fund' and arrests anyone who bribes clumsily. "
            "Response: 4D6 minutes to Club Chiaroscuro, 2D6 to Xanadu Studios (PANICBUTTON), 1D6 to "
            "Crull's house (Renton patrols of four, Predators plus an FN-HAR in the car, better trained "
            "and corp-friendly). Blue Crew block p.24: B3 Q5 S5 C6 I5 W6, Threat 3/3 (2/2 on p.40), "
            "Police Procedures 4, Ares Predator (laser), armor jacket, club, restraints. One patrolman's "
            "report of an unleashed barghest in the city sits unconfirmed in SPU-1. Lone Star breaks up "
            "any Golden Gators extermination at Heaven. Crull's samurai impersonate Lone Star officers in "
            "his ambush. Precinct 249 Matrix map in the Dark Angel prep doc."
        ),
        "leadership_add": [
            {"name": "Lieutenant Dolchev", "title": "Lieutenant, Precinct 249 (Pinehurst, Everett)", "notes": "Crooked, competent; buried the Dark Angel case on an executive's order."},
        ],
    },
    "Knight Errant Security Services": {
        "notes_append": (
            "Dark Angel (2054): finances a shadow operation in the half of Xanadu Studios' building in "
            "Renton's Merideth district -- polished black doors, cameras wired to KE headquarters, bare "
            "plaster inside -- to be converted into a clinic manned by undercover operatives; a repair tag "
            "bills a KE LTG (Computer 4). Four special agents track any trespasser to learn what they "
            "wanted, then abandon the site. September news: the Association of Advertising Producers at "
            "Cannes named KE Seattle's campaign the best commercial art of the year -- clips apparently "
            "filmed during an actual security operation, subterranean combat with automatic weapons, "
            "high explosives and a berserk shaman."
        ),
    },
    "Aztechnology": {
        "notes_append": (
            "Dark Angel: the Oni-do assassin Akimoto's third lie under interrogation is a faked breakdown "
            "confessing that he works for Aztechnology -- 'Chummer, you fragged with the Big Pyramid once "
            "too often.' Runners who believe him go looking in the wrong pyramid."
        ),
    },
    "Seattle News-Intelligencer": {
        "notes_append": (
            "Dark Angel: Update-Net of Friday September 8, 14:00 (the handout prints 2051; the book is "
            "set in 2054). Knight Errant wins best commercial art at Cannes; parazoologist Luke Emerson "
            "of the Seattle Paranormal Facility killed by a school of torpedo sharks (Dr. Sheila Clinton "
            "of Seattle University: 'I guess he got his wish'); Friends of Trolls' second recruitment "
            "drive (Butch Hatchett); and either 'Fallen Angel' (Xanadu releases the second Dark Angel "
            "album Earth Dawn to waning interest; Nigel Spector of Infinity Music: 'Even death can't make "
            "you immortal') or 'Back From the Dead' (Dark Angel appears at a downtown record store to "
            "announce Earth Dawn -- 'What lies in the past is over' -- and drops Xanadu for Zor "
            "Entertainment). Earlier newsfax: 'Singer Dead' -- burned remains recovered by Lone Star "
            "from a notorious BTL den, chip-induced suicide, 'for more details, access 456'."
        ),
    },
    "University of Seattle": {
        "notes_append": (
            "Dark Angel: the September 2054 handout quotes Dr. Sheila Clinton 'of Seattle University' on "
            "her colleague Luke Emerson's death by torpedo-shark feeding frenzy; treated here as this "
            "row under a variant name."
        ),
    },
    "Haida Tribe": {
        "notes_append": (
            "Dark Angel: Sarah Cold-Stream-Water grew up among the oppressed Haida in Tsimshian with "
            "nothing but her looks, fell in with the tribe's less savory members, charmed her way out of "
            "the pimps, and was brought to Seattle by the yakuza and sold as a wife to Mitsuhama's Edward "
            "Crull -- white slavery being 'only technically illegal'. A non-magical Haida mask hangs in "
            "her bedroom."
        ),
    },
    "Tsimshian Nation": {
        "notes_append": (
            "Dark Angel: the yakuza traffic Haida women out of Tsimshian to Seattle as corporate wives; "
            "Sarah Crull (nee Cold-Stream-Water) is one."
        ),
    },
}

LOC_UPDATES = {
    "The Space Needle": {
        "notes_append": (
            "Dark Angel: Club Chiaroscuro, the neo-mystic nightclub where Icelady holds her meets, is "
            "three blocks from the Needle."
        ),
    },
}

NPC_UPDATES = {}

TAG_EXISTING = {}

MATRIX_HOSTS = """
All three mapped systems use the UMS image set (interlinking geometric / fractal constructs).

**1. Xanadu Studios** (p.22; access code from Legwork contacts, by decking, or straight in from any
office terminal, which lands the decker in I/OP-1). Active alert = full shutdown in three Combat Turns.
The SAN trace tells Edward Crull where the decker is (Brother to an Angel).

| Node | Function | Rating / IC |
|---|---|---|
| SAN-1 | Entry | Orange-5, Access 5, Trace and Burn 5 |
| SPU-1 | Business data, extensive telecom records: Dynamo speaks frequently with a Mr. Crull at Mitsuhama Inc. | Orange-4, Access 5 |
| I/OP-1 | All office terminals; upcoming-release data worth 5,000 nuyen to a rival studio | Orange-5, Access 4 |
| SM-1 | Studio recording equipment | Orange-4 |
| SPU-2 | Accounting: 50,000 nuyen petty cash; several million nuyen to Mr. Crull as 'Community Donations', 'Annual Gratuities', 'Miscellaneous Services Rendered' (about equal to Dark Angel's income); the REAL accounts that disprove the forged chip | Orange-5, Tar Baby 4 |
| CPU | -- | Orange-4, Tar Pit 5 |

**2. Lone Star Precinct 249** (p.26; codes by the usual methods, SRII p.163). Active alert = two police
deckers enter to dispose of the intruder. Dolchev has made the files match the official story, so the
run yields nothing on Angel -- but SPU-2 is a gold mine.

| Node | Function | Rating / IC |
|---|---|---|
| SAN-1 | Entry | Orange-5, Access 5, Trace and Burn 5 |
| SPU-1 | Administrative files, auto registrations, patrol reports (one patrolman's unconfirmed unleashed-barghest sighting) | Orange-4, Access 5, Scramble 5 |
| I/OP-1 | All station office terminals | Orange-5, Access 4 |
| SPU-2 | Current investigations: the Angel 'suicide at Heaven' file; about 30,000 nuyen of data on street snitches and undercover officers in the precinct | Red-4, Access 5, Blaster 5, Tar Pit 5, Trace and Burn 4 |
| CPU | -- | Red-4, Blaster 5, Tar Pit 5, Trace and Burn 5 |

**3. Kat Akmura's personal system aboard the Shio-Zuchi** (pp.55-56). Reached from Seattle only by
finding it: Computer (5) senses static, a tenuous Matrix link; Computer (10) reveals an experimental
high-speed wireless link based on satellite-uplink technology; a second Computer (10) places the
hardware physically on Puget Sound. Vicious IC 'meant to dust any interlopers'; the yakuza have far
larger Matrix realities elsewhere. Trace on SAN-1 or DS-2 sends assassins (the Icelady's Doss / Members
of the Band or Mindwarp / Crull's thugs forces, or five Street Samurai archetypes).

| Node | Function | Rating / IC |
|---|---|---|
| SAN-1 | Entry | Orange-4, Barrier 4, Tar Pit 4, Trace and Burn 5 |
| SPU-1 | Communications routing | Orange-5, Blaster 5 |
| DS-1 | Directory: Akmura's contacts and enemies across Seattle, California and Japan -- 200,000 nuyen on the black market, 500 Mp, and a lot of new enemies; her Angel file ('Neutralized. Presumed dead -- operation clean. The bird sings quite prettily in my cage. For the moment, I shall keep him.') | Red-3, Scramble 5, Black-4 (a descending sheet of darkness) |
| SPU-2 | Systems management | Orange-4, Blaster 4 |
| I/OP-1 | The terminal in Akmura's chambers (Area H) | Orange-4 |
| DS-2 | Finances: petty cash 500,000 nuyen, 500 Mp | Red-4, Access 6, Scramble 6, Tar Baby 4, Trace and Burn 5 |
| I/OP-2 | Navigational equipment on the bridge -- precise coordinates that pinpoint the ship | Orange-5, Tar Pit 4 |
| SM-1 | Ship management: layout, and control of the vessel | Red-4, Access 5, Blaster 5 |
| SM-2 | Recording equipment: several unreleased Dark Angel performances | Orange-4 |
| CPU | -- | Red-3, Blaster 6, Black-4 (an Oriental dragon with a transparent body) |

**Not mapped**: Edward Crull's home terminal (no Matrix link; Computer (6) on site for the Fuji account;
Computer (6) or a Virtual Realities quick run TN 6 against tax records to name Akmura); Club
Chiaroscuro's and the Mindwarp's house systems (Eric Girard's Fuchi Cyber-4 defends the latter); the
forged Global Trust chip (Computer (6), -2 with a deck: 1 success = rare Mitsuhama format, 2+ = poor
forgery); Marian Parks' battery cameras (deliberately offline).
"""

NOT_BUILT = """
- **Trista** (the girl in Angel's alley song), **Global Trust** and account 22343 (the bank on the
  forged chip -- the transfers never happened), **Fenris Nacht policlub** and the fixer **Jackal**
  (Akimoto's second lie), **Naked Steele** (holo in Xanadu's security station) and the **Thundering
  Herd** (Bryan's T-shirt logo), **Rocker Born** (the magazine) -- name-drops.
- **Luke Emerson** (Seattle Paranormal Facility researcher, eaten by torpedo sharks) -- dead in the
  news handout; on the facility's org row.
- **The Japanese punker** who hands Bryan and Drew the chip at Heaven, the **two yakuza spies** among
  the culties, the **skagman** and the **coat-check man** at the Mindwarp, the **elevator troll**, the
  **pink-haired receptionist** and **three wageslaves** at Xanadu, **Crull's three punks**, the **Xanadu
  guards and captains**, **Mindwarp troll guards, soldiers and special assistants**, **Jinjiro's five
  bodyguards** and **ten servants**, **MCT guards, senior technicians and security mages**, the
  **Shio-Zuchi's fifteen crew** and **surgeon**, the **megaphone crewman**, the **Oni-do trolls** and the
  **torpedo shark** -- stat blocks on the location and org rows.
- **The Lone Star executive** who ordered the cover-up and the **corp suit** who has seen Angel sing
  for 'some big wheel' (Legwork, 5 successes) -- unnamed hooks.
- **The Oriental troll with the iron bar** in the prologue alley (one of the Oni-do; possibly Kure
  before he was Kure) and **the black van** -- on The Whistler row.
- **Lili's talisman shop** (p.44 only) -- folded into Icelady's Doss.
- **The two or three big oyabun in Japan** Akmura stole Seattle from, **Akmura's friends in the
  yakuza** the GM is told to invent, and **the trio of elves** seen before the epilogue fire.
"""

PLAY_NOTES = """
- Decision tree, not a rail: five opening leads (Chiaroscuro, Xanadu, Precinct 249, Heaven, the band)
  overlap so heavily that missing any is fine. If the team stalls, Homatsu drops an anonymous hint, or
  the two hit teams (Crull's fake-cops ambush, then Akimoto and Kure) explain who the enemy is.
- Protect Icelady 'at all costs' -- she is the paycheck -- but Angel rewards his rescuers even if she
  dies. Her sarcasm is a feature; if the table cannot take it, she offers 1,000 more a head instead.
- Runners who attack Dynamo start a steady stream of firefights and resolve nothing: Akmura replaces
  guards, buildings and Dynamo, and keeps every Xanadu document on chips in cold storage on the ship.
- Nobody kills an oyabun without another oyabun's sanction. Have a contact say so plainly; give a
  team that honestly seeks Usaka or Homatsu a fair chance to reach them (any Fixer or Yakuza Boss
  contact can set the meet). An unsanctioned hit means Chigo Akwe for the rest of the campaign.
- Usaka's meet is Etiquette TN 6 with modifiers; his test ambush wants live captives (trauma patches)
  for Akmura. Homatsu's meet is roleplay -- five minutes of small talk, tea, one clean hit.
- The Oni-do ambush is two skilled assassins doing to the runners what runners do to NPCs; warn them
  through a mumbling street mage or a spirit selling a tip for one service, and use Caesar and
  Cleopatra as the bail-out.
- The Shio-Zuchi is the James Bond finale. Ease it (no MGs in public waters) but keep it a fight.
  Silver hurts the Oni-do. Angel dies to any weapon big enough to sink the ship -- 'a team of violent
  blunderers deserves the consequences'; bad luck gets a miraculous coincidence.
- Alternatives to killing Akmura: she trades Angel for services and becomes a patron, a recurring
  villain or a sinister neutral -- the door into a yakuza campaign. Give her friends the team would
  hesitate to offend, and tell them so.
- Karma: Angel saved 4; Akmura dealt with 2; actions cleared with the yakuza 1; Icelady killed -2;
  partial success (Angel dead, Akmura eliminated, proof of his fate) 2. Individual: -1 per runner the
  yakuza identify. Wise runners hide their faces from the start.
- Loose ends: Sarah Crull (contact, companion, or left in place at MCT); Dynamo as a music-industry
  contact; the Knight Errant clinic in Merideth; the Fallen Heroes' vendetta if a bandmate died; Shiro
  and Homatsu as enemies or employers; Angel's fortune and the epilogue fire and the three elves.
"""
