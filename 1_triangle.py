# Given 3 sides, check whether a triangle is formed. If yes, find the area.

import math

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if (
        # Sum of 2 sides is greater than 3rd side
        a+b > c and
        b+c > a and
        c+a > b and

        # Difference of 2 sides is lesser than 3rd side
        a-b < c and
        b-c < a and
        c-a < b
    ):
    print("Given sides form a triangle")

    # Heron's formula
    s = (a+b+c)/2 # semi-perimeter
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    print("Area of triangle is:", area)

else:
    print("Given sides do not form a triangle")
