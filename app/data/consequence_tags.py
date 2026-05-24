"""
Consequence tag taxonomy for Shadowrun 2nd Edition.

Tags are snake_case strings. Each entry maps a frozenset of tags to a list of
narrative consequence suggestions. The engine uses subset matching -- a rule fires
if its tag set is a subset of the active tags. More specific rules (larger sets)
are listed first in the output.

Tag format: {category}_{subject}_{qualifier}
"""
from typing import Any

# ---------------------------------------------------------------------------
# Single-tag rules
# ---------------------------------------------------------------------------
SINGLE_TAG_RULES: dict[str, dict[str, Any]] = {
    # --- Run outcome ---
    "run_success_clean": {
        "severity": "positive",
        "suggestions": [
            "The Johnson is satisfied -- future work from this contact is likely.",
            "Word travels quietly; the team's street cred improves in relevant circles.",
        ],
    },
    "run_success_exposed": {
        "severity": "low",
        "suggestions": [
            "The objective was achieved, but faces and methods are now known to the target.",
            "Corporate or gang intel files may now include the runners' descriptions.",
            "The Johnson got results but may be nervous about loose ends.",
        ],
    },
    "run_failure_quiet": {
        "severity": "moderate",
        "suggestions": [
            "The target is now alert -- security has been quietly tightened.",
            "The Johnson may seek alternative runners or demand a discount on the next job.",
            "The team's reputation takes a minor hit in shadow circles.",
        ],
    },
    "run_failure_exposed": {
        "severity": "severe",
        "suggestions": [
            "The target has faces, descriptions, or SINs -- active investigation is underway.",
            "The Johnson distances themselves; no payment and possibly a public denial.",
            "Law enforcement or corp security is building a case.",
            "The team should expect increased scrutiny at checkpoints and corp-controlled zones.",
        ],
    },
    "run_partial_success": {
        "severity": "low",
        "suggestions": [
            "Primary objective complete, but the secondary failure creates a loose thread.",
            "The Johnson pays partial, and may bring the unfinished business back later.",
        ],
    },
    "run_partial_failure": {
        "severity": "moderate",
        "suggestions": [
            "Primary objective failed; whatever they were protecting or retrieving is still in play.",
            "The secondary success may create an unexpected ally or bargaining chip.",
        ],
    },
    "run_abandoned": {
        "severity": "moderate",
        "suggestions": [
            "The Johnson is owed an explanation -- relations may sour permanently.",
            "Whatever triggered the abort (heat, betrayal, casualties) is still unresolved.",
            "The target remains at full readiness; a retry will be significantly harder.",
        ],
    },

    # --- Faction: Megacorp ---
    "megacorp_offended": {
        "severity": "moderate",
        "suggestions": [
            "Corporate security sweeps increase in the runners' known haunts.",
            "A fixer or contact with corp ties quietly distances themselves.",
            "The corp adds the team to a watch list; ID checks may flag them.",
        ],
    },
    "megacorp_burned": {
        "severity": "severe",
        "suggestions": [
            "A corporate black ops team is tasked to neutralize or capture the runners.",
            "Known contacts, safe houses, and associates may be surveilled or pressured.",
            "A significant bounty circulates through back-channels.",
            "Rival corps may try to poach or use the runners as a proxy weapon.",
        ],
    },
    "megacorp_favored": {
        "severity": "positive",
        "suggestions": [
            "A corporate fixer reaches out with a job offer at improved rates.",
            "Corp-controlled zones and facilities may extend a degree of tolerance.",
            "The team gains access to corporate resources or safe passage -- for now.",
        ],
    },

    # --- Faction: Law enforcement ---
    "government_burned": {
        "severity": "severe",
        "suggestions": [
            "Lonestar or Metroplex Guard escalates to active pursuit mode.",
            "Known associates and contacts are brought in for questioning.",
            "Any legal SINs the runners hold are flagged; travel and banking become risky.",
            "SWAT-level response teams placed on standby for the runners' known areas.",
        ],
    },
    "government_offended": {
        "severity": "moderate",
        "suggestions": [
            "Patrols increase in areas associated with the runners.",
            "Informants are pressured; word may reach Lonestar through unexpected channels.",
        ],
    },
    "government_favored": {
        "severity": "positive",
        "suggestions": [
            "A detective or official looks the other way -- once.",
            "The team may be able to call in this favor to suppress a warrant or get intel.",
        ],
    },

    # --- Faction: Gang ---
    "gang_burned": {
        "severity": "moderate",
        "suggestions": [
            "The gang marks the runners -- their territory becomes actively hostile.",
            "Gang members may harass known contacts or associates.",
            "A gang boss may put out a street-level bounty.",
        ],
    },
    "gang_favored": {
        "severity": "positive",
        "suggestions": [
            "Safe passage through gang territory is extended.",
            "The gang may share intel or provide muscle if asked.",
        ],
    },

    # --- Faction: Syndicate / Organized crime ---
    "syndicate_burned": {
        "severity": "severe",
        "suggestions": [
            "Organized crime sends a message -- usually violent.",
            "Shadow contacts with syndicate ties go quiet or turn hostile.",
            "The runners may find their gear or credstick suppliers suddenly unavailable.",
        ],
    },
    "syndicate_favored": {
        "severity": "positive",
        "suggestions": [
            "A syndicate fixer owes a favor -- it will come with strings.",
            "Access to black market goods improves, temporarily.",
        ],
    },

    # --- NPCs ---
    "npc_major_killed": {
        "severity": "significant",
        "suggestions": [
            "A power vacuum forms in the NPC's organization -- factions scramble for control.",
            "Loyal subordinates or family members seek revenge.",
            "Unfinished business the NPC was managing becomes an open, dangerous thread.",
            "Investigators (corporate, criminal, or legal) begin asking questions.",
        ],
    },
    "npc_minor_killed": {
        "severity": "low",
        "suggestions": [
            "Collateral casualties draw local attention and possible media coverage.",
            "Survivors may surface later as informants or hostile witnesses.",
        ],
    },
    "npc_major_betrayed": {
        "severity": "moderate",
        "suggestions": [
            "Word spreads in the shadows -- burning contacts has a cost.",
            "The betrayed NPC, if alive, actively works against the team.",
            "The NPC's allies may treat the runners with distrust or hostility.",
        ],
    },
    "npc_major_rescued": {
        "severity": "positive",
        "suggestions": [
            "The rescued NPC becomes a significant ally -- at least for now.",
            "Their organization may extend goodwill, resources, or intelligence.",
        ],
    },
    "npc_contact_burned": {
        "severity": "significant",
        "suggestions": [
            "The contact is compromised, dead, or hostile -- that resource is gone.",
            "Other contacts in the same network may become wary.",
            "The opposition now knows the team had a contact in that network.",
        ],
    },
    "npc_contact_upgraded": {
        "severity": "positive",
        "suggestions": [
            "The contact's loyalty or connection improves -- they're more invested in the team's success.",
            "The contact may proactively offer tips or introductions.",
        ],
    },

    # --- PC status ---
    "pc_identity_exposed": {
        "severity": "severe",
        "suggestions": [
            "The exposed runner's real SIN or identity is now known -- new SIN required.",
            "Family, former employers, or old enemies may be contacted.",
            "Travel and financial transactions tied to that identity become a liability.",
        ],
    },
    "pc_bounty_placed": {
        "severity": "severe",
        "suggestions": [
            "Bounty hunters and opportunistic runners begin taking interest.",
            "Street contacts may tip off the opposition for a cut.",
            "Public spaces and corp-controlled zones become significantly more dangerous.",
        ],
    },
    "pc_reputation_shift": {
        "severity": "variable",
        "suggestions": [
            "Update Street Cred, Notoriety, and/or Public Awareness tracks accordingly.",
            "Changed reputation ripples into future job offers, contact interactions, and NPC attitudes.",
        ],
    },
    "pc_injured_seriously": {
        "severity": "moderate",
        "suggestions": [
            "Recovery time may affect availability for the next run.",
            "Medical treatment requires a trusted street doc -- and discretion.",
            "The injury may attract questions if the runner is seen in public.",
        ],
    },

    # --- Locations ---
    "location_burned": {
        "severity": "moderate",
        "suggestions": [
            "The location is now compromised -- safe meetings and handoffs there are inadvisable.",
            "Assets or stashes left at the location may be seized or monitored.",
        ],
    },
    "location_destroyed": {
        "severity": "significant",
        "suggestions": [
            "Collateral damage draws heat from Lonestar, media, and the owning organization.",
            "Innocent bystanders create political complications for the Johnson.",
            "The owning organization seeks accountability -- the team may be blamed.",
        ],
    },
    "location_secured": {
        "severity": "positive",
        "suggestions": [
            "The team has a new operational base or safe house.",
            "Track who knows about it -- that number should stay small.",
        ],
    },
    "location_corp_lockdown": {
        "severity": "moderate",
        "suggestions": [
            "Corporate security presence in the area intensifies.",
            "Civilians and street contacts in the district may be affected or displaced.",
        ],
    },
    "location_gang_claimed": {
        "severity": "moderate",
        "suggestions": [
            "A previously neutral zone is now gang territory -- tolls, hostility, or new leverage.",
            "Former occupants or businesses may reach out for help reclaiming it.",
        ],
    },

    # --- Assets ---
    "asset_data_stolen": {
        "severity": "variable",
        "suggestions": [
            "The target organization initiates damage control -- they know something was taken.",
            "The data may contain information with implications beyond the run's original scope.",
            "Counter-intelligence may attempt to trace the data or plant disinformation.",
        ],
    },
    "asset_data_leaked": {
        "severity": "significant",
        "suggestions": [
            "Sensitive information is now in the wild -- multiple parties may act on it.",
            "The team may be held responsible for the fallout, even if unintentional.",
        ],
    },
    "asset_person_extracted": {
        "severity": "positive",
        "suggestions": [
            "The extracted person is now an asset, dependent, or complication.",
            "The organization they were extracted from will want them back -- or silenced.",
        ],
    },
    "asset_person_lost": {
        "severity": "significant",
        "suggestions": [
            "The Johnson may withhold payment or seek damages.",
            "If the person was killed, their organization's response depends on their value.",
        ],
    },
    "asset_item_retrieved": {
        "severity": "positive",
        "suggestions": [
            "The item's value is now known -- others may seek it as well.",
            "Delivery to the Johnson completes the obligation, but the item's story may continue.",
        ],
    },
    "asset_item_destroyed": {
        "severity": "moderate",
        "suggestions": [
            "The Johnson may refuse payment if the item was the objective.",
            "The item's former owner or creator may have reasons to investigate its destruction.",
        ],
    },

    # --- Heat level ---
    "heat_low": {
        "severity": "low",
        "suggestions": [
            "Minor attention is on the team -- lying low for a session or two clears it.",
        ],
    },
    "heat_medium": {
        "severity": "moderate",
        "suggestions": [
            "Active investigation is underway -- the team should avoid known haunts and public SIN checks.",
            "Consider a temporary change of base or identity.",
        ],
    },
    "heat_high": {
        "severity": "severe",
        "suggestions": [
            "Direct pursuit is active -- hostile encounters at known locations are likely.",
            "Contacts may be pressured or monitored; use cutouts.",
        ],
    },
    "heat_extreme": {
        "severity": "severe",
        "suggestions": [
            "Multiple factions are actively hunting -- nowhere feels safe.",
            "The team needs to resolve the cause of the heat before any normal operations can resume.",
            "Consider drastic measures: new SINs, relocation, or negotiating a truce.",
        ],
    },
    "heat_cleared": {
        "severity": "positive",
        "suggestions": [
            "Previous heat has gone cold or been resolved -- normal operations can resume.",
            "Note what cleared the heat; the same approach may work again.",
        ],
    },

    # --- World state ---
    "political_shift": {
        "severity": "variable",
        "suggestions": [
            "A change in power structure creates new enemies, allies, and job opportunities.",
            "Previously reliable contacts in the old power structure may be vulnerable.",
        ],
    },
    "corp_war_triggered": {
        "severity": "severe",
        "suggestions": [
            "Corporate conflict escalates -- shadow ops increase, collateral damage rises.",
            "Both sides may recruit the runners, creating dangerous divided loyalties.",
            "Civilian zones near corp assets become unpredictable and dangerous.",
        ],
    },
    "awakened_event": {
        "severity": "variable",
        "suggestions": [
            "Magical or Awakened phenomena draw attention from Talismongers, corps, and cults.",
            "The event may have changed a location's background count permanently.",
            "Awakened characters on the team may have new responsibilities -- or enemies.",
        ],
    },
    "matrix_event": {
        "severity": "variable",
        "suggestions": [
            "A significant Matrix disruption may have left traces -- the decker's ID may be at risk.",
            "Corps or the Shadowland BBS may have intel on the event.",
            "Damaged or altered systems may create downstream effects in future runs.",
        ],
    },
    "favor_owed_to_team": {
        "severity": "positive",
        "suggestions": [
            "A powerful figure owes the runners a favor -- track it, it can be called in.",
            "The relationship may shift faction allegiances over time.",
        ],
    },
    "team_owes_favor": {
        "severity": "moderate",
        "suggestions": [
            "The debt will be called in at the worst possible moment.",
            "Failing to honor the debt will have significant reputation consequences.",
        ],
    },
}

