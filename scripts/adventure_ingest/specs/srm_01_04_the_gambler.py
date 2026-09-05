# SRM 01-04 The Gambler (FanPro / WizKids, 2004, Shadowrun Missions Season One, SR3) --
# campaign order #47. Redmond (Crusher 495, Touristville) and Everett (the Griffin Biotechnology
# compound off 172nd Street), with Auburn and downtown Everett gambling dens in the background.
# SETTING NOTE / DISCREPANCY WITH THE TASK BRIEF: commissioned as "Denver in the 2060s (SR4 era)";
# the book is Seattle and "For use with Shadowrun, Third Edition". Denver is never mentioned. Every
# location carries city "Seattle".
# Dating: no in-world date is printed. The run occupies 48 hours -- the meet is 9 PM on a Tuesday,
# the deadline 9 PM Thursday -- and takes place "at least two weeks after" the reconnaissance runs
# of SRM 00-03 FORCEd Recon, with the DocWagon second-quarter results already public. YEAR follows
# the campaign at 2064.
# ROW COUNTS: this spec creates no organizations at all and only four locations, because almost its
# entire cast and setting were already built by specs/srm_00_03_forced_recon.py (Griffin
# Biotechnology, Mackie Construction, the Everett research facility, the Marine Drive Stuffer Shack,
# the Brackhaus, Dohner and Draco Foundation properties, Dr. Indira Chontel and Rebecca Owls-Breath)
# and by specs/srm_00_02_demolition_run.py (Paladin Medical Technologies, Dr. Fredericks). Those rows
# are updated, never re-created; the bulk of this adventure's substance is therefore in the eleven
# ORG_UPDATES / LOC_UPDATES / NPC_UPDATES entries rather than in new rows.
# Editing inconsistencies in the book, noted again on the affected rows: Paladin is "Paladin
# Systems" in the plot synopsis and the legwork table, "Paladin Medical Services" in the Cast of
# Characters, on Alex's contact card, on the cyberware card and in the Shadowland thread, and
# "Paladin Biomedical" in the opening fiction, where Fredericks is also called its "president"
# rather than its CEO -- earlier books use Paladin Medical Technologies and that name is kept; the
# lead researcher is "Dr. Chontel" in the plot synopsis and the hire text and "Dr. Chantel" in the
# paydata paragraph, on both floor maps and throughout the KFIN article; the company is variously
# "Griffin Biotech", "Griffin Biotechnology" and "Griffin Biotechnologies"; the meet is "in Renton,
# at the club Crusher 495" in the plot synopsis but "Crusher 495 in Redmond" in The Hire, and the
# club is described as being on the edge of Touristville, which is Redmond; the adventure text says
# the residual background count around the perimeter wall is gone while the handout security report
# still lists a Background Count of 1 "everywhere inside the facility and three meters to either
# side of the main security wall"; The Hire refers the GM to "the racist attack encounter in the
# Extra Cards section", and no Extra Cards section exists anywhere in the adventure or the playing
# aids; guard distribution is "two two-man teams patrolling in each exterior quadrant" in the
# adventure and "four patrolling in each exterior quadrant" in the handout (the same headcount); and
# the Interrogating Personnel section still carries FORCEd Recon text about the facility being "only
# a week away" from opening and about employees commuting to "the old facility" downtown, both
# contradicted by this adventure's own update section.
# The arc-level continuity problem is bigger: SRM 01-01 Double Cross names Griffin's lead neurology
# researcher Dr. Chandra Dasari, while SRM 00-03 and this book give the identical research, role and
# shareholders'-meeting announcement to Dr. Indira Chontel. Both rows are kept and cross-referenced.
# Source text: docs/Adventures/text/SRM01-04A_The_Gambler.txt (20 pages) and
# docs/Adventures/text/SRM01-04B.txt (player handouts, including the full Griffin security report,
# the compound and floor maps, Alex's contact card and the Ambidexterity Router card).
# ASCII only (pre-commit hook).

ADVENTURE = "SRM 01-04 The Gambler"
ORDER = 47
SOURCE = "SRM01-04A_The_Gambler.pdf, pp. 3-20; SRM01-04B.pdf (player handouts)"
YEAR = "2064 (48 hours, Tuesday 9 PM to Thursday 9 PM, at least two weeks after SRM 00-03 " \
       "FORCEd Recon; no in-world date is printed)"

SYNOPSIS = """
**Dr. Donald Kukalakee** bets on everything. He has watched a simfeed of a horse race in faraway
Saratoga eat most of a paycheque, he has been passed over for promotion twice because Griffin
Biotechnology considers a gambling addiction a security risk, and he is certain he knows more about
the brain and cybernetic interface design than **Dr. Renee Josario**, the woman put in charge of the
team that works most closely with **Dr. Chontel**. Some months ago one of **Dr. Fredericks**'s
agents started drinking in the same bars, then started lending him money. Paladin now pays
Kukalakee's debts, and pays him to gamble -- at **Stuck's Carnival** in Auburn, well away from his
own backyard, where there is also a girl called **Zoe**.

On Josario's last day before a conference in Atlanta, Don took her and some coworkers out for
drinks and lifted her ID badge out of her purse. He already knew her keycode: she uses her birth
year, 2029. He passed badge and code to Paladin with the warning that she would be back by the end
of the week, and did it precisely so that the fallout would land on her. He is too small a fish for
Paladin to extract yet; what he does not realise is how deep their hooks are already.

So on a quiet Tuesday evening at **Crusher 495**, an ork-owned bar on the edge of Touristville where
racial harmony prevails and Johnsons like the neutral ground, a bouncer points the runners at a back
booth and a well-dressed female ork introduces herself as **Alex**. The job is a datasteal: get into
the Griffin compound off 172nd Street in Everett, reach the stand-alone workstation in the small
room off Dr. Chontel's private lab, take the file tagged **Project 27**, and get out. Forty-eight
hours. One thousand nuyen down and ten percent of the data's value, negotiable to twenty. No
bloodshed, no damage, and above all no trace -- because Ms. Johnson's sponsors have assets inside
Griffin they do not want compromised.

She hands over Josario's passcard and code and a complete security package bought with previous
shadowruns, and asks the team to leave the badge in Josario's office on the way out. What she does
not hand over is the two weeks of changes since that package was compiled: monowire now runs along
the north wall as well, every sensor is live, the labs and Chontel's own windows have been lined
with biofiber, and Knight Errant's barghest and handler are on the grounds from eight o'clock on
the second morning. The runners can take the file on trust, or spend some of their forty-eight hours
finding out what it no longer says.

Griffin is a four-metre stone wall raised out of the ground by earth elementals, thirty-eight
Knight Errant guards a shift, four separate and deliberately unconnected computer networks, magnetic
anomaly detectors and chemical sniffers in the door frames, wards that turn solid in astral space
and spray fluorescing bacteria at anything that pushes through them, and a security director with
delta-grade wired reflexes and a shotgun. It also has one oversight: every external sensor and
camera runs straight into a slave node, so a team that reaches the compound quietly can tap the line
and own the security computer from the inside.

Weeks later, DocWagon Seattle posts its first record quarterly loss, Chontel's research is reported
destroyed in an unexpected system crash, and a shadowrunner on the boards is delighted with the new
router that lets him use his sword in either hand.
"""

TIMELINE = """
- **Over the past year** -- Griffin Biotechnology takes sizeable venture investment from DocWagon
  Seattle and Ares Macrotechnology, and Fredericks starts researching what could attract heavy
  hitters like that. He decides to keep tabs on Griffin.
- **Weeks of canvassing** -- one of Fredericks's agents befriends Don Kukalakee in the bars near the
  compound. Kukalakee likes to gamble. The agent starts lending him money.
- **A few weeks later** -- Kukalakee is a bought man and does not seem to mind, having high
  aspirations and few morals. Paladin moves his gambling to Stuck's Carnival in Auburn and starts
  paying him to be there.
- **Earlier still** -- Fredericks hires shadowrunners to scope out Griffin's new Everett facility in
  case future incursions become necessary (SRM 00-03 FORCEd Recon), and other agents keep probing.
- **Two or more weeks before the adventure** -- the reconnaissance runs are complete. Griffin moves
  fully into the compound; the old downtown offices shut; all security goes live.
- **Days back** -- Josario's last day before her Atlanta conference. Kukalakee takes her and some
  coworkers out for drinks and lifts her badge; he already knows her keycode is her birth year,
  2029. Both go to Paladin with the warning that she returns by the end of the week.
- **Tuesday, ~5 PM** -- fixers call the runners about "a matter of discretion". Four hours' notice.
- **Tuesday, 9 PM** -- the meet at Crusher 495. 1,000 nuyen down, 10 to 20 percent of the paydata.
  The 48-hour clock starts.
- **Wednesday** -- legwork and planning. Any hit before 8 AM Thursday misses the barghest patrol.
- **Thursday, 8 AM onward** -- Knight Errant's barghest and handler are working the grounds.
- **Thursday, 9 PM** -- deadline. Alex takes the chip in the same bar, this time with a bodyguard,
  verifies it on a small cyberdeck and pays the negotiated percentage.
- **Days later** -- Josario returns and her badge is reported missing, if it has not already been
  left in her office.
- **Weeks later** -- DocWagon Seattle posts record second-quarter losses; Chontel's critical research
  data is announced destroyed in "an unexpected system crash" days before prototype testing; Paladin
  begins field-testing the Ambidexterity Router; and Rose Croix is said to be opening negotiations
  with Paladin for the technology.
"""

ORGS = []

