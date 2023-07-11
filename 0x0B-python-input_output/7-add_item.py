import sys

from json_functions import save_to_json_file, load_from_json_file


def add_arguments_to_list(args_list):
    """Represents adding arguments"""
    try:
        existing_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        existing_list = []

    existing_list.extend(args_list)
    save_to_json_file(existing_list, "add_item.json")

if __name__ == "__main__":
    arguments = sys.argv[1:]
    add_arguments_to_list(arguments)
