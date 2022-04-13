
# Find the minimum number of position a knight takes from source to destination
import sys
from collections import deque
 
 
# A queue node used in BFS
class Node:
    # (x, y) represents chessboard coordinates
    # `dist` represents its minimum distance from the source
    def __init__(self, x, y, dist=0):
        self.x = x
        self.y = y
        self.dist = dist
 
    # As we are using `Node` as a key in a dictionary,
    # we need to override the `__hash__()` and `__eq__()` function
    def __hash__(self):
        return hash((self.x, self.y, self.dist))
 
    def __eq__(self, other):
        return (self.x, self.y, self.dist) == (other.x, other.y, other.dist)
 
 
# Below lists detail all eight possible movements for a knight
row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]
bp = set()
 
# Check if (x, y) is valid chessboard coordinates.
# Note that a knight cannot go out of the chessboard
def isValid(x, y, N):
    return not (x < 0 or y < 0 or x >= N or y >= N)

def bisphopPositions(src, N):
    x = src.x
    y = src.y
    # 1st diagonal "\" -> max number of position could be 8
    # 2nd diagonal "/" -> max number of position could be 8
    bp.add((x,y))
    for i in range(N):
        x = x-1
        y = y-1
        if isValid(x, y, N):
            bp.add((x,y))
            print('1',bp)
    x = src.x
    y = src.y
    for i in range(N):
        x = x+1
        y = y+1
        if isValid(x, y, N):
            bp.add((x,y))
            print('2',bp)
    x = src.x
    y = src.y
    for i in range(N):
        x = x-1
        y = y+1
        if isValid(x, y, N):
            bp.add((x,y))
            print('3',bp)
    x = src.x
    y = src.y
    for i in range(N):
        x = x+1
        y = y-1
        if isValid(x, y, N):
            bp.add((x,y))
            print('4',bp)
    print('check if the knight is bishops range', (1,0) in bp)


# Find the minimum number of steps taken by the knight
# from the source to reach the destination using BFS
def findShortestDistance(src, dest, N):
 
    # set to check if the matrix cell is visited before or not
    visited = set()
 
    # create a queue and enqueue the first node
    q = deque()
    q.append(src)
 
    # loop till queue is empty

    while q:
 
        # dequeue front node and process it
        node = q.popleft()
 
        x = node.x
        y = node.y
        dist = node.dist
 
        # if the destination is reached, return distance
        if x == dest.x and y == dest.y:
            return dist
 
        # skip if the location is visited before
        if node not in visited:
            # mark the current node as visited
            visited.add(node)
 
            # check for all eight possible movements for a knight
            # and enqueue each valid movement
            for i in range(len(row)):
                # get the knight's valid position from the current position on
                # the chessboard and enqueue it with +1 distance
                x1 = x + row[i]
                y1 = y + col[i]
 
                # print((x1,y1) not in bp)
                if isValid(x1, y1, N) and (x1,y1) not in bp:
                    q.append(Node(x1, y1, dist + 1))
    
    # return infinity if the path is not possible
    return sys.maxsize
 
 
if __name__ == '__main__':
 
    N = 8                # N x N matrix
    src = Node(0, 7)    # source coordinates
    dest = Node(7, 0)   # destination coordinates

    bsrc = Node(2,3)
    bisphopPositions(bsrc, N)
    
    print("The minimum number of steps required is",
          findShortestDistance(src, dest, N))