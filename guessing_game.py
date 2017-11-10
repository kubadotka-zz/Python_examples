import random
import sys
number = random.randint(1, 10)
guess = None
tries = 1
#print(number)
while True:
    guess = int(input("Enter your lucky number form 1 to 9(or enter '0' to end game): "))
    if guess > number:
        print("wrong! too high!")
    elif int(guess) < number:
        if guess == 0:
            print("Better luck next time!")
            sys.exit()
        else:
            print("wrong! too low!")
        
    
    elif guess == number:
        print("u did it at %s time!!" %tries)
        
    else:
        print("wrong input!, %s tries!" %tries)
        
    tries += 1 

        