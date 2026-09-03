# Mercurial (FASA 7302, 1989) -- campaign order #4. RE-CHECK PASS over the 2026-08-30 load.
# Source text: docs/Adventures/text/SR_Mercurial.txt (78 pages).
# The earlier agent created orgs 25-31, locations 18-25 and NPCs 36-59 by hand; this spec tags those
# rows, appends what the book adds (stats, descriptions, layouts, the hearth spirit, the news items),
# corrects the "Kathy Sakura" row to Sumiko Hotoda, and adds the flavor the first pass skipped.
# ASCII only (pre-commit hook).

ADVENTURE = "Mercurial"
ORDER = 4
SOURCE = "SR_Mercurial.pdf (FASA 7302), pp. 4-78"
YEAR = "2050 (December)"

SYNOPSIS = """
Maria Mercurial, the silver-skinned novastar, is playing Underworld 93. Her new agent **Max Foley**
hires the runners at 2:00 a.m. in Dressing Room One as bodyguards (5,000 nuyen each for five days,
Negotiation 7 to raise it) against her ex-manager **Armando Hernandez**, who Maria dumped after
finding "evidence" that he pushes dreamchips. Three Pugnacine-Beta-drugged street samurai with
glowing red eyes crash the meeting yelling "Don't frag with Hernandez!", and Newt and Tellin push
everyone out the back door ahead of Lone Star.

None of it is what it seems. Five years ago Maria was Maria Aguilar, indentured bodyguard, secretary
and mistress to Aztechnology exec **Reynaldo Texamachach**, rebuilt by the Chiba cyber-artist
**Sorayama** and addicted to custom BTLs to keep her obedient. When Texamachach was sent to bury
**Perfekto Polymers'** illegal Barrens waste tank (and the Greenwar cell that found it), he stored his
only report in her sealed memory; she blew his brains out in his Pyramid suite and vanished into the
Barrens, where Hernandez found her singing in a brothel. Now **New Horizons Development** -- a front
for the **Shigeda-gumi** yakuza -- is redeveloping the poisoned land and blackmailing Perfekto, so
Aztechnology has sent assassin **Kyle Morgan**, his Western dragon partner **Perianwyr**, and the
"Dragon Knights" to Seattle, with Shigeda mage **Sumiko Hotoda** ("Kathy Sakura") as liaison. The
plan: frame Hernandez, kidnap Maria, pull the data out of her head, kill them both.

Part One: a 10,000-nuyen street bounty, a rent-a-hideout in the Barrens, Foley's double-dealing, the
Federated Funds Net piggy bank, Hernandez drunk and heartbroken in his brownstone, Gum E. Bear guarding
Foley's system, and the yakuza assault on the hideout where Sumiko offers Maria a dreamchip. Part Two:
Perianwyr burns Foley (and Sumiko) and the hideout, the legwork trail leads through New Horizons,
Sorayama's samurai-castle host in Chiba, Ms. Kenner, Snout the ork snitch, and the Dragon Knights'
mainframe to the derelict **Taetzel Building** -- griffins, a cockatrice, a basilisk, servoguns, an
elevator that drops from the 11th floor, and Morgan choosing to die rather than torture Maria, while
Perianwyr carries his body into the smoke. Unlock code for Maria's sealed memory: "Silver Virgin".
"""

TIMELINE = """
- **2044** -- Sorayama's "Ultra #84" commissioned 06/13/44 by "Johnson-san" for Aztechnology; subject
  Maria Aguilar. **2045** -- Perfekto plant shut, Greenwar cell wiped out, Texamachach killed by Maria
  in the Seattle Pyramid; Hernandez pulls her out of a Barrens brothel and into Dr. Kenner's clinic.
- **2047** -- first set at Underworld 93 (Hernandez camped in Murdoch's waiting room for a week).
  **2048** -- "Who Weeps for the Children?" number one for two months; "Night Tears"; "Take It To
  Mister". **2049** -- "Puta" and a 28-city tour. **Feb 12, 2050** -- Rocker Stars interview.
- **A year ago** New Horizons starts buying the Barrens; **last month** it starts building, Perfekto
  warns it of the tank, New Horizons stops work and delivers its ultimatum; Sumiko plants the BTL
  evidence on Hernandez's computer (Gum E. Bear); Maria signs with Foley; the "Hernandez" threats.
- **Night 1** -- Underworld 93, 2:00 a.m. meet, shootout, escape in Newt's lime-green van.
- **Days 1-5** -- the five days of Foley's contract: hideout, bounty, legwork, Hernandez, Federated,
  Foley's host, the yakuza attack (Part One ends). Then the dragon strike, New Horizons / Sorayama /
  Kenner / Snout / Dragon Knights mainframe legwork, Knock Knock, and the Taetzel assault.
"""

# ----------------------------------------------------------------------------------------------
ORGS = [
    {
        "name": "Greenwar",
        "org_type": "eco-terrorist policlub",
        "tier": 2,
        "headquarters": "Cells worldwide; the Seattle cell was wiped out in 2045",
        "summary": "Eco-terrorist policlub whose Seattle cell found Perfekto's dumping data and gloated -- then died",
        "description": (
            "An eco-terrorist policlub. Its local Seattle cell ran Perfekto Polymers' mainframe in 2045 "
            "and came away with a secret report on how much the plant was saving by dumping industrial "
            "waste into a hidden underground tank instead of shipping it to UCAS dump sites far from NAN "
            "territory. Greenwar meant to hand it to the news-nets -- meganuyen fines, clean-up costs, "
            "and NAN pressure to pull Perfekto's Seattle license -- but the drekheads in charge had the "
            "urge to gloat and left a nasty note in the CEO's mailbox first."
        ),
        "notes": (
            "The note gave Aztechnology time: Reynaldo Texamachach had the plant closed, the manager "
            "shipped to Mexico City, the night-shift technicians killed in accidents, and the whole local "
            "Greenwar cell wiped out by a strike force of Aztechnology shadowrunners. Surviving Greenwar "
            "cells elsewhere are a natural ally for runners who go public with the waste-tank data, and "
            "the Treaty of Denver makes NAN councils sudden death on polluters."
        ),
        "enemies": ["Aztechnology", "Perfekto Polymers"],
    },
    {
        "name": "Musician's Guild Local 14",
        "org_type": "trade guild",
        "tier": 1,
        "headquarters": "Seattle",
        "summary": "The performers' guild; contract notices, the 30-day rule, and the leverage Foley was waiting for",
        "description": (
            "Seattle's musicians' and performers' guild. Artists give a manager statutory 30 days' notice "
            "of intent to leave; once the notice runs out the guild comes in on the new agent's side and "
            "anyone who so much as looks cross-eyed at the artist is history in the business. Contract "
            "reinstatements are filed here."
        ),
        "notes": (
            "Foley's five-day bodyguard contract exists because Maria's notice to Hernandez has five days "
            "to run. In the happy ending the guild receives notice that Maria has reinstated her contract "
            "with Hernandez. A useful lever for any future music-industry run."
        ),
    },
]

