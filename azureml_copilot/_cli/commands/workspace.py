from azureml_copilot.consts import WORKSPACES
from azureml_copilot.utils import workspace_config_json_string


def list_workspaces():
    for workspace_name, workspace_config in WORKSPACES.items():
        print(workspace_name)
        print("  subscription_id:", workspace_config.subscription_id)
        print("  resource_group:", workspace_config.resource_group_name)
        print("  workspace:", workspace_config.workspace_name)
        print("  region:", workspace_config.region)


def get_workspace(workspace_name: str):
    workspace_config = WORKSPACES.get(workspace_name)
    if workspace_config is None:
        raise ValueError(f"Workspace {workspace_name!r} not found!")
    print(workspace_config_json_string(workspace_config))