LOCATIONS = [
    {
        "name": "Crusher 495",
        "location_type": "bar",
        "city": "Seattle",
        "district": "Redmond Barrens (edge of Touristville)",
        "security_level": "Low Security",
        "summary": "Ork-owned Barrens bar on the edge of Touristville where racial harmony holds and Johnsons come for the neutral ground; Humanis occasionally tries a drive-by and it has never worked",
        "description": (
            "A bar on the edge of the Touristville section of the Barrens, owned and operated by a "
            "group of orks, where racial harmony generally prevails and Johnsons like to do "
            "business precisely because the ground is neutral. At nine on a Tuesday evening it is "
            "quiet: the crowd has not begun to arrive, the hardcore drinkers are wobbling out, and "
            "strangely everyone is getting along. Inside it is a genuine mixing pot of orks, "
            "humans and a few trolls and dwarfs all interacting together; only elves are noticeably "
            "absent. Booths line the back wall, and the bouncers know who is expecting whom. To the "
            "sprawl at large it is a taste of the Barrens for the mundanes; to the shadows it is a "
            "meet spot. Written up in New Seattle p.63."
        ),
        "notes": (
            "Both the hiring meet and the payoff happen here. Legwork ladder p.9 (any Barrens "
            "contact, Fixer, Data Broker or any ork; Ork Bars / Barrens Bars / Barrens Meet Spots / "
            "Barrens Runner Hang Outs, TN 4): 0 'Yeah, he's that wrestler, The Crusher, and 495 is "
            "his weight.'; 1 a bar in the Barrens, Touristville section; 2 ork owned, but pretty "
            "much everyone can go there, a taste of the Barrens for the mundanes; 3 Humanis "
            "occasionally likes to do a drive-by to try to scare off the metas, and it has not "
            "worked yet; 4+ the manager, Janus Koskey, knows everything worth knowing in Redmond "
            "and sells information for a fee. At the payoff Alex brings a large muscular ork "
            "bodyguard and verifies the data on a small cyberdeck at the table before paying. "
            "DISCREPANCY: the plot synopsis places the meet 'in Renton, at the club Crusher 495'; "
            "The Hire and the club's own description put it in Redmond, on the edge of "
            "Touristville. Redmond is correct."
        ),
    },
    {
        "name": "Stuck's Carnival",
        "location_type": "casino",
        "city": "Seattle",
        "district": "Auburn",
        "security_level": "Patrolled / Commercial",
        "summary": "The Auburn casino where Paladin pays Don Kukalakee to gamble, safely outside Everett; urban brawl and combat biking books, a bar, a restaurant and a girl called Zoe",
        "description": (
            "A casino in Auburn with urban brawl and combat biking books, a bar and a restaurant, "
            "and the kind of back rooms the book alludes to as 'more sordid ways' to spend a "
            "win. It is Don Kukalakee's regular house, which is not an accident: Paladin has been "
            "paying off his gambling debts to the point of actually paying him to gamble, and this "
            "is where the payments are made, deliberately well away from Everett so that he is not "
            "doing business in his own backyard. When he does win he blows it all immediately at "
            "the casino bar or the restaurant, or on Zoe, and the cycle starts again."
        ),
        "notes": (
            "No scene is written here and the whole conspiracy runs through it. This is where a "
            "Paladin agent hands a Griffin researcher money, where the badge and keycode almost "
            "certainly changed hands, and where Kukalakee is most easily found, most easily "
            "watched, and most easily leaned on. A team that wants to know who really hired them, "
            "or that wants insurance against Alex, has a name to follow and a room to sit in. It is "
            "also the reason Griffin's own security has never caught the leak: Kukalakee's known "
            "gambling problem is watched for in Everett, and he does his real business two "
            "districts away."
        ),
    },
    {
        "name": "Jason's Bar and Grill",
        "location_type": "bar",
        "city": "Seattle",
        "district": "Everett",
        "security_level": "Low Security",
        "summary": "A local Everett gambling den where Don Kukalakee slips and bets in his own backyard, against his handlers' arrangements",
        "description": (
            "A bar and grill in Everett that runs as a local gambling den, close enough to the "
            "Griffin compound that Kukalakee's colleagues drink in the same district. Paladin moved "
            "his action to Auburn precisely to keep him out of places like this, and occasionally "
            "he slips and gambles here anyway -- which is exactly the sort of lapse that gets a "
            "bought man noticed by the wrong people."
        ),
        "notes": (
            "Named once, in the What's Really Happening section, and worth keeping for two reasons. "
            "It is the nearest thing the adventure offers to a place where a runner could meet a "
            "Griffin employee socially without going through the compound's gate, which matters "
            "because Fredericks's own agent got at Kukalakee by 'canvassing a few nearby bars'. And "
            "it is the crack in Paladin's operational security: every time Kukalakee gambles in "
            "Everett he does it among people who know where he works."
        ),
    },
    {
        "name": "Paladin Beta Clinic",
        "location_type": "corporate facility",
        "city": "Seattle",
        "district": "Seattle metroplex (location unstated)",
        "security_level": "Corporate High Security",
        "controlling_org": "Paladin Medical Technologies",
        "summary": "The Paladin-owned beta-grade clinic Alex can open to runners who impress her -- three visits, negotiable down with gifts, and a field-test bench for stolen cyberware",
        "description": (
            "A beta-grade cyberware clinic owned by Paladin Medical Technologies, and the real "
            "reward of this adventure for a cybered team. Alex can arrange access for runners who "
            "were effective, creative or otherwise professional, and it can be used immediately. "
            "The book gives it no address and no staff -- it is a contact benefit rather than a "
            "place with a scene -- but its purpose in the corporation is clear enough: Paladin "
            "wants the Ambidexterity Router prototype in living subjects and to market quickly, and "
            "a clinic that will install a first-generation prototype for a shadowrunner off the "
            "books is where that happens."
        ),
        "notes": (
            "Access is earned, not bought: on Alex's contact card the character makes an Etiquette "
            "(6) test needing four or more successes, with the target number reduced by 1 for every "
            "5,000 nuyen given to Alex as a 'gift'. She will allow a total of three visits (the "
            "card carries three boxes). The one-time field-test offer that comes with taking her as "
            "a contact: any character with wired reflexes and 0.5 Essence remaining may have the "
            "Ambidexterity Router installed -- Essence 0.50, 50,000 nuyen, Availability 12 at one "
            "month, Street Index 4, legality as per Wired Reflexes, and it must match the grade of "
            "the wired system it attaches to. It is NOT available as beta or delta ware but can be "
            "had as alphaware to match existing wired reflexes, and if the owner ever parts with it "
            "the custom-built prototype is treated as betaware. Effect: six points of the "
            "Ambidexterity Edge (Cannon Companion p.96) -- off-hand penalties reduced by 3; ranged, "
            "the primary weapon fires at no penalty and the second at +1 target modifier with all "
            "other two-weapon rules unchanged; melee, no Off-Hand (Weapon) skill is needed but the "
            "secondary weapon uses half the dice of the primary skill, rounded down. Damage the "
            "unit and there is a 1-in-6 chance of an epileptic seizure every time the wired "
            "reflexes fire, lasting 1D6 combat turns during which the subject cannot dodge, move or "
            "act. The router is built from the plans the runners are stealing in this adventure."
        ),
    },
]

