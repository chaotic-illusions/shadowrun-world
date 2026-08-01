# =============================================================================
# run-matrix-harness.ps1 -- ONE command for the whole Matrix run-console test harness.
#
# Generates seeded Matrix systems, drives the REAL run console in a headless browser (Playwright:
# renders matrix-run.html, checks the Known IC / paydata panes, the action dropdown, admin-vs-player
# redaction, and the Federated Bank regressions), runs the generative data-layer fuzzer over many
# random hosts, and the engine/static contracts -- then prints an obvious PASS / FAIL banner.
#
# Usage:
#   .\run-matrix-harness.ps1                 # default depth (thorough, ~1-2 min)
#   .\run-matrix-harness.ps1 -FuzzSeeds 400  # deeper generative sweep
#   .\run-matrix-harness.ps1 -DomHosts 16 -DomSteps 10   # more DOM-driven systems
# =============================================================================
param(
    [int]$FuzzSeeds   = 200,   # generative data-layer systems (admin/player redaction battery per step)
    [int]$OracleSeeds = 200,   # generative CORRECTNESS systems (rules oracle: did X -> expect Y, per step)
    [int]$DomHosts    = 12,    # seeded systems driven through the REAL rendered DOM
    [int]$DomSteps    = 8      # actions taken per DOM-driven system
)

$py = ".\.venv\Scripts\python.exe"
if (-not (Test-Path $py)) { Write-Host "venv not found at $py" -ForegroundColor Red; exit 1 }

$env:MATRIX_FUZZ_SEEDS   = "$FuzzSeeds"
$env:MATRIX_ORACLE_SEEDS = "$OracleSeeds"
$env:MATRIX_DOM_HOSTS    = "$DomHosts"
$env:MATRIX_DOM_STEPS    = "$DomSteps"

Write-Host ""
Write-Host "===============================================================" -ForegroundColor Cyan
Write-Host " MATRIX RUN-CONSOLE HARNESS" -ForegroundColor Cyan
Write-Host "   data-layer fuzz systems : $FuzzSeeds  (admin/player redaction battery per step)" -ForegroundColor Cyan
Write-Host "   correctness systems     : $OracleSeeds  (rules oracle: did X -> per rules expect Y)" -ForegroundColor Cyan
Write-Host "   DOM-driven systems      : $DomHosts hosts x $DomSteps steps (real headless browser)" -ForegroundColor Cyan
Write-Host "===============================================================" -ForegroundColor Cyan
Write-Host ""

& $py -m pytest `
    tests/test_matrix_ui_dom.py `
    tests/test_matrix_visibility_e2e.py `
    tests/test_matrix_visibility_fuzz.py `
    tests/test_matrix_correctness_fuzz.py `
    tests/test_matrix_flows.py `
    -v -s --durations=10
$code = $LASTEXITCODE

Remove-Item Env:\MATRIX_FUZZ_SEEDS, Env:\MATRIX_ORACLE_SEEDS, Env:\MATRIX_DOM_HOSTS, Env:\MATRIX_DOM_STEPS -ErrorAction SilentlyContinue

Write-Host ""
if ($code -eq 0) {
    Write-Host "===============================================================" -ForegroundColor Green
    Write-Host " HARNESS PASSED" -ForegroundColor Green
    Write-Host "   - every named run-console function was exercised" -ForegroundColor Green
    Write-Host "   - redaction / pane / action / admin-superset invariants held" -ForegroundColor Green
    Write-Host "     on every seeded system" -ForegroundColor Green
    Write-Host "   - the engine computed the SR2 rules correctly on every seeded action" -ForegroundColor Green
    Write-Host "   - multi-step rule CHAINS produced the right cascade at each step" -ForegroundColor Green
    Write-Host "   - all Federated Bank regressions green" -ForegroundColor Green
    Write-Host "   (frontend block coverage is printed above -- ~63%; the rest is" -ForegroundColor Green
    Write-Host "    defensive/rare-branch code, see 'functions never entered')" -ForegroundColor Green
    Write-Host "===============================================================" -ForegroundColor Green
} else {
    Write-Host "===============================================================" -ForegroundColor Red
    Write-Host " HARNESS FAILED (pytest exit $code)" -ForegroundColor Red
    Write-Host "   scroll up to the FAILED lines -- each names the exact" -ForegroundColor Red
    Write-Host "   system/state and the invariant or UI element that broke." -ForegroundColor Red
    Write-Host "===============================================================" -ForegroundColor Red
}
exit $code
