# PowerShell Helper Script for Question 2 - AttendX Git Workflow
# Student: 23IT057
# This script guides you through Tasks 1 to 6 or performs the steps interactively.

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host " AttendX Test Automation - Git Version Control Helper" -ForegroundColor Yellow
Write-Host "==========================================================" -ForegroundColor Cyan

Write-Host "`n[1] Current Directory:" (Get-Location)

Write-Host "`n--- Checking Python and Tests ---" -ForegroundColor Green
python run_tests.py

Write-Host "`n--- Git Configuration Check ---" -ForegroundColor Green
$userName = git config --global user.name
$userEmail = git config --global user.email

if (-not $userName -or -not $userEmail) {
    Write-Host "Git user name or email is not set globally." -ForegroundColor Yellow
    $inputName = Read-Host "Enter your Name or Roll No (e.g. 23IT057)"
    $inputEmail = Read-Host "Enter your Email (e.g. 23it057@example.com)"
    
    if ($inputName -and $inputEmail) {
        git config --global user.name "$inputName"
        git config --global user.email "$inputEmail"
        Write-Host "Git configured successfully with: $inputName <$inputEmail>" -ForegroundColor Green
    }
} else {
    Write-Host "Configured as: $userName <$userEmail>" -ForegroundColor Cyan
}

Write-Host "`nTo perform the remaining steps manually or view the complete table:" -ForegroundColor White
Write-Host "Refer to file: GIT_WORKFLOW_WALKTHROUGH.md" -ForegroundColor Yellow
Write-Host "`nQuick Command Reference for Stage 1:" -ForegroundColor White
Write-Host "  git init" -ForegroundColor Gray
Write-Host "  git branch -M main" -ForegroundColor Gray
Write-Host "  git status" -ForegroundColor Gray
Write-Host "  git add ." -ForegroundColor Gray
Write-Host '  git commit -m "feat(automation): initial commit with AttendX login and attendance test suites"' -ForegroundColor Gray
Write-Host "  git remote add origin https://github.com/<YOUR_USERNAME>/AttendX-Test-Scripts.git" -ForegroundColor Gray
Write-Host "  git push -u origin main" -ForegroundColor Gray
Write-Host "==========================================================" -ForegroundColor Cyan
