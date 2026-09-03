# Divided Assets (FASA 7318, 1994, Tom Dowd) -- campaign order #22. Denver / Front Range Free Zone (Sioux,
# Pueblo and UCAS Sectors), with a Chicago prologue and a Seattle-based rival corp. "The year is 2055" (p.4);
# no calendar dates or dated news handouts anywhere in the book. Shawn Gaffney's DOB is 17 June 2047 and he
# is "eight-year-old" throughout, so the run falls in the second half of 2055; the kidnap happens "at least
# two months" after the Chicago extraction. The hire is a "sunny, cool afternoon" followed by "chill rain".
# Source text: docs/Adventures/text/Shadowrun 2e - Adventure - Divided Assets {FASA7318}.txt (64 pages).
# Editing inconsistencies in the book (recorded on the affected rows):
#   - Shawn's therapist is "Dr. Martin Singtree" everywhere except the General Family Schedule (p.25), which
#     twice calls him "Marvin Singtree".
#   - The See It Now hook (p.8) has the boy "dangling dozens of stories above Seattle's streets"; the
#     extraction was in downtown Chicago.
#   - Jack Drew's sports car is a "Saab Dynamit 776M" (p.12) and a "Saab Dynamit 776TI" (p.55).
#   - "Dassurn Securities and Investments" (synopsis, Legwork) is "Dassurn Security and Investments" on p.10
#     and in the Player Handout.
#   - The Player Handout says Shawn must be held "two to four days"; the adventure runs six days (132 hours).
#   - The Chicago runner is arrested by "Eagle Security" (p.7); Denver's Sioux Sector police are "Eagle
#     Security Services Inc. (ESSI)". Treated here as the same Sioux-owned contractor, flagged on the row.
#   - Anna "put herself through Cambridge University and eventually the Milken Securities University"
#     (p.51); the handout gives only the Milken degree.
#   - The Decision Time option names "Marti, leader of the Shoalwater Elven Community" (Ivy and Chrome);
#     the Ivy and Chrome spec calls her Marti Vann and makes her the community's spokesperson, not leader.
# ASCII only (pre-commit hook).

ADVENTURE = "Divided Assets"
ORDER = 22
SOURCE = "Shadowrun 2e - Adventure - Divided Assets {FASA7318}.pdf, pp. 4-64"
YEAR = "2055 (second half; month not given)"

SYNOPSIS = """
Two months ago every trid in North America watched **Audrey W.** of **The All-Seeing Eye** run the
footage: a botched extraction from the **Fuchs-Auberlien Financial Services** tower in downtown
Chicago, a corporate economist named **Colin Gaffney** riding an emergency escape cable to the street
with one shadowrunner while a second runner and Gaffney's eight-year-old son **Shawn** hung tangled
thirty stories up for twenty-seven minutes until the fire department cut them down. **Dassurn
Securities and Investments** got its man; Shawn got a hospital bed, nightmares and a transfer with his
mother **Anna Coleridge-Gaffney** to FAFS's "more secure" Denver site.

Now an unnamed corporation -- **Corporation X**, and the runners never learn who -- wants Anna. It
assumes she will not jump for money, so it hires the team through two pale, sunglassed Johnsons on a
park bench (5-Mp datachip, 50,000 nuyen, Rating 9 forged IDs that rot a point every two days) to
"remove the SUBJECT from the control of FAFS" with as little trauma as possible and hold him for
"pre-arranged transfer to SEATTLE". Everything about the hire invites the runners to assume Dassurn is
reuniting a boy with his father. In Denver the fixer **Jack Drew** collects them in a Leyland-Rover van,
installs them in a dead print shop in the Sioux Sector, and hands over a 15,000-nuyen budget he is
quietly skimming. The runners case Shawn's world: the **Shining Bright School** in the Pueblo Sector
(a soulless expert-system academy behind a Barrier 24 wall, guarded by **Falconer Protective
Services** and a combat mage), the **Brandis Development** in the Sioux Sector (three white towers,
stables, a stocked lake and twelve guards loosely overseen by **Knight Errant**), the Tuesday and
Thursday drive to **Dr. Martin Singtree's** shabby therapy office in the UCAS Sector, and the family's
turbo Westwind driven by the beta-chromed bodyguard **Peter Tomita**, who will hand the boy over
rather than let him be hurt.

The grab is the easy part. Then the clock starts: Knight Errant has Anna under guard in half an hour
and its combat mages ritual-tracking Shawn by his blood inside two; **Pueblo Security Enterprises**,
**Eagle Security Services** or Lone Star chase whichever sector the team lit up; Audrey W. lands at
the **Hyatt-Star Regency** eight hours later and puts Shawn's face in every bar in Denver; the boy's
DocWagon bracelet and pocket phone are homing beacons; and FAFS posts a 50,000-nuyen reward. For six
days the runners baby-sit a quiet, sly, damaged child who slowly stops believing anyone is taking him
to his father, who freezes at real bloodshed and lights up at the first modern music he has ever
heard. On day six Anna, freshly promoted by FAFS, tells Corporation X "no deal", and Drew walks in:
"It's over. We're done. There are no instructions." Paid in full, the team has an eight-year-old and
no one to give him to -- mother, father, the reporter, a friend, an elven commune, themselves. The book
offers no right answer and asks the GM not to invent one.
"""

TIMELINE = """
- **Two months earlier** -- The All-Seeing Eye airs the Chicago extraction (show it during an unrelated
  run). FAFS complains about Audrey's harassment; on-air coverage stops, she keeps watching.
- **Hire, day 1** -- park bench, the first Johnson and the datachip (Player Handout). **Day 2** -- the
  second Johnson in the rain: 50,000 nuyen (opposed Negotiation, 2,500 a success), Jack Drew's picture
  and an FRFZ e-mail address. Biometrics within 48 hours; passes 48 hours later; travel 24 hours after.
- **Arrival** -- "Hey chummer, I'm finally here! Can you pick me up?" Drew in 3D6 x 5 minutes; the
  Sioux safe house. Surveillance of the school (7:30 AM / 3:30 PM run), Brandis, Singtree's (Tue/Thu
  5:00 PM), weekend day trips with Kellie Ross. IDs drop a rating point every two days -- plan the grab
  inside two weeks.
- **00:00 the grab** -- 00:15 Knight Errant opens its investigation; 00:30 Anna under KE guard at
  Brandis; 01:30 forensic magic team at the scene, ritual search begins; 04:00 Corp X delivers its
  demand to Anna (she tells no one); 05:30 material link complete, the Sending begins; 08:00 Audrey W.
  in Denver; 10:00 Shawn withdraws; 10:30 Audrey's first broadcast; 22:30 Sending complete -- a KE mage
  follows the astral trail.
- **Day 2** -- 34:00 the mage finds Shawn, KE ground forces deploy (30-45 minutes to muster); 38:00
  Audrey: the boy was in therapy; Dassurn denies everything.
- **Day 3** -- 49:00 Shawn believes no one is taking him to his father; 58:00 he fears his mother's
  anger and may trigger the DocWagon bracelet or phone home; Audrey: out-of-town runners, and how close
  KE came.
- **Day 4** -- 70:00 word reaches the team that Audrey wants to meet; 82:00 an anonymous runner from
  the Chicago job tells Audrey Shawn was never a target -- Colin becomes her focus; 92:00 Shawn refuses
  to eat, tries the bracelet or phone within 1D6 hours.
- **Day 5** -- 106:00 Audrey's Dassurn sources say the corp is clean; 117:00 Shawn decides he does not
  want to go home.
- **Day 6** -- 128:00 Audrey reports the kidnappers have contacted Anna; 130:00 Anna tells Corp X "no
  deal"; 132:00 Drew: the deal is off, turn the boy loose. Decision Time.
"""

