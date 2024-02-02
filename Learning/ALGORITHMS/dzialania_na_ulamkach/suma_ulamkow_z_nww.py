def nwd(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a


def nww(a,b):
    return a*b//nwd(a,b)

# l1/m1 + licz2/mian2 = (l1*((nww(m1,mian2))/m1) + licz2*(nww(m1,mian2)/mian2))/nww(m1,mian2)

def suma(l1,m1,licz2,mian2):
    NWW = nww(m1,mian2)
    licznik3 = l1*NWW//m1 + licz2*NWW//mian2  # '//' uzywamy aby byl int a nie float. Mozna uzyc tez '/' lecz wtedy nalezy uzyc int()
    mianownik3 = NWW
    return f'{l1}/{m1} + {licz2}/{mian2} = {licznik3}/{mianownik3}'


 