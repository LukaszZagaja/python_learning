# Zalozenia: 1. Funkcja jest ciagla.   2. W przedziale [a,b] ma tylko i dokladnie 1 miejsce zerowe
# zawsze f(a) * f(b) < 0   <-> poniewaz wartosci na krancach przedzialow maja zawsze inne znaki (chyba ze wartosc na krancu to miejsce zerowe - to wtedy nie)
# Epsilon to min odleglosc funkcji od osi OX

def f(x:float)->float:
    return  x * (x * (x - 3) + 2) - 6

def polowienie_przedzialu(a:float,b:float,epsilon: 0.00001):
    if f(a) == 0.0: return a
    elif f(b) == 0.0: return b


    while b-a > epsilon:
        srodek = (a + b) / 2

        print(f"a: {a}\nb: {b}\n srodek: {srodek}\nf(a):{f(a)}\nf(b): {f(b)}\nf(srodek): {f(srodek)}\nf(a)*f(srodek): {f(a)*f(srodek)}\n\n")
        if f(srodek) == 0.0:
            return srodek
        
        if f(a) * f(srodek) < 0:
            b = srodek
        else:
            a = srodek
    
    return round((a + b) / 2, 5)

a = -10; b = 10; epsilon = 0.00001
print("Znalezione miejsce zerowe wynosi:", polowienie_przedzialu(a, b, epsilon))