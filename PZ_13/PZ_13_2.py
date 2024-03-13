"""
В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза.
"""
matrix = [[i + j * 3 + 1 for i in range(3)] for j in range(3)]

number_column = int(input("Введите номер столбца (от 0 до 2): "))

for row in matrix:
    row[number_column] *= 2

for row in matrix:
    print(row)
