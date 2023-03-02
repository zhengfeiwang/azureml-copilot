import argparse
import sys


def _workspace_parser(argv=None):
    from azureml_copilot._cli import workspace

    # comes from command acw
    if argv is None:
        argv = sys.argv[1:]

    workspace_parser = argparse.ArgumentParser()
    workspace_parser.add_argument(
        "verb", nargs="*", help="`list` or `get <workspace-name>`"
    )
    workspace_parser.add_argument(
        "--json", action="store_true", help="print with json format"
    )
    workspace_parser.add_argument(
        "--url", action="store_true", help="print with workspace url"
    )
    workspace_parser.add_argument(
        "--environ", action="store_true", help="print with environ format"
    )

    args = workspace_parser.parse_args(argv)
    kwargs = vars(args)
    verb = kwargs.pop("verb")

    if verb[0] == "list":
        workspace.list_workspace(**kwargs)
    elif verb[0] == "get":
        workspace.get_workspace(verb[1], **kwargs)


def _entry(argv):
    noun = argv[0]
    if noun == "workspace":
        _workspace_parser(argv[1:])


def main():
    command_args = sys.argv[1:]
    if len(command_args) == 0:
        command_args.append("help")
    _entry(command_args)
