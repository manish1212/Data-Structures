class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        return str(self.__dict__)

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        
        self.length+=1
        return self.head.data

    def prepend(self, data):
        newNode = Node(data)

        if self.head is None:
            self.tail = newNode
        
        newNode.next = self.head
        self.head = newNode
        self.length+=1

    def insert(self, index, value):
        newNode = Node(value)
        newIndex = index
        if index > self.length:
            self.append(value)
            return

        if index == 0:
            self.prepend(value)
            return

        if index < 0:
            newIndex = self.length + index

        i=0
        currentNode = self.head
        while i < self.length:
            if i == newIndex-1:
                temp = currentNode.next
                currentNode.next = newNode
                newNode.next = temp
                self.length+=1
                return
            currentNode = currentNode.next
            i+=1

    def removeByValue(self, valueToRemove):
        currentNode = self.head
        if currentNode.data is None:
            return 'Empty list'
        
        while currentNode:
            nextNode = currentNode.next
            if nextNode is None:
                return 'No element found'

            if nextNode.data == valueToRemove:
                if nextNode.next is None:
                    currentNode.next = None
                    self.tail = currentNode
                    return
                currentNode.next = nextNode.next
                self.length-=1
                return
            currentNode = currentNode.next
        return None

    def removeByIndex(self, index):
        currentNode = self.head
        i = 0
        if self.length == 0 or index>=self.length:
            return 'Insert Valid index'
        
        if index == 0:
            self.head = self.head.next 
            self.length-=1
            
        if index == self.length - 1:
            while currentNode:
                if i == index-1:
                    currentNode.next = None
                    self.tail = currentNode
                    self.length-=1
                    return
                currentNode = currentNode.next
                i+=1

        while currentNode:
            if i == index-1:
                nextNode = currentNode.next
                currentNode.next = nextNode.next
                self.length-=1
                return
            currentNode = currentNode.next
            i+=1

    def reverse(self):
        self.tail = self.head
        prev = None
        while self.head:
            temp = self.head
            self.head = self.head.next
            temp.next = prev
            prev = temp
        self.head = temp

    def listprint(self):
        printVal = self.head
        while printVal:
            print('value',printVal.data, 'next', printVal.next, self.tail.data)
            printVal = printVal.next

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
# ll.prepend(-1)
# ll.prepend(-2)
# ll.insert(2,25)
ll.listprint()
print('-------')
# ll.removeByValue(50)
# print(ll.removeByIndex(3))
# print(ll.removeByValue(0))
ll.reverse()
ll.listprint()

