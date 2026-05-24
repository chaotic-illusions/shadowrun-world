param()

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
Push-Location $repoRoot

git config core.hooksPath .githooks
Write-Host "Configured git hooks path: .githooks"
Write-Host "Pre-commit hook enabled."

Pop-Location