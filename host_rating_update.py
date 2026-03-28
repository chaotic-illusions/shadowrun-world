#!/usr/bin/env python3
"""
One-shot migration: replace numeric host_rating values with color-coded strings.

Rating tiers:
  Blue-3        : Public service, advertising, general-use
  Green-3..5    : Low-security limited-access, subscription, public library
  Orange-4..8   : Corporate/govt non-classified, low-to-mid criminal
  Red-5..9      : Classified corp/govt (financial, R&D), organized crime syndicates
  Black-6..10   : Most secret — black R&D, dragon intel, top crime leadership
"""
import json

SEED_FILE = "data/world_seed.json"

# Maps id_code -> new rating string.
# For public (id_code=None) entries, key is the description text instead.
RATINGS = {
    # ── Aztechnology ──────────────────────────────────────────────────────────
    "Corporate info & PR host":                          "Blue-3",
    "Stuffer Shack retail/franchise host":               "Blue-3",
    "AZT-EXEC":  "Orange-7",   # Seattle exec ops
    "AZT-RES1":  "Red-8",      # Bellevue R&D
    "AZTCORP7":  "Red-9",      # Tenochtitlan backbone
    "QP7NX38M":  "Black-8",    # Sub-basement research node

    # ── Aztlan (government) ───────────────────────────────────────────────────
    "Consulate public information host":                 "Blue-3",
    "AZTGOV1":   "Orange-7",   # Govt ops, Seattle liaison
    "AZTMIL2":   "Red-7",      # Military attache comms
    "8ZKNVX1Q":  "Black-8",    # Intelligence ops node

    # ── Ares Macrotechnology ──────────────────────────────────────────────────
    "Corporate information & products host":             "Blue-3",
    "Ares Arms public catalog host":                     "Blue-3",
    "ARES-NW":   "Orange-6",   # Pacific NW division ops
    "ARES-DEF":  "Red-8",      # Defense contracts & R&D
    "ARES-DET":  "Red-9",      # Detroit HQ backbone
    "3FNKP7QM":  "Black-8",    # Black ops liaison node

    # ── Fuchi Industrial Electronics ─────────────────────────────────────────
    "Corporate information & product support host":      "Blue-3",
    "Fuchi retail & consumer support host":              "Blue-3",
    "FUCHI-NA":  "Orange-6",   # Villiers faction NA ops
    "FUCHI-JP":  "Orange-7",   # Japanese board mirror
    "FUCHI-TK":  "Red-9",      # Tokyo HQ backbone
    "MV73XKPQ":  "Black-7",    # Internal faction conflict docs

    # ── Renraku Computer Systems ──────────────────────────────────────────────
    "SCIRE public information host":                     "Blue-3",
    "Corporate products & services host":                "Blue-3",
    "RNR-SCIR":  "Red-9",      # SCIRE internal ops
    "RNR-EXEC":  "Orange-7",   # Corporate executive host
    "RNR-SAMS":  "Red-8",      # Red Samurai tactical ops
    "RNR-CHIB":  "Red-9",      # Chiba HQ backbone
    "QKX39NZM":  "Black-10",   # SCIRE sub-level research

    # ── Shiawase Corporation ──────────────────────────────────────────────────
    # "Corporate information host" is shared key — handled below per-org
    "Environmental services public host":                "Blue-3",
    "SHAW-OPS":  "Orange-6",   # Seattle division ops
    "SHAW-BIO":  "Red-7",      # Biotech research
    "SHAW-OSK":  "Red-9",      # Osaka HQ backbone
    "PX4NRMW9":  "Black-8",    # Pharmaceutical black R&D

    # ── Saeder-Krupp Heavy Industries ─────────────────────────────────────────
    # "Corporate information host" shared — handled below
    "SK-PACNW":  "Orange-7",   # Pacific NW ops (SK is paranoid)
    "SK-FIN1":   "Red-8",      # Financial ops
    "SKHQ-ESN":  "Red-9",      # Essen HQ backbone
    "KWNPZ73M":  "Black-10",   # Lofwyr's intelligence node

    # ── Mitsuhama Computer Technologies ──────────────────────────────────────
    # "Corporate information host" shared — handled below
    "MCT-OPS1":  "Orange-8",   # Seattle ops (MCT paranoia)
    "MCT-PAR2":  "Red-8",      # Paranormal research
    "MCT-SEC3":  "Red-8",      # Zero-zone security coord
    "MCTHQ-KY":  "Red-9",      # Kyoto HQ backbone
    "NX8Q7VKZ":  "Black-7",    # Yakuza financial liaison

    # ── Yamatetsu Corporation ─────────────────────────────────────────────────
    # "Corporate information host" shared — handled below
    "Port logistics & shipping coordination host":       "Green-3",
    "YAMA-OPS":  "Orange-6",   # Seattle division ops
    "YAMA-BIO":  "Red-7",      # Biotech research
    "YAMAHQ-VL": "Red-8",      # Vladivostok HQ backbone
    "R4MXWPK9":  "Black-8",    # Next-gen bioware research

    # ── Knight Errant Security Services ──────────────────────────────────────
    "Public information & incident reporting host":      "Blue-3",
    "KE-OPS1":   "Orange-6",   # Seattle patrol ops
    "KE-TAC2":   "Orange-7",   # Tactical response coord
    "KE-INTL":   "Orange-6",   # Internal affairs
    "KE-CHI1":   "Red-7",      # Chicago HQ backbone
    "ZN8XQKVM":  "Black-7",    # Contract intel node (LS dossier)

    # ── Lone Star Security ────────────────────────────────────────────────────
    "Public host, warrant lookups & civilian reports":   "Blue-3",
    "LST-DISP":  "Orange-5",   # Dispatch & patrol coord
    "LST-SINT":  "Orange-6",   # Special Investigations
    "LST-DIR1":  "Orange-5",   # Director Hargrove private node
    "LST-REC1":  "Orange-5",   # Personnel & records
    "4KZW91VN":  "Black-7",    # IA corruption tracking node

    # ── Yakuza (Watada-rengo) ─────────────────────────────────────────────────
    "WTD-FIN1":  "Red-6",      # Financial ops & laundering
    "WTD-OPS2":  "Red-7",      # Seattle ops & territory
    "WTD-MCT3":  "Red-7",      # MCT financial liaison
    "WTD-INT4":  "Red-8",      # Intel & opposition tracking
    "8XKZPMQ4":  "Black-8",    # Oyabun Shotozumi's private node

    # ── Seattle Mafia ─────────────────────────────────────────────────────────
    "MAFIA-F1":  "Red-6",      # Financial ops & union accounts
    "MAFIA-O2":  "Red-7",      # Seattle family ops
    "MAFIA-P3":  "Red-8",      # Political leverage & blackmail
    "NQ7ZMKXP":  "Black-8",    # Don Bigio's private archive

    # ── Red Dragon Association ────────────────────────────────────────────────
    "RDA-FIN1":  "Red-6",      # Financial ops & smuggling
    "RDA-OPS2":  "Red-7",      # Seattle ops coord
    "RDA-BTL3":  "Red-7",      # BTL production & distribution
    "RDA-INT4":  "Red-8",      # Intel & inter-syndicate
    "WX4K9NZP":  "Black-9",    # The Engineer's production node

    # ── Seoulpa Rings ─────────────────────────────────────────────────────────
    "SPR-RNG1":  "Orange-6",   # Park Jin-ho ring ops
    "SPR-RNG2":  "Orange-7",   # Kim Soo-yeon ring (tech crime)
    "SPR-RNG3":  "Orange-6",   # Third ring BTL
    "SPR-BRG4":  "Red-7",      # The Bridge inter-ring coord
    "7FZNQXKM":  "Black-7",    # Anti-Yakuza intel archive

    # ── Humanis Policlub ──────────────────────────────────────────────────────
    "Political information & membership host":           "Blue-3",
    "HUM-POL1":  "Orange-5",   # Internal political coord & donors
    "HUM-OPS2":  "Orange-7",   # Enforcement arm ops
    "KP9NZMQX":  "Black-7",    # Deacon's command node
}

