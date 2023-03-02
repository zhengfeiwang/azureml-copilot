import json
import os
import typing
from pathlib import Path

from azureml_copilot.consts import Macros


class WorkspaceConfig:

    LOCAL_CONFIG_PATH = Path(os.path.expanduser("~")) / ".azureml" / "azureml_copilot"

    def __init__(
        self,
        subscription_id: str,
        resource_group_name: str,
        workspace_name: str,
        region: str,
    ):
        self.subscription_id = subscription_id
        self.resource_group_name = resource_group_name
        self.workspace_name = workspace_name
        self.region = region

    @staticmethod
    def load_local_config() -> typing.Dict[str, "WorkspaceConfig"]:
        workspaces = dict()
        with open(WorkspaceConfig.LOCAL_CONFIG_PATH, "r") as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            (
                name,
                subscription_id,
                resource_group_name,
                workspace_name,
                region,
            ) = line.split()
            resource_group_name = resource_group_name.replace(
                Macros.DPV2_SAMPLE_WORKSPACE_NAME_MACRO,
                Macros.resolve_dpv2_sample_workspace_macro(),
            ).replace(
                Macros.PIPELINES_SAMPLE_WORKSPACE_NAME_MACRO,
                Macros.resolve_pipelines_sample_workspace_macro(),
            )
            workspace_name = workspace_name.replace(
                Macros.DPV2_SAMPLE_WORKSPACE_NAME_MACRO,
                Macros.resolve_dpv2_sample_workspace_macro(),
            ).replace(
                Macros.PIPELINES_SAMPLE_WORKSPACE_NAME_MACRO,
                Macros.resolve_pipelines_sample_workspace_macro(),
            )
            workspaces[name] = WorkspaceConfig(
                subscription_id, resource_group_name, workspace_name, region
            )
        return workspaces

    @property
    def json(self) -> str:
        return json.dumps(
            {
                "subscription_id": self.subscription_id,
                "resource_group": self.resource_group_name,
                "workspace_name": self.workspace_name,
            },
            indent=4,
        )

    @property
    def environ(self) -> str:
        return "\n".join(
            [
                f"ML_SUBSCRIPTION_ID='{self.subscription_id}'",
                f"ML_RESOURCE_GROUP='{self.resource_group_name}'",
                f"ML_LOCATION='{self.region}'",
                f"ML_WORKSPACE_NAME='{self.workspace_name}'",
            ]
        )

    @property
    def url(self) -> str:
        return f"https://ml.azure.com/?wsid=/subscriptions/{self.subscription_id}/resourceGroups/{self.resource_group_name}/providers/Microsoft.MachineLearningServices/workspaces/{self.workspace_name}"


WORKSPACES = WorkspaceConfig.load_local_config()
