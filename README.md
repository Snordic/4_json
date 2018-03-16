#  Работа с JSON

Форматирование JSON файла для удобства читаемости.

# Как использовать

Необходимо добавить функцию:

```python
from pprint_json import pretty_print_json, load_data
```
 
Добавить json файл:

```python
load_data('alco_shops.json')
```

При помощи функций `print()` выводим информацию с JSON:

```python
print(load_data('alco_shops.json'))


...
 {
                     "geometry": {
                            "coordinates": [
                                   37.61869265083847,
                                   55.66062001719139
                            ],
                            "type": "Point"
                     },
                     "properties": {
                            "Attributes": {
                                   "Address": "Варшавское шоссе, дом 64, корпус 1",
                                   "AdmArea": "Южный административный округ",
                                   "ClarificationOfWorkingHours": null,
                                   "District": "Нагорный район",
                                   "IsNetObject": "нет",
                                   "Name": "Магазин «Пиво есть»",
                                   "OperatingCompany": null,
                                   "PublicPhone": [
                                          {
                                                 "PublicPhone": "(499) 351-22-17"
                                          }
                                   ],
                                   "TypeService": "реализация продовольственных товаров",
                                   "WorkingHours": [
                                          {
                                                 "DayOfWeek": "понедельник",
                                                 "Hours": "11:00-23:00"
                                          },
                                          {
                                                 "DayOfWeek": "вторник",
                                                 "Hours": "11:00-23:00"
                                          },
                                          {
                                                 "DayOfWeek": "среда",
                                                 "Hours": "11:00-23:00"
                                          },
                                          {
                                                 "DayOfWeek": "четверг",
                                                 "Hours": "11:00-23:00"
                                          },
                                          {
                                                 "DayOfWeek": "пятница",
                                                 "Hours": "11:00-23:00"
                                          },
                                          {
                                                 "DayOfWeek": "суббота",
                                                 "Hours": "10:00-23:00"
                                          },
                                          {
                                                 "DayOfWeek": "воскресенье",
                                                 "Hours": "10:00-23:00"
                                          }
                                   ],
                                   "global_id": 25214474
                            },
                            "DatasetId": 1854,
                            "ReleaseNumber": 2,
                            "RowId": "a8526203-a2a9-4ee1-a856-96eaec0c18b7",
                            "VersionNumber": 1
                     },
                     "type": "Feature"
              },
...
```

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
$ python pprint_json.py <path to file>
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке ― [DEVMAN.org](https://devman.org)