NPCS = [
    {
        "name": "Alexandra Detwiler",
        "role": "Paladin's professional Ms. Johnson, an ork who hires the team over a back-booth table and can open a beta clinic to anyone who impresses her",
        "archetype": "Corporate Fixer",
        "title": "\"Alex\" -- Ms. Johnson, Paladin Medical Technologies",
        "race": "Ork",
        "gender": "Female",
        "organization": "Paladin Medical Technologies",
        "connection": 4,
        "description": (
            "Well dressed, well groomed and well mannered, waiting alone in a back booth at an ork "
            "bar -- a professional Johnson who is entirely capable of handling herself around "
            "shadowrunners and is not intimidated by them. She has one blind spot and it is ugly: "
            "she is prejudiced against 'freaks', meaning anyone affected by SURGE and anyone who "
            "has voluntarily gone in for visible cyberarms or cyberskulls, reptilian orthoskin, "
            "balance tails or anything else that does not look normal. Such runners are ignored at "
            "best, and asked to wait outside if they are in any way rude or obnoxious; she has a "
            "low tolerance for insufferable weirdos. She has no tolerance at all for haggling: push "
            "her too far and she stands up, insults the team's professionalism, mentions the "
            "follow-on work they have just lost, and heads for the door."
        ),
        "background": (
            "A professional Johnson working for Paladin, and Fredericks's chosen instrument for the "
            "Griffin datasteal -- the 'specialist' on his staff he calls after taking the packet of "
            "data from his wall safe. Her knowledge skills say what she is: Cybertechnology 4 and "
            "Biotechnology 4, which is a Johnson who understands what she is buying. She keeps her "
            "own access to a Paladin-owned beta clinic and treats it as currency, which suggests "
            "she has been doing this long enough to know what shadowrunners actually want."
        ),
        "notes": (
            "No attributes are printed -- 'she is as good as she needs to be based on the tier of "
            "the table'. Etiquette (Corporate) 4 (5); Cybertechnology 4, Biotechnology 4; a pocket "
            "secretary. For negotiation her Negotiation skill is (3 + tier), so 4 against Green "
            "runners and 9 against Prime. TERMS: 1,000 nuyen down on acceptance, then 10 percent of "
            "the paydata's value, negotiable to 20 -- somewhere between 10,000 and 20,000 nuyen "
            "apiece per tier. She supplies Josario's passcard and keycode, a floor plan and the "
            "full security details bought from earlier shadowruns, and, if nobody on the team has "
            "Computer skill, a pocket-secretary-sized device that downloads the file by itself once "
            "hooked to the machine. She asks that the badge be left in Josario's office afterwards, "
            "and hopes the team will not waste time on legwork her employer went to great lengths "
            "to spare them. At the payoff she brings a large muscular ork bodyguard and verifies "
            "the chip on a small cyberdeck before paying. CONTACT CARD (SRM01-04B): ork female, Ms. "
            "Johnson for Paladin. Uses: jobs, clinic access. Meets at bars, clubs and private "
            "meeting rooms; email and phone; availability 1-6. Beta clinic access is an Etiquette "
            "(6) test needing four successes, -1 to the target number per 5,000 nuyen gifted, three "
            "visits maximum. Awarded as a Level 1 Contact to teams that were effective, creative or "
            "professional, along with the one-time Ambidexterity Router field-test offer."
        ),
        "contact_skills": [
            "Paladin datasteal and extraction contracts",
            "Beta clinic access (three visits)",
            "Cybertechnology and biotechnology assessment",
        ],
    },
    {
        "name": "Dr. Donald Kukalakee",
        "role": "The gambler of the title -- a passed-over Griffin researcher bought by Paladin, who stole his own boss's badge to frame her and take her job",
        "archetype": "Corporate Scientist",
        "title": "Researcher, Griffin Biotechnology (brain and cybernetic interface design)",
        "race": "Human",
        "gender": "Male",
        "organization": "Griffin Biotechnology",
        "connection": 3,
        "description": (
            "Standing riveted in a gambling parlour while a simfeed delivers the sights, sounds and "
            "smells of a horse race at Saratoga, unable to dodge a stampede that is not there, "
            "unable to contain the adrenaline -- and then unplugging the feed from his datajack "
            "with a sense of despair, close to tears, watching the payoffs scroll across the "
            "parlour's main screens. Another sure thing, another paycheque. He knows he has a "
            "gambling problem and cannot rid himself of it; to him it is more exciting than combat, "
            "which is itself just something else to wager on. He will bet on almost anything. "
            "Ambitious, aggrieved and, in Fredericks's assessment, 'the perfect blend of greed, a "
            "gambling addiction, a little ambition, and questionable morals'."
        ),
        "background": (
            "Griffin knows about the addiction and has tried to help him as best it can, but the "
            "problem alone makes him a security risk and has kept him from rising: he has been "
            "passed over for promotion twice, and now has to endure Dr. Josario, who leads the team "
            "that works most closely with Dr. Chontel. He believes he knows far more about the "
            "brain and cybernetic interface design than she does and that the job should be his. "
            "One of Fredericks's agents spent weeks canvassing bars near the facility before "
            "befriending him; within a few more weeks Don owed a great deal of money to a man only "
            "too happy to lend it in exchange for a little information, and he was bought -- and "
            "did not seem to mind. He eventually made the offer himself: for a little financial "
            "compensation he would hand his new friends the way to Griffin's cash cow, Dr. Chontel, "
            "and access to her research files, using his boss's credentials so that any fallout "
            "would land on her."
        ),
        "notes": (
            "No statistics; he never appears on stage. THE THEFT: on Josario's last day before her "
            "Atlanta conference he invited her and some coworkers out for drinks and slipped her ID "
            "badge out of her purse, having previously learned that she uses her birth year, 2029, "
            "as her keycode. He passed both to Paladin with the warning that she would be back by "
            "the end of the week -- which is the entire reason the run has a 48-hour clock. He is "
            "too small a fish for Paladin to extract at present, and expects to capitalise on the "
            "situation to move up, gain value to both companies and make a little nuyen for his "
            "habit; the book's closing note on him is that 'what he doesn't realise is how deep "
            "Paladin's hooks will then be in him'. Paladin now pays his debts and pays him to "
            "gamble, at Stuck's Carnival in Auburn rather than in his own backyard, where he has "
            "developed a taste for a girl named Zoe; he occasionally slips and gambles in Everett "
            "at Jason's Bar and Grill; and when he wins he blows it all at once and starts again. "
            "He is the run's alternative solution: a team that identifies the leak instead of "
            "climbing the wall has a Griffin insider with a career-ending secret and every reason "
            "to cooperate."
        ),
        "contact_skills": ["Griffin research staff, projects and internal politics", "Neural interface and cyberware design"],
    },
    {
        "name": "Dr. Renee Josario",
        "role": "Dr. Chontel's team leader, out of town at a conference while her stolen badge and her birth-year keycode walk a shadowrunner team into the lab",
        "archetype": "Corporate Scientist",
        "title": "Team leader and assistant to Dr. Chontel, Griffin Biotechnology",
        "race": "Human",
        "gender": "Female",
        "age": 35,
        "organization": "Griffin Biotechnology",
        "connection": 3,
        "description": (
            "Never seen: she is in Atlanta for the whole adventure and is, as far as she knows, "
            "having a good week. What the runners hold of her is a passcard with her photograph on "
            "one side and a swipe bar on the other, and a four-digit code that is her year of "
            "birth. She is senior enough to lead the team working most closely with Griffin's star "
            "researcher and social enough to go for drinks with her staff on the last evening "
            "before a trip, which is the only reason any of this worked."
        ),
        "background": (
            "One of Dr. Chontel's assistants and a team leader, born in 2029, promoted over Don "
            "Kukalakee, who considers himself the better neural-interface man and has never "
            "forgiven it. She is scheduled to attend a conference in Atlanta later in the week; "
            "Kukalakee timed his theft to it, took her out for drinks with coworkers on her last "
            "day, lifted the badge from her purse, and passed it on with her keycode and the "
            "warning that she would be back by the end of the week. His stated purpose in using her "
            "credentials rather than his own is to implicate her in whatever fallout follows the "
            "liberation of the research data: once Paladin makes use of it, Josario will probably "
            "be removed from her position, and he will be there."
        ),
        "notes": (
            "No statistics. The badge and code are the whole of the runners' access and the whole of "
            "the clock: once Josario returns and the badge is discovered missing it will be reported "
            "and locked out of the system, which is why Alex insists on 48 hours. The team is asked "
            "to leave the badge in Josario's office (second floor, room 11 on the handout map) after "
            "the run -- doing so completes the frame, and not doing so leaves the corporation "
            "hunting a lost card rather than a disloyal team leader. Runners who work out what is "
            "actually happening have a real choice here: an innocent woman is about to lose her "
            "career to a man who sold his employer to pay off a bookmaker, and returning the badge "
            "as instructed is the act that finishes her. Credential mechanics p.15: her passkey is "
            "rated as the highest maglock it is encoded to; keycards carry no biometric data at all, "
            "only the photo and the swipe bar, with everything else held in the security network, so "
            "a card alone fails at any palm-print lock."
        ),
        "contact_skills": ["Griffin neural-interface research teams"],
    },
    {
        "name": "Janus Koskey",
        "role": "Manager of Crusher 495, who knows everything worth knowing in Redmond and sells it",
        "archetype": "Fixer",
        "title": "Manager, Crusher 495",
        "race": "Ork",
        "gender": "Male",
        "connection": 3,
        "description": (
            "The man running the bar the Johnsons choose for neutral ground, and the top result on "
            "the adventure's own legwork ladder for the place: four or more successes gets a runner "
            "his name and the information that he 'knows everything worth knowing in Redmond, and "
            "sells information for a fee'. Managing an ork-owned Barrens venue that keeps humans, "
            "trolls and dwarfs drinking peacefully in the same room, through periodic Humanis "
            "drive-bys, is a qualification in itself."
        ),
        "background": (
            "Crusher 495 is owned and operated by a group of orks and is one of the few places in "
            "the Barrens where racial harmony genuinely prevails; Koskey manages it. Humanis "
            "Policlub occasionally likes to do a drive-by to try to scare off the metas, and it has "
            "never worked. Johnsons use the bar precisely because it is neutral, which means Koskey "
            "sees every meet that happens in his booths and has no obligation to any of the parties "
            "to them."
        ),
        "notes": (
            "No statistics; he never appears in a scene. He exists as a legwork prize and he is a "
            "very good one: a paid-for information broker sitting in the room where the runners are "
            "about to be hired, who will have watched Alex book the booth. A team that spends money "
            "on Koskey before the meet rather than after it can learn who their Johnson works for "
            "before they take the job, which is the one piece of intelligence the adventure "
            "otherwise withholds. He is also the obvious permanent Redmond contact to award from "
            "this adventure alongside Alex."
        ),
        "contact_skills": ["Redmond Barrens information brokerage", "Who met whom at Crusher 495", "Barrens meet spots and gang activity"],
    },
    {
        "name": "Zoe",
        "role": "The girl at Stuck's Carnival that Paladin's bought researcher has developed a taste for",
        "archetype": "Casino Worker",
        "title": "Stuck's Carnival, Auburn",
        "race": "Human",
        "gender": "Female",
        "connection": 2,
        "description": (
            "Named in a single clause: Don Kukalakee 'has since developed a taste for a girl there "
            "named Zoe'. The book gives her nothing else -- not a role in the casino, not an "
            "opinion, not a face. What it does give her is a position: she is the second reason a "
            "Griffin researcher keeps coming back to an Auburn casino two districts from his home "
            "and his work, and the person he sees on the nights when he wins."
        ),
        "background": (
            "Works at Stuck's Carnival, the Auburn casino Paladin steered Kukalakee towards so that "
            "he would not be doing business in his own backyard. When he wins he parties at the "
            "casino bar or restaurant 'or in more sordid ways' and blows it all immediately, "
            "starting the cycle again -- and Zoe is part of what he spends it on."
        ),
        "notes": (
            "No statistics and no scene. Recorded because she is named, has a place, and is the "
            "cheapest lever in the adventure that the adventure never picks up: the woman who sees "
            "Kukalakee on the good nights knows how much he wins, who pays him, and how often the "
            "same quiet man from Paladin is at the same table. A team investigating who really "
            "hired them, or building leverage on their own employer, gets further through Zoe than "
            "through the compound wall. She is also exposed -- if Paladin ever decides Kukalakee is "
            "a liability, she is standing next to him."
        ),
        "contact_skills": ["Stuck's Carnival regulars and who pays whom"],
    },
    {
        "name": "Dominic Woodhall",
        "role": "DocWagon Seattle's Chief Financial Officer, explaining the division's first record quarterly loss to a briefly panicking market",
        "archetype": "Corporate Executive",
        "title": "Chief Financial Officer, DocWagon Seattle",
        "race": "Human",
        "gender": "Male",
        "organization": "DocWagon",
        "connection": 3,
        "description": (
            "The voice DocWagon puts in front of the financial press when, for the first time, its "
            "Seattle division posts record losses for a quarter. His explanation is the corporate "
            "one and it is not quite a lie: the losses come from overextending the division in an "
            "attempt to expand market offerings. The losses can be absorbed without further damage "
            "to the division's financial stability, and the news is met with a momentary panic among "
            "shareholders anyway."
        ),
        "background": (
            "Chief Financial Officer of a division that has, in the space of a few months, had its "
            "clone and tissue vault robbed and burned, lost a wave of Platinum contracts to a "
            "competitor that did not exist last year, been publicly tied to the organlegging murder "
            "of two dozen SINless, and now watched the Griffin neurology research it was banking on "
            "vanish in what is reported as an unexpected system crash. He is the third named "
            "DocWagon Seattle officer of the arc, after CEO Garrett Walsh and the late COO Michael "
            "Davenport, and the one whose job it is to make the numbers survive the rest of them."
        ),
        "notes": (
            "No statistics; a screamsheet appearance only (SRM01-04B, KFIN). The article he anchors "
            "is the arc's scoreboard: DocWagon Seattle invested an undisclosed sum in Griffin, "
            "reported at last summer's annual shareholders' meeting, and the partnership has "
            "blossomed over the past year with DocWagon benefiting from Griffin's procedural "
            "improvements; DocWagon was depending on cashing in on Dr. Chantel's motor-neurology "
            "and epilepsy research and could not position itself once the data was lost; analysts "
            "believe the corporation banked on the new technology as a response to its recent "
            "contract losses, especially among Platinum subscribers, and that Rose Croix has made "
            "more than a dent. The closing line is the arc's own question: 'What started with the "
            "dramatic assassination of their COO at the last shareholders meeting, will DocWagon's "
            "latest string of bad luck motivate them to wake from their content slumber and meet "
            "their challenges head on?' A CFO with that quarter behind him is an excellent Johnson "
            "for whatever DocWagon does next."
        ),
        "contact_skills": ["DocWagon Seattle finances and investment positions"],
    },
    {
        "name": "Enigo Montoya",
        "role": "The shadowrunner who ends up with one of the first Ambidexterity Routers -- the adventure's stolen research, in a runner's arm, weeks later",
        "archetype": "Street Samurai",
        "title": "Shadowland handle \"Enigo Montoya\"",
        "gender": "Male",
        "connection": 2,
        "description": (
            "A voice on the board with a sword and no interest in the corporate politics everyone "
            "else is arguing about: 'I don't know who was behind it, but my fixer hooked me up with "
            "one of these new ambidexterity routers -- it hooked right into my wired reflexes, and "
            "now I can surprise my opponents by using my sword in either hand!' He is the only "
            "poster in the thread who is happy."
        ),
        "background": (
            "One of the first field-test subjects for the Ambidexterity Router, obtained through a "
            "fixer rather than through Paladin directly, weeks after the datasteal. That places him "
            "in exactly the position the runners themselves are offered at the end of this "
            "adventure: a wired shadowrunner carrying a first-generation custom prototype built "
            "from plans a corporation appropriated from a rival, on a corporation's field-test "
            "programme, whether or not he knows it is one."
        ),
        "notes": (
            "No statistics. Recorded because he is a named consequence rather than a commentator: "
            "the paydata the runners took off Dr. Chontel's stand-alone workstation is now inside "
            "another shadowrunner. Worth remembering that a damaged router gives a 1-in-6 chance of "
            "an epileptic seizure lasting 1D6 combat turns every time the wired reflexes fire, "
            "during which the subject cannot dodge, move or act -- somebody testing this device in "
            "the field with a sword is going to find that out. Also useful as the in-world proof "
            "that Paladin went to market fast, and as a lead for anyone trying to trace the "
            "technology back to the run."
        ),
        "contact_skills": ["Prototype cyberware on the street"],
    },
]

