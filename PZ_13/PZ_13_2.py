"""
В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза.
"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

column_index = int(input("Введите номер столбца (от 0 до 2): "))

for row in matrix:
    row[column_index] *= 2

for row in matrix:
    print(row)
