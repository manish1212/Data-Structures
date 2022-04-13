class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stacks():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, data):
        newNode = Node(data)
        if self.length==0:
            self.top = newNode
            self.bottom = newNode
        else:
            holdingPointer = self.top
            self.top = newNode
            self.top.next = holdingPointer
        self.length+=1

    def peek(self):
        if self.top:
            return self.top.data


    def pop(self):
        if self.length == 0:
            self.bottom=None
        self.top = self.top.next
        self.length-=1

    def printStack(self):
        currentVal = self.top
        while currentVal:
            print("" ,currentVal.data,'\n','|','\n','¥')
            currentVal = currentVal.next
        print('head', self.top.data)
        print('Bottom', self.bottom.data)
        print('totallen', self.length)


stack = Stacks()
stack.push('a')
stack.push('b')
stack.push('c')
stack.push('d')
stack.printStack()
print("Peek : ", stack.peek())
stack.pop()
stack.printStack()