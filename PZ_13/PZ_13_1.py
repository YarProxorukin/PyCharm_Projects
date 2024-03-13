"""
В матрице элементы последней строки заменить на 0.
"""
matrix = [[i + j * 3 + 1 for i in range(3)] for j in range(3)]

last_index = len(matrix) - 1
num_columns = len(matrix[0])

for i in range(num_columns):
    matrix[last_index][i] = 0

for row in matrix:
    print(row)
