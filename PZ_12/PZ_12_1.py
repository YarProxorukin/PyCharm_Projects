"""
Организовать и вывести последовательность из 20 целых чисел, выбрать не повторяющиеся элементы, найти их количество.
Элементы больше 5 увеличить в два раза.
"""

spisok = [-4, -3, -2, -2, -1, 0, 1, 3, 3, 4, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10]

unique_elements = list(set(spisok))
print(f'Уникальные элементы: {unique_elements}')
print(f'Количество уникальных элементов: {len(unique_elements)}')


five = lambda num: num * 2 if num > 5 else num


new_spisok = list(map(five, unique_elements))
print(f'Модифицированная последовательность: {new_spisok}')
