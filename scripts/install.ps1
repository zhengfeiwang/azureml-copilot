# guide user manually update profile
Write-Host "code `$PROFILE"

# black SDK
$ScriptPath = Join-Path -Path $(Get-Location) -ChildPath "black_sdk.ps1  # black SDK"
Write-Host "New-Alias blacksdk $ScriptPath"
