# Prepare for Linux Transfer
# This script creates a clean archive ready for Linux deployment

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Taxi Service - Prepare for Transfer" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Remove .venv if exists
if (Test-Path ".venv") {
    Write-Host "[1/3] Removing virtual environment..." -ForegroundColor Yellow
    Remove-Item -Recurse -Force .venv
    Write-Host "      Virtual environment removed" -ForegroundColor Green
}

# Remove __pycache__ directories
Write-Host "[2/3] Cleaning Python cache files..." -ForegroundColor Yellow
Get-ChildItem -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
Get-ChildItem -Recurse -Filter "*.pyc" | Remove-Item -Force
Write-Host "      Cache files removed" -ForegroundColor Green

# Create archive
Write-Host "[3/3] Creating archive..." -ForegroundColor Yellow
$archiveName = "taxi_service_linux.zip"
if (Test-Path $archiveName) {
    Remove-Item $archiveName -Force
}

$exclude = @(".venv", "__pycache__", "*.pyc", "*.pyo", "db.sqlite3")
$files = Get-ChildItem -Path . -Exclude $exclude

Compress-Archive -Path $files -DestinationPath $archiveName -Force
Write-Host "      Archive created: $archiveName" -ForegroundColor Green

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Archive Ready!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "File: $archiveName" -ForegroundColor White
Write-Host "Size: $((Get-Item $archiveName).Length / 1MB) MB" -ForegroundColor White
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "  1. Transfer $archiveName to Linux server" -ForegroundColor White
Write-Host "  2. Extract: unzip $archiveName -d taxi_service" -ForegroundColor White
Write-Host "  3. Run: cd taxi_service && bash setup.sh" -ForegroundColor White
Write-Host ""
Write-Host "See TRANSFER_GUIDE.md for detailed instructions" -ForegroundColor Cyan
Write-Host ""

