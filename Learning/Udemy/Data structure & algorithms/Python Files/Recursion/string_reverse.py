def stringReverse(str):
    reversed = []
    for i in range(len(str)-1, -1, -1):
        reversed.append(str[i])
    return ''.join(reversed)

s = "hsinaM si eman yM"
print(stringReverse(s))


def reverseStringRecursive(str):
    if str == "":
        print('if', str)
        return ""
    else:
        print('else', str[1:], '--', str[0])
        return reverseStringRecursive(str[1:]) + str[0]

s = "hsinaM si eman yM"
print(reverseStringRecursive(s))


  
