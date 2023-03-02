from azure.ai.ml import MLClient


def _get_credential():
    from azure.identity import CredentialUnavailableError, DefaultAzureCredential

    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except CredentialUnavailableError:
        from azure.identity import InteractiveBrowserCredential

        credential = InteractiveBrowserCredential()
    return credential


# explicitly specify workspace info
def init_ml_client(
    subscription_id: str,
    resource_group_name: str,
    workspace_name: str,
) -> MLClient:
    return MLClient(
        subscription_id=subscription_id,
        resource_group_name=resource_group_name,
        workspace_name=workspace_name,
        credential=_get_credential(),
    )


# from .azureml/config.json
def init_ml_client_from_config() -> MLClient:
    return MLClient.from_config(credential=_get_credential())
