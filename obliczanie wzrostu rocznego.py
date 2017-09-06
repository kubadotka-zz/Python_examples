amount = float(input("Podaj wartosc: "))
inrate = float(input("Podaj wzrost w procentach: "))
period = int(input("podaj okres czasu: "))
value = 0
year = 1
while year <= period:
    value = amount + (inrate * 0.01 * amount)
    print("Year %d Rs. %.2f" % (year, value))
    amount = value
    year = year + 1
    
