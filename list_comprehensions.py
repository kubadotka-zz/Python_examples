import random
n = int(input("Enter number of elements in random list: "))
a = []
for j in range(n):
    a.append(random.randint(1, 101))
b = []
b = [number for number in a if number % 2 == 0]
print("list a: ", a)
print("list b: ", b)
