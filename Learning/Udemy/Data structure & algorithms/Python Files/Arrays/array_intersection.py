'''
array1 = [2,5,8,9,12,15,18]
array2 = [5,7,10,11,12,13]

result = {5,12}
'''
# another question what if one of the array is huge...

def intersections(arr1, arr2):
    i=0
    j=0
    m=len(arr1)
    n=len(arr2)
    result=[]
    
    while i<m and j<n:
        if arr1[i]<arr2[j]:
            i+=1
        elif arr2[j]<arr1[i]:
            j+=1
        elif arr1[i] == arr2[j]:
            result.append(arr1[i])
            i+=1
            j+=1
    return result

array1 = [5,5,7,12]
array2 = [2,5,5,8,9,12,15,18]
print(intersections(array1,array2))