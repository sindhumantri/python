"""Count characters, newlines, and words in a string."""
import re
paragraph = '''alam was elected as the 11th President of India in 2002 with the support of both the ruling Bharatiya Janata Party and the then-opposition Indian National Congress. Widely referred to as the "People's President,"[6] he returned to his civilian life of education, writing and public service after a single term. He was a recipient of several prestigious awards, including the Bharat Ratna, India's highest civilian honour.'''

words = [word for word in paragraph.split(" ") if word.isalpha() == True or word.isalnum() == True]
specialWords = []
for word in paragraph.split(" "):
	res = re.findall(r"[A-Za-z]+[\,\.\'\,][a-z]*[\"\[0-9\]]*", word)
	if res != []:
		specialWords.append(res[0])

print(words)
print(specialWords)

"""Reverse a singly linked list."""

def reverseList(head):
	cur = head
	if cur == None:
		return 
	reverseList(cur.next)
	print(cur.value)

def reverseList1(head):
	l = LinkedList()
	cur = head
	while cur:
		l.insertAtHead(cur.value)
		cur = cur.next
	return l.head

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
		
class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
	
	def insertAtHead(self, value):
		newNode = Node(value)
		if self.head == None:
			self.head = newNode
			self.tail = newNode
		else:
			newNode.next = self.head
			self.head = newNode
	
	def insertAtTail(self, value):
		newNode = Node(value)
		if self.head == None:
			self.head = newNode
			self.tail = newNode
		else:
			self.tail.next = newNode
			self.tail = newNode
	
	def printList(self):
		cur = self.head
		while cur:
			print(cur.value)
			cur = cur.next

def pPrint(res):
	c = res
	while res:
		print(res.value)
		res = res.next

l = LinkedList()
l.insertAtTail(10)
l.insertAtTail(20)
l.insertAtTail(30)
l.insertAtTail(40)
#reverseList(l.head)
res = reverseList1(l.head)
pPrint(res)

"""Implement the Fibonacci series iteratively and recursively."""

def Fibonacci(n):
	if n == 1 or n == 0:
		return n
	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

def fibonacciIterative(n):
	l =[]
	if n== 0 or n==1:
		return n
	l.append(0)
	l.append(1)
	while n >= 2:
		sum = l[-1] + l[-2]
		a=l[-1]
		b = sum
		l.append(sum)
		n -= 1
	return l

print(fibonacciIterative(3))

"""Find the in-order successor of a node in a BST where each node has a parent pointer in addition to left/right child pointers."""
"""Note- 2 conditions for finding the successor
1. If the given node has right subtree:
	we have to find the leftmost node in the right subtree or find the min 
	in a right subtree
2. If the given node has no right subtree:
	we have to go right most subtree and find the deepest ancestor where 
	the given node is in right subtree
Note- We have to look at the ancestor only if the node no right subtree"""


class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

#Function to find the successor
class BinaryTree:
	def __init__(self):
		self.root = None
	
	def insertion(self, rt, newNode):
		if rt.val > newNode.val:
			if rt.left == None:
				rt.left = newNode
			else:
				self.insertion(rt.left, newNode)
		else:
			if rt.right == None:
				rt.right = newNode
			else:
				self.insertion(rt.right, newNode)
	
	def inOrder(self, rt):
		if rt == None:
			return
		self.inOrder(rt.left)
		print(rt.val)
		self.inOrder(rt.right)
	
	def search(self,rt,value):
		cur = rt
		if cur == None:
			return None
		elif cur.val == value:
			return cur
		elif cur.val > value:
			return self.search(cur.left, value)
		else:
			return self.search(cur.right, value)
	
	def findMin(self, rt):
		if rt == None:
			return None
		while rt.left != None:
			rt = rt.left
		return rt
		
	def findSuccessor(self, rt, value):
		current = self.search(rt, value)
		if current == None:
			return None
		# if the node has right subtree
		if current.right != None:
			return self.findMin(current.right)
		# if node has no right subtree
		else:
			successor = None
			ancestor = rt
			while current.val != ancestor.val:
				if current.val < ancestor.val:
					successor = ancestor
					ancestor = ancestor.left
				else:
					ancestor = ancestor.right
			return successor
			
		
b = BinaryTree()
b.root = Node(15)
b.insertion(b.root, Node(10))
b.insertion(b.root, Node(8))
b.insertion(b.root, Node(6))
b.insertion(b.root, Node(12))
b.insertion(b.root, Node(11))
b.insertion(b.root, Node(20))
b.insertion(b.root, Node(17))
b.insertion(b.root, Node(16))
b.insertion(b.root, Node(25))
b.insertion(b.root, Node(27))
b.inOrder(b.root)
print("----Search the node-----")
res = b.search(b.root, 12)
print(res.val)
print("-----Find Minimum-----")
res = b.findMin(b.root)
print(res.val)
print("---Find successor------")
res = b.findSuccessor(b.root, 15)
print(res.val)


"""Remove all occurrences of a value in a singly linked list."""

class Node:
	def __init__(self,val):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
	
	def insertAtTail(self, value):
		new_node = Node(value)
		if self.head == None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node
	
	def printList(self):
		cur = self.head
		while cur:
			print(cur.val)
			cur = cur.next
	
	def removeDuplicate(self):
		dupList = []
		cur = self.head
		prev = None
		while cur:
			if not cur.val in dupList:
				dupList.append(cur.val)
				prev = cur
			else:
				prev.next = cur.next
			cur = cur.next

	def removedup(self, prevNode, deleteNode):
		if prevNode == None:
			self.head = deleteNode.next
		else:
			prevNode.next = deleteNode.next
		del deleteNode
		
	def removeDuplicates(self):
		cur1 = self.head
		while cur1:
			prev = cur1
			cur2 = cur1.next
			while cur2:
				nextNode = cur2.next
				if cur2.val == cur1.val:
					removedup(prev, cur2)
				prev = cur2
				cur2 = nextNode
			cur1 = cur1.next
	

l = LinkedList()
l.insertAtTail(10)
l.insertAtTail(20)
l.insertAtTail(20)
l.insertAtTail(20)
l.insertAtTail(40)
l.insertAtTail(50)
l.removeDuplicate()
l.printList()
print("---------------")
l.removeDuplicates()
l.printList()
			
				
