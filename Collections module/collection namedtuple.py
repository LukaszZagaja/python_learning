from collections import namedtuple

'''
NORMAL TUPLE
'''
mytuple = (10,20,30)
print(mytuple[0])

'''
NAMED TUPLE
'''
print("\n\n")

Dog = namedtuple('Dog', ['breed', 'age', 'name'])
Rex = Dog(breed='German Shepherd', age=7, name='Rex')
print(type(Rex))
print(Rex)
print(Rex.age)
print(Rex.breed)
print(Rex[2])