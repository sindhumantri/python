#!/usr/bin/python

import multiprocessing


def processNumbers(numbers):
  j = 0
  print(numbers[j:j+2])

def processNumbers1(numbers):
  j = 2
  print(numbers[j:j+2])

def processNumbers2(numbers):
  j = 4
  print(numbers[j:j+2])

if __name__ == "__main__":
  l = ["a", "b", "c"]
  arr = [1, 2, 3, 4, 5, 6]
  l[0] = multiprocessing.Process(target=processNumbers, args=(arr,))
  l[1] = multiprocessing.Process(target=processNumbers1, args=(arr,))
  l[2] = multiprocessing.Process(target=processNumbers2, args=(arr,))
  l[0].start()
  l[1].start()
  l[2].start()
  l[0].join()
  l[1].join()
  l[2].join()
