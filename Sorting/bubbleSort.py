#! /usr/bin/python

def bubbleSort(list):
  for i in range(len(list)):
    for j in range(len(list) - 1):
      if list[j] > list[j+1]:
        list[j],list[j+1] = list[j+1],list[j]
   
def main():
  list = [8,7,12,4,9,6,5]
  bubbleSort(list)
  print list

if __name__ == "__main__":
  main()
