import json

from azureml_copilot.consts import WorkspaceConfig


def workspace_config_json_string(workspace_config: WorkspaceConfig) -> str:
    config_json = {
        "subscription_id": workspace_config.subscription_id,
        "resource_group": workspace_config.resource_group_name,
        "workspace_name": workspace_config.workspace_name,
    }
    return json.dumps(config_json, indent=4)
