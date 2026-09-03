# Ivy & Chrome (FASA 7311, 1991) -- campaign order #15. Bellevue / Downtown / Auburn / Snohomish /
# Everett / Sea-Tac / Salish-Shidhe North Cove, June 2051 (both news handouts are the Seattle
# News-Intelligencer Update-Net for Thursday June 8 2051; the introduction's "The year is 2050" is
# the FASA boilerplate line and is ignored). A decision-tree "find the runaway heiress" run that
# turns into an Aztec blood-magic horror and a helicopter assault on a pacifist elven commune.
# Source text: docs/Adventures/text/Shadowrun 1e - Ivy & Chrome {FASA7311}.txt (62 pages).
# ASCII only (pre-commit hook).
#
# Editing inconsistencies in the book (recorded on the affected rows):
#  - Fayette's eyes are hazel in the prologue (p.5) and "flashing blue" in the cast page / medical
#    handout (pp.48, 58).
#  - Juzu Clinic SAN: the system map key gives NA/SEA/3206 (34-8705) (p.30); the Legwork table gives
#    NA/SEA/3206 (34-8075) (p.46). The room text also swaps I/OP-3 and I/OP-4 (Kaus/Meader terminals
#    vs the basement Improvised Offices) relative to the map key.
#  - North Cove is "north of Seattle" on p.24 and "southwest of Seattle" on p.46 (it is southwest, on
#    the Pacific coast; Interstates 12 and 101 run west).
#  - The intern is "Farmwelll" in the contents and "Farnwell" everywhere else; Arhill signs Memo 2
#    as "Dr. Achill"; Aztechnology's branch is "Tialoc III" (p.7), "45-Tlaoc" (pp.59-60) and the
#    "Tlaoc division" (p.62) -- all Tlaloc, the Aztec rain god. The spirit Anton contacted is "the
#    Aztec god of rain" in Legwork (p.44) but "Patecatl" in the medical handout (p.59).
#  - Rat Mash Dancer has "brass cartridge cases woven into her dreadlocked hair" (p.25) and "a knotted
#    braid ornamented with feathers and spent cartridges" (p.55). The bar scene gives her five
#    followers plus a seventh ork at Sea-Tac; the cast page says "all five".
#  - Anton wears "an armor vest with plates" on p.35 and Armor Clothing (3/0) on p.49.
#  - Marti "joined the Shoalwater elven community shortly after reaching puberty" (p.52) but the
#    Legwork contact says she "showed up at Shoalwater ... suddenly Martha Newblood" with a five-year-old
#    "over ten years ago" (p.46); she is Suzanne's "step-sister" on p.7 and "sister" elsewhere.
#  - The prologue has Fayette walking from the Conservatory (Bellevue) toward Elby's and getting lost
#    two blocks out; p.23 puts Elby's at James Street and Ninth Avenue, downtown.
#  - The Knights' pistol is a "Colt American L36" (p.22); Nick's is a "Colt America L36" (p.53).

ADVENTURE = "Ivy & Chrome"
ORDER = 15
SOURCE = "Shadowrun 1e - Ivy & Chrome {FASA7311}.pdf, pp. 4-62"
YEAR = "2051 (June; news handouts dated Thursday June 8, 2051)"

SYNOPSIS = """
The fixer calls with a job that will not happen anywhere real: a meet inside **Virtual Meetings
Incorporated**, the corporate-elite iconferencing service. In a teak conference room that smells
right and is not there, the runners wait for a Johnson who arrives through the wall wearing the
milky-glass, gold-armored icon of **Diana** -- a legendary decker dead ten years -- and who moves and
speaks like someone who has never worn a body before. An AI? No: it is **Marti Vann**, Diana's
sister, a non-decker driving her sister's Fuchi Cyber-4 by keyboard, who wants 10,000 nuyen each up
front and 20,000 more for the safe return of her niece **Fayette Myers**, missing since this morning
from the **Rhododendron Conservatory**, a 130,000-nuyen-a-year finishing school in Bellevue.

Fayette has run away with **Nick Voigt**, an elven go-ganger of the **Double Devils**, on his
Yamaha Rapier, bound for her aunt's pacifist elven commune at **Shoalwater** on North Cove in
Salish-Shidhe territory. The school wants it kept quiet; its security chief hires a ganger to
deliver monogrammed bullets. The clues -- a napkin from **Elby's Bar and Grill** reading "WE'LL USE
THE RAPIER", a three-month-old **Native American Airways** ticket to **King's Glen**, a follow-up
appointment at **Juzu Clinic** for a test that does not exist, a math teacher who belongs to the
**High Chivalrous Order of Humanis Policlub** and keeps the boyfriend's photo -- lead through a
back-room den at **Cratchit's Family Entertainment** in Auburn, a Snohomish tire dump full of
booby-trapped elves, an airport stakeout, and Elby's, where twenty-eight bodies lie in the back
room and an intern's astral form keeps watch.

The truth is under Juzu Clinic in Everett. Fayette is Fayette d'Venescu, daughter of Diana
(**Suzanne Vann-d'Venescu**) and **Anton d'Venescu**, once Aztechnology's star corporate mage, who in
2034 ate the peyote extract *ocapatli*, contacted an Aztec power, and swore to sacrifice his wife's
heart and his baby daughter's. He impaled Suzanne in a coffin motel; she got the child to Marti and
a fortune out of his Aztechnology accounts first. Anton lost his magic, believes the spirits will
kill him, and lives in a malon-fumigated, Rating 7-warded bunker beneath the clinic guarded by four
Force 7 elementals. His physician and only friend, **Dr. Arhill**, recognized Fayette's face,
confirmed her DNA, told Aztechnology, and hired **Rat Mash Dancer's** Cascade ork mercenaries to
bring her in. Runners who get caught wake in the alley behind Elby's with a tracking disk under the
shoulder blade.

Endgame at Shoalwater: sixty-five pacifist elves, a consensus council, one Remington 750, five
bows, an ex-panzer rigger named **Jac** and the wreck of his thunderbird **Charlotte** with two
salvageable anti-vehicle missile launchers -- against an invisible infiltration team (Arhill,
Anton, both interns, four Aztechnology senior technicians) at 2:30 a.m. on high tide and two
Hughes Stallions carrying twenty orks. Save Fayette and kill Anton: 5 Karma, and the news reports
Aztechnology quietly cancelling its grants to Juzu Clinic. Fail, and Anton tells the newsnet, "I owe
it all to my daughter Fayette. With her contribution, I cut right to the heart of the matter."
"""

TIMELINE = """
- **2034** -- Anton d'Venescu's ocapatli research and ritual at Aztechnology; he is initiated, swears
  the mother-daughter sacrifice. About three years after the marriage he impales Suzanne (Diana) in
  a coffin motel; she has already hidden the baby with Marti and moved several million nuyen from his
  Aztechnology accounts into a Banque Orbitale de Suisse trust. "About ten years ago" on the street.
- **Over ten years ago** -- Marti Vann arrives at Shoalwater as Martha Newblood with a five-year-old.
  At fourteen Fayette is sent to Seattle as Fayette Myers, Rhododendron Conservatory, Oxus Hall.
- **Three months before** -- first escape: Fayette books a King's Glen flight, gets lost near Zappy
  Zed's, is picked up by Lone Star and examined at Juzu Clinic; Arhill confirms the resemblance,
  schedules a "follow-up" in four months and writes Memo 2 to Aztechnology Branch 45-Tlaloc.
- **Three days before** -- the Chivalric Knights find Nick and Fayette at Elby's and chase them to
  the Snohomish dump; Bart begins his watch on Elby's. **Two days before** -- Rat Mash Dancer's orks
  raid Elby's on Arhill's orders and kill everyone inside (28 bodies). **The day before** -- Bart's
  last report.
- **Day 1, after midnight** -- Fayette sneaks under the fence; Che-Che tells the aunt on the phone.
  **Morning** -- Marti books VMI; **~6 hours later** the meet; 3:00 p.m. Nick and Fayette reach
  Shoalwater on the Rapier (via Interstates 12 and 101, Blue Ticket bought "last week").
- **Day 4** -- left to his own sources, Arhill locates Fayette at Shoalwater (sooner if the runners
  lead him there; Aztechnology attacks three hours after learning the location).
- **Day 5, 2:30 a.m., high tide** -- the raid on Shoalwater (or the roadblock ambush on Interstate 12
  if the party runs).
- **Thursday June 8, 2051** -- the Seattle News-Intelligencer Update-Net handouts.
"""

