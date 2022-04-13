'''
Given an integer array nums, move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.


Example:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

'''

def moveSums(nums):
    zero = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero+=1
    return nums
input = [0,1,0,3,12]
print(moveSums(input))