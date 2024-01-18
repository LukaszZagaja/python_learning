tuple1 = (1,2,3,4,5)
tuple2 = (6,7,8,9,10)
tuple3 = (1,2,2,4,5,3,2,7,9,6,10,2,5)

print(tuple1 + tuple2)
print(tuple1*3)
print(f'3 in tuple2: {3 in tuple2}')
print(f'There are this much of 2 in tuple3: {tuple3.count(2)}')
print(f'Index of 6 is equal to: {tuple3.index(6)}')
print(f'Max in tuple is: {max(tuple3)}')
print(f'Min of tuple3 is: {min(tuple3)}')
print(tuple([5,4,3,2,1]))

for i in len(tuple1):
    print(tuple1[i])


