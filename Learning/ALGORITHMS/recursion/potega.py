def potega(a,n):
    if n==0: return 1
    else: return potega(a,n-1)*a

print(f'6 do potegi 3 to: {potega(6,3)}')