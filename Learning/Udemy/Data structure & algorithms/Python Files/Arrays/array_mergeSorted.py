# merge 2 sorted arrays

def mergeSorted(arr1, arr2):
    # initialization
    mergedArray = []
    i = 0
    j = 0
    # if either are empty return other
    if(len(arr1) == 0 or len(arr2) == 0):
        return arr1 + arr2
    # logic
    while i<len(arr1) and j<len(arr2):
        if arr1[i] <= arr2[j]:
            mergedArray.append(arr1[i])
            i+=1
        elif arr2[j]<arr1[i]:
            mergedArray.append(arr2[j])
            j+=1
    return mergedArray+arr1[i:]+arr2[j:]

array1 = [0,3,4,19,32,43,55,60]
array2 = [4, 6,30,40]
print(mergeSorted(array1,array2))
