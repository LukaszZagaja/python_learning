def linearSearch(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1
        
print(linearSearch([0, 20,40,60,80,100], 80))