ORGS = [
    {
        "name": "Rhododendron Conservatory",
        "org_type": "private boarding school",
        "tier": 2,
        "headquarters": "Inglewood District, Bellevue, near Lake Washington (Sorrel Hall)",
        "summary": "Genteel 130,000-nuyen-a-year finishing school for corporate heirs; wants Fayette's disappearance buried",
        "description": (
            "A prestigious private academy for the children of the corporate elite, set on sculpted "
            "lawns behind a wire-mesh fence in Bellevue's Inglewood District. Its business is "
            "'breeding': instilling manners in teenagers against the pull of 21st-century mass "
            "society. Tuition is 130,000 nuyen a year. Headmaster Raymond Blum handles the "
            "hospitality and the Hall of Fame plaques; Director Anita Wood does the real work; "
            "Director of Security Mr. Blake keeps order and convinces prospective parents that "
            "there is nothing to keep order against. Faculty: P. Grumblatt (mathematics), Mr. Burg "
            "(Media Arts), Ms. Lee (Corporate Civics), Ms. Primrose (history), Mr. Denn (coach); "
            "housemother Cyndy in Oxus Hall; groundskeeper Leroy."
        ),
        "leadership": [
            {"name": "Raymond Blum", "title": "Headmaster", "notes": "Plump, red-faced; propriety first, scandal never."},
            {"name": "Anita Wood", "title": "Director", "notes": "Runs the school day to day."},
            {"name": "Mr. Blake", "title": "Director of Security", "notes": "'Bent' on covering Fayette up."},
        ],
        "notes": (
            "Three crack guards at the gate cottage (Former Company Man stats: Wired 2, smartlink, "
            "muscle replacement, Roomsweepers with stun gel, forearm snap blades, headset radios) plus "
            "five reinforcements in 1D6 minutes; PANICBUTTON in the Main Offices; electrified sensor "
            "fence (3L3, Electronics 4). No magical defenses (hires a security firm's wage mage if "
            "needed). The school assumes Fayette ran off with a boy, hopes she comes back, and will "
            "press charges against impostors; prisoners can bribe the local Lone Star branch for 1,000 "
            "nuyen. Blake pays the ganger Dragon Ted to deliver a receipt for monogrammed bullets. "
            "Fayette's tuition is paid from a confidential Banque Orbitale de Suisse account that "
            "traces (Computer 9, two successes) to Aztechnology. Student files carry 'ashes' left by "
            "Aztechnology deckers. Uses Juzu Clinic for medical care. Aftermath: Marti sends Fayette "
            "back; she fails every course and is expelled."
        ),
        "allies": ["Juzu Clinic"],
    },
    {
        "name": "Juzu Clinic",
        "org_type": "private medical clinic",
        "tier": 2,
        "headquarters": "Pinehurst neighborhood, Everett",
        "summary": "Aztechnology-funded clinic for corporate mages; Dr. Arhill's practice and Anton d'Venescu's hiding place",
        "description": (
            "'A medical facility to meet your health care needs, offering general practice, cosmetic "
            "modification, and cybernetic evaluation. Juzu provides ultra-low-impact therapy for the "
            "magically sensitive.' Dr. Kaus (general practice), Dr. Meader (cyberneticist) and senior "
            "physician Dr. Arhill (Practitioner of Essence Medicine) with six nurses, two interns and "
            "a Board of Directors. The megacorps send their valuable wage mages here because Arhill can "
            "cure even fatal diseases without destroying the magic that makes them worth curing: 1D6 "
            "days and a 500-nuyen deposit for an appointment, prices at 1.5 times book. Most of its "
            "money comes as charitable grants from Aztechnology."
        ),
        "leadership": [
            {"name": "Dr. Arhill", "title": "Senior physician, Practitioner of Essence Medicine", "notes": "Anton's doctor and partner."},
            {"name": "Dr. Kaus", "title": "General Practitioner", "notes": None},
            {"name": "Dr. Meader", "title": "Cyberneticist", "notes": None},
        ],
        "notes": (
            "Fifteen security guards (Corporate Security Guard stats, armor jackets with respirator "
            "helmets, headware radios, Uzi IIIs wired as smartguns) under a chief in the Guard "
            "Headquarters who can lock every steel door (Rating 6 maglocks) and control the basement "
            "elevator. Arhill's records on Fayette Myers and Anton d'Venescu are the player handouts "
            "(pp.58-60); the business datastore lists accounts with mercenaries and military outfitters "
            "for a raid into Salish-Shidhe territory. Hospitalization but not Intensive Care. The "
            "clinic's Matrix trace does not call Lone Star -- it rings a phone at The Quick, the Dead, "
            "and the Still Moving and sends the orks. Success news: Aztechnology abruptly cancels its "
            "grants 'citing budget shortfalls' and the Board launches an Emergency Fund Drive."
        ),
        "allies": ["Aztechnology", "Aztechnology Tlaloc Division", "Rat Mash Dancer's Mercenaries"],
        "enemies": ["Shoalwater Elven Community"],
    },
    {
        "name": "Aztechnology Tlaloc Division",
        "org_type": "corporate research division",
        "tier": 3,
        "headquarters": "Aztechnology Branch Office 45-Tlaloc (the 'shadowy Tlaloc III outlet'); in practice the Juzu Clinic basement",
        "summary": "Anton d'Venescu's ritual-magic research division: senior technicians, a typing pool, two chemists and a hidden bunker",
        "description": (
            "The Aztechnology branch that funded Anton d'Venescu's 2034 research into ocapatli and "
            "pre-Columbian conjuring and still carries him on the payroll. Certain people in the "
            "corporation want to see whether his ritual methods work, so the division keeps him in a "
            "protected environment, finances his search for his daughter, and looks the other way "
            "while he hires outside talent. Its field staff are Aztechnology Senior Technicians ('a "
            "grade below the typical company man'), a secretary and two research scientists, all "
            "living in the improvised offices and laboratory under Juzu Clinic and synthesizing "
            "ocapatli, the peyote-derived hallucinogen through which one is said to commune with the "
            "powerful spirits."
        ),
        "leadership": [
            {"name": "Anton d'Venescu", "title": "Project supervisor (wage mage, magic lost)", "notes": None},
        ],
        "notes": (
            "Senior Technician block (p.56): B6 Q5 S6 C2 I4 W5 Ess 3.65 R4; Biotech 5, Computer 3, "
            "Electronics 2, Etiquette (Corporate) 3, Firearms 8, Unarmed 6; cybereyes (thermographic, "
            "flare comp), headware radio, smartlink; armor jacket 5/3, Uzi III with smartgun adaptor. "
            "Seven of them under the clinic (one at the elevator, three in the offices, three in the "
            "lab), trained for indoor warfare -- doorway fire teams, concentrated fire on one victim. "
            "The secretary (Colt America, four defensive grenades) and lab assistants throw grenades. "
            "Four technicians join the Shoalwater infiltration team. Failure news: 'Scientists in "
            "Aztechnology's Tlaoc division have discovered a promising new technique for harnessing "
            "metamagic.' Success: Aztechnology management would like to forget Anton ever existed and "
            "does not retaliate unless the runners sell the story to the media."
        ),
        "allies": ["Aztechnology", "Juzu Clinic"],
        "enemies": ["Shoalwater Elven Community"],
    },
    {
        "name": "High Chivalrous Order of Humanis Policlub",
        "org_type": "policlub chapter / hate group",
        "tier": 1,
        "headquarters": "Back room of Cratchit's Family Entertainment, Maple County neighborhood, Auburn",
        "summary": "The 'Chivalric Knights' -- robed, torch-bearing Humanis fanatics on a crusade to rescue Fayette from her 'rapacious elf'",
        "description": (
            "A den of Humanis Policlub members who style themselves a High Chivalrous Order: formal "
            "bows for a new 'brother', back-slapping and beer afterwards, a homemade altar among the "
            "ammunition boxes, and hooded robes, torches and quasi-mystic symbols for their trials. "
            "They put captured 'traitors' on trial for crimes against humanity, record the proceedings "
            "for propaganda and recruitment vids, always find the accused guilty, and administer "
            "summary 'justice'. Buffoons in appearance; fanatics who will kill for the cause. Password: "
            "'purity', whispered to Cratchit."
        ),
        "leadership": [
            {"name": "Cratchit", "title": "Den keeper; 'a big man in the poli'", "notes": None},
            {"name": "P. Grumblatt", "title": "Member; Rhododendron Conservatory mathematics teacher", "notes": "The Order's eyes inside the school."},
        ],
        "notes": (
            "Knight block (p.22): B4 Q4 S5 C2 I2 W4 Ess 6 R3, armor 2/1; Bike 3, Car 3, Demolitions 4, "
            "Etiquette (Street) 3, Firearms 4; armored vest, Colt American L36, knife -- they fetch "
            "heavier weapons from the firing range when expecting a fight, and one member uses the "
            "Former Wage Mage (combat) block for the ambush. Five in the back room. Their 'quest': a "
            "member found Fayette and Nick at Elby's three days before the hire, chased them to the "
            "Snohomish dump and lost them; Bart kept watch on Elby's and reported orks with 'lots of "
            "artillery' going to The Quick, the Dead, and the Still Moving and in the back door of "
            "Juzu Clinic. They will talk to humans with the password; they attack anyone who admits "
            "traffic with metahumans, and ambush runners Grumblatt flags. Rumor: 'Cratchit ... is "
            "starting a new crusade. Guys from his place keep scopin' out the metahuman bars, looking "
            "for some human girl.'"
        ),
        "allies": ["Humanis Policlub"],
        "enemies": ["Double Devils"],
    },
    {
        "name": "Double Devils",
        "org_type": "go-gang (all-elven)",
        "tier": 1,
        "headquarters": "The tire dump on Filbert-Maltby Road, northern Snohomish district, near Thrasher's Corner",
        "summary": "Hard-core all-elven go-gang living in vans buried under a mountain of shredded tires; Nick's former gang",
        "description": (
            "A hard-core, semi-organized all-elven go-gang that prowls the northern Snohomish district "
            "on Yamaha Rapiers. Most of them lost family and friends along with their humanity; they "
            "mistrust humans, and the human street gangs make their lives hell. Colors: a black and "
            "red logo of a pitchfork overlaid with two Ds with arrowhead tails; red is the only color "
            "they wear, over black pants, black boots and long black coats with the sleeves cut off. "
            "They evicted a squatter tribe from the dump about a year ago and now live in vans and "
            "campers under the heap of twisted wire and rubber."
        ),
        "leadership": [
            {"name": "Shark", "title": "Gang boss", "notes": "Drives a yellow garbage-crushing construction machine."},
        ],
        "notes": (
            "Twelve gangers (p.27): B5 Q6 S5 C6 I4 W4 R5, armor 0/1; Armed Combat 5, Bike 4, Etiquette "
            "(Street) 4, Firearms 4, Stealth 5, Throwing 3, Unarmed 5; hand razors, low-light eyes; "
            "AK-97 or Uzi III, knife, synth-leather, Yamaha Rapier. Booby-trap grenades buried in the "
            "trash (Reaction 6 to cross; Intelligence 2 finds three per success). Camp: thirteen "
            "Rapiers and spare parts, a human skull in a party hat, a battered simsense player, 100 "
            "Streetline Special clips, 30 AK-97 clips, 13 Uzi clips. Nick was a member in good standing "
            "until he took up with a human; some of them would like to see him hurt. They know he ran "
            "off with 'a classy human girl named Fayette Myers', that he fears flying, and that there "
            "is a commune in the North Cove area. Nick's minivan hides the North Cove map with "
            "Shoalwater circled. Squatters in an abandoned strip mall a few blocks away raid them for "
            "food; the gang may mistake the runners for a raid. Rumor: 'some kinda go-gang in the "
            "tire dump by Route 12, and they're out for blood.'"
        ),
        "enemies": ["High Chivalrous Order of Humanis Policlub"],
    },
    {
        "name": "Rat Mash Dancer's Mercenaries",
        "org_type": "mercenary band (Cascade ork)",
        "tier": 1,
        "headquarters": "The Quick, the Dead, and the Still Moving, Pine Street",
        "summary": "Seven Cascade ork tribal warriors turned city mercs under a Coyote shaman; Arhill's kidnappers and the Elby's killers",
        "description": (
            "Warriors of the Cascade ork tribe whom the chance of bigger nuyen brought to the city. "
            "Leather-Look armor jackets over dirty T-shirts and camouflage trousers, swords etched "
            "with Cascade ork traceries, and absolutely no social inhibitions, of which they are "
            "proud. Their leader Rat Mash Dancer finds them jobs, mothers them harshly and keeps them "
            "honest with the threat of a powerball. They find Dr. Arhill ridiculous but stay bought "
            "until someone else pays; left to themselves they would switch sides for 10,000 nuyen, "
            "which she does not permit."
        ),
        "leadership": [
            {"name": "Rat Mash Dancer", "title": "Leader; Coyote shaman", "notes": None},
        ],
        "notes": (
            "Ork Mercenary block (p.54): B7 Q5 S6 C1 I3 W2 Ess 6 R3; Armed Combat 8, Demolitions 4, "
            "Etiquette (Corporate) 2 / (Street) 3, Firearms 8, Rotor Craft 3, Stealth 6, Unarmed 8; "
            "AK-97 with two clips, armor jacket 5/3, sword (Reach +1, 6M2), two Neuro-Stun VIII gas "
            "grenades. Six sit at a table cleaning guns in the bar (Stealth 6 to eavesdrop); the seventh "
            "watches the Native American Airways lounge at Sea-Tac in black shades handing out Mothers "
            "of Metahumans leaflets, carrying a Walther palm pistol, a survival knife, Fayette's "
            "photograph, an underlined King's Glen flight schedule and an Ever-Light matchstick from "
            "the bar. They massacred Elby's on Arhill's orders, ambush and kidnap anyone the interns "
            "point them at, and deliver prisoners to the Juzu loading dock for cash. 'Airmobile "
            "insertion' job pinned on the bar's war map: tan/yellow pin near North Cove, Aztechnology "
            "links rumored. Rind's troll brothers may come looking for them."
        ),
        "allies": ["Juzu Clinic", "Cascade Ork"],
    },
    {
        "name": "Shoalwater Elven Community",
        "org_type": "elven tribal holding / commune",
        "tier": 2,
        "headquarters": "Shoalwater, North Cove, Salish-Shidhe Council (former Shoalwater Indian reservation)",
        "summary": "Sixty-five pacifist pinkskin elves farming wind, sun and vegetables on a rocky Pacific inlet; Marti Vann speaks for them",
        "description": (
            "The Elven Tribal Holding of Shoalwater: a 'tribe' formed shortly after the Native "
            "Americans began admitting pinkskin metahumans, on a former Indian reservation whose "
            "original people moved to more desirable land. Sixty-five inhabitants, thirty of them "
            "children, thirty-five voting adults, all decisions by consensus. They believe technology "
            "should be used to reduce damage to the environment: solar panels, one-armed windmills, "
            "passive-solar roofs, vegetable gardens, and a little income from selling the power they "
            "generate. Quiet, reclusive, dedicated pacifists with neither the knack nor the stomach for "
            "combat; they freeze in battle without a Leadership (3) test to rally them."
        ),
        "leadership": [
            {"name": "Marti Vann", "title": "Spokesperson ('Martha Newblood')", "notes": "Calls the council; cannot decide for it."},
            {"name": "Arden", "title": "Council voice; former Tir Tairngire office-holder", "notes": "'Elves handle their own problems.'"},
            {"name": "Jac", "title": "Council voice; ex-panzer rigger", "notes": "'There's always Charlotte...'"},
        ],
        "notes": (
            "Winning a defense plan: Charisma or Persuasion (4), ten total successes across speakers, "
            "another day and +1 for each revised plan. Opponents: Marietta (send Fayette away), Arden "
            "(outsiders out), Fantine ('I just don't think that's right'); Jac supports any plan that "
            "uses the Charlotte and adds his five Charisma dice. Arms: one Remington 750, five hunting "
            "bows, garden tools, Jac's Colt Manhunter, and two jury-rigged twin-pack LG-AVM launchers "
            "with three reloads. Ordinary members use Elf Pedestrian stats, some with Firearms 2 or "
            "Projectile Weapons 2. Fayette 'may walk in Salish-Shidhe lands as long as trees grow and "
            "sun shines' -- the Council numbers her among its people and gave her a new name. Arhill's "
            "Watchers (Force 3, two at a time) patrol the perimeter once he finds the place. The "
            "Charlotte's radio still reaches the Salish-Shidhe Ranger Force."
        ),
        "allies": ["Salish-Shidhe Council"],
        "enemies": ["Aztechnology Tlaloc Division", "Juzu Clinic"],
    },
    {
        "name": "Virtual Meetings Incorporated",
        "org_type": "corporation (virtual-reality teleconferencing)",
        "tier": 3,
        "headquarters": "Seattle facility (three-storey atrium); a division of UCAS Data Systems",
        "summary": "VMI -- photo-resolution virtual conference rooms for the corporate elite; where Marti hires the team as 'Diana'",
        "description": (
            "Virtual Meetings Incorporated, a division of UCAS Data Systems, has quite a rep among the "
            "corporate elite of the UCAS: privacy, security, quality and photo-resolution reality, "
            "assuming you have the nuyen. Larger corps run their own iconferencing; VMI serves smaller "
            "corporations and individual clients. Participants lie on reclining couches under ornate "
            "headgear or datajack adaptors while technicians resolve multi-band visuals into image "
            "templates, then meet in a teak-and-Impressionist conference room that smells, feels and "
            "tastes real. Dedicated city-to-city hardlines or secure satellite uplinks and a legion of "
            "crack corporate deckers guard the system; external clients receive connection protocols "
            "to sync their own systems in."
        ),
        "notes": (
            "No decking inside VMI -- entry is only through its senselink couches; a decker may glance "
            "at the hardware. Magicians suffer a TN modifier equal to their Magic while jacked in ('Magic "
            "and the Matrix just don't mix'); no magic is possible and violence gets a null response. "
            "Marti fed the protocols into Diana's deck, could not execute the integration, and let the "
            "deck force it -- sparks and strain on the VMI system, the walls shimmering as her icon "
            "arrives through the corner. She departs by Slow Disconnect (an astounding failure of "
            "protocol to any decker) and later offers a private e-mail drop box for contact. Antagonize "
            "VMI and they call Lone Star; the receptionist has a PANICBUTTON. A reusable neutral meet "
            "for Johnsons who will not be seen."
        ),
    },
    {
        "name": "Native American Airways",
        "org_type": "regional airline",
        "tier": 2,
        "headquarters": "Native American Airways terminal, Seattle-Tacoma Airport",
        "summary": "Small-plane commuter airline into Salish-Shidhe territory; the King's Glen flights Fayette booked and never took",
        "description": (
            "A commuter airline flying small planes from its own terminal at Seattle-Tacoma Airport to "
            "airstrips in Salish-Shidhe territory, including King's Glen on North Cove. Its lounge is "
            "where sararimen wait for tribal-land flights -- and where Arhill posts an ork."
        ),
        "notes": (
            "Sea-Tac's ticket registry holds the record: Fayette and Nick scheduled a commuter flight "
            "to North Cove three months ago and never showed. Nick has a severe fear of flying. The "
            "book also calls it 'Native American Airlines' and 'Native America Airways'."
        ),
    },
    {
        "name": "Concrete Dreams",
        "org_type": "rock band",
        "tier": 2,
        "headquarters": "Seattle (touring; surprise gigs at Club Zor)",
        "summary": "Megafamous rock band whose surreal city-street logo is on Fayette's dorm door; 'still together' per the June 2051 news",
        "description": (
            "The megafamous Concrete Dreams, whose surreal city-street logo decorates the door of "
            "Fayette's suite at Rhododendron Conservatory. Known for unannounced appearances at the "
            "watering hole regulars call Club Zor, drawing several hundred people with no advance "
            "publicity and bringing Lone Star out for crowd control."
        ),
        "notes": (
            "June 8, 2051 news: 'No way, chummer. Like, not us,' says the lead singer of break-up "
            "rumors; a sound technician says they settled 'all that personal stuff' long ago; rumors "
            "persist that one or more C-Dreamers may quit over the licensing agreement on their latest "
            "T-shirt line. Name-dropped in Mercurial's rocker scene as well."
        ),
    },
    {
        "name": "Mothers of Metahumans",
        "org_type": "policlub (metahuman rights)",
        "tier": 2,
        "headquarters": "Seattle chapter (national policlub)",
        "summary": "Metahuman-rights policlub whose leaflets a shamefaced ork mercenary hands out as his Sea-Tac stakeout cover",
        "description": (
            "A metahuman-rights policlub -- 'We're all loving brothers under the skin, chummer, ain't "
            "that so?' -- whose pamphleteers are a familiar enough sight at Sea-Tac that one of Rat "
            "Mash Dancer's orks uses a stack of their leaflets as a disguise while watching the Native "
            "American Airways lounge."
        ),
        "notes": "Only the leaflets appear in this adventure; the ork is embarrassed by the cover and keeps it up half-heartedly. Real policlub in later sourcebooks; treat as texture until then.",
    },
    {
        "name": "Futisama Research Ventures Institute",
        "org_type": "research corporation (Fuchi subsidiary)",
        "tier": 2,
        "headquarters": "Seattle area (formerly independent; now majority-owned by Fuchi Industrial Electronics)",
        "summary": "Small research firm Fuchi took over at gunpoint in spring 2051; the public has stopped caring",
        "description": (
            "A formerly independent research institute whose key laboratories Fuchi Industrial "
            "Electronics allegedly held hostage with security troops as a bargaining chip during "
            "merger negotiations. Fuchi has since become majority shareholder; deposed president Mr. "
            "Kama 'considers it inappropriate to comment' and is planning an extended vacation in "
            "Amazonia."
        ),
        "notes": (
            "June 8, 2051 news: polls show the public has lost interest; Fuchi asks UCAS agents to end "
            "their investigation ('This is a standard business procedure' -- Mr. San of Fuchi). One UCAS "
            "investigator: 'If we tolerate something like this, pretty soon the corps will be running "
            "this country.' The failure handout links Fuchi Cyber's 35-point stock jump on 'a "
            "breakthrough magic/technology meld' to the Aztechnology metamagic story."
        ),
        "enemies": ["Fuchi Industrial Electronics"],
    },
]

