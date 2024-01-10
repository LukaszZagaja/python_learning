import array

#my_array = array.array('i') # i means int
#print(my_array) # there no elements to store in memory

arr1 = array.array('i', [1,2,3,4,5,6])
#print(arr1)

# INSERTING VALUE INTO ARRAY
#arr1.insert(2, 9) # (id, value)  //// if id number is higher than lenght of array, then value is gonna be added at the end of the array 
                                    # (ie. array is 4 in lenght, id of added value is 100, value is gonna be added at 5th)
#print(arr1) 

# ARRAY TRAVERSAL (MOVE THROUGHT EVERY ELEMENT)
def traverseArray(array):
    for i in array:
        print(i)

#traverseArray(arr1)


# ACCESSING AN ELEMENT OF ARRAY
arr2 = array.array('i', [1,2,3,4,5,6])

def accesElement(array, index):
    if index >= len(array):
        print('There is not any element in this index')
    else:
        print(array[index])

#accesElement(arr2, 1)

# SEARCHING FOR AN ELEMENT IN ARRAY
arr3 = array.array('i', [1,2,3,4,5])
def linear_search(array, target):
    for i in range(len(arr3)):
        if array[i] == target:
            return i
    return -1

print(linear_search(arr3, 8))