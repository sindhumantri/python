import sys

class Person:
    def __init__(self, pId):
        self.pId = pId
        self.pName = None
    
    def display(self):
        print ("persons name %s and id %d" % (self.pName, self.pId))
        
class Properties(Person):
    
    def __init__(self, pId, sYear, eYear):
        Person.__init__(self, pId)
        self.pId = pId
        self.sYear = None
        self.eYear = None

    def getProperty(self):
        self.sYear = int(input("Enter the Start year that you started earning salar: "))
        self.eYear = int(input("Enter the End year that you started earning salar: "))
        pProperties = []
        for i in range(self.sYear, self.eYear):
            salary = int(input("Enter your salary \(e.g- 50k\): "))
            fav = input("Enter your fav color: ")
            person = (self.pId,fav,salary,i)
            pProperties.append(person)
        return pProperties
        

p = Person(1)
p.pName = "sindhu"
p.display()
proper = Properties(2, 21, 25)
print (proper.getProperty())
