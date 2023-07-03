# get access token from Azure CLI
$json = az account get-access-token | ConvertFrom-Json
$access_token = $json | Select-Object -ExpandProperty accessToken
Write-Host $access_token
# copy to clipboard
$access_token | Set-Clipboard