LOCATIONS = [
    {
        "name": "The Armadillo",
        "location_type": "bar",
        "district": "Puyallup Barrens (fringe)",
        "security_level": "No Security / Barrens",
        "summary": "Razor-guy dive where Maria unwinds after gigs by starting bar fights",
        "description": (
            "A razor-guy dive a block off a dark Barrens street, crammed with the wannabes, used-to-bes "
            "and assorted killer-bees of the samurai scene, the vibes a veritable oratorio of bad-ass. The "
            "tequila is toxic waste under an alias. Grimy-nasties offer dubious pleasures at the bar; "
            "trouble follows the sound of breaking glass within seconds."
        ),
        "notes": (
            "Where Maria goes to unwind after a show (prologue, pp.4-5): black armorcloth street outfit "
            "set with silver splints, opaque vision-augmenting shades, her limo driver waiting a block away "
            "with a shotgun. She cartwheels a would-be suitor through the bottle pyramid, starts a brawl, "
            "then vomits in a doorway down the block while thuggers close in. Kyle Morgan shadowed her here "
            "before the adventure. Anyone who wants to find Maria off-stage starts at joints like this."
        ),
    },
    {
        "name": "The Down And Out",
        "location_type": "bar",
        "district": "Seattle (street level)",
        "security_level": "Low Security",
        "summary": "Snout's favorite bar; where he buys a round with Morgan's 500 nuyen",
        "description": (
            "A low street bar where a small-time ork snitch can buy a round of drinks for the house and "
            "nobody argues with anyone who walks in showing ready weapons."
        ),
        "notes": (
            "Snout is easy to find here after the Knock, Knock raid, flush with Kyle Morgan's 500 nuyen. "
            "Threaten him even a little and he gives up the scarred Aztlan Indian who hired him and the "
            "Taetzel Building he peeked at through his blindfold."
        ),
    },
    {
        "name": "New Horizons Development Sites",
        "location_type": "commercial district",
        "district": "Barrens (around the old Perfekto plant)",
        "security_level": "No Security / Barrens",
        "controlling_org": "New Horizons Development",
        "summary": "Half-demolished blocks under 'New Tomorrows FROM New Horizons' billboards; work stopped a month ago",
        "description": (
            "Big new billboards reading \"New Tomorrows FROM New Horizons\" stand over partially demolished "
            "blocks and abandoned building sites in the slum around the old Perfekto Polymers plant. Work "
            "went quickly for a week and then stopped on every site on the same day, leaving every job "
            "unfinished. Two kilometers away Mitsuhama is about to open a new regional manufacturing and "
            "sales center that will send local property values into orbit."
        ),
        "notes": (
            "Construction stopped the day Perfekto warned New Horizons that millions of liters of toxic "
            "waste are buried somewhere in the development -- a week before Maria found the planted "
            "evidence. New Horizons bought everything in the neighborhood except the plant and the "
            "Taetzel Building, both still Perfekto's. Street people saw unmarked vans and dozens of workers "
            "spend three days at the Taetzel about a week later, after which squads of toughs began driving "
            "everyone away for blocks around. Legwork TN 4 (clue table p.51); at 25+ successes two yakuza "
            "goons put a runner in the hospital as a warning."
        ),
    },
    {
        "name": "Dr. Kenner's Clinic",
        "location_type": "hospital",
        "district": "Seattle",
        "security_level": "Patrolled / Commercial",
        "summary": "The detox clinic that got Maria off BTLs; her therapist's records and Personality Profile",
        "description": (
            "The clinic where Armando Hernandez had Maria treated for dreamchip addiction in 2045, and where "
            "Ms. Kenner still sees her. Its records note that Maria's datajack was routed through the limbic "
            "pleasure/pain centers -- surgery too complex to undo -- and that her addiction was to a custom "
            "chip no Barrens prostitute could afford."
        ),
        "notes": (
            "Aztechnology's corporate shadowrunners lifted copies of Maria's records here years ago, which "
            "is how the corp knew she had lost her memory and stopped hunting her. Kenner talks only with "
            "Hernandez vouching for the runners, and shares the Personality Profile only if convinced it is "
            "in Maria's interest. A biotech with a microtronic tool kit (TN 5) can match the dreamchip from "
            "the hideout fight -- studio-quality, made in Aztlan, five years old, tuned to one person -- "
            "against her records."
        ),
    },
]

NPCS = [
    {
        "name": "Warren Cartwright",
        "role": "Acoustic guitar legend who coaxed Maria into an unsynthed jam at the Penumbra",
        "archetype": "Rocker",
        "title": "Musician (acoustic); friend of Maria Mercurial",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "He can make you cry, or dance, or anything when he plays. Heard Maria noodling on her 1965 "
            "Martin at home after a gig, went wild about it, and talked her into sitting in on his acoustic "
            "jam at the Penumbra last year -- no synthing, no amps, just old-fashioned miking and friends."
        ),
        "notes": (
            "One of the few people Maria calls family. No stats in the source. A back channel to Maria that "
            "bypasses Foley, Hernandez and the whole music-industry machine; a trusted friend who would "
            "notice if she went missing."
        ),
        "contact_skills": ["Seattle music scene (the acoustic / Penumbra crowd)", "Personal friend of Maria Mercurial"],
    },
    {
        "name": "Johnny Disk",
        "role": "Rocker Stars reporter who interviewed Maria and spotted the dreamchipper tells",
        "archetype": "Media Producer",
        "title": "Reporter, Rocker Stars newsnet",
        "race": "Human",
        "gender": "Male",
        "connection": 3,
        "description": (
            "The music reporter behind \"Rapping With A Rocker\" (Rocker Stars, February 12, 2050). Got two "
            "answers and a wall of small talk out of Maria in her condo, watched her switch personalities "
            "mid-sentence, and wrote that it was the classic sign of a ROM-burner -- and that he hoped she "
            "was off the BTLs, because this woman is for real."
        ),
        "notes": (
            "Rocker Stars is the leading rock newsnet and tridcasts Maria's Underworld 93 gig (channel 93, "
            "20 nuyen). Disk knows the rocker scene's history of chip-heads (Zango Wilkes of Astral "
            "Lightning suicided onstage the same way). A media contact who could break -- or bury -- the "
            "Perfekto story."
        ),
        "contact_skills": ["Rock journalism / Rocker Stars newsnet access", "Music-industry gossip"],
    },
]

