def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        temp = arr[i]
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i]=arr[min]
        arr[min]=temp
    return arr

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print('final',selectionSort(numbers))