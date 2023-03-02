from azureml_copilot.workspace import WORKSPACES, WorkspaceConfig


def list_workspace():
    for workspace_name, workspace_config in WORKSPACES.items():
        print(workspace_name)
        print("  subscription_id:", workspace_config.subscription_id)
        print("  resource_group:", workspace_config.resource_group_name)
        print("  workspace:", workspace_config.workspace_name)
        print("  region:", workspace_config.region)


def get_workspace(workspace_name: str) -> WorkspaceConfig:
    workspace_config = WORKSPACES.get(workspace_name)
    if workspace_config is None:
        raise ValueError(f"Workspace {workspace_name!r} not found!")
    return workspace_config
