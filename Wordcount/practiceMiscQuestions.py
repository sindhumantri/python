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
