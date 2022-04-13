'''
Given an array, rotate the array to the right by k steps, 
where k is non-negative.

Example:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
'''

'''Approach 1'''
def rotateArray(nums, k):
    a = [0]*len(nums)
    for i in range(len(nums)):
        a[(i+k)%len(nums)]=nums[i]
    for i in range(len(nums)):
        nums[i]=a[i]
    return nums
# Time Complexity O(2n) ~ O(n)
# Space Complexity O(n)


'''Approach 2 -->'''
def rotateArray2(nums, k):
    k%=len(nums)
    reverse(nums, 0, len(nums)-1)
    reverse(nums, 0,k-1)
    reverse(nums, k, len(nums)-1)
    return nums

def reverse(arr, start, end):
    while start<end:
        temp = arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start+=1
        end-=1   
    return arr 

# Time Complexity O(n)
# Space Complexity O(1)



input=[1,2,3,4,5,6,7]
steps=3
# print(rotateArray(input,steps))
print(rotateArray2(input,steps))