from azureml_copilot.workspace import WORKSPACES


def list_workspace(**kwargs):
    json_format = kwargs.get("json", False)
    environ_format = kwargs.get("environ", False)
    default_format = not (json_format or environ_format)

    for workspace_name, workspace_config in WORKSPACES.items():
        if default_format:
            print(workspace_name)
            print("  subscription_id:", workspace_config.subscription_id)
            print("  resource_group:", workspace_config.resource_group_name)
            print("  workspace:", workspace_config.workspace_name)
            print("  region:", workspace_config.region)
            print("  url:", workspace_config.url)
        else:
            if json_format:
                print(workspace_config.json)
            if environ_format:
                print(workspace_config.environ)


def get_workspace(workspace_name: str, **kwargs) -> None:
    workspace_config = WORKSPACES.get(workspace_name)
    if workspace_config is None:
        raise ValueError(f"Workspace {workspace_name!r} not found!")

    json_format = kwargs.get("json", False)
    url_format = kwargs.get("url", False)
    environ_format = kwargs.get("environ", False)
    all_format = not (json_format or url_format or environ_format)

    if json_format or all_format:
        print(workspace_config.json)
    if url_format or all_format:
        print(workspace_config.url)
    if environ_format or all_format:
        print(workspace_config.environ)
