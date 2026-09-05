# SRM 01-09 For Whom the Bell Tolls (FanPro/WizKids, 2005, SR3) -- campaign order #52. The Duwamish
# industrial area in south Seattle (the DocWagon warehouse), the base of the Space Needle, and
# Selenium, a high-class restaurant near the top of a Downtown skyscraper.
# SETTING NOTE: this is a SEATTLE adventure, not a Denver one, and it is Shadowrun Third Edition,
# not SR4. "For Whom the Bell Tolls is the final adventure in the Rose Croix story arc"; every scene
# is in the metroplex, the fight is over DocWagon's Seattle franchise, and the Space Needle is the
# rendezvous. Every location row is therefore city "Seattle".
# Dating: no in-world date is printed; the campaign year is 2064, matching the rest of Season 1. The
# adventure runs across roughly thirty-six hours -- a 04:00 conference call, the pre-dawn warehouse
# hit, a call two hours after the team gets home, 16:00 at the Space Needle, 17:30 at Selenium's
# address and the 18:00 meeting.
# Book editing inconsistencies, noted on the affected rows:
#   * the table of contents lists the third cast entry as "Shadowrunners"; the stat block itself is
#     headed "Broward's Mercenaries";
#   * the text says Broward "hired 3 mercenaries" while the stat block reads "2+TR at Selenium";
#   * the target is "located in the southern part of Downtown Seattle, in an old industrial district
#     called the Duwamish industrial area" in one paragraph and "located in the South Seattle, north
#     of the Sea-Tac area" in the next;
#   * "Micheal Davenport" is misspelled three times;
#   * the 01-09B warehouse maps are captioned "sRMO1-03" and "SRMO1-03" rather than SRM01-09, and the
#     Selenium map carries the credit "Bodenplan von: www.shadowrun.de";
#   * he is "Dr. Walter Broward" once in the Adventure Background and plain "Mr. Walter Broward"
#     everywhere else, including the press handout;
#   * no stat blocks exist for Saint James, Walter Broward, Garrett Walsh or Craig Gillespie;
#   * the full corporate name "Rose Croix Biomedical Solutions" appears only in the two press
#     handouts, never in the adventure text;
#   * the transformer sabotage disconnects "6 buildings ... 3 of them are unused, and the other 2 are
#     rarely accessed warehouses" -- three plus two plus the target makes six.
# Cross-spec note: Saint James is created by specs/srm_00_02_demolition_run.py; Michael Davenport
# (the man behind the Walter Broward identity), Garrett Walsh and Rose Croix by
# specs/srm_01_01_double_cross.py; Griffin Biotechnology by specs/srm_00_03_forced_recon.py. All are
# appended to here, never re-created. DocWagon, Knight Errant, Lone Star and Gaeatronics already
# exist and are likewise updated.
# Source text: docs/Adventures/text/SRM01-09A_For_Whom_the_Bell_Tolls.txt (16 pages) and
# docs/Adventures/text/SRM01-09B.txt (play aids, 10 pages).
# ASCII only (pre-commit hook).

ADVENTURE = "SRM 01-09 For Whom the Bell Tolls"
ORDER = 52
SOURCE = "SRM01-09A_For_Whom_the_Bell_Tolls.pdf, pp. 3-16; SRM01-09B.pdf (Play Aids), pp. 2-10"
YEAR = "2064"

SYNOPSIS = """
**Garrett Walsh** is preparing for a board meeting he dreads. In two weeks the third quarter plan
goes to DocWagon's executive branch, and Atlanta has been expressing serious concerns about the
Seattle franchise. This time the bad news has a name: **Rose Croix**. The competing corporation has
forced him to fight on ground he is not comfortable on -- the shadows -- and the last time he hired
runners he lost a trusted exec and ate a news story about organ harvesting. He walks into the
meeting room and finds a fifth man sitting with his four trusted directors. His CFO, **Craig
Gillespie**, takes the lead: "Mister Walsh, this gentleman goes by Saint James. He contacted us with
a possible solution for our problems."

**Saint James** worked out what the silence meant. Rose Croix's contracts through him had dried up;
he linked that to the announced IPO a month out and understood his client was lying low until then.
So he sold the knowledge: a few well-placed calls to DocWagon Seattle's top executives, a plan to
trap Rose Croix red-handed, carte blanche and the keys to an important but not crucial depot. Then a
call to **Walter Broward** offering him an elementary but lucrative run against DocWagon. Broward
took it, not realizing DocWagon meant to use it to engineer a hostile takeover.

At 04:00 the runners' comm rings on a conference call. Broward himself, excited and firm: a power
failure has hit a DocWagon supply depot in the **Duwamish industrial area**, security is minimal,
destroy everything stored there before reinforcements arrive or the power comes back, 20,000 nuyen
each, no witnesses, lethal force perfectly acceptable. The warehouse is pitch black, stocked to
twenty-five percent with about 100,000 nuyen of bandages and blankets in cardboard crates arranged
for easy filming, defended by SINless mercenaries in DocWagon uniforms who do not know they are
props and two HTR operators DocWagon has accepted it may lose. Eight battery cameras in the ceiling
railings, invisible at anything short of Perception (18), radio everything to a technician in a van.
It is a milk run. It is also evidence.

Two hours after the runners get home, a British voice: "Good morning lad. You dropped a tooth
yesterday and the fairy is ready to pay you back for it... Bring your little self to the base of the
**Space Needle** at 4 PM." A limousine and two black SUVs collect them for a conversation that is
half business and half blackmail. Their job is to bodyguard an 18:00 meeting at **Selenium** and make
sure Broward signs a low-balled buyout -- the death warrant of Rose Croix -- for 15,000 nuyen each
and a complete erasure of their DocWagon dossier. Accept or be eradicated.

Broward arrives alone, calls them sewer rats, then flashes a money hand-sign. He reads all twenty
pages, says "However, I have my counter-proposal... Now," and three mercenaries come out of an
out-of-service elevator over the host's body. When the shooting stops he sighs "Holy pig!", produces
a luxury blue pen, and Walsh -- who gave him that pen for his anniversary -- finally sees Michael
Davenport. Davenport offers the runners 100,000 nuyen each to let him walk. Walsh says they will
never see it. The whole two-year arc ends on the runners' choice.
"""

