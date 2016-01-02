"""input=
1 
5"""

import sys

num_tests = sys.stdin.readline()

for i in num_tests:
    num = int(sys.stdin.readline())
    primeList = []
    for i in range(1,num+1):
        if num % i == 0:
            primeList.append(i)
    if len(primeList) == 2:
        print (True)
    else:
        print (False)

"""output = True"""
