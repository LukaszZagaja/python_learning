def toBinary(number):
    potega = len(number)-1 # jak liczba ma 6 cyfr to potega bedzie 5 poniewaz jest 5,4,3,2,1,0 -> wykladnik jest o 1 mniejszy od ilosci znakow w liczbie w bin
    suma = 0
    for i in number:
        if i == '1':
            suma += 2**potega
        potega-=1
    return suma

print(toBinary(input('Give a binary number you want to have in decimal: ')))