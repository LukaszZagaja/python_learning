from math import sqrt

# ax^2 + bx + c = 0
# delta = b**2 - 4 * a * c
def delta(a,b,c):
    return b**2 - 4 * a * c

def x0(a,b):
    return f"x0 = {-b/a*2}"

def x1(a,b,delta):
    return f"x1 = {round((-b-sqrt(delta))/(a*2), 2)}"

def x2(a,b,delta):
    return f"x2 = {round((-b+sqrt(delta))/(a*2), 2)}"

def miejscaZerowe(delta,a,b,):
    if delta<0:
        return "Brak miejsc zerowych. Delta mniejsza od 0"
    elif delta==0:
        return x0(a,b)
    else:
        return [x1(a,b,delta), x2(a,b,delta)]

a = round(float(input("Podaj wartosc a: ")),2)
b = round(float(input("Podaj wartosc b: ")),2)
c = round(float(input("Podaj wartosc c: ")),2)

print(miejscaZerowe(delta(a,b,c),a,b))
print(f"Delta: {delta(a,b,c)}")