LOCATIONS = [
    {
        "name": "Rhododendron Conservatory",
        "location_type": "private boarding school",
        "district": "Inglewood District, Bellevue, near Lake Washington",
        "security_level": "Corporate Standard",
        "controlling_org": "Rhododendron Conservatory",
        "summary": "Fenced campus of white halls and DecoVeggie shrubs: Sorrel Hall offices, Oxus Hall dorms, Dearpark Gym, Frankle Hall classrooms",
        "description": (
            "Well-trimmed lawns and DecoVeggie shrubs behind a thin wire-mesh fence, with three "
            "blue-eyed, fresh-faced men in dapper leisure suits and troll-sized shoulders sitting by an "
            "ornate white cottage at the gate. Sorrel Hall (white walls, porch, decorative columns, "
            "voice-print door, a machine dispensing real coffee) holds the Main Offices, the "
            "Dispensary and the Headmaster's RealWood-panelled office with its Hall of Fame plaques. "
            "Dearpark Gymnasium is brick with a basketball court, lockers and a trophy alcove. Oxus "
            "Hall is a complex of linked apartment clusters with pink columns, chrome conduits, the "
            "beat of the Stim Boys from some room at every hour, a cafeteria, a housemother, visiting "
            "hours 7-9 p.m. and reinforced plate-glass windows. Frankle Hall's antique brick hides "
            "trideo classrooms and a faculty broadcasting studio. The grounds are green hillocks, "
            "tropical flowers on DeFrost, stands of pine and sheds -- and a groundskeeper ducking into "
            "the branches."
        ),
        "notes": (
            "Sorrel Hall: microphones in every room; the computer tolerates ten minutes of visitors "
            "talking to each other and five minutes of silence in an empty room before sending Mr. "
            "Blake in with a cheerful 'Hallo'; maglocks (janitor's door Rating 4), ultrasonic sensors "
            "on windows and the main door at night. Dispensary: unstaffed, supplies for three medkits, "
            "a standalone medical computer listing Fayette's 'Cqm-S' follow-up at Juzu early next "
            "month. Fayette's locker (Strength 4): acid-green tights, the three-month-old Native "
            "American Airways ticket to King's Glen, a male elf's ear-tip stud. Oxus Hall: maglock 3, "
            "Electronics 4; someone comes or goes every 2D6 minutes; the girls (Street Kid stats, no "
            "skills) need an Opposed Charisma vs Intelligence test. Fayette's suite 'Welcome to the "
            "Inferno' (Concrete Dreams poster, holographic Chinese zodiac): Tanya's room, Vi and "
            "Anastasia's, Che-Che and Fayette's, Cyndy's office. Fayette's half: posters and audio "
            "disks already combed through; Perception (8) finds the Elby's napkin 'WE'LL USE THE "
            "RAPIER'; missing are her favorite outfit, a pillow, flashlight, chemsuit top and blanket; "
            "the secret place under a loose floor tile is empty (Che-Che gave it to Arhill). Fence "
            "gap: light-blue synthetic threads (Perception 5). Firefights bring teenage girls back "
            "with Insta-Pix cameras."
        ),
    },
    {
        "name": "Juzu Clinic",
        "location_type": "hospital",
        "district": "Pinehurst neighborhood, Everett",
        "security_level": "Corporate High Security",
        "controlling_org": "Juzu Clinic",
        "summary": "Brick clinic of beige waiting rooms and Aztec-motif corridors over a malon-gassed, warded basement bunker where Anton d'Venescu hides",
        "description": (
            "Thick glass doors, a plastic sign listing Drs. Kaus, Meader and Arhill, and a waiting "
            "room of pastel walls, plastic plants, orange seats and red video screens selling cosmetic "
            "surgery and Health Council nutrition -- with a surprising number of corporate wizards, "
            "charms and fetishes tucked into their suits. Cream corridors pass examination rooms with "
            "gas tanks, tissue vats and nests of tubing. Arhill's wing has steel-blue carpet, paintings "
            "of Aztec motifs and Rating 12 maglocks on every door but his windowless office. Beyond "
            "the 'Bioisolation Chamber. Keep Out.' sign: a white aluminum shower room, yellow "
            "chemsuits, canisters of malon insecticide feeding the ventilation, and an elevator down "
            "to a corridor of mirrored ebony glass where hospital wards have become office, squat and "
            "gunnery shop. A one-way ballistic mirror hides Anton's spartan gray chamber."
        ),
        "notes": (
            "Map pp.32, 34. (A) Waiting room: receptionist (Corporate Secretary, PANICBUTTON: four "
            "Lone Star troopers in five minutes, unlimited in twenty), 2D6 citizens, 1D6 wage mages; "
            "Stealth 6 to slip past. (C) Guard HQ: guard in surgical-green armor, monitors, door and "
            "elevator switches. (E) Arhill's office: Arhill and Hortense matching X-rays to Chinese and "
            "Amerindian mystic body diagrams; on the desk Che-Che's bag (Elby's napkin, a Seattle-to-"
            "Shoalwater I-12/I-101 travel brochure) and charcoal rubbings of Aztec glyphs describing a "
            "chamber sealed against insects that protects its occupant from the vengeance of the gods "
            "for years, not forever. (F) Exam Room I: step-pyramid DNA scan/matcher; readout 'Fayette "
            "and Family' -- 'a clear match ... Fayette will satisfy the requirements of her father's "
            "ritual.' (G) Exam Room II: two-snake calendar; cabinet (maglock 5) with 10 stim, 50 tranq, "
            "5 trauma patches; alarmed box (maglock 8, Electronics 7) of ardone -- Anton's "
            "hallucinogen-overdose drug, poisonable, used within 1D6 days. (H) Recovery: Farnwell's "
            "empty body. (I) Loading dock (maglock 7, IR cameras, two guards in one turn): a three-meter "
            "flint-eyed idol tagged 'Property of Anton d'Venescu, ATC' -- authentic Aztec blood-magic "
            "idol, aura sickening (Willpower 8 or a Light Stun), used 15-20 years ago. (J) Quarantine: "
            "malon vapor 6L3 per two turns without a respirator; eight-person elevator; a Rating 7 ward "
            "renewed by Arhill and Aztechnology mages, weakening. (K) Basement: seven senior "
            "technicians, a secretary, two scientists (ocapatli synthesis; stray shots spill "
            "chemicals), fifteen guards who let intruders reach the gas chamber then fire fifteen Uzis, "
            "four Force 7 elementals (air, earth, fire, water) on the astral. (N) Anton's chamber: "
            "banishment foci over the bed (+5 dice), a Rating 4 sorcery library with the ritual and all "
            "his spell formulas, Hard Cover 8 door. Three alarms shut the system down in 4D6 turns."
        ),
    },
    {
        "name": "Elby's Bar and Grill",
        "location_type": "bar",
        "district": "James Street and Ninth Avenue, Downtown (basement)",
        "security_level": "Patrolled / Commercial",
        "summary": "24-hour metahuman basement bar ('Humans welcome, too!') where Nick met Fayette; now a silent charnel house with 28 bodies in back",
        "description": (
            "Easy to walk past among the looming buildings and plate-glass storefronts: a silvery "
            "plaque marks the stairs down, open 24 hours, 'Humans welcome, too!' A narrow staircase "
            "past dank concrete scrawled with pen, then a smoky red room lit by a glowing 'Baer Beer' "
            "sign over the credit-registry machine, tables in rows, a black steel counter, a vibrating "
            "trideo game box in the corner and a simsense arcade game chirping for customers. Rind the "
            "troll bouncer is the adoptive father of the metahumans in this part of town; Nick's "
            "Double Devils congregate here. Astrally the room is dead but for anger, death and violence."
        ),
        "notes": (
            "Arhill's orks scouted, then raided: everyone inside -- including Bart of the Knights -- "
            "was taken to the back room and killed, twenty-eight bodies, the evidence tidied. Lights "
            "on, nobody in or out for a day (street rumor). Farnwell watches in astral form and fetches "
            "the orks from The Quick, the Dead, and the Still Moving; loiter and they ambush here. "
            "Perception (4): a spent cartridge. Electronics (5) on the registry: Nick and Fayette were "
            "regulars; three successes put both here the night she vanished. Napkins from here are "
            "Nick's stationery. Debugging: Bart alive but near death in a back room; Rind and half a "
            "dozen troll brothers (Troll Bouncer stats) arriving to ask the runners' business. The alley "
            "behind is where captured runners wake up with tracking disks. Bar map: Sprawl Sites p.12."
        ),
    },
    {
        "name": "The Quick, the Dead, and the Still Moving",
        "location_type": "bar",
        "district": "Pine Street (ork section), Downtown",
        "security_level": "Low Security",
        "controlling_org": "Rat Mash Dancer's Mercenaries",
        "summary": "Trog bar under a real skull with pink-lit eye sockets; a mercenaries' office with war maps and pinned jobs",
        "description": (
            "A real skull hangs from the sign, its eye sockets lighting up from pink bulbs in the "
            "cranium. Through a brick anteroom past an enormous troll bouncer and several dozen flies "
            "into loud, angry, chaotic music nobody listens to. A bulletin board in one corner carries "
            "maps of regions of ongoing warfare, pins stuck in the hot spots; the bar serves almost as "
            "an office for cutthroats and mercenaries. Bar, office, store room, booths, stage, dressing "
            "room, meeting room (map p.24)."
        ),
        "notes": (
            "Ask about 'business' and the bartender points at the maps. The big job: Salish territory, "
            "'airmobile insertion', a tan/yellow pin near North Cove; only regulars know the pin colors "
            "(Etiquette (Mercenary) 4 or (Street) 8): independent job, Aztechnology links rumored. A "
            "contact number on a corner table reaches a Senior Technician at Juzu Clinic ('all spots "
            "are taken'); Perception (3) with the LTG directory traces it. Six of Rat Mash Dancer's "
            "orks clean guns at the big table while she assenses for Farnwell; the troll bouncer knows "
            "them and intervenes only if the runners are winning. The Juzu Clinic Matrix trace rings a "
            "telephone here. Legwork calls it 'one of those trog bars downtown'."
        ),
    },
    {
        "name": "Cratchit's Family Entertainment",
        "location_type": "shooting range / family entertainment center",
        "district": "Maple County neighborhood, Auburn",
        "security_level": "Low Security",
        "controlling_org": "High Chivalrous Order of Humanis Policlub",
        "summary": "'Soy-Ice, Miniature Golf and Guns-Guns-Guns' behind chain-link and placards; Humanis den in the back room",
        "description": (
            "A chain-link fence, garishly painted placards, and a flickering neon sign: 'Cratchit's "
            "Family Entertainment. Soy-Ice, Miniature Golf and Guns-Guns-Guns.' Soy-chip bags and gray "
            "sand skitter past the gate. Soy-Ice half a nuyen a cone; a miniature golf course laid out "
            "like a section of the Matrix, one nuyen a round; and the automatic-weapons range where ten "
            "nuyen buys five shots (AK-97, Uzi III, an H&K variant, AK-98, Ingram Valiant, a military "
            "heavy machine gun; Walther Palm, Roomsweeper or Browning Max-Power for the subtle) at "
            "man-shaped targets -- a stubby dwarf with a wrench, a moronic ork, and Lord Erindil, "
            "Tir Tairngire's spokes-elf. The back room: towers of ammunition boxes, scuffed chairs "
            "around a homemade altar, five brawny men at a trideo-poker machine in filthy T-shirts, one "
            "cap reading 'Kill 'em all. Period.'"
        ),
        "notes": (
            "Busiest in late afternoon with families. Firearms (4) to hit; TN 10 to shoot only the "
            "points off Lord Erindil's ears wins a FabriSoft raccoon giving a fascist salute, a "
            "feathered serpent with a plastic ork in its jaws, or a polar bear with a toothbrush "
            "mustache. Cratchit sneers at metahuman customers, guffaws with humans about the Mariners "
            "and the elven pitcher Ellsley, bellows 'You can that!' at any mention of the policlub, and "
            "takes anyone who whispers 'purity' into the back. Astral scouting meets no resistance "
            "unless the wage-mage Knight is present. Map p.22."
        ),
    },
    {
        "name": "Double Devils' Tire Dump",
        "location_type": "gang territory",
        "district": "Filbert-Maltby Road, northern Snohomish (near Thrasher's Corner)",
        "security_level": "No Security / Barrens",
        "controlling_org": "Double Devils",
        "summary": "Dunes of plastic bottles and oozing barrels converging on a mountain of wire and shredded rubber; the elves' vans are buried inside it",
        "description": (
            "The ground gives way to a huge dump: dunes of plastic bottles and disposable packaging, "
            "oozing barrels protruding from the debris, everything converging on a mountain of twisted "
            "wire and shredded rubber. Inside the mountain, a semi-open area where the debris was piled "
            "over a group of vans and campers the gangers live in; near the back, Nick's small "
            "Chrysler-Nissan Open Trail minivan full of soiled clothes, hardcopy pop media and a dozen "
            "Stayfresh stuffer wrappers. Map p.26."
        ),
        "notes": (
            "Perception (4) in Nick's van: a water-stained hardcopy North Cove map under a carpet mat, "
            "Shoalwater circled in red. Approach wrong and the Devils take the team for a squatter raid: "
            "Shark in the yellow crusher (4D4 to anyone run over), gangers shooting from rubbish piles "
            "and grabbing bikes, buried booby-trap grenades. Defeated or charmed, they talk. Street "
            "rumor places the gang 'in the tire dump by Route 12'."
        ),
    },
    {
        "name": "Seattle-Tacoma Airport (Sea-Tac)",
        "location_type": "transportation hub",
        "district": "Sea-Tac",
        "security_level": "Corporate High Security",
        "summary": "Cavernous international airport; the Native American Airways commuter lounge, an ork with leaflets, and the ticket registry",
        "description": (
            "Aircraft roar down the runways outside; within, dark-suited sararimen wait for baggage or "
            "buy tickets from blinking autoclerk machines. A lounge serves small-plane commuters to "
            "Salish territory, next to the Native American Airways terminal, where an overweight ork "
            "in black shades shamefacedly presses Mothers of Metahumans leaflets on travelers. X-ray "
            "machines at the gates and a hundred security guards (Corporate Security Guard stats, "
            "partial armor, H&K 227 SMGs) who exist to prevent hijacking, not to referee scuffles."
        ),
        "notes": (
            "The ork is Rat Mash Dancer's seventh (Ork Mercenary stats, palm pistol and knife only); "
            "pick his pockets for Fayette's photo and the underlined King's Glen schedule. Guards "
            "ignore a minor scuffle, break up a melee, and overlook small imbroglios for 200 nuyen and "
            "a good excuse; heavy weapons drawn here mean overwhelming firepower and jail. Ticket "
            "machines can be used as terminals (Program Rating max 2) straight into the Ticket "
            "Registry subsystem (see Matrix systems). Later books call the airport by this name; the "
            "book says 'Seattle-Tacoma Airport'."
        ),
    },
    {
        "name": "Virtual Meetings Incorporated (Seattle Facility)",
        "location_type": "corporate facility",
        "district": "Seattle (address not given); three-storey atrium",
        "security_level": "Corporate Standard",
        "controlling_org": "Virtual Meetings Incorporated",
        "summary": "VMI's Seattle iconferencing center: nervous receptionist, glad-handing corporator, leather couches and senselink headgear",
        "description": (
            "Automatic doors into a three-storey atrium where the receptionist barely keeps her hand "
            "off the PANICBUTTON at the sight of shadowrunners; a side door; a wide-grinned, "
            "dark-suited corporator blathering about privacy, security, quality and perceived image "
            "resolution; a modern room of plush reclining leather couches, technicians resolving "
            "multi-band visuals into icons and offering tranquilizers to the magically active; ornate "
            "headgear for some, datajack adaptors for the rest. Then teak, a vaulted ceiling, deep "
            "carpet, gold-brushed walls hung with priceless Impressionists, an antique telephone on the "
            "side table, ice water that is cool and refreshing, and one door participants seem to "
            "enter by."
        ),
        "notes": (
            "The virtual room is a construct on VMI's system, not a Matrix host the runners can deck; "
            "Analyze on the Diana icon reveals nothing (Analyze never reads other personas). Marti's "
            "arrival makes the walls bend 'under the laws of pure mathematics rather than physics'. "
            "Runners abusing 'Diana' may see her crash the VMI system with the deck's combat programs "
            "in frustration."
        ),
    },
    {
        "name": "Zappy Zed's Trideo Kiosk",
        "location_type": "shop",
        "district": "Bellevue, a few blocks from Rhododendron Conservatory (per the prologue)",
        "security_level": "Patrolled / Commercial",
        "summary": "Neon-lit trideo kiosk where a lost Fayette walked the block until a Lone Star cruiser IDed her and drove her back to school",
        "description": (
            "An entertainment kiosk in the neon rainbow of the plex where Fayette, having ducked into a "
            "soy bar to dodge an off-duty school guard and taken a wrong street on her first escape, "
            "found herself instead of at Elby's -- walking up one street and down the other, looking "
            "more out of place than she hoped, until a blue Lone Star patrol vehicle stopped, IDed her, "
            "and carted her back to the Conservatory with advice about that part of the plex."
        ),
        "notes": (
            "Maya saw the pickup ('Slot, but it was a chuckler'). School files record only that Lone "
            "Star 'found her behind an entertainment kiosk'. Book inconsistency: the prologue implies "
            "this is walking distance from the Conservatory in Bellevue, while Elby's is downtown; "
            "place the kiosk wherever the campaign's geography needs it."
        ),
    },
    {
        "name": "Shoalwater",
        "location_type": "residential community",
        "district": "Shoalwater, North Cove (Pacific coast, former Shoalwater Indian reservation)",
        "city": "North Cove, Salish-Shidhe Council",
        "security_level": "Low Security",
        "controlling_org": "Shoalwater Elven Community",
        "summary": "Rocky outcrop between a tidal inlet and wooded fields: solar roofs, one-armed windmills, vegetable gardens, and a crashed thunderbird in the stream bed",
        "description": (
            "The Shoalwater elven community sits on a rocky outcrop with a tidal inlet on one side and "
            "partially wooded fields on the other. Solar panels and one-armed windmills sprout from "
            "clumps of forest; light gleams from passive-solar roofs; visitors nearly trample the "
            "vegetable gardens coming in. Half a kilometer off, nose-down at a steep angle in a stream "
            "bed under camouflage netting, lies the Charlotte, an older GMC Banshee-A4 thunderbird that "
            "took two chopper-launched AS-AAMs -- turret all but sheared off, autocannon, assault "
            "cannon and twin 10mm MMGs gone, drone racks empty. The 'elven lodge in Shoalwater' to the "
            "truck-stop crowd on Route 12."
        ),
        "notes": (
            "Map p.37 (Pacific Ocean / Shoalwater). Nick and Fayette arrive 3:00 p.m. on day one. "
            "Salvage: two twin-pack LG-AVM launchers (Electronics B/R or Gunnery B/R 6, base time six "
            "hours; laser designators on rifles or smartgun adaptors; 8D4 vs vehicles, 16D8 vs people; "
            "three reloads in Jac's room; too bulky to move once set) and a working radio on "
            "Salish-Shidhe Ranger Force frequencies -- convince the Rangers and a pair of Combat Mages "
            "arrive astrally in 1D3 turns. The raid, 2:30 a.m. at high tide on day five: false alarms "
            "first (forest-fire aircraft, whales, backfiring cars); an invisible infiltration team rows "
            "in from half a kilometer out (Perception TN = half the distance in meters), then two Hughes "
            "WK-2 Stallions (Handling 5, Speed 170/250, Body 6, Armor 2, Sig 5; twin chin LMGs, 6-pack "
            "HEM rack; two riggers each) land ten orks apiece, LMGs only near Fayette, everything at "
            "reinforcements. Shoalwater has several domains -- a wilderness shaman can seed each with "
            "a nature spirit. Fleeing puts the same fight on Interstate 12 between log roadblocks."
        ),
    },
    {
        "name": "King's Glen Airstrip",
        "location_type": "transportation hub",
        "district": "King's Glen, North Cove",
        "city": "King's Glen, Salish-Shidhe Council",
        "security_level": "Low Security",
        "summary": "Two runways and a one-building terminal on North Cove, served by Native American Airways from Sea-Tac; Fayette's unused destination",
        "description": (
            "A small airstrip in the North Cove area of Salish-Shidhe territory, southwest of Seattle: "
            "two runways and a single-building passenger terminal, serviced by Native American Airways "
            "commuter flights from Sea-Tac. The nearest airport to Shoalwater."
        ),
        "notes": "Runners who actually fly here can meet a Shoalwater resident working as an attendant who will point them the right way. Fayette booked the flight three months ago and never took it; Nick will not fly.",
    },
    {
        "name": "Interstate Routes 12 and 101 (Seattle to North Cove)",
        "location_type": "highway",
        "district": "Salish-Shidhe territory west of Seattle",
        "city": "Salish-Shidhe Council",
        "security_level": "Low Security",
        "summary": "Black kilometers of tree-screened highway through Salish trading country: Border Patrol stops, Blue Tickets, truck stops, and the roadblock ambush",
        "description": (
            "A curtain of trees screens the Salish territories from the black kilometers of Interstate "
            "Route 12; the occasional long-haul rig lumbers past while battered station wagons and "
            "pickups of tribal holdings own the road, and when the breeze blows from the north you can "
            "smell the Pacific. Routes 12 and 101 stay open under the Salish-Shidhe, who traditionally "
            "live as traders. Roadside truck stops, riggers, and bands of tribesmen holding impromptu "
            "parties after long hours on the road."
        ),
        "notes": (
            "A Border Patrol (four Former Tribal Warriors in a Chrysler-Nissan patrol vehicle; camo "
            "armor clothing, Browning Max-Powers, an Enfield AS7 and two Remington 750s) stops the "
            "runners about 30 km out: no Blue Ticket from the metroplex Council Lodge means a 200-nuyen "
            "fine and an escort back; narcotics and non-hunting weapons are confiscated. Kill warriors "
            "and nearly the whole Salish population becomes an enemy (3D6 Tribesmen). Warn them of the "
            "raid and they shake their heads: 'This is not the way in our land.' Etiquette (6) at a "
            "truck stop: city types going west; an elf and a pinkskin girl on a bike whose name is on "
            "the tribal registry; then suits and razortypes dropping yen on the patrols; wetwork at "
            "Shoalwater at [the schedule's time]. The road ambush: log roadblocks a kilometer ahead and "
            "behind (Strength 6, 30 minutes), 35-meter cleared embankments, 1D6 Tribesmen in pickups "
            "and a Patrol in 1D6 turns firing at both sides (Leadership 5 to win them over)."
        ),
    },
    {
        "name": "Seattle Aquarium",
        "location_type": "landmark / monument",
        "district": "Waterfront, Downtown",
        "security_level": "Patrolled / Commercial",
        "summary": "Where Governor Schultz convened a bare-quorum Metroplex Council at 1:00 a.m. to pass her auto-ownership tax order (June 2051 news)",
        "description": "The Seattle Aquarium on the downtown waterfront -- a public attraction and, in June 2051, the venue of a highly irregular 1:00 a.m. Metroplex Council meeting.",
        "notes": "'Something Fishy in Council' (June 8, 2051): only a bare quorum attended and unanimously approved Governor Marilyn Schultz's controversial executive order on auto ownership taxes. 'I might start holding all the Council meetings that way.' Not otherwise used in the adventure.",
    },
    {
        "name": "Me 'n' My Shadow",
        "location_type": "nightclub",
        "district": "Seattle (district not given)",
        "security_level": "Patrolled / Commercial",
        "summary": "Dance club where a melee erupted over a ban on wearing 'any living animal life form' as jewelry (June 2051 news)",
        "description": "A Seattle dance club fashionable enough that patrons wear live animals as jewelry -- until management banned 'any living animal life form' and a melee erupted.",
        "notes": "Entertainment item in both June 8, 2051 handouts. Texture for a night on the town.",
    },
    {
        "name": "Club Zor",
        "location_type": "nightclub",
        "district": "Seattle (district not given)",
        "security_level": "Patrolled / Commercial",
        "summary": "The popular watering hole where Concrete Dreams turn up unannounced and Lone Star has to control the crowd",
        "description": "'The popular watering hole known to regulars as Club Zor', where the megafamous Concrete Dreams appeared unannounced in June 2051 and drew several hundred people with no advance publicity.",
        "notes": "Lone Star was called in for crowd control. A place to run into the band, a fan riot, or a Concrete Dreams T-shirt licensing dispute.",
    },
]

