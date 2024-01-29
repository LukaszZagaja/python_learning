import array

# 1. Create an array and traverse
print('\nStep 1.')
my_array = array.array('i', [1,2,3,4,5])

for i in my_array:
    print(i)

# 2. Access invidual elements through indexes
print('\nStep 2.')
print(my_array[0])

# 3. Append any value to the array using append() method
print('\nStep 3.')
my_array.append(6)
print(my_array)

# 4. Insert value into array using insert() method
print('\nStep 4.')
my_array.insert(0, 0)
print(my_array)

# 5. Extend python array using extend() method
print('\nStep 5.')
arr1 = array.array('i', [11,12,13,14])
my_array.extend(arr1)
print(my_array)

# 6. Add items from list into array using fromlist() method
print('\nStep 6.')
list1 = [21,22,23]
my_array.fromlist(list1)
print(my_array)

# 7. Remove any array elements using remove() method
print('\nStep 7.')
my_array.remove(14) # removes first instance of the value
print(my_array)

# 8. Remove last element using pop() method
print('\nStep 8.')
my_array.pop() # without value inside removes the last element
print(my_array)

# 9. Fetch any element through it index using index() method
print('\nStep 9.')
print('Fetched index of value 12 is: {}'.format(my_array.index(12)))
print('.index() method searches for value and returns id of this value')

# 10. Reverse array using reverse() array
print('\nStep 10.')
print(f'Array: {my_array}')
my_array.reverse()
print('Reversed array: {}'.format(my_array))
my_array.reverse()

# 11. Get array buffer information through buffer_info() method
print('\nStep 11.')
# buffer_info() provides array buffer start address in the memory and number of elements
print('Array buffer: ', my_array.buffer_info())

# 12. Check for number of occurances of an element using count() method
print('\nStep 12.')
my_array.append(3)
print(f'Amount of times that 3 is present in array: {my_array.count(3)}')

# 13. Convert array to list with the same elements using tolist() method
print('\nStep 13.')
temp_list = my_array.tolist()
print(temp_list)

# 14. Slice elements from an array
print('\nStep 14.')
print(my_array[::2]) # the same way like string
print(my_array[::-1])

