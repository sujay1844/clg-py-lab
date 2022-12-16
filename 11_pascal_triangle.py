# Program to generate a pascal's triangle.

limit = int(input("Enter number of rows of pascal's triangle to be printed: "))

# First row is 1
triangle = [[1]]

# Since the first row is 1, we exclude it from the computation
limit-=1

for _ in range(limit):

    # First element is 1
    row = [1]

    for i, element in enumerate(triangle[-1]):

        # Skip the first element since it's 1
        if i == 0: continue

        # Add element above and previous element to that
        row.append(element + triangle[-1][i-1])

    # Last element is 1
    row.append(1)

    triangle.append(row)

for row in triangle:
    print(*row)
