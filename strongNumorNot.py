import sys

num_tests = sys.stdin.readline()

def factorial(num):
    if num == 1 or num == 0:
        return num
    else:
        return num * factorial(num-1)

for test in range(int(num_tests)):
    num = sys.stdin.readline().strip()
    factors = [factorial(int(i)) for i in list(num)]
    sumOfFactors = sum(factors)
    if sumOfFactors == int(num):
        print ("Strong")
    else:
        print ("Not Strong")


"""
Input:
2
145
10

Output:
Strong
Not Strong"""
