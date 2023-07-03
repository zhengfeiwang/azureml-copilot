if (Test-Path -Path ".git" -PathType Container)
{
    Write-Host "This is a git repository, will prune it..."
    # prune branches not on remote
    git fetch --prune && git branch -vv | Select-String -Pattern ': gone]' | ForEach-Object { $_.ToString().Trim().Split(' ')[0] } | ForEach-Object { git branch -D $_ }
    Write-Host "Done!"
}
else {
    Write-Host "This is not a git repository, please navigate to a git repository and try again."
}
