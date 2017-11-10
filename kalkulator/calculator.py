from addition import addition  
from subtraction import subtraction
from multiplication import multiplication
from division import division
def calculator ():

    print("Welcome to Kuba's Calculator!")
    while True:
        print("Options to do: ")
        print("Enter 'add' to use addiction(+)")
        print("Enter 'subtract' to use subtraction(-)")
        print("Enter 'multiply' to use multiplication(X)")
        print("Enter ' divide' to use division(/)")
        print("Enter 'close' to end the program :(")
        result = input("Your choice?!: ")
        if result == "add":
            num1 = input("Enter first substrate of operation: ")
            num2 = input("Enter second substrate of operation: ")
            n1t = num1.isdigit()
            n2t = num2.isdigit()
            if n1t and n2t == True:
                    product = addition(num1, num2)
                    print("it's ", product, ", and again!")
                
            else:
                print("Enter again!")
                continue
        elif result == "subtract":
            num1 = input("Enter first substrate of operation: ")
            num2 = input("Enter second substrate of operation: ")
            n2t = num2.isdigit()
            if n1t and n2t == True:
                    product = subtraction(num1, num2)
                    print("It's ", product, ", and again!")
            else:
                print("Enter again!")
                continue
        elif result == "multiplication":
            num1 = input("Enter first substrate of operation: ")
            num2 = input("Enter second substrate of operation: ")
            n2t = num2.isdigit()
            if n1t and n2t == True:
                    product = multiplication(num1, num2)
                    print("It's ", product, ", and again!")
            else:
                print("Enter again!")
                continue
        elif result == "division":
            num1 = input("Enter first substrate of operation: ")
            num2 = input("Enter second substrate of operation: ")
            n2t = num2.isdigit()
            if n1t and n2t == True:
                    product = division(product)
                    print("It's ", product, ", and again!")
            else:
                print("Enter again!")
                continue
        elif result == "close":
            break
        else:
            print("Enter again!")
            continue
            
            
calculator()
   





        

        



    