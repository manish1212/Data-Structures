# Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items
#For Example:
#const array1 = ['a', 'b', 'c', 'x'];
#const array2 = ['z', 'y', 'i'];
#should return false.
#-----------
#const array1 = ['a', 'b', 'c', 'x'];//const array2 = ['z', 'y', 'x'];
#should return true.

# 2 parameters - arrays - no size limit
# return true or false

array1 = ['a','b','c','x']
array2 = ['z','y','z']

# Naive Solution 1
# def containsCommonItems(arr1, arr2):
#     for x in arr1:
#         for y in arr2:
#             if(x == y):
#                 return True
#     else:
#         return False
                
# print(containsCommonItems(array1, array2))  
# O(a*b)

# Better Solution 2
def containsCommonItems2(arr1, arr2):
    # create a dictonary 
    dict = {}
    for x in arr1:
        dict[x]=True
        
    # check if the value is true in another loop
    for x in arr2:
        if(dict.get(x)):
            return True
            
    # if no match found
    return False

print(containsCommonItems2(array1, array2))  
# O(a+b)
                
                
                
                
                
                
                
                