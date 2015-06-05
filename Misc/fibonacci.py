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

print fibonacci_generate(5)
print fibonacci_iterative(5)
print fibonacci_recursive(5)
