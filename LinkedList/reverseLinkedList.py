#! /usr/bin/python

class Node():
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

class singlyLinkedList():
  def __init__(self):
    self.head = None
    self.tail = None
   
  def insertAtHead(self, new_node):
    if self.head == None:
      # first node
      new_node.next = None
      self.head = new_node
      self.tail = new_node
    else:
      # more than one node
      new_node.next = self.head
      self.head = new_node
  
  def insertAtTail(self, new_node):
    if self.tail == None:
      new_node.next = None
      self.tail = new_node
      self.head = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
      
  def delete(self, value):
    cur_node = self.head
    prev_node = None
    while(cur_node):
      if cur_node.value == value:
        if cur_node == self.head:
          self.head = cur_node.next
        else:
          prev_node.next = cur_node.next
      prev_node = cur_node    
      cur_node = cur_node.next 
  
  def printL(self):
    cur_node = self.head
    while cur_node:
      print cur_node.value,
      cur_node = cur_node.next

def isIntersecting(nodeA, nodeB):
  curA = nodeA
  curB = nodeB
  new_list = []
  
  while curA:
    print "list 1 value %d" % curA.value
    new_list.append(curA)
    curA = curA.next
  
  while curB:
    print "list 2 value %d" % curB.value
    if curB in new_list:
      return True
    curB = curB.next 
  
  return False
  
def main():
  sl = singlyLinkedList()
  for i in range(0, 10):
    n = Node(i)
    sl.insertAtTail(n)
  sl.printL()
  
  sl2 = singlyLinkedList()
  cur = sl.head
  while cur:
    print "inserting cur value %d" % cur.value
    node = Node(cur.value)
    sl2.insertAtHead(node)
    cur = cur.next
  sl2.printL()
  print "asserting two lists" 
  n1 = Node(10)
  n2 = Node(20)
  n3 = Node(30)
  n4 = Node(40)
  n5 = Node(50)
  n6 = Node(60)
  s1 = singlyLinkedList()
  s1.insertAtTail(n1)
  s1.insertAtTail(n2)
  s1.insertAtTail(n3)
  s1.insertAtTail(n4)
  s2 = singlyLinkedList()
  s2.insertAtTail(n5)
  s2.insertAtTail(n6)
  #s2.insertAtTail(n3)
  #s2.insertAtTail(n4)
  assert(isIntersecting(s1.head, s2.head) == False)
  s2.insertAtTail(n3)
  s2.insertAtTail(n4)
  assert(isIntersecting(s1.head, s2.head))
  
if __name__ == "__main__":
  main()
