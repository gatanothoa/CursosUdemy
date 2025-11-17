Param(
    [switch]$DryRun
)

$here = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent
Set-Location $here\..\
Write-Host "Iniciando auto-push (DryRun=$DryRun)" -ForegroundColor Cyan
if ($DryRun) {
    python .\scripts\update_readmes.py --dry-run
} else {
    python .\scripts\update_readmes.py --push
}
if ($LASTEXITCODE -eq 0) {
    Write-Host "Proceso finalizado correctamente." -ForegroundColor Green
} else {
    Write-Host "Proceso terminado con errores. Código: $LASTEXITCODE" -ForegroundColor Red
}