# ---------------------------------------------------------------------------
# Compound rules -- fire when ALL tags in the key set are present
# ---------------------------------------------------------------------------
COMPOUND_TAG_RULES: dict[frozenset, dict[str, Any]] = {
    frozenset({"megacorp_burned", "run_failure_exposed"}): {
        "severity": "severe",
        "suggestions": [
            "The corp has faces AND a motive -- a dedicated extraction or elimination team is likely.",
            "Public Awareness for all involved runners increases by at least 1.",
            "The Johnson who hired them may also face corporate pressure.",
        ],
    },
    frozenset({"megacorp_burned", "pc_identity_exposed"}): {
        "severity": "severe",
        "suggestions": [
            "Corporate resources are focused on the exposed runner -- family and associates are at risk.",
            "All legal financial accounts and registered assets tied to that identity should be considered compromised.",
        ],
    },
    frozenset({"npc_major_killed", "megacorp_burned"}): {
        "severity": "severe",
        "suggestions": [
            "The corp mourns their asset and wants accountability -- expect a high-value bounty.",
            "Internal corp politics around who replaces the NPC may create unexpected allies.",
        ],
    },
    frozenset({"location_destroyed", "megacorp_offended"}): {
        "severity": "significant",
        "suggestions": [
            "Property damage plus operational disruption -- the corp escalates from 'watch list' to 'respond'.",
            "Legal action (in addition to shadow action) may be filed against known identities.",
        ],
    },
    frozenset({"heat_high", "pc_bounty_placed"}): {
        "severity": "severe",
        "suggestions": [
            "With active heat AND a bounty, even street-level allies may be tempted to sell the team out.",
            "Safe houses and known contacts should be considered potentially compromised.",
        ],
    },
    frozenset({"run_success_clean", "npc_major_rescued"}): {
        "severity": "positive",
        "suggestions": [
            "Clean success plus a significant rescue -- the team's reputation in that NPC's network rises substantially.",
            "Future jobs from this network will come with better terms and better intelligence.",
        ],
    },
}


def get_all_tags() -> list[str]:
    return sorted(SINGLE_TAG_RULES.keys())


def get_tag_info(tag: str) -> dict[str, Any] | None:
    return SINGLE_TAG_RULES.get(tag)
