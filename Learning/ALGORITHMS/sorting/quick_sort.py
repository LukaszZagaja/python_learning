def quick_sort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left, partition_pos-1) # partition - 1 means its called on all elements smaller than pivot point (in this scenario its last element of array)
        quick_sort(arr, partition_pos+1, right) # called on subarray that are greater than the pivot element


def partition(arr, left, right):
    i = left # i searches for element bigger than pivot, moves from left to right
    j = right-1 # defines the point right of the pivot (i.e.    [val1,val2,val3,pivot,point]) 
                # j searches for element smaller than pivot, moves from right to left
    # i and j moves till they cross their ways
    pivot = arr[right]
    while i < j: #while they didnt cross 
        while i < right and arr[i] < pivot: # when value of arr[i] is bigger than pivot it stops 
            i+=1
        
        while j > left and arr[j] >= pivot: # when value of arr[j] is smaller than pivot it stops
            j-=1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    if arr[i] > pivot:
        arr[i],arr[right] = arr[right],arr[i]

    return i # returns value where value is already sorted || returns where to split the array while recursively calling the function


array1 = [22,11,88,66,55,77,33,44,99]
quick_sort(array1,0,len(array1)-1)
print(array1)