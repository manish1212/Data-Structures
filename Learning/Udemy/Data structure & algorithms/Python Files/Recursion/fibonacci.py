'''
Given a number N return the index value of the Fibonacci sequence, where the sequence is:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
the pattern of the sequence is that each value is the sum of the 2 previous values, that means that for N=5 → 2+3

For example: fibonacciRecursive(6) should return 8
'''

# sol 1 
# def fiboIterative(n): # O(n)
#     if n<2:
#         return n
#     a=0
#     b=1
#     total=0
#     for i in range(n-1):
#         total=a+b
#         a=b
#         b=total
#     return total

# sol 2
def fiboIterative(n): # O(n)
    arr = [0,1]
    for i in range(2,n+1):
        arr.append(arr[i-1]+arr[i-2])
    return arr[n]

print(fiboIterative(6))

def fiboRecursive(n): # O(2^n) - exponential
    # print(n)
    if n<2:
        return n
    return fiboRecursive(n-1) + fiboRecursive(n-2)

print(fiboRecursive(6))