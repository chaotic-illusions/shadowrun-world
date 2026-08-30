# Mercurial — Prep Notes: NPCs, Locations, Organizations, Matrix Systems

Compiled from a full read-through of `docs/SR_Mercurial.pdf` (78 pages).
Everything below is meant to be entered as **inactive/undiscovered** and
flipped active as the party encounters it in play (see
`docs/todo_active_inactive_toggles.md` for the toggle work this depends on).

**Status (2026-08-30): all Locations, NPCs, and Organizations listed below
are loaded into the live campaign DB, flagged `is_active: false`.** Matrix
hosts are not built yet — see `docs/mercurial_matrix_conversion.md`.
Existing world entities were reused rather than duplicated: "Underworld 93"
and "Aztechnology Pyramid" (locations) and "Aztechnology" (org, id 1)
already existed before this prep. Locations/NPCs tied to Perfekto Polymers,
Shigeda-gumi, or Dragon Knights were relinked from the Aztechnology stand-in
to their real orgs once those were created.

Entries are split into **Core** (named, plot-relevant, worth a real record)
and **Flavor/Optional** (one-off names, mostly there for color — add only if
you want maximum texture; skip without losing anything mechanically important).

---

## Plot synopsis (short version)

Maria Mercurial, Seattle's biggest rock star, was five years ago the
memory-wiped mistress of Aztechnology exec Reynaldo Texamachach. Before his
secretary murdered him, he hid a devastating report in Maria's sealed memory:
proof that Aztechnology subsidiary **Perfekto Polymers** illegally dumped
toxic waste in the Barrens, a crime a Greenwar eco-terrorist cell nearly
exposed. **New Horizons Development** — a real-estate front secretly owned by
the **Shigeda-gumi** yakuza — is buying up the poisoned Barrens land cheap and
has threatened to expose Perfekto unless Aztechnology pays up or hands over
the waste site's location, which only exists inside Maria's head.

Aztechnology sends corporate fixer **Kyle Morgan** and his "Dragon Knights"
team, with yakuza mage **Sumiko Hotoda** as liaison, to solve the problem by
kidnapping Maria and framing her manager **Armando Hernandez** for it — while
Shigeda loan sharks blackmail rival agent **Max Foley** (who Maria dumped
Hernandez for) into helping. The player characters are hired by Foley,
ostensibly as Maria's bodyguards, and get pulled into the yakuza kidnap
attempt, Hernandez's frame-up, and ultimately Aztechnology's cover-up —
climaxing at the Dragon Knights' hidden base, the **Taetzel Building**, guarded
by Morgan's dragon partner **Perianwyr**.

---

## Matrix Systems — how many need to be built

**6 systems get real node maps/security ratings in the book and are worth
building in the Matrix designer:**

1. **Federated Funds Net** — small bank holding Hernandez's account. 4 nodes
   (SAN/SPU/Datastore/CPU). Early, low-stakes decking job (redirect/expose
   Hernandez's 180,000¥). *(pp. 18, 35)*
2. **Max Foley's system ("SAN")** — 7 nodes, guarded by decker Gum E. Bear.
   Holds Foley's blackmail files, Hotoda's recorded threat message, bank
   interface. *(pp. 39-41)*
3. **New Horizons Development** — minimal, phone-only "Blue"-rated network.
   Deliberately kept clean — only legit zoning/PR filings, since the real
   business is off-Matrix on purpose. Good "dead end" system for players who
   go looking. *(p. 51)*
4. **Sorayama's clinic (Chiba)** — 9 nodes, samurai/castle-themed IC. Holds
   Maria's original modification records under her old identity "Maria
   Aguilar." Can summon yakuza decker backup on alert. *(pp. 54-55)*
5. **Taetzel Building mainframe ("System A")** — the building's general
   control system (non-28th-floor systems, security net, servoguns).
   Interconnects with System B. *(pp. 58-60, 62)*
6. **Dragon Knights' mainframe ("System B")** — Kyle Morgan's private mission
   system. Holds the mission briefing, Aztechnology resource list, Dragon
   Knights personnel dossiers, security clearances, armory inventory. The
   "big" late-game host. *(pp. 58-60)*

**Not worth building as full hosts** (mentioned but no node map given, or too
minor to matter mechanically) — handle these as flavor/GM fiat if players poke
at them:
- Hernandez's home/office computer (referenced only, "GM runs it via
  passcodes")
- Underworld 93's lighting/sound control console (local A/V rig, not a host)
- Maria's condo home-automation system (flavor — she avoids it anyway)
- Sidney Murdoch's office camera feed (unrated internal surveillance)
- Lin Hwang's personal cyberdeck (an NPC's gear, not a target system)

---

## NPCs (Persons of Interest)

