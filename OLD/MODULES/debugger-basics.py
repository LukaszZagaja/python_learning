import pdb
x = [1,2,3]
y = 2
z = 3

''' DEBUGGING WITH PRINT STATEMENT
result = y + z
print(y)
print(z)
print(result)

result2 = x + y
print(result2)
print(x)
'''

result_one = y + z

pdb.set_trace()
# TO QUIT DEBUGGER JUST TYPE 'q'

result_two = y + x
