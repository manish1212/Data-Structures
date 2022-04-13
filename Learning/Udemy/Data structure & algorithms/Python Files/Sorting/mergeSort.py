def mergeSort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]

    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    result = []
    leftIndex = 0
    rightIndex = 0
    
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex+=1
        else:
            result.append(right[rightIndex]) 
            rightIndex+=1
    return result + left[leftIndex:] + right[rightIndex:]

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(mergeSort(numbers))