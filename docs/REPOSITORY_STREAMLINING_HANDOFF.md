# Repository Streamlining Handoff

## Objective

Prepare this repository for public release without losing the private sourcebook,
OCR, research, and adventure-preparation material used to build the world data.
The private archive is temporarily committed to the private GitHub repository so
trusted machines can synchronize it. The repository MUST remain private until the
archive and all former source paths have been removed from Git history.

Do this work in a separate clone only after the current data-completion changes
have been committed. The present worktree contains a large, related rollout and
must not be cleaned piecemeal or reset.

## Current Verified State

- Production snapshot:
  `data/shadowrun_prod.db`
- Production SHA-256 after the copyable-text audit and the 2026-09-27 merge of
  player edits made on the live server since 2026-09-15 (deployed to the server):
  `093eb9fed2d2a611235dbf5a06ae9b8244bdb89b10f2d9294f8fd413150c33ee`
- Portable seed SHA-256:
  `52de4ef8413149d9e63c521564240f2d0a00bfcf2f09fe1803fcf9e2ca259208`
- World counts: 821 organizations, 1,183 locations, 874 characters including
  10 PCs, 67 RTGs, 7 Matrix hosts, 13 PC-owned contacts, and 1 adventure log.
- The portable seed contains 862 NPCs and excludes PCs and PC-associated state.
- `scripts/audit_copyable_world_text.py` reports zero findings on production.
- SQLite integrity is `ok`; `PRAGMA foreign_key_check` returns zero rows.
- A byte-identical pre-cleanup backup is retained outside Git under
  `data/backups/shadowrun_prod-pre-copyable-text-audit-20260927-184034.db`.

## Public Release State

- The 26 sourcebook PDFs, totaling 1,258,762,258 bytes, now live under
  `reference-private/`. Their former public-tree paths are deleted.
- `reference-private/` contains 588 files totaling approximately 1.212 GiB. No
  individual file exceeds GitHub's 100 MB per-file limit.
- The archive is ignored for normal local additions but force-added to Git for
  temporary synchronization through the private remote. Once tracked, `.gitignore`
  does not prevent updates to existing archive files from being committed.
- Git's packed object store is approximately 1.18 GiB. Deleting working-tree
  files alone will not reduce that history.
- The public tree contains 48 maintained test modules and passes 1,851 tests with
  1 skip using an unfiltered `pytest -q` command.
- The local archive contains 73 sourcebook provenance, rehearsal, and one-time
  migration/audit test modules. They are excluded from public pytest collection.
- Repository-wide text hygiene and the production copyable-text audit both pass.

## Protected Public Surface

Keep these in the public repository:

- `app/`
- `frontend/`
- `alembic/` and every applied migration
- `seed.py`
- `data/world_seed.json`
- `scripts/audit_copyable_world_text.py`
- Runtime and application tests, including `tests/test_copyable_world_text.py`
- Deployment files, dependency manifests, and active operational documentation
- `tools/check_text_hygiene.py`

No database file is committed. The production snapshot is a local-only file, and
`LOCAL_REFERENCE.md` (ignored) records where it and the private archive live.

Do not remove an Alembic migration because it looks historical. Applied migration
IDs are part of the database contract.

## Private Archive

The temporarily tracked private archive contains:

```text
reference-private/
  sourcebooks/
    pdf-and-ocr/
    research/
    book-ledgers/
    extraction/
  adventures/
    analysis/
    prep/
  ingest/
    specs/
    rehearsal-tests/
    one-time-tools/
    workflow/
    audits/
  generated/
    npc_dossiers_full.txt
  manifests/
    checksums.sha256
    source-path-map.csv
```

The archive contains 586 checksummed payload files plus `source-path-map.csv`
and `checksums.sha256`. It is excluded from Docker builds, pytest collection, and
repository-wide text-hygiene scans.

Primary move candidates:

- `docs/Sourcebooks/` -> `reference-private/sourcebooks/pdf-and-ocr/`
- `docs/sourcebook-ingest/research/` -> `reference-private/sourcebooks/research/`
- `docs/sourcebook-ingest/books/` -> `reference-private/sourcebooks/book-ledgers/`
- `docs/sourcebook-ingest/extraction/` -> `reference-private/sourcebooks/extraction/`
- `docs/adventure-analysis/` -> `reference-private/adventures/analysis/`
- `docs/adventure-prep/` -> `reference-private/adventures/prep/`
- `scripts/adventure_ingest/specs/` -> `reference-private/ingest/specs/`
- 73 sourcebook-only and one-time audit tests -> `reference-private/ingest/rehearsal-tests/`
- Completed one-time ingest scripts -> `reference-private/ingest/one-time-tools/`
- `npc_dossiers_full.txt` -> `reference-private/generated/`

The `/reference-private/` exclusion remains active in `.gitignore` to prevent
accidental additions after the archive is purged. `.dockerignore` prevents the
temporarily tracked archive from entering application images.

After cloning on another trusted machine, verify the payload before removing any
other copy:

```powershell
$root = (Resolve-Path reference-private).Path
$bad = @()
foreach ($line in Get-Content reference-private/manifests/checksums.sha256) {
  if ($line -notmatch '^([0-9a-f]{64})  (.+)$') { $bad += $line; continue }
  $actual = (Get-FileHash -LiteralPath (Join-Path $root $Matches[2]) -Algorithm SHA256).Hash.ToLowerInvariant()
  if ($actual -ne $Matches[1]) { $bad += $Matches[2] }
}
if ($bad.Count) { $bad; throw 'archive verification failed' }
```