NPCS = [
    {
        "name": "Fayette Myers",
        "role": "Runaway heiress, Diana's daughter, the heart Anton d'Venescu must offer the Aztec gods; sharper than her guardians know",
        "archetype": "Student / Heiress",
        "title": "Rhododendron Conservatory boarder; born Fayette d'Venescu; a named member of the Salish-Shidhe Council",
        "race": "Human",
        "gender": "Female",
        "age": 16,
        "connection": 2,
        "description": (
            "Unremarkable at first glance: eyes on the floor, shy and forlorn, lank curls, chewing her "
            "nails. With friends she comes alive -- flashing blue eyes (hazel in the prologue), an "
            "appealing grin, a sly devilish chuckle. Sandy-blond hair worn loose that curls in damp "
            "weather; jeans and sweaters, or a denim skirt when the occasion demands; 1.6 m, 53.6 kg. "
            "Deceptively quiet, sharp-minded, with a taste for excitement and Strawberry Spurs in "
            "Seattle's underworld clubs, mixing with metahumans. Loves Nick and says so to everyone; "
            "bound to Aunt Marti and Shoalwater; snaps an insult and hides tears if told she brought "
            "disaster on the elves."
        ),
        "background": (
            "Born to Aztechnology mage Anton d'Venescu and the decker Suzanne Vann ('Diana'). Her "
            "father tried to sacrifice her as a baby; her mother got her to Aunt Marti at Shoalwater "
            "and died for it. Raised in the elven commune under a Salish-Shidhe name; sent to Seattle "
            "at fourteen as Fayette Myers with a laundered Banque Orbitale de Suisse trust paying the "
            "tuition. Her aunt told her the story of her mother's death only when she left for school. "
            "Placid at first, she developed a riotous social life, met Nick at Elby's, and grew "
            "terrified of the school and of Dr. Arhill -- 'I think I corrupted her real good,' Nick "
            "says, but it was her idea to run. First escape three months ago ended with Lone Star and "
            "a Juzu examination that left her 'shaking like a wired mouse'; the second is this "
            "adventure."
        ),
        "notes": (
            "Stats (p.48): B3 Q4 S2 C4 I4 W5 Ess 6 R4; Bike 2, Stealth 4, Etiquette (Elven) 4 / (Street) "
            "3 / (Upper Class) 1, Firearms 1, Unarmed 2; 10 Karma banked; credstick with 1,000 nuyen, "
            "Streetline Special. Investments worth 1.5 million nuyen (10 percent a year, not "
            "convertible) held by Marti until she is 21. Will not be separated from Nick; can be "
            "coached in a skill while waiting for the raid; Arhill's Sleep spells are meant for her. "
            "Aftermath: sent back to the Conservatory, fails everything, expelled, finds Nick; an "
            "excellent permanent contact or even a patron -- she knows people in the sprawls, the "
            "tribes and the moneyed elite. A runner may remember glimpsing her in one of the team's "
            "haunts. Age is inferred: about five 'over ten years ago', sent to school at fourteen."
        ),
        "contact_skills": ["Rhododendron Conservatory and Seattle's corporate-heir set", "Shoalwater and the Salish-Shidhe registry"],
    },
    {
        "name": "Nick Voigt",
        "role": "'Crazy Nick' -- eighteen-year-old elven go-ganger who loves Fayette, fears flying, and threw away the Double Devils for her",
        "archetype": "Go-Ganger",
        "title": "Former Double Devil; Fayette's boyfriend",
        "race": "Elf",
        "gender": "Male",
        "age": 18,
        "connection": 2,
        "description": (
            "A wiry six feet in the synthetic leathers of his go-gang, a cropped shock of hair standing "
            "straight up over a filthy bandanna, the world viewed with irony through half-open eyes, a "
            "roguish crooked smile for Fayette; pale, with a square firm jaw and eyes that flash blue "
            "when angry. Witty, glib, delightfully irreverent; fights or sulks when things do not go "
            "his way. Show him the street courtesy due any belligerent ganger. Loyal to Fayette, his "
            "metahuman chummers from the street, and not much else."
        ),
        "background": (
            "Bad family life from the start; on the streets more than at home by fourteen; at eighteen "
            "the sprawls are the only home he knows. Ran with the Double Devils until a human girl "
            "shattered his bonds with the gang. He sat down next to Fayette at Elby's half daring her "
            "to insult elves; she understood them perfectly, and he became her thrilling street "
            "companion, showing her the ropes and bringing her to Rind. Planned the airport, then wrote "
            "'WE'LL USE THE RAPIER' on an Elby's napkin because he cannot face flying. Bought a "
            "twelve-moon Blue Ticket last week."
        ),
        "notes": (
            "Stats (p.53): B5 Q6 S6 C6 I5 W4 Ess 6 R5; Armed Combat 5, Bike 4, Etiquette (Elven) 1 / "
            "(Street) 4, Firearms 6, Unarmed 6; armor vest, Colt America L36, survival knife, Yamaha "
            "Rapier; a Chrysler-Nissan Open Trail minivan at the dump. Fights as well as any runner. "
            "Any male runner's move on Fayette makes him erupt and try to flee with her regardless of "
            "the raid. He and Marti are due a terrible fight; she dismisses him afterwards, and Fayette "
            "finds him again."
        ),
        "contact_skills": ["Snohomish go-gang scene and the Double Devils", "Metahuman bars (Elby's, Rind)"],
    },
    {
        "name": "Marti Vann",
        "role": "'Martha Newblood' -- Shoalwater's brisk, bossy elven spokesperson; Diana's sister, Fayette's guardian, and the 'AI' Johnson",
        "archetype": "Community Leader",
        "title": "Spokesperson, Shoalwater Elven Community; trustee of Fayette's 1.5-million-nuyen fund",
        "race": "Elf",
        "gender": "Female",
        "organization": "Shoalwater Elven Community",
        "connection": 4,
        "description": (
            "A willowy elven woman who looks about twenty-five, lustrous black hair in a bun, low-light "
            "eyes, a nuisance allergy to iron. Years of presiding over Shoalwater have made her brisk "
            "and slightly bossy: she defers to the runners in their own field and corrects them on "
            "everything else. Old-fashioned mores for 2051, especially regarding young men on "
            "motorcycles -- Nick being an elf may soften her. Behind Diana's icon she moves "
            "falteringly, speaks with difficulty, and fades out instead of disconnecting."
        ),
        "background": (
            "Joined the Shoalwater elven community shortly after puberty, never an idealist but at home "
            "with its ecology and its distrust of corporate Seattle; earned prestige selling computer "
            "programs for the tribe and became spokesperson. Her younger sister Suzanne married Anton "
            "d'Venescu; three years later he murdered her. With Suzanne's code numbers Marti pulled "
            "several million nuyen out of Anton's Aztechnology accounts, hid the child in the "
            "electronic confusion Suzanne left behind, took the name Martha Newblood, bought the "
            "'Fayette Myers' identity and the Conservatory place, and waited for the day she would have "
            "to deal with Anton. Legwork has her arriving at Shoalwater with a five-year-old 'over ten "
            "years ago'."
        ),
        "notes": (
            "Stats (p.52): B2 Q5 S2 C5 I5 W4 Ess 5.5 R5(9); Projectile Weapons (Bow) 4, Computer 2, "
            "Computer Theory 1, Etiquette (Tribal) 6 / (Elven) 6 / (Street) 2 / (Corporate) 2, "
            "Leadership 2, Negotiation 3; Hacking pool 11; datajack, 30 Mp headware memory; microtronics "
            "workshop, tabletop computer. Diana's deck: Fuchi Cyber-4 equivalent with Response Increase "
            "2 and Diana's custom MPCP chips (Bod 6, Evasion 6, Masking 6, Sensors 7, Attack 3, Evaluate "
            "5, Sleaze 5) -- she runs it as a Tortoise by keyboard under simsense headgear, Transit in "
            "Auto-Evade to get anywhere, and would rather be taken for a legend than change the icon. "
            "Offers 10,000 each up front and 20,000 on Fayette's safe return (Negotiation +/-5 percent "
            "per success), never mentions Aztechnology or Anton, and does not know Fayette is already on "
            "her way to her. Never admits to the runners that she was Diana (tells Fayette later). "
            "Fights with a runner's skill in the raid; wants Fayette protected from Anton and from Nick."
        ),
        "contact_skills": ["Shoalwater and the North Cove elven communes", "Salish-Shidhe tribal etiquette and registry", "Diana's legacy programs and MPCP"],
    },
    {
        "name": "Anton d'Venescu",
        "role": "Aztechnology's fallen star conjurer -- wife-murderer, drug-initiate of an Aztec power, hiding from devil flies under Juzu Clinic and hunting his daughter's heart",
        "archetype": "Corporate Mage (burned out)",
        "title": "Project supervisor, Aztechnology Branch 45-Tlaloc; 'Cacodemon Debt Default Syndrome' patient",
        "race": "Human",
        "gender": "Male",
        "organization": "Aztechnology Tlaloc Division",
        "connection": 4,
        "description": (
            "Once a dashing figure, now showing months in an isolation chamber: sagging muscles, a "
            "sharp jaw drooping listlessly, olive skin pasty under artificial light, a black goatee "
            "with fuzz sprouting untended from the rest of his chin, a sweeping armored coat over a "
            "conventional dress shirt, trousers and tie. Speaks in the suave tones of a man used to "
            "power; every word serves the pursuit of Fayette -- to hire, to delude, to learn. Knows not "
            "to trifle with the Aztec gods and has no other honor or duty; the notion that he should "
            "regret killing his wife or hunting his daughter gets a puzzled laugh. If the end comes he "
            "curses the runners and his gods in the same breath."
        ),
        "background": (
            "The ideal corporate mage, able to enslave the nether powers with a lawyer's dispassion, "
            "destined for the top of Aztechnology; a shamanic-tradition magician whose superiors "
            "rushed to fund his 2034 research into the Aztec drugs of magic. Under ocapatli he "
            "believes he contacted Patecatl (or the rain god, says the street), was initiated into a "
            "long-forgotten cult, and bound himself to sacrifice a mother-daughter dyad. He married the "
            "ace decker Suzanne Vann to enhance his career, then decided killing her and their baby "
            "would enhance it further; she hid the child, evaded him for days, and he impaled her in a "
            "coffin motel. The sacrifice incomplete, his magic gone (ATC psychologists call it a "
            "self-induced block; he calls it proof), he has spent years beneath Juzu Clinic behind "
            "malon vapor, a ward, enslaved elementals and spirit foci, certain the Aztec spirits will "
            "tear his soul out within months if Fayette is not delivered."
        ),
        "notes": (
            "Stats (p.49): B3 Q3 S1 C6 I6 W3 Ess 6 Magic (6, unusable) R4; Archaeology 5, Conjuring 8, "
            "Etiquette (Aztechnology) 4, Firearms 2, Magical Theory 8, Sorcery 8; no astral or magic "
            "pools. Armor clothing (an armor vest with plates on p.35); Mossberg CMDT with APDS and an "
            "underslung launcher, six IPE defensive grenades. Spell foci he cannot use: an engraved "
            "diamond lens (Illusion 2), a golden Aztec calendar replica (Manipulation 2), an obsidian "
            "sacrificial knife (Spirit 2). Terrified of fighting without magic; joins the Shoalwater "
            "infiltration team anyway. His chamber's library holds every spell formula and the ritual's "
            "gruesome details. Poison his ardone patches and he uses one in 1D6 days. Dies horribly of "
            "the spirits or of his own belief within months if he fails; alive, he comes back with "
            "Aztechnology's resources for a sequel. Aztechnology would prefer to forget him."
        ),
    },
    {
        "name": "Dr. Arhill",
        "role": "Cold, humorless Practitioner of Essence Medicine who runs Juzu Clinic, cures megacorp mages, and will murder a girl to save his one friend",
        "archetype": "Hermetic Mage / Physician",
        "title": "Senior physician, Juzu Clinic; Initiate (Grade 2); Anton d'Venescu's doctor and partner",
        "race": "Human",
        "gender": "Male",
        "organization": "Juzu Clinic",
        "connection": 4,
        "description": (
            "Balding, gleaming-skinned, thick glasses, a long thin nose, a lab coat; in the prologue "
            "he examines Fayette from a wheelchair in a clinic full of cybernetic legs. Always seems "
            "distracted, stealing glances at some irrelevant chart or vidscreen -- on purpose, to "
            "discourage people from bothering him. Cold-blooded and humorless: he wants to study magic "
            "and diseases and settles for magicians and people who have them. The headmaster calls him "
            "'rather distant'."
        ),
        "background": (
            "Broke his own rule against emotional involvement with a patient when he befriended Anton "
            "d'Venescu -- perhaps he saw himself in a man who would kill his loved ones for magic, "
            "perhaps after years of lonely practice he wanted someone to talk clinical pathology with. "
            "Watched a girl at a Seattle private school for years as a candidate for 'your project', "
            "examined her three months ago after her first escape, confirmed the DNA match, wrote "
            "Aztechnology Branch 45-Tlaloc that 'she is, without a doubt, d'Venescu's daughter', and "
            "took their money to complete the sacrifice. Hopes saving this one patient will make up for "
            "years of cold disinterest toward all the others."
        ),
        "notes": (
            "Stats (p.50): B2 Q3 S2 C2 I6 W6 Ess 6 Magic 8 R4; Biology 6, Biotech 5, Cybertechnology 6, "
            "Conjuring 6, Enchanting 4, Etiquette (Aztechnology) 6, Firearms (Pistols) 4, Magic Theory "
            "8, Sorcery 5; Grade 2 self-initiate, no geasa; Magic pool 5 (11 with the Power Focus 6); "
            "armor clothing, Walther Palm Pistol. Spells: Antidote Toxin 3, Cure Disease 4, Detox 3, "
            "Heal Wounds 5, Prophylaxis Deadly Pathogen 4, Chaotic World 5, Confusion 6, Mind Probe 7, "
            "Sleep 9. Keeps four Force 7 elementals under the clinic (with Aztechnology mages; not "
            "counted against his bound total), Watchers (Force 3) on Shoalwater's perimeter, and two "
            "interns as astral spies. Interrogates prisoners with tranq patches and Mind Probe, "
            "implants tracking disks under the shoulder blade, and releases them to be followed. "
            "Charges 1.5 times book prices; appointment 1D6 days and 500 nuyen. Leads the Shoalwater "
            "infiltration (Sleep on Fayette, invisibility, flee). Signs Memo 2 as 'Dr. Achill'."
        ),
        "contact_skills": ["Magical medicine for wage mages (cures that spare the Magic)", "Aztechnology Northwest medical and mercenary accounts"],
    },
    {
        "name": "Hortense",
        "role": "Arhill's first intern -- skinny, red-eyed doctor-in-training who reads parchment aloud and astrally fetches the orks",
        "archetype": "Magician (intern)",
        "title": "Intern in Mystic Medicine, Juzu Clinic",
        "race": "Human",
        "gender": "Male",
        "organization": "Juzu Clinic",
        "connection": 1,
        "description": "Young and skinny with bulging eyes red from drudgery on Dr. Arhill's projects; the much younger man standing beside Arhill's terminal reading from a sheet of parchment. Without Arhill's directions he and Farnwell look at each other in confusion and avoid anything that might get them in trouble. Obeys unquestioningly.",
        "notes": (
            "Intern block (p.51): B4 Q4 S1 C1 I6 W4 Ess 6 Magic 6 R5; Biology 3, Biotech 6, Conjuring 3, "
            "Cybertechnology 2, Firearms 2, Magical Theory 3, Physical Sciences 4, Sorcery 4; Ares "
            "Crusader, armor vest, Power Focus 3; Chaotic World 4, Confusion 4, Heal Moderate Wounds 3, "
            "Sleep 5. Arhill hands him a 'note' that sends him to a recovery room to project astrally to "
            "The Quick, the Dead, and the Still Moving; follows tracked runners astrally in brief "
            "visits; stuns and distracts rescuers at Shoalwater."
        ),
    },
    {
        "name": "Farnwell",
        "role": "Arhill's second intern -- astral watcher at Elby's whose projection is a tall imperious surgeon and whose body is a shrunken kid with glasses askew",
        "archetype": "Magician (intern)",
        "title": "Intern in Mystic Medicine, Juzu Clinic",
        "race": "Human",
        "gender": "Male",
        "organization": "Juzu Clinic",
        "connection": 1,
        "description": (
            "On the astral plane: a tall man pacing Elby's in a white coat hung loose over the "
            "snappiest of corporate suits, laser scalpels and rubber tubing in a pocket, a credstick "
            "chained in gold to his belt, great depth of wisdom in imperious eyes. In the flesh: a "
            "shrunken young man motionless on a recovery-room bed in lab coat, trousers and shoes, "
            "glasses askew. The gap is laughable."
        ),
        "notes": (
            "Intern block as Hortense (p.51). Watches Elby's in astral form between rests, races to the "
            "ork bar at full astral speed when anyone arrives, and guides the mercenaries to the "
            "ambush. Runs for his body at Juzu if attacked astrally, and knows a nearby apartment "
            "complex well enough to lose pursuers physically. Captured, he answers questions and "
            "deflects anger with ironic jokes about Dr. Arhill -- his license depends on Arhill, but he "
            "will not die for him. 'Farmwelll' in the table of contents."
        ),
    },
    {
        "name": "Rat Mash Dancer",
        "role": "Cascade ork Coyote shaman who mothers a band of mercenaries with a powerball; the biggest ork at the table and the brains of Arhill's hired muscle",
        "archetype": "Shaman (Coyote) / Mercenary Leader",
        "title": "Leader, Rat Mash Dancer's Mercenaries (Cascade ork)",
        "race": "Ork",
        "gender": "Female",
        "nationality": "Cascade Ork (Salish-Shidhe Council)",
        "organization": "Rat Mash Dancer's Mercenaries",
        "connection": 3,
        "description": (
            "A hairy, narrow face and a squat build; a coarse black skirt beneath a camouflage-pattern "
            "armor jacket; a knotted braid down her back ornamented with feathers and spent cartridges "
            "(brass cases woven into dreadlocks in the bar scene). Every few moments her head lolls "
            "back and she sits rigid, assensing for Farnwell: 'Nuttin' again. Wish these freaks would "
            "slot and run.' Despises nearly everyone in the city -- 'Breeders, execs, vatjobs... let "
            "'em chew drek' -- but likes their money. Almost motherly toward her band and harsh with "
            "them because Seattle would eat them otherwise; ork player characters may bring out the "
            "maternal instinct unless she pegs them as enemies. Loyal to herself and her orks, and "
            "knows enough never to betray an employer."
        ),
        "notes": (
            "Stats (p.55): B5 Q3 S3 C4 I4 W6 Ess 6 Magic 6 R3; Armed Combat 4, Conjuring 6, "
            "Enchantment 4, Etiquette (Corporate) 2 / (Street) 3 / (Tribal) 4, Firearms 8, Magical "
            "Theory 3, Rotor Craft 3, Sorcery 6, Stealth 6, Unarmed 6; Magic pool 6 (10 with the Power "
            "Focus 4). Spells: Mana Bolt 4, Powerball 6, Sleep 7. AK-97, armor jacket 5/3, sword with "
            "Cascade ork traceries (Weapon Focus 3, Reach +1), two Neuro-Stun VIII gas grenades. Her "
            "tribal status, her knack for finding jobs and her powerball keep the orks in line. Not "
            "listed on the Shoalwater helicopters (those are archetype orks); use her as the GM sees fit."
        ),
        "contact_skills": ["Cascade ork mercenaries for hire", "Mercenary job board at The Quick, the Dead, and the Still Moving"],
    },
    {
        "name": "Rind",
        "role": "Well-respected troll bouncer at Elby's, adoptive father to the metahumans of his part of town; knows everything about Nick and Fayette",
        "archetype": "Troll Bouncer",
        "title": "Bouncer, Elby's Bar and Grill",
        "race": "Troll",
        "gender": "Male",
        "connection": 3,
        "description": (
            "Two enormous warty hands on your shoulders and an oversized head shaking slowly: 'Hold on "
            "there, chummer. Chiller down. What's your drek?' When Rind talks you listen, if you want "
            "to keep your ears. Considers himself adoptive father to the other metahumans in his part "
            "of the city; tries to pull brawlers apart, calling futilely for order; will 'see if I can "
            "make 'em any worse'. Told Nick that a rich girl would never leave a life in the sun for scum "
            "like the two of them."
        ),
        "notes": (
            "Troll Bouncer stats (SR p.173), as do his half-dozen 'brothers'. Not among the twenty-eight "
            "dead at Elby's -- the book keeps him as the GM's lifeline: he can arrive at Elby's, or at the "
            "ork bar having worked out who did the shootings, wanting to know the runners' business, and "
            "he knows all about Nick, 'Fayette Myers' (not her past) and their plan to flee to "
            "Shoalwater."
        ),
        "contact_skills": ["Downtown metahuman street (Elby's regulars, the Double Devils)", "Six troll brothers for a fight"],
    },
    {
        "name": "Maya",
        "role": "Tiny, pasty trideo-game player at Elby's with datajacks drilled deep into her scalp; saw Lone Star cart Fayette off at Zappy Zed's",
        "archetype": "Bar Regular / Decker",
        "title": "Elby's Bar and Grill regular",
        "race": "Human",
        "gender": "Female",
        "connection": 1,
        "description": "A tiny woman with datajacks drilled deep into her scalp and a pasty face that sags into a smile, peering lazily around the trideo game box after losing again. Cheerfully calls Fayette 'the prettiest little tart you'll ever pick up' and 'the girl who kept scopin' out all the razorguys', which gets her slammed face-first into the machine by Nick and starts a general brawl.",
        "notes": "Prologue only. Witness to Fayette's first pickup near Zappy Zed's ('Slot, but it was a chuckler'). Fate after the ork raid is not stated -- one of the twenty-eight, or a survivor who was not there that night, at the GM's choice.",
    },
    {
        "name": "Raymond Blum",
        "role": "Plump, red-faced headmaster of Rhododendron Conservatory, tormented by Fayette and terrified of scandal; a confidant if you appeal to propriety",
        "archetype": "Corporate Official",
        "title": "Headmaster, Rhododendron Conservatory",
        "race": "Human",
        "gender": "Male",
        "organization": "Rhododendron Conservatory",
        "connection": 2,
        "description": "Plump and red-faced in a padded recliner behind a tidy desk; gulps and looks fiercely at strangers, then remembers that hospitality is an obligation of his class and praises his school without reserve, lamenting the difficulty of instilling 'breeding' under 21st-century mass society. Wipes his brow with a white handkerchief the instant anyone says Fayette.",
        "notes": (
            "Corporate Official stats (Sprawl Sites p.107) with Computer 2, Etiquette (Corporate) 4, "
            "Etiquette (Upper Class) 6, Leadership 3, Negotiation 4, Physical Sciences 1, Psychology 2, "
            "Sociology 3. Every runner in the room must pass Charisma or Persuasion (8) -- 5 if washed "
            "and suited, 3 if uncommonly well-heeled -- and the total successes become the TN for his "
            "Intelligence test to see through them. Won over, he gives every school file on Fayette, "
            "free run of students and faculty, 'the utmost confidence' in Juzu Clinic and admiration for "
            "the 'rather distant' Dr. Arhill. Sent Fayette to Juzu after her first escape, introduced "
            "Che-Che to Arhill after the second, and relays whatever Che-Che reports to Arhill a day "
            "later. His terminal is I/OP-1 of the Sorrel Hall system."
        ),
    },
    {
        "name": "Anita Wood",
        "role": "Rhododendron's Director, who does the real work behind a red plastic desk buried in datachips and mumbles about mailings when Fayette comes up",
        "archetype": "Corporate Secretary",
        "title": "Director, Rhododendron Conservatory",
        "race": "Human",
        "gender": "Female",
        "organization": "Rhododendron Conservatory",
        "connection": 1,
        "description": "Contends with the day's business behind a red plastic desk where piles of datachips and trinkets grow ever taller around the vid-terminal. Happily sets work aside to discuss admissions and 130,000-nuyen tuition; immediately mumbles about overdue mailings if visitors raise sensitive topics. Knows little about Fayette except that it is unwise to discuss her.",
        "notes": "Corporate Secretary stats (SR p.165). May give prospective 'parents' the school's public Matrix address. Her old-fashioned terminal is I/OP-2; anyone who watches her log in learns the access code and passwords, and anyone who gets her and Blake out of the room can sit down at it. Shuts the system down (two actions) on an External alert.",
    },
    {
        "name": "Mr. Blake",
        "role": "Tall, hairless, chiseled Director of Security who guards the Director's terminal like a hawk and buys threats by the bullet",
        "archetype": "Bodyguard",
        "title": "Director of Security, Rhododendron Conservatory",
        "race": "Human",
        "gender": "Male",
        "organization": "Rhododendron Conservatory",
        "connection": 2,
        "description": "A tall, hairless man at a small workstation at the back of the Main Office who may be a secretary but, from the muscles, chiseled features and arrogant grin, is not. Wanders into rooms where visitors have gone quiet with a cheerful 'Hallo' and the toughest questions that seem appropriate. Answers unwanted questions with 'We've got that matter nailed down, so ka?' and 'We don't need any outside help at this stage.'",
        "notes": "Bodyguard stats (Sprawl Sites p.97). Dual job: keep order and convince prospective parents no dangers exist. His one solution to the Fayette embarrassment is to cover it up; Cyndy calls him 'bent' on it. If hints fail he pays Dragon Ted 100 nuyen or so to hand the runners a Matrix-catalog receipt for monogrammed bullets bearing their initials (pulled from the Sorrel Hall security computer) with a sales brochure and a handwritten 'Mind your own business.' Guards Anita's terminal vigilantly unless deluded by magic or a fire elsewhere.",
    },
    {
        "name": "Dragon Ted",
        "role": "Local Bellevue street-ganger hired by Mr. Blake to deliver the monogrammed-bullet threat; sells his employer for 100 nuyen",
        "archetype": "Gang Member",
        "title": "Street-gang member (Bellevue)",
        "race": "Human",
        "gender": "Male",
        "connection": 1,
        "description": "A standard ganger waiting outside the Conservatory gate to hand one shadowrunner a receipt print-out and a brochure: 'Give him a bullet with HIS name on it. It's the perfect gift for that special someone.' No particular loyalty to Mr. Blake.",
        "notes": "Gang Member archetype (SR p.39). Reveals who hired him for 100 nuyen or if captured. Harm him and ten Gang Member archetypes in this part of Seattle become enemies.",
    },
    {
        "name": "Mr. Denn",
        "role": "Loud, big-bellied coach with a Nailhead hair spike who wants to be 'just another chummer' and will threaten to hose up faces",
        "archetype": "Corporate Security Guard",
        "title": "Coach, Dearpark Gymnasium, Rhododendron Conservatory",
        "race": "Human",
        "gender": "Male",
        "organization": "Rhododendron Conservatory",
        "connection": 1,
        "description": "A loud-mouthed, unimaginative fellow with a large stomach and a hair spike modelled on Nailhead the Urban Brawl star, affecting the manner of a combat-sports fan so his teenage students think him one of them. Lets nobody prowl the locker room without another official's permission and readily threatens to 'hose up faces'.",
        "notes": "Corporate Security Guard stats (SR p.165), no weapons. Accept his challenge and beat him and he is too embarrassed to report anything the party does. Fayette's locker is in his gym.",
    },
    {
        "name": "Cyndy",
        "role": "Twenty-three-year-old housemother with a party veteran's heavy eyelids who cannot be fooled, tolerates horseplay, and becomes a real ally",
        "archetype": "Rocker (retired)",
        "title": "Housemother, Fayette's suite, Oxus Hall, Rhododendron Conservatory",
        "race": "Human",
        "gender": "Female",
        "age": 23,
        "organization": "Rhododendron Conservatory",
        "connection": 2,
        "description": "Heavy eyelids, a jaded smile, a tiny Stim Boys decal on her office door, and a voluminous pocket with a Defiance Super Shock taser in it. Spent her adolescence doing exactly what she is now paid to guard the girls against, so she tolerates a little horseplay, is loved for it, and unfailingly scents out and squashes real infractions. Feign innocence and she answers with extremely perceptive guesses about your past exploits; catch her detecting a lie and you are out of the dormitory, by force if necessary.",
        "notes": (
            "Rocker stats (SR p.43), no cyberware; taser. Listens unobtrusively to 'private' talks with "
            "students. Convinced Fayette genuinely needs help, she becomes a trustworthy ally: Blake is "
            "'bent' on concealment, Grumblatt frets that Fayette is 'polluting the race' by dating an "
            "elf. On Fayette: 'That girl never ran wild... the smart, quiet type, who thinks before she "
            "gets into trouble. That means you gotta watch her most of all, so ka.' 'There's more to it "
            "than that, chummer.'"
        ),
        "contact_skills": ["Rhododendron faculty gossip and who is 'bent'", "Reading runners (ex-scene)"],
    },
    {
        "name": "Tanya Oko",
        "role": "Thin Japanese dorm princess in a rhinestone Dewine Dee bodysuit who elects the 'Most Razored Sir Samurai Guy' and hijacks every answer about Fayette",
        "archetype": "Student",
        "title": "Student, Rhododendron Conservatory; daughter of a Mitsuhama Assistant Technical Vice President",
        "race": "Human",
        "gender": "Female",
        "organization": "Rhododendron Conservatory",
        "connection": 1,
        "description": "A thin Japanese girl who thrusts herself forward and monopolizes the runners: 'Cybergear is just... so wizzer spectacky, am I right?' Her Dewine Dee bodysuit (left leg in rhinestones, right sleeve solid black) cost several thousand nuyen. Orchestrates impromptu elections for 'Most Razored Sir Samurai Guy' and 'Most Mysterious Mage'; does not like orks, trolls or dwarfs ('Oooh, like, wizzer blech'). Never liked the mysterious runaway and does not want her as a rival for attention.",
        "notes": "Street Kid stats (Sprawl Sites p.119), no skills. Daughter of a Mitsuhama Assistant Technical Vice President for Facilities Management. Interrupts and 'interprets' every answer: 'Fayette ran off with some go-gangers. What'd you expect from a loser? Anyway, you're a decker, with all those 'trodes, right?' The other girls admire her and let her run the conversation; quiet her and Anastasia talks.",
    },
    {
        "name": "Anastasia",
        "role": "Homely dorm gossip with an encyclopedic memory and a Fax-a-Tabloid theory that Tir Tairngire elves stole Fayette for a 'Seelie honeymoon'",
        "archetype": "Student",
        "title": "Student, Rhododendron Conservatory (Fayette's suite)",
        "race": "Human",
        "gender": "Female",
        "organization": "Rhododendron Conservatory",
        "connection": 1,
        "description": "A homely girl who keeps her place in dormitory society with an encyclopedic store of gossip and a knack for guessing secrets, told with accurate facial expressions and lurid anecdotes; when facts fail her she invents. In company she offers only the well-known rumors (an elven boyfriend named Nicholas); alone she has 'something nobody else can hear'.",
        "notes": "Street Kid stats. Her theory: Tir Tairngire sorcerers have revived bride abduction; Fayette knew everything about North Cove, her mother was assassinated in a mystic rite, so she is a princess of the pinkskin Salish whose family feuds with the High Prince, and the elves have scored a coup. ('And if the runners believe that story...') The true nuggets: Fayette never spoke of home, seemed to live with an aunt or with elves somewhere, and her mother died in a ritual.",
    },
    {
        "name": "Violeta",
        "role": "'Vi' -- suave Mexican charmer, the dorm's bad girl, daughter of an ex-Aztechnology shadowrunner; knew Fayette best and started her sneaking out",
        "archetype": "Student (street-wise)",
        "title": "Student, Rhododendron Conservatory (Fayette's suite)",
        "race": "Human",
        "gender": "Female",
        "nationality": "Mexican",
        "organization": "Rhododendron Conservatory",
        "connection": 2,
        "description": "Folds her arms and blinks her long lashes in amusement while the others talk; stays quiet lest anyone remember she was the one who first encouraged Fayette to break curfew and make covert visits to the sprawl. Sophistication and self-possession any runner would admire. Refuses to cooperate with anyone who does not show benevolent intent toward Fayette.",
        "background": "Raised by her mother, a disgruntled Aztechnology employee who left the company for the shadows; a few successful runs paid for the Conservatory, to keep the girl away from reprisals. Knows enough about ATC procedure to find an Aztechnology connection plausible the moment someone suggests it.",
        "notes": (
            "Rocker stats (SR p.43), no cyberware; Street Etiquette 5 -- negotiate with her as with any "
            "street contact (Opposed Street Etiquette; 100 nuyen or more flatters her, +2 to her TN). Her "
            "theory: Fayette 'crashed and burned' dealing dreamchips, came back from Juzu 'shaking like "
            "a wired mouse' and swore never to be examined again; 'Fayette's own dad pulled a wetjob on "
            "her mother -- she told me.' Knows Nick, his go-gang's haunt (Elby's) and his handwriting; "
            "calls Anastasia's fantasies 'drek'. Can roll on the Aztechnology legwork table as a contact."
        ),
        "contact_skills": ["Aztechnology procedure (second-hand from her mother)", "Sneaking off the Rhododendron campus"],
    },
    {
        "name": "Che-Che",
        "role": "Fayette's shy, plump roommate with purple-streaked hair who gave Fayette's secret stash to Dr. Arhill and reports everything to the headmaster",
        "archetype": "Student",
        "title": "Student, Rhododendron Conservatory (Fayette's roommate)",
        "race": "Human",
        "gender": "Female",
        "organization": "Rhododendron Conservatory",
        "connection": 1,
        "description": "Round cheeks, a plump body, wide blue eyes, streaks of purple dye she tried and failed to wash out, a heart-shaped pink pillow that beats when squeezed. Shies away whenever anyone looks at her, speaks no more than she must, and tries to divert attention to Tanya.",
        "notes": "Street Kid stats. After the second disappearance the headmaster introduced her to Dr. Arhill; under pressure she opened Fayette's secret place under a loose floor tile and handed over napkins and a Council Lodge Travel Bureau brochure on Salish-Shidhe lodging. Feels awful, which only weakens her; reports anything the party says or does to the headmaster, who tells Arhill a day later. Knows the aunt phoned every few days, that Fayette never called back ('Too dangerous'), and that the aunt called the morning Fayette vanished. Can identify what is missing from Fayette's things.",
    },
    {
        "name": "P. Grumblatt",
        "role": "Round-bodied, mustached math teacher and Humanis 'Chivalrous Knight' who spies on Fayette to save her from the 'dandelion-eater'",
        "archetype": "Humanis Policlub Member",
        "title": "Mathematics teacher, Rhododendron Conservatory; member of the High Chivalrous Order",
        "race": "Human",
        "gender": "Male",
        "organization": "High Chivalrous Order of Humanis Policlub",
        "connection": 2,
        "description": "A round-bodied instructor who purses his lips beneath his mustache, coughs, and lectures: 'we teachers are, if you will, sort of Daddy-figures' -- which makes Fayette start. Takes a paternal interest in her and fears a lecherous elf is leading her astray. To an all-human party that has let its interest slip: 'Lend me a couple of minutes. That poor girl needs our help.' Cannot look at Nick's photo without muttering about 'the absolute, shameless gall of these dandelion-eaters'.",
        "notes": "Humanis Policlub Member stats (SR p.168); Ruger Super Warhawk in his desk. Volunteered to escort Fayette to Juzu after her first escape. Began spying on her afterwards: keeps a color photocopy of the signed holopic 'With love, Nick' (Etiquette (Street) 3 spots Double Devils colors). Directs friendly humans to Cratchit's with the password 'purity'. Spot a metahuman among the runners, or insult his principles, and he turns curt, alerts the Knights, and they follow the team from the school -- physically or by Watcher -- to ambush and 'try' them.",
    },
    {
        "name": "Mr. Burg",
        "role": "Elderly Media Arts professor lost in 1990s two-dimensional television commercials",
        "archetype": "Teacher",
        "title": "Professor of Media Arts, Rhododendron Conservatory",
        "race": "Human",
        "gender": "Male",
        "organization": "Rhododendron Conservatory",
        "connection": 1,
        "description": "An elderly professor with an obsessive nostalgia for old-fashioned 2-D color television; a video player in his room continually reruns 1990s commercials for denture cleansers, oat-bran cereal and action figures.",
        "notes": "Human Pedestrian stats (Sprawl Sites p.116). Laments that Fayette was 'such a fine little student' until she 'caught the bug' and stopped studying. Platitudes otherwise.",
    },
    {
        "name": "Ms. Lee",
        "role": "Painfully thin Corporate Civics teacher who insists shadowrunning and wetwork are figments of the media's imagination",
        "archetype": "Teacher",
        "title": "Corporate Civics teacher, Rhododendron Conservatory",
        "race": "Human",
        "gender": "Female",
        "organization": "Rhododendron Conservatory",
        "connection": 1,
        "description": "A painfully thin Oriental woman who emphasizes to students and guests alike that 'so-called shadowrunning of data piracy and so-called wetwork are largely a figment of the media's imagination.' The runners may argue with her if they like.",
        "notes": "Human Pedestrian stats. 'Fayette was a fine girl. Such a shame.'",
    },
    {
        "name": "Ms. Primrose",
        "role": "Mousy young history teacher finishing a doctoral thesis on 'Unmarred Friendship: Japanese-American Brotherhood in the Mid-20th Century'",
        "archetype": "Teacher",
        "title": "History teacher, Rhododendron Conservatory",
        "race": "Human",
        "gender": "Female",
        "organization": "Rhododendron Conservatory",
        "connection": 1,
        "description": "A mousy young history teacher who teaches a non-controversial version of history from a text-chip titled 'Unmarred Friendship: Japanese-American Brotherhood in the Mid-20th Century' while completing her own doctoral thesis.",
        "notes": "Human Pedestrian stats. Platitudes about Fayette.",
    },
    {
        "name": "Leroy",
        "role": "Dawdling groundskeeper who let Fayette through the fence after curfew for six-packs from Elby's",
        "archetype": "Dock Worker",
        "title": "Groundskeeper, Rhododendron Conservatory",
        "race": "Human",
        "gender": "Male",
        "organization": "Rhododendron Conservatory",
        "connection": 1,
        "description": "Short black hair, brown eyes, and a preference for dawdling among the pines instead of working -- the figure glimpsed ducking into the branches. Accosted with weapons he dashes forward, hands up: 'Hey, don't get violent, chummer.' Then the runners explain to the guards why they drew on a harmless workman.",
        "notes": "Dock Worker stats (Sprawl Sites p.109), surprisingly. Knew Fayette well; helped her slip through the fence after curfew in exchange for six-packs from Elby's Bar and Grill. Shows the spot (Perception 5: light-blue synthetic threads) and points the way to Elby's if asked politely.",
        "contact_skills": ["The gap in the Conservatory fence"],
    },
    {
        "name": "Cratchit",
        "role": "Beer-bellied owner of Cratchit's Family Entertainment and 'a big man in the poli'; keeps the Chivalrous Knights' den and fires an Ingram Valiant at lulls",
        "archetype": "Humanis Policlub Contact",
        "title": "Owner, Cratchit's Family Entertainment; den keeper, High Chivalrous Order of Humanis Policlub",
        "race": "Human",
        "gender": "Male",
        "organization": "High Chivalrous Order of Humanis Policlub",
        "connection": 2,
        "description": "Beer-bellied; gazes sullenly at metahuman customers and takes their credsticks, insulting them when he can; greets humans with guffaws -- 'Scope the Mariners last night? They're not gonna win drek till they dump that Ellsley' (the elven pitcher who keeps winning close games). Bellows 'You can that!' if anyone mentions the policlub in the public area.",
        "notes": "Humanis Policlub contact stats (SR p.168); Ingram Valiant with a 200-round bandolier, fired idly at the targets during lulls. Takes anyone who whispers 'purity' into the back room. Street rumor: starting a new crusade, with his guys scoping the metahuman bars for a human girl.",
        "contact_skills": ["Humanis Policlub rank and file in Auburn", "Automatic weapons range and prizes"],
    },
    {
        "name": "Bart",
        "role": "Chivalrous Knight who watched Elby's day and night 'havin' himself quite the party' and died smiling in the ork raid",
        "archetype": "Humanis Policlub Member",
        "title": "Member, High Chivalrous Order of Humanis Policlub (deceased)",
        "race": "Human",
        "gender": "Male",
        "organization": "High Chivalrous Order of Humanis Policlub",
        "connection": 1,
        "description": "After the Knights lost Nick and Fayette at the dump, Bart kept watch on Elby's day and night, 'dandelion-eaters or no', reporting orks with 'lots of artillery' and following them to The Quick, the Dead, and the Still Moving and to Juzu Clinic's back door. His last report was the day before the adventure began.",
        "notes": "Knight block (p.22). Long dead, caught with a smile on his face when the ork mercenaries raided Elby's; among the twenty-eight in the back room. The Knights are debating sending someone to look for him. Debugging option: alive in a back room, beaten, shot and near death, able to feed the runners whatever the GM needs.",
    },
    {
        "name": "Dr. Kaus",
        "role": "Juzu Clinic's general practitioner; legitimate medicine and tight professional smiles about Dr. Arhill",
        "archetype": "Street Doc",
        "title": "General Practitioner, Juzu Clinic",
        "race": "Human",
        "gender": "Male",
        "organization": "Juzu Clinic",
        "connection": 2,
        "description": "Works in an office off the cream-colored corridors while the clinic's six nurses do the routine procedures. Asked about Dr. Arhill, gives a tight smile and says he has a great deal of experience -- professionals do not comment on one another's work.",
        "notes": "Street Doc stats (SR p.171). With Dr. Meader provides Hospitalization (not Intensive Care); the clinic prefers not to do in-patient work. Terminal to the clinic system's medical-terminal node. A runner could make an appointment with him and wander off toward Arhill's wing.",
        "contact_skills": ["Discreet general medicine (Everett)"],
    },
    {
        "name": "Dr. Meader",
        "role": "Juzu Clinic's cyberneticist -- the man with the chrome nozzle in the groaning ork's eye socket",
        "archetype": "Street Doc / Cyberneticist",
        "title": "Cyberneticist, Juzu Clinic",
        "race": "Human",
        "gender": "Male",
        "organization": "Juzu Clinic",
        "connection": 2,
        "description": "Second name on the clinic's plastic sign. Cybernetic evaluation and cosmetic modification are the clinic's public trade; in the prologue Fayette glimpses a groaning ork with the chrome nozzle of some machine deep in his eye socket.",
        "notes": "Street Doc stats (SR p.171). Professional silence about Arhill. Terminal to the medical-terminal node.",
        "contact_skills": ["Cyberware evaluation and cosmetic surgery (Everett)"],
    },
    {
        "name": "Shark",
        "role": "Double Devils gang boss who charges in a roaring yellow garbage-crusher with studded steel wheels",
        "archetype": "Gang Boss",
        "title": "Boss, Double Devils go-gang",
        "race": "Elf",
        "gender": "Male",
        "organization": "Double Devils",
        "connection": 2,
        "description": "Advances on intruders in a roaring yellow construction machine built for crushing garbage, four bare steel wheels with huge studs grinding whatever they roll over, while his Devils dash around the rubbish piles shooting. No advanced tactics; independent scrambling that may well surround a party.",
        "notes": "Stats (p.27): B5 Q6 S4 C4 I6 W5 Ess 6 R6, armor 5/2; Armed Combat 5, Bike 4, Etiquette (Street) 6, Firearms 4, Stealth 3, Unarmed 5, Drive Compactor 4; no cyberware; AK-97 with a spare clip, armor jacket, Yamaha Rapier. Crusher: Handling 4, Speed 10/25, Body 5, Armor 1, Sig 5; 4D4 to anyone run over. Once beaten or properly approached: 'Hey, ya shoulda said that in the first place, ya dig?'",
        "contact_skills": ["Double Devils and the northern Snohomish go-gang scene"],
    },
    {
        "name": "Jac",
        "role": "Lantern-jawed ex-panzer rigger nursed back to life by Shoalwater's pacifists, aching to prove his trade with the wreck of the Charlotte",
        "archetype": "Rigger (former panzer driver)",
        "title": "Shoalwater council member; former thunderbird driver",
        "race": "Elf",
        "gender": "Male",
        "organization": "Shoalwater Elven Community",
        "connection": 2,
        "description": "A lantern-jawed elf with a dark gaze who feels ostracized by the commune's anti-war idealists and looks away when he says, quietly, 'There's always Charlotte...' -- and is shouted down. Accept his plan and he becomes the runners' avid supporter, adding his five Charisma dice to the council pool.",
        "background": "A true child of the sprawls whose last panzer run ended half a kilometer from the commune, brought down by two AS-AAMs from a wing of Salish-Shidhe Ranger choppers that never found the wreck; his partner did not crawl away. The elves found him battered and bleeding and nursed him back; during the slow recovery he fell in love with commune life, though he still longs for the action.",
        "notes": "Corporate Rigger stats (Sprawl Sites p.107) with his Vehicle Control Rig burned out by the crash's electric flashover; Vector Thrust in place of Rotor; Colt Manhunter (26 rounds) under his bed; three LG-AVM reloads in his room. Leads the runners to the Charlotte and helps jury-rig the launchers. Its radio still reaches the Ranger Force that shot him down.",
        "contact_skills": ["Thunderbird smuggling runs and Ranger patrol patterns", "Jury-rigged vehicle weapons"],
    },
    {
        "name": "Marietta",
        "role": "Emaciated, stringy-haired Shoalwater elf who wants Fayette sent away to spare the tribe a battle",
        "archetype": "Commune Member",
        "title": "Shoalwater council voice",
        "race": "Elf",
        "gender": "Female",
        "organization": "Shoalwater Elven Community",
        "connection": 1,
        "description": "An emaciated elf with stringy black hair who aggressively suggests that Fayette leave: 'Sorry, I see your position. But I think this is an issue where we have to consider the rights of the community, too.'",
        "notes": "Elf Pedestrian stats. One of the four council opponents the runners must argue past (Charisma or Persuasion 4, ten total successes).",
    },
    {
        "name": "Arden",
        "role": "Tall Shoalwater elf in the sash of a former Tir Tairngire office-holder; 'Elves handle their own problems, thank you very much'",
        "archetype": "Commune Member (former Tir official)",
        "title": "Shoalwater council voice; formerly held office in the Tir Tairngire hierarchy",
        "race": "Elf",
        "gender": "Male",
        "organization": "Shoalwater Elven Community",
        "connection": 2,
        "description": "A tall elf who wears a sash indicating he once held an office in the hierarchy of Tir Tairngire and wants the adventurers to leave Shoalwater alone.",
        "notes": "Elf Pedestrian stats. Why a Tir official ended up in a pacifist pinkskin commune in Salish territory is the GM's to invent; a possible line to the Tir for later.",
        "contact_skills": ["Tir Tairngire hierarchy (former insider)"],
    },
    {
        "name": "Fantine",
        "role": "Middle-aged Shoalwater elf who knits through the council and then sits up with 'I just don't think that's right'",
        "archetype": "Commune Member",
        "title": "Shoalwater council voice",
        "race": "Elf",
        "gender": "Female",
        "organization": "Shoalwater Elven Community",
        "connection": 1,
        "description": "Hair in a long braid, knitting through most of the meeting; when it is time to decide she suddenly sits up and says, 'I just don't think that's right.' Asked why: 'It just doesn't seem like a good idea.'",
        "notes": "Elf Pedestrian stats. Council opponent.",
    },
    {
        "name": "Suzanne Vann-d'Venescu",
        "role": "'Diana' -- the legendary decker whose gold-armored icon still haunts her deck; murdered by her husband, she saved her daughter and stole his fortune first",
        "archetype": "Decker (legend)",
        "title": "Decker 'Diana' (deceased c. 2036-2041); Fayette's mother, Marti's sister",
        "race": "Elf",
        "gender": "Female",
        "connection": 3,
        "description": (
            "Her icon: a figure of milky glass in finely constructed translucent gold armor in the "
            "ancient Greek style over a tunic of sheerest silk, hair spun gold floating in an imaginary "
            "breeze, eyes the cool blue of sky, a crisp powerful voice laced with rushing water. 'A hot "
            "decker back a number of years. Big player.' 'A real burner, that one.' Real ID on the "
            "street: 'Elle Vann or something'."
        ),
        "background": (
            "A crack decker who married Aztechnology's rising conjurer Anton d'Venescu and three years "
            "later became the first half of his sacrifice. She evaded him for several days, hid the baby "
            "with her sister Marti in the electronic confusion she created, transferred a fortune out "
            "of an Aztechnology account her husband had access to into an orbital trust, and was "
            "caught and impaled in a coffin motel. The street says her husband killed the little girl "
            "too, and that this started the 'blood magic' and 'helipads-turned-sacrificial-altars' "
            "rumors about Aztechnology."
        ),
        "notes": (
            "Deceased; appears only as the persona her sister wears. Her deck (Fuchi Cyber-4 "
            "equivalent, Response Increase 2, custom MPCP chips, Bod 6 / Evasion 6 / Masking 6 / Sensors "
            "7 / Attack 3 / Evaluate 5 / Sleaze 5) still manifests as Diana. Legwork (Matrix contacts, "
            "TN 3 if active around 2040): 'Somebody killed her up close and personal about ten years "
            "ago.' The AI red herring is worth fostering. Race inferred: her sister is an elf. Any old "
            "decker who knew her is a hook."
        ),
    },
]