TIMELINE = """
- **Over the past year** -- Michael Davenport, blocked as DocWagon Seattle's Chief Operations
  Officer, hires two runner teams to stage his own assassination (SRM 01-01), takes cosmetic surgery
  in the Caribbean League and returns as Walter Broward of Rose Croix. Then a chess match: the vault
  job that empties DocWagon's tissue samples, cloned bodies and donor organs and shifts many Platinum
  contracts across; the shearing campaign that provokes DocWagon into hiring organ theft on a
  low-life community and wrecks its reputation (SRM 01-02); the Caring Gardens near-disaster from a
  skipped background check (SRM 01-07); and the hits on Griffin Biotechnology in Everett (SRM 00-03,
  SRM 01-04, SRM 01-08) that finally irritate DocWagon, one of Griffin's main investors.
- **A month out** -- Broward announces the Rose Croix Initial Public Offering. Investors are already
  drooling. He puts all shadowruns on hold and waits, patient, generating subtle but efficient
  marketing.
- **Shortly before the adventure** -- Saint James notices the stream of contracts from his regular Mr.
  Johnson has dried up, links it to the IPO, and calls DocWagon Seattle's top executives. Craig
  Gillespie brings him in front of Garrett Walsh and four other directors. DocWagon reluctantly
  accepts; Saint James is given carte blanche and the keys to an important but not crucial deposit.
- **Then** -- Saint James calls Broward to offer him an elementary but lucrative run against
  DocWagon. Broward agrees. A nearby electrical transformer is sabotaged, blacking out six buildings.
- **Day 1, 04:00** -- the conference call. Broward, other runners, 20,000 nuyen each, urgent
  sabotage, act now.
- **Day 1, pre-dawn** -- the warehouse hit. Eight hidden cameras record everything; two DocWagon HTR
  operators and two mercenaries per runner defend a building full of bandages.
- **Day 1, after** -- the runners call the number, Broward pays, the job is done. Do the usual
  debriefing; let the players think the session is over.
- **Day 1, two hours later** -- Saint James calls. The Space Needle at 16:00.
- **Day 1, 16:00** -- the limousine and two SUVs at the base of the Needle. Gillespie's ultimatum,
  Saint James's offer: 15,000 nuyen each and the erasure of their DocWagon dossier.
- **Day 1, 17:30** -- the runners return to Selenium's address; the same limo is waiting. Microphones
  are handed out; they follow Walsh in.
- **Day 1, 18:00** -- the meeting. Broward arrives alone, reads for about fifteen minutes, springs
  the mercenaries, is unmasked by the pen and the catchphrase, and offers 100,000 nuyen each.
- **After** -- Ending 1: the press conference, the buyout, DocWagon shares up 30 percent, all pending
  Corporate Court cases dropped. Ending 2: DocWagon releases the revelations, the UCAS Department of
  Justice warrants Michael Davenport for conspiracy, fraud and identity theft, and he disappears.
"""

ORGS = [
    {
        "name": "Corporate Court",
        "org_type": "government agency",
        "tier": 5,
        "headquarters": "Zurich-Orbital",
        "summary": "The arbiter both sides of the Rose Croix war are trying to avoid -- the low-balled buyout exists precisely so the fight never reaches it",
        "description": (
            "The extraterritorial judiciary of the megacorporate world, and the shadow hanging over the "
            "final act of the Rose Croix arc. DocWagon tried to stop Rose Croix through legal means and "
            "failed: Rose Croix acted too skilfully to be apprehended through legal action, and "
            "economically it deserves its reputation in its financial business. What Saint James offers "
            "instead is photographic evidence of Rose Croix's exploits -- proof that shadowrunners were "
            "hired to hit DocWagon -- which DocWagon can then use to leverage a contract buy out or a "
            "lawsuit in the Corporate Court. The contract Broward is made to sign is described in "
            "exactly those terms: a low-balled buyout agreement, signed to avoid a messy fight in the "
            "Corporate Court."
        ),
        "notes": (
            "Never appears on stage; it is the institutional pressure that makes the whole plot work. "
            "Both companies had filed grievances against each other for tortuous interference with "
            "business relations, and the press handout for Ending 1 notes that all pending Corporate "
            "Court cases were dropped as part of the acquisition. In Ending 2 the cases remain: Michael "
            "Davenport is 'suspected of implication in several cases filed at the Corporate Court by "
            "DocWagon Seattle' alongside the UCAS Department of Justice's own warrant for conspiracy, "
            "fraud and identity theft. Plot use: the reason a megacorporation prefers blackmail to "
            "litigation, and the reason the evidence has to be photographic rather than testimonial -- "
            "shareholders do not care too much how a company makes its money, at least as long as their "
            "reputations are not touched."
        ),
    },
]

