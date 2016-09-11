#! /usr/bin/python

def fibonacci_generate(number):
  list = []
  list.append(0)
  list.append(1)
  index = 2
  while(number > 2):
    num = list[index -1] + list[index -2]
    list.append(num)
    index +=1
    number -= 1
  return list

def fibonacci_iterative(number):
  f0 = 0
  f1 = 1
  if number == f0 or number == f1:
    return number
  while (number > 1):
    ans  = f0 + f1
    f0 = f1
    f1 = ans
    number -= 1
  return ans

def fibonacci_recursive(number):
  if number == 0 or number == 1:
    return number
  else:
    return fibonacci_recursive(number - 1) + fibonacci_recursive(number -2)

#Generator method of implementing Fibonacci

def fib():
    a,b = 1,1
    while 1:
        yield a
        a, b = b, a+b
        
counter = 0
for n in fib():
    print(n)
    counter += 1
    if counter == 10:
        break

print fibonacci_generate(5)
print fibonacci_iterative(5)
print fibonacci_recursive(5)
