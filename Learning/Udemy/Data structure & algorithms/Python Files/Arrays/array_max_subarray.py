'''
Given an integer array nums, 
find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum

Example : 
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

'''

# better than O(n)

def maxSubarray(arr):
    finalMax = currentMax = arr[0]
    for num in arr[1:]:
        currentMax = max(currentMax + num, num)
        finalMax = max(currentMax, finalMax)
    return finalMax
nums = [5,4,-1,7,8]
print(maxSubarray(nums))