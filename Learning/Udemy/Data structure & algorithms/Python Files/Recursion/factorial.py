def factorialRecursive(num):
    if num == 2:
        return 2
    return num*factorialRecursive(num-1)

print(factorialRecursive(5))

def factorialIterative(num):
    fact = 1
    for i in range(num,1,-1):
        fact *= i
    return fact

print(factorialIterative(5))

'''
3 rules:
1. Identify the base case
2. Identify the recursive case
3. get closer and closer and return when needed (usually 2 returns – for base and recursive case)
'''