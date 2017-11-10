number = int(input("write a number to check if it's even, odd or multiple of 4: "))
if number % 2 == 0:
    if number % 4 == 0:
        print("number is even and a multiple of 4")
        
    else: 
        print("number is even")
else:
    print("number is odd")