# Given 3 points (x1, y1), (x2, y2) and (x3, y3), find whether they are collinear, if not, find centroid, orthocenter, incenter, circumcenter.

x1, y1 = [int(n) for n in input("Enter co-ordinates of 1st point: ").split()]
x2, y2 = [int(n) for n in input("Enter co-ordinates of 2nd point: ").split()]
x3, y3 = [int(n) for n in input("Enter co-ordinates of 3rd point: ").split()]

# Check for collinearity (3rd condition here is redundant)
if (y2-y1)/(x2-x1) == (y3-y2)/(x3-x2) == (y1-y3)/(x1-x3):

    print("Given points are collinear.")

else:

    print("Given points are not collinear")

    centroid = [
        (x1+x2+x3)/3,
        (y1+y2+y3)/3
    ]

    print("Centroid is ", centroid)

    # I will get back to these later
    circumcenter = [0, 0]
    incenter = [0, 0]
    orthocenter = [0, 0]