# ----------------------------------------------------------------------------------------------
ORG_UPDATES = {
    "Shigeda-gumi": {
        "set": {"headquarters": "Seattle"},
        "description_append": (
            "A powerful Seattle yakuza syndicate. Runs dreamchips into the rock trade, holds loan-shark "
            "paper (Toroshi holds Max Foley's 500,000 nuyen), secretly owns New Horizons Development, and "
            "keeps an 'off-Matrix' policy for its real business. Its soldiers are cybered professionals who "
            "work in pairs, charge gunmen with katana out, and die rather than fail; its goons are tattooed "
            "irezumi legbreakers with stun batons who run when outmatched. Any Seattle runner knows the "
            "Shigeda are not to be messed with."
        ),
        "notes_append": (
            "Soldier block (p.44): Strength and Quickness boosted by muscle replacement 2, Wired Reflexes 1 "
            "(2D6 initiative), Stealth 6; armor jacket, HK227 with laser sight and silencer, katana, two "
            "concussion grenades. Sumiko brings (opposing characters minus one) soldiers to the hideout "
            "fight and cannot call reinforcements; they will fight Maria only with sheathed swords or bare "
            "hands. Goons (p.52): Fichetti Security 500, stun batons, lined coats; one is missing the little "
            "finger of his left hand. The Shigeda bribed a phone-company worker to plant a false directory "
            "number (555-7395) for Hernandez so 'Kathy Sakura' could intercept his calls; his real number "
            "is 555-9845. Sorayama's clinic in Chiba can call two Major League deckers from a Japanese "
            "yakuza syndicate. After the adventure the Shigeda still hold New Horizons and its poisoned "
            "land; Perfekto management is slated for replacement by Aztechnology and the Shigeda together."
        ),
        "leadership_add": [
            {"name": "Toroshi", "title": "Loan shark", "notes": "Holds Max Foley's 500,000-nuyen paper."},
        ],
        "allies_add": ["New Horizons Development"],
        "enemies_add": ["Perfekto Polymers"],
    },
    "Perfekto Polymers": {
        "set": {"headquarters": "Seattle (plant and Taetzel Building, Barrens); parent Aztechnology"},
        "description_append": (
            "Plastics manufacturing subsidiary of Aztechnology. In 2045 the bright lad running its Seattle "
            "plant cut costs by dumping industrial waste into a large underground tank instead of recycling "
            "it or hauling it to UCAS dump sites far from NAN territory -- and Seattle law comes down "
            "heavier on dumpers than on murderers. The cover-up shut the plant overnight, turned the "
            "neighborhood into a slum, and the only record of the tank's location went into Maria "
            "Aguilar's sealed memory."
        ),
        "notes_append": (
            "New Horizons' ultimatum: give up the tank's location and pay the clean-up, or the media get "
            "the story and New Horizons sues. Perfekto's own shadowrunners discovered New Horizons is a "
            "Shigeda front. The waste-dumping fallout could also wreck Aztechnology's delicate trade "
            "negotiations with the Seattle City Council. Happy-ending news: Perfekto under City Council "
            "investigation with 'damning' documentation, the Salish-Shidhe Council's formal protest, CEO "
            "Andrew Masterson dead of a 'heart attack' on Queen Anne Hill, Seattle GM Miguel Allende away "
            "at a 'special managerial briefing' with no return date. Management slated for wholesale "
            "replacement."
        ),
        "enemies_add": ["New Horizons Development", "Greenwar"],
    },
    "New Horizons Development": {
        "description_append": (
            "Armed with inside information about a coming corporate expansion nearby (Mitsuhama's new "
            "regional center), New Horizons spent a year quietly buying the slum around the old Perfekto "
            "plant to renovate it into condos for the suits who will work there. Its Matrix presence is a "
            "wide-open Blue network of perfectly legal zoning and licensing agreements and publicity about "
            "reviving the Barrens; the real business is kept off the Matrix on purpose."
        ),
        "notes_append": (
            "Construction stopped the day Perfekto warned of the buried waste. The company's 'upper "
            "management' -- the Shigeda -- called for stronger measures than lawsuits. The only properties "
            "it does not own in the area are the plant and the Taetzel Building. Max Foley only ever heard "
            "that 'larger issues' involved something called New Horizons."
        ),
        "allies_add": ["Shigeda-gumi"],
    },
    "Dragon Knights": {
        "description_append": (
            "Codename for the Aztechnology troubleshooting team flown to Seattle under Kyle Morgan, the "
            "corp's court of last resort. Cadre per Morgan's own resources file: Kyle Morgan (team leader), "
            "Perianwyr (team second and 'Occult Services'), Jorge Mixacopotec (security), Blackstone "
            "(technical services), Lin Hwang (computer services), plus fifteen corporate agents, four of "
            "them trained as handlers for Perianwyr's griffins, cockatrice and basilisk. Funded through an "
            "open credit account with Orbital Credit Bearnaise (750,000 nuyen behind Scramble 8)."
        ),
        "notes_append": (
            "Agents are Corporate Security Guard archetypes with Heavy Weapons 3: FN HAR with laser sight "
            "and gas vents, Fichetti Security 500, partial heavy armor and helmet in unmarked black-and-gray "
            "urban camo, low-light goggles; two per squad carry missile launchers with anti-vehicle "
            "missiles. Two modified Chrysler-Nissan Patrol-1s (medium MG, twin AVM launchers). Agents "
            "surrender when trapped, resist interrogation at TN 10, admit only that orders came from a "
            "scarred Indian with an Aztlan accent, and vanish from police custody within hours. Morgan's "
            "unnamed Mr. Johnson (scrambled voice) orders 'any means necessary'; the mission fails if the "
            "runners go public with the sealed-memory data -- the Knights leave within three hours and the "
            "Taetzel burns. Orders on file: liquidate Blackstone after the mission."
        ),
        "leadership_add": [
            {"name": "Perianwyr", "title": "Team Second / Occult Services", "notes": "Western dragon."},
            {"name": "Jorge Mixacopotec", "title": "Security", "notes": None},
            {"name": "Blackstone", "title": "Technical Services", "notes": "Marked for liquidation after the mission."},
            {"name": "Lin Hwang", "title": "Computer Services", "notes": None},
        ],
        "allies_add": ["Aztechnology", "Shigeda-gumi"],
    },
    "Federated Funds Net": {
        "description_append": (
            "A 'tin-plated, rinky-dink' operation on Twelfth Avenue that a lot of show-business people use "
            "because its tax reporting and record-keeping understand the demands the business makes on "
            "cash flow. Cannot afford deckers on retainer: on External Alert the operator simply starts a "
            "2D6-turn shutdown."
        ),
        "notes_append": (
            "System on LTG #7206; each account file carries Scramble 3 and a failed unscramble dumps the "
            "account off-line. Hernandez's 90 Mp file (180,000 nuyen of Maria's concert fees) is the only "
            "account worth more than a few hundred nuyen. Foley's one-way deposit code feeds his own bank "
            "on LTG #9206 for a 10 percent finder's fee. A decker investigating the emptied account (TN 4, "
            "three successes, Red node) sees the same fingerprints as the decker who invaded Hernandez's "
            "office computer -- Gum E. Bear."
        ),
    },
    "Citizens for a Decent Society Policlub": {
        "notes_append": (
            "Its Seattle branch announces an 'immediate inquiry into the behavior of public performers' if "
            "Maria is hospitalized after a BTL relapse; chairwoman Margot Tipper: \"what kind of decent "
            "woman does things like that?\" Maria's tour was picketed by policlubs she calls corporate "
            "front groups."
        ),
    },
    "Salish-Shidhe Council": {
        "set": {"headquarters": "Salish-Shidhe Council lands surrounding the Seattle metroplex"},
        "notes_append": (
            "The Treaty of Denver is sudden death on industrial pollution in or bordering NAN territory; "
            "hot enough, the neighboring councils could press to strip a polluter of its Seattle license. "
            "Underworld 93's 'Pure Earth' foods come out of the Tribals' turf."
        ),
    },
    "Aztechnology": {
        "notes_append": (
            "Mercurial: Reynaldo Texamachach kept an indentured girl (Maria Aguilar) as bodyguard, "
            "secretary and mistress, rebuilt by Sorayama in Chiba on an open credstik in 2044, with a "
            "sealed memory space transparent to scanners and a datajack routed through her pleasure/pain "
            "centers, then addicted to custom chips; she killed him in his suite in the Seattle Pyramid in "
            "2045. Corporate policy afterwards: revenge doesn't show on the bottom line -- until the "
            "Perfekto tank made her memory worth killing for. Kyle Morgan has been the corp's court of last "
            "resort for ten years. The Dragon Knights' Mr. Johnson orders any means necessary and reminds "
            "Morgan that upper management is watching. Aztechnology keeps its less-loyal employees' "
            "families in 'corporate dependents' facilities' (velvet-lined prisons); Blackstone's wife died "
            "under 'intensive interview'. Trade negotiations with the Seattle City Council were at risk "
            "from the dumping scandal. Epilogue: Morgan and Perianwyr are alive on the Pyramid roof at dawn."
        ),
    },
    "Lone Star Security": {
        "notes_append": (
            "Mercurial: Lone Star patrols Underworld 93 on big nights (twelve private guards with gel "
            "rounds, tasers and stun shotguns inside; police in five minutes) and does not want incidents "
            "with so many important people present. Getting hauled in means a couple of hours in a holding "
            "cell, statements on the record, and a back-room 'discussion' for the SINless (4M3 stun). Bail "
            "500 nuyen each."
        ),
    },
    "Mitsuhama Computer Technologies": {
        "notes_append": (
            "Opening a new regional manufacturing and sales center next year about two kilometers from the "
            "old Perfekto Polymers neighborhood in the Barrens -- the expansion New Horizons Development "
            "was front-running (Mercurial, p.51)."
        ),
    },
}

