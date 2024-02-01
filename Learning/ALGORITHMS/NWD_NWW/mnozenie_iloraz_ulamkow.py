def nwd(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a

# l1/m1 * licz2/mian2 = (l1/nwd(l1,mian2)) * (licz2/nwd(licz2,m1)) // (m1/nwd(m1,licz2)) * (mian2/nwd(mian2,l1)) = licznik3/mianownik3
# licznik3 = (l1/nwd(l1,mian2)) * (licz2/nwd(licz2,m1))
# mianownik3 = (m1/nwd(m1,licz2)) * (mian2/nwd(mian2,l1))

def mnozenie_ulamkow(l1,m1,licz2,mian2):
    licznik3 = l1//nwd(l1,mian2) * licz2//nwd(licz2,m1)
    mianownik3 = m1//nwd(m1,licz2) * mian2//nwd(mian2,l1)
    nwd_l3_m3 = nwd(licznik3,mianownik3)
    return f'{l1}/{m1} * {licz2}/{mian2} = {licznik3//nwd_l3_m3}/{mianownik3//nwd_l3_m3}'

print(mnozenie_ulamkow(4,7,7,8))