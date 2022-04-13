def firstNonRepeatingChar(str1):
    # char_order = []
    # counts = {}
    # for c in str1:
    #     if c in counts:
    #         counts[c] += 1
    #     else:
    #         counts[c] = 1
    #         char_order.append(c)
    # print(char_order)
    # print(counts)
    # for c in char_order:
    #     if counts[c] == 1:
    #         return c
    # return None
    uniqueChars = []
    chars = {}

    for i in range (len(str1)):
        currentChar = str1[i]
        if currentChar in chars:
            chars[currentChar]+=1
        else:
            chars[currentChar] = 1
            uniqueChars.append(currentChar)
    
    result = []
    for char in uniqueChars:
        if char in chars:
            if chars[char] == 1:
                result.append(char)
    return ''.join(result)

print(firstNonRepeatingChar('PythonforallPythonMustforall'))
print(firstNonRepeatingChar('tutorialspointfordeveloper'))
print(firstNonRepeatingChar('AABBCC'))
