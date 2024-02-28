def sprawdz(wzorzec, tekst):
    dlugosc_wzorca=len(wzorzec)
    dlugosc_tekstu=len(tekst)

    for i in range(dlugosc_tekstu-dlugosc_wzorca+1):
        for j in range(dlugosc_wzorca):
            if tekst[i+j] != wzorzec[j]:
                break
            elif j == dlugosc_wzorca-1:
                return True
    return False


txt = 'Ala ma kota'
wz = 'kot'

print(f'Czy "{wz}" znajduje sie w: "{txt}": {sprawdz(wz,txt)}')