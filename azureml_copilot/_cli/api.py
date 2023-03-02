import sys

from .workspace import list_workspace, get_workspace


def list_workspace_api():
    list_workspace()


def get_workspace_api():
    args = sys.argv[1:]
    workspace_name = args[0]
    workspace_config = get_workspace(workspace_name)
    if len(args) == 2:
        string_format = args[1]
        print(getattr(workspace_config, string_format))
    else:
        print(workspace_config.url)
        print(workspace_config.json)
        print(workspace_config.environ)