LOC_UPDATES = {
    "Underworld 93": {
        "set": {"district": "Puyallup Barrens (fringe)"},
        "description_append": (
            "Anyone who knows the scene knows Underworld 93. A five-story converted industrial warehouse on "
            "the fringe of the Puyallup Barrens, gutted to a cavernous post-industrial, rust-belt interior "
            "-- a favorite of everyone who likes their rock and roll meltdown-hot, where Barrens street "
            "slime rubs shoulders with Bellevue shaikujin. Two Kromeglow marquees lay meter-high letters "
            "over vids of the acts, topped by the club's logo: Charon steering a speedboat across the Styx. "
            "Newt the troll works the main doors in a tuxedo (a private entrance to the left for "
            "passholders); a sweeping ramp runs down from the lobby to the dance floor; spiral staircases "
            "climb to catwalks, balconies and booths hung from the walls, with windows so the people inside "
            "can watch the people trying to get in. The Beast, a ten-meter bald bullet-headed mascot "
            "sculpture, lashes lasers from its eyes, pumps the stage mix from a speaker in its belly and "
            "flashes subliminal 'Question Authority' and 'Love Is the Law' through its holograms. Tellin "
            "runs the bar with half a dozen barkeeps and holds his information exchanges in the alcove by "
            "the storeroom. Owner Sidney Murdoch has a knack for booking struggling acts that become "
            "chartbusters, and they keep coming back; Maria played her first set here in '47."
        ),
        "notes_append": (
            "Full map key pp.14 and 23. Weapons bigger than a pistol are checked at the armor-glass booth "
            "(no exceptions, whoever invited you). Twelve private guards with Fichetti Security 500s loaded "
            "with gel rounds, two tasers, one stun shotgun; Lone Star in five minutes. Backstage is a flimsy "
            "four-meter construction-plastic box (Barrier 4): a dwarf doorman in a holoprint-dragon jacket, "
            "lounge, stage mirror with synthlink check, the master control and patch console for every "
            "light and effect in the house, storage (Medikit in the red-cross cabinet), dressing rooms 8-12, "
            "and Dressing Room One with private bath, bar, trid and a practice synthlink rig. Murdoch's "
            "office wall trid pulls any camera in the club. The club's hearth spirit (any shaman conjuring "
            "inside gets it): a meter-tall figure in black denim, silver-skull boots, chains and mirrored "
            "shades, dreadlocks, a solid-gold Fender spelled out in diamonds; its ear-splitting chord "
            "always hits everyone in the area for (Force)M2 stun vs Willpower, and it talks in "
            "late-20th-century rocker slang (\"Peace, love, and waterbeds!\"). Treat it with courtesy and it "
            "may invite the shaman back for a chat once he has his act together. Newt's lime-green van with "
            "the purple racing stripe is parked in the alley."
        ),
    },
    "Federated Funds Net (Offices)": {
        "set": {"district": "Twelfth Avenue, Downtown"},
    },
    "Hernandez's Brownstone & Studio": {
        "description_append": (
            "An old brownstone in a gentrified downtown neighborhood that largely escaped the urban "
            "makeovers of the past century. Ground floor: waiting room, Armando's office (messy desk, the "
            "office computer, a control panel under the glass looking into the studio, shelves of "
            "magazines, technical manuals and antique hardback fiction, pictures of Maria everywhere), a "
            "state-of-the-art recording studio, and a library of thousands of volumes with a terminal and "
            "a copy of Don Quixote open face-down to the chapter where Quixote first meets Dulcinea. "
            "Upstairs: bedroom with Maria's picture by the bed, kitchen, dining room."
        ),
        "notes_append": (
            "Break in and he is asleep on the office couch with an empty tequila bottle; mention Maria and "
            "he sobers. Office system (Computer TN 5 at a terminal / TN 4 decking, cumulative successes): "
            "1 -- the crash weeks ago was a decker; 2 -- a sloppy one who left fingerprints all over the "
            "Matrix; 3 -- fragments of the files Maria erased; 4 -- reconstructed payment records 'proving' "
            "Hernandez fronted Shigeda dreamchips into the rock trade; 5 -- data trails where someone pried "
            "out his Federated Funds Net access code. He bought tougher IC for his SAN after the crash. His "
            "real phone number is 555-9845 (answering machine plays 'Who Weeps For The Children?'; a "
            "message mentioning Maria brings him on the line); the directory's 555-7395 is the yakuza's "
            "intercept. His weapons and armor are in a locker."
        ),
    },
    "Star Gardens Endominium": {
        "description_append": (
            "Forty-eighth floor penthouse, four-meter ceilings, impact-plastic walls (Barrier 5): a "
            "camera-scanned corridor that doubles as a bar and buffet when Maria entertains; a living room "
            "built around a circular conversation pit and a raised holographic fireplace (she is an "
            "ecology supporter and burns nothing), a floor-to-ceiling vidscreen, a trid console with every "
            "gimmick except simsense, an autobar, and a glass wall that slides into the ceiling onto a "
            "rooftop garden with trees, a swimming pool and a whirlpool; kitchen (peanut butter, grape "
            "jelly and protobread on the cutting board when the staff are off); formal dining room, small "
            "parlor, guest room with VibraSkrub sonic shower, storage with the household servo units; her "
            "bedroom with a Muzeeka 9000 synthlink and a 1965 Martin acoustic with rosewood inlays "
            "(25,000+ nuyen) in a locked climate case; a half-million-nuyen recording studio with a "
            "Mitsuhama BandBox and a Konzert Acoustic Modulator; a Japanese-style private garden planted "
            "entirely with Central American vegetation; and a gymnasium with Sendai-Nautilus gear, a "
            "Shiatsu-Matic, a cyberware diagnostic unit, and a holographic pistol range."
        ),
        "notes_append": (
            "Correction to the earlier note: the pleasure/pain datajack wiring was Sorayama's work for "
            "Texamachach, not something installed in the condo. Every household control has a keypad and "
            "she only ever uses the manual controls (Intelligence TN 5 to notice); she jacks in only to "
            "synthlink her music. Floor plan p.30-31. A luxury lifestyle showcase if the team holes up here."
        ),
    },
    "Rent-a-Hideout Warehouse": {
        "description_append": (
            "A single-story, ten-meter-tall warehouse in an abandoned Barrens industrial park: office, "
            "empty storage, bathroom, locker room, a hall of unclaimed shipments stacked six meters high "
            "(hard cover; Strength TN 12 to topple a stack for 6M2 stun), a working Mitsubishi Jacklift "
            "cargo handler with rigger and manual controls (grappling arms, effective Strength 12, 6M2, +2 "
            "to all combat tests), a lounge with a battered trid and cheap furniture, flimsy screens around "
            "cots, and a kitchenette. Windows paneled with thick impact plastic (Barrier 10), exterior "
            "doors reinforced steel under veneer (Barrier 24), tooled-steel locks (Strength TN 15 to break, "
            "TN 12 to pick)."
        ),
        "notes_append": (
            "500 nuyen a day (landlord Negotiation 3, TN 6, minus 50 per net success). Miss a payment and "
            "the landlord sells the address to the street and the reward. 'Abandoned Building Sites, Ltd. "
            "Ideal for shadowrunners, terrorists, spies. Will redesign to suit.' The lounge is where Sumiko "
            "offers Maria the dreamchip. Max phones the hideout's details to Sumiko from the bathroom. "
            "Perianwyr burns it at the start of Part Two (4M3 to get out; explosive rounds cook off on a 6); "
            "Franklin Co. firefighters and a DocWagon arrive in ten minutes -- a 'real' hospital, not a "
            "secure one."
        ),
    },
    "Old Perfekto Polymers Plant": {
        "description_append": (
            "A big abandoned factory in a maze of old buildings, dead office blocks and the usual debris, "
            "the one property in the neighborhood New Horizons could not buy. Perianwyr's descent toward "
            "his lair leads pursuers here, into missile fire from Dragon Knights agents on the ground."
        ),
    },
    "Taetzel Building": {
        "description_append": (
            "Festung-style: solid concrete to the 20th floor (Barrier 32), mirrored reinforced armor glass "
            "above (Barrier 8) where the executives had their view. A core of four passenger elevators "
            "flanked by stairwells, a freight elevator and back stairs. Three-meter chain-link fence with "
            "pressure sensors (Intelligence/Electronics TN 4 to spot, Electronics TN 6 to disarm), two "
            "agents circling the grounds every 15 minutes, weed-cracked parking lots, main gate opened from "
            "the 28th floor, rear gate and loading dock. Roof: a helipad raised five meters over Perianwyr's "
            "den (gnawed sides of beef, a 100-liter vat of beer, a voice-controlled trid with thousands of "
            "rock recordings from the 1950s to the latest Mercurial hit), air-conditioning plant, "
            "communications shack with the satellite dish that feeds the Knights' mainframe, elevator "
            "machinery."
        ),
        "notes_append": (
            "Ground floor (p.63): lobby with camera and servogun watched from an armor-glass guard booth "
            "(FN HAR firing port, building alarm); basilisk lair in a converted office; inner lobby with two "
            "servoguns; loading dock with the cockatrice, two modified Patrol-1s and crates of 'Office "
            "Supplies' holding two missile launchers and 8 AVMs; rear entrance with two agents. Servoguns: "
            "Firearms 6 at short/medium range, 4M3, initiative 20, Body 4, partial cover. The passenger "
            "elevator freezes at the 11th floor and drops after three turns (4D2) unless the computer is "
            "controlled; Strength TN 8 (6 with tools) to force the doors, TN 4 to smash the hatch. 28th "
            "floor (p.64): elevator core with two camera/servogun pairs and two agents; Morgan's luxurious "
            "quarters (photos with simsense star Beauty Shannon in his sports car, an old flat photo of a "
            "gangly teenage Morgan against a dragon marked 'Llawrgwynedd 2022' on the back, the Command "
            "Terminal -- Computer TN 8, ten minutes divided by successes); Mixacopotec's spartan quarters "
            "with an obsidian-spiked war club; Lin Hwang's quarters with deck and terminal; conference room "
            "with a trid tank of photos, maps of Maria's and Hernandez's homes and possibly of the runners; "
            "kitchen with a locked liquor cabinet; computer room; 16-bunk barracks; gymnasium (Maria bound "
            "here, guarded by a visibly upset dwarf); armory (cardkey or passkey + Electronics TN 8: six FN "
            "HARs, four Predators, two missile launchers, grenades and explosives); security center with "
            "the Security Terminal (Blackstone and one agent); Blackstone's cluttered quarters with a holo "
            "of his wife and two-year-old son. Guards carry portable phones the computer cannot block. "
            "Agent tactics: two groups to surround if the cameras work, otherwise four groups sweeping down "
            "both stairwells with the elevators disabled; they break at two-to-one losses. Only Perianwyr "
            "or Morgan can control a creature whose handler dies; the dragon can command the cockatrice and "
            "basilisk from astral space but not the griffins."
        ),
    },
    "Sorayama's Clinic (Chiba)": {
        "set": {"district": "Chiba prefecture, Japan"},
        "description_append": (
            "Chiba cyber is top-of-the-line, leaving anything else buried in the dust. Sorayama does about "
            "fifty modifications a year at three to five times normal prices, treats his skills like an "
            "art, and signs only his 'Ultra' masterpieces -- each a unique job, about 120 to date, number "
            "84 done in 2044. Rumor says a lot of his borderline work is modifying people into toys for "
            "corporate clients, like human bonsai trees."
        ),
        "notes_append": (
            "Legwork: Etiquette (Street) or Biotech at TN 8 (leads table p.53; a Seattle hot-cyberware fixer "
            "sells the current system address for 1,000 nuyen). Host details in the prep doc: the customer "
            "record store holds Maria's 20 Mp file (keywords '84 Sorayama', 'Aztechnology', 'Mercurial') -- "
            "the Ultra #84 commission, the sealed memory, the pleasure/pain datajack, ten days of forced "
            "custom-chip exposure -- and an entry two months ago noting an Aztechnology rep requested a "
            "copy, delivered to LTG #6206, Kyle Morgan's mainframe. The R&D store holds eight cybermod "
            "design files (530 Mp total, 20,000 nuyen per 10 Mp, or install them at 25-50 percent less "
            "Essence for double price); Sorayama hunts thieves through yakuza connections and the code "
            "calls for death to vendor and receiver alike. CPU credit file: 500,000 nuyen behind Black-4."
        ),
    },
    "Aztechnology Pyramid": {
        "notes_append": (
            "Mercurial: Reynaldo Texamachach's suite here is where Maria Aguilar blew his brains out in "
            "2045 before fleeing into the Barrens. In the epilogue Kyle Morgan limps in from the helipad at "
            "dawn with Perianwyr's wings gold in the sunrise -- a sleepy guard offers him a light."
        ),
    },
    "Club Penumbra": {
        "notes_append": (
            "Mercurial: Warren Cartwright's acoustic jam here last year -- no synthing, no amps, just "
            "old-fashioned miking -- is the only time Maria Mercurial has performed unsynthed in public "
            "(Rocker Stars interview, Feb 12, 2050)."
        ),
    },
    "The Barrens (Seattle)": {
        "notes_append": (
            "Mercurial: Seattle's own little heart of darkness -- the razor-guy dives like The Armadillo, "
            "the cheap brothel where Hernandez found Maria singing a cantamuerte, the rent-a-hideout "
            "industrial parks, the slum that grew around the shuttered Perfekto plant, and the Taetzel "
            "Building at its center."
        ),
    },
}

