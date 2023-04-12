# may make conda environment name a variable
Write-Host "switch to v2-github conda environment..."
conda activate v2-github

Write-Host "cd to azure-ai-ml directory..."
$cwd = Get-Location
Set-Location ~/source/repos/azure-sdk-for-python/sdk/ml/azure-ai-ml

Write-Host "execute black command..."
black --config ../../../eng/black-pyproject.toml .

# recover context
Set-Location $cwd
conda deactivate
