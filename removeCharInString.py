"""Input:
2
acbac
aababc

Output:

aaac"""

import sys
import re
num_test = sys.stdin.readline()

def isSubString(str1, str2):
    if str1 in str2:
        return True
    else:
        return False
        
for test in range(int(num_test)):
    str2 = sys.stdin.readline()
    if isSubString("b",str2) or isSubString("ac",str2):
        res = re.sub("b|ac", "", str2)
    print (res)
