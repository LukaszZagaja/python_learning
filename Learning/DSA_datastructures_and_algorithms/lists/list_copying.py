original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
copied_list = original_list # copied array equals original meaning theye're the same thing in memory so if we change one of them, second one changes too
new_list = original_list[::] # its copied the way that it is completely 'new' array in memory, its the same but for computer its different thing

print(f'\nOriginal list: {original_list}')
print(f'Copied list:   {copied_list}')
print(f'Copied list 2: {new_list}')

print('\n\n Changed lists:')

copied_list[0] = 'new_item'
new_list[0] = 'different new item'

print(f'Original list: {original_list}')
print(f'Copied list:   {copied_list}')
print(f'Copied list 2: {new_list}')
