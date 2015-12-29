class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def findKthToLastElement(self, position):
        fast = self.head
        slow = self.head
        while position:
            fast = fast.next
            position = position-1
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        return slow.value
        
    def insertAtTail(self, ele):
        if type(ele) == Node:
            new_node = ele
        else:
            new_node = Node(ele)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def printList(self):
        cur = self.head
        while cur:
            print (cur.value)
            cur = cur.next

lList = LinkedList()
lList.insertAtTail(20)
lList.insertAtTail(30)
lList.insertAtTail(40)
lList.insertAtTail(50)
lList.insertAtTail(60)
lList.insertAtTail(80)
lList.insertAtTail(70)
lList.printList()
print ("------Print kth Position from the last--------")
kthelement = lList.findKthToLastElement(3)
print (kthelement)

                    
    
