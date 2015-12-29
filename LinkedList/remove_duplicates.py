class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def deleteDupNode(self):
        cur1 = self.head
        prev = None
        while cur1:
            prev = cur1
            cur2 = cur1.next
            while cur2:
                nextNode = cur2.next
                if cur2.value == cur1.value:
                    self.delete(prev, cur2)
                prev = cur2
                cur2 = nextNode
            cur1 = cur1.next
    
    def delete(self, prev, deleteNode):
        if prev == None:
            self.head = deleteNode.next
        else:
            prev.next = deleteNode.next
        del deleteNode
        
    def deleteNode(self, delNode):
        cur = self.head
        prev = None
        while cur:
            if cur == delNode:
                if prev == None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                del cur
                break
            prev = cur
            cur = cur.next

    def removeDupSinglyLL(self):
        dupList = []
        cur = self.head
        prev = None
        while cur:
            if not cur.value in dupList:
                dupList.append(cur.value)
                prev = cur
            else:
                prev.next = cur.next
            cur = cur.next
    
    def insertAtHead(self, ele):
        if type(ele) == Node:
            new_node = ele
        else:
            new_node = Node(ele)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            
    def printList(self):
        cur = self.head
        while cur:
            print (cur.value)
            cur = cur.next

lList = LinkedList()
lList.insertAtHead(10)
lList.insertAtHead(20)
lList.insertAtHead(10)
lList.insertAtHead(10)
lList.insertAtHead(40)
lList.printList()
#print ("------Remove Duplicates in Singly Linked List--------")
#lList.removeDupSinglyLL()
#lList.printList()
print ("------Remove Duplicates without Temperary List--------")
lList.deleteDupNode()
lList.printList()
                    
    
