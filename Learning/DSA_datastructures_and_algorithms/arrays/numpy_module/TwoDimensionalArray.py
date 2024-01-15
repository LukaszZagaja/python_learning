import numpy as numpy

# day 1: 11, 15, 10, 6
# day 2: 10, 14, 11, 5
# day 3: 12, 17, 12, 8
# day 4: 15, 18, 14, 9

two_dim_arr = numpy.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print('\n', two_dim_arr)

#new_two_dim = numpy.insert(two_dim_arr, 0, [[1,2,3,4]], axis=0) # axis=1 -> adding as column, axis=0 -> adding as row
                            #     this 0 ^ means in which row the new array is added. 
#print(new_two_dim)

new_two_dim = numpy.append(two_dim_arr, [[1,2,3,4]], axis=0) # adds at the end of the array, depends on axis
print(new_two_dim)
