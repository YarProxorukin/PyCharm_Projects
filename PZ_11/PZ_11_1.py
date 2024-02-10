"""
Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
последовательности из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:
Элементы первого и второго файлов:
Среднее арифметическое элементов первого и второго файлов:
Количество нечетных элементов первого и второго файлов:
Элементы общие для двух файлов:
Количество элементов, общих для двух файлов:
"""
import random

numbers1 = [random.randint(-10, 20) for _ in range(10)]
numbers2 = [random.randint(-10, 20) for _ in range(10)]
# файл 1
for i in numbers1:
    open('file_1.txt', 'a').write(str(i) + '\n')
# файл 2
for i in numbers2:
    open('file_2.txt', 'a').write(str(i) + '\n')
# файл 3
numbers = numbers1 + numbers2

with open('file_3.txt', 'w', encoding='utf-8') as f:
    f.write(f'Элементы: {" ".join(map(str, numbers))} \n')
    f.write(f'Среднее арифметическое: {(sum(numbers)) / (len(numbers))} \n')
    count_chet = 0
    for i in numbers:
        if i % 2 == 0:
            count_chet += 1
    count_nechet = len(numbers) - count_chet
    f.write(f'Количество нечетных элементов: {count_nechet} \n')
    common_numbers = set(numbers1) & set(numbers2)
    f.write(f'Общие элементы файлов: {common_numbers} \n')
    f.write(f'Количество общих элементов: {len(common_numbers)}')
