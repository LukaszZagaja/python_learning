numbers = []
even = 0
uneven = 0

for x in range(10):
    a = int(input('Give numbers: '))
    numbers.append(a)

for x in range(10):
    if numbers[x]%2 == 0:
        even+=1
    else:
        uneven+=1

print('There are ', even, ' numbers and', uneven, " uneven numbers")
