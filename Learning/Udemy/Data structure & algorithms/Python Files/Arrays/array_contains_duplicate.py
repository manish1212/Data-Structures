'''
Given an integer array nums, 
return true if any value appears at
least twice in the array, 
and return false if every element is distinct.

Example:
Input: nums = [1,2,3,1]
Output: true
'''

# naive approach
def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
input = [1,2,3,1]
print(containsDuplicate(input))


# Better Approach
def containsDups(nums):
    contains = set()
    for num in nums:
        if num in contains:
            return True
        contains.add(num)
    return False
print(containsDups(input))
