import datetime
import os
from pathlib import Path

LOCAL_CONFIG_PATH = Path(os.path.expanduser("~")) / ".azureml" / "azureml_copilot"


class Macros:
    DPV2_SAMPLE_WORKSPACE_NAME_MACRO = "${{dpv2_sample_workspace_name_macro}}"
    PIPELINES_SAMPLE_WORKSPACE_NAME_MACRO = "${{pipelines_sample_workspace_name_macro}}"

    @staticmethod
    def resolve_dpv2_sample_workspace_macro() -> str:
        # Reference from azureml-examples:
        # https://github.com/Azure/azureml-examples/blob/main/infra/init_environment.sh#L46-L53
        return (datetime.datetime.today() + datetime.timedelta(days=2)).strftime(
            "%Y%m"
        )[2:]

    @staticmethod
    def resolve_pipelines_sample_workspace_macro() -> str:
        # Reference from DesignerPrivatePreviewFeatures:
        # https://github.com/Azure/DesignerPrivatePreviewFeatures/blob/master/azure-ai-ml/scripts/utils.py#L45-L53
        today = datetime.datetime.today()
        weekday = today.weekday()  # weekday: 0-Monday, 6-Sunday
        monday_date = today - datetime.timedelta(days=weekday)
        return monday_date.strftime("%Y%m%d")
