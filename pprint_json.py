import json
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_with_json:
        data_from_file = json.load(file_with_json)
    return data_from_file


def pretty_print_json(data_output):
    return print(json.dumps(data_output, ensure_ascii=False, sort_keys=True, indent=7))


if __name__ == '__main__':
    pretty_print_json(load_data(sys.argv[1]))
