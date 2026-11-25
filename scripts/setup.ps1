# Create venv and install dependencies (Windows PowerShell)
$ErrorActionPreference = "Stop"
$Root = Split-Path $PSScriptRoot -Parent
Set-Location $Root

$Venv = Join-Path $Root ".venv"
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    throw "python not found on PATH"
}

Write-Host "Project root: $Root"
if (-not (Test-Path $Venv)) {
    Write-Host "Creating .venv ..."
    python -m venv $Venv
} else {
    Write-Host ".venv already exists"
}

$Pip = Join-Path $Venv "Scripts\pip.exe"
Write-Host "Upgrading pip ..."
& $Pip install --upgrade pip
Write-Host "Installing requirements.txt ..."
& $Pip install -r (Join-Path $Root "requirements.txt")

Write-Host ""
Write-Host "Done. Activate with:"
Write-Host "  $($Venv)\Scripts\Activate.ps1"