NPC_UPDATES = {
    "Kathy Sakura": {
        "set": {
            "name": "Sumiko Hotoda",
            "title": "Shigeda-gumi kobun mage; alias \"Kathy Sakura\", Talent Contract Manager",
            "nationality": "Japanese",
        },
        "description_append": (
            "Pure-blood Japanese, late thirties, very attractive; as 'Kathy Sakura' she wears a severe dark "
            "business suit and a few pieces of elegant, simple jewelry whose occult symbolism is exactly "
            "correct -- they are working foci (Sorcery TN 4 to notice). The very image of subdued oriental "
            "femininity one minute and cold-blooded efficiency the next; in the field she wears street "
            "armor and carries an ornate walking stick (her power focus)."
        ),
        "background_append": (
            "Trained by a major Japanese corp, she got fed up with the ingrained sexism of the zaibatsu "
            "structure and emigrated to Seattle, ran missions for the underworld, and formally entered the "
            "Shigeda-gumi four years ago. No foolish notions of honor or courage: she leads from the rear, "
            "shoots from ambush, keeps the yakuza code only as far as her obligation to the Shigeda "
            "requires, and kills without hesitation anyone in her way."
        ),
        "notes_append": (
            "Stats (p.43): B3 Q3 S3 C5 I6 W5, Ess 6, Magic 5 (7 with power focus), Reaction 5(9) from a "
            "spell-locked Increase Reaction (three initiative dice); Sorcery 7, Conjuring 4, Firearms 6, "
            "Monofilament Whip 5, Unarmed 5, Karate 6; Astral pool 18. Gear: Ares Predator (explosive, "
            "laser sight), armor jacket, staff (+2 power focus), medallion (+2 Ignite spell focus), "
            "monofilament whip. Spells: Mana Bolt 7, Sleep, Analyze Truth 4, Detect Enemies 6, Increase "
            "Reaction, Heal Severe Wounds 5, Barrier 7, Ignite 6, and the unpublished Force 5 'Eyes of the "
            "Pack' (sees through her drugged samurai's eyes -- which is why they glow). Runs the "
            "555-7395 intercept line and offers 20,000 nuyen for Maria's whereabouts, never intending to "
            "show up. Perianwyr burns her (and her walking stick) at the start of Part Two if she survived "
            "the hideout."
        ),
    },
    "Maria Mercurial": {
        "set": {"nationality": "Aztlan (indentured to Aztechnology)"},
        "description_append": (
            "Mid-twenties. Arms, legs and face of mirror-bright metal that throws the spotlights back in a "
            "cascade of color, golden hair like a solar corona around a silver moon, an athlete's torso -- "
            "and deep brown, living human eyes Texamachach left unaltered, which make people want to cry "
            "or kill something. Excellent English with an Aztlan accent; excited, she mixes Aztec and "
            "Spanish into it. On stage the Amazon prowls like a silver panther radiating sexuality and "
            "danger; after a show the Schoolmistress emerges in a tightly belted padded kimono, quiet and "
            "factual; the Innocent, rare, is a trusting child. Off duty she dresses in black armorcloth with "
            "silver splints and opaque vision-augmenting shades, and unwinds in razor-guy dives by "
            "starting fights. Her stage rig is a synthlink -- every tone driven by muscle and nerve. High on "
            "one silver thigh: the imprint '84 Sorayama'."
        ),
        "background_append": (
            "Indentured young to Aztechnology; Texamachach had her rebuilt by Sorayama (Ultra #84, 2044) "
            "with a sealed memory space transparent to scanners and a datajack routed through the limbic "
            "pleasure/pain centers, then addicted her to custom chips over ten days. Killed him in the "
            "Seattle Pyramid in 2045 and fed the habit as a working girl in a Barrens brothel until "
            "Hernandez heard her sing a cantamuerte, killed her pimp, and put her through Dr. Kenner's "
            "clinic. She kept her working handle. The Sorayama circuitry let her sublimate the addiction "
            "into synthlinking and gives her unconscious control over the sealed memory -- she can hold "
            "out against the recovery code ('Silver Virgin') for days. Albums 'Night Tears' and 'Puta'; "
            "singles 'Who Weeps for the Children?', 'Take It To Mister', 'Shadow Storm'. Her home is a "
            "1.5-million-nuyen penthouse at Star Gardens Endominium; her limo is a mirror-chromed "
            "Mitsubishi Nightsky with an armed driver."
        ),
        "notes_append": (
            "Constants across all three personas: she loves and respects Hernandez more than she admits, "
            "denial is her main defense, she will not admit to dreamchips or memory loss, and she will not "
            "discuss her cyberwork. Only a confession from Foley convinces her Hernandez was framed, and "
            "even then she is too ashamed to call him. Faced with Sumiko's dreamchip she sinks to her knees "
            "and jacks in within five turns; re-addicted, she goes into a coma that may burn out her nervous "
            "system. Stats (p.71, partly illegible in scan): Quickness 5(6), Strength 4(5) from muscle "
            "replacement, Intelligence 4, Willpower 5, Reaction 5(7) from wired reflexes; datajack "
            "(limbic-routed), silver dermal replacement, cortical implants; Browning Max-Power. Karma: 1 "
            "each for keeping her alive, keeping her off the chip, and revealing the sealed data. Happy "
            "ending: she marries Hernandez at City Hall and cancels her tour."
        ),
    },
    "Max Foley": {
        "set": {"organization_id": None},
        "description_append": (
            "Short, fat and balding, in his fifties, complexion like week-old nutrisoy, fashions suited to "
            "a teenager, fat greenish cigars, rings on most fingers and a mass of real gold that looks "
            "cheap on him -- anything within three meters of Max Foley seems to become cheapened. A talker: "
            "'am I right?' ends every sentence. Like some greasy idiot savant he can scope a hundred nowhere "
            "bands and pick the chartbuster."
        ),
        "notes_append": (
            "Negotiation 7 (TN 5 once he is scared); every net success adds 500 nuyen per runner, or 1,000 "
            "per runner in legitimate expenses (gear, ammo, medical, bail). Offers the decker Federated's "
            "address on LTG #7206, Hernandez's account code and a deposit-only feed to his own bank on LTG "
            "#9206 for a 10 percent finder's fee. Interrogation TN 11 (Willpower +6) or TN 8 with physical "
            "persuasion to admit the Shigeda connection; he does not know the real plan is to kill Maria. "
            "His host (7 nodes, guarded by Gum E. Bear) holds Sumiko's 'keep the woman with you' message, "
            "his real earnings (blackmail material), a coded bank interface with 300,000 nuyen (180,000 of it "
            "Hernandez's), and a diary entry: 'Mrs. Foley's little boy is saved... Is this a great country, "
            "or what?' Faints after the shootout; dives for cover in every fight; if let go, Perianwyr "
            "burns him outside the hideout ('Hey, not me, am I RIIIGHT--'). Stats: Body 2; Streetline "
            "Special."
        ),
    },
    "Armando Hernandez": {
        "set": {"organization_id": None},
        "description_append": (
            "Mid-forties, husky, middle height, black hair shot with gray, pleasantly ugly with a nose "
            "broken more than once. Quiet unless he is putting on the act to get a contract signed, when "
            "he comes on strong with Aztlan machismo. Found drunk on his office couch, bloodshot, "
            "steadied only by talking about Maria."
        ),
        "background_append": (
            "Emigrated from Aztlan in the 2020s at the founding of the new regime, whose politics his "
            "liberal views did not suit; a UCAS citizen now. Once Maria's career took off he handed his "
            "other acts to other agents and worked with her exclusively."
        ),
        "notes_append": (
            "Skills include Etiquette (Show Biz) 6, Etiquette (Street) 2, Firearms; gear Beretta 101T, "
            "Defiance T-250, lined coat. When he learns Maria is in danger the theatrical rage vanishes and "
            "he quietly pulls his weapons and armor from their locker; nothing short of knocking him cold "
            "stops him coming, and at the hideout he charges Sumiko berserk. If the runners kill him, Maria "
            "becomes an implacable, wealthy enemy. Karma: 1 for keeping him alive."
        ),
    },
    "Kyle Morgan": {
        "set": {"nationality": "Welsh"},
        "description_append": (
            "Mid-forties and as fit as a man half his age, handsome, one of the Sixth World's premier "
            "assassins -- which is why you have never heard of him. Known under various aliases as a rally "
            "driver and a useless drone on the glitter scene of the international jet set. Smokes black "
            "and gold Sobranies."
        ),
        "background_append": (
            "A Welsh farm boy who in 2022 stood off a mob of shotgun-toting farmers with a rusty shotgun and "
            "charisma to save a newly awakened, sheep-glutted dragon; the photo in his quarters is marked "
            "'Llawrgwynedd 2022'. Twenty-five years of partnership in the world's shadows; ten years as "
            "Aztechnology's court of last resort. He and Perianwyr have big plans that will make them "
            "powers in the Sixth World or get them killed, and are increasingly disenchanted with their "
            "corporate masters."
        ),
        "notes_append": (
            "Stands aloof from the Taetzel fight, monitoring from the Command Terminal, then the security "
            "center, then the roof. Cornered without Maria he attacks blazing away, seeking cover from "
            "nothing -- fighting to die, not to kill; if Perianwyr is wounded his concentration breaks and "
            "he reaches for a grenade. With Maria captive he shoots Mixacopotec off her ('And then there was "
            "one') and then attacks. Blasted out the window, his body is never found; the epilogue has him "
            "alive at dawn on the Pyramid roof, planning to hear Maria sing. Gear (p.66, partly illegible): "
            "datajack, smartgun link, Wired Reflexes 2; armor jacket; Ares Predator smartgun with explosive "
            "ammo, Ares Viper Slivergun, Ranger Arms SM-3 sniper rifle; Firearms 4+. Juggles Maria's 'Night "
            "Tears' CD during his Mr. Johnson's call."
        ),
    },
    "Perianwyr": {
        "set": {"race": "Western Dragon", "archetype": "Dragon", "nationality": "Welsh"},
        "description_append": (
            "A Western dragon with a taste for vintage rock and roll (History of Rock and Roll 6) and beer "
            "by the 100-liter vat; speaks Ancient Celtic, Latin and Welsh; a rumbling basso profundo. "
            "Regards Morgan as his only friend, the only being for whom he feels affection; may respect or "
            "fear the mightier of his own kind, but only this fierce and loving human has a fire of spirit to "
            "match his own."
        ),
        "notes_append": (
            "Stats (p.67, partly illegible): Body 15/4, Intelligence 5, Willpower 8, Essence 8; Sorcery 6; "
            "powers: Animal Control (reptiles), enhanced senses (low-light, wide-band hearing), flame "
            "projection (8L1), flight. Spells: Mana Bolt 6, Sleep 8, Mind Probe 6, Heal Deadly Wounds 8, "
            "Invisibility 6, Magic Fingers 6. Flies invisible (Intelligence TN 3 with radar or astral senses "
            "to spot); attacks astral pursuers and lands only under his lair's missile cover. Trained the "
            "Taetzel's two griffins, cockatrice and basilisk. Stays aloof from the final battle unless "
            "Morgan is threatened; hovers outside shouting 'Kyle, get DOWN'; after Morgan falls he "
            "bellows, flames, and dives into the smoke after the body. Never seen again -- until dawn."
        ),
    },
    "Jorge Mixacopotec": {
        "set": {"race": "Human", "nationality": "Aztlan"},
        "description_append": (
            "A heavily scarred Indian with a thick Aztlan accent -- the face the Dragon Knights' agents "
            "and Snout describe. Keeps an obsidian-spiked war club on his wall. Like a slasher-movie "
            "villain he is back on his feet for the last scene even if the runners killed him earlier."
        ),
        "background_append": (
            "Fought to survive the slums he was born in, then as a gladiator in the blood sports of the "
            "2050s; after a spectacularly bloody trid career he became an Aztechnology mercenary. Knows only "
            "two ways to end a fight."
        ),
        "notes_append": (
            "Gear (p.68): Ingram Valiant with deluxe gyro mount (rating 6), Browning Max-Power smartgun, "
            "three aerodynamic defensive grenades, partial heavy armor and helmet. Leads one agent group "
            "down the central stairs. Pays Snout 500 nuyen for the runners' hideout. Shot dead by Morgan "
            "over Maria's bound body, syringe and dreamchip injector in hand."
        ),
    },
    "Blackstone": {
        "description_append": "Dwarven Technician archetype with the stereotypical dwarven brilliance with technology.",
        "background_append": (
            "Indentured to Aztechnology by a state creche; trained, married and became a father under "
            "corporate regulation, his wife and son kept in a 'corporate dependents' facility'. His wife "
            "tried to escape with the child, was caught, and 'succumbed to intensive interview'; the boy is "
            "missing, presumed with dissidents in the slums of Aztlan. Morgan's orders on file: liquidate "
            "this agent on completion of the mission."
        ),
        "notes_append": (
            "Will NOT fight, and will actively turn the building security system to the runners' side if "
            "they tell him what happened to his family (the message is in Node 3B). Will not willingly face "
            "death because he still hopes to find his son. Mans the Security Terminal with one agent; the "
            "visibly upset dwarf with a heavy pistol guarding Maria in the gymnasium."
        ),
    },
    "Lin Hwang": {
        "set": {"nationality": "Macao (Chinese)"},
        "description_append": (
            "Middle-aged. Matrix persona: a sleek gold-skinned robot in crackling electric-blue tunic and "
            "pants swirling with yin/yang symbols, neon tattoos on the forearms -- a dragon on the left that "
            "breathes fire when he attacks, a tiger on the right that roars and absorbs attacks when he "
            "shields -- and a faint tinkling of wind chimes and tiny gongs when he moves or speaks."
        ),
        "background_append": (
            "Trained as a decker by a Macao Triad of the old school; betrayed his fellows to the police "
            "during a major datasteal, kept the take, and fled to the Americas. Serves Aztechnology for "
            "protection and profit; failure could mean exposure to the Triad, so he fulfils missions to the "
            "letter."
        ),
        "notes_append": "Reaction 4 (10 in the Matrix); Decking 6, Firearms 3, Unarmed 4; Hacking pool 6; datajack with 100 Mp. Jacks in the moment an External Alert fires on either Taetzel system.",
    },
    "Newt": {
        "description_append": (
            "An oversized troll in a nattily tailored tuxedo of armor cloth (Ballistic 3), the Underworld's "
            "arbiter of elegance: nobody gets in who is not macroflash or outrageously grungy enough to "
            "please his sense of the grotesque. Talks like a movie gangster ('Awright, yer in. Enjoy da show "
            "and don't make no trouble'). Carries no firearm -- but keeps a large axe (treat as a pole arm)."
        ),
        "notes_append": (
            "Troll Bouncer stats (SR1 p.173). Turns the runners away, then lets them in on Foley's phone "
            "call. Brings the checked weapons backstage after the shootout and hands over the keys to his "
            "lime-green van with the purple racing stripe in the alley -- 'Dis ain't on accounta youse. It's "
            "on accounta her.' Cavalry option: attacks Samurai #3 from behind with the axe."
        ),
        "contact_skills_add": ["Underworld 93 door and security", "A van when you need one"],
    },
    "Tellin": {
        "description_append": (
            "A tall, typically handsome elf behind the central bar with a sly smile ('I've been expecting "
            "you'). Everyone who comes to Underworld 93 for information ends up in his alcove by the "
            "storeroom. Translates Newt into English with a sigh."
        ),
        "notes_append": (
            "A vending machine: 50 nuyen per question (answers on Maria, Foley and Hernandez, pp.16-17 -- "
            "'Nuyen to nutrisoy, that's what Foley wants to talk to you chummers about'). Biotech 7; patches "
            "the wounded from the storage-area first-aid kit. Cavalry option: snipes with an assault rifle "
            "from a trapdoor in the ceiling."
        ),
    },
    "Sidney Murdoch": {
        "description_append": (
            "A middle-aged guy with a big gut in a grungy Underworld 93 T-shirt who leads the applause "
            "center-stage and introduces the acts: 'Right, you brain-damaged, re-wired mutants!... Ladies "
            "and gentlemen -- if there are any out there -- and all the rest of you trash as well, here's "
            "MARIA MERCURIAL!'"
        ),
        "notes_append": (
            "Booked Maria on an open contract the moment he heard her sing in '47, after Hernandez camped a "
            "week in his waiting room. Calls the Beast the club's mascot and refuses to explain the private "
            "joke. His office wall trid pulls any camera in the club; would-be rockers wait in his outer "
            "office for auditions by day."
        ),
    },
    "Gum E. Bear": {
        "description_append": (
            "Hired help. If he loses sight of an intruder or takes too much of a beating he jacks out and "
            "starts the shutdown -- he is not paid enough to worry about what the invader does in the "
            "meantime."
        ),
        "notes_append": (
            "Deck: Fuchi Cyber-7 with Level 1 Response Increase; programs Bod 5, Evasion 4, Masking 4, "
            "Sensors 6, Attack 6, Medic 8, Shield 3. Not very good: left fingerprints all over Hernandez's "
            "system and the emptied Federated account. Foley's SAN now runs Trapped Access 4 with Killer 5 "
            "gray IC because Max got nervous."
        ),
    },
    "Snout": {
        "description_append": "A small-time ork goon and snitch. Blindfolded for the meet, he sneaked a peek -- the Taetzel Building.",
        "notes_append": "Fingers a runner's home or hideout for Kyle Morgan's agents (Knock, Knock, p.57), then buys the house a round at The Down And Out. Folds at the slightest threat.",
    },
    "Sorayama": {
        "set": {"nationality": "Japanese"},
        "description_append": (
            "A brilliant, eccentric Chiba street doc who treats cyberware as art: about fifty jobs a year at "
            "three to five times the going rate, and a signature only on the 'Ultra' masterpieces. Keeps "
            "clinical notes in the tone of a connoisseur ('even when nature accidentally creates such "
            "beauty, art can improve on it'); mildly pleased to spot Ultra #84 on tri-vid and mulls a "
            "monograph."
        ),
        "notes_append": (
            "Maria's file: commissioned 06/13/44 by 'Johnson-san' (an Aztechnology rep), subject Maria "
            "Aguilar under standard indenture; dermal replacement, reflex and muscle work, cortical implants, "
            "an ultra-secure sealed memory transparent to scanners, datalink plugs routed through the "
            "pleasure/pain centers ('acceptable to the client'), synthlink training, ten days of forced "
            "high-amplitude custom simsense. Sent a copy to Kyle Morgan's mainframe (LTG #6206) two months "
            "ago. Hunts data thieves through yakuza connections; can summon two Major League yakuza deckers "
            "in samurai personas within ten turns of an External Alert."
        ),
    },
    "Toroshi": {
        "notes_append": "Etiquette (Street) TN 5 to know he is Shigeda. Told Foley 'the Shigeda have a deal to settle that little financial problem'.",
    },
    "Dr. Kenner": {
        "set": {"name": "Ms. Kenner", "title": "Maria Mercurial's therapist (dreamchip detox clinic)"},
        "notes_append": (
            "Reachable only through Hernandez vouching. Explains the limbic datajack (only scum-sucking drek "
            "would do that to someone; undoing it risks serious damage and Maria refuses anything that "
            "affects her performing), the custom-chip addiction no Barrens prostitute could afford, and "
            "Maria's use of 'average' street chips to blunt the withdrawal. Hopes to build an integrated "
            "personality on the Innocent."
        ),
    },
    "Reynaldo Texamachach": {
        "notes_append": (
            "Sent to Seattle in 2045 to fix the Perfekto plant; ordered the total cover-up (plant closed, "
            "manager to Mexico City, night-shift technicians dead in accidents, Greenwar cell wiped out, "
            "records purged) and stored his final report -- the only record of the tank's location -- in his "
            "secretary's sealed memory. She shot him that night."
        ),
    },
    "Margot Tipper": {
        "notes_append": "Quote for the BTL-scandal ending: 'Taking drugs, burning BTLs, living lascivious lifestyles while they preach the overthrow of our great culture in their nefarious music: what kind of decent woman does things like that?'",
    },
    "Andrew Masterson": {
        "notes_append": "Home on Queen Anne Hill. The 'heart attack' comes the day before the dumping investigation breaks.",
    },
    "Miguel Allende": {
        "notes_append": "The 'bright lad' plant manager of 2045 was sent to Mexico City for a 'special managerial briefing' and never heard from since; Allende's office uses the same phrase in the news handout.",
    },
}

