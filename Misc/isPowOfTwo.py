#code
import sys

num_tests = int(sys.stdin.readline())

while num_tests:
    num = int(sys.stdin.readline())
    for i in range(num):
        value = pow(2,i)
        if num == value:
            print "YES"
        else:
            print "NO"
        break
    num_tests -= 1
