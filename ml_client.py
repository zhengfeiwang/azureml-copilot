from azure.ai.ml import MLClient


# explicitly specify workspace info
def init_ml_client(
    subscription_id: str,
    resource_group_name: str,
    workspace_name: str,
) -> MLClient:
    from azure.identity import DefaultAzureCredential

    return MLClient(
        subscription_id=subscription_id,
        resource_group_name=resource_group_name,
        workspace_name=workspace_name,
        credential=DefaultAzureCredential(),
    )


# from .azureml/config.json
def init_ml_client_from_config() -> MLClient:
    from azure.identity import DefaultAzureCredential

    return MLClient.from_config(credential=DefaultAzureCredential())
