#! /usr/bin/python
def factorial(n):
  fact = 1
  if(n == 0):
    return 1
  for i in range(1, n+1):
    fact *= i
  return fact

def factorialRecursion(n):
  fact = 1
  if(n == 0 or n == 1):
    return 1
  else:
    return n * factorialRecursion(n-1) 

def main():
  while(True):
    x = raw_input('Enter the number to find factorial of the number, Enter exit to quit: ')
    if x == "exit":
      break
    print factorial(int(x))
    print factorialRecursion(int(x))

if __name__ == "__main__":
  main()