ORG_UPDATES = {
    "Aztechnology": {
        "notes_append": (
            "Ivy & Chrome (June 2051): public profile -- home office Mexico City, Aztlan; President/CEO "
            "Juan Atzcapotzalco; Northwest Division under Salvador Ramirez, diversified from armaments "
            "to electronics, backed by elements of the Third Aztlan Legion; many believe the company "
            "is the real power behind Aztlan's government; grew from South and Central American "
            "resource and technopirate outfits in the early Awakening on magically endowed employees "
            "and ruthless industrial espionage; founder and son both said to be accomplished "
            "magicians. The d'Venescu affair: the company funded Anton d'Venescu's 2034 ocapatli/Aztec "
            "ritual research, lost several million nuyen to his murdered wife's transfers, keeps him "
            "alive under Juzu Clinic because 'certain people' want to know whether his methods work, "
            "and lets Branch 45-Tlaloc finance his hunt for his daughter with outside talent while "
            "'watching him string out the rope he'll hang himself with'. Aztechnology deckers combed "
            "the Rhododendron Conservatory's student files. Legwork with a current Aztech contact: TN 8, "
            "and a failure means a polite, firm warning off; a former employee who left badly, TN 2. "
            "Street rumor ties the corp's rise to an unholy alliance with Aztec spirits -- 'Has "
            "Aztechnology really contacted the great Aztec spirits? Only time will tell.' Aftermath: "
            "the corp quietly cancels Juzu's grants (success) or announces a Tlaloc-division metamagic "
            "breakthrough with d'Venescu crediting 'my daughter Fayette' (failure); either way ATC "
            "prefers to forget him and does not retaliate unless the story is sold to the media. "
            "Discrepancies with this row: the book's public database gives the home office as 'Mexico "
            "City, Aztlan' (this row says Tenochtitlan) and spells the Northwest Division head "
            "'Salvador Ramirez' (this row's leadership entry reads 'Ramierez'); both left as they were."
        ),
        "allies_add": ["Juzu Clinic", "Aztechnology Tlaloc Division"],
    },
    "Humanis Policlub": {
        "notes_append": (
            "Ivy & Chrome: a den styling itself the High Chivalrous Order of Humanis Policlub meets in "
            "the back room of Cratchit's Family Entertainment in Auburn (password 'purity') -- "
            "'loosely affiliated' with the club, robed and hooded for ritual trials of 'traitors' "
            "recorded for recruitment vids, and on a crusade to rescue a Bellevue schoolgirl from her "
            "elven boyfriend. Rhododendron Conservatory math teacher P. Grumblatt is a member. Cratchit "
            "is 'a big man in the poli'. Humanis Policlub Member and Contact stat blocks (SR p.168) "
            "used throughout."
        ),
        "allies_add": ["High Chivalrous Order of Humanis Policlub"],
    },
    "Lone Star Security": {
        "notes_append": (
            "Ivy & Chrome: a blue patrol cruiser picked Fayette Myers up near Zappy Zed's kiosk three "
            "months ago, IDed her and drove her back to the Conservatory with advice about that part of "
            "the plex. The Conservatory's guards hand impostors to Lone Star and the school presses "
            "charges; the local branch lets prisoners buy their way out for 1,000 nuyen. Juzu Clinic's "
            "PANICBUTTON brings four troopers (Ares Predators, vests, helmets) in five minutes and near-"
            "unlimited reinforcements in twenty; the Sea-Tac ticket-registry Trace sends a patrol of "
            "four Street Cops. VMI calls Lone Star if abused. Crowd control at Club Zor for Concrete "
            "Dreams (June 2051 news). Twenty-eight murders at Elby's Bar and Grill went uninvestigated "
            "for at least a day."
        ),
    },
    "Salish-Shidhe Council": {
        "notes_append": (
            "Ivy & Chrome (June 2051): Interstate Routes 12 and 101 to North Cove stay open under "
            "Salish-Shidhe traders; the Border Patrols and Ranger Force stop vehicles at random (four "
            "Former Tribal Warriors per Chrysler-Nissan patrol car, Browning Max-Powers, an Enfield AS7, "
            "two Remington 750s), fine Seattle residents without a Blue Ticket from the metroplex Council "
            "Lodge 200 nuyen and escort them home, and confiscate narcotics and non-hunting weapons. "
            "Kill a warrior and nearly the whole population becomes an enemy; warn them of a corporate "
            "raid and they say 'This is not the way in our land.' The Rangers' fastest response is "
            "astral -- a pair of Combat Mages in 1D3 turns if convinced by radio that a corporation is "
            "waging war on tribal land; Ranger choppers shot down Jac's thunderbird near Shoalwater. The "
            "Council numbers the human Fayette Myers among its people under a name of its own giving, "
            "and its Seattle Council Lodge spokeswoman names 'Martha Newblood' as the honored woman who "
            "speaks for the elves of Shoalwater. Blue Tickets: Nicholas Voigt requested one three "
            "months ago and bought a twelve-moon ticket last week. Shoalwater, a former Indian "
            "reservation on North Cove, is now a pinkskin elven tribal holding. The June 8 newsnet has "
            "the North American heads-of-state economic summit opening the next day."
        ),
        "allies_add": ["Shoalwater Elven Community"],
    },
    "Cascade Ork": {
        "notes_append": (
            "Ivy & Chrome: Rat Mash Dancer, a Coyote shaman of the Cascade ork, leads seven tribal "
            "warriors who came to Seattle for bigger nuyen as mercenaries (stat blocks pp.54-55: swords "
            "etched with Cascade ork traceries, AK-97s, Neuro-Stun grenades, 'absolutely no social "
            "inhibitions'). Hired through Juzu Clinic for Aztechnology's d'Venescu affair, they massacred "
            "Elby's Bar and Grill downtown; the twenty orks on the Shoalwater helicopters use the Ork "
            "Mercenary archetype. Her tribal status is part of why they obey her."
        ),
        "allies_add": ["Rat Mash Dancer's Mercenaries"],
    },
    "Banque Orbitale de Suisse": {
        "notes_append": (
            "Ivy & Chrome: Suzanne Vann-d'Venescu ('Diana') moved several million nuyen from an "
            "Aztechnology account her husband could access into a Banque Orbitale de Suisse orbital "
            "trust for her daughter before he killed her; Marti Vann pays Fayette's 130,000-nuyen "
            "Conservatory tuition from a confidential account there (Computer 9 on the school's "
            "accounts: laundered; two successes: originally Aztechnology's) and paid VMI from the same "
            "trust. Fayette's 1.5-million-nuyen investments vest at 21."
        ),
    },
    "Tir Tairngire": {
        "notes_append": (
            "Ivy & Chrome: Lord Erindil, 'a well-known spokes-elf for Tir Tairngire', is a man-shaped "
            "target on the automatic-weapons range at Cratchit's Family Entertainment in Auburn -- "
            "shoot only the points off his ears for a FabriSoft prize. Fax-a-Tabloid rumor has Tir "
            "sorcerers reviving bride abduction ('Seelie honeymoons'). Arden of Shoalwater wears the "
            "sash of a former office in the Tir hierarchy."
        ),
    },
    "Mitsuhama Computer Technologies": {
        "notes_append": (
            "Ivy & Chrome: Tanya Oko, daughter of a Mitsuhama Assistant Technical Vice President for "
            "Facilities Management, boards at Rhododendron Conservatory in Bellevue -- the kind of "
            "corporate heir the school exists for."
        ),
    },
    "Fuchi Industrial Electronics": {
        "notes_append": (
            "Ivy & Chrome (June 8, 2051 news): Fuchi Cyber stock up 35 points on unsubstantiated rumors "
            "of a breakthrough magic/technology meld by a subsidiary. 'Apathy about Futisama': UCAS "
            "investigators say Fuchi security troops used illegal measures -- allegedly holding the "
            "formerly independent Futisama Research Ventures Institute's key laboratories hostage at "
            "gunpoint -- during the merger; Fuchi is now majority shareholder, Mr. San calls it 'a "
            "standard business procedure', deposed president Mr. Kama is off to Amazonia, and Fuchi has "
            "asked UCAS agents to drop it since the public stopped caring."
        ),
        "enemies_add": ["Futisama Research Ventures Institute"],
    },
    "Renraku Computer Systems": {
        "notes_append": (
            "Ivy & Chrome (June 8, 2051 news): dozens injured at the Renraku Arcology by three "
            "allegedly magical fires; witnesses say Renraku security mages banished three 'berserk' fire "
            "elementals. No word on their origin and no statement from Renraku."
        ),
    },
    "Seattle News-Intelligencer": {
        "notes_append": (
            "Ivy & Chrome: the Update-Net for Thursday June 8, 2051 (14:00, Local News) -- summit, UCAS "
            "Marine Corps recruiting orks and trolls (Major Feanor Oldtree: 'You don't need to be 2.5 "
            "meters tall and covered with warts to be a good marine'), the Arcology fire elementals, "
            "Fuchi Cyber stock, the Me 'n' My Shadow jewelry melee, Commissioner Michael Mount "
            "McKinley keeping the 'Dwarf at the Plate' rule, Governor Schultz's 1 a.m. Aquarium council, "
            "Futisama, Concrete Dreams at Club Zor, and either 'Public Clinic Loses Grant' (Aztechnology "
            "drops Juzu) or 'Magic Reveals Its Secrets at Aztechnology' (d'Venescu thanks his daughter)."
        ),
    },
    "Seattle Metroplex Guard": {
        "notes_append": (
            "Ivy & Chrome (June 2051 news, city government): Governor Marilyn Schultz convened the "
            "Metroplex Council at 1:00 a.m. in the Seattle Aquarium with a bare quorum, which unanimously "
            "approved her controversial executive order on auto ownership taxes -- not expressly "
            "forbidden by city law, 'highly irregular' say her critics. 'Being governor means making "
            "these tough decisions. People will always complain.' UCAS Marine Corps recruiters are "
            "targeting orks and trolls amid discrimination protests."
        ),
    },
}

