"""
В исходном текстовом файле(dates.txt) найти все даты в форматах ДД.ММ.ГГГГ и ДД/ММ/ГГГГ.
Посчитать количество дат в каждом формате.
Поместить в новый текстовый файл все даты февраля в формате ДД/ММ/ГГГГ.
"""
import re

with open('dates.txt', 'r', encoding='utf8') as file:
    data = file.read()

regular_dot = r'\d{2}\.\d{2}\.\d{4}'
regular_slash = r'\d{2}/\d{2}/\d{4}'
regular_februaries_slash = r'\d{2}\/02/\d{4}'

dates_dot = re.findall(regular_dot, data)
dates_slash = re.findall(regular_slash, data)
dates_februaries = re.findall(regular_februaries_slash, data)
print(dates_dot)
print(f'Количество дат формата ".": {len(dates_dot)}')
print(dates_slash)
print(f'Количество дат формата "/": {len(dates_slash)}')

with open('result.txt', 'w', encoding='utf8') as file:
    file.write('\n'.join(dates_februaries))
