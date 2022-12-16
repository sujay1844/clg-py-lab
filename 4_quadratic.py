# Find roots of a quadratic equation ax^2 + bx + c = 0, what if b^2 - 4ac = 0, b^2 - 4ac > 0, b^2 - 4ac < 0.

import math, cmath

a, b, c = [int(x) for x in input("Enter a, b, c: ").split()]

det = b**2 - 4*a*c

x1, x2 = 0, 0 # In case solutions are unbound

if det >= 0:
    # Real roots
    x1 = (-b + math.sqrt(det)) / (2*a)
    x2 = (-b - math.sqrt(det)) / (2*a)

elif det < 0:
    # Imaginary roots
    x1 = (-b - cmath.sqrt(det)) / (2 * a)
    x2 = (-b + cmath.sqrt(det)) / (2 * a)

print("Roots are:", x1, x2)
