class Employees:
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary
	
	def __repr__(self):
		return "({}, {}, ${})".format(self.name, self.age, self.salary)
	
e1 = Employees('Sindhu', 27, 100000)
e2 = Employees('Hemanth', 29, 150000)
e3 = Employees('Likith', 24, 90000)
emplyee = [e1,e2,e3]

def e_sort(emp):
	return emp.salary
	
my_emp = sorted(emplyee, key=e_sort, reverse=True)
print(my_emp)


my_emp = sorted(emplyee, key=lambda e:e.age)
print(my_emp)
