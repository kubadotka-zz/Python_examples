warunek = string(input("wybierz jaka jednostke czasu chcesz przeliczyc. Wybierz jedno: rok, miesiac, tydzien, dzien, godzina, minuta, sekunda"))

if warunek = rok:
    years = int(input("wpisz ilosc lat do przeliczenia"))
    months = years * 12
    days = years * 365
    hours = years * 8760
    minutes = years * 525600
    seconds = years * 31536000
    print("jeden rok to: " + months " miesiecy, " + days + " dni, " + hours + " godzin, " + seconds + " sekund.") 

else
if warunek = miesiac:
    months = int(input("wpisz ilosc miesiecy do przeliczenia"))
    years = months / 12
        months_ = months % 12
    days = months * 30
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    print("jeden miesiac to: " + years + " i " + months_ + "miesiecy. Zamiennie: " + days + " dni, " + hours + " godzin, " + minutes + " minut, " + sekund + ".")

else
if warunek = dzien:
    days = int(input("wpisz ilosc dni do przeliczenia"))
    years = days / (12 * 30)
    months_ = days % 12
        days_ = months_ % 30
    months = days / 30
        days__ = days % 30
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    print("jeden dzien to: " + years + " lat, " + months_ + " miesiecy i " + days_ + " dni. Zamiennie: " + months + " miesiecy i " + days__ + "dni. Zamiennie: " + hours + "godzin, " + minutes + "minut, " + seconds + "sekund.")

    
