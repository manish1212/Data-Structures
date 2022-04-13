import timeit
def reverseString(str):
    backward = []
    totalLen = len(str)
    
    # using reversed() (reversed start from totalLen - 1 where as range start from totalLen)
    # e.g if len is 17 --> reversed will start from 16 (because range goes until second last) --> hence reverse of that
    for i in reversed(range(totalLen)):
        backward.append(str[i])
    print(''.join(backward),'\n')
    # return backward

    # using range function 
    for i in range(totalLen -1, -1, -1):
        backward.append(str[i])
    # print(''.join(backward))
    # return backward


    # one liner to reverse a string
    print('lol',str[::-1])
    print('lol2', ''.join(reversed(str)))


string = "hsinaM si eman yM"
# reverseString(string)
# min(timeit.repeat(lambda: reverseString(string)))

def reverseBySwapping(str):
    start = 0
    input = list(str)
    end = len(input)-1
    while start<end:
        temp=input[start]
        input[start]=input[end]
        input[end]=temp
        start+=1
        end-=1
    return ''.join(input)

print("reverseBySwapping",reverseBySwapping(string))

arr = ['a','b','c','d']
print(5%2)