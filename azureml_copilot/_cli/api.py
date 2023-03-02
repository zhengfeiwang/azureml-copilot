import sys

from .workspace import list_workspace, get_workspace


def list_workspace_api():
    list_workspace()


def get_workspace_api():
    args = sys.argv[1:]
    workspace_name = args[0]
    if len(args) == 2:
        string_format = args[1]
    else:
        string_format = "json"
    workspace_config = get_workspace(workspace_name)
    print(getattr(workspace_config, string_format))
