# Repository Streamlining Handoff

## Objective

Prepare this repository for public release without losing the private sourcebook,
OCR, research, and adventure-preparation material used to build the world data.
Keep the application, migrations, portable seed, audited production snapshot, and
maintained tests public. Move source-derived working material into one local,
ignored archive and remove it from Git history before republishing.

Do this work in a separate clone only after the current data-completion changes
have been committed. The present worktree contains a large, related rollout and
must not be cleaned piecemeal or reset.

## Current Verified State

- Production snapshot:
  `data/prod-snapshot/2026-09-15/shadowrun_prod.db`
- Production SHA-256 after the copyable-text audit:
  `0bbaa01dc98cbcb877818c0d3d68ea1d68f2ad51bb52864f2fe72c65880679e9`
- Portable seed SHA-256:
  `52de4ef8413149d9e63c521564240f2d0a00bfcf2f09fe1803fcf9e2ca259208`
- World counts: 821 organizations, 1,183 locations, 872 characters including
  10 PCs, 67 RTGs, 7 Matrix hosts, 11 PC-owned contacts, and 1 adventure log.
- The portable seed contains 862 NPCs and excludes PCs and PC-associated state.
- `scripts/audit_copyable_world_text.py` reports zero findings on production.
- SQLite integrity is `ok`; `PRAGMA foreign_key_check` returns zero rows.
- A byte-identical pre-cleanup backup is retained outside Git under
  `data/backups/shadowrun_prod-pre-copyable-text-audit-20260927-184034.db`.

## Public Release State

- The 26 sourcebook PDFs, totaling 1,258,762,258 bytes, now live under the
  ignored local `reference-private/` archive. Their public-tree paths are deleted.
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
- `data/prod-snapshot/2026-09-15/shadowrun_prod.db`
- `scripts/audit_copyable_world_text.py`
- `scripts/clean_copyable_world_text.py`
- `scripts/copyable_text_rewrites_*.py`
- Runtime and application tests, including `tests/test_copyable_world_text.py`
- Deployment files, dependency manifests, and active operational documentation
- `tools/check_text_hygiene.py`

Do not remove an Alembic migration because it looks historical. Applied migration
IDs are part of the database contract.

## Private Archive

The ignored local working copy now contains:

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

The archive contains 733 files. It is excluded by `.gitignore`, `.dockerignore`,
pytest collection, and repository-wide text-hygiene scans.

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

The `/reference-private/` exclusion is active in `.gitignore` and `.dockerignore`;
Docker does not read `.gitignore`.

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

## Safe Execution Order

1. Commit and push the completed public-tree and data changes.
2. Clone that branch to the other local machine requested by the project owner.
3. Create a disposable mirror clone for history rewriting.
4. Use `git filter-repo`, not `filter-branch`, to remove private paths from every
   historical commit.
5. Re-run secret scanning and validation against the rewritten clone.
6. Publish to a new empty remote first. Force-push the old public remote only
    after review and explicit approval.

Adding `.gitignore` rules does not untrack files and does not erase Git history.
`git rm --cached` removes files only from the current index. History rewriting is
required to remove the approximately 1.26 GB sourcebook corpus from old commits.

## History Rewrite

Install `git-filter-repo`, then work in a disposable mirror clone. Start with the
known private paths and add any older aliases discovered by `git log --all --name-only`:

```powershell
git filter-repo --invert-paths `
  --path docs/Sourcebooks `
  --path npc_dossiers_full.txt `
  --path docs/sourcebook-ingest/books `
  --path docs/sourcebook-ingest/extraction `
  --path docs/sourcebook-ingest/research `
  --path docs/adventure-analysis `
  --path docs/adventure-prep `
  --path scripts/adventure_ingest/specs
```

If sourcebook-only tests and one-time tools are removed from the public tree, add
their exact historical paths to the rewrite command. Do not remove the active seed,
production snapshot, migrations, or runtime application code.

After rewriting, inspect the largest remaining objects and verify that no PDF or
private path remains:

```powershell
git rev-list --objects --all
git log --all -- docs/Sourcebooks
git ls-files '*.pdf'
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
- `git ls-files` shows no private reference paths.
- `git rev-list --objects --all` shows no removed PDF or archive path.
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

The public-history rewrite is destructive for commit identities and downstream
clones. Preserve the private pre-rewrite repository and checksum manifests until
the new public remote has been cloned and validated independently.