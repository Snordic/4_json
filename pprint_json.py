import json
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return pretty_print_json(data)


def pretty_print_json(data):
    return json.dumps(data, ensure_ascii=False, sort_keys=True, indent=7)


if __name__ == '__main__':
    filename = 'alco_shops.json'
    print(load_data(filename))
else:
    print(load_data(sys.argv[1]))