# Program to sort a given list of elements (both ascending and descending).

lst = input("Enter a list: ").split()
# lst = [int(x) for x in input().split()]

print("Ascending order,")
print(sorted(lst))

print("Descending order,")
print(sorted(lst)[::-1])
