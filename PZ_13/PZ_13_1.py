"""
В матрице элементы последней строки заменить на 0.
"""
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

last_index = len(matrix) - 1
num_columns = len(matrix[0])

for i in range(num_columns):
    matrix[last_index][i] = 0

for row in matrix:
    print(row)
