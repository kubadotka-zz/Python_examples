def unit_change():

    print("That program changes units to seconds ( readable by shell )")
    unit = str(input("Write unit of time: (month, day, hour, minute)"))



    if unit=="month":
        amount = int(input("Write amount of months: "))
        print("It's " + str(amount * 2628000) + " seconds")
    elif unit=="week":
        amount = int(input("Write amount of weeks: "))
        print("It's " + str(amount * 604800) + " seconds")
    elif unit=="day":
        amount = int(input("Write amount of days: "))
        print("It's " + str(amount * 86400) + " seconds")
    elif unit=="hour":
        amount = int(input("Write amount of hours: "))
        print("It's " + str(amount * 3600) + " seconds")
    elif unit=="minute":
        amount = int(input("Write amount of minutes: "))
        print("It's " + str(amount * 60) + " seconds")

    else:
        print("Write unit of time: (month, day, hour, minute")
    


    

unit_change()