# Orgs that share "Corporate information host" description — map by org name
CORP_INFO_HOST_RATINGS = {
    "Shiawase Corporation":         "Blue-3",
    "Saeder-Krupp Heavy Industries":"Blue-3",
    "Mitsuhama Computer Technologies": "Blue-3",
    "Yamatetsu Corporation":        "Blue-3",
}


def update(seed_file: str) -> None:
    with open(seed_file, encoding="utf-8") as f:
        data = json.load(f)

    changed = 0
    for org in data.get("organizations", []):
        org_name = org.get("name", "")
        for entry in org.get("ltgs", []):
            if entry.get("type") != "matrix_host":
                continue

            id_code = entry.get("id_code")
            description = entry.get("description", "")

            new_rating = None
            if id_code and id_code in RATINGS:
                new_rating = RATINGS[id_code]
            elif description in RATINGS:
                new_rating = RATINGS[description]
            elif description == "Corporate information host" and org_name in CORP_INFO_HOST_RATINGS:
                new_rating = CORP_INFO_HOST_RATINGS[org_name]

            if new_rating is None:
                print(f"  WARN: no mapping for id_code={id_code!r} desc={description!r} (org: {org_name})")
                continue

            old = entry.get("host_rating")
            if old != new_rating:
                print(f"  {org_name} | {id_code or description[:40]}: {old} -> {new_rating}")
                entry["host_rating"] = new_rating
                changed += 1

    with open(seed_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nDone. {changed} host_rating values updated.")


if __name__ == "__main__":
    update(SEED_FILE)
