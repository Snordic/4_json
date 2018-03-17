import json
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_with_json:
        data_json = json.load(file_with_json)
    return pretty_print_json(data_json)


def pretty_print_json(json_handling):
    return json.dumps(json_handling, ensure_ascii=False, sort_keys=True, indent=7)


if __name__ == '__main__':
    print(load_data(sys.argv[1]))
else:
    file_name_json = 'alco_shops.json'
    print(load_data(file_name_json))