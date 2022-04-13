class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
            self.length+=1
            return
        self.tail.next = newNode
        self.tail = newNode
        self.length+=1

    def dequeue(self):
        if self.length == 0:
            return None
        if self.head == self.tail:
            self.tail=None
        self.head = self.head.next
        self.length-=1
        return
    
    def peek(self):
        if self.length >0:
            return self.head.data

    def printQueue(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next
        print('head', self.head.data)
        print('tail', self.tail.data)
        print('totallen', self.length)

myqueue = Queue()
myqueue.enqueue('google')
myqueue.enqueue('chrome')
myqueue.enqueue('firefox')
myqueue.enqueue('safari')
myqueue.dequeue()
myqueue.dequeue()
myqueue.printQueue()
print('Peek',myqueue.peek())
        