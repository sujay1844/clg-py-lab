# Given 4 sides and two diagonals of a quadrilateral classify the quadrilateral as square, rhombus, rectangle and parallelogram.

a, b, c, d = [int(x) for x in input("Enter 4 sides: ").split()]
d1, d2 = [int(x) for x in input("Enter 2 diagonals: ").split()]

# Check for square
if a == b == c == d and d1 == d2:
    print("Given quadrilateral is a square.")

# Check for rhombus
elif a == b == c == d:
    print("Given quadrilateral is a rhombus.")

# Check for rectangle
elif (
        (
            (a == b and c == d) or
            (a == c and b == d)
        ) and d1 == d2
    ):
    print("Given quadrilateral is a rectangle.")

# Check for parallelogram
elif (a == b and c == d) or (a == c and b == d):
    print("Given quadrilateral is a parallelogram.")
