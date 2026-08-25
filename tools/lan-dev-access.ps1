<#
.SYNOPSIS
    Enable or disable LAN access to the local dev server, for testing the digital sheet
    (or any page) from a phone or another PC on the same network.

.DESCRIPTION
    Start the server first with:
        .\.venv\Scripts\python.exe -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    Then run this script with -Action Enable to open the firewall for it.
    Run -Action Disable when you're done to revert everything it changed.

    Windows auto-generates inbound "TCP/UDP Query User" Block rules for a program the
    first time it tries to listen and the prompt is dismissed or times out. Those Block
    rules silently override a later port-based Allow rule for the SAME program -- Block
    always wins over Allow in Windows Firewall, regardless of which rule is more specific.

    This bit us directly: .venv\Scripts\python.exe on Windows is a launcher stub that
    re-execs a separate shared interpreter (the actual "pythoncore" install), so the
    Block rule Windows created was scoped to THAT path, not the venv Scripts path. A
    plain port-based Allow rule alone was not enough -- the pre-existing Block rule for
    the resolved interpreter path had to be disabled too. This script resolves the real
    interpreter path via `sys.executable` rather than assuming the venv Scripts path,
    and handles both sides (Allow rule + matching Block rules) together.

    Requires elevation. Run from an elevated PowerShell, or right-click > "Run with
    PowerShell" as Administrator.

.EXAMPLE
    .\tools\lan-dev-access.ps1 -Action Enable
    .\tools\lan-dev-access.ps1 -Action Disable
    .\tools\lan-dev-access.ps1 -Action Status
#>
param(
    [ValidateSet('Enable', 'Disable', 'Status')]
    [string]$Action = 'Status'
)

$ruleName = 'Shadowrun World Dev Server (8000)'

function Resolve-DevPythonPath {
    $venvPython = Join-Path $PSScriptRoot '..\.venv\Scripts\python.exe'
    if (-not (Test-Path $venvPython)) {
        throw "No venv python found at $venvPython -- create the venv first (see README Local Development)."
    }
    (& $venvPython -c 'import sys; print(sys.executable)').Trim()
}

function Get-MatchingBlockRules($pythonPath) {
    Get-NetFirewallRule -Direction Inbound -Action Block |
        Where-Object {
            $app = $_ | Get-NetFirewallApplicationFilter -ErrorAction SilentlyContinue
            $app -and $app.Program -and ($app.Program -ieq $pythonPath)
        }
}

switch ($Action) {
    'Status' {
        $rule = Get-NetFirewallRule -DisplayName $ruleName -ErrorAction SilentlyContinue
        if ($rule) {
            Write-Host "Allow rule '$ruleName': present, Enabled=$($rule.Enabled)"
        } else {
            Write-Host "Allow rule '$ruleName': not present"
        }
        $pythonPath = Resolve-DevPythonPath
        $blocks = Get-MatchingBlockRules $pythonPath
        if ($blocks) {
            Write-Host "Block rules for $pythonPath :"
            $blocks | ForEach-Object { Write-Host "  $($_.Name)  Enabled=$($_.Enabled)" }
        } else {
            Write-Host "No Block rules found for $pythonPath."
        }
    }

    'Enable' {
        $pythonPath = Resolve-DevPythonPath
        Write-Host "Resolved interpreter: $pythonPath"

        $blocks = Get-MatchingBlockRules $pythonPath | Where-Object { $_.Enabled }
        if ($blocks) {
            $blocks | Disable-NetFirewallRule
            Write-Host "Disabled $($blocks.Count) pre-existing Block rule(s) for this interpreter."
        }

        if (-not (Get-NetFirewallRule -DisplayName $ruleName -ErrorAction SilentlyContinue)) {
            New-NetFirewallRule -DisplayName $ruleName -Direction Inbound -Protocol TCP `
                -LocalPort 8000 -Profile Private -Action Allow | Out-Null
            Write-Host "Created inbound Allow rule '$ruleName' (TCP 8000, Private profile only)."
        } else {
            Write-Host "Allow rule '$ruleName' already present."
        }
    }

    'Disable' {
        Remove-NetFirewallRule -DisplayName $ruleName -ErrorAction SilentlyContinue
        Write-Host "Removed Allow rule '$ruleName' (if it existed)."

        $pythonPath = Resolve-DevPythonPath
        $blocks = Get-MatchingBlockRules $pythonPath | Where-Object { -not $_.Enabled }
        if ($blocks) {
            $blocks | Enable-NetFirewallRule
            Write-Host "Re-enabled $($blocks.Count) Block rule(s) for this interpreter."
        }

        Set-NetFirewallProfile -Profile Private -LogBlocked False -LogAllowed False -ErrorAction SilentlyContinue
        Write-Host "Reverted Private-profile firewall packet logging to default (off)."
    }
}
