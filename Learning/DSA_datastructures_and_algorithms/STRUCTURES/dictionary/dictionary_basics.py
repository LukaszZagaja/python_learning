# updating
dict1 = {'name':'Eddie', 'age': 26, 'address':'London', 'school':'Oxford'}
print(dict1)
dict1['age'] = 20
print(dict1)

# adding to dict
dict1['education']='masters'
print(dict1)

# deleting an element
print(f'\nBefore deleting: {dict1}')
del dict1['education']
print(f'After deleting: {dict1}')

removed_ele = dict1.pop('name', None) # <- None will be there if previous value got misspelled, if there wont be None then there can be exception when misspelled value
# before 3.7 pop was deleting random value, after 3.7 it removes last one
print(f'Element removed: {removed_ele}')
print(f'Dictionary after pop method: {dict1}')

# traversing
def traverse(dict):
    for key in dict:
        print(key, dict[key])

traverse(dict1)

# searching for an element
# linear search
def search(dict, value):
    for key in dict:
        if dict[key]==value:
            return key, value
    return 'Value does not exist'

print(f'searching: {search(dict1, 20)}')

# Clearing whole dict
dict1.clear()
print(f'Dict after clear() method: {dict1}')