ORG_UPDATES = {
    "Griffin Biotechnology": {
        "notes_append": (
            "SRM 01-04 The Gambler (two or more weeks after the FORCEd Recon legwork): the compound "
            "is in full operation -- all personnel are onsite, the old downtown offices are shut, "
            "and every security measure is live, with some last-minute additions. Griffin has "
            "recently taken venture capital from investment firms including Ares Macrotechnology "
            "and DocWagon Seattle, which is what drew Paladin's attention in the first place: "
            "Fredericks wanted to know what an upstart could be developing that would attract heavy "
            "hitters like that. Legwork ladder p.9 (street doc, any corporate, any Everett contact, "
            "data broker, fixer, Mr. Johnson; Biotech / (Mega)corporate security / Data Brokerage / "
            "Everett corporations, TN 4): 0 'Yeah, they're turning metahumans into griffins.'; 1 a "
            "biotech firm with a new facility in Everett; 2 security drones on patrol but no rigger "
            "on duty; 3 no mages on duty but some spirits and maybe other passive magical "
            "protections, and they are on the verge of a major breakthrough; 4+ all their important "
            "data is on stand-alone workstations needing physical access, and Paladin is interested "
            "in it. PERSONNEL POLICY: the corporation is not blind to industrial espionage and has "
            "decided its people matter more than its secrets. Employees from the lowest janitor up "
            "are instructed to cooperate with captors and divulge what they know, then contact the "
            "corporation as soon as possible so arrangements can be made; passcodes and passkeys "
            "are not to be withheld. Mid-level managers, prominent scientists and doctors have "
            "basic Knight Errant resistance training and at least three dice against interrogation "
            "or intimidation (Interrogation [Resist Verbal]: 1 [3]) -- no help against magical truth "
            "detection -- and will play along while stalling, redirecting and misdirecting, "
            "confident the corporation will find and protect them; those with a Professional Rating "
            "hold out under physical torture until they have taken wounds commensurate with the "
            "rating. Only the highest staff and lead scientists get bodyguards, but most carry a "
            "PanicButton whose signal can be tracked by radio detection and ranging equipment, and "
            "a VIP taken without isolating every device brings four Knight Errant response teams "
            "with close air support. Staff are encouraged onto public transport and car/van pools, "
            "though most senior people drive their own vehicles and can be stopped between home and "
            "work. Killing captives brings the corporation's wrath; naturally healable damage is "
            "not considered foul play, but anything requiring cybernetic replacement or expensive "
            "healing or magic is -- Etiquette (Corporate) TN 2 to know it. THE LEAK: Don Kukalakee, "
            "a researcher passed over for promotion twice because his gambling addiction makes him "
            "a security risk, was bought by a Paladin agent over a few weeks of drinks and loans, "
            "and stole his own team leader's badge and keycode to sell. INTERNAL POLITICS worth "
            "keeping: Dr. Renee Josario leads the team working most closely with Dr. Chontel, "
            "Kukalakee believes the job should have been his, and the datasteal is designed to end "
            "her career. DISCREPANCY: the company is 'Griffin Biotech', 'Griffin Biotechnology' and "
            "'Griffin Biotechnologies' in the same book, and its lead researcher is 'Dr. Chontel' "
            "and 'Dr. Chantel' in the same book -- and 'Dr. Chandra Dasari' in SRM 01-01."
        ),
        "leadership_add": [
            {"name": "Dr. Renee Josario", "title": "Team leader and assistant to Dr. Chontel", "notes": "Her stolen badge and 2029 keycode are the runners' way in."},
            {"name": "Dr. Donald Kukalakee", "title": "Researcher, brain and cybernetic interface design", "notes": "Bought by Paladin; stole Josario's credentials to discredit her."},
        ],
        "enemies_add": ["Paladin Medical Technologies"],
    },
    "Paladin Medical Technologies": {
        "notes_append": (
            "SRM 01-04 The Gambler (Seattle, 2064): the Griffin datasteal, and Paladin's best "
            "operation of the arc. Fredericks noticed the sizeable investments DocWagon Seattle and "
            "Ares Macrotechnology had put into Griffin Biotechnology, started researching what "
            "could attract heavy hitters like that, and decided to keep tabs -- hiring "
            "shadowrunners to scope out the new Everett compound in case future incursions became "
            "necessary (SRM 00-03 FORCEd Recon) while other agents probed elsewhere. His operating "
            "principle: 'the weakest part of any organization was the people'. After weeks of "
            "canvassing nearby bars, one agent befriended the Griffin researcher Don Kukalakee, "
            "lent him money until he was bought, and took delivery of Dr. Renee Josario's ID badge "
            "and keycode. Paladin now pays Kukalakee's gambling debts and effectively pays him to "
            "gamble, at Stuck's Carnival in Auburn rather than in Everett. The run itself is put out "
            "through Alexandra 'Alex' Detwiler, a professional ork Johnson on Fredericks's staff: "
            "1,000 nuyen down, 10 percent of the paydata negotiable to 20, a 48-hour clock set by "
            "Josario's return, and absolute conditions of no bloodshed, no damage and no trace, "
            "because 'Ms. Johnson's sponsors have assets inside Griffin they do not want "
            "compromised at this time'. Paladin owns a beta-grade clinic Alex can open to runners "
            "who impress her, and wants the product of this run -- the Ambidexterity Router -- field "
            "tested and to market fast enough that it offers the prototype to the very team that "
            "stole the plans. Aftermath (handout): Shadowland's Bitrunner reports that 'Paladin "
            "Medical Services was behind the run -- they've had Griffin in their sights for the last "
            "year. As one of Griffin's chief rivals in the R&D field, Paladin needs to keep ahead', "
            "and Linei adds that Rose Croix may be opening negotiations with Paladin for the "
            "technology once field testing is complete. NAMING DISCREPANCY: this book calls the "
            "company 'Paladin Systems', 'Paladin Medical Services' and 'Paladin Biomedical' in "
            "different sections and makes Fredericks its 'president'; SRM 00-02 and SRM 01-01 use "
            "Paladin Medical Technologies with Fredericks as CEO, and that reading is kept."
        ),
        "leadership_add": [
            {"name": "Alexandra Detwiler", "title": "Ms. Johnson", "notes": "Professional ork Johnson; controls access to a Paladin beta clinic."},
        ],
        "enemies_add": ["Griffin Biotechnology"],
    },
    "Knight Errant Security Services": {
        "notes_append": (
            "SRM 01-04 The Gambler (Seattle, 2064): Knight Errant holds every security function at "
            "the Griffin Everett compound except the Security Director's post, which is a Griffin "
            "employee. SHIFTS: three eight-hour shifts starting at 7:00 AM with a fourth in "
            "rotation, callsigns Alpha, Bravo, Charlie and Delta -- four days on, one off, four "
            "swings (3 PM to 11 PM), one off, four mids (11 PM to 7 AM), then three days off, and "
            "the shift on its three-day break can be recalled as reinforcements when security is "
            "heightened. STRENGTH: 38 guards a shift -- one shift commander/corporate liaison, two "
            "at the main gate, three in the control room, four in the main lobby, four on each of "
            "the two floors and the basement, and two two-man teams patrolling each of four "
            "exterior quadrants (the handout report phrases the last as 'four patrolling in each "
            "exterior quadrant'; same headcount). External guards wear light security armour and "
            "matching helmets with low-light amplifiers and carry an AZ-150 stun baton, an Ares "
            "Predator II, an Ares Ravener SMG and two flash-bangs -- all Ares brand. Internal guards "
            "wear secure ultra-vests and secure clothing in KE uniform with a stun baton, pistol "
            "and flashlight; two of the four at the front entrance are equipped as externals. On an "
            "alarm every internal guard reports to the armory and refits. Roaming guards patrol in "
            "pairs, report by radio every ten minutes, know where every camera and sensor in their "
            "area is and sometimes report through the camera pickups, take a 15-minute break every "
            "three hours and stagger meals across the lunch hour; shift change covers the half hour "
            "either side of the hour. They arrive in a mix of private vehicles and Ares Citymaster "
            "troop transports; the shift commander drives an Ares corporate Ford Americar made "
            "exclusively for Ares. K-9: Knight Errant periodically supplies a barghest and handler "
            "patrolling within 20 metres of the building, on duty from the second morning after the "
            "meet -- a team that hits inside the first 36 hours misses them; a Knight Errant contact "
            "at TN 6 (+2 friend-of-a-friend) can say so, and the next scheduled patrol costs a "
            "minimum 2,000 nuyen bribe. GUARD BLOCK p.18: B5 Q6 S6 C3 I5 W5, Ess 0.9, Reaction "
            "5(9), Init 5+1d6 [9+3d6], Combat Pool 8, Karma Pool TR, Professional Rating "
            "4/Professional; smartlink, hearing damper, datajack, cybereyes (flare compensation, "
            "rangefinder, thermographic), headware radio with Comlink-IV and Crypto-3, Wired "
            "Reflexes 2; Assault Rifles 3, Pistols 5, Unarmed 3, Armed Combat (Club) 2 (4), "
            "Throwing 4, Launch Weapons (Launchers) 2 (4), SMG 5, Athletics 3, Stealth 4, Etiquette "
            "2, Intimidation 4, Interrogation 4, Electronics 3; KE Operational Procedures 4, "
            "Security Procedures 4, Shadowrunner Tactics 3; light security armour with helmet (7/6) "
            "or secure clothing with secure ultra vest (5/1); Ares Predator II (7M Stun, gel), Ares "
            "Ravener SMG (7M), AZ-150 stun baton (8S Stun), two flash-bangs (12S Stun, flash), "
            "security passcard, flashlight. Every guard at this site has at least two years with the "
            "company and combat experience, and most have seen action against shadowrunners "
            "elsewhere. K-9 HANDLER: as a regular guard plus Animal Handling 4. SHIFT SUPERVISOR "
            "and RAPID RESPONSE TEAM p.19, identical statistics: B5 Q6[8] S6[8] C4 I4 W5, Ess 0.4, "
            "Reaction 6(11), Init 11+3d6, Combat Pool 8, Karma Pool TR+2, Professional Rating 4; "
            "all-alpha smartlink, cyberears (hearing damper/amplification), datajack, cybereyes "
            "(flare compensation, rangefinder, thermographic), headware radio with Comlink-IV and "
            "Crypto-3, Wired Reflexes 2, Muscle Replacement 2; bioware Enhanced Articulation, "
            "Orthoskin 3, Trauma Damper; Assault Rifles 7, Pistols 5, Unarmed 4, Armed Combat "
            "(Club) 2 (4), Throwing 4, Heavy Weapons (Launchers) 2 (4), SMG 5, Athletics 3, Stealth "
            "4, Etiquette 2, Intimidation 4, Interrogation 4, Electronics 3, Leadership 4; KE "
            "Operational Procedures 6, Security Procedures 6, Shadowrunner Tactics 5. The response "
            "team differs only in kit: full heavy security armour with helmet (8/7), EnviroSeal, "
            "fire resistant (-4 to the Power of fire attacks); Ares Alpha Combat Gun (assault "
            "rifle, 42(c), SA/BF/FA, 8M, smartlinked, grenade link, Recoil 2) with offensive "
            "air-timed mini-grenades (10S). ARMORY on order: light security armour with helmet "
            "(7/6); Ares Predator II (9M); Ares Ravener SMG (7M, as HK-227); Ares Alpha Combat Gun "
            "(8M, smartlinked, grenade link, APDS standard) with offensive air-timed mini-grenades "
            "(10S) (CC p.22); Ares MP-LMG (7S, APDS standard) (CC p.26); Ares Raptor rocket "
            "launcher (as the Aztech Lasher) (CC p.27); Zapper Static Discharge Rocket (CC p.44, "
            "16D, Blast -10/m, Scatter 2d6, fence 1,250 nuyen); anti-vehicle rocket (16D, Blast "
            "-8/m, Scatter 2d6, fence 1,000 nuyen); APDS in pistol, SMG and assault rifle calibre; "
            "flash-bangs. DOCTRINE against distractions: the nearest team investigates while the "
            "shift supervisor deploys, some guards refit at the armory and others fall back to the "
            "building, and standard tactical procedure puts assets on the OPPOSITE side of the "
            "disturbance specifically to defeat distraction tactics. They observe by sensor rather "
            "than engage, feed intelligence to incoming backup, raise the Matrix security posture, "
            "and within minutes commit spirits and elementals -- some to the threat, some to hold "
            "the fort -- with an astral mage or two scouting and materialising before the shift "
            "supervisor to report. Containment, not battle, is the goal: keep the intruders "
            "fighting until backup arrives. Anyone captured 'will eventually find themselves in the "
            "Stuffer Shack parking lot'. AT THE GATE: Knight Errant has been told there are no "
            "expected deliveries or arrivals other than normal personnel and no surprise "
            "inspections (a real one would have the Security Director escorting it); requests get a "
            "stony stare and an instruction to move along. Magically dominating the gate guards "
            "fails on procedure -- the control room confirms every gate opening by radio and telecom, "
            "realises the guards are not in control of their own minds, sounds a silent alarm and "
            "redistributes the shift to capture and interrogate."
        ),
    },
    "DocWagon": {
        "notes_append": (
            "SRM 01-04 The Gambler (Seattle, 2064): the arc's bill arrives. DocWagon Seattle posts "
            "record losses for the second quarter -- the first time the division has done so -- and "
            "although they can be absorbed without further damage to its financial stability, the "
            "news is met with a momentary panic among shareholders. CFO Dominic Woodhall attributes "
            "them to overextending the division in an attempt to expand market offerings. The "
            "specifics: DocWagon invested an undisclosed sum in Griffin Biotechnology, reported at "
            "last summer's annual shareholders' meeting, and the partnership has blossomed over the "
            "past year with DocWagon benefiting from Griffin's medical procedural improvements; the "
            "division was depending on cashing in on Dr. Chantel's research into motor neurology and "
            "epilepsy -- a mechanism for the motor cortex that would control the irregular signals "
            "behind neurological disorders and, as a side benefit, let a subject direct motor-cortex "
            "impulses to the desired limb, granting ambidexterity -- and only days from testing the "
            "prototype all the critical research data was destroyed in 'an unexpected system crash'. "
            "Financial analysts believe DocWagon banked on the new technology in response to its "
            "recent losses of customer contracts, especially Platinum-level subscribers, and note "
            "that the appearance and growth of Rose Croix has made more than a dent in the "
            "division's operations. Shadowland's summary: DocWagon 'can handle a little dip, and "
            "this is exactly the wakeup call they need -- they've been operating basically "
            "uncontested in Seattle since the fall of CrashCart.'"
        ),
        "leadership_add": [
            {"name": "Dominic Woodhall", "title": "Chief Financial Officer, DocWagon Seattle", "notes": "Fronts the division's first record quarterly loss."},
        ],
    },
    "Ares Macrotechnology": {
        "notes_append": (
            "SRM 01-04 The Gambler (Seattle, 2064): Ares is one of the investment firms whose "
            "venture capital moved Griffin Biotechnology into the Everett compound, alongside "
            "DocWagon Seattle -- and it was precisely that pairing of heavy hitters that made "
            "Paladin's Dr. Fredericks start researching what Griffin could be developing. Ares "
            "presence at the site is total without being obvious: the Griffin Matrix architecture "
            "overview in the player handouts is marked 'Prepared by Ares Macrotechnology, Matrix "
            "Services Division, COMPANY CONFIDENTIAL'; the Knight Errant contract guards are armed "
            "entirely with Ares brand kit (Predator II, Ravener SMG, AZ-150 stun baton, Alpha "
            "Combat Gun, MP-LMG, Raptor launcher) and arrive in Ares Citymaster troop transports; "
            "the shift commander and Griffin's own Security Director both drive an Ares corporate "
            "Ford Americar made exclusively for Ares; and Ares private property adjoins the Griffin "
            "compound on the aerial reconnaissance photo. A runner walking that wall is inside an "
            "Ares supply chain from the gate lights to the security host."
        ),
    },
    "Humanis Policlub": {
        "notes_append": (
            "SRM 01-04 The Gambler (Seattle, 2064): Humanis occasionally likes to do a drive-by at "
            "Crusher 495, the ork-owned bar on the edge of Touristville, to try to scare off the "
            "metas. The legwork ladder's verdict, at three successes, is flat: 'Hasn't worked yet.' "
            "The bar remains the Barrens' most reliable neutral ground for Johnson meets, and the "
            "adventure keeps a racist attack in reserve as the consequence for runners who make "
            "trouble at the meet -- although the section it points the GM to does not exist (see "
            "the header note on the missing Extra Cards section)."
        ),
    },
    "Draco Foundation": {
        "notes_append": (
            "SRM 01-04 The Gambler (Seattle, 2064): the Draco Foundation's Everett complex still "
            "sits on the same wooded stretch of Marine Drive as the Griffin compound, and is item 3 "
            "on the aerial reconnaissance photograph the runners are given in their security "
            "package (SRM01-04B). No scene takes place there and the adventure never mentions it in "
            "the text, but any team planning an approach across the terrain is planning it between "
            "Draco Foundation and Ares private property, with the Brackhaus and Dohner estates and "
            "Puget Sound beyond."
        ),
    },
    "Mackie Construction": {
        "notes_append": (
            "SRM 01-04 The Gambler (Seattle, 2064): Mackie's files remain the only complete record "
            "of what is actually under the Griffin compound. The basement plan in the player "
            "handouts is annotated 'Note that areas 15-18 only appear on Mackie Construction files' "
            "-- the airlock and bridge to the Float Floor, the Float Floor itself (an inner section "
            "that floats above the foundation and is separated from the walls to minimise vibration "
            "and external effects), the microtech labs and cyberware assembly and prototyping "
            "rooms, and the main nanotech lab. Griffin's own drawings do not show them. Paladin's "
            "security package for this run does, which says something about where the package came "
            "from."
        ),
    },
    "Rose Croix": {
        "notes_append": (
            "SRM 01-04 The Gambler (Seattle, 2064): Rose Croix takes no part in this adventure and "
            "profits from it anyway. The KFIN piece on DocWagon Seattle's record quarterly losses "
            "names 'the appearance and growth of new rival Rose Croix' as having made more than a "
            "dent in the division's operations, on top of the Platinum contract losses of the "
            "previous three chapters. The Shadowland thread goes further: 'I've got some sources "
            "that mention Rose Croix may be opening negotiations with Paladin for the technology, "
            "once the field testing is completed' -- meaning Broward is preparing to buy the "
            "ambidexterity router that Paladin stole from the research DocWagon was banking on, "
            "which would, as another poster puts it, 'certainly give them a leg up on DocWagon'. "
            "Deacon Blues, who has called every previous move in this arc, closes the thread with a "
            "warning: 'Don't count out the Wagon too soon -- I still say that they're gonna come "
            "back, and when they do, Rose Croix is going to have to dance hard to stay in the "
            "game.'"
        ),
        "allies_add": ["Paladin Medical Technologies"],
    },
}

