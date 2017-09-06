fahrenheit = 0.0
print("fahrenheit Celsius")
while fahrenheit <= 250:
    celsius = ( fahrenheit - 32.0 ) / 1.8 #kalkulowanie wartosci C
    print("%5.1f %7.2f" % (fahrenheit , celsius))
    fahrenheit = fahrenheit + 25
