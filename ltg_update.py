#!/usr/bin/env python3
"""
Migrates LTG data in world_seed.json from embedded notes text to a structured
`ltgs` list field on each organization (same pattern as `leadership`).

Safe to re-run — strips old text block if present, then writes clean structured data.

LTG entry shapes
────────────────
Telecom:
  { "type": "telecom", "number": "(206) XXX-XXXX",
    "description": "...", "visibility": "listed" | "unlisted" }

Matrix host:
  { "type": "matrix_host", "rtg": "NA/UCAS-SEA", "ltg": "4A7C2",
    "id_code": null | "AZT-EXEC",
    "description": "...", "visibility": "listed" | "unlisted" | "black",
    "host_rating": 4, "notes": "..." (optional) }
"""

import json

SEED_FILE = "d:/Code Projects/shadowrun-world/data/world_seed.json"

# ── helpers ───────────────────────────────────────────────────────────────────

def T(number, description, visibility="listed"):
    return {"type": "telecom", "number": number,
            "description": description, "visibility": visibility}

def H(rtg, ltg, description, visibility, host_rating, id_code=None, notes=None):
    entry = {"type": "matrix_host", "rtg": rtg, "ltg": ltg,
             "id_code": id_code, "description": description,
             "visibility": visibility, "host_rating": host_rating}
    if notes:
        entry["notes"] = notes
    return entry

# ── structured LTG data ───────────────────────────────────────────────────────