## Test Classification

The archived sourcebook modules generally match sourcebook slugs and end in:

- `_spec.py`
- `_loader_rehearsal.py`
- `_fastapi_rehearsal.py`

The generic loader contract and all 48 maintained application modules remain
public. Unfiltered public pytest now passes.

## Markdown Review

Do not bulk-delete Markdown by age. Classify each file as one of:

1. Active operator/developer documentation: keep and update.
2. Private source-derived evidence or adventure preparation: archive privately.
3. Historical rollout status now superseded by the seed and audit: remove after
   preserving any unique operational facts.
4. Duplicate or stale instructions: merge into the active guide, then remove.

At minimum, review all Markdown under `docs/`, top-level rollout notes, and
generated sourcebook ledgers. Check references with `rg` before removal. Keep the
main `README.md`, `AGENTS.md`, active architecture notes, Matrix operating guides,
and this handoff until the public rewrite is complete.

## Mandatory Steps Before Public Release

1. Keep the existing GitHub repository private.
2. Clone or pull the private repository on the second trusted machine.
3. Verify `reference-private/manifests/checksums.sha256` on that machine.
4. Copy `reference-private/` outside every repository clone or create another
  verified offline backup. Git history must not be the only remaining copy.
5. In the working repository, remove `reference-private/` from the index while
  retaining the ignored local files: `git rm -r --cached reference-private`.
6. Commit that removal, but do not assume the files are gone from history.
7. Create a disposable `--mirror` clone for the destructive history rewrite.
8. Use `git filter-repo`, not `filter-branch`, to remove `reference-private/` and
  every former private path from every branch and tag.
9. Expire reflogs and garbage-collect the rewritten mirror, then inspect the
  largest remaining objects and all historical paths.
10. Run a secret scan and the complete validation checklist below from a fresh
   non-mirror clone of the rewritten repository.
11. Publish to a new empty public remote first. Prefer a new remote over reusing
   the private one because old pull-request refs, forks, release assets, caches,
   and GitHub retention may survive a force-push.
12. Make the new remote public only after a fresh anonymous-style clone confirms
   that no private path or blob is reachable.

Adding `.gitignore` rules does not untrack files and does not erase Git history.
`git rm --cached` removes files only from the current index. History rewriting is
required to remove the approximately 1.26 GB sourcebook corpus from old commits.

## History Rewrite

Install `git-filter-repo`, then work in a disposable mirror clone. Start with the
known private paths and add any older aliases discovered by `git log --all --name-only`:

```powershell
git filter-repo --invert-paths `
  --path reference-private `
  --path docs/Sourcebooks `
  --path npc_dossiers_full.txt `
  --path docs/sourcebook-ingest `
  --path docs/adventure-analysis `
  --path docs/adventure-prep `
  --path scripts/adventure_ingest/specs `
  --path scripts/ocr_sourcebooks.py `
  --path scripts/audit_world_data.py
```

Add the exact historical paths of sourcebook-only tests, one-time ingest tools,
and sourcebook workflow instructions from
`reference-private/manifests/source-path-map.csv`. Do not remove the active seed,
production snapshot, migrations, or runtime application code.

After rewriting, inspect the largest remaining objects and verify that no PDF or
private path remains:

```powershell
git rev-list --objects --all
git log --all -- docs/Sourcebooks
git ls-files '*.pdf'
git ls-files reference-private
git count-objects -vH
```

The fillable character sheet needs a separate licensing decision. It is not part
of the 26 sourcebook corpus and should not be removed automatically with that tree.

## Validation Checklist

Run from the proposed public tree before any push:

```powershell
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe scripts\audit_copyable_world_text.py
.\.venv\Scripts\python.exe -m pytest -q tests\test_seed.py tests\test_full_world_seed.py
.\.venv\Scripts\python.exe -c "import app.main"
.\.venv\Scripts\python.exe -m alembic heads
.\.venv\Scripts\python.exe tools\check_text_hygiene.py
git diff --check
```

Also verify:

- Alembic reports one head.
- The portable seed round-trips exactly through a fresh database.
- Production counts and hashes match the values recorded above.
- `docker build` does not include `reference-private/`, databases from
  `data/backups/`, `.git/`, `.venv/`, or other local artifacts.
- `git ls-files reference-private` returns no output.
- `git rev-list --objects --all` contains no `reference-private`, removed PDF,
  sourcebook-ingest, adventure-prep, or archived-test path.
- No blob from `checksums.sha256` can be found by hash in rewritten history.
- A secret scan reports no tokens, credentials, or private source extracts.
- A fresh clone of the rewritten public remote can run the application and tests
  without access to `reference-private/`.

## Stop Conditions

Stop and ask the project owner before:

- Force-pushing or deleting the current remote.
- Dropping the production snapshot or portable seed.
- Removing any applied migration.
- Deleting a document with unique operational instructions.
- Archiving a generic loader/runtime test rather than a sourcebook-specific test.
- Removing the fillable character sheet without a licensing decision.

The public-history rewrite changes commit identities and invalidates downstream
clones. Preserve the private pre-rewrite repository and verified external archive
until the new public remote has been cloned and validated independently. Never
change the current private remote's visibility before that process is complete.