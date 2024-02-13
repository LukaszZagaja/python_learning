def dodawanie(a,b):
    if b<1:
        return "Druga liczba powinna byc rozna od 0"
    else:
        return a+b

def odejmowanie(a,b):
    if b<1:
        return "Druga liczba powinna byc rozna od 0"
    else:
        return a-b

def mnozenie(a,b):
    if b<1:
        return "Druga liczba powinna byc rozna od 0"
    else:
        return a*b

def dzielenie(a,b):
    if b<1:
        return "Druga liczba powinna byc rozna od 0"
    else:
        return a/b
    

liczba1 = int(input("Podaj pierwsza liczbe: "))
liczba2 = int(input("Podaj druga liczbe: "))

print(f"Dodawanie: {dodawanie(liczba1,liczba2)}")
print(f"Odejmowanie: {odejmowanie(liczba1,liczba2)}")
print(f"Mnozenie: {mnozenie(liczba1,liczba2)}")
print(f"Dzielenie: {dzielenie(liczba1,liczba2)}")
