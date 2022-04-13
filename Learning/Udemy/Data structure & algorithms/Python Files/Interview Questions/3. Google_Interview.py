# [1,2,3,9] = 8
# [1,2,4,4] = 8
# in memory, ordered, repeated (same element at same index)
# integers, negative

# Naive approach
# array1 = [1,2,3,9]
# # array1 = [1,2,4,4]
# def checkSum(arr1):
#   for i in range(len(arr1)-1):
#     for j in range(i+1,len(arr1)):
#       first = arr1[i]
#       second = arr1[j]
#       if first+second == 8:
#         return True
#   return False


# print(checkSum(array1))
# O(n^2) quadratic time

# Better approach when array is sorted
# array = [1,2,3,9]
# array = [1,2,4,4]
# result = 8

def checkSum2(arr):
  low = 0
  high = len(arr) - 1
  while(low < high):
    sum = arr[low] + arr[high]
    if(sum == result):
      return True
    elif (sum > result):
      high -= 1
    elif (sum < result):
      low += 1
  return False

# print(checkSum2(array))
# Time complexity O(n) 
# Space complexity O(n)


# Better Solution #2 when the array is not sorted
# array = [1,2,3,9]
array = [1,2,4,4]
result = 8

def checkSum3(arr):
  comp = set() # compliment
  for val in arr:
    print(comp)
    if val in comp:
      return True
    comp.add(result - val)
  return False


print(checkSum2(array))
# Time Complexity O(n)
