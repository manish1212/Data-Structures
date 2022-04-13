
def searchInsert(nums, target):
    low=0
    high=len(nums)-1

    while low <= high:
        mid = (high+low)//2
        if target == nums[mid]:
            return mid 
        elif nums[mid]>target:
            high= mid-1
        else:
            low = mid+1
    return low

target = 15
numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
print('final',searchInsert(numbers, target))


