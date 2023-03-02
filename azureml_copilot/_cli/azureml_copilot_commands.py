import sys

from azureml_copilot._cli.commands import get_workspace, list_workspaces


def main():
    command_args = sys.argv[1:]
    if len(command_args) == 0:
        command_args.append("-h")
    if command_args[0] == "list":
        list_workspaces()
    if command_args[0] == "get":
        get_workspace(command_args[1])
