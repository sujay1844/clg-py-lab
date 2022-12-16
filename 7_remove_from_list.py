# Program to remove all occurrences of a number entered by the user in the given list.

# arr = input("Enter list: ").split()
arr = [int(x) for x in input("Enter list of numbers: ").split()]

# unwanted = input("Enter element to be removed")
unwanted = int(input("Enter element to be removed"))

for _ in range(arr.count(unwanted)):
    arr.remove(unwanted)

print(arr)
