#! /usr/bin/python
class Node:
	def __init__(self,value):
		self.value = value
		self.next = None
		self.prev = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		
	def printList(self, Node=None):
		if Node == None:
			return None
		else:
			cur = Node
			while cur:
				print(cur.value)
				cur = cur.next

def insert(head, data):
	l = LinkedList()
	#check whether type of data is node or a value
	if type(data) == Node:
		new_node = data
	else:
		new_node = Node(data)
	if head == None:
		head = new_node
	else:
		#Insert at tail
		l.printList(new_node)
		head.next = new_node
		#Insert at head
		#new_node.next = head
		#head = new_node
	return head
	
l = LinkedList()
a1 = Node(20)
a2 = Node(30)
a3 = Node(40)
h1 = insert(a1,20)
h2 = insert(h1,30)
h3 = insert(h2,40)
l.printList(h3)
