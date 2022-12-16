# Program to find the addition of two matrices.
# Not using numpy

def add_matrices(matrix1:list, matrix2:list) -> list:

    # Addition is only possible when two matrices are of same size
    if len(matrix1) != len(matrix2): return []
    if len(matrix1[0]) != len(matrix2[0]): return []

    result = []
    for row1, row2 in zip(matrix1, matrix2):
        result_row = [x+y for x, y in zip(row1, row2)]
        result.append(result_row)

    return result
