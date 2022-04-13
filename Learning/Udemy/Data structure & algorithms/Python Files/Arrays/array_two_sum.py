'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1]
'''


# negative numbers
# better than O(n^2)
# indicies when no match?
# naive approach

# 1
def naiveApproach(a, target):
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if a[i]+a[j] == target:
                return i,j

nums=[-2,7,11,15]
tg=9
# print(naiveApproach(nums, tg))



# 2
def betterApproach(arr, target):
    visited={}
    for index, value in enumerate(arr):
        if value in visited:
            return [visited[value], index]
        visited[target-value] = index 
nums1=[-2,7,11,15]
tg2=9
print(betterApproach(nums1, tg2))
# Time Complexity O(n)