def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            print(arr[j], arr[j+1])
            if arr[j]>arr[j+1]:
                print(arr[j],'>',arr[j+1], 'hence swap')
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        print('after', i+1,'th loop ->',arr)
    return arr

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

print(bubbleSort(numbers))