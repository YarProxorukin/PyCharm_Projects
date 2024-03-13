"""
В матрице элементы столбца N (N задать с клавиатуры) увеличить в два раза.
"""
matrix = [[i + j * 3 + 1 for i in range(3)] for j in range(3)]
for row in matrix:
    print(row)

number_column = int(input("Введите номер столбца (от 0 до 2): "))

matrix = [[row[i] * 2 if i == number_column else row[i] for i in range(len(row))] for row in matrix]

for row in matrix:
    print(row)