TAG_EXISTING = {
    "orgs": [
        "Shigeda-gumi", "Perfekto Polymers", "New Horizons Development", "Federated Funds Net",
        "Dragon Knights", "Salish-Shidhe Council", "Citizens for a Decent Society Policlub",
    ],
    "locations": [
        "Federated Funds Net (Offices)", "Rent-a-Hideout Warehouse", "Star Gardens Endominium",
        "Hernandez's Brownstone & Studio", "Taetzel Building", "Old Perfekto Polymers Plant",
        "Sorayama's Clinic (Chiba)",
    ],
    "npcs": [
        "Maria Mercurial", "Armando Hernandez", "Max Foley", "Reynaldo Texamachach", "Sumiko Hotoda",
        "Kyle Morgan", "Perianwyr", "Jorge Mixacopotec", "Blackstone", "Lin Hwang", "Sidney Murdoch",
        "Newt", "Tellin", "Sorayama", "Ms. Kenner", "Toroshi", "Gum E. Bear", "Snout",
        "Andrew Masterson", "Miguel Allende", "Margot Tipper",
    ],
}

MATRIX_HOSTS = """
The earlier pass wrote a full VR2 conversion plan (recoverable with
`git show 16fd881:docs/mercurial_matrix_conversion.md`). Nothing has been built. Systems, with the
SR1 node data verified against the book on this pass:

**1. Federated Funds Net** (p.35, LTG #7206) -- Node 1 SAN Orange-3 Access 4; Node 2 Datastore Red-3
Trace and Dump 5 (each account file Scramble 3; failed unscramble dumps the account off-line);
Node 4 CPU Orange-4 Killer 4 (the transfer works here too). Hernandez's file 90 Mp / 180,000 nuyen;
transfer is a system operation, Computer TN 3, three successes (Red node). External Alert = 2D6-turn
shutdown, no defending decker. Earlier plan: Orange-4, ACIFS 4/3/4/5/3.

**2. Max Foley's system** (p.41, LTG #9206) -- Node 1 SAN Orange-4, Trapped Access 4 with Killer 5
gray IC; Node 2 SPU Green-5 Barrier 3; Node 3 Datastore Green-3 no IC (public correspondence, tax
figures, publicity -- nothing); Node 4 Blue-4 slave modules (recording gear, office machinery,
answering machine with Sumiko's 'keep the woman with you' vid message timestamped half an hour ago,
apartment gadgetry); Node 5 Datastore Orange-5 Trace and Dump 4 (80 Mp real-earnings file under
Scramble 4 = blackmail; coded bank interface under Scramble 4 with 300,000 nuyen, transferable to
Hernandez as a system op TN 5 two successes; 20 Mp unguarded diary); Node 6 SPU Green-5 Barrier 5;
Node 7 CPU Orange-3 no IC. Gum E. Bear defends on External Alert as an enemy decker. Earlier plan:
Orange-6, ACIFS 4/5/5/5/4.

**3. New Horizons Development** (p.51) -- wide-open Blue network, phone-accessible, legal filings and
PR only. Earlier plan: Blue-4 flat, unlisted LTG. A deliberate dead end.

**4. Sorayama's clinic, Chiba** (pp.54-55; Seattle RTG Green-4 -> Chiba RTG Orange-3, then directory
assistance) -- samurai-castle sculpting. Node 1 SAN Red-3 Trace and Dump 4 (gate house; bells and
gongs); Node 2 SPU Orange-5 Access 6 (eight-sided enclosure, samurai with conch trumpet); Node 3 SPU
Green-4 Barrier 3 (bonsai garden with a koi pool of data); Node 4 I/OP to bioscanners and imaging (a
gallery of windows); Node 5 slave modules for the surgical gear (courtyard of peasant craftsmen with
glittering tools and quivering body parts); Node 6 SPU Red-4 Killer 4 (armory with an armored
warrior); Node 7 Datastore Red-4 Access 5 Tar Pit (counting house with a nightingale floor that drops
into a bottomless pit; 5,000 Mp customer database, 1,000 Mp masterpiece database holding Maria's
20 Mp file); Node 8 Datastore Red-4 Black IC 5 (Buddhist temple courtyard, eight rocks = eight R&D
files: 50/80/120/50/40/60/90/40 Mp at 20,000 nuyen per 10 Mp); Node 9 CPU Red-5 Trace and Burn 6
(daimyo's great hall; the oni with the longbow is Black-4 guarding a 500,000-nuyen / 100 Mp credit
file; two Fu dogs are the Trace and Burn -- one fights, one runs howling to trace). External Alert:
two Major League yakuza deckers in samurai personas within ten turns. Earlier plan: Red-8.

**5. Taetzel Building, System A** (pp.58-59, the 'public' building mainframe) -- 1A SAN Green-4
Access 5 (supplies, deliveries, fire/police); 2A SPU Orange-3 Barrier 5; 3A slave modules Orange-7
(all building systems except the independently powered 28th floor; cameras, servoguns, anti-intruder
devices, the elevator drop trick; ops here may be seen from the Security Terminal -- roll 1D6 vs
successes); 4A CPU Orange-4 Trace and Report 6 (a trace sends two squads of six agents); 5A Datastore
Blue-4 (150 Mp building records: closed 2045, refit six weeks ago on the ground and 28th floors,
supplies for two to three dozen, hundreds of kilos of real beef and a lake of beer); 6A SAN Green-4
Killer 5 leading into System B. Earlier plan: build as its own host with a Trap Door into B.

**6. Dragon Knights' mainframe, System B** (pp.59-60, LTG #6206, fed by the roof satellite dish) --
1B SAN Red-4 Trace and Burn 3; 2B SPU Orange-4 Blaster 6; 3B Datastore Green-5 Access 6 (Morgan's
private area: mission summary incl. the whole Perfekto history; the Dragon Knights resources list
with holopix -- 'holy steaming drek, that's a picture of a DRAGON!'; the unlock code 'Silver Virgin';
the Blackstone liquidation order; the Orbital Credit Bearnaise cash box, Scramble 8, 750,000 nuyen);
4B Command Terminal (overrides the Security Terminal, orders shutdown of either system, any CPU op);
5B SPU Green-4 Barrier 5; 6B Datastore Green-6 no IC (personnel files on 15 agents, four flagged as
handlers; armory inventory; vehicle and fuel requisitions); 7B SPU Blue-4 (a system op here crashes
the special security interface between 8B and 3A -- obvious to the operator, cuts his building
controls until both mainframes restart); 8B Security Terminal Red-6 (any 3A operation, undetected by
the human operator); 9B CPU Red-7 Black IC 5. Lin Hwang defends. Earlier plan: two hosts, A's
trap_doors_json pointing at B, B flagged is_trap_door_dest.

**Not worth building:** Hernandez's office computer (no map; open access with his passcodes; clue
table p.37), Underworld 93's patch console, Maria's condo controls, Murdoch's camera wall, the
directory-assistance intercept.
"""

