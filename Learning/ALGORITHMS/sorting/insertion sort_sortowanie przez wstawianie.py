def insertionSort(list1):
    for i in range(1, len(list1)): # current item is index of i |||  from 1 not 0 because we assume that first element is already sorted
        key = list1[i] 
        j = i-1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < list1[j]:
            list1[j+1] = list1[j]
            j -= 1 # without this line, it will run infinitely 
        # Place key at after the element just smaller than it.
        list1[j+1] = key
        print(list1)


trial_list = [1,6,2,7,5,10,4,8,3,9]
insertionSort(trial_list)