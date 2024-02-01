# Aby zrobic NWW nalezy najpierw zrobic NWD

def nwd(a, b):
    while a!=b:
        if a>b:
            a-=b
        elif b>a:
            b-=a
    return a

def nww(a,b):
    return a*b//nwd(a,b)

print(nww(10,4))