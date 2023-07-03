# guide user manually update profile
Write-Host "code $PROFILE"

# black SDK
$ScriptPath = Join-Path -Path $(Get-Location) -ChildPath "black_sdk.ps1  # black SDK"
Write-Host "New-Alias blacksdk $ScriptPath"

# git prune
$ScriptPath = Join-Path -Path $(Get-Location) -ChildPath "git_prune.ps1  # prune merged branches"
Write-Host "New-Alias gitprune $ScriptPath"

# Azure CLI token
$ScriptPath = Join-Path -Path $(Get-Location) -ChildPath "token.ps1  # Azure CLI access token"
Write-Host "New-Alias token $ScriptPath"
