string = list(input("Enter a string to check if it's palindrome or not: "))
string2 = list(reversed(string))
print(string2)
if str(string) == str(string2):
    print("entered string is a palindrome!!")
else:
    print("entered string isn't palindrome")