LOC_UPDATES = {
    "Griffin Biotechnology Everett Research Facility": {
        "notes_append": (
            "SRM 01-04 The Gambler -- the target of the run, two or more weeks after the FORCEd "
            "Recon legwork, with the security package the runners are handed now partly out of "
            "date. WHAT HAS CHANGED. Physical: additional funds bought monowire along the north "
            "perimeter wall, so three sides now carry it -- Perception (10) to spot, 10S damage, "
            "wired into the security system so that breaking the strand breaks a slight electrical "
            "circuit and raises the alarm; Electronics (5) with insulated cutters and an "
            "electronics toolkit bypasses it, and the monowire cannot be stolen from this facility. "
            "[Security Systems Technician contact, TN 6; +2 for friend-of-a-friend.] Technical: "
            "every external and internal sensor is now online and fully operational. [Electrician "
            "or Security Systems Technician, TN 4; +2 FOAF.] Matrix: no changes at all. Astral: the "
            "residual background count around the perimeter wall is gone -- the wall can still be "
            "seen astrally to have been raised from the earth itself by earth elementals, but "
            "nothing else about it is remarkable; and the inner walls, floors and ceilings of the "
            "labs and sensitive work areas have been lined with biofiber, Dr. Chontel's private lab "
            "included, whose windows are now covered with biofiber panels behind what still looks "
            "from outside like the same darkened plexiglass. [Any magically active contact or "
            "Security Systems Technician, TN 4; +2 FOAF.] (DISCREPANCY: the handout security report "
            "still lists a Background Count of 1 'everywhere inside the facility and three meters to "
            "either side of the main security wall'.) K-9: Knight Errant's barghest and handler are "
            "on the grounds, usually within 20 metres of the building, from 8 AM on the second day "
            "after the meet -- hit inside the first 36 hours and they are not there. [Knight Errant "
            "contact, TN 6; +2 FOAF; 2,000 nuyen minimum bribe for the next scheduled patrol.] "
            "Personnel: everyone is onsite, all staff except janitorial and maintenance work 8 AM "
            "to 6 PM Monday to Friday with occasional technical staff and researchers later and on "
            "Saturdays, and janitorial and maintenance work around the clock. The run falls on "
            "Wednesday and Thursday. BARGHEST p.18: B7 Q6x4 S5 I3/6 W3, Ess 6Z, Reaction 6, Init "
            "6+2d6, attack 9S, Professional Rating 3/Trained; Enhanced Senses (Sonar), Fear, "
            "Paralyzing Howl. An oversized solid black mastiff whose short flat fur gives the "
            "impression of naked hide, with spines the length of its back, red eyes and teeth that "
            "glow faintly from luminescent bacteria in its saliva; dual natured, so its senses and "
            "powers work on the astral plane; the howl is an opposed Essence (Willpower) test and "
            "one net success paralyses. GETTING IN. Smooth talker: no deliveries or arrivals are "
            "expected other than normal personnel, there are no surprise inspections, previously "
            "successful covers such as school orientation trips and hiring interviews no longer "
            "work (no more tours, all positions filled), and questions get a stony stare -- but the "
            "same approach works much better once inside, because the systems are built to keep "
            "people out and anyone already in must belong. Stealth: the grounds are far easier than "
            "the building; the only normal ways in are the front doors, the loading dock and the "
            "emergency exits, two guarded and one alarmed, and only the common areas have no active "
            "systems during business hours. THE WEAK POINT, and the book calls it 'really the best "
            "way to infiltrate the facility': every external sensor, camera and device connects "
            "directly to slave nodes in the security system, so a team that gets quietly into the "
            "compound can place a dataline tap and hack the security computer far more easily than "
            "decking in from the public SAN, then modify the biometrics database, pull guard "
            "schedules and so on. Being spotted crossing the wall or the forest raises the silent "
            "alarm and gives the guards time to draw heavier weapons from the armory and call in "
            "Knight Errant backup. THE JOB: a stand-alone workstation in a small room off Dr. "
            "Chontel's private lab (second floor, room 6 on the handout map), holding the file "
            "tagged Project 27 -- 1,000 Mp per tier of the team, from 1,000 for Green to 6,000 for "
            "Prime. Access is Dr. Renee Josario's stolen passcard and her keycode, 2029, which is "
            "her birth year, and the badge is to be left in Josario's office (room 11) afterwards. "
            "MAPS (SRM01-04B). Aerial reconnaissance: 1 Puget Sound, 2 Brackhaven Estate (spelled "
            "Brackhaus elsewhere in the campaign), 3 Draco Foundation Complex, 4 Universal Omnitech "
            "private property, 5 Ares private property, 6 Stuffer Shack / BP Gas, 7 Dohner Estate, "
            "8 Entry / Guard Shack, 9 Main Facility, 10 Parking Areas / Helipad, with a yellow line "
            "marking the property border and stone wall. First floor: 1 Main Entrance, 2 Front "
            "Lobby / Stairs / Main Elevators, 3 Restrooms, 4 Basic Labs, 5 Loading Dock, 6 Snack "
            "Machines, 7 Break Area, 8 Administrative Offices, 9 Demonstration Labs, 10 Conference "
            "Room / Auditorium, 11 and 14 Freight Elevators, 12 Radiology Labs, 13 Tissue Culture "
            "Labs; A Main Electrical Closet, B Security Center, C Security Director, D Armory, E "
            "Sprinkler Control. Second floor: 1 Main Stairs / Glass Lobby / Elevators, 2 first-floor "
            "hallway into the hillside, 3 and 9 Conference Rooms, 4 and 12 Bio Labs, 5 Computer "
            "Center / Administrator's Office, 6 Dr. Chantel's Private Lab, 7 Dr. Chantel's Office, "
            "8 Senior Doctors' Offices, 10 Restrooms, 11 Director's Office, 13 Medical Equipment "
            "Storage, 14 Secure Labs; A Telecom closet, B Electrical closet. Basement: 1 Main "
            "Stairwell / Lobby Doors / Elevators, 2 Generators, 3 General Supplies and Storage, 4 "
            "Maintenance, 5 and 12 Restrooms (12 with showers), 6 Secure Labs, 7 Observation Rooms, "
            "8 Mechanical Fabrication Rooms, 9 Kitchen, 10 Operating Room (Beta Clinic), 11 "
            "Laundry, 13 Nurse's Station / Monitoring, 14 Recovery Rooms, 15 Airlock / Bridge to "
            "Float Floor, 16 the Float Floor itself (an inner section that floats above the "
            "foundation and is separated from the walls to minimise vibration and external "
            "effects), 17 Microtech Labs and Cyberware Assembly / Prototyping, 18 Main Nanotech "
            "Lab; A Electrical Closet, B Telecom Closet. Every hallway, wall, floor and ceiling of "
            "the basement is rigged for FAB dispensers; areas 15-18 appear only on Mackie "
            "Construction files; and all three basement wings are astrally warded past the main "
            "lobby. FULL SECURITY REPORT (SRM01-04B): 172nd Street off Marine Drive, Everett "
            "(Lynnwood neighbourhood, security class B); restricted terrain of hills and woods; a "
            "four-metre natural stone wall with some sections augmented with monowire; fire doors "
            "at the end of every hall and every major intersection; external walls of natural cut "
            "stone and heavy plexiglas, internal walls of ordinary drywall except sensitive areas, "
            "which are plascrete with reinforced rebar. HVAC in two systems -- the main one serving "
            "common areas, halls and offices, the secondary serving the labs and sensitive areas "
            "with an Airwall system (SOTA63 p.83) that sterilises the flow with UV light and "
            "special filters; both have choke points and filtration fans preventing anything larger "
            "than Body 1 from using them as an entryway (small animals such as squirrels may fit "
            "through some areas) and both carry the same detection as the doors. Power is "
            "three-phase with redundant crossover circuits; on a full loss, UPS batteries carry "
            "every computer, the internal security systems, the laboratory equipment and emergency "
            "lighting for five minutes, long enough to start auxiliary generators that run "
            "essential systems for up to six hours -- a window designed for systematic shutdown "
            "and/or defence. Astral: no spirits or watchers monitor the building, but wards protect "
            "various labs and research areas from scrying and astral intrusion -- astral barriers "
            "only, opaque in astral space -- and certain walls, collocated with security doors, are "
            "solid in astral space and hold tanks of Fat Bacteria that are pressure-sprayed into "
            "the surrounding walls, floor, ceiling and doors on an astral breach, with a second "
            "release of fluorescing bacteria into the hallways to help security find the intruder. "
            "Maglocks: external locks are active during non-business hours (7 PM to 8 AM) and take a "
            "card reader plus numeric keypad, with access rosters determining which cards and PINs "
            "work where and when; internal offices and low-security areas are keycard only; labs "
            "and high-security areas add the keypad; and the most secure areas -- the subterranean "
            "labs, the armory and other sensitive rooms -- add retinal scan on locks of the highest "
            "calibre. Lighting is exceptional: high-powered daylight halogen at the main gate, along "
            "the main drive, across the front of the facility and in the parking area, with "
            "standard fluorescent inside. Cameras sit visibly on posts at the gate and along the "
            "drive, hidden among artificial trees and boulders in the woods and the terrain behind "
            "the building, and in unobtrusive black ceiling globes inside; all have a 120-degree "
            "field, normal spectrum, low light, thermographic, 5x variable zoom and normal-range "
            "audio pickup, with interior cameras at major intersections and common areas rotating "
            "for a full 360 in 120-degree increments, behind black ballistic polymer covers. Sensor "
            "grids of pressure pads (triggering over 30 kg, to ignore small animals) and UV laser "
            "grids strung between artificial trees focus the operator's attention; inside they "
            "exist only in sensitive areas and are armed only after hours. Ultrasound sensors near "
            "the building pick up invisible intruders on the grounds, and are used in sensitive "
            "interior areas after hours as well. The main doors and the entrances to high-security "
            "areas such as the nanolabs, and the HVAC intakes, carry passive magnetic anomaly "
            "detectors for weapons and cyberware plus chemical sniffers for explosives, gunpowder "
            "and other dangerous chemicals or gases, scanning both entering and exiting."
        ),
    },
    "Marine Drive Stuffer Shack and BP Gas Station": {
        "notes_append": (
            "SRM 01-04 The Gambler (Seattle, 2064): still the dumping ground. Runners captured "
            "inside the Griffin compound -- which is where a failed distraction attempt ends, once "
            "the containment doctrine has held them in place long enough for Knight Errant's backup "
            "to arrive -- 'will eventually find themselves in the Stuffer Shack parking lot', drugged "
            "and relieved of anything worth keeping, exactly as in SRM 00-03. It is item 6 on the "
            "aerial reconnaissance photograph in the runners' own security package, which means "
            "they are looking at where they will wake up before they ever cross the wall."
        ),
    },
}

