'''
Parul Upadhyaya to Everyone (11:07 AM)
// Traverse a tree in clockwise order
          //
          //        1
          //     /    \         => 1,3,7,6,5,4,2
          //    2      3        
          //   / \    / \   
          //  4   5  6   7 

          //      _____1_____
          //     /           \
          //    2             3
          //   / \            /   => 1,3,6,10,9,8,7,4,2
          //  4   5          6   
          //     / \        / \
          //    7   8      9  10
'''                        

class Node():
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def rightBorder(root,result):
    if root:
        if root.right:
            result.append(root.val)
            rightBorder(root.right, result)
        elif root.left:
            result.append(root.val)
            rightBorder(root.left, result)

def bottom(root, result):
    stack = []
    if root:
        stack.append(root)
    while len(stack)>0:
        curr_node = stack.pop()
        if curr_node.left is None and curr_node.right is None:
            result.append(curr_node.val)
        else:
            if curr_node.left is not None:
                stack.append(curr_node.left)
            if curr_node.right is not None:
                stack.append(curr_node.right)

def leftReverse(root,result):
    if root:
        if root.left:
            leftReverse(root.left, result)
            result.append(root.val)
        elif root.right:
            leftReverse(root.right, result)
            result.append(root.val)

def clockwise(root, result):
    if root:
        result.append(root.val)
        rightBorder(root.right, result)
        bottom(root, result)
        leftReverse(root.left, result)  

# Example 1
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

# Example 2
# root = Node(1)
# root.left= Node(2)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.left.right.left = Node(7)
# root.left.right.right = Node(8)
# root.right= Node(3)
# root.right.left = Node(6)
# root.right.left.left = Node(9)
# root.right.left.right = Node(10)

result = []
clockwise(root, result)
print(result)








num = 1234
print(len(str(num)))