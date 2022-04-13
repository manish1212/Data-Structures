class Stack():
    def __init__(self) -> None:
        self.array = []
    
    def push(self, value):
        self.array.append(value)
    
    def peek(self):
        return self.array[len(self.array)-1]

    def pop(self):
        self.array.pop()


    def printStack(self):
        print(self.array)

# Implement Queue's using stack
    def enqueue(self, value):
        self.array.append(value)
        return
    
    def dequeue(self):
        del self.array[0]
        return

    def peekQueue(self):
        return self.array[0]


# mystack = Stack()
# mystack.push('google')
# mystack.push('firefox')
# mystack.push('chrome')
# mystack.push('safari')
# mystack.printStack()
# print(mystack.peek())
# mystack.pop()
# mystack.pop()
# mystack.pop()
# mystack.printStack()

# 
myqueue = Stack()
myqueue.enqueue('manish')
myqueue.enqueue('ruben')
myqueue.enqueue('arthur')
myqueue.dequeue()
# myqueue.dequeue()
print('first in queue', myqueue.peekQueue())
myqueue.printStack()