NPC_UPDATES = {
    "Dr. Indira Chontel": {
        "description_append": (
            "SRM 01-04 The Gambler: still never seen. What the runners deal with is her room -- a "
            "private lab on the second floor whose walls, floor and ceiling have now been lined "
            "with biofiber and whose windows have been covered with biofiber panels behind the same "
            "darkened plexiglass, so that from outside nothing has changed and from astral space "
            "the room has gone dark. The workstation the whole adventure turns on stands in a small "
            "room off it, stand-alone and unnetworked, holding a file tagged Project 27."
        ),
        "background_append": (
            "SRM 01-04 The Gambler: the KFIN screamsheet describes what she was days away from. "
            "DocWagon Seattle was depending on cashing in on 'rising star Dr. Chantel's research "
            "into motor neurology and epilepsy'; sources indicate she was close to developing a "
            "mechanism for the motor cortex that would control the irregular signals associated "
            "with neurological disorders such as epilepsy, and that as a side benefit a subject "
            "would be able to control the impulses from the motor cortex and direct them to the "
            "desired limb, granting ambidexterity. She is Griffin's 'latest cash cow' in "
            "Fredericks's phrasing, and Dr. Renee Josario leads the team that works most closely "
            "with her -- the job Don Kukalakee believes should have been his."
        ),
        "notes_append": (
            "SRM 01-04 The Gambler: Chontel's research is the paydata. The file is tagged Project "
            "27 and sized 1,000 Mp per tier of the team; the book calls its content "
            "'inconsequential' from the players' point of view, which is a lie the handouts "
            "immediately correct -- Paladin turns it into the Ambidexterity Router, a prototype "
            "wired-reflex option giving six points of the Ambidexterity Edge, and starts field "
            "testing it within weeks. Aftermath: only days from testing her own prototype, all of "
            "her critical research data is announced destroyed in 'an unexpected system crash', "
            "DocWagon cannot position itself to leverage the technology, and the Seattle division "
            "posts its first record quarterly loss. NAMING: this book prints 'Dr. Chontel' in the "
            "plot synopsis and the hire text and 'Dr. Chantel' in the paydata paragraph, on both "
            "floor maps and throughout the KFIN article. ARC DISCREPANCY: SRM 01-01 Double Cross "
            "gives the identical research, the identical role as Griffin's lead neurology "
            "researcher and the identical announcement at the DocWagon shareholders' meeting to "
            "Dr. Chandra Dasari. Both rows are kept and cross-referenced rather than merged."
        ),
    },
    "Dr. Chandra Dasari": {
        "notes_append": (
            "SRM 01-04 The Gambler -- ARC DISCREPANCY, recorded here rather than resolved. This "
            "book and SRM 00-03 FORCEd Recon give Griffin Biotechnology's lead neurology researcher "
            "as Dr. Indira Chontel, and the KFIN screamsheet in SRM01-04B confirms it is the same "
            "post, the same research (motor neurology and epilepsy, with a motor-cortex mechanism "
            "whose side benefit is ambidexterity) and the same DocWagon shareholders' meeting "
            "announcement that SRM 01-01 Double Cross attributes to Dr. Chandra Dasari. Earlier "
            "books are canon and this row stands as written; treat the two either as one scientist "
            "the campaign renamed between chapters, or -- if a GM prefers a reading that costs "
            "nothing -- as two members of the same programme, with Dasari the public face DocWagon "
            "introduced at the meeting and Chontel the researcher whose stand-alone workstation "
            "Paladin robbed. Either way, everything that happens to Chontel's research in The "
            "Gambler happens to Dasari's."
        ),
    },
    "Rebecca Owls-Breath": {
        "description_append": (
            "SRM 01-04 The Gambler: the exception in a building full of contract guards, and the "
            "reason a Knight Errant gate guard can say with confidence that no inspection is "
            "genuine unless she is escorting it. She drives an Ares-issued Ford Americar like the "
            "shift commander, and she is the only member of Griffin's staff at this site with any "
            "combat or defensive skill whatsoever."
        ),
        "notes_append": (
            "SRM 01-04 The Gambler, stats p.17: B4(6) Q5(6) S5(6) C4 I4(6) W5, Ess 0.6, Magic 0, "
            "Reaction 5(14), Init 5(14)+1d6 (4d6), Combat Pool 9, Karma Pool TR+4, Professional "
            "Rating 4/Professional. ALL cyberware is DELTA grade: smartlink, hearing damper "
            "modification, datajack, Wired Reflexes 3, Reaction Enhancer (+2), Muscle Replacement "
            "1, Dermal Plating 2, Encephalon 2, headware radio with Comlink-IV and Crypto-3, "
            "Tactical Computer 1. Bioware: Cerebral Booster 2, Enhanced Articulation. Skills: "
            "Assault Rifles 5, Shotguns 5, Unarmed Combat 6, Athletics 3, Stealth 4, Etiquette 2, "
            "Intimidation 4, Electronics 3, Computers 3, Biotech 3; Security Procedures 6, "
            "Shadowrun Tactics 5. Armour jacket (5/3). Enfield AS-7 shotgun (Concealability 3, Ammo "
            "10(c), SA/BF, 8S) with an internal smartgun system and four clips of slug ammunition, "
            "2,000 nuyen value. Note what delta-grade Wired Reflexes 3 with a Reaction Enhancer "
            "means at a table that expected a corporate administrator: Initiative 14 + 4d6, faster "
            "than anything Knight Errant fields on the site. The Security Director's post is the "
            "one security function Griffin has kept for itself, and her office is room C on the "
            "first-floor map, beside the Security Center and the armory."
        ),
    },
    "Dr. Fredericks": {
        "description_append": (
            "SRM 01-04 The Gambler: a content sigh, the rich flavour of brandy and its aroma "
            "wafting up from a crystal tumbler, and a man savouring the thing he likes best in the "
            "world, which is being right about something after months of careful planning and a few "
            "calculated risks. He talks about his own operations the way his agent's mark talks "
            "about horses: 'He was just like Kukalakee, but of course gambled on a bigger scale. He "
            "had opened with the shadowrun to evaluate Griffin's new facility in case an opportunity "
            "arose, and then he filled his inside straight with Don, the perfect blend of greed, a "
            "gambling addiction, a little ambition, and questionable morals.' His only remaining "
            "risk, as he sees it, is that it is a setup and that the operation can be traced back "
            "to him and Paladin. He puts the tumbler down, opens the wall safe, takes out the large "
            "packet of data from the previous operations, and calls a specialist on his staff."
        ),
        "background_append": (
            "SRM 01-04 The Gambler: the origin of the whole scheme. Griffin Biotechnology, an "
            "upstart firm, had recently taken sizeable investments from companies such as DocWagon "
            "Seattle and Ares Macrotechnology; that intrigued Fredericks, who immediately started "
            "researching what Griffin could be developing that would attract such heavy hitters. "
            "His instincts told him to keep tabs, so he hired shadowrunners to scope out the new "
            "Everett facility in case future incursions became necessary and put other agents to "
            "work on the company. His operating principle is stated outright: 'the weakest part of "
            "any organization was the people, and Griffin was no different'. It took a few weeks of "
            "canvassing nearby bars before one of his agents befriended Don Kukalakee, and a few "
            "more before Kukalakee owed him a great deal of money and was a bought man who did not "
            "seem to mind. Kukalakee eventually made the offer himself. It was, as the saying goes, "
            "a deal Fredericks could not refuse."
        ),
        "notes_append": (
            "SRM 01-04 The Gambler: Fredericks never appears in play -- he is the opening fiction "
            "and the hand behind Alex. Note the title discrepancy: this book calls him 'the "
            "president of Paladin Biomedical' where SRM 00-02 and SRM 01-01 make him CEO of Paladin "
            "Medical Technologies. The through-line for a GM is that this is his third recorded "
            "operation and his first clean one: he had a rival's plant levelled in SRM 00-02, he is "
            "still solvent only on the strength of the UCAS defense contract in SRM 01-01, and here "
            "he lands a technology worth taking to market inside weeks -- with Rose Croix reportedly "
            "already opening negotiations for it. He is also, on the evidence of his own internal "
            "monologue, an addict of exactly Kukalakee's kind who happens to be playing for larger "
            "stakes, which is the joke the adventure's title is making."
        ),
        "contact_skills_add": ["Corporate intelligence on Seattle biotech rivals"],
    },
    "Michael Davenport": {
        "notes_append": (
            "SRM 01-04 The Gambler: Broward is offstage for the whole adventure and the arc summary "
            "is restated -- the two hired teams, the Caribbean surgery, the vault raid that shifted "
            "'many of their Platinum contracts' to Rose Croix, the smaller runs since, and the "
            "organlegging footage that dropped into Rose Croix's lap. What is new is the "
            "opportunity: with Griffin's motor-neurology research stolen by Paladin and DocWagon "
            "unable to leverage the technology it was banking on, Shadowland reports that 'Rose "
            "Croix may be opening negotiations with Paladin for the technology, once the field "
            "testing is completed', which would give it a further leg up on DocWagon. Broward's "
            "chess match is now being advanced by a corporation he is not paying."
        ),
    },
}