NOT_BUILT = """
- **Beauty Shannon** (simsense star in Morgan's photos), **Zango Wilkes** of Astral Lightning (suicided
  onstage), **ME-109 / Red Barron, Concrete Dreams** (rocker scene name-drops), **Low Earth Orbit** (the
  warm-up band), **Nicky Saitoh** -- name-drops only.
- **Johnson-san** (the 1944 Aztechnology rep who commissioned Maria's mods) and **Morgan's Mr. Johnson**
  (scrambled voice) -- unnamed handlers, kept in the org notes.
- **The three Pugnacine-Beta street samurai** (p.24: B4(5) Q4 S4 C2 I2 W1, Ess 3.3, Reaction 3(5);
  Firearms 6, Unarmed 6; dermal plating 1, retractable razors, Wired Reflexes 1; lined coats; Uzi III /
  Remington Roomsweeper flechette / AK-97 carbine + Super Shock taser; Predators with explosive ammo;
  concussion grenades; they die of systemic shock when the drug wears off), **yakuza soldiers and
  goons**, **Dragon Knights agents**, **street-gang bounty hunters** (p.33: stun rounds, stun batons,
  Streetline Specials, want a prisoner) -- stat blocks on the org rows.
- **Pugnacine-Beta** (Soviet-era combat drug: no pain, no fatigue, Willpower to 1, 95 percent fatal when
  it wears off) and the **Eyes of the Pack** spell -- on the Shigeda / Sumiko rows.
- **Franklin Co. firefighters, DocWagon, Orbital Credit Bearnaise, Rocker Stars newsnet, the
  Seattle Directory Assistance Database** -- services, noted where relevant.
- **The Barrens brothel** where Hernandez found Maria, the **local wino** who saw the dragon, the **dwarf
  doorman** backstage, the **sultry redheaded 'secretary'** on the intercept line -- one-scene color.
- **The hostage-holding / Greenwar strike** history and the **Perfekto plant manager** -- folded into
  Greenwar, Perfekto and Texamachach.
"""

