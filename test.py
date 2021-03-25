import json
import os

from cbapi.example_helpers import build_cli_parser


def import_watchlist(parser, args):
    with open("export.json", "r") as file:
        imported = json.load(file)


def file_dump(exported):
    data_path = "export"
    data_file = "export.json"
    data_location = data_path + "/" + data_file
    with open(data_location, "w") as file:
        file.write(json.dumps(exported, indent=4))


def main():

    parser = build_cli_parser()
    commands = parser.add_subparsers(help="Feed commands", dest="command_name")

    import_command = commands.add_parser("import", help="Import a previously exported watchlist")
    specifier = import_command.add_mutually_exclusive_group(required=False)
    specifier.add_argument("-f", "--file_name", type=str, help="JSON File")

    args = parser.parse_args()

    if args.command_name == "import":
        return import_watchlist(parser, args)


if __name__ == '__main__':
    main()
