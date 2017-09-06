import math
a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))
d = b * b - 4 * a * c
if d < 0:
    print("This equation has no real solution")
elif d == 0:
    x = -1 * b / (2 * a)
    print("This equation has one solution: x = " + x )
else:
        xy = (-b - math.sqrt(d)) / (2 * a)
        xz = (-b + math.sqrt(d)) / (2 * a)
        print("This equation has two solutions: x = " + str(xy) + ", " + str(xz))

