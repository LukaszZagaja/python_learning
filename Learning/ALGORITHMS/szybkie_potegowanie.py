def potegowanieSzybkie(podstawa,wykladnik):
    if wykladnik == 0:
        return 1
    wynik = 1
    while wykladnik > 0:
        if wykladnik%2==1: # 10100110 <- bits. if we meet 1 then both if 0 then only podstawa
            wynik*=podstawa
        print(f'Podstawa przed: {podstawa}')
        podstawa*=podstawa
        print(f'Podstawa po mnozeniu: {podstawa}')
        print(f'Wykladnik przed: {wykladnik}')
        wykladnik = wykladnik//2
        print(f'Wykladnik po dzieleniu: {wykladnik}\n')
    return wynik


potegowanieSzybkie(2,5)