LOCATIONS = [
    {
        "name": "DocWagon Duwamish Warehouse",
        "location_type": "corporate facility",
        "city": "Seattle",
        "district": "Duwamish industrial area (South Seattle)",
        "security_level": "Low Security",
        "controlling_org": "DocWagon",
        "summary": "An outgrown DocWagon ambulance-equipment store, blacked out, stripped of anything valuable, restocked with burnable props and rigged with eight hidden cameras",
        "description": (
            "The warehouse was used a lot during the DocWagon Seattle branch's inception, but with "
            "recent years and growth it became too small for the corporation's operations. For about "
            "eight years it has been used for stocking ambulance equipment -- one of DocWagon's main "
            "focuses, and therefore something Rose Croix would like to put a stick in the wheels of. "
            "The building is twenty feet high, its walls concrete with steel covering at Barrier rating "
            "10, with windows only at the office area. There are two entrances: the main door, used for "
            "normal employee and visitor entrance, which is closed but unlocked, and the cargo bay door "
            "for loading equipment and deliveries, which cannot be opened without electricity. Both are "
            "steel at Barrier rating 8. Two propane-powered forklifts sit on the floor. With the power "
            "out the place is pitch black."
        ),
        "notes": (
            "THE SET-UP: DocWagon has already removed its most valuable equipment, so the warehouse is "
            "stocked to only 25 percent capacity. To keep credibility there is still a lot of material, "
            "worth about 100,000 nuyen -- mostly bandages, syringes, disinfectant, blankets and "
            "clothing. Nothing is explosive, but everything will burn. The crates are cardboard and "
            "have been organized to allow for easy filming of the shadowrun; they are heavy, but a "
            "regular Strength (5) roll lifts one manually. OBSERVATION: eight cameras inside the "
            "building, each battery powered with enough charge to film all runner activity, installed "
            "in the steel railings used for ceiling support. They emit no light and no heat and are "
            "very small -- a Perception (18) roll by an actively searching character is required to "
            "notice one. They are remote controlled and each immediately transmits its images over "
            "radio waves to a technician in a nearby van, who records them and retransmits to Saint "
            "James and the DocWagon executives. They are positioned to catch all the action inside, and "
            "two more have been set up outside in case the runners try to demolish the building. "
            "ELECTRICITY: every electrical device in the warehouse is unusable -- the telecom, the two "
            "computers (whose memories have been completely wiped), the maglock on the front door, the "
            "lighting and the system that opens the loading bay. The place is totally isolated from the "
            "Matrix. SECURITY: two mercenaries per runner in DocWagon uniforms, plus two DocWagon HTR "
            "team members who parked their modified Ares Citymaster out front and stormed in, in "
            "commlink contact with a dispatch office that can also give orders based on the camera "
            "feeds. This scene is a milk run and should take roughly half the session; if the runners "
            "figure out that something is wrong, have the guards switch from defense to offense so "
            "DocWagon still films what it needs."
        ),
    },
    {
        "name": "Duwamish Industrial Area",
        "location_type": "commercial district",
        "city": "Seattle",
        "district": "South Seattle (north of Sea-Tac)",
        "security_level": "Low Security",
        "summary": "A much busier district last century, now low-cost warehousing with a D security rating and almost no Lone Star presence -- a perfectly isolated spot",
        "description": (
            "An old industrial district that was a much busier area in the previous century and these "
            "days is used mostly for low-cost warehousing. The various buildings in the immediate area "
            "of the target warehouse are all similar. It is considered low-class and carries a 'D' "
            "security rating, so Lone Star presence is very rare. This section is heavily industrial "
            "and busy during the day but a dead area at night, and with no nearby residential areas it "
            "is a perfectly isolated spot -- for the duration of the run there are no external "
            "witnesses at all, and the runners should meet nobody other than the token DocWagon "
            "security. The book places it both 'in the southern part of Downtown Seattle' and 'in the "
            "South Seattle, north of the Sea-Tac area' in consecutive paragraphs."
        ),
        "notes": (
            "The isolation is not an accident of geography so much as the reason Saint James chose this "
            "depot out of DocWagon's holdings: nobody will see the runners arrive, nobody will call the "
            "Star, and the only record of what happens will be the one DocWagon is making. It also sets "
            "up the contrast the final scene depends on -- from a D-rated dead industrial zone at "
            "four in the morning to an AAA Downtown restaurant at six in the evening, where Lone Star "
            "will be very prompt to answer and can shut the place down very quickly. The runners "
            "arriving for the hit spot each other in the dark and exchange a nod; the book gives the "
            "scene total freedom and tells the GM to adapt to the players' styles, stealth or carnage "
            "as they prefer, because this is the beer and pretzels part of the scenario."
        ),
    },
    {
        "name": "Duwamish Electrical Transformer (sabotaged)",
        "location_type": "power plant",
        "city": "Seattle",
        "district": "Duwamish industrial area (South Seattle)",
        "security_level": "Low Security",
        "controlling_org": "Gaeatronics",
        "summary": "The steel box at ground level that Saint James had opened and wrecked to black out six buildings and manufacture a window for a run",
        "description": (
            "Saint James's plan required a power shortage for the warehouse, so a nearby electrical "
            "transformer was sabotaged. It sits at ground level, encased in a steel box, entirely "
            "unremarkable in a district full of low-cost warehousing. The result is that six buildings "
            "are currently completely disconnected from the electrical network -- three of them unused "
            "and two of them rarely accessed warehouses, plus the target. It will take some time before "
            "the authorities are even aware of the situation, which is the whole point: the outage is "
            "not a lucky break for Rose Croix, it is the bait, and the clock Broward keeps pressing the "
            "runners about is a clock Saint James wound himself."
        ),
        "notes": (
            "Investigating it is the one chance the runners have to realize they are being played "
            "before the trap closes. A runner with electrical skills who searches the area to examine "
            "the electrical network finds the transformer on an appropriate skill roll at TN 5. A "
            "Perception (5) roll shows the box has been recently opened. A second electrical background "
            "(4) roll establishes that there has been a sabotage in the transformer, and that only a "
            "Gaeatronics technician has the necessary equipment to replace one. The book notes that "
            "there is a small but realistic possibility a player works out that things are not right -- "
            "in which case the guards switch from defense to offense so that DocWagon can still film "
            "the elements it needs for its proof."
        ),
    },
    {
        "name": "Selenium",
        "location_type": "restaurant",
        "city": "Seattle",
        "district": "Downtown",
        "security_level": "Corporate High Security",
        "summary": "A red-and-chrome high-class restaurant near the top of a Downtown skyscraper, closed for an hour so two CEOs can end a corporate war at a booth table",
        "description": (
            "A very chic restaurant with a red and chrome design, reached by elevator from the lobby of "
            "the skyscraper that hides it. DocWagon has managed to get it closed for an hour thanks to a "
            "connection and a pay-off; there will be no patrons at all. A host welcomes visitors and "
            "directs them into the main room. The meeting is held at a booth table on the side of the "
            "wall directly in front of the entrance doorway. Twelve employees -- three cooks, four "
            "waiters, two cook assistants, a barman, a host and a manager -- have been asked to stay in "
            "the surroundings since the restaurant will reopen afterwards; the host stays in the "
            "entrance lobby telling customers the restaurant will open later while the rest wait in a "
            "park nearby or clean the kitchen. They have been instructed absolutely not to intervene "
            "during the meeting. This is the runners' playground."
        ),
        "notes": (
            "SECURITY: the area is AAA, so Lone Star will be very prompt to answer any problem and can "
            "shut the place down very quickly if an alert is launched -- efficiency is necessary. A "
            "silent weapons detector at the entrance remains active and feeds an earbud in the host's "
            "ear, and the host carries a microphone matched to the runners' own, so he may warn them of "
            "an armed intrusion before it happens. Three security cameras cover the restaurant, their "
            "feed running to the central security office on the first floor; they have been cut down "
            "for the meeting. A PANICBUTTON terminal is available inside, and the personnel have been "
            "asked not to use it unless their lives are in danger. The employees will trigger an alarm "
            "only if they feel things are getting out of hand, in which case the building's security "
            "office -- held by Knight Errant -- will intervene and secure the place; they are aware an "
            "independent security force is in place and have been asked to contact the DocWagon "
            "executive supervising the meeting in the limousine before taking action. A team decker can "
            "be given a temporary password granting access privilege to the slave nodes related to the "
            "restaurant, with notice that every action will be logged and supervised; abuse it and "
            "security will cut his privileges and force him out of the Matrix. An out-of-service "
            "elevator on the restaurant level hides Broward's mercenaries, and there is underground "
            "parking in the building. The map in the play aids is credited 'Bodenplan von: "
            "www.shadowrun.de'."
        ),
    },
]