LOC_UPDATES = {
    "Renraku Arcology (SCIRE)": {
        "notes_append": (
            "Ivy & Chrome (June 7, 2051): three allegedly magical fires injured dozens; Renraku security "
            "mages banished three 'berserk' fire elementals of unreported origin. Renraku issued no "
            "statement."
        ),
    },
    "Grand Council Lodge (Council Island)": {
        "notes_append": (
            "Ivy & Chrome: the 'metroplex Council Lodge' issues the Blue Tickets Seattle residents need "
            "to travel Salish-Shidhe roads (Nick Voigt requested one three months ago and never picked "
            "it up; bought a twelve-moon ticket last week) and houses the Council Lodge Travel Bureau, "
            "whose brochure on Salish-Shidhe lodging Fayette kept under a floor tile. An impassive "
            "woman at the lodge desk (Etiquette (Tribal) 4) will confirm that Fayette is numbered among "
            "the Council's people, that her aunt Martha Newblood speaks for the elves of Shoalwater, and "
            "that Fayette's tribal name needs the proper forms and six weeks."
        ),
    },
    "Salish-Shidhe Border Post (Seattle crossing)": {
        "notes_append": (
            "Ivy & Chrome: the westbound crossings onto Interstates 12 and 101 are where Anton "
            "d'Venescu's raiders were 'dropping yen right and left to get the drop on patrols' to smuggle "
            "armed troops toward Shoalwater; Blue Ticket checks, 200-nuyen fines and weapon "
            "confiscation are the routine about 30 km out."
        ),
    },
    "The Barrens (Seattle)": {
        "notes_append": (
            "Ivy & Chrome: 'You aren't thinkin' about a trip through the Barrens, are ya? ... There's "
            "some kinda go-gang in the tire dump by Route 12, and they're out for blood.' The Double "
            "Devils' dump is on Filbert-Maltby Road in northern Snohomish near Thrasher's Corner, with a "
            "squatter tribe in an abandoned strip mall a few blocks off."
        ),
    },
}

