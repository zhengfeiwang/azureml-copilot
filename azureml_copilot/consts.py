import collections
import datetime
import os
import typing
from pathlib import Path

WorkspaceConfig = collections.namedtuple(
    "WorkspaceConfig", ["subscription_id", "resource_group_name", "workspace_name"]
)

LOCAL_CONFIG_PATH = Path(os.path.expanduser("~")) / ".azureml" / "azureml_copilot"


class Macros:
    SAMPLE_WORKSPACE_DATE_STRING = "${{monday_date}}"


def get_sample_workspace_date_string() -> str:
    # Reference from sample repository:
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
        name, subscription_id, resource_group_name, workspace_name = line.split()
        workspace_name = workspace_name.replace(
            Macros.SAMPLE_WORKSPACE_DATE_STRING, get_sample_workspace_date_string()
        )
        workspaces[name] = WorkspaceConfig(
            subscription_id, resource_group_name, workspace_name
        )
    return workspaces


WORKSPACES = _load_local_config()
