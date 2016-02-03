"""{([])}"""
import re
def parenthesisChecker(s):
    BRACES = { '(': ')', '[': ']', '{': '}' }
    stack = []
    for b in s:
        #print (b)
        c = BRACES.get(b)
        if c:
            stack.append(c)
        elif not stack or stack.pop() != b:
            return False
    return not stack
BRACES = { '(': ')', '[': ']', '{': '}' }

print (parenthesisChecker("{"))
    
