list1 = [1,2,3,4,5,6,7,8,9,10]

# Normal
new_list = []
for item in list1:
    new_list.append(item*2)

print(f'Starting list:       {list1}')
print(f'List using for loop: {new_list}')

# list comprehension:
newer_list = [item*2 for item in list1]
print(f'List comprehension:  {newer_list}')