ORGS = [
    {
        "name": "Fuchs-Auberlien Financial Services",
        "org_type": "financial consultancy corporation (FAFS)",
        "tier": 3,
        "headquarters": "Home office Cheyenne, Sioux Nation; Chicago tower (downtown core); Denver offices on three floors of the Yamatetsu building, UCAS Sector",
        "summary": "Cheyenne-based economic-strategy consultancy that treats employees' families as corporate assets; lost Colin Gaffney to Dassurn, keeps Anna, and pays Knight Errant to guard both her and Shawn",
        "description": (
            "Primarily a consultancy house advising wealthy private individuals and corporations on "
            "long-term, multi-track economic strategies in a variety of financial forums -- 'leading "
            "mid-sized corporations through the nasty shark tank of multinational, megacorporate status. "
            "For a cut, of course.' President/CEO Miriam Fox-Wallow. Its advancement and enrichment "
            "program pays, promotes and grants stock to employees who marry inside the company, weaving "
            "whole families so tightly into the corporate structure that leaving is disastrous; the "
            "Gaffneys signed a family-combined contract that covers their son. Colin Gaffney's extraction "
            "by Dassurn made the news across North America; FAFS refused to cooperate with The All-Seeing "
            "Eye, complained publicly about Audrey W.'s harassment, and moved Anna and Shawn to its "
            "'more secure' Denver site -- three floors of the Yamatetsu building in the non-contiguous "
            "UCAS Sector, with Knight Errant officers loitering as a supplemental force. Legwork (TN 6 in "
            "Denver, 8 elsewhere): 'They don't do anything except figure out what might happen if "
            "something else maybe happened. Lots of prognosticating, very little exposure or culpability.'"
        ),
        "leadership": [
            {"name": "Miriam Fox-Wallow", "title": "President/CEO (Cheyenne)", "notes": "Public record only; never appears."},
            {"name": "Anna Coleridge-Gaffney", "title": "Multi-market analyst/counselor, Denver office", "notes": "Fast-tracked for a management/analysis post; the target of Corporation X."},
            {"name": "Colin Gaffney", "title": "Former economic statistician (extracted to Dassurn)", "notes": "Ran a resource group rivalling his wife's until he skipped."},
        ],
        "notes": (
            "FAFS believes Shawn was a target of the Chicago extraction and acts solely through Knight "
            "Errant after the kidnapping, posting a 50,000-nuyen reward for leads to his safe return. "
            "When Corp X's demand reaches Anna, FAFS -- perhaps sensing the truth -- makes her an offer she "
            "cannot refuse, which is why she says no. The Denver computer system (three layers, a "
            "'white-hot kernel of nasty IC' at the core) holds nothing relevant; mapped in the prep doc. "
            "Shawn never visits his mother's office, so the grab cannot happen there; trying it in the "
            "UCAS non-contiguous sector brings Lone Star in moments. The Chicago tower's emergency escape "
            "cables can be frozen mid-descent from the security subprocessor -- the trick that stranded "
            "Shawn."
        ),
        "allies": ["Knight Errant Security Services", "Yamatetsu Corporation"],
        "enemies": ["Dassurn Securities and Investments", "Corporation X"],
    },
    {
        "name": "Dassurn Securities and Investments",
        "org_type": "international banking and investment corporation (DSI)",
        "tier": 3,
        "headquarters": "Seattle, UCAS (home office; street address not given)",
        "summary": "Seattle banking and market-analysis house that extracted Colin Gaffney from FAFS in Chicago -- the corp the runners are meant to assume hired them; it did not",
        "description": (
            "Specializes in multi-market investments and practices for a wide variety of private and "
            "corporate clients; an international banking concern as well as a financial-market investment "
            "and analysis firm. President/CEO Elliot Winright. DSI hired the shadowrun team that pulled "
            "Colin Gaffney out of the Fuchs-Auberlien tower in Chicago in broad daylight -- one person "
            "out, let alone two -- and now 'treats him like a god' as head of a focused-project group in "
            "multi-acquisition theory. Legwork (TN 8): 'I keep hearing they're on Saeder-Krupp's "
            "acquisition list, but there doesn't seem to be any activity.' Corporation X's Johnsons let "
            "the runners infer that Dassurn is behind the kidnapping; the book's p.10 and the Player "
            "Handout spell the name 'Dassurn Security and Investments'."
        ),
        "leadership": [
            {"name": "Elliot Winright", "title": "President/CEO", "notes": "Public record only."},
            {"name": "Colin Gaffney", "title": "Head of a focused-project group (multi-acquisition theory)", "notes": "Extracted from FAFS; refuses all comment on his son."},
        ],
        "notes": (
            "Executives are genuinely surprised by the kidnapping and say through a corporate mouthpiece "
            "that DSI had nothing to do with it; Audrey W.'s low-placed Dassurn sources confirm it on day "
            "five. Colin Gaffney refuses to answer any question from the runners or Audrey. Sending Shawn "
            "to his father is a long shot that needs GM improvisation: pressure (Audrey's broadcasts) "
            "might make Colin take the boy in, but nothing suggests Dassurn will be different from FAFS."
        ),
        "enemies": ["Fuchs-Auberlien Financial Services"],
    },
    {
        "name": "Corporation X",
        "org_type": "corporation (identity deliberately unknown)",
        "tier": 4,
        "headquarters": "Unknown -- 'the corp's real name doesn't matter; the runners can't find out who Corp X really is'",
        "summary": "The unnamed corporation that wants Anna Coleridge-Gaffney badly enough to kidnap her son as a bargaining chip; hires the runners through two pale Johnsons and the fixer Jack Drew",
        "description": (
            "Another corporation that badly wants Anna Coleridge-Gaffney's talents and believes she will "
            "not leave Fuchs-Auberlien for money, security or position -- so it tries extortion, a plan "
            "that 'has worked for many corps, many times in many other places'. Its two Johnsons meet in a "
            "park in the runners' home sprawl: a small, slight, thin-faced man in a cream suit with "
            "thinning blond-gray hair and terrifyingly expensive gold-and-black sunglasses, feeding "
            "pigeons ('Prompt. I like that.'), who does not know what is on the 5-Mp chip he hands over; "
            "and next day, in the rain, a tall woman in the same cream suit and sunglasses under a white "
            "umbrella, a gold datajack behind her ear, who knows the mission and negotiates the fee. Both "
            "are pale -- 'wherever they're from, they don't get out in the sun much'. They will not confirm "
            "or deny Dassurn. Once the boy is taken, Corp X waits a few hours, then quietly tells Anna her "
            "son has been spirited out of the city and she must come to work for them to see him again."
        ),
        "notes": (
            "Second Johnson: all Attributes 3 except Intelligence and Charisma 4, Willpower 5; Negotiation "
            "7; no weapons, armor or gear beyond a trimline pocket phone. Fee 50,000 nuyen (25,000 on "
            "acceptance, 25,000 on transfer per the handout), +/-2,500 per net success on an opposed "
            "Negotiation (Willpower) Test; +1 TN per two extra runners at the meet. Supplies Rating 9 fake "
            "IDs and UCAS/Pueblo/Sioux travel passes (passcode, fingerprint, voiceprint only; useless "
            "against Rating 6+ cellular cross-referencing; lose a point every two days after activation). "
            "Turning the chip over to FAFS would sink the team's reputation. When Anna refuses on day six "
            "Corp X pays the balance and issues no instructions for the boy. Leaving the chip's data "
            "with Drew's e-mail address is the only thread -- and it leads nowhere by design."
        ),
        "enemies": ["Fuchs-Auberlien Financial Services"],
    },
    {
        "name": "The All-Seeing Eye",
        "org_type": "syndicated trideo news-magazine (Audrey W.'s production)",
        "tier": 3,
        "headquarters": "Syndicated across North America via an international trideo-distribution syndicate; Denver base the Hyatt-Star Regency, Sioux Sector",
        "summary": "Audrey W.'s top-rated, on-demand crusading news-magazine; broke the Chicago extraction story and follows the runners to Denver, airing daily reports that put Shawn's face in every bar",
        "description": (
            "One of the hottest things on trid, pulling huge instant ratings all across North America; "
            "the program has an 'on-demand' broadcast slot, meaning Audrey gets airtime whenever she wants "
            "a show. Produced and hosted by Audrey W. from a custom virtual set in chic Abandallo business "
            "suits: penetrating questions, revealing footage, and a megacorporate fiend of the week. The "
            "Chicago segment ('the utter disdain felt by certain elements of society for the rest of us') "
            "called shadowrunners 'vicious, careless criminals' and promised that 'somebody, somewhere, "
            "pays'. Audrey flies to Denver with a few staff members within hours of the kidnapping."
        ),
        "leadership": [
            {"name": "Audrey W.", "title": "Producer, host and cybersnoop", "notes": None},
        ],
        "notes": (
            "Broadcast schedule after the grab (hours): 10:30 first report, blasting the runners, Knight "
            "Errant and the local law; 38:00 Shawn's therapy, Dassurn denies; 58:00 out-of-town runners and "
            "KE's near-miss; 82:00 an anonymous Chicago runner says Shawn was never a target; 106:00 "
            "Dassurn is clean; 128:00 the kidnappers have contacted Anna. Uses archival Chicago footage "
            "and covert surveillance of Shawn's day trips; may show the runners if a pedestrian with a "
            "mini-camera caught them. Use the reports to feed players who are failing legwork. Knight "
            "Errant files a complaint with her supervisors; it does no good. Audrey's word on the street "
            "(via the Nexus/Shadowland) that she wants to meet the kidnappers reaches the team at 70:00 -- "
            "her people suggest a time she is on the air."
        ),
        "enemies": ["Knight Errant Security Services"],
    },
    {
        "name": "Falconer Protective Services",
        "org_type": "private security corporation (site, personal, magical and Matrix security)",
        "tier": 2,
        "headquarters": "Denver, Front Range Free Zone (headquarters address not given; hardwired to the Shining Bright School)",
        "summary": "Security contractor for the Shining Bright School: two guards and a combat mage on site, samurai and an astral wage mage on call, a decker two turns away by hardwire",
        "description": (
            "Handles all aspects of the Shining Bright School's security in the Pueblo Corporate Council "
            "Sector, including magical and Matrix security. Supervises and maintains the security systems "
            "in the school's computers but keeps no decker on site; one is on call and reaches the "
            "school's Restricted layer through a hardwired SAN in 2D6 Combat Turns (on a 2D6 roll of 2-3 "
            "the decker is busy for 2D6 x 10 turns). Every guard wears an emergency bracelet wired to "
            "Falconer headquarters; every teacher wears one wired to the on-site guards."
        ),
        "notes": (
            "Day shift: two Corporate Security Guards (Ares Predator, 20 rounds, armored jacket 5/3, TR "
            "3/3) and a Combat Mage (archetype, TR 4/3) with two Force 4 elementals and a Force 2 watcher "
            "on call; two H&K 227 SMGs with laser sights and 60 rounds locked in the security office. "
            "Bracelet alarm brings two Street Samurai (TR 4/3) in a Ford Americar in 2D6 x 2 minutes and a "
            "Former Wage Mage (TR 4/3, two Force 5 elementals) astrally in D6 turns, her body riding with "
            "the samurai. Night: one guard, no mage; samurai 2D6 x 4 minutes, mage astral in 2D6 turns. "
            "Decker: Corporate/Security Decker profile with TR 4/3. On-grounds trouble: guards help Tomita "
            "and call Pueblo Security Enterprises; off-grounds escape: the mage follows astrally, two "
            "guards pursue in the Americar, everything goes to PSE and the boy's mother. No jurisdiction "
            "beyond the wall."
        ),
        "allies": ["Pueblo Security Enterprises"],
    },
    {
        "name": "Pueblo Security Enterprises",
        "org_type": "contracted law enforcement (Pueblo Corporate Council Sector, Denver)",
        "tier": 3,
        "headquarters": "Pueblo Corporate Council Sector, Front Range Free Zone (Denver pp.125-26)",
        "summary": "The Pueblo Sector's police: fast, scalable response to trouble at the Shining Bright School, then a low-priority investigation once Knight Errant claims the case",
        "description": (
            "Local law enforcement for the Pueblo Corporate Council Sector of the Front Range Free Zone "
            "(Denver: City of Shadows pp.125-26; response times Denver GM pp.53-54). Reacts only to events "
            "in and around the Shining Bright School. Once it abandons pursuit PSE becomes secondary to "
            "Knight Errant: Shawn is technically a megacorporate 'employee' under a licensed security "
            "provider's protection, and why should the Pueblo Sector spend public money finding a foreign "
            "national when a corporate force is on it?"
        ),
        "notes": (
            "Scale the response to the runners: magic brings a combat mage (second response roll at +3), "
            "drones or heavy weapons bring the big guns. Use Lone Star Sourcebook troopers, gear and "
            "vehicles with the logos changed. Runners' Rating 9 travel passes cover the Pueblo Sector. "
            "PSE forwards everything Falconer gives it and contacts Anna, who calls Knight Errant."
        ),
        "allies": ["Falconer Protective Services", "Pueblo Corporate Council"],
    },
    {
        "name": "Eagle Security Services Inc.",
        "org_type": "contracted law enforcement (Sioux Sector, Denver) -- ESSI",
        "tier": 3,
        "headquarters": "Sioux Sector, Front Range Free Zone (Denver p.135); the Chicago 'Eagle Security' that arrested the dangling runner is presumably the same company",
        "summary": "Sioux Sector police: answer any alarm at the Brandis Development, then run a full joint investigation with Knight Errant over jurisdictional squabbles the runners never see",
        "description": (
            "Law enforcement for Denver's Sioux Council Sector (Denver p.135). Brandis Development's guards "
            "call ESSI and Knight Errant the moment they see intruders. Because Anna and Shawn are resident "
            "aliens under corporate protection who hold UCAS passports, ESSI works with Knight Errant in a "
            "full investigation; the two fight over jurisdiction without it affecting the nuts and bolts. "
            "The Chicago prologue has the captured shadowrunner 'taken into custody by Eagle Security' -- "
            "the book never says whether that is the same Sioux-owned contractor; recorded here as one "
            "organization with two offices."
        ),
        "notes": (
            "Response per Denver GM pp.53-54, scaled to the runners; a combat mage arrives on a second "
            "roll at +4; heavy weapons or drones bring the big guns; Lone Star Sourcebook troopers with new "
            "patches. 'Smartgun-equipped ESSI or KE troopers' are the worst-case hostage standoff at "
            "Brandis. The bigger the splash, the harder ESSI comes after the team."
        ),
        "allies": ["Knight Errant Security Services", "Sioux Nation"],
    },
    {
        "name": "The Nexus",
        "org_type": "Denver data haven / illicit information exchange (Shadowland's heart)",
        "tier": 3,
        "headquarters": "Denver, Front Range Free Zone (Matrix presence; physical location per Denver: City of Shadows)",
        "summary": "Denver is home to the Nexus, 'the heart of illicit information in North America'; a decker with the right connections gets any information in 1D6 hours -- and hears Audrey W. is looking",
        "description": (
            "Because Denver is home to the Nexus, electronic information is easier to get there than "
            "anywhere -- for a decker with the right connections. Being at the heart of illicit "
            "information in North America means information flows better both ways: the team's decker "
            "most likely hears via the Nexus/Shadowland that Audrey W. wants to meet the kidnappers."
        ),
        "notes": (
            "Rules: base 18 hours and an Etiquette (Matrix) (10) Test (or Intelligence default) to make "
            "connections, modified for reputation and history with Matrix veterans. Every two successes "
            "lower all Shadowland target numbers by one; any success at all suspends the normal Shadowland "
            "one-request limit -- the decker finds anything, base time 1D6 hours. Standard Shadowland: "
            "Etiquette (Matrix) (4) to find a local echo station, one request per adventure, 8 dice, base "
            "36 hours split between speed and accuracy."
        ),
    },
]

