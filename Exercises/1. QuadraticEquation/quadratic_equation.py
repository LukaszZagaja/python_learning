from math import pow
from math import sqrt
# x**2 + 5*x + 4 = 0
# Drugie zadanie
l1 = 4
l2 = 3
l3 = 4.5
l4 = 5
quad = l1*l2*l3*l4
x = int(quad**(1/4))
print('Geometric mean: ', x)



# Pierwsze zadanie
delt = (pow(x,2) + x*5 + 4)
print('\n')

if int(delt) > 0:
    x1 = (-5 - sqrt(delt))/2
    x2 = (-5 + sqrt(delt))/2
    print('Delta > 0')
    print('x1 = ', x1, '\nx2 = ', x2)
elif int(delt) == 0:
    x0 = -5/2
    print('\nDelta = 0')
    print('x0 = ', x0)
else:
    print("Delta < 0")
    