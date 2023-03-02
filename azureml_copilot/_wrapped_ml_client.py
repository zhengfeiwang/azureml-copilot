from azure.ai.ml import MLClient

from azureml_copilot.workspace import WORKSPACES
from azureml_copilot._ml_client import init_ml_client


def get_ml_client(workspace_name: str = "sdk-master") -> MLClient:
    workspace_config = WORKSPACES.get(workspace_name)
    if workspace_config is None:
        raise ValueError(f"Workspace {workspace_name!r} not found!")

    return init_ml_client(
        subscription_id=workspace_config.subscription_id,
        resource_group_name=workspace_config.resource_group_name,
        workspace_name=workspace_config.workspace_name,
    )