TAG_EXISTING = {}

MATRIX_HOSTS = """
The Gambler prints no security codes or sheafs of its own -- the adventure states flatly that "there
has been no changes or updates to the matrix systems of the facility" since SRM 00-03 FORCEd Recon,
which the GM is told to have on hand. What the player handouts do supply is the architecture, on a
sheet marked "Griffin Biotechnology -- Matrix Architecture Overview -- COMPANY CONFIDENTIAL --
Prepared by Ares Macrotechnology, Matrix Services Division". Four systems, deliberately not
interconnected, so that any one of them can be shut down for maintenance or to stop an intrusion
while the rest keep running.

| Network | Function | Connections and defences |
|---|---|---|
| **Communications** | The corporate Matrix presence (public web site), email and telecom, plus pattern recognition and control software that analyses and routes data packets by content | The ONLY system with a standard SAN to the Matrix. Every inbound stream is inspected for viruses, smart frames, persona programs and other illegal traffic; telecom passes through to recipients on the main network, email is held in the data store and read from the main network. A decker crossing to the main network through the internal SAN must first evade the program's Sensor rating, then the node's Access rating |
| **Logistics** | The facility's nerve centre: housekeeping and gardening drones, HVAC, lighting, elevator control, fire suppression, sprinklers and the PanicButton system | One-way outbound link to communications, dedicated to the PanicButton, on a deadman's switch that constantly transmits status packets to the Matrix -- shutting down EITHER network cuts the feed and immediately triggers an alarm. The security network can override most of its functions |
| **Main** | All processing for the labs, offices and research areas | Not connected to the Matrix directly; research data and reports route out through communications. Decking in from outside means two SANs, the second of which passes only telecom, email and data directly requested by an internal user |
| **Security** | All security hardware inside and out | Overrides most logistics functions. Includes a smart frame that analyses the patterns coming off the cameras and sensors |

**The hole in it** (p.12, and the book's own recommendation): all of the external sensors, cameras
and other devices are wired directly to slave nodes in the security system. A team that stealths
into the compound can place a dataline tap and hack the security computer from there -- much easier
than decking in from the public SAN -- and once inside it can modify the biometrics database, read
guard schedules, and open the way for everyone else. "This is really the best way to infiltrate the
facility."

**Not on any host**: the target itself. The paydata is a file tagged Project 27, 1,000 Mp per tier
of the team, on a STAND-ALONE workstation in a small room off Dr. Chontel's private lab, with no
network connection at all -- which is why this is a physical infiltration and why a decker, though
useful, is explicitly not required. If nobody on the team has Computer skill, Alex supplies a
pocket-secretary-sized device that downloads the file by itself once it is hooked to the machine.
Ratings for all four networks: see SRM 00-03 FORCEd Recon.
"""

