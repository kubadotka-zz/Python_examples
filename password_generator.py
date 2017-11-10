import string
import random
def Password_generator(letter1 = string.ascii_lowercase + string.digits + string.ascii_uppercase):
    size = int(input("How long the password should be?"))
    return(''.join(random.choice(letter1) for _ in range(size)))
print(Password_generator())