LOCATIONS = [
    {
        "name": "Shining Bright School",
        "location_type": "private school",
        "district": "Near 10th Avenue and Depew Street, Pueblo Corporate Council Sector",
        "city": "Denver",
        "security_level": "Corporate High Security",
        "summary": "Exclusive single-story expert-system academy behind a sensor-topped Barrier 24 wall; 38 students, Falconer guards and a combat mage; Shawn's weekday cage 8:00-3:30",
        "description": (
            "A sedate southwestern-style single-story building that clashes with its two-and-a-half-meter "
            "ivy-covered wall (steel-reinforced brick, Barrier 24) and heavy wrought-iron gates (reinforced "
            "steel alloy, Barrier 20 against ramming). Terra-cotta lobby under a glass roof, southwestern "
            "art, a flower garden that blooms year-round. Thirty-eight students in classes of about seven, "
            "regrouped constantly by ability; the modern theory of 'continual challenge' means no fixed "
            "schedule and no fixed rooms. Structural and technological marvel, no soul: the teachers are "
            "administrators who point children at machines. Rooms: Aesthetic Studies (traditional media, "
            "classical instruments only), Dotti Findler's student-liaison office and nurse's station, "
            "faculty office and lounge, three tiers of administrators ending in Headmaster Walter "
            "Denhurst's office with every monitor feed, Security Control, the Central Computer room, "
            "Computer Sciences (student network deliberately isolated from the school system), Social, "
            "Bio and Physical Sciences rooms, kitchen (three staff), maintenance rooms that double as the "
            "two ork janitors' office, coat check, and the 'Big Room' that is lunch hall, study hall and "
            "festival room. Map pp.15-16."
        ),
        "notes": (
            "Shawn is dropped by Peter Tomita just before 8:00 AM and collected just before 3:30 PM (2D6 + "
            "20 minutes from Brandis; route: I-25 south, Route 6 west, Sheridan Boulevard, 10th Avenue). "
            "Only fixed point: a half-hour lunch between 12:15 and 1:15, half of it in the Big Room; the "
            "day's schedule sits in the Administration SPU. Round ornaments every ten feet along the wall "
            "are motion/thermographic sensors to five meters, always on; buried vibration sensors only at "
            "night; pressure pads and motion sensors in the gravel drive; gates run from Security Control, "
            "with a camouflaged emergency switch inside the left column (Perception (10)). Cameras "
            "everywhere except offices, lounges and bathrooms. Equivalent of a Platinum DocWagon contract. "
            "Security by Falconer Protective Services (see org). Staff are Average People (humans and "
            "elves). School records: promise in music and computers, will not apply himself. A grab on the "
            "grounds is the hardest option in the book -- make it fiercer, not easier."
        ),
    },
    {
        "name": "Brandis Development",
        "location_type": "residential community",
        "district": "Near East 71st Street and Lafayette Street, Sioux Council Sector",
        "city": "Denver",
        "security_level": "Corporate Standard",
        "summary": "Three 30-storey white towers on rolling green hills -- country club, stables, stocked lake, tennis domes, pool -- ringed by a Barrier 20 rail fence; twelve guards, Knight Errant on the alarm line",
        "description": (
            "Part apartment complex, part country club: three virtually identical 30-storey white towers "
            "visible for kilometers, on lush grass and thriving trees that could be Montana horse country, "
            "inside a double-rail wooden fence that is really four meters of steel-reinforced rail "
            "(Barrier 20) with motorized barricades (Barrier 18) at the unmanned, camera-monitored front "
            "and rear gates. A manmade lake dug thirteen years ago and stocked with inedible fish; "
            "year-round stables (six development horses, four residents', a winter sleigh); four lit "
            "tennis courts under winter domes; an oversized pool with seven lifeguards, hot tubs and a "
            "24-hour bathhouse; underground valet garage with a chauffeurs' lounge (1D6 + 1 minutes to "
            "fetch a car); a bare concrete helipad. Southwest tower: laundry, maintenance, central "
            "security; southeast tower: restaurant. Marble lobbies with a pool and miniature waterfall "
            "under six-meter ceilings; residences on Rating 6 maglocks (keycard or programmed voice), top "
            "five floors single-unit condos. Maps pp.20-23."
        ),
        "notes": (
            "Main (northernmost) tower: exterior Barrier 15, windows 5 below the sixth floor and 3 above, "
            "lobby doors 8 with Barrier 16 automated locks; four elevators (5 seconds per floor, any voice "
            "will do, stop dead if a hole over half a meter is punched in them). Lobby staffed 5 AM-9 PM "
            "(doors unlocked), one staffer overnight. Ground floor: exercise, weight and workout rooms, "
            "travel office, rec rooms, building security M1 (guard 24 hours, camera bank) and M2 (Knight "
            "Errant PR rep by day; lightly protected computers on the security grid behind a Rating 6 "
            "maglock). Security: twelve guards hired by the property-management corp (Corporate Security "
            "Guard, Ares Predator, Uzi III, armored jacket 5/3, TR 3/3) -- two per lobby, two in central "
            "security, four patrolling in pairs in two Ford Americars with spotlights, never more than a "
            "block away; alarms to central security and the local Knight Errant office. Central security "
            "office (southwest tower): Rating 8 maglocks, Barrier 10 walls, Barrier 8 doors, ballistic "
            "glass (+2 to shoot through), both layer CPUs and the security processor, alarms hardwired to "
            "KE outside the computer system. Color low-light cameras, 120-degree arcs. NO magical security. "
            "Guards repel intruders but will not endanger residents; they call KE and ESSI at once. Anna's "
            "Westwind lives in the garage; Tomita arrives 7:15 AM. System mapped in the prep doc."
        ),
    },
    {
        "name": "Coleridge-Gaffney Condo (Brandis Development)",
        "location_type": "apartment complex",
        "district": "21st floor, east condo, main (north) tower, Brandis Development, Sioux Sector",
        "city": "Denver",
        "security_level": "Corporate Standard",
        "summary": "Anna's tech-noir showpiece with a black-glass dining table and a study Shawn is forbidden to enter; the boy's own room, his war toys boxed under the bed and a secret toy base in his mother's closet",
        "description": (
            "Aggressive tech-noir decor. A sparse living room with hardly any comfortable furniture because "
            "Anna never entertains at home; a cluttered study/library where she works and Shawn pokes "
            "around when alone; a dining room dominated by a single-support black-glass table and this "
            "week's handmade 'Tibetan' stoneware, where mother and son eat every meal (dinner at 7:00 PM "
            "whether she is home or not); a bathroom with far too many mirrors; a master bedroom so pristine "
            "the maid knows another maid will replace her if it ever looks lived in; a guest bedroom; and "
            "Shawn's room -- scattered toys, half-working electronics on the dresser, mainstream trid "
            "posters, personal stuff under the mattress, and, packed in a box under the bed since his "
            "father's extraction, every realistic-looking war toy. In the far corner of his mother's "
            "impeccably coordinated walk-in closet he keeps a secret base for his Butt-Kicking Banzai "
            "Raiders, the evil overlord El Butcher in permanent residence. Post-modern kitchen ruled at "
            "mealtimes by the off-site cook Mario S., its locker grossly overstocked in case Anna asks for "
            "anything at all."
        ),
        "notes": (
            "Rating 6 maglock, interior walls Barrier 8, doors 6, windows Barrier 3 at this height. Anna "
            "is collected at 7:00 AM Monday-Saturday by a corporate Toyota Elite limousine (Bodyguard "
            "archetype chauffeur, TR 4/3), home after 6:00 PM (5:00 PM + 2D6 x 30 minutes). Shawn leaves "
            "at 7:30, returns 4:00-4:30 (6:15-6:30 on therapy days). Saturdays with Kellie Ross and Tomita; "
            "Sundays with Ross so Anna can rest. After the grab Anna is here under Knight Errant protection "
            "within half an hour and the whole development is under heavy guard -- returning Shawn means a "
            "cab or a drop-off nearby, not a visit."
        ),
    },
    {
        "name": "Sioux Sector Safe House (Drew's Print Shop)",
        "location_type": "safehouse",
        "district": "Commercial district of a less-than-stellar neighborhood, Sioux Sector",
        "city": "Denver",
        "security_level": "Low Security",
        "summary": "Long-closed printing company Jack Drew rented for the team: loading dock, basement, an illegal Matrix jack in office G, a poster of Euphoria in the kitchen, and a stoned local gang as lookouts",
        "description": (
            "Larger than the team needs because Drew did not know how big a team he was supporting: a "
            "small printing company that closed years ago. Foyer and lobby with sheet metal behind the "
            "street windows; an open room of odd furniture for gear, bedrolls and toys; an ad-hoc kitchen "
            "(microwave, grill, a fridge that grinds when it cycles, an aged poster of the simsense star "
            "Euphoria on the wall); two bathrooms with inside dead-bolts and a medkit's worth of cabinet; "
            "offices F and G, the latter with a Matrix-capable telecom jack and a roof conduit for "
            "satellite cable; storerooms; a loading dock with an exhaust fan; a bug-infested workroom with "
            "the fuse box; three empty rooms for sleeping, one with a wide stair to a basement the size of "
            "the whole building. Map p.12."
        ),
        "notes": (
            "Exterior wall Barrier 12; polyglass windows (3) backed with hardwood (4, together 7) that "
            "slides aside to shoot; doors Barrier 6 (loading-dock doors 8) on key-tumbler locks (Barrier "
            "14, effectively 4 for anyone with an archaic-locks skill); interior walls 6, doors 4. The "
            "office G telecom hookup is illegal and adds +2 to Trace IC against a decker using it. The "
            "local gang -- humans and metahumans of no particular ability, on Drew's payroll when not "
            "blasted on something -- gives 3D6 x 30 seconds' warning of visitors (3D6 vs TN 8: one "
            "success 'someone is coming', two or more a reasonable guess who). Drew's 15,000-nuyen budget "
            "buys the cheapest supplies he can find because he keeps half of what he does not spend. Six "
            "days here: salesmen at the door, wrong numbers, suspicious neighbors, paranoia; Knight "
            "Errant's ritual mages and a phone call home are what actually find it."
        ),
    },
    {
        "name": "Singtree Medical Building",
        "location_type": "medical office building",
        "district": "Near York Street and East 28th Avenue, UCAS Sector",
        "city": "Denver",
        "security_level": "Patrolled / Commercial",
        "summary": "Two-storey brick block of 36 identical 'soft science' offices where Dr. Martin Singtree sees Shawn Tuesdays and Thursdays at 5:00 PM; one rented cop at the door, no cameras",
        "description": (
            "An unassuming two-storey brick building housing 36 virtually identical offices leased mostly "
            "to therapists, psychologists and other 'soft' science professionals, parking directly in "
            "front just off the road. Dr. Singtree's office is decidedly tribal for UCAS territory; his "
            "Arapaho receptionist Nora shares a desktop computer with him and makes eyes at Peter Tomita, "
            "who ignores her from the waiting room. Runners may wonder why Anna sends her son to a "
            "lower-class practice: friends who wanted therapy their corporate masters would not hear about "
            "recommended him. Map p.27 ('Singtree Building', Denver area map site 3)."
        ),
        "notes": (
            "Exterior walls Barrier 12, windows 3, interior walls and every door 6; Rating 6 maglocks on "
            "the street doors, Rating 4 inside. No cameras, no sensors. One guard 9 AM-8 PM (Street Cop "
            "archetype, Colt American L36, armored vest 2/1, TR 2/2). No after-hours appointments though "
            "lessors have access any time. 4D6 offices busy in business hours with 1D6 + 2 people each "
            "(Average People). Route from the school: Route 6 east across I-25 becoming 6th Avenue, then "
            "north on York Street; sessions last an hour, home by 6:15-6:30. Office computer: shared "
            "desktop, Green-3 CPU and datastore, Access 2 on the SAN/CPU, only reachable when switched on "
            "in business hours; Shawn's file is psycho-jargon (Psychology (4), or Intelligence (12)). A "
            "grab here is UCAS territory -- Lone Star, not ESSI or PSE."
        ),
    },
    {
        "name": "Yamatetsu Building (Denver)",
        "location_type": "corporate facility",
        "district": "Non-contiguous UCAS Sector, downtown Denver (Location Q on the Denver downtown map)",
        "city": "Denver",
        "security_level": "Corporate Extraterritorial",
        "controlling_org": "Yamatetsu Corporation",
        "summary": "Yamatetsu's downtown tower where Fuchs-Auberlien rents three floors; passcard entry, a holding pen for unknown visitors, Yamatetsu guards and loitering Knight Errant officers",
        "description": (
            "Site security is pretty tight: Yamatetsu's own people handle the building while enough Knight "
            "Errant officers and officials loiter on the premises to suggest a tenant uses them as a "
            "supplemental force -- Fuchs-Auberlien Financial Services, on three floors. Passcards control "
            "entry; unknown or unexpected guests are shunted into a small holding area off the spacious "
            "lobby until someone from a tenant company comes down to vouch for them. Yamatetsu has become "
            "a stickler for security lately because of internal problems that have nothing to do with "
            "this adventure (Corporate Shadowfiles pp.150-52). No map or game statistics are given."
        ),
        "notes": (
            "Shawn never comes here, so the grab cannot happen here; the runners may still case it. Anna's "
            "Toyota Elite limo delivers her by 7:00 AM plus 1D6 x 5 minutes and returns her after six. "
            "Raiding the building or its systems means the GM designs it; the FAFS computer is separate "
            "from the building's and mapped in the prep doc (three layers, Probe-6 and Blaster-6 roaming "
            "the core). Trouble in the non-contiguous UCAS sector brings Lone Star 'in a matter of moments'."
        ),
    },
    {
        "name": "Hyatt-Star Regency",
        "location_type": "hotel",
        "district": "Sioux Sector (Denver map p.141)",
        "city": "Denver",
        "security_level": "Patrolled / Commercial",
        "summary": "The Sioux Sector hotel where Audrey W. and her All-Seeing Eye crew set up shop eight hours after the kidnapping",
        "description": (
            "Audrey W. and a few staff members fly into Denver within hours of Shawn's kidnapping and "
            "eight hours after the grab have set up shop in the Hyatt-Star Regency in the Sioux Sector, "
            "from which she fails to get a comment from Knight Errant and, two hours later, airs her first "
            "Denver story. The book gives no description of the hotel beyond the name and map reference."
        ),
        "notes": (
            "Base for daily reports, a network of low-placed sources, and Audrey's own street legwork -- she "
            "may cross the runners' path without recognizing them. A meet arranged from here is 'a dumb "
            "idea'; her people propose a time she is on the air. If the runners capture her and put her "
            "with Shawn (the book's suggestion for the 'Audrey takes him' ending), this is where they take "
            "her from."
        ),
    },
    {
        "name": "Fuchs-Auberlien Financial Services Tower (Chicago)",
        "location_type": "corporate facility",
        "district": "Downtown core, Chicago",
        "city": "Chicago",
        "security_level": "Corporate High Security",
        "controlling_org": "Fuchs-Auberlien Financial Services",
        "summary": "The gleaming Chicago spire from The All-Seeing Eye's footage: a blown-out window thirty stories up, an emergency escape cable jammed with a runner and an eight-year-old on it",
        "description": (
            "A gleaming corporate spire in Chicago's downtown core, recognizable by the buildings around "
            "it. Like many corporate skyscrapers it mounts emergency escape systems behind protected wall "
            "sections on key floors: high-speed descending cables triggered manually or by building "
            "security, controlled from slave nodes reachable only through the security subprocessor, "
            "which is usually kept off the Matrix -- and which can stop a cable mid-descent to leave "
            "intruders dangling. Dassurn's team blew a window here after Shawn Gaffney tripped the internal "
            "alarms; the first runner and Colin Gaffney rode one cable down, the second runner and the boy "
            "tangled on the other for twenty-seven minutes with security guns on them until the fire "
            "department cut them loose. The captured runner went to Eagle Security."
        ),
        "notes": (
            "Prologue only; no map. Legwork after the kidnapping (TN 6): the second runner had no extra "
            "harness and 'looks fraggin' surprised to have that kid hanging off him' -- they never planned "
            "to take Shawn. Two months after the extraction FAFS security here has probably relaxed. "
            "Corporate Shadowfiles and Denver are the reference books; Chicago itself is outside the "
            "adventure."
        ),
    },
    {
        "name": "Knight Errant Denver Headquarters",
        "location_type": "corporate facility",
        "district": "Non-contiguous region of the UCAS Sector",
        "city": "Denver",
        "security_level": "Corporate High Security",
        "controlling_org": "Knight Errant Security Services",
        "summary": "Where the KE tracking mage reports Shawn's location before returning to astral surveillance; troops muster here in 30-45 minutes",
        "description": (
            "Knight Errant's Denver headquarters, in the UCAS Sector's non-contiguous downtown region. "
            "Once the ritual Sending finds Shawn, the fourth mage tracks the path of power to the boy, "
            "notes the real-world location, zips back here to report, and returns to keep the place under "
            "astral surveillance while the ground forces muster. Not described or mapped."
        ),
        "notes": (
            "Also the destination of Anna's phone alert, Falconer's and PSE's forwarded surveillance, "
            "DocWagon's notification, and FAFS's 50,000-nuyen reward hotline. Knight Errant takes half an "
            "hour to forty-five minutes to muster and deploy; 'then the fun begins'."
        ),
    },
]

