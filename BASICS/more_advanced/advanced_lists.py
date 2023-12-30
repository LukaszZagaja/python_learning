l = [1,2,3]

print('\n')
l.append(4)
print(l.count(1))
print('\n')

###----------- Difference between append and extend
print('Difference between append and extend')
x = [1,2,3]
x.append([4,5])
print(x) # x looks like: [1, 2, 3, [4, 5]] \\ added whole thing as 1, list is 4 long 

x = [1,2,3]
x.extend([4,5])
print(x) # x looks like: [1, 2, 3, 4, 5] \\ added each thing separately, list is 5 long
print('\n')


# Inserting
print('----- INSERT -----')
print(l)
print(l.index(2)) # if something is not in list then it returns value error
l.insert(2, 'inserted') # in given index place object 
print(l)


# Deleting
print('----- POP -----')
print(l.pop()) # pop can be given index as value
print(l.pop(0))
print(l)

print('----- REMOVE -----')
print(l.remove('inserted')) # deletes first instance of given value 
print(l)

a = [1,2,3,4,5,3,3]
print('\n')
print(a)
a.remove(3)
print(a)
print('\n')

# Sorting
print("----- SORTING -----")
a.sort()
print(a)