NPCS = [
    {
        "name": "Craig Gillespie",
        "role": "Chief Financial Officer of DocWagon Seattle -- brought Saint James in front of Walsh, and delivers the ultimatum in the limousine",
        "archetype": "Corporate Executive",
        "title": "Chief Financial Officer, DocWagon Seattle franchise",
        "race": "Human",
        "gender": "Male",
        "organization": "DocWagon",
        "connection": 4,
        "description": (
            "One of three men in the limousine dressed in tres chic clothing, the latest corporate "
            "fashion, and the one who speaks first, in a very crisp English accent: 'I'm Craig "
            "Gillespie, Chief Financial Officer at DocWagon Seattle. The winds have turned, and it's "
            "time to get things back on track. Your hands are stained in blood, but not ours. We offer "
            "you the chance to redeem yourselves. This will be our one and only offer. Accept or you'll "
            "be eradicated. Saint James, please continue.' The DocWagon executives are deadly serious; "
            "they want all the trouble to stop, they do not like working with runners, but they will be "
            "honest with them. Anxiety shows on their faces at the second meeting -- they have been "
            "waiting for this a long time."
        ),
        "background": (
            "It was Gillespie who took the lead in the meeting room when Garrett Walsh walked in and "
            "found an intruder sitting with his four trusted directors: 'Mister Walsh, this gentleman "
            "goes by Saint James. He contacted us with a possible solution for our problems. Please, "
            "have a seat.' Walsh never liked to use consultants to solve his problems, but he did not "
            "want to bring bad news to Atlanta either, so he sat down and reluctantly listened. Every "
            "part of the plan that follows -- the depot handed over, the transformer sabotaged, the "
            "cameras, the buyout contract -- goes forward because DocWagon's CFO brought a fixer in "
            "front of his CEO and made the case in financial terms."
        ),
        "notes": (
            "No stat block; he never fights and never leaves the limousine. His function is to be the "
            "hard edge behind Saint James's charm. If Saint James's diplomatic speech does not work and "
            "the runners want out, Gillespie stops him and lays it out clearly: the situation following "
            "the IPO of Rose Croix shares, the negative impact the recent shadowruns will have on Rose "
            "Croix, that Rose Croix fell into a trap and will not survive it, that DocWagon has "
            "evidence against the runners, and that cooperating is in their best interest. If they "
            "still walk, the scenario is over -- and DocWagon still succeeds in getting the contract "
            "signed. He is one of the DocWagon partners waiting in the limousine to receive the signed "
            "contract, and the executive whom Knight Errant building security has been told to contact "
            "before taking any action inside Selenium. In Ending 1 he takes the contract from Saint "
            "James's hand and gives him a very convincing handshake before the car leaves."
        ),
        "contact_skills": [
            "DocWagon Seattle corporate finance and board politics",
        ],
    },
    {
        "name": "Selenium's Host",
        "role": "The maitre d' with an earbud on the weapons detector and a microphone to the runners -- and the first person Broward's mercenaries kill",
        "archetype": "Service Worker",
        "title": "Host, Selenium (Downtown Seattle)",
        "gender": "Male",
        "connection": 1,
        "description": (
            "The man who welcomes the runners and Garrett Walsh at the top of the elevator and directs "
            "them into the main room, and who then goes back to the entrance lobby to tell arriving "
            "customers that the restaurant will be open later. He is wired into the operation more "
            "than he looks: an earbud tells him when the silent weapons detector at the entrance "
            "registers someone carrying a gun, and he has a microphone matched to the runners' own, so "
            "he can warn them of an intrusion before it happens. He is not security, he has not been "
            "told what this meeting is, and he has been instructed absolutely not to intervene."
        ),
        "background": (
            "One of twelve Selenium employees -- three cooks, four waiters, two cook assistants, a "
            "barman, the manager and the host -- kept on the premises because the restaurant reopens as "
            "soon as the meeting ends. DocWagon closed the place for an hour through a connection and a "
            "pay-off, cut the three security cameras, and left the weapons detector and the "
            "PANICBUTTON terminal live. The staff will only trigger an alarm if they feel things are "
            "getting out of hand."
        ),
        "notes": (
            "No stat block. His moment comes at Broward's code phrase: the mercenaries open the doors "
            "of the out-of-service elevator on the restaurant level, the host tries to warn them off, "
            "and a bullet in the head quickly silences him. Used well, he is a warning system the "
            "players can actually hear over the commlink a second before the shooting starts -- and "
            "then a body on the floor of a room the runners were paid to keep in good state. Note that "
            "the personnel have been asked not to use the PANICBUTTON terminal unless their lives are "
            "in danger; his are, and he does not get the chance."
        ),
    },
    {
        "name": "Selenium Staff",
        "role": "Twelve restaurant employees waiting out a closed hour in the kitchen and a nearby park, told absolutely not to intervene",
        "archetype": "Service Worker",
        "title": "Cooks, waiters, barman and manager, Selenium (Downtown Seattle)",
        "connection": 1,
        "description": (
            "Three cooks, four waiters, two cook assistants, a barman, a host and a manager, asked to "
            "stay in the surroundings because the restaurant will reopen as soon as the meeting ends. "
            "Some clean the kitchen; the rest wait in a park nearby. None of them knows who is sitting "
            "at the booth table by the wall or why an independent security team is standing around the "
            "room, and none of them has been told anything except to stay out of it. They are twelve "
            "civilians in a room where a corporate war is about to end in gunfire."
        ),
        "background": (
            "Selenium is a high-class restaurant in an AAA part of Downtown; DocWagon closed it for an "
            "hour thanks to a connection and a pay-off, and reduced the security in the process -- the "
            "three cameras covering the room were cut down, though the silent weapons detector at the "
            "entrance stayed live. The staff were instructed absolutely not to intervene during the "
            "meeting, and their employer expects the place back in working order afterwards."
        ),
        "notes": (
            "No stat blocks; treat them as ordinary civilians. They matter for three reasons. First, "
            "they are the alarm: the employees will trigger one only if they feel that things are "
            "getting out of hand, at which point the building security office -- held by Knight Errant "
            "-- intervenes and secures the place, having been asked first to contact the DocWagon "
            "executive supervising from the limousine. Second, they are the reason the runners' "
            "instructions include keeping the restaurant in good state: DocWagon would prefer no force "
            "or magic at all, will tolerate reasonable persuasion, and wants any of it discreet and "
            "efficient. Third, an AAA district means Lone Star answers fast and can shut the place down "
            "very quickly, and twelve witnesses in a kitchen is how that call gets made."
        ),
    },
    {
        "name": "DocWagon Security Mercenary (Duwamish Warehouse)",
        "role": "SINless hired muscle in a DocWagon uniform, three nights into a decent-paying job, with no idea it is a stage set",
        "archetype": "Mercenary",
        "title": "Contract security guard, DocWagon Duwamish warehouse",
        "organization": "DocWagon",
        "connection": 1,
        "description": (
            "Low-grade fighters dressed in DocWagon security guard uniforms and hired to act as "
            "security officers. They are from various backgrounds but all have one point in common: "
            "they desperately need cash and are ready to fight for it. They have been on the night "
            "shift for three days, they are SINless, and they are very happy to have a decent paying "
            "job. They did not know about the power outage and were initially trapped inside; they are "
            "currently scared, and were relieved when two real DocWagon security guards arrived to "
            "assist them. They will fight well enough to make sure they get paid, but will try to flee "
            "before they will put their lives on the line."
        ),
        "background": (
            "Saint James used a mix of mercenaries and DocWagon employees to staff the trap. These are "
            "the mercenaries: hired for a warehouse containing about 100,000 nuyen of bandages, "
            "syringes, disinfectant, blankets and clothing arranged in cardboard crates for the "
            "convenience of eight hidden cameras. They have no idea of Saint James's plan and no idea "
            "that the building they are defending was emptied of anything valuable before they started. "
            "Nobody has told them that the point of the exercise is to film somebody killing them."
        ),
        "notes": (
            "Stats: B5 Q4 S4 C2 I3 W3, Ess 6.0, Reaction 3, Init 3+1D6, Combat Pool 4, Karma 2, Pro 2. "
            "Athletics 3, Stealth 4, Clubs 2, Pistols 4, Unarmed Combat 3; Mercenary Background 3. No "
            "cyberware, no bioware, no armor (0/0). Weapons: Fichetti Security 500 pistol (SA, 6L) with "
            "two clips of regular ammo. Gear: small flashlight. Two mercenaries for each runner in the "
            "team. Debugging: if things stall, make them lose their nerve and try to escape, and use "
            "their professional rating at the right level -- except for the HTR team, the fight should "
            "be very simple. Note the encounter's design constraint: it is intended to be challenging "
            "but not deadly, because DocWagon wants the runners alive for the second part of its plans."
        ),
    },
    {
        "name": "DocWagon HTR Team Member",
        "role": "Two real High Threat Response operators sent to supervise a power outage, expendable and not told so",
        "archetype": "Corporate Security Specialist",
        "title": "High Threat Response operator, DocWagon Seattle",
        "organization": "DocWagon",
        "connection": 3,
        "description": (
            "Two genuine DocWagon operators who parked their van -- a modified Ares Citymaster -- in "
            "front of the building and stormed in. They are not used to working with in-house security "
            "agents and will not really care about the other guards, though they will give them orders "
            "if needed. They stay in contact with their dispatch office by commlink throughout, and "
            "that command center can give orders based not only on the guards' reports but also on the "
            "camera input from eight lenses the guards do not know exist. They are the only opposition "
            "in the warehouse worth taking seriously, and they will surrender if they feel overwhelmed."
        ),
        "background": (
            "DocWagon High Threat Response teams are very highly trained. Many of them come from "
            "military units or even occasionally from the shadows, and using standard military training "
            "methods and procedures they work together to escort medical technicians in the field and "
            "extract clients if necessary. They are highly loyal to their employer, are among the "
            "highest skilled agents in the DocWagon arsenal, and know it, having often to intervene in "
            "unusual occasions; their lower-level coworkers respect them highly. These two were "
            "assigned to supervise the power outage and were not told what the night was really for. "
            "DocWagon is well aware that the odds are good it might lose these employees, and has "
            "accepted the risk."
        ),
        "notes": (
            "Stats: B4(5) Q5(7) S5(7) C3 I5 W4, Ess 0.4, Reaction 6(8), Init 6+1D6 (8+2D6), Combat Pool "
            "8, Karma 3, Pro 3. Biotech 5, Negotiation 3, Pistols 4, Assault Rifle 6; Medicine 2, "
            "DocWagon Procedures 4. Cyber/bioware: datajack, bone lacing (plastic), cybereyes (thermo, "
            "flare compensation), Muscle Replacement 2, Smartlink 2, Wired Reflexes 1, enhanced "
            "articulation. Armor jacket 5/3 (150 nuyen). AK-98 assault rifle with gel rounds, 6M Stun "
            "(750 nuyen). Gear: Rating 2 commlink (200 nuyen), silver ID credstick with individual "
            "names and a balance of 1D6 x 1,000 nuyen. Two at the warehouse. If the challenge is way "
            "too easy for the table, feel free to add another HTR team or two -- but keep in mind the "
            "encounter is intended to be challenging and not deadly, because DocWagon wants the runners "
            "alive for the second half of the plan. Even the HTR team has its limits and will surrender "
            "if overwhelmed. Their gel loadout is the quiet tell that somebody upstairs wants live "
            "shadowrunners on film."
        ),
    },
    {
        "name": "Broward's Mercenary",
        "role": "Ex-military gun for hire waiting in an out-of-service elevator for the code phrase, ready to shoot a way out for the man who gave them their first big run",
        "archetype": "Mercenary",
        "title": "Contract muscle to Walter Broward; listed as \"Shadowrunners\" in the book's contents",
        "organization": "Rose Croix",
        "connection": 2,
        "description": (
            "Three ex-military professionals in armor jackets with Ares Predator IIs and combat knives, "
            "standing in an out-of-service elevator car on the restaurant level since shortly before "
            "Broward walked in. Their brief is simple: help him get out of the place if things go "
            "badly. At his code phrase they open the doors, shoot the host who tries to warn them off, "
            "and -- having come expecting opposition -- open up a can of firefight at the earliest "
            "opportunity, most likely spotting the runners before they spot Broward."
        ),
        "background": (
            "These shadowrunners are ex-military who quickly left the army and decided to use their "
            "skills for their own survival instead of protecting others. They worked with Walter "
            "Broward once, on their first big shadowrun, and they definitely want to keep this kind of "
            "contact alive -- which is exactly why he could call three of them to a Downtown skyscraper "
            "on the day he was summoned to sign away his company. He hired them from a previous run's "
            "contact and asked them to get him out if the meeting went badly."
        ),
        "notes": (
            "Stats: B6 Q4 S4 C3 I3 W5, Ess 6, Reaction 3, Init 3+1D6, Combat Pool 4, Karma 3, Pro 3. "
            "Athletics 4, Stealth 4, Pistols 6, Unarmed Combat 4, Edged Weapons 4, Etiquette 2; "
            "Security Systems 3, Military Procedures 4. Cyber: Smartlink 2. Armor jacket 5/3. Weapons: "
            "Ares Predator II (SA, 9M) with three clips of regular ammo, combat knife (Str L). Gear: "
            "Rating 2 commlink. NUMBERS: the text says Broward hired three; the stat block heading says "
            "2+TR at Selenium. The table of contents calls this entry 'Shadowrunners' while the block "
            "itself is headed 'Broward's Mercenaries'. TRIGGER: Broward finishes reading the contract, "
            "says 'I never thought that a weakling such as you would be able to do such a thing. "
            "Disgusting! However, I have my counter-proposal... Now.' If a PC decker identifies them and "
            "shuts down the elevator, Broward is warned and they attempt to over-ride the shutdown or "
            "get into the restaurant another way -- which can set up quite a game of cat and mouse "
            "through the building. If the confrontation becomes too dangerous, a team of Knight Errant "
            "security guards enters and puts down the opposition; they will give the runners no trouble "
            "but will ask that everyone leaves soon."
        ),
    },
    {
        "name": "Saint James's Camera Technician",
        "role": "The man in the van recording eight hidden feeds and retransmitting the evidence to Saint James and the DocWagon executives",
        "archetype": "Technician",
        "title": "Surveillance operator, Duwamish warehouse sting",
        "connection": 1,
        "description": (
            "A technician located in a nearby van, invisible to the runners for the entire adventure "
            "and more consequential than anyone they shoot. Eight battery-powered cameras in the "
            "warehouse ceiling railings and two more outside feed him over radio; he records the images "
            "and retransmits them to Saint James and the DocWagon executives in real time. Everything "
            "the runners do in that building -- every crate they burn, every mercenary they drop, every "
            "word they say on comms in the open -- goes through his hands and becomes the leverage that "
            "ends Rose Croix."
        ),
        "background": (
            "Saint James was given carte blanche by DocWagon Seattle to lay an intricate web and catch "
            "Rose Croix red-handed, and the whole plan reduces to one deliverable: photographic evidence "
            "of Rose Croix's exploits, which DocWagon can use to leverage a contract buy out or a "
            "lawsuit in the Corporate Court. The sabotaged transformer, the emptied warehouse, the "
            "restocked cardboard crates arranged for easy filming and the expendable guards all exist "
            "to give this technician something worth recording."
        ),
        "notes": (
            "No stat block, no name, no scene -- the book mentions him in a single sentence and never "
            "puts him on stage. He is included here because he is the adventure's actual antagonist in "
            "mechanical terms: everything the runners do to win the first half is being converted into "
            "the blackmail that traps them in the second. GM use: a team that sweeps the perimeter, "
            "notices a parked van in a dead industrial zone at four in the morning, or wins the "
            "Perception (18) against a camera can find him -- and finding him breaks the plot open "
            "early, which the book handles by having the guards switch from defense to offense so that "
            "DocWagon films what it needs anyway. Two of the cameras are outside specifically in case "
            "the runners try to demolish the building."
        ),
    },
]

