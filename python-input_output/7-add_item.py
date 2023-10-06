#!/usr/bin/python3
"""
Module to add all arguments to a py list and save them to a file.
"""


from sys import argv
save_to_f = __import__('5-save_to_json_file').save_to_json_file
load_from_f = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    """Main function to add arguments to a list and save to a file."""
    f_name = "add_item.json"

    try:
        items = load_from_f(f_name)
    except Exception:
        items = []

    items += argv[1:]
    save_to_f(items, f_name)
