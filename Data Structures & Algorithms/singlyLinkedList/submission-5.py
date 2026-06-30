class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        current = self.head
        i = 0
        while current:
            if i == index:
                return current.val
            else:
                current = current.next
                i +=1
        return -1

    def insertHead(self, val: int) -> None: 
        newHead = LinkedListNode(val)
        prevHead = self.head

        newHead.next = prevHead
        self.head = newHead

        
    def insertTail(self, val: int) -> None:
        node = LinkedListNode(val)

        # if list is empty, create node and set it as the head, then return
        if self.head is None:
            self.head = node
            return
        
        # set a pointer to the header, loop through to the end using the next property 
        current = self.head
        while current.next != None:
            current = current.next
        
        current.next = node
            

    def remove(self, index: int) -> bool:
        i = 0
        current = self.head
        prev = None

        while current:
            if i == index:
                if i == 0 and index == 0:
                    self.head = current.next
                    return True
                elif current.next:
                    prev.next = current.next
                    return True
                elif not current.next:
                    prev.next = None
                    return True
                else: 
                    return False
            else: 
                prev = current
                current = current.next
            i += 1
        return False


    def getValues(self) -> List[int]:
        vals = []
        current = self.head
        while current != None:
            vals.append(current.val)
            current = current.next
        return vals