PLAY_NOTES = """
- Optimum six players; the team needs a wizard, a decker and muscle. Read the prologue ('Out After
  Dark') and the 'Wings in the Morning' epilogue -- both are Kyle Morgan's voice.
- Foley's Negotiation is 7; roleplay it loud. Give the decker the Federated job so the 'same decker'
  fingerprint clue (Gum E. Bear) lands later.
- Everything Max learns reaches Sumiko within minutes. A team that follows him into the bathroom
  can turn him into a trap for the yakuza.
- The bounty (10,000, then 20,000 nuyen via 555-7395) makes hiring street muscle impossible; only
  buddies, gang/tribe members and followers can be trusted.
- Down to the Wire: Sumiko drops the dreamchip when attacked; Maria jacks it in five turns. If the
  runners are all captured, Maria grabs Sumiko's pistol and buys them a turn or two.
- Part Two legwork uses running success totals per section (New Horizons TN 4, Sorayama TN 8). If the
  players stall, Snout leads the Dragon Knights to their door (Knock, Knock: agents at 150 percent of
  the party, no missiles, a Patrol-1 for pursuit).
- The Taetzel: the decker can hold the elevator trick and the servoguns for the team -- or against
  the agents. Tell Blackstone about his family and the building's security is yours.
- Karma: 1 alive, 1 each for Maria alive / Hernandez alive / no dreamchip / sealed data revealed, 3
  for the threat; 8 possible.
- Loose ends worth keeping: Morgan and Perianwyr are alive and 'putting on a new face'; the Shigeda
  still own New Horizons and the poisoned land; whoever holds the tank data holds Aztechnology's
  Seattle license; Maria and Hernandez are married; the hearth spirit wants the shaman to visit.
"""
