# Program to print identity matrix using list.
# Not using numpy

size = int(input("Enter size of identity matrix: "))

matrix = []

for i in range(size):
    row = [0] * size
    row[i] = 1
    matrix.append(row)

for row in matrix:
    print(*row)
