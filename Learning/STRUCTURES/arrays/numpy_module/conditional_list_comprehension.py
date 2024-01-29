list1 = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
new_list = [number**2 for number in list1 if number < 0]

#print(f'\nOriginal list:                           {list1}')
#print(f'Numbers smaller than 0 to the root of 2: {new_list}\n')

newer_list = [number if number > 0 else 0 for number in list1]
print(f'List comprehension with if: {newer_list}')