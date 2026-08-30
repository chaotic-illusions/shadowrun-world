# Converting Mercurial's SR1 Matrix Hosts to VR2.0

Mercurial is an SR1-era adventure. Its Matrix sections describe each host as a
**chain of individual nodes** (SAN, SPU, Datastore, CPU, Slave Module), each
with its own color-coded rating and its own attached IC. This app's Matrix
Designer implements **VR2.0** (the SR2 sourcebook), which collapses all of
that into **one host** with a single Security Code/Value, five ACIFS
subsystem ratings, and a security sheaf (tally-triggered IC events). See
`docs/vr2_rules.md` for the full ruleset.

This is a suggested conversion, not a build — nothing below has been created
in the Matrix Designer yet. Numbers are starting points; tune them to your
table.

## The core translation

**One SR1 host chain -> one VR2 `MatrixHost` record.** Don't try to recreate
the node-by-node topology as separate hosts — build one host and let its
ACIFS ratings carry the "shape" of the original chain:

| SR1 node role | VR2 ACIFS subsystem | Why |
|---|---|---|
| SAN (entry node) | **Access** | Both gate initial log-on. |
| SPU / "Barrier" rating | **Control** | Both represent systemwide administrative/defensive infrastructure. |
| Datastore | **Files** | Direct match — both govern read/write/edit/delete on stored data. |
| Slave Module(s) | **Slave** | Direct match — both govern remote device/peripheral control. |
| CPU | **Control** (usually) or the host's overall **Security Value** | The CPU is typically the "final boss" node; let its rating anchor the host's overall toughness. |
| *(no SR1 equivalent)* | **Index** | SR1 didn't track "finding the file" separately. Estimate as roughly the average of Access and Files, adjusted up if the book describes multiple decoy/hidden datastores. |

**Security Code (color):** use the color that best represents the host's
*overall* character, not necessarily the single highest node — a small host
with one nasty Red datastore buried in mostly-Green infrastructure should
usually stay Green or Orange overall, with that toughness showing up in the
Files rating and sheaf instead. Reserve Red for hosts the book clearly means
to be a top-tier target.

**Security Value:** generally anchor this to the deepest/CPU node's rating.
For hosts with many nodes (a long original chain), consider nudging the
Security Value **up 1-2 points** from the source's peak number — a single
VR2 Security Value has to represent the *cumulative* difficulty of a chain
that used to make the decker clear several separate node challenges in
sequence. This is called out explicitly per host below.

## IC name mapping

Good news: VR2 kept most SR1 IC names as-is. Translation is mostly direct:

| SR1 term | VR2 equivalent | Notes |
|---|---|---|
| Killer | **Killer** | Same mechanic (proactive damage IC). |
| Scramble | **Scramble** | Same mechanic (protects specific files/subsystems). |
| Tar Pit | **Tar Pit** | Same mechanic (crashes + corrupts utilities). |
| Black IC | **Black IC** | Same mechanic; pick Lethal or Non-Lethal per book context. |
| Trace & Dump / Trace-Burn | **Trace IC** | The "dump"/"burn" flavor folds into Trace IC completing its Location Cycle (physical response dispatched); pair with Blaster as **Trap IC** if the book implies deck damage on top. |
| Blaster | **Blaster** | Same mechanic (Gray IC, permanent MPCP damage). |
| "Barrier N" node rating | *(not an IC)* | This is the node's own defense rating, not a program — fold it into Control or the host's Security Value, don't build it as IC. |
| Named guardian icons (oni, Fu-dog, guardian-warrior, etc.) | **Construct / Party IC** | Build the mechanical IC normally (pick component programs + ratings) and keep the flavor name in the host's `notes` field — the engine doesn't carry a display name per IC. |
| A hired human decker guarding the system (e.g. Gum E. Bear) | Not IC at all — an **enemy decker** | This app already generates tier-appropriate enemy deckers off a host's Security Code/Value (`generate_enemy_decker`). Use that instead of trying to represent a person as IC. |

## Structural gimmick: linked hosts (Taetzel Building)

The Taetzel Building's two systems ("System A" building control, "System B"
Dragon Knights' private mainframe) are connected through "a special
security-interface SPU bridging into System A" — concealed behind a
subsystem other than Access. That is **exactly** VR2's Trap Door rule
(`docs/vr2_rules.md` -> Grids and Hosts -> System Tricks -> Trap Doors): a
hidden connection controlled by a subsystem other than Access, requiring an
Analyze Subsystem to find and a Graceful Logoff to use.

Build this as **two separate `MatrixHost` records**, with System A's
`trap_doors_json` pointing at System B and System B flagged
`is_trap_door_dest`. No approximation needed here — the rules line up
natively.

---

## Per-host conversions

### 1. Federated Funds Net (Mercurial pp.18, 35)
Small 4-node "piggy bank" host — the adventure's easiest decking job.

- **Security Code / Value:** `Orange-4` (Easy band). Keeping Orange rather
  than pushing to Red for the Datastore's rating matches the fiction ("small,
  rinky-dink" bank); the sensitivity shows up in Files below.