ORG_UPDATES = {
    "DocWagon": {
        "notes_append": (
            "SRM 01-09 For Whom the Bell Tolls: the Seattle franchise ends its war with Rose Croix by "
            "hiring the enemy's own fixer. Rose Croix's aggressiveness and opportunism has struck a "
            "massive blow -- at that rate the company could easily disappear within months. DocWagon "
            "tried to stop it through legal means and failed, because Rose Croix acted too skilfully "
            "to be apprehended through legal action and economically deserves its financial reputation. "
            "STRUCTURE: CEO Garrett Walsh runs the Seattle franchise, with CFO Craig Gillespie and four "
            "other trusted directors; the Atlanta headquarters has been expressing serious concerns "
            "about Seattle and there is an investors meeting coming at which the franchise did not want "
            "to present catastrophic results. FINANCIALS from the press handout: DocWagon lost 60 "
            "percent of its value in the last year, the majority of the losses within the last three "
            "months, hurt by the announcement of the Rose Croix IPO and a rising necessity to upgrade "
            "all equipment; the buyout announcement causes shares to skyrocket 30 percent within "
            "minutes. Analysts agree DocWagon made a risky but appropriate move. THE STING: Saint James "
            "is given carte blanche and the keys to an important but not crucial deposit -- a Duwamish "
            "warehouse used for eight years to stock ambulance equipment, emptied of anything valuable, "
            "restocked to 25 percent with about 100,000 nuyen of burnable props in cardboard crates "
            "arranged for easy filming, blacked out by a sabotaged transformer, wired with eight hidden "
            "cameras, and defended by SINless mercenaries in DocWagon uniforms plus two real HTR "
            "operators the corporation has accepted it may lose. The runners' pay for the second half "
            "is 15,000 nuyen each plus a complete erasure of their DocWagon dossier -- everything they "
            "have done against the corporation wiped for a fresh start. The executives are deadly "
            "serious, want all the trouble to stop, do not like working with runners, and will be "
            "honest with them. In Ending 1 DocWagon buys Rose Croix Biomedical Solutions outright and "
            "all pending Corporate Court cases are dropped; in Ending 2 it releases the revelations "
            "instead, and the street notes that DocWagon has started investing in good connections in "
            "the business and that runners who worked with Rose Croix have been getting interesting "
            "calls."
        ),
        "leadership_add": [
            {"name": "Craig Gillespie", "title": "Chief Financial Officer, Seattle franchise", "notes": "Brought Saint James in front of Walsh; delivers the ultimatum to the runners in the limousine."},
        ],
    },
    "Rose Croix": {
        "notes_append": (
            "SRM 01-09 For Whom the Bell Tolls: the end of the arc. The full corporate name appears in "
            "the press handouts as Rose Croix Biomedical Solutions. Its CEO announced recently that the "
            "Initial Public Offering will be held within the month and investors are already drooling; "
            "if Rose Croix can maintain its recent growth there will be a substantial short to mid-term "
            "return. The latest runs against DocWagon have raised questions -- fortunately, shareholders "
            "do not care too much how a company makes its money, at least as long as their reputations "
            "are not touched. Broward knows he must be calm in the coming months: his shadowrunning "
            "teams and good investments have given him a comfortable position, and all he has to do is "
            "be patient, generate subtle but efficient marketing and wait for the flock of investors. "
            "Consequently, shadowruns have been on hold -- which is the tell that destroys him, because "
            "his favourite fixer noticed the silence, worked out the reason and sold it. Ending 1: "
            "DocWagon buys the company; Broward invokes familial reasons and Walsh does not deny that "
            "Broward might have had a word to say in the transaction; all pending Corporate Court "
            "grievances for tortuous interference are dropped. Ending 2: DocWagon releases the "
            "revelations, Michael Davenport is warranted and vanishes, no official word comes from the "
            "Rose Croix direction, and the street thinks that if what is left of the company can "
            "restructure and prove the wrongdoing was all Davenport's it might survive -- it had found "
            "a perfect niche, and with the bad publicity it will not require much money to buy in."
        ),
        "enemies_add": ["DocWagon"],
    },
    "Knight Errant Security Services": {
        "notes_append": (
            "SRM 01-09 For Whom the Bell Tolls: Knight Errant holds the security office of the Downtown "
            "skyscraper that houses the restaurant Selenium. They are aware that an independent security "
            "force -- the runners -- will be in place for the 18:00 meeting, and they have been asked to "
            "contact the DocWagon executive supervising from the limousine before taking any action. "
            "They intervene and secure the place only if the restaurant employees trigger an alarm "
            "because things are getting out of hand. If a team decker is granted the temporary "
            "restaurant password, Knight Errant logs and supervises every action he takes and will cut "
            "his privileges and force him out of the Matrix if it decides he is abusing them. "
            "Debugging: if the confrontation at the end becomes too dangerous, a team of Knight Errant "
            "security guards enters and puts down the opposition -- they give the runners no trouble, "
            "but will ask that everyone leaves soon."
        ),
    },
    "Lone Star Security": {
        "notes_append": (
            "SRM 01-09 For Whom the Bell Tolls: the adventure is built on the contrast between two "
            "security ratings. The Duwamish industrial area is low-class with a 'D' rating, so Lone "
            "Star presence is very rare, there are no external witnesses for the whole of the warehouse "
            "run, and the sabotage of a Gaeatronics transformer that blacked out six buildings will "
            "take some time before the authorities are even aware of the situation. Downtown, twelve "
            "hours later, is an AAA area: Lone Star will be very prompt to answer any problem at "
            "Selenium and can shut the place down very quickly if an alert is launched, so efficiency "
            "is necessary and the PANICBUTTON terminal inside is not to be used unless somebody's life "
            "is in danger. The runners also have to walk through corporate Seattle in full daylight, "
            "past frequent Lone Star patrols and throngs of sararimen leaving their jobs."
        ),
    },
    "Gaeatronics": {
        "notes_append": (
            "SRM 01-09 For Whom the Bell Tolls: a Gaeatronics distribution transformer in the Duwamish "
            "industrial area is deliberately sabotaged to manufacture the run. It sits at ground level "
            "encased in a steel box; wrecking it disconnected six buildings from the electrical network "
            "-- three unused, two rarely accessed warehouses and the DocWagon depot that is the target "
            "-- and it will take some time before the authorities are even aware of the situation. A "
            "runner with electrical skills who searches the area finds it at TN 5; Perception (5) shows "
            "the box was recently opened; an electrical background (4) test establishes the sabotage "
            "and the fact that only a Gaeatronics technician has the necessary equipment to replace "
            "one. That last detail is the runners' one chance to realize that the power failure they "
            "were told about at four in the morning was not an accident."
        ),
    },
    "Griffin Biotechnology": {
        "notes_append": (
            "SRM 01-09 For Whom the Bell Tolls: Griffin is named in the campaign background as the "
            "final straw. It is described as DocWagon Seattle's latest business venture, and 'a series "
            "of hits on the Griffin Biotechnologies complex in Everett have started to irritate "
            "DocWagon, one of its main investors. Rose Croix has been linked to these acts, and "
            "DocWagon is now ready to stop the war in the Seattle market once and for all.' Walsh's own "
            "assessment before the meeting that changes everything is that the Everett complex 'seemed "
            "to have gathered too much attention' and that he had begun to feel the price was too high "
            "to pay for the probable return. Everything the runners did to that facility in SRM 00-03, "
            "SRM 01-04 and SRM 01-08 is what puts a fixer in front of DocWagon's board with a plan."
        ),
    },
}

