def merge_sort(arr):
    if len(arr) > 1:
        left_array = arr[0:len(arr)//2] # from start to middle, if arr%2 != 0 then left array is smaller than right
        right_array = arr[len(arr)//2:] # from middle to end

        # recursion
        merge_sort(left_array)
        merge_sort(right_array)
        # after recursion arrays are 'sorted' -> array with 1 len are always sorted
        # In short, there only array with lenght of 1 left after this recursion

        # merge
        l = 0 # keeps track of leftmost element of left array
        r = 0 # - || -   - || - rightmost  - || -    - || -
        m = 0 # keeps track of index in merged array
        while l < len(left_array) and r < len(right_array):
            if left_array[l] < right_array[r]:
                arr[m] = left_array[l]
                l+=1
                #m+=1
            else:
                arr[m] = right_array[r]
                r+=1
                #m+=1
            m+=1 # can use inside if and else, if it is only here then code becomes less redundant


        # if right array is empty but left still has values
        while l < len(left_array):
            arr[m] = left_array[l]
            l+=1
            m+=1
        
        # if left arr is empty but right still has values
        while r < len(right_array):
            arr[m] = right_array[r]
            r+=1
            m+=1
    #return arr # can be used but not mandatory

test_arr = [2,1,3,7,5,1,7,4,4,4,2,6,0]

merge_sort(test_arr)
print(test_arr)
