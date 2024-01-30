def insertionSort(list1):
    for i in range(1, len(list1)): # current item is indes of i
        key = list1[i] 
        j = i-1 # previous item is index j
        while j>=0 and key<list1[j]:
            list1[j+1] = list1[j]
            j -= 1 # without this line, it will run infinitely 
        list1[j+1] = key
    print(list1)


trial_list = [1,6,2,7,5,10,4,8,3,9]
insertionSort(trial_list)