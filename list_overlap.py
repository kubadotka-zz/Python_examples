import random
a = []
b = []
n = int(input("enter number of elements is first list: "))
m = int(input("enter number of elements in second list: "))
for j in range(n):
    a.append(random.randint(1, 101))
for j in range(m):
    b.append(random.randint(1,101))
print("Elements of 1st list: " + str(a))
print("Elements of 2nd list: " + str(b))
intersection = set(a).intersection(b)
print("List of intersection of these two lists: ", list(intersection))