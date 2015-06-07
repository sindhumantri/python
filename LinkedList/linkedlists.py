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
   
  def insert(self, value):
    new_node = Node(value)
    if self.head == None:
      # First Node  
      self.head = new_node
      self.tail = new_node
    else:
      # more than one node
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

class doublyLinkedList():
  def __init__(self):
    self.head = None
    self.tail = None

  def insert(self, value):
    new_node = Node(value)
    if self.head == None:
      # First Node  
      self.head = new_node
      self.tail = new_node
    else:
      # more than one node
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
      
  def delete(self, value):
    cur_node = self.head
    while(cur_node):
      if cur_node.value == value:
        if cur_node.prev is not None:
          # not first node
          cur_node.prev.next = cur_node.next
          if cur_node.next :
            cur_node.next.prev = cur_node.prev
          if cur_node == self.tail:
            self.tail = cur_node.prev
        else:
          # first node
          self.head = cur_node.next
          self.head.prev = None
      cur_node = cur_node.next
  
  def printList(self):
    cur_node = self.head
    while cur_node:
      print cur_node.value,
      cur_node = cur_node.next
    print
  
  def printRev(self):
    cur_node = self.tail
    while cur_node:
      print cur_node.value,
      cur_node = cur_node.prev
    print 
          
def main():
  sl = singlyLinkedList()
  sl.insert(10) 
  sl.insert(30)
  sl.insert(40)
  sl.insert(50)
  sl.insert(20)
  sl.insert(10)
  sl.insert(50)
  sl.printL()
  sl.delete(30)
  sl.printL()
  sl.delete(20)  
  sl.printL()
  sl.delete(50)
  sl.printL()
  sl.delete(40)
  sl.printL()
  sl.delete(10)
  sl.printL()
  dl = doublyLinkedList()
  dl.insert(10)
  dl.insert(40)
  dl.insert(20)
  dl.printList()
  dl.printRev()
  dl.delete(10)
  dl.printList()
  dl.delete(40)
  dl.printList()

if __name__ == "__main__":
  main()