LTG_DATA = {

"Aztechnology": [
    T("(206) 554-2900", "Public switchboard"),
    T("(206) 554-2930", "Media & PR line"),
    T("(206) 554-2977", "Executive reception, Pyramid"),
    H("NA/UCAS-SEA", "4A7C2", "Corporate info & PR host",            "listed",   4),
    H("NA/UCAS-SEA", "B391F", "Stuffer Shack retail/franchise host", "listed",   3),
    H("NA/UCAS-SEA", "7E04D", "Seattle executive operations host",   "unlisted", 7,  "AZT-EXEC"),
    H("NA/UCAS-SEA", "C28A1", "Bellevue R&D campus host",            "unlisted", 9,  "AZT-RES1"),
    H("NA/AZ-CE",    "0F39B", "Tenochtitlan corp backbone, Seattle mirror", "unlisted", 10, "AZTCORP7"),
    H("NA/UCAS-SEA", "91C4D", "Sub-basement research node, Bellevue campus", "black", 12, "QP7NX38M"),
],

"Aztlan": [
    T("(206) 632-1800", "Aztlan Consulate, Seattle"),
    T("(206) 632-1850", "Consulate press & visa services"),
    H("NA/UCAS-SEA", "2D8F1", "Consulate public information host",   "listed",   3),
    H("NA/AZ-CE",    "A7C34", "Aztlan government ops, Seattle liaison", "unlisted", 8, "AZTGOV1"),
    H("NA/AZ-CE",    "3B9E7", "Military attache communications",     "unlisted", 9,  "AZTMIL2"),
    H("NA/UCAS-SEA", "F2B04", "Intelligence operations node",        "black",    10, "8ZKNVX1Q"),
],

"Ares Macrotechnology": [
    T("(206) 445-6700", "Seattle corporate reception"),
    T("(206) 445-6750", "Defense contracts & procurement"),
    T("(206) 445-6799", "Executive direct line"),
    H("NA/UCAS-SEA", "D3A71", "Corporate information & products host", "listed",   4),
    H("NA/UCAS-SEA", "8C0F4", "Ares Arms public catalog host",         "listed",   3),
    H("NA/UCAS-SEA", "51B9E", "Pacific Northwest division operations host", "unlisted", 7, "ARES-NW"),
    H("NA/UCAS-SEA", "7D4C2", "Defense contracts & R&D Seattle mirror",    "unlisted", 9, "ARES-DEF"),
    H("NA/UCAS-MW",  "B2F83", "Detroit HQ backbone, Seattle access node",  "unlisted", 10, "ARES-DET"),
    H("NA/UCAS-SEA", "0E6A3", "Black ops division liaison node", "black", 11, "3FNKP7QM"),
],

"Fuchi Industrial Electronics": [
    T("(206) 229-5500", "Seattle corporate reception"),
    T("(206) 229-5520", "Consumer products & deck support"),
    T("(206) 229-5599", "Villiers North America office, direct"),
    H("NA/UCAS-SEA", "6B3D9", "Corporate information & product support host", "listed",   4),
    H("NA/UCAS-SEA", "1A7F2", "Fuchi retail & consumer support host",         "listed",   3),
    H("NA/UCAS-SEA", "C5E08", "Villiers faction North America operations host", "unlisted", 7, "FUCHI-NA"),
    H("NA/UCAS-SEA", "9D4B1", "Japanese board Seattle mirror node",            "unlisted", 7, "FUCHI-JP"),
    H("AS/JPN-KAN",  "3F72A", "Tokyo HQ backbone, Seattle access node",        "unlisted", 10, "FUCHI-TK"),
    H("NA/UCAS-SEA", "E8C35", "Internal faction conflict documents", "black", 9, "MV73XKPQ",
      "Whoever controls this node controls the narrative of the Villiers/board split."),
],

"Renraku Computer Systems": [
    T("(206) 331-7800", "SCIRE public information"),
    T("(206) 331-7850", "SCIRE residential admissions"),
    T("(206) 331-7900", "Seattle corporate reception"),
    H("NA/UCAS-SEA", "4E9C7", "SCIRE public information host",     "listed",   5),
    H("NA/UCAS-SEA", "2A0D4", "Corporate products & services host","listed",   4),
    H("NA/UCAS-SEA", "F73B8", "SCIRE internal operations host",    "unlisted", 10, "RNR-SCIR"),
    H("NA/UCAS-SEA", "8C1F6", "Corporate executive host, Seattle", "unlisted", 8,  "RNR-EXEC"),
    H("NA/UCAS-SEA", "0D9A2", "Red Samurai tactical operations host", "unlisted", 11, "RNR-SAMS"),
    H("AS/JPN-KAN",  "B6E41", "Chiba HQ backbone, Seattle access node", "unlisted", 12, "RNR-CHIB"),
    H("NA/UCAS-SEA", "5B7F3", "SCIRE sub-level research node", "black", 14, "QKX39NZM",
      "Rumored to contain data from pre-lockdown SCIRE experiments. The rating is not inflated."),
],

"Shiawase Corporation": [
    T("(206) 342-8800", "Seattle corporate reception"),
    T("(206) 342-8830", "Environmental services division"),
    T("(206) 342-8870", "Biotech research division"),
    H("NA/UCAS-SEA", "7C4E1", "Corporate information host",            "listed",   4),
    H("NA/UCAS-SEA", "3A9D6", "Environmental services public host",    "listed",   3),
    H("NA/UCAS-SEA", "D1B08", "Seattle division operations host",      "unlisted", 7,  "SHAW-OPS"),
    H("NA/UCAS-SEA", "6F3C2", "Biotech research host, Seattle",        "unlisted", 9,  "SHAW-BIO"),
    H("AS/JPN-KNS",  "9E7A4", "Osaka HQ backbone, Seattle access node","unlisted", 10, "SHAW-OSK"),
    H("NA/UCAS-SEA", "2C8F7", "Pharmaceutical black R&D node",         "black",    10, "PX4NRMW9"),
],

"Saeder-Krupp Heavy Industries": [
    T("(206) 467-3300", "Seattle operations reception"),
    T("(206) 467-3350", "Port & industrial contracts"),
    H("NA/UCAS-SEA", "A3D72", "Corporate information host",              "listed",   4),
    H("NA/UCAS-SEA", "5F09C", "Pacific Northwest operations host",       "unlisted", 8,  "SK-PACNW"),
    H("NA/UCAS-SEA", "C7B41", "Financial operations, Seattle mirror",    "unlisted", 10, "SK-FIN1"),
    H("EU/AGS-NW",   "8A3F6", "Essen HQ backbone, Seattle access node", "unlisted", 12, "SKHQ-ESN"),
    H("NA/UCAS-SEA", "1D4B9", "Lofwyr's Seattle intelligence node", "black", 15, "KWNPZ73M",
      "If this node is ever accessed, assume Lofwyr knows within minutes. The rating is not a typo."),
],

"Mitsuhama Computer Technologies": [
    T("(206) 682-4400", "Seattle corporate reception"),
    T("(206) 682-4420", "Zero-zone public security warning line"),
    H("NA/UCAS-SEA", "9B5E3", "Corporate information host", "listed", 5,
      notes="Connecting logs your access node. MCT cross-references all visitors against known runner SINs."),
    H("NA/UCAS-SEA", "F4C71", "Seattle division operations host",       "unlisted", 9,  "MCT-OPS1"),
    H("NA/UCAS-SEA", "2E8D0", "Paranormal research data host",          "unlisted", 11, "MCT-PAR2"),
    H("NA/UCAS-SEA", "6A3B9", "Zero-zone security coordination host",   "unlisted", 10, "MCT-SEC3"),
    H("AS/JPN-KNS",  "D70F5", "Kyoto HQ backbone, Seattle access node", "unlisted", 12, "MCTHQ-KY"),
    H("NA/UCAS-SEA", "B1C4E", "Yakuza financial liaison node", "black", 10, "NX8Q7VKZ",
      "Known only to senior Watada-rengo and MCT board level. Most sensitive data in MCT's Seattle operation."),
],

"Yamatetsu Corporation": [
    T("(206) 587-4200", "Seattle corporate reception"),
    T("(206) 587-4250", "Port operations & logistics"),
    T("(206) 587-4280", "Biotech research division"),
    H("NA/UCAS-SEA", "3D6A0", "Corporate information host",                  "listed",   4),
    H("NA/UCAS-SEA", "C8B34", "Port logistics & shipping coordination host", "listed",   3),
    H("NA/UCAS-SEA", "7F1E9", "Seattle division operations host",            "unlisted", 7,  "YAMA-OPS"),
    H("NA/UCAS-SEA", "4A3D7", "Biotech research host, Seattle",              "unlisted", 9,  "YAMA-BIO"),
    H("AS/RUS-FE",   "B92C1", "Vladivostok HQ backbone, Seattle access node","unlisted", 9,  "YAMAHQ-VL"),
    H("NA/UCAS-SEA", "0E7F4", "Next-generation bioware research node",       "black",    11, "R4MXWPK9"),
],

"Knight Errant Security Services": [
    T("(206) 445-9911", "Emergency response dispatch"),
    T("(206) 445-9900", "Public information & non-emergency"),
    T("(206) 445-9955", "Corporate security contracts"),
    H("NA/UCAS-SEA", "E2A74", "Public information & incident reporting host", "listed",   4),
    H("NA/UCAS-SEA", "9C3F1", "Seattle patrol operations host",               "unlisted", 7,  "KE-OPS1"),
    H("NA/UCAS-SEA", "5B08D", "Tactical response coordination host",          "unlisted", 8,  "KE-TAC2"),
    H("NA/UCAS-SEA", "A7D43", "Internal affairs & incident review host",      "unlisted", 7,  "KE-INTL"),
    H("NA/UCAS-MW",  "3E91C", "Chicago HQ backbone, Seattle access node",     "unlisted", 9,  "KE-CHI1"),
    H("NA/UCAS-SEA", "6F4B0", "Contract acquisition intelligence node", "black", 9, "ZN8XQKVM",
      "Contains KE's compiled Lone Star corruption dossier for the city contract bid. Valuable to both sides."),
],

"Lone Star Security": [
    T("(206) 267-3911", "Emergency dispatch"),
    T("(206) 267-3900", "Public information & non-emergency"),
    T("(206) 267-3955", "Press relations"),
    H("NA/UCAS-SEA", "1B8A3", "Public host, warrant lookups & civilian reports", "listed", 3),
    H("NA/UCAS-SEA", "6C2F0", "Internal dispatch & patrol coordination host", "unlisted", 6, "LST-DISP",
      "Static's backdoor enters here. She has read access to patrol assignments and BOLO alerts."),
    H("NA/UCAS-SEA", "D047C", "Special Investigations division host",   "unlisted", 7, "LST-SINT"),
    H("NA/UCAS-SEA", "9F3E1", "Director Hargrove's private node",       "unlisted", 5, "LST-DIR1"),
    H("NA/UCAS-SEA", "4A8C2", "Personnel & internal records host",      "unlisted", 6, "LST-REC1"),
    H("NA/UCAS-SEA", "3E8B2", "Internal affairs & corruption tracking node", "black", 8, "4KZW91VN",
      "Contains documentation of Hargrove's organized crime relationships. Most dangerous data in Lone Star's possession."),
],

"Yakuza (Watada-rengo)": [
    T("(206) 324-7711", "Shotozumi Ramen, Little Tokyo — known front",     "listed"),
    T("(206) 324-7750", "Pacific Rim Import/Export LLC — known front",     "listed"),
    T("(206) 324-7788", "Watada Investments Group — shadow community knows this one", "listed"),
    H("NA/UCAS-SEA", "B4D71", "Financial operations & money laundering coordination", "unlisted", 8,  "WTD-FIN1"),
    H("NA/UCAS-SEA", "7C2F9", "Seattle operations & territory coordination",          "unlisted", 9,  "WTD-OPS2"),
    H("NA/UCAS-SEA", "3A8E4", "MCT financial liaison node",                           "unlisted", 8,  "WTD-MCT3"),
    H("NA/UCAS-SEA", "F91C0", "Intelligence & opposition tracking host",              "unlisted", 10, "WTD-INT4"),
    H("NA/UCAS-SEA", "2D5B7", "Oyabun Shotozumi's private communications node", "black", 12, "8XKZPMQ4"),
],

"Seattle Mafia": [
    T("(206) 621-8840", "Bigio Family Imports LLC — known front",    "listed"),
    T("(206) 621-8870", "Ruggerio Dockside Services — known front",  "listed"),
    T("(206) 621-8900", "Argento Legal Group — money laundering vehicle", "listed"),
    H("NA/UCAS-SEA", "5C3D8", "Financial operations & union accounts",      "unlisted", 7,  "MAFIA-F1"),
    H("NA/UCAS-SEA", "9B7A1", "Seattle family operations coordination",     "unlisted", 8,  "MAFIA-O2"),
    H("NA/UCAS-SEA", "E4F06", "Political leverage & blackmail archive",     "unlisted", 9,  "MAFIA-P3"),
    H("NA/UCAS-SEA", "1A3C7", "Don Bigio's private archive", "black", 10, "NQ7ZMKXP",
      "Contains decades of compromising material on city officials. Father Argento is the only other party with access."),
],

"Red Dragon Association": [
    T("(206) 382-6600", "Hong Kong Trading Company — known front",      "listed"),
    T("(206) 382-6640", "Golden Dragon Restaurant, Chinatown",          "listed"),
    T("(206) 382-6680", "Pacific Rim Shipping & Freight — smuggling front", "listed"),
    H("NA/UCAS-SEA", "7F4B2", "Financial operations & smuggling accounts",      "unlisted", 7,  "RDA-FIN1"),
    H("NA/UCAS-SEA", "2C9E0", "Seattle operations coordination host",           "unlisted", 8,  "RDA-OPS2"),
    H("NA/UCAS-SEA", "E3C80", "BTL production & distribution coordination",     "unlisted", 8,  "RDA-BTL3"),
    H("NA/UCAS-SEA", "8B1F4", "Intelligence & inter-syndicate relations",        "unlisted", 9,  "RDA-INT4"),
    H("NA/UCAS-SEA", "5E6C9", "The Engineer's production node", "black", 11, "WX4K9NZP",
      "BTL lab location is derivable from this node. Most sought-after paydata in Seattle shadow community."),
],

"Seoulpa Rings": [
    T("(206) 493-5500", "Seoul House Restaurant — Park Jin-ho ring front",         "listed"),
    T("(206) 493-5540", "Korean-American Business Association — political cover",  "listed"),
    T("(206) 493-5580", "Hangang Electronics LLC — tech crime front, Kim Soo-yeon ring", "listed"),
    H("NA/UCAS-SEA", "6D4A8", "Park Jin-ho ring operations node",             "unlisted", 7,  "SPR-RNG1"),
    H("NA/UCAS-SEA", "B3F71", "Kim Soo-yeon ring — tech crime & SIN forgery", "unlisted", 8,  "SPR-RNG2"),
    H("NA/UCAS-SEA", "9A2C5", "Third ring — BTL distribution & territory",    "unlisted", 7,  "SPR-RNG3"),
    H("NA/UCAS-SEA", "4E8D0", "The Bridge — inter-ring coordination node",    "unlisted", 10, "SPR-BRG4",
      "Compromising this node identifies the Bridge. Yakuza has been trying to locate it for two years."),
    H("NA/UCAS-SEA", "C17B3", "Anti-Yakuza intelligence archive", "black", 9, "7FZNQXKM"),
],

"Humanis Policlub": [
    T("(206) 547-2800", "Seattle chapter public line"),
    T("(206) 547-2820", "Voter registration & political action"),
    T("(206) 547-2860", "Councilman Vogel's constituent office — officially separate from Humanis"),
    H("NA/UCAS-SEA", "3C7D1", "Political information & membership host",        "listed",   3),
    H("NA/UCAS-SEA", "A8F24", "Internal political coordination & donor records","unlisted", 6, "HUM-POL1"),
    H("NA/UCAS-SEA", "5D3B9", "Enforcement arm operational coordination",       "unlisted", 8, "HUM-OPS2"),
    H("NA/UCAS-SEA", "E71C4", "Deacon's command node — enforcement orders & target lists", "black", 10, "KP9NZMQX",
      "Contains authorization chains linking Vogel directly to enforcement violence. Career-ending paydata."),
],

}

# ── strip old text-block LTG section from notes ───────────────────────────────

LTG_MARKER = "LTG DIRECTORY"

def strip_ltg_from_notes(notes: str) -> str:
    if not notes or LTG_MARKER not in notes:
        return notes
    # Find the last occurrence of the marker's surrounding block and trim
    idx = notes.find(LTG_MARKER)
    # Walk back to the nearest preceding newline block to clean up whitespace
    trimmed = notes[:idx].rstrip()
    return trimmed if trimmed else None


# ── main ──────────────────────────────────────────────────────────────────────

def main():
    with open(SEED_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    updated = 0
    skipped = 0

    for org in data["organizations"]:
        name = org["name"]
        if name not in LTG_DATA:
            skipped += 1
            continue

        # Strip old text block from notes
        org["notes"] = strip_ltg_from_notes(org.get("notes") or "")

        # Write structured ltgs field
        org["ltgs"] = LTG_DATA[name]
        updated += 1
        print(f"  + {name}  ({len(LTG_DATA[name])} entries)")

    with open(SEED_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nDone. Updated: {updated}  No LTG data defined: {skipped}")


if __name__ == "__main__":
    main()
