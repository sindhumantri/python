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

print(Employee.employee_count)

emp1 = Employee("Sindhu", "Manch", 100000)
emp2 = Employee("Hemanth", "Mantri", 150000)

print(emp1.email)
print(Employee.employee_count)
emp1.raise_pay()
print(emp1.pay)
print(Employee.emp_name(emp1))

print("-----Using class methods------")
#Using class methods to get the employee info
emp1_details = "Harika-kkk-34211"
emp2_details = "Harshitha-llll-23456"
emp3_details = "Karishma-rrrrr-432144"

e1 = Employee.emp_details(emp1_details)
print(e1.emp_name())

Employee.set_raise_amount(1.05)

print(e1.pay)

print("-----Using static methods----------")
#Using static methods in a class
import datetime
day = datetime.date(2016, 11, 5)
print(Employee.is_weekday(day))

print("-----Using Inheritence method------")
# Inheritence 

class Developer(Employee):
	#raise_amount = 1.30
	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang

class Manager(Employee):
	# Note: we should never declare the default value as a list or tuple
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees == None:
			self.employees = []
		else:
			self.employees = employees
			
	def add_emp(self, emp):
		if not emp in self.employees:
			self.employees.append(emp)
			

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)
	
	def print_emp(self):
		for e in self.employees:
			print(" {} under this manager {}".format(e.emp_name(), self.first))	
			

		
dev_1 = Developer("Sindhu", "Manch", 100000, "python")
dev_2 = Developer("Hemanth", "Mantri", 150000, "java")

#print(help(Developer))
#print(emp1.__dict__)
#print(dev_1.pay)
#dev_1.raise_pay()
#print(dev_1.pay)

#print(dev_1.prog_lang)

m = Manager("ken", "rubin", 200000, [dev_1])
m.add_emp(dev_1)
#m1 = Manager("ken", "rubin", 200000, [dev_2])
m.add_emp(dev_2)
m.print_emp()

# to check weather the class is instace of other class, we have to use isinstance function

print(isinstance(dev_1, Manager))
print(isinstance(m, Employee))

# to check weather the class is subclass or not there is a function called 
# issubclass

print(issubclass(Employee, Manager))
print(issubclass(Manager, Employee))
