dict1 = {'one':'une', 'two':'deux', 'three':'trois'}
dict2 = {'one':'jeden', 'two':'dwa', 'three':'trzy'}
print(f'Whole dictionary: {dict1}')

# clear
dict1.clear()
print(f'Dictionary after clear() method: {dict1}')

# copy
print(f'\nDictionary 2: {dict2}')
dict3 = dict2.copy()
print(f'Dictionary 3 after copying dict2 with copy() method: {dict3}')

# fromkeys
dict4 = {}.fromkeys([1,2,3], '0')
print(dict4)

# get
print(dict2.get('one', 'jeden'))
print(dict2.get('ten', 350)) # if first value is not present, then 2nd one is standard value shown 

# items
print(f'\nItems of dictionary2: {dict2.items()}') # return items as tuples

# keys
print(f'List of keys of dict2: {dict2.keys()}')

# popitem
print(f'Dict2 before popitem: {dict2}')
print(f'popitem() function: {dict2.popitem()}')
print(f'Dict2 after popitem(): {dict2}')

# setdefault
print('\nsetdefault method: ')
print(f'{dict2.setdefault("two", "added")}')
print(dict2)
print(f'{dict2.setdefault("dwa", "deux")}')
print(dict2)

# pop
print(f'Pop: {dict3.pop("une", "value not present")}')
print(f'Pop: {dict2.pop("dwa", "Value not present")}')

# values
print(f'Values of dict3: {dict3.values()}')

# update
new_dict = {'four':'cztery', 'five':'piec', 'six':'szesc', 'seven':'siedem'}
print(f'Dict3 before update: {dict3}')
dict3.update(new_dict)
print(f'Dict3 after update: {dict3}')
