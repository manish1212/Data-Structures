# Interview3

'''
Input: 
list1 = [[0,2],[5,10],[13,23],[24,25]], 
m
         
list2 = [[1,5],[8,12],[15,24],[25,26]]
n

Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

-- 0,1,2
     m
-- 1,2,3,4,5
     n


-- 5,6,7,8,9,10
-- 8,9,10,11,12

Input: 
list1 = [[1,7]] ->1,2,3,4,5,6,7 ([[0][0], [0][1]])
         i
list2 = [[3,10]] -> 3,4,5,6,7,8,9,10
        j

i = 0
j = 0

nums
nums[i][0], nums[i][1]
nums[j][0], nums[j][1]

result = []
currArr = []

if 1<3<7 (j)
    currArr.append(3)
    
if i<5<7 
    currArr.append(3)
if 
result.append(currArr)



    
Output: [[3,7],[8,10],[11,12]]


Input: 
list1 = [[1,7]] ->1,2,3,4,5,6,7 ([[0][0], [0][1]])
         i
list2 = [[3,10]] -> 3,4,5,6,7,8,9,10
'''
# nums[i][0], nums[i][1]
# nums[j][0], nums[j][1]

def Intersection(list1, list2):
    i = 0
    j=0
    
    while i < len(list1):
        l11, l12 = list1[i][0], list1[i][1]
        l21, l22 = list1[j][0], list1[j][1]
        curr = []
        if l21>l11:
            if l21<l12:
                curr.append(l21)
            else:
                i+=1

list1 = [[1,7],[8,12]]
list2 = [[8, 10],[11,15]]

Intersection(list1, list2)

