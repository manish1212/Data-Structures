def insertionSort(arr):
    for i in range(1,len(arr)): # start with the first element
        key_item = arr[i]
        j=i-1
        while j>=0 and arr[j]>key_item:
            arr[j+1]=arr[j] # swaps until arr[j] < key_item
            j-=1
        arr[j+1]=key_item # when arr[j] is not greater/j==-1 then key_item replace it with current positon of j
        # print('after',i,'th loop',arr)
    return arr

numbers = [99, 44, 6, 50, 1, 5, 63, 87, 283, 4, 0]
print('final',insertionSort(numbers))