# "i am good because i am good" - "i am good because"
# "i am good because 23 i am good" 

# 1
def uniqueWords(str):
    arr = str.split()
    uniqueset = set(arr)
    return uniqueset

input = "i am good because 23 i am good"
print(uniqueWords(input))


# 2
#     9
#   5   15
# 1  6 2  20



def isbst(root, lastel):
    if root.left:
        isbst(root.left)

    if root.val < lastel:
        return False
    # list.append(root.val)

    if root.right:
        isbst(root.right, )
    return True

isBinary = isbst(9,[])

1,5,6,9,2,15

# for i in range(1,isBinary):
#     if isBinary[i]<isBinary[i-1]:
#         return False



