import random

def random_matrix(rows, cols):
    matrix = []
    for a in range(rows):
        row = [random.randint(1, 100) for a in range(cols)]
        matrix.append(row)
    return matrix

def get_column_sum(matrix, column_index):
    if not matrix:
        return 0
    if column_index < 0 or column_index >= len(matrix[0]):
        return 0
    column_sum = sum(row[column_index] for row in matrix)
    return column_sum

def get_row_average(matrix, row_index):
    if not matrix:
        return 0
    if row_index < 0 or row_index >= len(matrix):
        return 0
    row = matrix[row_index]
    row_average = sum(row) / len(row)
    return row_average

#test
matrix = random_matrix(4, 4)
print("matrix")
for row in matrix:
    print(row)

column_sum = get_column_sum(matrix, 1)
print("Sum of column 1: ", column_sum)

row_average = get_row_average(matrix, 1)
print("Average of row 1: ", row_average)