NPCS = [
    {
        "name": "Shawn Gaffney",
        "role": "The eight-year-old 'SUBJECT': quiet, sly, bright and emotionally abandoned; the kidnap victim whose fate the runners must decide",
        "archetype": "Child (corporate dependent)",
        "title": "Son of Colin Gaffney and Anna Coleridge-Gaffney; Shining Bright School pupil; FAFS corporate dependent",
        "race": "Human",
        "gender": "Male",
        "nationality": "UCAS (born Chicago, Illinois)",
        "organization": "Fuchs-Auberlien Financial Services",
        "connection": 1,
        "description": (
            "Shawn Bryan Gaffney, born 17 June 2047: 121 cm, 21 kg, light brown/sandy hair, hazel eyes, a "
            "bright-purple SynthaCanvas backpack that never leaves him. Quiet by nature, he says little "
            "and nothing to strangers, stares at nowhere or at the computer he keeps playing with, and "
            "tenses when he knows you are watching. Get him to relax and there is a sly, understated "
            "sense of humor and a talent for the dry put-down; he puts two and two together fast, seems "
            "older than eight, and still has every fear, hope and misconception of a boy that age raised "
            "inside a corporate bubble only one event ever pierced. Freezes at real bloodshed; enjoys "
            "loud, cinematic bravado as long as nobody bleeds. Lights up at the first modern music he "
            "hears."
        ),
        "background": (
            "Conceived by artificial insemination to exploit FAFS's incentives for corporate families and "
            "considered a corporate asset by both parents, raised by a succession of guardians and "
            "companions, no real friends in his isolated corporate world. NIEE score 221 (47 above "
            "average) sixteen months ago; grades 'average'; 'learning-directed attention-focus "
            "deficiency'; inquisitive but introverted, bursts of undirected anger. When Dassurn's team "
            "came for his father he tried to go too, tripped the alarms just as the drills taught him, and "
            "ended up hanging from an escape cable in a stranger's arms while his father dropped to the "
            "street without a backward glance. Two months of nightmares and Tuesday-Thursday therapy with "
            "Dr. Singtree later, he half-expects a shadowrunner to come and take him away; he blames his "
            "mother for driving his father off, craves her approval, and is not sure he misses his Dad at "
            "all. Unrecognized talent for computer-generated music: the only electronic music he has ever "
            "heard is the tones of the math program on his portable computer, which he drills for hours."
        ),
        "notes": (
            "Stats: B2 Q3 S2 C4 I5 W4, Ess 5.7, R4, Init 4 + 1D6; TR 1/1; Armed 1, Athletics 3, Biology 1, "
            "Computer* 2, Etiquette (Corporate) 2, Physical Sciences 1, Unarmed 1; Bicycle 4, Music "
            "(General)* 2 (* = untapped potential when used together). Datajack, datasoft link. Gear: "
            "purple backpack, credstick with 12 nuyen, a container of Smelly Glop (Do Not Eat!), DocWagon "
            "Gold contract with emergency-trigger sealed-band wrist phone, portable computer (50 Mp, the "
            "musical math program), music chip player with three classical chips, a portable phone, "
            "school chips plus two slightly adult comic chips, one NERP, a rubber lizard named Sam. Fear of "
            "heights: Willpower (2) at a window, (4) in the open, +1 above ten stories, +2 per repeat every "
            "30 seconds or he freezes. Violence: Willpower (3/6/10) when someone nearby takes a "
            "Moderate/Serious/Deadly wound (+1 to +4 for brutality) or he goes catatonic 2D6 minutes (+1D6 "
            "each time) and then acts as if Serious Stun. Talking: Charisma (8) once per six hours "
            "(1 success monosyllables, 2-3 words, 4+ a conversation); cumulative successes 10/15/20 to "
            "make him responsive / broach his parents / get him to open up; +1 TN per extra runner per "
            "six hours. Calming an outburst: Charisma (12), 1 success = 2D6 minutes, 3 = the whole "
            "episode; -1/-2/-4 at 10/15/20 cumulative. Timeline of his collapse: 8 hours confusion, 50 "
            "hours fear of his mother (bracelet or phone), 90 hours refusing to eat, ~117 hours 'I don't "
            "want to go home' behind a fragile mask, dawn of day six falling apart. Play modern music and "
            "he talks without a test. Removing him from his parents does him no more long-term damage than "
            "has been done. Karma: 2 team points for grabbing him with minimum fuss and violence."
        ),
    },
    {
        "name": "Anna Coleridge-Gaffney",
        "role": "Shawn's mother -- driven, caustic FAFS market analyst who sees the corporation as a machine and her son as an asset; refuses Corporation X's blackmail",
        "archetype": "Corporate Executive",
        "title": "Multi-market analyst/counselor, Fuchs-Auberlien Financial Services (Denver); fast-tracked for management",
        "race": "Human",
        "gender": "Female",
        "nationality": "UCAS (Boston)",
        "organization": "Fuchs-Auberlien Financial Services",
        "connection": 3,
        "description": (
            "Thirty-eight, tall, average-to-medium build, shoulder-length dark red hair and dark green eyes, "
            "neo-conservative business suits; hobbies adaptive market strategies and fine-art criticism. "
            "Coworkers call her intimidating, obsessive, demanding, bossy, humorless and caustic -- 'a real "
            "cold fish'. Difficult and demanding to work for, unforgiving and brutally honest, with no room "
            "for luxuries or anything else that does not advance her career, and that includes her son. "
            "Gives virtual lectures on pan-corporate investment theory."
        ),
        "background": (
            "Born to working-class parents just outside Boston, she put herself through Cambridge "
            "University and then the Milken Securities University in Manhattan by sheer willpower and as "
            "many jobs as she could juggle, and has spent her life distancing herself from her upbringing "
            "-- in her own telling the family home is on Beacon Hill and her parents are much more than "
            "they were. Met Colin Gaffney nine years ago at a mandatory corporate function, a kindred "
            "ambition; both used FAFS's marriage-and-family incentive program, and Shawn was conceived by "
            "artificial insemination as, on many levels, a corporate asset. She and Colin ran rival "
            "resource groups until he skipped. Still legally married, she has begun reverting to her "
            "maiden name. In Denver she replaced a less-than-well-liked researcher and has been "
            "fast-tracked because 'she's got more to prove' with her husband gone."
        ),
        "notes": (
            "Stats: B3 Q2 S2 C4 I5 W4, Ess 2.6, R3, Init 3 + 1D6; TR 1/1; Car 3, Computer 5, Etiquette "
            "(Corporate) 6, Firearms 1, Interrogation (Verbal) 3, Negotiation 4, Sailboat 3; Economics 6, "
            "Finance 7. Datajack, datasoft link, display link, 300 Mp headware memory. Fichetti Security "
            "500, pocket secretary, pocket telecom. Schedule: Toyota Elite limo at 7:00 AM Monday-Saturday, "
            "home after 6:00 PM, never entertains. Infuriated by the kidnapping and first blames her "
            "husband; when Corp X's message arrives she is oddly flattered, does not fear for Shawn (too "
            "valuable a chip), is tempted, and turns it down at 130:00 because FAFS makes her an offer she "
            "cannot refuse -- with no more than a twinge that Corp X might not release him. Then she waits. "
            "If Shawn goes home she pays attention for a while, then old habits; Singtree's reports have "
            "only widened the gap and may make her pull the boy out of therapy."
        ),
    },
    {
        "name": "Colin Gaffney",
        "role": "Shawn's father -- brilliant economic theoretician and 'questionable human being' who left his son hanging in Chicago and now heads a project group at Dassurn in Seattle",
        "archetype": "Corporate Executive",
        "title": "Head of a focused-project group (multi-acquisition theory), Dassurn Securities and Investments, Seattle",
        "race": "Human",
        "gender": "Male",
        "nationality": "UCAS",
        "organization": "Dassurn Securities and Investments",
        "connection": 3,
        "description": (
            "Thirty-five, tall and lightly built, short dark hair flecked with gray, conservative business "
            "suits; anxious but not particularly alarmed on the news footage as he steps out of a blown "
            "window in a security guard's arms. Coworkers: 'intense', 'brooding', 'self-absorbed', "
            "'domineering', 'hostile', 'a cold fish'. Legwork: 'Brilliant economic theoretician. "
            "Questionable human being.'"
        ),
        "background": (
            "Economic statistician known for demand-event curve theorems and multi-yield acquisition "
            "practices, a 'Distinguished' graduate of the Roos Institute for Pan-Economic Studies in "
            "London and a frequent contributor to the online source Adaptive Economic Theory; hobbies "
            "statistical population evaluation and currency-market appreciation. Married Anna under "
            "FAFS's family-incentive program and ran a resource group rivalling hers. Wanting out of both "
            "the marriage and FAFS, he accepted Dassurn's offer and a daylight extraction from the Chicago "
            "tower; when Shawn blundered in and wanted to come, Colin and the team tried to leave him "
            "behind. Contacts say the real reason he left was to get away from Anna. Dassurn treats him "
            "like a god."
        ),
        "notes": (
            "Never appears on stage; no stats given (use Anna's as a guide). Refuses every question from "
            "the runners or Audrey W., and his silence about his own son is meant to make the players "
            "doubt him. Tells himself he loves the boy but does not know what to do with him; sufficient "
            "pressure (Audrey's broadcasts after the 82:00 revelation that Shawn was never a target) might, "
            "at GM discretion, make him agree to take Shawn in -- with no reason to think Dassurn will be "
            "better than FAFS. The team's 'transfer to SEATTLE' was always a fiction."
        ),
    },
    {
        "name": "Peter Tomita",
        "role": "The Gaffneys' freelance bodyguard and combat driver -- beta-chromed, immaculate, and ready to surrender the boy rather than see him hurt",
        "archetype": "Bodyguard",
        "title": "Freelance personal bodyguard to Anna Coleridge-Gaffney and Shawn Gaffney",
        "race": "Human",
        "gender": "Male",
        "nationality": "UCAS (San Francisco; Japanese-American)",
        "connection": 3,
        "description": (
            "A San Francisco native of Japanese-American descent, below-average height, medium build, short "
            "dark hair and green eyes, fond of fine arts and dressed in expensive European -- mostly Spanish "
            "-- suits tailored for him. A true professional who resorts to violence only when necessary; "
            "'hard hitter but very professional, not the type who blindly sprays a crowd with submachine "
            "gun fire'. Drives 'like a son-of-a-bat' -- rumor says he was a pro on the virtual circuit."
        ),
        "background": (
            "Internationally experienced freelance bodyguard; the safety of his charge is paramount, more "
            "important than his own. Drives Shawn to school in the family's black turbo Eurocar Westwind "
            "2000 every weekday (7:30 AM out, 3:30 PM back, side trips for ice cream or a mall), to "
            "Singtree's on Tuesdays and Thursdays, and on Saturday day trips with Kellie Ross; waits in "
            "Singtree's lobby ignoring Nora's eye contact. Arrives at Brandis in his own car at 7:15 and "
            "has it valet-parked."
        ),
        "notes": (
            "Stats: B6(9) Q6 S5 C4 I5 W5, Ess 0.4, R5(9), Init 9 + 3D6; TR 6/4; Armed 6, Car 9, "
            "Electronics 4, Etiquette (Corporate) 4, (High Society) 4, Firearms 8, Negotiation 5, Stealth 6, "
            "Unarmed 8. Beta-grade: cybereyes (low-light, flare compensation), dermal plating 3, smartlink, "
            "vehicle control rig 2, wired reflexes 2. Armored jacket 5/3, concealed holster, DocWagon Gold, "
            "Franchi SPAS-22 (40 regular, 20 gel 8S Stun, smartlink, +2 RC), Savalette Guardian (4 clips "
            "APDS, 4 clips gel 7M Stun, smartlink), pocket secretary, boosted ear phone, tres chic "
            "clothing. Westwind 2000: Handling 3/8, Speed 80/240, B/A 4/9, Sig 2, Autopilot 3, anti-theft 5, "
            "APPS, mobile PANICBUTTON and vidphone, runflats. On the road: knows it is a kidnap not a hit "
            "and assumes the runners are tied to the Chicago job; alerts local law freely by headware "
            "phone; makes for a border crossing or Ares/Fuchi grounds (never a European or Asian corp); "
            "uses the car's speed and terrain, bails with Shawn when it takes damage, fires stun rounds "
            "until someone aims at his head -- and hands the boy over the moment Shawn's life is in "
            "danger, to get him back later. Debriefed by Knight Errant afterward. A superb future contact "
            "or opponent."
        ),
        "contact_skills": ["Executive-protection tradecraft and combat driving", "Denver corporate-enclave routines"],
    },
    {
        "name": "Audrey W.",
        "role": "Internationally famous crusading cybersnoop of The All-Seeing Eye; hunts the runners across Denver because Shawn's story is her own neglected childhood",
        "archetype": "Media Reporter",
        "title": "Producer and host, The All-Seeing Eye (syndicated trideo news-magazine)",
        "race": "Human",
        "gender": "Female",
        "nationality": "CAS (Texas; raised in Houston)",
        "organization": "The All-Seeing Eye",
        "connection": 5,
        "description": (
            "Tall, attractive and distinctive: long blond hair ('Think she's a real blond?'), pale blue "
            "eyes, dressed for action in the latest rough-and-tumble fashion -- on air, chic Abandallo "
            "business suits on a custom virtual set; to network meetings, a black T-shirt reading "
            "'Because I'm The Bitch, That's Why'. Cool, sharp, penetrating; seeing her in a restaurant "
            "makes hardened executives sweat. Off camera and face to face she is far more subdued, wants "
            "to know if the boy is safe, and cannot hold a casual conversation to save her life."
        ),
        "background": (
            "Daughter of a wealthy Texas couple (Audrey is not her real name) who says she did not "
            "realize who her parents were until she introduced herself at about ten; fled their control "
            "early and worked her way up on the streets of Houston as a reporter, apprenticed to the "
            "hot-shot Wyatt Holliday and to every broadcast and cable station in town. Her series on "
            "Texas-Aztlan BTL smuggling was picked up by an international syndicate; a year as a regular on "
            "'HotFlash!' and then her own program. Forces herself to stay cold and detached, and cannot "
            "when a story echoes her past. Aggressive, target-oriented, uncompromising, an idealist about "
            "truth and justice. Little is known of her private life; most assume she has none."
        ),
        "notes": (
            "Stats: B5 Q6 S4 C6 I4 W5, Ess 0.15, R5(6), Init 5(6) + 2D6; TR 4/4; Driving 2, Electronics "
            "(B/R) 1, Video (B/R) 3, Etiquette (Corporate) 7, (Media) 4, (Street) 5, Firearms 4, "
            "Interrogation 2, Video Interview 6, Leadership 1, Video Reporting 5, Portacam 5. Boosted "
            "reflexes 2, cyberears (amplification, select sound filter 4, recorder interface), Dr. Spott "
            "Smartcam, Eyecrafter Opticam package, 200 Mp headware, smartgun link. Ares Predator II (APDS, "
            "smartlink), Ingram Smartgun, armor jacket 5/3, lined coat, two line taps, bug scanner 6, data "
            "codebreaker 5, jammer 5, signal locator with two tracking signals, voice identifier 3, AZT "
            "Micro20 microcamcorder, Sony CB-5000 cybercam, Steadicam mount, 1,000 Mp auxiliary memory, "
            "secure short-haul transmitter, DocWagon Platinum, a Honda-GM 3220 ZX Turbo (Handling 4/8, "
            "Speed 50/150, B/A 2/0). Opposed Intelligence or Charisma vs her Willpower 5 reveals she is "
            "hiding something (1), that it concerns the boy (2-3), that she genuinely cares (4+). Cannot "
            "take Shawn -- she knows she would pay him no more attention than his parents -- but if prodded "
            "may use her contacts to place him with childless friends or an artistic commune deep in NAN "
            "lands; a GM who wants an obvious ending can let a persuasive team talk her into it. Does not "
            "find the runners before Decision Time. Harasses them on air throughout."
        ),
        "contact_skills": ["Continental media reach and an on-demand broadcast slot", "Corporate and street sources across North America"],
    },
    {
        "name": "Jack Drew",
        "role": "Denver fixer-turned-Johnson who supplies the safe house, the van and the budget, and delivers the news that there are no instructions",
        "archetype": "Fixer",
        "title": "Fixer and Johnson, Front Range Free Zone; Corporation X's on-site representative",
        "race": "Human",
        "gender": "Male",
        "nationality": "Front Range Free Zone",
        "organization": "Corporation X",
        "connection": 4,
        "description": (
            "A muscular black man of average height with collar-length black hair, gray eyes, a wide face "
            "and a wider smile that matches his easygoing, null-perspiration sense of humor. 'Big black guy "
            "-- saw him kill someone with a swizzle stick once. I mean, the guy he killed had one.' A fixer "
            "by trade who lately acts more often as a Johnson and feels his career sliding that way. "
            "Straight shooter, resourceful, very loyal to his employer. Very loyal."
        ),
        "background": (
            "Hired by Corporation X through a cash account and an e-mail address; does not know who his "
            "employer is and has no desire to find out. Arranged the Sioux Sector safe house, its gang of "
            "lookouts and a 15,000-nuyen operating budget of which he may keep half of whatever he does "
            "not spend, so he outfits the team as cheaply as he can. Knows about the mission and does not "
            "find it interesting."
        ),
        "notes": (
            "Stats: B4 Q3 S5 C5 I4 W4, Ess 1.4, R3, Init 3 + 2D6; TR 3/3; Computer 3, Electronics 3, "
            "Etiquette (Corporate) 3, (Street) 4, Firearms 3, Negotiation 6; Appraisal of High Tech Items 6, "
            "Equipment Acquisition 4. Boosted reflexes 1, thermographic cybereyes, datajack, 300 Mp "
            "headware. Fichetti 500a (laser sight), lined coat 4/2, pocket secretary, DocWagon Basic. "
            "Vehicles: Leyland-Rover Transport Minibus (Handling 4/8, Speed 35/105, B/A 5/15, nine folding "
            "benches, anti-theft 6, turbo, aural masking 4, armor +15, body +2) and an off-the-lot white "
            "and blue Saab Dynamit 776TI (Handling 4/8, Speed 80/250, B/A 2/3, roll cage) for when speed "
            "matters and there are no trolls to carry -- p.12 calls it a '776M'. Passcode from the runners: "
            "'Hey chummer, I'm finally here! Can you pick me up?'; e-mail forwards to his pocket secretary, "
            "answers in 2D6 x 10 seconds, arrives in 3D6 x 5 minutes (traffic and checkpoints). Handles "
            "supplies but should not hang around; may be talked into driving or minding Shawn; not a team "
            "member, fights only in self-defense. At 132:00: 'It's over. We're done... There are no "
            "instructions.' A good recurring Denver fixer."
        ),
        "contact_skills": ["Denver safe houses, vehicles and supplies", "High-tech appraisal and equipment acquisition"],
    },
    {
        "name": "Dr. Martin Singtree",
        "role": "Shawn's psychotherapist -- a warm, round Owl-follower with a memory like a vault and a side business in therapy corps never hear about",
        "archetype": "Psychotherapist",
        "title": "Licensed UCAS psychotherapist, Singtree Medical Building, UCAS Sector",
        "race": "Human",
        "gender": "Male",
        "nationality": "UCAS (Native American)",
        "connection": 3,
        "description": (
            "Short and round, dark graying hair, large round spectacles, warm and charming -- the strength "
            "his practice relies on. Not a shaman, but he follows the ways of the Owl totem and his office "
            "is decidedly tribal for UCAS territory. Prescribes no medication and uses no technological "
            "therapy aids: a holistic approach. Legwork calls him 'Marty', 'quite a charismatic little "
            "fellow', living rather well for a mid-level practice. The family schedule on p.25 misnames "
            "him 'Marvin'."
        ),
        "background": (
            "Registered psychotherapist licensed in the UCAS with a below-average count of complaints and "
            "malpractice suits, not listed in the UCAS Who's Who of Psychotherapists. Specializes in "
            "private cases -- a lucrative side business in corporate employees who need help and do not "
            "want Big Brother Corp to know; friends of Anna's who used him quietly recommended him, and she "
            "preferred him to a corporate expert in psychological conditioning. Has worked with Shawn on "
            "post-event trauma for some time; the boy is making progress, and Singtree has begun to see "
            "that the problem is the family, not the father's departure. Debating how to tell Anna; fears "
            "Shawn will be in therapy for life unless the family changes."
        ),
        "notes": (
            "Average People stats with all Mental Attributes 5 and Professional Skill 5; TR 1/2. Sessions "
            "Tuesday and Thursday 5:00 PM, one hour. Remarkable memory, so minimal files: Shawn's is notes "
            "in outlandish psycho-jargon (Psychology (4); Intelligence default TN 12) blaming the parents' "
            "poor care, noting withdrawal and disassociation. If the runners grab him to help Shawn he "
            "keeps the boy together, tells them in no uncertain terms they are fragging him up, says his "
            "environment must change, and privately believes Shawn should be taken from his parents -- "
            "'might solve some problems, could create others'. After a return home he may be able to use "
            "the disruption to move Anna, or not. Receptionist Nora at the desk."
        ),
        "contact_skills": ["Discreet therapy for corporate employees", "Child trauma and family assessment"],
    },
    {
        "name": "Nora (Singtree's receptionist)",
        "role": "Dr. Singtree's Arapaho receptionist and assistant, who shares his desktop computer and wastes suggestive glances on Peter Tomita",
        "archetype": "Receptionist",
        "title": "Receptionist/assistant to Dr. Martin Singtree",
        "race": "Human",
        "gender": "Female",
        "nationality": "Arapaho (full-blooded)",
        "connection": 1,
        "description": (
            "A full-blooded Arapaho Indian who runs Singtree's front desk and shares the practice's only "
            "computer with him. While Shawn is with the doctor she tries suggestive eye contact on Peter "
            "Tomita in the waiting room; he ignores all of it."
        ),
        "notes": (
            "Average People with TR 2/3 -- steadier under pressure than her boss. Knows the desktop is only "
            "switched on in business hours (Green-3, Access 2) and who comes and goes on Tuesdays and "
            "Thursdays at five."
        ),
    },
    {
        "name": "Kellie Ross",
        "role": "Shawn's freelance weekend nanny/governess -- useless as a hostage and no comfort to the boy",
        "archetype": "Nanny / Governess",
        "title": "Freelance companion/nanny/governess, Front Range Free Zone; weekend adult companion to Shawn Gaffney",
        "race": "Human",
        "gender": "Female",
        "nationality": "Front Range Free Zone",
        "connection": 1,
        "description": (
            "A freelance companion/nanny/governess working in the Front Range Free Zone (Shadowland TN 8 "
            "to learn even that), hired by Anna to take Shawn places on Saturdays and to give his mother a "
            "day of rest on Sundays. Shawn is not particularly fond of her."
        ),
        "notes": (
            "Average People. Present on most weekend day trips with Tomita -- covert footage of those trips "
            "turns up on The All-Seeing Eye. If the runners grab her to mind the boy they could not be more "
            "wrong: angry, then desperately afraid, dysfunctional within hours, cycling compliance and "
            "rebellion, no use to Shawn or the team even at her most 'with it'. Shawn does not know what "
            "to make of the changed woman and is barely affected."
        ),
    },
    {
        "name": "Dotti Findler",
        "role": "Shining Bright School's student liaison and nurse -- the adult every pupil's problem goes through, and the coat-check gatekeeper at the start and end of the day",
        "archetype": "School Administrator",
        "title": "Student liaison and school nurse, Shining Bright School",
        "race": "Human",
        "gender": "Female",
        "nationality": "Pueblo Corporate Council (Denver)",
        "connection": 1,
        "description": (
            "Ms. Findler's office is where students take problems, complaints and other concerns; she "
            "doubles as school nurse, trained on the medical/diagnostic expert system, with at least two "
            "other people always working in her office. Students need her help to get into the coat "
            "check, and she is always on duty near it when school starts and ends."
        ),
        "notes": (
            "Average People. Wears a staff alert bracelet (guards in 1D6 turns). The school's equivalent "
            "of a Platinum DocWagon contract runs through her station. A social-engineering way in: a "
            "'concern' about Shawn brings his file, his schedule and his half-hour in the Big Room."
        ),
    },
    {
        "name": "Walter Denhurst",
        "role": "Headmaster of the Shining Bright School, with every security monitor on his office wall",
        "archetype": "School Administrator",
        "title": "Headmaster, Shining Bright School",
        "race": "Human",
        "gender": "Male",
        "nationality": "Pueblo Corporate Council (Denver)",
        "connection": 2,
        "description": (
            "Headmaster of an exclusive expert-system academy of thirty-eight children, sitting above two "
            "mid-level and three low-level administrators in office I, with access to every one of the "
            "building's security monitors -- every room but the offices, lounges and bathrooms, and all the "
            "grounds."
        ),
        "notes": (
            "Average People. The face of 'advanced modern education theory' with no soul; his school has "
            "no modern music recordings or music technology of any kind, which is why nobody noticed "
            "Shawn's talent. Calls Falconer's decker and Pueblo Security Enterprises."
        ),
    },
    {
        "name": "Mario S.",
        "role": "The Coleridge-Gaffney condo's off-site cook, master of a grossly overstocked larder",
        "archetype": "Cook",
        "title": "Cook, Coleridge-Gaffney condo, Brandis Development",
        "race": "Human",
        "gender": "Male",
        "nationality": "Front Range Free Zone",
        "connection": 1,
        "description": (
            "Presides over the post-modern kitchen at mealtimes and lives off-site; dinner is on the "
            "black-glass table at 7:00 PM whether Anna is home or not, and the storage locker is grossly "
            "overstocked in case she asks for anything -- anything at all."
        ),
        "notes": (
            "Average People. Knows the family's real routine better than anyone but Tomita and the maid; "
            "comes and goes through the valet garage."
        ),
    },
    {
        "name": "Miriam Fox-Wallow",
        "role": "President/CEO of Fuchs-Auberlien Financial Services in Cheyenne -- public record only",
        "archetype": "Corporate Executive",
        "title": "President/CEO, Fuchs-Auberlien Financial Services (Cheyenne, Sioux Nation)",
        "race": "Human",
        "gender": "Female",
        "nationality": "Sioux Nation",
        "organization": "Fuchs-Auberlien Financial Services",
        "connection": 5,
        "description": (
            "Named in FAFS's public corporate profile as President/CEO of the Cheyenne-based consultancy; "
            "nothing else is said of her."
        ),
        "notes": (
            "Name-level entry from the Legwork corporate profile (p.47). The decisions that matter -- "
            "refusing Audrey W., moving the Gaffneys to Denver, the 50,000-nuyen reward, the offer Anna "
            "cannot refuse -- are FAFS's, and she is the name on the door."
        ),
    },
    {
        "name": "Elliot Winright",
        "role": "President/CEO of Dassurn Securities and Investments, Seattle -- public record only",
        "archetype": "Corporate Executive",
        "title": "President/CEO, Dassurn Securities and Investments (Seattle, UCAS)",
        "race": "Human",
        "gender": "Male",
        "nationality": "UCAS",
        "organization": "Dassurn Securities and Investments",
        "connection": 5,
        "description": (
            "Named in Dassurn's public corporate profile as President/CEO of the Seattle banking and "
            "investment house that extracted Colin Gaffney; nothing else is said of him."
        ),
        "notes": (
            "Name-level entry from the Legwork corporate profile (p.47). Dassurn's mouthpiece denies any "
            "part in the kidnapping and means it; rumor puts the company on Saeder-Krupp's acquisition "
            "list."
        ),
    },
]

