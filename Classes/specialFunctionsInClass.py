class Employee:
	
	employee_count = 0
	raise_amount = 1.04
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = self.first + self.last + "@gmail.com"
		Employee.employee_count += 1
		
	def emp_name(self):
		return "Employee name is: {} {}".format(self.first, self.last)
	
	def raise_pay(self):
		self.pay = self.pay * Employee.raise_amount
	
	#Class methods are the alternative constructors for the class
	@classmethod
	def emp_details(cls, emp_info):
		first, last, pay = emp_info.split("-")
		return cls(first, last, pay)
	
	@classmethod
	def set_raise_amount(cls, amount):
		cls.raise_amount = amount
	
	#Static variables which will not work on instance methods or class methods
	@staticmethod
	def is_weekday(day):
		if day == 5 or day == 6:
			return False
		return True
	
	#represents the class variables. Without the representation function 
	#def __repr__(self):
	#	return "{}, {}, {}".format(self.first, self.last, self.pay)
		
	#represents the class variables in string format
	#def __str__(self):
	#	return "{} - {}".format(self.emp_name(), self.email)
		
	#adds the variables in a class
	def __add__(self, other):
		return self.pay + other.pay
	
	#To find length of an object in a class 
	def __len__(self):
		return len(self.email)
		
emp1 = Employee("Sindhu", "Manch", 100000)
emp2 = Employee("Hemanth", "Mantri", 150000)
#print(Employee.__repr__(emp1))
#print(emp2)
#print(Employee.__str__(emp1))
#print(emp1 + emp2)
print(len(emp1))
