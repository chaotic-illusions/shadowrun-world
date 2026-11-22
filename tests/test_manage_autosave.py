"""Executable tests for the shared edit-modal auto-save helper (frontend/shared.js makeManageAutoSave).

Runs the real helper source under Node against a minimal fake `document` (event listeners plus a
footer status span) with a stubbed async save, the same way tests/test_frontend_polling.py runs
the polling helper. Every edit modal (manage-characters / -locations / -organizations / -rtgs /
-tokens and the six World State modals) relies on these behaviours.
"""

import json
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SHARED_JS = ROOT / "frontend" / "shared.js"

pytestmark = pytest.mark.skipif(shutil.which("node") is None, reason="Node.js is required")

# Plain string (not an f-string) so the JS braces need no escaping; HELPER is spliced in below.
_HARNESS = r"""
const listeners = {};
const document = {
  addEventListener(type, fn) { (listeners[type] = listeners[type] || []).push(fn); },
  createElement() { return { className: '', textContent: '', style: {} }; },
};
HELPER

const statusEl = { className: '', textContent: '', style: {} };
const foot = { querySelector: () => statusEl, insertBefore() {} };
// A fake element: inside the overlay unless `outside`; `noauto` = inside a [data-noautosave] block.
function el(opts = {}) {
  const self = {
    classList: { contains: c => (opts.classes || []).includes(c) },
    closest(sel) {
      if (sel === '#ov') return opts.outside ? null : {};
      if (sel === '[data-noautosave]') return opts.noauto ? {} : null;
      if (sel === 'button') return opts.button ? self : null;
      return null;
    },
  };
  return self;
}
const fire = (type, target) => (listeners[type] || []).forEach(fn => fn({ target }));
const sleep = ms => new Promise(r => setTimeout(r, ms));

const model = { v: 'a' };
const saved = [];
let inflight = 0, maxInflight = 0;
const saver = makeManageAutoSave({
  overlayId: 'ov', foot: () => foot, delay: 30,
  snapshot: () => JSON.stringify(model),
  save: async () => {
    inflight++; maxInflight = Math.max(maxInflight, inflight);
    const v = model.v;
    await sleep(15);
    inflight--;
    if (!v) throw new Error('Name is required');
    saved.push(v);
  },
});
const fails = [];
const check = (label, cond) => { if (!cond) fails.push(label + ' [saved=' + JSON.stringify(saved) + ', status=' + statusEl.textContent + ']'); };

(async () => {
  saver.open();
  check('open shows the idle status', statusEl.textContent === 'Changes save automatically');

  // Typing is debounced: three keystrokes, one save of the latest value.
  const input = el();
  model.v = 'ab'; fire('input', input);
  model.v = 'abc'; fire('input', input);
  check('nothing saved before the debounce fires', saved.length === 0);
  await sleep(90);
  check('one save after typing stops, with the latest value', JSON.stringify(saved) === '["abc"]');
  check('status says saved', statusEl.textContent === 'All changes saved');

  // An event with nothing changed (e.g. blur after the debounced save) doesn't save again.
  fire('change', input);
  check('unchanged form is not re-saved', (await saver.flush()) === true && saved.length === 1);

  // A select/checkbox change saves right away; flush resolves once it is written.
  model.v = 'sel'; fire('change', input);
  check('flush resolves true once saved', (await saver.flush()) === true);
  check('change event saved', saved[saved.length - 1] === 'sel');

  // Rapid changes are written one at a time, ending on the newest value.
  model.v = 'x'; fire('change', input);
  await sleep(1);
  model.v = 'y'; fire('change', input);
  await saver.flush();
  check('saves never overlap', maxInflight === 1);
  check('last write is the newest value', saved[saved.length - 1] === 'y');

  // Fields that aren't record fields never trigger a save.
  const n = saved.length;
  model.v = 'skip';
  fire('input', el({ classes: ['sel-search'] }));
  fire('input', el({ noauto: true }));
  fire('input', el({ outside: true }));
  await sleep(60);
  check('search boxes, data-noautosave and outside inputs are ignored', saved.length === n);
  model.v = 'y';

  // A failed save reports why and makes flush (i.e. closing) return false until it is fixed.
  model.v = ''; fire('input', input);
  check('flush is false while the save fails', (await saver.flush()) === false);
  check('status shows the reason', statusEl.textContent === 'Not saved: Name is required');
  model.v = 'fixed'; fire('input', input);
  check('flush is true once a save succeeds again', (await saver.flush()) === true);
  check('the fixed value was saved', saved[saved.length - 1] === 'fixed');

  // Putting the last saved value back after a failure counts as saved (nothing to write).
  model.v = ''; fire('input', input); await saver.flush();
  const before = saved.length;
  model.v = 'fixed'; fire('input', input);
  check('reverting to the saved value clears the error', (await saver.flush()) === true && saved.length === before);
  check('status back to saved', statusEl.textContent === 'All changes saved');

  // A button click inside the modal (tier dot, add row) saves only when something changed.
  const btn = el({ button: true });
  const m = saved.length;
  fire('click', btn); await saver.flush();
  check('click with no change does not save', saved.length === m);
  model.v = 'tier6'; fire('click', btn); await saver.flush();
  check('click after a change saves', saved[saved.length - 1] === 'tier6');

  // cancel() (before deleting the record) drops pending work and later events.
  model.v = 'doomed'; fire('input', input);
  saver.cancel();
  fire('input', input);
  await sleep(60);
  check('cancel drops the pending save', saved[saved.length - 1] === 'tier6');
  check('flush after cancel is a no-op true', (await saver.flush()) === true);

  // Re-opening (next record) starts clean even after a failure on the previous one.
  saver.open();
  model.v = ''; fire('input', input); await saver.flush();
  model.v = 'next'; saver.open();
  check('open() resets the error from the previous record', (await saver.flush()) === true);
  check('open() takes the filled form as the saved baseline', saved[saved.length - 1] !== 'next');

  console.log(JSON.stringify(fails));
})();
"""


def _run_harness() -> list:
    source = SHARED_JS.read_text(encoding="utf-8")
    helper = source[source.index("function makeManageAutoSave(cfg)"):source.index("// -- Heat helpers")]
    result = subprocess.run(["node", "-e", _HARNESS.replace("HELPER", helper)],
                            check=True, capture_output=True, text=True, timeout=30)
    return json.loads(result.stdout.strip().splitlines()[-1])


def test_manage_autosave_behaviour():
    assert _run_harness() == []
