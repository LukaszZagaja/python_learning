def potegowanieSzybkie(podstawa,wykladnik):
    if wykladnik == 0:
        return 1
    wynik = 1
    while wykladnik > 0:
        if wykladnik%2==1: # if there is 1 then both if 0 then only podstawa
            wynik*=podstawa
        podstawa*=podstawa
        wykladnik = wykladnik//2
    return wynik