NPC_UPDATES = {}

TAG_EXISTING = {}

MATRIX_HOSTS = """
**1. Rhododendron Conservatory -- Sorrel Hall system** (map key p.16; UMS image set, interlinking
geometric and fractal constructs; SAN LTG# 9206 (12-8902), public access). Anita Wood shuts the system
down in two actions on an External alert; PANICBUTTON connections in the Main Offices. The public
front is the school's promotional feed; the real prize is DS-2/DS-3 behind SPU-2. Build as a small
Orange host with a Blue public shell.

| Node | Function | Rating / IC |
|---|---|---|
| SAN-1 | Public access, LTG# 9206 (12-8902) | Blue-1 |
| SPU-1 | Data routing | Blue-1 |
| DS-1 | Promotional hyper/multimedia files for prospective clients; nothing of interest | Blue-1 |
| SPU-2 | Office systems | Orange-5, Access 5, Trace 4 |
| I/OP-1 | Terminal in the Headmaster's office | Green-4 |
| I/OP-2 | Terminals in the Main Offices (Anita's old-fashioned video-monitor terminal) | Green-4 |
| SM-1 | Office equipment in Sorrel Hall | Green-4 |
| SM-2 | Educational computers in Frankle Hall | Green-4 |
| SM-3 | Security systems throughout the campus (cameras, voice-print door, room microphones, fence, maglocks) | Orange-5, Trace and Burn 4 |
| CPU | -- | Orange-5, Blaster 4, Trace 4 |
| DS-2 | School accounts: 15,000 nuyen (15 Mp); Fayette's tuition paid from a confidential Banque Orbitale de Suisse account (Computer 9: laundered; 2 successes: originally an Aztechnology account) | Orange-5, Trace and Burn 5 |
| DS-3 | Student files: Fayette's grades collapsed this year; her earlier disappearance and Lone Star return; the Juzu examination (records withheld by the clinic); Computer 5 finds 'ashes' left by Aztechnology deckers; other students' records 5 Mp, 5,000 nuyen to corporate rumor-mongers | Orange-5 |

The Dispensary's medical computer is standalone (no Matrix link): first-aid expert system plus the
school's health calendar, including Fayette's 'Cqm-S' follow-up at Juzu Clinic early next month.

**2. Seattle-Tacoma Airport -- Ticket Registry subsystem** (map key p.29). A tiny subsystem of the
airport's enormous account; nothing here triggers a full External Alert, but the Trace brings Lone
Star (four Street Cops). Ticket machines double as terminals with a maximum Program Rating of 2 that
open straight into the system. Anyone going in from outside needs the GM to invent the route.

| Node | Function | Rating / IC |
|---|---|---|
| SAN-1 | Intersystem access only, no direct Grid access | Orange-4, Trace and Dump 4 |
| SPU-1 | Data routing | Orange-3, Barrier 5 |
| I/OP-1 | Ticket machines | Blue-2 |
| DS-1 | Ticket registry: Fayette and Nick scheduled a Seattle-North Cove commuter flight three months ago and never showed | Orange-5, Scramble 3 |
| SPU-2 | Data processing, leading away to the bulk of the airport's systems (random generation if explored) | Orange-5, Barrier 3, Trace and Burn 4 |

**3. Juzu Clinic system** (map key pp.30-31; UMS multi-colored polygons, one or two sculpted nodes;
SAN NA/SEA/3206 (34-8705) on the map, (34-8075) in Legwork -- pick one; Everett, 3206 LTG, 34-block).
One alarm = Internal Alert; three = External Alert and total shutdown in 4D6 turns (the clinic does
not need a permanent link). The SAN's Trace does NOT call Lone Star: it rings a telephone at The Quick,
the Dead, and the Still Moving and a synthesized voice sends the orks after the decker. Arhill's
office terminal (I/OP-5) bypasses most of the IC. A decker contact swears it has 'not even any IC'.
The best host in the book -- build it in full.

| Node | Function | Rating / IC |
|---|---|---|
| SAN-1 | Entry; Trace alerts the ork mercenaries, not the police | Orange-4, Barrier 4, Trace and Report 4 |
| SPU-1 | Data routing | Orange-4, Access 4 |
| I/OP-1 | Waiting-room terminals (receptionist) | Green-4 |
| SPU-2 | Medical records and machinery | Orange-5, Tar Baby 4 |
| I/OP-2 | Crisis Counseling node: a rippling black-leather couch and an automated psychotherapist that answers keywords ('Was that a negative event in your life?') | Blue-4 |
| SM-1 | Scanners and medical equipment (the DNA scan/matcher) | Orange-4, Access 4 |
| I/OP-3 | Medical terminals of Dr. Kaus and Dr. Meader (room text swaps this with I/OP-4) | Orange-4, Barrier 4 |
| DS-1 | Medical records: Fayette Myers' file with Arhill's asterisks and his examination report (5 Mp, handout p.58); Anton d'Venescu's file (5 Mp, handout p.59); records of important wage mages, 280 Mp, 50,000 nuyen on the black market | Red-3, Blaster 4 |
| SPU-3 | Administrative systems | Orange-5, Access 4, Tar Baby 4 |
| I/OP-4 | Terminals in the basement Improvised Offices | Orange-4 |
| DS-2 | Business records: Aztechnology grants; accounts with mercenaries and military outfitters for a raid into Salish-Shidhe territory (300 nuyen to a recruiter, 800 to an Aztech-watcher); Arhill's correspondence including Memo 2 to Branch 45-Tlaloc (handout p.60); wage-mage dealings, 100 Mp, 500 nuyen | Orange-4, Scramble 4 |
| I/OP-5 | Dr. Arhill's office terminal | Orange-5, Blaster 3 |
| SPU-4 | System management (the Trace lives here; see SAN-1) | Orange-5, Barrier 4, Trace and Burn 4 |
| SM-2 | Security systems: every camera and alarm; a decker can look through the cameras and switch them off, mapping the clinic and its lower levels | Orange-5, Killer 4 |
| CPU-1 | -- | Red-4, Barrier 5, Trace 5, Black IC 2 |
| DS-3 | Finances: 200,000 nuyen (200 Mp) | Orange-5, Scramble 5 |

**4. Virtual Meetings Incorporated** -- the conference room is a construct on VMI's own system, entered
only through its senselink couches; dedicated hardlines, satellite uplinks and a legion of corporate
deckers. Never mapped and not deckable from inside; do not build unless a later run targets VMI.

**5. Rhododendron promotional feed** -- the public Blue nodes above are what Anita hands out to
prospective parents.
"""

