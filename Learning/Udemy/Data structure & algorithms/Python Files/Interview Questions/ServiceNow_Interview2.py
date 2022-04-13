# Interview2
# Remove the Nth node from the end of a LinkedList given the head of the linkedList. 
# 1,2,3,4,5
# 0 1 2 3 4
# n = 3

def removeNth(head, n):
    currNode=Node(0)
    len = 0
    while head:
        len+=1
        head = head.next
    
    target = len - n
    pointer = 0
    
    while head:
        if pointer == target -1:
            # remove
            temp = head.next.next
            if temp is None:
                head.next = None
            head.next = temp
            len-=1
        
        pointer+=1
        currNode.next = head
        currNode = currNode.next
        head = head.next
        
    return currNode.next