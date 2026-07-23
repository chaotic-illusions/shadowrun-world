(function (global) {
  'use strict';

  const OPTION_DEFS = [
    { id: 'area', label: 'Area', type: 'number', description: 'Rule: Hit up to [Area] targets with one Attack Test. [Num Targets] added to TN.\n\nCounter: Armor +2 effective vs Area attacks.\n\nEff Rating: +[Area].\n\nDesign: Per [Eff Rating]^2 x Multiplier) Mp.' },
    { id: 'chaser', label: 'Chaser', type: 'check', description: 'Rule: Negates Shift attack penalty. Cannot combine with Penetration.\n\nCounter: Shield adds additional +2 TN.\n\nEff Rating: +1.\n\nDesign: Per [Eff Rating].' },
    { id: 'dinab', label: 'DINAB', type: 'number', description: 'Rule: Utility can act autonomously with Computer Skill equal to [DINAB].\n\nCounter: DINAB degrades by 1 on failed tests and will crash on all-1s.\n\nEff Rating: +[DINAB].\n\nDesign: Per [Eff Rating]^2 x Multiplier) Mp.' },
    { id: 'limit', label: 'Limit', type: 'check', description: 'Rule: Restrict utility to one target type, reducing effective rating.\n\nCounter: Non-matching target types are unaffected.\n\nEff Rating: -1.\n\nDesign: Per [Eff Rating].' },
    { id: 'oneshot', label: 'One-Shot', type: 'check', description: 'Rule: Single-use program, much smaller size. Must load fresh copy each use.\n\nCounter: Tar Baby/Tar Pit crashes wipe all copies on the Deck.\n\nEff Rating: No change.\n\nDesign: x1.5 Actual: x0.25.' },
    { id: 'optimization', label: 'Optimization', type: 'check', description: 'Rule: Reduces actual size, increases design size.\n\nEff Rating: No change.\n\nDesign: x2.0. Actual: x0.5.' },
    { id: 'penetration', label: 'Penetration', type: 'check', description: 'Rule: Negates Shield attack penalty. Cannot combine with Chaser.\n\nCounter: Shift adds additional +2 TN.\n\nEff Rating: +1.\n\nDesign: Per [Eff Rating].' },
    { id: 'skulk', label: 'Skulk', type: 'number', description: 'Rule: When this utility crashes IC, reduce tally increase by [Skulk].\n\nEff Rating: +[Skulk].\n\nDesign: Per [Eff Rating].' },
    { id: 'squeeze', label: 'Squeeze', type: 'check', description: 'Rule: Compresses upload by 50%; must decompress before use.\n\nEff Rating: No change.\n\nDesign: Per ([Eff Rating] + 1).' },
    { id: 'targeting', label: 'Targeting', type: 'check', description: 'Rule: -2 TN on attacks made with this utility.\n\nEff Rating: +2.\n\nDesign: Per [Eff Rating].' },
  ];

  const OPERATIONAL_OPTIONS = ['dinab', 'oneshot', 'optimization', 'squeeze'];
  const PROGRAMS = [
    { key: 'analyze', display: 'Analyze', category: 'Operational', description: 'Reduces TN for Systems Tests that identify IC, programs, and other host resources.\n\nValid Operations: Analyze [IC|Icon|Security], Locate IC.' },
    { key: 'crash', display: 'Crash', category: 'Operational', description: 'Reduces TN on attempts to crash a program or host.\n\nValid Operations: Crash [Application|Host].' },
    { key: 'defuse', display: 'Defuse', category: 'Operational', description: 'Reduces TN to defuse data bombs.\n\nValid Operations: [File|Slave] Subsystem Test.' },
    { key: 'deception', display: 'Deception', category: 'Operational', description: 'Reduces TN for Access Tests.\n\nValid Operations: Graceful Logoff, Logon.' },
    { key: 'decrypt', display: 'Decrypt', category: 'Operational', description: 'Reduces TN to Decrypt (defeat) Scramble IC.\n\nValid Operations: Decrypt [Access|File|Slave].' },
    { key: 'disinfect', display: 'Disinfect', category: 'Operational', description: 'Reduces TN to destroy worms.\n\nValid Operations: [Access|Control|Index|File|Slave] Subsystem Test.' },
    { key: 'evaluate', display: 'Evaluate', category: 'Operational', description: 'Searches for valuable data in a host. Degrades 1-3 after each run.\n\nValid Operations: Locate Paydata.' },
    { key: 'mirrors', display: 'Mirrors', category: 'Operational', description: 'Reduces TN for decoy operations.\n\nValid Operations: Decoy.' },
    { key: 'read_write', display: 'Read/Write', category: 'Operational', description: 'Reduces TN for Systems Tests related to data.\n\nValid Operations: Download Data, Edit File.' },
    { key: 'relocate', display: 'Relocate', category: 'Operational', description: 'Reduces TN on Control Test to spoof Trace IC during location cycle.\n\nValid Operations: Control Test.' },
    { key: 'scanner', display: 'Scanner', category: 'Operational', description: 'Reduces TN to locate other Deckers and Frames.\n\nValid Operations: Locate [Decker|Frame].' },
    { key: 'validate_pgm', display: 'Validate', category: 'Operational', description: 'Reduces TN for Administrative System Tests.\n\nValid Operations: Validate Passcode.' },
    { key: 'compressor', display: 'Compressor', category: 'Special', description: 'Reduce transfer file size by 50%. Max file = Rating x 100 Mp.', options: [] },
    { key: 'sleaze', display: 'Sleaze', category: 'Special', description: 'Passive. Increases Detection Factor. ((Masking + Sleaze) / 2)', options: [] },
    { key: 'attack', display: 'Attack', category: 'Offensive', description: 'Standard cybercombat. Multiplier varies by damage level chosen.', options: ['area', 'chaser', 'dinab', 'limit', 'oneshot', 'optimization', 'penetration', 'skulk', 'targeting'] },
    { key: 'black_hammer', display: 'Black Hammer', category: 'Offensive', description: 'Decker version of Black IC, minus the Blaster-like capabilities. Lethal damage to deckers. Uses standard program cap.', options: ['oneshot', 'optimization', 'targeting'] },
    { key: 'hog', display: 'Hog', category: 'Offensive', description: 'Enemy Decker Virus: Reduces rating and crashes deck programs in sequence.', options: ['dinab', 'oneshot', 'optimization', 'targeting'] },
    { key: 'killjoy', display: 'Killjoy', category: 'Offensive', description: 'Decker version of non-lethal Black IC, minus the Blaster-like capabilities. Stun damage to deckers. Uses standard program cap.', options: ['oneshot', 'optimization', 'targeting'] },
    { key: 'lock_on', display: 'Lock-On', category: 'Offensive', description: 'Maneuver aid. Lowers YOUR Sensor Test TN (by [Rating]) to hold a lock on an opposing icon that maneuvers to evade you.', options: ['oneshot', 'optimization'] },
    { key: 'poison', display: 'Poison', category: 'Offensive', description: 'Decker version of Acid Crippler. Attacks enemy MPCP Bod attribute.', options: ['area', 'dinab', 'oneshot', 'optimization', 'targeting'] },
    { key: 'restrict', display: 'Restrict', category: 'Offensive', description: 'Decker version of Binder Crippler. Attacks enemy MPCP Evasion attribute.', options: ['area', 'dinab', 'oneshot', 'optimization', 'targeting'] },
    { key: 'reveal', display: 'Reveal', category: 'Offensive', description: 'Decker version of Marker Crippler. Attacks enemy MPCP Masking attribute.', options: ['area', 'dinab', 'oneshot', 'optimization', 'targeting'] },
    { key: 'slow', display: 'Slow', category: 'Offensive', description: 'Slows proactive IC execution speed. Net successes reduce IC actions.', options: ['area', 'dinab', 'oneshot', 'optimization', 'targeting'] },
    { key: 'steamroller', display: 'Steamroller', category: 'Offensive', description: 'Inflicts [Rating]D to Tar-IC, and is immune to their effects.', options: ['dinab', 'oneshot', 'optimization', 'skulk', 'targeting'] },
    { key: 'armor', display: 'Armor', category: 'Defensive', description: 'Reduces Power of IC/decker attacks against the persona. Loses 1 rating each time the decker takes damage (a hit that lands 1+ boxes). Can be reloaded via Swap Memory.', options: ['optimization'] },
    { key: 'camo', display: 'Camo', category: 'Defensive', description: 'Adds [Rating] to Trace Factor. Also reduces Redirect Datatrail TN.', options: ['oneshot', 'optimization'] },
    { key: 'cloak', display: 'Cloak', category: 'Defensive', description: "Maneuver aid. Lowers YOUR Evasion Test TN (by [Rating]) when you maneuver (Evade/Parry/Position) against an opposing icon's Sensor Rating.", options: ['oneshot', 'optimization'] },
    { key: 'medic', display: 'Medic', category: 'Defensive', description: 'Heals persona damage. Loses 1 rating each use. Can be reloaded via Swap Memory.', options: ['dinab', 'optimization'] },
    { key: 'restore', display: 'Restore', category: 'Defensive', description: 'Repairs BEMS (persona attribute) damage from cripplers/rippers. 1 pt per 2 successes. Cannot fix permanent chip damage.', options: ['dinab', 'oneshot', 'optimization'] },
    { key: 'shield', display: 'Shield', category: 'Defensive', description: 'Parries attacks. Can reduce attacker net successes, as well as Crippler/Ripper IC successes. Loses 1 rating each use. Can be reloaded via Swap Memory.', options: ['optimization'] },
  ].map(program => ({
    ...program,
    options: program.options || (program.category === 'Operational' ? OPERATIONAL_OPTIONS : []),
  }));

  const PROGRAM_BY_KEY = Object.fromEntries(PROGRAMS.map(program => [program.key, program]));
  const PROGRAM_BY_DISPLAY = Object.fromEntries(PROGRAMS.map(program => [program.display.toLowerCase(), program]));

  function keyOf(value) {
    const normalized = String(value || '').trim().toLowerCase();
    if (!normalized) return '';
    if (PROGRAM_BY_KEY[normalized]) return normalized;
    if (normalized === 'read/write') return 'read_write';
    if (normalized === 'validate') return 'validate_pgm';
    const byDisplay = PROGRAM_BY_DISPLAY[normalized];
    return byDisplay ? byDisplay.key : normalized.replace(/[^a-z0-9]+/g, '_').replace(/^_+|_+$/g, '');
  }

  function get(value) {
    return PROGRAM_BY_KEY[keyOf(value)] || null;
  }

  global.MatrixPrograms = Object.freeze({
    programs: Object.freeze(PROGRAMS.map(Object.freeze)),
    options: Object.freeze(OPTION_DEFS.map(Object.freeze)),
    get,
    keyOf,
  });
})(window);