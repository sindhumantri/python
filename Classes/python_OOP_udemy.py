"""class Student():
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.balance = 0
		self.credit = 50

s = Student('Sindhu', 26)
print(s.balance)
print(s.credit)

class myclass():
	def test(self):
		print("wlecome")
		print(self)
		
this = myclass()
this.test()
print(this)

class myclass1(object):
	class_value = "my class value"
d = myclass1()
print(d.class_value)

d.class_value = "Sindhu Manch"
print(d.class_value)

del d.class_value
print(d.class_value)"""


class Student1:
	def __init__(self, name):
		self.name = name
		self.marks = []
		print("wlecome {} to the school".format(name))
		
	def addmarks(self,mark):
		self.marks.append(mark)
		
	def average(self):
		x = sum(self.marks)
		return x/len(self.marks)

s1 = Student1("sindhu")
print(s1.name)
s1.addmarks(20)
s1.addmarks(25)
s1.addmarks(25)
s1.addmarks(26)
print(s1.marks)
print(s1.average())


class animal:
	def __init__(self, name):
		self.name = name
	
	def eat(self, food):
		print("{} animal eats {}".format(self.name, food))

class dog(animal):
	def fetch(self, thing):
		print("{} animal eats {}".format(self.name, thing))

class cat(animal):
	def cat_name(self):
		print("{} animal eats {}".format(self.name))

d = dog('dog')
d.fetch('cat')