NOT_BUILT = """
- **The Beta Clinic operating room in Griffin's own basement** (room 10 on the basement map), the
  **Float Floor**, the **microtech and cyberware prototyping rooms** and the **main nanotech lab** --
  all recorded on the Griffin Biotechnology Everett Research Facility row. Areas 15-18 appear only on
  Mackie Construction files.
- **The Knight Errant guards, K-9 handlers, shift supervisor and rapid response teams**, the
  **barghest**, and the **armory upgrade list** -- stat blocks on the Knight Errant Security Services
  and facility rows.
- **Alex's ork bodyguard** at the payoff, the **Crusher 495 bouncers**, the **Paladin agent** who
  spent weeks befriending Kukalakee in bars, and the **shadowrunners Fredericks hired for the
  original reconnaissance** (the SRM 00-03 team, which may well be the same player characters) --
  unnamed roles.
- **Griffin's scientists, lab technicians, administrative staff, computer technicians, janitorial
  and maintenance staff** -- the corporation's capture-and-cooperate policy and the resistance
  training given to managers and senior scientists are on the Griffin Biotechnology row.
- **"Hank the Troll" and "Mary the Elf"** -- rhetorical examples in the Duplicating Credentials
  section, not characters.
- **Saratoga** (the racetrack in Don Kukalakee's simfeed) and the **Atlanta conference** Josario
  attends -- place-names only.
- The Shadowland posters on the handout other than Enigo Montoya -- **The Chromed Accountant**,
  **OurTeam**, **Bitrunner**, **Linei** and **Deacon Blues** -- board handles with no face; their
  claims are recorded on the DocWagon, Paladin and Rose Croix rows.
- **The Extra Cards section** and its racist attack encounter, which The Hire tells the GM to turn
  to and which does not exist anywhere in the adventure or the playing aids. A GM who needs it can
  use the Humanis drive-by from the Crusher 495 legwork ladder.
"""

PLAY_NOTES = """
- The book says outright that this is not a traditional Shadowrun adventure: most of the legwork has
  already been handed to the players, so the whole session is planning and execution. Read the
  facility material to know where things are rather than to memorise it, and expect to be answering
  questions from it all evening. Have SRM 00-03 FORCEd Recon open beside you for the Matrix ratings
  and anything this book does not restate.
- The real test is not the wall, it is whether the team trusts a free intelligence package. Paladin's
  data is two weeks stale and four things have changed: monowire on the north wall, every sensor
  live, biofiber lining the labs and Chontel's windows, and a barghest on the grounds from 8 AM on
  day two. Each is discoverable through a named contact type at a stated target number. A team that
  spends part of its forty-eight hours checking is rewarded; a team that does not walks into a dog
  that can see it astrally.
- Time the run and the barghest is simply absent. Anything inside the first 36 hours misses the K-9
  patrol entirely -- which is worth letting a clever team work out rather than telling them.
- Steer towards the dataline tap. All external sensors and cameras run into slave nodes, so getting
  quietly onto the grounds and tapping the line gives a decker the security computer, the biometrics
  database and the guard schedules for far less risk than the public SAN. The book calls it the best
  way in and it is.
- Distractions do not work here and should be allowed to fail informatively. Knight Errant deploys to
  the OPPOSITE side of a disturbance on purpose, observes by sensor instead of engaging, and plays
  for containment until backup and elementals arrive. Runners who grab and go can still get out;
  runners who dig in get captured and wake up in the Stuffer Shack car park.
- The no-bloodshed condition is the adventure and the Karma table enforces it: 1 for killing only in
  self defence or 2 for killing nobody, plus 1 for minimal exposure or 2 for a perfect run with no
  evidence whatsoever. Maximum 4 from the adventure, never more than 6 with personal Karma.
- Ms. Johnson is a professional and expects professionals. She offers a real opportunity, a target
  the team may already have scouted, and follow-on work. If the players grind the negotiation, have
  her stand up, insult their professionalism, mention the work they just lost and walk. Her
  Negotiation is 3 + tier. Her prejudice against visibly modified runners is written in and is
  playable as an obstacle, not a joke -- and it is a reason for a face to do the talking.
- Employees are not obstacles. Griffin policy is to cooperate with captors, so a captured wageslave
  hands over passcodes and passkeys and then reports the incident, and a keycard alone is nearly
  useless because it holds no biometric data and the security network has to be told to honour a
  forgery. Killing them costs the team Notoriety and a note on the log sheet, and the corporation's
  wrath is triggered specifically by damage that natural healing cannot fix.
- Leave the badge in Josario's office as instructed and the team completes the frame on an innocent
  team leader who will probably lose her position. Nothing in the adventure asks the players to
  notice this. Let them notice it if they do, and let it cost them nothing mechanically -- the
  interesting version of this scene is the one where they realise on the way out.
- Rewards beyond the cash: Alex as a Level 1 Contact for teams that were effective, creative or
  professional, which carries three uses of a Paladin beta clinic (Etiquette (6), four successes,
  -1 TN per 5,000 nuyen gifted), and the one-time offer to field test the Ambidexterity Router for
  any character with wired reflexes and 0.5 Essence remaining. Alphaware only, matched to the
  existing wired grade, and a damaged unit means a 1-in-6 chance of seizure every time the reflexes
  fire.
- Arc hooks to plant: Kukalakee, who is about to discover how deep Paladin's hooks are; Josario,
  ruined by proxy; Janus Koskey, who saw the meet and sells what he sees; Zoe, standing next to a
  liability; and Deacon Blues's warning that DocWagon is going to come back and that Rose Croix will
  have to dance hard to stay in the game.
"""