### Core cast
| Name | Role |
|---|---|
| Maria Mercurial | Amnesiac rock star protagonist; alternates Amazon/Schoolmistress/Innocent personas; former identity "Maria Aguilar" |
| Armando Hernandez | Maria's manager, rescued her from a Barrens/Aztlan brothel as a teen, genuinely loves her, framed for BTL trafficking |
| Max Foley | Rival agent who poached Maria's contract; secretly ¥500,000 in debt to the Shigeda-gumi; hires the PCs |
| Reynaldo Texamachach | (Deceased) Aztechnology exec, Maria's former owner/lover; hid the Perfekto data in her memory |
| Sumiko Hotoda (alias "Kathy Sakura") | Shigeda-gumi kobun mage; leads the kidnap plot; killed by Perianwyr |
| Kyle Morgan | Aztechnology fixer, leads the "Dragon Knights"; empathically bonded to Perianwyr; secretly sympathetic to Maria |
| Perianwyr | Western Dragon, Morgan's partner; lairs on the Taetzel Building roof; ambivalent about the mission |
| Jorge Mixacopotec | Dragon Knights security chief, scarred Aztlan merc; killed by Morgan at the climax |
| Blackstone | Dragon Knights technomancer (dwarf); coerced — Aztechnology holds his family hostage |
| Lin Hwang | Dragon Knights decker; ex-Macao Triad, hiding from his old gang |

### Supporting
| Name | Role |
|---|---|
| Sidney Murdoch | Owner of Underworld 93 |
| Newt | Troll bouncer at Underworld 93, loyal to Foley |
| Tellin | Elf bartender/fixer/medic at Underworld 93, info broker |
| Sorayama | Chiba cyberware artist who modified Maria for Texamachach |
| Johnson-san | Aztechnology handler who originally commissioned Maria's mods |
| Dr./Ms. Kenner | Maria's therapist |
| Toroshi | Shigeda loan shark holding Foley's debt |
| Gum E. Bear | Decker hired by Foley to plant evidence on Hernandez |
| Snout | Ork informant who sells hideout locations to Morgan |
| Andrew Masterson | Perfekto Polymers CEO (found dead — news handout) |
| Miguel Allende | Perfekto Polymers Seattle GM (missing — news handout) |
| Margot Tipper | Chairwoman, Citizens for a Decent Society Policlub |

### Flavor/optional (skip unless you want extra texture)
Beauty Shannon (simsense star linked to Morgan), Johnny Disk (reporter),
Warren Cartwright (musician friend of Maria), Zango Wilkes (deceased singer,
namedropped for tone).

---

## Locations

### Core
| Name | Notes |
|---|---|
| Underworld 93 | Seattle nightclub where Maria performs; includes backstage complex |
| Federated Funds Net (offices) | Small bank handling Hernandez's account |
| Rent-a-Hideout warehouse | Rentable Barrens safehouse the party can use |
| Star Gardens Endominium | Maria's ¥1.5M penthouse condo, downtown Seattle |
| The Barrens (Seattle) | Slum district; site of the hideout, the old Perfekto plant, New Horizons' land grab |
| Hernandez's brownstone/office | His home and recording studio |
| Taetzel Building | Dragon Knights' hidden HQ (28-story derelict tower); includes 28th floor and roof/helipad (Perianwyr's lair) |
| Old Perfekto Polymers plant | Abandoned factory tied to the waste-dumping scandal |
| Sorayama's clinic (Chiba) | Off-map (Japan) — reachable via Matrix/travel for the cyberware-records subplot |
| Aztechnology Pyramid | Seattle corporate HQ, epilogue scene |

### Flavor/optional
The Down And Out (bar), Penumbra (club), Queen Anne Hill (Masterson's
neighborhood), Aztlan/la barranca (Hernandez's home slum, off-map backstory
only).

---

## Organizations

### Built (7 new, all `is_active: false`)
| Name | Notes |
|---|---|
| Shigeda-gumi | Yakuza cell blackmailing Foley and running the kidnap plot. Distinct from the world's existing "Yakuza (Watada-rengo)" org. Sumiko Hotoda and Toroshi linked here. |
| Perfekto Polymers | Aztechnology subsidiary (org id 1) at the center of the waste-dumping scandal. Taetzel Building and the old plant site relinked here from Aztechnology. Masterson and Allende linked here. |
| New Horizons Development | Shigeda-owned real-estate front buying up the Barrens. |
| Federated Funds Net | Small bank (also a Matrix target, see below). The "Federated Funds Net (Offices)" location relinked here. |
| Dragon Knights | Kyle Morgan's Aztechnology-employed strike team. Morgan, Mixacopotec, Blackstone, and Lin Hwang relinked here from the generic Aztechnology stand-in. |
| Salish-Shidhe Council | Nation-state (matches the world's existing "Aztlan" org type); filed a formal protest over the dumping. |
| Citizens for a Decent Society Policlub | Moral-watchdog policlub (matches the world's existing "Humanis Policlub" org type); Margot Tipper linked here as chairwoman. |

Already existed in the world before this prep, reused as-is (no changes):
**Aztechnology** (org id 1) and **Lone Star Security**.

### Not built (too minor to warrant a tracked org record)
Musician's Guild Local 14 (files one piece of paperwork), Orbital Credit
Bearnaise (Dragon Knights' funding bank, background-only), the "Major
League" yakuza decker syndicate (Sorayama's on-call backup — represented
instead as spawned enemy deckers per `docs/mercurial_matrix_conversion.md`).
Mitsuhama already exists in the world and needed no changes.
