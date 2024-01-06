d = {'k1':1, 'k2':2}

print('\n')
print({x:x**2 for x in range(10)}) # key x: x squared for every x in range 
print('\n')
print({k:v**2 for k,v in zip(['a', 'b', 'c', 'd', 'e'], range(5))})
print('\n')


