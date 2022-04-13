# Google Question
# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1

# Given an array = [2,3,4,5]:
# It should return undefined

'''Brute Force'''
# approach 1
def firstRecurring(arr):
    flag = False
    index=0
    n=len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                index=i
                i+=1
                n=j
                flag =True
                break
    if index == 0 and not flag:
        return False
    return arr[index]

# Approach 2
# array = [2,3,2,5,5,4,3,2]
def firstRecurring2(arr):
    i=j=0
    length = len(arr)-1
    finalIndex=-1
    while i<length:
        j=i+1
        while j<length:
            if arr[i]==arr[j]:
                finalIndex=i
                i+=1
                length=j
                break
            j+=1
        i+=1
    if finalIndex != -1:
        return arr[finalIndex]
    return False


# *************************************

# best Solution
def firstRecurring3(arr):
    visited = set()
    for i in range(len(arr)):
        current = arr[i]
        if current in visited:
            return current
        visited.add(current)
    return False

array = [2,3,2,5,5,4,3,2]
# array = [2,1,1,2,3,5,1,2,4]
# print(firstRecurring(array))
print(firstRecurring2(array))
# print(firstRecurring3(array))