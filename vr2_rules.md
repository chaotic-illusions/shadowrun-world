# Virtual Realities 2.0 -- Rules Reference

> Shadowrun 2nd Edition sourcebook. This document contains all mechanical rules extracted from the specified page ranges for use by an AI agent building Matrix-rules-aware applications.

---

## Table of Contents

1. [Matrix Overview](#matrix-overview)
2. [Grids and Hosts](#grids-and-hosts)
3. [Intrusion Countermeasures (IC)](#intrusion-countermeasures-ic)
4. [Mapping Matrices and Security Sheaves](#mapping-matrices-and-security-sheaves)
5. [Deckers](#deckers)
6. [Cyberdecks](#cyberdecks)
7. [Programs](#programs)
8. [System Operations](#system-operations)
9. [Cybercombat](#cybercombat)
10. [Reference Tables](#reference-tables)
11. [Matrix Hot Spots](#matrix-hot-spots)

---

## Matrix Overview

### ASIST and the Matrix

The Matrix is accessed via ASIST (Artificial Sensory Induction SysTem) technology, which creates a full direct neural interface (DNI) between the decker and the Matrix. The decker's physical body remains in the real world; only the persona travels through cyberspace.

Persona programs running on the cyberdeck are downloaded as "server-side" versions into the Matrix when the decker logs on. Two program sets exist simultaneously:
- **Front-end programs** on the deck: convert the decker's neural impulses into computer commands.
- **Server programs** in the Matrix: convert those commands into programming instructions that influence what the system does.

If the server programs crash (the persona is crashed), the decker is **dumped** offline.

### System Ratings (ACIFS)

Every grid and host has a **Security Code** (color), **Security Value** (number) and five **Subsystem Ratings**. The shorthand format is:

```
Security Code - Security Value / Access / Control / Index / Files / Slave
```

**Example:** `Red-6/10/12/10/9/9` (simplified) or `Red-6/10/12/9` (with Index/Files/Slave averaged).

The acronym **ACIFS** covers the five subsystems:

| Subsystem | Function |
|-----------|----------|
| **Access** | Resists unauthorized log-on attempts. Target number for Access Tests. |
| **Control** | Resists unauthorized manipulation of host functions. |
| **Index** | Resists unauthorized searches for data addresses and file locations. |
| **Files** | Resists unauthorized reading, writing, editing, or deleting of data files. |
| **Slave** | Resists unauthorized control of remote devices connected to the host. |

High subsystem ratings do not impede **authorized** users -- they only affect unauthorized (decker) attempts.

#### Security Codes

| Code | Security Value Range | Description |
|------|---------------------|-------------|
| Blue | Any | Little or no security. Public databases, small businesses. |
| Green | Any | Moderate security. Resists casual intruders. |
| Orange | Any | Significant security. Includes killer IC. Sensitive corporate or government data. |
| Red | Any | Maximum security. Killer defenses. Top-secret or high-value data. |
| Black | Any | Extremely rare. Qualitatively different cyberspace. Only accessible by hot decks. |

Double-digit Security Values represent extreme security.

#### Control Rating

The **Control Rating** measures how much attention a system pays to rogue programs. An unauthorized decker accessing a grid must succeed on a **Control Test** (Computer Skill vs. Control Rating) to avoid detection each time they interact with the grid.

#### Slave Rating

Governs operation of remote devices. A successful Slave Test lets an unauthorized decker take control of devices such as security cameras, elevators, and automated machinery.  (In the ACI condensed rules, this falls under Index tests)

### Deck Ratings (MPCP/BEMS)

The power of a decker's persona is defined by:
- **MPCP Rating** (Master Persona Control Program): Central operating system of the deck. Measures the deck's ability to take damage and continue functioning. Serves as the cap for other program ratings.
- **BEMS** (Bod, Evasion, Masking, Sensor): The four persona programs. These are the decker's "attributes" in the Matrix.

**MPCP constraints:**
- Total of all four persona programs (Bod + Evasion + Masking + Sensor) cannot exceed **MPCP Rating x 3**.
- No single Persona Rating may exceed the MPCP Rating.
- Maximum rating for most utility programs equals the MPCP Rating.

**Deck shorthand format:**
```
MPCP Rating / Bod / Evasion / Masking / Sensor
```

**Example:** `MPCP-8/6/6/6/6` (total persona = 24, maximum for MPCP-8 = 24).

If Evasion is increased by 2 points (to max of 8), reduce other persona programs by 2:
`MPCP-8/8/5/6/5`

### Detection Factor

The **Detection Factor** is the target number the gamemaster uses when making tests to detect the decker's presence or prevent the decker from performing actions in the Matrix.

**Formula:**
```
Detection Factor = Average (round up) of Masking Rating and Sleaze utility rating
```

If no Sleaze utility is running:
```
Detection Factor = Masking Rating / 2 (round up)
```

**Example:** MPCP-8/8/4/6/6 deck running Sleaze-8: Detection Factor = (6 + 8) / 2 = 7.

### Hacking Pool

The Hacking Pool provides bonus dice for Matrix tests.

**Formula:**
```
Hacking Pool = (Intelligence + MPCP Rating) / 3, round down
```

Any increase to Intelligence (from cyberware, bioware, etc.) also increases the Hacking Pool.

**Hacking Pool dice may be added to:**
- System Tests
- Attack or defense tests
- Maneuver tests
- Programming tests
- Attribute tests

**Hacking Pool dice may NOT be added to:**
- Initiative rolls
- Doctrinal dice rolls (e.g., "roll 1D6 to see how long before host crashes")
- Body or Willpower tests to resist gray or black IC damage (only Karma Pool dice, cyberware, or bioware/magic boosts apply there)

#### Optional Rule: Multiple Improvements

Characters with cyberware or bioware that raises Intelligence may apply those increases to the Hacking Pool as well. The increases are cumulative unless the gamemaster opts to use this rule, in which case only the single largest increase to Intelligence counts.

### System Tests

Unauthorized deckers make a **System Test** for every task attempted in the Matrix. These are always **opposed tests**: decker vs. host/grid.

- **Decker's roll:** Computing skill dice. Target number = Subsystem Rating, modified by running utilities and situation modifiers.
- **Host/grid's roll:** Security Value dice. Target number = Decker's Detection Factor.

| Result | Outcome |
|--------|---------|
| Decker more successes | Task succeeds |
| Host more successes | Task fails |
| Tie | Task fails |

Regardless of outcome, the gamemaster records the host's successes and adds them to the running **security tally**.

### Security Tally

The security tally is a running total of all successes a host/grid accumulates against the decker across System Tests during a run. It persists as long as the decker is logged on to that host/grid.

When the tally reaches a gamemaster-set threshold, it triggers events: IC activation, alert escalation, or nothing. The decker never knows the threshold or how close the next trigger is.

---

## Grids and Hosts

### Grid Types

#### Regional Telecommunication Grids (RTG)

**This section removed as we will perform a different update to the LTG's/RTG's already in the shadowrun-world.db file.**

When generating ratings for public grids not listed, assume Easy Intrusion Difficulty and subtract 2 from all ratings (range 6-8).

#### Local Telecommunications Grids (LTG)

LTGs are the local "area codes" within an RTG. In North America, LTG ratings are usually equal to the parent RTG ratings.

**Optional Rule: Variable LTG Ratings**

Roll 1D6:
- 1-2: Reduce all LTG's basic System Ratings by 1.
- 3-4: Ratings unchanged.
- 5-6: Increase all LTG's System Ratings by 1.

#### Private LTGs (PLTG)

PLTGs are independent, restricted global grids owned by corporations or governments. They are closed to the public. Key rules:

- PLTGs are stable; their System Ratings do not vary.
- A security tally built up on an RTG **follows the decker into a PLTG** (PLTGs pick up security "flags" from RTGs).
- If the tally is high enough to trigger IC when the decker logs on to the PLTG, that IC activates immediately upon log-on.
- Gamemasters should assign Orange or Red security codes and Easy Intrusion Difficulty to PLTGs.
- Most megacorps maintain at least one PLTG. Most developed countries maintain several government PLTGs.

**PLTG Regulations:** Anti-PLTG regulations exist in Pueblo, Ute, Sioux Nation, Tir Tairngire, Aztlan, Tir na nOg, Israel, Japan, the Confederated Azanian Nations (outside Trans-Swazi Federation), and some strong African states and megacorp-owned ministates.

### Jackpoints

Jackpoints are the physical connections deckers use to access the Matrix. Each type has three values:

| Type | Trace Factor | Access Modifier | Base Bandwidth |
|------|-------------|-----------------|---------------|
| Legal Access | -2 | -2 | 20 Mp |
| Illegal Access | +0 | +0 | 20 Mp |
| Satellite Uplink | (varies.  Reference Satlink Target Numbers) | +2 | 50 Mp |
| Workstation | -4 | -4 | 50 Mp |
| Remote Device | +4 | +4 | 20 Mp |
| Console Access | -6 | See text | Unlimited |

- **Trace Factor**: Applied for the entire run. Lower = trace IC can locate the jackpoint more easily.
- **Access modifier**: Applied to all the decker's Access Tests during the run.
- **Base Bandwidth**: Maximum bandwidth accepted without further reducing Trace Factor.

**Console Access:** Halve the opposing system's Access Rating and Security Value for all Access Tests. No bandwidth penalty. Requires physical access to the machine room.

**Satellite Uplink:** Partial immunity to Trace IC -- the IC can locate the satellite jackpoint but cannot pinpoint the decker's physical location. Also reduces Reaction by -2 due to signal lag.

**Bandwidth Trace Modifier (optional):**
```
Modifier = (Decker's Bandwidth / Base Bandwidth, rounded down) x -1
```
Example: 78 Mp bandwidth, Base 20 Mp: modifier = -3 (78 / 20 = 3.9, rounded down to 3, x -1).

### Grid Security Tallies

- Switching LTGs **within the same RTG** does not reset the security tally.
- Switching to a **different RTG** does reset the tally.
- The tally **does** follow the decker from an RTG onto any PLTG accessed from that RTG.

### Satellite Links

To access the Matrix via satellite, the deck must have a satlink interface. Procedure:

1. Decker makes a **Computer Test** against a target number from the Satlink Target Number Table.
2. Base Time: 3 minutes.
3. Failure: decker must wait 5 minutes before trying again.

**Satlink Target Numbers:**

| Conditions | Target Number |
|------------|---------------|
| Open country, clear view of horizon | 2 |
| Open country, some obstruction | 3 |
| Open country, mountain or heavy forest | 4 |
| Suburban | 5 |
| Light Urban | 6 |
| Downtown Urban | 8 |
| Bad weather (more than overcast) | +2 modifier |

Satellites function as LTGs rated Orange-Average or Orange-Hard (no Subsystem Rating reduction). Military and private corporate comsats: Red-Hard.

From a satellite, a decker may perform a Logon to RTG operation to any RTG on Earth. Most near-earth orbit systems using that satellite for communications are also accessible.

### Hosts

Host systems are where the Sixth World processes its data. Each host has a **Security Code**, a **Security Value**, and five **Subsystem Ratings** (ACIFS).

#### Host Security Codes

| Code | Character |
|------|-----------|
| **Blue** | Public service databases, small businesses, free information. Minimal IC. |
| **Green** | Moderate protection. More active intent to resist intruders. May include IC. |
| **Orange** | Significant security including killer IC. Sensitive corporate/government data. |
| **Red** | Maximum security. Killer defenses. Top-secret data. |
| **Black** | Black/Ultraviolet. Extremely rare. Qualitatively different cyberspace. Hot decks only. |

#### Intrusion Difficulty

| Difficulty | Description | Security Value Range | Subsystem Rating Range |
|------------|-------------|---------------------|----------------------|
| Easy | Friendly to multiple users; high traffic | 4-6 | 8-10 |
| Average | Standard corporate or government system | 7-9 | 11-15 |
| Hard | High-security system | 8-12 | 13-18 |

**Random Host Rating Generation:**

Formula for Security Values:
- Easy: 1D3 + 3 -> final range 4-6
- Average: 1D3 + 6 -> final range 7-9
- Hard: 2D3 + 6 -> final range 8-12

Formulas for each Subsystem Rating:
- Easy: 1D3 + 7 -> final range 8-10
- Average: 2D3 + 9 -> final range 11-15
- Hard: base 1D6 + 12 -> final range 13-18

**Assigned Number Guidelines:**
- Final Target Number of 3 or less: trivial.
- Average system with a Computer-6 decker and decent Detection Factor: stiff opposition.
- Hard system likely defeats a starting decker without very good utilities.
- Deckers with skill 8+, Detection Factor 8-9, and utilities 8+ find Hard systems challenging but beatable.

**Optional Rule: Varying Subsystem Ratings**

Gamemasters may individually raise or lower Subsystem Ratings to give hosts distinct characters. For example, increasing the Access Rating by 2 for entry points on public grids makes the host harder to enter but not harder to work within.

### System Tricks

#### Bouncers

A bouncer host starts at low security and upgrades its Security Code when it detects an intrusion. Example: normally Green-4, transforms to Red-8 when security tally reaches a threshold. Takes 1 turn to make the upgrade.

When a decker triggers a bouncer, the gamemaster makes a Sensor Test (Security Value dice vs. target number). On any success, the decker notices the rating is rising but must perform an Analyze Host operation to determine the new security code and value.

High-sensitivity areas may function as automatic bouncers regardless of the tally.

#### Chokepoints

A chokepoint host exists solely to block unauthorized access to more sensitive systems. It generally has higher System Ratings than the hosts it protects. Smart deckers find alternate access paths to bypass the chokepoint.

#### Trap Doors

A trap door is a concealed comm port connecting one host to another (or to a PLTG) that is **not accessible via the Access subsystem**. A different subsystem -- such as Slave -- controls passage, making the door invisible to standard Access analysis.

**Using a Trap Door:**
1. Detect the port via an **Analyze Subsystem** operation on the concealing subsystem.
2. Perform a **Graceful Logoff** using the concealing subsystem's rating to exit through the trap door.
3. Perform a **Logon to Host** operation to enter the destination host on the other side.

Trap doors combined with chokepoints are especially dangerous -- the decker must navigate a hostile chokepoint environment to find the hidden exit.

#### Networks (Hub/Second-Tier Systems)

First-tier hub hosts function as traffic cops for the network. To travel between hosts in a network:
1. Make an **Analyze Subsystem** operation on the Access subsystem of the hub.
2. Perform a **Logon to Host** operation to the second-tier host.

Network-wide operations (Locate File, Locate Slave) can be performed from the hub.

#### Virtual Machines (VMs)

A VM is an emulated host running as a subprogram of a real host. Actions on the VM do not affect the actual host datastore. VMs can be used to camouflage a real system behind decoy data.

**VM System Ratings:** Maximum VM Security Code equals the native host's Security Code. VM Subsystem Ratings cannot exceed the native host's Subsystem Ratings minus 1.

**Breaking Out of a VM:**

Requires a **Control Test** against the native host's Security Rating (opposed). Number of successes needed to break out:
| VM Security Code | Successes Required |
|------------------|--------------------|
| Blue | 1 |
| Green | 2 |
| Orange | 3 |
| Red | 4 |
| Black | 5 |

If the decker gets successes but doesn't break out, add the shortfall to his security tally. Crashing a VM dumps the decker but does not crash the native host.

A decker can detect a VM with an Analyze Host operation.

#### Teleporting SANs

Some corporate PLTGs use access nodes that change their RTG/LTG addresses on a secret schedule. To exploit a teleporting SAN, a decker must either know the algorithm, use a frame with a Trigger utility to monitor for the SAN's appearance, or have an inside asset provide the schedule.

#### Vanishing SANs

Vanishing SANs open only at specific times. A decker must be ready to perform a Logon to Host operation before the SAN disappears. Typical window: a few seconds. The base time for the Logon Test equals 1D6 seconds.

#### Triggered SANs

Triggered SANs open only in response to specific actions elsewhere in the Matrix (e.g., Slave operations, database hits, satellite signals).

### Passcodes

Passcodes grant automatic success for specific tasks on a host. Any activity outside the passcode's authorization requires System Tests.

**Passcode Types:**
- **Simple passcode:** Symbol set entered at log-on.
- **Linked passcode:** Works in combination with the user's MPCP signature. A stolen linked passcode gives a -2 target number bonus for Logon to Host operations when the decker uses a Deception utility.
- **Passkey:** Locked to a specific chip installed on the user's terminal. A decker must steal or duplicate the key-chip. The key-chip algorithm is a 10 Mp program.

**Passcode Duration:**
- Most systems change passcodes quarterly. High-security systems: weekly. Most paranoid: time-based rolling codes (new code every log-on).
- Passcodes are deactivated immediately if the user triggers an active alert while logged in with that code.

**Authorization Levels:**
- Low: Read-only access to specified public files.
- Mid: Read/write access to most non-sensitive files. Important Slave operations require a test.
- High: Write access to sensitive files; read access to most secure files.
- Supervisor/Sysop: Nearly unlimited, including creating/deleting passcodes.

### Ultraviolet (UV) Hosts

UV hosts are qualitatively different from all other Matrix environments. Rules:
- Only **hot decks** can log on to UV hosts.
- The decker's persona transforms: Strength and Body equal Bod Rating; Quickness equals Evasion Rating; Mental Attributes equal the decker's own.
- Utility programs become physical tools, weapons, or armor.
- **Damage to the persona is direct damage to the decker's body** (Mental damage -> Mental Condition Monitor; Physical damage -> Physical Condition Monitor).
- Jacking out of a UV host: 12D Stun dump shock.
- UV hosts are currently rumored but not confirmed. Possibly at Denver Nexus, UCAS government, Tir na nOg, Zulu Nation, Zurich-Orbital, and Renraku Arcology.

---

## Intrusion Countermeasures (IC)

IC (Intrusion Countermeasures, pronounced "ice") programs defend Matrix systems against unauthorized access. They range from passive detection to lethal attacks.

### IC Ratings

Each IC program has its own **rating**:
- **Attack Tests:** The host makes Attack Tests using the host's **Security Value** as its "skill" (number of dice rolled).
- **IC Rating** = target number for the decker's Damage Resistance Tests and the Power of the damage the IC inflicts.
- **Damage Resistance for IC programs:** Use the host's Security Value as the number of dice.

### Locating IC

- **Proactive IC** is immediately visible when it activates -- it betrays itself through action.
- **Reactive IC** does not betray itself. To detect it, the gamemaster makes a secret **Sensor Test** vs. IC rating. On 0 successes, the decker is unaware. On 1 successes, the decker is informed their actions triggered IC. On 2 successes, the decker knows the IC type.  On 3+ successes, the Decker learns the IC's rating and location.

### Crashing IC

When a decker crashes IC in cybercombat, add the IC's rating to the decker's security tally.

**Utility Options for Crashing IC:**
If the decker uses a utility with the Stealth option to destroy IC, reduce the tally increase by the Stealth rating. Stealth-6+ eliminates the tally increase entirely.

### Suppressing IC

A decker can avoid the security tally penalty for crashing IC by **suppressing** it instead of destroying it. Suppression uses Detection Factor points:
- Reduce Detection Factor by 1 for each IC program suppressed.
- The decker must declare suppression immediately when crashing IC.
- To release suppressed IC: Free Action. Detection Factor is restored. Security tally increases by the appropriate amount for each released IC program.
- IC remains suppressed only as long as the decker is in the system.
- The Deckers Detection Factor cannot be less than 1.

### White IC

White IC affects only the decker's online icon. It cannot permanently damage the cyberdeck's ratings or utilities. Worst effects: dump the decker off the Matrix, or scramble data being read/written. On hot decks, white IC can cause slight physical simsense overload damage if the decker is dumped.

#### Cripplers

**Type:** Proactive

Attack one specific persona attribute (Bod, Evasion, Masking, or Sensor). Types: **Acid** (Bod), **Binder** (Evasion), **Jammer** (Sensor), **Marker** (Masking).

In cybercombat, a crippler makes an Attack Test. The targeted attribute is used as the decker's defense dice. If the crippler's successes exceed the decker's, reduce the targeted attribute by the difference divided by 2 and rounded down. The reduction remains in effect until the decker logs off.  Icon attributes cannot be reduced below 1.

#### Killer

**Type:** Proactive

Killer IC attacks decker icons in cybercombat. Power equals the IC's rating. Damage Level is based on the host's security code:

| Host Security Code | Damage Level |
|--------------------|-------------|
| Blue | (IC Rating)L |
| Green | (IC Rating)M |
| Orange | (IC Rating)M |
| Red | (IC Rating)S |
| Black | (IC Rating)S |

Stage damage up 1 level for every 2 successes on the host's Attack Test (same as standard combat staging).

If Killer IC fills the decker's Condition Monitor, the decker is **dumped**. Armor utility programs reduce the Power of Killer IC attacks. Killer IC does not permanently damage deck ratings or utilities -- it is classified as **White IC**.

#### Data Bomb

**Type:** Reactive

A data bomb is a booby trap attached to a specific datafile or Slave-subsystem device. It waits silently and does not interact with the security tally until triggered.

**Detecting:** Analyze Icon operation on the protected file or device.

**Defusing:**
- Make a **Computer Test** against the controlling subsystem rating minus the Defuse utility rating.
  - File bomb: **Files Rating - Defuse Rating** (target number)
  - Slave device bomb: **Slave Rating - Defuse Rating** (target number)
- Failed attempts leave the bomb primed (unless the decker rolls all 1s, which detonates it).
- Each attempt may add successes to the security tally via the opposed Security Test.
- Successful defuse does **not** count as crashing -- do not add the bomb's rating to the tally. Once defused, no suppression is needed.

**Triggering:** If the decker fails to defuse and then **succeeds** on a System Test to access the protected target, the bomb explodes. A failed access test does not trigger it.

**Explosion effects:**
- Hits the persona automatically for **(IC Rating)M** damage; icon resists normally.
- Armor utility programs reduce the Power.
- Adds the IC's rating to the security tally.
- Decker may spend 1 Detection Factor point to suppress the IC and avoid the tally increase.

#### Probe

**Type:** Reactive

Probe IC interrogates data packets and program requests. For every System Test the decker makes, the gamemaster makes a **Probe Test** (Probe Rating vs. Detection Factor). Add any successes to the security tally.

#### Scramble

**Type:** Reactive

Scramble IC protects specific elements of a host's Access, Files, or Slave subsystems. Can protect individual files, a datastore, or an entire subsystem. Two varieties:
- **Exploding:** Linked to a data bomb. If decrypted or crashed without defusing first: boom.
- **Poison:** Destroys the data it protects if the decker fails to defeat the IC. To defeat poison IC, the decker first must attempt to decrypt it.  If the decryption fails, the IC makes a Poison Test (IC rating vs. target number = Decker computer skill). Success destroys the data.

Decrypting scramble IC with the Decrypt utility does **not** add to the security tally. Using an attack program to crash it does add to the tally (unless suppressed).

#### Tar Baby

**Type:** Reactive

Tar baby IC attacks operational utilities used in System Tests (not passive utilities like armor or sleaze). Whenever the decker uses a trigger utility, the gamemaster makes an opposed test:
- **Tar Baby Test:** IC rating dice vs. utility program rating as target number.
- **Utility Test:** Utility rating dice vs. tar baby IC rating as target number.

If tar baby wins: both the IC and the utility crash. No security tally increase. The decker must reload the utility with a Swap Memory operation.

If the utility wins: the utility survives; the gamemaster makes a secret Sensor Test to see if the decker notices the IC.

Tar baby can be placed inside a construct, party IC cluster, or combined with trap IC.

**Note:** Tar baby is classified as White IC -- it does not permanently damage utility programs.

### Gray IC

Gray IC attacks the cyberdeck and its utilities directly. Damage is **permanent** -- it reduces deck ratings until chips are replaced.

#### Blaster

**Type:** Proactive

Fights like killer IC. Armor reduces damage. If blaster IC dumps a decker, make a **Blaster Test** (IC Rating vs. MPCP Rating; Hardening increases the target number). Reduce the MPCP Rating by 1 point for every 2 successes. The decker may need to reduce persona programs to stay within the new limit (total persona <= MPCP x 3).

#### Rippers

Gray version of cripplers. Types: **Acid-rip** (Bod), **Bind-rip** (Evasion), **Jam-rip** (Sensor), **Mark-rip** (Masking). Same attack sequence as cripplers, but whenever a ripper damages an icon, make a **Ripper Test** (IC Rating vs. MPCP Rating; Hardening increases target number). Reduce the targeted persona chip's Rating by 1 for each success. Replacing the persona chip is the only way to restore this damage.

#### Sparky

**Type:** Proactive

Fights like blaster IC. If sparky IC crashes the persona, it causes an overload in the deck's power supply:
1. Make a **Sparky Test** vs. MPCP Rating + 2 (Hardening increases TN). Reduce MPCP Rating by 1 for every 2 successes.
2. Sparky causes `(IC Rating)M` damage to the decker physically. Stage the damage up one level for every 2 successes on the Sparky Test.
3. The decker resists this damage normally (using physical Body attribute). Hardening reduces the Power.

#### Tar Pit

**Type:** Reactive

Operates like tar baby IC but if it trashes a utility, it also **injects viral code** that corrupts all copies of that program in active and storage memory. The decker loses the program for the rest of the run unless he has a backup in offline memory.

**Tar Pit Test:** IC Rating vs. MPCP Rating (Hardening increases TN). On no successes: same effect as tar baby; decker can reload. On any success: all copies corrupted.

#### Worms

**Type:** Reactive

Worms booby-trap subsystems. Any System Test against a worm-infested subsystem risks infecting the decker's MPCP.

**Worm Infection Test:** Security Value dice vs. MPCP Rating. On 1+ success: worm infects the MPCP. If the deck has Hardening, the test must produce successes **greater** than the Hardening rating to infect.

Once infected, the MPCP cannot be erased -- the chip must be replaced. Detection: Computer skill or B/R skill, Base Time 10 hours.

**Dataworm variant:** Logs run information. Each time an infected deck logs onto a grid, roll 1D6. On a 1, the dataworm tries to send a report. Sensor (8) Test for the decker; on failure, he doesn't notice.  If noticed, the Decker can try to stop the report in cybercombat.  Data reports act as standard Icons with 3D6 initiative, and Evasion of 8.  They cannot attack and only use the **Evade Detection** Maneuver.

**Deathworm variant:** Increases all target numbers for Attack and Resistance tests in cybercombat by 2. Multiple infections: +1 per additional worm.

**Tapeworm variant:** Erases downloaded files. At the end of each run, roll 1D6-1; subtract from Paydata Points downloaded. On a 5-6 for specific datafiles: corrupts the information.

### Trace IC

**Type:** Hybrid (White/Gray behavior, two-stage operation)

Trace IC has two phases:

**Hunt Cycle:**
- Trace IC makes Attack Tests against the decker using the **Trace Factor** as target number.
- Hunt cycle continues until the trace IC achieves a successful Attack Test.
- The decker can attack and destroy trace IC during the hunt cycle.

**Location Cycle:**
- Begins when trace IC makes a successful Attack Test (the IC vanishes and becomes reactive).
- Duration: 10 Combat Turns / number of successes on the IC's Attack Test (rounded down).
- During this time, the decker can attempt to locate and neutralize the IC.

**Trace Factor:**
```
Trace Factor = Evasion Rating - Trace IC Rating + (number of Redirect Datatrail operations) + Camo utility rating + Jackpoint Trace modifier + Bandwidth Trace modifier
```

**Defeating Trace IC:**
1. **Attack it** during hunt cycle (cybercombat).
2. **Graceful Logoff** (adds IC rating to the target number for the logoff operation).
3. **Relocate utility**: Spend a Simple Action, make a **Control Test** (Relocate utility reduces target number). Gamemaster makes an opposing Security Test; successes add to security tally. If the decker's Control Test yields more successes, the trace is spoofed for that turn.  The Decker can choose to suppress the IC at this point and no further tests will be necessary unless the suppression is released.

Simply jacking out does not stop trace IC -- the commiline remains open, and the IC can still complete its cycle. Roll 1D6 (minimum 1); that many turns remain for the trace to complete after jack-out.

**Trace Effects on Completion:**
- Records jackpoint network address and physical location in security logs.
- **IC-targeting bonus:** Reduces target numbers for Attack Tests by all proactive IC by 1.
- **Tally acceleration:** Adds 1 to every subsequent increase to the security tally.
- Physical security assets may be dispatched (see Security Asset Response Times table below).

**Physical Measures:**

Response speed depends on the invaded system owner's resources, jurisdictional concerns, proximity of security assets, local law-enforcement involvement, and the Security Rating of the jackpoint's location. Gamemasters may use discretion or roll on the table below. All values are **minutes**. "On-site" means the jackpoint is inside a manned facility belonging to the target system's owner. "Government" entries assume a UCAS setting -- adjust for less organized or more paranoid governments.

See [Security Asset Response Times](#security-asset-response-times-when-trace-ic-locates-deckers-jackpoint) in Reference Tables.

**Trace on a Grid:**
Trace triggered by an RTG or LTG follows the decker as long as they remain on that RTG's system. The IC loses interest if the decker moves to a different RTG, PLTG, or host. If the trace was triggered by the RTG governing the decker's jackpoint, the trace can immediately dump the decker once it locates the jackpoint.

### Black IC

Black IC injects dangerous biofeedback into the deck's ASIST interface, overloading the decker's neural connections. Effects range from unconsciousness to death.

Cool decks reduce damage: lethal black IC acts as non-lethal black IC on a cool deck. Tortoises are immune to lethal effects; they are still vulnerable to stun and psychotropic IC.

**Black IC in Combat:**
- Before a black IC hit: jacking out is a Free Action.
- After the first black IC hit (even if no damage): the decker must spend a Complex Action and make a **Willpower (Black IC Rating) Test** to jack out.
- If the Willpower Test succeeds, the decker may jack out, but black IC makes one more Attack before the connection goes down.
- An ICCM biofeedback filter (see [Cyberdecks](#cyberdecks)) changes the jack-out procedure.

#### Lethal Black IC

Fights like killer IC. Damage Code based on host Security Code:

| Host Security Code | Damage Level |
|--------------------|-------------|
| Blue | (IC Rating)L |
| Green | (IC Rating)M |
| Orange | (IC Rating)M  |
| Red | (IC Rating)S  |
| Black | (IC Rating)S |

Stage up 1 level for every 2 successes on the IC's Attack Test.

**On each hit, the decker makes two Resistance Tests:**
1. **Body Resistance Test** to resist damage to his physical body. Hardening reduces Power. Hacking Pool dice cannot be used; Karma Pool dice can.
2. **Bod Resistance Test** to resist damage to the icon. Hardening reduces Power and Armor protects normally.

**If the icon is killed before the decker dies:** The Matrix connection remains intact. The IC's effective rating increases by 2. The decker cannot fight back -- only attempt to jack out.

**If black IC kills the decker:** Connection automatically drops. Before releasing, the IC attacks the MPCP as blaster IC at **double its rating**. If the MPCP is destroyed (rating reduced to 0), all data downloaded during the run is deleted.

**Deckers running a cool deck experience lethal Black IC as Non-Lethal**

#### Non-Lethal Black IC

Same as lethal black IC, except:
- Causes **Stun** (not Physical) damage.
- Decker resists with Willpower Tests.
- If rendered unconscious, Matrix connection breaks automatically.
- The Black IC gets the opportunity to attack the MPCP as blaster IC at **double its rating**, the same as Lethal Black IC
- Works the same on both hot and cool decks.
- Mental damage can overflow into the Physical Condition Monitor.

#### Psychotropic Black IC

This campaign will not be utilizing Psychotropic Black IC.  This section on Psychotropic IC can be ignored.

Same as non-lethal black IC, with the addition of psychological trauma on dump/unconsciousness. **Willpower (Psychotropic Black IC Rating) Test** to avoid lasting effects. Cool deck: reduce target number by 2.  Only 1 success is needed to resist.

**Psychotropic effects (roll 1D6):**

| D6 | Effect |
|----|--------|
| 1-3 | Cyberphobia |
| 4 | Judas effect |
| 5 | Matrix Maniac |
| 6 | PCPIC (Positive-Conditioning Psychotropic IC) |

**Cyberphobia:** Profound fear of the Matrix. Willpower Test (IC rating) required before jacking in. Add the IC's rating to all decking, programming, and hardware test target numbers.

**Judas:** Subliminal compulsion to betray self and colleagues. Willpower (Psychotropic IC Rating) Test each time the decker would perform a compromising act. Failure: the decker carries out the act with Stealth equal to the psychotropic IC rating.

**Matrix Maniac:** Decker recovers consciousness in a rage. Fights at full auto, no holds barred. Lasts until killed or knocked out. Resumes if the decker regains consciousness. Willpower (Psychotropic IC Rating) Test every 24 hours to snap out of it.

**PCPIC:** Decker is compelled to jack out. Willpower (Psychotropic IC Rating) Test each turn to resist. May also include brand loyalty conditioning. Decker successfully jacked out may make a Willpower Test to negate subsequent effects.

**Recovering from Psychotropic Effects:** Willpower Tests (vs. IC Rating). Matrix maniacs test daily; others test weekly. Under medication: reduce TN by 1. Under intensive psychotherapy (Hospitalized lifestyle): reduce TN by 2 (not cumulative with medication).

### IC Defensive Options

Any IC program may carry defensive options:

| Option | Effect |
|--------|--------|
| **Armor** | Reduces Power of attacks against the IC by 2. |
| **Shield** | +2 target number modifier for all tests a decker makes to hit the IC. Penetration option defeats shield automatically (no +2 penalty). Extra-effective vs. chaser option (+4 modifier instead). |
| **Shift** | +2 modifier to all tests to hit the IC. Chaser option defeats shift automatically. Extra-effective vs. penetration option (+4 modifier). Shield and Shift are mutually exclusive (both compatible with Armor). |

### Trap IC

Any white, gray, or trace IC can be used as **trap IC** -- linked to hidden gray or black IC. When the trap IC is:
- Destroyed in cybercombat: triggers the hidden IC.
- In the case of trace IC: when its location cycle completes successfully.

If the decker **neutralizes** the trap IC without destroying it, the hidden IC is not triggered.

Applications, files, and slave remotes can also be fitted with hidden gray or black IC -- triggered when the decker crashes the protected icons or fails a System Test to control the icon. A **data bomb** variant detonates if the decker fails a test against the booby-trapped subsystem.

Detecting trap IC: **Analyze IC** operation on white IC, or **Analyze Icon** for other Matrix entities fitted with trap IC.

### Optional Rules: Advanced IC

#### Cascading IC

When a proactive IC program **misses** the decker, it allocates more system resources: increase the Security Value used for its attacks by 1. Each subsequent miss: +1 more.

If the IC hits but the decker **resists all damage**: increase the IC's Rating by 1 for subsequent attacks.

Maximum increase:

| System Security Code | Maximum Increase |
|---------------------|-----------------|
| Blue | 1 |
| Green | 25% of original rating, or +2 (whichever is lower) |
| Orange | 50% of original rating, or +3 (whichever is lower) |
| Red | 75% of original rating, or +4 (whichever is lower) |
| Black | 100% of original rating, or +6 (whichever is lower) |

#### Expert IC

Expert IC provides a bonus to offense or defense. Value Range of 1 to 3.  Increase to offensve reduces Defense by the same amount and vice versa.

### Constructs

A construct is a gamemaster-designed icon combining two or more IC programs into a single Matrix critter. Constructs may have **Threat Ratings** -- extra dice added to all tests except Initiative rolls:

| System Security Code | Maximum Threat Rating |
|---------------------|-----------------------|
| Blue | None |
| Green | 1 |
| Orange | 2 |
| Red | 3 |
| Black | 4 |

#### Building Constructs

**Capacity** = 2 x Security Value of the parent host/grid.

- Combined IC program ratings cannot exceed the construct's capacity.
- No single IC program may have a rating greater than [Security Value x 2/3] (rounded up).
- Gray IC programs cost 1 extra capacity point (e.g., Blaster-4 uses 5 points).
- Black IC programs cost 2 extra capacity points.
- Armor, Shield, or Shift defensive options each cost 2 capacity points.

**Example:** Security Value 8 -> capacity 16. Max single program rating = 6. Blaster-4 (gray) costs 5 points. Fitting Armor + Shift costs 4 points, leaving 12 for IC programs.

#### Constructs in Cybercombat

- Constructs are always **proactive** (a construct with only reactive components offers no advantage).
- Attacks using any one available IC program per action.
- Treated as a **single icon** with one Condition Monitor -- fill it and all programs crash.
- Attack and Damage Resistance Tests use the host/grid's **Security Value**; individual program ratings determine effect only.
- Can use all standard combat maneuvers.
- **Initiative** = lowest rating among all component IC programs.

### Party IC

Party IC is a cluster of independent IC programs working cooperatively. Each component is a **separate icon** -- the decker must defeat each one individually.

**Attack penalty on party IC programs:** Increase the target number for all Attack Tests made by party IC programs by the number of programs in the cluster (host is dividing attention).

**Defense bonus against the decker:** Increase the decker's target number to hit any cluster component by the number of programs in the cluster. Combat utilities with the **area effect** option bypass this penalty entirely.

Both penalties apply even if the decker has already crashed some components.

#### Building Party IC

**Capacity** = 2 x Security Value of the parent host/grid.

- Combined ratings of all component programs <= capacity.
- Maximum number of components = [Security Value / 2].
- Non-IC component programs may have any rating.
- Each defensive option (Armor, Shield, Shift) consumes 1 capacity point.

### Host Shutdown

If IC and constructs fail to stop an intruder, the host may initiate a self-shutdown to force-dump the decker.

**Determining shutdown duration:** When the shutdown threshold is reached, roll **1D6 per 2 points (or fraction thereof) of the host's Security Value**:

| Security Value | Dice Rolled |
|---------------|------------|
| 1-2 | 1D6 |
| 3-4 | 2D6 |
| 5-6 | 3D6 |
| 7-8 | 4D6 |
| (and so on) | +1D6 per 2 points |

Result = number of Combat Turns the shutdown sequence lasts.

Also roll **1D3** to determine the **final warning turn** -- the turn on which all deckers in the system are told the shutdown is in progress and how many turns remain.

**Detection:** At the end of each Combat Turn, make a secret **Sensor Test** for each decker against TN = turns remaining in the sequence. The first decker to succeed learns the host is shutting down. All deckers are informed automatically when the final warning turn is reached.

**At the end of the last turn:** All online deckers are **dumped** (Dump Shock applies). All running frames and programs crash. All ongoing and monitored operations terminate.

---

## Mapping Matrices and Security Sheaves

### System Access Nodes (SANs)

SANs connect hosts to grids and to each other. When a decker performs a Logon to Host operation, they enter through the SAN. SANs can be:
- **Standard:** Always visible on the LTG.
- **Vanishing:** Open for a few seconds, at intervals determined by the gamemaster (1D6 seconds, several times per day or hour).
- **Teleporting:** Change their RTG/LTG address on a secret schedule.
- **Triggered:** Open only in response to specific events elsewhere in the Matrix.

### Security Sheaves

A **security sheaf** defines all of the security measures on a host or grid, expressed as a list of **trigger steps** -- security tally thresholds. When the security tally reaches a trigger step, the host activates the specified IC programs and/or changes alert status.

**Sample Security Sheaf:**

| Trigger Step | Event |
|-------------|-------|
| 3 | Probe-5 |
| 7 | Trace-7 |
| 12 | Killer-8, Passive Alert |
| 13 | Party IC:  Expert Offense 2/Acid-6, Killer-6/Armor/Shifting |

### Trigger Steps

**Generating Trigger Steps (random):**

Roll 1D3 and apply the modifier from the table; the result is the interval between trigger steps.

| System Security Code | Roll Modifier | Trigger Step Range |
|---------------------|---------------|--------------------|
| Blue | +4 | 5 to 7 |
| Green | +3 | 4 to 6 |
| Orange | +2 | 3 to 5 |
| Red | +1 | 2 to 4 |
| Black | +1 | 2 to 4 |

To create a high-security system: use the lowest value in the range. For mild-mannered systems: use the highest value.

**Multiple Triggers:** If a security tally increase jumps past two or more trigger steps at once, all indicated events activate simultaneously.

### Alerts

All systems have three alert statuses:

**No Alert:**
- Normal operating status.
- Trigger steps activate mostly reactive IC or trace IC.

**Passive Alert:**
- System suspects an intruder but is not 100% certain.
- Typically activated at the third or fourth trigger step.
- Trigger steps activate proactive white or gray IC. Reactive IC is typically trapped or part of party IC.
- **All Subsystem Ratings increase by 2** while the system is on passive alert.

**Active Alert:**
- System has verified the presence of an illegal icon.
- Typically activated two or three trigger steps after passive alert.
- Trigger steps activate proactive and black IC. May activate corporate/law enforcement deckers, and console operators may initiate a system shutdown.
- Logging back in after active alert is significantly harder.

### Random IC Allocation Tables

**Alert Table (roll 1D6 for each trigger step):**

| 1D6 Result | No Alert | Passive Alert | Active Alert |
|------------|----------|--------------|-------------|
| 1-3 | Reactive White | Proactive White | Proactive Gray |
| 4-5 | Proactive White | Reactive Gray | Proactive White |
| 6-7 | Reactive Gray | Proactive Gray | Black IC |
| 8+ | Passive Alert | Active Alert | Shutdown |

At No Alert and Passive Alert: add the number of trigger steps already passed to the roll result.

**Reactive White IC Table (roll 1D6):**

| 1D6 Result | IC |
|------------|----|
| 1-2 | Probe |
| 3-5 | Trace |
| 6 | Tar Baby |

**Proactive White IC Table (roll 2D6):**

| 2D6 Result | IC |
|------------|----|
| 2-5 | Crippler+ |
| 6-8 | Killer |
| 9 | Trap Trace++ |
| 10 | Trap Probe++ |
| 11-12 | Construct/Party IC |

+ Roll on Crippler/Ripper IC Table for persona attribute targeted; then roll on IC Rating table for the program rating.
++ Roll on Trap IC Table to determine type of trap IC; then roll on IC Ratings Table for the program rating.

**Reactive Gray IC Table (roll 1D6):**

| 1D6 Result | IC |
|------------|----|
| 1-2 | Trap Probe++ |
| 3-5 | Trap Trace++ |
| 6 | Tar Pit |

++ Roll on Trap IC Table to determine type of trap IC; then roll on IC Ratings Table for the program rating.

**Proactive Gray IC Table (roll 2D6):**

| 2D6 Result | IC |
|------------|----|
| 2-5 | Rippers+ |
| 6-8 | Blaster |
| 9-10 | Sparky |
| 11-12 | Construct/Party IC |

+ Roll on the Crippler/Ripper IC Table for persona attribute targeted; then roll on IC Rating table for the program rating.

**Black IC Table (roll 2D6):**

| 2D6 Result | IC |
|------------|----|
| 2-4 | Lethal |
| 5-9 | Non-Lethal |
| 10-12 | Construct/Party IC |

For Psychotropic type, roll 1D6: 1-3 = Cyberphobia; 4 = Judas; 5 = Matrix Maniac; 6 = PCPIC.  (NOTE:  Psychotropic is not being using in this campaign)

**Trap IC Table**
| 2D6 Result | IC |
| 2-5 | Blaster |
| 6-8 | Killer |
| 9-11 | Sparky |
| 12 | Black IC |

**Crippler/Ripper Target Attribute Table (roll 1D6):**

| 1D6 | Attribute Targeted |
|-----|--------------------|
| 1-2 | Bod |
| 3 | Evasion |
| 4-5 | Masking |
| 6 | Sensor |

**IC Ratings Table (roll 2D6):**

| 2D6 Result | Security Value 4 or less | Security Value 5-7 | Security Value 8-10 | Security Value 11+ |
|------------|--------------------------|--------------------|---------------------|--------------------|
| 2-5 | 4 | 5 |6 | 8 |
| 6-8 | 5 | 7 | 8 | 10 |
| 9-11 | 6 | 9 | 10 | 11 |
| 12 | 7 | 10 | 12 | 12 |

**IC Options Table (roll 2D6):**

| 2D6 | Option |
| 2 | Cascading |
| 3-5 | Expert Offense+ |
| 6-8 | None |
| 9-11 | Expert Defense+ |
| 12 | Cascading |

+ Roll 1D3 to determine Expert modifier value.

**IC Defenses Table (roll 2D6):**

| 2D6 | Defense |
|-----|---------|
| 2-3 | Armor and Shifting |
| 4-5 | Armor |
| 6 | Shifting |
| 7 | None |
| 8 | Shielding |
| 9-10 | Armor
| 11-12 | Armor and Shielding |

### Host Reset

After all deckers log off from a host, the host begins resetting itself:

| Security Code | Reset Time |
|---------------|------------|
| Blue | 2D6 minutes |
| Green | 1D6 * 5 minutes |
| Orange | 1D6 * 10 minutes |
| Red | 1D6 * 15 minutes |
| Black | 1D6 hours |

During reset, the security tally decreases. IC programs deactivate when the tally drops below the trigger step that activated them. Programs still running at the reset's start remain active until the tally drops below their trigger step.

If a decker logs on illegally during a reset, his security tally begins at the tally level the reset has reached -- he picks up where the previous decker left off.

Should a Decker logon before the tally resets, divide the number of elapsed minutes by reset time, and multiply the resulting percentage against the security tally to determine the new level.

### Paydata

**Paydata Points (random generation):**

See [Paydata Points Table](#paydata-points-table) in Reference Tables.

Deckers must first perform a Locate Paydata operation.  The number of successes determines how many paydata points are discovered up to the Paydata Points result.  The Decker must then download the Paydata file completely to gain 1 Paydata Point. File size = data density result.

**Base street price of a Paydata Point:** 5,000 nuyen.

The value decreases by 1 Paydata Point per day unsold (per standard SR fencing rules). This does not apply to specific files with predetermined prices.

**Paydata File Defenses (roll 1D6):**

| Security Code | 1D6 Range: No Defense | Data Bomb | Scramble IC | Data Bomb + Scramble IC Combo |
|---------------|----------------------|-----------|-------------|-------|
| Green | 1-4 | 5 | 6 | - |
| Orange | 1-3 | 4 | 5--6 | - |
| Red | 1 | 2--3 | 4--5 | 6 |
| Black | - | 1-2 | 3-4 | 5-6 |

(Specific defense results depend on 1D6 roll)

### Slave Systems

Slave subsystems control remote devices. A successful Slave Test gives an unauthorized decker control of devices such as security cameras, elevators, automated factories, and medical equipment.

For manufacturing or scientific processes, the decker must make the Control Test with the appropriate B/R or Knowledge Skill.

To upload a program to control a slave via a remote device: use the Locate Slave operation, followed by Control Slave or Edit Slave.

### UMS and Sculpted Systems

**UMS (Universal Matrix Symbology):** The standard default visual representation of Matrix space -- functional icons representing computer components.

**Sculpted Systems:** Hosts designed with custom virtual reality imagery. When logging onto a sculpted system, everything is explained in terms of the system's central metaphor.

**Rules for Sculpted Systems:**
- If a decker describes his actions in terms that don't conform to the metaphor: +2 modifier to all target numbers.
- If the decker's reality filter does not match the metaphor:
  - Roll an **MPCP Test** vs. the system's Security Value.
  - **Failure:** Lose 2 Reaction and 1D6 Initiative for the remainder of the run.
  - **Success:** The decker's filter dominates; no penalty.
- Sculpted systems can extend over linked hosts, across an entire PLTG.

---

## Deckers

### Decker Skills and Attributes

**Key attributes for deckers:**
- **Intelligence:** Crucial for the Hacking Pool. All forms of Intelligence increase also increase the Hacking Pool.
- **Body:** Resists damage from black IC (Decker can use Willpower with ICCM technology).
- **Willpower:** Resists black IC effects and jacking out while under attack.
- **Quickness:** Affects Reaction and thus Matrix initiative.
- **Charisma:** Not generally useful for decking.

**Key skills:**
- **Computer (Decking specialization):** Essential for all Matrix operations. Governs programming. Maximum program ratings the character can create = Computer (or Software Concentratio/Matrix Programming Specialization) Skill.  The maximum ratings of character designed MPCPs = Computer (or Software Concentratio/Matrix Programming Specialization) Skill x 1.5
- **Hardware:** Governs construction of deck components and searching for equipment.
- **Electronics B/R:** Used for some construction tasks alongside Computer B/R.
- **Matrix Etiquette:** Governs access to shadowland networks and underground goods/services.

### MPCP

The **Master Persona Control Program** is the operating system of the cyberdeck. Key functions:
- Defines the persona's appearance (icon) in the Matrix.
- The ratings of the four Persona programs (BEMS) combined cannot exceed 3x MPCP rating.
- Writes the user's **Matrix signature** into system logs each time the user logs on, edits a file, or touches a control system.
- Cyberdecks illegally "stealth" their MPCPs with masking chips, but each MPCP retains a distinctive appearance.
- Tests directly involving the MPCP: stability tests in sculpted hosts, and when the deck is under gray or black IC attack.
- All other programs execute under MPCP control; the MPCP Rating is the cap for all subordinate utilities.

### Persona Programs (BEMS)

The four persona programs define the decker's "attributes" in the Matrix:

| Program | Function |
|---------|----------|
| **Bod** | Stability of the icon; resistance to error, logic attacks, and cybernetic attacks. Governs damage resistance in cybercombat. |
| **Evasion** | Agility of the icon in cybercombat; ability to evade trace IC. Governs combat maneuvers. |
| **Masking** | Ability of the icon to avoid detection. Important for resisting Security Tests. Forms part of the Detection Factor. |
| **Sensor** | Icon's perception of cyberspace; ability to process data. Used for ad hoc Sensor Tests to detect changes in the host (alert states, IC activations). |

### Optional Rule: Deck Modes

Cyberdecks may switch between five modes (switching requires a Complex Action):

| Mode | Effect |
|------|--------|
| **Default** | All ratings at base values. |
| **Bod Mode** | Bod increased 50%; Evasion, Masking, Sensor reduced 50%; I/O bandwidth reduced 50%. |
| **Evasion Mode** | Evasion increased 50%; Bod, Masking, Sensor reduced 50%; I/O bandwidth reduced 50%. |
| **Masking Mode** | Masking increased 50%; Evasion, Sensor reduced 50%; bandwidth unaffected. |
| **Sensor Mode** | Sensor increased 50%; Bod, Evasion, Masking reduced 50%; bandwidth unaffected. |

Round up all fractions. Throughput loss makes Evasion Mode especially costly bandwidth-wise.

### Deckers and Tasks

Most decker construction and programming activities are **tasks** requiring:
- A minimum set of tools and resources.
- A base time (usually in days).
- A **Success Test** (gamemaster rolls secretly; base time / successes = task period).

If the test fails: the number of days it fails by = wasted work before discovering the effort is flawed.

**Task Bonuses:** Superior resources can reduce the task period.

**Task Bonus Table:**

| Task Requires | Tool Available | Task Bonus |
| Kit | Kit | 0 |
| Kit | Shop | +1 |
| Kit | Facility | +3 |
| Shop | Shop | 0 |
| Shop | Facility | +1 |
| Facility | Facility | 0 |

**Interruptions:** Tasks can be completed in parts. Light wounds: no penalty. Moderate wounds: half productivity.  Serious wounds: no work can be done.

---

## Cyberdecks

### Core Components

Microtronic tools are required for cyberdeck construction.  As with other tools, they come in Kits, Shops, and Facilities.

Cybernetic tools are required in addition to Microtronic tools when constructing a cranial cyberdeck.  The **Implant** specialization of the Computer Skill is appropriate for all Cook and Installation tasks of Cranial Cyberdecks.  Apply a +2 target number modifier if using Computer B/R instead.

An Optical Chip Encoder is required to program the Optical Code Chips used in Cyberdecks.  Prices are found in the **Tool Prices Table**.

#### MPCP (Master Persona Control Program)

The MPCP is the heart of the cyberdeck -- all other components depend on it.

**Software Task:**
- Rating: MPCP Rating (add 2 if including a reality filter)
- Multiplier: 8

**Cook Task:**
- Time: MPCP Rating x 3 days
- Test: Computer B/R (MPCP Rating) Test
- Parts: OCC @ program size
- Tools: Personal Computer (memory >= program size), Microtronics Shop, Optical-Chip Encoder

**Installation Task:**
- Time: MPCP Rating x 2 days
- Test: Computer B/R (MPCP Rating) Test
- Parts: PLC @ MPCP Rating^2; DTC @ MPCP Rating^2
- Tools: Microtronics Shop

### MPCP Upgrades

When upgrading an MPCP, the following components must also be upgraded to match the new MPCP Rating before the deck can run with the new MPCP:
- ASIST Interface
- ICCM Filter
- Response Increase

Until upgraded, the decker must choose: run with the old (lower) MPCP, or run without those components.

#### Persona Programs (Bod, Evasion, Masking, Sensor)

**Software Task:**
- Rating: Program Rating
- Multiplier: 3 (Bod and Evasion); 2 (Masking and Sensor)

**Cook Task:**
- Time: Program Rating x 3 days
- Test: Computer B/R (Program Rating) Test
- Parts: OCC @ program size
- Tools: Personal Computer (memory >= persona program size), Microtronics Shop, Optical-Chip Encoder

**Installation Task:**
- Time: Program Rating x 2 days
- Test: Computer B/R (Program Rating) Test
- Parts: PLC @ Program Rating^2; DTC @ Program Rating^2
- Tools: Microtronics Kit

#### Active Memory

Active memory limits the utility programs the deck can run at one time. 100 Mp of active memory can run at most 100 Mp of utilities simultaneously.

**App cap (implemented):**
- Active Memory cannot exceed MPCP Rating x 100 Mp.

**Construction (Installation Task only):**
- Time: Memory Size / 100 days (round up)
- Test: Computer B/R (Memory Size / 100, round up) Test
- Parts: OMC @ memory size; PLC @ memory size / 10 (round up)
- Tools: Microtronics Kit

#### ASIST Interface

Controls the simsense experience of cyberspace and DNI connection to the Matrix.

**Hot deck:** Maximum ASIST signal intensity (BTL chip-level). Best Matrix interface. Running hot on pure DNI (Direct Neural Interface) adds 1 **Response Increase** point.

**Cool deck:** Reduced ASIST signal (legal simsense level). Black IC cannot inflict lethal damage; lethal black IC acts as non-lethal. Reduces Initiative by 1D6 (for running cool with manual controls), reduces dump shock Power by 2 and lowers Damage Level by 1.

**Tortoise:** No ASIST interface. Reduces Reaction to half (minimum 1). Immune to dump shock. Can receive benefit from **Response Increase** hardware but no bonus to reaction from Reponse Increase. Immune to lethal and simsense overload effects.

Switching between hot, cool, and tortoise requires the same test as jacking out while under black IC attack.

**ASIST Construction:**

Software Task:
- Rating: MPCP Rating
- Multiplier: Hot deck: MPCP Rating x 2 (approximately); Cool deck: MPCP Rating x 1

Cook Task:
- Time: MPCP Rating days
- Test: Computer B/R (MPCP Rating) Test
- Parts: OCC @ program size
- Tools:  Personal Computer (memory >= persona program size), Microtronics Shop, Optical-Chip Encoder

Installation Task:
- Time: MPCP Rating days
- Test: Computer B/R (MPCP Rating) Test
- Parts: Hot Deck: PLC @ MPCP Rating x 2; Cool Deck: PLC @ MPCP Rating; ASIST Processing Unit @ 1,250Y
- Tools: Microtronics Kit

#### Hardening

Hardening protects the deck from gray IC that targets the MPCP. Each point of Hardening:
- Increases the target number for all tests made by gray IC against the MPCP by 1 (effectively: TN = MPCP Rating + Hardening).
- Reduces the Power of sparky and black IC damage to the decker.

**Software Task:**
- Rating: Hardening Rating
- Multiplier: 8

**Cook Task:**
- Time: MPCP Rating x Hardening Rating days
- Parts: OCC @ Hardening program size
- Tools: Personal Computer (memory >= hardening program size), Microtronics Shop, Optical-Chip Encoder

**Installation Task:**
- Time: MPCP Rating x Hardening Rating x 2 days
- Test: Computer B/R (MPCP Rating) Test
- Parts: PLC @ Hardening Rating x 2; DTC @ Hardening Rating x 2
- Tools: Microtronics Shop

#### ICCM Biofeedback Filter

The ICCM (Intrusion Counter-Countermeasures) biofeedback filter:
- Allows the decker to make a separate **Willpower Test** when black IC attacks, reducing the chance of physical damage.  (1 test each with Body and Willpower.  Decker chooses which test to use.  Karma Pool dice allowed, Hacking Pool dice disallowed)
- Decreases the target number for jacking out while under black IC attack by 2.
- Does not protect against psychotropic effects.
- Does buffer the deck against physical side effects of sparky IC.
- Test for ICCM construction involves **average of Computer B/R and Biotech skills**.

**Software Task:**
- Rating: MPCP Rating
- Multiplier: 4

**Cook Task:**
- Time: MPCP Rating x 2 days
- Test: Average Computer B/R and Biotech (MPCP Rating) Test
- Parts: OCC @ ICCM program size
- Tools: Personal Computer (memory >= ICCM program size), Microtronics Shop, Optical-Chip Encoder

**Installation Task:**
- Time: MPCP Rating x 2 days
- Test: Average Computer B/R and Biotech (MPCP Rating) Test
- Parts: PLC @ MPCP Rating^2; DTC @ MPCP Rating^2; Bioscanner (5,000Y fixed cost)
- Tools: Microtronics Shop

#### I/O Speed

I/O Speed determines the maximum bandwidth -- the data transfer rate between the deck and the Matrix.

- Must be built in multiples of 10 Mp.
- Maximum bandwidth = Sensor Rating x MPCP Rating x 10 Mp.
- Icon bandwidth = sum of all persona program ratings + all loaded utility ratings.

**Construction (Installation Task only):**
- Time: I/O Speed / 20 days (round up)
- Test: Computer B/R (I/O Speed / 100, round up) Test
- Parts: PLC @ I/O Speed / 20 (round up); DTC @ I/O Speed / 10 (round up)
- Tools: Microtronics Kit

#### Response Increase

Response Increase is the Matrix equivalent of wired reflexes.

**Each point of Response Increase adds:**
- +2 to Reaction
- +1D6 to Initiative

**Constraints:**
- Maximum 3 points from hardware alone.
- Response Increase cannot exceed MPCP Rating / 4 (round down). A deck with MPCP <= 3 cannot have any Response Increase.
- 1 additional point from a Reality Filter.
- 1 additional point for running hot on pure DNI control.
- **Absolute maximum: 5 points** (= +10 Reaction, 6D6 Initiative).

**Software Task:**
- Rating: MPCP Rating
- Multiplier: Response Increase Rating x 2

**Cook Task:**
- Time: MPCP Rating x Response Increase Rating in days
- Test: Computer B/R (Response Increase Rating x 2) Test
- Parts: OCC @ program size
- Tools: Personal Computer (memory >= Response program size), Microtronics Shop, Optical-Chip Encoder

**Installation Task:**
- Time: (MPCP Rating + Response Increase Rating) days
- Test: Computer B/R (Response Increase x 2) Test
- Parts: PLC @ Rating x 3; DTC @ Rating x 3
- Tools: Microtronics Shop

#### Reality Filters

Reality filters allow deckers to run the entire Matrix through a chosen metaphor (e.g., a cyberpunk swordsman; a jazz musician).

- Increase Reaction by 2 and add +1D6 to Initiative.
- Reduce MPCP Rating by 1 (may require reducing persona programs).
- Turning a filter on or off: Free Action at the beginning of a Combat Turn.
- Turning off the filter while active: reduce current Initiative by half, apply a modifier to all target numbers.

**Reality Filter construction:** As MPCP, with Rating = MPCP Rating + 2, and Multiplier = 8.

#### Satlink Interface

Allows the deck to connect via satellite uplink. Requires an external satellite dish.

**Software Task:**
- Rating: MPCP Rating
- Multiplier: 2

**Cook Task:**
- Time: MPCP Rating days
- Test: Computer B/R (MPCP Rating) Test
- Parts: OCC @ program size
- Tools: Personal Computer (memory >= MPCP program size), Microtronics Shop, Optical-Chip Encoder

**Installation Task:**
- Time: MPCP Rating days
- Test: Computer B/R (MPCP Rating) Test
- Parts: PLC @ MPCP Rating; DTC @ MPCP Rating
- Tools: Microtronics Shop

**Satlink Dish Prices:**

| Dish Type | Price |
|-----------|-------|
| Standard portable (0.5m) | 800Y |
| Large portable (1m) | 1,200Y |
| Fixed-base | 900Y |
| Cable | 10Y/meter |
| Temporary dish electronics | 1,000Y |
| Temporary plastic webbing | 5Y |
| Temporary spray polymer (1 use) | 1Y |

Large portable dishes reduce target numbers for satellite location tests by 1. Fixed-base: -2.

#### Storage Memory

Programs not currently in active memory are stored here. Programs must be in storage memory to be loaded into active memory via Swap Memory operations. Cheaper than active memory.

**App cap (implemented):**
- Storage Memory has no SR2 hard rules cap, but this app uses a practical upper bound of 65,535 Mp.

**Construction (Installation Task only):**
- Time: Memory Size / 100 days (round up)
- Test: Computer B/R (Memory Size / 100, round up) Test
- Parts: OMC @ Memory Size; PLC @ Memory Size / 10 (round up)
- Tools: Microtronics Kit

### Component Prices

**Miscellaneous Components:**

| Component | Price |
|-----------|-------|
| Casing (Basic, Impact 1) | Negligible |
| Casing Level 1 (Impact 2, Ballistic 1) | 500Y |
| Casing Level 2 (Impact 3, Ballistic 2) | 2,000Y |
| Casing Level 3 (Impact 4, Ballistic 3) | 5,000Y |
| Hitcher Jack | 250Y |
| Off-line Storage (OMC) | 50Y + 0.5Y/Mp |
| Vidscreen | 100Y |

### Decks a la Carte

Deckers can order custom decks from manufacturers assembled from components they specify. Each price formula in the Deck Component Prices table covers the full cost of a component -- software, hardware, circuitry, and installation.

Formulas for components with software use a **Program Factor (PF)**: a multiplier determined by a specific deck rating called the **PF basis**. For example, the PF basis for Hardening is the deck's MPCP rating -- an MPCP-8 deck uses a PF of 500Y in its Hardening formula.

A decker who already owns the object code for a component (e.g., an existing MPCP chip) only needs to pay for the OCC and installation portions, which can be calculated from the component's task description.

**Program Factors (PF) by Rating:**

| Program Rating | PF (nuyen) |
|---------------|-----------|
| 1-3 | 100 |
| 4-6 | 200 |
| 7-9 | 500 |
| 10+ | 1,000 |

See [Deck Component Prices](#deck-component-prices-quick-reference) in Reference Tables.

**Package discount:** 10% discount when ordering a complete deck (MPCP + persona chips + ASIST interface + optional components). Generous dealers may offer 20%.

**Tool Prices Table**

| Tool | Cost | Availability | Street Index |
| Cybernetics Kit | 1500 | 5/48 hrs | 2 |
| Cybernetics Shop | 15000 | 8/72 hrs | 3 |
| Cybernetics Facility | 300000 | 14/7 days | 4 |
| Microtronics Kit | 1500 | 5/48 hrs | 2 |
| Microtronics Shop | 15000 | 8/72 hrs | 3 |
| Microtronics Facility | 300000 | 14/7 days | 4 |
| Personal Computer | 20 per Mp of memory | Always | .75 |

**Optical Chip Encoder Prices Table**

| Optical Chip Encoder | Rating | Task Bonus | Cost | Availability | Street Index |
| Sony Encoder I | 0 | 0 | 1200 | 4/24 hrs | 1 |
| Fuchi OCE/500 | 1 | 0 | 2700 | 6/24 hrs | 1 |
| Sony Encoder II | 2 | 1 | 6000 | 8/72 hrs | 1.5 |
| Hitachi RM-AX | 3 | 2 | 9500 | 10/7 days | 2 |


**Parts Prices:**

| Part | Price |
|------|-------|
| Optical Code Chip (OCC) | 20Y per Mp |
| Optical Memory Chip (OMC) | 5Y per Mp |
| Cranial OCC | 200Y per Mp |
| Cranial OMC | 50Y per Mp |
| Processor Logic Circuitry (PLC) | 25Y x Rating |
| Data Transport Circuitry (DTC) | 10Y x Rating |
| Cranial PLC | 250Y x Rating |
| Cranial DTC | 100Y x Rating |

---

## Programs

### Source and Object Code

- **Source code:** Original human-readable form of a program. Required to upgrade or modify a program.
- **Object code:** Machine-executable form. Object-code copies cannot be upgraded or modified; a full new program must be written from source.

### Utilities

Utilities supplement the decker's persona. Four categories:

1. **Operational utilities:** Reduce target numbers for System Tests by the utility's rating.
2. **Special utilities:** Perform specific Matrix tasks.
3. **Offensive utilities:** Attack opposing deckers, IC, and icons.
4. **Defensive utilities:** Prevent or reduce damage in cybercombat.

All operational utilities may use the DINAB, one-shot, optimization, and squeeze options.

#### Operational Utilities

**Analyze** | Multiplier: 3
- System Operations: Analyze IC, Analyze Icon, Analyze Security, Locate IC
- Reduces target numbers for System Tests that identify IC, programs, and other resources or events controlled by a host.

**Browse** | Multiplier: 1
- System Operations: Locate Access Node, Locate File, Locate Slave
- Reduces target numbers for Index Tests made to locate specific data values or system addresses. (Unlike Analyze and Scanner, Browse works on the *content* of data nodes.)

**Commlink** | Multiplier: 1
- System Operations: Retrain, Tap Comcall
- Reduces target numbers for any tests affecting the decker's communications link.

**Crash** | Multiplier: 3
- System Operations: Crash Application, Crash Host
- Reduces target numbers for crashing an application or host.

**Defuse** | Multipler: 2
- Reduces the target numbers for System Tests to defuse data bombs.

**Decrypt** | Multiplier: 1
- System Operations: Decrypt Access, Decrypt File, Decrypt Slave
- Reduces target numbers for System Tests to defeat scramble IC programs.

**Deception** | Multiplier: 2
- System Operations: Graceful Logoff, Logon to (LTG, RTG, or Host)
- Unless otherwise noted, reduces target numbers for all Access Tests.

**Disinfect** | Multiplier: 2
- System Operations: Disinfect
- Reduces target numbers for System Tests to destroy worm viruses.

**Evaluate** | Multiplier: 2
- System Operations: Locate Paydata, Locate File (value assessment)
- Used to identify and locate paydata.
- Evaluate degrades at the end of each run.  Roll 1D3.  The value of all Evaluate programs is reduced by the result.  Deckers with source copies can upgrade per standard rules.

**Mirrors** | Multiplier: 3
- System Operations: Decoy
- Reduces target numbers for Decoy operations.

**Read/Write** | Multiplier: 2
- System Operations: Download Data, Edit File, Upload Data
- Reduces target numbers for reading and writing datafiles and for upload/download operations.

**Relocate** | Multiplier: 2
- System Operations: Relocate (defeating trace IC)
- Used to defeat trace IC during its location cycle. Reduces target number for the Control Test.
- Cannot defeat trace IC during the hunt cycle.

**Scanner** | Multiplier: 3
- System Operations: Locate Decker, Locate Frame
- Reduces target numbers for locating other deckers and frames in the Matrix.

**Spoof** | Multiplier: 3
- System Operations: Command Slave, Edit Slave, Monitor Slave
- Reduces target numbers for controlling or manipulating slave subsystem functions.

**Validate** | Multiplier: 4
- System Operations: Dump Log, Invalidate Passcode, Validate Passcode
- Reduces target numbers for passcode operations. Also used when tracing accessed icons.

#### Special Utilities

**Compressor** | Multiplier: 2
- Reduces size of data being transferred by 50%.  Max file size is Program Rating * 100 Mp.
- Decks must have sufficient active memory to hold the uncompressed size of the file.
- Files must be decompressed before being able to read or use them.

**Sleaze** | Multiplier: 3
- Used passively; part of the Detection Factor formula (see [Detection Factor](#detection-factor)).
- Reduces the chance that the system detects the decker's presence.
- Must be running during the entire run to be effective.

**Track** | Multiplier: 8
- Used to trace enemy deckers in the Matrix, functioning much like Trace IC does against a decker.
- Works against enemy deckers in general -- not only after they jack out -- following their datatrail to locate them.

#### Offensive Utilities

**Attack** | Multiplier: Light: 2; Moderate: 3; Serious: 4; Deadly: 5
- Target: Deckers, Frames, IC
- Options: Area, Chaser, DINAB, Limit, One-shot, Optimization, Penetration, Stealth, Targeting
- Standard combat utility. Inflicts standard icon damage in cybercombat.

**Black Hammer** | Multiplier: 20
- Target: Deckers
- Options: One-shot, Optimization, Targeting
- Maximum program rating is half Computer skill (rounded up)
- Inflicts lethal damage. Functions like black IC but from a decker. If attack hits, target resists with Body (damage to person) and Bod (damage to icon). Also reduces the target's deck MPCP Rating if the attack crashes the icon (test like blaster IC at double the program rating). Hardening reduces the damage target number for resistance tests.

**Hog** | Multiplier: 3
- Target: Deckers
- Options: DINAB, One-shot, Optimization, Targeting
- A virus weapon that introduces self-replicating code into the target cyberdeck, occupying active memory and crashing running utilities.
- **On a successful attack:** Target makes an **MPCP (Hog Rating) Test**. Hardening reduces the target number.
  - If the attacker wins: reduce the **highest-rated running program** on the targeted deck by 1 point per 2 net successes.
  - The same drain repeats at the **end of every subsequent Combat Turn** until that program crashes.
  - Once a program crashes, Hog moves to the **next highest-rated program** and repeats, continuing until all programs on the deck are crashed.
- Infected programs operate at their reduced ratings until fully crashed.
- **Purging Hog:** Spend a Complex Action and succeed on a **Computer (Hog Rating - Hardening) Test**, with the target number increased by the original rating of the infected program. A single success wipes both the Hog virus and the infected program from active memory. The virus cannot be purged without also purging the infected program.
- Crashed or purged programs can be reloaded via the Swap Memory operation.

**Killjoy** | Multiplier: 10
- Target: Deckers
- Options: One-shot, Optimization, Targeting
- Functions exactly like *Black Hammer* program, except it does Stun damage to the opponent Decker instead of Physical.
- Maximum program rating is half Computer skill (rounded up)

**Poison** | Multiplier: 3
- Target: Deckers, Frames
- Options: Area, DINAB, One-shot, Optimization, Targeting
- The poison utility attacks the Bod attribute, like Acid Crippler IC. If the attack hits, the target makes a Bod (Rating) Test. On failure: Bod Rating is reduced by 1 for every 2 net successes the attacker achieved.

**Restrict** | Multiplier: 3
- Target: Deckers, Frames
- Options: Area, DINAB, One-shot, Optimization, Targeting
- The Restrict utility attacks the Evasion attribute, like Binder Crippler IC. If the attack hits, the target makes an Evasion (Rating) Test. On failure: Evasion Rating is reduced by 1 for every 2 net successes the attacker achieved.

**Reveal** | Multiplier: 3
- Target: Deckers, Frames
- Options: Area, DINAB, One-shot, Optimization, Targeting
- The Reveal utility attacks the Masking attribute, like Marker Crippler IC. If the attack hits, the target makes a Masking (Rating) Test. On failure: Masking Rating is reduced by 1 for every 2 net successes the attacker achieved.

**Slow** | Multiplier: 4
- Target: Proactive IC only (reactive IC is immune; trace IC is only vulnerable during its Hunt Cycle)
- Options: Area, DINAB, One-shot, Optimization, Targeting
- Reduces execution speed of proactive IC. On a successful hit, make an opposed **Resistance (Slow Rating) Test** for the targeted IC:
  - IC more successes: no effect.
  - Attacker more successes: IC loses **1 action per 2 net successes**. If the IC has no actions remaining in the turn, it **hangs** (goes dead for that turn).
- Hanging IC may be suppressed using standard suppression rules.
- If the IC is not suppressed at the start of the next Combat Turn, the gamemaster rolls initiative for it normally and it resumes operation.

**Steamroller** | Multiplier: 3
- Target: Tar Baby and Tar Pit IC
- Options: DINAB, One-shot, Optimization, Stealth, Targeting
- Inflicts **(Rating)D** damage to tar IC programs. Immune to the destructive effect of tar programs -- tar IC cannot crash the Steamroller utility.
- Crashing tar IC with Steamroller adds to the security tally unless the Steamroller has the **Stealth** option or the decker suppresses the IC per standard rules.

#### Defensive Utilities

**Armor** | Multiplier: 3
- Options: Optimization
- Reduces the Power of attacks against the decker's *icon* by the Armor utility's rating. Applied to Damage Resistance Tests.
- **Armor loses 1 Rating Point every time the decker takes damage.**  Degraded armor utilities can be replaced via a **Swap Memory** operation.

**Camo** | Multiplier: 3
- Options: One-shot, Optimization
- Adds its rating to the Trace Factor, making the decker harder to trace.
- Also reduces target number for Redirect Datatrail operations.

**Cloak** | Multiplier: 3
- Options: One-shot, Optimization
- Reduces target numbers for the decker's Evasion Tests during combat maneuvers.

**Lock-On** | Multiplier: 3
- Options: One-shot, Optimization
- Reduces target numbers for the opposing icon's Sensor Test when the decker performs combat maneuvers.

**Medic** | Multiplier: 4
- Options: DINAB, Optimization
- Heals the decker's icon via a *complex action*. Makes a **Medic Test** against a target number based on the damage to the Icon. Recovers 1 box per success.
- **Medic loses 1 Rating Point each time it is used, regardless of outcome.**  Degraded medic programs can be replaced via **Swap Memory** operation.
- Medic Target Numbers Table
| Icon Wound Level | Target Number |
| Light | 4 |
| Moderate | 5 |
| Serious | 6 |

**Restore** | Multiplier: 3
- Options: DINAB, One-shot, Optimization
- Repairs damage to online icon attributes. Cannot repair permanent damage to Persona chips caused by gray or black IC.
- **Restore Test:** TN = rating of the program that caused the damage. If damage came from multiple programs, use the highest rating.
- Repairs **1 point of damage per 2 successes**.

**Shield** | Multiplier: 4
- Options: Optimization
- Parry attacks in cybercombat. When an attack affects the decker's persona, make a **Shield Test** (target number = attacker's skill: Computer Skill for a decker, Security Value for IC). Net successes reduce the attacker's damage successes.
- Effective against crippler/ripper attacks: add Shield Test successes to the decker's opposed test successes.
- **Shield loses 1 Rating Point every time it is used** (regardless of outcome). Fresh copies must be loaded via **Swap Memory** operation.

### Utility Options (Optional Rule)

Options modify a utility's effective rating or size. Under standard Matrix rules, a program has one size that governs both the space it occupies on the deck and its programming base time. When options are applied, a program has **two separate sizes**:

- **Actual size:** The space the program occupies on the cyberdeck.
- **Design size:** Used to determine the programming base time (and thus cost).

Options affect size in two ways:
1. An option may alter the program's **rating**, which changes the actual size derived from that rating.
2. An option may increase or decrease the program's size by a **percentage of its original size**. Some options reduce actual size but increase design size (requiring hyper-efficient code).

**Options which modify the effective rating do not count against the base rating.** Maximum program rating limits (MPCP cap) apply to the base rating only.

**When combining multiple options, apply in this order:**
1. Apply all **rating modifiers** first (before any size calculations).
2. Calculate program size based on the new rating.
3. Apply any **percentage size changes** sequentially -- each percentage change is applied to the result of the previous one, not the original size.

**Example:** A 180 Mp program receives two 50% size reductions. First: 180 -> 90. Then: 90 -> 45.

#### Options and Ratings

- Option-driven rating changes do **not** count against the programmer's maximum designable rating. A Computer-8 programmer can design a base rating-8 utility regardless of how high options push the effective rating.
- Option-driven rating changes do **not** affect the target number for the programming task. The TN is always based on the **base rating** (e.g., Slow-4 with Area-4 has a programming TN of 4, not 8).
- Options that have their own ratings (e.g., Area) are capped at the **base rating of the program**. A Slow-4 program cannot have higher than 4, even if the programmer's skill is higher.

#### Options and Cost

Program price is based on **base rating** and **design size**. The multiplier is determined by the program's base rating -- see the [Program Prices Table](#program-prices-table).

**Example:** Attack-6M (no options): base rating 6, design size 108 Mp -> 108 x 200Y = **21,600Y**. With a Skulk-4 option: effective rating 10, design size 300 Mp -> 300 x 200Y = **60,000Y** (multiplier still based on base rating 6).

| Option | Rating Modifier | Notes |
|--------|----------------|-------|
| **Area** | +Area Rating | Engages up to (Area Rating) targets simultaneously. Make one Attack Test and apply the result to all specified targets. Increase the target number for **each target** by the total number of targets being attacked. Armor utility provides extra protection against Area attacks: targets carrying Armor add +2 to their effective Armor rating when hit by an Area-option utility. |
| **Chaser** | +1 | Negates the +2 TN penalty for attacking IC with the **Shift** defensive utility. Adds a +2 TN penalty when attacking IC with the **Shield** defensive utility. Cannot be combined with Penetration. |
| **DINAB** | +DINAB Rating | "Decker In A Box." Gives the utility a built-in Computer skill equal to the DINAB rating. The decker may spend a Free Action to let the utility run itself for that action; the decker cannot also use the program during any phase it runs autonomously. DINAB degrades (-1 rating point) each time it fails a test (opposed System Test lost to host, fails to hit in cybercombat, or target reduces all damage to 0). If a DINAB-controlled program rolls all 1s on a failed test, it crashes -- reload via Swap Memory. Decker may override DINAB at any time and use their own Computer skill (normal action cost applies). Frames can carry DINAB; smart frames must have it. |
| **Limit** | -1 | Restricts the utility to one target type (e.g., deckers, IC programs, or frames); useless against all other types. Because the option reduces effective rating, it also reduces the program's actual size accordingly. |
| **One-Shot** | Special | The utility executes once, then vanishes. Reload via Swap Memory to reuse. Reduces actual size by 75%; increases design size by 50%. Multiple copies may be loaded in active memory simultaneously, but tar baby and tar pit IC wipe **all copies** from active memory when they crash a One-Shot utility. |
| **Optimization** | Special | Reduces actual size by 50%; increases design size by 100%. No effect on effective rating or performance. |
| **Penetration** | +1 | Defeats the **Shield** defensive utility. Against IC with the **Shift** defensive utility, the program suffers a +2 TN penalty -- in addition to the +2 penalty already granted by Shield. Cannot be combined with Chaser. |
| **Sensitive** | Special | Restricts the utility to one manufacturer's hardware; useless on all other manufacturers' systems. Programming requires using the average of Computer skill and Computer Theory (or Matrix Theory concentration) for the programming test. Reduces actual size by 75%; increases design size by 50%. |
| **Skulk** | +Skulk Rating | When this utility crashes an IC program, reduce the resulting security tally increase by the Skulk rating. *(Note: "Skulk" and "Stealth" are used interchangeably in the source material for this option.)* |
| **Squeeze** | +1 | Self-compressed program. Actual size is reduced by 50% for uploading purposes. Cannot be used until decompressed (Complex Action, no test required). If also uploaded via the Compression utility, size is reduced 75% total, but requires two separate decompression actions. The +1 rating modifier affects design size only, not actual size. The deck must have enough free active memory to hold the fully decompressed program. |
| **Targeting** | +2 | Provides a -2 TN modifier for all attacks made with this utility. |

### Command Sets

A command set is a simple program of orders left on a host to execute at a later time or in response to a trigger.

**Writing a command set** requires one or more System Tests based on the tasks it performs:

| Task | Required Test |
|------|--------------|
| Manipulate a remote device (open a door, trigger a device) | Slave Test |
| Print, erase, or edit a file | Files Test |
| Open a SAN | Access Test |
| Other host actions | Control Test (default) |

The **Deception** utility reduces TN for all of these tests.

**Complex sequences** (multi-step or conditional logic) require writing a dedicated program in advance and uploading it. Design size = 1D6 x 20 Mp. After uploading, the decker must succeed on a **Control Test** to load the program into the host.

**Detection and purge timer:** Total all successes the host scored opposing the subsystem tests. Divide 24 by that total -- the result is the number of hours the command set runs undetected before the host purges it. If the host scored no successes, the command set runs undetected for **48 hours**.

### Frames

Frames are combinations of decker-selected utilities, analogous to constructs (which combine IC). Frames can be:
- **Dumb frames:** Linked to the decker's persona. Exist only as long as the controlling decker is active on the host.
- **Smart frames:** Capable of independent existence in the Matrix, whether or not their creator is logged on.

**Frame Core:**

The frame core is the master control program for the frame:
- Size: Frame Core Rating^2 x Frame Core Multiplier (2 for dumb cores; 3 for smart cores).
- Core Ratings may not exceed the programmer's Computer Skill x 1.5 (round down).
- Combined ratings of Bod, Evasion, Masking, and Sensor may not exceed the Core Rating.
- Core Rating substitutes for MPCP Rating in any test requiring an MPCP Rating.
- For smart frames: Reaction = Core Rating.
- Combined ratings of all programs (not including options) in the frame may not exceed the Core Rating

**Frame options:** DINAB, optimization, and squeeze.

**Running a Frame:**

Dumb frames are deployed via a Decoy operation (see [System Operations](#system-operations)) or similar. Smart frames are uploaded to the host and run independently.

**Weapon Carrier Frames:** Dumb frames used to carry attack utilities. A simple weapon-carrier frame uses a Simple Action to fire. Smart weapon-carrier frames act independently on their own initiative.

### Programming

All programming follows the task rules:
1. **Calculate program size:** Rating^2 x Multiplier (from program description). See Program Size Table.  Include any options in this calculation that would change the Rating value.
2. **Calculate base time:** Program Size x 2 (in days).
3. **Make a Computer Test** (target number = program rating) to determine task period = Base Time / successes.  Use the base Program Rating for the Base Time test, not the utility augmented rating.
4. **Work through the task period.**

**Program Size Table (Rating^2 x Multiplier = size in Mp):**

| Rating | x1 | x2 | x3 | x4 | x5 | x6 | x7 | x8 | x9 | x10 |
|--------|-----|-----|-----|-----|-----|-----|-----|-----|-----|------|
| 1 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| 2 | 4 | 8 | 12 | 16 | 20 | 24 | 28 | 32 | 36 | 40 |
| 3 | 9 | 18 | 27 | 36 | 45 | 54 | 63 | 72 | 81 | 90 |
| 4 | 16 | 32 | 48 | 64 | 80 | 96 | 112 | 128 | 144 | 160 |
| 5 | 25 | 50 | 75 | 100 | 125 | 150 | 175 | 200 | 225 | 250 |
| 6 | 36 | 72 | 108 | 144 | 180 | 216 | 252 | 288 | 324 | 360 |
| 7 | 49 | 98 | 147 | 196 | 245 | 294 | 343 | 392 | 441 | 490 |
| 8 | 64 | 128 | 192 | 256 | 320 | 384 | 448 | 512 | 576 | 640 |
| 9 | 81 | 162 | 243 | 324 | 405 | 486 | 567 | 648 | 729 | 810 |
| 10 | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 | 1000 |
| 11 | 121 | 242 | 363 | 484 | 605 | 726 | 847 | 968 | 1089 | 1210 |
| 12 | 144 | 288 | 432 | 576 | 720 | 864 | 1008 | 1152 | 1296 | 1440 |
| 13 | 169 | 338 | 507 | 676 | 845 | 1014 | 1183 | 1352 | 1521 | 1690 |
| 14 | 196 | 392 | 588 | 784 | 980 | 1176 | 1372 | 1568 | 1764 | 1960 |

**Programming Tools and Bonuses:**

| Tool | Task Bonus | Cost |
|------|-----------|------|
| Personal computer (base) | 0 | 20Y/Mp memory |
| Personal computer (doubled memory) | +1 | 20Y/Mp memory |
| Programming kit | +1 | 1,500Y |
| Programming shop | +2 | 15,000Y |
| Mainframe host | +4 | 100Y x Security Value per day (5,000,000 x Security Value to purchase) |
| Mainframe access | 0 | 100Y x Security Value per day |
| Programming Suite | +5 | 300,000 to purchase |

**Maximum program ratings:**
- Persona programs and MPCP: no individual cap except MPCP Rating.
- Utility programs: cannot exceed the designer's Computer Skill (or Software Concentration, or Matrix Programming Specialization) rating x 1.5 (effectively, cannot exceed MPCP Rating when installed on a specific deck).
- Frame cores: cannot exceed programmer's Computer Skill x 1.5 (round down).

**Programming teams:**
- Team size limit: half the highest Computer Skill rating (rounded down).
- Maximum program rating the team can produce: 1 + highest Computer Skill in the team.
- Computer Test to determine task period uses the average of team members' skills (round up).
- Each team member must have their own minimum tools.
- Team task bonus = sum of all individual task bonuses - number of team members.

**Buying Programs:**

| Program Rating | Price | Availability | Street Index |
|---------------|-------|-------------|-------------|
| 1-3 | Size x 100Y | 2/7 days | 1 |
| 4-6 | Size x 200Y | 4/7 days | 1.5 |
| 7-9 | Size x 500Y | 8/14 days | 2 |
| 10+ | Size x 1,000Y | 16/30 days | 3 |

**Upgrading Programs:**

Any program (except command sets) may be upgraded by raising its rating, provided the programmer has a copy of the program's source code. Options may also be added to a program as an alternative to raising its rating.

Upgrading is a programming task. Determine the base time as follows:

1. Calculate the base time to write the **upgraded version** from scratch.
2. Calculate the base time to write the **current version** from scratch.
3. Subtract: `Upgrade Base Time = Upgraded Version Base Time - Current Version Base Time`

**Task period:** Make a Computer Test against the **upgraded program's rating**. Divide the upgrade base time by the number of successes -- the result is the task period in days. The rest of the process follows standard programming rules.

---

## System Operations

Every Matrix action is expressed as a system operation. Each operation has three components:
- **Test:** Which Subsystem Test the decker makes (Access, Control, Index, Files, or Slave), rolled against the host/grid's corresponding Subsystem Rating.
- **Utility:** The utility that reduces the target number for the Subsystem Test. Missing the right utility makes the operation harder but not impossible.
- **Action:** The type of game action required -- Free, Simple, or Complex.

**Action type guidelines:**
- **Free Action:** Very simple operations -- obtaining a single piece of information, manipulating a single control. Matrix equivalents of opening a door or looking out a window.
- **Simple Action:** Operations involving a single program, icon, or control.
- **Complex Action:** Any task involving a search, analysis, or control of a complicated or precise process.

**Security Test:** As part of every System Test, the gamemaster makes an opposed Security Test for the host/grid against the decker's Detection Factor (see [System Tests](#system-tests)).

### Interrogation Operations

During interrogation operations, the decker engages in a dialogue with the system, searching for specific information. The operation may need to be repeated until the target is located.

**Mechanics:**
- Track the decker's cumulative successes across repeated attempts.
- **5+ accumulated successes:** Objective located.
- The gamemaster may independently assign a different success threshold, or build a list of data to reveal as the decker reaches specific success totals.
- If the host does not have the information at all, reveal this after the decker accumulates **3+ successes**.

**Query precision modifiers (applied to TN):**

| Query Quality | TN Modifier |
|---|---|
| Extremely vague or general | +2 |
| Vague or general | +1 |
| Specific (default) | 0 |
| Well-phrased, relevant, or insightful | -1 or -2 |

Computers cannot lie -- only conceal. A decker who has gathered good intel and phrases the inquiry precisely gets a real mechanical advantage.

**Operations that are interrogations:** Locate Access Node, Locate File, Locate Paydata, Locate Slave, Dump Log.

### Ongoing Operations

Some operations continue running after the initial System Test without further input from the decker (uploads, downloads, etc.).

**Timing:** Time is measured in seconds per each operation's description. Convert to Combat Turns by dividing seconds by 3 -- **do not round fractions.**

| Upload Time | Combat Turns | Available |
|---|---|---|
| 6 seconds | 2 full CTs | Start of CT 3 after beginning |
| 7 seconds | 2 CTs + 1 sec remainder | Second action of CT 3 after the 2 CTs |
| 8 seconds | 2 CTs + 2 sec remainder | Third action of CT 3 after the 2 CTs |

When an ongoing operation interacts with other events, calculate the exact point within a Combat Turn that it completes.

**Operations that are ongoing:** Download Data, Upload Data, Locate Paydata.

### Monitored Operations

Monitored operations must be actively maintained after the initial System Test.

**Mechanics:**
- The decker must spend a **Free Action on every available action** to maintain the operation.
- If the decker fails even once to spend a maintenance Free Action, the operation **aborts** and the decker must repeat the full System Test to restart it.
- Aborting a monitored operation may have irreversible real-world consequences (e.g., aborting an Edit Slave that was masking a team's infiltration could expose them to guards).

**Operations that are monitored:** Control Slave, Edit Slave, Monitor Slave, Make Comcall, Tap Comcall.

### Complete System Operations List

| Operation | Test | Utility | Action | Notes |
|-----------|------|---------|--------|-------|
| **Analyze Host** | Control | Analyze | Complex | For each success, decker chooses one piece of info: host Security Rating, one subsystem rating, or whether host is a VM. 7+ successes reveals all available info. Decker must be logged on to the host (not the grid). |
| **Analyze IC** | Control | Analyze | Free | Identifies type, rating, options, and defenses of a located IC program. For trace IC: also reveals whether it is in hunt or location cycle, and turns remaining in the cycle. |
| **Analyze Icon** | Control | Analyze | Free | Scans any icon to identify its general type (IC, persona, frame, application, etc.). Decker reduces Control Test TN by Sensor Rating + Analyze utility rating; minimum TN of 2. |
| **Analyze Security** | Control | Analyze | Simple | Reveals current Security Rating of the host, the decker's security tally (including tally points accrued by this test), and the host's alert status. |
| **Analyze Subsystem** | Targeted Subsystem | Analyze | Simple | Identifies anything out of the ordinary on the targeted subsystem: trap doors, worm IC, scramble IC, and other defenses or system tricks. |
| **Control Slave** | Slave | Spoof | Complex | Monitored operation. Takes control of a remote device. For manufacturing or scientific processes, test with average of Computer + relevant B/R or Knowledge Skill. |
| **Crash Application** | Appropriate Subsystem | Crash | Simple | Shuts down one of the host's application programs (legitimate programs -- business processes, security installations, user sessions). Subsystem Test depends on the application targeted. No effect on IC, frames, constructs, or other deckers. |
| **Crash Host** | Control | Crash | Complex | On success, divide decker's successes into 10 = turns before host shuts down. At end of each turn, host makes Security Value Test vs. decker's MPCP to abort. During countdown, all IC ratings are reduced by 2; ratings return to normal if abort succeeds. Successful crash wipes all frames, command sets, and decker-left programs; host reboots, clearing all security tallies and alerts. |
| **Decrypt Access** | Access | Decrypt | Simple | Defeats scramble IC on a SAN. Must be performed before Logon to Host on a scrambled SAN. |
| **Decrypt File** | Files | Decrypt | Simple | Defeats scramble IC protecting a specific file. Must be performed before other operations on a scrambled file. |
| **Decrypt Slave** | Slave | Decrypt | Simple | Defeats scramble IC protecting a Slave subsystem. Must be performed before Slave Tests against a scrambled Slave subsystem. |
| **Decoy** | Control | Mirrors | Complex | Creates a decoy copy of the decker's icon. Record Control Test successes; when proactive IC attacks the decker, roll 1D6 -- if result < successes, IC attacks the decoy instead (ties go to the decoy). Decoys have no defenses, take full damage, and disappear when their Condition Monitors fill. Not effective against trace IC. Can be used to focus IC attention on frames. |
| **Disinfect** | Appropriate Subsystem | Disinfect | Complex | Destroys worm IC on a targeted subsystem. Test against the subsystem hosting the worm (e.g., Files Test for a Files subsystem worm). On failure, worm may infect the MPCP (see [Worms](#worms)). |
| **Download Data** | Files | Read/Write | Simple | Ongoing operation. Copies a file to the decker's cyberdeck at allocated I/O bandwidth. Terminating early produces a corrupted (worthless) copy. Gamemaster may allow partial recovery: reconstruction base time = (full file size / downloaded amount) x 2 days; chance of containing needed info = (downloaded / full) x 100%. |
| **Dump Log** | Control | Validate | Complex | Reads host access logs (identities of legal users, files accessed, programs run, intrusions). Logs may also be downloaded; 24-hour log size = multiplier x 100 Mp (Easy host: 2D6x5 Mp; Average: 2D6x2 Mp; Hard: 2D6 Mp). |
| **Edit File** | Files | Read/Write | Simple | Creates, modifies, or erases a datafile. After altering, inserting, or deleting a file: Computer Test (TN = Files Rating x 2; add Masking to Computer Skill) to determine if host notices. Can copy a file within the same host (Files Test + subsystem test for destination). To detect tampering in a file: Computer Test (TN = Files Rating x 2; add Sensor to Computer Skill). |
| **Edit Slave** | Slave | Spoof | Complex | Monitored operation. Modifies data sent to or received from a remote device (video signals, sensor readings, console data). |
| **Graceful Logoff** | Access | Deception | Complex | Safely disconnects from the Matrix without dump shock. On success, clears all traces of the decker from host security and memory systems, leaving decker invulnerable to trace IC after disconnecting. If trace IC is in progress, add its rating to the target number. |
| **Improvised Attack** | -- | -- | Simple | See [Cybercombat](#cybercombat). |
| **Invalidate Passcode** | Control | Validate | Complex | Erases a single passcode from the host's security tables. To wipe the entire passcode list: +4 TN modifier. |
| **Locate Access Node** | Index | Browse | Complex | Finds LTG codes for specific hosts; also locates commcodes for comm calls. TN modifier: broad goal +1; specific goal: no modifier; very specific goal: -1. Interrogation operation. |
| **Locate Decker** | Index | Scanner | Complex | Two-step: Index Test + Sensor Test. Locates other deckers whose Masking <= decker's Sensor Test result. If target runs Sleaze, add its rating to target's Masking for detection purposes. |
| **Locate File** | Index | Browse | Complex | Searches for specific datafiles. Decker must have a meaningful search goal. On success, decker knows the system location of the file. Interrogation operation. |
| **Locate Frame** | Index | Scanner | Complex | Locates smart frames or SK programs running on the host. Not effective against IC constructs -- use Locate IC instead. |
| **Locate IC** | Index | Analyze | Complex | System Test only -- no Sensor Test required; IC is auto-located if System Test succeeds. IC remains located unless it maneuvers to evade detection. |
| **Locate Paydata** | Index | Evaluate | Complex | Ongoing operation. Each net success locates 1 Paydata Point. Continues until stopped or all paydata found. Once located, paydata must be downloaded in its entirety. |
| **Locate Slave** | Index | Analyze | Complex | Finds system addresses for specific remote devices. Decker needs only 3 successes to locate the target. Once located, can perform Control Slave, Monitor Slave, etc. |
| **Logon to Host** | Access | Deception | Complex | Opposed Access Test vs. host Access Rating. Requires the LTG code. Trace from previous grid carries over to PLTG. If trace IC is running, add its rating to the TN. |
| **Logon to LTG** | Access | Deception | Complex | Opposed Access Test vs. LTG Access Rating. Jackpoint Access modifier applies; bandwidth Trace Factor modifier applies. On failure, security tally remains on grid (public LTGs remember unauthorized access for 1D3x5 minutes). Decker can switch jackpoints to start a fresh tally. |
| **Logon to RTG** | Access | Deception | Complex | Opposed Access Test vs. RTG Access Rating. Local LTG rating changes do not carry over to the RTG. RTG maintains the same security tally for all decker activity across all dependent LTGs and the RTG itself. |
| **Make Comcall** | Files | Commlink | Complex | Places a Matrix communications call. Decker can link calls across multiple RTGs for a conference call; each additional link requires another opposed Files Test. Trace routines on the call are treated as trace IC. Decker can detect taps with Sensor (Device Rating) Test and neutralize them with Evasion (Device Rating) Test. Monitored operation. |
| **Monitor Slave** | Slave | Spoof | Simple | Monitored operation. Reads real-time data from a remote device: audio pickups, cameras, medical scanners, etc. Provides constant updates while maintained. |
| **Null Operation** | Control | Deception | Complex | Performed while waiting. Security Value modifier by inactivity duration: <10 sec: base SV; <1 min: +1; <1 hr: +2; <12 hrs: +4; each additional 12 hrs: +1. |
| **Redirect Datatrail** | Control | Camo | Complex | Reduces the opposing Security Test TN by the decker's trace modifier (jackpoint Trace Factor). Decker can leave only one redirect per grid. Each redirect left on a grid reduces the decker's Trace Factor by 1 (does not affect bandwidth modifier's impact on further Redirect Datatrail tests). |
| **Retrain** | Access | Commlink | Free | Reallocates I/O bandwidth between icon bandwidth and I/O bandwidth. Can be performed at any time, even while loading data. |
| **Scan Icon** | Special | Scanner | Simple | Computer Test vs. target's Masking Rating. If target runs Sleaze: adjust TN by difference between Sleaze and Scanner ratings (reduce TN if scanner > sleaze; increase if sleaze > scanner). Each success: choose one -- MPCP Rating, any Persona Rating, or Response Increase Rating. |
| **Swap Memory** | None | None | Simple | Loads a utility from storage to active memory (or vice versa). If insufficient active memory, first spend a Free Action to unload a program. No tests required. Squeezed or Compressed utilities must be decompressed before use (Complex Action required). |
| **Tap Comcall** | Special | Commlink | Complex | Multi-step monitored operation. (1) Index Test to locate active commcodes on an LTG (must be on controlling RTG). (2) Control Test to trace call to origin/destination; each success on a conference call reveals one participant's commcode. (3) Files Test to record (1 Mp/minute). If scrambled: Computer Test vs. encryption rating (Decrypt reduces TN; +2 per retry). Dataline scanners: Computer Test vs. highest scanner rating, 1 success per scanner. Neither decryption nor scanner tests affect security tally. |
| **Upload Data** | Files | Read/Write | Simple | Ongoing operation. Transmits data from deck storage to the Matrix. New files written automatically; modifying existing files requires Edit File afterward. Not used for utilities -- use Swap Memory for that. |
| **Validate Passcode** | Control | Validate | Complex | Plants a fake passcode on a host. +2 TN for superuser passcode; +6 TN for supervisor passcode. On success: passcode lasts 1D6 x successes days. If decker uses the passcode during a run that triggers an active alert, the host flags and deletes it. |

---

## Cybercombat

### Participants

Cybercombat can involve: deckers, IC programs, smart frames (SK programs), and Artificial Intelligences (AIs). System resource icons and application icons cannot attack or be attacked directly (use system operations instead).

### Initiative

#### Decker Initiative

Standard Shadowrun Initiative rules apply. Base:
```
Reaction + 1D6 (base)
+ Response Increase bonuses (+1D6 initiative per level and +2 Reaction, up to a maximum +3D6 / +6)
+ Reality Filter bonus (+1D6)
+ Hot DNI bonus (+1D6 if running hot deck on pure DNI)
```

Cool deck: -1D6 Initiative when running cool with manual controls.

Tortoise: only 1D6 Initiative regardless of Response Increase.

Physical world actions (firing a gun, speaking verbally in a long statement) may interrupt Matrix actions, depending on the circumstances. A decker involved in a physical altercation while jacked in takes penalties.

#### IC Initiative

IC initiative is determined by the host Security Code:

| Host Security Code | IC Initiative |
|-------------------|--------------|
| Blue | IC Rating + 1D6 |
| Green | IC Rating + 2D6 |
| Orange | IC Rating + 3D6 |
| Red | IC Rating + 4D6 |
| Black | IC Rating + 5D6 |

Other programs (Smart Frames, SKs, other autonomous expert systems) have Reactions equal to their core ratings.  Roll 1D6 for initiative unless they have Reponse Increase.
For any other program not previously defined, assume they have Reaction equal to their ratings, and 1D6 initiative.  For programs without ratings, default reaction is 6.

### Actions

#### Free Actions

- Speak a word
- Delay action
- Buffer message (up to 100 words, transmitted to linked character at end of Combat Turn)
- Terminate download/upload
- Unload program (Releases active memory and Icon bandwidth for a swap memory operation.  No test required.)
- Unsuppress IC (Point added to Detection Factor.  Crashed IC rating gets added to security tally immediately.  If IC actions were suppressed, IC becomes active immediately.)
- Suspend/restore icon operations
- Turn reality filter on or off (takes effect start of next Combat Turn)

#### Simple Actions

- **Attack** (cybercombat attack with an offensive utility)
- **Combat Maneuver** (see [Combat Maneuvers](#combat-maneuvers))
- **Improvised Attack** (create a one-shot attack program on the fly -- see [Improvised Attacks](#improvised-attacks))

#### Complex Actions

- **Change Deck Mode** (if using optional Deck Modes rule)

#### Non-Combat Actions

A decker who wants to perform multiple non-combat tasks divides their reaction by 10 (round up).  Add 1 action for each initiative die the decker has beyond the standard 1D6.  The result is the number of actions the decker can take every turn.  Each Action can comprise 1 Complex Action, or 2 Simple Actions.  A Free action can take the place of one of the Simple Actions.

### Initiating Cybercombat

A decker may initiate combat with any icon that is **visible** or **located**.

**Visibility and location rules:**
- Any icon that attacks a decker automatically becomes visible, unless it successfully performs a combat maneuver to conceal itself.
- Reactive IC programs can be located via Analyze operations (see [System Operations](#system-operations)).
- Other deckers can be located via the Locate Decker operation.
- Other deckers may also make themselves visible by communicating, attacking, or deliberately revealing themselves.
- Once visible or located, an icon remains so until it succeeds at a combat maneuver to evade detection.

**Proactive IC:** May initiate combat with any decker whose security tally triggers the IC. The IC continues attacking until the decker logs off or evades detection via a combat maneuver.

### Combat Maneuvers

Combat maneuvers require an **opposed test** between two icons:

**Maneuvering icon:** Makes an **Evasion Test** (IC: Security Value dice vs. target = opposing icon's Sensor Rating). Cloak utility reduces target number.

**Opposing icon:** Makes a **Sensor Test** (IC: Security Value dice vs. target = maneuvering icon's Evasion Rating). Lock-On utility reduces target number.

If the maneuvering icon gets more successes: the maneuver succeeds. Net successes determine magnitude of effect. If the opposing icon ties or beats: maneuver fails.

Non-IC programs without Evasion/Sensor attributes cannot perform or oppose maneuvers.

#### Evade Detection

Evades an opposing icon that has detected the maneuvering icon. The maneuvering icon disappears from the opposition's view. IC re-detects an evaded icon after a number of Combat Turns equal to the net successes of the Evasion Test. Security tally increases shorten the evasion period by 1 turn each.

- To re-detect an evaded IC program: **Analyze Icon** operation.
- To re-detect an evaded decker/frame: **Locate Decker** operation.
- Cannot evade reactive IC during its location cycle.

#### Parry Attack

Enhances defenses. If the maneuvering icon wins, increase target numbers for attacks against it by the net successes. Bonus lasts until the next attack by the opposing icon. Bonus is lost if either icon performs an evade-detection maneuver.

#### Position Attack

Positions the icon for a better attack. Dangerous: if the maneuvering icon wins, it may either reduce the target number for its next attack by the net successes or increase the Power of its next attack by the net successes. If the opposing icon wins: that icon gets the bonus instead.

### Resolving Attacks

All cybercombat attacks are **Simple Actions**.

1. The attacker makes a test with the offensive utility program (Hacking Pool dice may be added).
2. Target number depends on the target icon's status (Intruding or Legitimate) and the host Security Code.

**Cybercombat Target Numbers Table:**

Column headers = **TN to hit an icon of that status**.

| Host Security Code | TN to Hit Intruding Icon | TN to Hit Legitimate Icon |
|-------------------|--------------------------|---------------------------|
| Blue | 6 | 3 |
| Green | 5 | 4 |
| Orange | 4 | 5 |
| Red | 5 | 6 |
| Black | 3 | 8 |

Any icon logged on with a valid passcode is **Legitimate**. All others are **Intruding**.

A decker can temporarily gain Legitimate status mid-run with a **Validate Passcode** operation, making himself harder to hit (attackers use the Legitimate column TN instead of the Intruding column TN). This does not affect System Tests. The host detects and deletes the faked passcode when the decker logs off.

A decker who logged on with a **genuine or pre-planted passcode** can use Legitimate status in combat against other intruding deckers without blowing his cover. The host only devalidates the passcode when the decker logs off or jacks out after using it against the host's own security programs.

Apply any additional modifiers from utility options, maneuvers, or damage.

### Improvised Attacks

A decker can write a one-shot attack program as a Simple Action:

1. The decker allocates points from Evasion and/or Bod ratings to set the attack Power. Power may not exceed MPCP Rating.
2. Those Evasion/Bod ratings are reduced immediately (until the attack is used or the current action ends if the decker fails to attack).
3. Make a **Computer Test** vs. target number = Power. Successes determine Damage Level:

| Successes | Damage Level |
|-----------|-------------|
| 1 | Light |
| 2 | Moderate |
| 3 | Serious |
| 4+ | Deadly |

### Icon Damage

**Programs that inflict standard damage** (attack, killer IC, etc.) have a Damage Code: Power = IC Rating; Damage Level = from the IC Damage Table.

See [IC Damage Level by Host Security](#cybercombat-summary-tables) in Reference Tables.

Stage up 1 Damage Level for every 2 successes on the attacker's Attack Test.

**Damage Resistance:** The targeted icon rolls a **Bod Resistance Test** (Bod Rating dice) against a target number equal to the Power of the attack. Armor utility reduces the Power. Stage down 1 Damage Level for every 2 successes on the Resistance Test.

### Condition Monitors

All icons use a **Condition Monitor** with 10 boxes.

**Condition Monitor Table:**

| Damage Level | Boxes Filled |
|-------------|-------------|
| Light | 1 box |
| Moderate | 2 boxes |
| Serious | 3 boxes |
| Deadly | 6 boxes |

When all 10 boxes are filled: the icon **crashes**. If it was a persona, the decker is dumped from the Matrix and is vulnerable to dump shock.

### Simsense Overload

When a decker's icon takes damage from **white or gray IC on a hot deck**, the decker may suffer Stun damage through ASIST resonance.

**Procedure:**
1. Make a **Willpower Test** against a target number based on the Damage Level taken by the icon.

See [Simsense Overload TN](#cybercombat-summary-tables) in Reference Tables.

- Running hot with DNI-only interface: +2 to TN.
- ICCM filter: -2 to TN.

If the Willpower Test fails: decker suffers 1 box of Stun damage on his Mental Condition Monitor.

Deadly icon damage crashes the icon automatically and exposes the decker to dump shock regardless.

Cool decks and tortoises are immune to simsense overload.

### Dump Shock

When a decker is **crashed off the Matrix** or jacks out without a Graceful Logoff, he risks Stun damage from dump shock.

**Dump Shock Damage Code:**
- Power = Host Security Value
- Damage Level = from the Dump Shock Damage Levels table

See [Dump Shock Damage Level by Host Security](#cybercombat-summary-tables) in Reference Tables.

**Modifiers:**
- Cool deck: -2 Power and Damage Level drops by 1 level.
- ICCM filter: -2 Power and Damage Level drops by 1 level.
- Both cool deck and ICCM: cumulative (-4 Power, -2 Damage Levels).
- Tortoise: immune to dump shock.

---

## Reference Tables

### Security Asset Response Times (when trace IC locates decker's jackpoint)

Results in **minutes**. "On-Site" = entry point inside a manned location owned by the system's owners. "Government" assumes a UCAS setting -- adjust for other governments. On-Site values are divided by 2 (security is already present).

| Jackpoint Security Rating | Public | Corporate | Megacorp | Government |
|---------------------------|--------|-----------|----------|------------|
| B or higher | 10 + 2D6 | 15 + 2D6 | 8 + 2D6 | 10 + 1D6 |
| C | 10 + 4D6 | 15 + 3D6 | 10 + 1D6 | 10 + 1D6 |
| D | 20 + 4D6 | 10 + 2D6 | 5 + 1D6 | 5 + 1D6 |
| Z | N/A | 10 + 1D6 | 5 + 1D6 | 5 + 1D6 |
| On-Site | N/A | 1D6 | 1D3 | 1D6 |

### Host Design Table Summary

| System | Security Code | Security Value | Subsystem Base |
|--------|---------------|---------------|----------------|
| Easy | Blue | 4-6 | 8-10 |
| Average | Green-Orange | 7-9 | 11-15 |
| Hard | Orange-Red | 8-12 | 13-18 |

### Log Size Multipliers

| Host Intrusion Difficulty | Log Size Multiplier (x 100 Mp per 24 hrs) |
|--------------------------|------------------------------------------|
| Easy | 2D6 x 5 |
| Average | 2D6 x 2 |
| Hard | 2D6 |

### Paydata Points Table

| System Security Code | Paydata Points Roll | Data Density Roll |
|---------------------|--------------------|--------------------|
| Blue | 1D6 - 1 | 2D6 x 20 Mp |
| Green | 2D6 - 2 | 2D6 x 15 Mp |
| Orange | 2D6 | 2D6 x 10 Mp |
| Red | 2D6 + 2 | 2D6 x 5 Mp |
| Black | 2D6 + 4 | 3D6 x 5 Mp |

**Base street value per Paydata Point:** 5,000Y.

### Sheaf Design Table Summary

| Trigger Step Interval | Security Code |
|----------------------|---------------|
| +4 (range 5-7) | Blue |
| +3 (range 4-6) | Green |
| +2 (range 3-5) | Orange |
| +1 (range 2-4) | Red |
| +1 (range 2-4) | Black |

### Program Prices Table

| Rating | Price | Availability | Street Index |
|--------|-------|-------------|-------------|
| 1-3 | Size x 100Y | 2/7 days | 1 |
| 4-6 | Size x 200Y | 4/7 days | 1.5 |
| 7-9 | Size x 500Y | 8/14 days | 2 |
| 10+ | Size x 1,000Y | 16/30 days | 3 |

### Deck Component Prices (quick reference)

All prices in nuyen. PF = Program Factor based on listed basis.

| Component | Formula | PF Basis |
|-----------|---------|----------|
| MPCP | MPCP^2 x [(8 x PF) + 195] | MPCP Rating |
| Bod or Evasion | Rating^2 x [(3 x PF) + 95] | Program Rating |
| Masking or Sensor | Rating^2 x [(2 x PF) + 75] | Program Rating |
| Active Memory | Mp x 7.5Y | -- |
| Storage Memory | Mp x 6Y | -- |
| ASIST (Hot) | (MPCP^2 x [(PF x 2) + 40]) + (MPCP x 50) | MPCP Rating |
| ASIST (Cool) | (MPCP^2 x [(PF x 2) + 20]) + (MPCP x 25) | MPCP Rating |
| Hardening | (Hardening^2 x [(PF x 8) + 160]) + (Hardening x 70) | MPCP Rating |
| ICCM Filter | (MPCP^2 x [(PF x 4) + 115]) + 5,000 | MPCP Rating |
| I/O Speed | Speed in MePS x 30Y | -- |
| Response Increase | [(MPCP^2 x Response) x (PF + 80)] + (Response x 105) | MPCP Rating |
| Satlink Interface | (MPCP^2 x [(PF x 2) + 40]) + (MPCP x 35) | MPCP Rating |

### Cybercombat Summary Tables

**Target Numbers by Icon Status and Host Security:**

Column headers = TN to hit an icon of that status.

| Host | TN to Hit Intruding | TN to Hit Legitimate |
|------|---------------------|----------------------|
| Blue | 6 | 3 |
| Green | 5 | 4 |
| Orange | 4 | 5 |
| Red | 5 | 6 |
| Black | 3 | 8 |

**IC Damage Level by Host Security:**

| Host | IC Damage Level |
|------|---------------|
| Blue | Light |
| Green | Moderate |
| Orange | Moderate |
| Red | Serious |
| Black | Serious |

**Condition Monitor Fill:**

| Damage Level | Boxes |
|-------------|-------|
| Light | 1 |
| Moderate | 2 |
| Serious | 3 |
| Deadly | 6 |

**Dump Shock Damage Level by Host Security:**

| Host | Dump Shock Damage Level |
|------|------------------------|
| Blue | Light |
| Green | Moderate |
| Orange | Serious |
| Red | Deadly |
| Black | Deadly |

**Simsense Overload TN (hot deck only, white/gray IC):**

| Icon Damage Level | TN |
|------------------|----|
| Light | 2 |
| Moderate | 3 |
| Serious | 5 |

(+2 TN if hot deck with DNI-only; -2 TN if ICCM equipped.)

### System Operations Summary Table

| Operation | Test | Utility | Action |
|-----------|------|---------|--------|
| Analyze Host | Control | Analyze | Complex |
| Analyze IC | Control | Analyze | Free |
| Analyze Icon | Control | Analyze | Free |
| Analyze Security | Control | Analyze | Simple |
| Analyze Subsystem | Targeted Subsystem | Analyze | Simple |
| Control Slave | Slave | Spoof | Complex |
| Crash Application | Varies | Crash | Simple |
| Crash Host | Control | Crash | Complex |
| Decrypt Access | Access | Decrypt | Simple |
| Decrypt File | Files | Decrypt | Simple |
| Decrypt Slave | Slave | Decrypt | Simple |
| Decoy | Control | Mirrors | Complex |
| Disinfect | Appropriate Subsystem | Disinfect | Complex |
| Download Data | Files | Read/Write | Simple |
| Dump Log | Control | Validate | Complex |
| Edit File | Files | Read/Write | Simple |
| Edit Slave | Slave | Spoof | Complex |
| Graceful Logoff | Access | Deception | Complex |
| Invalidate Passcode | Control | Validate | Complex |
| Locate Access Node | Index | Browse | Complex |
| Locate Decker | Index | Scanner | Complex |
| Locate File | Index | Browse | Complex |
| Locate Frame | Index | Scanner | Complex |
| Locate IC | Index | Analyze | Complex |
| Locate Paydata | Index | Evaluate | Complex |
| Locate Slave | Index | Analyze | Complex |
| Logon to LTG | Access | Deception | Complex |
| Logon to RTG | Access | Deception | Complex |
| Logon to Host | Access | Deception | Complex |
| Make Comcall | Files | Commlink | Complex |
| Monitor Slave | Slave | Spoof | Simple |
| Null Operation | Control | Deception | Complex |
| Redirect Datatrail | Control | Camo | Complex |
| Retrain | Access | Commlink | Free |
| Scan Icon | Special | Scanner | Simple |
| Swap Memory | None | None | Simple |
| Tap Comcall | Special | Commlink | Complex |
| Upload Data | Files | Read/Write | Simple |
| Validate Passcode | Control | Validate | Complex |

---

## Matrix Hot Spots

### NPC Decker Guidelines

**Inferior:** MPCP Rating = player decker's -2; Response Increase = player decker's -1.
**Equal:** All ratings = player decker's.
**Superior:** MPCP Rating = player decker's +2; Response Increase = player decker's +1.

All persona programs (BEMS) at maximum (3/4 of MPCP, rounded down) for corp/government deckers. Without a Masking program, all four programs equal the MPCP Rating.

All utilities at maximum value = MPCP Rating.

Standard loadout: Armor, Attack, Cloak, Lock-On.

- Inferior: No self-repair programs.
- Equal: Matches player decker's capabilities.
- Superior: Medic and Restore.

Systems where deadly force is expected: NPC deckers may carry Black Hammer or Killjoy.

Government deckers specialize in track programs (Matrix law enforcement).

NPC deckers on their own systems use Legitimate icons (IC does not attack them). Intruding deckers use the Legitimate target numbers column to attack these NPCs.

### Ares Macrotechnology -- Regional Sales

**Architecture:** Tiered (Open Access -> Chokepoint -> Hub-and-Spoke -> Secure Host). Transaction packets between hosts pass through heavily loaded chokepoints. Working mainframes are IC-free for efficiency; chokepoints carry the security load.

**Host A** (Salesroom/Open Access)
- Rating: `Green-5/8/10/8/10/10`
- Paydata: 0
- Standard office/UMS iconography. Reality filters dominate automatically. Viewing sales files and promos does not raise the security tally. SAN to Host B visible via successful Analyze Access operation.

| Trigger Step | Event |
|-------------|-------|
| 6 | Probe-6 |
| 11 | Trace-7 |
| 16 | If jackpoint not located: Trap Trace-8 (Killer-7); If jackpoint located: Passive Alert |
| 21 | Expert Killer-7/Offense +2 |
| 25 | Active Alert |
| 31 | Blaster-7 (Armor) |
| 35 | Trap Probe-7 (Blaster-6 (Armor)) |
| 40 | Shutdown |

**Host B** (Chokepoint)
- Rating: `Orange-10/14/15/16/14/18`
- Paydata: 0
- Standard UMS icons. Reality filter provides advantage.
- Security tally accumulates throughout the entire run, even while on other hosts. Passive IC pauses when decker moves to another host and resumes on return. Active IC follows the decker to any host in the network.

| Trigger Step | Event |
|-------------|-------|
| 4 | Trace-10 |
| 7 | Probe-8 |
| 11 | Trap Probe-10 (Killer-8) |
| 16 | Passive Alert |
| 19 | Acid-10 (Armor, Shifting) |
| 22 | Expert Blaster-12/Defense +1 |
| 26 | Active Alert |
| 30 | Expert Construct/Offense +2 (Armor), Blaster-7, Acid-5, Tar Baby-4 |
| 35 | Black IC-8 (Armor) |
| 38 | Shutdown |

**Network C** (C1-C4, second-tier hosts)
- Rating: `Green-7/12/13/15/12/13`
- C1 (Accounting): Paydata 8
- C2 (Tech Support): Paydata 5
- C3 (Sales Management): Paydata 6
- C4 (Maintenance): Paydata 4
- Paydata Density: 2D6 x 15 Mp
- Passive IC shuts down when decker logs off a C host. Active IC pursues to another C host or back to Host B. Security tallies persist per host (e.g., tally of 4 on C1 resumes at 4 on return).
- C1 and C2 have PLTG gateways in their Access subsystems; protected by Scramble IC -- must Decrypt to log on to the PLTG.
- C4 trap door to Host D rotates randomly through all subsystems nanosecond-by-nanosecond; must search for it on every visit.

| Trigger Step | Event |
|-------------|-------|
| 5 | Construct (Armor), Killer-5, Probe-2, Trace-5 |
| 9 | If jackpoint not located: Trace-6; If jackpoint located: Killer-6 |
| 13 | Passive Alert |
| 18 | Mark-Rip-7 |
| 24 | Blaster-6 |
| 29 | Active Alert |
| 33 | Sparky-7 |
| 37 | Expert Black IC/Offense +2 |
| 42 | Shutdown |

**Host D** (Executive files and security node)
- Rating: `Red-9/15/14/16/14/16`
- Paydata: 11
- Paydata Density: 2D6 x 5 Mp
- 2-in-6 chance any given slave system is rigged with a Data Bomb-6.
- Sculpted as a giant chess game: pawns = Probe IC, knights = Trace IC, queen = Black IC.

| Trigger Step | Event |
|-------------|-------|
| 3 | Construct (Shifting), Killer-6, Trace-6, Tar Baby-4 |
| 5 | Probe-8 |
| 8 | Killer-8 |
| 10 | Passive Alert |
| 14 | Sparky-10 |
| 16 | Binder-8 |
| 19 | Black IC-10 (Armor) |
| 22 | Shutdown |

### Shiseki Clan

**Overview:** Mid-level Yakuza syndicate, Seattle area. Smuggling, industrial espionage, and secure communications services. Aggressively pursues, terminates, and makes examples of anyone who decks their systems -- including accomplices and buyers of stolen data.

**Tri-Marine Exports** (cover operation/front)
- LTG: 1206
- Rating: `Green-4/10/9/10/8/9`
- Paydata: 0
- Appears as a normal small business until provoked. At trigger 19, a bouncer upgrades security to Red-9 and switches from UMS to sculpted (hell/underworld legends: western demons, Greek Furies, Egyptian Eater of Souls, Dante's Inferno, Taoist hells, etc.).
- The subsystem holding the trap door to the Shiseki Clan Host is infected with data worm IC. The trap door uses mimetic routines and can reside in any subsystem.

| Trigger Step | Event |
|-------------|-------|
| 4 | Probe-8 |
| 9 | Probe-8 |
| 15 | Probe-8 *(if multiple Probe IC are running, all attempt to raise the security tally on each operation)* |
| 19 | Bouncer: upgrade Security Code to Red-9; switch to sculpted IC (hell/underworld legends metaphor) |
| 21 | Passive Alert |
| 23 | Killer-6 |
| 27 | Active Alert |
| 30 | Cascading Psychotropic Black IC-8 (Judas Syndrome) *(alt: Cascading Black IC-8 if Psychotropic not in use)* |
| 33 | Shutdown |

**Shiseki Clan Host** (real operations computer)
- Rating: `Red-10/16/18/14/16/14`
- Paydata: 13
- Paydata Density: 2D6 x 5 Mp
- Military history metaphor; constantly switches historical periods, making preset MPCP iconography nearly impossible.
- IC always appears in keeping with the active metaphor (another figure in the combat setting). Until IC lands a damaging attack, the decker may believe he is making a System Test rather than being attacked.
- **All secure datafiles (including all paydata) are loaded with data bombs.**
- The Slave subsystem has no function on this host.

**Subsystem Metaphors:**

| Subsystem | Historical Metaphor |
|-----------|-------------------|
| Access | Martial Arts / Japanese military history |
| Control | Classic Greek or Roman |
| Index | American Civil War |
| Files | Medieval |
| Slave | World War II |

| Trigger Step | Event |
|-------------|-------|
| 4 | Construct (Armor), Probe-6, Trace-6, Killer-6 |
| 5 | Trace-10 |
| 8 | Passive Alert |
| 10 | Trap Probe-8 (Cascading Blaster-6) |
| 14 | Tar Pit-10 |
| 18 | Active Alert |
| 21 | Construct (Expert Offense +2 (Shifting)), Killer-7, Blaster-7, Tar Baby-2 |
| 24 | Blaster-10 (Armor, Shielding) |
| 27 | Black IC-8 |
| 31 | Shutdown |

### Federal Records

**Architecture:** Multi-tier; non-secure (connects to public grid). This represents typical UCAS offices outside Washington D.C. High-security sites (IRS, FBI, black military) keep secret data on machines with no grid connection.

**Host A** (Public Access)
- Rating: `Blue-4/8/10/9/9/8`
- Paydata: 2
- Paydata Density: 2D6 x 20 Mp
- Plain UMS iconography; bureaucratic quality. Slave systems control building amenities. Paydata only in large, bulky packages (near-public records).

| Trigger Step | Event |
|-------------|-------|
| 6 | Display of penalties for unauthorized access (also shown at logon; software re-displays whenever it suspects activity) |
| 11 | Probe-5 |
| 18 | SIN/comm code verification display. If ignored >10 seconds: Trace-8 triggered. If decker submits false info without a successful Control Test: Trace-8 triggered. Icon can be killed but counts as Passive IC for security tally. |
| 25 | Active Alert |
| 30 | Trap Probe-6 (Blaster-7) |
| 37 | Federal/local Matrix law enforcement alerted; government decker arrives in 2D3 turns |
| 44 | Shutdown |

**Host B** (Day-to-day operations)
- Rating: `Green-8/12/13/14/12/13`
- Paydata: 6
- Paydata Density: 2D6 x 15 Mp
- Routine office records. Low-level employee private files stored here (illegally). Confidential-but-not-secret personnel or operational records also here. Secure operational files on Host D.

| Trigger Step | Event |
|-------------|-------|
| 4 | Probe-7 |
| 10 | Trap Trace-6 (Killer-8) |
| 15 | Construct (Armor), Acid-6, Blaster-6 |
| 20 | Passive Alert |
| 24 | Marker-7 |
| 29 | Blaster-8 (Armor and Shifting) |
| 34 | Active Alert; government decker arrives in 2D3 turns |
| 39 | Shutdown |

**Host C** (Chokepoint between Host D/PLTG and public grids)
- Rating: `Orange or Red-11/14/15/17/16/18`
- Paydata: 0
- Highly secure offices use Red (authorized for lethal Black IC). Both configurations share the sheaf below.

| Orange Step | Red Step | Event |
|------------|----------|-------|
| 4 | 3 | Probe-8; disclaimer display (Red also displays "Use of Deadly Force Authorized") |
| 9 | 7 | Tar Baby-8 |
| 12 | 9 | Trap Trace-10 (Killer-8) |
| 16 | 12 | Passive Alert |
| 21 | 16 | Expert Construct (Armor, +2 Defense/-2 Offense), Trace-8, Tar Baby-4, Marker-5 |
| 24 | 18 | Cascading Blaster-8 |
| 28 | 21 | Active Alert (Orange: government decker arrives in 1D3 turns; Red: arrives next turn) |
| 31 | 23 | Expert Construct (Armor and Shielding, +2 Offense/-2 Defense), Black IC-8 (non-lethal/lethal), Acid-6 |
| 36 | 27 | Cascading Black IC-7 (non-lethal/lethal) |
| 39 | 29 | Shutdown |

**Host D** (Sensitive government data + PLTG gateway)
- Rating: `Green-10/17/18/13/15/14`
- Paydata: 9
- Paydata Density: 2D6 x 15 Mp
- Access subsystem protected by Scramble IC (must Decrypt before logging on).
- All secure datafiles protected by Scramble IC, data bombs, or worms.
- Records distributed to PLTG: erasing or modifying them requires an additional, extremely dangerous run through the government grid.

| Trigger Step | Event |
|-------------|-------|
| 5 | Trap Probe-10 (Killer-11) |
| 9 | Party IC, Tar Pit-4, Killer-10, Marker-6 |
| 15 | Trap Trace-8 (Sparky-10) |
| 20 | Passive Alert |
| 24 | Probe-11 |
| 28 | Construct (Armor), Killer-7, Acid-7, Probe-4 |
| 33 | Active Alert; government decker arrives in 1D3 turns |
| 39 | Party IC, Bind-rip-5, Acid-rip-5, Jam-rip-5, Mark-rip-5 |
| 43 | Cascading Psychotropic Black IC-9 (Cyberphobia) *(alt: Cascading Black IC-9 if Psychotropic not in use)* |
| 48 | Shutdown |

---

*End of VR 2.0 Rules Reference. All content extracted from Shadowrun 2nd Edition: Virtual Realities 2.0, pages 22-27, 32-61, 68-77, 84-85, 90-99, 102-132, 157-172.*
