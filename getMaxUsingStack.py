"""Find max element in array using stack"""

class Stack:
    
    def __init__(self):
        self.stack = []
      
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1][0]
    
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()[0]
    
    def getMax(self):
        if len(self.stack) > 0:
            return self.stack[-1][1]
    
    def push(self, value):
        if len(self.stack) == 0:
            self.stack.append((value,value))
        else:
            maximum = self.stack[-1][1]
            if value > maximum:
                maximum = value
            self.stack.append((value, maximum))
    
    def isEmpty(self):
        return self.stack == []
        

l = Stack()
l.push(10)
l.push(20)
l.push(5)
l.push(25)
maxi = l.getMax()
print (maxi)
