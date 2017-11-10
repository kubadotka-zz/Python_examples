
from datetime import datetime
print("ta funkcja obliczy w ktorym roku bedziesz mial 100 lat")
name = input("What's your name?")
years = int(input("How old are you?"))
current_year = datetime.now().year
birth_date = current_year - years
year_of_turning_100 = birth_date + 100
print(name + ", bedziesz mial 100 lat w roku: " + str(year_of_turning_100) + ".")