class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubelLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.length+=1
            return
        
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.length+=1
        return

    def prepend(self, value):
        newNode=Node(value)
        if self.head is None:
            self.append(value)
            return
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode
        self.length+=1
        return

    def insert(self, index, value):
        newNode = Node(value)
        if self.head is None:
            return 'Empty List'
        if index == 0:
            self.prepend(value)
            return
        if index >= self.length:
            print('append',index,self.length)
            self.append(value)
            return
        
        i=0
        currentNode = self.head
        while currentNode:
            if i == index:
                prevNode = currentNode.prev
                newNode.prev = prevNode
                currentNode.prev = newNode
                newNode.next = currentNode
                currentNode = newNode
                prevNode.next = currentNode
                self.length+=1
            currentNode = currentNode.next
            i+=1
        return
    
    def removeByValue(self, valueToRemove):
        currentNode = self.head
        if self.length==0:
            self.data = None
            self.next = None
            self.prev = None
            return

        while currentNode:
            if currentNode.data == valueToRemove:
                # if the value is at first position
                if currentNode.prev is None:
                    self.head = currentNode.next
                    self.head.prev = None
                    currentNode.next = None
                    self.length-=1
                    return
                # if the value is at last
                if currentNode.next is None:
                    self.tail = currentNode.prev
                    self.tail.next = None
                    self.length-=1
                    return
                currentNode.prev.next = currentNode.next
                currentNode.next.prev = currentNode.prev
                self.length-=1
            currentNode = currentNode.next

    def removeByIndex(self, index):
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
        if index >= self.length:
            return 'Insert valid index'
        
        if index == self.length-1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length-=1
        i=0
        currentNode = self.head
        while currentNode:
            if i == index:
                currentNode.prev.next = currentNode.next
                currentNode.next.prev = currentNode.prev
                self.length-=1
                return
            currentNode = currentNode.next
            i+=1


    def reverse(self):
        self.tail = self.head
        ptr1 = self.head
        ptr2 = self.head.next

        ptr1.next = None
        ptr1.prev = ptr2

        while ptr2:
           ptr2.prev = ptr2.next
           ptr2.next = ptr1
           ptr1= ptr2
           ptr2=ptr2.prev
        self.head=ptr1
        return

    def printList(self):
        currentNode = self.head
        while currentNode is not None:
            print('currentNode',currentNode.data)
            if currentNode.prev:
                print('prev',currentNode.prev.data)
            if currentNode.next:
                print('next',currentNode.next.data)
            print('-------')
            currentNode=currentNode.next
        print('tail',self.tail.data, 'prev',self.tail.prev, self.tail.next,'totalength', self.length)

dll = DoubelLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)
# dll.prepend(-1)
# dll.insert(2,25)
# dll.removeByValue(50)
# dll.removeByIndex(3)
dll.reverse() 
dll.printList()