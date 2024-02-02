def toBin(a):
    binary1 = []
    while a>0:
        binary1.append(a%2)
        a=a//2
    binary1.reverse()
    string_ver = ''.join(str(elem) for elem in binary1)
    return string_ver

print(toBin(54))