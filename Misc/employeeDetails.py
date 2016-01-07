import inspect
class Employee:
    empCount = 0
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    
    def printEmpDetails(self):
        print (self.name)
        print (self.salary)
    
    def printCount(self):
        return (Employee.empCount)
        

empD = Employee("sindhu", 100000)
empD1 = Employee("aaaaa", 10000)
empD.printEmpDetails()
empD1.printEmpDetails()
print (Employee.empCount)
print (hasattr(empD, "name"))
setattr(empD1, "name", "Hemanth")
empD1.printEmpDetails()
print (Employee.empCount)
print ("------Returning all functions in a class-------")
name_func_tuples = inspect.getmembers(Employee, inspect.isfunction)
functions = dict(name_func_tuples)
for keys in functions.keys():
    print (keys)


"""output:
xxxxx
100000
yyyyy
10000
2
True
Hemanth
10000
2
------Returning all functions in a class-------
__init__
printCount
printEmpDetails"""