LOC_UPDATES = {
    "The Space Needle": {
        "notes_append": (
            "SRM 01-09 For Whom the Bell Tolls: the 16:00 rendezvous, chosen by a fixer who does not "
            "want too much implication in his own plot. 'Bring your little self to the base of the "
            "Space Needle at 4 PM. I don't think I need to give you instructions on how to find it.' "
            "The runners meet their partners from the previous night's run there, all of them tired and "
            "confused -- it is normally part of the landscape, but standing at its base you cannot "
            "ignore the beauty of the Space Needle, especially its dominating aspect. A black limousine "
            "accompanied by two black SUVs pulls up; Saint James steps out and invites them to enter "
            "the limo and meet their new business partners, then gets in last and closes the door. The "
            "conversation that follows -- half business, half blackmail -- happens with the car moving. "
            "Afterwards Saint James signals the driver and the runners are brought back here."
        ),
    },
}

NPC_UPDATES = {
    "Saint James": {
        "notes_append": (
            "SRM 01-09 For Whom the Bell Tolls: the fixer sells out his best client and runs the sting "
            "himself. He was one of Walter Broward's favourite allies, and he eventually realized that "
            "the stream of contracts from his regular Mr. Johnson had dried up. He made the link with "
            "the upcoming IPO, understood his client was laying low until then, and -- being a smart "
            "man -- decided to use the knowledge for himself: a few well-placed calls to DocWagon "
            "Seattle's top executives, a proposal to trap Rose Croix, and carte blanche plus the keys "
            "to an important but not crucial deposit. He knows this is a risky move, because "
            "shadowrunners are very unpredictable in nature, and he is ready to take the risk; neither "
            "he nor DocWagon took the time to plan for every possibility. VOICE: familiar, British, "
            "calling everyone lad and lads. 'Good morning lad. You dropped a tooth yesterday and the "
            "fairy is ready to pay you back for it. You lost something precious, but I can make you get "
            "something valuable in exchange. Bring your little self to the base of the Space Needle at "
            "4 PM. I don't think I need to give you instructions on how to find it. Cheers!' At the "
            "kerb he greets them martini in hand. 'Lads, as you may know I take care of my runners... "
            "You're my best prospects and I don't want to lose you. I've worked for Rose Croix before, "
            "but I believe that the winds are changing. I suggest you jump that ship before it sinks.' "
            "And, proudly: 'The run was a set-up, a trap, to which Rose Croix fell prey. This was my "
            "idea. Great isn't it?' His reputation toward the runners is stained and he knows it; he is "
            "arrogant but trying to be comforting. If they try to back out he turns very aggressive and "
            "will not hesitate to throw insults, but he will not prevent them from leaving. Terms: "
            "15,000 nuyen each, non-negotiable, plus a complete erasure of their DocWagon dossier, for "
            "supervising the meeting and making sure Broward signs; he stays on a radio commlink "
            "throughout and should not intervene, but will answer questions. Ending 1: 'Ahhh, I knew I "
            "could trust you! You know, the shadows have it's own justice and that idiot learned it the "
            "hard way' -- then he hands over the credsticks, the limousine drives off with the "
            "contract, and he shrugs: 'Ah rats, they could at least have give me a lift... Anyway, "
            "let's forget all that over a round of drinks. This one's on me!' If the runners have never "
            "met him, tell them they have heard the name -- a rising star in the shadows, the kind of "
            "fixer most runners are glad to work for."
        ),
        "contact_skills_add": [
            "DocWagon executive access at franchise-CEO level",
            "Corporate stings and evidence-gathering operations",
        ],
    },
    "Michael Davenport": {
        "notes_append": (
            "SRM 01-09 For Whom the Bell Tolls: the arc closes on him and the runners decide how. "
            "Background as the book states it: Walter Broward, formerly known as Michael Davenport, has "
            "been called the next Damien Knight; his meteoric rise in DocWagon Seattle hit a glass "
            "ceiling at Chief Operations Officer, where the shortsightedness of the CEO overruled "
            "whatever he proposed. He hired two teams of shadowrunners -- one to extract him, one as a "
            "diversion to make an assassination look believable -- returned from the Caribbean League "
            "with cosmetic surgery, and built Rose Croix to compete directly with DocWagon and bid on "
            "contracts DocWagon would never touch. THIS ADVENTURE: at 04:00 he opens a conference call "
            "himself. 'Good morning. This is Walter Broward, Rose Croix CEO. I'm sorry to wake you, but "
            "I need a quick response team. You surely know about my generosity to compensate for runs. "
            "Well, tonight is the night that I'm ready to open my purse wider since I require immediate "
            "action. Urgent sabotage. Who's in?' Terms: 20,000 nuyen each, non-negotiable, destroy "
            "everything stored in the depot at once, no equipment supplied, absolutely no witnesses or "
            "leads, lethal force perfectly acceptable, be quick before reinforcements arrive or the "
            "power comes back. He answers only three questions -- security guards very probable and the "
            "threat level hard to guess, magic possible but improbable, Matrix defense irrelevant "
            "because the grid is down; medical equipment is what is stored there; act as soon as "
            "possible -- because Saint James contacted him only a few minutes earlier. Afterwards he is "
            "warm: 'The job's done? Excellent... Thanks again, and I hope to have a chance to work with "
            "you again in the future, my friend.' AT SELENIUM he arrives alone and is surprised to see "
            "the runners and far more surprised to see Walsh (Perception (6) or a psychology skill "
            "spots it). He shows his disgust by calling them sewer rats, then subtly shakes his fingers "
            "in a money hand sign at one of them, hoping for help. He reads all twenty pages very "
            "cautiously for about fifteen minutes, throwing coughed-down insults Walsh does not react "
            "to, then closes it: 'I never thought that a weakling such as you would be able to do such "
            "a thing. Disgusting! However, I have my counter-proposal... Now.' -- the code phrase for "
            "three mercenaries in an out-of-service elevator. If the shooting starts he waits for his "
            "team to finish so he can be extracted unless there is an obvious opening; if he gets out "
            "he goes down to the underground parking and leaves when he feels safe. When the lead "
            "stops: an exasperated 'Holy pig!', then 'That's it. Rose Croix is yours. May you die "
            "young, fragger', and a luxury blue pen out of his coat -- the pen Walsh gave him for his "
            "anniversary, and the catchphrase only one man ever used. Unmasked, he bluntly offers the "
            "runners 100,000 nuyen each to let him get out of this. Ending 2: the UCAS Department of "
            "Justice warrants him for conspiracy, fraud and identity theft, he disappears from the "
            "surface, and the feds are not the only ones reading bounties in the shadows."
        ),
    },
    "Garrett Walsh": {
        "notes_append": (
            "SRM 01-09 For Whom the Bell Tolls: Walsh finally wins, and finds out what he actually "
            "won. He opens the adventure preparing for a board meeting -- in two weeks the third "
            "quarter plan goes to DocWagon's executive branch, Atlanta has been expressing serious "
            "concerns about the Seattle franchise, and this time the enemy has a name. Usually bad news "
            "comes paired with explanations about the economic situation, asset value fluctuation and "
            "legal battles; Rose Croix has forced him to fight in the shadows, where he is not "
            "comfortable. The last time he hired runners it went poorly: he lost a trusted exec and a "
            "news story broke that DocWagon was suspected of organ harvesting, and DocWagon Seattle's "
            "latest venture, the Griffin Biotech complex in Everett, has gathered too much attention "
            "for the probable return. His own line, before he walks into the meeting room and finds a "
            "stranger sitting with his four directors: 'If only Michael Davenport, their late COO was "
            "still around. For once, his style could have truly helped the corporation.' He never liked "
            "using consultants, but he did not want to bring bad news to Atlanta, so he sat down and "
            "listened. AT SELENIUM he gets out of the limousine, throws the runners a quick glance and "
            "walks in with his attention more on his briefcase; he takes his time setting the table "
            "right and will not even talk to them. When Broward calls them sewer rats, Walsh counters "
            "that the runners are professionals who take care of business just like everyone, and that "
            "he should not worry about that since it is not the worst thing that will happen to him "
            "today. He presents the twenty-page contract, ignores every coughed-down insult, and dives "
            "wisely for cover when the shooting starts. Then the pen and the catchphrase: 'Davenport?! "
            "That's the pen I gave you at your anniversary. And I know only one guy who would say that "
            "stupid holy pig line. So your assassination was all set up? You're the devil himself.' "
            "When Davenport offers the runners 100,000 nuyen each, Walsh counters that they should "
            "ignore him because his career is over anyway, and that they will never see the money. In "
            "Ending 1 he holds a joint press conference with Broward and does not deny that Broward "
            "might have had a word to say in the transaction."
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
There is deliberately nothing to deck in the first half of this adventure, and a tightly leashed
guest account in the second.

### The DocWagon Duwamish warehouse -- no host at all

Broward's briefing says it outright: Matrix defense is irrelevant because the entire power grid there
is down and there is no alternative power source. Every electrical device in the warehouse is
unusable -- the telecom, the two computers, the maglock on the front door, the lighting and the
system that opens the loading bay door. The place is totally isolated from the Matrix, and the two
computers have had their memory completely wiped, so there is no paydata and nothing to recover even
by hand. This is a deliberate design choice: the scene is a milk run with no decking, no rigging and
no legwork, and the only electronics in the building that still work belong to the people filming.

### The surveillance rig

Eight battery-powered cameras inside the building, installed in the steel railings used for ceiling
support, emitting no light and no heat and very small: Perception (18) by an actively searching
character to notice one. They are remote controlled and each immediately transmits its images over
radio waves -- not over the Matrix -- to a technician in a nearby van who records them and
retransmits to Saint James and the DocWagon executives. Two more cover the outside in case the
runners try to demolish the building. The DocWagon HTR pair are in commlink contact with a dispatch
office that can give orders based on the camera input as well as the guards' reports, which is the
one in-fiction clue that somebody outside is watching the inside.

### Selenium (building security network, held by Knight Errant)

No ratings, IC or trigger steps are printed. What the book specifies is access rather than
architecture: three security cameras cover the restaurant and their feed is sent to the central
security office on the first floor, and they have been cut down for the meeting. A silent weapons
detector at the entrance remains live and feeds an earbud in the host's ear. There is a PANICBUTTON
terminal inside the restaurant which the staff have been told not to use unless their lives are in
danger. If the team has a decker he can be granted a temporary password giving him access privilege
to the slave nodes related to the restaurant so he can supervise the meeting; he is explicitly
notified that every one of his actions will be logged and supervised, and if security thinks he is
abusing his privileges they will attempt to cut down his privileges and force him out of the Matrix.

The one offensive use the book anticipates: a decker who identifies Broward's mercenaries and shuts
down their elevator. Broward is warned when that happens, and the mercenaries attempt to over-ride
the shutdown or reach the restaurant another way -- setting up a cat-and-mouse chase through the
building while the meeting continues upstairs.
"""

NOT_BUILT = """
- **The Shadowland and matrix voices on the two press handouts.** Ending 1: **Metaman**, **Jane3**,
  **Kenny Gump**, **Blue Serge**, **The Chromed Accountant** and **Jazari**, arguing about whether
  Broward made the deal of the century, whether Rose Croix treated its people like cattle, and who
  cut down whose favourite breadmaker. Ending 2: **Vagrant Soul**, **Craesus**, **Soyuz**, **Bunker
  Dweller**, **Tin-Lin** and **Dee**, on the bounties out for Davenport, whether the remains of Rose
  Croix can restructure, whether DocWagon has learned to work the shadows, and Dee's hint that
  "someone else got their hand on a certain File H". Handles on a board, not characters.
- **The four other DocWagon directors** who sit with Gillespie when Saint James is introduced, and
  the three men in the limousine (Gillespie plus two) -- unnamed, undescribed beyond "tres chic
  clothing, the latest corporate fashion".
- **The limousine driver and the two black SUVs** that collect the runners at the Space Needle.
- **The DocWagon dispatch office** that the HTR team reports to and that relays orders based on the
  camera feeds -- an offstage command center, folded into the warehouse notes.
- **The connection at Selenium** who, with a pay-off, got the restaurant closed for an hour. Never
  named.
- **KSEA**, the news outlet carrying both endings; the **Federal Trade Commission**, which must
  approve the transaction in Ending 1 though neither party believes it will be a problem; and the
  **UCAS Department of Justice**, which issues the arrest warrant in Ending 2. Institutions
  name-dropped in the press handouts only.
- **DocWagon's Atlanta headquarters and the upcoming investors meeting** -- pressure applied from
  offstage; folded into the DocWagon update.
- **Ares, Fichetti, AK** -- manufacturer name-drops on gear and the modified Citymaster.
- **"File H"** -- an unexplained hook dropped by Dee in the Ending 2 gossip, deliberately left open.
"""

PLAY_NOTES = """
- The scenario's shape is a bait and switch, and the GM has to sell both halves. The first half is
  high-adrenaline and deliberately shallow: no time to think, Broward impatient with wishy-washy
  questions or delay, the pressure very high, an "act now" mission. The description of the warehouse
  fight is deliberately vague so you can adapt to the players' style -- stealth if they want stealth,
  total carnage if they want carnage. It is the beer and pretzels part and it should take no more
  than half your allotted time.
- Then comes the hardest bit of GMing in the adventure: making the players believe the session is
  over. Do the usual debriefing, congratulate them, announce that the 20,000 nuyen has arrived, act
  like you are looking for the Debriefing Logs and adding up karma -- and then read the wake-up call.
  The players should be looking at their watches thinking "what? That's all?" If they start packing
  up, accelerate the pace and get their attention back.
- The Space Needle scene is supposed to be uncomfortable. Runners do not like being forced into a
  situation and that is exactly what is happening. Be firm. The DocWagon executives are deadly
  serious and honest; Saint James is arrogant, proud of his own cleverness, and trying to be
  comforting about a betrayal.
- Questions the runners will ask, and the answers: force or magic on Broward is not preferred (no
  legal problems, but reasonable persuasion is tolerated if discreet and efficient, and keeping the
  restaurant in good state is essential); opposition unknown; Lone Star very prompt in an AAA area; a
  PANICBUTTON the staff have been told not to use; a weapons detector at the entrance; twelve staff
  in the kitchen and no patrons; Saint James on a radio commlink; and "Why not hire more neutral
  bodyguards?" -- this question will not be answered.
- The final scene is written as a scripted "normal" course of events and will not survive contact
  with the players. That is intended. As long as the main story elements are present you can add or
  remove freely; if the runners have already had their share of danger, skip the assault on the
  restaurant and cover the essentials. One thing must hold: there should be one winner, Rose Croix or
  DocWagon, and the goal of the scenario is to give the choice to the runners.
- Karma: destroying the items stored in the warehouse 1; getting the acquisition contract signed 2,
  OR deliberately preventing it from being signed 1. Maximum 3 team plus 3 individual. The book notes
  this mission has a great impact throughout corporate Seattle and that the runners' business ethics
  should be awarded in consequence.
- Debriefing Log boxes: the DocWagon Warehouse was destroyed / remained secure; Walter Broward signed
  the contract with DocWagon / did not sign / escaped.
- Two endings are written and both are worth reading aloud. Ending 1 has Saint James checking the
  signature, handing over the credsticks and losing his own lift home. Ending 2 has the runners going
  home thinking about how Micheal Davenport tricked everyone, waiting a few days for a call that
  never comes, and consoling themselves that at least their street rep is untouched -- DocWagon
  learned the hard way that you cannot control shadowrunners.
"""
