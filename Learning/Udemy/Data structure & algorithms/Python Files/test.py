# arr = [i for i in range(10)]
# arr2 =[]
# for i in range(10):
#     arr2.append(i)
# print(arr)
# print(arr2)'

# print(3//3)
# print(0%2)


# arr = [1,2,3,4,5,5,5,6]
# d = {}

# for i in range(8):
#     d[arr[i]] = d.get(arr[i], 0) + 1


# print(d)




# class Solution:
from collections import defaultdict
# class Solution:
def findCircleNum(M):
    
    graph = defaultdict(list)
    
    if not M:
        return 0
    
    n = len(M)
    for i in range(n):
        for j in range(i+1,n):
            if M[i][j]==1:
                graph[i].append(j)
                graph[j].append(i)
    
    visit = [False]*n
    
    def dfs(u):
        for v in graph[u]:
            if visit[v] == False:
                visit[v] = True
                dfs(v)
    
    count = 0
    for i in range(n):
        if visit[i] == False:
            count += 1
            visit[i] = True
            dfs(i)
    
    return count


lst = ['1100','1110','0110','0001']
print(findCircleNum(lst))