ORG_UPDATES = {
    "Knight Errant Security Services": {
        "notes_append": (
            "Divided Assets (Denver, 2055): Fuchs-Auberlien Financial Services' contracted security "
            "firm; the contract covers FAFS employees and their families, so KE reacts in force to anything "
            "at the Brandis Development (whose security it designed and loosely oversees, with a PR rep in "
            "the main tower's office M2) and keeps officers loitering in the Yamatetsu building. Denver HQ "
            "in the UCAS Sector's non-contiguous region. Cannot prevent the kidnapping but takes control "
            "within fifteen minutes: Anna under guard at her condo in half an hour, the whole development "
            "locked down, Tomita debriefed. Ninety minutes in, a forensic magic team (sorcerer-adepts, "
            "Sorcery (Forensic Magic) 5, Preserve spell) collects half of any usable blood from Serious or "
            "Deadly wounds at the scene while three Combat Mages (TR 4/3, Magic Pool 12, base TN 5) and a "
            "Former Wage Mage (TR 3/3) on astral guard begin a Force 5 Detect Life ritual: material link "
            "by 05:30, Sending by 22:30, the fourth mage astrally tracks Shawn by 34:00, reports to HQ and "
            "sits on the place while troops muster (30-45 minutes). The ritual sample is astrally "
            "vulnerable -- a gutsy runner can track the Sending and destroy it. A call from Shawn's phone is "
            "traced in 2D6 + 4D6 + 2D6 minutes; DocWagon reports any bracelet trigger under a standing "
            "agreement and KE arrives in three times DocWagon's time. A KE decker (Corporate Decker, TR "
            "6/3, all passwords) enters the Brandis system in 2D6 turns on any active alert. Runs a joint "
            "investigation with Eagle Security Services; Audrey W.'s reports tarnish KE's image and it "
            "complains to her network in vain. Four team karma for avoiding the ritual."
        ),
        "allies_add": ["Fuchs-Auberlien Financial Services", "Eagle Security Services Inc."],
        "enemies_add": ["The All-Seeing Eye"],
    },
    "Lone Star Security": {
        "notes_append": (
            "Divided Assets (Denver, 2055): 'Lone Star Security Services Denver' polices the UCAS Sector "
            "of the Front Range Free Zone, including Dr. Singtree's office and the FAFS/Yamatetsu offices "
            "in the non-contiguous downtown sector; it is all over any grab there 'in a matter of "
            "moments' (response per Denver GM pp.53-54; combat mage on a second roll at +2). Little to do "
            "with the long-term hunt: Anna and Shawn are UCAS citizens living in a foreign country (the "
            "Sioux Sector) and attached to a multinational, so Lone Star and the UCAS government leave the "
            "investigation to Knight Errant."
        ),
    },
    "DocWagon": {
        "notes_append": (
            "Divided Assets (Denver, 2055): Shawn Gaffney carries a Gold contract with an emergency "
            "trigger built into a sealed-band wrist phone (Neo-Anarchists' Guide p.43); Tomita has Gold, "
            "Audrey W. Platinum, Jack Drew Basic, and the Shining Bright School the equivalent of a "
            "Platinum contract. DocWagon has an agreement with Knight Errant to notify it whenever anyone "
            "under KE protection requests service, so the boy's bracelet is a homing beacon: KE troopers "
            "arrive in three times DocWagon's response time. Shawn is likely to trigger it around 58 or "
            "92 hours into his captivity unless the runners take it or calm him."
        ),
        "allies_add": ["Knight Errant Security Services"],
    },
    "Yamatetsu Corporation": {
        "notes_append": (
            "Divided Assets (Denver, 2055): Yamatetsu owns the downtown tower in Denver's non-contiguous "
            "UCAS Sector (Location Q on the Denver downtown map) where Fuchs-Auberlien Financial Services "
            "rents three floors. Yamatetsu's own people run building security -- passcard entry, a "
            "holding area for unvouched visitors -- and the corp has become 'a stickler for security' "
            "because of internal problems unrelated to the adventure (Corporate Shadowfiles pp.150-52). "
            "Knight Errant officers loiter in the lobby on FAFS's behalf."
        ),
        "allies_add": ["Fuchs-Auberlien Financial Services"],
    },
    "Saeder-Krupp Heavy Industries": {
        "notes_append": (
            "Divided Assets (2055): Seattle's Dassurn Securities and Investments is rumored to be 'on "
            "Saeder-Krupp's acquisition list, but there doesn't seem to be any activity' (corporate "
            "legwork, TN 8)."
        ),
    },
    "Sioux Nation": {
        "notes_append": (
            "Divided Assets (2055): Cheyenne is the home office of Fuchs-Auberlien Financial Services. In "
            "the Front Range Free Zone the Sioux Council Sector holds the Brandis Development corporate "
            "enclave (near East 71st and Lafayette) and Jack Drew's safe house, and is policed by Eagle "
            "Security Services Inc.; Corporation X's forged travel passes cover the Sioux Sector along "
            "with UCAS and Pueblo. Anna and Shawn live there as resident aliens on UCAS passports."
        ),
    },
    "Pueblo Corporate Council": {
        "notes_append": (
            "Divided Assets (2055): the Pueblo Corporate Council Sector of the Front Range Free Zone "
            "holds the exclusive Shining Bright School (near 10th Avenue and Depew Street) and is policed "
            "by Pueblo Security Enterprises, which gives the kidnapping low priority once Knight Errant "
            "claims a megacorporate dependent. The school's public SAN sits on the NA/PUE grid "
            "(429-3329)."
        ),
    },
    "UCAS Federal Bureau of Investigation": {
        "notes_append": (
            "Divided Assets (Denver, 2055): technically involved in the Gaffney kidnapping -- UCAS "
            "citizens abducted in the Sioux Sector -- but, like the CIA to a lesser extent, the Bureau "
            "keeps only an advisory eye on a case the victims' megacorporation and Knight Errant are "
            "running."
        ),
    },
    "Aztlan": {
        "notes_append": (
            "Divided Assets: Audrey W.'s career break was a series of reports on Texas-Aztlan BTL "
            "smuggling, picked up by an international trideo-distribution syndicate."
        ),
    },
    "Shoalwater Elven Community": {
        "notes_append": (
            "Divided Assets (2055): the book's 'A Home With a Friend' option suggests the runners might "
            "convince 'Marti, leader of the Shoalwater Elven Community' to take in the kidnapped "
            "eight-year-old Shawn Gaffney for a time, if the team earned that kind of favor in Ivy and "
            "Chrome. Likelihood is the GM's call; a pacifist commune of sixty-five with thirty children "
            "is one of the few plausible homes the adventure offers."
        ),
    },
}

