class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None
    
    # O(log N)
    def insert(self, value):
        newNode = Node(value)

        if self.root is None:
            self.root = newNode
            return
        currentNode = self.root

        while(True):
            if newNode.value < currentNode.value:
                # left
                if currentNode.left is None:
                    currentNode.left = newNode
                    return
                currentNode = currentNode.left
            else:
                # right
                if currentNode.right is None:
                    currentNode.right = newNode
                    return
                currentNode = currentNode.right

    # O(log N)
    def lookup(self, valueToFind):
        currentNode = self.root
        while True:
            if currentNode is None:
                return False
            if valueToFind == currentNode.value:
                return currentNode.value
            elif valueToFind < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right



    # O(log N)
    def remove(self, value):
        if self.root is None:
            return False
        currentNode = self.root
        parentNode = None

        while currentNode:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            elif value == currentNode.value:
                # main logic

                # if the right is None
                if currentNode.right == None:
                    if parentNode == None:
                        self.root = currentNode.left
                        return
                    if currentNode.value < parentNode.value:
                        parentNode.left = currentNode.left
                        return
                    elif currentNode.value>parentNode.value:
                        parentNode.right = currentNode.left
                        return

                # if right.left is none - > right.left = currentNode.left
                elif currentNode.right.left == None:
                    currentNode.right.left = currentNode.left
                    if parentNode == None:
                        self.root = currentNode.right
                        return

                    if currentNode.value<parentNode.value:
                        parentNode.left = currentNode.right
                        return
                    elif currentNode.value>parentNode.value:
                        parentNode.right = currentNode.right
                        return
                
                # if right.left is not None -> find the leftmost  
                else:
                    leftmostParent = currentNode.right
                    leftmost = currentNode.right.left
                    while leftmost.left:
                        leftmostParent = leftmost
                        leftmost = leftmost.left

                    leftmostParent.left = leftmost.right
                    leftmost.left = currentNode.left
                    leftmost.right = currentNode.right

                    if parentNode == None:
                        self.root = leftmost
                        return
                    if currentNode.value < parentNode.value:
                        parentNode.left = leftmost
                        return
                    elif currentNode.value > parentNode.value:
                        parentNode.right = leftmost
                        return

    def BreadthFirstSearch(self):
        list = []
        queue = []
        currentNode = self.root
        queue.append(currentNode)
        while len(queue)>0:
            currentNode = queue.pop(0)
            list.append(currentNode.value)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        return list    

    def BreadthFirstSearchR(self, queue, list):
        currentNode = self.root
        while len(queue)>0:
            currentNode = queue.pop(0)
            list.append(currentNode.value)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        return queue, list

    def DFSInorder(self):
        return self.traverseInorder(self.root,[])

    def DFSPreorder(self):
        return self.traversePreorder(self.root,[])

    def DFSPostorder(self):
        return self.traversePostorder(self.root,[])

    def traverseInorder(self, node, list):
        if node.left:
            self.traverseInorder(node.left, list)
        list.append(node.value)
        if node.right:
            self.traverseInorder(node.right, list)
        return list

    def traversePreorder(self, node, list):
        list.append(node.value)
        if node.left:
            self.traversePreorder(node.left, list)
        if node.right:
            self.traversePreorder(node.right, list)
        return list

    def traversePostorder(self, node, list):
        if node.left:
            self.traversePostorder(node.left, list)
        if node.right:
            self.traversePostorder(node.right, list)
        list.append(node.value)
        return list

    def printTree(self):
        return str(self.traversePrintTree(self.root))

    def traversePrintTree(self, curr):
        lines = []
        if curr.right:
            found = False
            for line in self.traversePrintTree(curr.right).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " ┌─" + line
                elif found:
                    line = " | " + line
                else:
                    line = "   " + line
                lines.append(line)
        lines.append(str(curr.value))
        if curr.left:
            found = False
            for line in self.traversePrintTree(curr.left).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " └─" + line
                elif found:
                    line = "   " + line
                else:
                    line = " | " + line
                lines.append(line)
        return "\n".join(lines)

bst = BinarySearchTree()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.insert(1)
# bst.insert(12)
# bst.insert(10)
# bst.insert(13)
# bst.remove(12)
# bst.remove(13)
# bst.remove(9)
# print(bst.lookup(9))
# print(bst.printTree())
print(bst.BreadthFirstSearch())
print(bst.BreadthFirstSearchR([bst.root], []))
# print(bst.DFSInorder())
# print(bst.DFSPreorder())
# print(bst.DFSPostorder())




# Inorder = [1, 4, 6, 9, 15, 20, 170]
# Preorder = [9, 4, 1, 6, 20, 15, 170]
# Postoder = [1, 6, 4, 15, 170, 20, 9]
'''
    ┌─170
 ┌─20
 |  └─15
9
 |  ┌─6
 └─4
    └─1
'''  

