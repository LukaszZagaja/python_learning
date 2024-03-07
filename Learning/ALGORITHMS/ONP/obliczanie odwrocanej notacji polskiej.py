lista = "2 4 + 4 6 - *"
#  	2 4 + 4 6 - * is equal to: (2 + 4)*(4 - 6)
lista = lista.split()
stack = []

for i in lista:
    if i.isdigit():
        num = int(i)
        stack.append(num)
    else:
        b = stack.pop()
        a = stack.pop()
        # it must be like that because its stack from bottom to the top 
        if i == '*':
            stack.append(a*b)
        elif i == '-':
            stack.append(a-b)
        elif i == '+':
            stack.append(a+b)
        else:
            stack.append(a//b)