NOT_BUILT = """
- **Governor Marilyn Schultz** and the **Metroplex Council** (1 a.m. Aquarium session) -- on the
  Seattle Metroplex Guard / News-Intelligencer rows, as in Bottled Demon. **Major Feanor Oldtree**
  (UCASMC), **Commissioner Michael Mount McKinley**, **Mr. San** and **Mr. Kama** (Fuchi/Futisama),
  **Lord Erindil** (Tir spokes-elf target), **Ellsley** (elven Mariners pitcher), **Nailhead** (Urban
  Brawl star), **the Stim Boys** (dorm music), **Juan Atzcapotzalco** and **Salvador Ramirez**
  (already leadership entries on the Aztechnology row) -- news and name-drops.
- **The Conservatory gate guards** (Former Company Man block), **the Oxus Hall girls**, **the Juzu
  security chief, guards, nurses, receptionist, secretary, scientists and senior technicians**, **the
  ork on the Sea-Tac bench**, **the Border Patrol warriors**, **the truck-stop shopowner**, **the
  Council Lodge spokeswoman**, **VMI's receptionist, corporator and head technician**, **the troll
  bouncer at The Quick, the Dead, and the Still Moving**, **Rind's brothers** -- stat pointers on the
  org and location rows.
- **UCAS Data Systems** (VMI's parent) -- on the VMI row. **Aztech Pharmco** (boxes in the loading dock)
  and **Aztechnology Branch Office 45-Tlaloc** -- on the Tlaloc Division row.
- **The Charlotte** (GMC Banshee-A4 wreck), **the two Hughes WK-2 Stallions and their riggers**, **the
  twenty archetype orks**, **the four Force 7 elementals**, **Arhill's Watchers** -- on the Shoalwater
  and Juzu rows.
- **The coffin motel** where Suzanne died, **the elven enclave** Fayette grew up in, **the soy bar**
  Fayette hid in, **the abandoned strip mall** of the dump squatters, **the truck stop on Route 12** --
  unnamed; folded into the relevant rows.
- **Patecatl / the Aztec rain god**, **ocapatli**, **ardone**, **malon**, **devil flies**, **Cacodemon
  Debt Default Syndrome** -- lore on Anton's and Juzu's rows; no mechanics invented beyond the book.
"""

PLAY_NOTES = """
- A decision tree, not a rail: the Conservatory, Cratchit's, Elby's, the ork bar, the dump and Sea-Tac
  all overlap; it does not matter which clues are missed. Everything points at Juzu Clinic or
  Shoalwater, and the first one investigated explains the rest. If the team stalls, send Rind, stage an
  ork ambush, or have a contact drop a hint.
- Play the Diana icon as a possible AI for as long as the players will bite; Marti never admits it.
- The Conservatory is a test of restraint: a plausible cover gets wide access, a firefight ends the
  investigation, and Lone Star jail follows. Wash and wear suits (Blum's TN drops from 8 to 5).
- Two clocks: Nick and Fayette reach Shoalwater at 3 p.m. on day one; Arhill finds them on day four
  by himself, sooner if the runners are trailed (tracking disks, Watchers, astral interns), and the raid
  comes at 2:30 a.m. on day five -- three hours after the location is confirmed if the runners gave it
  away. The GM is told to fudge freely.
- Captured runners are not killed: tranq patches, Mind Probe, a disk under the shoulder blade, and a
  wake-up in the alley behind Elby's. Biotech (4) finds the scar; removal costs 200 nuyen or Biotech (9).
- Salish territory: kill a Border Patrol and the whole nation is an enemy for the rest of the campaign.
  Blue Tickets come from the Council Lodge; the patrols will not believe a corporate raid is coming.
- The Shoalwater council is roleplay first, dice second (ten successes by consensus). The Charlotte's
  two missile launchers (three shots) and its Ranger-frequency radio are the equalizers; a wilderness
  shaman with spirits in Shoalwater's several domains 'could sway the battle radically'.
- Nick erupts at any male runner's move on Fayette; he and Marti are due a terrible fight.
- Karma: Fayette saved and d'Venescu eliminated 5; Anton neutralized 3; survival 1. Fayette has 10 Karma
  of her own and can be taught a skill while waiting.
- Loose ends: Anton alive (a sequel run with Aztechnology's resources, until the spirits or his own
  mind finish him in months); Fayette expelled and back with Nick as a contact or patron; a grudge
  from Rat Mash Dancer's surviving orks; the Chivalrous Knights' recruitment vid; Arden's Tir past;
  Aztechnology's helipads-turned-altars rumor; Juzu Clinic's Emergency Fund Drive.
"""
