import json
import sys


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_with_json:
        data_from_file = json.load(file_with_json)
    return data_from_file


def pretty_print_json(data_from_json):
    print(json.dumps(data_from_json, ensure_ascii=False,
                     sort_keys=True, indent=7))


if __name__ == '__main__':
    try:
        pretty_print_json(load_data(sys.argv[1]))
    except IndexError:
        print('Ошибка: Вы не добавили файл!')
    except json.decoder.JSONDecodeError:
        print('Ошибка: Расширение файла не JSON!')
