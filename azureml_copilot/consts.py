import collections
import datetime
import os
import typing
from pathlib import Path

WorkspaceConfig = collections.namedtuple(
    "WorkspaceConfig",
    ["subscription_id", "resource_group_name", "workspace_name", "region"],
)

LOCAL_CONFIG_PATH = Path(os.path.expanduser("~")) / ".azureml" / "azureml_copilot"


class Macros:
    DPV2_SAMPLE_WORKSPACE_NAME_MACRO = "${{dpv2_sample_workspace_name_macro}}"
    PIPELINES_SAMPLE_WORKSPACE_NAME_MACRO = "${{pipelines_sample_workspace_name_macro}}"


def _resolve_dpv2_sample_workspace_macro_value() -> str:
    # Reference from azureml-examples:
    # https://github.com/Azure/azureml-examples/blob/main/infra/init_environment.sh#L46-L53
    return (datetime.datetime.today() + datetime.timedelta(days=2)).strftime("%Y%m")[2:]


def _resolve_pipelines_sample_workspace_macro_value() -> str:
    # Reference from DesignerPrivatePreviewFeatures:
    # https://github.com/Azure/DesignerPrivatePreviewFeatures/blob/master/azure-ai-ml/scripts/utils.py#L45-L53
    today = datetime.datetime.today()
    weekday = today.weekday()  # weekday: 0-Monday, 6-Sunday
    monday_date = today - datetime.timedelta(days=weekday)
    return monday_date.strftime("%Y%m%d")


def _load_local_config() -> typing.Dict[str, WorkspaceConfig]:
    workspaces = dict()
    with open(LOCAL_CONFIG_PATH, "r") as f:
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
            _resolve_dpv2_sample_workspace_macro_value(),
        ).replace(
            Macros.PIPELINES_SAMPLE_WORKSPACE_NAME_MACRO,
            _resolve_pipelines_sample_workspace_macro_value(),
        )
        workspace_name = workspace_name.replace(
            Macros.DPV2_SAMPLE_WORKSPACE_NAME_MACRO,
            _resolve_dpv2_sample_workspace_macro_value(),
        ).replace(
            Macros.PIPELINES_SAMPLE_WORKSPACE_NAME_MACRO,
            _resolve_pipelines_sample_workspace_macro_value(),
        )
        workspaces[name] = WorkspaceConfig(
            subscription_id, resource_group_name, workspace_name, region
        )
    return workspaces


WORKSPACES = _load_local_config()
