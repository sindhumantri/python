"""input =1
5 10"""

import sys

num_tests = sys.stdin.readline()

for i in num_tests:
    ele = sys.stdin.readline().split()
    l = [int(i) for i in ele]
    a,b = l[0], l[1]
    if a > b:
        greater = a
    else:
        greater = b
    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += 1
    print (lcm)
  
"""output = 10 5""" 
