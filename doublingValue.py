"""Input:
1
5 2
1 2 3 4 8

Output:
16"""

import sys

num_tests = int(sys.stdin.readline())
for test in range(num_tests):
    values = sys.stdin.readline().split(" ")
    n, b = int(values[0]), int(values[1])
    l = [int(i) for i in sys.stdin.readline().split(" ")]
    newVal = 0
    for i in range(n-1):
        if b in l:
            b = (b*b)
    print (b)
