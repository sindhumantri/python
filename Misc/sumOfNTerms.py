input = """
1
5"""

import sys

num_tests = int(sys.stdin.readline())

for i in range(num_tests):
    n = int(sys.stdin.readline())
    sum = n * (n + 1) / 2
    print sum

output = """
15"""
