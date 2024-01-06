s = set()
s.add(1)
s.add(2)
print(s)

s.add(2) # there cannot be duplicates in sets
print(s)

# Clearing sets
print('Clearing sets')
s.clear()
print(s)

# Copying sets 
print('------ Copying -----')
s = {1,2,3}
sc = s.copy()
s.add(4)
print(s)
print(sc)

# Difference of 2 or more sets
print('----- Difference -----')
print(s.difference(sc)) # returns only difference 

# Difference update 
print('----- Difference update -----')
s1 = {1,2,3}
s2 = {1,4,5}
s1.difference_update(s2) # returns s1 after removing every similar value that s2 has
print(s1)

# Discard
print('----- Discard -----')
print(s)
s.discard(2) # if value is inside given set then it will be deleted, if not -> nothing happens
print(s)

# Intersect
print('----- Intersection -----')
s1 = {1,2,3,}
s2 = {1,2,4}
print(s1.intersection(s2)) # returns what exists in both sets, in this case its 1,2
s1.intersection_update(s2) # gives s1 value of s1.intersection(s2)
print(s1)

# Isdisjoint
print('----- isdisjoint -----')
s1 = {1,2,3}
s2 = {1,2,4}
s3 = {5}
print(s1.isdisjoint(s2)) # return True is intersection equals NULL
print(s1.isdisjoint(s3))

# issubset
print('----- issubset -----')
s1 = {1,2}
s2 = {1,2,4}
print(s1.issubset(s2)) # returns True if s1 is subset of s2
print(s2.issuperset(s2)) # returns True is s1 is subset of s2 (i.e. s1 is inside s2)

# symmetric_difference
print('----- symmetric_difference -----')
print(s1.symmetric_difference(s2)) # it is the opposite of intersection
# Same thing with symmetric_difference_update -> it does the same thing but changes value of s1 

# union
print('----- Union -----')
s1 = {1,2,3}
s2 = {4,5,6}
print(s1.union(s2)) 

# update
print('----- Update -----')
s1.update(s2)
print(s1)

