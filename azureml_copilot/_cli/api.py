import sys

from .workspace import list_workspace, get_workspace_environ, get_workspace_json


def list_workspace_api():
    list_workspace()


def get_workspace_api():
    args = sys.argv[1:]
    workspace_name = args[0]
    if len(args) == 2:
        string_format = args[1]
    else:
        string_format = "json"
    if string_format == "json":
        get_workspace_json(workspace_name)
    else:
        get_workspace_environ(workspace_name)
