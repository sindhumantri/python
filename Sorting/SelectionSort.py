#! /usr/bin/python

def SelectionSort(listEle):
  for i in xrange(len(listEle)):
    min = i
    for j in xrange(i, len(listEle)):
      if listEle[j] < listEle[min]:
        min = j
    listEle[i], listEle[min] = listEle[min], listEle[i]

def main():
  listEle = [30, 20, 3, 1, 50, 60]
  SelectionSort(listEle)
  print listEle

if __name__ == "__main__":
  main()
