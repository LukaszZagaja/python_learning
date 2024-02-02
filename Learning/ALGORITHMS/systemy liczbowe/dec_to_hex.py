def toHex(number):
    while number>0:
        remainder = number%16
        if remainder==10:
            whole_hex.append('A')
        elif remainder==11:
            whole_hex.append('B')
        elif remainder==12:
            whole_hex.append('C')
        elif remainder==13:
            whole_hex.append('D')
        elif remainder==14:
            whole_hex.append('E')
        elif remainder==15:
            whole_hex.append('F')
        else:
            whole_hex.append(remainder)
        number = number//16
    
    whole_hex.reverse()
    whole_number = ''.join(str(num) for num in whole_hex)
    return whole_number

whole_hex = [] # i dont really know but if this line is in function then whole if/else thing doesnt work 
print(toHex(int(input('Give a dedcimal number you want to have in Hexadecimal: '))))
