// SR2 core stock cyberdecks (p.173), adapted forward to this app's VR2-flavored matrix engine.
// Source of truth / decision log: docs/reference-data/sr2-cyberdecks-vr2.json.
//
// Quick-pick rules (a stock deck is an "easy option" -- you cannot customize it):
//   * Purchase price is the printed book cost below (NOT the a-la-carte street price).
//   * Persona is not fixed: the buyer splits MPCP x 3 points across Bod/Evasion/Masking/Sensor.
//   * I/O is derived, not stored: io_speed = ceil(MPCP x Sensor x 5 / 10) x 10 (half the app's
//     MPCP x Sensor x 10 ceiling, so there is room to upgrade later).
//   * Reality Filters cannot be fitted to a stock deck (persona cap stays MPCP x 3, never (MPCP-1) x 3).
//   * MPCP, hardening and memory are fixed by the model; the only buyer choice is the persona split.
window.StockDecks = [
  { n: "Radio Shack PCD-100", mpcp: 2,  hardening: 0, activeMemory: 10,  storageMemory: 50,   personaPool: 6,  cost: 6800,    src: "SR2", pg: 173 },
  { n: "Allegiance Alpha",    mpcp: 3,  hardening: 1, activeMemory: 10,  storageMemory: 50,   personaPool: 9,  cost: 12600,   src: "SR2", pg: 173 },
  { n: "Fuchi Cyber-4",       mpcp: 4,  hardening: 2, activeMemory: 100, storageMemory: 500,  personaPool: 12, cost: 121400,  src: "SR2", pg: 173 },
  { n: "Sony CTY-360",        mpcp: 6,  hardening: 3, activeMemory: 50,  storageMemory: 100,  personaPool: 18, cost: 99400,   src: "SR2", pg: 173 },
  { n: "Fuchi Cyber-6",       mpcp: 8,  hardening: 4, activeMemory: 100, storageMemory: 500,  personaPool: 24, cost: 334500,  src: "SR2", pg: 173 },
  { n: "Fuchi Cyber-7",       mpcp: 10, hardening: 4, activeMemory: 200, storageMemory: 1000, personaPool: 30, cost: 1112100, src: "SR2", pg: 173 },
  { n: "Fairlight Excalibur", mpcp: 12, hardening: 5, activeMemory: 500, storageMemory: 1000, personaPool: 36, cost: 5529600, src: "SR2", pg: 173 },
];

// Stock deck I/O: half the app ceiling (MPCP x Sensor x 5), rounded UP to the next multiple of 10.
window.stockDeckIoSpeed = function (mpcp, sensor) {
  const raw = (Math.max(0, mpcp) * Math.max(0, sensor)) * 5;
  return Math.ceil(raw / 10) * 10;
};