LOC_UPDATES = {}

NPC_UPDATES = {
    "Euphoria": {
        "notes_append": (
            "Divided Assets (Denver, 2055): an aged poster of 'simsense star Euphoria' hangs on the far "
            "wall of the kitchen in Jack Drew's Sioux Sector safe house -- four years after her "
            "disappearance she is still pin-up decor in a dead Denver print shop."
        ),
    },
    "Marti Vann": {
        "notes_append": (
            "Divided Assets (2055): Decision Time names 'Marti, leader of the Shoalwater Elven Community' "
            "as someone the runners might persuade to take in Shawn Gaffney for a time. She cannot decide "
            "for the council alone; expect the consensus process from Ivy and Chrome."
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
The book uses its own **Layered Matrix System** (pp.62-64): each system is a stack of layers joined by
SANs; nodes inside a layer have no spatial relationship, only a security code and IC. Finding a node is
a Sensor Test against its code (Hacking dice up to MPCP, Complex Action); entering a coded node is a
Computer Test (Simple Action, Hacking dice up to Computer skill); from a layer CPU a decker can move
anywhere in the layer; UMS nodes show as "?" until identified; hardwired paths carry no IC. To build
these in the designer, treat each layer as a host section and hang the listed nodes off its CPU/SPUs.

**1. Shining Bright School** (p.17). No security decker on staff; Falconer Protective Services' decker
enters the Restricted layer by hardwire in 2D6 turns (Corporate/Security Decker, TR 4/3). Object of
interest: the day's class schedule (Administration layer) and Shawn's records (Restricted layer).

| Layer / node | Function | Rating / IC |
|---|---|---|
| Public Access -- SAN-1 (NA/PUE 429-3329) | Public scheduling, e-mail, promotional files; sculpted as the school building and a lobby of kiosks | Green-3, Access 2 |
| Public Access -- SPU + datastore | Public information only | none |
| Administration -- SAN-2 (from Public via e-mail) | Internal path | Orange-4, Access 6 |
| Administration -- SAN-3 (from Public via public records) | Internal path | Orange-4, Barrier 5 |
| Administration -- Departmental SPUs | One per department, datastores and I/O ports; UMS polygons | Orange-3, Access 3 |
| Administration -- Administration SPU | Daily class schedules in its datastores | Orange-4, Access 5, Killer 4 |
| Administration -- Building Maintenance SPU | Datastores, I/O, slave module for sprinklers / fire alarm | Orange-3, Access 3 |
| Restricted -- SAN-4 (hardwired from Falconer) | External path; no IC (hardwired) | Red-5, Access 6, Blaster 6 |
| Restricted -- SAN-5 (from Administration SPU) | Internal path | Red-4, Access 6, Killer 4 |
| Restricted -- Administration SPU | School and student records, accounting, inventory | Red-3, Access 4, Killer 3 |
| Restricted -- Security SPU | Records datastore, I/O ports, slave modules for motion detectors and cameras | Red-3, Access 5, Killer 4 |

**2. Brandis Development** (pp.24-25). Two layers; almost nothing worth hiding. Any active alert
brings a Knight Errant decker (Corporate Decker, TR 6/3, all passwords) in 2D6 turns. Central security
office alarms are hardwired to KE outside this system.

| Layer / node | Function | Rating / IC |
|---|---|---|
| Outer -- SAN-1 (NA/SIO/877-29291, listed) | Public access | Orange-4, Access 4, Killer 3 |
| Outer -- Layer CPU | Administration and building maintenance; UMS | Orange-5, Barrier 4 |
| Outer/Inner -- SAN-2 | Link between layers | Orange-5, Access 5, Killer 4 |
| Inner -- Residential SPUs (one per tower) | I/O ports in every condo (networked desktops) | Orange-4, Access 4 |
| Inner -- Residential Datastore | Shared storage, one Scramble 3 partition per condo | Orange-4, Access 4, Scramble 3 |
| Inner -- Administration SPU | Complaints, security problem reports | Orange-5, Access 5, Killer 4 |
| Inner -- Administration Datastore / I/O ports | | Orange-4, Access 3 / Orange-4, Access 4 |
| Inner -- Security SPU | Security terminals, cameras, sensors, datastore | Red-4, Access 6, Blaster 4, Tar Pit 4 |
| Inner -- Security Datastore | | Red-4, Access 6, Scramble 4 |
| Inner -- Security I/O ports / slave nodes | Terminals; cameras and sensors | Red-4, Access 5 |

**3. Fuchs-Auberlien Financial Services, Denver** (pp.29-30). Separate from the Yamatetsu building's
systems. Nothing relevant to the adventure anywhere in it; the outer layers are lightly sculpted as a
late-1800s counting house and the core is 'a white-hot kernel of nasty IC'.

| Layer / node | Function | Rating / IC |
|---|---|---|
| Outer -- SAN-1 (NA/SIO 2928-1028, listed) | Public access | Red-4, Access 5, Killer 5 |
| Outer -- SAN-2 (NA/SIO 2918-2918, unlisted) | Automatic data transfers | Red-4, Access 5, Killer 5 |
| Outer -- SAN-3 (to Secondary) | Internal path | Orange-4, Access 4, Blaster 4 |
| Outer -- SAN-4 (to Core) | Internal path | Red-5, Access 6, Blaster 5 |
| Outer -- Layer CPU | Most SPUs, I/O ports and reference datastores live here | Red-5, Access 6, Trace and Burn 4 |
| Secondary -- SAN-5 (to Core) | Internal path | Red-5, Access 6, Blaster 5 |
| Secondary -- Processing SPUs (3) | Non-critical data crunching | Red-4, Access 5, Killer 4 |
| Secondary -- Processing Datastores (3) | One per SPU | Red-4, Access 5, Tar Pit 4, Scramble 4 |
| Secondary -- Layer CPU | | Red-5, Access 6, Trace and Burn 5 |
| Core -- Processing SPUs (2) | Critical data; UMS | Red-5, Access 6, Blaster 5 |
| Core -- Processing Datastores (2) | | Red-5, Access 6, Tar Pit 5, Scramble 5 |
| Core -- Layer CPU | | Red-6, Access 6, Blaster 6, Trace and Burn 5 |
| Core -- roaming | Probe-6 IC linked to Blaster-6 patrols the layer (treat as mobile Access-6 + Blaster-6 without Virtual Realities) | -- |

**4. Dr. Singtree's office desktop** (p.28). A shared desktop with no permanent Matrix connection,
reachable only while switched on in business hours: CPU and datastore Green-3, Access 2 on the SAN/CPU.
Holds Shawn's file in psycho-jargon. Not worth a host of its own.

**5. Corporate/Security Decker profile** (p.56) for any NPC decker: B2 Q3 S1 C1 I4 W3, Computer 5,
Computer Theory 4, Etiquette (Matrix) 4; cyberdeck MPCP = 2 x Professional Rating, persona programs
1.5 x PR, hardening = PR, response increase +2/+1D6 per two points of Threat Rating (max +6/+3D6),
PR utilities from each of Combat/Defense and Sensor/Masking at 1.5 x PR. Falconer's decker TR 4/3;
Knight Errant's TR 6/3.

**6. Skyscraper emergency escape systems** (p.8): cable controls sit in protected slave nodes adjacent
to and reachable only through the building's security subprocessor, usually off the Matrix and often
on an autonomous system; they can freeze a cable mid-descent. Worth a node in any corporate tower host.
"""

NOT_BUILT = """
- **The two Johnsons** (the pigeon-feeding man in the cream suit; the datajacked woman with the white
  umbrella) -- unnamed; stats and behavior on the Corporation X row. **The park** with the stagnant pool
  where they meet is in the runners' home sprawl and never named.
- **The safe-house gang** (mixed human/metahuman, average, stoned, on Drew's payroll) -- on the safe
  house row. **Brandis staff**: stable hands, tennis pros, lifeguards, garage attendants, lobby
  staffers, the maid, the property-management corporation and its twelve guards -- on the Brandis row.
  **Shining Bright staff**: five administrators, faculty, three kitchen staff, two ork janitors, the
  technical specialist, the three Falconer guards and combat mage -- on the school and Falconer rows.
- **Anna's Toyota Elite chauffeur** (Bodyguard archetype, TR 4/3), **street cops and bystanders** who
  may aid Tomita (2D6 on the road), **Knight Errant's forensic and ritual mages** and **KE/ESSI/PSE
  troopers** -- on the Tomita and law-enforcement rows.
- **The Chicago extraction team** (two runners, one captured by Eagle Security; the anonymous one who
  later talks to Audrey), **Chicago fire department**.
- **Wyatt Holliday** (the Houston hot-shot reporter Audrey apprenticed to), **"HotFlash!"** (the trideo
  newsmagazine she left), **Abandallo** (her suit label), **Audrey's Denver crew** -- on the Audrey and
  All-Seeing Eye rows.
- **Milken Securities University** (Manhattan), **Cambridge University**, **the Roos Institute for
  Pan-Economic Studies** (London), **Adaptive Economic Theory** (online journal), **the NIEE** -- CVs.
- **Butt-Kicking Banzai Raiders**, **El Butcher**, **Sam the rubber lizard**, **Smelly Glop** -- Shawn's
  gear. **Anna's Beacon Hill parents**, **the estranged relative** the GM may invent for the ending.
- **Name-drops and rulebook references**: Ares and Fuchi are named only as North American megacorps
  whose grounds Tomita would flee to; **Corporate Shadowfiles**, **Denver: City of Shadows**, **Shadowbeat**,
  **Lone Star Sourcebook**, **Virtual Realities**, **Neo-Anarchists' Guide** are rulebook references.
"""

PLAY_NOTES = """
- Not a decision tree and not about guns: the first encounter sets the situation, the middle
  encounters are places, and the end is a moral problem with no correct answer. The GM's job is to
  let the players discover Shawn's damage through hints, not theatrics, and then refuse them an easy
  out. Without an emotional link between at least one runner and the boy there is no dilemma.
- Seed The All-Seeing Eye broadcast during an earlier, unrelated run about two months before the hire,
  and stop the players building theories on it. The whole hire is engineered so the team assumes
  Dassurn and Seattle; never confirm or deny, and never let them identify Corporation X.
- Denver logistics matter: sector walls, three police forces, Rating 9 IDs that decay a point every
  two days (grab within two weeks), +2 to reach home contacts by telecom, doubled TNs for a stranger's
  own legwork, the Nexus as the shortcut. Getting a chromed troll into the UCAS Sector is a scene.
- The grab: the school is the hardest, the road is the likeliest (rush-hour traffic, Tomita's driving,
  stun rounds, and his surrender if Shawn is endangered), Singtree's is the softest but is Lone Star
  territory, Brandis is a hostage situation with smartgun-equipped troopers. FAFS's office is off the
  table -- Shawn never goes there. Make the players earn a quiet extraction (2 karma).
- The pressure is ritual magic: blood at the scene by 01:30, material link 05:30, Sending 22:30,
  found at 34:00. Teams that think ahead (no blood left behind, Shawn under magical protection, track
  and burn the sample, take the bracelet and phone) earn 4 karma; teams that do not get Knight Errant
  at the door on day two -- tip them off or hit them hard and keep them one step ahead for four days.
- Run Shawn on the timeline (10 / 49 / 58 / 92 / 117 hours) but let his moods change naturally; the
  Charisma (8) and (12) mechanics gate real conversation. Play music near him. Grabbing Singtree is
  legitimate and gives the players their diagnosis straight from a professional.
- Audrey W. exists to add pressure and options; she never finds the runners before Decision Time and
  will not take the boy unless the GM decides to hand the group an obvious ending. Meeting her on air
  is a trap; meeting her quietly gives perceptive runners her childhood.
- Endings the book lists: home to mother (easy, and the environment that damaged him), off to father
  (Colin must be pressured and may say no), Audrey's contacts (childless friends, an artistic commune
  in NAN lands), a friend of the team (Marti and Shoalwater from Ivy and Chrome), a runner adopts him
  (a can of worms), an invented estranged relative. Corporation X pays in full and the trip home is
  uneventful; the boy walks away unsure what will become of him.
- Karma: 10 team for completing; +2 minimum-fuss grab; +4 avoiding the ritual; individual awards per
  SRII p.199, adjusted for how the team handled the dilemma.
"""
