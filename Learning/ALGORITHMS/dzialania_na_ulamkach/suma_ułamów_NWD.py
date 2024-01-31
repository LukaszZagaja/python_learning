def euclides(a,b):
    while a != b:
        if a > b:
            a = a-b
        elif b > a:
            b = b-a
    return a

def suma(licznik1, mianownik1, licz2, mian2):
    licznik_sumy = licznik1 * mian2 + mianownik1 * licz2
    mianownik_sumy = mianownik1 * mian2
    nwd = euclides(licznik_sumy, mianownik_sumy)
    return(f'{licznik_sumy//nwd}/{mianownik_sumy//nwd}') # // znaczy dzielenie bez reszty -> podobne do %

print('\nSUMA ULAMKOW\n')

l1 = int(input('Licznik pierwszego ulamka: '))
m1 = int(input('Mianownik pierwszego ulamka: '))
l2 = int(input('Licznik drugiego ulamka: '))
m2 = int(input('Mianownik drugiego ulamka: '))

print(f'{l1}/{m1} + {l2}/{m2} = {suma(l1,m1, l2,m2)}')