- **ACIFS:** Access 4 &middot; Control 3 &middot; Index 4 &middot; Files 5 &middot; Slave 3
- **Sheaf (Orange interval, roughly every 3-5 tally):**
  - Trigger ~4: Scramble-3 (per-account file protection, matches the book's "each account Scramble 3")
  - Trigger ~8: Killer-4 (the CPU node's rating)
  - Trigger ~12, Active Alert: shutdown sequence begins (the book is explicit: External Alert -> 2D6-turn shutdown countdown)

### 2. Max Foley's System (pp.39-41)
7 nodes, includes a public/decoy Datastore alongside the real blackmail files, guarded by a hired decker.

- **Security Code / Value:** `Orange-6` (top of Easy / edge of Average — riskier than the bank, still beatable).
- **ACIFS:** Access 4 &middot; Control 5 &middot; Index 5 &middot; Files 5 &middot; Slave 4
- **Notes:** Represent Gum E. Bear as an enemy decker at this host's tier
  rather than as IC — he actively defends and dump-shocks intruders per the
  text.
- **Sheaf:**
  - Early: Killer-5 (Gray) on the trapped access node
  - Mid: Trace-4 tied to the private (real) Datastore
  - Active Alert: Gum E. Bear logs on to respond directly

### 3. New Horizons Development (p.51)
Deliberately a dead end — legit filings only, phone-accessible only.

- **Security Code / Value:** `Blue-4` (floor of the scale).
- **ACIFS:** flat ~4 across the board (Blue = "little or no security").
- **Notes:** No public SAN — mark this host's LTG as **unlisted/black**
  (same disposition concept already used on org LTG catalog entries) so
  players must discover the phone number rather than finding it on a
  directory. Minimal sheaf; one Reactive Trace around tally 5-7 is enough.

### 4. Sorayama's Clinic, Chiba (pp.54-55)
9 nodes, samurai/castle theme, mostly Red — the richest host in the book.

- **Security Code / Value:** `Red-8`. The source's peak explicit number is
  6 (the CPU's Trace-Burn), but 9 defended nodes compound into more than a
  flat 6 once collapsed to one host — bumped to 8 to keep it a genuine
  "Average-to-Hard" fight rather than undersell the original gauntlet.
- **ACIFS:** Access 5 &middot; Control 5 &middot; Index 6 &middot; Files 7 &middot; Slave 5
- **Sheaf** (tight Red interval, every 2-4 tally):
  - ~4: Reactive Trace ("temple watchmen" flavor)
  - ~8: Killer-4 ("guardian warrior" armory SPU)
  - ~12: **Tar Pit** on the scroll-house Datastore protecting Maria's file — direct name match, no translation needed
  - ~16, Active Alert: **Black IC-5** on the R&D Datastore — direct match
  - ~20: Construct/Party IC built from a Killer+Black IC pair, flavored as "oni and Fu-dog" in the host's notes
  - On Active Alert: spawn a "Major League" yakuza enemy decker (or two) at this host's tier

### 5. Taetzel Building — System A (building control) (pp.57-64)
Public-facing building systems; everything except the 28th floor.

- **Security Code / Value:** `Orange-7` (Average band) — the outer shell of
  a disguised black site.
- **ACIFS:** Access 4 &middot; Control 5 &middot; Index 5 &middot; Files 4 &middot; Slave 7
  (Slave carries the weight here — servoguns, cameras, elevators all live
  on this subsystem, matching the book's explicit Slave Modules Orange-7)
- **Trap door:** `trap_doors_json` -> System B, gated behind the **Slave**
  subsystem specifically (matches the book's own description of the bridge).

### 6. Taetzel Building — Dragon Knights Mainframe / System B (pp.58-60)
The adventure's true climax host: mission briefing, cadre dossiers, security clearances.

- **Security Code / Value:** `Red-8`. Source peak is 7 (the CPU); bumped to
  8 for the same "collapsed-chain" reasoning as Sorayama's clinic, and
  because this is meant to be the hardest system in the book.
- **ACIFS:** Access 6 &middot; Control 5 &middot; Index 5 &middot; Files 6 &middot; Slave 4
- **Trap door:** flagged `is_trap_door_dest` (entered from System A).
- **Sheaf:**
  - Mid: **Blaster** on the SPU — direct match, permanent deck damage
  - Late, Active Alert: **Black IC-5** on the CPU — direct match, the book's real final boss IC
- **The "Security Terminal that hides operator detection"** isn't a clean
  IC translation — model it as a human response instead: once Active Alert
  fires, **Lin Hwang** (already built as a Person of Interest, stats in his
  notes: Fairlight Excalibur, MPCP 6, Attack 7) logs on to fight the
  intruder directly from his quarters one floor away.

---

## Suggested build order

Federated Funds Net first (smallest, cleanest test of the conversion),
then Foley's system, then the Taetzel Building pair together (build System A
and System B in the same sitting so the trap door wiring is fresh), and
Sorayama's clinic last (the most involved sheaf). New Horizons Development
can be built anytime — it's nearly configuration-free.

Say the word when you want any of these actually built in the Matrix
Designer and I'll create the host records with these starting numbers.
