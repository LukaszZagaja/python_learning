def bubbleSort(list):
    #temp=0
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                #temp = list[j]
                #list[j] = list[j+1]
                #list[j+1] = temp
    print(list)
                 
list1 = [2,1,3,7,10,4,6,21]

bubbleSort(list1)