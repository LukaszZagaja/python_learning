dict1 = {
    1:'one',
    2:'two',
    9:'nine',
    5:'five',
    3:'three',
    7:'seven'
         }

dict2 = {
    0:'zero',
    1:'one',
    10:'ten',
    False:'False'
}

print(f'\nDict1: {dict1}')
print(f'Dict2: {dict2}')
print(f'3 in dict1: {3 in dict1}') 


print(f'"three" in dict1: {"three" in dict1}') # only works with keys, not values
print(f'"three" in dict1 using values(): {"three" in dict1.values()}')
# 'not in' is just opposite of 'in'
print(f'Len(): {len(dict1)}')


print(f'All() dict1: {all(dict1)}') # all checks if bools are true and if 0 is not present (0 means that something is false so all would return false)
print(f'All() dict2: {all(dict2)}') # in all() everything has to be true, every key must be integer (excluding 0) or booleans that are not false

print(f'Any() dict1: {any(dict1)}') # every key true -> true;  at least one key is true -> true; no true key -> false
print(f'Any() dict2: {any(dict2)}')

print(f'\n Dict1: {dict1}')
print(f'sorted dict1: {sorted(dict1)}') # sorted returns sorted keys 
