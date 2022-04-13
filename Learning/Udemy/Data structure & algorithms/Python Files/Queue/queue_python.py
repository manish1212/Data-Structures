from collections import deque
q = deque()
# q.pop()
# q.popleft()

q.append('a')
q.append('b')
q.append('c')

print(q)
print('pop the last element',q.pop())
print('pop the first element',q.popleft())
print(q)

